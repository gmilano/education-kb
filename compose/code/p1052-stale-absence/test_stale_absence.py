#!/usr/bin/env python3
"""Offline checks for P1052. No network: every case is a fixture string taken
verbatim from a file this pass actually read over raw.githubusercontent.com.

Run: python3 -I test_stale_absence.py
"""
import os
import sys

# python3 -I removes the script directory from sys.path, so put it back.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stale_absence as S  # noqa: E402

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


# --- limb 2, manifest extraction: the forms this pass measured -----------------
check(S.manifest_license("package.json", '{"name":"x","license":"MIT"}') == "MIT",
      "npm: a flat license string must be read")
check(S.manifest_license("package.json",
                         '{"name":"x","license":{"type":"MIT","url":"u"}}') == "MIT",
      "npm: the legacy object form must be read")
check(S.manifest_license("package.json", '{"name":"x"}') is None,
      "npm: no license field must return None, not a guess")
check(S.manifest_license("package.json", "not json at all") is None,
      "npm: unparseable manifest must not raise")

# shmercer/writeAlizer, DESCRIPTION, read this pass. The LICENSE file beside it is
# 47 B of YEAR/COPYRIGHT HOLDER and carries no grant at all.
check(S.manifest_license("DESCRIPTION",
                         "Package: writeAlizer\nLicense: MIT + file LICENSE\nLanguage: en-US\n")
      == "MIT + file LICENSE",
      "CRAN: the grant lives in DESCRIPTION and must be read verbatim")

check(S.manifest_license("pyproject.toml", '[project]\nlicense = {text = "Apache-2.0"}\n')
      == "Apache-2.0", "pyproject: PEP 621 table form")
check(S.manifest_license("Cargo.toml", 'license = "GPL-3.0-or-later"\n')
      == "GPL-3.0-or-later", "cargo: plain string form")
check(S.manifest_license("pom.xml",
                         "<licenses><license><name>Educational Community License, "
                         "Version 2.0</name></license></licenses>")
      == "Educational Community License, Version 2.0", "maven: nested <name>")

# --- the FALSE POSITIVE this pass measured, kept as a regression --------------
# ShuyunYuan/talentcoach serves an 842 B ALL RIGHTS RESERVED licence that copies
# MIT's warranty disclaimer. GRANT_TEXT matches it. The instrument must therefore
# never be read as a verdict, and this test documents that it is not one.
TALENTCOACH = ("Copyright (c) 2026 Shuyun Yuan. All rights reserved.\n\n"
               "This repository is published for portfolio and code-review purposes "
               "only. Viewing the source on GitHub is permitted; no other rights are "
               "granted.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY "
               "KIND, EXPRESS OR IMPLIED")
check(S.GRANT_TEXT.search(TALENTCOACH) is not None,
      "the disclaimer-borrowing false positive must still be reproduced, so that "
      "anyone reading this instrument knows the marker is a CUE and not a verdict")
check(S.IDENT.search(TALENTCOACH) is None,
      "and no licence IDENTIFIER may be claimed for it: 'all rights reserved' is not "
      "an SPDX identifier")

# --- the INCOMPLETE grant: a title and a holder, no permission clause ---------
# MoKangMedical/digital-sage, 46 B, read verbatim this pass.
DIGITAL_SAGE = "MIT License\n\nCopyright (c) 2026 MoKangMedical\n"
check(S.IDENT.search(DIGITAL_SAGE) is not None,
      "the identifier IS present in a 46 B stub")
check(S.GRANT_TEXT.search(DIGITAL_SAGE) is None,
      "but no grant text is — so grant_text=NO is what distinguishes a 46 B stub "
      "from the 1 068 B full MIT text, and the bytes column is why it is printed")

# --- path casing, the defect that produced an overturn -----------------------
check("License" in S.LIC_PATHS and "license" in S.LIC_PATHS and "LICENSE" in S.LIC_PATHS,
      "the channel is case-sensitive: fsrs4anki-helper serves 'License'. All three "
      "casings must be probed or the absence is an artefact")

if fails:
    print(f"FAIL ({len(fails)})")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print(f"ok — {13 - len(fails)} checks, 0 failures")
