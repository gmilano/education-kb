#!/usr/bin/env python3
"""p911 — controls for the identifier-collision gate.

The first case is the defect this gate was built for, reproduced from the real file: `p910`
published a second `## T25` in `intel/trends.md` at line 1391 while line 934 already held one.

🔴 One control here exists because this gate's FIRST cut passed on an empty tree.  A gate that
reports PASS over zero identifiers is `p541`/`Gap 245` all over again — and `p383` is the worked
example of that defect reaching print.  `empty-tree` therefore asserts exit **2**, not 0.

Run: python3 -I test_collision_gate.py       (no network, writes only to a temp dir)
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "cg", os.path.join(os.path.dirname(os.path.abspath(__file__)), "collision_gate.py"))
cg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cg)

HDR = "---\nindustry: education\nregion: Global\nupdated: 2026-11-19\n---\n\n"

# label, trends.md body, patterns.md body, expected exit
CASES = [
    ("p910's real defect: a duplicate T25",
     "## T24 — a\n## T25 — the licence trap moved to data\n## T33 — b\n## T25 — national-curriculum supply\n",
     "## P1 — x\n", 1),
    ("clean tree",
     "## T1 — a\n## T2 — b\n## T33 — c\n", "## P1 — x\n## P29 — y\n", 0),
    ("gaps in the sequence are LEGAL — re-scoped rows leave real holes",
     "## T1 — a\n## T9 — b\n## T40 — c\n", "## P2 — x\n## P29 — y\n", 0),
    ("a duplicate in patterns.md, not trends.md",
     "## T1 — a\n", "## P7 — x\n## P7 — y\n", 1),
    ("three copies of one identifier",
     "## T5 — a\n## T5 — b\n## T5 — c\n", "## P1 — x\n", 1),
    ("### subsections are NOT the register and may repeat freely",
     "## T1 — a\n### T1 — detail\n### T1 — more detail\n", "## P1 — x\n", 0),
    ("a T-number inside prose is not a heading",
     "## T1 — a\nThis row supersedes T1 and is cited as T1 throughout.\n", "## P1 — x\n", 0),
    ("empty registers must REFUSE, not pass (p541/Gap 245)", "", "", 2),
]


def run_case(trends, patterns):
    d = tempfile.mkdtemp(prefix="p911-collision-")
    try:
        os.makedirs(os.path.join(d, "intel"))
        os.makedirs(os.path.join(d, "compose"))
        with open(os.path.join(d, "intel", "trends.md"), "w") as f:
            f.write(HDR + trends)
        with open(os.path.join(d, "compose", "patterns.md"), "w") as f:
            f.write(HDR + patterns)
        return cg.main([d])
    finally:
        shutil.rmtree(d)


def main(argv):
    if argv:
        sys.stderr.write("🔴 test_collision_gate.py takes no arguments.\n")
        return 2
    fails = []
    for label, trends, patterns, expect in CASES:
        got = run_case(trends, patterns)
        if got != expect:
            fails.append(f"   🔴 {label}: expected exit {expect}, got {got}")
    # a missing register file is a defect, not a clean tree
    d = tempfile.mkdtemp(prefix="p911-collision-absent-")
    try:
        got = cg.main([d])
        if got not in (1, 2):
            fails.append(f"   🔴 absent register files: expected 1 or 2, got {got}")
    finally:
        shutil.rmtree(d)
    # too many arguments must refuse
    if cg.main(["a", "b"]) != 2:
        fails.append("   🔴 two arguments: expected refusal (exit 2)")

    print(f"── p911-identifier-collision suite ({len(CASES) + 2} controls: p910's real "
          f"duplicate, legal sequence gaps, ### subsections, prose mentions, empty-register "
          f"refusal, absent files, arity)")
    for f in fails:
        print(f)
    if fails:
        print(f"🔴 FAIL — {len(fails)}/{len(CASES) + 2}")
        return 1
    print(f"   PASS — {len(CASES) + 2}/{len(CASES) + 2}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
