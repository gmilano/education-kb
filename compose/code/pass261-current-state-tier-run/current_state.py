"""`pass261-current-state-tier-run` — `ACTION ZD` built so that `ACTION ZE` could be run.

Two ACTIONs, one instrument, because the second cannot be measured without the first.

`ACTION ZD` (p260) — *"Build a CURRENT-STATE row harvester.  A row's state is what the
newest section says about it, not every historical mention.  Falsified if fewer than
`20 %` of a `NOASSERTION` harvest turns out to be already-answered history — in which
case the cost is not worth the index."*

`ACTION ZE` (p260, highest priority) — *"Run the ladder's EXISTING tiers over every
carried row that has no grant, and record `tier_coverage()` per `(path, row)` rather
than per path.  Stop extending the ladder until this is at `100 %`.  Falsified if fewer
than `20` further rows resolve from tiers already on the ladder."*

🔵 **Why they are one module.**  `ZE` needs a population: *every carried row that has no
grant*.  `p260` built that population by grepping all eight shelves for `NOASSERTION`
and `NONE` cells and got `142` rows of which `26` were already answered — a `72 %` noise
rate, because an append-only file's old sections are not its state.  `ZD` is the index
that makes `ZE`'s population honest, so it is measured first and its falsifier is
evaluated on `ZE`'s own harvest.

## The shape of the answer

These shelves are append-only with the NEWEST section at the top — asserted here, per
file, rather than assumed (`newest_first()`), because the whole index rests on it.  A
row's CURRENT state is therefore the FIRST cell that mentions its slug, and every later
mention is history.  Two orderings are available: file position and the pass number in
the heading.  They are computed independently and asserted to agree
(`ordering_agreement()`), because a hand-written heading is a transcription and this
base has met a mistyped one before.

## What `ZE` measures that `p260` could not

`p260`'s `tier_coverage()` answered `RUN`/`NOT-RUN`/`ABSENT` from two booleans handed to
it.  Nothing produced those booleans at scale, so the quantity it exists to measure —
how much of the ladder has actually been RUN against the rows that need it — was never
computed.  `coverage_matrix()` computes it per `(path, row)`, which is the key `ZE`
asked for, and `coverage_fraction()` is the number that has to reach `100 %` before the
ladder is extended again.
"""

import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CODE_ROOT = os.path.dirname(HERE)
REPO_ROOT = os.path.dirname(os.path.dirname(CODE_ROOT))
LADDER_SH = os.path.join(CODE_ROOT, "p229-grant-ladder-reach", "ladder.sh")
FAMILY_SH = os.path.join(CODE_ROOT, "lib", "license_family.sh")

# 🔴 p265: only these two files are APPEND-ONLY shelves — dated sections stacked
# newest-first, history preserved beneath.  p264 deliberately rewrote the other six
# as undated reference documents, which made the "carries dated sections" leg of the
# p261 control red on a DESIGN CHANGE rather than on a regression (12/166, measured
# on a clean HEAD tree before any p265 edit).  The ordering invariant still applies
# to any file that DOES carry dated sections; the requirement that it carry them
# applies only to these two.
APPEND_ONLY = ("agents/trending.md", "repos/trending.md")

SHELVES = ("agents/top.md", "agents/trending.md", "repos/foundations.md",
           "repos/trending.md", "verticals/solutions.md", "intel/market.md",
           "intel/trends.md", "compose/patterns.md")

# ── The vocabulary a CELL can carry. ──────────────────────────────────────────────
# 🔵 This is NOT a licence classifier.  `lib/license_family.sh` classifies PAYLOADS and
# is the only thing allowed to (P237).  This reads a markdown CELL, which is this
# base's own prose about a payload, and the two must not share a vocabulary: a cell can
# say "grant unreadable", which no payload ever says.
FAMILY_IN_CELL = re.compile(
    r"(?<![A-Za-z0-9-])("
    r"AGPL-3\.0(?:-only|-or-later)?|LGPL-[23](?:\.[01])?(?:-only|-or-later)?|"
    r"GPL-[23](?:\.0)?(?:-only|-or-later)?|Apache-2\.0|MIT|ISC|"
    r"BSD-[234]-Clause|MPL-2\.0|EPL-[12]\.0|ECL-2\.0|CDDL-1\.[01]|"
    r"CC0-1\.0|CC-BY(?:-SA|-NC|-ND)*-[34]\.0|Unlicense|Zlib|"
    r"Elastic-2\.0|BUSL-1\.1|SSPL-1\.0|PolyForm[A-Za-z-]*"
    r")(?![A-Za-z0-9])")

