#!/bin/sh
# p288 — el caso que las 41 aserciones de `lib/test_license_family.sh` NO ejercitaban.
#
# Todas las fixtures AGPL de esa suite empiezan con el titulo CANONICO EN MAYUSCULAS, y la
# rama AGPL de `osi_family_of` es un glob de `case`, que es SENSIBLE A LA CAJA.  Un payload
# AGPL-3.0 REFLOWED (sin linea de titulo en mayusculas) cae por esa rama, y entonces lo
# atrapa la rama GPL —que usa `grep -qi`, insensible— porque el PREAMBULO DE LA PROPIA AGPL
# dice «The GNU General Public License permits making a modified version and letting the
# public access it on a server...».  Veredicto: GPL-3.0.  Es P171 reabierto por la caja.
#
# Esto es P126 punto 2 al pie de la letra: un control positivo que pasa no habilita un
# instrumento si no ejercita el caso donde ese instrumento puede fallar.
#
# Invocacion: sh test_casefold.sh
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
. "$HERE/../lib/license_family.sh"
n=0; bad=0
check() { # check <nombre> <esperado> <obtenido>
  n=$((n+1))
  if [ "$2" = "$3" ]; then printf 'ok   %-58s %s\n' "$1" "$3"
  else printf 'FAIL %-58s esperado=%s obtenido=%s\n' "$1" "$2" "$3"; bad=$((bad+1)); fi
}

KFS=$(cat "$HERE/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE")

# --- 1. el caso que faltaba: AGPL-3.0 reflowed, sin titulo en mayusculas
check "AGPL-3.0 reflowed (kuali/kfs) es AGPL-3.0" AGPL-3.0 "$(osi_family_of "$KFS")"
check "la fixture NO trae el titulo canonico en mayusculas" 0 \
  "$(head -40 "$HERE/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE" | grep -c 'GNU AFFERO GENERAL PUBLIC LICENSE')"
check "la fixture SI nombra la AGPL en caja mixta" 3 \
  "$(head -40 "$HERE/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE" | grep -c 'GNU Affero General Public License')"
check "el ancla definitoria de la seccion 0 esta presente" 1 \
  "$(grep -c 'refers to version 3 of the GNU Affero General Public License' "$HERE/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE")"

# --- 2. el caso NEGATIVO que mantiene P171 cerrado: la seccion 13 de la GPL-3.0 NO es un ancla.
#        La GPL-3.0 dice «...licensed UNDER version 3 of the GNU Affero...»; la AGPL dice
#        «...REFERS TO version 3 of the GNU Affero...».  El ancla lleva «refers to» por eso.
GPL3_S13='                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

  0. Definitions.
  "This License" refers to version 3 of the GNU General Public License.

  13. Use with the GNU Affero General Public License.
  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.'
check "GPL-3.0 con su seccion 13 sigue siendo GPL-3.0 (P171)" GPL-3.0 "$(osi_family_of "$GPL3_S13")"
check "la seccion 13 de la GPL NO contiene el ancla 'refers to ... Affero'" 0 \
  "$(printf '%s' "$GPL3_S13" | grep -c 'refers to version 3 of the GNU Affero')"

# --- 3. no se rompe lo que ya andaba: el titulo canonico en mayusculas
AGPL_CANON='                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007'
check "AGPL canonica en mayusculas sigue siendo AGPL-3.0" AGPL-3.0 "$(osi_family_of "$AGPL_CANON")"

# --- 4. el uso comercial no se altera: la AGPL-3.0 lo permite (P250)
if commercial_use_ok "$KFS"; then r=allowed; else r=forbidden; fi
check "AGPL-3.0 reflowed permite uso comercial (P250)" allowed "$r"

# --- 5. el limite DECLARADO de affero_lines: es un conteo de LINEAS, y las lineas dependen
#        del REFLOW, no del contenido.  Los polos calibrados en el pase 77 (3 contra 15) NO
#        son portables, y esta fixture es la prueba: 10, ni 3 ni 15.
check "affero_lines sobre la fixture reflowed" 10 "$(affero_lines "$KFS")"

printf '\n%d/%d\n' "$((n-bad))" "$n"
[ "$bad" -eq 0 ] || exit 1
