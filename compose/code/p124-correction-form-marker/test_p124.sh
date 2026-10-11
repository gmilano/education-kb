#!/usr/bin/env bash
# p124 suite. FULLY OFFLINE: no network, no clock, no GitHub.
#
# Every licence fixture is a REAL file from a REAL repository, and all but the
# carried p122/p123 lineage are files that broke a p124 build. The markdown
# fixtures are real constructions copied off this KB's own live pages.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
F="$HERE/fixtures"
PASS=0; FAIL=0
ok()   { PASS=$((PASS+1)); }
bad()  { FAIL=$((FAIL+1)); echo "  FAIL: $1"; echo "        want [$2] got [$3]"; }
eq()   { if [ "$2" = "$3" ]; then ok; else bad "$1" "$2" "$3"; fi; }

cls()   { python3 -I "$HERE/classify_licence.py" "${2:-LICENSE}" < "$1"; }
shape() { python3 -I "$HERE/split_shape.py" < "$1" 2>/dev/null; }
ccv()   { python3 -I "$HERE/cc_version.py" < "$1"; }

echo "== carried lineage: p122/p123 classifier fixtures must not move =="
eq "gpl2 preamble names Lesser"      "GPL-2.0"            "$(cls $F/gpl2-preamble-names-lesser.txt)"
eq "epl2 secondary names gpl2"       "EPL-2.0"            "$(cls $F/epl2-secondary-names-gpl2.txt)"
eq "mit control"                     "MIT"                "$(cls $F/mit-control.txt)"
eq "apache2 control"                 "Apache-2.0"         "$(cls $F/apache2-control.txt)"
eq "agpl3 control"                   "AGPL-3.0"           "$(cls $F/agpl3-control.txt)"
eq "bsd3 control"                    "BSD-3-Clause"       "$(cls $F/bsd3-control.txt)"
eq "lgpl3 headerless"                "LGPL-3.0"           "$(cls $F/lgpl3-headerless.txt)"
eq "cc-by-nc-sa control"             "CC-BY-NC-SA-4.0"    "$(cls $F/cc-by-nc-sa-control.txt)"
eq "elastic control"                 "Elastic-2.0"        "$(cls $F/elastic-control.txt)"
eq "faircode stays non-OSI"          "SPLIT:FairCode-NonOSI" "$(cls $F/faircode-sustainable-use.txt)"
eq "koski EUPL 1.1 + upgrade"        "EUPL-1.1-or-later"  "$(cls $F/eupl11-byref-koski.txt LICENSE.txt)"
eq "EUPL 1.1 без upgrade clause"     "EUPL-1.1"           "$(cls $F/eupl11-byref-no-upgrade.txt)"
eq "R LICENSE stub"                  "STUB-SEE-DESCRIPTION" "$(cls $F/r-stub-license.txt)"
eq "R DESCRIPTION field"             "REF:MIT"            "$(cls $F/r-description.txt DESCRIPTION)"

echo "== ACTION AA: a split grant detected by SHAPE, not by phrasing =="
# Elgg: "Bundled plugins (the contents of the \"/mod\" directory) are available
# only under the GPLv2 license. The remainder of the project is available under
# either MIT or GPLv2." No SPLIT_MARKER matches it; p123 returned bare MIT.
eq "elgg: p123 reduced it to MIT"    "MIT"                "$(cls $F/elgg-split-shape.txt LICENSE.txt)"
eq "elgg: shape finds the split"     "SHAPE-SPLIT:GPL-2.0+MIT" "$(shape $F/elgg-split-shape.txt)"
# understory: code MIT, lesson content CC BY-NC-SA 4.0. In an education KB the
# content IS the deliverable, so losing this arm inverts the commercial answer.
eq "understory: p123 said MIT"       "MIT"                "$(cls $F/understory-code-content-split.txt)"
eq "understory: shape finds content" "SHAPE-SPLIT:CC-BY-NC+CC-BY-NC-SA+MIT" \
                                     "$(shape $F/understory-code-content-split.txt)"
# masakhane-NER: Apache-2.0 code (from HuggingFace transformers) + the NER
# DATA under CC BY-NC 4.0.
eq "masakhane: p123 said Apache-2.0" "Apache-2.0"         "$(cls $F/masakhane-code-data-split.txt)"
eq "masakhane: shape finds NC data"  "SHAPE-SPLIT:Apache-2.0+CC-BY-NC" \
                                     "$(shape $F/masakhane-code-data-split.txt)"
# anki: AGPL-3 core with named per-file exceptions.
eq "anki: shape finds the split"     "SHAPE-SPLIT:AGPL-3.0+CC-BY-SA" "$(shape $F/anki-perfile-split.txt)"

echo "== ACTION AA negatives: naming two licences is NOT a split =="
eq "gpl2 preamble: not a split"      "NO-SHAPE-SPLIT"     "$(shape $F/gpl2-preamble-names-lesser.txt)"
eq "epl2 secondary: not a split"     "NO-SHAPE-SPLIT"     "$(shape $F/epl2-secondary-names-gpl2.txt)"
eq "mit control: not a split"        "NO-SHAPE-SPLIT"     "$(shape $F/mit-control.txt)"
eq "apache2: not a split"            "NO-SHAPE-SPLIT"     "$(shape $F/apache2-control.txt)"
eq "agpl3: not a split"              "NO-SHAPE-SPLIT"     "$(shape $F/agpl3-control.txt)"
eq "bsd3: not a split"               "NO-SHAPE-SPLIT"     "$(shape $F/bsd3-control.txt)"
eq "lgpl3: not a split"              "NO-SHAPE-SPLIT"     "$(shape $F/lgpl3-headerless.txt)"
eq "cc-by-nc-sa: not a split"        "NO-SHAPE-SPLIT"     "$(shape $F/cc-by-nc-sa-control.txt)"
eq "elastic: not a split"            "NO-SHAPE-SPLIT"     "$(shape $F/elastic-control.txt)"
# 🔴 The regression that cost p124 two false findings: `\bCC[ -]?BY\b` matches
# INSIDE `CC BY-SA 4.0` because the hyphen is a word boundary, so a plain
# CC-BY-SA file looked like it named two licences.
eq "CC-BY-SA is ONE licence"         "NO-SHAPE-SPLIT"     "$(shape $F/ccbysa4-not-a-split.txt)"

