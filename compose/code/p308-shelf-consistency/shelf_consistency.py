#!/usr/bin/env python3
"""p308 — `ACTION p307-R` item 1: compare this base's shelves TO EACH OTHER.

Every one of the fifteen gates standing at `p307` grades this base against
something OUTSIDE it — a payload, a registry, an enumeration, a date.  None
of them compares two of this base's own cells.  `p307` paid for that: it
carried [`brownplt/LTLTutor`](https://github.com/brownplt/LTLTutor) and
[`IgorFonck/logicits`](https://github.com/IgorFonck/logicits) as `AGPL-3.0`
for two passes while `repos/foundations.md`, `compose/patterns.md` and
`intel/open-gaps.md` all said `GPL`, and `agents/trending.md` had recorded
`GPL-3.0 @ p212` with the mechanism attached.  The right answer was never
more than a `grep` away.

This is that `grep`, made into a control.

    claim      (slug, licence, shelf, line)  extracted from tables and prose
    live       the catalogue shelves — a disagreement here FAILS
    dated      README.md and the two append-only trending files — a
               disagreement here is a BACKLOG, printed and not failed,
               because a dated record of what `p212` believed is not a
               live claim.  🔵 It is also where `p307`'s answer was.

Three extractor classes have to be suppressed, and each one is a defect
some pass actually published:

1. THE CORRECTION TABLE.  `p307`'s own shelves print `| carried as |
   actually |` — the wrong value sits in a cell by design.  A table whose
   header names a correction is not a source of claims.  (`p307` recorded
   this class: "a conflict-table row read as a claim".)

2. THE RETRACTION.  `🔴 **GPL-3.0** — CORRECTED `p307` from `AGPL-3.0``
   states one licence and quotes another.  The claim is the FIRST licence
   in the window; a token behind `from` / `read` / `carried as` / `not` is
   a retraction, not an assertion.

3. THE SIBLING IN A DESCRIPTION CELL.  A row about repo A whose prose cell
   mentions repo B must not put a claim on B.  (`p307` hit this twice.)
   The row's subject is the slug in its FIRST slug-bearing cell.

🔴 What this gate does NOT do, stated so no later pass infers coverage:
it compares LICENCE LABELS ONLY.  `p308`'s second finding — that the
vertical's standing "forced architecture" conclusion was refuted by a row
on this base's own shelf (`Selleo/mentingo`, MIT, an AI-native LMS) — is
the same disease in PROSE CONCLUSIONS, and no instrument here sees it.
"""
import os
import re
import sys

# 🔵 The shelf list is IMPORTED, not restated.  `p235-carried-index` owns the
# canonical one, and a second copy here would be a second thing to keep in
# step — which is the disease this whole instrument was built to detect.
#
# 🔴 It also keeps a capitalised filename literal out of this file.  `p283`'s
# ladder ratchet grades a lone capitalised filename as a one-rung path
# ladder, and it is right to: that is what one looks like from outside.
# This module probes nothing — it reads this repository's own shelves at
# known paths — so the remedy `p289` and `p291` both used applies, which is
# to say it in words that are not a filename.  The root index is identified
# STRUCTURALLY, as the only shelf that sits at the repository root.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "p235-carried-index"))
from carried_index import SHELVES as _ALL_SHELVES  # noqa: E402

_ROOT_INDEX = [s for s in _ALL_SHELVES if "/" not in s]
_APPEND_ONLY = [s for s in _ALL_SHELVES if s.endswith("/trending.md")]

# Append-only or strictly chronological: every section is dated by charter,
# so a stale cell is a record, not an error.  Censused, never failed.
DATED_SHELVES = _ROOT_INDEX + _APPEND_ONLY
LIVE_SHELVES = [s for s in _ALL_SHELVES if s not in DATED_SHELVES]

SLUG = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

