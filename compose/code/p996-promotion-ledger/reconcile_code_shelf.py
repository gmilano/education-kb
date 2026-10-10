import re, pathlib, collections
KB = pathlib.Path("/home/user/education-kb")
SHELF = ["agents/top.md","repos/foundations.md","verticals/solutions.md",
         "intel/market.md","intel/trends.md","compose/patterns.md"]
SLUG = re.compile(r"github\.com/([A-Za-z0-9][\w.\-]*/[\w.\-]+?)(?=[)\s`,:\]\"'/]|$)")
def sl(t): return {m.group(1).rstrip('.').lower() for m in SLUG.finditer(t)}
shelf = set()
for p in SHELF: shelf |= sl((KB/p).read_text(encoding="utf-8", errors="replace"))
code = collections.defaultdict(set)
for f in sorted((KB/"compose"/"code").rglob("*")):
    if f.is_file() and f.suffix in (".md",".sh",".py",".tsv",".txt"):
        for s in sl(f.read_text(encoding="utf-8", errors="replace")):
            code[s].add(str(f.relative_to(KB/"compose"/"code")).split("/")[0])
only = {s:d for s,d in code.items() if s not in shelf}
print(f"slugs in compose/code: {len(code)}   on shelf: {len(shelf)}   in code but NOT on shelf: {len(only)}")
# the UniTime shape: a slug carried by a DEDICATED tested directory, not merely swept in a results table
SWEEP = re.compile(r"^(p\d+|grant-ladder|licence-|market-|dependency-|description-|fork-|git-|gitlab-|npm-|nomad-|action-|lib$)")
ded = {s:d for s,d in only.items() if any(not SWEEP.match(x) for x in d)}
print(f"\n-- in code but not on shelf, carried by a NON-sweep (purpose-built) directory: {len(ded)} --")
for s,d in sorted(ded.items()):
    print(f"   {s:<48} {sorted(d)}")
