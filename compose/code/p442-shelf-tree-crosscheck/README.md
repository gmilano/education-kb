---
industry: education
region: Global
updated: 2026-10-25
---

# `p442-shelf-tree-crosscheck` — the ladder returns ONE row, and the cell it writes was not always measured

Two instruments, bought against two gaps that turn out to be the same mechanism:
**a correction that lives in an instrument never reaches the path that writes the verdicts.**

| Gap | What it said | What this pass did |
|---|---|---|
| `Gap 441-A` | `lib/probe_payload.sh::probe_repo` **returns on the first ladder hit**, so `P441`'s tree enumeration — built at `p441-tree-licence-enumeration`, re-run at `p444-root-vs-tree-family` — is implemented **beside** the library and not **in** it | `probe_tree_paths` + `probe_repo_all` land in the shared library, with 22 live controls in `lib/test_probe_payload.sh` (14 → 35 checks) |
| — (found here) | 🔴 **19 of the 162 payload cells this base publishes did not reproduce** | the 19 are repaired, `cell_of_file` / `lib/measure --cell` give the cell one owner, and `gate-cell-reproduction` is the standing ratchet |

## 1 · The ladder's answer is one row, and on 12 of 134 repositories that is not the whole grant

Denominator: **134 repositories** whose payload path this base publishes across its three
sell shelves (`agents/top.md`, `repos/foundations.md`, `verticals/solutions.md`), enumerated
with `p441-tree-licence-enumeration/enumerate_licence.py` **sourced, not re-implemented** —
33 s for all 134.

| | n |
|---|---|
| repositories with exactly one own-grant path | 🟢 **121** |
| repositories carrying **more than one** | 🔴 **12** |
| of those, carrying **more than one FAMILY** | 🔴 **4** |
| `ABSENCE-ENUMERATED` — no licence TEXT anywhere in the tree | 🟡 **1** |
| published path absent from the tree | 🟢 **0** |

