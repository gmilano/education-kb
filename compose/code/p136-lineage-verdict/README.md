---
industry: education
region: Global
updated: 2026-10-11
---

# `p136-lineage-verdict` — `ACTION BU` and `ACTION BW` discharged, and p135's "verdict" demoted to a candidate

**Pass 136, 2026-10-11.** `ACTION BU` asked for p135's README-byte-identity mirror detector to be
run **across the whole corpus**, predicting refutation *"if fewer than 2 further cross-owner
identical-README clusters exist."* `ACTION BW` asked whether the four `api_enem_microdados`
repositories are really clones, predicting refutation *"if the source trees differ substantially."*

🟢 **Both discharged. Neither refuted.** 1 389 READMEs fetched over 1 528 published rows;
**71 byte-identical clusters**, of which **25 are cross-owner** — twelve times the threshold.
🔴 **And running it at corpus scale falsified the sentence p135 wrote about its own detector:**
*"a shared licence body proves nothing … which is why licence grouping is a lead and README
identity is a verdict."* **README identity is a lead too.**

## The defect, in one row

| cluster | what README identity says | what the refs say |
|---|---|---|
| `jdolny/OneRoster.NET` + `theopenem/OneRoster.NET` | two owners, byte-identical README → a mirror | 🔴 **identical ref set** — ONE repository, served under a slug GitHub still answers after a rename |

**11 of the 25 cross-owner clusters are that case.** A detector that stops at README identity
reports eleven mirrors that do not exist, and it reports them in a corpus where this KB has already
pinned rows by owner — `agents/top.md` says *"both licences name `theopenem` as copyright … so pin
`theopenem/OneRoster.NET`"*, a conclusion reached about what is now measured to be a single repo.

## 🔵 What this builds on, and the one thing it corrects

`compose/code/p989-sha-identity-fork/` (pass 97) already established the channel and the first
version of the test: *"`git ls-remote` costs one round trip, needs no token, and answers the
identity question through the only channel that is open"*, published under the heading
**"two slugs at the same HEAD SHA are one repository"**.

🔴 **That heading is wrong, and p989's own body shows why** — it labels `CHINOBv/OpenPronounce`,
at the same HEAD SHA as the upstream, *"a non-diverged fork"*, which is not the same thing as the
same repository. **This corpus contains 4 same-HEAD pairs that are forks** (`moodler-mcp` 2 refs
vs 17, `purdue-mcp`, `mcp-brasil` 48 vs 50, `awesome-eu-ai-act`). 🟢 **The fix is one more field
from the same round trip: the REF SET.** Two slugs for one repository serve *every* ref
identically; a fork at the tip serves the same HEAD and a different ref set.

🔵 **Re-measuring p989's own sample also dates it:** `Ronald-TR/OpenPronounce` was
`f43079b80fcbef` on 2026-10-10 and is `d08f355381f1` today.

## What it measures, and in which order

Order is the whole instrument. Two slugs for one repository necessarily share HEAD, so checking HEAD
before the ref set calls a rename a fork.

| step | measurement | cost |
|---|---|---|
| 1 | `README.md` sha256 via `raw.githubusercontent.com` | 1 GET per repo |
| 2 | **ref-set sha** — `git ls-remote --heads --tags`, sha256 of the sorted sha list | 1 ls-remote |
| 3 | HEAD commit sha | same ls-remote |
| 4 | shared commit shas — `git rev-list` over a bounded clone | 1 shallow clone |
| 5 | **root tree sha** — `git rev-parse HEAD^{tree}` | same clone |
| 6 | commit count, and the file list for `licence_dropped()` | same clone |

## The six verdicts

| verdict | the evidence | what it means for a shelf |
|---|---|---|
| `ALIAS` | identical ref sets | 🔴 **a KB data defect** — two rows, one repository |
| `FORK_AT_TIP` | same HEAD, different ref sets | 🟡 supply inflation; count once |
| `DIVERGED_FORK` | different HEAD, shared commit shas | 🟡 supply inflation; the fork may still be the live one |
| `ATTRIBUTION_STRIPPED_COPY` | **identical root tree, zero shared commit shas** | 🔴 the history was replayed under another identity |
| `SQUASHED_COPY` | different tree, zero shared commits, **one side a single commit** | 🔴 re-upload without history; check `licence_dropped()` |
| `UNRESOLVED` | steps 4–6 were not run | 🔵 **said, not guessed** |

