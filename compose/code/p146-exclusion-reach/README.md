---
industry: education
region: Global
updated: 2026-10-12
---

# p146-exclusion-reach — was `P145-A` an incident, or a shelf property?

`P145-A` found `surface_gate2.py` excluding `dist` and `build` unconditionally while 7 of
the 8 npm packages on this shelf keep their entire payload under exactly those names. It
walked **zero files** and published `NOT_AN_MCP_SERVER` for two passes. `T42` names it.

p145 repaired the list in its own successor. 🔴 **It did not ask whether anything else on
the shelf could do the same, or whether anything would notice.**

    python3 exclusion_reach.py ../                      # TSV to stdout, summary to stderr

## Result, 2026-10-12

| | count |
|---|---|
| instruments that traverse a tree | **35** |
| …carrying an **empty-walk guard** | 🔴 **0** |
| …excluding `dist`/`build`, no re-admission, emitting a verdict | 🔴 **5** |
| …that cannot read anything but a git clone | 🔴 **16** |

🔴 **AT_RISK**: `p141-agent-surface-gate/surface_gate.py` (🆕 **new, and it is the agent
tier's own gate**), `p143-surface-gate-repair/surface_gate2.py` (`P145-A`'s own),
`p142-americas-disambiguation/americas.py`, `p142-schema-location-tiers/schema_tiers.py`,
`p143-vendor-tenancy/tenancy.py`.

🟢 **REPAIRED**: `p145-surface-payload-repair/surface_gate3.py` — `payload_trees` ∩
`SKIP_DIRS` passed as `admit`, verified by test rather than by regex.

🆕 🔴 **`T59`**: 16 of 35 instruments traverse by `git ls-tree`/`ls-files`, so a clone is a
precondition rather than a convenience — and the **entire region-placement lane** is in
that set. 🔵 **A published npm package is not a git tree, so this shelf's 8 npm rows are
structurally unplaceable on the region axis.**

## 🔴 The defect this probe had, recorded because it ran in the reassuring direction

Its first run reported **36** instruments, **1** guarded and **2** `REPAIRED`. 🔴 **Both
extra rows were its own source**: it traverses with `rglob` and carries the guard and
re-admission token sets *as regexes*, so it read itself as a compliant instrument. 🔵 **A
census that includes the censor inflates exactly the number it exists to report.** The
population now excludes `p146-*`, and the honest baseline is **35 / 0**.

## Limits

🔴 **A capability census, not an audit of published figures.** It says which instruments
*can* return a verdict over nothing. Establishing that a given row *did* needs the payload,
and the payload needs a clone — refused in this environment (`P146-A`). The five affected
rows are named for p147 as `ACTION EI` rather than re-verdicted here.
