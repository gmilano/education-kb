"""p146-exclusion-reach — was `P145-A` an incident, or a property of this shelf?

`P145-A` found `surface_gate2.py` excluding `dist` and `build` unconditionally while 7 of
the 8 npm packages on this shelf keep their entire payload under exactly those two names.
It walked zero files and published `NOT_AN_MCP_SERVER` for two passes. `T42` names the
class: an exclusion list can turn a measurement into a verdict over nothing.

p145 repaired the list in its own successor. This probe asks the question p145 did not:
**how many other instruments on this shelf can do the same thing, and how many could
notice?**

## Method

Static reading of every `.py` on the code shelf that traverses a tree, on four axes:

  1. **traversal channel** — `rglob`/`os.walk`/`iterdir` (reads a loose payload) versus
     `git ls-tree`/`ls-files` (reads a clone, and *only* a clone).
  2. **does its exclusion set name `dist` or `build`?**
  3. **is there a re-admission path** — `BUILT_TREES`, `declared_entries`, an `admit`
     parameter, `payload_trees` — i.e. does it ask the artefact instead of the name?
  4. **is there an empty-walk guard** — any check that the walked set is non-empty before
     a verdict is formed?

Tests and negative controls are excluded from the population by filename, and so are
this pass's own two probe trees.

🔴 **A defect this probe had and this note records.** Its first run reported **36**
instruments, **1** of them guarded and **2** `REPAIRED`. Both extra rows were its OWN
source: `exclusion_reach.py` traverses with `rglob` and carries the `GUARD` and `READMIT`
token sets *as regexes*, so it read itself as a guarded, repaired instrument. 🔵 **A
census that includes the censor inflates exactly the number it exists to report** — and
in the reassuring direction. The population is now `p146-*`-excluded, and the honest
baseline is **35 instruments, 0 guarded**.

## Limits, stated rather than hidden

🔴 **This is a capability census, not an audit of published figures.** It says which
instruments are CAPABLE of returning a verdict over nothing. Establishing that a given
published row *did* is a per-row question that needs the payload, and the payload needs a
clone — which `P146-A` records as refused in this environment. The at-risk rows are
therefore named for `p147` rather than re-verdicted here.

🔵 A regex for a re-admission path can be fooled by a mechanism spelled differently. The
`REPAIRED` verdict was checked by hand on the one row that earns it (`surface_gate3.py`,
whose `payload_trees` ∩ `SKIP_DIRS` is passed as `admit`), and that row is pinned by
`p146-empty-walk-guard/test_walk_guard.py`.
"""
import re
import sys
from pathlib import Path

WALK_FS = re.compile(r"\brglob\(|\bos\.walk\(|\biterdir\(")
WALK_GIT = re.compile(r"ls-tree|ls-files")
DIST = re.compile(r"""['"]/?(?:dist|build)/?['"]""")
READMIT = re.compile(r"BUILT_TREES|declared_entries|\badmit\b|payload_trees")
GUARD = re.compile(
    r"if\s+not\s+(?:files|texts|paths|walked|by_path|sources?|tracked|listing)\b"
    r"|NO_PAYLOAD|EMPTY_WALK|NOTHING_WALKED|WALKED_ZERO")
VERDICT = re.compile(r"verdict|VERDICT|NOT_AN_MCP_SERVER|BOUNDED|UNBOUNDED|classify")

COLS = ["instrument", "channel", "excludes_dist_build", "has_readmission",
        "empty_walk_guard", "emits_verdict", "class"]


def classify(channel, dist, readmit, verdict):
    if dist and not readmit and verdict:
        return "AT_RISK"
    if dist and readmit:
        return "REPAIRED"
    if dist:
        return "DIST_NO_VERDICT"
    return "NO_DIST_EXCLUSION"


def census(root):
    rows = []
    for p in sorted(Path(root).rglob("*.py")):
        if p.name.startswith("test_") or "NEGATIVE-CONTROL" in p.name:
            continue
        # 🔴 This pass's own trees are not part of the population it measures.
        if p.relative_to(root).parts[0].startswith("p146-"):
            continue
        try:
            src = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        fs, git = bool(WALK_FS.search(src)), bool(WALK_GIT.search(src))
        if not (fs or git):
            continue
        channel = "fs+git" if fs and git else ("fs" if fs else "git-only")
        dist, readmit = bool(DIST.search(src)), bool(READMIT.search(src))
        guard, verdict = bool(GUARD.search(src)), bool(VERDICT.search(src))
        rows.append({
            "instrument": str(p.relative_to(root)), "channel": channel,
            "excludes_dist_build": dist, "has_readmission": readmit,
            "empty_walk_guard": guard, "emits_verdict": verdict,
            "class": classify(channel, dist, readmit, verdict),
        })
    return rows


def main(argv):
    rows = census(argv[0])
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))

    at_risk = [r for r in rows if r["class"] == "AT_RISK"]
    git_only = [r for r in rows if r["channel"] == "git-only"]
    guarded = [r for r in rows if r["empty_walk_guard"]]
    e = sys.stderr
    print("\n# traversing instruments: %d" % len(rows), file=e)
    print("# AT_RISK (dist/build excluded, no re-admission, emits a verdict): %d"
          % len(at_risk), file=e)
    for r in at_risk:
        print("#   %-9s %s" % (r["channel"], r["instrument"]), file=e)
    print("# git-only (cannot read a loose payload at all): %d" % len(git_only), file=e)
    print("# WITH AN EMPTY-WALK GUARD: %d of %d" % (len(guarded), len(rows)), file=e)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
