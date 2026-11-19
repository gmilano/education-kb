#!/usr/bin/env python3
"""p920 — the CELL-LEVEL licence divergence sweep.  Discharges `919-G3`; controls `919-G9`.

`919-F1` established that the duplicate-ROW class does not exist on this shelf (786 row-subjects,
zero repeats inside one table) and that the live class is one table away: **the same repository
carried in two tables with licence CELLS that disagree**.  `919-F2` is the instance —
`PrairieLearn` read `AGPL-3.0 (CE) + proprietary EE` at `verticals/solutions.md` L141 and
`MIT + AGPL-3.0 conjunction` at L193.

`919-G9` measured why no existing gate sees it: `gate-shelf-consistency` compares licence
*tokens*, and BOTH those cells contain `AGPL-3.0`, so they register as agreement.  🔵 The rule
this instrument is built on: **compare the token SET of each cell, and treat a cell whose set is a
strict superset of another's as a DIVERGENCE, not as agreement.**  That is the single decision
that separates this sweep from the gate it replaces.

Two further rules inherited from this base's own history:
  • `918-G4`/`919-F1` — a row's SUBJECT is the FIRST repository address in the row.  A slug the row
    merely *talks about* is not the subject.  Without this the sweep raises `OpenJudge`'s prose
    mention of `AI-for-Education/pedagogy-benchmark` as a defect, which it is not.
  • `919-G4` — `noncommercial` appearing inside a stock GPL/AGPL body is not a licence term.  No
    token in VOCAB matches on it, so this instrument cannot reproduce `918-G0`.

OFFLINE CONTROL (`make -f ... ` or `--selftest`): the fixture is this base's own archived
pre-fix tree.  `compose/code/p920-cell-divergence/fixtures/verticals-solutions.p918.md` is `verticals/solutions.md`
 at commit `8bc72dd` (`p918`), the last tree in which the divergence was live.  It carries the
PrairieLearn divergence that `p918`/`p919` later fixed.  An instrument that does not fail on that
file is not trusted, and `--selftest` exits non-zero if it does not fire.
"""
import re, sys, collections

VOCAB = [
    ("AGPL-3.0", r"\bAGPL[- ]?3(\.0)?\b|\bAFFERO\b"),
    ("GPL-3.0",  r"(?<!A)\bGPL[- ]?3(\.0)?\b"),
    ("GPL-2.0",  r"(?<!A)\bGPL[- ]?2(\.0)?\b"),
    ("LGPL",     r"\bLGPL\b"),
    ("MIT",      r"\bMIT\b"),
    ("Apache-2.0", r"\bApache[- ]?2(\.0)?\b"),
    ("BSD",      r"\bBSD\b"),
    ("MPL",      r"\bMPL\b|\bMozilla Public\b"),
    ("ECL-2.0",  r"\bECL[- ]?2(\.0)?\b|\bEducational Community\b"),
    ("CC0-1.0",  r"\bCC0\b"),
    ("CC-BY-SA", r"\bCC[- ]BY[- ]SA\b"),
    ("CC-BY-NC", r"\bCC[- ]BY[- ]NC\b"),
    ("CC-BY",    r"\bCC[- ]BY(?![- ](SA|NC))\b"),
    ("ODbL-1.0", r"\bODbL\b"),
    ("PROPRIETARY", r"\bproprietary\b|\bEnterprise Edition\b|\bEE\b"),
    ("NONE",     r"\bno licence file\b|\bno license file\b|\bungranted\b|NO-LICENCE-FILE-FOUND"),
]
SLUG = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9._-]*)/([A-Za-z0-9][A-Za-z0-9._-]*)")

NEG = re.compile(r"(?:\bNOT\b|\bnot\b|\bno longer\b|\bnever\b|\bisn't\b|\bis not\b|≠|\brather than\b)[^.;|]{0,24}$")

def polarity(cell, start):
    """919-G3's prescribed token-SET comparison cannot see the live defect, because a cell that
    says `NOT MIT` and a cell that says `MIT` both contain the token `MIT` (p920 `920-F1`).
    Polarity is read from the <=24 characters immediately before the token."""
    return "¬" if NEG.search(cell[:start]) else ""

def tokens(cell):
    """The polarity-tagged token SET — what 919-G3 asked for, corrected for negation."""
    return {polarity(cell, m.start()) + name
            for name, pat in VOCAB
            for m in [re.search(pat, cell, re.I)] if m}

