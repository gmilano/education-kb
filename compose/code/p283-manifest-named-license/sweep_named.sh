#!/bin/sh
# Barrido EN VIVO del pase 95: la accion PRE-REGISTRADA por el pase 94.
#
# Uso:  sh sweep_named.sh <slugs.txt>        (o)   sh sweep_named.sh --repos org/a org/b
# Salida: TSV por repo ->
#   slug  ref  testigo  veredicto  payload  familia  manifiesto  manifest_name  propiedad  nombrado  sondas
#
# El canal es `raw.githubusercontent.com`: contra `github.com/` y `api.github.com` este entorno
# devuelve 403 (medido hoy, 3 de 3), y citar un 403 como verificacion no es verificar (P247).
#
# Lo que este barrido hace y el del pase 94 no:
#   P279 -> no adivina el nombre del archivo: LEE `license-files` del manifiesto y sonda ESE
#           nombre, con su CAJA exacta.  La lista fija de variantes queda como respaldo.
#   P280 -> antes de atribuir la licencia de un manifiesto, compara el `name` que declara con
#           el repo que lo hospeda.  Si es de otro proyecto, NO la publica.
# La familia de licencia la classifica `lib/license_family.sh` (P237: no se reescribe).

set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
. "$HERE/../lib/license_family.sh"

RAW=https://raw.githubusercontent.com
# `HEAD` PRIMERO: resuelve la rama por omision cualquiera sea su nombre, que es lo que `P249`
# documento y lo que la v1 de este barrido NO uso (usaba solo la lista fija, así que un repo
# con rama por omision `trunk`/`dev` habria salido INDETERMINADO sin estarlo).
REFS="HEAD main master develop"
WITNESS="README.md readme.md README.rst README.txt README Readme.md .gitignore"
# Respaldo cuando el manifiesto no nombra nada. Matriz de CAJA incluida (es el hueco de P279).
VARIANTES="LICENSE LICENSE.txt LICENSE.TXT LICENSE.md LICENSE.rst LICENCE LICENCE.txt LICENCE.md
COPYING COPYING.txt COPYING.md COPYING.LESSER LICENSE-MIT LICENSE-APACHE LICENSE.html
license license.txt license.md licence LICENSE-2.0.txt UNLICENSE NOTICE"
MANIFESTS="pyproject.toml package.json composer.json Cargo.toml setup.cfg"

code() { curl -sI -o /dev/null -w '%{http_code}' --max-time 12 "$1" 2>/dev/null; }
body() { curl -s --max-time 12 "$1" 2>/dev/null; }

one() {
  r="$1"; n=0; ref=""; wit=""
  # --- 1. testigo de ALCANCE: sin el, una ausencia no es una ausencia (es INDETERMINADO)
  for w in $WITNESS; do
    for b in $REFS; do
      n=$((n+1))
      if [ "$(code $RAW/$r/$b/$w)" = 200 ]; then ref="$b"; wit="$w"; break 2; fi
    done
  done
  if [ -z "$ref" ]; then
    printf '%s\t-\t-\tINDETERMINADO\t-\t-\t-\t-\t-\t-\t%d\n' "$r" "$n"
    return
  fi
  # --- 2. el manifiesto, en la ref VIVA (P278: la ruta del payload es de la (repo,ref))
  mf=""; mname=""; mlic=""; mown=""; named=""
  for f in $MANIFESTS; do
    n=$((n+1))
    bd=$(body "$RAW/$r/$ref/$f")
    [ -z "$bd" ] && continue
    js=$(printf '%s' "$bd" | python3 "$HERE/manifest_license.py" "$f" "$r" 2>/dev/null)
    [ -z "$js" ] || [ "$js" = "null" ] && continue
    mf="$f"
    mname=$(printf '%s' "$js" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("name") or "-")' 2>/dev/null)
    mlic=$(printf '%s' "$js" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("license") or "-")' 2>/dev/null)
    mown=$(printf '%s' "$js" | python3 -c 'import json,sys; print(json.load(sys.stdin)["ownership"])' 2>/dev/null)
    named=$(printf '%s' "$js" | python3 -c 'import json,sys; print(" ".join(json.load(sys.stdin)["license_files"]))' 2>/dev/null)
    break
  done
  # --- 3. el nombre NOMBRADO por el manifiesto, con su caja exacta (P279)
  pay=""; via=""
  for nm in $named; do
    [ -z "$nm" ] && continue
    n=$((n+1))
    if [ "$(code $RAW/$r/$ref/$nm)" = 200 ]; then pay="$nm"; via="NOMBRADO"; break; fi
  done
  # --- 4. respaldo: la lista fija, en la ref viva
  if [ -z "$pay" ]; then
    for nm in $VARIANTES; do
      n=$((n+1))
      if [ "$(code $RAW/$r/$ref/$nm)" = 200 ]; then pay="$nm"; via="VARIANTE"; break; fi
    done
  fi
  # --- 5. veredicto
  fam="-"
  if [ -n "$pay" ]; then
    fam=$(osi_family_of "$(body $RAW/$r/$ref/$pay)")
    [ -z "$fam" ] && fam=UNCLASSIFIED
    ver="CON_LICENCIA"
  elif [ "$mown" = "OWN" ] || [ "$mown" = "WEAK" ]; then
    # sin archivo, pero el manifiesto del PROPIO proyecto declara una expresion
    if [ -n "$mlic" ] && [ "$mlic" != "-" ]; then ver="SOLO_MANIFIESTO"; fam="$mlic"; else ver="SIN_LICENCIA"; fi
  elif [ "$mown" = "FOREIGN" ]; then
    ver="SIN_LICENCIA"   # el manifiesto es de otro proyecto: su licencia NO cuenta (P280)
  else
    ver="SIN_LICENCIA"
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%d\n' \
    "$r" "$ref" "$wit" "$ver" "${pay:--}" "$fam" "${mf:--}" "${mname:--}" "${mown:--}" "${via:--}" "$n"
}

if [ "${1:-}" = "--repos" ]; then shift; printf '%s\n' "$@" > /tmp/p283.slugs.$$; SL=/tmp/p283.slugs.$$
else SL="${1:?uso: sh sweep_named.sh <slugs.txt> | --repos org/a ...}"; fi

if [ "${P283_ONE:-}" = 1 ]; then one "$2"; exit 0; fi
# Paralelo acotado: el canal tolera unas pocas en vuelo, y 40 repos x ~30 sondas en serie no termina.
grep -v '^[[:space:]]*$' "$SL" | grep -v '^#' | \
  xargs -P "${P283_JOBS:-6}" -I{} sh -c 'P283_ONE=1 sh "$0" x {}' "$0"
