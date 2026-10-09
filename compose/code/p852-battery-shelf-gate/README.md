---
industry: education
region: Global
updated: 2026-10-09
---

# `P852`/`P853` — the battery's candidates gated against the shelf by an ARTEFACT

Artefacts of the **seventy-seventh pass (2026-10-09)**. Offline except for the corpus it reads;
single file on purpose (`Gap 300`).

## What this exists for

🔴 Four consecutive passes reported the discovery battery **saturated** by comparing each
candidate against the shelf **from recollection**, inside the prose of the pass that wrote it.
🟢 This gate makes the comparison an artefact: its input is a TSV of candidates, its output is a
TSV of verdicts, and both are committed beside the pass that produced them.

```
./shelf_gate.sh <kb-root> <candidates.tsv>
# candidates.tsv:  limb <TAB> label <TAB> word-bounded-ERE
```

## The rules it enforces

| rule | what it does here |
|---|---|
| `P840` | every count is **word-bounded**, and the **substring** count is printed beside it |
| `P849` | four tokens known to be PRESENT are measured FIRST; **any zero aborts the run** |
| 🆕 `P853` | the probe **excludes its own directory**, `.git/` and `archive/` from the corpus |

## 🔴 The finding this suite exists to remember

🔴 **The first run of this gate was contaminating its own corpus, and no verdict looked wrong.**

🟢 `candidates.input.tsv` and `result.2026-10-09.tsv` contain every candidate string **by
construction**. The probe wrote a name, greped the tree, and **found itself**. It also greped
`.git/` pack files and merged `archive/` into the live shelf.

| token | contaminated | 🟢 clean |
|---|---|---|
| `Moodle` (`P849` control) | 209 | **125** |
| `OpenEduCat` | 79 | **50** |
| `ai-agents-for-beginners` | 32 | **24** |
| `RAISE Act` | 3 | **2** |
| `UPC` | 4 | **1** |

🔵 **No verdict flipped, and that is exactly why it was dangerous.** 🔴 Every *count* was
inflated, and on the thin candidates two of three or four "shelf files" were the probe's own
scratch. 🔴 **Self-contamination biases every verdict toward `SHELVED`** — the error that
**suppresses** a finding, and therefore the precise mirror of `P849`, whose broken zero
**fabricates** one.

## The verdict vocabulary

| verdict | meaning |
|---|---|
| `SHELVED` | ≥1 live `.md`/`.tsv` file outside this probe names it |
| `ARCHIVE-ONLY` | 🟡 named only under `archive/` — **not** the same as shelved |
| `UNSHELVED` | 🟢 nothing on the live shelf names it — a candidate worth pricing |

🔴 **Never collapse `ARCHIVE-ONLY` into `SHELVED`.** An entity that appears only in a
pre-reset archive has been *dropped*, not *adopted*, and the two license opposite next actions.

## What it measured this pass

| run | candidates | shelved | 🔴 unshelved |
|---|---|---|---|
| `result.2026-10-09.tsv` — the prescribed battery | 34 | 34 | **0** |
| `trending-result.2026-10-09.tsv` — GitHub `/trending`, 3 language slices | 14 | 2 `PRE` / 3 `POST` | 🟢 **12** `PRE` / **11** `POST` |

🔵 **The two runs together are the pass's headline:** the prose battery is saturated for a fifth
pass, and the channel it could not see returned **12 unshelved repositories in the same hour**.
