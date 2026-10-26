#!/usr/bin/env python3
"""p456 -- re-read the grant at the RESOLVED default branch for the 15 carried
cells whose default branch is outside the ref list every carried pass guessed.

For each: what the resolver reads at the default branch, and -- separately --
what the carried ladder WOULD have read, by walking `p455`'s own ref list in
`p455`'s own order. The gap between those two columns is the defect.
"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor

import resolve
from family_version import family, only_or_later
from fetch import raw, digest, GRANT_PATHS

CARRIED_REFS = ["HEAD", "main", "master", "develop", "dev", "development", "trunk"]


def carried_read(owner_repo):
    """`p455/fetch.grant()`'s ref order, reproduced, to show what it saw."""
    for ref in CARRIED_REFS:
        for path in GRANT_PATHS:
            st, body = raw(owner_repo, ref, path)
            if st == 200 and body.strip():
                return (ref, path, len(body), digest(body),
                        body.decode("utf-8", "replace"))
    return (None, None, 0, "", "")


def one(addr):
    g = resolve.grant(addr)
    cr_ref, cr_path, cr_b, cr_sha, cr_text = carried_read(addr)
    return {
        "addr": addr,
        "default": g.get("default", ""),
        "verdict": g["verdict"],
        "res_ref": g.get("ref", ""), "res_path": g.get("path", ""),
        "res_bytes": g.get("bytes", 0), "res_sha": g.get("sha", ""),
        "res_family": family(g.get("text", "")) if g.get("text") else "",
        "car_ref": cr_ref or "", "car_path": cr_path or "",
        "car_bytes": cr_b, "car_sha": cr_sha,
        "car_family": family(cr_text) if cr_text else "",
    }


if __name__ == "__main__":
    addrs = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    with ThreadPoolExecutor(max_workers=6) as ex:
        recs = list(ex.map(one, addrs))
    json.dump(recs, open(sys.argv[2], "w"), indent=1)
    hdr = f"{'addr':48} {'default':26} {'verdict':20} {'resolved':34} {'carried ladder saw':34} {'same?'}"
    print(hdr); print("-" * len(hdr))
    for r in sorted(recs, key=lambda r: r["addr"]):
        res = f"{r['res_family'] or '-':12} {r['res_ref']:12}/{r['res_path'] or '-'}"
        car = f"{r['car_family'] or '-':12} {r['car_ref'] or '-':12}/{r['car_path'] or '-'}"
        same = "SAME" if (r["res_sha"] and r["res_sha"] == r["car_sha"]) else "DIFFER"
        print(f"{r['addr']:48} {r['default']:26} {r['verdict']:20} {res:34} {car:34} {same}")