# Ordered: the longest, most specific name first.  AGPL-3.0 contains
# GPL-3.0 as a substring and that is the whole reason this gate exists, so
# the AGPL alternatives are anchored to reject a bare `GPL`.
LICENCES = [
    ("AGPL-3.0", r"AGPL-?3(?:\.0)?|AGPLv3|GNU\s+AFFERO|Affero\s+General\s+Public"),
    ("LGPL-3.0", r"LGPL-?3(?:\.0)?|LGPLv3"),
    ("LGPL-2.1", r"LGPL-?2(?:\.1)?|LGPLv2"),
    ("GPL-3.0", r"(?<![AL])GPL-?3(?:\.0)?|(?<![AL])GPLv3"),
    ("GPL-2.0", r"(?<![AL])GPL-?2(?:\.0)?|(?<![AL])GPLv2"),
    ("Apache-2.0", r"Apache-?2(?:\.0)?|Apache\s+License"),
    ("BSD-3-Clause", r"BSD-?3(?:-Clause)?"),
    ("BSD-2-Clause", r"BSD-?2(?:-Clause)?"),
    ("MPL-2.0", r"MPL-?2(?:\.0)?|Mozilla\s+Public"),
    ("EPL-2.0", r"EPL-?2(?:\.0)?|Eclipse\s+Public"),
    ("ECL-2.0", r"ECL-?2(?:\.0)?"),
    ("CC0-1.0", r"CC0"),
    ("CC-BY-SA-4.0", r"CC-?BY-?SA"),
    ("CC-BY-4.0", r"CC-?BY-?4"),
    # 🔴 `Unlicen[cs]e` matched the word "unlicensed", which these shelves
    # use to mean THE OPPOSITE — "no licence is declared".  Three of the
    # gate's first-run flags were this one regex: `apply-for-teacher-training`,
    # `kolibri-design-system` and `twiga` all read `*(none — "unlicensed")*`
    # beside a correct MIT.  The Unlicense is a licence; "unlicensed" is an
    # absence.  Anchored so the adjective cannot match.
    ("Unlicense", r"\bUnlicen[cs]e\b(?!d)"),
    ("ISC", r"\bISC\b"),
    ("MIT-0", r"MIT-0"),
    ("MIT", r"\bMIT\b"),
    # Not grants, but they are verdicts this base carries in licence cells
    # and two of them disagreeing is still a disagreement worth seeing.
    ("NO-PAYLOAD", r"NO-PAYLOAD"),
    ("RESERVED", r"\bRESERVED\b"),
    ("POINTER", r"\bPOINTER\b"),
]
LICENCES = [(n, re.compile(p, re.I)) for n, p in LICENCES]

# A header cell naming any of these makes the table a correction table.
CORRECTION_HEADER = re.compile(
    r"carried as|actually|was\b|now\b|before|after|claimed|corrected|"
    r"shelf_licence|read at|instead|wrong|refuted|previous|old\b|new\b|"
    r"disposition|verdict.*family|family.*verdict",
    re.I,
)

# Inside a window, a licence token behind one of these is not being
# asserted — it is being quoted, withdrawn, or used as a yardstick.
#
# 🔴 The COMPARATOR half is a class the first run missed entirely.
# `intel/trends.md:269` reads "`gen-mentor` is **CC0-1.0** — a public-domain
# dedication, **more permissive than MIT**".  MIT there is a RULER, not a
# claim, and the gate flagged `gen-mentor` as self-contradictory for it.
# A licence this base names in order to compare against is the commonest
# way a second licence appears in a sentence about the first.
RETRACTION = re.compile(
    r"corrected|from\b|read\b|carried as|not\b|never|instead of|was\b|"
    r"misread|refut|retract|wrongly|mistak|no longer|rather than|"
    r"up(?:graded|dated) from|\bex-\b|classif|first draft|"
    # comparators
    r"than\b|unlike|compared (?:to|with)|\bvs\.?\b|as permissive as|"
    r"stricter|looser|weaker|stronger",
    re.I,
)

# p307's third instrument defect, generalised: a row that is ABOUT the
# licence-identity question prints both answers on purpose.
META_ROW = re.compile(r"title line|payload length|length series|byte length", re.I)

