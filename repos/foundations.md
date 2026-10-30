---
industry: education
region: Global
updated: 2026-10-30
---

# Foundational Education Repos

**Pass `p542` · 2026-10-30.** Load-bearing systems an education engagement is
likely to inherit, extend or integrate against — not agents (those are in
[`../agents/top.md`](../agents/top.md)), but the platforms, standards and
toolkits the agents must live beside.

🔴 **The count in this sentence was stale and is now stated as arithmetic rather
than asserted.** This header read *"Pass `p532` · **Fifty-eight**"* while `p533`
filed **eleven** further rows below it without touching it — so the headline
number was wrong for a whole pass, in the one place a reader looks first.
🟡 By pass arithmetic the figure is **fifty-eight + eleven (`p533`) + three
(`p534`) = seventy-two**; it is *derived*, not recounted, because several
sections here are **censuses** (the Moodle MCP census alone covers 222
addresses) and a row count and a "load-bearing system" count are not the same
quantity. 🔵 A recount against an explicit rule for what counts is `Gap 534-E`
— and until it runs, no total on this page should be quoted.

> 🟢 **`p530` adds a layer this file did not have: the e-learning standards
> implementations.** Twelve repos — SCORM runtimes, xAPI learning record stores,
> LTI frameworks, knowledge-tracing libraries and autograders. 🔴 **None of them
> is new to this base.** Every one was already in its append-only history, some
> across twenty passes, and none had ever reached a curated file. They surfaced
> only once `Gap 529-A`'s index existed
> ([`../ingest/address-ledger.py`](../ingest/address-ledger.py)).
>
> 🔵 **Why this layer decides engagements.** An institution does not buy a tutor;
> it buys something that plugs into the LMS it already runs. These twelve are how
> you plug in, and **eleven of the twelve are MIT, Apache-2.0 or BSD** — against
> a platform-core layer below that is almost entirely copyleft. 🔴 **The
> permissive surface of this sector is the integration layer, not the
> platforms.**
>
> 🔴 **One retrieval failure worth naming, because the search channel stated it
> as a capability gap.** Asked for an open-source grader this pass, generic
> search replied *"I found no open-source agent that grades students."* This base
> already owned **three permissive autograders totalling 2 337★**. The gap was
> never in the world.

> 🆕 **`p529` changed one section of this file and nothing else — the same
> section, again, and this time the correction runs the other way.** The GitHub
> search API became reachable this pass (see
> [`../agents/top.md`](../agents/top.md)), and it reports **`total_count: 222`**
> for the Moodle MCP field. `p528`'s census of eleven was not a census; it was a
> sample of what a search engine surfaced. 🔴 **The ceiling, the star total and
> the licence spread are all corrected below.** The platform-core and
> administration rows above were not re-read this pass except where the API
> corroborated them — `fsrs4anki` (**MIT, 4,119★**), `openeducat_erp` (**LGPL**,
> 900★ / **782 forks**) and `rosariosis` (**GPL-2.0**, 648★) all **confirmed**.

