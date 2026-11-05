---
industry: education
region: Global
updated: 2026-11-05
---

# 📡 Trends — Education

> What is actually changing in AI + education as of November 2026. Each trend names its evidence and its confidence.

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

## T31 — The psychometric measurement layer is permissive, complete, and almost entirely dormant 🟢 new at p657

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

## T32 — Spoken assessment is a layer this KB had never seen at all, and it has a permissive answer that displaces a paid API 🟢 new at p657

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

## T39 — The sector's standard licence shape is permissive code wrapped around unlicensed courseware 🟢 new at p658

`code-dot-org/code-dot-org` states it in one payload: Apache-2.0 for "all source codes and assets", **except** Code.org's artwork, graphics, sounds, lectures, videos, logos, characters and fonts, enumerated in a 4,271 B / 77-line `NOTICE`, which "may not be used or distributed or accessed in any manner other than directly via Code.org's own web site, mobile applications, or social media channels … **without modification or embedding in another format**". The Minecraft assets inside it are **Microsoft's**, and any distribution outside Code.org's own site needs a separate agreement with Microsoft.

This is the same shape p657 found at the OER layer and p656 at the platform layer, and it is the shape that decides education engagements: **the engine is free, the lesson content is not.** A proposal that says "we will build on Code.org" and means "we will ship their courses" is a licence incident waiting to be discovered by the client's counsel.

**Confidence: high** (licence and `NOTICE` both read in full).

## T40 — Scratch is two licences, and which one you touch decides the business model 🟢 new at p658

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

## T39 — This base's absence claims are checked against its shelves and refuted in its logs, and that is now its dominant defect class 🟢 new at p661

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

## T40 — Every "no permissive supply" claim this base has tested has turned out to be an adoption gap instead, and that is now five for five 🟢 new at p661

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

## T31 — A regional "zero" on this base's shelves has twice turned out to be a query-language artefact, and the instrument is the finding 🟢 new at p664

Two regions carried zero placed agent rows on `agents/top.md`. Both closed inside two passes, and neither closed because the sector changed.

| Region | Closed at | Leg that closed it | What the mandated English legs returned |
|---|---|---|---|
| **LATAM** | p663 | **Spanish** | nothing in scope |
| **EMEA** | p664 | **German** — first attempt | nothing in scope, 7th consecutive pass |

The four mandated English-language supply legs have now returned **zero in-scope novel addresses for seven consecutive passes**, and the trending digests have gone **twenty** passes without a yield. In the same window, non-English legs produced `TutorIA`, `Profe Bit`, `EduRAG` and `RUCAI` — every regionally placed row added since p662.

🔵 **The generalisable claim is narrow and worth stating precisely:** English-language search surfaces the *most-starred* education repositories, which are disproportionately American and Chinese, and it does not surface *institutionally-situated* ones, which are where regional placement evidence lives. A base that searches only in English will therefore measure a world in which only APAC and the unplaced global middle build education agents — which is exactly what this base measured for its first ~660 passes.

🔴 **The counter-case that stops this becoming a rule.** **North America now has one placed row against APAC's eight** and its query language is already English. So language is a sufficient explanation for the LATAM and EMEA zeros and **not** a general theory of regional coverage. The North American thinness is unexplained and is registered as an open question in `intel/market.md`, not papered over with this trend.

**Operationally:** run the supply legs in German, French, Spanish and Portuguese as standing practice, and treat a declared regional absence as a statement about the instrument until it has been tested in the region's own language.

## T32 — In LATAM, adoption and licensability are inversely correlated, which makes licence remediation the cheapest intervention available 🔴 new at p664

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
| **2. Appendix capture** | `Opetushallitus/compleap` — the **full** EUPL v1.2 text, `13,956 B` | 🟢 **`EUPL-1.2` — correct** | 🟢 EUPL-1.2 | 🔴 **the *classifier* fails, not the index**: a keyword reader matches `GNU Affero General Public License` **inside the EUPL's compatibility appendix** and returns `AGPL-3.0` |
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
