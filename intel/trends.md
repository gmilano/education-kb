---
industry: education
region: Global
updated: 2026-11-07
---

# 📡 Trends — Education

> What is actually changing in AI + education as of November 2026. Each trend names its evidence and its confidence.

🔴 **Read this before citing any `T` number: four identifiers on this page resolve to two different trends each, and `156` references across the shelves point at them.** Re-measured at p685 by counting headings rather than trusting the last figure: **`87` `## T` headings, `83` distinct numbers, `0` gaps** — 🔄 **re-derived at p687: `93` headings, `89` distinct numbers, `max = T93`, and now `4` gaps at `T84`–`T87`.** 🟢 **Those four gaps are the reservation this banner's own repair plan created, not a defect — do NOT close them.** p685 set aside `T84`–`T87` to receive the renumbered second occurrences of `T31`/`T32`/`T39`/`T40`; p686 then filed `T88`–`T90` and p687 `T91`–`T93`, both correctly numbering from `max(## T)` and stepping over the reserved block. 🔴 **A future pass that re-derives this census will see `4` gaps and may read them as a numbering error. Reusing `T84`–`T87` for new trends would consume the only free identifiers the collision repair can land in, and the repair would then have nowhere to go.** The reserved block is load-bearing; the next `T` number is `T94` — so the heading count is *not* the trend count (the `distinct` vs `total` distinction this page records as **T62**). The collisions are **`T31`, `T32`, `T39` and `T40`**, each used once by `p657`/`p658` and again by `p661`/`p664`:

| id | first use | second use | shelf references |
|---|---|---|--:|
| `T31` | psychometric measurement layer (`p657`) | regional "zero" as a query artefact (`p664`) | `43` |
| `T32` | spoken assessment (`p657`) | LATAM adoption vs licensability (`p664`) | `36` |
| `T39` | permissive code around unlicensed courseware (`p658`) | absence claims refuted in logs (`p661`) | `47` |
| `T40` | Scratch's two licences (`p658`) | "no permissive supply" claims as adoption gaps (`p661`) | `30` |

🔧 **`p671` annotated the four *headings* and stopped there, which fixed the symptom a reader sees on this page and left the one they cannot see.** A reader arriving from `**T39**` on `repos/foundations.md` still has no way to know which of two unrelated trends was meant.

🔴 **p685 deliberately did not repair it, and the reason is a data-integrity one rather than a scheduling one.** Renumbering the second of each pair to free identifiers (`T84`–`T87`) is mechanical, but **rewriting the `156` citations is not**: each site meant one specific trend, that intent is not recoverable from the token `T39`, and a bulk reassignment would silently point a documented claim at the wrong evidence. **A wrong citation is worse than an ambiguous one, because it reads as resolved.** The repair is therefore: renumber the four second-occurrence headings, then disambiguate references **one at a time, by reading each site**, and leave `T31`/`T32`/`T39`/`T40` permanently retired rather than reused. 🔵 **Until that is done, every `T31`/`T32`/`T39`/`T40` citation on these shelves should be read as naming a *pair*, not a trend.** New trends are numbered from `max(## T)`, never from the last heading in file order — `p685` filed **T82** and **T83** that way and both are unique.

## T91 — An Apache-2.0 payload's byte count is not its identity, and this pass measured five of them
*Added p687. Confidence: **high** — five payloads read first-hand the same day, every size and digest reproduced.*

This base already records (**T56**) that `11,357` and `11,358` are two different Apache-2.0 canonicals and that size alone cannot tell them apart. p687 shows the ambiguity is not a pair — it is a **sliding window**, and the window now has five measured positions:

