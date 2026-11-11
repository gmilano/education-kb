#!/usr/bin/env python3
"""p766 substitute commit gate.

`make hooks` is denied in the cloud session as repository-code execution, so this
stands in for it and its result is recorded in intel/open-gaps.md.

Checks, in order of how much damage each has historically done to this base:
  1. HEADER-AS-DATA   - a body row whose cells are generic column labels
                        ("Nombre", "Repo", "Licencia", "Agent", "Repository"...).
                        This has been compiled into KB entities more than once.
  2. SEPARATOR-AS-DATA- a |---|---| row sitting where a body row belongs.
  3. PLACEHOLDER      - example/TBD/lorem/xxx/your-org rows.
  4. FRONTMATTER      - present, parseable, region in the CLOSED vocabulary.
  5. REGION-PLACEMENT - every p766 `####` block must sit AFTER its `###`
                        region heading, not before it (ACTION p756-C).
  6. OVERWIDE-ROWS    - rows with more cells than their header (ACTION p765-G),
                        reported as warnings; the fix is additive.

SCOPE, and why it is scoped: checks 1-3 run ONLY over the section this pass wrote
(from the top of the shelf to the first prior-pass `## ` heading). The shelves are
append-only and carry 765 passes of history that legitimately *discusses* header
rows, placeholder rows and the "nombre" defect in prose and in tables; running a
placeholder regex over that history produces 282 findings and not one of them is
a defect. A commit gate exists to stop THIS pass shipping a bad row. Checks 4
(frontmatter) and 5 (region placement) are cheap and run base-wide.
"""
import re, sys, pathlib

SHELVES = ["agents/top.md","agents/trending.md","repos/foundations.md","repos/trending.md",
           "verticals/solutions.md","intel/market.md","intel/trends.md","intel/open-gaps.md",
           "intel/measured-unusable.md","compose/patterns.md","README.md"]
REGIONS = {"North America","EMEA","APAC","LATAM","Global"}
HEADERISH = {"nombre","repo","licencia","agent","repository","name","license","grant","platform",
             "descripcion","description","id","item","state","region","branch","stars","verdict",
             "query","token","count","duty","instrument","old address","successor","pushed"}
PLACEHOLDER = re.compile(r"\b(lorem ipsum|tbd|tba|xxx+|your[- ]org|example\.com|foo/bar|placeholder|coming soon)\b", re.I)

fail, warn = [], []
rows_checked = [0]

def cells(line):
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")): return None
    return [c.strip() for c in s[1:-1].split("|")]

def strip_md(t):
    t = re.sub(r"`[^`]*`", lambda m: m.group(0)[1:-1], t)
    t = re.sub(r"\*\*|\*|__", "", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return t.strip().lower().rstrip(":")

for rel in SHELVES:
    p = pathlib.Path(rel)
    if not p.exists():
        fail.append(f"{rel}: MISSING"); continue
    text = p.read_text(encoding="utf-8")
    lines = text.split("\n")

    if not text.startswith("---\n"):
        fail.append(f"{rel}: no YAML frontmatter")
    else:
        fm = text.split("---",2)[1]
        keys = dict(re.findall(r"^(\w+):\s*(.+)$", fm, re.M))
        for k in ("industry","region","updated"):
            if k not in keys: fail.append(f"{rel}: frontmatter missing '{k}'")
        if "region" in keys and keys["region"].strip() not in REGIONS:
            fail.append(f"{rel}: region '{keys['region'].strip()}' outside closed vocabulary")
        if "updated" in keys and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", keys["updated"].strip()):
            fail.append(f"{rel}: updated not YYYY-MM-DD")

    # scope checks 1-3 to this pass's own new section
    new_end = len(lines)
    for j, line in enumerate(lines):
        if j > 5 and re.match(r"^## ", line) and "p766" not in line and "(p766)" not in line:
            new_end = j; break

    hdr = None; hdr_n = 0
    for i, line in enumerate(lines, 1):
        c = cells(line)
        if c is None:
            hdr = None; continue
        is_sep = all(re.fullmatch(r":?-{2,}:?", x) for x in c if x != "")
        if is_sep:
            if hdr is None and i <= new_end:
                fail.append(f"{rel}:{i}: separator row with no header above it")
            continue
        if hdr is None:
            hdr = c; hdr_n = len(c); continue
        if i > new_end:
            continue
        norm = [strip_md(x) for x in c]
        nonempty = [x for x in norm if x]
        if len(nonempty) >= 2 and all(x in HEADERISH for x in nonempty):
            fail.append(f"{rel}:{i}: HEADER-AS-DATA row -> {c[:4]}")
        if PLACEHOLDER.search(line):
            fail.append(f"{rel}:{i}: placeholder row -> {c[:3]}")
        if len(c) > hdr_n:
            warn.append(f"{rel}:{i}: NEW overwide row ({len(c)} cells vs header {hdr_n})")
        rows_checked[0] += 1

    if rel == "intel/market.md":
        cur = None; seen = set()
        for i, line in enumerate(lines, 1):
            m3 = re.fullmatch(r"### (.+?)\s*", line)
            m4 = re.match(r"#### .*?\bp766\b", line)
            if m3 and m3.group(1).strip() in REGIONS:
                cur = m3.group(1).strip()
            elif line.startswith("## ") and not line.startswith("###"):
                cur = None
            elif m4:
                if cur is None:
                    fail.append(f"{rel}:{i}: p766 block not under any ### region heading")
                else:
                    seen.add(cur)
        missing = REGIONS - seen
        if missing:
            fail.append(f"{rel}: p766 block missing under region(s): {sorted(missing)}")
        else:
            print(f"  OK  {rel}: 5/5 p766 region blocks sit after their ### heading")

print()
for w in warn[:12]: print("  WARN", w)
if warn: print(f"  ({len(warn)} overwide rows total — ACTION p766-E, additive fix only)")
print()
if fail:
    print(f"GATE RED — {len(fail)} failure(s):")
    for f in fail: print("   ", f)
    sys.exit(1)
print(f"GATE GREEN — {len(SHELVES)} shelves, {rows_checked[0]} new p766 table rows checked, 0 failures.")
