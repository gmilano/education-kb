#!/usr/bin/env python3
"""p541 — Gap 540-B, built as predicates rather than as a patch.

540-B asked: *"the grant classifier is English-keyed, and that is a LATAM
bias.  Add Portuguese and Spanish title strings for the GPL/AGPL/MIT/Apache
families, re-run over the 600 gated addresses, and report how many verdicts
move."*

🔴 WHAT p541 GOT WRONG FIRST, RECORDED BECAUSE IT IS THE POINT.

This pass fetched all 37 `UNKNOWN` payloads from
`evidence/backlog-gated-slice2.2026-10-30-p540.tsv`, ran both classifiers this
base owns, found that 19 of 37 are named by them, and drafted that as its
headline: *"19 of the 37 UNKNOWN verdicts are a recording artefact."*

**That headline was a restated presence.**  `p540` had already read all 37 by
hand and published them as **twelve dialects** on
[`../../../agents/trending.md`](../../../agents/trending.md), with the
non-buildable count, the Portuguese AGPL, the `open-webui` clause-4 variant,
the R `template-stub` class and `INGInious`'s two-space indent all named.  The
decomposition below reproduces p540's table almost cell for cell.  🔵 The
`UNKNOWN` string survives only in the TSV column, which p540 did not rewrite
after resolving the rows in prose.

🔵 **And the generalisable half, which is worth more than the gate this pass
also shipped:** `p541` built `gate-restated-presence` for `Gap 540-A` and then
nearly published a restated presence as its own headline.  The gate did not
catch it, and could not: **it grades ADDRESSES, and this was a restated
ANALYSIS.**  Every address here was already known to be in the tree.  The
cheaper and more dangerous restatement is of a CONCLUSION, and nothing on this
base grades those.  → `Gap 541-A`.

WHAT IS ACTUALLY NEW HERE, stated narrowly so a successor can audit it:

  1. p540's twelve dialects are a MEASUREMENT, read by hand, in prose.  These
     are four PREDICATES with 19 controls, so the next instance is caught
     rather than re-read.  p540 resolved the residue; this grades it.
  2. 🔴 **540-B's own remedy is unsafe as written, and no page says so.**  Six
     of the 37 reproduce a stock body under a NON-STOCK TITLE -- `SATA`
     (MIT + a star obligation), `PySilicon Research`, `O'Saasy`,
     `snflwr.ai` (titled "Proprietary"), `open-webui` (BSD-3 + clause 4), and
     `INGInious` (scoped: "Most of the files").  Adding title strings widens
     recall, and widening recall over these six converts SIX CORRECT REFUSALS
     INTO FALSE PERMISSIVE GRANTS -- the one error class a studio builds on.
     So `bespoke_guard` runs BEFORE recall, and a control fails if that order
     is ever inverted.
  3. 🔴 **540-B's premise is half-wrong.**  It says
     `portabilis/pre-matricula-digital` is graded UNKNOWN *"solely because its
     text is Portuguese"*.  `p228/classify_grant.py` does miss it, but
     `ingest/backlog-gate.py:spdx_of` ALREADY carries `'LICENÇA PÚBLICA GERAL'`
     and returns `AGPL-3.0`.  **The base already had the Portuguese
     capability, in one of its two classifiers.**  The defect is two
     classifiers that do not share a title table -- and a Spanish/Portuguese
     patch applied to one would have left that divergence in place while
     appearing to fix it.  → `Gap 541-C`.
  4. The `template-stub` class has a cheaper fix than p540 recorded.  p540
     put the SPDX id in R's `DESCRIPTION`; p541 confirmed first-hand that all
     three of `rstudio/ggcheck`, `rstudio/tblcheck` and `shmercer/writeAlizer`
     serve `# MIT License` at **`LICENSE.md`**, one rung further along a ladder
     the gate already walks.
  5. Language explains **1 of 37**, not the bucket.  The dominant causes are
     bespoke titling (13) and licensing BY REFERENCE (7).

THE DECOMPOSITION, over the 37, by cause:

  14  a stock family both classifiers name correctly
   7  licence BY REFERENCE, not reproduced (EUPL-1.1 ×6, 1.2 ×1)
   6  a stock BODY under a non-stock TITLE ... UNKNOWN was the SAFER answer
   7  genuinely bespoke / source-available / non-OSI ... correctly withheld
   3  the ladder stopped at a template fill-in

Evidence: `../../../evidence/grant-residue-decomposed.2026-10-30-p541.tsv`.

The four predicates:

  by_reference()    a short notice that NAMES an authority it does not
                    reproduce.  p289 graded restatement-vs-authority on the
                    curriculum layer; this is the same shape in a LICENSE.
  stub_payload()    a payload that is a template's FILL-IN, not a grant.
  bespoke_guard()   a stock body under a non-stock title is NOT that family.
  residue_cause()   the five-way decomposition above, as a verdict.
"""

