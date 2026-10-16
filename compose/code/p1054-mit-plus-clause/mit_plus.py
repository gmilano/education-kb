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

The `p252` extension: a rider that makes the file SHORTER
---------------------------------------------------------
`ACTION XI` (registered `p248`, carried silently through `p249`/`p250`, re-registered as
`ACTION XQ` at `p251`) measured this instrument against the canonical **Commons Clause**
body and it answered `MIT` / `is_usable_permissive: True` — on a payload whose operative
sentence is *"the License does not grant to you, the right to Sell the Software"*.

Two independent reasons it missed, and both had to be closed:

1. **Vocabulary.** The Commons Clause says *Sell*, not *compete*, *SaaS* or
   *non-commercial*. `RESTRICTION_TERMS` knew none of its words.
2. **Length, and this is the structural half.** `excess` is a byte-EXCESS test:
   `max(0, nbytes - MIT_CANONICAL_HIGH)`. The fixture is `621` B. A test that can only
   see bytes ADDED above the band is blind by construction to a rider that leaves the
   file **shorter** than canonical MIT — here because the MIT body itself is abridged to
   its first sentence, with the grant's enumerated rights dropped.

So `p252` adds a third length state. An MIT body in a payload **below**
`MIT_CANONICAL_LOW` is not a narrow MIT grant and not a wide one: it is **ungradeable**,
because the text that would carry the rest of the grant is not there to read.

The hazard this deliberately does NOT repeat
--------------------------------------------
`p248` measured the failure mode shared by `ACTION XE`, `XG` and `XI`: **a new state
emitted without closing the arm that consumes it makes the verdict worse, not better** —
the caller falls through the unknown label into the permissive branch. So usability here
is a CLOSED SET (`USABLE_VERDICTS`), not a comparison against one constant, and
`ALL_VERDICTS` exists so a control can prove every other state is refused. A later pass
that adds a sixth verdict and forgets the arm will fail `test_every_verdict_is_graded`
rather than silently bless it.
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

# `p252` / `ACTION XQ` — the Commons Clause rider's own vocabulary.  Kept separate from
# RESTRICTION_TERMS so a hit can be reported as a NAMED rider rather than as generic
# restriction vocabulary: the Commons Clause is a specific, widely-copied instrument and
# naming it is what lets a reader act on the row.
RIDER_ANCHORS = (
    "commons clause",
    "right to sell the software",
    "the license does not grant to you",
)

# `p252` — the third length state.  Canonical MIT is tightly clustered (1062-1093 B
# measured over 15 genuine grants); the band below carries headroom at both ends.
LENGTH_SHORT = "SHORTER-THAN-CANONICAL"
LENGTH_IN_BAND = "IN-BAND"
LENGTH_LONG = "LONGER-THAN-CANONICAL"

VERDICT_MIT = "MIT"
VERDICT_RESTRICTED = "NOT-OPEN-SOURCE:added-restriction"
VERDICT_MIT_PLUS = "MIT-BODY-PLUS:unclassified-addition"
VERDICT_NOT_MIT = "NOT-MIT-BODY"
# `p252` — an MIT body in a payload too small to CONTAIN the MIT grant.  Not a verdict
# about the licensor's intent; a verdict about what can be read.
VERDICT_SHORT = "MIT-BODY-SHORT:ungradeable"

# Every state `classify` can return.  A control iterates this, so adding a verdict
# without grading it fails the suite.
ALL_VERDICTS = (
    VERDICT_MIT,
    VERDICT_RESTRICTED,
    VERDICT_MIT_PLUS,
    VERDICT_NOT_MIT,
    VERDICT_SHORT,
)

# 🔴 THE CONSUMING ARM, as a closed set.  `p248`'s measured hazard is a new state
# falling through into the permissive branch; an allow-list cannot fall through.
USABLE_VERDICTS = frozenset({VERDICT_MIT})


def length_state(nbytes: int) -> str:
    """Which side of the canonical MIT band this payload sits on."""
    if nbytes < MIT_CANONICAL_LOW:
        return LENGTH_SHORT
    if nbytes > MIT_CANONICAL_HIGH:
        return LENGTH_LONG
    return LENGTH_IN_BAND


def classify(text: str) -> dict:
    """Classify a licence file that may or may not be MIT.

    Returns a dict with the verdict, the byte length, and the restriction terms hit,
    so a caller can print the evidence rather than just the label.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    low = raw.lower()
    nbytes = len(raw.encode("utf-8"))

    length = length_state(nbytes)

    if MIT_BODY_MARKER not in low:
        return {
            "verdict": VERDICT_NOT_MIT,
            "bytes": nbytes,
            "mit_body": False,
            "hits": [],
            "riders": [],
            "excess": 0,
            "length_state": length,
        }

    hits = sorted({t for t in RESTRICTION_TERMS if t in low})
    riders = sorted({a for a in RIDER_ANCHORS if a in low})
    excess = max(0, nbytes - MIT_CANONICAL_HIGH)

    # Order matters, and it is an EVIDENCE order: a named rider or known restriction
    # vocabulary says WHAT is wrong, which is worth more to a reader than "too short".
    # The length state catches only what the vocabulary does not know.
    if riders or hits:
        verdict = VERDICT_RESTRICTED
    elif length == LENGTH_SHORT:
        verdict = VERDICT_SHORT
    elif excess > 0:
        verdict = VERDICT_MIT_PLUS
    else:
        verdict = VERDICT_MIT

    return {
        "verdict": verdict,
        "bytes": nbytes,
        "mit_body": True,
        "hits": hits,
        "riders": riders,
        "excess": excess,
        "length_state": length,
    }


def is_usable_permissive(text: str) -> bool:
    """True only for an MIT grant with nothing added to it.

    A row this returns False for must not be published as `MIT` on any page of this KB.
    """
    return classify(text)["verdict"] in USABLE_VERDICTS
