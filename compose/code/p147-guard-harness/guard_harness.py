"""p147-guard-harness -- `ACTION EJ`, implemented as a wrapper because the literal form
would destroy the figures it is meant to protect.

> 🟢 **`ACTION EJ`** -- wire the guard into the five at-risk instruments.

🔴 **Wiring it IN means editing five files whose bytes produced published figures.** p145
hit the same choice and answered it the other way round: it repaired `surface_gate2.py` in
a **successor** (`surface_gate3.py`) and left the original intact, which is the only reason
`p145-surface-payload-repair` could report *"baseline reproduces p143 row for row"* and
attribute every difference to its own two changes.

🔵 **Edit `surface_gate2.py` in place and that sentence becomes unverifiable for every
future pass.** So this module wires the guard AROUND each instrument instead of into it:
it calls the instrument's **own** enumeration function, counts what that function yields,
and refuses a verdict at zero.

| instrument | enumeration called | exclusion owner |
|---|---|---|
| `p141-agent-surface-gate/surface_gate.py` | `walk(root)` | 🔴 inline literal inside `walk()` |
| `p143-surface-gate-repair/surface_gate2.py` | `walk(root)` | `SKIP_DIRS` |
| `p142-americas-disambiguation/americas.py` | `source_files(repo)` | `SKIP_DIR` |
| `p142-schema-location-tiers/schema_tiers.py` | `tracked(repo)` | `EXCLUDE` |
| `p143-vendor-tenancy/tenancy.py` | `source_files(repo)` | `SKIP_DIR` |

🟢 **Nothing is duplicated.** The harness never carries a copy of any exclusion set --
`P146-D` showed what happens to a census that carries the tokens it counts -- so a later
change to any of the five is picked up with no change here.

🔵 **What this cannot do.** A wrapper guards a CALLER that goes through it. It does not
stop the five from being run directly, and `ACTION EK` is where that gap belongs.

    python3 guard_harness.py <clone-or-payload-root>...
    python3 test_guard_harness.py        # 9 tests, authored fixtures, offline
"""

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p146-empty-walk-guard"))
from walk_guard import walked_or_refuse, NO_PAYLOAD_WALKED, WALKED      # noqa: E402

# (label, module path relative to compose/code, enumeration attr, exclusion attr or None)
AT_RISK = [
    ("p141-surface-gate", "p141-agent-surface-gate/surface_gate.py", "walk", None),
    ("p143-surface-gate2", "p143-surface-gate-repair/surface_gate2.py", "walk",
     "SKIP_DIRS"),
    ("p142-americas", "p142-americas-disambiguation/americas.py", "source_files",
     "SKIP_DIR"),
    ("p142-schema-tiers", "p142-schema-location-tiers/schema_tiers.py", "tracked",
     "EXCLUDE"),
    ("p143-tenancy", "p143-vendor-tenancy/tenancy.py", "source_files", "SKIP_DIR"),
]


def load(rel):
    """Import one instrument by path, without requiring it to be a package."""
    path = os.path.normpath(os.path.join(HERE, "..", rel))
    name = "instr_" + os.path.basename(path)[:-3].replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def guarded_enumeration(label, rel, fn_name, excl_name, root):
    """(status, n, detail) from the instrument's OWN enumeration over `root`."""
    try:
        mod = load(rel)
    except Exception as exc:                        # noqa: BLE001 - reported, not raised
        return "LOAD_FAILED", 0, "%s: %s" % (type(exc).__name__, exc)
    fn = getattr(mod, fn_name, None)
    if fn is None:
        return "NO_ENUMERATION", 0, "%s has no %s()" % (rel, fn_name)
    excluded = getattr(mod, excl_name, ()) if excl_name else ("<inline in walk()>",)
    try:
        files = list(fn(root))
    except Exception as exc:                        # noqa: BLE001
        return "ENUMERATION_RAISED", 0, "%s: %s" % (type(exc).__name__, exc)
    status, detail = walked_or_refuse(files, root, excluded)
    return status, len(files), detail


COLS = ["root", "instrument", "status", "files", "detail"]


def main(argv):
    roots = argv[1:]
    if not roots:
        print(__doc__)
        return 2
    print("\t".join(COLS))
    refused = 0
    rows = 0
    for root in roots:
        root = root.rstrip("/")
        for label, rel, fn_name, excl_name in AT_RISK:
            status, n, detail = guarded_enumeration(label, rel, fn_name, excl_name, root)
            rows += 1
            if status == NO_PAYLOAD_WALKED:
                refused += 1
            print("\t".join([os.path.basename(root), label, status, str(n), detail]))
    sys.stderr.write("\n# %d (root, instrument) pair(s); %d would be REFUSED a verdict\n"
                     % (rows, refused))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
