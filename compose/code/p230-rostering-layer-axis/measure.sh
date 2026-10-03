#!/usr/bin/env bash
# p230 — LAYER × LICENSE × SPEC sobre la capa OneRoster.
#
# Mide, para cada pieza, las TRES condiciones que esta KB le pide a una fundación,
# y las mide por separado para no volver a publicar una conclusión que las mezcla:
#
#   1. LICENCIA  -> payload del archivo (nunca una insignia, nunca un campo de registro solo)
#   2. CAPA      -> servidor | cliente | puente  (declarado en la tabla de abajo, no inferido)
#   3. SPEC      -> v1p1 | v1p2  (leido del README/codigo, no del nombre del repo)
#
# Regla de metodo que este instrumento hace cumplir (el error del pase 75):
#   un repo MUERTO se mide IGUAL. La muerte no exime de medir la licencia:
#   un permisivo muerto se BIFURCA, un AGPL muerto no. La licencia pesa MAS, no menos.
#
# Canal: solo raw.githubusercontent.com (el unico que sirve payload en este entorno;
# api.github.com/repos -> 403, ver p230 README seccion "cota de canal").
#
# Uso:  ./measure.sh            # barre la tabla versionada
#       ./measure.sh owner/repo # mide una pieza suelta

set -uo pipefail

LICENSE_NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE-MIT MIT-LICENSE NOTICE"
BRANCHES="main master"
RAW="https://raw.githubusercontent.com"

# slug|capa|spec_declarado  -- la capa y el spec se declaran aqui y se citan en el README
PIECES="
bgwdotdev/go-oneroster|servidor|v1p1
fffnite/go-oneroster|servidor|v1p1
bgwdotdev/libre-oneroster|servidor|v1p1
usechalk/chalk|servidor|v1p1
jdolny/OneRoster.NET|cliente|v1p1+v1p2
gotranseo/oneroster|cliente|v1p1
TCI/OneRoster|cliente|v1p1
jrissler/ex_oneroster|cliente|v1p1
the-glasgow-academy/oneroster-api-to-csv-sds|puente|v1p1
the-glasgow-academy/oneroster-api-to-csv-asm|puente|v1p1
"

classify() { # stdin: payload de licencia -> clase
  local p; p=$(head -40)
  case "$p" in
    *"MIT License"*|*"Permission is hereby granted, free of charge"*) echo "MIT" ;;
    *"GNU AFFERO GENERAL PUBLIC LICENSE"*) echo "AGPL-3.0" ;;
    *"GNU LESSER GENERAL PUBLIC"*) echo "LGPL" ;;
    *"GNU GENERAL PUBLIC LICENSE"*) echo "GPL" ;;
    *"Apache License"*) echo "Apache-2.0" ;;
    *"Redistribution and use in source and binary forms"*) echo "BSD" ;;
    "") echo "VACIO" ;;
    *) echo "OTRO" ;;
  esac
}

measure_one() { # $1 slug -> "clase|titular|ruta"
  local slug=$1 br f url code body
  for br in $BRANCHES; do
    for f in $LICENSE_NAMES; do
      url="$RAW/$slug/$br/$f"
      code=$(curl -sS -o /dev/null -w "%{http_code}" --max-time 15 "$url" 2>/dev/null)
      [ "$code" = "200" ] || continue
      body=$(curl -sS --max-time 15 "$url" 2>/dev/null)
      printf '%s|%s|%s\n' \
        "$(printf '%s' "$body" | classify)" \
        "$(printf '%s' "$body" | grep -m1 -oE 'Copyright \(c\) [0-9]{4}.*' | sed 's/Copyright (c) //' | cut -c1-40)" \
        "$br/$f"
      return 0
    done
  done
  echo "SIN-ARCHIVO-DE-LICENCIA||(${BRANCHES// / y } x $(echo $LICENSE_NAMES | wc -w) nombres)"
}

if [ $# -ge 1 ]; then measure_one "$1"; exit 0; fi

printf '%-46s %-8s %-11s %-14s %-24s %s\n' SLUG CAPA SPEC LICENCIA TITULAR RUTA
printf '%s\n' "----------------------------------------------------------------------------------------------------------------------------"
permisivo_v1p2=0; permisivo_total=0
echo "$PIECES" | while IFS='|' read -r slug capa spec; do
  [ -n "${slug:-}" ] || continue
  IFS='|' read -r clase titular ruta <<< "$(measure_one "$slug")"
  printf '%-46s %-8s %-11s %-14s %-24s %s\n' "$slug" "$capa" "$spec" "$clase" "${titular:--}" "$ruta"
done