import re

# ── by_reference ─────────────────────────────────────────────────────────────
# The Finnish National Agency for Education publishes seven repositories whose
# LICENSE is a ~650 B English notice: "Licensed under the EUPL, Version 1.1 or
# - as soon as they will be approved by the European Commission - subsequent
# versions of the EUPL".  The grant is real and the text of it is elsewhere.
# p540 called this "opetushallitus/koski's EUPL grant ... already in this
# tree" -- the FAMILY was known, the VERSION is 1.1, and the only EUPL title
# either classifier carries is 1.2.
REFERENCE_CUES = (
    r"licensed\s+under\s+the\s+(?P<fam1>[A-Z][A-Za-z0-9 .-]{1,40}?)[,\s]+version\s+(?P<ver1>[\d.]+)",
    r"you\s+may\s+obtain\s+a\s+copy\s+of\s+the\s+licen[cs]e\s+at",
    r"the\s+(?:full|complete)\s+(?:legal\s+)?text\s+(?:is|can\s+be\s+found)",
    r"texto\s+legal\s+completo",
    r"see\s+the\s+(?P<fam2>[A-Z][A-Za-z0-9 ]{3,40}?\s+Licen[cs]e)\s+for\s+more\s+details",
)
_REF = [re.compile(p, re.I) for p in REFERENCE_CUES]

# A reproduced grant is long.  EUPL-1.2 is ~14 kB, GPL-3.0 ~35 kB, MIT ~1 kB.
# A NOTICE that points at one is short and contains a URL to it.
REFERENCE_MAX_BYTES = 2500
URL = re.compile(r"https?://\S+")


def by_reference(text):
    """(True, named_authority) when the payload POINTS at a grant instead of
    reproducing it.  Such a payload is a real grant and an unreadable one: the
    family is citable, the version must be read off the notice, and the terms
    are not in the repository."""
    if len(text.encode("utf-8")) > REFERENCE_MAX_BYTES:
        return False, None
    hits = [r for r in _REF if r.search(text)]
    if not hits:
        return False, None
    if not URL.search(text):
        return False, None
    # Name it from the strongest cue that captured something.
    for r in _REF:
        m = r.search(text)
        if m and m.groupdict():
            fam = m.groupdict().get("fam1") or m.groupdict().get("fam2")
            if fam:
                ver = m.groupdict().get("ver1")
                return True, (f"{fam.strip()} {ver}".strip() if ver else fam.strip())
    return True, None


# ── stub_payload ─────────────────────────────────────────────────────────────
# `usethis::use_mit_license()` writes TWO files: a 45 B LICENSE carrying only
# the year and holder, and a LICENSE.md carrying the MIT text.  A ladder that
# probes LICENSE and stops reads the fill-in and calls it unrecognisable.
# This is p275's lesson -- "the LADDER, not the slug, is the defect" -- in a
# shape the ladder's authors had not seen: the file EXISTS and is not a grant.
STUB_PATTERNS = (
    re.compile(r"^\s*YEAR:\s*\S+\s*COPYRIGHT\s+HOLDER:\s*\S", re.I | re.S),
    re.compile(r"^\s*\{\{\s*year\s*\}\}", re.I),
    re.compile(r"^\s*(\[year\]|<year>|YYYY)\b", re.I),
)
STUB_MAX_BYTES = 400


def stub_payload(text):
    """True when the payload is a template's FILL-IN rather than a grant.

    Deliberately narrow: a short file matching a known generator's stub shape.
    A 45 B file is not evidence on its own -- `opetushallitus/ataru` is 296 B
    and a real notice -- so the pattern must match too."""
    if len(text.encode("utf-8")) > STUB_MAX_BYTES:
        return False
    return any(p.search(text) for p in STUB_PATTERNS)


# ── bespoke_guard ────────────────────────────────────────────────────────────
# p341's `gate-bespoke-title` established that a bespoke instrument is not a
# stock text.  This is its missing converse: a BESPOKE TITLE over a STOCK BODY.
# The body matches, so every recall-widening change names the family and is
# wrong.  Five of the 37 are this shape, and all five would become false
# permissive grants under 540-B's patch as written.
STOCK_TITLES = (
    r"MIT\s+Licen[cs]e", r"Apache\s+License", r"BSD(\s+\d-Clause)?\s+Licen[cs]e",
    r"New\s+BSD\s+License", r"GNU\s+(AFFERO\s+|LESSER\s+)?GENERAL\s+PUBLIC\s+LICENSE",
    r"ISC\s+Licen[cs]e", r"Mozilla\s+Public\s+License", r"Eclipse\s+Public\s+License",
    r"Educational\s+Community\s+License", r"EUROPEAN\s+UNION\s+PUBLIC\s+LICENCE",
    r"Creative\s+Commons", r"CC0\s+1\.0", r"The\s+Unlicense",
    r"LICEN[ÇC]A\s+P[ÚU]BLICA\s+GERAL", r"LICENCIA\s+P[ÚU]BLICA\s+GENERAL",
)
_STOCK = [re.compile(p, re.I) for p in STOCK_TITLES]

