---
industry: education
region: Global
updated: 2026-10-12
---

# `p143-surface-gate-repair` — `ACTION DM`: the falsifier FIRED, and for a worse reason than it named

🔴 **`T30`'s three figures are withdrawn.** The GitHub-only tier's dynamic-registration
share moves from **50% to 33%** — a **17-point** move against a falsifier that withdrew
all three figures on anything over five.

## What was registered

> 🔴 **`ACTION DM`** — repair `p141-agent-surface-gate` for `REFLECTION` (bare decorator
> wrapping `server.tool`, name from `fn.__name__`) and for multi-line decorators, then
> re-run all three tiers.
> 🔴 **Refuted if re-running changes any tier's dynamic share by more than five points**
> — which would mean `T30`'s three figures were measured with an instrument blind to a
> third of its subjects, and **all three must be withdrawn**.

## The defect, located in one line rather than guessed

p141 scans **line by line**:

```python
for i, line in enumerate(lines):
    m = REG_PY.search(line)        # REG_PY = r"@(?:\w+)\.tool\s*\(([^)]*)\)"
```

🔵 **Every failure below follows from that.** `@mcp.tool(` alone on a line has no `)` on
that line, so `([^)]*)\)` cannot match.

## Four static shapes, not two

The pre-registration named two. 🔴 **There are four, and the two it did not name are the
ones that moved the number.**

| shape | example | p141 | repaired |
|---|---|---|---|
| multi-line decorator | `@mcp.tool(\n  annotations={…},\n)` | 🔴 invisible | 🟢 `LITERAL` |
| indirection decorator | `@_tool` where `_tool` → `server.tool(…)(fn)` | 🔴 invisible | 🟢 `LITERAL` |
| 🆕 **call-applied decorator** | `server.tool(annotations=x)(get_grades)` | 🔴 invisible | 🟢 `LITERAL` |
| 🆕 **single-line decorator with no `name=`** | `@mcp.tool(description="…")` | 🔴 **`DYNAMIC`** | 🟢 `LITERAL` |

🔴 **The fourth is the one that mattered and nobody had registered it.** p141 classified
any `@x.tool(…)` without a literal `name=` as dynamic. That is not blindness — it is a
**misclassification**, and it inverts the verdict rather than dropping the row.

## The row that moved, and why no share-based falsifier could have caught it

`krzysztofbury/librus-mcp`:

| | p141 | repaired (shipped tree) |
|---|---|---|
| literal sites | 🔴 **0** | 🟢 **35** |
| dynamic sites | 🔴 **23** | 🟢 **0** |
| verdict | `DYNAMIC_UNBOUNDED` | 🟢 `BOUNDED_STATIC` |

🔴 **And not one of p141's 23 sites is in the server the package runs.** They are 21 in
`legacy_reference/src/server.py` and 2 in `scripts/qualify_native.py`. The real surface is
**35 `server.tool(annotations=…)(fn)` calls** in `src/librus_mcp/`, a shape p141 had no
pattern for.

🔵 **This instrument's own first draft reproduced the same error** — it reported those same
23 sites, merely relabelled `LITERAL`. The tier share was **identical** both times, so a
share-based falsifier would have passed a measurement drawn entirely from dead code.
🔴 **`NOT_SHIPPED` exists because of that**, and `test_not_shipped_trees_are_excluded`
pins it.

## Validation: two independent hand counts the instrument had to hit

🟢 **The repair is checkable against numbers this KB already holds, and it hits both
exactly.**

| row | independent count | source of that count | repaired instrument |
|---|---|---|---|
| `oliverhruby/edupage-mcp` | **31** | p142's hand read (*"31 of 31 tools carry a declared `ToolAnnotations` class"*) | 🟢 **31** |
| `malkreide/global-education-mcp` | **10** | the repository's own committed `tools.lock.json` | 🟢 **10** |

🔵 **Hitting 31 required one more correction.** The forwarding call inside `_tool`'s own
body is the *mechanism*, not a tool; counting it gave 32. `test_indirection_body_is_not_counted_as_a_tool` pins it.

## Tier shares: before, after, and the one tier that cannot be measured here

| tier | p141/p142 published | repaired | move | falsifier |
|---|---|---|---|---|
| agent servers | 50% (2 of 4) | **50%** (2 of 4) | **0 pts** | silent |
| GitHub-only connectors | 50% (3 of 6) | 🔴 **33%** (2 of 6) | 🔴 **−17 pts** | 🔴 **FIRES** |
| npm connectors | 12% (1 of 8) | 🔴 **not measurable** | — | see below |

### 🔴 The npm figure was never produced by this instrument at all

7 of 8 npm packages ship **only compiled output** — `dist/` or `build/` — and both
instruments skip compiled trees. Run through `surface_gate.py`, 7 of 8 read
`NOT_AN_MCP_SERVER`.

🔴 **So `T30`'s npm 12% came from `p140-live-surface-bound/surface_bound.py`, a different
instrument reading a different artefact kind.** The agent and GitHub figures came from
`surface_gate.py` over source trees. 🔵 **`T30` compared three numbers produced by two
instruments over two artefact kinds, and presented them as one gradient.**

That is not a second-order quibble: a literal-vs-dynamic classification over a **minified
bundle with its dependencies inlined** is not the same measurement as one over source.
🟢 **Adopted as `T36`.**

## What replaces the withdrawn figures

🔵 **One instrument, one artefact kind, one tier at a time.** On source trees, with the
four static shapes seen and dead trees excluded:

| tier | servers | `BOUNDED_STATIC` | `DYNAMIC_UNBOUNDED` | `GATED` |
|---|---|---|---|---|
| agent servers | 4 | 2 | 2 | 🟢 **0** |
| GitHub-only connectors | 6 | 4 | 2 | 🟢 **0** |
| foundations (`global-education-mcp`) | 1 | 1 | 0 | 🟢 **0** |

🟢 **`GATED` is 0 of 11 servers**, which leaves `T28`'s rescoped claim standing: exactly
one row on these shelves gates registration, and it is not in this population.

🔴 **The npm tier is absent from that table and must stay absent until it is measured on
source.** Only `@n35da/brightspace-mcp` publishes source; **n=1 is reported as n=1**.

## Run it

```
python3 -I surface_gate2.py subject=path=tier [...]     # result.2026-10-12-p143.tsv
python3 -I test_surface_gate2.py                        # 10 tests, all pinning a real defect
```

`baseline-p141-instrument.2026-10-12-p143.tsv` is p141's instrument run **unmodified** over
the same 24 subjects, so the comparison above is reproducible rather than quoted.

🔵 **JS, Go and PHP handling is carried over byte-identical from p141**, deliberately: all
four repaired shapes are Python, so the npm tier's JS result moving would have meant the
rewrite leaked. It did not move.
