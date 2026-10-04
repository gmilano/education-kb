#!/bin/bash
# Mide el LICENSE por PAYLOAD (raw.githubusercontent.com): bytes, sha256, familia, titular.
#
# P255 (pase 85): la columna `holder` la llenaba `grep -m1 -i copyright`, SIN compuerta de
# familia, asi que sobre cualquier payload GPL devolvia el copyright del PROPIO texto de la
# licencia -- la Free Software Foundation -- como si fuera el titular del proyecto. Dos filas
# de `result.2026-10-03.tsv` quedaron asi (`classroomio/classroomio`, `gibbonedu/core`), y la
# prosa del README de este mismo directorio YA decia "boilerplate FSF": el defecto estaba en
# el DATO, no en la lectura. Ahora el titular lo responde `holder_of` de `lib/`, que es el
# control compartido, y se agrega la columna `family` para que la compuerta sea AUDITABLE en
# el propio TSV. El script anterior queda como
# `sweep_payload_license.UNGATED-SUPERSEDED-2026-10-04.sh`.
. "$(dirname "$0")/../lib/license_family.sh"
# P255 (pase 85): el script dejaba `body.tmp` en el directorio de trabajo al terminar, asi
# que un barrido ensuciaba el arbol del repo. Se limpia al salir.
trap 'rm -f body.tmp' EXIT
printf "slug\tbranch\tfile\thttp\tbytes\tsha256_12\tfamily\tholder\n"
for slug in "$@"; do
  found=0
  for br in main master; do
    # P255 (pase 85): la lista de 5 nombres producia un FALSO "sin cesion" sobre
    # `frappe/education`, que SI cede y lo hace en `license.txt` MINUSCULA. p170 ya barria
    # 14 nombres desde el pase 64; este instrumento barria 5. Se adoptan las variantes en
    # minuscula, que es de donde venia el falso.
    for f in LICENSE LICENSE.md LICENSE.txt COPYING LICENCE license license.txt license.md COPYING.txt; do
      url="https://raw.githubusercontent.com/$slug/$br/$f"
      code=$(curl -sS -o body.tmp -w '%{http_code}' --max-time 25 "$url")
      if [ "$code" = "200" ]; then
        b=$(wc -c < body.tmp | tr -d ' ')
        h=$(sha256sum body.tmp | cut -c1-12)
        payload=$(cat body.tmp)
        fam=$(family_of "$payload")
        hold=$(holder_of "$payload" | cut -c1-70)
        printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "$slug" "$br" "$f" "$code" "$b" "$h" "$fam" "$hold"
        found=1; break
      fi
    done
    [ "$found" = "1" ] && break
  done
  if [ "$found" = "0" ]; then
    printf "%s\t-\t-\t404\t-\t-\t-\tNO-LICENSE-FILE-FOUND\n" "$slug"
  fi
done

# P255 (pase 85): el script salia con codigo 1 cuando TODO habia ido bien, porque la
# ultima sentencia era un test que fallaba al haber encontrado licencia. Un barrido que
# miente en su codigo de salida no se puede encadenar ni poner en una compuerta.
exit 0
