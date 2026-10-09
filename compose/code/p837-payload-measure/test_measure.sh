#!/usr/bin/env bash
# Offline regression suite for `lib/payload_measure.sh` and `lib/measure`.
# Pass 74 of 2026-10-09, closing `Gap 328`.
#
# 🔵 Why this suite is OFFLINE while `lib/test_probe_payload.sh` is not.  That file opens with
# "These hit the network on purpose", and in this environment every one of its cases is
# unrunnable: `curl` to raw.githubusercontent.com is refused `[Exfil Scouting]` and sourcing
# `probe_payload.sh` at all is refused `[Code from External]`.  So the shelf's only probe
# suite cannot be run by the passes that most need it.  This one can.
#
# 🔴 Every case below is the case where the instrument CAN FAIL, per `P126`-2 — not a restating
# of a case that already passes.  The two that matter most are the NEGATIVE controls:
#   * `mit-no-newline` — the correct primitive and the `P834` defect must AGREE here.  A suite
#     that only checked the newline fixture would pass against an instrument that subtracted
#     1 unconditionally.
#   * `paths-lti-trap` — word-bounded counting must return 1 where substring counting returns 3.
#
# ⚠️ Fixtures, not live repositories, and that is a deliberate trade this suite names: a
# fixture cannot catch a change upstream.  It can catch every defect listed above, none of
# which needs the network, and it runs — which `test_probe_payload.sh` does not.
set -u
cd "$(dirname "$0")"
. ../lib/payload_measure.sh
F=fixtures
pass=0; fail=0
check() { # check <label> <expected> <actual>
  if [ "$2" = "$3" ]; then pass=$((pass+1)); printf '  OK   %s\n' "$1"
  else fail=$((fail+1)); printf '  FAIL %s\n       want %s\n       got  %s\n' "$1" "$2" "$3"; fi
}

printf '\n-- P834: the sizing primitive is byte-exact --\n'
check "mit-trailing-newline is 244 B"            "244" "$(size_of_file $F/mit-trailing-newline.txt)"
check "mit-no-newline is 243 B"                  "243" "$(size_of_file $F/mit-no-newline.txt)"
check "mit-three-newlines is 99 B"               "99"  "$(size_of_file $F/mit-three-newlines.txt)"
check "gpl3-section13 is 470 B"                  "470" "$(size_of_file $F/gpl3-section13.txt)"

printf '\n-- P834: the defect, and the NEGATIVE control where it must not fire --\n'
# POSITIVE: one trailing newline -> the capture method is one byte low.
check "capture is 1 B low on 1 trailing newline" "243" "$(size_of_capture_BROKEN $F/mit-trailing-newline.txt)"
check "  ... so the delta is exactly 1"          "1"   "$(trailing_newlines $F/mit-trailing-newline.txt)"
# NEGATIVE CONTROL: no trailing newline -> the two methods MUST agree.  This is the case that
# distinguishes "strips the trailing run" from "always subtracts one".
check "capture AGREES when no trailing newline"  "243" "$(size_of_capture_BROKEN $F/mit-no-newline.txt)"
check "  ... so the delta is exactly 0"          "0"   "$(trailing_newlines $F/mit-no-newline.txt)"
# `P834` as recorded says "one byte low".  It strips the whole run.
check "capture is 3 B low on 3 trailing newlines" "96" "$(size_of_capture_BROKEN $F/mit-three-newlines.txt)"
check "  ... so P834 is a RUN, not one byte"     "3"   "$(trailing_newlines $F/mit-three-newlines.txt)"

printf '\n-- P171: the classifier is delegated, never re-implemented --\n'
check "MIT payload -> MIT"                       "MIT" "$(family_of_file $F/mit-trailing-newline.txt)"
# The mandatory case from lib/README.md: GPL-3.0 section 13 is TITLED "Use with the GNU
# Affero General Public License", and section 6 contains "noncommercially".  A body-grep
# classifier reads this fixture as AGPL-3.0 or as NonCommercial.  Both are wrong.
check "GPL-3.0 section 13 is NOT AGPL"           "GPL-3.0" "$(family_of_file $F/gpl3-section13.txt)"
check "holder carried for MIT"                   "Copyright (c) 2026 Globant AI Studios" "$(holder_of_file $F/mit-trailing-newline.txt)"

printf '\n-- P831: word-bounded counting, and the substring trap it replaces --\n'
# The fixture holds `tooLTIp`, `muLTI-tenancy` and ONE real `src/lti/launch.ts`.
check "word-bounded LTI count is 1"              "1" "$(count_word_in_file $F/paths-lti-trap.txt 'lti')"
# NEGATIVE CONTROL: the defect this replaces.  Substring matching finds FOUR — and the
# fourth is the one worth recording: this suite was written expecting 3 (`tooLTIp`,
# `muLTI-tenancy`, the real `src/lti/`) and measured 4, because `src/utils/multiply.ts`
# contains `lti` as well (mu-LTI-ply).  🔵 The innocuous filename is the dangerous one: the
# two traps a human thinks to write down are the two a human would also have caught by eye.
check "  ... substring would have found 4"       "4" "$(grep -oiE 'lti' $F/paths-lti-trap.txt | wc -l | tr -d ' ')"
check "word-bounded count via stdin agrees"      "1" "$(cat $F/paths-lti-trap.txt | count_word_in_pathlist 'lti')"
check "a word absent from the list is 0"         "0" "$(count_word_in_file $F/paths-lti-trap.txt 'scorm')"

printf '\n-- the TSV row: six fields, same order as probe_repo --\n'
row=$(measure_payload_file $F/mit-trailing-newline.txt "globant/example" "main" "LICENSE")
check "field count is 6"                         "6" "$(printf '%s' "$row" | awk -F'\t' '{print NF}')"
check "bytes field is the exact size"            "244" "$(printf '%s' "$row" | cut -f4)"
check "family field is MIT"                      "MIT" "$(printf '%s' "$row" | cut -f5)"
check "a missing payload is NO-PAYLOAD, not 0 B" "NO-PAYLOAD" \
      "$(measure_payload_file $F/does-not-exist.txt globant/example main | cut -f3)"

printf '\n-- lib/measure: argument-invocable, and fails loudly --\n'
check "--size matches the primitive"             "244" "$(bash ../lib/measure --size $F/mit-trailing-newline.txt)"
check "--newlines reports the run"               "3"   "$(bash ../lib/measure --newlines $F/mit-three-newlines.txt)"
check "--family delegates to P171"               "GPL-3.0" "$(bash ../lib/measure --family $F/gpl3-section13.txt)"
check "--count is word-bounded"                  "1"   "$(bash ../lib/measure --count $F/paths-lti-trap.txt lti)"
# A missing payload must EXIT NON-ZERO, never print 0.  `Gap 328`'s whole point is that a
# pass must not be able to mistake a failure for a measurement.
bash ../lib/measure --size $F/does-not-exist.txt >/dev/null 2>&1
check "missing file exits non-zero"              "1" "$?"
bash ../lib/measure >/dev/null 2>&1
check "no arguments exits 2 with usage"          "2" "$?"

total=$((pass+fail))
printf '\ntest_measure.sh: %d/%d checks passed\n' "$pass" "$total"
[ "$fail" -eq 0 ]
