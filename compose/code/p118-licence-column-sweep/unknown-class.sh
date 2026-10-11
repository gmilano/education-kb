#!/usr/bin/env bash
# P118. The 18 addresses classify2.sh returns UNKNOWN for are not one failure
# mode but four, and naming them is worth more than a bare "unread" count.
set -u
awk -F'\t' '$4=="UNKNOWN"{print $1"\t"$2"\t"$3}' measured2.2026-10-11.tsv | while IFS=$'\t' read -r slug br p; do
  f="streams2/$(printf '%s' "$slug" | tr '/' '%')@$br@$p"
  [ -f "$f" ] || { printf '%s\tMISSING-STREAM\t-\n' "$slug"; continue; }
  sz=$(wc -c < "$f" | tr -d ' ')
  if   grep -qiE 'LICEN[CÇ]A P[UÚ]BLICA|LICENCIA P[UÚ]BLICA|GENERALE PUBBLICA|ALLGEMEINE [ÖO]FFENTLICHE' "$f"; then
       cls="NON-ENGLISH-GRANT"; note=$(grep -oiE 'AFFERO|LESSER|GERAL|GENERAL' "$f" | head -1)
  elif grep -qiE 'Elastic License|Business Source License|Server Side Public License|Commons Clause|PolyForm' "$f"; then
       cls="SOURCE-AVAILABLE-NOT-OSS"; note=$(head -1 "$f" | tr -d '\r')
  elif [ "$sz" -lt 200 ] && grep -qiE '^(YEAR|COPYRIGHT HOLDER)' "$f"; then
       cls="GRANT-IN-MANIFEST"; note="$sz B field stub; licence named in DESCRIPTION/manifest"
  elif grep -qiE 'licensed as follows|usa duas licen|is licensed under \[|two licen|duas licen' "$f"; then
       cls="MULTI-GRANT-PROSE-INDEX"; note=$(head -1 "$f" | tr -d '#\r' | sed 's/^ *//')
  else cls="STILL-UNCLASSIFIED"; note=$(head -1 "$f" | tr -d '\r' | cut -c1-60)
  fi
  printf '%s\t%s\t%s\n' "$slug" "$cls" "$note"
done