`UNRESOLVED` exists because the failure this instrument is built against is publishing a verdict
from a measurement nobody took. Three clusters carry it; they are named in the result file.

## Result on this corpus

```
ALIAS 11 · DIVERGED_FORK 5 · FORK_AT_TIP 4 · UNRESOLVED 3
ATTRIBUTION_STRIPPED_COPY 1 · SQUASHED_COPY 1          (25 cross-owner clusters)
CASE_VARIANT 37 · SAME_OWNER_ALIAS 6                    (46 further clusters, no finding)
```

🔴 **The 37 `CASE_VARIANT` clusters are this KB citing one repository under two spellings** —
`Elgg/Elgg` and `elgg/elgg`, `Schroedinger-Hat/certo` under **three** spellings, eight
`Opetushallitus/*` pairs. That is `p443`'s case-collision class, measured across the whole corpus
for the first time, and it is why `same_slug()` runs before anything else.

## `ACTION BW` — the ENEM cluster, at source level

🔴 **"Clone" was too weak, not too strong.** All four repositories share the **root tree sha**
`a847c05fb690b23ec6255d17de4542b3416ce562`, 20 commits each, identical commit messages and dates —
and **not one shared commit sha**, because every commit was re-authored:

| repo | commit authors | HEAD |
|---|---|---|
| `filipedeschamps/api_enem_microdados` *(original, created 2022-07-25)* | Filipe Deschamps, OtavioVB | `1e8d72ebc1fe` |
| `rendgentmars/api_enem_microdados` | `rendgentmars` | `988d4d9c1c3c` |
| `livrunakcream/api_enem_microdados` | `livrunakcream` | `0743bc1408dc` |
| `bluesky816/api_enem_microdados` | 🔴 **`garu2044x`** — a fifth identity; the owner is not even the rewritten author | `17af4e419096` |

The files are byte-identical. The only thing changed is who the history says wrote them. 🔵 Stated as
a measurement of authorship fields, not as a legal conclusion.

## Why `licence_dropped()` is in here

`0awei0/kt` carries `hcnoh/knowledge-tracing-collection-pytorch`'s README byte-for-byte
(`55e2f536ac87f2893dc89463`) in **one commit**, with `__pycache__` and checkpoints included — and
**without the upstream `LICENSE` file**. Upstream is **MIT (Hyungcheol Noh, 2022)**; the copy reads
as unlicensed to any probe that looks for a licence filename.

🔴 **So a licence verdict belongs to a lineage, not to a slug** — the same error as this pass's
`pipwerks` correction, in the opposite direction: there, a missing `LICENSE` file was read as a
missing grant when the grant sits in `package.json` and the source header.

## Running it

```
python3 -I test_lineage.py      # 10 tests, every fixture a value measured on 2026-10-11
```

`python3 -I` does not put the script directory on `sys.path`; the test file inserts it, so the
instrument runs under the isolated interpreter the harness rules ask for. No `pytest` in this
environment.

## Files

| file | what it holds |
|---|---|
| `lineage.py` | the six verdicts, `same_slug`, `cluster_verdict`, `attribution_rewritten`, `licence_dropped` |
| `test_lineage.py` | 10 tests over measured fixtures |
| `clusters.2026-10-11-p136.tsv` | all 71 README-identity clusters, classified |
| `lsremote.2026-10-11-p136.tsv` | ref-set and HEAD measurements for the 55 cross-owner slugs |
| `result.2026-10-11-p136.tsv` | the 25 cross-owner clusters with verdicts and the evidence behind each |

## 🔴 What this instrument does NOT do

- It reads **one** payload (`README.md`) at **one** path on **main** then **master**. 139 of 1 528
  rows returned no README at either; a cluster among those is invisible here.
- `UNRESOLVED` is not "unrelated": three clusters were left at ref level because resolving them
  needs a clone each and they are not education-supply rows.
- It cannot tell a **fork** from an **upstream** without dates; `FORK_AT_TIP` says which rows to
  count once, not which row to cite.
- Nothing here measures *why* a tree was copied. A shared template, a course exercise and a
  deliberate re-upload all land in the same two verdicts.
