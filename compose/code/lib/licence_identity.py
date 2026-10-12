#!/usr/bin/env python3
"""`lib/licence_identity.py` — the licence-identity question, asked ONCE.

Pass 151 of 2026-10-12. 🔵 **This module exists because `P263`'s rule came due.** The
rule is written in `lib/README.md` and in `lib/region.py`:

> *while the question does not live in `compose/code/lib/`, every new instrument
> reimplements it and chooses the bug again.*

🔴 **`T77` is that rule being paid.** Three published modules carried a copy of the same
`identify()`, and every copy carried the same rung:

    (re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I), "AGPL-3.0"),

applied with `rx.search(body)` over the WHOLE licence text. 🔴 **GPL-3.0's own section 13
is titled "Use with the GNU Affero General Public License"**, so every verbatim GPL-3.0
file matched the AGPL rung before the GPL rung was reached. 🔴 **5 of this shelf's 7
GNU-family rows were published wrong, and the id `GPL` was published ZERO times in 150
passes.**

## The contract

🟢 **A licence is identified from its TITLE LINE, never from its body.** `title_spdx()`
reads only the first `TITLE_WINDOW_LINES` non-blank lines, and the licence name must *be*
the line (optionally followed by a version). 🔵 **That is what makes the surface immune to
a sibling mention**: every GNU licence names its siblings somewhere in its text — GPL-2.0's
preamble says *"use the GNU **Lesser** General Public License instead"* — but a sentence is
never just the licence's name.

🟢 **`clause_licence()` is a SECOND, independent surface** — AGPL-3.0 §13 *"Remote Network
Interaction"* is the clause that makes AGPL different from GPL, and a plain GPL-3.0 file
cannot contain it. `agree()` returns a verdict only when the two surfaces say the same
thing, and names the disagreement otherwise.

🔴 **What this module deliberately does NOT do: read an election.** `-only` versus
`-or-later` is NOT in the licence body — or rather, it is in every GNU licence's body, in
the *"How to Apply These Terms"* appendix, which is why reading it there is `T77` one
layer down (`T81`, pass 151). The election belongs to the per-file header surface and
lives in `p151-election-surface`.

Measured reach, pass 151: **39 of 39** licence files across the 58-row census carry a
readable title line, so the title surface costs **zero coverage** against the body
matcher it replaces.

Use:
    import sys, os; sys.path.insert(0, ".../compose/code/lib")
    from licence_identity import title_spdx, agree, GNU_FAMILY
"""
import re

# The title window: a GNU licence names itself on its FIRST non-blank line. 5 lines covers
# the title and version block and nothing else. 🔵 It must stay narrow: widen it far enough
# and it reaches the preamble, which is the very text the fix exists to get away from.
TITLE_WINDOW_LINES = 5

TITLES = [
    (re.compile(r"GNU\s+AFFERO\s+GENERAL\s+PUBLIC\s+LICENSE", re.I), "AGPL-3.0"),
    (re.compile(r"GNU\s+LESSER\s+GENERAL\s+PUBLIC\s+LICENSE", re.I), "LGPL"),
    (re.compile(r"GNU\s+GENERAL\s+PUBLIC\s+LICENSE", re.I), "GPL"),
    (re.compile(r"Apache\s+License", re.I), "Apache-2.0"),
    (re.compile(r"Mozilla\s+Public\s+License", re.I), "MPL-2.0"),
    (re.compile(r"Educational\s+Community\s+License", re.I), "ECL-2.0"),
    (re.compile(r"MIT\s+License", re.I), "MIT"),
    (re.compile(r"ISC\s+License", re.I), "ISC"),
    (re.compile(r"BSD\s+\d-Clause", re.I), "BSD"),
]

# A title is a LINE, not a substring: the name must occupy the whole line, optionally
# followed by a version. 🔴 Scanning a window for the name *anywhere in it* fails the same
# way the body matcher does, only over fewer lines.
TITLE_TAIL = re.compile(r"[\s,]*(?:Version\s+[\d.]+.*)?$", re.I)
VERSION_LINE = re.compile(r"Version\s+(\d+)(?:\.(\d+))?", re.I)

# AGPL-3.0's operative clause — the *difference* between AGPL and GPL, so the right
# second surface.
AGPL_NETWORK_CLAUSE = re.compile(r"^\s*13\.\s+Remote Network Interaction", re.M)
# GPL-3.0's section 13, which is what makes the naive body matcher fire.
GPL_SEC13_AFFERO = re.compile(r"^\s*13\.\s+Use with the GNU Affero", re.M)
# The retired rung, kept so the defect can be REPRODUCED rather than asserted.
NAIVE_AGPL_BODY = re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I)

GNU_FAMILY = re.compile(r"(?i)^(a?gpl|lgpl)")