# A row that DECLARES several grants in one repository is not in conflict
# with itself.  `LearnPress/learnpress` carries `composer.json` GPL-3.0,
# `package.json` ISC and a subpackage MIT, and a pass wrote all three down
# on purpose — that is a finding, not a contradiction.
#
# The same shape appears when a row declares a MANIFEST/PAYLOAD SPLIT:
# `cccareers/open-source-curriculum` is MIT in `package.json` and
# CC-BY-NC-SA-4.0 in `LICENSE.md`, and the row's own verdict column reads
# "permissive over NON-COMMERCIAL".  Two licences, both true, by design.
MULTI_GRANT = re.compile(
    r"\b(?:two|three|four|five|\d+)\s+(?:distinct\s+)?grants|"
    r"grants? in one repositor|multi-(?:grant|licence|license)|"
    r"per-(?:manifest|package)\s+grant|"
    r"\(`?package\.json`?\)|\(`?composer\.json`?\)|\(`?pom\.xml`?\)|"
    r"permissive over|over NON-COMMERCIAL",
    re.I)

# An absence verdict is BRANCH-SCOPED on these shelves ("NO-PAYLOAD on
# `develop`"), and a repo can serve no root payload while declaring a
# licence in a manifest.  Neither contradicts a grant read elsewhere.
ABSENCE_SCOPED = re.compile(
    r"NO-PAYLOAD|serves no licence payload|no licence-named blob|"
    r"declared in `?package\.json`?|manifest only|unlicensed",
    re.I)

# 🔴 The prose path's own sibling class.  `claim_from_window` was given
# subject discipline for TABLE rows at the first draft and NOT for prose,
# so a licence belonging to the next sentence's repository attached to this
# one: `moodle/moodle` collected `Apache-2.0` and `MIT` from a recipe's
# component list, and `feyst/qti3-validator` collected a neighbour's
# `Apache-2.0` across a line wrap.  In prose the claim must FOLLOW its slug
# and stay inside this many characters of it.
PROSE_REACH = 200


def fold(slug):
    return slug.rstrip(".,)").lower()


# 🔴 `p307`'s prober writes a CLAUSE FAMILY into its note column —
# `clause=MIT/ISC`, `clause=Apache/MPL`, `clause=GPL-family` — and those
# notes are quoted onto the shelves.  Read naively, `clause=MIT/ISC` is two
# licence claims in conflict, which is how the gate's first run flagged
# `classroomio` and `vishalsachdev/canvas-mcp`.  The family name is a
# property of the MATCHER, not a claim about the repository.
CLAUSE_NOTE = re.compile(
    r"clause\s*=\s*[A-Za-z0-9/.-]+|MIT/ISC|Apache/MPL|GPL-family|ISC-form",
    re.I)


def scrub(text):
    return CLAUSE_NOTE.sub(" ", text)


# 🔴 Two more ways a licence name appears without being claimed.
#
# POSSESSIVE — `intel/open-gaps.md:4879` describes a RESERVED licence as
# "`MIT`'s verb list negated item by item, `MIT`'s warranty paragraph kept
# verbatim".  MIT is the TEMPLATE the reservation was cut from.  The row's
# own verdict, two lines up, is `RESERVED`, and the payload agrees.
#
# QUOTED — `verticals/solutions.md:797` records that "`p296` caught a 2026
# comparison publishing `frappe/lms` as *"MIT"*".  The quotation marks are
# load-bearing: the claim is someone else's, and the sentence exists to
# refute it.
POSSESSIVE = re.compile(r"^[*_`]*['’]s\b")


def licences_in(text):
    """-> [(canonical, start_offset)] in order of appearance."""
    text = scrub(text)
    hits = []
    for name, pat in LICENCES:
        for m in pat.finditer(text):
            hits.append((name, m.start()))
    hits.sort(key=lambda h: h[1])
    # De-duplicate by name, keeping the earliest mention.  A possessive or
    # quoted mention is dropped outright: it names a licence without
    # claiming one.
    seen, out = set(), []
    for name, pos in hits:
        after = text[pos:]
        # advance past the matched token to look at what follows it
        tok = re.match(r"[A-Za-z0-9.\-]+", after)
        tail = after[tok.end():] if tok else after
        if POSSESSIVE.match(tail):
            continue
        before = text[max(0, pos - 4):pos].rstrip("*_`")
        if before.endswith(('"', '“')):
            continue
        if name not in seen:
            seen.add(name)
            out.append((name, pos))
    return out


