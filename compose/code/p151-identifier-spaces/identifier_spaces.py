#!/usr/bin/env python3
"""p151-identifier-spaces — `ACTION FQ`: a DANGLING citation, and the three spaces.

> 🟢 **`ACTION FQ`** — extend `p150-identifier-collision` to catch a DANGLING citation: a
> pattern id cited in prose with no allocation anywhere. Resolve or withdraw `P240`.
> 🔴 *Refuted if `P240` is the only dangling citation* — which would make it a
> transcription slip rather than the mirror of `T75`, and the extension a one-line check
> kept for the next one.

## What the measurement found, and it is not what the action expected

🟢 **`P240` is NOT dangling. It RESOLVES.** It is allocated at
[`compose/code/p239-table-integrity/README.md`](../p239-table-integrity/README.md) line
17, as the region-column completeness axis: *"Tabla con columna de región a la que le
falta una de las cinco del vocabulario cerrado"*. 🟢 **The citation at
`compose/patterns.md:555` is correct**, and `p356-citation-origin` had already filed
`P240` among fifteen ids that were *born cited* (`NACIÓ CITADA`) — the debt was paid at
pass 78, thirty-nine passes after the citation.

🔴 **The real defect is bigger than a slip: this shelf has THREE identifier spaces that
share one `P` prefix, and the gate reads one of them.**

| space | where allocated | measured, pass 151 | example |
|---|---|---|---|
| **1 — patterns** | `## `P35` — …` headings on `compose/patterns.md` | **39**, max `P39` | `P35` the MCP governance pattern |
| **2 — module axes** | a table row in `compose/code/*/README.md` whose first cell is the bare id | **21** | `P240`, the region-column axis |
| **3 — pass findings** | a pass section; cited bare or as `P150-A` | not enumerated | `P138`, *"a licence identifier is not a licence"* |

🔴 **Read `compose/patterns.md` against space 1 alone and 2 of its 41 cited ids look
dangling.** Both resolve: `P240` in space 2, `P138` in space 3. 🟢 **Zero genuinely
dangling citations on the live page.** 🔴 **Read it against the append-only history as
well and 685 ids look dangling** — because the 2026-10-06 reset restarted space 1 at `P1`,
so every id the history cites belongs to a *previous generation* of the same space.

🔵 **So a dangling-citation check is meaningless until its scope is declared**, and that is
this module's contract: `scope` names the files, `spaces` names where allocations may be
found, and `dangling()` reports an id only when it is absent from EVERY declared space.
🆕 **`T82`.**

    python3 identifier_spaces.py /path/to/kb          # gate: non-zero on a dangling id
"""
import os
import re
import sys
from collections import defaultdict

# Space 1 — a pattern heading on the pattern page. Grammar carried from
# p150-identifier-collision, which is the module that owns the collision half.
HEADING = re.compile(r"^(#{2,3})\s+(?P<markers>[^\w\n]*)`?(?P<id>P\d+)`?"
                     r"(?P<mid>[^—–\n]*?)\s*(?:—|–)\s*(?P<title>.*)$")
# Space 2 — a module README's axis table: `| **P240** | what the axis looks for |`.
# 🔵 The second cell must hold real text: `\s*[^|\s]` and not `\s*\S`, because `\S`
# matches the NEXT pipe and so an empty cell would allocate an id with no definition.
ROW_DEF = re.compile(r"^\|\s*\**`?(P\d+)`?\**\s*\|\s*[^|\s]")
# Space 3 — a pass finding, which is allocated by being REPORTED in a pass and is cited
# either bare (`P138`) or qualified (`P150-A`). A bare citation of a pass number is
# resolvable iff that pass exists on this shelf, which `pass_numbers()` reads from the
# module directory names and the README's own pass headings.
FINDING_QUALIFIED = re.compile(r"`(P\d+)-[A-Z]+`")
PASS_DIR = re.compile(r"^p(\d+)-")
PASS_HEADING = re.compile(r"(?m)^##\s+Pass\s+(\d+)\b")

# A citation: `P35`, **P35** or (P35.
CITE = re.compile(r"`(P\d+)`|\*\*(P\d+)\*\*|\((P\d+)\b")

# 🔴 The two trending pages and the README are APPEND-ONLY pass history. Their citations
# belong to the identifier generation of the pass that wrote them, so they are NOT in the
# default scope — including them turns 1 finding into 685.
# 🔴 FOUR of this shelf's ten content files are append-only pass history, not three:
# `intel/open-gaps.md` accumulates every pass's action verdicts alongside the two trending
# pages and the README. Measured: with `open-gaps.md` in scope the gate reports **260**
# dangling ids; without it, **0** over 44 citations. 🔵 Every one of the 260 is a
# generation-1 id (`P469`..`P1047`) surviving in a verdict row written before the
# 2026-10-06 reset restarted space 1 at `P1`.
APPEND_ONLY = ("agents/trending.md", "repos/trending.md", "README.md",
               "intel/open-gaps.md")
