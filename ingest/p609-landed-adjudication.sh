#!/usr/bin/env bash
# p609 — adjudicates 607-C's open item: ledger rows whose verdict is LANDED but which sit on no
# SELL shelf. Hypothesis under test: they landed on a TRENDING shelf. Result: all 50 did; 0 lost.
#
# 609-L NOTE — read this before changing the dedupe. An earlier draft of this script deduplicated on
# the (slug, verdict) PAIR, which silently reported 225 "distinct slugs" against 607-C's 219. The
# 6-row difference was not a normalisation disagreement: it is 6 slugs carrying TWO verdicts
# (LANDED and MOVED) across ledger rows. Dedupe on the SLUG and collect the verdicts into one cell,
# so a conflict is visible as data instead of inflating the denominator.
#
# Emits TSV: slug  verdicts  sell_hits  trending_hits  disposition
set -u
L=evidence/promotion-ledger.2026-10-25-p436.tsv
SELL="agents/top.md repos/foundations.md verticals/solutions.md"
TREND="agents/trending.md repos/trending.md"
printf 'slug\tverdicts\tsell\ttrending\tdisposition\n'
awk -F'\t' 'NR>1&&$1!=""{s=tolower($1); v[s]=(index(v[s],$8)?v[s]:v[s]"/"$8)}
            END{for(k in v) print k"\t"substr(v[k],2)}' "$L" | sort | while IFS=$'\t' read -r slug verd; do
  s=0; t=0
  for f in $SELL;  do n=$(grep -ciF "$slug" "$f" 2>/dev/null); s=$((s+n)); done
  for f in $TREND; do n=$(grep -ciF "$slug" "$f" 2>/dev/null); t=$((t+n)); done
  if   [ "$s" -gt 0 ]; then d=ON-SELL-SHELF
  elif [ "$t" -gt 0 ]; then d=TRENDING-ONLY
  else                      d=ON-NO-SHELF
  fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$verd" "$s" "$t" "$d"
done
