#!/usr/bin/env bash
# Suite de `p560`.  La referencia es EXTERNA al instrumento (`P417`): los fixtures son payloads
# REALES leidos de primera mano el 2026-10-07, no textos construidos para que el sweep pase.
#
# Y la parte que importa son los MUTANTES.  Un sweep que reporta «0 divergentes» sobre un
# clasificador ya arreglado no prueba nada: prueba lo mismo que un sweep roto que no mira nada
# (es la clase de `P541`).  Asi que cada defecto se REINTRODUCE en una copia de la libreria y se
# afirma que el sweep lo VUELVE A VER.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")" || exit 2

LIB=../lib/license_family.sh
FIX=fixtures
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

n=0; fail=0
check() { # check <nombre> <esperado> <obtenido>
  n=$((n+1))
  if [ "$2" = "$3" ]; then printf 'ok   %-62s %s\n' "$1" "$3"
  else printf 'FAIL %-62s esperado=%s obtenido=%s\n' "$1" "$2" "$3"; fail=$((fail+1)); fi
}

divergentes() { # divergentes <lib> -> cuenta de filas DIVERGENT
  bash sweep_versions.sh "$1" "$FIX" 2>/dev/null | awk -F'\t' '$5=="DIVERGENT"' | wc -l | tr -d ' '
}
familia() { # familia <lib> <fixture> -> family_of del payload
  bash sweep_versions.sh "$1" "$FIX" 2>/dev/null | awk -F'\t' -v f="$2" '$1==f{print $4}'
}

echo "== 1. El estado arreglado: ningun payload declara una version que el clasificador no da =="
check "libreria viva: 0 divergentes" 0 "$(divergentes "$LIB")"

echo
echo "== 2. Las ocho familias, leidas de payloads reales =="
check "EPL-1.0 real (junit-team/junit4, 11.374 B)"      EPL-1.0 "$(familia "$LIB" epl-1.0-junit4.LICENSE)"
check "EPL-2.0 real (hcengineering/platform, 14.196 B)" EPL-2.0 "$(familia "$LIB" epl-2.0-huly.LICENSE)"
check "EPL-2.0 real (eclipse-ee4j/jersey, 35.081 B)"    EPL-2.0 "$(familia "$LIB" epl-2.0-jersey.LICENSE)"
check "EPL-2.0 real (paho, 519 B, con EDL v1.0 dentro)" EPL-2.0 "$(familia "$LIB" epl-2.0-paho-with-edl-1.0.LICENSE)"
check "MPL-1.1 canonico (SPDX, 23.668 B)"               MPL-1.1 "$(familia "$LIB" mpl-1.1-spdx-canonical.LICENSE)"
check "MPL-2.0 real (mozilla/rhino, concesion parcial)" MPL-2.0 "$(familia "$LIB" mpl-2.0-rhino-partial-grant.LICENSE)"
check "NEG: MIT real (krayin) no lo toca ninguna rama"  MIT     "$(familia "$LIB" mit-krayin-webkul.LICENSE)"

echo
echo "== 3. MUTANTE A — se re-estampa la version de MPL (el defecto P561, que es P551 verbatim) =="
# Exactamente la linea que habia antes del arreglo.
sed -E 's#^(  if printf .%s. "\$t" \| grep -qi .Mozilla Public License.; then)#  printf "%s" "$t" | grep -qi "Mozilla Public License" \&\& { echo "MPL-2.0"; return; }\n\1#' \
  "$LIB" > "$TMP/mut_a.sh"
mut_a=$(divergentes "$TMP/mut_a.sh")
check "el mutante A reintroduce >=1 divergencia" SI "$([ "$mut_a" -ge 1 ] && echo SI || echo NO)"
check "y es MPL-1.1 la que vuelve a contestar 2.0" MPL-2.0 "$(familia "$TMP/mut_a.sh" mpl-1.1-spdx-canonical.LICENSE)"

echo
echo "== 4. MUTANTE B — se re-colapsa EPL (el defecto P560) =="
sed -E 's#^(  if printf .%s. "\$t" \| grep -qi .Eclipse Public License.; then)#  printf "%s" "$t" | grep -qi "Eclipse Public License" \&\& { echo "EPL"; return; }\n\1#' \
  "$LIB" > "$TMP/mut_b.sh"
mut_b=$(divergentes "$TMP/mut_b.sh")
check "el mutante B reintroduce >=4 divergencias (los 4 EPL)" SI "$([ "$mut_b" -ge 4 ] && echo SI || echo NO)"
check "y las dos versiones vuelven a dar el MISMO string (1.0)" EPL "$(familia "$TMP/mut_b.sh" epl-1.0-junit4.LICENSE)"
check "y las dos versiones vuelven a dar el MISMO string (2.0)" EPL "$(familia "$TMP/mut_b.sh" epl-2.0-huly.LICENSE)"

