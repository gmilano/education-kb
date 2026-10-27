import sys, io, re, datetime
target, block = sys.argv[1], sys.argv[2]
body = io.open(target, encoding='utf-8').read()
new = io.open(block, encoding='utf-8').read().rstrip('\n') + '\n\n'
lines = body.split('\n')
assert lines[0] == '---', target
end = lines.index('---', 1)
fm = lines[:end+1]
fm = [re.sub(r'^updated: .*$', 'updated: 2026-10-27', l) for l in fm]
rest = '\n'.join(lines[end+1:]).lstrip('\n')
out = '\n'.join(fm) + '\n\n' + new + rest
io.open(target, 'w', encoding='utf-8').write(out)
print("%-32s prior_body_preserved=%s  +%d bytes" % (target.split('/')[-1], rest in out, len(out)-len(body)))
