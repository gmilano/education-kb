#!/usr/bin/env bash
# p120 test suite. Fully OFFLINE: every assertion runs against licence files
# captured in evidence/ and evidence2/ this pass, so the suite is deterministic
# and re-runnable after raw.githubusercontent.com closes.
#
# Four things are tested, in increasing order of what they would catch:
#   A. classify3.sh names each captured grant correctly        (the measurement)
#   B. the F4 branch does not fire on a real permissive file   (the false-positive guard)
#   C. the resolution tiers are assigned as documented         (the method)
#   D. p119's four ACTION F answers are REPRODUCED from scratch (the control)
set -u
cd "$(dirname "$0")"
pass=0; fail=0
ok()   { pass=$((pass+1)); printf '  \033[32mok\033[0m   %s\n' "$1"; }
no()   { fail=$((fail+1)); printf '  \033[31mFAIL\033[0m %s\n     want: %s\n     got:  %s\n' "$1" "$2" "$3"; }
eq()   { if [ "$2" = "$3" ]; then ok "$1"; else no "$1" "$2" "$3"; fi; }
has()  { case "$3" in *"$2"*) ok "$1" ;; *) no "$1" "contains $2" "$3" ;; esac; }
hasnt(){ case "$3" in *"$2"*) no "$1" "NOT contains $2" "$3" ;; *) ok "$1" ;; esac; }
cls()  { ./classify3.sh "$1" 2>/dev/null; }
E=evidence; E2=evidence2

echo "A. classify3.sh on the grants captured this pass"
eq "ais-chat LICENSE is AGPL-3.0"              "AGPL-3.0"   "$(cls $E/FWU-DE_ais-chat__LICENSE)"
eq "Ed-Fi-Data-Standard LICENSE is Apache-2.0" "Apache-2.0" "$(cls $E/Ed-Fi-Alliance-OSS_Ed-Fi-Data-Standard__LICENSE)"
eq "openSIS docs/License.txt is GPL-2.0"       "GPL-2.0"    "$(cls $E2/OS4ED_openSIS-Classic__docs_License.txt)"
eq "ggcheck LICENSE.md is MIT"                 "MIT"        "$(cls $E/rstudio_ggcheck__LICENSE.md)"
eq "tblcheck LICENSE.md is MIT"                "MIT"        "$(cls $E/rstudio_tblcheck__LICENSE.md)"
eq "tna LICENSE.md is MIT"                     "MIT"        "$(cls $E/sonsoleslp_tna__LICENSE.md)"
eq "educabR LICENSE.md is MIT"                 "MIT"        "$(cls $E/SidneyBissoli_educabR__LICENSE.md)"
eq "ottr LICENSE.md is BSD"                    "BSD"        "$(cls $E/ucbds-infra_ottr__LICENSE.md)"
eq "bncc-benchmark code half is MIT"           "MIT"        "$(cls $E/bncc-dev_bncc-benchmark__LICENSE-CODIGO.md)"
has "bncc-benchmark data half is CC-BY"        "CC-BY"      "$(cls $E/bncc-dev_bncc-benchmark__LICENSE-DADOS.md)"

echo "   the R manifest-pointer stubs are still reported as pointers, not resolved"
for r in rstudio_ggcheck rstudio_tblcheck sonsoleslp_tna SidneyBissoli_educabR ucbds-infra_ottr; do
  eq "$r root LICENSE is a manifest pointer" "GRANT-IN-MANIFEST" "$(cls $E/${r}__LICENSE)"
done

echo
echo "B. F4 fires on unnamed proprietary grants and NOT on permissive ones"
has "cloud-learning-ce is proprietary"  "PROPRIETARY-UNNAMED-NOT-OSS" "$(cls $E/yuanjiusheng_cloud-learning-ce__LICENSE)"
has "leemons is proprietary"            "PROPRIETARY-UNNAMED-NOT-OSS" "$(cls $E/leemonade_leemons__LICENSE.md)"
eq  "cloud-learning-ce signal count"    "PROPRIETARY-UNNAMED-NOT-OSS:restriction-signals=4" "$(cls $E/yuanjiusheng_cloud-learning-ce__LICENSE)"
# The guard that matters: a BSD file literally contains "All rights reserved",
# so a one-signal threshold would have called every BSD repo proprietary.
hasnt "BSD-3 ottr is NOT called proprietary"  "PROPRIETARY" "$(cls $E/ucbds-infra_ottr__LICENSE.md)"
hasnt "MIT ggcheck is NOT called proprietary" "PROPRIETARY" "$(cls $E/rstudio_ggcheck__LICENSE.md)"
hasnt "AGPL ais-chat is NOT called proprietary" "PROPRIETARY" "$(cls $E/FWU-DE_ais-chat__LICENSE)"
hasnt "Apache Ed-Fi is NOT called proprietary"  "PROPRIETARY" "$(cls $E/Ed-Fi-Alliance-OSS_Ed-Fi-Data-Standard__LICENSE)"
eq "ottr BSD does contain the reserved-rights phrase (so the guard is real)" "1" \
   "$(grep -ci 'All rights reserved' $E/ucbds-infra_ottr__LICENSE.md)"