echo "== 5. Las DOS protecciones del payload de paho, medidas en 2x2 (no una sola, como se afirmo) =="
# ESTA SECCION REFUTO DOS VECES LA JUSTIFICACION CON LA QUE SE ESCRIBIO EL ARREGLO, y queda
# escrita asi porque la refutacion ES el resultado.
#
#   Afirmacion 1 (el comentario original del arreglo): «lo load-bearing es el ORDEN, 2.0 primero».
#     REFUTADA: se invirtio el orden y paho siguio contestando EPL-2.0.
#   Afirmacion 2 (el primer intento de este mutante): «entonces lo load-bearing es el ANCLA».
#     REFUTADA TAMBIEN: se desanclo la sonda de 1.0 dejandola segunda y paho siguio en EPL-2.0,
#     porque la sonda de 2.0 matchea antes y retorna.
#
# Lo medido es que las dos protecciones son REDUNDANTES: hace falta romper LAS DOS --sonda suelta
# Y puesta primera-- para que `eclipse/paho.mqtt.java` degrade a EPL-1.0.  Redundancia esta bien;
# afirmar que una sola es el control, cuando el mutante dice que no, no.
#
# Payload: 519 B que nombran «Eclipse Public License v2.0» Y «Eclipse Distribution License v1.0».
mutante() { # mutante <salida> <suelta:si|no> <primera:si|no>
  python3 - "$LIB" "$1" "$2" "$3" <<'PY'
import re, sys
src, out_path, suelta, primera = open(sys.argv[1]).read(), sys.argv[2], sys.argv[3], sys.argv[4]
pat2 = re.compile(r"    printf '%s' \"\$t\" \| grep -qiE 'eclipse public licen\[cs\]e[^\n]*\?2\\\.0' \\\n[^\n]*\n")
pat1 = re.compile(r"    printf '%s' \"\$t\" \| grep -qiE 'eclipse public licen\[cs\]e[^\n]*\?1\\\.0' \\\n[^\n]*\n")
m2, m1 = pat2.search(src), pat1.search(src)
assert m2 and m1, "los dos bloques EPL deben existir"
b2, b1 = m2.group(0), m1.group(0)
if suelta == 'si':
    b1 = "    printf '%s' \"$t\" | grep -qiE '1\\.0' \\\n        && { echo \"EPL-1.0\"; return; }\n"
new = (b1 + b2) if primera == 'si' else (b2 + b1)
out = src.replace(m2.group(0) + m1.group(0), new)
assert out != src, "el mutante no cambio nada"
open(out_path, 'w').write(out)
PY
}
mutante "$TMP/mut_anclada_primera.sh" no si
mutante "$TMP/mut_suelta_segunda.sh"  si no
mutante "$TMP/mut_suelta_primera.sh"  si si
P=epl-2.0-paho-with-edl-1.0.LICENSE
check "anclada + segunda (la libreria viva): 2.0"        EPL-2.0 "$(familia "$LIB" $P)"
check "anclada + PRIMERA: sigue 2.0 (el orden no decide)" EPL-2.0 "$(familia "$TMP/mut_anclada_primera.sh" $P)"
check "SUELTA + segunda: sigue 2.0 (el ancla no es la unica)" EPL-2.0 "$(familia "$TMP/mut_suelta_segunda.sh" $P)"
check "SUELTA + PRIMERA: AHORA SI degrada a 1.0"          EPL-1.0 "$(familia "$TMP/mut_suelta_primera.sh" $P)"
check "y el mutante que degrada no toca a Huly (sin EDL)" EPL-2.0 \
  "$(familia "$TMP/mut_suelta_primera.sh" epl-2.0-huly.LICENSE)"

echo
echo "== 6. El instrumento se niega en vez de reportar limpio sobre nada (P542) =="
bash sweep_versions.sh >/dev/null 2>&1; check "sin argumentos: exit 2" 2 "$?"
bash sweep_versions.sh "$LIB" /tmp/p560-no-existe >/dev/null 2>&1; check "corpus inexistente: exit 2" 2 "$?"
mkdir -p "$TMP/vacio"
bash sweep_versions.sh "$LIB" "$TMP/vacio" >/dev/null 2>&1; check "corpus VACIO: exit 2, no 'limpio'" 2 "$?"

echo
echo "== 7. Gap 249 declarado, no resuelto en silencio: el dual se reporta por un solo brazo =="
check "H2 (MPL-2.0 O EPL-1.0) contesta solo MPL-2.0" MPL-2.0 \
  "$(familia "$LIB" dual-mpl-2.0-or-epl-1.0-h2database.LICENSE)"

printf '\n%d/%d\n' "$((n-fail))" "$n"
[ "$fail" = 0 ] || exit 1
