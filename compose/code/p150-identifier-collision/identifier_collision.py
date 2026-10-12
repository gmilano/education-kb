"""p150-identifier-collision — `ACTION FM`: a committed gate for `T75`.

🔴 **The defect `T75` names.** Pattern and thesis numbers on this shelf are allocated
from an *unread high-water mark*: a pass picks "the next number" from memory instead of
from the page, and two different patterns end up sharing one identifier. p149 found
`P32` naming two live patterns and renumbered the later to `P35`. 🔵 **The habit, not the
typo, is the cause** — the same one produced the thesis collisions `P144-F` recorded.

## What counts as a collision

A pattern page carries three kinds of heading:

  `## 🆕 `P30` — … *(new, p146 …)*`        a FIRST allocation
  `## 🔁 `P18` AMENDED at step 1 — …`       a REVISIT of an existing pattern
  `## P1 — Auditable AI tutor …`            an early pattern, no marker

🟢 **A revisit is legitimate and must not be flagged** — `P18` is amended five times on
purpose. 🔴 **A collision is two FIRST allocations of the same number**, which is what
`P32` was and what this module detects.

🔵 **Two first allocations with the SAME title are a duplicate heading, not a
collision** — reported separately, because the remedy differs: one is a renumber, the
other is a deletion.
"""
import os
import re
import sys
from collections import defaultdict

# `## 🆕 🟢 `P36` — title *(new, p149 — …)*` or `## P1 — title *(…)*`.
#
# 🔵 `markers` admits only NON-WORD characters — emoji, backticks, whitespace. That is
# what separates an allocation from a subsection: `### 🔴 What `P36` does NOT solve`
# carries the word "What" before the id and is correctly not read as an allocation.
#
# `mid` is whatever sits between the id and the em dash (`AMENDED at step 1`,
# `RECAVEATED`, `rewritten`), and it is searched for revisit markers alongside the
# title, because this page states the revisit verb in both places.
HEADING = re.compile(r"^(#{2,3})\s+(?P<markers>[^\w\n]*)`?(?P<id>P\d+)`?"
                     r"(?P<mid>[^—–\n]*?)\s*(?:—|–)\s*(?P<title>.*)$")

# A revisit names itself in the markers or in the title's leading verb.
REVISIT = re.compile(r"🔁|\bAMENDED\b|\bRECAVEATED\b|\bCORRECTED\b|\brewritten\b"
                     r"|\bSTRENGTHENED\b|\bamended\b|\bRENUMBERED\b", re.I)

# A first allocation says so parenthetically: *(new, p147 — …)*.
FIRST = re.compile(r"\(\s*new\b", re.I)

# `T74`, `T75` … in the thesis register, and `P149-A` style finding ids.
THESIS = re.compile(r"`(T\d+)`")
FINDING = re.compile(r"`(P\d+-[A-Z]+)`")


def normalise_title(title):
    """Strip emoji, markdown and the trailing parenthetical so two titles compare."""
    t = re.sub(r"\*\([^)]*\)\*\s*$", "", title)
    t = re.sub(r"[`*_]", "", t)
    t = re.sub(r"[^\w\s—–-]", " ", t)
    return " ".join(t.split()).lower()


def classify(line):
    """(id, kind, title) for a pattern heading, or None if the line is not one."""
    m = HEADING.match(line)
    if not m:
        return None
    pid, title = m.group("id"), m.group("title")
    markers = m.group("markers") + m.group("mid")
    if REVISIT.search(markers) or REVISIT.search(title):
        kind = "REVISIT"
    elif FIRST.search(title):
        kind = "FIRST"
    else:
        kind = "UNMARKED"
    return pid, kind, normalise_title(title)


def scan_patterns(text):
    """{id: [(kind, title, lineno)]} over every pattern heading in a page."""
    out = defaultdict(list)
    for i, line in enumerate(text.splitlines(), 1):
        c = classify(line)
        if c:
            out[c[0]].append((c[1], c[2], i))
    return out


def collisions(index):
    """Ids whose FIRST allocations name two or more DIFFERENT patterns.

    🔵 `UNMARKED` headings count as first allocations: `P1`..`P14` predate the marker
    convention, so excluding them would blind the gate to the oldest half of the page.
    """
    found = []
    for pid, entries in sorted(index.items(), key=lambda kv: int(kv[0][1:])):
        firsts = [e for e in entries if e[0] in ("FIRST", "UNMARKED")]
        titles = {e[1] for e in firsts}
        if len(titles) > 1:
            found.append(dict(id=pid, kind="COLLISION", count=len(firsts),
                              titles=sorted(titles),
                              lines=[e[2] for e in firsts]))
        elif len(firsts) > 1:
            found.append(dict(id=pid, kind="DUPLICATE_HEADING", count=len(firsts),
                              titles=sorted(titles),
                              lines=[e[2] for e in firsts]))
    return found


def register_collisions(text, rx):
    """Ids in a register that are DEFINED more than once.

    A definition is a table row or a heading whose first cell/word is the id. A mention
    inside prose is not a definition, so only line-leading occurrences count.
    """
    defined = defaultdict(list)
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not (s.startswith("|") or s.startswith("#")):
            continue
        cell = s.lstrip("#| ").split("|")[0] if s.startswith("|") else s.lstrip("# ")
        m = rx.search(cell)
        if m:
            defined[m.group(1)].append(i)
    return {k: v for k, v in defined.items() if len(v) > 1}


def gate(patterns_text):
    """(exit_code, report_lines). Non-zero when a collision is present."""
    index = scan_patterns(patterns_text)
    found = collisions(index)
    hard = [f for f in found if f["kind"] == "COLLISION"]
    lines = ["ids=%d collisions=%d duplicate_headings=%d"
             % (len(index), len(hard), len(found) - len(hard))]
    for f in found:
        lines.append("  %-18s %-6s lines=%s" % (f["id"], f["kind"],
                                               ",".join(str(x) for x in f["lines"])))
        for t in f["titles"]:
            lines.append("      - %s" % t[:96])
    return (1 if hard else 0), lines


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    code, lines = gate(text)
    for ln in lines:
        print(ln)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
