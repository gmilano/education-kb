#!/bin/sh
# p294 — el camino de PRODUCCION corrido punta a punta sobre los pom.xml REALES.
#
# Pase 97 del 2026-10-04.  No usa las fixtures: baja el payload de `raw.githubusercontent.com`
# (el unico canal vivo, `P247`) y lo pasa por `p283/manifest_license.py`, que es el modulo que
# produce los veredictos publicados.  La familia la classifica `lib/license_family.sh` (P237).
#
# La columna `publicado` es lo que ESTA KB ya afirma para esa fila, leido del payload del
# archivo de licencia en pases anteriores.  El acuerdo entre dos canales INDEPENDIENTES
# --archivo de licencia vs. declaracion del manifiesto-- es el resultado que importa.
#
# Uso:  sh sweep_pom_production.sh [salida.tsv]
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
RAW=https://raw.githubusercontent.com
ML="$HERE/../p283-manifest-named-license/manifest_license.py"
. "$HERE/../lib/license_family.sh"
OUT="${1:-$HERE/result.$(date -u +%F).tsv}"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# Los destinos van ESCRITOS A MANO, uno por cita: este entorno niega enumerar destinos en
# lote (pase 96), y las sondas puntuales atadas a una cita si corren.
TARGETS='kuali/kc|AGPL-3.0
sakaiproject/sakai|ECL-2.0
UniTime/unitime|Apache-2.0
OpenOLAT/OpenOLAT|Apache-2.0
DSpace/DSpace|BSD-3-Clause
SafeExamBrowser/seb-server|MPL-2.0'

jget() { python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('$1') if d.get('$1') is not None else '<NADA>')"; }

printf 'slug\tpom_bytes\tganador\tpropiedad\tatribuible\tdeclarado\tfamilia\tpublicado\tacuerdo\n' > "$OUT"
echo "$TARGETS" | while IFS='|' read -r slug pub; do
  [ -z "$slug" ] && continue
  pom="$TMP/pom.xml"
  code=$(curl -s --max-time 30 -w '%{http_code}' -o "$pom" "$RAW/$slug/HEAD/pom.xml")
  if [ "$code" != "200" ]; then
    printf '%s\t-\t-\t-\t-\tSIN_POM(%s)\t-\t%s\tINDETERMINADO\n' "$slug" "$code" "$pub" >> "$OUT"
    continue
  fi
  sz=$(wc -c < "$pom" | tr -d ' ')
  js=$(python3 "$ML" pom.xml "$slug" < "$pom" 2>/dev/null)
  if [ -z "$js" ] || [ "$js" = "null" ]; then
    printf '%s\t%s\t-\t-\t-\t<NADA>\t-\t%s\tSIN_DECLARACION\n' "$slug" "$sz" "$pub" >> "$OUT"
    continue
  fi
  win=$(printf '%s' "$js" | jget name)
  own=$(printf '%s' "$js" | jget ownership)
  att=$(printf '%s' "$js" | jget attributable)
  dec=$(printf '%s' "$js" | jget license)
  if [ "$dec" = "<NADA>" ]; then
    printf '%s\t%s\t%s\t%s\t%s\t<NADA>\t-\t%s\tSIN_DECLARACION\n' "$slug" "$sz" "$win" "$own" "$att" "$pub" >> "$OUT"
    continue
  fi
  fam=$(osi_family_of "$dec")
  # ACUERDO si la familia leida del manifiesto coincide con la publicada en su raiz de familia.
  # `BSD (declaracion)` contra `BSD-3-Clause` es acuerdo de FAMILIA y perdida de PRECISION:
  # se marca aparte, porque es el limite de este canal y no un error.
  base=$(printf '%s' "$fam" | sed 's/ (declaracion)//')
  case "$pub" in
    "$base") ac=ACUERDO ;;
    "$base"-*) ac=ACUERDO_MENOS_PRECISO ;;
    *) ac=REVISAR ;;
  esac
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$sz" "$win" "$own" "$att" "$dec" "$fam" "$pub" "$ac" >> "$OUT"
done
cat "$OUT"
