#!/usr/bin/env bash
# ACTION AI -- the false-permissive question, asked of all 86 non-standard
# -default addresses rather than of the 79 that happen to carry a grant.
#
# WHY THE DENOMINATOR MATTERS. p124's gold set required a readable grant on
# the REAL default branch, which quietly excludes the worst case: a repository
# whose real default carries NO grant while a surviving `main`/`master`
# carries a permissive one. There, guessing does not return a wrong licence --
# it returns a licence where there is none. Seven of the 86 are in exactly
# that position and none of them was scored.
#
# usage: false_permissive.sh NONSTD_TSV CACHE_DIR > probe.tsv
#   NONSTD_TSV: address <TAB> real-default-branch
# output: address <TAB> branch <TAB> which(real|main|master) <TAB> path
#         <TAB> bytes <TAB> token
set -uo pipefail
IN="$1"; CACHE="$2"; mkdir -p "$CACHE"

PATHS="${PATHS:-LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt COPYING COPYING.txt LICENSE.rst LICENSE-CODE LICENSE-MIT LICENSE-APACHE license.txt license.md}"

probe() {
  local addr="$1" br="$2" which="$3" p url code sz out
  for p in $PATHS; do
    url="https://raw.githubusercontent.com/${addr}/${br}/${p}"
    code="$(curl -sI -o /dev/null -w '%{http_code}' --max-time 20 "$url" 2>/dev/null)"
    if [ "$code" = "200" ]; then
      out="${CACHE}/$(printf '%s' "$addr" | tr '/' '~')__${which}__$(printf '%s' "$p" | tr '/' '~')"
      curl -sL -o "$out" --max-time 25 "$url" 2>/dev/null
      sz="$(wc -c <"$out" | tr -d ' ')"
      printf '%s\t%s\t%s\t%s\t%s\n' "$addr" "$br" "$which" "$p" "$sz"
      return 0
    fi
  done
  printf '%s\t%s\t%s\t-\t0\n' "$addr" "$br" "$which"
  return 0
}
export -f probe
export CACHE PATHS

# Three rows per address: the real default, then `main` and `master` as a
# branch-guessing probe would request them. `main` and `master` are requested
# even when one of them IS the real default, because the point is to measure
# what GUESSING returns, not what resolving returns.
awk -F'\t' '{print $1"\t"$2"\treal"; print $1"\tmain\tmain"; print $1"\tmaster\tmaster"}' "$IN" \
| xargs -P 12 -n 3 bash -c 'probe "$0" "$1" "$2"'
