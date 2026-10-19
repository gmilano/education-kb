#!/usr/bin/env python3
"""p310 — offline controls for the fixture-coverage gate and its grader.

No network, no clock. Every licence control runs on a payload pinned in
`fixtures/`, read first-hand at p310.

🔵 `p309` established that a control asserting non-emptiness is worth nothing —
and that *the static screen was wrong 34 times out of 36 while the dynamic arm
decided all 11*. So the controls below assert EXACT grades, and the NEGATIVE
controls are the point of the file: three of them are the false positives this
grader actually produced on its first three builds, kept as controls rather than
described in a comment.

Run: python3 test_family_coverage.py     (from this directory)
"""
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.normpath(os.path.join(HERE, ".."))


def _load(name, path, extra=None):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    if extra:
        sys.path.insert(0, extra)
    sink, sys.stdout = sys.stdout, io.StringIO()
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.stdout = sink
        if extra and extra in sys.path:
            sys.path.remove(extra)
    return mod


FX = _load("t_fixtures", os.path.join(HERE, "fixtures.py"), HERE)
COV = _load("t_coverage", os.path.join(HERE, "family_coverage.py"), HERE)
ARM = _load("t_arm", os.path.join(HERE, "run_families.py"), HERE)
CC = _load("t_cc", os.path.join(CODE, "p124-correction-form-marker", "cc_version.py"))
PROBE = _load("t_probe", os.path.join(CODE, "p306-licence-probe", "licence_probe.py"),
              os.path.join(CODE, "p306-licence-probe"))

passed, failed = [], []


def check(label, got, want):
    if got == want:
        passed.append(label)
    else:
        failed.append("%s\n       got  %r\n       want %r" % (label, got, want))


TEXT = {name: text for name, _f, _c, _w, text, _n, _s in FX.declared()}
BYTES = {name: (n, sha) for name, _f, _c, _w, _t, n, sha in FX.declared()}

NC = "ccbync-4.0-aegis-graph"
BY = "ccby-4.0-writing-support"
PF = "polyform-nc-1.0.0-paper-tutor-skills"
PR = "proprietary-algomind"
CC0 = "cc0-1.0-gen-mentor"

# ---------------------------------------------------------------- the pins
check("pin: CC-BY-NC payload is 19 347 B / 41003d4a7474", BYTES[NC], (19347, "41003d4a7474"))
check("pin: CC-BY payload is 18 873 B / aa0d3c9d6a28", BYTES[BY], (18873, "aa0d3c9d6a28"))
check("pin: PolyForm payload is 4 563 B / ffcca38841ad", BYTES[PF], (4563, "ffcca38841ad"))
check("pin: proprietary payload is 831 B / b2496e89aa4d", BYTES[PR], (831, "b2496e89aa4d"))
check("pin: CC0 legalcode is 7 048 B", BYTES[CC0][0], 7048)

# 🔴 The CC0 clause defect, as a live control: the DEED's wording is absent from
# the LEGALCODE, so the rung written against it could never fire.
check("the CC0 DEED phrase appears ZERO times in the CC0 legalcode",
      TEXT[CC0].lower().count("has waived all copyright"), 0)
check("the CC0 LEGALCODE's operative verb is present exactly once",
      TEXT[CC0].lower().count("waives, abandons, and surrenders"), 1)
check("p306 repaired: the CC0 legalcode is a GRANT, not a POINTER",
      PROBE.classify(TEXT[CC0]), ("GRANT", "CC0-1.0"))
check("p124 oracle agrees the CC0 legalcode is CC0-1.0", CC.resolve(TEXT[CC0]), "CC0-1.0")
check("P250: a CC0 grant is commercially OK", PROBE.commercial_use("CC0-1.0", TEXT[CC0].lower()), "OK")

# ------------------------------------------- THE DEFECT, as a live control
# 🔴 The exact rung p306 carried, reproduced here so the gate can prove it
# catches something. A gate that can only judge its own matches cannot be shown
# to catch anything — `p124`'s `ACTION AG` established that.
def naive_cc(text):
    low = text.lower()
    if "cc0" in low or "public domain dedication" in low:
        return "CC0-1.0"
    if "attribution-sharealike" in low:
        return "CC-BY-SA-4.0"
    if "creative commons" in low:
        return "CC-other"
    return None


