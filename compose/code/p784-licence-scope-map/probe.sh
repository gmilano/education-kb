#!/usr/bin/env bash
# p784 -- licence SCOPE probe.  Gap 282's bounded remedy.
#
# Every licence probe on this shelf answers the question "WHERE does the grant hide?"
# (p759's four layers: file -> below-reference -> manifest -> headers) and returns a
# SCALAR family.  Measured counter-example, pass 60: haolpku/K12-KGraph @ 865bc35 ships
# TWO licence files with DIFFERENT SCOPES -- `LICENSE` = CC BY-NC-SA 4.0 (the dataset),
# `LICENSE-CODE` = MIT (the code).  A probe that breaks on the first of the 16 filenames
# returns NC and wrongly REJECTS usable MIT code; one that happened to order LICENSE-CODE
# first returns MIT and wrongly ADMITS an NC dataset.  Both directions are wrong.
#
# So this probe does not break.  It enumerates ALL names and emits a {path -> family} map.
# Exit status is the VERDICT, not an error code:
#   0 = SINGLE      -- one family across every grant found (the scalar case, still common)
#   3 = PARTITIONED -- more than one family; the caller MUST read scope before building
#   4 = UNGRANTED   -- no grant at any of the names
#
# Usage: scope_probe.sh owner/repo [ref]
set -u

NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENSE-MIT LICENSE-APACHE \
COPYING COPYING.txt COPYING.LESSER LICENSE.rst license license.md LICENSE.code LICENSE-CODE \
LICENSE-DATA"

# family(): title-line classifier.  Deliberately NOT a body substring test -- P753/P773:
# every GNU text NAMES ITS RELATIVES, so GPL-2.0's preamble (line 18) says "GNU Lesser
# General Public License" and a lowercased body match mislabels it LGPL.  Three passes in
# a row (58, 59, 60) made exactly that error.  The gates below are UPPERCASE and anchored.
family() {
  local t up
  t="$1"
  up=$(printf '%s' "$t" | head -c 4000 | tr '[:lower:]' '[:upper:]')
  # P775 / Gap 281: the gates are applied to an UPPERCASED copy, so a reflowed or
  # uppercased payload classifies the same as a title-cased one.  The shared lib's
  # `case` glob is case-SENSITIVE and this is the divergence Gap 281 asked to close.
  case "$up" in
    *"GNU AFFERO GENERAL PUBLIC LICENSE"*) echo "AGPL-3.0"; return ;;
  esac
  # LGPL only when the LESSER text is the TITLE, not when it is merely named.  Measured:
  # restrict to the first 400 B, which is the title block proper; GPL-2.0's preamble
  # mention sits at line 18, outside it.
  local head400
  head400=$(printf '%s' "$up" | head -c 400)
  case "$head400" in
    *"GNU LESSER GENERAL PUBLIC LICENSE"*)
      case "$up" in *"VERSION 2.1"*) echo "LGPL-2.1" ;; *) echo "LGPL-3.0" ;; esac
      return ;;
  esac
  case "$up" in
    *"GNU GENERAL PUBLIC LICENSE"*)
      case "$up" in
        *"VERSION 2, JUNE 1991"*) echo "GPL-2.0" ;;
        *"VERSION 3"*)            echo "GPL-3.0" ;;
        *)                        echo "GPL-?"   ;;
      esac
      return ;;
    *"ATTRIBUTION-NONCOMMERCIAL-SHAREALIKE"*) echo "CC-BY-NC-SA-4.0"; return ;;
    *"ATTRIBUTION-NONCOMMERCIAL"*)            echo "CC-BY-NC-4.0";    return ;;
    *"ATTRIBUTION-SHAREALIKE"*)               echo "CC-BY-SA-4.0";    return ;;
    *"CREATIVE COMMONS ATTRIBUTION"*)         echo "CC-BY-4.0";       return ;;
    *"APACHE LICENSE"*)                       echo "Apache-2.0";      return ;;
    *"MOZILLA PUBLIC LICENSE"*)               echo "MPL-2.0";         return ;;
    *"MIT LICENSE"*|*"THE MIT LICENSE"*)      echo "MIT";             return ;;
    *"BSD 3-CLAUSE"*|*"REDISTRIBUTION AND USE IN SOURCE AND BINARY FORMS"*)
      case "$up" in
        *"NEITHER THE NAME"*) echo "BSD-3-Clause" ;;
        *)                    echo "BSD-2-Clause" ;;
      esac
      return ;;
    *"PERMISSION IS HEREBY GRANTED, FREE OF CHARGE"*) echo "MIT"; return ;;
  esac
  echo "UNCLASSIFIED"
}

repo="${1:?usage: scope_probe.sh owner/repo [ref]}"
ref="${2:-HEAD}"

if [ "$ref" = "HEAD" ]; then
  sha=$(git ls-remote "https://github.com/$repo" HEAD 2>/dev/null | awk '{print $1}')
  [ -n "$sha" ] || { echo "$repo	UNREACHABLE	ls-remote returned nothing"; exit 5; }
else
  sha="$ref"
fi

echo "== $repo @ ${sha:0:7}"
found=0
fams=""
for n in $NAMES; do
  body=$(curl -sf --max-time 25 "https://raw.githubusercontent.com/$repo/$sha/$n" 2>/dev/null) || continue
  [ -n "$body" ] || continue
  bytes=$(printf '%s' "$body" | wc -c | tr -d ' ')
  # A file NAMED licence can DECLARE THERE IS NONE -- a real specimen is on this shelf
  # (murderszn/open-tutor).  Size alone is not a grant.
  fam=$(family "$body")
  title=$(printf '%s' "$body" | grep -m1 '[A-Za-z]' | sed 's/^[[:space:]]*//' | cut -c1-72)
  printf '   %-16s %-16s %8s B  | %s\n' "$n" "$fam" "$bytes" "$title"
  found=$((found+1))
  fams="$fams $fam"
done

if [ "$found" -eq 0 ]; then
  echo "   VERDICT: UNGRANTED (0 of $(echo $NAMES | wc -w) filenames)"
  exit 4
fi
uniq_fams=$(printf '%s\n' $fams | sort -u | tr '\n' ' ')
n_uniq=$(printf '%s\n' $fams | sort -u | wc -l | tr -d ' ')
if [ "$n_uniq" -gt 1 ]; then
  echo "   VERDICT: PARTITIONED -- $n_uniq families across $found files: $uniq_fams"
  echo "   >> read SCOPE from the README before building; a scalar answer here is a DEFECT"
  exit 3
fi
echo "   VERDICT: SINGLE -- $uniq_fams ($found file(s))"
exit 0
