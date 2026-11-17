#!/bin/bash
# p862 -- 861-G2: the LATAM assessment vocabulary, run for the first time in this base.
# Reports total_count per term and the top hits by stars, so a nil is a MEASURED nil.
set -u
printf 'term\tqualifier\ttotal_count\ttop_hits_by_stars\n'
run(){
  t="$1"; q="$2"
  full="$t $q"
  tot=$(gh api -X GET search/repositories -f q="$full" -f per_page=1 --jq '.total_count' 2>/dev/null)
  [ -z "$tot" ] && tot='ERR'
  hits=$(gh api -X GET search/repositories -f q="$full" -f sort=stars -f order=desc -f per_page=5 \
        --jq '[.items[]|"\(.full_name)(\(.stargazers_count)★)"]|join(" · ")' 2>/dev/null)
  [ -z "$hits" ] && hits='-'
  printf '%s\t%s\t%s\t%s\n' "$t" "$q" "$tot" "$hits"
  sleep 3
}
for t in '"corrección automática"' '"correção automática"' 'autocorrección' 'rúbrica' '"corretor automático"' 'banca' 'prova'; do
  run "$t" ''
  run "$t" 'stars:>5'
done
