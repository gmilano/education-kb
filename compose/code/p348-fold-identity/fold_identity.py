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
"""
import collections
import os
import re
import sys

SLUG = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
PASS_H2 = re.compile(r"^## +Pass +\d+", re.M)
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


def gate(paths):
    """P348-NEW-CASING over each file's live pass section."""
    findings = []
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
            prior_variants = prior.get(s.lower(), set())
            if prior_variants and s not in prior_variants:
                findings.append((p, "P348-NEW-CASING", s,
                                 "published as " + "/".join(sorted(prior_variants))))
    return findings


def main(argv):
    # P541: a gate that measures the files it is GIVEN must refuse an empty argument
    # list, because `total 0` without files is indistinguishable from a clean tree.
    mode = "gate"
    if argv and argv[0] in ("gate", "census"):
        mode, argv = argv[0], argv[1:]
    paths = [a for a in argv if os.path.exists(a)]
    if not paths:
        print("P541-NO-INPUT\tREFUSED: this gate measures the files it receives by "
              "argument and received none.  `total 0` with no files is NOT a clean "
              "tree.  Usage: fold_identity.py [gate|census] <shelf.md> ...",
              file=sys.stderr)
        return 2
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
