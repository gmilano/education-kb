---
industry: education
region: Global
updated: 2026-10-12
---

# `p145-surface-payload-repair` — `ACTION DZ` discharged, and `ACTION DV` refuted by what it found

🔴 **The npm tier was never measured.** `surface_gate2.py` excludes `dist` and `build`
unconditionally, and **7 of the 8 npm packages on this shelf ship their entire payload
under exactly those two names**. The instrument walked **zero files** on all seven and
returned `NOT_AN_MCP_SERVER (0 'mcp' tokens, no SDK import)` — a verdict drawn from an
empty file set, published for two passes.

🟢 **`ACTION DZ` is discharged and its falsifier is silent**: 7 of 24 rows change verdict.
🔴 **But `ACTION DZ` could not have been the reason**, because the rows it was written to
repair were not being read at all.

## The two actions, as registered

> 🟢 **`ACTION DZ`** — give `surface_gate2.py` a pattern for
> `setRequestHandler(ListToolsRequestSchema, …)`. Add the shape, re-run the npm and
> github-only tiers, and compare. 🔴 *Refuted if no row's verdict changes.*

> 🔴 **`ACTION DV`** — reinstate `T30`'s npm figure explicitly, with the tier recomputed by
> ONE instrument over shipped trees. Run `surface_bound.py` over the shipped tree of all 24
> subjects across the four tiers. 🔴 *Refuted if any tier's dynamic share moves more than
> five points from p143's published value* — which would mean the instrument choice, not
> the artefact, is what `T30` was measuring all along, and `T30` must be withdrawn outright
> rather than reinstated.

## 🟢 The baseline reproduces exactly, which is what makes the rest readable

`surface_gate2.py` was re-run unmodified over all 24 subjects
([`baseline-p143-instrument.2026-10-12-p145.tsv`](baseline-p143-instrument.2026-10-12-p145.tsv))
and returns p143's published table row for row: **agent 50%, foundations 0%,
github-only 33%, npm 100% (n=1)**.

🔵 **So every difference below is this probe's two changes and nothing else.**

## 🔴 `ACTION DV` — REFUTED, and `T30` is withdrawn outright

The falsifier fires on both available routes.

| route | npm tier dynamic share | move |
|---|---|---|
| p143 published (`surface_gate2`, n=**1**) | **100%** | — |
| repaired (`surface_gate3`, n=**8**) | 🔴 **50%** | **50 points** |
| `surface_bound` descriptor counting (n=**8**) | 🔴 **12.5%** | **87 points** |

🔴 **And the second row is the smoking gun.** `T30`'s npm figure was **12%**.
`surface_bound.py` reads **1 of 8** non-static on this tier — **12.5%**. 🔴 **`T30`
compared a `surface_bound` number on npm against `surface_gate2` numbers on the other
tiers**, which is precisely the error `T36` was adopted and then withdrawn for. The
artefact was never the variable; **the instrument was**, exactly as `ACTION DV` predicted
in its own refutation clause.

### 🔴 `ACTION DV` is also not executable as written, and the reason is structural

It asks for all four tiers under `surface_bound.py`. 🔴 **`surface_bound.py` reads JS and
TS only** (`JS_SUFFIXES`, `TS_SUFFIXES` at lines 82–83), and of the 20 MCP servers across
the four tiers, **7 are Python and 1 is PHP**:

| tier | js | python | php |
|---|---|---|---|
| npm | **8** | 0 | 0 |
| agent | 1 | 2 | 1 |
| github-only | 2 | 4 | 0 |
| foundations | 0 | 1 | 0 |

🔵 **"One instrument over all four tiers" is unachievable on this population**, because the
tiers are not one language. It is recorded as an environment-independent impossibility
rather than a probe to re-register unchanged, and the 11 JS rows `surface_bound` *can* read
are published in
[`surface-bound-11-js-rows.2026-10-12-p145.tsv`](surface-bound-11-js-rows.2026-10-12-p145.tsv).

### 🔴 The deeper reason the two instruments disagree: they measure different properties

`surface_bound` counts **descriptors** — how many tool definitions exist in the payload.
`surface_gate2`/`gate3` count **registration sites** — where tools are attached to the
server. 🔴 **On a low-level-SDK server these live in different files**: the descriptors sit
in per-module arrays, the registration is one request handler. `@imazhar101/mcp-canvas-server`
reads **227 `BOUNDED_STATIC`** on one and **18 dynamic sites** on the other, and both are
correct about what they measure.

🔵 **So "dynamic share" was never one quantity.** `T30` is withdrawn outright.

## 🆕 `ACTION DZ` — the five `ListToolsRequestSchema` shapes, each read off a real row

`REG_JS` matches `.registerTool(` and `.tool(`. A low-level-SDK server registers nothing of
the kind; its whole surface is the array one handler returns. Five shapes occur here:

