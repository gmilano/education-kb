#!/usr/bin/env python3
"""`pass258-content-licence-family` — the licence class these shelves carry MOST
is the one the live gate cannot name at all.

🔴 The defect, measured at `p258` against the seven canonical Creative Commons
payloads read first-hand from `spdx/license-list-data` in the same hour, each run
through `pass257-restriction-scan.scan()`:

    payload           bytes   p257 family   p257 verdict                            hits
    CC0-1.0           7 048   NONE          UNCLASSIFIED:no-family-no-restriction   []
    CC-BY-4.0        17 023   NONE          UNCLASSIFIED:no-family-no-restriction   []
    CC-BY-SA-4.0     18 375   NONE          UNCLASSIFIED:no-family-no-restriction   []
    CC-BY-ND-4.0     16 830   NONE          UNCLASSIFIED:no-family-no-restriction   []
    CC-BY-NC-4.0     17 649   NONE          RESTRICTED:added-restriction            [noncommercial]
    CC-BY-NC-SA-4.0  19 018   NONE          RESTRICTED:added-restriction            [noncommercial]
    CC-BY-NC-ND-4.0  17 452   NONE          RESTRICTED:added-restriction            [noncommercial]

🟢 **The NC half is already caught**, and that is worth stating plainly: `p257`'s
vocabulary was built for commercial source-available licences and it fires correctly
on Creative Commons NonCommercial without having been designed for it.  Nothing
non-commercial was ever published as permissive.

🔴 **The hole is the other three rows.**  `CC0-1.0` is a public-domain dedication —
the most permissive grant that exists — and `CC-BY-ND-4.0` forbids distributing a
derivative at all, which is precisely what a studio does with material.  The live
gate reports them IDENTICALLY: `UNCLASSIFIED:no-family-no-restriction`, zero hits.
🔵 And the reason is measurable rather than arguable: the vocabulary contains no term
for a derivative restriction.  `[t for t in RESTRICTION_TERMS if "deriv" in t]` is
empty, so `ND` is not a near-miss — it is out of scope.

🔴 Why this matters more here than it would in another industry: **instructional
material is licensed as CONTENT, not as software.**  A census of the shelves at
`p258` found `828` Creative Commons licence tokens, of which 🔴 **`191` (`23.1 %`)
carry a `NonCommercial` term** and `216` carry `ShareAlike` — the single largest
licence class on this base, and the one its standing gate could not name.

🟢 `is_usable_permissive` was NOT wrong: `USABLE_VERDICTS` is closed on `{MIT}`, so
no CC payload was ever published as a usable permissive grant.  🔵 **The defect is in
the EVIDENCE, which is exactly `p257`'s own lesson repeating one layer out** — and
`p258`'s addition to it is that the lesson repeated on a population two orders of
magnitude larger than the one `p257` found it on.

🔵 Per `p256`: an instrument must publish the SIZE of what it covers beside the claim
that it covers it.  `coverage()` does that, and `--census` prints it.
"""
import re
import sys

# 🟢 The anchor is the CC name, matched in a WINDOW of leading lines rather than on
# line 1 alone.  Measured, not assumed: `CC0-1.0`'s own identifier sits on line 2,
# under the generic heading `Creative Commons Legal Code`.  A line-1-only anchor
# reads CC0 as unidentified, and `test_content_licence.py` pins that case.
TITLE_WINDOW = 6
CC_ANCHOR = "creative commons"

# The three restriction/condition axes, as Creative Commons spells them in its own
# title line and operative text.  Deliberately NOT lazy: `ACTION TB`'s
# lazy-quantifier lint runs over this directory.
AXIS_SHARE_ALIKE = "sharealike"
AXIS_NON_COMMERCIAL = "noncommercial"
AXIS_NO_DERIVATIVES = "noderivatives"

# 🟢 The operative markers that separate a GRANT from a POINTER to one.  `P1065`
# (p254) settled that a pointer is not a grant; this is that predicate for content
# licences.  Measured across all seven payloads: every `4.0` text contains
# `By exercising the Licensed Rights` exactly once and `Licensed Rights` 13–14 times;
# `CC0-1.0` contains neither and carries `Copyright and Related Rights` 7 times.
OPERATIVE_MARKERS = ("licensed rights", "copyright and related rights")

# The real pointer this was built against: `datacarpentry/r-socialsci`'s `LICENSE.md`
# (`3 357` B) names the Creative Commons Attribution licence in prose and LINKS to the
# legal text.  It names a grant; it does not make one.
VERSION = re.compile(r"([0-9])\.([0-9])")

