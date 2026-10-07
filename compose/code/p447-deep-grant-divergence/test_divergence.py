#!/usr/bin/env python3
"""Controls for p444.  Runs offline: no clone, no fetch.

Every positive is paired with a negative that must NOT move, because this pass's own
rule (`is_own_grant`) narrows a bucket the pass pre-registered a prediction over, and a
narrowing rule with no negative control is indistinguishable from tuning to the answer.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from divergence import (  # noqa: E402
    COPYLEFT, PERMISSIVE, THIRD_PARTY_NAME_RE, is_own_grant,
)
sys.path.insert(0, os.path.join(HERE, "..", "p436-fork-hypothesis"))
sys.path.insert(0, os.path.join(HERE, "..", "p441-tree-licence-enumeration"))
from sweep_payload import family_of  # noqa: E402
from enumerate_licence import family_marks, is_grant_path, is_own_path  # noqa: E402

ok = 0
bad = []


def check(label, got, want):
    global ok
    if got == want:
        ok += 1
    else:
        bad.append("%s: got %r want %r" % (label, got, want))


# ---------------------------------------------------------------------------
# 1. the defect this pass found in its OWN first build: a third-party notice at
#    root depth was published as the project's second grant
# ---------------------------------------------------------------------------
# POSITIVE: the real path that caused it, from dequelabs/axe-core
check("axe-core 3rd-party notice is NOT an own grant",
      is_own_grant("LICENSE-3RD-PARTY.txt"), False)
# and the defect stays DETECTABLE: the old rule still calls it own, so if someone
# reverts is_own_grant to is_own_path this assertion is what fails
check("the OLD rule still mis-files it (defect remains detectable)",
      is_own_path("LICENSE-3RD-PARTY.txt"), True)

# more spellings of the same disclaimer
for p in ("THIRD-PARTY-LICENSES.txt", "third_party_licence.txt", "NOTICE",
          "LICENSE.dependencies", "licenses/ATTRIBUTION.txt", "CREDITS",
          "ACKNOWLEDGEMENTS.md", "LICENSE-vendor.txt", "bundled-LICENSE"):
    check("disclaimed by name: %s" % p, is_own_grant(p), False)

# NEGATIVES that must still count as the project's own grant -- this is the half that
# proves the rule is not just "reject anything with a hyphen"
for p in ("LICENSE", "LICENSE.TXT", "licence", "COPYING", "COPYING.LESSER",
          "LICENSE.md", "aoe-web-backend/LICENSE", "debian/copyright",
          "LICENSE-MIT", "LICENSE-APACHE", "docs/LICENSE"):
    check("own grant survives the rule: %s" % p, is_own_grant(p), True)

# `LICENSE-MIT` / `LICENSE-APACHE` are the DUAL-LICENSED spelling and must survive:
# they are the tier the pre-registration expects divergence to concentrate in, so a
# rule that silently ate them would have hidden the finding.
check("dual-licence pair is two own grants",
      (is_own_grant("LICENSE-MIT"), is_own_grant("LICENSE-APACHE")), (True, True))

# depth still governs: four levels into a static tree is nobody's own grant
check("deep vendored path rejected by depth",
      is_own_grant("public/javascripts/fckeditor/license.txt"), False)
check("owl2shacl path rejected by depth",
      is_own_grant("src/ontology/utils/owl2shacl/LICENSE"), False)

# ---------------------------------------------------------------------------
# 2. the regex must not fire on words that merely CONTAIN a token
# ---------------------------------------------------------------------------
# "licence" contains no listed token; these are the false-positive traps.
check("no match on plain LICENSE", bool(THIRD_PARTY_NAME_RE.search("LICENSE")), False)
check("no match on COPYING", bool(THIRD_PARTY_NAME_RE.search("COPYING")), False)
# but 'dependenc' is deliberately a stem so it catches both spellings
check("dependencies caught", bool(THIRD_PARTY_NAME_RE.search("LICENSE.dependencies")),
      True)
check("dependency caught", bool(THIRD_PARTY_NAME_RE.search("dependency-LICENSE")),
      True)

# ---------------------------------------------------------------------------
# 3. family_of corrections from pass 26 must hold, since stage 0 rests on them
# ---------------------------------------------------------------------------
MPL_HEAD = ("Mozilla Public License Version 2.0\n\n1.12. \"Secondary License\"\n"
            "means either the GNU General Public License, Version 2.0, the GNU Lesser\n"
            "General Public License, Version 2.1, the GNU Affero General Public\n"
            "License, Version 3.0")
check("MPL-2.0 naming three GNU families classifies MPL", family_of(MPL_HEAD),
      "MPL-2.0")
check("...and family_marks COUNTS all four", set(family_marks(MPL_HEAD)),
      {"MPL", "GPL", "LGPL", "AGPL"})
# the line-wrapped copy that chose GPL over LGPL in pass 26
MPL_WRAPPED = MPL_HEAD.replace("GNU Lesser\nGeneral", "GNU Lesser\n   General")
check("line wrapping no longer decides the verdict", family_of(MPL_WRAPPED), "MPL-2.0")

# NEGATIVE: a real GNU payload must NOT be dragged to MPL by the reordering
GPL_HEAD = ("GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007\n\n"
            "Copyright (C) 2007 Free Software Foundation, Inc.")
check("plain GPL stays GPL", family_of(GPL_HEAD), "GPL")
check("plain GPL names one family", family_marks(GPL_HEAD), ["GPL"])
AGPL_HEAD = "GNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3, 19 November 2007"
check("plain AGPL stays AGPL", family_of(AGPL_HEAD), "AGPL-3.0")

# The real EUPL-1.2 Appendix, spelled as the European Commission spells it -- British
# "Licence" on the Mozilla line, and every name WRAPPED, which is the p445 case.  The
# first draft of this control invented an appendix listing SPDX ids (`GPL-2.0`,
# `MPL-2.0`), which no `_MARKS` pattern matches, and so asserted a fiction.
EUPL_HEAD = ("EUROPEAN UNION PUBLIC LICENCE v. 1.2\n"
             "EUPL (c) the European Union 2007, 2016\n\n"
             "Appendix\n\n'Compatible Licences' according to Article 5 EUPL are:\n"
             "- GNU General Public License (GNU GPL) v. 2\n"
             "- GNU Affero General Public\n  License (GNU AGPL) v. 3\n"
             "- Eclipse Public\n  License (EPL) v. 1.0\n"
             "- Mozilla Public Licence\n  (MPL) v. 2\n"
             "- GNU Lesser General Public\n  Licence (LGPL) v. 2.1, v. 3\n"
             "- Creative Commons Attribution-ShareAlike v. 3.0\n")
check("EUPL naming five families classifies EUPL", family_of(EUPL_HEAD), "EUPL")
check("...and marks count them all despite wrapping",
      set(family_marks(EUPL_HEAD)),
      {"EUPL", "GPL", "AGPL", "LGPL", "MPL", "EPL", "CC"})

# ---------------------------------------------------------------------------
# 3b. P447 -- the flattening fix itself, with the negatives that bound it
# ---------------------------------------------------------------------------
# POSITIVE: the exact real bytes that exposed it, from axe-core lines 74-76
AXE = ('1.12. "Secondary License"\n\n'
       '      means either the GNU General Public License, Version 2.0, the GNU Lesser\n'
       '      General Public License, Version 2.1, the GNU Affero General Public\n'
       '      License, Version 3.0, or any later versions of those licenses.\n')
check("P447: wrapped LGPL and AGPL are now both counted",
      set(family_marks("Mozilla Public License Version 2.0\n" + AXE)),
      {"MPL", "GPL", "LGPL", "AGPL"})

# NEGATIVE 1: the fix must be a no-op on text that does not wrap.  If flattening
# changed an already-flat payload's answer it would be adding matches, not recovering
# them.
FLAT = ("mozilla public license version 2.0 means either the gnu general public "
        "license, version 2.0, the gnu lesser general public license, version 2.1, "
        "the gnu affero general public license, version 3.0")
check("P447 is a no-op on unwrapped text", set(family_marks(FLAT)),
      {"MPL", "GPL", "LGPL", "AGPL"})

# NEGATIVE 2: flattening must not BRIDGE two unrelated paragraphs into a family that
# neither one names.  "...the GNU" ending one paragraph and "General Public License"
# opening the next is the adversarial case, and it is a TRUE match for GPL by any
# reading -- so the honest negative is the one below: a payload that names NO family
# must still name none after flattening, however it is wrapped.
NONE = ("Copyright (c) 2026 Example Org\n\n   All\n rights\n reserved.\n"
        "   See\n the\n documentation\n for\n terms.\n")
check("P447 invents no family in a payload that names none",
      family_marks(NONE), [])

# NEGATIVE 3: a single-family payload stays single after flattening -- the undercount
# fix must not inflate the >1 bucket that action B's prediction is scored on.
check("P447 keeps a plain GPL payload at one family",
      family_marks("GNU GENERAL PUBLIC LICENSE\n   Version 3,\n 29 June 2007\n"),
      ["GPL"])
check("P447 keeps a plain MIT payload at one family",
      family_marks("MIT License\n\nPermission is hereby granted,\n free of charge,"
                   " to any\n person obtaining a copy\n"), ["MIT"])

# ---------------------------------------------------------------------------
# 3c. P452 -- the GNU family read from the TITLE, not from the window
# ---------------------------------------------------------------------------
# POSITIVE: a real GPL-2.0 payload.  Its Preamble recommends the LGPL ~790 chars in,
# which is why the 4000-char window returned LGPL for all seven GPL-2.0 rows on this
# shelf.  The title says what it is.
GPL2 = ("                    GNU GENERAL PUBLIC LICENSE\n"
        "                       Version 2, June 1991\n\n"
        " Copyright (C) 1989, 1991 Free Software Foundation, Inc.\n\n"
        "  Preamble\n\n"
        + ("  The licenses for most software are designed to take away your freedom "
           "to share and change it. " * 6)
        + "\n  [This is the point where GPL-2.0 recommends the GNU Lesser General "
          "Public License instead of this License.]\n")
check("P452: a GPL-2.0 payload is GPL, not LGPL", family_of(GPL2), "GPL")
# the defect must stay DETECTABLE: the LGPL string really is inside the old window
check("...and the LGPL cross-reference really is in the old 4000-char window",
      "gnu lesser general public license" in GPL2[:4000].lower(), True)

# NEGATIVE 1: a genuine LGPL-2.1 payload must still be LGPL
LGPL21 = ("                  GNU LESSER GENERAL PUBLIC LICENSE\n"
          "                       Version 2.1, February 1999\n\n"
          " Copyright (C) 1991, 1999 Free Software Foundation, Inc.\n")
check("P452 negative: real LGPL-2.1 stays LGPL", family_of(LGPL21), "LGPL")

# NEGATIVE 2: LGPL-3.0 opens with the FSF copyright line and names the GPL 90 chars
# after it names itself -- `untisapi/untis4j` is this shape and is correct today
LGPL30 = ("                   GNU LESSER GENERAL PUBLIC LICENSE\n"
          "                       Version 3, 29 June 2007\n\n"
          " Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>\n\n"
          "  This version of the GNU Lesser General Public License incorporates the\n"
          "terms and conditions of version 3 of the GNU General Public License.\n")
check("P452 negative: LGPL-3.0 stays LGPL though it names the GPL", family_of(LGPL30),
      "LGPL")

# NEGATIVE 3: a GPL-3.0 payload (correct BEFORE the fix) must not move
GPL30 = ("                    GNU GENERAL PUBLIC LICENSE\n"
         "                       Version 3, 29 June 2007\n\n"
         " Copyright (C) 2007 Free Software Foundation, Inc.\n")
check("P452 negative: GPL-3.0 unchanged", family_of(GPL30), "GPL")

# NEGATIVE 4: AGPL must still win over both
AGPL30 = ("                 GNU AFFERO GENERAL PUBLIC LICENSE\n"
          "                   Version 3, 19 November 2007\n")
check("P452 negative: AGPL-3.0 unchanged", family_of(AGPL30), "AGPL-3.0")

# NEGATIVE 5: a prose grant with NO title block must still resolve by the wide window.
# `openeducat/openeducat_erp` is this shape ("OpenEduCat is published under the GNU
# Lesser General Public License, version 3"), and so is `espoon-voltti/evaka`, whose
# REUSE notice names the LGPL 656 characters in with no title at all.
NOTITLE = ("For copyright information, please see the COPYRIGHT file. OpenEduCat is\n"
           "published under the GNU Lesser General Public License, version 3\n"
           "(LGPLv3), as published by the Free Software Foundation.\n")
check("P452 negative: a titleless prose grant still resolves", family_of(NOTITLE),
      "LGPL")
# and the wide-window fallback is what does it, so it must not have been deleted
check("...the wide window is still reachable (fallback retained)",
      family_of("x" * 500 + "\nthis is under the gnu affero general public license\n"),
      "AGPL-3.0")

# NEGATIVE 6: MPL/EUPL are probed BEFORE the GNU block and must be unaffected by it
check("P452 negative: MPL still beats the GNU marks", family_of(MPL_HEAD), "MPL-2.0")
check("P452 negative: EUPL still beats the GNU marks", family_of(EUPL_HEAD), "EUPL")

# ---------------------------------------------------------------------------
# 4. the commercial axis is a PARTITION over what family_of can return
# ---------------------------------------------------------------------------
check("axis buckets are disjoint", PERMISSIVE & COPYLEFT, set())
RETURNABLE = {"EUPL", "MPL-2.0", "EPL", "AGPL-3.0", "LGPL", "GPL", "Apache-2.0",
              "ECL-2.0", "MIT", "BSD", "ISC", "CC0-1.0", "CC-BY", "Unlicense",
              "MulanPSL"}
check("axis covers every family family_of can return",
      RETURNABLE - (PERMISSIVE | COPYLEFT), set())
# UNKNOWN must be in NEITHER bucket: an unreadable payload is not permissive
check("UNKNOWN is not permissive", "UNKNOWN" in PERMISSIVE, False)
check("UNKNOWN is not copyleft", "UNKNOWN" in COPYLEFT, False)

# ---------------------------------------------------------------------------
# 5. is_grant_path inherited behaviour -- the badge and the icon stay rejected
# ---------------------------------------------------------------------------
check("EUPL README badge is not a grant path",
      is_grant_path("edci-issuer/licence-EUPL 1.2-brightgreen.svg"), False)
check("icon component is not a grant path",
      is_grant_path("lib/KIcon/material-icons/copyright/baseline.vue"), False)
check("node_modules grant excluded",
      is_grant_path("node_modules/foo/LICENSE"), False)
check("LICENSE.TXT IS a grant path", is_grant_path("LICENSE.TXT"), True)
check("licences inventory json is not a grant path",
      is_grant_path("licenses.json"), False)

print("p447 controls: %d/%d" % (ok, ok + len(bad)))
for b in bad:
    print("  FAIL", b)
sys.exit(1 if bad else 0)
