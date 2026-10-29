"""family_resolution — the SPDX cell `commercial_posture` cannot fill.

WHY THIS EXISTS (p522)
======================
`p521` shipped `commercial_posture` to answer the question `licence-grant-gate` is silent
about: *may a paid engagement build on this?* That instrument answers its question
correctly — this pass re-ran it over seven payloads read from bytes today and every
POSTURE verdict was right (see README.md, "p521 re-run").

🔴 Two FAMILY cells are wrong, and the shelves publish family cells to clients:

    GeminiLight/gen-mentor    7 048 B  CC0-1.0   -> commercial_posture says family "CC-BY"
    portabilis/i-educar      18 092 B  GPL-2.0   -> commercial_posture says family "GPL"

Both are reproducible; both are one `python3` invocation away in the suite beside this file.

WHY EACH ONE COSTS SOMETHING
----------------------------
1. CC0-1.0 READ AS CC-BY. `cc_variant()` keys on "creative commons" in the title region and
   then resolves only the -NC / -SA elements, falling through to "CC-BY". CC0 1.0 is a
   PUBLIC-DOMAIN DEDICATION: no attribution duty at all. Publishing it as CC-BY invents an
   attribution obligation the grantor explicitly waived, and — in the other direction — a
   genuinely CC-BY asset becomes indistinguishable from a dedicated one. The KB's own shelf
   records this repository as CC0-1.0 BY HAND (`agents/trending.md`); the instrument
   contradicts the shelf.

2. GPL WITHOUT A VERSION. `TITLE_FAMILIES` maps every "GNU GENERAL PUBLIC LICENSE" title to
   the bare family "GPL". GPL-2.0-only and GPL-3.0 differ on the one question an education
   engagement asks: GPL-2.0-only is INCOMPATIBLE with Apache-2.0 (patent/termination terms),
   GPL-3.0 is compatible. `portabilis/i-educar` — this base's LATAM municipal-SIS row — is
   GPL-2.0, so "can we combine the SIS with our Apache-2.0 components?" is answerable from
   the payload and NOT answerable from the published cell.

WHAT THIS MODULE ADDS, AND WHAT IT DELIBERATELY DOES NOT
--------------------------------------------------------
It resolves FAMILY to an SPDX-shaped identifier, including the version, and it reports
posture using p521's vocabulary plus one value p521 lacks: PUBLIC-DOMAIN. It does not
re-implement p521's restriction scan — `commercial_posture.restrictions_in()` is correct and
is imported where available. Composition, not replacement.

THE SUBSTRING TRAP, MEASURED THIS PASS
--------------------------------------
🔵 p521's lesson is "scan the WHOLE payload for restriction terms". That is right, and it is
only safe with word boundaries. A first-cut scan written for this pass WITHOUT them flagged
the four most permissive grant families in the sector, every hit quoted from served bytes:

    Apache-2.0 "...royalty-free, irrevocable copyright license..."        -> "revocable grant"
    CC0-1.0    "...non exclusive, irrevocable and unconditional license"  -> "revocable grant"
    GPL-3.0    "...allowed only occasionally and noncommercially..."      -> "non-commercial"
    AGPL-3.0   (the same GPL section 6 sentence)                          -> "non-commercial"

In every case the matched word is the GRANT'S STRENGTH or a PERMISSION, read as a
restriction. p521's `\b` anchors already prevent all four; NEGATION_GUARDS below exist so a
later pass cannot quietly drop them, and the suite asserts the four payloads stay clean.
"""

import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                os.pardir, "p521-commercial-posture"))
try:                                      # composition, not replacement
    import commercial_posture as _cp
except Exception:                          # the module must still answer offline
    _cp = None

# Posture vocabulary: p521's, plus PUBLIC-DOMAIN. Only these are buildable in paid work.
BUILDABLE_PAID = {"PERMISSIVE", "PUBLIC-DOMAIN", "COPYLEFT", "WEAK-COPYLEFT"}

# Words whose LONGER form is a permission or a grant strength. Each pair is
# (trap_substring, the_word_that_contains_it) and the suite proves each one bites.
NEGATION_GUARDS = [
    ("revocable", "irrevocable"),       # Apache-2.0, CC0-1.0, GPL-3.0 section 2
    ("commercial", "noncommercially"),  # GPL-3.0 / AGPL-3.0 section 6
]

