"""Controls for `grade.py`. Runs under `python3 -I` from the repository root AND from this
folder (the `p355-cwd-portability` class the Makefile says kept a working gate a one-off).

🔵 A channel or a grader that agrees with everything proves nothing. The controls below include
NEGATIVE ones: payloads that MUST NOT grade permissive, and a garbage payload that must grade
`UNSTATED` rather than fall back to a guess.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grade import (
    grade,
    permissive,
    buildable_for_paid_client_work,
    gnu_or_later,
    gnu_version,
    title_block,
    gnu_title_region,
    headline,
    names_standard,
)

MIT = """MIT License

Copyright (c) 2021 Learning Equality

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
"""

APACHE = """                               Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
"""

GPL3 = """                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc.
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
"""

AGPL3 = """                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc.
"""

# The WRAPPER control, and it is the one that refines p455: a title block naming a licence no
# SPDX id matches, sitting over a verbatim AGPL-3.0 body.
WRAPPER = """Claroline Connect License
=========================

Copyright (c) 2013 Claroline Consortium

                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc.
"""

CC_NC = """Attribution-NonCommercial 4.0 International
=======================================================================

Creative Commons Corporation ("Creative Commons") is not a law firm.
"""

CC_SA = """Creative Commons Attribution-ShareAlike 4.0 International

Copyright (c) 2026 Gareth Manning

The educational skills are licensed under the Creative Commons
Attribution-ShareAlike 4.0 International licence (CC BY-SA 4.0).
"""

ELASTIC = """Elastic License 2.0

URL: https://www.elastic.co/licensing/elastic-license

## Acceptance
By using the software, you agree to all of the terms and conditions below.
"""

# A bespoke grant that BORROWS the MIT opening phrase but restricts commercial use. A grader
# that matches the MIT phrase first calls this permissive, which is the defect this control
# exists to catch.
BESPOKE_NC = """# PageLM Community License

**Copyright (c) 2025 nullure & recabasic**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to use, copy, modify, and run the Software
for **personal, educational, or non-commercial research purposes**, subject to the terms herein.
"""

GARBAGE = "all rights reserved\n\nplease contact us for terms\n"

# 🔴 The control that found the defect: canonical GPL-3.0 names the AGPL in its own section 13.
# A grader that scans the BODY for "gnu affero" grades this AGPL-3.0. It must grade GPL-3.0.
GPL3_WITH_AGPL_CROSSREF = GPL3 + """
  13. Remote Network Interaction; Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have permission to
link or combine any covered work with a work licensed under version 3 of the
GNU Affero General Public License into a single combined work.
"""

CASES = [
    # (name, payload, expected spdx, expected verdict)
    ("mit", MIT, "MIT", "PERMISSIVE"),
    ("apache", APACHE, "Apache-2.0", "PERMISSIVE"),
    ("gpl3", GPL3, "GPL-3.0", "COPYLEFT"),
    ("agpl3", AGPL3, "AGPL-3.0", "COPYLEFT"),
    ("wrapper-over-agpl", WRAPPER, "AGPL-3.0", "COPYLEFT"),
    ("cc-by-nc", CC_NC, "CC-BY-NC-4.0", "NON_COMMERCIAL_REFUSED"),
    ("cc-by-sa", CC_SA, "CC-BY-SA-4.0", "SHAREALIKE_CONTENT"),
    ("elastic", ELASTIC, "Elastic-2.0", "SOURCE_AVAILABLE_RESTRICTED"),
    ("bespoke-nc", BESPOKE_NC, "BESPOKE-NC", "NON_COMMERCIAL_REFUSED"),
    ("garbage-refusal", GARBAGE, "UNSTATED", "UNSTATED"),
    ("gpl3-naming-agpl-in-s13", GPL3_WITH_AGPL_CROSSREF, "GPL-3.0", "COPYLEFT"),
]


def main():
    failures = []
    n = 0

    for name, payload, want_spdx, want_verdict in CASES:
        got = grade(payload)
        n += 1
        if got["spdx"] != want_spdx:
            failures.append("%s: spdx %r != %r" % (name, got["spdx"], want_spdx))
        n += 1
        if got["verdict"] != want_verdict:
            failures.append("%s: verdict %r != %r" % (name, got["verdict"], want_verdict))

    # The wrapper control must also SAY it is a wrapper, else a reader cannot tell the
    # difference between a clean AGPL and a bespoke title over one.
    n += 1
    if "WRAPPER" not in grade(WRAPPER)["basis"]:
        failures.append("wrapper: basis does not record the wrapper")

    # Negative controls on the two predicates.
    n += 1
    if permissive(grade(CC_NC)["verdict"]):
        failures.append("cc-by-nc graded permissive")
    n += 1
    if permissive(grade(BESPOKE_NC)["verdict"]):
        failures.append("bespoke-nc graded permissive")
    n += 1
    if permissive(grade(ELASTIC)["verdict"]):
        failures.append("elastic graded permissive")
    n += 1
    if buildable_for_paid_client_work(grade(CC_NC)["verdict"]):
        failures.append("cc-by-nc called buildable for paid client work")
    n += 1
    if buildable_for_paid_client_work(grade(BESPOKE_NC)["verdict"]):
        failures.append("bespoke-nc called buildable for paid client work")
    n += 1
    if not buildable_for_paid_client_work(grade(MIT)["verdict"]):
        failures.append("mit called not buildable")
    n += 1
    if not permissive(grade(APACHE)["verdict"]):
        failures.append("apache not graded permissive")

    # p455's version + election axes.
    n += 1
    if gnu_version(GPL3) != "3.0":
        failures.append("gpl3 version misread: %r" % gnu_version(GPL3))
    n += 1
    if gnu_or_later(GPL3) != "or-later":
        failures.append("gpl3 election misread: %r" % gnu_or_later(GPL3))
    n += 1
    if gnu_or_later(AGPL3) != "UNSTATED":
        failures.append("agpl3 election should be UNSTATED, got %r" % gnu_or_later(AGPL3))

    # The title block must not reach into a long body: 20 NON-BLANK filler lines, then a
    # sentinel. A blank-line pad would not test the boundary, since the window counts non-blank.
    n += 1
    padded = MIT + "".join("filler %d\n" % i for i in range(20)) + "TERMS AND CONDITIONS\n"
    if "terms and conditions" in title_block(padded):
        failures.append("title_block reached past its window")

    # The wrapper's headline must be the bespoke name, and the 12-line window must NOT be able
    # to tell the difference -- that asymmetry is the whole finding, so it is pinned here.
    n += 1
    if headline(WRAPPER) != "claroline connect license":
        failures.append("headline misread: %r" % headline(WRAPPER))
    n += 1
    if not names_standard(title_block(WRAPPER)):
        failures.append("title window should (misleadingly) look standard for the wrapper")
    n += 1
    if names_standard(headline(WRAPPER)):
        failures.append("headline should NOT look standard for the wrapper")
    n += 1
    if "WRAPPER" in grade(AGPL3)["basis"]:
        failures.append("clean AGPL wrongly flagged as a wrapper")

    # The GNU window must exclude a cross-reference sitting just past it, and must still reach
    # the AGPL title in the wrapper (line 4).
    n += 1
    if "affero" in gnu_title_region(GPL3_WITH_AGPL_CROSSREF):
        failures.append("GNU window reached the section-13 cross-reference")
    n += 1
    if "affero" not in gnu_title_region(WRAPPER):
        failures.append("GNU window failed to reach the wrapper's AGPL title on line 4")

    print("controls: %d/%d green" % (n - len(failures), n))
    for f in failures:
        print("  FAIL", f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
