---
industry: education
region: Global
updated: 2026-10-12
---

# p150-grant-ladder-order — `ACTION FE` discharged, falsifier silent

`ACTION FE` asked for `T74` to be fixed: restore `p147-licence-language`'s grant ladder to
`FILE > PKG_ONLY > README_ONLY`, matching `p145`'s documented intent, and re-run over all
**58** subjects. 🔴 *Refuted if any row other than the three npm rows p149 named changes
class.*

## 🟢 DISCHARGED — exactly three rows move, and they are the three

| subject | tier | p147 (inverted) | corrected | direction |
|---|---|---|---|---|
| `eth-moodle-mcp-1.3.3` | npm | 🔴 `README_ONLY` / MIT | 🟢 **`PKG_ONLY` / MIT** | 🟢 strengthening |
| `moodle-mcp-server-aql-0.1.7` | npm | 🔴 `README_ONLY` / AGPL-3.0 | 🟢 **`PKG_ONLY` / AGPL-3.0** | 🟢 strengthening |
| `owen-x-tech-canvas-mcp-1.1.0` | npm | 🔴 `README_ONLY` / MIT | 🟢 **`PKG_ONLY` / MIT** | 🟢 strengthening |

🟢 **No connector row and no agent row changes class.** 🟢 **No licence identification
changes on any row** — only the rung that records *where the grant was found*.

🔵 **The direction is worth stating plainly.** `PKG_ONLY` is a licence declared in a
machine-read manifest field; `README_ONLY` is prose. p147's inversion was quietly
*weakening* three rows — telling a studio it had only a prose mention where a declared
`package.json` licence exists. 🟢 **The correction restores the stronger reading**, which
is why it moves no figure in the dangerous direction.

## Why this did not need all 58 clones

🟢 **FILE-grant rows are invariant to the swap by construction.** `census()` returns on
the licence-file branch before either of the reordered branches is reached, so no row with
a licence file can move. That leaves the **18 non-FILE rows** of `p145`'s published census
(10 connector + 8 npm) as the only rows that can change, and the **6 agent-tier rows**
were measured alongside them for `ACTION FL`.

🟢 **24 subjects measured** — 16 clones + 8 `npm pack` trees — and the invariance is
asserted, not assumed: `test_the_two_arms_agree_on_every_file_row` runs both arms over
every combination of the three surfaces on a FILE row and requires agreement.

## Both arms live in one module, deliberately

A comparison needs both arms in one place, so `census_p147_order()` keeps p147's inverted
ladder verbatim as the control, and `ORDER` names the corrected one explicitly so a later
pass can read the ladder without reading the control flow.

## Run it

    python3 run_ladder_order.py <clones-dir> <npm-trees-dir> > result.2026-10-12-p150.tsv
    python3 test_ladder_order.py     # 17 tests, authored fixtures, offline

## 🔴 What this does NOT do

- 🔴 **`p147-licence-language` itself is unchanged.** The fix lives here, beside its
  control and its tests. Patching the published module in the same pass that measures it
  would leave no arm to compare against — 🔵 **the reason `ACTION FE` existed as a
  separate action at all.** 🔵 **Registered as `ACTION FP`**: retire `p147`'s copy, or
  mark it superseded in place.
- 🔴 **The three moved rows' published figures are not re-issued here.** They are stated
  above and in `result.2026-10-12-p150.tsv`; no page that quotes a `README_ONLY` count for
  the npm tier has been rewritten.