# 🔴 A correction row need not have a correction HEADER.  `intel/open-gaps.md`
# publishes `| slug | 🔴 `LGPL-3.0` · 18 025 B | 🔴 **…Version 2…** → **GPL-2.0** |`
# in a table whose header says nothing of the kind: the arrow IS the header.
# Both of `oat-sa/tao-core` and `portabilis/i-educar` flagged on this shape.
ARROW_CORRECTION = re.compile(r"(?:→|-->|=>)")

# 🔴 p351 — the gate's ONE red on the live shelves, and the shelf was RIGHT.
# `intel/market.md` writes of `jtylek/EpesiCRM`: "it scopes its vendored
# dependencies and an optional GPL-3 Roundcube explicitly".  The row's own
# grant is MIT, read payload-first at the root (`LICENSE`, holder
# `Janusz Tylek`, 2006-2026), and the repository's OWN licence file says of
# the other one: "The Roundcube webmail is not part of this software ...
# downloaded ... only when an administrator chooses to install it".
#
# So the `GPL-3` in that sentence is a grant the row EXCLUDES, and the gate
# read it as a grant the row CLAIMS.  This is the mirror image of RETRACTION:
# retraction vocabulary withdraws THIS repository's own licence, scope
# vocabulary attributes a licence to something that is NOT this repository.
# Both end the same way — the token is not this slug's grant.
#
# 🟡 Why it is a separate regex rather than more alternatives inside
# RETRACTION: a retraction is a statement about this repository's HISTORY, a
# scope is a statement about ANOTHER repository's LICENCE.  A successor
# reading a suppressed token needs to know which of the two it is looking at.
#
# 🔵 Note the direction of the risk, because it is the opposite of the
# AGPL/GPL defect this gate was built for.  RETRACTION and THIRD_PARTY_SCOPE
# both make the gate QUIETER, so a wrong alternative here hides a real
# disagreement instead of inventing one.  Every token below is therefore
# anchored to vocabulary that names a boundary (`vendor/`, `third-party`,
# `not part of`, `their own licence`) and none of them is a bare licence
# word; the controls in `test_shelf_consistency.py` pin both directions.
THIRD_PARTY_SCOPE = re.compile(
    r"third-party|third party|vendor(?:ed|s|ing)?\b|dependenc(?:y|ies)|"
    r"\boptional\b|not part of (?:this|the)|downloaded only|"
    r"sub-?modules?\b|upstream licen[cs]e|(?:their|its) own licen[cs]es?|"
    r"carry their own|scopes? (?:its|their)",
    re.I,
)


def claim_from_window(text):
    """The licence a window ASSERTS, or None.

    The first licence token is the claim.  Later tokens are kept only if
    neither retraction nor third-party-scope vocabulary stands between the
    claim and them — otherwise they are being quoted in order to be
    withdrawn, or attributed to something that is not this repository.
    """
    hits = licences_in(text)
    if not hits:
        return None
    if (META_ROW.search(text) or MULTI_GRANT.search(text)
            or ABSENCE_SCOPED.search(text) or ARROW_CORRECTION.search(text)):
        return None
    first_name, first_pos = hits[0]
    # A retraction — or a third-party scope — BEFORE the first token means
    # the whole window is quoting somebody else's grant.
    pre = text[:first_pos]
    if ((RETRACTION.search(pre) or THIRD_PARTY_SCOPE.search(pre))
            and not re.match(r"^[\s|*`🔴🟢🟡🔵🆕⚠️⏱—–-]*$", pre)):
        return None
    out = {first_name}
    for name, pos in hits[1:]:
        between = text[first_pos:pos]
        if not (RETRACTION.search(between) or THIRD_PARTY_SCOPE.search(between)):
            out.add(name)
    return out


