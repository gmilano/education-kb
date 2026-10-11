#!/usr/bin/env python3
"""ACTION AI — join the probe rows and emit the false-permissive verdict.

usage: run_ai.py PROBE_TSV CACHE_DIR > ai-verdict.tsv
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import permissiveness as pm                              # noqa: E402


def main(probe, cache):
    rows = {}
    for line in open(probe, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) != 5:
            continue
        addr, br, which, path, _sz = p
        tok = "NO-FILE"
        if path != "-":
            fp = os.path.join(
                cache, addr.replace("/", "~") + "__" + which + "__"
                + path.replace("/", "~"))
            try:
                with open(fp, encoding="utf-8", errors="replace") as fh:
                    tok = pm.classify(fh.read())
            except OSError:
                tok = "UNREADABLE"
        rows.setdefault(addr, {})[which] = (br, path, tok)

    tally = {}
    print("\t".join(["address", "real_branch", "real_token", "real_tier",
                     "guess_branch", "guess_token", "guess_tier", "verdict"]))
    for addr in sorted(rows):
        r = rows[addr]
        rb, _rp, rt = r.get("real", ("-", "-", "NO-FILE"))
        # A guessing probe tries `main` then `master` and takes the first
        # that answers -- so the guess is that one, not the better of the two.
        guess = None
        for which in ("main", "master"):
            if which in r and r[which][2] not in ("NO-FILE", "UNREADABLE"):
                guess = (which, r[which][2])
                break
        gb, gt = guess if guess else ("-", "NO-FILE")
        v = pm.compare(rt, gt)
        tally[v] = tally.get(v, 0) + 1
        print("\t".join([addr, rb, rt, str(pm.tier(rt)), gb, gt,
                         str(pm.tier(gt)), v]))
    for v in sorted(tally, key=lambda k: -tally[k]):
        print("# %-20s %d" % (v, tally[v]), file=sys.stderr)
    print("# addresses %d" % len(rows), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1], sys.argv[2]))