| bytes | sha256₁₂ | what it is | API `license` field |
|--:|---|---|---|
| `10,172` | `59899c6091b5` | canonical, clause 4(a) wrapped one way — `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | 🟢 `Apache-2.0` |
| `10,173` | `c4a2cd14eb3a` | **same licence text**, clause 4(a) wrapped the other way — `learning-commons-org/agent-skills` | 🟢 `Apache-2.0` |
| `11,356` | `f1a2e5fccede` | canonical with the appendix placeholder **filled on one line** — `122-syf-wcy/PhysicsOS` | 🟢 `Apache-2.0` |
| `11,356` | `43070e2d4e53` | 🔴 **the `11,357` canonical with its trailing newline stripped by a shell capture** — a measurement error, not a payload | — |
| `11,357` | `c71d239df917` | the `apache/.github` canonical — `ably-labs/realtime-quiz-framework`, `THU-MAIC/MAIC-Core` | 🟢 `Apache-2.0` |
| `11,505` | `4b6615cdb446` | canonical with the appendix **block replaced** by a completed notice — `rasbt/LLMs-from-scratch` | 🔴 **`NOASSERTION`** |

Three results follow, and the third is the expensive one.

**(1) The `10,172`/`10,173` byte is a line re-wrap, not a licence difference.** `diff` gives one changed pair inside clause 4(a): `"…of the Work or / Derivative Works…"` against `"…of the Work or Derivative / Works…"`. Two legitimate upstream reflows of identical terms.

**(2) `11,356` is occupied twice, by a real payload and by an error.** `122-syf-wcy/PhysicsOS` genuinely measures `11,356 B` because filling `Copyright [yyyy] [name of copyright owner]` → `Copyright (c) 2026 PhysicsOS contributors` is one character shorter. And `printf '%s' "$(cat canonical)" | wc -c` → `11356` for the `11,357` canonical, because a shell capture strips the trailing newline — the defect p674 proved on `Opetushallitus/compleap`. **A cell reading `11,356 B` without a digest cannot say which of the two it saw.** Write the payload to a file and hash the file; never measure through `$(...)`.

**(3) 🔴 Filling the appendix can cost you the licence field, and the threshold is how much canonical text survives.** `PhysicsOS` filled **one line** and still matches `Apache-2.0`. `rasbt/LLMs-from-scratch` replaced **the whole appendix block** with a real notice (`Copyright 2023-2026 Sebastian Raschka` plus the completed *"Licensed under the Apache License…"* paragraph), `+148 B`, and the SPDX matcher stops recognising it — so **`gh api` reports `NOASSERTION` on a verbatim Apache-2.0 grant held by a `107,940★` repository.** A licence filter over the API field drops the highest-starred repository on this base's foundations shelf. **The remedy is not a better filter; it is reading the payload.** Consistent with p686's finding that `NOASSERTION` carries no information, now with the *mechanism* named rather than just the spread.

## T92 — `curl -sSL` without `--fail` makes a 404 into a 14-byte document, and this pass measured its own probe doing it
*Added p687. Confidence: **high** — caught in p687's own instrument, with the artefact reproduced.*

p687 measured README language shares to place regions. For `SafeExamBrowser/seb-server` the probe reported **"README `14 B`, CJK `0`"**. There is no `README.md` in that repository — the document is `README.rst`. `curl -sSL` returned GitHub's `404` body, the literal bytes `404: Not Found`, **with exit status `0`**, and the measurement was computed over that string.

🔴 **A 14-byte README is not a terse README; it is the absence of one, wearing the shape of data.** Every pipeline in this base that reads a URL into a buffer and then measures the buffer is exposed: CJK share, title-line grading, byte counts, digests. A digest of `404: Not Found` is a perfectly stable, perfectly reproducible, perfectly wrong digest — and it is the *same* digest (`d5558cd419c8`) on every repository that lacks the file, so it will even cross-validate against itself.

**Rule:** `curl --fail --silent --show-error --location`, check the HTTP status explicitly, and treat any payload under ~`64 B` as a probe failure to be investigated rather than a value to be recorded. 🔵 This is the same class as **T56** and **T91(2)**: in all three, the instrument produced a number that was internally consistent and described bytes the repository does not serve.

## T93 — The mandated search legs report this sector late, and the lag is now quantified at `-19.4%`
*Added p687. Confidence: **medium-high** — two first-hand comparisons, one of them large; the direction is structural, the magnitude is a sample of two.*

This base has recorded `29` consecutive passes in which the eight mandated legs produced no new address. The standing interpretation has been that the legs are saturated. p687 adds a second, sharper reading: **the legs are not just saturated, they are stale, and the staleness is measurable.**

| subject | figure the leg returned | first-hand, same week | error |
|---|--:|--:|--:|
| `HKUDS/DeepTutor` | `45,224★` (October roundup) | **`56,080★`** | 🔴 **−19.4%** |
| `THU-MAIC/OpenMAIC` | *"about 42K★"* | **`42,851★`** | ≈ −2% |

The mechanism is not error, it is **latency**: a roundup's number is frozen at publication while the repository keeps moving, and the search channel surfaces roundups in preference to repositories. The bias is therefore **one-directional** — always low, never high — which is exactly what a filter tuned on adoption thresholds will mis-rank.

🔵 **Two consequences for how this base should be read.** First, a nil streak on these legs is evidence about the *channel*, not about the sector: `DeepTutor` added `~10,800★` in the window the legs described as quiet. Second, any star figure this base publishes must name whether it is first-hand or cited, because the two are not the same kind of number — which is why every star cell added at p687 states the ref and date it was read at.

## T1 — The agentic classroom arrives, and it simulates peers

The year's structural shift is from *tutor* to *classroom*. OpenMAIC (Tsinghua, MIT, **42.7k ★**, v1.4.0 released 2026-11-04) generates a full lesson from a topic or document and staffs it with AI teachers **and AI classmates** that speak, draw on a shared whiteboard and argue with each other. DeepTutor (HKU, Apache-2.0, **55.0k ★**) holds the one-to-one position with a persistent learner model.

Together these two repositories hold ~98k stars — more adoption than every other open source education project combined. **Confidence: high** (both verified first-hand this pass).

**Why peer simulation matters:** a one-to-one tutor cannot produce disagreement, and disagreement is where a good deal of learning happens. This is a genuinely new capability, not an incremental one.

## T2 — The reference stack is MCP + LangGraph

OpenMAIC orchestrates with LangGraph. `canvas-mcp` (MIT, 317★) exposes ~102–128 LMS tools over the Model Context Protocol, and `tutor-mcp` packages Bayesian Knowledge Tracing itself as an MCP server. Bloom (MIT, 302★) ships as a Claude Code skill *and* a web app.

The pattern has settled: **pedagogy in MCP servers, orchestration in LangGraph, the LMS left untouched.** That is good news for licence containment (see T6). **Confidence: high.**

## T3 — Usage has outrun governance, and governance is now the buying trigger

86% of education organisations use generative AI and most have no policy. 54% of K-12 students and 92% of university students use AI. In LATAM, >50% of teachers in Chile and Brazil use AI tools while <10% of institutions have formal guidelines (UNESCO).

The consequence for sellers: in 2026 the thing a client lacks is usually **control**, not capability. Governance frameworks, audit trails and policy enforcement are the wedge; the tutor is what gets bought afterwards. **Confidence: high.**

## T4 — Agent deployment is still rare, which is where the work is

The Bridges 2026 survey of K-12 and college leaders found relatively few institutions running agents in daily operations, with leaders explicitly unwilling to give agents access to sensitive student data. Pilots exist for tutoring and enrolment.

The gap between chatbot adoption (near-universal) and agent deployment (rare) is precisely the systems-integration gap. The blocker named by buyers is **data access governance**, not model quality. **Confidence: high** (survey-based).

## T5 — One LATAM deployment is the proof point the industry lacked

A Chilean university reported **194 pedagogical agents across ~100 courses serving 4,600+ students** (February 2026). This is the largest concrete agentic-education deployment surfaced anywhere in this pass — and it is in LATAM, not North America or Europe.

**Confidence: medium** (single secondary source, institution unnamed in the reporting). Worth verifying directly; if it holds, it is the strongest reference case available for the region.

## T6 — The institutional LMS is no longer copyleft-only: there is an Apache-2.0 platform, and it has the LLM layer in-tree

🔴 **This entry has now been wrong twice and is being rewritten a second time. Both earlier versions are withdrawn.**

| Pass | What this entry claimed | Why it failed |
|---|---|---|
| ≤ p650 | "Open source education has no permissive platform, only permissive components" | `learningequality/kolibri` is MIT, 1.2k ★, a production offline-first platform |
| p651–p652 | "No permissive platform **of the Moodle / Open edX class**" — i.e. institutional course management | `OpenOLAT/OpenOLAT` is **Apache-2.0**, 449 ★ / 167 forks / **32,210 commits**, and is institutional course management: courses, enrolment, assessment, QTI testing, portfolio, curriculum management |

**The current claim, and this one is a count rather than a generalisation.** Across fifteen platform rows: **ten copyleft** (GPL-3.0: Moodle, Chamilo, ILIAS, Gibbon; AGPL-3.0: Open edX, Frappe LMS, Veo; GPL-2.0: RosarioSIS, openSIS; LGPL-3.0: OpenEduCat) and **five permissive** (Apache-2.0: **OpenOlat**; MIT: Kolibri, Richie, GegoK12; ECL-2.0: Sakai). One of those five is in the institutional class. The licence-only objection to a permissive institutional deliverable is gone.

🟢 **And the part that matters more than the licence:** OpenOlat ships `langchain4j` 1.23.0 (Apache-2.0) in `pom.xml` with the OpenAI, Anthropic and **embeddings** modules, plus Apache Lucene. Read at first hand from the manifest on 2026-11-04. Because `langchain4j-open-ai` speaks the OpenAI-compatible wire protocol that Ollama and vLLM both serve, **an in-jurisdiction no-egress deployment is a configuration change, not a fork** — which is exactly the architecture EMEA public education keeps asking for.

🔵 **The methodological finding, which generalises past education.** This base missed OpenOlat for seven consecutive passes because every pass ranked the platform shelf by stars. OpenOlat's star:commit ratio is **1:72**. A star-ordered channel buries a 32,000-commit university LMS beneath tutorial repositories — and this base had already written down the reason (it notes that Moodle has *more forks than stars*, "a codebase institutions take copies of, not a project people watch") without applying it to its own instrument. **Institutional software is under-starred by construction. For the platform shelf, rank by licence or by commit depth; a star floor is the wrong tool.** The row came back from one licence-first query.

**What has *not* changed, and still governs most engagements:** the LMS a client *already runs* is almost always copyleft — Moodle and Chamilo across LATAM and EMEA K-12, Canvas and Blackboard across North America. Stock-platform-plus-out-of-tree-agent remains the common case. What changed is the **greenfield** choice.

## T7 — The EU's high-risk deadline moved to December 2027, and most guidance is stale

The Digital Omnibus (Regulation (EU) 2026/1744) deferred high-risk obligations for stand-alone education AI from 2 August 2026 to **2 December 2027**. Article 50 transparency duties still apply from 2 August 2026. Emotion recognition in schools has been banned since February 2025. Article 4's AI-literacy duty was softened to "taking measures".

**Most published guidance still cites August 2026 and is wrong.** That is itself a commercial opening: clients working from stale advice are either over-panicking or mis-scoped. **Confidence: medium** — multiple secondary sources agree, but Commission primary text was not read this pass. Verify before quoting to a client.

## T8 — Regulation is diverging by region, not converging

| Region | Shape |
|---|---|
| EMEA | Horizontal, binding, risk-tiered, dated |
| North America | Sub-national patchwork: 134+ bills across 31 states |
| APAC | Service-by-service (China), labelling-first (India), voluntary (Japan) |
| LATAM | Largely pending; only Peru enacted |

A single global compliance posture is no longer achievable. Multi-region clients need per-jurisdiction policy nodes in the agent itself — a concrete architectural requirement, not a legal footnote. **Confidence: high.**

## T9 — Knowledge tracing is still research-grade, not productised

pyKT (MIT) is the field's reference implementation at **457 stars** — not the 1.2k this KB previously published. OATutor (MIT, 276★) is the main production-grade BKT system.

🔴 **One piece of evidence in this entry is withdrawn.** It previously read "`tutor-mcp` packages BKT as an MCP server but has **0 stars**". That measured `kvnloo/tutor-mcp`, which the repository page states is a **fork**; the upstream `ArnaudGuiovanna/tutor-mcp` has **96 ★ / 13 forks** and packages BKT *and* FSRS spaced repetition behind one MCP tool surface. The broader claim stands on pyKT (457★) and OATutor (276★); the 0-star datum does not.

The honest read: knowledge tracing is scientifically mature and commercially immature. Budget real integration effort; do not promise adaptive mastery modelling as an off-the-shelf component. **Confidence: high** (star counts measured directly) — but see **T13**, because the adjacent problem of *review scheduling* has an answer that knowledge tracing does not.

## T10 — The evidence base remains the sector's weak point

A July 2026 scoping review of **474 studies** found the field fragmented, with pedagogical design poorly connected to technical capability. A 2025 study found AI tutors adapt worse in real time than human tutors, following predictable response patterns.

Sophisticated buyers know this, which is why 2026 procurement favours measured pilots. **Ship with measurement attached** — pre/post assessment, retention tracking, teacher time saved. An engagement that cannot show an effect will not renew. **Confidence: high.**

## T11 — Public support for banning AI in schools is rising in parts of APAC

Ipsos Education Monitor 2026, support for a ban: South Korea 31%, Japan 29% (**up from 21%**), Malaysia 29%, Singapore 28%, India 26%, Thailand 25%, Indonesia 23%; Australia and New Zealand higher still.

Roughly a quarter to a third of the public in major APAC markets would ban AI in schools outright. Visible, teacher-in-the-loop designs are the commercially safer posture there. **Confidence: high** (single reputable polling source).

## T12 — Binding, education-specific AI regulation is no longer only a European phenomenon

**South Korea's AI Basic Act (Law No. 20676) has been in force since 22 January 2026**, and its "high-impact AI" definition names **AI used for student assessment in early-childhood, elementary and secondary education**. Operators must determine whether their system qualifies before deployment and must make efforts to assess its impact on fundamental rights beforehand. MSIT has signalled a grace period of at least one year before administrative fines, putting the enforcement edge around **January 2027** — *earlier* than the EU's deferred high-risk date of 2 December 2027. Vietnam's Law on AI has been in force since 1 March 2026.

**Why this matters more than a second data point:** until this pass, "conformity by design" was an EMEA offer and APAC was characterised as service-specific, labelling-first and voluntary. That characterisation is now incomplete. The same engagement shape — risk classification, documentation, human oversight, impact assessment on the assessment and placement use cases — is sellable in two jurisdictions against two dates, and the Asian one lands first. A client operating in both needs **one conformity programme with two jurisdictional profiles**, which is a larger and more defensible engagement than either alone.

**Confidence: high** on the statute, its date and the education clause (multiple independent legal-practice sources and the official text's definition agree). **Medium** on the grace-period length, which is reported as "at least one year" and should be confirmed with MSIT before being relied on contractually.

## T13 — Spaced repetition is the one permissive education algorithm that is already in production

The pattern across this KB has been permissive-but-research-grade (pyKT, 457★) or adopted-but-copyleft (every institutional platform). **FSRS breaks it in both directions at once.**

| | Reading |
|---|---|
| `open-spaced-repetition/fsrs4anki` | **MIT**, 4.1k ★ — scheduler plus an optimiser that machine-learns parameters from a learner's own review history |
| `open-spaced-repetition/fsrs-rs` | **BSD-3-Clause**, 456 ★ — the embeddable Rust engine; bindings for C, Python, Node.js, Dart, PHP |
| Adoption | **The algorithm ships inside Anki itself from v23.10** — mainstream production software, consumer scale, not awaiting integration |

Knowledge tracing answers *"does this learner know X?"*. FSRS answers *"when should this learner see X again?"* — and the second question is the one that drives retention, which is the outcome institutions actually measure. The two are complementary, and `ArnaudGuiovanna/tutor-mcp` (MIT, 96★) already exposes both behind one MCP tool surface.

**Why it is commercially interesting:** it is permissive, per-learner optimisable, computable on-device with no model call, and already validated at scale. It is therefore the cheapest credible "measured outcome" a pilot can ship — see **T10**, where the sector's weak evidence base makes measurable retention the difference between a pilot that renews and one that does not. **Confidence: high** (licence payloads read byte-for-byte; the Anki integration is stated in the project README).

## T14 — African education AI is real, offline-first, and built on open weights rather than released as open source

Previous passes recorded "no Africa-specific data" as a gap. The gap was in the search, not the territory — and what the territory contains has a consistent shape:

- **Demand and public investment are moving.** Google launched a free, **offline-capable** AI and digital-skills training platform for Nigeria and other African markets around **3 November 2026** (English, Swahili, Arabic; Hausa being added; lessons downloadable over Wi-Fi then usable without mobile data). Saudi Arabia and the UAE, at the other end of EMEA, have made AI literacy a mandatory or system-wide part of education.
- **Builders exist and are product companies, not projects.** **Mdali** (Johannesburg) adapts open-source models into an offline-first CAPS Grades 10–12 maths tutor that runs on basic phones and keeps student data on-device. Nigeria's EDAT piloted offline-sync tutoring across 60+ Edo State secondary schools. Kenya's M-Shule and Ghana/Côte d'Ivoire's Chalkboard Education are older precedents in the same mould.
- **But the code is not open.** No African open-source education repository was found at any adoption level. These products are built *on* open weights and released as **proprietary applications**.

**The commercial reading, which is different from every other region:** elsewhere the motion is "adopt the regional open source stack and extend it". For Africa there is no stack to adopt, so the motion is **co-development with existing product teams**, and the differentiating capability is offline-first architecture rather than model work. The one thing that would change this is the stated Google/Fab AI programme with innovators in Kenya, Ghana and South Africa, under which **datasets, evaluation suites and open-source models are to be published**. Worth watching specifically.

**Confidence: medium.** Every item rests on secondary reporting; `blog.google` does not resolve under this session's network policy, so Google's own announcements could not be read first-hand. The *absence* of African open-source supply is the better-evidenced half, since it survived a dedicated search.

## T15 — The EU is now the *last* of three binding education-AI deadlines, not the forcing function

This page has treated the EU AI Act as the sector's clock since it was written. At p652 that is no longer accurate, and the correction changes how a multi-region programme should be sequenced.

| Date | Jurisdiction | Trigger |
|---|---|---|
| **≈ January 2027** | South Korea | Administrative fines become available after MSIT's signalled grace period. Student assessment in early-childhood, elementary and secondary education is **high-impact by statute**. |
| **1 September 2027** | Vietnam | Compliance deadline for education systems already operating before 15 August 2026. **Decision 33/2026/QD-TTg** lists 46 high-risk systems across six sectors; **education is three of them**. |
| **2 December 2027** | EU | Stand-alone Annex III high-risk obligations, after the Digital Omnibus (Regulation (EU) 2026/1744) deferred them from 2 August 2026. |

**Why it matters, beyond the ordering.** The EU deferral bought European clients sixteen months of runway and bought APAC clients nothing — so the two regions this KB has long characterised as "the regulated one" and "the supply one" have swapped position on urgency. Vietnam's trigger is also the sharpest-edged of the three: the high-risk classification bites **only where results serve as the official basis** for assessing learning outcomes or ranking learners, which makes the architecture decision — formative tool versus system of record — the compliance decision.

Three consequences: a proposal that frames December 2027 as "the deadline" is eleven months late for any client with Korean exposure; a multi-region conformity programme should be sequenced to the Korean date with EU and Vietnamese profiles layered on, not the reverse; and **"APAC is the supply side" and "EMEA is the compliance side" are both now wrong** — APAC is both.

**Confidence: medium-high on the dates** (consistent across multiple legal-practice summaries), **low on clause-level detail** — no primary Korean, Vietnamese or Commission text has been read at first hand in any pass.

## T16 — The licence unit is the dependency graph, not the repository

Every pass of this KB has got more rigorous about reading `LICENSE` from bytes. p652 found the limit of that discipline: three separate findings, all the same defect, none of them detectable by reading `LICENSE`.

| Project | Badge | What is in the tree |
|---|---|---|
| **OpenMAIC** (42.7k★, this KB's #2 agent) | MIT | `packages/mathml2omml` is **LGPL-3.0-or-later** — 7,652 B payload, `"license": "LGPL-3.0-or-later"` verbatim in its `package.json`, declared `"workspace:*"` in the root manifest, and compiled as the **first step** of `build:packages`. A deliverable built from OpenMAIC links it. |
| **OmniEdu** (590★) | Apache-2.0 | The payload covers the **code**. The weights — the artefact a client deploys — have **no named grant anywhere in the repository**: *"Model weights and third-party datasets and benchmarks retain their respective licenses."* Backbones are Qwen. |
| **open-moodle** (0★) | MIT | Depends on **PyMuPDF (AGPL-3.0)** for PDF extraction, stated in its own README. |

LGPL-3.0 is not the GPL and does not make a whole application copyleft; it requires that the component stay replaceable with its source available, and "or-later" means a client cannot freeze the terms. For a bundled, transpiled JavaScript component in a shipped web app that is an engineering requirement rather than a formality. **Workable — but it has to be designed in, and nothing on the badge says so.**

Alongside these, this base now holds **five distinct grant-defect classes** in education open source, four of which pass a licence-badge check: grant absent while a README asserts permissiveness; grant complete but delegating copyright to a missing `COPYRIGHT` file; grant replaced by a 19-byte pointer to its own name (`frappe/education`: `License: GNU GPL V3`); grant complete but contradicted by the README (`protorubric`: Apache-2.0 payload, MIT README); and grant permissive but not covering the artefact that matters (`Omni-Edu`).

**The operational rule:** read `LICENSE` *and* the manifests — `package.json`, `pyproject.toml`, `Cargo.toml` — and for a model, read the weight card. **Confidence: high.** Every item was read from bytes or from the manifest field verbatim.

## T17 — Education gets its own open-weight foundation models, and FP8 makes it a deployment story

Until p652 every agent on this shelf was an application calling somebody else's general-purpose model. **OmniEdu** (Apache-2.0 code, 590★ / 93 forks, Peking University + UCAS + Zhongguancun Academy, arXiv:2609.23088, 22 September 2026) is the first education-domain open-weight family this base has found: 4B / 9B / 27B, trained on 69,999 instruction examples and 15.96M supervised response tokens across subject competence, curriculum grounding, diagnostic reasoning and pedagogical scaffolding.

**The number that makes it operational is not a benchmark, it is a file size.** The FP8 checkpoints are 37–44% smaller than BF16: 27B at 28.30 GiB against 50.96, 9B at 11.09 against 17.53, 4B at 5.14 against 8.46. A ~11 GiB curriculum-grounded tutoring model is single-GPU, in-jurisdiction, no-egress and offline-capable — which is simultaneously the EMEA data-residency architecture, the Sub-Saharan African offline-first architecture and the Korean/Vietnamese "keep it off the system of record" architecture. One artefact answers the binding constraint in three regions.

**Two caveats, both load-bearing.** The benchmark results are self-reported (27B: K12-Bench 63.12 EM / 76.69 F1, MathFish 85.89, EDUMATH MaC 86.95, MathTutorBench Scaffold 78.74, against 16 compared models). And **the weight licence is unknown** — see T16. **Confidence: high on the artefact's existence and composition** (repository and README read at first hand), **nil on the weights' usability** (`huggingface.co` does not resolve in this session).

## T18 — Open source invested in Canvas-shaped institutions, and the bill lands in LATAM and EMEA

This KB declared in every prior pass that no permissively-licensed Moodle-side agent existed. p652 searched the category properly: **seven MIT Moodle MCP servers exist, in five languages** — Rust, Python, TypeScript, Go and Python again — one with full write coverage and a web-service escape hatch.

**And the entire category tops out at 27 stars.** `canvas-mcp`, doing the identical job for Canvas, sits at 317★. Six of the eight Moodle servers measured have four stars or fewer.

So the gap was never a supply gap. It is a **consolidation and adoption gap**, and it is distributed along exactly the fault line that matters commercially: Canvas dominates North American higher education, Moodle dominates LATAM and much of EMEA, and open source has put roughly **12× more reviewed effort** into the agent layer for the former. A LATAM or EMEA client running Moodle is paying for that asymmetry in integration risk, and the honest scoping consequence is that **the Canvas pattern is cheaper than the Moodle pattern today** and should not be priced as though it were not.

The useful half: adopt-and-harden is a weeks-scale input, not a build. `G36maid/moodle-mcp` is the only credible base — most tools, most commits, broadest version claim (Moodle 3.7 → 5.x), real write support — and the engagement is hardening it and contributing upstream. **Confidence: high.** All eight repositories were verified from bytes and their pages measured on 2026-11-04.

## T19 — The strongest statement of this sector's evidence problem now comes from model builders, not critics

**T10** has recorded for several passes that the sector's weak point is its evidence base, resting on third-party analyses. At p652 the claim acquired a better source: the OmniEdu authors, reporting what they say are the leading open-weight results across curriculum-grounding and pedagogical-tutoring benchmarks, write in their own README:

> "Benchmark performance does not establish classroom learning gains."

The OECD says the same thing from the policy side in the **Digital Education Outlook 2026** (January 2026): tools with an intentional pedagogical purpose *"tend to show sustained improvements in learning"*, while *"if designed or used without pedagogical guidance, outsourcing tasks to GenAI simply enhances performance with no real learning gains"* — and it recommends that *"education systems should incentivise the development of tools that aim to enhance teaching and learning"*. And the demand side agrees it has not happened: only **15% of students** say AI is integrated into many of their courses and only **29%** think their instructors are equipped to guide its use (Digital Education Council global survey 2026), against **87% institutional adoption but ~9% outcome evaluation** in LATAM (UNESCO IESALC).

**The convergence is the finding.** Builders, the OECD and students independently describe the same hole: performance has been demonstrated, learning has not, and almost nobody is measuring. Two commercial consequences. First, **measurement is a product** — an evaluation wrapper whose deliverable is the client's own evidence is the one offer that does not require anyone to believe a vendor's efficacy claim, and in a market where 9% of institutions evaluate anything it is close to uncontested. Second, an OECD recommendation to incentivise purpose-built tools over general-purpose chatbots is a policy tailwind under precisely the shelf in `agents/top.md`. **Confidence: high on the quotations and the survey figures; the OECD text is quoted from search excerpts of the PDF because `www.oecd.org` does not resolve in this session.**

## T20 — Permissive assessment software exists now; the *agentic* half of it **also does** — the research-artefact claim is withdrawn 🔴 corrected at p657

Four passes of searching produced, in order: nothing; two education-specific graders with **no usable grant**; one permissive general rubric primitive that is **not** education-specific (`microsoft/LLM-Rubric`, MIT, 45★); and at p653, searching the automated-essay-scoring literature rather than the agent ecosystem, **two permissive education-specific systems**.

| Project | Licence | Adoption | What it is |
|---|---|---|---|
| `wwrwbs/AI_AWE` (**ArguLens**) | Apache-2.0 (notice form) | **2★ / 2 commits** | Scorer **and** label-aware feedback generator. Decomposes AES into a discourse-move classifier, a grade-independent LightGBM scorer over 31 features, and feedback generation. arXiv:2608.17356 |
| `littlecookie0722/AI-Teaching-Agent` | MIT | **0★ / 30 commits** | Exam generation plus a `WAITING_REVIEW` human-approval state machine, Docker-sandboxed grading, no auto-publish. Author declares grading and MCP tracks **frozen** |

**The trend is the shift in the *kind* of gap, and it is the second time this base has seen that shift.** The Moodle bridge went from "no permissive supply" to "seven MIT servers capped at 27★" — a consolidation gap. Assessment has now made the same move: from absent to present-but-unadopted. **This is a better commercial position than it sounds**, because adopt-and-harden against a peer-reviewed decomposition is scopeable, while building a grader from zero is not. It is also the one place in this KB where the production artefact would be Globant's to create.

🔴 **The half that has not moved is the regulated half.** Scoring now has permissive research supply; **assessment *integrity* and proctoring have none, in any pass** — and under EU AI Act Annex III that is the high-risk half, with emotion recognition in schools prohibited outright since February 2025. Permissive supply is appearing where the regulatory exposure is lowest.

🔴 **Refined at p656, and the original heading was too strong.** This trend read *"all of it is a research artefact"*. [`numbas/Numbas`](https://github.com/numbas/Numbas) is **Apache-2.0** (11,357 B, byte-exact canonical), **216 ★ / 129 forks**, pushed 2026-10-28, and is the browser e-assessment system **Newcastle University builds and runs for its own teaching** — randomised question generation, algebraic answer marking, partial credit, SCORM packaging. That is production university software, not a paper's companion code, and it was already present in this repository's logs when the claim was published. The defensible core of the trend survives and is now the heading: **agentic** assessment — LLM scoring, generated feedback, agent-run marking — remains research-grade, and the two rows in the table above (2 ★ and 0 ★) are still the whole permissive supply for it. 🔵 The regulated half named below has not moved either: assessment *integrity* and proctoring still have no permissive production supply, with `SafeExamBrowser` (MPL-2.0, 363 ★) the nearest thing and deliberately not shelved pending a pass that can scope proctoring properly. Shelved at p656 on `repos/foundations.md` and `verticals/solutions.md`.

🔴 **Corrected at p657, and this time the heading itself was wrong.** The claim that the agentic half of permissive assessment is a research artefact rested on two repositories at **2 ★** and **0 ★**. [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) is **MIT** (1,091 B payload read on its real default branch, `develop`), **826 ★ / 395 forks**, pushed **2026-11-05**, latest tag **`10.3.1`**, built and operated by **TUM for its own teaching** — and it ships **three AI subsystems in the tree**: **Iris**, an LLM tutor that guides with hints and leading questions; **Athena**, which suggests feedback on text, modeling and programming submissions; and **Hyperion**, AI-assisted exercise authoring on Spring AI. All three are configuration-gated. That is permissively-licensed, production, agentic assessment running against real cohorts, and it was reachable by searching `topic:autograding` — a topic head no prior pass had swept.

🔵 **The same sweep found three more permissive production autograders this KB did not hold**: `autolab/Autolab` (Apache-2.0, 808 ★, CMU), `Submitty/Submitty` (BSD-3-Clause, 805 ★ / **1,119 forks**, RPI) and `ucbds-infra/otter-grader` (BSD-3-Clause, 162 ★, Berkeley, **and it grades R as well as Python**). With `nbgrader` and `Numbas`, that is **six** permissive production assessment systems, not one exception.

🟢 **What survives, and it is the part worth keeping.** The split **T24** argues for — deterministic grading for what is checkable, calibrated LLM rubrics for what is not, a human decision boundary on anything consequential — is not weakened by this correction; `Artemis` and `Submitty` both *implement* it, `Athena` **suggests** feedback rather than issuing it and Submitty's manual-grading workflow is first-class. 🔴 **And the regulated half has still not moved: assessment integrity and proctoring have no permissive production supply in any pass**, with `SafeExamBrowser` (MPL-2.0, 363 ★) the nearest thing. Permissive supply continues to appear where regulatory exposure is lowest.

🔵 **The method lesson, repeated for the third pass running: saturation is a property of the query.** p656 wrote that sentence about `topic:xapi`. This pass proves it again on a claim this KB had already "refined" once — a refinement that corrected the scope of the error without re-testing its premise. **When a trend is refined rather than retested, re-run the search that produced it.**

## T21 — Local-first by default is becoming a product category, not a deployment option

Three independent signals converged in this base's measurements this pass, and none of them is a cloud product:

- **`zijinz456/OpenTutor`** (MIT, **166★**, 274 commits) defaults to **Ollama**, with the README claiming *"no API keys required, no data leaves your machine"*, and ships **FSRS 4.5** in-tree. Cloud providers are the alternative, not the default.
- **`OpenOlat`** (Apache-2.0) carries `langchain4j-embeddings` — embeddings computed in-process — and Lucene, so semantic search over course content needs no external call.
- **`OmniEdu`**'s FP8 checkpoints (9B ≈ 11 GiB) put a curriculum-grounded model on one GPU, and `Kolibri` (MIT) already runs with no connectivity at all.

**Why this is a trend and not a coincidence:** the three forces pushing it are all strengthening at once — EU AI Act deployer obligations on schools, the sovereignty turn in EMEA public procurement, and the plain fact that student data is minors' data under LGPD, FERPA/COPPA and GDPR alike. The commercial consequence is concrete: **"nothing leaves your hardware" is now demonstrable in an afternoon with permissively-licensed parts**, where a year ago it was an architecture diagram. That is the fastest-moving sales argument on this shelf, and `compose/patterns.md` P7, P9 and P11 all now rest on it.

## T22 — Licence form and licence hygiene are independent variables

p653 catalogued a **sixth** grant-defect class — *grant by reference*: the Apache-2.0 **notice** (the short boilerplate for source headers) used in place of the licence terms, as in `wwrwbs/AI_AWE`'s 1,865-byte `LICENSE`. It is materially stronger than Class 5 (`frappe/education`'s 19-byte `License: GNU GPL V3`) because it carries the operative grant language, the exact version and the canonical URL; what it omits is the copy of the text that Apache-2.0 §4(a) obliges a redistributor to provide. Usable, with a one-line upstream fix.

🔵 **The instructive part is the inversion.** Those same 1,865 bytes enumerate every component and its licence, name the vendored paths, and state what is deliberately **not** redistributed (the Qwen2.5-7B base model; the academic-use-only Persuade 2.0 corpus), closing with a bias notice against high-stakes automated use. That is better licence hygiene than any other repository this base has read — **while the 42.7k★ repository with a byte-perfect MIT payload quietly builds an LGPL-3.0-or-later component.**

**The operational rule this yields:** a short or unusual grant file is a reason to **read** it, not to reject the project; and a perfect grant file is not evidence about the tree. Five of the six defect classes pass a licence-badge check. The sixth fails the badge and passes on substance. Badges measure neither.

## T23 — The permissive-platform claim has collapsed completely, and the blind spot was vocabulary, not availability 🟢 new at p655

This base spent six passes asserting that no permissively-licensed production LMS existed, narrowed it at p651, and retracted it at p653 when `OpenOLAT` (Apache-2.0) was found after seven passes of looking. **p655 shows the retraction was not enough.** Three more permissive platform-class projects were found in a single pass: **`jupyterhub`** (BSD-3-Clause, **8,362★**), **`oppia`** (Apache-2.0, **6,974★**) and **`mentingo`** (MIT, 106★). Two of them out-adopt every copyleft platform this KB tracks except `edx-platform` itself.

**The diagnosis matters more than the rows.** None of the three was hidden; all three were missed because they do an education job without education vocabulary — JupyterHub calls itself infrastructure, Oppia calls itself a learning platform for *explorations*, Mentingo files itself under corporate L&D. **The search instrument was looking for the word "LMS".** Trend-level statement: in 2026 the permissive education stack is substantially larger than keyword search on education terms reveals, and any claim of the form "there is no open source X for education" should be treated as a statement about the searcher.

**Signal:** 5 permissive platform-class rows at p655 against 2 at p653, with no new releases in between — pure measurement, not market change.

## T24 — The assessment gap had a permissive answer the whole time, and it is deterministic rather than AI 🟢 new at p655

Four consecutive passes searched for a permissively-licensed education grader and reported the field as unlicensed or research-grade; the best available row was `microsoft/LLM-Rubric` at 45★. **`jupyter/nbgrader` — BSD-3-Clause, 1,370★, pushed 2026-11-03 — has been autograding university coursework for roughly a decade.**

**The reason it was invisible is the trend.** Every pass searched for an *AI* grader, and nbgrader is not one: it runs tests, allocates points per cell, and separates release → collect → autograde → **manual grade** → feedback. In 2026 the instinct is to look for the LLM-shaped answer to an assessment problem, and for the checkable half of assessment the pre-LLM answer is better — auditable, deterministic, reproducible, and already acceptable to an academic board. **The defensible architecture is a split, not a model:** deterministic autograding for what is checkable, calibrated LLM rubrics for what is not, and a human decision boundary on anything consequential — which is also what the **DC OSSE ban on AI in grading and discipline decisions** and **NY A 9190** make legally necessary in North American K-12.

**Signal:** this KB's own declared assessment gap closed at p655 by a project older than the LLM era.

## T25 — Open edX's official agent bridge arrived, and it is AGPL — the licence boundary inside the stack is now fixed 🟢 new at p655

The Open edX project announced **Open edX MCP** through its own blog in September 2026: a Django app (`blend-ed/openedx-mcp`) plus a Tutor plugin (`blend-ed/tutor-contrib-openedxmcp`) exposing staff and superuser administration operations to MCP clients, targeting the **Ulmo** release. Both grant payloads were read at p655: **34,522 bytes, GNU Affero GPL v3** — matching `edx-platform` itself. `openedx/openedx-ai-extensions`, the official AI-helpers plugin, is the same.

This settles a question this KB has carried open, and settles it negatively: **the official route from an agent into Open edX is network-copyleft, and the permissive route into that stack remains `XBlock` (Apache-2.0) and nothing else.** The practical consequence is a clean architectural line rather than a problem — AGPL components run as separate, unmodified services behind their own network boundary; client IP lives in XBlocks and in out-of-tree agents. ⚠️ Note the correction this forces: earlier notes in this programme described `openedx-ai-extensions` as Apache-2.0. **It is Affero.**

**Signal:** 4 of 4 official-or-announced Open edX AI/agent components read at p655 are AGPL-3.0. Zero permissive.

## T26 — The permissive shelf is tilting from tutors to delivery, and content generation now outnumbers conversation 🟢 new at p655

Of seven agent rows added at p655, **six generate or schedule content rather than converse with a learner**: `Papermorph` (book → animated narrated explainer, 1,211★), `claudemy` (topic → cited audio-lesson course, 611★), `anki-mcp-server` (agent → spaced-repetition scheduler, 544★), `wordlink` (offline fine-tuned 1.5B in-browser vocabulary trainer, 280★), `AILearningGuide` (58 offline labs, 248★) and `lumen` (one-sentence goal → private course + cited RAG tutor, 92★). All MIT, all payloads read at first hand.

**Two structural reads follow.** First, `anki-mcp-server` completes a chain this KB has been assembling for three passes: FSRS (`fsrs4anki` MIT, `fsrs-rs` BSD-3-Clause) is the retention algorithm, `tutor-mcp` (MIT) is the mastery estimator, and this is the tool surface that lets an agent *write into* the scheduler that already ships inside Anki — see **T13** and `compose/patterns.md` **P6**. Second, `wordlink` is the first row on the shelf that **ships its own task-specific fine-tuned weights small enough to run in a browser tab**, which is the EMEA data-residency and low-connectivity argument demonstrated in working MIT code rather than argued. ⚠️ Its code grant is MIT; the weights carry no separately named licence — the same defect this KB flags on `OmniEdu`, and now visibly a pattern rather than an incident.

**Signal:** 6 of 7 new permissive rows at p655 are delivery-shaped; 1 is a tutor.

## T27 — The interoperability layer is permissive and the content layer is copyleft, and the line between them is clean 🟢 new at p656

p656 read the grant payload of every open source component in the layer that joins an AI tool to an institution. The licence split is not a tendency; it is a clean break along a functional boundary:

| Sub-layer | What it does | Licences measured | Verdict |
|---|---|---|---|
| **LTI 1.3** | Launches a tool inside an LMS | Apache-2.0 (`tsugi`), MIT (`pylti1.3`, `marsha`), BSD-3 (`ltiauthenticator`) | 🟢 **Entirely permissive** |
| **SCORM / cmi5** | Plays existing packaged courseware | MIT (`scorm-again`) | 🟢 Permissive |
| **xAPI / LRS** | Records what the learner did | Apache-2.0 (`xAPI-Spec`, `lrsql`, `ADL_LRS`, `TinCanJS`) | 🟢 **Entirely permissive** |
| **Assessment** | Delivers and marks | Apache-2.0 (`Numbas`) vs GPL-2.0 (`tao-core`) | 🟡 Split |
| **Interactive content authoring** | Builds the content | GPL-3.0 (`h5p-php-library`, `H5P-Nodejs-library`), no grant (`Lumi`) | 🔴 **Entirely copyleft** |
| **Accessibility remediation** | Finds and fixes WCAG defects | GPL-3.0 (`UDOIT`, `adapt_framework`) | 🔴 **Entirely copyleft** |

**Why the break falls there, and why it is stable.** The permissive half is the half written by *specification bodies and their implementers* — ADL (US Department of Defense), Rustici, 1EdTech's ecosystem, IMS LTI. A specification wants maximum adoption, so its reference implementations are Apache or MIT by design. The copyleft half is the half written by *product communities* — H5P, Adapt, UDOIT — who chose GPL precisely to keep commercial forks out. 🔵 **This is not an accident of sampling and it will not drift: the incentives that produced each half are still in place.**

**The commercial consequence is a scoping rule.** Globant can own the pipes — get in over LTI, move content over SCORM, record to an Apache-2.0 LRS, assess with Numbas — and must treat authoring and accessibility as *integrate, do not fork*. See `compose/patterns.md` **P17** and `verticals/solutions.md` **Pattern I**. **Confidence: high** — every licence in the table was read byte-for-byte from `raw.githubusercontent.com` on the repository's real default branch, not taken from a GitHub sidebar.

## T28 — The sector's measurement problem had a permissive answer the whole time, and there is exactly one of it 🟢 new at p656

T10 and T19 have recorded across many passes that the evidence base is this sector's weakest point — and T19 noted that the sharpest statement of the problem now comes from model builders rather than critics. p656 closes the *supply* half of that gap and replaces it with a narrower, harder one.

**The answer exists:** xAPI is a ratified Apache-2.0 specification, and a Learning Record Store is the database that implements it — every learner interaction as a statement with actor, verb, object, result and timestamp, queryable by the client's own analysts. This is what turns "the tutor seems to help" into a cohort delta somebody can audit. [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) is **Apache-2.0** (11,357 B, byte-exact canonical), 144 ★, pushed **2026-11-03**, nine open issues, running on SQLite, PostgreSQL and MySQL.

🔴 **And there is exactly one.** The field around it is copyleft, dormant, or both:

| LRS | Licence | Last push | Status |
|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 | **2026-11-03** | 🟢 **The only live permissive option** |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | Apache-2.0 | 2025-11-14 | ⚠️ ~12 months quiet — reference, not production |
| [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | 🔴 GPL-3.0 | 🔴 2024-05-30 | 🔴 Copyleft **and** dormant ~17 months. 584 ★ — the one a client most likely already runs |

**So the gap moves rather than closing.** It was *"no permissive way to measure outcomes."* It is now *"one permissive way to measure outcomes, maintained by one small project, with no permissive fallback."* That is a better problem — it is buildable today — but it is a single-vendor dependency and any proposal selling measurement on a permissive stack should name it. 🔵 **The failure was never discovery: `lrsql` appears in 230 files of this repository's own logs, described there as the permissive production candidate, and had never reached a shelf.** **Confidence: high** on the licences and dates (all measured this pass); **moderate** on `lrsql`'s project health, which rests on commit recency and issue count rather than on any funding or governance signal.

## T29 — The April 2026 US accessibility deadline decomposes into four capabilities, and three of them had permissive answers in this base's own logs all along 🔴 corrected at p661

This base records an **April 2026 ADA deadline for large US public institutions** as a North America demand driver, alongside the state-level activity in T3 and T12. p656 swept for the supply side and the result is negative:

- `topic:accessibility topic:education` returns **442 repositories**. Star-ranked, the permissive rows at the top are `evoluteur/braille-tools` (MIT, 43 ★) and `osunyorg/admin` (MIT, 49 ★) — **neither is a WCAG remediation tool.**
- The production tool is [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) — scans Canvas content for WCAG defects, explains them, fixes many in place, University of Central Florida, 117 ★, pushed 2026-11-04 — and it is 🔴 **GPL-3.0** (35,147 B payload read).
- The authoring tool with accessibility as a design goal, `adaptlearning/adapt_framework` (632 ★), is also 🔴 **GPL-3.0**.
- `screen-reader`, `captioning`, `dyslexia` and `special education` return **zero rows on any shelf** of this KB, before and after this pass.

**Why this is a trend and not merely a gap.** Every other regulatory driver this base tracks — the EU AI Act's Article 50 transparency duty, Korea's high-impact assessment scope, US state model policies — creates demand that *permissive software can serve*. Accessibility is the exception: the mandate is hard, dated and enforceable, and the only real tool forbids a proprietary derivative. 🔵 **The engagement shape is therefore different in kind:** deploy UDOIT inside the client's own estate, bill the remediation work and the integration, and ship no derivative. It is a services engagement, not a product one — and saying that up front is more valuable than discovering it after a proposal has promised a platform. **Confidence: high** on the licence and the supply absence (both measured); **moderate** on the deadline itself, which this KB carries from secondary sources and has not read in primary form.

🔧 **CORRECTED AT p661 — the headline claim above is withdrawn, and the paragraph below replaces it.** What was true: `topic:` and star-ranked queries over `accessibility`, `captioning`, `screen-reader` and `dyslexia` return nothing usable, and no shelf row carried those tags. What was false: the inference drawn from it — *"the one named demand driver in this KB with no permissive answer"*. **The mandate is not one capability, and this base held production-grade permissive answers to three of its four parts without ever shelving them.**

| Capability the April 2026 deadline actually creates | Permissive answer | Verified first-hand at p661 |
|---|---|---|
| **Caption existing lecture video and audio** — by volume, the largest task the deadline creates | [`openai/whisper`](https://github.com/openai/whisper) | 🟢 **MIT**, `1,063 B`, `sha256₁₂ b5d65a59060e`, **`111,975★`**, pushed `2026-08-31` |
| **Make mathematical content accessible** (speech, braille, navigation) | [`NSoiffer/MathCAT`](https://github.com/NSoiffer/MathCAT) | 🟢 **MIT**, `1,065 B`, `sha256₁₂ f8f65c73234f`, DAISY-sourced, ★ unmeasured (three channels refused) |
| **Audit course pages for WCAG defects** | [`GoogleChrome/lighthouse`](https://github.com/GoogleChrome/lighthouse) | 🟢 **Apache-2.0**, `11,358 B`, **`31,019★`**, pushed `2026-11-04`, **runs locally** |
| **Repair WCAG defects *in place* inside an LMS course** | [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) | 🔴 **GPL-3.0**, `35,147 B`, `117★`, pushed `2026-11-04` — **still the only tool** |

🔵 **So the engagement conclusion narrows from the whole mandate to one quarter of it.** *"Deploy UDOIT in the client's estate, bill the remediation, ship no derivative"* is correct **only** for in-place WCAG repair. Captioning, mathematical accessibility and auditing all permit a closed, client-branded deliverable — and captioning is the biggest piece of the work. The useful sentence for a proposal is therefore the opposite of the one this trend used to carry: **most of an accessibility remediation programme can be built permissively; the last mile inside the LMS cannot.** Shipped as `compose/patterns.md` **P26**.

🔴 **Why the claim survived five passes.** It was checked against the shelves and refuted only in the logs — see **T39**. `whisper` is named in *both* append-only logs as *"the ASR baseline"*. **Confidence: high** on all four licence readings (payloads byte-read this pass); **moderate** on the April 2026 deadline itself, which this base still carries from secondary sources and has never read in primary form — that half of T29 is unchanged and still unverified.

## T30 — Autograding is not an AI story and not a thin layer: it is university infrastructure, permissively licensed, and six systems deep 🟢 new at p657

Across p652–p656 this base searched for education *agents* and for *AI* graders, found the field thin, and recorded the thinness as a market gap. The thinness was in the query. Sweeping `topic:autograding` — **94 repositories, never swept before** — returns a shelf of production systems each run by the university that wrote it:

| System | Licence | ★ / forks | Institution | Pushed |
|---|---|--:|---|---|
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **MIT** | **826 / 395** | TUM | **2026-11-05** |
| [`autolab/Autolab`](https://github.com/autolab/Autolab) | 🟢 **Apache-2.0** | **808 / 234** | Carnegie Mellon | 2026-11-03 |
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | 🟢 **BSD-3-Clause** | **805 / 1,119** | Rensselaer | **2026-11-05** |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3-Clause | 1,370 | Project Jupyter | 2026-11-03 |
| [`okpy/ok`](https://github.com/okpy/ok) | 🟢 Apache-2.0 | 370 / 88 | UC Berkeley | ⚠️ 2025-07-02 |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 BSD-3-Clause | 162 / 80 | UC Berkeley DS | 2026-11-01 |

**Three structural reads.** First, **not one of the six is copyleft** — MIT, Apache-2.0 and BSD-3-Clause throughout, which is the opposite of the pattern on the LMS and content shelves and consistent with **T27**: this software was written by universities for peer adoption, not by product communities defending a market. Second, **`Submitty` has 1,119 forks against 805 ★ and `Tango` has 63 against 49** — the adoption signature of infrastructure institutions copy and run, so star counts systematically *understate* this layer. Third, **the sector's grading problem was never a supply problem; it was a discovery problem**, and the thing that hid it was filing autograders as developer tooling rather than as education software.

**Commercial consequence:** the credible engagement is **adopt-and-harden** — deploy, integrate over LTI, migrate real exercises, calibrate, train graders — not build. Any proposal to write a grader from scratch for a university client should now have to argue against six working systems. See `compose/patterns.md` **P19** and `verticals/solutions.md` Pattern J.

## T31 — The psychometric measurement layer is permissive, complete, and almost entirely dormant 🟢 new at p657 🔧 **`p671`: this identifier is used twice on this page.** `p664` reused `T31` for an unrelated trend (the query-language artefact). Both are kept — `82` cross-page references point at the four duplicated numbers and renumbering would break every one — so each collision is named at both ends instead. **This is the `p657` `T31`.**

This base has held knowledge tracing (`pyBKT`, `pykt-toolkit`) for several passes and **T9** correctly called it research-grade. It never held **psychometrics**, which is a different question: knowledge tracing predicts *whether the next answer will be right*; psychometrics estimates *how hard each item is, which skills a learner actually holds, and which item to ask next*. Only the second yields the calibrated item parameters an adaptive test is built on. Sweeping `topic:psychometrics` (517 repos), `topic:item-response-theory` (153) and `topic:computerized-adaptive-testing` (24) returns a full pipeline, all permissive:

| Stage | Component | Licence | ★ | Live? |
|---|---|---|--:|---|
| Parse the client's item bank | [`bigdata-ustc/EduNLP`](https://github.com/bigdata-ustc/EduNLP) | Apache-2.0 | 64 | 🔴 2024-03 |
| Cold-start calibration data | [`tswsxk/EduData`](https://github.com/tswsxk/EduData) | Apache-2.0 | 83 | 🔴 2023-05 |
| Fit item difficulty / discrimination | [`eribean/girth`](https://github.com/eribean/girth), [`17zuoye/pyirt`](https://github.com/17zuoye/pyirt), [`inuyasha2012/pypsy`](https://github.com/inuyasha2012/pypsy) | MIT | 127 / 111 / 242 | 🔴 2022 / 2023 / **2018** |
| Diagnose which skills are held | [`bigdata-ustc/EduCDM`](https://github.com/bigdata-ustc/EduCDM) | Apache-2.0 | 203 | 🔴 2024-10 |
| Predict the next response | [`bigdata-ustc/EduKTM`](https://github.com/bigdata-ustc/EduKTM) | Apache-2.0 | 267 | 🔴 2024-01 |
| **Choose the next item** | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | BSD-3-Clause | 153 | 🟢 **2026-11-01** |
| Learned selection policies | [`bigdata-ustc/EduCAT`](https://github.com/bigdata-ustc/EduCAT) | MIT | 77 | 🔴 2024-08 |

🔴 **One of seven stages is maintained.** `catsim` — BSD-3-Clause, tag `0.9.1`, default branch **`dev`** — is the only live component, and it happens to be the one that matters most, because it is the piece that converts a question bank into an adaptive test and the piece `compose/patterns.md` **P4** has assumed for several passes without naming.

**This is a different kind of gap from T28's and should be scoped differently.** T28 found *one live permissive LRS with no fallback* — a single-vendor dependency. Here the **mathematics is published and stable** (IRT is five decades old; these are implementations of textbook estimators, not model wrappers that rot), so dormancy is a far smaller risk than it looks: a 2022 maximum-likelihood 2PL fitter is not stale in the way a 2022 LLM integration is. ⚠️ **But the engagement must own them.** Any proposal built on this layer is taking maintenance responsibility for unmaintained code, and should price that in explicitly rather than describe seven dormant repositories as a stack. See `compose/patterns.md` **P18**.

## T32 — Spoken assessment is a layer this KB had never seen at all, and it has a permissive answer that displaces a paid API 🟢 new at p657 🔧 **`p671`: duplicate identifier — `p664` reused `T32`. This is the `p657` `T32`.**

Before this pass, `grep` for `pronunciation` and `speech assessment` across all eight shelves returned **zero files** — and, unlike the p656 interop finding, **zero files in the 5.8 MB and 4.5 MB append-only logs as well.** Not held-but-unshelved: genuinely never seen. `topic:pronunciation` (331 repositories) returns a working stack:

- [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) — **MIT**, 184 ★, pushed 2026-08-15. Phoneme-level assessment: a score, the mispronounced words with the sounds **actually heard in IPA**, a confidence per word, the transcription, and pitch and energy curves. Wav2Vec2 + DTW, **CPU-only**, `pip install openpronounce`.
- [`Kyubyong/g2p`](https://github.com/Kyubyong/g2p) — **Apache-2.0**, 936 ★. English grapheme-to-phoneme: the reference the learner is scored against.
- [`CUNY-CL/wikipron`](https://github.com/CUNY-CL/wikipron) — **Apache-2.0**, 376 ★, live. Pronunciation lexicons mined across **hundreds of languages**, which is what makes this multilingual rather than English-only.
- [`liguozheng-ac/japanese-speech-xray`](https://github.com/liguozheng-ac/japanese-speech-xray) — **MIT**, 177 ★, live. Prosody and pitch-accent, which phoneme scoring alone cannot represent.

**Two things make this commercially unusual for this KB.** First, **it displaces a named line item rather than filling a vacuum**: `OpenPronounce` is positioned by its own author as a self-hosted alternative to **Azure Pronunciation Assessment**, so the proposal is a metered cloud cost replaced by a container in the client's estate — and because voice is biometric-adjacent personal data, that *removes* an EMEA transfer question instead of answering it. Second, the licence advantage runs **against** adoption: the better-known project in the layer, `Thiagohgl/ai-pronunciation-trainer` (525 ★), is 🔴 **AGPL-3.0** and cannot be a client deliverable. ⚠️ **State two boundaries in writing:** a single maintainer at 184 ★, and **phoneme accuracy is not fluency and not a CEFR level** — it does not replace a human oral examiner.

**Regional fit is the strongest of any finding this pass:** English-language training is a large, funded, measurable LATAM and APAC market, and `wikipron` means Spanish and Portuguese learners can be scored on the same stack.

## T33 — The credential-issuing layer is the mirror image of T27: entirely copyleft, with exactly one permissive exception 🟢 new at p657

**T27** established a clean functional break — the *interoperability* layer (LTI, SCORM, xAPI) is permissive because specification bodies write it, while the *content* layer (H5P, Adapt, UDOIT) is copyleft because product communities write it. Credentialing is the second case, and sharply:

| Project | Function | Licence (payload read) | ★ |
|---|---|---|--:|
| [`learningeconomy/LearnCard`](https://github.com/learningeconomy/LearnCard) | Issue / earn / store / share / map credentials | 🟢 **MIT** (1,109 B) | **70** |
| [`fedora-infra/tahrir`](https://github.com/fedora-infra/tahrir) | Open Badges issuer | 🔴 **AGPL-3.0** (34,917 B) | 85 |
| [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) | Course / conference certification | 🔴 **AGPL-3.0** (33,820 B) | 64 |
| [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) | Open Badges 3.0 / W3C VC library | 🔴 **LGPL-3.0** (7,650 B) | 2 |
| [`edubadges/badgr-ui`](https://github.com/edubadges/badgr-ui) | Badgr front end (SURF edubadges) | 🔴 **AGPL-3.0** | — 🔴 **archived** |

🟢 **`LearnCard` is the only permissive route, and it is a real one:** its monorepo package list, read this pass, carries `vc-plugin`, `vc-api-plugin`, `openid4vc-plugin`, `sd-jwt-vc-plugin`, `didkit-plugin`, `did-web-plugin` and `chapi-plugin` — **W3C Verifiable Credentials, VC-API, OpenID4VC, SD-JWT-VC and DIDs**, standards rather than a bespoke badge format — and it ships an **agent skill** (`npx @learncard/cli skill install`), which makes it directly composable with `agents/top.md`. Pushed **2026-11-05**.

⚠️ **And it is 70 ★ with 42 open issues and one sponsoring organisation.** That is the same single-vendor shape **T28** flagged for `lrsql`, and it should be named in any proposal rather than discovered during delivery. 🔵 **Why the break falls where T27 predicts:** `LearnCard` is written by a *standards-adjacent* body (Learning Economy Foundation, in the 1EdTech/W3C orbit) and the copyleft rows are *products* — badge platforms defending a market. T27's incentive argument holds on a layer it was not derived from, which is the first out-of-sample test it has passed.

## T34 — Skills-based credentialing is a named 2026 buying trend, and the permissive supply for it is one project 🟢 new at p657

1EdTech's own 2026 watch-list names **skills-based credentialing** alongside AI governance as the year's structural shifts, driven by employer expectations moving from degrees to demonstrated skills. Campus Technology's 2026 survey of industry leaders describes AI becoming core infrastructure across **admissions, advising, accessibility and administration** rather than standalone pilots — all four of which are credential- and record-shaped workloads.

**So the demand signal and the supply constraint are both unusually crisp**, and they point in opposite directions: a named, dated, employer-driven buying trend met by **one MIT project at 70 ★** (see **T33**). This is the third demand driver in this KB whose supply side is a single point of failure — alongside `lrsql` for measurement (**T28**) and nothing at all for accessibility remediation (**T29**).

🔵 **The pattern across all three is worth stating as a rule, because it keeps recurring:** where education's demand is *regulatory or institutional* (accessibility mandates, evidence duties, credential recognition), permissive supply is one project deep or absent; where demand is *pedagogical* (tutoring, content generation, autograding), permissive supply is abundant. **Globant's differentiated work is therefore concentrated on the institutional side**, because that is where there is nothing to adopt — and it is also where the client cannot buy an alternative. See `compose/patterns.md` **P21**.

## T35 — The 2026 consensus is governed, purpose-built education AI — and three independent bodies now say the same thing 🟢 new at p657

**T3** recorded that usage had outrun governance and that governance had become the buying trigger. The 2026 sources converge further, and the convergence is the trend:

- **OECD**, *Digital Education Outlook 2026*: move beyond general-purpose AI tools toward **purpose-built educational AI** — curriculum-aligned, with safeguards for minors.
- **1EdTech**, 2026 watch-list: the field is moving **from experimentation to governance**, with explicit policy and oversight as the central concern.
- **HolonIQ**, 2026 Education Trends Snapshot: buyers now favour approaches that demonstrate **instructional value** over broad personalisation promises.
- **Campus Technology** (industry-leader survey): AI as **core operational infrastructure** across admissions, advising, accessibility and administration, not pilots.
- 🆕 **European Parliament (EPRS)**, briefing `784574`, *“Artificial Intelligence in Classrooms: Pedagogical Dimensions”* (`15` pp., Vasiliki Charisi, requested by the CULT Committee) — **read at p669, and it is a fourth independent body saying the same thing**, this time from the EU's own research service and aimed at primary and secondary education: *“A learner-centred approach requires that clearly defined educational objectives, rather than technological capabilities, guide the use of AI in classrooms.”* It names **insufficient pedagogical guidance in classroom AI tools** as a concern. ⚠️ **Evidence class: a search-index read, not a byte-read** — `www.europarl.europa.eu` does not resolve in this session; see the host bullet below. 🔵 **The heading of this trend says “three independent bodies” and the list now carries four. The list is the derived figure and the list is what to count** — `668-O`'s defect is that every derived figure goes stale independently, so the count is stated here rather than buried in a heading written at p657.

⚠️ **One adoption statistic qualifies all of this and should travel with it: 85% of educators report feeling unprepared to manage generative AI in the classroom** (Azumo's 2026 compilation of secondary sources — treat the figure as indicative, not measured). Against **60% of US teachers already using AI tools** (Gallup, n > 2,200), the gap between use and readiness *is* the services market.

**Commercial reading, and it is a reversal of the 2024–25 pitch.** "A general assistant for your institution" is now the weaker proposal; the stronger one is narrow, curriculum-aligned, evidenced and governed — which is exactly what the permissive stack on these shelves supports: `Artemis` with AI configuration-gated per cohort, `lrsql` producing an auditable statement log, `catsim` making item selection explainable rather than learned, and a human decision boundary wherever a jurisdiction requires one. 🔵 **The one claim to avoid** is that purpose-built means proprietary: three of the four bodies above are standards or policy organisations, and their recommendation is satisfied better by auditable open components than by a closed product.

## 🔴 What this page does not claim

- 🟢 **Retracted at p655: the assessment gap.** This page carried "no permissive education-specific grader exists" for four passes. `jupyter/nbgrader` (BSD-3-Clause, 1,370★) existed throughout. See **T24**. What survives of the claim is narrower and still true: **no permissive proctoring or assessment-integrity tool was found**, in five passes of searching.
- 🔴 **No primary regulatory text was read at p655 either**, unchanged for four passes. The EU deadline shift to December 2027 (Regulation (EU) 2026/1744), the Korean AI Basic Act, the Vietnamese AI law and the US state statutes are all carried from secondary commentary — much of it vendor blogs. **Any date that will appear in a contract must be confirmed against the primary instrument.** This is the oldest open item on this page and it is not closing by search alone.
- 🔴 **`huggingface.co` and `openedx.org` do not resolve under this session's network policy**, so the OmniEdu and `wordlink` model cards and the Open edX MCP announcement were read only at second hand (the MCP packages' *grant payloads* were read directly from `raw.githubusercontent.com` and are first-hand).
- 🟡 **The four mandated regional legs returned real material at p655, for the first time in three passes** — US state bill counts, the EU deadline split, the Ipsos APAC ban-support range and Korea's teacher-training spend, the LATAM 90%-use/26%-strategy split and the UNESCO Observatory's partner list. **The one leg that returned nothing is LATAM open source code**, and that is now a measured finding rather than a gap: see `intel/market.md`, LATAM.

- ~~**No verified star counts for `richie`, `chamilo-lms` or `sakai`**~~ — 🟢 **closed at p652**: 318, 1.0k and 1.2k respectively, measured from the repository pages on 2026-11-04 after three passes flagged it. `edx-platform` (8.2k), `moodle` (7.6k), `XBlock` (471) and `kolibri` (1.2k) were re-measured in the same batch and **all four reproduce**.
- **No first-hand reading of any primary regulatory text.** The EU Digital Omnibus, the Korean AI Basic Act and the Vietnamese AI law are all carried from legal-practice and secondary summaries. They agree with one another, which is why confidence is high on the dates — but no Commission, MSIT or Vietnamese National Assembly document was fetched. Verify before quoting a clause to a client.
- ~~**No country-level education AI regulation for any Sub-Saharan African state**~~ — 🟢 **resolved at p652 into an accurate statement rather than an absence**: national AI *strategies* with explicit education commitments exist (Kenya's National AI Strategy 2025–2030 commits to AI literacy across primary, secondary and higher-education curricula; Nigeria's digital economy strategy references AI), and education-sector *rules* still do not. South Africa's draft National AI Policy was published 10 April 2026 and withdrawn 27 April 2026. The African Union's own roadmap puts Phase 1 (2025–2026) at strategy-building, so this is where the continent is scheduled to be. 🔴 **Still absent: any published Kenyan AI-literacy framework** implementing the strategy's commitment — a named, unfilled deliverable as of September 2026.
- **The "agentic university" framing** carried by earlier versions of this page rested on a single arXiv preprint. It is a useful taxonomy, not measured adoption, and has been demoted accordingly.
- **No evidence was found of a dominant open source assessment-integrity or proctoring tool.** Given this is the most heavily regulated use case in the sector, the absence of permissive supply is notable and is recorded as a gap rather than a finding. p652 widened the search to general rubric-scoring libraries and found **one** permissive, credible option — `microsoft/LLM-Rubric` (MIT, 45★), which is **not education-specific** — plus `protorubric`, whose payload and README name different licences. **Three passes, two search strategies, same hole** — 🟢 **and at p653 a third strategy broke half of it.** Searching the automated-essay-scoring literature instead of the agent ecosystem found two permissive education-specific systems: `wwrwbs/AI_AWE` / ArguLens (Apache-2.0, scorer + feedback, arXiv:2608.17356, **2★ / 2 commits**) and `littlecookie0722/AI-Teaching-Agent` (MIT, exam generation + `WAITING_REVIEW` approval gate + sandboxed grading, **0★ / 30 commits**, grading track frozen by its author). **So the accurate split is now: assessment *scoring* has permissive supply at research-artefact adoption; assessment *integrity* and proctoring have none at any adoption, in four passes.** The hole that remains is the regulated half — which is the one that matters under Annex III. See **T20**. 🔵 The methodological point is that the hole was partly in the *channel*: three passes searched for agents, and the supply was in the literature.
- 🔴 **One claim was tested at p652 and rejected rather than published:** that **TEQSA requires Australian higher education providers to submit institutional gen-AI action plans.** No submission mandate was found; TEQSA publishes guidance ("Assuring quality learning in a gen AI-integrated future", 24 June 2026), maintains a Gen AI Knowledge Hub, and leans on Threshold Standard 5.2. This is the second consecutive pass whose mandated regional leg produced a valuable *negative* result — the first was the North Carolina SL 2026-41 dates at p651. **The regional leg's job is partly adversarial, and that is now a pattern rather than an anomaly.**
- 🔴 **A seven-pass blind spot in this base's own instrument, found at p653.** `OpenOLAT/OpenOLAT` — Apache-2.0, 449★, **32,210 commits**, the institutional LMS of much of German-speaking European higher education — was missed by every prior pass because the platform shelf was always ranked by stars, and its star:commit ratio is **1:72**. This page had already recorded the reason (Moodle's forks exceed its stars; institutional software is taken, not watched) and did not apply it to its own ranking. **The correction is a channel change, not a row: for platforms, rank by licence or commit depth.** Counted honestly, this is the third consecutive pass in which the most consequential finding was a defect in this knowledge base rather than a change in the world.
- 🔴 **Still no first-hand reading of the three AI-education statutes, unchanged at p653**, and `huggingface.co` still does not resolve, so OmniEdu's weight licence remains unread for a second pass. Both are cheap to lift and neither was lifted.
- 🟡 **The four mandated regional legs returned almost nothing new at p653, and that is the honest result rather than a gap.** North America, EMEA, APAC and LATAM were each searched; the great majority of what came back — the EU Digital Omnibus deferral to 2 December 2027, Korea's AI Basic Act, Vietnam's education transition date, the UNESCO IESALC 87%/26% denominators, the Universidad de los Andes count of 716 instruments — **this base already held and already sourced.** Four genuinely new readings are recorded in `intel/market.md` under p653. Reproduction is not waste: it is the only evidence that the regional picture is stable rather than stale.
- 🔴 **Five hosts did not resolve in this session at p652** — `www.oecd.org`, `www.unesco.org`, `www.iesalc.unesco.org`, `www.dlapiper.com`, `huggingface.co` — so the OECD recommendations, the Canadian strategy detail and OmniEdu's weight licence rest on secondary sources or are unresolved. The IESALC LATAM figures were independently re-derived from search and reproduce. This is a network-policy ceiling on verification, not a research gap, and it is cheap to lift.
- 🔴 **A sixth host joins that list at p669 — and p669 establishes *why* the class exists, not merely that it does.** `www.europarl.europa.eu` was registered at p668 as a novelty this base could not verify, with the instruction to retry the fetch. p669 retried it on a **different channel** — `WebFetch` rather than `curl` — and got **`getaddrinfo ENOTFOUND`**. 🔵 **Two independent channels failing at *name resolution* is not a transport failure, a proxy refusal or a rate limit: it is the session's network policy.** Every host on this list is therefore in the same class, and **none of them is a retry target.** Stated so no later pass spends budget on it: **these hosts have to be allowed in the session's network settings — re-fetching them cannot succeed.** The documents behind them stay filable at the **secondary** class, which is how the EPRS briefing is filed on `intel/market.md` and in the list above, and they must never be re-quoted as primary reads.

## T36 — The substrate under every school coding tool changed hands, and almost nobody re-pointed at it 🟢 new at p658

**Blockly — the drag-and-drop block library underneath Scratch Blocks, Microsoft MakeCode, Code.org, ardublockly and openblock — moved from Google to the Raspberry Pi Foundation on 10 November 2025.** Google announced it on its Open Source blog in late October 2025; the Foundation published its own notice on 28 October 2025; the library stays Apache-2.0, and Google funded the handover with a grant.

Verified at first hand rather than taken from the announcement: `git ls-remote` returns **the same HEAD SHA** (`a4dbe9f`) for `google/blockly` and `RaspberryPiFoundation/blockly`, and the same again (`8c1a305`) for the `blockly-samples` pair. Identical SHAs on both pairs means these are **redirects of one repository**, not forks — the canonical address is now `RaspberryPiFoundation/*`.

Three consequences, in descending order of how much they cost:

1. 🔴 **A star-ranked census structurally cannot see Blockly.** `blockly in:name stars:>3000` returns `RaspberryPiFoundation/blockly` at **13,600 ★** and does **not** return `google/blockly` at all, because the stars travelled with the transfer and the old address is only a redirect. This base held **zero** Blockly rows before p658 while running star-floor sweeps for hundreds of passes. That is p647-C's finding — *the sort key is the filter* — arriving through a second mechanism: **a transfer silently removes an address from every ranked query that names the old owner.**
2. **The governance fact is procurement-grade.** The library under the world's school coding tools is now stewarded by an **education charity in the UK (EMEA)** rather than a US advertising company. For a public-sector or ministry engagement that is an argument, not trivia.
3. ⚠️ **The ecosystem has not re-pointed.** `TutoriaLLM`, shelved this pass and pushed 2026-11-03, still badges `github.com/google/blockly` in its README. Expect client codebases, docs and SBOMs to name the old owner for years; treat `google/blockly` as an **alias**, not a different project.

**Confidence: high** — transfer verified by SHA identity on two independent repository pairs, date corroborated by Google's and the Foundation's own announcements.

## T37 — The largest blind spot this base has ever had was not a hard layer, it was an unswept one: learn-to-code 🟢 new at p658

Before p658 the shelves held 27 agents and 52 foundations covering tutoring, autograding, psychometrics, spoken assessment, credentialing, LMS and SIS — and **not one row** for block-based programming, physical computing or CS-education delivery. The words `makecode`, `pxt` and `micro:bit` appeared **nowhere** in the repository, not even in `archive/`; `blockly` appeared only inside archived prose describing another project's feature list.

That is the category with the **widest installed base in K-12 worldwide** — Scratch, MakeCode, micro:bit and Code.org are what "computing" means in most school systems. Eighteen foundation rows and five platform rows now cover it.

🔵 **Why it stayed invisible is the transferable lesson, and it is not "nobody looked".** Three mechanisms compounded:
- **T36's redirect** removed Blockly from every star-ranked query naming Google.
- **Topic homonymy**, p646-H's finding, at four new heads at once: `topic:oer` is dominated by ASN.1 **O**ctet **E**ncoding **R**ules (`eerimoq/asn1tools`, 338 ★) and a RISC-V core; `topic:scratch` by "from scratch" tutorials (`geektutu/7days-golang`, **17,036 ★**); `topic:captioning` by image-captioning ML; `topic:wcag` by colour-contrast libraries. A star-ranked read of these four heads publishes a Go tutorial, a CAPTCHA widget and a Swift colour library as education's leading assets.
- **Vintage**: this layer predates the `main` default. **15 of the 21 addresses verified this pass (71%) sit off `main`** — `develop` ×3, `master` ×11, `staging` ×1 — against p645-B's 34.0% population baseline. p646-J said branch name tracks project vintage; here it tracks it at **double** the base rate, because this is the oldest layer in the KB.

**Confidence: high** (the absence was measured by grep over the whole repository including `archive/`; the 21 addresses were verified individually).

## T38 — The index's licence field is unsafe in the permissive direction, and this pass has the worst specimen yet 🟢 new at p658

p657 established that `NOASSERTION` is not a licence finding. p658 establishes the sharper and more dangerous half: **a licence field that names a permissive family can also be wrong.**

🔴 **`TurboWarp/extensions` (194 ★, pushed 2026-11-05) is reported by `gh api search/repositories` as plain `MIT`.** It has **no root grant file at all** — seven filenames probed, all 404. Its `package.json` declares:

```
"license": "MIT AND LGPL-3.0-only AND GPL-3.0-only AND CC-BY-SA-4.0 AND CC-BY-4.0
            AND CC-BY-2.5 AND CC0-1.0 AND Apache-2.0 AND MPL-2.0 AND BSD-3-Clause AND ISC"
```

Eleven families joined by **AND**, two of them GPL. A studio that trusted the index's "MIT" would ship GPL-3.0 code inside a proprietary deliverable. **This is the first address this base has found where the index's error runs toward permissive**; every prior case (`NOASSERTION`, p646's `ltijs`) erred toward restrictive, which is the safe direction to be wrong in.

The pass's other two index disagreements both resolved the *other* way, which is why the asymmetry matters: `microsoft/pxt-microbit` (`NOASSERTION` → **MIT**, canonical body behind a two-line bespoke header) and `code-dot-org/code-dot-org` (`NOASSERTION` → **Apache-2.0 + carve-out**). **Rule: the index's licence field is a hint in both directions and evidence in neither.**

**Confidence: high** (all three read byte-for-byte on the resolved default branch).

## T39 — The sector's standard licence shape is permissive code wrapped around unlicensed courseware 🟢 new at p658 🔧 **`p671`: duplicate identifier — `p661` reused `T39`. This is the `p658` `T39`.**

`code-dot-org/code-dot-org` states it in one payload: Apache-2.0 for "all source codes and assets", **except** Code.org's artwork, graphics, sounds, lectures, videos, logos, characters and fonts, enumerated in a 4,271 B / 77-line `NOTICE`, which "may not be used or distributed or accessed in any manner other than directly via Code.org's own web site, mobile applications, or social media channels … **without modification or embedding in another format**". The Minecraft assets inside it are **Microsoft's**, and any distribution outside Code.org's own site needs a separate agreement with Microsoft.

This is the same shape p657 found at the OER layer and p656 at the platform layer, and it is the shape that decides education engagements: **the engine is free, the lesson content is not.** A proposal that says "we will build on Code.org" and means "we will ship their courses" is a licence incident waiting to be discovered by the client's counsel.

**Confidence: high** (licence and `NOTICE` both read in full).

## T40 — Scratch is two licences, and which one you touch decides the business model 🟢 new at p658 🔧 **`p671`: duplicate identifier — `p661` reused `T40`. This is the `p658` `T40`.**

Not one project: `scratch-gui` (4,807 ★) and `scratch-vm` (1,306 ★) are **AGPL-3.0**; `scratch-blocks` (2,769 ★, pushed 2026-11-05) is **Apache-2.0**. Hosting a modified Scratch editor as a service triggers network copyleft on the hosted work; building on the blocks library does not.

Two permissive escape routes exist and both were verified this pass: build the editor on **`scratch-blocks`**, and execute projects with **MIT-licensed `forkphorus`** (150 ★) instead of the AGPL `scratch-vm`. `goboscript` (MIT, 577 ★) compiles text to `.sb3`, and `leopard` (MIT, 168 ★) converts Scratch projects to readable JavaScript — the block→text migration path a curriculum needs after year two.

🔴 **A payload finding sits underneath this trend.** `scratch-blocks` and `ardublockly` ship **byte-identical** Apache-2.0 payloads (`md5 f15febb3…`, 10,174 B) that are **not canonical**: the header is misdated **"Version 2.0, January 2011"** (canonical: January 2004) and the entire APPENDIX is truncated. Operative terms, lines 1–177, are byte-identical to canonical, so **the grant is Apache-2.0** — but a byte-equality or template-identity test keyed on 11,357 B scores both `UNKNOWN-TEMPLATE`. Two independent downstream Blockly derivatives carrying the same corrupted text is a **copy lineage**, and it is bounded: `openblock-desktop`, `aily-blockly` and `pxt` all differ.

**Confidence: high** (diffed line by line against a canonical payload read the same hour).

## T41 — The runtime is the distribution channel: education tools now ship as a plugin per agent host 🟢 new at p659

For most of this base's history an education AI tool was *an application* — something an institution deployed, or a learner opened in a browser. p659 measures how far that has moved, and the number is on this KB's own shelf: **9 of the 29 rows on `agents/top.md` are not applications at all, they are surfaces into an agent runtime** — seven MCP servers (`canvas-mcp` × 2 independent projects, `moodle-mcp`, `tutor-mcp`, `anki-mcp-server`, `brightspace-mcp-server`, `brightspace-d2l-mcp`), one agent *skill* (`universal-examprep-skill`) and one runtime *plugin* (`PAIDEIA`). **Just under a third of the permissive education shelf is plumbing for somebody else's agent.**

🔵 **The clearest single specimen is `OPTIMETA/PAIDEIA`, and it is why this trend gets its own number rather than a line under T27.** One author shipped the same study engine as **five separate repositories**, one per agent host — Claude Code, OpenAI Codex CLI, `sst/opencode`, `NousResearch/hermes-agent`, and a standalone local MCP server — all MIT, all created between **21 April and 14 June 2026**, all still pushed through **September 2026**. Not a port forced by a client; a *distribution decision*. The engine is identical; what varies is the host it plugs into.

🔴 **Why this is a commercial fact and not a packaging detail.** It inverts where the integration cost sits. An application has to be deployed, hosted, secured and signed off by an institution before a learner touches it — months, in public education. A plugin inherits its host's installed base, its auth, its file access and its model access, and reaches a learner the day it is published. **That is also the catch:** it reaches the learner *and nobody else*. A tool distributed this way has no institutional telemetry, no roster, no grade book and no audit trail — which is precisely what the EU AI Act's Article 50 and every Annex III obligation ask a deployer to produce (**T15**, **T35**). 🔵 **So the two halves of this sector are now diverging on who the customer is:** runtime plugins are consumer distribution to individual learners, and the institutional sale still needs the evidence spine of **P17**. A client proposing to “ship a plugin” for an accredited programme is proposing something that cannot be evidenced.

🟡 **Read the star counts honestly before building a thesis on them.** The four `PAIDEIA` ports carry `26`, `3`, `2` and `1` star against the canonical's `92`. This trend is evidenced by **what builders are choosing to ship**, not by adoption — there is no adoption here to measure. The canonical's `#1` placing on GeekNews and a Product Hunt launch are reach signals for the *project*, not for the ports.

🔵 **The port worth watching is the MCP one**, for the same reason `anki-mcp-server` mattered at p655 and `tutor-mcp` before it: an MCP server is the one shape on this list that is **not** tied to a single vendor's runtime, so it is the only one an institution can point at a local model it controls. If this trend resolves anywhere durable, it resolves there — see **P24**.

## T42 — `NOASSERTION` has a second mechanism, and it is the one with a commercial consequence 🟢 new at p660

p659 named a mechanism for `NOASSERTION`: on a controlled five-repo set, appending text to an otherwise byte-stock MIT grant flips GitHub's classifier off a correct verdict. That mechanism is real, and it is **benign** — the stated licence still governs the whole repository, so reading the payload recovers the right answer and nothing about the engagement changes.

p660 found a **second, distinct mechanism with the opposite consequence.** Both `NOASSERTION` repositories measured this pass carry a payload that is **not a grant at all**. It is a *licence-split manifest*: a short file naming two or three different licences for different directories.

| Repository | Classifier | Payload, byte-read at p660 | What the file actually says |
|---|---|---|---|
| [`scratchfoundation/Scratch_1.4`](https://github.com/scratchfoundation/Scratch_1.4) | `NOASSERTION` | `LICENSE`, `1,008 B` | **Three licences in one repo.** Code **GPL-2.0**; `/src/plugins` **MIT**; `/Help`, `/Media`, `/Projects` **CC BY-SA 3.0**. Plus a term rarely seen in this KB: modified versions must be *designated as modified in the `Help > About` dialog at runtime* — an attribution obligation in the **UI**, not just the source. |
| [`RaspberryPiFoundation/scratch-curriculum`](https://github.com/RaspberryPiFoundation/scratch-curriculum) | `NOASSERTION` | `LICENSE.md`, `551 B` | **CC BY-NC-SA 4.0** — Attribution–**NonCommercial**–ShareAlike, plus Code Club terms and conditions by reference. |

**Why the distinction matters more than it sounds.** Under p659's mechanism, a payload read *resolves* `NOASSERTION` into a usable licence. Under p660's, a payload read resolves it into **a question you still have to answer**: which licence governs the part you intend to ship. A pipeline that files one SPDX value per address — as this base's own ledger schema does — cannot represent either row honestly, and `Scratch_1.4` is filed in `evidence/address-ledger.tsv` as `licence-split:GPL-2.0+MIT+CC-BY-SA-3.0` for exactly that reason.

### 🔴 And the curriculum-licence finding gets worse, not just confirmed

This base has been accumulating a hypothesis: permissively-licensed education **software** is common, permissively-licensed education **content** is not. The evidence was two assets, both ShareAlike — [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) (949★, CC BY-SA 4.0, declined at p651) and a French K-12 curriculum pack (CC BY-SA 4.0, declined at p658).

`scratch-curriculum` (212★, **357 forks** — more forks than stars, the signature of material institutions take copies of) is the third, and it is **stricter than both**: CC BY-**NC**-SA 4.0. ShareAlike bars a *closed* derivative. NonCommercial bars **commercial use at all** — a Globant engagement cannot ship it, cannot bundle it, and cannot charge for a service built on it, regardless of whether the derivative is open.

**3 of 3 curriculum assets this base has measured are non-commercialisable, and the newest is the hardest.** The single counter-case remains [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) (MIT, `1,066 B`, re-read at p660), which is precisely why `compose/patterns.md` **P10** is built on that one and not on a school curriculum. **Confidence: high** on the licences (three payloads byte-read); **medium** on the generalisation — three assets is a pattern, not a census, and this base says so rather than rounding it up.

🔵 **The practical rule this yields.** In an education engagement, price the *content* licence separately from the *code* licence and read it first. The code is usually MIT or Apache; the curriculum is usually the thing that cannot be sold, and it is usually the thing the client actually wanted.

🟢 **Extended at p662 with a controlled specimen that isolates the filename axis.** `anchore/syft` serves canonical Apache-2.0 at `LICENSE` (`11,357 B`, `sha256₁₂ c71d239df917`) and classifies **`Apache-2.0`**. `aboutcode-org/scancode-toolkit` serves **the same bytes and the same digest** at `apache-2.0.LICENSE` on `develop`, and classifies **`NOASSERTION`**. Payload held constant, filename varied, verdict flipped — which is the cleanest demonstration this base holds that a `NOASSERTION` carries no information about the grant. 🟢 **And the complementary control:** `CycloneDX/cyclonedx-cli` *filled in* the Apache `APPENDIX` boilerplate (`Copyright OWASP Foundation`, brackets `{}`, `11,341 B`, `sha256₁₂ 6c29f22a4a73`) and still classifies `Apache-2.0`. **Completing the appendix is safe; removing it and appending text — OpenOLAT's shape — is what flips the classifier.** All four readings taken first-hand on `2026-11-05`. Wired as `compose/patterns.md` **P27**.

## T39 — This base's absence claims are checked against its shelves and refuted in its logs, and that is now its dominant defect class 🟢 new at p661 🔧 **`p671`: duplicate identifier — `T39` was already taken by `p658`'s courseware-licence trend. This is the `p661` `T39`.**

Four of the last six passes found the same thing, on four different layers: **the finding was already held and had never reached a shelf.** p656 — the interop, telemetry and accessibility layer, measured in the logs for many passes, never promoted. p659 — `PAIDEIA` measured since p540 and never filed; `ollama/ollama` cited on five shelves while its ledger verdict read `unstated`. p660 — `35` of `159` shelf addresses missing from the base's own index, `22.0%` invisible. p661 — the accessibility layer again, plus a proctoring absence claim its own log had refuted `451` passes earlier.

🔵 **p661 names the mechanism, and it is a scope bug in one instrument rather than carelessness in many passes.** `evidence/absence-claim-census.2026-10-31-p569.tsv` exists precisely to catch an absence claim the base's own holdings contradict, and it works — it flagged `27` gateable claims and closed a 145-pass-old gap. Its scope:

```
broad   pages_scanned         11      live pages only, archive excluded
broad   shelf_rows_indexed    10892   lines carrying a github.com address
narrow  supply_claims         569     absence sentence naming a buildable-on noun
narrow  full_token_collision  27      the gateable set
```

A claim is flagged only when its content tokens collide with a **shelf row**. The two append-only logs are a further **`124,015` lines** carrying exactly such addresses (`agents/trending.md` `69,591`, `repos/trending.md` `54,424`) and collisions there are **not scored at all**. So the census can catch *"X does not exist"* when X is on a shelf, and is structurally blind to it when X is in a log — which is where this base puts everything it measures before deciding whether to promote it. **The blind spot is exactly the backlog.**

🔴 **And the ledger makes the diagnosis worse, not better.** `evidence/address-ledger.tsv` is a dated, machine-readable index of `3,228` addresses, and it **held the refuted material with the correct licence the whole time**: [`openai/whisper`](https://github.com/openai/whisper) has been in it since **`p6`** with verdict `MIT` and `filed_on = "-"` — `655` passes indexed, correctly licensed, never shelved — and `GoogleChrome/lighthouse` since **`p19`** with verdict `Apache-2.0`, likewise. So this is not a case of the base not knowing. **It knew, in a machine-readable file, and no instrument compares that file against the sentences the pages assert.** 🔵 **`filed_on = "-"` is a ready-made promotion backlog and the least-used column in this base** — one `awk` filter produces it. 🔧 p661 also repaired two verdicts that were wrong in the **restrictive** direction (`lebmatter/exampro` and `vardanagarwal/Proctoring-AI`, both carried `unstated` while serving clean MIT payloads). **T38** warned that the licence field is unsafe in the permissive direction; the restrictive direction is quieter and costs more, because an `unstated` verdict on an MIT repository silently removes a usable asset and nobody ever finds out.

🔴 **Why this matters outside this repository.** Every absence claim on these pages is load-bearing for an engagement: *"there is no permissive proctoring software"* becomes a line item to build, and *"accessibility has no permissive answer"* becomes a services-only proposal with no product. Two such claims were wrong this pass, and both would have changed a proposal's shape and price. **An append-only log is an asset only if something reads it back.** Registered as `Gap 661-C`; the fix is to index the logs as a refutation corpus distinct from the shelf corpus, and it was not performed because `make hooks` and `ingest/` have been denied for eleven consecutive passes. **Confidence: high** — the mechanism is read directly off the instrument's own recorded scope, and both p661 cases fit it exactly.

## T40 — Every "no permissive supply" claim this base has tested has turned out to be an adoption gap instead, and that is now five for five 🟢 new at p661 🔧 **`p671`: duplicate identifier — `T40` was already taken by `p658`'s Scratch trend. This is the `p661` `T40`.**

The pattern is complete enough to state as a rule. Each of these was published as a supply absence and each, when the right query was finally run, turned out to be shallow-but-real supply:

| Layer | Published as | Turned out to be | Pass |
|---|---|---|---|
| Moodle agent bridges | *"no permissive Moodle-side agent"* | **7 MIT servers**, whole field ≤ `27★` | p652 |
| Permissive institutional LMS | *"no permissive platform of the Moodle class"* | **`OpenOLAT`**, Apache-2.0, `32,210` commits | p653 |
| Assessment scoring | *"no permissive assessment agent"* | **2 education-specific**, both research artefacts | p653 |
| Learn-to-code | not even searched for `657` passes | **18 foundation rows**, incl. BSD-3 ScratchJr | p658 / p660 |
| Proctoring and integrity | *"genuinely unsupplied under a permissive licence"* | **6 permissive addresses**, held since `p202` | p661 |

🔵 **The mechanism is the same every time and it is a vocabulary problem, not a search-effort problem.** Each absence was measured with a `topic:` head or a star-ranked query, and each was broken by a different channel: licence-first for OpenOlat, the academic literature for assessment, org enumeration for ScratchJr, and at p661 **`license:mit` sorted by stars** for proctoring — none of those six proctoring repositories is tagged `proctoring` in a way the topic sweeps reached. p658 wrote the prescription — *"a future pass should query by capability, not by tag"* — and p661 is the pass that applied it to a different gap and was paid out twice.

🔴 **The operating rule for a proposal.** When these pages say a layer has no permissive supply, read it as **"no permissive supply this base has found with the queries it has run"** — and expect the true answer to be *shallow, fragmented, unadopted supply* rather than emptiness. That distinction changes the engagement from *build* to *adopt-and-harden*, which is a different scope, a different price and a different risk profile. 🟢 **The two absences that have survived every re-probe are worth naming for contrast**, because they are the ones that look real: **in-place WCAG repair inside an LMS** (UDOIT, GPL-3.0, re-verified p661) and **any OpenOlat agent bridge at all** (`0 of 5` addresses resolve, re-probed p661, fourth consecutive confirmation). **Confidence: high** on the five cases, each of which is a measured reversal recorded on these pages with first-hand licence reads.

## T43 — A knowledge base's index can assert filings its own pages no longer carry, and the cause is the rewrite, not the research 🟢 new at p662

T39 named this base's dominant defect class as *claims checked against shelves and refuted in logs*. p662 found the adjacent one, and it is larger. `evidence/address-ledger.tsv` is the index that answers *"do we already own this?"*; its `filed_on` column made **`259`** claims and **`29`** were exactly right. **`142`** named a page that does not carry the address at all, and **`100`** of those name an address the live tree carries nowhere. In the other direction, **`59`** addresses sitting on a curated page carried `filed_on = "-"`.

🔴 **The cause is a step missing from a procedure the base performs deliberately.** Traced against `archive/`, **`85`** of the `142` were last carried by the `p568` pre-rewrite snapshot and **`52`** by `p650`'s. Both passes rewrote all six curated pages and both archived the previous version first — the discipline was there. Neither reconciled the index against the page that replaced it, and no pass ever has. `85` claims stood false for `94` passes.

🔧 **And the headline metric could not have caught it, because it was right by cancellation.** `ingest/promotion-ratchet.json` reported `filed: 258`. The true count of distinct index addresses present in the curated tree is **`176`** — and `259 − 142 + 59 = 176` exactly. An over-count and an under-count of opposite sign and near-equal size produced a number one away from the truth while `230` of its `259` constituents were inaccurate.

🔵 **Why this generalises past this base.** Any curated knowledge store that (a) rewrites whole pages and (b) keeps a separate index of what it holds will drift the same way, and the drift is invisible precisely because the index is what you would check. The control is cheap — re-derive the index from the tree and diff — and it belongs **in front of** a rewrite, not after one. Confidence: 🟢 **high**, measured twice with a re-implemented instrument and `6/6` hand controls; the generalisation beyond this repository is 🟡 **argued, not measured**.

🔴 **One scope question is deliberately left open.** `42` of the `142` are still reachable on `intel/open-gaps.md` or `intel/measured-unusable.md` — reader-facing pages outside the index's `CURATED` list. Either those pages join `CURATED`, or `filed_on` needs a third state for *demoted, still readable*. p662 did not decide it, because deciding it silently is how the column became wrong.

## T44 — The sixth "no permissive supply" claim fell too, but to a different mechanism: the supply was there and the base was searching in the wrong language 🟢 new at p663

**T40** records that every *"no permissive supply"* claim this base has tested turned out to be an **adoption** gap instead — five for five. p663 makes it **six for six and changes the mechanism**, which is why this is a separate entry rather than another tally mark on T40.

The claim under test was this base's longest-standing structural gap: **`agents/top.md` carried *"EMEA and LATAM have zero placed agent rows between them"***, and had carried some version of it for dozens of passes.

🟢 **It is now closed for LATAM, with two rows** — [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Universidad Tecnológica de Pereira, Open edX XBlock) and [`AndresGuido9820/trabajo2-agente-tutor`](https://github.com/AndresGuido9820/trabajo2-agente-tutor) (MIT, Universidad Nacional de Colombia, 151 commits / 314 tests). Both placed on a **named institution in the repository's own text**; the placement rule was not relaxed to get there.

🔵 **The mechanism is new, and it is the transferable part.** The first five instances were all *adoption* gaps: the software existed, was findable in English, and was simply shallow or unadopted. This one was an **instrument** gap:

| Leg | In-scope addresses returned | Novel |
|---|---|---|
| 4 × mandated **English-language** supply legs | 🔴 **0** — sixth consecutive pass | 0 |
| `…educación IA agente tutor español México Chile Colombia licencia MIT 2026` | 4 | 🟢 1 |
| `…tutor agent Brazil Mexico Argentina universidad github MIT licença educação` | 7 | 🟢 1 (an AGPL refutation) |

**Both** novel addresses in the pass came from non-English legs, and **both** were LATAM. The English legs have returned nothing in scope since p658.

🔴 **Why this is a trend and not a one-off.** The three forces behind it are structural, not accidental. (1) **Education software is written in the language of its curriculum** — a tutor for Colombian rural higher education is described in Spanish, names a Colombian university, and uses the word *tutor* in a Spanish sentence that an English-keyword query does not match. (2) **This base's own placement rule compounds it**: author names and README language are correctly excluded as placement channels, so a project that *is* placeable only shows up as placed if a query reaches it at all. (3) **Star-ordered discovery buries it further** — both rows are `0★`, and this base has already measured that stars mis-rank education software by up to **1:72** on star:commit (`OpenOlat`).

🟡 **The honest limit, stated with the claim.** Closing the LATAM zero did **not** produce an adoptable production base: both rows are `0★` university coursework. So T40's underlying shape survives intact — supply exists, and it is shallow and fragmented. What changed is that this base can no longer attribute a regional supply gap to the *region* without first running the legs in the region's own languages.

🔴 **EMEA is still zero, and it is now the sharper anomaly** — it is where the binding statute is, and where this base's strongest *platform* rows are built (OpenOlat, ILIAS, Artemis), yet it has no placed **agent** row. T44 predicts the fix and the next pass should test it: **run the supply legs in German, French, Spanish and Portuguese before concluding anything about EMEA agent supply.**

⚠️ **Consequence for every absence claim on this page.** Any *"searched and not found"* on a non-anglophone region that rests only on English-language legs is **provisional**, not settled, and should be re-stated as such rather than cited as a measured gap.

🔧 **Numbering note:** this entry is **T44** because **T43** is the highest unique number on the page — `T39` and `T40` each appear **twice** (p658 and p661 both minted a pair). The duplicates are left in place rather than silently renumbered, since other pages cite them by number; flagged here so the next pass does not mint a third `T39`.

## T31 — A regional "zero" on this base's shelves has twice turned out to be a query-language artefact, and the instrument is the finding 🟢 new at p664 🔧 **`p671`: duplicate identifier — `T31` was already taken by `p657`'s psychometric-layer trend. This is the `p664` `T31`.**

Two regions carried zero placed agent rows on `agents/top.md`. Both closed inside two passes, and neither closed because the sector changed.

| Region | Closed at | Leg that closed it | What the mandated English legs returned |
|---|---|---|---|
| LATAM | p663 | **Spanish** | nothing in scope |
| EMEA | p664 | **German** — first attempt | nothing in scope, 7th consecutive pass |

The four mandated English-language supply legs have now returned **zero in-scope novel addresses for seven consecutive passes**, and the trending digests have gone **twenty** passes without a yield. In the same window, non-English legs produced `TutorIA`, `Profe Bit`, `EduRAG` and `RUCAI` — every regionally placed row added since p662.

🔵 **The generalisable claim is narrow and worth stating precisely:** English-language search surfaces the *most-starred* education repositories, which are disproportionately American and Chinese, and it does not surface *institutionally-situated* ones, which are where regional placement evidence lives. A base that searches only in English will therefore measure a world in which only APAC and the unplaced global middle build education agents — which is exactly what this base measured for its first ~660 passes.

🔴 **The counter-case that stops this becoming a rule.** **North America now has one placed row against APAC's eight** and its query language is already English. So language is a sufficient explanation for the LATAM and EMEA zeros and **not** a general theory of regional coverage. The North American thinness is unexplained and is registered as an open question in `intel/market.md`, not papered over with this trend.

**Operationally:** run the supply legs in German, French, Spanish and Portuguese as standing practice, and treat a declared regional absence as a statement about the instrument until it has been tested in the region's own language.

## T32 — In LATAM, adoption and licensability are inversely correlated, which makes licence remediation the cheapest intervention available 🔴 new at p664 🔧 **`p671`: duplicate identifier — `T32` was already taken by `p657`'s spoken-assessment trend. This is the `p664` `T32`.**

Measured at p664, the Brazilian education-agent field:

| Address | Stars | Forks | Grant |
|---|---|---|---|
| `digitalinnovationone/dio-agent` (DIO) | **2,988** | **367** | 🔴 **none at four root filenames; `spdx = null`** |
| `LabSirius/TutorIA` | 0 | 0 | 🟢 MIT |
| `AndresGuido9820/trabajo2-agente-tutor` | 0 | 0 | 🟢 MIT |
| `ThallesYVasconcelos/Agente-Educacional` | 0 | 0 | 🟢 MIT |

**The one with three orders of magnitude more adoption than the others combined cannot be built on at all**, and neither can the 367 forks already downstream of it.

🔵 This is a different problem from the one **T18** describes. T18 is about where open source *invested* — Canvas-shaped institutions, at the expense of Moodle-shaped ones. T32 is about **licence hygiene tracking adoption in the wrong direction**: the projects that earned users are the ones that never did the paperwork. **T22** established that licence form and licence hygiene are independent variables; T32 is the regional consequence, and it is severe enough to invert the standard advice. Where this base would normally say *adopt-and-harden* (**T18**, **P8**), in LATAM the first move on the most-adopted repositories is **neither adopt nor build: it is ask for a licence file.**

That is weeks of relationship work with a named publisher, it converts a dead 2,988-star base into a reusable one, and it is the highest-leverage, lowest-cost move this base has identified in the region. Scoped as **`compose/patterns.md` P29**.

⚠️ **Scope limit:** measured on Brazilian repositories in one pass. Whether it holds for Spanish-speaking LATAM, or outside LATAM, is **untested** — the Spanish leg's novel addresses at p663 and p664 were all research-scale, so there was no high-adoption case to grade.

## T45 — A declared filing is not a filed row, and the log is where the claim goes to be believed 🟢 new at p665

**T43** measured an *index* asserting filings its pages no longer carried, and traced the cause to whole-page rewrites. p665 found the sibling one level up, and it is cheaper to cause and harder to see: **the append-only log asserts filings that were never written at all.**

`repos/trending.md` at **`p588`** published a table under the heading *“SIX ROWS FILED”*, with star counts, provenance and a passes-unfiled column — the full apparatus of a completed action. Re-measured at p665 against every sell shelf (`agents/top.md`, `repos/foundations.md`, `verticals/solutions.md`, `compose/patterns.md`, `intel/trends.md`, `intel/market.md`):

| `p588` declared filed | ★ | On a shelf at p665 | `MOVED` records |
|---|--:|---|--:|
| `microsoft/generative-ai-for-beginners` | 122,693 | 🔴 no — only in `intel/open-gaps.md` | 3 |
| `rasbt/LLMs-from-scratch` | 107,625 | 🔴 no — only in `intel/open-gaps.md` | 1 |
| `jingyaogong/minimind` | 64,710 | 🔴 **no — on no page at all** | 2 |
| `karpathy/nanochat` | 59,252 | 🟢 yes (`agents/top.md`) | 3 |
| `ashishpatel26/500-AI-Agents-Projects` | 39,200 | 🔴 **no — on no page at all** | 6 |
| `apache/openmeetings` | 688 | 🔴 no | 🔴 **0** |

**Five of six, four passes later.** And the `MOVED` column separates two different failures that look identical from the index: rows that were written and later dropped by a rewrite (**T43**'s mechanism), and `apache/openmeetings`, which has **zero** drop records — it was *never written*. p588's own prose had already called it the sharpest specimen of this base's bottleneck, having found it in a file named `permissive_unshelved.txt` that nothing had read for 63 passes. **The pass that diagnosed the bottleneck then reproduced it.**

🔵 **The generalisable claim.** In any store where the narrative log is append-only and the curated pages are rewritten, **the log accumulates intentions and the pages hold state** — and because the log is the richer, more recent and more confident document, a later pass reads the intention and stops. The control is not another census: it is that *a filing is a row in a table*, verified by looking at the table in the same pass that claims it. p665 wrote six rows across three shelves and re-derived every count from the columns rather than incrementing them.

🔴 **Corollary, and it retires a signal one pass after it was introduced.** p664 promoted off the signature *“`filed_on = -` plus many distinct passes”*. Over the whole ledger `filed_on = -` covers **3,050 of 3,237 addresses (94.2 %)**, and on the 23 education-shaped candidates this pass served, **20 were demotions** (`MOVED` to the log), not omissions. p664's own true positive, `academico-sis/academico`, carries **10** `MOVED` records, so the obvious refinement — *never dropped* — would have missed it. The signal that survives is the conjunction **never dropped ∧ ≥ 5 distinct passes**, which narrows 3,050 to **10** addresses; everything else needs a *stated re-filing reason*, in-cell, of the kind `universal-diagnostic-tutor-skill` and `TorchLeet` now carry.

## T46 — The reference implementation of statutory personalised learning is a government's production repository, and it is licensed EUPL 🟢 new at p665

Four passes of EMEA legs on this base have returned regulation: the **Annex III** postponement to 2 December 2027, the UK DfE's product-safety standards, KHDA guidance. p665's EMEA fact came from a different channel — the repository channel — and it changes what an EMEA engagement can start from.

**`Opetushallitus`, the Finnish National Agency for Education, runs its learner-facing stack in public**: applications (`ataru`), the statutory **personal competence development plan** every vocational student is entitled to (`ehoks`), the machine-readable **national core curriculum and qualification requirements** (`eperusteet`), attainments (`suorituspalvelu`), learner identity, organisations and state grants. Seven repositories, all pushed `2026-11-05`, all under the **European Union Public Licence** — two at EUPL-1.2-or-later, five at EUPL-1.1-or-later, every payload read at p665.

🟢 **Two of those objects are things this base has watched agents reinvent.** Every curriculum-grounded tutor on `agents/top.md` grounds itself in a *document* — BNCC as PDF, a `Rahmenlehrplan` as PDF. `eperusteet` is that object **as a service, with a data model, maintained by the authority that issues it**. And “personalisation” in a European public tender usually means `ehoks`'s statutory object, not an adaptive-tutoring claim; here it is, implemented.

🔴 **The licence is the constraint, and it is not GPL's.** The EUPL is copyleft whose own definition of *“Distribution or Communication”* reaches making the Work available **online** — so a modified fork stood up as SaaS triggers the obligation, the way AGPL-3.0 does and GPL-3.0 does not. Its appendix brings two compensations a procurement office cares about: a **compatibility list** permitting relicensing onto GPL-2.0, AGPL-3.0, EPL, MPL-2.0, LGPL, OSL, CeCILL or LiLiQ, and **legal validity in 23 EU languages**.

🔵 **So the trend is not “ministries are going open source” — it is that the open artefacts of European public education are arriving under a licence that prices forking and rewards integration.** The commercial shape that follows is arm's-length: an MIT/Apache agent layer in its own process, calling these services over their APIs, inheriting nothing — written up as **P32**. 🔵 **And a measurement lesson worth carrying: `gh api` reports all seven as `NOASSERTION`.** Third instance of that trap in three passes (p663 on MIT, p664 on AGPL-3.0), and the first to hide a whole licence *family* — the classifier does not match a four-line EUPL reference, so a tier was missing from `verticals/solutions.md` for want of reading four lines.

## T47 — A licence identifier is not a licence: three mechanisms by which the index and the payload disagree, measured on one organisation 🟢 new at p666

🔵 **Why this is a trend and not a bug report.** This base has recorded index/payload disagreement four passes running — `663` (MIT), `664` (AGPL-3.0), `665` (EUPL) — each time as an instance of `NOASSERTION`. p666 enumerated a single owner and found **three distinct mechanisms** in one pass, two of them in the opposite direction to `NOASSERTION`. Grouping them under one name was the error.

| Mechanism | Instance at p666 | `gh api` says | The payload says | Direction |
|---|---|---|---|---|
| **1. Pointer, not grant** | `Opetushallitus/koski`, `varda`, `ludos`, `eperusteet-ylops`, `kouta-backend`, `oph-design-system` — short `"Licensed under the EUPL, Version 1.x"` references of `295`–`653 B` | 🔴 `NOASSERTION` | 🟢 EUPL-1.1 / 1.2-or-later | **under**-reports a real grant |
| **2. Appendix capture** | `Opetushallitus/compleap` — the **full** EUPL v1.2 text, **`13,957 B`** 🔧 (p674; published as `13,956 B`) | 🟢 **`EUPL-1.2` — correct** | 🟢 EUPL-1.2 | 🔴 **the *classifier* fails, not the index**: a keyword reader matches `GNU Affero General Public License` **inside the EUPL's compatibility appendix** and returns `AGPL-3.0` |
| **3. Phantom grant** | `amandasiqueirasouza1-ux/ia-para-professores` | 🔴 **`MIT`** | 🔴 **no grant file at any of five standard paths** | **over**-reports an absent grant |
| **4. Family slip** | `Ignacio-Ghub/asistente-docente-sin-conexion` | 🔴 `GPL-3.0` | 🟠 **AGPL-3.0** (`35,148 B`, full text) | wrong **family**, and the difference is network copyleft |

🔴 **Mechanism 2 is the one that will cost this base money, and it is self-inflicted.** `NOASSERTION` is *visibly* unhelpful — it asserts nothing, so a pass goes and reads the file. **An appendix-captured classifier is confidently wrong**, and it is wrong about precisely the licence family `verticals/solutions.md` has just started carrying. 🟢 **The remedy is one line of discipline: bind the verdict to the payload's opening declaration, not to any licence name occurring anywhere in it.** The EUPL declares itself on line 1 (`EUROPEAN UNION PUBLIC LICENCE v. 1.2`) and then spends a page naming the licences it is compatible with.

🔵 **And `665-H` narrows.** p665 inferred from `7/7` `NOASSERTION` that the API *hides the EUPL family*. It does not: it reported `EUPL-1.2` correctly for the one repository that ships the full text, and it was the **only** SPDX it reported in `100`. **`NOASSERTION` tracks the payload's form, not its family** — an index can classify a licence and cannot classify a pointer to one.

🟢 **The operational consequence for a client engagement.** Any licence posture built from a repository-metadata API — an SBOM tool, a procurement scan, a compliance dashboard — inherits all four mechanisms. For European public-sector education code specifically, mechanism 1 is the *common* case: **the default reading of a ministry's repository is "no licence", and the truth is usually EUPL.** Read the file.

## T48 — A national education ministry is an organisation, not a repository set, and the search leg returns its newest member 🟢 new at p666

🔵 **Twice measured, same shape.** `p660` read a search leg's account of `scratchfoundation`'s permissive options, enumerated the org instead, and found a **whole BSD-3-Clause product** (ScratchJr) in it. `p665` read a search leg's account of `Opetushallitus` and published *"seven repositories in which a national education ministry runs its production learner stack in public"*. p666 enumerated the org: **`182` repositories, `52` pushed in the last ten weeks.**

🔴 **The systematic bias, and it is not random.** The member the search leg missed is not an obscure one — [`koski`](https://github.com/Opetushallitus/koski) at **`23★` and 12 forks** is the **most-adopted education-domain repository in the organisation**, and it is the *incumbent* system in the very domain whose `0★` newcomer (`suorituspalvelu`) p665 did file and described as *"the credential-records end"* of the family. 🔵 **Freshness-ranked discovery surfaces what was created or pushed most recently and most visibly; a public body's crown jewels are old, boring, and named in Finnish.**

🟢 **What the enumeration added that no amount of searching would have.** The early-childhood register (`varda`) — a tier `p660` went looking for and reported as unsupplied. The **local**-curriculum authoring tool (`eperusteet-ylops`) — without which p665's national-curriculum row is half a story, because deployments ground against local curricula. The matriculation-exam content service (`ludos`) — against a standing assessment gap. **None of the three was returned by any search leg in this base's history; all three are production services pushed this week.**

🔵 **So the channel rule, stated for the next pass:** when a row's owner is an institution rather than a person — a ministry, an agency, a university, a foundation — **enumerate the owner before writing the row, and write the org's size into the cell.** A family size that is really a page size is a claim this base has now published twice.


## T49 — Retention is a layer, not an algorithm: the sector's one "proven" primitive sits on a dense permissive field with a choice of objective function 🟢 new at p667

🔵 **What T13 said, and why it was true and incomplete.** **T13** has recorded for many passes that spaced repetition — specifically FSRS, via `fsrs4anki` and `fsrs-rs` — is *"the one permissive education algorithm that is already in production"*. Every word of that holds. What it also did was end the conversation: a client asking how generated material is made to stick got a single answer and no trade-off, and this base carried retention as **one point** rather than a layer.

🟢 **p667 mapped the field underneath it, and it is dense.** Sixteen rows filed to `repos/foundations.md` in one pass, all permissive, all with the grant payload read at first hand:

- **A published alternative scheduler.** [`maimemo/SSP-MMC`](https://github.com/maimemo/SSP-MMC) (MIT, `227★`) solves for the **stochastic shortest path** to a target recall — it minimises *total review cost to mastery*, trained on MaiMemo's own large-scale learner data. FSRS optimises predicted recall; SSP-MMC optimises cost. **These are different objective functions and both are permissive and published.**
- **The peer-reviewed optimum the heuristics approximate.** [`Human-Centric-Machine-Learning/memorize`](https://github.com/Human-Centric-Machine-Learning/memorize) (MIT, `190★`) is the code **and the real data** for *Enhancing Human Learning via Spaced Repetition Optimization*, **PNAS 2019**.
- **Clients in every delivery form.** `olmps/memo` (BSD-3, **`1,870★`**, Flutter → iOS/Android/desktop), `shaankhosla/repeater` (Apache-2.0, terminal), `lakesare/memcode` (MIT, web, ten years of history), and three Obsidian-native systems — `ctrlaltwill/LearnKit`, `kitschpatrol/yanki-obsidian`, `bjsi/incremental-writing`.
- **The write primitive.** [`repeat-space/anki-apkg-export`](https://github.com/repeat-space/anki-apkg-export) (MIT, `182★`) produces a `.apkg` deck **file** with no Anki installed, completing the pair with `anki-mcp-server`, which drives a *running* instance.
- **A different primitive entirely.** `bjsi/incremental-writing` and `campfirium/foliole` schedule **engagement with long material** in prioritised queues rather than retrieval of atoms — a job no flashcard scheduler does.
- **And content.** `nastaso/cloudcertprep` (MIT, `246★`) is a **1,469-question** permissive item bank for AWS CLF-C02 and AIF-C01.

🔴 **The trend is not "there is more of it".** It is that **retention stopped being a library choice and became an architecture choice**, with four decisions a studio now has to make explicitly: the objective function (recall vs cost-to-mastery vs the PNAS optimum), the primitive (atom retrieval vs incremental reading), the delivery form (mobile, web, terminal, vault-native, or a deck file handed over), and whether the item bank is generated or adopted.

🟢 **Why three of these rows matter beyond retention.** `yanki-obsidian`, `LearnKit` and `incremental-writing` keep the cards as **plain Markdown in a repository**. That makes generated learning material reviewable in a pull request and version-controlled — which is the provenance and governance answer that **T3** identifies as the buying trigger and that regulated buyers in EMEA, and increasingly North America, ask for by name. The retention layer turns out to be where the auditability argument is cheapest to satisfy.

🔵 **Read the staleness, not just the stars.** Four of the sixteen have not been pushed in over a year and two (`incremental-writing`, `memorize`) are effectively finished work; `microsoftarchive/Learn-LTI` is formally `archived`. Each row on `repos/foundations.md` states its push date and says whether it is a dependency, a codebase to adopt, or a design reference. In this layer specifically, "finished" is often the correct state for an algorithm implementation and a disqualifying one for a client application — and the rows distinguish the two.

## T50 — The student-information layer is where open source education software stops being permissive and stops being adopted at the same time 🟢 new at p668

🔵 **This base has measured the tutor layer, the delivery layer, the retention layer, the assessment layer, the credential layer and the interoperability layer. The *record-keeping* layer — the system of record that actually runs a school — turns out to behave unlike all of them, and p668 has the numbers.**

**The layer is small.** GitHub's own topic counts, read at `2026-11-05`: `lms` → **`2,646`** tagged repositories, `ai-tutor` → **`880`**, `student-information-system` → **`193`**, `intelligent-tutoring-system` → **`45`**. The SIS layer is an order of magnitude thinner than course delivery, and it is thinner than *AI tutoring*, a category that did not exist four years ago.

**Its head is copyleft, with exactly one permissive member.** The three most-adopted members, all already on this base's shelves:

| Repo | Stars | Licence | Note |
|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `652` | **GPL-2.0** | The topic's `#1`. School management, PHP. Default ref **`mobile`** |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | `411` | 🟢 **MIT** | **The only permissive member of the head.** Laravel + Filament |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | `349` | **GPL-2.0** | Multi-institution, PHP |

**And its tail is both unadopted and unlicensable.** `11` of the topic's top `20` were addresses this base had never recorded — but **every one sits at `≤20★`**, and the three most plausible, byte-read at their real default refs, are `AGPL-3.0` (`MeetPlan/MeetPlanFrontend`, `34,523 B`), `GPL-3.0` (`ClassyCreations/ScheduleCheck`, `35,069 B`) and **no grant at all** (`LindungiLw/student_information_portal`, `404` on four payload names).

🔴 **Why this is a trend and not a gap.** Every prior "no permissive supply" claim this base tested turned out to be an **adoption** gap — `T40` says so, and it has held six times. The SIS layer is the first one where **both** variables fail together: the permissive supply is a single 411-star repository, and the copyleft supply is where all the adoption is. That is a different market, and it has a different consequence.

🟢 **The consequence for an engagement.** On every other layer this base tracks, the move is to take a permissive component and build on it. Here there is **no permissive system of record to build on at any scale** — so a client who needs AI inside the system of record is choosing between (a) building on `academico` (MIT, real, but 411 stars of external review for software that holds student records), (b) integrating *alongside* a GPL SIS across a process boundary and keeping the derivative question off the table — the `P27`/`P36` licence-provenance work is the gate for this — or (c) treating the SIS as a data source and putting the AI in the layer above it, which is where the permissive supply actually is. 🔵 **Option (c) is the one this base's shelves can staff today, and the reason to say so is that options (a) and (b) both look cheaper on a slide and are not.**

**Caveat, stated:** the `11`-of-`20` novelty figure measures *this base's* coverage of a topic page, not global supply, and the topic-page channel reads only the first 20 of 193. The licence readings are first-hand and the star counts are GitHub's own as displayed on `2026-11-05`.


## T51 — The licence boundary has moved out of the repository and into the run-time download, and a manifest-derived SBOM can no longer see it 🔴 new at p670

**The claim.** This base has said since p666 that *a licence identifier is not a licence* (**T47**), and `agents/top.md` has carried a section arguing that **the licence unit is the dependency graph, not the repository**. p670 found an instance that breaks even that: a product whose copyleft dependency is **neither declared, vendored nor pinned in any manifest**, because it is **fetched after installation**.

**The evidence, measured this pass.** [`DaRL-GenAI/instructional_agents_studio`](https://github.com/DaRL-GenAI/instructional_agents_studio) is MIT in full — payload `1,093 B`, `sha256₁₂ 338aae8b3c7c`, read at the real default ref. It ships `123` tracked files. **Nothing in the repository would fail a licence scan.** Its `NOTICE` then states that the slides and documents editor **is not in the package**: the application downloads it on first use into `~/.cache/instructional-agents/editor/<version>/`, verifies a SHA-256, and serves it to the browser — a trimmed build of [`ranuts/document`](https://github.com/ranuts/document) embedding **ONLYOFFICE `sdkjs` and `web-apps`**. **Both verified independently at p670 rather than taken from the NOTICE: `ranuts/document` is AGPL-3.0 (`2,018★`, pushed `2026-11-03`); `ONLYOFFICE/sdkjs` is AGPL-3.0.**

🔴 **So a client SBOM generated from the manifest reports this product as MIT, and it is wrong.** Not through concealment — the `NOTICE` is explicit and even explains the Section 7 additional terms and where the corresponding source is published. **The disclosure is in a file almost nobody reads, and in the one format no tool parses.**

🔴 **The second half of the same mechanism is a data-residency finding, not a licence one.** When the editor download is absent, the app falls back to a **hosted editor at `edit.chaxus.com`** — a third-party domain, named in the shipped `bin/cli.mjs`. The product's pitch is that the API key and the data stay in the browser. **The documents can leave to a third party by default.** For the EMEA public-sector and LATAM budget conversations this base tracks, that is the first question a buyer asks, and the honest answer is not the one on the README.

🔵 **Why this is a trend and not an anecdote.** The shape is a consequence of how 2026 education tooling is built, not a quirk of one lab. Browser-only, bring-your-own-key agents are the fastest route to a demo that installs nothing — which is exactly why this row was worth filing — and the heavyweight parts they cannot ship in a `123`-file static bundle (document editors, model weights, speech engines) get fetched at run time instead. **Every one of those fetches is a licence and egress decision made after the scan.** This base has already flagged the same shape once on weights: `wordlink` grants MIT on its *code* and names no licence for its released model.

**The rule, stated so it is not re-derived.** 🟢 **Read the `NOTICE`, not only the `LICENSE`, and ask what the artefact downloads on first run.** Add it to the triage in `compose/patterns.md` **P36**; the remediation — keep the MIT shell, replace the editor — is **P39**.

**Confidence.** 🟢 **High on the facts** — all four licence readings and the `bin/cli.mjs` reference were taken first-hand this pass. 🟡 **Medium on the generality**: one measured instance of the run-time mechanism, plus one adjacent instance on weights. **It is filed as a trend on the strength of the mechanism being structural, and the next pass should test it by counting how many shelf rows download anything on first run** — a question no pass has yet asked.

## T52 — The addresses rot faster than the software, and every integrity check the industry runs is blind to it 🆕 new at p671

**The claim.** An open-source education dependency can change *stewardship* — move from an individual maintainer to a standards body, or be renamed under its own foundation — while every automated check an engagement runs on it keeps passing at the old address, indefinitely. The URL stays live, the licence payload stays byte-identical, the default branch still resolves. **Nothing in the ordinary toolchain reports that the thing you are depending on is now owned by someone else.**

**The evidence, measured first-hand at `p671` on this base's own `197` shelf addresses.**

| Old address | New address | What proves identity | What still answers at the dead address |
|---|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | **[`openedx/openedx-platform`](https://github.com/openedx/openedx-platform)** | identical `HEAD` `78b892c6a`; licence payload **`sha256` identical** (`e12d78569742`, `35,136 B`, AGPL-3.0) | `git ls-remote --symref` → `refs/heads/master`; `raw.githubusercontent.com` → `200`; the full AGPL grant |
| [`NSoiffer/MathCAT`](https://github.com/NSoiffer/MathCAT) | **[`daisy/MathCAT`](https://github.com/daisy/MathCAT)** — the **DAISY Consortium** | identical `HEAD` `c6bba2f3a`; MIT `1,065 B`, *Copyright (c) 2022 NSoiffer* unchanged across the move | `git ls-remote --symref` → `refs/heads/main`; `raw.githubusercontent.com` → `200`; the full MIT grant |

**`2` of `197` addresses — `1.0%` — and both moved in the same direction: toward an institution.** An individual maintainer's accessibility library is now held by the accessibility standards body; a platform is now named after its own foundation. That direction is the substance of the trend, because **stewardship is what licence and governance risk actually track.** A row that reads *"MIT, maintained by an individual"* and a row that reads *"MIT, held by the DAISY Consortium"* carry the same licence and completely different answers to *who will still be maintaining this in three years*, which is the question a client asks.

🔴 **Why the toolchain cannot see it.** GitHub honours a rename redirect **indefinitely**. So the three channels this base — and essentially every SBOM, dependency audit and link checker — uses as proof of life all keep answering at the dead address: existence (`git ls-remote`), payload (`raw.githubusercontent.com`), and licence (the grant bytes, which are *identical*, not merely similar). 🔵 **The only channel that distinguishes them is the search index, and only as an error**: `repo:<old>` returns `422`, and `user:<owner>` returns `≥1`, so the address is unresolvable while its owner is fine. That pair is the detector (`repos/trending.md` `671-J`).

🔴 **And the second specimen shows how long this survives undetected in practice.** `p526` published the Open edX rename on **2026-10-29**. The correct address had been in `evidence/address-ledger.tsv` since **`p28`**, never filed. `p671` — **145 passes later** — still found the dead slug on `9` places across `3` live pages, including a component table that also still called the AGPL platform `Apache-2.0`. **The rename was not missed. It was published and not propagated.**

🔵 **What follows for an engagement, concretely.** An open-source inventory built on URL liveness is not an inventory of *what you depend on*, it is an inventory of *what still answers*. Add the `422`/`user:` pair to the audit (see **P40**), and treat a rename as a governance event rather than a link fix: re-read the grant at the new address, re-check the copyright holder, and ask who the new owner is before assuming the licence means what it meant.

**Confidence.** 🟢 **High on the facts** — both renames proven at `HEAD`-sha and licence-payload level this pass, the detector controlled on `18` probes at both signs. 🟡 **Medium on the rate** — `2` of `197` is this base's shelves at one moment, not a sector-wide measurement, and `p671` makes no claim about the general rename rate in education open source. 🟢 **High on the blindness** — that `git`, `raw` and the licence bytes all pass at a dead address is not an inference, it is what was measured.


## T53 — Every instrument that reads a licence agrees on the family and disagrees on the terms that decide usability 🆕 new at p672

🔴 **The finding.** Run three independent licence readers over one repository and they return three answers that are all "about" the same licence and are not interchangeable. On `July-Tea/EssayMate` at p672: `gh api` said **`NOASSERTION`**; this repository's own `ingest/probe-grant.sh` said **`CC-BY-4.0`**; the byte read said **`Attribution-NonCommercial-ShareAlike 4.0 International`**. Only the third is correct, and the difference between the second and third is the entire commercial question — `NC` forbids the derivative, `SA` forces reciprocity, and a label of `CC-BY-4.0` implies neither.

🔵 **Why this is a trend and not a bug report.** The three readers fail in three different, structural ways, and all three are in production across the industry:
- **A classifier that does not match emits a null** (`NOASSERTION`). `p658` established this means *"the classifier did not match"*, never *"no licence"* — but it is routinely rendered as "unlicensed" in dependency dashboards, which is a **false negative** that blocks usable software.
- **A classifier that normalises to a family drops the modifiers.** This is the dangerous direction: `CC-BY-NC-SA` → `CC-BY` turns a non-commercial grant into a permissive-looking one. **A false positive on usability.**
- **A grader with an unvalidated reference text condemns correct payloads.** `672-B`: a canonical MIT reference missing the words `THE USE OR` reported `4` of `4` verbatim payloads as mutated.

🔵 **The structural reason it keeps happening: a licence is not a label, it is a *conjunction of terms*, and every layer between the file and the dashboard is lossy by design.** SPDX identifiers compress well for permissive licences, where family and terms coincide, and badly for everything with modifiers — Creative Commons variants, dual grants, split grants by material type (`542-A`), run-time grant boundaries (`T51`). The compression is invisible because the output still looks like a licence.

🟡 **What is genuinely hard here.** You cannot byte-read every grant in a real dependency tree; classifiers exist because the volume demands them. So the usable rule is not "never use a classifier" but **"a classifier may triage and may never decide"**: let it rank, and byte-read the payload of anything you intend to *ship on*, anything it labels with a family that has modifiers, and anything it labels null. That is tens of reads, not thousands.

🔵 **For an engagement.** The inventory question a client asks is *"what are we allowed to do with this?"* and the artefact most tools hand back answers *"what family is this in?"*. Those come apart precisely on the licences that restrict commercial use — which is to say, precisely where the answer matters. **A licence column in an SBOM is a triage field, not a finding**, and the deliverable that is worth money is the short list of payloads actually read.

**Confidence.** 🟢 **High on the mechanism** — three readers, one payload, three answers, all four reproduced first-hand at p672 with the byte read as ground truth (`20,849 B`, `sha256₁₂ 1349a4b61484`), and the reference-text defect reproduced at both signs on five further payloads. 🟡 **Medium on the breadth claim** — the three failure modes are each evidenced here on one or two specimens, not surveyed across a corpus; the *family-collapse* mode in particular is demonstrated on Creative Commons and is predicted, not shown, for dual and split grants.

## T54 — The interoperability layer is where open source education software is still permissive, and it is specification-complete 🆕 new at p673

**`T50` established the floor:** the **student-information layer** — the system of record — is where open source education software stops being permissive (GPL-2.0 `i-educar`, LGPL-3.0 `fenixedu-academic`, AGPL-3.0 Open edX) *and* stops being adopted at scale. That trend has held for `25` passes and is not revised here.

**`T54` is its corollary, and it is the more useful half:** the layer **immediately above** the SIS is almost entirely **MIT / Apache-2.0 / ECL-2.0**, and every standard in it has a working permissive implementation this base has now read byte-for-byte:

| Standard | What it carries | Permissive implementation | Licence (byte-read) |
|---|---|---|---|
| **LTI 1.3 / Advantage** | launch, identity, roles, course context, grade return | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | Apache-2.0 (`11,361 B`) |
| **xAPI** | learning-activity records | [`openfun/ralph`](https://github.com/openfun/ralph) | MIT (`1,094 B`) |
| **xAPI + Caliper (warehouse)** | institution-scale analytics store | [`Apereo…/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | **ECL-2.0** (`9,878 B`) |
| **OneRoster 1.2** | rosters, enrolments, classes | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) · [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) | Apache-2.0 · MIT |
| **QTI 3** | portable assessment items | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | MIT (`1,072 B`) |
| **Open Badges** | verifiable credentials | [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | Apache-2.0 (`13,185 B`) |
| **(evaluation)** | randomised trials in a live course | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | Apache-2.0 (`11,323 B`) |

🟢 **Why this changes the engagement shape.** The integration surface has historically been the expensive, bespoke, re-written-every-time part of an education project, and the copyleft SIS underneath it has been treated as the blocker. `T54` says the blocker is routable: **nobody has to relicense or replace the system of record** — the work is to put a permissive, standards-conformant **adapter** in front of it. `edfi-oneroster` is the specimen: a OneRoster 1.2 API served from an Ed-Fi ODS, Apache-2.0, `6★`. Adoption is negligible and that is the point — this layer is **specification-driven, not popularity-driven**, so a six-star repository implementing a certified standard is a safer dependency than a six-thousand-star one implementing nobody's.

🔴 **The cost this trend carries.** These components are **maintained thinly**: `OpenLRW` ~14 months stale, `openbadges-validator-core` ~12, `OneRoster.NET` **three years**. Permissive and specification-complete does **not** mean actively maintained, and every one of those rows is filed with its staleness as a headline rather than a footnote. The correct reading is *fork base*, not *dependency* — and that maintenance cost belongs in the estimate.

🟡 **Standing prediction, falsifiable:** if `T54` is right, the next genuinely novel education supply this base finds will be **adapters and evaluators**, not tutors. `p673` found `9` of the former and `0` of the latter from the same eight legs that have returned tutors for `25` passes.

## T55 — The licence label from an index is now wrong in both directions on this base, and only the byte read is load-bearing 🆕 new at p673

**`T47` recorded three mechanisms by which an index and a payload disagree. `T53` sharpened it: every instrument agrees on the *family* and disagrees on the *terms that decide usability*. `T55` closes the loop by establishing the two signs, measured one pass apart:**

- 🔴 **Fails UNSAFE — understates restrictions.** `672-D`: `July-Tea/EssayMate` is **CC BY-NC-SA 4.0** (NonCommercial — it bars the commercial derivative this KB exists to scope). `gh api` said `NOASSERTION`; this repository's own `ingest/probe-grant.sh` said **`CC-BY-4.0`**, collapsing the family and dropping both the `NC` and `SA` terms. A pipeline trusting either label ships a grant it must not.
- 🔴 **Fails by HIDING SUPPLY — overstates restrictions.** `673-B`: three `NOASSERTION` labels in one pass, decomposing into **three unrelated mechanisms, all permissive** — a **split grant** whose scope preamble precedes verbatim MIT (`pupilfirst`), an **OSI-approved licence the classifier does not know** (`OpenLRW` → ECL-2.0), and a **verbatim Apache-2.0 body with the `APPENDIX` stripped** (`feedbacksystem`, `−524` normalised). A pipeline filtering on `spdx_id` discards all three.

🟢 **The operational rule, and it is cheap:** **never filter candidates on `license.spdx_id`.** Treat `NOASSERTION` as an instruction to **byte-read**, not as a verdict. Read the payload from `raw.githubusercontent.com` at the **real default ref** — which `p673` found to be `master`, `development`, `develop` and `dev` for four of its `18` candidates, so reading at `main` would have returned `404` and been recorded as *no licence*.

🔴 **And grade by normalised diff, not by length or hash.** `673-A`: `UniTime/unitime`'s payload is **`11,357 B`, the canonical Apache length exactly**, and hashes differently — a blank line added at byte `0` and the trailing newline dropped, `+1` and `−1` cancelling in length but not in hash. `671-R` said *hash, do not count*; `673-A` adds that **hash alone condemns an honest grant**. Length-equality is not identity; hash-inequality is not mutation. Both are descriptors; the normalised diff is the verdict.

## T56 — A published byte count can be an artefact of how it was read, and a stripped digest makes different payloads look identical 🟢 new at p674

**Evidence.** p674 re-measured every byte cell over `7 000 B` on this base's three sell shelves — `69` cells across `59` repositories. **`62` reproduce exactly.** Five are short by precisely their payload's **trailing-newline run**, which is the `P834` signature: a payload read into a shell variable loses its *entire* trailing newline run, so the count and the digest both describe bytes that are not what the repository serves.

🔴 **One case is proven rather than inferred, and it is the one that matters.** `Opetushallitus/compleap` was published as `13 956 B` with `sha256₁₂ 900a5a8a3c56`. The payload is **`13 957 B`** (`922e7e3be8ed`), and `900a5a8a3c56` is **the digest of the stripped bytes**. When *both* halves of a cell — size and hash — come from the capture, the cell is internally consistent and still wrong. 🔵 **A self-consistent cell is therefore not a verified cell**, which is the part that generalises.

🔴 **The consequence is worse than an off-by-one, because stripping DESTROYS DISTINCTIONS.** This base published *"`34,522 B` each"* across three AGPL-3.0 rows. Measured: the two `blend-ed` repositories are **`34 524 B`** (digest `8d56b405468a`, trailing run `2`); `openedx/openedx-ai-extensions` is **`34 523 B`** (`8486a10c4393`, run `1`). They are **different payloads**. All three collapse to the same `34 522 B` text (`20b067f86de3`) only *after* stripping — so the published figure did not just understate three sizes, it **manufactured a three-way identity that does not exist in any tree.** A byte count whose discriminating power has been stripped out of it cannot do the job a byte count is carried for.

🟢 **The fix that makes the numbers safe to read again is a digest, not a bigger number.** `11 357` is **simultaneously** the `apache/.github` canonical size and the *stripped* size of the `apache.org` canonical, so a cell reading `11 357 B` cannot be typed from its number alone. With both canonicals pinned — `11 357` / `58d1e17ffe51` and `11 358` / `cfc7749b96f6` — `numbas/Numbas` at `11 357 B` is demonstrably **correct** and `oppia/oppia` at `11 357 B` is demonstrably **wrong**, a distinction that was unavailable one pass ago.

🔵 **Why this is a sector trend and not merely housekeeping.** This base sells *licence certainty*: the byte count and digest exist so a client can confirm that the grant in a deliverable's dependency is the grant that was audited. An artefact in that figure attacks the one claim the artefact was introduced to support. 🔴 **And the defect was in the published cells, not in the library** — this repository's own `lib/payload_measure.sh` carries the correct primitive *and* predicted, in its own header, the environment denial that stopped p674 from sourcing it. **A control that exists but is not the only path to the number is not yet a control.**

⚠️ **Scope, stated plainly: a trailing-newline error changes the SIZE and the DIGEST, never the FAMILY.** Every licence *family* verdict this base has published stands. Only byte counts and hashes moved, and only in the five cells named.

## T57 — A grant verdict without a quotation cannot be audited, and the sector's corpora are where that costs money 🆕 new at p675

**Confidence: high — read at every author repository in the chain, both corpora, both releases.**

🔵 **`T21` and `P957` got the direction right:** as AI work moves from code to code-plus-evaluation-data, licence risk migrates to the corpus. 🔵 **And `P1007` got the channel right:** *"a corpus's licence is stated by its AUTHOR's repository, never by its funder's or distributor's page."* 🔴 **What p675 found is that the verdict recorded beside `P1007` is the opposite of what that channel says.**

| Corpus | Author's own repository | Grant, verbatim | Licence file |
|---|---|---|---|
| **PERSUADE 1.0** | [`scrosseye/PERSUADE_corpus`](https://github.com/scrosseye/PERSUADE_corpus) `main` @ `6b69a55c9d36` | 🟢 **CC BY 4.0** (README `3,486 B`, sha256₁₆ `809c25c2379d639e`; ⚠️ grant sentence ends in a truncated `…d.en)` link fragment) | 🔴 none |
| **PERSUADE 2.0** | [`scrosseye/persuade_corpus_2.0`](https://github.com/scrosseye/persuade_corpus_2.0) `main` @ `5bdbad1175d1` | 🟢 **CC BY 4.0** (README `2,081 B`, sha256₁₆ `2f984c8712650050`) | 🔴 none |
| **CLEAR** *(same author)* | [`scrosseye/CLEAR-Corpus`](https://github.com/scrosseye/CLEAR-Corpus) `main` @ `dbf1cf0df30b` | 🔴 **CC BY-NC-SA 4.0** (README `1,795 B`, sha256₁₆ `44d9d46bbd540d39`) | 🔴 none |

🔴 **`Gap 390` / `T21` has carried *"PERSUADE 2.0 is `CC-BY-NC-SA-4.0` by its author's own repo"* since p57. Two author repositories say `CC BY 4.0`. The `NC-SA` sentence is real and belongs to the author's *other* corpus** — same single-sentence construction, same author, one token apart. 🔵 The redistributor (`learning-commons-org/evaluators`, `LICENSE.md` `1,615 B`) makes the same substitution in a claim *about* upstream, linking to the repository that contradicts it.

🟢 **The trend, which is the mechanism and not the two data points.**

1. **A verdict without a quotation is unauditable.** `P1007` named the right channel and recorded no quoted payload, so for 618 passes there was nothing for a successor to check the verdict *against* — only a citation to re-trust. 🟢 **Every grant cell on these shelves now carries bytes and a digest; grant *prose* must carry the sentence.**
2. **The error ran in the safe direction, which is why nothing surfaced it.** Over-restrictive licence errors produce no ticket, no breach and no complaint — only work that was never proposed. 🔴 **It is the one class of licence error that is invisible by construction**, and this sector's corpora are where it bites, because the corpus is the valuable half.
3. **Corpora have no licence file.** All three repositories here grant in README prose; six licence filenames `404` on each; GitHub detects no licence on any. 🔵 **SPDX classifiers, `licensee`, SBOM tooling and GitHub's own label all return nothing**, so the only working reader is a person reading a sentence — and `P965`'s inverse shape (a grant with no file) is now three instances strong.
4. **The grant is detached from the bytes it governs.** The data is on Google Drive, not in the repositories. A README can be edited and a link replaced. 🔴 **A corpus grant can only be pinned by pinning the commit of the sentence that makes it** — which is what `P45`'s evidence pack must now do for data rows, and `P46` does.
5. **Sibling artefacts by one author are a contamination channel.** Two corpora, one author, near-identical grant sentences, different terms. 🔵 **Read the grant on the row you are filing, never on its neighbour.**

🟢 **Commercial consequence, stated once.** An automated writing evaluation product **can** be trained on PERSUADE under attribution alone — `P46` wires it. CLEAR **cannot** be shipped, and `SA` reaches derivatives including fine-tunes. 🔵 **`P675-A`: a grant verdict must quote the payload it came from.**

## T58 — 🔄 `T273`'s channel alias reproduces a third time, and the arm that had never been graded is this base's own `Ref` **column** 🔄 re-measured at p675

**Confidence: high — four fresh positives, the asymmetry control re-run, and a 61-repository sweep of an arm the existing census cannot see.**

🔵 **This is not a new finding and p675 nearly filed it as one.** The mechanism is already this base's `T273` (p273), re-stated as `T429` and `Gap 419-B`, and it already has a standing instrument — `make gate-branch-alias` (p428, **36 assertions over 26 controls**), which 🟢 **was run at p675 and PASSES**. 🔴 **Recording the near-miss, because it is the same defect class the base keeps finding in itself:** a measurement was made, it was correct, and it was about to be published as novel because the prior pass's record lived under a different name.

🟢 **What p675 adds is evidence, not a claim.** Four fresh positives for the alias, and the asymmetry `T273` left as *"mechanism NOT established"* re-run on both signs:

| Probe | Repositories | `raw…/master/…` | `raw…/main/…` | arbitrary ref |
|---|---|---|---|---|
| **`main`-only** (no `master` head) | `scrosseye/CLEAR-Corpus` (single ref), `scrosseye/persuade_corpus_2.0` (single ref), `HKUDS/DeepTutor` (11 heads), `learning-commons-org/evaluators` (44 heads) | 🔴 **`200`**, default-branch bytes | — | 🟢 `404` |
| **`master`-only** (no `main` head) | `CAHLR/pyBKT`, `adlnet/xAPI-Spec`, `chamilo/chamilo-lms`, `numbas/Numbas` | 🟢 `200` (genuine) | 🔴 **`404`** | 🟢 `404` |

🟢 **The asymmetry is confirmed on 8 repositories at both signs: `master` is aliased to the default branch, `main` is not.** 🔵 So it behaves exactly like GitHub's legacy redirect for repositories renamed away from `master`, and not like a general fallback — arbitrary names `404`.

🟢 **And the genuinely new arm.** `Gap 428-D` declared, on the pass that built the gate, that `branch-alias-census` *"grades PATHS and cannot see the PROSE that qualifies them"* — it inspects published `raw`/`blob` URLs. 🔴 **The `Ref` column of the three sell shelves is prose, so it has never been graded by anything.** p675 graded it: **`70` `master` cells over `61` distinct repositories** across `agents/top.md` (1), `repos/foundations.md` (44) and `verticals/solutions.md` (25), each re-resolved with `ls-remote --heads` plus `--symref HEAD`.

> 🟢 **`61 / 61` MASTER-EXISTS, `master` the default in every case, `0` corrupted cells, `0` unreachable.**

🟢 **That is the useful outcome and it closes an exposure rather than opening one:** the alias is live on the channel this base reads payloads with, it had an ungraded arm, and that arm is clean. 🔵 **`P675-B`: a ref is established by `ls-remote`, never by a `raw` `200` — which is `ACTION p419-B`'s instruction, now also applied to the `Ref` column and not only to published paths.**

## T59 — The ledger addresses a payload; it does not grade one — and this base's own backlog column is wrong in the unsafe direction 🆕 new at p676

**What was measured.** `p665` established, and `p673` confirmed across `16` of `16` filed addresses, that this base's yielding supply channel is its **own backlog**: `evidence/address-ledger.tsv` carries **`3,032`** addresses with `filed_on = -`, of which **`1,497`** have a recorded verdict in the permissive family. The ledger also carries a `last_verdict` column. Promoting from the backlog *on that column* is the obvious economy — the licence is already measured, and working a backlog off its own index is what a backlog is for.

🔴 **`p676` re-read the grant payload for the `5` best-tracked backlog candidates against their ledger verdict. Two contradicted it. Both contradictions point the wrong way.**

| Address | Ledger verdict | Payload, re-read at the real default ref | `p555` grader | Direction |
|---|---|---|---|---|
| [`leemonade/leemons`](https://github.com/leemonade/leemons) | **`MIT`** since `p12`, `7` passes | **Fair Code License** on the **Sustainable Use License** — not OSI; Leemons Edtech Solutions SL, Madrid | **SUBSTANTIVE** | 🔴 **UNSAFE** |
| [`beltromatti/get-it`](https://github.com/beltromatti/get-it) | **`Apache-2.0`** since `p123`, `9` passes | **modified Apache-2.0** — §6 trademark clause rewritten | **SUBSTANTIVE** | 🔴 **UNSAFE** |
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | `GPL-3.0｜Apache-2.0` since `p14` | **MIT**, verbatim, © *2016 Public Consulting Group* | **COSMETIC** | 🟢 safe — hid supply `6` passes |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | `MIT` since `p90`, `19` passes | **MIT**, verbatim | **COSMETIC** | 🟢 correct |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `GPL-2.0` since `p2`, `27` passes | GNU GPL, `15,214 B`, not verbatim against canon | **SUBSTANTIVE** | 🟢 correct in family |

**Why this is a trend and not a bookkeeping note.** `T55` established at `p673` that *the licence label from an index is wrong in both directions*. `T59` is the same defect **one level in** — the index that is wrong is now **this base's own**, and it is the index the base had just finished identifying as its most productive channel. `p673-B` found `NOASSERTION` concealing permissive supply (failing **safe**, costing opportunity). `T59` finds the ledger concealing **restricted** supply (failing **unsafe**, costing a client). The two are not symmetric: one loses a row, the other ships an AGPL-or-worse dependency into a commercial derivative.

🔧 **The operative rule, and it is cheap:** *re-read the grant payload at the real default ref, every time, for every promotion.* It cost `29` `git ls-remote` calls and `29` `raw.githubusercontent.com` reads for this pass's whole candidate set — roughly one minute of wall-clock — and it is the only step that caught either error.

🔵 **What a reader should take from this about the KB itself.** Every licence cell on the four curated shelves now carries a byte count and a `sha256₁₂`. Those are not decoration and they are not provenance theatre: they are the record that *someone opened the file*. A row without them is a row that inherited its verdict, and after `T59` an inherited verdict is a claim, not a measurement.


## T60 — `T50` survives as a *scale* statement and dies as a *tier* statement: the permissive student-information layer exists, at the size where most private education actually operates 🆕 new at p676

**`T50`, held for 28 passes, in its published form:** *the student-information layer is where open source education software stops being permissive and stops being adopted at the same time.* The evidence was consistent and it is still true at the top of the market.

🟢 **`p676` re-measured the tier rather than re-asserting it, and found the exception:**

| System of record | Licence | Stars | Scale it is built for |
|---|---|---|---|
| Open edX (`openedx/openedx-platform`) | 🔴 `AGPL-3.0` | — | national platforms, large universities |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 `GPL-2.0` (`15,214 B`, re-read at `p676`; default branch 🔴 **`mobile`**) | **652** | districts, public K-12 |
| `i-educar` | 🔴 `GPL-2.0` | — | Brazilian municipal networks |
| `FenixEdu/fenixedu-academic` | 🟠 `LGPL-3.0` | — | universities |
| `AlekSIS` | 🔴 `AGPL-3.0` | — | German public schools |
| `foradian/fedena` | 🟡 refused at `p673` — three independent liveness signals failed | — | — |
| 🟢 [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **`MIT`** (`1,094 B`, `6051a15f4d44`, verbatim) | **411** | 🟢 **small and medium institutions, multi-tenant** |

**The narrowed claim, which is the useful one.** The copyleft wall in the system-of-record tier is real **where the buyer is a ministry, a district or a university** — institutions whose procurement produced those licences on purpose. It is **not** present at the tier below, where the buyer is a private school, a language school, a training centre or a franchise network, and where Academico is MIT, maintained and multi-tenant by design (`storage/tenants/<id>`).

🔵 **Why that distinction is commercially load-bearing for a studio.** `p673` established the `T54` pattern — *nobody has to relicense the system of record; the work is a permissive adapter in front of it* — which is the right answer for a ministry engagement and an expensive one for a 40-school private network. For the latter, `T60` says the system of record **itself** can be permissive, so the AI layer is built *inside* the tenant model rather than bolted onto an API in front of a GPL core. That is a materially shorter engagement and it is the segment with the shortest procurement cycle.

⚠️ **Bounded, and the bound is stated.** `411★` is one address. `T60` claims the tier is *not uniformly copyleft*; it does not claim a permissive SIS exists at every scale, and this base has found exactly one. The next pass should test the tier at the **training-centre / corporate-academy** scale, which neither `T50` nor `T60` has measured.


## T61 — A knowledge base fails at publication before it fails at research, and nothing in the pipeline reads the destination file 🆕 new at p677

**Confidence: high — measured, not inferred.** p677 audited `p597`'s promotion ledger — `11` addresses, each with a *“promoted to”* cell naming a shelf file — against the files those cells name. **`4` correct, `1` on a different shelf than claimed, `6` absent from every shelf.** And [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) was claimed-as-filed by **two passes `25` days apart** while absent throughout; `prometheus-eval` and `rubric`, claimed in the same breath, are in **none** of the eight shelf files.

🟢 **The measurements were sound.** All six absent payloads re-measured at p677 to **exactly** the byte counts the ledger published. **So the failure is not epistemic — it is clerical, and it is invisible precisely because the research half worked.**

🔵 **Why this is a trend and not an incident.** This base verifies licences byte-for-byte against the internet, re-reads payloads across passes, grades operative bodies and pins digests — an unusually rigorous apparatus, pointed entirely **outward**. It has **no check pointed at itself**: no pass has ever asked *“is the row I said I filed actually in that file?”* That asymmetry is structural in automated knowledge bases, because the external claim is the one that feels falsifiable. 🔴 **The cost is total for the affected rows:** an unpublished row and a wrong row are indistinguishable to the studio engineer who opens the shelf before an engagement.

🔧 **The remedy is `6` lines and no network:** for every *“filed to”* / *“promoted to”* cell, `grep -iF` the address against the path the cell itself names. Run today it finds all seven defects. **`ACTION p677-B`.**

🔵 **Generalises past this KB.** Any pipeline that writes a provenance ledger and a content shelf in the same run should treat the ledger as an **assertion about the shelf** — and assert it. A ledger never checked against its own target is documentation, not provenance.

## T62 — Re-deriving a count from the table fixes staleness and creates blindness to duplication 🆕 new at p677

**Confidence: high — measured.** Four separate passes repaired a *stale* row count on these shelves (`p658`, `p663`, `p668`, `p676`), and the remedy each time was **“re-derive by counting the table rather than incrementing.”** p677 measured a different way — extracting the address from the **subject column only** and looking for repeats:

| Shelf | Rows | Distinct subjects |
|---|--:|--:|
| `agents/top.md` | `59` | `58` |
| `repos/foundations.md` | `128` | 🟢 `128` |
| `verticals/solutions.md` | `61` | `58` |

**All four duplicate rows were created at p676**, each labelled *“New at p676”*, each on a repository its own shelf already carried (`OpenMAIC`; `OpenOlat` since p653; `Academico` since p664; `frappe/lms` earlier). **The counts are no longer behind the table; they are ahead of the inventory.**

🔵 **The mechanism is general: a remedy inherits the blind spot of the thing it measures.** Counting rows is a faithful measure of rows and is silent about subjects, so the fix for staleness cannot see double-counting — and the pass that re-derived the number correctly still published a wrong one. **A row count is not an inventory count.** 🔴 **The harm is not cosmetic.** The two `frappe/lms` rows give **opposite advice** — one recommends it, the p676 one flags it as AGPL-3.0 and not a build-on option — and a reader gets whichever row they reach first. The two `OpenMAIC` rows publish two different star figures for one repository in one table.

🔵 **Same family as `T56`, one level up.** `T56`: a published byte count can be an artefact of **how** it was read. `T62`: a published count can be an artefact of **what unit** was counted. In both the number is honest and the *question* was wrong. 🔧 **`ACTION p677-C`:** add the distinct-subject check to `ingest/derive-counts.py`. 🔧 **`ACTION p677-A`:** merge the four pairs, preserving both cells' facts.

## T63 — A correction verified on the channel that caused the defect is not a correction 🆕 new at p677

**Confidence: high — four payloads measured four ways.** `p674` correctly diagnosed that `11,357` is *also* the newline-stripped size of the `11,358`-byte Apache-2.0 payload, so the byte count alone cannot separate the two canonicals, and it added digests to pin them. **One of the two digests it published is itself a stripped-capture artefact:**

| Payload | Bytes | sha256₁₂ |
|---|--:|---|
| `apache.org` canonical, as served | `11,358` | `cfc7749b96f6` |
| `apache/.github` canonical, as served | `11,357` | **`c71d239df917`** |
| `apache.org` canonical, newline stripped | `11,357` | **`58d1e17ffe51`** ← published as the `apache/.github` canonical |
| `apache/.github` canonical, newline stripped | `11,356` | `43070e2d4e53` |

**Four distinct values; the page published two of them as the two canonicals, and both describe the same document.** The distinguisher names one canonical twice, so it distinguishes nothing.

🔵 **The operational cause is mundane and reproducible: a shell `$(...)` capture strips trailing newlines**, so any payload measured through command substitution is silently one byte short and hashes to a value that exists nowhere on the internet. **Write the payload to a file; hash the file.** p677 re-measured all four that way, and re-confirmed `c71d239df917` independently from a new address — [`THU-MAIC/MAIC-Core`](https://github.com/THU-MAIC/MAIC-Core)'s `LICENSE` is byte-identical to `apache/.github` (`diff` exit `0`).

🔵 **The general claim, which is the point of this trend:** a remediation pass must verify on a **different channel** from the one that produced the error, because the cause is still live in the original channel. `T63` is the fourth member of a family this base has measured end to end — `671-R` (byte equality is not identity), `673-A` (hash inequality is not mutation), `676-A` (a `+2` residual concealing an edit to the operative terms), and now **the fix for a measurement defect, measured with the defect.** 🟢 **Each was caught by adding a channel, never by trusting one harder.**

## T64 — The licence boundary inside a platform runs through its components, and it runs in both directions 🆕 new at p678

A platform's licence is routinely used as a proxy for its parts. **p678 found that proxy failing in both directions, in the same pass, on two of this industry's most prominent assets.**

- **Permissive parts inside a copyleft platform.** Open edX core is `AGPL-3.0` — the standing copyleft objection this base has recorded against it. Its two **official mobile clients are `Apache-2.0`**: [`openedx/openedx-app-android`](https://github.com/openedx/openedx-app-android) and [`openedx/openedx-app-ios`](https://github.com/openedx/openedx-app-ios), carrying a **byte-identical** grant payload (`11,356 B`, `43070e2d4e532684`). A branded commercial mobile client ships without the binary inheriting AGPL.
- **An ungranted part inside a permissive project.** `THU-MAIC/OpenMAIC`, the ~42k-star multi-agent classroom, is permissively granted. Its front end [`THU-MAIC/MAIC-UI`](https://github.com/THU-MAIC/MAIC-UI) — `184★`, `39` forks — has **no grant payload at all**: six licence paths probed at the real default ref, all `404`.

🔵 **Both errors are invisible to a repository-level licence badge, and both change a scope.** The first *expands* what a studio may sell; the second *removes* a component someone would reasonably assume was adoptable. **The unit of licence diligence is the component you will actually ship**, which is this base's standing *"the licence unit is the dependency graph"* clause pushed down one level — from dependencies to **sibling repositories under one owner**.

🔧 **The practical test is cheap:** for every platform in a proposal, byte-read the grant of **each repository you will ship code from**, at its real default ref. p678 did this for `12` addresses in one pass.

## T65 — Forks per star separates deployed platforms from imported libraries, and the floor matters more than the ranking 🆕 new at p678

This base hypothesised at `p540` that **forks beat stars for institutional software** and ranked `14` points by forks-per-star, finding a boundary near `0.5` between a *deploy-per-institution* class and an *import-as-dependency* class. p678 is the **out-of-sample test**: `12` new points, measured independently, merged into [`evidence/forks-per-star-rank.2026-11-06-p678.tsv`](../evidence/forks-per-star-rank.2026-11-06-p678.tsv).

🟢 **The boundary held.** Institutional infrastructure landed above `0.5` without exception — LMS mobile clients (`1.632`, `1.097`), LTI libraries (`1.074`, `0.800`), a school ERP (`0.725`), Kolibri installers (`0.806`). The two **agent-shaped** repositories landed below it: `MAIC-UI` `0.212`, `moodlehq/wiki-rag` `0.189`. **Platform code is forked and deployed; agent code is imported.**

🟢 **New `#1` at adequate `n`:** `openedx/openedx-app-android` at `1.632`, displacing `dspace/dspace` (`1.364`), which had led since `p540`.

🔴 **But the adequacy floor, not the ranking, is where this metric earns trust.** Three of the top seven *raw* ratios are inadmissible at `n >= 20` stars: `oppia/oppia-ml` (`3.000`, `n=3`), `learningequality/kolibri-app` (`1.727`, `n=11`), `moodlehq/moodle-mlbackend-python` (`1.053`, `n=19`). **An unfloored ratio ranks a three-star repository first.** Published with the caveat in the cell rather than ranked — and the `n=3` verdict reproduces the one this base already recorded for `ucfopen/pylti1.3`.

🔧 **For a platform shortlist: rank by forks per star, apply an `n >= 20` floor, and read the stale date before the ratio** — `1EdTech/LTI-Tool-Provider-Library-PHP` ranks `#6` and was last pushed in `2018`.

## T66 — A curated base's standing failure mode is republishing its own holdings as discovery 🆕 new at p678

`p677` diagnosed this base as one that **measures well and publishes unreliably**: six addresses claimed-as-filed were absent from every shelf. **p678 found the same defect at the opposite sign** — a pass about to publish, as a new mechanism, something the tree already held.

The intended headline was that two verbatim `Apache-2.0` payloads can share a byte count and hash differently because the appendix placeholder style differs (`{yyyy}` vs `[yyyy]`), and that the authoritative `apache.org` text is `11,358 B`. **Scored against the tree before drafting: all of it held** — the ASF digest `cfc7749b96f63bd3` in `22` files, both variant digests already recorded, the `11,356–11,358 B` span stated verbatim on the foundations shelf, and the general rule already registered as **`T101` — *a length is not an identity***.

🔵 **The two failures are one rule at opposite signs**, which is the same shape as `667-C`: *a knowledge base must test its own claims against itself, in both directions.* `p677` tested whether a published claim was **on the shelf**; p678 tested whether a **new claim was already** on the shelf. **Neither test is expensive and neither was standing practice.**

🔧 **`ACTION p678-H`, now registered:** a pass's headline claim is scored against the tree **before** it is drafted, with the same variant-spelling discipline already applied to search legs — because `667-B` proved a fixed-string needle misses a held fact `53.8%` of the time on orthography alone.

## T67 — A reachability verdict belongs to an endpoint, not a host 🆕 new at p678

This base has recorded `api.github.com` as `403` **channel-wide** since `p670`, repeated at `p677`. **p678 refutes the scope of that claim with a control pair:**

| Call | Result |
|---|---|
| `gh api repos/openedx/openedx-app-android` | 🔴 `403` — *"GitHub access to this repository is not enabled for this session"* |
| `gh api -X GET search/repositories -f q='repo:openedx/openedx-app-android'` | 🟢 `200`, **returning the same fields**: stars, forks, `license.spdx_id`, `pushed_at`, `language` |

**Same host, same tool, same credential — opposite verdicts.** The block is a **session repository-scope** restriction on the per-repository path, not a network block on the host. Every star and fork count published at p678 came through the search path.

🔵 **The general claim:** a one-line-per-host reachability table **cannot express this**, and in recording the host as dead it discarded a live channel for an unknown number of passes. 🔧 Reachability tables name the **endpoint**, and a dead verdict on one path requires a second path tested before the host is written off.

## T68 — Placement is a property of the *search*, not of the repository 🟢 new at p679

Two consecutive passes ran the same eight legs against the same sector and got opposite placement results, and the difference was which legs supplied the finds. p678 sourced nine addresses by enumerating owner organisations and placed **zero** of them. p679 sourced four from the **four regional legs** and placed **three**. The mechanism is not subtle: a global query ranks on popularity, which selects for software that has deliberately shed its locale in order to travel; a regional query selects for software that is bound to a curriculum, a statute, a language or a timezone — and that binding *is* the placement evidence.

**Consequence for this base:** an unplaced shelf is not evidence that the sector is placeless. It is evidence that the search was global. Regional legs are not a reporting courtesy to be run after the real search; they are the only legs that return placeable supply.

## T69 — The strongest placement evidence is what a deployer *inherits*, not what an author *declares* 🟢 new at p679

This base has ranked its placement channels repeatedly, and p679 adds a class that outranks most of them: **the shipped default**. `Gego-K12/gegok12` had been carried unplaced through many passes, because its owner declares nothing and its README names no country. Its `.env.example` ships `TIMEZONE = 'Asia/Kolkata'`, and `config/app.php` resolves the application timezone from that variable — so every operator who installs it without editing config inherits an Indian locale. Similarly, `yasserhegazy/lab-grader-skill` writes student feedback in **Palestinian colloquial Arabic by default**.

A default is better evidence than a declaration for three reasons: it is **load-bearing** (changing it changes behaviour, so it is maintained), it is **unmarketed** (nobody sets a default timezone for positioning), and it describes **who is affected** rather than who wrote it. The adjacent new class is the **regulatory regime**: a `FERPA Compliance` section places `jlouisbru/Canvas-grading-with-AI` in North America more reliably than its author's address, because FERPA is meaningless outside the United States. Ranking, strongest first: national curriculum standard → jurisdiction-specific statute → shipped locale default → named institution with matching institutional domain → body-text language → owner self-declared location. 🔴 Below the line entirely: **language of instruction** — `bp-master-agent` teaches Brazilian Portuguese and is for that reason *not* LATAM-placed.

## T70 — The sector finally has a measurement instrument, and it is regional rather than global 🟢 new at p679

This base has recorded the evidence problem as education AI's central weakness across many passes, and has repeatedly noted that no dominant open-source evaluation exists. `bncc-dev/bncc-benchmark` is the first asset here that closes a usable part of it — and the significant thing is that it does so **for one country's curriculum**, not for education in general. It measures how much models fabricate BNCC codes and texts without access to the structured source, publishes **17,100 raw responses** from 19 models, holds a **private set back against contamination**, and reports a faithful-text spread of **88% down to 3%**.

The design choice that generalises is scoring **"refused a fake code"** separately from **"reproduced a real one"**. Those come apart in the published round — a model can sit mid-table on fidelity while accepting **10%** of fabricated codes — and they fail differently in production: confident confirmation of a curriculum objective that does not exist is a safeguarding problem, where poor recall is merely a quality problem. **The transferable lesson is that education evaluation is curriculum-shaped**, so it will arrive as a family of national benchmarks rather than one global leaderboard, and whoever grounds a tutor in a curriculum should be reporting both columns against the benchmark for *that* curriculum.

## T71 — Forks per star has **two regimes**, not one scale, and the adoption floor hides the second one 🔴 narrows T65, new at p680

`T65` established forks-per-star as this base's instrument for separating a **deployed platform** from an **imported library**, and said the floor matters more than the ranking. p680 keeps the instrument and breaks the single scale it assumes.

`jsboige/CoursIA` measures **`f/★ = 9.563`** — `153` forks against `16` stars. The census maximum this base had recorded was `moodle/moodle` at `1.017` (`p489`), with `openedx/openedx-app-android` at `1.632` (`p678`) as the outlier. `9.563` is not a larger value on the same axis; it is **a different behaviour**:

| Regime | `f/★` | What a fork means | Example |
|---|--:|---|---|
| **Deployment** | ~`0.3` – `1.6` | one institution runs its own instance | `moodle/moodle` `1.017`, `portabilis/i-educar` `0.767` |
| **Classroom** | ~`10` | one *learner* takes a working copy | `jsboige/CoursIA` `9.563` |
| **Reading** | <`0.3` | consumed in place, rarely copied | `BedirT/ACM-ICPC-Preparation` `0.274`, `hyyhf/agent-book-code` `0.153` |

Two consequences for anyone scoping from these shelves. **First, a single ranking is uninterpretable** — a course repository and a platform appear on the same list with the course repository on top, and the number means something different in each row. **Second, and this is the expensive one: the `stars:>40` floor that every supply census on this base has used excludes `CoursIA` outright.** The adoption filter and the adoption signal point in opposite directions here: `16` stars reads as *nobody uses this*, while `153` forks of a curriculum actively pushed the same day reads as *a class is running on it right now*. A star floor is a proxy for *attention*, and teaching material is used without being starred.

🔵 **The practical rule:** rank by `f/★` within a class, never across classes, and when a candidate fails a star floor, read its fork count before dropping it.

## T72 — A channel is exhausted when its new findings stop being *usable*, not when it stops returning rows 🔴 new at p680

p680 swept nine GitHub topic heads, six of which this base had never queried, and the raw yield looks healthy: `80` candidates at `stars:>40`, `21` of them absent from this repository entirely. On a row count, that is a productive channel. On the only test that matters it is finished: **of the `21` novel addresses, `1` is a permissive, live education asset.** The other `20` fail on licence (GPL-3.0, AGPL-3.0, `NOASSERTION`, no grant), on dormancy (several large curricula last pushed in 2023–2024), or on being the wrong sector entirely (`topic:plagiarism-detection` returns music-tooling and binary-similarity research alongside academic integrity).

This matters because the two readings recommend opposite actions. *"The channel returned 21 new addresses"* argues for sweeping more topics. *"The channel returned one usable address"* argues for spending the next pass somewhere else — and the second reading is the correct one, because `63.8%` of everything the channel returned is already on these shelves.

🔵 **Three topic heads are simply empty**, and that is a vocabulary finding rather than a supply finding: `topic:early-childhood-education` → `0` repositories, `topic:teacher-tools` → `0`, `topic:competency-based-education` → `1` (already held). These are terms **educators** use and **repository owners do not tag with** — the same mismatch `T23` found from the other direction when the permissive-platform claim collapsed on vocabulary rather than availability. A `0` on a topic head is evidence about the tagging, not about the world.

## T73 — GitHub's licence field has no direction, and the licensor it punishes is the careful one 🔴 new at p681

Every supply census on these shelves works from the mandate *"focus on MIT / Apache-2.0 / BSD"*, and the cheapest way to honour it is GitHub's own licence facet — the `spdx_id` that `search/repositories` returns. p681 read the **grant bytes** of five repositories that all report **`NOASSERTION`**, on the same day, at their resolved default refs:

| repo | `spdx` | grant payload, byte-read | what a facet filter does |
|---|---|---|---|
| `Saidkhusayn/student-dropout-early-warning` | `NOASSERTION` | 🟢 **verbatim MIT** + an explicit `CC BY 4.0` data carve-out | 🔴 **drops a permissive row** |
| `ChrisWhiteSr/teach-skill` | `NOASSERTION` | 🟢 **MIT** + a portions notice naming an upstream that verifies | 🔴 **drops a permissive row** |
| `GarethManning/education-agent-skills` | `NOASSERTION` | 🔴 **CC BY-SA 4.0** | 🟢 right, by accident |
| `PreTeXtBook/pretext` | `NOASSERTION` | 🔴 **GPL-2-or-3**, text absent from the repo | 🟢 right, by accident |
| `workforce-data-initiative/skills-api` | `NOASSERTION` | 🔴 **non-commercial**, and names a different program | 🟢 right, by accident |

🔴 **Two of five sit on verbatim MIT and three on grants that forbid a commercial derivative.** The field is not a weak signal that needs a wider threshold; it is a signal with **no direction** — the three it classified usefully it classified for reasons unrelated to the two it got wrong.

🔵 **The mechanism, which makes the behaviour predictable rather than random.** GitHub's detector matches licence **bodies**. Anything appended to, prepended to, or substituted for a canonical body defeats it. So the repositories it fails on are precisely the ones whose authors did something *more* careful than pasting a template: `Saidkhusayn` separated code from data in the grant file, `ChrisWhiteSr` attributed an upstream inside the grant, and `PreTeXtBook` wrote a correct licence *notice* and shipped no body for the detector to find. **The detector rewards the template and punishes the drafting.**

🟡 **Scope, so this is not overread.** This says nothing about SPDX as a standard, nor about repositories that do report `MIT` — in **`9` of `9`** cases this pass where the facet read `MIT`, the bytes agreed (counted from [`evidence/p681-candidate-verification.2026-11-06-p681.tsv`](../evidence/p681-candidate-verification.2026-11-06-p681.tsv), not estimated). **A positive `MIT` reading was reliable every time it appeared; it is the absence of a reading that carries no information.** The claim is narrower and operational: **`NOASSERTION` is not evidence of anything, in either direction, and a census that treats it as "no permissive grant" will systematically lose the most carefully licensed projects in the field.** The only reading is the bytes at the resolved default ref.

## T74 — Where a copyleft education platform fronts a public API, the permissive opportunity is the client 🟢 new at p681

This base's standing objection to the education platform layer is licence-shaped: the systems institutions actually run are copyleft. Moodle is GPL-3.0, Chamilo GPL-3.0, Open edX AGPL-3.0, Pressbooks GPL-3.0, and `PreTeXtBook/pretext` is GPL-2-or-3 — so a client-branded fork carries source disclosure, and `T6` treats the arrival of an Apache-2.0 LMS as news precisely because the alternative is so constrained. **p681 found that the objection is avoidable without an Apache-2.0 platform, by moving one layer out.**

| layer | project | licence | reaches your code? |
|---|---|---|---|
| platform | `pressbooks/pressbooks` | 🔴 GPL-3.0 | yes, if you fork it |
| authoring toolchain | `PreTeXtBook/pretext` | 🔴 GPL-2-or-3 | yes, if you derive from it — **no**, if you run it as a program |
| **corpus access client** | `johnnyrobot/pressbooks-cli` | 🟢 **MIT** | 🟢 **no — it holds no platform code** |
| corpus | 28 networks, **`9,601`** open textbooks | openly licensed per book | reachable with **no account, key or token** |

🟢 **The mechanism is ordinary copyright law rather than a licence loophole, which is why it is safe to build on.** Copyleft attaches to derivative works. A client that speaks a platform's public REST API links against nothing the platform licenses, so it inherits nothing — and running a GPL program over a client's content (PreTeXt converting XML to PDF) imposes obligations on neither the content nor the code beside it. **The obligation follows the code, not the data and not the pipeline.**

🔵 **Generalised, and this is the reusable part: for any copyleft platform on `verticals/solutions.md` that exposes an API, ask what the permissive client tier would be before asking whether the platform can be relicensed.** Moodle, Open edX, Chamilo, Sakai and ILIAS all expose web services. The permissive asset is the agent, the exporter, the analytics client or the corpus reader that talks to them — and `P51`'s "ship over the LMS via LTI, never fork it" is the same argument arriving from the integration side rather than the licence side.

🔴 **The limit, stated so the trend is not over-applied.** This buys access, not control: you cannot change platform behaviour from outside it, and anything you need *inside* the platform is still copyleft. It also assumes the API is public and adequate — and `pressbooks-cli`'s README is a catalogue of how inadequate a real one can be (no directory endpoint, a `search` parameter accepted and discarded, `per_page` hard-capped at `10`, `403` to an unrecognised `User-Agent`). **The licence problem moves to an engineering problem, which is the trade worth making, not a free lunch.**


## T75 — The next binding education-AI deadline in North America is a **funding** rule, and it buys outcome plumbing rather than AI 🟢 new at p682

Every deadline this file has tracked in North America has been a *restriction*: state bills, exam bans, district policy mandates. **Workforce Pell is the first one that is a cheque.** The US Department of Education's final rule extends Pell eligibility to **short-term programmes** — roughly **`150`–`599` clock hours**, about **8–15 weeks** — **generally effective `2026-07-20`, with optional early implementation from `2026-07-01`**, offered only by accredited institutions, with **governors and state workforce boards** designating high-demand industries and approving programmes.

🟢 **The trend is in the eligibility condition, not in the money.** A programme keeps Workforce Pell only by passing **completion, outcome and earnings tests, per programme, over time** — and a programme with zero or negative value-added earnings **loses eligibility**. That converts a funding opportunity into a **longitudinal, auditable, per-programme reporting obligation**, landing on community and technical colleges and continuing-education arms: precisely the institutions whose student-records estate is thinnest and whose BI layer is a spreadsheet.

| What the rule demands | What answers it on these shelves | Licence |
|---|---|---|
| per-learner activity and completion evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (`144★`) over [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) (`955★`) | 🟢 Apache-2.0 / permissive |
| roster and programme identity across systems | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster), [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) | 🟢 permissive |
| at-risk detection before the completion test fails | [`Saidkhusayn/student-dropout-early-warning`](https://github.com/Saidkhusayn/student-dropout-early-warning) | 🟢 **MIT** (+ `CC BY 4.0` data carve-out) |
| credential evidence | [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 permissive |

🔵 **Why this generalises past one US rule.** The pattern — *a regulator funds a programme and makes the money conditional on measured outcomes* — is the strongest buying trigger this file has found in any region, because it is **dated, statutory, and unambiguous about what must be produced**. `T3` recorded that governance became the buying trigger when usage outran policy; `T75` is the sharper form: **the buying trigger is an audit you cannot pass with a spreadsheet.** 🔴 **The limit, stated so the trend is not over-sold: none of this is AI.** The compliance work is data plumbing, and an engagement that leads with an AI tutor will lose to one that leads with an earnings-linkage report. The AI is what you sell *second*.

## T76 — A closed vocabulary decays silently, and the report that it was fixed is the most dangerous artefact it produces 🔴 new at p682

This KB's `Region` field is a closed vocabulary of five values. At p682 it held **`114` distinct strings**, with **`367` of `795` cells (46 %) outside the vocabulary**: `**EMEA**` beside `EMEA`, `🟢 **LATAM**` beside `LATAM`, `EMEA (Finland)`, `APAC 🇨🇳`, `Global (unplaced)`, `Not placed`, `—`, and in seven rows an entire sentence of prose sitting in the field a filter reads.

🔴 **The failure mode is not untidiness — it is partial answers that look complete.** A reader filtering `Global` lost the `38` rows spelled `Global (unplaced)`. A reader filtering `EMEA` lost the `32` spelled `**EMEA**` and the `8` spelled `EMEA (Finland)`. **Nothing in the output was marked wrong**, because a bucket of size zero and a bucket that was never queried are indistinguishable downstream. This is the same shape as `T73` (a licence field with no direction) and `682-C` (two rows for one subject): **in each case the defect is invisible to the consumer of the data and visible only to a census.**

🔵 **The decay mechanism, which is the transferable part.** Each individual deviation was *locally reasonable*: bolding a region to match the row's typography, appending `(Finland)` because the country is the useful fact, writing `Not placed` because it is more honest than `Global`. **A closed vocabulary cannot absorb local reasonableness** — every well-meant annotation is a new bucket. The field must carry the value and **nothing else**, with the country, the evidence class and the confidence living in prose or in their own fields.

🔴 **And the most dangerous artefact was the fix report.** `p669` recorded this column *normalised* — truthfully, for one table out of eight — and that note then stood for thirteen passes as evidence the problem was handled, which is why it was never re-measured. **A repair stated at the top of one file is not a repair of the base.** The rule p682 adopts: **a normalisation claim must publish the census it is derived from, before and after, over every file it claims to cover** — `114` → `8` distinct, `367` → `3` non-conforming, and all three survivors shown to be non-placements (`Verdict`, `Adopcion`, `mixed`). ⚠️ **The residue is honest and unresolved:** `Global` now means both *truly global* and *not placed*, `240` cells hold it, and a sixth value would re-break the filter. The right fix is a `placed: true|false` field beside the region.

## T77 — A knowledge base's own novelty measurement is a channel, and it decays toward optimism 🔴 new at p683

p683 swept `558` education repositories over `22` search heads and measured novelty **twice**. Against the three sell shelves (`344` slugs): **`71.1 %` novel**. Against the whole tree (`5,053` slugs): **`47.1 %` novel** — `90` already shelved, **`205` already in the tree but never shelved**, `263` absent.

🔴 **The shelves and the tree answer different questions, and only one of them is the question.** A shelf records what was *bought*. The tree records what was *looked at and rejected*. Measure against the shelf and every rejected candidate reads as a discovery — so the error has a **direction**: it always overstates novelty, never understates it. On p683's own hand-picked set the overstatement was `17` of `21` candidates.

🔵 **Why this is a trend and not a one-off.** The bias grows monotonically: every pass that assesses a candidate and declines it adds another row to the tree and nothing to the shelves, so the gap between the two denominators widens with every pass forever. A base at pass `683` has `5,053` slugs in the tree and `344` on the shelves — a factor of `14.7`. At pass `100` that factor was small enough that the wrong denominator gave nearly the right answer, which is exactly why the habit survived.

**Signal**: p680 measured the split correctly (`51` shelved / `8` in-tree unshelved / `21` absent). p683 reproduced the *method* and still used the wrong denominator. A measurement discipline that is written down but not instrumented regresses to the convenient default.

**What to do with it on an engagement**: the same asymmetry governs a client's own build-vs-buy inventory. An architecture review that lists what the client *runs* and not what they *evaluated and rejected* will re-propose rejected tools as new options, and will do it confidently.

## T78 — Jurisdiction evidence has a strength ordering, and the strongest channel available is a registry fact 🟢 new at p683

Across p683's sweep, five distinct placement channels were exercised on the same candidate set, and they do not have equal authority:

| rank | channel | authority | why |
|---|---|---|---|
| `1` | 🟢 **committed ccTLD / restricted TLD host** | registry fact | `.br` is registry-restricted to Brazil; `.edu` to US institutions. Not an inference |
| `2` | 🟢 **named national examination** | statutory fact | 公务员笔试, 高考, ENEM — an examination is a jurisdiction |
| `3` | 🟡 **named institution, singular** | strong | `uni-heidelberg.de`, `hax.psu.edu`. Fails the moment it becomes a *list* |
| `4` | 🟡 **body-text language, measured** | weak but defensible | `55.7 %` CJK is a number; "it looks Chinese" is not |
| `5` | 🔴 **owner `location` field** | empty in practice | three consecutive passes have produced nothing from it |

🔴 **Each channel has its own characteristic false positive, and they are not interchangeable.** The TLD channel's is the **documentation placeholder** (`acme.edu` matched on this very sweep). The named-institution channel's is the **enumeration** (`vkaravir/JSAV`'s grant names Aalto *and* Virginia Tech — two regions, so no placement). The language channel's is the **substring inside an identifier** (`china` inside the org name `datawhalechina`).

🔵 **The practical rule, and it is cheap**: take the highest-ranked channel that returns a *single* answer, verify that answer is not a placeholder or a list, and write down which channel it came from in the row. p683 placed three repositories on channels `1`, `1` and `4`, and **refused three placements outright** rather than drop to channel `5`.

**What to do with it on an engagement**: a client's data-residency or sovereignty audit faces the identical problem. Residency claimed from a vendor's marketing page is channel `5`; residency read from the TLD and the contracted region of a storage bucket is channel `1`. The EU AI Act and Vietnam's Decision 33 both bind on where a system *operates*, not on where its vendor says it does.

## T79 — Academic integrity is the sector's one *statutorily forced* AI demand with essentially no permissive supply behind it 🟢 new at p684

Every other demand this base tracks has a permissive answer somewhere on its shelves. This one does not, and the asymmetry is measured rather than impressionistic.

**Demand side, all of it already held on this base's own pages:** Ofqual published AI-and-coursework-integrity resources in March 2026; the UK DfE issued generative-AI product safety standards in January 2026; the EU treats assessment as Annex III high-risk from `2027-12-02`; Vietnam's Decision `33/2026/QD-TTg` names **automated assessment** as high-risk; TEQSA requires every Australian higher-education provider to file a generative-AI risk action plan; UNESCO IESALC finds `87 %` of surveyed Latin American institutions using AI with `26 %` holding a strategy. Assessment integrity is the single capability named by regulators on **four** continents.

**Supply side, censused at p684 across four never-swept heads:** `395` candidates, `337` novel, `132` permissive — and **`0` live permissive repositories above `20★`**. The category's most-starred permissive asset (`163★`) is self-declared archived *and* built on an upstream API that no longer exists. The usable shelf is `16★` and below.

🔴 **The gap is not a discovery failure — it is a property of the problem.** AI-text detection is a classifier against an adversary that is already productised (`Cam3L1/ghost-skill` exists to defeat GPTZero, Turnitin and CopyLeaks), so an open detector is obsolete the week it ships and nobody accumulates stars on it.

🟢 **Which is why the three assets worth having are the ones that are not detectors.** `OSLL/code-plagiarism` compares ASTs — structure, not style, and renaming does not defeat it. `DSL4-Digital/RefExists` resolves citations against Crossref, arXiv and Semantic Scholar — a DOI either resolves or it does not. `pisan-labs/code-viva` examines the student about their own code — authorship by examination. **All three are decidable; none of them classifies prose.** The sellable position in this category is deterministic evidence, and it is open for the taking.

## T80 — The licensor's legal-entity suffix is a rank-1 jurisdiction fact, and it is sitting in a file this base already reads for every row 🟢 new at p684

`T78` ranked five placement channels and put registry facts at rank 1. p684 adds a sixth that belongs at rank 1 and costs **nothing**.

**`DSL4-Digital/RefExists`** carries `Copyright (c) 2026 DSL4 Digital, S.L.U.` in its `LICENSE`. `S.L.U.` is *Sociedad Limitada Unipersonal* — a company form that exists only in the **Spanish** commercial register. That is not an inference about where someone lives: it is the jurisdiction of incorporation, stated by the licensor, in the operative grant.

🟢 **The economics are what make it matter.** This base already fetches and hashes the grant payload for **every** row it files — the channel is a `grep` over bytes already in hand, with no extra request. The equivalent class generalises directly: `S.L.`/`S.L.U.`/`S.A.U.` (Spain), `GmbH`/`UG` (Germany), `S.à r.l.` (Luxembourg, France), `B.V.` (Netherlands), `Oy`/`Ab` (Finland, Sweden), `Pty Ltd` (Australia), `Ltda`/`S.A.` (Brazil and Spanish-speaking LATAM), `K.K.`/`G.K.` (Japan), `LLC`/`Inc.` (United States — weakest of the set, since US entity suffixes do not identify a state and barely identify a country).

⚠️ **Two limits, stated so the channel is not over-read.** It gives the jurisdiction of **incorporation**, which for a vendor is usually the right answer and for a holding company may not be. And it only fires when the licensor is a **company** — p684's other five candidates were licensed by individuals or contributor collectives, so the channel placed `1 of 6`. 🔵 Low hit rate, zero cost, rank-1 authority: run it on every row, expect it to be silent most of the time.

## T81 — Past a certain maturity, a curated base learns more demand-side facts from repositories than from demand-side searches 🔴 new at p684

p684 ran the four mandated regional demand legs and the four mandated English legs. `18` facts returned, **`16` already held** — and held in more detail than the sources gave them.

🟢 **The two facts that were genuinely novel arrived through a repository's README.** **Lei 12.764** (Brazil's national autism-rights policy) and the **LBI / Lei 13.146** were absent from this entire knowledge base, and both came out of `Fernandosr85/sistema-gestao-pei` — a `1★` prototype found by a `topic:special-education` sweep, not by any question about Brazilian education policy.

🔴 **This inverts the direction the mandated legs assume.** Demand legs read secondary commentary, which converges on the same canonical set of statutes and surveys; a base that has already absorbed that set will keep scoring near-total nil on them (`T72`). A *working implementation*, by contrast, cites the statutes its author actually has to comply with — including the ones no commentary mentions, because they are too specific to generalise about.

🟢 **The operational consequence is a reordering, not an abandonment.** Keep the demand legs — they are the control that proves nothing was missed, and the nil is only informative because the denominator is written down. But **mine the shelved repositories' own texts as a demand channel in their own right**: statutes, named examinations, accreditation bodies and funding programmes cited in a README are facts a client's legal team will recognise, and `T78` already ranks them above anything a trend article can offer. This also explains why `T78` rank 2 keeps producing: a statute citation is simultaneously the best **placement** evidence and a novel **demand** fact.

## T82 — A repository name is not a licence, and the collision risk is concentrated exactly where adoption is highest 🟢 new at p685

Measured at p685 across all `104` distinct bare repository names on `agents/top.md`, filtered to exact name equality: **`63` (`60.6 %`) share their name with at least one other repository**, `23` have a namesake whose grant *differs* from the canonical's, and **`43` pair a permissive canonical with a namesake that is copyleft or carries no grant at all.** In total `1,422` foreign repositories wear this shelf's names, of which **`936` (`65.8 %`) have no licence file at all** and `82` are copyleft.

🔴 **The `60.6 %` is not a defect rate**, and quoting it as one would repeat the `p455` error this base already retracted once. A collision is trivial when the name is a dictionary word, and nobody searching for `lumen` is looking for a shelf row. **The risk is a function of the canonical's own adoption**, because adoption is what puts a bare name into a blog post, a README instruction or an agent's tool call:

| canonical adoption | dangerous-class subjects |
|---|--:|
| ≥ `10,000★` | **`3`** |
| ≥ `1,000★` | `6` |
| ≥ `100★` | `18` |
| any | `43` |

**All three `≥10,000★` cases are rows this base sells from**, and the sharpest is its #2: `THU-MAIC/OpenMAIC` is **MIT** (`1,065 B`, `ba2525637432`), while `kolbyzhu5/OpenMAIC` and `ChengZhuo2025/OpenMAIC` are both **AGPL-3.0** with a payload that is byte- *and* hash-identical between them (`34,523 B`, `0d96a4ff68ad`). `HKUDS/DeepTutor` is Apache-2.0 while `rddy/deeptutor` is MIT — the quieter half of the defect, where the grant changes permissive-to-permissive and nothing looks wrong.

🔵 **Two consequences, both actionable.** (1) **Resolve by owner-qualified slug, never by bare name** — and treat a bare name in a dependency manifest, a vendoring script or an agent tool definition as a lint error. (2) **Checking for the word "GPL" catches less than a fifth of the class**; the dominant failure is the *ungranted* repository, which conveys no rights at all and is therefore worse than copyleft, not better. The buildable rule is **P61** in `compose/patterns.md`: pin slug **and** payload digest, and enumerate vendored subtrees — because `OpenMAIC`'s own MIT root sits above an LGPL-3.0-or-later vendored subpackage, so a root-only check passes it and still ships copyleft.

**Confidence: high** for the measurements (one instrument, `gh api search/repositories`, exact-name filtered, controls at both signs). **Confidence: moderate** for the risk ordering, which rests on the claim that high adoption drives name-resolution — plausible and consistent with how the legs themselves returned these repositories (the `github trending education AI 2026` leg named `DeepTutor`, `OpenMAIC` and `ai-engineering-hub` **without owners**), but not directly measured.

## T83 — A verification channel certifies nothing until it has been controlled at both signs 🔴 new at p685

`p684` found that the standing quality bar's `curl -sI` URL check returns `403` in this environment for a real repository **and** for one that does not exist, so it can never fail. p685 reproduced that and then found the **same defect in a channel this base had been treating as authoritative**: `gh api repos/<slug>` returns `403` for every repository here, real or imaginary, because repository access is session-scoped — and the error text is identical in both cases (*"GitHub access to this repository is not enabled for this session"*).

| channel | real repo | real repo, absent file | non-existent repo | discriminates? |
|---|---|---|---|---|
| `curl -sI github.com/<slug>` | `403` | — | `403` | 🔴 **no** |
| `gh api repos/<slug>` | `403` | — | `403` | 🔴 **no** |
| `git ls-remote --symref` | `ref: refs/heads/main` | — | `fatal` | 🟢 **yes** |
| `raw.githubusercontent.com/.../LICENSE` | `200` + bytes | `404` | `404` | 🟡 **partly** |
| `gh api search/repositories` | row + stars + SPDX | — | `total_count 0` | 🟢 **yes** |

🟡 **The `raw` row is the one that changes a protocol rather than just annotating it.** It cannot separate *"live repository, no file at that path"* from *"no such repository"* — both are `404`. So the two-channel procedure this base already follows is not stylistic: **existence must come from `ls-remote` first**, and only then does a `404` from `raw` carry the meaning *"ships no grant at that path."* Reversed, or used alone, `raw` would report a nonexistent repository as one with a missing licence.

🔵 **The transferable rule is about instruments, not about GitHub.** A channel that returns the same answer for a true and a false input has zero information content, and it fails *silently* — every candidate "passes", including invented ones. **Any channel used to certify a row must be run against a negative control in the same pass that relies on it**, because scope rules, proxies and rate limits change underneath a base that is re-run hourly: `gh api repos/<slug>` presumably worked when something started depending on it. 🔴 **And a standing instruction can itself be the defect** — the mandated `curl -sI` check is now in its second pass of being demonstrably inert, and no number of passes "complying" with it would have revealed that.

**Confidence: high.** Every row above was measured at p685 with explicit positive and negative controls, on two tools.


---

## T88 — `NOASSERTION` is not a licence state, it is the absence of a classification — and in education what it hides is a Creative Commons plurality 🔴 new at p686

**This extends T82/T83 and P61 rather than discovering something new in kind.** p685 already recorded that `license.spdx_id` is a classifier's opinion and wrong in both directions. What p686 adds is the **magnitude and the composition**, which change what you do about it.

Of `31` repositories in this pass's candidate pool reported `NOASSERTION`, resolved by reading each grant payload at the real default ref: **`12` permissive and adoptable** (Apache-2.0, MIT, MIT/X, Unlicense), `1` **ECL-2.0** (OSI-approved, Apache-derived), `4` copyleft, **`5` Creative Commons**, `2` split-grant, `2` with **no licence file at all**, and **`1` outright proprietary**.

🔴 **The distribution has no mode you can bet on.** It spans public domain to all-rights-reserved, so **both** default policies are wrong: *unknown → skip* discards `12` adoptable repositories including the only institutional LMS in this industry under a permissive grant (OpenOlat, Apache-2.0) and an eleven-year-old autograding platform (RELATE, MIT/X) this base had never shelved in `686` passes; *unknown → probably fine* adopts a repository whose `LICENSE` reads *"All rights reserved — Source Available — Personal Use"* **while its own GitHub description calls itself open-source**.

🟢 **The education-specific finding is Creative Commons.** `5` of `31`, and `2` of the pool's `3` largest subjects by stars, carry a CC grant — because education repositories are frequently **content wearing a code repository's clothes**. `xiaoyang111222/cn-math-taxonomy` at `6,928★` is a taxonomy; `5mdld/anki-jlpt-decks` at `3,117★` is a deck. **CC cannot license software**, and no amount of package manifest makes it do so. This failure mode is far more common in education than in the other industries this KB covers, and a general-purpose ingest filter will not be looking for it.

🟡 **A single licence cell is also insufficient where the grant is split.** `andymatuschak/orbit` is Apache-2.0 across most of the tree **but `packages/app` and `packages/backend` are AGPL-3.0-or-later or BUSL-1.1** — the deployable halves are precisely the non-permissive ones. A cell reading "Apache-2.0" would be true of the repository and false of anything shippable.

**Confidence: high.** All `31` resolved first-hand at p686 by payload read, with byte counts and digests, and negative controls clean.

---

## T89 — A search index's `422` is not evidence of absence, and it under-reports exactly the largest subjects 🔴 new at p686

`gh api search/repositories` answers `repo:openedx/edx-platform` with **`422 Validation Failed`** — *"the listed users and repositories cannot be searched either because the resources do not exist or you do not have permission to view them"*. The repository is fully alive on the other channel: `ls-remote --symref` resolves **`master`**, and `LICENSE` reads `35,136 B`, `sha256₁₂ e12d78569742`, AGPL-3.0. Three further `422`s at p686 (`patchy631596/awesome-ai-agents`, `open-learning-exchange/treehouses`, `open-resources/open-education`) were re-probed and **none was absent**.

🔴 **The error has a direction, and that is what makes it dangerous.** It does not add noise symmetrically; it **removes** subjects, and it removed the largest open platform in this industry. This is the `p674` search-index-absence condition recurring on a different org, so it is a property of the channel rather than an incident. **A census built on `search/repositories` alone silently under-counts, and its own `total_count 0` looks exactly like a clean negative result.** Every `422` must be re-probed on `ls-remote` before it is recorded as an absence — the rule T83 states in general, applied to the specific instrument this base relies on for stars and grants.

**Confidence: high.** Four instances at p686, each contradicted on an independent channel.

---

## T90 — The strongest new education agents demote the LLM to narrator and take ground truth from a domain solver 🟢 new at p686

Two independent instances arrived in a single pass, in unrelated domains, both permissively licensed:

- [`wimi321/GoAgent`](https://github.com/wimi321/GoAgent) (MIT) wires **KataGo** — a superhuman Go engine — to a multimodal LLM. The engine scores the move; the model explains *why* the score is what it is.
- [`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server) (Apache-2.0) puts **OpenFOAM** behind an MCP surface for CFD teaching with Socratic questioning. The solver computes the field; the model surfaces the gap between it and the student's prediction.

🟢 **Why this matters more than either repository does.** Every tutor on this base's agent shelf asks one model to be **both examiner and explainer**, which is why hallucinated correctness is the sector's standing risk and why academic-integrity demand (**T79**) has no permissive supply behind it. This architecture removes the conflict structurally rather than by prompting: correctness is **decidable** because a solver decides it, and the model is confined to the one task it is reliably good at — narrating a result it did not author. It also degrades honestly: when the solver has no answer, the system can say so, which a single-model tutor cannot.

🟡 **The limit is scope, and it is severe.** It only works where a *checkable oracle exists* — board games, physics, mathematics, code, symbolic algebra. It does not transfer to essay feedback, language production or history, which is most of the curriculum. ⚠️ Both instances are also small and partly dormant (`58★`; `127★`, last push `2026-01-18`), so this is a **pattern worth building**, not a dependency worth adopting — see **P62**.

**Confidence: medium.** The architecture is clearly evidenced and verified first-hand in two instances; its durability is not, and `n = 2`.
