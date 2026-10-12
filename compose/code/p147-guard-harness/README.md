---
industry: education
region: Global
updated: 2026-10-12
---

# p147-guard-harness — `ACTION EJ`, wired AROUND the five rather than into them

> 🟢 **`ACTION EJ`** — wire the guard into the five at-risk instruments.

🔴 **The literal form edits five files whose bytes produced published figures.** p145 faced
the same choice and answered it the other way: it repaired `surface_gate2.py` in a
**successor**, which is the only reason it could report *"baseline reproduces p143 row for
row"* and attribute every difference to its own two changes. 🔵 **Edit the original and that
sentence becomes unverifiable for every future pass.** So the guard is wired around each
instrument, calling the instrument's **own** enumeration and refusing at zero.

    python3 guard_harness.py <root>...     # (root, instrument) pairs
    python3 test_guard_harness.py          # 9 tests, authored fixtures, offline

🟢 **Nothing is duplicated** — `P146-D` showed what happens to a census that carries the
tokens it counts, and a test asserts this module holds no copy of any exclusion set.

## Result, 2026-10-12

| population | pairs | refused |
|---|---|---|
| 8 npm payloads → 2 measured here | **10** | 🔴 **10 of 10** |
| 44 connector clones | **220** | 🟢 **2** |

🔴 **All five instruments would be refused a verdict on both npm payloads** — which
confirms `P146-D`'s capability census empirically rather than by reading code.

🔵 **And it separates two causes p146 had merged.** The two `os.walk` gates read zero
because `dist`/`build` holds the whole payload (`T42`). The three `git ls-tree` instruments
read zero because `git` answers *"not a git repository"* — a tarball is not a tree at all
(`T59`). 🟢 **Both are instrument-failure states and the guard catches both**, but only the
first is an exclusion-list problem.

## 🆕 `T64` — an empty walk has THREE causes, and the third was found by the control

🔴 **`zavora-ai/mcp-student-records` is refused by both `os.walk` gates and passes all three
git instruments.** 2 of 220 pairs, found while running the negative control.

🔴 **It has no `dist/` and no `build/`.** It is **Rust** — `Cargo.toml`, `src/*.rs` — and
`surface_gate.lang_of` maps `.py .js .mjs .cjs .ts .go .php` and **not `.rs`**. 🔵 **So the
walk is empty because the payload's language is outside the instrument's map**, a third
cause alongside the exclusion and the artefact kind.

| cause | example | rows |
|---|---|---|
| 🔴 exclusion drops the payload | npm `dist/` tier | **7** (`T42`) |
| 🔴 artefact is not the kind read | tarball vs `git ls-tree` | **8** npm (`T59`) |
| 🆕 🔴 language outside the map | `.rs` | **1**, and it is a real server |

🔵 **One guard catches all three**, because all three are the same question — *did I read
anything at all?* — and that question has one right answer in every artefact kind.
