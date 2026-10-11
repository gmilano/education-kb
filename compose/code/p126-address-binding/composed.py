#!/usr/bin/env python3
"""The composed assertion: ACTION AJ's binding under ACTION AK's SETs.

p125 left AJ and AK as independent pre-registrations. They are one mechanism:

  * AJ alone is REFUTED as a CAUSE -- it explains 3 of the 15 violations its
    clause attributed to it, not 12.
  * AK alone is REFUTED as a REMEDY -- an unbound address-level set hands
    `pyBKT`'s MIT to `catsim` and clears 9 live false claims.
  * Composed, AK clears its 6 and keeps catsim's 9.

So the assertion is restated once, with both: a token is superseded for an
address when a marked row BINDS it to that address and no marked row binds the
same token to it as a surviving value; and a page violates the assertion when
it BINDS a superseded token to that address outside a marked span.

Offline. usage: composed.py PAGE...
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p125-retraction-cue"))
import binding                                             # noqa: E402
import grant_set                                           # noqa: E402
import repair_search                                       # noqa: E402
from correction_form import in_marked, marked_regions, norm_token  # noqa: E402


def violations(paths, pairs):
    """repair_search.violations with co-occurrence replaced by binding."""
    by_addr = {}
    for (addr, tok) in pairs:
        by_addr.setdefault(addr, set()).add(norm_token(tok))
    out = []
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                regions = marked_regions(line)
                for at, tok, addr in binding.bind(line):
                    if not addr or in_marked(line, at, regions):
                        continue
                    if norm_token(tok) in by_addr.get(addr, ()):
                        out.append((path, ln, addr, norm_token(tok),
                                    line.strip()[:150]))
    return out


def main(pages):
    pairs = grant_set.repaired_pairs(pages)
    vs = violations(pages, pairs)
    print("# repaired pairs = %d over %d addresses"
          % (len(pairs), len({a for a, _ in pairs})))
    seen = set()
    for path, ln, addr, tok, txt in vs:
        if (path, ln, addr, tok) in seen:
            continue
        seen.add((path, ln, addr, tok))
        print("VIOLATION\t%s:%d\t%s\t%s" % (path, ln, addr, tok))
    print("# violations = %d over %d addresses"
          % (len(seen), len({v[2] for v in vs})))
    by_addr = {}
    for path, ln, addr, tok, _ in vs:
        by_addr.setdefault((addr, tok), set()).add("%s:%d" % (path, ln))
    print("#")
    for (addr, tok), where in sorted(by_addr.items(),
                                     key=lambda kv: -len(kv[1])):
        print("# %-44s %-14s %d rows" % (addr, tok, len(where)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