# 🔴 The absence vocabulary, which is the population `ZE` is about.  Every token here
# has been published as a CELL on these shelves by some pass.
ABSENCE_IN_CELL = re.compile(
    r"NOASSERTION|NO[-_ ]ASSERTION|NO_LICENCE_FILE|NO-LICENCE-FILE|"
    r"\bNONE\b|no grant|grant unreadable|grantless|unreadable grant|"
    r"no readable grant|licence unread|license unread|UNREAD|"
    r"ABSENCE-CONFIRMED|GRANT-ABSENT", re.I)

SLUG_RX = re.compile(r"https?://(?:www\.)?(github\.com|gitlab\.com)/"
                     r"([A-Za-z0-9][\w.-]*/[\w.-]+?)(?:[)#?]|/(?:blob|tree|releases|"
                     r"commit|issues|pull|raw)/|\.git\b|\s|$)")

# 🔴 The word `Pass` is REQUIRED, and that requirement is a measurement.
# A first version of this regex read `\bP(?:ass)?\s*(\d+)` — a bare `P` followed by
# digits — and reported SEVEN of the eight shelves `NOT-MONOTONE`, which would have
# sunk the whole index.  The shelves are fine.  The headings carry THREE different
# `P###` namespaces: pass numbers (`## Pass 260 — …`), PATTERN ids
# (`## 🆕 🟢 \`P56\` — the licence gate…`) and FINDING ids (`## 🔴 \`P126-S\` — …`).
# A loose reader mixes all three into one ordering key and mis-orders silently.
# 🔵 `p151` built `p151-identifier-spaces` and `p150-identifier-collision` for exactly
# this shape in repository identifiers; it is here too, in this base's own prose.
# With the word required, all eight shelves verify `NEWEST-FIRST`.
PASS_IN_HEADING = re.compile(r"\bPass\s+(\d{2,4})\b")


def slugs_in(text):
    """Every repository slug a line addresses, host-qualified.  A slug is `host:owner/
    repo`, because `github.com/foo/bar` and `gitlab.com/foo/bar` are different rows and
    this base carries both."""
    out = []
    for host, path in SLUG_RX.findall(text or ""):
        # 🔵 There is NO segment-count guard here, and the absence is measured rather
        # than an oversight.  The first version carried `if path.count("/") != 1:
        # continue`, mutation `M17` removed it, and all 164 controls stayed green —
        # because neither capture class in `SLUG_RX` can match a `/`, so the guard
        # could never fire.  A guard whose removal changes nothing is decoration
        # (`p258`'s lesson, on this module's own code), so it is gone and the two
        # controls that document the real mechanism — the terminator alternation —
        # stay.
        out.append(f"{host}:{path.rstrip('/.')}")
    seen, uniq = set(), []
    for s in out:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq


def cell_state(line):
    """What this cell says about the row's grant: ("FAMILY", token) | ("ABSENT", token)
    | ("SILENT", None).

    🔵 Order matters and is the one judgement in this function.  A cell reading
    *"carried as `NOASSERTION`, now `MIT`"* holds both vocabularies, and the FAMILY is
    the operative half — a pass writes the correction beside the thing corrected.  So a
    family token wins, and `ABSENT` is only returned when no family is named at all."""
    fam = FAMILY_IN_CELL.search(line or "")
    if fam:
        return "FAMILY", fam.group(1)
    ab = ABSENCE_IN_CELL.search(line or "")
    if ab:
        return "ABSENT", ab.group(0)
    return "SILENT", None


def is_table_row(line):
    s = (line or "").lstrip()
    if not s.startswith("|"):
        return False
    # a separator row carries no data
    return not re.fullmatch(r"\|[\s:|-]+\|?\s*", s)


