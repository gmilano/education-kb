#!/usr/bin/env python3
"""p861 -- prepend a pass block directly beneath a file's YAML frontmatter and re-date it.

Every curated page in this base carries a 5-line frontmatter block whose `updated:` field is
read by the compiler.  A pass that prepends by hand has twice written the block ABOVE the
frontmatter, which makes the file's region and date invisible to the compiler.  This does it
once, the same way, for every file.

    python3 -I ingest/p861-prepend.py <target.md> <block.md> <YYYY-MM-DD>
"""
import sys

def main(target, block, date):
    lines = open(target, encoding="utf-8").read().split("\n")
    if lines[0].strip() != "---":
        raise SystemExit("%s: no frontmatter" % target)
    end = next(i for i, l in enumerate(lines[1:], 1) if l.strip() == "---")
    for i in range(1, end):
        if lines[i].startswith("updated:"):
            lines[i] = "updated: %s" % date
    body = open(block, encoding="utf-8").read().rstrip("\n")
    out = lines[:end + 1] + ["", body, ""] + lines[end + 1:]
    open(target, "w", encoding="utf-8").write("\n".join(out))
    print("prepended %d lines into %s" % (len(body.split(chr(10))), target))

if __name__ == "__main__":
    main(*sys.argv[1:4])
