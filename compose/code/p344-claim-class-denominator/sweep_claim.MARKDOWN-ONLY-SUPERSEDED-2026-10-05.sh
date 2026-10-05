#!/usr/bin/env bash
# Accion A del pase 110 (P342 contra el catalogo entero).
# Para cada repo: (1) pide README en 2 ortografias x 3 refs, (2) pide 10 nombres de
# licencia x 2 ramas, (3) si el README llega, extrae AFIRMACIONES de cesion:
#     - badge  [![License...](...)](RUTA)
#     - arbol  |-- LICENSE / `-- LICENSE  (entrada de arbol dibujado)
#     - prosa  "licensed under the X License"
# Salida TSV. El control negativo va en el MISMO lote (P320).
set -u
RAW=https://raw.githubusercontent.com
NAMES=(LICENSE LICENSE.md LICENSE.txt LICENSE.TXT LICENCE LICENCE.md COPYING COPYING.md LICENSE-MIT LICENSE.rst)
BRANCHES=(main master)
READMES=(README.md readme.md Readme.md README.MD)
code(){ curl -sS -o "$2" -w '%{http_code}' --max-time 25 "$1" 2>/dev/null || echo 000; }

OUT=${1:?outfile}
: > "$OUT"
printf 'slug\tlicense_file_hits\tprobes\treadme_ref\treadme_bytes\tbadge_claim\ttree_claim\tprose_claim\tveredicto\n' >> "$OUT"

while read -r slug; do
  [ -z "$slug" ] && continue
  hits=0; probes=0
  for b in "${BRANCHES[@]}"; do for n in "${NAMES[@]}"; do
    probes=$((probes+1))
    c=$(code "$RAW/$slug/$b/$n" /tmp/lic.$$)
    if [ "$c" = "200" ]; then hits=$((hits+1)); fi
  done; done
  # README
  rref=-; rbytes=0
  for b in "${BRANCHES[@]}" HEAD; do for r in "${READMES[@]}"; do
    [ "$rref" != "-" ] && break 2
    c=$(code "$RAW/$slug/$b/$r" /tmp/rm.$$)
    if [ "$c" = "200" ]; then rref="$b/$r"; rbytes=$(wc -c < /tmp/rm.$$ | tr -d ' '); fi
  done; done

  badge=-; tree=-; prose=-
  if [ "$rref" != "-" ]; then
    # badge: enlace markdown cuyo TEXTO menciona licencia y cuyo DESTINO es una ruta (no http)
    badge=$(grep -oE '\[!\[[^]]*[Ll]icen[sc]e[^]]*\]\([^)]*\)\]\([^)]*\)' /tmp/rm.$$ | head -3 | tr '\n' ';' )
    [ -z "$badge" ] && badge=-
    # arbol dibujado: linea con caracteres de arbol Y un nombre de licencia
    tree=$(grep -nE '(\xe2\x94\x9c|\xe2\x94\x94|\|--|`--).*LICEN[SC]E' /tmp/rm.$$ | head -3 | tr '\n' ';')
    [ -z "$tree" ] && tree=-
    prose=$(grep -noiE 'licen[sc]ed under the [A-Za-z0-9 .-]{2,30} licen[sc]e|under the [A-Za-z0-9 .-]{2,20} licen[sc]e' /tmp/rm.$$ | head -2 | tr '\n' ';')
    [ -z "$prose" ] && prose=-
  fi

  if [ "$hits" -gt 0 ]; then v=CEDE
  elif [ "$rref" = "-" ]; then v=INALCANZABLE
  elif [ "$badge" != "-" ] || [ "$tree" != "-" ]; then v=P342-AFIRMA-SIN-ARCHIVO
  elif [ "$prose" != "-" ]; then v=P314-PROSA-SIN-ARCHIVO
  else v=SILENCIO-CONFIRMADO
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$hits" "$probes" "$rref" "$rbytes" "$badge" "$tree" "$prose" "$v" >> "$OUT"
  printf '%-50s hits=%-2s readme=%-18s %s\n' "$slug" "$hits" "$rref" "$v" >&2
done
rm -f /tmp/lic.$$ /tmp/rm.$$
