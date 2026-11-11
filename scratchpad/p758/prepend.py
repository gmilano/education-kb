import sys, io
# prepend.py <target> <section-file> <anchor-substring>
# Inserts the section immediately BEFORE the first line containing anchor-substring.
target, sec, anchor = sys.argv[1], sys.argv[2], sys.argv[3]
body = io.open(sec, encoding='utf-8').read()
lines = io.open(target, encoding='utf-8').read().split('\n')
idx = None
for i, l in enumerate(lines):
    if anchor in l:
        idx = i; break
if idx is None:
    raise SystemExit('ANCHOR NOT FOUND in %s: %r' % (target, anchor))
out = '\n'.join(lines[:idx]) + '\n' + body.rstrip('\n') + '\n\n' + '\n'.join(lines[idx:])
io.open(target, 'w', encoding='utf-8').write(out)
print('OK %s: inserted %d bytes before line %d' % (target, len(body), idx+1))
