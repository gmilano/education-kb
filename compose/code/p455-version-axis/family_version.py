#!/usr/bin/env python3
"""p455 -- the licence reader gains a VERSION AXIS, closing `Gap 454-C`.

`p454` built a sound family reader (`p454-carried-cell-value/family_title.py`)
by anchoring the GPL discrimination on the TITLE BLOCK instead of a 40-line
window. It graded correctly at the FAMILY level and said so, and then it
registered its own ceiling:

    Gap 454-C -- "A family-level reader cannot grade a version-level
    incompatibility, and this base has one live."
    `edu-sharing/Edu-Sharing`: npm `ngx-edu-sharing-api@10.0.1` declares
    `GNU GPL v2`; the payload at HEAD is GPL *Version 3*. GPL-2.0 and
    GPL-3.0 are MUTUALLY INCOMPATIBLE, and `canon()` collapsed both onto
    the family `GPL` and therefore graded the pair AGREE.

Why the version is not cosmetic: a deliverable may not combine GPL-2.0-only
code with GPL-3.0 code. A shelf that records `GPL` for both tells an engagement
team the two are the same constraint. They are opposite constraints.

This file is `family_title.py` with ONE addition and ONE subtraction:

  + `version_of()` reads the version from the TITLE BLOCK, where the GNU
    licences state it ("GNU GENERAL PUBLIC LICENSE\\n Version 3, 29 June 2007").
    Same anchor as `p454`'s family discrimination, for the same reason: a
    preamble cannot reach it. GPLv2's preamble recommends the LGPL at
    non-empty line 15 -- inside any 40-line window -- which is the defect
    `Gap 454-A` records as still unfixed in the carried `verify.py`.

  - `family()` no longer returns a bare `GPL` / `LGPL` / `AGPL-3.0` when a
    version is legible. It returns `GPL-2.0` / `GPL-3.0` / `LGPL-2.1` /
    `LGPL-3.0` / `AGPL-3.0`.

`only_or_later()` is the second axis the same title block carries, and it is
NOT decoration either: GPL-2.0-ONLY cannot combine with GPL-3.0, while
GPL-2.0-OR-LATER can (it may be taken forward to v3). The "or later" grant
lives in the per-file headers and the `How to Apply` appendix, never in the
title block, so this function reads the WHOLE payload and says UNSTATED when
the payload itself does not say -- which is the honest answer for a stock
`COPYING` with no project-specific notice.
"""
import re

# Imported wholesale from p454 -- unchanged, because the family layer was
# measured sound over 179 payloads and this pass adds to it rather than
# relitigating it.
from family_title import (FAMILY_TOKENS, NOT_OPEN, BESPOKE_TITLE,
                          PERMISSIVE_GRANT, OSI_TITLES, title_block, head40,
                          families_named, pointer_target)
import family_title

# The GNU title block states the version on its own line, directly under the
# name: "GNU GENERAL PUBLIC LICENSE" / "Version 3, 29 June 2007". Apache states
# it inline: "Apache License, Version 2.0". Both forms are matched; the search
# is confined to the title block for the GNU family (p454's anchor) and to the
# head for Apache (which recommends no sibling in its own body).
VERSION_RE = re.compile(r"\bversion\s+(\d+)(?:\.(\d+))?\b", re.I)

# "or later" / "or any later version" is a FORWARD-COMPATIBILITY grant and the
# single most consequential bit on this axis, because it decides whether a
# GPL-2.0 payload may be combined with GPL-3.0 code at all.
OR_LATER_RE = re.compile(
    r"or\s+\(?at\s+your\s+option\)?\s+any\s+later\s+version|"
    r"or\s+any\s+later\s+version|"
    r"\bor[- ]later\b|"
    r"either\s+version\s+[\d.]+\s+of\s+the\s+license,?\s+or", re.I)

# An explicit refusal of the forward grant. Projects that mean GPL-2.0-ONLY
# usually say so in exactly one of these forms.
ONLY_RE = re.compile(
    r"\bversion\s+2\s+only\b|\bgpl-?2\.0-?only\b|\bgplv2\s+only\b|"
    r"\bversion\s+3\s+only\b|\bgpl-?3\.0-?only\b|"
    r"but\s+not\s+any\s+later\s+version", re.I)

GNU_DEFAULTS = {"AGPL": "3.0", "LGPL": "3.0", "GPL": "3.0"}


def version_of(text, gnu=True):
    """The licence version stated in the TITLE BLOCK, or '' when not stated.

    Anchored on the title block for the same reason p454 anchors the family
    there: it is the only region of a licence payload that cannot be reached by
    a preamble, an appendix, or a sibling-licence recommendation.
    """
    scope = title_block(text, lines=4) if gnu else head40(text)
    m = VERSION_RE.search(scope)
    if not m:
        return ""
    major, minor = m.group(1), m.group(2)
    return f"{major}.{minor}" if minor else f"{major}.0"


