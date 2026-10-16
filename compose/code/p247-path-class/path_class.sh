# `p247-path-class` — ¿QUE CLASE DE COSA es la ruta que la escalera acaba de traer?
#
# `ACTION XC` (p246).  p246 publico `3` de sus `10` veredictos crudos `NOT-APACHE` como
# errores de CATEGORIA suyos: `foradian/fedena` y `projectfedena/fedena` se graduaron sobre un
# **`NOTICE`** (y Apache-2.0 distingue en su propio texto `LICENSE` de `NOTICE`), y
# `openedx/XBlock` sobre **`pyproject.toml`** (el campo `license` de un manifiesto es una
# DECLARACION, no un payload).  El Tier A de la escalera CONTIENE `NOTICE` y el Tier C es
# todo manifiestos, asi que CUALQUIER consumidor que gradue el payload devuelto como texto de
# licencia repite el error.  p246 publico la columna A MANO en su tabla de evidencia y
# registro que el pase siguiente la tomara DE LA ESCALERA.  Esto es eso.
#
# POR QUE NO VIVE EN `lib/licence_path.sh`, que seria el sitio obvio: el cuerpo de ese fichero
# es una COPIA BYTE A BYTE de `p196-none-tree-reach/tree_reach.sh` y su propia suite FALLA si
# difiere en un byte (P441/P237).  Editarlo para anadir una clase mas lo convertiria en un
# fork con otro nombre -- el defecto que ese control existe para impedir.  Asi que esta
# funcion COMPONE el predicado compartido en vez de reescribirlo, y el predicado sigue siendo
# el unico que decide «¿es una ruta de concesion?».
#
# Y COMPONER LO MIDIO.  `is_licence_path` contesta YES sobre `src/v/security/license.h` y
# sobre `license.go` -- un cabecero C y un fichero Go, porque el basename es `license.*`.  No
# es hipotetico: la busqueda de codigo de este mismo pase devolvio esos dos ficheros exactos
# de `redpanda-data/redpanda` como «hits de licencia».  Un payload de 200 lineas de C++
# graduado por un clasificador de licencias contesta `UNCLASSIFIED`, y `UNCLASSIFIED` es la
# rama que CAE AL TOKEN-MATCH de `commercial_use_ok` (P171).  Entonces la clase de ruta no es
# cosmetica: es una via mas al mismo ALLOWED.
#
# Uso:  . "$(dirname "${BASH_SOURCE[0]}")/path_class.sh"
#       path_class "NOTICE"            -> NOTICE
#       path_class "pyproject.toml"    -> MANIFEST
#       path_class "LICENSE"           -> LICENCE-PATH
#
# Las clases, y lo que cada una le dice al consumidor:
#   LICENCE-PATH  graduable como texto de concesion
#   NOTICE        NO graduable: Apache-2.0 lo distingue de su propia licencia
#   EULA          graduable, pero NO es una licencia abierta -- se separa para que un
#                 lector no la cuente como una
#   MANIFEST      una DECLARACION (`license: MIT`), no un payload: la lee la gramatica de
#                 ecosistema de `p222`, nunca el clasificador de cuerpo
#   SOURCE-FILE   codigo que se llama `license.*` -- el error de categoria medido arriba
#   BUNDLED       una concesion VENDORIZADA: es de otro, no del repositorio
#   OTHER         ninguna de las anteriores

__pc_here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=../lib/licence_path.sh
. "$__pc_here/../lib/licence_path.sh"

# Extensiones de CODIGO.  Un fichero cuyo basename es `license.<ext>` con una de estas no es
# un payload de concesion aunque el predicado compartido diga que si.
__PC_SOURCE_EXT="h c cc cpp cxx hpp hh go py js jsx ts tsx java rb rs php cs swift kt kts
m mm sh bash zsh pl pm lua sql tf vue svelte dart scala clj ex exs erl hs ml fs r"

