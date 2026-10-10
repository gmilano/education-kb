import re, pathlib, collections
KB = pathlib.Path("/home/user/education-kb")
SHELF = ["agents/top.md","repos/foundations.md","verticals/solutions.md",
         "intel/market.md","intel/trends.md","compose/patterns.md"]
HIST  = ["agents/trending.md","repos/trending.md"]
SLUG = re.compile(r"github\.com/([A-Za-z0-9][\w.\-]*/[\w.\-]+?)(?=[)\s`,:\]\"'/]|$)")
def slugs(p):
    t = (KB/p).read_text(encoding="utf-8", errors="replace")
    return t, [(m.group(1).rstrip('.'), t.count("\n",0,m.start())+1) for m in SLUG.finditer(t)]
shelf = collections.defaultdict(set)
for p in SHELF:
    _, s = slugs(p)
    for sl,_ln in s: shelf[sl.lower()].add(p)
# history: newest-first, so the OLDEST mention is the LAST line. Map line -> enclosing dated section.
HDR = re.compile(r"^##+\s*(?:🔴|🟢|🟡|🔵|\s)*(\d{4}-\d{2}-\d{2})\s*[—-]+\s*(?:pase|pass)\s*(\d+)", re.I)
HDR2 = re.compile(r"(?:pase|pass)\s*(\d+)", re.I)
first_seen = {}
for p in HIST:
    t, s = slugs(p)
    lines = t.split("\n")
    marks = []  # (lineno, label)
    for i,l in enumerate(lines, 1):
        if l.startswith("##"):
            m = HDR.match(l)
            if m: marks.append((i, f"{m.group(1)}/pase{m.group(2)}"))
            else:
                d = re.search(r"\d{4}-\d{2}-\d{2}", l); n = HDR2.search(l)
                if d: marks.append((i, f"{d.group(0)}/pase{n.group(1) if n else '?'}"))
    def sect(ln):
        lab = "pre-dated"
        for mln, l in marks:
            if mln <= ln: lab = l
            else: break
        return lab
    deepest = {}
    for sl, ln in s:
        k = sl.lower()
        if k not in deepest or ln > deepest[k]: deepest[k] = ln
    for k, ln in deepest.items():
        lab = sect(ln)
        if k not in first_seen or lab < first_seen[k][0]:
            first_seen[k] = (lab, f"{p}:{ln}")
print(f"shelf slugs: {len(shelf)}")
print(f"history slugs: {len(first_seen)}")
rows = []
for sl, pages in sorted(shelf.items()):
    lab, where = first_seen.get(sl, ("NOT-IN-HISTORY","-"))
    rows.append((sl, ",".join(sorted(pages)), lab, where))
with open("promotion-ledger-pass98.tsv","w") as f:
    f.write("slug\tshelf_pages\toldest_history_section\tevidence\n")
    for r in rows: f.write("\t".join(r)+"\n")
nih = [r for r in rows if r[2]=="NOT-IN-HISTORY"]
print(f"shelf rows with NO history mention: {len(nih)}")
for r in nih[:12]: print("   ", r[0], "|", r[1])
# the forgotten-kind detector: shelf row whose oldest history mention is >=3 passes older than today
import datetime
print("\n-- oldest-history distribution (top 14 by age) --")
for r in sorted(rows, key=lambda x: x[2])[:14]: print(f"   {r[2]:>22}  {r[0]}")
