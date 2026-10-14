#!/bin/bash
# p197 -- para UN slug: TODA ruta de concesion del arbol completo, leida y clasificada.
#
# Existe porque la accion pre-registrada pide «fila por fila»: un conteo de 15 textos no
# dice si la capa concede.  Hay que leer los 15.  Misma cadena de reglas que
# `read_grants.sh`; lo unico que cambia es que no se queda con la primera ruta.
set -u
HERE="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}" 2>/dev/null || printf '%s' "${BASH_SOURCE[0]}")")" && pwd)"
LIB="$HERE/../lib"
. "$LIB/licence_path.sh"; . "$LIB/license_family.sh"; . "$LIB/payload_measure.sh"
SLUG="${1:?slug}"; OUT="${2:?tsv}"
WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
d="$WORK/r"
git clone --filter=blob:none --no-checkout --depth 1 -q "https://github.com/$SLUG" "$d" || { echo "CLONE-FAILED" >&2; exit 2; }
printf 'slug\tpath\tdepth\tbundled\tbytes\tfamily\tholder_hint\n' > "$OUT"
git -C "$d" ls-tree -r --name-only HEAD > "$WORK/tree"
echo "rutas en el arbol: $(wc -l < "$WORK/tree")"
while IFS= read -r path; do
  is_licence_path "$path" || continue
  bun=NO; is_bundled "$path" && bun=YES
  blob="$WORK/b"
  if ! git -C "$d" cat-file -p "HEAD:$path" > "$blob" 2>/dev/null; then
    printf '%s\t%s\t%s\t%s\t-\t-\tBLOB-UNREACHABLE\n' "$SLUG" "$path" "$(echo "$path" | tr -cd / | wc -c)" "$bun" >> "$OUT"; continue
  fi
  bytes="$(size_of_file "$blob")"
  fam="$(family_of "$(cat "$blob")")"
  # pista de titularidad: la primera linea de copyright, que es lo que dice DE QUIEN es el
  # texto -- la diferencia entre la concesion del repo y la de una dependencia copiada.
  hint="$(grep -m1 -i 'copyright' "$blob" | tr -s ' \t' ' ' | cut -c1-80)"
  [ -z "$hint" ] && hint="(sin linea de copyright)"
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$SLUG" "$path" "$(echo "$path" | tr -cd / | wc -c)" "$bun" "$bytes" "$fam" "$hint" >> "$OUT"
done < "$WORK/tree"
awk -F'\t' 'NR>1{printf "%-62s %-4s %7s B %-16s %s\n",$2,$4,$5,$6,$7}' "$OUT"
echo "--- $OUT"
