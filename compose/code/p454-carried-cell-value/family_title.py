#!/usr/bin/env python3
"""p454 -- the licence-family reader, rebuilt twice in one pass, because the
first rebuild had its own ordering defect.

### Defect 1 (inherited, MEASURED here): the 40-line window is unsound

Gap 450-C defect (a) was: a whole-body grep calls every GPLv3 payload LGPL,
because GPLv3's closing "How to Apply" section recommends the LGPL. p450's
remedy, carried in `p453-vocabulary-ledger/verify.py::family`, truncates to the
first 40 NON-EMPTY lines.

That remedy is unsound, and this pass measured the failure first-hand: GPLv2's
PREAMBLE recommends the LGPL at non-empty line 15 --

    "(Some other Free Software Foundation software is covered by
     the GNU Lesser General Public License instead.)"

-- INSIDE the window. So the window fixes GPLv3 and breaks GPLv2, and the
defect stayed invisible because it was only ever validated on the version whose
mention falls outside the window. Measured cost over 179 carried payloads:
1 (`oat-sa/tao-core`, GPL-2.0 served, graded LGPL).

The sound anchor is the TITLE BLOCK: a licence names itself in its first
non-empty line. Nothing in a preamble or appendix can reach it.

### Defect 2 (this pass's own): single-family checks ran BEFORE the composite check

The first cut of this file placed its COMPOSITE check last, so a two-section
notice graded as whichever family it happened to mention first:
`bncc-dev/bncc-pacotes` serves a notice reading "Codigo -- MIT" / "Dados
embutidos -- CC BY 4.0" and graded `CC-BY`, silently discarding the MIT half.
And the heuristic itself was wrong -- it keyed on MARKDOWN HEADING COUNT, so it
fired on `nakafaai/aksara`, whose payload is a single bespoke licence that
merely has fifteen numbered sections.

A composite is TWO OR MORE DISTINCT FAMILIES NAMED, never a heading count.

### The class both defects were hiding: a payload that is not a licence at all

`nakafaai/aksara` serves "Nakafa Source Available License 2.0", whose own second
sentence is *"It is not open source, and it is not free to reuse."* Both readers
before this one graded it `UNREAD`. On a shelf, `UNREAD` reads as "grant not
determined" and INVITES a later pass to promote it. That is the most expensive
direction a licence reader can fail in, so it gets its own verdict class.
"""
import re

FAMILY_TOKENS = [
    ("AGPL-3.0",     r"gnu affero general public license|\bagpl\b"),
    ("LGPL",         r"gnu lesser general public license|\blgpl\b"),
    ("GPL",          r"gnu general public license|\bgplv?[23]\b"),
    ("Apache-2.0",   r"apache license.{0,40}version 2\.0|\bapache-2\.0\b"),
    ("MIT",          r"\bmit license\b|licen[cs]ed? (?:under|sob) (?:the )?mit|— mit|-- mit"),
    ("BSD",          r"\bbsd[- ][23][- ]clause\b"),
    ("ISC",          r"\bisc license\b"),
    ("MPL-2.0",      r"mozilla public license"),
    ("CC0-1.0",      r"cc0 1\.0 universal|\bcc0\b"),
    ("CC-BY",        r"creative commons attribution|\bcc[- ]by\b"),
    ("ODbL",         r"open data commons|\bodbl\b"),
    ("Unlicense",    r"the unlicense"),
]

# A payload that REFUSES permission. "All rights reserved" is NOT in this set:
# it is the standard opening line of thousands of MIT and BSD payloads
# (`davepacheco/node-extsprintf` serves exactly that, then grants MIT in the
# next sentence), and this pass's own first cut of the NOT-OSI class graded it
# NOT-OSI on that line alone -- a false positive in the one direction that
# matters, because it would have condemned a genuinely permissive dependency.
# This list is NOT the discriminator, and this pass learned why: Nakafa's
# CONTENT_LICENSE refuses permission as "not public domain, not open content,
# and not free material", which no enumeration this pass wrote anticipated. A
# refusal vocabulary cannot be enumerated -- there are unboundedly many ways to
# say no. It is kept only as a second arm for UNTITLED payloads (`asherlc/dofek`
# opens on a bare copyright line, not a title).
NOT_OPEN = re.compile(
    r"not open source|source available|no permission is granted|"
    r"may not be used|not free to reuse|viewing and reference purposes only|"
    r"not public domain|not open content|not free material|"
    r"noncommercial|non-commercial|no commercial use", re.I)

# THE discriminator. A payload whose TITLE names itself a licence, policy or
# terms, and which contains no affirmative grant anywhere in its head, is a
# bespoke instrument by construction -- no enumeration of refusals required.
BESPOKE_TITLE = re.compile(r"licen[cs]e|policy|terms|agreement", re.I)

# The grant forms that AFFIRM permission. If one of these is present the
# payload is a licence, whatever boilerplate precedes it, and the NOT-OSI test
# must not run.
PERMISSIVE_GRANT = re.compile(
    r"permission is hereby granted, free of charge|"
    r"redistribution and use in source and binary forms|"
    r"permission to use, copy, modify, and/or distribute|"
    r"apache license|gnu (?:affero |lesser )?general public license|"
    r"mozilla public license|creative commons|cc0 1\.0 universal|the unlicense",
    re.I)

