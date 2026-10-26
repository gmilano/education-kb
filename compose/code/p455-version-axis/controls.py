#!/usr/bin/env python3
"""p455 controls -- run BEFORE any verdict is published, in both directions.

`Gap 454-E` is the reason this file is longer than the instrument it guards:
four defects were found inside p454's own reader, three of them that pass's
own, and every one of them would have published a wrong grant. The cheapest
protection this base has found is a control that asserts digests EARLIER
PASSES PUBLISHED -- a reader that cannot reproduce them has regressed.

Directions asserted:
  POSITIVE  -- a stock payload of family F version V grades F-V
  NEGATIVE  -- a payload of family F version V does NOT grade F-W, W != V
  REGRESSION-- p454's family-level grades are unchanged for non-GNU families
  PUBLISHED -- digests from p454/p453 shelf cells reproduce byte-for-byte
  FABRICATED-- an address that cannot exist reads as ADDRESS_DEAD, so every
               positive above is a measurement and not a property of the probe
"""
import os
import re
import sys

# `-I` (isolated) drops the script directory from sys.path; these modules are
# this pass's own instrument, so the path is added back explicitly rather than
# running without isolation.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import family_version as fv
import family_title as ft
import fetch

FAILS, RUNS = [], 0

def ft_canon(grade):
    """p454's collapsing canon(), reconstructed from its published behaviour:
    it mapped every GNU grade onto the bare FAMILY, which is exactly why it
    graded the edu-sharing pair AGREE (`Gap 454-C`)."""
    g = (grade or "").strip().lower().replace("gnu ", "")
    g = re.sub(r"[\s_-]+", "-", g)
    if "agpl" in g or "affero" in g:
        return "AGPL"
    if "lgpl" in g or "lesser" in g:
        return "LGPL"
    if "gpl" in g:
        return "GPL"
    return fv.canon(grade)



def check(name, got, want):
    global RUNS
    RUNS += 1
    if got != want:
        FAILS.append(f"{name}: got {got!r}, want {want!r}")
        print(f"  FAIL {name}: got {got!r} want {want!r}")
    else:
        print(f"  ok   {name}: {got!r}")


def check_true(name, cond, detail=""):
    global RUNS
    RUNS += 1
    if not cond:
        FAILS.append(f"{name}: {detail}")
        print(f"  FAIL {name}: {detail}")
    else:
        print(f"  ok   {name} {detail}")


# ---------------------------------------------------------------- stock payloads
# Read first-hand from the projects that serve them, not pasted from memory.
# Each is a repository this base already carries or a canonical GNU host.
STOCK = {
    "GPL-2.0":   ("oat-sa/tao-core", "GPL-2.0"),      # p454: GPLv2, the defect case
    "GPL-3.0":   ("edu-sharing/Edu-Sharing", "GPL-3.0"),  # Gap 454-C's live pair
    "AGPL-3.0":  ("learnhouse/learnhouse", "AGPL-3.0"),
    "Apache-2.0": ("huggingface/agents-course", "Apache-2.0"),
    # p454 grades a titleless MIT payload `MIT (body form, no title)` and that
    # is CORRECT -- `inducer/relate` serves a bare "Copyright (c) ..." opening
    # with no title line. This control's first cut expected "MIT" and the
    # failure was the EXPECTATION's, not the reader's.
    "MIT":       ("inducer/relate", "MIT (body form, no title)"),
}

print("[1] POSITIVE + NEGATIVE: stock payloads read first-hand at HEAD")
payloads = {}
for want, (addr, expect) in STOCK.items():
    g = fetch.grant(addr)
    if g["verdict"] != "READ":
        check_true(f"read {addr}", False, g["verdict"])
        continue
    payloads[addr] = g
    got = fv.family(g["text"])
    check(f"{addr} [{g['bytes']}B {g['sha']}]", got, expect)
    # NEGATIVE direction: the grade must not be any OTHER version of its family.
    if "-" in expect and expect.split("-")[0] in ("GPL", "LGPL", "AGPL"):
        fam = expect.split("-")[0]
        for other in ("2.0", "2.1", "3.0"):
            if f"{fam}-{other}" != expect:
                check_true(f"{addr} not {fam}-{other}", got != f"{fam}-{other}")

