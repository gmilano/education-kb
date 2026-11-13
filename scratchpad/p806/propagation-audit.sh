#!/usr/bin/env bash
# p806 propagation audit — education-kb
# Structural defect recorded at p805: the two append-only trending logs
# (agents/trending.md, repos/trending.md) are >140k lines combined, so a
# repository can be byte-verified in the log and never reach a file a studio
# reads. This script makes that diff repeatable instead of manual.
#
# Usage: bash scratchpad/p806/propagation-audit.sh
set -uo pipefail
cd "$(dirname "$0")/../.." || exit 1
OUT="scratchpad/p806"; mkdir -p "$OUT"

TRENDING="agents/trending.md repos/trending.md"
SHELF="agents/top.md repos/foundations.md verticals/solutions.md compose/patterns.md intel/market.md intel/trends.md intel/open-gaps.md intel/measured-unusable.md README.md"

slugs() { grep -ohiE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' $1 2>/dev/null \
  | sed 's#.*github\.com/##' | sed 's/[.,)]*$//' | tr 'A-Z' 'a-z' | sort -u; }

slugs "$TRENDING" > "$OUT/trending-slugs.txt"
slugs "$SHELF"    > "$OUT/shelf-slugs.txt"

# A slug counts as VERIFIED only where its own line in a trending log carries a
# green mark AND an explicit verification or license token. This is the signal
# p805 audited by hand.
grep -hiE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' $TRENDING \
  | grep '🟢' \
  | grep -iE 'payload-verified|byte-verified|MIT|Apache-2\.0|BSD|ISC|CC BY 4\.0' \
  | grep -ohiE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' \
  | sed 's#.*github\.com/##' | sed 's/[.,)]*$//' | tr 'A-Z' 'a-z' | sort -u \
  > "$OUT/verified-slugs.txt"

comm -23 "$OUT/verified-slugs.txt" "$OUT/shelf-slugs.txt" > "$OUT/unpropagated-verified.txt"
comm -23 "$OUT/trending-slugs.txt" "$OUT/shelf-slugs.txt" > "$OUT/unpropagated-all.txt"

printf 'trending slugs (all)        : %s\n' "$(wc -l < "$OUT/trending-slugs.txt")"
printf 'shelf slugs                 : %s\n' "$(wc -l < "$OUT/shelf-slugs.txt")"
printf 'verified-in-log slugs       : %s\n' "$(wc -l < "$OUT/verified-slugs.txt")"
printf 'UNPROPAGATED (verified)     : %s\n' "$(wc -l < "$OUT/unpropagated-verified.txt")"
printf 'unpropagated (all, context) : %s\n' "$(wc -l < "$OUT/unpropagated-all.txt")"