def only_or_later(text):
    """'or-later' | 'only' | 'UNSTATED' -- read over the WHOLE payload.

    Deliberately NOT title-anchored: the forward grant is stated in the per-file
    notice and the `How to Apply` appendix, which is outside the title block by
    construction. UNSTATED is a real and common answer (a stock COPYING carries
    no project-specific election) and must not be guessed in either direction --
    guessing `or-later` invents a combination right, guessing `only` invents a
    prohibition.
    """
    if ONLY_RE.search(text):
        return "only"
    if OR_LATER_RE.search(text):
        return "or-later"
    return "UNSTATED"


def family(text):
    """p454's grade, with the GNU and Apache families carrying their version."""
    base = family_title.family(text)

    if base in ("GPL", "LGPL", "AGPL-3.0"):
        fam = "AGPL" if base.startswith("AGPL") else base
        ver = version_of(text, gnu=True) or GNU_DEFAULTS[fam]
        # Normalise to the SPDX forms that actually exist: there is no LGPL-2.0
        # in common use for new code, and AGPL has only 1.0/3.0.
        if fam == "LGPL" and ver == "2.0":
            ver = "2.1"
        return f"{fam}-{ver}"

    return base


def canon(grade):
    """Version-PRESERVING canonicalisation -- the one `Gap 454-C` asked for.

    p454's `canon()` collapsed GPL-2.0 and GPL-3.0 onto `GPL`, which is what
    graded the `edu-sharing` mismatch AGREE. This one keeps the version and
    therefore CAN disagree. It still normalises spelling, punctuation and the
    registry shorthands ("GNU GPL v2", "GPLv2", "gpl-2.0-only") onto one form,
    because that was the half of `canon()` that was doing useful work.
    """
    if not grade:
        return ""
    g = grade.strip().lower()
    g = re.sub(r"\s+", " ", g)
    g = g.replace("gnu ", "").replace("licence", "license")
    g = re.sub(r"\(([^)]*)\)", "", g).strip()          # drop parentheticals
    g = re.sub(r"[\s_]", "-", g)
    g = re.sub(r"-license\b|-only\b|-or-later\b", "", g)
    # DEFECT CAUGHT BY THIS PASS'S OWN CONTROL, and it is the one that would
    # have mattered most: `\bv(\d)` cannot fire inside `gplv3`, because `l`
    # and `v` are both word characters so there is no boundary between them.
    # "GNU GPL v2" (spaced) normalised correctly and `GPLv3` (compact) fell
    # through to the identity branch -- and the compact form is the commonest
    # shorthand npm and crates.io actually serve. `family_title.py`'s own
    # FAMILY_TOKENS anticipated it (`\bgplv?[23]\b`); this canon did not.
    g = re.sub(r"\b(a|l)?gpl-?v\s*(\d)", r"\1gpl-\2", g)
    g = re.sub(r"\baffero-gpl\b|\bagplv?\b", "agpl", g)

    m = re.match(r"^(agpl|lgpl|gpl)-?(\d)(?:\.(\d))?$", g)
    if m:
        fam, major, minor = m.group(1), m.group(2), m.group(3)
        if minor is None:
            minor = "1" if (fam == "lgpl" and major == "2") else "0"
        return f"{fam.upper()}-{major}.{minor}"

    m = re.match(r"^apache-?2(?:\.0)?$", g)
    if m:
        return "Apache-2.0"
    if g in ("mit",):
        return "MIT"
    if g.startswith("bsd-3"):
        return "BSD-3-Clause"
    if g.startswith("bsd-2"):
        return "BSD-2-Clause"
    if g == "isc":
        return "ISC"
    if g.startswith("mpl-2"):
        return "MPL-2.0"
    return grade.strip()


def compatible(a, b):
    """Can a deliverable combine payloads graded `a` and `b`?

    Only the GNU axis is decided here, because that is the axis `Gap 454-C`
    opened and the only one where two grades of the SAME family are mutually
    exclusive. Anything else returns None -- 'not decided by this function' --
    rather than a reassuring True.
    """
    ca, cb = canon(a), canon(b)
    gnu = re.compile(r"^(AGPL|LGPL|GPL)-(\d)\.(\d)$")
    ma, mb = gnu.match(ca or ""), gnu.match(cb or "")
    if not (ma and mb):
        return None
    if ca == cb:
        return True
    # GPL-2.0 and GPL-3.0 are mutually incompatible unless one is or-later,
    # which this function cannot see (it takes grades, not payloads). The
    # caller must pass only_or_later() separately; absent that, the safe
    # answer for differing GNU versions is False.
    if ma.group(1) == mb.group(1):
        return False
    # LGPL-3.0 may be taken up into GPL-3.0; AGPL-3.0 and GPL-3.0 are not
    # interchangeable in a single combined work.
    if {ma.group(1), mb.group(1)} == {"LGPL", "GPL"} and ma.group(2) == mb.group(2):
        return True
    return False
