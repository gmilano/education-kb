#!/usr/bin/env python3
"""Insert a pass block directly after a page's H1 title.

These pages are reverse-chronological: the newest pass sits at the top, under
the title, above the previous pass's block. Doing this by hand is how p122
put `ACTION V` in one record out of three (`P122-F`), so it is a script.

usage: prepend_pass.py [--after-frontmatter] PAGE BLOCK_FILE

🔴 `--after-frontmatter` is required for the APPEND-ONLY trending pages and
exists because of a real misfire: those pages carry no H1 at the top but DO
contain one thousands of lines down in their history, so an H1 search inserted
p124's section at line 7166, in the middle of p60-era content. The insertion
point is not something to infer.
"""
import sys


def main(page, block_file, after_frontmatter=False):
    with open(page, encoding="utf-8") as fh:
        lines = fh.readlines()
    with open(block_file, encoding="utf-8") as fh:
        block = fh.read().rstrip("\n") + "\n\n"

    # The H1 is the first line starting with a single '# '. Frontmatter sits
    # above it and must not move.
    idx = None
    if not after_frontmatter:
        for i, line in enumerate(lines):
            if line.startswith("# "):
                idx = i + 1
                break
    if idx is None:
        # The APPEND-ONLY trending pages carry no H1: their newest dated
        # section sits directly under the frontmatter. Insert there, after the
        # closing `---`, so the frontmatter is never disturbed.
        if lines and lines[0].strip() == "---":
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    idx = i + 1
                    break
    if idx is None:
        raise SystemExit("no H1 and no frontmatter found in %s" % page)
    # Skip the blank line that follows the title, so the block does not weld
    # itself onto the heading.
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1

    out = lines[:idx] + [block] + lines[idx:]
    with open(page, "w", encoding="utf-8") as fh:
        fh.writelines(out)
    print("%s\t+%d lines at %d" % (page, block.count("\n"), idx))


if __name__ == "__main__":
    argv = sys.argv[1:]
    af = "--after-frontmatter" in argv
    rest = [a for a in argv if a != "--after-frontmatter"]
    if len(rest) != 2:
        raise SystemExit(__doc__)
    main(rest[0], rest[1], af)
