#!/usr/bin/env python3
"""The ACTION AC assertion, re-measured against ACTION AF's marker.

For every repair this corpus records -- (address, superseded token) harvested
from a MARKED span -- no page may carry that token on a line naming that
address outside a marked span. p124 measured 27 violations over 15 addresses
with forms 1/2/3/9 marked. p125 adds forms 4-8 and re-measures.

Offline. usage: repair_search.py FILE...   (exit 1 if any violation)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import correction_form                                     # noqa: E402
from correction_form import (MARKER, in_marked,  # noqa: E402
                             marked_regions, norm_token, vocab)

ADDR = re.compile(r"github\.com/([A-Za-z0-9][\w.-]*/[A-Za-z0-9][\w.-]*)")


def addrs_on(line):
    """p124 took the raw match; a trailing `.`/`,`/`)` is punctuation, not a
    repository name, and folding it makes two spellings of one address."""
    raw = ADDR.findall(line)
    if correction_form.BASELINE:
        return {a.lower() for a in raw}
    return {a.lower().rstrip(".,);") for a in raw}


def repaired_pairs(paths):
    pairs = {}
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                if MARKER not in line:
                    continue
                addrs = addrs_on(line)
                if not addrs:
                    continue
                regions = marked_regions(line)
                inside, outside = set(), set()
                for m in vocab().finditer(line):
                    (inside if in_marked(line, m.start(), regions)
                     else outside).add(m.group(0))
                live = {norm_token(t) for t in outside}
                for tok in inside:
                    if norm_token(tok) in live:
                        continue      # an omission corrected, not a token
                    for addr in addrs:
                        pairs.setdefault((addr, tok), []).append(
                            "%s:%d" % (path, ln))
    return pairs


def violations(paths, pairs):
    out = []
    by_addr = {}
    for (addr, tok) in pairs:
        by_addr.setdefault(addr, set()).add(tok)
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                addrs = addrs_on(line)
                if not addrs:
                    continue
                regions = marked_regions(line)
                for addr in sorted(addrs):
                    for tok in sorted(by_addr.get(addr, ())):
                        hit = False
                        for m in re.finditer(r"\b" + re.escape(tok) + r"\b",
                                             line):
                            if not in_marked(line, m.start(), regions):
                                hit = True
                                break
                        if hit:
                            out.append((path, ln, addr, tok,
                                        line.strip()[:150]))
                            break
    return out


def main(argv):
    paths = [a for a in argv if not a.startswith("-")]
    if "--baseline" in argv:
        correction_form.BASELINE = True
    pairs = repaired_pairs(paths)
    vs = violations(paths, pairs)
    print("# repaired pairs=%d over %d addresses"
          % (len(pairs), len({a for a, _ in pairs})))
    for path, ln, addr, tok, txt in vs:
        print("VIOLATION\t%s:%d\t%s\t%s\t%s" % (path, ln, addr, tok, txt))
    print("# violations=%d over %d addresses"
          % (len(vs), len({v[2] for v in vs})))
    return 1 if vs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
