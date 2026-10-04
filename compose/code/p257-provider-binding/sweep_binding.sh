#!/bin/sh
# P257 — barrido de LIGADURA DE PROVEEDOR por el canal CALIBRADO (`raw.githubusercontent.com`).
#
# Se NIEGA a correr si el canal no discrimina (regla de P249): primero 200 a una ruta
# buena y 404 a una inexistente, y solo entonces se le cree un negativo.
# TSV: slug \t manifest \t verdict \t providers \t layers
here=$(cd "$(dirname "$0")" && pwd)
RAW=https://raw.githubusercontent.com

if [ "$1" = "--calibrate" ]; then
  good=$(curl -s -o /dev/null --max-time 25 -w '%{http_code}' \
    "$RAW/openedx/edx-platform/HEAD/LICENSE")
  bad=$(curl -s -o /dev/null --max-time 25 -w '%{http_code}' \
    "$RAW/openedx/zzz-no-such-repo-9x8y7/HEAD/LICENSE")
  if [ "$good" = "200" ] && [ "$bad" = "404" ]; then
    echo "CALIBRATED good=$good bad=$bad"; exit 0
  fi
  echo "NO-CLAIM good=$good bad=$bad — el canal no discrimina, no se le cree un negativo"
  exit 1
fi

slug="$1"

# Marcador de WORKSPACE fuera del manifiesto: pnpm y lerna no lo escriben en el
# package.json, asi que desde el manifiesto solo la raiz de un monorepo parece un
# paquete sin dependencias. Es el falso negativo que este barrido cometio en su
# primer corte (ver result-monoroot.NEGATIVE-CONTROL-2026-10-04.tsv).
marker=""
for wf in pnpm-workspace.yaml lerna.json; do
  wc=$(curl -s -o /dev/null --max-time 25 -w '%{http_code}' "$RAW/${slug}/HEAD/${wf}" 2>/dev/null)
  [ "$wc" = "200" ] && { marker="--workspace-marker"; break; }
done

for fn in package.json requirements.txt pyproject.toml; do
  out=$(curl -s --max-time 25 -w "\n%{http_code}" "$RAW/${slug}/HEAD/${fn}" 2>/dev/null)
  code=$(printf '%s' "$out" | tail -1)
  if [ "$code" = "200" ]; then
    row=$(printf '%s' "$out" | sed '$d' | python3 "$here/classify_binding.py" "$fn" $marker)
    printf '%s\t%s\t%s\n' "$slug" "$fn" "$row"
    exit 0
  fi
done
# Sin manifiesto LEIDO no se afirma ausencia de ligadura: NO-CLAIM (P251 en este eje).
printf '%s\t-\tNO-CLAIM\t-\t-\n' "$slug"
