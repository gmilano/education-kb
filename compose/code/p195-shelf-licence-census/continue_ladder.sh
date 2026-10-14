# ACTION P195-B — the DEFECT in P195-A, and its repair.
#
# P195-A walked a frequency-ordered ladder and stopped at the FIRST 200.  For
# `shmercer/writeAlizer` the first 200 was `LICENSE` — 47 bytes reading only
# "YEAR:" / "COPYRIGHT HOLDER:".  That is the R/usethis MIT TEMPLATE STUB, not a grant.
# The real grant is `LICENSE.md`, 1076 B, MIT.  First-hit-wins is therefore WRONG for any
# repository carrying both a stub and a grant, and this KB already models the general case
# as `p627-multi-grant-repo`.
#
# 🟢 What did NOT fail: `lib/license_family.sh` returned UNCLASSIFIED on the 47-byte stub
# rather than inventing MIT from the word "COPYRIGHT".  The classifier guard held; the
# LADDER was the defect.  So the repair walks the WHOLE ladder for every row the classifier
# could not classify, and reports every licence-shaped path, not the first.
set -u
_HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$_HERE/../lib/payload_measure.sh"
LADDER="LICENSE LICENSE.md LICENSE.txt COPYING license.txt LICENCE LICENSE.rst LICENCE.md \
license license.md licence.txt COPYING.txt COPYRIGHT NOTICE MIT-LICENSE MIT-LICENSE.txt \
LICENSE-MIT LICENSE-APACHE UNLICENSE"
for slug in "$@"; do
  for fn in $LADDER; do
    tmp="$(mktemp)"
    code="$(curl -s -L --max-time 25 -o "$tmp" -w '%{http_code}' \
            "https://raw.githubusercontent.com/$slug/HEAD/$fn" 2>/dev/null)" || code=000
    if [ "$code" = 200 ]; then
      printf '%s\t%s\t%s\t%s\n' "$slug" "$fn" "$(size_of_file "$tmp")" "$(family_of_file "$tmp")"
    fi
    rm -f "$tmp"
  done
done
