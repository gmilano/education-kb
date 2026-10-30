#!/usr/bin/env bash
# claim-role.sh — p543. Grades a CLAIM (not an address) against the committed
# tree and returns p541's roles, because "already held" and "already filed" are
# different verdicts and only the second licenses a pass to stop (p542).
#
#   FILED   — present in a curated NON-trending page (the shelf a reader lands on)
#   HISTORY — present only in a trending log or the gap register (529-A debt)
#   ABSENT  — nowhere in the tree
#
# USAGE  ./claim-role.sh <<< $'label\tgrep-pattern'   (TSV on stdin, -F fixed)
set -uo pipefail
FILED_PAGES=(agents/top.md repos/foundations.md verticals/solutions.md \
             intel/market.md intel/trends.md compose/patterns.md)
HIST_PAGES=(agents/trending.md repos/trending.md intel/open-gaps.md)
printf 'label\tpattern\trole\tfiled_hits\thist_hits\n'
while IFS=$'\t' read -r label pat; do
  [ -z "${pat:-}" ] && continue
  f=$(grep -F -c -e "$pat" "${FILED_PAGES[@]}" 2>/dev/null | awk -F: '{s+=$2} END{print s+0}')
  h=$(grep -F -c -e "$pat" "${HIST_PAGES[@]}"  2>/dev/null | awk -F: '{s+=$2} END{print s+0}')
  if   [ "$f" -gt 0 ]; then role=FILED
  elif [ "$h" -gt 0 ]; then role=HISTORY
  else role=ABSENT; fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$label" "$pat" "$role" "$f" "$h"
done
