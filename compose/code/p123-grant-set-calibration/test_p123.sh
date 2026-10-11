#!/usr/bin/env bash
# p123 suite. FULLY OFFLINE: no network, no clock, no GitHub.
# Every classifier fixture is a REAL licence file that broke a real build.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
F="$HERE/fixtures"
PASS=0; FAIL=0
ok()   { PASS=$((PASS+1)); }
bad()  { FAIL=$((FAIL+1)); echo "  FAIL: $1"; echo "        want [$2] got [$3]"; }
eq()   { if [ "$2" = "$3" ]; then ok; else bad "$1" "$2" "$3"; fi; }

cls() { python3 -I "$HERE/classify_licence.py" "${2:-LICENSE}" < "$1"; }

echo "== classifier: carried fixtures must not move (p122 lineage) =="
eq "gpl2 preamble names Lesser"      "GPL-2.0"            "$(cls $F/gpl2-preamble-names-lesser.txt)"
eq "epl2 secondary names gpl2"       "EPL-2.0"            "$(cls $F/epl2-secondary-names-gpl2.txt)"
eq "mit control"                     "MIT"                "$(cls $F/mit-control.txt)"
eq "apache2 control"                 "Apache-2.0"         "$(cls $F/apache2-control.txt)"
eq "agpl3 control"                   "AGPL-3.0"           "$(cls $F/agpl3-control.txt)"
eq "bsd3 control"                    "BSD-3-Clause"       "$(cls $F/bsd3-control.txt)"
eq "lgpl3 headerless"                "LGPL-3.0"           "$(cls $F/lgpl3-headerless.txt)"
eq "cc-by-nc-sa control"             "CC-BY-NC-SA-4.0"    "$(cls $F/cc-by-nc-sa-control.txt)"
eq "elastic control"                 "Elastic-2.0"        "$(cls $F/elastic-control.txt)"
eq "faircode non-OSI stays non-OSI"  "SPLIT:FairCode-NonOSI" "$(cls $F/faircode-sustainable-use.txt)"

echo "== classifier: EUPL by reference (p123, from opetushallitus/koski) =="
# The real file grants "the EUPL, Version 1.1 or ... subsequent versions" and
# reproduces NO body. p122's classifier returned UNKNOWN; this KB recorded it
# as bare "EUPL", losing the version AND the upgrade clause.
eq "koski: EUPL 1.1 + upgrade clause" "EUPL-1.1-or-later" "$(cls $F/eupl11-byref-koski.txt LICENSE.txt)"
# The upgrade clause is HARD-WRAPPED in the real file. A space-literal regex misses it.
eq "upgrade clause survives wrapping" "EUPL-1.1-or-later" \
   "$(printf 'Licensed under the EUPL, Version 1.1 or - as soon as approved - subsequent\nversions of the EUPL (the "Licence");\n' | python3 -I "$HERE/classify_licence.py" LICENSE)"
# ... and the floor version must NOT silently gain "-or-later".
eq "EUPL 1.1 without upgrade clause"  "EUPL-1.1"          "$(cls $F/eupl11-byref-no-upgrade.txt)"

echo "== classifier: a grant stated in a FIELD, not a body (R/CRAN) =="
eq "LICENSE stub defers to DESCRIPTION" "STUB-SEE-DESCRIPTION" "$(cls $F/r-stub-license.txt)"
eq "DESCRIPTION License: field read"    "REF:MIT"              "$(cls $F/r-description.txt DESCRIPTION)"
eq "DESCRIPTION without a grant field"  "NOT-A-GRANT" \
   "$(printf 'Package: x\nTitle: y\n' | python3 -I "$HERE/classify_licence.py" DESCRIPTION)"
eq "empty file is EMPTY, never UNKNOWN" "EMPTY" "$(printf '' | python3 -I "$HERE/classify_licence.py" LICENSE)"

