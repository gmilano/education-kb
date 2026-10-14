#!/bin/bash
# p197 -- the suite for `run_from_dirs.sh`, and its cases are NEGATIVE on purpose.
#
# A runner that only ever reports CLEAN proves nothing: it would report CLEAN on the very
# defect it was written to find.  So the cases below hand it (1) a replica of the suite with
# the PRE-FIX relative resolution restored, (2) a replica whose fixtures are gone, (3) a
# path that does not exist and (4) a script that prints no total -- and assert that it says
# so in each case, with the right verdict and a non-zero exit.  Case 5 is the real suite.
set -u
HERE="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}" 2>/dev/null || printf '%s' "${BASH_SOURCE[0]}")")" && pwd)"
CODE="$(cd "$HERE/.." && pwd)"
RUNNER="$HERE/run_from_dirs.sh"
n=0; fail=0
check() { n=$((n+1)); if [ "$2" = "$3" ]; then printf 'ok   %-56s %s\n' "$1" "$3"
  else printf 'FAIL %-56s expected=%s got=%s\n' "$1" "$2" "$3"; fail=$((fail+1)); fi; }
checkc() { n=$((n+1)); case "$3" in *"$2"*) printf 'ok   %-56s contains %s\n' "$1" "$2";;
  *) printf 'FAIL %-56s expected to contain=%s got=%s\n' "$1" "$2" "$3"; fail=$((fail+1));; esac; }

# A replica of just enough of compose/code for the suite to run: lib/ plus the three
# sibling fixture directories it reaches into.
mk_replica() { # dest
  local d="$1"
  mkdir -p "$d"
  cp -a "$CODE/lib" "$d/"
  for s in p560-epl-mpl-version-read p173-apache11-family p308-phrase-anchor-sweep; do
    mkdir -p "$d/$s"; cp -a "$CODE/$s/fixtures" "$d/$s/" 2>/dev/null || true
  done
}

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

# --- CASE 1: the pre-fix suite.  This is p196's defect, restored on purpose. ------------
mk_replica "$TMP/defective"
S1="$TMP/defective/lib/test_license_family.sh"
python3 - "$S1" <<'PY'
import sys,re
p=sys.argv[1]; s=open(p).read()
# revert p197's absolute resolution to the relative forms the file carried before it
# restore the EXACT pre-p197 header: one `cd $(dirname $0)`, no absolute resolution,
# no source guard and no family_of assertion.  A half-reverted replica would test the
# half, and C1 exists to reproduce p196's reading, not an approximation of it.
import re
i=s.index('# p197 (pre-registrado por p196)'); j=s.index('fi\n', s.index('family_of no esta definida'))+3
s = s[:i] + 'cd "$(dirname "$0")" && . ./license_family.sh\n' + s[j:]
s=s.replace('FIXP551="$_SUITE_HERE/fixtures-p551"','FIXP551="fixtures-p551"')
s=s.replace('FIXP613="$_SUITE_HERE/fixtures-p613"','FIXP613=fixtures-p613')
s=s.replace('FIXP560="$_SUITE_HERE/../p560-epl-mpl-version-read/fixtures"','FIXP560="$(dirname "${BASH_SOURCE[0]}")/../p560-epl-mpl-version-read/fixtures"')
s=s.replace('_H845="$_SUITE_HERE"','_H845="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"')
s=s.replace('_H852="$_SUITE_HERE"','_H852="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"')
s=s.replace('_A11="$_SUITE_HERE/','_A11="$(dirname "$0")/')
s=s.replace('_A11NEG="$_SUITE_HERE/','_A11NEG="$(dirname "$0")/')
s=s.replace('_BSD3="$_SUITE_HERE/','_BSD3="$(dirname "$0")/')
open(p,'w').write(s)
PY
O1="$(SUITE_UNDER_TEST="$S1" bash "$RUNNER" "$HERE/result.prefix-replica.$(date +%F)-p197.tsv" 2>&1)"; R1=$?
cp "$HERE/result.prefix-replica.$(date +%F)-p197.tsv" "$TMP/o1.tsv"
check  "C1 the pre-fix suite is REJECTED (exit)"            1 "$R1"
checkc "C1 and the runner says which way"                   "NOT PATH-INDEPENDENT" "$O1"
T1="$(awk -F'\t' 'NR>1{print $4}' "$TMP/o1.tsv" | sort -u | wc -l)"
# THREE distinct totals, not two.  p196 saw 207 and 181 and recorded "the directory";
# the symlink form of the SAME pre-fix suite answers 163, because there the classifier
# itself never loads.  One defect, three denominators, and every one of them printed as
# if it were the suite's size.
check  "C1 the forms give THREE distinct totals"            3 "$T1"
checkc "C1 and a form reports SILENT-SKIP"                  "SILENT-SKIP" "$O1"
# the in-dir form still passes -- that is why p196 could see 207/207 and 179/181 at once
check  "C1 in-suite-dir still totals 207 (p196's reading)"  207 \
  "$(awk -F'\t' '$1=="in-suite-dir"{print $4}' "$TMP/o1.tsv")"

