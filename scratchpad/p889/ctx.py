import subprocess,re
cands=['ShravaC/FRIA-O','tjf-trojer/fria-editor','Christospsa/ai-act-ontology-compliance-framework','Siva-Kandula/ai-governance-toolkit-','Ankit-Uniyal/eu-ai-act-compliance-toolkit','jessicavittorio-law/ai-governance-toolkit']
t=re.compile(r'(education|educational|school|student|university|pupil)',re.I)
for s in cands:
    body=None
    for br in ('main','master'):
        r=subprocess.run(['curl','-sL','-w','\n%{http_code}',f"https://raw.githubusercontent.com/{s}/{br}/README.md"],capture_output=True,text=True)
        b,_,c=r.stdout.rpartition('\n')
        if c.strip()=='200' and b.strip(): body=b; break
    print('='*4, s)
    if not body: print('  NOFILE'); continue
    for ln in body.splitlines():
        if t.search(ln): print('   |', ln.strip()[:190])
