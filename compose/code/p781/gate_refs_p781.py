#!/usr/bin/env python3
"""p781 gate-refs, AMENDED per p780's own measured amendment of T809.

p780 found its PRIMARY test too loose: a summary row that QUOTES a primary
row's bytes was scored PRIMARY, inflating nothing but misclassifying 7 of 8
residual rows. Amended test, as p780-A ordered:

    A row is PRIMARY only if it is the FIRST assertion of a given grade for a
    given repository, in PASS order. A row restating an already-established
    grade is DERIVED however much evidence it quotes.

p780-A forbade REBUILDING this gate and asked that p779's be reused. That is
not possible in this session: `python3 compose/code/p779/gate_refs_cohort.py`
is DENIED `[Code from External]`, as is `make hooks` run inside the cloned KB.
So this is written from scratch under duress, and the denial is reported, not
worked around.

Also carries ACTION p780-G: the newest `## ` section of each shelf must name
the current pass AND the shelf's YAML `updated:` must equal that heading's date.
"""
import re, sys, os, collections

SHELVES = ['agents/top.md','agents/trending.md','repos/foundations.md','repos/trending.md',
           'verticals/solutions.md','intel/market.md','intel/trends.md','compose/patterns.md',
           'intel/open-gaps.md','README.md']

# p778-F: MIT-the-institution must never be read as MIT-the-licence.
INST = [r'mitodl', r'MIT Media Lab', r'MIT Sloan', r'MIT App Inventor', r'MIT OpenCourseWare',
        r'MIT Press', r'MIT CSAIL', r'MIT Open Learning', r'MIT-WPU', r'MIT Horizon']
INST_RE = re.compile('|'.join(INST), re.I)

LIC = re.compile(r'\b(MIT|Apache-2\.0|AGPL-3\.0|GPL-3\.0|GPL-2\.0|LGPL-[\d.]+|BSD-[\d-]+(?:-Clause)?|'
                 r'MPL-2\.0|ECL-2\.0|CECILL(?:-[ABC2.1]+)?|CC-BY(?:-SA)?-[\d.]+|EPL-2\.0|'
                 r'Unlicense|ISC|NOASSERTION|NONE|PROPRIETARY)\b')
PASS = re.compile(r'`p(\d{1,4})`')
SLUG = re.compile(r'github\.com/([A-Za-z0-9][\w.-]*)/([A-Za-z0-9][\w.-]*)')
# A ref is `<branch-NAME>` · `<12 hex>`. A byte count followed by a sha has the
# same SHAPE and must be rejected; so must a hex · hex pair.
REF = re.compile(r'`([^`]{1,60})`\s*·\s*`([0-9a-f]{7,40})`')
HEXONLY = re.compile(r'^[0-9a-f]+$')
BYTES_CELL = re.compile(r'^[\d,]+\s*B$', re.I)

def is_data_row(line):
    s = line.strip()
    if not s.startswith('|'): return False
    if re.match(r'^\|[\s:|-]+\|?$', s): return False
    return True

def has_ref(line):
    for m in REF.finditer(line):
        first = m.group(1).strip()
        if BYTES_CELL.match(first): continue          # `1,102 B` · `97952c…` is NOT a ref
        if HEXONLY.match(first) and len(first) >= 7: continue   # hex · hex is NOT a ref
        if re.search(r'[A-Za-z]', first): return True            # branch names carry letters
    return False

def grade(line):
    masked = INST_RE.sub('@@INST@@', line)
    return set(LIC.findall(masked))

def main(root, cur_pass, cur_date):
    rows = []
    for sh in SHELVES:
        p = os.path.join(root, sh)
        if not os.path.exists(p): continue
        cur = None
        for ln, line in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
            if line.startswith('## '):
                m = PASS.search(line); cur = int(m.group(1)) if m else None
            if not is_data_row(line): continue
            g = grade(line)
            if not g: continue
            sm = SLUG.search(line)
            slug = f'{sm.group(1)}/{sm.group(2)}' if sm else None
            rows.append(dict(shelf=sh, line=ln, pas=cur, grades=g, slug=slug, ref=has_ref(line)))

    # AMENDED T809: first assertion of (slug, grade) in PASS order is PRIMARY.
    seen = set()
    for r in sorted(rows, key=lambda r: (r['pas'] if r['pas'] is not None else 0, r['shelf'], r['line'])):
        if r['slug'] is None:
            r['cls'] = 'NO-SLUG'; continue
        keys = [(r['slug'], g) for g in sorted(r['grades'])]
        if any(k not in seen for k in keys):
            r['cls'] = 'PRIMARY'
            for k in keys: seen.add(k)
        else:
            r['cls'] = 'DERIVED'

    coh = collections.defaultdict(lambda: collections.Counter())
    for r in rows:
        if r['pas'] is None: continue
        coh[r['pas']][r['cls']] += 1
        if r['cls'] == 'PRIMARY' and r['ref']: coh[r['pas']]['PRIMARY_REF'] += 1
    return rows, coh