# --- CASE 2: fixtures removed.  Absence must not pass. ----------------------------------
mk_replica "$TMP/nofix"
rm -rf "$TMP/nofix/p173-apache11-family" "$TMP/nofix/lib/fixtures-p845"
O2="$(SUITE_UNDER_TEST="$TMP/nofix/lib/test_license_family.sh" bash "$RUNNER" "$TMP/o2.tsv" 2>&1)"; R2=$?
check  "C2 a suite missing fixtures is REJECTED"            1 "$R2"
V2="$(awk -F'\t' 'NR>1{print $8}' "$TMP/o2.tsv" | sort -u | tr '\n' ' ')"
checkc "C2 every form is loud, none CLEAN"                  "SILENT-SKIP" "$V2"
case "$V2" in *CLEAN*) printf 'FAIL %-56s a form was CLEAN with fixtures gone\n' "C2 no form may be CLEAN"; fail=$((fail+1));;
  *) printf 'ok   %-56s none\n' "C2 no form may be CLEAN"; esac; n=$((n+1))
# the canaries p197 added are the reason absence is visible at all in the ones that run
checkc "C2 the p845 presence canary FAILS, not skips"       "FAIL" "$(SUITE_UNDER_TEST=x bash -c 'true'; cd "$TMP/nofix/lib" && bash test_license_family.sh | grep -E 'FAIL (P845|T232)')"

# --- CASE 3: a suite that is not there.  RUNFAIL, never 0/0 and never CLEAN. ------------
O3="$(SUITE_UNDER_TEST="$TMP/does-not-exist.sh" bash "$RUNNER" "$TMP/o3.tsv" 2>&1)"; R3=$?
check  "C3 a missing suite is REJECTED"                     1 "$R3"
check  "C3 and recorded RUNFAIL, not 0"                     RUNFAIL \
  "$(awk -F'\t' 'NR==2{print $4}' "$TMP/o3.tsv")"
case "$O3" in *" 0 "*|*"total=0"*) printf 'FAIL %-56s a zero was printed\n' "C3 no zero"; fail=$((fail+1));;
  *) printf 'ok   %-56s none\n' "C3 no zero"; esac; n=$((n+1))

# --- CASE 4: a script that runs fine and prints no total -------------------------------
printf '#!/bin/bash\necho "ok   something"\n' > "$TMP/silent.sh"
O4="$(SUITE_UNDER_TEST="$TMP/silent.sh" bash "$RUNNER" "$TMP/o4.tsv" 2>&1)"; R4=$?
check  "C4 a suite with no N/M line is REJECTED"            1 "$R4"
check  "C4 and recorded RUNFAIL"                            RUNFAIL \
  "$(awk -F'\t' 'NR==2{print $8}' "$TMP/o4.tsv")"

# --- CASE 5: the real suite, as committed ----------------------------------------------
O5="$(bash "$RUNNER" "$TMP/o5.tsv" 2>&1)"; R5=$?
check  "C5 the committed suite is PATH-INDEPENDENT"         0 "$R5"
check  "C5 six forms, one total"                            1 \
  "$(awk -F'\t' 'NR>1{print $4}' "$TMP/o5.tsv" | sort -u | wc -l)"
check  "C5 and that total is 207"                           207 \
  "$(awk -F'\t' 'NR==2{print $4}' "$TMP/o5.tsv")"
check  "C5 six forms measured"                              6 \
  "$(awk -F'\t' 'NR>1' "$TMP/o5.tsv" | wc -l)"
check  "C5 zero SKIP lines across all forms"                0 \
  "$(awk -F'\t' 'NR>1{s+=$7} END{print s+0}' "$TMP/o5.tsv")"

echo
echo "$((n-fail))/$n"
[ "$fail" -eq 0 ]
