#!/bin/bash
K=/home/user/education-kb
TSV="$K/evidence/edtech-band-50-400.2026-10-28-p499.tsv"
OUT=residual-promotion.2026-10-28-p500.tsv
printf "repo\tstars\tlicence_api\tpushed\tpermissive\tlive_2026\ton_shelf_now\tp499_said\tshelf_files\ttrending_mentions\n" > $OUT
awk -F'\t' 'NR>1{print $1"\t"$2"\t"$3"\t"$5"\t"$8}' "$TSV" | while IFS=$'\t' read -r repo stars lic pushed p499said; do
  sh=""
  for f in agents/top.md repos/foundations.md verticals/solutions.md; do
    grep -q "$repo" "$K/$f" 2>/dev/null && sh="$sh$(basename $f),"
  done
  [ -z "$sh" ] && on=no || on=yes
  tm=$(( $(grep -c "$repo" "$K/agents/trending.md" 2>/dev/null) + $(grep -c "$repo" "$K/repos/trending.md" 2>/dev/null) ))
  case "$lic" in MIT|Apache-2.0|BSD-3-Clause|BSD-2-Clause) perm=yes;; *) perm=no;; esac
  case "$pushed" in 2026-*) live=yes;; *) live=no;; esac
  printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "$repo" "$stars" "$lic" "$pushed" "$perm" "$live" "$on" "$p499said" "${sh:-NONE}" "$tm" >> $OUT
done
