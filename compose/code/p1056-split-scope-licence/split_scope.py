"""p188 / P1056 — the SPLIT-SCOPE licence: permissive CODE, CC-licensed CONTENT.

Why this exists
---------------
`ACTION MW` ran `P1054` over every row this KB publishes as `MIT`. One row fired the
SIZE signal with no restriction-vocabulary hit — the case P1054's own docstring said it
could catch but not name:

    ktwyw/python-for-engineers, LICENSE, 1 328 B, MIT-BODY-PLUS:unclassified-addition

Read, the addition is not a narrowing. It is a SCOPE SPLIT:

    Code in this repository (src/, tests/, *.py) is licensed under the MIT License.
    Teaching materials (notebooks, README files, cheatsheets, datasets created
    for this course) are licensed under CC BY 4.0.

The MIT body that follows is verbatim and unnarrowed, so P1054 is right to call the row
"MIT-body-plus" and right not to call it restricted. But publishing the row as `MIT` is
still wrong, and wrong in the half that matters: in an EDUCATION repository the asset a
studio wants is usually the CONTENT — the notebooks, the item bank, the vocabulary — and
that half carries CC BY's irrevocable ATTRIBUTION requirement. It cannot be silently
white-labelled into a client's course.

A second instance, found by probing for it, confirms the shape is a pattern and NOT a
quirk of one author — and it declares the split in a different PLACE:

    siskinskai/spedlex — README "## License": Code: MIT (LICENSE).
    Data (everything in `data/`, `schema/` and the term lists in `sources/`):
    CC BY 4.0 (LICENSE-DATA).   [LICENSE 1 077 B + LICENSE-DATA 17 023 B]

So the split may live in the licence file, in a second licence file, or only in the
README. All three are checked.

Why it matters for THIS vertical specifically
---------------------------------------------
Education repositories are code PLUS content by construction: a course is notebooks, a
tutor is an item bank, a de-identifier is a term list. The split-scope licence is
therefore the EXPECTED shape here, not an edge case — which is why this KB needs an
intake check for it rather than a one-off correction.

Deliberately NOT done here
--------------------------
No network. The caller supplies bytes, so this is testable offline (`gap 139`: this
harness cannot install dependencies). This is a SCREEN, not a verdict: it prints the
scope nouns and the second licence it matched so a human reads the file.
"""

from __future__ import annotations

import re

# A second licence IDENTIFIER appearing alongside a permissive grant.
CC_IDENT = re.compile(
    r"CC[ \-]BY(?:[ \-](?:SA|NC|ND))*(?:[ \-]?\d(?:\.\d)?)?"
    r"|Creative Commons|creativecommons\.org", re.I)

# The nouns an education repository uses for the CONTENT half.
CONTENT_NOUNS = (
    "notebook", "teaching material", "cheatsheet", "dataset", "data set",
    "slide", "course content", "term list", "item bank", "curriculum",
    "worksheet", "lesson", "schema", "documentation", "docs",
)

# A scope-assigning sentence: "<noun(s)> ... (are|is) licensed under", or "Code: MIT.
# Data: CC BY 4.0", i.e. a label-colon-licence form.
SCOPE_SENTENCE = re.compile(
    r"(?:[A-Za-z][\w ,/()*.\-]{0,120}?)\b(?:are|is)\s+licen[sc]ed\s+under\b"
    r"|^\s*(?:code|data|content|materials?|source)\s*:\s*\[?[A-Z]", re.I | re.M)

PERMISSIVE_BODY = (
    "permission is hereby granted, free of charge",   # MIT / ISC-ish
    "licensed under the apache license",
    "redistribution and use in source",               # BSD
)

VERDICT_SPLIT = "SPLIT-SCOPE:code-permissive-content-CC"
VERDICT_CC_ONLY = "CC-PRESENT:scope-unstated"
VERDICT_SINGLE = "SINGLE-SCOPE"


def classify(text: str, second_licence_files: tuple[str, ...] = ()) -> dict:
    """Screen one licence-or-README text for a code/content scope split.

    `second_licence_files` is the names of any OTHER licence files found in the tree
    (e.g. ("LICENSE-DATA",)); their presence is corroboration, never the sole signal.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    low = raw.lower()

    cc = CC_IDENT.search(raw)
    nouns = sorted({n for n in CONTENT_NOUNS if n in low})
    scoped = SCOPE_SENTENCE.search(raw) is not None
    permissive = any(p in low for p in PERMISSIVE_BODY)

    if cc and nouns and (scoped or second_licence_files):
        verdict = VERDICT_SPLIT
    elif cc:
        verdict = VERDICT_CC_ONLY
    else:
        verdict = VERDICT_SINGLE

    return {
        "verdict": verdict,
        "bytes": len(raw.encode("utf-8")),
        "second_licence": cc.group(0) if cc else None,
        "content_nouns": nouns,
        "scope_sentence": scoped,
        "permissive_body": permissive,
        "second_licence_files": list(second_licence_files),
    }


def publishable_licence(text: str, second_licence_files: tuple[str, ...] = ()) -> str:
    """What this KB may publish in a licence column.

    A split-scope row must NEVER be published as a bare permissive identifier: the
    content half is the half an education engagement usually wants.
    """
    c = classify(text, second_licence_files)
    if c["verdict"] == VERDICT_SPLIT:
        return f"MIT (code) + {c['second_licence']} (content)"
    return "read the file"