def sections(lines):
    """[(index, pass_number_or_None, first_line, last_line)] in file order."""
    heads = [i for i, l in enumerate(lines) if l.startswith("## ")]
    out = []
    for n, i in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        m = PASS_IN_HEADING.search(lines[i])
        out.append((n, int(m.group(1)) if m else None, i, end))
    return out


def newest_first(lines):
    """🔴 The assumption the whole index rests on, asserted rather than trusted.

    Returns (verdict, first_pass, last_pass).  `NEWEST-FIRST` when the pass numbers in
    the headings are non-increasing down the file, `NOT-MONOTONE` otherwise, and
    `UNDATED` when fewer than two headings carry a pass number at all."""
    nums = [p for _, p, _, _ in sections(lines) if p is not None]
    if len(nums) < 2:
        return "UNDATED", None, None
    if all(b <= a for a, b in zip(nums, nums[1:])):
        return "NEWEST-FIRST", nums[0], nums[-1]
    return "NOT-MONOTONE", nums[0], nums[-1]


def ordering_agreement(lines):
    """🟢 The cross-check, because FILE POSITION and the HEADING's pass number are two
    independent orderings and the index uses the first.

    File position is authoritative on an append-only shelf: a pass prepends its
    section, so position cannot lie.  A pass number is a hand-typed transcription.
    Returns (verdict, headings, headings_carrying_a_pass_number).  `AGREE` means the
    parsed numbers are non-increasing in file order, so neither ordering contradicts
    the other."""
    secs = sections(lines)
    nums = [p for _, p, _, _ in secs if p is not None]
    if len(nums) < 2:
        return "UNDECIDABLE", len(secs), len(nums)
    agree = all(b <= a for a, b in zip(nums, nums[1:]))
    return ("AGREE" if agree else "DISAGREE"), len(secs), len(nums)


def harvest(lines):
    """slug -> every mention, in file order.  Each mention is a dict with the section
    index, the heading's pass number, the line number, the state and the token."""
    out = {}
    for idx, pnum, start, end in sections(lines):
        for ln in range(start, end):
            line = lines[ln]
            if not is_table_row(line):
                continue
            state, token = cell_state(line)
            for slug in slugs_in(line):
                out.setdefault(slug, []).append(
                    {"section": idx, "pass": pnum, "line": ln + 1,
                     "state": state, "token": token})
    return out


def current_state(mentions):
    """🟢 `ACTION ZD`'s predicate.  The state of a row is its NEWEST *informative*
    mention — the first `FAMILY` or `ABSENT` cell in file order.

    🔵 `SILENT` mentions are skipped rather than treated as state: a row named in a
    pattern recipe or a market table says nothing about its grant, and `p260`'s harvest
    could not tell that from a row whose grant had been retracted."""
    for m in mentions:
        if m["state"] in ("FAMILY", "ABSENT"):
            return m
    return {"section": None, "pass": None, "line": None,
            "state": "NEVER-GRADED", "token": None}


def already_answered(mentions):
    """🔴 `ZD`'s falsifier, per row.  True when an `ABSENT` cell exists BELOW a newer
    `FAMILY` cell — i.e. the row is answered and a whole-file harvest would collect it
    anyway.  This is the `72 %` noise `p260` measured, made a predicate."""
    cur = current_state(mentions)
    if cur["state"] != "FAMILY":
        return False
    return any(m["state"] == "ABSENT" and m["section"] > cur["section"]
               for m in mentions)


def naive_population(mentions):
    """`p260`'s method, kept executable so the two can be compared on one harvest: any
    row with an `ABSENT` cell ANYWHERE in the file."""
    return any(m["state"] == "ABSENT" for m in mentions)


def current_population(mentions):
    """`ZD`'s method: the row's CURRENT cell says there is no grant."""
    return current_state(mentions)["state"] == "ABSENT"


def noise_rate(harvested):
    """(naive_rows, current_rows, already_answered_rows, fraction).  `ZD` is falsified
    when the fraction is below `0.20`."""
    naive = [s for s, m in harvested.items() if naive_population(m)]
    cur = [s for s, m in harvested.items() if current_population(m)]
    ans = [s for s in naive if already_answered(harvested[s])]
    frac = (len(ans) / len(naive)) if naive else 0.0
    return len(naive), len(cur), len(ans), frac


