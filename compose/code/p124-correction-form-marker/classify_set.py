#!/usr/bin/env python3
"""Classify every cached grant file. One python process for the whole set.

usage: classify_set.py HITS_TSV CACHE_DIR
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify_licence import classify  # noqa: E402


def main(hits, cache):
    with open(hits, encoding="utf-8") as fh:
        for row in fh:
            parts = row.rstrip("\n").split("\t")
            if len(parts) != 3:
                continue
            addr, br, path = parts
            fn = os.path.join(cache, addr.replace("/", "~") + "__" + path.replace("/", "~"))
            try:
                with open(fn, "rb") as g:
                    raw = g.read()
            except OSError:
                continue
            text = raw.decode("utf-8", "replace")
            print(f"{addr}\t{br}\t{path}\t{len(raw)}\t{classify(text, path)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
