#!/usr/bin/env bash
# `ACTION SW` — p229's registered highest priority.  Extend `p228-shelf-gate`'s grant ladder
# to the paths and refs these shelves ALREADY RECORD, over the 45 `CELL-WITHOUT-GRANT` slugs.
#
# p228 read 468 of 520 grants and left 52 slugs unread, reported as `CELL-WITHOUT-GRANT` with
# the note `6 paths x 2 refs`.  That note is the whole hypothesis: ABSENT is only ever
# ABSENT-AT-THE-PATH-PROBED (p222's rule, written down for the third time at p228), and this
# KB has recorded non-root grants for at least three of those very slugs:
#
#   os4ed/openSIS-Classic   docs/License.txt   (T209, re-proven at p228: 17 286 B, 224ac3d403e3)
#   formalms/formalms       html/license.txt   (gap 116)
#   moodle/moodle           public/           (P973: the 5.0 tree moved out of the root)
#
# So the ladder is extended on BOTH axes, and the second one is new here:
#
#   PATH axis  root names + the non-root prefixes the shelves record + the manifest channels
#   REF  axis  the REAL default branch from `git ls-remote --symref`, not the guess `main|master`
#
# The ref axis matters on its own: p228 guessed two branch names.  A repository whose default
# branch is `develop`, `trunk` or `MOODLE_405_STABLE` answers 404 at every path on both guesses
# and is indistinguishable from a grantless one.  `git ls-remote` is 200 through this proxy
# (p225, re-measured p229) and returns the default branch and HEAD SHA in ONE request, so the
# ref stops being a guess and the SHA gets PINNED (grant-ladder-v3's rule, kept by v4).
#
# P237: this file has NO classifier.  It fetches and records; `lib/license_family.sh` decides.
# T272: the name vocabulary is PRINTABLE (`--reach`) so the next pass extends it instead of
#       copying it.  A probe list copied is a probe list forked.
#
# usage: ladder.sh <slugs-file> <out-dir>   |   ladder.sh --reach
set -u
export GIT_TERMINAL_PROMPT=0 GIT_ASKPASS=/bin/true
HERE="$(cd "$(dirname "$0")" && pwd)"
. "$HERE/../lib/fetch_payload_to_file.sh"
# `ACTION XC` (registrada p246, descargada p247).  La escalera emite ahora la CLASE DE RUTA
# como columna 10, EN EL SITIO donde la ruta se decide.  p246 tuvo que escribir esa columna a
# mano y se equivoco tres veces en un pase: dos filas graduadas sobre un `NOTICE` -- que
# Apache-2.0 distingue de su propia licencia en su propio texto -- y una sobre
# `pyproject.toml`, cuyo campo `license` es una DECLARACION y no un payload.  El Tier A
# CONTIENE `NOTICE` y el Tier C es todo manifiestos, asi que el consumidor NO puede deducir
# la clase del tier: tiene que venir de la ruta.  `graduable_as_licence` es el unico predicado
# que hay que preguntar antes de pasarle un cuerpo a `family_of`.
. "$HERE/../p247-path-class/path_class.sh"

# Tier A — root licence names.  p228 probed six; the four additions are the ones this base has
# measured elsewhere: `COPYING.txt` (Moodle's own spelling), the British `LICENCE.txt`, the
# lowercase `copying.txt` (nvaccess/nvda) and `LICENSE.rst`.
# p247: `LICENSE-CODE` entra PRIMERA, y lo midio un falso positivo de este propio pase.
# `microsoft/autogen` trae DOS rutas de concesion: `LICENSE` es **CC-BY-4.0** (18.650 B, la
# licencia de la DOCUMENTACION) y `LICENSE-CODE` es **MIT** (la del codigo).  `LICENSE-CODE`
# no estaba en ninguno de los 40 nombres, asi que la escalera devolvia el payload de los
# DOCUMENTOS y un gate de primera mano habria "corregido" una celda `MIT` CORRECTA a
# `CC-BY-4.0`.  Releer de primera mano no es automaticamente mas seguro: leer el fichero
# EQUIVOCADO es una clase de error nueva, y es la familia de `ACTION XC` extendida de
# `NOTICE`/manifiesto a los HERMANOS de alcance partido.  El sujeto de estos estantes es
# software, asi que cuando las dos rutas existen la del CODIGO es la que gobierna.
# p256: SIETE rutas anadidas, y seis de ellas estaban PROBADAS en esta base antes de
# anadirse aqui -- que es el defecto, no el remedio.  `LICENSE.TXT` es exactamente la ruta
# que `P1057` (p189) publico con `openedx/XBlock` -- `11 358` B de Apache-2.0 verbatim,
# `raw.githubusercontent.com` es sensible a mayusculas -- y SESENTA Y SIETE pasadas despues
# seguia ausente de esta escalera, la que `make reach` imprime para que nadie la retipee.
# p256 volvio a tropezar con ella en `openedx/xblock-sdk`, HERMANO del repositorio de p189
# y en la MISMA organizacion.  `MIT-LICENSE` es la convencion de las gemas Rails y es donde
# `openstax/fine_print` guarda su concesion MIT real (`1 055` B, `0a9ed2a2ba710b61`);
# `LICENSE-MIT`/`LICENSE-APACHE` es la doble concesion de Rust.  `licence.txt` cerraba el
# hueco de la grafia britanica en minuscula, que estaba en TITULO pero no en minuscula.
# El coste es 7 peticiones mas por slug; el precio de no tenerlas fue dos verdictos falsos
# en una sola pasada.  `compose/code/pass256-ladder-closure/` lo sostiene mecanicamente.
TIER_A="LICENSE-CODE LICENSE LICENSE.md LICENSE.txt LICENSE.TXT LICENCE LICENCE.txt
licence.txt COPYING COPYING.txt COPYING.md COPYING.LESSER license.txt license.md
License.txt copying.txt LICENSE.rst NOTICE NOTICE.txt License licenses MIT-LICENSE
MIT-LICENSE.txt LICENSE-MIT LICENSE-APACHE APACHE-LICENSE-2.0.txt"
# Tier B — non-root licence paths THIS KB HAS ALREADY RECORDED, plus the SPDX `LICENSES/` dir.
TIER_B="docs/License.txt docs/LICENSE docs/LICENSE.txt docs/license.txt html/license.txt
public/COPYING.txt public/LICENSE public/license.txt LICENSE/LICENSE licenses/LICENSE
LICENSES/LICENSE legal/LICENSE doc/LICENSE app/LICENSE src/LICENSE"
# Tier C — manifest channels.  These carry a DECLARATION, not a licence body, so they are read
# by the ecosystem grammar (p222) and never by the body classifier.
TIER_C="version.php composer.json package.json pyproject.toml setup.py DESCRIPTION
__manifest__.py Cargo.toml pubspec.yaml setup.cfg"