# 🔴 THE FALSE POSITIVE THIS PREDICATE HAD FIRST, AND THE FIX.
#
# The draft matched a keyword list -- "Community", "Source Available",
# "Research", "Proprietary", "License Agreement" -- anywhere in the payload.
# Run over the 37 it graded SIX ECL-2.0 payloads as bespoke, because
# `Educational Community License` contains "Community License"; and it caught
# `open-webui` on the string "CONTRIBUTOR_LICENSE_AGREEMENT" in a sentence
# rather than on its actual title.  Both are the same mistake: a licence is
# named by its TITLE BLOCK, and a keyword anywhere is not a title.
#
# So the predicate reads the first non-empty line, strips Markdown heading
# marks, and asks one question: does this line name a licence, and is that
# name in the stock table?  Generic, so it needs no keyword list and catches
# `Open WebUI License` -- which no keyword list would have -- while ECL-2.0,
# `New BSD License` and `LICENÇA PÚBLICA GERAL AFFERO GNU` all read as stock.
#
# 🔵 "Bespoke" here means OUTSIDE THE STOCK TABLE, not necessarily
# hand-written: `Elastic License 2.0` and the `ODC Open Database License` are
# real published licences that this base does not carry a template for.  The
# verdict a studio needs from both is the same -- not a permissive software
# grant on file -- so they share a class.
NAMES_A_LICENCE = re.compile(
    r"licen[cs]e|licen[çc]a|licencia|conditions\s+of\s+use", re.I)
HEADING_MARKS = re.compile(r"^[#*\s>|-]+")


def first_offset(text, patterns):
    """Earliest match offset among `patterns`, or None.  Used to ask whether a
    STOCK BODY is present at all, which separates a bespoke licence that
    reproduces one from a bespoke licence that does not."""
    best = None
    for r in patterns:
        m = r.search(text)
        if m and (best is None or m.start() < best):
            best = m.start()
    return best


def title_block(text):
    """The first non-empty line, without Markdown furniture.

    p378's `gate-presentation-fold` established that one licence TEXT may be
    re-wrapped without becoming another licence; this is the same idea at the
    title's width."""
    for raw in text.splitlines():
        line = HEADING_MARKS.sub("", raw).strip()
        if line:
            return line
    return ""


def bespoke_guard(text):
    """(is_bespoke, title) — True when the TITLE BLOCK names a licence that is
    not in the stock table.

    Positional, like p227's surviving channel, and for the same reason: a
    bespoke licence that reproduces the MIT body puts its own name first and
    the stock text after.  Reading the stock match alone inverts the answer --
    which is exactly what both committed classifiers do on five of the 37."""
    line = title_block(text)
    if not line or not NAMES_A_LICENCE.search(line):
        return False, None
    for r in _STOCK:
        if r.search(line):
            return False, None
    return True, " ".join(line.split())[:80]


# ── residue_cause ────────────────────────────────────────────────────────────
CAUSES = (
    "BESPOKE-OVER-STOCK",   # a stock body under a bespoke title: do NOT name
    "BESPOKE",              # genuinely bespoke / source-available / non-OSI
    "BY-REFERENCE",         # a real grant, named but not reproduced
    "LADDER-STUB",          # the probed file is a template fill-in
    "NAMED",                # a stock family: the UNKNOWN was a recording artefact
)


def residue_cause(text, named_family=None):
    """Decompose one UNKNOWN payload.  Order matters, and it is the order of
    COST: the guard runs before recall, because a false permissive grant is the
    error a studio builds on."""
    is_bespoke, title = bespoke_guard(text)
    if is_bespoke:
        stock_at = first_offset(text, _STOCK)
        body_stock = stock_at is not None or named_family is not None
        return ("BESPOKE-OVER-STOCK" if body_stock else "BESPOKE"), title
    if stub_payload(text):
        return "LADDER-STUB", None
    ref, authority = by_reference(text)
    if ref:
        return "BY-REFERENCE", authority
    if named_family:
        return "NAMED", named_family
    return "BESPOKE", None
