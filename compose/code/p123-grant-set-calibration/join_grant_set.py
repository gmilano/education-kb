#!/usr/bin/env python3
"""Score the KB's licence claims against the GRANT SET (ACTION X / ACTION Z).

THE MODEL CHANGE, AND WHY IT IS THE WHOLE POINT. Every licence census in this
KB from p114 to p122 compared a published claim against ONE token: the first
grant file that returned 200. p122 then measured its own prose census at a
95 % false-positive rate and proved the cause was structural -- these pages
record grants PER ARTIFACT ("MIT code / CC BY-NC-SA data", "MIT
(LICENSE-CODE) - LICENSE is CC-BY-4.0 for docs"), so a one-token comparison
is less precise than the text it audits and must manufacture disagreements.

Here a repository's grant is a SET. A claim AGREES when its token appears
ANYWHERE in the set. That single change is what makes the per-artifact prose
this KB writes verifiable instead of punishable.

VERDICTS
  AGREES        claim token is in the grant set
  AGREES-SPLIT  the set holds SPLIT:<claim>, i.e. the file says so itself
  NO-GRANT      the tree has no readable grant file and the page names one
  DEFECT        the claim names a licence the tree does not grant anywhere
  CORRECTED     a DEFECT on a row already carrying the ACTION V marker
  UNMEASURABLE  the address was never measured

usage: join_grant_set.py CLAIMS_TSV GRANTS_TSV > verdicts.tsv
"""
import re
import sys
from collections import defaultdict

EQ = {
    "mit": "mit",
    "apache-2.0": "apache-2.0", "apache 2.0": "apache-2.0", "apache2": "apache-2.0",
    "agpl-3.0": "agpl-3.0", "agpl-3": "agpl-3.0", "agplv3": "agpl-3.0",
    "gpl-3.0": "gpl-3.0", "gplv3": "gpl-3.0",
    "gpl-2.0": "gpl-2.0", "gplv2": "gpl-2.0",
    "lgpl-3.0": "lgpl-3.0", "lgplv3": "lgpl-3.0", "lgpl-2.1": "lgpl-2.1",
    "bsd-3-clause": "bsd-3-clause", "bsd-2-clause": "bsd-2-clause",
    "mpl-2.0": "mpl-2.0", "epl-2.0": "epl-2.0", "ecl-2.0": "ecl-2.0",
    "eupl-1.2": "eupl-1.2", "eupl-1.1": "eupl-1.1",
    "elastic license": "elastic-2.0", "elastic-2.0": "elastic-2.0",
    "cc by-nc-sa": "cc-by-nc-sa-4.0", "cc-by-nc-sa-4.0": "cc-by-nc-sa-4.0",
    "cc by-sa": "cc-by-sa-4.0", "cc-by-sa-4.0": "cc-by-sa-4.0",
    "cc by 4.0": "cc-by-4.0", "cc-by-4.0": "cc-by-4.0",
    "isc": "isc", "unlicense": "unlicense",
}


def norm(tok):
    t = tok.strip().lower()
    # An EUPL grant that admits later versions satisfies a claim naming
    # EITHER the floor version or a later one, so it normalises to a set.
    if t.startswith("eupl-") and t.endswith("-or-later"):
        return "eupl-or-later"
    return EQ.get(t, t)


def grant_tokens(rows):
    """The SET of tokens a repository grants, over every grant file."""
    toks = set()
    for _path, tok in rows:
        n = norm(tok)
        if tok.startswith("SPLIT:"):
            toks.add("split:" + norm(tok[6:]))
            toks.add(norm(tok[6:]))
        elif tok.startswith("SPLIT-REF:"):
            for arm in tok[10:].split("+"):
                toks.add(norm(arm))
        elif tok.startswith("REF:"):
            for arm in tok[4:].split("+"):
                toks.add(norm(arm))
        else:
            toks.add(n)
    return toks


def main(claims_p, grants_p):
    gset = defaultdict(list)
    for row in open(grants_p, encoding="utf-8"):
        parts = row.rstrip("\n").split("\t")
        if len(parts) != 5:
            continue
        addr, _br, path, _b, tok = parts
        gset[addr.lower()].append((path, tok))

    counts = defaultdict(int)
    for row in open(claims_p, encoding="utf-8"):
        parts = row.rstrip("\n").split("\t", 5)
        if len(parts) != 6:
            continue
        page, line, addr, claim, dist, ctx = parts
        rows = gset.get(addr.lower())
        if not rows:
            v = "UNMEASURABLE"
        else:
            toks = grant_tokens(rows)
            c = norm(claim)
            if toks == {"no-file"}:
                v = "NO-GRANT"
            elif c in toks:
                v = "AGREES"
            elif "split:" + c in toks:
                v = "AGREES-SPLIT"
            elif c.startswith("eupl") and "eupl-or-later" in toks:
                v = "AGREES"
            else:
                v = "CORRECTED" if "<!--corrected-->" in ctx else "DEFECT"
        counts[v] += 1
        if v in ("DEFECT", "NO-GRANT", "CORRECTED"):
            paths = ",".join(f"{p}={t}" for p, t in sorted(gset.get(addr.lower(), [])))
            print(f"{v}\t{page}\t{line}\t{addr}\t{claim}\t{paths}\t{ctx[:160]}")
    for k in sorted(counts):
        print(f"# {k}={counts[k]}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
