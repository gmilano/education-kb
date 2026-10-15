#!/usr/bin/env python3
"""p230 — ACTION TB. The lint for the shape that produced p229's two defects.

THE SHAPE.  A lazy quantifier stops at the FIRST position where what follows
can match.  When the quantified atom is a character class and the terminator
is a lookahead over another character class, the match ends at the first
character in the INTERSECTION of the two.  If the TARGET may legitimately
contain such a character, the instrument silently truncates its own subject:

    ([A-Za-z0-9_.-]*?)(?=[)\\s`,.;:'"\\]]|$)      target may hold `.`
                            ^                      terminator holds `.`

`processing/p5.js` harvests as `processing/p5`.  Nothing errors; a shorter,
wrong answer is simply returned, which is why eleven passes did not see it.

THE TEST is therefore mechanical and needs no judgement: expand both classes
and intersect them.  A NON-EMPTY intersection is the defect; an empty one is
a lazy quantifier that is perfectly safe (most of them are, which is the
point — a grep for `*?` is not this lint).
"""
import re
import sys
from pathlib import Path

# T230-6: the terminator class of the very defect this lint hunts BEGINS with `)`
# — `(?=[)\s\`,.;:'"\]]|$)` — so a `([^)]*)` capture of the lookahead body stops
# at the first character of the thing it is trying to read. The first draft of
# this lint reported 0 findings for exactly that reason, including on its own
# positive control. A bracket class must be scanned, never captured with a
# negated-char group. Sixth defect found in this pass's instruments before
# publishing, and the SAME FAMILY as the defect under investigation.
LAZY = re.compile(r"\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\s*[*+]\?")

ESCAPES = {"\\s": " \t\n\r\f\v", "\\w": "", "\\d": "", "\\n": "\n", "\\t": "\t"}


def expand(cls: str) -> set:
    """Characters a bracket-class body can match. Ranges, escapes, literals."""
    out, i = set(), 0
    cls = cls.replace("|$", "")
    while i < len(cls):
        if cls[i] == "\\" and i + 1 < len(cls):
            tok = cls[i:i + 2]
            out.update(ESCAPES.get(tok, tok[1]))
            i += 2
            continue
        if i + 2 < len(cls) and cls[i + 1] == "-" and cls[i + 2] != "]":
            for o in range(ord(cls[i]), ord(cls[i + 2]) + 1):
                out.add(chr(o))
            i += 3
            continue
        out.add(cls[i])
        i += 1
    return out


def first_class_after(line: str, pos: int):
    """The body of the first bracket class inside a `(?=` that follows `pos`."""
    la = line.find("(?=", pos)
    if la < 0 or la - pos > 4:
        return None
    i = line.find("[", la)
    if i < 0 or i - la > 3:
        return None
    i += 1
    buf = []
    while i < len(line):
        if line[i] == "\\" and i + 1 < len(line):
            buf.append(line[i:i + 2]); i += 2; continue
        if line[i] == "]":
            return "".join(buf)
        buf.append(line[i]); i += 1
    return None


def scan(path: Path):
    """Findings in CODE. T230-7: this lint's first clean sweep flagged two lines of
    its own prose — docstrings that QUOTE the defective pattern in order to explain
    it. A lint that cannot tell code from the documentation of code reports its own
    explanation as a bug, so triple-quoted spans and comments are skipped. Seventh
    defect found in this pass's own instruments before publishing."""
    findings = []
    in_doc = False
    for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        fences = line.count(chr(34) * 3) + line.count(chr(39) * 3)
        was_doc = in_doc
        if fences % 2:
            in_doc = not in_doc
        if was_doc or (in_doc and fences % 2):
            continue
        if line.lstrip().startswith("#"):
            continue
        if "lazy-lint: fixture" in line:
            # T230-8: a SINGLE-LINE triple-quoted literal holding the defective pattern —
            # which is exactly how a positive-control fixture is written — opens and closes
            # its fence on one line, so the docstring tracker sees an even count and lets it
            # through. The lint cannot tell a fixture from code by looking, and guessing
            # would be the same class of error it hunts, so a fixture DECLARES itself.
            # Eighth defect found in this pass's own instruments before publishing.
            continue
        for m in LAZY.finditer(line):
            target = m.group(1)
            term = first_class_after(line, m.end())
            if term is None:
                continue
            overlap = expand(target) & expand(term)
            overlap.discard("^")
            if overlap:
                findings.append((n, "".join(sorted(overlap)), line.strip()[:120]))
    return findings


def main():
    roots = [Path(a) for a in sys.argv[1:]] or [Path(".")]
    total = 0
    for root in roots:
        files = sorted(root.rglob("*.py")) if root.is_dir() else [root]
        for f in files:
            if "fixtures" in f.parts:
                continue
            for n, chars, src in scan(f):
                total += 1
                print(f"{f}\t{n}\t{chars!r}\t{src}")
    print(f"# {total} finding(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
