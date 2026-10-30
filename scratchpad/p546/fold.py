#!/usr/bin/env python3
"""Fold each named file to one normalised line: "<path>\x1f<text>".

The whole file collapses to a single line so that a quote wrapped across source
lines still matches as one string — the defect that made the README-only stage
report false FAILs.
"""
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from importlib import import_module
norm = import_module("quote-gate").norm

for p in sys.argv[1:]:
    try:
        t = pathlib.Path(p).read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    folded = norm(t)
    if folded:
        sys.stdout.write(p + "\x1f" + folded + "\n")
