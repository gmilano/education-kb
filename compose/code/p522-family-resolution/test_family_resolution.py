"""Offline suite for family_resolution. No network.

    cd compose/code/p522-family-resolution && python3 test_family_resolution.py

Every fixture is a payload read from `raw.githubusercontent.com` on 2026-10-29; the exact
slug, served path and byte count are in fixtures/PROVENANCE.tsv. The two positive controls
are p521's fixtures, referenced rather than copied — if that pass's fixtures move, this
suite fails loudly instead of silently testing nothing.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import family_resolution as fr                                      # noqa: E402

FIX = os.path.join(HERE, "fixtures")
P521_FIX = os.path.join(HERE, os.pardir, "p521-commercial-posture", "fixtures")

CHECKS = []


def check(name, got, want):
    CHECKS.append((name, got == want, got, want))


def payload(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def fixture(name):
    return payload(os.path.join(FIX, name))


# --------------------------------------------------------------------------------------
# 1. FAMILY RESOLUTION — the two cells p521 gets wrong, and five it gets right
# --------------------------------------------------------------------------------------
CASES = [
    # fixture                                          family            posture
    ("cc0-1.0.gen-mentor.LICENSE.txt",                 "CC0-1.0",        "PUBLIC-DOMAIN"),
    ("gpl-2.0.i-educar.LICENSE.txt",                   "GPL-2.0",        "COPYLEFT"),
    ("gpl-3.0.lumen.LICENSE.txt",                      "GPL-3.0",        "COPYLEFT"),
    ("agpl-3.0.freelingo.LICENSE.txt",                 "AGPL-3.0",       "COPYLEFT"),
    ("apache-2.0.feedbacksystem.LICENSE.txt",          "Apache-2.0",     "PERMISSIVE"),
    ("mit.mentingo.LICENSE.txt",                       "MIT",            "PERMISSIVE"),
    ("cc-by-sa-4.0.education-agent-skills.LICENSE.txt", "CC-BY-SA-4.0",  "WEAK-COPYLEFT"),
]

for fx, want_fam, want_posture in CASES:
    fam, posture, _ = fr.resolve(fixture(fx))
    check("family   %-48s" % fx, fam, want_fam)
    check("posture  %-48s" % fx, posture, want_posture)

# --------------------------------------------------------------------------------------
# 2. POSITIVE CONTROLS — p520 refused these two BY HAND; p521's fixtures, this instrument
# --------------------------------------------------------------------------------------
pagelm = payload(os.path.join(P521_FIX, "pagelm.LICENSE.md.txt"))
cnmath = payload(os.path.join(P521_FIX, "cn-math-taxonomy.LICENSE.txt"))

fam, posture, _ = fr.resolve(pagelm)
check("positive control PageLM is refused", posture, "BESPOKE-RESTRICTED")
check("positive control PageLM not buildable", fr.buildable_in_paid_engagement(pagelm)[0], False)

fam, posture, _ = fr.resolve(cnmath)
check("positive control cn-math family", fam, "CC-BY-NC-4.0")
check("positive control cn-math is refused", posture, "NON-COMMERCIAL")
check("positive control cn-math not buildable",
      fr.buildable_in_paid_engagement(cnmath)[0], False)

# --------------------------------------------------------------------------------------
# 3. NEGATIVE CONTROLS — the four permissive payloads a boundary-less scan flags.
#    Each assertion names the exact word that would have caused the false refusal.
# --------------------------------------------------------------------------------------
TRAPS = [
    ("apache-2.0.feedbacksystem.LICENSE.txt",  "irrevocable",    True),
    ("cc0-1.0.gen-mentor.LICENSE.txt",         "irrevocable",    True),
    ("gpl-3.0.lumen.LICENSE.txt",              "noncommercially", True),
    ("agpl-3.0.freelingo.LICENSE.txt",         "noncommercially", True),
]

for fx, word, present in TRAPS:
    text = fixture(fx)
    hits = [w for _, w, _ in fr.guard_hits(text)]
    check("trap present   %-42s %s" % (fx, word), word in hits, present)
    # the trap is present AND the verdict stays buildable — that is the whole point
    check("trap harmless  %-42s" % fx, fr.buildable_in_paid_engagement(text)[0], True)

# --------------------------------------------------------------------------------------
# 3b. THE CC0 BOILERPLATE TRAP — Creative Commons prints a CC0 dedication sentence in the
#     boilerplate of EVERY 4.0 payload. It dedicates the LICENCE TEXT, not the work.
#     p522's own first draft read cn-math-taxonomy (CC BY-NC) as CC0-1.0 / PUBLIC-DOMAIN
#     because of it, which would have passed an asset p520 refused by hand.
# --------------------------------------------------------------------------------------
# As served the sentence is wrapped across lines, so the presence check normalises
# whitespace — the same reason CC_TEXT_DEDICATION is joined on `\s+`.
check("the boilerplate sentence IS in the CC BY-NC payload",
      "CC0 Public Domain Dedication" in " ".join(cnmath.split()), True)
check("...and the strip removes it",
      "cc0 public domain dedication" in
      " ".join(fr.CC_TEXT_DEDICATION.sub(" ", cnmath).split()).lower(), False)
check("...and it does NOT win over the -NC element", fr.resolve(cnmath)[0], "CC-BY-NC-4.0")

ccby_with_boilerplate = (
    "Attribution 4.0 International\n"
    "=======================================================================\n"
    "Creative Commons Corporation is not a law firm.\n"
    "Using Creative Commons Public Licenses: the text of the Creative Commons public "
    "licenses is dedicated to the public domain under the CC0 Public Domain Dedication.\n"
    "Section 1 - Definitions.")
check("CC-BY 4.0 + boilerplate stays CC-BY-4.0",
      fr.resolve(ccby_with_boilerplate)[0], "CC-BY-4.0")

# Where two elements appear, the restrictive one must win.
both = ("Creative Commons Legal Code\nCC0 1.0 Universal\n"
        "...this work is additionally offered under Attribution-NonCommercial 4.0.")
check("two CC elements: restrictive wins", fr.resolve(both)[1], "NON-COMMERCIAL")

# --------------------------------------------------------------------------------------
# 4. SYNTHETIC EDGE CASES
# --------------------------------------------------------------------------------------
check("empty payload", fr.resolve("")[1], "UNKNOWN")
check("whitespace payload", fr.resolve("   \n  \n")[1], "UNKNOWN")

# A GNU title with NO version line must say so rather than guess a version.
fam, posture, ev = fr.resolve("GNU GENERAL PUBLIC LICENSE\n\nsome text with no version line")
check("GNU without version is explicit", fam, "GPL-?")
check("GNU without version says why", any("NO version line" in e for e in ev), True)

# The MIT incipit with a restriction below it is still refused (p521's defect class).
camouflage = ("Permission is hereby granted, free of charge, to any person obtaining a copy "
              "of this software...\n\nThis software may not be used for commercial purposes "
              "without a revenue share agreement.")
check("MIT incipit + restriction is refused", fr.resolve(camouflage)[1], "BESPOKE-RESTRICTED")

# BSD-3's no-endorsement clause contains "prior written permission" and must NOT downgrade.
bsd3 = ("Redistribution and use in source and binary forms, with or without modification, "
        "are permitted provided that the following conditions are met:\n"
        "Neither the name of the copyright holder nor the names of its contributors may be "
        "used to endorse or promote products derived from this software without specific "
        "prior written permission.")
check("BSD-3 no-endorsement is not a gate", fr.resolve(bsd3), ("BSD-3-Clause", "PERMISSIVE",
      ["BSD incipit", "no-endorsement clause is not a gate"]))

# --------------------------------------------------------------------------------------
# 5. THE DISAGREEMENT, ASSERTED AS A TEST SO IT CANNOT ROT
#    When a later pass fixes commercial_posture, these two flip to None and the patch in
#    family_resolution can be retired. Until then they document a live divergence.
# --------------------------------------------------------------------------------------
check("p521 disagrees on CC0 (CC-BY)",
      fr.disagreement_with_p521(fixture("cc0-1.0.gen-mentor.LICENSE.txt")),
      ("CC0-1.0", "CC-BY"))
check("p521 disagrees on GPL-2.0 (bare GPL)",
      fr.disagreement_with_p521(fixture("gpl-2.0.i-educar.LICENSE.txt")),
      ("GPL-2.0", "GPL"))
check("p521 AGREES on Apache-2.0",
      fr.disagreement_with_p521(fixture("apache-2.0.feedbacksystem.LICENSE.txt")), None)
check("p521 AGREES on MIT",
      fr.disagreement_with_p521(fixture("mit.mentingo.LICENSE.txt")), None)

# --------------------------------------------------------------------------------------
if __name__ == "__main__":
    bad = [c for c in CHECKS if not c[1]]
    for name, ok, got, want in CHECKS:
        print("%s  %s" % ("PASS" if ok else "FAIL", name.strip()))
        if not ok:
            print("        got  %r\n        want %r" % (got, want))
    print("\n%d/%d checks pass" % (len(CHECKS) - len(bad), len(CHECKS)))
    sys.exit(1 if bad else 0)
