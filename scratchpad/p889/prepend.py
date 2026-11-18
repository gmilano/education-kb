import sys
target, block, lead = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(target, encoding='utf-8').read().split('\n')
# locate end of YAML frontmatter
assert lines[0].strip() == '---', f"{target}: no frontmatter"
end = next(i for i in range(1, len(lines)) if lines[i].strip() == '---')
# refresh updated: field
for i in range(1, end):
    if lines[i].startswith('updated:'):
        lines[i] = 'updated: 2026-11-18'
blk = open(block, encoding='utf-8').read().rstrip('\n')
if lead:
    blk = blk.replace('\n\n', '\n\n' + lead + '\n\n', 1)
out = lines[:end+1] + ['', blk, ''] + lines[end+1:]
open(target, 'w', encoding='utf-8').write('\n'.join(out))
print(f"{target}: inserted {blk.count(chr(10))+1} lines after frontmatter line {end+1}")
