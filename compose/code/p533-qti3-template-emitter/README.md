---
industry: education
region: Global
updated: 2026-10-07
---

# P533 — `Gap 238` closed: QTI 3 parametric items can now be authored, not only delivered (pass 43, 2026-10-07)

## The gap, as pass 42 left it

`Gap 238` was declared by pass 42 and marked **"the cheapest gap on this KB… the one a
single pass could close outright"**:

> `LongsightGroup/qti3`'s `writer` cannot emit `qti-template-declaration` /
> `qti-template-processing`, so parametric item variants cannot be **authored** on the stack
> that can **deliver** them.

Reproduced first, before anything was built, at HEAD `0ca7d6fc` (2026-10-07):

| Measurement | Value |
|---|---|
| `packages/writer/src/index.ts` exports | **33** |
| …of which reference the template mechanism | **0** |
| `packages/core/src` files referencing it | **34** |
| `qti3` licence (shared classifier `../lib/license_family.sh`) | **MIT**, © 2026 Longsight, Inc. |
| `qti3` version | `0.13.2` |

So the asymmetry is real and it is the one the gap describes: the runtime implements the whole
mechanism and the authoring package implements none of it.

## What this directory contains

| File | Status |
|---|---|
| `emit_template.py` | 🟢 **Executed and tested here.** The emitter, stdlib only |
| `test_emit_template.py` | 🟢 **43 assertions, 0 failures, 19 of them negative controls** |
| `writer-contribution.ts` | 🟡 **Parse-checked only, NOT executed** — the upstream-shaped deliverable |
| `fixtures/` | The two upstream fixtures used as oracles |
| `result.2026-10-07.tsv` | The run's machine-readable record |

Reproduce:

```
python3 -I test_emit_template.py
```

## 🔴 Why the oracle is transitive, and why that is sound rather than convenient

`Gap 238` names the round-trip oracle as `core`'s parser plus the fixture. Two stronger
instruments were tried **first** and both are unavailable here. Recording which, because an
unexplained substitution is how `P469` happens:

1. **Execute `qti3`'s own suite** — not permitted. Installing a third-party repository's
   dependencies is out of scope in this environment. This is the same limit pass 42 stated
   on `P527`, and `Gap 238` already carries it as a prerequisite for whoever lands the patch.
2. **Validate against the official QTI 3.0.1 ASI schema** — `qti3` pins it by sha256 in
   `packages/conformance/schemas/qti3/sources.json`, but the schema is **fetched, not
   vendored**, and `purl.imsglobal.org:443` is refused by this environment's egress proxy
   (`connect_rejected`, organization policy). 🔴 **Same class as `Gap 56`** (eur-lex) **and
   `Gap 92`** (docs.moodle.org) — a primary source blocked, recorded rather than silently
   worked around.

🟢 **So the oracle is transitivity through a document the upstream gate has already
validated.** `scripts/check-test-xsd.mjs` runs `xmllint --nonet --noout --schema <pinned
official ASI xsd>` over `packages/fixtures/xml/*.xml` and reports *"official ASI schema
validation passed"*. A fixture is therefore a **known schema-valid QTI 3 document**. If the
emitter regenerates one **node-for-node**, its output is schema-valid by transitivity, with no
need for this environment to reach the schema at all.

🔵 **Two independent fixtures are used, not one** — `random-integer-template-reference.xml`
(four declarations, three draws, nested arithmetic, derived key) and
`template-processing-reference.xml` (two declarations, a literal, inline formatting) — so a
single hand-tuned success cannot pass as a general result. Each fixture's comparison is
controlled against the other's document.

## What the oracle actually asserts

| # | Assertion | Control that proves it can fail |
|---|---|---|
| **O1** | The complete 4-declaration parametric item is **canonically identical** to the fixture | An explicit-`step` variant is rejected by the same comparison |
| **O2** | A second, differently-shaped fixture is also regenerated | O2's comparison rejects O1's block |
| **O3** | 20 000 executed draws all land on the declared grid, and every grid point is reachable | `min=1 max=10 step=4` → grid `[1,5,9]`; a contiguous-range assumption is detectably wrong |
| **O3b** | An omitted `step` is **1**, asserted against `operator-attribute.ts:24` | An explicit `step=2` on the same bounds is not contiguous |
| **O4** | The derived answer key always solves the stem it was generated from, and **varies** | A frozen key would be caught by the variance check |
| **O5** | Constraint feasibility is computed **before** publication | An unsatisfiable constraint reports exactly 0 acceptance |
| **O6** | 10 malformed inputs refused; 7 valid ones accepted | The accept list proves the validator is not refusing everything |
| **O7/O7b** | Hostile text **and** hostile attribute values survive escaping | The raw string must not appear unescaped |
| **O8** | Children are emitted in **schema** order, not parser order | The fixture exhibits the same order |

