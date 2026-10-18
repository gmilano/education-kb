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
# 🔴 p279 (`p278`'s declared item 2) — THIS SCRIPT RE-COMMITTED THE ERROR IT WAS BUILT TO
# CORRECT.  `p278` left one defect standing and named it: the manifest channel read ROOT
# manifests only, so `ls1intum/Athena` returned `NO-CHANNEL` while `p275` had already
# established that **12 of its 14 manifests declare MIT**, every one of them in a
# subdirectory.  *"A monorepo declares its grant per package"* is `p275`'s own sentence, and
# the instrument built to enforce `p275`'s lesson probed exactly one path.
# 🔵 A ladder of one rung is still a ladder, which is `p275`'s whole finding: the manifest
# channel is ENUMERATED from the tree now, never guessed, over the same blobless-clone
# channel `enumerate.sh` proved -- and NOT `api.github.com`, which is 403 from this session
# and has been for five passes.
# 🟢 It also makes visible a class a root-only read cannot see at all: a repository whose
# SUBPACKAGES disagree with each other (`declared_distinct` > 1).  A studio vendoring one
# directory of a monorepo gets THAT directory's grant, not the root's.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/../lib/probe_payload.sh"
# `is_bundled` — the SHARED vendored-path predicate (P441).  A `node_modules/*/package.json`
# declares a DEPENDENCY's licence, never the repository's; `p260`'s foreign-manifest guard is
# the same concern, and this is its existing implementation rather than a second one.
. "$HERE/../lib/licence_path.sh"

MANIFESTS="package.json pyproject.toml composer.json Cargo.toml pom.xml"
# Bound the walk.  A monorepo with hundreds of packages is a cost problem, not a licence
# problem: the first `MANIFEST_CAP` non-vendored manifests in path order answer "does this
# repository declare a grant per package", and what was SKIPPED is published, so the bound
# is never invisible.  14 is `Athena`'s own manifest count -- the control case fits exactly.
# 🟢 p280 (`p279`'s declared item 3): THE CAP WAS THE CONTROL CASE'S OWN COUNT.  14 is
# `Athena`'s manifest count, and `leemonade/leemons` has 114 -- so its published
# "12 declaring" was 12 OF THE FIRST 14 READ, with 100 skipped.  A bound set to the size of
# the example is not a bound on the corpus.  The cost it bounds is one
# `raw.githubusercontent.com` GET per manifest; 250 covers every tree this base has
# enumerated (max 114, measured) and `manifests_skipped` is still published, so a tree that
# exceeds it still says so instead of looking complete.
# 🔵 MEASURED after raising it: `leemons` reads 114 of 114, `0` skipped --
# `evidence/package-provenance.2026-10-18-p280.tsv`.
MANIFEST_CAP="${MANIFEST_CAP:-250}"
PYBIN="${PYBIN:-python3}"

# Enumerate every non-vendored manifest path in the tree.  Same channel as `enumerate.sh`:
# a blobless shallow clone yields the full path list without fetching a single blob.
_manifest_paths() { # _manifest_paths <slug>
  local slug="$1" d all p base
  d="$(mktemp -d)"
  if ! GIT_TERMINAL_PROMPT=0 timeout 240 git clone --depth 1 --filter=blob:none \
         --no-checkout --quiet "https://github.com/$slug" "$d" >/dev/null 2>&1 </dev/null; then
    rm -rf "$d"; return 1
  fi
  all="$(git -C "$d" ls-tree -r --name-only HEAD 2>/dev/null)"
  rm -rf "$d"
  # Root manifests sort first, so the chosen row stays the root's when a root grant exists:
  # the verdict column does not change meaning for any row already published.
  while IFS= read -r p; do
    [ -z "$p" ] && continue
    base="${p##*/}"
    case " $MANIFESTS " in *" $base "*) ;; *) continue ;; esac
    is_bundled "$p" && continue
    printf '%s\t%s\n' "$(awk -F/ '{print NF-1}' <<< "$p")" "$p"
  done <<< "$all" | sort -k1,1n -k2,2 | cut -f2
}

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

