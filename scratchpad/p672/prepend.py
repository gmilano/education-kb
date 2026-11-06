#!/usr/bin/env python3
"""Append-only prepend: insert a dated section immediately after the YAML
frontmatter, keeping every prior section below it untouched. Verifies the tail
is byte-identical afterwards, so 'append-only' is measured, not asserted."""
import sys, hashlib
path, secfile = sys.argv[1], sys.argv[2]
orig = open(path, encoding="utf-8").read()
sec  = open(secfile, encoding="utf-8").read()
lines = orig.split("\n")
assert lines[0] == "---", "no frontmatter"
end = lines.index("---", 1)
# bump the frontmatter's updated: field
for i in range(1, end):
    if lines[i].startswith("updated:"):
        lines[i] = "updated: 2026-11-05"
head = "\n".join(lines[:end+1])
tail = "\n".join(lines[end+1:])
before = hashlib.sha256(tail.encode()).hexdigest()
new = head + "\n" + sec.rstrip("\n") + "\n" + tail
open(path, "w", encoding="utf-8").write(new)
after_tail = "\n".join(open(path, encoding="utf-8").read().split("\n")[end+1:])
after = hashlib.sha256(after_tail[len(sec.rstrip(chr(10)))+1:].encode()).hexdigest()
print("%-22s prior content sha256 before=%s after=%s %s"
      % (path, before[:12], after[:12], "APPEND-ONLY OK" if before == after else "!! TAIL CHANGED"))
