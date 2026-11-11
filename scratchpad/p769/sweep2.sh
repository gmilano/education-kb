#!/usr/bin/env bash
set -u
OUT=scratchpad/p769
: > $OUT/counts2.tsv; : > $OUT/cands2.tsv
while IFS='|' read -r LANG Q; do
  [ -z "${Q:-}" ] && continue
  R=$(gh api -X GET search/repositories -f q="$Q" -f per_page=20 -f sort=stars 2>/dev/null)
  if [ -z "$R" ]; then printf '%s\t%s\tERR\n' "$LANG" "$Q" >> $OUT/counts2.tsv; continue; fi
  printf '%s\t%s\t%s\n' "$LANG" "$Q" "$(printf '%s' "$R" | jq -r '.total_count // "ERR"')" >> $OUT/counts2.tsv
  printf '%s' "$R" | jq -r --arg l "$LANG" --arg q "$Q" \
    '.items[]? | [$l,$q,.full_name,(.stargazers_count|tostring),(.license.spdx_id//"NONE"),(.pushed_at//"-"),((.description//"")|gsub("[\t\n]";" ")|.[0:110])] | @tsv' >> $OUT/cands2.tsv
done < $OUT/q2.txt
awk -F'\t' '{printf "%-3s %-42s %s\n",$1,$2,$3}' $OUT/counts2.tsv
