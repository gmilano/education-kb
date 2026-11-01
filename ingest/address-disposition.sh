#!/usr/bin/env bash
# address-disposition.sh — shell-only replica of `ingest/address-ledger.py --debt`
# disposition logic. Registered as the remedy for gap 583-C: the Python ledger is
# denied in the cloud harness ("Code from External", the 576-G per-invocation
# denial), so the FILED / UNFILED / NEW split that belongs in front of every
# prescribed sweep (gap 583-A) must be runnable with nothing but shell + grep.
#
# Usage:  ingest/address-disposition.sh <file-of-owner/name-per-line>
#         ingest/address-disposition.sh -   # read addresses from stdin
#
# Output: TSV  disposition <TAB> address <TAB> curated_hits <TAB> history_hits
#   FILED   = appears on at least one CURATED page  -> already shelved
#   UNFILED = appears ONLY in append-only history   -> owned but never shelved
#   NEW     = appears nowhere in the base
#
# Run from the repository root.

set -uo pipefail

CURATED=(agents/top.md repos/foundations.md verticals/solutions.md
         intel/market.md intel/trends.md compose/patterns.md)
HISTORY=(agents/trending.md repos/trending.md intel/open-gaps.md README.md)

src="${1:-}"
[ -z "$src" ] && { echo "usage: $0 <addr-file>|-" >&2; exit 2; }

# archive/ is history too, when present
mapfile -t ARCH < <(find archive -name '*.md' 2>/dev/null)

f=0; u=0; n=0
while IFS= read -r addr; do
  addr="$(printf '%s' "$addr" | tr -d '[:space:]')"
  [ -z "$addr" ] && continue
  # match the address as a literal token; -F avoids regex surprises in owner names
  c=$(grep -F -o -- "$addr" "${CURATED[@]}" 2>/dev/null | wc -l)
  h=$(grep -F -o -- "$addr" "${HISTORY[@]}" "${ARCH[@]+${ARCH[@]}}" 2>/dev/null | wc -l)
  if   [ "$c" -gt 0 ]; then d=FILED;   f=$((f+1))
  elif [ "$h" -gt 0 ]; then d=UNFILED; u=$((u+1))
  else                      d=NEW;     n=$((n+1))
  fi
  printf '%s\t%s\t%s\t%s\n' "$d" "$addr" "$c" "$h"
done < <(if [ "$src" = "-" ]; then cat; else cat "$src"; fi)

printf '#\tFILED=%s\tUNFILED=%s\tNEW=%s\n' "$f" "$u" "$n" >&2
