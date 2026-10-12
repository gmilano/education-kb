#!/usr/bin/env python3
"""Suite for `lib/licence_identity.py`. Prints its own total (`P126`'s rule, point 3).

🔵 **The obligatory cases of this suite are the ones where the retired matcher and the
title surface DISAGREE.** A suite that only asserted "an AGPL file reads AGPL" would pass
with the body matcher still in place, which is the mistake this module exists not to make.
Every fixture here is authored in this file; nothing is read from a clone.

    python3 test_licence_identity.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from licence_identity import (GNU_FAMILY, agree, clause_licence,  # noqa: E402
                              naive_verdict, retired_identify, title_licence,
                              title_spdx, title_version)

# ── fixtures, authored ────────────────────────────────────────────────────────────────
# A verbatim GPL-3.0 file: its section 13 names Affero, which is what fired the old rung.
GPL3 = """                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have permission to
link or combine any covered work with a work licensed under version 3 of the
GNU Affero General Public License into a single combined work.

  To do so, attach the following notices to the program.  It is safest to
attach them to the start of each source file:

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
"""

AGPL3 = """                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

  13. Remote Network Interaction; Use with the GNU General Public License.

  Notwithstanding any other provision of this License, if you modify the
Program, your modified version must prominently offer all users interacting
with it remotely through a computer network an opportunity to receive the
Corresponding Source of your version.
"""

# GPL-2.0's preamble names the LESSER licence, which is why a window-wide substring
# search is not good enough and the name must BE the line.
GPL2 = """                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.

  (We sometimes call it the "Library" licence; if this is what you want to do,
use the GNU Lesser General Public License instead of this License.)
"""

LGPL3 = """                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

  This version of the GNU Lesser General Public License incorporates the terms
and conditions of version 3 of the GNU General Public License.
"""

MIT = """MIT License

Copyright (c) 2026 Somebody

Permission is hereby granted, free of charge, to any person obtaining a copy
"""

APACHE = """                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/
"""

ECL = """Educational Community License, Version 2.0

