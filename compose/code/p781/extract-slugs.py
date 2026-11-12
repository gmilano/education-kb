import re, sys, glob, os
# p781 slug census: every DISTINCT github.com/<owner>/<repo> slug this base DISPLAYS.
pat = re.compile(r'github\.com/([A-Za-z0-9][A-Za-z0-9._-]*)/([A-Za-z0-9][A-Za-z0-9._-]*)')
BAD_OWNER = {'topics','trending','features','about','pricing','marketplace','apps','sponsors','orgs','settings','login','collections','readme'}
files = ['agents/top.md','agents/trending.md','repos/foundations.md','repos/trending.md',
         'verticals/solutions.md','intel/market.md','intel/trends.md','compose/patterns.md',
         'intel/open-gaps.md','README.md']
counts = {}
where = {}
for f in files:
    if not os.path.exists(f): continue
    txt = open(f, encoding='utf-8', errors='replace').read()
    for m in pat.finditer(txt):
        o, r = m.group(1), m.group(2)
        if o.lower() in BAD_OWNER: continue
        r = re.sub(r'\.git$', '', r)
        # strip trailing punctuation artefacts
        r = r.rstrip('.')
        if not r: continue
        slug = f'{o}/{r}'
        counts[slug] = counts.get(slug, 0) + 1
        where.setdefault(slug, set()).add(f)
print(f'DISTINCT_SLUGS\t{len(counts)}')
print(f'TOTAL_CITATIONS\t{sum(counts.values())}')
with open('/tmp/p781/slugs.tsv','w') as fh:
    for slug, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        fh.write(f'{slug}\t{n}\t{",".join(sorted(where[slug]))}\n')
print('TOP_20:')
for slug, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:20]:
    print(f'  {n}\t{slug}')