OSI_TITLES = re.compile(
    r"gnu (?:affero |lesser )?general public license|apache license|mit license|"
    r"bsd|isc license|mozilla public license|creative commons|cc0|the unlicense|"
    r"eclipse public license|european union public licence|eupl", re.I)


def title_block(text, lines=3):
    return "\n".join([l.strip() for l in text.splitlines() if l.strip()][:lines])


def head40(text):
    return "\n".join([l for l in text.splitlines() if l.strip()][:40])


def families_named(text):
    """Distinct families NAMED anywhere in the head. Order-stable."""
    h = head40(text).lower()
    out = []
    for name, pat in FAMILY_TOKENS:
        if re.search(pat, h) and name not in out:
            out.append(name)
    return out


# An IN-REPO POINTER: a short payload whose whole content is "the licence lives
# over there". `ckeditor/ckeditor5` serves a 170 B root `LICENSE.md` reading
# "The license for this repository is maintained in
# [`packages/ckeditor5/LICENSE.md`](...)" -- and the repository really does
# serve a 17 983 B `COPYING.GPL`. The first cut of the NOT-OSI class graded that
# pointer NOT-OSI, because its title is "Software License Agreement" and a
# pointer contains no grant text by definition. A pointer is the ABSENCE of a
# grant at this path, never the refusal of one.
POINTER_RE = re.compile(
    r"(?:licen[cs]e|terms).{0,80}?(?:is |are )?(?:maintained|found|located|"
    r"available|specified|described)?\s*(?:in|at|under|see)\s*\[?`?"
    r"([A-Za-z0-9._/-]+\.(?:md|txt|rst|html))`?", re.I | re.S)
POINTER_MAX_BYTES = 600


def pointer_target(text):
    """The in-repo path a short pointer payload names, or ''."""
    if len(text.encode()) > POINTER_MAX_BYTES:
        return ""
    m = POINTER_RE.search(text)
    if not m:
        return ""
    tgt = m.group(1).lstrip("./")
    return tgt


def family(text):
    t = title_block(text)
    tl = t.lower()
    h = head40(text)
    hl = h.lower()

    # (0) A pointer is the absence of a grant here, not a refusal of one.
    tgt = pointer_target(text)
    if tgt and not PERMISSIVE_GRANT.search(h):
        return f"POINTER_IN_REPO ({tgt})"

    # (1) A bespoke grant that names itself and is NOT an OSI family. Checked
    #     FIRST: this is the only class whose mis-grade invites a promotion.
    if (not OSI_TITLES.search(t) and not PERMISSIVE_GRANT.search(h)
            and (BESPOKE_TITLE.search(t.splitlines()[0] if t.splitlines() else "")
                 or NOT_OPEN.search(h))):
        m = re.match(r"#*\s*(.+?)\s*$", t.splitlines()[0]) if t.splitlines() else None
        name = (m.group(1) if m else "bespoke")[:60]
        return f"NOT-OSI ({name})"

    # (2) A composite: two or more DISTINCT families named, and the title is not
    #     itself one family's own text. Never a heading count.
    fams = families_named(text)
    if len(fams) >= 2 and not OSI_TITLES.search(t):
        return "COMPOSITE: " + "+".join(fams)

    # (3) GPL family, discriminated on the TITLE ONLY (defect 1).
    if re.search(r"\bgnu lesser general public license\b", tl):
        return "LGPL"
    if re.search(r"\bgnu affero general public license\b", tl):
        return "AGPL-3.0"
    if re.search(r"\bgnu general public license\b", tl):
        return "GPL"

    # (4) The remaining families recommend no sibling in their own body, so the
    #     40-line head is safe for them.
    if "apache license" in hl and "version 2.0" in hl:
        return "Apache-2.0"
    if tl.startswith("mit license") or re.search(r"^mit license", hl, re.M):
        return "MIT"
    if "permission is hereby granted, free of charge" in hl:
        return "MIT (body form, no title)"
    if "redistribution and use in source and binary forms" in hl:
        return "BSD-3-Clause" if "neither the name" in text.lower() else "BSD-2-Clause"
    if "isc license" in hl or "permission to use, copy, modify, and/or distribute" in hl:
        return "ISC"
    if "mozilla public license" in hl:
        return "MPL-2.0"
    if "cc0 1.0 universal" in hl:
        return "CC0-1.0"
    if "creative commons" in hl:
        ABBR = {"sharealike": "SA", "noncommercial": "NC", "noderivatives": "ND"}
        clauses = [ABBR[k] for k in ("noncommercial", "noderivatives", "sharealike") if k in hl]
        ver = "4.0" if "4.0" in hl else ("3.0" if "3.0" in hl else "")
        return "-".join(["CC-BY"] + clauses + ([ver] if ver else []))
    if "open data commons" in hl or "odbl" in hl:
        return "ODbL"
    if "the unlicense" in hl or "unlicense" in hl.split("\n")[0]:
        return "Unlicense"
    return "UNREAD"
