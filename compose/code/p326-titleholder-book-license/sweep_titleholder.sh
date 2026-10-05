#!/usr/bin/env bash
# p326 — lee la licencia de cada libro DEL TITULAR (org `openstax` en GitHub), por payload.
# Canal: raw.githubusercontent.com (vivo). NO usa openstax.org (403 por egress) ni agregadores.
# Dos lecturas independientes por libro:
#   (1) <md:license> del collection.xml del propio libro  -> cesion POR LIBRO
#   (2) LICENSE en la raiz del repo del bundle            -> cesion POR REPO
# Discrepancia entre (1) y (2) es un hallazgo, no un error del barrido.
set -u
RAW="https://raw.githubusercontent.com/openstax"
IN="${1:-books.tsv}"
printf 'curso\trepo\tcollection\tlicencia_collection_xml\turl_collection_xml\tlicencia_LICENSE_raiz\tbytes_LICENSE\thttp_collection\n'
tail -n +2 "$IN" | while IFS=$'\t' read -r curso repo coll n tasa; do
  [ -z "${repo:-}" ] && continue
  cxml=$(curl -sS --max-time 30 -w '\n%{http_code}' "$RAW/$repo/main/collections/$coll.collection.xml" 2>/dev/null)
  code=$(printf '%s' "$cxml" | tail -1)
  body=$(printf '%s' "$cxml" | sed '$d')
  if [ "$code" = "200" ]; then
    lic=$(printf '%s' "$body" | grep -o '<md:license[^>]*>[^<]*</md:license>' | head -1 | sed 's/<[^>]*>//g')
    url=$(printf '%s' "$body" | grep -o '<md:license url="[^"]*"' | head -1 | sed 's/.*url="//;s/"$//')
  else
    lic="NO-ALCANZABLE"; url="-"
  fi
  raw_lic=$(curl -sS --max-time 30 "$RAW/$repo/main/LICENSE" 2>/dev/null)
  bytes=$(printf '%s' "$raw_lic" | wc -c | tr -d ' ')
  head1=$(printf '%s' "$raw_lic" | head -1 | tr -d '\r')
  case "$head1" in
    *NonCommercial-ShareAlike*) fam="CC BY-NC-SA 4.0" ;;
    *NonCommercial*)            fam="CC BY-NC (variante)" ;;
    Attribution\ 4.0*)          fam="CC BY 4.0" ;;
    *Attribution*ShareAlike*)   fam="CC BY-SA (variante)" ;;
    *)                          fam="SIN-ARCHIVO-O-NO-CC" ;;
  esac
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$curso" "$repo" "$coll" "${lic:-VACIO}" "${url:-VACIO}" "$fam" "$bytes" "$code"
done
