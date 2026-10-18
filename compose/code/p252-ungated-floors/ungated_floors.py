"""p252 / `ACTION XR` — floor the unittest suites OUTSIDE the gate.

What `p251` left, and the number it got wrong
---------------------------------------------
`p251` discharged `ACTION XM` by finding that five of the gate's own controls run
through `unittest.main()`, which **exits `0` on zero collected tests and on
all-skipped**, and that those same five were the only lines whose `stderr` the gate
discarded — `stderr` being where `Ran 0 tests` appears. It floored those five and
registered `ACTION XR` for the rest, sized as *"`344` instruments on disk, `23`
referenced by the `Makefile`, so `321` are ungated and unfloored"*.

🔴 **That `321` is not the exposure, and this instrument measures why.** A directory
is not a suite. `p252` counts the artefact that can actually lie:

    347  instrument directories on disk (346 before this instrument was added, 347 with it)
    201  python test files in them
     20  gated — reached by a `Makefile` recipe (19 before this instrument, 20 with it)
    181  ungated
     71  of the 181 run `unittest.main()`      <- the silent-zero population
    110  of the 181 signal failure explicitly  <- cannot pass while asserting nothing

So the population at risk is **`71`**, not `321`: the other `110` ungated suites raise
or `sys.exit` on failure and are immune to the silent-zero mode by construction.

🟢 **And the second measurement is the one that decides how urgent this is: `0` of the
`71` collect zero tests today.** The defect is LATENT, not active. Nothing on these
shelves is currently resting on a suite that asserts nothing. What the `71` are exposed
to is a FUTURE edit — a method rename, a class dropped, a mass `@skip` — landing with no
signal at all, which is exactly how `p250`'s `lazy_lint.py` and `p251`'s five controls
got there.

Why a generated floor table rather than 71 numbers in Python
-------------------------------------------------------------
`p251` pinned its five floors as literals, which is right for five. Hand-writing `71`
would itself be the drift surface: a floor nobody can regenerate is a floor that gets
edited to match a broken suite. So the pins live in `floors.tsv`, written by `--pin`
and checked by `--verify`, and `--verify` is what the gate runs. A suite whose static
`def test_*` count drops below its pinned floor fails the gate by name.

🔵 The classifier is IMPORTED from `p251-gate-exit-reach`, never re-implemented here, so
`suite_signal`'s measured shell/python asymmetry cannot diverge between the two
instruments. The one thing this module adds is the ENUMERATION.
"""

from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE_ROOT = os.path.dirname(HERE)
REPO_ROOT = os.path.dirname(os.path.dirname(CODE_ROOT))
FLOORS_TSV = os.path.join(HERE, "floors.tsv")

sys.path.insert(0, os.path.join(CODE_ROOT, "p251-gate-exit-reach"))
from gate_reach import (  # noqa: E402  — imported, never re-implemented
    FLOORS as GATE_FLOORS,
    collected_tests,
    silent_zero,
    suite_signal,
)

TEST_FILE = re.compile(r"^test_.*\.py$")

HEADER = ("relpath", "signal", "collected", "floor", "verdict")

V_OK = "OK"
V_BELOW = "BELOW-FLOOR"
V_UNPINNED = "UNPINNED"
V_ZERO = "COLLECTS-ZERO"


def makefile_text(repo_root: str = None) -> str:
    """The gate's own recipes. Missing `Makefile` is an error, not an empty gate."""
    path = os.path.join(repo_root or REPO_ROOT, "Makefile")
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def is_gated(relpath: str, mk: str) -> bool:
    """True when a `Makefile` recipe reaches this test file.

    Matching on the FILE, not the directory: `p251`'s `321` came from counting
    directories, and a directory can hold a gated suite beside an ungated one.

    🔴 p280, AND THE CENSUS FOUND IT ON ITSELF.  A BARE BASENAME IS NOT A FILE EITHER.
    `p280` added `pass280-package-provenance/test_provenance.py` to `make hooks`, and this
    predicate immediately credited `p791-registry-id-provenance/test_provenance.py` -- a
    different suite, in a different directory, that NO recipe runs -- as gated, because the
    two share a basename.  The pinned population moved by two for one added suite, which is
    how it surfaced: `gated 37 -> 39`, `ungated 181 -> 180`.
    🔵 That is `p251-prefix-collision`'s class (a short token colliding onto a real subject)
    arriving inside the instrument that measures gating, and it is this docstring's own
    lesson one step finer: `p251` moved from the DIRECTORY to the FILE, and the move from
    the FILE to its BASENAME was never made.
    🟢 A recipe reaches a suite when ONE LINE names both its DIRECTORY and its BASENAME --
    which is the shape every recipe in this Makefile actually has, in both of its forms
    (`cd compose/code/X && $(PY) test_y.py`, and `$(PY) -I compose/code/X/test_y.py`).
    A directory alone still does not gate, so `p251`'s finding is preserved.
    """
    if relpath in GATE_FLOORS:
        return True
    if relpath in mk:
        return True
    base = os.path.basename(relpath)
    folder = os.path.basename(os.path.dirname(relpath))
    if not folder:
        return base in mk
    for line in mk.splitlines():
        if base in line and folder in line:
            return True
    return False


