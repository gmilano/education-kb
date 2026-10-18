#!/usr/bin/env python3
"""Controls for p283's ladder-case audit.

🔵 C5 and C6 are the two overclaims the first draft of this instrument made on this
base's own corpus, kept as controls so a later pass cannot reintroduce them.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from ladder_case import classify, spellings  # noqa: E402

FAILED = []


def run(name, toks, text, expect):
    got = classify(set(toks), text)
    ok = got == expect
    print(f"{'  ok  ' if ok else '  FAIL'} {name} (expected {expect}, got {got})")
    if not ok:
        FAILED.append(name)


# C1 — P1057's own finding: the ladder that varies the EXTENSION's case is closed.
run("C1 LICENSE.txt + LICENSE.TXT is closed",
    ["LICENSE.txt", "LICENSE.TXT"], 'p = ["LICENSE.txt", "LICENSE.TXT"]', "CASE-CLOSED")

# C2 — p282's defect: four rungs, stem case varied, extension spelled one way.
run("C2 README/readme.md with no uppercase ext is STEM-ONLY",
    ["README", "README.md", "readme.md", "README.rst"],
    'p = ["README", "README.md", "readme.md", "README.rst"]', "STEM-ONLY")

# C3 — a multi-rung ladder with no case variation at all is not a "single spelling".
# 🔴 The first draft called this SINGLE-SPELLING, which reads as "the author only
# thought of one name" when in fact they thought of four and cased them all alike.
run("C3 four rungs, no case variation, is CASE-UNVARIED",
    ["README", "README.md", "README.rst", "README.txt"],
    'p = ["README", "README.md", "README.rst", "README.txt"]', "CASE-UNVARIED")

run("C4 one rung is SINGLE-SPELLING", ["LICENSE"], 'p = "LICENSE"', "SINGLE-SPELLING")

# C5 — THE OVERCLAIM, control 1.  A `.lower()` far from the path vocabulary is not
# evidence that the PATH is folded.  The first draft returned CASE-INSENSITIVE for
# 316 of 580 ladders on this basis.
run("C5 a distant .lower() does not confer immunity",
    ["README.md"],
    'name = row.split()[0].lower()\n' + "\n" * 10 + 'p = "README.md"', "SINGLE-SPELLING")

# C6 — and the converse: a fold BESIDE the path vocabulary is a real screen hit.
run("C6 a fold beside the path is FOLD-ON-PATH",
    ["README.md"], 'for f in tree:\n    if f.lower() == "README.md".lower(): hit(f)',
    "FOLD-ON-PATH")

# C7 — enumeration beats every ladder: p275's "a path ladder cannot prove absence".
run("C7 ls-tree beside the path is TREE-ENUMERATED",
    ["LICENSE", "LICENSE.md"],
    'out = git("ls-tree", "-r", head)\nfor p in ("LICENSE", "LICENSE.md"): check(p)',
    "TREE-ENUMERATED")

# C8 — the extractor must find bare (unquoted) shell vocabulary, not just literals.
got = {t for _, t in spellings("for f in README README.MD LICENSE.TXT; do curl $f; done")}
ok = {"README", "README.MD", "LICENSE.TXT"} <= got
print(f"{'  ok  ' if ok else '  FAIL'} C8 bare shell path vocabulary is extracted (got {sorted(got)})")
if not ok:
    FAILED.append("C8")

# C9 — a family must not swallow a different family's token.
got = {f for f, _ in spellings('p = ["LICENSE.md", "README.md", "NOTICE", "COPYING"]')}
ok = got == {"licence", "readme", "notice", "copying"}
print(f"{'  ok  ' if ok else '  FAIL'} C9 families are kept apart (got {sorted(got)})")
if not ok:
    FAILED.append("C9")

# C10 — NEGATIVE CONTROL: a file with no path vocabulary yields no ladder at all.
got = spellings("def add(a, b):\n    return a + b\n")
print(f"{'  ok  ' if not got else '  FAIL'} C10 negative control: no vocabulary, no ladder")
if got:
    FAILED.append("C10")

print(f"\n{10 - len(FAILED)}/10 controls pass")
sys.exit(1 if FAILED else 0)
