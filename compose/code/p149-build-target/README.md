---
industry: education
region: Global
updated: 2026-10-12
---

# `p149-build-target` — `ACTION FB` not refuted, and p148's "single instance" was its own key list

> 🟢 **`ACTION FB`** — state which build target every `NOT_SHIPPED` figure was measured
> against. Audit the **5** `ALLOWLIST` rows for a second target.
> 🔴 *Refuted if no other subject declares two* — which would make `librus-mcp` the single
> instance and `T68` a caution rather than a census correction.

    python3 build_target.py <clone-dir> [subject ...]
    python3 test_build_target.py       # 22 tests, authored fixtures, offline

## 🟢 Not refuted — `yourssu/soongpt-plugin` declares two targets as well

🟢 **16 subjects, 18 target rows, 2 subjects with more than one target.**

| subject | target | key | items | files in scope | 🔵 **tool sites** |
|---|---|---|---|---|---|
| `krzysztofbury/librus-mcp` | **wheel** | `packages` | 1 | 23 | 🟢 **35** |
| `krzysztofbury/librus-mcp` | **sdist** | `only-include` | 16 | 60 | 🔴 **39** → **DIVERGE** |
| 🆕 `yourssu/soongpt-plugin` | **wheel** | `packages` | 1 | 33 | **20** |
| 🆕 `yourssu/soongpt-plugin` | **sdist** | 🔴 **`include`** | 4 | 42 | **20** → 🟢 **AGREE** |
| `malkreide/global-education-mcp` | wheel | `packages` | 1 | 4 | 10 |
| `divyarthjain/vtop-bhopal-mcp` | npm tarball | `files` | 4 | 3 | 0 |
| `nirholas/ai-tutor-mcp` | npm tarball | `files` | 4 | 8 | 1 |

🟢 **`librus-mcp` reproduces p148's 35 and 39 exactly**, which is the control that licenses
every other number in the table.

## 🔴 Why p148 could not see it

p148's `PY_SHAPES` table reads `("tool.hatch.build.targets.sdist", "only-include", …)`.
🔴 **`soongpt-plugin`'s sdist uses `include`, not `only-include`** — and p148's `measure()`
returns the **first** shape it matches, which for this subject is the wheel. 🔵 **So "one
instance" was a property of a key list, not of the shelf.** This module enumerates **all**
targets and adds the three hatch pairs p148 omitted (`sdist include`, `sdist packages`,
`wheel include`).

🔵 **Same defect class as `T39` and `P148-C`**: an instrument that answers only the question
it was spelled to ask, and a count check that passes while the thing it stands for drifts.

## 🟡 `T68` splits into two claims, and only one of them generalises

| claim | after this pass |
|---|---|
| *a manifest can declare two allowlists* | 🟢 **GENERALISES — 2 of 5** `ALLOWLIST` rows do |
| *and they disagree on the published figure* | 🔴 **STILL ONE INSTANCE — `librus-mcp` only** |

🟢 **`soongpt-plugin`'s two targets agree at 20.** Its sdist adds `skills`, `README.md` and
`pyproject.toml` on top of the wheel's `src/soongpt_mcp`, and 🟢 **none of those carries a
tool-definition site** — 42 files in scope against 33, same count. 🔵 **So the two-target
*structure* is a census property and the *divergence* is not**, and `T68` should be cited as
the first rather than the second.

## 🟢 The build target behind every `NOT_SHIPPED` figure, named

| subject | the figure's target | why |
|---|---|---|
| `krzysztofbury/librus-mcp` | 🟢 **wheel** (35) | what a consumer installs; `MCP_CONTRACT.md` agrees to the token |
| `yourssu/soongpt-plugin` | **wheel** (20) | 🟢 **moot — the sdist agrees** |
| `malkreide/global-education-mcp` | **wheel** (10) | the only target it declares |
| `divyarthjain/vtop-bhopal-mcp` | **npm tarball** (0) | 🔵 **structurally single** |
| `nirholas/ai-tutor-mcp` | **npm tarball** (1) | 🔵 **structurally single** |

🔵 **An npm row cannot have a second target to disagree with.** npm publishes one tarball and
`files` is the only allowlist a `package.json` can declare, so 🟢 **`T68` cannot reach the two
npm rows at all** — a limit of the format, not a finding about the authors. 🔴 **That also
means the 5 `ALLOWLIST` rows are really 3 Python rows at risk of `T68` and 2 that are immune**,
and two of the three have two targets.

## 🔴 The defect this module produced, and the control that caught it

🔴 **Its first run read 43 sites in `librus-mcp`'s sdist scope against p148's 39** — while
reproducing the wheel's 35 exactly. 🔵 **The asymmetry was the clue**: `count_sites` ran two
regexes and `@mcp.tool(` matches both, so every decorator site was counted twice, and the
wheel scope hid it because `librus-mcp` registers with `server.tool(` and uses no decorators.
🟢 **Positions are now deduplicated by the open paren**, the sdist reproduces **39**, and the
double-count is pinned by `test_a_decorator_site_is_counted_ONCE`.

🔵 **Recorded because the direction matters**: an over-count makes the shipped surface look
*larger* than it is, which on this shelf reads as better-governed. 🟢 **It was caught before
publication by a reproduction control**, not in review.

## Files

| file | what it is |
|---|---|
| `build_target.py` | the module; enumerates every declared target |
| `test_build_target.py` | **22 tests**, authored fixtures, offline |
| `result.16.2026-10-12-p149.tsv` | all 16 surface subjects, 18 target rows |
