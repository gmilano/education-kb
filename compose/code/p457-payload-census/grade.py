#!/usr/bin/env python3
"""Grade each measured payload family against the family the shelves CLAIM for that address.

The claim is read LINE-LOCALLY: these shelves are markdown tables, so the licence token on the
same line as the address is that address's cell. A line-local read is why p452's three false
DISAGREE verdicts happened on a different axis (it derived an address from a package NAME); here
the address is literal and the risk is the opposite one -- a line carrying two addresses. Those
are counted and excluded rather than guessed at.
"""
import json, re, sys, collections

SHELVES = ["agents/top.md", "repos/foundations.md", "verticals/solutions.md"]
SLUG_RE = re.compile(r'github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?:\.git)?(?=[)\s>"\'`,;\]]|/|$)')
FAMILIES = [
    ("AGPL-3.0", r"\bAGPL-?3(\.0)?\b|\bAGPLv3\b"),
    ("LGPL-3.0", r"\bLGPL-?3(\.0)?\b|\bLGPLv3\b"),
    ("LGPL-2.1", r"\bLGPL-?2\.1\b"),
    ("GPL-3.0",  r"(?<!A)(?<!L)\bGPL-?3(\.0)?\b|(?<!A)(?<!L)\bGPLv3\b"),
    ("GPL-2.0",  r"(?<!A)(?<!L)\bGPL-?2(\.0)?\b|(?<!A)(?<!L)\bGPLv2\b"),
    ("Apache-2.0", r"\bApache-?2(\.0)?\b"),
    ("BSD-3-Clause", r"\bBSD-?3-?Clause\b"),
    ("BSD-2-Clause", r"\bBSD-?2-?Clause\b"),
    ("MPL-2.0", r"\bMPL-?2(\.0)?\b"),
    ("ECL-2.0", r"\bECL-?2(\.0)?\b"),
    ("Unlicense", r"\bUnlicense\b"),
    ("ISC", r"\bISC\b"),
    ("CC", r"\bCC-?BY\b|\bCC0\b|\bODbL\b"),
    ("MIT", r"\bMIT\b"),
]
# A family the payload reader returns as equivalent to a claimed one
EQUIV = {("BSD", "BSD-3-Clause"), ("BSD-3-Clause", "BSD"),
         ("BSD", "BSD-2-Clause"), ("BSD-2-Clause", "BSD")}

def claims():
    out = collections.defaultdict(set)
    multi = collections.Counter()
    for f in SHELVES:
        for line in open(f, encoding="utf-8"):
            slugs = {m.group(1) for m in SLUG_RE.finditer(line)}
            if not slugs:
                continue
            fams = [fam for fam, rx in FAMILIES if re.search(rx, line)]
            if not fams:
                continue
            if len(slugs) > 1:
                for s in slugs:
                    multi[s] += 1      # ambiguous line: recorded, never graded
                continue
            out[next(iter(slugs))].add(fams[0])   # first (most specific) family wins
    return out, multi

def main():
    measured = json.load(open(sys.argv[1]))
    cl, multi = claims()
    tally = collections.Counter()
    rows = []
    for slug, rec in sorted(measured.items()):
        if slug not in cl:
            continue
        if slug in multi and slug not in cl:
            continue
        claimed = sorted(cl[slug])
        got = rec.get("family")
        v = rec["verdict"]
        if v == "ADDRESS_DEAD":
            verdict = "DEAD_BUT_CLAIMED"
        elif v == "REPO_LIVE_NO_GRANT":
            verdict = "CLAIM_WITHOUT_PAYLOAD"
        elif got == "UNCLASSIFIED":
            verdict = "UNREAD_BY_INSTRUMENT"
        elif got in claimed or any((got, c) in EQUIV for c in claimed):
            verdict = "AGREE"
        else:
            verdict = "DISAGREE"
        tally[verdict] += 1
        rows.append((verdict, slug, "/".join(claimed), got or "", rec.get("bytes", ""),
                     rec.get("sha256_12", ""), rec.get("ref", ""), rec.get("path", "")))
    print(f"graded cells: {sum(tally.values())}   (addresses with a line-local claim)")
    print(f"ambiguous lines excluded (>1 address on the claim line): {len(multi)}")
    for k, n in tally.most_common():
        print(f"  {k:24s} {n}")
    print()
    for r in sorted(rows):
        if r[0] != "AGREE":
            print("  ", " | ".join(str(x) for x in r))
    with open(sys.argv[2], "w") as fh:
        fh.write("verdict\tslug\tclaimed\tmeasured\tbytes\tsha256_12\tref\tpath\n")
        for r in sorted(rows):
            fh.write("\t".join(str(x) for x in r) + "\n")

if __name__ == "__main__":
    main()
