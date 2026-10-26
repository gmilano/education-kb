import os,re,sys
R=sys.argv[1]
dec=re.compile(r'@mcp\.tool(\((?:[^()]|\([^()]*\))*\))?\s*((?:@[\w.]+(?:\([^)]*\))?\s*)*)(?:async\s+)?def\s+([a-zA-Z_]\w*)')
ro=0;rw=0;un=0;names={'ro':[],'rw':[],'un':[]}
for dp,dn,fn in os.walk(R):
    dn[:]=[x for x in dn if x not in ('.git','node_modules','tests','test')]
    for f in fn:
        if not f.endswith('.py') or '.test.' in f: continue
        t=open(os.path.join(dp,f),encoding='utf-8',errors='ignore').read()
        for args,_mid,name in dec.findall(t):
            if 'read_only_hint=True' in (args or ''): ro+=1; names['ro'].append(name)
            elif 'read_only_hint=False' in (args or ''): rw+=1; names['rw'].append(name)
            else: un+=1; names['un'].append(name)
tot=ro+rw+un
print(f"vishalsachdev/canvas-mcp — tools extracted: {tot}")
print(f"  self-declared read_only_hint=True  : {ro}  ({100*ro/tot:.1f}%)")
print(f"  self-declared read_only_hint=False : {rw}  ({100*rw/tot:.1f}%)")
print(f"  no read_only_hint declared         : {un}  ({100*un/tot:.1f}%)")
print()
print("  WRITE-declared (read_only_hint=False):")
print("   ", ', '.join(sorted(names['rw'])) or '(none)')
print()
print("  undeclared sample:", ', '.join(sorted(names['un'])[:14]) or '(none)')
