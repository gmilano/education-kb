#!/usr/bin/env python3
"""Controls for `p241-blanket-denial`, in BOTH directions.

The suite's whole burden is the FALSE-POSITIVE mode.  `all rights reserved` is a line in
`BSD-2`, `BSD-3` and many `MIT` headers, so a gate that convicts on it would downgrade
most of this KB's permissive estate.  Every `grant-*` fixture is a real payload read
first-hand from `raw.githubusercontent.com`, and `grant-bsd3.txt` carries the line AND a
grant -- it is the control that must never convict.

`p355-cwd-portability`: this file is invoked from its own directory by `make hooks`.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blanket_denial import (  # noqa: E402
    verdict, may_publish, grants_found, denials_found, reserved_found,
    GRANT, DENIAL, RESERVED_WEAK,
)

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, "fixtures")

fails = []
n = 0


def check(label, got, want):
    global n
    n += 1
    if got != want:
        fails.append("%-56s got=%r want=%r" % (label, got, want))


def fixture(name):
    with open(os.path.join(FIX, name), "rb") as fh:
        return fh.read().decode("utf-8", "replace")


# ---------------------------------------------------------------- the two positives
# Both are ENGLISH, and both returned `commercial_use_ok`=ALLOWED from the shared
# classifier at p241.  That is the defect this instrument exists for.
d1 = fixture("denial-no-permission.txt")
check("Samielakkad: verdict", verdict(d1), "BLANKET-DENIAL")
check("Samielakkad: may_publish", may_publish(d1), False)
check("Samielakkad: no grant verb present", grants_found(d1), [])
check("Samielakkad: a denial fired", len(denials_found(d1)) > 0, True)

d2 = fixture("denial-proprietary-relicense.txt")
check("snflwr.ai: verdict", verdict(d2), "BLANKET-DENIAL")
check("snflwr.ai: may_publish", may_publish(d2), False)
check("snflwr.ai: no grant verb present", grants_found(d2), [])

# `p240`'s headline payload.  This instrument does NOT read Chinese and must not pretend
# to: the correct answer is a REFUSAL, reached without any restriction vocabulary at all.
d3 = fixture("denial-zh-opengaokao.txt")
check("OpenGaokao(zh): verdict", verdict(d3), "NO-GRANT-LANGUAGE")
check("OpenGaokao(zh): may_publish", may_publish(d3), False)
check("OpenGaokao(zh): no English grant verb", grants_found(d3), [])

# ------------------------------------------------- THE FALSE-POSITIVE MODE: BSD
# `BSD-3-Clause` says "All rights reserved." and then GRANTS.  If this convicts, the gate
# is worse than no gate.
bsd = fixture("grant-bsd3.txt")
check("BSD-3: carries the reserved line", reserved_found(bsd), ["all rights reserved"])
check("BSD-3: ALSO carries a grant verb", len(grants_found(bsd)) > 0, True)
check("BSD-3: verdict is GRANT-PRESENT", verdict(bsd), "GRANT-PRESENT")
check("BSD-3: may_publish", may_publish(bsd), True)

# ---------------------------------------------------------------- permissive controls
for name, label in (("grant-mit.txt", "MIT"),
                    ("grant-apache20.txt", "Apache-2.0"),
                    ("grant-agpl30.txt", "AGPL-3.0")):
    p = fixture(name)
    check("%s: verdict" % label, verdict(p), "GRANT-PRESENT")
    check("%s: may_publish" % label, may_publish(p), True)
    check("%s: no denial fires" % label, denials_found(p), [])

# ---------------------------------------------------------------- the discriminator
# This pair IS the design.  Same reserved line; the grant decides.
check("reserved alone convicts",
      verdict("Copyright (c) 2026 X. All rights reserved."), "BLANKET-DENIAL")
check("reserved + grant does NOT convict",
      verdict("Copyright (c) 2026 X. All rights reserved.\n"
              "Permission is hereby granted, free of charge, to any person."),
      "GRANT-PRESENT")

# ---------------------------------------------------------------- explicit denials
check("no permission is granted",
      verdict("NO PERMISSION is granted to use this."), "BLANKET-DENIAL")
check("no license is granted",
      verdict("No license is granted to any party."), "BLANKET-DENIAL")
check("British spelling: no licence is granted",
      verdict("No licence is granted."), "BLANKET-DENIAL")
check("proprietary software license header",
      verdict("Acme - Proprietary Software License"), "BLANKET-DENIAL")
check("no rights are granted",
      verdict("No rights are granted hereunder."), "BLANKET-DENIAL")
check("strictly prohibited",
      verdict("Redistribution is strictly prohibited."), "BLANKET-DENIAL")
check("unauthorized copying",
      verdict("Unauthorized copying of this file is forbidden."), "BLANKET-DENIAL")
check("is not open source",
      verdict("This is not open source software."), "BLANKET-DENIAL")

# a denial OUTRANKS a grant: a payload that grants and then denies is not clearable
check("denial outranks a grant verb",
      verdict("Permission is hereby granted. However no license is granted "
              "for commercial use."), "BLANKET-DENIAL")

# ---------------------------------------------------------------- refusal state
check("empty payload refuses", verdict(""), "NO-GRANT-LANGUAGE")
check("whitespace payload refuses", verdict("   \n\t  "), "NO-GRANT-LANGUAGE")
check("prose with no grant and no denial refuses",
      verdict("This repository contains course notes for CS101."),
      "NO-GRANT-LANGUAGE")
check("NO-GRANT-LANGUAGE never publishes",
      may_publish("This repository contains course notes."), False)

# ---------------------------------------------------------------- normalisation
check("case-insensitive grant",
      verdict("PERMISSION IS HEREBY GRANTED, FREE OF CHARGE"), "GRANT-PRESENT")
check("newline-folded grant",
      verdict("permission is\nhereby granted"), "GRANT-PRESENT")
check("tab/multi-space-folded denial",
      verdict("no    permission\tis  granted"), "BLANKET-DENIAL")
check("case-insensitive reserved line",
      verdict("ALL RIGHTS RESERVED"), "BLANKET-DENIAL")

# ---------------------------------------------------------------- each grant verb clears
for g in GRANT:
    check("grant verb clears: %s" % g[:34], verdict("Notice. " + g + " etc."),
          "GRANT-PRESENT")

# ---------------------------------------------------------------- each denial convicts
for d in DENIAL:
    check("denial convicts: %s" % d[:34],
          verdict("Notice. " + d + " etc."), "BLANKET-DENIAL")

# ---------------------------------------------------------------- vocabulary hygiene
check("no phrase is in both lists", set(GRANT) & set(DENIAL), set())
check("grant list is lowercase", all(g == g.lower() for g in GRANT), True)
check("denial list is lowercase", all(d == d.lower() for d in DENIAL), True)
check("reserved-weak is lowercase",
      all(r == r.lower() for r in RESERVED_WEAK), True)
check("no duplicate grant phrases", len(set(GRANT)), len(GRANT))
check("no duplicate denial phrases", len(set(DENIAL)), len(DENIAL))
# a RESERVED_WEAK phrase must never also be a DENIAL, or the exemption is dead code
check("reserved-weak disjoint from denial",
      set(RESERVED_WEAK) & set(DENIAL), set())

# ---------------------------------------------------------------- the three states only
for p in (d1, d2, d3, bsd, fixture("grant-mit.txt"), "", "random prose"):
    check("verdict is one of three states",
          verdict(p) in ("GRANT-PRESENT", "BLANKET-DENIAL", "NO-GRANT-LANGUAGE"),
          True)

# ---------------------------------------------------- CROSS-INSTRUMENT AGREEMENT (p637)
# `lib/license_family.sh` carries this predicate a SECOND time, as a shell branch inside
# `commercial_use_ok`.  `p637-cross-instrument-licence-agreement` established the rule:
# two implementations of one predicate are MEASURED against each other, never assumed to
# agree.  `P171` -- reintroduced at pass 77 by a hand-written copy -- is why.
import subprocess  # noqa: E402

LIB = os.path.join(HERE, "..", "lib", "license_family.sh")
SH = """. %s
if commercial_use_ok "$(cat %s)"; then echo ALLOWED; else echo RESTRICTED; fi"""


def shell_commercial(path):
    out = subprocess.run(["bash", "-c", SH % (LIB, path)],
                         capture_output=True, text=True,
                         cwd=os.path.join(HERE, "..", "lib"))
    return out.stdout.strip().splitlines()[-1] if out.stdout.strip() else "ERR"


# For every fixture, the python verdict and the shell branch must give the SAME
# commercial answer.  GRANT-PRESENT -> ALLOWED; both refusal states -> RESTRICTED,
# EXCEPT where the shell reaches a recognised family first (AGPL/Apache/MIT are
# classified and return ALLOWED before this branch is consulted at all).
AGREEMENT = {
    "denial-no-permission.txt": "RESTRICTED",
    "denial-proprietary-relicense.txt": "RESTRICTED",
    "denial-zh-opengaokao.txt": "RESTRICTED",   # via the P240 branch, not this one
    "grant-mit.txt": "ALLOWED",
    "grant-apache20.txt": "ALLOWED",
    "grant-agpl30.txt": "ALLOWED",
    "grant-bsd3.txt": "ALLOWED",                # the false-positive control
}
for name, want in AGREEMENT.items():
    check("cross-instrument: %s" % name,
          shell_commercial(os.path.join(FIX, name)), want)

# And the one that would have caught the defect: a payload this instrument calls
# BLANKET-DENIAL must never be ALLOWED by the shell branch.
for name in ("denial-no-permission.txt", "denial-proprietary-relicense.txt"):
    text = fixture(name)
    check("no BLANKET-DENIAL is shell-ALLOWED: %s" % name,
          (verdict(text), shell_commercial(os.path.join(FIX, name))),
          ("BLANKET-DENIAL", "RESTRICTED"))

print("%d/%d controls pass" % (n - len(fails), n))
for f in fails:
    print("  FAIL " + f)
sys.exit(1 if fails else 0)