| shape | row | reading |
|---|---|---|
| `JS_LIST_HANDLER` — descriptors inline in the body | `mcp-canvas-lms` | 🟢 **3 LITERAL** |
| `JS_LIST_HANDLER_REF` — returns an identifier that IS a literal array | `canvas-mcp-server`, `@owen-x-tech/canvas-mcp` | 🟢 **54** and **62 LITERAL** |
| `JS_LIST_HANDLER_SPREAD_CALL` — array spreads method calls | `@imazhar101/mcp-canvas-server` | 🔴 **18 DYNAMIC** |
| `JS_LIST_HANDLER_MUTATED` — the array is `.push()`ed into | `moodle-mcp-server-aql` | 🔴 **DYNAMIC** |
| `JS_LIST_HANDLER_WRAPPED` — surface is a *function of* the array | (`@imazhar101`'s return) | 🔴 **DYNAMIC** |

🟢 **Five of the counts corroborate figures this KB already held by other means** —
`16`, `18`, `3` reproduce `p143-tier-size`'s hand counts exactly, `54` reproduces its
reading of `canvas-mcp-server`, and **62** reproduces the live surface `p139` and `p142`
established for `@owen-x-tech/canvas-mcp` against its own "150+" claim.

### 🔴 The row that deserves its `DYNAMIC` verdict for a real reason

`moodle-mcp-server-aql` does not fail to be static by accident. It builds
`toolDefinitions = buildCoreToolDefinitions()` and then **`.push()`es a descriptor per
discovered plugin** (`dist/server/factory.js:131`, inside the plugin loop). 🔴 **Its tool
surface grows with whatever plugins are installed at run time** — the only row on this
shelf whose surface is unbounded *by design* rather than by instrument limitation.

## 🔴 The defect this probe exists for: `SKIP_DIRS` is not property-relative

🔵 **This is `T39` exactly, one level up from where `P144-O` applied it.** `P144-O`
established that a population exclusion is sound only relative to the property measured,
and fixed `NOT_SHIPPED`. 🔴 **`SKIP_DIRS` was never examined**, and it carries the same
defect in a worse place: `dist/` is a regenerated artefact in a git checkout and it is
**the shipped tree itself** in a published tarball. Same name, same exclusion, opposite
correctness.

### The rule, stated so it can be tested rather than tuned

A tree named `dist`/`build` is admitted when, and only when, **excluding it would leave the
package with no declared entry point**: read `package.json`'s `main`, `bin`, `module`,
`exports`; if every declared entry resolves inside such a tree, that tree IS the shipped
source (`artefact=PAYLOAD`); otherwise it is a build artefact beside its own source and
stays excluded (`artefact=SOURCE`).

🟢 **This forecloses `T37`'s defect by construction.** `P144-A`'s first draft read a
committed `dist/` *and* its source and double-counted. Here the two are mutually exclusive
by rule, and the mode used is printed in a column rather than assumed —
`@n35da/brightspace-mcp` is the one npm row that reads `SOURCE`, and it is the one row
p143 managed to measure.

## Results

All 24 subjects: [`result.2026-10-12-p145.tsv`](result.2026-10-12-p145.tsv).

| tier | p143 | p145 | servers seen |
|---|---|---|---|
| npm | 100% (n=1) | 🔴 **50%** | 🟢 **1 → 8** |
| agent | 50% | 50% | 4 |
| github-only | 33% | 33% | 6 |
| foundations | 0% | 0% | 1 |

🔵 **Only the npm tier moves, and it moves because it went from one row to eight.** The
github-only and agent tiers are unchanged, which is the control: this probe's handler shape
touches no row that `REG_JS` was already reading correctly.

## Limits, stated rather than hidden

- 🔴 **One level of identifier resolution.** `resolve_array` does not follow a function
  call, so `JS_LIST_HANDLER_FROM_CALL` and `_SPREAD_CALL` mean *"this instrument cannot
  bound it"*, not *"the surface is unbounded"*. `surface_bound` resolves `@imazhar101`
  deeper and gets 227; both readings are published rather than reconciled by fiat.
- 🔴 **`BOUNDED_STATIC` still bounds from above only.** Lexical analysis does not prove
  reachability — `p140`'s limit, carried over unchanged.
- 🟡 **`lib` and `out` are in `BUILT_TREES` but not in `SKIP_DIRS`**, so they were never
  excluded and need no admission. They are listed for the next shelf that adds a row
  shipping `out/`.

## Run it

```
python3 surface_gate3.py "<subject>=<path>=<tier>" …      # TSV on stdout, tier shares on stderr
python3 test_surface_gate3.py                             # 14 tests
```

🟢 **14 tests, each pinning a defect that was real** — two on the payload exclusion
(including `test_unpatched_exclusion_would_walk_zero_files`, which pins the measured
defect itself), one per handler shape, one that `REG_JS`'s path is untouched, and one that
a `name:` without a schema is metadata rather than a tool.