> 🆕 **`p528` changed one section of this file and nothing else.** The Moodle MCP
> census below was re-probed from scratch — existence first, then the licence
> file's title block — and `p527`'s reading of that field ("roughly three real
> codebases") is **corrected to eleven**. The platform-core rows were not
> re-read this pass and carry `p527`'s verification; their dates and digests are
> `p527`'s, not this pass's.

> **Every licence in this file was re-read this pass from the licence file's own
> title block**, fetched from `raw.githubusercontent.com` (reachable, while
> `github.com` and `api.github.com` return HTTP 403 through the session proxy).
> Star counts remain rounded page values. This changed one cell, and it was the
> cell `p526` flagged red — see the Frappe Education row.

> **Licence reality for this sector, stated plainly and confirmed again:** the
> mainstream education platforms are **copyleft**, not permissive. Moodle is
> GPL-3.0, Open edX and Canvas are AGPL-3.0. A targeted search for a mainstream
> Apache/MIT LMS returned none. This is not a gap in the research — it is the
> shape of the market, and it drives the architecture: **build permissive agents
> that integrate across a process or network boundary** (LTI, xAPI, REST, MCP)
> rather than forking an AGPL core and inheriting its obligations.

## 🆕 `p542` — one framework row off the French leg, and the Intel education suite read down to its components

🟢 **One row filed.** [`Intelligent-Internet/ii-agent`](https://github.com/Intelligent-Internet/ii-agent)
was **absent from this base entirely** — not in trending history, not on a
live page — and it arrived on the **French** leg, which is the clearest single
demonstration of `p542`'s corpus finding on
[`../agents/trending.md`](../agents/trending.md#-p542--2026-10-30).

| Repo | Licence (read as bytes) | Stars | Region (origin) | Why it is load-bearing here |
|---|---|---|---|---|
| 🆕 [`Intelligent-Internet/ii-agent`](https://github.com/Intelligent-Internet/ii-agent) | 🟢 **Apache-2.0** — `LICENSE` @`main`, **11 357 B**, canonical title block `Apache License / Version 2.0, January 2004` | **3.4k** · 524 forks | 🟡 Global — organisation `Intelligent-Internet`; country not stated on the page | *"II-Agent: a new open-source framework to build and deploy intelligent agents."* 156 commits. 🔵 **Filed as a foundation, not an agent, and the distinction is the point:** it is general agent infrastructure with **no education semantics at all**, which is precisely what an engagement wants underneath a tutor — the education-specific repos on this base are mostly *applications*, and swapping an application is expensive. **Apache-2.0 with its patent grant** puts it in the small set this base can hand a client without a licence conversation. ⚠️ **Not education-validated:** nothing on its page mentions teaching, tutoring or learners, so it is a substrate candidate on licence and generality, and **no pedagogy claim is made for it here.** |

### 🔵 `p542` — `open-edge-platform/education-ai-suite`, read down to its components

This base has carried the row since `p533` on licence and star count alone.
Read first-hand this pass, it is more actionable than its **2 stars** suggest,
and the shape of its numbers is the reason:

- **2 stars against 14 forks.** 🟢 A forks-to-stars ratio **above 1** is the
  signature of a repo being *derived from* rather than *bookmarked* — the
  inverse of the entire rest of this page — and `p540` built a forks-per-star
  ranking precisely to find this shape. **481 commits** behind it.
- **Named components, as the tree lists them:** `ai-teaching-assistant`,
  `smart-classroom`, `teacher-assistant-claw-demo`, `utils/flutter`. 🔵 The
  README's two applications are **Smart Classroom** — *"an extensible framework
  for processing, analyzing, and summarizing classroom sessions"*, with
  classroom statistics, student re-identification and classroom summaries — and
  **Teaching Assistant**, *"voice-first assistance in studying"* for
  self-directed learning.
- **Runtime:** audio and video pipelines *"accelerated with the OpenVINO™
  toolkit"*, targeting Intel CPUs, integrated GPUs and **NPUs**. 🟢 That makes
  it the only artefact on this page that is **on-premise by construction** —
  which is the EMEA data-residency and LATAM connectivity answer, in hardware
  rather than in policy.
- ⚠️ **Its own disclaimer, carried verbatim:** the applications are *"intended
  for reference and demonstration, not production."* It is a starting point and
  a benchmark harness, **not a deployable product**, and no pattern on this
  base should imply otherwise.
- 🔴 **One correction to how it is addressed.** The parent monorepo
  [`open-edge-platform/edge-ai-suites`](https://github.com/open-edge-platform/edge-ai-suites)
  (Apache-2.0, `LICENSE` @`main` **11 351 B**, 140★ / **170 forks**) is
  **absent from this base**, and it does **not** contain the education suite —
  its README states the Education AI Suite *"is developed in its own
  repository"*. 🔵 Worth knowing beyond this KB: the same monorepo carries
  **Metro, Manufacturing, Retail, Robotics, Health and Life Sciences, and
  Federal and Aerospace** AI suites under one Apache-2.0 grant, so five of
  Globant's other industry KBs have a verified, permissive reference body
  sitting at an address none of them hold.

### 🔴 `p542` — the probe shape that lost a grant, stated here because it is this page's risk too

[`ocademy-ai/machine-learning`](https://github.com/ocademy-ai/machine-learning)
has **two** root grants — `LICENSE-CODE` (MIT, 1 122 B) and `LICENSE-TEXT`
(CC-BY-4.0, 18 649 B) — and **nothing at `LICENSE`**. Twelve probes across
`LICENSE`/`.md`/`.txt`/`COPYING` × `main`/`master` return 404. 🟢 **Adding
`LICENSE-CODE` and `LICENSE-TEXT` to the probe surface is the whole fix.**
🔴 **The exposure is concentrated on this page rather than the agent shelf,**
because split-by-material-type grants are what *courseware and standards
bodies* use, and that is what a foundations page collects. **Every "no grant
found" verdict on a content-bearing repo here should be re-read as "not yet
probed".** Full working in
[`../agents/top.md`](../agents/top.md#-p542--the-licence-probes-shape-produced-one-false-negative-and-one-unnamed-grant-and-both-are-fixable).


## 🆕 `p540` — six rows off the gate-to-600, and the first forks-per-star ranking this base has run

🟢 **`Gap 539-B` asked for exactly this:** *"run the grant gate to 600 and rank
the permissive residue by forks-per-star."* Both halves delivered. 450 further
`LIVE` backlog addresses were probed at their resolved default branch (**600 of
3 869 now gated**; 3 269 remain), and the permissive residue was ranked.
Every row below was then read first-hand on `github.com` for its star and fork
counts — none is from memory, and none is gate-attested, because `make hooks`
was denied again (`Gap 540-E`).

| Repo | Licence | Stars · forks | **f/★** | Why it is foundational |
|---|---|---|---|---|
| [dspace/dspace](https://github.com/dspace/dspace) | 🟢 BSD-3-Clause | 1.1k · **1.5k** | 🟢 **1.364** | *"(Official) The DSpace digital asset management system that powers your Institutional Repository."* **More forks than stars** — the strongest institutional signal this base has measured. Every university that runs DSpace runs *its own* DSpace, which is what the ratio detects. The repository layer is where theses, datasets and OER already live, so it is the corpus an institutional RAG grounds on **before** anyone builds a tutor. |
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause | 8.4k · 2.1k | 0.250 | *"Multi-user server for Jupyter notebooks."* 🟢 **`Gap 539-D` closed by this row** — named in **44** of this base's files since `p531` and never carrying a measured star count until now. The standard way an institution gives every student an isolated, resourced compute environment; the substrate under every "AI teaching assistant in a notebook" pattern on [`../compose/patterns.md`](../compose/patterns.md). |
| [ucfopen/canvasapi](https://github.com/ucfopen/canvasapi) | 🟢 MIT | 681 · 192 | 0.282 | *"Python API wrapper for Instructure's Canvas LMS. Easily manage courses, users, gradebooks, and more."* Maintained by the University of Central Florida. Canvas itself is AGPL-3.0, so this is the **process-boundary** route this file's licence rule prescribes: integrate across the API, do not fork the core. 🟡 **Default branch is `develop`**, not `main` or `master` — pin accordingly. |
| [yetanalytics/xapipe](https://github.com/yetanalytics/xapipe) | 🟢 Apache-2.0 | 17 · 9 | 0.529 | *"LRSPipe is an xAPI Statement forwarding/middleware process governed directly by xAPI Profiles."* The piece between a Learning Record Store and everything downstream: filter, transform and forward learner statements under a declared Profile rather than ad-hoc code. 🟢 Completes the xAPI leg `learnmcp-xapi` opened on the agent shelf — that one *writes* statements, this one *routes* them. 🔴 17★: small, and the Profile governance is the reason to take it, not the community. |
| [EducationalTestingService/skll](https://github.com/EducationalTestingService/skll) | 🟢 BSD-3-Clause | 561 · 69 | 0.123 | *"SciKit-Learn Laboratory (SKLL) makes it easy to run machine learning experiments."* From **Educational Testing Service** — the organisation behind TOEFL and the GRE. Configuration-driven experiment running with the reproducibility discipline assessment work demands; the pairing for the efficacy layer `p535` filed. 🟡 Graded `UNKNOWN` by the title gate because its payload reads *"New BSD License"*. |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 🟢 Apache-2.0 | 30.1k · 3.2k | 0.106 | *"🤗 smolagents: a barebones library for agents that think in code."* 🟢 **`Gap 539-D` closed by this row** — named in **24** of this base's files and never measured. The minimal agent loop to reach for when LangGraph or CrewAI is more framework than a single tutoring or grading task needs. |

### 🔵 How to read the `f/★` column — and its two stated limits

Fourteen points were classed **first by what the software is** (does an
institution run its own copy, or import it as a dependency?) and only then
ordered by forks-per-star. Evidence:
[`../evidence/forks-per-star-rank.2026-10-30-p540.tsv`](../evidence/forks-per-star-rank.2026-10-30-p540.tsv).
🟢 **The classes separated with an empty band between them**: every
deploy-per-institution point at **≥ 0.250**, every import-as-dependency point at
**≤ 0.182**, no instance in between. Star counts do not do this —
`smolagents` (30.1k) and `jupyterhub` (8.4k) are both large and land on opposite
sides.

> **f/★ ≥ 0.25 → fork it.** Institutions run their own copy. Budget for
> carrying a fork: migrations, upgrades, local schema.
> **f/★ ≤ 0.15 → pin it.** It is a dependency. Budget for version drift.
> **Between, or under ~50 stars → the ratio says nothing.** Read the repository.

🔴 **Limit one: n = 14, one sector, one hour.** A boundary fitted to fourteen
points is a hypothesis. → `Gap 540-C` re-measures at n ≥ 60 before any recipe
may depend on the threshold.

🔴 **Limit two, demonstrated on the ranking's own output: the ratio ranks, it
does not vet.** [`Apereo-Learning-Analytics-Initiative/OpenLRS`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS)
(ECL-2.0, 47★ · 38 forks) scored **0.809** — second of fourteen — and its
repository description is the single word **"Deprecated"**. Forks-per-star
measures how software *was* used, which is past tense. A liveness read stays
mandatory before promotion, and this row is **not filed** above.

### 🔴 What the gate found that does not become a row — and why it matters more than the rows

37 of the 450 addresses served a grant file whose title the matcher could not
name. 🟢 **Every one resolved on a hand read** — not one was unnameable — across
**twelve** dialects. 🔴 **23 of 37 (62 %) are not buildable permissively**,
against ~0 % in the named-permissive buckets. `UNKNOWN` is not noise; it is
where this sector's non-buildable grants concentrate, at roughly eight times the
base rate. Full table and evidence on
[`trending.md`](trending.md#-p540--2026-10-30) and
[`../evidence/unknown-residue-graded.2026-10-30-p540.tsv`](../evidence/unknown-residue-graded.2026-10-30-p540.tsv).

🟡 **One dialect is a regional bias against the region this base exists to
serve.** [`portabilis/pre-matricula-digital`](https://github.com/portabilis/pre-matricula-digital)
is ordinary AGPL-3.0, graded `UNKNOWN` **only because its licence text is in
Portuguese**. An English-keyed classifier under-grades LATAM supply, and
"no grant found" reads downstream as "no supply". → `Gap 540-B`.

## 🆕 `p539` — the backlog's head was never obscure, it was the field's own infrastructure

🔴 **The measurement that reframes this file.** `p538` left the promotion queue
empty and set its successor a choice: generate a new queue from the `HISTORY`
bucket — **4 120 distinct addresses against 262 filed** — or find an unused
channel. `p539` built the queue
([`../ingest/history-backlog.py`](../ingest/history-backlog.py)) and then
gated it in bulk
([`../ingest/backlog-gate.py`](../ingest/backlog-gate.py)), and the result is
not a list of obscure repositories:

| | Value |
|---|---|
| `HISTORY` − `FILED` (the backlog) | **3 869** |
| 🟢 LIVE (`git ls-remote --symref`, all 3 873 probed) | **3 725 — 96.2 %** |
| 🔴 DEAD / PRIVATE | 148 — 3.8 % |
| Grant-gated at the ranked head | 147 of 150 live, **67 MIT · 18 Apache-2.0 · 2 BSD · 1 ISC · 1 ECL-2.0** |
| 🔴 UNRESOLVED on 46 grant filenames | 17 |

🔵 **So the 6.8 % filing rate is a promotion deficit, not a graveyard.** Only
3.8 % of the backlog is dead. The top of it — ranked by how many of this base's
own files name an address and never file it — reads
`openedx/edx-platform` (**59 files, 243 mentions**), `jupyterhub/jupyterhub`
(44 files), `plastic-labs/tutor-gpt` (37), `INGInious/INGInious` (34),
`frappe/erpnext`, `apache/ofbiz-framework`, `huggingface/smolagents`,
`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`. **This base has been describing the education
field's load-bearing infrastructure in prose for hundreds of passes without
putting it in a table row a successor can paste.**

🟢 **Filed this pass, every figure read first-hand from the repository page:**

| Repo | Licence | Stars · forks | Region | Why it is foundational |
|---|---|---|---|---|
| [AnubisLMS/Anubis](https://github.com/AnubisLMS/Anubis) | 🟢 **MIT** (`LICENSE` at `main`) | **382** · 54 | 🟢 **North America (USA)** — *stated*: *"battle tested at **NYU Tandon** for several semesters"* | *"Distributed LMS for automating Computing Science Courses From NYU."* Autogrades by running tests when a student pushes to their assignment repo, and serves browser **Cloud IDEs** (Theia) on **Kubernetes**. Topics `k8s` · `cloud-ide` · `learning-management-system`. 🟢 The only row here that is an LMS **and** an autograder **and** a per-student sandbox — the three pieces a code course needs and that this base has otherwise only had separately. |
| [inducer/relate](https://github.com/inducer/relate) | 🟡 **MIT by README text only** — sidebar names **no** licence; README carries MIT-style permission text, `Copyright (C) 2014-15 Andreas Kloeckner` | **437** · 125 | 🟡 unplaced — no institution named on the page | *"RELATE is an Environment for Learning And TEaching."* Django courseware: content authored in **YAML + Markdown under git**, so an instructor previews new content while students still see the old version; sandboxed code questions with autograding plus optional human second-stage marking; grade book, class calendar, live in-class quizzes. 🔵 **The git-versioned-content model is the asset** — it is the only row here where course material is a reviewable commit. |
| [Ed-Fi-Alliance-OSS/Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | 🟢 **Apache-2.0** (`LICENSE.txt` at `main`) | **28** · 48 | 🟢 **North America** — Ed-Fi Alliance, LLC in the copyright notice; the standard is US K-12 | *"The core code for the Ed-Fi Operational Data Store (ODS) and Ed-Fi ODS API."* 🟢 **The K-12 data substrate a US district engagement inherits whether or not anyone chose it.** 48 forks against 28 stars is the signature of an implementation base, not an audience — people deploy it, they do not admire it. 🔵 Pair with `1EdTech` for the standards layer: Ed-Fi carries the records, LTI/Caliper carry the events. |
| [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | 🟢 **MIT** (`LICENSE` at `main`) | **27** · 23 | 🟢 **EMEA (England)** — *stated*: *"a free job-listing service from the **Department for Education**"*, covering *"schools or trusts in England"* | **19 739 commits** on a live national government service, integrating **GOV.UK One Login** and DWP *Find a Job*. 🟢 **And it ships `AGENTS.md`, `CLAUDE.md` and `GEMINI.md` plus a documentation section titled *"Guidance for AI coding agents"*** — a state education department publishing its agent conventions in the open. 🔵 Read it for the conventions, not the domain: it is the clearest public example of how a public-sector education body expects agents to work inside its codebase. |
| [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | 🟢 **MIT** (`LICENSE` at `main`) | **6 500** (page rounds to 6.5k) · 1 100 | ⚪ Global | *"Policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents. Covers 10/10 OWASP Agentic Top 10."* Sits between an agent and the actions it takes; every tool call or data access is checked against policy first, with agent identity, isolated execution and audit records. SDKs in several languages plus framework adapters and a CLI. 🔴 **Education is not mentioned anywhere on the page, and that is stated rather than glossed.** 🟢 It is filed here because the 2026 education story is *governed* adoption — an Annex III high-risk assessment tool needs exactly an audit record and a policy gate, and this is the only permissive artefact on this base that provides them. **Public preview.** |

🔴 **Two rows the gate attested and this pass did NOT read first-hand**, recorded
as such so a successor does not mistake a gate for a page read:
[`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub)
(**BSD-3-Clause**, `LICENSE` at `main`) and
[`huggingface/smolagents`](https://github.com/huggingface/smolagents)
(**Apache-2.0**, `LICENSE` at `main`). Both are grant-attested from the licence
file's own bytes at the resolved default branch; **neither has a star count
measured this pass**, so none is written. `jupyterhub` is named in **44** of
this base's files and `smolagents` in **24**, and both remain unfiled on the
platform tables above — the single largest piece of promotion debt left.

🟢 **`apache/ofbiz-framework` proved the default-branch rule still earns its
keep.** Its default branch is **`trunk`**, not `main` or `master`. `p509` found
that defect, `p517` fixed it in
[`../ingest/probe-grant.sh`](../ingest/probe-grant.sh), and the bulk gate
inherits the fix — a probe that assumed `main` would have filed a top-20
backlog address as UNRESOLVED.

## 🆕 `p541` — eighteen rows off the promotion debt, and the EMEA public-sector layer this base never filed

🔵 **Where these came from.** Not from a search. p540 resolved the 37
`UNKNOWN` grants in its residue into twelve dialects **in prose** and filed
none of them. Graded against the committed tree by
[`gate-restated-presence`](../compose/code/p541-restated-presence/),
**32 of those 37 appear only in trending history** — measured, named, never a
row. That is `Gap 529-A`'s promotion debt with a number on it. Every grant
below was re-read first-hand this pass as **bytes at
`raw.githubusercontent.com`** (`github.com` HTML answers 403 through this
session's proxy) and the byte count is given so a successor can re-measure.

### 🟢 The Apereo sector layer — `ECL-2.0`, a real OSI licence both classifiers now name

🔵 **`ECL-2.0` is the Educational Community License**, Apache-2.0 with a
patent clause rewritten for university consortia. It is permissive and
Globant can build on it. It is also the single most common grant in this
residue, which says something about where education's institutional code
actually lives.

| Repo | Grant (bytes read) | What it is | Reuse |
|---|---|---|---|
| [`Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor`](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | 🟢 **ECL-2.0** (9,919 B) | The LAP batch engine: pulls from an LRS and a SIS, runs risk models, writes scores back | 🟢 The reference pipeline for dropout-risk work |
| [`Apereo-Learning-Analytics-Initiative/OpenDashboard-api`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) | 🟢 **ECL-2.0** (9,919 B) | The API half of the analytics dashboard | 🟢 Serve LAP output to an LMS |
| [`Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy) | 🟢 **ECL-2.0** (9,919 B) | The dashboard UI, explicitly `legacy` | 🟡 Read for the data contract, not to deploy |
| [`Apereo-Learning-Analytics-Initiative/lap-sakai-extractor`](https://github.com/Apereo-Learning-Analytics-Initiative/lap-sakai-extractor) | 🟢 **ECL-2.0** (11,087 B) | Extracts Sakai activity into the LAP schema | 🟢 The pattern to copy for a Moodle/Canvas extractor |
| [`KualiCo/rice`](https://github.com/KualiCo/rice) | 🟢 **ECL-2.0** (11,106 B) | Kuali Rice — the middleware under Kuali's higher-ed administration suite (workflow, identity, business rules) | 🟡 Large and institutional; take the workflow engine, not the suite |

🔴 **One warning carried from p540's ranking, not re-measured here:**
`Apereo…/OpenLRS` is already on this base and its GitHub description reads
**"Deprecated"**. The sector licence does not make a dead project live.

### 🟢 Assessment and standards

| Repo | Grant (bytes read) | What it is | Reuse |
|---|---|---|---|
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause** (2,058 B — *"The QTIWorks source code is distributed under the 3-clause BSD licence"*) | A **QTI 2.1** assessment engine — delivery, response processing, scoring | 🟢 **The permissive QTI implementation this base has wanted.** Standards-compliant item banks without an AGPL obligation |
| [`UCL-INGI/INGInious`](https://github.com/UCL-INGI/INGInious) | 🟡 **AGPL-3.0, SCOPED** (34,764 B; the file opens *"Most of the files in INGInious are distributed under the GNU AGPL"*) | Automated grading of programming assignments, container-isolated, from UCLouvain | 🔴 **Copyleft and the grant is not repository-wide.** `p382`'s subtree class: "most of the files" obliges a per-path read before any reuse |

### 🟢 The ladder's own blind spot — three MIT grants one rung further along

🔴 **Each of these three serves a two-line template fill-in at `LICENSE`** —
`YEAR: 2021 / COPYRIGHT HOLDER: …`, 45–47 B, written by R's
`usethis::use_mit_license()` — **and the real MIT text at `LICENSE.md`.** A
ladder that probes `LICENSE` and stops reads the fill-in and reports nothing.
🔵 `p275` taught this base that *"the LADDER, not the slug, is the defect"*;
this is that lesson in a shape its authors had not seen — **the file exists
and is not a grant.** All three `LICENSE.md` reads were confirmed **200,
`# MIT License`** this pass.

| Repo | Grant | What it is |
|---|---|---|
| [`rstudio/ggcheck`](https://github.com/rstudio/ggcheck) | 🟢 **MIT** (at `LICENSE.md`; `LICENSE` is a 45 B stub) | Inspects student `ggplot2` code for automated grading of data-viz exercises |
| [`rstudio/tblcheck`](https://github.com/rstudio/tblcheck) | 🟢 **MIT** (at `LICENSE.md`; `LICENSE` is a 46 B stub) | The table equivalent — grades student data frames against an expected result |
| [`shmercer/writeAlizer`](https://github.com/shmercer/writeAlizer) | 🟢 **MIT** (at `LICENSE.md`; `LICENSE` is a 47 B stub) | Automated scoring of **student writing quality** from scored corpora |

🔵 **Why these three are worth a row:** automated grading of *statistics and
writing* is the assessment case this base has otherwise only held for code.

### 🟢 EMEA, public sector — `opetushallitus`, seven national registries under `EUPL`

🟢 **This is the largest single block of **state-operated** education software
on this base, and it was entirely unfiled.** The Finnish National Agency for
Education publishes its production registries in the open. 🔴 **The grant is
licensed *by reference*, not reproduced**: each `LICENSE` is a ~650 B English
notice naming the **EUPL, Version 1.1 or subsequent** and pointing at
`joinup.ec.europa.eu` for the text. 🔵 **The version matters and the base had
it wrong by implication** — the only EUPL title either classifier carries is
**1.2**, and six of these seven say **1.1**.

| Repo | Grant (bytes read) | What it is |
|---|---|---|
| [`opetushallitus/koski`](https://github.com/opetushallitus/koski) | 🟡 **EUPL-1.1+** by reference (654 B notice) | The **national study-rights and completed-studies register**. 23★ · 12 forks |
| [`opetushallitus/eperusteet`](https://github.com/opetushallitus/eperusteet) | 🟡 **EUPL-1.1+** by reference (632 B) | The **national curriculum** service — the machine-readable core curriculum |
| [`opetushallitus/ehoks`](https://github.com/opetushallitus/ehoks) | 🟡 **EUPL-1.1+** by reference (632 B) | Personal competence-development plans for vocational students |
| [`opetushallitus/oppijanumerorekisteri`](https://github.com/opetushallitus/oppijanumerorekisteri) | 🟡 **EUPL-1.1+** by reference (632 B) | The national **learner-identifier** registry |
| [`opetushallitus/organisaatio`](https://github.com/opetushallitus/organisaatio) | 🟡 **EUPL-1.1+** by reference (632 B) | The register of educational **institutions** |
| [`opetushallitus/valtionavustus`](https://github.com/opetushallitus/valtionavustus) | 🟡 **EUPL-1.1+** by reference (653 B) | State **grant administration** for education providers |
| [`opetushallitus/ataru`](https://github.com/opetushallitus/ataru) | 🟡 **EUPL-1.2** by reference (296 B — the one that says 1.2) | The national **application and admissions** system |

🔴 **EUPL is reciprocal.** It is a copyleft licence with an EU-law
jurisdiction clause, so these are **reference architectures and integration
targets, not components to vendor into a client's proprietary stack.** 🟢
What they are worth is the **data model**: a working, legally published,
national-scale set of schemas for learners, institutions, curricula and
admissions — the thing every EMEA public-sector education engagement has to
invent otherwise.

### 🟢 Two general-purpose rows the residue also returned

| Repo | Grant (bytes read) | Note |
|---|---|---|
| [`crewAIInc/crewAI`](https://github.com/crewAIInc/crewAI) | 🟢 **MIT** (1,055 B, **untitled** body) | The multi-agent framework. 🔵 Filed because its grant was in the `UNKNOWN` residue for `p314`'s untitled-payload reason, not because this base lacked the name |
| [`hcengineering/platform`](https://github.com/hcengineering/platform) | 🟡 **EPL-2.0** (14,197 B) | Huly platform — project/knowledge management. 🟡 **Weak copyleft**: file-level reciprocity, so it is usable alongside proprietary code but not inside it |

### 🟢 Two Spanish-language curriculum repos, with a split grant worth reading as a model

| Repo | Grant (bytes read) | Note |
|---|---|---|
| [`CaminosMarina/curso-ia`](https://github.com/CaminosMarina/curso-ia) | 🟡 **SPLIT — content `CC BY-SA 4.0`** (`LICENSE`, 1,900 B) **and code `MIT`** (`LICENSE-CODE`, 1,534 B, confirmed 200) | A Spanish self-study AI curriculum running LLM fundamentals → agents → **MCP** → n8n automation. 🟢 **The licence structure is the lesson**: it separates the course text from the scripts, names third-party material as retaining its own terms, and says so in the file. 🔴 A roundup described this repo as "MIT"; MIT covers `scripts/` and lesson snippets only |
| [`thalisantunes/eecri-2026-ia-artesanato`](https://github.com/thalisantunes/eecri-2026-ia-artesanato) | 🟢 **MIT** (1,080 B, titled, `Copyright (c) 2026 Thalis Antunes de Souza`) | Workshop material from I EECri 2026 (Nova Porteirinha, MG, Brazil): slides, scripts, a prompt sheet, OpenSCAD models, and **blind prompt tests across five models**. 🔵 Thin on education-platform relevance; filed for the **blind-test methodology**, which is a reusable evaluation harness |

### 🔴 What the residue returned that must NOT become a row

🔵 Recorded so a successor does not re-discover them as finds. Seven payloads
are genuinely outside the stock table and **none is a permissive software
grant**: [`heronerar/OpenGaokao`](https://github.com/heronerar/OpenGaokao)
(*OpenGaokao Source-Available License 1.0*),
[`nakafaai/aksara`](https://github.com/nakafaai/aksara) (*Nakafa Source
Available 2.0*), [`sodadata/soda-core`](https://github.com/sodadata/soda-core)
(*Elastic License 2.0*),
[`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom)
(*AStheTECH Community License*),
[`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset)
(*Evaluation Dataset License* — field-of-use limited to evaluation),
[`aclascollege/polymath`](https://github.com/aclascollege/polymath) (**ODbL**,
a database share-alike and not a code grant), and
[`yuanjiusheng/cloud-learning-ce`](https://github.com/yuanjiusheng/cloud-learning-ce)
(**all rights reserved**, in Chinese). 🔴 Plus the six **bespoke-over-stock**
traps listed on [`../agents/top.md`](../agents/top.md#-p541--the-licence-traps-in-p540s-residue-and-why-gap-540-bs-own-remedy-is-unsafe).

## Platform cores

| Repo | Licence | Stars | Why it is foundational |
|---|---|---|---|
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | 9.3k | "A complete web conferencing system for virtual classes." README names **BigBlueButton 4.0**; default branch `v4.0.x-develop`. The default synchronous-classroom layer, already integrated into Moodle, Canvas and Open edX. LGPL is the friendliest copyleft here. |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 8.2k | The Open edX LMS + Studio authoring core. *(`openedx/edx-platform` now redirects here — use the `openedx-platform` address.)* The reference choice for MOOC-scale and large corporate-training deployments. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7.6k | "The world's open source learning platform." PHP, `main` branch, 123k+ commits. **Largest plugin ecosystem in the sector by a wide margin** — which makes the plugin boundary the cheapest place to attach anything new, and makes the missing Moodle MCP server (see below) the loudest gap on this base. |
| [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** | 7.0k | "A free, online learning platform to make quality education accessible for all." Python + Angular on App Engine. **The largest permissively licensed learning platform found** — the one core on this shelf a studio can fork without copyleft consequences. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 6.9k | "The open LMS by Instructure, Inc." Dominant in North American higher ed. Caveat worth repeating to any client: the open-source codebase is **not** equivalent to Instructure's full commercial feature set. |
| [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | 3.4k | "Easy to Use, 100% Open Source Learning Management System." Title block read this pass: `GNU AFFERO GENERAL PUBLIC LICENSE Version 3`. Lighter and newer than Moodle, sitting on the Frappe/ERPNext stack — the natural LMS when the client already runs Frappe for administration. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 1.2k | Higher-ed teaching, research and collaboration platform. Title block: `Educational Community License, Version 2.0 (ECL-2.0)` — an Apache-2.0 derivative with a patent-grant tweak for academic consortia, **permissive in practice**. Page lists 25.2 and 23.5 as community-supported. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1.2k | "The offline app for universal education." Python + JS, `develop` branch, ~39.8k commits. **The only MIT-licensed full learning platform on this shelf**, and the only one designed for intermittent or absent connectivity — the deciding constraint for LMIC and rural deployments in LATAM, Africa and South/Southeast Asia. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 | 1.1k | "The Docker-based Open edX distribution designed for peace of mind." In practice nobody should deploy Open edX by hand; this is the supported path, and the plugin system is where customisation belongs. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1.0k | LMS focused on ease of use and accessibility; install docs reference **v2.0.3**. Strong footprint in Spanish- and French-speaking deployments with small or no technical staff — relevant for LATAM public-sector work. |

## Administration, records and integrity

| Repo | Licence | Stars | Why it is foundational |
|---|---|---|---|
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 900 | "Comprehensive Open Source ERP for Educational Institutes", built as Odoo modules; branch `19.0`. Admissions, timetabling, attendance, fees, library, hostel. The ERP counterpart to the LMS cores above. |
| 🔵 [frappe/education](https://github.com/frappe/education) | **GPL-3.0** — *resolved this pass* | 685 | "Open source education / school management system." **`p526` left this red:** the repository page renders no licence type and a `license.txt` is present but unnamed. Fetched directly this pass, the file is three lines of front matter — `--- / License: GNU GPL V3 / ---` — so it is **GPL-3.0**: strong copyleft, *not* permissive, and **not the same licence as Frappe LMS**, which is AGPL-3.0. Two apps, same stack, two different copyleft regimes; a deliverable spanning both inherits both. 472 forks. |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 | 722 | **LATAM anchor.** School-management software described on its own page as "the largest free education software in Brazil" — originally built by the municipal government of **Itajaí, Santa Catarina**, released on the Brazilian federal Public Software Portal in 2008, now stewarded by Portábilis. Any Brazilian public-sector education engagement meets this system. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 648 | "RosarioSIS Student Information System for school management." PHP/PostgreSQL, modular, widely deployed in small and mid-size schools; strong Spanish/French/Portuguese localisation. Origin is not stated on the repo page. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | **EMEA anchor.** German non-profit-governed LMS, branch `release_11`. The usual choice for compliance-heavy European public-sector and government training, where governance provenance matters as much as features. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | 449 | **EMEA, permissive.** Swiss web-based LMS covering teaching, learning, assessment and communication. Apache-2.0 plus a European governance story is a rare combination on this shelf — the best base for an EMEA engagement that needs to ship proprietary extensions. |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | 355 | "Source code plagiarism detection" — finds similar or modified solutions to programming exercises. Copyright line reads `Team Dolos <dolos@ugent.be>`, i.e. **Ghent University (EMEA)** — read from the licence file, not inferred. No LLM in it, and that is the point: assessment-integrity findings have to be explainable to an appeals board. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 152 | Framework-independent PHP library for H5P interactive content; grant at **`LICENSE.txt`**. H5P is the de facto interoperable format for interactive exercises across Moodle, Canvas, Open edX and Drupal — the cheapest way to make generated content portable. |
| [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | GPL-2.0 | 64 | QTI-standard computer-based assessment core. The right base when items must interoperate with national testing infrastructure. |
| [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | 51 | "The ultimate Learning Record Store (and more!) for your learning analytics." Python/FastAPI/Pydantic; copyright line reads `France Université Numérique` (**EMEA**). Fifty-one stars and genuinely load-bearing: it is the **xAPI/LRS seam** where agent-generated learning events get stored in a standard shape instead of a vendor's private table. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | 4.1k | FSRS (Free Spaced Repetition Scheduler). The retention primitive — use it instead of inventing a review interval, because the scheduling problem is solved and the solution is permissive. |

## 🆕 The Moodle MCP census — 🔴 **222 addresses, not eleven; ceiling 52★ and ungranted**

> 🔴 **`p529` correction, read this before the table.** The heading of this
> section used to read *"eleven codebases, 37 stars, no convergence"*. The API
> reports **222** matching addresses; `p529` read the **top 80 by stars**, which
> alone total **352★**. The field's ceiling is **not** `G36maid` at 27★ — it is
> [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) at **52★**, and
> ⛔ **it has no licence file** (no `license` key from the API; no file at five
> paths on `main`). The permissive ceiling is
> [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server),
> **MIT, 45★**, last pushed **22 Feb 2026**. Licence spread over the 80 read:
> **MIT 44 · none 18 · GPL-3.0 7 · `NOASSERTION` 4 · Apache-2.0 4 · AGPL-3.0 2 ·
> WTFPL 1** → **60% permissive, 27.5% with no usable grant** — not *"ten of
> eleven MIT"*.
>
> 🔵 **And the conclusion changes with the number.** `p528` recommended
> consolidating eleven codebases. **You cannot consolidate 222 repositories whose
> purpose is to be institution-specific** — 14 of the top 26 bridge one named
> university each, and LATAM and APAC ship five apiece while **North America
> ships none**. The asset is a **bridge generator**, not a merged bridge. Full
> census, regional placement and reasoning in
> [`trending.md`](trending.md); the recipe is `P558` in
> [`../compose/patterns.md`](../compose/patterns.md).
>
> ⚠️ **The table below is `p528`'s thirteen-address census, kept as-is**, because
> its tool counts and read/write analysis are first-hand and the API exposes
> neither. **Read it as a deep sample of the field, not as the field.**

⚠️ **This section is corrected and widened this pass.** `p527` wrote that the
Moodle MCP field is *"eight search results, roughly three real codebases"*. That
was wrong, and it was wrong in the direction that matters: the field is not
small, it is **fragmented**. `p528` probed **twelve addresses first-hand** —
existence first (`README.md` on `main` and `master`), then the licence file's
title block — for a census of **thirteen**. ⚠️ The thirteenth,
`triffon/moodle-mcp`, is **carried from `p527`** as a confirmed duplicate of
`falkenslab` and was *not* re-probed this pass; its row is marked. The thirteen
resolve to **eleven independent codebases plus two forks**.

| Repo | Licence (title block) | Stars | Lang | Tools | Reads / writes |
|---|---|---|---|---|---|
| [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | **MIT** | **27** | Rust (`rmcp`) | 22 (20 typed + 2 escape hatches, opt-in via `MOODLE_ENABLE_WS_FUNCTION`) | Web Services; courses, assignments, forums, grades, files-as-markdown. **Verified live against Moodle 3.7, 4.5 and 5.2** — the only one on this list that names three tested versions. |
| [thc1006/moodle-mcp](https://github.com/thc1006/moodle-mcp) | MIT (`© G36maid`) | 0 | Rust | 22 | ⛔ **Fork of the above**, stated on the page; the copyright line confirms it. |
| 🆕 [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) | **MIT** (`© Ghaith AlHallak`) | 3 | Python 3.14+ | **40** (32 read / 8 write) | Writes **off by default** behind two separate flags (`MOODLER_ALLOW_STUDENT_WRITES`, `MOODLER_ALLOW_TEACHER_GRADING`); destructive calls require `confirm=true`. Playwright/Chromium sign-in, SQLite cache, ships as a `.mcpb` bundle. 🟢 **The best-governed write model in the census.** |
| 🆕 [Faixiang/moodle-mcp](https://github.com/Faixiang/moodle-mcp) | **MIT** | 2 | Python 3.8+, **stdlib only** | 8 | Read-only against Moodle (the one exception, `moodle_download_week`, writes to local disk). Single `server.py`, zero dependencies, docs in 10 languages, verified against Moodle 4.3.6. ⚠️ `v1.3.0` dated 2026-10-27 — **and all four changelog entries, 1.0.0 through 1.3.0, carry that same date.** Treat the version history as a self-claim. ⚠️ Its own "Why this exists" section still says *"six read-only tools"* against a table of eight. |
| 🆕 [leshamblin/MoodleMCP](https://github.com/leshamblin/MoodleMCP) | **MIT** | 2 | Python 3.10+, FastMCP | **70 claimed / 67 counted** | Read *and* write, with the clearest safety story: read-only by default, writes confined to `MOODLE_DEV_COURSE_WHITELIST`, `MOODLE_PROD_ALLOW_WRITES=false` recommended, token in a local `.env`. Writes cover grading, enrolment, messages and forum posts. |
| [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) | **MIT** | 2 | — | **~230 claimed** | Drives a logged-in **browser session** rather than Web Services; README claims grading-with-rubrics and quiz construction for Moodle 4.5/5.x. ⚠️ Largest tool claim in the census and the least verifiable; a search summary said 140, the README says ~230, **neither is verified by use.** |
| [triffon/moodle-mcp](https://github.com/triffon/moodle-mcp) | MIT (`© Falkenslab`) | — | — | ~230 | ⛔ **Same code as `falkenslab`** — identical copyright holder and description. Not an independent project. |
| 🆕 [Jawadh-Salih/moodle-mcp-server](https://github.com/Jawadh-Salih/moodle-mcp-server) | **MIT** | 0 · 2 forks | **Go** | 14 | 13 read + `submit_assignment` (write) + `login`. Also exposes a REST mode for ChatGPT and Gemini. Student-facing. README examples use a `uom.lk` domain (University of Moratuwa, **Sri Lanka**) — 🟡 *inferred*, not stated. |
| 🆕 [sonstellar969/open-moodle](https://github.com/sonstellar969/open-moodle) | **MIT** — 🔴 **but see the dependency** | 0 | Python | 14 | Read-mostly CLI + MCP server; SQLite FTS5 search. 🔴 **Its own page states that PyMuPDF, its PDF-extraction dependency, is AGPL-3.0.** A repo-level licence probe grades this buildable; the shipped artefact carries network copyleft. ⚠️ Also notes its `moodle_mobile_app` token *can* permit writes on some sites — so "read-only" here is a property of the deployment, not of the code. |
| 🆕 [AnonymousOnyx22/moodle-student-mcp](https://github.com/AnonymousOnyx22/moodle-student-mcp) | **MIT** | 0 | TypeScript / Node 20+ | 12 | Read-only by construction — *"can never submit, edit or delete anything."* States *"Not affiliated with Moodle Pty Ltd."* |
| [duck-5/moodle-mcp](https://github.com/duck-5/moodle-mcp) | **MIT** | not read | — | — | Independent small implementation; existence and grant re-confirmed `p528`, star count not read. |
| ⚠️ [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** (title block: *"GNU AFFERO GENERAL PUBLIC LICENSE"*) | 1 | TypeScript / Node | — | The most *visible* in search results and **the one that is not permissive.** Read-only by design, no plugin install needed. AGPL-3.0 §13 on an integration server a hosted deliverable calls is an architecture decision, not a detail. |
| ⛔ [tosuki/moodle-mcp](https://github.com/tosuki/moodle-mcp) | **none** | — | — | — | A search result called it *"MIT licensed."* Repository **resolves**; **no licence file at any of six common paths on `main`.** ⛔ Ungranted — `p527`'s call, re-confirmed this pass. |

**The read, corrected.** Thirteen addresses, **eleven independent codebases**,
**four languages**, tool counts spanning **8 → ~230**, and **37 stars in total
across every codebase whose counter was read this pass** — less than one eighth
of [canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) alone (**308★**), for
the *larger* install base.

🟢 **Ten of the eleven independent codebases are MIT.** That is the finding that
changes the build decision. The gap is not a licensing problem and not an
absence — it is 🔴 **a convergence problem**: no two of these agree on a tool
vocabulary, nobody is above 27★, and the one project with real traction is
written in Rust while the mass of the field is Python.

🔵 **So the build is a consolidation, not a greenfield.** The pieces to take, all
MIT, all verified this pass: **G36maid's typed-tool surface and tested version
matrix**, **moodler-mcp's two-flag write gate with `confirm=true`**,
**leshamblin's course-whitelist boundary**, **Faixiang's zero-dependency
posture**. The thing none of them has is a **shared tool vocabulary** — and that,
not another server, is what would make this the sector's bridge. See
[`../compose/patterns.md`](../compose/patterns.md) **P553**.

⚠️ **One caveat on the whole census:** every star count here is a rounded page
value read through the session proxy, and every tool count is the repository's
own claim. Three of them contradict themselves on that claim (Faixiang 6 vs 8,
leshamblin 70 vs 67, falkenslab 140 vs ~230). **Tool counts in this field are
marketing, not measurement.**

## 🆕 Standards, records and assessment — the integration layer (`p530`)

Grants read from the licence file's own title block; counters exact from the API
this pass. **Passes unfiled** is from
[`../evidence/address-ledger.tsv`](../evidence/address-ledger.tsv) — how many
distinct passes described the address before anything filed it.

| Repo | Licence | Stars | Passes unfiled | Why it is foundational |
|---|---|---|---|---|
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | 956 | — | The xAPI specification itself, from US DoD ADL — the vocabulary every learning-record claim in this sector is written against. 402 forks. 🟡 Apache-2.0 on a *specification document* is deliberate, not a category error: the patent grant is the point. |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 | 144 | 🔴 **19** | A SQL-backed xAPI Learning Record Store. Clojure, runs on Postgres/SQLite. **This is where agent-generated learning events belong** — an institution will ask where the data lands, and an LRS is the standards-compliant answer. |
| [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) | Apache-2.0 | 334 | — | ADL's own reference LRS, Python. 156 forks. 🟡 Pushed **2025-11-14** — the reference implementation, not the one to deploy; `lrsql` is the live option. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | MIT | 361 | 🔴 **20** | A modern SCORM JavaScript runtime (SCORM 1.2 / 2004 / AICC), offline-first, cross-frame. TypeScript. **The bridge to every legacy course package an institution already owns**, and the reason an AI layer need not discard existing content. |
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | Apache-2.0 | 377 | 🔴 **14** | LTI tool framework — build a tool once, launch it inside Moodle, Canvas, Sakai or Open edX. 267 forks. **The cheapest route to putting an agent inside an LMS an institution will not replace.** |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | Apache-2.0 (`LICENSE.md`) | 54 | — | IMS-certified LTI 1.3 tool-provider library, PHP. 🔴 **A fork, so GitHub repository search does not return it** — see shelf rule 10. Certification is what matters here, not the star count. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0 | 471 | 🔴 **15** | The Open edX component SDK: the supported way to add a custom learning component to an AGPL-3.0 platform **without touching the platform's code**. 231 forks. 🔵 Note the grants differ — the SDK is Apache-2.0 while the core is AGPL-3.0. |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | MIT | 291 | — | Bayesian Knowledge Tracing and extensions, from Berkeley's CAHLR — the same lab behind [OATutor](https://github.com/CAHLR/OATutor) on the agent shelf. C++ core with Python bindings. **Mastery estimation that a faculty board will accept**, because it predates the LLM era and has a literature. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | 453 | — | pyKT: benchmark library for deep knowledge tracing, with standard datasets and prediction scenarios. **The way to show an adaptive claim is measured rather than asserted.** |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | BSD-3-Clause | 1 370 | — | Assigning and grading Jupyter notebooks — release, collect, autograde, manual-grade, return feedback. 345 forks. **The highest-starred permissive grading system in this sector.** |
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | BSD-3-Clause | 806 | — | Homework submission, automated grading and TA grading, from RPI. **1 118 forks against 806 stars** — a deployment-heavy system, i.e. institutions actually run it. |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | BSD-3-Clause | 161 | — | Python *and* R autograding, container-based, from Berkeley Data Science. The lighter alternative to Submitty when only the grading half is wanted. |

🔴 **What this layer does not contain: an agent.** Every row above is
infrastructure an agent would *drive*. The composition is in
[`../compose/patterns.md`](../compose/patterns.md).

## 🆕 Serving the course — the JupyterHub deployment family (`p531`)

🔴 **This is the single largest coherent layer this base has ever been missing,
and it was not missing from the world — it was missing from this file.** Every
row below sat in an `archive/` snapshot and **nowhere in the live corpus**: they
are part of the **349** addresses `Gap 530-A` measured as dropped by a rewrite.
`p531` read the grant of all 349 first-hand and these came back **BSD-3-Clause,
every one**, title block `BSD 3-Clause License · Copyright (c) 2016/2017,
Project Jupyter Contributors`.

🔵 **Why it is foundational and not plumbing.** This file already carries
[`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) (1 370★) — how you
*grade* notebooks. It carried nothing about how a university *serves* them to
500 students, authenticated out of the LMS they already log into, on hardware
they already have. That is the whole gap between a notebook demo and a course,
and it is **nine live repositories, 2 309★, all permissive**.

| Repo | Licence | Stars | Forks | Last push | What it is for |
|---|---|---|---|---|---|
| [jupyterhub/kubespawner](https://github.com/jupyterhub/kubespawner) | **BSD-3-Clause** | **611** | 308 | 2026-10-27 | Spawns each student's notebook server as a Kubernetes pod. **The default answer for a cohort of any size**, and the one that makes per-student resource limits a config value rather than a project. |
| [jupyterhub/dockerspawner](https://github.com/jupyterhub/dockerspawner) | **BSD-3-Clause** | **543** | 305 | 2026-10-27 | The same, in Docker containers on one host. 🟢 The right choice for a single-department pilot, and the cheapest credible demo in this layer. |
| [jupyterhub/oauthenticator](https://github.com/jupyterhub/oauthenticator) | **BSD-3-Clause** | **443** | 367 | 2026-10-27 | OAuth2 sign-in — Google, GitHub, Globus, generic OIDC. The institutional-identity half for any tenant that already runs SSO. |
| [jupyterhub/ldapauthenticator](https://github.com/jupyterhub/ldapauthenticator) | **BSD-3-Clause** | **214** | 177 | 2026-08-20 | LDAP/AD sign-in. 🔵 Named separately because in public-sector and EMEA university estates **this, not OAuth, is what the directory speaks**. |
| [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | **BSD-3-Clause** | 73 | 55 | 2026-07-01 | 🔴 **The row that connects this layer to the rest of the file.** Launch the hub *from inside Moodle, Canvas or Brightspace* over LTI, so the student never sees a second login. Known to this base since `p13` and described in **13 separate passes** without ever being filed. |
| [jupyterhub/batchspawner](https://github.com/jupyterhub/batchspawner) | **BSD-3-Clause** | **207** | 137 | 2026-07-17 | Spawns into Slurm/PBS/LSF batch queues. **The HPC route** — the deciding row wherever the client's compute is a research cluster, which in higher education it usually is. |
| [jupyterhub/systemdspawner](https://github.com/jupyterhub/systemdspawner) | **BSD-3-Clause** | 101 | 45 | 2026-10-24 | systemd units with real resource limits, no container runtime. The answer when Docker is not permitted on the box. |
| [jupyterhub/wrapspawner](https://github.com/jupyterhub/wrapspawner) | **BSD-3-Clause** | 65 | 60 | 🟡 2025-08-16 | Lets the *student* pick a spawner/profile at launch. 🟡 Fourteen months stale — read it, pin it, do not assume maintenance. |
| [jupyterhub/sudospawner](https://github.com/jupyterhub/sudospawner) | **BSD-3-Clause** | 52 | 39 | 2026-08-05 | Spawns as the student's own Unix user via a narrow sudo rule. The shape a university's own sysadmins will ask for. |

🔴 **Two members of the family are archived by their owner and are read-only
history:** [`jupyterhub/yarnspawner`](https://github.com/jupyterhub/yarnspawner)
(19★, Hadoop/YARN) and
[`jupyterhub/jupyterhub-tutorial`](https://github.com/jupyterhub/jupyterhub-tutorial)
(**202★**). 🔵 The second is worth naming precisely because it is the thing a
reader would reach for first: **the official deployment tutorial is archived**,
so an engagement should budget its own runbook rather than cite that one. 🟡
[`jupyterhub/kerberosauthenticator`](https://github.com/jupyterhub/kerberosauthenticator)
(12★, BSD-3-Clause, live) completes the authenticator set for Kerberos estates.

## 🆕 The LTI libraries this base has described 55 times and never filed (`p531`)

🔴 **`p530` built the integration layer above and filed the PHP LTI library
while leaving the Node and Python ones unfiled.** These are the **#1 and #2
most-described unfiled permissive addresses in the entire live corpus**, by the
base's own ledger:

| Repo | Licence | Stars | Forks | Passes unfiled | Why it is foundational |
|---|---|---|---|---|---|
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** | **373** | 86 | 🔴 **28** | *"Turn your application into a fully integratable LTI 1.3 tool provider."* TypeScript/Node. **The reference implementation of the Node LTI stack** — the one an agent written in TypeScript attaches to any LMS with. Pushed 2026-10-13. |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** | **138** | 84 | 🔴 **27** | LTI 1.3 Advantage tool for Python, with Django/Flask adapters. 🟢 The Python counterpart, and therefore the one that sits in front of a Python agent without a language boundary. Pushed 2026-09-10. |
| [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** | 6 | 3 | 11 | Dependency-light, framework-neutral TypeScript reference implementation of **QTI 3** assessment items. 🔵 QTI is how an assessment moves between systems; this is the only permissive, current QTI 3 implementation this base has found. |
| [jdolny/OneRoster.NET](https://github.com/jdolny/OneRoster.NET) | **MIT** | 6 | 8 | 12 | OneRoster API client. 🔵 OneRoster is **rostering** — the standard a district uses to tell a tool who is in which class. Thin, .NET-only, and the only permissive client on record. |
| [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) | **Apache-2.0** | 61 | 31 | 12 | Open Badges validation, Python, **from the standards body itself**. The credential half: if a deliverable issues badges, this is what says whether they are well-formed. |
| [Apereo-Learning-Analytics-Initiative/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | **ECL-2.0** | 62 | 25 | 12 | Apereo's Learning Record Warehouse — Caliper/xAPI ingestion with a OneRoster-shaped model. 🟡 ECL-2.0 behaves as permissive (Apache-2.0 with an academic patent tweak), which this base has already graded on `sakaiproject/sakai`. |

## 🆕 Assessment science, and the licence-compliance instruments (`p531`)

| Repo | Licence | Stars | Forks | What it is for |
|---|---|---|---|---|
| [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** | **153** | 37 | **Computerised Adaptive Testing** simulator: item-response theory, item selection, ability estimation, stopping rules. 🟢 **The only permissive CAT/IRT implementation on this base**, and the thing that separates "an LLM asks harder questions" from a defensible adaptive assessment. Author in Brazil — **LATAM-origin psychometrics**. Pushed 2026-10-28. |
| [open-spaced-repetition/fsrs.js](https://github.com/open-spaced-repetition/fsrs.js) | **MIT** | **180** | 14 | FSRS — the scheduler that superseded Anki's SM-2. The retention half of any tutoring deliverable, as a library rather than a prompt. |
| [VienDinhCom/supermemo](https://github.com/VienDinhCom/supermemo) | **MIT** | **337** | 24 | SM-2 in JS/TS. 🔵 Filed beside FSRS deliberately: SM-2 is simpler, auditable in an afternoon and still what a client's existing flashcard data was scheduled with. |
| [aboutcode-org/scancode-toolkit](https://github.com/aboutcode-org/scancode-toolkit) | **Apache-2.0** (code) · 🟡 **CC-BY-4.0** (licence datasets) | **2 656** | 831 | 🔴 **`Gap 528-C` closes here, with a retrieval instead of a build.** Its own README states it *"detects licenses, copyrights, package manifests, **direct dependencies**"* and *"can process packages, build manifest and lockfile formats"* — which is exactly the dependency-grant enumerator `528-C` had scoped as new work for four passes. 🟡 **Read the dual grant before shipping:** the engine is Apache-2.0, the reference licence data is CC-BY-4.0, so redistributing the rule set carries attribution duties. |
| [oss-review-toolkit/ort](https://github.com/oss-review-toolkit/ort) | **Apache-2.0** | **2 109** | 393 | The orchestrated form of the same job: an *Analyzer* that *"determines the dependencies of projects and their metadata, abstracting which package managers are actually being used"*, plus an Evaluator for policy-as-code. 🟢 Pick `ort` when the client wants a **gate in CI**; pick `scancode` when they want the **evidence**. |
| [anchore/syft](https://github.com/anchore/syft) | **Apache-2.0** | **9 792** | 1 031 | SBOM generation from images and filesystems (SPDX, CycloneDX). The deployed-artefact view, where the other two read the source tree. |

🔵 **Five of the six rows above came out of a drop set, and the sixth off the
live promotion queue** — `catsim` had been described in **10** separate passes
and never filed; `ort`, `syft`, `fsrs.js` and `supermemo` are in the **349**
archive-only addresses `p531` triaged; `scancode` is in `archive-drops`, the
691-row looser bound. 🔴 **Four licence/SBOM instruments — `scancode`, `ort`,
`syft`, [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli)
(Apache-2.0, 552★) — were owned, dropped, and then re-scoped as a build.** That
is `Gap 528-C`'s whole history, and it is a retrieval failure, not a supply gap.

## 🆕 Two platform rows the drop set also returned (`p531`)

| Repo | Licence | Stars | What it is |
|---|---|---|---|
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** | **823** | *"Interactive Learning with Automated Feedback"*, from **TU München**. Programming, modelling, text and quiz exercises with automated assessment and an exam mode, in production across European universities. 🔴 **MIT, 823★, 395 forks, pushed today — and this base had no row for it.** The strongest permissive assessment platform in EMEA, and the natural alternative to bolting autograding onto Moodle. Ansible collection: [`ls1intum/artemis-ansible-collection`](https://github.com/ls1intum/artemis-ansible-collection) (MIT). |
| [opensacorg/learning-blocks](https://github.com/opensacorg/learning-blocks) | **MIT** | 6 | 🟢 **A second permissive Student Information System.** `p529` published *"zero permissive SIS"*; `p530` falsified it with `academico-sis/academico` (MIT, 409★). This is the third reading: the field is small and thin, but it is **not empty and not copyleft-only**. 22 forks against 6★ — more forks than stars, the signature of a system people deploy rather than star. Python. Pushed 2026-09-21. |

## 🆕 The LMS agent-bridge layer completes — Blackboard was the hole (`p532`)

Every row below came off the **ranked** promotion queue
([`../evidence/promotion-queue.2026-10-29-p532.tsv`](../evidence/promotion-queue.2026-10-29-p532.tsv)),
not off a search, and every grant was read this pass from the licence file's own
title block over `raw.githubusercontent.com`.

> 🔴 **The hole this closes.** This base has carried a Canvas bridge since `p490`
> (`canvas-mcp`, MIT, 308★), filed a Brightspace bridge at `p531`
> (`brightspace-mcp-server`, MIT, 60★), and censused the Moodle MCP field twice
> — while saying nothing about **Blackboard Learn**, which is one of the four
> LMS platforms a Western higher-ed engagement actually meets. The bridge
> existed, MIT-licensed, and this base had described it in **8 separate
> passes**.
>
> 🟡 **Read the star counts honestly.** `bb-mcp` is **2★** and
> `MarcosNahuel/moodle-mcp` is **1★**. These are not adopted projects; they are
> *correct starting points with a permissive grant*, which in this layer is the
> scarce thing — `p529` measured the Moodle MCP field at **222 addresses with a
> 52★ ceiling that is ungranted**. A studio forks one of these; it does not
> depend on it.

| Repo | Licence (title block) | Stars | Passes unfiled | Why it is foundational |
|---|---|---|---|---|
| [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | 🟢 **MIT** — `MIT License · Copyright (c) 2026 nitsuah` (1 063 B, `e024d09e682a`) | 2 | 🔴 **8** | **The Blackboard Learn bridge this shelf had no row for.** A *standalone* MCP server wrapping the Blackboard Learn REST API — its README argues the case explicitly: *"the integration logic lives here, not in the client… build it once, use it everywhere."* Any MCP client (Claude Desktop, Cursor, agent-board) attaches unchanged. 🔵 With this row the agent-bridge layer covers **all four** major LMS platforms: Canvas, Brightspace, Moodle and Blackboard. |
| [MarcosNahuel/moodle-mcp](https://github.com/MarcosNahuel/moodle-mcp) | 🟢 **MIT** — `MIT License · Copyright (c) 2026 Italicia` (1 065 B, `f27341a8425b`) | 1 | 🔴 **9** | **The most capable Moodle MCP this base has read, and the field's own census said the ceiling was ungranted.** Wrapper **v0.5.2** + a companion Moodle plugin **v0.5.0**, exposing **40 high-level facades** plus one `ws_raw` escape hatch, over Moodle Web Services, with *idempotency guarantees* — its README claims ~80% of a course teaching workflow operable from an agent. 🟡 Spanish-language file paths and an `Italicia` copyright; **no country stated**, so unplaced. |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **MIT** — `MIT License · Copyright (c) Microsoft Corporation` (1 141 B, `c2cfccb812fe`) | 🔴 **78.1k** | 🔴 **23** | **Courseware, not an agent — and filed here for exactly that reason.** 18 lessons on building AI agents, with runnable Python on Microsoft Agent Framework and Foundry. For an education engagement this is the *reference curriculum artefact*: the thing to fork when a client wants an AI-literacy track with working code, and the thing to point at when asked what a well-structured 18-lesson technical course looks like. 🔴 **The single largest promotion debt in this base's history** — described in 23 passes, filed in none until now. |

## 🆕 The materiality-ranked queue's first eleven rows (`p533`)

Every row below came off
[`../evidence/promotion-queue.2026-10-29-p533.tsv`](../evidence/promotion-queue.2026-10-29-p533.tsv)
— the queue `Gap 532-B` asked for, gated on grant and liveness and ranked by
**measured** stars rather than by how often this base had mentioned the address.
Grants marked 🟢 were read this pass from the licence file's own title block over
`raw.githubusercontent.com`; the rest are API SPDX ids, flagged as such per shelf
rule 8.

> 🔴 **The queue's own headline: recall ranked an unusable address first and the
> largest permissive asset in this sector eighteenth.** See
> [`trending.md`](trending.md). The three A-band rows below had been described in
> this base **5, 7 and 7 separate passes** and filed in none.

| Repo | Licence | Stars | What it is, and why it is here |
|---|---|---|---|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 🟢 **BSD-3-Clause** (`main/LICENSE.md`) | 🔴 **458,181** | *"freeCodeCamp.org's open-source codebase and curriculum."* 🔴 **The largest permissive asset this base has ever touched, by a factor of 32 over the next-largest unfiled address**, and it sat at recall rank 18. 🟡 **Read what it is before costing it in:** this is a **curriculum plus the platform that delivers it**, not a library — the reusable parts are the curriculum corpus, the challenge/test format and the certification model. BSD-3-Clause means all of it may be reused with attribution. 🔵 For an engagement that needs *content* rather than a tutor, this is the starting point, and `Gap 533-C` is the note that stars alone would overstate it. |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 🟢 **MIT** (`main/LICENSE`) | **14,372** | *"A framework for building, orchestrating and deploying AI agents and multi-agent workflows."* The successor line to AutoGen and Semantic Kernel. 🔵 Filed on the foundations leg rather than the agent shelf because it is **horizontal** — nothing in it is education-specific — but it is the orchestration layer most of this base's multi-agent patterns (`P549`, `P553`, `P558`) actually need, and it is MIT. |
| [frappe/frappe](https://github.com/frappe/frappe) | 🟢 **MIT** (`master/LICENSE`) | **11,024** | *"Low code web framework for real world applications, in Python and JavaScript."* 🔴 **The licence distinction this base has needed since `p526`:** the **framework** is MIT, while **Frappe Education and Frappe LMS on top of it are GPL-3.0 and AGPL-3.0** respectively (see the licence map below). So the platform is copyleft and the thing underneath it is not — which means a studio can build an education app *on Frappe* without inheriting Frappe Education's grant. 🔵 That is a genuinely different architecture decision from the one the licence map implied while only the apps were filed. |
| [autolab/Autolab](https://github.com/autolab/Autolab) | 🟢 **Apache-2.0** (`master/LICENSE`) | 808 | *"Course management service that enables auto-graded programming assignments."* From **Carnegie Mellon**. 🟢 **The autograder layer, which this base had no row for at all** — and it is permissive, which the rest of the layer is not (see `judge0` below). Ruby on Rails, with language-agnostic grading in containers. 🔵 Pairs directly with `Artemis`/`EduTelligence` as the North American analogue of the same idea; see `P567`. |
| [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | 🟢 **Apache-2.0** (`master/LICENSE`) | 287 | *"Enterprise open source portal built by and for the higher education community."* Java. 🔵 The **student-facing front door** — the layer that aggregates LMS, SIS, calendar and announcements into one authenticated surface. For an engagement where the ask is *"one place where the student sees everything, with an agent in it"*, this is the permissive host, and nothing else on this base occupies that position. |
| [judge0/judge0](https://github.com/judge0/judge0) | 🔴 **GPL-3.0** (`master/LICENSE`) | **4,498** | *"Robust, fast, scalable, and sandboxed open-source online code execution system for humans and AI"* — its own topics include `ai-agent-tools` and `ai-agents`. 942 forks. 🔴 **Copyleft, and filed here anyway because the architecture answer is specific:** GPL-3.0 is **not** AGPL-3.0, so running Judge0 as a **separate self-hosted network service** that a proprietary deliverable calls over HTTP does not pull copyleft onto the deliverable, where `classroomio` (AGPL-3.0) would. 🔵 **Any agent that grades, runs or tests student code needs a sandbox, and this is the field's default one.** Deploy it beside the product, never inside it. |
| [webtech-network/autograder](https://github.com/webtech-network/autograder) | 🟢 **Apache-2.0** (`main/LICENSE`) | 62 | *"Flexible, Consistent and Powerful Autograding Tool that grades and generates feedback."* 🟢 The permissive, small-footprint alternative to the two rows above when the ask is grading *with feedback* rather than a full course-management system. |
| [opensalt/opensalt](https://github.com/opensalt/opensalt) | 🟢 **MIT** — 🔴 **ledger carried `GPL-3.0\|Apache-2.0`; corrected this pass** | 47 | *"Standards Alignment Tool."* Authoring, hosting and aligning academic standards (CASE/CFItem). 🔵 This is the repository that makes *"which standard does this question assess?"* answerable as data rather than as a prompt — the same job `corretor-enem` does for ENEM and `bncc-dev` for the BNCC, generalised. 🟢 **The grant correction matters:** it moved from "copyleft, check carefully" to permissive on one title-block read. |
| [1EdTech/OpenCASE](https://github.com/1EdTech/OpenCASE) | `Apache-2.0` (API) | 11 | *"Implementations of CASE Server and Editor"*, from **1EdTech** itself — the standards body. The reference implementation behind the row above. |
| [Ed-Fi-Alliance-OSS/Data-Management-Service](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | `Apache-2.0` (API) | 12 | *"Code and design documentation for the Ed-Fi API Platform, successor to the Ed-Fi ODS/API."* 🔵 **North America's K-12 data-interoperability layer**, and the successor generation of it — the row to start from when an engagement's first problem is *"the student data is in six systems."* Its sibling [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) (Apache-2.0, 6★) serves a **OneRoster 1.2** API over an Ed-Fi ODS, and [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET) (🟢 **MIT**, `master`) is the .NET client — 🔴 **one of the three addresses the API silently dropped this pass**, see shelf rule 14. |
| [open-edge-platform/education-ai-suite](https://github.com/open-edge-platform/education-ai-suite) | 🟢 **Apache-2.0** (`main/LICENSE`) | 2 | *"The Education AI Suite is a collection of open-source reference applications."* 🔵 **Two stars and worth more than its band suggests**, which is why `Gap 533-C` exists: this is **Intel's** `open-edge-platform`, so it is edge-and-on-premise reference architecture under a permissive grant, pushed **2026-10-29**. For `P565` (the disconnected classroom) and for any EMEA sovereignty engagement, vendor-backed on-prem reference code is scarcer than stars. |

🟡 **Also measured, also unfiled, and deliberately *not* promoted:**
[`tl-its-umich-edu/my-learning-analytics`](https://github.com/tl-its-umich-edu/my-learning-analytics)
(Apache-2.0, 37★, Univ. of Michigan — a learning-analytics dashboard, useful but
not a foundation), [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player)
(MIT, 30★, QTI 3 item player — a renderer, listed under the standards leg
already), and the three `learning-commons-org` repositories
([`knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
164★, [`evaluators`](https://github.com/learning-commons-org/evaluators) 87★),
which return **`NOASSERTION`** and so are **not yet graded** — per shelf rule 8
that means *the title block has not been read*, not that a grant exists. 🔴 They
are the highest-starred ungraded addresses left on the queue and the obvious
first read for `p534`.

## 🆕 `p534` — the institutional AI toolchain, off `Gap 533-A`'s org enumeration

`Gap 533-A` said this base's "is it filed?" test matches on the **address**, so
an institution that ships its platform in one repository and its intelligence in
another reads as *filed* the moment the platform is. 🟢 **Nine orgs already
cited on these pages were enumerated this pass** —
[`../evidence/org-layer-diff.2026-10-29-p534.tsv`](../evidence/org-layer-diff.2026-10-29-p534.tsv)
— and the three rows below are what came back that belongs on *this* page rather
than on the agent shelf. Grants read first-hand from the licence file's title
block, bytes and sha256 recorded in
[`../evidence/grant-reads.2026-10-29-p534.tsv`](../evidence/grant-reads.2026-10-29-p534.tsv).

| Repo | Licence (title block) | Stars | Fitness | Why it is foundational |
|---|---|---|---|---|
| 🆕 [mitodl/agent-kit](https://github.com/mitodl/agent-kit) | 🟢 **BSD-3-Clause** — `BSD 3-Clause License · Copyright (c) 2026, Tobias Macey` (1 499 B, `8afd1cd502a7`, `main` `431fde4`) | 5 | `infrastructure` | **The agent platform a real university's AI team actually runs.** Three `witan` packages — `witan-council` (work coordination), `witan-code` (a code graph for coding agents) and `witan-core` (shared memory) — plus the `agent-config-kit` CLI, reusable skills (`creating-skills`, `dependency-updates`, `deploy-verification`), custom agent definitions for **Claude Code and GitHub Copilot**, MCP install helpers (`witan-council`, `witan-code`, `toolhive-swe`) and six environment profiles. **551 commits**, docs on Read the Docs. 🔵 Education logic lives in [`mitodl/learn-ai`](https://github.com/mitodl/learn-ai); *this* is the plumbing under it, and BSD-3-Clause makes it the most permissively licensed institutional agent toolkit on this base. |
| 🆕 [Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC](https://github.com/Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC) | 🟢 **Apache-2.0** (11 357 B, `c71d239df917`, `main` `d42adc2`) | 🔴 0 | `reference-implementation` | *"Prompts, Skills, Hooks, Agents, etc. for use in the Ed-Fi Alliance software development lifecycle."* 🔵 Its value is **whose** SDLC it is: Ed-Fi governs the data standard that US K-12 student records move on, so this is the standards body publishing how it uses agents on its own codebase — a citable precedent for the governance conversation, which is the part of an education engagement that has no open-source answer anywhere else on this page. 🔴 Zero stars, pushed 2026-09-08. |
| 🆕 [pguso/agents-from-scratch](https://github.com/pguso/agents-from-scratch) | 🟢 **MIT** — `MIT License · Copyright (c) 2025 AI Agents from Scratch Contributors` (1 091 B, `f78cc6bf1d57`, `main` `da3f9df`) | **~1.1k** (page-rounded) · 262 forks | `curriculum` | **Twelve lessons building an agent from a single local LLM call** — text in/out, tools, the agent loop, memory, planning, **evals and telemetry** — with no frameworks, no cloud APIs and no hidden reasoning. Topics include `ai-education` and `open-source-education`. 🔴 **Filed as a `curriculum`, and the distinction is the point:** there is nothing here to deploy for a client. It ramps a studio team, on a local model, without an API budget. 🔴 **It is also the only new address generic web search has produced in seven passes** — and the search snapshot's **796★** against the page's **~1.1k** is a ~38 % disagreement, which is why no star figure on these pages is search-sourced. |

## 🆕 `p534` — a register claim this base has **refuted**, recorded rather than restored

🔴 **`make gate-prose-claims` reports `NO-PERMISSIVE-PLATFORM` as `CLAIM-LOST`**
— *"a declared gap that three patterns choose their base on"* — and asks this
file to carry the sentence **"No permissive education platform exists"**.

🟢 **It is recorded here as RETIRED, not restored, because this base's own
shelves disprove it.** Three permissive full learning platforms are filed on
this page:

| Platform | Grant | Stars |
|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | 7.0k |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 449 |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 1.2k |

plus [sakaiproject/sakai](https://github.com/sakaiproject/sakai) under
**ECL-2.0**, an Apache-2.0 derivative that is permissive in practice.

🔵 **Why this is written down instead of simply dropped.** `p494` established
that a deleted claim is indistinguishable from coverage — so the honest
discharge of a refuted claim is a **dated retraction in the file that owed it**,
naming the evidence that killed it. 🔴 **And the register row should now be
retired**, because a gate that demands a false sentence will eventually be
satisfied by someone re-asserting it. → noted in
[`../intel/open-gaps.md`](../intel/open-gaps.md) under `Gap 534-I`.

## 🆕 `p535` — the efficacy layer: **causal inference**, which this base argued for and never held

🔵 **This section exists because of a contradiction inside this KB, not because of a
search.** [`../intel/trends.md`](../intel/trends.md) Trend 3 has argued since early passes
that *"pedagogy is becoming measurable and almost nobody is measuring it"*, and `p535`
added Trend 21: the **procurement gate is becoming causal evidence**, on a reported
review in which only ~**20 of 800+** K-12 AI studies produced strong causal evidence.
🔴 **Asked what it could hand a buyer who demands an effect estimate, this base held
nothing**: `openfun/ralph` (xAPI event capture) appears in it **157 times**, and
causal-inference libraries appeared **zero** times. Capturing events is not estimating
an effect, and the distinction is the whole of Trend 21.

| Repo | Grant (title block) | Stars | Fitness | What it is for here |
|---|---|---|---|---|
| [`py-why/dowhy`](https://github.com/py-why/dowhy) | 🟢 **MIT** | **8.4k** | `dependency` | Makes the causal **assumptions explicit and testable** — you state the graph (who got the tutor, what else differs between cohorts), and it refutes or survives that statement. This is the part a funder or ministry reviewer actually interrogates. |
| [`py-why/EconML`](https://github.com/py-why/EconML) | 🟢 **MIT** 🔴 *page names no licence; bytes do* | **4.8k** | `dependency` | **Heterogeneous** treatment effects — *who* did it help. In education this is the finding that matters: a null average effect that hides a large gain for the lowest-attaining quartile is a success story the average destroys. |
| [`comet-ml/opik`](https://github.com/comet-ml/opik) | 🟢 **Apache-2.0** | **23.0k** | `infrastructure` | Tracing and automated evaluation for the agent itself, so an effect estimate can be tied to **a known model, prompt and retrieval version**. 🔴 Filed only now: `p534` recorded Opik **by name** inside [`mitodl/learn-ai`](https://github.com/mitodl/learn-ai)'s production stack and never filed the repository. |

🟢 **All three are permissive, and that is the point.** An efficacy claim has to be
auditable by the buyer, which means the client must be able to **run and inspect** the
estimation code — MIT and Apache-2.0 allow that without the copyleft conversation the
rest of this sector forces. 🔵 They sit *beside*, not inside, the LMS: the estimation
runs on exported xAPI records, so the copyleft boundary this file keeps insisting on
(see the licence map below) is not touched.

🔴 **What this layer does not give you.** None of these three makes a weak design strong.
Observational estimation on a cohort that self-selected into using a tutor will produce a
confident, wrong number — which is plausibly how a field accumulates 800 studies and 20
credible ones. The design (assignment, a control arm, a pre-registered outcome) is
`P571`'s subject in [`../compose/patterns.md`](../compose/patterns.md); these libraries
are what you run **once the design is sound**.

## 🆕 `p536` — the institutional data plane, and the instruments that grade it

🔵 **None of these rows came from a search for a repository.** Three came from
enumerating an organisation this base has cited since `p1`, nine came from the
prose-address queue (`Gap 535-E`'s instrument,
[`../ingest/prose-address-ledger.py`](../ingest/prose-address-ledger.py)), and
four came from two topic-qualified API queries that replace the four mandated
global queries `Gap 535-A` retired. Every grant below was read from the licence
payload's **title block** over `raw.githubusercontent.com`, with the ref that
answered recorded —
[`../evidence/grant-title-block.2026-10-29-p536.tsv`](../evidence/grant-title-block.2026-10-29-p536.tsv).

### The Learning Commons stack — three repositories, three different grants

🔴 **Shelf row 3 of [`../agents/top.md`](../agents/top.md) is
`anthropics/k12-teacher-skills`, built *"with Learning Commons"*, and this base
filed none of Learning Commons' own repositories across 535 passes.** The
`agent-skills` third is shelved as an agent; the other two are here, and the
reason they are *here* rather than *there* is that neither is an agent — they are
the **rubric layer** and the **content layer** that an agent is pointed at.

| Repo | Grant (title block) | Stars | Fitness | What it is for here |
|---|---|---|---|---|
| 🆕 [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 🔵 **MIT code; data per-dataset — Open / Open + Gated / Gated.** Title line is *"This page explains the licensing framework…"*, 5 788 B at `main`. **API: `NOASSERTION`** | **164** · 23 forks | `dependency` | *"The data layer for smarter educational AI. Integrate trusted instructional content and research directly into your AI-powered tools."* 🟢 **The thing every tutor on the agent shelf needs and none of them ships**: academic standards, curriculum and instructional materials with provenance. 🔴 **Not vendorable as a corpus** — see the fifth verdict band on [`../agents/top.md`](../agents/top.md); treat it as an external data dependency with a per-row access type, which is `P572`. Pushed 2026-10-28. |
| 🆕 [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🔵 **Code MIT · rubric content CC BY 4.0 · annotated corpora CC BY-NC-SA 4.0.** **API: `NOASSERTION`** | **87** · 17 forks | `dependency` | *"Evaluation for AI outputs against trusted educational rubrics."* 🟢 **This is the instrument Trend 3 has asked for since early passes** — research-backed rubrics a buyer can audit, in TypeScript, with 25 open issues and a push **inside this pass's own window**. 🔴 **The non-commercial half is the useful half for calibration**: annotated **CLEAR Corpus** and **PERSUADE 2.0** are the marked ground truth, and they are `CC BY-NC-SA`. Ship the rubrics, licence the corpora separately, or calibrate against `pedagogy-benchmark` instead. |

🔵 **Read the three grants together and the org's intent is legible**: the
*code* is permissive everywhere, the *rubrics* are permissive with attribution,
and the *marked corpora* are not. That is a rational position for a non-profit
holding licensed instructional content — and it means a studio can build the
pipeline and must negotiate the data.

### The efficacy layer gains its missing half: **assignment**

`p535` filed the estimation libraries (`dowhy`, `EconML`) and said in terms what
they do not give you: *"None of these three makes a weak design strong… The
design (assignment, a control arm, a pre-registered outcome) is `P571`'s
subject."* 🟢 **That component exists, it is Apache-2.0, and it runs inside the
LMS.**

| Repo | Grant (title block) | Stars | Fitness | What it is for here |
|---|---|---|---|---|
| 🆕 [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | 🟢 **Apache-2.0** — `Apache License Version 2.0, January 2004`, 11 323 B at `main`; **API agrees** | **21** · 9 forks | `dependency` | *"Tool for Education Research with RAndomized COnTrolled TriAls"* — an **LTI plug-in** that differentiates assignment content into experimental conditions and **randomises pupils to them inside the LMS they already use**, with informed consent hidden from the teacher, non-consenting participants filtered from summaries and exports, and student identifiers stripped on export. Java, default branch `development`, pushed **2026-10-29**. 🟢 **The randomisation, the consent handling and the de-identification are the three things a studio would otherwise build by hand and get wrong** — and the privacy design is what makes an RCT survive an EU AI Act Art. 10 conversation. 🔴 21★: fitness, not popularity. |
| 🆕 [`bydeng01/ability-levels-audit`](https://github.com/bydeng01/ability-levels-audit) | 🟢 **MIT** — `MIT License · Copyright (c) 2026 Shuyi Fan, Boyuan Deng, Mengyu Xu, Xinh…`, 1 153 B at **`master`**. 🔴 **API said `NOASSERTION`** | 4 | `reference implementation` | *"Code and frozen data for a pre-registered LLM-judge audit, with exploratory analysis of spurious DiD effects from bounded ratings."* **NeurIPS 2026 NewInML Workshop, arXiv:2608.27309.** 🟢 **The methodological warning a studio needs before it believes its own dashboard**: when the outcome is a bounded rating, difference-in-differences manufactures effects that are not there. 🔵 Pre-registered, with frozen data — reproducible in a way almost nothing in this sector is. |
| 🆕 [`bydeng01/conv-vs-ped-tutor`](https://github.com/bydeng01/conv-vs-ped-tutor) | 🟢 **MIT**, 1 149 B at `main`. 🔴 **API said `NOASSERTION`** | 3 | `reference implementation` | *"A pre-registered audit of LLM-judged helpfulness, answer leakage, and student independence across tutor models."* **arXiv:2607.28128**, LangGraph. 🟢 **`answer leakage` and `student independence` are the two failure modes every tutor on the agent shelf can exhibit and none of them measures**, and the repo's topics name `reward-hacking` outright: an LLM judge scoring *helpfulness* rewards the tutor that simply gives the answer. 🔵 Pair it with `evaluators` and `pedagogy-benchmark` and the eval story stops being a single judge's opinion. |
| 🆕 [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna) | 🟡 **MIT — declared in the *manifest*, not the payload.** `DESCRIPTION`: `License: MIT + file LICENSE`; `LICENSE` is **45 B** of template parameters. 🔴 **API said `NOASSERTION`** | 13 | `dependency` | **CRAN** package `tna` **1.3.1**, *Transition Network Analysis*: models learning as **transitions between states over time** (Markov) rather than as a score, which is how you show a tutor changed a learner's *process*. R. 🔴 **The row that produced shelf rule 16** — three of this base's instruments disagree about it and all three are wrong. 🔵 Learning analytics and psychometrics ship in R; this is not the last CRAN grant this base will have to read. |
| 🆕 [`tl-its-umich-edu/my-learning-analytics`](https://github.com/tl-its-umich-edu/my-learning-analytics) | 🟢 **Apache-2.0**, 11 378 B, read at **`master`** (404 on `main`) | **37** · 39 forks | `dependency` | **MyLA** — the University of Michigan's student-facing learning-analytics dashboard, in production, **98 open issues against 39 forks**. 🟢 **More forks than stars, which on this base reads as institutions deploying it.** 🔴 A `main`-only reader grades it ungranted: second `Gap 535-C` instance of the pass. Python. |
| 🆕 [`edulinq/autograder-py`](https://github.com/edulinq/autograder-py) | 🟢 **MIT** — `Copyright (c) 2023 Eriq Augustine`, 1 070 B at `main` | 16 | `dependency` | The Python client for the EduLinq autograder server, **21 forks against 16 stars**, pushed 2026-10-02. 🟢 Completes the autograder layer `p533` opened: the server was filed, the interface students and CI actually call was named in a sentence on [`../intel/market.md`](../intel/market.md) and filed nowhere. |
| 🆕 [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** — `Copyright (c) 2022-2024 Amp-up.io, LLC`, 1 075 B at `main` | 30 | `dependency` | A 100 % JavaScript **QTI 3 item player** — the *delivery* half of the standards stack whose *authoring* half `p533` built an emitter for (`compose/code/p533-qti3-template-emitter/`). 🟢 Named in a sentence on this very file and filed in no table on it. 🟡 Pushed 2025-06-21 — 16 months stale; the standard moves slowly, so read that as settled rather than abandoned, and verify against your QTI version. |
| 🆕 [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli) | 🟢 **Apache-2.0**, 11 340 B at `main`; **API agrees** | **552** · 86 forks | `infrastructure` | SBOM analysis, merging, diffing and format conversion. 🟢 **This is the instrument `Gap 528-C` has been costed against for eight passes** — the gap that says every 🟢 on these pages is a *repository-level* grant and this base has no way to enumerate **dependency** grants. `open-moodle` (MIT repo, AGPL-3.0 PyMuPDF in the artefact) is the standing proof it matters. 🔴 Named on this file and on [`../intel/market.md`](../intel/market.md) and filed in no table row. Pushed 2026-10-19. |

### The national data plane — four countries, four grants, all permissive

🔵 **This is the layer Trend 12 implies and this base has only ever held the
*product* end of.** An education agent that answers a question about a school
system needs that system's own data, and in four countries it is published as a
permissive repository.

| Repo | Grant (title block) | Stars | Region | What it is for here |
|---|---|---|---|---|
| 🆕 [`nso-india/esankhyiki-mcp`](https://github.com/nso-india/esankhyiki-mcp) | 🟢 **MIT** — `Copyright (c) 2026 Ministry of Statistics and Prog…`, 1 115 B at `main` | **147** · 28 forks | 🟢 **APAC (India)** — *stated in the copyright line*: the **Ministry of Statistics and Programme Implementation** | An **official government MCP server** over the eSankhyiki national statistics platform, pushed 2026-10-27. 🟢 **The first row on this base where a national statistical office ships the MCP itself** — not a third party scraping it. 🔵 For an engagement that must ground claims about enrolment, attainment or expenditure in the government's own figures, this is the shape to ask every ministry for, and the precedent to cite when asking. |
| 🆕 [`hantang/smartedu-dl-go`](https://github.com/hantang/smartedu-dl-go) | 🟢 **MIT** — `Copyright (c) 2024 hantang`, 1 063 B at `main` | **207** · 45 forks | 🟢 **APAC (China)** — *stated by the product* | Multi-platform downloader for the **国家中小学智慧教育平台** (national K-12 smart-education platform): textbooks as PDF, courseware, audio and video. Go. 🟢 **The largest-starred national-curriculum *ingest* tool on this base** — and the ingest step is the one `P560` and `lineage-skill` both assume someone else solved. 🟡 It is an access tool, not a licence: what it downloads carries the platform's own terms, which this base has **not** read and does not claim. |
| 🆕 [`cortega26/chile-hub`](https://github.com/cortega26/chile-hub) | 🟢 **MIT** — `Copyright (c) 2026 Carlos Ortega`, 1 069 B at `main` | **136** · 12 forks | 🟢 **LATAM (Chile)** — *stated by the product* | *"Datos públicos de Chile curados, normalizados y validados: geografía…"* — curated, normalised, validated Chilean public data, pushed 2026-10-26. 🟢 Pairs with the Colombian agent [`startin-lab/brujula-educativa`](https://github.com/startin-lab/brujula-educativa) (agent shelf) as the data half of the same pattern, and with the Chilean exam data already behind `pedagogy-benchmark`. |
| 🆕 [`openeduhub/edu-sharing-python-client`](https://github.com/openeduhub/edu-sharing-python-client) | 🟢 **Apache-2.0**, 11 348 B at `main` | 🔴 0 | 🟢 **EMEA (Germany)** — Open Edu Hub | Python client and connectors for the **edu-sharing** API — the OER repository layer German states run (WirLernenOnline). 🟢 Zero stars and the only permissive client for a national OER infrastructure on this base. 🔵 Filed on the attachment point, per `Gap 534-C`: a star gate cannot see a public-sector integration layer. |
| 🆕 [`openfun/arnold`](https://github.com/openfun/arnold) | 🟢 **MIT** — `Copyright (c) 2018-present GIP FUN MOOC`, 1 077 B, read at **`master`** | 41 · 10 forks | 🟢 **EMEA (France)** — *stated*: **GIP FUN MOOC**, France Université Numérique | Kubernetes deployment tooling for the FUN MOOC stack, pushed 2026-10-28. 🟢 Completes the `openfun` family already here (`ralph` LRS, `richie` CMS): CMS, learning-record store **and** the deployment that runs them, all MIT, all from the French national MOOC operator. 🔴 Third `Gap 535-C` instance of the pass. |
| 🆕 [`Turkish-AI-Community/hsd-agu-egitim`](https://github.com/Turkish-AI-Community/hsd-agu-egitim) | 🟢 **MIT** — `Copyright (c) 2026 Enes Fehmi Manan`, 1 072 B at `main` | 33 | 🟡 **EMEA (Türkiye)** — *inferred* from the org name and Turkish-language material | *"From Model to Agent"* mini-bootcamp project and teaching documents, Abdullah Gül University. 🟢 **Filed as a curriculum, explicitly not as an education-sector product** — the same honest classification `p534` gave `pguso/agents-from-scratch`. 🔵 It is the only Türkiye-origin address on this base, which is itself the finding: EMEA on these pages has meant Western Europe plus Morocco. |
| 🆕 [`RozhakDev/EduPintarIPAS`](https://github.com/RozhakDev/EduPintarIPAS) | 🟢 **MIT** — `The MIT License (MIT) · Copyright (c) 2025 Rozhak`, 1 092 B at `main` | 20 | 🟢 **APAC (Indonesia)** — *stated by the product* | Web chatbot for **IPAS** (integrated science) for Indonesian primary pupils. 🟡 Pushed 2025-08-10 — 14 months stale. 🔵 Filed beside `naufaldi/teacher-exam` (agent shelf, Indonesia): two Indonesian artefacts, one teacher-facing and one pupil-facing, both MIT, both naming the national curriculum by its own acronym — which is the texture Trend 12 predicts and a global query never returns. |

🔴 **Four rows this pass are copyleft or network-copyleft and are recorded here
rather than filed as buildable**, because an unstated exclusion looks like an
oversight: [`Schlaflied/Plot-Ark`](https://github.com/Schlaflied/Plot-Ark)
(**AGPL-3.0**, 13★ — curriculum operations over xAPI and Moodle, the closest
thing to `P558`'s output anyone has shipped),
[`brownplt/LTLTutor`](https://github.com/brownplt/LTLTutor) (**GPL-3.0**, 12★ —
Brown PLT, a *misconception*-based tutor, which is a sharper pedagogy than any
permissive row here), [`avps82/mentar`](https://github.com/avps82/mentar)
(**AGPL-3.0**, 0★ — local-first child tutor, *"no cloud, no accounts, no child
data leaving the device"*) and `openedx/openedx-ai-extensions` (AGPL-3.0,
carried from `p534`). 🔵 **All four are usable behind a service boundary and none
is vendorable into a proprietary deliverable** — Trend 14's point, four more
times, and note that **three of the four are 2026 projects**: the sector's
copyleft is a present-tense choice, not a legacy.

## Licence map, for the architecture decision

| Band | Repos |
|---|---|
| **Permissive — fork freely** | 🆕 **freeCodeCamp (BSD-3-Clause, 458k★)**, 🆕 **frappe/frappe (MIT)**, 🆕 **microsoft/agent-framework (MIT)**, 🆕 **Artemis + EduTelligence (MIT, TU München)**, 🆕 **Autolab (Apache-2.0, CMU)**, 🆕 **uPortal (Apache-2.0)**, 🆕 **webtech-network/autograder (Apache-2.0)**, 🆕 **opensalt (MIT)**, Oppia (Apache-2.0), OpenOLAT (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT), Dolos (MIT), Ralph (MIT), FSRS (MIT), 🆕 **ten of the eleven Moodle MCP codebases (MIT)** — G36maid, moodler-mcp, Faixiang, leshamblin, falkenslab, Jawadh-Salih, open-moodle*, moodle-student-mcp, duck-5 |
| **Weak copyleft — link across a boundary** | BigBlueButton (LGPL-3.0), OpenEduCat (LGPL-3.0) |
| **Strong copyleft — integrate, do not fork** | Moodle, Chamilo, ILIAS, H5P (GPL-3.0); 🔵 **Frappe Education (GPL-3.0)** — 🆕 but **`frappe/frappe`, the framework underneath it, is MIT**, so the copyleft is in the app, not the platform; i-educar, RosarioSIS, TAO (GPL-2.0); 🆕 **Judge0 (GPL-3.0)** — 🟢 **deploy it as a separate network service and the copyleft does not reach your deliverable**, because GPL-3.0 has no §13 |
| **Network copyleft — integrate, do not fork, and read §13** | Open edX, Canvas, Frappe LMS, Tutor, csmediapro/moodle-mcp-server (AGPL-3.0); **PyMuPDF (AGPL-3.0)** — reached *transitively* by the MIT-licensed `sonstellar969/open-moodle`; 🆕 **classroomio/classroomio (AGPL-3.0, 1,735★)** — the contrast that makes the Judge0 row's distinction concrete |

🔴 \* **`open-moodle` is MIT and still lands in the network-copyleft row in
practice**, because it links AGPL-3.0 PyMuPDF for PDF extraction. 🔵 **The rule:
the grant you ship is the union of the grants you link** — a repo-level licence
probe cannot see this, and this is the first instance of it recorded on the
platform legs.

AGPL-3.0 §13 reaches users interacting over a network, which is precisely the
hosted-SaaS shape most engagements want. **The integration seams — LTI 1.3, xAPI
via Ralph, H5P content, Canvas/Moodle REST, MCP servers — are where permissive
code belongs.**

## Searched and not found

- **No mainstream Apache/MIT-licensed LMS** beyond Oppia and OpenOLAT. Searched
  explicitly again; the sector is copyleft and that is the finding.
- **No permissively licensed SIS.** Every student-information system found is
  GPL-2.0 or GPL-3.0 — and `frappe/education`, the one genuinely unresolved cell
  on this file, resolved to **GPL-3.0** this pass rather than to something
  permissive. The AI-native advising option
  ([canyongbs/advisingapp](https://github.com/canyongbs/advisingapp)) is
  Elastic-2.0 and unusable as a hosted base.
- 🔴 **No credible Moodle MCP server — but not for lack of attempts.** See the
  census above: **eleven independent codebases, ten of them MIT, 37 stars
  between them, a 27★ ceiling** on the sector's biggest LMS. 🔵 Corrected from
  `p527`, which read the same field as *"roughly three real codebases."*
- 🆕 🔴 **No shared tool vocabulary for Moodle.** Eight tools in one server, ~230
  in another, and no two naming the same operations the same way. This is the
  actual missing artefact, and it is a specification rather than a product.
- **No APAC-origin platform core surfaced on the platform legs this pass.** APAC's
  open-source strength in education is on the *agent* legs (DeepTutor, OpenMAIC,
  lineage-skill, Educhain) — see [`../agents/top.md`](../agents/top.md). Moodle's
  Perth origin is historical and its governance is now global.
- **No LATAM-origin platform beyond i-educar and RosarioSIS's localisation.**

## 🆕 Gulf-origin supply — `Gap 536-D` answered, and the hole is a **grant** hole (`p537`)

`Gap 536-D` registered this base's largest adoption-to-supply gap: `p535` measured the
**UAE at ~75 % of teachers using AI in their work** — the highest figure in the whole
TALIS set this base holds — against **zero Gulf-origin repositories** in any curated
table. The gap prescribed `org:` and region-qualified search against named Gulf
institutions (KAUST, KFUPM, Khalifa, NYU Abu Dhabi, MBZUAI). 🟢 **It was run, it
returned supply, and the supply inverts the gap's premise.**

🔴 **The Gulf is not short of published education repositories. It is short of
ones a studio may build a product on.** Every grant below was read first-hand at the
resolved default branch.

| Address | Stars | Licence — read first-hand | Origin | Pushed | What it is |
|---|---|---|---|---|---|
| [`KAUST-Academy/Artificial-Intelligence-Courses`](https://github.com/KAUST-Academy/Artificial-Intelligence-Courses) | **443** · 88 forks | 🔴 **GPL-3.0** — `GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007`, **35 128 B** at `main` | 🟢 **EMEA (Saudi Arabia — KAUST Academy)** | 2026-10-22 | **The largest Gulf-origin education asset this base has found.** Jupyter-notebook AI curriculum, ~3.2 GB of tree. Taught with King Khalid University; the org's teaching line, not a research dump. 🔴 **GPL-3.0 on courseware is the hard case**: the grant binds derivative *teaching materials*, so a client-branded fork of this curriculum is a GPL-3.0 distribution |
| [`KAUST-Academy/2025_Artificial-Intelligence-Summer`](https://github.com/KAUST-Academy/2025_Artificial-Intelligence-Summer) | **279** | 🔴 **GPL-3.0** — 35 128 B at `main` | 🟢 **EMEA (Saudi Arabia)** | 2025-09-10 | The 2025 summer-school edition. Same grant, no longer maintained |
| [`KAUST-Academy/2026_Introduction_To_AI`](https://github.com/KAUST-Academy/2026_Introduction_To_AI) | **80** | 🔴 **GPL-3.0** — 35 128 B at `main` | 🟢 **EMEA (Saudi Arabia)** | 2026-01-16 | Current-year introductory track |
| [`KAUST-Academy/2026_Advanced_AI`](https://github.com/KAUST-Academy/2026_Advanced_AI) | **57** | 🔴 **GPL-3.0** — 35 128 B at `main` | 🟢 **EMEA (Saudi Arabia)** | 2026-02-07 | Current-year advanced track |
| [`KAUST-Academy/2026_KASP_Summer_School`](https://github.com/KAUST-Academy/2026_KASP_Summer_School) | 24 | ⛔ **No grant at 21 probed paths** on the resolved default branch | 🟢 **EMEA (Saudi Arabia)** | 2026-08-20 | Live, current, and **unusable** — absence of a grant is not permission |
| [`KAUST-Academy/weekly-ai-brief`](https://github.com/KAUST-Academy/weekly-ai-brief) | 18 | ⛔ **No grant at 21 probed paths** | 🟢 **EMEA (Saudi Arabia)** | 2026-10-27 | An automated weekly AI report, mailed on a schedule. 🔵 Interesting as a *pattern* (an institution running agentic content ops), unusable as a *dependency* |
| [`KAUST-Academy/2025_Advanced-Ai`](https://github.com/KAUST-Academy/2025_Advanced-Ai) | 47 | ⛔ **No grant at 21 probed paths** | 🟢 **EMEA (Saudi Arabia)** | 2025-03-13 | Prior-year advanced track, ungranted |
| [`mbzuai-oryx/groundingLMM`](https://github.com/mbzuai-oryx/groundingLMM) | **969** | 🟢 **Apache-2.0** — 11 356 B at `main` | 🟢 **EMEA (UAE — MBZUAI, Oryx lab)** | 2026-09-05 | **The one permissive Gulf asset of real size here.** GLaMM, a grounded large multimodal model (CVPR 2024). Not education-built — it is the *capability* layer a diagram-grading or worked-example tutor would sit on |
| [`mbzuai-oryx/OpenEarthAgent`](https://github.com/mbzuai-oryx/OpenEarthAgent) | **131** | ⛔ **No grant at 21 probed paths** | 🟢 **EMEA (UAE — MBZUAI)** | 2026-10-26 | ECCV 2026 tool-augmented geospatial agent framework. Pushed three days before this read and still ungranted |

🔴 **The measured shape, and it is the finding `536-D` was really asking for.**
Across the two leading Gulf AI institutions' public output, education-relevant supply is
**courseware under GPL-3.0** or **research code under no grant at all**. Of the nine rows
above, **one** (`groundingLMM`) carries a permissive grant, and it is not an education
project. 🔵 **So the Gulf engagement does not look like the LATAM or EMEA ones on
these pages.** There is no permissive vertical platform to fork and no MIT agent to
compose. What exists is:

1. **Curriculum under copyleft** — integrate and attribute, or license separately from
   the institution; do not fork into a client-branded product. This is the `Moodle` posture
   applied to *content* rather than code, and `Trend 41`'s adapter inversion applied to
   a syllabus.
2. **A capability model under Apache-2.0** — `groundingLMM` is buildable, and it is the
   only thing here that is.
3. **A grant-hygiene gap wide enough to be a service line.** Four of nine Gulf
   repositories, including two pushed within the last ten weeks, serve no licence at any
   probed path. 🟢 An institution that wants its work adopted and has not noticed
   this is a conversation, not a blocker.

🔵 **Declared gap, stated rather than left silent.** `Khalifa University`,
`KFUPM` and `NYU Abu Dhabi` were in `536-D`'s named list and returned **no
education-relevant repository** through the channels run here. A separate full-text leg
for Arabic-language education tooling returned **noise only** — twenty hits, of which the
single Arabic-specific one,
[`h9-tec/Awesome_Arabic_NLP`](https://github.com/h9-tec/Awesome_Arabic_NLP) (**258★**),
is a link list serving **no grant at 21 probed paths**, and is not Gulf-origin. 🔴
**There is no Arabic-language intelligent-tutoring repository on this base and this pass
did not find one.** That is an informed gap, not coverage.

## 🆕 Nine platform rows promoted off the prose queue — and two are archived upstream (`p537`)

Every row below was named in a *sentence* on a curated page and filed in **no** table
row on any of them. Grants read first-hand at the resolved default branch; stars, forks
and the **archived** flag from the repository-search channel.

| Address | Stars | Licence — read first-hand | Upstream state | What it is |
|---|---|---|---|---|
| [`jupyterhub/jupyterhub-tutorial`](https://github.com/jupyterhub/jupyterhub-tutorial) | **202** · 56 forks | 🟢 **BSD-3-Clause** — `BSD 3-Clause License · Copyright (c) 2017, Project Jupyter Contributors`, 1 527 B at **`master`** | 🔴 **ARCHIVED, read-only** | Deployment tutorial for JupyterHub. 🔴 **Do not start here in 2026** — it is filed so the next pass stops re-finding it, and the archived flag is the row's point |
| [`jupyterhub/yarnspawner`](https://github.com/jupyterhub/yarnspawner) | 19 · 14 forks | 🟢 **BSD-3-Clause** — `Copyright (c) 2018, Jim Crist`, 1 491 B at **`master`** | 🔴 **ARCHIVED, read-only** | Spawns single-user notebook servers into Hadoop/YARN containers. Dead, and only relevant to an on-prem Hadoop estate |
| [`jupyterhub/kerberosauthenticator`](https://github.com/jupyterhub/kerberosauthenticator) | 12 · 8 forks | 🟢 **BSD-3-Clause** — `Copyright (c) 2019, Jim Crist`, 1 491 B at `main` | 🟢 Live (pushed 2026-08-01) | Kerberos auth for JupyterHub. 🔵 **The row that earns its place in this trio**: Kerberos is what a university IT department actually runs, and this is the supported bridge to it |
| [`classroom-resources/autograding-python-grader`](https://github.com/classroom-resources/autograding-python-grader) | 11 · 14 forks | 🟢 **MIT** — `Copyright (c) 2023 GitHub`, 1 062 B at `main` | 🟢 Live | GitHub Classroom's Python autograder action. 🟢 **North America origin (GitHub), and vendor-maintained** — the cheapest credible grading substrate for a CS course, with no model call in it at all |
| [`classroom-resources/autograding-io-grader`](https://github.com/classroom-resources/autograding-io-grader) | 7 · 8 forks | 🟢 **MIT** — `Copyright (c) 2023 GitHub`, 1 062 B at `main` | 🟢 Live | Its stdin/stdout sibling: language-agnostic I/O grading |
| [`Ed-Fi-Alliance-OSS/Ed-Fi-AdminApp`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-AdminApp) | 🔴 **0** · 5 forks | 🟢 **Apache-2.0** — 11 356 B at `main` | 🟢 Live (pushed 2026-10-28) | Administrator UI for Ed-Fi Technology Suite deployments. 🟢 **North America (Ed-Fi Alliance)** — zero stars and actively developed on the same day it was read, which is what vendor-internal tooling looks like. Completes the Ed-Fi row set beside `Fiona` on the agent shelf |
| [`brownplt/LTLTutor`](https://github.com/brownplt/LTLTutor) | 12 | 🔴 **GPL-3.0** — `GNU GENERAL PUBLIC LICENSE Version 3`, **35 148 B** at `LICENSE.txt`, `main` | 🟢 Live (2026-07-28) | Misconception-based tutor for Linear Temporal Logic, from Brown University's PLT group. 🔵 **The research-grade exemplar of the only tutoring design this base rates**: it models *specific wrong beliefs*, not a generic mastery score. 🔴 GPL-3.0 — integrate, do not fork |
| [`Schlaflied/Plot-Ark`](https://github.com/Schlaflied/Plot-Ark) | 13 | 🔴 **AGPL-3.0** — `GNU AFFERO GENERAL PUBLIC LICENSE Version 3`, 34 522 B at **`master`** | 🟢 Live (2026-09-12) | *"Evidence-driven curriculum operations: turn learning signals into reviewable course changes, then track outcomes over time with knowledge graphs and long-term memory."* Moodle + xAPI + LightRAG + human-in-the-loop. 🔴 **AGPL-3.0 §13 — a hosted SaaS built on this owes source to its users** |
| [`avps82/mentar`](https://github.com/avps82/mentar) | 🔴 **0** | 🔴 **AGPL-3.0** — 34 522 B at `main` | 🟢 Live (2026-10-01) | *"OSS-first, local-first AI tutor for children — supplements school, never replaces it. No cloud, no accounts, no child data leaving the device."* Ollama / llama.cpp, Bayesian knowledge tracing. 🔵 **The child-data posture is the asset**, and it is the one an EU AI Act deployer or a COPPA-exposed district can actually defend. 🔴 Zero stars; AGPL-3.0 rules out a hosted product |

🔵 **The pattern across all nine, and it is why this section is not padding:** the
queue's residue is not junk — seven of nine are live and six carry a grant this base can
act on — but **two of nine were archived upstream and no instrument here would have said
so**. A promotion queue without an `archived` column promotes dead projects as
foundations. `Gap 537-A`.


## 🆕 Nine platform rows — the prose queue emptied, and placed in all four regions (`p538`)

`p537` left **twenty** addresses in the promotion queue. `p538` read every one
first-hand and filed the non-agent half here; the seven agent-grade ones went to
[`../agents/top.md`](../agents/top.md). 🔵 **Read the region column before the
star column.** This base's standing complaint is that its supply is APAC-heavy
and LATAM-thin, and this residue is the first promotion set that places rows in
**all four regions** — because a queue built from sentences inherits whatever
the sentences were about, and this base writes about every region.

⚠️ **Grants here are read from the repository page's own sidebar and title
block**, not from a licence-file probe: `curl` and the GitHub API are both
refused for this session, so the channel is the rendered page. A row marked
*"README only"* means the sidebar carried **no** licence entry.

| Address | Stars | Licence — read first-hand | Region (basis) | What it is |
|---|---|---|---|---|
| [`alterem/knowledge-grab`](https://github.com/alterem/knowledge-grab) | 🟢 **567** · 52 forks | 🟢 **MIT** — sidebar `MIT license` | APAC (China — Chinese-language description, targets a PRC national platform) | 🟢 **The highest-starred row this queue has produced, and it is a *data acquisition* tool, not an agent.** A Tauri + Vue 3 desktop app that downloads from 国家中小学智慧教育平台 (`basic.smartedu.cn`), the PRC's national K-12 resource platform: e-textbooks, course video and courseware, with video decryption and ffmpeg merge to MP4. 🔵 **Why it is load-bearing:** every tutoring agent needs a grounded corpus, and this is the only tool on this base that acquires a *national curriculum* corpus at scale. Pair it with a RAG stack and the curriculum-grounding pattern stops being hypothetical. ⚠️ Downloading from a state platform has terms this base has **not** read — the licence covers the *tool*, not the content. |
| [`h9-tec/Awesome_Arabic_NLP`](https://github.com/h9-tec/Awesome_Arabic_NLP) | **258** · 42 forks | 🟡 **CC BY 4.0 — README badge only.** The sidebar carries **no licence entry**; the grant is a badge reading `License: CC BY 4.0`. 🔵 **Fourth verdict band** — granted, but not under a code licence | 🟢 **EMEA (Gulf / Arabic-speaking)** — subject matter | *"The most comprehensive, up-to-date collection of Arabic NLP resources on the internet"* — models, datasets, tools, research and companies, with a dedicated **🎓 Tutorials & Learning Resources** section. 🟢 **The index `Gap 536-D` implied and the Gulf set did not supply.** `p537` found Gulf *code* to be copyleft or ungranted; this is the region's **map**, and at 258★ it is the most-used Arabic-NLP entry point in the open. 🔵 A content grant is right for an index and wrong for a dependency: cite it, do not vendor it. |
| [`oas114/EduShield`](https://github.com/oas114/EduShield) | 11 · 2 forks | 🟢 **MIT** — sidebar `MIT license` | APAC (Taiwan — Traditional-Chinese description) | 教育隱私保護系統 — *"Zero-Trust Data Anonymization Shield for AI."* De-identifies student text **before** it reaches a model and re-identifies the output after, as **a single static HTML file with no backend**, with an optional local-LLM scan via Ollama. 🟢 **The architecture is the finding.** Every data-protection pattern on this base assumes a service to deploy and an institution to run it; this one assumes neither, which is exactly the posture a school with no IT department can adopt. 🔵 **Composes with anything** — it sits in front of a model, so it is licence- and vendor-neutral. |
| [`dougpenny/SwiftyPSCore`](https://github.com/dougpenny/SwiftyPSCore) | 6 · 0 forks | 🟢 **MIT** — sidebar `MIT license` | 🟢 **North America** (PowerSchool is the dominant US K-12 SIS) | *"Swift interface for the PowerSchool API"* — a pure-Swift client handling authentication and response decoding against the PowerSchool SIS API. 🟢 **The first permissively granted SIS access layer on this base**, against a gap that has read *"no open-source SIS/advising agent under a permissive licence"* for many passes. 🔴 **It is a client, not an agent**, so it narrows that gap without closing it — the only full candidate (`advisingapp`) is still Elastic-2.0. ⚠️ README states it *"is not endorsed, sponsored, or affilitated with PowerSchool in any way"* (sic). Swift is also a constraint: an agent runtime in Python or TypeScript cannot link it directly. |
| [`shishiv/EDUCA`](https://github.com/shishiv/EDUCA) | 🔴 **1** · 0 forks | 🟢 **MIT** — sidebar `MIT license` | 🟢 **LATAM (Brazil)** — Portuguese-language README, targets *secretarias de educação* | *"A planilha da secretaria de educação não aguenta mais. O EDUCA aguenta"* — "the spreadsheet your school district runs on doesn't scale; EDUCA does." Schools, students, guardians, classes, enrolment and attendance in one place, with district-staff dashboards. TypeScript / Next.js. 🔵 **It names the actual LATAM baseline, which is a spreadsheet** — and that framing is more useful to an engagement than the code is. ⚠️ README states it is a **synthetic-data-only pilot foundation, not approved for real student data or production**. A reference implementation. |
| [`guruduan/SIMG`](https://github.com/guruduan/SIMG) | 🔴 **1** · 0 forks | 🟢 **MIT** — sidebar `MIT license` | APAC (Indonesia — Indonesian-language description) | A **Moodle plugin** (PHP 8.2) for school administration: teaching journals, homeroom-teacher journals, student leave letters, attendance recaps, counselling (BK) services and extracurriculars, with WhatsApp notifications through the Wablas API. 🟢 **Evidence for a claim this base makes and rarely substantiates: that Moodle's value is its plugin ecosystem.** This is a *national administrative practice* — BK counselling, Indonesian leave letters — encoded as a Moodle plugin under MIT. 🔵 **WhatsApp as the notification channel is the regional lesson**, not an implementation detail. |
| [`mizcausevic-dev/state-ai-disclosure-state-tracker`](https://github.com/mizcausevic-dev/state-ai-disclosure-state-tracker) | 🔴 **0** · 0 forks | 🟢 **MIT** — sidebar `MIT license`, README agrees | 🟢 **North America** (US state statutes) | *"Hash-chained per-state lifecycle record + reference verifier for EdTech AI products."* A v0.1 draft schema for an append-only per-state status record, plus a verifier. Names **Illinois SOPPA**, **California AB 1584** and **AB 2876**, **Texas HB 18** and **NY Ed Law 2-d**. ⚠️ Its own words: *"EdTech-readiness scaffolding, not certification."* The worked example covers **three** states. |
| [`mizcausevic-dev/pii-student-vault-contract-profile`](https://github.com/mizcausevic-dev/pii-student-vault-contract-profile) | 🔴 **1** · 0 forks | 🟢 **MIT** — sidebar `MIT license`, README agrees | 🟢 **North America** (FERPA / COPPA) | An EdTech profile of an *AI Procurement Decision Card* vault contract: maps **FERPA's 7 PII categories** and **COPPA's 10 PI categories** to vault targets, each with default retention and redaction rules and a **four-doctrine consent taxonomy**. Ships a `profile.json` and one example deployment. ⚠️ Same disclaimer — scaffolding, not compliance. |
| [`mizcausevic-dev/student-data-access-audit-stream`](https://github.com/mizcausevic-dev/student-data-access-audit-stream) | 🔴 **0** · 0 forks | 🟢 **MIT** — sidebar `MIT license` | 🟢 **North America** (FERPA §99.32) | *"Hash-chained event schema + reference verifier for AI tool reads of student records"* — a tamper-evident log of which tool read which record, when, under what legal basis and under which authorising Decision Card. A small Node verifier checks the hash chain and enforces tokenised student IDs and **FERPA §99.32** logging consistency. |

🟢 **The three `mizcausevic-dev` repositories are one asset, and this base has
nothing else like it.** Every US-regulation finding on
[`../intel/market.md`](../intel/market.md) — 134 bills across 31 states, the
amended COPPA rule's 22 Apr 2026 compliance date, Ohio's 1 Jul 2026 deadline —
is **demand-side intelligence with no supply-side answer**. These three are the
answer's shape: a per-state status record, a PII-category vault contract, and an
access audit stream, all MIT, all hash-chained, all composing into one
compliance spine. 🔴 **And all three are 0–1★ v0.1 drafts by a single author
with no adoption whatsoever.** 🔵 **So the correct use is as a specification,
not a dependency** — the FERPA-7 / COPPA-10 category mapping and the
§99.32 logging rule are the reusable parts, and they are the parts an engagement
would otherwise derive from statute by hand. Recipe in
[`../compose/patterns.md`](../compose/patterns.md).

🔵 **The pattern across all nine, and it is the one `p537` asked for.** `p537`
closed on `Gap 537-A`: a promotion queue with no `archived` column promotes dead
projects. 🟢 **None of these nine is archived** — every page rendered live. But
the sharper observation is about *region*: these nine place **3 in North
America, 3 in APAC, 1 in EMEA, 1 in LATAM** with one global index, against a
base whose supply has been APAC-dominated for its whole history. 🔵 **A queue
built from sentences inherits the regional spread of the prose, and this base's
prose is more balanced than its tables are.** That is a cheaper way to fix a
regional gap than another regional search leg — which this pass ran, four times,
and which returned nothing unfiled.
