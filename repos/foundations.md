---
industry: education
region: Global
updated: 2026-10-10
---

# Education — foundational repos

**Pass 94, 2026-10-10.** ⏱️ **Fourth pass of this date** (91: 23:0x–00:00 UTC; 92: 00:4x–01:3x; 93:
01:4x–02:24; this one 02:5x). 🔴 **Repository code still will not execute in this sandbox**, so no
classifier was written for the second pass running (`P237`); the oracle map was run by hand and payloads
printed rather than matched (`P970`). 🟢 **Pass 94 adds Tier 2d (scoring validation), `P972`–`P977`, and
resolves `Gap 370`'s failing path by hand.** Everything not marked 🆕 p94 is carried and was not re-read.

#### Pass 93 — carried below, unchanged

**Pass 93, 2026-10-10.** ⏱️ **Third pass of this date** (91 ran 23:0x–00:00 UTC, 92 ran 00:4x–01:3x,
this one later the same day).

🔴 **The instrument changed again, and this time because the pass could not run the shelf's own.**
`compose/code/grant-ladder-v4/ladder.sh` is committed and correct, but **this session's sandbox declines
to execute repository code**, so pass 93 could not call it. 🔴 **The tempting move — write a fresh
classifier — is exactly what `P237` forbids and exactly what cost pass 91 two platform licences.**
🟢 **So pass 93 wrote no classifier at all.** It ran v4's *oracle map* by hand and **printed the
payload's title block instead of matching on it**:

| step | oracle | pass 93 |
|---|---|---|
| existence · default ref · SHA | `git ls-remote --symref` | ✅ ran |
| licence payload | `raw.githubusercontent.com/<slug>/<SHA>/<name>`, HTTP 200 + ≥ 1 B | ✅ ran |
| licence **family** | `lib/license_family.sh` | 🔴 could not execute → 🟢 **title block printed and read, not classified** |

🆕 🔵 **`P970` — when the shared classifier cannot be run, the honest fallback is to decline to classify,
not to fork.** Every new row below carries the bytes, the filename, the ref and the SHA, so v4 can
re-derive it mechanically next pass and disagree with this pass on the record.

**Two-sided control.** 🟡 `moodle/moodle` → `COPYING.txt` **35 147 B** at `main` · `f205347` —
byte-identical to pass 92 **and at the same SHA**, so this is a re-read of the same object rather than an
independent eleventh measurement. **Stated as such instead of counted as a reproduction.** 🟢 Invented
slug `CAHLR/pyBKT-invented-control-p93` → `ABSENT` (git exit 128, auth prompt refused). 🟢 And a
*third-party* control that cost nothing: [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic)
returned **404 on `LICENSE`, `LICENSE.txt` and `LICENSE.md`** at `master` · `5d546f2` — independently
reproducing the no-grant negative `verticals/solutions.md` already carries, with a different instrument.

🔵 **Rows not marked 🆕 are carried at their pass-92 SHAs and were NOT re-read this pass.** `—` in ★ means
not read this pass.

A *foundation* here is a repo a studio can standardise on **across clients**, independent of which LMS any one
client runs. The useful property of this tier is that it sits on spec boundaries (SCORM, xAPI, cmi5, QTI,
Open Badges, LTI), and spec-boundary code is permissive far more often than product code.

## Tier 1 — content and learner-data interoperability

