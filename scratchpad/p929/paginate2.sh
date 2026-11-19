#!/bin/bash
# p928 - pagination sweep: 927-R1 asked for the backlog measured to the bottom.
OUT=scratchpad/p928/raw-hits2.tsv
LEGLOG=scratchpad/p928/leg-pages2.tsv
: > "$OUT"; : > "$LEGLOG"
while IFS= read -r q; do
  [ -z "$q" ] && continue
  page=1; tc=-1; got=0
  while :; do
    resp=$(gh api -X GET search/repositories -f q="$q" -f per_page=100 -f page=$page 2>/dev/null)
    if [ -z "$resp" ]; then echo -e "$q\t$page\tERROR\t0\t0" >> "$LEGLOG"; sleep 4; break; fi
    [ "$tc" = "-1" ] && tc=$(echo "$resp" | jq -r '.total_count // 0')
    n=$(echo "$resp" | jq -r '.items | length')
    echo "$resp" | jq -r --arg leg "$q" --arg pg "$page" '.items[] | [(.full_name),(.stargazers_count|tostring),(.license.spdx_id // "NOLICENSE"),(.pushed_at[0:10]),(.created_at[0:10]),((.archived)|tostring),((.description//"")|gsub("[\t\n\r]";" ")),$leg,$pg] | @tsv' >> "$OUT"
    got=$((got+n))
    echo -e "$q\t$page\t$tc\t$n\t$got" >> "$LEGLOG"
    [ "$n" -lt 100 ] && break
    page=$((page+1))
    [ "$page" -gt 10 ] && break
    sleep 2.2
  done
  sleep 2.2
done < scratchpad/p928/queries2.txt
echo "SWEEP DONE rows=$(wc -l < $OUT) legs=$(cut -f1 $LEGLOG | sort -u | wc -l)"
