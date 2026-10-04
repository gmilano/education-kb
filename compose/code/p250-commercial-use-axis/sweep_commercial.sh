#!/bin/sh
# P250 — familia de licencia Y uso comercial, en DOS columnas separadas.
#
# Usa el classificador COMPARTIDO (`lib/license_family.sh`), no uno propio: p170 trae su
# `classify()` en linea porque es del pase 64 y la libreria es del 77, y esa es exactamente
# la deuda que P237 nombro. Este barrido es el primero del catalogo que la consume.
# TSV: slug \t status \t hit_path \t bytes \t family \t commercial_use
here=$(cd "$(dirname "$0")" && pwd)
. "$here/../lib/license_family.sh"
slug="$1"
for fn in LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt license license.md license.txt \
          LICENCE LICENCE.md LICENSE-MIT LICENSE-APACHE LICENSE.rst LICENSE-MIT.txt; do
  out=$(curl -s --max-time 25 -w "\n%{http_code}" "https://raw.githubusercontent.com/${slug}/HEAD/${fn}" 2>/dev/null)
  code=$(printf '%s' "$out" | tail -1)
  if [ "$code" = "200" ]; then
    content=$(printf '%s' "$out" | sed '$d')
    bytes=$(printf '%s' "$content" | wc -c | tr -d ' ')
    if commercial_use_ok "$content"; then cu="OK"; else cu="PROHIBIDO"; fi
    printf '%s\tLICENSED\t%s\t%s\t%s\t%s\n' "$slug" "$fn" "$bytes" "$(family_of "$content")" "$cu"
    exit 0
  fi
done
for rm in README.md README.rst readme.md README README.markdown docs/README.md package.json setup.py; do
  code=$(curl -s -o /dev/null --max-time 25 -w '%{http_code}' "https://raw.githubusercontent.com/${slug}/HEAD/${rm}" 2>/dev/null)
  [ "$code" = "200" ] && { printf '%s\tUNLICENSED\t-\t0\tNO-LICENSE-FILE\tSIN-DETERMINAR\n' "$slug"; exit 0; }
done
printf '%s\tUNREACHABLE\t-\t0\t-\tSIN-DETERMINAR\n' "$slug"
