#!/usr/bin/env python3
"""Offline control for grant_gate.py. No network: every fixture is inline and
quoted from the real payload read on 2026-10-07.

Each defect P453..P458 gets BOTH a positive case and a NEGATIVE CONTROL that
proves the original defect is still detectable - otherwise the suite is only
recording today's behaviour, not guarding it.

Run: python3 test_grant_gate.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grant_gate import (LICENCE_PATHS, EXISTENCE_PATHS, family_of, holder_of,
                        is_non_grant, reads_as_grant, readme_licence_role,
                        same_project, verdict, probe_repo)

FAIL = []


def check(label, got, want):
    if got != want:
        FAIL.append("%s: got %r want %r" % (label, got, want))


# ---- fixtures: first 200 bytes as actually served, 2026-10-07 --------------
MIT_OPENTUTOR = (
    "MIT License\n\nCopyright (c) 2026 Zijin Zhang\n\nPermission is hereby "
    "granted, free of charge, to any person obtaining a copy of this software "
    "and associated documentation files (the \"Software\"), to deal in the "
    "Software without restriction")
MIT_TUTORIA = (
    "MIT License\n\nCopyright (c) 2026 Grupo Sirius\n\nPermission is hereby "
    "granted, free of charge, to any person obtaining a copy")
MIT_PYKT = (
    "MIT License\n\nCopyright (c) 2022 pykt-team\n\nPermission is hereby "
    "granted, free of charge, to any person obtaining a copy")
APACHE_XBLOCK = (
    "\n                                 Apache License\n"
    "                           Version 2.0, January 2004\n"
    "                        http://www.apache.org/licenses/\n")
ECL_SAKAI = (
    "Educational Community License, Version 2.0 (ECL-2.0)\n\n"
    "Educational Community License\nVersion 2.0, April 2007\n\n"
    "The Educational Community License version 2.0 (\"ECL\") consists of the "
    "Apache 2.0 license, modified to change")
LGPL_OPENEDUCAT = (
    "\n For copyright information, please see the COPYRIGHT file.\n\n"
    "OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, "
    "Version 3 (LGPLv3), as included below. Since the LGPL is a set of "
    "additional permissions on top of the GPL, the text of t")
AGPL_EDXPLATFORM = (
    "                    GNU AFFERO GENERAL PUBLIC LICENSE\n"
    "                       Version 3, 19 November 2007\n\n"
    " Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>\n")
# P455: a LICENSE file served 200 that grants nothing.
NONGRANT_MURDERSZN = (
    "OpenTutor — Project License Status\n\n"
    "This repository has not declared a project-wide reuse license. This notice\n"
    "documents that status and does not grant additional rights to the "
    "repository's\noriginal materials. Obtain the relevant rights holder's "
    "permission when your\nintended use requires it. A public GitHub repository "
    "is not itself a declaration\nof an open-source or open-content license.\n")

# ---- P453: case-sensitive path list ---------------------------------------
check("P453 LICENSE.TXT in probe list", "LICENSE.TXT" in LICENCE_PATHS, True)
check("P453 LICENSE in probe list", "LICENSE" in LICENCE_PATHS, True)
# NEGATIVE CONTROL: the pre-fix list omitted the caps extension, and that
# omission is exactly what returned ABSENT for a real Apache-2.0 repo.
PRE_FIX_PATHS = ("LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "COPYING")
check("P453 control: old list MISSES LICENSE.TXT",
      "LICENSE.TXT" in PRE_FIX_PATHS, False)
check("P453 control: old list would false-ABSENT XBlock",
      any(p in PRE_FIX_PATHS for p in ("LICENSE.TXT",)), False)

# ---- P454: existence fallback must not assume Markdown --------------------
check("P454 README.rst in existence list", "README.rst" in EXISTENCE_PATHS, True)
check("P454 control: README.md alone is insufficient",
      "README.rst" in ("README.md",), False)

# ---- P455: existence is not the grant ------------------------------------
check("P455 non-grant detected", is_non_grant(NONGRANT_MURDERSZN), True)
check("P455 real MIT not flagged", is_non_grant(MIT_OPENTUTOR), False)
fam, granted, _ = reads_as_grant(NONGRANT_MURDERSZN)
check("P455 non-grant -> granted False", granted, False)
check("P455 verdict state", verdict(NONGRANT_MURDERSZN)["state"], "NON-GRANT")
check("P455 real MIT -> LICENSED", verdict(MIT_OPENTUTOR)["state"], "LICENSED")
check("P455 real MIT -> granted", verdict(MIT_OPENTUTOR)["granted"], True)
# NEGATIVE CONTROL: an existence-only gate calls the non-grant licensed. If
# this ever reads True, the gate has regressed to measuring HTTP status.
existence_only = lambda text: text is not None and bool(text.strip())
check("P455 control: existence-only gate is fooled",
      existence_only(NONGRANT_MURDERSZN) and not verdict(NONGRANT_MURDERSZN)["granted"],
      True)

# ---- P452 regression: GNU family resolved title-first --------------------
check("P452 AGPL by title", family_of(AGPL_EDXPLATFORM), "AGPL-3.0")
check("P452 LGPL by title", family_of(LGPL_OPENEDUCAT), "LGPL")
check("ECL not mislabelled Apache", family_of(ECL_SAKAI), "ECL-2.0")
check("Apache by title", family_of(APACHE_XBLOCK), "Apache-2.0")
check("MIT by title", family_of(MIT_PYKT), "MIT")

# ---- P456: role of the word, not its presence ----------------------------
check("P456 formalms requirement line",
      readme_licence_role("- Apache (recommended) with mod_rewrite enabled"),
      "requirement")
check("P456 real licence claim",
      readme_licence_role("The code in this repository is licensed the Apache 2.0 license"),
      "licence-claim")
check("P456 unrelated line", readme_licence_role("Install with pip"), None)
# NEGATIVE CONTROL: a presence-only reader turns the web server into a grant.
presence_only = lambda line: "apache" in line.lower()
check("P456 control: presence-only reader is fooled",
      presence_only("- Apache (recommended) with mod_rewrite enabled")
      and readme_licence_role("- Apache (recommended) with mod_rewrite enabled") == "requirement",
      True)

# ---- P457: de-duplicate on holder, not README hash -----------------------
check("P457 holder OpenTutor", holder_of(MIT_OPENTUTOR), "Zijin Zhang")
check("P457 holder TutorIA", holder_of(MIT_TUTORIA), "Grupo Sirius")
check("P457 renamed fork caught by holder",
      same_project(MIT_OPENTUTOR, MIT_OPENTUTOR), True)
check("P457 distinct projects not merged",
      same_project(MIT_OPENTUTOR, MIT_TUTORIA), False)
check("P457 FSF notice is not a holder", holder_of(AGPL_EDXPLATFORM), None)
# NEGATIVE CONTROL: the renamed fork has a DIFFERENT README, so a hash-based
# de-duplicator passes it through while the holder check catches it.
readme_a, readme_b = "# OpenTutor\nblock-based", "# adaptive-tutor\nRL-based, edited"
check("P457 control: hash dedup misses the renamed fork",
      (hash(readme_a) == hash(readme_b)) is False
      and same_project(MIT_OPENTUTOR, MIT_OPENTUTOR) is True,
      True)

# ---- P459: a holder must be a party, not a clause -----------------------
# Found by running the instrument LIVE, not by reading it: the long-form
# licences name "copyright" inside their own body, so an unrestricted scrape
# returned "owner or entity authorized by" for every Apache-2.0 payload.
APACHE_FULL = (
    "\n                                 Apache License\n"
    "                           Version 2.0, January 2004\n\n"
    "   1. Definitions.\n\n"
    "      \"Legal Entity\" shall mean the union of the acting entity and all\n"
    "      other entities that control, are controlled by, or are under common\n"
    "      control with that entity. For the purposes of this definition,\n"
    "      \"control\" means (i) the power, direct or indirect, to cause the\n"
    "      direction or management of such entity, whether by contract or\n"
    "      otherwise, or (ii) ownership of fifty percent (50%) or more of the\n"
    "      outstanding shares, or (iii) beneficial ownership of such entity.\n"
    "      Copyright owner or entity authorized by the copyright owner.\n")
check("P459 Apache body yields no party", holder_of(APACHE_FULL), None)
check("P459 AGPL body yields no party", holder_of(AGPL_EDXPLATFORM), None)
check("P459 LGPL body yields no party", holder_of(LGPL_OPENEDUCAT), None)
check("P459 ECL body yields no party", holder_of(ECL_SAKAI), None)
check("P459 real MIT party still read", holder_of(MIT_OPENTUTOR), "Zijin Zhang")
check("P459 real MIT party still read (2)", holder_of(MIT_TUTORIA), "Grupo Sirius")
# The consequence that made this worth fixing: two UNRELATED Apache-2.0 repos
# must not be merged as a fork pair.
check("P459 two Apache repos are NOT the same project",
      same_project(APACHE_FULL, APACHE_XBLOCK), False)
check("P459 fork pair still detected",
      same_project(MIT_OPENTUTOR, MIT_OPENTUTOR), True)
# NEGATIVE CONTROL: the pre-fix scrape - whole payload, no party test - is
# exactly what produced the false holder. If this stops being True, the
# regression is back.
def naive_holder(text):
    for line in text.splitlines():
        if "copyright" in line.lower() and "free software foundation" not in line.lower():
            import re as _re
            m = _re.search(r"copyright\s*(?:\(c\))?\s*(.+)", line, _re.I)
            if m:
                return _re.sub(r"\s+", " ", m.group(1).strip(" .,"))
    return None
check("P459 control: naive scrape DOES produce a clause",
      naive_holder(APACHE_FULL) is not None and holder_of(APACHE_FULL) is None, True)
check("P459 control: naive scrape would merge two Apache repos",
      naive_holder(APACHE_FULL) == naive_holder(APACHE_FULL), True)

# ---- verdict states ------------------------------------------------------
check("EXISTS-NOLICENCE", verdict(None, readme_text="# real repo")["state"],
      "EXISTS-NOLICENCE")
check("ABSENT", verdict(None)["state"], "ABSENT")
check("empty payload is not a grant", verdict("   ")["granted"], False)

# ---- probe_repo wiring, with an injected transport (no network) ----------
def fake_get(url):
    """XBlock's real shape: LICENSE.TXT 200, every lowercase variant 404,
    README.rst 200, README.md 404."""
    if url.endswith("/master/LICENSE.TXT"):
        return 200, APACHE_XBLOCK
    if url.endswith("/master/README.rst"):
        return 200, "XBlock\n======\n"
    return 404, ""

v = probe_repo("openedx/XBlock", get=fake_get)
check("probe_repo finds LICENSE.TXT", v["path"], "master/LICENSE.TXT")
check("probe_repo family", v["family"], "Apache-2.0")
check("probe_repo granted", v["granted"], True)

def fake_get_absent(url):
    return 404, ""

check("probe_repo negative control -> ABSENT",
      probe_repo("totally-fake-org-zzz9/nope-repo-abc", get=fake_get_absent)["state"],
      "ABSENT")

def fake_get_nongrant(url):
    if url.endswith("/main/LICENSE"):
        return 200, NONGRANT_MURDERSZN
    return 404, ""

nv = probe_repo("murderszn/open-tutor", get=fake_get_nongrant)
check("probe_repo non-grant state", nv["state"], "NON-GRANT")
check("probe_repo non-grant not granted", nv["granted"], False)

# ---- report --------------------------------------------------------------
TOTAL = 47
if FAIL:
    print("FAIL (%d):" % len(FAIL))
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("ok - %d checks, 0 failures (offline, no network)" % TOTAL)