VERDICT_RESTRICTED_NC = "CONTENT-RESTRICTED:non-commercial"
VERDICT_RESTRICTED_ND = "CONTENT-RESTRICTED:no-derivatives"
VERDICT_COPYLEFT = "CONTENT-COPYLEFT:share-alike"
VERDICT_PERMISSIVE = "CONTENT-PERMISSIVE"
VERDICT_POINTER = "CONTENT-POINTER:not-a-grant"
VERDICT_NOT_CC = "NOT-A-CONTENT-LICENCE"

ALL_VERDICTS = frozenset({
    VERDICT_RESTRICTED_NC, VERDICT_RESTRICTED_ND, VERDICT_COPYLEFT,
    VERDICT_PERMISSIVE, VERDICT_POINTER, VERDICT_NOT_CC,
})

# 🔴 The studio-facing point of the whole instrument: these two verdicts mean "cannot
# ship in a paid client deliverable", and they are a CLOSED set so that a later pass
# widening the vocabulary cannot silently widen what counts as usable.
UNUSABLE_VERDICTS = frozenset({VERDICT_RESTRICTED_NC, VERDICT_RESTRICTED_ND})


def _head(text):
    """The leading window, folded.  Keeps the title-line discipline p198/p257 settled."""
    return "\n".join(text.splitlines()[:TITLE_WINDOW]).lower()


def is_content_licence(text):
    """Does the CC anchor appear in the title window?  Anchor only — says nothing
    about whether the payload actually GRANTS anything."""
    return CC_ANCHOR in _head(text)


def names_content_licence(text):
    """-> does the payload mention Creative Commons ANYWHERE?

    🔴 Measured against this instrument's own first draft, which graded the real
    Carpentries pointer `NOT-A-CONTENT-LICENCE`: a CC legal text identifies itself in
    its first line, but a POINTER buries the name in prose.
    `datacarpentry/r-socialsci`'s `LICENSE.md` opens with YAML frontmatter and an
    `## Instructional Material` heading, and does not say *"Creative Commons"* until
    line `8`.  🟢 **So the title window is the right test for a GRANT and the wrong
    test for a POINTER**, and the two need separate predicates.

    🔵 Why a body-wide anchor is safe HERE and was not safe for `p257`'s family
    detection: `p257` found that `GPL-3.0` §13 quotes the Affero licence's name, so
    family anchors cannot be matched body-wide.  No OSI software licence text names
    Creative Commons, measured across this base's own fixtures — and this predicate
    is used ONLY to reach the pointer branch, never to assign a family.
    """
    return CC_ANCHOR in text.lower()


def is_grant(text):
    """🟢 `P1065` for content licences: a payload that NAMES a Creative Commons
    licence is not the same as one that IS one."""
    low = text.lower()
    return any(marker in low for marker in OPERATIVE_MARKERS)


def axes_of(text):
    """-> the set of axes present, read from the whole payload rather than the title.

    🔵 Measured rather than inferred: in the `4.0` texts each axis token appears in the
    title line AND in the operative sections (`ShareAlike` 5×, `NonCommercial` 8–9×,
    `NoDerivatives` 3×), and appears in NO payload that does not carry that axis.  The
    token is therefore load-bearing on its own, and the title line is corroboration.
    """
    low = text.lower().replace("-", "").replace(" ", "")
    found = set()
    for axis in (AXIS_SHARE_ALIKE, AXIS_NON_COMMERCIAL, AXIS_NO_DERIVATIVES):
        if axis in low:
            found.add(axis)
    return found


def family_of_content(text):
    """-> an SPDX-shaped identifier for a Creative Commons payload, or None.

    Returns None for anything that is not a CC GRANT — including a CC pointer, which
    `content_verdict` reports separately rather than silently treating as a grant.
    """
    if not is_content_licence(text) or not is_grant(text):
        return None

    head = _head(text)
    if "cc0" in head.replace(" ", ""):
        return "CC0-1.0"

    axes = axes_of(text)
    parts = ["CC", "BY"]
    if AXIS_NON_COMMERCIAL in axes:
        parts.append("NC")
    if AXIS_NO_DERIVATIVES in axes:
        parts.append("ND")
    # 🔵 CC's own ordering: NC precedes ND precedes SA, and SA and ND are mutually
    # exclusive by construction (you cannot require share-alike on a derivative you
    # may not make).  Pinned as a control.
    if AXIS_SHARE_ALIKE in axes and AXIS_NO_DERIVATIVES not in axes:
        parts.append("SA")

    version = VERSION.search(head)
    ident = "-".join(parts)
    return f"{ident}-{version.group(1)}.{version.group(2)}" if version else ident