## 🟢 The three findings the build produced that reading could not

### 1. `max` is frequently not attainable, and nothing says so

`processing-evaluator.ts:170-171` computes `count = floor((max - min) / step) + 1` and draws
`min + floor(random() * count) * step`. So the draw is over a **grid**, and when `step` does not
divide `max - min`, **`max` never occurs**. `min=1 max=10 step=4` draws from `{1, 5, 9}`.

🔴 An author reading `max="10"` as "the largest value a student can see" authors a different
item from the one delivered. The emitter therefore exposes `grid()` and the oracle asserts on
it rather than on the bounds.

### 2. An infeasible `qti-template-constraint` degrades silently into a wrong item

`session.ts:449-476` restarts on constraint failure **at most 100 times** and then
**proceeds with the violating draw** rather than raising. A constraint satisfied by few grid
points therefore produces a quietly invalid item: at acceptance probability `p`, exhaustion
has probability `(1 - p) ** 101` — ~0.5% at `p = 0.05`, but ~90% at `p = 0.001`.

🟢 `estimate_constraint_restarts` computes acceptance exactly over the cartesian product of the
declared grids, so this is checkable at authoring time. 🔴 It is invisible in the XML.

### 3. Parser order and schema order are different orders

`core` finds children by name (`childElements(node, …)`) and so accepts any order; the XSD
declares a sequence. 🔴 **An emitter written against the parser would produce documents that
deliver correctly and fail validation** — the worst failure mode available, because the
authoring tool's own test would pass. `build_parametric_item` emits in schema order and `O8`
pins it against the fixture.

## 🔴 The two defects mutation testing found in this pass's own oracle

The suite passed 38/38 before it was mutation-tested. It was then run against 11 deliberate
mutations of the emitter, and **two survived** — the oracle was passing while not judging:

| Mutation | Why it survived | Fix |
|---|---|---|
| **M8** — `step` defaults to `2` instead of `1` | `O3.grid` and `O3.cover` both compare the draw against `grid()`, and **both sides derive from `effective_step`**, so a wrong default is self-consistent and invisible. The round-trips miss it too, because a defaulted `step` is never emitted | 🟢 `O3b` asserts the default against the **external source** (`operator-attribute.ts:24`), not against another expression of itself |
| **M9** — drop `"` → `&quot;` in `_escape_attr` | Every attribute value in the suite happened to be quote-free | 🟢 `O7b` round-trips a `title` containing `"`, `<` and `&` |

🔵 **This is `P469`'s shape in miniature: a value asserted from itself is not measured.** And
`P471`'s: a gate can pass every assertion while judging nothing. 🟢 Neither defect was
findable by reading the suite; both required mutating the thing under test.

A third defect was found the same way: **M4** (drop text escaping) *was* detected, but as an
uncaught `ParseError` traceback rather than a reported failure — on a board a crash is
indistinguishable from a broken runner. `check_call` now reports an assertion's own exception
as a failure.

### Mutation matrix, after both fixes

```
M0  baseline (unmutated)                     43 passed,  0 failed
M1  always emit step                         41 passed,  2 failed
M2  grid off-by-one                          39 passed,  4 failed
M3  drop identifier validation               39 passed,  4 failed
M4  drop text escaping                       41 passed,  2 failed
M5  schema child order -> parser order       40 passed,  3 failed
M6  allow step<=0                            41 passed,  2 failed
M7  allow min>max                            42 passed,  1 failed
M8  wrong default step      (survived before) 41 passed,  2 failed
M9  drop attr quote escaping(survived before) 41 passed,  2 failed
M11 grid truncates last point                38 passed,  5 failed
M12 restored baseline                        43 passed,  0 failed
```

🟢 **11 of 11 mutations now detected, and the baseline returns to clean** — the last row
matters, because a matrix that cannot get back to 0 failures is measuring its own damage.

## 🟡 What is NOT closed, stated rather than implied

- 🔴 **The TypeScript is not executed.** `writer-contribution.ts` is **parse-checked only**
  (`node --experimental-strip-types --check`, after stripping imports that need `qti3`'s tree).
  That proves syntax, **not types and not behaviour**. The Python module is the tested artefact.
- 🔴 **Nothing has been contributed upstream.** This KB produced the patch; landing it in
  `LongsightGroup/qti3` is a pull request this pass did not open, and opening one is outside
  what a KB pass should do unprompted.
- 🟡 **`qti3` is at `0.13.2`** — pre-1.0, and its HEAD moved on the same day this was read.
  The emitter targets a grammar that can still change.
