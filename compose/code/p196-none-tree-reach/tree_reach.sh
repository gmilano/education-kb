# ACTION P196-D -- p969's open limb, run with the instrument this KB ALREADY HOLDS.
#
# p195 pre-registered this as: "Probe docs/, legal/, .github/ for the 88 root-NONE rows".
# 🔴 THAT IS THE DEFECT P441 NAMED AND PROVED: "widening a list cannot fix a list".  P441
# measured it three times over -- a 14-name list missed openedx/XBlock's LICENSE.TXT, p440's
# 41-name widening missed it a THIRD time -- and established the channel that sustains an
# ABSENCE instead of merely failing to find a presence:
#     git clone --filter=blob:none --no-checkout --depth 1   # commit + trees, no blobs
#     git ls-tree -r --name-only HEAD                        # COMPLETE tree, unpaginated
# So this runs P441's channel, not p195's three directories.  3 named directories cannot
# distinguish "no licence" from "no licence WHERE I LOOKED"; the complete tree can.
#
# Emits: slug  paths_in_tree  own_root  own_subtree  bundled  verdict
#   ABSENCE-ENUMERATED  no path in the complete tree is a licence text (the only verdict a
#                       filename list can never reach)
#   OWN-GRANT-AT-ROOT   a root licence text the 19-name ladder missed
#   OWN-GRANT-IN-SUBTREE a licence text below the root, outside vendored paths
#   BUNDLED-GRANT-ONLY  every licence text found belongs to a vendored dependency
#   CLONE-FAILED        channel error, reported not hidden
set -u
OUT="${1:?out tsv}"; IN="${2:?slug list}"
WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT

# Vendored-path exclusions: imported from p441/p436 rather than rewritten (P126 rule 1).
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
    # 🟢 p280, FOUND BY ENUMERATION AND NOT BY READING: `codeXsidd/Studivexa` serves
    # `frontend/.vite/deps/package.json` -- Vite's dependency-optimiser CACHE, a build
    # artefact committed to the tree.  This predicate knew `*/dist/*`, `*/build/*` and
    # `*/.yarn/*` and not `.vite`, so the cache was in the manifest walk's denominator.
    # 🔵 It graded SILENT (no name, no licence field) so no count was corrupted TODAY --
    # which is the whole argument for widening a floor from a measurement rather than from
    # a defect: the next cache directory to carry a `license` field would have been counted.
    # Measured: `evidence/package-provenance.2026-10-18-p280.tsv`.
    */.vite/*|.vite/*|*/.next/*|.next/*|*/.nuxt/*|.nuxt/*|*/.turbo/*|.turbo/*)         return 0 ;;
  esac
  return 1
}
# A path is a licence TEXT by basename.  Case-insensitive on purpose: P441's whole point is
# that LICENSE.TXT, license, COPYING.txt and licence are the same artefact.
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

printf 'slug\tpaths_in_tree\town_root\town_subtree\tbundled\tverdict\n' > "$OUT"
n=0
while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  n=$((n+1))
  d="$WORK/r$n"
  if ! git clone --filter=blob:none --no-checkout --depth 1 -q \
        "https://github.com/$slug" "$d" 2>/dev/null; then
    printf '%s\t-\t-\t-\t-\tCLONE-FAILED\n' "$slug" >> "$OUT"; continue
  fi
  paths="$(git -C "$d" ls-tree -r --name-only HEAD 2>/dev/null)" || paths=""
  total=$(printf '%s' "$paths" | grep -c . || true)
  root=0; sub=0; bun=0
  while IFS= read -r p; do
    [ -z "$p" ] && continue
    is_licence_path "$p" || continue
    if is_bundled "$p"; then bun=$((bun+1))
    elif [ "$p" = "$(basename "$p")" ]; then root=$((root+1))
    else sub=$((sub+1)); fi
  done <<< "$paths"
  if   [ "$root" -gt 0 ]; then v=OWN-GRANT-AT-ROOT
  elif [ "$sub"  -gt 0 ]; then v=OWN-GRANT-IN-SUBTREE
  elif [ "$bun"  -gt 0 ]; then v=BUNDLED-GRANT-ONLY
  else v=ABSENCE-ENUMERATED; fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$total" "$root" "$sub" "$bun" "$v" >> "$OUT"
  rm -rf "$d"
done < "$IN"
