import re,sys,io,collections
RE=re.compile(r'github\.com/([A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*)')
def slugs(p):
    s=collections.Counter()
    for ln in io.open(p,encoding='utf-8',errors='replace'):
        for m in RE.finditer(ln): s[m.group(1).rstrip('.')]+=1
    return s
tr=slugs('agents/trending.md'); tr.update(slugs('repos/trending.md'))
shelf=set()
for p in ['agents/top.md','repos/foundations.md','verticals/solutions.md','compose/patterns.md','intel/market.md','intel/trends.md','intel/open-gaps.md']:
    try: shelf |= set(slugs(p))
    except FileNotFoundError: pass
absent={k:v for k,v in tr.items() if k not in shelf}
print(f"trending distinct slugs = {len(tr)}")
print(f"shelf distinct slugs    = {len(shelf)}")
print(f"in trending, ABSENT from every shelf page = {len(absent)}")
io.open(sys.argv[1],'w').write('\n'.join(k for k,_ in sorted(absent.items(), key=lambda x:-x[1])))
for k,v in sorted(absent.items(), key=lambda x:-x[1])[:40]: print(f"{v:5d}  {k}")
