#!/bin/sh
# C11 — control de E1: una ruta con COMILLA debe sobrevivir al barrido.
#
# `xargs -I{}` procesa comillas por defecto.  La ruta real
# `content-pool/a343428l'hopital2/a343428l'hopital2.json` (la regla de L'Hopital) llegaba
# al curl SIN la comilla -> 404 -> y el cuerpo «404: Not Found» entraba al clasificador.
# Este control afirma las DOS mitades: que el modo viejo PIERDE la comilla, y que el
# modo nuevo (-d '\n') la conserva.  Sin la primera mitad, el defecto es prosa.
ok=0; fail=0
P="content-pool/a343428l'hopital2/a343428l'hopital2.json"
TMP=$(mktemp -d); printf '%s\n' "$P" > "$TMP/in.txt"

got_new=$(xargs -a "$TMP/in.txt" -d '\n' -I{} -P 1 sh -c 'printf "%s" "$1"' _ {})
if [ "$got_new" = "$P" ]; then
  ok=$((ok+1)); echo "  ok   C11a modo nuevo (-d '\\n') conserva la comilla"
else
  fail=$((fail+1)); echo "  FAIL C11a esperado [$P] dio [$got_new]"
fi

got_old=$(xargs -a "$TMP/in.txt" -I{} -P 1 sh -c 'printf "%s" "$1"' _ {} 2>/dev/null)
if [ "$got_old" != "$P" ]; then
  ok=$((ok+1)); echo "  ok   C11b modo viejo PIERDE la comilla (dio [$got_old]) — el defecto esta aserido"
else
  fail=$((fail+1)); echo "  FAIL C11b el modo viejo no reprodujo el defecto: el control no vale"
fi
rm -rf "$TMP"
echo ""; echo "$ok/$((ok+fail))"
[ "$fail" -eq 0 ]
