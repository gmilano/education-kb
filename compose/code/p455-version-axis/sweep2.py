#!/usr/bin/env python3
"""p455 -- the `Gap 454-C` sweep, RE-ATTRIBUTED, because the first run's
headline was this instrument's artefact and not a property of the shelves.

The first run reported **99 FAMILY_DISAGREE (20.6 %)** over 481 cells. It is
wrong, and the mechanism is one line of extraction logic:

    for every GNU token on a line, for every address on the same line:
        attribute the token to the address

That is LINE-LEVEL CO-OCCURRENCE, and these shelves are full of prose and
table rows that name several projects at once. The first run therefore
"found":

  - `learningequality/kolibri` carrying a shelf claim of `GPL-3.0` when
    Kolibri is MIT and this base's own notes say so ("Kolibri(MIT-offline)");
  - `junit-team/junit4` carrying `GPL` when JUnit 4 is EPL;
  - `rhasspy/piper`, `jcputney/scorm-again`, `microsoft/moodle-ai-assistant`
    all carrying a GNU claim they never made -- each one sharing a line with
    Moodle, whose GPL is real.

This is the same defect class the last three passes each caught once:
`p452`'s three false DISAGREE verdicts from deriving an address out of a
package name, `Gap 451`'s rule that a registry NAME hit is not evidence, and
`Gap 454-I`'s header-shape control that cried wolf on a house table
convention. The lesson generalises past licences: ON A PROSE SHELF,
ADJACENCY IS NOT ATTRIBUTION.

Attribution rule used here, in order:
  1. SAME CELL -- the address and the GNU token are in one `|`-delimited
     markdown cell. This is the row's own grant column, and it is the only
     direct evidence a table gives.
  2. SOLE ADDRESS IN ROW -- the row names exactly one distinct address, so
     every grade in it is about that address.
  3. otherwise AMBIGUOUS -- excluded from the denominator and COUNTED, because
     an excluded cell that is silently dropped looks exactly like a cell that
     agreed.

And the version question is split, because "no version stated" is not a
disagreement:
  VERSION_DISAGREE  -- shelf states a version, payload serves a DIFFERENT one
  UNDER_SPECIFIED   -- shelf states a bare family, payload serves a version.
                       This is the honest answer to `Gap 454-C`'s real
                       question: how much of this base cannot support a
                       compatibility decision at all.
"""
import collections
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import family_version as fv

KB = "/home/user/education-kb"
SHELVES = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
           "repos/trending.md", "verticals/solutions.md", "intel/market.md",
           "intel/trends.md", "compose/patterns.md"]
ADDR = re.compile(r"github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+?)(?:\.git)?(?=[)\s`,/\]]|$)")
SHELF_GNU = re.compile(
    r"\b(AGPL-?3(?:\.0)?|AGPLv?3|LGPL-?2\.1|LGPL-?3(?:\.0)?|LGPLv?[23]|"
    r"GPL-?2(?:\.0)?|GPL-?3(?:\.0)?|GPLv?[23]|AGPL|LGPL|GPL)\b")
SKIP = {"issues", "tree", "blob", "wiki", "releases", "pulls", "topics",
        "apps", "features", "about", "orgs", "sponsors"}
BARE = {"GPL", "LGPL", "AGPL"}


def addrs_in(text):
    out = []
    for o, r in ADDR.findall(text):
        if r.lower() in SKIP or o.lower() in SKIP:
            continue
        a = f"{o}/{r}"
        if a not in out:
            out.append(a)
    return out


attributed = collections.defaultdict(set)     # address -> {shelf grades}
ambiguous = collections.defaultdict(set)      # address -> {grades we REFUSED}
basis = {}                                    # address -> 'cell' | 'sole-row'

