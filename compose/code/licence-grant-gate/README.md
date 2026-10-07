---
industry: education
region: Global
updated: 2026-10-07
---

# licence-grant-gate — the instrument of `P453`–`P459` (pass 32, 2026-10-07)

**What it measures.** Whether a repository **grants** a licence — not whether a file exists at a
path that usually holds one. Those are different questions, and this KB had been answering the
second while publishing the first.

```
python3 test_grant_gate.py     # 47 checks, offline, no network
```

🟢 **Result this pass: `47/47` green offline, and `12/12` live cases reproduce the pass-32
verdicts** (the live list is in the pass-32 section of `agents/trending.md`; the harness is
`probe_repo`, whose transport is injectable precisely so the suite needs no network).

## Why it exists

Pass 31 established the environment: `curl -sI` on a github.com landing page returns **403**, so
HEAD is not an existence test. This pass re-measured that and found **two more closed channels** —
`curl` **GET** on the same page is also **403**, and `api.github.com` is **403**. Three channels,
three refusals, so `raw.githubusercontent.com` is the only route and **no star count is readable**.

Then the prober built on that channel was run against repositories whose correct answer was already
known. **It was wrong six ways.** Every defect is recorded here with a **negative control** that
proves the original failure is still detectable — a suite that only records today's behaviour
guards nothing.

| ID | Defect | Direction of the error |
|---|---|---|
| `P453` | `raw.githubusercontent.com` paths are **case-sensitive**; the probe list lacked `LICENSE.TXT` | 🔴 **deletes a true row** |
| `P454` | existence fallback probed only `README.md`, so `.rst` projects looked non-existent | 🔴 **deletes a true row** |
| `P455` | 🔴 **a `200` on a `LICENSE` path is not a grant** | 🔴 **publishes an all-rights-reserved repo as licensed** |
| `P456` | a licence family in a README's *requirements* section is not a licence claim | 🔴 **inverts a commercial answer** |
| `P457` | README-hash de-duplication misses a **renamed** fork | 🟡 double-counts one project as two |
| `P459` | holder scraped from a long-form licence **body** returns boilerplate | 🔴 **merges two unrelated repos as forks** |

## The findings, with their proofs

### `P453` — the path is case-sensitive

Negative control, run live: `pykt-team/pykt-toolkit/main/LICENSE` **200**, `…/license` **404**,
`…/LiCeNsE` **404**. And `openedx/XBlock` keeps its grant at **`master/LICENSE.TXT`** — a caps
extension. 🔴 **A probe list without that spelling returns `ABSENT` for a real, correctly licensed
Apache-2.0 repository that was already on this shelf.** `LICENCE_PATHS` now carries 16 spellings.

### `P454` — not every project writes Markdown

`openedx/XBlock` has `master/README.rst` **200** and **no** `README.md`. The existence fallback
reported a live repository as missing. `EXISTENCE_PATHS` now includes `README.rst`, `README.txt`,
`pyproject.toml` and `package.json`.

### `P455` — existence was never the test; the grant is the test

