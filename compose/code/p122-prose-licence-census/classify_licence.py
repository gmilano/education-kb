#!/usr/bin/env python3
"""Classify a licence file's text into an SPDX-ish token.

Pure function over text: no network, no filesystem. Driven online by
scan_licences.sh and offline by test_p122.sh against fixtures/.

THREE DEFECTS THIS CLASSIFIER WAS BUILT TO SURVIVE, each found in p122 by a
real file in fixtures/, each of which a substring-anywhere matcher gets wrong:

  1. GPL-2.0's own PREAMBLE names the Lesser GPL ("...use the GNU Lesser
     General Public License instead"), at byte 853 of an 18 092-byte file.
     A `"lesser" in text` test reads every GPL-2.0 file as LGPL.
     -> fixtures/gpl2-preamble-names-lesser.txt (portabilis/i-educar)

  2. EPL-2.0's SECONDARY LICENSE clause names "GNU General Public License,
     version 2.0". A `"general public license" in text` test reads every
     EPL-2.0 file as GPL-2.0.
     -> fixtures/epl2-secondary-names-gpl2.txt (hcengineering/platform)

  3. A SPLIT-GRANT file names several licences on purpose ("Portions of this
     software are licensed as follows"). There is no single token; reporting
     whichever name appears first is arbitrary.
     -> fixtures/mit-split-grant-names-cc.txt (pupilfirst/pupilfirst)

The fix for 1 and 2 is to anchor the GPL family on the licence TITLE rather
than on any occurrence, and to resolve the licences with unique names first.
The fix for 3 is to detect the split and name the PRIMARY grant explicitly,
so a reader is told it is a split rather than given one arm of it.
"""
import re
import sys

SPLIT_MARKERS = (
    "portions of this software are licensed as follows",
    "portions of this project are licensed",
    "the following licenses apply",
    # p122: a split-grant marker is LANGUAGE-SPECIFIC. This KB carries
    # Brazilian BNCC repositories whose LICENSE is written in Portuguese, so
    # an English-only marker list reads a dual licence as a single one.
    "usa duas licen\u00e7as",
    "usa duas licencas",
    "utiliza duas licen\u00e7as",
    "dos licencias",
    "deux licences",
    "zwei lizenzen",
    # p122: a split grant need not announce itself. This shape states the
    # code licence in prose and holds the content under separate terms.
    "code is licensed under",
    "codigo esta licenciado",
)

def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


# A licence TITLE, matched only in the opening block of the file. Order is by
# specificity: the AGPL/LGPL variants must be tried before plain GPL.
TITLES = [
    (re.compile(r"eclipse public license[\s,-]*v?\.?\s*2(\.0)?", re.I), "EPL-2.0"),
    (re.compile(r"eclipse public license", re.I), "EPL-1.0"),
    (re.compile(r"mozilla public license[\s,]*version\s*2(\.0)?", re.I), "MPL-2.0"),
    (re.compile(r"mozilla public license", re.I), "MPL"),
    (re.compile(r"apache license[\s,]*(?:\n|.)*?version\s*2\.0", re.I), "Apache-2.0"),
    (re.compile(r"elastic license[\s,]*2(\.0)?", re.I), "Elastic-2.0"),
    (re.compile(r"business source license", re.I), "BUSL-1.1"),
    (re.compile(r"mulan permissive software license", re.I), "MulanPSL-2.0"),
    (re.compile(r"gnu\s+affero\s+general\s+public\s+license[\s,]*version\s*3", re.I), "AGPL-3.0"),
    (re.compile(r"gnu\s+lesser\s+general\s+public\s+license[\s,]*version\s*3", re.I), "LGPL-3.0"),
    (re.compile(r"gnu\s+lesser\s+general\s+public\s+license[\s,]*version\s*2\.1", re.I), "LGPL-2.1"),
    (re.compile(r"gnu\s+general\s+public\s+license[\s,]*version\s*3", re.I), "GPL-3.0"),
    (re.compile(r"gnu\s+general\s+public\s+license[\s,]*version\s*2", re.I), "GPL-2.0"),
    (re.compile(r"creative commons attribution[- ]noncommercial[- ]sharealike\s*4\.0", re.I), "CC-BY-NC-SA-4.0"),
    (re.compile(r"creative commons attribution[- ]noncommercial\s*4\.0", re.I), "CC-BY-NC-4.0"),
    (re.compile(r"creative commons attribution[- ]sharealike\s*4\.0", re.I), "CC-BY-SA-4.0"),
    (re.compile(r"creative commons attribution\s*4\.0", re.I), "CC-BY-4.0"),
    (re.compile(r"the unlicense", re.I), "Unlicense"),
    # p122: non-OSI source-available grants. These are the highest-consequence
    # class to misread, because a reader who sees a copyleft token assumes a
    # freedom the grant does not give.
    (re.compile(r"fair\s*code\s*licen[cs]e", re.I), "FairCode-NonOSI"),
    (re.compile(r"sustainable\s*use\s*licen[cs]e", re.I), "SustainableUse-NonOSI"),
    (re.compile(r"commons\s*clause", re.I), "CommonsClause-NonOSI"),
    (re.compile(r"server\s*side\s*public\s*licen[cs]e", re.I), "SSPL-NonOSI"),
]

