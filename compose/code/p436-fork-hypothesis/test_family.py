#!/usr/bin/env python3
"""Offline control for `family_of`'s RULE ORDER, which is the whole function.

Added 2026-10-07 with the defect it demonstrates. Rule 2 of P126: each positive is
paired with the case that must NOT move, because a reordering that fixes MPL by
breaking GPL passes every one-sided control.

Run: python3 test_family.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sweep_payload import family_of  # noqa: E402

FAIL = []


def check(label, got, want):
    if got != want:
        FAIL.append("%s: got %r want %r" % (label, got, want))


# MPL-2.0 section 1.12 DEFINES "Secondary License" by naming all three GNU licences.
# This is the real wording, and it is why five payloads were filed GPL.
MPL = """Mozilla Public License Version 2.0
==================================

1. Definitions
1.12. "Secondary License"
    means either the GNU General Public License, Version 2.0, the GNU Lesser
    General Public License, Version 2.1, the GNU Affero General Public License,
    Version 3.0, or any later versions of those licenses.
"""
check("an MPL-2.0 payload is MPL-2.0, not GPL", family_of(MPL), "MPL-2.0")

# The line wrapping is the point: "lesser" and "general" split across a newline, so
# the literal "gnu lesser general public license" never matched and the plain GPL
# rule caught it instead.  A whitespace difference chose the commercial verdict.
MPL_UNWRAPPED = MPL.replace("GNU Lesser\n    General", "GNU Lesser General")
check("and it is MPL-2.0 however the GNU names happen to wrap",
      family_of(MPL_UNWRAPPED), "MPL-2.0")

# --- the negatives: nothing in the GNU family may move -----------------------
# No GPL, LGPL or AGPL text names the Mozilla or Eclipse licences, which is what
# makes probing MPL first safe.  Without these three, a reorder that returns
# "MPL-2.0" for everything would pass.
check("a real GPL header is still GPL",
      family_of("                    GNU GENERAL PUBLIC LICENSE\n"
                "                       Version 3, 29 June 2007\n"), "GPL")
check("AGPL is still AGPL and is not swallowed by the GPL rule",
      family_of("GNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3, 19 November 2007\n"),
      "AGPL-3.0")
check("LGPL is still LGPL",
      family_of("GNU LESSER GENERAL PUBLIC LICENSE\nVersion 2.1\n"), "LGPL")
check("Apache-2.0 is unaffected",
      family_of("                                 Apache License\n"
                "                           Version 2.0, January 2004\n"),
      "Apache-2.0")
check("MIT is unaffected",
      family_of("MIT License\n\nCopyright (c) 2026 Someone\n"), "MIT")

# --- EUPL, the EMEA public-sector licence this function could not name -------
# The real `Opetushallitus/aoe` grant, 303 B, in a SUBDIRECTORY.
EUPL = """Copyright (c) 2025 Finnish National Agency for Education

Licensed under the EUPL, Version 1.2 or - as soon as they will be
approved by the European Commission - subsequent versions of the
EUPL.

You may obtain a copy of the EUPL at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
"""
check("the real aoe grant is EUPL, which was UNKNOWN before this pass",
      family_of(EUPL), "EUPL")
check("the spelled-out name resolves in the body too",
      family_of("This work is licensed under the European Union Public Licence 1.2\n"
                "and you may not use it except in compliance with that Licence.\n"),
      "EUPL")
# The NEGATIVE for EUPL: its Appendix names GPL-2.0, AGPL-3.0, EPL and MPL-2.0 as
# compatible licences, so the text carries their marks exactly as MPL carries GNU's.
check("an EUPL payload listing its compatible licences is still EUPL",
      family_of("EUPL-1.2\nAppendix: Compatible Licences\n"
                "GNU General Public License v2.0\n"
                "GNU Affero General Public License v3.0\n"
                "Mozilla Public License v2.0\n"
                "Eclipse Public License v1.0\n"), "EUPL")
# And the negative that stops `eupl` in a HEADER being over-eager: a GPL file that
# merely mentions the word in running prose far down must stay GPL.
check("a GPL payload merely mentioning EUPL compatibility late is still GPL",
      family_of("                    GNU GENERAL PUBLIC LICENSE\n"
                "                       Version 3, 29 June 2007\n\n"
                + "x" * 500 + "\nSee also the EUPL for European public bodies.\n"),
      "GPL")

# --- the dual-licensed pair that found the whole thing -----------------------
check("veraPDF's GPL arm reads GPL",
      family_of("                    GNU GENERAL PUBLIC LICENSE\n   Version 3\n"),
      "GPL")
check("veraPDF's MPL arm reads MPL-2.0, and before this pass read GPL",
      family_of(MPL), "MPL-2.0")

TOTAL = 15
if FAIL:
    print("FAIL (%d of %d)" % (len(FAIL), TOTAL))
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("%d/%d assertions pass, no network" % (TOTAL, TOTAL))
