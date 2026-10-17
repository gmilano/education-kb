"""`pass257-restriction-scan` — run the restriction vocabulary on EVERY payload,
not only on the ones shaped like MIT.

🔴 The defect this closes, measured at `p257` against three real payloads read
first-hand in the same hour:

    payload                                   bytes   p1054 verdict    p1054 hits
    opentutor/opentutor-classifier (USC)       1 812   NOT-MIT-BODY     []
    yetanalytics/project-persephone (Apache)  11 356   NOT-MIT-BODY     []
    moodlehq/moodle-plugin-ci (GPL-3.0)       35 146   NOT-MIT-BODY     []

A permissive grant, a copyleft grant and a NON-COMMERCIAL ACADEMIC licence are
byte-for-byte distinguishable and `p1054` reports them identically.  `classify()`
returns early when `MIT_BODY_MARKER` is absent and hardcodes `"hits": []`, so the
restriction vocabulary is only ever applied INSIDE the MIT-body branch.

🟢 `is_usable_permissive` is NOT wrong — `USABLE_VERDICTS` is a closed set holding
only `MIT`, so nothing restricted was ever published as permissive through it.
The defect is in the EVIDENCE, and the cost is a reader's: `NOT-MIT-BODY` with no
hits reads as *"not MIT, probably fine, check later"* when the correct reading of
the USC payload is *"non-profit use only; commercial use requires a written
agreement with the USC Stevens Center for Innovation."*  `p255` caught PageLM only
because PageLM RECITES the MIT grant before diverging at the eleventh word; a
bespoke academic licence never recites it and so never reaches the vocabulary.

🔵 This is `ACTION YM`/`ACTION YH`'s hole met in the wild for the first time with a
real payload, and it is wider than either registered: the gap is not a missing
title anchor, it is the SCOPE of the scan.

🔴 And the trap that makes a naive fix wrong, also measured rather than read:
verbatim `GPL-3.0` contains the token `noncommercial` in its own anti-circumvention
text.  A scanner that simply reports any vocabulary hit as a restriction flags
every GPL payload.  Each family therefore carries its MEASURED benign hit set, and
the verdict is computed on hits MINUS that set.
"""

# The vocabulary `p1054` carries, lifted verbatim so the two cannot drift apart
# silently — `test_restriction_scan.py` asserts this set is a superset of it.
P1054_TERMS = (
    "commercial use",
    "compete",
    "competing",
    "competitor",
    "field of use",
    "hosted, managed",
    "may not use the software to",
    "non-commercial",
    "noncommercial",
    "saas",
    "software as a service",
    "software-as-a-service",
)

# 🟢 New at `p257`, every one of them PRESENT in the USC payload and absent from
# `p1054`'s vocabulary.  An academic licence restricts with a different register
# than a commercial source-available one: it says "non-profit", not "non-commercial".
ACADEMIC_TERMS = (
    "non-profit",
    "nonprofit",
    "all rights reserved",
    "without a written agreement",
    "research purposes",
    "educational, research",
    "personal, educational",
    "academic use",
    "internal use only",
    "evaluation purposes",
)

RESTRICTION_TERMS = tuple(sorted(set(P1054_TERMS + ACADEMIC_TERMS)))

# 🔴 Anchored on the TITLE LINE, and that is a correction this instrument's own
# controls forced at `p257`.  The first draft matched these anchors anywhere in the
# body, with `agpl` ordered before `gpl` so an AGPL payload could not grade as GPL.
# It graded `moodlehq/moodle-plugin-ci`'s verbatim GPL-3.0 (35 146 B, read
# first-hand) as `AGPL` — because **GPL-3.0 section 13, at line 552 of its own
# text, is titled "Use with the GNU Affero General Public License"**.  Every
# GPL-3.0 payload in existence carries that string.  A body-wide anchor for a
# family whose name another family's own text QUOTES can only ever be wrong.
#
# 🟢 So: the family is named by the payload's own title line, which is where a
# licence states what it is.  Ordering within this tuple becomes a tiebreaker
# rather than load-bearing, and that is the point — the fix removes the dependence
# on order instead of getting the order right.
TITLE_ANCHORS = (
    ("apache license", "Apache-2.0"),
    ("gnu affero general public license", "AGPL"),
    ("gnu lesser general public license", "LGPL"),
    ("gnu general public license", "GPL"),
    ("eclipse public license", "EPL"),
    ("mozilla public license", "MPL"),
    ("isc license", "ISC"),
    ("mit license", "MIT"),
    ("bsd", "BSD"),
)

