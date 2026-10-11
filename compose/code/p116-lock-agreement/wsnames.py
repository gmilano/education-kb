#!/usr/bin/env python3
"""wsnames.py -- the `name` of every package.json in a tree except the root's.

Reads a `git cat-file --batch` stream on stdin and prints one name per line.
ONE process for the whole tree: the first draft of this instrument spawned a
python per sub-manifest, and canvas-lms's 596 of them made the census
unrunnable -- 3 rows in four minutes (P116-O). Invoked with `-I` and handed no
path from the tree, so nothing in a fetched repository can be imported by the
code that reads it.

A workspace-local dependency is defined as one whose name is the `name` of
another package.json IN THIS TREE (P116-L). That is read here rather than
glob-matched against the root manifest's `workspaces` field, because the globs
are not required to be accurate and the names are.
"""
import sys, json


def main():
    b = sys.stdin.buffer
    out = set()
    while True:
        hdr = b.readline()
        if not hdr:
            break
        parts = hdr.split()
        if len(parts) < 3:
            continue
        try:
            size = int(parts[2])
        except ValueError:
            continue
        body = b.read(size)
        b.read(1)                     # the newline git writes after each blob
        try:
            d = json.loads(body.decode('utf-8', 'replace') or '{}')
            n = d.get('name')
            if isinstance(n, str) and n.strip():
                out.add(n.strip())
        except Exception:
            pass
    for n in sorted(out):
        print(n)
    return 0


if __name__ == '__main__':
    sys.exit(main())