for rel in SHELVES:
    with open(os.path.join(KB, rel), encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if not SHELF_GNU.search(line):
                continue
            row_addrs = addrs_in(line)
            if not row_addrs:
                continue
            cells = line.split("|") if "|" in line else [line]
            claimed_here = set()
            # rule 1: same cell
            for cell in cells:
                toks = SHELF_GNU.findall(cell)
                if not toks:
                    continue
                for a in addrs_in(cell):
                    attributed[a].update(toks)
                    basis.setdefault(a, "cell")
                    claimed_here.add(a)
            # rule 2: sole address in the row
            if len(row_addrs) == 1:
                a = row_addrs[0]
                attributed[a].update(SHELF_GNU.findall(line))
                basis.setdefault(a, "sole-row")
                claimed_here.add(a)
            # rule 3: everything else is refused, and counted
            for a in row_addrs:
                if a not in claimed_here:
                    ambiguous[a].update(SHELF_GNU.findall(line))

grades = {r["addr"]: r for r in json.load(open("sweep.json"))}
pop = sorted(attributed)
refused_only = sorted(set(ambiguous) - set(attributed))

print(f"line-level population (first run):  481")
print(f"cell-attributed population:         {len(pop)}")
print(f"refused as AMBIGUOUS (no direct attribution anywhere): {len(refused_only)}")

# Where the first run's 99 actually came from, MEASURED rather than asserted:
# re-attribution changes the CLAIM SET of an address, not just the population.
line_claims = collections.defaultdict(set)
for rel in SHELVES:
    with open(os.path.join(KB, rel), encoding="utf-8", errors="replace") as fh:
        for line in fh:
            toks = SHELF_GNU.findall(line)
            if toks:
                for a in addrs_in(line):
                    line_claims[a].update(toks)
narrowed = [a for a in attributed if line_claims[a] - attributed[a]]
print(f"addresses whose claim set SHRANK under cell attribution: {len(narrowed)}")
print(f"addresses dropped entirely: {len(refused_only)}\n")

rows, tally = [], collections.Counter()
for addr in pop:
    shelf_claims = sorted(attributed[addr])
    g = grades.get(addr)
    if not g:
        continue
    # `sweep.json`'s `verdict` field holds the first run's COMPARISON verdict,
    # not the read verdict -- the first script overwrote one with the other.
    # Readability is therefore taken from the recorded payload itself.
    if g["verdict"].startswith("UNCHECKABLE") or not g["served"]:
        verdict = g["verdict"] if g["verdict"].startswith("UNCHECKABLE") \
            else "UNCHECKABLE/NO_PAYLOAD"
    else:
        served, cs = g["served"], fv.canon(g["served"])
        cclaims = {fv.canon(c) for c in shelf_claims}
        bare = {c for c in shelf_claims if c.upper() in BARE}
        if cs in cclaims:
            verdict = "AGREE"
        else:
            sf = re.match(r"^(AGPL|LGPL|GPL)-(\d\.\d)$", cs or "")
            claim_fams = {m.group(1) for m in
                          (re.match(r"^(AGPL|LGPL|GPL)", c) for c in cclaims) if m}
            if sf and sf.group(1) in claim_fams:
                # same family, different or absent version
                versioned = {c for c in cclaims
                             if re.match(r"^(AGPL|LGPL|GPL)-\d\.\d$", c)
                             and c.startswith(sf.group(1))}
                verdict = "UNDER_SPECIFIED" if (bare and not versioned) else "VERSION_DISAGREE"
            else:
                verdict = "FAMILY_DISAGREE"
    tally[verdict.split("/")[0]] += 1
    rows.append({**g, "shelf_claims": shelf_claims, "verdict2": verdict,
                 "basis": basis.get(addr, "")})

print("=== VERSION_DISAGREE -- shelf states a version, payload serves another ===")
for r in rows:
    if r["verdict2"] == "VERSION_DISAGREE":
        print(f"  {r['addr']:46} shelf={','.join(r['shelf_claims']):16} "
              f"served={r['served']:10} fwd={r['fwd']:9} [{r['basis']}] "
              f"{r['bytes']}B {r['sha']}")

print("\n=== FAMILY_DISAGREE (cell-attributed, so these survive re-attribution) ===")
for r in rows:
    if r["verdict2"] == "FAMILY_DISAGREE":
        print(f"  {r['addr']:46} shelf={','.join(r['shelf_claims']):16} "
              f"served={r['served'][:34]:34} [{r['basis']}] {r['bytes']}B {r['sha']}")

print(f"\n--- {len(rows)} cell-attributed cells ---")
for k, v in tally.most_common():
    print(f"  {k:22} {v:4}  {100.0*v/len(rows):5.1f} %")

out = os.path.join(KB, "evidence", "gnu-version-axis.2026-10-26-p455.tsv")
with open(out, "w") as fh:
    fh.write("address\tshelf_claims\tattribution_basis\tserved\tforward_grant\t"
             "verdict\tbytes\tsha\tat\n")
    for r in rows:
        fh.write("\t".join([r["addr"], "|".join(r["shelf_claims"]), r["basis"],
                            r["served"], r["fwd"], r["verdict2"],
                            str(r["bytes"]), r["sha"], r["at"]]) + "\n")
    fh.write("\n# refused as AMBIGUOUS (adjacency only, no cell-level attribution):\n")
    for a in refused_only:
        fh.write(f"# {a}\t{'|'.join(sorted(ambiguous[a]))}\n")
print(f"evidence -> {out}")