# Version lines, probed INSIDE the payload rather than in the title region: the GNU titles
# carry no version, the line beneath them does.
GNU_VERSIONS = [
    # 🔴 AGPL-3.0 and GPL-3.0 are both "Version 3" and their DATES differ. A probe carrying
    # only the GPL date leaves every AGPL payload at "AGPL-?" — p522's suite caught exactly
    # that on artcc/freelingo (34 514 B).
    (r"Version 3, 19 November 2007", "3.0"),
    (r"Version 3, 29 June 2007", "3.0"),
    (r"Version 2\.1, February 1999", "2.1"),
    (r"Version 2, June 1991", "2.0"),
    (r"Version 1\.3", "1.3"),
]

# CC variants, MOST RESTRICTIVE FIRST. The order is the safety property: where a payload
# carries two elements, the restrictive one must win, because the cost of the two errors is
# not symmetric — passing an -NC asset into paid work is unrecoverable, calling a CC0 asset
# CC-BY is merely wrong.
#
# 🔴 CC0 IS LAST, AND IT IS RESOLVED FROM THE TITLE REGION ONLY. Creative Commons prints
# this sentence in the boilerplate of EVERY 4.0 payload:
#
#   "the text of the Creative Commons public licenses is dedicated to the public domain
#    under the CC0 Public Domain Dedication."
#
# It dedicates the LICENCE TEXT, not the licensed work. A whole-payload `\bCC0\b` probe
# therefore reads CC BY-NC 4.0 — and every other 4.0 variant — as a public-domain
# dedication. p522's first draft did exactly that and passed `cn-math-taxonomy`, the asset
# p520 refused by hand. The positive control caught it; see README.md.
CC_ELEMENTS = [
    (r"Attribution-NonCommercial-ShareAlike", "CC-BY-NC-SA-4.0", "NON-COMMERCIAL"),
    (r"Attribution-NonCommercial-NoDerivatives", "CC-BY-NC-ND-4.0", "NON-COMMERCIAL"),
    (r"Attribution-NonCommercial", "CC-BY-NC-4.0", "NON-COMMERCIAL"),
    (r"\bNonCommercial\b|\bnon-?commercial\b", "CC-BY-NC-4.0", "NON-COMMERCIAL"),
    (r"Attribution-NoDerivatives", "CC-BY-ND-4.0", "NOT-OSI"),
    (r"\bNoDerivatives\b", "CC-BY-ND-4.0", "NOT-OSI"),
    (r"Attribution-ShareAlike", "CC-BY-SA-4.0", "WEAK-COPYLEFT"),
    (r"\bShareAlike\b", "CC-BY-SA-4.0", "WEAK-COPYLEFT"),
    (r"CC0 1\.0 Universal|\bCC0\b", "CC0-1.0", "PUBLIC-DOMAIN"),
    (r"Creative Commons Attribution", "CC-BY-4.0", "PERMISSIVE"),
    (r"Attribution 4\.0 International|\bCC[- ]BY[- ]4\.0\b", "CC-BY-4.0", "PERMISSIVE"),
]

# The boilerplate sentence above, stripped before any body-wide CC probe.
# 🔴 Joined on `\s+`, not spaces. As served, the sentence is wrapped across four lines
# ("...the Creative Commons\npublic licenses is dedicated to the public domain under the CC0
# Public\nDomain Dedication."), so a literal-space pattern matches NOTHING in the payloads it
# exists for. p522 wrote it with spaces first; the suite caught it.
CC_TEXT_DEDICATION = re.compile(
    r"\s+".join("the text of the Creative Commons public licenses is dedicated to the "
                "public domain under the CC0 Public Domain Dedication".split()) + r"\.?",
    re.IGNORECASE)

# Titled families that need no version probe.
FLAT_FAMILIES = [
    (r"Apache License", "Apache-2.0", "PERMISSIVE"),
    (r"Educational Community License", "ECL-2.0", "PERMISSIVE"),
    (r"Mozilla Public License", "MPL-2.0", "WEAK-COPYLEFT"),
    (r"Elastic License", "Elastic-2.0", "NOT-OSI"),
    (r"Business Source License", "BUSL-1.1", "NOT-OSI"),
    (r"Server Side Public License", "SSPL-1.0", "NOT-OSI"),
]

TITLE_LINES = 8


def title_lines(text):
    """The opening non-blank lines — p521's bound, kept deliberately identical.

    The window matters: a generous character window lets GPLv3 section 13 ("Use with the GNU
    Affero General Public License") beat the title line. p521 found that; this does not
    re-find it.
    """
    return [l.strip() for l in text.splitlines() if l.strip()][:TITLE_LINES]


def guard_hits(text):
    """Substring traps present in this payload, as (trap, containing_word, count).

    Reported, never acted on: the point is that a scan WITHOUT word boundaries would act.
    """
    out = []
    low = text.lower()
    for trap, word in NEGATION_GUARDS:
        n = low.count(word)
        if n:
            out.append((trap, word, n))
    return out


