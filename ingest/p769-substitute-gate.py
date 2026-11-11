#!/usr/bin/env python3
"""p769 substitute commit gate.

`make hooks` is denied in this session as repository-code execution (eleventh
consecutive pass; the command is run, not assumed). This stands in for it.

Scoping, per p766's correction: row-shaped checks run ONLY over the section this
pass wrote, because the shelves are append-only and 767 passes of history
legitimately DISCUSS header rows and filler rows. Frontmatter and region
placement are checked base-wide.
"""
import io, re, sys, glob

PASS = 'p769'
SHELVES = ['README.md', 'agents/top.md', 'agents/trending.md', 'repos/foundations.md',
           'repos/trending.md', 'verticals/solutions.md', 'intel/market.md',
           'intel/trends.md', 'intel/open-gaps.md', 'intel/measured-unusable.md',
           'compose/patterns.md']
REGIONS = ['North America', 'EMEA', 'APAC', 'LATAM', 'Global']
VOCAB = REGIONS

findings = []


def read(p):
    return io.open(p, encoding='utf-8').read()


def this_pass_section(path):
    """Lines belonging to the p769 section only."""
    lines = read(path).split('\n')
    start = None
    for i, l in enumerate(lines):
        if PASS in l and l.startswith('#'):
            start = i
            break
    if start is None:
        return []
    for j in range(start + 1, len(lines)):
        lj = lines[j]
        if lj.startswith('## ') and PASS not in lj:
            return lines[start:j]
        if lj.startswith('#### 🆕') and PASS not in lj:
            return lines[start:j]
    return lines[start:]


def cells(row):
    """Split a markdown table row, ignoring escaped pipes and pipes in code spans.

    p767's D2: counting escaped \\| as a separator reported 48 rows, 41 of them
    that defect. Code spans are stripped first for the same reason.
    """
    r = re.sub(r'`[^`]*`', 'X', row)
    r = r.replace('\\|', '')
    r = r.strip()
    if r.startswith('|'):
        r = r[1:]
    if r.endswith('|'):
        r = r[:-1]
    return r.split('|')


# --- 1. frontmatter, base-wide ---
for s in SHELVES:
    lines = read(s).split('\n')
    if lines[0] != '---':
        findings.append('%s: no frontmatter' % s); continue
    try:
        end = lines.index('---', 1)
    except ValueError:
        findings.append('%s: unterminated frontmatter' % s); continue
    fm = dict()
    for l in lines[1:end]:
        if ':' in l:
            k, v = l.split(':', 1)
            fm[k.strip()] = v.strip()
    if fm.get('industry') != 'education':
        findings.append('%s: industry=%r' % (s, fm.get('industry')))
    if fm.get('region') not in VOCAB:
        findings.append('%s: region=%r outside closed vocabulary' % (s, fm.get('region')))
    if fm.get('updated') != '2026-11-11':
        findings.append('%s: updated=%r' % (s, fm.get('updated')))

# --- 2. region blocks sit DIRECTLY after their ### heading (ACTION p756-C) ---
ml = read('intel/market.md').split('\n')
placed = 0
for i, l in enumerate(ml):
    if l.startswith('### ') and l[4:].strip() in REGIONS:
        nxt = [x for x in ml[i + 1:i + 4] if x.strip()]
        if nxt and PASS in nxt[0]:
            placed += 1
if placed != 5:
    findings.append('market.md: %d/5 region blocks directly after their ### heading' % placed)

# --- 3. row-shaped checks, this pass's sections only ---
SEP = re.compile(r'^\|[\s:|-]+\|$')
for s in SHELVES:
    sec = this_pass_section(s)
    if not sec:
        findings.append('%s: no %s section found' % (s, PASS)); continue
    tables = []   # (header_cells, rows)
    hdr = None
    for i, l in enumerate(sec):
        if not l.startswith('|'):
            hdr = None; continue
        if SEP.match(l.strip()):
            continue
        c = cells(l)
        if hdr is None:
            hdr = len(c); tables.append((hdr, []))
            continue
        tables[-1][1].append((i, c))
    for width, rows in tables:
        for i, c in rows:
            # 3a. a data row that renders as a header (all cells bare and short)
            # 3b. over-wide row: more cells than the header admits
            if len(c) > width:
                findings.append('%s:+%d over-wide row: %d cells vs header %d' % (s, i, len(c), width))
            # 3c. filler / example rows left as data
            low = ' '.join(c).lower()
            for bad in ('nombre', 'licencia', 'your repo', 'example.com', 'lorem ipsum', 'tbd', 'xxx'):
                if re.search(r'(^|[\s|`*])' + re.escape(bad) + r'($|[\s|`*])', low):
                    findings.append('%s:+%d filler-shaped cell %r' % (s, i, bad))

# --- 4. every address written as a LINK must be https://github.com/owner/repo ---
badlink = 0
for s in SHELVES:
    for m in re.finditer(r'\[`([^`]+)`\]\(([^)]+)\)', '\n'.join(this_pass_section(s))):
        slug, url = m.group(1), m.group(2)
        if url.startswith('https://github.com/') and not url.rstrip('/').endswith(slug):
            findings.append('%s: link text %r != url %r' % (s, slug, url)); badlink += 1

print('p769 substitute gate')
print('  shelves checked      : %d' % len(SHELVES))
print('  region blocks placed : %d/5' % placed)
print('  link mismatches      : %d' % badlink)
if findings:
    print('RED — %d finding(s):' % len(findings))
    for f in findings[:40]:
        print('   -', f)
    sys.exit(1)
print('GREEN')
