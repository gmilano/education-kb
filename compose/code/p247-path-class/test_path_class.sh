#!/usr/bin/env bash
# Controles de `p247-path-class` (`ACTION XC`).
#
# Los tres casos que p246 publico como errores de categoria propios son controles aqui, con
# la ruta EXACTA que los produjo:
#   `foradian/fedena`    -> NOTICE
#   `openedx/XBlock`     -> pyproject.toml
# y los dos ficheros de codigo que la busqueda de codigo de p247 devolvio como «hits de
# licencia» de `redpanda-data/redpanda`:
#   `src/v/security/license.h`                 -> SOURCE-FILE
#   `src/go/rpk/pkg/cli/generate/license.go`   -> SOURCE-FILE
# Los cuatro son rutas REALES leidas en este repositorio o en la API, no inventadas.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/path_class.sh"

ok=0; bad=0
t() { # t <path> <expected>
  local got; got="$(path_class "$1")"
  if [ "$got" = "$2" ]; then ok=$((ok+1)); printf 'ok   %-48s %s\n' "$1" "$got"
  else bad=$((bad+1)); printf 'FAIL %-48s got=%s want=%s\n' "$1" "$got" "$2"; fi
}
tg() { # tg <path> <0|1 expected for graduable_as_licence>
  local got=1; graduable_as_licence "$1" && got=0
  if [ "$got" = "$2" ]; then ok=$((ok+1)); printf 'ok   graduable(%-37s)=%s\n' "$1" "$got"
  else bad=$((bad+1)); printf 'FAIL graduable(%s) got=%s want=%s\n' "$1" "$got" "$2"; fi
}

# ---- 1. grant texts -------------------------------------------------------------------
t LICENSE                LICENCE-PATH
t LICENSE.md             LICENCE-PATH
t LICENSE.txt            LICENCE-PATH
t LICENCE                LICENCE-PATH
t license.md             LICENCE-PATH
t COPYING                LICENCE-PATH
t COPYING.LESSER         LICENCE-PATH
t COPYRIGHT              LICENCE-PATH
t docs/License.txt       LICENCE-PATH
t html/license.txt       LICENCE-PATH
t LICENSE/LICENSE        LICENCE-PATH
t LICENSES/MIT.txt       LICENCE-PATH
t UNLICENSE              LICENCE-PATH
# los hermanos de alcance partido (p247, medido en `microsoft/autogen`)
t LICENSE-CODE           LICENCE-PATH
t LICENSE-MIT            LICENCE-PATH
t LICENSE-APACHE         LICENCE-PATH
t license-code.md        LICENCE-PATH

# ---- 2. the p246 category errors, by their real paths ---------------------------------
t NOTICE                 NOTICE
t NOTICE.txt             NOTICE
t notice.md              NOTICE
t pyproject.toml         MANIFEST
t package.json           MANIFEST
t composer.json          MANIFEST
t version.php            MANIFEST
t __manifest__.py        MANIFEST
t Cargo.toml             MANIFEST
t pubspec.yaml           MANIFEST
t setup.cfg              MANIFEST
t setup.py               MANIFEST
t DESCRIPTION            MANIFEST
t pom.xml                MANIFEST
t go.mod                 MANIFEST
t foo.gemspec            MANIFEST

# ---- 3. code that is NAMED like a licence (measured on redpanda-data/redpanda) --------
t src/v/security/license.h                     SOURCE-FILE
t src/v/security/license.cc                    SOURCE-FILE
t src/go/rpk/pkg/cli/generate/license.go        SOURCE-FILE
t src/license/license.hpp                      SOURCE-FILE
t licence.py                                   SOURCE-FILE
t LICENSE.sh                                   SOURCE-FILE
t copying.rb                                   SOURCE-FILE

# ---- 4. EULA keeps its own class --------------------------------------------------------
t EULA                   EULA
t EULA.txt               EULA
t eula.md                EULA

# ---- 5. vendored grants belong to someone else ------------------------------------------
t node_modules/left-pad/LICENSE        BUNDLED
t vendor/github.com/x/y/LICENSE        BUNDLED
t third_party/zlib/COPYING             BUNDLED
t .venv/lib/python3.11/site-packages/requests/LICENSE  BUNDLED

# ---- 6. nothing else is a grant ---------------------------------------------------------
t README.md              OTHER
t CONTRIBUTING.md        OTHER
t src/main.py            OTHER
t LICENSES/README.md     OTHER
t ""                     OTHER

# ---- 7. the one predicate a consumer should ask ------------------------------------------
tg LICENSE          0
tg EULA.txt         0
tg NOTICE           1
tg pyproject.toml   1
tg src/v/security/license.h  1
tg node_modules/x/LICENSE    1
tg README.md        1

echo
echo "$ok/$((ok+bad))"
[ "$bad" = "0" ] || exit 1
