#!/usr/bin/env python3
"""p772 — extract every DISPLAYED github address from the live shelves.

Written from scratch for p772. Implements ACTION p771-B's instrument:
  "does the DISPLAYED ADDRESS RESOLVE on the ref channel?"
plus its companion assertion:
  link_text == url_path  for every owner/repo-shaped link text.

Only MARKDOWN LINKS count as displayed addresses. A bare token in prose is
not an address a reader can click, and p770-C/p769-C both show that counting
prose tokens as citations is how a pass invents a defect.
"""
import re, sys, json, collections

LINK = re.compile(r'\[([^\]\n]{0,300}?)\]\(\s*(https?://github\.com/[^\s)]+?)\s*\)')
# owner/repo, stopping before any deeper path component
SLUG = re.compile(r'^https?://github\.com/([A-Za-z0-9][A-Za-z0-9._-]*)/([A-Za-z0-9][A-Za-z0-9._-]*?)(?:\.git)?(?:[/#?].*)?$')
SLUGISH = re.compile(r'^[`*_ ]*([A-Za-z0-9][A-Za-z0-9._-]*)/([A-Za-z0-9][A-Za-z0-9._-]*?)[`*_ ,.]*$')

rows = []
for path in [l.strip() for l in open(sys.argv[1]) if l.strip()]:
    for ln, line in enumerate(open(path, encoding='utf-8'), 1):
        for text, url in LINK.findall(line):
            m = SLUG.match(url)
            if not m:
                rows.append({'file': path, 'line': ln, 'text': text, 'url': url,
                             'owner': None, 'repo': None, 'kind': 'non-slug'})
                continue
            owner, repo = m.group(1), m.group(2)
            # classify the link TEXT: is it owner/repo-shaped (a claim about the address)?
            t = SLUGISH.match(text.strip())
            if t:
                agree = (t.group(1).lower() == owner.lower() and t.group(2).lower() == repo.lower())
                kind = 'slug-text-agrees' if agree else 'slug-text-DISAGREES'
                claimed = f'{t.group(1)}/{t.group(2)}'
            else:
                kind, claimed = 'prose-text', None
            rows.append({'file': path, 'line': ln, 'text': text.strip(), 'url': url,
                         'owner': owner, 'repo': repo, 'slug': f'{owner}/{repo}',
                         'kind': kind, 'claimed': claimed})

json.dump(rows, open(sys.argv[2], 'w'), indent=1)
slugs = sorted({r['slug'] for r in rows if r.get('slug')}, key=str.lower)
owners = sorted({r['owner'].lower() for r in rows if r.get('owner')})
open(sys.argv[3], 'w').write('\n'.join(slugs) + '\n')

print(f'markdown github links found : {len(rows)}')
print(f'distinct owner/repo addresses: {len(slugs)}')
print(f'distinct owners              : {len(owners)}')
kc = collections.Counter(r['kind'] for r in rows)
for k, v in kc.most_common():
    print(f'  {k:22s} {v}')
print()
print('LINK TEXT DISAGREEING WITH URL PATH:')
bad = [r for r in rows if r['kind'] == 'slug-text-DISAGREES']
for r in bad:
    print(f"  {r['file']}:{r['line']}  text={r['claimed']!r}  url={r['owner']}/{r['repo']}")
print(f'  total: {len(bad)}')
print()
print('NON-SLUG github links (not owner/repo addresses):')
for r in rows:
    if r['kind'] == 'non-slug':
        print(f"  {r['file']}:{r['line']}  {r['url']}")
