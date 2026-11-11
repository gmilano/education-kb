# p763 self-contained commit gate (written for this pass; not repository code)
import io,re,sys
KB='/tmp/education-kb/'
SHELVES=['agents/top.md','agents/trending.md','repos/foundations.md','repos/trending.md',
         'verticals/solutions.md','intel/market.md','intel/trends.md','compose/patterns.md',
         'intel/open-gaps.md']
REGIONS={'North America','EMEA','APAC','LATAM','Global'}
GENERIC={'nombre','name','repo','repositorio','licencia','license','licence','descripcion',
         'descripción','description','agent','agente','stars','estrellas','url','link','tbd',
         'todo','xxx','placeholder','ejemplo','example','foo','bar','n/a','...','—','-'}
fail=[]; tables=0; rows=0; hdrish=0; ph=0
for f in SHELVES:
    txt=io.open(KB+f,encoding='utf-8').read()
    L=txt.split('\n')
    # frontmatter
    if L[0].strip()!='---': fail.append('%s: no frontmatter open'%f)
    try: end=L[1:].index('---')+1
    except ValueError: fail.append('%s: no frontmatter close'%f); end=0
    fm='\n'.join(L[1:end])
    if 'industry: education' not in fm: fail.append('%s: industry'%f)
    m=re.search(r'^region:\s*(.+)$',fm,re.M)
    if not m: fail.append('%s: no region'%f)
    else:
        vals=[v.strip() for v in m.group(1).split('|')]
        bad=[v for v in vals if v not in REGIONS]
        if bad: fail.append('%s: region vocabulary %r'%(f,bad))
    if not re.search(r'^updated:\s*2026-11-11\s*$',fm,re.M): fail.append('%s: updated != 2026-11-11'%f)
    # tables
    insep=False
    for i,l in enumerate(L):
        if re.match(r'^\|[\s:\-|]+\|\s*$',l.strip()):
            tables+=1; insep=True; continue
        if insep:
            if l.strip().startswith('|'):
                rows+=1
                cells=[c.strip().strip('*`').strip().lower() for c in l.strip().strip('|').split('|')]
                nonempty=[c for c in cells if c]
                if nonempty and all(c in GENERIC for c in nonempty):
                    hdrish+=1; fail.append('%s:%d HEADER-AS-DATA: %s'%(f,i+1,l.strip()[:80]))
                for c in cells:
                    if c in ('tbd','todo','xxx','placeholder','...'):
                        ph+=1; fail.append('%s:%d PLACEHOLDER: %s'%(f,i+1,l.strip()[:80]))
            else:
                insep=False
# region block placement in market.md (ACTION p756-C): p763 block must come AFTER its ### heading
mk=io.open(KB+'intel/market.md',encoding='utf-8').read().split('\n')
placed=0
for r in REGIONS:
    for i,l in enumerate(mk):
        if l.strip()=='### '+r:
            nxt=[x for x in mk[i+1:i+4] if x.strip()]
            if nxt and 'p763' in nxt[0]: placed+=1
            else: fail.append('market.md: p763 block not immediately after ### %s'%r)
            break
print('tables checked      :',tables)
print('data rows checked   :',rows)
print('header-as-data rows :',hdrish)
print('placeholder rows    :',ph)
print('region blocks placed: %d / 5'%placed)
print('frontmatter shelves : %d'%len(SHELVES))
print()
if fail:
    print('FAILURES (%d):'%len(fail))
    for x in fail[:40]: print('  -',x)
    sys.exit(1)
print('GATE GREEN')
