#!/usr/bin/env python3
"""p456 -- `Gap 455-A` settled at population scale, for free.

`Gap 455-A` asserts: "HEAD on raw.githubusercontent does NOT follow the
repository's default branch." It was inferred from ONE repository
(`kurwjan/LanisAPI`) by comparing two README byte-counts, and on the strength
of it `p455` rewrote the ladder to keep walking refs and accept any grant it
found -- which is how a withdrawn grant reached the shelves.

The claim is testable without a single extra request. `git ls-remote --symref`
returns, in one response, BOTH the commit HEAD points at AND the commit every
branch points at. So "does HEAD follow the default branch?" is just
`head_sha == head_shas[default]`, asked over the whole carried population.
"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor

import resolve


def one(addr):
    default, heads, tags, head_sha, head_shas = resolve.ls_remote(addr, want_sha=True)
    if default is None and not heads:
        return {"addr": addr, "class": "ADDRESS_DEAD"}
    agree = bool(default and head_sha and head_shas.get(default) == head_sha)
    return {"addr": addr, "class": "HEAD_IS_DEFAULT" if agree else "HEAD_DIVERGES",
            "default": default or "", "head_sha": head_sha[:12],
            "default_sha": (head_shas.get(default or "") or "")[:12],
            "n_heads": len(heads)}


if __name__ == "__main__":
    addrs = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    with ThreadPoolExecutor(max_workers=12) as ex:
        recs = list(ex.map(one, addrs))
    json.dump(recs, open(sys.argv[2], "w"), indent=1)
    tally = {}
    for r in recs:
        tally[r["class"]] = tally.get(r["class"], 0) + 1
    live = [r for r in recs if r["class"] != "ADDRESS_DEAD"]
    print(f"population {len(recs)}  live {len(live)}")
    for k in sorted(tally, key=lambda k: -tally[k]):
        print(f"  {k:18} {tally[k]:4}")
    div = [r for r in recs if r["class"] == "HEAD_DIVERGES"]
    print(f"\nHEAD diverges from the resolved default branch: {len(div)} of {len(live)} live")
    for r in div:
        print(f"  {r['addr']:48} default={r['default']:24} HEAD={r['head_sha']} default={r['default_sha']}")
