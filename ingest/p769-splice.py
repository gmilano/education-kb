#!/usr/bin/env python3
"""p769 section splicer. Prepends a dated pass section directly after the shelf's
H1 title, preserving YAML frontmatter and the whole history below (append-only)."""
import sys, re, io
shelf, secfile = sys.argv[1], sys.argv[2]
body = open(shelf, encoding='utf-8').read()
new  = open(secfile, encoding='utf-8').read().rstrip() + '\n\n'
lines = body.split('\n')
# frontmatter: lines[0] == '---' .. next '---'
assert lines[0].strip() == '---', shelf + ': no frontmatter'
end = next(i for i in range(1, len(lines)) if lines[i].strip() == '---')
# refresh the updated: field in place
for i in range(1, end):
    if lines[i].startswith('updated:'):
        lines[i] = 'updated: 2026-11-11'
# insertion point: after the first H1 that follows the frontmatter, else right after it
ins = end + 1
for i in range(end + 1, min(end + 8, len(lines))):
    if lines[i].startswith('# '):
        ins = i + 1
        break
while ins < len(lines) and lines[ins].strip() == '':
    ins += 1
out = '\n'.join(lines[:ins]) + '\n\n' + new + '\n'.join(lines[ins:])
open(shelf, 'w', encoding='utf-8').write(out)
print('spliced %-28s +%d lines' % (shelf, new.count('\n')))
