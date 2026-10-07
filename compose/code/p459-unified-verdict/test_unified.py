#!/usr/bin/env python3
"""Regression test for p459's unified verdict.  Run: python3 test_unified.py

The assertions that matter are the COMPOSITION ones.  A verdict function built from two
classifiers can be wrong in a way neither input is: it can resolve a disagreement
silently and in the unsafe direction.  So every case below pins which side the answer
came from, and the NC cases pin that ONE side forbidding is enough to forbid.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unified import unified  # noqa: E402

FAIL = []
n = 0


def check(label, got, want):
    global n
    n += 1
    if got != want:
        FAIL.append("%s: got %r want %r" % (label, got, want))


MIT = ("MIT License\n\nCopyright (c) 2026 Example\n"
       "Permission is hereby granted, free of charge, to any person obtaining a copy")
APACHE = ("                                 Apache License\n"
          "                           Version 2.0, January 2004")
CC_NC = ("Creative Commons Attribution-NonCommercial 4.0 International\n\n"
         "NonCommercial - You may not use the material for commercial purposes.")
CC_NC_SA = ("Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International\n\n"
            "NonCommercial - You may not use the material for commercial purposes.\n"
            "ShareAlike - You must distribute under the same license.")
CC_BY = ("Creative Commons Attribution 4.0 International\n\n"
         "You are free to share and adapt for any purpose, even commercially.")
EUPL = ("European Union Public Licence\nV. 1.2\n\n"
        "This European Union Public Licence (the EUPL) applies to the Work.")
ELASTIC = "Elastic License 2.0\n\nURL: https://www.elastic.co/licensing/elastic-license"
POINTER = ("This repository follows the REUSE specification v3.0 for stating license\n"
           "information. All source files contain SPDX IDs in their headers.")

# --- the permissive baseline: both sides agree, and the answer is billable ----------
f, c, py, sh, shc, fl = unified(MIT)
check("MIT family", f, "MIT")
check("MIT commercial", c, "ALLOWED")
check("MIT has no flags", fl, [])
f, c, *_ = unified(APACHE)
check("Apache-2.0 family", f, "Apache-2.0")
check("Apache-2.0 commercial", c, "ALLOWED")

# --- the class that reaches an invoice ----------------------------------------------
f, c, py, sh, shc, fl = unified(CC_NC)
check("CC-BY-NC family is the FINE one", f, "CC-BY-NC-4.0")
check("CC-BY-NC commercial", c, "PROHIBITED")
# 🔴 THIS ASSERTION PINS AN OPEN DEFECT, and it is the reason the flag exists.
# `sweep_payload.family_of` has NO NonCommercial concept: it answers a flat `CC-BY` for a
# payload whose text says NonCommercial, and `CC-BY` permits commercial use.  Pass 28's
# `p447` named this (its `P449` -- "one label CC-BY covers plain Attribution,
# Attribution-NonCommercial, Attribution-NonCommercial-ShareAlike") and did not fix it.
# So the composition is carried by the SHELL side alone on exactly the rows where being
# wrong costs an invoice, and `NC-ONLY-SHELL` records that it is load-bearing rather than
# corroborating.
#
# 🟢 WHEN the Python side gains the NC axis, this assertion must flip to `[]`.  That is
# deliberate: a test that goes red when a defect is FIXED is how this instrument refuses to
# let the gap be closed silently and the flag left behind as noise.
check("CC-BY-NC is seen by the shell alone -- pins the open Python NC gap",
      fl, ["NC-ONLY-SHELL"])
f, c, *_ = unified(CC_NC_SA)
check("CC-BY-NC-SA family", f, "CC-BY-NC-SA-4.0")
check("CC-BY-NC-SA commercial", c, "PROHIBITED")
# NEG: a plain CC-BY is NOT NonCommercial.  Over-restricting costs an opportunity, and
# this is the assertion that keeps the conservative composition from becoming a blanket.
f, c, *_ = unified(CC_BY)
check("NEG plain CC-BY is still commercially usable", c, "ALLOWED")
check("NEG plain CC-BY family carries no NC", f, "CC-BY-4.0")

# --- what only ONE side knows: the EUPL (python taught the shell this pass) ---------
f, c, *_ = unified(EUPL)
check("EUPL family resolves to a version", f, "EUPL-1.2")
check("EUPL commercial", c, "ALLOWED")
# --- what only the shell knows: the non-OSI restriction families --------------------
f, c, py, sh, shc, fl = unified(ELASTIC)
check("Elastic family comes from the shell", f, "Elastic")
check("Elastic commercial", c, "PROHIBITED")
check("Elastic: python's vocabulary has no token for it", py, "UNKNOWN")
check("Elastic is flagged as seen by one side only", "NC-ONLY-SHELL" in fl, False)

# --- declining is an answer, and it must not read as permission ---------------------
f, c, py, sh, shc, fl = unified(POINTER)
check("a REUSE pointer file names no family", f, "UNDETERMINED")
check("an undetermined family is NOT reported as billable", c, "UNDETERMINED")
check("both-declined is flagged", "BOTH-DECLINED" in fl, True)
f, c, *_ = unified("")
check("an empty body is UNREADABLE, not UNKNOWN", f, "UNREADABLE")
check("an unreadable payload is NOT reported as billable", c, "UNDETERMINED")

# --- the negative goes BEFORE the gate ----------------------------------------------
# A payload whose family neither classifier can name can still forbid commercial use.
# The first cut of `unified` asked about the family first and answered UNDETERMINED for
# three real root payloads whose text forbids exactly that -- so this is the assertion
# that keeps "we could not name it" from overwriting "you may not sell it".
NC_NO_FAMILY = ("This dataset is released for academic research or other not-for-profit\n"
                "purposes only.  Any other use requires written permission.")
f, c, py, sh, shc, fl = unified(NC_NO_FAMILY)
check("a restriction without a nameable family is still PROHIBITED", c, "PROHIBITED")
check("and the family is honestly reported as undetermined", f, "UNDETERMINED")

# --- P460: a markup container is declined, not token-matched ------------------------
# The real specimen: `OS4ED/openSIS-*`'s `docs/LICENSE.rtf` wraps the GPL-2.0 text, so
# its title block is RTF markup, the family falls to UNCLASSIFIED, and the body token
# match then reads GPL-2.0 section 3(c)'s "allowed only for noncommercial distribution"
# -- a CONDITION on one distribution option -- as a restriction on the licensee.
RTF_GPL = ("{\\rtf1\\adeflang1025\\ansi\\ansicpg1252\\uc1\\adeff1\\deff0\n"
           "{\\f34\\fbidi \\froman\\fcharset1\\fprq2 Cambria Math;}\n"
           "GNU GENERAL PUBLIC LICENSE Version 2, June 1991\n"
           "this alternative is allowed only for noncommercial distribution and only if\n"
           "you received the program in object code or executable form.")
f, c, py, sh, shc, fl = unified(RTF_GPL)
check("an RTF container is declined, not read", f, "CONTAINER-RTF (no legible)")
check("a declined container is NOT reported as forbidding commercial use", c, "UNDETERMINED")
check("the container is flagged by name", fl, ["CONTAINER-RTF"])
# NEG: the SAME licence as plain text must still read GPL-2.0 and ALLOWED -- otherwise
# the fix above would be suppressing a readable payload too.
PLAIN_GPL2 = ("GNU GENERAL PUBLIC LICENSE\nVersion 2, June 1991\n\n"
              "this alternative is allowed only for noncommercial distribution and only\n"
              "if you received the program in object code or executable form.")
f, c, *_ = unified(PLAIN_GPL2)
check("NEG the same GPL-2.0 as plain text still reads GPL-2.0", f, "GPL-2.0")
check("NEG and section 3(c) does not make GPL-2.0 non-commercial", c, "ALLOWED")

TOTAL = 30
if FAIL:
    print("FAIL (%d of %d)" % (len(FAIL), n))
    for x in FAIL:
        print("  -", x)
    sys.exit(1)
print("%d/%d assertions pass" % (n, n))
