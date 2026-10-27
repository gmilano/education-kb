import io, re, subprocess, sys
REPO='/tmp/education-kb'
SHELVES=['agents/top.md','agents/trending.md','repos/foundations.md','repos/trending.md',
         'verticals/solutions.md','intel/market.md','intel/trends.md','compose/patterns.md',
         'intel/open-gaps.md']
REGIONS={'North America','EMEA','APAC','LATAM','Global'}
HEADERISH=re.compile(r'^\|\s*(nombre|name|repo|agent|licencia|license|licence|platform|component|instrument|gap|figure|measure|signal|pass|role|what|observation|defect|probe|tier|grant class)\s*\|', re.I)
fails=[]

print("== 1. frontmatter keys + closed-vocabulary region ==")
for s in SHELVES:
    t=io.open(REPO+'/'+s,encoding='utf-8').read().split('\n')
    assert t[0]=='---'; e=t.index('---',1)
    fm=dict(l.split(': ',1) for l in t[1:e] if ': ' in l)
    ok = fm.get('industry')=='education' and fm.get('region') in REGIONS and fm.get('updated')=='2026-10-27'
    print(("  OK   " if ok else "  FAIL ")+"%-26s industry=%s region=%s updated=%s"%(s.split('/')[-1],fm.get('industry'),fm.get('region'),fm.get('updated')))
    if not ok: fails.append('frontmatter '+s)

print("== 2. p473 tables: separator present, pipe count consistent, no header row as data ==")
tot_tables=tot_rows=0
for s in SHELVES:
    body=io.open(REPO+'/'+s,encoding='utf-8').read()
    # p473 section = from its header to the next '## ' at col 0
    m=re.search(r'^## .*?`p473`.*?$', body, re.M)
    if not m: fails.append('no p473 section '+s); continue
    nxt=re.search(r'^## (?!.*`p473`)', body[m.end():], re.M)
    sec=body[m.end(): m.end()+(nxt.start() if nxt else len(body))]
    lines=sec.split('\n'); i=0
    while i < len(lines):
        if lines[i].startswith('|'):
            block=[]
            while i<len(lines) and lines[i].startswith('|'): block.append(lines[i]); i+=1
            tot_tables+=1; tot_rows+=len(block)-2
            if len(block)<2 or not re.match(r'^\|[\s\-:|]+\|$', block[1]):
                fails.append('%s: table missing separator near %r'%(s,block[0][:50]))
            widths={l.count('|') for l in block}
            if len(widths)!=1:
                fails.append('%s: pipe-count mismatch %s near %r'%(s,sorted(widths),block[0][:50]))
            for row in block[2:]:
                if HEADERISH.match(row):
                    fails.append('%s: HEADER ROW PUBLISHED AS DATA: %r'%(s,row[:70]))
        else: i+=1
print("  %d tables, %d data rows across 9 shelves" % (tot_tables, tot_rows))

print("== 3. append-only containment on the two trending shelves, vs git HEAD ==")
for s in ['agents/trending.md','repos/trending.md']:
    old=subprocess.run(['git','-C',REPO,'show','HEAD:'+s],capture_output=True,text=True).stdout
    new=io.open(REPO+'/'+s,encoding='utf-8').read()
    oldbody=old.split('---',2)[2].lstrip('\n')
    ok = oldbody in new
    print(("  OK   " if ok else "  FAIL ")+"%-22s prior body contained verbatim: %s (old %d B -> new %d B)"%(s,ok,len(old),len(new)))
    if not ok: fails.append('append-only '+s)

print("== 4. single canonical Opportunities block with 5 region children ==")
mk=io.open(REPO+'/intel/market.md',encoding='utf-8').read()
bare=len(re.findall(r'^## Opportunities by region$', mk, re.M))
blk=mk.split('\n## Opportunities by region\n',1)[1]
blk=blk.split('\n## ',1)[0]
kids=re.findall(r'^### (.+)$', blk, re.M)
ok = bare==1 and set(kids)==REGIONS
print(("  OK   " if ok else "  FAIL ")+"bare canonical blocks=%d, children=%s"%(bare,kids))
if not ok: fails.append('canonical block')

print("== 5. every sha256-12 printed on a shelf is in the evidence ledger ==")
led=io.open(REPO+'/evidence/grant-class.2026-10-27-p473.tsv',encoding='utf-8').read()
extra=io.open(REPO+'/evidence/p473-address-resolution.tsv',encoding='utf-8').read()
printed=set()
for s in SHELVES:
    body=io.open(REPO+'/'+s,encoding='utf-8').read()
    m=re.search(r'^## .*?`p473`.*?$', body, re.M)
    nxt=re.search(r'^## (?!.*`p473`)', body[m.end():], re.M)
    sec=body[m.end(): m.end()+(nxt.start() if nxt else len(body))]
    printed |= set(re.findall(r'`([0-9a-f]{12})`', sec))
missing=sorted(d for d in printed if d not in led and d not in extra)
print("  %d distinct 12-hex values printed; %d not in evidence" % (len(printed), len(missing)))
if missing: print("   MISSING:", missing); fails.append('digest traceability')

print("\n== RESULT: %s ==" % ("ALL CHECKS GREEN" if not fails else "%d FINDINGS"%len(fails)))
for f in fails: print("  -", f)
