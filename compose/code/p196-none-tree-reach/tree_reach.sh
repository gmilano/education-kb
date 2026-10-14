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
  return 1
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
