#!/usr/bin/env python3
"""p911 — a published identifier may not name two different things.

Built because `p910` published a new trend as **`T25`** in `intel/trends.md` while `T25` was
already taken (`"The licence trap has moved from the code to the data and content assets"`,
added `p906`) and the file's maximum was **`T33`**.  Nothing caught it: 139 gates run in
`make hooks` and not one of them checks that a delivery file's own identifiers are distinct.

🔴 Why this is a data defect and not a typo.  `gate-case-collision` (p439) exists on exactly
this reasoning for repository addresses — *"two spellings of one repository compile to two
entities"* — and the converse is just as bad: **two trends under one identifier compile to one
entity**, so `T25` resolves to whichever the compiler reads last and the other becomes
unreachable. Every `T25` citation already written in this tree (`trends.md`, `market.md`,
`agents/trending.md`, `compose/patterns.md`) now points at an ambiguity, and a KB whose
standing rule is `M1 cite or disclaim` cannot have ambiguous cite targets.

Scope: the `##`-level numbered registers this tree publishes and cites —
  `intel/trends.md`      `## T<n>`
  `compose/patterns.md`  `## P<n>`
A monotonic-successor check is deliberately NOT asserted: this tree's registers have real
gaps from re-scoped rows, and demanding density would fail honest files. Uniqueness is the
property that citation integrity actually needs.

No network.  Run from anywhere: paths resolve from this file.
Usage: collision_gate.py [ROOT]
"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

# file, identifier regex on a `##` heading, human name of the register
REGISTERS = [
    ("intel/trends.md", re.compile(r"^##\s+(T\d+)\b"), "trend"),
    ("compose/patterns.md", re.compile(r"^##\s+(P\d+)\b"), "pattern"),
]


def scan(root):
    """Returns (findings, counts). A finding is (file, register, ident, [line numbers])."""
    findings, counts = [], {}
    for rel, pat, label in REGISTERS:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            findings.append((rel, label, "FILE-ABSENT", []))
            continue
        where = collections.defaultdict(list)
        with open(path, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                m = pat.match(line)
                if m:
                    where[m.group(1)].append(n)
        counts[rel] = len(where)
        for ident, lines in sorted(where.items(), key=lambda kv: int(kv[0][1:])):
            if len(lines) > 1:
                findings.append((rel, label, ident, lines))
    return findings, counts


def main(argv):
    if len(argv) > 1:
        sys.stderr.write("🔴 collision_gate.py takes at most one argument (ROOT).\n")
        return 2
    root = os.path.abspath(argv[0]) if argv else DEFAULT_ROOT
    if not os.path.isdir(root):
        sys.stderr.write(f"🔴 not a directory: {root}\n")
        return 2
    findings, counts = scan(root)
    total = sum(counts.values())
    # 🔴 p541/Gap 245: an instrument that measured nothing may not report success.
    if total == 0:
        sys.stderr.write(
            f"🔴 p911-identifier-collision judged ZERO identifiers under {root}.\n"
            "   That is a broken invocation, not a clean tree — refusing to report PASS.\n")
        return 2
    print(f"── p911-identifier-collision — {total} published identifiers judged "
          + ", ".join(f"{v} in {k}" for k, v in sorted(counts.items())))
    if findings:
        for rel, label, ident, lines in findings:
            if ident == "FILE-ABSENT":
                print(f"   🔴 {rel}: register file absent")
            else:
                print(f"   🔴 {rel}: {label} {ident} is published "
                      f"{len(lines)} times, at lines {', '.join(map(str, lines))} — "
                      f"a citation to {ident} resolves to only one of them")
        print(f"🔴 FAIL — {len(findings)} colliding identifier(s)")
        return 1
    print("   PASS — every published identifier names exactly one thing")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