echo "== ACTION AD: the CC family resolved to a VERSION =="
# 🔴 The defect this channel order exists to prevent: the CC 4.0 legalcode
# recommends the CC0 Public Domain Dedication in its own boilerplate, so a
# whole-text scan reads EVERY CC-BY-4.0 file as CC0.
eq "autogen docs are CC-BY-4.0"      "CC-BY-4.0"          "$(ccv $F/ccby4-legalcode-names-cc0.txt)"
eq "openstax physics is NC"          "CC-BY-NC-SA-4.0"    "$(ccv $F/ccbyncsa4-openstax-title.txt)"
eq "CC0 title on the SECOND line"    "CC0-1.0"            "$(ccv $F/cc0-title-on-second-line.txt)"
eq "a UTF-8 BOM must not hide it"    "CC-BY-4.0"          "$(ccv $F/ccby4-with-bom.txt)"
eq "CC-BY-SA resolved, not BY"       "CC-BY-SA-4.0"       "$(ccv $F/ccbysa4-not-a-split.txt)"
eq "cc-by-nc-sa control"             "CC-BY-NC-SA-4.0"    "$(ccv $F/cc-by-nc-sa-control.txt)"
eq "MIT is not CC"                   "NOT-CC"             "$(ccv $F/mit-control.txt)"
eq "Apache-2.0 is not CC"            "NOT-CC"             "$(ccv $F/apache2-control.txt)"
eq "GPL-2.0 is not CC"               "NOT-CC"             "$(ccv $F/gpl2-preamble-names-lesser.txt)"

echo "== ACTION AB: the three correction forms, and what is NOT one =="
# Count hits from the TOTAL line on stderr only -- the per-file summary on
# stdout also contains the string "FORM-", which made the first build of this
# helper count summaries instead of findings.
cf() { python3 -I "$HERE/correction_form.py" "$1" 2>&1 >/dev/null \
       | sed -n 's/^# TOTAL //p' | tr ' ' '\n' \
       | awk -F= '/^FORM/{s+=$2} END{print s+0}'; }
# 🔴 "token that WAS invisible" -- `was` as a relative pronoun in a header.
# The column holds a LIVE claim; marking it would hide a real licence.
eq "relative-pronoun was: no hit"    "0"                  "$(cf $F/md-relative-pronoun-was.md)"
# 🔴 Two passes measuring independently, scored by an `agrees` column.
eq "two-pass cross-check: no hit"    "0"                  "$(cf $F/md-crosscheck-two-passes.md)"
# 🔴 `GPL-3` and `GPL-3.0` are the same grant; the row's own cell says AGREE.
eq "GPL-3 vs GPL-3.0: 1 hit only"    "1"                  "$(cf $F/md-spelling-agrees.md)"
# 🟢 Two OLD columns and one NEW is still a correction table.
eq "two old columns: 1 hit"          "1"                  "$(cf $F/md-two-old-columns.md)"
# 🟢 `actually`, which an `\bactual\b` header regex misses.
eq "actually-header: 1 hit"          "1"                  "$(cf $F/md-actually-header.md)"
# 🟢 1 prose retraction; the QUOTED one and the DESCRIPTIVE one are not records.
eq "prose: 1 of 3 is a retraction"   "1"                  "$(cf $F/md-prose-forms.md)"

echo "== ACTION AC: a repair is a SEARCH, and the region must be NARROW =="
rs() { python3 -I "$HERE/repair_search.py" "$1" 2>/dev/null | head -1; }
rsv() { python3 -I "$HERE/repair_search.py" "$1" 2>/dev/null | grep -c VIOLATION || true; }
# 🔴 A FORM-1 cell holds the OLD and the NEW value together. Treating the whole
# cell as marked harvests `Apache-2.0` -- the repaired, correct value -- as an
# old token, and then every correct row in the KB reads as a violation.
eq "form1 cell: 1 pair, not 2"       "# repaired pairs=1 over 1 addresses" \
                                     "$(rs $F/md-form1-both-tokens.md)"
eq "form1 cell: no self-violation"   "0"                  "$(rsv $F/md-form1-both-tokens.md)"

echo "== ACTION AE: the branch divergence the gold set must contain =="
# 🔴 Learnosity/learnosity-qti serves MIT on `master` and GPL-2.0 on `develop`,
# which IS its default branch. A branch-guessing probe returns the PERMISSIVE
# answer for a copyleft repository -- the exact error a studio cannot afford.
eq "learnosity develop = GPL-2.0"    "GPL-2.0"            "$(cls $F/learnosity-develop-gpl2.txt)"
eq "learnosity master  = MIT"        "MIT"                "$(cls $F/learnosity-master-mit.txt)"

echo
echo "== $PASS passed / $FAIL failed =="
[ "$FAIL" -eq 0 ] || exit 1
