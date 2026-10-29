#!/usr/bin/env python3
"""P520 — REPAIR the `P383` region-heading contract instead of only detecting its breach.

🔴 Why this exists. `Gap 520-E` registered that the `P383` contract — *exactly one* bare
`## Opportunities by region`, the current pass's — has now regressed **three** times (`p508`,
`p511`/`p514`, `p519`). The gap's own diagnosis: a fixed-position contract inside a **prepend-only**
file is structurally fragile, because every pass that prepends a section must remember to demote
the previous bare heading, and a detector that only reports the breach leaves the work undone.

🟢 The named closure was *"make the gate repair it rather than only detect it"*. This does that.

The rule, and it is the one `p519` applied by hand:
  - The file is prepend-only, so the FIRST bare canonical heading is the newest pass's. It stays.
  - Every LATER bare one is demoted to `## Opportunities by region — `pNNN`` where `pNNN` is read
    by scanning BACKWARDS for the nearest `## 🆕 `pNNN`` section marker that owns it.
  - 🔴 Nothing is renumbered and nothing is guessed. A bare heading with no pass marker above it
    is reported `UNREPAIRABLE` and left exactly as it was.
  - Idempotent: a repaired file is a fixed point, so `make hooks` can run this every pass.

Usage:
  python3 -I repair_headings.py <file.md>            # report only, exit 1 if repairs are needed
  python3 -I repair_headings.py <file.md> --write     # apply repairs, exit 0 on success
"""
import re
import sys

CANON_BARE = re.compile(r"^## +Opportunities by region\s*$")
PASS_MARKER = re.compile(r"^## +.*?`(p\d+)`")
DEMOTED = "## Opportunities by region — `%s`"


def owning_pass(lines, idx):
    """The pass id of the section that owns line `idx`, by scanning backwards. None if absent."""
    for j in range(idx - 1, -1, -1):
        m = PASS_MARKER.match(lines[j])
        if m:
            return m.group(1)
    return None


def plan(lines):
    """-> (keep_line, [(line_idx, new_text, pass_id)], [unrepairable_line_idx])."""
    bare = [i for i, l in enumerate(lines) if CANON_BARE.match(l)]
    if not bare:
        return None, [], []
    keep = bare[0]
    repairs, unrepairable = [], []
    for i in bare[1:]:
        pid = owning_pass(lines, i)
        if pid is None:
            unrepairable.append(i)
        else:
            repairs.append((i, DEMOTED % pid, pid))
    return keep, repairs, unrepairable


def apply_plan(lines, repairs):
    out = list(lines)
    for i, new_text, _ in repairs:
        out[i] = new_text
    return out


def main(argv):
    if len(argv) < 2:
        print("P520-REPAIR\tNO-INPUT\t-\trefusing: no file given (the p541 class)")
        return 2
    path = argv[1]
    write = "--write" in argv[2:]

    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    keep, repairs, unrepairable = plan(lines)

    if keep is None:
        print("P520-REPAIR\tNO-CANON-BLOCK\t-\t%s has no bare `## Opportunities by region`" % path)
        return 1

    print("file\tbare_kept_line\trepairs\tunrepairable")
    print("%s\t%d\t%d\t%d" % (path, keep + 1, len(repairs), len(unrepairable)))
    for i, new_text, pid in repairs:
        print("  REPAIR\tline %d\t-> %s" % (i + 1, pid))
    for i in unrepairable:
        print("  UNREPAIRABLE\tline %d\tno `pNNN` section marker above it; left untouched" % (i + 1))

    if write and repairs:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(apply_plan(lines, repairs)))
        # Idempotence is a property worth asserting rather than assuming.
        with open(path, encoding="utf-8") as fh:
            again = fh.read().split("\n")
        _, again_repairs, _ = plan(again)
        if again_repairs:
            print("🔴 NOT IDEMPOTENT: %d repairs still pending after a write" % len(again_repairs))
            return 1
        print("🟢 wrote %d repair(s); re-plan is empty, so the file is a fixed point" % len(repairs))
        return 1 if unrepairable else 0

    if repairs or unrepairable:
        return 1
    print("🟢 exactly one bare canonical heading; contract holds")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
