#!/usr/bin/env python3
"""ACTION AA + AD over the harvested grant corpus.

Reads the cache `grant_set.sh` built and emits two TSVs:

  out/action-aa.tsv   address, branch, path, p123 token, p124 shape verdict
  out/action-ad.tsv   address, branch, path, p123 token, resolved CC token

Offline: reads only files already on disk. No network, no clock.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cc_version                      # noqa: E402
import split_shape                     # noqa: E402
from classify_licence import classify   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "out", "cache")
OUT = os.path.join(HERE, "out")


def cache_path(addr, p):
    return os.path.join(CACHE, addr.replace("/", "~") + "__" + p.replace("/", "~"))


def read(addr, p):
    fp = cache_path(addr, p)
    try:
        with open(fp, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return None


def main():
    rows = []
    with open(os.path.join(CACHE, "hits.tsv"), encoding="utf-8") as fh:
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) == 3:
                rows.append(parts)

    aa, ad = [], []
    for addr, br, p in rows:
        text = read(addr, p)
        if text is None:
            continue
        tok = classify(text, p)

        # ---- ACTION AA: does the SHAPE say split where p123's token did not?
        is_split, lics, nb = split_shape.split_by_shape(text)
        p123_split = tok.startswith("SPLIT")
        if is_split and not p123_split:
            aa.append((addr, br, p, tok, "SHAPE-SPLIT:" + "+".join(lics), str(nb)))
        elif is_split and p123_split:
            aa.append((addr, br, p, tok, "AGREES:" + "+".join(lics), str(nb)))

        # ---- ACTION AD: resolve a bare CC token to a version
        if tok == "CC" or tok.endswith(":CC") or tok == "GPL-UNTITLED":
            r = cc_version.resolve(text)
            ad.append((addr, br, p, tok, r or "NOT-CC"))

    with open(os.path.join(OUT, "action-aa.tsv"), "w", encoding="utf-8") as fh:
        for r in sorted(aa):
            fh.write("\t".join(r) + "\n")
    with open(os.path.join(OUT, "action-ad.tsv"), "w", encoding="utf-8") as fh:
        for r in sorted(ad):
            fh.write("\t".join(r) + "\n")

    changed = [r for r in aa if r[4].startswith("SHAPE-SPLIT")]
    # A row RESOLVES when it reaches a versioned CC token. `NOT-CC` is a
    # correct rejection, not a resolution, and `*UNVERSIONED` is an honest
    # failure; neither counts toward ACTION AD's clause.
    resolved = [r for r in ad
                if r[4] != "NOT-CC" and "UNVERSIONED" not in r[4]]
    print("ACTION AA: %d addresses change verdict, %d agree with p123"
          % (len({r[0] for r in changed}), len({r[0] for r in aa if r[4].startswith('AGREES')})))
    bare = [r for r in ad if r[3] == "CC"]
    print("ACTION AD: %d of %d bare-CC grants resolved to a version "
          "(%d candidates read in total, %d correctly rejected as NOT-CC)"
          % (len([r for r in resolved if r[3] == "CC"]), len(bare),
             len(ad), len([r for r in ad if r[4] == "NOT-CC"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
