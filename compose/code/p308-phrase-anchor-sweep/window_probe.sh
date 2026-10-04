#!/bin/sh
# window_probe.sh -- where does each decisive anchor SIT, in BYTES, inside a real payload?
#
# This exists because the pase 100 suite's NEGATIVE control failed, and the failure was real:
# the AGPL-3.0 anchor that P288 installed is NORMALIZED, so a newline cannot split it -- and
# it was lost anyway.  The reason is not the phrase, it is the WINDOW.  `osi_family_of` bounds
# the title block with `head -40`, which counts LINES, and re-wrapping a payload narrower
# pushes the same TEXT past line 40.  A line count is not a property of the document; it is a
# property of where its newlines happen to be.
#
# So the replacement bound has to be measured, not guessed.  It must sit AFTER the AGPL's
# section-0 definition (the P288 anchor) and BEFORE section 13 of the GPL-3.0 (the P171 trap,
# titled "Use with the GNU Affero General Public License").  This prints both offsets for the
# real payloads in this base, so the window can be chosen from numbers.
#
# Invocation:  sh window_probe.sh
cd "$(dirname "$0")"

# off <file> <pattern> -> byte offset of the first match in the WHITESPACE-NORMALIZED payload,
# or "-" when absent.  Normalized, because that is the view the repaired classifier reads.
off() {
  tr -s '[:space:]' ' ' < "$1" \
    | grep -oib -m1 -- "$2" 2>/dev/null | head -1 | cut -d: -f1
}
show() {
  printf '%-46s %9s  %s\n' "$2" "${3:--}" "$1"
}
printf '%-46s %9s  %s\n' 'ANCHOR' 'BYTE-OFF' 'PAYLOAD'
printf '%s\n' '---------------------------------------------------------------------------------'
for f in ../p288-agpl-casefold/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE \
         ../p184-holder-mismatch/fixtures/gpl-3.0-moodle-COPYING.txt \
         ../p255-holder-shared-control/fixtures/gpl-2.0-openemis-core-LICENSE.txt \
         ../p184-holder-mismatch/fixtures/apache-2.0-deeptutor.txt; do
  [ -f "$f" ] || continue
  b=$(wc -c < "$f" | tr -d ' ')
  printf '\n%s   (%s B)\n' "$(basename "$f")" "$b"
  show "$f" 'refers to version 3 of the GNU Affero General Public License' "$(off "$f" 'refers to version 3 of the GNU Affero General Public License')"
  show "$f" 'GNU AFFERO GENERAL PUBLIC LICENSE (title)' "$(off "$f" 'GNU AFFERO GENERAL PUBLIC LICENSE')"
  show "$f" 'GNU GENERAL PUBLIC LICENSE' "$(off "$f" 'GNU GENERAL PUBLIC LICENSE')"
  show "$f" 'Version 3' "$(off "$f" 'Version 3')"
  show "$f" 'Apache License' "$(off "$f" 'Apache License')"
  show "$f" 'FIRST mention of Affero anywhere' "$(off "$f" 'Affero')"
  show "$f" 'sec.13 trap: Use with the GNU Affero' "$(off "$f" 'Use with the GNU Affero')"
done
