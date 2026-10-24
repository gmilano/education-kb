#!/usr/bin/env python3
"""p348 -- `ACTION ZZ-x`: fold the slug before comparing it, and over the RIGHT denominator.

`ACTION ZZ-x` was registered by `p347` as *"case-folded slug comparison plus an alias
table in `gate-identity`, then wire `gate-identity-online` into a target a pass with
egress is expected to run."*  Both halves are discharged here, and running them turned
up a defect in the measurement that motivated them.

## The denominator, which was the real finding

`p347` ran the HEAD-equality test *"over EVERY address on these shelves"* and declared
257 distinct addresses extracted from **the five live shelf files**.  Re-harvested here
over **all nine** published shelves, this base carries **2 531 distinct addresses**, of
which **2 091 appear only on `agents/trending.md` and `repos/trending.md`** -- the two
APPEND-ONLY shelves, which together hold 74 076 of 122 217 shelf lines.  So the
shelf-wide run covered **440 of 2 531 addresses, 17.4 %**, and its own verdict column
reads *"unique HEAD across the shelf set"*: a true statement about the set it measured
and a false one about the shelves.

The specimen is the pair that proves it.  `openwallet-foundation-labs/learner-credential-wallet`
was in `p347`'s set and graded unique.  `digitalcredentials/learner-credential-wallet`
is on `agents/trending.md`, outside it.  Both resolve to HEAD `1c46a82ba384`: ONE
repository, published twice, under owners that share no characters -- the MIT Digital
Credentials Consortium having moved the project to the OpenWallet Foundation.

## Three identity classes, and this base had one instrument in `hooks`

| Class | Example | Caught by folding? | Caught by HEAD equality? |
|---|---|---|---|
| same address, different CASE | `CAHLR/OATutor` / `cahlr/OATutor` | 🟢 yes | 🟢 yes |
| different OWNER, one repository (a transfer or rename) | `digitalcredentials/…` / `openwallet-foundation-labs/…` | 🔴 **no** | 🟢 yes |
| different repository, IDENTICAL payload | `anthropics/k12-teacher-skills` / `learning-commons-org/agent-skills` (`SKILL.md` sha256 `152e3272fbd108fe`) | 🔴 no | 🔴 **no** |

## Why folding is safe to wire as a gate: it was measured, not assumed

All 65 folded-collision groups on the complete shelf set (the `OWNER/REPO` command
template dropped) were resolved first-hand with `git ls-remote --symref`.  **64 resolved
and all 64 are SAME-HEAD** -- one repository under two or three casings.  **Zero groups
came back with different HEADs**, so folding produced no false positive anywhere on this
corpus.  One group (`gegok12/gegok12`) does not answer under either casing.

## The contract this gate enforces, and why it is forward-looking

An append-only shelf cannot be repaired backwards -- `p347` established that the only
move which ever clears an inherited finding is to satisfy the contract BY CONSTRUCTION
in the successor's own text.  A gate that failed on all 65 historical collisions would
therefore be permanently red and would teach nothing.  So this gate judges the LIVE PASS
SECTION, exactly as `gate-absence` does:

    P348-NEW-CASING   the current pass section publishes an address whose fold already
                      exists on these shelves under a DIFFERENT casing.

Writing `cahlr/OATutor` in a new section when the shelves say `CAHLR/OATutor` is the
failure.  Citing the casing already published is not.  The 65 inherited groups are a
CENSUS -- a backlog with a denominator, never a failure -- which is the `p308`
`shelf-census` / `gate-shelf-consistency` split applied to the identity axis.

## p423 -- PRECEDENCE IS NOT AUTHORITY, and this gate had only precedence

The contract above reads *"writing `cahlr/OATutor` in a new section when the shelves say
`CAHLR/OATutor` is the failure.  Citing the casing already published is not."*  That is
right exactly when the first publication was right, and `p423` measured a case where it
was not.  `p370` published `mattlo0546/canvas-mcp` in lower case.  GitHub's own canonical
display form is `Mattlo0546` -- page title and breadcrumb, the lower-case form appearing
only inside URLs, which are case-insensitive.  So `p422` wrote the CORRECT casing, this
gate reddened against the correct row, and the stale one sat in history serving as the
oracle.  A precedence-only gate does not merely miss that: it DEMANDS every later pass
reproduce the error, and reddens the pass that repairs it.

So this gate now adjudicates by AUTHORITY where authority is known:

    P348-NON-CANONICAL-CASING   a LIVE address deviates from a REGISTERED canonical
                                casing.  Fatal -- strictly stronger than the precedence
                                arm, because the canonical is a first-hand read and not
                                a guess at which published row came first.
    P423-HISTORICAL-NON-CANONICAL   a HISTORICAL address deviates from a registered
                                canonical.  A CENSUS row with a denominator, never a
                                failure: an append-only shelf cannot be repaired
                                backwards (`p347`), which is the same disposition the
                                65 inherited folds already have.

🔴 AND THE CHANNEL ORDER WAS ALREADY IN THIS REPOSITORY.  `p439-case-collision-gate` wrote
it down -- registry homepage, then the repository's own self-link, then a recorded
majority decision -- and has been in NO `make` target since `p439`.  `p423` built this arm
without knowing that, and found it only afterwards while discharging `ACTION p421-A`.  So
`Gap 421-A` is not merely untidy: an instrument in no target is invisible, and the
invisibility CAUSED a duplication, which is `T109`'s class turned on the pass itself.
`p439` is wired as of `p423` and the register row below is re-grounded on ITS channel 2,
read at the SHA, rather than on the novel channel this arm first reached for.

🟢 The two instruments cover different axes, measured rather than assumed.  `p439` scans
only the six non-append-only shelves and keys on collisions WITHIN them.  `p422`'s failure
was a LIVE row against an APPEND-ONLY history row, which `p439` by design never sees -- and
on the very corpus where this gate was red, `p439` reports 0 findings.  So: `p439`
live-vs-live with the channel order; this arm live-vs-unrepairable-history.

A fold with NO register entry keeps the precedence arm unchanged, so nothing is loosened
where authority is absent -- which is most of the corpus.  The register is
`evidence/p423-canonical-casing.tsv`, one first-hand read per row, with the channel named,
because the channel here is NOT this base's usual raw-at-SHA read and must not be blended
into it.  `git ls-remote` cannot serve this question at all: it answers case-insensitively
and never echoes the owner's stored casing.
"""
import collections
import os
import re
import sys

