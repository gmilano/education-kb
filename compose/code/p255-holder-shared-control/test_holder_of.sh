#!/bin/bash
# Regression test for holder_of() in lib/license_family.sh.  Run: ./test_holder_of.sh
#
# THE REQUIRED CASE IS GPL-2.0, and the reason is the same one test_license_family.sh gives
# for requiring GPL-3.0: an instrument validated only on the class you care about scores 100%
# while broken.  p198's filter was written against the GPL-3.0 line ("Copyright (C) 2007 Free
# Software Foundation") and is correct on it.  GPL-2.0 writes TWO years -- "Copyright (C) 1989,
# 1991 Free Software Foundation" -- and the same filter lets it straight through.  A suite
# without a GPL-2.0 fixture cannot see that, so GPL-2.0 is mandatory here, not optional.
#
# The fixtures are REAL payloads, fetched from the trees named in their filenames, not hand-typed.
set -u
cd "$(dirname "$0")" && . ../lib/license_family.sh

n=0; fail=0
check() { n=$((n+1)); if [ "$2" = "$3" ]; then printf 'ok   %s\n' "$1"
  else printf 'FAIL %s\n       want: %s\n       got:  %s\n' "$1" "$2" "$3"; fail=$((fail+1)); fi; }
contains() { n=$((n+1)); case "$3" in *"$2"*) printf 'ok   %s\n' "$1" ;;
  *) printf 'FAIL %s\n       want substring: %s\n       got:  %s\n' "$1" "$2" "$3"; fail=$((fail+1)) ;; esac; }

GPL2=$(cat fixtures/gpl-2.0-openemis-core-LICENSE.txt)
GPL3=$(cat ../p184-holder-mismatch/fixtures/gpl-3.0-moodle-COPYING.txt)
APACHE=$(cat ../p184-holder-mismatch/fixtures/apache-2.0-deeptutor.txt)
DECL=$(cat fixtures/declaration-19B-frappe-education-license.txt)
MIT_H=$(cat fixtures/mit-with-holder.txt)
MIT_Y=$(cat fixtures/mit-year-only.txt)

# --- 1. THE CASE THAT OPENS P255 -----------------------------------------------------------
# GPL-2.0.  The family gate must answer before any copyright line is read.
contains "GPL-2.0 payload -> NOT-APPLICABLE, never the FSF" \
         "NOT-APPLICABLE (GPL-2.0" "$(holder_of "$GPL2")"
n=$((n+1)); case "$(holder_of "$GPL2")" in
  *"Free Software Foundation"*) printf 'FAIL GPL-2.0 must never report the FSF as holder\n'; fail=$((fail+1)) ;;
  *) printf 'ok   GPL-2.0 must never report the FSF as holder\n' ;; esac

# --- 2. NEGATIVE CONTROL: the two ungated instruments, reproduced verbatim ------------------
# These assertions pin the DEFECT.  They must keep passing: if a future pass "fixes" p198 in
# place, this test tells it that the old regex was the thing being replaced, not slandered.
p198_filter() { printf '%s' "$1" | grep -iE '^[[:space:]]*(Copyright|\(c\))' \
  | grep -viE 'Copyright \(C\) [0-9]{4} Free Software Foundation' | head -1 | sed 's/^[[:space:]]*//'; }
p204_filter() { printf '%s' "$1" | grep -m1 -iE 'copyright' | sed 's/^[[:space:]]*//'; }

contains "negative control: p198's regex LEAKS the FSF on GPL-2.0" \
         "Free Software Foundation" "$(p198_filter "$GPL2")"
contains "negative control: p204's grep LEAKS the FSF on GPL-2.0" \
         "Free Software Foundation" "$(p204_filter "$GPL2")"
contains "negative control: p198's anchor returns BODY PROSE on GPL-3.0" \
         "copyright on the Program" "$(p198_filter "$GPL3")"

# --- 3. The anchor must not reach the 'How to Apply These Terms' TEMPLATE -------------------
# Line 635 of a real GPL-3.0 payload is literally "Copyright (C) <year>  <name of author>".
# An unbounded anchor can return a PLACEHOLDER as a holder.
n=$((n+1)); case "$(holder_of "$GPL3")" in
  *"name of author"*) printf 'FAIL GPL-3.0 must never report the <name of author> template\n'; fail=$((fail+1)) ;;
  *) printf 'ok   GPL-3.0 must never report the <name of author> template\n' ;; esac
contains "GPL-3.0 payload -> NOT-APPLICABLE" "NOT-APPLICABLE (GPL-3.0" "$(holder_of "$GPL3")"

# --- 4. Apache-2.0: pristine boilerplate, holder absent by construction --------------------
contains "Apache-2.0 payload -> NOT-APPLICABLE" "NOT-APPLICABLE (Apache-2.0" "$(holder_of "$APACHE")"

# --- 5. A DECLARATION cedes nothing, so it has no holder (P179) -----------------------------
contains "19 B declaration -> NOT-APPLICABLE, and for the P179 reason" \
         "a declaration carries no holder" "$(holder_of "$DECL")"

# --- 6. The families that DO carry a holder must still return it ----------------------------
# The gate must not become a blanket refusal: that would lose P184 entirely.
check "MIT with holder -> the holder line" "Copyright (c) 2024 R.Huijts" "$(holder_of "$MIT_H")"

# --- 7. A year alone is not a holder (P198: no distinguishing holder -> zero identity) ------
check "MIT with a year and no name -> NO-HOLDER-LINE" "NO-HOLDER-LINE" "$(holder_of "$MIT_Y")"

# --- 8. ...AND A YEAR IS NOT A REQUIREMENT EITHER ------------------------------------------
# The regression this test exists for second.  The first cut of the guard demanded a digit
# after "Copyright (c)" and so returned NO-HOLDER-LINE for katoj65/emis -- the EMIS of the
# Ministry of Education of Uganda -- whose MIT text names "Jonathan Reinink" with NO year.
# Suppressing that line suppresses a P184 HOLDER-UNRELATED finding (Reinink is the author of
# Inertia.js, not of a Ugandan ministry EMIS), so the guard must test for a NAME, not a year.
MIT_NY=$(cat fixtures/mit-holder-no-year-katoj65.txt)
check "MIT holder with NO year -> still the holder line" \
      "Copyright (c) Jonathan Reinink <jonathan@reinink.ca>" "$(holder_of "$MIT_NY")"

# And the body lines of that same MIT text must never be mistaken for the holder.
n=$((n+1)); case "$(holder_of "$MIT_NY")" in
  *"shall be included"*|*"BE LIABLE"*) printf 'FAIL MIT body prose must not be read as a holder\n'; fail=$((fail+1)) ;;
  *) printf 'ok   MIT body prose must not be read as a holder\n' ;; esac

printf '\n%d/%d\n' "$((n-fail))" "$n"
[ "$fail" = 0 ] || exit 1
