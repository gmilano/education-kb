#!/usr/bin/env python3
"""p456 -- the carried-cell ref sweep.

Runs `resolve.ls_remote` over every GitHub address cited on the three primary
shelves (`agents/top.md`, `repos/foundations.md`, `verticals/solutions.md`)
and asks two questions the shelves have never been able to ask:

1. Which addresses are ACTUALLY dead? Every `ADDRESS_DEAD` on these shelves was
   inferred from a 404 sweep over guessed refs x guessed paths. ls-remote
   answers it in one request, authoritatively.

2. For how many carried cells is the resolved default branch OUTSIDE the ref
   list every pass since `p449` guessed? Those are the cells the carried
   instrument could not have read at the default branch AT ALL -- it either
   failed over to some other ref and published that ref's grant as the
   project's, or published a false "ungranted".

`GUESSED` is the exact list from `p455/fetch.py:REFS` plus `p455`'s
`fetch_fast.ALT_REFS`, which is the widest set any carried pass walked.
"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor

import resolve

GUESSED = {"main", "master", "develop", "dev", "development", "trunk"}


def main(path, out):
    addrs = [l.strip() for l in open(path) if l.strip() and "/" in l]
    # one ls-remote per address; the verdict never depends on thread order
    with ThreadPoolExecutor(max_workers=12) as ex:
        rows = list(ex.map(lambda a: (a,) + resolve.ls_remote(a), addrs))

    recs = []
    for addr, default, heads, tags in rows:
        if default is None and not heads:
            cls = "ADDRESS_DEAD"
        elif default is None:
            cls = "NO_SYMREF"           # heads exist, HEAD not symbolic
        elif default in GUESSED:
            cls = "DEFAULT_GUESSABLE"
        else:
            cls = "DEFAULT_OFF_LIST"    # the carried ladder never read this ref
        recs.append({"addr": addr, "default": default or "", "class": cls,
                     "n_heads": len(heads), "n_tags": len(tags),
                     "heads": heads[:40]})

    json.dump(recs, open(out, "w"), indent=1)
    tally = {}
    for r in recs:
        tally[r["class"]] = tally.get(r["class"], 0) + 1
    n = len(recs)
    print(f"population: {n}")
    for k in sorted(tally, key=lambda k: -tally[k]):
        print(f"  {k:20} {tally[k]:4}  {100.0*tally[k]/n:5.1f} %")
    print("\n--- DEFAULT_OFF_LIST: the refs the carried ladder never walked ---")
    off = [r for r in recs if r["class"] == "DEFAULT_OFF_LIST"]
    for r in sorted(off, key=lambda r: r["addr"]):
        print(f"  {r['addr']:52} default={r['default']}")
    print(f"\n--- ADDRESS_DEAD ({tally.get('ADDRESS_DEAD',0)}) ---")
    for r in sorted([r for r in recs if r["class"] == "ADDRESS_DEAD"],
                    key=lambda r: r["addr"]):
        print(f"  {r['addr']}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
