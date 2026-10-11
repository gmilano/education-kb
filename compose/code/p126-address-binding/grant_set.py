#!/usr/bin/env python3
"""ACTION AK -- grant-as-a-SET, and why it cannot be done without ACTION AJ.

p125 pre-registered AK: "A correction table that collapses a split grant into
one token (`pupilfirst` 'published CC-BY-SA-4.0 -> corrected MIT', where the
truth is MIT + CC-BY-SA-4.0 on `docs/`) makes the surviving split member read
as superseded on 6 live rows. REFUTED if treating the old and new values as
SETS does not clear all 6."

p125 computes the live set PER LINE: a token marked on a row is superseded
unless the SAME row carries it unmarked. A split grant is published one member
per row, so the row reading `CC-BY-SA-4.0 -> MIT` never sees the `docs/`
member and reports the survivor as stale.

The fix is an address-level NEW SET. Two subtleties decide whether it works:

  1. Only CORRECTION RECORDS may contribute -- rows carrying the marker. A
     union over every line would LAUNDER stale rows: a page still asserting
     the superseded token would itself make that token "live".

  2. The contribution must be BOUND, not co-occurring. Run with
     `--no-bind` this module reproduces the failure that makes the point:
     `compose/patterns.md` carries

         | mastery | `CAHLR/pyBKT` + `douglasrizzo/catsim` | ... |
         | 🟢 **MIT** (`pyBKT`) + **BSD-3-Clause** (`catsim`)
           ⚠️ **was 🟢 MIT both**<!--corrected--> |

     and an unbound union hands `MIT` -- true of `pyBKT` -- to `catsim` as a
     surviving set member. That clears `catsim`'s superseded `MIT`, which is
     the defect p125 called the one worth the pass. AK without AJ re-opens it.

Offline. usage: grant_set.py [--no-bind] PAGE...
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p125-retraction-cue"))
import binding                                             # noqa: E402
import repair_search                                       # noqa: E402
from correction_form import (MARKER, in_marked, marked_regions,  # noqa: E402
                             norm_token, vocab)

BIND = True


def _attributed(line):
    """-> (inside, outside) as {(address, raw token)} for a marked row."""
    regions = marked_regions(line)
    addrs = repair_search.addrs_on(line)
    inside, outside = set(), set()
    if BIND:
        for at, tok, addr in binding.bind(line):
            if not addr:
                continue
            (inside if in_marked(line, at, regions) else outside).add(
                (addr, tok))
    else:
        for m in vocab().finditer(line):
            bucket = (inside if in_marked(line, m.start(), regions)
                      else outside)
            for addr in addrs:
                bucket.add((addr, m.group(0)))
    return inside, outside


def new_sets(paths):
    """-> {address: {normalised surviving token}} from MARKED rows only."""
    sets = {}
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if MARKER not in line:
                    continue
                _, outside = _attributed(line)
                for addr, tok in outside:
                    sets.setdefault(addr, set()).add(norm_token(tok))
    return sets


def repaired_pairs(paths):
    survives = new_sets(paths)
    pairs = {}
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                if MARKER not in line:
                    continue
                inside, _ = _attributed(line)
                for addr, tok in inside:
                    if norm_token(tok) in survives.get(addr, set()):
                        continue
                    pairs.setdefault((addr, tok), []).append(
                        "%s:%d" % (path, ln))
    return pairs


def main(argv):
    global BIND
    if "--no-bind" in argv:
        BIND = False
        argv = [a for a in argv if a != "--no-bind"]
    pages = argv
    before = repair_search.repaired_pairs(pages)
    after = repaired_pairs(pages)
    v_before = repair_search.violations(pages, before)
    v_after = repair_search.violations(pages, after)

    print("# binding = %s" % ("ON (AK over AJ)" if BIND else "OFF (AK alone)"))
    print("# repaired pairs   per-line=%d  address-SET=%d"
          % (len(before), len(after)))
    print("# violations       per-line=%d  address-SET=%d"
          % (len(v_before), len(v_after)))

    def key(vs):
        return {(p, a, t) for p, _, a, t, _ in vs}

    for p, a, t in sorted(key(v_before) - key(v_after)):
        print("CLEARED\t%s\t%s\t%s" % (p, a, t))
    for p, a, t in sorted(key(v_after) - key(v_before)):
        print("REGRESSED\t%s\t%s\t%s" % (p, a, t))

    pupil_b = [r for r in v_before if r[2] == "pupilfirst/pupilfirst"
               and r[3] == "CC-BY-SA-4.0"]
    pupil_a = [r for r in v_after if r[2] == "pupilfirst/pupilfirst"
               and r[3] == "CC-BY-SA-4.0"]
    cats_b = [r for r in v_before if r[2] == "douglasrizzo/catsim"
              and r[3] == "MIT"]
    cats_a = [r for r in v_after if r[2] == "douglasrizzo/catsim"
              and r[3] == "MIT"]
    print("#")
    print("# pupilfirst / CC-BY-SA-4.0  (AK's quarry)   before=%d after=%d"
          % (len(pupil_b), len(pupil_a)))
    print("# catsim / MIT  (must NOT be laundered)      before=%d after=%d"
          % (len(cats_b), len(cats_a)))
    print("# clause: refuted if the SET rule does not clear all 6")
    ok = len(pupil_b) >= 6 and not pupil_a and len(cats_a) == len(cats_b)
    print("# VERDICT: %s" % ("DISCHARGED, NOT REFUTED" if ok
                             else "DISCHARGED, REFUTED"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