SLUG = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
# 🔴 p349: THIS PATTERN MISSED ONE OF THE NINE SHELVES' HEADING FORM AND THE MISS WAS
# SILENT.  `agents/trending.md` writes its sections as `## 2026-10-20 · Pass 348 — …`,
# date first, while every other shelf writes `## Pass 348 · 2026-10-20 — …`.  Anchored at
# `^## Pass`, the splitter skipped every dated heading and found its "second pass
# heading" tens of thousands of lines down, in the old-form history — so the LIVE SECTION
# of that file was most of the file, and `gate-fold-identity` had been judging p349's
# contract against inherited text since p348.  🟢 It passed anyway, which is exactly why
# nothing said so: a boundary that is too GENEROUS only shows up when a gate that uses it
# finds something.  `p349`'s author-key gate was that gate, on its first run.
PASS_H2 = re.compile(r"^## .{0,40}?\bPass +\d+", re.M)
# A command template is not an address.  `p347` dropped two placeholders by hand; this
# is the same exclusion, written down so it is a rule and not a judgement call.
TEMPLATES = {"owner/repo", "org/repo", "user/repo", "owner/name", "your-org/your-repo"}


def slugs_in(text):
    out = []
    for m in SLUG.finditer(text):
        s = m.group(1).rstrip(".").rstrip(")")
        if s.endswith(".git"):
            s = s[:-4]
        if s.count("/") != 1:
            continue
        if s.lower() in TEMPLATES:
            continue
        out.append(s)
    return out


def split_live_section(text):
    """(current pass section, everything published before it).

    The live section runs from the top of the file to just before the SECOND `## Pass`
    heading.  A file with fewer than two pass headings is all live, which is the right
    answer for a file a pass has only just started.
    """
    heads = [m.start() for m in PASS_H2.finditer(text)]
    if len(heads) < 2:
        return text, ""
    return text[:heads[1]], text[heads[1]:]


def fold_index(paths):
    """folded slug -> {as published}."""
    idx = collections.defaultdict(set)
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            for s in slugs_in(fh.read()):
                idx[s.lower()].add(s)
    return idx


def census(paths):
    """Every folded collision, with a denominator.  A measurement, never a failure."""
    idx = fold_index(paths)
    groups = {k: sorted(v) for k, v in idx.items() if len(v) > 1}
    return len(idx), groups


# ---------------------------------------------------------------- p423
# The authority register.  Resolved against this file's location so the gate reads the
# same register whether it is run from the repo root or from its own directory.
_HERE = os.path.dirname(os.path.abspath(__file__))
# 🔴 p423: the first draft climbed THREE levels and landed on `compose/`, so the register
# loaded as {} and the gate fell back to pure precedence — green for the same reason a
# correct run is green, which is `gate-backlog-denominator`'s class.  Caught by asserting
# the known row loads, not by reading the path.  Four levels:
#   compose/code/p348-fold-identity -> compose/code -> compose -> <repo root>
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
CASING_REGISTER = os.path.join(_ROOT, "evidence", "p423-canonical-casing.tsv")


