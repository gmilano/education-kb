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
    # 🟢 p279: two vendoring conventions this corpus actually uses and this predicate did
    # not know.  Found by the per-package manifest walk, not by reading: `tadreeblms`
    # bundles `moment`, `swiper`, `tailwindcss`, `prismjs` and three CKEditor builds under
    # `public/assets/libs/`, and `LearnPress` bundles `wp-background-process` under
    # `inc/libraries/` (the WordPress plugin convention).  Counted as the repository's own
    # per-package declarations, they turned ten dependency licences into a false
    # "SUBPACKAGES DISAGREE" verdict.
    # 🔵 A path vocabulary can only reject the conventions somebody enumerated, which is
    # why this list is a floor and not a proof -- see `T229-M2` for the NAME channel, and
    # the residual `ui/static/pyodide/` that neither channel safely catches.
    */assets/libs/*|assets/libs/*|*/inc/libraries/*|inc/libraries/*)                   return 0 ;;
    # 🔴 THE SAME REPOSITORY VENDORS THE SAME LIBRARIES TWICE, UNDER TWO SPELLINGS.
    # `tadreeblms` carries `moment`, `swiper`, `tailwindcss`, `prismjs` and three CKEditor
    # builds under `public/assets/libs/` AND again under
    # `resources/views/backend/assetslib/libs/`.  Adding `assets/libs` above caught the
    # first copy and left the second, so the repository still published a false
    # "SUBPACKAGES DISAGREE" on CKEditor's GPL-2.0.
    # 🔵 This is the measured proof that a path vocabulary is a FLOOR AND NOT A PROOF: one
    # repository defeated it twice in one hour.  The durable channel is the one that reads
    # the package NAME against a list of known third-party projects, which this base does
    # not have -- registered for `p280`, and until it exists every vendored-manifest count
    # here is a LOWER BOUND.
    */assetslib/*|assetslib/*)                                                         return 0 ;;
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
  # p256 -- the TOKEN form, added because a real payload defeated the globs above.
  # `openstax/fine_print` keeps its MIT grant at `MIT-LICENSE` (1 055 B, read first-hand
  # this pass); the globs are dot-anchored, so a HYPHENATED token is invisible to them.
  # `MIT-LICENSE` is the Rails/Ruby gem convention and `LICENSE-MIT` + `LICENSE-APACHE`
  # the Rust dual-grant one.  P441: this is the FORM, not a list of tokens.
  case "$b" in
    *-licence*|*-license*|licence-*|license-*|licences-*|licenses-*|copying-*) ;;
    *) return 1 ;;
  esac
  # ...and the guard that stops the form swallowing PROSE ABOUT a grant.  Without it
  # `license-faq.md` and `third-party-license-report.json` would both grade as grants,
  # which is `p782-policy-gate`'s class arriving through a path instead of a payload.
  case "${b%%.*}" in
    *faq|*policy|*report|*notes|*guide|*header|*check|*template|*list|*scan|*summary|*index|*readme) return 1 ;;
  esac
  return 0
}