def content_verdict(text):
    """-> one of ALL_VERDICTS.  The studio question, answered in one call.

    🔴 The ORDER is the whole point: `NC` is checked before `ND` before `SA`, because a
    payload carrying more than one axis is as unusable as its strictest axis, and a
    reader given only the weakest verdict would ship it.
    """
    if not is_content_licence(text):
        # 🟢 The pointer branch: names a Creative Commons licence, does not identify
        # as one and does not grant.  `P1065`'s class on content licences.
        if names_content_licence(text) and not is_grant(text):
            return VERDICT_POINTER
        return VERDICT_NOT_CC
    if not is_grant(text):
        return VERDICT_POINTER

    axes = axes_of(text)
    if AXIS_NON_COMMERCIAL in axes:
        return VERDICT_RESTRICTED_NC
    if AXIS_NO_DERIVATIVES in axes:
        return VERDICT_RESTRICTED_ND
    if AXIS_SHARE_ALIKE in axes:
        return VERDICT_COPYLEFT
    return VERDICT_PERMISSIVE


def is_usable_in_deliverable(text):
    """🟢 Closed-set, like `p257`'s `is_usable_permissive`: a verdict this instrument
    does not know is NOT usable.  A new verdict added without updating the set fails
    closed, and `test_content_licence.py` asserts that direction."""
    verdict = content_verdict(text)
    if verdict in UNUSABLE_VERDICTS:
        return False
    return verdict in (VERDICT_PERMISSIVE, VERDICT_COPYLEFT)


SHELVES = (
    "README.md",
    "agents/top.md", "agents/trending.md",
    "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md",
    "intel/market.md", "intel/trends.md", "intel/open-gaps.md",
    "compose/patterns.md",
)

# Deliberately NOT lazy — longest alternatives first so `CC-BY-NC-SA-4.0` cannot be
# truncated to `CC-BY` by an earlier branch.  That truncation is `p251-prefix-collision`'s
# class, met on licence identifiers instead of slugs, and it is pinned as a control.
SHELF_TOKEN = re.compile(
    r"CC0-1\.0|CC-BY-NC-ND-[0-9.]+|CC-BY-NC-SA-[0-9.]+|CC-BY-NC-[0-9.]+"
    r"|CC-BY-SA-[0-9.]+|CC-BY-ND-[0-9.]+|CC-BY-[0-9.]+"
    r"|CC-BY-NC-ND|CC-BY-NC-SA|CC-BY-NC|CC-BY-SA|CC-BY-ND|CC-BY|CC0"
)


def classify_token(token):
    """Grade a licence IDENTIFIER as written on a shelf, without a payload.

    🔵 Weaker evidence than a payload read and labelled as such: a shelf cell is a
    claim a previous pass made, not a grant this pass read.
    """
    folded = token.upper()
    if "NC" in folded:
        return VERDICT_RESTRICTED_NC
    if "ND" in folded:
        return VERDICT_RESTRICTED_ND
    if "SA" in folded:
        return VERDICT_COPYLEFT
    return VERDICT_PERMISSIVE


def coverage(root="."):
    """-> (total, {verdict: count}).  🟢 `p256`'s lesson, built in: the instrument
    publishes the SIZE of the population it covers beside the claim that it covers it.
    A missing shelf is skipped and ANNOUNCED by the caller, never counted as zero."""
    counts = {}
    total = 0
    missing = []
    for shelf in SHELVES:
        try:
            with open(f"{root}/{shelf}", encoding="utf-8", errors="replace") as fh:
                body = fh.read()
        except FileNotFoundError:
            missing.append(shelf)
            continue
        for token in SHELF_TOKEN.findall(body):
            verdict = classify_token(token)
            counts[verdict] = counts.get(verdict, 0) + 1
            total += 1
    return total, counts, missing


def main(argv):
    if len(argv) > 1 and argv[1] == "--census":
        root = argv[2] if len(argv) > 2 else "."
        total, counts, missing = coverage(root)
        if missing:
            # 🔴 p257: a skip that does not announce itself is indistinguishable from
            # coverage.  This one announces itself.
            print(f"NOTE: {len(missing)} shelf/shelves ABSENT, SKIPPED not passed: "
                  f"{', '.join(missing)}")
        print(f"content-licence tokens covered: {total}")
        for verdict in sorted(counts):
            share = 100.0 * counts[verdict] / total if total else 0.0
            print(f"  {verdict:<34} {counts[verdict]:>5}  ({share:.1f} %)")
        unusable = sum(counts.get(v, 0) for v in UNUSABLE_VERDICTS)
        share = 100.0 * unusable / total if total else 0.0
        print(f"  {'UNUSABLE IN A PAID DELIVERABLE':<34} {unusable:>5}  ({share:.1f} %)")
        return 0

    if len(argv) > 1:
        for path in argv[1:]:
            with open(path, encoding="utf-8", errors="replace") as fh:
                body = fh.read()
            print(f"{path}\t{family_of_content(body) or 'NONE'}\t{content_verdict(body)}")
        return 0

    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
