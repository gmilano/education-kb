#!/usr/bin/env python3
"""Stand-in for the gates `make hooks` will not run in this environment.

Reads the committed markdown as DATA (no repo code is executed) and checks the
controls that bear on what p306 wrote: frontmatter, the closed region vocabulary,
table structure (p277's class), and placeholder rows published as data.
"""
import re
import sys

REPO = "/home/user/education-kb"
FILES = [
    "agents/top.md", "agents/trending.md", "repos/foundations.md",
    "repos/trending.md", "verticals/solutions.md", "intel/market.md",
    "intel/trends.md", "compose/patterns.md", "README.md",
]
REGIONS = {"North America", "EMEA", "APAC", "LATAM", "Global"}

# A separator must contain at least one dash. Without this, the legitimate
# EMPTY-HEADER row `| | |` matches the separator pattern and the real separator
# on the next line is reported as headerless — a false positive this check
# produced on 29 inherited rows before the dash was required.
SEP = re.compile(r"^\s*\|[\s:|-]*-[\s:|-]*\|\s*$")
# the exact failure the brief names: a header or example row compiled as an entity
PLACEHOLDERS = {
    "nombre", "repo", "licencia", "descripcion", "descripción", "name",
    "license", "description", "url", "stars", "ejemplo", "example", "tbd",
    "xxx", "foo", "bar", "lorem",
}

fails, warns = [], []

for rel in FILES:
    path = f"{REPO}/{rel}"
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")

    # --- frontmatter + closed region vocabulary
    m = re.match(r"\A---\n(.*?\n)---\n", text, re.S)
    if not m:
        fails.append(f"{rel}: no YAML frontmatter")
        continue
    fm = m.group(1)
    reg = re.search(r"^region:\s*(.+?)\s*$", fm, re.M)
    if not reg:
        fails.append(f"{rel}: frontmatter has no region")
    elif reg.group(1) not in REGIONS:
        fails.append(f"{rel}: region '{reg.group(1)}' outside closed vocabulary")
    if not re.search(r"^industry:\s*education\s*$", fm, re.M):
        fails.append(f"{rel}: frontmatter industry is not 'education'")
    if not re.search(r"^updated:\s*\d{4}-\d{2}-\d{2}\s*$", fm, re.M):
        fails.append(f"{rel}: frontmatter updated is not an ISO date")

    # --- p277: a separator must sit directly under its header, never below a data row
    for i, line in enumerate(lines):
        if SEP.match(line) and line.count("|") > 2:
            if i == 0 or not lines[i - 1].strip().startswith("|"):
                fails.append(f"{rel}:{i+1}: separator with no header row above it")

    # --- placeholder rows published as DATA (the row below a separator)
    for i in range(1, len(lines) - 1):
        if SEP.match(lines[i]) and lines[i].count("|") > 2:
            nxt = lines[i + 1]
            if nxt.strip().startswith("|"):
                cells = [c.strip().strip("*`").lower() for c in nxt.strip("| \t").split("|")]
                if cells and all(c in PLACEHOLDERS or c == "" for c in cells):
                    fails.append(f"{rel}:{i+2}: placeholder row published as data: {nxt.strip()[:70]}")

# --- every repo URL written this pass must be one p306 actually read
payload = open(f"{REPO}/evidence/p306-licence-payload.2026-10-19-p306.tsv", encoding="utf-8")
probed = {l.split("\t")[0] for l in payload if l.strip() and not l.startswith(("#", "slug"))}
found = set()
for rel in ["repos/foundations.md", "repos/trending.md", "compose/patterns.md"]:
    head = open(f"{REPO}/{rel}", encoding="utf-8").read().split("## ", 2)
    sec = head[1] if len(head) > 1 else ""
    for slug in re.findall(r"github\.com/([A-Za-z0-9._-]+/[A-Za-z0-9._-]+)", sec):
        found.add(slug.rstrip(")."))
unprobed = {s for s in found if s not in probed}
if unprobed:
    warns.append("slugs cited in p306 sections but not in this pass's payload file "
                 "(carried from earlier passes — verify they are marked as carried): "
                 + ", ".join(sorted(unprobed)))

print(f"probed slugs in evidence: {len(probed)}")
for w in warns:
    print(f"WARN  {w}")
for f in fails:
    print(f"FAIL  {f}")
print(f"\n{'RED' if fails else 'GREEN'} — {len(fails)} failures, {len(warns)} warnings")
sys.exit(1 if fails else 0)
