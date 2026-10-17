#!/usr/bin/env python3
"""Controls for p278's direction classifier.

THE FIXTURES ARE NOT INVENTED.  Rows 1-10 are `p121`'s own measured contradiction table from
`repos/trending.md`, re-expressed as (manifest, payload) -> expected verdict.  A classifier
that cannot reproduce the hand-written table it replaces has not replaced it.

`p252`'s census pins the floor count of every suite on this base, so the floor is asserted
here rather than left implicit -- a suite that silently runs zero controls passes vacuously,
which is the defect `ACTION XR` exists for.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direction import direction, tier_of  # noqa: E402

FAILED = []
RAN = 0


def check(label, got, want):
    global RAN
    RAN += 1
    if got != want:
        FAILED.append(f"FAIL {label}:\n     got  {got}\n     want {want}")


def verdict(m, p):
    return direction(m, p)[0]


def severity(m, p):
    return direction(m, p)[1]


# ---------------------------------------------------------------- p121's ten, reproduced
# Each line is: manifest says, committed file says, p121's published direction.
P121 = [
    ("leemonade/leemons",                      "MIT",  "FAIR-CODE",     "MANIFEST-OVERSTATES"),
    ("classroomio/classroomio",                "MIT",  "AGPL-3.0",      "MANIFEST-OVERSTATES"),
    ("codelitdev/courselit",                   "MIT",  "AGPL-3.0",      "MANIFEST-OVERSTATES"),
    ("tadreeb-lms/tadreeblms",                 "MIT",  "AGPL-3.0",      "MANIFEST-OVERSTATES"),
    ("LearnPress/learnpress",                  "ISC",  "GPL-3.0",       "MANIFEST-OVERSTATES"),
    ("cccareers/open-source-curriculum",       "MIT",  "CC-BY-NC-SA-4.0", "MANIFEST-OVERSTATES"),
    ("Gnanakamalesh-M/student-dropout-early-warning", "MIT", "NONE",    "MANIFEST-OVERSTATES"),
    ("Open-TutorAi/open-tutor-ai-CE",          "MIT",  "BSD-3-Clause",  "SAME-TIER-WRONG-NAME"),
    ("codeXsidd/Studivexa",                    "ISC",  "MIT",           "SAME-TIER-WRONG-NAME"),
    ("nextcloud/llm2",                         "AGPL-3.0", "MIT",       "MANIFEST-UNDERSTATES"),
]
for slug, m, p, want in P121:
    check(f"p121 row {slug} ({m} manifest / {p} payload)", verdict(m, p), want)

# 🔴 The asymmetry p121 measured, asserted as a property of the classifier rather than of the
# sample: 7 of its 10 are the dangerous direction and exactly 1 is the harmless one.
reds = [s for s, m, p, _ in P121 if severity(m, p) == "RED"]
check("p121's measured asymmetry: 7 of 10 rows bill", len(reds), 7)
check("p121's measured asymmetry: exactly 1 harmless direction",
      len([1 for s, m, p, _ in P121 if verdict(m, p) == "MANIFEST-UNDERSTATES"]), 1)
check("p121's measured asymmetry: exactly 2 same-tier",
      len([1 for s, m, p, _ in P121 if verdict(m, p) == "SAME-TIER-WRONG-NAME"]), 2)

# ---------------------------------------------------------------- the negative arms
# A channel that was not read is NOT agreement.  This is the arm that makes the instrument
# honest, so it is asserted in every shape an unread channel arrives in.
for unread in ("", "-", "UNREAD", "NOT-READ", "404", "ABSENT-AT-ADDRESS"):
    check(f"unread manifest ({unread!r}) is SINGLE-CHANNEL, never AGREE",
          verdict(unread, "MIT"), "SINGLE-CHANNEL-PAYLOAD")
    check(f"unread payload ({unread!r}) is SINGLE-CHANNEL, never AGREE",
          verdict("MIT", unread), "SINGLE-CHANNEL-MANIFEST")
    check(f"unread payload ({unread!r}) is never GREEN", severity("MIT", unread), "GREY")
check("both channels unread is NO-CHANNEL", verdict("", ""), "NO-CHANNEL")
check("both channels unread is not a conflict claim", severity("", ""), "GREY")

# ---------------------------------------------------------------- agreement
check("identical families AGREE", verdict("MIT", "MIT"), "AGREE")
check("identical families are GREEN", severity("MIT", "MIT"), "GREEN")
check("Apache-2.0 agreeing with itself", verdict("Apache-2.0", "Apache-2.0"), "AGREE")

# ---------------------------------------------------------------- tier placement
# ECL-2.0 is Apache-2.0-derived and governs Sakai AND Opencast on this base's shelves.
# Misfiling it as copyleft would mis-grade two of the largest platforms here, so it is pinned.
check("ECL-2.0 is permissive (Sakai + Opencast)", tier_of("ECL-2.0"), 0)
check("ECL-2.0 agreeing with MIT is same-tier, not a danger",
      severity("MIT", "ECL-2.0"), "YELLOW")
# `-or-later` and other suffixes normalise onto the base family.
check("GPL-3.0-or-later places on the GPL tier", tier_of("GPL-3.0-or-later"), 3)
check("AGPL-3.0-only places on the network-copyleft tier", tier_of("AGPL-3.0-only"), 4)
check("BSD-3-Clause is permissive", tier_of("BSD-3-Clause"), 0)
check("CC-BY-NC-4.0 is NOT permissive — p276's P-N1", tier_of("CC-BY-NC-4.0"), 5)
check("BUSL-1.1 is NOT permissive (sdv-dev/SDV's grant)", tier_of("BUSL-1.1"), 5)
check("NONE sits with proprietary, not with permissive", tier_of("NONE"), 5)
# An unplaceable family must NOT silently pass as permissive.
check("an unknown family is unplaceable", tier_of("Hypothetical-Bespoke-1.0"), None)
check("an unplaceable family is GREY, never GREEN",
      severity("Hypothetical-Bespoke-1.0", "MIT"), "GREY")
check("an unplaceable family reports UNPLACEABLE",
      verdict("MIT", "Hypothetical-Bespoke-1.0"), "UNPLACEABLE")

# ---------------------------------------------------------------- the costly direction
# The rows that matter commercially: a hosted studio deliverable over a network-copyleft grant.
check("MIT manifest over AGPL payload bills", severity("MIT", "AGPL-3.0"), "RED")
check("MIT manifest over proprietary payload bills", severity("MIT", "PROPRIETARY"), "RED")
check("MIT manifest over an ABSENT grant bills — permissive over nothing",
      severity("MIT", "NONE"), "RED")
check("GPL manifest over AGPL payload still bills (both copyleft, wrong tier)",
      severity("GPL-3.0", "AGPL-3.0"), "RED")
check("AGPL manifest over GPL payload is the harmless direction",
      verdict("AGPL-3.0", "GPL-3.0"), "MANIFEST-UNDERSTATES")
check("LGPL manifest over MIT payload is harmless", severity("LGPL-3.0", "MIT"), "YELLOW")

# ------------------------------------------- the defects THIS instrument shipped with
# 🔴 Found by sweeping the classifier adversarially before trusting it, not by reading it.
# The first cut normalised any unknown family onto a known PREFIX, so all three of these
# placed as tier 0 — permissive — and the third is the one that bills.
check("MITIGATED is not MIT — a family name is a name or it is noise (P299)",
      tier_of("MITIGATED"), None)
check("MIT_MODIFIED does not normalise onto MIT", tier_of("MIT_MODIFIED"), None)
check("MIT-plus-clause is not plain MIT — p1054's whole subject",
      tier_of("MIT-plus-clause"), None)
check("an unplaceable family is GREY, so a human reads the payload",
      severity("MIT-plus-clause", "MIT"), "GREY")
# 🔴 The Commons Clause REMOVES THE RIGHT TO SELL.  A studio reading "Apache-2.0" here ships
# a deliverable it may not sell, so the restriction marker must outrank the base name.
check("Apache-2.0 + Commons Clause is NOT permissive", tier_of("Apache-2.0-with-Commons-Clause"), 5)
check("MIT + Commons Clause is NOT permissive", tier_of("MIT-with-Commons-Clause"), 5)
check("a Commons Clause row over a plain-MIT manifest bills",
      severity("MIT", "Apache-2.0-with-Commons-Clause"), "RED")
check("an added-restriction suffix is not permissive",
      tier_of("MIT-with-added-restriction"), 5)
check("a non-commercial suffix is not permissive", tier_of("Apache-2.0-NonCommercial"), 5)
check("CC-BY-NC-SA-4.0 is caught by the NC marker, not by a prefix",
      tier_of("CC-BY-NC-SA-4.0"), 5)
# And the arms the guard must NOT break: real SPDX spellings still normalise.
check("BSD-3-Clause-Clear is still permissive", tier_of("BSD-3-Clause-Clear"), 0)
check("MIT-0 is still permissive", tier_of("MIT-0"), 0)
check("CC-BY-SA-4.0 stays attribution-share, not NC", tier_of("CC-BY-SA-4.0"), 1)

# ---------------------------------------------------------------- floor (ACTION XR)
# 🔵 The floor is a LOWER BOUND, deliberately below the current count.  `p277` found
# `recount.py` anchored on a literal copy of the number it was checking, so correcting the
# shelf deleted the boundary.  A floor set equal to the current control count has that same
# shape: it fails on every honest addition.  This one catches the case it exists for -- a
# suite that runs nothing and passes vacuously -- and survives growth.
FLOOR = 50
if RAN < FLOOR:
    FAILED.append(f"FAIL floor: suite ran {RAN} controls, floor is {FLOOR} "
                  "(a suite that runs no controls passes vacuously — p252/ACTION XR)")

if FAILED:
    print(f"# {len(FAILED)} FAILING of {RAN}:")
    for f in FAILED:
        print("  " + f)
    sys.exit(1)
print(f"# {RAN}/{RAN} controls pass (p121's ten reproduced, every negative arm asserted)")
sys.exit(0)
