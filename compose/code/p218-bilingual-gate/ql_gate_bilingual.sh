#!/usr/bin/env bash
# p218 ACTION QP: ACTION QL's precondition, made bilingual.
# Usage: ql_gate_bilingual.sh <concept-or-literal> [...]
# For each argument: if it names a concept in bilingual_tokens.tsv, grep BOTH columns.
# Otherwise grep the literal in both the EN form given and (unchanged) as a slug.
# Exit 1 if ANY language half returns a hit -> the absence claim is REFUTED.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
TBL="$(dirname "$0")/bilingual_tokens.tsv"
SHELVES=(agents/top.md agents/trending.md repos/foundations.md repos/trending.md \
         verticals/solutions.md intel/market.md intel/trends.md compose/patterns.md)
rc=0
for arg in "$@"; do
  row=$(awk -F'\t' -v c="$arg" '$1==c{print $2"\t"$3}' "$TBL")
  if [ -n "$row" ]; then
    en=$(printf '%s' "$row" | cut -f1); es=$(printf '%s' "$row" | cut -f2)
  else
    en="$arg"; es="$arg"
  fi
  for lang in EN:"$en" ES:"$es"; do
    tag=${lang%%:*}; pat=${lang#*:}
    n=$(cd "$ROOT" && grep -Eic -- "$pat" "${SHELVES[@]}" 2>/dev/null | awk -F: '{s+=$2} END{print s+0}')
    printf '%s\t%s\t%s\t%s\n' "$arg" "$tag" "$pat" "$n"
    [ "$n" -gt 0 ] && rc=1
  done
done
exit $rc
