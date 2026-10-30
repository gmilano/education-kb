#!/usr/bin/env python3
"""p546 pre-commit validation of the eight curated pages.

Checks the three things this KB's own rules make non-negotiable:
  1. YAML frontmatter present, with industry / region / updated
  2. `region` drawn from the CLOSED five-value vocabulary
  3. no table row that is a header, a placeholder or an example left as data
     (the "| Nombre | Repo | Licencia |" defect)
"""
import re
import sys

REGIONS = {"North America", "EMEA", "APAC", "LATAM", "Global"}
# The defect this KB warns about is a row where EVERY cell is a header word or a
# placeholder — "| Nombre | Repo | Licencia |" compiled into an entity named
# "nombre". A row whose FIRST cell is a field label and whose other cells hold
# real data is a legitimate key/value table, and this base uses hundreds of them:
# matching on the first cell alone produced 40 false positives on pages that are
# correct. So every non-empty cell must match.
PLACEHOLDER_CELL = re.compile(
    r"\A(nombre|name|agent|agente|repo|repositorio|url|licencia|licence|license"
    r"|descripci[oó]n|description|notas?|notes?|ejemplo|example|placeholder"
    r"|tbd|todo|t[ií]tulo|title|xxx|yyy|foo|bar|baz|lorem|ipsum|n/?a|-+|\.\.\.)\Z",
    re.I)

PAGES = sys.argv[1:]
bad = 0

for p in PAGES:
    text = open(p, encoding="utf-8").read()
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        print(f"RED  {p}: no frontmatter")
        bad += 1
        continue
    fm = dict(
        (k.strip(), v.strip())
        for k, v in (l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    )
    for key in ("industry", "region", "updated"):
        if key not in fm:
            print(f"RED  {p}: frontmatter missing `{key}`")
            bad += 1
    if fm.get("industry") != "education":
        print(f"RED  {p}: industry is {fm.get('industry')!r}, expected 'education'")
        bad += 1
    reg = fm.get("region", "")
    if reg not in REGIONS:
        print(f"RED  {p}: region {reg!r} is not in the closed vocabulary {sorted(REGIONS)}")
        bad += 1
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fm.get("updated", "")):
        print(f"RED  {p}: updated {fm.get('updated')!r} is not YYYY-MM-DD")
        bad += 1

    # placeholder / header rows left as data
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        if not line.startswith("|") or re.fullmatch(r"\|[\s|:-]+\|?", line):
            continue
        # a header row is legitimate when the NEXT line is a separator
        nxt = lines[i] if i < len(lines) else ""
        if re.fullmatch(r"\|[\s|:-]+\|?", nxt.strip()):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        cells = [c for c in cells if c]
        if len(cells) >= 2 and all(PLACEHOLDER_CELL.match(c) for c in cells):
            print(f"RED  {p}:{i}: placeholder/header row left as data: {line[:70]}")
            bad += 1

print(("GREEN  all %d pages pass" % len(PAGES)) if not bad else f"RED  {bad} problem(s)")
sys.exit(1 if bad else 0)
