# `p144-npm-source-parity` — `ACTION DP`

> Measure the npm tier on SOURCE, so `T36` has a test rather than an example.
> 🔴 *Refuted if the two counts agree within one tool on 6 of 8 or more.*

## Verdict: 🔴 **DISCHARGED and REFUTED on every row it could reach — and the threshold was unreachable**

🟢 **Bundle and source agree EXACTLY on 3 of 3 measurable packages — not within one tool, but
to the tool name.** 🔴 **5 of 8 packages have no reachable source at all**, so the registered
`6 of 8` threshold could never have been evaluated, in either direction.

| package | bundle (`surface_bound.py`) | shipped source (same instrument) | name sets |
|---|---|---|---|
| `canvas-mcp-server@2.2.3` | **54** | 🟢 **54** | 🟢 identical (55/55 under the set extractor) |
| `moodle-mcp-server-aql@0.1.7` | **14** | 🟢 **14** | 🟢 identical |
| `mcp-canvas-lms@1.0.5` | **3** | 🟢 **3** | 🟢 identical |

🔵 **Set identity is the result, not count identity.** Two trees can both read 14 and name
different tools; `namesets.py` compares the sorted name sets and reports `bundle_only` and
`source_only`, both of which are empty on all three rows.

## 🔴 The disagreement that appeared first, and why it was NOT an artefact-kind effect

The first run read **54 → 0**, **14 → 3**, **3 → 3** and would have corroborated `T36`
emphatically. 🔴 **It was wrong, and the cause is `T37` in a second probe.**

- `canvas-mcp-server` and `mcp-canvas-lms` **commit their own `dist/`**. A clone therefore
  contains the source *and* a stale bundle, so `surface_bound.py` — which has **no
  `NOT_SHIPPED` exclusion of any kind** — counted 3 and 2 server instances respectively and
  suppressed the count as `MULTI_SURFACE`.
- `moodle-mcp-server-aql` is a **monorepo**; the full tree offered `packages/client`
  (4 names, 3 tools) alongside `packages/server` (14).

🟢 **Restricted to the tree each package actually ships, all three return the bundle figure
exactly.** 🔵 **So the artefact kind was never the variable — the population was.**

## 🔴 Why 5 of 8 rows cannot be measured, stated per row

| package | source route | outcome |
|---|---|---|
| `@owen-x-tech/canvas-mcp@1.1.0` | `repository: owentaylor/canvas-mcp` | 🔴 **declared and DEAD** — `git ls-remote` prompts for credentials |
| `mcp-canvas-lms@1.0.5` | 🟢 `homepage`/`bugs` → `MisterCommand/mcp-canvas-lms` | 🟢 cloned |
| `@imazhar101/mcp-canvas-server@2.1.3` | none | 🔴 no `repository`, `homepage` or `bugs` |
| `@ink-waffle/moodle-mcp@0.2.0` | none | 🔴 **18 `.map` files, zero `sourcesContent`** |
| `@n35da/brightspace-mcp@0.4.0` | none | 🔴 no pointer |
| `eth-moodle-mcp@1.3.3` | none | 🔴 no pointer |

🔵 **`mcp-canvas-lms` is the useful correction to `P138-H`**: that row was recorded as having
no `repository` field, which is true, and it is placeable anyway from `homepage`. 🔴 **The
sourcemap route was tested and is dead** — three packages ship `.map` files and not one
carries `sourcesContent`, so a map gives original *path names* and no original *bytes*.

## Consequence for `T36` and `T30`

🔴 **`T36`'s central example collapses.** `T36` was adopted on the claim that npm was measured
over bundles while other tiers were measured over source, making the figures incomparable. On
every row where both artefacts exist, **they are the same measurement**. 🟢 **`T30`'s npm
figure should be reinstated on these grounds**, as `ACTION DP` itself specified.

🔵 **What survives of `T36` is narrower and still true**: `surface_gate2.py` and
`surface_bound.py` are not interchangeable — they count different things (registration *sites*
versus tool *descriptors*), and `surface_gate2.py` reads **0** on all three of these packages
in both artefact kinds, because they register through
`setRequestHandler(ListToolsRequestSchema, …)` and it has no pattern for that shape.

## Channel note

🔴 **`curl -sI https://github.com/<owner>/<repo>` returns `403` in this environment for every
repository, live or not**, so it cannot verify a repository URL. 🟢 **`git ls-remote` and
`git clone` both work and distinguish the cases**, and are what this probe uses.

## Run

```bash
python3 -I namesets.py label=<bundle-dir>=<shipped-source-dir> [...]
```
