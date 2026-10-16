#!/usr/bin/env bash
# `ACTION XB` (p246) — correr el gate de integridad sobre el TIER MIT, que nunca se barrio.
#
# p246 barrio los `313` slugs `Apache-2.0` y encontro `1` payload CONFLICTED en `321`
# (`0xnavarro/IA-PARA-TODOS`: un conflicto de merge sin resolver DENTRO de un `LICENSE`, con
# el titular real y la plantilla de la ASF los dos presentes).  Registro el tier MIT como
# `9x` mas grande y nunca barrido, con un presupuesto estimado de ~`2 700` peticiones.
#
# PRIMERA CORRECCION, medida antes de gastar una peticion: son `2 801` CELDAS pero `881`
# SLUGS DISTINTOS.  El presupuesto de `ACTION XB` contaba celdas, y una celda no es una
# peticion -- el mismo repositorio aparece en ocho estantes.  `881` cabe en un pase.
#
# ESTO ES UN COSECHADOR, NO UN CLASIFICADOR (regla P237): trae y anota.  Deciden
# `lib/license_family.sh`, `p246-payload-integrity` y `p247-keyed-grant`.
#
# LO QUE ESTE BARRIDO **NO** HACE, dicho aqui porque la omision tiene que viajar con el dato:
# no corre `git ls-remote`, asi que la rama es una ADIVINANZA (`main`, luego `master`) -- la
# via que `p229` midio como indistinguible de un repositorio sin concesion.  Un slug cuya
# rama por defecto sea `develop` o `trunk` sale como `UNREAD`, y `UNREAD` NO ES UNA AUSENCIA
# (`ACTION UK`).  Se publica como tal: el denominador del barrido son los payloads LEIDOS.
#
# usage: sweep.sh <slugs-file> <out-dir> [parallelism]
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="${2:?usage: sweep.sh <slugs-file> <out-dir> [parallelism]}"
SLUGS="${1:?}"
PAR="${3:-10}"
mkdir -p "$OUT/bodies"

probe_one() {
  local slug="$1" out="$2" key dest code
  key="$(printf '%s' "$slug" | tr '/' '_')"
  dest="$out/bodies/$key.body"
  for ref in main master; do
    for path in LICENSE LICENSE.md LICENSE.txt LICENCE COPYING; do
      code=$(curl -sS -o "$dest.tmp" -w '%{http_code}' --max-time 25 \
             "https://raw.githubusercontent.com/$slug/$ref/$path" 2>/dev/null || echo 000)
      if [ "$code" = "200" ]; then
        mv "$dest.tmp" "$dest"
        printf '%s\tREAD\t%s\t%s\t%s\n' "$slug" "$ref" "$path" "$(stat -c%s "$dest")"
        return 0
      fi
      rm -f "$dest.tmp"
    done
  done
  # 5 nombres x 2 ramas adivinadas.  NO es «sin concesion»: es sin leer.
  printf '%s\tUNREAD\t-\t5-paths-x-2-guessed-refs\t-\n' "$slug"
}
export -f probe_one

xargs -a "$SLUGS" -I{} -P "$PAR" bash -c 'probe_one "$@"' _ {} "$OUT"
