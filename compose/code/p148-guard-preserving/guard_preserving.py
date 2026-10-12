"""p148-guard-preserving -- `ACTION EU`: is the guard wrapper verdict-preserving?

`ACTION EJ` (p147) wired `p146-empty-walk-guard` **around** the five at-risk instruments
rather than editing their bytes, because editing them would have destroyed the "baseline
reproduces" discipline p145 established. 🟢 **`p147-guard-harness` showed the wrapper
refuses on 10 of 10 npm pairs and 2 of 220 clone pairs.** 🔴 **What it never showed is what
the wrapper does on the 218 pairs that DO have input.**

> 🟡 **`ACTION EU`** — test whether the guard harness changes any PUBLISHED figure when the
> five at-risk instruments are run over the full 44-row census, rather than only reporting
> refusals. 🔴 *Refuted if any row's published value changes* — which would mean the wrapper
> is not verdict-preserving on rows that DO have input, and `ACTION EJ`'s "wrap, do not
> rewrite" answer is unsafe as implemented.

🔵 **The falsifier is inverted relative to the others on this shelf, and that is deliberate.**
Here a *silent* falsifier is the good outcome: it means the wrapper adds refusals and changes
nothing else.

## Method -- the instrument's own verdict function, twice

For each (instrument, row) pair this module calls the instrument's **published verdict
entry point** -- the same `row()` / `survey()` / `is_mcp_server()` the figures on these
pages came from -- and compares:

| run | what it is |
|---|---|
| `bare` | the entry point called directly, as the published pass called it |
| `guarded` | the same call, but only after `walked_or_refuse` says the enumeration saw files |

A pair is `PRESERVED` when the enumeration is non-empty and the two runs are equal;
`REFUSED` when the guard declines (the enumeration is empty); and 🔴 `CHANGED` when both
ran and disagree -- the state that refutes the action.

    python3 guard_preserving.py <clone-dir>
    python3 test_guard_preserving.py     # 9 tests, authored fixtures, offline
"""

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p146-empty-walk-guard"))
from walk_guard import walked_or_refuse, WALKED            # noqa: E402

# (label, module rel path, enumeration attr, exclusion attr, verdict entry point)
SUBJECTS = [
    ("p141-surface-gate", "p141-agent-surface-gate/surface_gate.py",
     "walk", None, "is_mcp_server"),
    ("p143-surface-gate2", "p143-surface-gate-repair/surface_gate2.py",
     "walk", "SKIP_DIRS", "is_mcp_server"),
    ("p142-americas", "p142-americas-disambiguation/americas.py",
     "source_files", "SKIP_DIR", "hosts_in"),
    ("p142-schema-tiers", "p142-schema-location-tiers/schema_tiers.py",
     "tracked", "EXCLUDE", "survey"),
    ("p143-tenancy", "p143-vendor-tenancy/tenancy.py",
     "source_files", "SKIP_DIR", "scan"),
]


def load(rel):
    path = os.path.normpath(os.path.join(HERE, "..", rel))
    name = "instr_" + os.path.basename(path)[:-3].replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def freeze(value):
    """A comparable, printable rendering of whatever an entry point returns."""
    if isinstance(value, dict):
        return repr(sorted((str(k), freeze(v)) for k, v in value.items()))
    if isinstance(value, (list, tuple, set)):
        return repr(sorted(freeze(v) for v in value)) if isinstance(value, set) \
            else repr([freeze(v) for v in value])
    return repr(value)


def one(label, rel, enum_name, excl_name, verdict_name, root):
    try:
        mod = load(rel)
    except Exception as exc:                                   # noqa: BLE001
        return dict(instrument=label, status="LOAD_FAILED", files=0,
                    bare="-", guarded="-", detail="%s: %s" % (type(exc).__name__, exc))
    enum = getattr(mod, enum_name, None)
    verdict = getattr(mod, verdict_name, None)
    if enum is None or verdict is None:
        return dict(instrument=label, status="NO_ENTRY_POINT", files=0,
                    bare="-", guarded="-",
                    detail="missing %s or %s" % (enum_name, verdict_name))
    excluded = getattr(mod, excl_name, ()) if excl_name else ("<inline in walk()>",)
    try:
        files = list(enum(root))
    except Exception as exc:                                   # noqa: BLE001
        return dict(instrument=label, status="ENUMERATION_RAISED", files=0,
                    bare="-", guarded="-", detail="%s: %s" % (type(exc).__name__, exc))
    status, detail = walked_or_refuse(files, root, excluded)

    def call():
        try:
            return freeze(verdict(root))
        except Exception as exc:                               # noqa: BLE001
            return "RAISED(%s)" % type(exc).__name__

    bare = call()
    if status != WALKED:
        # The guard declines, so the published value is withdrawn rather than changed.
        return dict(instrument=label, status="REFUSED", files=len(files),
                    bare=bare, guarded="NO_VERDICT", detail=detail)
    guarded = call()
    return dict(instrument=label, status="PRESERVED" if bare == guarded else "CHANGED",
                files=len(files), bare=bare, guarded=guarded, detail="")


COLS = ["root", "instrument", "status", "files", "bare_eq_guarded"]


def census(clone_dir):
    roots = sorted(d for d in os.listdir(clone_dir)
                   if os.path.isdir(os.path.join(clone_dir, d)))
    out = []
    for r in roots:
        for args in SUBJECTS:
            res = one(*args, root=os.path.join(clone_dir, r))
            res["root"] = r
            out.append(res)
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    rows = census(argv[1])
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print("# pairs: %d" % len(rows))
    for k in sorted(counts):
        print("# %-20s %d" % (k, counts[k]))
    changed = counts.get("CHANGED", 0)
    print("#")
    print("# ACTION EU falsifier -- CHANGED pairs: %d -> %s"
          % (changed, "REFUTED" if changed else "NOT REFUTED"))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join([r["root"], r["instrument"], r["status"], str(r["files"]),
                         "yes" if r["status"] == "PRESERVED" else
                         ("n/a" if r["status"] == "REFUSED" else "NO")]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
