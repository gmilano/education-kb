#!/bin/bash
# p863: 862-G2 — Spanish-speaking LATAM national examination vocabulary, never queried in this base.
out=sweep.tsv
: > "$out"
run() {
  local label="$1" q="$2"
  local tot s5
  tot=$(gh api -X GET search/repositories -f q="$q" -f per_page=1 2>/dev/null | python3 -c 'import sys,json;print(json.load(sys.stdin).get("total_count","ERR"))' 2>/dev/null)
  sleep 2
  s5=$(gh api -X GET search/repositories -f q="$q stars:>5" -f per_page=1 2>/dev/null | python3 -c 'import sys,json;print(json.load(sys.stdin).get("total_count","ERR"))' 2>/dev/null)
  sleep 2
  printf '%s\t%s\t%s\t%s\n' "$label" "$q" "$tot" "$s5" | tee -a "$out"
}
run MX-exani        'EXANI'
run MX-ceneval      'Ceneval'
run MX-comipems     'COMIPEMS'
run CO-icfes        'ICFES'
run CO-saber11      '"Saber 11"'
run CO-saberpro     '"Saber Pro"'
run CL-paes         'PAES prueba'
run PE-admision     '"examen de admisión"'
run AR-ingreso      '"examen de ingreso"'