def walk(code_root: str = None):
    """Yield `(relpath, source)` for every python test file under `compose/code`."""
    root = code_root or CODE_ROOT
    for d in sorted(os.listdir(root)):
        dpath = os.path.join(root, d)
        if not os.path.isdir(dpath):
            continue
        for fn in sorted(os.listdir(dpath)):
            if not TEST_FILE.match(fn):
                continue
            with open(os.path.join(dpath, fn), encoding="utf-8", errors="replace") as fh:
                yield d + "/" + fn, fh.read()


def census(code_root: str = None, mk: str = None):
    """The whole population, classified. Returns a list of dicts."""
    mk = makefile_text() if mk is None else mk
    out = []
    for rel, src in walk(code_root):
        sig = suite_signal(src, "python")
        out.append(
            {
                "relpath": rel,
                "signal": sig,
                "collected": collected_tests(src),
                "silent_zero": silent_zero(sig),
                "gated": is_gated(rel, mk),
            }
        )
    return out


def ungated_silent_zero(rows):
    """The `ACTION XR` population: ungated AND able to pass while asserting nothing."""
    return [r for r in rows if r["silent_zero"] and not r["gated"]]


def read_floors(path: str = None) -> dict:
    path = path or FLOORS_TSV
    floors = {}
    if not os.path.exists(path):
        return floors
    with open(path, encoding="utf-8") as fh:
        for i, line in enumerate(fh):
            parts = line.rstrip("\n").split("\t")
            if i == 0 and parts[0] == "relpath":
                continue
            if len(parts) < 3 or not parts[0]:
                continue
            floors[parts[0]] = int(parts[2])
    return floors


def verdict_for(row: dict, floors: dict) -> str:
    """`COLLECTS-ZERO` outranks everything: it is the defect itself, not the pin."""
    if row["collected"] == 0:
        return V_ZERO
    floor = floors.get(row["relpath"])
    if floor is None:
        return V_UNPINNED
    return V_OK if row["collected"] >= floor else V_BELOW


def verify(floors: dict = None, rows: dict = None):
    """`(failures, table)` — a failure is anything but `OK`."""
    rows = ungated_silent_zero(census()) if rows is None else rows
    floors = read_floors() if floors is None else floors
    table, failures = [], []
    for r in sorted(rows, key=lambda x: x["relpath"]):
        v = verdict_for(r, floors)
        table.append((r["relpath"], r["signal"], r["collected"],
                      floors.get(r["relpath"], ""), v))
        if v != V_OK:
            failures.append((r["relpath"], v))
    return failures, table


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--verify"
    rows = census()
    pop = ungated_silent_zero(rows)

    if mode == "--census":
        print("instrument_dirs\t%d" % len([d for d in os.listdir(CODE_ROOT)
                                          if os.path.isdir(os.path.join(CODE_ROOT, d))]))
        print("python_test_files\t%d" % len(rows))
        print("gated\t%d" % sum(1 for r in rows if r["gated"]))
        print("ungated\t%d" % sum(1 for r in rows if not r["gated"]))
        print("ungated_silent_zero\t%d" % len(pop))
        print("ungated_explicit\t%d" % sum(
            1 for r in rows if not r["gated"] and not r["silent_zero"]))
        print("collects_zero\t%d" % sum(1 for r in pop if r["collected"] == 0))
        return 0

    if mode == "--pin":
        with open(FLOORS_TSV, "w", encoding="utf-8") as fh:
            fh.write("\t".join(("relpath", "signal", "floor")) + "\n")
            for r in sorted(pop, key=lambda x: x["relpath"]):
                fh.write("%s\t%s\t%d\n" % (r["relpath"], r["signal"], r["collected"]))
        print("pinned %d floors -> %s" % (len(pop), FLOORS_TSV))
        return 0

    if mode == "--table":
        _, table = verify(rows=pop)
        print("\t".join(HEADER))
        for row in table:
            print("\t".join(str(c) for c in row))
        return 0

    failures, table = verify(rows=pop)
    print("ACTION XR — %d ungated silent-zero suites, %d pinned, %d failing"
          % (len(pop), len(read_floors()), len(failures)))
    for rel, v in failures:
        print("  %-12s %s" % (v, rel))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