# Stage two, consulted ONLY when the title line names nothing: a BSD or ISC grant
# is routinely shipped with a bare copyright line first, so its operative clause is
# the only anchor available.  Both phrases are ones no other family's text quotes.
BODY_ANCHORS = (
    ("redistribution and use in source and binary forms", "BSD"),
    ("permission to use, copy, modify, and/or distribute this software", "ISC"),
)

# How many leading lines count as the title.  A licence names itself in its first
# line or two; `4` carries headroom for a leading blank line or a rule.
TITLE_LINES = 4

PERMISSIVE_FAMILIES = frozenset({"Apache-2.0", "BSD", "ISC", "MIT"})
COPYLEFT_FAMILIES = frozenset({"AGPL", "GPL", "LGPL", "EPL", "MPL"})

# 🔴 Measured, not assumed.  `moodlehq/moodle-plugin-ci`'s verbatim GPL-3.0 body
# (35 146 B, read first-hand at `p257`) hits `noncommercial`; verbatim Apache-2.0
# (11 356 B) hits nothing.  A family's benign set is the price of not crying wolf.
BENIGN_FAMILY_HITS = {
    "GPL": frozenset({"noncommercial"}),
    "AGPL": frozenset({"noncommercial"}),
    "LGPL": frozenset({"noncommercial"}),
}

VERDICT_RESTRICTED = "RESTRICTED:added-restriction"
VERDICT_FAMILY_PLUS = "FAMILY-PLUS-RESTRICTION:needs-a-human"
VERDICT_PERMISSIVE = "PERMISSIVE"
VERDICT_COPYLEFT = "COPYLEFT"
VERDICT_UNCLASSIFIED = "UNCLASSIFIED:no-family-no-restriction"

ALL_VERDICTS = (
    VERDICT_RESTRICTED,
    VERDICT_FAMILY_PLUS,
    VERDICT_PERMISSIVE,
    VERDICT_COPYLEFT,
    VERDICT_UNCLASSIFIED,
)

# 🔴 The consuming arm as a CLOSED allow-list, for `p248`'s reason: a verdict added
# later must not fall through into the usable branch.
USABLE_VERDICTS = frozenset({VERDICT_PERMISSIVE})


def family_of(text):
    """The licence family the payload NAMES ITSELF, or None.

    Two stages, and the order between them is the whole correctness argument:
    the title line first, because that is where a licence states its identity;
    the operative-clause anchors only when the title named nothing, because a
    BSD or ISC grant often opens with a bare copyright line.

    A body-wide search is deliberately NOT a third stage.  GPL-3.0 quotes the
    Affero GPL by name in its own section 13, so any family whose name appears
    inside another family's text is unresolvable body-wide.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    low = raw.lower()

    head = "\n".join(
        [ln for ln in low.splitlines() if ln.strip()][:TITLE_LINES]
    )
    for anchor, fam in TITLE_ANCHORS:
        if anchor in head:
            return fam

    for anchor, fam in BODY_ANCHORS:
        if anchor in low:
            return fam
    return None


def scan(text):
    """Scan ANY licence payload.  `hits` is populated unconditionally.

    The contract that distinguishes this from `p1054.classify`: there is no shape
    gate in front of the vocabulary.  A payload that mentions a restriction gets a
    non-empty `hits` whatever it looks like.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    low = raw.lower()
    nbytes = len(raw.encode("utf-8"))

    fam = family_of(raw)
    hits = tuple(t for t in RESTRICTION_TERMS if t in low)
    benign = BENIGN_FAMILY_HITS.get(fam, frozenset())
    effective = tuple(t for t in hits if t not in benign)

    if effective:
        verdict = VERDICT_RESTRICTED if fam is None else VERDICT_FAMILY_PLUS
    elif fam in PERMISSIVE_FAMILIES:
        verdict = VERDICT_PERMISSIVE
    elif fam in COPYLEFT_FAMILIES:
        verdict = VERDICT_COPYLEFT
    else:
        verdict = VERDICT_UNCLASSIFIED

    return {
        "verdict": verdict,
        "family": fam,
        "bytes": nbytes,
        "hits": hits,
        "benign_hits": tuple(sorted(t for t in hits if t in benign)),
        "effective_hits": effective,
    }


def is_usable_permissive(text):
    """True only for a payload whose family is permissive AND carries no restriction.

    A row this returns False for must not be published as permissive on any page
    of this KB.  It is deliberately independent of `p1054`: the two instruments
    agree on MIT by construction and this one also grades Apache, BSD and ISC.
    """
    return scan(text)["verdict"] in USABLE_VERDICTS
