#!/usr/bin/env python3
"""p401 membership check, re-implemented from scratch this pass.

Answers "is THIS candidate on the shelf?" over BOTH address channels:
  channel U : github.com/<owner>/<repo>   (URL form)
  channel B : `<owner>/<repo>`            (backticked bare slug)

Four verdicts, deliberately keeping NAME-OTHER-OWNER apart from
NAME-SUBSTRING-ONLY (p400 finding 2: collapsing them is how the defect
survived).
"""
import re, sys, os

SHELF_FILES = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
               "repos/trending.md", "verticals/solutions.md", "intel/market.md",
               "intel/trends.md", "intel/open-gaps.md", "compose/patterns.md"]

SEG = r"[A-Za-z0-9][A-Za-z0-9._-]*"
URL_RE = re.compile(r"github\.com/(" + SEG + r")/(" + SEG + r")", re.I)
BQ_RE  = re.compile(r"`(" + SEG + r")/(" + SEG + r")`")

# repo-name suffixes that are path noise, not repo names
def norm(owner, repo):
    repo = re.sub(r"\.git$", "", repo)
    return owner.lower(), repo.lower()

def harvest(root):
    urls, bqs = set(), set()
    for rel in SHELF_FILES:
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            print(f"!! missing shelf file: {rel}", file=sys.stderr)
            continue
        txt = open(p, encoding="utf-8", errors="replace").read()
        for m in URL_RE.finditer(txt):
            urls.add(norm(*m.groups()))
        for m in BQ_RE.finditer(txt):
            bqs.add(norm(*m.groups()))
    return urls, bqs

def main():
    root = sys.argv[1]
    cands = [c.strip() for c in sys.argv[2:] if c.strip()]
    urls, bqs = harvest(root)
    union = urls | bqs
    names = {}
    for (o, r) in union:
        names.setdefault(r, set()).add(o)

    print(f"# channel U addresses : {len(urls)}")
    print(f"# channel B addresses : {len(bqs)}")
    print(f"# union addresses     : {len(union)}")
    print()
    print("candidate\tverdict\tchannel\tdetail")
    for c in cands:
        o, r = norm(*c.split("/", 1))
        inU, inB = (o, r) in urls, (o, r) in bqs
        if inU or inB:
            ch = "U+B" if (inU and inB) else ("U" if inU else "B")
            print(f"{c}\tSHELVED-EXACT\t{ch}\t-")
        elif r in names:
            others = ",".join(sorted(names[r]))
            print(f"{c}\tNAME-OTHER-OWNER\t-\tsame repo name under: {others}")
        else:
            # substring class: some shelved repo name CONTAINS this one's, or vice versa
            subs = sorted({f"{oo}/{rr}" for rr, os_ in names.items()
                           for oo in os_ if r in rr or rr in r})
            if subs:
                print(f"{c}\tNAME-SUBSTRING-ONLY\t-\tsubstring neighbours: {','.join(subs[:4])}"
                      + (f" (+{len(subs)-4} more)" if len(subs) > 4 else ""))
            else:
                print(f"{c}\tUNSHELVED\t-\tno address, no name collision")

main()

# 🔴 DECLARED, so this is never compared with the committed census cells:
# this harvester is DELIBERATELY loose -- it applies none of p351's shape
# rejection rules, so it also catches non-addresses (`evidence/foo.tsv`,
# `left_eye_x/y`, `public/ai`).  Its totals on 2026-10-23 were
# U=2 695 / B=3 874 / union=4 238, against p400's committed 2 666 / 3 124 /
# 3 497.  The two are DIFFERENT MEASUREMENTS of different denominators and
# neither refutes the other.  It is used here for exact-address MEMBERSHIP
# only -- the question "is THIS candidate on the shelf?" -- where a loose
# denominator is safe because a false address in the corpus cannot make a
# real candidate look shelved unless it matches owner AND name exactly.
