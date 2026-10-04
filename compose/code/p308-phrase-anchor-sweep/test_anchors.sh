#!/bin/sh
# test_anchors.sh -- the pase 99 pre-registered action, run, and the repair it forced.
#
# AFFIRMATION TO REFUTE (pre-registered in agents/top.md, pase 99):
#   "P304's defect is not the BSD branch alone: there are more anchors written as a CONTIGUOUS
#    PHRASE in lib/license_family.sh, and each one loses its variants with insertion."
# PREDICTION, with the unit named: a sweep of the phrase anchors against REAL payloads with
# insertion finds >=1 MORE family misclassified.  Candidates named: MIT, Unlicense, MPL-2.0.
# "If all three hold, P304 was specific to BSD and that section was wrong."
#
# VERDICT: CONFIRMED on the Unlicense -- and the consequence is WORSE than P304's, because it
# INVERTS the commercial verdict instead of merely losing a shelf.  Of the three candidates
# named, one fails (Unlicense), one is fragile but SHADOWED (MIT), one is form-safe (MPL-2.0,
# not measured for want of a payload).  And the suite's own NEGATIVE control then failed on an
# anchor that is NOT a phrase at all -- the AGPL section-0 definition from P288 -- which found
# the same defect on a second axis: the title-block WINDOW is counted in LINES.
#
# Invocation:  sh test_anchors.sh
#
# Payloads are REAL, fetched first-hand from raw.githubusercontent.com (the only 200 channel
# this pase measured: github.com and api.github.com are 403), and committed under fixtures/
# so the suite reproduces when the channel does not.
set -e
cd "$(dirname "$0")"
. ../lib/license_family.sh

PASS=0; FAIL=0
ok() { PASS=$((PASS+1)); printf '  ok   %s\n' "$1"; }
no() { FAIL=$((FAIL+1)); printf '  FAIL %s\n    expected: %s\n    actual:   %s\n' "$1" "$2" "$3"; }
is() { if [ "$2" = "$3" ]; then ok "$1"; else no "$1" "$2" "$3"; fi; }

UNL=fixtures/unlicense-FWU-DE-mem-mcp.LICENSE
MIT=fixtures/mit-adlnet-xapi-lab.LICENSE
AGPL=../p288-agpl-casefold/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE
GPL2=../p255-holder-shared-control/fixtures/gpl-2.0-openemis-core-LICENSE.txt
GPL3=../p184-holder-mismatch/fixtures/gpl-3.0-moodle-COPYING.txt
APACHE=../p184-holder-mismatch/fixtures/apache-2.0-deeptutor.txt
DECL=../p255-holder-shared-control/fixtures/declaration-19B-frappe-education-license.txt

echo "== 1. Baseline: every real payload classifies correctly AS SHIPPED =="
is 'FWU-DE/mem-mcp     (1.211 B)  -> Unlicense'  'Unlicense'  "$(family_of "$(cat $UNL)")"
is 'adlnet/xapi-lab    (1.082 B)  -> MIT'        'MIT'        "$(family_of "$(cat $MIT)")"
is 'kuali/kfs         (33.755 B)  -> AGPL-3.0'   'AGPL-3.0'   "$(family_of "$(cat $AGPL)")"
is 'OpenEMIS/core     (15.518 B)  -> GPL-2.0'    'GPL-2.0'    "$(family_of "$(cat $GPL2)")"
is 'moodle/moodle     (35.147 B)  -> GPL-3.0'    'GPL-3.0'    "$(family_of "$(cat $GPL3)")"
is 'HKUDS/DeepTutor   (11.408 B)  -> Apache-2.0' 'Apache-2.0' "$(family_of "$(cat $APACHE)")"
is 'frappe/education      (19 B)  -> declaration' 'GPL-3.0 (declaracion)' "$(family_of "$(cat $DECL)")"