🟢 **The one `ABSENCE-ENUMERATED` row is corroboration, not a defect.**
[`pengusto/google-classroom-mcp`](https://github.com/pengusto/google-classroom-mcp) is already
published here as 🔴 proprietary (*"Pengusto Commercial License 1.0"*, `LICENSE` 3 053 B ·
`d84e558a5033`), and the tree channel reaches the same verdict independently: 41 paths, one
licence-ish name, and its payload classifies as no licence family at all.

🔴 **The four multi-family repositories are the finding**, and one of them is sold here as a
permissive build-on row:

| repository | root grant | what else the tree carries | why it matters |
|---|---|---|---|
| [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) | MIT, `LICENSE` 1 071 B · `22e7ab2dbddc` | 🔴 **GPL-3.0, `legacy_reference/LICENSE` 35 149 B · `3972dc9744f6`, `GRANT-PRESENT`**, beside 20+ `.py` files | a client who vendors the repository takes GPL-3.0 on that subtree; integrating `librus-mcp` over its MCP interface does not |
| [`Hiepler/EuConform`](https://github.com/Hiepler/EuConform) | MIT, `LICENSE` 1 073 B · `65335056589f` | **EUPL-1.2, `LICENSE-EUPL` 13 240 B · `3dcf9c6f6119`** | dual-licensed; EUPL-1.2 is the EMEA public-sector grant and this base has **no profile for it** |
| [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | ODbL, `LICENSE` 25 289 B · `77d2692c3d64` | **CC BY-SA 4.0, `LICENSE-CONTENT` 18 375 B · `cde7883b9050`**, `CONTENT-COPYLEFT:share-alike` | **two** share-alike obligations, not one: the database and the content |
| [`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) | AGPL-3.0 | MIT ×2 + Apache-2.0 in `mathlive-assets/`, `sre-assets/` | 🟡 vendored, **not** the project's grant — see the declared limit below |

🟢 **And the inverse case, which is the stronger argument for the tree arm.**
[`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) (583 ★) has a
root `LICENSE` of **1 134 B · `3fb8cda58638`** that grades 🔴 `GRANT-BY-REFERENCE` — a notice,
not a grant — while the complete **AGPL-3.0 (34 523 B · `0d96a4ff68ad`, byte-identical to the
canonical text this base already holds twice)** sits at **`app/LICENSE`**. The ladder's answer
was not merely incomplete; it was **wrong about the project**. 🟢 Read first-hand, the notice
also carries a **dual-licensing clause** that no instrument here had joined: the `skills/`
content is available **AGPL-3.0 *or* MIT at the user's option**, and only `app/` is AGPL-only.
**There is an MIT lane in a repository this base had typed AGPL.**

## 2 · 19 published cells carried the `P834` signature, and the signature is reproduced here

`sweep_published.sh` re-measures every published cell twice: from the file
(`size_of_file` / `sha12_of_file`) and through the library's own preserved defect
(`size_of_capture_BROKEN` / `sha12_of_capture_BROKEN`).

    🟢 143  REPRODUCES
    🔴  19  CAPTURE-MEASURED   bytes short by the trailing-newline run AND a digest
                               that is the digest of the STRIPPED bytes

🔵 **That is a measured claim about how the number was produced, not an inference.** For
`GarethManning/education-agent-skills` at the pinned commit `135d6275e7db`, the file is
**1 230 B · `f952182df4eb`** and `printf '%s' "$(cat LICENSE)"` is **1 229 B ·
`40db9b472090`** — the published cell, to the digit.

🔴 **Attributed to the passes that wrote the rows**, against my own first hypothesis that the
discovery lane simply never sourced the library:

| pass | rows it shelved | capture-measured |
|---|---|---|
| `p432` | 5 | 🔴 **5** |
| `p433` | 5 | 🔴 2 |
| `p438` | 11 | 🔴 2 |
| every other pass | 113 | 🟢 0 |

🔵 So the defect is **not lane-shaped — it is intra-pass.** The same pass measured some rows
through the library and typed others by hand, and the shelf gives a reader no way to tell
which cell is which. That is why the remedy is a primitive plus a gate, not a reminder.

## 3 · Mutation results — a control that cannot fail is not a control

| mutation | controls that go red |
|---|---|
| `cell_of_file` publishes the capture digest | 1 |
| `cell_of_file` publishes the capture size | 1 |
| `group_digits` groups every four digits | 3 |
| `lib/measure --cell` emits only the size | 1 |
| the capture-digest control is made identical to the correct primitive | 1 |
| the gate counts **any** recorded verdict as green | 4 |
| the gate's key drops bytes and digest | 2 |
| the gate's key is the digest alone (cross-slug credit) | 1 |
| an empty or missing record passes | 2 |
| zero parsed cells passes | 2 |

## Declared reading limits

- 🔴 **`is_own_path()` does not know `*-assets/`.** `p441`'s enumerator excludes
  `node_modules/`, `vendor/`, `third_party/` and `.corepack/`, so `AlloFlow`'s three
  **vendored** asset grants (MathLive, Speech Rule Engine, Temml) are typed as the project's
  own. The verdict `OWN-GRANT-AT-ROOT` is right for that repository for a different reason —
  its root really is a grant — but the family list on its row is three families too wide.
  Recorded, not quietly fixed: it is `Gap 442-B`.
- ⚠️ **A second grant in the tree is a FACT, not an intent.** That `legacy_reference/LICENSE`
  is a complete GPL-3.0 is measured; whether the project means it to govern that subtree only
  is a reading of the project, and the row says so.
- 🔴 **`EUPL-1.2` has no clause profile**, so `Hiepler/EuConform`'s second grant grades
  `GRANT-UNCALIBRATED`. `p440` enumerated the unprofiled families as MPL, LGPL, EPL and BSD
  and **EUPL was not among them** — a denominator fault of exactly the shape `p310` named.
  `Gap 442-C`.
- 🔵 **`agents/trending.md` and `repos/trending.md` are out of the gate's scope** by design:
  they are append-only history, their cells were true when written, and they are not
  re-measurable at today's HEAD.

## Files

| file | what it is |
|---|---|
| `extract_published_cells.py` | the parser — every published cell on the three sell shelves |
| `sweep_published.sh` | the re-measurement, both methods, one row per cell |
| `cell_reproduction_gate.py` | the standing offline gate (`make gate-cell-reproduction`) |
| `test_cell_reproduction.py` | 21 offline controls, 11 of them negative |
| `probe_second_grants.sh` | first-hand read of every second path the tree returned |
| `second-grants.2026-10-25.tsv` | those 19 measurements |
| `published-cells.2026-10-25.tsv` · `sweep.2026-10-25.tsv` | the 162 cells, parsed and re-measured |
| `slug-first-pass.2026-10-25.tsv` | which pass first shelved each slug (the attribution table above) |
| `payloads/` | every payload this pass graded, as fetched |
