#!/bin/sh
# Is a carried star claim's correctness a function of WHERE on the page it sits?
# Split each page at its midpoint and compare verdicts head vs tail.
V=verdict.2026-10-11.tsv
printf '%-26s %-6s %-34s %s\n' page lines 'HEAD (top half)' 'TAIL (bottom half)'
for p in agents/top.md repos/foundations.md verticals/solutions.md intel/market.md intel/trends.md compose/patterns.md; do
  f=../../../$p
  total=$(wc -l < "$f")
  mid=$((total/2))
  head_s=$(awk -F'\t' -v p="$f" -v m="$mid" '$3==p && $4<=m{c[$1]++} END{printf "E%d/D%d/W%d", c["EXACT"], c["DRIFT"], c["WRONG"]}' $V)
  tail_s=$(awk -F'\t' -v p="$f" -v m="$mid" '$3==p && $4>m{c[$1]++} END{printf "E%d/D%d/W%d", c["EXACT"], c["DRIFT"], c["WRONG"]}' $V)
  printf '%-26s %-6s %-34s %s\n' "$p" "$total" "$head_s" "$tail_s"
done
echo
echo "All WRONG and DRIFT cells, with position as a fraction of page length:"
for p in agents/top.md repos/foundations.md verticals/solutions.md intel/market.md intel/trends.md compose/patterns.md; do
  f=../../../$p; total=$(wc -l < "$f")
  awk -F'\t' -v p="$f" -v t="$total" -v n="$p" '$3==p && $1!="EXACT"{printf "%-7s %-42s %-24s L%-6s %3d%% of page  claimed=%-8s measured=%s\n", $1, $5, n, $4, ($4*100)/t, $6, $7}' $V
done
