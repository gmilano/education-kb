---
industry: education
region: Global
updated: 2026-10-13
---

# `p171-cross-block-gate` — `P170-C` implemented, and `P471` avoided on the second try

**Pass 171, 2026-10-13.** `ACTION JM`: does `T216`'s lost-row defect affect shelves other than the
LMS route?

**It does. `6` repositories besides `OpenOLAT` were routed by an earlier pass and are absent from
the newest routing table.** The falsifier FIRED, `T216` is systemic in `verticals/solutions.md`,
and `P170-C` is necessary.

## Why the first shape of this gate was thrown away

| attempt | produced | why it was unsound |
|---|---|---|
| every repo on a line also carrying a licence identifier | **`372`** across `3` files | wrong **POPULATION**, not wrong threshold. These files carry `190`-row **CENSUS** tables — MCP servers, LTI libraries, QTI players, OneRoster implementations — that no pass ever offered as recommendations. A newest block that does not re-state a census has lost nothing. This is `P471`: a gate that marks everything controls nothing |
| restricted to **ROUTING** tables | **`7`** — a `98%` cut | in this KB a routing table is headed `need`, `engagement` or `layer` and answers *"what should a client use"*. A census is headed `repo`, `candidate` or `agent / library` |
| plus `casefold` on the slug | **`6`** | GitHub owner names are case-insensitive and this KB writes `openolat/OpenOLAT` **and** `OpenOLAT/OpenOLAT` in the same file, so a case-sensitive match reported a row p170 had RESTORED as still lost (`T226`) |

## The test that mattered

After `verticals/solutions.md` was rewritten with p171's own routing table, the gate reported
**`3` rows that p171 itself had dropped** — `ILIAS`, `RosarioSIS` and `openSIS-Classic`, all carried
by p170. They were re-stated before the pass was committed.

**A gate that catches the pass that wrote it is the only kind worth keeping.**

## It reports; it never auto-fixes

Of the `6` flagged rows, `5` were RESTORED and **`1` was a deliberate removal**:
[`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia), which p169 measured as abandoned
(last commit a README edit `228` days earlier, `Django<4.0` past EOL, sibling package unresolvable).

A gate that had *"corrected"* that row back onto the routing table would have re-recommended a dead
package. **The absence of a row may be a decision; it must be a decision someone recorded.**

## How to run it

```sh
python3 -I check_lost_rows.py verticals/solutions.md repos/foundations.md agents/top.md compose/patterns.md
```

## Scope limit, stated rather than smoothed

`ACTION JM` asked for three files. **Only one of them has a routing table in this sense.**
`repos/foundations.md` and `agents/top.md` carry verification and census tables and route nothing
directly — the agent and repo routing function lives in `compose/patterns.md` as `P170-D`, which
this gate reads as `80` of `80` rows intact. So: the shelf that routes by **need** lost `6`; the
shelf that routes by **stack layer** lost `0`.
