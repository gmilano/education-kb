#!/usr/bin/env python3
"""ACTION AJ scored against its own clause.

p125 pre-registered: "All 15 violations ACTION AF newly surfaced have one
cause: a cell naming two repositories lets a token co-occur with an address it
does not describe. REFUTED if fewer than 12 of the 15 are explained by
mis-binding."

The 15 are derived, not asserted: they are the records in p125's
`out/ac-after.triples` that are NOT in its `out/ac-baseline.triples`. Both
files were produced in one run, so their line numbers share a coordinate
system and the set difference is exact.

Each is then RELOCATED onto the committed pages by (page, address, token) --
p125's recorded line numbers do not survive its own write (see P126-A) -- and
scored with `binding.explains`.

Offline. usage: score_aj.py BASELINE AFTER PAGE...
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p125-retraction-cue"))
import binding                                             # noqa: E402


def read(path):
    out = []
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            raw = raw.strip()
            if not raw or raw.startswith("#"):
                continue
            where, addr, tok = raw.split("|")
            page, ln = where.rsplit(":", 1)
            out.append((page, int(ln), addr, tok))
    return out


def main(argv):
    base, after, pages = argv[0], argv[1], argv[2:]
    newly = sorted(set(read(after)) - set(read(base)))
    found = binding.relocate(pages)

    print("# newly surfaced by ACTION AF = %d" % len(newly))
    misbound = bound = unlocatable = substring = 0
    rows = []
    seen = {}
    for page, ln, addr, tok in newly:
        key = (page, addr, tok)
        lns = sorted(found.get(key, []))
        i = seen.get(key, 0)
        seen[key] = i + 1
        if i >= len(lns):
            unlocatable += 1
            rows.append(("UNLOCATABLE", page, 0, addr, tok,
                         "no live line carries this pair"))
            continue
        tgt = lns[i]
        with open(os.path.join(page), encoding="utf-8") as fh:
            line = fh.readlines()[tgt - 1]
        mis, why = binding.explains(line, addr, tok)
        if not mis:
            bound += 1
            verdict = "BOUND"
        elif why.startswith("SUBSTRING"):
            substring += 1
            verdict = "SUBSTRING"
        else:
            misbound += 1
            verdict = "MISBOUND"
        rows.append((verdict, page, tgt, addr, tok, why))

    for verdict, page, tgt, addr, tok, why in rows:
        print("%-11s\t%s:%d\t%s\t%s\t%s"
              % (verdict, page, tgt, addr, tok, why))
    print("#")
    print("# explained by MIS-BINDING = %d" % misbound)
    print("# SUBSTRING artefacts      = %d" % substring)
    print("# genuinely BOUND          = %d" % bound)
    print("# unlocatable              = %d" % unlocatable)
    clause = 12
    print("# clause: refuted if fewer than %d of %d are mis-binding"
          % (clause, len(newly)))
    print("# VERDICT: %s"
          % ("DISCHARGED, NOT REFUTED" if misbound >= clause
             else "DISCHARGED, REFUTED"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
