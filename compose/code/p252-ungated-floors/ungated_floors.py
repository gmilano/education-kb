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


# 🟢 p284 (`p283` item 1, an EIGHT-pass streak): derive the census, stop typing it.
#
# `p283` registered this: *"The remedy is not 'remember next time', which is what eight
# passes have now tried: it is to DERIVE these three literals from the Makefile instead
# of typing them."*  This is that derivation, and writing it exposed WHY the streak ran
# for eight passes — which is a sharper finding than the streak.
#
# 🔴 THE THREE LITERALS WERE PINNING THE WRONG POPULATION.  `--verify` already fails on
# `UNPINNED`, so a newly added suite that is ungated AND silent-zero — the only shape
# `ACTION XR` exists to catch — was ALREADY caught, by name, with no literal involved.
# What the literals added on top of that was a count of FILES ON DISK.  In all eight
# reds the added suite arrived INSIDE `make hooks` (p261, p262, p275, p277, p278, p279,
# p280, p283 all say so in their own notes above: *"`ungated` stays at 181"*).  So eight
# consecutive passes were stopped by a red gate over a change that moved the exposure by
# ZERO.  A gate that fires on every change and on no risk trains the reader to bump the
# number, which is precisely what eight passes did.
#
# 🟢 What the literals DID uniquely protect, and what is kept: `is_gated` itself.  `p280`
# found that predicate crediting an unrun suite only because `gated` moved by two for one
# added suite.  That detection does not need a typed number — it needs a SECOND, INDEPENDENT
# reading of the gate's reach to disagree with the first.  `derive_gated` is that second
# reading, and it is written in the opposite direction on purpose: `is_gated` walks DISK
# FILES and asks the Makefile "does a line reach me?", while `derive_gated` walks MAKEFILE
# LINES and asks disk "which file did I just name?".  Set equality between the two is
# therefore a real cross-check and not a tautology, and it carries no literal that a pass
# has to remember.
#
# 🔵 A recipe reaches a suite two ways, and both are honoured here, so "derived from the
# Makefile" is stated precisely: a Makefile LINE naming it, or `p251`'s in-gate floor
# registry (`gate_reach.FLOORS`), which the gate reads directly rather than through a
# recipe.  Omitting the second would make the two readings disagree by exactly those five.
_DERIVE_PATH = re.compile(r"(?:compose/code/)?([A-Za-z0-9_.-]+)/(test_[A-Za-z0-9_.-]*\.py)")
_DERIVE_DIR = re.compile(r"compose/code/([A-Za-z0-9_.-]+)")
_DERIVE_BASE = re.compile(r"(test_[A-Za-z0-9_.-]*\.py)")


def derive_from_recipes(mk: str, on_disk) -> set:
    """The suites the `Makefile` RECIPES reach, read from the recipes OUTWARD.

    The inverse of `is_gated`.  `is_gated(relpath, mk)` starts from a file and searches
    the recipes; this starts from the recipes and emits files, then keeps only those that
    exist.  The `on_disk` filter is what makes the direction matter: a line naming a
    directory and a basename that do not combine into a real file contributes NOTHING
    here, while `is_gated` would never have been asked about it.

    Both recipe forms in this Makefile are covered:
      `cd compose/code/X && $(PY) test_y.py`      -> directory and basename, one line
      `$(PY) -I compose/code/X/test_y.py`         -> an explicit relative path
    A directory alone gates nothing (`p251`) and a bare basename alone gates nothing
    (`p280`): neither form can produce a relpath without the other half, so both findings
    are preserved here as behaviour rather than as a count that moves.

    🔵 This reads the RECIPES ONLY, deliberately.  `derive_gated` adds `p251`'s in-gate
    floor registry on top.  Keeping them separate is what lets the controls test this
    reading in isolation — the first version of this function unioned the registry
    unconditionally, and four controls could then not express "this Makefile text reaches
    nothing", because five registry suites came back on every call.
    """
    on_disk = set(on_disk)
    out = set()
    for line in mk.splitlines():
        for folder, base in _DERIVE_PATH.findall(line):
            rel = folder + "/" + base
            if rel in on_disk:
                out.add(rel)
        folders = set(_DERIVE_DIR.findall(line))
        bases = set(_DERIVE_BASE.findall(line))
        for folder in folders:
            for base in bases:
                rel = folder + "/" + base
                if rel in on_disk:
                    out.add(rel)
    return out


def derive_gated(mk: str, on_disk) -> set:
    """The gate's FULL reach: the recipes, plus `p251`'s in-gate floor registry.

    🔵 "Derived from the Makefile" has to be stated precisely, because a recipe is not the
    only way the gate reaches a suite: `gate_reach.FLOORS` is read by the gate directly.
    Omitting those five would make this reading disagree with `is_gated` by exactly them —
    a false finding manufactured by the instrument, which is the class `p281` logged three
    times in one pass.
    """
    on_disk = set(on_disk)
    return derive_from_recipes(mk, on_disk) | {r for r in GATE_FLOORS if r in on_disk}


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

    if mode == "--derive":
        # p284: the census with NO typed literal in it. `python_test_files` is a disk
        # enumeration, `gated` is the Makefile read outward, `ungated` is the remainder,
        # and `agree` is the cross-check that replaces the three pins.
        disk = {r["relpath"] for r in rows}
        pred = {r["relpath"] for r in rows if r["gated"]}
        drv = derive_gated(makefile_text(), disk)
        print("python_test_files\t%d" % len(disk))
        print("gated_predicate\t%d" % len(pred))
        print("gated_derived\t%d" % len(drv))
        print("ungated\t%d" % (len(disk) - len(pred)))
        print("agree\t%s" % ("YES" if pred == drv else "NO"))
        for rel in sorted(pred - drv):
            print("  PREDICATE-ONLY\t%s" % rel)
        for rel in sorted(drv - pred):
            print("  DERIVED-ONLY\t%s" % rel)
        return 0 if pred == drv else 1

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
