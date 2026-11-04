---
industry: education
region: Global
updated: 2026-11-04
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

## T6 — Permissive platforms exist in open source education, but only outside the institutional LMS class

🔴 **This entry previously read "open source education has no permissive platform, only permissive components." That was wrong and is withdrawn.** `learningequality/kolibri` is **MIT** (1,097 B payload read 2026-11-04), **1.2k ★ / 1.0k forks**, and a production offline-first learning platform.

Measured across fourteen platform rows: **ten are copyleft** (GPL-3.0: Moodle, Chamilo, ILIAS, Gibbon; AGPL-3.0: Open edX, Frappe LMS, Veo; GPL-2.0: RosarioSIS, openSIS; LGPL-3.0: OpenEduCat), **four are permissive** (MIT: Kolibri, Richie, GegoK12; ECL-2.0: Sakai).

The accurate claim, stated at the width the evidence supports:

- **No permissive platform of the Moodle / Open edX class.** Institutional course management — enrolment at scale, gradebook, SIS integration, large plugin ecosystem, multi-tenant MOOC delivery — is copyleft only. For those engagements the forced architecture is unchanged: **stock platform, permissive agent layer, integrate over REST or MCP**, because modifying an AGPL platform for a managed service pulls network-disclosure obligations onto the service.
- **A permissive platform does exist for offline-first learning delivery**, and it permits a closed derivative. In low-connectivity markets the recommended base changes accordingly.

🔵 **How the error survived several passes, because the mechanism generalises:** each pass enumerated the institutional LMS field, found it uniformly copyleft, and generalised to all of open source education. Kolibri was never in the comparison set, because it is not an institutional LMS — **the question's framing excluded the answer.** When a trend entry claims "there is no X", its strength is bounded by the enumeration behind it, and an enumeration drawn from one product class cannot support a claim about a whole field. **Confidence: high** on the corrected statement (all fourteen licence payloads read byte-for-byte); the previous entry's confidence was high and the entry was still wrong, which is the part worth remembering.

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

## 🔴 What this page does not claim

- ~~**No verified star counts for `richie`, `chamilo-lms` or `sakai`**~~ — 🟢 **closed at p652**: 318, 1.0k and 1.2k respectively, measured from the repository pages on 2026-11-04 after three passes flagged it. `edx-platform` (8.2k), `moodle` (7.6k), `XBlock` (471) and `kolibri` (1.2k) were re-measured in the same batch and **all four reproduce**.
- **No first-hand reading of any primary regulatory text.** The EU Digital Omnibus, the Korean AI Basic Act and the Vietnamese AI law are all carried from legal-practice and secondary summaries. They agree with one another, which is why confidence is high on the dates — but no Commission, MSIT or Vietnamese National Assembly document was fetched. Verify before quoting a clause to a client.
- ~~**No country-level education AI regulation for any Sub-Saharan African state**~~ — 🟢 **resolved at p652 into an accurate statement rather than an absence**: national AI *strategies* with explicit education commitments exist (Kenya's National AI Strategy 2025–2030 commits to AI literacy across primary, secondary and higher-education curricula; Nigeria's digital economy strategy references AI), and education-sector *rules* still do not. South Africa's draft National AI Policy was published 10 April 2026 and withdrawn 27 April 2026. The African Union's own roadmap puts Phase 1 (2025–2026) at strategy-building, so this is where the continent is scheduled to be. 🔴 **Still absent: any published Kenyan AI-literacy framework** implementing the strategy's commitment — a named, unfilled deliverable as of September 2026.
- **The "agentic university" framing** carried by earlier versions of this page rested on a single arXiv preprint. It is a useful taxonomy, not measured adoption, and has been demoted accordingly.
- **No evidence was found of a dominant open source assessment-integrity or proctoring tool.** Given this is the most heavily regulated use case in the sector, the absence of permissive supply is notable and is recorded as a gap rather than a finding. p652 widened the search to general rubric-scoring libraries and found **one** permissive, credible option — `microsoft/LLM-Rubric` (MIT, 45★), which is **not education-specific** — plus `protorubric`, whose payload and README name different licences. **Three passes, two search strategies, same hole**, which makes it a property of the field rather than of the searching.
- 🔴 **One claim was tested at p652 and rejected rather than published:** that **TEQSA requires Australian higher education providers to submit institutional gen-AI action plans.** No submission mandate was found; TEQSA publishes guidance ("Assuring quality learning in a gen AI-integrated future", 24 June 2026), maintains a Gen AI Knowledge Hub, and leans on Threshold Standard 5.2. This is the second consecutive pass whose mandated regional leg produced a valuable *negative* result — the first was the North Carolina SL 2026-41 dates at p651. **The regional leg's job is partly adversarial, and that is now a pattern rather than an anomaly.**
- 🔴 **Five hosts did not resolve in this session at p652** — `www.oecd.org`, `www.unesco.org`, `www.iesalc.unesco.org`, `www.dlapiper.com`, `huggingface.co` — so the OECD recommendations, the Canadian strategy detail and OmniEdu's weight licence rest on secondary sources or are unresolved. The IESALC LATAM figures were independently re-derived from search and reproduce. This is a network-policy ceiling on verification, not a research gap, and it is cheap to lift.
