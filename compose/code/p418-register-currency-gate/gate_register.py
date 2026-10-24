#!/usr/bin/env python3
"""p418 — ACTION p417-D: the gap register's CURRENCY, made a standing control.

Register staleness has now failed FOUR times on this base — `p411` once (repaired
by `p412`) and `p414`, `p415`, `p416` consecutively (backfilled by `p417`, which
registered `ACTION p417-D` asking for exactly this gate).  A failure that recurs
four times is not a discipline problem, it is a missing control (`P237`: a usage
contract you have to REMEMBER is not a control).

The contract, as `ACTION p417-D` states it:

    if the newest `## 🆕 \\`pN\\`` header in `intel/open-gaps.md` is older than the
    newest on `agents/top.md`, the register is stale and the gate is red.

Generalised one step, because the register owes currency to every live shelf and
not only to `agents/top.md`: the register's newest pass number must be >= the
newest pass number on ANY shelf it is measured against.

Findings:
  P418-REGISTER-STALE   register's newest pass < a shelf's newest pass
  P418-NO-HEADER        a file carries no `## 🆕 `pN`` header at all
  P418-NO-INPUT         called with fewer than two paths (p541: measuring
                        nothing is not a clean tree)

TSV on stdout.  Exit 1 if there are findings, 2 on refusal.

Usage: gate_register.py REGISTER SHELF [SHELF ...]
"""
import re
import sys

# `## 🆕 \`p417\` · 2026-10-24 — ...`  The pass number is the FIRST backticked
# `pN` on an h2 marked 🆕.  Anchored at line start so a quoted header inside a
# table cell or a blockquote cannot be mistaken for a section of this file.
HEADER = re.compile(r"^## +🆕 +`p(\d+)`")


def newest(lines):
    """Highest pass number among this file's own 🆕 h2 headers, or None."""
    ns = [int(m.group(1)) for m in (HEADER.match(l) for l in lines) if m]
    return max(ns) if ns else None


def check(register_path, register_lines, shelves):
    """shelves: [(path, lines)].  Returns a list of finding tuples."""
    found = []
    reg = newest(register_lines)
    if reg is None:
        found.append((register_path, "P418-NO-HEADER", 0,
                      "the register carries no `## 🆕 `pN`` header, so its currency "
                      "cannot be established"))
    for path, lines in shelves:
        shelf = newest(lines)
        if shelf is None:
            found.append((path, "P418-NO-HEADER", 0,
                          "shelf carries no `## 🆕 `pN`` header"))
            continue
        if reg is not None and reg < shelf:
            found.append((register_path, "P418-REGISTER-STALE", 0,
                          f"register newest=p{reg}; {path} newest=p{shelf}; "
                          f"stale by {shelf - reg} pass(es)"))
    return found


def main(argv):
    if len(argv) < 2:
        print(
            "P418-NO-INPUT\tREFUSED: this gate compares a REGISTER against one or "
            "more SHELVES and needs at least two paths.  A run that measured "
            "nothing is not a clean tree (p541).  "
            "Usage: gate_register.py intel/open-gaps.md agents/top.md [...]",
            file=sys.stderr,
        )
        return 2
    read = lambda p: open(p, encoding="utf-8").read().split("\n")
    register, shelf_paths = argv[0], argv[1:]
    rows = check(register, read(register), [(p, read(p)) for p in shelf_paths])
    print("file\tfinding\tline\tdetail")
    for r in rows:
        print("\t".join(str(x) for x in r))
    print(f"#\ttotal\t{len(rows)}")
    return 1 if rows else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
