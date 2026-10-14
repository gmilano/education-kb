#!/bin/bash
# Offline checks for p201-licence-channel/probe_licence_blob.sh.
#
# These do NOT hit the network: they assert the properties that the p201 measurement turned
# into requirements.  The network reads themselves are recorded in
# evidence/paella-grant-found.2026-10-14-p201.tsv and
# evidence/topic-lms-licence-coverage.2026-10-14-p201.tsv.
set -u
cd "$(dirname "$0")"
pass=0; fail=0
ck() { if [ "$2" = "$3" ]; then echo "ok   $1"; pass=$((pass+1));
       else echo "FAIL $1 (want '$3', got '$2')"; fail=$((fail+1)); fi; }
has() { if printf '%s' "$2" | grep -qF -- "$3"; then echo "ok   $1"; pass=$((pass+1));
        else echo "FAIL $1 (missing '$3')"; fail=$((fail+1)); fi; }

V=$(sed -n '/^LICENCE_PATHS=/,/"$/p' probe_licence_blob.sh)

# The four path forms p200 missed or found late.  Each is a real repository's real grant.
has "lowercase license.txt is in the vocabulary (paella, erpnext)" "$V" "license.txt"
has "non-root docs/License.txt is in the vocabulary (openSIS)"     "$V" "docs/License.txt"
has "COPYING.txt is in the vocabulary (moodle)"                    "$V" "COPYING.txt"
has "LICENSE.md is in the vocabulary (courselit, leemons)"         "$V" "LICENSE.md"
has "a licence DIRECTORY form is in the vocabulary"                "$V" "LICENSE/LICENSE"
has "COPYING.LESSER is in the vocabulary (LGPL)"                   "$V" "COPYING.LESSER"

# Gap 454: capitalised-only vocabularies are what produced the false absence.
lower=$(printf '%s' "$V" | grep -o 'license\.txt' | head -1)
ck  "the vocabulary is case-aware, not case-folded" "$lower" "license.txt"

# The branch must be resolved, never assumed: 11 of 35 p201 repos use neither main nor master.
has "branch is resolved with ls-remote --symref" "$(cat probe_licence_blob.sh)" "ls-remote --symref"
if grep -qE 'raw\.githubusercontent\.com/\$slug/(main|master)/' probe_licence_blob.sh; then
  echo "FAIL the script hardcodes a branch in the raw URL"; fail=$((fail+1))
else
  echo "ok   no hardcoded main/master in the raw URL"; pass=$((pass+1))
fi

# P237: this instrument must not classify.  Classification is lib/license_family.sh's job.
if grep -qiE 'affero|gpl-3\.0|spdx_id *=' probe_licence_blob.sh; then
  echo "FAIL the probe tries to classify (P237: use lib/license_family.sh)"; fail=$((fail+1))
else
  echo "ok   the probe does not classify (defers to lib/license_family.sh)"; pass=$((pass+1))
fi

# Usage contract.
out=$(bash probe_licence_blob.sh 2>&1); rc=$?
ck "no arguments exits 2" "$rc" "2"
has "no arguments prints usage" "$out" "usage:"

echo
echo "$((pass+fail)) checks: $pass passed, $fail failed"
[ "$fail" -eq 0 ]
