#!/usr/bin/env python3
"""Insert a pass section directly after a page's YAML frontmatter, leaving history intact.

🔵 Exists because p191 edited nine pages, and the append-only ones must keep every prior
section BELOW the new one: an insert that misses the frontmatter boundary writes the new
section above the opening `---`, which breaks the compiler's typed-entity read — the exact
failure `P1043`'s frontmatter-coverage gate exists to catch after the fact. Catching it
before the write is cheaper.

    python3 -I prepend_pass.py <page.md> <section.md>
"""
import sys

page, section = sys.argv[1], sys.argv[2]
with open(page, encoding="utf-8") as fh:
    text = fh.read()
with open(section, encoding="utf-8") as fh:
    new = fh.read().rstrip("\n") + "\n\n"

lines = text.split("\n")
if lines[0].strip() != "---":
    sys.exit(f"{page}: no frontmatter opener — refusing to write")
end = next(i for i, l in enumerate(lines[1:], 1) if l.strip() == "---")
for i in range(1, end):
    if lines[i].startswith("updated:"):
        lines[i] = "updated: 2026-10-14"
head = "\n".join(lines[: end + 1])
rest = "\n".join(lines[end + 1:]).lstrip("\n")
with open(page, "w", encoding="utf-8") as fh:
    fh.write(head + "\n" + new + rest)
print(f"{page}: inserted {len(new)} B after frontmatter")
