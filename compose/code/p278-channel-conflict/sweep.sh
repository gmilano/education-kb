#!/usr/bin/env bash
# p278 — the ONLINE half of the CONFLICT class: read BOTH channels for each slug, at a
# pinned SHA, and let `direction.py` decide the verdict.
#
# WHY THIS IS A SCRIPT AND NOT A TABLE.  `p121` built this census BY HAND on 2026-10-11 --
# 249 addresses, 161 manifests, 10 contradictions -- and the result was a published table
# with a typed verdict per row.  It has never been re-run.  A one-off census answers "was
# there a conflict on 11 October"; a studio needs "is there one now, on the ref I am about
# to vendor".  That is the `p228 -> p229` move the Makefile's own header describes, applied
# to the channel axis.
#
# STAYS OUT OF `make hooks` (needs egress).  The OFFLINE half is `conflict_gate.py`.
#
#   usage: ./sweep.sh <slugs-file> > out.tsv
#      or: ./sweep.sh < <slugs-file> > out.tsv
#
# 🔴 SELF-INFLICTED, MEASURED ON THE FIRST RUN: the first cut documented a FILE ARGUMENT and
# implemented a `while read` over STDIN, copying `enumerate.sh`'s stdin shape while keeping
# its own `<slugs-file>` usage line.  Run under `nohup`, stdin is `/dev/null`, so the sweep
# emitted its header, read zero slugs and exited 0 -- a GREEN run over an empty input.
# 🔵 That is `p252`'s silent-zero class (`ACTION XR`) arriving in a harvester instead of a
# suite, so the remedy is the same: the input is resolved explicitly AND an empty read is a
# non-zero exit, because a sweep that measured nothing must not look like a sweep that found
# nothing.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/../lib/probe_payload.sh"

MANIFESTS="package.json pyproject.toml composer.json Cargo.toml pom.xml"

_raw_at() { curl -sS --max-time "${PROBE_TIMEOUT:-25}" \
    "https://raw.githubusercontent.com/$1/$2/$3" 2>/dev/null; }

_is404() { head -1 "$1" 2>/dev/null | grep -q '^404: Not Found$'; }

# Normalise a DECLARED licence string onto a family name.  The declared field is already
# SPDX-ish in most ecosystems, so this is mostly a passthrough; the mapped cases are the
# spellings that are NOT SPDX and would otherwise arrive UNPLACEABLE.
_norm_decl() {
  local d; d=$(printf '%s' "$1" | tr -d '"' | sed -E 's/^[[:space:]]+|[[:space:]]+$//g')
  case "$(printf '%s' "$d" | tr 'A-Z' 'a-z')" in
    "mit license"|"mit licence"|mit)                echo "MIT" ;;
    "apache license 2.0"|"apache-2"|"apache 2.0")   echo "Apache-2.0" ;;
    "bsd license"|bsd)                              echo "BSD" ;;
    "isc license"|isc)                              echo "ISC" ;;
    "gpl-3.0+"|"gplv3"|"gpl v3")                    echo "GPL-3.0" ;;
    "agpl-3.0+"|"agplv3"|"agpl v3")                 echo "AGPL-3.0" ;;
    "")                                             echo "-" ;;
    *)                                              echo "$d" ;;
  esac
}

