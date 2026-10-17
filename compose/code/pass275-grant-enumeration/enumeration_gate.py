#!/usr/bin/env python3
"""p275 — the OFFLINE half of ACTION p275: no shelf may assert a negative licence
verdict that an enumeration refutes, and no negative verdict may rest on a path ladder
that was never enumerated.

WHY THIS EXISTS.  p274 found `gegok12` refuted twice by probing a slug that does not
exist, and ranked "re-probe every negative licence verdict with ls-remote as a positive
control" as p275's highest-value item.  The control passed on every row -- and running it
exposed that the LADDER, not the slug, is the defect:

  * `os4ed/openSIS-Classic` was carried licence-UNVERIFIED for multiple passes.  Its grant
    is at `docs/License.txt` (GPL-2.0, 17 286 B).  The 19-path ladder never tried that
    spelling, so every one of its 76 probes was guaranteed to miss.
  * `ls1intum/Athena` was carried "no grant, treat as all-rights-reserved, ask TUM in
    writing" across three passes.  12 of its 14 manifests declare `license = "MIT"`.  The
    ladder probed the ROOT `pyproject.toml` -- the one manifest in the repo that is silent.

A ladder can only ever refute the paths it tried.  This gate makes that unfalsifiable
state visible instead of letting it read as a finding.  No network: it reads the shelves
and the enumeration ledgers already committed to `evidence/`.

    python3 -I enumeration_gate.py --root /path/to/education-kb
"""
import argparse
import glob
import os
import re
import sys

SHELVES = [
    "agents/top.md", "agents/trending.md", "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md", "intel/market.md", "intel/trends.md", "compose/patterns.md",
]

# A shelf is ASSERTING an absent grant when one of these appears on the line.
NEGATIVE = re.compile(
    r"no licen[cs]e payload|no payload|no grant|serves no grant|PRE-LICEN[CS]E|"
    r"licen[cs]e[- ]unverified|licen[cs]e UNVERIFIED|all rights reserved|"
    r"treat as all-rights-reserved",
    re.I,
)

# ...but these mark the line as NARRATING a verdict that has since been overturned.
# Greedy by construction (ACTION TB): no lazy quantifiers anywhere in this module.
RETRACTION = re.compile(
    # 🟢 p275 correction 3a: the STEM, not the past participle.  A cell that says it
    # "retracts" an earlier verdict is narrating one just as much as a "RETRACTED" banner.
    r"retract|RESOLVED|REFUTED|refuted|NOW READ|does not exist|UPHELD|"
    r"was FALSE|FALSE in both|no longer|correction|CORRECTED|"
    # 🟢 p275: `trending.md` is APPEND-ONLY, so a wrong cell there is annotated in place
    # with a dated supersede marker rather than rewritten.  The original claim STAYS on
    # the line by design -- so the marker, not the absence of the claim, is what tells the
    # gate the line is narration.
    r"SUPERSEDED|was wrong",
    re.I,
)

# 🟢 p275: a line cannot coherently assert "there is no grant" AND publish the grant.
# When it does both, it is a CORRECTION narrating the claim it replaces -- which is the
# idiom this base writes corrections in, and the shape of every line this predicate was
# added for.  Requires an SPDX-ish token AND concrete grant evidence (a licence-bearing
# path or a byte count), so "MIT" appearing alone in prose is not enough to silence a row.
SPDX = re.compile(
    r"\b(MIT|Apache-2\.0|BSD-[23]-Clause|BSD|GPL-[23]\.0|GPL-2|AGPL-3\.0|LGPL-3\.0|"
    r"CC0-1\.0|CC-BY(-NC)?(-SA)?-4\.0|MPL-2\.0|EUPL)\b")
# 🔴 p275: NO global re.I here, and the reason is a defect this predicate caused.
# With re.I the `\bLICEN[CS]E\b` alternative -- meant to match a FILENAME in caps --
# matched a vendor's marketing prose, *"free core is free forever under the MIT licence"*,
# and silenced two live stale claims about `Gego-K12/gegok12`.  A predicate that
# suppresses rows must be narrower than the rows it suppresses.  Case is load-bearing:
# `LICENSE` is a filename; `licence` is a word.
GRANT_EVIDENCE = re.compile(
    r"[Ll]icen[cs]e\.(txt|md|rtf)"      # License.txt, LICENSE.md, LICENSE.rtf
    r"|/[Ll]icen[cs]e\b"                # a PATH ending in a licence file
    r"|\bLICEN[CS]E\b"                  # the bare filename, in caps
    r"|\d[\d\u00a0 ]*B\b"              # a measured byte count, e.g. "17 286 B"
    r"|(?i:manifests? declare)"         # the metadata channel, stated
    r"|(?i:read at payload)")


def states_a_grant(line):
    """Does this line publish a grant, as well as quoting an absence?"""
    return bool(SPDX.search(line) and GRANT_EVIDENCE.search(line))


SLUG = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

# Directories whose licence files belong to a VENDORED dependency, not to the repo.
VENDORED = re.compile(
    r"(^|/)(vendor|node_modules|custompackages|libraries|third_party|thirdparty|"
    r"precompiled-icons|plugins|samples)(/|$)",
    re.I,
)
# Extensions that make a licence-like path a SOURCE FILE, not a grant.
SOURCEY = re.compile(r"\.(php|java|vue|py|js|ts|jsx|tsx|go|rb|cs|png|svg|jpg|gif)$", re.I)
LICENCEY = re.compile(
    r"(^|/)(licen[cs]e|copying|notice|unlicense|eupl|copyright)", re.I
)


