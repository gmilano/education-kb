import io, sys
KB='/tmp/education-kb/'

def insert_before(target, secfile, anchor):
    body=io.open(secfile,encoding='utf-8').read().rstrip('\n')
    lines=io.open(KB+target,encoding='utf-8').read().split('\n')
    idx=None
    for i,l in enumerate(lines):
        if anchor in l:
            idx=i; break
    if idx is None: raise SystemExit('ANCHOR NOT FOUND in %s: %r' % (target,anchor))
    out='\n'.join(lines[:idx])+'\n'+body+'\n\n'+'\n'.join(lines[idx:])
    io.open(KB+target,'w',encoding='utf-8').write(out)
    print('OK  %-26s inserted %6d B before line %d' % (target,len(body),idx+1))

def insert_after(target, secfile, anchor):
    body=io.open(secfile,encoding='utf-8').read().rstrip('\n')
    lines=io.open(KB+target,encoding='utf-8').read().split('\n')
    idx=None
    for i,l in enumerate(lines):
        if l.strip()==anchor:
            idx=i; break
    if idx is None: raise SystemExit('ANCHOR NOT FOUND in %s: %r' % (target,anchor))
    out='\n'.join(lines[:idx+1])+'\n\n'+body+'\n'+'\n'.join(lines[idx+1:])
    io.open(KB+target,'w',encoding='utf-8').write(out)
    print('OK  %-26s inserted %6d B after  line %d (%s)' % (target,len(body),idx+1,anchor))

P762='## 🆕 `p762`'
insert_before('agents/top.md',        'sec/agents-top.md',      P762)
insert_before('repos/foundations.md', 'sec/repos-found.md',     P762)
insert_before('verticals/solutions.md','sec/verticals.md',      P762)
insert_before('intel/open-gaps.md',  'sec/open-gaps.md',        P762)
insert_before('README.md',           'sec/readme.md',           P762)
insert_before('intel/trends.md',     'sec/trends.md',           '# 🆕 Trends new at `p762`')
insert_before('compose/patterns.md', 'sec/patterns.md',         '## 🆕 `P305`–`P310`')
insert_before('agents/trending.md',  'sec/agents-trending.md',  '## 🆕 2026-11-11 (p762)')
insert_before('repos/trending.md',   'sec/repos-trending.md',   '## 🆕 2026-11-11 (p762)')

# market: five region blocks, each AFTER its ### heading (ACTION p756-C)
for region,sec in [('North America','mkt-na'),('EMEA','mkt-emea'),('APAC','mkt-apac'),
                   ('LATAM','mkt-latam'),('Global','mkt-global')]:
    insert_after('intel/market.md', 'sec/%s.md'%sec, '### '+region)