# Pull the declared licence out of one manifest body, per ecosystem.
_decl_from() { # _decl_from <manifest-name> <file>
  local name="$1" f="$2" v=""
  case "$name" in
    package.json|composer.json)
      v=$(grep -oE '"license"[[:space:]]*:[[:space:]]*"[^"]*"' "$f" | head -1 \
          | sed -E 's/.*:[[:space:]]*"([^"]*)".*/\1/')
      # composer.json may carry an ARRAY of licences; take the first.
      [ -z "$v" ] && v=$(grep -oE '"license"[[:space:]]*:[[:space:]]*\[[[:space:]]*"[^"]*"' "$f" \
          | head -1 | sed -E 's/.*"([^"]*)"$/\1/')
      ;;
    pyproject.toml|Cargo.toml)
      v=$(grep -oE '^[[:space:]]*license[[:space:]]*=[[:space:]]*"[^"]*"' "$f" | head -1 \
          | sed -E 's/.*"([^"]*)".*/\1/')
      # PEP 621 table form: license = { text = "MIT" }
      [ -z "$v" ] && v=$(grep -oE 'license[[:space:]]*=[[:space:]]*\{[^}]*text[[:space:]]*=[[:space:]]*"[^"]*"' "$f" \
          | head -1 | sed -E 's/.*"([^"]*)".*/\1/')
      # Trove classifier, which is how older Poetry projects say it.
      [ -z "$v" ] && v=$(grep -oE '"License :: OSI Approved :: [^"]*"' "$f" | head -1 \
          | sed -E 's/.*Approved :: ([^"]*)".*/\1/')
      ;;
    pom.xml)
      # The FIRST <licenses><license><name> only.  A pom may also list a PARENT's or a
      # dependency's licence further down; taking the first <name> after <licenses> is the
      # project's own.  `p260`'s foreign-manifest guard is the same concern one layer out.
      v=$(tr -d '\n' < "$f" | grep -oE '<licenses>.*?</licenses>' | head -1 \
          | grep -oE '<name>[^<]*</name>' | head -1 | sed -E 's|</?name>||g')
      ;;
  esac
  _norm_decl "$v"
}

printf 'slug\tdefault_ref\thead_sha\tpayload_path\tpayload_bytes\tpayload_family\tmanifest_path\tmanifest_declares\tverdict\tseverity\tnote\n'

# Resolve the input ONCE, explicitly: a file argument if given, otherwise stdin.
if [ "$#" -ge 1 ]; then
  exec < "$1"
fi

SEEN=0
while read -r slug; do
  [ -z "${slug// }" ] && continue
  case "$slug" in \#*) continue;; esac
  SEEN=$((SEEN + 1))

  br=$(probe_default_branch "$slug")
  if [ -z "$br" ]; then
    printf '%s\t-\t-\t-\t0\tUNRESOLVED\t-\t-\tNO-CHANNEL\tGREY\tslug did not resolve\n' "$slug"
    sleep 1; continue
  fi
  sha=$(GIT_TERMINAL_PROMPT=0 timeout 45 git ls-remote "https://github.com/$slug" HEAD 2>/dev/null \
        | awk '/HEAD/{print substr($1,1,12); exit}')

  # ---- payload channel
  p_path="-"; p_bytes=0; p_fam="-"
  for fn in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt License license LICENSE-MIT; do
    t=$(mktemp); _raw_at "$slug" "$br" "$fn" > "$t"
    if [ -s "$t" ] && ! _is404 "$t"; then
      p_path="$fn"; p_bytes=$(wc -c < "$t" | tr -d ' '); p_fam=$(family_of_file "$t")
      rm -f "$t"; break
    fi
    rm -f "$t"
  done

  # ---- manifest channel
  m_path="-"; m_decl="-"
  for mf in $MANIFESTS; do
    t=$(mktemp); _raw_at "$slug" "$br" "$mf" > "$t"
    if [ -s "$t" ] && ! _is404 "$t"; then
      d=$(_decl_from "$mf" "$t")
      if [ -n "$d" ] && [ "$d" != "-" ]; then m_path="$mf"; m_decl="$d"; rm -f "$t"; break; fi
      # A manifest that EXISTS and declares nothing is recorded as such: that is `p276`'s
      # `pupilfirst` shape (`"private": true`, no licence field) and it is NOT an absence
      # of the manifest channel.
      [ "$m_path" = "-" ] && m_path="$mf(no-licence-field)"
    fi
    rm -f "$t"
  done

  read -r verdict severity note < <(python3 -I "$HERE/direction.py" "$m_decl" "$p_fam" \
      | awk -F'\t' '{print $1, $2, $3}')
  note=$(python3 -I "$HERE/direction.py" "$m_decl" "$p_fam" | cut -f3)

  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$br" "${sha:--}" "$p_path" "$p_bytes" "$p_fam" "$m_path" "$m_decl" \
    "$verdict" "$severity" "$note"
  sleep 1   # the session git proxy caps concurrent smart-HTTP ops; serialise deliberately
done

# 🔴 An empty sweep is a FAILURE, not a clean result.  See the header: the first run of this
# script read zero slugs and exited 0.
if [ "$SEEN" -eq 0 ]; then
  echo "🔴 sweep.sh read ZERO slugs — input was empty or unreadable (pass a file, or redirect stdin)" >&2
  exit 1
fi
