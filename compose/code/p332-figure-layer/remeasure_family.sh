#!/bin/sh
# Accion C, segunda mitad — remedir la FAMILIA de las huellas que esta base nombra.
# La familia se decide por BLOQUE DE TITULO (`P171`), nunca por el sha (`P329`).
# El canal se calibra antes: ancla buena -> 200, ancla inventada -> 404, o se sale con codigo 2.
set -u
RAW=https://raw.githubusercontent.com

code() { curl -s -o /dev/null -w '%{http_code}' --max-time 25 "$1"; }

echo "--- calibracion del canal (P249) ---"
ok=$(code "$RAW/vishalsachdev/canvas-mcp/main/LICENSE")
no=$(code "$RAW/vishalsachdev/canvas-mcp/main/NO-EXISTE-107")
echo "ancla buena=$ok  ancla inventada=$no"
[ "$ok" = "200" ] && [ "$no" = "404" ] || { echo "canal NO discrimina => NO-CLAIM"; exit 2; }

familia() {  # lee stdin, decide por bloque de titulo
  t=$(head -c 400 "$1" | tr 'A-Z' 'a-z')
  case "$t" in
    *"apache license"*)        echo "Apache-2.0" ;;
    *"mit license"*)           echo "MIT" ;;
    *"bsd zero clause"*|*"0bsd"*) echo "0BSD" ;;
    *"gnu affero"*)            echo "AGPL-3.0" ;;
    *"gnu lesser"*)            echo "LGPL" ;;
    *"gnu general public"*)    echo "GPL" ;;
    *"mozilla public"*)        echo "MPL-2.0" ;;
    *"creative commons"*)      echo "CC (ver clausulas)" ;;
    *"redistribution and use"*) echo "BSD" ;;
    *)                          echo "NO-RESUELVE" ;;
  esac
}

printf '%-42s %-9s %-18s %-18s %s\n' slug bytes sha256_crudo sha256_normalizado familia
for slug in vishalsachdev/canvas-mcp bibo242/blackboard-mcp felipedias-ie/blackboard-mcp \
            OpenEMIS/core buriro-ezekia/mwalimulens-agent; do
  got=""
  for br in main master; do
    if curl -sf --max-time 30 "$RAW/$slug/$br/LICENSE" -o /tmp/lic.$$ 2>/dev/null; then got=$br; break; fi
  done
  if [ -z "$got" ]; then printf '%-42s %s\n' "$slug" "LICENSE no alcanzable en main/master => NO-CLAIM"; continue; fi
  b=$(wc -c < /tmp/lic.$$ | tr -d ' ')
  craw=$(sha256sum /tmp/lic.$$ | cut -c1-16)
  cnorm=$(tr -d '\r' < /tmp/lic.$$ | sha256sum | cut -c1-16)
  printf '%-42s %-9s %-18s %-18s %s\n' "$slug" "$b" "$craw" "$cnorm" "$(familia /tmp/lic.$$)"
  rm -f /tmp/lic.$$
done
