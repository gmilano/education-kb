#!/usr/bin/env python3
"""ACTION AD — resolve a Creative Commons grant to a VERSIONED token.

Pure function over text: no network, no filesystem, no clock.

WHY THIS MATTERS COMMERCIALLY, AND WHY IN THIS KB ESPECIALLY. p123's census
left 41 readable grants in a bare `CC` bucket, because p123's classifier
anchors on a TITLE in the first 400 characters and the CC family has at least
four title conventions. `CC` is not a licence. The difference between

    CC-BY-4.0          -> a studio may ship a commercial derivative
    CC-BY-NC-SA-4.0    -> it may not, at any price

is the whole engagement, and in an EDUCATION knowledge base the asset under
the CC grant is usually the curriculum, the item bank or the knowledge graph
— the deliverable itself, not a doc folder. A census that cannot separate
these two is reporting the commercially decisive fact as unknown.

THE FOUR CHANNELS, in decreasing authority. Each is checked over the WHOLE
text, not a 400-character head, because the CC deed convention puts the
canonical URL in the footer and the legalcode puts the version in s.1.

  1. TITLE LINE     — "Attribution-NonCommercial-ShareAlike 4.0 International".
     Every CC legalcode and every CC deed opens with the canonical name on
     its first line. This channel is FIRST and it is decisive.
  2. CANONICAL URL  — creativecommons.org/licenses/by-nc-sa/4.0/ (or
     /publicdomain/zero/1.0/). The licence's own identifier.
  3. SHORT TOKEN    — "CC BY-NC-SA 4.0" named anywhere.
  4. ELEMENTS + VERSION read separately — a body that states its version in
     one place and its elements in another.

A text that reaches none of them stays `CC-UNVERSIONED`, which is an honest
answer and a different answer from `CC`: it says the elements are unreadable
too, so the row needs a human, not a better regex.

🔴 WHY THE TITLE HAD TO COME FIRST — the defect this file was built WITH and
then repaired, recorded because it is the whole lineage of this KB's
classifier in miniature. The first build of this resolver scanned the WHOLE
text for its element set and returned **`CC0-1.0` for 9 of 13 rows**,
including [`openstax/osbooks-college-physics-bundle`](https://github.com/openstax/osbooks-college-physics-bundle),
whose first line reads `Attribution-NonCommercial-ShareAlike 4.0
International` — the single most commercially consequential CC token there
is, reported as the single least restrictive one.

The cause is not a typo. The CC 4.0 **legalcode body itself** contains, in
its "Considerations for licensors" boilerplate, a recommendation to use the
**CC0 Public Domain Dedication** instead. So every CC-BY-4.0 file on earth
contains the string `CC0 Public Domain Dedication`, and a whole-text scan
reads all of them as CC0. This is defect #1 of the carried lineage —
GPL-2.0's preamble naming the Lesser GPL — recurring in a different family,
and it was caught for exactly the reason that one was: the fixture is a real
file, and the real file was read before the result was published.
"""
import re

# Channel 1. Element order in CC URLs is canonical (by, by-sa, by-nc,
# by-nc-sa, by-nd, by-nc-nd), so the path segment IS the element set.
URL = re.compile(
    r"creativecommons\.org/(?:licen[cs]es|publicdomain)/"
    r"(by(?:-nc)?(?:-sa|-nd)?|zero|mark|certification)"
    r"(?:/(\d(?:\.\d)?))?",
    re.I)

# Channel 2/3. The element set, however spelled. Longest first: an
# "Attribution-NonCommercial-ShareAlike" text also contains "Attribution".
ELEMENTS = [
    ("BY-NC-SA", re.compile(r"attribution[\s-]*non[\s-]*commercial[\s-]*share[\s-]*alike"
                            r"|\bCC[\s-]*BY[\s-]*NC[\s-]*SA\b", re.I)),
    ("BY-NC-ND", re.compile(r"attribution[\s-]*non[\s-]*commercial[\s-]*no[\s-]*deriv"
                            r"|\bCC[\s-]*BY[\s-]*NC[\s-]*ND\b", re.I)),
    ("BY-SA",    re.compile(r"attribution[\s-]*share[\s-]*alike"
                            r"|\bCC[\s-]*BY[\s-]*SA\b", re.I)),
    ("BY-ND",    re.compile(r"attribution[\s-]*no[\s-]*deriv"
                            r"|\bCC[\s-]*BY[\s-]*ND\b", re.I)),
    ("BY-NC",    re.compile(r"attribution[\s-]*non[\s-]*commercial"
                            r"|\bCC[\s-]*BY[\s-]*NC\b", re.I)),
    ("BY",       re.compile(r"creative\s+commons\s+attribution"
                            r"|\bCC[\s-]*BY\b", re.I)),
]