def canonical_casings(register=None):
    """folded slug -> the canonical casing, from the p423 authority register.

    Comment and blank lines are skipped, and so is the header row: a header compiled as
    data is a defect this base has published more than once.  A malformed or absent
    register yields {}, which returns the gate to pure precedence rather than silently
    passing everything.
    """
    path = register or CASING_REGISTER
    out = {}
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.lstrip().startswith("#"):
                continue
            cells = line.split("\t")
            if len(cells) < 2:
                continue
            folded, canonical = cells[0].strip(), cells[1].strip()
            if folded == "folded_slug":          # the header row is not a register entry
                continue
            if folded.count("/") != 1 or canonical.lower() != folded.lower():
                continue                          # a row that does not agree with itself
            out[folded.lower()] = canonical
    return out


def gate(paths, register=None):
    """The LIVE-section casing contract, adjudicated by authority where it is known.

    P348-NEW-CASING             precedence arm, for folds with no register entry.
    P348-NON-CANONICAL-CASING   authority arm: a live address against a registered
                                canonical.  Fatal, and it fires on the WRONG row rather
                                than on whichever row happened to be published first.
    """
    findings = []
    canon = canonical_casings(register)
    prior = collections.defaultdict(set)
    live = {}
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            text = fh.read()
        cur, old = split_live_section(text)
        live[p] = slugs_in(cur)
        for s in slugs_in(old):
            prior[s.lower()].add(s)
    # an address published in ANOTHER file's history counts as published
    for p in paths:
        for s in live[p]:
            fold = s.lower()
            if fold in canon:
                # 🟢 Authority beats precedence.  The register is a first-hand read; the
                # history is only whichever pass wrote first.
                if s != canon[fold]:
                    findings.append((p, "P348-NON-CANONICAL-CASING", s,
                                     "canonical is " + canon[fold]))
                continue
            prior_variants = prior.get(fold, set())
            if prior_variants and s not in prior_variants:
                findings.append((p, "P348-NEW-CASING", s,
                                 "published as " + "/".join(sorted(prior_variants))))
    return findings


def historical_casing_census(paths, register=None):
    """P423-HISTORICAL-NON-CANONICAL -- a backlog with a denominator, never a failure.

    Returns (registered_folds, rows).  An append-only shelf cannot be repaired backwards
    (`p347`), so a deviation already published is a measurement; only the live section is
    gated.
    """
    canon = canonical_casings(register)
    rows = []
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            _, old = split_live_section(fh.read())
        for s in slugs_in(old):
            fold = s.lower()
            if fold in canon and s != canon[fold]:
                rows.append((p, "P423-HISTORICAL-NON-CANONICAL", s,
                             "canonical is " + canon[fold]))
    return len(canon), rows


def main(argv):
    # P541: a gate that measures the files it is GIVEN must refuse an empty argument
    # list, because `total 0` without files is indistinguishable from a clean tree.
    mode = "gate"
    if argv and argv[0] in ("gate", "census", "casing-census"):
        mode, argv = argv[0], argv[1:]
    paths = [a for a in argv if os.path.exists(a)]
    if not paths:
        print("P541-NO-INPUT\tREFUSED: this gate measures the files it receives by "
              "argument and received none.  `total 0` with no files is NOT a clean "
              "tree.  Usage: fold_identity.py [gate|census] <shelf.md> ...",
              file=sys.stderr)
        return 2
    if mode == "casing-census":
        # p423 — the HISTORICAL arm of the authority register.  A backlog with a
        # denominator: an append-only shelf cannot be repaired backwards (`p347`), so a
        # deviation already published is a measurement and only the live section is gated.
        registered, rows = historical_casing_census(paths)
        print("# p423 historical casing census -- a backlog with a denominator, never a failure")
        print("archivo\thallazgo\tslug\tdetalle")
        for r in rows:
            print("\t".join(str(x) for x in r))
        print("#\tregistered_canonical_folds\t%d" % registered)
        print("#\thistorical_deviations\t%d" % len(rows))
        if not registered:
            print("#\tREFUSED\tthe p423 register loaded ZERO canonical folds -- a zero "
                  "denominator is not a clean corpus")
            return 2
        return 0
    if mode == "census":
        total, groups = census(paths)
        print("# p348 fold census -- a backlog with a denominator, never a failure")
        print("folded_slug\tvariants\tas_published")
        for k, v in sorted(groups.items()):
            print("%s\t%d\t%s" % (k, len(v), " ".join(v)))
        print("#\tdistinct_folded_addresses\t%d" % total)
        print("#\tcollision_groups\t%d" % len(groups))
        return 0
    findings = gate(paths)
    print("archivo\thallazgo\tslug\tdetalle")
    for f in findings:
        print("\t".join(str(x) for x in f))
    print("#\ttotal\t%d" % len(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
