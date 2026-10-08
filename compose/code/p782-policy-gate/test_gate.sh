#!/usr/bin/env bash
# Regression suite for p782.  Offline -- the matrix is committed data, so this suite has no
# network dependency and no excuse to go yellow (P713).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
G="$HERE/gate.sh"
pass=0; fail=0
ck() { if [ "$2" = "$3" ]; then pass=$((pass+1)); printf '  ok   %-56s %s\n' "$1" "$3"
       else fail=$((fail+1)); printf '  FAIL %-56s expected=%s actual=%s\n' "$1" "$2" "$3"; fi }
ec() { bash "$G" "$@" >/dev/null 2>&1; echo $?; }

echo "== verdicts map to exit codes"
ck "emotion_recognition EMEA -> PROHIBITED(4)"   4 "$(ec emotion_recognition EMEA)"
ck "assessment_grading EU    -> GATED(3)"        3 "$(ec assessment_grading EU)"
ck "assessment_grading BR    -> PROPOSED(5)"     5 "$(ec assessment_grading BR)"
ck "assessment_grading MX    -> clear(0)"        0 "$(ec assessment_grading MX)"
ck "ai_literacy_instruction US-IL -> clear(0)"   0 "$(ec ai_literacy_instruction US-IL)"

echo "== the strictest row wins when a function spans jurisdictions"
# Deliberate: a deployment ships to the jurisdictions it ships to, so an unscoped query
# must return the STRICTEST verdict present, never the friendliest.
ck "assessment_grading unscoped -> GATED(3)"     3 "$(ec assessment_grading)"
ck "teacher_replacement unscoped -> PROHIBITED(4)" 4 "$(ec teacher_replacement)"

echo "== an unmeasured pair is NOT a permission (P476) -- the property that matters most"
ck "assessment_grading US-TX -> NO ROW(6)"       6 "$(ec assessment_grading US-TX)"
ck "invented function        -> NO ROW(6)"       6 "$(ec facial_scoring_of_essays)"
ck "invented jurisdiction    -> NO ROW(6)"       6 "$(ec assessment_grading Narnia)"

echo "== region is a CLOSED vocabulary; a variant must fail loudly, not return {}"
# An empty result set reads exactly like "nothing is regulated there", which is the most
# expensive possible misreading of this file.
ck "--region Latam  -> FATAL(2)"                 2 "$(ec --region Latam)"
ck "--region Europe -> FATAL(2)"                 2 "$(ec --region Europe)"
ck "--region Brazil -> FATAL(2)"                 2 "$(ec --region Brazil)"
ck "--region LATAM  -> ok(0)"                    0 "$(ec --region LATAM)"
ck "--region 'North America' -> ok(0)"           0 "$(ec --region "North America")"

echo "== every one of the five regions except Global carries rows"
for r in "North America" EMEA APAC LATAM; do
  n=$(bash "$G" --region "$r" 2>/dev/null | head -1 | grep -o '[0-9]\+' | head -1)
  ck "region '$r' row count > 0" "yes" "$([ "${n:-0}" -gt 0 ] && echo yes || echo no)"
done

echo "== the data file parses: no row may carry an unknown verdict"
bad=$(grep -v '^#' "$HERE/../../../intel/policy-matrix.tsv" | awk -F'\t' 'NR>1 && NF>=4 {print $4}' \
      | sort -u | grep -vE '^(PROHIBITED|GATED|MANDATED|PROPOSED|UNREGULATED)$' | tr '\n' ' ')
ck "no unknown verdicts in the matrix" "" "$bad"
badr=$(grep -v '^#' "$HERE/../../../intel/policy-matrix.tsv" | awk -F'\t' 'NR>1 && NF>=4 {print $1}' \
      | sort -u | grep -vE '^(North America|EMEA|APAC|LATAM|Global)$' | tr '\n' ' ')
ck "no unknown regions in the matrix" "" "$badr"

echo
echo "  passed=$pass failed=$fail"
[ "$fail" -eq 0 ] || exit 1
