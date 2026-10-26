#!/usr/bin/env python3
"""p455 -- the `Gap 454-C` re-sweep: every carried GNU-family cell, re-read
first-hand, graded on the VERSION axis.

`Gap 454-C` asked for exactly this and said `p454` did not do it:

    "Open: add a version axis and re-sweep the carried GPL/LGPL/AGPL cells;
     p454 did not."

Population: every distinct GitHub address on the eight shelves whose own shelf
line names a GNU family. That is the definition of "a carried GPL/LGPL/AGPL
cell" -- the shelf asserts a GNU grant at that address -- and it is extracted
mechanically rather than hand-listed, so the denominator is reproducible.

Three verdicts matter and are reported separately, because `Gap 454-H` showed
this base had been publishing two of them as one class:
  VERSION_DISAGREE  -- shelf says family F, payload says F at a DIFFERENT version
  FAMILY_DISAGREE   -- shelf says F, payload says a different family entirely
  UNCHECKABLE       -- ADDRESS_DEAD or REPO_LIVE_NO_GRANT: the carried grant
                       can no longer be checked against anything
"""
import collections
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import family_version as fv
import fetch
import fetch_fast
from concurrent.futures import ThreadPoolExecutor

KB = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  ".." , "..", ".."))
SHELVES = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
           "repos/trending.md", "verticals/solutions.md", "intel/market.md",
           "intel/trends.md", "compose/patterns.md"]

ADDR = re.compile(r"github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+?)(?:\.git)?(?=[)\s`,/\]]|$)")
# The GNU grade the SHELF LINE asserts. Version-bearing forms first, so
# `AGPL-3.0` is not read as a bare `AGPL`.
SHELF_GNU = re.compile(
    r"\b(AGPL-?3(?:\.0)?|AGPLv?3|LGPL-?2\.1|LGPL-?3(?:\.0)?|LGPLv?[23]|"
    r"GPL-?2(?:\.0)?|GPL-?3(?:\.0)?|GPLv?[23]|AGPL|LGPL|GPL)\b")
SKIP = {"issues", "tree", "blob", "wiki", "releases", "pulls", "topics",
        "apps", "features", "about", "orgs", "sponsors"}

claims = collections.defaultdict(set)   # address -> {shelf grade strings}
where = collections.defaultdict(set)    # address -> {shelf names}

for rel in SHELVES:
    path = os.path.join(KB, rel)
    if not os.path.exists(path):
        continue
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            gnu = SHELF_GNU.findall(line)
            if not gnu:
                continue
            for owner, repo in ADDR.findall(line):
                if repo.lower() in SKIP or owner.lower() in SKIP:
                    continue
                addr = f"{owner}/{repo}"
                for g in gnu:
                    claims[addr].add(g)
                where[addr].add(rel)

pop = sorted(claims)
print(f"population: {len(pop)} distinct addresses on {len(SHELVES)} shelves "
      f"whose shelf line asserts a GNU grant\n")

# Fabricated negative control FIRST, so every verdict below is a measurement.
neg = fetch.grant("nope-p455-sweep/nope-p455")
print(f"fabricated negative control: {neg['verdict']}")
assert neg["verdict"] == "ADDRESS_DEAD", "probe is not separating live from dead"

def grade(addr):
    return (addr, fetch_fast.grant(addr))


# 12 workers over 481 cells. The verdict for each cell is computed from its own
# payload only, so concurrency cannot change any result -- it only changes how
# long the denominator takes to reach.
with ThreadPoolExecutor(max_workers=12) as ex:
    got = dict(ex.map(grade, pop))

rows, tally = [], collections.Counter()
for i, addr in enumerate(pop, 1):
    shelf_claims = sorted(claims[addr])
    g = got[addr]
    if g["verdict"] != "READ":
        verdict = "UNCHECKABLE/" + g["verdict"]
        served, fwd = "", ""
    else:
        served = fv.family(g["text"])
        fwd = fv.only_or_later(g["text"])
        cs = fv.canon(served)
        cclaims = {fv.canon(c) for c in shelf_claims}
        if cs in cclaims:
            verdict = "AGREE"
        else:
            sf = re.match(r"^(AGPL|LGPL|GPL)", cs or "")
            cf = {re.match(r"^(AGPL|LGPL|GPL)", c).group(1)
                  for c in cclaims if re.match(r"^(AGPL|LGPL|GPL)", c)}
            if sf and sf.group(1) in cf:
                verdict = "VERSION_DISAGREE"
            else:
                verdict = "FAMILY_DISAGREE"
    tally[verdict.split("/")[0]] += 1
    rows.append({"addr": addr, "shelf_claims": shelf_claims, "served": served,
                 "fwd": fwd, "verdict": verdict, "bytes": g.get("bytes", 0),
                 "sha": g.get("sha", ""),
                 "at": f"{g.get('path', g.get('live_path',''))}@{g.get('ref','')}",
                 "shelves": sorted(where[addr])})
    if verdict != "AGREE":
        print(f"  [{i}/{len(pop)}] {verdict:28} {addr:46} "
              f"shelf={','.join(shelf_claims):18} served={served!r} {fwd}")

print(f"\n--- {len(pop)} cells ---")
for k, v in tally.most_common():
    print(f"  {k:22} {v:4}  {100.0*v/len(pop):5.1f} %")

out = os.path.join(KB, "evidence", f"gnu-version-axis.2026-10-26-p455.tsv")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as fh:
    fh.write("address\tshelf_claims\tserved\tforward_grant\tverdict\tbytes\tsha\tat\tshelves\n")
    for r in rows:
        fh.write("\t".join([r["addr"], "|".join(r["shelf_claims"]), r["served"],
                            r["fwd"], r["verdict"], str(r["bytes"]), r["sha"],
                            r["at"], "|".join(r["shelves"])]) + "\n")
print(f"\nevidence -> {out}")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sweep.json"), "w") as fh:
    json.dump(rows, fh, indent=1)