echo
echo "== 2. THE DEFECT, reproduced against a PRE-P308 REPLICA of the two broken rules =="
# P126 pt.2, which this base has paid for twice: a control whose assertions pass without ever
# exercising the case that breaks it is not a control.  So the two pre-fix rules are
# re-implemented inline here and shown to FAIL on the same real payloads the repaired
# classifier now gets right.  Without this block, section 3 would pass vacuously.
pre_unlicense() { printf '%s' "$1" | grep -qi 'free and unencumbered software released into the public domain'; }
pre_titleblock() { printf '%s' "$1" | head -40 | tr -s '[:space:]' ' '; }

is 'pre-fix Unlicense anchor, payload as shipped: MATCHES' 'matches' \
   "$(pre_unlicense "$(cat $UNL)" && echo matches || echo FAILS)"
is 'pre-fix Unlicense anchor at fill-column 70: FAILS'     'FAILS' \
   "$(pre_unlicense "$(./reflow.sh 70 < $UNL)" && echo matches || echo FAILS)"
# Why 70 is the hinge, and it is not a round number chosen to make a point: the canonical
# first line is exactly 71 columns -- "This is free and unencumbered software released into
# the public domain." -- and the anchor occupies columns 9..70 of it.  Wrap at >=71 and the
# line is untouched; wrap at 70 and the break lands between "public" and "domain", INSIDE the
# anchor.  Emacs `fill-column` defaults to 70.
is 'pre-fix Unlicense anchor at 71: still matches (anchor ends at col 70)' 'matches' \
   "$(pre_unlicense "$(./reflow.sh 71 < $UNL)" && echo matches || echo FAILS)"
is 'pre-fix LINE window loses the AGPL section-0 anchor at 70' 'LOST' \
   "$(pre_titleblock "$(./reflow.sh 70 < $AGPL)" | grep -qi 'refers to version 3 of the GNU Affero' && echo present || echo LOST)"
is 'pre-fix LINE window keeps it on the payload as shipped'    'present' \
   "$(pre_titleblock "$(cat $AGPL)" | grep -qi 'refers to version 3 of the GNU Affero' && echo present || echo LOST)"
is 'repaired BYTE window keeps it at 70'  'present' \
   "$(./reflow.sh 70 < $AGPL | tr -s '[:space:]' ' ' | head -c 4000 | grep -qi 'refers to version 3 of the GNU Affero' && echo present || echo LOST)"

echo
echo "== 3. The REPAIR: every family is reflow-INVARIANT, at every width =="
inv() { # inv <label> <file> <expected>
  _l="$1"; _f="$2"; _e="$3"
  for w in 72 71 70 68 64 60 50 40 30 20; do
    is "$_l w=$w" "$_e" "$(family_of "$(./reflow.sh $w < $_f)")"
  done
}
inv 'Unlicense  FWU-DE/mem-mcp' "$UNL"    'Unlicense'
inv 'MIT        adlnet/xapi-lab' "$MIT"   'MIT'
inv 'AGPL-3.0   kuali/kfs'      "$AGPL"   'AGPL-3.0'
inv 'GPL-2.0    OpenEMIS/core'  "$GPL2"   'GPL-2.0'
inv 'GPL-3.0    moodle/moodle'  "$GPL3"   'GPL-3.0'
inv 'Apache-2.0 HKUDS/DeepTutor' "$APACHE" 'Apache-2.0'

echo
echo "== 4. And the commercial verdict, which is the one that reaches a deliverable =="
# THE THREE LAYERS, each sound on its own.  (a) the fragile anchor loses the family;
# (b) P250's gate is conditioned on "family identified", so losing it OPENS the gate;
# (c) the body token-match the gate exists to suppress then runs -- and the Unlicense grants
#     permission with the words "for any purpose, commercial or NON-COMMERCIAL", so the most
#     permissive text there is gets flagged by the very word it uses to GRANT.
# The lib's own P250 comment names (c) as the unsoundness the gate was written to prevent.
# It was prevented -- and the gate's precondition turned out to be reflow-dependent.
is 'the granting phrase really is in the payload'   'present' \
   "$(tr -s '[:space:]' ' ' < $UNL | grep -qi 'commercial or non-commercial' && echo present || echo absent)"
