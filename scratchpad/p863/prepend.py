import sys
path, blockpath = sys.argv[1], sys.argv[2]
block = open(blockpath, encoding='utf-8').read()
txt = open(path, encoding='utf-8').read()
lines = txt.split('\n')
assert lines[0] == '---', path
end = lines.index('---', 1)
head = '\n'.join(lines[:end+1])
rest = '\n'.join(lines[end+1:])
open(path, 'w', encoding='utf-8').write(head + '\n\n' + block.strip('\n') + '\n\n' + rest.lstrip('\n'))
print("prepended ->", path)
