#!/usr/bin/env bash
# test_ladder.sh — two-sided control for grant_ladder.sh. Prints its own total (P126 pt.3).
# Exercises the case the instrument can FAIL at: an invented slug must be DENIED, not
# silently granted (P126 pt.2 — a positive control alone does not enable an instrument).
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
LADDER="$HERE/grant_ladder.sh"
pass=0; total=0

check() { # $1 label  $2 expected-substring  $3 actual
  total=$((total+1))
  if [[ "$3" == *"$2"* ]]; then pass=$((pass+1)); echo "  ok   — $1"
  else echo "  FAIL — $1 (expected '$2', got '$3')"; fi
}

echo "two-sided control for grant_ladder.sh"

# NEGATIVE control: the case this instrument can fail at.
neg=$(bash "$LADDER" invented-org-xyz/not-a-real-repo-999 2>/dev/null | tail -1)
check "invented slug is DENIED, not granted" "EXISTENCE-DENIED" "$neg"
check "invented slug yields no byte figure"  $'\t-\t-\t'         "$neg"

# POSITIVE control: a known copyleft payload, pinned.
pos=$(bash "$LADDER" moodle/moodle 2>/dev/null | tail -1)
check "moodle resolves a default ref"        "main"        "$pos"
check "moodle licence file is COPYING.txt"   "COPYING.txt" "$pos"
check "moodle canonical GPL-3.0 byte count"  "35147"       "$pos"
check "moodle family named GPL"              "GPL"         "$pos"

# POSITIVE control for the P946 case: appendix-replaced Apache is still Apache.
ool=$(bash "$LADDER" OpenOLAT/OpenOLAT 2>/dev/null | tail -1)
check "OpenOLAT default ref is master (T1)"  "master"      "$ool"
check "OpenOLAT grant is Apache-2.0"         "Apache-2.0"  "$ool"
check "OpenOLAT byte figure is 10982"        "10982"       "$ool"

# POSITIVE control for the P943 case: MIT with no family name in the payload.
gs=$(bash "$LADDER" gamestdio/scorm 2>/dev/null | tail -1)
check "unnamed MIT resolves by signature"    "MIT-by-signature" "$gs"

echo "$pass/$total controls passed"
[ "$pass" = "$total" ]
