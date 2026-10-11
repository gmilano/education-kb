#!/usr/bin/env bash
# p122 suite — FULLY OFFLINE. No network, no git, no clock.
# Run: ./test_p122.sh
cd "$(dirname "$0")" || exit 1
pass=0; fail=0
ok()   { pass=$((pass+1)); printf '  ok   %s\n' "$1"; }
bad()  { fail=$((fail+1)); printf '  FAIL %s\n   expected: %s\n   actual:   %s\n' "$1" "$2" "$3"; }
eq()   { if [ "$2" = "$3" ]; then ok "$1"; else bad "$1" "$2" "$3"; fi; }
cls()  { python3 -I classify_licence.py < "$1"; }

echo "== classify_licence: the nine captured licence files =="
eq "apache2 control"                 "Apache-2.0"      "$(cls fixtures/apache2-control.txt)"
eq "mit control"                     "MIT"             "$(cls fixtures/mit-control.txt)"
eq "bsd3 control"                    "BSD-3-Clause"    "$(cls fixtures/bsd3-control.txt)"
eq "elastic control"                 "Elastic-2.0"     "$(cls fixtures/elastic-control.txt)"
eq "agpl3 control"                   "AGPL-3.0"        "$(cls fixtures/agpl3-control.txt)"
eq "gpl2 whose preamble names LGPL"  "GPL-2.0"         "$(cls fixtures/gpl2-preamble-names-lesser.txt)"
eq "epl2 whose clause names GPL-2.0" "EPL-2.0"         "$(cls fixtures/epl2-secondary-names-gpl2.txt)"
eq "mpl2 whose clause names GPL"     "MPL-2.0"         "$(cls fixtures/mpl2-secondary-names-gpl.txt)"
eq "split grant, primary MIT"        "SPLIT:MIT"       "$(cls fixtures/mit-split-grant-names-cc.txt)"
eq "cc-by-nc-sa control"             "CC-BY-NC-SA-4.0" "$(cls fixtures/cc-by-nc-sa-control.txt)"
eq "headerless LGPL-3.0"             "LGPL-3.0"        "$(cls fixtures/lgpl3-headerless.txt)"
eq "pt-BR dual licence, by reference" "SPLIT-REF:MIT+CC-BY-4.0" "$(cls fixtures/split-grant-portuguese.txt)"
eq "fair-code grant is named non-OSI" "SPLIT:FairCode-NonOSI"   "$(cls fixtures/faircode-sustainable-use.txt)"
eq "R/CRAN stub names its next tier" "STUB-SEE-DESCRIPTION"    "$(cls fixtures/r-stub-licence.txt)"
eq "unmarked split names ALL 3 grants" "SPLIT-REF:MIT+CC-BY-4.0+CC-BY-NC-SA-4.0" "$(cls fixtures/split-unmarked-code-vs-content.txt)"

echo "== the three defect classes, asserted as such =="
# 1. A NAME must never outvote a TITLE.
eq "GPL-2.0 file is not LGPL" "no-lesser" \
   "$([ "$(cls fixtures/gpl2-preamble-names-lesser.txt)" = "LGPL" ] && echo lesser || echo no-lesser)"
eq "EPL-2.0 file is not GPL"  "no-gpl" \
   "$(case "$(cls fixtures/epl2-secondary-names-gpl2.txt)" in GPL*) echo gpl;; *) echo no-gpl;; esac)"
eq "MPL-2.0 file is not AGPL" "no-agpl" \
   "$(case "$(cls fixtures/mpl2-secondary-names-gpl.txt)" in *GPL-3.0) echo agpl;; *) echo no-agpl;; esac)"
# 2. A split grant must be REPORTED as split, not silently reduced.
eq "split is flagged, not reduced" "split" \
   "$(case "$(cls fixtures/mit-split-grant-names-cc.txt)" in SPLIT:*) echo split;; *) echo reduced;; esac)"
# 3. A mere mention of a licence yields no token.
eq "mention-only is UNKNOWN" "UNKNOWN" \
   "$(printf 'This project is licensed under the MIT license. See docs.\n' | python3 -I classify_licence.py)"
eq "empty file is EMPTY" "EMPTY" "$(printf '' | python3 -I classify_licence.py)"
# 4. A headerless LGPL-3.0 must not degrade to an untitled GPL.
eq "headerless LGPL is not GPL-UNTITLED" "no" \
   "$([ "$(cls fixtures/lgpl3-headerless.txt)" = "GPL-UNTITLED" ] && echo yes || echo no)"
# 5. A split marker in another language must still split.
eq "pt-BR split is detected" "split" \
   "$(case "$(cls fixtures/split-grant-portuguese.txt)" in SPLIT*) echo split;; *) echo missed;; esac)"
# 6. A non-OSI grant must never be reported as a copyleft token.
eq "fair-code is not GPL" "no" \
   "$(case "$(cls fixtures/faircode-sustainable-use.txt)" in *GPL*) echo yes;; *) echo no;; esac)"
eq "fair-code is marked non-OSI" "yes" \
   "$(case "$(cls fixtures/faircode-sustainable-use.txt)" in *NonOSI*) echo yes;; *) echo no;; esac)"
