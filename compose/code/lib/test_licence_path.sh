#!/bin/bash
# Suite de `lib/licence_path.sh`.  Dos mitades:
#
#  1. LOS CASOS DE p196, puertos literales de `p196-none-tree-reach/test_tree_reach.sh` --
#     las rutas REALES que derrotaron a las listas de nombres de esta base (`P441`), mas los
#     negativos que refutaron las versiones v1 y v2 del propio instrumento de p196.
#  2. EL CONTROL DE IDENTIDAD, que es la razon por la que esta promocion no es un fork:
#     los cuerpos de las dos funciones se extraen de `licence_path.sh` y de
#     `p196-none-tree-reach/tree_reach.sh` y se comparan BYTE A BYTE.  Si alguien toca una
#     copia y no la otra, esto falla, que es exactamente el `Gap 440` de las paginas
#     ("una correccion aterriza en un sitio y no en el otro") aplicado al codigo.
set -u
HERE="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}" 2>/dev/null || printf '%s' "${BASH_SOURCE[0]}")")" && pwd)"
. "$HERE/licence_path.sh" || { echo "FATAL: no se pudo cargar licence_path.sh" >&2; exit 2; }
for f in is_licence_path is_bundled; do
  declare -F "$f" >/dev/null 2>&1 || { echo "FATAL: $f no definida" >&2; exit 2; }
done

t=0; p=0
yes_lic() { t=$((t+1)); if is_licence_path "$1"; then p=$((p+1)); else echo "FAIL want-licence: $1"; fi; }
no_lic()  { t=$((t+1)); if is_licence_path "$1"; then echo "FAIL want-NOT-licence: $1"; else p=$((p+1)); fi; }
yes_bun() { t=$((t+1)); if is_bundled "$1"; then p=$((p+1)); else echo "FAIL want-bundled: $1"; fi; }
no_bun()  { t=$((t+1)); if is_bundled "$1"; then echo "FAIL want-NOT-bundled: $1"; else p=$((p+1)); fi; }
chk()     { t=$((t+1)); if [ "$2" = "$3" ]; then p=$((p+1)); printf 'ok   %s\n' "$1"; else echo "FAIL $1: expected=$2 got=$3"; fi; }

# --- 1. los casos de p196, sin cambiar uno ---------------------------------------------
yes_lic "LICENSE.TXT"                             # openedx/XBlock -- derroto 5 listas
yes_lic "package/license"                         # @learninglocker/xapi-agents
yes_lic "aoe-web-frontend/LICENSE"                # Opetushallitus/aoe -- EUPL en subdirectorio
yes_lic "COPYING.txt"
yes_lic "docs/License.txt"                        # OS4ED/openSIS-Classic
yes_lic "LICENSE"; yes_lic "licence"; yes_lic "COPYING"; yes_lic "LICENSE.md"
yes_lic "NOTICE.txt"
yes_lic "LICENSES/MIT.txt"                        # REUSE/SPDX -- refuto v1 de p196
yes_lic "LICENSES/GPL-3.0-or-later.txt"
no_lic  "licenses/README.md"                      # refuto v2 de p196
no_lic  "README.md"; no_lic "src/licensing.py"; no_lic "LICENSE_HEADER_CHECK.cfg"
no_lic  "licenses.json"
yes_bun "node_modules/foo/LICENSE"; yes_bun "vendor/bar/COPYING"
yes_bun "web/third_party/x/LICENSE"; yes_bun ".venv/lib/LICENSE"
no_bun  "LICENSE"; no_bun "docs/License.txt"; no_bun "aoe-web-frontend/LICENSE"
# --- casos nuevos de p197, de las rutas que esta pasada leyo de verdad -----------------
yes_lic "license.txt"                             # frappe/education -- minuscula, 19 B
yes_lic "License"                                 # una de las 3 raices que la escalera perdio
yes_lic "License.txt"
# `no_lic "licenses"` se PROBO y se RETIRA, y el motivo es del canal, no del predicado:
# `git ls-tree -r --name-only` lista FICHEROS, nunca directorios, asi que una ruta `licenses`
# que llega por este canal es un fichero llamado `licenses` -- y eso SI es una concesion.
# El caso estaba mal escrito; afirmarlo habria endurecido un error.
yes_lic "licenses"
no_lic  "doc/licensing-faq.md"

# --- 2. el control de identidad: la copia sigue siendo la copia -------------------------
extract() { # fichero nombre -> cuerpo
  awk -v fn="$2" 'index($0, fn "() {")==1 {on=1} on {print} on && $0=="}" {exit}' "$1"
}
SRC="$HERE/../p196-none-tree-reach/tree_reach.sh"
if [ -f "$SRC" ]; then
  for fn in is_bundled is_licence_path; do
    a="$(extract "$HERE/licence_path.sh" "$fn")"
    b="$(extract "$SRC" "$fn")"
    chk "identidad byte-a-byte de $fn con p196" "$(printf '%s' "$b" | md5sum | cut -d' ' -f1)" \
                                                "$(printf '%s' "$a" | md5sum | cut -d' ' -f1)"
    chk "el cuerpo de $fn no esta vacio" si "$([ -n "$a" ] && echo si || echo no)"
  done
else
  # la ausencia del original NO puede leerse como identidad
  chk "el original de p196 esta presente" si no
fi

echo "$p/$t"; [ "$p" = "$t" ] || exit 1
