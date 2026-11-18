import re,sys
bad=0
for f in ['blk-trending-common.md','blk-top.md','blk-foundations.md','blk-verticals.md','blk-trends.md','blk-market.md','blk-patterns.md']+[x for x in __import__('glob').glob('reg-*.md')]:
    lines=open(f,encoding='utf-8').read().split('\n')
    i=0; infence=False
    while i<len(lines):
        if lines[i].strip().startswith('```'): infence=not infence
        if not infence and lines[i].lstrip().startswith('|'):
            tbl=[]; start=i
            while i<len(lines) and lines[i].lstrip().startswith('|'):
                tbl.append(lines[i]); i+=1
            widths=[len([c for c in re.split(r'(?<!\\)\|',r)[1:-1]]) for r in tbl]
            hdr=widths[0]
            if len(tbl)<2 or not re.match(r'^\s*\|[\s:\-|]+\|\s*$',tbl[1]):
                print(f"{f}:{start+1} TABLE WITHOUT SEPARATOR"); bad+=1
            off=[(start+1+k,w) for k,w in enumerate(widths) if w!=hdr]
            if off:
                print(f"{f}:{start+1} header={hdr} cols, mismatched rows: {off}"); bad+=1
            # placeholder/header-as-data detection
            for k,r in enumerate(tbl[2:],start=2):
                cells=[c.strip().strip('*`').lower() for c in re.split(r'(?<!\\)\|',r)[1:-1]]
                if cells and all(c in ('repo','nombre','name','licencia','license','grant','描述','desc','description','★','stars') for c in cells if c):
                    print(f"{f}:{start+1+k} HEADER-AS-DATA: {r[:80]}"); bad+=1
            continue
        i+=1
print("tables with problems:",bad)