# 7. A by-reference resolution must stay visibly weaker than a read body.
eq "by-reference tier is visible" "yes" \
   "$(case "$(cls fixtures/split-grant-portuguese.txt)" in SPLIT-REF:*) echo yes;; *) echo no;; esac)"

echo "== token equivalence (join normalisation) =="
n() { python3 -I -c "import sys;sys.path.insert(0,'.');from join_claims import norm;print(norm(sys.argv[1]))" "$1"; }
eq "Apache 2.0 == Apache-2.0" "$(n 'Apache-2.0')" "$(n 'Apache 2.0')"
eq "AGPL-3 == AGPL-3.0"       "$(n 'AGPL-3.0')"   "$(n 'AGPL-3')"
eq "AGPLv3 == AGPL-3.0"       "$(n 'AGPL-3.0')"   "$(n 'AGPLv3')"
eq "GPLv3 == GPL-3.0"         "$(n 'GPL-3.0')"    "$(n 'GPLv3')"
eq "LGPLv3 == LGPL-3.0"       "$(n 'LGPL-3.0')"   "$(n 'LGPLv3')"
eq "MIT != Apache-2.0"        "differ" \
   "$([ "$(n MIT)" = "$(n Apache-2.0)" ] && echo same || echo differ)"

echo "== ACTION U: slug case must not split one address into two =="
u() { python3 -I -c "
import sys;sys.path.insert(0,'.')
from join_claims import fold
print(len(fold(sys.argv[1:])))" "$@"; }
eq "two spellings fold to one" "1" "$(u 'xGabrielCv/Auto-Matricula' 'xgabrielcv/auto-matricula')"
eq "distinct addresses stay two" "2" "$(u 'a/one' 'a/two')"
eq "三 spellings fold to one" "1" "$(u 'DSpace/DSpace' 'dspace/dspace' 'DSPACE/DSPACE')"

echo "== a stub must never read as an absent grant =="
# 8. An R/CRAN stub is the tier-2 case, NOT tier-5 "no grant". Conflating the
#    two publishes "no licence" for a repository that states MIT in DESCRIPTION.
eq "stub is not UNKNOWN"  "no"  "$([ "$(cls fixtures/r-stub-licence.txt)" = "UNKNOWN" ] && echo yes || echo no)"
eq "stub is not NO-FILE"  "no"  "$([ "$(cls fixtures/r-stub-licence.txt)" = "NO-FILE" ] && echo yes || echo no)"
eq "stub points at a tier" "yes" "$(case "$(cls fixtures/r-stub-licence.txt)" in *DESCRIPTION*) echo yes;; *) echo no;; esac)"
# 9. A NonCommercial arm of a split grant must never be dropped: it is the
#    arm that decides whether Globant can build on the repository at all.
eq "NonCommercial arm is kept" "yes" \
   "$(case "$(cls fixtures/split-unmarked-code-vs-content.txt)" in *NC-SA*) echo yes;; *) echo no;; esac)"

echo "== verdicts: a SPLIT primary agrees with a bare claim of that licence =="
v() { python3 -I -c "
import sys;sys.path.insert(0,'.')
from join_claims import verdict
print(verdict(sys.argv[1], sys.argv[2]))" "$1" "$2"; }
eq "MIT vs SPLIT:MIT agrees"        "AGREES-SPLIT"  "$(v MIT 'SPLIT:MIT')"
eq "MIT vs SPLIT-REF:MIT+CC agrees" "AGREES-REF"    "$(v MIT 'SPLIT-REF:MIT+CC-BY-4.0')"
eq "GPL-3.0 vs SPLIT:FairCode"      "DISAGREES"     "$(v 'GPL-3.0' 'SPLIT:FairCode-NonOSI')"
eq "MIT vs CC-BY-NC-SA-4.0"         "DISAGREES"     "$(v MIT 'CC-BY-NC-SA-4.0')"
eq "Apache 2.0 vs Apache-2.0"       "AGREES"        "$(v 'Apache 2.0' 'Apache-2.0')"
eq "NO-FILE is unmeasurable"        "UNMEASURABLE"  "$(v MIT 'NO-FILE')"
eq "stub is unmeasurable, not wrong" "UNMEASURABLE" "$(v MIT 'STUB-SEE-DESCRIPTION')"
eq "MIT vs SPLIT-REF:MIT (unmarked)" "AGREES-REF"   "$(v MIT 'SPLIT-REF:MIT')"

echo "== P121-B: an inline correction is not a defect =="
c() { python3 -I -c "
import sys;sys.path.insert(0,'.')
from join_claims import is_correction
print('correction' if is_correction(sys.argv[1]) else 'claim')" "$1"; }
eq "inline 'was X' marker"   "correction" "$(c 'freelingo is MIT ⚠️ **was 🟢 MIT**')"
eq "'actually' marker"       "correction" "$(c 'published MIT, actually AGPL-3.0')"
eq "plain assertion"         "claim"      "$(c 'OATutor is an MIT-licensed tutoring system.')"

echo
echo "p122: $pass passed / $fail failed"
[ "$fail" -eq 0 ]