# The pages this shelf REWRITES each pass. These are the only pages on which a dangling
# citation is a defect rather than a historical record.
LIVE_SCOPE = ("compose/patterns.md", "agents/top.md", "repos/foundations.md",
              "verticals/solutions.md", "intel/market.md", "intel/trends.md")


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return ""


def space_patterns(kb):
    """Space 1: {id: [location]} from the pattern page's headings."""
    out = defaultdict(list)
    path = os.path.join(kb, "compose/patterns.md")
    for i, line in enumerate(read(path).splitlines(), 1):
        m = HEADING.match(line)
        if m:
            out[m.group("id")].append("compose/patterns.md:%d" % i)
    return out


def space_module_axes(kb):
    """Space 2: {id: [location]} from every module README's axis table."""
    out = defaultdict(list)
    code = os.path.join(kb, "compose/code")
    if not os.path.isdir(code):
        return out
    for d in sorted(os.listdir(code)):
        rp = os.path.join(code, d, "README.md")
        if not os.path.isfile(rp):
            continue
        for i, line in enumerate(read(rp).splitlines(), 1):
            m = ROW_DEF.match(line.strip())
            if m:
                out[m.group(1)].append("compose/code/%s/README.md:%d" % (d, i))
    return out


def pass_numbers(kb):
    """Space 3's allocator: the passes this shelf can name.

    🔵 A bare `P138` is a finding of pass 138. It resolves iff pass 138 is on this shelf,
    which is evidenced two ways — a `p138-*` module directory, or a `## Pass 138` heading.
    """
    nums = set()
    code = os.path.join(kb, "compose/code")
    if os.path.isdir(code):
        for d in os.listdir(code):
            m = PASS_DIR.match(d)
            if m:
                nums.add("P" + m.group(1))
    for m in PASS_HEADING.finditer(read(os.path.join(kb, "README.md"))):
        nums.add("P" + m.group(1))
    return nums


def citations(kb, scope):
    out = defaultdict(list)
    for rel in scope:
        for i, line in enumerate(read(os.path.join(kb, rel)).splitlines(), 1):
            for m in CITE.finditer(line):
                out[m.group(1) or m.group(2) or m.group(3)].append("%s:%d" % (rel, i))
    return out


def resolve(pid, spaces):
    """The name of the first space that allocates `pid`, or None."""
    for name, index in spaces:
        if pid in index:
            return name
    return None


def dangling(kb, scope=LIVE_SCOPE):
    """(rows, spaces) — every cited id with the space that resolves it, or `DANGLING`."""
    spaces = [("patterns", space_patterns(kb)),
              ("module-axis", space_module_axes(kb)),
              ("pass-finding", {k: ["pass %s" % k[1:]] for k in pass_numbers(kb)})]
    rows = []
    for pid, where in sorted(citations(kb, scope).items(),
                             key=lambda kv: int(kv[0][1:])):
        space = resolve(pid, spaces)
        rows.append(dict(id=pid, space=space or "DANGLING", cited=len(where),
                         first=where[0],
                         allocated=(dict(spaces)[space][pid][0] if space else "-")))
    return rows, spaces


def gate(kb, scope=LIVE_SCOPE):
    """(exit_code, report). Non-zero when a cited id resolves in no declared space."""
    rows, spaces = dangling(kb, scope)
    bad = [r for r in rows if r["space"] == "DANGLING"]
    report = ["spaces: %s" % "  ".join("%s=%d" % (n, len(ix)) for n, ix in spaces),
              "scope: %d files   cited=%d   dangling=%d"
              % (len(scope), len(rows), len(bad))]
    for r in bad:
        report.append("  DANGLING %-7s cited %dx, first at %s"
                      % (r["id"], r["cited"], r["first"]))
    return (1 if bad else 0), report


def main(argv):
    kb = argv[1] if len(argv) > 1 else "."
    scope = tuple(argv[2:]) or LIVE_SCOPE
    code, report = gate(kb, scope)
    for ln in report:
        print(ln)
    rows, _ = dangling(kb, scope)
    sys.stderr.write("\nresolution by space:\n")
    by = defaultdict(int)
    for r in rows:
        by[r["space"]] += 1
    for k in sorted(by):
        sys.stderr.write("  %-14s %d\n" % (k, by[k]))
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
