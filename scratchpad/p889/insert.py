import sys
target, block, mode = sys.argv[1], sys.argv[2], sys.argv[3]
txt = open(target, encoding='utf-8').read()
lines = txt.split('\n')
assert lines[0].strip() == '---', f"{target}: no frontmatter"
fm_end = next(i for i in range(1, len(lines)) if lines[i].strip() == '---')
for i in range(1, fm_end):
    if lines[i].startswith('updated:'):
        lines[i] = 'updated: 2026-11-18'
blk = open(block, encoding='utf-8').read().rstrip('\n').split('\n')
if mode == 'before-first-h2':
    # first '## ' heading strictly after the H1
    h1 = next(i for i in range(fm_end+1, len(lines)) if lines[i].startswith('# '))
    ins = next(i for i in range(h1+1, len(lines)) if lines[i].startswith('## '))
    out = lines[:ins] + blk + [''] + lines[ins:]
else:
    raise SystemExit('bad mode')
open(target, 'w', encoding='utf-8').write('\n'.join(out))
print(f"{target}: +{len(blk)} lines at line {ins+1}")
