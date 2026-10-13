#!/bin/sh
# Tests for licence_fold.sh. Every fixture is a REAL body read at p169 from
# raw.githubusercontent.com, pinned at the HEAD sha recorded in
# evidence/agent-grant-surface.2026-10-13-p169.tsv.
#
# The controls matter more than the findings: a fold that silences a REAL
# modification is worse than no fold, so case 5 asserts that DeepTutor's
# altered body still reads as deviant AFTER folding.

set -eu
cd "$(dirname "$0")"
FIX=./fixtures
pass=0; fail=0

check() {
    name=$1; canon=$2; body=$3; want=$4
    got=$(./licence_fold.sh "$FIX/$canon" "$FIX/$body")
    if [ "$got" = "$want" ]; then
        pass=$((pass+1)); printf 'ok    %s\t(%s)\n' "$name" "$got"
    else
        fail=$((fail+1)); printf 'FAIL  %s\twant=%s got=%s\n' "$name" "$want" "$got"
    fi
}

# 1. THE REGRESSION THIS SCRIPT EXISTS FOR. tutor-gpt's GPL-3.0 vs SPDX's copy.
#    Unfolded this is 71/71. Folded it is 1/1, and the one word is the FSF's
#    philosophy/ -> licenses/why-not-lgpl.html revision, which p168 identified
#    independently as the whole 2-byte spread in its own band test.
check "tutor-gpt GPL-3.0 is clean at one word" canon-gpl3.txt tutor-gpt-LICENSE "1	1"

# 2-4. Three AGPL-3.0 bodies, two byte-identical and one a byte apart. All fold to
#      ZERO deviation, so the 1-byte spread is trailing whitespace and nothing else.
check "penecho AGPL-3.0 verbatim"   canon-agpl.txt penecho-LICENSE   "0	0"
check "Echo-Loop AGPL-3.0 verbatim" canon-agpl.txt echo-loop-LICENSE "0	0"
check "ChatTutor AGPL-3.0 verbatim" canon-agpl.txt chattutor-LICENSE "0	0"

# 5. CONTROL - the fold must NOT silence a real change. DeepTutor's Apache-2.0 has an
#    altered section 4(d) and a rewritten APPENDIX; it must stay loudly deviant.
check "DeepTutor Apache-2.0 still deviant after folding" canon-apache.txt deeptutor-LICENSE "40	29"

# 6. CONTROL - a filled-in APPENDIX placeholder is a SMALL, bounded diff, not zero.
#    ai-shifu replaced [yyyy] and [name of copyright owner]; that is 2 added / 5 removed.
check "ai-shifu Apache-2.0 placeholder only" canon-apache.txt ai-shifu-LICENSE.txt "2	5"

# 7. CONTROL - identity. Any body against itself must be 0/0, folded or not.
check "identity: canonical vs canonical" canon-gpl3.txt canon-gpl3.txt "0	0"

printf '\n%s passed, %s failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
