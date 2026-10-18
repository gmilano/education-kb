#!/usr/bin/env bash
# pass280 — the ONLINE half: for every non-vendored manifest in a slug's tree, record what
# the manifest says about WHOSE manifest it is.  One blobless clone per slug for the paths,
# one raw read per manifest for the payload.  Stays out of `make hooks`.
#
#   usage: ./measure.sh <slugs-file> > out.tsv
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/../lib/probe_payload.sh"
. "$HERE/../lib/licence_path.sh"

MANIFESTS="package.json pyproject.toml composer.json Cargo.toml pom.xml"
# 🔴 p279 item 3: `p278`/`p279`'s walk caps at 14 and `leemonade/leemons` has 114 manifests,
# so its published "12 declaring" is 12 OF THE FIRST 14 READ.  The cap exists to bound COST,
# and the cost it bounds is one `raw.githubusercontent.com` GET per manifest -- so the bound
# belongs where the corpus is, not at the control case's own count.  250 covers every tree
# this base has enumerated (max 114) and the SKIPPED count is still published, so a tree that
# exceeds it still says so instead of looking complete.
MANIFEST_CAP="${MANIFEST_CAP:-250}"

_raw_at() { curl -sS --max-time "${PROBE_TIMEOUT:-25}" \
    "https://raw.githubusercontent.com/$1/$2/$3" 2>/dev/null; }
_is404() { head -1 "$1" 2>/dev/null | grep -q '^404: Not Found$'; }

_manifest_paths() { # <slug> -> root-first path order, vendored paths excluded
  local slug="$1" d all p base
  d="$(mktemp -d)"
  if ! GIT_TERMINAL_PROMPT=0 timeout 240 git clone --depth 1 --filter=blob:none \
         --no-checkout --quiet "https://github.com/$slug" "$d" >/dev/null 2>&1 </dev/null; then
    rm -rf "$d"; return 1
  fi
  all="$(git -C "$d" ls-tree -r --name-only HEAD 2>/dev/null)"
  rm -rf "$d"
  while IFS= read -r p; do
    [ -z "$p" ] && continue
    base="${p##*/}"
    case " $MANIFESTS " in *" $base "*) ;; *) continue ;; esac
    is_bundled "$p" && continue
    printf '%s\t%s\n' "$(awk -F/ '{print NF-1}' <<< "$p")" "$p"
  done <<< "$all" | sort -k1,1n -k2,2 | cut -f2
}

printf 'slug\tref\tpath\tdepth\tbytes\tdeclared_name\tdeclared_repo\tverdict\treason\tdeclares_licence\n'
SEEN=0
if [ "$#" -ge 1 ]; then exec 3< "$1"; else exec 3<&0; fi
while read -r slug <&3; do
  [ -z "${slug// }" ] && continue
  case "$slug" in \#*) continue;; esac
  SEEN=$((SEEN + 1))
  br=$(probe_default_branch "$slug")
  if [ -z "$br" ]; then
    printf '%s\t-\t-\t-\t0\t-\t-\tUNRESOLVED\tslug did not resolve\t-\n' "$slug"; continue
  fi
  paths="$(_manifest_paths "$slug")" || { printf '%s\t%s\t-\t-\t0\t-\t-\tCLONE_FAIL\ttree not enumerated\t-\n' "$slug" "$br"; continue; }
  n=0
  while IFS= read -r mf; do
    [ -z "$mf" ] && continue
    n=$((n + 1))
    if [ "$n" -gt "$MANIFEST_CAP" ]; then
      printf '%s\t%s\t%s\t-\t0\t-\t-\tSKIPPED\tbeyond MANIFEST_CAP=%s\t-\n' "$slug" "$br" "$mf" "$MANIFEST_CAP"
      continue
    fi
    t=$(mktemp); _raw_at "$slug" "$br" "$mf" > "$t"
    if [ ! -s "$t" ] || _is404 "$t"; then
      printf '%s\t%s\t%s\t-\t0\t-\t-\tUNREADABLE\tpath in tree, raw read empty or 404\t-\n' "$slug" "$br" "$mf"
      rm -f "$t"; continue
    fi
    python3 -I "$HERE/provenance.py" --row "$slug" "$br" "$mf" "$t"
    rm -f "$t"
  done <<< "$paths"
  sleep 1
done
[ "$SEEN" -eq 0 ] && { echo "🔴 measure.sh read ZERO slugs" >&2; exit 1; }
if [ "$#" -ge 1 ]; then
  WANT=$(grep -v "^[[:space:]]*#" "$1" | grep -c "[^[:space:]]")
  [ "$SEEN" -ne "$WANT" ] && { echo "🔴 measure.sh read $SEEN of $WANT slugs — TRUNCATED" >&2; exit 1; }
fi
exit 0
