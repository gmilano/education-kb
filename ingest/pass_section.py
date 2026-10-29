#!/usr/bin/env python3
"""Read a pass section's own id from the heading's LEADING segment.

p530's matcher was case-sensitive on `Pass` and missed 212 sections.  p531 fixed
that with a case fold -- and the fold then matches a pass number CITED in the
title prose, which is the very defect p531 diagnosed for `pass 277`.  Both
matchers share one root cause: they search the WHOLE heading for a number, and a
heading contains two kinds of number.

    ## 2026-10-07 - twenty-ninth pass: ... every defect pass 28 had just fixed
       ^ date        ^ SELF-ID (ordinal word)      ^ CITATION

This base writes a heading as `<date/id segment> — <date/id segment> — <title>`,
and the self-id is always in a LEADING segment, never in the title prose.  So
the rule is positional, not lexical: split on the em-dash, cut each segment at
its first colon, and take the first segment that yields a token.

Dialects this resolves, all present in the live files:
    ## 🆕 `p531` — `2026-10-29` — **TITLE**            -> 531  (backtick)
    ## 2026-10-16 — Pass 250 — TITLE                   -> 250  (second segment)
    ## Pass 262 — 2026-10-17 — TITLE                   -> 262  (first segment)
    ## 2026-10-18 (pass 283) — TITLE                   -> 283  (parenthesised)
    ## 2026-10-07 — twenty-ninth pass: TITLE           -> 29   (ordinal word)
    ## 🟢 Pass 129 — 2026-10-11 (sixteenth pass of…)   -> 129  (not 16)
"""

import re

ONES = {
    "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6,
    "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10, "eleventh": 11,
    "twelfth": 12, "thirteenth": 13, "fourteenth": 14, "fifteenth": 15,
    "sixteenth": 16, "seventeenth": 17, "eighteenth": 18, "nineteenth": 19,
}
TENS_EXACT = {
    "twentieth": 20, "thirtieth": 30, "fortieth": 40, "fiftieth": 50,
    "sixtieth": 60, "seventieth": 70, "eightieth": 80, "ninetieth": 90,
}
TENS_PREFIX = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90,
}

BACKTICK = re.compile(r"`p(\d{1,4})`")
WORDFORM = re.compile(r"\(?\b[Pp]as[se]\s+(\d{1,4})\b\)?")
BARE = re.compile(r"\bp(\d{1,4})\b")
HUNDREDS = {
    "one": 100, "two": 200, "three": 300, "four": 400, "five": 500,
    "six": 600, "seven": 700, "eight": 800, "nine": 900,
}
# `Hundred-and-twenty-fourth pass` is 124, and this base writes 17 headings that
# way.  Both earlier matchers resolved those to a pass number CITED in the same
# title; an ordinal reader that stops at the tens resolves them to 24.
ORDINAL = re.compile(
    r"\b(?:(one|two|three|four|five|six|seven|eight|nine)[-\s])?"
    r"(hundred)(?:[-\s]and)?[-\s]"
    r"(?:(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)[-\s])?"
    r"(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|"
    r"eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|"
    r"seventeenth|eighteenth|nineteenth|twentieth|thirtieth|fortieth|"
    r"fiftieth|sixtieth|seventieth|eightieth|ninetieth)\s+pass\b"
    r"|"
    r"\b(?:(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)[-\s])?"
    r"(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|"
    r"eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|"
    r"seventeenth|eighteenth|nineteenth|twentieth|thirtieth|fortieth|"
    r"fiftieth|sixtieth|seventieth|eightieth|ninetieth)\s+pass\b"
    r"|"
    r"\b(hundredth)\s+pass\b", re.I)

# Segment separators this base actually uses in headings.
SPLIT = re.compile(r"\s+[—–]\s+|\s+-\s+")
# An id sits at the START of its segment; title prose that mentions a pass puts
# the number further in ("...for the ninth pass running").  So the window is a
# PREFIX of the segment, not a cap on the whole segment -- a cap wrongly
# rejected `## 2026-10-13 — Pass 170 *(append-only; history below is preserved)*`,
# whose id is leading and whose aside is long.
ID_PREFIX = 48


def _ordinal_value(m):
    """Resolve whichever of the three alternations matched.

    Groups 1-4: [hundreds-word] `hundred` [tens] ones   (`Hundred-and-twenty-fourth`)
    Groups 5-6: [tens] ones                             (`twenty-ninth`)
    Group 7:    `hundredth`
    """
    g = m.groups()
    if g[6]:
        return 100
    if g[1]:  # the `hundred` literal matched
        base = HUNDREDS[g[0].lower()] if g[0] else 100
        tens, word = g[2], g[3]
    else:
        base = 0
        tens, word = g[4], g[5]
    if not word:
        return None
    word = word.lower()
    if word in TENS_EXACT:
        return base + TENS_EXACT[word]
    v = ONES.get(word)
    if v is None:
        return None
    return base + (TENS_PREFIX[tens.lower()] + v if tens else v)


def pass_of_heading(line):
    """The section's own pass number, or None.

    Returns (pass_no, dialect) so a caller can attribute the reading.
    """
    text = line.lstrip("#").strip()
    # The bold title starts the prose; nothing after it is an id.
    cut = text.find("**")
    if cut > 0:
        text = text[:cut]
    for seg in SPLIT.split(text):
        seg = seg.strip()
        if not seg:
            continue
        # Within a segment the prose starts at the first colon.
        head = seg.split(":", 1)[0].strip()
        if not head:
            continue
        m = BACKTICK.search(head)
        if m:
            return int(m.group(1)), "backtick"
        prefix = head[:ID_PREFIX]
        m = WORDFORM.search(prefix)
        if m:
            return int(m.group(1)), "wordform"
        m = ORDINAL.search(prefix)
        if m:
            v = _ordinal_value(m)
            if v is not None:
                return v, "ordinal"
        # The bare dialect is `## 2026-10-13 — p180 — title`: the id is a
        # segment ON ITS OWN.  Accepting a bare token anywhere in a prefix
        # instead reads `## 🔴 🆕 \`P125-A\` — … p124 read by hand` -- a gap
        # registration, not a pass section -- as p124, which is what both
        # earlier matchers did.
        if len(head) <= 12:
            m = BARE.search(head)
            if m:
                return int(m.group(1)), "bare"
    return None, None
