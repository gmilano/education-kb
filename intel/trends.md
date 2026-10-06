---
industry: education
region: Global
updated: 2026-10-06
---

# Trends — Education, October 2026

## 1. Purpose-built beats general-purpose

The most defining trend of 2026 is the move away from generic AI assistants
toward platforms built specifically for education. Buyers who piloted a general
chatbot in 2024–25 are now replacing it with something that understands
curriculum, mastery and assessment. Consequence for Globant: a thin wrapper over
a frontier API is no longer a differentiated offer; the pedagogy layer is.

## 2. From experimentation to governance

AI in education has shifted from "can we" to "under what policy." Clear policies,
data boundaries and oversight are now preconditions of adoption, not follow-ups.
Ohio required every district to have a written AI policy by July 2026; 134
state-level bills were introduced in the US in 2026; the EU AI Act classifies
educational assessment as high-risk. **The compliance artefact is now part of the
deliverable.** Ship the policy mapping, the audit trail and the oversight gate
with the software.

## 3. Agent-native tutoring architecture is settling

DeepTutor (Apache-2.0, 40.8k★, v1.6.13 on 2026-10-04) shows the shape the
category is converging on:

- a **two-layer plugin model** — single-shot *Tools* the model calls, and
  multi-stage *Capabilities* that take over a whole turn;
- **three entry points** — CLI, WebSocket API and Python SDK, so the same engine
  serves a terminal, a web client and an embedded integration;
- **per-learner workspaces with persistent memory**, personality and an evolving
  skill set, rather than one stateless assistant for everyone.

Copy this decomposition even if you do not use DeepTutor. Memory-per-learner and
the Tool/Capability split are the two decisions that matter.

## 4. MCP has become the LMS integration layer

This is the most practically important shift of the last few months.
`vishalsachdev/canvas-mcp` (MIT) now exposes **up to 102 Canvas tools and 8 agent
skills** — including a 20-check WCAG accessibility scanner and bulk grading —
and works with 40+ MCP clients. `peancor/moodle-mcp-server` (MIT) does the
equivalent for Moodle.

Why it matters beyond convenience: **MCP side-cars keep their permissive
license** while in-tree LMS plugins inherit copyleft. Every in-tree Moodle AI
plugin probed this pass is GPL-3.0; both canonical MCP servers are MIT. The
integration style now determines the IP outcome.

**Refinement from the second pass of 2026-10-06 — and it is a correction of
emphasis.** A side-car is permissive *by the author's choice*, not by
construction. Sweeping every Canvas and Moodle MCP server that surfaces in
search, the shelf is in worse shape than the canonical two suggest:
`DMontgomery40/mcp-canvas-lms` (103★, 54 tools, v2.3.0) and `loyaniu/moodle-mcp`
(38★) carry **no license at all** on any branch or in their READMEs, and
`csmediapro/moodle-mcp-server` is **AGPL-3.0 with a paid premium tier**. Only
four of the seven servers probed are usable, and the most-starred non-canonical
one is not. An unlicensed repo is worse than a copyleft one: AGPL is a constraint
you architect around, no license is all-rights-reserved. **A license probe is now
week-one engagement work, not diligence you defer.** Full table in
`agents/top.md`.

## 5. Framework consolidation — AutoGen is out

`microsoft/autogen` (61.3k★) is in **maintenance mode**: no new features,
community-managed, with the README directing new users to **Microsoft Agent
Framework** (MIT, 14.0k★, Python + .NET). Its `LICENSE` at HEAD is now CC-BY-4.0
rather than plain MIT. Any education proposal still specifying AutoGen should be
re-specified on MAF, smolagents or LangGraph. Earlier cycles of this KB
recommended AutoGen; that recommendation is withdrawn.

## 6. Sovereign and on-prem inference is a requirement, not a preference

EMEA districts with data-residency rules self-host open-weight models (Llama,
Mistral) rather than call commercial APIs. Every major APAC economy has built its
own base model — Sarvam AI, ILMU, Sahabat AI, SEA-LION, HyperCLOVA X Think, NTT
Sarashina. California AB 1159 makes "student data is not used for training" a
legal commitment that must be demonstrable. Ollama (MIT) and vLLM are therefore
infrastructure, not an optimisation.

Note the APAC gap: these are **base models with no education agent layer**.

## 7. Assessment is the regulated frontier — and the tooling gap

AI-driven assessment is named in nearly every forecast as a growth area, and in
nearly every regulation as high-risk. Meanwhile **no permissive open source
auto-grader exists** — searched again this pass, nothing credible found. OATutor
(MIT) supplies something more useful than a grader: Bayesian Knowledge Tracing,
which yields a *defensible, inspectable* mastery estimate, published at CHI '23
with follow-up in PLOS ONE.

The honest position with a client: automate item generation and feedback, keep
scoring human-gated, and use an explainable mastery model where a number has to
be justified.

