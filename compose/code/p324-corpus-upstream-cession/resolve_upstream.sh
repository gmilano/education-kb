#!/bin/bash
# P324 — resolver la CESION DEL TITULAR de cada corpus vendoreado.
#
# Deuda de los pases 102 y 103 (`amber` 45 archivos + `ncte` 29 = 74 de los 111 de
# `rosewang2008/edu-convokit`).  El pase 103 no pudo correrla: canal denegado.
#
# El paso que esta base tuvo que inventar en el pase 102 y que ningun barrido de licencias
# hace solo: NO alcanza con leer el LICENSE del repo que redistribuye.  Hay que
#   1. encontrar el UPSTREAM          (de primera mano, no inferido del nombre del directorio)
#   2. ENUMERAR su arbol              (canal P275: el unico que sostiene una AUSENCIA)
#   3. leer SU cesion del payload     (P314: un agregador no cede nada)
#   4. verificar la IDENTIDAD         (nombres de archivo, no "parece el mismo dataset")
#
# TSV: corpus \t n_archivos \t upstream \t cesion_upstream \t alcance \t identidad
set -u
WORK="${WORK:-/tmp/p324}"; mkdir -p "$WORK"
EC="$WORK/edu-convokit"
[ -d "$EC/.git" ] || git clone --filter=blob:none --no-checkout --depth 1 \
    https://github.com/rosewang2008/edu-convokit "$EC" >&2

lic_of() { # slug -> "familia|archivo|bytes" leyendo el PAYLOAD, o SIN-ARCHIVO
  local slug="$1" f out code body
  for f in LICENSE LICENSE.md LICENSE.txt license.txt LICENCE COPYING LICENSE.TXT; do
    out=$(curl -s --max-time 25 -w $'\n%{http_code}' "https://raw.githubusercontent.com/$slug/HEAD/$f")
    code=$(printf '%s' "$out" | tail -1); body=$(printf '%s' "$out" | sed '$d')
    if [ "$code" = "200" ]; then
      printf '%s|%s|%sB' "$(printf '%s' "$body" | head -3 | tr -d '\n' | cut -c1-40)" "$f" "$(printf '%s' "$body" | wc -c)"
      return
    fi
  done
  printf 'SIN-ARCHIVO-DE-LICENCIA|-|-'
}

printf 'corpus\tn_archivos\tupstream\tcesion_upstream\talcance\tidentidad\n'
for c in amber ncte talkmoves; do
  n=$(git -C "$EC" ls-tree -r --name-only HEAD | grep -c "^data/$c/")
  case "$c" in
    # Los upstreams NO se adivinan del nombre: se leen de los notebooks del propio
    # redistribuidor (docs/source/tutorial_<corpus>.ipynb), que los enlazan de primera mano.
    amber)     up="laurenceholt/amber" ;;
    ncte)      up="ddemszky/classroom-transcript-analysis" ;;
    talkmoves) up="SumnerLab/TalkMoves" ;;
  esac
  printf '%s\t%s\t%s\t%s\t?\t?\n' "$c" "$n" "$up" "$(lic_of "$up")"
done