# p279 APPENDS its four columns rather than replacing any: every `channel-conflict.*.tsv`
# already in `evidence/` stays readable against this header, and a diff between a p278 row
# and a p279 row is a diff in the MEASUREMENT, not in the schema.
# p280 APPENDS two columns for the same reason p279 appended four: every earlier
# `channel-conflict.*.tsv` stays readable against this header, so a diff between a p279 row
# and a p280 row is a diff in the MEASUREMENT.
printf 'slug\tdefault_ref\thead_sha\tpayload_path\tpayload_bytes\tpayload_family\tmanifest_path\tmanifest_declares\tverdict\tseverity\tnote\tmanifests_in_tree\tmanifests_declaring\tdeclared_distinct\tmanifests_skipped\tmanifests_foreign\troot_manifest_name\tmanifests_thirdparty\tthirdparty_paths\n'

# Resolve the input ONCE, explicitly: a file argument if given, otherwise stdin.
# 🔴 p279, MEASURED: the slug list is read on FD 3, not stdin.  With the per-package walk
# added, `git clone` inside the loop body CONSUMED THE REST OF THE LIST from stdin -- the
# sweep processed 10 of 14 slugs and still exited 0, because `while read` simply saw EOF.
# 🔵 That is this script's own silent-zero class again (`p252`/`ACTION XR`), and the header
# above already records it arriving once: an empty read was made fatal, but a TRUNCATED read
# was not.  A sweep that measured PART of its input must not look like a sweep that measured
# all of it, so the count is asserted against the input at the end.
if [ "$#" -ge 1 ]; then
  exec 3< "$1"
else
  exec 3<&0
fi

