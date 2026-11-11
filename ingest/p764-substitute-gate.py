import os, re, sys, glob
ROOT = '/tmp/education-kb'
SHELVES = ['agents/top.md','agents/trending.md','repos/foundations.md','repos/trending.md',
           'verticals/solutions.md','intel/market.md','intel/trends.md','compose/patterns.md',
           'intel/open-gaps.md','intel/measured-unusable.md','README.md']
REGIONS = {'North America','EMEA','APAC','LATAM','Global'}
HEADERISH = {'nombre','name','repo','repository','licencia','license','licence','descripcion',
             'descripción','description','stars','agent','platform','item','role','grant','branch',
             'probe','topic','source','claim','component','channel','instrument','figure','verdict',
             'reading','state','buyer','pattern','region','indicator','line','share of schools'}
# A cell that IS a placeholder, not prose that mentions one. p764: the naive
# substring form produced 60+ false positives because this base documents the defect.
PLACE_CELL = re.compile(r'^(TBD|TODO|FIXME|XXX+|N/?A|placeholder|lorem ipsum|example|example\.com|your-org|owner/repo|owner/name|a/b|O/R|\.\.\.|\?+|-{1,3})$', re.I)
fails, tables, rows = [], 0, 0
for rel in SHELVES:
    p = os.path.join(ROOT, rel)
    txt = open(p, encoding='utf-8').read()
    lines = txt.split('\n')
    # frontmatter
    if lines[0] != '---': fails.append(f'{rel}: no frontmatter')
    else:
        end = next((i for i,l in enumerate(lines[1:],1) if l=='---'), None)
        fm = dict()
        for l in lines[1:end]:
            if ':' in l: k,v = l.split(':',1); fm[k.strip()] = v.strip()
        for k in ('industry','region','updated'):
            if k not in fm: fails.append(f'{rel}: frontmatter missing {k}')
        if fm.get('industry') != 'education': fails.append(f'{rel}: industry={fm.get("industry")}')
        if fm.get('region') not in REGIONS: fails.append(f'{rel}: region not in closed vocab: {fm.get("region")!r}')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', fm.get('updated','')): fails.append(f'{rel}: updated malformed')
    # tables
    i = 0
    while i < len(lines):
        if lines[i].startswith('|') and i+1 < len(lines) and re.fullmatch(r'\|[\s:|-]+\|', lines[i+1].strip()):
            tables += 1
            j = i+2
            while j < len(lines) and lines[j].startswith('|'):
                rows += 1
                cells = [c.strip().strip('`*_ ') for c in lines[j].strip().strip('|').split('|')]
                low = [c.lower() for c in cells if c]
                if len(low) >= 2 and all(c in HEADERISH for c in low):
                    fails.append(f'{rel}:{j+1}: data row renders as a table header: {lines[j][:80]}')
                if re.fullmatch(r'\|[\s:|-]+\|', lines[j].strip()):
                    fails.append(f'{rel}:{j+1}: separator as data row')
                ph = [c for c in cells if PLACE_CELL.fullmatch(c)]
                if ph and len(ph) == len([c for c in cells if c]):
                    fails.append(f'{rel}:{j+1}: every cell is a placeholder: {lines[j][:80]}')
                j += 1
            i = j
        else:
            i += 1
# region blocks must follow their ### heading inside Opportunities by region
mkt = open(os.path.join(ROOT,'intel/market.md'), encoding='utf-8').read().split('\n')
inside, seen = False, {}
for idx,l in enumerate(mkt):
    if l.strip() == '## Opportunities by region': inside = True; continue
    m = re.fullmatch(r'### (North America|EMEA|APAC|LATAM|Global)\s*', l)
    if inside and m and m.group(1) not in seen:
        reg = m.group(1); seen[reg] = False
        for k in range(idx+1, min(idx+6, len(mkt))):
            if mkt[k].startswith('#### 🆕 p764'): seen[reg] = True; break
            if mkt[k].startswith('### '): break
for reg in REGIONS:
    if not seen.get(reg): fails.append(f'market.md: p764 block not directly under ### {reg}')
print(f'tables={tables} data_rows={rows} shelves={len(SHELVES)} region_blocks_ok={sum(1 for v in seen.values() if v)}/5')
if fails:
    print('FAIL:'); [print('  '+f) for f in fails[:40]]; sys.exit(1)
print('GREEN: 0 header-as-data rows, 0 separator rows, 0 placeholder rows, frontmatter valid on all shelves, 5/5 region blocks placed')