path_class() {
  local p="$1" b d ext
  b="$(basename "$p" | tr 'A-Z' 'a-z')"
  d="$(dirname "$p" | tr 'A-Z' 'a-z')"

  # 1. VENDORIZADA gana sobre todo lo demas: una concesion dentro de `node_modules/` describe
  #    a un tercero, y atribuirla al repositorio es el error de categoria mas grande de todos.
  if is_bundled "$p"; then echo "BUNDLED"; return 0; fi

  # 2. MANIFIESTOS — el Tier C de la escalera, mas los que este KB ha leido en otros canales.
  case "$b" in
    version.php|composer.json|package.json|pyproject.toml|setup.py|description|\
__manifest__.py|cargo.toml|pubspec.yaml|setup.cfg|package-lock.json|composer.lock|\
*.gemspec|*.podspec|*.cabal|build.gradle|pom.xml|go.mod|*.nuspec|project.clj)
      echo "MANIFEST"; return 0 ;;
  esac
  # `DESCRIPTION` de R es el unico manifiesto SIN extension del Tier C, y en minuscula choca
  # con nada mas en estas listas, asi que se resuelve arriba por nombre exacto.

  # 3. NOTICE y EULA, cada uno con su propia clase, ANTES de la via generica de concesion --
  #    las dos entran por `is_licence_path` y las dos significan otra cosa.
  case "$b" in notice|notice.*) echo "NOTICE"; return 0 ;; esac
  case "$b" in eula|eula.*)     echo "EULA";   return 0 ;; esac

  # 3b. Los HERMANOS de alcance partido.  `LICENSE-CODE` (la convencion de Microsoft: el
  #     `LICENSE` de la raiz es CC-BY-4.0 para los documentos y `LICENSE-CODE` es MIT para el
  #     codigo) y los `LICENSE-MIT`/`LICENSE-APACHE` del mundo Rust son RUTAS DE CONCESION, y
  #     `is_licence_path` no los ve porque su basename no empieza por `license` sin sufijo.
  #     Medido en p247 sobre `microsoft/autogen`: el payload MIT real vive en `LICENSE-CODE`.
  case "$b" in
    license-code|licence-code|license-mit|license-apache|license-apache-2.0|\
license-bsd|license-gpl|license-agpl|license-code.*|license-mit.*|license-apache.*)
      echo "LICENCE-PATH"; return 0 ;;
  esac

  # 4. El predicado COMPARTIDO decide el resto.  Nada se reescribe aqui.
  #
  #    `SOURCE-FILE` es un RESCATE de este predicado, no un clasificador de tipos de fichero:
  #    solo se pregunta por la extension CUANDO el predicado compartido ya reclamo la ruta
  #    como concesion.  Esa distincion es la que mantiene `src/main.py` en `OTHER` -- un
  #    fichero de codigo que NO se llama como una licencia nunca estuvo en riesgo de que un
  #    clasificador de licencias lo leyera, y meterlo en `SOURCE-FILE` convertiria la clase en
  #    una afirmacion sobre el repositorio entero en vez de sobre el error medido.
  if is_licence_path "$p"; then
    ext="${b##*.}"
    if [ "$ext" != "$b" ]; then
      for e in $__PC_SOURCE_EXT; do
        if [ "$ext" = "$e" ]; then echo "SOURCE-FILE"; return 0; fi
      done
    fi
    echo "LICENCE-PATH"; return 0
  fi

  echo "OTHER"; return 0
}

# `graduable_as_licence <path>` — el unico predicado que un consumidor deberia preguntar antes
# de pasarle el payload a `family_of`.  Se expone con nombre propio para que la decision no se
# reconstruya en cada llamador (que es como p246 cometio el error tres veces en un pase).
graduable_as_licence() {
  case "$(path_class "$1")" in
    LICENCE-PATH|EULA) return 0 ;;
    *) return 1 ;;
  esac
}