echo "== grant SET semantics (ACTION Z) =="
set_t() { python3 -I -c "
import sys; sys.path.insert(0,'$HERE')
from join_grant_set import grant_tokens
print(','.join(sorted(grant_tokens(eval(sys.argv[1])))))
" "$1"; }
eq "two files, two grants, both kept" "apache-2.0,mit" \
   "$(set_t "[('LICENSE','MIT'),('LICENSE-DOCS','Apache-2.0')]")"
eq "split grant exposes its primary"  "mit,split:mit" \
   "$(set_t "[('LICENSE','SPLIT:MIT')]")"
eq "split-ref keeps BOTH arms"        "cc-by-4.0,mit" \
   "$(set_t "[('LICENSE','SPLIT-REF:MIT+CC-BY-4.0')]")"
eq "REF from DESCRIPTION resolves"    "mit" "$(set_t "[('DESCRIPTION','REF:MIT')]")"
eq "eupl-or-later folds to one key"   "eupl-or-later" "$(set_t "[('LICENSE','EUPL-1.1-or-later')]")"
eq "per-artifact grant: code vs data" "cc-by-nc-sa-4.0,mit" \
   "$(set_t "[('LICENSE-CODE','MIT'),('LICENSE-DADOS','CC-BY-NC-SA-4.0')]")"

echo "== join: the per-artifact prose this KB writes must VERIFY, not fail =="
T="$(mktemp -d)"; trap 'rm -rf "$T"' EXIT
# The exact shape p122 reported as a false positive: page states both arms.
printf 'agents/top.md\t10\tmicrosoft/autogen\tMIT\t5\tMIT (LICENSE-CODE) - LICENSE is CC-BY-4.0 for docs\n' > "$T/c.tsv"
printf 'agents/top.md\t11\tmicrosoft/autogen\tCC BY 4.0\t5\tMIT (LICENSE-CODE) - LICENSE is CC-BY-4.0 for docs\n' >> "$T/c.tsv"
printf 'microsoft/autogen\tmain\tLICENSE-CODE\t1000\tMIT\n' > "$T/g.tsv"
printf 'microsoft/autogen\tmain\tLICENSE\t2000\tCC-BY-4.0\n' >> "$T/g.tsv"
out="$(python3 -I "$HERE/join_grant_set.py" "$T/c.tsv" "$T/g.tsv" 2>&1 >/dev/null)"
eq "both arms of a split claim AGREE" "# AGREES=2" "$(printf '%s' "$out" | grep -c '^# AGREES=2' | sed 's/^1$/# AGREES=2/')"
# A claim the tree grants NOWHERE is still a defect. The set must not excuse it.
printf 'agents/top.md\t20\tfwu-de/ais-chat\tMIT\t5\tMIT, so a closed derivative is permitted\n' > "$T/c2.tsv"
printf 'fwu-de/ais-chat\tmain\tLICENSE\t34523\tAGPL-3.0\n' > "$T/g2.tsv"
eq "a wrong claim is still a DEFECT" "DEFECT" \
   "$(python3 -I "$HERE/join_grant_set.py" "$T/c2.tsv" "$T/g2.tsv" 2>/dev/null | cut -f1)"
# A page naming a licence over a tree with no grant file at all.
printf 'repos/foundations.md\t7\tsome/repo\tMIT\t5\tMIT badges over a 404\n' > "$T/c3.tsv"
printf 'some/repo\tmain\t-\t0\tNO-FILE\n' > "$T/g3.tsv"
eq "no grant file is NO-GRANT"  "NO-GRANT" \
   "$(python3 -I "$HERE/join_grant_set.py" "$T/c3.tsv" "$T/g3.tsv" 2>/dev/null | cut -f1)"
# ACTION V's marker is the correction guard now: exact match, no vocabulary.
printf 'agents/top.md\t30\tx/y\tMIT\t5\t| 🔴 AGPL-3.0 ⚠️ **was MIT**<!--corrected--> |\n' > "$T/c4.tsv"
printf 'x/y\tmain\tLICENSE\t34523\tAGPL-3.0\n' > "$T/g4.tsv"
eq "marked row scores CORRECTED" "CORRECTED" \
   "$(python3 -I "$HERE/join_grant_set.py" "$T/c4.tsv" "$T/g4.tsv" 2>/dev/null | cut -f1)"

echo "== ACTION V back-fill: a row is a ROW, not prose about a row =="
mk() { printf '%s\n' "$1" > "$T/v.md"; python3 -I "$HERE/backfill_marker.py" --apply "$T/v.md" >/dev/null 2>&1; cat "$T/v.md"; }
eq "table row gains the marker" \
   '| [`a/b`](u) | 🟢 **BSD-3-Clause** ⚠️ **was 🟢 MIT**<!--corrected--> | note |' \
   "$(mk '| [`a/b`](u) | 🟢 **BSD-3-Clause** ⚠️ **was 🟢 MIT** | note |')"
eq "PROSE about the marker is left alone" \
   'Its correction tables read *"⚠️ **was LGPL-3.0**"* on two pages.' \
   "$(mk 'Its correction tables read *"⚠️ **was LGPL-3.0**"* on two pages.')"
eq "idempotent: no double marker" \
   '| x ⚠️ **was 🟢 MIT**<!--corrected--> |' \
   "$(mk '| x ⚠️ **was 🟢 MIT**<!--corrected--> |')"
eq "a row with TWO corrections marks both" \
   '| x ⚠️ **was MIT**<!--corrected--> y ⚠️ **was BSD**<!--corrected--> |' \
   "$(mk '| x ⚠️ **was MIT** y ⚠️ **was BSD** |')"
eq "a row with no correction is untouched" \
   '| [`a/b`](u) | 🟢 **MIT** | note |' \
   "$(mk '| [`a/b`](u) | 🟢 **MIT** | note |')"

echo "== ACTION W calibration arithmetic =="
# Gold row: the tree grants MIT in LICENSE-CODE; the page says MIT. A
# one-token census reads LICENSE (CC-BY-4.0) and flags a CORRECT row.
printf 'p\t1\tm/a\tMIT\t5\tctx\n' > "$T/wc.tsv"
printf 'm/a\tmain\tLICENSE\t1\tCC-BY-4.0\nm/a\tmain\tLICENSE-CODE\t1\tMIT\n' > "$T/wg.tsv"
printf 'm/a\tEXISTS\tmain\n' > "$T/wh.tsv"
eq "one-token FP on a split-grant gold row" "ONE-TOKEN false positives	1	100.0 %" \
   "$(python3 -I "$HERE/calibrate.py" "$T/wc.tsv" "$T/wg.tsv" "$T/wh.tsv" 2>/dev/null | sed -n 2p)"
# A repo with ONE plain LICENSE cannot separate the models, so it must be
# EXCLUDED from the denominator rather than padding it.
printf 'm/b\tmain\tLICENSE\t1\tMIT\n' > "$T/wg2.tsv"
printf 'p\t1\tm/b\tMIT\t5\tctx\n' > "$T/wc2.tsv"
printf 'm/b\tEXISTS\tmain\n' > "$T/wh2.tsv"
eq "trivially-agreeing row excluded from gold" "1" \
   "$(python3 -I "$HERE/calibrate.py" "$T/wc2.tsv" "$T/wg2.tsv" "$T/wh2.tsv" >/dev/null 2>&1; echo $?)"
# MAIN-ONLY: a gold row on a repo whose default branch is neither main nor master.
printf 'm/c\tEXISTS\tdevelop\n' > "$T/wh3.tsv"
printf 'm/c\tdevelop\tLICENSE\t1\tCC-BY-4.0\nm/c\tdevelop\tLICENSE-CODE\t1\tMIT\n' > "$T/wg3.tsv"
printf 'p\t1\tm/c\tMIT\t5\tctx\n' > "$T/wc3.tsv"
eq "main-only FP on a develop-default repo" "MAIN-ONLY false positives	1	100.0 %" \
   "$(python3 -I "$HERE/calibrate.py" "$T/wc3.tsv" "$T/wg3.tsv" "$T/wh3.tsv" 2>/dev/null | sed -n 3p)"

echo
echo "$PASS passed / $FAIL failed"
[ "$FAIL" -eq 0 ]