SEEN=0
while read -r slug <&3; do
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

  # ---- manifest channel, ENUMERATED PER PACKAGE (p279)
  m_path="-"; m_decl="-"; m_in_tree=0; m_declaring=0; m_skipped=0; m_distinct="-"
  m_fallback=""; m_foreign=0; m_rootname="-"; m_thirdparty=0; tp_paths=""
  declared_list=""
  # 🔵 Capture the status ONCE.  Distinguishing "the tree has no manifest" from "the clone
  # failed" matters -- `p278` could not tell them apart, and they are different findings:
  # the first is a real absence of the channel, the second is an instrument that did not
  # measure -- but re-running the clone to find out would pay twice for one answer.
  paths="$(_manifest_paths "$slug")"; clone_rc=$?
  if [ "$clone_rc" -ne 0 ]; then
    m_path="CLONE_FAIL"
  elif [ -n "$paths" ]; then
    m_in_tree=$(printf '%s\n' "$paths" | grep -c .)
    n=0
    while IFS= read -r mf; do
      [ -z "$mf" ] && continue
      n=$((n + 1))
      if [ "$n" -gt "$MANIFEST_CAP" ]; then m_skipped=$((m_skipped + 1)); continue; fi
      t=$(mktemp); _raw_at "$slug" "$br" "$mf" > "$t"
      if [ -s "$t" ] && ! _is404 "$t"; then
        # 🔴 THE THIRD DEFECT IN THIS WALK, and the one that would have shipped a wrong
        # answer rather than a missing one.  Enumerating manifests per package counts a
        # monorepo's VENDORED dependency manifests as the repository's own declarations:
        # `tadreeblms` returned `13 declaring`, of which ten are `moment`, `swiper`,
        # `tailwindcss`, `prismjs` and three CKEditor builds under `public/assets/libs/`,
        # and `open-tutor-ai-CE`'s second "declaration" is a bundled `pyodide`.
        #
        # 🔴 AND THE FIRST FIX FOR IT WAS A MISUSE OF A CORRECT PREDICATE, measured on
        # `Athena`: applying `T229-M2`'s NAME check at every depth rejected **12 of
        # Athena's 14** manifests as foreign, because `T229-M2` asks *"is this ROOT
        # manifest UPSTREAM's?"* -- and a workspace package (`assessment_module_manager`)
        # has no reason whatever to carry its repository's name.  The predicate is right
        # for the depth it was built for and wrong one layer down: this pass's `is_bundled`
        # lesson, repeated against a different shared predicate within the same hour.
        #
        # 🟢 So each depth is asked the question it can answer:
        #   depth 0  -> `T229-M2` by NAME: a root manifest naming another project is a fork
        #               serving upstream's file (`openmage/magento-lts`).
        #   depth >0 -> the PATH predicate alone: a subpackage manifest is the repository's
        #               own unless it sits in a vendored directory.
        # 🔴 AND THE SECOND FIX WAS WRONG TOO -- as a REJECTION.  Used as a gate, the
        # name check marked FOUR root manifests foreign that plainly are not:
        # `mcp-canvas-lms` names its package `canvas-mcp-server`, `open-source-curriculum`
        # names it `course-content-player`, `Studivexa` names it
        # `student-management-backend`.  **Naming a package differently from its repository
        # is ordinary and legitimate**, and `T229-M2` was validated on names that are
        # ANOTHER KNOWN PROJECT (`laravel/laravel`, `openmage/magento-lts`) -- an upstream
        # skeleton served at a fork's root.  A name that is merely DIFFERENT is not that.
        # 🔴 `p229`'s own positive control for `mcp-canvas-lms` passes on the payload
        # `{"name":"@dmontgomery40/mcp-canvas-lms"}`, which **the repository does not
        # serve** -- the control was written against an invented manifest, so it could not
        # have caught this.  Registered for `p280`.
        # 🟢 So the name is RECORDED, not enforced: a differing root name is a flag for
        # adjudication, which is how `p229` actually used it, and the vendoring exclusion
        # rests on the PATH predicate, which is controlled and was widened this pass.
        # 🟢 p280 (`p279`'s declared item 1): THE DECLARED-PROVENANCE CHANNEL.  `p279`
        # registered this as "a list of known third-party projects, which this base does
        # not have" -- and the residual it named, `ui/static/pyodide/package.json`, needs
        # no list: it declares `"repository": "https://github.com/pyodide/pyodide"` and
        # `"homepage"` the same, in its own bytes.  A subpackage manifest that names
        # ANOTHER repository is vendored; at the ROOT the same difference is only recorded,
        # because `p436` measured three innocent causes for it and `p279` a fourth.
        # 🔵 Both halves of the channel were already on this base's shelf
        # (`lib/package_repo.sh::normalise_repo_url`, `p436-fork-hypothesis`), so
        # `pass280-package-provenance/provenance.py` imports them rather than writing a
        # third parser.  Coverage is bounded and published: 24 of 192 manifests across
        # these 14 slugs declare a repository at all (12.5 %), and ONE of those 24 is the
        # residual no path vocabulary could reach.
        if $PYBIN -I "$HERE/../pass280-package-provenance/provenance.py" \
             --row "$slug" "$br" "$mf" "$t" 2>/dev/null \
             | awk -F'\t' '$8=="THIRD-PARTY" || $8=="THIRD-PARTY-NAMED"{found=1} END{exit !found}'; then
          m_thirdparty=$((m_thirdparty + 1))
          tp_paths="${tp_paths:+$tp_paths,}$mf"
          rm -f "$t"; continue
        fi
        if [ "$(awk -F/ '{print NF-1}' <<< "$mf")" -eq 0 ]; then
          m_rootname=$($PYBIN -I "$HERE/../p229-grant-ladder-reach/manifest_grant.py" \
            --attributable "$slug" "${mf##*/}" "$t" 2>/dev/null) || m_foreign=$((m_foreign + 1))
        fi
        d=$(_decl_from "${mf##*/}" "$t")
        if [ -n "$d" ] && [ "$d" != "-" ]; then
          m_declaring=$((m_declaring + 1))
          declared_list="$declared_list$d"$'\n'
          # The FIRST DECLARING manifest in root-first path order is the row's chosen
          # channel, so a row whose root declares keeps the verdict it was published with.
          [ "$m_decl" = "-" ] && { m_path="$mf"; m_decl="$d"; }
        else
          # A manifest that EXISTS and declares nothing is recorded as such: that is
          # `p276`'s `pupilfirst` shape (`"private": true`, no licence field) and it is NOT
          # an absence of the manifest channel.
          # 🔴 SECOND DEFECT, measured on `Athena` and not read: this marker used to claim
          # the chosen slot via `[ "$m_path" = "-" ]`, so the root's SILENCE shadowed the
          # twelve subpackages that do declare -- the walk found all 14 manifests, graded 12
          # of them, and still published `NO-CHANNEL`.  Enumerating the paths is only half
          # the fix; the SELECTION has to prefer a grant over a silence, or the root-only
          # verdict survives the walk that was built to replace it.  The marker is a
          # fallback now and is only consulted when nothing declared.
          [ -z "$m_fallback" ] && m_fallback="$mf(no-licence-field)"
        fi
      fi
      rm -f "$t"
    done <<< "$paths"
    if [ -n "$declared_list" ]; then
      m_distinct=$(printf '%s' "$declared_list" | sort -u | grep -c .)
    fi
    # Nothing in the tree declared: NOW the no-licence-field marker is the honest answer.
    [ "$m_decl" = "-" ] && [ -n "$m_fallback" ] && m_path="$m_fallback"
  fi

  read -r verdict severity note < <(python3 -I "$HERE/direction.py" "$m_decl" "$p_fam" \
      | awk -F'\t' '{print $1, $2, $3}')
  note=$(python3 -I "$HERE/direction.py" "$m_decl" "$p_fam" | cut -f3)

  # 🔴 The intra-repo disagreement class, which a root-only read cannot see AT ALL: a
  # studio vendoring one directory of a monorepo gets THAT directory's grant.
  if [ "$m_distinct" != "-" ] && [ "$m_distinct" -gt 1 ] 2>/dev/null; then
    note="$note; SUBPACKAGES DISAGREE ($m_distinct distinct declarations)"
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$br" "${sha:--}" "$p_path" "$p_bytes" "$p_fam" "$m_path" "$m_decl" \
    "$verdict" "$severity" "$note" \
    "$m_in_tree" "$m_declaring" "$m_distinct" "$m_skipped" "$m_foreign" "${m_rootname:--}" \
    "$m_thirdparty" "${tp_paths:--}"
  sleep 1   # the session git proxy caps concurrent smart-HTTP ops; serialise deliberately
done

# 🔴 An empty sweep is a FAILURE, not a clean result.  See the header: the first run of this
# script read zero slugs and exited 0.
if [ "$SEEN" -eq 0 ]; then
  echo "🔴 sweep.sh read ZERO slugs — input was empty or unreadable (pass a file, or redirect stdin)" >&2
  exit 1
fi
# 🔴 And a PARTIAL read is a failure too, for the same reason: p279 lost 4 of 14 slugs to a
# subprocess eating stdin and the exit status was 0.  When the input is a FILE its slug count
# is knowable, so it is checked rather than trusted.
if [ "$#" -ge 1 ]; then
  WANT=$(grep -v "^[[:space:]]*#" "$1" | grep -c "[^[:space:]]")
  if [ "$SEEN" -ne "$WANT" ]; then
    echo "🔴 sweep.sh read $SEEN of $WANT slugs — the input was TRUNCATED, not exhausted" >&2
    exit 1
  fi
fi