**Amended in the third pass of 2026-10-06 — the tooling half of this trend is no
longer true as stated.** [Selleo/mentingo](https://github.com/Selleo/mentingo)
(**MIT**, read from payload, 91★) grades open-ended behavioural and
problem-solving answers automatically and returns actionable feedback, and traces
every model call through Langfuse. So a permissive auto-grader exists — for
**corporate L&D**, not for academic assessment, and with no rubric or curriculum
alignment. Three things follow:

1. **The build-vs-adopt answer changed for L&D work.** You no longer start an
   enterprise training grader from scratch.
2. **The compliance answer did not change at all.** Annex III, the Oklahoma and
   Maryland statutes and Korea's high-impact classification are indifferent to
   licence. The human gate on consequential scores stays.
3. **Say both sentences to the client in that order.** A client who hears only
   "an open source auto-grader exists" will hear "we can drop the review step",
   and that is the one misreading of this KB that creates real liability.

## 8. Skills economy and verifiable competency

Real-time skills visibility, adaptive training and competency frameworks gained
ground in 2026, with career-navigation tools spreading across K-12,
post-secondary and workforce contexts. Open Badges tooling
(`1EdTech/openbadges-validator-core`, Apache-2.0) is the permissive
infrastructure for competency claims a third party can verify. Expect corporate
L&D and public workforce programmes to converge on this.

## 9. Offline-first is an equity requirement, not a legacy concern

Kolibri (MIT) — offline-first teaching and learning with no internet — is the
only fully permissive end-to-end platform on the education shelf. Given CEPAL's
findings on LATAM structural gaps and a widening talent gap since 2022, plus
sub-10% institutional readiness in a region where over half of Chilean and
Brazilian teachers already use AI personally, offline-capable and low-cost is
where the volume is.

## 10. Human connection is becoming the measured outcome

As AI becomes commonplace, human-driven indicators — engagement, well-being,
sustained participation — are becoming *more* important, not less. Practical
effect: instrument for retention and participation, not just for correctness and
completion. A tutoring deployment that improves completion while reducing
sustained participation is a failure that only shows up if you measure it.

## 11. Agent-specific governance has arrived, and a regulator wrote it first

Until 2026, education AI governance was general AI rules applied to education by
analogy. That changed: **Singapore's IMDA published the world's first Model AI
Governance Framework for Agentic AI** at Davos in January 2026, updated in June
2026 — a framework that governs autonomous planning, reasoning and action
directly. Its four dimensions read as a build checklist:

1. **bound the agent upfront** — pick appropriate agentic use cases and place
   explicit limits on the agent's powers;
2. **make humans meaningfully accountable** — define which checkpoints require
   human approval (note *meaningfully*: a rubber-stamp approval does not count);
3. **technical controls across the whole agent lifecycle**, not just at launch;
4. **enable end-user responsibility** through transparency and **training** — the
   framework explicitly expects users of workflow-assisting agents to be taught
   capabilities, common failure points and risks.

Two consequences. First, dimension 4 makes teacher and student enablement a
*compliance artefact*, which means it is fundable rather than discretionary.
Second, a system designed to this framework largely satisfies EU Annex III, the
Oklahoma/Maryland human-oversight statutes and Korea's high-impact
classification at the same time — so use it as the cross-region checklist even on
engagements nowhere near Singapore.

The binding-regulation wave is also wider than this KB recorded: **Korea's AI
Framework Act took effect 22 January 2026** and **Vietnam's dedicated AI law
(No. 134/2025/QH15) on 1 March 2026**.

## 12. Agent Skills are becoming the distribution format for pedagogy

The interesting packaging unit is shifting from "a tutoring app" to "a skill an
agent can load." `vishalsachdev/canvas-mcp` (MIT) ships **8 agent skills**
alongside its 103 tools. `JuneYaooo/lineage-skill` (Apache-2.0, 448★ — the
highest-starred project on the `education-ai` topic) exists only to produce them:
it distils videos, PDFs, transcripts and notes into **source-backed teacher Agent
Skills**, preserving source attribution, extracting the instructor's methodology
and ordering practice tasks progressively.

**Measured in the third pass of 2026-10-06, and it is now the majority shape.**
The `ai-tutor` topic sweep returned a skills cluster that no earlier pass had seen,
all MIT, all read from payload: **universal-examprep-skill (300★)** with
cross-session memory and citation-sourced answers; **algo-sensei (285★)** for
DSA mentoring; **universal-diagnostic-tutor-skill (238★)**, diagnosis-first for
STEM and CS; **kaogong-skill (156★)** with authority citations for Chinese
civil-service exams; **flysheep-ai/education-skills (106★)**, the first skill
**pack** rather than a single skill; plus feynman-tutor, anything-to-course and
Scientific-learning-skills. Of the 17 permissive projects added this pass, **eight
are skills and only nine are applications.**

Three signals worth separating out:

- **A pack is emerging as the distribution unit above the skill.** `education-skills`
  bundles teaching-and-learning skills as a collection — the shape an institution
  would actually publish, and the shape a studio would actually sell.
- **Citations and cross-session memory are the differentiators, not the prompt.**
  The two highest-starred skills both carry provenance (citation-sourced,
  authority citations) and one carries memory across sessions. That is exactly what
  the high-risk regimes ask for, arrived at by the market rather than by the
  regulator.
- **Diagnosis-first is the pedagogically strongest pattern on the shelf.**
  `universal-diagnostic-tutor-skill` and `Scientific-learning-skills` both establish
  the misconception before explaining, and `feynman-tutor` inverts the roles so the
  learner teaches the AI. These reach for what OATutor's Bayesian Knowledge Tracing
  does, without the statistical machinery — cheaper to build, weaker to defend.
  Use the skill shape for formative work and the BKT shape where a number must be
  justified.

Why this matters commercially: a skill is portable across the 40+ clients that
speak MCP, which makes an institution's *pedagogy* — its methodology, its
sequencing, its worked examples — the reusable asset rather than the application
wrapped around it. Source-backed matters just as much: a skill that carries
provenance back to the instructor's own materials is defensible in a way a
fine-tune is not, and provenance is what the high-risk regimes ask for. Expect
"turn our course into agent skills" to become a recognisable engagement shape.

## 13. Curriculum mandates have become the demand driver — and they specify the architecture

New in the third pass of 2026-10-06, and the most actionable trend added today.
Two jurisdictions have moved past guidance to **compulsory AI instruction with
published specifics**:

- **UAE** — Cabinet decision **May 2025**, mandatory AI from **Kindergarten (age 4)
  to Grade 12**, from the **2025–26 academic year**, delivered **inside an existing
  subject** (Computing, Creative Design and Innovation) **without extending school
  hours**, by **specially trained teachers**, across **seven areas**: foundational
  concepts, data and algorithms, software use, ethical awareness, real-world
  applications, innovation and project design, and policies and community
  engagement.
- **China, at provincial level** — **Beijing**: at least **8 hours of AI lessons a
  year** in every primary and secondary school from **1 September 2025**, compulsory
  from age six. **Guangdong**: **6 hours a year** in lower grades rising to **one
  hour a fortnight in grades 10 and 11**. The sequence runs from voice-recognition
  basics through machine learning and **misinformation detection** to applied
  projects.

**Why this is a different kind of trend from trend 2 (governance).** Governance
constrains how you deploy. A mandate **creates a budgeted obligation to deliver
content and train teachers** — it is a procurement trigger, not a compliance cost.
The UAE design makes that explicit: the material goes inside an existing subject
with no extra hours, so what is being bought is **integrated curriculum content and
teacher enablement**, which is services work, not a licence sale.

**And the mandates hand you the two hardest design requirements as inputs.** Beijing
**bars primary-school pupils from independent generative-AI use** and **prohibits
teachers from substituting AI for their core instructional duties.** Those are not
policy footnotes; they are system requirements:

- **age-gated capability** — younger cohorts get teacher-mediated AI only, enforced
  by the system and not by guidance;
- **enforced teacher-in-the-loop** — the teacher's role is structurally protected,
  not advisory.

This is the strictest formulation of human oversight anywhere in this KB, and it is
therefore the most useful one to build to: **a design that satisfies Beijing
satisfies EU Annex III, the Oklahoma and Maryland statutes, Korea's high-impact
classification and Singapore's agentic framework.** Note also that two of the UAE's
seven areas — ethical awareness, and policies and community engagement — are
governance and civics rather than technique, so a curriculum pipeline must produce
**age-appropriate ethics and policy material**, not only exercises. Pattern P9 in
`compose/patterns.md` builds to all of it.

## 14. The permissive shelf stopped being thin, so the differentiator moved

Three passes on 2026-10-06 took the permissive education open source layer from
"DeepTutor plus fragments" to roughly **30 verified projects**, including a full
**MIT** AI-native LMS (Mentingo), a 506★ MCP server, a local-first adaptive
workspace with FSRS and a knowledge graph (OpenTutor), and a skills cluster at
100–300★. Earlier passes of this KB described the AI layer as thin and the platform
layer as copyleft, and concluded that the defensible position was the permissive
side-car. **The side-car conclusion survives; the "thin layer" premise does not.**

What changes in the pitch: the scarce thing is no longer *knowing which repos
exist* — a client can read a listicle. The scarce things are now

1. **composition** — wiring a specific set of these parts into something that
   serves one institution's pedagogy;
2. **licence diligence** — this pass alone rejected six projects totalling 963★ for
   AGPL, GPL or no licence at all, including two whose only licence statement was
   unenforceable prose;
3. **governance** — the audit trail, the oversight gate, the age gating, the
   provenance.

None of the three is available off a shelf, and all three are services.

## 15. Permissive is a bigger set than "MIT, Apache, BSD" — and open core hides inside directories

A practical trend with a direct commercial cost, measured this pass.

**The allowlist is wrong if it has three names on it.** The education shelf depends
on at least six permissive licences: MIT, Apache-2.0, BSD, **ECL-2.0** (the
Apache-2.0 text with the patent grant narrowed to education — Sakai, Opencast and
Kuali Rice all use it), **the PostgreSQL License** (pgvector), and ISC. A filter
that string-matches `MIT|Apache|BSD` rejects **four genuinely permissive
higher-education components**. Fix the filter, not the finding.

**And a repo-level licence is no longer a sufficient reading.**
`langfuse/langfuse` is MIT *except* its `ee/`, `web/src/ee/` and `worker/src/ee/`
directories, which carry a separate enterprise licence — a **by-directory**
carve-out that no badge can express. Its copyright line now reads **ClickHouse,
Inc.**, so the holder changed between passes while the licence string did not. Two
additions to the probe discipline: read the carve-out **paths**, and record the
**copyright holder** alongside the licence so a change of ownership is visible next
pass.

**The flip side, and the harder lesson, is about withdrawals.** Everything above
guards against a false positive. The second pass of 2026-10-06 produced the
opposite error: it withdrew this KB's OpenTutor entry after probing
`tutornew/OpenTutor` (8★, unlicensed) when the real project was
`zijinz456/OpenTutor` (**MIT, 130★, FSRS 4.5, 12 blocks, LOOM knowledge graph**).
A 404 or an unlicensed verdict is evidence about **one owner's repository**, never
about a project. **A withdrawal needs a stronger probe than an addition**, because
a wrong addition wastes a probe and a wrong withdrawal destroys knowledge and is
believed.

## 16. US state law has converged on one testable rule: human judgment is final

Fifteen trends in, the single most useful thing about the 134 AI-in-education bills
across 31 US states is **how little they disagree on the core requirement.** Read
by mechanism rather than by state, the 2026 statutes converge on a sentence you can
build against:

| State | Instrument | The operative requirement |
|---|---|---|
| Idaho | **SB 1227**, Generative AI in Education Act | statutory test: **"human judgment remains the final authority"**; AI may not replace human teachers |
| Oklahoma | **SB 1734** | AI only **under educator supervision with human review**; barred from high-stakes decisions; **annual parent disclosure** |
| Maryland | **AI Ready Schools Act** | human oversight; all **24** districts adopt aligned policies within **120 days** of MSDE guidance |
| Ohio | **HB 96** (2025–27 budget) | first state to **mandate** a written district AI policy — deadline **1 July 2026, now passed** |
| California | **AB 1159** (CALPIPA, signed 10 Sep 2026) | **identifiable student data may not train generative AI**; higher-ed provisions from **1 July 2027** |

**Why this is a trend and not a list.** Four different legislatures, drafting
independently, landed on **teacher-in-the-loop plus no-high-stakes-automation** —
the *same* requirement the EU AI Act imposes on Annex III education systems, the
*same* one Beijing enforces by barring primary pupils from independent generative-AI
use, and the *same* one trend 7 identifies as the regulated frontier. **A single
oversight architecture now satisfies the EU, five-plus US states and China.** That
is the strongest reuse argument in this KB: build the gate once, sell it in every
region.

**And the statutes are buying more than compliance.** Idaho mandates **AI literacy
standards and educator training**; Oklahoma requires **annual parent disclosure**;
Ohio's districts are **past** their policy deadline and therefore in the
implement-and-audit phase. These are **enablement and recurring-reporting lines**,
not one-off policy documents — the same shape as the UAE's teacher-training mandate
in trend 13.

**What to build, concretely.** The gate is the product:
`WAITING_REVIEW`-style approval before any graded or published artefact, an
immutable evidence trail per decision, cohort-based capability tiering, and a
disclosure report generator. [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent)
(MIT) is the **only permissive reference implementation** of that shape this KB has
found — 0★ and unproven, so read it and re-implement rather than pin it. Pattern
P11 assembles the production version.

## 17. The EU compliance clock moved, and the near-term deliverable is labelling

**Added in the fifth pass of 2026-10-06. This supersedes the August 2026 dates
used in trend 2 and pattern P4.**

**Regulation (EU) 2026/1744** — the *Digital Omnibus on AI* — amends the AI Act.
Parliament approval **16 June 2026**, Council adoption **29 June 2026**, signature
**8 July 2026**, Official Journal **24 July 2026**, in force **27 July 2026**.
CELEX **32026R1744**.

| Obligation | Was | Now |
|---|---|---|
| Annex III stand-alone high-risk — **education**: admission and access, evaluation of learning outcomes, student level placement, exam or behaviour monitoring | 2 Aug 2026 | **2 Dec 2027** |
| Annex I embedded high-risk | 2 Aug 2027 | **2 Aug 2028** |
| **Article 50 transparency**, incl. **watermarking / synthetic-content marking** | 2 Dec 2026 | **unchanged** |

The industry read this as a reprieve. It is not, quite. The **heavy** work moved
— technical documentation, conformity assessment, CE marking, EU-database
registration. The **transparency** work did not, and its deadline is **2 December
2026**: disclose that a learner is talking to an AI system, and mark
AI-generated content. For an education deployment that means labelling every
generated lesson, item and piece of feedback.

**So the trend is a sequencing inversion.** Through 2026 the assumption was:
conformity first, transparency as a detail inside it. From now to December 2027
it is the reverse — **labelling and classification are the live obligations, and
conformity is the planned programme.** The deferral is also explicitly not a
holiday: classifying systems against Annex III and Annex I, and beginning
compliance planning, is immediate.

The clients in the worst position are the ones who heard "delayed" and stopped:
unlabelled, unclassified, and 14 months from a conformity deadline they have not
started scoping.

**Sourcing caveat.** EUR-Lex and the Commission's own notice are unreachable from
this environment (egress denied). Every date above is corroborated across several
independent legal and compliance-vendor analyses, and the CELEX id is given for
one-step verification. **Verify against EUR-Lex before this goes into a client
deliverable.**

## 18. Pedagogy evaluation is published as research and licensed as content

**Added in the fifth pass of 2026-10-06.** The fourth pass found one instrument
claiming MIT in a peer-reviewed paper with no `LICENSE` payload and called it a
licence failure mode. Searching for an alternative revealed that **this is how the
entire subfield licenses**:

| Instrument | Venue | Claimed | `LICENSE` payload |
|---|---|---|---|
| [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) (ETH Zurich LRE, 43★, 14 forks) | EMNLP 2025 oral | README badge **CC BY 4.0**; README body **CC BY-SA 4.0** — *same file* | **none** (10 filenames probed) |
| [kaushal0494/AITutor-EvalKit](https://github.com/kaushal0494/AITutor-EvalKit) | EACL 2026 | MIT, stated in the paper | **none** |
| [kaushal0494/UnifyingAITutorEvaluation](https://github.com/kaushal0494/UnifyingAITutorEvaluation) | NAACL 2025 | not stated | **none** |
| Open TutorAI (arXiv 2602.07176) | arXiv | "open source" | **CC BY-NC-SA 4.0** |

Four instruments for measuring whether a tutor *teaches well* — the one
capability an education client actually buys — and **not one permissive software
licence among them.**

**Why this is structural rather than accidental.** These come from education and
NLP research groups, where the publishing norm is Creative Commons for artefacts
and papers. CC licences govern *content*; they were never designed to grant the
rights a delivery team needs over *code*. The subfield is behaving normally for
research and anomalously for software, and the mismatch lands on whoever tries to
ship.

**A fifth failure mode, and the nastiest: the licence that contradicts itself
inside one file.** MathTutorBench's badge says CC BY 4.0 and its footer says
CC BY-SA 4.0, with no payload behind either. A reviewer who checks the badge
clears it; a reviewer who reads to the bottom flags ShareAlike; a reviewer who
probes the payload finds nothing. All three are reading the same commit.

**What to do.** MathTutorBench is also the best of the four — 7 tasks across 3
skills (problem solving, Socratic questioning, solution correctness, mistake
location, mistake correction, scaffolding generation, pedagogy following), a
**1.5B pedagogical reward model** scoring generated teacher utterances against
ground truth, and a 20+ model leaderboard. **Read the task design, re-implement
the harness, vendor none of them, and file a `LICENSE` issue on all three
unlicensed repositories.** For model *selection* — a different question —
[`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
is MIT and usable today.

## 19. The compliance toolchain commoditised; the education profile did not

**Added in the fifth pass of 2026-10-06.** This KB recorded "no open source EU AI
Act compliance toolkit" four times and implied each time that the work was a
build from scratch. It is not, any longer:

| Repo | Licence (payload) | What it already carries |
|---|---|---|
| [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) | **MIT** | Six-tier risk classifier over the Act's decision tree; **61 conformity checklist items** across risk management, data governance, documentation and human oversight; **8 document templates**; CLI, zero-dependency TypeScript SDK, client-only web UI |
| [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) | **Apache-2.0** | ETH Zurich: a technical interpretation of the Act plus a generative-model benchmarking suite — the measurement half |

**Neither mentions education, or Annex III point 3.** So the generic layer
commoditised while the vertical layer stayed empty, which is the same shape
trend 14 identified on the agent shelf: *the permissive base is no longer the
scarce thing, and the differentiator moved up the stack.*

**The missing artefact is small and specific:** Annex III point 3's four education
categories — admission and access, evaluation of learning outcomes, student level
placement, exam or behaviour monitoring — mapped onto the 61 checklist items a
school, university or edtech vendor actually has to evidence. That is a
**profile on an MIT base**, contributable upstream, and it is days of work.
Pattern **P13**.

## 20. Voice became a permissive capability — while its two best-known assets relicensed away

Added sixth pass, 2026-10-06.

Spoken interaction has been the one education capability that forced a
proprietary dependency. Oral practice, pronunciation feedback, role-play,
accessibility for pre-literate and low-literacy learners — all of it routed to a
paid speech API, which in turn meant per-token cost, a connectivity requirement
and student audio leaving the institution. **That is no longer true, and the
reason is one component.**

[k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) — **Apache-2.0,
15.1k★, 2,092 commits** — provides speech-to-text, text-to-speech, speaker
diarization and voice-activity detection **in a single permissive tree that runs
with no Internet connection** on Android, iOS, HarmonyOS, Raspberry Pi, RISC-V and
x86. Four capabilities, one licence, embedded-class hardware.

**The same trend has a trap inside it, and it caught the obvious choice.** The
best-known offline TTS in education and accessibility is Piper — adopted by Home
Assistant and NVDA, fast on a Pi 4. [rhasspy/piper](https://github.com/rhasspy/piper)
is **MIT** and has been **archived read-only since 2025-10-06**; development moved
to [OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl), which is
**GPL-3.0**. **The permissive version is frozen and the maintained version is
copyleft.** Separately, Coqui TTS — 46.1k★, MPL-2.0 — is **unmaintained upstream**
after the company wound down, while the [Idiap fork](https://github.com/idiap/coqui-ai-TTS)
at 2.3k★ carries **5,309 commits against the original's 4,668**. And
**SeamlessM4T**, the first result for "open source multilingual speech", is
**CC BY-NC-4.0** — unusable in billable work.

**What this means for how the shelf is read.** On an immature shelf, stars find
the live projects. On this one they point at a frozen repository, an abandoned
one, and a non-commercial licence. **The fields that carry the signal are archive
status, the successor notice and the commit count on the fork** — and the fork
with 5% of the stars is the one to depend on.

**The commercial consequence** is that voice moves from a line item with a
recurring per-token cost to a one-off build on hardware the client already owns.
That reprices every spoken-practice and oral-assessment proposal, and it is the
component that completes the offline-first pattern (**P18**).

## 21. Mother-tongue AI is a three-region capability — and the two-region version of this trend was wrong

Added sixth pass, 2026-10-06. **Revised in the seventh pass of 2026-10-06: the
headline claim was "two regions" and it is false.** ASEAN has a permissive,
self-hostable language layer in **five languages across four countries**, found
by searching in Bahasa, Thai and Vietnamese rather than in English:

| Repo | Licence (payload) | ★ / commits | Country |
|---|---|---|---|
| [undertheseanlp/underthesea](https://github.com/undertheseanlp/underthesea) | **Apache-2.0** | **1.8k** / 1,276 | Vietnam |
| [PyThaiNLP/pythainlp](https://github.com/PyThaiNLP/pythainlp) | **Apache-2.0** | **1.2k** / **6,649** | Thailand |
| [malaysia-ai/malaya](https://github.com/malaysia-ai/malaya) | **MIT** | 530 / 961 | Malaysia |
| [IndoNLP/nusa-crowd](https://github.com/IndoNLP/nusa-crowd) | **Apache-2.0** | 292 / 992 | Indonesia |
| [malaysia-ai/malaya-speech](https://github.com/malaysia-ai/malaya-speech) | **MIT** | 291 / 755 | Malaysia |

**Why the sixth pass got it wrong, because the error is reusable.** It asked
which languages have a permissive layer and went looking for **sovereign
models** — found SEA-LION, correctly established it has no repository-level
grant, and recorded the region as empty. But what makes a Thai tutor possible is
not a sovereign LLM, it is a **tokenizer**: Thai has no spaces between words.
**The gap was an artefact of the noun, not of the region.** Three regional gaps
in this KB have now been refuted by changing the channel, the layer and the noun
— and none by searching the original channel harder.

**Two qualifications that keep this honest.** None of the ASEAN shelf is
education-specific — like AI4Bharat, these are general toolkits that make a
mother-tongue tutor possible without making one. And only **one** of them covers
speech (`malaya-speech`), so spoken practice in Thai, Vietnamese and Indonesian
routes through the general shelf (`sherpa-onnx`, Whisper) and must be
accuracy-tested per language rather than assumed.

**What survives of the original trend, and it is still the commercially useful
part:** most of the world's teaching languages still have no permissive
self-hostable layer, the gap is a differentiator rather than a disqualifier, and
corpus-building is fundable first-phase work that ministries and development
funders pay for directly. The count moved from two regions to three. The argument
did not change.

**Original sixth-pass text follows, retained so the correction is legible.**

"Multilingual" in education AI usually means the handful of languages a frontier
model happens to serve well. Asked instead **which teaching languages have a
permissive, self-hostable layer**, the honest answer is narrow and uneven.

**Where it exists:**

- **India — broad, MIT, one institution.** AI4Bharat (IIT Madras) ships
  translation across **all 22 scheduled Indian languages**
  ([IndicTrans2](https://github.com/AI4Bharat/IndicTrans2)), TTS in **13**
  ([Indic-TTS](https://github.com/AI4Bharat/Indic-TTS)), ASR pretrained on **40**
  ([IndicWav2Vec](https://github.com/AI4Bharat/IndicWav2Vec)), and the annotation
  platform to curate it all ([Shoonya](https://github.com/AI4Bharat/Shoonya)) —
  **every one MIT**. Paired with Sunbird (MIT), a full national stack is
  permissive end to end (**P16**).
- **Uganda and Africa — small, Apache-2.0/MIT, and better than it looks.**
  [SunbirdAI/salt](https://github.com/SunbirdAI/salt) (**Apache-2.0**) ships
  translation, ASR and **studio-recorded TTS by professional voice actors** across
  Luganda, Swahili, Ateso, Lugbara, Acholi and Runyankole;
  [masakhane-mt](https://github.com/masakhane-io/masakhane-mt) (**MIT**) carries
  continental MT from a 1,000-participant, 30-country community.
- **Portuguese — permissive, but it moved.** Tucano (Apache-2.0, peer-reviewed in
  *Patterns*) was Brazil-origin and is **archived since 2026-02-24**; **Tucano 2**
  continues under the **University of Bonn** [Polygl0t](https://github.com/Polygl0t/Polygl0t)
  initiative (Apache-2.0).

**Where it does not exist:** essentially everywhere else. Most of the world's
teaching languages have **no permissive, self-hostable speech or translation
layer** — and in ASEAN the nearest thing,
[SEA-LION](https://github.com/aisingapore/sea-lion), **has no repository-level
licence at all**: its grant is deferred to each HuggingFace model card because
terms vary with the base model, so "SEA-LION is MIT" is not a sentence anyone can
truthfully say.

**Three consequences for how engagements are scoped.**

1. **Check the language before promising the capability.** Mother-tongue delivery
   is deliverable from the shelf in two regions. Elsewhere the honest scope begins
   with **data collection**, and SALT is the worked example of doing that
   properly — six languages, studio recordings, two peer-reviewed papers,
   Apache-2.0.
2. **The gap is the differentiator, not the disqualifier.** A client whose
   language has no permissive layer has no off-the-shelf competitor either.
   Building the corpus is a defensible, fundable first phase — and it is the kind
   of work ministries and development funders pay for directly.
3. **Licence review in APAC is per checkpoint and recurring.** Where the grant
   lives on the model card, it must be re-read every time the checkpoint changes.
   Budget it as a standing task, not a one-time gate.

**And the sharpest instance of the gap is an application, not a language.** Oral
reading fluency — the highest-volume literacy measurement in primary education —
has **no permissive implementation anywhere**: FLORA, Literably, Amplify Text
Reading Online and SoapBox Labs are all closed, with no public repository. The
components are all now permissive and shelved, and a **public dataset with a
published accuracy baseline** exists (Ghana ORF Dataset; Whisper V2 at 10.3% WER,
*IJAIED* [10.1007/s40593-024-00435-9](https://doi.org/10.1007/s40593-024-00435-9)).
That is an open category with no open competitor — wired up as **P17**.

## 22. Regulation has started pricing the *corpus*, not just the decision

Added seventh pass, 2026-10-06.

Every education-AI compliance regime this KB has tracked regulates by the
**decision an AI makes about a learner**. EU AI Act **Annex III point 3**:
admission and access, evaluation of learning outcomes, level placement, exam or
behaviour monitoring. The Oklahoma and Maryland statutes: human judgment must be
final on consequential decisions. Korea's AI Framework Act: high-impact systems
need oversight and documentation. All decision-shaped.

**Vietnam has added a second axis, and it regulates the tutor by where its
content came from.**

**Decree 33**, signed **2026-06-30**, in force **2026-08-15**, implements Law No.
134/2025/QH15 and lists **46 high-risk AI systems** across six sectors. Three are
in education:

1. AI providing **self-learning content from uncontrolled data sources**
2. AI that **automatically evaluates results and ranks learners**
3. AI that **monitors and analyses learner behaviour using biometric data**

Categories 2 and 3 are Annex III in different words. **Category 1 has no
European equivalent, and it is the one that reaches the default architecture in
this KB.** An AI that generates self-study material from an uncurated corpus is
high-risk *even when it makes no decision about any learner at all*. A RAG tutor
that only ever explains things — no grading, no ranking, no monitoring — is in
scope in Vietnam on **corpus provenance alone**.

Obligations: report the risk level to the **Ministry of Science and Technology
before use**; **conformity assessment** before deployment and maintained
throughout; designated systems assessed by a **registered or recognised body**,
others **self-assessed** by the provider. Transition: education systems already
operating — grouped with healthcare and banking — have until **2027-09-01**;
everything else high-risk until **2027-03-01**.

**Three consequences.**

- **The ingestion pipeline becomes a compliance artefact.** Pattern **P2**
  (curriculum ingestion → item bank) and every RAG tutor on the shelf need a
  **source manifest** — what was ingested, from where, under what rights, reviewed
  by whom — not as good practice but as the evidence a conformity assessment
  consumes. This is the same gate `microsoft/shiksha-copilot` built as a human
  curator step and `CurriculumCraft-AI` argued for with synthetic generation; both
  now have a regulator asking for it. Wired up as **P20**.
- **One trigger is narrower than the EU's, and that is worth money.** Vietnam
  qualifies behaviour monitoring to **biometric** data. Non-biometric engagement
  analytics — time on task, attempt counts, mastery curves — sit **outside**
  category 3, where the EU's "behaviour monitoring" arguably captures them.
  Analytics-heavy products can be scoped more aggressively in Vietnam than in the
  EU, which is the first instance in this KB of an APAC regime being *looser* than
  Annex III on a specific axis.
- **"Curated corpus" stops being a quality claim and becomes a licence to
  operate.** The commercial read: in Vietnam the defensible tutor is the one that
  can name its sources. That favours exactly the curriculum-aligned, ministry-
  reviewed ingestion shape this KB already recommends, and it disfavours the
  general-purpose "upload anything" assistant.

**Provenance caveat, and it matters here more than anywhere else in this file.**
Every legal-publisher domain carrying Decree 33 is **EGRESS_BLOCKED** in this
environment — `allenandgledhill.com`, `vietnam-briefing.com`, `vietnamnews.vn`,
`thuvienphapluat.vn`, `vietanlaw.com` and `ed.events`, **6/6 refused** — so **the
primary text was not read.** The three education categories come from **two
independently-phrased searches whose summaries agreed on all three**, across five
secondary outlets; the **biometric** qualifier on category 3 appeared in only one
of the two. **Verify against the decree before this reaches a client
deliverable**, and treat the biometric narrowing as the least-confirmed element.

## Regional notes where the trend diverges

- **North America:** adoption is broad (60% of K-12 teachers) and the binding
  constraint is policy and procurement, not willingness.
- **EMEA:** the AI Act's general application is **already live (2 August 2026)**;
  what is deferred is the high-risk set (Annex III stand-alone to 2 December 2027,
  embedded to 2 August 2028). The trend is pre-emptive compliance architecture, and
  the sequencing institutions actually use is admin and teacher support first,
  assessment last. The region is $2.64B in 2026 and the K-12 integration leaders
  are Finland, Estonia and the Netherlands — small digitally mature states, not the
  large economies. Africa is in this bucket and is greenfield.
- **EMEA, third pass:** Europe is **$2.64B (2026) → $8.0B (2030) at 31.9% CAGR** —
  *slower* than the 41.5% global rate, so it is the compliance-depth market rather
  than the growth market. **Middle East & Africa is sized at last: $0.56B (2026) →
  $1.6B (2030), 34.3% CAGR**, though a second source puts the UAE alone at $7.4M
  (2024) → $21M (2029), so quote MEA as a range. MEA runs on **strategies, not
  statutes** — Saudi Arabia, the UAE, Egypt, Nigeria, Kenya, Rwanda, Morocco and
  South Africa all have national AI strategies and none has a binding AI law — and
  the **UAE's compulsory KG→Grade 12 AI curriculum** is the region's clearest
  procurement trigger.
- **APAC, third pass:** the regional shelf is the **strongest** permissive shelf in
  this KB, not the weakest — StudyMate (MIT, 624★), kaogong-skill (MIT, 156★),
  feifei-companion (Apache-2.0, 105★) and AI_Tutor_Release (MIT, 57★, aligned to
  the Chinese grade 1–9 curriculum) are all China-origin, and DeepTutor is Hong
  Kong. What is genuinely absent is an education layer on a **sovereign** model, and
  any India-, Japan-, Korea- or ASEAN-origin permissive education project at all.
  Scale: **~530M K-12 students in Asia**; adoption 65–75% (2025) → 80–90% (2026).
  Law per country: Korea 22 Jan 2026, **Vietnam 1 Mar 2026 (SEA's first)**, Japan
  deliberately voluntary, **India and Australia with no national framework in
  force**.
- **LATAM, third pass:** **87% of institutions use AI, 26% have a formal AI
  strategy**; **72% of faculty are positive about AI against 57% globally.** An
  enthusiasm-rich, governance-poor market — the easiest region in this KB to sell
  governance into and the hardest to sell adoption into. **Uruguay is the first
  LATAM signatory of the Council of Europe's AI Framework Convention (2025)**,
  which makes it the cheapest bridgehead for reusing EMEA compliance artefacts in
  the region.
- **APAC:** sovereign models everywhere; an education agent layer nowhere — and
  now sovereign *inferencing platforms* too, so the hosting gap is closing while
  the pedagogy gap stays open. Singapore leads on agentic governance, Korea
  (22 Jan 2026) and Vietnam (1 Mar 2026) on binding law. ANZ
  diverges from the rest of the region — higher public support for banning AI in
  schools, where Asian markets surveyed show lower support for bans.
- **LATAM:** the trend is teacher-led, bottom-up adoption outrunning institutional
  governance by a wide margin — now quantified for higher education: **92% of
  students and 79% of faculty** actively using AI, **94% of faculty** expecting to,
  while **88% of faculty report only minimal-to-moderate engagement**. Adoption is
  done; depth is not. UNESCO's LAC Observatory (14 April 2026) is the top-down
  counterweight now forming, and Colombia's funded CONPES 4144 programme shows the
  regulatory map fragmenting country by country rather than converging.

## Declared gaps this pass

**Updated in the fifth pass of 2026-10-06. Read this block first — it supersedes
the fourth-pass block that follows it.**

Channel new to this KB this pass: **institution-first search** (funding body,
ministry, university and research-group names, English and Spanish, not ordered by
stars). **Six gaps changed state, three of them refuted outright.**

- **REFUTED: "no India-origin permissive education project."**
  [microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot) —
  **MIT, 9★, 12 forks, 149 commits** — Microsoft Research India's VELLM
  initiative, validated in classrooms with the **Sikshana Foundation**.
  Teacher-side: curriculum → lesson plans, examples, analogies, activities and
  assessments → DOCX/PPT/handouts, plus multi-chapter question banks against
  blueprint formats, with a **human-curator gate** on textbook ingestion. Plus
  [Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI)
  (MIT, 0★, **CBSE/NCERT grades 9–12 on open-weight Gemma only**).
- **REFUTED and reframed: "no ASEAN-origin permissive education project."**
  [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) —
  **MIT, 158★, 78 forks, 15,802 commits**, NUS-origin, "currently supported by the
  AI Centre for Educational Technologies." **What is actually missing is ASEAN's
  agent layer:** AICET's Codaveri (30,000+ feedback items), Softmark (70,000+
  scripts in 2025) and ScholAIstic run at Singapore Ministry-of-Education scale
  and are **all closed source**. The substrate is permissive; the products are
  not.
- **REFUTED on existence, confirmed on substance: "no LATAM-origin permissive
  education project — the firmest finding in this KB."**
  [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) — **MIT**, Universidad
  Tecnológica de Pereira, Sirius research group, Colombia, funded under
  **SNCTI** — specifies an Open edX side-car tutor for rural higher education in
  Risaralda, with a named pedagogical director. It has **4 commits and every code
  path in its own documented tree returns 404.** **The LATAM gap is a delivery-capacity
  gap, not an interest gap**, and a Colombian public university has
  independently specified **this KB's pattern P1**. Partnership lead; never a fork
  point.
- **RE-SIZED, much smaller: "no open source EU AI Act compliance toolkit specific
  to education."** The generic toolkit exists and is **MIT** —
  [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit)
  (six risk tiers, **61 conformity checklist items**, 8 document templates, CLI +
  SDK + client-only UI) — alongside Apache-2.0
  [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) from ETH Zurich.
  Neither mentions education or **Annex III point 3**. The gap is now an
  **education profile on an MIT base**: days of work, upstream-contributable.
  Trend 19, pattern **P13**.
- **STILL OPEN, and now structural rather than accidental: no shippable permissive
  evaluator of tutoring quality.** All four published instruments are licensed as
  *content*, not software: MathTutorBench (**CC BY 4.0 badge vs CC BY-SA 4.0 body,
  same file, no payload**), AITutor-EvalKit (MIT in the paper, no payload),
  UnifyingAITutorEvaluation (no payload), Open TutorAI (CC BY-NC-SA). See trend
  18. Re-implement; vendor none.
- **STILL OPEN, with a licence reason attached: no education layer on an APAC
  sovereign model.** [aisingapore/sealion](https://github.com/aisingapore/sealion)
  (424★) has **no repository-level `LICENSE` payload**; its README states terms
  vary by base model — Llama3 variants restrict commercial use, Gemma variants
  differ — and points to each **Hugging Face model card**. **Rights clear per
  model and per release, never per repository.** Landscape additions: **MaLLaM**
  (Malaysia, with NVIDIA, 3M+ users via YTL/Yes) and **Gemma-SEA-LION-v4-27B-VL**
  (March 2026).
- **NEW: no permissive way for a non-technical educator to author and publish
  their own agent.** AICET's **ScholAIstic** does exactly this — educators design
  and deliver specialised chatbots, deployed across Social Work, Law and Nursing
  at NUS since June 2024 — and it is closed. Pattern **P8** is the nearest thing
  in this KB and it stops short: it produces Agent Skills *for* educators, not an
  authoring surface *used by* them. Precisely sized, uncontested, and validated at
  faculty scale by somebody else.
- **NEW: the education vertical does not appear in general AI trend tracking.** A
  daily AI open-source trend feed read on 2026-10-06
  ([duanyytop/agents-radar#3628](https://github.com/duanyytop/agents-radar/issues/3628))
  listed 23 repositories by star movement and **not one was an education-vertical
  project** — the only education-adjacent entry was `rasbt/LLMs-from-scratch`, which
  is AI literacy. *(That feed's star counts are demonstrably inflated and were not
  used for any number in this KB; it was read as a presence/absence check only.)*
  **An education shelf must be built by vertical search and never by watching what
  trends.**
- **Still no Brazil-origin permissive project.**
  [vitorr2101/Projeto-Agente-IA-Educacional](https://github.com/vitorr2101/Projeto-Agente-IA-Educacional)
  surfaced on a Portuguese-language search and has **no `LICENSE` payload** on
  either branch across five filenames. The one LATAM-origin project that exists is
  **Colombian**.
- **Unverifiable, therefore not recorded: "K.A.L.I."**, described in search results
  as a sovereign AI learning engine with 3D logic visualisation. A targeted search
  returned ten unrelated `sovereign`-named repositories and no such project. Named
  here so a later pass does not re-surface it as new.

---

### Fourth-pass gap block, retained

**Updated in the fourth pass of 2026-10-06.** Channels new to this KB this pass:
paper-to-repository tracing, a GitHub-organisation sweep, and a
Spanish/Portuguese-language search. Four of the gaps below changed state.

- **RESOLVED-IN-PART: lesson generation is no longer a gap at all.**
  [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (**MIT, 40.0k★,
  Tsinghua**) generates complete lessons — slides, quizzes, HTML simulations, PBL
  scenes — with server-side PostgreSQL-backed persistence. This KB spent three
  passes recording the 404 of a `-Brasil`-suffixed fork of this project as evidence
  of absence. **Check the upstream of a name before recording a gap.**
- **NARROWED: Africa has a code shelf.** `AI-for-Education` (5 of 6 repos MIT) is
  built for **Sierra Leone's MBSSE** and **Uganda**. At 1–12★ it is research-grade,
  so the gap becomes *small and specific* rather than *empty*. Teacher capability
  is still the binding constraint.
- **NARROWED: the gated-grading architecture has a permissive reference
  implementation.** `littlecookie0722/AI-Teaching-Agent` (MIT) implements the
  `WAITING_REVIEW` gate, sandboxed grading with evidence, and answer-stripped
  candidate views. **0★, no releases** — so the gap moves from "unbuilt" to
  "**not built at production maturity**". Re-implement, do not pin.
- **STILL OPEN, and now the firmest finding in this KB: no LATAM-origin permissive
  education project.** The gap **lost its strongest piece of evidence** this pass
  (`OpenMAIC-Brasil` was never Brazilian) and **survived anyway** on a
  Spanish/Portuguese-language search that returned zero LATAM-origin projects.
  Four independent channels agree.
- **STILL OPEN: no India-, Japan-, Korea- or ASEAN-origin permissive education
  project**, searched by jurisdiction name this pass. OpenMAIC **widens** the China
  lead rather than closing this. And still **no education layer on any APAC
  sovereign model** (Sarvam, SEA-LION, Sahabat AI, ILMU, HyperCLOVA X Think,
  BharatGen, Fugaku-LLM, NTT Sarashina).
- **NEW, precisely sized: no shippable permissive evaluator of tutoring quality.**
  `AITutor-EvalKit` (EACL 2026) is the only published instrument for scoring
  *tutoring* rather than answers — **MI** (Mistake Identification), **ML** (Mistake
  Location), **PG** (Providing Guidance), **AC** (Actionability) — and it has **no
  `LICENSE` payload**. `AI-for-Education/pedagogy-benchmark` (MIT, 12★) closes only
  the adjacent half: it scores **models against exam questions, not live tutor
  dialogue**. The evaluation gap is now split, and only the model-selection half is
  closed.
- **Still no open source EU AI Act compliance toolkit specific to education** —
  re-searched this pass, nothing found.

- **NARROWED (third pass, 2026-10-06): a permissive automated grader exists, for
  corporate L&D only.** `Selleo/mentingo` (MIT) grades open-ended behavioural and
  problem-solving answers automatically with Langfuse tracing over it. Still
  missing: a standalone permissive grader for **academic** assessment, and anything
  rubric- or curriculum-aligned for K-12 or higher-ed exams. The oversight
  requirement is unchanged — see trend 7.
- No open source EU AI Act compliance toolkit specific to education.
- No LATAM-origin open source education agent project — **now confirmed across
  three independent channels.** The third pass of 2026-10-06 added the `ai-tutor`
  topic page and a stars-sorted education search: 30 repositories read, 17 net new,
  **zero LATAM-origin.** This is the most firmly established gap in this KB.
  Earlier evidence, retained: `planejaia/OpenMAIC-Brasil`, surfaced by search as a
  Brazil-origin multi-agent classroom with a v1.0.0 release, returns **HTTP 404**;
  every file 404s across four branches. The `education-ai` GitHub topic contains
  no LATAM-origin project at all (its long tail is Chinese, Indian and German, and
  nothing on it exceeds 448★). Latam-GPT is regional foundation infrastructure,
  not a pedagogy layer.
- **Africa: almost entirely uncovered, and that is now stated rather than
  implied.** South Africa's draft national AI policy (2026) is forming and
  GenAITEd Ghana is a published first-of-its-kind curriculum-aligned teacher-education
  agent, but there is no deployed open source African education AI shelf to
  recommend from. Greenfield, with teacher capability as the binding constraint.
- **No permissive open source auto-grader — and now a measured reason to distrust
  the shelf generally.** Of seven education MCP servers probed, three are
  unusable (two unlicensed, one AGPL + paid tier). The education open source
  shelf is thinner than its star counts imply.
- **PARTLY REFUTED (third pass, 2026-10-06): APAC-origin education agents exist in
  volume.** The earlier claim that `panaversity/learn-agentic-ai` was the only
  APAC-origin asset was an artefact of sweeping one topic page. StudyMate (MIT,
  **624★**), kaogong-skill (MIT, 156★), feifei-companion (Apache-2.0, 105★) and
  AI_Tutor_Release (MIT, 57★, Chinese grade 1–9 curriculum-aligned) are all
  China-origin and permissive; DeepTutor is Hong Kong. **What survives:** no
  education layer on an APAC **sovereign** model (Sarvam, SEA-LION, Sahabat AI,
  ILMU, HyperCLOVA X Think, BharatGen, Fugaku-LLM, NTT Sarashina), and **no India-,
  Japan-, Korea- or ASEAN-origin permissive education project found in any channel.**
  The APAC shelf is China-plus-Hong-Kong.
- **No curriculum-aligned permissive content pipeline for the UAE's seven-area
  mandate** — searched this pass, nothing found. `Zenglian990/AI_Tutor_Release`
  (MIT) is aligned to the Chinese grade 1–9 curriculum and is the only
  curriculum-aligned permissive tutor on the shelf; there is **no equivalent for
  the UAE framework**, and two of its seven areas are ethics and policy rather than
  technique. That is a specific, sized, uncontested build opportunity.
- **No open source age-gating or capability-tiering component for education.**
  Beijing bars primary pupils from independent generative-AI use and China
  prohibits teachers from substituting AI for core instruction; nothing on the
  permissive shelf implements cohort-based capability tiering. Pattern P9 assembles
  it from general-purpose parts, as pattern P4 does for Annex III.