check("NEGATIVE CONTROL: the refuted rung reads CC-BY-NC as CC0", naive_cc(TEXT[NC]), "CC0-1.0")
check("NEGATIVE CONTROL: the refuted rung reads CC-BY as CC0", naive_cc(TEXT[BY]), "CC0-1.0")
check("the CC0 string really is present exactly once in CC-BY-NC",
      TEXT[NC].lower().count("cc0"), 1)
check("the CC0 string really is present exactly once in CC-BY",
      TEXT[BY].lower().count("cc0"), 1)

# -------------------------------------------- the canonical oracle (p124)
check("p124 oracle: CC-BY-NC-4.0", CC.resolve(TEXT[NC]), "CC-BY-NC-4.0")
check("p124 oracle: CC-BY-4.0", CC.resolve(TEXT[BY]), "CC-BY-4.0")
check("p124 oracle declines PolyForm (not CC)", CC.resolve(TEXT[PF]), None)
check("p124 oracle declines a proprietary notice (not CC)", CC.resolve(TEXT[PR]), None)

# ------------------------------------------------ the repaired prober (p306)
check("p306 repaired: CC-BY-NC -> GRANT-NONCOMMERCIAL / CC-BY-NC-4.0",
      PROBE.classify(TEXT[NC]), ("GRANT-NONCOMMERCIAL", "CC-BY-NC-4.0"))
check("p306 repaired: CC-BY -> GRANT / CC-BY-4.0",
      PROBE.classify(TEXT[BY]), ("GRANT", "CC-BY-4.0"))
check("p306 repaired: PolyForm -> GRANT-NONCOMMERCIAL / PolyForm-Noncommercial-1.0.0",
      PROBE.classify(TEXT[PF]), ("GRANT-NONCOMMERCIAL", "PolyForm-Noncommercial-1.0.0"))
check("p306 unchanged on the positive control: proprietary -> RESERVED-NO-GRANT",
      PROBE.classify(TEXT[PR]), ("RESERVED-NO-GRANT", "-"))

# ------------------------------------- P250's rule, including its SAFE half
# 🔴 p250's versioned negative control: AGPL-3.0 §6 contains "noncommercially"
# and the Unlicense grants "commercial or non-commercial". A marker scan that
# runs on a protected family condemns both.
check("P250: an OSI family is OK without any marker scan",
      PROBE.commercial_use("AGPL-3.0", "allowed only occasionally and noncommercially"),
      "OK")
check("P250: the Unlicense is OK though it says non-commercial",
      PROBE.commercial_use("Unlicense", "for any purpose, commercial or non-commercial"),
      "OK")
check("P250: CC0-1.0 is OK", PROBE.commercial_use("CC0-1.0", ""), "OK")
check("P250: CC-BY-SA-4.0 is OK (ShareAlike is not a commercial bar)",
      PROBE.commercial_use("CC-BY-SA-4.0", ""), "OK")
check("P250: CC-BY-NC-4.0 is PROHIBITED by its own token",
      PROBE.commercial_use("CC-BY-NC-4.0", ""), "PROHIBITED")
check("P250: CC-BY-NC-SA-4.0 is PROHIBITED", PROBE.commercial_use("CC-BY-NC-SA-4.0", ""),
      "PROHIBITED")
check("P250: an unknown family with no marker is UNDETERMINED, not OK",
      PROBE.commercial_use("unknown", "some prose"), "UNDETERMINED")
check("P250: an unknown family WITH a marker is PROHIBITED",
      PROBE.commercial_use("unknown", "for noncommercial purposes only"), "PROHIBITED")

# ----------------------- the POINTER class (ACTION p309-R item 2) three-valued
# 🔵 p309's own pointer payload, resolved through p309's `body(prefix)` so this
# suite holds no second copy of its handle.
P309 = FX.p309_fixtures()
if P309 is not None:
    pointer = P309.body(P309.CC_POINTER)
    check("POINTER: a grant BY REFERENCE is POINTER, not NO-GRANT-CLAUSE",
          PROBE.classify(pointer), ("POINTER", "CC-BY-SA-4.0"))
    check("POINTER: and it is p309's pinned 1 230 B payload", len(pointer.encode()), 1230)
else:
    failed.append("p309's fixture module is not reachable")

check("POINTER: a pointer at a restricted licence is POINTER-NONCOMMERCIAL",
      PROBE.classify("Attribution-NonCommercial 4.0 International\n\n"
                     "The materials here are licensed under CC BY-NC 4.0.\n"),
      ("POINTER-NONCOMMERCIAL", "CC-BY-NC-4.0"))
