#!/usr/bin/env python3
"""p830-prepend.py -- insert a pass section directly after a page's YAML frontmatter.

usage: python3 -I ingest/p830-prepend.py TARGET SECTION_FILE
The frontmatter is the first '---' ... '---' block; the section is inserted after it,
leaving the rest of the page (the pass history) untouched. APPEND-ONLY by construction.
"""
import re
import sys

target, section = sys.argv[1], sys.argv[2]
body = open(target, encoding="utf-8").read()
new = open(section, encoding="utf-8").read()
if not body.startswith("---\n"):
    sys.exit("RED: %s has no frontmatter; refusing to touch it" % target)
end = body.index("\n---\n", 4) + len("\n---\n")
# p830: insert BELOW the page's H1 title when it has one, so the title stays at the top and
# only the pass history is pushed down. Inserting above it buried the title under the newest
# pass and made the page open on a paragraph instead of a name.
rest = body[end:]
m = re.match(r"\s*\n(# [^\n]*\n)", rest)
if m:
    end += m.end()
out = body[:end] + "\n" + new.rstrip("\n") + "\n" + body[end:]
open(target, "w", encoding="utf-8").write(out)
print("OK prepended %d bytes into %s" % (len(new), target))