ZERO = re.compile(r"\bCC0\b|creative\s+commons\s+zero"
                  r"|public\s+domain\s+dedication", re.I)

# Channel 4. A version number, but only where it is attached to a CC name or
# to the word "version" — never a bare "4.0" that could be an Apache header.
VERSION = re.compile(
    r"(?:attribution[a-z\s-]*|CC[\s-]*BY[A-Z\s-]*|licen[cs]e[,\s]*|version\s*)"
    r"(\d(?:\.\d)?)",
    re.I)

IS_CC = re.compile(r"creative\s*commons|\bCC[\s-]*BY\b|\bCC0\b", re.I)


# A DOCUMENT-TYPE header, not a licence name. The CC0 legalcode as served by
# Creative Commons opens with "Creative Commons Legal Code" and puts the
# canonical name "CC0 1.0 Universal" on the NEXT line. Skipping these is not
# a phrase list for licences — it is the distinction between a document's
# type and a document's subject.
DOC_HEADER = re.compile(r"^(?:creative\s+commons(?:\s+legal\s+code)?"
                        r"|legal\s+code"
                        r"|licen[cs]e|licen[cs]e\s+agreement)[\s.:-]*$", re.I)

TITLE_LINES = 4


def _titles(text):
    """The first few non-empty lines, BOM stripped, document headers dropped.

    CC files are served with a UTF-8 BOM often enough that ignoring it loses
    the title on exactly the rows a docs/code split puts it on
    (`azure/moodle`'s `LICENSE-DOCS` is one).
    """
    out = []
    for line in text.lstrip("﻿").splitlines():
        s = line.strip().lstrip("﻿").strip()
        if not s:
            continue
        if not DOC_HEADER.match(s):
            out.append(s)
        if len(out) >= TITLE_LINES:
            break
    return out


def _from_title(title):
    """Resolve from the canonical title line alone, or return None.

    This is channel 1 and it runs before everything else: see the module
    docstring on why a whole-text scan cannot be trusted for the CC family.
    """
    if re.match(r"^(?:creative\s+commons\s+)?(?:CC0|zero)\s*1\.0", title, re.I):
        return "CC0-1.0"
    m = re.match(r"^(?:creative\s+commons\s+)?"
                 r"(attribution[\w\s-]*?)"
                 r"\s+(\d(?:\.\d)?)\s*(?:international|unported|generic)?\b",
                 title, re.I)
    if not m:
        return None
    name, ver = m.group(1), m.group(2)
    for code, rx in ELEMENTS:
        if rx.search(name):
            return "CC-%s-%s" % (code, ver)
    return None


def resolve(text):
    """Return a versioned CC token, `CC-UNVERSIONED`, or None if not CC."""
    if not IS_CC.search(text):
        return None

    # --- channel 1: the canonical TITLE LINE, which is decisive ----------
    for line in _titles(text):
        t = _from_title(line)
        if t:
            return t

    # --- channel 2: the licence's own URL -------------------------------
    m = URL.search(text)
    if m:
        code, ver = m.group(1).lower(), m.group(2)
        if code in ("zero",):
            return "CC0-1.0"
        if code in ("mark", "certification"):
            return "CC-PDM"
        if ver:
            return "CC-" + code.upper().replace("BY", "BY", 1) + "-" + ver
        # A URL without a version is still the element set.
        elements = code.upper()
    else:
        elements = None

    # --- channel 3: the element set, spelled or tokenised ---------------
    # 🔴 ZERO is NOT consulted here. "CC0 Public Domain Dedication" appears in
    # the boilerplate of every CC 4.0 legalcode file, so outside the title and
    # the URL it is evidence of nothing. CC0 is reachable by channel 1 and 2
    # only, on purpose.
    if elements is None:
        for name, rx in ELEMENTS:
            if rx.search(text):
                elements = name
                break
    if elements is None:
        return "CC-UNVERSIONED"

    # --- channel 4: the version, read separately -------------------------
    for m in VERSION.finditer(text):
        v = m.group(1)
        if v in ("1.0", "2.0", "2.5", "3.0", "4.0"):
            return "CC-%s-%s" % (elements, v)
    return "CC-%s-UNVERSIONED" % elements


if __name__ == "__main__":
    import sys
    r = resolve(sys.stdin.read())
    print(r if r else "NOT-CC")
