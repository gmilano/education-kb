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

# --- casos nuevos de p256: la FORMA CON TOKEN, y la prosa que no debe colarse -----------
# `openstax/fine_print` -- la concesion MIT real vive en `MIT-LICENSE`, 1 055 B,
# sha256-16 `0a9ed2a2ba710b61`, leida de primera mano en p256 sobre `main`@`3b75fbcbcfb0`.
# Los cinco `yes_lic` de abajo FALLAN contra el predicado anterior a p256; eso es lo que
# convierte esta ampliacion en una correccion medida y no en una preferencia.
yes_lic "MIT-LICENSE"                             # openstax/fine_print -- gema Rails, REAL
yes_lic "MIT-LICENSE.txt"
yes_lic "LICENSE-MIT"                             # convencion de doble concesion de Rust
yes_lic "LICENSE-APACHE"
yes_lic "APACHE-LICENSE-2.0.txt"
yes_lic "third-party-licenses.txt"                # agregado de avisos: NOTICE.txt ya era SI
no_lic  "license-faq.md"                          # prosa SOBRE una concesion
no_lic  "LICENSE-POLICY.md"
no_lic  "third-party-license-report.json"
no_lic  "LICENSE-HEADER-CHECK.cfg"
no_lic  "licenses.json"                           # ya estaba arriba; se repite como ancla

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


# 🔴 p279: THESE CONTROLS WERE APPENDED BELOW THE SUMMARY LINE AND THEREFORE DID NOT RUN AS
# CONTROLS.  `echo "$p/$t"; [ "$p" = "$t" ] || exit 1` had already decided the suite's exit
# status, so ten new assertions printed their failures into a suite that had already passed.
# The count gave it away: 44/44 both before and after adding them.
# 🔵 Third instance of ONE shape in this single pass -- a CLI appended below the `__main__`
# that dies first, a second `__main__` below the function it needs, and now controls below
# the summary that grades them.  `p278` wrote "an anchor that breaks when a paragraph is
# reflowed is the same brittleness class as one copied from the number it checks"; this is
# that class in file ORDER.  **Position relative to the thing that reads you is load-bearing.**
# --- p279: the two vendoring conventions the per-package manifest walk exposed -----------
# Each of these was counted as a repository's OWN per-package licence declaration before
# `is_bundled` learned the convention.  Real paths from real rows on these shelves.
yes_bun "public/assets/libs/moment/package.json"
yes_bun "public/assets/libs/@ckeditor/ckeditor5-build-classic/package.json"
yes_bun "assets/libs/swiper/package.json"
yes_bun "inc/libraries/wp-background-process/composer.json"
# 🔵 The NEGATIVE controls that keep the widening narrow: a real workspace package must
# still read as the repository's own, or the walk this was built for stops seeing anything.
no_bun  "packages/ai-assistant/package.json"
no_bun  "apps/api/package.json"
no_bun  "assessment_module_manager/pyproject.toml"
no_bun  "src/libs/helper.js"
# 🔴 the SECOND spelling in the SAME repository -- the floor-not-a-proof control
yes_bun "resources/views/backend/assetslib/libs/moment/package.json"
yes_bun "resources/views/backend/assetslib/libs/@ckeditor/ckeditor5-build-classic/package.json"

echo "$p/$t"; [ "$p" = "$t" ] || exit 1
