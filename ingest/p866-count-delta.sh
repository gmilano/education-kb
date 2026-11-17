#!/bin/bash
# p866 -- discharge of `865-G2`: the uncounted-table detector, reported as a DELTA.
#
# THE DEFECT IT ANSWERS.  `derive-counts.py`'s uncounted-table detector named
# `repos/foundations.md` lines 14 and 43 in BOTH `p863`'s and `p864`'s gate output and
# both passes read past it -- because the line arrived inside a 13-table RED block that
# had been standing for many passes.  Seven shelf rows were counted nowhere as a result.
# `865-G2`: "the defect is not the miscount, it is that a standing RED has no delta."
#
# TWO ARMS, because the first version of this script had ONE and silently conflated them.
# A pass can break the count two ways -- by editing a SHELF, or by editing the DETECTOR --
# and one arm cannot tell those apart:
#
#   ARM A (content)    the WORKING detector, run over `git archive HEAD` and over the
#                      working tree.  The detector is held constant, so every difference
#                      is a shelf edit this pass made.  This is the arm that fails.
#   ARM B (published)  HEAD's OWN detector over HEAD, against the working detector over
#                      the working tree -- i.e. what `make hooks` printed last pass
#                      against what it prints now.  A declaration added to the detector
#                      shows up here and nowhere else.  Reported, never failed on: closing
#                      REDs by declaring a signature is the intended repair, not a defect.
#
# Exit 0 = ARM A clean.  Exit 1 = this working tree broke a table.
set -u
cd "$(dirname "$0")/.." || exit 2
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/head"
git archive HEAD | tar -x -C "$TMP/head" || { echo "🔴 git archive HEAD failed"; exit 2; }

det() { python3 -I "$1" "$2" 2>&1 | grep -E 'RED|line [0-9]+ \([0-9]+ rows\)' | sed 's/^[[:space:]]*//' | sort; }
WORK_DET=ingest/derive-counts.py
HEAD_DET="$TMP/head/ingest/derive-counts.py"

det "$WORK_DET" "$TMP/head" > "$TMP/a_head.txt"
det "$WORK_DET" "."         > "$TMP/a_work.txt"
det "$HEAD_DET" "$TMP/head" > "$TMP/b_head.txt"
cp "$TMP/a_work.txt" "$TMP/b_work.txt"

report() { # $1 label  $2 head-set  $3 work-set  $4 fail?
  local new gone carried
  new=$(comm -13 "$2" "$3"); gone=$(comm -23 "$2" "$3")
  carried=$(comm -12 "$2" "$3" | wc -l | tr -d ' ')
  echo "   ── $1"
  echo "      carried : $carried line(s)"
  [ -n "$gone" ] && { echo "      🟢 closed  : $(echo "$gone" | wc -l | tr -d ' ') line(s)"; echo "$gone" | sed 's/^/         - /' | head -8; }
  if [ -n "$new" ]; then
    echo "      🔴 NEW     : $(echo "$new" | wc -l | tr -d ' ') line(s)"
    echo "$new" | sed 's/^/         + /' | head -12
    [ "$4" = "fail" ] && return 1
  else
    echo "      🟢 NEW     : none"
  fi
  return 0
}

echo "── p866-count-delta — uncounted-table detector, HEAD vs working tree"
rc=0
report "ARM A (content): working detector, HEAD content vs working content" "$TMP/a_head.txt" "$TMP/a_work.txt" fail || rc=1
report "ARM B (published): HEAD's detector at HEAD vs working detector now" "$TMP/b_head.txt" "$TMP/b_work.txt" report || true
exit $rc