for w in 72 70 64 40 20; do
  is "Unlicense commercial use at w=$w -> ALLOWED" 'ALLOWED' \
     "$(commercial_use_ok "$(./reflow.sh $w < $UNL)" && echo ALLOWED || echo PROHIBITED)"
done
is 'holder_of stays NOT-APPLICABLE for the Unlicense at w=40' 'yes' \
   "$(case "$(holder_of "$(./reflow.sh 40 < $UNL)")" in NOT-APPLICABLE*) echo yes;; *) echo "no";; esac)"
# P309, RESIDUAL AND DECLARED, not papered over.  The byte window made the holder LINE
# reachable again at any wrap -- but `holder_of` returns A LINE, and a line is reflow-dependent
# BY CONSTRUCTION: once the wrap is narrower than the holder line itself, the NAME is cut.
# Measured: "Copyright (c) 2015 Tyler Mulligan" is 33 columns, so it survives at w>=33 and
# comes back as "Copyright (c) 2015 Tyler" at w=30.  The fix is NOT to drop the `^Copyright`
# line anchor -- that anchor is what P255 installed to stop body prose being reported as a
# holder (gibbonedu/core returned a sentence out of section 8).  It needs a span read off the
# normalized text, which is a bigger change than this pase should make on its own, so it is
# pre-registered instead.  At every realistic fill-column the holder is intact.
is 'holder_of finds the MIT holder intact at w=40' 'Copyright (c) 2015 Tyler Mulligan' \
   "$(holder_of "$(./reflow.sh 40 < $MIT)")"
is 'holder_of finds it intact at w=33, the width of the line itself' 'Copyright (c) 2015 Tyler Mulligan' \
   "$(holder_of "$(./reflow.sh 33 < $MIT)")"
# Asserted on the SEMANTICS (the surname is gone), not on the exact string: `fold -s` keeps
# the space it broke on, so the literal is "Copyright (c) 2015 Tyler " with a trailing blank,
# and pinning that would be a test of fold's padding instead of a test of the defect.
is 'P309 residual: at w=30 the surname is CUT from the holder' 'TRUNCATED' \
   "$(holder_of "$(./reflow.sh 30 < $MIT)" | grep -q 'Mulligan' && echo intact || echo TRUNCATED)"
is 'P309 residual: and what survives is still the holder line, not prose' 'yes' \
   "$(holder_of "$(./reflow.sh 30 < $MIT)" | grep -q '^Copyright (c) 2015 Tyler' && echo yes || echo no)"

echo
echo "== 5. MIT was fragile too, but SHADOWED -- and the shadow is what saved it =="
# The MIT anchor is 43 columns wide, so it needs a wrap NARROWER THAN 43 to split -- rarer
# than the Unlicense's 70, and the reason this one never surfaced.  Measured, not assumed:
is 'pre-fix MIT anchor at w=70: still matches (43 < 70)' 'matches' \
   "$(printf '%s' "$(./reflow.sh 70 < $MIT)" | grep -qi 'Permission is hereby granted, free of charge' && echo matches || echo FAILS)"
is 'pre-fix MIT anchor at w=40: FAILS (43 > 40)'         'FAILS' \
   "$(printf '%s' "$(./reflow.sh 40 < $MIT)" | grep -qi 'Permission is hereby granted, free of charge' && echo matches || echo FAILS)"
# And the control that proves the SHADOW did the work rather than the anchor: strip the title
# line -- the titleless-MIT shape, a payload that opens straight on "Copyright (c) ..." -- and
# the fragile anchor is the only route to the family that is left.
TL=$(tail -n +2 $MIT)
is 'control: titleless MIT, unwrapped -> MIT' 'MIT' "$(family_of "$TL")"
is 'control: titleless MIT at w=40, REPAIRED -> MIT' 'MIT' "$(family_of "$(printf '%s' "$TL" | ./reflow.sh 40)")"
is 'control: titleless MIT at w=40 would have been LOST pre-fix' 'FAILS' \
   "$(printf '%s' "$TL" | ./reflow.sh 40 | grep -qi 'Permission is hereby granted, free of charge' && echo matches || echo FAILS)"