def signature(cell):
    """The polarity-tagged token SEQUENCE, with multiplicity and order.  920-F1 measured that the
    SET is still not enough: `AGPL-3.0 (CE) + proprietary EE` and `MIT + AGPL-3.0 conjunction,
    plus proprietary EE` carry the SAME polarity-tagged set and different grants.  The sequence
    separates them.  🔵 It is deliberately NOT a verdict: a difference here is a row pair a human
    adjudicates, and `report()` prints the precision of the run so the reader can weigh it."""
    hits = []
    for name, pat in VOCAB:
        for m in re.finditer(pat, cell, re.I):
            hits.append((m.start(), polarity(cell, m.start()) + name))
    return tuple(n for _, n in sorted(hits))

def cells_of(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

def sweep(paths):
    # subject -> list of (file, lineno, frozenset(tokens), cell text)
    seen = collections.defaultdict(list)
    for p in paths:
        try:
            lines = open(p, encoding="utf-8").read().splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            if not line.startswith("|"):
                continue
            if re.match(r"^\|[\s:\-|]+\|?$", line):      # separator row
                continue
            m = SLUG.search(line)
            if not m:
                continue
            subject = f"{m.group(1)}/{m.group(2)}".rstrip(".")
            cs = cells_of(line)
            # 920-F2: the licence cell is the LEFTMOST cell carrying a licence token, NOT the
            # densest one.  Picking the densest hands you `Submitty`'s prose cell — which names
            # `Apache-2.0` only to contrast it with Autolab — over its actual `BSD-3-Clause`
            # cell one column to the left.  That is `918-G4`'s subject-versus-mention defect
            # reproduced at CELL level, in this instrument, before its first real run.
            best, best_t = None, set()
            for c in cs:
                if SLUG.search(c):          # the address cell is not the licence cell
                    continue
                t = tokens(c)
                if t:
                    best, best_t = c, t
                    break
            if not best_t:
                continue
            seen[subject].append((p, i, frozenset(best_t), best[:160], signature(best)))
    out = []
    for subject, rows in sorted(seen.items()):
        if len({r[2] for r in rows}) > 1:
            out.append((subject, rows, "SET"))        # differs even as a polarity-tagged set
        elif len({r[4] for r in rows}) > 1:
            out.append((subject, rows, "SEQUENCE"))   # same set, different sequence — 920-F1's class
    return seen, out

def report(paths, label):
    seen, div = sweep(paths)
    print(f"── {label}: {len(seen)} address-bearing rows with a licence cell; "
          f"{len(div)} subject(s) whose cells DIVERGE")
    for subject, rows, kind in div:
        print(f"\n🔴 {subject}   [{kind}]")
        for p, i, t, c, sig in rows:
            print(f"   {p}:{i}  set={{{', '.join(sorted(t))}}}")
            print(f"       seq={' · '.join(sig)}")
            print(f"       {c}")
    return div

if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--selftest":
        fx = "compose/code/p920-cell-divergence/fixtures/verticals-solutions.p918.md"
        div = report([fx], f"OFFLINE CONTROL ({fx})")
        hit = any(s.endswith("PrairieLearn") for s, _, _ in div)
        print(f"\ncontrol: PrairieLearn divergence detected = {hit}")
        sys.exit(0 if hit else 1)
    # ── 921-F10.  THE DEFAULT FILE LIST MADE THIS INSTRUMENT UNUSABLE AS A GATE, and the reason
    # is structural rather than a tuning problem.  `p920` shipped the list above, which includes
    # `repos/trending.md` and `agents/trending.md` — and those two files are **APPEND-ONLY LOGS**.
    # A log's job is to RECORD a superseded cell next to the pass that superseded it, so a cell in
    # the log is SUPPOSED to disagree with the live shelf.  Measured on the p921 tree:
    #     default list (5 files):          4,169 rows → 206 diverging subjects
    #     delivery shelves only (3 files):   463 rows →   4 diverging subjects
    #     of the 206, subjects involving a trending log:  205
    # 🔴 So 202 of the 206 are the instrument comparing a delivery cell against its own history and
    # calling it a defect — `919-G0`'s class exactly: a gate generating false work faster than the
    # base generates shelf growth, by comparing live content against something stale.  The four
    # that survive on the delivery shelves are ALL `SEQUENCE`-arm hits with IDENTICAL sets, which
    # `920-R1` already binds as measurements and never failures — i.e. the SET arm is CLEAN.
    # 🔵 A log may still be swept DELIBERATELY by naming it on the command line; it is no longer
    # swept by default, because a gate nobody can read is a gate nobody runs.
    div = report(args or ["agents/top.md", "repos/foundations.md",
                          "verticals/solutions.md"], "LIVE SHELF (delivery files only — 921-F10)")
    sys.exit(1 if div else 0)
