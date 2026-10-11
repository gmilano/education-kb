#!/bin/sh
# p120 ACTION L - test p119's claim that wrong cells live in the page TAIL.
# p119 found all 7 of its wrong STAR cells below 78 % page depth and
# pre-registered a tail re-measurement. ACTION J's 17 LICENCE defects are a
# second, independent sample of the same pages, so they test the hypothesis
# without a new measurement: if depth predicts wrongness, these should cluster
# in the tail too.
set -u
printf '%-10s %-22s %-7s %-7s %-7s %s\n' verdict page line lines depth slug
awk -F'\t' '$1=="OVERSTATED"||$1=="UNGRANTED"' score.2026-10-11.tsv | while IFS="$(printf '\t')" read -r v pg ln slug rest; do
  total=$(wc -l < "/home/user/education-kb/$pg")
  d=$(awk -v l="$ln" -v t="$total" 'BEGIN{printf "%.1f", (l/t)*100}')
  printf '%-10s %-22s %-7s %-7s %-7s %s\n' "$v" "$pg" "$ln" "$total" "$d%" "$slug"
done
