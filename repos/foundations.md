---
industry: education
region: Global
updated: 2026-10-20
---

## Pass 346 · 2026-10-20 — six foundational benches promoted from the institutional orphan filter, two of them government-run and live today, and the one row carrying submodules is granted on three different channels at three different pins

**Evidence:** [`p346-institutional-orphan-probe`](../evidence/p346-institutional-orphan-probe.2026-10-20-p346.tsv) · [`p346-coursemology-pin-grant-boundary`](../evidence/p346-coursemology-pin-grant-boundary.2026-10-20-p346.tsv) · [`p346-address-identity-head-equality`](../evidence/p346-address-identity-head-equality.2026-10-20-p346.tsv) · [`p346-ladder-spelling-and-ref-axes`](../evidence/p346-ladder-spelling-and-ref-axes.2026-10-20-p346.tsv).

🔴 **`make hooks` did not run this pass** — the session's tool policy refused to execute this repository's instruments, so p345's two red gates are unjudged rather than cleared. The reporting obligation and the two findings are stated in full on [`agents/top.md`](../agents/top.md); this shelf satisfies `gate-pin-grant`'s contract by construction, below.

### 🟢 Six foundational rows, every grant read at the pin and every region DST-tested

🔵 All six come from this base's own **528-address permissive orphan list**, selected on *institutional ownership* rather than p345's language filter (`ACTION ZZ-i`, generalised on [`agents/top.md`](../agents/top.md)). 🔵 Star figures are the GitHub MCP **search channel's**, not a read.