def _gnu_version(text):
    for pat, ver in GNU_VERSIONS:
        if re.search(pat, text):
            return ver
    return None


def resolve(text):
    """Resolve a licence payload to (family, posture, evidence).

    `family` is SPDX-shaped and carries the version wherever the payload states one.
    `evidence` names the line or clause the verdict was read from, so a cell can be audited
    without re-fetching.
    """
    if not text or not text.strip():
        return (None, "UNKNOWN", ["empty payload"])

    titles = title_lines(text)
    head = "\n".join(titles)
    head_low = head.lower()

    # --- GNU first: these are the families whose title omits the version ------------------
    for probe, fam, posture in ((r"GNU AFFERO GENERAL PUBLIC LICENSE", "AGPL", "COPYLEFT"),
                                (r"GNU LESSER GENERAL PUBLIC LICENSE", "LGPL", "WEAK-COPYLEFT"),
                                (r"GNU GENERAL PUBLIC LICENSE", "GPL", "COPYLEFT")):
        for line in titles:                       # title LINES in order, never a window
            if re.search(probe, line, re.IGNORECASE):
                ver = _gnu_version(text)
                fam_full = "%s-%s" % (fam, ver) if ver else fam + "-?"
                ev = ["title line: %s" % line]
                ev.append("version line resolved: %s" % ver if ver
                          else "NO version line found — family left explicitly unresolved")
                return (fam_full, posture, ev)

    # --- Creative Commons: TITLE REGION first, then the de-boilerplated body -------------
    if "creative commons" in head_low or "cc by" in head_low or re.search(r"\bCC0\b", head):
        # The boilerplate is stripped from BOTH regions: on a short human-readable notice it
        # falls inside the 8-line title window, so stripping only the body is not enough.
        for region, where in ((CC_TEXT_DEDICATION.sub(" ", head), "title region"),
                              (CC_TEXT_DEDICATION.sub(" ", text), "body, CC0 boilerplate stripped")):
            for pat, fam, posture in CC_ELEMENTS:
                m = re.search(pat, region, re.IGNORECASE)
                if m:
                    return (fam, posture,
                            ["CC element %r matched in %s" % (m.group(0), where)])
        return ("CC-?", "UNKNOWN",
                ["Creative Commons payload with no resolvable element — do NOT publish a "
                 "variant cell for it"])

    # --- flat titled families -------------------------------------------------------------
    for pat, fam, posture in FLAT_FAMILIES:
        for line in titles:
            if re.search(pat, line, re.IGNORECASE):
                return (fam, posture, ["title line: %s" % line])

    # --- incipit families. A restricted grant may OPEN with the MIT sentence (p521) -------
    low = text.lower()
    restrictions = []
    if _cp is not None:
        restrictions = [label for label, _ in _cp.restrictions_in(text)]

    if "permission is hereby granted, free of charge" in low:
        if restrictions:
            return ("BESPOKE-restricted", "BESPOKE-RESTRICTED", restrictions)
        return ("MIT", "PERMISSIVE", ["MIT incipit, no restriction terms"])

    if "redistribution and use in source and binary" in low:
        fam = "BSD-3-Clause" if "neither the name" in low else "BSD-2-Clause"
        # BSD-3's no-endorsement clause contains "prior written permission". It is a
        # TRADEMARK clause, not a commercial gate, so the posture is not downgraded here.
        return (fam, "PERMISSIVE", ["BSD incipit", "no-endorsement clause is not a gate"])

    if "this is free and unencumbered software released into the public domain" in low:
        return ("Unlicense", "PUBLIC-DOMAIN", ["Unlicense incipit"])

    if restrictions:
        return ("BESPOKE-restricted", "BESPOKE-RESTRICTED", restrictions)

    return (None, "UNKNOWN", ["no recognised family"])


def buildable_in_paid_engagement(text):
    """(bool, family, posture, evidence) — the studio's question, with an SPDX cell."""
    fam, posture, ev = resolve(text)
    return (posture in BUILDABLE_PAID, fam, posture, ev)


def disagreement_with_p521(text):
    """(p522_family, p521_family) where the two instruments differ, else None.

    This exists so the disagreement stays MEASURED rather than asserted in prose: a later
    pass that fixes `commercial_posture` will see this return None and can retire the patch.
    """
    if _cp is None:
        return None
    mine, _, _ = resolve(text)
    theirs, _, _ = _cp.posture_of(text)
    return None if mine == theirs else (mine, theirs)
