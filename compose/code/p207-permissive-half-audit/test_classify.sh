#!/usr/bin/env bash
# p207 — offline tests for the permissive-half classifier repairs.
# NO NETWORK. Every fixture is a real body read from its own blob this pass,
# or (mit-plain, apache, elastic2) a minimal regression guard.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
. "$HERE/classify.sh"
pass=0; fail=0
t() { # t <fixture> <expected> <why>
  got=$(classify_grant "$(cat "$HERE/fixtures/$1")")
  if [ "$got" = "$2" ]; then pass=$((pass+1)); printf 'ok   %-28s %s\n' "$1" "$got"
  else fail=$((fail+1)); printf 'FAIL %-28s got=%s want=%s  (%s)\n' "$1" "$got" "$2" "$3"; fi
}

# --- D11: the dot in `cc0 1\.0 universal` was double-escaped in p206, so the
# title line never matched and every CC0 body fell through to CC-unversioned.
t cc0.txt                     CC0-1.0                      "D11 double-escaped dot"

# --- D12: BSD was in p206's TITLE_RE but had no arm in the title case block,
# so a titled BSD-3 body fell to the body fallback and came back BSD-2 --
# a 3-clause licence reported as 2-clause, losing the no-endorsement clause.
t bsd3.txt                    BSD-3-Clause                 "D12 BSD-3 reported as BSD-2"

# --- D13: "attribution-noncommercial" matched before any ShareAlike test, and
# the deed branch tested /by-sa/ and /by-nc/ but never /by-nc-sa/.
t bync-sa-title.txt           CC-BY-NC-SA-4.0              "D13 ShareAlike dropped"
t bync-sa-deed.txt            CC-BY-NC-SA-4.0-DEED         "D13 deed fell through"

# --- D14: a rider AMENDS the licence below it. p206 returned a confident,
# clean "MIT" here -- strictly worse than the UNRECOGNISED of T206-4, because
# UNRECOGNISED at least asks to be looked at.
t commons-clause-mit.txt      NON-OSI-CommonsClause+MIT    "D14 rider invisible"

# --- the adversarial shape that put a wrong cell on this shelf: the MIT verb
# list appearing inside a PROHIBITION. A reader that greps for the verbs says
# MIT; the body reserves all rights.
t proprietary-inverted-mit.txt NON-OSI-proprietary         "inverted MIT"

# --- regression guards: p205's and p206's repairs must still hold.
t mit-plain.txt               MIT                          "p205 title anchor"
t apache.txt                  Apache-2.0                   "p205 title anchor"
t elastic2.txt                NON-OSI-Elastic-2.0          "p206 D4"
t pt-agpl.txt                 AGPL-3.0                     "p206 D3 Portuguese"
t agpl-notice.txt             AGPL-3.0                     "titled AGPL notice, family right"
t r-description-stub.txt      UNRECOGNISED                 "R manifest channel, not a body"

printf '\n%d/%d passed\n' "$pass" "$((pass+fail))"
[ "$fail" -eq 0 ]
