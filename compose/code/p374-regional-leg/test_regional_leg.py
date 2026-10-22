#!/usr/bin/env python3
"""Controls for `p374-regional-leg`.  OFFLINE.  Run from inside this directory (`p355`'s class).

🟢 `p305`'s standing demand: a new standing rule is run over this base's OWN corpus before it
is published.  Group A does exactly that — the ten legs in `legs.tsv` are this base's real
recorded legs, not fixtures.  Groups B-F are the controls, and groups C and F are the NEGATIVE
controls: each one must turn a specific invariant RED.
"""
import copy
import os
import sys

#: 🔴 `p355-cwd-portability` / the Makefile's own header: `-I` strips the script's directory
#: from `sys.path`, so this suite dies on import when a hook invokes it even WITH a `cd`.
#: Every sibling instrument here carries this same two lines; without them a working gate
#: stays a one-off that cannot be invoked from the place a hook runs.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from regional_leg import (  # noqa: E402
    REGIONS, names_a_jurisdiction, nil_is_admissible, nil_limbs,
    redundancy_is_admissible, region_is_in_vocabulary, verdict_is_consistent,
)
from regional_leg_gate import load_legs, run  # noqa: E402

FAILURES = []
#: 🔴 Derived, never asserted. `p274`'s `recount` exists because this base published counts it
#: could not re-derive; a suite that hardcodes its own control total is the same defect in
#: miniature. `GROUPS` is derived too, so adding a group cannot leave the banner stale.
RAN = []


def check(group, name, got, want):
    RAN.append(group)
    if got != want:
        FAILURES.append("%s / %s: got %r, want %r" % (group, name, got, want))


# ── A. the real corpus.  The gate is green on this base's own ten recorded legs.
LEGS = load_legs()
failures, counts = run(LEGS)
check("A", "the ten committed legs pass every invariant", failures, [])
check("A", "ten legs loaded", len(LEGS), 10)
check("A", "J2 fires on exactly the two NIL legs", counts["J2"], 2)
check("A", "J3 checks the one published redundancy claim", counts["J3"], 1)

# ── B. J2 limb 1 — a region label is not a jurisdiction.
check("B", "'EMEA' alone names no jurisdiction", names_a_jurisdiction(["EMEA"]), False)
check("B", "'LATAM' alone names no jurisdiction", names_a_jurisdiction(["LATAM"]), False)
check("B", "'Europe' alone names no jurisdiction", names_a_jurisdiction(["Europe"]), False)
check("B", "several region labels still name none",
      names_a_jurisdiction(["EMEA", "Global", "Asia-Pacific"]), False)
check("B", "a country names one", names_a_jurisdiction(["Germany"]), True)
check("B", "an organ alone names one", names_a_jurisdiction(["KMK"]), True)
check("B", "an organ in its own script names one", names_a_jurisdiction(["文部科学省"]), True)
check("B", "a region label PLUS a country names one",
      names_a_jurisdiction(["EMEA", "Germany"]), True)
check("B", "empty names none", names_a_jurisdiction([]), False)
check("B", "whitespace names none", names_a_jurisdiction(["  ", ""]), False)

# ── C. NEGATIVE CONTROL 1 — `p373` cell 1, un-withdrawn, must turn J2 red.
#    🔴 This is the control that matters.  `p373` said `I4` "would pass" cell 1.  It did.
unwithdrawn = copy.deepcopy(LEGS)
for leg in unwithdrawn:
    if leg["leg_id"] == "p373-c1":
        leg["nil_disposition"] = "PUBLISHED"
f2, _ = run(unwithdrawn)
check("C", "un-withdrawing p373-c1 turns J2 RED", [f[0] for f in f2], ["J2"])
check("C", "and it is limb 1 that refuses it",
      "LIMB-1" in f2[0][2] if f2 else False, True)
check("C", "I4's one-limb test, by contrast, PASSES cell 1 — the defect p373 named",
      nil_limbs({"verdict": "NIL", "jurisdiction": "Germany", "language": "German",
                 "placenames": ["EMEA"]},
                [{"jurisdiction": "Germany", "language": "English"}])[0], False)

# ── D. J2 limb 2 — a nil with no sibling leg in another language.
lonely = {"verdict": "NIL", "jurisdiction": "Chile", "language": "English",
          "placenames": ["Chile", "MINEDUC"], "nil_disposition": "PUBLISHED"}
check("D", "a jurisdiction-naming nil with no in-language sibling is refused",
      nil_is_admissible(lonely, [lonely])[0], False)
check("D", "and the reason is limb 2", "LIMB-2" in nil_is_admissible(lonely, [lonely])[1], True)
with_sibling = [lonely, {"jurisdiction": "Chile", "language": "Spanish",
                         "verdict": "PRODUCTIVE", "placenames": ["Chile"]}]
