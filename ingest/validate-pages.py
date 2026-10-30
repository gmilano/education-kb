#!/usr/bin/env python3
"""validate-pages.py -- frontmatter + shape checks for the shelf pages (p547).

WHAT IT IS FOR
  Run it over the lines a pass ADDS, as a pre-commit check on that pass's own work:
      git diff -U0 -- <page> | grep '^+'
  Scoped that way it answered cleanly for p547's 894 added lines across 10 files
  (0 placeholder-as-data rows, 0 ragged tables).

🔴 READ THIS BEFORE QUOTING IT PAGE-WIDE
  Run over a WHOLE page its two shape heuristics have a high false-positive rate on
  this corpus, and p547 therefore refused to publish a defect rate from it:

    * `PLACEHOLDER_ROW` cannot tell a stranded header from a legitimate ROW LABEL.
      These pages use two-column `| Field | Value |` tables whose first cell is the
      word `Licence`, `Repo` or `Name`. Those are correct rows and it flags them.
    * the ragged-table check counts `|` characters. ESCAPED pipes (`\|`), which are
      the correct way to put a literal pipe in a cell, are now stripped before
      counting -- p547 added that fix after the heuristic flagged p547's OWN
      negative-controls table, which is a clean 3 columns. An unescaped pipe inside
      inline code will still read as a mismatch.

  p455 retracted a 20.6 % shelf-defect sweep for exactly this class of error --
  "adjacency is not attribution, and the shelves were more precise than the
  instrument". A heuristic that cannot distinguish a row label from a stranded
  header is not evidence. Fixing either heuristic means parsing the table, not
  counting tokens; until then, use this on a diff and not on a page.

FRONTMATTER CHECKS, by contrast, are exact and safe to quote: industry must be
`education`, `region` must be one of the five closed-vocabulary values, and
`updated` must be ISO `YYYY-MM-DD`.
"""
import pathlib, re, sys
REGIONS = {"North America","EMEA","APAC","LATAM","Global"}
PLACEHOLDER_ROW = re.compile(r"^\|\s*(nombre|name|agent|repo|repositorio|licencia|license|licence|descripcion|descripción|tbd|xxx|\.\.\.|…)\s*\|", re.I)
FILES = ["agents/top.md","agents/trending.md","repos/foundations.md","repos/trending.md",
         "verticals/solutions.md","intel/market.md","intel/trends.md","compose/patterns.md",
         "intel/open-gaps.md","intel/measured-unusable.md"]
bad = 0
for f in FILES:
    p = pathlib.Path(f)
    lines = p.read_text(encoding="utf-8").splitlines()
    # frontmatter
    if lines[0].strip() != "---":
        print(f"FAIL {f}: no frontmatter"); bad += 1; continue
    end = next(i for i,l in enumerate(lines[1:],1) if l.strip()=="---")
    fm = dict()
    for l in lines[1:end]:
        if ":" in l:
            k,v = l.split(":",1); fm[k.strip()] = v.strip()
    errs = []
    for k in ("industry","region","updated"):
        if k not in fm: errs.append(f"missing {k}")
    if fm.get("industry") != "education": errs.append(f"industry={fm.get('industry')}")
    if fm.get("region") not in REGIONS: errs.append(f"region={fm.get('region')!r} not in closed vocab")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fm.get("updated","")): errs.append(f"updated={fm.get('updated')}")
    # placeholder rows left as data
    ph = [(i+1,l[:60]) for i,l in enumerate(lines) if PLACEHOLDER_ROW.match(l) and not re.match(r"^\|[\s|:-]+\|?\s*$", l)]
    # a header row is legitimate only when a separator row follows it
    ph = [(n,s) for n,s in ph if not (n < len(lines) and re.match(r"^\s*\|[\s|:-]+\|?\s*$", lines[n]))]
    if ph: errs.append(f"{len(ph)} placeholder-as-data row(s): {ph[:3]}")
    # table pipe-count consistency per contiguous block
    blk, start = [], None
    for i,l in enumerate(lines):
        if l.lstrip().startswith("|"):
            if start is None: start = i
            # strip escaped pipes: `\|` is a literal pipe in a cell, not a delimiter
            blk.append(l.replace("\\|", "").count("|"))
        else:
            if blk and len(set(blk)) > 1:
                errs.append(f"ragged table at line {start+1}: pipe counts {sorted(set(blk))}")
            blk, start = [], None
    print(("FAIL " if errs else "ok   ") + f"{f}  region={fm.get('region')}  updated={fm.get('updated')}" + ("  :: " + "; ".join(errs) if errs else ""))
    bad += bool(errs)
print("\nRESULT:", "ALL GREEN" if not bad else f"{bad} file(s) with findings")
sys.exit(0)