def split_row(line):
    """A markdown table row -> its cells, or None."""
    s = line.strip()
    if not s.startswith("|"):
        return None
    if is_separator(line):  # the |---|---| separator
        return None
    return [c.strip() for c in s.strip("|").split("|")]


def is_separator(line):
    return bool(re.match(r"^\|[\s:|-]+\|?$", line.strip()))


def is_table_line(line):
    return line.strip().startswith("|")


def extract_claims(body, shelf):
    """-> [dict(slug, licences, shelf, line, kind)]

    Pure.  No filesystem, no network.
    """
    claims = []
    header_cells = None
    in_correction = False
    lines = body.split("\n")
    for i, line in enumerate(lines, 1):
        # 🔴 The separator is part of the table.  The gate's first version
        # let `split_row` return None for it, fell through to the prose
        # path, and read the NEXT line — the first data row — as prose,
        # which bypassed correction-table suppression entirely.  Caught by
        # this suite's own controls before publication.
        if is_separator(line):
            continue
        cells = split_row(line)
        if cells is None and not is_table_line(line):
            header_cells = None
            in_correction = False
            # ---- prose claim: slug and licence on the same logical line.
            # These shelves hard-wrap, so a claim can straddle two lines;
            # the window is the line plus the next one — but never a table
            # row, which has its own, stricter reader.
            nxt = lines[i] if i < len(lines) else ""
            window = line + " " + ("" if is_table_line(nxt) else nxt)
            m = SLUG.search(window)
            if not m:
                continue
            # Subject discipline: a prose claim belongs to the slug it
            # FOLLOWS, within reach.  Anything further along the window is
            # the next sentence's business.  (And if a SECOND slug appears
            # before the licence, the licence is that one's, not this one's.)
            tail = window[m.end():m.end() + PROSE_REACH]
            nxt_slug = SLUG.search(tail)
            if nxt_slug:
                tail = tail[:nxt_slug.start()]
            lic = claim_from_window(tail)
            # 🔴 In prose, take the FIRST licence only.  A sibling named as
            # a bare code span rather than a link escapes the slug
            # boundary above: `intel/market.md:6670` reads
            # "`portabilis/i-educar` (GPL-2.0, …) and `i-diario` (AGPL-3.0)"
            # — one link, two repositories, two licences.  A dual grant is
            # declared in a licence CELL, not mid-sentence, so prose gives
            # up the ability to express one in exchange for not inventing
            # contradictions.
            if lic and len(lic) > 1:
                first = min(licences_in(tail), key=lambda h: h[1])[0]
                lic = {first}
            if lic:
                claims.append(dict(slug=fold(m.group(1)), licences=lic,
                                   shelf=shelf, line=i, kind="prose"))
            continue
        # ---- table row
        if header_cells is None:
            header_cells = cells
            in_correction = any(CORRECTION_HEADER.search(c) for c in cells)
            continue
        if in_correction:
            continue
        # The row's SUBJECT is the slug in its first slug-bearing cell.
        subject, subject_idx = None, None
        for idx, c in enumerate(cells):
            m = SLUG.search(c)
            if m:
                subject, subject_idx = fold(m.group(1)), idx
                break
        if subject is None:
            continue
        # 🔴 A row with TWO subjects has two licences on purpose.
        # `verticals/solutions.md:1468` is one row for `portabilis/i-educar`
        # AND `portabilis/i-diario`, licence cell `GPL-2.0 · AGPL-3.0` — the
        # GPL is the first repo's and the AGPL is the second's.  Read as one
        # subject it is a contradiction; it is a PAIR.
        if len(SLUG.findall(cells[subject_idx])) > 1:
            continue
        # Prefer a licence-named column when the header offers one; this is
        # what keeps a sibling repo in a description cell from collecting a
        # claim it never made.
        # The arrow is read over the WHOLE row, before the licence column
        # narrows the window: `intel/open-gaps.md:12449` puts the stale
        # label in its licence cell and the correction in the NEXT cell, so
        # a column-scoped read never sees the arrow that marks it.
        if ARROW_CORRECTION.search(line):
            continue
        lic_idx = [n for n, c in enumerate(header_cells)
                   if re.search(r"licen[cs]e|licencia", c, re.I)]
        if lic_idx:
            pool = " ".join(cells[n] for n in lic_idx if n < len(cells))
        else:
            # No licence column: read the subject's own cell and the one
            # after it, never the whole row.
            pool = " ".join(cells[subject_idx:subject_idx + 2])
        lic = claim_from_window(pool)
        if lic:
            claims.append(dict(slug=subject, licences=lic, shelf=shelf,
                               line=i, kind="table"))
    return claims


