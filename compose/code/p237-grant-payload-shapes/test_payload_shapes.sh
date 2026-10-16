#!/bin/bash
# p237 — three grant payloads whose SHAPE, not whose text, is the hazard.
#
# Every row this pass shelved was grant-read first-hand. Three of those payloads carry a
# defect in the FRAME rather than the licence:
#
#   1. a UTF-8 BOM (ef bb bf) before "Apache License"     — Lu-Yu-Zhen/KongMeng-Agent
#   2. an MIT text with NO copyright line at all          — telekom/ki-in-schulen
#   3. an MIT text whose copyright line carries NO YEAR   — schild-report/schild.report
#
# (1) is the one that could have cost a verdict: a classifier anchored on a PREFIX
# (`body.startswith("Apache License")`, `head -1`) sees three invisible bytes first and falls
# through. `osi_family_of` is anchored on a SUBSTRING and is therefore BOM-safe — but that was
# luck until this file asserted it, and p237 ran it before publishing the row rather than
# assuming it.
#
# (2) and (3) are NOT misgrants. They are holder-field defects, and they matter because these
# shelves publish a holder in every grant cell. p235 already found that `GPL-2.0` has no
# holder field to read; these two show the field can be absent or year-less inside a licence
# that DOES have one. A cell reading "holder *unknown*" is correct; one that invents a holder
# from the org handle is not.
set -u
cd "$(dirname "$0")" || exit 2
source ../lib/license_family.sh

fails=0
check() { # name expected actual
  if [ "$2" != "$3" ]; then echo "FAIL  $1: expected '$2', got '$3'"; fails=$((fails+1)); fi
}

# ── 1. the BOM must not defeat the family classifier ─────────────────────────────────────
bom="fixtures/KongMeng-Agent.BOM-apache-2.0.LICENSE"
check "BOM fixture really starts with ef bb bf" "efbbbf" \
      "$(head -c 3 "$bom" | od -An -tx1 | tr -d ' \n')"
check "BOM Apache-2.0 classifies" "Apache-2.0" "$(osi_family_of "$(cat "$bom")")"

# the negative control for the same property: strip the BOM and the verdict must not move
check "same payload without the BOM" "Apache-2.0" \
      "$(osi_family_of "$(tail -c +4 "$bom")")"

# and the prefix anchor a naive reader would have used is DEMONSTRABLY broken on it, which is
# why this fixture is kept rather than described
first="$(head -1 "$bom")"
case "$first" in
  "Apache License"*) echo "FAIL  the BOM fixture no longer demonstrates the prefix hazard"; fails=$((fails+1));;
esac

# ── 2. a holderless MIT is still MIT ────────────────────────────────────────────────────
nh="fixtures/telekom-ki-in-schulen.HOLDERLESS-mit.LICENSE"
check "holderless MIT classifies" "MIT" "$(osi_family_of "$(cat "$nh")")"
if grep -qiE 'copyright *\(c\)' "$nh"; then
  echo "FAIL  the holderless fixture has acquired a copyright line"; fails=$((fails+1))
fi

# ── 3. a year-less MIT is still MIT, and its holder is readable but undated ──────────────
ny="fixtures/schild.report.NO-YEAR-mit.LICENSE"
check "year-less MIT classifies" "MIT" "$(osi_family_of "$(cat "$ny")")"
check "its holder line has no 4-digit year" "" \
      "$(grep -ioE 'copyright \(c\) [0-9]{4}' "$ny")"
if ! grep -qi 'copyright (c) hmt' "$ny"; then
  echo "FAIL  the year-less fixture's holder is no longer readable"; fails=$((fails+1))
fi

total=9
if [ "$fails" -eq 0 ]; then echo "$total/$total PASS"; else echo "$fails FAILURES"; exit 1; fi
