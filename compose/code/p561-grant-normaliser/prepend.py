#!/usr/bin/env python3
"""p561 — insert a pass section immediately after a page's YAML frontmatter.

Every shelf page on this base is newest-pass-first below the frontmatter.  Doing
that with sed is how `557-C` happened (a pass wrote "amended in place" and
appended a duplicate instead), so it is a committed instrument here.

Usage:  prepend.py <page.md> <section.md>
Refuses if the page has no frontmatter, or if the section's first heading is
already present on the page (which would be a duplicate pass section).
"""
import pathlib, re, sys
page, sect = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
lines = page.read_text(encoding="utf-8").splitlines(keepends=True)
if lines[0].strip() != "---":
    sys.exit(f"REFUSED {page}: no frontmatter")
end = next(i for i, l in enumerate(lines[1:], 1) if l.strip() == "---")
body = sect.read_text(encoding="utf-8")
first = next(l for l in body.splitlines() if l.startswith("## "))
if first in "".join(lines):
    sys.exit(f"REFUSED {page}: section heading already present — {first[:60]}")
if not body.endswith("\n\n"):
    body = body.rstrip("\n") + "\n\n"
out = lines[: end + 1] + ["\n"] + [body] + lines[end + 1 :]
page.write_text("".join(out), encoding="utf-8")
print(f"ok   {page}: inserted {len(body.splitlines())} lines after frontmatter")
