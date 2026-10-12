---
industry: education
region: Global
updated: 2026-10-12
---

# p148-rust-surface — `ACTION EO` + `ACTION EP`: a Rust reader, and set identity proved

`T64` (p147) named three causes of an empty walk, and the third was **a language outside
`surface_gate.lang_of`'s map**. The row it hid is `zavora-ai/mcp-student-records` — Apache-2.0,
46 tools, a typed `mcp-server.toml` — and p147 measured it with `grep`, which is what this KB
tells itself not to do.

    python3 rust_surface.py <repo-dir>
    python3 test_rust_surface.py        # 14 tests, authored fixtures, offline

## 🟢 Result — both actions discharge, both falsifiers silent

| property | value |
|---|---|
| `.rs` files walked | **8** |
| router block | `src/server.rs`, one `#[tool_router] impl StudentServer` |
| 🟢 **router tools** | 🟢 **46** |
| 🟢 **manifest tools** | 🟢 **46** (`mcp-server.toml`, 46 `[[tools]]`) |
| 🟢 **`ACTION EO`** | 🟢 **counts AGREE** |
| 🟢 **`ACTION EP`** | 🟢 **`SET_IDENTICAL`** — `router_only` empty, `manifest_only` empty |
| duplicates | **0** router-side, **0** manifest-side |
| order | 🟢 **identical** — not required, and it holds |

🟢 **`P144-G` closes at 4 of 4.** The three earlier bidirectional pins were a SHA-256
lockfile, a classification manifest and a golden name array; this is the first that is a
**governance** artefact — a risk class and an approval flag per tool — and 🔴 **the only one
the repository does not verify itself.** `tests/manifest_test.rs` asserts `m.tools.len() == 46`
and `requires_approval` on eleven named writes, all read from the manifest. 🔴 **No test
compares the manifest's names against the router's.** 🟢 **`P32` in `compose/patterns.md` is
the CI gate that closes it.**

## Method — a brace-tracked reader, not a line grep

`#[tool(...)]` is a registration only inside the `impl` block that `#[tool_router]`
annotates. A line count cannot know that. This module:

1. finds `#[tool_router]` and the `impl ... {` that follows it;
2. tracks brace depth to find that block's extent, **ignoring braces inside string
   literals, char literals, line comments and block comments**;
3. inside the block only, pairs each `#[tool(` with the `fn` that follows it, preferring an
   explicit `name = "..."` in the attribute;
4. reads `[[tools]]` names from `mcp-server.toml` with a minimal table-array scan.

🟢 **It refuses rather than returning zero** (`T64`'s rule): no `.rs`, no `#[tool_router]`, or
no manifest yields `NO_RUST_SURFACE_READ` / `NO_MANIFEST_READ`.

## 🔵 Why `ACTION EP` is the question and `ACTION EO` is not

🔴 **Test 7 is the point of the whole module.** Two counts agreeing at 46 is compatible with
46 names on one side and 46 **different** names on the other. The fixture does exactly that:
`EO` reports `counts AGREE` and `EP` reports `SET_DIVERGENT`, naming `beta` and `delta`.
🔵 **`EO` alone would have passed a drifted repository.**

## 🆕 🔴 The negative control found a second Rust row

Run over all 50 clones, the reader finds Rust in **two** trees, not one:

| row | `.rs` files | `#[tool_router]` | verdict |
|---|---|---|---|
| `zavora-ai/mcp-student-records` | **8** | 🟢 yes | 🟢 **46, `SET_IDENTICAL`** |
| 🆕 `BetterSEQTA/DesQTA` | **31** | 🔴 no | 🟢 **`NO_RUST_SURFACE_READ` — refuses, as designed** |

🟢 **`DesQTA`'s published `NOT_AN_MCP_SERVER` holds** — it walked 427 files and found no MCP
token. 🔵 **But until this pass, nothing on this shelf could have read its tool surface if it
had one**, and nothing would have said so. 🟢 **A row can be right and unmeasurable at the
same time.**

## The 14 tests

Four pin cases a line count gets wrong — a `}` in a string, a `}` in a block comment, a
commented-out `#[tool(`, and a lifetime `'a` that a naive char-literal stripper swallows.
Four pin the **refusals**. One pins the counts-agree/sets-diverge case. The rest pin explicit
`name =`, the TOML scan's table boundary, and duplicate reporting (a set comparison would
hide a duplicated name, so it is reported separately).

    14/14 passed
