#!/bin/bash
# Authoritative license sweep, HEAD-ref based.
# raw.githubusercontent.com resolves the ref "HEAD" to the repo's DEFAULT branch,
# whatever it is named -> the branch dimension disappears (main/master/develop/trunk all covered).
# Three-way outcome: LICENSED / UNLICENSED (repo reachable, no license file) / UNREACHABLE.
# TSV: slug \t status \t hit_path \t bytes \t license_id
slug="$1"
# P237 CERRADO en el pase 101 (P312).  Esta copia inline se REWIREO a la libreria
# compartida.  La razon declarada en el pase 100 para no hacerlo era concreta y correcta
# --«el control compartido todavia no es un superconjunto de las copias» (BUSL, Elastic y
# PolyForm vivian SOLO aca)-- asi que el pase 101 primero las agrego a
# `lib/license_family.sh` con sus controles negativos (6 aserciones nuevas) y DESPUES
# rewireo.  Parchar la copia era el antipatron que P237 existe para nombrar.
#
# El VOCABULARIO publicado de este barrido se CONSERVA a proposito.  La libreria responde
# mas fino que esta copia (`GPL-3.0` donde esta decia `GPL`, `CC-BY-4.0` donde decia
# `CC-BY`, `UNCLASSIFIED` donde decia `UNKNOWN`), y adoptar el vocabulario fino en silencio
# volveria incomparables los TSV ya publicados (`result.2026-10-03.tsv`,
# `result.2026-10-04.pase99.tsv`).  La traduccion es explicita y es de UNA sola direccion:
# agrupa, nunca inventa.
. "$(dirname "$0")/../lib/license_family.sh"
classify() {
  case "$(family_of "$1")" in
    GPL-2.0|GPL-3.0)        echo "GPL" ;;
    CC-BY-*|CC-BY)          echo "CC-BY" ;;
    UNCLASSIFIED)           echo "UNKNOWN" ;;
    NONCOMMERCIAL-NOT-OSI)  echo "UNKNOWN" ;;
    *)                      family_of "$1" ;;
  esac
}
for fn in LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt license license.md license.txt \
          LICENCE LICENCE.md LICENSE-MIT LICENSE-APACHE LICENSE.rst LICENSE-MIT.txt; do
  out=$(curl -s --max-time 25 -w $'\n%{http_code}' "https://raw.githubusercontent.com/${slug}/HEAD/${fn}" 2>/dev/null)
  code=$(printf '%s' "$out" | tail -1)
  if [ "$code" = "200" ]; then
    content=$(printf '%s' "$out" | sed '$d')
    bytes=$(printf '%s' "$content" | wc -c | tr -d ' ')
    printf '%s\tLICENSED\t%s\t%s\t%s\n' "$slug" "$fn" "$bytes" "$(classify "$content")"
    exit 0
  fi
done
# Existence control: separates "reachable but unlicensed" from "cannot reach the repo at all".
for rm in README.md README.rst readme.md README README.markdown docs/README.md package.json setup.py; do
  code=$(curl -s -o /dev/null --max-time 25 -w '%{http_code}' "https://raw.githubusercontent.com/${slug}/HEAD/${rm}" 2>/dev/null)
  if [ "$code" = "200" ]; then
    printf '%s\tUNLICENSED\t-\t0\t(reachable via %s)\n' "$slug" "$rm"
    exit 0
  fi
done
printf '%s\tUNREACHABLE\t-\t0\t-\n' "$slug"