check("D", "adding a Spanish leg admits it", nil_is_admissible(lonely, with_sibling)[0], True)
check("D", "a sibling in the SAME language does not count",
      nil_is_admissible(lonely, [lonely, {"jurisdiction": "Chile", "language": "English",
                                          "verdict": "PRODUCTIVE",
                                          "placenames": ["Chile"]}])[0], False)
check("D", "a sibling for ANOTHER jurisdiction does not count",
      nil_is_admissible(lonely, [lonely, {"jurisdiction": "Peru", "language": "Spanish",
                                          "verdict": "PRODUCTIVE",
                                          "placenames": ["Peru"]}])[0], False)

# ── E. J2 over-firing — the half `I4` got wrong in the OTHER direction.
#    🟢 Brazil's English leg is PRODUCTIVE, so J2 never asks it for a Portuguese sibling at all.
brazil_en = [l for l in LEGS if l["leg_id"] == "p374-r3"][0]
check("E", "J2 does not touch a productive leg", nil_is_admissible(brazil_en, LEGS)[0], True)
check("E", "and says so explicitly", nil_is_admissible(brazil_en, LEGS)[1], "not-a-nil")

# ── F. J3 — "redundant" needs a fact-class test.  NEGATIVE CONTROL 2 is the Japan row.
check("F", "Portuguese IS redundant for Brazil — both productive, same fact class",
      redundancy_is_admissible("Brazil", "Portuguese", LEGS)[0], True)
check("F", "🔴 Japanese is NOT redundant for Japan — the fact classes differ",
      redundancy_is_admissible("Japan", "Japanese", LEGS)[0], False)
check("F", "and the refusal names the fact classes",
      "DIFFERENT fact classes" in redundancy_is_admissible("Japan", "Japanese", LEGS)[1], True)
check("F", "English is not redundant for Japan either, symmetrically",
      redundancy_is_admissible("Japan", "English", LEGS)[0], False)
check("F", "redundancy cannot be claimed before both legs run",
      redundancy_is_admissible("India", "Hindi", LEGS)[0], False)
check("F", "a NIL leg is necessity, not redundancy",
      redundancy_is_admissible("Germany", "German", LEGS)[0], False)

# ── G. J1 — the closed vocabulary, compared literally.
check("G", "five values exactly", len(REGIONS), 5)
for good in REGIONS:
    check("G", "%r admitted" % good, region_is_in_vocabulary(good), True)
for bad in ("Latam", "LatAm", "latam", "Europe", "Brazil", "APAC ", "", "Asia"):
    check("G", "%r refused" % bad, region_is_in_vocabulary(bad), False)

# ── H. J4 — a verdict agrees with its own fact count.
check("H", "a NIL with facts is refused",
      verdict_is_consistent({"verdict": "NIL", "fact_count": 3})[0], False)
check("H", "a NIL with none is fine",
      verdict_is_consistent({"verdict": "NIL", "fact_count": 0})[0], True)
check("H", "a PRODUCTIVE with none is refused",
      verdict_is_consistent({"verdict": "PRODUCTIVE", "fact_count": 0})[0], False)
check("H", "a PARTIAL with one is fine — p374's R2",
      verdict_is_consistent({"verdict": "PARTIAL", "fact_count": 1})[0], True)
check("H", "an unknown verdict is refused",
      verdict_is_consistent({"verdict": "MAYBE", "fact_count": 1})[0], False)

# ── I. the disposition limb cannot be used to hide a SOUND nil.
sound_but_withdrawn = copy.deepcopy(LEGS)
for leg in sound_but_withdrawn:
    if leg["leg_id"] == "p373-c2":
        leg["nil_disposition"] = "WITHDRAWN-p374"
f3, _ = run(sound_but_withdrawn)
check("I", "retracting a SOUND nil turns J2 red too", [f[0] for f in f3], ["J2"])
check("I", "the disposition limb is symmetric, not an escape hatch",
      "may not be retracted silently" in f3[0][2] if f3 else False, True)

TOTAL = len(RAN)
GROUPS = len(set(RAN))
if FAILURES:
    print("🔴 FAIL — %d of %d controls" % (len(FAILURES), TOTAL))
    for f in FAILURES:
        print("   %s" % f)
    sys.exit(1)
print("🟢 PASS — %d controls over %d groups "
      "(p373 cell 1 un-withdrawn turns J2 red; I4 passes the same cell; "
      "Japan refuses the redundancy claim p373 generalised; "
      "retracting a sound nil is refused symmetrically)" % (TOTAL, GROUPS))