LICENCE_NAMES = re.compile(
    r"^(LICEN[CS]E|COPYING|UNLICEN[CS]E|MIT-LICEN[CS]E|LICENSE-MIT|LICENSE-APACHE)"
    r"(\.(md|txt|rst|html))?$", re.IGNORECASE)


def title_window(body):
    """The first `TITLE_WINDOW_LINES` non-blank lines of a licence file."""
    lines = [ln for ln in body.splitlines() if ln.strip()]
    return "\n".join(lines[:TITLE_WINDOW_LINES])


def title_licence(body):
    """The licence FAMILY named on the file's title line, or None."""
    for line in [ln.strip() for ln in body.splitlines() if ln.strip()][
            :TITLE_WINDOW_LINES]:
        for rx, name in TITLES:
            m = rx.match(line)
            if m and TITLE_TAIL.fullmatch(line[m.end():]):
                return name
    return None


def title_version(body):
    """The version stated in the title block, as "3.0", or None."""
    m = VERSION_LINE.search(title_window(body))
    if not m:
        return None
    return "%s.%s" % (m.group(1), m.group(2) if m.group(2) else "0")


def title_spdx(body):
    """The SPDX id from the TITLE surface, version included where the family needs one.

    🔵 The version is load-bearing: `qxbao/qldt-hanu-mcp` is GPL-**2.0**, which has no
    patent grant and no section 13 at all, and this shelf published it as `LGPL`.
    """
    name = title_licence(body)
    if name is None:
        return None
    if name in ("GPL", "LGPL"):
        ver = title_version(body)
        return "%s-%s" % (name, ver) if ver else name
    return name


def clause_licence(body):
    """AGPL-3.0 or GPL, read from the operative section 13, or None if neither."""
    if AGPL_NETWORK_CLAUSE.search(body):
        return "AGPL-3.0"
    if GPL_SEC13_AFFERO.search(body):
        return "GPL"
    return None


def naive_verdict(body):
    """The ONE retired rung, in isolation. Reproduces `T77`'s trigger, nothing more.

    🔴 **Do not use this as "what the census published".** It tests only the AGPL rung,
    so it is silent on GPL-2.0 and on every non-GNU licence, and comparing it against
    `title_spdx` as if it were a whole matcher overstates the delta — it reported 37
    differing rows where the census's real delta is 5. `retired_identify()` is the
    comparable surface.
    """
    return "AGPL-3.0" if NAIVE_AGPL_BODY.search(body) else None


# The non-GNU body rungs, unchanged from the published `identify()`. They are tried first
# there and they are kept here so `retired_identify()` is the published matcher and not an
# approximation of it.
RETIRED_NON_GNU = [
    (re.compile(r"Apache License.*Version 2\.0", re.S | re.I), "Apache-2.0"),
    (re.compile(r"Mozilla Public License", re.I), "MPL-2.0"),
    (re.compile(r"Permission is hereby granted, free of charge", re.I), "MIT"),
    (re.compile(r"Redistribution and use in source and binary forms", re.I), "BSD"),
    (re.compile(r"This is free and unencumbered software released into the public"
                r" domain", re.I), "Unlicense"),
    (re.compile(r"Permission to use, copy, modify, and/or distribute", re.I), "ISC"),
]
RETIRED_GNU = [
    (NAIVE_AGPL_BODY, "AGPL-3.0"),
    (re.compile(r"GNU LESSER GENERAL PUBLIC LICENSE", re.I), "LGPL"),
    (re.compile(r"GNU GENERAL PUBLIC LICENSE", re.I), "GPL"),
]


def retired_identify(body):
    """`identify()` AS PUBLISHED before pass 151 — the whole ladder, in its own order.

    🔵 The order is the defect: the Apache rung comes first (and so a GNU file quoting
    Apache sorts OUT of the family), then the three GNU rungs with AGPL ahead of GPL (and
    so every verbatim GPL-3.0 file sorts to AGPL). Both orderings are preserved exactly,
    because a reproduction that fixes either one cannot measure what was published.
    """
    for rx, name in RETIRED_NON_GNU[:1]:          # Apache, first, as published
        if rx.search(body):
            return name
    for rx, name in RETIRED_GNU:                   # then the three GNU rungs
        if rx.search(body):
            return name
    for rx, name in RETIRED_NON_GNU[1:]:           # then the rest
        if rx.search(body):
            return name
    return None


def agree(body):
    """(verdict, surfaces, status) over the two independent surfaces.

    `AGREE` when both answer and answer the same, `TITLE_ONLY` when only the title answers
    (a non-GNU licence has no section 13), `DISAGREE` when they differ, `UNDETERMINED`
    when neither answers.
    """
    t = title_licence(body)
    c = clause_licence(body)
    if t and c:
        if t == c or (c == "GPL" and t in ("GPL", "LGPL")):
            return t, (t, c), "AGREE"
        return t, (t, c), "DISAGREE"
    if t:
        return t, (t, None), "TITLE_ONLY"
    return None, (None, c), "UNDETERMINED"