nA=$(echo $TIER_A | tr ' ' '\n' | grep -c .)
nB=$(echo $TIER_B | tr ' ' '\n' | grep -c .)
nC=$(echo $TIER_C | tr ' ' '\n' | grep -c .)
if [ "${1:-}" = "--reach" ]; then
  echo "tierA=$nA tierB=$nB tierC=$nC total=$((nA+nB+nC)) byte-floor=1B ref=ls-remote-default+main+master"
  echo "--- TIER A (root licence names)";    echo $TIER_A | tr ' ' '\n' | grep .
  echo "--- TIER B (non-root licence paths)"; echo $TIER_B | tr ' ' '\n' | grep .
  echo "--- TIER C (manifest channels)";     echo $TIER_C | tr ' ' '\n' | grep .
  exit 0
fi

SLUGS="${1:?usage: ladder.sh <slugs-file> <out-dir>}"; OUT="${2:?}"; mkdir -p "$OUT"

while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  key=$(printf '%s' "$slug" | tr '/' '__')

  # --- existence + default branch + pinned SHA, in one request -----------------------------
  sym=$(timeout 45 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  if [ -z "$sym" ]; then
    # ABSENT is a DIFFERENT state from grantless, and p228 could not tell them apart.
    printf '%s\tABSENT\t-\t-\t-\t-\t-\t-\t-\t-\n' "$slug"
    continue
  fi
  defref=$(printf '%s' "$sym" | awk '/^ref:/{print $2}' | sed 's#refs/heads/##' | head -1)
  headsha=$(printf '%s' "$sym" | awk '!/^ref:/{print $1; exit}')
  [ -n "$defref" ] || defref="HEAD"

  # Refs to try: the REAL default first, then p228's two guesses (deduplicated) so that any
  # hit attributable purely to the ref axis is visible as such.
  refs="$defref"
  for g in main master; do [ "$g" = "$defref" ] || refs="$refs $g"; done

  hit=0
  for ref in $refs; do
    [ "$hit" = "1" ] && break
    for tier in A B C; do
      [ "$hit" = "1" ] && break
      case $tier in A) names="$TIER_A";; B) names="$TIER_B";; C) names="$TIER_C";; esac
      for path in $names; do
        dest="$OUT/$key.$tier.body"
        code=$(fetch_raw_to_file "$slug" "$ref" "$path" "$dest")
        if [ "$code" = "200" ]; then
          bytes=$(stat -c%s "$dest")
          # A 404 body is 14 B through this proxy, so the CODE is authoritative and the byte
          # count is recorded beside it rather than instead of it (p228's rule).
          sha=$(sha256sum "$dest" | cut -c1-12)
          mv "$dest" "$OUT/$key.body"
          printf '%s\tFOUND\t%s\t%s\t%s\t%s\t%s\t%s\ttier%s\t%s\n' \
                 "$slug" "$ref" "$headsha" "$path" "$code" "$bytes" "$sha" "$tier" \
                 "$(path_class "$path")"
          hit=1; break
        fi
        rm -f "$dest"
      done
    done
  done
  [ "$hit" = "1" ] || printf '%s\tNO-GRANT\t%s\t%s\t-\t404\t-\t-\t%d-paths-x-%d-refs\t-\n' \
                             "$slug" "$defref" "$headsha" "$((nA+nB+nC))" "$(echo $refs | wc -w)"
done < "$SLUGS"
