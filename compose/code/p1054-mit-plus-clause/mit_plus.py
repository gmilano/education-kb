"""p187 / P1054 — detect an MIT BODY carrying ADDED TERMS.

Why this exists
---------------
`willwearing/graspful` (surfaced by ACTION MR on `topics/adaptive-learning?s=updated`)
ships a file called `LICENSE.md` titled **"O'Saasy License Agreement"**. Its operative
paragraph is MIT's, verbatim:

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software ... to deal in the Software without restriction ...

and it then appends a second numbered condition forbidding use of the software to
"directly compete with the original Licensor by offering it ... as a hosted, managed,
or Software-as-a-Service (SaaS) product".

That is a field-of-use restriction. The result is **not** open source and **not**
MIT, but every instrument on this shelf that classifies by matching the MIT body
returns `MIT` for it — confidently, and wrongly. This is the same failure shape as
`P971` (a LICENSE file that is Apache's header NOTICE rather than Apache's terms):
the title block and the body both look right, and the usability is opposite.

The discriminator
-----------------
Two independent signals, because either alone is weak:

1. **Size.** Canonical MIT is small and extremely consistent. Measured over the 15
   genuine MIT grants this pass verified, every one fell in **1062-1093 B**. An MIT
   body in a materially larger file has had text ADDED to it.
2. **Restriction vocabulary.** MIT's text contains no notion of competition, hosting,
   service provision, commercial/non-commercial split, or field of use. A hit on that
   vocabulary alongside an MIT body means the grant has been narrowed.

Signal 2 is the one that decides, because a licensor may legitimately add only a
copyright line (a few bytes) and size alone would then over-fire. Signal 1 is kept
because it is free and it catches an added clause written in vocabulary this list
does not yet know.

Deliberately NOT done here
--------------------------
No network. The caller supplies bytes, so this is testable offline — which matters,
because this harness cannot install dependencies (`gap 139`, `ACTION LC` limb 2).
"""

from __future__ import annotations

# Canonical MIT, as measured on this shelf. The upper bound carries headroom over the
# widest genuine row seen (openfun/ralph, 1093 B) so a long copyright line alone does
# not fire the size signal.
MIT_CANONICAL_LOW = 1020
MIT_CANONICAL_HIGH = 1150

MIT_BODY_MARKER = "permission is hereby granted, free of charge"

# Vocabulary MIT does not contain. Lower-cased substring match.
RESTRICTION_TERMS = (
    "compete",
    "competing",
    "competitor",
    "software-as-a-service",
    "software as a service",
    "saas",
    "hosted, managed",
    "non-commercial",
    "noncommercial",
    "commercial use",
    "field of use",
    "may not use the software to",
)

VERDICT_MIT = "MIT"
VERDICT_RESTRICTED = "NOT-OPEN-SOURCE:added-restriction"
VERDICT_MIT_PLUS = "MIT-BODY-PLUS:unclassified-addition"
VERDICT_NOT_MIT = "NOT-MIT-BODY"


def classify(text: str) -> dict:
    """Classify a licence file that may or may not be MIT.

    Returns a dict with the verdict, the byte length, and the restriction terms hit,
    so a caller can print the evidence rather than just the label.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    low = raw.lower()
    nbytes = len(raw.encode("utf-8"))

    if MIT_BODY_MARKER not in low:
        return {
            "verdict": VERDICT_NOT_MIT,
            "bytes": nbytes,
            "mit_body": False,
            "hits": [],
            "excess": 0,
        }

    hits = sorted({t for t in RESTRICTION_TERMS if t in low})
    excess = max(0, nbytes - MIT_CANONICAL_HIGH)

    if hits:
        verdict = VERDICT_RESTRICTED
    elif excess > 0:
        verdict = VERDICT_MIT_PLUS
    else:
        verdict = VERDICT_MIT

    return {
        "verdict": verdict,
        "bytes": nbytes,
        "mit_body": True,
        "hits": hits,
        "excess": excess,
    }


def is_usable_permissive(text: str) -> bool:
    """True only for an MIT grant with nothing added to it.

    A row this returns False for must not be published as `MIT` on any page of this KB.
    """
    return classify(text)["verdict"] == VERDICT_MIT
