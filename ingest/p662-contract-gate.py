#!/usr/bin/env python3
"""p662 contract gate, written to run OUT-OF-TREE.

`make hooks` and `ingest/address-ledger.py` have been denied by the external-code
classifier for twelve consecutive passes (660-A, 661-G, 662-I), so each pass has
been checking the page contracts by hand with grep/awk.  This is that check, as
one script, so the next pass does not re-derive it:

  * frontmatter present on every live page, with industry/region/updated
  * `region` inside the CLOSED five-value vocabulary
  * exactly one `## Opportunities by region` in intel/market.md, with one
    `###` subsection per region and nothing else
  * no header-shaped row left as DATA (the defect the KB brief names by name)
  * the row count in each shelf heading reconciles with its table

Usage:  python3 -I ingest/p662-contract-gate.py [repo-root]
Exit 0 green, 1 red.
"""
import os, re, sys

R = sys.argv[1] if len(sys.argv) > 1 else "."
PAGES = ["agents/top.md", "agents/trending.md", "repos/foundations.md", "repos/trending.md",
         "verticals/solutions.md", "compose/patterns.md", "intel/market.md", "intel/trends.md",
         "intel/open-gaps.md", "intel/measured-unusable.md"]
REGIONS = {"North America", "EMEA", "APAC", "LATAM", "Global"}
SEP = re.compile(r"^\|[\s:|-]+\|?\s*$")
# A header-shaped DATA row is one that looks like a table header AND is the first
# row of its table AND is not followed by a separator.  Requiring "first row of
# its table" is what stops a legitimate two-column `| licence | ... |` body row
# from being reported -- p662's first draft of this gate flagged 23 of those.
HDRWORD = re.compile(r"^\|\s*(Nombre|Name|Repo|Repositorio|Platform|Plataforma|Licencia|License|"
                     r"Licence|Descripci[oó]n|Description|Stars|Estrellas)\s*\|", re.I)
fail = 0

def frontmatter(lines):
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return None
    return dict(x.split(":", 1) for x in lines[1:lines[1:].index("---") + 1] if ":" in x)

for f in PAGES:
    path = os.path.join(R, f)
    if not os.path.exists(path):
        print("🔴 missing page:", f); fail += 1; continue
    lines = open(path, encoding="utf-8").read().split("\n")
    fm = frontmatter(lines)
    bad = []
    if fm is None:
        bad.append("NO FRONTMATTER")
        reg = upd = "?"
    else:
        reg = fm.get("region", "").strip(); upd = fm.get("updated", "").strip()
        if fm.get("industry", "").strip() != "education":
            bad.append(f"industry={fm.get('industry','').strip()!r}")
        if reg not in REGIONS:
            bad.append(f"region={reg!r} NOT IN CLOSED VOCABULARY {sorted(REGIONS)}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", upd):
            bad.append(f"updated={upd!r} not YYYY-MM-DD")
    hs = []
    for i, l in enumerate(lines):
        if not HDRWORD.match(l):
            continue
        first_row = i == 0 or not lines[i - 1].startswith("|")
        followed_by_sep = i + 1 < len(lines) and SEP.match(lines[i + 1])
        if first_row and not followed_by_sep:
            hs.append(i + 1)
    if hs:
        bad.append(f"header-shaped DATA rows at lines {hs}")
    print(("🔴 " if bad else "🟢 ") + f"{f}  region={reg} updated={upd}" +
          ("  | " + "; ".join(bad) if bad else ""))
    fail += len(bad)

m = open(os.path.join(R, "intel/market.md"), encoding="utf-8").read()
n = len(re.findall(r"^## Opportunities by region\s*$", m, re.M))
subs = re.findall(r"^### (.+?)\s*$", m[m.index("## Opportunities by region"):], re.M)
subs = [x for x in subs if not x.startswith(("🟢", "🔴", "🟡", "🔵", "🔧"))]
ok = n == 1 and set(subs) == REGIONS and len(subs) == len(REGIONS)
print(("🟢 " if ok else "🔴 ") + f"intel/market.md: '## Opportunities by region' ×{n}, subsections={subs}")
if not ok:
    fail += 1

for f, pat in (("agents/top.md", r"^## The agents — (\d+) verified rows\s*$"),
               ("repos/foundations.md", r"^## Foundations — (\d+) verified rows\s*$"),
               ("verticals/solutions.md", r"^## Platforms — (\d+) verified rows\s*$")):
    s = open(os.path.join(R, f), encoding="utf-8").read()
    mt = re.search(pat, s, re.M)
    if not mt:
        print("🔴 " + f + ": no row-count heading found"); fail += 1; continue
    claimed = int(mt.group(1))
    rows, started, widths = [], False, set()
    for l in s[mt.end():].split("\n"):
        if l.startswith("|"):
            started = True
            if not SEP.match(l):
                rows.append(l); widths.add(l.count("|"))
        elif started and l.strip() == "":
            break
    data = len(rows) - 1                       # drop the header row
    ragged = len(widths) > 1
    good = claimed == data and not ragged
    print(("🟢 " if good else "🔴 ") + f"{f}: heading claims {claimed}, table has {data} data rows"
          + (f" 🔴 RAGGED: cell counts {sorted(widths)}" if ragged else ""))
    if not good:
        fail += 1

print("\nGATE:", "🟢 GREEN" if fail == 0 else f"🔴 {fail} RED")
sys.exit(0 if fail == 0 else 1)
