#!/usr/bin/env python3
"""Score proximity-attributed prose claims against measured licences."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from join_claims import is_correction, norm, verdict  # noqa: E402

EQ_EXTRA = {"ecl-2.0": "ecl-2.0", "eupl-1.2": "eupl-1.2",
            "cc by-nc-sa": "cc-by-nc-sa-4.0", "cc by-sa": "cc-by-sa-4.0",
            "cc by 4.0": "cc-by-4.0"}


def n2(tok):
    return EQ_EXTRA.get(tok.strip().lower(), norm(tok))


def main(scratch):
    measured = {}
    with open(os.path.join(scratch, "prox-measured.tsv"), encoding="utf-8") as fh:
        for row in fh:
            a, b, p, by, tok = row.rstrip("\n").split("\t")
            measured[a.lower()] = tok

    buckets = {"DEFECT": [], "CORRECTION": [], "SPLIT-OK": [], "UNMEASURABLE": []}
    for row in open(os.path.join(scratch, "claims-prox.tsv"), encoding="utf-8"):
        page, line, addr, claim, dist, ctx = row.rstrip("\n").split("\t", 5)
        tok = measured.get(addr.lower())
        if tok is None:
            continue
        v = verdict(claim, tok) if n2(claim) == norm(claim) else (
            "AGREES" if n2(claim) == n2(tok) else verdict(claim, tok))
        if v == "UNMEASURABLE":
            buckets["UNMEASURABLE"].append((page, line, addr, claim, tok, ctx))
        elif v in ("AGREES", "AGREES-SPLIT"):
            continue
        elif v == "AGREES-REF":
            buckets["SPLIT-OK"].append((page, line, addr, claim, tok, ctx))
        elif is_correction(ctx):
            buckets["CORRECTION"].append((page, line, addr, claim, tok, ctx))
        else:
            buckets["DEFECT"].append((page, line, addr, claim, tok, ctx))

    for k, rows in buckets.items():
        for r in rows:
            print(k + "\t" + "\t".join(r))
    for k, rows in buckets.items():
        print(f"# {k}={len(rows)}", file=sys.stderr)
    addrs = {r[2].lower() for r in buckets["DEFECT"]}
    print(f"# DEFECT distinct addresses={len(addrs)}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1])
