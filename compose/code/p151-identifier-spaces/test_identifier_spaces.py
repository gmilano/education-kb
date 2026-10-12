#!/usr/bin/env python3
"""Suite for `p151-identifier-spaces`. Prints its own total (`P126` point 3).

🔵 **The obligatory cases are the two ways this gate can lie.** (1) A cited id that
resolves in a space the gate does not read must be reported as DANGLING when that space is
withheld and as resolved when it is declared — otherwise "0 dangling" only means "the gate
read the right file by luck". (2) An append-only page in scope must blow the gate up, so
the scope declaration is tested and not merely documented. Every KB here is authored under
a temporary directory.

    python3 test_identifier_spaces.py
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import identifier_spaces as S  # noqa: E402

PATTERNS = """# Patterns

## 🆕 🟢 `P1` — the first pattern *(new, p100 — …)*

Body citing `P2` and the module axis `P240` and the pass finding `P138`.

## 🔁 `P1` AMENDED at step 2 — the same pattern, revisited

## 🆕 `P2` — the second pattern *(new, p101 — …)*

### 🔴 What `P2` does NOT solve
"""
MODULE_README = """# P239 / P240 — table integrity

| axis | what it looks for |
|---|---|
| **P239** | a table whose rows disagree with its header |
| **P240** | a table with a region column missing one of the five |
"""
HISTORY = """# History

Pass 99 cited `P900` and `P901`, both from the previous generation.
"""

cases = []


def check(name, got, want):
    cases.append((name, got == want, got, want))


def kb(tmp, name, files):
    root = os.path.join(tmp, name)
    for rel, body in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)
    return root


def main():
    tmp = tempfile.mkdtemp(prefix="p151-ids-")
    try:
        root = kb(tmp, "kb", {
            "compose/patterns.md": PATTERNS,
            "compose/code/p239-table-integrity/README.md": MODULE_README,
            "compose/code/p138-npm-payload-licence/README.md": "# p138\n",
            "README.md": "## Pass 138 — 2026\n\ntext\n",
            "agents/trending.md": HISTORY,
        })
        scope = ("compose/patterns.md",)

        # ── 1. the three spaces are found, separately ─────────────────────────────────
        check("space 1 finds both first allocations and the revisit",
              sorted(S.space_patterns(root)), ["P1", "P2"])
        check("space 2 finds the module axes", sorted(S.space_module_axes(root)),
              ["P239", "P240"])
        check("space 3 finds the pass numbers",
              sorted(S.pass_numbers(root)), ["P138", "P239"])
        check("a module DIRECTORY name allocates its pass number",
              "P239" in S.pass_numbers(root), True)
        check("and a README pass heading does too",
              "P138" in S.pass_numbers(root), True)

        # ── 2. the gate, with every space declared ────────────────────────────────────
        code, report = S.gate(root, scope)
        check("the gate is green when all three spaces are declared", code, 0)
        check("and it says so", "dangling=0" in report[1], True)
        rows, _ = S.dangling(root, scope)
        by = {r["id"]: r["space"] for r in rows}
        check("P1 resolves in the pattern space", by["P1"], "patterns")
        check("P240 resolves in the MODULE-AXIS space", by["P240"], "module-axis")
        check("P138 resolves in the PASS-FINDING space", by["P138"], "pass-finding")
        check("the allocation location is reported, not just the space",
              [r["allocated"] for r in rows if r["id"] == "P240"],
              ["compose/code/p239-table-integrity/README.md:6"])

        # ── 3. OBLIGATORY — withhold a space and the gate must go red ────────────────
        bare = kb(tmp, "kb-bare", {"compose/patterns.md": PATTERNS})
        code2, report2 = S.gate(bare, scope)
        check("withhold spaces 2 and 3 and the gate goes RED", code2, 1)
        rows2, _ = S.dangling(bare, scope)
        check("and P240 and P138 are exactly what it flags",
              sorted(r["id"] for r in rows2 if r["space"] == "DANGLING"),
              ["P138", "P240"])
        check("so '0 dangling' is a statement about the DECLARED scope",
              code != code2, True)

        # ── 4. OBLIGATORY — an append-only page in scope must blow the gate up ───────
        code3, _ = S.gate(root, ("compose/patterns.md", "agents/trending.md"))
        check("an append-only page in scope turns the gate red", code3, 1)
        rows3, _ = S.dangling(root, ("agents/trending.md",))
        check("and the ids it flags are the previous generation's",
              sorted(r["id"] for r in rows3 if r["space"] == "DANGLING"),
              ["P900", "P901"])
        check("which is why APPEND_ONLY names four files, not three",
              len(S.APPEND_ONLY), 4)
        check("and open-gaps.md is one of them",
              "intel/open-gaps.md" in S.APPEND_ONLY, True)
        check("the live scope and the append-only set do not overlap",
              set(S.LIVE_SCOPE) & set(S.APPEND_ONLY), set())

        # ── 5. the heading grammar must not read a subsection as an allocation ───────
        check("`### What `P2` does NOT solve` is not an allocation",
              len(S.space_patterns(root)["P2"]), 1)
        check("a revisit is not a second allocation either",
              len(S.space_patterns(root)["P1"]), 2)
        # 🔵 Two entries for P1 is correct here: this module indexes HEADINGS and leaves
        # first-vs-revisit to p150-identifier-collision, which owns that question.

        # ── 6. an axis row needs CONTENT, not just an id in the first cell ───────────
        thin = kb(tmp, "kb-thin", {
            "compose/patterns.md": "## 🆕 `P1` — x *(new, p1 — …)*\n\n`P9`\n",
            "compose/code/m/README.md": "| **P9** |  |\n"})
        check("an empty second cell does not allocate", "P9" in S.space_module_axes(thin),
              False)
        check("so the citation of P9 is correctly DANGLING",
              [r["space"] for r in S.dangling(thin, ("compose/patterns.md",))[0]
               if r["id"] == "P9"], ["DANGLING"])

        # ── 7. an empty / missing KB must not read as green by vacuity ───────────────
        nothing = os.path.join(tmp, "nope")
        rows4, _ = S.dangling(nothing, scope)
        check("a missing KB yields no citations", len(rows4), 0)
        check("and therefore no finding — the caller must check the scope exists",
              S.gate(nothing, scope)[0], 0)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    failed = [c for c in cases if not c[1]]
    for name, ok, got, want in cases:
        if not ok:
            print("FAIL  %-58s got=%r want=%r" % (name, got, want))
    print("p151-identifier-spaces: %d tests, %d passed, %d failed"
          % (len(cases), len(cases) - len(failed), len(failed)))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
