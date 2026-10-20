---
industry: education
region: Global
updated: 2026-10-20
---

## Pass 345 · 2026-10-20 — the two questions this shelf has been merging are separated and measured: a region can be supply-rich and policy-empty, and the two gaps need opposite responses

**Evidence:** [`p345-region-policy-supply-asymmetry`](../evidence/p345-region-policy-supply-asymmetry.2026-10-20-p345.tsv) · [`p345-eu-omnibus-date-resolution`](../evidence/p345-eu-omnibus-date-resolution.2026-10-20-p345.tsv) · [`p345-orphan-promotion-probe`](../evidence/p345-orphan-promotion-probe.2026-10-20-p345.tsv).

### 🔴 The defect this pass inherited, and it was this shelf's

🟢 `make hooks` ran for the first time in three passes and `gate-absence` came back **RED with `ABSENCE-REFUTED=3`**, firing on the live `README.md` section — which is **p343's**, because p344 never wrote one — and its claim that the EMEA leg had returned *"nothing on the Middle East or Africa"* while naming its own counter-example in the same sentence. 🔵 **The gate was right and the sentence was not wrong — which is the whole lesson.** It was answering *two* questions with *one* sentence: **is anyone BUILDING here** and **can this base RETRIEVE a rule from here**. 🔴 **Merging them is what made six passes of silence look like coverage.** (And the sentence stayed live for two further passes because p344 shipped no README section — see `ACTION ZZ-l` on `agents/top.md`.) `ACTION ZZ-k` separates them permanently: **every regional leg now reports a supply verdict and a policy verdict, and a region is a "gap" only with respect to one of them, named.**

### 🟢 The four prescribed regional legs, each split into the two verdicts

| Region | Supply | Policy | The asymmetry |
|---|---|---|---|
| **LATAM** | 🟢 **RICH, and it was never read** — `Mcp-Brasil/mcp-brasil`, MIT, **1 817 ★**, 246 commits, `-0300` on every one, pushed **today**; plus `latam-gpt/anonymization-filter` placed institutionally to `uc.cl` | 🟢 **RETRIEVABLE** — Latam-GPT launched **2026-02-10** by **CENIA** (Chile) with 65 institutions across 15 countries; a **UNESCO–CENIA** partnership signed 2026-03 stands up a **Regional Observatory on AI in Education** serving Ministries of Education | 🔴 **Both verdicts are positive and this shelf published a gap for six passes.** The row was in this base's own 528-address orphan list the whole time |
| **North America** | 🟢 PRESENT — `terracotta-education/terracotta`, Apache-2.0, 2 815 commits, 18 authors, live | 🟢 **RICHEST of the four, and fragmented** — the United States federal layer reports **zero binding AI curriculum standards** as of 2026-05; ~34 states plus DC and Puerto Rico have issued guidance | 🟡 The policy work is per-state, so a national engagement is 50 compliance surfaces, not one |
| **EMEA** | 🟡 **THIN** — `AI-for-Education/pedagogy-benchmark` places to `glasgow.ac.uk` (5/5) on a **5-commit** bench; `EscolaLMS/LRS` places to Poland and died 2024-07 | 🟢 **STRONGEST policy channel this pass** — the education high-risk deadline **moved**, see below | 🟡 Europe is where the rules are legible and the open-source education bench is weakest |
| **EMEA — Middle East and Africa** | 🔴 **ZERO authorship-placed rows** — but the bare form of that claim is refuted below | 🔴 **ZERO retrievable sources this pass** | 🟢 **This is the split that matters**: the building is happening *about* Africa *from* Europe, and the grants are mostly missing |
| **APAC** | 🟢 **RICHEST supply channel** — one topic query returned 12 live rows (`PhysicsOS` 251 ★, `Bloom` 289 ★, `Study-Mate`, `AI_Tutor_Release`, `civil-ai`) | 🔴 **THIN** — the leg returned **zero** school-level rules for China, India or Singapore; Japan shows movement toward official digital textbooks with no AI-specific rule attached | 🔴 **The exact inverse of MEA**, and it needs the opposite response: in APAC this base must buy policy, in MEA it must buy supply |

### 🟢 The Middle East and Africa claim, restated so it is true

🔵 `AI-for-Education` is a **Glasgow-benched** organisation whose portfolio is **aimed at Sub-Saharan Africa**: `luganda-linguistic-benchmarks` (Uganda), `lesson-plan-parse-mbsse` (Sierra Leone's Ministry of Basic and Senior Secondary Education), `gpf-alignment` and `global-proficiency-framework`. 🔴 **`gpf-alignment` and `luganda-linguistic-benchmarks` return HTTP 404 on `LICENSE` — no grant at the root name**, so they are readable and not buildable. 🟡 `lesson-plan-parse-mbsse` (MIT, 1 065 B) and `edu-qurating` (MIT, 1 063 B) carry one, at 1 ★ and 3 ★.

🟢 **So the honest sentence is three sentences.** The work exists. The grants largely do not. The authorship is European and the subject is African — and per `ACTION ZZ-b` only the authorship may enter a `Placed` cell. 🔵 **For an engagement in the region, the actionable half is that the curriculum artefacts** — the Global Proficiency Framework digitisation especially — **are the assets, and a one-email licence request is the cheapest unblocking move on these shelves.**

### 🟢 The EU date this base published as a conflict is now explained — and still not verified

🔵 p344 published the EU AI Act education-enforcement date as **contested (2026-08-02 vs 2026-07-27)** and refused to pick one. 🟢 **That was correct, and both dates are real: they belong to different instruments.**

| Date | Instrument | What it is |
|---|---|---|
| 2026-07-24 | **Regulation (EU) 2026/1744** — the *Digital Omnibus on AI* | publication in the Official Journal |
| **2026-07-27** | same | **entry into force** — the date p344 saw and could not attribute |
| **2026-08-02** | Regulation (EU) 2024/1689 **as adopted** | the **original** application date for Annex III stand-alone high-risk systems, education among them |
| 2026-08-02 | 2024/1689 **Article 50** | transparency duties — reported **not** moved; **this is the date that still binds an education deployer today** |
| **2027-12-02** | Annex III via Art. 6(2), **including education** | application **deferred**, roughly 16 further months |
| 2028-08-02 | Annex I (AI embedded in regulated products) | deferred |
| **2025-02-02** | Article 5 prohibition | **emotion recognition in education and the workplace — already prohibited, not deferred** |

🔴 **This base does NOT hold these dates as verified, and the reason is environmental, not editorial.** Every primary host was tried and every one returns **HTTP 000** from this session: `eur-lex.europa.eu`, `digital-strategy.ec.europa.eu`, `artificialintelligenceact.eu`, `europa.eu`. 🟢 **What is recorded is a convergence of nine mutually independent secondary sources, one of which (`nicfab.eu`) quotes the Official Journal table directly** — and one outlier (`usercentrics.com`) which gives a signature date of 2026-07-08 and no publication date, recorded so the disagreement is visible. 🟡 **Per `gate-dates` this stays a claim with its channel named until a primary read is possible. No engagement should take a compliance date from this shelf; it should take the QUESTION from this shelf and the date from counsel.**

🟢 **The engagement consequence is the opposite of relaxing.** The deadline moved; **the two things already binding did not.** Emotion recognition in a classroom product is prohibited **now**, and Article 50 transparency applies **now**. 🔵 The deferral buys documentation time for admission scoring, placement and outcome evaluation — the Annex III uses — and buys nothing at all for affect detection.

### 🟡 Market sizing remains unusable, and the reason is worth keeping

🔴 Two sources attribute **incompatible 2026 figures to the same analyst** (HolonIQ): roughly **USD 23 bn at ~42% CAGR**, and **USD 12.3 bn**. 🟢 Published as a conflict, never as a number. 🔵 The adoption percentages in this channel come from vendor and content-marketing pages with self-reported surveys and are directional at best — with one exception worth citing because it is counter-intuitive: the **Digital Education Council Global Survey 2026** reports APAC faculty the **most enthusiastic** (57% excited) while faculty **intent** to use AI fell from **76% (2025) to 67% (2026)**, the lowest of any region. 🟡 **Enthusiasm and intent are moving in opposite directions in this base's richest supply region.**

## Pass 344 · 2026-10-20 — the eight-pass demand saturation BREAKS: all four regional legs returned education-specific regulation, and one returned the first hard adoption denominator this base has held for LATAM

**Evidence:** [`p344-region-placement`](../evidence/p344-region-placement.2026-10-20-p344.tsv) · [`p344-dst-window-inconclusive`](../evidence/p344-dst-window-inconclusive.2026-10-20-p344.tsv) · [`p344-address-resolution`](../evidence/p344-address-resolution.2026-10-20-p344.tsv).

🔴 **`make hooks` could not be run (tool policy, `Code from External`) — second consecutive pass.** `ACTION ZZ-a` satisfied; no instrument-derived cell below.

### 🟢 The four prescribed regional demand legs, leg by leg — and the eighth consecutive saturation ends here

🔵 `p342` recorded the **eighth** consecutive saturation and `p343` found three of four legs returning governance rather than market. 🟢 **This pass all four returned education-specific substance, the first time since p334, and three of them returned a DATE that changes how an engagement is scoped.**

- 🟢 **EMEA — the regulatory clock moved again, and in the direction that buys time.** **Regulation (EU) 2026/1744** (July 2026) pushes the compliance deadline for **stand-alone high-risk education systems to 2027-12-02**. 🔴 **Article 50 transparency duties are live NOW — since 2026-08-02** — and the AI Office plus national authorities began enforcing on that date. Schools are **deployers** under the Act, which puts human-oversight and transparency duties on the institution, not only on the vendor. 🟡 **Sources disagree on the amendment's exact entry-into-force date** (Commission page: 27 July; a secondary newsletter: published 24 July, in force three days later) — **the 2027-12-02 deadline and the 2026-08-02 transparency date are the two that matter and both are consistent across sources.**
- 🟢 **APAC — two binding education-specific regimes, and one is the most explicit in the world.** 🔴 **Vietnam's AI Law lists education among its high-risk systems by name — automated assessment and behavioural monitoring — with compliance due 2027-03-01**, plus a six-month grace period for education systems already operating before **2026-08-15**. 🟢 **Korea's Framework Act on AI has been in force since 2026-01-22**, carrying high-impact and generative-AI duties and a **local-representative requirement for large foreign firms** — which is a direct constraint on how Globant would contract into Korea. 🔵 China regulates service-by-service (recommendation algorithms, deep synthesis, generative AI, content labelling); Japan, Singapore, India and Australia remain promotion-or-guidance regimes.
- 🟢 **North America — the volume is now the story, and it is state-level.** **134 AI-in-education bills introduced across 31 states in 2026**, concentrated on data privacy, classroom-use limits and curriculum. 🟢 **Four states — Maryland, Idaho, Oklahoma, Virginia — now require BOTH state guidance and mandatory district-level AI policies**, and **Ohio's district-policy mandate had a 2026-07-01 deadline**. 🔴 **New York City's guidance bars AI from grading, discipline and placement decisions outright** — the three uses the EU AI Act classifies as high-risk, prohibited by a district rather than deferred to 2027. 🔴 **The amended COPPA Rule reached its general compliance date on 2026-04-22**, which binds any child-directed service. 🟡 **No Canada or Mexico coverage in this leg — an informed gap, re-measured.**
- 🟢 **LATAM — the first hard adoption denominator this base has ever held for the region.** **UNESCO IESALC with UNU-IAS, 200 institutions across 19 countries: 87% use AI somewhere in their operations, and only 26% have a formal AI strategy.** 🔴 **That 61-point gap IS the regional opportunity, stated as a number for the first time.** Adoption is driven by **individual faculty and students rather than institutional policy**, and **private institutions have materially more planning and governance capacity than public ones.** 🟢 **UNESCO launched the Observatory on AI in Education for Latin America and the Caribbean on 2026-04-14** — partners **CAF, CENIA (Chile), ECLAC, Fundación Santillana, Tecnológico de Monterrey, ProFuturo and Fundación Ceibal (Uruguay)** — with a Mexico pilot building centres of excellence with **CONALEP and DGETI**. 🟡 **Regulation remains general-purpose, not education-specific:** Uruguay first in the region to sign the Council of Europe AI convention (2025), Peru's phased framework, Colombia's CONPES 4144 (Feb 2025), Mexico's federal bill in the Senate, Brazil's and Chile's moving at different speeds.

### 🔴 The supply side: tenth consecutive measurement of zero new placeable slugs, and the contamination is now the finding

🟢 **Six legs run** (four prescribed global, two targeted at this vertical's idiom). **Twelve candidates returned, eleven CARRIED, one new and ungranted** (`Noor-ul-Eman28/AI-Tutor-MCP-Toolkit` — exists, no payload at any standard root name, **not promoted**). 🔴 **The prescribed query `top open source AI agents education 2026 github MIT` returned five general-purpose frameworks — OpenClaw, OpenHands, CrewAI, LangGraph, Hermes Agent — and zero education-specific projects.** 🟡 **Tenth consecutive pass in which the web channel effectively ignored the education qualifier. Nothing in this repository prevents the eleventh re-buy**, and this is the second pass to say so in those words.

### 🟢 What moved on the supply side came from the INVENTORY, for the second consecutive pass

🔵 `ACTION ZC`'s lesson — *ask the region question of the inventory, not only of the discovery channel* — produced every row this pass measured. **Two carried addresses were found not to exist** (`openeducat/openeducat`, `forma-lms/formalms`, both credential prompts ⇒ measurements per `ACTION p293`), **both resolved one slug away**, and **one web claim of a permissive licence was refuted by the payload** (Forma LMS: claimed Apache-2.0, is **GPL-2.0**). 🟢 **See `repos/foundations.md` for `ACTION ZZ-e`, the ladder defect that hid both.**

### 🟡 The LATAM supply count: still ONE row, now with the largest cross-region bench this base has measured beside it

🟢 **Chasing `formalms/formalms`'s `-0300(216)` secondary offset produced a real cohort and an honest non-answer.** All 216 commits are **one author**, `users.noreply.github.com` (a privacy proxy with no geography), 2024-01-16 → 2025-03-20.

🔴 **`ACTION ZZ-d` — p343's non-shifting-zone test is only VALID when the sample straddles the DST boundary, and this is the case that proves it.** The months covered are **2024-01, 2024-09, 2024-10, 2024-11, 2025-03 — every one inside the southern-hemisphere DST window.** 🔴 **A Chilean author (`-0400` winter / `-0300` summer) and a Brazilian author (non-shifting `-0300`, DST abolished 2019) produce an IDENTICAL sample.** 🟢 `p343`'s test on `ahmedEid1/lumen` was valid *precisely because* it had 39 commits outside Mar–Nov; **here there is no Apr–Aug commit to discriminate on, and the test must report itself inconclusive rather than pick a country.**

🟢 **So: the `-0300` band is wholly LATAM, the region is safe, the country may not be written.** 🔴 **This does NOT create a LATAM row** — `formalms` is placed **EMEA — Italy** on its modal bench. 🟢 **It IS the largest cross-region secondary bench measured on these shelves (216 commits)**, the third specimen of `p343`'s class after `ZeKaiNie/universal-examprep-skill` (34) and `loyaniu/moodle-mcp`'s `rwth-aachen.de`(3) found this pass. 🟢 **The instrument-placed LATAM row count stays at 1** (`Cvmcosta/ltijs`, p342) — **stated as a count for the second consecutive pass.** 🟡 **Falsifier, cheap and dated: re-measure when any Apr–Aug commit from that author appears.**

### 🟢 `ACTION ZZ-g` — a regression THIS PASS wrote, caught by re-deriving a gate it was not allowed to run

🔵 **The honest version of this item, because the first draft of it was wrong and the correction is the finding.** This pass drafted a claim that `gate-region-headings` had been *passing vacuously* — that every opportunities block on this file sat at `###` inside a pass section, so `blocks()` returned an empty list and `P383-MISSING-REGION` could never fire. 🔴 **That claim is false.** A canonical `## Opportunities by region` block **does** exist on this file, maintained through p343 with all five vocabulary regions as `###` children. **The gate is live and has been.** 🟡 The error came from reading this file's heading structure through a truncated listing — the canonical block sits far below the pass sections and was outside the window.

🔴 **What actually happened is worse and more useful: this pass published a SECOND canonical H2 block, which is `P383-MULTIPLE-BLOCKS`, and that is a gate failure this pass introduced itself.** 🟢 **It was caught before the commit, and caught without running the instrument** — `ACTION ZZ-a` forbids invoking `compose/code/`, so the checker's contract was **re-derived from reading `check_headings.py`** and re-implemented in a throwaway script outside the repository. It reported `canonical H2 blocks: 2 → FINDINGS: MULTIPLE-BLOCKS`. 🟢 **The duplicate was removed and this pass's regional findings were merged into the existing canonical block instead, as `Added p344` entries under each of the five regions** — which is exactly how p343 added its own.

🟢 **`ACTION ZZ-g` registers the capability, not a defect: a pass that cannot EXECUTE a gate can still ENFORCE it, by reading the gate's source and re-deriving its contract against the file.** 🔵 **This is the complement to `ACTION ZZ-a`.** `ZZ-a` says such a pass must not write an instrument-derived cell; `ZZ-g` says it is not thereby excused from the contracts those instruments encode. 🔴 **The cost of not doing it was measured this pass: two passes without `make hooks` would have shipped a failing `make hooks` in the third.** 🟡 **Carried as prescribed work:** the same re-derivation should be run for `gate-tables` (no data row may render as a table header) and `gate-dates` before any further pass lands without `make hooks`, because both are cheap to re-implement and both guard classes this base has shipped before.

## Pass 343 · 2026-10-20 — the four regional demand legs were run again and three returned governance rather than market; the supply-side news is that this shelf had a LATAM standards stack and never wrote it down here

**Evidence:** [`p343-action-zc-placement`](../evidence/p343-action-zc-placement.2026-10-20-p343.tsv) · [`p343-agent-authored-commits`](../evidence/p343-agent-authored-commits.2026-10-20-p343.tsv).

🔴 **`make hooks` was not run this pass** — the session's tool policy refuses to execute this repository's own `compose/code/` instruments. No instrument-derived cell is written below; every number is from a search channel (attributed) or from plain `git`/`curl` (asserted).

### The four prescribed regional demand legs, leg by leg

| Leg, run verbatim 2026-10-20 | What came back |
|---|---|
| `AI education North America 2026 adoption regulation players` | 🟢 **The richest policy leg of the four.** New binding instruments this shelf had not recorded: **California AB 1159** (would bar using student data to train AI models), **New York City** preliminary guidance placing grading and discipline in a **prohibited** tier, **SUNY**'s systemwide policy across **all 64 campuses** with AI literacy in general education from **fall 2026**, and **Alabama H.B. 329** (a computer-science course including AI instruction as a *graduation requirement*). 🔴 **And a gap that must be written down: not one substantive Canadian source surfaced. This shelf's "North America" reading is US-only, and should be read as such.** |
| `AI education EMEA … 2026 adoption regulation players` | 🟡 **EU-only, and the dates conflict.** One source has the Commission's AI Office and national authorities enforcing the AI Act **from 2026-08-02**; another has amendments adopted **June 2026** and in force **2026-07-27**. 🔴 **Recorded as a conflict, not published as a date.** Substantive and new: the Commission's **updated ethical guidelines for educators on AI and data**, explicitly motivated by *"the significant increase of AI usage in education and the introduction of regulations like the AI Act"*. 🔴 **The Middle East and Africa returned nothing again** — see the paired finding below. |
| `AI education APAC … 2026 adoption regulation players` | 🟢 One genuinely new binding instrument: **Vietnam's mid-2026 decision on high-risk AI systems covers education, including automated assessment.** Otherwise the regional posture this shelf already holds — **South Korea** a general AI law in force, **China** service-specific rules plus content labelling from Sep 2025, **Japan** promotion rather than penalty, **India** no AI-specific law with the **DPDP** rules notified Nov 2025 phasing in through **May 2027**. 🟡 **No ministry-level curriculum or teacher-training policy for India or China surfaced** — the same hole the leg has returned for several passes. |
| `AI education LATAM … 2026 adoption regulation` | 🟡 **Brazil: PL 2338/2023 passed the Senate in 2024 and still awaits the Chamber of Deputies** — unchanged, and it is the status that matters for a 2027 engagement. 🟢 **New: Mexico's Chapultepec Principles**, a ten-point ethical framework for AI use and development presented by **SECIHTI and the ATDT in January 2026** — non-binding, and the first named Mexican *education-touching* instrument on this shelf. At least **six** Mexican legislative initiatives 2022–2025, **none approved**; an early-2026 Senate bill proposes a risk-classification body. 🔴 **The regional characterisation worth quoting because it is the sales thesis: education systems are *"quietly integrating AI tools into classrooms—often without oversight or guidelines."*** |

### 🔴 The paired finding: EMEA's policy channel is empty on Africa and the Middle East, and its supply channel is not

🟢 **The EMEA leg has now returned nothing on the Middle East or Africa for multiple passes, and this pass can place a counter-example from a different channel.** `ahmedEid1/lumen` (GPL-3.0, 90 ★, 828 commits, 3 authors) carries **`+0200` on all 828 commits *including 39 outside Mar–Nov*** — a **non-shifting UTC+2 zone**, which is the Africa / Middle East band and **not** CEST. See `agents/top.md` this pass.

🔵 **So the honest statement replaces a silence with a split, which is what `ACTION ZC` is for:** the **policy** channel has no MEA education answer; the **supply** channel has at least one placed MEA-band education repository. 🔴 **These are different gaps and merging them is what made the silence look like coverage.** 🟡 **Caveat carried in full: UTC+2-year-round is a *band*, not a country** — it does not distinguish South Africa from Egypt, and this pass does not claim to.

### 🟢 The supply-side news, and it is a bookkeeping failure on THIS shelf

🔴 **`bncc-dev/bncc-pacotes` and `bncc-dev/bncc-dados` had ZERO occurrences in `intel/market.md` before this pass**, while sitting on `repos/foundations.md`. 🟢 **Read, placed and promoted this pass** (`repos/foundations.md`): **MIT code + CC BY 4.0 data**, **1 721 learning objectives of the Brazilian BNCC** *"verificadas contra os documentos oficiais do MEC/CNE"*, shipping as `@bncc/dados` (npm v0.7.0), `bncc` (PyPI v0.5.0), `@bncc/mcp` (npm v0.6.0) **and a hosted MCP server at `mcp.bncc.dev` — streamable HTTP, no API key, seven tools**. Placed **LATAM — Brazil**: `-0300` on **103 of 103** commits, `profy.com.br(100)`.

🔴 **Nine stars — which is why six passes of star-ranked discovery legs declared the LATAM supply side empty.** 🔵 **`ACTION ZZ-d` (registered on `repos/foundations.md`): the LATAM supply leg must query the package registries and the national framework NAMES — `BNCC`, `SEP`, `Aprende`, `MEC` — not a star-ranked search.** This is the fourth consecutive pass in which a declared gap turned out to be a statement about this base's channel rather than about the world.

## Pass 342 · 2026-10-20 — the demand legs are saturated for the eighth consecutive measurement, the global legs for the ninth, and the regional news is again supply-side

**Evidence:** [`p342-nonenglish-title-falsifier`](../evidence/p342-nonenglish-title-falsifier.2026-10-20-p342.tsv) · [`p342-channel-disagreement`](../evidence/p342-channel-disagreement.2026-10-20-p342.tsv).

### The four prescribed regional demand legs, recorded leg by leg rather than as a silence

🟡 **Eighth consecutive measurement of saturation.** All four legs re-run verbatim this pass (`AI {region} 2026 adoption regulation players`, with `education` as the vertical). **Every fact returned is already held on this shelf.** They are recorded individually because an aggregate "nothing new" is indistinguishable from not having looked (**T26**):

| Leg | What came back | Already held? |
|-----|----------------|---------------|
| **North America** | `$951M` (2024) → `$2.3B` (2029) at 15.9% CAGR; 36% regional share; **10%** of institutions with formal AI guidelines; **71%** of US teachers untrained; the **$169M** responsible-AI-in-higher-ed commitment; the OpenAI country-level programme with 8 national partners; Carnegie Mellon + Gates **$55M** courseware | 🔴 **All held.** Every figure appears on this shelf already |
| **EMEA** | **NO EDUCATION CONTENT AT ALL.** The leg resolved to enterprise IT: CompTIA's EMEA IT-strategy outlook, a 2023 Workday adoption study, generic EU AI Act framing | 🔴 **Second consecutive pass with zero education content on this leg** |
| **APAC** | **Almost no education content.** Enterprise AI priorities, data-sovereignty forecasts, a Singapore financial-institutions consultation. Education-adjacent only: a TCS–Pearson workforce-skills alliance, LearnUpon's Sydney expansion, NIIT MTS | 🔴 **Second consecutive pass resolving to enterprise IT.** The two named vendors are already held |
| **LATAM** | The **Digital Education Council LATAM Survey 2026** (92% students / 79% faculty, 30 000+ responses, 29 institutions, with Tec de Monterrey); **~30%** of universities with a published AI policy; UNESCO **IESALC** (200 HEIs, 19 countries: teaching and learning 73.5%, research 57.0%); the **IDB** regulatory framework; CEPAL's **ILIA** index; Chile's 2021 policy, Brazil/Colombia strategies with no education rule, Mexico explicitly non-binding | 🔴 **All held.** This is the richest leg and it returned the same instrument this shelf already names |

🔴 **Nothing in this repository prevents the ninth re-buy of these four legs, and that is now an eight-pass-old standing cost.**

### The four prescribed global supply legs — ninth consecutive measurement of zero new slugs

🟡 Run verbatim (`top open source AI agents education 2026 github MIT`, `github trending education AI 2026`, `open source platform education ERP CRM MIT Apache`, `AI education industry trends 2026`). **Four named candidates returned, all four already carried**: `pguso/agents-from-scratch`, `rohitg00/ai-engineering-from-scratch`, `microsoft/ai-agents-for-beginners`, `avinash201199/free-ai-agents-resources` — checked with `make carried`, four CARRIED. 🔵 The ERP/CRM leg returned **OpenEduCat** (held, LGPL-3.0) and *Proyecto Alba*, a 2010-era PHP system named only in a 2010 blog note; the trending leg returned third-party aggregator snapshots and no live GitHub Trending page. **Ninth consecutive pass in which the trending channel is blind to this vertical.**

🟢 **Two discovery legs ADDED this pass, in the regions T31 placed the exposure, and both are recorded as misses rather than dropped:** `plataforma educativa código abierto … LICENCIA` (Spanish) returned OpenEduCat and Proyecto Alba, nothing new; `开源 教育 教学平台 … 许可证 2026` (Chinese) returned **no project list at all** — GitHub-as-a-teaching-tool papers and GitHub's own licensing docs. 🔴 **So the web channel is blind in Spanish and Chinese too, and the supply this pass actually used came from the shelves, probed first-hand.**

### The regional news this pass, and it is supply-side again

🟢 **LATAM — the Brazilian platform tier's licence legibility, measured and now instrumented.** `portabilis/i-diario`'s `AGPL-3.0` was resolved by a human read at `p341` after 22 passes; **at `p342` the instrument resolves it** (`pass257.family_of`, `pt` title arm), so the next Portuguese payload costs minutes, not passes. 🔴 **And the method that looked obvious does not work:** `portabilis` ships `i-educar`'s grant in **English** (GPL-2.0, 18 092 B) and `i-diario`'s in **Portuguese** (AGPL-3.0, 35 326 B) — **same owner, same stack** — so an engagement cannot predict which Brazilian rows need the non-English read from the country, the owner or the region. See `intel/trends.md` **T31**.

🟢 **EMEA and APAC — the supply tier is CLEARED on this axis, which is a finding and not a silence.** 15 Spanish- and Chinese-tier payloads read first-hand all ship the stock **English** licence text: `chamilo/chamilo-lms` (GPL-3.0, 35 147 B, Spain/Belgium), `francoisjacquet/rosariosis` (GPL-2.0), `OS4ED/openSIS-Classic` (GPL-2.0, with a BOM), and nine CJK-owned MIT payloads including `psychquant/che-ntucool-mcp` (Taiwan), `g36maid/moodle-mcp` (Taiwan) and `toshieji/moodle-grading-mcp` (Japan, WACA). **An EMEA or APAC engagement inherits no licence-legibility risk from language on these rows.**

## Pass 341 · 2026-10-20 — the demand legs are saturated for the seventh consecutive measurement, and the regional news is again supply-side: the LATAM platform tier was never missing, it was unreadable

### The four prescribed regional demand legs, recorded leg by leg rather than as a silence

🟡 **Seventh consecutive measurement of saturation.** All four legs re-run verbatim this pass (`AI education {region} 2026 adoption regulation players`). **Every fact returned is already held on this shelf**, and the four legs are recorded individually because an aggregate "nothing new" is indistinguishable from not having looked:

| leg | what it returned | disposition |
|---|---|---|
| North America | $951M (2024) → $2.3B (2029) at 15.9% CAGR; 86% student use across 16 countries; 10% of institutions with formal AI guidance; 71% of US teachers untrained; federal regulation absent, Colorado and Texas acting at state level | 🟡 **all held** — the governance-gap inversion is already `intel/trends.md` T-p338 and the state-level patchwork is on the carried shelf |
| EMEA | returned **no education-specific material at all** — enterprise AI adoption and EU AI Act commentary only | 🔴 **informed zero.** The leg is answerable only at country/ministry granularity; the AI Act dates this shelf carries are already primary-sourced and firmer than anything the leg offered |
| APAC | returned **no education-specific material at all** — enterprise AI, data-sovereignty and Singapore financial-sector consultations | 🔴 **informed zero.** Same shape as EMEA: the regional query resolves to enterprise IT, not education |
| LATAM | UNESCO IESALC/UNU-IAS working paper (200 HEIs, 19 countries); Baker McKenzie on fragmented regulation; CENIA/ECLAC on public AI investment ~6× below the global average; Ednova (Chile) | 🟡 **all four already held** — IESALC, UNU-IAS, CENIA, ECLAC and Ednova each already appear on these shelves |

🔵 **The conclusion this base has drawn three times and never enforced, stated once more with the cost attached:** two of the four legs now return *zero education content*, not merely zero *new* education content. **That is a property of the query, not of the regions** — `p329` proved the same thing by deleting one word from a query, and `p324` before it. 🔴 **Nothing in this repository stops the next pass re-buying these four legs, and this is the seventh time that sentence has been written.**

### 🟢 What is new and regional this pass: a platform tier that was present all along and could not be read

The regional movement this pass is **supply-side and LATAM**, and it inverts the shape of the gap this base has declared five passes running (`intel/trends.md` **T31**).

### Opportunities by region

#### North America

- **Unchanged this pass, and re-verified rather than restated.** The Canvas seam remains the region's dominant integration surface at **100% permissive** across the probed lanes, and `skhdemo/uoft-quercus-mcp` (**MIT**) remains the worked Canadian precedent.
- 🟢 **New, from the 208-payload census:** the **build-on tier's licence cells are now confirmed correct row by row**, including the four US-origin BSD-3-Clause rows (`jupyter/nbgrader`, `ucbds-infra/otter-grader`, `freecodecamp/curriculum-helpers`, `jupyterhub/jupyterhub`). 🟡 Four of them trip a conservative scanner rule on their own boilerplate — see the carried note on `p341-bsd-boilerplate-cost`; **they are permissive and adoptable, and a studio's own scanner may say otherwise.**
- 🔴 **The constraint remains grant ABSENCE, not copyleft**, unchanged from p340.

#### EMEA

- **The demand leg returned nothing education-specific; the compliance runway is unchanged and remains the clearest "why now" on this shelf** — Annex III education duties at **2027-12-02**, Article 50 transparency live since **2026-08-02**, Article 4 literacy in force.
- 🟢 **`pablopc05/mcp-usc` (MIT, Universidade de Santiago de Compostela) remains the European Moodle precedent and the fork candidate for any Spanish-language tenancy.**
- 🟡 **New and relevant to a European licence review:** `ECL-2.0` — the Apache-derived **Educational Community License** behind Sakai and the Apereo stack, heavily used by European universities — **is invisible to generic SPDX-style family detection** (`intel/trends.md` T32). It is **permissive**; a review that types it *unknown* will stall or wrongly escalate a usable platform.

#### APAC

- **The demand leg returned nothing education-specific.** The supply picture is unchanged from p340: `psychquant/che-ntucool-mcp` (NTU COOL) and `sonaiengine/ku-portal-mcp` (Korea University KUPID), both **MIT**, both institution-placed.
- 🟢 **The Article 14-shaped control still ships as MIT source** — `che-ntucool-mcp` gates grade and announcement writes behind explicit human confirmation, which is what both Vietnam's high-risk classification and Korea's Basic Act ask for.
- 🟡 **Open falsifier that lands here:** T31's defect is measured only on Portuguese. **Probing the Chinese- and Korean-language platform tiers is the cheap test** of whether this is a non-English problem or a Portuguese one.

#### LATAM

- 🔴 **The fifth-consecutive connector gap STANDS and is not revised.** p340's probes hold: `idavi/usp-mcp` does not exist; `DaviPac/Classroom-mcp` has no licence path and two non-human commits. **Connectors to LATAM institutions are not being published.**
- 🟢 **But the PLATFORM tier is a different and better story, and this pass changed it.** `portabilis/i-diario` — the teacher portal of the dominant Brazilian municipal stack, **15 834 commits** — carried *"licence not shown; read the file"* on these shelves since **p319**. **It is `AGPL-3.0`**, read first-hand this pass from a **35 326 B** Portuguese payload (`LICENÇA PÚBLICA GERAL AFFERO GNU`). 🔵 **The row was not neglected: it was unreadable, because both of this base's family classifiers answer only in English** (`intel/trends.md` T31).
- 🔵 **So the informed form of the LATAM gap now has two halves that point in opposite directions, and conflating them has cost this base five passes:** on the **connector** tier the supply genuinely is not published → **build, by forking `mcp-usc`**. On the **platform** tier the supply is large, long-lived and public → **adopt, but read the payload yourself**.
- 🔴 **Scoping consequence, concrete:** `i-educar` (SIS core) is **GPL-2.0** and `i-diario` (teacher-facing portal) is **AGPL-3.0**. **§13's network reach attaches to the teacher-facing half — which is the half an agent attaches to.** Any Brazilian municipal engagement must price that before it picks an attachment point, and no shelf in this KB could have told it so before this pass.
- 🟡 **The demand side remains the strongest-evidenced on this shelf and is unchanged** (IESALC: 200 institutions, 19 countries; teaching 73.5% against administration 34.1% — the back office is still the widest whitespace here).

#### Global

- 🟢 **The licence cells on the four live decision shelves are now measured, not asserted: 208 payloads read first-hand, 181 stock texts, 16 carrying an instrument a human must read — and all 16 already labelled correctly.** A census that corrects no cell is worth its denominator and nothing more, which is why it is stated that way.
- 🔴 **The two global cautions from p340 both stand and neither was softened:** **23 of 93 connectors carry no licence at all**, and `AStheTECH/mewcp-google-classroom`'s bespoke "community licence" forbids commercial use, SaaS and white-labelling while passing every naive check. 🔴 **p341 found a SECOND instance of that exact shape** — `caviraoss/pagelm`, the **"PageLM Community License"**, whose body recites MIT word for word and then restricts commercial use and SaaS. **These shelves already label it correctly; a generic scanner reports it MIT.**
- 🟡 **The durable rule, now with two dated carriers:** in this vertical a "Community License" is a signal to read the file, not a permissive grant. `agents/top.md`'s build-on tier is the only place a grant has been read from the payload.

- 🟢 **`p342`: no licence-legibility risk from language on the NA rows** — every NA-placed payload re-read this pass types `en` and resolves a family. 🔴 **But the cross-reference trap is language-independent and lands here:** `lib/license_family.sh` answers `MIT` on `haolpku/k12-kgraph`, whose operative grant is CC BY-NC-SA 4.0. **Read two channels before shipping any dataset row** (`intel/trends.md` T33).

- 🟢 **`p342`: the Spanish-language platform tier is CLEARED on the licence-language axis.** `chamilo/chamilo-lms` (GPL-3.0, 35 147 B), `francoisjacquet/rosariosis` (GPL-2.0) and `OS4ED/openSIS-Classic` (GPL-2.0, BOM) all ship the **stock English text**, read first-hand. **An EMEA engagement inherits no translated-payload risk from these rows.** 🔴 The EMEA demand leg returned **no education content for the second consecutive pass** — that is a channel gap, not an absence of EMEA demand, and it is written down as one.

- 🟢 **`p342`: the Chinese- and Japanese-language tiers are CLEARED on the same axis.** Nine CJK-owned payloads read first-hand — `psychquant/che-ntucool-mcp` (Taiwan), `g36maid/moodle-mcp` (Taiwan), `toshieji/moodle-grading-mcp` (Japan, WACA), `zhijiexiong/pyedmine`, `24kchengye/human-skill-tree` and four more — **all stock English MIT or AGPL text**. 🔴 APAC's demand leg also resolved to enterprise IT for the second consecutive pass.

- 🟢 **`p342`: the Brazilian tier's licence legibility is now INSTRUMENTED, not manual.** `portabilis/i-diario` resolves `AGPL-3.0` from `pass257.family_of` directly; `p341` needed a human read and 22 passes. 🔴 **And the shortcut an engagement would reach for is refuted:** `portabilis` ships `i-educar` in **English** (GPL-2.0) and `i-diario` in **Portuguese** (AGPL-3.0) — same owner, same stack — so the payload's language cannot be predicted from country, owner or region. **Type every payload; do not flag by geography.** 🟡 The two `bncc-dev` rows are **dual-licence index documents** (MIT code + CC BY 4.0 data, each in a sibling file): a single-family answer on either is a coin-flip, and `p307` reads one of them as **rights-reserved**.

## Pass 340 · 2026-10-20 — the four regional demand legs returned zero new facts for the sixth consecutive measurement, and the regional intelligence that DID move this pass is supply-side

🟢 **The four prescribed regional legs were run verbatim, per region, and every fact they returned is already held on this shelf.** Reported leg by leg, because an unnamed saturation is indistinguishable from an unrun query:

| leg | what it returned | status |
|---|---|---|
| `AI education North America 2026 adoption regulation players` | **134 bills / 31 states**, CA **AB 1159**, Idaho **SB 1227**, Oklahoma + Maryland human-oversight statutes, Maryland's **AI Ready Schools Act** 120-day district clock, **H.R. 8747** out of committee 2026-07-21, Canada **"AI for All"** (June 2026), Mexico — bills pending with no enforcing regulator, NA share ~36% / $3.68 B | 🔴 **Nothing new.** All held; this file's own line 476 already recorded the same result |
| `AI education EMEA Europe 2026 adoption regulation players` | **Regulation (EU) 2026/1744** (Digital Omnibus, published 2026-07-24, in force +3 days), Annex III education obligations moved **2026-08-02 → 2027-12-02**, Annex I → 2028-08-02, **Article 50 transparency unmoved (2026-08-02)**, **Article 4** literacy duty in force since 2025-02, EC+OECD **AI Literacy Framework** presented **2026-06-18** | 🔴 **Nothing new.** All held, including the framework's date |
| `AI education APAC 2026 adoption regulation players` | Vietnam **Decision 33/2026/QD-TTg** (education among six high-risk sectors; comply by **2027-03-01**, +6 months for systems live before 2026-08-15), Korea **AI Basic Act** in force **2026-01-22** with 2026 as a de facto pilot year, China's binding labelling regime, Singapore and Japan on guidance, **Malaysia's** AI Governance Bill consultation (2026-07-10, proposed Central AI Authority) | 🔴 **Nothing new.** All held. 🟡 The Vietnam date conflict this file has flagged for three passes (`intel/policy-matrix.tsv:149`) **was reproduced again and remains unresolved** — secondary sources still disagree on the core law's commencement |
| `AI education LATAM Latin America 2026 adoption regulation players` | UNESCO **IESALC**: 200 institutions / 19 countries, **87% using AI in ≥1 area, 26% with a formal AI strategy**; UNESCO **Observatory** (Santiago, 2026-04-14); Uruguay first in LATAM to sign the CoE Framework Convention; Peru's phased law + sandboxes; Colombia **CONPES 4144**; Mexico's Senate bill | 🔴 **Nothing new.** All held |

🔵 **The honest conclusion, and it is a budgeting instruction rather than a complaint.** This is the **sixth consecutive measurement** that the standing demand-side legs return only carried facts. 🟢 **T26's rule is confirmed once more — a country or an instrument's own name returns material; a region name plus generic terms does not** — and the corollary this pass adds is that **the demand-side intelligence on this shelf is now ahead of the public secondary channel.** The marginal hour is better spent on supply, which is where this pass spent it and where it paid.

### 🟢 What is new and regional this pass: the integration seam, placed

p340's completed connector census ([`p340-connector-licence-census`](../evidence/p340-connector-licence-census.2026-10-20-p340.tsv), 93 repositories probed first-hand) produced the first **regionally placed supply** this base has held — placed by the **institution a connector points at**, which is a fact about geography rather than an inference from a commit footprint (`intel/trends.md` T30).

### Opportunities by region

#### North America

- **The connector seam is permissive and locally precedented.** `skhdemo/uoft-quercus-mcp` (**MIT**, grant read first-hand) connects **University of Toronto Quercus**, a Canvas tenancy, via a personal access token — a worked Canadian precedent, and the first Canada-placed artefact of any kind on these shelves, against a canonical block that has declared Canada an informed gap. 🟡 It states plainly that it is unaffiliated with the university and may be rate-limited.
- **Canvas is the region's dominant seam and it is 100% permissive**: 30 permissive lanes of 40 probed, **zero copyleft found**. For a US or Canadian engagement, the LMS integration layer carries no licence obligation into the deliverable.
- 🔴 **The constraint is grant absence, not copyleft:** 7 of 40 Canvas connectors have **no licence path anywhere in their tree**, including `DMontgomery40/mcp-canvas-lms`, which roundups still recommend. Verify before adopting.

#### EMEA

- **A European Moodle tenancy now has a permissive precedent.** `pablopc05/mcp-usc` (**MIT**) connects the **Campus Virtual Moodle of the Universidade de Santiago de Compostela**, Spanish-language, with CI, acting only under the student's own account permissions. 🟢 **It is also the evidence that corrected T25:** Moodle's connector layer is **85% permissive** (11 of 13 granted lanes), so the platform's GPL-3.0 does **not** force a copyleft connector.
- **The compliance runway is unchanged and still the clearest "why now" in this KB** — Annex III education obligations at **2027-12-02**, Article 50 transparency live since **2026-08-02**, Article 4 literacy in force. An engagement starting now is design; one starting in 2027 is remediation.
- 🔴 **Architecture note that follows from the census:** `psychquant/che-ntucool-mcp` ships **human confirmation gating on writes** (grades, announcements). **That is the Article 14 human-oversight control, already implemented in an MIT codebase** — cheaper to adopt than to specify from scratch in a conformity file.

#### APAC

- **Two institution-placed permissive lanes, both MIT and both read first-hand.** `psychquant/che-ntucool-mcp` connects **NTU COOL**, National Taiwan University's Canvas deployment — and notably **every endpoint was curl-tested against a real course before any code was written**, plus the write-confirmation gate above. `sonaiengine/ku-portal-mcp` connects **Korea University's KUPID** portal and is published to **PyPI**. `kimmahone/edu-workspace-mcp` (MIT) is a Korean-language read-only Google Workspace reader.
- **The regulatory fit is good and the clock is real.** Vietnam classes education AI as high-risk with automated assessment named explicitly; Korea's Basic Act puts education in its high-impact class. 🟢 **A connector that gates writes behind human confirmation is the control both regimes ask for**, and it exists here as MIT source rather than as a requirement to be built.
- **Mandated-curriculum delivery remains the volume opportunity** (China from age six, India from Class 3), unchanged this pass.

#### LATAM

- 🔴 **The supply gap stands, and p340 probed two candidates in order to say so rather than leave it silent — fifth consecutive measurement.** `idavi/usp-mcp`, whose slug names **Universidade de São Paulo** and which these shelves have carried, **does not exist**: `git ls-remote` returns no refs. `DaviPac/Classroom-mcp` has a **Portuguese** README written from the student's perspective and references **SIGAA**, the academic system of Brazilian federal universities — then turns out to have **no licence path in its tree and two commits, both authored `Claude <noreply@anthropic.com>` at `+0000`**.
- 🔵 **The informed form of the gap, and it is a different and more useful claim than "we found nothing": LATAM institutions run these platforms, and connectors to them are not being published.** EMEA and APAC each produced a real, MIT-licensed, institution-specific connector this pass; LATAM produced one dead slug and one ungranted stub.
- 🟢 **Which makes it a build opportunity rather than an adoption one, and the parts are already permissive and regionally adopted.** The demand side is the strongest-evidenced on this shelf (**87% of 200 institutions across 19 countries using AI, 26% with a strategy**). The toolchain favours the region: **`chamilo/chamilo-lms`** has a disproportionate regional install base, **`falkenslab/moodle-mcp`** ships Spanish documentation, **`pablopc05/mcp-usc`** is a Spanish-language Moodle connector that can be forked rather than written, and **`learningequality/kolibri`** (MIT) is the offline-first answer for low-connectivity deployments. **A LATAM institutional connector is a two-week fork of an EMEA one, not a greenfield build.**

#### Global

- **All six MCP-reachable LMS platforms now have a permissive lane with a grant read from the file** — Canvas, Moodle, Google Classroom, Brightspace/D2L, Blackboard and Open edX were three such platforms at p339 and are six at p340. **The LMS seam is no longer the open question in scoping an education engagement.**
- 🔴 **Two global cautions from the census, both of which cost money if missed.** **23 of 93 connectors (25%) carry no licence at all** — on Blackboard, 4 of 7 — and an unlicensed repository is a harder blocker than a copyleft one because it states no price. And **one repository's `LICENSE.md` is a bespoke proprietary licence** (`AStheTECH/mewcp-google-classroom`, the "AStheTECH Community License") that forbids commercial use, SaaS hosting and white-labelling: **it passes every naive licence check and fails a legal review** (`intel/trends.md` T29).
- **On Open edX specifically, prefer LTI 1.3 over MCP.** Both MCP lanes that exist are **AGPL-3.0**; the LTI seam carries no such reach.

## Pass 339 · 2026-10-20 — the headline number is unresolvable to one figure, and the regulatory clock in EMEA just moved 16 months; both change how an engagement should be scoped

### Market size — a range, not a number

The four firms measured this pass do not agree, and the spread is wide enough that quoting a single figure to a client would be misleading. Recorded as a range with each source's own framing:

| Source | 2026 figure | Forward projection | CAGR |
|---|---|---|---|
| Precedence Research | USD 9.58 B | USD 136.79 B by 2035 | 34.52 % |
| Grand View Research | USD 11.4 B (2025: USD 8.3 B) | — | 25.9 % (2026–2033) |
| Aggregator (newmarketpitch) | USD 10.4 B | USD 32.27 B by 2030 | — |
| Higher-education segment only | USD 4.09 B | — | — |

🔵 **Usable reading: AI-in-education is a USD 9–11 B market in 2026 growing in the mid-20s to mid-30s percent.** The 2035 figures diverge by an order of magnitude because the firms disagree on whether "AI in education" means AI-native products or all education software with AI features. 🔴 **Several of these are vendor or aggregator pages, not primary research**; the methodology spread is the finding, and any client-facing figure should be attributed to one named report rather than blended.

**Regional share, from the same channel:** North America holds the largest share at ~36 %; APAC is the fastest-growing at ~35.3 % CAGR. Assessment and grading is called out as the fastest-growing segment, driven by academic-integrity pressure — which is a demand signal pointing at exactly the layer the EU just reclassified as high-risk.

### The structural market map

Education AI splits into four buyers who do not share budgets, and conflating them is the most common scoping error:

1. **K-12 public systems** — budget is political, procurement is slow, data protection is the gate. Buys district-wide, needs teacher training more than models.
2. **Higher education** — devolved budgets, faculty are the real buyers, academic integrity and assessment dominate the agenda. Open-source-friendly by culture.
3. **Corporate academies / workforce** — fastest decisions, clearest ROI story, increasingly the same buyer as HR tech. Where Open edX and Frappe LMS land.
4. **Consumer / supplemental** — app-store dynamics, high churn; in APAC and LATAM this tier is where the venture money and the local champions are.

**Key named players observed this pass.** Anthropic launched **Claude for Teachers** (July 2026), giving verified US K-12 educators free premium access through at least 30 June 2027, and open-sourced the underlying skills as `anthropics/k12-teacher-skills` (Apache-2.0, verified). ByteDance's **Gauth** ranks among top US education apps. **TAL** pivoted to AI learning hardware after China's tutoring crackdown. **PhysicsWallah** listed at ~USD 5 B and shipped its own AI tutor; **BYJU'S** collapsed into insolvency — the two facts together are the clearest statement of how the Indian market re-rated. **Teachy** (Brazil) exports AI lesson-prep from LATAM into Asia.

### Opportunities by region

#### North America

Largest market by share (~36 %) and the most legislatively active, but **regulation is state-level guidance rather than binding federal law** — more than half of state education departments have issued AI guidance, with no binding federal AI curriculum standards as of May 2026. Federal direction comes from an April 2025 executive order on AI education for youth. The PIE Network tracked **nearly 100 state bills** this session touching student AI use; Idaho's SB 1227 is the template to read (statewide K-12 framework, AI literacy standards, educator training, data-privacy requirements, and an explicit prohibition on AI replacing human teachers).

- **The opportunity is compliance-shaped, not model-shaped.** Fifty divergent state regimes mean districts need policy-configurable deployments: the same tutor with per-state guardrails, audit logs and human-oversight attestations. That is integration and governance work, which is Globant's shape.
- **Higher-ed AI-competency mandates are a curriculum build.** Purdue is reported as the first US university with a board-approved AI competency requirement for all undergraduates effective Fall 2026; Ohio State's AI Fluency covers the Class of 2029 onward. Every such mandate needs courseware, assessment and faculty enablement at institutional scale.
- **Age-scaffolded access is becoming a product requirement.** NYC's March 2026 "Traffic Light Framework" and Katy ISD's K-6 chatbot ban with scaffolded access through grade 12 (2026-27) both describe the same feature: grade-band-aware capability gating. Few vendors ship it.
- 🟡 **Canada and Mexico were not covered** by the North America leg this pass — the channel returned US-only material. An informed gap, not coverage.

#### EMEA

🔴 **The single most consequential finding of this pass.** Regulation (EU) 2026/1744 — the Digital Omnibus, published 24 July 2026, in force 27 July 2026 — **moved stand-alone Annex III high-risk obligations, which include education, from 2 August 2026 to 2 December 2027.** Education examples explicitly covered: automated marking, admissions triage, exam proctoring. AI embedded in regulated products (Annex I) moves to 2 August 2028. Confirmed across multiple secondary sources; 🟡 every one is commentary, so the Official Journal text should be read before this goes in a client contract.

What was **not** delayed, and is therefore live now:
- **Article 4 AI-literacy duty** — in force since 2 February 2025, applying to staff of both providers and deploying institutions.
- **Article 50 transparency obligations** — apply from 2 August 2026.
- **Article 5(1)(f)** — emotion inference in educational institutions is an outright **prohibition**, not a high-risk category, exempt only for medical or safety reasons.

- **The opportunity is a 16-month conformity runway, and it is perishable.** Clients get until December 2027 to build Annex III conformity — technical documentation, risk management, human oversight, post-market monitoring — for grading and admissions AI. Engagements that start in 2027 will be remediation; engagements that start now are design. This is the clearest "why now" in the KB.
- **AI literacy is billable today.** Schools are reported to be requiring AI-literacy certification from vendors as part of tendering. Article 4 is already in force, and teacher training is repeatedly named as the binding constraint on scale.
- **Build the emotion-inference prohibition into reference architectures.** Any engagement-detection or attention-monitoring feature is banned in EU educational settings. Catching that at design time is cheap; catching it at audit is not.
- The European Commission, with the OECD and G7 endorsement, has introduced a draft **AI Literacy Framework** for primary and secondary education — a curriculum anchor worth tracking, though education policy stays national.

#### APAC

Fastest-growing region (~35.3 % CAGR) and the most fragmented regulatory picture — a patchwork of three broad models.

- **China has the most developed binding regime** in the region: algorithm registry, deep-synthesis rules and generative-AI measures requiring security assessment and algorithm filing before public launch, with mandatory AI content labelling since September 2025. It is also furthest on curriculum — AI reported as a **compulsory subject from age six as of September 2025**, with ethics, privacy and equitable access lagging the rollout.
- **India moved at the platform layer and the curriculum layer at once.** Amended IT Rules took effect **20 February 2026**, imposing labelling and due-diligence duties on intermediaries handling AI-generated content. AI and computational thinking become **mandatory from Class 3 in 2026-27** across government and private schools, backed by a ₹500 crore centre of excellence and the ₹10,372 crore India AI Mission.
- **Vietnam's new law classes AI in education as high-risk**, explicitly covering automated assessment and behavioural monitoring — the same category the EU just deferred, arriving on a different clock.
- **The opportunity is mandated-curriculum delivery at national scale.** China from age six and India from Class 3 are both state-mandated build-outs: teacher enablement, content localisation and assessment infrastructure, procured nationally. Nothing else in this KB has that volume.
- **The compliance opportunity is pre-launch, not post-market.** Where the EU demands conformity files, China demands filing and assessment *before* a service goes public. Same work, different gate, and it must be scoped into the delivery timeline rather than bolted on.
- **The post-crackdown market has re-formed around non-academic STEM, coding and AI tutoring**, plus AI learning hardware (TAL). UNESCO notes readiness varies widely; infrastructure and teacher training matter as much as policy.

#### LATAM

The region with the most initiative density relative to spend, and the one where the regulatory frame is still being written.

- **Adoption is real and measurable.** The IDB counts **193 AI education initiatives** across the region, of which **59 % use generative AI** and 27 % use language models. 🔴 But CENIA (Chile) found **13 of 19 countries studied do not teach early AI in schools** — the gap between pilot activity and curriculum is the defining feature of this market.
- **Regulation is in motion, not settled.** Brazil's **Bill 2.338/2023** has passed the Senate and sits in the Chamber of Deputies; it would classify education uses such as student selection as high-risk, with fines to **BRL 50 M or 2 % of turnover**. LGPD already governs personal data in AI systems. Mexico has a proposed ethical-AI framework criticised for copying the EU risk model; Argentina's submitted bill is explicitly deregulatory. 🟡 Brazil's bill status should be re-checked against Chamber records before it is quoted.
- **Funded demand exists and is dated.** **Google.org committed USD 4.6 M** across Argentina, Brazil, Chile, Colombia, the Dominican Republic, El Salvador, Mexico, Peru and Uruguay, targeting **1.25 M students by 2028**. **UNESCO launched its Observatory on AI in Education for Latin America and the Caribbean in April 2026**, with a Mexico pilot alongside CONALEP and DGETI to build centres of excellence.
- **The strongest commercial signal is employability, not courseware.** The HolonIQ 2026 LATAM EdTech 100 shows a shift from course delivery to job-outcome-linked training: **Ginia** (Mexico, AI-driven employability), **Vetto** (Brazil, newly funded on the same thesis), **Teachy** (Brazil, AI lesson prep, now exporting to Asia), **Mattilda** (Mexico, school billing and collections, USD 50 M plus an acquisition).
- **The opportunity is Spanish/Portuguese-first delivery into the curriculum gap**, and the toolchain already favours it: **`chamilo/chamilo-lms`** has a disproportionate regional installed base, **`moodle-mcp`** ships Spanish documentation, and **`learningequality/kolibri`** (MIT) is the offline-first answer for low-connectivity deployments. A regional engagement can be assembled from permissive and regionally-adopted parts rather than from US defaults.

---

## ⏷ Carried history — everything below this line predates Pass 339 and was NOT rewritten

🟢 **Pass 339 prepends; it does not replace.** An earlier draft of this pass replaced these shelves outright and `gate-permissive-arm` caught the cost: the corpus lost ~1.2 MB of first-hand-verified rows and the `MIT`+`Apache-2.0` cell count fell from 7 000+ to 6 597. 🔵 **Deleting verified rows is not curation** — the live section above carries this pass's findings, and every prior pass's verified shelf stands underneath it.

## Pass 338 · 2026-10-20 — the regional legs returned real material for the first time in four passes, and the gate that polices this file's own region contract had never been run

🟢 **The supply side is unchanged and saturated for a ninth consecutive pass** (see `agents/top.md`). 🔵 **The demand side is where this pass moved**, and the shape is the same in every region that answered: **usage is near-universal, governance is scarce, and the gap is the engagement.**

| leg, run verbatim 2026-10-20 | what came back |
|---|---|
| `top open source AI agents education 2026 github MIT` | 🔴 **0 new.** Listicles; the only education rows are courseware already carried |
| `github trending education AI 2026` | 🔴 **0 new.** GitHub Trending has no education category |
| `open source platform education ERP CRM MIT Apache` | 🔴 **0 new**, and **5 of 9 results were one vendor's glossary in 5 languages** (`openeducat.org`). 🟢 Re-confirmed: **OpenEduCat is LGPL-3.0**; the leg presumes an MIT/Apache education ERP that does not exist |
| `AI education industry trends 2026` | 🟡 **Market sizes irreconcilable across three publishers** — third consecutive pass. Recorded as a conflict, never as a number (`intel/trends.md` T-338.2) |

🔴 **The structural finding of this pass belongs to this file.** The engagement contract fixes this file's shape — *"opportunities go under a single `## Opportunities by region` heading with one `###` subsection per region"* — and an instrument for it exists (`compose/code/p383-region-heading-gate`) with its own passing test suite. 🔴 **It was wired into no Makefile target and had therefore never judged this file.** Run for the first time this pass: **5 canonical blocks**, 2 missing `Global` children, 14 out-of-vocabulary `###` headings adopted as regions.

🟢 **Fixed in this pass, both halves:** `p383` now runs in the `hooks` tier (22 gates → **23**), and this file now carries **one** canonical block with exactly the **five** closed-vocabulary children. The four earlier blocks are **relabelled, not deleted** — their content stands as history, and only the live block claims the canonical heading. 🔵 **The two append-only files were not touched by the restructure.**

🟢 **One licence question CLOSED, and it was closed from this base's own shelves.** This file registered *"Forma LMS: Apache-2.0 vs GPL-v2, unresolved"* one pass ago. 🔴 **It was resolved 72 passes ago at `p265` and reproduced at `p276`.** Re-measured first-hand today: `formalms/formalms`, `master`, **`html/license.txt`**, **18 346 B**, GPL-2.0, `sha256`₁₆ **`4e63feff285d9215`** — the hash on the shelf. 🟡 **For a bid, this matters in one direction: a permissive reading of Forma LMS is wrong, and a root-only SPDX scan will report the platform as unlicensed rather than GPL-2.0.**

---

### 🟢 Key players and market map, as this pass's channels named them

🔵 **Named by the regional legs, recorded with the channel and not promoted to a ranking** — this base has no instrument that ranks vendors, and a listicle's order is not one.

| layer | who the channel named | region of the naming |
|---|---|---|
| hyperscale / platform | IBM · Microsoft · Google — a market the report itself calls *"highly fragmented"* | North America |
| courseware capital | Carnegie Mellon + Gates Foundation, **$55M** into AI courseware | North America |
| national programmes | OpenAI country-level education programme with national partners, **Q1 2026** | 🟡 stated as global; placed by the source, not by this base |
| corporate L&D (a **different market** from schools) | Pearson + TCS multi-year AI learning alliance · LearnUpon (Sydney HQ, Create+ authoring) · Alteryx academy | APAC |
| research / measurement bodies | Digital Education Council · UNESCO IESALC · UNU-IAS · CEPAL/IDB (**ILIA 2025** index, 19 countries) · Tecnológico de Monterrey IFE | LATAM |
| ministries and sector bodies | SEP · ANUIES · Observatorio IA (all **non-binding** proposals) | LATAM |
| 🟢 open-source platform tier | **OpenOLAT** (Apache-2.0) · Moodle · Open edX · Chamilo · RosarioSIS · openSIS · Forma LMS — all re-read first-hand this pass | 🟡 Global, EMEA-maintained |

---

## Opportunities by region

### North America

- 🟢 **Added p345 — the responsible-experiment seam, and it is a differentiator rather than a feature.** `terracotta-education/terracotta` (**Apache-2.0**, 2 815 commits, 18 authors, live 2026-10-19, `unicon.net` + `iu.edu` + `calpoly.edu`) delivers randomised controlled trials **inside live coursework** over LTI 1.3, with consent collected in a form the instructor cannot see and non-consenting students filtered out of exports. 🔵 **The opportunity:** every US district and university buying an AI tutor this year is being asked by a board or an IRB to show it worked. ~34 states plus DC and Puerto Rico have issued AI guidance and the federal layer reports **zero** binding curriculum standards, so the burden of proof is institutional — and an engagement that ships the evidence layer with the tutor wins the renewal. See `compose/patterns.md` **`P31`**. 🟡 **Named statutes to design against:** Idaho SB 1227 (signed 2026-03-19, effective 2026-07-01), Ohio (district AI policy due 2026-07-01), Oklahoma SB 1734 (policy before 2027-28), SUNY AI literacy in general education from Fall 2026.

🔴 **The sellable gap is governance, and it is ~56 points wide.** ChatGPT used by **66%** of students; **only 10%** of institutions have formal AI guidelines; **71%** of US teachers report no AI training *(search channel, vendor roundup — attributed, not asserted)*.

- 🟢 **AI acceptable-use and assessment-redesign engagements.** No model ships this. The deliverable is policy + training + an audit trail, and the buyer already has the usage problem.
- 🟡 **The regulatory surface is a state patchwork, not a federal rule** — Colorado and Texas have introduced piecemeal requirements; there is no single rulebook. 🔵 **Sell per-state compliance mapping, not "AI Act readiness."**
- 🔴 **Any NA vendor selling into Europe inherits the EU AI Act's high-risk classification for education.** That is a cross-border design constraint on a US-built product, and it is cheapest to honour at architecture time.
- 🟢 **Build-on tier for closed IP:** `OpenOLAT` (Apache-2.0, 10 982 B) and `JupyterHub` (BSD, 1 475 B) — the two platforms whose grant does not reach your layer.
- 🟢 **Added p343 — the mandates are no longer all prospective, and three of them change what you BUILD, not just what you file.** **New York City** places **grading and discipline** in a *prohibited* tier, so an NA K-12 product must be able to demonstrate that a human decision sits between the model and the record. **California AB 1159** would bar using **student data to train AI models** — a constraint on the training pipeline, not on the UI, and the one most likely to invalidate an architecture that already exists. **SUNY** has adopted a systemwide policy across **all 64 campuses**, with **AI literacy in general education from fall 2026** — a single procurement surface covering a whole state system. **Alabama H.B. 329** makes a CS course including AI instruction a **graduation requirement**, which is the curriculum-content buy rather than the governance one.
- 🔴 **Added p343 — this subsection is US-only and must be read that way.** The prescribed leg returned **no substantive Canadian source**. 🟢 **Written down rather than left as apparent coverage:** a Canadian engagement cannot be planned off this subsection, and a future pass should run a provincial leg (Ontario, Québec, British Columbia) — because *"North America"* is a vendor sales region and no ministry describes itself with the word. That is `ACTION ZR`'s lesson applied to the other side of the border.

- 🟢 **Added p344 — the state surface now has a volume number and four hard mandates, which turns this from a narrative into a pipeline.** **134 AI-in-education bills introduced across 31 states in 2026.** **Maryland, Idaho, Oklahoma and Virginia** require **both** state guidance **and** mandatory district-level AI policies; **Ohio's district mandate deadline was 2026-07-01 and has passed.** 🔴 **Every district under those mandates owes a written policy, an inventory of AI uses and an oversight record, and almost none has the staff to produce one** — a repeatable, scoped engagement with a date already behind it.
- 🔴 **Added p344 — the amended COPPA Rule has been binding since 2026-04-22** on any child-directed service. Together with NYC's prohibition on AI in **grading, discipline and placement**, the region's K-12 constraint set is now as concrete as EMEA's and arrives sooner.
- 🟢 **Added p344 — the Article 14-shaped human-confirmation control is a NA requirement too, and it already ships as MIT source.** `psychquant/che-ntucool-mcp` gates grade and announcement writes behind explicit human confirmation — the same component answers NYC's prohibition, Korea's Act and Vietnam's classification.
- 🔴 **Added p344 — the sharpest grant-absence specimen yet is US-placed.** `loyaniu/moodle-mcp` is institutionally benched (`calvin.edu`, with a genuine `rwth-aachen.de` EMEA co-contribution) and ships **no licence payload and no manifest declaration** ⇒ all rights reserved. **The most credible-looking connector in the region is the one that cannot be built on.**

### EMEA

- 🟢 **Added p345 — sell the re-ordering, not the reprieve.** Regulation (EU) **2026/1744** defers **Annex III** education high-risk from 2026-08-02 to **2027-12-02** (secondary-source convergence; **every EU primary host returns HTTP 000 from this environment**, so the date travels as a claim with its channel named). 🔴 **Two obligations did not move:** emotion recognition in education has been **prohibited since 2025-02-02**, and Article 50 transparency applies from 2026-08-02. 🔵 **The engagement, concretely:** an affect-feature audit billable **now** (attention scoring, engagement detection and affect-aware tutoring are out, deferral or not), and an Annex III documentation programme that can be scheduled across 2027 instead of crashed. 🟡 **The supply-side caveat for delivery:** this region's best-placed new row is a **5-commit** bench (`AI-for-Education/pedagogy-benchmark`, MIT, `glasgow.ac.uk`), so European engagements should expect to import their implementation bench and keep the local contribution in governance and evaluation.

🔴 **This region returned NOTHING education-specific on the prescribed leg, and that is written down rather than left as apparent coverage.** Every result was enterprise AI or general EU AI Act commentary; one of two substantive sources is a **2023** study. No edtech vendor, no ministry of education, no school-level rule, no student-data material.

- 🟡 **What stands, because it is the one named binding instrument:** the **EU AI Act classifies education AI as high-risk.** EMEA is the only region where **regulation leads adoption** — the inverse of everywhere else.
- 🟢 **That inversion is itself the opportunity:** conformity-by-construction. Documented data lineage, human-in-the-loop on anything affecting grades or progression, and a technical file that exists before the audit does.
- 🟢 **The supply side here is genuinely strong and already on these shelves** — H5P (Norway), `openpatch/hyperbook`, `otacke/h5p-theme-picker` (Germany), OpenOLAT (Zurich). **EMEA is this KB's deepest permissive authoring stack**, which makes the thin policy reading the more frustrating.
- 🔵 **`ACTION ZR` applies here first:** re-run this region with political names (*"AI in schools Europe regulation 2026"*, *"EU AI Act education high-risk"*), because `EMEA` is a vendor sales region and no ministry describes itself with the word.
- 🟡 **Added p343 — the AI Act's education-enforcement date is CONTESTED across sources, and this base publishes neither.** One has the Commission's AI Office and national authorities enforcing **from 2026-08-02**; another has amendments adopted **June 2026** and in force **2026-07-27**. 🔵 **Sell against the obligations, which are not in dispute** — risk management, data governance, human oversight and conformity assessment before deployment, for admissions, student evaluation and exam scoring — **and let the client's counsel own the date.**
- 🟢 **Added p343 — the non-binding instrument is the cheapest way in.** The Commission's **updated ethical guidelines for educators on AI and data** are explicitly motivated by *"the significant increase of AI usage in education and the introduction of regulations like the AI Act."* A guidelines-shaped deliverable is procurable without a high-risk conformity exercise, and is the natural engagement ahead of one.
- 🔴 **Added p343 — the MEA half of this region is a POLICY gap, not a supply gap, and the two were being merged.** The leg returned nothing on the Middle East or Africa for another pass. 🟢 **But `ahmedEid1/lumen` (GPL-3.0, 828 commits, 3 authors) carries `+0200` on all 828 commits *including 39 outside Mar–Nov* — a non-shifting UTC+2 zone, i.e. the MEA band, not CEST.** There are builders here; there are no retrievable rules. 🟡 **A band is not a country:** this does not distinguish South Africa from Egypt, and this pass does not claim to.
- 🟡 **Added p343 — do not quote the regional market size.** A $2.64B (2026) → $8.0B (2030) at 31.9% figure circulates for European education AI from a low-authority aggregator. `ACTION ZQ` holds: **attribute or omit.**

- 🟢 **Added p344 — the Annex III clock moved again and the split is now the whole EMEA pitch.** **Regulation (EU) 2026/1744** (July 2026) moves stand-alone high-risk **education** systems to **2027-12-02**. 🔴 **Article 50 transparency duties are live since 2026-08-02 and are being enforced** by the AI Office and national authorities. 🟢 **So: sell transparency and oversight instrumentation NOW, and scope the Annex III conformity work against 2027.** 🟡 Sources disagree on the amendment's exact entry-into-force date; the **2027-12-02** and **2026-08-02** dates are consistent across all of them and are the two to quote.
- 🟢 **Added p344 — schools are DEPLOYERS**, carrying human-oversight and transparency duties themselves. **That is a governance-tooling engagement that does not require replacing any platform** — the cheapest possible entry into an institution.
- 🟡 **Added p344 — new EMEA supply, with the limits that decide its use.** `formalms/formalms` (**Forma LMS**) — a 13-year Italian corporate-training LMS, **7 494 commits · 59 authors**, real vendor bench (`joint-tech.it`, `grifomultimedia.it`), **0% agent-authored**, placed **EMEA — Italy** on a CET/CEST pair. 🔴 **It is GPL-2.0 and three months stale, and a secondary source called it Apache-2.0 — the payload at `html/license.txt` refutes that.** Useful only where copyleft is already accepted; **not a permissive foundation.**

### APAC

- 🟢 **Added p345 — the richest supply channel on these shelves, and the thinnest governance one.** One GitHub topic query returned **12 live rows**, among them `122-syf-wcy/PhysicsOS` (251 ★, a K-12 physics agent driving a real physics engine so a problem becomes an inspectable scene), `Li-Evan/Bloom` (289 ★, placed APAC — China at p343), `Miaotofu01/Study-Mate`, `Zenglian990/AI_Tutor_Release` and `zhangl1001/civil-ai`. 🔴 **The policy leg returned zero school-level rules for China, India or Singapore**; Japan shows movement toward official digital textbooks with no AI-specific rule attached. 🔵 **So the opportunity is inverted here: the buildable material is local and abundant, and the governance is what a studio supplies.** 🟡 **One counter-intuitive datum worth quoting to a client** (Digital Education Council Global Survey 2026): APAC faculty are the **most enthusiastic** (57% excited) while faculty **intent** to use AI fell **76% → 67%**, the lowest of any region — enthusiasm and intent are diverging, which is a change-management engagement, not a licensing one.

🔴 **Also returned nothing education-specific.** The education-adjacent hits are **corporate L&D** (Pearson/TCS, LearnUpon, Alteryx) — a different buyer from schools and universities. **No national education-ministry AI policy surfaced.**

- 🟡 **The governing posture that did surface is *"sovereign-by-design"***: 2026 is described as the year APAC moves from pilots to production with data residency and sovereignty as the design constraint.
- 🟢 **Read commercially, that favours the self-hostable stack this KB already curates** — Moodle/OpenOLAT/JupyterHub on client infrastructure beats a hosted SaaS tutor in any sovereignty-led procurement. 🔵 **The AGPL §13 trap is the thing to get right**: hosting a *modified* Open edX for a client triggers the source offer, so the boundary is unmodified core + XBlock/LTI.
- 🟡 **A measured adoption constraint, for enterprises rather than schools:** **49%** of APAC businesses cite insufficient real-time data infrastructure.
- 🔴 **Named rows already on these shelves place real APAC supply** — `PerryLink/dsh-essay-rubric-check` (China, `+0800`), `likr/canvas-lms-agent` (Japan, `+0900`), `corsairdev/corsair` (India, `+0530`) — **so the region is not empty of builders; the policy channel is empty of answers.** Those are different gaps and must not be merged.
- 🟢 **Added p343 — one new binding instrument that names education directly: Vietnam's mid-2026 decision on high-risk AI systems covers education, including automated assessment.** 🔵 **That makes Vietnam the second jurisdiction on these shelves, after the EU, where automated assessment is high-risk by statute** — and the cheaper of the two to design for first, because the obligation set is narrower.
- 🟢 **Added p343 — six more APAC rows placed on the commit channel** (`agents/top.md` this pass), and the regional bench is now legible: **China** — `Miaotofu01/Study-Mate` (1.1k ★, **727 commits in five weeks**, `+0800(711)` + `qq.com(197)`) and `Li-Evan/Bloom` (289 ★); **Australia** — `zijinz456/OpenTutor` (`+1100/+1000`, the AEDT/AEST pair); **India** — `karanb192/algo-sensei` (`+0530` on all 9, 🔴 **293 ★ on nine commits, dormant**). 🔵 **APAC is this base's largest regional supply bench by row count and its youngest by history** — most of it is weeks old, so place it as momentum, not as a dependency.
- 🟡 **Added p343 — the exam-prep cluster is this region's distinctive product shape, and it carries a trap worth naming.** `KeWang0622/kaogong-skill` is China civil-service exam preparation whose **authorship** channel reads `-0700/-0500` on five commits, and it resolves to **NOT RESOLVED**. 🔵 **A China-facing product need not have a China-based bench** (`ACTION ZZ-b`), so a regional headcount built from subject matter will overstate this region.

- 🟢 **Added p344 — Vietnam now carries the most explicit education-AI rule in the world, and it has a grandfathering window that is open today.** The Vietnam AI Law names **education** among its high-risk systems — **automated assessment and behavioural monitoring** — with compliance due **2027-03-01**, plus **six months' additional grace for education systems already operating before 2026-08-15.** 🔴 **A system shipped into Vietnam now sits inside that window: a dated, concrete reason to start rather than wait.**
- 🔴 **Added p344 — Korea's Framework Act on AI has been in force since 2026-01-22**, carrying high-impact and generative-AI duties **and a local-representative requirement for large foreign firms.** 🟢 **That is a contracting constraint, not merely a compliance one, and it must reach a Korean proposal before any architecture does.**
- 🟢 **Added p344 — the region's supply is the strongest on these shelves and it just gained the vertical's only live full education ERP.** `openeducat/openeducat_erp` — 🟡 **LGPL-3.0** (read first-hand, `19.0/LICENSE`, 8 241 B), **India**, **1 711 commits · 97 authors, live 2026-10-13**, placed on `techreceptives.com`/`openeducat.com` with `+0530` on 1 493/1 711. 🔴 **Architect it at arm's length: agents outside the ERP, over its API — an Odoo-style addon that subclasses a core model is a modification under the LGPL, not a link.**

### LATAM

- 🟢 **Added p345 — the region this shelf called barren for six passes produced the single largest new row of the pass, and it was in this base's own orphan list.** `Mcp-Brasil/mcp-brasil` (**MIT code grant, 1 072 B stock**, **1 817 ★**, 301 forks, 246 commits, `-0300` on all of them, pushed 2026-10-20) exposes **INEP** — ENEM microdata and the national school census — plus `FNDE`, through an MCP server over ~70 Brazilian public APIs, with a **PII column whitelist in code**, re-identification **VEDADO** under LGPD art. 12, and formal microdata research routed out to INEP's **SEDAP** service. 🔴 **Its grant is a split cell:** MIT covers the code; `NOTICE` (3 135 B), `ACCEPTABLE_USE.md` (8 109 B) and `SOURCES.md` (19 286 B, 61 headed sections) scope the data, the institutional marks and the permitted uses. 🔵 **The demand side matches:** Latam-GPT launched **2026-02-10** (CENIA, Chile — 65 institutions across 15 countries) and a **UNESCO–CENIA** partnership signed 2026-03 stands up a **Regional Observatory on AI in Education** serving Ministries of Education. 🟢 **The engagement is `compose/patterns.md` `P32`: a defensible-on-day-one agent over national assessment data, 6–8 weeks**, with the four hard rules taken from the project's own documents. 🟡 Also placed this pass but **not** recommended as a bench: `latam-gpt/anonymization-filter` (MIT, `uc.cl`, Chile) — 6 commits, dormant 17 months.

🟢 **The richest region this pass, and the only one with a figure carrying a real denominator.** Digital Education Council **LATAM survey 2026**: **>30 000 responses across 29 institutions** — **92%** of students and **79%** of faculty actively engaging with AI. UNESCO IESALC, separately: **200 higher-education institutions across 19 countries** — teaching and learning **73.5%**, research **57.0%**, administration **34.1%**, community engagement **20.0%**.

- 🔴 **The gap is the widest measured anywhere: ~62 points.** **92%** usage against **~30%** of LATAM universities having published AI policies (Tecnológico de Monterrey, in the same survey).
- 🟡 **Policy is heterogeneous and mostly non-binding.** **Chile** is furthest along — National AI Policy since 2021, a law under discussion. In **Mexico**, SEP, ANUIES and Observatorio IA have produced **recommendations with no binding force**. 🔵 **CEPAL/IDB's ILIA 2025 index covers readiness, adoption and governance across 19 countries** and is the instrument to cite in a regional bid.
- 🟢 **Administration at 34.1% against teaching at 73.5% is the clearest whitespace on this shelf**: the back office is barely touched while the classroom is saturated. **Enrolment, retention prediction, financial aid and SIS workflow** — and `rosariosis`/`openSIS-Classic` are the open SIS platforms, both GPL-2.0, both with the boundary pattern already written in `verticals/solutions.md`.
- 🟢 **Real local supply, placed on the commit channel, not inferred:** `SidneyBissoli/uis-mcp-server` (**MIT**, 1 088 B — UNESCO education statistics over MCP) and `Cvmcosta/ltijs` (Brazil, `-0300` on 513 of 575 commits). 🔵 **Two unrelated maintainers, two instruments, one region — a measurement with a denominator, not an anecdote.**
- 🟡 **`digitaleducationcouncil.com` could not be reached from this environment** (`ENOTFOUND`). The figures above are **attributed to the survey, not asserted by this base**, and the primary PDF is the first thing a future pass should fetch from a network that can reach it.
- 🟢 **Added p343 — THE FINDING FOR THIS REGION, and it was on these shelves the whole time: the Brazilian curriculum-standards layer is available, permissively licensed, and already hosted.** `bncc-dev/bncc-pacotes` + `bncc-dev/bncc-dados` + `bncc-dev/bncc-benchmark` — **MIT code, CC BY 4.0 data** — carry **1 721 learning objectives of Brazilian basic education**, which the README states are *"verificadas contra os documentos oficiais do MEC/CNE"*. They ship as `@bncc/dados` (npm **v0.7.0**, typed TS API), `bncc` (PyPI **v0.5.0**), `@bncc/mcp` (npm **v0.6.0**) **and a hosted MCP server at `mcp.bncc.dev` — streamable HTTP, NO API KEY, seven tools** (`bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`). Placed **LATAM — Brazil** on both channels: `-0300` on **225 of 225** commits across the three repositories, with `profy.com.br` on **211** of them. 🔵 **A Brazilian engagement can call a national curriculum from an agent on day one and spend its budget on the platform half.**
- 🔴 **Added p343 — and the reason six passes missed it is the CHANNEL, not the region: nine stars.** Every discovery leg this base runs is star- or trending-ranked, and a nine-star repository with a production MCP server over a national curriculum is invisible to all of them. 🟢 **`ACTION ZZ-d`: query the package registries and the framework NAMES — `BNCC`, `SEP`, `Aprende`, `MEC` — not the star count.**
- 🟢 **Added p343 — the complementary gap, enumerated from an asset's own source list rather than from a silence.** `withmarbleapp/os-taxonomy` (6.6k ★, the most-cited education repository of this month) carries **3 881 standards from eight frameworks and not one of them is Latin American** — UK National Curriculum, Australian Curriculum v9, Common Core, NGSS, NCSS, IB. 🔵 **So the dominant open curriculum graph has no LATAM spine, and the LATAM spine exists separately under a CLEANER grant than that graph's own US tiers** (CC BY 4.0, against a purpose-limited CCSS licence and a codes-only NGSS tier). **That composition is this region's clearest build, and `compose/patterns.md` R-343.1 is it.**
- 🟡 **Added p343 — Mexico's first named education-touching instrument: the Chapultepec Principles**, a ten-point ethical framework for the use and development of AI presented by **SECIHTI and the ATDT in January 2026**. Non-binding. At least **six** legislative initiatives 2022–2025, **none approved**; an early-2026 Senate bill proposes a risk-classification body. 🔵 **Mexico is a guidelines market, not a compliance market — price it accordingly.** Brazil's **PL 2338/2023** remains Senate-passed (2024) and **awaiting the Chamber of Deputies**.
- 🔴 **Added at p341, and it revises how this subsection's "gap" should be read:** the regional **platform** supply was never absent, it was **unreadable** — `portabilis/i-diario` sat on these shelves for 22 passes as *"licence not shown"* because both shared family classifiers are English-only, and its Portuguese payload is **`AGPL-3.0`** (`intel/trends.md` **T31**). **Read the payload on a LATAM engagement; do not trust the sidebar or a scanner.**

- 🟢 **Added p344 — the region finally has a hard denominator, and the gap IS the engagement.** **UNESCO IESALC with UNU-IAS: 200 institutions across 19 countries — 87% use AI somewhere in operations, and only 26% have a formal AI strategy.** 🔴 **A 61-point gap.** Adoption is **faculty- and student-driven rather than institutional**, so the buyer is a rector or provost who has **already lost control of the surface and needs it mapped**. 🟡 **Private institutions have materially more planning and governance capacity than public ones** — the realistic first cohort.
- 🟢 **Added p344 — the convening structure exists and should be aligned to rather than competed with.** **UNESCO's Observatory on AI in Education for Latin America and the Caribbean launched 2026-04-14**, with **CAF, CENIA (Chile), ECLAC, Fundación Santillana, Tecnológico de Monterrey, ProFuturo and Fundación Ceibal (Uruguay)**, plus a Mexico pilot building centres of excellence with **CONALEP and DGETI**.
- 🟡 **Added p344 — regulation here is general-purpose, NOT education-specific** (Uruguay's Council of Europe convention signature, Peru's phased framework, Colombia's CONPES 4144, Mexico's Senate bill, Brazil and Chile in motion). 🟢 **So a LATAM engagement is sold on the adoption gap and institutional risk, never on a compliance deadline. That is the inverse of the EMEA and APAC pitch and must not be copied from them.**
- 🔴 **Added p344 — the supply count, stated as a count for the second consecutive pass: ONE instrument-placed LATAM row** (`Cvmcosta/ltijs`, Brazil). 🟢 **Plus the largest cross-region bench measured on these shelves — 216 commits at `-0300` by a single author inside `formalms`** — 🟡 **whose country is NOT resolvable from the available evidence: every sampled month falls inside the southern DST window, so Chile and Brazil are indistinguishable (`ACTION ZZ-d`). The band is LATAM; the country may not be written, and this creates no LATAM row.**

### Global

- 🟢 **Added p345 — two cross-cutting facts a studio can use in any region.** 🔴 **Market sizing from this channel is unusable:** two sources attribute incompatible 2026 figures to the *same* analyst (≈ **USD 23 bn at ~42% CAGR** and **USD 12.3 bn**), so it is published as a conflict and never as a number; the adoption percentages in the same channel come from vendor pages with self-reported surveys. 🟢 **What IS reusable is the promotion discipline:** of 12 live rows a single topic query returned, **9 had sat on a trending shelf without ever being adjudicated** — one at **4 696 ★** — and this base held **528** permissively-licensed addresses it had measured and never offered. 🔵 **For a client running their own radar the lesson transfers directly: measure delivery, not intake, or you will report saturation while sitting on an unread backlog** (`intel/trends.md` **`T41`**). 🟡 **And two placement traps that cost nothing to avoid:** a repository or organisation NAME in a regional language is not a region signal (`ACTION ZZ-g`), and a FORK's commit log measures its upstream's bench (`ACTION ZZ-h`).

🟢 **What holds in every region, and is therefore the reusable part of a bid.**

- 🔴 **Usage leads permission everywhere it was measured.** 66/10 in North America, 92/30 in LATAM. The scarce good is **not capability**; it is **an auditable boundary**. That is one offer, sellable in four regions, and it is what `compose/patterns.md` R-338.1 builds.
- 🔴 **Licence risk sits in two places a standard review misses**, and both are now measured on these shelves: **CONTENT** (curriculum graphs and standards frameworks under ODbL / CC BY-SA / OGL / purpose-limited public licences — p337's T-337.1) and **PATH DEPTH** (a grant at `docs/License.txt` or `html/license.txt` that a root-only SPDX scan reports as *no licence*). 🟢 **Enumerate the tree; never trust a badge.**
- 🟢 **The permissive platform tier is exactly two deep, re-verified this pass:** `OpenOLAT` (Apache-2.0) and `JupyterHub` (BSD). **Everything else in the LMS/SIS tier is copyleft**, and the same architectural boundary answers all seven of them: unmodified core, your logic in a separate service, integrate over LTI or web services.
- 🟡 **Do not quote a market size for education AI.** Three publishers, three irreconcilable figures, three passes running (`ACTION ZQ`). **Quote the surveys with denominators instead** — they are what a client can check.
- 🔴 **Added p343 — the content-licence tier list is the reusable asset, and it is regionally INVERTED.** Read first-hand from `os-taxonomy`'s `PROVENANCE.md` (8 685 B): a curriculum-standards payload is **not** governed by its repository's headline grant. **OGL v3.0** (UK — commercial, adaptable, **no share-alike**) and **CC BY 4.0** (Australia, and Brazil via BNCC) are workable; the **CCSS Public License** is **purpose-limited** and, in that file's own words, *"does not clearly grant derivative-work or sublicensing rights"*; **NGSS** ships **codes only**, because commercial reuse of the text needs **WestEd approval** plus a trademark disclaimer; **NCSS** and **IB** are permission-based. 🟢 **Coverage and usability are different maps: the EMEA and APAC tiers of the dominant graph are its cleanest, and the North American tiers are its worst.** 🔵 **Topic→standard LINKS survive at every tier — it is the standard's PROSE that does not.** So plan a US K-12 product on codes, or licence the text directly.
- 🔴 **Added p343 — a star count and a commit count are not comparable units across repositories, and the test is one command.** `zijinz456/OpenTutor` has **52 of its 194 commits authored by `noreply@anthropic.com`, every one a `chore:`** — weekly build-in-public content, repo health reports, community post drafts, running since March. `ArnaudGuiovanna/tutor-mcp` has **30 of 467 from the same address, every one a `fix:` or `test:`** — migrations, store exceptions, a named stabilization audit. 🟢 **Same channel, opposite meaning: the axis is engineering vs promotion, and only the subject lines carry it** (`ACTION ZZ-c`). **Run `git log --format='%ae%x09%s'` before quoting any row's bench to a client.**

- 🟢 **Added p344 — the structural fact to lead any platform conversation with, now stable across passes: the education PLATFORM tier is copyleft, and the permissive tier is where the AI layer goes.** Eleven platforms measured this pass; **the intersection of *permissive* and *education domain model* is empty**, excepting the Apereo/`ECL-2.0` family. 🟢 **Prescription, licence-robust across Moodle (GPL-3.0), Open edX (Apache-2.0), OpenEduCat (LGPL-3.0) and Forma LMS (GPL-2.0) alike: agents sit OUTSIDE the platform and speak to it over its API; they never ship as patched addons.**
- 🔴 **Added p344 — grant ABSENCE, not copyleft, is the recurring blocker in the connector tier.** Of three MCP connectors re-probed, **two declare MIT in a manifest with no licence text anywhere in the tree**, and **one has neither** (all rights reserved). 🟢 **Two are a one-email fix; the third is a blocker. Check the payload, never the badge.**
- 🔴 **Added p344 — a new global risk class, measured three passes running: agent-authored repositories.** A repository can now be authored, promoted and defaulted-to by an agent while **star count, commit count and timezone offset all stay silent** (`ACTION ZZ-c`, `ZZ-f`). 🟢 **Cheap test: `git log --format='%ae%x09%s' | grep -i anthropic`.** 🔴 **At a 100% agent-authored share the region channel is VOID, not merely weak** — `davipac/classroom-mcp` is the specimen, and its `+0000` offset is a datacenter's, not a geography.
- 🔴 **Added p344 — two addresses carried on these shelves do not exist**, and both resolved one slug away with a default branch no ladder assumes (`openeducat/openeducat` → `openeducat/openeducat_erp@19.0`; `forma-lms/formalms` → `formalms/formalms`, grant at `html/license.txt`). 🟢 **Before relying on any row, read its default ref from `ls-remote --symref` and enumerate the tree (`ACTION ZZ-e`).**
- 🟡 **Added p344 — market sizing remains a RANGE, not a number** (unchanged from p339). The figures this pass's leg returned — a **$12.3B** 2026 size and an **83%** survey number — arrived **without verifiable sourcing from a vendor page and are NOT adopted.**

## Pass 337 · 2026-10-20 — eighth consecutive pass with no new supply from the prescribed legs, and the first one where the reason is measured as SATURATION

🔴 **The four prescribed global legs were run verbatim and returned 0 new promotable repository slugs. Eighth consecutive measurement.** What is new this pass is the *reason*, which is not the same as the previous seven:

| leg, run verbatim 2026-10-20 | what came back |
|---|---|
| `top open source AI agents education 2026 github MIT` | 🔴 General agent round-ups with **no education ranking at all** — OpenHands, OpenClaw, CrewAI, LangGraph. One source's own caveat: AgentGPT is **GPL-3.0 and archived 2026-01-28**. |
| `github trending education AI 2026` | 🔴 Infrastructure and dev-tool repos. The single education-relevant hit, `withmarbleapp/os-taxonomy`, **this base added at p326.** |
| `open source platform education ERP CRM MIT Apache` | 🟡 LMS/SIS vendor and review pages. **Confirmed: there is no mainstream MIT-licensed LMS or SIS** — Open edX is AGPL, Moodle/Chamilo/ILIAS GPL, Canvas CE AGPL, RosarioSIS GPL-2.0. 🟢 **`OpenOLAT` is the Apache-2.0 exception** and is re-verified first-hand this pass at 10 982 B. |
| `AI education industry trends 2026` | 🔴 Vendor trend blogs with **conflicting market sizes** ($6B 2024→$32B 2030 vs $12.3B by 2026). Not usable as a figure; recorded as a conflict. |

🟢 **The saturation measurement, which is the new fact.** The one leg returning education-specific repositories gave 8 candidate slugs; **6 were already `CARRIED`** and the 2 new ones are below bar (10 commits / 2 commits). 🔵 **6-of-8-already-held is a different signal from 0-of-8-found, and it is the healthier one:** it says the channel's education-agent supply has been absorbed, not that the channel is dry.

🔴 **A cross-cutting licence conflict worth carrying, from the search layer itself:** two separate comparison pages list **Forma LMS** as Apache-2.0 and as GPL-v2 respectively. 🟡 **Unresolved — not probed this pass, and not published as either.** Registered as the next licence question for this tier.

---

## Opportunities by region — superseded, Pass 337 (kept for history; the canonical block is at the top of this file)

### North America

🟢 **The buy is a compliance artefact, and the deadlines are already binding.** Trackers disagree on volume — **134 bills across 31 states**, FutureEd's narrower count **68 across 27**, a third source ~100 — and the disagreement is itself the datum: **the definition of "AI-in-education bill" is not standardised**, so a client's own count will differ from any vendor deck. What is NOT in dispute is that **mandates with dates now exist**: Ohio district AI policies due **2026-07-01**; Tennessee requires district policies; Maryland gives its **24** districts **120 days** after state guidance; Oklahoma **SB 1734** requires a written policy before the **2027-28** school year. **35+ states** have education-department AI guidance as of June 2026, and the federal Department of Education finalised its **AI grant-priority rule on 2026-04-13**.

🔵 **Shape of the engagement:** the statutes mandate **human oversight and prohibitions**, not adoption — DC's policy bans AI from grading, discipline, IEP decisions and teacher evaluation; Oklahoma and Maryland bar AI from high-stakes student decisions. 🟢 **So the sellable artefact is a policy-conformant workflow with an audit trail and a human decision point, not an autonomous grader.** Alabama's graduation requirement (an approved CS course including AI instruction) and Florida's K-2→12 draft standards open a **curriculum** line of business alongside the platform one.

🟢 **Open-source starting points, all re-verified first-hand this pass:** `OpenOLAT` **Apache-2.0** (closed-IP safe) or `JupyterHub` **BSD** for the delivery platform; `CAHLR/OATutor` **MIT** (1 105 B, UC Berkeley CAHL lab) where a transparent, auditable mastery model is the requirement — **BKT is explainable to a school board in a way an LLM is not**, which is exactly what the oversight statutes ask for.

### EMEA

🔴 **Do not sell the August 2026 cliff. It is the wrong date and this base has already corrected it** (`intel/trends.md` T-336.1): high-risk obligations for education — **admissions, assessment, proctoring, AI-detection in assessment, and path-steering personalisation** — apply from **2027-12-02** (Digital Omnibus postponement, approved June 2026), and high-risk AI embedded in regulated products from **2028-08-02**. 🟢 **Corroborated independently this pass:** the Commission's own framing is that **from 2026-08-02 the AI Office and national authorities began enforcing the Act** — which is the *enforcement machinery* and the **transparency** duties (disclose AI; disclose synthetic content), **not** the Annex III education deadline. **Both facts are true and they are different facts**; conflating them overstates urgency to a buyer with ~14 months of runway while hiding the duties that bind today.

🟡 **Demand-side figures, held with their provenance:** one aggregator puts the European AI-in-education market at **$2.64B in 2026** growing **31.9% CAGR to $8.0B by 2030**, and names Finland, Estonia and the Netherlands as K-12 leaders — **aggregator-sourced, verify against Eurostat/OECD before any deck.** Denmark's national AI strategy carries **€200M** for R&D including education. **73% of UK adults report no AI education or training at all** — a workforce-reskilling opening distinct from the K-12 and HE ones. Policy anchors: **Digital Education Action Plan 2021-2027**, and the **AI Continent Action Plan**, which names education among its uptake sectors.

🟢 **Starting points:** `OpenOLAT` **Apache-2.0** is a European-origin, university-grade LMS with assessment and competence management — **the single best fit in this tier for an EU client needing closed IP plus AI Act documentation**. Add `h5p-cli` **MIT** (Norway, H5P Group) for interactive content and `hyperbook` **MIT** (Germany, OpenPatch) for courseware, both already carried with first-hand grants.

### APAC

🟢 **The region is the mandate leader, and it is fragmented by design — there is no single regulatory model to build one compliance product against.** Three distinct postures: **binding horizontal law** (South Korea's **AI Basic Act** and **Vietnam's Law on AI**, both in force early 2026), **promotion without penalties** (Japan), and **voluntary guidance that functions as de-facto requirement** (Singapore, India, Australia). China has **no general AI law** but binding rules per service type, with **AI-generated-content labelling applicable since 2025-09-01**.

🔵 **Curriculum mandates are the demand driver, not procurement cycles.** India: **AI and computational thinking mandatory from Class 3 in 2026-27**, backed by the IndiaAI Mission with a teacher-training push — 🟡 single-source, worth primary confirmation. China: AI reported **compulsory from age six since September 2025** — 🟡 **not confirmed against an official Chinese source; do not put it in a client deck unverified.** Singapore pilots through a government-funded research centre **with the Ministry of Education before classroom release** — the most implementation-mature pipeline in the region.

🟡 **Attitudes, which cut against a ban-driven narrative:** Ipsos (May 2026) finds support for banning AI in schools at only **23% (Indonesia) to 31% (South Korea)**, with India **26%**, Thailand **25%**, Singapore **28%**, Japan and Malaysia **29%**. Diffusion: Singapore **60.9%** of working-age adults (second globally behind the UAE), reported as **64.3%** on Microsoft's June 2026 data — **two figures, two sources, recorded as a spread rather than averaged.** China exceeds **700M** generative-AI users (CNNIC).

🟢 **Starting points:** `panaversity/learn-agentic-ai` **MIT** (1 068 B) is the region's own agentic curriculum asset at scale; pair with `microsoft/ai-agents-for-beginners` **MIT** (1 141 B) for teacher upskilling. For multi-jurisdiction delivery, the policy variation is best handled as **configuration at the orchestration layer**, not as forked products.

### LATAM

🟢 **The strongest demand-side evidence on this shelf, and the gap is governance — which is a sellable artefact.** UNESCO IESALC surveyed **200 higher-education institutions across 19 countries**: **87% use AI in at least one area** and **74% in teaching and learning**, while **only 26% have a formal AI strategy**. 🔴 **That 61-point spread between use and governance IS the engagement.** Adoption is uneven by sector — **84%** private non-profit, **68%** public, **52%** private for-profit — and is driven by individual academics and students rather than institutional strategy, which means **shadow AI is the default state** and an inventory-plus-policy mandate is the entry point.

🟢 **K-12 is ahead of the OECD, not behind it:** OECD TALIS (2024) shows **56%** of secondary teachers in Brazil and **55%** in Chile had used AI in the previous year against an OECD average of **36%**; Uruguay reports **75%** of public-school teachers using these tools (Ceibal, 2026). 🔵 **Ceibal and the Brazil/Chile teacher base are the reference accounts** — this is a teacher-adoption-led market, so teacher-facing workflow and assessment support outsells student-facing tutoring.

🟡 **Institutional buyers and channels:** **UNESCO's Observatory on AI in Education for Latin America and the Caribbean**, launched **2026-04-14 in Santiago**, is the policy-guidance channel; UNESCO also runs AI ethics and regulation training for officials in Ecuador and Chile. The **Digital Education Council**'s *AI in Higher Education LATAM Survey 2026* (**30 000+** responses across **29** institutions) and **ILIA** (Índice Latinoamericano de IA) are the two comparative datasets a regional deck should cite. 🟡 **Several of these figures are secondary coverage of the same UNESCO report, so they are less independent than their count suggests** — cite the IESALC study once, not four times.

🟢 **Starting points:** `chamilo-lms` **GPL-3.0** has the deepest LATAM public-sector install base — integrate over web services, never in-tree, to keep the AI layer proprietary. `uis-mcp-server` **MIT** (Brazil, already carried, placed on two channels) is the region's own MCP-native SIS/LMS connector precedent.

🔵 **Region vocabulary check:** the five values on this shelf are **North America | EMEA | APAC | LATAM | Global**, closed. Countries appear in prose above; none of them appears in a `region` field.

## Pass 336 · 2026-10-20 — the four prescribed search legs returned no supply for a seventh pass, and the strongest demand-side intelligence of the quarter

🔴 **Seventh consecutive measurement: the four global search legs returned 0 new repository slugs.** Run verbatim this pass — `top open source AI agents education 2026 github MIT`, `github trending education AI 2026`, `open source platform education ERP CRM MIT Apache`, `AI education industry trends 2026`. The first two returned general agent round-ups with no education ranking at all; the third returned ERP vendor pages (GegoK12, OpenEduCat, Frappe Education, RosarioSIS) already on these shelves; the fourth returned vendor trend blogs. 🟢 **The `ACTION TJ` registry channel returned 733 slugs new to a 3 031-slug corpus, 15 of them education-domain, 8 promoted.** The split between the two channels is now a stable, reproducible property of this base, not a bad week.

🟢 **But the REGION legs are a different story, and this pass they carried the most substantive demand-side intelligence in several passes.** All four returned placeable material. Recorded per region below.

### 🔴 One correction that outranks everything else on this shelf

🔴 **The EU AI Act's high-risk obligations for education do NOT apply from 2 August 2026. They were postponed to 2 December 2027.** The European Parliament and Council approved the delay in June 2026 (the Digital Omnibus); high-risk AI embedded in regulated products moves to **2 August 2028**.

🔴 **This base's own `intel/trends.md` lineage has carried `2 agosto 2026` as the compliance cliff for education AI**, and the earlier `globant-kb` education shelf states it outright: *"2 agosto 2026: auditoría, explicabilidad, supervisión humana requeridos."* 🟢 **That date is now wrong by sixteen months, and the error is commercially expensive in BOTH directions** — it overstates urgency to an EMEA buyer who has until December 2027, and it understates what *is* already in force.

🟢 **What IS in force from 2 August 2026**, and therefore the only EMEA compliance work that is live today: **transparency duties** — people must be told when they are dealing with an AI system, and **deepfake / synthetic content must be disclosed**. The **AI-literacy duty** remains but is the lighter form: organisations must *support* literacy, not guarantee a level. 🟡 Several vendor pages still print the August 2026 high-risk date; check publication dates. 🔵 The December 2027 date should be confirmed against the Official Journal before it goes into a client deck.

## Opportunities by region — superseded, Pass 336 (kept for history; the canonical block is at the top of this file)

### North America

🟢 **The largest regional share of the AI-in-education market — 36 %.** Teacher-side adoption is already majority: **60 % of US K-12 teachers** used AI tools in the 2024-25 school year, **32 % at least weekly**.

🔴 **Regulation is state-level and fragmenting fast: 134 AI-in-education bills across 31 states** in the 2026 session, concentrated on student-data privacy, classroom-use restrictions and curriculum.

| instrument | jurisdiction | what it does |
|---|---|---|
| **AB 1159** | California | 🔴 bars using **student data to train AI models** |
| **SB 1227** | Idaho | requires privacy protections for AI tools in schools |
| state statutes | Oklahoma, Maryland | 🔴 require **human oversight**; bar AI from high-stakes decisions about students |
| **H.R. 8747** — K-12 AI Literacy and Readiness Act of 2026 | US federal | advanced out of the House Education and Workforce Committee **2026-07-21**; would let schools spend federal funds on AI literacy. 🟡 Advanced, not enacted, and largely along party lines |
| National AI Strategy | 🟢 **Canada**, launched **2026-06-04** | national AI-literacy push, watermarking of AI-generated content, a **Canada Trusted AI Certification** programme. 🟡 A strategy, not a statute |
| one-year moratorium | New York City | 🔴 **no student-facing AI through eighth grade** |
| K-12 implementation guidance | North Carolina DPI | detailed district-level guidance |

🟢 **The opportunity: compliance-shaped delivery, not model work.** Fifty jurisdictions with divergent rules means the buyable artefact is a **policy-enforcement layer** — per-state configuration of what may be processed, logged and automated, with human-in-the-loop where Oklahoma and Maryland require it. 🔵 The row for this is already on these shelves: `Principled-Evolution/gopal`, Rego policies covering EU AI Act, GDPR, NIST AI RMF **and FERPA**.
🟡 **The counter-signal to price in:** NYC's through-eighth-grade moratorium and the University of Chicago Law School's device-free 1L pilot (from autumn 2026) say the K-8 and assessment-integrity segments are *narrowing*, not opening. Sell teacher-side and administrative automation there, not student-facing tutors.

### EMEA

🟢 **Sixteen extra months of runway, and a governance market that is already buying.** With high-risk duties at **2026-12-02 → 2027-12-02**, the EMEA engagement in the next four quarters is **readiness**, not remediation — and the institutions are building the apparatus now rather than waiting.

🟢 **The reference implementation to cite is Utrecht University**: AI systems classified **by EU AI Act risk level**, an **AI Veritas** system that pre-approves tools before use, and **Certified AI Compliance Officers appointed across faculties**. Edinburgh is cited in the same report as a governance model. 🔵 That is a replicable three-part pattern — a risk register, a tool-approval gate, named accountable officers per faculty — and it is a deliverable, not a philosophy.

🟢 **Policy direction is explicit and recent**: the European Commission's updated **ethical AI guidelines for education (May 2026)** and the **EU Council conclusions of 11 May 2026** on a human-centred approach to AI in education both push human oversight.

🟡 **What EMEA is actually deploying is administration and teacher support, not grading.** Parent-communication chatbots are treated as low-risk routine tools; **auto-grading summative exams without teacher review is advised against** under current guidance. 🔴 Sell the administrative layer and the teacher-facing layer; do not sell autonomous summative assessment into EMEA before December 2027.

🟢 **The supply side here is unusually strong this pass, and it is European-built**: `openpatch/hyperbook` (Germany), `h5p/h5p-cli` (Norway), `otacke/h5p-theme-picker` (Germany), `missing-elements/h5p-offline-player`, `zensation-ai/zenbrain`, `falkenslab/moodle-driver`, plus `FenixEdu` (Portugal) and `celtic-project/LTI-PHP` (UK) recovered as LGPL-3.0. 🟢 **Six of the seven rows promoted this pass are EMEA** — an EMEA engagement can now be staffed almost entirely from components whose maintainers sit in the same time zones as the client.

### APAC

🔴 **The most binding education-specific AI rules in the world are here, and they are not uniform.**

| jurisdiction | instrument | status | what it means for an engagement |
|---|---|---|---|
| 🔴 **Vietnam** | July 2026 decision naming **education** — specifically **automated assessment and behavioural monitoring** — a high-risk area | compliance by **2027-03-01**; systems already operating before **2026-08-15** get a further **six-month grace** | 🟢 The sharpest education-specific rule in APAC. 🔵 Crucially, many listed systems are high-risk **only where AI output is the sole basis for a decision without meaningful human review** — so a human-in-the-loop design exits the high-risk class by construction |
| 🟡 **South Korea** | **AI Framework Act**, in force **2026-01-22** | MSIT running 2026 as a de facto pilot; **one-year grace on penalties** | Build now, under the Act, while enforcement is soft |
| 🔴 **China** | full-lifecycle binding requirements; and the **《"人工智能+教育"行动计划》 AI+Education Action Plan** (MOE + four agencies, **2026-04-10**) — a five-year plan to 2030 with a **partly central-budget-funded national AI-education pilot base** | in force | 🟡 Demand is state-driven and the compliance surface is the heaviest anywhere |
| 🟢 **India** | **CT & AI** curriculum (MoE / CBSE, Classes **3–8**), launched 2026-04-01, **mandatory from the 2026-27 session**; plus platform-level labelling of AI-generated audio/image/video | in force | 🟢 A **mandatory national curriculum** with a free teacher handbook — teacher-enablement and content-localisation at national scale |
| 🟡 **Japan** | **MEXT** generative-AI guideline **Ver. 2.0**; AI Promotion Act is a principles law with **no penalties** | pilot figures dated 2026-04-30: **149 municipalities / 478 schools** | 🟢 Permissive, and the stated principle — *the final judgement and the responsibility are human* — is a design brief |
| 🟡 **Singapore** | agentic-AI framework | best-practice guidance, not law | Light-touch |

🟢 **The opportunity: the same product, gated by jurisdiction.** Vietnam's "sole basis without meaningful human review" carve-out, Japan's human-responsibility principle and Oklahoma/Maryland's human-oversight statutes all point at **one** architecture — a reviewable decision boundary with an auditable human step — which is sellable in five jurisdictions from one build. 🟡 Named commercial incumbents in APAC AI-education are Google, Microsoft, IBM, Pearson and Byju's, per a market report whose rankings should be treated with caution.

### LATAM

🟢 **The demand side is now measured, and the number that matters is the gap between use and governance.** The **UNESCO IESALC / UNU-IAS** study — **200 institutions across 19 countries**, launched at Digital Learning Week 2026, UNESCO Paris — found **87 % of institutions use AI somewhere, and only 26 % have a formal AI strategy.** Adoption is **bottom-up**, driven by individual academics, researchers and students rather than institutional programmes. A separate **Digital Education Council** survey covers **30 000+ responses across 29 LATAM higher-education institutions**.

🟢 **That 87 / 26 split is the single most actionable figure on this shelf.** It is not an adoption problem and it is not a technology problem — it is a **governance and consolidation** problem, and it is exactly the engagement LATAM institutions can be sold: take the shadow AI that 87 % already run and give it a strategy, a data boundary, a procurement path and an audit trail. 🔵 Sixty-one points of institutions are using AI with no mandate covering it.

🟢 **The regional institutional anchor is new and well-funded**: the **UNESCO Observatory on AI in Education for Latin America and the Caribbean**, launched **2026-04-14 in Santiago**, with **CAF, CENIA (Chile), CETIC.br (Brazil), ECLAC, Fundación Santillana, Tecnológico de Monterrey, ProFuturo, Fundación Ceibal (Uruguay) and IRCAI** as partners. 🔵 That partner list is a ready-made route to ministries in Chile, Brazil, Mexico and Uruguay.

| jurisdiction | instrument | status |
|---|---|---|
| 🟢 **Uruguay** | first LATAM signatory of the **Council of Europe Framework Convention on AI and Human Rights, Democracy and the Rule of Law** (2025) | signed |
| 🟢 **Peru** | risk-based classification + **regulatory sandboxes**, tied to INDECOPI and the data-protection authority | adopted |
| 🟡 **Colombia** | policy-first: **CONPES 4144** national AI policy (Feb 2025) | policy, not statute |
| 🟡 **Mexico** | federal AI bill (2024) with an oversight authority | 🔴 bills without an enforcing regulator yet |
| 🟡 **Brazil, Chile** | AI bill / framework | moving at different speeds |

🟢 **And the LATAM SUPPLY side is confirmed, for a second pass and by a second independent instrument.** p335 placed `Cvmcosta/ltijs` (Apache-2.0, the canonical Node LTI 1.3 library) in **Brazil** off its commit channel. This pass placed **`SidneyBissoli/uis-mcp-server`** (MIT, 100 c, `-0300` on 100 of 100, sole human author **Sidney da Silva Pereira Bissoli**) in **Brazil** — a UNESCO-statistics MCP server listed in the official MCP Registry. 🟢 **Two unrelated maintainers, two different layers, same region, both found on the registry channel.** The five passes that recorded *"the LATAM supply side returned nothing placeable"* were measuring the search engine, not the region. 🟡 The bound p335 stated still holds for both rows: this places **maintainers**, not purchasing.
🔴 **The honest gap, stated so silence is not read as coverage:** this pass found **no LATAM-built AI *tutor* or *assessment* agent** — the two Brazilian rows are both **infrastructure** (LTI integration, statistics access). The region is producing the layer an engagement is built *on*, not the pedagogy on top of it. That gap has now been measured twice on two different channels and is a real feature of the supply, not a search failure.

**Pass 335 · 2026-10-20 (eighth pass of this date).** 🟢 **The LATAM supply gap this file has declared for five consecutive passes is CLOSED, and it closed on a row this base already recommended:** `Cvmcosta/ltijs`, the canonical LTI 1.3 Node library, on the build tier since p331, is **Brazilian** — root commit `cvmcosta@yahoo.com.br` 2019-05-30, `yahoo.com.br` on **429 of 575** commits, `-0300` on **513 of 575** ([`evidence/p335-ltijs-latam-placement`](../evidence/p335-ltijs-latam-placement.2026-10-20-p335.tsv)). 🔴 **The gap was an artefact of asking only the discovery channel; the placement instrument was never run over the inventory.** 🟡 **Every policy row in this file remains search-channel-attributed and none is read first-hand: `moe.gov.cn`, `mext.go.jp`, `eur-lex.europa.eu` are all `000` — no connect — from this environment, re-tested this pass. The repository rows ARE first-hand; the policy tier is still the least-verified tier here.**

### 🔵 EU AI Act — corroborated a fifth time, zero new fact

The EMEA leg returned the **Annex III** education deferral to **2027-12-02** via **Regulation (EU) 2026/1744** once more. 🟢 **This file has held it since p328 with better precision than the channel serves it** — including the `2028-08-02` embedded-product date, the unmoved **Art. 50** transparency duty, the **Art. 4** literacy duty live since 2025-02-02, and the **Art. 5(1)(f)** emotion-inference prohibition that is not a high-risk duty at all. 🔴 **Two sources in this sweep still print the superseded `2026-08-02` high-risk date.** 🟢 **No change. Recorded as corroboration so the next pass does not re-litigate it.**

## Opportunities by region — superseded, Pass 336 (kept for history; the canonical block is at the top of this file)

### North America

🟢 **Supply is deep and newly measurable.** `@brightspace-ui/core` — **Apache-2.0, 9,598 commits, 180 authors, 1,020 commits in 2026, `d2l.com` on 2,748** — is the deepest bench on these shelves and belongs to a **proprietary** LMS vendor. `chrischall/gogcli-mcp` (MIT, 498 c all in 2026) puts Google Classroom behind MCP. `harvard-edtech/caccl` (MIT, © Harvard University) is an eight-year Canvas+LTI scaffold.

🟢 **The opportunity:** a **D2L or Canvas front-end engagement can be built almost entirely on permissive, vendor-maintained components** — which compresses the build and removes the licence conversation from the contract. 🔴 **The constraint is institutional, not technical:** the search channel reports **only ~10% of institutions hold formal AI guidelines** and **71% of US teachers lack AI training** (vendor roundup, provenance unclear, **not carried as data**). 🔵 **Read commercially: the governance deliverable sells before the model deliverable.**

🟡 **Market figures, directional only, from the search channel:** North America ≈ **$951M (2024) → $2.3B (2029), CAGR 15.9%** (MarketsandMarkets), ~**36%** of global share. **Methodologies differ by a factor of two across firms; not reconciled.**

### EMEA

🟢 **Two placed supply rows added this pass** — `christophblessing/quiz-recap` (MIT, **Germany**, `hpi.de`, npm scope `@openhpi` = Hasso-Plattner-Institut Potsdam) and `studiolxd/xapi` (**EMEA** by offset, but ungranted and single-author). 🔵 Together with p334's `CogitoNTNU/TutorAI` (Norway) and `r-huijts/canvas-mcp` (Netherlands), **the EMEA supply side is now seven placed permissive rows** and is no longer regulation-only.

🟢 **The commercial shape is unchanged and now well-evidenced:** a **~14-month build window** before Annex III bites on 2027-12-02, with **two deliverables sellable this quarter** — an **Art. 50 transparency review** and an **Art. 4 staff-literacy programme**, neither of which moved. 🔵 **Lead with the near dates; a client who hears only "2027" will under-scope the live prohibitions.** Sovereignty is argued on **architecture**, citing Council conclusions **9003/26** (p334), because **no education-specific data-residency rule exists.**

🔴 **The gap that survives, sixth consecutive pass: zero named EMEA vendors, zero national adoption statistics for the UK, Germany or France.** The EMEA competitive map here is still regulation plus supply-side repositories, with no demand-side map.

### APAC

🟢 **New this pass, and it is a first: the APAC SUPPLY side is placed.** Every prior APAC row in this file was a policy instrument. Three producing repositories now carry a commit-channel placement — **Japan** (`likr/canvas-lms-agent`, `likr-lab.com`, `+0900`), **India** (`scormflow/scorm-engine-client`, MIT, `+0530`, 45 commits all in 2026), **Vietnam** (`DamPhuQuy/Agent-as-a-tutor`, MIT, `+0700`). 🟡 **Two of the three are below this base's bench bar and one is ungranted** — recorded as placement evidence, not as recommendations.

🟢 **Policy, carried and corroborated:** Japan's **MEXT** GenAI guideline **Ver. 2.0** with the FY2026 pilot at **149 municipalities / 478 schools** (*under 2% of schools nationwide* — the figure that keeps the pilot in proportion); **Korea's AI Basic Act** in force **2026-01-22** with education inside its high-impact class; **Vietnam's Decision 33/2026/QĐ-TTg** (46 high-risk systems, 6 sectors, effective **2026-08-15**), whose entry 2 reaches automated assessment **only where the AI output is the sole basis for the decision without meaningful human review**.

🟢 **The architectural lever, and it is one design across four jurisdictions:** a **human-in-the-loop grading design keeps the product out of the high-risk class entirely** — Vietnam's entry 2, the EU's Art. 14, and the Oklahoma and Maryland human-oversight rules all reward the same shape. 🔵 **Build it once; sell it in four places.**

🔴 **Gap: China's 《"人工智能+教育"行动计划》 and MEXT's own text remain unread first-hand** — both hosts answer `000` from this environment, as they did at p334.

### LATAM

🟢 **The supply gap is closed, and the answer is a production dependency rather than a demo.** `Cvmcosta/ltijs` — **Apache-2.0, 575 commits, 17 authors, 51 in 2026** — is the LTI 1.3 library a large share of the world's LMS integrations run on, and it is maintained from Brazil with a commercial sponsor behind it (`ltiaas.com`, 90 commits). 🔵 **A LATAM engagement can be pitched on regional authorship of the integration layer itself**, which is a stronger position than regional adoption statistics.

🟡 **The bound, stated plainly: this places a maintainer, not a market.** It says the region produces the seam; it does not say LATAM institutions are buying.

🔴 **The DISCOVERY channel is still empty for LATAM — sixth consecutive measurement.** A targeted sweep (`plataforma educativa código abierto IA`, Brazil/Chile/Argentina, 2026) returned **zero open-source AI education repositories**. 🟢 **Two new citable non-repository facts, search-channel only:** **HolonIQ's 2026 Latin America EdTech 100** (Brazil's **Teachy**, AI lesson preparation, has expanded beyond the region into Asia; Argentina's **Cboard**, accessibility) and **Google.org with the Raspberry Pi Foundation committing $4.6M** to extend *Experience AI* across **Argentina, Brazil and Chile** among others. **Both are commercial or philanthropic, neither is an open-source platform.**

🟢 **Demand-side, carried from p333 and still the strongest LATAM datum this file holds:** **UNESCO IESALC across 200 institutions in 19 countries — 87% use AI in at least one area, 26% have any formal framework**, teaching and learning leading at **73.5%**, research **57.0%**, administration **34.1%**. 🔵 **A 61-point gap between use and governance is the engagement.** The Digital Education Council's **LATAM 2026** survey (**92% of students, 79% of faculty** actively engaging) points the same way from the other side.

### Global

🔴 **The prescribed global search legs returned nothing new for the sixth consecutive pass.** Market sizing remains irreconcilable across firms — 2025 estimates spread **$6.4B–$8.3B**, CAGRs **25.9%–42.8%** — and this file continues to carry the spread rather than pick a number.

---


**Pass 334 · 2026-10-20 (seventh pass of this date).** 🟢 **The APAC leg finally returned, and it returned because the query was run per country instead of per region — the instruction `compose/patterns.md` has carried since p330.** 🔴 **p333 declared the opposite ("the English-language secondary channel does not carry APAC education policy at all") and the `gate-absence` hook refuted it on p333's own shelves.** 🟡 **Every policy row below is ATTRIBUTED to the search channel and none was read first-hand: `moe.gov.cn`, `mext.go.jp`, `consilium.europa.eu` and `cset.georgetown.edu` are all `000` — no connect — from this environment ([`evidence/p334-channel-reachability`](../evidence/p334-channel-reachability.2026-10-20-p334.tsv)).**

## 🟢 The four national instruments the per-country query found — three of them APAC

| jurisdiction | instrument | date | the operative content |
|---|---|---|---|
| 🟢 **APAC — China** | 《"人工智能+教育"行动计划》 **AI+Education Action Plan** — MOE **plus four other agencies** | **2026-04-10** | Five-year plan to **2030**: K-12, universities, vocational, lifelong learning. A **national AI (education) application pilot base**, partly **central-budget** funded. 🟡 Provincial/municipal bureaus **expected** to issue implementing rules and begin buying **2026–2027** — expectation, not a published schedule |
| 🟢 **APAC — India** | **CT & AI** (Computational Thinking & Artificial Intelligence), MoE / **CBSE**, Classes **3–8** | announced late **2025**; launched **2026-04-01**; mandatory from the **2026-27** session | Curriculum framework + **teacher handbook** + learning material, **free on the CBSE site**. Committee chaired by **Prof. Karthik Raman, IIT Madras**; aligned to **NEP 2020**. **Internal assessment, no separate exam** for 3–8. 🟡 Classes 9–12 timelines are reported inconsistently (2027-28 modules; board subject 2029) — unresolved |
| 🟢 **APAC — Japan** | **MEXT** *Guideline for the Use of Generative AI in Elementary and Secondary Education* **Ver. 2.0** | Ver. 2.0 **Dec 2024**; pilot scale in a MEXT document dated **2026-04-30** | **149 municipalities / 478 schools**, split **10 classroom use · 100 teacher administrative use · 51 courseware trial**. Core principle: **the final judgement and the responsibility remain human** |
| 🟢 **EMEA — EU** | **Council conclusions on teachers in the era of AI**, doc **9003/26**, adopted at **EYCS** | **2026-05-11** (draft 8262/26, 2026-04-24, agreed by all delegations in the Education Committee) | Calls on member states to build teachers' AI skills and promote **education-specific** AI tools, with teachers involved in **designing and evaluating** them ("digital humanism"). 🟢 **Names digital sovereignty and strategic autonomy as essential, and says reducing dependence on AI tools developed outside Europe, including in education, is critical** |

### 🟢 p333's declared EMEA sovereignty gap — now answered, and the answer is that the thing it looked for does not exist

🔴 **p333 declared:** *"The EMEA sovereignty leg returned NOTHING when queried explicitly for data residency and non-EU vendor procurement in education. Declared as an informed gap — this KB cannot place European data-residency requirements for education AI."*

🟢 **Measured this pass: there is no education-specific data-residency rule to find.** The sovereignty lever in European education AI is **political and horizontal**, in two pieces:

1. 🟢 **Education-specific but non-binding** — Council conclusions **9003/26** (above). Conclusions are a political instrument: they direct member states and the Commission, they do not bind a vendor.
2. 🟢 **Binding-shaped but horizontal** — the Commission's **tech-sovereignty package**, which sets criteria against which **cloud and AI services demonstrate a level of sovereignty**, explicitly including **infrastructure location, software supply-chain control and cyber security**. 🔴 **It is general public-sector policy; the sources do not place edtech inside its scope.**

🔵 **For an engagement this is a better answer than a rule would have been:** there is nothing to certify against, so **sovereignty in an EMEA education bid is won on architecture, not on paperwork** — self-hostable models, EU-located inference, and a named supply chain. 🟢 That is exactly what pattern **P24** (sovereign stack) already builds, and the Council text is now the thing to cite in the bid.

## 🟢 Opportunities by region

🔵 **Scope stated: these are read off the instruments and figures in this file, and every policy citation is search-channel attested, not read first-hand.**

### North America

🟢 **The buying signal is teacher-facing and oversight-shaped, and the connector tier is already permissive and American.** State policy keeps converging on human-in-the-loop rather than prohibition: **Idaho SB 1227 enacted** (statewide K-12 framework, data-privacy rules, AI may not replace teachers); **Oklahoma and Maryland** require human oversight and bar AI from high-stakes decisions about students; **California AB 1159** (proposed) would forbid training models on student data absent direct school benefit. **~40 states plus Puerto Rico** have official guidance — a single-directory figure, worth re-checking. Federal: **H.R. 8747**, the K-12 AI Literacy and Readiness Act of 2026, **advanced out of committee and is not enacted**; there are **no binding federal AI curriculum standards**.

🟢 **The concrete opening:** the two widest-bench permissive MCP connectors measured this pass are both North American — **`vishalsachdev/canvas-mcp`** (MIT, 1,041 c · 30 a · 927 in 2026) and **`rohanmuppa/brightspace-mcp-server`** (MIT, 414 c · 17 a, head today). **Both point at the LMSs US districts and universities actually run.** Sell **pattern P26**: graded assessment with the approval hop in the protocol, which answers Oklahoma, Maryland and AB 1159 in one design.

### EMEA

🟢 **Two dates, and they are the whole shape of an EMEA engagement.** **2026-08-02**: the AI Act is generally applicable and **Article 50 transparency duties apply now** — a learner must be told they are talking to an AI. **2027-12-02**: Annex III point 3 high-risk obligations for stand-alone education systems, **postponed from 2026-08-02 by Regulation (EU) 2026/1744**. 🔴 **Not postponed and not a high-risk duty at all: Article 5(1)(f) prohibits AI that infers emotions in education institutions outright**, except for medical or safety purposes.

🟢 **The opening is the 18-month window plus sovereignty.** Annex III covers systems determining **access or admission**, assigning learners to institutions, and **evaluating learning outcomes where the outcome steers the learning**. Build inside the window so the human-oversight control (Art. 14) is already the architecture, and cite **9003/26** for the sovereignty half. 🟢 **The EMEA supply side is real and measurable:** `CogitoNTNU/TutorAI` (MIT, Norway, `stud.ntnu.no`), `r-huijts/canvas-mcp` (MIT, `fontys.nl`), `ankimcp/anki-mcp-server`, `falkenslab/moodle-mcp`, `felipedias-ie/blackboard-mcp`, `kaveheng/GenAi-in-education` (CC BY 4.0) — **six EMEA-placed permissive rows, all placed on the commit channel.**

### APAC

🟢 **This is now the best-documented region on this shelf, and it is three separate markets, not one.** **China**: a funded five-year national plan dated 2026-04-10, bought at **provincial and municipal bureau** level — target a province, not a ministry. **India**: a **mandated** curriculum for Classes 3–8 from the 2026-27 session, with the framework, teacher handbook and materials **already published free** — so the gap is not content, it is **teacher capability and delivery at scale**. **Japan**: a pilot measured at **478 schools** with a human-responsibility principle written into the guideline, and a 2030 AI-literacy target in draft. **Korea**: the **AI Basic Act in force 2026-01-22**, education inside its **high-impact** class with human-oversight duties. 🟡 **Singapore returned only a broad Smart Nation goal to train teachers at all levels on AI in education by 2026 — no MOE curriculum document surfaced; declared as a partial.**

🟢 **The concrete opening:** India's mandate is a **teacher-enablement** engagement, not a content engagement — and `Haozhe-Xing/agent_learning` (MIT, APAC-placed, 11 authors in 2026) ships a curriculum **and** an eval harness that a training programme can be measured against. For Japan and Korea, lead with **P26**'s approval hop, which both jurisdictions' human-oversight duties ask for in almost the same words.

### LATAM

🟢 **The money here is multilateral and philanthropic, and it is already committed.** **UNESCO** launched a regional **AI-in-education observatory** for Latin America and the Caribbean in **April 2026**, with a pilot in **Mexico** with **CONALEP and DGETI** on centres of excellence. **Google.org** committed **$4.6M** across **nine countries** including Brazil and Mexico, targeting **1.25M students by 2028**. The **IDB**'s review of **193** initiatives found **59% use generative AI**. **HolonIQ's 2026 Latin America EdTech 100** reports AI-native positioning rising sharply and concentrated in **teacher-facing** tools rather than consumer tutoring, with **Brazil at the centre**. Market research puts regional edtech growth at **~11.8% a year, 2026–2034** — an estimate, not a measurement.

🔴 **Regulation is the gap, stated as one.** **Brazil's LGPD** gives a right to review decisions made solely by automated processing — directly relevant to automated grading — and **Mexico** has its private-sector data law; **both countries' comprehensive AI bills are proposals whose enacted status this pass could not confirm.** 🟡 **And the supply side stayed empty for the fourth consecutive measurement: a repository-level search for LATAM-origin education AI projects (Brazil, Mexico, Argentina, universities, government) returned no placeable repository.** 🔵 **One near-miss, recorded honestly rather than claimed:** `affromero/Sotto` carries **1,243 commits at `-0500`** and a `.co` domain beside **2,571 at `+0100`** — **a two-offset footprint this pass refused to place**, and it is **AGPL-3.0** in any case.

🟢 **The concrete opening:** sell into the **committed** money, not the projected market. The IDB's 59%-generative figure and the UNESCO observatory mean the region's buyers are mid-pilot and need **evaluation and teacher-facing delivery**, which is where `learning-commons-org/evaluators` and **P26** fit — with LGPD Article 20 review as the design constraint rather than an afterthought.

---

**Pass 332 · 2026-10-20 (fifth pass of this date).** 🔴 **The regional sweep was run as prescribed — four global legs and one per region — and it returned ZERO net-new artefacts. That is this pass's market finding, and it is recorded as a measured gap rather than left as silence.**

🔵 **The honest yield, leg by leg, so the next pass does not re-spend it:**

| leg | yield | status |
|---|---|---|
| `AI education industry trends 2026` | Market forecasts only, from three houses that **do not agree** | 🟡 carried below, with the spread stated |
| `AI education North America 2026 adoption regulation players` | Market-report summaries + one newsletter digest | 🟡 **state-level items unverified at source — flagged, not promoted** |
| `AI education EMEA 2026 adoption regulation players` | One primary EU document (EESC policy note, March 2026) | 🟢 **the single new citation this pass** |
| `AI education APAC 2026 adoption regulation players` | Enterprise-AI coverage, **nothing on K-12 or HE policy** | 🔴 **explicit gap — see below** |
| `AI education LATAM 2026 adoption regulation players` | IESALC/UNU working paper, ILIA 2025 | 🔴 **both already held: IESALC in 8 shelf files / 79 evidence files; ILIA in 10 / 102** |

🔴 **The market-size spread is the finding, not any one number.** Three houses, three answers for the same year: **IMARC ~$6.4B (2025) → $79.6B (2034)**; **Grand View–linked $8.3B (2025), $11.4B (2026) → $57.2B (2033)**; **The Business Research Company $7.52B (2025) → $10.6B (2026)**. 🟡 **A 78% spread between the lowest and highest 2026 figure means the methodologies disagree about what counts as "AI in education," and all three are vendor research.** 🟢 **Use the direction, never the number: quote a range with the houses named, or quote nothing.** A single figure in a client deck invites exactly the question it cannot survive.

🟡 **One adoption datum worth carrying with its caveat attached:** student AI use reported as **66% (2024) → 92% (2025)**. The population is not specified in any source that repeats it. 🔴 **Do not put it in a deck without the primary citation**; it is the most-repeated and least-sourced number in this sector.

## Opportunities by region — superseded, Pass 336 (kept for history; the canonical block is at the top of this file)

### North America

🟢 **The seam: a fragmented state-level rulebook is a compliance-engineering market.** There is no federal framework; governance is state-by-state, and reported items this pass include **Maryland and Oklahoma** restricting AI from high-stakes decisions without human oversight, **Colorado and Texas** piecemeal requirements, and **Boston** making AI fluency a graduation requirement from **September 2026**. 🔴 **Flagged, not promoted: these came from a single newsletter digest and were NOT verified at the primary source this pass.** Verify before any one of them appears in a proposal.

🟢 **What is solid and what to build:** the human-approval hop is the recurring requirement across every version of these rules, and this KB already has the pattern for it — **`P26` in `compose/patterns.md`**, whose compliance argument holds in four jurisdictions. 🟢 **Ed-Fi is the North American data standard and its open surface is dormant:** `esegrave/edfi` (Apache-2.0, head 2022-03-04) and `xmarcosx/edfi-via-kubernetes` are both stale, measured p332. **A current, permissive Ed-Fi integration is an unoccupied position** — the standard is live, the open tooling is not.

### EMEA

🟢 **The one new primary citation this pass: the EESC AI policy note, March 2026**, carrying Eurostat 2025 enterprise AI adoption — **~5% (Romania) to ~42% (Denmark)** — and, for enterprises that considered AI and did not adopt, the barriers in their own ranking: **lack of expertise 70.89%, uncertainty about legal consequences 52.52%, data-protection concerns 48.83%**.

🔵 **Read those three numbers together and the EMEA engagement shape follows from them.** 🟢 **The top barrier is skills, not law** — 70.89% against 52.52% — which means the sellable unit is capability transfer, not a platform licence. 🟢 **And the 37-point adoption spread inside one regulatory bloc kills the single-EMEA-motion assumption:** Denmark and Romania are the same rulebook and different engagements.

🟢 **The build:** the EU AI Act's Annex III pt 3 puts education in the high-risk tier, and `P26` is already written against it (Art. 14 human oversight, 2027-12-02). 🟡 **Procurement datum from p332:** `zanichellieditore/learningrecordstore-xapi` — **MIT, © 2019 Zanichelli Editore s.p.a., dead since 2020-03-18**. A major Italian education publisher open-sourced its LRS and stopped. **The code is stale; the precedent is a conversation.**

### APAC

🔴 **DECLARED GAP, and it is the honest result rather than an omission: the APAC leg returned NOTHING on K-12 or higher-education AI policy.** What came back was enterprise-AI coverage — Singapore's financial-institution consultations, Australia tightening AI governance and copyright, Forrester expecting data sovereignty to drive infrastructure choice for ~half of APAC firms, and **49% of APAC businesses citing insufficient real-time data infrastructure** (Omdia, 5 markets, 1,100+ decision-makers). 🔴 **None of that is education policy.** Education surfaced only as vendor activity: **TCS + Pearson**'s multi-year AI learning alliance on employer skills gaps, **LearnUpon**'s Sydney HQ and AI course authoring, **Alteryx Academy**'s relaunch.

🟢 **What this base already holds that the leg did not return, and which is the better ground:** **Korea's AI Basic Act (in force January 2026)**, **Vietnam's Decision 33/2026/QĐ-TTg (effective 2026-08-15)** — both already cited in `intel/trends.md` and `P26` — and **China's content-labeling rules (September 2025)**. 🔵 **So the gap is in the CHANNEL, not the jurisdiction.** The next APAC leg should query the instruments by name rather than the region by topic; the topic query returns enterprise press.

🟢 **The build:** sovereignty-constrained deployment. If half the region's firms let data residency drive infrastructure, the education stack has to be self-hostable — which points at **Kolibri (MIT)** and local inference, not a hosted tutor. 🟡 **`sagorbrur/bnlp` (MIT, 541 c · 10 a · head 2026-04-01, measured p332)** is live low-resource-language groundwork for Bengali — relevant to any South Asian engagement where the content language is not English.

### LATAM

🟢 **The region remains the best-documented on these shelves, and this pass added nothing — because everything the leg returned was already held.** **IESALC/UNU** (200 institutions, 19 countries, fielded August–October 2025) is in **8 shelf files and 79 evidence files**; **ILIA 2025** in **10 and 102**. 🔵 **Recording that as a nil result is the point: the LATAM channel is saturated, which is a statement about this KB's coverage and not about the region.**

🟢 **Standing position, unchanged and still the strongest in this file:** **Kolibri (MIT, offline-first)** is the base for low-connectivity deployment; **RosarioSIS (GPL-2.0)** has the Spanish/French SIS surface with its redistribution constraint stated; **Latam-GPT** (CENIA, 60+ institutions, 15 countries) is the regional model story. **Brazil's Marco Legal da IA**, **Chile**, **Uruguay** — the only LATAM entries in the global top 50 on the ILIA governance axis — and **Mexico with no AI law** are the four-way split any regional proposal has to address separately.

🟡 **p332's LATAM datum is a negative, and it is useful:** `roncuevas/ipn_saes_utils` (MIT, © 2026) addresses the **IPN/SAES student-system seam in Mexico** and is **2 commits**. 🔵 **The seam is real and nobody has built it.** A permissive integration against Mexican public-university student systems is an open position, and the evidence it is wanted is that someone started one.

### Global

🔴 **Tenth consecutive pass with no permissive education LMS, SIS or ERP** (`verticals/solutions.md` p332). Moodle GPLv3, Open edX AGPLv3, Canvas AGPL-3.0, OpenEduCat LGPL-3.0. 🟢 **The permissive surface in this sector is the LAYERS — integration (`lti-tool`, MIT), content types (H5P content tier, MIT, p332), pedagogy (`OATutor`, MIT) — never the platform.** **Any proposal that assumes a permissive base platform is mispriced; one that puts permissive layers on a copyleft base deployed as-is is not.**

---

**Pass 331 · 2026-10-20 (fourth pass of this date).** 🟢 **One genuinely new regulatory instrument, one date correction to this file's own EU row, and a LATAM finding that answers the measurement complaint p330 closed with.** 🔴 **And one thing this pass did NOT find, said first because the silence would otherwise read as coverage: the North America news leg returned nothing this file does not already hold — for the fourth consecutive pass.**

🔵 **The regional sweep was run globally and once per region, as prescribed. Here is the honest yield, leg by leg:**

| leg | yield | status |
|---|---|---|
| **APAC** | 🟢 **The Vietnam two-instrument conflict open since p269 is CLOSED — Decree 142 and Decision 33 compose, and the "two dates" were one date and its grace period** | 🟢 **The instrument was already held (line 149). What is new: the reconciliation, the third education entry, the two conformity pathways, and 2027-09-01 confirmed directly** |
| **EMEA** | 🟡 **Reg. (EU) 2026/1744 — OJ publication 2026-07-24, entry into force 2026-07-27** | 🟡 **Refines a date this file carries as 2026-07-08. The 2027-12-02 deadline agrees on both readings** |
| **LATAM** | 🟢 **The most-deployed open LTI library in the world is maintained from Brazil — first-hand from the commit record** | 🟢 **NEW, and it is an artefact finding rather than a statistic** |
| **North America** | 🔴 **Nothing new.** 134 bills / 31 states, AB 1159, SB 1227, H.R. 8747, NYC K-8 moratorium, Canada "AI for All" — **all already held** | 🔴 **DECLARED GAP, and it is the fourth consecutive pass the NA leg has returned held material.** See the method note below |
| **Global** | 🟡 Reproduced the trend layer; the one artefact it surfaced (`os-taxonomy`) is held and its licence re-read identically | 🟡 Held |

🔴 **The NA leg's repeated nil return is now a statement about the query, not the region, and this file should stop paying for it in its current form.** `evidence/p271-websearch.2026-10-17-p271.tsv` recorded the same outcome three passes ago with the same query string, and named the one datum that was new then (**AFT National Academy for AI Instruction**, with Microsoft, OpenAI and Anthropic). 🟢 **The standing query `AI education North America 2026 adoption regulation players` has been saturated for four passes. p329 already proved the fix on this very file by deleting the word *players* and asking about the procurement vehicle instead.** **Apply the same surgery to the NA leg: ask about the named district or state contract, not the region.**

🟢 **What did move North America this pass came from the repository channel, not the news channel** — the dead-LTI risk line p330 wrote into the NA block now has a live, MIT, US-institution-backed answer. **It is under `### North America` below.**

---



# Market intelligence — education

**Pass 329 · 2026-10-20 (second pass of this date).** 🟢 **The gap this file declared for four consecutive passes is
closed: it can now place a ROUTE TO MARKET in every region, and it was closed by deleting one word from a query.**
🔴 **The four-pass finding was *"this file can place regulation by region and cannot place vendors by region"* (line 1447 below),
and p328 prescribed the fix: drop `players` and query the procurement surface instead.** 🔵 **The deeper reason it had failed is
that the vendor map was the WRONG OBJECT.** Four passes asked *who are the players in region X* and got market-research SEO and
law-firm explainers, because that is what the word *players* ranks. **A studio does not sell to a region; it sells THROUGH A VEHICLE** —
and unlike a vendor list, a procurement vehicle is nameable, dated, and has an eligibility rule you can read. 🟢 **Four vehicles
or mechanisms are now named that this file had never recorded: GEANT OCRE (EMEA), cooperative purchasing via Sourcewell / OMNIA
Partners / NASPO ValuePoint (North America), ChileCompra Directive 44/2026 (LATAM), and provincial-level buying under China's AI Plus
Education plan (APAC).** They are placed under *Opportunities by region* below, one `###` block per region.

🔴 **AND THE WHOLE LAYER CARRIES ONE CAVEAT, STATED ONCE HERE AND REPEATED IN EVERY BLOCK: IT IS SEARCH-CHANNEL-ONLY.**
**Sixteen non-GitHub hosts were tested this pass and all sixteen answered `403` at CONNECT or `000`** — `find-tender.service.gov.uk`,
`geant.org`, `ocre-project.eu`, `nwupc.ac.uk`, `crescentpurchasing.co.uk`, `irishtimes.com`, `aasa.org`, `stotles.com`,
`marketbrief.edweek.org`, `govtech.com`, `791coop.org`, `createyourrfp.com`, `govspend.com`, `oecd.ai`, `unu.edu`, `cenia.cl`.
**So no notice number, contract value, date or eligibility rule in this pass is verified at source.** 🔵 **Every notice ID is
recorded precisely so that confirming it costs one lookup on the buyer's own portal rather than one search** — which is the correct
form for a lead, and this layer is leads, not facts. 🟡 **Two regions also carry an INFORMED GAP rather than silence: no
2026 state-education-agency AI-tutoring RFP in North America, and no procurement vehicle of any kind in APAC.**

🔴 **One market-size note, because the prescribed trends query produced nothing usable:** three research firms put the 2025 AI-in-education
base at **$6.4B**, **$8.3B** and **$7.52B**, and 2034 at **$79.6B** — mutually inconsistent by roughly a factor of eight.
**No figure from that query is carried into this file.** The maturity reading is the only directional item worth keeping and it matches
what this file already says: most institutions remain in pilot mode.

**Pass 327 · 2026-10-19 (thirteenth pass of this date).** 🔴 **No market-size figure moved, no
regulation was added, and all four prescribed regional queries returned material this file already
holds.** That is the pass's market finding and it is recorded per region under *Declared regional
gaps* below rather than left as silence. **One new market actor, one new citable source, and one
structural read that changes the North America opportunity.**

🟢 **The new actor is a supply-side consolidation, not a statistic.** A single US vendor —
**Learning Commons** — now publishes the **curriculum-standards spine, the teacher-workflow agent
skills and the pedagogy evaluation layer** as three separate repositories with permissive code,
**co-developing the skills tier with Anthropic** (`NOTICE`: *Copyright 2026 Anthropic, PBC* /
*Copyright 2026 Learning Commons*, "under a collaboration agreement") and shipping it into
**Claude for Teachers** with a Knowledge Graph connector claiming **academic standards across all
50 states**. 🔵 **Read it against this file's own *Key players* section: the three layers Globant
has been proposing to assemble per engagement are now available pre-wired from one vendor, under
MIT and Apache-2.0 on the code. That raises the floor on a North America K-12 bid and lowers the
billable hours in it — see *Opportunities by region → North America*.**

🟡 **The new citable source is the OECD *Digital Education Outlook 2026*** (published January 2026,
247 pages, DOI `10.1787/062a7394-en`). It argues generative AI aids learning **only under explicit
pedagogical design**, warns that general-purpose tools without such design risk **reduced
cognitive effort and loss of teacher autonomy**, and reports from **TALIS that 37% of
lower-secondary teachers said they used AI in their work in 2024**. 🔵 **It is an
intergovernmental source for a position this file has so far sourced to vendor blogs and
`intel/trends.md` inference — which makes it usable in a bid.** 🔴 **Flagged as
search-channel-only: `www.oecd-ilibrary.org` answered 403 to CONNECT, so the DOI, page count and
the 37% figure are from search-result text and are not verified at source.** The next pass with a
reachable host should confirm them before they are quoted to a client.

🔴 **Verification surface of this pass, because it bounds everything above.** GitHub was reachable;
`arxiv.org`, `www.nature.com`, `www.sciencedirect.com`, `www.oecd-ilibrary.org`,
`www.iesalc.unesco.org`, `huggingface.co`, `www.semanticscholar.org`, `ar5iv.org`,
`docs.learningcommons.org` and `platform.learningcommons.org` **all answered 403 to CONNECT**.
🔵 **Every repository claim in this pass is first-hand from the `raw` channel or the rendered
GitHub page. Every policy and market claim that could not be checked at source is labelled above
and below as search-channel-only. Nothing from a denied host has been promoted to data.**

**Pass 326 · 2026-10-19 (twelfth pass of this date).** **One regional regulatory addition, one
promotion out of the policy matrix into prose, one new market actor, and one claim rejected
before it reached this file.** No market-size figure moved. The supply finding of this pass is in
`repos/foundations.md` and it has a market reading: **the sector's largest open curriculum
dataset is published by a venture-funded consumer edtech, not by a ministry or a university** —
see *Key players* below.

🔴 **Rejected before writing: "Ley Nahui."** The LATAM sweep returned it as a Mexican AI bill. A
direct verification search found **no bill, no author and no document of that name** in the
Gaceta Parlamentaria results or anywhere else. **It is not in this file and the next pass should
not re-find it.** Mexico's actual position is unchanged and already carried here: no general AI
law published in the DOF; the Senate's *Ley Nacional para Regular el Uso de la Inteligencia
Artificial* (Sen. Karina Isabel Ruíz Ruíz, MORENA) **stalled in committee**; a PRI general-law
bill received by the Permanent Commission in June 2026; sectoral rules advancing instead.

**Pass 320 · 2026-10-19 (sixth pass of this date).** This pass adds **regional regulation only** —
no market-size figure moved and no new player was found. Four additions and one reconciliation:
**Taiwan** enters this file for the first time (AI Basic Act, December 2025; implementing committee,
March 2026); **South Carolina H.B. 5253** gives the parent-consent requirement a **second,
independent instance** after pass 319 could source it only to a single tracker; **California AB 2876
and Utah H.B. 273** add to the curriculum-mandate column; and **two European Commission reports of
2026-09-22** supply a citable substitute for the EU strategy-coverage statistic pass 319 told future
passes not to quote. The reconciliation is **Vietnam**: the two conflicting education dates this KB
declared irreconcilable now look like **a grandfathering cutoff and a transition deadline**, not a
contradiction. **LATAM returned nothing new and that is recorded as an informed gap, not omitted.**
**Everything in this file remains snippet-sourced — the egress test was re-run this pass, not
inherited; see the sourcing note at the end.**

**Pass 319 · 2026-10-19.** This pass adds four things and corrects one.

It adds **the first quantified grounding number in this KB** — on Brazil's national curriculum, an
ungrounded model invents a standard **31.9%** of the time, falling to **2.3%** when it queries the
verified source over MCP (`repos/foundations.md`). It adds **four more US states with enacted
education-AI statutes** and a product requirement nobody has been scoping: **a parent opt-out**. It
adds the **European Commission's two September 2026 reports** and the education package behind
them. And it adds **LATAM teacher-adoption figures that are not derived from global forecasts** —
the gap this KB has declared four passes running, now partly closed with UNESCO country data.

**The correction matters more than any of them.** This KB, via a secondary summary, was carrying
South Korea's AI-textbook reversal as an **August 2026** event. **It was August 2025.** The full,
dated sequence is in the APAC regulation entry below, and it is the best-documented failure of a
national AI-in-education rollout anywhere in this KB.

**Method note, stated plainly because it governs everything below.** This session's egress policy
allowed **github.com and nothing else**: `unesco.org`, `arxiv.org`, `education.ec.europa.eu`,
`digital-strategy.ec.europa.eu`, `koreaherald.com`, `k12dive.com`, `multistate.us` and `iadb.org`
were all refused at connect time. **Every GitHub fact in this KB this pass is first-hand; every
non-GitHub fact in this file is from search snippets.** Brief on them; confirm before a client
document.

## Market size — and why the numbers still disagree

Published 2026 estimates for AI-in-education span roughly **$6.4B to $11.4B** depending on the
house and what it counts:

| Estimate | Source type | Note |
|---|---|---|
| $6.4B (2025), ~31% CAGR to 2034 | commercial forecast | lowest base of the set |
| $8.3B (2025) → ~$11.4B (2026) | commercial forecast | implies ~37% YoY |
| ~$9.58B (2026), ~34.5% CAGR to 2035 | commercial forecast | new this pass; lands mid-range |
| $10.6B (2026) → $42.48B (2030) | commercial forecast | the figure earlier passes carried; the 2030 number implies ~41% CAGR |
| → ~$32.27B (2030) | commercial forecast | new this pass; a third 2030 terminal value, ~24% below the $42.48B one |

**Do not quote a single figure to a client.** The honest framing: *high single-digit to low
double-digit billions in 2026, growing 30–40% a year, with no agreement on the base.* All are
vendor or research-house marketing and none publishes its segmentation. The directional claim —
fastest-growing software vertical in education, driven by tutoring and assessment — is well
supported; the decimal places are not.

Regional shares, same caveat (single-house figures, do not add them up):
- **North America** ≈ $951M (2024) → ≈ $2.3B (2029); a separate house puts NA at ~36% of the global
  market and $3.68B in 2026, which is not reconcilable with the first series. Both are secondary.
- **APAC** ≈ $591.6M (2024) → ≈ $1.85B (2029); China (≈$417.5M) + Japan (≈$318.7M) > 55% of APAC.
  Separately, APAC is claimed to grow fastest at ~48% CAGR — an outlier; treat sceptically.
- **EMEA — the five-pass gap is closed, and the answer is two forecasts that disagree.** Europe-
  specific AI-in-education figures *are* published, contrary to what passes 313–317 concluded:
  **Marketdataforecast puts Europe at $2.11B (2026) → $19.97B (2034), 32.47% CAGR**, from a $1.59B
  2025 base; **SNS Insider puts the 2025 base at $1.46B → $16.84B (2035), 27.71% CAGR.** The two
  2025 bases differ by ~9%, the terminal years differ, and neither publishes a methodology. A third,
  lower-quality blog estimate assigns Europe 25% of the global market at $2.75B in 2026.
  **Quote the range ($1.5–2.8B in 2025–26, ~28–32% CAGR) and name the houses, never a point
  figure.** No euro-denominated figure was found at all — every estimate is USD.
  The funding signal stands alongside it and is better evidence: **edtech venture funding of ~$1B in
  H1 2026, down 26% from ~$1.35B in H1 2025**, with Europe a preferred destination for US and global
  edtech expansion. Funding is contracting while expansion continues — buyers are consolidating onto
  fewer vendors. **The correction to record: earlier passes advised "stop looking, it is not
  published." That was wrong — it is published, it is just weak.**
- **GCC** — UAE ≈ **28% of the GCC edtech market in 2026**, the largest regional share, on the back
  of the UAE National AI Strategy 2031 and Saudi Arabia's Human Capability Development Program.
- **LATAM** — no market-size figure found that is not derived from the global forecasts. Declared
  gap, fourth pass running. The LATAM evidence that *does* exist is survey and company-level, below.

## Adoption — the Digital Education Council 2026 survey replaces this section's old numbers

Earlier passes carried "student AI use 66% → 92%" from a secondary roundup. This pass found a
primary-style source with published methodology and it is better: the **Digital Education Council
AI in Higher Education Global Survey 2026 — 45,398 responses (27,284 students, 18,114 faculty)
across 35 countries.** Use these figures and retire the roundup.

- **Students using AI in their learning: 88%. Faculty using AI in their teaching: 77%, up 16
  percentage points year on year.** Faculty are closing the gap, not widening it.
- **Only 29% of students believe their instructors are equipped to guide them on AI use — and only
  17% in the US and Canada.** The lowest confidence is in the most-regulated market.
- **57% of students say their assessments come with inadequate AI guidance.**
- **43% of students report no AI integration in their courses at all**, and among those who have
  seen integration, **only 5% say it transformed how they learn.**
- **64% of faculty have had AI literacy training**, but **only 31% feel meaningfully involved in
  shaping their institution's AI policy.**
- Regional: **APAC faculty are the most enthusiastic (57% excited) yet report the lowest future
  adoption intent of any region at 67%**. **Faculty intent in the US and Canada fell 9 percentage
  points year on year, from 76% in 2025 to 67% in 2026** — quantified this pass — while other
  regions held steady. **North America is the only region where faculty appetite is going
  backwards**, and it is the region with the heaviest regulation and the lowest student confidence
  in faculty (17%). Those three facts are the same fact: NA faculty are being asked to carry AI
  without preparation or cover, and they are withdrawing.
- **Public appetite for restriction splits APAC internally** (Ipsos Education Monitor 2026): the
  Asian markets surveyed show **lower** support for banning AI in schools, while **Australia and
  New Zealand record higher support for a ban.** An ANZ engagement is closer to the North American
  restriction posture (pattern P7) than to the rest of APAC — do not treat APAC as one market.
- LATAM, separate DEC survey — **provenance upgraded this pass and now the numbers behind it.**
  The *AI in Higher Education LATAM Survey 2026* (**30,000+ responses across 29 higher-education
  institutions**; one secondary source specifies 22,941 students, unconfirmed on DEC's own pages)
  reports: **92% of students and 79% of faculty actively engaging with AI** — both above DEC's own
  global figures of 88%/77% — **94% of faculty expect to use AI in future teaching** and **only 12%
  see AI as a threat to their role**; **61% of students fear peers misusing AI** and **65% worry AI
  makes learning too shallow**; **only 30% of students say their institution's use of AI meets their
  expectations**; and **50% of students want AI-assisted feedback while only 19% of faculty provide
  it.** Earlier passes carried the 92/30 pair from an opinion column; it now traces to the survey.
  **The 50/19 feedback gap is the most directly actionable number in LATAM** — a named feature,
  wanted by half the students, delivered by a fifth of the faculty.

**The LATAM institutional baseline, new this pass and the strongest regional source in this KB.**
UNESCO IESALC's *AI Implementation in Higher Education in Latin America and the Caribbean*,
**launched 2026-09-09 during Digital Learning Week in Paris** with UNU-IAS support, surveyed
**200 institutions across 19 countries**:

- **87% of institutions use AI in at least one area of their activities.**
- **Only 26% have a formal AI strategy.**
- **74% use it in teaching and learning**, usually through general-purpose tools rather than
  education-specific systems.
- **57% use it to support data analysis and research quality.**
- Adoption is **driven by individual academics, researchers and students**, not institution-wide
  strategy, and the study finds shortfalls in policies, governance structures, monitoring and
  evaluation.
- **Public institutions face greater resource and capacity constraints** than private ones.

Earlier passes carried this paper as "a citable regional baseline" without its headline figures;
these are the figures. **Do not confuse them with a separate, earlier UNESCO IESALC figure of 45%
of LAC institutions having formal AI guidance against 70% in Europe and North America** — different
instrument, different question. The 87/26 pair is the one to quote, and the gap between them is the
entire LATAM pitch: near-universal use, almost no strategy, and the adoption happening bottom-up
where no procurement process can see it.

**The structural reading is sharper than "usage is ahead of governance".** Usage is near-universal,
*institutional integration is largely absent* (43% see none), and where it exists it is judged
worthless by 95% of the students who experience it. The sellable problem is not adoption and not
only governance — it is that institutional AI deployments are not landing.

US K-12, retained from earlier passes and directionally consistent: teacher AI training 24% → 48%
of districts to spring 2025; student ChatGPT-for-schoolwork 13% → 26%; district AI policies ~40%;
~60% of US K-12 teachers used AI tools in 2024-25, 32% at least weekly. **A Gallup/Walton
Family Foundation figure surfaced this pass puts it as 32% of teachers using AI tools at least
weekly and 40% not using them at all** — consistent with the above and a useful pairing, because
the 40% is the half of the room a district enablement programme is actually for.

**LATAM teacher adoption — the figures this KB has wanted for four passes, new this pass.** UNESCO
reports that in **2024**, secondary-school teachers who had used AI in the previous year ran at
**56% in Brazil, 55% in Chile, 53% in Colombia and 52% in Costa Rica, against an OECD average of
36%.** A later Uruguayan survey puts **75% of public-school teachers** there reporting use.
**Read with the UNESCO IESALC institutional figures below (87% of institutions using AI, 26% with a
strategy), this is the sharpest regional story in the KB: LATAM teachers are roughly 50% more
likely to have used AI than the OECD average, and their institutions have almost no strategy for
it.** *(Country figures are snippet-sourced from UNESCO material this session could not fetch
directly; the 2024 reference year matters — do not present them as 2026 figures.)*

**The grounding number — new this pass, and the most useful single statistic in this file for a
technical pitch.** `bncc-dev/bncc-benchmark` (`repos/foundations.md`) measured curriculum
hallucination across 8 models and 300 items on Brazil's BNCC: **31.9% with no source available,
0.2% with the curriculum data pasted into the prompt, 2.3% when the model queried the verified
dataset over MCP** — an average drop of 30.6 points. Faithful-text rates across the models it
tested range from 88% down to 3%. **This is first-hand, reproducible and regionally specific, and
it is the answer to "why not just use ChatGPT?" in one line.**

## Key players — who the client is already talking to
### 🟢 Learning Commons — the US standards-data vendor behind Claude for Teachers (added p327)

**A player this file has never named, and the client is already talking to it whether or not they
know the name.** Learning Commons publishes three repositories with permissive code — all licences
read first-hand at p327:

| artefact | licence | ★ | what the client sees |
|---|---|---|---|
| `learning-commons-org/knowledge-graph` | MIT code; data **per dataset and per download** (Open / Open + Gated / Gated) | 161 | US academic standards by state, state↔CCSS crosswalks with `jaccard` scores, Math + ELA learning components, Math Coherence Map, WIDA ELD, XQ Competencies, Carnegie Skills Progressions (Carnegie Foundation + ETS), Eedi Misconceptions Graph, IM® v.360, OpenSciEd |
| `learning-commons-org/agent-skills` | **Apache-2.0** | 40 | Four K-12 teacher skills over MCP |
| `learning-commons-org/evaluators` | MIT code · CC BY 4.0 prompts · **CC BY-NC-SA 4.0 corpora** | 86 | 19 learning-science evaluators, Python + TypeScript SDKs |
| `anthropics/k12-teacher-skills` | **Apache-2.0**, co-developed | **575** | The same four skills shipped inside **Claude for Teachers** |

🔵 **Why it belongs in this section rather than in the repo files alone.** p326 observed that the
sector's largest open curriculum dataset is published by a **venture-funded consumer edtech, not a
ministry or a university**. **This is the second and stronger instance of the same market
structure, and it goes further: the vendor is distributing through a frontier-model provider's
teacher product.** 🟢 **The distribution channel, not the dataset, is the competitive fact.** A US
district that adopts Claude for Teachers inherits this standards spine by default — so a Globant
proposal that assumes the client needs a standards layer built is proposing something the client
may already have, and a proposal that *integrates* it starts further up the value chain.

🔴 **And the commercial boundary, because it is where a bid gets stuck:** the code is permissive
throughout, but **IM® v.360 instructional and assessment materials and the whole OpenSciEd dataset
are Gated** — publisher approval and a separate agreement — and the **expert-annotated CLEAR and
PERSUADE 2.0 corpora that validate the evaluators are CC BY-NC-SA 4.0**, so they cannot be
redistributed in a paid deliverable or used to validate a commercial model release. **Build on the
Open tier; price the Gated tier as a publisher negotiation.** Details in
`verticals/solutions.md`.


**New actor, new category — the curriculum-data publisher (p326).** **Generative Spark, Inc.
(Marble)** — a consumer learning app — published the **Marble Skill Taxonomy** on 2026-07-08 as
`withmarbleapp/os-taxonomy`: **1,591 micro-topics, 3,225 prerequisite edges, seven national
curricula, ODbL-1.0 + CC BY-SA 4.0, 6.1 ★k, 998 forks.** 🔵 **The market reading is the publisher,
not the dataset.** This KB's trend 12 has assumed curriculum-standard data comes from ministries
(Brazil's BNCC), national operators (France's FUN, Germany's `openeduhub`) or universities. **This
one came from a venture-backed consumer edtech that gave away the asset its own product is built
on**, under a share-alike licence that keeps improvements flowing back to it. 🟢 **That is a
commons-as-moat play and it is the first in this sector this KB has recorded.** For a studio it
cuts both ways: **the spine is free, so nobody can sell the client a curriculum graph any more** —
and the differentiation moves to what the client's own jurisdiction, assessment evidence and
delivery add on top of it.

**Global / model layer:** Anthropic (Claude for Education, Socratic "Learning Mode", institutional
deals) · Google (free Gemini for college students through 2026 — the volume play) · OpenAI ($50M to
university research partnerships) · Microsoft, AWS, IBM as infrastructure incumbents.

**The model vendors are now buying the institution directly, not the department — new this pass.**
The named 2026 flagships are **California State University's ChatGPT Edu deployment, covering
460,000+ students and 63,000+ faculty and staff**, and **Northeastern's Claude for Higher Education
rollout**. **Harvard's CS50 Duck** remains the most-cited course-level tutor deployment.
**The commercial read is uncomfortable and should be said plainly to a studio lead:** a system-wide
frontier-model licence is the competing line item to a custom tutor build, and it arrives with the
CIO rather than through the LMS. What it does *not* include is the deterministic pedagogy layer,
the audit trail a regulated district has to buy anyway, LMS-native grade passback, or on-premise
operation. Pitch against the gaps in the seat licence, never against the model.

**Platform layer:** Instructure (Canvas — **Project Athena**, AI study coach announced 2026-07-22,
in development) · Moodle HQ · edX/2U · Pearson · McGraw Hill · D2L · Coursera + Udemy (all-stock
merger; consolidation at the content layer).

**MENA / Africa — named for the first time in this KB:**
- **Alef Education** (Abu Dhabi) — ranked **#1 edtech company in MEA and 13th globally** in TIME's
  World's Top EdTech Companies 2026 list (~6,500 companies evaluated). The region's flagship.
- **Classera** (Saudi Arabia) and **Abwaab** (Jordan) — adaptive-learning platforms active across
  the Gulf; personalised adaptive learning is the region's most common AI use.
- **EIDU** (Kenya) — structured-pedagogy platform with roughly **400,000 children** using it and
  documented learning gains.
- **FlexiSAF** (Nigeria, school management + AI course creation) and **Tuteria** (Lagos, tutoring
  marketplace).
- **World Bank AI-tutoring programme in Edo State, Nigeria** — significant learning gains reported
  after six weeks of AI tutoring with teacher guidance. The most-cited evidence base for AI tutoring
  in a low-resource setting; the widely repeated "400,000 students" figure is secondary, so cite the
  programme, not the number.
- **Kenya DigiSchool** — over 1 million tablets delivered to primary schools by 2025.
- **All of these are proprietary.** See the gap note in `verticals/solutions.md`.

**LATAM — named for the first time in this KB** (HolonIQ 2026 Latin America EdTech 100):
- **Teachy** (Brazil) — AI lesson preparation; a regional incumbent that has expanded into Asia.
- **Mattilda** (Mexico) — billing and collections for private schools; **$50M plus an acquisition**.
- **Ginia** (Mexico) — AI-driven employability matching between employers, institutions, students.
- **Vetto** (Brazil) — raised new capital on a similar employability thesis.
- **Luca** (Mexico) — **US$8M Series A**, K-12 AI education, regional expansion planned.
- Brazil accounts for **68.93% of LATAM's 898 active edtech startups** (secondary source).
- **CENIA (Chile)** — Latam-GPT; the region's only sovereign-model effort.

**APAC — named education-specific players, partially closing a declared gap:** **Riiid** (South
Korea, AI tutoring) and **Squirrel AI** (China, adaptive learning) are the region's
education-specific AI companies named in directory sources; generic market-report player lists for
APAC (Google, Microsoft, IBM, Pearson, Byju's) are not education-AI-specific and are not worth
quoting. There is still **no APAC edtech ranking** comparable to HolonIQ's LATAM 100 or TIME's MEA
list — the gap narrows to named players, not a ranked market map.

**LATAM — the multilateral layer, new this pass.** UNESCO launched the **Observatory on Artificial
Intelligence in Education for Latin America and the Caribbean on 2026-04-14 in Santiago**, to help
states integrate AI into education systems. Its partners are the institutional map of the region:
**CAF, CENIA (Chile), CETIC.br (Brazil), ECLAC, Fundación Santillana, Tecnológico de Monterrey,
ProFuturo and Fundación Ceibal (Uruguay).** For a studio, this is the list of bodies that will shape
LATAM public-sector education AI procurement, and a credible route in that is not a sales call.
Also new: the **Raspberry Pi Foundation's Experience AI programme is scaling across LATAM with
$4.6M from Google.org**, targeting **24,000 educators trained and 1.25 million students by 2028
across nine countries** including Brazil, Chile and Mexico — openly licensed teacher-training
material arriving at scale, which is competition for the "train the client's team" phase and a
partner opportunity for everything after it.

Named LATAM education-AI products from the OEI/ProFuturo mapping: **Letrus** (Brazil,
Portuguese-language writing instruction) and **MusíGlota** (Chile, English learning). Both
private-sector, neither open source.

**Open source:** the twenty-six agents in `agents/top.md`, the twenty foundational repos in
`repos/foundations.md` and the twenty-seven platforms in `verticals/solutions.md`. HKUDS (DeepTutor,
LightRAG) remains the single most consequential lab for this sector's permissive tier, and
**OpenOLAT** (Apache-2.0, 31,877 commits, Switzerland) the one mature permissively licensed LMS.
**New and regionally significant this pass: Brazil.** `portabilis/i-educar` (GPL-2.0, 34,948
commits) is a municipally originated school-management system published through the federal Portal
do Software Público; **`bncc-dev` (Profy) publishes the national curriculum as verified data under
MIT/CC BY 4.0, with an MCP server and a hallucination benchmark.** For the first time this KB can
describe a complete regional open source stack that is not imported.

**Venture funding — updated, and the definitional spread is now part of the finding.** HolonIQ
counts roughly **$1B of global edtech venture funding in H1 2026, down 26% from ~$1.35B in H1
2025**; **Crunchbase puts education-related startups just under $1.8B for the same period**, the
gap being what counts as an education company. **No Q3 2026 edtech-specific total was found this
pass** — Crunchbase's $159B Q3 figure is all sectors and must not be repurposed. What is visible is
selective capital: **Reach Capital closed a $265M fifth fund in August 2026** naming AI
applications in learning, health and work; recent rounds include **Preply $150M Series D**,
**Multiverse $70M** for AI and workforce training, and **EdVisorly $13.3M Series A** for
AI-assisted college transfer. One commentary notes many AI education tools are **being
commoditised because they offer little a general-purpose AI subscription does not** — the same
competitive read as the frontier-model seat licences above. *(A circulating "EdTech funding fell
89%" headline and an undated "$410M invested in 2026" figure conflict with everything else here;
do not use either. A Rest of World piece reporting K-12 startup funding down 82% is from April
2026.)*

## Standards — new to this KB and a live buying trigger

**1EdTech's 2026 position is that interoperability is the precondition for AI**, naming **CASE,
Edu-API and OneRoster** as the standards that give an AI system the shared context it needs to act
with trust and relevance; it has also signalled an expanded Generative AI rubric. **IEEE P3428**
targets interoperability of LLM agents in educational systems and is in its initial phases.

This matters commercially because it is the first credible answer to "how does your agent know
anything about my institution?" that is not a bespoke integration — and because `Ed-Fi` +
`edfi-oneroster` (Apache-2.0, see `repos/foundations.md`) is now a verified open source path to it.

## Regulation by region — the real buying trigger

### 🔴 CORRECTION (p328) — the EU AI Act high-risk date this file has been quoting has moved by sixteen months

**This file and `compose/patterns.md` P4 have both been built on Annex III education obligations biting on 2026-08-02.** The p328 EMEA sweep reports that date **superseded**: high-risk obligations for **stand-alone** education AI systems move to **2027-12-02**, and for high-risk AI **embedded in regulated products** to **2028-08-02**, via **Regulation (EU) 2026/1744**.

🟢 **What does NOT move, and this is the part that keeps the EMEA bid alive:**
- **Art. 4 AI literacy** — applicable since **2025-02**, already binding on institutions today.
- **Art. 50 transparency** — unmoved. Sources in this sweep disagree on the exact date (**2026-08-02** vs **2026-11-02**); **the disagreement is recorded rather than resolved**, and either way it is *this quarter or next*, i.e. **before** the high-risk regime.

🟡 **Confidence, stated plainly: this is a single-sweep finding from secondary legal-commentary sources, and one of them notes the Council had not formally adopted the text at the time of writing.** `eur-lex.europa.eu` and every institutional host were unreachable this pass (see the gap note), **so the Regulation number above is NOT first-hand.** 🔵 **Verify against EUR-Lex before it goes in a client deck.**

🔵 **The commercial read, and it is a sharpening rather than a loss.** The EMEA pitch has been *"the compliance deadline is weeks away."* It is not, and a client who checks will find that out. **The honest and still-urgent pitch is the inversion: the binding duties that remain on the near calendar are literacy and transparency — documentation, disclosure, training — which is the cheap half of the Art. 50 package and sells as a 6–8 week engagement. The expensive half (conformity assessment, the Annex IV technical file) now has eighteen months of runway, which makes it a 2027 pipeline item, not a 2026 emergency.** 🔴 **A studio that keeps quoting August 2026 will be corrected by the client's counsel.**

- **North America: four states now have *enacted* education-specific AI statutes, and one of them
  contains a product requirement nobody in this KB has been scoping — a parent opt-out.** New this
  pass: **Idaho, Maryland, Oklahoma and Virginia** each passed 2026 measures requiring the state
  education department to produce guidance on safe and responsible AI use in schools **and
  requiring local school boards to adopt aligned policies.** The laws set guardrails rather than
  removing AI from classrooms. **Oklahoma is the restrictive one:** AI permitted only under
  educator supervision with human review, **barred from high-stakes student decisions**, with
  parent disclosure — and per one tracker, **a parent opt-out from student-facing AI tools together
  with a duty to provide alternative access to core instruction.** *(The opt-out appears in a
  single tracker, not read against the statute — verify before it enters a bid, but scope for it:
  the feature is cheap and a product that cannot honour a per-pupil opt-out is unbiddable where it
  applies. See pattern P7.)*
  **Curriculum mandates arrived alongside the guardrails:** Georgia and Mississippi are requiring
  computer-science credits that include AI instruction later this decade, and **Alabama requires an
  approved CS course with AI instruction to graduate.**
  **Guidance coverage is now ~33–35 states plus Puerto Rico** (this KB previously carried ">28
  states plus DC"), and **Ohio has published its model policy** against the 2026-07-01 district
  deadline.
  The rest of the picture is unchanged: state-led, fragmented, and *accelerating*. **134
  AI-in-education bills across 31 states in 2026**, focused on data privacy, classroom restrictions and curriculum
  (California AB 1159, Idaho SB 1227 on student data; Oklahoma and Maryland reported to require
  human oversight and bar AI from high-stakes student decisions). Ohio requires an AI framework in
  every public/community/STEM school by **2026-07-01**. >28 states plus DC have K-12 guidance,
  mostly non-binding. **Federal: the K-12 AI Literacy and Readiness Act of 2026 (H.R. 8747)
  advanced out of the House Education and Workforce Committee at a 2026-07-21 markup — no floor
  passage found.** Restriction is also real: **New York City has a one-year moratorium on
  student-facing AI through eighth grade**, and Katy ISD (Texas) is banning generative AI chatbots
  for K-6. **North Carolina** has published K-12 guidance, joining the >28 states plus DC with mostly
  non-binding frameworks. A **student-authored national framework, the "STUDENTS FIRST Act of
  2026", was produced by students from all 50 states** and publicised by AASA on 2026-08-03 with
  Day of AI — not legislation, but a live signal of what student stakeholders will ask districts
  for, and useful in a governance workshop. **Canada:** a June 2026 "AI for All" plan with a
  national AI literacy push — strategy, not statute. **Mexico:** bills but no enforcing regulator yet.
  For scale, **NCSL counts ~1,390 AI bills across 49 states in 2026** across all subjects — the 134
  education bills sit inside a far larger wave. Tracker counts disagree (one K-12-only tracker says
  27 states with active bills and five enacted; a source found this pass says "around 100
  AI-in-education bills" are moving in the 2026 session against this KB's 134 across 31 states);
  the disagreement is scope, not error, so **cite the tracker you used and the date you read it.** **North Carolina's dates are now specific:** covered districts had to adopt a
  policy by **2026-07-01**, a state model policy is due **2026-12-31**, and local policies follow by
  **2027-06-30.**
  **The amended COPPA Rule is the hardest dated trigger in this KB, and it is already in force —
  new this pass.** The FTC published the amendments on **2025-04-22**, effective **2025-06-23**,
  with full compliance required from **2026-04-22**. Three changes bite directly on an AI tutor for
  under-13s: **§312.5(a)(2) requires separate verifiable parental consent before disclosing a
  child's personal information to a third party** — and the exception covers disclosures *integral*
  to the service, not merely useful or convenient; **data retention limits plus a written, published
  retention policy**; and **biometric identifiers added to the definition of personal information.**
  **Read against a typical architecture, sending a K-6 pupil's prompts to OpenAI, Anthropic or
  Google is a third-party disclosure requiring its own parental consent, separate from consent to
  use the product at all** — and parents may grant the second while refusing the first. That single
  clause is the strongest commercial argument in this KB for the on-premise and offline stacks
  (patterns P5 and P7) and for Moodle's Ollama/LiteLLM provider route
  (`verticals/solutions.md`). Treat it as a design constraint, not a legal footnote. FERPA, COPPA
  and state privacy law (CA, IL, NY) continue to do the binding work.
  **Pass 320 adds a second, independent instance of the parent-consent requirement — which was the
  weakest-sourced item in this entry.** Pass 319 flagged Oklahoma's **parent opt-out** as appearing
  in *a single tracker*, unread against the statute, and told future passes to scope for it anyway.
  **South Carolina H.B. 5253 is reported to require written parental opt-in consent**, among other
  protections. Opt-*in* is a stricter posture than Oklahoma's opt-*out*, and two states reaching for
  parent consent by different mechanisms **moves this from a single-tracker curiosity to a product
  requirement.** Pattern **P7** should treat per-pupil consent state as a first-class data model,
  not a flag. *(Snippet-sourced; `www.future-ed.org` and `www.multistate.us` are both unreachable
  from this session — see the sourcing note at the end of this file.)*
  **Two curriculum mandates new to this KB, both snippet-sourced:** **California AB 2876** is
  reported to mandate integration of **AI literacy into the K-12 curriculum**, and **Utah H.B. 273**
  to integrate **AI into the state computer-science standards.** These belong with Georgia,
  Mississippi and Alabama in the curriculum-mandate column rather than the guardrail column — and
  the distinction matters commercially, because a literacy mandate buys **content and teacher
  training**, while a guardrail mandate buys **governance tooling**. This KB has been better at
  tracking the second than the first.
  **The FTC's amended COPPA rule reached its general compliance date on 2026-04-22.** This KB
  already carries COPPA as a design constraint (see P9); **what it lacked was the date**, and a
  compliance date that has already passed changes how a disclosure-boundary conversation opens.
- **EMEA:** the EU AI Act lists education in Annex III as stand-alone high-risk — admissions,
  learning-outcome evaluation, student level placement, and exam or behaviour monitoring. **The
  Digital Omnibus (Regulation (EU) 2026/1744, OJ 2026-07-24, in force 2026-07-27) deferred the
  Annex III high-risk obligations by 16 months to 2027-12-02.** What was *not* deferred, and is
  new detail this pass: **Article 50 transparency has applied since 2026-08-02**, and the
  **watermarking grace period for AI-generated content runs to 2026-12-02**; **new prohibitions
  (non-consensual intimate imagery, CSAM) apply from 2026-12-02**; **Article 4 was relaxed to an
  obligation to take AI-literacy measures for staff**; Annex I embedded products move to 2028-08-02.
  Emotion-recognition AI has been banned in schools since Feb 2025 — the prohibition is
  **Article 5(1)(f)**, with narrow medical and safety exceptions, and it is one of the few AI Act
  provisions that was never deferred. Schools are "deployers"; the
  tool vendor is the "provider" carrying conformity duty — precisely the role a Globant-built tutor
  occupies. The deferral moved the date, not the substance.
  **The Omnibus's status was re-verified this pass and confirmed in force**, with the adoption trail:
  **Parliament endorsed the deal on 2026-06-16, the Council adopted it on 2026-06-29**, OJ
  2026-07-24, in force 2026-07-27. **A trap worth knowing:** at least one major law firm's published
  AI-Act tracker still carries pre-adoption text describing the deferral as "proposed" and an
  April 2026 trilogue as having ended without agreement. **A client may well arrive holding that
  page.** Enforcement itself began on schedule — the **AI Office and national authorities started
  enforcing the AI Act from 2026-08-02** — so "the Act is delayed" is a misreading: what moved is
  the Annex III high-risk obligations, nothing else.
  **The Commission published two education reports on 22–23 September 2026, and they are the best
  EMEA demand evidence in this file — new this pass.** The first, **"Friend or foe?"**, assesses
  generative AI in learning and teaching and concludes that **genAI is moving from technological
  innovation to a mainstream tool across EU education**, that whether it benefits learning *depends
  on how it is used*, that its long-term skills effects remain unclear, and that teachers therefore
  need **substantial initial and continuing professional development supported by institutional
  guidelines for responsible use.** The second is a **Eurydice** report on digital education in
  schools: most systems address the core components of digital infrastructure, but school-level
  access, technical support and digital environments still differ; **digital competence appears in
  lower-secondary curricula in almost all systems analysed, while national or standardised
  assessment of it remains uncommon.** A Commission **education package** is expected "later this
  year", carrying a **2030 Roadmap on the Future of Digital Education and Skills**. Separately, an
  item dated **2026-10-09** records **ENESET** evidence feeding a Commission paper on generative AI
  in education, and the Commission has published an **AI Literacy Framework (AILit)** alongside
  **2026 guidelines on the ethical use of AI and data in teaching and learning for educators**.
  **Three cautions, because this is the part a proposal will lean on:** the **"nearly two-thirds of
  European education systems have AI strategies, guidance or policy frameworks" figure could not be
  verified** and should not be quoted; the **November 2026 date** attached to the education package
  by one secondary source **could not be verified** either — the Commission texts say only "later
  this year"; and the AILit framework's status (draft or final, voluntary or expected) was not
  readable this pass because `education.ec.europa.eu` was unreachable. **The reports themselves,
  their dates and their conclusions are well attested across multiple independent summaries.**
  **Programmes to name in an EMEA conversation, new this pass:** **AI-ENTR4YOUTH**, a three-year
  programme coordinated by **JA Europe** with support from **Intel** and the European Commission,
  has students building applied AI projects in **10 European countries**; and **DUAL.AI.TEACHer**,
  an **Erasmus+ Teacher Academy of €1.9M with 11 partner organisations across 8 countries**. Both
  are publicly funded teacher- and youth-capability programmes — competition for the enablement
  phase of an engagement and a partner route into it.
  **National funding and capacity, carried from pass 318:** Denmark's AI strategy carries **€200M
  for R&D with education named as a focus area**; **France's AI for Humanity** and the **Netherlands'
  National AI Strategy** both direct public funding at educational AI. On the demand side,
  **73% of UK adults report having had no AI education or training at all** — the clearest
  single number in this KB for the EMEA adult-reskilling opportunity.
  **MENA, new this pass: the UAE was the first country in the world to make an AI curriculum
  mandatory nationwide across K-12, from May 2025** — ahead of both China and India. Read with the
  GCC market-share figure below and the fact that every named MEA platform is proprietary
  (`verticals/solutions.md`), it describes a market with statutory demand, public money and no open
  source supply.
  **Pass 320, snippet-sourced: two European Commission reports published 2026-09-22** are reported
  to describe **generative AI as a mainstream tool in EU education**, with its effect on learning
  depending on how it is used. **Read against this KB's own declared gaps, this is the useful
  shape:** pass 319 searched for and failed to find the "nearly two-thirds of European education
  systems have an AI strategy" figure and told future passes not to quote it. **A Commission
  publication describing mainstream adoption is the citable substitute** for that unciteable
  statistic — it supports "this is normal in EU classrooms now" without inventing a percentage.
  `education.ec.europa.eu` and `digital-strategy.ec.europa.eu` remain unreachable from this
  session, so **the 2026-09-22 date and the characterisation are snippet-grade. Confirm both before
  a client document**, and note that pass 319 already recorded a *different* Commission education
  package as "later this year" with no verified month.
- **APAC — and the first item is the most important thing in this file for an APAC conversation,
  because it is a national AI-in-education mandate that was politically unwound.**
  **South Korea's AI digital textbooks lost their legal status as textbooks.** The National
  Assembly passed an amendment **on 2025-08-04** narrowing the statutory definition of a textbook
  to **printed books and e-books, excluding "learning support software using intelligent
  information technology"**, effective on promulgation. The practical consequence was financial:
  schools using the AI textbooks **lost funding support** for the subscriptions. Before the law
  changed, the Education Ministry had already retreated from a nationwide mandate to **voluntary
  adoption** after criticism from educators and parents about rushed implementation.
  **The adoption numbers are the lesson, and sources differ in scope rather than direction:** about
  **30% of schools** had integrated the textbooks (an OECD 2025 analysis puts it at roughly
  one-third, ranging from **98% in Daegu to 8% in Sejong**), and usage *decayed within the year* —
  **from ~37% of eligible classes in the first semester of 2025 to 19% in the second**, with
  schools using them falling from **~4,190 to 2,095**.
  **This KB was carrying the reversal as an August 2026 event, from a secondary summary. That was
  wrong: it was August 2025.** Correcting the date matters because it changes what the episode
  means — this is not breaking news, it is **a completed experiment with a year of outcome data**,
  and it is the strongest available evidence for this KB's standing position that *institutional AI
  deployment, not adoption, is the thing that fails* (trend 1).
  **How to use it:** in any APAC public-sector pitch, the Korean sequence — mandate, rushed
  rollout, teacher and parent backlash, retreat to voluntary, de-officialisation, funding withdrawn
  — is the risk the buyer is trying to avoid. **Sell preparation, teacher capability and
  measurable deployment, and price the change-management work as the main line item rather than the
  technology.** *(A widely repeated "$850M spent" figure comes from a low-quality blog and should
  not be used. One EU-based source attributes part of the unwinding to the Korean privacy
  regulator; that is unverified here. Both the Korea Herald and the ABC report were unreachable at
  this session's proxy, so all of the above is snippet-sourced.)*
  **China, new detail this pass:** Beijing's provincial authorities have set **a compulsory minimum
  of eight hours of AI education a year in both primary and secondary schools** since 2025,
  alongside the national move making AI a compulsory subject from age six. China still has **no
  general AI law** — it governs by instrument: recommendation algorithms (2022), deep synthesis
  (2022), the generative-AI measures (2023) and **AI-content labelling, applicable from
  2025-09-01**.
  **Japan, new detail this pass:** the **AI Promotion Act carries no penalties for
  non-compliance**, and the Cabinet **approved a second AI Basic Plan on 14 July**, revising the
  December 2025 original. The education ministry's posture is explicitly neutral — it is monitoring
  results from school AI pilots rather than mandating. **Japan is the region's lowest-friction
  market and the slowest-moving buyer; both at once.**
  **India, new signal this pass:** a July 2026 report indicates India **may now pursue dedicated,
  risk-based AI legislation** rather than continuing with voluntary guidance plus sectoral and data
  rules, and a **ten-million-teacher training push** is reported alongside the curriculum mandate.
  Treat both as signals, not commitments; the hard date remains the Class 3–8 curriculum mandate
  below.
  The rest of the region is unchanged: fragmented and mostly not education-specific. China's
  Interim AI Measures (in force 2023-08-15) require service registration, security review and labelling of AI-generated content;
  the State Council's "AI Plus" guideline (Aug 2025) targets 90% penetration of intelligent
  terminals/agents across six sectors by 2030. Japan is deliberately light-touch and voluntary.
  **South Korea — the flagged claim is now resolved, and the earlier framing was wrong.** Earlier
  passes carried "South Korea's AI Data Protection Act imposes strict privacy protocols on
  AI-driven edtech" from a single secondary source, flagged unverified. **There is no such act.**
  The instrument is the **Framework Act on the Development of Artificial Intelligence and
  Establishment of Trust** (the "AI Basic Act"), **promulgated 2025-01-21 as Law No. 20676 and in
  force since 2026-01-22**, with a reported **one-year grace period on administrative fines**
  (exceptions for serious social harm). It reaches education through its **high-impact AI**
  category, and the statutory definitions explicitly include **student evaluation in early
  childhood, elementary or secondary education** by reference to Article 9(1) of the Framework Act
  on Education. Operator duties reported for high-impact AI: **user-protection measures and records
  of safety and trust measures (Art. 34(1))**, with a **fundamental-rights impact assessment
  voluntary (Art. 35)**. **Foreign operators without a Korean presence must appoint a domestic
  agent** — which reaches a Globant-built tutor sold into Korea. An English translation of the Act
  is published by Georgetown CSET; the Enforcement Decree and MSIT guidance set the education
  thresholds and should be read before scoping. **Korea is now the clearest education-AI compliance
  trigger in APAC**, and the only general mandatory AI statute in the region.
  **Vietnam — new to this KB.** A binding AI law with transition periods; sources conflict on the
  education date (one gives extra time to education systems already operating before **2026-08-15**,
  another gives **2027-09-01** for health, education and finance). **Verify against the primary text
  before quoting either.** Singapore, India and Australia have **no AI-specific statute**: Singapore
  runs voluntary frameworks, India relies on its data-protection law, and **Australia's mandatory
  guardrails are paused** in favour of existing technology-neutral law. India's data-protection law
  phases in to full compliance by May 2027. **India's curriculum mandate remains the hard date: AI + Computational
  Thinking compulsory for Classes 3–8 from 2026-27, extending to Classes 9–10 in 2027-28, across
  32,900 CBSE-affiliated schools (50 h/yr Classes III–V, 100 h/yr VI–VIII).**
  **Public appetite for restriction, by country — new this pass** (Ipsos Education Monitor 2026,
  share supporting a ban on AI in schools): **Indonesia 23%, India 26%, Japan 29%, South Korea
  31%**, with **Australia and New Zealand higher than any of them.** This is the hard version of
  the "APAC is not one market" warning: a product can be sold into Jakarta or Delhi on capability
  and must be sold into Sydney on restraint. **China has made AI compulsory for school students
  from age six**, which with India's Class 3–8 mandate means the region's two largest school
  systems both have statutory AI curriculum demand running now.
  **Pass 320 adds a jurisdiction this KB had zero coverage of: Taiwan.** Reported this pass: an
  **AI Basic Act passed in December 2025**, with an **implementing committee established in March
  2026**. That is all that was found — no education-specific provision, no high-risk schedule, no
  classification of education systems. **Recorded because a named statute with a standing committee
  is a different planning object from silence**, and because this KB's APAC regulation entry has
  until now gone South Korea → China → Japan → Singapore/India/Australia → Vietnam with no Taiwan
  row at all. **Treat it as a lead to develop, not a finding to brief.**
  **Pass 320 also partially reconciles the Vietnam date conflict this KB declared open.** The
  declared gap records education transition dates of **2026-08-15 in one source and 2027-09-01 in
  another** and says to verify against the primary text. This pass found **2026-08-15 described not
  as the transition date but as a grandfathering cutoff**: education AI systems **already operating
  before 2026-08-15 are reported to get an additional six-month grace period**, with education one
  of **six sectors where AI systems are classed high-risk** — and high-risk mainly where the output
  is **the sole basis for a decision without meaningful human review**, which is a materially
  narrower trigger than "used in education". **If that reading is right, the two dates were never in
  conflict: one is the cutoff for existing systems and the other a transition deadline.** It is
  still snippet-sourced and `www.lw.com` is unreachable from this session, so **the gap stays open —
  but it is now a hypothesis to test against the primary text rather than an unexplained
  contradiction.** The "sole basis for a decision" trigger is the commercially important half:
  **a human-in-the-loop design may keep a product out of the high-risk class entirely**, which is
  exactly what P3's and P7's review gates already build.
  **One refinement to the Ipsos reading already carried here:** the **Education Monitor 2026**
  finding of lower support for banning AI in schools across Asian markets is reported with
  **Australia and New Zealand as the exception** — i.e. the permissive-public story is an *Asian*
  story, not an APAC-wide one, and an ANZ engagement should not inherit it.
- **LATAM, new this pass: Brazil signed an AI and technology regulation agreement with the EU in
  June 2026**, which is the clearest signal yet that an EU-shaped conformity file travels in the
  region — and it makes porting the pattern-P4 artefacts to Brazil a near-term rather than
  speculative move. **Chile's bill has a specific status now:** the executive's draft was unified
  with an earlier parliamentary initiative and is in its **first constitutional stage in the
  Chamber's Commission on the Future, Science and Technology**. **UNESCO's LAC Observatory has
  named pilots**, including one in **Mexico with CONALEP and DGETI to build centres of
  excellence** — a concrete entry point rather than a declaration. And a market-structure
  observation from HolonIQ worth carrying into positioning: **LATAM's AI activity is concentrated
  in teacher-facing instructional support rather than consumer tutoring**, which matches what this
  pass found in code — Brazilian open source is school-management and curriculum infrastructure,
  not student chatbots.
  Otherwise: still no unified framework, but **Brazil's PL 2338/2023 status is now confirmed** —
  a horizontal, risk-based AI bill, **approved by the Senate in December 2024** and not yet enacted;
  separately, **Brazil's data protection authority (ANPD) is running an AI regulatory sandbox
  through December 2026.** That closes a gap this KB declared for three passes. Chile leads with a
  National AI Policy since 2021 and a law under discussion. **Colombia's instrument is now named:
  CONPES 4144, adopted February 2025** — a national AI policy without education-specific rules.
  **Uruguay became the first country in Latin America to sign the Council of Europe's Framework
  Convention on Artificial Intelligence (2025)** — new this pass, and the region's strongest
  signal of alignment with European norms, which makes Uruguay the natural LATAM pilot for a
  conformity-packaged product. **Peru's regime sets phased implementation, entering into force
  after ninety business days.** **Mexico has a 2024 federal AI bill** that mirrors the
  international risk-based approach and **proposes an oversight authority**, but still no binding
  national law in force — SEP/ANUIES recommendations are non-binding. A comparative study across Argentina, Brazil, Chile, Peru and Spain found shared
  need for ethical guidelines but sharply different scope and implementation.
  **Pass 320 searched LATAM and found nothing new — stated explicitly, because an unrecorded empty
  search is indistinguishable from coverage.** The regional query returned only material this KB
  already carries first-hand or by snippet: the **UNESCO IESALC 87%/26%** institutional figures (200
  institutions, 19 countries, 74% in teaching and learning), the **UNESCO Observatory on AI in
  Education for LAC** launched **2026-04-14** at ECLAC in Santiago, **Uruguay's** Council of Europe
  framework-convention signature, **Colombia's CONPES 4144**, **Mexico's** 2024 federal bill,
  **Peru's** regulatory sandboxes, and the ILIA finding that school-level AI education is advancing
  but remains exceptional. **No new instrument, no new player, no K-12 adoption rate.** The one
  genuinely new LATAM item this pass is supply-side, not demand-side, and it is a rejection:
  `Bimbi-Dev/OpenTeacher` (Peru, Hackathon AIdea Lima 2026, no licence, core agent logic unwritten) —
  see `agents/top.md`. **The LATAM supply gap and the LATAM market-size gap both stand.**

## Opportunities by region — superseded, Pass 336 (kept for history; the canonical block is at the top of this file)

> **Pass 324 — one new opportunity, and it is cross-regional, so it is placed in all four rather
> than written as a section of its own.** The academic-integrity evidence chain is now buildable
> from permissive and service-isolatable open source (`sunilgentyala/aegis-integrity` MIT,
> `NoplagLabs/noplag-engine` Apache-2.0, `jplag/JPlag` GPL-3.0 behind HTTP, over the existing
> nbgrader / otter-grader / JupyterHub process-evidence stack — wiring in `compose/patterns.md`
> **P11**). Where it lands, by region, and the ranking is by *dated demand*, not by market size:
>
> - **North America — strongest.** Oklahoma and Maryland already require **human oversight** and
>   bar AI from high-stakes decisions about students; California **AB 1159** bars training on
>   student data; **134 bills in 31 states**. An integrity product whose output is *evidence for a
>   human* rather than a verdict is the compliant shape by statute, and the one this stack
>   produces. Sell the audit trail, and the fact that `aegis-integrity` runs **locally** and sends
>   only reference metadata to Crossref — never the student's document.
> - **EMEA — strongest on the regulatory argument.** Under the EU AI Act, AI used in **assessment
>   and exam scoring** is high-risk with duties live from **August 2026**. A tool that refuses to
>   issue an authorship verdict and logs human review is materially easier to place in the
>   high-risk regime than any detector, and **self-hosting plus local-only processing** is the
>   sovereignty story this region buys. 🔴 Note the licence constraint sharply here: JPlag is
>   GPL-3.0 — service boundary, never linked.
> - **APAC — narrower and more specific.** **Vietnam's** high-risk list covers automated assessment
>   and is explicitly high-risk *"only when the AI output is used as the sole basis for decisions
>   without meaningful human review"* — i.e. **the statute names the mitigation this stack
>   implements.** Korea's 2026 penalty grace is the window to deploy in.
> - **LATAM — highest institutional need, lowest institutional readiness.** UNESCO IESALC / UNU-IAS:
>   **87% of institutions use AI somewhere and 26% have a formal strategy.** An integrity
>   evidence chain is a concrete first artefact for the 61-point gap between those numbers, and
>   `aegis-integrity`'s **venue-guideline checks (IEEE, ACM, Elsevier)** fit the
>   research-integrity remit of the regional university sector better than a K-12 framing. The
>   Observatory partners (CENIA, CETIC.br, Ceibal, Tec de Monterrey) are the convening table for it.
>
> 🔴 **The one thing not to sell in any region: an AI-authorship verdict.** The best artefacts in
> this category refuse to make that claim (`intel/trends.md` trend 9), and a client who asks for it
> should be sold the evidence chain instead.

### North America

### 🟢 The OIDC half of every district LTI integration now has a permissive, maintained answer — and it is the same house as the record store (added p333)

🔵 **p330 recorded the dead-Python-LTI risk, p331 answered the launch surface with `lti-tool` (MIT). The auth substrate under both was still unnamed.** 🟢 **It is named now, verified first-hand p333, and it is North American:** [`yetanalytics/pedestal-oidc`](https://github.com/yetanalytics/pedestal-oidc) (**Apache-2.0**, 11,357 B · 123 c · 5 a · head **2026-10-16**) and [`yetanalytics/re-oidc`](https://github.com/yetanalytics/re-oidc) (**Apache-2.0**, 11,357 B · 70 c · 4 a · head **2026-10-16**) — server side and browser side of the same flow. **LTI 1.3 launch is an OpenID Connect flow, so this is not an adjacent nicety; it is the layer the launch sits on.**

🟢 **Commercially the point is the house, not the rows.** Yet Analytics is the **xAPI / Learning Record Store** vendor, and `yetanalytics/lrsql` was verified this pass as **Apache-2.0**. 🔵 **A district engagement can therefore be quoted end-to-end on permissive, maintained, US-maintained components: LTI 1.3 launch (`lti-tool`, MIT) → OIDC both halves (Apache-2.0) → xAPI record store (`lrsql`, Apache-2.0)** — with the LMS itself (Moodle GPL-3.0, Canvas commercial) left where it is, unforked.

🔴 **Still unoccupied, and now a two-pass-old finding: Ed-Fi.** The North American data standard is live and its open tooling is stale (`esegrave/edfi`, Apache-2.0, head 2022-03-04). **Nothing changed this pass.**

🟡 **Three NA items surfaced on the search channel this pass that this KB does NOT already hold, recorded as UNVERIFIED leads rather than findings:** **Illinois SB720** (reported to align district AI procurement with state guidance), the **EDSAFE AI Alliance** (a US framework body this corpus has never mentioned), and a reported **424-district study finding that AI-policy quality tracks district wealth** — a procurement-inequality argument with obvious relevance to a studio selling to districts. 🔴 **All three are search-channel-only: `ilga.gov`, `edsafeai.org` and `future-ed.org` each returned `000` at CONNECT from this environment this pass, and `WebFetch` returns `ENOTFOUND`.** **Confirm at source before any of the three enters a proposal.**

### 🟢 The dead-LTI risk line p330 put in your bid now has a named, live, US-backed answer (added p331)

🔴 **p330 wrote the risk honestly: every district integration in this region sits on `pylti1.3`, and it has not been touched since 2022-11-21.** This pass **confirmed that on a second channel** — `PyLTI1p3` 2.0.0 was uploaded to PyPI on **2022-11-20**, one day before the last commit. **The library is dead on both the commit record and the release record. The risk line stands.**

🟢 **What changes is that the migration target is now named, measured and placed in this region.** `lti-tool/lti-tool` — 🟢 **MIT** (1,077 B, read first-hand p331), **346 commits · 6 authors · head 2026-10-19**, with **235 of those commits in 2026 by 6 authors**, and `@lti-tool/core` **v1.3.1 published 2026-10-20 — the day of this pass**. Complete LTI 1.3 Advantage surface confirmed in code: launch, **AGS**, **NRPS**, Deep Linking, **Dynamic Registration**, JWKS.

🟢 **It is placed in North America institutionally, not by inference.** 161 of 346 commits at `-0400` and 62 more at `-0500`, and the third author domain is **`longsight.com` — 28 commits — Longsight Inc., a US Sakai/Tsugi hosting firm.** 🔵 **This KB already holds `LongsightGroup/qti3` (MIT).** **An LMS-hosting company in this region commits to this library. That is the sentence that de-risks the migration in a bid.**

🟢 **And its shape clears this region's three binding constraints without an architecture argument** — which is the actual commercial point:

| constraint, already held in this file | why `@lti-tool/core` clears it |
|---|---|
| **California AB 1159** — student data may not train AI models | 🟢 The library is an **integration layer, not a model**. Nothing in `zod` + `jose` trains on anything |
| **Oklahoma / Maryland** — human oversight required, no AI decisions on high-stakes outcomes | 🟢 **AGS writes the score the human approves.** The gradebook hop is explicit and auditable in `scoreSubmission.schema.ts` |
| **NYC** — one-year moratorium on student-facing AI through grade 8 | 🟢 **Teacher-facing deployment needs the same LTI launch and no student surface.** The integration is sellable inside the moratorium |

🟢 **The bid, concretely:** quote the `pylti1.3` → `@lti-tool/core` migration as a **named, dated de-risking line item** with a two-package dependency surface (`zod`, `jose`) against the 10-package closure this KB payload-verified for `ltijs`. 🔵 **A district CIO can be shown two release dates — 2022-11-20 and 2026-10-20 — and needs no further argument.**

🔴 **Gap, declared rather than left silent: no procurement vehicle or contract notice was found for this region this pass.** The news leg returned only material this file already holds (134 bills / 31 states, AB 1159, Idaho SB 1227, H.R. 8747, the NYC moratorium, Canada's "AI for All" of 2026-06-04). **The cooperative-purchasing route p329 named — Sourcewell, OMNIA Partners, NASPO ValuePoint — remains this region's only recorded vehicle and remains unverified at source, because every procurement host tested at p329 answered 403 at CONNECT.**


### 🔴 The Python LTI dependency under every district integration is dead, and that is a risk line in your bid (added p330)

**Measured first-hand at p330 on the git channel: `dmitry-viskov/pylti1.3` — the MIT LTI 1.3 Advantage library this KB has recommended since p319 as *"the repo that gets your agent into the client's existing LMS"* — has no commit on any branch or tag since `2022-11-21`.** 178 commits, 16 authors, newest tag `2.0.0` the same day, final substantive commit *"Support Python 3.11"*. `openfun/django-lti-toolbox`, the other permissive Python option, is dead since `2024-11-14`.

🔴 **Why this is a North America opportunity note and not just an engineering one.** This is the region where the LMS is the integration point: Canvas, Schoology and PowerSchool sit between a district and anything a studio ships, and **cooperative purchasing (p329) makes the integration the reusable asset** — win one district, become buyable by every member, and the LTI layer is what carries across. 🔴 **A proposal that names an abandoned library as the integration path is a proposal whose maintenance cost lands on the studio in year two.**

🟢 **The three honest options, to state in the bid rather than discover in week six:**

| option | when it fits | cost |
|---|---|---|
| **Put the LTI boundary in PHP** — `tsugiproject/tsugi`, Apache-2.0, 4,012 commits, **47 authors**, committed 2026-10-19, with `LTI13.php`, AGS, NRPS and Deep Linking **under unit test** | the client already runs PHP, or the boundary can be a thin separate service | 🟢 lowest — the only living, complete, permissive LTI implementation in this KB. 🟡 three authors in 2026; bus factor near one |
| **Put it in TS** — `Liberate-Labs/ltikit-sdk`, 🟢 **MIT** (1,063 B, read first-hand p330), `ags.ts`/`nrps.ts`/`deep-linking.ts` each with tests, Dynamic Registration, cookieless launches, serverless/edge | the stack is JS/TS, or the deployment target is edge | 🟡 **fork and pin.** 38 commits, **one author**, last `main` commit 2026-07-10 and it is an **ownership handover**; seven dependabot branches unmerged |
| **Fork `pylti1.3`** | Python is non-negotiable and the client will fund maintenance | 🔴 highest — you now own an LTI implementation |

🔵 **And the procurement framing that makes this sellable rather than alarming: the client's incumbent vendor has the same problem and has not told them.** **A bid that prices the integration layer honestly, names the library, and shows the commit date is doing diligence the incumbent did not.**

🟢 **One artefact added this region this pass:** `Gchism94/jupyterquest` — **MIT**, a `.ipynb` autograder with CI, Codecov and a **Zenodo DOI**, placed **North America institutionally from the commit record** (`gchism@arizona.edu`, University of Arizona). 🔵 **The DOI is the detail that matters in a US higher-ed bid: it is what a research office and an IRB ask for, and almost nothing in this KB has one.** 🟡 Five months quiet (last commit 2026-05-07).

🔵 **It also fits the region's binding constraint directly.** California **AB 1159** bars using student data to train AI models, and Oklahoma and Maryland require human oversight with no AI decision-making on high-stakes outcomes. **An autograder that runs locally over notebooks the institution already holds, with a citable method, is the shape that clears all three without an architecture argument.**

### 🟢 The procurement route, named for the first time: cooperative purchasing — win once, become buyable by every member district (added p329)

🔴 **Read the confidence line before quoting any of this: every source below is SEARCH-CHANNEL-ONLY.** Not one procurement host is
reachable from this session — `marketbrief.edweek.org`, `govtech.com`, `791coop.org`, `createyourrfp.com`, `govspend.com` and
`aasa.org` all answer **403 at CONNECT**. **No notice number, value or date below is verified at source.** Each is recorded precisely
enough that confirming it is one lookup on the buyer's own portal, not one search.

🟢 **The mechanism, and it is the finding this region was missing.** A **purchasing cooperative** runs **one** competitive
solicitation, awards a contract, and its member agencies then buy off that contract **without each running their own RFP**.
🔵 **This inverts the sales motion: you do not win 13,000 districts, you win one cooperative solicitation and become buyable by all of
its members.** **Named vehicles: `Sourcewell`, `OMNIA Partners`, `NASPO ValuePoint`** — none of which this file had ever recorded.

| vehicle | detail | why it matters |
|---|---|---|
| **791 Purchasing Cooperative** | **RFP `791202603005`, "AI Services and Solutions for Government"**, led by the Central Texas Council of Governments; scope includes school districts | A live, named, **AI-scoped** cooperative solicitation that reaches districts |
| **California Ed Tech Joint Powers Authority** | **RFP No. 25/26-01** for AI platforms. 🔴 **Dated 2025-07-28 — 2025, not 2026.** Builds a **portfolio of pre-vetted vendors rather than picking one winner**; scope includes tutoring | 🟢 **The model to design a bid around: not winner-take-all, so a specialist studio can get onto the list rather than having to beat Google** |
| **ESC Region 19 / Allied States Cooperative** | 2026 consulting and instructional-resources award, includes an AI vendor | Another buy-off-it vehicle |
| **Digital Promise** | USD **8M** RFP for AI tutoring solutions. 🔴 **Nonprofit, not a state agency; single secondary source, blog-dated 2026-06-04** | 🔴 **The weakest row here. A lead, not a vehicle** |

🔴 **An informed gap, written down because silence would look like coverage: there is no 2026 state-education-agency AI-tutoring RFP in
these results.** SEA buying concentrates on **assessment, data systems, licensure platforms and programme evaluation**, and those
contracts post to the **state central procurement portal, not the agency's own site** — which is where the next pass should look.
### 🟢 The binding district mandate arrived, it is dated, and the first deadline has already passed (added p328)

🔴 **This region crossed from guidance into enforceable obligation during 2026, and one deadline is already behind us.** From the p328 sweep:

| instrument | what it binds | date |
|---|---|---|
| **Ohio** — district AI-use policy mandate | **every district must have adopted an AI use policy** | 🔴 **2026-07-01 — already past** |
| **Idaho S.B. 1227** | district policies **+ AI literacy standards** | signed **2026-03** |
| **Oklahoma S.B. 1734** | **parent opt-out rights** + **teacher review of AI output** | 2026 session |
| **Maryland S.B. 720** | state guidance, **teacher professional development**, district tool-evaluation support | 🟡 **status contested** — one source reports signed and effective 2026-06-01, another reports it only passed one chamber |
| **California A.B. 1159** | would **bar using student data to train AI models** unless it directly benefits the school | proposed |

**Coverage: roughly 33–35 states plus Puerto Rico now issue official AI-in-education guidance, up from about 28 in early 2025.**

🟢 **The opportunity, and it is a different sale from the one this file has been describing.** A mandate to *have a policy* is not a mandate to have a *good* one, and the sweep's own finding is that **most current proposals do not require vendors to disclose how outputs are generated, or to show that a tool was tested for bias or accuracy.** 🔵 **So the districts that met the Ohio deadline bought a document, and nobody checked whether their tools comply with it.** That is a **conformance-gap engagement**: take the district's adopted policy as the specification, audit the deployed AI estate against it, and produce the evidence the policy implies but did not require. **It is sellable to a client who believes they are already done, which is the easiest procurement conversation in this region.**

🟢 **And the artefact to build it on is now permissive.** `eai6/ai-tutor` (**MIT**, p328) ships `ConsentRecord` with a **`parental` consent type and a `withdrawn_at` timestamp**, plus `export_user_data` / `delete_user_data` commands — **exactly the mechanics Oklahoma's opt-out and California's data-use restriction ask for**, and the first time this KB has held them under a licence that can enter a deliverable. 🔵 **Pair it with `anthropics/k12-teacher-skills` and `learning-commons-org/agent-skills` (both Apache-2.0, both now on the `agents/top.md` shelf) for the teacher-workflow layer.**

### 🟢 The standards spine is now a commodity here — move the bid up a layer (added p327)

🔴 **What changed: a US client can get the curriculum-standards layer for free, and may already
have it.** `learning-commons-org/knowledge-graph` (MIT code, Open datasets typically CC BY 4.0,
161 ★, v1.15.0 of 2026-10-14) publishes **US academic standards by state with state↔CCSS
crosswalks**, and the companion skills ship inside **Claude for Teachers** with a connector
claiming **all 50 states**. 🔵 **Any North America proposal whose first phase is "build a standards
and curriculum data model" is now quoting for something available under CC BY 4.0 with an MCP
server in front of it.**

🟢 **Where the money moved to, in order of defensibility:**

1. **Evaluation and acceptance criteria.** `learning-commons-org/evaluators` (MIT code, 19
   evaluators, 289 commits) gives a district a *measurable* definition of acceptable AI output —
   grade-level appropriateness, revision actionability, **withholding answers**, tone. 🟢 **Sell
   the acceptance-gate design, not the generator.** 🔴 **The annotated corpora are CC BY-NC-SA
   4.0: re-annotate against the client's own materials, which is billable and defensible.**
2. **Gated-content negotiation and integration.** IM® v.360 instructional + assessment materials
   and OpenSciEd are **Gated**. 🔵 **A client who wants curriculum-aligned generation against the
   curriculum they actually bought needs a publisher agreement and an integration — that is the
   scope item, and it is not an open-source task.**
3. **The policy-gating layer, unchanged and still the hard requirement.** P3, P7 and P9 already
   carry parent consent as state, grade-band gating, teacher-only mode and the COPPA disclosure
   boundary. **The free spine does not touch any of it.**
4. **Retention and completion evidence.** `datakind/student-success-tool` (MIT, 3,015 commits,
   John Jay College CUSP, funded by Google.org) and `autolab/Autolab` (Apache-2.0, CMU, 2,179
   commits) are the two US-institution-deployed artefacts promoted at p327. 🔵 **Buyers are asking
   for evidence of persistence gains; these are the starting points with a named campus behind
   them.**


#### Illinois HB 316 — promoted out of `intel/policy-matrix.tsv` into this file (p326)

**It has been in this KB's policy matrix and never in the market prose, which is where a studio
lead actually reads.** **HB 316 requires AI literacy instruction for grades 6–12 statewide and
takes effect 2026-08-01** — reported to have become law without the governor's signature. 🟡
**Single-source and secondary**; the matrix row carries the same caveat. Verify against the
Illinois General Assembly before quoting it in a bid.

🟢 **Why it is worth promoting now rather than at re-verification:** it is the **fourth** US
jurisdiction in this file on the *literacy* motion — with **California AB 2876**, **Utah H.B.
273** and the Georgia/Mississippi CS-credit route — and p320 separated that motion from the
*guardrail* motion precisely because they land with different budget holders. **As of this pass
the literacy motion has a sequenced, commercially licensable, age-banded curriculum asset behind
it** (`withmarbleapp/os-taxonomy`, 21 AI topics, ages 5–11, ODbL + CC BY-SA). 🔴 **Mind the gap
in the gap: HB 316 is grades 6–12 and the open asset stops at age 11.** The spine is real; the
upper-secondary extension is scope, and should be priced as scope.

> **Pass 323 — the regional search produced new primary-ish detail on the statute layer, and it
> sharpens P3 rather than changing it.** Three items are new to this file and one existing item is
> now dated precisely:
>
> - **Oklahoma SB 1734, the restrictive one, now with its dates and its duties.** Signed by Governor
>   Stitt **2026-05-12**, effective **2026-07-01**. Instructional AI must be **educator-directed with
>   human review**, and **high-stakes decisions — grading and discipline — cannot rest mainly on AI**.
>   **Districts must adopt written AI policies before the 2027-28 school year**, and parents get an
>   **annual notice listing AI tools, vendors and collected data**, with an opt-out **without
>   academic penalty**. That is a dated procurement trigger with a named deliverable: the annual
>   tool-and-vendor disclosure is a document somebody has to produce, and it is pattern **P9**
>   Stage 1 output.
> - **Maryland SB 720 (Ready Schools Act)** — signed **2026-05-26**, effective **2026-06-01**;
>   requires state AI guidance **and an AI coordinator in each local school system.** A named human
>   role per district is a buyer this file did not previously have a title for.
> - **Idaho SB 1227** — signed **2026-03-26** per one tracker, and **the statewide generative-AI
>   framework was approved in August 2026** with companion standards still pending. **Bars AI from
>   replacing human teachers.** The "framework approved, standards pending" state is the window in
>   which a governance layer gets specified.
> - **Still pending, not enacted: South Carolina H. 5253** — opt-**in** parental consent, annual
>   disclosure of tools and vendors, and **meaningful human review before automated disciplinary or
>   placement decisions** — **in committee** as of this pass. This file has flagged the opt-in
>   posture twice; it has still not passed.
> - **Volume, with the disagreement recorded:** one tracker reports **68 bills across 27 states and
>   10 enactments in 2026**; another reports only three states with enacted K-12 AI statutes while
>   itself listing more. **The counts in this sector's trackers do not reconcile** — quote the named
>   statutes, which do, and not the totals. Curriculum-mandate enactments named this pass: **Alabama
>   H.B. 329** (AI-inclusive computer-science graduation requirement), **Utah H.B. 273** (AI in CS
>   standards plus supervised **"AI sandbox"** courses), **Virginia H.B. 1186** (pilot programme plus
>   guidance with district policies).
>
> **What does not change: the buyer is still the governance layer, not the tutor.** What changes is
> that three of these statutes name an artefact — a written district policy, an annual
> tool-and-vendor disclosure, a district AI coordinator's operating framework — and **artefacts are
> easier to price than principles.**


1. **Compliance-as-the-product.** Ohio's 2026-07-01 deadline, Idaho SB 1227, Oklahoma/Maryland
   human-oversight rules and 134 bills across 31 states create dated, budgeted need: districts must
   adopt a framework and prove human supervision. Sell the governance layer — audit logging,
   human-in-the-loop gates, parent disclosure, FERPA/COPPA-safe retention — not the tutor. Pattern
   P3.
2. **Restriction is a product requirement, not a lost market.** NYC's K-8 moratorium and Katy ISD's
   K-6 ban mean any district product needs enforceable **age and grade-band gating** and a
   teacher-facing-only mode. A tutor that cannot be switched off for a grade band is unbiddable in
   those districts. Build the gate; it is cheap and it is a differentiator.
3. **COPPA remediation is a dated, in-force, unbudgeted liability — and the most sellable finding
   of this pass.** Full compliance with the amended Rule has been required since **2026-04-22**.
   Any K-12 product already deployed that forwards a pupil's prompts to a third-party model
   provider is making a third-party disclosure, and **§312.5(a)(2) requires separate verifiable
   parental consent for it** — consent to use the product does not cover it. Add the retention
   limits, the written published retention policy and biometrics-as-PII, and most district AI
   deployments shipped in 2025 are now out of compliance in a way nobody has audited. The offer
   writes itself: **a COPPA posture review of what the district already runs**, then the
   remediation — consent separation, retention enforcement, and where the answer is to stop
   disclosing at all, the on-premise swap (Moodle's Ollama/LiteLLM provider route, or pattern P5's
   offline stack). This is near-term, scoped, and it sells into the installed base rather than
   competing with a frontier-model seat licence.
4. **The Ed-Fi / OneRoster data spine.** Apache-2.0, standards-body maintained, and now verified
   (`repos/foundations.md`). Every district engagement needs roster and SIS sync; this is the
   first pass where that is a build-on-open-source line item rather than bespoke integration.
   Pattern P6.
5. **Teacher enablement at scale, and the trend is now negative.** Only 17% of US and Canadian
   students think their instructors can guide them on AI, the lowest of any region, against 64% of
   faculty having had training — training exists and is not landing. **And NA faculty intent fell
   9 points this year (76% → 67%), the only region going backwards.** Enablement here is no longer
   a capability sale; it is a trust-recovery programme, and it should be scoped and priced as one. `ai-agents-for-beginners` (MIT, 77.5k ★) and
   `education-agent-skills` (878 ★, CC BY-SA 4.0 — check the ShareAlike terms) are licence-clean
   bases to white-label, but the sellable work is redesigning the programme, not sourcing content.

6. **Human review and a parent opt-out are now statutory features, not differentiators — NEW.**
   Oklahoma's 2026 law permits AI only under educator supervision with human review, bars it from
   high-stakes student decisions and requires parent disclosure; one tracker adds **a parent
   opt-out with a duty to provide alternative access to core instruction.** Idaho, Maryland and
   Virginia require state guidance plus aligned local board policies. **Three concrete build items
   follow**, and all three are cheap next to the cost of losing a bid: a **per-pupil opt-out flag
   that degrades gracefully** (the pupil still gets the instruction, without the AI path); an
   **approval queue** so no AI output reaches a student or a record without a named educator
   signing it — the shape `JaimeArriagadaRosas/Plugin-Feedback-Canvas` implements and cannot
   license (`agents/top.md`); and a **decision log** proving no high-stakes determination was
   AI-made. Build them once, reuse them in every district.
7. **"Prove it teaches" is now a sellable, defensible offer — NEW.** The evaluation layer exists
   (`agents/top.md`): MathTutorBench (EMNLP 2025), AITutor-EvalKit (MIT, MBZUAI) and two
   pre-registered MIT audits whose finding is that **LLM-judged helpfulness can reward answer
   leakage** and that **difference-in-differences on a bounded rating scale can manufacture an
   effect.** Every competitor's uplift claim in this market is built on exactly the instrument
   those audits discredit. **An engagement that pre-registers its comparison, freezes and hashes
   its data, keeps a decisions log and reports what MathTutorBench measures is doing something no
   vendor deck in this sector does** — and in the most-regulated market, where faculty trust is
   falling (17% student confidence, intent down 9 points), credibility is the product.

### EMEA

### 🟡 The EU deferral is confirmed on a fourth sweep — and this pass adds nothing to it, which is the point (added p333)

🔵 **The search leg for EMEA returned, again, Regulation (EU) 2026/1744 moving Annex III high-risk education systems from 2026-08-02 to 2027-12-02, the AI-literacy duty live since 2025-02-02, Article 50 transparency from 2026-08-02, and emotion recognition in education prohibited.** 🟢 **This KB already holds every one of those** — `2026/1744` appears 10 times in this file, `2027-12-02` 14 times, `Annex III` 15 times, and the correction that fixed the date is p328's. **Fourth independent sweep, no new fact.**

🟢 **Recorded as a measurement rather than a shrug: the EMEA regulatory leg is SATURATED for this KB, and a saturated leg is a reason to change the query, not to re-run it.** 🔵 **The next EMEA question is not "what does the AI Act say" — it is answered — but "which national transposition or framework is a nameable buying VEHICLE", which is the shape p329 proved worked (GÉANT OCRE 2024, 39 countries, direct award available).** **That is the query the next pass should run here.**

🔴 **The sovereignty leg returned nothing at all.** Queried explicitly for EU-hosted infrastructure, data residency and the procurement of non-EU AI vendors for schools, the channel returned only AI Act commentary. 🟡 **This is an INFORMED GAP, written down so it is not mistaken for coverage:** this KB cannot currently place European data-residency requirements for education AI, and the sovereignty argument that EMEA buyers reportedly care about is the one it has least evidence for.

### 🟡 The EU deferral is confirmed on a third sweep, and this file's publication date for it is off by sixteen days (added p331)

🟢 **The substance is unchanged and now corroborated a third time, independently: Annex III stand-alone education obligations bite on 2027-12-02, not 2026-08-02.** p328 caught the move, p331's EMEA leg reproduces it from a fresh set of sources, and **every source this pass agrees on the deadline**.

🟡 **The correction is narrow and it is to this file's own metadata, not its conclusion.** `intel/policy-matrix.tsv` records *"published as Reg. (EU) 2026/1744 of 2026-07-08."* **This pass's sources give the Official Journal publication as 2026-07-24 and entry into force as 2026-07-27.**

| datum | this file carried | p331 sources | status |
|---|---|---|---|
| instrument | Reg. (EU) 2026/1744 | Reg. (EU) 2026/1744 | 🟢 agrees |
| Annex III education deadline | **2027-12-02** | **2027-12-02** | 🟢 agrees — three independent sweeps |
| Annex I embedded deadline | 2028-08-02 | 2028-08-02 | 🟢 agrees |
| OJ publication | **2026-07-08** | 🟡 **2026-07-24** | 🟡 **CONFLICT — 16 days** |
| entry into force | not recorded | 🟡 **2026-07-27** | 🟡 **new, unverified at source** |

🔴 **Neither date is verified at source, and the reason is recorded: no EU host in this session's reach answers.** **Both are search-channel figures.** 🟢 **The resolution costs one lookup on EUR-Lex by CELEX number and should be spent before any client-facing compliance date is quoted** — the deadline is safe to quote today, the publication date is not.

🟢 **Three things in the same instrument that are NOT deferred, and they are the near-term sales surface:**

- **Art. 50 transparency** — unmoved, in application. **This file already records a source disagreement on its exact date (2026-08-02 vs 2026-11-02); that disagreement is still unresolved and is still recorded rather than resolved.** Either way it is **already live**.
- 🔴 **Two new Art. 5 prohibitions phase in on 2026-12-02** — **six weeks out.** New this pass; this file had not recorded them. **Education-relevant because emotion inference in educational settings is the Art. 5 limb this sector touches.**
- 🟡 **Art. 4 AI-literacy duty relaxed** — from a hard obligation to *"take measures"* for staff. **Softer, not gone, and it is the cheapest compliance deliverable in the region: a staff AI-literacy programme is now a measure you can evidence rather than a bar you must clear.**

🟢 **The commercial read: a ~14-month build window on assessment and admissions products, and two compliance deliverables sellable this quarter** — an Art. 50 transparency review and an Art. 4 staff-literacy programme — **while Annex III conformity work is scoped against 2027-12-02.** 🔵 **Lead with the near dates. The deferral is a planning fact, not a reprieve, and a client who hears only "2027" will under-scope the December 2026 prohibitions.**


### 🟢 Switzerland's Openki is the healthiest open education codebase in this KB, and the accessibility gap here has a name and no artefact (added p330)

**Two EMEA findings this pass, both first-hand, and neither came from the regional query set.**

🟢 **One: `Openki/Openki` — measured for the first time, because `git clone --filter=blob:none` turns out to answer 200 against `gitlab.com` as well as GitHub.** **12,988 commits · 88 authors lifetime · 1,580 commits in 2026 from 19 distinct authors · last commit 2026-10-19.** **Placed EMEA/Switzerland first-hand** — `cis.ch` is the third-largest author domain at 1,759 commits, and 2026 commit offsets are overwhelmingly `+0200`/`+0100`.

🔵 **Nineteen people committing in one year is without parallel in this base.** Tsugi: 3 authors in 2026 on 486 commits. RosarioSIS: 3 on 332. **Openki is the only artefact here whose contributor base would survive losing its lead maintainer** — which is the single question a European public buyer asks about open source and the one this KB has had no good answer to. 🔴 **Two limits, both load-bearing: it is AGPL-3.0, so §13 reaches the users of a hosted service, and it is a course-organisation platform — who teaches what to whom, where and when — not an LMS and not a SIS.** 🟢 **Propose it as the community-learning and scheduling surface, and cite its contributor base as the sustainability evidence in a bid that has to argue open source is not a single-vendor risk.**

🔴 **Two: the accessibility gap is now named, and the artefact that would have filled it does not exist.** The search channel returned `projectremedy-ai/remedy-canvas-lti` with a full description — *"Canvas LTI 1.3 tool that scans entire courses for WCAG 2.2 AA accessibility issues and remediates them in-place"* — and **`raw` 404s and the clone fails.** 🟡 **The gap behind the invention is real and is an EMEA buying trigger specifically: the European Accessibility Act applies to services in the member states, and public-sector bodies are already under the Web Accessibility Directive.** 🔵 **This KB's earlier WCAG sweep found permissive accessibility agents, and they remediate *software* — they review code for a developer.** 🔴 **Nothing here remediates *course content* inside an LMS**, which is what a university's accessibility office is actually liable for. **A named absence, carried as a build opportunity rather than a shelf row.**

🟡 **Two further EMEA placements from the commit record, recorded for completeness:** `francoisjacquet/rosariosis` (**EMEA**, `rosariosis.org`, `+0200`/`+0100` — 8,034 commits, 332 in 2026, GPL-2.0 by payload) and `afri-bit/revibe` (**EMEA**, all commits `+0200`; 🟡 the author's name is Indonesian, so this places the work and not the person). **`artcc/freelingo` is placed EMEA on the weakest evidence in this file — a Spanish personal name on 1,064 of 1,168 commits, no institution declared — and is labelled inferred everywhere it appears.**

🔴 **The caveat that bounds this whole region, new this pass and permanent until the environment changes.** `forge.apps.education.fr` — the French Ministry of Education's own forge — and `gitlab.opencode.de`, Germany's public-sector code platform, both answer **`000`**, along with eleven other self-hosted instances, while `gitlab.com/api/v4` answers **200** in the same session. **This is a host allowlist, not a protocol limit.** 🔵 **The European public sector runs its education code on sovereign forges by policy, so the artefacts an EMEA buyer most likely already operates are precisely the ones invisible here.** **Every EMEA count in this file is a floor. State that in an EMEA bid instead of implying the search was exhaustive — the buyer knows their forge exists and will notice if your map does not.**

### 🟢 GÉANT OCRE is the route into European universities, and a cancelled €160M Irish framework is a near-term opening (added p329)

🔴 **Confidence, first: every source below is SEARCH-CHANNEL-ONLY.** `find-tender.service.gov.uk`, `geant.org`, `ocre-project.eu`,
`nwupc.ac.uk`, `crescentpurchasing.co.uk` and `irishtimes.com` all answer **403 at CONNECT / 000**. **Nothing below is verified at
source.** Notice IDs are recorded so confirmation costs one lookup.

| vehicle | detail | why it matters |
|---|---|---|
| 🟢 **GÉANT OCRE 2024 framework** | Pan-European framework for **IaaS / PaaS / SaaS** to research and education institutions. Began **2025-02-03**, runs to **2030-02**. **39 participating countries.** Routes: **direct award**, mini-competition, desktop mini-competition | 🟢 **The single most useful procurement fact for an EMEA education engagement. An eligible institution can DIRECT-AWARD off this framework — no new tender.** This is the EMEA analogue of North America's cooperative purchasing, and this file had never recorded it |
| **UK DfE — "AI Tutoring Tools for Education"** | **Preliminary market engagement** notice (pre-tender), Department for Education (England). **~£1.5M ex VAT**; estimated contract **2026-06 → 2028-05**, possible extension. Find a Tender notices **014992-2026** and **013464-2026** | 🟢 **A named national buyer shaping an AI-tutoring specification BEFORE tender** — the window in which a studio influences requirements rather than responding to them. Schools and academy trusts then buy via **DfE-reviewed frameworks**, so the framework is the real gate |
| **Crescent Purchasing Consortium** | Open framework, education professional services, published **2026-02**. Its **SEND advisory lot explicitly covers AI in education systems** — adaptive testing, feedback tools | An **already-open** UK vehicle whose published scope names AI adaptive testing |
| 🟢 **Ireland — €160M FET framework, CANCELLED** | Multi-supplier framework for further education and training services **collapsed before award over process "anomalies"** (reported **2026-03-05**). ETBs may run **interim local arrangements** until a new national framework exists | 🟢 **A cancelled national framework is an OPENING, not a closure: interim local buying, smaller lots, less competition — and a national re-run to position for** |
| **NWUPC** | North Western Universities Purchasing Consortium (UK HE). **Its listed frameworks are not AI-specific and the frameworks page does not mention AI** | 🔵 **Recorded as a NEGATIVE deliberately.** A named consortium with no AI vehicle is a gap a studio can point at — and a reason the OCRE route matters more |

🟡 **One genuinely new regulatory date, and it is the only thing the prescribed EMEA sweep added.** **EU AI Act Art. 57 national
regulatory sandboxes are deferred to `2027-08-02`** by the Digital Omnibus. 🔵 **Everything else the sweep returned, this file already
holds with better precision than the snippets had**: Annex III → `2027-12-02`, Annex I → `2028-08-02`, Regulation (EU) **2026/1744**,
OJ **2026-07-24**, in force **2026-07-27**, Parliament **2026-06-16**, Council **2026-06-29**, Article 50 and Article 4 live now.
🟢 **A third-party source independently reached this file's own framing** — *"December 2027 is not a snooze button"* — which is
corroboration of the sales argument at line 989, not new information.
### 🟢 The region's reference implementation is now MIT, it was funded multilaterally, and it ships the consent layer (added p328)

🟢 **`eai6/ai-tutor` — MIT, 1,090 B grant read first-hand, *"Copyright (c) 2026 World Bank Group and contributors"*, seeded with a Seychelles curriculum (7 geography + 8 mathematics units).** It is the find of p328 and it is placed in this region.

**Why it changes the EMEA conversation specifically:**
- 🟢 **It is the first permissive artefact in this KB that ships a GDPR layer as code rather than as documentation.** `apps/safety/models.py`: `ConsentRecord` with a **`parental`** type and a `withdrawn_at` timestamp, `unique_together` on (user, consent_type); `SafetyAuditLog` with a **pseudonymised 16-char `user_hash`**, `consent_given` / `consent_withdrawn` event types and a `severity` field; management commands `export_user_data`, `delete_user_data`, `safety_cleanup`. 🔵 **Consent withdrawal as a first-class timestamped event, and pseudonymisation at the log layer, are the two things a DPO asks for and an edtech pilot never has.**
- 🟢 **It answers the sovereignty question without a port.** `local Ollama` is a first-class provider alongside Claude, GPT, Gemini and Azure OpenAI, **so "no student data leaves the jurisdiction" is a configuration change.** Combine with `open-edge-platform/education-ai-suite` (Apache-2.0, Intel, OpenVINO) for the no-GPU variant.
- 🟡 **It is an Africa-placed artefact in a region this KB has mostly covered through the EU.** Seychelles is a **small island developing state**, and the repo's `seed_seychelles` command plus its *"local context"* pedagogy principle (examples adapted to Seychelles geography and culture) make it **a localisation template, not just a codebase** — which is the shape of a ministry engagement across the African Union's education ministries.

🔴 **Two caveats that must travel with this row into any bid.** (1) **The World Bank affiliation is self-declared** — copyright line and contributors list name the World Bank Education Team, but the repository sits in a **personal namespace**, and `github.com`, `api.github.com` and `worldbank.org` were all unreachable this pass, **so the institutional link is uncorroborated.** Say *"MIT, with the World Bank Group on the copyright line"*; do not say *"a World Bank project."* (2) **The announced Seychelles national programme appears to be a different stack** — a World Bank 2026 Annual Meetings transcript has a Seychelles minister describing a rollout built on a **proprietary Grok tutor**. 🔵 **That gap — open artefact here, proprietary procurement there — is the sale, not an objection to it: the open stack is what a ministry can be shown, audited and handed.**

🔴 **And the date correction above is an EMEA correction: the Annex III high-risk deadline is reported moved to 2027-12-02. Re-scope the EMEA compliance pitch to Art. 4 literacy and Art. 50 transparency, which have not moved.**

### 🟢 The integrity layer has a maintaining university behind it — and it is a procurement answer, not a feature (added p327)

🟢 **`dodona-edu/dolos` — MIT, 1,083 B licence read first-hand at p327, 352 ★, 48 forks, 3,838
commits, Ghent University / Team Dodona.** The deepest commit history of any artefact promoted this
pass. 🔵 **This KB already holds `JPlag` and `jieplag`; `dolos` is the one with a European
university maintaining it, which is the difference between a tool and a citation in a tender
response.** Wire it into **P11** (the academic-integrity evidence chain — sell the audit trail,
never the verdict).

🟡 **The OECD *Digital Education Outlook 2026* is the EMEA-usable version of a position this KB has
been arguing from inference.** It states that generative AI supports learning **only under explicit
pedagogical design** and warns of **reduced cognitive effort and loss of teacher autonomy** from
general-purpose tools — and it reports **37% of lower-secondary teachers using AI (TALIS, 2024)**.
🔵 **Against an AI Act high-risk classification for admissions and assessment, an OECD citation
does work in a bid that a vendor blog cannot: it supports a purpose-built, pedagogy-designed system
over a general chatbot as a *compliance* argument, not a taste argument.** 🔴 **Search-channel
only — `www.oecd-ilibrary.org` answered 403 to CONNECT. Confirm at source before quoting.**

🔵 **Fully permissive EMEA stack, now assemblable with no copyleft seam:** OpenOLAT (Apache-2.0)
+ `learning-commons-org/agent-skills` (Apache-2.0) + `evaluators` (MIT code) + `dolos` (MIT). **The
only non-permissive element is the standards data, and in EMEA the standards are national rather
than CCSS — so the Learning Commons data tier does *not* port, while its agent and evaluation tiers
do.** State that distinction in any EMEA proposal that reuses a North America reference
architecture.


> **Pass 323 — the AI Act timeline was re-verified against an independent search channel and this
> file is correct.** Recorded because the deferral is the single most quoted and most misquoted fact
> in EMEA education-AI bids, and because a KB that holds a contested date should be able to say when
> it last re-checked it.
>
> - **Confirmed:** **Regulation (EU) 2026/1744** (the Digital Omnibus on AI) moved the **Annex III**
>   standalone high-risk obligations — education among them, with recruitment, credit scoring, law
>   enforcement and border control — from **2026-08-02 to 2027-12-02**, a 16-month deferral.
>   Published in the Official Journal **2026-07-24**, in force **2026-07-27**. **Annex I** embedded
>   products deferred to **2028-08-02**.
> - **Confirmed as not deferred:** **Article 4 AI-literacy** duty (live since 2025-02), the
>   **Article 5(1)(f)** ban on emotion recognition in educational institutions (live), and
>   **Article 50** transparency, which **applied from 2026-08-02** as planned — with the
>   **Article 50(2) marking grace period closing 2026-12-02**, alongside the new prohibitions landing
>   the same day.
> - **One nuance worth carrying into contract talks:** a law-firm reading holds that high-risk
>   systems placed on the market **before** the new application dates are caught **only if
>   substantially modified afterwards.** If that reading survives, "substantial modification"
>   becomes the operative term in every maintenance clause on an education AI system — **and a
>   continuously updated tutor is modification-shaped by construction.** Flagged, not asserted:
>   secondary-sourced.
>
> **The sales line stays exactly as this file already states it: "the AI Act is delayed" is a
> misreading.** What moved is Annex III. Literacy, the emotion-recognition ban and Article 50 are
> live now, and **2026-12-02 is the next real date**, not 2027.


**New at p321 — the EMEA public-sector stack is now named end to end, and it is mostly copyleft or
unlicensed.** Germany's publicly funded OER portal WirLernenOnline publishes its plumbing on GitHub
under the **`openeduhub`** organisation (67 repositories; `github.com/wirlernenonline` is a 404 and
was this KB's wrong guess for two passes). Read first-hand at p321: the platform
`edu-sharing/edu-sharing-community-repository` is **GPL-3.0 with 16,110 commits since 2007**; the
harvester `oeh-search-etl` has **1,397 commits and no licence file**; the metadata layer
`oeh-metadata-vocabs` is **CC0-1.0 with 938 commits**, carrying SKOS vocabularies for educational
context, level, discipline, school type, rights, cost, machine-readable quality criteria and the
**DigCompEdu, ESCO and EQF/DQR** competence frameworks; and two Apache-2.0 AI tools sit on top
(`tutor-chatbot`, `ki-prompt-benchmark`).

**The commercial read is the licence asymmetry.** The engineering-heavy layers are the unusable
ones; the permissive ones are a 938-commit *dataset* and two prototypes of 10 and 3 commits. So an
EMEA bid against a public OER buyer is **integration and extension work, not platform work** — and
the CC0 competency vocabularies are a genuine shortcut, because mapping a tutor's skill graph onto
DigCompEdu/ESCO/EQF is otherwise bespoke effort on every engagement. **This is also the EMEA answer
to the `bncc-dev` precedent LATAM has**: the data layer exists here, it is just German and
tagged under neither `bildung` nor `oer`.

**`tutor-chatbot` names a sovereign-inference path, which is the detail to carry into a pitch.** Its
provider options are **OpenAI or GWDG** (German academic compute), and `ki-prompt-benchmark` adds
**AcademicCloud**. A publicly funded buyer that must keep inference inside national or academic
infrastructure now has a working reference implementation to point at — see `intel/trends.md`.

**Pass 322 completes that EMEA picture, and the licence asymmetry p321 identified is sharper than
it looked.** All 67 `openeduhub` repositories were enumerated and sixteen read first-hand. The
portal has shipped a **twelve-service AI metadata pipeline** — ingestion, LLM extraction into
eleven schemas, a human-review canvas with per-field confidence, MinHash deduplication, Flesch and
Wiener readability scoring, Lighthouse accessibility and licence lookup, a Pyro Bayesian metadata
predictor, a Keras discipline classifier shipping its pretrained weights, bulk prompt running, a
factual-accuracy judge, and a unified gateway over the lot. **And the licences divide by layer:
119 commits of Apache-2.0 interaction shells plus a 519-commit Apache-2.0 API client, 790 commits
of GPL-3.0 analysers, and 1,852 commits — every model and every harvester — with no licence file
at all.**

**What that means commercially, stated plainly.** The permissive surface of Germany's publicly
funded education AI contains **none of its machine learning**. An EMEA bid can take the
`edu-sharing-python-client` (Apache-2.0, 389 generated operations, verified against edu-sharing
11.0) and the interaction layers, must keep the GPL-3.0 analysers behind a process boundary, and
**cannot ship the inference core at all** — so either reimplement it or open a licence conversation
with the operator. For a publicly funded body sitting on 1,852 commits of unlicensed public money,
**licence remediation is itself a sellable engagement**, and it is a cheaper first conversation than
a replatforming pitch. Per-repository detail is in `repos/foundations.md`; the README-versus-LICENSE
hazard that cost this pass four separate verifications is recorded there too.

**One more EMEA detail worth a pitch sentence.** The sovereign-inference path p321 found in two
prototypes is now visible in the production line as well: `metadata-agent-api` and
`metadata-agent-canvas` both ship a **B-API→AcademicCloud (`deepseek-r1`)** provider alongside
OpenAI. A buyer that must keep inference inside German academic compute has a working reference for
the *metadata* workload, not just the tutor demo.

1. **Provider-grade conformity packaging.** Under the AI Act the school is the deployer and the
   tool-builder is the provider; a Globant-built tutor inherits the heavier duty. Productise it:
   technical documentation, risk management, data governance and post-market monitoring shipped
   *with* the tutor. **2027-12-02 is the sales window, not a reprieve** — European public-education
   procurement runs 12–18 months, so conformity-ready wins 2026–27 bids.
2. **Three dated items that are live now, not in 2027.** Article 50 transparency (since
   2026-08-02): AI-interaction disclosure and machine-readable marking. The new prohibitions from
   **2026-12-02**. Article 4's relaxed-but-real duty to take AI-literacy measures for staff. Each is
   a small, immediate, billable remediation across existing EMEA deployments — and 2026-12-02 is
   six weeks out.
3. **Sovereign/on-prem tutoring, and it just got a licence-clean base.** Richie (MIT) + Open edX +
   self-hosted models keeps data in-region and avoids US hyperscaler dependency — the standing EMEA
   public-sector requirement. **New this pass: `OpenOLAT` (Apache-2.0, 448 ★, 31,877 commits) is a
   mature LMS built in Switzerland by frentix GmbH on the University of Zurich's OLAT** — the only
   EMEA-authored, EMEA-maintained, permissively licensed LMS in this KB. For a sovereignty-driven
   buyer it answers three objections at once: data stays in-region, the vendor is European, and the
   licence lets Globant link agent code directly instead of paying the LTI-boundary tax. See
   pattern **P8**.
4. **AI literacy as a billable programme, with a number behind it.** **73% of UK adults have had no
   AI education or training**, Article 4 obliges staff AI-literacy measures, and Denmark (€200M with
   education named), France and the Netherlands are funding educational AI nationally. The
   combination of a legal duty, public money and a measured skills deficit is the cleanest
   demand signal in EMEA that is not conformity work.
4. **The Gulf is the region's growth market and it is buying, not building.** UAE ~28% of GCC
   edtech on the back of National AI Strategy 2031; Saudi's Human Capability Development Program;
   Alef Education ranked 13th globally. All proprietary, all adaptive-learning-first. The opening is
   integration and localisation (Arabic-first tutoring, curriculum alignment) alongside incumbents,
   not displacing them.
6. **The Commission's own September 2026 reports name the deliverable — NEW.** "Friend or foe?"
   concludes that genAI's effect on learning **depends on how it is used** and that teachers need
   substantial initial and continuing development **supported by institutional guidelines for
   responsible use**; the Eurydice report finds digital competence in lower-secondary curricula
   almost everywhere but **standardised assessment of it uncommon**. That is a two-part brief —
   a teacher-development programme and an institutional guidance framework — published by the buyer
   itself, and the Commission's **education package with a 2030 Roadmap on the Future of Digital
   Education and Skills** is the budget line behind it. Pair it with the **AI Literacy Framework
   (AILit)** and the **2026 ethical-use guidelines for educators** as the artefacts a client will
   be asked to align to. *(Verify the package's date and AILit's status directly; both were
   unreadable this pass.)*
7. **Two EU-funded programmes are the partner route, not the competition — NEW.**
   **AI-ENTR4YOUTH** (JA Europe with Intel and the Commission, 10 countries, three years) and
   **DUAL.AI.TEACHer** (Erasmus+ Teacher Academy, €1.9M, 11 partners, 8 countries) are already
   running teacher and youth AI capability at national scale. A studio competes badly with free
   publicly funded training and partners well with it: **take the deployment, assurance and
   integration work these programmes do not do.**
8. **EMEA now has its own permissively licensed autograder, and it is institution-built — NEW.**
   `thm-mni-ii/feedbacksystem` (**Apache-2.0, 2,248 commits, Technische Hochschule Mittelhessen**)
   checks submissions automatically, returns the mistake with suggestions, and **aggregates common
   errors so lecturers can address them in class** — the feedback loop European higher education
   keeps asking for, already built, Apache-licensed, at 24 stars. With `smashburger-dev/argmin`
   (MIT + CC BY 4.0, 343 commits, a German-language AI course that runs offline in the browser),
   an EMEA engagement can now be assembled from EMEA-authored permissive components:
   **OpenOLAT + feedbacksystem + argmin + a Globant agent.** That is a sovereignty story told with
   software rather than hosting diagrams.
9. **Africa's evidence base is the strongest in the world for low-resource AI tutoring** — the World
   Bank's Edo State, Nigeria programme and EIDU in Kenya (~400k children) — and it is the clearest
   fit for the offline-first stack in pattern P5. Kenya's DigiSchool tablets are installed hardware
   looking for content.

### APAC

### 🔴 p332 prescribed naming the instruments; it was done, and the channel STILL returns enterprise press — so the defect is the channel, not the query (added p333)

🔵 **p332 diagnosed this leg precisely: *"The APAC channel is returning enterprise press instead of education policy, and that is a QUERY defect. Query the instruments by name, not the region by topic."*** 🟢 **The prescription was followed exactly.** The leg named **Korea's AI Basic Act**, **China's AI Plus education plan** and **Japan's MEXT guidelines** in the query string itself.

🔴 **It did not work, and the result is worth recording because it REFUTES p332's diagnosis.** What came back:
- 🟢 **Korea — the one genuine confirmation.** The **AI Basic Act took effect 2026-01-22**, with a grace period of at least a year before fines, and **education is explicitly inside its "high-impact AI" class** alongside healthcare, finance and employment. 🔵 **That is the commercially useful sentence: a tutoring or assessment system sold into Korea is high-impact by statute, not by interpretation.**
- 🔴 **China — nothing on the AI Plus education plan.** The channel returned the general regime (algorithm, deep-synthesis and generative-AI rules; the amended Cybersecurity Law in force 2026-01-01) and **no school-specific provision whatsoever**.
- 🔴 **Japan — no binding education instrument.** A second **AI Basic Plan** approved by Cabinet on **July 14** revising the December 2025 original, and the AI Promotion Act, which is promotional rather than restrictive. **No MEXT education guidance surfaced.**

🟢 **The corrected diagnosis: naming the instrument fixes the SEARCH, but the English-language secondary channel does not carry APAC education policy at all.** 🔴 **It carries APAC *enterprise* AI regulation, written for multinationals, and education appears in it only as one item in a list of high-impact sectors.** **Two passes have now spent their APAC leg on this; the next one should either query the ministries in their own languages (MOE Korea, 教育部, MEXT) or declare the leg closed to this channel and say so in the client-facing text.**

🟡 **Written down as an informed gap, per this KB's own rule that silence looks exactly like coverage: APAC education-AI policy below the national-framework level is NOT covered by this KB, for China and Japan specifically, and two passes of effort have failed to close it.**

### 🟢 The Vietnam reconciliation open since p269 can now be CLOSED, and the two instruments were never in conflict (added p331)

🔴 **This file's APAC row has carried an explicit standing warning for three passes:** `intel/policy-matrix.tsv` line 149 — *"TWO instruments, two dates, same jurisdiction and function, never reconciled on any shelf. Do NOT brief either date alone and do NOT collapse them."* **Decree 142/2026/NĐ-CP (GATED, eff. 2026-04-30) against Decision No. 33/2026/QĐ-TTg (compliance 2027-03-01, +6 months for education systems already operating before 2026-08-15).**

🟢 **This pass's APAC leg resolves it, and the resolution is that the premise of the conflict was wrong: the two instruments do not compete, they compose.** Reported consistently across this pass's sources: **Decision 33/2026/QĐ-TTg operates *alongside* Decree 142/2026/NĐ-CP.**

| instrument | what it actually does | date |
|---|---|---|
| **Decree 142/2026/NĐ-CP** | 🟢 **The framework** — risk tiers, and the duty on providers to **self-classify** before deployment | effective **2026-04-30** |
| **Decision 33/2026/QĐ-TTg** | 🟢 **The LIST the framework refers to** — promulgates **46 high-risk AI systems across 6 sectors** | signed **2026-06-30**, effective **2026-08-15** |

🔵 **A framework decree and a promulgated list are the normal two-instrument shape of Vietnamese regulation. There was never a question of "which governs" — the Decree governs, and the Decision tells you whether you are in scope.** 🟢 **So both dates brief together: self-classification has been a live duty since 2026-04-30, and since 2026-08-15 there is a published list to classify against.**

🟢 **And the two compliance dates reconcile arithmetically, which is the part that should have been caught earlier.** This file carried *"compliance 2027-03-01 and a further six-month grace for education systems already operating before 2026-08-15."* 🟢 **2027-03-01 + six months = 2027-09-01 — and two independent sources in this pass's sweep state the deadline for already-operating healthcare, education and finance systems as exactly 2027-09-01.** 🔵 **The "two dates" were one date and its own grace period.**

| date | what it is | confidence |
|---|---|---|
| **2026-04-30** | Decree 142 in force — self-classification duty live | 🟢 held, two passes |
| **2026-08-15** | Decision 33 in force — the list applies | 🟢 **corroborated this pass** |
| **2027-03-01** | general compliance date | 🟢 held (p269, p271) |
| 🟢 **2027-09-01** | **already-operating education systems — the one to put in a plan** | 🟢 **2027-03-01 + 6 months, and stated directly by two sources this pass** |

### 🟢 New this pass: the three education entries, by name

🟢 **Education is one of the six sectors, and it carries three entries.** This file has had *"automated assessment and behavioural monitoring named"* since p269; **the third entry and the conditions are new:**

| # | the education entry, as reported | what it reaches in a studio deliverable |
|---|---|---|
| 1 | 🟢 **NEW — large-scale self-study content generation built on uncontrolled data** | 🔴 A RAG tutor over an unvetted corpus. **Curating and declaring the corpus is the mitigation** |
| 2 | **Automated testing and ranking of learners where the result counts as the official outcome** | 🔴 Autograding of record. 🟢 **The condition is the escape hatch — below** |
| 3 | **Biometric or emotion monitoring of learners** | 🔴 Proctoring and attention tracking. **Keep out of scope** |

🟢 **Also new: conformity has two pathways, and Decision 33 specifies which applies per system** — mandatory **third-party certification** before deployment, **or** provider **self-assessment** (optionally via an approved body). 🔵 **Which pathway each education entry draws is now the highest-value unknown in this block: it is the difference between a certification line item and a documentation one.**

🟢 **The architectural lever, now attached to a named list entry rather than to a decree in general.** Entry 2 reaches automated assessment **only where the AI output is the sole basis for the decision without meaningful human review.** 🟢 **A human-in-the-loop grading design keeps the product out of the high-risk class entirely** — the same shape Oklahoma's and Maryland's human-oversight rules reward and the EU's Art. 14 requires. **One architecture, four jurisdictions: see Trend 20 and `compose/patterns.md` P26.**

🔴 **Caveat inherited by anything built on this block: the per-entry wording above comes from secondary summaries plus a truncated reading of the official text.** Primary sources are the Vietnamese texts on `thuvienphapluat.vn` and `english.luatvietnam.vn`. 🟢 **The instrument number, the signing date (2026-06-30), the effective date (2026-08-15), the 46-systems/6-sectors count and the 2027-09-01 transition are each carried by two or more independent sources this pass. The per-entry wording and the per-entry conformity pathway are not.**

🟡 **The rest of the region is held, not new:** Korea's AI Basic Act in force 2026-01-22, China's registration-and-labelling regime, Singapore and Japan at the voluntary end (Japan's AI Promotion Act a principles law with no penalties), India regulating at the platform layer via amended IT rules on AI-content labelling. 🔴 **And p329's gap stands: no APAC procurement vehicle surfaced this pass either.** China's "AI Plus Education" buying remains recorded as provincial-level, with no named vehicle.

### 🟡 The region's artefacts are the strongest in this KB and the LTI finding does not reach them — which is itself the opening (added p330)

🔴 **The APAC regional query returned nothing new for a fourth pass** — Korea's AI Basic Act, Vietnam's risk-tiered law, Japan's penalty-free principles act and China's provincial buying are all held, and the vendor-named player list (Google, Microsoft, IBM, Pearson, Byju's) is not carried.

🟢 **What did move is the measurement, and it favours this region.** Every APAC-placed agent this KB holds was re-measured on the activity channel across p329–p330 and all of them are live: **`THU-MAIC/OpenMAIC`** (733 commits, **127 authors**, 2026-10-19), **`HKUDS/DeepTutor`** (2,935 commits, **273 authors**, 2026-10-19), **`Orenda-Project/rumi-platform`** (847 commits, 2026-10-05), **`microsoft/Shiksha-Copilot`** (149 commits, 2026-09-15). 🔵 **127 authors on OpenMAIC corroborates its multi-institution claim first-hand, and 273 on DeepTutor makes it the largest education agent in this base by every measure that is not a star count.**

🟢 **And the LTI collapse this pass found does not bite here in the same way, which is a commercial fact worth naming.** **The APAC artefacts are tutors and classroom shells, not LMS plugins** — they are deployed *beside* an institution's systems or as national programmes, not *inside* a Canvas tenancy. 🔵 **Where North America's integration risk is "the LTI library is dead", APAC's equivalent question is the ministry or provincial procurement route, which this file already treats under China's provincial "AI Plus Education" buying and India's Class-3 mandate.** 🟢 **So an APAC engagement can start from the strongest open artefacts in this KB with the least integration debt — and a studio should say that explicitly when comparing a regional pilot against a North American one.**

🟡 **One row re-graded against this region this pass.** `zhangl1001/civil-ai` — the APAC ports-and-adapters education runtime — was recorded at p323 as *"the highest-starred education agent pushed since 2026-10-01"*. 🔴 **Its default branch's last commit is 2026-08-23; eight newer refs exist and every one is a `dependabot/` branch.** **The architecture finding stands; the recency claim was reading bot pushes and is withdrawn.**

🔴 **A declared regional gap, restated because it did not close:** `ictinnovations/ictexam-mcp` (🟢 **MIT**, read first-hand p330) and its Moodle companion are plausibly APAC on a Pakistan/Gulf vendor signal, **and nothing in either repository declares a country.** **Left unplaced rather than guessed** — the commit record gave one author and one gmail address, which is not evidence.

### 🟡 China's "AI Plus Education" buying happens at provincial level, not ministry level — and no APAC vehicle surfaced (added p329)

🔴 **Confidence: SEARCH-CHANNEL-ONLY. `oecd.ai` and every other non-GitHub host tested answer 403 at CONNECT.**

🟢 **The plan itself this file already holds** (`README.md` lines 1361 and 4190: announced **2026-04-10**, running to **2030**, with
teacher AI-literacy in qualification exams and the per-grade hour floors). 🔵 **What p329 adds is the procurement read, and it changes
who the addressable buyer is: provincial and municipal education bureaus are expected to begin AI procurement in 2026–2027.**
🔴 **So the buyer is a province, not the ministry** — which also means the deal count is high and the deal size is provincial.
🟡 **Stated as an expectation, not a confirmed tender: no notice, portal or value was found.**

🔴 **An informed gap, and it is the honest headline for this region: no APAC framework agreement or consortium vehicle surfaced at
all.** The prescribed regional query returned enterprise-AI commentary and two **commercial training alliances** —
**TCS + Pearson** (multi-year AI learning alliance aimed at employer skills gaps) and **LearnUpon** (new Sydney HQ, AI course
authoring) — which are **competitor signals, not procurement vehicles**, and are recorded as such. 🔵 **APAC is therefore the one
region where this pass closed nothing, and the next pass should go at it per-country (`MOE Singapore`, `MEXT Japan`, `AusTender`,
`GeM India`) rather than as "APAC", which is not a procurement jurisdiction.**
### 🟢 Korea's AI Basic Act is in force with education named high-impact, and India's Class-3 mandate starts this school year (added p328)

| jurisdiction | instrument / move | date | what it means for a bid |
|---|---|---|---|
| **South Korea** | **AI Basic Act in force**, education named among **high-impact** sectors | 🔴 **2026-01-22**, with a **grace period of at least one year before fines** | 🟢 **The highest-quality APAC trigger in this file: a binding obligation already in force, with a penalty cliff ~12 months out.** The grace period is the engagement window — remediate before fines, not after |
| **South Korea** | **AI-textbook programme stripped of official status** by the National Assembly; adoption **under 30%** | 2025-08 | 🔴 **The cautionary case, and it is the most useful single data point in this region.** A national top-down content mandate failed on adoption, not on technology. **Lead with teacher workflow and measured outcomes; do not lead with content volume** |
| **India** | **AI + computational thinking mandatory from Class 3**, government *and* private schools | **2026–27 school year** | 🟢 **The largest dated demand signal in the sector.** Reference implementation already on the shelf: `microsoft/Shiksha-Copilot` (**MIT**, Microsoft Research India + **Sikshana Foundation**) — a named ministry-adjacent NGO deployment, which is what a public-sector bid asks for |
| **China** | reported as one of only **two** nations (with the **UAE**) running a **compulsory national AI curriculum** since the **2025-26** school year; binding rules on algorithms, deep synthesis and generative AI | in force | 🟡 Curriculum demand is real; **the data boundary is the constraint** — see trend 12 and `compose/patterns.md` P10 Variant C, where the Chinese curriculum artefact is **CC BY-NC** and cannot enter a deliverable |
| **Japan** | **AI Basic Plan** adopted under the AI Promotion Act | **2026-07-14** | 🟡 Promotion without penalties. **No compliance trigger — sell capability, not compliance** |
| **India** | still **no dedicated AI statute**; MEITY content-rule amendments (2026-02) target platforms, not education | — | 🔵 **So the India sale is the curriculum mandate, not regulation.** Do not build an India pitch on a compliance deadline that does not exist |

🟢 **Three APAC agents reached the `agents/top.md` shelf this pass** (graded at p296, written into p327's commentary, cut into the canonical table at p328): **`THU-MAIC/OpenMAIC`** (MIT, Tsinghua, the largest permissive education agent in this KB — multi-agent classroom shell with `skills/`, `eval/`, `e2e/` already wired), **`microsoft/Shiksha-Copilot`** (MIT, India), **`Orenda-Project/rumi-platform`** (Apache-2.0, **Pakistan**, Taleemabad national-curriculum library, 847 commits). 🔵 **For the first time this region's shelf is not thinner than EMEA's.**

🟡 **One new APAC-adjacent agent is copyleft and should not be embedded:** `HugeCatLab/ChatTutor` is **AGPL-3.0** (34,522 B grant read first-hand) and placed here **on a `README_CN.md` language signal only** — no country or institution is named. **Read it; do not ship it in a proprietary deliverable.**

### 🟢 Three region-placed agents were already graded for promotion and never delivered — they are live now (added p327)

🔴 **p296 placed three APAC artefacts, marked all three `PROMOTE-to-agents-top`, and none reached a
shelf file until this pass.** Licences re-read first-hand at p327:

| artefact | licence | ★ | placing evidence |
|---|---|---|---|
| `THU-MAIC/OpenMAIC` | 🟢 **MIT** (1,064 B) | **41.1k** | Tsinghua (THU-MAIC) — *Open Multi-Agent Interactive Classroom*. 6.4k forks, 733 commits |
| `microsoft/Shiksha-Copilot` | 🟢 **MIT** (1,140 B) | 9 | README names **Microsoft Research India** + **Sikshana Foundation** |
| `Orenda-Project/rumi-platform` | 🟢 **Apache-2.0** (11,286 B) | 18 | README names **Pakistan** and the **Taleemabad** national-curriculum library. 847 commits |

🟢 **`OpenMAIC` is the largest permissive education agent in this KB by an order of magnitude and it
is a Chinese university release** — it ships `skills/`, `eval/`, `e2e/` and a `render-service`,
which means the multi-agent classroom shell, its eval harness and its rendering layer are all in
one Apache-free MIT tree. 🔵 **For an APAC engagement that wants a demonstrable multi-agent
classroom in weeks rather than quarters, this is the starting point, and the 41.1k stars are a
procurement argument on their own.**

🔵 **`Shiksha-Copilot` and `rumi-platform` are the two artefacts in this KB with a *named
ministry-adjacent deployment* in South Asia** — MSR India with Sikshana in Karnataka, and
Taleemabad's national-curriculum library in Pakistan. **India's 2026-27 mandate (P10 Variant B)
has been described in this KB as arriving without an artefact; `Shiksha-Copilot` is the closest
thing to one, and it is MIT.** 🔴 **Both are small-star repositories — 9 and 18 — so cite the
institution, never the star count.**

🟢 **`open-edge-platform/education-ai-suite` (Apache-2.0, Intel, OpenVINO, CPU/iGPU/NPU) is the
offline/on-device answer for the region's low-connectivity deployments** and pairs with Kolibri
(MIT) in **P5**. 0 stars, 450 commits — a vendor release, not a community one.


> **Pass 323 — the region's finding this pass is not a policy, it is an artefact, and it changes the
> competitive read.** `haolpku/K12-KGraph` (`repos/foundations.md`) is **China's PEP K-12 curriculum
> as a verified, evidence-linked knowledge graph** — 10,685 nodes, 23,278 edges over 48 textbooks,
> per-edge textbook evidence, **12 expert annotators at Fleiss' κ = 0.84**, a 23,640-question
> benchmark, three released checkpoints, **NeurIPS 2026 Evaluations & Datasets Track**, **420 ★**.
>
> - **Its data licence is CC BY-NC-SA 4.0 and its code is MIT.** The method is reusable in any
>   jurisdiction; the curriculum cannot enter a commercial deliverable **anywhere**, China included.
> - **The competitive consequence:** this KB priced the verified-curriculum layer as an uncontested
>   build-once opportunity at 22 stars. **In APAC it is contested, with academic backing and a
>   peer-reviewed quality bar a Globant build would be measured against.** Pick jurisdictions that
>   are still open — and expect a Chinese client to already know this artefact exists.
> - **The supply read, measured rather than asserted:** of the ten repositories on the first page of
>   the new-supply sweep (education/AI/tutor/agent, pushed since 2026-10-01, star-sorted), **four are
>   Chinese-language exam-prep skills** and the **highest-starred new education agent of the window
>   is APAC-authored** (`zhangl1001/civil-ai`, MIT, 41 ★). **APAC is now the largest bloc of new
>   education-agent supply in this KB, not a token presence.**
> - **And a new risk class, APAC-first:** two of those skills are built on the teaching persona of a
>   **named, living educator**, MIT-licensed, with explicit unofficial disclaimers. **The code
>   licence does not cover the persona.** See `intel/trends.md` and `agents/top.md` — treat any
>   "make it teach like [named person]" request as a legal question first.
> - **Regulation, unchanged and worth restating:** no APAC-wide AI law is expected; the landscape is
>   fragmented by jurisdiction (Singapore mature guidelines, China focused on algorithmic
>   misconduct, the ASEAN governance guide early-stage), **and none of the sources reached this pass
>   addresses education-specific rules.** Market framing also unchanged: APAC is the fastest-growing
>   region in the vendor forecasts (one report: USD 591.6m in 2024 → USD 1,848.1m by 2029, 20.9%
>   CAGR) — **vendor research, treat as indicative.**


**New at p321 — Indonesia, measured rather than assumed.** The `pendidikan` GitHub topic holds **42
repositories**, and exactly one is an AI artefact: `RozhakDev/EduPintarIPAS` (**MIT**, 20 ★, **1
commit**, Flask + **Azure AI Language Custom Question Answering**), a year-6 `IPAS`
science-and-social-studies chatbot whose QA set the README says was built from the **official `SD`
curriculum**, aimed explicitly at **3T regions** (*tertinggal, terdepan, terluar* — underdeveloped,
frontier, outermost). Everything else in the topic is school administration at 0–4 ★.

**So the Indonesian opportunity has the same shape as the Indian one and a named local precedent.**
The curriculum-grounded-QA *pattern* is present and someone has already pointed it at the
hardest-to-serve districts; the *engineering* is one commit. A buyer with a national curriculum and
no data layer under it is Pattern **P10**, and Indonesia now joins India in that column — with the
difference that Indonesia has a demonstrated framing (3T equity) a bid can be written around.

**Japanese and Korean are now measured negatives, not blanks.** `kyoiku` holds one repository at
0 ★; `gyoyuk` **exists and holds zero**. Both were reached only as romanisations — the CJK topic
slug `教育` is a 404, because GitHub normalises topic slugs to ASCII. **These are findings about the
open-source supply, not about the market**: Korea has the region's first binding AI statute (in
force `2026-01-22`, see Regulation by region) and no open education-AI repositories under its own
language tag. **Demand with no local open supply is a build opportunity, not an absence** — but
price it as greenfield, because there is nothing to fork.

1. **India's Class 3–8 mandate remains the single most concrete opportunity in this KB.** 32,900
   schools, a fixed 2026-27 start, specified contact hours, and a documented delivery gap — 64.7%
   of schools have computers, 63.5% have internet. That gap is the brief: **Kolibri (MIT,
   offline-first) + Sunbird (MIT, the national stack) + locally-cached content**, not a cloud tutor.
2. **The APAC paradox is a sales problem worth naming.** APAC faculty are the *most* enthusiastic
   (57% excited) and have the *lowest* future adoption intent (67%). Enthusiasm without intent means
   the blocker is institutional, not attitudinal — procurement, infrastructure, language, assurance.
   Lead with a deployment and assurance story, not a capability demo.
3. **South Korea is now a dated compliance market, not a watch item.** The Framework Act on AI has
   been in force since **2026-01-22**, its high-impact category explicitly reaches **student
   evaluation in early childhood, elementary and secondary education**, high-impact operators owe
   user-protection measures and safety records (Art. 34(1)), and **a foreign vendor must appoint a
   domestic agent.** The grace period on fines is reported as one year, so it lapses around
   2027-01. This is the same product as pattern P3 and P4 — audit trail, human oversight, documented
   risk management — resold into Korea, plus a local-agent arrangement. Read the Enforcement Decree
   and MSIT guidance before quoting thresholds.
4. **China's labelling and registration regime as a design constraint.** Service registration,
   security review and AI-content labelling are mandatory; "AI Plus" gives state-backed demand
   through 2030. Compliance-first architecture with labelling at the generation step.
5. **Build the Indian curriculum data layer. This is the clearest build-once opportunity in the
   KB — NEW.** India's Class 3–8 AI + Computational Thinking mandate starts in 2026-27 across
   32,900 CBSE schools with specified contact hours. **There is no verified machine-readable
   NCERT/CBSE curriculum dataset.** GitHub's `ncert` (55 repos) and `cbse` (125 repos) topics hold
   nothing above 15 stars that is infrastructure; the MCP attempt (`jinanshm/ncert-mcp`) is
   unlicensed and **LLM-tags its chunks with no human verification**; the best data asset is a 2018
   scrape of ~20,000 schools. **Brazil has exactly this artefact and published what it is worth:
   31.9% → 2.3% hallucination** (`repos/foundations.md`). Porting the `bncc-dev` pattern — verified
   extraction against the official source, JSON Schema, 30 contract checks in CI, MIT code with
   CC BY 4.0 data, an MCP server — is a bounded, fundable, reusable asset with a named buyer in a
   board, a ministry or a national edtech. Pattern **P10**.
6. **Sell Korea's lesson, not Korea's mandate — NEW.** The AI digital textbook programme was
   mandated, rushed, resisted, retreated to voluntary adoption, **stripped of textbook status by
   the National Assembly on 2025-08-04** and defunded, with usage falling from ~37% of eligible
   classes to 19% within 2025 and schools from ~4,190 to 2,095. Every APAC education ministry has
   watched this. **The engagement that sells into that memory leads with teacher preparation,
   staged voluntary adoption, measured outcomes and an exit path — and prices change management as
   the main line item.** The Korean compliance work (Framework Act on AI, high-impact category,
   domestic agent requirement) is a separate, additive sale.
7. **Offline delivery has a second permissive component — NEW.** `elimu-ai/webapp` (MIT, 8,075
   commits) hosts per-language educational content and pushes it to Android devices for
   out-of-school children, with production deployments in **Hindi, Tagalog, Thai, Vietnamese and
   English** and real ML pieces in the same org (reading-level prediction, storybook and video
   recommenders). With **Kolibri** (MIT) and **`ipti/br.tag`**'s sync-without-internet design, the
   offline-first stack in pattern P5 is now assembled from three independently maintained
   permissive projects rather than one.
8. **Japan's light-touch regime and low public AI use** (26.7% in 2024 vs 81.2% China, 68.8% US)
   makes it the region's adoption-enablement market: Japanese-language tutoring and teacher-facing
   automation, with the fewest regulatory blockers of any major market in this KB.

### LATAM

### 🟡 One new LATAM vehicle on the search channel, and the regional picture is otherwise unchanged (added p333)

🟢 **New to this KB: the UNESCO Observatory on Artificial Intelligence in Education for Latin America and the Caribbean.** 🔵 **Why it matters commercially and not just institutionally: an observatory is a convening and standard-setting surface, which is how a studio gets into a regional conversation before a tender exists** — the same logic that made GÉANT OCRE (EMEA) and cooperative purchasing (North America) worth naming at p329. 🔴 **Search-channel-only: `unesco.org` returned `000` at CONNECT this pass and `WebFetch` returned `ENOTFOUND`. Name, no notice number, no date verified at source. Confirmation costs one lookup from a connected machine.**

🟢 **Confirmed and already held — re-reported by the channel, no change:** Brazil's **PL 2.338/2023** as the region's most developed framework (Senate-approved December 2024), Chile's bill (**Boletín 16821-19**) in its first constitutional stage, and Mexico with **no federal AI law passed**. 🔵 **p329's `ChileCompra Directive No. 44/2026` remains the only LATAM instrument in this KB that is a buying RULEBOOK rather than a forecast, and it is still the strongest single LATAM asset on this shelf.**

🔴 **The adoption gap this file should keep quoting, because it is the actual sales argument:** reportedly **more than 50% of teachers in Chile and Brazil already use these tools while fewer than 10% of institutions in the region have formal guidelines** (UNESCO), and **13 of 19 LAC countries studied do not teach early AI adoption in schools** (CENIA). 🟢 **Classroom use is running ahead of institutional readiness, which is precisely a governance-and-enablement engagement rather than a model engagement** — and it is the one region where this KB can state the mismatch with numbers.

🟡 **Honest limit, unchanged from the LATAM leg's standing problem: none of these figures is verified at source from this environment.** The non-GitHub channel is closed here and has been since p294.

### 🟢 The most-deployed open LTI library in the world is maintained from Brazil — measured, not inferred (added p331)

🔴 **p330 closed this block with a complaint: *"LATAM is invisible to the instrument, not absent from the sector."* 🟢 This pass pointed the instrument at the global LTI stack and found a LATAM artefact at the centre of it.**

🟢 **`Cvmcosta/ltijs` — Apache-2.0 (11,361 B, read first-hand p331) — is maintained from Brazil.** From the commit record, first-hand: **429 of 575 commits come from a single `yahoo.com.br` address.** It is **575 commits, 17 authors lifetime, head 2026-10-13**, and `ltijs` **7.0.7 was released on 2026-10-06**. 🔵 **This is the LTI library the open education ecosystem actually installs, and this KB has recommended it since p232 without ever noticing where it comes from.**

🔴 **And the same record carries the risk, which is what makes this an opportunity rather than a trophy.** Measured this pass: **51 commits in 2026 by only 2 distinct authors**, against 17 lifetime. The current head is a dependabot merge. And the second author domain is 🔴 **`ltiaas.com` — 90 commits — the maintainer's own commercial hosted LTI product.**

🟢 **So the opening is maintenance capacity, and it is unusually cheap to occupy.** **A studio that puts two engineers on `ltijs` becomes the second name on the most-deployed open LTI library in the sector** — in the region where this KB's procurement layer is thinnest and where a credible open-source credential is worth more than a case study. 🔵 **Contrast the alternative route into the same layer: `@lti-tool/core` is MIT, healthier (235 commits in 2026 by 6 authors) and North American. 🟢 Propose `lti-tool` for a new build; propose *contributing to* `ltijs` as the regional capability play.**

🟢 **This pass's new quantitative detail for the region — teacher-level AI use, from OECD TALIS 2024:**

| country | secondary teachers who used AI in the previous year |
|---|---|
| 🟢 **Brazil** | **56%** |
| 🟢 **Chile** | **55%** |
| 🟢 **Colombia** | **53%** |
| 🟢 **Costa Rica** | **52%** |
| OECD average | **36%** |

🔵 **Four LATAM countries run 16–20 points above the OECD average on teacher AI use.** 🟢 **Read against the institutional figures this file already holds — UNESCO IESALC: 87% of 200 institutions across 19 countries using AI somewhere, 74% in teaching and learning, and only 26% with a formal AI strategy — the region's profile is unambiguous: the highest practitioner adoption in the world sitting on the thinnest governance layer.**

🟢 **The engagement that fits, and it now has a local artefact to point at:** a governance-and-integration package — an institutional AI strategy (the 26% gap), delivered on an LTI integration into the LMS the institution already runs, **built on or contributed to a library maintained in the region**. 🔵 **The 84% / 68% / 52% split this file already holds — private non-profit, public, private for-profit — says to lead with private non-profit universities, which are both the most adopted and the most able to buy.**

🔴 **Held, not new, and restated so the figures are not re-sourced next pass:** the UNESCO LAC Observatory on AI in Education (launched 2026-04-14 at ECLAC, Santiago), the ILIA third edition, the Digital Education Council's 2026 LATAM survey (30,000+ responses, 29 institutions), and ChileCompra Directive 44/2026 as the region's one named procurement vehicle.


### 🔴 The region's measurement problem is now specific: LATAM is invisible to the instrument, not absent from the sector (added p330)

🔴 **The LATAM regional query returned nothing this file does not already hold** — the UNESCO IESALC 87%/26% split, the Observatory at ECLAC Santiago with CAF, CENIA, CETIC.br, Santillana, Tec de Monterrey, ProFuturo and Ceibal, the CONALEP/DGETI Mexico pilot, the Digital Education Council survey, Uruguay's Council of Europe signature, Peru's sandboxes and Colombia's CONPES 4144 are all carried.

🟢 **What this pass adds is a precise account of *why* the artefact side of this region stays empty, and it is an instrument property rather than a fact about Latin American software.**

1. 🔴 **The Spanish/Portuguese sweep was run and it works.** `compose/code/gitlab-api-channel/data/discovery-es-pt.json` holds **141 projects from 16 Spanish and Portuguese terms, 140 of them invisible to the 25-term English sweep.** 🔵 **The language barrier is real, it was measured, and it was crossed.**
2. 🔴 **And not one of the three real LATAM education projects it found declares a licence** (`latam-candidates.json`). **An unlicensed repository is not a finding this KB can ship** — it is legally unusable in a client deliverable regardless of its quality.
3. 🔴 **The new structural limit found this pass compounds it.** Thirteen self-hosted forges answer `000`. **Latin American ministries and universities that host their own GitLab are as invisible as European ones** — and this region has a stronger institutional-hosting pattern than North America, not a weaker one.

🔵 **Put together, the honest statement for a LATAM engagement is not "there are no open education artefacts in the region". It is: across two forges, four sweeps and two languages, the artefacts this instrument can see from the region are unlicensed, and the ones most likely to be licensed are on infrastructure it cannot reach.** 🟢 **That is a far better sentence to bring to a client than silence, and it changes the engagement shape: in LATAM the studio should expect to *originate* the open artefact — and the existing regional assets this file already holds, the Chilean pedagogy benchmark and the Brazilian BNCC curriculum stack, are the two counter-examples proving it can be done.**

🟡 **One concrete action for the next pass, pre-registered so it is not re-derived:** the three unlicensed LATAM candidates in `latam-candidates.json` should be re-probed for a licence file, because **an unlicensed repository that adds one later becomes shippable overnight** and this KB has no watch on them. **Cost: three `raw` requests.**

### 🟢 ChileCompra Directive 44/2026 is the rulebook for selling AI to a Chilean public buyer, and Mexico cannot be monitored federally (added p329)

🔴 **Confidence: SEARCH-CHANNEL-ONLY. `cenia.cl`, `unu.edu` and `oecd.ai` all answer 000 / 403 at CONNECT; no primary text was read.**

| finding | detail | why it matters |
|---|---|---|
| 🟢 **ChileCompra Directive No. 44/2026** | Official guidance to Chilean public entities on **how to buy data-science and AI projects** through **Mercado Público**. The 2023 version was **updated 2026-03**, reflecting the reform of **Law No. 19,886** and its new regulation | 🟢 **The most actionable LATAM procurement artefact this KB has found. It is not a market forecast — it is the RULEBOOK the buyer must follow, so reading it tells a studio the shape of the bid before the bid exists** |
| **Brazil — PBIA, with its buyers named** | National AI plan, goals to **2028**, including **AI literacy in primary and secondary education**. Watch **MCTI**, **MEC**, **federal universities** and the **SENAI / SENAC** networks | 🟢 **This file already held PBIA as policy. Naming the institutional buyers is the step that was missing** — policy becomes a pipeline only once you know who signs |
| 🔴 **Portal coverage, with its defect named** | **PNCP** (Brazil), **Mercado Público** (Chile), **CompraNet** (Mexico) — 🔴 **CompraNet federal data is reported FROZEN AT 2022, with only Nuevo León live** | 🔴 **A named data defect beats a portal list: Mexico cannot be monitored federally at all, so Mexican coverage must be state-level or it is fiction.** Any "we track LATAM tenders" claim that includes federal Mexico is wrong |
| **UNESCO LAC Observatory** | Roadmap **2026–2029**; partners include **CENIA**, **CETIC.br**, **Tec de Monterrey** (this file also holds **Ceibal**) | 🔵 **ALREADY HELD** (lines 323, 641, 704) — recorded as held so the pass does not double-count it as new |

🔵 **And the one thing the prescribed LATAM query returned that this file already holds better:** the **UNESCO IESALC / UNU-IAS**
higher-education survey. The snippet gave "200 institutions, 19 countries"; **this file already carries 200 institutions, 19 countries,
87% using AI in ≥1 area, 74% in teaching and learning, and only 26% with governance** — so the regional query confirmed a held row at
lower precision, which is the fifth consecutive pass it has done that.
### 🟢 UNESCO put a regional AI-in-education observatory in Chile, and the adoption-versus-governance gap is now a number (added p328)

| finding (p328 sweep) | detail |
|---|---|
| 🟢 **UNESCO launched the Observatory of Artificial Intelligence in Education for Latin America and the Caribbean** | announced **2026-04**, **based in Chile** |
| 🔴 **The gap, quantified** | **more than 50% of teachers in Chile and Brazil already use these tools**, against **fewer than 10% of institutions in the region holding any formal guidance** |
| 🔴 **Chile — Ley 21.719 (personal data)** | **in force 2026-12-01** — **the region's nearest dated compliance deadline, now about six weeks out.** A dedicated AI bill remains in the Senate |
| 🟡 **Brazil — PL 2338/2023** | passed the **Senate** in late 2024; **still pending in the Câmara dos Deputados.** Not yet an obligation |
| 🟡 **Brazil / Mexico — education specifically** | **orientative guidance or open consultations, not duties.** Universities largely operating in a regulatory vacuum |
| 🟢 **Institutional demand signal** | **Tecnológico de Monterrey** signed an agreement with UNESCO on educational AI and plans AI integration across **44+ programmes by 2026** |

🟢 **The opportunity this creates is unusually clean, because the two numbers point opposite ways.** **Teacher adoption above 50% with institutional governance below 10% is not a technology gap — it is a liability gap that has already opened.** The tools are in the classroom; the policy, consent basis and audit trail are not. 🔵 **And unlike EMEA, where the expensive obligation just slid to 2027, LATAM has a hard date: Chile's Ley 21.719 on 2026-12-01.** **A Chilean institution with majority teacher AI use and no formal guidance is six weeks from processing student personal data under a new statute with no documented lawful basis.**

🟢 **What to build it on, all permissive and all already on this KB's shelves:**
- **`AI-for-Education/pedagogy-benchmark`** (**MIT**, foundations row since p327) — **1,143 questions from real teacher-qualification examinations (920 CDPK + 223 SEND)**, acknowledging **Chile's MINEDUC Agencia de la Calidad de la Educación and CPEIP**. 🟢 **The region's own pedagogy benchmark, and the exams behind it are Chilean — so "prove it teaches" is answerable in-region with a licence that can ship.**
- **`eai6/ai-tutor`** (**MIT**, p328) for the consent and audit layer: `ConsentRecord` (incl. **parental**, `withdrawn_at`), pseudonymised audit log, `export_user_data` / `delete_user_data`. 🔵 **Ley 21.719 compliance work needs exactly these mechanics, and this is the first time this KB can point a LATAM client at them under MIT.**
- **`bncc-dev`** (CC BY 4.0) for the Brazilian curriculum spine, and **`withmarbleapp/os-taxonomy`** (ODbL-1.0) for the cross-national one — see `compose/patterns.md` P10 Variant D.

🔴 **Not carried, and recorded so it does not creep in later.** One source asserts Chile approved a *"Marco Nacional de IA Educativa"* in 2025 under **Ley 21.640**, citing IDB data. **No other source in the sweep supports it and no official record was reachable. It is excluded from this file.**

### 🟢 The region finally has a pedagogy benchmark, it is MIT, and the exams behind it are Chilean (added p327)

🟢 **`AI-for-Education/pedagogy-benchmark` — MIT, 1,063 B licence read first-hand at p327, 12 ★,
5 commits.** **1,143 questions drawn from real teacher-qualification examinations: 920 in the CDPK
benchmark and 223 in SEND** (Special Educational Needs and Disabilities) — counts read from the
README this pass. **The README acknowledges Chile's Ministry of Education — Agencia de la Calidad
de Educación — and CPEIP for developing and sharing the exams.** Scores live on external
leaderboards; p296 records arXiv:2506.18710.

🔵 **Why this is the most useful LATAM addition in several passes.** This KB's LATAM position has
rested on `bncc-dev` (Brazil's curriculum spine, P10 Variant A) and on policy coverage. **Neither
answers the question a client actually asks first — "which model should we use, in Spanish, for
teachers?"** 🟢 **A benchmark built from a LATAM ministry's own licensing exam answers it with a
number instead of a vendor claim, and it is MIT, so the harness can go into a deliverable.**

🟢 **The pairing to sell, and it is concrete:** run `pedagogy-benchmark` as the **model-selection
gate** and `learning-commons-org/evaluators` (MIT code) as the **output-acceptance gate** — the
first picks the model, the second polices what it emits. 🔴 **Two boundaries to respect: the
evaluators' annotated CLEAR and PERSUADE 2.0 corpora are CC BY-NC-SA 4.0 and cannot ride into a
paid deliverable, and the evaluator rubrics are English-language and ELA-centric, so a Spanish
deployment needs them re-annotated — which is billable scope, not a blocker.**

🔵 **`bncc-dev` remains the curriculum spine for Brazil; the Learning Commons data tier is US state
standards and does not port to LATAM.** **What ports is the architecture, not the data** — spine +
skills + evaluators — and in LATAM the spine is national. Nothing in this pass changes P10
Variant A.


### 🟢 Chile's Ley 21.719 is the region's nearest dated compliance deadline — and it is six weeks out (added p326)

**New to this file.** Chile's **Ley 21.719** on the protection of personal data was **published
2024-12-13** and its first transitional article sets entry into force at **the first day of the
twenty-fourth month after publication — 2026-12-01.** 🔵 **That is the closest hard date in this
KB's whole LATAM record, and no education engagement scoped in Chile this quarter can ignore it.**

**What it does to an education deal, concretely:**
- It is a **GDPR-shaped regime** — lawful basis, data-subject rights, breach notification, a new
  supervisory **Agencia de Protección de Datos Personales** — landing on a sector whose data is
  **minors' data by default.**
- **Penalties** are cited at up to **20,000 UTM**, rising to up to **4% of annual revenue** for
  repeated violations.
- If the 2026 date holds, the Agency may issue **written warnings instead of fines to smaller
  entities for the first twelve months** — a grace period, not an exemption.

🔴 **Two caveats, and both change how you should advise.** **(1) A delay bill is live.** The
government filed **boletín 18.623-07 on 2026-09-01** to push entry into force to **2027-12-01**;
as of **2026-10-11** it was in first reading in the Constitution Committee with no report and no
vote, with *suma urgencia* renewed **2026-10-06**. **The legal default remains 2026-12-01 until
that bill passes and is published.** **(2) The Agency does not exist yet.** The Senate rejected
the President's nominees for its council in **May 2026** and the June deadline to seat the first
council passed unmet. 🔵 **Advise to the statute, not to the forecast:** build the consent,
minimisation and breach-notification surface now — it is required under either date — and treat
the Agency's absence as a reason the enforcement ramp is uncertain, never as a reason the
obligation is.

🟢 **The architecture this KB already holds is the answer to it, and it is LATAM-authored.**
`JustinoLM/STI-matematicas` (Panama) keeps **no student data**, hashes with **Argon2**, scopes
teachers to their own groups, and **substitutes anonymous placeholders server-side so prompts
never carry student names.** **That is a Ley 21.719–shaped design built before the law bites, by
a graduating student in a public school.** It carries no licence, so copy the design, not the
code — pattern **P12**.

🟡 **Regional frame, unchanged and worth restating against this date.** Brazil and Peru have the
more consolidated frameworks; Chile and Argentina advance through ethical and institutional
guidance; Mexico and Ecuador are early. A 2026 survey finding already carried in spirit here now
has a figure attached: **~70% of institutions in Europe and North America have or are developing
AI guidance, against ~45% in Latin America and the Caribbean.** 🔴 **Secondary source, directional
only.** **Higher education across the region has no unified AI framework** — though a México /
Colombia / Chile comparison found all three require students to **declare when and why they used
AI**, which is a disclosure obligation a product can be built to satisfy.

### 🟢 The region's first measured classroom outcome — Panama, and it belongs in this file (added p325)

**This KB has held `JustinoLM/STI-matematicas` since an earlier pass and this file never carried its
numbers.** It is, as far as this base reaches, **the only artefact in the whole education KB with a
measured learning outcome, a significance test and a usability score from a real classroom** — and
it is LATAM.

**Universidad Tecnológica de Panamá**, Facultad de Ingeniería de Sistemas Computacionales; an
intelligent tutoring system for sixth-grade decimal arithmetic, validated **May–July 2026 across
three sixth-grade sections of a Panamanian public school**:

| indicator | result |
|---|---|
| students participating | **74** (65 completed at least one practice) |
| practice sessions completed | **710**, in two months |
| pre-test → post-test (n = 63, scale 0–8) | **1.83 → 2.56** correct, mean |
| significance | **Wilcoxon p = 0.0012**; **medium effect, r = 0.41** |
| perceived usability (SUS, n = 70) | **70.1 / 100** |
| used the in-app reward shop | **92%** of those who practised |

🟢 **And it states its own limit, in its own README: there was no control group, so the gain cannot
be attributed to the system alone.** 🔵 **That single sentence is worth more in a bid than the
p-value.** It is the posture p323's *"prove it teaches"* section asks for, written by a graduating
student in a public school deployment, and it is **stricter than every commercial uplift claim this
file records.** Quote the design, name the limit, and the room will trust the rest of the deck.

🔴 **Two hard limits on using it.** (1) **It carries no licence** — seven candidate filenames probed
across five branch names, none present — so **nothing in it can enter a deliverable**; the project
is finished, tagged `v1.0-tesis`, its infrastructure decommissioned and there is no live demo.
(2) The sample is one school and three sections.

🟢 **The part a LATAM public-sector engagement should copy verbatim is the data posture, because it
is the question a ministry will ask first.** The repository contains **no student data**; passwords
are **Argon2** hashes only; administrative functions require a server-verified token; each teacher
sees only their own groups within their own school; and — **the detail to put on a slide** —
**prompts sent to the language model carry anonymous placeholders substituted server-side, never
student names.** 🔵 **The model it calls is DeepSeek.** A Panamanian public primary school, a
Chinese frontier model, and name-stripping at the boundary is **the data-sovereignty conversation of
this region in one artefact** — and it shows the conversation has a technical answer that does not
require a sovereign model.

**Wiring this evidence design onto components that *are* licensed is pattern P12 in
`compose/patterns.md`.**


> **Pass 323 — one concrete, peer-reviewed deployment datapoint and one regional measurement, both
> new to this file.**
>
> - **Piauí, Brazil — a statewide AI curriculum that is actually running, with numbers.** An
>   **AIED 2026** conference chapter (*"Implementing a Statewide AI Curriculum: One Brazilian
>   Experience"*, Springer) reports a **weekly AI subject required in public full-time high schools
>   since 2024**, expanding grade by grade **through 2026**, with **650+ teachers certified** and
>   roughly **120,000 students across 494 schools**. **🟡 Snippet-sourced:** the Springer chapter
>   page failed at DNS when fetched directly this pass, so the figures are from the search channel
>   and the chapter itself has not been read. **Re-verify before quoting in a bid.**
> - **Why it matters more than its size:** this KB's LATAM case has rested on the **artefact**
>   (`bncc-dev`'s verified BNCC) and on market forecasts. **This is the delivery half** — a named
>   state, a mandated weekly subject, a teacher-certification pipeline and a student count. **A
>   reference a Brazilian or regional ministry buyer will recognise**, and the natural anchor for
>   pattern P10 Variant A conversations.
> - **The regional measurement that frames the opportunity:** Chile's **CENIA** reports that **13 of
>   19** Latin American and Caribbean countries it studied **do not teach AI in schools early on.**
>   That is the scale of the curriculum-and-training gap in one number, from a regional institution
>   rather than a vendor.
> - **One governance datapoint:** **Brazil and the EU signed an AI and tech-regulation agreement**
>   (reported 2026-06). Relevant because a Brazilian deployment that aligns to EU AI Act structures
>   gets cheaper to sell in both markets — **the P4 conformity package may be partly reusable in
>   Brazil**, which would be a first for this file. Reported, not verified against the agreement
>   text.
> - **Unchanged:** `bncc-dev` remains **the only verified national curriculum in this KB whose data
>   is licensed for commercial use** (MIT pipeline, CC BY 4.0 data) — and after this pass's Chinese
>   finding, that exclusivity is the LATAM region's single strongest asset in this KB. Market
>   sizing unchanged and still weak: one firm puts *rest-of-LATAM* AI-in-education at USD 18.2m
>   (2024) → USD 36m (2029), which covers only part of the region.


1. **Latam-GPT as the regional differentiator.** Launched 2026-02-10 by CENIA (Chile) with 30+
   partner institutions; ~8 TB of regional and synthetic data; reported 70B parameters on a Llama
   3.1 architecture; Spanish and Portuguese, indigenous languages planned; positioned as public
   infrastructure for governments and universities. **A tutor grounded in Latam-GPT rather than a
   US-centric model is a proposition no global competitor is currently making.**
2. **The 92/30 gap is the pitch.** 92% of LATAM students use AI; only 30% say their institution's
   use of it meets their expectations. That is the widest usage-to-satisfaction gap in any region in
   this KB, and it is an institutional-delivery problem — exactly what a studio sells.
3. **Brazil's regulatory clock has started.** PL 2338/2023 passed the Senate in December 2024 and
   the ANPD sandbox runs to December 2026. A vendor who arrives in 2027 with an EU-style conformity
   file already built will be the only one in the room. Port pattern P4's artefacts now — the
   risk-based structure is the same.
4. **The LATAM market is consolidating around funded local champions, all proprietary** — Teachy
   (Brazil, expanded into Asia), Mattilda (Mexico, $50M + acquisition), Ginia, Vetto, Luca ($8M
   Series A). Globant's play here is partner-or-build-underneath, not head-on: these companies need
   the pedagogy engine, the governance layer and the Spanish/Portuguese quality bar that open source
   can supply.
5. **The evidence base is now quotable, and the numbers are the pitch.** UNESCO IESALC / UNU-IAS,
   launched **2026-09-09**: **200 institutions, 19 countries, 87% using AI in at least one area,
   only 26% with a formal AI strategy, 74% in teaching and learning, 57% in research** — with
   adoption driven by individuals rather than institutions and public institutions the most
   resource-constrained. **A 61-point gap between use and strategy is a governance engagement that
   sells itself**, and it is the same product as North America's pattern P3 with the compliance
   driver replaced by an institutional-risk driver.
6. **The multilateral route in.** UNESCO's **Observatory on AI in Education for LAC launched
   2026-04-14 in Santiago** with CAF, CENIA, CETIC.br, ECLAC, Fundación Santillana, Tecnológico de
   Monterrey, ProFuturo and Fundación Ceibal. These are the bodies that will shape LATAM public
   education AI procurement; engaging them is a slower and far more durable route than a sales
   cycle. **Uruguay is the natural pilot** — first in LATAM to sign the Council of Europe AI
   Framework Convention, and Fundación Ceibal is an Observatory partner.
7. **"LATAM consumes open source but does not write it" is no longer true — and the exception is
   worth a slide.** Pass 318 found that **`openedx/openedx-ai-extensions`, the official AI
   extension plugin for Open edX, was built by eduNEXT, a Bogotá company** whose co-founders are
   long-standing Open edX core committers (703 commits; docs v2.6.0 dated 2026-09-01; AGPL-3.0;
   **explicitly not production-ready**). Full detail and provenance caveats in
   `verticals/solutions.md`. **For a LATAM public-sector or university bid this is a credibility
   asset before it is a technical one:** the AI layer of one of the world's two largest open source
   LMS platforms is maintained from the region, and Globant can speak to it as a peer. The backdrop
   is unchanged — the Linux Foundation's December 2025 report puts **Mexico at 65% and Brazil at
   46% for organisational use of open source AI** — and so is the commercial position: LATAM still
   mostly runs on open source it does not write, which is exactly where a studio that *does* write
   it sells integration, localisation and support.
9. **The whole LATAM stack can now be Brazilian open source — NEW, and this is the pass's biggest
   commercial change.** `portabilis/i-educar` (GPL-2.0, **34,948 commits**, municipally originated,
   published through the federal Portal do Software Público) plus `portabilis/i-diario` (15,834
   commits, the teacher portal) plus `ipti/br.tag` (3,959 commits, offline sync for rural schools)
   give the records layer; **`bncc-dev` gives the national curriculum as verified data with an MCP
   server (MIT code / CC BY 4.0 data)**; a Globant agent sits on the far side of the boundary.
   **None of the three platforms has any AI feature at all.** The pitch is not "adopt our platform"
   but "we add the intelligence layer to the software your ministry already runs, grounded in the
   curriculum it is already accountable to" — and the grounding has a number: **31.9% → 2.3%**.
   Pattern **P10**.
10. **The teacher-adoption figures make the LATAM case without a market forecast — NEW.** UNESCO:
   in 2024, **56% of secondary teachers in Brazil, 55% in Chile, 53% in Colombia and 52% in Costa
   Rica** had used AI in the previous year against an **OECD average of 36%**; a later Uruguayan
   survey reports **75% of public-school teachers**. Against UNESCO IESALC's **87% of institutions
   using AI and 26% with a strategy**, the region's story needs no market-size estimate: **teachers
   are ahead of the OECD and their institutions have no plan.** HolonIQ's observation that LATAM AI
   activity concentrates in **teacher-facing instructional support rather than consumer tutoring**
   says where to aim it.
11. **Two named entry points that are not sales calls — NEW.** UNESCO's LAC Observatory is running
   a pilot in **Mexico with CONALEP and DGETI to build centres of excellence** — vocational
   education, federal scale, a partner list rather than a procurement. And **Brazil's June 2026 AI
   and technology regulation agreement with the EU** means the EU-style conformity package
   (pattern P4) is the artefact Brazilian buyers will increasingly recognise. Build it once for
   EMEA, carry it to São Paulo.
12. **The IDB has already mapped the competition.** The Inter-American Development Bank's review of
   **193 AI solutions across education in Latin America and the Caribbean** reports that **few have
   rigorous evaluations or robust safeguards.** *(Source note: the IDB blog could not be retrieved
   directly in this session — see the gaps section — so the 193 figure is from search snippets and
   should be confirmed against the IDB publication before it appears in a client document.)* If it
   holds, it is the LATAM counterpart to the UNESCO IESALC 87/26 finding and points the same way:
   the region does not need another AI solution, it needs evaluation, safeguards and governance
   around the ones it has. **That is a services engagement, not a product sale**, and it is the
   same offer as pattern P3 with the compliance driver replaced by an evidence driver.

## Declared regional gaps — what was searched this pass and not found

### Pass 330 — what was searched per region, and what came back

🔴 **Fifth consecutive pass in which all four regional queries returned relevant, correct, and already-held material. Zero regulatory or market additions.** 🔵 **Recorded per region, in full, because an informed gap is information and silence looks exactly like coverage.**

| region | query run | what came back | verdict |
|---|---|---|---|
| **North America** | `AI education North America 2026 adoption regulation players` | **134 AI-in-education bills across 31 states in 2026**; California **AB 1159** (bars using student data to train AI models); Oklahoma and Maryland requiring human oversight and barring AI from high-stakes decisions about students; the **K-12 AI Literacy and Readiness Act of 2026** advanced by the House Education and Workforce Committee in July; Canada's June 2026 **"AI for All"** strategy; Mexico's bills with no enforcement regulator; NA at **36% / $3.68B** of the 2026 market; **60%** of US K-12 teachers using AI in 2024–25 | 🔴 **Nothing new.** `AB 1159`, `AI for All`, the Literacy Act and the 134-bill figure are all already held. 🟡 The 36% / $3.68B figure is single-source vendor-aggregator and is **not** carried into this file's market table |
| **EMEA** | `AI education EMEA 2026 adoption regulation players` | EU AI Act with education access and assessment as **high-risk**; the **"AI omnibus"** adopted June 2026, in force 2026-07-27; the Commission's updated ethical guidelines for educators; **$2.64B** European market 2026; **Finland, Estonia and the Netherlands** leading K-12 integration; a **£4M** UK investment in lesson-planning and marking tools; *"only 10% of 450+ institutions have formal AI guidelines"* | 🔴 **Nothing new, and one figure rejected.** The omnibus and the high-risk classification are held, including **this file's own p328 correction to the high-risk date — which the search channel still does not reflect.** 🔴 The *"10% of 450+ institutions"* claim is **cross-region, not EMEA**, and is not carried |
| **APAC** | `AI education APAC 2026 adoption regulation players` | South Korea's **AI Basic Act** in force 2026-01-22; **Vietnam's** AI law in force 2026-03-01 with risk-tier classification; China's comprehensive framework; Japan's **AI Promotion Act** as a principles law with no penalties; Singapore voluntary; *"Google, Microsoft, IBM, Pearson and Byju's"* named as key APAC players; China, India and Japan dominant | 🔴 **Nothing new.** Korea, Vietnam, Japan and China are all held — Vietnam in `intel/policy-matrix.tsv` with a **date conflict this file has already declared open**. 🟡 The player list is a vendor research summary naming four global incumbents and one company in financial distress; **not carried** |
| **LATAM** | `AI education LATAM 2026 adoption regulation players` | **UNESCO IESALC**: 200 institutions, 19 countries, **87%** using AI in ≥1 area, only **26%** with a formal AI strategy; the **UNESCO Observatory** launched 2026-04-14 at ECLAC Santiago with CAF, CENIA, CETIC.br, Fundación Santillana, Tec de Monterrey, ProFuturo and Fundación Ceibal; the **CONALEP / DGETI** Mexico pilot; **Digital Education Council** 2026 LATAM survey (30,000+ responses, 29 institutions); Uruguay first in the region to sign the Council of Europe AI convention; Peru's sandboxes; Colombia's **CONPES 4144**; Mexico's stalled federal bill | 🔴 **Nothing new.** Every one of these — the 87/26 split, the Observatory and its partner list, CONALEP/DGETI, the DEC survey, Ceibal — is already held in this file |

🟢 **The method conclusion, and it is the same one p327 reached by a different route: the prescribed regional queries are saturated for this industry, and the regional intelligence this pass actually produced came from somewhere else entirely — the commit record.**

**Six artefacts were region-placed this pass without a single search**, from author email domains and commit UTC offsets inside clones the activity channel was already fetching:

| artefact | evidence | region |
|---|---|---|
| `Gchism94/jupyterquest` | 🟢 `gchism@arizona.edu`, 124 of 249 commits | **North America** — University of Arizona |
| `Jellypod-Inc/school-skills` | `pierson@jellypod.ai`; all commits `-0700` | **North America** — was 🔴 UNPLACED since p328 |
| `Openki/Openki` | `cis.ch`, 1,759 commits; 2026 offsets `+0200`/`+0100` | **EMEA** — Switzerland |
| `francoisjacquet/rosariosis` | `rosariosis.org`; 2026 offsets `+0200`/`+0100` | **EMEA** |
| `artcc/freelingo` | 🟡 Spanish personal name on 1,064 of 1,168 commits; no institution declared | **EMEA** *(inferred — weakest evidence here, labelled as such)* |
| `afri-bit/revibe` | all commits `+0200` (CEST) | **EMEA** — was 🔴 UNPLACED since p328. 🟡 Places the keyboard, not the person |

🔵 **The next pass should spend its regional budget on the commit record and not on the query set.** 🔴 **One structural caveat that belongs with every regional count in this file, and it is new this pass:** thirteen self-hosted and alternative forges — including **`forge.apps.education.fr`** (the French Ministry of Education's own) and **`gitlab.opencode.de`** (Germany's public-sector platform) — answered **`000`** to a plain API probe, while `gitlab.com/api/v4` answers **200** in the same session. **The reachable surface is a host allowlist. European public-sector education code hosted on sovereign forges cannot be seen from here at all, so every EMEA count in this file is a floor, structurally biased toward European projects that also mirror to GitHub or gitlab.com.**


### Pass 328 — what was searched per region, and what came back

🔵 **Four regional queries run, one per region, in the region's own idiom where that mattered. An informed gap is recorded as a finding; silence is not.**

| region | query | outcome |
|---|---|---|
| **North America** | `AI education North America 2026 adoption state policy K-12 districts regulation` | 🟢 **New and material**: Ohio's 2026-07-01 district deadline, Idaho S.B. 1227, Oklahoma S.B. 1734, Maryland S.B. 720 (**status contested**), California A.B. 1159, 33–35 states + PR issuing guidance. 🔴 **Gap: nothing on Canada or Mexico.** Every result was US-only. **This region's "North America" coverage is in practice US coverage, and that should be said in a bid rather than papered over** |
| **EMEA** | `AI education EMEA Europe 2026 adoption EU AI Act high-risk schools players` | 🟢 **New and material**: the Annex III high-risk postponement to **2027-12-02** / **2028-08-02** (Reg. (EU) 2026/1744 — **not first-hand**). 🔴 **Gap, and it is the same one as p327: zero named EMEA vendors, zero market-share figures, zero national adoption statistics for the UK, Germany or France.** Nine results, all of them AI-Act explainers. **The EMEA competitive map in this file remains regulation-only, and four consecutive passes have failed to populate it — the query shape is the suspect, per this pass's own retraction of "the query set is exhausted"** |
| **APAC** | `AI education APAC 2026 adoption regulation India China Japan Korea players` | 🟢 **New and material**: Korea's AI Basic Act in force 2026-01-22 with education high-impact + ≥1yr grace; India's Class-3 mandate for 2026–27; China/UAE as the only compulsory national AI curricula; Japan's AI Basic Plan 2026-07-14. 🟡 **Caveat recorded: the education-specific claims trace to a single outlet and could not be corroborated** — government curriculum notices were unreachable. 🔴 **Gap: no named APAC vendors or market sizes** |
| **LATAM** | `AI educación LATAM 2026 adopción regulación Brasil México Chile edtech` | 🟢 **New and material**: UNESCO's LAC observatory (Chile, 2026-04); >50% teacher use in Chile/Brazil vs <10% institutional guidance; Chile Ley 21.719 in force 2026-12-01; Brazil PL 2338/2023 pending in the Câmara; Tec de Monterrey + UNESCO, 44+ programmes. 🔴 **Gap: no edtech market-size figures for Brazil, Mexico or Chile — asked for directly, not returned.** 🔴 **One unsupported claim actively excluded** (the "Ley 21.640 Marco Nacional") |

🔴 **The gap that spans all four regions, and it is the same one for the fourth pass running: this file can place *regulation* by region and cannot place *vendors* by region.** Every regional query returns policy and returns no competitive map. 🔵 **p328's own retraction applies here: four passes of the same bare query shape returning the same nothing is evidence about the query, not about the market. The next pass should drop `players` — which ranks legal explainers — and query the procurement surface instead: national framework agreements, ministry tender portals, and university consortium contracts.**


### Pass 327 — what was searched per region, and what came back

🔴 **All four regional queries returned relevant, correct, already-held material. Zero additions.
Recorded per region because an informed gap is information and silence is not.**

| region | query run | what came back | verdict |
|---|---|---|---|
| **North America** | `AI education North America 2026 adoption regulation players` | H.R. 8747 (K-12 AI Literacy and Readiness Act), California AB 1159 and AB 2876, Katy ISD's K-6 chatbot ban, NYC's moratorium, Canada's June 2026 *AI for All* strategy, the 134-bills-across-31-states count, Oklahoma and Maryland human-oversight rules | 🔴 **0 new — every item already in this file.** The 2025 Executive Order and the *Pledge to America's Youth* are the only items not separately carried, and both are already represented by the policy positions they produced |
| **EMEA** | `AI education EMEA 2026 adoption regulation players` | AI Act (Reg. (EU) 2024/1689) with admissions screening as high-risk, enforcement from **2026-08-02**, June 2026 amendments in force **2026-07-27**, the **Digital Omnibus**, the Commission's ethical guidelines for educators, Erasmus+ 2026 calls, UNESCO GenAI guidance | 🟡 **0 new regulation.** One new citable source: **OECD *Digital Education Outlook 2026*** — recorded above, search-channel only. The "$2.64 B European market" and "10% of institutions have formal guidelines" figures are **vendor roundups with unclear provenance and are deliberately NOT recorded as data** |
| **APAC** | `AI education APAC 2026 adoption regulation players` | **Vietnam Decision 33/2026/QD-TTg** naming education a high-risk sector (already in `intel/policy-matrix.tsv`), South Korea's AI Basic Act and its 2026 grace period, China's content-labelling measures, Singapore's agentic-AI guidance, Japan's AI Promotion Act, India's February 2026 intermediary amendments | 🔴 **0 new.** 🟡 **One unresolved conflict carried forward: sources disagree on Vietnam's effective date (2026-03-01 vs. the 2026-07-02 issuance). The matrix should record both until a primary source settles it** |
| **LATAM** | `AI education LATAM 2026 adoption regulation players` | **UNESCO IESALC**: 200 institutions, 19 countries, **87%** using AI in ≥1 area, **74%** in teaching and learning, only **26%** with a formal AI strategy — **all five figures already in this file.** The **UNESCO Observatory on AI in Education for LAC** (launched 2026-04-14 at ECLAC, Santiago) and its partners **CAF, CENIA, Cetic.br, CEIBAL, Fundación Santillana, Tecnológico de Monterrey, ProFuturo** — all already named here. Uruguay's Council of Europe Framework Convention signature, Peru's sandbox, Colombia's CONPES 4144, Mexico's stalled Senate bill | 🔴 **0 new.** Only **IRCAI** was absent from this file, and a partner-organisation name is not a market finding |

🔵 **The method conclusion, and it should change the next pass's plan rather than its queries.**
**Four consecutive passes of region-by-region sweeping have added nothing.** The eight prescribed
queries are not broken — they return correct, relevant material — **they are exhausted for this
industry.** 🟢 **The channel that returned ten region-placed artefacts this pass was an audit of
this KB's own `evidence/` directory against its four shelf files, at a cost of one command. The
next pass should run that audit first and the sweep second.**

### Pass 326 — what was searched per region, and what came back

**Four regional queries, run as prescribed. Reported as findings, including the empty ones, because
silence and coverage look identical in a file like this.**

- **North America — one promotion, no new intelligence.** The sweep returned US *state* policy only
  and **nothing on Canada or Mexico at the federal level**, which is now the **second consecutive
  pass** with no Canadian education-AI policy from this channel. Every state item returned (Ohio's
  2026-07-01 board-policy deadline, Maryland SB 720's AI coordinator, Idaho SB 1227, Oklahoma's
  parent opt-out, Georgia, Mississippi) **was already carried here.** Only **Illinois HB 316** was
  new to the prose, and it was already in the policy matrix. 🔴 **Declared gap, new: no
  primary-source Canadian provincial or federal AI-in-education policy anywhere in this file.**
- **EMEA — fully re-confirmed, nothing added.** The AI Act dates this file already carries were
  returned independently and **matched on every value**: Regulation (EU) 2026/1744, Annex III
  education deferred to **2027-12-02**, Article 50 transparency live since **2026-08-02**, the
  emotion-recognition ban in educational institutions live since Feb 2025. 🔴 **The
  three-pass declared gap is now four passes old and unchanged: this KB still has no named EMEA
  education-AI vendor list and no primary-source national school AI policy for any single European
  country.** The channel keeps returning the Act and never the countries.
- **APAC — nothing new from either channel.** India's AI and computational-thinking mandate **from
  Class 3 in AY 2026–27** and the **UAE** national K-12 AI curriculum are already carried. New but
  secondary and not written as fact elsewhere in this file: Microsoft Q2-2026 usage figures of
  **17.5%** of working-age people in China and **24.7%** in Japan (**34.5%** of Japanese firms on
  generative AI), and Ipsos support for **banning AI in schools** at **26% India / 29% Japan / 31%
  South Korea**, higher in Australia and New Zealand. 🔴 **Declared gap, new and now specific: the
  data channel that found this pass's largest artefact returned no APAC-authored curriculum dataset
  at any licence.** The channel is known to work; the absence is therefore informative.
- **LATAM — one real addition, one rejection.** Added: **Chile's Ley 21.719**, above. Rejected:
  **"Ley Nahui"**, which does not appear to exist. 🔴 **Declared gap, unchanged: no classroom
  adoption figures — teacher or student usage rates — for any LATAM country.** The regional
  channel returns regulation and forecasts; it has never returned usage. The only measured
  classroom numbers in this file remain Panama's, and they came from a repository, not from a
  survey.

**Pass 325 — the battery ran in full for the FIFTH consecutive saturated pass, it produced exactly
one new figure, and that figure is worse news than the gap it fills.** Recorded in full, because an
unrecorded empty search reads identically to coverage.

- 🔴 **Both primary sources attempted this pass were refused at DNS, and they were the two this
  file has most needed.** `unu.edu` → `getaddrinfo ENOTFOUND` (the **UNU-IAS / UNESCO IESALC**
  working paper *"AI implementation in higher education in Latin America and the Caribbean"* — named
  as the clearest target for the LATAM slot at p323, re-named at p324, **and now unread for a third
  pass for an infrastructural reason rather than for want of trying**). `www.marketsandmarkets.com`
  → `getaddrinfo ENOTFOUND`. 🔵 **Every figure in this file remains snippet-sourced. Three passes
  have now tried to change that and the sandbox is the binding constraint, not the research.**
- 🟡 **LATAM — one new figure, and read the bucket before quoting it.** A market aggregator
  publishes a **"Rest of Latin America" AI-in-education** line: **USD 18.2m (2024) → USD 36m
  (2029)**. 🔴 **This does not close the seven-pass LATAM market-size gap and must not be presented
  as doing so.** *"Rest of Latin America"* is a **residual bucket** — the region minus the markets a
  buyer actually asks about — and at USD 18.2m against the same class of source's **USD 3.68bn**
  North America 2026 figure it is **roughly half a percent of that number.** 🔵 **What it is good
  for:** it is the first LATAM-specific published line this file has found that is not a share of a
  global forecast, and it establishes an *order of magnitude* for the non-Brazil, non-Mexico
  remainder. **What it is not good for: any sentence beginning "the LATAM market is".** The standing
  instruction from p320 holds and is now better supported — **a client asking for LATAM market size
  is asking whether the demand is real, and the adoption and outcome data answer that better than
  any of these forecasts** (and this pass added a measured classroom outcome to the LATAM section
  above, which no forecast in this file can match).
- 🔴 **EMEA — no education-specific result for the THIRD consecutive pass; the gap is five passes
  old.** The query returned enterprise AI material again: CompTIA's 2026 EMEA IT-strategy trends, a
  Workday adoption study (**38% of EMEA organisations have not begun piloting**), a Bandwidth/Cavell
  barriers study, and the EU AI Act as a general adoption driver. **It named no education vendor, no
  ministry programme and no school-data rule** — the search's own stated gap, not only this file's.
  🟢 **But the EMEA gap is materially narrower after this pass for a reason the news channel will
  never supply: the code channel produced a named, dated, licence-verified public-operator stack.**
  `repos/foundations.md` now carries **six MIT repositories from France Université Numérique** — the
  operator of France's national public MOOC platform — covering LRS, analytics, education ERP, forum
  and LTI plumbing. **That is not a vendor list, and it is better than one for a studio: it is the
  software a European public buyer is already running.** The *vendor* half of the gap stands.
- 🔵 **North America and APAC — their own prior contents, re-confirmed, nothing new.** No new
  statute, no new figure, no new player that this file did not already hold. The p323 method
  conclusion stands unchanged and is now five passes stable: **the regional query establishes what
  the channel believes; only a statute-, artefact- or code-level query returns something quotable.**

**Pass 324 — the prescribed eight-search battery was run in full, and for the FOURTH consecutive
pass it added nothing this file did not already hold at equal or higher precision.** That is the
finding, and it is recorded rather than hidden, because an unrecorded empty search is
indistinguishable from coverage. **Every item the four regional queries returned was checked
against this file before being called old**, by token — `IESALC`, `UNU-IAS`, `Observatory`,
`ECLAC`, `AB 1159`, `H.R. 8747`, `omnibus`, `Vietnam`, `AI for All`, `134 bills`, `NYC`,
`moratorium`, `Digital Education Council`, `87%`, `26%` — **and all fifteen were already present.**

- 🟡 **North America — four items returned, all four already held.** 60% of US K-12 teachers used
  AI in 2024-25 and 32% weekly; **134 AI-in-education bills across 31 states in 2026**; California
  **AB 1159** (prohibits using student data to train AI models); the federal **K-12 AI Literacy and
  Readiness Act (H.R. 8747)** advanced out of House committee on 21 July largely along party lines;
  Oklahoma and Maryland requiring human oversight and barring AI from high-stakes decisions about
  students; **NYC's one-year moratorium** on student-facing AI through eighth grade; Canada's June
  2026 **"AI for All"** strategy (national AI-literacy push, watermarking, a Canada Trusted AI
  Certification); Mexico with *"a stack of bills and no regulator to enforce them yet"*; the
  **SREB AI Commission's nine recommendations**; and the student-authored *STUDENTS FIRST Act of
  2026* from a July youth festival. **New this pass: nothing.** 🔵 The one genuinely new item is
  **negative**: a market aggregator putting the North American AI-in-education market at
  **USD 3.68bn in 2026, 36% of global** — a *different* figure from the USD 951m-2024 → USD 2.3bn-2029
  framing this file already records from the same class of source, with no reconciliation between
  them. **Recorded as evidence that this sector's market numbers do not survive comparison, not as
  a market number.**
- 🔴 **EMEA — no education-specific result for the SECOND consecutive pass, and the gap is now four
  passes old.** The generic EMEA query returned the EU AI Act timeline (high-risk duties for
  admissions, assessment and exam scoring from August 2026; AI Office and national enforcement from
  **2 August 2026**; the targeted **"AI omnibus" amendment in force 27 July 2026**), the
  Commission's ethical guidelines for educators, Erasmus+ policy-experimentation calls, a vendor
  estimate of **USD 2.64bn for the European market in 2026** with Finland, Estonia and the
  Netherlands named as K-12 leaders, a *"only 10% of 450+ institutions have formal AI guidelines"*
  survey figure, Germany's €20bn 2025-2030 AI commitment, and the UK's principles-based sector-led
  posture — **all of it already in this file, and the dates independently re-confirmed for the
  third pass running.** 🔴 **Still missing, now four passes: a named EMEA education-AI vendor list,
  and a primary-source national school AI policy for any single European country.** One search
  result stated the same gap in its own words — no consolidated list of EMEA education vendors,
  ministries, or Middle East and Africa national education rules. **The gap is in the sources, not
  only in this file.**
- 🔴 **APAC — corporate and general-AI material for the SIXTH consecutive pass, and the code
  channel beat the policy channel again.** The regional query returned regulation only: **Vietnam's
  high-risk AI list covers education** including automated assessment and behavioural monitoring,
  high-risk *"only when the AI output is used as the sole basis for decisions without meaningful
  human review"*, with the law reported effective **1 March 2026**; **South Korea's** MSIT
  signalling 2026 as a pilot period with a one-year penalty grace under the AI Basic Act; **China's**
  mandatory registration, content labelling and penalties to **CNY 50m**; and Singapore, Japan and
  Australia on voluntary guidance (Singapore's agentic-AI framework is best practice, not law;
  Japan's AI Promotion Act is a principles law with no penalties). On players it named only
  **Google, Microsoft, IBM, Pearson and Byju's** from a commercial report, with China, India and
  Japan dominating. **All already held.** 🔵 **And for the second pass running everything of APAC
  value came from GitHub:** this pass, `Kaiji-Z/LookatStudy` (bilingual, BKT, local-first) and
  `WEIWEI0614/math-bank` (12,030 items against CIE 9709, Edexcel IAL, TMUA, ESAT, BMO, UKMT —
  **the first international-qualification item bank in this KB**). **Method finding, now twice
  measured: for APAC, read the code channel first.**
- 🟡 **LATAM — one new item, and it is a partner list rather than a number.** The regional query
  returned the UNESCO IESALC / UNU-IAS study (**200 institutions, 19 countries, 87% using AI
  somewhere, 26% with a formal strategy, 74% in teaching and learning**, adoption driven by
  individual academics rather than institutional strategy), the **Observatory on AI in Education
  for Latin America and the Caribbean launched April 2026 at ECLAC headquarters in Santiago**, the
  Digital Education Council's 2026 LATAM survey (30,000+ responses, 29 institutions), Uruguay as
  the first LATAM signatory of the Council of Europe AI convention (2025), Mexico's risk-based
  federal bill in the Senate, Colombia's **CONPES 4144** (February 2025), Peru moving to risk-based
  governance, and UNESCO ethics training in Ecuador and Chile — **all already held.** 🟢 **New and
  usable: the Observatory's named partner list** — CAF, **CENIA** (Chile), **CETIC.br** (Brazil),
  ECLAC, Fundación Santillana, **Tecnológico de Monterrey**, ProFuturo, Universidad del Desarrollo
  and **Fundación Ceibal** (Uruguay). For a LATAM public-sector engagement that is the convening
  table, and this file previously named the Observatory without naming who sits at it. **All
  snippet-sourced; `www.digitaleducationcouncil.com` was unreachable in p322 and was not re-tried
  this pass.**

🔵 **The standing conclusion, stated once and not re-argued each pass: the prescribed regional
battery has reached saturation as an intelligence channel.** It now returns this file's own
contents. The channels still producing new regional facts are **the code channel** (GitHub, where
author locale and language place a finding by region) and **targeted statute or artefact queries**
rather than generic regional ones. 🔴 **And the honest caveat on everything in `intel/`:**
**no claim in this file has a primary-source read behind it.** Every figure here is
snippet-sourced from a search result or a secondary aggregator; the first-hand reading in this KB
is all in `agents/` and `repos/`. **The regional half of this base is reportage and its licence
half is measurement. Do not quote them with the same confidence.**

**Pass 323 — the four regional searches were run plus four targeted follow-ups. What each returned,
including the empty ones.**

- **North America — productive, and the only region where the generic regional query was not the
  one that worked.** The generic `AI education North America 2026 adoption regulation players` query
  returned **only market-research and vendor blogs**: a USD 951m-2024 → USD 2.3bn-2029 framing, a 36%
  regional-share figure, the 66%→92% student-usage jump, 10%-of-institutions-with-guidelines and
  71%-of-US-teachers-untrained — **all already held in this file**, plus an unsourced
  "USD 169m government commitment" that **names no government and is not recorded as a fact.** A
  **second, targeted query on the statute layer** produced the dated, named material now in the
  North America opportunities section (Oklahoma SB 1734's dates and duties, Maryland SB 720, Idaho's
  August-2026 framework approval, South Carolina H. 5253 still in committee, and the Alabama/Utah/
  Virginia curriculum mandates). **The lesson is the same one this KB keeps relearning: the regional
  query finds market research; the artefact-or-statute query finds facts.**
- **EMEA — no new market or vendor intelligence; the regulatory timeline re-verified.** The generic
  EMEA query returned **enterprise** AI-adoption material (Eurostat's 5.21%–42.03% member-state
  spread, an AWS-executive interview, a Workday CEO survey) with **nothing education-specific, no
  named EMEA education vendors and no national school-level policy.** A targeted AI Act query
  **independently confirmed every date this file already carries** (Regulation (EU) 2026/1744, OJ
  2026-07-24, in force 2026-07-27, Annex III → 2027-12-02, Annex I → 2028-08-02, Article 50 live
  from 2026-08-02 with the 50(2) grace closing 2026-12-02) and added one secondary-sourced nuance on
  pre-existing systems and "substantial modification". **Declared gap, unchanged and now three
  passes old: this KB still has no named EMEA education-AI vendor list and no primary-source
  national school AI policy for any single European country.**
- **APAC — nothing from the policy channel, the pass's largest artefact from the code channel.** The
  generic APAC query returned **general** regional AI-adoption material (Forrester on fragmented
  legislation, a MarketsandMarkets sizing, CIO-survey governance commentary) and, in its own words,
  **named no education AI vendors and no ministry programmes** — the search's own stated gap, not
  just this file's. **Everything of value for APAC this pass came from GitHub, not from the news
  channel:** K12-KGraph, `civil-ai`, and the persona-skill sub-pattern. **Recorded as a method
  finding: for APAC, the code channel is currently the better intelligence source than the policy
  channel.**
- **LATAM — two real items, both snippet-sourced, and a documented fetch failure.** The Piauí
  statewide AI curriculum figures (AIED 2026 / Springer) and CENIA's **13 of 19** finding are new
  and useful; the **Springer chapter page failed at DNS when fetched directly**, so neither the
  chapter nor its figures have been read first-hand. **Also searched and not found: any 2026
  national AI-in-education regulatory update for Mexico or Chile.** The only Mexico and Chile claims
  the search produced came from a single unverified blog and are **not recorded as facts.** The
  comparative study of Argentina, Brazil, Chile, Peru and Spain and the UNESCO IESALC / UNU-IAS
  survey of 200 institutions in 19 countries (Aug–Oct 2025) are **real and unread** — the clearest
  named target for p324's LATAM slot.

**One cross-regional method note, recorded because it held in all four regions this pass.** The
mandated `AI {industry} {region} {year} adoption regulation players` query shape returns
market-research aggregation in every region. **Every fact added to this file this pass came from a
second, narrower query** — a statute name, a regulation number, an artefact type. **Run the regional
query to establish what the channel believes; run the targeted query to get something quotable.**

**Pass 322 — the four regional searches were run and here is exactly what each returned.** Recorded
in full because an unrecorded region reads identically to a covered one.

- **North America — nothing new.** Returned the 36%-share and USD 951m/2024 market framings, the
  "86% of students across 16 countries" roundup, the 10%-of-institutions-with-guidelines and
  71%-of-US-teachers-untrained pair, OpenAI's eight-partner country programme, and Carnegie
  Mellon/Gates USD 55m courseware. **All already held**, and the regulation commentary was thinner
  than the bill-level tracking already in this file. One unusable item: a "USD 169m committed to
  responsible AI in higher education, Q1 2026" figure **that names no government** — not recorded
  as a fact.
- **EMEA — nothing new from the search channel.** The battery returned enterprise-AI governance
  material (Workday, CompTIA, a Bandwidth/Cavell barriers study) with **no education-specific
  result at all**: no ministry, no edtech vendor, no school-data rule. **Everything EMEA gained
  this pass came from the GitHub channel instead**, and that asymmetry is the finding.
- **APAC — nothing new, and the fifth consecutive pass with no education institution.** All
  education-adjacent hits were corporate L&D again: TCS–Pearson, LearnUpon, NIIT MTS, Alteryx's
  academy, plus OpenAI's ANZ policy appointment. The governance figure that did come back
  (87% encouraging agents, 47% with governance) is an enterprise statistic, not an education one,
  and is **not** recorded as such.
- **LATAM — nothing new, and the gap is unchanged.** The battery returned the Digital Education
  Council survey (92%/79%, 30,000+ responses), IESALC's 200 institutions across 19 countries with
  the 73.5%/57.0%/34.1%/20.0% activity split, the 30%-with-published-policies governance figure,
  the 50/19 feedback gap and the usual Chile/Brazil/Colombia/Mexico policy picture — **every one of
  which this file already holds, most at higher precision.** The two numbers that looked newest
  were checked individually against the KB and were present. **The LATAM supply-side gap stands:
  still no national education code channel, still no LATAM market-size figure that is not derived
  from a global forecast.**

**The method conclusion, now third-pass stable and worth acting on:** for this industry the
prescribed search battery has stopped adding information, while the GitHub channel produced twelve
verified rows this pass. The regional searches are still worth running as a **negative control** —
they are how this KB knows coverage has not changed — but a pass should budget them at a quarter of
its effort, not half. Non-GitHub primary sources remain unreachable from this sandbox
(`www.digitaleducationcouncil.com` → `getaddrinfo ENOTFOUND` this pass), so **every figure in this
file is snippet-sourced and should be re-verified against the publishing house before it reaches a
client deck.**

- ~~**No EMEA AI-in-education market-size figure**~~ — **RESOLVED this pass, with a caveat that
  matters more than the number.** Europe-specific figures exist: **Marketdataforecast ($2.11B 2026
  → $19.97B 2034, 32.47% CAGR, from a $1.59B 2025 base)** and **SNS Insider ($1.46B 2025 → $16.84B
  2035, 27.71% CAGR)**. They disagree on the 2025 base and on the terminal year, neither publishes
  a methodology, and no EUR-denominated figure exists at all. **Quote the range and name the
  houses.** The correction to record for future passes: five passes concluded "it is not published
  — stop looking." It is published; it is just weak, and "weak" is a different answer from
  "absent". **The LATAM market-size gap remains open** — still nothing that is not derived from the
  global forecasts.
- **No AI-in-education adoption rate for MENA or Africa.** Named players and programmes were found;
  a regional adoption percentage was not.
- **No APAC edtech company *ranking*** comparable to HolonIQ's LATAM 100 or TIME's MEA ranking.
  Narrowed this pass: named education-specific APAC players now exist in this KB (**Riiid**, South
  Korea; **Squirrel AI**, China), but no ranked regional market map was found. Generic
  market-report player lists for APAC name Google, Microsoft, IBM, Pearson and Byju's, which is not
  an education-AI map and should not be used as one.
- **No education-specific AI regulation in Brazil or Mexico.** PL 2338 is horizontal, not
  education-specific; Mexico has no binding law. Confirmed absence, not an unsearched gap.
- ~~**South Korea's AI Data Protection Act**~~ — **resolved this pass and corrected: no such act
  exists.** The instrument is the **Framework Act on AI (Law No. 20676, in force 2026-01-22)**; see
  the APAC regulation entry above. The earlier claim came from a low-quality secondary source that
  also misnamed the statute, and one source found this pass explicitly contradicts it. **Retire the
  old wording wherever it has been reused.**
- **The Australia/Japan "stricter data governance" claims remain unverified** and came from the same
  weak source. What *is* supportable for Australia: **no AI-specific statute and mandatory guardrails
  paused**, with existing technology-neutral law applying.
- **Vietnam's AI law dates conflict across sources** (education transition given as 2026-08-15 in
  one, 2027-09-01 in another). Verify against the primary text before quoting either.
  **Pass 320 narrowed this from a contradiction to a testable hypothesis.** A source this pass
  describes **2026-08-15 as a grandfathering cutoff** — education AI systems already operating
  before it get **six further months** — which would make the two dates complementary rather than
  conflicting. **Still snippet-sourced (`www.lw.com` unreachable), so the gap stays open**, but the
  next pass should test *that* reading against the primary text rather than re-discovering the
  conflict. Also new and worth verifying with it: education is **one of six high-risk sectors**, and
  the high-risk trigger is reported as the output being **the sole basis for a decision without
  meaningful human review** — if correct, **a human-in-the-loop design may avoid the class
  altogether**, which changes the commercial shape of a Vietnamese engagement.
- **No education-specific provision found in Taiwan's AI Basic Act (new gap, pass 320).** The
  statute and its March 2026 implementing committee were found; **nothing on education
  classification, high-risk scheduling or school guidance was.** Declared rather than left silent
  because this is a named instrument with a live committee, i.e. the most likely APAC jurisdiction
  to produce education rules next. **Sweep it first next pass.**
- **No new LATAM demand-side intelligence this pass (pass 320), searched and empty.** The regional
  query returned only already-carried material. Recorded here because this KB's standing instruction
  is that **an unrecorded empty search is indistinguishable from coverage.** Both standing LATAM
  gaps — market size, and open-source supply — are unchanged.
- **The LATAM market-size gap stands, seventh pass — but it matters less than it did.** Still no
  region-specific commercial forecast that is not derived from the global numbers. What changed is
  that the alternative evidence is now strong enough to carry a conversation on its own:
  institutional adoption (UNESCO IESALC: **87% using AI, 26% with a strategy**, 200 institutions,
  19 countries), **country-level teacher adoption** (UNESCO 2024: Brazil 56%, Chile 55%, Colombia
  53%, Costa Rica 52% vs an OECD average of 36%; Uruguay 75% of public-school teachers in a later
  survey), the DEC LATAM survey's 92%/79% engagement and 50/19 feedback gap, company-level funding,
  and now **a measured technical result from the region** (31.9% → 2.3% curriculum hallucination,
  `repos/foundations.md`). **Stop treating the missing forecast as the problem: a client asking for
  LATAM market size is usually asking whether the demand is real, and the adoption data answers
  that better than a forecast would.**
- **This pass could reach github.com and nothing else, so the whole of this file is
  snippet-sourced. Named so no one assumes otherwise.** Refused at connect time by the egress
  policy: `www.unesco.org`, `arxiv.org`, `education.ec.europa.eu`,
  `digital-strategy.ec.europa.eu`, `www.koreaherald.com`, `www.k12dive.com`, `www.multistate.us`,
  and (carried from pass 318) `www.iadb.org`, `www.digitaleducationcouncil.com` and
  `www.iesalc.unesco.org`. **Everything in `agents/top.md`, `repos/foundations.md` and
  `verticals/solutions.md` this pass was read first-hand off GitHub; everything in this file was
  not.** Brief on it, name the house or publisher, and confirm before a client document. The UNESCO
  IESALC 87/26 figures were read first-hand in an earlier pass and are unaffected. **An unreachable
  source is not a verified one, and recording the difference is the whole point of this section.**
- **Three specific claims this pass declined to adopt, after searching for them.** (1) The
  **"nearly two-thirds of European education systems have an AI strategy, guidance or policy
  framework"** figure: searched directly, not found in any Commission source, **do not quote.**
  (2) A **November 2026** date for the Commission's education package: the Commission texts say
  "later this year", so the month is unverified. (3) A **Q3 2026 edtech-specific venture funding
  total**: does not appear to be published yet; Crunchbase's $159B Q3 figure is **all sectors** and
  must not be repurposed. Also rejected outright: a circulating "EdTech funding fell 89%" headline
  and an undated "$410M invested in 2026" figure, both of which conflict with HolonIQ's and
  Crunchbase's H1 numbers.
- ~~**South Korea's AI-textbook reversal is an August 2026 event.**~~ **CORRECTED this pass: it was
  2025-08-04.** The amendment narrowed the textbook definition to printed books and e-books,
  excluding "learning support software using intelligent information technology", and schools lost
  funding support. Adoption had already decayed within 2025 (~37% of eligible classes in the first
  semester to 19% in the second; schools ~4,190 → 2,095; roughly 30% of schools overall, 98% in
  Daegu to 8% in Sejong). **The error came from a regional-roundup snippet and it changed the
  meaning of the finding** — a completed experiment with outcome data, not breaking news. The
  "$850M spent" figure circulating with it comes from a low-quality blog and is not adopted here.
- **No verified, machine-readable NCERT/CBSE curriculum dataset (APAC).** Declared this pass after
  sweeping GitHub's `ncert` and `cbse` topics: nothing above 15 stars that is curriculum
  infrastructure, the one MCP server unlicensed and LLM-tagged without verification, the best data
  asset a 2018 school scrape. **This is a gap with a template** (`bncc-dev`, Brazil) **and a hard
  deadline** (Classes 3–8, 2026-27). See the APAC opportunities above and pattern P10.
- **Moodle's AI placements could not be confirmed against primary documentation.** Secondary
  sources report two core placements (text editor, course support) in the 5.x AI subsystem; the
  official placements page was not read this pass. Verify before it enters a proposal.
