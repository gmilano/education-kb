#!/bin/bash
set -u
printf 'query\ttotal_count\ttop_10_by_stars\n'
q(){
  tot=$(gh api -X GET search/repositories -f q="$1" -f per_page=1 --jq '.total_count' 2>/dev/null); [ -z "$tot" ] && tot=ERR
  h=$(gh api -X GET search/repositories -f q="$1" -f sort=stars -f order=desc -f per_page=10 --jq '[.items[]|"\(.full_name)(\(.stargazers_count))"]|join(" · ")' 2>/dev/null); [ -z "$h" ] && h='-'
  printf '%s\t%s\t%s\n' "$1" "$tot" "$h"; sleep 3
}
# --- the two collision candidates and their colliding partners
q 'banca'
q 'banco'
q 'banca NOT banco NOT bancaria NOT bancario'
q 'prova'
q 'prove'
q 'prova NOT prove NOT provable'
q 'rúbrica'
q 'rubrica orçamentária'
# --- the exam-vocabulary vein the LATAM probe opened
q 'enem stars:>5'
q 'vestibular stars:>5'
q 'concursos públicos'
q 'oposiciones stars:>2'
q 'selectividad'
q 'EBAU stars:>2'