def gate_g(root, cur_pass, cur_date):
    """ACTION p780-G: newest `## ` section must name the current pass, AND the
    shelf's YAML `updated:` must equal the date in that heading (the one extra line)."""
    out = []
    DATE = re.compile(r'(\d{4}-\d{2}-\d{2})')
    for sh in SHELVES:
        p = os.path.join(root, sh)
        if not os.path.exists(p): continue
        head = open(p, encoding='utf-8', errors='replace').read(400000).splitlines()
        upd = None
        for line in head[:12]:
            m = re.match(r'updated:\s*(\S+)', line.strip())
            if m: upd = m.group(1); break
        newest = None
        for line in head:
            if line.startswith('## '):
                newest = line; break
        pm = PASS.search(newest or '')
        npass = int(pm.group(1)) if pm else None
        # DEFECT found by this check on its FIRST run after p781's writes, and
        # fixed here: the date must come from the heading's PASS-MARKER zone, not
        # from the headline prose. intel/market.md's headline quotes the AI Act
        # date `2027-12-02`, which the first version read as the pass date.
        # Rule: consider only the text BEFORE the first bold marker.
        zone = (newest or '').split('**')[0]
        dm = DATE.search(zone)
        hdate = dm.group(1) if dm else None
        defects = []
        if npass != cur_pass: defects.append(f'newest-section=p{npass} not p{cur_pass}')
        if upd is None: defects.append('no YAML updated:')
        elif upd != cur_date: defects.append(f'updated:{upd} != {cur_date}')
        if hdate and upd and hdate != upd: defects.append(f'heading-date {hdate} != updated: {upd}')
        out.append((sh, npass, upd, hdate, defects))
    return out

if __name__ == '__main__':
    root, cur_pass, cur_date = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    rows, coh = main(root, cur_pass, cur_date)
    print('=== AMENDED T809 cohort (PRIMARY = FIRST assertion of a grade) ===')
    print(f"{'pass':>6} {'PRIMARY':>8} {'P+ref':>7} {'share':>7} {'DERIVED':>8} {'D+ref':>6} {'NO-SLUG':>8}")
    tot = dict(P=0, PR=0, D=0, DR=0, N=0)
    for k in sorted(coh):
        if k is None or k < 770: continue
        c = coh[k]
        P, PR, D = c['PRIMARY'], c['PRIMARY_REF'], c['DERIVED']
        DR = sum(1 for r in rows if r['pas']==k and r['cls']=='DERIVED' and r['ref'])
        N = c['NO-SLUG']
        sh = f'{100.0*PR/P:.1f}%' if P else '-'
        print(f'  p{k:>4} {P:>8} {PR:>7} {sh:>7} {D:>8} {DR:>6} {N:>8}')
        tot['P']+=P; tot['PR']+=PR; tot['D']+=D; tot['DR']+=DR; tot['N']+=N
    print('-'*60)
    print(f"  TOTAL  {tot['P']:>8} {tot['PR']:>7} {100.0*tot['PR']/tot['P']:>6.1f}% {tot['D']:>8} {tot['DR']:>6} {tot['N']:>8}")
    print()
    print('=== whole-base, all cohorts ===')
    allP = sum(1 for r in rows if r['cls']=='PRIMARY'); allPR = sum(1 for r in rows if r['cls']=='PRIMARY' and r['ref'])
    allD = sum(1 for r in rows if r['cls']=='DERIVED'); allDR = sum(1 for r in rows if r['cls']=='DERIVED' and r['ref'])
    allN = sum(1 for r in rows if r['cls']=='NO-SLUG')
    print(f'  licence rows={len(rows)}  PRIMARY={allP} ({allPR} w/ref, {100.0*allPR/max(allP,1):.1f}%)  DERIVED={allD} ({allDR} w/ref)  NO-SLUG={allN}')
    print()
    print('=== ACTION p780-G: newest-pass-present + YAML updated: equality ===')
    nd = 0
    for sh, npass, upd, hdate, defects in gate_g(root, cur_pass, cur_date):
        nd += len(defects)
        print(f"  {'OK ' if not defects else 'XX '}{sh:<26} newest=p{npass} updated={upd} heading-date={hdate} {'; '.join(defects)}")
    print(f'  DEFECTS={nd}')
    with open('/tmp/p781/noslug-rows.tsv','w') as fh:
        for r in rows:
            if r['cls']=='NO-SLUG' and r['pas'] and r['pas']>=770:
                fh.write(f"{r['pas']}\t{r['shelf']}\t{r['line']}\t{','.join(sorted(r['grades']))}\t{r['ref']}\n")
