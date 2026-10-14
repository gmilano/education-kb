# `lib/licence_path.sh` — ¿es esta RUTA un texto de concesion?, y ¿esta VENDORIZADA?
#
# p197.  Los dos predicados son los de `p196-none-tree-reach/tree_reach.sh`, COPIADOS
# BYTE A BYTE, no reescritos: `P237` dice que un clasificador no se vuelve a escribir, y
# `P441` dice que un predicado de RUTA no se vuelve a escribir como lista de nombres.  Viven
# aqui porque p196 pre-registro «promover los llamadores de la escalera de 19 nombres a este
# canal de arbol», y un predicado que hay que copiar para reusarlo se copia mal.
#
# El control de que la copia SIGUE siendo la copia esta en `test_licence_path.sh`: compara
# los cuerpos extraidos de los dos ficheros y falla si difieren en un byte.  Sin eso, esto
# es un fork con otro nombre.
#
# Uso:  . "$(dirname "${BASH_SOURCE[0]}")/licence_path.sh"
#       is_licence_path "LICENSE.TXT" && echo si
#       is_bundled "node_modules/x/LICENSE" && echo vendorizada

is_bundled() {
  case "$1" in
    */node_modules/*|node_modules/*|*/vendor/*|vendor/*|*/third_party/*|third_party/*) return 0 ;;
    */site-packages/*|*/dist-packages/*|*/.venv/*|.venv/*|*/venv/*|venv/*)             return 0 ;;
    */bower_components/*|*/Pods/*|*/.yarn/*|*/target/*|*/build/*|*/dist/*)             return 0 ;;
  esac
  return 1
}

is_licence_path() {
  local b d; b="$(basename "$1" | tr 'A-Z' 'a-z')"; d="$(dirname "$1" | tr 'A-Z' 'a-z')"
  # REUSE / SPDX convention: LICENSES/<SPDX-ID>.txt -- the basename is the SPDX id, not
  # "license", so a basename-only probe cannot see it.  My own suite refuted v1 on this.
  # v2: inside LICENSES/, everything is a grant EXCEPT the directory's own prose.
  case "$d" in licenses|*/licenses)
    case "$b" in readme|readme.*|index|index.*|notes|notes.*|.gitkeep) return 1 ;; esac
    return 0 ;;
  esac
  case "$b" in
    licence|license|licenses|licence.*|license.*|copying|copying.*|copyright|copyright.*) return 0 ;;
    unlicense|unlicence|unlicense.*|unlicence.*|notice|notice.*|eula|eula.*)              return 0 ;;
  esac
  return 1
}