print("\n[2] Gap 454-C: the pair p454's canon() graded AGREE must now DISAGREE")
# npm `ngx-edu-sharing-api` declares GNU GPL v2; the payload at HEAD is v3.
reg = fetch.registry("npm", "ngx-edu-sharing-api")
declared = reg["declared"]
check_true("npm ngx-edu-sharing-api readable", reg["status"] == 200,
           f"status={reg['status']} declared={declared!r} backlink={reg['backlink']!r}")
if "edu-sharing/Edu-Sharing" in payloads:
    served = fv.family(payloads["edu-sharing/Edu-Sharing"]["text"])
    old_decl, old_served = ft_canon(declared), ft_canon(served)
    new_decl, new_served = fv.canon(declared), fv.canon(served)
    print(f"  declared={declared!r} served={served!r}")
    print(f"  p454 canon: {old_decl!r} vs {old_served!r}")
    print(f"  p455 canon: {new_decl!r} vs {new_served!r}")
    check_true("p455 canon DISAGREES on the pair", new_decl != new_served,
               f"{new_decl} vs {new_served}")
    check_true("and the incompatibility is named",
               fv.compatible(declared, served) is False,
               f"compatible={fv.compatible(declared, served)}")

print("\n[3] REGRESSION: non-GNU grades identical to p454's reader")
for addr, g in payloads.items():
    a, b = ft.family(g["text"]), fv.family(g["text"])
    if not a.startswith(("GPL", "LGPL", "AGPL")):
        check(f"{addr} unchanged vs p454", b, a)
    else:
        # Second control defect of this pass: "must DIFFER from p454" is wrong
        # for AGPL, whose only live version is 3.0 -- p454's FAMILY_TOKENS
        # already spelled it `AGPL-3.0`, so there is nothing to refine. The
        # sound assertion is that the p455 grade CARRIES a version, which is
        # what `Gap 454-C` actually asked for.
        check_true(f"{addr} version-bearing", re.match(r"^(AGPL|LGPL|GPL)-\d\.\d$", b) is not None,
                   f"p454={a!r} p455={b!r}")

print("\n[4] only_or_later -- the axis that decides whether GPL-2.0 may combine")
if "oat-sa/tao-core" in payloads:
    ool = fv.only_or_later(payloads["oat-sa/tao-core"]["text"])
    check_true("tao-core GPLv2 forward grant read", ool in ("only", "or-later", "UNSTATED"), ool)
check("UNSTATED is not guessed", fv.only_or_later("MIT License\n\nPermission is hereby"), "UNSTATED")
check("explicit or-later", fv.only_or_later("either version 2 of the License, or (at your option) any later version"), "or-later")
check("explicit only", fv.only_or_later("GNU General Public License version 2 only"), "only")

print("\n[5] canon() normalises registry shorthand onto the SPDX form")
for raw_s, want in [("GNU GPL v2", "GPL-2.0"), ("GPLv3", "GPL-3.0"),
                    ("gpl-2.0-only", "GPL-2.0"), ("GPL-3.0-or-later", "GPL-3.0"),
                    ("LGPL-3.0", "LGPL-3.0"), ("GNU LGPL v2", "LGPL-2.1"),
                    ("AGPL-3.0", "AGPL-3.0"), ("Apache-2.0", "Apache-2.0"),
                    ("MIT", "MIT"), ("ISC", "ISC")]:
    check(f"canon({raw_s!r})", fv.canon(raw_s), want)

print("\n[6] FABRICATED NEGATIVE CONTROL")
neg = fetch.grant("nope-p455-version-axis/nope-p455")
check("fabricated address", neg["verdict"], "ADDRESS_DEAD")

print(f"\n{RUNS - len(FAILS)}/{RUNS} controls pass")
if FAILS:
    print("FAILURES:")
    for f in FAILS:
        print(" -", f)
    sys.exit(1)