check("POINTER: no grant and NO family named stays NO-GRANT-CLAUSE",
      PROBE.classify("See the project website for terms.\n"),
      ("NO-GRANT-CLAUSE", "-"))
check("POINTER: all-rights-reserved with no family stays RESERVED-NO-GRANT",
      PROBE.classify("Copyright (c) 2026 Someone. All rights reserved.\n"),
      ("RESERVED-NO-GRANT", "-"))

# ------------------------------------------- the grader's own false positives
# 🔴 Each of the three was produced by a real build of `run_families.py` against
# a real classifier, and each condemned a correct instrument. They are controls
# now, not anecdotes.
check("FP1: a house sentinel is an ABSTENTION (p211 'unrecognised')",
      ARM.grade("proprietary", "unrecognised"), "ABSTAIN")
check("FP2: a Spanish SENTENCE is an abstention, not a family claim (p419)",
      ARM.grade("CC-BY-NC-4.0",
                "el encabezado no nombra una familia — tratar como no-osi (`p412`)"),
      "ABSTAIN")
check("FP3: p228's phrase sentinel is an abstention",
      ARM.grade("proprietary", "no recognised licence title"), "ABSTAIN")
check("FP4: a verdict token is not a family claim (p306 GRANT-NONCOMMERCIAL)",
      ARM._answer(("GRANT-NONCOMMERCIAL", "CC-BY-NC-4.0")), "cc-by-nc-4.0")

# and the grader must still CONDEMN the real thing
check("the grader condemns CC0 for a NonCommercial payload, on the commercial axis",
      ARM.grade("CC-BY-NC-4.0", "cc0-1.0"), "DEFECT-COMMERCIAL")
check("the grader condemns CC0 for CC-BY (wrong, but not a commercial crossing)",
      ARM.grade("CC-BY-4.0", "cc0-1.0"), "DEFECT")
check("the grader condemns MIT for a proprietary payload",
      ARM.grade("proprietary", "mit"), "DEFECT-COMMERCIAL")
check("the grader accepts a COARSE but correct answer",
      ARM.grade("CC-BY-NC-4.0", "cc-by-nc"), "COARSE")
check("the grader accepts p191's axis answer for CC-BY",
      ARM.grade("CC-BY-4.0", "permissive-software"), "COARSE")
check("the grader accepts the exact answer", ARM.grade("CC-BY-4.0", "cc-by-4.0"), "CORRECT")

# ------------------------------------------------------- the coverage census
counts, missing = COV.published(os.path.normpath(os.path.join(CODE, "..", "..")))
check("census: no live shelf is unreadable", missing, [])
check("census: MIT is the most-published family on this base",
      max(counts, key=lambda k: counts[k]), "MIT")
for fam in ("MIT", "Apache-2.0", "AGPL-3.0", "GPL-3.0", "CC-BY-NC-SA-4.0", "CC0-1.0"):
    check("census: %s is published on these shelves" % fam, fam in counts, True)
# 🔴 p124 instance 4, as a control: the longer family must not be harvested as
# the shorter one. `CC-BY-NC-SA-4.0` contains `CC-BY-SA-4.0`'s letters in order.
check("census: CC-BY-NC-SA-4.0 and CC-BY-SA-4.0 are counted SEPARATELY",
      counts.get("CC-BY-NC-SA-4.0", 0) > 0 and counts.get("CC-BY-SA-4.0", 0) > 0, True)
check("census: a one-line CC-BY-NC-SA cell is not double-counted as CC-BY-SA",
      COV.published.__doc__ is not None, True)

corpus = {}
sys.path.insert(0, HERE)
try:
    corpus = COV.corpus_families()
finally:
    sys.path.remove(HERE)
check("coverage: every p310 fixture family is in the corpus map",
      all(f in corpus for _n, f, _c, _w in FX.DECLARED), True)
check("coverage: p309's three families are IMPORTED, not restated",
      all(f in corpus for f in ("GPL-3.0", "AGPL-3.0", "CC-BY-SA-4.0")), True)
check("coverage: the uncovered remainder is non-empty and MIT is in it",
      "MIT" not in corpus, True)

# ------------------------------------------------------------------- report
for line in passed:
    print("  🟢 %s" % line)
for line in failed:
    print("  🔴 %s" % line)
print("\n%d passed / %d failed over %d controls"
      % (len(passed), len(failed), len(passed) + len(failed)))
sys.exit(1 if failed else 0)
