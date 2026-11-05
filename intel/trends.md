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

## T29 — The April 2026 US accessibility deadline is the one named demand driver in this KB with no permissive answer 🟢 new at p656

This base records an **April 2026 ADA deadline for large US public institutions** as a North America demand driver, alongside the state-level activity in T3 and T12. p656 swept for the supply side and the result is negative:

- `topic:accessibility topic:education` returns **442 repositories**. Star-ranked, the permissive rows at the top are `evoluteur/braille-tools` (MIT, 43 ★) and `osunyorg/admin` (MIT, 49 ★) — **neither is a WCAG remediation tool.**
- The production tool is [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) — scans Canvas content for WCAG defects, explains them, fixes many in place, University of Central Florida, 117 ★, pushed 2026-11-04 — and it is 🔴 **GPL-3.0** (35,147 B payload read).
- The authoring tool with accessibility as a design goal, `adaptlearning/adapt_framework` (632 ★), is also 🔴 **GPL-3.0**.
- `screen-reader`, `captioning`, `dyslexia` and `special education` return **zero rows on any shelf** of this KB, before and after this pass.

**Why this is a trend and not merely a gap.** Every other regulatory driver this base tracks — the EU AI Act's Article 50 transparency duty, Korea's high-impact assessment scope, US state model policies — creates demand that *permissive software can serve*. Accessibility is the exception: the mandate is hard, dated and enforceable, and the only real tool forbids a proprietary derivative. 🔵 **The engagement shape is therefore different in kind:** deploy UDOIT inside the client's own estate, bill the remediation work and the integration, and ship no derivative. It is a services engagement, not a product one — and saying that up front is more valuable than discovering it after a proposal has promised a platform. **Confidence: high** on the licence and the supply absence (both measured); **moderate** on the deadline itself, which this KB carries from secondary sources and has not read in primary form.

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
