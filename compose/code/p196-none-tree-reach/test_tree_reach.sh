# Offline suite for the two pure predicates.  The cases are the ones P441 and p140 published
# as having DEFEATED earlier filename lists -- the external reference of P417.
set -u
. /dev/stdin <<'FNS'
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
FNS
t=0; p=0
yes_lic() { t=$((t+1)); if is_licence_path "$1"; then p=$((p+1)); else echo "FAIL want-licence: $1"; fi; }
no_lic()  { t=$((t+1)); if is_licence_path "$1"; then echo "FAIL want-NOT-licence: $1"; else p=$((p+1)); fi; }
yes_bun() { t=$((t+1)); if is_bundled "$1"; then p=$((p+1)); else echo "FAIL want-bundled: $1"; fi; }
no_bun()  { t=$((t+1)); if is_bundled "$1"; then echo "FAIL want-NOT-bundled: $1"; else p=$((p+1)); fi; }

# the three real rows that defeated this KB's earlier lists
yes_lic "LICENSE.TXT"                             # openedx/XBlock -- missed 3x by lists
yes_lic "package/license"                         # @learninglocker/xapi-agents -- lowercase, extensionless
yes_lic "aoe-web-frontend/LICENSE"                # Opetushallitus/aoe -- EUPL in a subdirectory
yes_lic "COPYING.txt"                             # the GNU-world name trend 252 recorded
yes_lic "docs/License.txt"                        # OS4ED/openSIS-Classic -- p969's root-only miss
yes_lic "LICENSE"; yes_lic "licence"; yes_lic "COPYING"; yes_lic "LICENSE.md"
yes_lic "NOTICE.txt"                              # p140: where XBlock/codejail record ownership
yes_lic "LICENSES/MIT.txt"            # REUSE/SPDX convention -- refuted v1 of this instrument
yes_lic "LICENSES/GPL-3.0-or-later.txt"
no_lic  "licenses/README.md"
no_lic  "README.md"; no_lic  "src/licensing.py"; no_lic "LICENSE_HEADER_CHECK.cfg"
no_lic  "licenses.json"                           # a manifest, not a licence text
# bundled exclusions, imported from p441/p436
yes_bun "node_modules/foo/LICENSE"; yes_bun "vendor/bar/COPYING"
yes_bun "web/third_party/x/LICENSE"; yes_bun ".venv/lib/LICENSE"
no_bun  "LICENSE"; no_bun  "docs/License.txt"; no_bun "aoe-web-frontend/LICENSE"
echo "$p/$t"; [ "$p" = "$t" ] || exit 1
