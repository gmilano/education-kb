#!/usr/bin/env bash
# ACTION AE -- build a gold set that CONTAINS branch disagreements, so the
# MAIN-ONLY model can be scored honestly.
#
# WHY. p123 measured the `MAIN-ONLY` model at 0 % error and said so, then
# noted in the same breath that the gold set it used could not see the defect:
# every gold row's default branch WAS `main` or `master`, so guessing the
# branch and resolving it gave identical answers by construction. A model
# scored only where it cannot fail scores perfectly and means nothing.
#
# This builds the complement. Gold rows are the addresses whose real default
# branch is NEITHER `main` NOR `master` and which carry a readable grant
# there -- exactly the population where guessing can be wrong. For each, the
# same grant path is probed on `main` and on `master`, and the MAIN-ONLY
# answer is whatever that guessing probe returns.
#
# usage: gold_branch.sh HEADS_ALL_TSV HITS_TSV CACHE_DIR > gold.tsv
# output: address <TAB> real-branch <TAB> path <TAB> real-token
#         <TAB> mainonly-branch|NONE <TAB> mainonly-token|NO-FILE <TAB> verdict
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
HEADS="$1"; HITS="$2"; CACHE="$3"
mkdir -p "$CACHE/ae"

# The gold population: a non-standard default branch AND a grant file on it.
awk -F'\t' '$2=="EXISTS" && $3!="main" && $3!="master"{print $1"\t"$3}' "$HEADS" \
  | sort -u > "$CACHE/ae/nonstd.tsv"
join -t$'\t' -1 1 -2 1 \
  <(sort -t$'\t' -k1,1 "$CACHE/ae/nonstd.tsv") \
  <(awk -F'\t' '{print $1"\t"$3}' "$HITS" | sort -t$'\t' -k1,1 -u) \
  > "$CACHE/ae/gold-candidates.tsv"      # addr <TAB> real-branch <TAB> path

probe() {
  local addr="$1" real="$2" p="$3" code tok br="NONE" out
  for guess in main master; do
    code="$(curl -sI -o /dev/null -w '%{http_code}' --max-time 20 \
           "https://raw.githubusercontent.com/${addr}/${guess}/${p}" 2>/dev/null)"
    if [ "$code" = "200" ]; then br="$guess"; break; fi
  done
  if [ "$br" = "NONE" ]; then
    tok="NO-FILE"
  else
    out="${CACHE}/ae/$(printf '%s' "$addr" | tr '/' '~')__${br}__$(printf '%s' "$p" | tr '/' '~')"
    curl -sL -o "$out" --max-time 25 \
      "https://raw.githubusercontent.com/${addr}/${br}/${p}" 2>/dev/null
    tok="$(python3 -I "${HERE}/classify_licence.py" "$p" < "$out")"
  fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$addr" "$real" "$p" "$br" "$tok"
  return 0
}
export -f probe
export CACHE HERE

awk -F'\t' '{print $1"\t"$2"\t"$3}' "$CACHE/ae/gold-candidates.tsv" \
  | xargs -P 12 -n 3 bash -c 'probe "$0" "$1" "$2"'
