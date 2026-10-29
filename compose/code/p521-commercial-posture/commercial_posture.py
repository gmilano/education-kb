"""commercial_posture — the question `licence-grant-gate` does not answer.

`licence-grant-gate.verdict()` answers *"is a licence granted?"*. Pass 521 found that a
caller reading its `granted` boolean as *"may a paid engagement build on this?"* is wrong
for the two repositories pass 520 refused by hand:

    CaviraOSS/PageLM          -> family=MIT, granted=True   (actually: bespoke non-commercial,
                                                             redistribution prohibited,
                                                             revenue-share required)
    xiaoyang111222/cn-math... -> family=CC,  granted=True   (actually: CC BY-NC 4.0)

Both reads are reproducible; see README.md. The gate is not wrong about *grant*, it is
silent about *commercial posture*, and in education that is the axis that decides.

Two defect classes are handled here:

  (1) MIT-INCIPIT CAMOUFLAGE. A bespoke restricted grant may open with the verbatim MIT
      incipit ("Permission is hereby granted, free of charge, ...") and impose the
      restrictions further down. `family_of` reads only the title region (1200 chars), so
      the incipit wins and the restrictions are never seen. Fix: scan the WHOLE payload for
      restriction terms and let them OVERRIDE a permissive family read.

  (2) NON-COMMERCIAL FAMILY READ AS COMMERCIAL. `family="CC"` is not a posture: CC BY-4.0 is
      commercially usable, CC BY-NC-4.0 is not. Fix: resolve the CC variant, never the
      bare family.

Posture vocabulary (closed):
    PERMISSIVE  COPYLEFT  WEAK-COPYLEFT  NON-COMMERCIAL  BESPOKE-RESTRICTED  NOT-OSI  UNKNOWN
Only PERMISSIVE and the copyleft postures are buildable in a paid engagement; the copyleft
ones carry a reciprocity obligation that the engagement must accept explicitly.
"""

import re

BUILDABLE_PAID = {"PERMISSIVE", "COPYLEFT", "WEAK-COPYLEFT"}

# Terms that contradict a permissive reading wherever they appear in the payload.
# Each is a (pattern, label) pair so a refusal can cite the clause that caused it.
RESTRICTION_TERMS = [
    (r"\bnon-?commercial\b",                       "non-commercial limitation"),
    (r"\bNonCommercial\b",                         "CC NonCommercial element"),
    (r"revenue[- ]shar",                           "revenue-sharing requirement"),
    (r"\bCommercial Use\b",                        "defined term 'Commercial Use'"),
    (r"redistribution[^.]{0,80}strictly prohibited","redistribution prohibited"),
    (r"prior written (?:permission|consent)",      "prior-written-consent gate"),
    (r"may not be sold",                           "sale prohibited"),
    (r"\brevocable\b",                             "revocable grant"),
]

# Title-region families. Order matters: AGPL before GPL, because the GPLv3 body names the
# AGPL in section 13 and a body-wide grep misclassifies every GPLv3 payload as AGPL.
TITLE_FAMILIES = [
    ("AGPL-3.0",  ("GNU AFFERO GENERAL PUBLIC LICENSE",),      "COPYLEFT"),
    ("LGPL",      ("GNU LESSER GENERAL PUBLIC LICENSE",),      "WEAK-COPYLEFT"),
    ("GPL",       ("GNU GENERAL PUBLIC LICENSE",),             "COPYLEFT"),
    ("ECL-2.0",   ("Educational Community License",),          "PERMISSIVE"),
    ("MPL-2.0",   ("Mozilla Public License",),                 "WEAK-COPYLEFT"),
    ("Elastic",   ("Elastic License",),                        "NOT-OSI"),
    ("Apache-2.0",("Apache License",),                         "PERMISSIVE"),
]

# The title is on the opening lines, not merely "somewhere near the top". Two bounds matter:
#
#   * WINDOW. A 1200-character window is too generous — on a payload with a short preamble the
#     GPLv3's section 13 ("Use with the GNU Affero General Public License") can fall inside it.
#   * ORDER. Resolving family-by-family over the whole window lets a LATER line beat the title:
#     the AGPL probe matches section 13 even though line 1 reads "GNU GENERAL PUBLIC LICENSE".
#     So scan the title LINES IN ORDER and take the first line that matches any family.
#
# This is safe for the GNU pair because "GNU AFFERO GENERAL PUBLIC LICENSE" does not contain
# the substring "GNU GENERAL PUBLIC LICENSE" — the word AFFERO separates them. Pass 521's own
# suite caught both bounds; neither was hypothetical.
TITLE_LINES = 8


def _title_lines(text):
    return [l.lower() for l in text.splitlines() if l.strip()][:TITLE_LINES]


def _title_region(text):
    return "\n".join(_title_lines(text))


def family_from_title(text):
    """(family, posture) from the first title line that names a licence, else (None, None)."""
    for line in _title_lines(text):
        for family, probes, posture in TITLE_FAMILIES:
            if any(p.lower() in line for p in probes):
                return (family, posture)
    return (None, None)


def restrictions_in(text):
    """Every restriction term present in the payload, as (label, matched_text)."""
    out = []
    for pat, label in RESTRICTION_TERMS:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            out.append((label, m.group(0)))
    return out


def cc_variant(text):
    """Resolve a Creative Commons payload to its variant, or None if not CC."""
    head = _title_region(text)
    if "creative commons" not in head and "cc by" not in head:
        return None
    if re.search(r"noncommercial|non-commercial", text, re.IGNORECASE):
        return "CC-BY-NC"
    if re.search(r"sharealike", text, re.IGNORECASE):
        return "CC-BY-SA"
    return "CC-BY"


def posture_of(text):
    """(family, posture, reasons) for a licence payload.

    `posture` is the commercial answer. A restriction term anywhere in the payload
    downgrades a would-be PERMISSIVE read to BESPOKE-RESTRICTED.
    """
    if not text or not text.strip():
        return (None, "UNKNOWN", ["empty payload"])

    head = _title_region(text)
    restrictions = restrictions_in(text)

    cc = cc_variant(text)
    if cc:
        posture = "NON-COMMERCIAL" if cc == "CC-BY-NC" else "PERMISSIVE"
        if cc == "CC-BY-SA":
            posture = "WEAK-COPYLEFT"
        return (cc, posture, [l for l, _ in restrictions] or ["CC variant resolved from body"])

    family, posture = family_from_title(text)
    if family:
        # A titled OSI licence is not overridden by its own body wording.
        return (family, posture, ["title-line match"])

    # No recognised title. An MIT incipit alone is NOT enough if the body restricts.
    if "permission is hereby granted, free of charge" in text.lower():
        if restrictions:
            return ("BESPOKE-restricted", "BESPOKE-RESTRICTED",
                    [l for l, _ in restrictions])
        return ("MIT", "PERMISSIVE", ["MIT incipit, no restriction terms"])

    if "redistribution and use in source and binary" in text.lower():
        return ("BSD", "PERMISSIVE", ["BSD incipit"])
    if "this is free and unencumbered" in text.lower():
        return ("Unlicense", "PERMISSIVE", ["public-domain dedication"])

    return (None, "UNKNOWN", ["no recognised family"])


def buildable_in_paid_engagement(text):
    """(bool, family, posture, reasons) — the question a studio actually asks."""
    family, posture, reasons = posture_of(text)
    return (posture in BUILDABLE_PAID, family, posture, reasons)
