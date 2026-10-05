#!/usr/bin/env bash
# El canal de `P275`: clon sin blobs + `git ls-tree -r`. Ve el arbol COMPLETO,
# no solo la raiz — que es donde los dos controles de respuesta conocida de este
# pase demuestran que el sondeo de raiz se queda corto (`P187`, `P172-semantic`).
set -u
OUT=${1:?outfile}
WORK=$(mktemp -d)
printf 'slug\ttree_files\tlicenseish_paths\tn_licenseish\testado\n' > "$OUT"
while read -r slug; do
  [ -z "$slug" ] && continue
  d="$WORK/$(echo "$slug" | tr / _)"
  if ! timeout 120 git clone -q --filter=blob:none --no-checkout \
        "https://github.com/$slug" "$d" 2>/dev/null; then
    printf '%s\t-\t-\t-\tCLON-FALLO\n' "$slug" >> "$OUT"
    printf '%-52s CLON-FALLO\n' "$slug" >&2
    continue
  fi
  n=$(git -C "$d" ls-tree -r --name-only HEAD | wc -l | tr -d ' ')
  # cualquier ruta que pueda CEDER, en cualquier profundidad y cualquier caja
  paths=$(git -C "$d" ls-tree -r --name-only HEAD \
          | grep -iE '(^|/)(licen[sc]e|copying|copyright|notice|terms|unlicense)([.-][a-z0-9.]+)?$' \
          | head -20 | tr '\n' ';')
  k=$(printf '%s' "$paths" | tr ';' '\n' | grep -c . || true)
  if [ "$k" -gt 0 ]; then e=CEDE-FUERA-DE-RAIZ; else e=SIN-ARCHIVO-EN-TODO-EL-ARBOL; fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$n" "${paths:--}" "$k" "$e" >> "$OUT"
  printf '%-52s files=%-6s licenseish=%-2s %s\n' "$slug" "$n" "$k" "$e" >&2
  rm -rf "$d"
done
rm -rf "$WORK"
