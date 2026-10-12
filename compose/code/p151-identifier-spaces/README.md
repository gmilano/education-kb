# `p151-identifier-spaces` — `ACTION FQ`: the dangling citation, and `P240`

🟢 **DISCHARGED, falsifier SILENT — and `P240` is not dangling. It RESOLVES.**

🟢 **`P240` is allocated** at [`../p239-table-integrity/README.md`](../p239-table-integrity/README.md)
line 17, as the region-column completeness axis: *"Tabla con columna de región a la que le
falta una de las cinco del vocabulario cerrado"* (pass 78). 🟢 **The citation at
`compose/patterns.md:555` is correct.** `p356-citation-origin` had already filed `P240`
among fifteen ids that were *born cited* (`NACIÓ CITADA`) at pass 39 — the documentation
debt was paid thirty-nine passes later, and the gate could not see it.

## 🆕 `T82` — three identifier spaces share one `P` prefix, and the gate read one

| space | allocated by | measured | example |
|---|---|---|---|
| **1 — patterns** | a `## `P35` — …` heading on `compose/patterns.md` | **39**, max `P39` | `P35`, the MCP governance pattern |
| **2 — module axes** | a table row in `compose/code/*/README.md` whose first cell is the bare id | **21** | `P240`, the region-column axis |
| **3 — pass findings** | being reported in a pass; cited bare (`P138`) or qualified (`P150-A`) | **174** pass numbers nameable | `P138`, *"a licence identifier is not a licence"* |

🔴 **Read the pattern page against space 1 alone and 2 of its 41 cited ids look dangling.**
Both resolve — `P240` in space 2, `P138` in space 3. 🟢 **So `P240` was not the only
citation space 1 cannot resolve, the falsifier is silent, and the extension is not a
one-line check kept for the next one.**

## 🔴 And the scope declaration is the load-bearing part

| scope | cited ids | dangling |
|---|---|---|
| the **6 pages this shelf rewrites each pass** | 44 | 🟢 **0** |
| …plus `intel/open-gaps.md` | 354 | 🔴 **260** |
| …plus the two trending pages and the README | 745 | 🔴 **685** |

🔴 **Four of this shelf's ten content files are append-only pass history, not three** —
`intel/open-gaps.md` accumulates every pass's action verdicts alongside the trending pages
and the README. 🔵 **Every one of the 260 is a generation-1 id** (`P469`…`P1047`) surviving
in a verdict row written before the **2026-10-06 reset restarted space 1 at `P1`**. They
are a historical record, not a defect — which is why a dangling-citation check is
meaningless until its scope is declared, and why `scope` and `spaces` are both arguments
of this gate rather than constants inside it.

🔵 **The gate is green:** `scope: 6 files   cited=44   dangling=0`, exit 0.

- instrument: [`identifier_spaces.py`](identifier_spaces.py) · **25 tests**, all offline
- the collision half lives in [`../p150-identifier-collision`](../p150-identifier-collision/README.md);
  this module owns the mirror image and leaves FIRST-vs-REVISIT to that one

```
python3 test_identifier_spaces.py
python3 identifier_spaces.py /path/to/kb            # exit != 0 on a dangling id
```
