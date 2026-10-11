#!/usr/bin/env bash
# p125 — ACTION AF, AG, AH, AI. Fully offline: no network, no clock, no
# environment. Every licence fixture is a real file from a real repository and
# every markdown fixture is a real construction copied off this KB's own live
# pages.
#
#   ./test_p125.sh
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
FX="$HERE/fixtures"
PASS=0; FAIL=0
ok(){ PASS=$((PASS+1)); printf '  \033[32mPASS\033[0m %s\n' "$1"; }
no(){ FAIL=$((FAIL+1)); printf '  \033[31mFAIL\033[0m %s — %s\n' "$1" "$2"; }
eq(){ [ "$2" = "$3" ] && ok "$1" || no "$1" "expected [$3], got [$2]"; }
has(){ case "$2" in *"$3"*) ok "$1";; *) no "$1" "[$3] not in [$2]";; esac; }
hasnt(){ case "$2" in *"$3"*) no "$1" "[$3] unexpectedly in output";; *) ok "$1";; esac; }

py(){ python3 -I -c "$1" "${@:2}"; }

echo
echo "=== ACTION AG — no licence token may be read without reading what SCOPES it ==="
# The clause: refuted if the check does not reproduce all four known
# instances. An instance is a (file, NAIVE pattern) pair -- the pattern that
# actually produced the defect -- and it is reproduced when no naive match
# survives the gate as a GRANT.
AG=$(py '
import sys, os, re
sys.path.insert(0, sys.argv[1]); os.chdir(sys.argv[1])
import scope_gate as sg
fx = sys.argv[2]
CASES = [("gpl2-preamble-names-lesser.txt", r"GNU Lesser General Public License", "PREAMBLE"),
         ("epl2-secondary-names-gpl2.txt",  r"GNU General Public License",        "SECONDARY"),
         ("ccby4-legalcode-names-cc0.txt",  r"CC0",                               "DOCUMENT-TEXT"),
         ("ccbysa4-not-a-split.txt",        r"\bCC[ -]?BY\b",                     "SUBSTRING")]
for fn, naive, want in CASES:
    t = open(os.path.join(fx, fn), encoding="utf-8", errors="replace").read()
    if t[:1] == "﻿": t = t[1:]
    hits = list(re.finditer(naive, t))
    labs = {sg.label_span(t, m.start(), m.end()) for m in hits}
    print("%s|%d|%s|%s" % (fn, len(hits), ",".join(sorted(labs)),
                           "SURVIVED" if "GRANT" in labs else "DISCARDED"))
for fn in ["mit-control.txt","apache2-control.txt","agpl3-control.txt",
           "bsd3-control.txt","cc-by-nc-sa-control.txt"]:
    t = open(os.path.join(fx, fn), encoding="utf-8", errors="replace").read()
    print("CTRL|%s|%s" % (fn, ",".join(sorted({x for x,_ in sg.grants(t)}))))
' "$HERE" "$FX")

has "AG.1 GPL-2.0 preamble names the Lesser GPL -> PREAMBLE, discarded" "$AG" "gpl2-preamble-names-lesser.txt|1|PREAMBLE|DISCARDED"
has "AG.2 EPL-2.0 secondary clause names GPL-2.0 -> SECONDARY, discarded" "$AG" "epl2-secondary-names-gpl2.txt|1|SECONDARY|DISCARDED"
has "AG.3 CC 4.0 boilerplate names CC0 -> DOCUMENT-TEXT, discarded" "$AG" "ccby4-legalcode-names-cc0.txt|1|DOCUMENT-TEXT|DISCARDED"
has "AG.4 \`CC BY\` inside \`CC BY-SA 4.0\` -> SUBSTRING, discarded" "$AG" "ccbysa4-not-a-split.txt|1|SUBSTRING|DISCARDED"
# 🔴 The controls assert an EXACT grant set, not non-emptiness. A model
# scored only where it cannot fail scores perfectly and means nothing
# (p124's ACTION AE).
has "AG.5 control MIT file yields exactly MIT"            "$AG" "CTRL|mit-control.txt|MIT"
has "AG.6 control Apache-2.0 file yields exactly Apache"  "$AG" "CTRL|apache2-control.txt|Apache License"
has "AG.7 control BSD-3 file yields exactly BSD-3-Clause" "$AG" "CTRL|bsd3-control.txt|BSD 3-Clause"
# 🔴 p125's own first build read `MIT` inside `LIMITED` and `ISC` inside
# `DISCLAIMED` -- the fifth instance of AG's class, committed inside AG.
hasnt "AG.8 BSD-3 disclaimer does NOT yield MIT (\`LIMITED\`)" "$AG" "bsd3-control.txt|BSD 3-Clause,MIT"
# 🔴 THE FIRST FORM OF THIS ASSERTION WAS `hasnt ... "ISC"` over the whole
# report, and it failed because `DISCARDED` contains `ISC`. The test
# committed, in its own one line, the exact substring error it exists to
# check. The assertion is now scoped to the control's own row.
BSD3_GRANTS=$(printf '%s\n' "$AG" | sed -n 's/^CTRL|bsd3-control.txt|//p')
eq "AG.9 BSD-3 disclaimer yields ONLY BSD-3-Clause (no \`LIMITED\`->MIT, no \`DISCLAIMED\`->ISC)" "$BSD3_GRANTS" "BSD 3-Clause"
# 🔴 AGPL-3's section 13 is a COMPATIBILITY grant over a work being combined
# with this one, and its preamble names the historical Affero GPL to say this
# is NOT it. Five spurious GPL grants from one AGPL file, until the control.
has "AG.10 AGPL-3 control yields no bare GPL grant" "$AG" "CTRL|agpl3-control.txt|AGPL,GNU Affero General Public License"
# A REAL split grant must still produce both tokens.
has "AG.11 real split grant keeps both tokens" "$AG" "CTRL|cc-by-nc-sa-control.txt|CC BY-NC-SA 4.0,MIT"

echo
echo "=== ACTION AH — a bulleted per-file exception list is a sequence of bindings ==="
AH=$(py '
import sys, os
sys.path.insert(0, sys.argv[1]); os.chdir(sys.argv[1])
import bullet_bindings as bb
t = open(os.path.join(sys.argv[2], "anki-perfile-split.txt"),
         encoding="utf-8", errors="replace").read()
print("SET|" + ",".join(sorted(bb.token_set(t))))
print("N|%d" % len([1 for _s,_t,l,_n in bb.bindings(t) if l == "GRANT"]))
for s, tok, lab, _ln in bb.bindings(t):
    print("B|%s|%s|%s" % (s, tok, lab))
' "$HERE" "$FX")
# p124 published `AGPL-3.0 + CC-BY-SA` for `ankitects/anki` and recorded the
# set as PARTIAL. The clause: refuted if fewer than 3 further tokens are
# recovered. Four are.
has "AH.1 anki grant SET is the full six tokens" "$AH" "SET|AGPL-3.0,Apache-2.0,BSD-3-Clause,CC-BY-4.0,CC-BY-SA-4.0,MIT"
eq  "AH.2 seven per-item bindings read from the list" "$(printf '%s' "$AH" | sed -n 's/^N|//p')" "7"
has "AH.3 statsbg.py binds CC-BY-4.0 under pylib/"  "$AH" "B|pylib/statsbg.py|CC-BY-4.0|GRANT"
has "AH.4 MathJax binds Apache-2.0 under qt/"       "$AH" "B|qt/MathJax|Apache-2.0|GRANT"
has "AH.5 protobuf.js binds BSD-3-Clause (no trailing period)" "$AH" "B|qt/protobuf.js|BSD-3-Clause|GRANT"
has "AH.6 jQuery-UI is not split at its own hyphen" "$AH" "B|qt/jQuery and jQuery-UI|MIT|GRANT"
# 🔴 Two licences the file names that are NOT grants over its tree. The
# `AGPL3-compatible license` is a SIXTH instance of AG's class and was not on
# p124's list of four.
hasnt "AH.7 Qt translation files (LGPL) are OUT-OF-TREE, not a grant" "$AH" "SET|AGPL-3.0,Apache-2.0,BSD-3-Clause,CC-BY-4.0,CC-BY-SA-4.0,LGPL"
hasnt "AH.8 \`AGPL3-compatible license\` is a class, not a grant"      "$AH" "|LGPL|GRANT"

echo
echo "=== ACTION AF — one retraction CUE over all thirteen surface forms ==="
AF=$(py '
import sys, os, glob
sys.path.insert(0, sys.argv[1]); os.chdir(sys.argv[1])
import mark_forms as mf
for p in sorted(glob.glob(os.path.join(sys.argv[2], "md-*.md"))):
    n, bf = mf.apply_marks(p, dry=True)
    print("%s|%d|%s" % (os.path.basename(p), n,
                        ",".join("%s=%d" % kv for kv in sorted(bf.items()))))
' "$HERE" "$FX")
has "AF.1  FORM 10 — \`⚠️ was X\` with no emphasis (19 of 61 violations)" "$AF" "md-form10-bare.md|2|1/4/5/10=2"
has "AF.2  FORM 4  — \`⚠️ *was X*\` italic"                               "$AF" "md-form4-italic.md|1|1/4/5/10=1"
has "AF.3  FORM 5  — \`⚠️ **KB said X**\`"                                "$AF" "md-form5-kbsaid.md|2|1/4/5/10=2"
has "AF.4  FORM 6  — reversed \`(New, published Old)\`"                   "$AF" "md-form6-reversed.md|3|"
has "AF.5  FORM 7  — \`as X not Y\`"                                      "$AF" "md-form7-asnot.md|1|7=1"
has "AF.6  FORM 8  — NEW cell holds no licence token"                     "$AF" "md-form8-nogrant.md|3|8=3"
has "AF.7  FORM 11 — prose naming a prior pass's reading"                 "$AF" "md-form11-priorpass.md|2|11=2"
# 🔴 THE THREE NEGATIVE FIXTURES ARE THE POINT. Each removed a whole class
# of false positive from this build's first run.
eq  "AF.8  FORM 13 — a CONTRAST clause is not a correction (AG's gate)" "$(printf '%s' "$AF" | sed -n 's/^md-form13-contrast-not-a-correction.md|\([0-9]*\)|.*/\1/p')" "0"
eq  "AF.9  prose ABOUT the marker is apparatus, not a row"              "$(printf '%s' "$AF" | sed -n 's/^md-apparatus-quoted.md|\([0-9]*\)|.*/\1/p')" "0"
# 🔵 And the boundary case, kept separate because it is a JUDGEMENT rather
# than a rule: *"The stale cell's value was **Apache-2.0**"* is apparatus
# prose AND a retraction -- it names a superseded value in its own voice,
# with the cue unquoted. It is marked, and that is the intended reading.
eq  "AF.9b an unquoted retraction inside apparatus prose IS a row"      "$(printf '%s' "$AF" | sed -n 's/^md-apparatus-boundary.md|\([0-9]*\)|.*/\1/p')" "1"
eq  "AF.10 \`GPL\` -> \`GPL-3.0\` is a RESOLUTION, not a correction"    "$(printf '%s' "$AF" | sed -n 's/^md-resolution-not-correction.md|\([0-9]*\)|.*/\1/p')" "0"
# 🔴 THE SELF-AUDIT, which p124 made part of the method: run the marker over
# the sections the CURRENT pass has just written. p125's own forms table and
# its paragraph on discussion OF the marker produced 8 false positives across
# 4 pages before the apparatus vocabulary was extended.
eq  "AF.10b a page DOCUMENTING the forms is apparatus, not thirteen rows" "$(printf '%s' "$AF" | sed -n 's/^md-apparatus-selfdoc.md|\([0-9]*\)|.*/\1/p')" "0"
# 🔴 A header row must CLEAR the previous table's column mapping. Not doing
# so marked a LIVE licence column on the foundational shelf as superseded.
eq  "AF.11 a correction table's mapping does not outlive its table"     "$(printf '%s' "$AF" | sed -n 's/^md-header-leak.md|\([0-9]*\)|.*/\1/p')" "1"
# 🔴 The marker must land OUTSIDE the emphasis the cue opened, or the span
# it is meant to close reads back as unmarked.
AFP=$(py '
import sys, os, shutil, tempfile
sys.path.insert(0, sys.argv[1]); os.chdir(sys.argv[1])
import mark_forms as mf
d = tempfile.mkdtemp(); p = os.path.join(d, "f.md")
shutil.copy(os.path.join(sys.argv[2], "md-emphasis-placement.md"), p)
mf.apply_marks(p, dry=False)
line = open(p, encoding="utf-8").read()
print("PLACED|" + ("after" if "*was GPL*" + mf.MARKER in line else "inside"))
n2, _ = mf.apply_marks(p, dry=True)
print("IDEMPOTENT|%d" % n2)
import repair_search as rs
print("REREAD|%s" % ("marked" if not rs.violations([p], rs.repaired_pairs([p])) else "unmarked"))
shutil.rmtree(d)
' "$HERE" "$FX")
has "AF.12 marker lands after the closing emphasis, not inside it" "$AFP" "PLACED|after"
has "AF.13 applying the marker is idempotent"                      "$AFP" "IDEMPOTENT|0"
has "AF.14 a marked span reads back as marked"                     "$AFP" "REREAD|marked"

echo
echo "=== ACTION AI — the false-permissive question, over all 86 addresses ==="
# The tier order is the whole content of "more permissive": a lower tier is a
# lower DUTY, which is what makes a false-permissive answer cost money.
AI=$(py '
import sys, os
sys.path.insert(0, sys.argv[1]); os.chdir(sys.argv[1])
import permissiveness as pm
for a, b in [("MIT","GPL-3.0"),("GPL-3.0","MIT"),("AGPL-3.0","Apache-2.0"),
             ("GPL-2.0","GPL-3.0"),("MIT","MIT"),("GPL-3.0","NO-FILE"),
             ("NO-FILE","MIT"),("NO-FILE","NO-FILE"),
             ("Elastic-2.0","Apache-2.0"),("CC-BY-NC-SA-4.0","CC-BY-4.0")]:
    print("CMP|%s|%s|%s" % (a, b, pm.compare(a, b)))
t = open(os.path.join(sys.argv[2], "learnosity-master-mit.txt"),
         encoding="utf-8", errors="replace").read()
print("CLS|master|%s" % pm.classify(t))
t = open(os.path.join(sys.argv[2], "learnosity-develop-gpl2.txt"),
         encoding="utf-8", errors="replace").read()
print("CLS|develop|%s" % pm.classify(t))
' "$HERE" "$FX")
has "AI.1 a guess of MIT for GPL-3.0 code is FALSE-PERMISSIVE"   "$AI" "CMP|GPL-3.0|MIT|FALSE-PERMISSIVE"
has "AI.2 a guess of GPL-3.0 for MIT code is FALSE-RESTRICTIVE"  "$AI" "CMP|MIT|GPL-3.0|FALSE-RESTRICTIVE"
has "AI.3 Apache-2.0 guessed for AGPL-3.0 is FALSE-PERMISSIVE"   "$AI" "CMP|AGPL-3.0|Apache-2.0|FALSE-PERMISSIVE"
has "AI.4 GPL-2.0 vs GPL-3.0 is SAME-TIER, not a permissiveness error" "$AI" "CMP|GPL-2.0|GPL-3.0|SAME-TIER"
has "AI.5 a grant where the real default has none is GUESS-INVENTS-GRANT" "$AI" "CMP|NO-FILE|MIT|GUESS-INVENTS-GRANT"
has "AI.6 no grant on either branch is BOTH-ABSENT, not an error" "$AI" "CMP|NO-FILE|NO-FILE|BOTH-ABSENT"
has "AI.7 Apache-2.0 guessed for Elastic-2.0 is FALSE-PERMISSIVE" "$AI" "CMP|Elastic-2.0|Apache-2.0|FALSE-PERMISSIVE"
has "AI.8 CC-BY-4.0 guessed for a NonCommercial grant is FALSE-PERMISSIVE" "$AI" "CMP|CC-BY-NC-SA-4.0|CC-BY-4.0|FALSE-PERMISSIVE"
# The one address in the corpus where this actually happens, both files read.
has "AI.9  learnosity-qti \`master\` really is MIT"      "$AI" "CLS|master|MIT"
has "AI.10 learnosity-qti \`develop\` really is GPL-2.0" "$AI" "CLS|develop|GPL-2.0"

# The committed verdict table is the evidence for the refutation.
V="$HERE/out/ai-verdict.tsv"
if [ -f "$V" ]; then
  eq "AI.11 verdict table covers all 86 non-standard-default addresses" \
     "$(($(wc -l <"$V") - 1))" "86"
  eq "AI.12 exactly ONE false-permissive address — the clause's refutation" \
     "$(awk -F'\t' '$8=="FALSE-PERMISSIVE"' "$V" | wc -l | tr -d ' ')" "1"
  eq "AI.13 and it is learnosity-qti" \
     "$(awk -F'\t' '$8=="FALSE-PERMISSIVE"{print $1}' "$V")" "Learnosity/learnosity-qti"
  eq "AI.14 no address has a grant invented by a guess" \
     "$(awk -F'\t' '$8=="GUESS-INVENTS-GRANT"' "$V" | wc -l | tr -d ' ')" "0"
  eq "AI.15 77 of 86 agree" \
     "$(awk -F'\t' '$8=="AGREE"' "$V" | wc -l | tr -d ' ')" "77"
fi

# ACTION AF's score against its clause, from the committed triples.
B="$HERE/out/ac-baseline.triples"; A="$HERE/out/ac-after.triples"
if [ -f "$B" ] && [ -f "$A" ]; then
  eq "AF.15 baseline is 61 ACTION AC violations over the ten live pages" \
     "$(wc -l <"$B" | tr -d ' ')" "61"
  eq "AF.16 40 of the 61 resolved — the clause required 20" \
     "$(comm -23 "$B" "$A" | wc -l | tr -d ' ')" "40"
fi

echo
printf '\033[1m%d passed / %d failed\033[0m\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ]