echo
echo "== 5b. The titleless-MIT population is NOT hypothetical: a specimen from THIS pase =="
# The pase-100 rotated axis returned `Priyamakeshwari/TeachGPT`, whose LICENSE.md (1.057 B)
# opens straight on "Copyright (c) 2023 Priyadharshini" with NO title line.  So the shape that
# section 5 had to CONSTRUCT by stripping a line exists in the field, and for it the fragile
# body anchor was the only route to the MIT family in the whole classifier.  Without this
# specimen the MIT half of P308 would rest on a payload this base edited itself.
TG=fixtures/mit-TITLELESS-Priyamakeshwari-TeachGPT.LICENSE-md.txt
is 'TeachGPT has NO title-block route to MIT' 'none' \
   "$(head -40 $TG | tr -s '[:space:]' ' ' | grep -qi 'MIT License' && echo shadowed || echo none)"
is 'TeachGPT classifies MIT as shipped'       'MIT' "$(family_of "$(cat $TG)")"
is 'TeachGPT at w=40, REPAIRED -> MIT'        'MIT' "$(family_of "$(./reflow.sh 40 < $TG)")"
is 'TeachGPT at w=40 would have been LOST pre-fix' 'FAILS' \
   "$(./reflow.sh 40 < $TG | grep -qi 'Permission is hereby granted, free of charge' && echo matches || echo FAILS)"
is 'mikhailvs/loqui (MIT, titled) invariant at w=30' 'MIT' \
   "$(family_of "$(./reflow.sh 30 < fixtures/mit-mikhailvs-loqui.LICENSE)")"

echo
echo "== 6. The declaration branch, whose tokens are single words =="
is 'frappe/education 19 B at w=12 invariant' 'GPL-3.0 (declaracion)' \
   "$(family_of "$(printf '%s' "$(cat $DECL)" | ./reflow.sh 12)")"

echo
echo "== 7. MPL-2.0, the third named candidate: NOT MEASURED, and why =="
# Declared instead of filled.  This base's education inventory holds no MPL-2.0 payload, so
# there is nothing to fetch and measure first-hand, and P286 forbids a verdict drawn from a
# specimen that does not exist.  What CAN be stated is a FORM fact, read off the code and
# asserted by the audit: the MPL anchor reads $t, which is normalized, so it was never in the
# fragile class.  That is a claim about the ANCHOR, not about any payload.
is 'MPL anchor audited as TITLE-NORMALIZED, before and after' '1' \
   "$(sh anchor_form.sh | awk -F'\t' '$1=="Mozilla Public License" && $5=="TITLE-NORMALIZED" && $6=="TITLE-NORMALIZED"' | wc -l | tr -d ' ')"

echo
echo "== 8. The count the pre-registration asked for, in its own unit =="
A=$(sh anchor_form.sh | tail -n +2 | awk -F'\t' '$4!=0' | wc -l | tr -d ' ')
FRAG=$(sh anchor_form.sh | awk -F'\t' '$5=="RAW-PHRASE-FRAGILE"' | wc -l | tr -d ' ')
UNSH=$(sh anchor_form.sh | awk -F'\t' '$5=="RAW-PHRASE-FRAGILE" && $7=="NONE"' | wc -l | tr -d ' ')
NOWFRAG=$(sh anchor_form.sh | awk -F'\t' '$6 ~ /FRAGILE/' | wc -l | tr -d ' ')
is 'licence anchors audited'                         '18' "$A"
is 'reflow-fragile BEFORE P308 (P304 predicted >=1)'  '3' "$FRAG"
is 'fragile AND unshadowed -> family LOST outright'   '1' "$UNSH"
is 'reflow-fragile AFTER P308'                        '0' "$NOWFRAG"

echo
printf -- '----\n'
printf 'PASS %s   FAIL %s\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ] || exit 1
