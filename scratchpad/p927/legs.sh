#!/bin/bash
# p927 - topic vocabulary extension leg runner
OUT=scratchpad/p927/raw-hits.tsv
: > "$OUT"
LEGLOG=scratchpad/p927/leg-counts.tsv
: > "$LEGLOG"
while IFS= read -r q; do
  [ -z "$q" ] && continue
  resp=$(gh api -X GET search/repositories -f q="$q" -f per_page=100 2>/dev/null)
  if [ -z "$resp" ]; then echo -e "$q\tERROR\t0" >> "$LEGLOG"; sleep 3; continue; fi
  tc=$(echo "$resp" | jq -r '.total_count // 0')
  n=$(echo "$resp" | jq -r '.items | length')
  echo "$resp" | jq -r --arg leg "$q" '.items[] | [(.full_name), (.stargazers_count|tostring), (.license.spdx_id // "NOLICENSE"), (.pushed_at[0:10]), (.created_at[0:10]), ((.archived)|tostring), ((.description//"")|gsub("[\t\n\r]";" ")), $leg] | @tsv' >> "$OUT"
  echo -e "$q\t$tc\t$n" >> "$LEGLOG"
  sleep 2.5
done < scratchpad/p927/queries.txt
echo "DONE rows=$(wc -l < $OUT)"
