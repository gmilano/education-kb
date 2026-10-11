#!/usr/bin/env python3
"""Classify a licence file's text into an SPDX-ish token.

Pure function over text: no network, no filesystem, no clock.

LINEAGE. The title-anchoring and split-grant behaviour is carried from
p122's classifier, which earned it against real files. The defects it must
survive, each with a fixture:

  1. GPL-2.0's own PREAMBLE names the Lesser GPL. A `"lesser" in text` test
     reads every GPL-2.0 file as LGPL.
  2. EPL-2.0's SECONDARY LICENSE clause names "GNU General Public License,
     version 2.0". A substring test reads every EPL-2.0 file as GPL-2.0.
  3. A SPLIT-GRANT file names several licences on purpose; whichever name
     appears first is arbitrary, so the split must be reported AS a split.
  4. The R/CRAN convention writes only YEAR + COPYRIGHT HOLDER into LICENSE
     and names the grant in DESCRIPTION. That file is a STUB, not a grant.

p123 adds nothing to the token vocabulary. What p123 adds is OUTSIDE this
file: the caller no longer reduces a repository to ONE token (ACTION Z).
"""
import re
import sys

SPLIT_MARKERS = (
    "portions of this software are licensed as follows",
    "portions of this project are licensed",
    "the following licenses apply",
    "usa duas licenças", "usa duas licencas",
    "utiliza duas licenças", "dos licencias",
    "deux licences", "zwei lizenzen",
    "code is licensed under", "codigo esta licenciado",
)


def _norm(text):
    return re.sub(r"\s+", " ", text).strip()


TITLES = [
    (re.compile(r"eclipse public license[\s,-]*v?\.?\s*2(\.0)?", re.I), "EPL-2.0"),
    (re.compile(r"eclipse public license", re.I), "EPL-1.0"),
    (re.compile(r"mozilla public license[\s,]*version\s*2(\.0)?", re.I), "MPL-2.0"),
    (re.compile(r"mozilla public license", re.I), "MPL"),
    (re.compile(r"apache license[\s,]*(?:\n|.)*?version\s*2\.0", re.I), "Apache-2.0"),
    (re.compile(r"elastic license[\s,]*2(\.0)?", re.I), "Elastic-2.0"),
    (re.compile(r"business source license", re.I), "BUSL-1.1"),
    (re.compile(r"mulan permissive software license", re.I), "MulanPSL-2.0"),
    (re.compile(r"european union public licence[\s,]*v?\.?\s*1\.2", re.I), "EUPL-1.2"),
    (re.compile(r"european union public licence[\s,]*v?\.?\s*1\.1", re.I), "EUPL-1.1"),
    (re.compile(r"european union public licence", re.I), "EUPL"),
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
    (re.compile(r"fair\s*code\s*licen[cs]e", re.I), "FairCode-NonOSI"),
    (re.compile(r"sustainable\s*use\s*licen[cs]e", re.I), "SustainableUse-NonOSI"),
    (re.compile(r"commons\s*clause", re.I), "CommonsClause-NonOSI"),
    (re.compile(r"server\s*side\s*public\s*licen[cs]e", re.I), "SSPL-NonOSI"),
]

BODIES = [
    ("this version of the gnu lesser general public license incorporates", "LGPL-3.0"),
    ("permission is hereby granted, free of charge", "MIT"),
    ("permission to use, copy, modify, and/or distribute", "ISC"),
    ("redistribution and use in source and binary forms", "BSD"),
    ("this is free and unencumbered software", "Unlicense"),
]

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

EUPL_REF = re.compile(
    r"licen[cs]ed under the eupl[\s,]*(?:version\s*)?(1\.[12])", re.I)
EUPL_LATER = re.compile(r"subsequent\s+versions\s+of\s+the\s+eupl", re.I)


R_STUB = re.compile(r"^\s*year\s*:\s*\d{4}\s*copyright\s*holder\s*:", re.I)
# The R/CRAN DESCRIPTION grant field, which is a NAMED grant, never a body.
DESC_FIELD = re.compile(r"^\s*License\s*:\s*(.+)$", re.I | re.M)


def _title_token(text):
    head = _norm(text[:400])
    for rx, tok in TITLES:
        if rx.search(head):
            return tok
    return None


def _body_token(text):
    tl = _norm(text).lower()
    for needle, tok in BODIES:
        if needle in tl:
            if tok == "BSD":
                return "BSD-3-Clause" if "neither the name" in tl else "BSD-2-Clause"
            return tok
    return None


def _named_in_order(text):
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


def _single(text):
    tok = _title_token(text) or _body_token(text)
    if tok:
        return tok
    tl = _norm(text).lower()
    if "general public license" in tl:
        return "GPL-UNTITLED"
    if "creative commons" in tl:
        return "CC"
    return "UNKNOWN"


def classify(text, path=""):
    """Return an SPDX-ish token, or a SPLIT form for a multi-grant file.

    `path` is advisory only: a DESCRIPTION file carries its grant in a
    `License:` FIELD and never reproduces a body, so reading it as prose
    would return UNKNOWN for a grant that is plainly stated.
    """
    if not text.strip():
        return "EMPTY"
    if path.rsplit("/", 1)[-1] == "DESCRIPTION":
        m = DESC_FIELD.search(text)
        if not m:
            return "NOT-A-GRANT"
        named = _named_in_order(m.group(1))
        return ("REF:" + "+".join(named)) if named else "UNKNOWN"
    tl = _norm(text).lower()
    if R_STUB.match(_norm(text)) and len(text) < 400:
        return "STUB-SEE-DESCRIPTION"
    flat = _norm(text)
    m = EUPL_REF.search(flat)
    if m and not _body_token(text):
        return "EUPL-%s-or-later" % m.group(1) if EUPL_LATER.search(flat) \
            else "EUPL-%s" % m.group(1)
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
    p = sys.argv[1] if len(sys.argv) > 1 else ""
    print(classify(sys.stdin.read(), p))
