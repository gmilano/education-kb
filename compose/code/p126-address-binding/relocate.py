#!/usr/bin/env python3
"""P126-A: can this corpus's committed evidence be found again on its pages?

p125 committed `out/ac-after.triples` -- 36 `path:line|address|token`
records, the residue of its own ACTION AC assertion. Every one of those line
numbers is wrong on the committed page, because p125 ran the instrument and
THEN prepended its pass section to each page it had just measured.

The test is deliberately not "guess the offset". It recomputes the violation
set from scratch with p125's own code and compares the two sets twice:

  * keyed on (path, address, token) -- the ADDRESS-keyed identity
  * keyed on (path, line, address, token) -- the LINE-keyed identity

If the first agrees and the second does not, the finding is dislocation and
nothing else: the same claims, at coordinates the pass itself invalidated.

Offline. usage: relocate.py TRIPLES PAGE...
"""
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "p125-retraction-cue"))
import correction_form                                     # noqa: E402
import repair_search                                       # noqa: E402


def read_triples(path):
    """`agents/top.md:163|pupilfirst/pupilfirst|CC-BY-SA-4.0`"""
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


def recompute(pages):
    pairs = repair_search.repaired_pairs(pages)
    return [(p, ln, a, t) for p, ln, a, t, _ in
            repair_search.violations(pages, pairs)]


def line_names(page, ln, addr, root="."):
    """Does the RECORDED line actually name the address it is filed under?"""
    full = os.path.join(root, page)
    try:
        with open(full, encoding="utf-8") as fh:
            lines = fh.readlines()
    except OSError:
        return None
    if not 1 <= ln <= len(lines):
        return False
    return addr.lower() in repair_search.addrs_on(lines[ln - 1])


def main(argv):
    triples_path, pages = argv[0], argv[1:]
    root = os.path.dirname(os.path.abspath(triples_path))
    for _ in range(4):                         # instrument dir -> repo root
        root = os.path.dirname(root)
    committed = read_triples(triples_path)
    fresh = recompute(pages)

    c_addr = {(p, a, t) for p, _, a, t in committed}
    f_addr = {(p, a, t) for p, _, a, t in fresh}
    c_line = set(committed)
    f_line = set(fresh)

    dislocated = [r for r in committed if line_names(r[0], r[1], r[2], root)
                  is False]

    print("# committed records      = %d" % len(committed))
    print("# recomputed violations  = %d" % len(fresh))
    print("# ADDRESS-keyed  committed=%d fresh=%d  identical=%s"
          % (len(c_addr), len(f_addr), c_addr == f_addr))
    print("# LINE-keyed     committed=%d fresh=%d  identical=%s"
          % (len(c_line), len(f_line), c_line == f_line))
    print("# recorded lines that do NOT name their own address = %d of %d"
          % (len(dislocated), len(committed)))
    for p, ln, a, t in sorted(dislocated):
        print("DISLOCATED\t%s:%d\t%s\t%s" % (p, ln, a, t))

    # The per-page shift, measured rather than assumed.
    print("#")
    by_page = {}
    for p, ln, a, t in fresh:
        by_page.setdefault(p, []).append((a, t, ln))
    for p in sorted(by_page):
        olds = sorted(ln for q, ln, a, t in committed if q == p)
        news = sorted(ln for _, _, ln in by_page[p])
        if len(olds) == len(news) and olds:
            shifts = {n - o for o, n in zip(olds, news)}
            print("SHIFT\t%s\t%s\trecords=%d"
                  % (p, sorted(shifts), len(olds)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
