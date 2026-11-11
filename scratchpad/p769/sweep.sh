#!/usr/bin/env bash
# p769 supply sweep. ACTION p767-A (per-language) + ACTION p768-A (orthography pairs).
set -u
OUT=scratchpad/p769
: > $OUT/counts.tsv
: > $OUT/cands.tsv
while IFS='|' read -r LANG Q; do
  [ -z "${Q:-}" ] && continue
  R=$(gh api -X GET search/repositories -f q="$Q" -f per_page=20 -f sort=stars 2>/dev/null)
  if [ -z "$R" ]; then printf '%s\t%s\tERR\n' "$LANG" "$Q" >> $OUT/counts.tsv; continue; fi
  N=$(printf '%s' "$R" | jq -r '.total_count // "ERR"')
  printf '%s\t%s\t%s\n' "$LANG" "$Q" "$N" >> $OUT/counts.tsv
  printf '%s' "$R" | jq -r --arg l "$LANG" --arg q "$Q" \
    '.items[]? | [$l,$q,.full_name,(.stargazers_count|tostring),(.license.spdx_id//"NONE"),(.pushed_at//"-"),((.description//"")|gsub("[\t\n]";" ")|.[0:120])] | @tsv' \
    >> $OUT/cands.tsv
done < $OUT/queries.txt
echo "queries: $(wc -l < $OUT/counts.tsv)  rows: $(wc -l < $OUT/cands.tsv)"
