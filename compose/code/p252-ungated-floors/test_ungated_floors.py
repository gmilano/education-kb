"""p252 / `ACTION XR` controls — stdlib only, no network, no dependencies.

Run from this directory:  python3 -I test_ungated_floors.py

🔴 This suite signals failure with an explicit non-zero exit, NOT `unittest.main()` —
because the defect it exists to catch is `unittest.main()` exiting `0` on zero collected
tests. A silent-zero runner guarding the silent-zero census would be `p250`'s
`lazy_lint.py` all over again: a control that cannot fail, watching for controls that
cannot fail.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ungated_floors as uf

FAILS = []
RUN = [0]


def chk(name, got, want):
    RUN[0] += 1
    if got != want:
        FAILS.append("%s\n     got:  %r\n     want: %r" % (name, got, want))
        print("FAIL %s" % name)
    else:
        print("ok   %s" % name)


ROWS = uf.census()
POP = uf.ungated_floors = uf.ungated_silent_zero(ROWS)
FLOORS = uf.read_floors()

# ── the census: the population ACTION XR asked to be NAMED, not just counted ──
# p253: 201 -> 204 and 20 -> 23.  Three instruments landed (`p253-captured-body-census`,
# `p253-settled-fact-regression`, `p253-gate-propagation`), each with an explicit-exit suite and each wired into
# `make hooks`, so the census and the gated count both move by three.  🔵 An absolute count
# pinned as a literal is a maintenance cost p252 chose knowingly; it is also what caught
# this pass's own additions, which is the behaviour wanted.
# p254: 204 -> 205 and 23 -> 24.  TWO instruments landed (`p254-exit-status-reach`,
# `p254-scoped-grant-reference`) and THREE gate steps, but only ONE is a python test file:
# `p254-scoped-grant-reference`'s suite is bash, and the third step runs `exit_reach.py
# --verify`, which is a verifier and not a suite.  🔵 Said explicitly because the two counts
# moved by DIFFERENT amounts for the first time; a later pass reading "+2 instruments, +1
# file" as an arithmetic error would be re-deriving this note.
# p255: +1 file and +1 gated — `p255-channel-reachability` (ACTION YE) entered the gate
# in the same pass it was written, so both literals move together this time.
# p256: +1 file and +1 gated — `pass256-ladder-closure`, likewise written and gated in one
# pass.  TWO gate steps landed but only ONE is a python TEST file: the second runs
# `ladder_closure.py --verify`, which is the p254 shape (a verifier is not a suite), so the
# `gated` literal counts the suite and not the verifier.  The `ungated` figure does NOT move.
# p257: +1 file and +1 gated — `pass257-restriction-scan`, written and gated in one pass.
# 🟢 Worth recording that THIS suite is what caught the new instrument: `make hooks` went
# red on `p252` the moment the step was wired, before the pass had typed a single shelf
# row.  A census pin that moves is the gate working, not the gate breaking.
# p259: +1 file and +1 gated — `pass259-grant-location-class`, written and gated in one
# pass, and this pin went red again the moment the step was wired.  Third consecutive pass
# where the census caught the new instrument before any shelf row was typed; the `ungated`
# figure stays at 181 because the suite arrived already inside `make hooks`.
# 🔴 p261: 210 -> 212 and 29 -> 31, and the TWO-step jump is the finding of the pass.
# `pass260-ecosystem-manifest-tier` was written and wired into `make hooks` at p260 and
# this pin was NOT moved, so `gate-offline` has been RED since that commit — exactly the
# behaviour the note above calls "the gate working".  🔴 Nobody saw it, because p251,
# p252 and p260 all recorded `make` as not runnable from their session and so never ran
# the gate they were extending.  p261 ran it: `make hooks` executes fine from a cloned
# checkout, and it exited `2` at this suite with `got 211 / want 210`.
# 🔵 The lesson is not about the pin.  Three passes declared a gap ("`make hooks` was NOT
# runnable") that was a property of one session and inherited it as a property of the
# base — p254's *the base inherits its own conclusions about what is impossible*, with
# the consequence that the standing gate was red for a full pass and read as unknown.
# p261 itself adds `pass261-current-state-tier-run` (+1 file, +1 gated), which is why
# both literals move by two here and `ungated` stays at 181: both suites arrived gated.
# 🟢 p275: 213 -> 214 and 32 -> 33.  `p275-tree-enumeration`'s suite is written AND gated
# (`make gate-enumeration`, in `hooks`), so both counts move together -- which is the shape
# this census is for: a suite that lands ungated moves only the first number.
# 🟢 p262: 212 -> 213 and 31 -> 32.  `pass262-scoped-reservation-audit` is written and
# wired into `make hooks` IN THE SAME CHANGE as this pin, which is the whole remedy
# p261 asked for: the pin moves with the step, not a pass later.  `ungated` stays at
# 181 because the suite arrived gated.
# 🟢 p277: 214 -> 215 and 33 -> 34.  `p277-table-structure` is written AND wired into
# `make hooks` (`make gate-tables`) in the SAME change as this pin -- the p262 shape and
# p261's remedy, so the census never spends a pass red.  `ungated` stays at 181 and the
# `71`/`110` partition is untouched because the suite arrived gated and exits explicitly
# (`sys.exit(1)`), so it never joins the silent-zero population.
# 🔵 And it went red exactly as designed: `gate-offline` failed at THIS suite the moment
# `gate-tables` was wired, before a single table-structure finding had been written up.
# Fifth consecutive pass where this census catches the new instrument first.
# 🟢 p278: 215 -> 217 and 34 -> 36.  `p278-channel-conflict` ships TWO suites
# (`test_direction.py`, `test_conflict_gate.py`), both wired into `make hooks` via
# `make gate-conflict` IN THE SAME CHANGE as this pin -- p262's shape, p261's remedy, so the
# census never spends a pass red.  `ungated` stays at 181 and the `71`/`110` partition is
# untouched: both suites arrive gated and exit explicitly (`sys.exit(1)`), so neither joins
# the silent-zero population.
# 🔵 Sixth consecutive pass where this census catches the new instrument first.
# 🟢 p279: 217 -> 218 and 36 -> 37.  `p279-absence-claims` ships ONE suite
# (`test_absence_claims.py`), wired into `make hooks` via `make gate-absence` IN THE SAME
# CHANGE as this pin -- p261's remedy again, so the census never spends a pass red.
# `ungated` stays at 181 and the `71`/`110` partition is untouched: the suite arrives gated
# and exits explicitly (`sys.exit(1)`), so it never joins the silent-zero population.
# 🔵 SEVENTH consecutive pass where this census catches the new instrument first, and the
# STREAK is the finding rather than the arithmetic: seven passes running, no pass has added
# an instrument and remembered this pin without the census going red first.
chk("python test files on disk", len(ROWS), 218)
chk("gated by a Makefile recipe", sum(1 for r in ROWS if r["gated"]), 37)
chk("ungated", sum(1 for r in ROWS if not r["gated"]), 181)
chk("ungated AND silent-zero (the XR population)", len(POP), 71)
chk("ungated AND explicit-exit (immune by construction)",
    sum(1 for r in ROWS if not r["gated"] and not r["silent_zero"]), 110)
chk("the partition closes: silent-zero + explicit == ungated",
    len(POP) + sum(1 for r in ROWS if not r["gated"] and not r["silent_zero"]),
    sum(1 for r in ROWS if not r["gated"]))
chk("no row is both gated and in the population",
    [r["relpath"] for r in POP if r["gated"]], [])

# 🟢 The measurement that decides urgency: the defect is LATENT, not active.
chk("suites collecting ZERO tests today", [r["relpath"] for r in POP if r["collected"] == 0], [])

# ── the pins ──
chk("every member of the population is pinned",
    sorted(r["relpath"] for r in POP if r["relpath"] not in FLOORS), [])
chk("the pin file holds no row outside the population",
    sorted(set(FLOORS) - {r["relpath"] for r in POP}), [])
chk("no floor is zero (a zero floor pins nothing)",
    sorted(k for k, v in FLOORS.items() if v < 1), [])
chk("floors.tsv is the pinned count of the population", len(FLOORS), 71)

# ── verdict_for: the grading, and its precedence ──
chk("a count at the floor is OK",
    uf.verdict_for({"relpath": "x/test_x.py", "collected": 5}, {"x/test_x.py": 5}), uf.V_OK)
chk("a count above the floor is OK",
    uf.verdict_for({"relpath": "x/test_x.py", "collected": 9}, {"x/test_x.py": 5}), uf.V_OK)
chk("a RENAMED method drops below the floor",
    uf.verdict_for({"relpath": "x/test_x.py", "collected": 4}, {"x/test_x.py": 5}), uf.V_BELOW)
chk("an unpinned suite is UNPINNED, not OK",
    uf.verdict_for({"relpath": "new/test_new.py", "collected": 3}, {}), uf.V_UNPINNED)
chk("COLLECTS-ZERO outranks the floor",
    uf.verdict_for({"relpath": "x/test_x.py", "collected": 0}, {"x/test_x.py": 5}), uf.V_ZERO)
chk("COLLECTS-ZERO outranks UNPINNED",
    uf.verdict_for({"relpath": "x/test_x.py", "collected": 0}, {}), uf.V_ZERO)

# ── is_gated matches the FILE, not the directory: p251's own conflation ──
_MK = "\tcd compose/code/dir-a && python3 test_one.py\n"
chk("a suite named in a recipe is gated", uf.is_gated("dir-a/test_one.py", _MK), True)
chk("a SIBLING suite in the same directory is NOT gated",
    uf.is_gated("dir-a/test_two.py", _MK), False)
chk("a gate floor from p251 counts as gated",
    uf.is_gated("p1054-mit-plus-clause/test_mit_plus.py", ""), True)

# ── the classifier is IMPORTED from p251, never re-implemented here ──
sys.path.insert(0, os.path.join(uf.CODE_ROOT, "p251-gate-exit-reach"))
import gate_reach  # noqa: E402

chk("suite_signal is p251's own function", uf.suite_signal is gate_reach.suite_signal, True)
chk("silent_zero is p251's own function", uf.silent_zero is gate_reach.silent_zero, True)
chk("a unittest.main() suite is silent-zero",
    uf.silent_zero(uf.suite_signal("import unittest\nunittest.main()\n", "python")), True)
chk("a sys.exit suite is not",
    uf.silent_zero(uf.suite_signal("import sys\nsys.exit(1 if f else 0)\n", "python")), False)

# ── FAILURE REACHABILITY: p251's lesson — prove it, do not assume it ──
_dropped = dict(FLOORS)
_victim = sorted(FLOORS)[0]
_dropped[_victim] = FLOORS[_victim] + 1000
_fails, _ = uf.verify(floors=_dropped, rows=POP)
chk("an impossible floor makes verify FAIL", [v for _, v in _fails], [uf.V_BELOW])
chk("and it names the suite", [r for r, _ in _fails], [_victim])

_fails_nopin, _ = uf.verify(floors={}, rows=POP)
chk("a MISSING pin file fails as UNPINNED, it does not read as clean",
    len(_fails_nopin), 71)

_clean, _table = uf.verify(floors=FLOORS, rows=POP)
chk("the real population verifies clean", _clean, [])
chk("the table has one row per member", len(_table), 71)

chk("read_floors on a missing path returns empty, not an exception",
    uf.read_floors(os.path.join(uf.HERE, "no-such-file.tsv")), {})

print()
if FAILS:
    print("%d/%d FAILED" % (len(FAILS), RUN[0]))
    for f in FAILS:
        print("  - %s" % f)
    sys.exit(1)
print("%d/%d passed" % (RUN[0], RUN[0]))