echo
echo "C. resolution tiers are assigned as documented"
tier() { awk -F'\t' -v s="$1" 'tolower($1)==tolower(s){print $4}' verdict.2026-10-11.tsv; }
grant(){ awk -F'\t' -v s="$1" 'tolower($1)==tolower(s){print $3}' verdict.2026-10-11.tsv; }
has "openSIS resolves at tier 2 (README-named path)" "tier2:readme-named-file" "$(tier OS4ED/openSIS-Classic)"
has "learnpress resolves at tier 3 (wp readme.txt)"  "tier3:wp-readme.txt"     "$(tier LearnPress/learnpress)"
eq  "learnpress grant is GPLv3, not the ISC in package.json" "MANIFEST:GPLv3"  "$(grant LearnPress/learnpress)"
has "AITutor-EvalKit is a DANGLING pointer"  "AUTHOR-CLAIM-DANGLING-POINTER" "$(grant kaushal0494/AITutor-EvalKit)"
has "EPESI is an author claim with no file"  "AUTHOR-CLAIM-NO-FILE"          "$(grant cezarc/EPESI)"
eq  "openbadges-specification grants nothing" "NO-GRANT-FOUND"               "$(grant 1EdTech/openbadges-specification)"
eq  "CourseMapper grants nothing"             "NO-GRANT-FOUND"               "$(grant lovejzzz/CourseMapper)"
eq  "Zion checker grants nothing"             "NO-GRANT-FOUND"               "$(grant Zion-support/curriculum-alignment-checker)"
echo "   the dangling pointers really do 404 - recorded, not assumed"
for a in kaushal0494/AITutor-EvalKit qed42/ai-accessibility-checker lovejzzz/CourseMapper; do
  k=$(echo "$a" | tr '/' '_')
  eq "$a LICENSE is absent on its default branch" "404" \
     "$(awk -F'\t' -v s="$a" '$1==s && $3=="LICENSE"{print $4}' $E/manifest.tsv)"
done

echo
echo "D. CONTROL - p119's four ACTION F answers, reproduced from scratch"
has "leemons: proprietary, not Apache-2.0"   "PROPRIETARY" "$(grant leemonade/leemons)"
has "evaluators: a NonCommercial tier"       "NONCOMMERCIAL-TIER" "$(grant learning-commons-org/evaluators)"
has "evaluators: MIT is present too"         "MIT"         "$(grant learning-commons-org/evaluators)"
has "knowledge-graph: MIT + CC0 + CC BY"     "CC0"         "$(grant learning-commons-org/knowledge-graph)"
has "bncc-benchmark: a split grant"          "SPLIT-GRANT" "$(grant bncc-dev/bncc-benchmark)"
has "bncc-benchmark: data half is CC-BY"     "CC-BY"       "$(grant bncc-dev/bncc-benchmark)"

echo
echo "E. the census itself"
eq "22 addresses resolved" "22" "$(wc -l < verdict.2026-10-11.tsv | tr -d ' ')"
eq "every address names its tier" "22" "$(grep -c 'tier' verdict.2026-10-11.tsv)"
eq "no address left UNKNOWN" "0" "$(grep -c 'UNKNOWN' verdict.2026-10-11.tsv)"
eq "scorer runs clean" "0" "$(python3 -I score.py >/dev/null 2>&1; echo $?)"

echo
echo "F. the repair - every defect cleared, nothing else touched"
python3 -I score_after.py > .score_after.txt 2>&1
for v in OVERSTATED UNGRANTED WRONG; do
  eq "no $v claim remains after the repair" "0" "$(awk -v k="$v" '$1==k{print $2}' .score_after.txt | head -1; echo 0 | head -0; true)$(awk -v k="$v" '$1==k{print $2; f=1} END{if(!f) print 0}' .score_after.txt)"
done
eq "7 defects recorded" "7" "$(wc -l < defects.2026-10-11.tsv | tr -d ' ')"
# repair.py v2 is content-anchored, so on an already-repaired tree every entry
# reports "already clean" and nothing is written. Running it TWICE asserts both
# that it is idempotent and that it does not drift.
eq "repair.py is idempotent (run 1)" "0 repaired, 6 already clean" \
   "$(python3 -I repair.py 2>&1 | tail -1)"
eq "repair.py is idempotent (run 2)" "0 repaired, 6 already clean" \
   "$(python3 -I repair.py 2>&1 | tail -1)"
# and the guard that v2 exists for: no row this pass WROTE was repaired into a
# doubled marker.
eq "no doubled correction marker anywhere in the live pages" "0" \
   "$(cd /home/user/education-kb && grep -c "$(printf '\U0001F534') \*\*$(printf '\U0001F534') \*\*" \
        agents/top.md repos/foundations.md verticals/solutions.md intel/market.md \
        intel/trends.md compose/patterns.md README.md 2>/dev/null | awk -F: '{s+=$2} END{print s+0}')"
# The property is that the repair introduced no NEW malformed row - not that the
# pages have none. Four pre-existing pipe-prefixed lines are ASCII diagrams and a
# shell pipeline, correctly rendered, and an absolute count would fail on them
# forever. The count is therefore compared against git HEAD.
short_rows() { awk -F'|' '/^[ \t]*\|/ {if (NF<3) n++} END{print n+0}'; }
for f in agents/top.md verticals/solutions.md intel/market.md compose/patterns.md; do
  now=$(short_rows < "/home/user/education-kb/$f")
  was=$(git -C /home/user/education-kb show HEAD:"$f" | short_rows)
  eq "$f introduced no new malformed table row" "$was" "$now"
done

echo
printf '%s passed / %s failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
