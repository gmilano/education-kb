#!/usr/bin/env python3
"""`P174` — the clone-path gate.

An instrument that names the KB's root with an ABSOLUTE path runs in the pass that
wrote it and nowhere else. p172's `classify_bodies.sh` sourced
`/tmp/education-kb/compose/code/lib/license_family.sh`; p173's clone was at
`/home/user/education-kb`, so the instrument could not run at all — and the pass
that needed it had to re-implement the classifier it was supposed to reuse
(`T247`).

This gate finds that defect before it is committed. It sweeps the instrument tree
for absolute paths that look like a KB CLONE ROOT and classifies each hit:

  LIVE    — the path is in executable text. The instrument is broken outside the
            clone it was written in. This is what the gate fails on.
  COMMENT — the path is inside a `#` comment or a Python docstring. Historical
            narrative about a defect is not the defect; nine of this KB's files
            describe p120's and p172's hardcoded paths and must stay readable.
  USAGE   — the path is an example INPUT directory handed to the script as an
            argument (`/tmp/edu-trees`), not the KB root. Parameterised already.

A `fixtures/` directory is DATA, not an instrument: the gate's own positive
controls have to contain the defect, so the sweep skips those paths and the suite
checks them through the classifier directly.

The classification rule is the finding, so it is stated here rather than implied:
a hit is LIVE only when the line, with any leading `#` comment stripped, still
contains the path AND the line is not inside a triple-quoted block.

`ROOT_PATTERNS` deliberately does NOT include bare `/tmp/` — scratch files like
`/tmp/lic.$$` are correct, portable and used by a dozen instruments. The gate is
about the KB ROOT, not about temporary files.
"""
from __future__ import annotations

import pathlib
import re
import sys

# The KB root as four passes have hardcoded it, plus the shape of any future one.
ROOT_PATTERNS = re.compile(
    r"(/tmp/education-kb|/home/[A-Za-z0-9_.-]+/education-kb|/root/education-kb"
    r"|/tmp/globant-kb|/home/[A-Za-z0-9_.-]+/globant-kb)"
)
SCRIPT_SUFFIXES = (".sh", ".py")
TRIPLE = ('"""', "'''")


def classify_lines(text: str, *, suffix: str) -> list[tuple[int, str, str]]:
    """Return (lineno, verdict, line) for every line carrying a clone-root path."""
    out: list[tuple[int, str, str]] = []
    in_doc: str | None = None
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip("\n")
        opened_here = False
        if suffix == ".py":
            if in_doc is None:
                for q in TRIPLE:
                    if line.count(q) == 1:
                        in_doc, opened_here = q, True
                        break
            elif in_doc in line:
                in_doc = None
                opened_here = True       # the closing line is still docstring text
        if not ROOT_PATTERNS.search(line):
            continue
        if in_doc is not None or opened_here:
            out.append((n, "COMMENT", line.strip()))
            continue
        stripped = re.sub(r"(?<!\$)#.*$", "", line)
        if not ROOT_PATTERNS.search(stripped):
            out.append((n, "COMMENT", line.strip()))
        else:
            out.append((n, "LIVE", line.strip()))
    return out


def sweep(root: pathlib.Path) -> list[tuple[str, int, str, str]]:
    rows: list[tuple[str, int, str, str]] = []
    base = root / "compose" / "code"
    for path in sorted(base.rglob("*")):
        if not path.is_file() or path.suffix not in SCRIPT_SUFFIXES:
            continue
        if path.resolve() == pathlib.Path(__file__).resolve():
            continue                     # the gate quotes the patterns it hunts
        if "fixtures" in path.relative_to(base).parts:
            continue                     # positive controls must carry the defect
        text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, verdict, line in classify_lines(text, suffix=path.suffix):
            rows.append((str(path.relative_to(root)), lineno, verdict, line))
    return rows


def main(argv: list[str]) -> int:
    # P174-KC: the KB root comes from THIS file. <kb>/compose/code/<instrument>/ -> parents[3].
    root = pathlib.Path(argv[1]).resolve() if len(argv) > 1 else pathlib.Path(__file__).resolve().parents[3]
    rows = sweep(root)
    print("file\tline\tverdict\ttext")
    for f, n, v, line in rows:
        print(f"{f}\t{n}\t{v}\t{line[:160]}")
    live = [r for r in rows if r[2] == "LIVE"]
    print(f"# hits={len(rows)} LIVE={len(live)} COMMENT={len(rows) - len(live)}")
    if live:
        print("# P174-LIVE-CLONE-PATH: " + ", ".join(sorted({f'{f}:{n}' for f, n, _, _ in live})))
    return 1 if live else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
