#!/usr/bin/env python3
"""Insert a block into a curated page directly after its YAML frontmatter, and
refresh the frontmatter's `updated:` field. Append-only pages keep their whole
history below the new block, which is the point of them.

Usage: insert.py <page> <block-file> [--updated YYYY-MM-DD]
"""
import re
import sys

page, block = sys.argv[1], sys.argv[2]
updated = None
if "--updated" in sys.argv:
    updated = sys.argv[sys.argv.index("--updated") + 1]

text = open(page, encoding="utf-8").read()
new = open(block, encoding="utf-8").read().rstrip("\n") + "\n"

m = re.match(r"\A---\n.*?\n---\n", text, re.S)
if not m:
    sys.exit(f"{page}: no YAML frontmatter — refusing to guess where to insert")
fm, body = m.group(0), text[m.end():]

if updated:
    fm2, n = re.subn(r"^updated:.*$", f"updated: {updated}", fm, flags=re.M)
    if n != 1:
        sys.exit(f"{page}: expected exactly one `updated:` line, found {n}")
    fm = fm2

open(page, "w", encoding="utf-8").write(fm + "\n" + new + "\n" + body.lstrip("\n"))
print(f"{page}: inserted {len(new)} bytes after frontmatter")