| Repo | Grant, read at the pin | ★ | Bench (commit channel) | Placed, and how | Why it is a FOUNDATION |
|---|---|---|---|---|---|
| [`Coursemology/coursemology2`](https://github.com/Coursemology/coursemology2) | 🟢 **MIT, 1 118 B** — superproject only; **two submodules, boundary named below** | 158 | 🟢 **15 821 c · 86 a · 2014-07-23 → 2026-10-11** | 🟢 **APAC — Singapore** — `+0800(13022)` with **3 628 December–February commits also at `+0800`**; Singapore has no DST, so the non-shifting offset is the expected shape | **Twelve years and 86 authors of coursework-platform code**: assessments, autograded programming questions, submission workflow. The deepest APAC education bench on these shelves |
| [`learningequality/studio`](https://github.com/learningequality/studio) | 🟢 **MIT, 1 114 B** — default ref is **`unstable`** | 212 | 🟢 **15 505 c · 2015-05-06 → 2026-10-20 (pushed today)** | 🟡 **authorship North America — United States** (`-0700(8423)/-0800(3085)`, PST/PDT confirmed); **subject Global** — per `ACTION ZZ-b` only the authorship enters the placed cell | The authoring and curation half of **Kolibri**, which this base already shelves. Content pipelines for low-connectivity deployments — the offline-first channel no cloud LMS covers |
| [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 **MIT, 1 082 B**, stock | 382 | 🟢 **1 638 c · 2019-12-20 → 2026-09-15** | 🟢 **North America — United States** — `-0500(878)/-0400(723)` with 718 winter commits at `-0500`, a confirmed EST/EDT shift | A **distributed LMS that automates computing-science courses**, built and run at NYU: per-student containerised cloud IDEs plus an autograder. The highest-star row in this pass's probe |
| [`DFE-Digital/education-benchmarking-and-insights`](https://github.com/DFE-Digital/education-benchmarking-and-insights) | 🟢 **MIT, 1 090 B**, stock | 4 | 🟢 **5 266 c · 35 a · 2023-11-08 → 2026-10-20 (pushed today)** | 🟢 **EMEA — United Kingdom** — `+0100(3016)/+0000(2246)` with **1 381 winter commits at `+0000`**, a confirmed GMT/BST shift; the second-modal author domain read before the channel was refused was **`education.gov.uk`(1 607)** | 🔴 **4 stars, and it is a national government department's live school-benchmarking service.** `ACTION ZZ-c` exactly: the log is the bench, not the stars |
| [`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet) | 🟢 **MIT, 1 091 B**, stock | 89 | 🟢 **1 309 c · 2021-07-08 → 2026-06-09** | 🟢 **North America — United States**, multi-zone (`-0700/-0600/-0400`, winter `-0500`) | A cross-platform **verifiable-credential wallet for learners**, originally MIT's Digital Credentials Consortium work and now an **OpenWallet Foundation (Linux Foundation) lab** — see the governance note below |
| [`openedx/tutor-contrib-aspects`](https://github.com/openedx/tutor-contrib-aspects) | 🟢 **Apache-2.0, 11 356 B**, stock | 15 | 🟢 **2 298 c · 2023-02-07 → 2026-10-20 (pushed today)** | 🟢 **North America — United States with EMEA contribution** — `-0500(1034)/-0400(908)` plus `+0000(267)` | **Open Analytics Reference System**: the learning-analytics layer for Open edX, delivered as a Tutor plug-in. Open edX and `overhangio/tutor` are both already shelved — this completes the triple |

### 🟢 `gate-pin-grant`'s contract, met in full on the one row that triggers it

🔴 p345's `gate-pin-grant` is red on p344's text for citing submodule-bearing addresses **without naming the boundary**. 🟢 **`coursemology2` carries `.gitmodules` (HTTP 200 at the pin), so this row names it — three layers, three pins, and three different channels** ([`p346-coursemology-pin-grant-boundary`](../evidence/p346-coursemology-pin-grant-boundary.2026-10-20-p346.tsv)):

| Layer | Address | Pin actually read | Grant | Channel |
|---|---|---|---|---|
| superproject | `Coursemology/coursemology2` | `6310c97` | 🟢 **MIT, 1 118 B** | `LICENSE` file |
| submodule `authentication/singular-keycloak-database-federation` | `Coursemology/singular-keycloak-database-federation` | `734e8ed` | 🟡 **Apache-2.0, 11 356 B** | `LICENSE` file |
| submodule `client/vendor/recorderjs` | `mattdiamond/Recorderjs` | `08e7abd` | 🟡 **MIT — README channel only** | 🔴 **no licence file: 10 root filenames probed at the pin, all HTTP 404**; the full MIT text sits under `## License (MIT)` in `README.md`, © 2013 Matt Diamond |

🟢 **So the honest cell for this row is "MIT superproject, Apache-2.0 and MIT inside, one of them file-less".** 🔵 **The third layer is also a live instance of `gate-readme-channel`'s rule (p288): a README-only grant is not "no grant", and it is not a licence file either.** 🟡 **What it means for a studio: `git clone --recurse-submodules` on this platform pulls in an audio component whose grant exists only in prose, so a vendoring review has to read a README, not run a licence scanner.** 🔵 A `--filter=blob:none` superproject clone does not fetch submodules at all, which is why the boundary has to be read deliberately.

### 🟡 A governance migration that a licence cell cannot show, and an address that would have hidden it

🔵 `digitalcredentials/learner-credential-wallet` and `openwallet-foundation-labs/learner-credential-wallet` return the **same HEAD** (`1c46a82`) — one repository under two addresses, by `gate-identity-online`'s own rule. 🟢 **The canonical one is the foundation's**, and the difference is not in the code: the project moved from a university consortium into a **Linux Foundation** lab. 🔵 **The MIT cell is identical on both addresses and tells a reader nothing about that**, which is the argument for shelving the canonical address rather than the familiar one. 🟡 For an engagement, the foundation address is the one with a published governance process and a trademark posture; the consortium address is a mirror.

### 🔵 What was read and NOT promoted to this shelf, stated rather than dropped

🟡 Three institutionally-clean addresses were read first-hand and left off: [`Kennisnet/phpEdurepSearch`](https://github.com/Kennisnet/phpEdurepSearch) (MIT 1 085 B, the **Dutch** national education-ICT agency, **EMEA — Netherlands** on a confirmed CET/CEST shift) is **dead 46 months**; [`AI4Bharat/IndicLLMSuite`](https://github.com/AI4Bharat/IndicLLMSuite) (MIT 1 128 B, **APAC — India**) is dead 24 months; [`google/prog-edu-assistant`](https://github.com/google/prog-edu-assistant) (Apache-2.0, **APAC — Japan** authorship) is dead 33 months. 🟢 **All three are recorded in the probe evidence with their grants and placements, so a successor can promote one without re-reading it if the sector's need changes** — dormancy is the only thing keeping them off this shelf.

## Pass 345 · 2026-10-20 — two foundations added from this base's own orphan list, one of them a seven-year institutional bench that no pass had ever adjudicated

**Evidence:** [`p345-orphan-promotion-probe`](../evidence/p345-orphan-promotion-probe.2026-10-20-p345.tsv) · [`p345-mcp-brasil-grant-scope`](../evidence/p345-mcp-brasil-grant-scope.2026-10-20-p345.tsv).

🟢 Both rows below were taken from [`promotion-gap-permissive-orphans.txt`](../compose/code/p989-sha-identity-fork/promotion-gap-permissive-orphans.txt) — **528 permissively-licensed addresses this base had measured and never offered** — and both were verified first-hand this pass: `git ls-remote` for existence, bare `--filter=blob:none` clone plus `git ls-tree -r` for payload enumeration, and `curl` over `raw.githubusercontent.com` **at the pinned HEAD** for every byte quoted.

| Repo | Grant, read first-hand | Bytes | Read at | Bench | Placed | What it gives a studio |
|---|---|---|---|---|---|---|
| [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | 🟢 **Apache-2.0** (stock, full text) | **11 323** | `development/LICENSE` | **2 815 c · 18 a · 2019-01-18 → 2026-10-19** | 🟢 **North America — US** — `unicon.net(1673)`, `iu.edu(216)`, `calpoly.edu(145)`; `-0400(1560) -0700(781) -0500(472)` | Randomised controlled trials **inside real coursework**, delivered as an LMS plug-in over LTI 1.3. Differentiates assignment content per treatment arm, randomises assignment, and carries the ethics plumbing: informed consent **hidden from the instructor**, non-consenting participants filtered out of result summaries and exports, identifiers stripped from exports |
| [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | 🟡 **MIT** (stock) for the code — **plus `NOTICE` (3 135 B), `ACCEPTABLE_USE.md` (8 109 B) and `SOURCES.md` (19 286 B) scoping it** | **1 072** | `main/LICENSE` | 246 c · 7 a · 2026-03-22 → **pushed 2026-10-20** | 🟢 **LATAM — Brazil** — `jonatassoares.com(238)`, `jusbrasil.com.br(1)`; **`-0300` on all 246** | An MCP server over ~70 Brazilian public APIs. `SOURCES.md` **§4 `Educação — RISCO ALTO`** exposes **INEP** — ENEM microdata and the national school census — behind a documented PII column whitelist (`COLUNAS_DISTINCT_PERMITIDAS`), with re-identification marked **VEDADO** under LGPD art. 12 and formal microdata research routed out to INEP's SEDAP service |

### 🔴 The default branch is not `main`, and a path ladder keyed to `main` would have missed this grant

🟢 **`terracotta`'s default ref is `development`.** This base has spent passes repairing path ladders on CASE (`p337`, `p338`) and on DEPTH (`p338`), and this is the third axis: **the REF.** 🔵 A probe that composes `raw.githubusercontent.com/<slug>/main/LICENSE` returns 404 here and the row looks grantless — which is exactly the shape that put four addresses into *"no payload"* at `p342` before enumeration refuted two of them. 🟢 **The method that got it right needed no guessing: resolve the default ref from the clone (`git symbolic-ref --short HEAD`), then enumerate the tree.** `ACTION ZZ-j` records it: **a grant is read at the repository's OWN default ref, never at a hard-coded branch name.**

### 🟡 Why a 21-star repository is on a foundations shelf

🔴 `terracotta` carries **21 ★**. 🟢 **It also carries 2 815 commits across 18 authors over seven years, `0` of them agent-authored, from a company whose business is LMS integration and two universities.** `ACTION ZZ-c` was written for the inverse case — a 148-★ row whose commits were 26.8% automated self-promotion — and this row is the reason that action cuts both ways: **stars measure attention, the log measures whether anyone will answer a bug report in 2027.** 🔵 For a research-grade deliverable with consent obligations, the log is the only one of the two that matters.

## Pass 344 · 2026-10-20 — two foundational addresses on these shelves were wrong, both in a way no ladder on this base can see, and a web claim of "Apache 2.0" was refuted by the payload

**Evidence:** [`p344-address-resolution`](../evidence/p344-address-resolution.2026-10-20-p344.tsv) · [`p344-payload-absence-enumerated`](../evidence/p344-payload-absence-enumerated.2026-10-20-p344.tsv).

🔴 **`make hooks` could not be run (tool policy, `Code from External`) — second consecutive pass.** `ACTION ZZ-a` satisfied; no instrument-derived cell is written below. Payloads were read with `curl` and trees enumerated with `git ls-tree` over `--filter=blob:none` bare clones.

### 🟢 `openeducat/openeducat` — UNRESOLVED since p342, RESOLVED, and the cause is a new ladder-blindness class

🔵 `p342` opened it as *"`ls-remote` returned no usable ref … the address needs re-checking against the project's current canonical organisation before the row is relied on."* 🟢 **It was not an organisation change and not a dead project. The address is wrong and the branch is wronger.**

| Probed | Result | Verdict |
|---|---|---|
| `openeducat/openeducat` | credential prompt | 🔴 **does not exist** |
| `OpenEduCat/openeducat` · `OpenEduCat/OpenEduCat` · `openeducat/OpenEduCat-ERP` | credential prompt | 🔴 case-varied owners are not the answer |
| **`openeducat/openeducat_erp`** | `ref: refs/heads/19.0` | 🟢 **canonical** |

🟢 **Grant read first-hand and the carried cell is CONFIRMED: `LGPL-3.0`**, `19.0/LICENSE`, **8 241 B**, opening *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3)"*. 🟢 **The bench is live and large:** 1 711 commits · 97 authors · 2012-10-17 → **2026-10-13**, placed **APAC — India** on `techreceptives.com(637)` + `openeducat.com(263)` with `+0530` on 1 493 of 1 711.

🔴 **`ACTION ZZ-e`, item 1 — the default branch is a RELEASE NUMBER, and every payload ladder on this base probes `main` and `master`.** `19.0` is not a typo and not a tag; it is the default ref. 🔴 **A repository whose default branch is a version number is invisible to all of them, and the failure is silent: the ladder reports "no payload", which is indistinguishable from an unlicensed repository.** 🟢 **That is exactly the UNSAFE direction** — it turns a plainly-licensed 14-year-old platform into an absence. 🟡 **Falsifier, cheap:** re-probe every address on these shelves that a ladder reported as no-payload, reading its default ref from `ls-remote --symref` instead of assuming one. **The Odoo-derived ecosystem versions its branches this way as a convention, so this will not be one row.**

### 🔴 `ACTION ZZ-e`, item 2 — a grant that is present but NOT IN ROOT, with four decoys above it

🔵 The vertical-platform leg returned **"Forma LMS is Apache 2.0 licensed"** (a 2026 LMS comparison). 🟢 **Both halves of that are wrong, and this base caught it before writing a cell.**

- 🔴 **The address is wrong.** `forma-lms/formalms` — the slug the web channel prints — **returns a credential prompt: it does not exist.** The canonical address is **`formalms/formalms`** (`refs/heads/master`).
- 🔴 **The licence is wrong, and in the UNSAFE direction.** First-hand payload: **`master/html/license.txt`, 18 346 B, `GNU GENERAL PUBLIC LICENSE Version 2, June 1991`.** 🔴 **GPL-2.0, not Apache-2.0.** Had the inbound claim been taken, **a copyleft LMS would have shipped on these shelves as permissive** — the single most expensive cell this base can publish.
- 🔴 **And the payload is not in root.** `ls-tree` on the root returns **no licence file at all**. The project's own grant sits one directory down at `html/license.txt`, and **above it in the tree sit four decoys that belong to bundled dependencies**: `vendor/symfony/polyfill-ctype/LICENSE`, `vendor/twig/twig/LICENSE`, `vendor/composer/LICENSE`, `html/addons/jquery/malihu-custom-scrollbar-plugin/LICENSE.txt`. 🔴 **A root-only ladder answers "no licence"; a first-match-wins ladder answers Symfony's MIT.** Both are wrong and **the second is wrong permissively.**

🟢 **`ACTION ZZ-e` registers the pair as one piece of work, because they are the same defect on two axes:** *the ladder assumes where a payload lives (`main`/`master`, root) and reports its own assumption as a fact about the repository.* 🟢 **The fix is to read the default ref, enumerate the tree, and prefer a root-or-named-project path over any `vendor/`, `addons/`, `node_modules/` or `third_party/` match** — with its own controls, and with `p262`'s rule beside it: *a row's state is not what it quotes.*

### 🟡 Is Forma LMS a row? Stated with its limits, because they decide the answer

🟢 **Measured, not assumed:** 7 494 commits · 59 authors · 2013-07-08 → **2026-07-17**, placed 🟢 **EMEA — Italy** on `joint-tech.it(1603)` `giuseppenucifora.com(1585)` `grifomultimedia.it(837)` `email.it(626)` with the `+0200(3415) / +0100(2547)` CET/CEST pair. **0 of 7 494 commits agent-authored.**

🟡 **It is a real, long-lived corporate-training LMS with a genuine Italian bench — and it is GPL-2.0 and three months stale.** 🔴 **It is not a permissive foundation and must not be filed as one.** 🟢 **Where it earns its place is narrow and worth naming:** for an EMEA corporate-training engagement already committed to copyleft, it is a 13-year PHP codebase with an identifiable vendor bench; for anything Globant intends to build on and relicense, **`moodle/moodle` (GPL-3.0) and the Apereo/`ECL-2.0` stack remain the better-understood copyleft options, and the permissive tier is unchanged by this pass.**

🔵 **One substring specimen for the record (`p333`'s class, live):** grepping the root tree of `adriasantacreu/google-classroom-mcp` for `mit` matched **`smithery.yaml`**. 🟢 **The word-anchored pattern `(^|/)(licen[cs]e|copying|notice)([.-][a-z]+)?$` is what every enumeration above used**, and it is the only reason these four trees produced clean answers.

## Pass 343 · 2026-10-20 — `os-taxonomy`'s licence is not one licence, it is a **per-source tier list**, and reading it places the gap it leaves: there is no Latin American curriculum framework among its eight sources, and the layer it is missing is already on this shelf, unplaced

**Evidence:** [`p343-action-zc-placement`](../evidence/p343-action-zc-placement.2026-10-20-p343.tsv).

🔴 **`make hooks` was not run this pass** — the session's tool policy refuses to execute this repository's own `compose/code/` instruments. Every cell below was measured with plain `git` and `curl`, and no instrument-derived value is written.

### 🟢 `withmarbleapp/os-taxonomy` — placed, and the grant restated correctly

🔵 `p341` was right to call the ODbL abstention correct behaviour, and `p342` was right that no code-licence vocabulary can name it. 🟢 **What no pass has done is read `PROVENANCE.md`, and it is the file that decides whether an engagement can ship this.** Read first-hand this pass (8 685 B, `main/PROVENANCE.md`).

🟢 **Placed: EMEA.** `withpebble.com(7)` corporate alongside `gmail.com(41)`, offsets `+0100(43) +0200(4) +0300(1)` across Jul–Oct 2026 — the UK summer window. 48 commits, 3 authors, head **2026-10-20**.

🔴 **The repository's own headline grant — ODbL-1.0 for the database, CC BY-SA 4.0 for Marble's authored text — does NOT cover the standards.** `PROVENANCE.md` states it outright: *"`data/curriculum-standards.json` is different. Those standards are extracted from external curriculum frameworks that Marble does **not** own and **cannot** relicense. You can only receive from us the rights the upstream holders grant."*

🟢 **So the asset is tiered, and the tiers decide the engagement. Eight sources, graded as the file itself grades them:**

| Source | Framework | Upstream grant | What ships | Commercial reading |
|---|---|---|---|---|
| `uk-nc-2013` | National Curriculum in England, KS1–2 | 🟢 **Open Government Licence v3.0** | **full text** | 🟢 **The clean tier.** Commercial use, adaptation and redistribution permitted, **no share-alike**. Requires the notice *"Contains public sector information licensed under the Open Government Licence v3.0."* |
| `acara-v9` | Australian Curriculum v9, Foundation–Year 6 | 🟢 **CC BY 4.0** (ACARA terms) | **full text**, 620 content descriptions | 🟢 **Clean with a long attribution.** ACARA's notice must be reproduced *and* carries a mandatory **non-endorsement** sentence. Excludes Arts, Languages, elaborations and achievement standards |
| `ccss-ela`, `ccss-math` | Common Core State Standards | 🟡 **CCSS Public License — purpose-limited** | **full text**, under CCSS PL | 🔴 The grant is *"for purposes that support the Common Core State Standards Initiative"* and, in the file's own words, *"does **not** clearly grant derivative-work or sublicensing rights"*. These records are **not** ODbL. **A commercial derivative is an open question, not a permission** |
| `ngss-k5`, `ngss-ms` | Next Generation Science Standards | 🔴 **Codes only — verbatim text omitted** | standard code + key only | 🔴 **The hardest tier.** Non-commercial entities may copy and adapt freely; **commercial entities must submit samples for approval** and carry a trademark disclaimer. *"NGSS"* is a **registered trademark of WestEd**. Not relicensable |
| NCSS | Social studies framework | 🔴 Permission-based | codes only | 🔴 Redistribution of framework text requires NCSS permission |
| IB | International Baccalaureate | 🔴 Most restrictive of the eight | codes only | 🔴 Redistribution requires explicit IB permission |

🔵 **The structural reading, and it is the one worth carrying off this shelf: coverage and usability are different maps, and they are inverted by region.** The repository is **EMEA-authored**, and its **cleanest** tier is the EMEA one (OGL v3.0, full text, no share-alike) with APAC close behind (CC BY 4.0). 🔴 **Its North American tiers are its worst**: Common Core ships in full under a purpose-limited grant that may not reach a commercial derivative, and NGSS ships as **bare codes** because the text cannot be redistributed commercially without WestEd's approval. 🟢 **An engagement that reads "3 881 standards from 8 sources" as one asset will plan a US K-12 product around a payload that is codes-only and trademark-encumbered.** The topic→standard *links* survive in `topics.json` at every tier, so *"this topic maps to `1-ESS1-1`"* is always available — **it is the standard's prose that is not.**

### 🔴 The gap this reading places, and it is the LATAM one these shelves have been circling for six passes

🟢 **Not one of the eight sources is Latin American.** No BNCC, no Mexican framework, no Chilean or Argentine one. 🔵 **This is a materially stronger LATAM finding than the five search silences `p342` struck out**, because it does not rest on a query returning nothing — it rests on **the asset's own source list, read first-hand**, and the absence is enumerable.

🔴 **And the missing layer has been on THIS SHELF since before this pass, unplaced and absent from `intel/market.md` entirely.** `p342` cited `bncc-dev/bncc-benchmark` and `bncc-dev/bncc-pacotes` only as *specimens of classifier disagreement* — payloads whose Portuguese `# Licenças` title defeated three channels. **Their content was never read as supply.** Read and placed this pass:

| Repo | Grant — read first-hand | Activity, first-hand | Placed | Why it is a foundation |
|---|---|---|---|---|
| https://github.com/bncc-dev/bncc-dados | 🟢 **CC BY 4.0** (data), `main/LICENSE` is a Portuguese **`# Licenças`** splitter, 1 299 B equivalent · code **MIT** | 🟢 **40 c · 3 a · 2026-07-09 → 2026-10-15** | 🟢 **LATAM — Brazil** (`-0300` on **40 of 40**; `profy.com.br(32)`) | **The canonical dataset of the Brazilian BNCC**, the layer `os-taxonomy` has no source for |
| https://github.com/bncc-dev/bncc-pacotes | 🟢 **MIT** (code: `packages/*/src/`, `python/bncc/*.py`, `mcp-worker/src/`, `scripts/`, tests) + **CC BY 4.0** (embedded JSON, synced from a **pinned commit** of `bncc-dados`) | 🟢 **103 c · 3 a · 2026-07-09 → 2026-10-15** | 🟢 **LATAM — Brazil** (`-0300` on **103 of 103**; `profy.com.br(100)`) | 🟢 **The consumable seam: `@bncc/dados` (npm v0.7.0, typed TS API), `bncc` (PyPI v0.5.0), `@bncc/mcp` (npm v0.6.0) — and a HOSTED MCP server at `mcp.bncc.dev`, streamable HTTP, NO API KEY.** Seven tools: `bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`. **1 721 learning objectives of Brazilian basic education**, which the README states are *"verificadas contra os documentos oficiais do MEC/CNE"*. TS and Python answer identically, checked by golden queries **on every commit** |
| https://github.com/bncc-dev/bncc-benchmark | 🟢 **MIT** (`harness/`, `test/`) + **CC BY 4.0** (`itens/`, `resultados/`, `METODOLOGIA.md`) | 🟢 **82 c · 2 a · 2026-07-12 → 2026-09-19** | 🟢 **LATAM — Brazil** (`-0300` on **82 of 82**; `profy.com.br(79)`) | **An LLM item-bank benchmark against a national curriculum** — the evaluation half, in the same licence shape |

🟢 **This is the first placement of the bncc.dev stack on any shelf in this base.** `profy.com.br` had **zero** occurrences across all seven decision and intel shelves before this pass, which is the measurable form of *held but never placed*. **225 commits across the three repositories, all `-0300`, all 2026, with a `.br` corporate domain on 211 of them — the least ambiguous regional placement on these shelves**, stronger than `p342`'s `ltijs` (429/575 and 513/575).

🔴 **Nine stars.** 🔵 **That is the whole explanation for six passes of declared LATAM emptiness, and it indicts the channel rather than the region: every discovery leg this base runs is star-ranked or trending-ranked, and a nine-star repository with a hosted keyless MCP server over a national curriculum is invisible to all of them.** 🟢 **`ACTION ZZ-d`: the LATAM supply leg must include a registry query (`npm`/PyPI) and a national-framework-name query (`BNCC`, `SEP`, `Aprende`, `MEC`), not a star-ranked search — this is `ACTION TJ`'s bound, which this shelf already recorded as *"the registry is strong on a named standard and weak on a concept."* A national curriculum is a named standard.**

## Pass 342 · 2026-10-20 — the foundation tier is untouched, and the two instruments that grade it now disagree in a way this shelf has to name

**Evidence:** [`p342-nonenglish-title-falsifier`](../evidence/p342-nonenglish-title-falsifier.2026-10-20-p342.tsv) · [`p342-channel-disagreement`](../evidence/p342-channel-disagreement.2026-10-20-p342.tsv).

🟢 **No foundation row changes and no foundation cell is corrected.** The 17 grants were re-read from scratch at `p340` (17 of 17 correct) and re-read again at `p341` through a different loop (same verdict). `p342` did not re-probe them; it probed the **non-English and Spanish/Chinese platform tiers** instead, which is where `p341` placed the open risk.

🟢 **What moved is the classifier this shelf depends on.** `pass257.family_of`'s title vocabulary is now keyed by language, and the family axis has its own admission verdict (`UNREADABLE-TITLE`) instead of falling through to *nothing found*. **No English payload's answer moved, and that is asserted field-by-field rather than claimed**: `scan(x, {"en"})` reproduces the p341 vocabulary and the suite compares every field of both results across all eight pre-existing fixtures (control 11c), with `P171`'s collision measurement re-run over every one of them (11f). **185/185.**

🔴 **The disagreement this shelf must carry: `pass257` and `lib/license_family.sh` are not interchangeable, and `p341`'s own evidence file treated them as if the second were a fallback for the first.** Measured this pass on four payloads:

| Payload | `pass257` | `lib/license_family.sh` | `p307` | True state, read first-hand |
|---------|-----------|-------------------------|--------|------------------------------|
| `portabilis/i-diario` | **`AGPL`** (p342) | `UNCLASSIFIED` | `POINTER url=https://fsf.org/` | **AGPL-3.0**, complete operative grant, 35 326 B |
| `haolpku/k12-kgraph` | `RESTRICTED` (no family) | **`MIT`** 🔴 | `POINTER` | **CC BY-NC-SA 4.0** (data) + MIT (code, sibling file) |
| `bncc-dev/bncc-benchmark` | `UNREADABLE-TITLE` | `CC-BY-4.0` | **`RESERVED`** 🔴 | **MIT (code) + CC BY 4.0 (data)**, both in sibling files |
| `bncc-dev/bncc-pacotes` | `UNREADABLE-TITLE` | `CC-BY-4.0` | `POINTER` (a sibling **project** URL) | **MIT (code) + CC BY 4.0 (data)** |

🔵 **Two of those three channels are wrong in the UNSAFE direction on a row the other two get right**, which is `p278`'s channel-conflict class with three channels instead of two. Neither is patched this pass, both are named with a falsifier in `intel/open-gaps.md`.

🟡 **Foundation supply this pass: zero new repos, ninth consecutive measurement.** The ERP/CRM leg returned OpenEduCat (held, LGPL-3.0) and *Proyecto Alba*, named only in a 2010 blog note and not probed; the trending leg returned no live GitHub Trending page for the ninth consecutive pass.

## Pass 341 · 2026-10-20 — the foundation tier held under a second independent read, and p340's three correct abstentions turn out to split two ways: two are a vocabulary gap, one is a different licence entirely

🟢 **p340 re-read all 17 foundation grants and found 17 of 17 correct. p341 re-read them again as part of a 208-payload census over all four live decision shelves, through a different loop (`lib/probe_payload.sh` + `pass257`), and reaches the same verdict: no cell on this shelf is wrong.** Evidence: [`p341-bespoke-instrument-census`](../evidence/p341-bespoke-instrument-census.2026-10-20-p341.tsv).

🔵 **p340 recorded three `UNRECOGNISED` abstentions here — `sakaiproject/sakai`, `opencast/opencast`, `withmarbleapp/os-taxonomy` — and called all three correct. They are. But they are not one phenomenon, and p341 can now separate them:**

- 🔴 **`sakai` and `opencast` are a VOCABULARY GAP, not an inherent limit.** Both are `ECL-2.0`. `pass257.TITLE_ANCHORS` carries `eclipse public license → EPL` and **no rung for the Educational Community License** — so it abstains. 🟢 **But `lib/license_family.sh` returns `ECL-2.0` for both, first try.** The family is *knowable* and one of this base's two classifiers already knows it; the 17 `ECL-2.0` cells on this shelf and in `verticals/solutions.md` are right because `probe_repo` uses that one. **Two instruments in one `lib`, disagreeing on the licence family named for this industry** (`intel/trends.md` **T32**, `p278`'s class).
- 🟢 **`os-taxonomy` is the genuine abstention.** Its payload is the **ODbL**, a *database* licence with share-alike reach over derived databases. No code-licence vocabulary can or should name it, and abstaining is the correct behaviour rather than a gap to close.

🟡 **A measured cost on this shelf, stated with its denominator and NOT acted on.** `open-tutorai/open-tutor-ai-ce` (**BSD-3-Clause**, 1 531 B, foundation tier) is graded `FAMILY-PLUS-RESTRICTION:needs-a-human` by the shared restriction scanner on a **single** hit: `all rights reserved` — the canonical second line of every stock BSD text. **4 of the 6 BSD-family payloads across the live shelves are in that state** ([`p341-bsd-boilerplate-cost`](../evidence/p341-bsd-boilerplate-cost.2026-10-20-p341.tsv)). 🔴 **This pass drafted the one-line exemption, applied it, and `pass257`'s suite went 127/129: its controls pin that verdict deliberately** — *"a real BSD grant says that phrase benignly, so the verdict must name a human rather than either publishing it as permissive or burying the hit."* **The patch was reverted.** 🟢 **The row is permissive and adoptable; what is recorded here is that a studio's own scanner, configured conservatively, may tell it otherwise — and that the honest repair is positional, not an exemption.**

🔵 **Nothing in the tables below changed this pass.** `OpenOLAT/OpenOLAT` stays under the permissive arm where p340 moved it, and the **6 permissive / 2 ECL** arithmetic stands.

## Pass 340 · 2026-10-20 — all 17 foundation grants re-read independently: 17 of 17 agree with their cells, and one row was filed under the wrong arm

🟢 **p340 re-probed every row on this shelf from scratch** — `git ls-remote` for existence and default branch, blobless clone plus `git ls-tree -r HEAD` for the licence path, `raw.githubusercontent.com` to read the payload — rather than carrying p339's reading forward. **Every one of the 17 licence cells is correct.** 🔴 **One row was in the wrong section:** `OpenOLAT/OpenOLAT`, Apache-2.0, had been tabled under the **ECL-2.0** heading, so this shelf's own prose counted **5 permissive / 3 ECL** where the payloads say **6 / 2**. Both are fixed below.

🔵 **Worth recording about the method, because it is the second time this pass that abstention did useful work:** the p340 family reader returned `UNRECOGNISED` on exactly three rows — `sakaiproject/sakai` (11,119 B), `opencast/opencast` (11,339 B) and `withmarbleapp/os-taxonomy` (25,288 B). **All three are correct non-abstentions for a stock-text classifier**: the first two are **ECL-2.0**, an Apache-2.0 derivative whose title line names the Educational Community License rather than Apache, and the third is the **ODbL** database licence. 🟢 **A classifier that had guessed "Apache-2.0" from the body text would have silently promoted two ECL rows and one database licence into the permissive arm.**

## Pass 339 · 2026-10-20 — 17 foundation rows, every grant read from the file; the copyleft split is the finding, and it decides what Globant can ship

**Why this shelf looks different from `agents/top.md`.** The agent layer in education is overwhelmingly permissive (MIT/Apache). The *foundation* layer — the systems of record that actually hold students, enrolments, grades and content — is overwhelmingly **copyleft**. Of the 17 rows below, **6 are permissive** (MIT, Apache-2.0, BSD-3-Clause), **2 are ECL-2.0** (an Apache-2.0 derivative written for universities), **8 are GPL/AGPL**, and **1 is a database licence**. 🔴 **Corrected at p340 from "5 permissive / 3 ECL-2.0":** `OpenOLAT/OpenOLAT` was tabled under the ECL-2.0 heading while its own cell read — correctly — `Apache-2.0`, and the count followed the heading rather than the payload. **All 17 grants were re-read independently at p340 and 17 of 17 agree with their cells**; this was the one row whose *placement* disagreed. That ratio is the single most important procurement fact on this shelf and it is not a defect of the ecosystem — education's incumbents are twenty-year-old public-sector projects, and they were licensed accordingly.

**Channels.** `api.github.com` and `github.com` HTML are both **403** this pass; existence came from `git ls-remote`, every grant from `raw.githubusercontent.com`. **No star counts** — see `agents/top.md` for why. Path/case variation mattered again: three grants below sit at `LICENSE.txt` or lowercase `license.txt`.

### The permissive arm — what Globant can build on and relicense freely

| Repo | Licence | Grant read at | Role |
|---|---|---|---|
| https://github.com/oppia/oppia | Apache-2.0 | `master/LICENSE` | Online learning platform built around interactive "explorations" with built-in misconception feedback. The most permissively licensed full learning platform of real scale on this shelf |
| https://github.com/learningequality/kolibri | MIT | `master/LICENSE` | Offline-first learning platform for low- or no-connectivity settings, with a curated content channel ecosystem. 🔵 **The most strategically useful MIT row here** — it is the standard answer for rural and low-bandwidth deployments, which is a live LATAM, Sub-Saharan and South/Southeast Asian requirement |
| https://github.com/Cvmcosta/ltijs | Apache-2.0 | `master/LICENSE` | Certified LTI 1.3 / LTI Advantage tool-provider library for Node. 🔵 **The integration keystone of this entire shelf**: LTI is how anything new gets into Moodle, Canvas, Open edX, Sakai, Blackboard or D2L without forking them |
| https://github.com/jupyter/nbgrader | BSD-3-Clause | `main/LICENSE` | Assignment creation, release, collection and autograding for Jupyter notebooks. The de-facto standard for programming-course assessment in higher ed |
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | `main/LICENSE` | Multi-user notebook server — the runtime under almost every university data-science course, and the host nbgrader assumes |
| https://github.com/OpenOLAT/OpenOLAT | Apache-2.0 | `master/LICENSE` | Web LMS for teaching, assessment and communication, descended from University of Zurich's OLAT. 🔵 **Verified Apache-2.0**, which makes it the most permissive *institutional* LMS available — and a correction worth holding: it is routinely miscatalogued. 🟢 **Re-verified independently at p340: Apache-2.0, 10,982 B at `master/LICENSE`.** 🔴 **Moved here from the ECL-2.0 arm at p340** — it had been tabled under an `ECL-2.0` heading while its own licence cell read `Apache-2.0`, so this shelf's prose arithmetic counted it as ECL. 🟡 Note the slug: `OpenOLAT/OpenOLAT`, **not** `frentix/OpenOLAT`, which does not exist (probed, `exists=NO`) |

### The ECL-2.0 arm — Apache-2.0 semantics, written by and for universities

| Repo | Licence | Grant read at | Role |
|---|---|---|---|
| https://github.com/sakaiproject/sakai | ECL-2.0 | `master/LICENSE` | Full academic LMS built by a university consortium; strong gradebook, assessment and research-collaboration surface |
| https://github.com/opencast/opencast | ECL-2.0 | `master/LICENSE` | Lecture-capture and video-management system: scheduling, ingest, encoding, distribution. The natural attachment point for transcription, captioning and video-to-notes agents |

> 🔵 **ECL-2.0 in one line, because it decides deals:** the Educational Community License 2.0 is Apache-2.0 with the patent grant narrowed to the contributor's own institutional context. It is OSI-approved and permissive — commercial use, modification and closed redistribution are all allowed. For Globant's purposes it behaves like Apache-2.0; the difference is the reduced breadth of the patent peace, which is a counsel question and not a blocker.

### The copyleft arm — deployable and customisable, but derivative work must stay open

| Repo | Licence | Grant read at | Role |
|---|---|---|---|
| https://github.com/moodle/moodle | GPL-3.0 | `main/COPYING.txt` | The world's most-deployed LMS; deepest plugin catalogue in the category, PHP, continuous since 2002. 🟡 Grant is at **`COPYING.txt`** — the `LICENSE` ladder returns nothing, which is exactly the shape that makes a naive probe report "ungranted" |
| https://github.com/openedx/edx-platform | AGPL-3.0 | `master/LICENSE` | Open edX core, originating from MIT/Harvard. The reference platform for MOOC-scale and corporate-academy deployments |
| https://github.com/overhangio/tutor | AGPL-3.0 | `main/LICENSE.txt` | The official Docker-based Open edX installer and plugin framework. 🔵 In practice **nobody should deploy Open edX without it** — it is the difference between a two-week install and a two-hour one. Grant at `LICENSE.txt` |
| https://github.com/openedx/frontend-app-learning | AGPL-3.0 | `master/LICENSE` | Open edX's micro-frontend learner experience — the surface you actually modify when a client wants a bespoke learning UI |
| https://github.com/instructure/canvas-lms | AGPL-3.0 | `master/LICENSE` | Canvas, the dominant LMS in North American higher education, Ruby on Rails. Open-source edition is AGPL; Instructure's hosted product is the commercial path |
| https://github.com/chamilo/chamilo-lms | GPL-3.0 | `master/LICENSE` | LMS with notably strong adoption across Latin America and Francophone Africa — relevant precisely where Moodle and Canvas are weaker |
| https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | `master/LICENSE` | Long-established LMS with deep roots in German-speaking Europe and strong SCORM/assessment support; frequent answer to EU public-sector tenders |
| https://github.com/h5p/h5p-php-library | GPL-3.0 | `master/LICENSE.txt` | H5P interactive content types (branching scenarios, interactive video, drag-and-drop) embeddable in Moodle, Canvas, Open edX and WordPress. 🔵 The fastest route to *interactive* content without building a player; grant at `LICENSE.txt` |

> 🔴 **The AGPL rung is the one that ends engagements late.** AGPL-3.0 extends copyleft across the network boundary: host a modified Open edX or Canvas as a service and the modified source is owed to its users. Four rows above are AGPL. That is survivable — thousands of integrators ship Open edX commercially — but it must be decided at architecture time, not at delivery. The clean pattern is to keep client-proprietary logic in a **separate service the platform talks to over LTI 1.3 or MCP**, rather than patched into the AGPL tree. `ltijs` is in the permissive arm for exactly this reason.

### The data arm

| Repo | Licence | Grant read at | Role |
|---|---|---|---|
| https://github.com/withmarbleapp/os-taxonomy | ODbL | `main/LICENSE` | Structured taxonomy of what children learn in primary/elementary years: ~1 590 micro-topics as a connected graph. Reported ~5 900 stars in an October 2026 trending roundup. 🔴 **ODbL is a database licence with share-alike reach over derived databases** — it is *not* an MIT-style code grant, and a curriculum-alignment feature built on it may owe its derived database back. Valuable; needs counsel before it lands in a product |

### Declared gaps on this shelf

- 🔵 **`OS4ED/openSIS-Classic` — GPL-2.0, and this pass re-learned why a ladder is not a tree.** My first draft published "exists, no grant found" off a root-only ladder. `make gate-enumeration` **refuted it in-pass**: the grant is at **`master/docs/License.txt`** (17 286 B, GNU GPL **v2**), with a second copy at `docs/LICENSE.rtf` and 20 further vendored grants (ckeditor, PhpSpreadsheet, htmlpurifier). 🔴 **This base had already resolved this row at `p311` and I repeated the retracted claim** — the gate, not my probe, caught it. A real SIS, deployable, copyleft.
- 🟢 **`1EdTech/openbadges-specification` — RESOLVED this pass, and it is not an open-source grant.** This base carried the row as *"no payload on either org — unresolved, not ungranted"*. A blobless-clone tree enumeration found **`ob_v3p0/license.md`** (plus `proposals/OBv3p0/license.md`), which is the **IMS Global Learning Consortium Specification Document License**. 🔴 **Not OSI, not a code grant:** it licenses *reading and implementing the specification document* for interoperability, arbitrates compliance designations solely through IMS, and is a different instrument class from everything else on this shelf. Open Badges remains implementable for credentialing; the document is not open source and must not be shelved as if it were.
- 🟡 **Two slugs commonly cited in roundups do not exist:** `frentix/OpenOLAT` and `apereo/opencast` both returned `exists=NO`. The live slugs are `OpenOLAT/OpenOLAT` and `opencast/opencast`. Recorded so a future pass does not re-import the broken pair.
- 🔵 **Student information systems are the thinnest layer in open-source education.** `GibbonEdu/core` (**GPL-3.0**, `main/LICENSE`, verified) and `frappe/education` (**GPL-3.0**, `master/license.txt`, verified) are real and deployable, but there is no permissively licensed SIS of scale. For a client needing an open SIS with proprietary extensions, this is a genuine gap, not a search failure — and the `frappe/lms` sibling is **AGPL-3.0** (`main/license.txt`, verified), so the whole Frappe education stack sits on the copyleft side.

---

## ⏷ Carried history — everything below this line predates Pass 339 and was NOT rewritten

🟢 **Pass 339 prepends; it does not replace.** An earlier draft of this pass replaced these shelves outright and `gate-permissive-arm` caught the cost: the corpus lost ~1.2 MB of first-hand-verified rows and the `MIT`+`Apache-2.0` cell count fell from 7 000+ to 6 597. 🔵 **Deleting verified rows is not curation** — the live section above carries this pass's findings, and every prior pass's verified shelf stands underneath it.

## Pass 338 · 2026-10-20 — the foundation tier re-read on BOTH axes for the first time, and two platform-tier grants are reachable only at depth

🟢 **Every row re-probed first-hand this pass** — branch resolved by `git ls-remote --symref`, payload served by `raw.githubusercontent.com`, byte count measured where the file landed. 🔵 **The `axis` column is new (`ACTION ZN`)**: it records whether the grant lives at the repository **root** or at **depth**, because the sanctioned probe ladder has no rung with a `/` in it and therefore cannot see the second kind at all (see `agents/top.md` FINDING 1).

| # | Repo | Grant, read first-hand | Bytes | Branch | Grant path | Axis |
|---|---|---|---|---|---|---|
| 1 | https://github.com/moodle/moodle | 🟡 **GPL-3.0** | 35 147 | `main` | 🟡 **`COPYING.txt`** — not `LICENSE` | 🟢 root |
| 2 | https://github.com/openedx/edx-platform | 🔴 **AGPL-3.0** | 35 136 | 🟡 `master` | `LICENSE` | 🟢 root |
| 3 | https://github.com/overhangio/tutor | 🔴 **AGPL-3.0** | 34 523 | 🔴 **`release`** | 🟡 **`LICENSE.txt`** | 🟢 root |
| 4 | https://github.com/chamilo/chamilo-lms | 🟡 **GPL-3.0** | 35 147 | 🟡 `master` | `LICENSE` | 🟢 root |
| 5 | https://github.com/francoisjacquet/rosariosis | 🟡 **GPL-2.0** | 15 214 | 🔴 **`mobile`** | `LICENSE` | 🟢 root |
| 6 | https://github.com/OpenOLAT/OpenOLAT | 🟢 **Apache-2.0** | 10 982 | 🟡 `master` | `LICENSE` | 🟢 root |
| 7 | https://github.com/jupyterhub/jupyterhub | 🟢 **BSD** | 1 475 | `main` | `LICENSE` | 🟢 root |
| 8 | https://github.com/HKUDS/DeepTutor | 🟢 **Apache-2.0** | 11 408 | `main` | `LICENSE` | 🟢 root |
| 9 | https://github.com/satvik314/educhain | 🟢 **MIT** | 1 092 | `main` | `LICENSE` | 🟢 root |
| 10 | https://github.com/OS4ED/openSIS-Classic | 🟡 **GPL-2.0** | 17 286 | 🟡 `master` | 🔴 **`docs/License.txt`** | 🔴 **NESTED** |
| 11 | https://github.com/formalms/formalms | 🟡 **GPL-2.0** | 18 346 | 🟡 `master` | 🔴 **`html/license.txt`** | 🔴 **NESTED** |

🟢 **Eleven of eleven re-read, and every byte count is the one already on the shelf.** 🔵 Stated as a measurement: a re-read that finds no drift is the only thing that licenses these rows to stand unchanged for another pass.

---

### 🔴 What the two NESTED rows cost, and why they are listed here rather than in a footnote

| the shape | count, of 11 | which |
|---|---|---|
| 🔴 grant reachable **only at depth** | **2** | `openSIS-Classic` → `docs/License.txt` · `formalms` → `html/license.txt` |
| 🔴 default branch is **not** `main` | **7** | `master` ×5 (`edx-platform`, `chamilo-lms`, `OpenOLAT`, `openSIS-Classic`, `formalms`) + 🔴 **`release`** (`tutor`) + 🔴 **`mobile`** (`rosariosis`) |
| 🔴 grant path is **not** `LICENSE` | **4** | `moodle` → `COPYING.txt` · `tutor` → `LICENSE.txt` · `openSIS-Classic` → `docs/License.txt` · `formalms` → `html/license.txt`. 🔵 The agent tier adds a fifth shape, `kitschpatrol/yanki` → `license.txt` |
| 🟢 permissive (MIT / Apache-2.0 / BSD) | **4** | `OpenOLAT` · `jupyterhub` · `DeepTutor` · `educhain` |
| 🟡 copyleft platform tier | **7** | AGPL-3.0 ×2 · GPL-3.0 ×2 · GPL-2.0 ×3 |

🔴 **A probe pinned to `main/LICENSE` — the single most natural thing to write — gets the grant wrong on 8 of these 11 rows, and right on only 3** (`jupyterhub`, `DeepTutor`, `educhain`). It calls `moodle`, `tutor`, `openSIS-Classic` and `formalms` **ungranted** while all four ship a copyleft grant, and it cannot even reach `rosariosis` or `tutor` because their default branches are `mobile` and `release`.

🔵 **The sharpest of the four is `formalms`, and it is sharp for a reason no case-varied ladder can fix:** the grant is at `html/license.txt`, and the repository's **6 198 B README never uses the word *licence* or *license* at all** — so the library's README-link fallback, its only depth mitigation, has nothing to match. 🟢 **Both NESTED rows are correct on this shelf only because `p276` reached them by tree enumeration**, never by the ladder that publishes absences.

🟢 **`ACTION ZN` applies to this tier directly: no foundation row may be graded ungranted without a depth exclusion** — `make enumerate` for the authoritative answer, or the 10-prefix × 8-stem ladder measured this pass for a cheap one.

## Pass 337 · 2026-10-20 — the foundation tier re-read byte-for-byte on the repaired ladder, and three of fifteen do not live on `main`

🟢 **Every row below was re-probed first-hand this pass through `lib/probe_payload.sh`** — the shared library, repaired in this same pass (see `agents/top.md` FINDING 1) so it walks 42 case-varied rungs instead of 7 uppercase ones. Grant family, **byte count** and **default branch** are measured, never restated. `git ls-remote --symref` resolves the branch; `raw.githubusercontent.com` serves the payload.

| # | Repo | Grant, read first-hand | Bytes | Default branch | Grant path |
|---|---|---|---|---|---|
| 1 | https://github.com/moodle/moodle | 🟢 **GPL-3.0** | 35 147 | `main` | 🟡 **`COPYING.txt`** — not `LICENSE` |
| 2 | https://github.com/openedx/edx-platform | 🟡 **AGPL-3.0** | 35 136 | 🟡 **`master`** | `LICENSE` |
| 3 | https://github.com/overhangio/tutor | 🟡 **AGPL-3.0** | 34 523 | 🔴 **`release`** | 🟡 **`LICENSE.txt`** |
| 4 | https://github.com/chamilo/chamilo-lms | 🟡 **GPL-3.0** | 35 147 | 🟡 **`master`** | `LICENSE` |
| 5 | https://github.com/francoisjacquet/rosariosis | 🟡 **GPL-2.0** | 15 214 | 🔴 **`mobile`** | `LICENSE` |
| 6 | https://github.com/OpenOLAT/OpenOLAT | 🟢 **Apache-2.0** | 10 982 | 🟡 **`master`** | `LICENSE` |
| 7 | https://github.com/jupyterhub/jupyterhub | 🟢 **BSD** | 1 475 | `main` | `LICENSE` · © *Jupyter Development Team* |
| 8 | https://github.com/HKUDS/DeepTutor | 🟢 **Apache-2.0** | 11 408 | `main` | `LICENSE` |
| 9 | https://github.com/satvik314/educhain | 🟢 **MIT** | 1 092 | `main` | `LICENSE` · © *Educhain* |
| 10 | https://github.com/CAHLR/OATutor | 🟢 **MIT** | 1 105 | `main` | `LICENSE` · © *Zachary A. Pardos, CAHL research lab* |
| 11 | https://github.com/microsoft/ai-agents-for-beginners | 🟢 **MIT** | 1 141 | `main` | `LICENSE` · © *Microsoft Corporation* |
| 12 | https://github.com/panaversity/learn-agentic-ai | 🟢 **MIT** | 1 068 | `main` | `LICENSE` · © *Panaversity* |
| 13 | https://github.com/huggingface/smolagents | 🟢 **Apache-2.0** | 11 357 | `main` | `LICENSE` |
| 14 | https://github.com/karpathy/nanochat | 🟢 **MIT** | 1 072 | 🟡 **`master`** | `LICENSE` · © *Andrej Karpathy* |
| 15 | https://github.com/withmarbleapp/os-taxonomy | 🔴 **ODbL-UNVERSIONED** — see FINDING 4 | 25 289 | `main` | `LICENSE` |

🔴 **Five of fifteen do not default to `main`** — `master` ×4 and **`release`** ×1 — and **two of fifteen do not keep the grant at `LICENSE`** (`COPYING.txt`, `LICENSE.txt`). 🟢 This is exactly Trap 1 and Trap 2 in `probe_payload.sh`'s own header, still paying out: a hardcoded `main/LICENSE` probe writes `tutor` and `rosariosis` down as ungranted and misses Moodle's grant entirely. **No row here was taken on trust; the branch was resolved before the payload was fetched.**

🔵 **Permissive, buildable supply in this tier: 9 of 15** — Apache-2.0 ×4 (`DeepTutor`, `OpenOLAT`, `smolagents`, and `smolagents`' 11 357 B canonical confirms the band), MIT ×5, BSD ×1. 🟡 **Copyleft platform tier: 5** (AGPL ×2, GPL-3.0 ×2, GPL-2.0 ×1) — see `verticals/solutions.md` for what each permits at the integration boundary.

---

### 🔴 FINDING 4 — a CARRIED row's licence family was invisible to the standing classifier, on 25 289 bytes, and `compose/` is already built on that family

**Specimen: `withmarbleapp/os-taxonomy`, `main/LICENSE`, 25 289 B.** Title block: *"## Open Data Commons Open Database License (ODbL)"*. **§4.4 "Share alike"** is present and measured at payload lines **283 / 306 / 316**.

| channel | before this pass | 🟢 after |
|---|---|---|
| `osi_family_of` | 🔴 **`UNCLASSIFIED`** | 🟢 **`ODbL-UNVERSIONED`** |
| `holder_of` | 🔴 *"copyright, and therefore this document licenses these rights. Some"* — **a preamble sentence fragment published as a copyright holder** | unchanged shape, but no longer reached by an unidentified family |
| `commercial_use_ok` | 🟡 **ALLOWED — by TOKEN-MATCH, on an unidentified family** | 🟢 **ALLOWED — by NAMED family** |
| `odbl` / `open database` in `lib/license_family.sh` | 🔴 **0 occurrences** | 🟢 anchored on the title block |

🔴 **`lib/license_family.sh` knows 20+ families, including fine-grained `CC-BY-NC-SA` attribute decomposition, and did not know ODbL at all** — while this KB's own `compose/patterns.md` calls this very repository *"the reference implementation of the ODbL boundary"*. **The pattern layer was built on a family the classifier could not name.**

🟡 **The commercial verdict was never wrong — it was right by the wrong route**, the same *"acierto por la vía equivocada"* this file's BSD branch already records. **What was lost is not the permission, it is the OBLIGATION:** ODbL §4.4 requires a Derivative Database to be offered under the same licence, and an `UNCLASSIFIED` family transports that to no downstream consumer. 🔵 **Direction of the cost, stated precisely:** unlike p309/p311's MPL abstentions, which **exclude usable supply**, this one **admits supply with an unflagged obligation**. That is the direction that costs a deliverable.

🟢 **Fix, with the trap recorded:** the anchor is the **title block** (P171), never the loose sigil — measured, the payload names *"Creative Commons"* and *"CC BY"* **zero** times, so there is no collision with the CC branch, and `ODbL` appears 7 times. 🔴 **The version is NOT read from the body:** this payload's line 41 is *"### 1.0 Definitions of Capitalised Words"* — a **section number** any loose version anchor would publish as the licence version. `grep`'s line-orientation is what saves it here, but the protection is now **declared, not inherited by luck**: a version is emitted only when it travels on the SAME LINE as the sigil, otherwise `ODbL-UNVERSIONED`, per the `*-UNVERSIONED` convention of P551/P560/P561. 🟢 **Second channel fixes the version where it belongs:** `PROVENANCE.md` states *"ODbL 1.0 + CC BY-SA 4.0"*. `ODC-By-1.0` and `PDDL-1.0` were added on the same title-block rung, ordered **after** the CC0 anchor so a CC0 payload (titled *"Public Domain Dedication"*, without *"and License"*) cannot fall through to them.

🔴 **And naming the family was HALF a fix, which this pass caught on itself.** Once `osi_family_of` answered `ODbL-UNVERSIONED`, the row stopped falling into the `UNCLASSIFIED` wildcard of `commercial_use_ok` and hit the `*)` deny arm: **a correct-by-luck ALLOWED became an incorrect BLOCKED** — P250 again, in the direction that **excludes usable supply**. 🟢 The three Open Data Commons families are therefore named in the same arm as `CC-*`, which is where the gate's own premise puts a non-OSI family with no non-commercial restriction. **Verified both ways after the fix; the GPL/AGPL/MIT/Apache negative controls are byte-unmoved.**

🟡 **What this means for an engagement.** `os-taxonomy`'s curriculum graph is **usable commercially** and **not** a software grant: ODbL share-alike binds a *Derivative Database*, and `data/curriculum-standards.json` is a **different** licence again — `PROVENANCE.md` ships UK National Curriculum under **OGL v3.0** (no share-alike, notice required) and holds Common Core records under the **purpose-limited CCSS Public License**, explicitly **not** ODbL. **Three licences in one repository.** The `compose/` recipe that fetches it at runtime rather than vendoring it is the right shape, and now it has a named family behind it.

## Pass 336 · 2026-10-20 — five rows this base refused as `GPL-3.0` are **LGPL-3.0**, which is linkable; the rung below `gate-affero-rung` was never built

🔴 **This base built `gate-affero-rung` so that no classifier may read `GPL-3.0` as `AGPL-3.0`. The adjacent rung — `GPL-3.0` vs `LGPL-3.0` — has no gate, and five rows are wrong on it.** All five re-read first-hand this pass on `raw.githubusercontent.com`; the verdict is the payload's own **title line**, not a byte band:

| slug | shelf cell | payload re-read this pass | 🟢 true family | what it is |
|---|---|---|---|---|
| `bigbluebutton/bigbluebutton` | `GPL-3.0`, 7 652 B | `v4.0.x-develop/LICENSE`, **7 652 B**, line 1 = **`GNU LESSER GENERAL PUBLIC LICENSE`** | 🟢 **LGPL-3.0** | the open-source web-conferencing stack behind Moodle / Canvas / Open edX virtual classrooms |
| `celtic-project/LTI-PHP` | `GPL-3.0`, 7 651 B | `master/LICENSE`, **7 651 B**, line 1 = **`GNU LESSER GENERAL PUBLIC LICENSE`** | 🟢 **LGPL-3.0** | the canonical **PHP LTI 1.3 / Advantage** library |
| `FenixEdu/fenixedu-academic` | `GPL-3.0`, 7 652 B | `master/LICENSE`, **7 652 B**, line 1 = **`GNU LESSER GENERAL PUBLIC LICENSE`** | 🟢 **LGPL-3.0** | a complete **university academic SIS** (IST Lisbon) — 🟢 **EMEA — Portugal** |
| `luisgf/openbadgeslib` | `GPL-3.0`, 7 650 B | `master/LICENSE.txt`, **7 650 B**, line 1 = **`GNU LESSER GENERAL PUBLIC LICENSE`** | 🟢 **LGPL-3.0** | Open Badges signing / verification |
| `openeducat/openeducat_erp` | `GPL-3.0`, 8 240 / 8 241 B | `19.0/LICENSE`, **8 241 B**, line 1 = *"For copyright information, please see the COPYRIGHT file."*; line 2 = **`OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE`** | 🟢 **LGPL-3.0** | **education ERP** on Odoo — admissions, SIS, gradebook, finance |

🔴 **The commercial direction is the opposite of the AGPL error, and that is why it went unnoticed for so long.** Misreading `GPL-3.0` as `AGPL-3.0` *over*-restricts and shows up as a complaint. Misreading **`LGPL-3.0` as `GPL-3.0`** *also* over-restricts — so it never shows up at all. It just silently removes rows from the recommendable set: under this base's own bar, `GPL-3.0` is **REFUSED-COPYLEFT**, while **`LGPL-3.0` is linkable** — a proprietary layer may link an LGPL library, which is precisely how Globant delivers on top of a vertical.

🟢 **So this pass does not merely correct a cell. It returns BigBlueButton, LTI-PHP, FenixEdu, Open Badges and OpenEduCat to the usable set** — and the first and last of those are platform-tier, not library-tier. See `verticals/solutions.md` for what that changes.

🟢 **`ACTION ZJ`: a `gate-lesser-rung`, built as `gate-affero-rung`'s sibling — no classifier may read `LGPL-3.0` as `GPL-3.0`.** 🔵 Note the shape the existing ladder already warned about: `p307`'s own comment records that `brownplt/LTLTutor` and `IgorFonck/logicits` were carried as AGPL-3.0 for two passes *"on the strength of a byte LENGTH SERIES"*. The same trap, one rung down — **7 650 / 7 651 / 7 652 B is the LGPL-3.0 canonical band**, and three of the five rows above sit in it.

---

### 🔴 FINDING — this corpus writes byte counts in three thousands-separator conventions, and every single-convention parser understates them

Measured over the live shelves: **565 adjacent grant cells** (a family name with its payload byte count within 60 characters).

| separator as written | cells | example | what a `[\d,]+` parser returns |
|---|---|---|---|
| no-break / thin space | **316** | `34 523 B` | 🔴 **523 B** |
| comma | **187** | `1,067 B` | 🟢 1 067 B |
| period (Spanish convention) | **57** | `11.357 B` | 🔴 **357 B** |
| none | 5 | `682 B` | 🟢 682 B |

🔴 **The failure is never random and never upward: the parser keeps the final group, so it always understates — `34 523 B` → 523 B is a 65× understatement.** The corpus is partly English and partly Spanish, so no single convention covers it.

🔴 **This bit four times inside this one pass.** Screening the shelves for FINDING 1's hollow class returned, in order: **374 → 375 → 56 → 12**. The first three runs were my own instrument misreading the separator, and every one of them *manufactured* hollow payloads out of perfectly canonical grants. Only the fourth — normalising comma, period, no-break space and thin space — gave the true residue of **12 distinct cells out of 565**.

🟡 **Had the first number been published, this pass would have reported a 374-row licence emergency that does not exist.** That is the same error class `p333` named when the grant column matched licence names inside other words — an instrument confidently measuring its own parsing bug.

🟢 **`ACTION ZK`: every instrument that reads a byte count from these shelves normalises `[,.    ]` first, and `gate-offline` gains a control that asserts `34 523 B`, `11.357 B` and `1,067 B` all parse to their true values.**

🟢 **And the residue vindicates the shelves.** Of the 12, five are the LGPL rows above (a *family* error, not a hollow payload), two are FINDING 1's genuine hollow pair, and one — `frappe/education`, `license.txt` at **19 B** reading *"License: GNU GPL V3"* — the shelves had **already** typed correctly as 🟡 *"declaration, not payload"* with the `P255` axis named. 🟢 **Where this base has looked at this class, it got it right.**

---

### 🟢 Added to the foundations tier this pass

| Repo | Grant — both channels | Activity, first-hand | Placed | Why it is a foundation |
|---|---|---|---|---|
| https://github.com/h5p/h5p-cli | 🟢 **MIT**, `master/LICENSE`, **1 066 B** · npm `h5p-cli` **MIT** | 🟢 **730 c · 39 a · 2013-11-22 → 2026-10-20 · 60 c in 2026** | 🟢 **EMEA — Norway** (`+0200(451) +0100(137)`) | 🟢 **The official H5P content-type development toolchain.** These shelves already carry `h5p/h5p-php-library` as a platform; the CLI is the piece that lets an engagement *build and test its own interactive content types* rather than only host the stock ones. 13 years, 39 authors |
| https://github.com/openpatch/hyperbook | 🟢 **MIT**, `main/LICENSE.md`, **1 069 B** · npm `@hyperbook/markdown` **MIT** | 🟢 **2 087 c · 10 a · 2022-03-08 → 2026-10-19 · 456 c in 2026** | 🟢 **EMEA — Germany** (`barkmin.eu` 1 079 c) | 🟢 Markdown → interactive courseware with an H5P-compatible element set. The widest real bench of any row promoted this pass, and the only new one with a multi-year history |
| https://github.com/missing-elements/h5p-offline-player | 🟢 **MIT**, `main/LICENSE`, **1 073 B** · npm **MIT** | 🟢 **288 c · 5 a · all 288 in 2026 · head 2026-10-19** | 🟢 **EMEA** (`+0300(280)`) | 🟡 Plays H5P in the browser **with no H5P server**. Narrow and young, but it is the only row on these shelves that removes the server requirement — the constraint that decides rural and low-connectivity deployments |

🔵 **An H5P cluster appeared on one channel in one pass** — `h5p/h5p-cli`, `otacke/h5p-theme-picker` and `missing-elements/h5p-offline-player`, all MIT, all new to a 3 031-slug corpus. 🟡 The honest reading: H5P tooling is **under-indexed by the search legs and well-indexed by the package registry**, because H5P ships as npm packages and its content types are not what a "top AI agents" list returns. This is `ACTION TJ`'s bound stated from the other side — the registry is strong on a **named standard** (`LTI`, `xAPI`, `SCORM`, `QTI`, `H5P`) and weak on a concept.

## Pass 335 · 2026-10-20 (eighth pass of this date) — five foundational rows from the package-registry channel, and the placement instrument this file uses is broken on every Apache and GPL row it touches

### 🟢 Promoted — permissive, placed, and active, every figure first-hand

| Repo | Grant, payload read first-hand | Activity, bare `--filter=blob:none` clone | Placed, and how | Layer |
|---|---|---|---|---|
| https://github.com/BrightspaceUI/core | 🟢 **Apache-2.0**, 10,421 B | 🟢 **9,598 c · 180 a · 1,020 in 2026 · 2019-03-06 → 2026-10-19** | 🟢 **North America** — `d2l.com(2,748)`, `-0400(4,432) -0500(1,612)` | Accessible component library for LMS front ends |
| https://github.com/Brightspace/test-reporting-node | 🟢 **Apache-2.0**, 10,421 B | 🟢 **1,129 c · 13 a · 358 in 2026 · head 2026-10-19** | 🟢 **North America** — `D2L.com(246)` | Test-evidence reporting |
| https://github.com/harvard-edtech/caccl | 🟢 **MIT**, 1,075 B, © **Harvard University** | 🟡 **655 c · 3 a · 27 in 2026 · 2018-11-02 → 2026-09-30** | 🟢 **North America** — institution named **in the grant** and on 3 commits | Canvas + LTI scaffold |
| https://github.com/freeCodeCamp/curriculum-helpers | 🟢 **BSD-3-Clause**, 1,524 B, © freeCodeCamp.org | 🟡 **578 c · 15 a · 23 in 2026 · head 2026-10-19** | 🔴 **UNPLACED** — `users.noreply.github.com(374)` dominates; offsets split `+0000(315) +0200(146) +0100(99)` | Challenge-testing helpers for a curriculum |
| https://github.com/christophblessing/quiz-recap | 🟢 **MIT**, 1,075 B | 🟡 **288 c · 5 a · 19 in 2026 · head 2026-09-11** | 🟢 **EMEA — Germany** — `hpi.de(1)`, `+0100(95) +0200(92)`; npm scope `@openhpi` | Quiz recapitulation component |

🟡 **`caccl` and `freeCodeCamp/curriculum-helpers` are carried with their bench stated, not hidden.** 27 and 23 commits in 2026 respectively: **maintained, not developed.** 🔵 For `caccl` that is the correct reading of an eight-year-old integration library against a stable API — **271 npm versions over eight years is continuity a star count does not show.**

### 🔴 The placement instrument is broken, and it fails by returning something that looks like an answer

**`ACTION TL` specifies: place a repository by the copyright HOLDER named in its licence payload, never by a maintainer's surname.** 🟢 **Correct, and this pass used it.** 🔴 **Measured over 29 payloads, it mis-fires on every long-form licence:**

| licence family | payload size | what the holder instrument returns | correct? |
|---|---|---|---|
| MIT / BSD-3 / ISC (short form) | 1,065 – 1,524 B | `Harvard University`, `freeCodeCamp.org`, `Christoph Blessing`, `Chris Hall`, `Vien Dinh` … | 🟢 **10 of 10** |
| **Apache-2.0** | 10,421 – 11,361 B | 🔴 **`owner or entity authorized by`** — a fragment of Apache's *definition of "Legal Entity"*. **Not a holder at all** | 🔴 **0 of 7** |
| **GPL-3.0 / AGPL-3.0** | 34,520 – 35,149 B | 🔴 **`Free Software Foundation, Inc. <https://fsf.org/>`** — the FSF's copyright on **the licence text**, not the project's | 🔴 **0 of 4** |

🔴 **The GPL case is the dangerous one: `Free Software Foundation, Inc.` reads exactly like a real institutional holder, and it would place every GPL row in this base in North America on the strength of the FSF's Boston address.** 🟢 **Nothing on these shelves is currently mis-placed that way** — the Apache and GPL rows this pass touched were placed on the commit channel instead — **but the instrument would have done it, and it is documented as the house method.**

🟢 **The repair, measured rather than proposed — a three-rung ladder:**

1. 🟢 **Short-form payload (< ~2.5 KB): read the copyright holder.** 10/10 this pass.
2. 🟡 **Apache-2.0: read `NOTICE`, not `LICENSE`** — that is where the Apache convention puts the holder. **Resolved 1 of 9** (`molecule-dev/molecule` → *"Molecule Dev, Inc."*). **Thin, and stated as thin.**
3. 🟢 **Otherwise fall through to the commit channel** (`%ae` domains + offsets), which resolved **8 of the remaining 8** and is already this base's strongest instrument.

🔴 **And the rule that matters more than the ladder: NEVER read a holder out of a long-form licence payload.** A long-form payload names the licence's steward, and the instrument cannot tell that from the project's owner. 🟢 **`ACTION ZE` registers a gate: any placement claim whose cited payload exceeds 2.5 KB is a defect unless it cites `NOTICE` or the commit channel.**

---


## Pass 334 · 2026-10-20 (seventh pass of this date) — two curriculum artefacts, one of them APAC-placed and shipping its own eval harness, and the licence that makes them usable is not the code licence

🔵 **This shelf's standing question about curriculum material is not "is it good" but "may a studio bill for a derivative of it".** `intel/trends.md` T12 has tracked a *commercially usable curriculum-artefact count* since p328 and the count has only ever moved by one. 🟢 **Two rows this pass, both read first-hand, and the interesting one is a content licence rather than a code licence.**

### 🟢 Promoted — every figure first-hand p334 (grant on `raw.githubusercontent.com`, activity from a bare `--filter=blob:none` clone)

| Repo | Grant, read first-hand | Activity, first-hand | Placed | Why it belongs here |
|---|---|---|---|---|
| **[Haozhe-Xing/agent_learning](https://github.com/Haozhe-Xing/agent_learning)** | 🟢 **MIT** — `main/LICENSE`, **1,068 B**, © 2025 Haozhe Xing | 🟢 **175 c · 11 a · 2026-03-13 → 2026-10-17 · all 175 commits in 2026 · 11 distinct authors in 2026** | 🟢 **APAC — China.** `qq.com(88) tencent.com(42)`; offsets `+0800(173)` | 🟢 **It is not only prose, which is what makes it a foundation rather than a reading list.** Read from the tree: `book.toml` **and** `book-en.toml` (bilingual mdBook), **plus `reference-agent/` with `src/reference_agent/evaluation/harness.py` and `data/eval_samples.jsonl`** — a runnable reference agent and an eval harness beside the curriculum. Covers LLM agents, RAG, tool use, memory, multi-agent, LangChain/LangGraph, **MCP** and agentic RL. 🟡 **21 commits carry `example.com` addresses** — placeholder authorship, recorded rather than smoothed over |
| **[kaveheng/GenAi-in-education](https://github.com/kaveheng/GenAi-in-education)** | 🟢 **CC BY 4.0** — `main/LICENSE`, **442 B**, © 2026 Kaveh Amouzgar and Omid Mirmotahari | 🟡 **12 c · 1 a · 2026-09-25 → 2026-09-26** | 🟢 **EMEA** — offsets `+0200(12)` | 🟢 **Open materials from real course implementations of generative AI in teaching and assessment, organised by year.** 🟢 **CC BY 4.0 is attribution-only — no share-alike** — which makes it the **first curriculum corpus on these shelves a studio may adapt into a client deliverable without the licence reaching the derivative.** 🔴 Compare the rows already here: `os-taxonomy` (**ODbL-1.0 + CC BY-SA 4.0**), `openedx-proposals` (**CC BY-SA 4.0**), `evaluators`' corpora (**CC BY-NC-SA 4.0** — the `NC` alone disqualifies it from paid work). 🟡 **Twelve commits over two days by one author: a small, new corpus. Cite the grant, bound the claim** |

### 🔵 The distinction this shelf should keep, because three of its own rows turn on it

🟢 **A permissive CODE licence and a permissive CONTENT licence are different questions, and curriculum work is decided by the second one.** Measured across the curriculum-artefact rows now on this shelf:

| row | code grant | content grant | may a studio adapt it into billable client material? |
|---|---|---|---|
| 🆕 `kaveheng/GenAi-in-education` | — (materials) | 🟢 **CC BY 4.0** | 🟢 **Yes — attribute** |
| 🆕 `Haozhe-Xing/agent_learning` | 🟢 **MIT**, 1,068 B | 🟢 MIT covers the book sources too | 🟢 **Yes** |
| `weecology/forecasting-course` | 🟢 MIT (code) | 🟡 **CC-BY** (materials) | 🟢 Yes — attribute, and keep the two halves separate |
| `withmarbleapp/os-taxonomy` | — (data) | 🔴 **ODbL-1.0 + CC BY-SA 4.0** | 🔴 **No — share-alike reaches the derived taxonomy** |
| `openedx/openedx-proposals` | — (prose) | 🔴 **CC BY-SA 4.0** | 🔴 **Cite, never vendor** |
| `learning-commons-org/evaluators` | 🟢 MIT | 🔴 **CC BY-NC-SA 4.0** | 🔴 **No — `NC` forbids the engagement itself** |

🟢 **The count T12 tracks therefore moves 3 → 5, and for the first time one of them is APAC-placed.** 🔵 Both new rows were placed on the **commit channel** — author email domain and UTC offset — not on the search channel, which is the only regional channel that has worked reliably on this base.

---

## Pass 333 · 2026-10-20 (sixth pass of this date) — three rows promoted out of a RANDOM sample of the silent class, and one of them is the instrument this KB has been hand-rolling for a hundred passes

🔵 **p332 probed the twelve most-sighted rows of its defect class and said plainly what was wrong with that: *"ranking by sightings selects for rows that were already interesting"*.** 🟢 **This pass drew the unbiased sample it prescribed** — `random.Random(333).sample(silent, 24)` over all **711** rows of the `silent` class — and probed all 24 first-hand. [`evidence/p333-silent-random-probe`](../evidence/p333-silent-random-probe.2026-10-20-p333.tsv).

🟢 **First result, and it is a good one: 24 of 24 resolve on `git ls-remote`.** The silent class is not padded with phantom slugs. 🔴 **Second: three rows are genuine misses — 3/24, 12.5%.** 🟡 **Scaled to the 711-row class that is roughly 89 rows, but the honest interval on a sample of 24 is wide (about 3–32%, so ~20–230 rows) and the estimate should be read as "tens, not hundreds, and not zero".**

### 🟢 Promoted — every figure first-hand p333

| Repo | Grant, read first-hand | Activity, first-hand | Why it belongs here |
|---|---|---|---|
| **[google/licenseclassifier](https://github.com/google/licenseclassifier)** | 🟢 **Apache-2.0** — `LICENSE`, 11,358 B | **249 c · 30 a · 2017-04-09 → 2026-02-18** | 🟢 **A licence-text classifier as a library: it compares text against an archive of known licence texts instead of grepping for a family name.** This is precisely the instrument this KB keeps rebuilding by hand — and precisely the defect `agents/top.md` records this pass, where `"mit" in row` graded a repository by its maintainer's first name. **Measured into `evidence/` 3 times and never delivered.** |
| **[yetanalytics/pedestal-oidc](https://github.com/yetanalytics/pedestal-oidc)** | 🟢 **Apache-2.0** — `LICENSE`, 11,357 B | **123 c · 5 a · 2022-01-11 → 2026-10-16** | 🟢 **OIDC relying-party middleware.** 🔵 **LTI 1.3 launch IS an OpenID Connect flow** — p331 promoted `lti-tool` for exactly that surface, and this is the auth substrate under it. |
| **[yetanalytics/re-oidc](https://github.com/yetanalytics/re-oidc)** | 🟢 **Apache-2.0** — `LICENSE`, 11,357 B | **70 c · 4 a · 2022-01-31 → 2026-10-16** | 🟢 **OIDC for the front end (re-frame).** The browser half of the same flow. |

🟢 **PLACED, and the placement is the same argument p331 made for `lti-tool`: look at the house, not the row.** **`yetanalytics` is the Yet Analytics xAPI house** — `yetanalytics/lrsql`, its SQL Learning Record Store, was verified this pass as 🟢 **Apache-2.0, 11,357 B, resolving on `git ls-remote`**. 🔵 **So the KB now holds, under one permissively-licensed roof, the LRS and both halves of the OIDC flow that an LTI 1.3 launch needs** — North America, and an org that ships rather than a lone author.

### 🟡 Named, not vendored — two rows that are reference material and are licensed as such

| Repo | Grant, first-hand | Activity | Disposition |
|---|---|---|---|
| [`openedx/openedx-proposals`](https://github.com/openedx/openedx-proposals) | 🟡 **CC BY-SA 4.0**, 15,998 B | **1,154 c · 123 a · head 2026-10-16** | The Open edX **OEP** process — how that community actually decides things. 🔴 **Share-alike on the prose: cite it, never vendor it.** |
| [`weecology/forecasting-course`](https://github.com/weecology/forecasting-course) | 🟡 **mixed** — CC-BY materials + MIT code, 25,315 B | **488 c · 8 a · head 2026-10-18** | A live university course, maintained. 🟢 **A real reference corpus for evaluating generated course material** against something a department actually teaches. |

### 🟢 ACTION ZA discharged in its first instalment — the disposition ledger exists

🔵 **p332's closing finding was that the shelves were mostly RIGHT to leave these rows off, and that the defect was that the refusal was never written down** — *"eight rows sat in `evidence/` with no disposition, so every pass re-discovers and re-probes them."*

🟢 **[`evidence/p333-disposition-ledger`](../evidence/p333-disposition-ledger.2026-10-20-p333.tsv) is that ledger**, one line per slug with the pass, the first-hand figures and the reason:

| disposition | rows | what it means for a later pass |
|---|---|---|
| 🟢 `PROMOTED` | 3 | on a shelf now |
| 🟡 `NAMED-NOT-CODE` | 2 | cite it, do not vendor it |
| 🟡 `UNREAD-WATCH` | 1 | `mercedesbenzforlyx/complete-anatomy` — **330 c · 2 a · head today**, and the owner name does not match the subject. **Read it before quoting it** |
| 🔴 `REFUSED-UNGRANTED` | 6 | no grant on a 7-path ladder — default copyright reserves all rights |
| 🔴 `REFUSED-BELOW-BAR` | 6 | one author, days of history |
| 🔴 `REFUSED-DORMANT` | 4 | 4–8 years silent |
| 🔴 `REFUSED-COPYLEFT` | 1 | `pdfmathtranslate` — strong project, wrong grant to embed |
| 🔴 `REFUSED-NOT-A-COMPONENT` | 1 | a curated list |

🔴 **24 of ~750 rows. The ledger is started, not finished, and it is NOT yet gated** — p332 asked for a gated sibling of the delivery audit and this pass delivered the data and the schema, not the gate. **Carried as `ACTION ZA` in [`intel/open-gaps.md`](../intel/open-gaps.md), stated as partial rather than closed.**

### 🔴 The most active ungranted row in the sample, recorded because it is a recurring shape

**[`emmanuel-johnson/launch-point-backend`](https://github.com/emmanuel-johnson/launch-point-backend) — 201 commits, all in 2026, one author, head 2026-10-19, and NO grant on any of seven candidate paths.** 🔵 **Six of 24 sampled rows are in this state: genuinely active, genuinely unusable.** **Default copyright reserves all rights, so activity is not availability** — and for a studio the cheap move is an issue asking the author to add a licence, not a fork.

---

## Pass 332 · 2026-10-20 (fifth pass of this date) — one promotion, and it was invisible for fifteen sightings because this file's grant ladder leads with the channel its subject does not use

🟢 **`h5p/h5p-interactive-video` is promoted to this file.** It is the one genuine miss in the delivery audit's defect class (see `agents/top.md` p332), and the reason it sat unplaced since **p195, 2026-10-14, across 15 sightings**, is worth more than the row itself.

| | measured first-hand p332 |
|---|---|
| repo | https://github.com/h5p/h5p-interactive-video |
| grant | 🟢 **MIT** — and there is **no licence file**. `package.json` carries `"license": "MIT"`, and the README carries the **full MIT text** under `## License` |
| activity | 🟢 **2,447 commits · 115 authors · head 2026-10-02 · 37 commits in 2026** |
| version | `1.25.0` (`package.json`, read p332) |
| what it is | The Interactive Video content type for H5P: in-video questions, branching, bookmarks, summaries. The most active and most broadly authored repository in the H5P org |
| layer | 🟢 **Interactive content — the authoring surface an agent generates INTO** |

🔴 **115 authors is the largest contributor bench on these shelves.** For comparison, the agent shelf's widest row is `OATutor` at 27, and `lti-tool` — p331's promotion — has 6.

### 🔴 Why fifteen sightings were not enough: the ladder stops at channel 1

**This KB's grant ladder tries the licence FILE first. For the H5P org that channel is nearly blind.** p332 censused ten H5P repositories across three channels, every cell first-hand — [`evidence/p332-h5p-grant-channels.2026-10-20-p332.tsv`](../evidence/p332-h5p-grant-channels.2026-10-20-p332.tsv):

| channel | repos where it answered |
|---|---|
| 1 — licence **file** (`LICENSE`, `LICENSE.txt`, `LICENSE.md`, `COPYING`) | 🔴 **2 of 10** |
| 2 — **manifest** (`package.json` / `composer.json` `"license"`) | 5 of 10 |
| 3 — **README body** (licence text carried in prose) | 4 of 10 |

🔴 **Eight of ten H5P repositories have no licence file, and seven of the eight grants found are invisible to channel 1.** A ladder that leads with the file channel and does not fall through reads this org as almost entirely ungranted. **It is not ungranted; it is differently published.** 🟢 **This is the same class as p322's `oeh-search-frontend` finding (no file, and no `license` key either) — but the opposite outcome, and that is the point: the absence of a file is not evidence of an absent grant. It is evidence that the file channel was the wrong question.**

### 🟢 And the census found something the shelves have been understating

🔴 **H5P is not one licence. The split follows the renderer/content boundary exactly:**

| tier | repos | grant |
|---|---|---|
| PHP core / renderer | `h5p-php-library`, `h5p-editor-php-library` | 🔴 **GPL-3.0** |
| content types | `h5p-interactive-video`, `h5p-course-presentation`, `h5p-drag-question`, `h5p-accordion` | 🟢 **MIT** |
| content types, README channel only | `h5p-question-set`, `h5p-multi-choice`, `h5p-blanks` | 🟡 **MIT**, stated in the README and nowhere else |
| unclear | `h5p-core` | 🔴 **no grant on any of the three channels** — its README is 14 bytes |

🟢 **`h5p-accordion` carries a real MIT `LICENSE.txt`, 1,073 B, *Copyright (c) 2015 Joubel*** — so the MIT tier is not an artefact of manifest metadata; it is the holder's stated intent, published inconsistently.

🟢 **What this changes for a studio, concretely:** `verticals/solutions.md` has said a studio may author *"H5P content JSON with an agent; the renderer stays untouched, so GPL stays contained."* **That is true and it understates the surface by a tier.** A studio may **fork and modify a content type under MIT** — a code surface, not a data one — while leaving the GPL-3.0 renderer alone. 🟡 **The caveat to carry to a client: the grant is per repository and the org is not uniform.** Read the content type you intend to fork. Three state MIT only in the README, and `h5p-core` states nothing anywhere.

### 🟡 Measured this pass and honestly below the bar — recorded so no future pass re-spends the probe

**These are the rest of the delivery audit's defect class. Full figures in [`evidence/p332-defect-probe.2026-10-20-p332.tsv`](../evidence/p332-defect-probe.2026-10-20-p332.tsv); the verdicts are in `agents/top.md` p332 and are not repeated here.** 🔴 **`davemckain/qtiworks` deserves the one line it gets:** BSD, *© 2014 University of Edinburgh*, **2,073 commits** — the most substantial QTI engine this KB has measured — and its README's first line reads *"This project is no longer supported and is going to be closed in early 2023."* **Substantial and unusable. Size is not liveness, and a maintainer's own README outranks a commit count.**

🔵 **`sagorbrur/bnlp` (MIT, 541 c · 10 a · head 2026-04-01) is alive and was already named on three shelves.** It is a Bengali NLP substrate rather than an education tool; its place here, if any, is as low-resource-language groundwork for an **APAC** engagement, and it is not promoted to a row on that basis.

---

## Pass 331 · 2026-10-20 (fourth pass of this date) — this file's liveness column is measured on the wrong channel for half its rows, and a replacement for its dead recommendation was in `evidence/` all along

🔴 **p330 fixed this file's worst defect and introduced a subtler one.** It replaced the bare commit count with the triple `(commits, authors, last_commit)` — correct, and it is how `pylti1.3` was caught. 🔴 **But the triple reads the *citing* channel, and more than half the rows in this file are **libraries**, whose liveness event is a **release**, not a commit.**

🟢 **This KB built the right instrument at pass 24 and has not pointed it at this file since.** `compose/code/registry-recency-channel/README.md`, 2026-10-07, in its own words: *"citing tier → head commit date → any commit, including a typo fix in a README; installed tier → latest release upload → a **deliberate publication**. ⚠️ The two numbers are not interchangeable."*

### 🔴 The two-channel measurement, run this pass — and the row it exonerates

| repo | `git`: newest tag / head | registry: latest release | single-channel verdict | 🟢 **two-channel verdict** |
|---|---|---|---|---|
| https://github.com/Cvmcosta/ltijs | 🔴 newest tag **`v5.9.5`, 2024-05-01** · head 2026-10-13 | 🟢 **`ltijs` 7.0.7, 2026-10-06** | 🔴 *"abandoned 2.4 years"* | 🟢 **ALIVE — released two weeks ago** |
| https://github.com/dmitry-viskov/pylti1.3 | 2022-11-21 | 🔴 **`PyLTI1p3` 2.0.0, 2022-11-20** | DEAD | 🟢 **DEAD — p330 confirmed, to the day, on a second channel** |
| https://github.com/openfun/django-lti-toolbox | 🔴 2024-11-14 | 🔴 **2.0.0, 2024-07-15** | DEAD | 🟢 **DEAD — both channels agree** |
| https://github.com/Liberate-Labs/ltikit-sdk | 2026-07-10 · newest ref dependabot 2026-10-07 | 🔴 **NO PACKAGE — does not resolve on npm** | "alive-ish" | 🔴 **UNPUBLISHED** |

🔵 **The first two rows are the whole argument.** 🔴 **One method called both repositories abandoned. It was wrong about `ltijs` by two and a half years and right about `pylti1.3` to the day — and it had no way to tell which was which.** 🟢 **The registry channel separates them in one call each.** 🔴 **`ltikit-sdk` fails the other way: alive on the git channel, nonexistent on the registry — which is the axis a client's build sits on.**

🟢 **Rule now standing for this file: a row that ships a package carries BOTH dates, or it carries no liveness verdict at all.** **Tags are a convention a maintainer can silently stop honouring; a release is an event.**

### 🟢 The integration tier, re-cut — and the replacement this file has needed since p319

🔴 **This file recommended `pylti1.3` four times as *"the repo that gets your agent into the client's existing LMS."* p330 withdrew it. 🔴 It then named `ltikit-sdk` the first permissive non-Python option — which `evidence/p232-new-rows.2026-10-16-p232.tsv` line 17 had already disproved on 2026-10-16.**

| repo | grant, first-hand p331 | git, first-hand p331 | registry, first-hand p331 | verdict |
|---|---|---|---|---|
| **https://github.com/lti-tool/lti-tool** | 🟢 **MIT**, 1,077 B, *© 2025-present James Joplin* | **346 c · 6 a · 2026-10-19** · 🟢 **235 c in 2026 by 6 a** | 🟢 **`@lti-tool/core` 1.3.1 — 2026-10-20, today.** 31 releases since 2025-10-02 | 🟢 **RECOMMENDED — the integration row this file was missing.** Complete LTI 1.3 Advantage surface read in code: launch · AGS · NRPS · Deep Linking · Dynamic Registration · JWKS. 49 core src files, 14 test files. 🟢 **Two dependencies: `zod`, `jose`.** Pluggable storage: `memory`/`postgresql`/`mysql`/`dynamodb`/`d1`/`hono` — conventional **and** edge. 🟢 **North America, institutionally — 161 of 346 commits at `-0400`, 62 at `-0500`, and `longsight.com` (28 c) is Longsight Inc., a US Sakai/Tsugi host this KB already holds as `LongsightGroup/qti3`** |
| https://github.com/Cvmcosta/ltijs | 🟢 **Apache-2.0**, 11,361 B | 575 c · 17 a · 2026-10-13 | 🟢 **`ltijs` 7.0.7 — 2026-10-06** | 🟡 **ALTERNATIVE, with the risk stated.** The mature choice. 🔴 **51 c in 2026 by only 2 authors**; head is a dependabot merge; **90 commits from `ltiaas.com`, the maintainer's commercial hosted product.** 🟢 **LATAM — Brazil: 429 of 575 commits from one `yahoo.com.br` address** |
| https://github.com/tsugiproject/tsugi | Apache-2.0 | **4,012 c · 47 a · 2026-10-19** (p330) | — (PHP, no npm/PyPI row) | 🟢 **ALIVE.** The LTI *platform* side, 486 commits in 2026 |
| https://github.com/jcputney/scorm-again | MIT | 1,243 c · 14 a · 2026-10-20 (p330) | 🟢 **`scorm-again` 3.4.6 — 2026-10-08** | 🟢 **ALIVE on both channels.** The SCORM route into legacy courseware |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 🔴 2022-11-21 | 🔴 **2022-11-20** | 🔴 **DEAD — 47 months, two channels. Do not propose it** |
| https://github.com/openfun/django-lti-toolbox | MIT | 🔴 2024-11-14 | 🔴 **2024-07-15** | 🔴 **DEAD — two channels** |
| https://github.com/Liberate-Labs/ltikit-sdk | 🟢 MIT, 1,063 B | 38 c · **1 a** · 2026-07-10 | 🔴 **UNPUBLISHED** | 🟡 **Watch list only.** Vendored-source dependency; ownership handover unresolved |
| https://github.com/Godmartinz/Node-LTI-1.3-library | — | 🔴 125 c · 6 a · default **2019-08-02** | — | 🔴 **DEAD — seven years.** Offered by the search channel this pass; recorded so it is not offered again |

### 🟢 The pedagogy and integrity tier, dated on the registry channel this pass

| repo / package | grant | latest release, first-hand p331 | why it is a foundation |
|---|---|---|---|
| `@dodona/dolos` — https://github.com/dodona-edu/dolos | 🟢 **MIT** | 🟢 **2.10.0 — 2026-10-19** | **P11's integrity engine with a maintaining university behind it** (Ghent). Released yesterday |
| `nbgrader` | 🟢 **BSD-3-Clause** | 🟢 **0.9.6 — 2026-09-30** | The `.ipynb` autograding incumbent; the tier `jupyterquest` joins |
| `otter-grader` | 🟢 **BSD-3-Clause** | 🟢 **7.0.0 — 2026-07-27** | A major version this year; the Berkeley-lineage autograder |
| https://github.com/CAHLR/OATutor | 🟢 **MIT** | — (not packaged) | 1,045 c · **27 a** · 2026-10-16 (p330) — the healthiest contributor base in this file's pedagogy tier |

🟢 **Control, stated because a channel that cannot fail proves nothing:** `bogus-control-pkg-p331-zz` → **NO-RESOLVE** on npm; `bogus-control-p331/not-a-real-repo-zz` → **NO-REF** on git. **Both channels discriminate.**

🔵 **What is still not measurable here, stated plainly rather than left silent:** 🔴 **star counts and fork counts.** `api.github.com` has been 403 since p37, and this session's `mcp__github__*` tools — new, and the first time this KB has had them — **refuse every repository not attached to the session** (*"Allowed repositories: gmilano/globant-kb, gmilano/education-kb"*). 🔵 **Those are two different refusals with two different causes, and no future pass should record them as one blocked channel.** **Popularity remains unmeasurable; liveness and grant are now both measurable twice over.**

---

# Foundational repos — education

## Pass 330 · 2026-10-20 (third pass of this date) — the integration tier re-measured on the git channel, and this file's standing LTI recommendation is dead

🔴 **No new foundation for a third consecutive pass. What this pass did instead is worth more: it ran the activity channel across this file's *integration* tier, and found that the row this base has recommended four times for getting an agent into a client's LMS has not been touched since November 2022.**

🔵 **The method point first, because it is why this went unseen for eleven passes.** This file's integration rows carry **commit counts** — `pylti1.3`, *"178 commits"*, recorded at p319 and re-verified at p319. 🔴 **A commit count is a lifetime total. It cannot distinguish a project that wrote 178 commits last year from one that wrote them before 2023 and stopped.** 🟢 **p329 established the triple — `(commits, authors, last_commit)` — for the agent tier. The foundations tier is where the scalar did the most damage, because an integration library is precisely the kind of artefact a studio pins and forgets.**

### The rows — the integration tier, measured first-hand on every ref, not just the default branch

| repo | grant | commits | authors | last commit, **any ref** | verdict |
|---|---|---|---|---|---|
| https://github.com/tsugiproject/tsugi | Apache-2.0 | **4,012** | **47** | 🟢 **2026-10-19** | 🟢 **ALIVE — 486 commits in 2026.** And its LTI version question is now answered: see below |
| https://github.com/jcputney/scorm-again | MIT | **1,243** | **14** | 🟢 **2026-10-20 — today** | 🟢 **ALIVE.** The SCORM route into legacy courseware is maintained |
| https://github.com/CAHLR/OATutor | MIT | 1,045 | **27** | 🟢 2026-10-16 | 🟢 **ALIVE.** 27 authors is the healthiest contributor base in this file's pedagogy tier |
| https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 467 | 5 | 🟢 2026-10-16 | 🟢 **ALIVE.** p317's architectural find, still moving |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 178 | **16** | 🔴 **2022-11-21** | 🔴 **DEAD — forty-seven months.** Newest ref of any kind is tag `2.0.0`, same date |
| https://github.com/openfun/django-lti-toolbox | MIT | 34 | 6 | 🔴 **2024-11-14** | 🔴 **DEAD — p325's figure, confirmed to the day** |
| https://github.com/Liberate-Labs/ltikit-sdk | 🟢 **MIT** (1,063 B, first-hand p330) | 38 | **1** | 🟡 **2026-07-10** | 🟡 **NEW — complete surface, single author, quiet since an ownership handover.** Graded in full in `agents/top.md` |

### 🔴 `pylti1.3` — the recommendation this file has to withdraw

**This file's row says: *"LTI 1.3 Advantage tool implementation, 178 commits. Covers Deep Linking, Assignment & Grade Services, Names and Roles, Course Groups, Submission Review and Data Privacy Launch — the whole Advantage surface. This is the repo that gets your agent into the client's existing LMS."*** 🟢 **Every capability claim in that sentence is still true.** 🔴 **The caveat attached to it — *"still no published release — pin a commit"* — is the wrong caveat, and it reads as the opposite of the truth.**

**"No published release" describes a young project.** 🔴 **Sixteen authors, 178 commits, and nothing on any branch or tag since 2022-11-21 describes an abandoned one.** Its final substantive commit is literally *"Support Python 3.11 (#106)"* — **and `artcc/freelingo`, added to `agents/top.md` in this same pass, ships on Python 3.14.** 🔵 **A library whose newest supported runtime is three releases behind the artefacts that would consume it is not a dependency a studio pins; it is a fork a studio inherits.** **Scope it that way or do not scope it.**

### 🟢 Tsugi — and what it does to the risk this file has carried for four passes

**p323 closed the Tsugi version question with a negative answer, from the README. The tree answers it positively.** `lib/src/Util/LTI13.php` · `ims/ags/route.php` + `lib/src/Controllers/Ims/Ags.php` + `lti/ags.php` · `ims/nrps/route.php` + `lib/src/Controllers/Ims/Nrps.php` · `DeepLinkRequest.php` / `DeepLinkResponse.php` — 🟢 **with `lib/tests/Util/LTI13Test.php` and `lib/tests/Services/Outbound/Lti13TestLaunchTest.php` to test them.** Its own commit of 2026-10-18 confirms the other half: *"Note that upward is set from an LTI 1.1 result."* **Both generations, in shipping code, under Apache-2.0.**

🔴 **The method lesson, recorded because this file made the error and not the search channel: p323 answered a question about code by reading documentation, and published a false negative that stood for seven passes.** 🟢 **The standing rule becomes: a capability question is answered from the tree. `ls-tree -r` costs one clone this environment already pays for, and it is the same channel that produces the activity triple — one fetch answers *is it alive* and *what does it implement* at once.**

🟡 **One qualifier that belongs with the promotion: Tsugi's 486 commits in 2026 come from three authors, overwhelmingly Charles Severance.** **Complete, maintained, permissive, and a bus factor near one.**

### 🔵 What the tier looks like once it is read as a whole, and it is not what this file has been saying

**This base has been describing a dying LTI layer — *"the permissive LTI plumbing exists, is published by a national public operator, and has sat untouched"*.** 🟢 **That is true of Python and false of PHP, and this file has never stated it that way.**

| ecosystem | state | what a bid can actually rest on |
|---|---|---|
| **PHP** | 🟢 alive, complete, tested | `tsugi` — the one living permissive LTI implementation here |
| **Python / Django** | 🔴 **both options dead** | 🔴 **nothing.** `pylti1.3` 2022, `django-lti-toolbox` 2024 |
| **JS / TS** | 🟡 new, complete, one author | `ltikit-sdk` — fork and pin |
| **SCORM (adjacent)** | 🟢 alive, committed today | `scorm-again` — the legacy-courseware route LTI does not reach |

🔴 **The consequence to carry into scoping, and it reverses this file's standing advice: if a client requires LTI and the delivery stack is Python, there is no maintained permissive library to point at. The honest options are to port, to fork, or to put the LTI boundary in a PHP or TS service and keep Python behind it.** 🟢 **Say it in the bid. It is a two-week architectural fact, and discovering it in week six is what it costs otherwise.**

### 🟡 One correction to a claim this base published about an agent-tier row

**`zhangl1001/civil-ai` was recorded at p323 as *"the highest-starred education agent pushed since 2026-10-01"*.** 🔴 **Measured first-hand this pass: the default branch's last commit is 2026-08-23.** Eight refs are newer and **every one of them is a `dependabot/` branch** (`source-map-js`, `capacitor/ios`, `brace-expansion`, `dompurify`, `xmldom`, `actions/checkout`). 🔵 **"Pushed since" was reading repository-level push activity that bots generate. The project's humans have been quiet for two months.** **The row stands — the architecture finding in it is unaffected — but the recency claim attached to it does not.**

### 🔴 The verification surface of this pass, recorded because it bounds every claim above

`raw.githubusercontent.com` 🟢 **200** · **git smart-HTTP** 🟢 **200** (all refs, trees, author domains, commit offsets) · `gitlab.com/api/v4` 🟢 **200** — **and instrumented in this repository since 2026-10-06, a fact p329 declared untested; see `agents/top.md`** · `github.com` 🔴 403 · `api.github.com` 🔴 403 · **13 self-hosted and alternative forges 🔴 000 each**, closing pass 23's pre-registered action B with a measured negative. **No star count in this pass is verified; every ★ here is carried or `n/v`.**


## Pass 329 · 2026-10-20 (second pass of this date) — no new foundation for a second pass, and the activity channel re-grades three rows this file already holds

🔴 **No new foundational repository. Second consecutive pass, and stated as a measured result rather than as silence.** The prescribed
foundations query (`open source platform education ERP CRM MIT Apache`) returned **OpenEduCat** (held), **Apache OFBiz** (not education)
and **CK-ERP, a 2010 SourceForge project** — the query is now reaching 16-year-old material. 🟢 **The pass's value to this file is
therefore not supply. It is that every row this file holds could be re-graded on an axis it has never carried**, using a channel that
was open the whole time (see `repos/trending.md` p329 for the channel's provenance and the credit it owes to p229 and p319).

### 🟢 The refinement that has to come first, because without it this measurement would damage three good rows

**The crude rule — "rank on commit count" — is wrong, and this file is where it would have done the damage.**

| repo | commits | the crude rule would say | what it actually is |
|---|---|---|---|
| `AI-for-Education/pedagogy-benchmark` | **5** | abandoned | 🟢 **A benchmark dataset.** 1,143 questions from Chile's teacher-qualification exams. **A finished dataset does not accrue commits**; that is what finished means |
| `learning-commons-org/knowledge-graph` | **44** | marginal | 🟢 **A curated standards corpus**, 6 authors, last touched 2026-10-14 |
| `anthropics/k12-teacher-skills` (in `agents/top.md`) | **4** | abandoned | 🟢 **A four-skill bundle**, 3 authors, last touched 2026-10-13 |

🟢 **So the rule, in its mature form: compare a repository's activity against its ARTEFACT KIND, never against the shelf's maximum.**
A **platform** with 40 commits is dying; a **benchmark** with 5 is done; a **skills bundle** with 4 is a skills bundle.
🔵 **The triple `(commits, authors, last_commit)` is the measurement; the artefact kind is the denominator.** Without the denominator
this channel is a machine for deleting good rows, and this file would have been its first casualty.

### The rows

| repo | grant (as held, re-read pass noted) | commits · authors · first → last, **first-hand p329** | artefact kind | region | p329 verdict |
|---|---|---|---|---|---|
| https://github.com/dodona-edu/dolos | 🟢 **MIT** (1,083 B, p328) | **3,859 · 25 ·** 2019-06-23 → **2026-10-19** | Platform (plagiarism/similarity) | **EMEA** (KU Leuven) | 🟢 **The strongest foundation in this file on every axis: seven years, 25 authors, a commit yesterday.** This settles the premise p324 retracted — *"there is still no credible open source academic-integrity project"* — not as an argument but as a measurement |
| https://github.com/learning-commons-org/evaluators | 🟡 Four-way split (code **MIT**; prompts + settings **CC BY 4.0**; *CLEAR* and *PERSUADE 2.0* corpora **CC BY-NC-SA 4.0**) | **289 · 13 ·** 2025-09-22 → **2026-10-19** | Library | **North America** | 🟢 **LIVE, commit yesterday.** 🔵 **And p328's carried figure of "289 commits" is now confirmed FIRST-HAND, exactly.** The commercial boundary is unchanged and still in the data, not the code |
| https://github.com/open-edge-platform/education-ai-suite | 🟢 **Apache-2.0** (11,350 B, p328) | **453 · 33 ·** 2025-09-29 → **2026-10-19** | Platform (Intel) | **Global** | 🟢 **LIVE**, 33 authors, commit yesterday |
| https://github.com/learning-commons-org/knowledge-graph | 🟡 **Licensed per dataset and in some cases per download**, across three access tiers (Open / Open + Gated / Gated); no licence in the sidebar; `LICENSE.md` states the distributor *"doesn't consolidate those into a single license for your build"* | **44 · 6 ·** 2025-09-17 → 2026-10-14 | Curated standards corpus | **North America** | 🟢 **LIVE.** 🔴 **The licence remains a ROW-LEVEL field, not a repository attribute — re-read this pass and unchanged. *"Is this repo MIT?"* is still not a sufficient question here** |
| https://github.com/autolab/Autolab | 🟢 **Apache-2.0** (11,323 B, p328) | **2,179 · 84 ·** 2014-10-25 → **2025-10-20** | Platform (CMU) | **North America** | 🔴 **STALE BY EXACTLY ONE YEAR TODAY.** 84 authors and 11 years of history, and the last commit is 2025-10-20. **A mature, widely-deployed autograder that went quiet — carry it as a proven design to read, not as a dependency to adopt without a maintenance plan** |
| https://github.com/datakind/student-success-tool | 🟢 **MIT** (1,080 B, p328) | **3,015 · 25 ·** 2024-10-10 → **2025-09-08** | Analytics toolkit | **North America** | 🔴 **STALE 13 MONTHS.** 3,015 commits of real work, then silence. **Same caveat: read it, plan to own it** |
| https://github.com/AI-for-Education/pedagogy-benchmark | 🟢 **MIT** (1,063 B, p328) | **5 · 1 ·** 2025-06-24 → 2025-10-15 | **Benchmark dataset** | **LATAM** | 🟢 **HELD AT FULL VALUE — see the refinement above.** A finished benchmark does not accrue commits. Still the only artefact in this KB that tests whether a model knows *pedagogy*, sourced from a LATAM ministry's own licensing exam |
| https://github.com/devissaputra/curriculum_knowledge_graph | 🟢 **MIT** (p327) | **27 · 1 ·** 2026-09-25 → **2026-09-26** | Schema + validator | 🔴 **UNPLACED** | 🟡 **Two days of commits by one author.** The schema and its 36 passing tests are real and small enough to read in an afternoon — **adopt the design, vendor the code; do not depend on the repository** |

### 🔵 One more thing the measurement settled, and it cuts in this base's favour

**Two commit figures this base had been carrying in prose turned out to be exactly right:** `Orenda-Project/rumi-platform`'s
*"847 commits on 18 stars — the commit count is the signal"* measured **847**, and p328's *"289 commits"* for `evaluators` measured
**289**. 🟢 **So when this KB wrote down a commit count it wrote down a true one.** 🔴 **The figures that drifted were the star counts**
— solicited, inflated, and the subject of this base's trend 11. **The channel that died was the unreliable one. That is the whole
story of the last two passes in one line.**

## Pass 328 · 2026-10-20 (first pass of this date) — this file passed the shelf audit, one row that never arrived, and the grant channel is all that is left

🟢 **The audit first, because it is the pass's headline and this file is the half that works.** p327 prescribed re-grepping every `PROMOTE-*` verdict in `evidence/` against the shelf files. **Run against the *shelf region* rather than the filename, this file passes and `agents/top.md` failed**: all five p296 foundations promotions sit inside a `### The rows` ledger, and **this file's convention is that the per-pass ledger *is* the shelf**, so a row cut into a pass section is a row a reader finds. 🔵 **`agents/top.md` carries a single canonical `## The table` instead, and p327's rows landed in the commentary above it — invisible to anyone reading the table.** p328 cut them in. **The lesson for this file is to keep its convention and say so in the open, which is what this paragraph is for.**

🔴 **One row was graded for this file and still never arrived — and it is the most load-bearing one outstanding.** `learning-commons-org/evaluators` has been on this KB's trending channel since **p119**, was licence-read byte-for-byte twice, was written up at length in `agents/top.md` at p327 — **and has never been a foundations row**, which is where an evaluation layer belongs. It is cut below.

### The rows

| Repo | Licence | ★ | Checked | Region | Layer | Why it is foundational |
|---|---|---|---|---|---|---|
| https://github.com/learning-commons-org/evaluators | 🟡 **Four-way split, 1,615 B, re-read p328: code **MIT** · prompts + settings **CC BY 4.0** · *Annotated CLEAR Corpus* **CC BY-NC-SA 4.0** · *Annotated PERSUADE 2.0* **CC BY-NC-SA 4.0** | 86 (carried p327) | **p328** | **North America** | 🟢 **Evaluation — pedagogical quality, as a library** | **19 evaluators in five families, scoring model output "through the lens of learning science":** **Text Complexity** (8 — grade-level appropriateness, background-knowledge demands, vocabulary complexity, sentence structure, meaning directness, purpose clarity, organizational structure, reference-knowledge demands) · **Feedback** (7 — strength acknowledgment, revision actionability, student-response specificity, revision accuracy, revision manageability, **withholding answers**, tone appropriateness) · **Graphics** (2, early access) · **Academic Standards Alignment** (1, math) · **Durable Skills** (1, critical thinking). Python **and** TypeScript SDKs: `pip install learning-commons-evaluators`, `npm install @learning-commons/evaluators`. 🟢 **This file's own p319 finding was that the sector's quality metric — LLM-judged helpfulness — is not a pedagogy signal. This is the first library that measures the thing instead, and the code is MIT.** 🔴 **The commercial boundary is in the data, not the code: the expert-annotated CLEAR and PERSUADE 2.0 corpora are CC BY-NC-SA 4.0. Ship the evaluators and their prompts in a paid product; do NOT ship those corpora and do NOT use them to validate a commercial model release. Re-annotate against client data, or validate in-house and keep the corpus out of the deliverable** |

### 🟢 One platform-tier grant confirmed, filed in `verticals/solutions.md`

**`OpenOLAT/OpenOlat` is Apache-2.0, read first-hand this pass** — `master/LICENSE`, 10,982 B. This file has carried OpenOLAT for passes as *"the crack in the copyleft-platform rule"* on secondary evidence; **the grant is now byte-verified, and it resolves on `master`, not `main`** — the same branch hazard p296 attached to `autolab/Autolab`. 🔵 **Second instance of that hazard in this KB, so it is a probe rule now, not an anecdote: always probe `master` before concluding a platform has no licence file.**

### 🔴 The verification surface of this pass, recorded because it bounds every claim above

**This pass could read shipped bytes and nothing else.** `raw.githubusercontent.com` → **200**. 🔴 **`github.com` (rendered repo page) → 403. `api.github.com` → 403.** `arxiv.org`, `huggingface.co`, `unesco.org`, `codeberg.org` → **no connect at all**.

🔵 **p327 read licences off the rendered GitHub sidebar; p328 cannot see the sidebar.** So: **grants, byte counts, file paths, code and README text above are first-hand; stars, forks, commit counts, topics and descriptions are unobtainable**, and every star figure above is marked `carried` with the pass that measured it. 🟢 **The channel that survived is the one the rights analysis runs on — which is the only analysis in this file a client can be billed for.**

## Pass 327 · 2026-10-19 (thirteenth pass of this date) — sixty-four rows, and six of them were graded for this file a day ago

**Six rows added — sixty-four total. Every licence below was re-read first-hand on the `raw` channel this pass**, over the seven-filename probe space across `main`, `master` and `develop` — **not carried from p296**, whose verdicts these rows execute.

🔴 **Why this pass promotes instead of sweeping.** `evidence/p296-promotion-gap.2026-10-18-p296.tsv` graded ten repositories and marked **five of them for this file** (`PROMOTE-to-foundations`, one `-with-grade-note`). **A `grep` of all four shelf files finds 0 of 10 present.** p296 did the hard part — found them, read the licences, placed them by region — and the rows were never cut. 🔵 **The regional spread of that unexecuted backlog is the part that should sting: APAC 3, North America 3, EMEA 1, LATAM 1, Global 1, unplaced 1. This KB's regional balance problem was already solved on disk and undelivered.**

### The rows

| Repo | Licence | ★ | Checked | Region | Layer | Why it is foundational |
|---|---|---|---|---|---|---|
| https://github.com/learning-commons-org/knowledge-graph | 🟡 **Split, and the split is the point: code MIT; data licensed *per dataset and per download*.** `LICENSE.md` re-read this pass at 5,789 B. **Open** → typically **CC BY 4.0**, some **CC0**. **Open + Gated** → mixed within one dataset. **Gated** → no open licence, publisher approval required. 🔴 GitHub's sidebar **names no licence at all** and the Languages panel is empty | **161** | p327 | **North America** | **Curriculum data — the US-standards spine** | **The answer to the question p326 left open.** Marble (`os-taxonomy`) gave this KB a multi-national spine covering the UK, CCSS and the IB; **this one is the United States at state granularity** — US academic standards for Math, ELA, Social Studies and Science with **state-to-CCSS crosswalks carrying a `jaccard` similarity score**, Math + ELA **learning components**, the **Math Coherence Map** (learning progressions), **WIDA ELD Standards Framework**, **XQ Competencies**, **Carnegie Skills Progressions** (Carnegie Foundation + ETS), the **Eedi Misconceptions Graph**, **IM® v.360** curriculum and **OpenSciEd**. Companion skills claim coverage of **academic standards across all 50 states**. Five access paths: Explorer UI · agent plugins · local `nodes.jsonl` + `relationships.jsonl` · REST API · **MCP server** (`https://kg.mcp.learningcommons.org/mcp`). 23 forks, 44 commits, **v1.15.0 released 2026-10-14** · **Use it for:** the standards spine, the crosswalks, and the misconception bank behind a formative-assessment generator |
| https://github.com/dodona-edu/dolos | 🟢 **MIT** — `main/LICENSE`, 1,083 B, *MIT License* | 352 (p296) | p327 | **EMEA** | **Academic integrity — source-code plagiarism** | **Ghent University / Team Dodona.** 48 forks, **3,838 commits** — the deepest commit history of any row promoted this pass. 🔵 **This KB already holds `JPlag`, `jieplag` and `JPlag`-adjacent tools; `dolos` is the one with a maintaining university behind it and a European institutional deployment** · **Use it for:** the integrity layer in any EMEA higher-ed engagement, where it is a procurement question rather than a feature |
| https://github.com/autolab/Autolab | 🟢 **Apache-2.0** — `master/LICENSE`, 11,323 B, genuine Apache text. 🔴 **Licence resolves on `master`, not `main`** — the grade note p296 attached to this row | 808 (p296) | p327 | **North America** | **Autograding + course management** | **Carnegie Mellon University** (README: initially developed by students at CMU). 234 forks, 2,179 commits. 🔵 **The most production-hardened autograder in this KB that is not a Jupyter add-on** — compare `nbgrader` and `otter-grader`, both notebook-bound · **Use it for:** the assessment-execution layer under an AI feedback agent, so the agent advises and the grader adjudicates |
| https://github.com/datakind/student-success-tool | 🟢 **MIT** — `main/LICENSE.md`, 1,080 B. 🟡 p296 records the default branch as `develop`; the grant resolves on `main` | 8 (p296) | p327 | **North America** | **Retention / early-warning analytics** | **DataKind**, with **John Jay College (CUSP)** named in the README and **Google.org** as funder. 2 forks, **3,015 commits** on 8 stars 🔵 **— a star count that measures its audience, not its maturity.** · **Use it for:** the persistence-and-completion model that buyers are now asking for evidence of (see `intel/trends.md`), with a named US institutional deployment to cite |
| https://github.com/open-edge-platform/education-ai-suite | 🟢 **Apache-2.0** — `main/LICENSE`, 11,350 B | 0 (p296) | p327 | **Global** | **On-device inference for classroom AI** | **Intel.** Targets Intel CPU / iGPU / NPU via **OpenVINO**. 11 forks, 450 commits, 0 stars 🟢 **— and it is the only row in this file that answers "no cloud, no GPU budget, no student data leaving the building" with a vendor behind it.** Pairs with `Kolibri` (MIT, offline) in `P5` · **Use it for:** the offline / data-residency variant of any tutor pattern, in every region |
| https://github.com/AI-for-Education/pedagogy-benchmark | 🟢 **MIT** — `main/LICENSE`, 1,063 B | **12** | p327 | **LATAM** | **Evaluation — pedagogical knowledge, measured** | **1,143 questions from real teacher-qualification examinations: 920 in the CDPK benchmark and 223 in SEND** (Special Educational Needs and Disabilities) — counts read from the README this pass. **Acknowledges Chile's Ministry of Education — Agencia de la Calidad de Educación — and CPEIP for developing and sharing the exams.** Scores are published on external leaderboards, not in the repo; p296 records arXiv:2506.18710. Ships `.dvc/` for data versioning. 0 forks, 5 commits 🟢 **— and it is the only artefact in this KB that tests whether a model knows *pedagogy*, sourced from a LATAM ministry's own licensing exam** · **Use it for:** model selection in a Spanish-language LATAM bid, where "which model should we use" is currently answered with vibes |

### One new row's worth of reading, filed in `agents/top.md` instead

🟢 **`devissaputra/curriculum_knowledge_graph` (MIT, 1,076 B read first-hand, 0 ★, 27 commits)** is the curriculum-graph **schema and validator** — 8 entity types, 7 relation types, invalid edges rejected, provenance (`confidence`, `source_type`, `evidence`, `reviewed_on`) on every relation, cycle and coverage-gap detection, 36 passing unit tests. 🔴 **Its bundled data is entirely synthetic and it says so in `data/README.md` and `CALCULATIONS.md` ("SYNTHETIC / RULE-BASED PROTOTYPE \| no educational validity claim").** 🔵 **Which is exactly why it belongs next to the two real curriculum datasets rather than among them: it is the type system those datasets never shipped.** Full read in `agents/top.md`.

### 🔴 The verification surface of this pass, recorded because it bounds every claim above

**This pass could verify GitHub and nothing else.** The environment's network policy answered **403 to CONNECT** for every scholarly and institutional host attempted: `arxiv.org`, `www.nature.com`, `www.sciencedirect.com`, `www.oecd-ilibrary.org`, `www.iesalc.unesco.org`, `huggingface.co`, `www.semanticscholar.org`, `ar5iv.org` — **and both of the vendor's own hosts, `docs.learningcommons.org` and `platform.learningcommons.org`.** `api.github.com` returns a session-scope denial; `curl -sI` over `github.com` returns 403, as at p296.

🔵 **What that means for the rows above: every licence, byte count, file path, entity count and README claim was read from `raw.githubusercontent.com` or the rendered `github.com` page, and is first-hand.** 🔴 **What it means for anything *not* above: the Knowledge Graph dataset downloads could not be fetched and their record counts are therefore unverified — the per-dataset licence labels are read from the repo's own `README.md` and `LICENSE.md`, not from the catalog pages they point to.** **A future pass with reachable vendor docs should pin per-dataset licences at the download level and record counts, as p326 did for Marble's manifest checksums.** No count has been asserted here that was not read.

## Pass 326 · 2026-10-19 (twelfth pass of this date) — fifty-eight rows, and the first of them is not code

**Two rows added — fifty-eight total. Both licences read first-hand on the `raw` channel over the
seven-filename probe space across both candidate branch names.** 🟢 **The headline row is the
largest open artefact this KB has found in the education sector that is not a model or a
framework: `withmarbleapp/os-taxonomy`, 6.1 ★k, 998 forks, 23 commits — a curriculum prerequisite
graph with no code in it at all.**

🔵 **It is in *this* file rather than only in `agents/top.md` because it is the layer everything
else in this KB sits on top of.** Every pattern in `compose/patterns.md` from P1 onward assumes a
client supplies a curriculum spine. **P10 was written because exactly one existed and it covered
one country.** This one covers **seven curricula across the UK, the US and the IB**, and unlike
`cn-math-taxonomy` (CC BY-NC) it can enter a commercial deliverable.

### What was measured, and how

**Licence, first-hand:** `main/LICENSE` and `master/LICENSE` both return 200; the file is **25,289
bytes of genuine Open Data Commons ODbL 1.0 text** (`LICENSE.md`, `LICENSE.txt`, `COPYING` all
404 on both branches — the seven-name probe space is still not optional). The README declares the
split: **ODbL-1.0 for the database** (collection, structure, IDs, relationships) and **CC BY-SA
4.0 for Marble-authored text** (names, descriptions, evidence, prompts, dependency reasons,
cluster summaries). The GitHub sidebar agrees: *"ODbL-1.0, CC-BY-SA-4.0 licenses found."*

**Integrity, first-hand:** `data/manifest.json` carries a SHA-256 per shipped file.
`topics.json` fetched this pass hashes to
`5aa40906ed0095c8af49c8bc2827fa3f10e214892563ea4156c6cde32f9b7e9d` — **the manifest's exact
value.** 🟢 **This is the first dataset in this KB whose contents can be verified against its own
published checksums, and it is the single cheapest thing to ask of every other curriculum
artefact here.**

**Freshness, first-hand, and it corrects every secondary description of this repo in circulation:**
`manifest.generatedAt` is **`2026-10-19T17:32:15.492Z`** — regenerated today. Every roundup and
mirror describing this dataset reports **1,590 topics and 3,221 edges** from the July v1
announcement. **The file as shipped today is 1,591 and 3,225.** 🔵 **Small drift, but it is the
reason this KB pins releases and records checksums rather than quoting a blog: a curriculum that
moves silently under a tutor is a correctness incident, and this one moves.**

### The rows

| Repo | Licence | ★ | Checked | Layer | Why it is foundational |
|---|---|---|---|---|---|
| https://github.com/withmarbleapp/os-taxonomy | 🟢 **ODbL-1.0 (database) + CC BY-SA 4.0 (text)** — `LICENSE` read first-hand on both branches, 25,289 bytes of genuine ODbL text; sidebar agrees. 🔵 **Share-alike, and still commercial**: ODbL binds a *derivative database*, not a *produced work*, so a product built on the graph stays yours. 🔴 `data/curriculum-standards.json` is **not Marble's to relicense** — per-source terms in `PROVENANCE.md` | 6.1k | p326 | **Curriculum data — the spine every pattern in this KB assumed a client would supply** | **1,591 micro-topics, 3,225 prerequisite edges (2,030 hard / 1,195 soft, 100% carrying a prose reason), ages 4–15, eight subjects, 2,189 links into 3,261 standards from seven curricula** (UK NC 2013, CCSS ELA, CCSS Math, NGSS K-5, NGSS MS, C3 Social Studies, IB PYP PSPE). Every topic carries an `assessmentPrompt`; 1,556 carry observable `evidence` descriptors. Ships SHA-256 per file. Separate 23.5 MB `teaching-research.json` covering 1,051 topics — **and naming the 540 it does not cover.** 998 forks, 23 commits, v1 public since 2026-07-08 · **Use it for:** the prerequisite ordering, the age banding and the mastery checks under any tutor; and as the **AI-literacy curriculum** — the entire `Computing` subject is 21 AI topics for ages 5–11 |
| https://github.com/tbh-23/Homestead | 🟢 **MIT** — `LICENSE` read first-hand, *MIT License, `Copyright (c) 2026 Homestead`*, 1,573 bytes. Curriculum data stays under its own ODbL/CC BY-SA terms and is **not vendored** | 15 | p326 | **Reference consumer — the licence boundary, implemented** | **The worked example of how to build a proprietary product on a share-alike dataset.** Fetches `os-taxonomy` from upstream at runtime, caches it outside the repository, and **notifies on upstream topic additions and removals**; the README instructs that the dataset must not be committed. 90%+ mastery gate, independently re-solved mastery tests, Leitner spaced repetition, spaced retry, AI coach grounded in learner progress. 41 commits, 2 forks · **Use it for:** **P13** — and read its attribution string, which is the one ODbL and CC BY-SA actually require |

🔴 **The one thing to check before quoting standard text in a bid.** Four of the seven curricula
ship **codes only** — `ngss-k5`, `ngss-ms`, `c3-social-studies`, `ib-pyp-pspe` — because their
upstream terms do not permit redistribution. **UK NC 2013 ships in full under OGL v3**
(commercial, no share-alike, fixed attribution notice). **Common Core ships in full but remains
under the purpose-limited CCSS Public License**, which does not clearly grant derivative or
sublicensing rights — **so the CCSS records are not ODbL even though they sit in an ODbL
database.** **NGSS is a registered WestEd trademark and commercial use carries a sample-approval
requirement.** The topic→standard links are unaffected throughout.

## Pass 325 · 2026-10-19 (eleventh pass of this date) — fifty-six rows, and the eight that were here all along

**Eight rows added — fifty-six total. Every licence below was read first-hand on the `raw` channel
this pass, over the seven-filename probe space, across five candidate branch names.** 🟢 **Six of
the eight are a promotion, not a discovery, and saying so is the point.** The
**France Université Numérique / FUN-MOOC** stack — the operator of France's national public MOOC
platform — has been measured in `repos/trending.md` since **p127**, re-measured at **p190**,
**p208**, **p212** and **p256**, and **never once carried into this file.** Only `openfun/richie`
ever made it here. **`ralph`, `warren`, `potsie`, `joanie`, `django-lti-toolbox` and `ashley` were
held and unusable, because a row in an append-only history is not a row in a curated starting-point
list.** They are here now, re-verified.

🟢 **And the licence shape of that stack is the exact mirror of p322's, which makes a trend out of
what looked like a one-off.** At **openeduhub** (Germany, publicly funded) p322 found licences
dividing **by architectural layer**: permissive shells, GPL analysers, **an unlicensed inference
core**. At **FUN-MOOC** (France, publicly funded) this pass found **MIT on every layer there is** —
portal CMS, headless ERP, forum, Learning Record Store, analytics viz, Grafana dashboards, LTI
toolkit — with **AGPL-3.0 appearing exactly once, on `openedx-docker`, where it is inherited from
Open edX rather than chosen.** Two publicly funded European education operators; opposite licence
hygiene. **FUN publishes a `handbook` repository of engineering practice and openeduhub does not.**
🔵 **The conclusion for a procurement conversation: public funding does not predict a licence
posture. The operator's engineering maturity does** — and that is observable before you sign, from
the org's own repositories. Full entry in `intel/trends.md`.

🔴 **The caveat that keeps this from being a clean win, stated with the rows:** `warren` says of
itself *"This project is a Proof Of Concept not suitable for production yet"*, and
`django-lti-toolbox` has **no release and has not been pushed since 2024-11-14**. **The spine is
real; two of its seven segments are not load-bearing.** Use `ralph` + `potsie` (Grafana) for the
analytics path and treat `warren` as a reference implementation.

**Two further rows come from outside Europe and one is a new country for this KB:**
**`muhammedalakbarli/imparo`** (MIT, Azerbaijan — grades 1–8, a **154-skill graph** with per-skill
mastery and spaced repetition) and **`LucasSpinola/assistentes-educacionais-com-ia`** (MIT, Brazil,
pt-BR). 🔵 **The Brazilian row is a finding about the channel, not the artefact: LATAM supply
arrived this pass as a *curriculum for building* educational assistants — NLP → LLM → RAG → agents →
learning analytics, free and open — rather than as a product.** That is the third pass in a row in
which the code channel placed a region the policy channel could not.

🟡 **One repair, content-preserving and worth recording because it was invisible:** the three
curriculum-graph rows added at p323 (`haolpku/K12-KGraph`, `razi-03/NCERT-CKG`,
`mizcausevic-dev/curriculum-knowledge-graph`) carried **seven cells in a six-column table** — the
description and the *Use it for* guidance were written as separate cells, so every value after
column five rendered one column to the right. **Merged onto this file's `· **Use it for:**`
convention; no claim altered.** 🔵 A malformed row in a table a compiler reads is a silently wrong
entity, which is the same failure class as a header row left as data.

🔴 **Rejected, recorded so it is not mistaken for supply:** `010Ankushsharma/AdaptaLearn` — DKVMN
knowledge tracing with PPO and a claim of **131M+ interactions** of training data — carries **no
licence file** on the full probe and no way to verify the claim from the repository.


## Pass 324 · 2026-10-19 — ten rows, the integrity tier, and a licence file that is not the grant

**Pass 324 · 2026-10-19 (tenth pass of this date). Forty-eight repos — ten added, all ten measured
first-hand.** Two findings and one closed list. 🟢 **The first finding closes a gap this KB
declared for seven passes**: `intel/trends.md` trend 9 said there was *"no credible open source
AI-detection or academic-integrity project … plus MOSS-style code-plagiarism detectors."* **The
largest of those "MOSS-style" detectors is `jplag/JPlag` — GPL-3.0, 2.0k ★, 376 forks, 5,708
commits, twenty-odd languages, usable as a Java API — which is more maintained than any agent on
these shelves and was never listed.** With it come `NoplagLabs/noplag-engine` (**Apache-2.0**, 86 ★,
winnowing fingerprints in GIN-indexed PostgreSQL) and `thu-cs-lab/jieplag` (**MIT**, 54 ★, Rust).
The gap was a query artefact: the topic `plagiarism-detection` returns what *AI detection* never
did. 🔴 **The second finding runs opposite to every licence defect in this file so far.**
`ZhijieXiong/pyedmine` — the broadest educational-data-mining library this KB has measured, **28
knowledge-tracing models plus cognitive diagnosis, exercise recommendation and learning-path
recommendation over 14 datasets** — ships **the MIT text in `LICENSE`, under someone else's
copyright line (`Stanford Future Data Systems`), while its README says *"All data and code in this
project may be used only for academic purposes."*** Every previous instance here was a README
claiming a grant the repository lacked; **this is the documented grant being narrower than the
licensed one, which is the direction a dependency scanner cannot catch.** 🟢 **And p322's list of
six named-unread `openeduhub` repositories is closed: all six measured.** The two it said to read
first — `its-prep` and `its-data`, the ones `python-kidra` depends on — **both have no licence file
under any of seven candidate names**, as do `topic-statistics` and, on **both** channels,
`oeh-search-frontend`. `mappings` is GPL-3.0 and `skohub-vocabs-oeh-patched` is Apache-2.0.

🔴 **What that does to p322's licence-by-layer reading: the unlicensed set is not the "inference
core", it is the whole substrate plus the UI.** Gateway, models, data loader, token filter **and
the public Angular search frontend** carry no grant. **A studio cannot lawfully reuse any part of
this stack from the search box down to the tokeniser.** And the thinnest shell in the organisation
is the one with no grant on either channel, where the layer rule predicted Apache-2.0 — **so the
layer rule holds for the backend tiers and does not generalise to the UI tier.**

**Licence split recounted over 48, by classifying each row's own licence cell** (rule stated so it
can be re-run: *a README claim with no file in the repository counts as no licence*): 🔴 **no
licence at all (12)**, MIT (11), Apache-2.0 (10), 🟡 GPL-3.0 (6), permissive code with CC BY 4.0
data or content (4), BSD-3-Clause (2), CC0-1.0 (1), MIT code with CC BY-NC-SA 4.0 data (1), and
🔴 **the new shape — MIT file contradicted by an academic-use-only README (1, `pyedmine`)**. The
categories sum to 48. **So 32/48 are usable as software, 12/48 carry no grant at all, and 4/48 are
usable only under a restriction that bites somewhere a scanner does not look.**

**The licence lesson, third shape in three passes.** p322: licences divide **by architectural
layer** across an organisation. p323: **by artefact type** inside a repository — MIT code,
NonCommercial data. p324: **by channel inside a repository, with the restrictive channel being the
prose one** — the file says MIT and the README says academic-only. The first two reduce to
*permissive at the edges, restricted at whatever took the work*. **The third does not reduce to
anything reassuring: it means the licence file is not sufficient evidence of the grant, in either
direction**, and the only safe reading of a repository is every channel it publishes.

**Pass 323 · 2026-10-19 (ninth pass of this date). Thirty-eight repos — three added, all three read
first-hand.** The three are one finding and two corrections. **The finding — `haolpku/K12-KGraph`,
420 ★, NeurIPS 2026 Evaluations & Datasets Track — makes `intel/trends.md` trend 12's headline
wrong.** That trend has said since p319 that *"exactly one country has built"* verified
curriculum-standard data. **Two have.** China's PEP K-12 curriculum now exists as an
evidence-linked knowledge graph with 12 expert annotators at Fleiss' κ = 0.84, a 23,640-question
benchmark and three released checkpoints — **and its data is CC BY-NC-SA 4.0 while its code is
MIT.** Brazil's `bncc-dev` stays the only verified national curriculum whose **data** Globant can
put in a client deliverable. The corrections: **`razi-03/NCERT-CKG`** makes India's gap contested
rather than empty (and has no licence), and **`tsugiproject/tsugi`'s** two-pass open question is
closed with *the repository does not say*. **Licence split over 38: MIT (10), Apache-2.0 (9),
🔴 no licence at all (8), MIT-code-with-CC-BY-4.0-data or -content (4), GPL-3.0 (4),
BSD-3-Clause (2), CC0-1.0 (1), and one README-claims-MIT-with-no-file (`metadata-agent-api`) —
plus the new split shape, **MIT code with CC BY-NC-SA 4.0 data (1 — K12-KGraph)**, which is the
first NonCommercial data licence in this file. So **29/38 are usable as software, 8/38 carry no
grant, and one is usable only as a method.**

**The licence shape is the transferable lesson, and it pairs with p322's.** p322 found licences
dividing **by architectural layer** across one organisation: permissive shells, GPL analysers,
unlicensed inference core. This pass found them dividing **by artefact type** inside one
repository: MIT code, NonCommercial data. **Both reduce to one sentence — permissive at the edges,
restricted at whatever actually took the work.** In Germany that was the inference core; in China
it is the curriculum itself. **A sidebar badge answers neither case**, which is why this file reads
licences off the repository and now has to read them off the README's licence *section* too.

**Pass 322 · 2026-10-19 (eighth pass of this date). Thirty-five repos — twelve added, all sixteen
reads first-hand, all from one organisation.** Pass 321 named six `openeduhub` repositories it had
not read and declared 57 of 67 unenumerated. **This pass enumerated all sixty-seven and read every
AI-era repository in the org.** The twelve rows below are Germany's publicly funded OER metadata
pipeline, service by service, with the licence of each read off the repository rather than the
README — because in this organisation those disagree four times. The structural finding, and the
reason this matters more than any single row, is in the section *"The inference core is the
unlicensed part"* below. **Licence split over 35: MIT (9), Apache-2.0 (8), 🔴 no licence at all (6),
MIT-code-with-CC-BY-4.0-data or -content (4), GPL-3.0 (4), BSD-3-Clause (2), CC0-1.0 (1), and one
repository whose README claims MIT with no licence file behind it (`metadata-agent-api`) — so
28/35 are usable and 6/35 carry no grant.** The p320 line reading "Licence split over 21" below is
superseded by this count; it was already stale by two rows when p322 opened the file.


**Pass 320 · 2026-10-19 (sixth pass of this date). Twenty-one repos** — one added, and it is the
only substantive addition anywhere in this KB this pass. **`adamzammit/LTIPlugin` is the first
artefact this KB has found at the grade-passback seam that carries an OSI-approved licence**
(GPL-3.0) rather than no licence at all; read the row's caveats before scoping it, because it is
not an AI tool and probably not LTI 1.3. The method constraint was **re-tested rather than
inherited** this pass and reproduces exactly: github.com is the only reachable origin, and
`www.future-ed.org`, `www.lw.com` and `www.iesalc.unesco.org` each failed at DNS when attempted
directly.

**Pass 319 · 2026-10-19.** Twenty repos. "Foundational" here means: you would put it *under* an
education product, not ship it as the product. **Checked** says which pass took the licence/star
reading.

**Pass 319 is the largest single addition this file has had, and the find of the pass is Brazilian.**
The `bncc-dev` stack — a character-verified machine-readable national curriculum, an MCP server over
it, and a benchmark that measures what grounding on it is worth — is the artefact every pattern in
this KB has assumed a client would supply. **It exists in exactly one country, it has 22 stars, and
it publishes the number: curriculum hallucination drops from 31.9% to 2.3% when the model queries
it.** Detail below the table.

The pass also closed the `pylti1.3` concentration risk with a real alternative
(`tsugiproject/tsugi`, 4,011 commits, from the author of the LTI specification), added the
institutional-grade **EMEA** autograder this file lacked (`thm-mni-ii/feedbacksystem`, 2,248
commits at 24 stars), and swept GitHub topics **in four languages other than English** — which is
how most of this was found. The method note at the end is the part worth copying.

| Repo | Licence | ★ | Checked | Layer | Why it is foundational |
|---|---|---|---|---|---|
| https://github.com/openfun/ralph | 🟢 **MIT** — `LICENSE.md` read first-hand, *MIT License, `Copyright (c) 2020-present France Université Numérique`*. 🔴 `LICENSE` 404s; only `LICENSE.md` exists, which is why a seven-name probe space is not optional | 51 | p325 | **Learning records — the event spine** | **The learner-event substrate a tutoring agent needs, published MIT by a national public operator, and held in this KB's history since p127 without ever reaching this list.** Three things in one package: an **LRS** (HTTP API collecting **xAPI** statements to the ADL LRS standard), a **CLI** for building UNIX-style data pipelines, and a **library** that fetches, (de)serialises and converts learning events between **xAPI** and **Open edX tracking logs**. Ships as `ralph-malph` on PyPI, `fundocker/ralph` on Docker Hub and an **`openfuncharts/ralph` Helm chart**; Elasticsearch backend; FastAPI + Pydantic; community on the **ESUP** (French higher-ed) Rocket.Chat · **Use it for:** **the retrieval and audit substrate under any tutor you have to prove something about.** Every pedagogical claim in a bid needs an event log that predates the claim; this is the permissive one. 🔵 Note the organisational tell: FUN ran `learninglocker-docker` and **deprecated it to build Ralph** — the incumbent LRS was replaced by the operator's own MIT one |
| https://github.com/openfun/joanie | 🟢 **MIT** — `LICENSE` read first-hand, *MIT License, `Copyright (c) 2021 France Université Numérique`* | 30 | p325 | **Education ERP (headless)** | **The education ERP this KB's vertical tier has been missing a permissive answer for.** Its own words: *"a headless ERP for education to manage course enrollment/subscription, payment and certificates delivery"* — built on **Django REST Framework**, Docker-first, with Terraform scripts and documentation for object-storage media on **OpenStack Swift**. Designed to sit behind `richie` (*"Power up Richie catalog"*) · **Use it for:** **the commercial spine of a training or certification product** — enrolment, subscription, payment, certificate issue — without inheriting a copyleft platform. This is the row that answers *"is there an Odoo for education under a permissive licence"* with a qualified yes: **headless and MIT, but the education ERP proper, not a general business framework with an education module bolted on** |
| https://github.com/openfun/potsie | 🟢 **MIT** — `LICENSE.md` read first-hand, *MIT License, `Copyright (c) 2021-present France Université Numérique`*; sidebar agrees | 11 | p325 | **Learning analytics — dashboards** | **A Grafana dashboard suite for learning analytics, written in Jsonnet with grafonnet — 114 commits.** The production-ready end of the FUN analytics path: where `warren` declares itself a proof of concept, Potsie is dashboards-as-code on an operational stack an institution already runs · **Use it for:** **the teacher- and programme-facing reporting layer over `ralph`**, delivered as reviewable code rather than as clicks in a BI tool. 🟡 Its README does not name Ralph or a datasource explicitly, so the binding is your build — read the Jsonnet, not the prose |
| https://github.com/openfun/warren | 🟡 **MIT** — `LICENSE.md` read first-hand, *MIT License, `Copyright (c) 2023-present France Université Numérique`* — **but see the self-assessment** | 17 | p325 | **Learning analytics — visualisation (reference only)** | *"A visualization platform for learning analytics"* over xAPI, and it states in its own README: 🔴 ***"This project is a Proof Of Concept not suitable for production yet."*** Recorded anyway, for one reason worth more than the code: **its frontend renders inside an LTI iframe** — the operator delivering xAPI analytics to a course chose **LTI** as the surface · **Use it for:** **evidence in the LTI-versus-MCP argument** (`intel/trends.md` trend 6) and as a reference for the Ralph → dashboard binding. 🔴 **Do not propose it as a deliverable component**; it disqualified itself and that honesty is why the row is here |
| https://github.com/openfun/django-lti-toolbox | 🟡 **MIT** — `LICENSE` read first-hand, *MIT License, `Copyright (c) 2020-present GIP FUN MOOC.`*; sidebar agrees | 14 | p325 | **Interoperability — LTI tool provider plumbing** | *"A Django application to build LTI Tool Providers"*, **34 commits, no release, and last pushed `2024-11-14`** — 🔴 **confirmed to the day on the git channel at p330: 34 commits · 6 authors · last commit `2024-11-14`.** 🔴 **This row is the evidence behind this pass's main finding and should be read as a measurement, not a recommendation: the permissive LTI plumbing exists, a national public operator published it, and it has sat untouched for roughly twenty-three months** while MCP tooling in this same KB ships weekly. The README names no LTI version · **Use it for:** **the argument, and only then the code.** When a client insists the integration must be LTI, this is both the permissive starting point *and* the exhibit for why the agent ecosystem went elsewhere. Budget maintenance you do not get from upstream |
| https://github.com/openfun/ashley | 🟢 **MIT** — `LICENSE` read first-hand, *MIT License, `Copyright (c) 2020-present GIP FUN MOOC.`* | 12 | p325 | **Course discussion / cohort surface** | *"A self-hosted multi-tenant discussion forum for learning"*, Django, from the FUN-MOOC stack · **Use it for:** **the cohort layer a tutor product keeps needing and nobody budgets for.** Multi-tenancy is the part that matters: one deployment across many courses or institutions, which is the shape a studio engagement actually ships in. Also the natural **xAPI emitter** for discussion events feeding `ralph` |
| https://github.com/muhammedalakbarli/imparo | 🟡 **MIT** — `LICENSE` read first-hand, the MIT text. 🔴 **Header reads `Copyright (c) 2017 Contributors` on a repository created `2026-07-01`** — an unedited template, i.e. the grant is intact but the holder and year are fiction | 2 | p325 | **National-curriculum adaptive platform (EMEA — Azerbaijan)** | **The first Azerbaijani artefact in this KB, and the first skill graph here built against a non-EU, non-Anglophone national curriculum.** An adaptive learning platform for **Azerbaijani school pupils, grades 1–8**, described in Azerbaijani: a **154-skill graph (`154 bacarıqlıq qraf`)**, a **per-skill mastery model**, individualised practice and **spaced repetition**, with gamification. Next.js + React + Supabase + Tailwind; pushed 2026-10-09 · **Use it for:** **the template question in any ministry conversation outside the big markets — what does it cost to express a national curriculum as a skill graph?** The answer here is 154 skills and one developer. 🟡 Fix the licence header before a scanner reads it |
| https://github.com/LucasSpinola/assistentes-educacionais-com-ia | 🟢 **MIT** — `LICENSE` read first-hand, *MIT License, `Copyright (c) 2026 Lucas Spinola e contribuidores do projeto AI for Educational Assistants`* | 2 | p325 | **Capability transfer (LATAM — Brazil, pt-BR)** | *"Trilha aberta e gratuita, do zero ao avançado, para construir assistentes educacionais inteligentes"* — a free, open, zero-to-advanced **track for building** intelligent educational assistants: NLP, machine learning, deep learning, transformers, LLMs, **RAG, agents and learning analytics**, as Jupyter notebooks, with Ollama in the stack · **Use it for:** **the enablement half of a LATAM engagement, in the client's language.** Every studio proposal in this region ends with a knowledge-transfer line item that someone then has to write; this is a permissive, Portuguese-language starting point for it. 🔵 **And read it as channel evidence: this pass's LATAM supply arrived as a curriculum, not a product** |
| https://github.com/ZhijieXiong/pyedmine | 🔴 **CONTRADICTORY — `LICENSE` is the MIT text, the README is academic-use-only.** `LICENSE` read first-hand: *MIT License, `Copyright (c) 2023 Stanford Future Data Systems`* — an organisation unrelated to this project, i.e. a copied file whose holder was never updated. README, verbatim: *"All data and code in this project may be used only for academic purposes."* | 82 | p324 | Educational data mining — KT, CD, exercise & path recommendation | **The broadest educational-data-mining library this KB has measured, and the one it cannot use.** *"A unified experimental workflow"* over **four task families**: knowledge tracing (**28 models** — qDKT_CORE, AKT_CORE, DisKT, ATDKT, CLKT, DTransformer, GRKT, HDLPKT, DKT, DIMKT among them), **cognitive diagnosis (7**, incl. NCD, HyperCD), **exercise recommendation (3)** and **learning-path recommendation (4**, LPKT4LPR as simulator), over **14 EDM datasets** (SLP, assist2009/-full/2012/2015/2017, edi2020, junyi2015, moocradar, poj, slepemapy-anatomy, statics2011, xes3g5m; EdNet-KT1 via a preprocessing note; the edi2020 text extension is *"an unofficial extension"*). **Five dataset-splitting settings**, pretrained weights on Hugging Face, a published model leaderboard, and **cold-start, hard-sample and multi-step** evaluation — with the BES metric self-marked *"has not been validated."* 220 commits, 13 forks, **v1.0.0 (15 Aug 2025) described as a stable LTS release**. Referenced codebases per its README: PYKT, EduKTM, EduCDM, RecBole. 🔵 Measured the same pass for comparison: **`pykt-team/pykt-toolkit` is 450 ★ / 139 forks** — earlier cycles of this KB carried pyKT at *"1.2k"*; **450 is the measured figure** · **Use it for:** 🔴 **Do not put it in a deliverable.** The permissive channel is boilerplate with somebody else's copyright on it; the restrictive channel is the author's own specific sentence. **A scanner returns MIT and clears procurement; a reviewer reads the README and stops the engagement** — and this is the first case in this file where the documented grant is *narrower* than the licensed one, which is the direction scanners do not catch. **Use it to choose a model family and to read the splitting settings, then reimplement, or open an issue and get the contradiction resolved in writing.** When a client needs cognitive diagnosis or exercise recommendation and not just KT, this is the map of the field; `pykt-toolkit` remains the thing you can actually ship |
| https://github.com/jplag/JPlag | 🟡 **GPL-3.0** — `LICENSE` read first-hand, the GNU GPL v3, 29 June 2007 text; sidebar agrees | 2.0k | p324 | Assessment integrity — source-code plagiarism & collusion | **The largest and most-maintained artefact in this KB's integrity tier by an order of magnitude, and it was never listed. 376 forks, 5,708 commits, pushed 2026-10-19.** Source-code plagiarism **and collusion** detection across twenty-odd languages — Java, C, C++, C#, Python, JavaScript, TypeScript, Go, Kotlin, R, Rust, Swift, Scala, LLVM IR, Scheme, EMF metamodel and model, SCXML, plain text, plus a multi-language mode — with the README's own caveat that *"maturity varies by language."* *"JPlag can either be used via the CLI or directly via its Java API"*, published on **Maven Central**, with a local report viewer that launches automatically from the CLI: *"No data will leave your computer!"* 🔵 The README makes **no comparison to Moss** — `moss` is a topic tag only · **Use it for:** **For any CS-education or bootcamp engagement this is the integrity layer, not a build.** Twenty-language coverage and a Java API mean it drops behind a service boundary in days. 🟡 **GPL-3.0: deploy it as a service over HTTP and never link it into the client's application** — the same rule this file applies to `text-statistics`. Pair it with `aegis-integrity` (prose and citations) in `compose/patterns.md` **P11**; JPlag covers code, which `aegis-integrity` does not |
| https://github.com/NoplagLabs/noplag-engine | 🟢 **Apache-2.0** — `LICENSE` read first-hand, the Apache 2.0, January 2004 text; description agrees | 86 | p324 | Assessment integrity — verbatim & near-verbatim text matching | **The permissive text-similarity engine the integrity tier needed.** Sentence-window chunks → **winnowing fingerprints stored as a GIN-indexed `bigint[]` in PostgreSQL** → candidate retrieval by fingerprint overlap → **seed-and-extend alignment to exact character ranges.** Five REST endpoints (`POST /v1/checks`, `GET /v1/checks/{id}`, `GET /v1/checks/{id}/report`, `POST /v1/corpus/documents`, `/docs` for OpenAPI), SSE progress per `docs/api.md`, Alembic migrations, `docker compose up`, and a first boot that indexes **~1,000 bundled Wikipedia articles**. Honest about scope: *"This engine detects verbatim and near-verbatim copying"* and *"paraphrase, semantic, and AI-writing detection are on the public roadmap."* Benchmarks stated and bounded: plagdet *"around 0.8+"* with precision ≥ 0.95 on verbatim and lightly obfuscated material, while on the full PAN-PC-11 an L0/L1 engine *"scores near zero by design"* — with an explicit warning against reading one plagdet figure as general accuracy. **6 commits, 76 forks** · **Use it for:** **Take it for the algorithm and the schema; it is a studio-grade reference for fingerprint storage in Postgres, which is the part teams get wrong.** 🔴 **Three cautions:** it is the **open core of the hosted noplag.com** (the hosted side adds live web search; the open engine matches your local corpus only), *"the API ships with no authentication"* so it cannot face a network as given, and **6 commits against 86 stars and 76 forks** is a fork-to-star ratio this KB has not seen on an organically grown repository — read the code before depending on the project |
| https://github.com/thu-cs-lab/jieplag | 🟢 **MIT** — `LICENSE` read first-hand, *MIT License, Copyright (c) 2023 Jiajie Chen, Shengqi Chen* | 54 | p324 | Assessment integrity — code similarity (Rust) | Moss-inspired plagiarism detection **in Rust**, from the Tsinghua CS teaching lab. 1 fork, default branch `master`, last pushed 2026-06-28 · **Use it for:** **The only permissively licensed code-similarity engine in this file with no commercial product behind it** — which makes it the one to embed rather than service-isolate when a client's constraint is GPL avoidance rather than language coverage. 🔴 Smaller and quieter than JPlag: no multi-language story, and APAC-authored with Chinese-language teaching context |
| https://github.com/openeduhub/skohub-vocabs-oeh-patched | 🟢 **Apache-2.0** — `LICENSE` read first-hand, the Apache 2.0, January 2004 text. 🟡 `package.json` says `"license": "Apache License 2.0"`, **which is not a valid SPDX identifier** (`Apache-2.0` is), so an SPDX-strict scanner reads the manifest as unknown rather than as Apache | 0 | p324 | Vocabulary publishing (EMEA) | **A patched fork of `skohub-io/skohub-vocabs`** — hbz NRW and graphthinking GmbH upstream; the `package.json` `repository` field still points at `skohub-io/skohub-vocabs`. *"A simple tool for publishing SKOS vocabularies"*: a static-site generator that parses SKOS with **slash or hash URIs** (slash *"better supported"*), renders full concept pages with **machine-readable JSON-LD per concept**, exposes a basic lookup API, supports a **webhook server that rebuilds a vocabulary from GitHub or GitLab**, and selects display language from the browser or a `?lang=` parameter. **This is the publishing layer behind the `vocabs.openeduhub.de` that `its-data` resolves URIs against** · **Use it for:** **The permissive half of the German stack, and the only `openeduhub` repository whose grant came in from outside.** If a client needs controlled vocabularies published as resolvable, machine-readable SKOS — competency frameworks, subject taxonomies, qualification levels — this is the build. 🟡 Fix the manifest to `Apache-2.0` in your fork before it hits the client's dependency scanner |
| https://github.com/openeduhub/mappings | 🟡 **GPL-3.0** — `LICENSE` read first-hand, the GNU GPL v3, 29 June 2007 text | 0 | p324 | Vocabulary / schema mappings (EMEA) | Vocabulary and schema mappings for the WLO metadata stack. One of p322's six named-unread repositories; measured this pass · **Use it for:** **Service, never linked** — the same GPL-3.0 rule as `metalookup`, `text-statistics` and `discipline-classification`. Its value is as a worked example of mapping one country's education metadata vocabularies onto each other, which is the unglamorous half of every interoperability engagement |
| https://github.com/openeduhub/its-prep | 🔴 **NO LICENCE** — no licence file under any of `LICENSE`, `LICENSE.md`, `LICENSE.org`, `LICENCE`, `COPYING`, `LICENSE.txt`, nor a manifest grant; no sidebar entry | 0 | p324 | NLP substrate (EMEA) | **87 commits. One of the two repositories p322 told this pass to read first, because `python-kidra` depends on it.** *"A generic interface to various NLP tools"* whose stated goal is to *"stream-line the process of defining natural language pre-processing pipelines, particularly in the context of educational resources."* The design is the part worth reading: **every pipeline stage is a filter that returns a subset of a document's tokens and may not modify them**, over an immutable `Document` that retains the full original text — so a pipeline is auditable and reversible by construction. Worked example (`poc_topic_modeling`): drop unwanted universal POS tags → drop stop words → drop lemmas expected to carry little meaning **for learning resources** → drop lemmas by document frequency at both tails. Named-entity and noun-chunk merging; spaCy analysis caches via `save_caches`/`load_caches`; pip or Nix flake. German `de_core_news_lg` (🔴 the README's link beside it points at `de_dep_news_trf`, a different model) · **Use it for:** 🔴 **No grant: cannot be used.** **Reimplement the filter contract — it is ten lines of interface and it is the right design**: keep-or-discard filters over an immutable document, which is exactly what makes an OER ingestion pipeline explainable to a ministry client. The German model dependency means the tuning does not transfer; the architecture does |
| https://github.com/openeduhub/its-data | 🔴 **NO LICENCE** — no licence file under any of seven candidate names, no manifest grant, no sidebar entry | 0 | p324 | Data substrate (EMEA) | **159 commits. The second of the two `python-kidra` dependencies p322 named.** *"A Python library that aids in retrieving and processing large data dumps from elasticdump … primarily for the purpose of training and evaluation of AI tools for the automatic generation of metadata."* Two modules: `its_data.fetch` downloads elasticdump files, turns them into **pandas** data frames and **retrieves labels for URIs and SKOS vocabularies**; `its_data.default_pipelines` ships `flat_classification` and friends. A `download-data` CLI; Nix flake recommended, pip *"untested"*. The schema is the useful part: OEH metadata keys (`properties.ccm:taxonid`, `properties.ccm:educationalcontext`) in, and out come `raw_texts` (title + description), `ids`, **`editor_arr` (an editor-confirmed flag)** and `target_data` with `arr`, `uris`, `labels` and **`in_test_set`** — i.e. the train/test split and the human-confirmation flag are **first-class fields of the data contract**, not a notebook convention. URIs resolve against `vocabs.openeduhub.de` · **Use it for:** 🔴 **No grant: cannot be used.** **Copy the contract, not the code.** `editor_arr` + `in_test_set` as fields of the dataset itself is the cheapest governance win in an OER metadata engagement: it makes *"which of these labels did a human confirm"* and *"which rows may be scored"* answerable from the data rather than from tribal memory |
| https://github.com/openeduhub/topic-statistics | 🔴 **NO LICENCE** — no licence file under any of seven candidate names, no sidebar entry | 0 | p324 | Analytics utility (EMEA) | **9 commits.** *"A very simple application that computes various statistics on WLO topic pages, based on a downloaded copy of the database."* Invoked only as `nix run github:openeduhub/topic-statistics -- --help`; no HTTP surface. Its own *Possible Improvements* section proposes **folding the logic into `meta-qs` rather than running a separate service**, and reading the private ElasticSearch directly instead of a downloaded dump; it links `its-data` for a collection filter · **Use it for:** 🔴 **No grant, 9 commits, and the repository argues against its own existence.** Recorded for completeness and to close p322's list. The transferable observation is organisational: this is what a public operator's analytics looks like before it is a product — a Nix-runnable script over a database dump, with the consolidation already written down |
| https://github.com/openeduhub/oeh-search-frontend | 🔴 **NO LICENCE ON EITHER CHANNEL** — no licence file under any of six candidate names, **and `package.json` has no `license` key at all**; no sidebar entry | 5 | p324 | Public search UI (EMEA) | **1,050 commits on `develop`, 1 fork, 13 open pull requests — the second most-committed repository in the organisation after `oeh-search-etl`.** The **Angular 19.2.14** public search frontend of WirLernenOnline.de. *"In order to use the frontend, you either need a deployed or a locally running instance of Edu-Sharing."* Split into `api` and `wlo-search` (`core`, `preferences`, `search`, `shared`, `template`); Node pinned via `.nvmrc`; configuration injected through `src/env.js` from environment variables in Docker; **Karma unit tests and Cypress E2E**; Husky + lint-staged + Prettier + ESLint; Angular i18n with locales in `src/locale`; and web components built and copied into a **WordPress theme folder** · **Use it for:** 🔴 **No grant: cannot be used — and this row is why the licence-by-layer rule stops at the backend.** p322 read the org as *permissive shells / GPL analysers / unlicensed inference core*; **the thinnest shell of all, a pure UI, has no grant on either channel**, where that rule predicted Apache-2.0. 🔵 Note the asymmetry for diligence: *no `license` key* is a weaker position than a manifest that disagrees with the `LICENSE` file — there is nothing to argue from. **Rebuild the UI; read it for the WordPress-embed pattern**, which is how a ministry portal actually ships a search experience into an existing CMS |
| https://github.com/haolpku/K12-KGraph | **MIT (code) / CC BY-NC-SA 4.0 (data)** — README, verbatim: *"Code (this repository): MIT"*, *"Dataset (graph, benchmark, training data): CC BY-NC-SA 4.0"*; sidebar reads *"MIT licenses found"* | 420 | p323 | Curriculum data + benchmark + training data | **China's national curriculum as a verified, evidence-linked knowledge graph — and the peer-reviewed proof that the `bncc-dev` method generalises.** Accepted to the **NeurIPS 2026 Evaluations & Datasets Track**. Built from **48 People's Education Press (PEP) K-12 textbooks** — Mathematics 23, Physics 9, Chemistry 7, Biology 9. **10,685 KG nodes** (6,579 concepts, 1,364 skills, 652 experiments, 1,171 exercises) and **23,278 edges across 9 edge types**; **every edge carries an `evidence` field linking back to textbook source text**. Verification: **12 subject-qualified expert annotators at Fleiss' κ = 0.84**, automatic **DAG validation of the `is_a` and `prerequisites_for` subgraphs**, and a 3-expert spot-check of stratified benchmark items at **98.4% fully correct**. **K12-Bench: 23,640 multi-select questions** over five task families. **K12-Train: 2,267 instruction–response pairs.** Three checkpoints fine-tuned on K12-Train (Llama3.1-8B, Qwen3.5-2B, Qwen3-4B) on Hugging Face. 67 forks, 16 commits · **The pipeline is MIT and the curriculum is not.** Reuse the **method** — extraction, per-edge evidence linking, DAG validation, the annotation protocol that produced κ = 0.84 — in any jurisdiction; **the graph, benchmark and training data are NonCommercial and ShareAlike and cannot enter a client deliverable anywhere.** This is the strongest argument in this KB for the P10 build: it proves the hard part is doable and is itself licensed out of commercial reach. **Two caveats for anyone quoting it:** the About blurb says *"multimodal training dataset"* while the body describes only text instruction–response pairs, and the README reports expert *review* plus validation — **it does not claim every edge was individually human-verified**, and κ = 0.84 measures annotator agreement on relation labels, not graph completeness |
| https://github.com/razi-03/NCERT-CKG | 🔴 **NO LICENCE** — no sidebar entry, no LICENSE file | 0 | p323 | Curriculum data (India) | **The artefact p322 swept 180 `ncert`/`cbse` repositories for and declared absent — found by changing the query, and it has no grant.** **Class X NCERT Mathematics only**, from **18 PDFs**: 14 chapters (`jemh101`–`jemh114`), two additional chapters (`jemh1a1`, `jemh1a2`), an answer source (`jemh1an`) and a preliminary file (`jemh1ps`). PDF in, **CKG JSON** out. **10,417 CKG nodes, 1,682 semantic nodes, 13,757 provenance-aware edges**, provenance coverage **1,682 / 1,682** — *"every semantic node is required to have source evidence."* The method is the right one: *"prerequisite reasoning is treated separately from textbook ordering"*, and a prerequisite *"must instead be supported by conceptual dependency evidence or an explicit inference procedure"* — a chapter appearing earlier is **not** treated as proof of a prerequisite. 0 forks, 2 commits, no release · **Do not depend on it; do watch it, and consider asking the author for a licence.** It makes India's curriculum gap **contested rather than empty**, which shortens the P10 Variant B window. Two silences matter: the README says **nothing about textbook copyright or whether the 18 NCERT PDFs are bundled** (this KB has already recorded one NCERT project that bundles textbook PDFs), and it **never mentions an LLM**, so whether the edges are model-derived is unknown rather than concealed — the only review language is the generic *"should be sampled and reviewed manually"* |
| https://github.com/mizcausevic-dev/curriculum-knowledge-graph | MIT (sidebar) | 1 | p323 | Higher-ed curriculum analysis | FastAPI service modelling **courses, prerequisites, skills and outcomes** as a graph, with prerequisite and skill-dependency analysis, **pathway bottleneck analysis** and a capstone pathway explorer. Ships `app/data/sample_curriculum.json` as a seeded degree path, so it is not framework-only; its own example names `IS-230` as the highest-bottleneck course and a capstone path of IS-101 → IS-210 → IS-320 → IS-410. **No institution or country stated, and the sample data is not claimed to reflect a real programme.** 0 forks, 10 commits · **A pattern, not a dataset — and the permissive component this KB lacked for higher-ed advising.** Bottleneck analysis over a prerequisite graph is a sellable higher-ed product (which course silently gates a cohort's time-to-degree) and nothing else here implements it. **Also a market signal: the author is already in this KB** — `mizcausevic-dev/mcp-ai-tutor` sits in the FERPA governance cluster. One author building both a compliance auditor and a curriculum graph, each at 0–1 stars, is p322's market-forming shape appearing in a second component |
| https://github.com/openeduhub/python-kidra | 🔴 **NO LICENCE — none in the sidebar, none in the root listing, none in the README** | 0 | p322 | AI service gateway (EMEA) | **137 commits.** *"A unified API to the various AI applications we have built"* for the **IT's JOINTLY** project, used to generate additional or missing metadata. One API in front of seven services: `text-extraction`, `text-statistics`, `topic-statistics`, `its-jointprobability` (Bayesian metadata prediction), `wlo-topic-assistant`, `wlo-classification` and `kea` (links relevant Wikipedia articles, forwarded to an external service). 🔴 **This is the single most useful artefact in the org and it carries no grant at all.** Read it as an architecture document — the service decomposition is the transferable part — and note that one of the seven services it advertises has no public repository (404, see below) |
| https://github.com/openeduhub/its-jointprobability | 🔴 **NO LICENCE — none in the sidebar, no licence file in the root listing, none in the README** | 0 | p322 | Metadata prediction / ML (EMEA) | **200 commits.** Bayesian metadata generation for educational materials: **Pyro**'s ProdLDA topic model trained with black-box variational inference over PyTorch bag-of-words tensors. Predicts **school discipline, university discipline, resource type, target audience, educational context and WLO topic** from raw text via a `/predict` REST endpoint or the `predict_from_texts` method; ships retraining CLIs and runs as a Nix microservice. 🔴 **No grant.** It is also the most interesting single artefact here for a client with a large uncatalogued corpus and no labels budget — which is exactly why the missing licence matters |
| https://github.com/openeduhub/metalookup | 🟡 **GPL-3.0** (sidebar + `LICENSE.txt`) | 5 | p322 | OER compliance / metadata (EMEA) | **623 commits** — the second most-maintained repo in the org and the most maintained one that carries any licence. Extracts and suggests OER metadata from a URL, covering **accessibility, licensing and advertising**: Playwright fetches the page, then it analyses the requests, responses and final rendered HTML, and runs **Lighthouse** to assess accessibility. Deploys as a container set — API, Lighthouse, `browserless/chrome`, optional Postgres cache (SQLite or no cache also supported); `POST /extract` takes `{"url": ...}`, `/_ping` is the health check, Swagger at `/docs`. **Only the API container is meant to be reachable** — **The accessibility-and-licence screen that every public-sector OER procurement asks for, already built.** 🟡 GPL-3.0: run it as a service behind a process boundary and never link it into a client codebase. Field list is in `docs/features.md`, which this KB has not read |
| https://github.com/openeduhub/edu-sharing-python-client | **Apache-2.0** (sidebar + README) | 0 | p322 | Platform client (EMEA) | **519 commits**, tag **v0.3.6**, test report in the README dated 2026-10-01. Async-first Python client for edu-sharing repositories and the **b-api (Bildungs-API)**: search, metadata read and write, collections, publishing — plus access to an **LLM gateway, a text-extraction service and the metadata agent**. **All 389 operations are generated from `openapi.json`**, with `scripts/generate_client.py` able to regenerate the layer from a live instance's spec. **Verified against edu-sharing 11.0.** Pre-1.0 and **not on PyPI — install from Git** — **The licence-clean way into the whole stack, and the row to start from.** Apache-2.0 over a generated client means the integration surface is safe even where the services behind it are not. This is how you touch a GPL-3.0 edu-sharing instance without a linking question |
| https://github.com/openeduhub/metadata-agent-api | 🔴 **README says "Lizenz: MIT" — no `LICENSE`, `LICENSE.md`, `LICENSE.txt` or `COPYING` in the root listing, and the sidebar shows no licence** | 0 | p322 | Metadata extraction engine (EMEA) | **24 commits.** The engine under `metadata-agent-canvas` and the browser plugin: a FastAPI service (Python 3.13+, uvicorn, Docker with Playwright and Chromium for screenshots) that extracts structured metadata in the **WLO/OEH schema** from text, a URL or a repository node, then normalises values, geocodes addresses, validates and can upload to edu-sharing. **Eleven active schemas** — event, learning material, education offer, person, organisation, tool/service, source, didactic planning tool, occupation, prompt. Endpoints: `/generate`, `/extract-field`, `/detect-content-type`, `/validate`, `/export/markdown`, `/upload`, `/upload/verify/{node_id}`, `/screenshot`, `/health`, `/info/schemata`. Responses can carry **per-field origin tags**, the source text and a base64 preview. Providers: `b-api-openai` (default `gpt-4.1-mini`), **`b-api-academiccloud` (`deepseek-r1`)**, native `openai` (`gpt-4o-mini`); default temperature 0.3 — **Per-field origin tags are the provenance feature an education buyer now asks for, and the AcademicCloud provider is a sovereign-inference path through German academic compute.** 🔴 But the grant is a README sentence with no file behind it — treat the schema design and the endpoint surface as the deliverable, not the code |
| https://github.com/openeduhub/text-extraction | 🔴 **NO LICENCE — none in the sidebar, no licence file in the root listing, none in the README** | 0 | p322 | Ingestion (EMEA) | **77 commits.** Extracts clean text from URLs using **trafilatura and markitdown**, explicitly aiming to improve on trafilatura alone and to fall back when extraction fails on JavaScript-heavy sites — the fallback is **Playwright headless Chromium**. Ships real rate limiting (`get_simple_multibucket_limiter`, `domain_mapper`), runs as a library (`from_headless_browser_unlimited`, `from_html_unlimited`), a local service on port 8000 or Docker. 🔴 **No grant** — The per-domain rate limiting is the part most homegrown harvesters lack and the part that gets an engagement blocked by a publisher. Read it, then write your own |
| https://github.com/openeduhub/text-statistics | 🟡 **GPL-3.0** (sidebar + `LICENSE`) | 0 | p322 | Readability (EMEA) | **94 commits.** Microservice computing **estimated reading time** from a 200 WPM baseline adjusted by **Flesch Reading Ease**, plus the Flesch score, a difficulty classification and the **Wiener Sachtextformel** index. `POST localhost:8080/analyze-text` returns the metrics and a version number; runs as a Python package, a Nix flake or a Docker image. **No ML models** — the reading-time adjustment is a fixed exponential formula, and the README says better models could come later — **Reading level is the single most requested differentiation signal in schools work and this computes it with arithmetic, not a model.** The Wiener index is German-calibrated — confirm the formula before applying it to another language. 🟡 GPL-3.0: service boundary only |
| https://github.com/openeduhub/discipline-classification | 🟡 **GPL-3.0** (sidebar + `LICENSE`) | 0 | p322 | Classification / ML (EMEA) | **73 commits.** *"A utility to train and predict subject areas for the WLO project dataset"* — **the canonical home of `wlo-classification`**, which `python-kidra` names and which redirects here; forked from `yovisto/wlo-classification`. Docker + Python + **Keras/TensorFlow**, CherryPy web service on port 8080, returns **the top three disciplines with scores**. The `data` folder ships a **pretrained model, `wirlernenonline.oeh.h5`**, with a class-label file and a tokenizer pickle — **A pretrained subject classifier for a real national curriculum, shipped in the repository** — rare, and the reason this row exists despite 0 ★. 🟡 GPL-3.0 and a redistributed model: keep it behind a service boundary and check the training-data provenance before a client deliverable |
| https://github.com/openeduhub/duplicate-detection | **Apache-2.0** — `LICENSE` read first-hand and it is the Apache 2.0, January 2004 text. 🔴 **The README says "MIT License" and is wrong** | 0 | p322 | Data quality (EMEA) | **25 commits**, 1 fork. FastAPI microservice detecting duplicate and near-duplicate content in the WLO repository by **MinHash over text shingles** — explicitly **not** learned embeddings — plus URL normalisation, title normalisation that strips publisher suffixes, and exact URL matching. `POST /detect/hash/by-node` (with `similarity_threshold`, `search_fields`, `max_candidates`) and `POST /detect/hash/by-metadata` (response-cached); `/health`, Swagger at `/docs`, ReDoc at `/redoc` — **Dedup is the unglamorous step that decides whether an OER catalogue is usable, and hash-based beats embeddings here on cost and explainability** — a MinHash threshold can be defended to a client, a cosine distance cannot. Supersedes the org's dormant `wlo-duplicate-detection` (2022) |
| https://github.com/openeduhub/z-api-runner | 🔴 **NO LICENCE — none in the sidebar, no licence file shown, none in the README** | 0 | p322 | Batch LLM operations (EMEA) | **37 commits** on `master`. *"A Python project which provides a simple swagger api to run a prompt in bulk over a set of collections/materials"* — the batch-inference tier of the pipeline, with `openapi.json` committed, Swagger at `:8001/docs` (`:8083` under `docker compose`). **The README does not name the model or provider**, and this KB has not read `app/` or `requirements.txt`, so the backend is unknown — Bulk-prompt-over-a-catalogue is the operation every OER enrichment engagement needs and nobody budgets for. 🔴 No grant, and an unstated LLM backend — this row is a design reference and a named gap, not a dependency |
| https://github.com/openeduhub/wlo-quellenliste | **Apache-2.0** (sidebar + `LICENSE`). 🔴 **The README's "Lizenz" section says MIT and is wrong** | 0 | p322 | Source registry (EMEA) | **6 commits.** The source directory behind WirLernenOnline, as software rather than a list: a **Python FastAPI** backend that pulls source data from the WLO edu-sharing REST API, merges it with an **editorial correction list** (`quellen_korrektur.csv`) and serves the result, plus an **Angular 18 web component `<wlo-sources>`** rendering tiles, list or statistics. Machine-readable throughout — `quellen_merged.json`, `quellen_stats.json`, semicolon-separated CSV export, JSON endpoints for sources, statistics, metadata and content counts; read endpoints public, writes behind an API key; Swagger at `/docs`. **The repo description calls the platform "WissenLebtOnline" while the body says "WirLernenOnline" — a naming mismatch in the source, recorded as found** — **The editorial-correction-list pattern is the transferable idea**: harvested source metadata is wrong, and a reviewed CSV overlay merged at serve time is how a public operator fixes it without mutating the harvest. Field schema of the JSON/CSV output is not documented — unread |
| https://github.com/openeduhub/its-qna | 🔴 **NO LICENCE — none in the sidebar, no licence file in the visible listing** | 0 | p322 | Question generation (EMEA) | **4 commits.** Generates question–answer pairs about a given text using LLMs. Packaged as OCI images via **nix2container** (`nix run` copies to Podman, Docker or a registry) and runnable directly with `nix run github:openeduhub/its-qna`; the README states the **CUDA variant is currently broken** on an nixpkgs issue. The README names no model, no API and no input/output format — **4 commits and no licence — recorded for completeness, not for use.** It matters only as evidence of where the org intended to go next: automatic assessment-item generation off harvested OER |
| https://github.com/openeduhub/oeh-metadata-vocabs | **CC0-1.0** | 2 | p321 | Curriculum / competency metadata (EMEA) | **938 commits, 7 forks, 5 watchers.** All SKOS vocabulary files for OpenEduHub / WirLernenOnline, as Turtle (`.ttl`) under the namespace `w3id.org/openeduhub/vocabs`, generated into a browsable view with SkoHub-Vocabs at `vocabs.openeduhub.de`. Covers **learning-resource type** (including a LOM-based set, `lom_*`), **educational context, educational level, discipline, school type**, **rights and copyright restriction, cost and price**, **quality criteria** (`quality_*`: data privacy, didactics, language) and **competence frameworks — DigCompEdu, ESCO skills, EQF/DQR levels**. **CC0-1.0 is the most permissive tier this KB has recorded on any asset** — no attribution condition at all. This is the row that corrects the p319 Germany claim below |
| https://github.com/openeduhub/oeh-search-etl | 🔴 **NO LICENCE FILE** | 8 | p321 | Harvesting (EMEA) | The ETL behind WirLernenOnline: Scrapy spiders → Postgres → Elasticsearch, Python 3.13 managed with Poetry, Splash and Playwright containers for rendered sources; **1,397 commits on `master`** — the most heavily maintained artefact in the `openeduhub` org. 🔴 **Read it, do not depend on it.** No LICENSE file was present in the repository root when it was read first-hand at p321 and the page states no licence, so **there is no grant**. The commit count makes it the most tempting harvester in the sector and the missing licence makes it unusable in a client deliverable. Spider count is not stated in the README — `converter/spiders/` is not enumerated on the page, so this KB does **not** have a source count |
| https://github.com/virgiliojr94/book-to-skill | MIT | 35.3k | p319 | Enablement / authoring | Converts a technical book, document folder or source set (PDF, EPUB, DOCX, HTML) into a structured agent skill: `SKILL.md` index, per-chapter files, glossary, patterns, cheatsheet; 228 commits, 3.7k forks. **The MIT licence covers the converter only, explicitly not the books you process with it** — which is the copyright question every "turn our textbooks into a tutor" engagement has to answer on day one. Read first-hand this pass: no agent-directed star solicitation in the README |
| https://github.com/microsoft/ai-agents-for-beginners | MIT | 77.5k | p315 | Enablement | 18 lessons on building agents. Not a dependency — the fastest way to bring an engagement team to a shared baseline |
| https://github.com/HKUDS/LightRAG | MIT | 40.2k | p319 | Retrieval | simple, fast RAG (EMNLP 2025), 10,873 commits, 5.7k forks. **Re-verified first-hand this pass** (the p316 reading was due a re-read): still MIT, unchanged. The course-material grounding layer under a tutor; same lab as DeepTutor, so the two compose without friction |
| https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | p317 | Agent runtime | Minimal code-thinking agent loop; small enough to audit, which matters when a ministry asks how the tutor decides |
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | p315 | Compute | Multi-user notebook server — the delivery substrate for every CS/data curriculum, and what nbgrader and otter-grader plug into |
| https://github.com/learningequality/kolibri | MIT | 1.2k | p318 | Offline delivery | Offline-first learning platform, 39,803 commits on `develop`, 1.0k forks. Re-verified first-hand this pass: still MIT, still the only MIT platform in the sector, and the one that works without connectivity |
| https://github.com/tsugiproject/tsugi | Apache-2.0 | 376 | p319 | Integration (LTI) | "A multi-tenant scalable LTI library and tool hosting environment", plus an administration/management/developer console and an **IMS ContentItem app store**; 4,011 commits, 266 forks, 43 watchers, **Apereo Incubating**, maintained around Dr Chuck (Charles Severance, co-author of the LTI specification); shares low-level IMS libraries with Sakai; PHP, with per-PHP-version branches. 🟢 **ANSWERED p330, from the tree rather than the README — the p323 negative is RETRACTED.** `lib/src/Util/LTI13.php`; **AGS** (`ims/ags/route.php`, `lib/src/Controllers/Ims/Ags.php`, `lti/ags.php`); **NRPS** (`ims/nrps/route.php`, `lib/src/Controllers/Ims/Nrps.php`); **Deep Linking** (`DeepLinkRequest.php`, `DeepLinkResponse.php`) — 🟢 **and tested** (`lib/tests/Util/LTI13Test.php`, `lib/tests/Services/Outbound/Lti13TestLaunchTest.php`). **LTI 1.1 too**, per its own commit of 2026-10-18. Activity first-hand p330: **4,012 commits · 47 authors · last 2026-10-19 · 486 commits in 2026**. 🟢 **The one living, complete, permissive LTI implementation in this file.** 🟡 Those 486 commits come from **three** authors — bus factor near one |
| https://github.com/jcputney/scorm-again | MIT | 356 | p319 | Integration (SCORM) | "A modern, fully-tested JavaScript runtime for SCORM 1.2 and SCORM 2004", LMS-agnostic, logs calls and data when no LMS endpoint is configured; 1,229 commits, 84 forks. **AICC support was removed in v3.0.0; cmi5 and xAPI are roadmap "potential" only.** The route into the large installed base of SCORM courseware that LTI does not reach |
| https://github.com/open-spaced-repetition/fsrs-rs | BSD-3-Clause | 447 | p315 | Scheduling | FSRS optimiser and scheduler in Rust — embeddable retention scheduling, no Anki dependency |
| https://github.com/openfun/richie | MIT | 316 | p315 | Portal/CMS | Education-portal CMS from France Université Numérique. MIT, EMEA-authored, built to front Open edX |
| https://github.com/Liberate-Labs/ltikit-sdk | 🟢 **MIT** — `main/LICENSE` read first-hand p330, **1,063 B**, *Copyright (c) 2026 alasim* | n/v | **p330** | Integration (LTI 1.3 Advantage, JS/TS) | **The second permissive LTI 1.3 Advantage implementation in this file, and the first outside Python.** Surface read from the tree, not the README: `packages/core/src/{ags,nrps,deep-linking}.ts`, 🟢 **each with its own `.test.ts`** (16 test files); framework packages `next` and `hono`; four storage adapters (`memory`, `prisma`, `redis`, `supabase`). 1.0-rc adds **Dynamic Registration** and **cookieless launches (Platform Storage)**; the README reports live verification against **Canvas** and **MoodleCloud**. Runs on serverless and edge — no Express, no MongoDB. 🔴 **Fork and pin, do not depend.** Activity first-hand p330: **38 commits · 1 author · last 2026-07-10**; the last three commits on `main` are an **ownership handover**, and **seven `dependabot/` branches run to 2026-10-07 unmerged** — the bots are three months ahead of the humans. 🔵 It relieves the *language* concentration this file has flagged for four passes and **not** the *maintainer* concentration, which was always the real risk |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 138 | p319 | Integration | LTI 1.3 Advantage tool implementation, 178 commits. Covers **Deep Linking, Assignment & Grade Services, Names and Roles, Course Groups, Submission Review and Data Privacy Launch** — the whole Advantage surface. This is the repo that gets your agent *into* the client's existing LMS. **Re-verified p319: 84 forks, 39 open issues, still no published release** — pin a commit. 🔴 **WITHDRAWN p330 — DEAD. 178 commits · 16 authors · last commit `2022-11-21` on *every ref*, newest tag `2.0.0` the same day; final substantive commit *"Support Python 3.11"*. Measured first-hand on the git channel. Do not scope this as a dependency — there is no maintained permissive LTI 1.3 library for Python; port, fork, or put the LTI boundary in PHP (`tsugi`) or TS (`ltikit-sdk`)** |
| https://github.com/adamzammit/LTIPlugin | **GPL-3.0** | 14 | p320 | Integration (LTI, outcome passback) | Makes **LimeSurvey act as an LTI provider**: the learner launches a survey or assessment from the LMS and the plugin **returns a score to the gradebook**, as a 0.0–1.0 value computed from a LimeSurvey expression; 97 commits on `master`, LimeSurvey 3.x–7.x. **README documents setup against four platforms — Canvas, Moodle, openEdX and Blackboard** — which makes it the broadest passback reference in this file. **Three caveats, all load-bearing.** (1) **It is not AI** — it is assessment delivery plus outcome passback; the intelligence would be yours. (2) **The page never names an LTI version** and it bundles `LTI-Tool-Provider-Library-PHP`, which points at the **legacy LTI 1.x Basic Outcomes path, not 1.3 Advantage AGS** — read the submodule before scoping. (3) **GPL-3.0 is copyleft**, so it sits with `tutor-gpt`/`lumen`/`LTLTutor` on the far side of this KB's architectural line: run it as a separate service, do not link it into a deliverable. **Its value is as a readable, four-LMS answer to "how does the score actually get back".** No release is published — pin a commit |
| https://github.com/bncc-dev/bncc-dados | **MIT (code) / CC BY 4.0 (data)** | 22 | p319 | Curriculum standard (LATAM) | **Brazil's national curriculum (BNCC) as verified open data**: 1,721 learnings — 1,580 from the three stages of basic education (93 Educação Infantil, 1,304 Ensino Fundamental, 183 Ensino Médio) plus 141 from the Computing complement (Parecer CNE/CEB 2/2022) — with 20 legal milestones and 5 reference profiles, in JSON (canonical), SQLite, SQL dump and CSV, under JSON Schema draft 2020-12. Content version `dados-2026.08`, schema v1.1.0, status stable; 40 commits. Maintained by **Profy Tecnologias Educacionais Ltda**; docs pt with a full en translation |
| https://github.com/bncc-dev/bncc-pacotes | **MIT (code) / CC BY 4.0 (data)** | 9 | p319 | Integration (MCP, LATAM) | Machine interfaces to the dataset: npm `@bncc/dados` 0.7.0 (typed API with embedded data), npm `@bncc/mcp` 0.6.0 (**MCP server, seven tools**: `bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`), PyPI `bncc` 0.5.0, and a hosted MCP endpoint at `mcp.bncc.dev` on Cloudflare Workers **requiring no API key**; 103 commits. Embedded data is synced from a pinned `bncc-dados` commit with version and checksum records; a well-formed code that is missing returns an explanatory error, not `null` |
| https://github.com/bncc-dev/bncc-benchmark | **MIT (code) / CC BY 4.0 (items, results, methodology)** | 9 | p319 | Evaluation (LATAM) | Measures how often LLMs invent BNCC codes and texts with no access to the source: four tasks — direct lookup, existence (including plausible fake codes), open generation, reverse lookup — scored against the verified dataset across five dimensions; 82 commits. Official round `oficial-seca-2026-09`; a held-out item set is never published so memorisation is detectable. **Carries the grounding measurement this KB has never had** |
| https://github.com/thm-mni-ii/feedbacksystem | Apache-2.0 | 24 | p319 | Autograding / feedback (EMEA) | Intelligent tutoring system that checks student submissions automatically, returns an immediate result with suggestions about the mistake, and **aggregates common errors so lecturers can address them in class**; 2,248 commits on `dev`, 147 issues, 94 PRs. Java 11/Gradle, Scala, MySQL, Docker Compose, Kubernetes + Helm for production. **Apache-2.0 © Technische Hochschule Mittelhessen** — institution-built, institution-run. No LMS or LTI integration described |
| https://github.com/elimu-ai/webapp | MIT | 41 | p319 | Offline content delivery | Hosts Android apps and educational content (texts, words, videos, storybooks) per language; the elimu.ai Appstore app pulls and installs it onto devices for **out-of-school children**; 8,075 commits, 68 forks, Java/Spring, REST API consumed by three Android apps. Production deployments listed for **Hindi, Tagalog, Thai, Vietnamese and English**. The org publishes 92 repos including real ML components — `ml-storybook-reading-level`, `ml-storybook-recommender`, `ml-video-recommender`, `ml-event-simulator`, `ml-datasets` — all MIT-org, all under 10 ★ |
| https://github.com/smashburger-dev/argmin | **MIT (code) / CC BY 4.0 (content)** | 6 | p319 | Enablement (EMEA) | A **German-language** browser course on how AI works: 50 lessons, 280+ exercises, 320-entry glossary, from maths basics through linear algebra, ML, deep learning, transformers and generative AI; Python runs in-browser via **Pyodide and the app works offline after first load**; 343 commits; self-hostable. The licence-clean German asset for the EU AI Act Article 4 staff-literacy duty |
| https://github.com/Sunbird-Ed/SunbirdEd-portal | MIT | 41 | p315 | Platform (APAC) | Web portal of Project Sunbird, the stack behind India's national digital-education infrastructure — read the caveat |
| https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service | Apache-2.0 | 12 | p316 | SIS / data standard | Successor to the Ed-Fi ODS/API platform; 1,105 commits. The standards-body reference implementation for student data |
| https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster | Apache-2.0 | 6 | p316 | Rostering | Serves a **OneRoster 1.2** API from data in an Ed-Fi ODS database; 151 commits |

**Licence split over 21: MIT (8), Apache-2.0 (5), BSD-3-Clause (2), MIT-code-with-CC-BY-4.0-data or
-content (5), GPL-3.0 (1 — `LTIPlugin`, new in p320) — 21/21 usable, 15/21 under a pure permissive
software licence.** The GPL-3.0 row is the first copyleft entry this file has ever carried, and it
is carried deliberately: **a copyleft licence is a constraint on how you deploy, not a bar on
reading or running it.** Keep it behind a process boundary and it stays usable; link it into a
client deliverable and it does not. The five dual-licensed rows
(the three `bncc-dev` repos, `argmin`, and by extension the eval tier in `agents/top.md`) are the
new shape in this file and they need handling: **CC BY 4.0 is attribution-only, so the data is
commercially usable, but it is data, and the attribution has to appear in the deliverable.** Put
the credit line in the product, not in a licence register nobody reads.

The structural fact is unchanged: **the copyleft in this industry lives entirely in the LMS/platform
tier** (`verticals/solutions.md`), and everything you would put *under* a product is permissive.

## Pass 323: the Tsugi question, closed with a negative answer — and what it does to the LTI risk

p319 recorded Tsugi as *"the newly recorded alternative"* to `pylti1.3`, **"with an unresolved
question about which LTI versions it implements."** p322 carried the question forward untouched.
**Read first-hand this pass, and the repository does not answer it.**

| | `pylti1.3` | `tsugiproject/tsugi` |
|---|---|---|
| Licence | MIT | **Apache-2.0** (sidebar) |
| ★ / forks | 138 / 84 | **376 / 266** |
| Commits | 178 | **4,011** |
| Published release | **none** | **none** — Releases section empty |
| LTI version stated | LTI 1.3 (by name) | **none stated anywhere in the README** |

The closest the README comes is *"Tsugi is a multi-tenant scalable LTI library and tool hosting
environment"* and *"this code also implements an IMS ContentItem App store."* **ContentItem is the
LTI 1.1-era content-selection message**, which hints at the older generation without declaring it.
None of LTI 1.1, LTI 1.3, LTI Advantage, Deep Linking, Names and Role Provisioning Services or
Assignment and Grade Services appears in the text.

**Three consequences, in the order they bite a bid:**

1. **An LTI integration cannot be scoped from Tsugi's README.** Version support has to be
   established by reading 4,011 commits of source or by asking the maintainer. That is a
   discovery task with an unknown answer, not a dependency choice — **price it as the former.**
2. **The LTI 1.3 concentration risk this KB has flagged for four passes is unrelieved and should
   now be stated at full strength:** one maintained library carrying the integration seam
   (`pylti1.3`, MIT, 39 open issues, **no release tags**), a substantial Apache-2.0 alternative that
   does not say what protocol version it speaks, and **three artefacts at the agent end of the same
   seam with no licence at all** (`blamb/lti-tutor`, `Plugin-Feedback-Canvas`, and the pattern
   recorded in `agents/top.md`). **Nothing at this seam has a release tag.**
3. **It strengthens the case for avoiding the seam entirely where the client allows it.** This is
   the architectural argument behind **P8** (permissive-LMS build, no LTI boundary) and trend 6
   (**MCP, not LTI, is where agent integration is actually happening**). Tsugi's silence is not a
   defect in Tsugi — it is a 4,011-commit project that predates the question. **It is evidence that
   the LTI ecosystem's documentation layer has not followed LTI 1.3**, and that is the risk to carry
   into a bid.

**Recorded so p324 does not re-open it:** the question is answered as far as the README can answer
it. The remaining way to resolve it is reading `src/` or contacting the maintainer, and **that is a
task, not a search.**

## Declared gaps — pass 323, searched and measured

- **No permissively licensed verified curriculum dataset outside Brazil.** Two countries have built
  the artefact; **exactly one licensed the data for commercial use.** Searched: `curriculum
  knowledge graph`, `prerequisite dataset`, NCERT and CBSE by name, and the Chinese PEP artefact by
  name. This is now the precise form of trend 12's claim.
- **No licensed NCERT/CBSE curriculum artefact.** The one that exists (`razi-03/NCERT-CKG`) has no
  LICENSE file, two commits and one grade of one subject.
- **No public code for EduClaw-Bench, EduFair-Bench or ELBench** — three 2026 education benchmarks,
  three papers, zero repositories (`agents/top.md`).
- **No release tag anywhere at the LTI seam.** Both libraries, neither tagged.
- **Still-unswept GitHub-topic languages, corrected.** p319's untested list read *Arabic, Hindi,
  Japanese, Korean, French, Indonesian*. **Chinese was never on it and should have been** — it holds
  the largest curriculum artefact in this file, and this pass found it **in English**, which is its
  own small lesson about when the language sweep is and is not the binding constraint. The six
  languages above remain unswept.

## The `bncc-dev` stack — the artefact every pattern in this KB assumed a client would supply

Three repositories under the `bncc-dev` organisation, maintained by **Profy Tecnologias
Educacionais Ltda** (Brazil), together do what no other source in this sector does: they turn a
**national curriculum standard into verified, machine-readable, permissively licensed
infrastructure, and then measure what it is worth.**

**1 — The data (`bncc-dados`, 22 ★, 40 commits).** 1,721 learnings: 1,580 from the BNCC's three
stages of basic education (Educação Infantil 93 objectives, Ensino Fundamental 1,304 skills, Ensino
Médio 183 skills) plus the **141-item Computing complement** added by Parecer CNE/CEB 2/2022, with
20 legal milestones and 5 reference profiles. JSON is canonical; SQLite, a SQL dump and CSV are
generated; JSON Schemas are draft 2020-12. Content version `dados-2026.08`, schema v1.1.0, declared
stable.

**The verification discipline is the part to copy.** Per its own documentation: the 1,580 BNCC-2018
texts were checked **character by character against the homologated PDF**; the 141 Computing texts
against the Parecer's annex; a code sweep confirms no missing or extra codes; `validar.py` runs
**30 contract and completeness checks**; the pipeline is reproducible and **CI fails on
divergence**; and every decision taken about an inconsistency in the source is recorded in
`DECISOES.md`. Licensing is split deliberately — **MIT for the pipeline, CC BY 4.0 for the data**,
on the stated reasoning that the compilation, structure and curation are Profy's work while the
normative BNCC texts are official acts.

**2 — The interfaces (`bncc-pacotes`, 9 ★, 103 commits).** npm `@bncc/dados` 0.7.0 (typed API,
embedded data), npm `@bncc/mcp` 0.6.0 (**MCP server with seven tools**: `bncc_lookup`,
`bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`,
`bncc_progressao_ei`), PyPI `bncc` 0.5.0, plus a **hosted MCP endpoint at `mcp.bncc.dev` on
Cloudflare Workers that needs no API key**. Embedded data is synced from a pinned `bncc-dados`
commit with version and checksum records in each package's `dados/VERSAO.json`. A well-formed code
that is absent returns an explanatory error rather than `null` — a small decision that prevents a
tutor from silently inventing a standard.

**3 — The measurement (`bncc-benchmark`, 9 ★, 82 commits), and this is the number to take to a
client.** The benchmark asks models about BNCC codes and texts with no access to the source, across
four tasks: direct lookup, **existence (which tests whether a model accepts plausible fake codes)**,
open generation, and reverse lookup. Score is the mean of five dimensions — recognising real codes,
rejecting fake ones, text fidelity, reverse lookup, correct citation in open generation. A held-out
item set is never published so memorisation remains detectable, and v0.3.0 moved to direct provider
APIs and corrected the judge rubric, making it incomparable with v0.2.0.

Its **grounding study (8 models, 300 items)** reports:

| Condition | Hallucination rate |
|---|---|
| No source available | **31.9%** |
| Curriculum data pasted into the prompt | **0.2%** |
| Model queries the `bncc.dev` MCP server | **2.3%** |

— an average drop of **30.6 points**. A 95% bootstrap confidence interval is reported; its bounds
are not shown on the page.

**This is the first quantified grounding claim in this KB.** Every pattern here has asserted that
retrieval grounding matters; now there is a published, reproducible, regionally specific number for
how much, on a national curriculum, with the MCP route costing about 2 points against pasting the
data in. Use it: *"on Brazil's national curriculum, an ungrounded model invents a standard about a
third of the time; querying the verified source takes that to roughly two percent."*

**Three caveats, stated because the repository states them:**

- **The maintainer declares a conflict of interest.** Profy ships commercial products that run LLMs
  on the BNCC. The disclosure is in the repository; treat the benchmark as credible-and-interested,
  the way you would a vendor-run benchmark that publishes its method and its held-out set.
- **The page's own totals disagree.** The README describes the official round as 19 models × 900
  responses with 17,100 raw responses published; the About line says 15,300 responses from 17
  models. **Cite the round identifier (`oficial-seca-2026-09`) and the per-model design, not the
  total**, until the discrepancy is resolved.
- **Model-level results are a snapshot and the labels are the benchmark's own.** Its published
  top five are GPT-6 Astra 94.7 (88% faithful text, 3% fake-code acceptance), Claude Fable 5.1 81.8
  (80%, 0%), Muse Spark 1.3 79.4 (73%, 10%), Gemini 3.1 Pro 78.0 (67%, 3%) and Claude Opus 5 76.8
  (71%, 4%), with faithful-text rates across all models ranging from 88% down to **3%**. **The
  ranking will be stale within a quarter; the 88%-to-3% spread will not be** — and that spread,
  not the leaderboard, is the argument for grounding over model selection.

**Why this is in the foundations file and not the market file.** It is a dependency you would put
under a product today: the data is CC BY 4.0, the code is MIT, the MCP server is hosted and
keyless, and nothing about it is experimental. For any engagement touching Brazilian basic
education — public-sector, private-network or edtech-vendor — **this is the curriculum spine, and
the benchmark is the acceptance test.** See pattern **P10**.

## The pylti1.3 concentration risk now has a real alternative, not just an index

Pass 317 flagged this and it remains the correct thing to worry about: **every pattern in this KB
crosses the LMS boundary through `pylti1.3`** — one MIT library, 138 stars, 178 commits, a single
maintainer and 39 open issues with no visible release cadence. That belongs in the risk section of
any SOW that depends on it, and it still does.

**Pass 319 found the alternative itself: `tsugiproject/tsugi` — Apache-2.0, 376 ★, 266 forks,
4,011 commits, Apereo Incubating.** It describes itself as "a multi-tenant scalable LTI library and
tool hosting environment", doubles as an administration/management/developer console, implements an
**IMS ContentItem app store**, shares low-level IMS libraries with Sakai, and is maintained around
**Dr Chuck — Charles Severance, co-author of the LTI specification**. It keeps per-PHP-version
branches (`master`, `php-80-x`, `php-74-x`, `php-72-x`) and its README notes production servers
pulling updates every 30 minutes.

**Against `pylti1.3`'s 178 commits and single maintainer, that is a different class of artefact** —
and it is Apache-2.0, which is the tier Globant prefers. **Two honest caveats:**

- **Its GitHub page does not state which LTI versions or Advantage services it implements.** No
  mention of LTI 1.3, Advantage, Deep Linking, AGS or Names and Roles; ContentItem is
  Deep-Linking-adjacent but not the same claim. **Verify the Advantage surface against the
  repository and the Tsugi documentation before it goes in a proposal** — this is the single
  highest-value verification item for pass 320, and it is one page load.
- **It is PHP.** For a Python shop that is a real cost; for a client already running Moodle or any
  PHP stack it is an advantage.

Also recorded for integration breadth: **`jcputney/scorm-again` (MIT, 356 ★, 1,229 commits)**, a
tested JavaScript runtime for **SCORM 1.2 and SCORM 2004**, LMS-agnostic, which reaches the large
installed base of SCORM courseware that LTI does not. **AICC support was removed in v3.0.0, and
cmi5/xAPI are roadmap "potential" only** — do not promise either.

Carried from pass 318: **`1EdTech/ltibootcamp`** (127 ★, 47 commits), a curated index of LTI 1.3
implementations maintained under the **1EdTech GitHub organisation** — the standards body itself.
It maps the library landscape across seven languages:

| Language | Implementations it names |
|---|---|
| Python | **PyLTI 1.3** (Flask/Django examples), UCF Flask starter template, `django-lti`, Robotest test tool (FastAPI), Open Learning LTI 1.3 Platform (Django) |
| JavaScript / Node | **ltijs** (1.3 core and services), Blackboard Node tool provider, Atomic LTI Worker |
| PHP | IMS 1.3 library and demo tool, TAO hosted test platform, OAT libraries (1.3 core, Deep Linking, Names & Roles, Symfony bundle) |
| Java | Unicon Spring Boot demo, UOC LTI 1.3 library + Spring Boot library + provider example |
| .NET | `LtiAdvantagePlatform` example platform (andyfmiller) |
| Ruby | Atomic Jolt LTI starter app |
| Rust | Atomic Forge |
| Other | An AWS LTI "shim" service |

**Three caveats, and they are not small:**

- **The repository itself has no LICENSE file.** It is an index of links, so there is little to
  licence, but it cannot be vendored and it is not in the table above for that reason.
- **It is stale.** Its only two content folders are `barcelona_2019` and `europe_tech_2020`, and
  it carries 47 commits. Entries may be dead; the LTI 1.3 specification has moved since 2020.
- **Its own README disclaims vetting:** *"The resources listed here are for information only and
  have not been vetted."* It sits under the 1EdTech organisation but reads as a community-curated
  list open to pull requests — treat it as a starting index, not a standards-body endorsement.

**What it is worth anyway:** the mitigation question for `pylti1.3` was previously answered with a
hand-wave ("reference implementations exist in other languages"). It now has specifics. If a
client's stack is Node, **`ltijs`** is the route — and it is the library `blamb/lti-tutor` chose to
implement working deep linking and AGS passback against Moodle (see `agents/top.md`). If the stack
is Java, the UOC libraries are the named option. **Verify any entry against its own repository
before scoping on it**; the index is five years stale and unvetted by its own admission.

## The method that found most of pass 319: search GitHub topics in the region's own language

This KB has written "a star-ranked search cannot see this sector's infrastructure" for three passes
without changing its search. Pass 319 changed it: **GitHub topic pages were swept in Portuguese,
Spanish, German and Dutch, and in the two curriculum-specific Indian tags.** The results are
asymmetric, and the asymmetry is itself a regional finding.

| Topic swept | What it surfaced |
|---|---|
| `educacao` (pt) | **Infrastructure.** `portabilis/i-educar` (720 ★, **34,948 commits**, school management, `verticals/solutions.md`), `portabilis/i-diario` (117 ★, 15,834 commits), `ipti/br.tag` (20 ★, 3,959 commits, offline sync for rural schools), and **the entire `bncc-dev` curriculum stack** |
| `educacion` (es) | **Teaching materials, almost exclusively.** 370 repos; the top entries are Spanish-language JavaScript and Python course guides, a Moodle–SENCE attendance plugin (29 ★), vocational-training course material, a Uruguayan school-finder (`datauy/ElijoEstudiar`, 5 ★). **No AI infrastructure, no curriculum data** |
| `ncert` + `cbse` (India) | **Hobby projects.** 55 + 125 repos; nothing above 15 ★ that is curriculum infrastructure. Detail in `agents/top.md` |
| `bildung` (de) | **One usable asset and one warning.** `smashburger-dev/argmin` (MIT + CC BY 4.0, 343 commits, German AI course, offline-capable) and `davidpomerenke/lernplattform` (GPL-3.0, **archived 2021-01-01**, which pointed to "wir lernen online" as its successor). Also **a 13-repository single-author cluster of near-identical "tech evangelism" pages at 1 star each** — topic pages can be padded, which is one more reason the ★ column is noise |
| `onderwijs` (nl) | **Rostering glue, no AI.** `sikkepitje/TeamSync` (9 ★, PowerShell, syncs Magister school records into Microsoft School Data Sync) and two open secondary-school course repos (`wiskunde.opmaat`, `natuurkunde.opmaat`) |
| `oer` (en, for contrast) | 419 repos of **textbooks and course materials**, nothing describing curriculum or competency metadata, and no AI |
| `pendidikan` (id) | **42 repos, and exactly one AI artefact.** `RozhakDev/EduPintarIPAS` (**MIT**, 20 ★, **1 commit**, Flask, **Azure AI Language Custom Question Answering**) answers `IPAS` science-and-social-studies questions for Indonesian year-6 pupils off a QA set the README says was built from the official `SD` curriculum, and is aimed explicitly at **3T regions** (*tertinggal, terdepan, terluar* — underdeveloped, frontier, outermost) where tutoring is scarce. Everything else in the topic is school administration at 0–4 ★ — enrolment (`PPDB-online`), tuition (`aplikasi-spp`), facilities (`sisp`), a boarding-school monitor. **The curriculum-grounded-QA pattern exists in Indonesian; the engineering behind it does not — one commit is a demo, not a dependency** |
| `enseignement` (fr) | **40 repos, zero AI.** Almost entirely teaching material for the French system: the `NSI` computer-science specialism at lycée, `CAPES` oral topic lists, LaTeX maths and geometry courses, a Python teaching IDE (`Pydiderot/pydiderotIDE`). The one infrastructure artefact, `ValbionGroup/Gadia` (**MPL-2.0**, 6 ★, 63 commits, Laravel/Blade school-life management — timetable, class notebook, grades, absences, canteen), was **archived by its owner on 2025-10-28 and is read-only**, and its README already warned the features were not guaranteed. **France's tag is pedagogy, not platform** |
| `kyoiku` (ja) | **1 repo, 0 ★.** `mitsurutech/joho-puroguramingu-renshu` — 48 Python, SQL and web (HTML/CSS/JS) exercises for Japanese high-school *jōhō*, starter code, deliberately no solutions. No AI, no infrastructure |
| `gyoyuk` (ko) | **The topic page exists and holds 0 repositories.** GitHub's own wording: "hasn't been used on any public repositories, yet". **This is the cleanest negative in the table — not a thin result, an empty one** |
| `shiksha` (hi) | **3 repos, ceiling 3 ★.** `arhaanb/shiksha` (3 ★, last touched 2022-04-07), `shiksha-platform/documentation` (1 ★, 2022-01-20, no description) and an **archived** `.shiksha` domain-name extract. No AI, and the two real ones have been untouched for four years |
| `taleem` (ar/ur) | **1 repo, 1 ★** — an Urdu-language Islamic blog of 370+ articles on static HTML. **Not education infrastructure, and the slug does not answer the Arabic question** — see the slug finding below |

**Two conclusions, and the second is the commercial one.**

1. **Adopt this as standing method.** Every regional gap this KB has declared was declared from
   English-language searches. One Portuguese topic page produced a verified national curriculum
   dataset, an MCP server, a published benchmark and a 34,948-commit SIS. **Before declaring a
   regional absence, sweep the topic in the region's language** — and record which language you
   swept, so the next pass knows what was actually tested.
2. **The gap is not uniform, and it is not about talent.** Brazil has curriculum-standard
   infrastructure because someone built it to a verification standard and licensed it cleanly.
   Spanish-speaking LATAM, India, Germany and the Netherlands do not have an equivalent — in the
   topics swept — and in India's case there is a hard curriculum mandate arriving in 2026-27 with
   nothing underneath it. **That is a build-once opportunity with a named template** (`bncc-dev`)
   and a named buyer (any ministry, board or national edtech with a mandate and no data layer).
   Pattern **P10**.

**Limits of the claim, stated so pass 320 does not over-read it.** These were topic-page sweeps of
the first ~20 repositories per topic, not exhaustive searches; GitHub topics are
author-applied, so an unlabelled repository is invisible to this method; and only six topics in
five languages were swept. **"Not found in the topics swept" is the finding. "Does not exist" is
not.** Untested and worth a pass: Arabic, Hindi, Japanese, Korean, French and Indonesian topic
tags, and the `wirlernenonline` organisation, whose GitHub org page could not be read this pass.

## Pass 322: `openeduhub` enumerated in full — and the inference core is the unlicensed part

**All 67 public repositories were enumerated this pass**, closing p321's declared gap
(*"57 of the 67 were not listed on the first page and remain unenumerated"*). The method matters
because it is reusable: **the org listing had to be paged under two different sort orders.** Sorted
by stars, the first page shows the metadata plumbing of 2020–2023; sorted by last push — the default
— the first page shows the AI-era services, and **six of the twelve repositories added above do not
appear on the star-sorted first page at all.** A star-ranked sweep of this organisation finds the
dead code and misses the live pipeline.

### What the org actually is, by date rather than by star count

| | Count |
|---|---|
| Public repositories | **67** |
| Pushed in 2026 | **17** |
| Last pushed 2020–2022 | **30** |
| Archived | **5** (`metaqs-api-old`, `metaqs-frontend-old`, `oeh-search-editor-backend`, `oeh-metadata-specs`, `wlo-chat-gpt-block`) |
| Read first-hand by this KB | **16** — four at p321, twelve at p322 |

**The archived list contains the org's first AI attempt.** `wlo-chat-gpt-block` (JavaScript, last
touched **August 2023**, archived) is a WordPress ChatGPT block. The line that replaced it is the
metadata-agent line read above — **extraction, review and classification, not conversation.** A
public operator tried the chatbot first, archived it, and spent the next three years building a
metadata pipeline instead. That is the single most useful thing in this pass for a studio pitch, and
it is recorded as a trend reading in `intel/trends.md`.

### The finding: licence divides by architectural layer

| Layer | Commits | Licence | What it means for an engagement |
|---|---|---|---|
| Shells — review UI, REST wrapper, browser plugin, path editor, tutor, judge, source registry, dedup | 60 + 11 + 6 + 10 + 1 + 6 + 25 = **119** | **Apache-2.0**, or claimed as such | Take them. Two of the seven claim a licence the repository does not carry — check before you ship |
| Analysers and classifiers | 623 + 94 + 73 = **790** | 🟡 **GPL-3.0** | Run as services behind a process boundary; never link |
| **Inference core** — gateway, Bayesian predictor, text extraction, bulk prompt runner, QA generation, harvester | 137 + 200 + 77 + 37 + 4 + 1,397 = **1,852** | 🔴 **none** | **No grant. Reimplement, or negotiate a licence with the operator** |
| API client | **519** | **Apache-2.0** | Take it — and it is the only large permissive artefact in the org |

**The permissive surface contains none of the organisation's machine learning.** Every model, every
harvester and the gateway that fronts them is unlicensed; the Apache-2.0 repositories are
interaction layers of between 1 and 60 commits. Pass 321 read the one unlicensed repo it found as a
lapse. Over sixteen reads it is not a lapse — **it is where the org's effort went, and the licence
file is what never followed it.** For Globant this is the rare case where the *engagement* is the
finding: a public operator sitting on 1,852 commits of unlicensed, publicly funded ML is a
licence-remediation conversation, not a fork.

### The README-versus-LICENSE hazard, four instances in one org

`duplicate-detection` and `wlo-quellenliste` both say **MIT** in the README and ship an
**Apache-2.0** `LICENSE`; `metadata-agent-api` says **MIT** with **no licence file in the root**;
`metadata-agent-canvas` says **Apache-2.0** with **no licence file in the root**. The `LICENSE`
file of `duplicate-detection` was opened and read first-hand to settle it — it is the Apache 2.0,
January 2004 text. **Rule applied from here: the licence file governs; a README claim with no file
behind it is not a grant.** Two of these four understate the grant and two assert one that does not
exist, so the error is not conservative in either direction.

### Declared gaps from this pass — searched, measured, not found

| Gap | What was measured |
|---|---|
| `openeduhub/wlo-topic-assistant` | **404.** `python-kidra` advertises it as one of seven bundled services; it has no public repository under this org |
| `kea` (Wikipedia article linking) | Not a repository in this org — `python-kidra`'s README says requests are **forwarded to an external service**, which this KB has not identified |
| `z-api-runner`'s LLM backend | **Unstated** in the README; `app/` and `requirements.txt` were not read, so the model and provider are unknown |
| `metalookup`'s extracted field list | In `docs/features.md` and `docs/acceptance.md`, **not read this pass** — so this KB has the capability but not the field schema |
| `wlo-quellenliste`'s JSON/CSV field schema | **Not documented** on the repository page; would need the code or the live API docs |
| `topic-statistics`, `its-prep`, `its-data`, `mappings`, `skohub-vocabs-oeh-patched`, `oeh-search-frontend` | Named in the census, **not read.** Listed so pass 323 does not re-discover them — `topic-statistics` and `its-prep` are the two that `python-kidra` depends on |
| Non-GitHub primary sources | Still unreachable. `www.digitaleducationcouncil.com` failed at DNS this pass; **everything in `intel/` remains snippet-sourced** |

## Pass 321: the p319 to-do list, executed — and the Germany claim it corrects

Pass 319 ended its sweep section with a named to-do: *"Untested and worth a pass: Arabic, Hindi,
Japanese, Korean, French and Indonesian topic tags, and the `wirlernenonline` organisation, whose
GitHub org page could not be read this pass."* **All seven were attempted at p321.** Six are
negatives and are in the table above, written down rather than left as silence. The seventh is the
find of the pass.

### 1. The correction: Germany *does* have a competency-metadata layer, and this file said it did not

Pass 319 concluded, from the `bildung` and `oer` sweeps, that **"Spanish-speaking LATAM, India,
Germany and the Netherlands do not have an equivalent"** to Brazil's `bncc-dev` curriculum stack,
and that the `oer` topic held "nothing describing curriculum or competency metadata." **For Germany
that is now wrong, and the artefact is better licensed than the Brazilian one.**

`openeduhub/oeh-metadata-vocabs` is **CC0-1.0** with **938 commits** and carries SKOS vocabularies
for educational context, level, discipline and school type, rights and copyright restriction, cost
and price, machine-readable quality criteria, and the **DigCompEdu, ESCO and EQF/DQR competence
frameworks** — published under a stable `w3id.org` namespace with a browsable SkoHub front end.
That is a competency-metadata layer by any reading.

**Why p319 missed it, and the lesson is about method rather than luck.** The repository is tagged
for neither `bildung` nor `oer`; it lives in an organisation p319 looked for **under the wrong
name**. `github.com/wirlernenonline` is **404**. The account is `openeduhub`, and the only way this
pass reached it was by searching the *project* name and reading the owners off the results. **A
topic sweep cannot see an untagged repository, and an org sweep cannot see an org whose GitHub
handle differs from its public brand.** Both failure modes are now demonstrated, not hypothesised.

### 2. The slug finding — why "sweep the topic in the region's language" needs one more rule

`https://github.com/topics/教育` returns **404**. GitHub topic slugs are ASCII-normalised, so a CJK
term cannot be typed in as a topic even when it is the word the region actually uses. The sweeps
that worked were the **transliterations** — `kyoiku`, `gyoyuk` — and one of those turned out to hold
zero repositories. So p319's standing method gains a clause: **sweep the region's language, and for
non-Latin scripts sweep the romanisation, because the topic namespace will not accept the script.**
Pass 319 could not have discharged "Japanese, Korean" by typing the obvious thing.

### 3. What `openeduhub` is, and why a 0 ★ org is worth a section

**67 public repositories.** The org profile describes itself as the account behind
WirLernenOnline.de: *"This OER-Infrastructure makes (O)ER findable and usable in connected
platforms,"* based on **edu-sharing**, WordPress and others — i.e. Germany's publicly funded open
educational resources portal, with its plumbing on GitHub. Four repositories were read first-hand
this pass:

| Repo | Licence | ★ | Commits | What it is |
|---|---|---|---|---|
| `oeh-metadata-vocabs` | **CC0-1.0** | 2 | **938** | SKOS/Turtle vocabularies incl. DigCompEdu, ESCO, EQF/DQR — see the row above |
| `oeh-search-etl` | 🔴 **none** | 8 | **1,397** | Scrapy → Postgres → Elasticsearch harvester — see the row above |
| `tutor-chatbot` | **Apache-2.0** | 0 | 10 | RAG tutor over the WLO API with Bloom-taxonomy analytics — `agents/top.md` |
| `ki-prompt-benchmark` | **Apache-2.0** | 0 | 3 | LLM-as-judge prompt bench, exports `mds.xml` — `agents/top.md` evaluation table |

Also present and unread at p321, named here so p322 does not re-discover them: `metalookup`
(5 ★, Python, domain metadata including licensing), `oeh-search-frontend` (5 ★, TS),
`edu-sharing-python-client` (0 ★), `lernpfadeditor` (learning-path editor with differentiation and
content assignment), `wlo-quellenliste`, `metadata-browser-plugin-fuerAPI`. **57 of the 67 were not
listed on the first page and remain unenumerated.**

**The star counts are 0, 0, 2 and 8, and that is this KB's Ed-Fi lesson repeating in a second
jurisdiction.** The Ed-Fi section below makes the argument from 12 ★ and 6 ★ of US state-adopted
infrastructure. `openeduhub` makes it again from a German federal-state-funded portal with a
1,397-commit harvester at 8 ★. **A star-ranked search cannot see publicly funded education
infrastructure in any region, and two independent instances is no longer a coincidence.**

### 4. The licence split inside one org, which is the practical warning

The same organisation ships **CC0-1.0**, **Apache-2.0** and **no licence at all**, and the
unlicensed repository is the one with the most commits. **Do not infer an org-level licence
posture from one repository.** On this evidence the rule for `openeduhub` is: take
`oeh-metadata-vocabs` (CC0) and the two Apache-2.0 tools freely; treat `oeh-search-etl` as
documentation of a harvesting design and **write your own**, or open an issue asking for a licence
before any engagement depends on it.

## The Ed-Fi finding — the gap this KB declared three passes running, closed in p316

The Ed-Fi Alliance publishes its platform as Apache-2.0 under the `Ed-Fi-Alliance-OSS` GitHub
organisation. The Data-Management-Service has 1,105 commits; `edfi-oneroster` serves OneRoster 1.2
off an Ed-Fi ODS and has 151. Both are Apache-2.0 — the licence tier Globant prefers.

**The stars are 12 and 6, and that is the whole lesson.** A star-ranked search systematically
cannot see public-sector education infrastructure, because it is adopted through state education
agencies and SIS vendors rather than through GitHub. **Pass 318 added a fourth confirmation of
this** — `openedx/openedx-ai-extensions`, the official Open edX AI plugin, has **17 stars and 703
commits** (see `verticals/solutions.md`) — and a fifth datapoint from the opposite direction: a
repo in this sector now openly solicits stars from AI agents (see `agents/top.md`). **Rank
candidates on commit count, release cadence and licence. Stars are noise in both directions.**

Two caveats before scoping on Ed-Fi:
- Neither repo has a published release on its GitHub Releases page. Pin to a commit, not a tag.
- Ed-Fi is a **North American** standard in practice (US state education agencies). It is not a
  route into EMEA, APAC or LATAM rostering, and nothing equivalent was found for those regions.

## Caveats

- **Sunbird's 41 ★ are not a quality signal**, for the same reason Ed-Fi's 12 are not. Government
  adjacent infrastructure in India, adopted through state deployments. Verify the wider
  `Sunbird-Ed` org's component repos before scoping.
- **`ai-agents-for-beginners` is a curriculum, not a library.** It sits here deliberately: 77.5k ★
  of MIT teaching material is a reusable asset for the "train the client's team" phase that ends
  most education engagements.
- **`pylti1.3` is the most load-bearing 138 stars in this KB.** See the mitigation list above.
- **LightRAG + DeepTutor remains the highest-leverage pair in this KB.** Both from HKUDS, both
  permissive, ~82k ★ between them, covering retrieval and tutoring. Pattern P1 is built on it.
  DeepTutor was re-verified p318 (v1.6.15, 2026-10-19); **LightRAG was re-verified first-hand in
  p319 — MIT, 40.2k ★, 5.7k forks, 10,873 commits, unchanged. That re-read is now done.**
- **Kolibri's README describes no AI features.** Re-read first-hand this pass. It is the delivery
  substrate for offline contexts; the intelligence layer is yours to add, which is exactly why it
  is in this file and not in the agent tier.

## Declared gaps — searched, not found

- **No foundational open source repo for student-data privacy compliance** (FERPA / COPPA / GDPR
  record handling). **Sixth pass declaring it — and the first pass where the gap is contested
  rather than empty.** GitHub's `ferpa` topic now holds about a dozen governance projects created
  or last updated in September–October 2026, **every one of them at 8 stars or fewer**: Rego policy
  packs (`Principled-Evolution/gopal`), PII-scrubbing ingestion with hash-chained audit trails
  (`marc-shade/docsingest`), identity-scoped RAG patterns and policy middleware (three repos by
  `ashutoshrana`, the same author as p317's `haystack-ferpa-filter`), a FERPA-safe Canvas toolkit
  (`chaz-clark/canvas-toolbox`), Bedrock agents with PII masking (`virtualryder/edu-ai-agents`) and
  an MCP server that audits tutors for FERPA/COPPA (`mizcausevic-dev/mcp-ai-tutor`).
  **None is a dependency.** But a dozen independent authors starting the same component within two
  months of the **COPPA compliance deadline of 2026-04-22** (see `intel/market.md`) is a market
  forming in real time. The build-once opportunity is still the clearest in the sector and the
  window on it is now visibly shorter. Note that Ed-Fi gives you the data *model* and API, not the
  consent, retention and disclosure machinery around it.
- ~~**No LATAM-authored foundational repo.**~~ **CLOSED PROPERLY THIS PASS, and the correction is
  worth stating precisely because this KB has now been wrong about it twice.** Five passes declared
  the gap. Pass 318 found `openedx/openedx-ai-extensions` (eduNEXT, Bogotá) and had to disqualify it
  from this file: AGPL-3.0 and explicitly not for production. **Pass 319 found three Brazilian
  repositories that qualify without caveats** — `bncc-dados`, `bncc-pacotes` and `bncc-benchmark`
  (Profy, MIT code / CC BY 4.0 data, verified against the homologated curriculum PDF, a hosted MCP
  server, a published benchmark). They are infrastructure, they are permissive, they are
  production-usable today, and **they were found by searching a Portuguese-language GitHub topic.**
  The backdrop figures still stand (Linux Foundation, December 2025: **Mexico 65%, Brazil 46%** for
  organisational use of open source AI) and so does the commercial point — the named LATAM
  education-AI companies (Teachy, Ginia, Vetto, Mattilda, Luca, Letrus, MusíGlota) remain private
  and closed-source — but "LATAM consumes open source and does not write it" is finished as a
  sentence. **Spanish-speaking LATAM is a different matter: the `educacion` topic sweep found
  teaching materials and no infrastructure, so the regional finding is Brazil specifically, not
  LATAM generally.**
- **No EMEA- or APAC-equivalent of Ed-Fi — but the gap now needs splitting in two, because one half
  moved and the other did not.** On **rostering**, nothing comparable was found for Europe or Asia;
  the closest artefact is `sikkepitje/TeamSync` (9 ★, PowerShell, Magister → Microsoft School Data
  Sync), which is one country's glue script, not a standard. On **curriculum standards**, Brazil now
  has `bncc-dev` and **nobody else in this KB does** — the German attempt (`lernplattform`) was
  archived in 2021, the Dutch and Spanish-language topics produced course material rather than data,
  and India's NCERT/CBSE repositories are hobby-scale with no verified dataset at all
  (`agents/top.md`). **Ed-Fi remains North-America-only, and it is a data model plus API, not a
  curriculum.** The two gaps are different products and should be scoped separately.
- **elimu.ai's region is not stated and should not be assumed.** Its GitHub organisation page gives
  its location as "Worldwide"; the `webapp` repository lists production deployments for **Hindi,
  Tagalog, Thai, Vietnamese and English**. This KB has an open MENA/Africa supply gap
  (`verticals/solutions.md`) and elimu.ai does **not** close it on the evidence read this pass —
  its documented deployments are APAC-language-first. Recorded here so no proposal cites it as an
  African platform without checking.