[`murderszn/open-tutor`](https://github.com/murderszn/open-tutor) serves **869 bytes** at
`main/LICENSE`:

> *"This repository has not declared a project-wide reuse license. This notice documents that status
> and does not grant additional rights… A public GitHub repository is not itself a declaration of an
> open-source or open-content license."*

🔴 **The file exists, is correctly named, returns 200, and refuses the grant.** `reads_as_grant`
returns `granted=False` with state `NON-GRANT`. 🔵 This is a *new shape of signal and it will
spread*: maintainers are learning that silence reads as permission, so some now publish an explicit
refusal where a licence would go. Good practice upstream, and it breaks every existence-based
scanner. ⚠️ Every other licence defect in this KB's history moved a row between two **real**
licences, where the error is a wrong *degree* of freedom. This one is binary.

### `P456` — check the word's role, not its presence

[`formalms/formalms`](https://github.com/formalms/formalms) publishes **no grant** (16 filenames ×
3 branches, all 404; the repo is real — `master/README.md` 200). The **only** "Apache" in its README
is:

```
- Apache (recommended) with mod_rewrite enabled
```

A secondary source rendered that as *"an open-source fork of Docebo with Apache 2.0 license, so
modified versions deploy and distribute without the copyleft obligations GPL and AGPL carry."*
🔴 **A web server in an install prerequisites list became a licence grant, and then became the exact
commercial conclusion that error produces.** ⚠️ Forma's Docebo lineage is **GPL** — the opposite.
*Apache*, *nginx*, *MIT* and *BSD* are each simultaneously the name of a licence and the name of
something that is not one, so `readme_licence_role` returns `requirement` / `licence-claim` / `None`
rather than a family.

### `P457` — de-duplicate on the licence holder, not the README hash

| Fork | Canonical | Tell |
|---|---|---|
| `adity982/OpenTutor` | `zijinz456/OpenTutor` | README **byte-identical** (md5 `620be84c…`) |
| 🔴 `algenlab/adaptive-tutor` | `zijinz456/OpenTutor` | **renamed, README edited** (12562 B vs 11807 B, different md5) — the hash check **passes it through**. Caught by `LICENSE` reading **© Zijin Zhang** |
| `wiwaszko-intel/education-ai-suite` | `open-edge-platform/education-ai-suite` | identical README **and the fork's own README links home** |

🟢 **A fork almost never rewrites the `LICENSE` copyright line** — that is the one edit that looks
like theft. The holder is the durable invariant; the README hash is not. Extends **`P160`**
(`fork-lineage-audit`), which keyed on inherited GitHub metadata — unavailable here, since
`api.github.com` is 403.

### `P459` — a holder must be a party, not a clause (found by running it, not reading it)

🔴 **This one is a defect in *this folder's own* first draft**, found when the instrument was run
live against the twelve real repositories rather than against fixtures. The long-form licences
contain the word *copyright* inside their **own body** — Apache-2.0's definition of "Legal Entity",
AGPL-3.0's section 2 — so an unrestricted scrape returned:

| Repo | Licence | "Holder" before the fix |
|---|---|---|
| `openedx/XBlock` | Apache-2.0 | `owner or entity authorized by` |
| `open-edge-platform/education-ai-suite` | Apache-2.0 | `owner or entity authorized by` |
| `openedx/edx-platform` | AGPL-3.0 | `on the software, and (2) offer` |
| `openeducat/openeducat_erp` | LGPL-3.0 | `information, please see the COPYRIGHT file` |

🔴 **Two unrelated Apache-2.0 repositories therefore shared a "holder", and `same_project()` would
have merged them as a fork pair.** That is a false **positive**, which is worse than the miss
`P457` fixed: it deletes a real project as a duplicate. Fixed in two parts — only a notice in the
payload's **head region** (12 lines) counts, and the captured string must pass
`_looks_like_a_party()`, which rejects clause fragments and licence boilerplate.

🟢 **Correct behaviour now: the long-form licences return `None`, and that is right, not a miss** —
a bare Apache-2.0 or GPL grant text names no party. `MIT`/`BSD` notices still resolve
(`Zijin Zhang`, `Grupo Sirius`), so `P457` still works: `algenlab/adaptive-tutor` is still caught
live as **© Zijin Zhang**.

## What this folder does NOT establish

- ⚠️ **No star counts, no momentum.** Three channels measured, three 403. This instrument reads
  licences and documents only.
- ⚠️ **It does not establish `formalms`' effective licence** — only that the **repository publishes
  no grant**, which is sufficient to keep it out of a deliverable.
- 🔴 **It does not re-probe this KB's historical `ABSENT` verdicts.** `P453` and `P454` mean any
  `ABSENT` recorded before pass 32 may be a false negative, especially for `.rst`-documented and
  Python-packaging projects where both defects land together. **Pre-registered as the next action
  for pass 33:** re-run `probe_repo` over every `ABSENT` in the corpus and publish the diff.
- ⚠️ **`verdict()` reads the grant, not the obligations.** `LICENSED` means *a grant was read*, not
  *safe to use*: `AGPL-3.0` and `GPL` rows come back `LICENSED` and are still copyleft. Licence
  family is the input to the commercial question, not its answer — see `P37` (the two-reader
  licence gate) and `P22`/`P22.5`.
