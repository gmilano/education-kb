#!/usr/bin/env bash
# p218: the corrected live/historical test. p216 used `^## ` and 364 of 1 349 level-2 headings
# on these shelves are NOT pass boundaries (compose/patterns.md 114, intel/market.md 64).
# Usage: pass_boundary.sh <file> <line>   -> prints "LIVE" or "HISTORICAL <heading>"
set -uo pipefail
f=$1; l=$2
h=$(awk -v L="$l" 'NR<=L && /^## (Pass |[0-9]{4}-)/{h=$0; n=NR} END{if(h) print "l."n": "h}' "$f")
if [ -n "$h" ]; then echo "HISTORICAL  $h"; else echo "LIVE"; fi