def candidate_grants(paths):
    """Of the licence-like paths an enumeration found, which could be THE repo's grant?"""
    out = []
    for p in paths:
        p = p.strip()
        if not p or p == "NONE_IN_TREE":
            continue
        if not LICENCEY.search(p):
            continue
        if VENDORED.search(p) or SOURCEY.search(p):
            continue
        out.append(p)
    return out


def load_ledgers(root):
    """slug -> list of licence-like paths, from every committed enumeration ledger."""
    ledger, dead = {}, set()
    pattern = os.path.join(root, "evidence", "tree-enumeration.*.tsv")
    for path in sorted(glob.glob(pattern)):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("#") or not line.strip():
                    continue
                cols = line.rstrip("\n").split("\t")
                if len(cols) < 5 or cols[0] == "slug":
                    continue
                slug, paths_cell = cols[0].strip(), cols[4]
                # 🔴 p275: a slug that does not RESOLVE must never be attributed a shelf's
                # claim about a real project.  `gegok12/gegok12` (dead) and
                # `Gego-K12/gegok12` (real, MIT at root) share the basename `gegok12`, and
                # attributing the dead one LAUNDERED a false "NOT ESTABLISHED" claim about
                # the real repo into a VERIFIED-ABSENT pass.  p251-prefix-collision's class.
                if re.search(r"\bFAIL\b|DOES_NOT_RESOLVE", cols[1] + paths_cell):
                    dead.add(slug)
                    continue
                # the cell is a comma-separated enumeration, or a NONE marker
                if re.search(r"\bNONE\b|NONE_IN_TREE", paths_cell):
                    ledger[slug] = []
                else:
                    ledger[slug] = [c.strip() for c in paths_cell.split(",")]
    return ledger, dead


def attribute(line, names=()):
    """Which slug does each negative phrase on this line actually refer to?

    🔴 p275, two corrections, both found by running the gate on the live shelves:

    1. The first version attributed every negative phrase to every slug on the line, and
       reported `ls1intum/Artemis` -- an MIT row with a root LICENSE -- as refuting
       itself.  The phrase on that line is about `ls1intum/Athena`, named four slugs later
       in the same cell.  One line can carry two subjects.
    2. Nearest-preceding-slug alone was still wrong on `verticals/solutions.md:28`, where
       the subject is the bare word **Athena** in bold PROSE and the only slug on the line
       is Artemis.  A project does not have to be hyperlinked to be the subject.

    Rule: a negative phrase belongs to the nearest project named before it -- whether that
    name arrives as a slug or as a bare repo name the enumeration ledger already knows.
    """
    marks = [(m.start(), m.group(1).rstrip(".")) for m in SLUG.finditer(line)]
    for slug in names:
        base = slug.split("/")[-1]
        # 🟢 p275 correction 3b: a POSSESSIVE mention is a modifier, not the subject.
        # "Artemis's feedback-suggestion engine ... treat as all-rights-reserved" is a
        # sentence about ATHENA; `Artemis's` only says whose engine it is.  Reported
        # ls1intum/Artemis -- which has a root LICENSE -- as refuting itself, again.
        for m in re.finditer(r"\b" + re.escape(base) + r"(?!'s|\u2019s)\b", line, re.I):
            marks.append((m.start(), slug))
    if not marks:
        return []
    marks.sort()
    owners = set()
    for phrase in NEGATIVE.finditer(line):
        before = [s for s in marks if s[0] < phrase.start()]
        owners.add(before[-1][1] if before else marks[0][1])
    return sorted(owners)


def scan(root):
    ledger, dead = load_ledgers(root)
    refuted, verified, unenumerated = [], [], []
    for shelf in SHELVES:
        full = os.path.join(root, shelf)
        if not os.path.exists(full):
            continue
        with open(full, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                if not NEGATIVE.search(line):
                    continue
                if RETRACTION.search(line) or states_a_grant(line):
                    continue  # narration of an overturned verdict, not a live claim
                for slug in attribute(line, ledger.keys()):
                    if slug not in ledger:
                        unenumerated.append((shelf, n, slug))
                        continue
                    grants = candidate_grants(ledger[slug])
                    if grants:
                        refuted.append((shelf, n, slug, grants))
                    else:
                        verified.append((shelf, n, slug))
    return refuted, verified, unenumerated


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    refuted, verified, unenumerated = scan(args.root)

    print("# p275 -- enumeration gate.  A negative licence verdict is only a finding if the")
    print("# tree was ENUMERATED.  Otherwise it is the state of a path ladder.")
    for shelf, n, slug, grants in refuted:
        print(f"REFUTED\t{shelf}:{n}\t{slug}\tenumeration found a candidate grant: {','.join(grants)}")
    for shelf, n, slug in verified:
        print(f"VERIFIED-ABSENT\t{shelf}:{n}\t{slug}\tenumerated, no candidate grant in tree")
    for shelf, n, slug in unenumerated:
        print(f"QUEUE-UNENUMERATED\t{shelf}:{n}\t{slug}\tnegative verdict rests on a path ladder")
    print(f"# REFUTED={len(refuted)} VERIFIED-ABSENT={len(verified)} "
          f"QUEUE-UNENUMERATED={len(unenumerated)}")
    if refuted:
        print("# FAIL: a shelf asserts an absent grant that an enumeration refutes.")
        return 1
    print("# PASS: no live negative verdict is contradicted by an enumeration.")
    print("#   (QUEUE rows are NOT a failure signal -- they are the enumeration backlog.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
