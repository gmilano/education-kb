#!/usr/bin/env python3
"""`p349-keyed-authors/author_key_gate.py` — `ACTION ZZ-ac`: AN AUTHOR FIGURE WITH NO KEY.

p348 tried to re-derive one of this base's own published cells —
`terracotta-education/terracotta`, *"2 815 commits, 18 authors"* — and found the commit
count exact and the author count underivable: `%an` 14, `%ae` 18, `%an|%ae` 20. p349 ran
the same read and **the key is `%ae`**, re-derived to the digit (`evidence/keyed-authors.
2026-10-20-p349.tsv`). 🔵 So the figure was never wrong; it was UNNAMED, and an unnamed
figure is indistinguishable from a wrong one by anybody holding a different key.

🔴 Why that is a live hazard and not a tidiness point: p346's PII refusal means a
successor re-deriving an author cell reaches for `%an` (names look less like personal
data than addresses do, which is backwards for a count but forward for a refusal). Over
the eight rows p348 measured, `%an` runs 1–9 BELOW `%ae`. Every published author figure
would read as inflated, and a KB whose repositories appear to be shedding contributors
is worse than one with no author column at all.

So: a figure in a LIVE pass section must name its key on the line that carries it.
`T37`'s `recount` cannot do this — it has no key to check against — which is why the
rule lives here and not there.

    author_key_gate.py gate   <shelf files...>   # P349-UNKEYED-AUTHORS over live sections
    author_key_gate.py census <shelf files...>   # the inherited backlog, with a denominator
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                os.pardir, "p348-fold-identity"))
from fold_identity import split_live_section  # noqa: E402

#: A figure, not a word: `18 authors`, `18 autores`, `18 contributors`, `18 committers`.
FIGURE = re.compile(r"\b\d[\d  ,.]*\s*(?:authors?|autores?|contributors?|committers?)\b",
                    re.I)
#: The key vocabulary. `%an|%ae` contains both single keys, so it needs no entry.
KEY = re.compile(r"%ae|%an|\bidentities\b|\bidentidades\b|\baddress(?:es)?\b|"
                 r"\bdirecciones\b|\bname-keyed\b|\bNO-KEY\b", re.I)


def _rows(text):
    return [l for l in text.splitlines() if FIGURE.search(l)]


def gate(paths):
    findings = []
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            live, _ = split_live_section(fh.read())
        for line in _rows(live):
            if not KEY.search(line):
                findings.append((p, "P349-UNKEYED-AUTHORS",
                                 FIGURE.search(line).group(0).strip(),
                                 "no key named on the line (%ae / %an / identities)"))
    return findings


def census(paths):
    keyed = unkeyed = 0
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            for line in _rows(fh.read()):
                if KEY.search(line):
                    keyed += 1
                else:
                    unkeyed += 1
    return keyed, unkeyed


def main(argv):
    mode = "gate"
    if argv and argv[0] in ("gate", "census"):
        mode, argv = argv[0], argv[1:]
    # P541: refuse an empty argument list — `total 0` with no files is not a clean tree.
    if not argv:
        sys.stderr.write("p349-author-key: no shelf files given — refusing (P541)\n")
        return 2
    if mode == "census":
        keyed, unkeyed = census(argv)
        print("keyed_lines\t%d" % keyed)
        print("unkeyed_lines\t%d" % unkeyed)
        print("total\t%d" % (keyed + unkeyed))
        return 0
    findings = gate(argv)
    print("archivo\thallazgo\tcifra\tdetalle")
    for f in findings:
        print("\t".join(f))
    print("#\ttotal\t%d" % len(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
