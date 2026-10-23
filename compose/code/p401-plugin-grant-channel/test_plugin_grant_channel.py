#!/usr/bin/env python3
"""p401 controls.  Offline, fixture-backed, no network, no live-tree reads.

p400-H's rule obeyed: no control pins a live derived verdict.  Every payload
below is a COMMITTED synthetic fixture, so a later pass writing to the shelves
cannot turn these red.

Two mutation runs at the bottom re-commit each defect on purpose and assert the
controls FIRE.  A control that cannot fail is not a control (p387-G).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import plugin_grant_channel as m  # noqa: E402

FIX = os.path.join(HERE, "fixture")


def fx(name):
    with open(os.path.join(FIX, name), encoding="utf-8") as f:
        return f.read()


PASS, FAIL = [], []


def check(n, label, got, want):
    (PASS if got == want else FAIL).append((n, label, got, want))


# ---- group 1: 401-B, the title-vs-name trap ------------------------------
# The whole point.  This payload is GPL-3.0 and CONTAINS "GNU Affero General
# Public License" because section 13 is titled with it.
check(1, "GPL-3.0 carrying its own s13 AFFERO title is GPL, not AGPL",
      m.classify(fx("gpl3-with-s13.txt")), "GPL-3.0")
check(2, "a real AGPL-3.0 payload is still AGPL",
      m.classify(fx("agpl3.txt")), "AGPL-3.0")
check(3, "the s13 fixture really does contain the AFFERO string "
         "(else control 1 proves nothing)",
      "AFFERO" in fx("gpl3-with-s13.txt").upper(), True)
check(4, "title_line stops at the TITLE, not at s13",
      m.title_line(fx("gpl3-with-s13.txt")), "GNU GENERAL PUBLIC LICENSE")
check(5, "a short GPL notice with no title block still reads GPL-3.0-or-later",
      m.classify(fx("gpl3-short-notice.txt")), "GPL-3.0-or-later")

# ---- group 2: the other families, so the classifier is not GPL-only ------
check(6, "MIT", m.classify(fx("mit.txt")), "MIT")
check(7, "Apache-2.0", m.classify(fx("apache2.txt")), "Apache-2.0")
check(8, "CC-BY-NC is marked NC, because NonCommercial is not an OSI grant",
      m.classify(fx("ccbync4.txt")), "CC-NC")
check(9, "a payload naming no licence is UNKNOWN, never a guess",
      m.classify("just some prose about education"), "UNKNOWN")
check(10, "an empty payload is UNKNOWN", m.classify(""), "UNKNOWN")

# ---- group 3: 401-A, the PHP header channel ------------------------------
check(11, "a Moodle version.php header yields GPL-3.0-or-later",
      m.php_header_grant(fx("version.php")), "GPL-3.0-or-later")
check(12, "a version.php with no notice yields None, not a default",
      m.php_header_grant(fx("nogrant.php")), None)
check(13, "LADDER_BLIND when only the PHP header answers",
      m.verdict(None, "GPL-3.0-or-later", True), "LADDER_BLIND")
check(14, "BOTH_AGREE when the two channels agree on the family",
      m.verdict("GPL-3.0-or-later", "GPL-3.0-or-later", True), "BOTH_AGREE")
check(15, "CHANNEL_CONFLICT is reachable and kept APART from LADDER_BLIND",
      m.verdict("AGPL-3.0", "GPL-3.0-or-later", True), "CHANNEL_CONFLICT")
check(16, "NO_GRANT_EITHER_CHANNEL needs a PASSING branch control",
      m.verdict(None, None, True), "NO_GRANT_EITHER_CHANNEL")
check(17, "a failing branch control is ADDRESS_UNRESOLVED and NOT an absence",
      m.verdict(None, None, False), "ADDRESS_UNRESOLVED")

# ---- group 4: 401-C, the case-folded branch control ----------------------
check(18, "the branch-control ladder is case-folded (readme.md is in it)",
      "readme.md" in m.BRANCH_CONTROL_LADDER, True)
check(19, "and version.php is in it, because a Moodle plugin always has one",
      "version.php" in m.BRANCH_CONTROL_LADDER, True)
check(20, "the LICENSE ladder is exactly the four paths prior passes probed",
      m.LADDER, ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"))

# ---- mutation run 1: re-commit 401-B (name-anywhere matching) ------------
def mutant_name_anywhere(payload):
    up = payload.upper()
    if "GNU AFFERO" in up:
        return "AGPL-3.0"
    if "GNU GENERAL PUBLIC LICENSE" in up:
        return "GPL-3.0"
    return "UNKNOWN"


MUT1 = [m.classify(fx("gpl3-with-s13.txt")) == mutant_name_anywhere(fx("gpl3-with-s13.txt")),
        m.classify(fx("agpl3.txt")) == mutant_name_anywhere(fx("agpl3.txt"))]

# ---- mutation run 2: re-commit 401-C (README.md as the sole control) -----
def mutant_single_control(present_files):
    return "README.md" in present_files


MUT2_live = mutant_single_control({"readme.md", "version.php", "lib.php"})
MUT2_fixed = any(f in {"readme.md", "version.php", "lib.php"}
                 for f in m.BRANCH_CONTROL_LADDER)

print(f"p401-plugin-grant-channel: {len(PASS)}/{len(PASS) + len(FAIL)} controls pass")
for n, label, got, want in FAIL:
    print(f"  RED  control {n}: {label}\n       got={got!r} want={want!r}")

print("\nmutation 1 — classifier keyed on a name ANYWHERE (401-B re-committed):")
print(f"  GPL-3.0 w/ s13 : mutant says {mutant_name_anywhere(fx('gpl3-with-s13.txt'))!r}, "
      f"instrument says {m.classify(fx('gpl3-with-s13.txt'))!r} "
      f"-> {'AGREE (control blind!)' if MUT1[0] else 'DIVERGE (control fires)'}")
print(f"  real AGPL-3.0  : mutant says {mutant_name_anywhere(fx('agpl3.txt'))!r}, "
      f"instrument says {m.classify(fx('agpl3.txt'))!r} "
      f"-> {'AGREE (correctly, both right here)' if MUT1[1] else 'DIVERGE'}")
print("  => the mutant is wrong on the GPL-3.0 payload and right on the AGPL one,")
print("     which is exactly why 7 false AGPL verdicts looked plausible in this pass's first run.")

print("\nmutation 2 — README.md as the SOLE branch control (401-C re-committed):")
print(f"  repo carrying only lowercase readme.md: mutant control ok={MUT2_live}, "
      f"ladder control ok={MUT2_fixed}")
print("  => the mutant grades a live repository ADDRESS_UNRESOLVED; the ladder does not.")

if FAIL or MUT1[0] or not MUT2_fixed or MUT2_live:
    sys.exit(1)
print("\nOK — 20/20 controls green, both mutations fire.")
