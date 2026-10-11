#!/bin/sh
# Which MEASURED grants can the claim-side alternation never emit?
# A measured token that no possible claim can match guarantees WRONG for every
# row on that address, whatever the page says. That is an instrument defect,
# not a KB error -- and p118 counted those rows in its headline.
ALT='AGPL-3.0|AGPL-3|LGPL-|GPL-3.0|GPL-3|GPL-2.0|GPL-2|Apache-2.0|Apache-2|BSD-2|BSD-3|BSD-4|ECL-2.0|ECL-2|MPL-2.0|MPL-2|EPL-1|EPL-2|CC-BY-SA|CC-BY-NC|CC-BY|CC0|Unlicense|MIT|AGPL|LGPL|GPL|BSD'
echo "measured grants present in the tree, and whether a claim could ever match:"
cut -f4 ../p118-licence-column-sweep/measured2.2026-10-11.tsv | sed 's/^MULTI-GRANT://' | tr ',' '\n' | sort -u | while read -r g; do
  [ -z "$g" ] && continue
  case "$g" in UNKNOWN|NO-LICENCE-FILE|EMPTY|GRANT-IN-MANIFEST|GRANT-BY-REFERENCE*) continue;; esac
  if echo "$g" | grep -qE "^($ALT)"; then :; else printf '  UNMATCHABLE  %s\n' "$g"; fi
done
