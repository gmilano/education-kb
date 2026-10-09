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

---

## 🔴 Pass 78 of 2026-10-09 — this gate **could not be executed**, and the artefacts beside it are not its output

🔴 **`[Code from External]` denied every execution path from the clone this pass** — not only the network ones. Measured on three widening cases, newest first:

| attempted | result |
|---|---|
| `bash lib/test_probe_payload.sh` (network half) | 🔴 **DENIED** |
| `lib/measure --family <file>` (the **offline** half) | 🔴 **DENIED** |
| `bash lib/test_license_family.sh` (an **offline test suite**) | 🔴 **DENIED** |
| `bash -n` on `shelf_gate.sh`, `probe_payload.sh`, `license_family.sh` | 🟢 **all parse clean** |

🔵 **`P860`: the boundary this pass measured is *parse vs execute*, not *network vs no-network*.** `../lib/README.md` publishes the narrower seam (and marks `. license_family.sh` 🟢 in pass 74) because that is the case it happened to try. **A capability boundary is re-measured at its narrowest case each pass.**

### What these two files ARE

* `candidates.input.2026-10-09-p78.tsv` — the 45 battery candidates, in this gate's input shape (`limb <TAB> label <TAB> word-bounded-ERE`).
* `inline-result.2026-10-09-p78.tsv` — verdicts produced by running **this gate's primitives inline**, by hand, with its rules honoured:
  * `P853` — corpus is tracked `.md`/`.tsv`, **348 live files**, with `.git/` and `archive/` excluded;
  * `P849` — the positive control ran **first**: `Moodle` 128 · `Open edX` 16 · `IESALC` 11 · `IDB` 7, all non-zero, so the zeros are interpretable;
  * `P840` — the substring count is printed beside every word-bounded count.
* Result: **45 candidates · 41 SHELVED · 4 UNSHELVED.**

🔴 **They are NOT `shelf_gate.sh` output and must not be cited as one.** 🟢 Each `SHELVED` verdict was additionally spot-checked with a literal `grep -F` — the `P853` direction, because a false `SHELVED` **suppresses** a finding.

### 🔴 What the next pass with execution owes this directory

1. Run `./shelf_gate.sh <kb-root> candidates.input.2026-10-09-p78.tsv` and **diff it against `inline-result.2026-10-09-p78.tsv`**. Any divergence is a defect in the hand-run, in the gate, or in the corpus — and all three are worth knowing.
2. `P862` — add the **lowercase** filenames to `../lib/probe_payload.sh`'s `PROBE_NAMES` (`license`, `license.txt`, `license.md`, `licence`, `copying`). `raw.githubusercontent.com` is case-sensitive and every name in the current ladder is uppercase-first, so **`frappe/erpnext` reads as `NO-PAYLOAD`** while `develop/license.txt` returns `200` (**GPL-3.0, 35 149 B**). Pin it as the named regression case.
3. `P859` — add `zijinz456/OpenTutor` (**1 068 B**, trailing-newline run **1**) and `aureuserp/aureuserp` (**1 077 B**, trailing-newline run **0**) as regression cases for `../p837-payload-measure/`. The second is the load-bearing one: **a payload whose trailing-newline run is zero must not be "corrected" upward.**

🔵 **`P861`, which is why points 2 and 3 are written here and not fixed here:** a denial suspends **execution**, not **knowledge**. The hand-rolled replacement this pass used reproduced two defects `probe_payload.sh` documents in its own source — it counted a **`404: Not Found` body as a 14-byte payload**, and reported a **dangling README licence link as a bare absence**. Both were caught by reading that source. **And `P126` is why no new instrument was written: the versioned one must be run before a hand-written one is committed, and it could not be run.**