# OPERATIVE text — the licence's own body, reproduced. A file that merely
# NAMES a licence ("licensed under the MIT license") does not match these.
BODIES = [
    # p122: the LGPL-3.0 text begins with a copyright line, and some repos
    # commit it WITHOUT the "GNU LESSER GENERAL PUBLIC LICENSE Version 3"
    # heading. Its own incorporation sentence is then the only identifier,
    # and a title-anchored matcher reads it as an untitled GPL.
    ("this version of the gnu lesser general public license incorporates", "LGPL-3.0"),
    ("permission is hereby granted, free of charge", "MIT"),
    ("permission to use, copy, modify, and/or distribute", "ISC"),
    ("redistribution and use in source and binary forms", "BSD"),
    ("this is free and unencumbered software", "Unlicense"),
]


def _title_token(text: str) -> str | None:
    head = _norm(text[:400])
    for rx, tok in TITLES:
        if rx.search(head):
            return tok
    return None


def _body_token(text: str) -> str | None:
    tl = _norm(text).lower()
    for needle, tok in BODIES:
        if needle in tl:
            if tok == "BSD":
                return "BSD-3-Clause" if "neither the name" in tl else "BSD-2-Clause"
            return tok
    return None


def _single(text: str) -> str:
    tok = _title_token(text)
    if tok:
        return tok
    tok = _body_token(text)
    if tok:
        return tok
    tl = _norm(text).lower()
    if "general public license" in tl:
        return "GPL-UNTITLED"
    if "creative commons" in tl:
        return "CC"
    return "UNKNOWN"


# Licences as NAMED in prose, for the by-reference tier only.
NAMED = [
    (re.compile(r"\bCC[ -]?BY[ -]?NC[ -]?SA[ -]?4\.0\b", re.I), "CC-BY-NC-SA-4.0"),
    (re.compile(r"\bCC[ -]?BY[ -]?SA[ -]?4\.0\b", re.I), "CC-BY-SA-4.0"),
    (re.compile(r"\bCC[ -]?BY[ -]?4\.0\b|creative commons attribution 4\.0", re.I), "CC-BY-4.0"),
    (re.compile(r"\bApache[ -]?2(\.0)?\b", re.I), "Apache-2.0"),
    (re.compile(r"\bAGPL[ -]?v?3(\.0)?\b", re.I), "AGPL-3.0"),
    (re.compile(r"\bLGPL[ -]?v?3(\.0)?\b", re.I), "LGPL-3.0"),
    (re.compile(r"\bGPL[ -]?v?3(\.0)?\b", re.I), "GPL-3.0"),
    (re.compile(r"\bGPL[ -]?v?2(\.0)?\b", re.I), "GPL-2.0"),
    (re.compile(r"\bBSD[ -]?3[ -]?Clause\b", re.I), "BSD-3-Clause"),
    (re.compile(r"\bMIT\b", re.I), "MIT"),
]


def _named_in_order(text: str):
    """Licences NAMED in the text, in document order, de-duplicated.

    Used only for p120's tier 2 — a grant resolved by REFERENCE, where the
    file names the licence and points at another file for its body. Reported
    as SPLIT-REF so a reader is never told a body was read when none was.
    """
    hits = []
    for rx, tok in NAMED:
        m = rx.search(text)
        if m:
            hits.append((m.start(), tok))
    seen, out = set(), []
    for _, tok in sorted(hits):
        if tok not in seen:
            seen.add(tok)
            out.append(tok)
    return out


R_STUB = re.compile(r"^\s*year\s*:\s*\d{4}\s*copyright\s*holder\s*:", re.I)


def classify(text: str) -> str:
    """Return an SPDX-ish token, or a SPLIT form for a multi-grant file.

    For a split-grant file the primary grant is the one whose BODY the file
    reproduces; the other licences are named only, and a name must never win.
    When the file reproduces NO body and instead points at other files,
    the grants are resolved BY REFERENCE and reported as SPLIT-REF:A+B, so
    the weaker evidence tier stays visible in the token itself.
    """
    if not text.strip():
        return "EMPTY"
    tl = _norm(text).lower()
    # p122: the R/CRAN convention writes only YEAR + COPYRIGHT HOLDER into
    # LICENSE and names the grant in DESCRIPTION ("License: MIT + file
    # LICENSE"). The file is a STUB, not a grant, and reading it as UNKNOWN
    # invites the far worse reading "no grant". Say which tier to ask next.
    if R_STUB.match(_norm(text)) and len(text) < 400:
        return "STUB-SEE-DESCRIPTION"
    if any(m in tl for m in SPLIT_MARKERS):
        primary = _body_token(text) or _title_token(text)
        if primary:
            return f"SPLIT:{primary}"
        named = _named_in_order(text)
        if named:
            return "SPLIT-REF:" + "+".join(named)
        return "SPLIT:UNKNOWN"
    return _single(text)


if __name__ == "__main__":
    print(classify(sys.stdin.buffer.read().decode("utf-8", "replace")))
