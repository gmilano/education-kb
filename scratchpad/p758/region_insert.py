import sys, io, json
# region_insert.py <target> <json: {"### North America": "file", ...}>
target = sys.argv[1]
mapping = json.load(io.open(sys.argv[2], encoding='utf-8'))
lines = io.open(target, encoding='utf-8').read().split('\n')
# only operate on headings AFTER '## Opportunities by region' and BEFORE the next '## ' that is not a region
start = next(i for i,l in enumerate(lines) if l.strip() == '## Opportunities by region')
done = {}
out = []
for i, l in enumerate(lines):
    out.append(l)
    if i > start and l.strip() in mapping and l.strip() not in done:
        body = io.open(mapping[l.strip()], encoding='utf-8').read().rstrip('\n')
        out.append('')
        out.extend(body.split('\n'))
        done[l.strip()] = True
io.open(target, 'w', encoding='utf-8').write('\n'.join(out))
print('OK %s: inserted under %d region headings: %s' % (target, len(done), sorted(done)))