Licensed under the Educational Community License, Version 2.0 (the "License");
"""

# A file whose first line is prose: no title, so no verdict from this surface.
NO_TITLE = """Copyright (c) 2026 Somebody. All rights reserved.
Redistribution and use in source and binary forms are permitted.
"""

cases = []


def check(name, got, want):
    cases.append((name, got == want, got, want))


# ── 1. the defect, reproduced ─────────────────────────────────────────────────────────
check("retired matcher calls GPL-3.0 an AGPL", naive_verdict(GPL3), "AGPL-3.0")
check("retired matcher calls GPL-2.0 nothing", naive_verdict(GPL2), None)
check("retired matcher is right only by accident on AGPL", naive_verdict(AGPL3),
      "AGPL-3.0")

# ── 2. the fix, on the five rows the defect reached ───────────────────────────────────
check("GPL-3.0 reads GPL-3.0", title_spdx(GPL3), "GPL-3.0")
check("GPL-2.0 reads GPL-2.0", title_spdx(GPL2), "GPL-2.0")
check("AGPL-3.0 still reads AGPL-3.0", title_spdx(AGPL3), "AGPL-3.0")
check("LGPL-3.0 reads LGPL-3.0", title_spdx(LGPL3), "LGPL-3.0")

# ── 3. the two surfaces must agree, and say so ────────────────────────────────────────
check("GPL-3.0 agrees across both surfaces", agree(GPL3)[2], "AGREE")
check("AGPL-3.0 agrees across both surfaces", agree(AGPL3)[2], "AGREE")
check("GPL-2.0 has no section 13 at all", clause_licence(GPL2), None)
check("GPL-2.0 is therefore TITLE_ONLY", agree(GPL2)[2], "TITLE_ONLY")
# 🔵 LGPL-3.0 is a set of additional permissions on top of GPL-3.0 and carries no
# numbered section 13 of its own, so the clause surface is silent and the verdict rests
# on the title alone. Asserted rather than assumed, because a reader expects `AGREE`.
check("LGPL-3.0 has no section 13 of its own", clause_licence(LGPL3), None)
check("LGPL-3.0 is therefore TITLE_ONLY, not AGREE", agree(LGPL3)[2], "TITLE_ONLY")

# ── 4. the sibling-mention traps, each one explicitly ─────────────────────────────────
check("the word Affero inside GPL-3.0's body does not win", title_licence(GPL3), "GPL")
check("the word Lesser inside GPL-2.0's preamble does not win", title_licence(GPL2),
      "GPL")
check("the words 'General Public License' inside LGPL's body do not win",
      title_licence(LGPL3), "LGPL")
check("a mention is not a title: prose first line yields nothing",
      title_licence(NO_TITLE), None)
check("and prose yields UNDETERMINED rather than a guess", agree(NO_TITLE)[2],
      "UNDETERMINED")

# ── 5. non-GNU licences, the negative control ─────────────────────────────────────────
check("MIT", title_spdx(MIT), "MIT")
check("Apache-2.0", title_spdx(APACHE), "Apache-2.0")
check("ECL-2.0", title_spdx(ECL), "ECL-2.0")
check("MIT has no section 13", clause_licence(MIT), None)
check("MIT is TITLE_ONLY", agree(MIT)[2], "TITLE_ONLY")
check("a non-GNU id carries no version suffix", title_spdx(APACHE), "Apache-2.0")

# ── 6. the version read, which is the half this shelf got wrong ───────────────────────
check("GPL-3.0 version", title_version(GPL3), "3.0")
check("GPL-2.0 version", title_version(GPL2), "2.0")
check("AGPL-3.0 version", title_version(AGPL3), "3.0")
check("a GNU file with no version line degrades to the bare family",
      title_spdx("GNU GENERAL PUBLIC LICENSE\n\nsome text\n"), "GPL")

# ── 7. the family test the census uses ────────────────────────────────────────────────
check("GPL-3.0 is GNU family", bool(GNU_FAMILY.match("GPL-3.0")), True)
check("AGPL-3.0 is GNU family", bool(GNU_FAMILY.match("AGPL-3.0")), True)
check("LGPL-3.0 is GNU family", bool(GNU_FAMILY.match("LGPL-3.0")), True)
check("MIT is not GNU family", bool(GNU_FAMILY.match("MIT")), False)
check("Apache-2.0 is not GNU family", bool(GNU_FAMILY.match("Apache-2.0")), False)

# ── 8. the window boundary, asserted rather than assumed ──────────────────────────────
deep = "\n".join(["prose line %d" % i for i in range(1, 6)]) + \
       "\nGNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3\n"
check("a title below the window is not read", title_licence(deep), None)
shallow = "\n\n\nGNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3\n"
check("blank lines do not consume the window", title_licence(shallow), "AGPL-3.0")
# 🔵 The window's WIDTH is load-bearing and this is the row that proves it:
# `mhlavac/edupage-mcp` prepends its own copyright line above the GNU title. A one-line
# window would read that row as having no licence at all.
prepended = ("Copyright (c) 2026 Martin Hlavac\n\n"
             "                    GNU GENERAL PUBLIC LICENSE\n"
             "                       Version 3, 29 June 2007\n")
check("a prepended copyright line does not hide the title",
      title_spdx(prepended), "GPL-3.0")

# ── 9. the one case where the surfaces must DISAGREE ──────────────────────────────────
# A hand-edited file titled GPL-3.0 but carrying AGPL's operative clause is the shape
# this module must report rather than guess at.
frankenstein = ("GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007\n\n"
                "  13. Remote Network Interaction; Use with the GNU General Public"
                " License.\n")
check("title GPL + AGPL clause is reported as DISAGREE", agree(frankenstein)[2],
      "DISAGREE")
check("and no verdict is silently promoted", agree(frankenstein)[1],
      ("GPL", "AGPL-3.0"))


# ── 10. `retired_identify` must be the PUBLISHED ladder, not an improvement of it ─────
# 🔵 A reproduction that quietly fixes the order cannot measure what was published, so the
# two orderings that caused T77 are asserted here as REQUIRED behaviour of the repro.
check("repro: GPL-3.0 sorts to AGPL-3.0", retired_identify(GPL3), "AGPL-3.0")
check("repro: GPL-2.0 sorts to LGPL", retired_identify(GPL2), "LGPL")
check("repro: AGPL-3.0 sorts to AGPL-3.0", retired_identify(AGPL3), "AGPL-3.0")
check("repro: LGPL-3.0 sorts to LGPL", retired_identify(LGPL3), "LGPL")
check("repro: MIT is unaffected", retired_identify(MIT), "MIT")
check("repro: Apache is unaffected", retired_identify(APACHE), "Apache-2.0")
check("repro: the Apache rung runs FIRST, so a GNU file quoting Apache sorts OUT",
      retired_identify(GPL3 + "\nbundles material under the Apache License, Version"
                              " 2.0.\n"), "Apache-2.0")
check("repro: a BSD body with no title line still sorts to BSD on the body ladder",
      retired_identify(NO_TITLE), "BSD")
check("and the title surface disagrees with the repro on exactly the GNU rows",
      [retired_identify(b) != title_spdx(b) for b in (GPL3, GPL2, AGPL3, MIT, APACHE)],
      [True, True, False, False, False])


def main():
    failed = [c for c in cases if not c[1]]
    for name, ok, got, want in cases:
        if not ok:
            print("FAIL  %-58s got=%r want=%r" % (name, got, want))
    print("lib/licence_identity: %d tests, %d passed, %d failed"
          % (len(cases), len(cases) - len(failed), len(failed)))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