This is the tier to own. Every education engagement eventually has to move content *into* a platform the client
already runs and get learner data *out* of it.

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** · 1 072 B · `master` · `882f3b8` | 354 | 🔵 unplaced | The runtime shim. SCORM 1.2 / 2004 API surface for any content in any LMS. |
| [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) | **Apache-2.0** · 11 324 B · `master` · `ea17c40` | 42 | **North America** (US DoD / ADL) | The authoritative SCORM → xAPI statement mapping. The audit-trail spec. |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | **Apache-2.0** · 11 357 B · `master` · `efa045e` | — | **North America** (US DoD / ADL) | Reference Learning Record Store — the canonical implementation to test against. |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** · 11 357 B · `main` · `cb794e4` | — | **North America** (Yet Analytics, US) | **A production SQL LRS.** Apache-2.0 and backed by a real database — this is the one to deploy, where `ADL_LRS` is the one to conform to. |
| [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) | **MIT** · 1 077 B · `master` · `b5ac7dd` | — | 🟡 **EMEA** (Tunapanda, Kenya lineage) | 🟢 **The MIT escape hatch from H5P's GPL core.** Plays H5P content with no LMS and no GPL server-side library. |
| [`celtic-project/LTI-PHP`](https://github.com/celtic-project/LTI-PHP) | 🟡 **LGPL-3.0** · 7 651 B · `master` · `1f47c93` | — | **EMEA** (UK) | LTI 1.3 tool provider. 🟡 LGPL — link, do not fork into a closed binary. |
| [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | **Apache-2.0** · 13 185 B · `develop` · `0a66b52` | — | **North America** (1EdTech) | Open Badges validation. The credentialing tier's conformance gate. |
| 🆕 [`edly-io/pxc`](https://github.com/edly-io/pxc) | **Apache-2.0** · 11 358 B · `main` · `01114d3` | 9 | 🔵 unplaced (publisher is the Open edX commercial vendor **edly.io**) | 🟢 **Watch this one.** A **proposed standard for learning activities explicitly intended to replace SCORM, H5P *and* LTI** — the three specs this entire tier is built on — published permissively by the vendor that packages Open edX. 🔵 **Nine stars and strategically larger than anything else on this page.** Not a dependency yet; a reason to keep the interop layer behind an interface you own. |

## 🆕 Tier 1b — a national curriculum as verified open data, and the counter-example to `Gap 367`

🔴 **The shelf has said for two passes that the reference frameworks of the curriculum mandates cannot be
shipped:** `touretzkyds/ai4k12` (AAAI/CSTA) carries **no licence payload in 24 filenames**, and
`learning-commons-org/knowledge-graph`'s `LICENSE.md` grants nothing at all (`P965`). 🟢 **For Brazil that
is now false, and the counter-example is better engineered than anything else in this category.**

**`bncc.dev`, run by Profy, publishes Brazil's *Base Nacional Comum Curricular* as verified open data** —
and the licences were read from the payload at pinned SHAs:

| repo | grant (payload · bytes · ref · SHA) | ★ | what it is |
|---|---|---|---|
| 🆕 [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟡 **`LICENSE` = MIT** · 1 073 B · `main` · `daabd7d` — **but the data is CC BY 4.0, and that grant is NOT at the root** (see `P969` below) | 20 | **1 721 learning objectives** (1 580 from the three stages of basic education + 141 from the Computing supplement) in **JSON, SQLite and CSV**, with **per-record provenance** (`fonte` → spreadsheet row + PDF page) and a reproducible extraction pipeline that CI re-runs and rejects on divergence. 🟢 **1 576 of 1 580 BNCC-2018 texts match the official MEC/CNE PDF character for character; the 4 mismatches are documented in `DECISOES.md`. 141 of 141 for Computing.** 🔵 **That is a provenance claim with a denominator — rare anywhere on this shelf.** |
| 🆕 [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 **split grant, declared at the root** · `LICENSE` 1 299 B (index) · `main` · `ac9feb8` → **MIT** for `packages/*/src/`, `python/bncc/*.py`, `mcp-worker/src/`, `scripts/`, tests and config; **CC BY 4.0** for the data | 9 | npm `@bncc/dados` 0.3.1, npm `@bncc/mcp` 0.2.0, PyPI `bncc` 0.2.0, plus a hosted MCP worker. 🟢 **The MCP server exposes 7 tools** (`bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`) **with the dataset embedded, so queries run locally.** 🟡 All three packages are pre-1.0. |
| 🆕 [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟢 **split grant, declared at the root** · `LICENSE` 911 B (index) · `main` · `4713901` → **MIT** for `harness/` and `test/`; **CC BY 4.0** for `itens/`, `resultados/`, `METODOLOGIA.md` | 9 | An **open hallucination benchmark over the BNCC**. See `intel/trends.md` `T11` — it carries the most useful number this pass produced. 🟢 **Its README declares a conflict of interest in its own words**: *"Vale declarar o conflito de interesse: a Profy opera produtos que usam LLMs sobre a BNCC."* |
| 🆕 [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) | **MIT** · `LICENSE` 1 218 B · `main` · `f94ca6a` | — | An **independent** MCP server over the BNCC skills, from a different author. 🔵 **n=2 for MCP × national curriculum**, which is the same "new shape, not n=1" test the shelf applied to MCP × SCORM in pass 92. |

🔵 **Region, and the evidence class.** **LATAM (Brazil)** — and not by inference from the subject matter:
the `bncc-pacotes` and `bncc-benchmark` licence payloads are **written in Portuguese**, and the data's
attribution clause names **MEC/CNE**, Brazil's education ministry and national council. The payload itself
carries the region.

### 🔴 🆕 `P969` — the grant ladder reads repo-root filenames only, so a per-directory data licence is invisible to it

🔴 **`bncc-dados` is the row that proves it, and the cost is an attribution obligation, not a nuance.**

| oracle | what it reports for `bncc-dev/bncc-dados` |
|---|---|
| the 24-filename ladder at the repo root | 🔴 **MIT** (`LICENSE`, 1 073 B) |
| GitHub's own licence sidebar | 🔴 **"MIT license"**, nothing else |
| the repo's README and `dados/LICENSE.md` | 🟢 **data under `dados/` is CC BY 4.0**; MIT covers `pipeline/` |

🔴 **A repository whose entire purpose is the dataset presents MIT at the root, and both automated oracles
agree on the wrong answer for the artefact a studio would actually ship.** `LICENSE-DADOS.md` at the root
is a **404** — the grant is one directory down, where 24 root filenames cannot reach.
🔵 **Two independent oracles, one blind spot, one cause: root-only detection.** That is the strongest form
this finding can take, because it cannot be dismissed as a defect in this KB's instrument.

🟢 **And the same publisher shows the fix in its own other two repos**: `bncc-pacotes` and `bncc-benchmark`
put a **split-grant index at the root** that names each licence and scopes it to explicit paths. The ladder
reads those correctly. **Convention, not tooling, is what makes a split grant legible.**

🟢 **`P965`'s measured threshold survives a payload it was not built on.** Pass 92 set it at *a real grant
names 0–2 families; a framework document names 3, from three lineages*. These index files name **2** (MIT +
CC BY 4.0), from two lineages, and they **are** real grants — each points at the full text
(`LICENSE-CODIGO.md` 1 286 B, `LICENSE-DADOS.md` 577 B, both HTTP 200, both verified present this pass).
🔵 **Same document *shape* as `learning-commons-org/knowledge-graph`, opposite usability — and the
threshold separates them correctly.**

🔴 **The fix this pass does not pretend to have made.** `compose/code/p199-perfile-license/` already does
per-path licence probing — it exists, and it was run on `INGInious`. **It is not wired into the ladder**,
and this pass could not execute either. **Recorded as `Gap 370`**, with the payload that proves it needed,
so the next pass that can run code has a failing case ready.

## Tier 2 — assessment and automated feedback

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| [`numbas/Numbas`](https://github.com/numbas/Numbas) | **Apache-2.0** · 11 357 B · `master` · `39b03e5` | 215 | **EMEA** (Newcastle University, UK) | Browser-native e-assessment with real mathematics; SCORM-packageable. The strongest permissive assessment engine on this shelf. |
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | **BSD** · `LICENSE.md` 1 542 B · `main` · `80d7d66` | — | **North America** (RPI, US) | Full course-management + autograding platform, **BSD**. Permissive and production — rare in this tier. |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | **BSD** · 1 560 B · `master` · `190c1a4` | — | **North America** (UC Berkeley, US) | Notebook autograding; the standard in data-science teaching. |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | **BSD** · 1 512 B · `main` · `f9915da` | — | **North America** (Project Jupyter) | Assignment release/collect/grade for notebooks. |
| [`webtech-network/autograder`](https://github.com/webtech-network/autograder) | **Apache-2.0** · 11 357 B · `main` · `04bee3e` | — | 🔵 unplaced | Rubric-driven autograding with report generation; release 0.4.0 (May 2026). |

## 🆕 p94 Tier 2d — the scoring-**validation** layer, and why it is the half worth having

🟢 **Three rows, all read from the payload this pass, and one of them changes what `Gap 372` says.**

| repo | grant (payload · bytes · file · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| 🆕 p94 [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) | 🟢 **Apache-2.0** · **11 358 B** · `LICENSE` · `main` · `a844f71` | 71 | 🟢 **North America** (ETS) | **2 916 commits.** Builds **and evaluates** automated scoring models from a configuration file; customisable HTML statistical report; scikit-learn + SHAP; `fairness` among its own topics. 🔴 **Not a scoring engine** — it is how you demonstrate one is valid. |
| 🆕 p94 [`EducationalTestingService/skll`](https://github.com/EducationalTestingService/skll) | 🟢 **BSD-3-Clause** · 1 555 B · `LICENSE.txt` · `main` · `b350eb0` | — | 🟢 **North America** — `P800`: *"Copyright (c) 2012–2022 Educational Testing Service"* | scikit-learn experiments driven by configuration. Pinned by `rsmtool` at `skll==5.0.1`, so the pair is a single dependency decision. |
| 🆕 p94 [`HASKI-RAK/NodeGrade`](https://github.com/HASKI-RAK/NodeGrade) | 🟢 **MIT** · 1 062 B · `LICENSE` · `main` · `8e144ac` | 3 | 🟡 **EMEA** (Germany, by the ECSEE '25 citation; the payload holder reads only *"HASKI"* — weaker than `P800`) | **421 commits.** Short-answer grading as a node graph with **LTI 1.1/1.3**; NestJS + Prisma + Postgres, React/Vite PWA, Python sentence-embedding worker, **local-model provider included**. |

🔵 **Why this tier is not a duplicate of Tier 2.** Tier 2 grades **structured** work — maths, notebooks,
code — and does it well and permissively. This tier is about **open-response** work and about the artefact
that regulated assessment actually owes: **a validity and fairness argument, in a report, with the model's
behaviour attributable.** 🟢 **That artefact is Apache/BSD.** 🔴 **The scorer is not** — see the flags
below.

🔴 **Flags that belong with this tier, all payload-read this pass:**

| repo | payload | why it is flagged |
|---|---|---|
| 🆕 p94 [`openedx/ease`](https://github.com/openedx/ease) | 🔴 **AGPL-3.0** · 35 136 B · `LICENSE.txt` · `master` · `056da0a` | edX's *Enhanced AI Scoring Engine*. The obvious candidate for an AES build, and network copyleft. |
| 🆕 p94 [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 **AGPL-3.0** · 35 135 B · `LICENSE` · `master` · `1b7ae59` | Open Response Assessment inside Open edX — peer, self and staff assessment. Same grant. |
| 🆕 p94 [`EducationalTestingService/factor_analyzer`](https://github.com/EducationalTestingService/factor_analyzer) | 🔴 **GPL-2.0** · 18 092 B · `LICENSE` · `main` · `de933d2` | 🔴 **From the same publisher as the two permissive rows above.** Dependency-shaped (EFA/CFA) — the kind of library a scoring pipeline imports without reading. `P975`. |

### 🔴 🆕 `P975` — licence is a property of the repository, never of the publisher

**Educational Testing Service ships Apache-2.0, BSD-3-Clause and GPL-2.0 from one GitHub organisation**,
measured in a single sitting above. 🔵 **A licensing-sophisticated publisher is the case where the
inference feels safest, which is what makes it the right counter-example.** 🟢 Negative control recorded
with it: `EducationalTestingService/rsmexplain`, named by a search summary, **does not resolve**
(`git ls-remote` exit 128).

### 🟢 🆕 `P974` — probe for clauses, not for bytes

Pass 93's `P971` (a `LICENSE` that is Apache's **header notice**, not its **licence**) was caught by size.
🔴 **Size alone also condemns honest abridged copies** — `SimonsTang/feifei-companion` is 10 227 B and
real. 🟢 **Four clause headings settle it**: *Grant of Patent License* · *Grant of Copyright License* ·
*Redistribution* · *APPENDIX*. `rsmtool` → **4 of 4**; `AI_AWE` → **0 of 4**. 🔵 **And the discriminating
clause is the one that justifies choosing Apache at all:** §3, the express patent grant.

### 🟢 🆕 `P972` / `P973` — platform versions are payload-readable, and `version.php` is not at the root

Full statement and evidence in **`compose/code/p972-platform-version-ladder/`**; the consequences for the
platform tier are in `verticals/solutions.md`. In one line each:

- 🟢 **`P972`** — `git ls-remote --heads|--tags <slug>` returns the release ladder and
  `raw.githubusercontent.com/<slug>/<SHA>/<version file>` returns the release string. **Moodle: `main` is
  `6.0dev (Build: 20261005)`, `MATURITY_ALPHA`; `MOODLE_503_STABLE` is `5.3`, `MATURITY_STABLE`.** 🔴 Every
  secondary source read this pass said 5.2.
- 🔴 **`P973`** — `moodle/moodle`'s root `version.php` is **404**; the file is `public/version.php`, because
  the web root moved into `public/` at 5.0. **`P969` is a path defect, not a licence defect**, and this KB
  has probed 24 licence filenames at the root for ninety passes.
- 🟡 **`P977`** — the ladder oracle's own limit: `openedx/edx-platform`'s `open-release/*` **heads stop at
  Sumac** while `release/teak.*` and `release/ulmo.*` exist only as **tags** under a **changed prefix**.
  Cross-check the deployment distribution (`overhangio/tutor` → `v22.0.2`).

## 🆕 Tier 2b — the learner model — **`Gap 335` discharged after eight passes untouched**

🔴 **`Gap 335` (knowledge tracing) was the oldest untouched item on this shelf**, named openly in
`agents/top.md` for eight passes: *"only `adaptive-knowledge-graph` (Bayesian) and `Bloom` (2-sigma)
carry an explicit learner model. Everything else relies on the context window, which is not a mastery
estimate."* 🟢 **The canonical library exists, it is MIT, and it was found on the first query that
named the technique instead of the industry** — `P955` holding for a second pass running.

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| 🆕 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` | ~430 | 🔵 unplaced | 🟢 **The reference deep-knowledge-tracing benchmark library** (NeurIPS 2022 datasets-and-benchmarks track, `pykt.org`). Standardised preprocessing plus a model zoo — **DKT, DKVMN, SAKT, SAINT, AKT, GKT, LPKT** — over 7 datasets. 🔵 **This is the missing layer, not another tutor:** it turns "the agent remembers the conversation" into **a per-skill mastery estimate you can threshold on**, which is what adaptive sequencing and mastery-gated progression actually need. MIT, so it can sit inside a paid deliverable. |
| 🆕 [`JonathanSilver/pyKT`](https://github.com/JonathanSilver/pyKT) | **MIT** · 1 065 B · `main` · `2bef7e9` | — | 🔵 unplaced | 🔴 **Name collision, and the weaker of the two.** A separate PyTorch reference implementation whose own README warns *"not all the implemented models have achieved comparable performance to that of the original implementations"*. 🔵 **Read it as a reference, never as the benchmark** — and note it is reachable by the same search string as the row above. |

🔴 **And the third candidate carries no grant:**
[`weiwei1392/knowledge-tracing`](https://github.com/weiwei1392/knowledge-tracing) → **no licence
payload in 24 filenames** · `main` · `136efef`.

🆕 🔵 **`P968` — two repos sharing a project name is a licence-and-quality trap, not a trivia item.**
`pykt-team/pykt-toolkit` and `JonathanSilver/pyKT` are both MIT, so a licence probe cannot separate
them; only reading the README does. This is the same shape as `Gap 368`'s acronym collision on
`topics/lms` (**LMS = Least Mean Squares**, **LMS = Library Management System**) — 🔵 **in this
industry, name collision is a recurring property of the search space, so the canonical slug belongs
in the shelf row and not just the project name.**

## 🆕 Tier 2c — the **psychometric** layer, and why it outranks the deep-learning one for a deliverable

🟢 **Pass 92 discharged `Gap 335` with one library** — `pykt-team/pykt-toolkit`, deep knowledge tracing —
and wrote that the learner model had arrived. 🔴 **That was half the answer.** Naming three more
techniques (`P955` for a third pass running) returns a **complete, composable, permissive stack**, and the
important finding is the ordering inside it:

🔵 **The classical psychometrics layer is more production-ready than the deep-learning layer, and more
defensible.** `catsim` has 877 commits and a BSD grant; `pykt-toolkit` is a research benchmark. More to the
point, **IRT and BKT produce a parameter you can show a regulator** — an item difficulty, a per-skill
mastery probability — whereas a DKT network produces an activation. Under the EU AI Act's Annex III,
assessing learning outcomes is high-risk and owes an explanation (`intel/trends.md` `T9`). **A 2-parameter
logistic item curve is an explanation. A trained LSTM is not.**

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| 🆕 [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | **MIT** · `LICENSE` 1 132 B · `master` · `cc1682e` | 282 | 🟢 **North America** (UC Berkeley — the payload's copyright line reads *"Computational Approaches to Human Learning (CAHL) Research, zp@berkeley.edu"*, `P800`) | **Bayesian Knowledge Tracing** and its variants, scikit-learn-shaped (`Model.fit`/`predict`), EM-fitted. 🟢 **The cheapest real mastery estimate on this shelf**: four interpretable parameters per skill (prior, learn, slip, guess), each of which a teacher can be shown. |
| 🆕 [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | **MIT** · `LICENSE` 1 121 B · `master` · `6514928` | 173 | 🟢 **North America** (Notre Dame — payload copyright line *"John Lalor <john.lalor@nd.edu> and Pedro Rodriguez"*, `P800`) | **Bayesian Item Response Theory** on Pyro/PyTorch, GPU-scalable. Calibrates *item* difficulty and discrimination and *learner* ability on the same scale. 🔵 **This is the calibration step; it does not select items.** |
| 🆕 [`eribean/girth`](https://github.com/eribean/girth) | **MIT** · `LICENSE.txt` 1 064 B · `master` · `daf2277` | 126 | 🔵 unplaced (payload copyright line is a pseudonym — *"eribean"* — no geography to take, so none is asserted) | The second IRT estimator, and the one **`catsim`'s own README points at**. 🟡 Note the filename: `LICENSE` is a **404** here and the grant lives in `LICENSE.txt` — the ladder's 24-name reach is what makes this row readable at all. |
| 🆕 p95 [`eribean/girth_mcmc`](https://github.com/eribean/girth_mcmc) | **MIT** · `LICENSE.txt` 1 061 B · `main` · version **0.6.0** | — | 🔵 unplaced (same pseudonymous holder as `girth`; no geography to take, so none is asserted) | **Bayesian / MCMC item-response-theory estimation** — the sampling companion to `girth`, and the third of the three estimators `catsim`'s README points Python users at. 🟢 **Triple-confirmed grant**: the `LICENSE.txt` payload is canonical MIT, `setup.py` declares `license="MIT"`, and the classifier says `License :: OSI Approved :: MIT License`. 🟡 **Same filename trap as `girth`**: `LICENSE` is a **404**, the grant is in `LICENSE.txt`. |
| 🆕 [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** · `LICENSE` 1 514 B · `dev` · `7e6caae` | 153 | 🟡 **LATAM** (Brazil) — ⚠️ **evidence class is weaker than `P800`**: the payload's copyright line is a personal name only, and the Brazil placement comes from the project's own documentation host, `douglasrizzo.com.br`, linked throughout the README. Labelled, not upgraded. | **Computerized Adaptive Testing engine** — item selection, ability estimation, stopping rules, plus a simulator. 🟢 **The only CAT engine on this shelf, and the only psychometrics row with a LATAM claim.** 🟡 Default branch is `dev`, not `main` — pin it. |
| 🆕 [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | **MIT** · `LICENSE` 1 079 B · `main` · `9446cb0` | 506 | 🔵 unplaced (payload copyright line is the org, *"Open Spaced Repetition"*) | **FSRS scheduling** — when to show an item again, as a library. 🔵 **The complement to mastery, not a duplicate of it:** BKT/IRT say *whether* a learner knows a skill; FSRS says *when they will forget it*. Highest star count in this tier. |
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` | ~430 | 🔵 unplaced | 🟢 Deep knowledge tracing: DKT, DKVMN, SAKT, SAINT, AKT, GKT, LPKT over 7 datasets (NeurIPS 2022). **Carried from pass 92 at its pass-92 SHA; not re-read this pass.** 🔵 Read it as the research ceiling, and `pyBKT` as the deliverable floor. |

### 🟢 The seam is named by the tools themselves, not inferred by this KB

🔵 **This is why the tier composes instead of overlapping, and the evidence is in `catsim`'s README
verbatim:** *"**catsim does not implement item parameter estimation.** I have had great joy outsourcing
that functionality to the [mirt] R package."* It then points Python users at exactly
[`eribean/girth`](https://github.com/eribean/girth), [`eribean/girth_mcmc`](https://github.com/eribean/girth_mcmc)
and [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt).

🟢 **So the wiring is documented by the dependency, not designed by us:** `py-irt` (or `girth`) calibrates
the item bank → `catsim` runs the adaptive session against it → `pyBKT` tracks per-skill mastery across
sessions → `py-fsrs` schedules the review. **Four permissive libraries, one seam each, no overlap.**
Costed as `P93-A` in `compose/patterns.md`.

🟢 **🆕 p95: the subtraction pass 93 and 94 both carried is now paid.** Those passes recorded that
`girth_mcmc` was *named by `catsim` but not resolved* — a lead, not a row. **Pass 95 resolved it: MIT,
`0.6.0`, at `LICENSE.txt`.** It is in the table above, and **all three estimators `catsim` names are now
permissive rows on this shelf** (`girth`, `girth_mcmc`, `py-irt`). 🔵 **The seam is therefore not just
documented by the dependency — it is fully supplied.**

## 🆕 p95 Tier 2e — the **autograding** layer, and the AGPL monopoly that just ended

🔴 **Until this pass, every automated-feedback row on this shelf with real classroom use was copyleft.**
`mumuki/mumuki-laboratory` (AGPL-3.0, Argentina) was the strongest, and `openedx/ease` and
`openedx/edx-ora2` are both AGPL-3.0. 🟢 **There is now a BSD-3 row at that layer.**

| repo | grant (payload · bytes · file · ref · SHA) | version | ★ | region | role in a build |
|---|---|---|---|---|---|
| 🆕 [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** · 1 560 B · `LICENSE` · `master` · `190c1a4` | **7.0.0** | — | 🟢 **North America** (UC Berkeley Data Science Education Program) | 🟢 **Production autograder for Python scripts and Jupyter notebooks at course scale.** Parallel Docker grading, an Otter-managed grading VM, a student-side client for public checks, **native Canvas and Gradescope support**. Zenodo DOI, live CI and coverage. |

🟢 **Three-layer licence agreement** — `LICENSE` payload, `pyproject.toml` (`license = "BSD-3-Clause"`) and
the PyPI classifier all concur. 🟢 **And it is the one row on this shelf where the default branch and the
tag ladder agree** (`7.0.0` = `v7.0.0`), which under `P978` makes its published version also its shippable
one.

🔴 **What this tier is NOT.** Otter grades **code against tests**. It is not an open-response scorer, so
**`Gap 372` is untouched by it** — see `agents/top.md` for that gap's three new measured negatives. 🔵 **The
honest framing: this closes the *programming-assessment* hole, which nobody had named, and leaves the
*constructed-response* hole, which five passes have.**

### 🔴 🆕 `P980` — resolve a tool to its repository, never to its distribution name

Finding this row surfaced a collision worth carrying into every future probe:

| what you cite | PyPI | repository | grant |
|---|---|---|---|
| `otter-grader` | `otter-grader` **7.0.0** | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** · 1 560 B · `190c1a4` |
| `Otter-Autograder` | `Otter-Autograder` **0.15.9** | [`OtterDen-Lab/Autograder`](https://github.com/OtterDen-Lab/Autograder) | 🔴 **GPL-3.0** · 35 149 B · `2d9555f` |

🔴 **Two unrelated projects, both autograders, incompatible grants, seven majors apart.** A search summary
reporting *"Otter-Autograder is GPL-3.0-or-later"* was reading the **other** project. 🟢 **Only the
`project_urls` → repository link disambiguates them.** 🟡 **And do not read `info.license` from PyPI for an
identifier:** `Otter-Autograder` pastes the **entire 35 kB GPL-3.0 text** into that field with
`license_expression` set to `None`. **The `classifiers` array was correct for both.**

## Tier 3 — delivery, runtime and agent substrate

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** · 1 097 B · `develop` · `d4fea9c` | — | **North America** (Learning Equality, US) | **Offline-first learning delivery.** MIT. The correct substrate wherever connectivity is the binding constraint — which, per UNESCO, is most of APAC's and LATAM's deployment reality, not an edge case. |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** · 11 358 B · `develop` · `ad22e91` | — | **North America** (Oppia Foundation) | Structured, explanation-driven interactive lessons; a real pedagogy model in code. |
| [`oppia/oppia-android`](https://github.com/oppia/oppia-android) | **Apache-2.0** · 11 357 B · `develop` · `25e3860` | — | **North America** | The offline Android client for the above. |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | **BSD** · 1 475 B · `main` · `f02ec3c` | — | 🔵 unplaced | Multi-tenant notebook serving — the per-learner compute boundary. |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** · 1 072 B · `main` · `12aeb0f` | — | **North America** | Stateful agent orchestration. The graph, not the agent. |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | **Apache-2.0** · 11 357 B · `main` · `96f33fa` | — | **EMEA** (Hugging Face, FR lineage) | Minimal agent loop; the low-ceremony option when LangGraph is too much machinery. |
| [`huggingface/agents-course`](https://github.com/huggingface/agents-course) | **Apache-2.0** · 11 357 B · `main` · `3c469e7` | — | **EMEA** | 🟢 The permissive **teaching** counterpart to `smolagents` — see the AI-literacy tier in `agents/top.md`. |

## Licence flags in this tier — the traps

| repo | grant | why it matters |
|---|---|---|
| [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** · `LICENSE.txt` 35 146 B · `master` · `cb64a1f` | 🔴 **H5P's core is GPL.** The interactive-content ecosystem everyone reaches for is copyleft at the library level. Use `tunapanda/h5p-standalone` (MIT) for playback instead of linking this. |
| [`lumieducation/H5P-Nodejs-library`](https://github.com/lumieducation/H5P-Nodejs-library) | 🔴 **GPL-3.0** · 35 146 B · `master` · `ac2d6aa` | 🔴 The Node port is GPL too. There is no permissive H5P *authoring* server. |
| [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | 🔴 **GPL-3.0** · 35 141 B · `master` · `5fec948` | 🔴 The best-known LRS is GPL. `yetanalytics/lrsql` (Apache-2.0) is the permissive substitute, and it is the better-maintained one. |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | 🔴 **AGPL-3.0** · 36 983 B · `master` · `d1e44b4` | 🔴 Excellent adaptive-assessment engine (UIUC), AGPL — network copyleft, so hosting it for a client triggers reciprocity. |
| [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** · 34 764 B · `main` · `8f90cc8` | 🔴 UCLouvain autograder, AGPL. |
| [`GatorEducator/gatorgrader`](https://github.com/GatorEducator/gatorgrader) | 🔴 **GPL-3.0** · `LICENSE.md` 35 191 B · `master` · `3be3278` | 🔴 |
| [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) | 🔴 **GPL-3.0** · 35 147 B · `main` · `61b5d8f` | 🔴 The LMS-integrated accessibility checker. GPL, and not AI-driven. 🆕 **But it is no longer the only option** — three permissive AI WCAG checkers are now shelved in `agents/top.md`. |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 **GPL-2.0** · 18 025 B · `develop` · `d9d462a` | 🔴 **CORRECTED this pass — it was published here as "LGPL-3.0 · linkable" and it is not.** TAO (Open Assessment Technologies, Luxembourg) is the serious QTI assessment platform and **the most mature one in this inventory**, so this is the row most likely to be costed. **GPL-2.0 is full copyleft: a fork shipped to a client carries reciprocity, and there is no LGPL linking exception to rely on.** Integrate across a process or network boundary, or budget for the obligation. 🔵 Also **GPL-2.0-only** — one-way incompatible with GPL-3.0 code. |

## 🆕 ADL leaves its own specs ungranted — now measured at three of five

🔴 **The US DoD's Advanced Distributed Learning initiative *authored* SCORM. Three of its repos carry no
licence payload in 24 filenames, while two carry Apache-2.0.** This was one row in pass 89's `Gap 354`; it is
now a pattern inside a single publisher:

| ADL repo | grant | ★ |
|---|---|---|
| [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) | 🟢 **Apache-2.0** · 11 324 B | 42 |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | 🟢 **Apache-2.0** · 11 357 B | — |
| [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | 🔴 **no payload / 24** · `master` · `3e532b8` | 99 |
| 🆕 [`adlnet/SCORM-2004-4ed-Test-Suite`](https://github.com/adlnet/SCORM-2004-4ed-Test-Suite) | 🔴 **no payload / 24** · `master` · `050f1b4` | 18 |
| 🆕 [`adlnet/SCORM-to-TLA-Roadmap`](https://github.com/adlnet/SCORM-to-TLA-Roadmap) | 🔴 **no payload / 24** · `master` · `da1b9a2` | 7 |

🔵 **Why this is worth a table.** Pass 89 read the single `SCORM-to-xAPI-Wrapper` negative as *"one missing
file, not a policy"*, on the reasoning that its Apache-2.0 sibling proved intent. 🔴 **Three of five says the
opposite: inside this publisher, grants are applied to the *profile and the server* and omitted from the
*wrapper, the conformance test suite and the roadmap*.** The omission tracks a category — reference
implementations and documents — not an oversight. 🔴 **Practical effect: the official SCORM 2004 conformance
test suite cannot be redistributed in a client deliverable.** Conformance must be demonstrated against
`ADL_LRS` (Apache-2.0) instead, which is what `P91-B` does.

## Other no-grant rows in this tier

| repo | status |
|---|---|
| [`1EdTech/openbadges-specification`](https://github.com/1EdTech/openbadges-specification) | 🔴 **No payload / 24** · `develop` · `04c4bc2`. The *specification* carries no grant while the *validator* is Apache-2.0. Cite the validator. |
| [`eecs-autograder/autograder.io`](https://github.com/eecs-autograder/autograder.io) | 🔴 **No payload / 24** · `master` · `5af4960`. 🔵 Consistent with its own README — a docs/issue tracker, not the code. Not a defect, but not a dependency either. |

## Slugs that do not exist

🔴 Re-confirmed `ABSENT` this pass. Recorded so they are not re-tried:

- `apereo/opencast` → 🟢 the real slug is [`opencast/opencast`](https://github.com/opencast/opencast)
- `tutor-dev/tutor` → 🟢 the real slug is [`overhangio/tutor`](https://github.com/overhangio/tutor)
- `h5p/h5p-standalone` → 🟢 the real slug is [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone)

## Count, stated plainly

🆕 **p95: 36 foundational rows above the flag line, 2 of them added this pass** (`girth_mcmc`,
`otter-grader`). 🟢 **35 are permissive for the CODE** (MIT / Apache-2.0 / BSD); **1 is LGPL**
(`celtic-project/LTI-PHP`). 🔵 **And the same qualifier the p94 count needed: this is a 2-row measurement on
top of a 34-row inheritance, not a 36-row measurement.** Both new rows were read from the payload at the
SHAs named; the other 34 are carried and were **not** re-read. 🔴 **See `Gap 376` — three consecutive
passes of ~12 hand-read rows against a 133-row census is a decaying denominator, and it is now the most
important thing on this page to fix.**

🔵 **Pass 94's own sentence, kept because it still governs the reading:**

**34 foundational rows above the flag line, 3 of them added this pass** (`rsmtool`, `skll`,
`NodeGrade`). 🟢 **33 are permissive for the CODE** (MIT / Apache-2.0 / BSD); **1 is LGPL**
(`celtic-project/LTI-PHP`). 🔵 **Pass 93's own sentence, kept because it still governs the reading:**

**31 foundational rows above the flag line, 9 of them added this pass.** 🟢 **30 are permissive for the
CODE** (MIT / Apache-2.0 / BSD); **1 is LGPL** (`celtic-project/LTI-PHP`).

🟡 **And one qualifier the previous counts did not need.** **3 of the 31 carry a CC BY 4.0 obligation on
their DATA** — the three `bncc-dev` rows. CC BY 4.0 is an **attribution duty, not a copyleft one**, so it
does not move those rows below the flag line; but **counting them as plainly "permissive" without naming
the data grant is precisely the elision `P969` exists to punish.** Named here instead.

🔵 **What the headline number does and does not mean.** 9 rows were resolved from the payload this pass;
**the other 22 are carried at their pass-92 SHAs and were not re-read.** So this is not a 31-row
measurement — it is a 9-row measurement on top of a 22-row inheritance, and the next pass that can run
`grant-ladder-v4/ladder.sh` should re-derive all 31 and disagree with this page on the record if it finds
cause.

🟢 **The standing finding survives a fifth measurement, and widens:** the interoperability, assessment,
learner-model and now **psychometric** tiers are the permissive heart of this industry. 🔵 **Pass 93's
addition to that claim is a ranking, not just a row count:** within the learner-model tier, the
*permissive* and the *explainable* options turn out to be the same ones — BKT, IRT and CAT are all
MIT/BSD **and** all produce a parameter you can defend in an Annex III audit, while the copyleft and the
black-box options sit together at the other end.

🔴 **One honest subtraction from pass 91's count, carried forward.** Pass 91 reported *"19 of 20
permissive, 1 LGPL"*. That line was true of the page as it stood **only because `oat-sa/tao-core` was
misfiled as LGPL-3.0**; it sits below the flag line either way, so that headline was unchanged by the
correction — but the LGPL row it referred to is `celtic-project/LTI-PHP`, and **`tao-core` was never one
of the 20.** Stated rather than silently re-tallied.

## Open gaps on this page

- 🔴 🆕 **`Gap 370` — the ladder cannot see a per-directory licence.** `compose/code/p199-perfile-license/`
  already does per-path probing and is not wired into `grant-ladder-v4`. Failing case ready:
  `bncc-dev/bncc-dados` → root `LICENSE` MIT, data `dados/LICENSE.md` CC BY 4.0, root `LICENSE-DADOS.md`
  404. See `P969`.
- 🟡 🆕 **p94: `Gap 372` narrowed to the scorer.** The validation half exists and is permissive (Tier 2d);
  the production scoring code is AGPL-3.0 (`openedx/ease`, `openedx/edx-ora2`). **What is missing is a
  permissive production-grade scorer for open-response work** — and nothing else.
- 🔴 🆕 **p94: `Gap 375` — this shelf has 3 payload-derived platform versions and the rest are prose.**
  Moodle (`5.3` stable / `6.0dev`), Artemis (`10.3`) and Open edX (`release/ulmo.4`, Tutor `v22.0.2`) were
  read this pass; every other version string in the platform tier still comes from a README or a blog.
  `P972` makes the fix mechanical, so this gap is work, not uncertainty.
- 🟢 🆕 **p95: `eribean/girth_mcmc` RESOLVED, after two passes as a named-and-unrun lead.** **MIT**,
  `0.6.0`, `LICENSE.txt` 1 061 B — triple-confirmed against `setup.py` and its OSI classifier. In **Tier
  2c**. 🟢 **All three estimators `catsim`'s README names are now permissive rows.**
- 🟢 🆕 **p95: `Gap 375` substantially discharged — 12 payload-derived platform versions, up from 3.**
  Nine were read this pass (`ILIAS` **`11.5 2026-10-06`**, Chamilo **`3.0.1`**, `frappe/lms` **`2.45.2`**,
  Gibbon **`31.0.00`**, OpenEduCat **`19.0.1.0`**, Mumuki **`9.23.0`**, `relate` **`2024.1`**,
  `classroomio` **`0.1.13`**, `otter-grader` **`7.0.0`**) plus four release ladders. 🟡 **What remains open
  is the permissive tier's smaller rows** (`pupilfirst`, `academico`, `open-tutor-ai-CE`), which were not
  probed.
- 🟢 🆕 **p95: `P978` — the default branch reports the DEVELOPMENT version.** Measured on four platforms:
  Sakai's root pom says `27-SNAPSHOT` against a newest tag of `25.2`; Opencast `21-SNAPSHOT` against
  `20.4`; OpenOLAT `21.2-SNAPSHOT` against `OpenOLAT_21.0.3`; Moodle `6.0dev` against `5.3` stable.
  🔴 **Publishing a default-branch version means publishing a release nobody can install.** Read both.
- 🔴 🆕 **p95: `Gap 377` — `pom.xml` / `build.gradle` are not in the grant ladder's path list.** Sakai's
  `pom.xml` names *"Educational Community License, Version 2.0"* and so independently confirms an ECL-2.0
  row that generic tooling returns as *unclassified* (`P979`). **A second concurring oracle for the licence
  family this tier most often loses. Cheap to add, and it pays on every JVM platform here.**
- 🔴 🆕 **p95: `Gap 378` — a probe that reads paths cannot follow an indirection.**
  `chamilo/chamilo-lms`'s `public/main/install/version.php` is HTTP 200 and its entire body is
  `return require dirname(__DIR__, 3).'/version.php';` — **a shim pointing back to the repository root**,
  where the real `3.0.1` lives. 🔵 **Moodle made the same `public/` migration and left a 404 instead.** Same
  shape as `Gap 370`: **this KB's probes read paths, and real projects indirect.**
- 🔴 🆕 **p95: `Gap 376` — the instrument has been unrunnable for three consecutive passes.**
  `grant-ladder-v4/ladder.sh` was denied before it started in passes 93, 94 and 95. 🟢 **The method is
  sound; the coverage is decaying.** **The next pass that can execute code must re-derive the full census
  before adding anything, and disagree with these pages on the record if it finds cause.**
- 🔴 **`Gap 369` carried.** Nothing on this shelf wires a knowledge-tracing model into an agent turn, so
  `pyBKT`/`pykt-toolkit` → agent is a build, not an integration. 🟡 **Pass 93 narrows it rather than
  closing it:** `P93-A` in `compose/patterns.md` now specifies that wiring concretely, but **no repository
  found this pass ships it**.

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