# ── `ACTION ZE`: the ladder, read from the ladder rather than copied. ─────────────

def ladder_tiers(path=None):
    """{tier: [paths]} parsed from `p229-grant-ladder-reach/ladder.sh` itself.

    🔴 `p229`'s own header says *"a probe list copied is a probe list forked"*, and
    `ZE` is about running the ladder that EXISTS — so this module must not hold its own
    copy.  The tiers are read out of the shell assignments at call time."""
    with open(path or LADDER_SH, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    tiers = {}
    for tier in ("TIER_A", "TIER_B", "TIER_C"):
        m = re.search(rf'^{tier}="([^"]*)"', text, re.M | re.S)
        if m:
            tiers[tier] = m.group(1).split()
    return tiers


def coverage_matrix(tiers, tree, fetched):
    """🟢 `ACTION ZE`'s key: `tier_coverage()` per `(path, row)`, not per path.

    `tiers`   {tier: [paths]} — the ladder's REACH
    `tree`    the paths this repository actually has (from its own tree)
    `fetched` the paths that were fetched FOR THIS ROW on this run

    Returns {(tier, path): verdict}.  `p260`'s three verdicts, with the one distinction
    that makes the matrix useful: a path the repository does not contain is
    `NOT-IN-TREE` and is not a hole in the ladder, while a path the tree HAS and the
    run did not fetch is `NOT-RUN` — the verdict `ZE` exists to drive to zero."""
    tree = set(tree or ())
    fetched = set(fetched or ())
    out = {}
    for tier, paths in (tiers or {}).items():
        for p in paths:
            if p in fetched:
                out[(tier, p)] = "RUN"
            elif p in tree:
                out[(tier, p)] = "NOT-RUN"
            else:
                out[(tier, p)] = "NOT-IN-TREE"
    return out


def coverage_fraction(matrix):
    """🔴 The number `ZE` says must reach `1.0` before the ladder is extended again:
    of the ladder paths a repository ACTUALLY HAS, how many were run for that row.
    `NOT-IN-TREE` is excluded — it is not a hole, and counting it would let a long
    ladder of absent names dilute the measurement to meaninglessness."""
    live = [v for v in matrix.values() if v in ("RUN", "NOT-RUN")]
    if not live:
        return None, 0, 0
    run = sum(1 for v in live if v == "RUN")
    return run / len(live), run, len(live)


def family_of(payload, family_sh=None):
    """The SHARED classifier (P237), called rather than reimplemented.  Returns its
    verdict on stdout, or `CLASSIFIER-UNAVAILABLE` if it cannot be run — which is a
    measurement, not a crash."""
    sh = family_sh or FAMILY_SH
    try:
        r = subprocess.run(["bash", "-c", f'. "{sh}"; family_of "$1"', "_", payload],
                           capture_output=True, text=True, timeout=60)
    except Exception:
        return "CLASSIFIER-UNAVAILABLE"
    if r.returncode != 0:
        # 🔵 A classifier that could not be SOURCED is a different measurement from one
        # that ran and said nothing, and only the second is about the payload.
        return "CLASSIFIER-UNAVAILABLE"
    return (r.stdout or "").strip() or "CLASSIFIER-SILENT"


def resolution_cause(before, after, path_was_on_ladder, path_was_in_tree):
    """Why a row that had no grant now has one — `p259`'s cause classification, keyed
    on the pair `ZE` asked for.

    🔴 `CHANNEL-ABSENT` is the only cause a LONGER ladder fixes, and `p259` measured it
    at `3` of `11` while `p260` measured it at `0` of `36`.  Keeping the causes apart is
    the whole reason this base stopped adding paths."""
    if before == after:
        return "NO-CHANGE"
    if not path_was_on_ladder:
        return "CHANNEL-ABSENT"
    if path_was_in_tree:
        return "TIER-NOT-RUN"
    return "ABSENCE-UNCONFIRMED"


# ── The index itself, across all eight shelves. ───────────────────────────────────

def harvest_shelves(repo_root=None, shelves=None):
    """slug -> [mentions], merged across the eight shelves and ordered NEWEST FIRST.

    🔵 The cross-file order key is `(pass DESC, section ASC)`.  Within one file,
    position alone is sound and is used.  Across files, only the pass number relates
    two sections, so a section whose heading carries no pass number sorts LAST — it is
    a standing rule or a page preamble, not a window, and this base writes grant cells
    in windows.  Declared rather than hidden: a grant cell in an undated section is
    read as the oldest evidence there is.
    """
    root = repo_root or REPO_ROOT
    out = {}
    orderings = {}
    for rel in (shelves or SHELVES):
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            orderings[rel] = ("MISSING", 0, 0)
            continue
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.read().splitlines()
        orderings[rel] = ordering_agreement(lines)
        for slug, mentions in harvest(lines).items():
            for m in mentions:
                m = dict(m)
                m["file"] = rel
                out.setdefault(slug, []).append(m)
    for slug in out:
        out[slug].sort(key=lambda m: (-(m["pass"] or 0), m["section"]))
    return out, orderings


# ── 🔴 "NOT SPDX" is not the same as "prose". ─────────────────────────────────────
# `p260`'s `token_verdict()` answers `NOT-SPDX-PROSE` for any manifest token that is
# not an SPDX identifier and is long enough or has enough words.  Measured over this
# pass's 11 Tier C declarations, THREE of them — 27 % — are values their own ecosystem
# SPECIFIES, and all three were reported unreadable:
#
#   npm      `"license": "SEE LICENSE IN LICENSE"`   nakafaai/nakafa.com
#            npm's package.json spec defines exactly this form, plus `UNLICENSED`.
#            It is a POINTER, which `p254` already ruled is not a grant — but it is a
#            specified pointer, and "unreadable" is the wrong thing to say about it.
#   PyPI     `"OSI Approved :: Apache Software License"`   mbzuai-oryx/ClimateGPT
#            A trove classifier from a CONTROLLED LIST.  `Apache Software License`
#            maps to `Apache-2.0` for every package PyPI has ever accepted.
#   CRAN     `License: MIT + file LICENSE`   sonsoleslp/tna
#            CRAN's own licence grammar.  `MIT + file LICENSE` means MIT, and the
#            `LICENSE` file it names is a two-line PARAMETER SHEET, not a licence.
#
# 🔵 `p259`'s lesson was that one PATH can carry two KINDS of evidence.  This is the
# same lesson one level in: one FIELD can carry two GRAMMARS, and SPDX is only one of
# them.  The remedy is not a longer ladder — again — it is a reader per grammar.

TROVE_CLASSIFIER = {
    "apache software license": ("Apache-2.0", None),
    "mit license": ("MIT", None),
    "mit no attribution license (mit-0)": ("MIT-0", None),
    "bsd license": ("BSD", None),
    "isc license (iscl)": ("ISC", None),
    "gnu general public license v3 (gplv3)": ("GPL-3.0", "only"),
    "gnu general public license v3 or later (gplv3+)": ("GPL-3.0", "or-later"),
    "gnu general public license v2 (gplv2)": ("GPL-2.0", "only"),
    "gnu general public license v2 or later (gplv2+)": ("GPL-2.0", "or-later"),
    "gnu lesser general public license v3 (lgplv3)": ("LGPL-3.0", "only"),
    "gnu lesser general public license v2 or later (lgplv2+)": ("LGPL-2.1", "or-later"),
    "gnu affero general public license v3": ("AGPL-3.0", None),
    "gnu affero general public license v3 or later (agpl v3+)": ("AGPL-3.0", "or-later"),
    "mozilla public license 2.0 (mpl 2.0)": ("MPL-2.0", None),
    "eclipse public license 2.0 (epl-2.0)": ("EPL-2.0", None),
    "the unlicense (unlicense)": ("Unlicense", None),
    "cc0 1.0 universal (cc0 1.0) public domain dedication": ("CC0-1.0", None),
    "other/proprietary license": (None, None),
}

# npm's package.json specification.  Two reserved values, both documented.
NPM_RESERVED = ("unlicensed",)
NPM_POINTER = re.compile(r"^SEE LICEN[CS]E IN\s+(.+?)\s*$", re.I)

# CRAN's `License:` grammar.  `+ file LICENSE` attaches a parameter sheet; `|` offers a
# choice; `(>= n)` is a bound.
CRAN_FILE = re.compile(r"^(.*?)\s*\+\s*file\s+LICEN[CS]E\s*$", re.I)
CRAN_BOUND = re.compile(r"^([A-Za-z][\w.-]*?)\s*\(\s*(>=|>|==)\s*([\d.]+)\s*\)$")


def controlled_vocabulary(ecosystem, token):
    """🟢 (family, bound, read_by) for a manifest token that is NOT SPDX but IS a value
    its ecosystem specifies.  `(None, None, reason)` when the token is genuinely
    unspecified prose.

    This is deliberately narrow: it recognises only documented vocabularies, and a
    token outside them still answers `None`.  A reader that guesses is worse than one
    that declines, because the next pass cannot tell a guess from a read."""
    t = (token or "").strip()
    if not t:
        return None, None, "EMPTY"
    low = t.lower()

    if ecosystem in ("NPM", "COMPOSER"):
        if low in NPM_RESERVED:
            return "UNLICENSED-NPM-RESERVED", None, "npm-spec:reserved-word"
        m = NPM_POINTER.match(t)
        if m:
            # 🔴 A specified POINTER, not a grant (`p254`).  The family comes from the
            # file it names, and this function says WHICH file to read next.
            return "FILE-POINTER:" + m.group(1), None, "npm-spec:SEE LICENSE IN"

    if ecosystem in ("PYPROJECT", "SETUPPY", "SETUPCFG"):
        cl = low
        if cl.startswith("license ::"):
            cl = cl.split("::", 1)[1].strip()
        cl = re.sub(r"^license\s*::\s*", "", cl).strip()
        for key, (fam, bound) in TROVE_CLASSIFIER.items():
            if cl == key or cl.endswith(key):
                if fam is None:
                    return "NAMED-PROPRIETARY", None, "trove:Other/Proprietary"
                return fam, bound, "trove-classifier"

    if ecosystem == "R-CRAN":
        m = CRAN_FILE.match(t)
        if m:
            # 🔴 The file CRAN names here is a two-line parameter sheet
            # (`YEAR:` / `COPYRIGHT HOLDER:`), measured first-hand on
            # `sonsoleslp/tna`.  Grading it as a licence payload answers UNCLASSIFIED
            # on the strongest tier while the weakest tier holds the family.
            inner = m.group(1).strip()
            fam, bound, _ = controlled_vocabulary("R-CRAN", inner)
            return (fam or inner), bound, "cran:<licence> + file LICENSE"
        m = CRAN_BOUND.match(t)
        if m:
            return m.group(1), ("or-later" if m.group(2) in (">=", ">") else "only"), \
                "cran:bound"
        if "|" in t:
            return "CHOICE:" + "|".join(x.strip() for x in t.split("|")), None, \
                "cran:choice-of-licences"
    return None, None, "NOT-A-SPECIFIED-VALUE"


def cran_parameter_sheet(body):
    """True when a payload is CRAN's `LICENSE` parameter sheet rather than a licence.

    🔴 Measured: `sonsoleslp/tna`'s root `LICENSE` is 46 bytes — `YEAR: 2025-2026` /
    `COPYRIGHT HOLDER: tna authors`.  It is Tier A, position 2, the strongest rung on
    the ladder, and it carries NO grant at all."""
    b = (body or "").strip()
    if len(b) > 400:
        return False
    keys = len(re.findall(r"^\s*(YEAR|COPYRIGHT HOLDER|ORGANIZATION)\s*:", b, re.M | re.I))
    return keys >= 1 and not re.search(r"permission|redistribution|warranty|liable", b, re.I)


# ── 🔴 A payload is not one grant. ────────────────────────────────────────────────
# `p260` wrote `reservation_verdict()` to stop a FALSE RETRACTION, and one pass later
# it produced one.  `Kosudo/nextSIS`'s `license.txt` is `39 890` B and its own table of
# contents says what it is:
#
#     1. Overview
#     2. nextSIS GNU General Public License Version 3
#     3. CodeIgniter License
#     4. Twitter Bootstrap License
#
# The `All rights reserved.` is on line `703`, inside EllisLab's CodeIgniter section —
# a THIRD PARTY's bundled grant — and CodeIgniter's bespoke text contains neither of
# the two permissive phrases `reservation_verdict()` looks for, so it answered
# `RESERVED` for a repository whose own licence is plainly `GPL-3.0`.
#
# 🔵 `p229`'s TIER_A header already knew that *"an aggregate carries OTHER projects'
# grants, and TIER_A governs THIS repository's verdict"*.  The knowledge existed; the
# new guard did not consume it — `p251`'s *unwired knowledge*, for the second time in
# three passes, and this time inside a guard written to be the wiring.

SECTION_RULE = re.compile(r"^\s*-{20,}\s*$")
LICENCE_NAME_IN_HEADING = re.compile(
    r"\b(licen[cs]e|public licen[cs]e|terms)\b", re.I)
# 🔴 A table of contents carries the word "LICENSE" and no grant, and `nextSIS` opens
# with one — `LICENSE CONTENTS`, between two rule lines, indistinguishable from a
# section heading to anything that only asks whether the word appears.  The first
# version of `subject_span()` took it as the subject's section and returned the right
# verdict for the WRONG SPAN, which is the failure `p260` named one pass ago: an
# accidentally-correct answer from an unsound method.  Excluded by name.
NON_GRANT_HEADING = re.compile(
    r"^\s*(\d+\.\s*)?(licen[cs]e\s+)?(contents|table of contents|overview|"
    r"summary|index|preamble)\s*$", re.I)


def aggregate_sections(body):
    """[(start_line, heading)] for a payload that bundles several grants.

    A section is a heading between two rule lines — the convention `nextSIS`,
    `openSIS` and several Moodle plugins use.  Returns `[]` for a single-grant payload,
    so a caller can tell the two apart before believing one verdict for the file."""
    lines = (body or "").splitlines()
    out = []
    for i in range(1, len(lines) - 1):
        if SECTION_RULE.match(lines[i - 1]) and SECTION_RULE.match(lines[i + 1]) \
                and lines[i].strip():
            out.append((i, lines[i].strip()))
    named = _grant_headings(out)
    return out if len(named) >= 2 else []


def _grant_headings(sections):
    """The headings that introduce a GRANT, with contents/overview blocks removed."""
    return [s for s in sections
            if LICENCE_NAME_IN_HEADING.search(s[1])
            and not NON_GRANT_HEADING.match(s[1])]


def subject_span(body):
    """(start, end) line numbers of the span that belongs to THIS repository.

    The subject's grant is the FIRST licence section; everything from the second
    licence-named heading onward is somebody else's.  For a single-grant payload the
    span is the whole file, which is what every caller before this pass assumed."""
    lines = (body or "").splitlines()
    secs = aggregate_sections(body)
    if not secs:
        return 0, len(lines)
    named = _grant_headings(secs)
    if not named:
        return 0, len(lines)
    first = named[0][0]
    rest = [s[0] for s in named[1:]]
    return first, (rest[0] if rest else len(lines))


def reservation_verdict_scoped(body):
    """🟢 `p260`'s guard, keyed on `(payload, SECTION)` instead of on the payload.

    Returns `BOILERPLATE`, `RESERVED`, `NO-RESERVATION`, or
    `THIRD-PARTY-RESERVATION` — the verdict that did not exist before this pass and
    that `nextSIS` needs: the phrase is in the payload, it is real, and it is not this
    repository's."""
    lines = (body or "").splitlines()
    hits = [i for i, l in enumerate(lines) if re.search(r"all rights reserved", l, re.I)]
    if not hits:
        return "NO-RESERVATION"
    start, end = subject_span(body)
    inside = [i for i in hits if start <= i < end]
    if not inside:
        return "THIRD-PARTY-RESERVATION"
    span = "\n".join(lines[start:end])
    permissive = (re.search(r"[Rr]edistribution and use in source and binary forms", span)
                  or re.search(r"Permission is hereby granted, free of charge", span))
    return "BOILERPLATE" if permissive else "RESERVED"
