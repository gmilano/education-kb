#!/bin/bash
cd /home/user/education-kb
R=scratchpad/p928/raw-hits.tsv
K=scratchpad/p928/known-slugs-lc.txt
# unique repos across sweep
awk -F'\t' '{print tolower($1)"\t"$0}' "$R" | sort -u -t$'\t' -k1,1 | cut -f2- > scratchpad/p928/uniq-hits.tsv
# unheld
awk -F'\t' 'NR==FNR{k[$1];next}{ if (!(tolower($1) in k)) print }' "$K" scratchpad/p928/uniq-hits.tsv > scratchpad/p928/unheld.tsv
echo "rows_total=$(wc -l < $R)  unique=$(wc -l < scratchpad/p928/uniq-hits.tsv)  unheld=$(wc -l < scratchpad/p928/unheld.tsv)"
# yield by page depth: for every (leg,page) count how many rows are unheld
awk -F'\t' 'NR==FNR{k[tolower($1)];next}{p=$9; tot[p]++; if(!(tolower($1) in k)) unh[p]++}END{for(i=1;i<=10;i++) if(tot[i]) printf "page %2d\ttotal %5d\tunheld %5d\t%.1f%%\n", i, tot[i], unh[i], 100*unh[i]/tot[i]}' "$K" "$R"