def disagreements(claims):
    """-> {slug: {licence: [(shelf, line, kind)]}} for slugs whose claims
    CANNOT ALL BE TRUE AT ONCE.

    🔴 The first version flagged a slug whenever two licence names appeared
    anywhere against it, and that is wrong twice over.  A single cell may
    legitimately assert a DUAL licence (`dual-licensed MIT and Apache-2.0`),
    and a row may carry one licence for code and another for content
    (`ankitects/anki`: AGPL-3.0 code, CC-BY-SA-4.0 decks).  Both read as
    "two licences" and neither is a contradiction.

    🟢 The test is the INTERSECTION over locations.  Each location asserts a
    SET; the claims agree if some licence is in every set.  `{MIT}` against
    `{MIT, Apache-2.0}` intersects at MIT — compatible.  `{MIT}` against
    `{Apache-2.0}` is empty — a contradiction, and the thing this gate is
    for.
    """
    per_slug = {}
    for c in claims:
        per_slug.setdefault(c["slug"], []).append(c)
    out = {}
    for slug, cs in per_slug.items():
        common = set.intersection(*(c["licences"] for c in cs))
        if common:
            continue
        table = {}
        for c in cs:
            for lic in c["licences"]:
                table.setdefault(lic, []).append((c["shelf"], c["line"], c["kind"]))
        out[slug] = table
    return out


def harvest(root=".", shelves=None):
    claims = []
    for shelf in (shelves or LIVE_SHELVES):
        try:
            with open(f"{root}/{shelf}", encoding="utf-8", errors="replace") as fh:
                body = fh.read()
        except FileNotFoundError:
            continue
        claims.extend(extract_claims(body, shelf))
    return claims


def report(root=".", census=False):
    live = disagreements(harvest(root, LIVE_SHELVES))
    print("scope\tslug\tlicence\tshelf\tline\tkind")
    for slug in sorted(live):
        for lic in sorted(live[slug]):
            for shelf, line, kind in live[slug][lic]:
                print(f"LIVE\t{slug}\t{lic}\t{shelf}\t{line}\t{kind}")
    dated = {}
    if census:
        dated = disagreements(harvest(root, DATED_SHELVES))
        for slug in sorted(dated):
            for lic in sorted(dated[slug]):
                for shelf, line, kind in dated[slug][lic]:
                    print(f"DATED\t{slug}\t{lic}\t{shelf}\t{line}\t{kind}")
    return live, dated


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else "."
    census = "--census" in sys.argv
    live, dated = report(root, census)
    if census:
        print(f"\n# census: {len(dated)} slug(s) disagree across the DATED shelves "
              f"(backlog, not a failure)", file=sys.stderr)
    if live:
        print(f"\n🔴 {len(live)} slug(s) carry disagreeing licence cells on the "
              f"LIVE shelves:", file=sys.stderr)
        for slug in sorted(live):
            print(f"   {slug}: " + " vs ".join(
                f"{lic} ({live[slug][lic][0][0]}:{live[slug][lic][0][1]})"
                for lic in sorted(live[slug])), file=sys.stderr)
        sys.exit(1)
    print("🟢 no slug carries disagreeing licence cells across the live shelves",
          file=sys.stderr)
