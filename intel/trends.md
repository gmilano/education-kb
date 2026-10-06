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

## 23. The licence label and the licence grant have come apart — and reading the payload is no longer enough

**Added in the eighth pass of 2026-10-06. This is a correction to how every
other trend in this file was verified.**

Eight passes of this KB established one verification rule: never trust a badge,
a sidebar or a blog post — **read the `LICENSE` payload from
`raw.githubusercontent.com`.** That rule bought real accuracy, and this pass
found its ceiling. **Four live cases, and the payload is wrong or silent in
every one:**

| Case | Payload says | Grant actually is | Direction |
|---|---|---|---|
| `Llamacha/IWSLT2023_Quechua_data` | **Apache-2.0**, complete and unambiguous | README: audio is **CC BY-NC-ND 3.0**, owned by Siminchikkunarayku + Llamacha | Payload **too permissive** |
| **Latam-GPT** (CENIA) | *(no repository located)* | **Llama 3.1 Community License** © Meta — **not OSI-approved**, AUP + 700M-MAU clause | Label **too permissive** |
| `caiuc/equipo-*` × 20 | **MIT**, complete | Holder is **CAi UC**, the event organiser, not the authoring teams — **template-inherited** | Grant **not issued by the author** |
| `AmericasNLP/americasnlp{2021,2022,2023,2024}` | **Nothing** | No grant at all, across four editions of a flagship venue — including a 2024 shared task on *creating educational materials* | **Silent** |

**The three shapes of failure, named so they can be checked for:**

1. **Wrong scope.** A correct, complete licence file that governs the
   repository's *scripts* while the *data* — the only reason to clone it — is
   governed elsewhere and more restrictively. New in this pass.
2. **Wrong holder.** A valid licence whose copyright line names someone other
   than the author, so the grant was inherited rather than issued. This KB's
   `p184` rule, now observed at a scale of 20 repositories at once.
3. **Wrong label.** Open *weights* under a bespoke corporate licence,
   described as open *source* by the press, by Brookings, and by **the European
   Commission's own Open Source Observatory**.

**Why it is a trend and not a methodology footnote.** All three shapes are
produced by the same market condition: **"open" has become a positioning claim
before it is a legal one.** Model-weight releases normalised bespoke licences
with acceptable-use policies and user-count thresholds; academic and
public-sector projects publish under grant-funded obligations to be "open"
without anyone on the project owning the licence question; and template-driven
repository creation propagates a copyright line nobody re-reads.

**Consequence for Globant, and it is a billable one.** The licence question in
an education engagement is no longer a checkbox a developer can clear in an
afternoon by looking at a repository page. **Three points, every time: the
payload, the asset-scope statement, and the holder.** For anything whose value
is data, audio, a corpus or weights, the asset-scope statement is
**controlling**. Budget it, and say so in the proposal — because the failure
mode is not "we could not find a licence", it is **"we found one, it was clean,
and it was the wrong one."**

**And the inverse is an opportunity.** The same condition means genuinely
permissive regional assets are **undersold**: BERTimbau sat at 886★ and MIT,
unmentioned anywhere in this KB for seven passes, while Latam-GPT's non-open
licence was being reported as open source by the EC. The asset that is quietly
correctly licensed is the one with no marketing behind it.

## 24. Licensing hygiene is now the measured constraint in two regions — and one event's rules fixed it in eight hours

**Added in the eighth pass of 2026-10-06.**

The seventh pass concluded of MEA: *"the binding constraint is not interest,
funding or capability — it is licensing hygiene. Three `LICENSE` files would
change the regional answer."* The eighth pass found the **same shape in LATAM's
indigenous-language layer**, which makes it a pattern rather than a regional
quirk:

- **AmericasNLP**, the flagship academic venue for the indigenous languages of
  the Americas: **four probed editions (2021, 2022, 2023, 2024), no `LICENSE`
  payload in any** — and the **2024 edition's Shared Task 2 is "Creation of
  Educational Materials for Indigenous Languages"**, which is precisely the
  asset this KB would want, shipped with data, baselines and no grant. Corpora for **Aymara** (6,531 pairs), **Nahuatl** (16,145)
  and **Quechua** (125,008).
- ASR for **Quechua, Guaraní, Bribri, Kotiria and Wai'khana**; MT for Peru; a
  T5 for **10** indigenous languages — **all ungranted.**
- **Ten of twelve** probed repositories carry no grant. The same organisation
  licensed its 2023 release and not its 2025 one; the same author licensed
  neither of two.
- Five LATAM education-AI applications found the same pass
  (Colombia ×3, Chile, Peru): **none has a `LICENSE` payload.**

**The capability is funded, published and benchmarked. The redistribution right
is absent.** So a Quechua or Guaraní tutor is blocked on **data rights, not on
modelling** — and that is a procurement and legal problem, which is cheap to fix
and expensive to discover late.

**The remedy, demonstrated rather than proposed.** **CAi UC** (*Centro de
Alumnos de Ingeniería*, Pontificia Universidad Católica de Chile) ran
**HaCAIthon 2026** with one clause in its rules: projects must ship an **OSI
licence** and a **root `LICENSE` file** to be *eligible for evaluation*.
**Result: 20 team repositories, 19 MIT and one AGPL-3.0, in a single eight-hour
event**, four of them education-track — including **EduFlow**, the first
LATAM-origin MIT education repository in this KB with running code.

**Why this is the most leveraged intervention this KB has identified.** The
sixth and seventh passes' recommendation was *file an issue asking for a
`LICENSE` file* — correct, but **retrospective**, one repository at a time, and
dependent on a maintainer who has already moved on. A submission rule is
**prospective**: it licenses work that does not exist yet, at the moment of
creation, when the authors are present and the question is trivial.

**The concrete action, with its caveat.** Sponsoring or co-writing the licence
clause in a university hackathon's rules — São Paulo, Lima, Bogotá, and on the
identical argument in Nairobi — costs a sponsorship line and addresses the one
constraint blocking **both** LATAM and MEA. **Caveat:** CAi UC's own template
put the **organiser** in the copyright line rather than the authoring team,
which is the wrong holder and triggers this KB's `p184` flag on all 20 repos. A
sponsored clause should name the **authors** as holders — a one-line difference
between a channel that produces usable assets and one that produces flagged
ones.

## 25. Permissive licensing has become a funding condition, and philanthropy is now the supply mechanism

For nine passes this KB has treated the permissive shelf as something that either
*exists* or *does not* — an organic output of universities, hackathons,
ministries and individuals, to be swept and graded. A different mechanism is now
operating: **a funder is buying the shelf into existence, and making the licence
a condition of the money.**

**The instrument.** The **K-12 AI Infrastructure Program** — **$26M**,
multi-year, led by **Digital Promise** with **Learning Data Insights**,
**DrivenData**, the **Massive Data Institute at Georgetown University** and
**Catalyst @ Penn GSE**, funded by the **Gates Foundation**, which also runs
proposal review and award monitoring. Launched 3 Nov 2025; first cycle open
4 Feb 2026.

**The condition.** All funded developments must be released under a licence **at
least as permissive as CC-BY-4.0 (content) or Apache-2.0 (code/models)** — with
**Apache-2.0** recommended for software and code *including evaluations, models
and applications*, and **CC-BY** for datasets and knowledge products.

**The volume already committed:** **twelve named projects** — four in cohort 1
(29 Jun 2026: Learning Equality on science misconceptions; Princeton on
simulated student models; National Tutoring Observatory / Cornell on ASR
leaderboards for education; Stanford's KB-TutorBench for formative assessment)
and **eight** in cohort 2 (21 Sept 2026, formative assessment plus math,
literacy and writing, outputs stated to be openly licensed) — plus the separate
**EDU AI** award of **up to $8M** for open-source K-12 math tutoring model(s),
closed 31 Jul 2026, work from Nov 2026 over 30–36 months.

**Why this is a trend and not a news item.** Three structural consequences:

1. **The arrival of permissive assets becomes predictable.** Organic open source
   gives you a shelf you discover; a funded programme gives you a **pipeline with
   owners and dates.** For the first time this KB can tell a client *when* a
   missing capability is expected rather than only that it is missing.
2. **Apache-2.0 becomes the default licence of the education AI commons,
   displacing MIT.** This KB's shelves are MIT-dominant because individuals and
   universities default to MIT. A funder specifying Apache-2.0 for *models,
   evaluations and applications* pushes the new layer toward Apache-2.0 — which
   brings an explicit patent grant, a material improvement for client work, and
   a licence-compatibility question nobody has to solve because both are
   permissive.
3. **It inverts where the gaps are.** The capabilities being funded are precisely
   the ones organic open source failed to produce: **evaluation, benchmarks,
   datasets, formative assessment, ASR for education.** These are expensive,
   unglamorous, require real data access, and have no individual-contributor
   path — which is exactly why this KB kept finding them absent for nine passes.

**The honest counterweight, measured:** **nothing has shipped.** `KB-TutorBench`
→ **0 repositories**; `learningequality` filtered on `benchmark` → **0
repositories**; the National Tutoring Observatory's org holds a website at 0★
with no licence payload. **Funded is not shipped**, and the correct posture is
architectural readiness (**P23**), not waiting.

⚠️ **Tier 2.** `k12-ai-infrastructure.org` and `digitalpromise.org` are
**EGRESS_BLOCKED** here; **no RFP or announcement was read.** Figures are
corroborated across independent search summaries. Confirm before client use.

## 26. In the US the procurement rubric, not the regulator, is now the specification

Trend 16 recorded that US state law had converged on one testable rule: **human
judgment is final.** That is a *constraint*. What a vendor actually has to
satisfy is a **scored rubric**, and 2026 is the year those rubrics became
mandatory, standardised and dated.

**The mechanism:**

- **Maryland SB 720** (effective **1 Jun 2026**): the state department publishes
  guidance **and an AI-tool evaluation rubric**; every local school system must
  adopt an aligned policy **within 120 days** and designate an **AI
  coordinator**. Reported as **24 districts** on the clock for **Fall 2026**.
- **Vermont** (**23 Jan 2026**): a rubric scoring **educational value, data
  privacy, usability and accessibility, cost, scalability, vendor reputation and
  age restrictions.**
- **Idaho, Maryland, Alabama**: statutory **capability assessments**,
  **pre-training verification**, and a **prohibition on vendors training models
  on student records** — now standard contract language.
- **CoSN, *U.S. State of EdTech 2026*: 39% of districts score interoperability in
  their RFP rubrics.**

**Three reasons this changes delivery, not just sales:**

1. **Interoperability is now a scored criterion, which retro-justifies trend 4.**
   This KB argued MCP/LTI side-cars on engineering grounds. In two of five
   district procurements, that architecture **wins points**. An LTI + MCP
   side-car (**P1**) is not merely clean — it is the shape the rubric rewards.
2. **"Prohibit training on student records" is an architecture constraint, and a
   familiar one.** It forces either a no-training contractual guarantee or
   inference you control. That is the **sovereign/on-prem** stack of trend 6 and
   pattern **P4** — arriving in North America through procurement law rather than
   through data-protection law as it did in the EU.
3. **The rubrics' own gap is the differentiator.** Most reportedly do **not**
   require **auditable interaction records**, **disclosure of how outputs are
   generated**, or **evidence of bias/accuracy/reliability evaluation.** Ship
   those three and you exceed every published rubric — and they are, nearly
   exactly, the artefacts the **EU AI Act education profile** already compels
   (**P13**). **One evidence pack, two regions.** That is the first genuine
   cross-region reuse this KB has identified on the compliance axis, and it runs
   from EMEA into North America rather than the other way round.

**The demand signal underneath it** is concrete: **NJSBA RFP 2026-02** (virtual
tutoring, with optional **outcomes-based contracting**) and **New Mexico PED RFP
27-92400-00002** (statewide high-impact tutoring for reading and math under
**House Bill 2**, SY2026-27 the first implementation year). Districts and states
are buying tutoring at scale, on rubrics, with outcome clauses.

⚠️ **Tier 2.** `cosn.org`, `marylandpublicschools.org`, `njsba.org`,
`web.ped.nm.gov`, `excelined.org` and `marketbrief.edweek.org` are all
**EGRESS_BLOCKED** here; **no rubric or RFP document was read.** Confirm each
statutory citation before client use.

## 27. The evaluation void is being closed by two instruments in two regions — a cheque and a rule

For five passes this KB recorded one absence: **no shippable permissive evaluator
of tutoring quality.** The ninth pass found North America buying it. This pass
found EMEA regulating it. **The same void, addressed by two different kinds of
instrument, on overlapping timelines.**

| Region | Instrument | Mechanism | Status |
|---|---|---|---|
| **North America** | **$26M K-12 AI Infrastructure Program** (Digital Promise + Gates Foundation) | **Funding**, with a mandatory licence floor at least as permissive as CC-BY-4.0 (content) / Apache-2.0 (code and models) | 12 projects funded; named grantees include Harvard's **OpenLiteracy**, Maryland's classroom datasets, Stanford's **KB-TutorBench**, Cornell's ASR leaderboards. **0 repositories shipped.** |
| **EMEA** | **Council of Europe Compass for AI and Education** + **Committee of Experts (EDU IA)** | **Rule-making** — a **European Reference Framework for the Evaluation of Educational Technologies**, plus a proposed **legal instrument to regulate AI systems in education** | 2026–27 work programme; Committee of Ministers text adopted in **Munich** under **Article 20** of the Framework Convention on AI |
| **APAC** | **none found** | — | Searched this pass and the ninth. No regional instrument and no regional funder addressing evaluation of educational AI. The region's most on-target asset, `AI-EDU-LAB/E-EVAL` (Chinese K12 LLM education evaluation benchmark, 33★), exists and is **ungranted** — re-probed across 20 URLs this pass, still no licence payload. **APAC built the benchmark and did not license it.** |
| **LATAM** | **none found** | — | Searched this pass and the ninth. No regional instrument, no regional funder. What exists is the measured demand: **9.0% of 200 higher education institutions across 19 countries have formal evaluation mechanisms** (UNESCO IESALC / UNU-IAS). **The need is quantified and the instrument is absent**, which makes this the region where an evaluation harness is sold as capability rather than as compliance. |

Both facts are **Tier 2** (search-summary corroborated; no primary document is
reachable from this environment).

**Why the pairing matters more than either half.** A benchmark you can adopt late;
a conformance framework you cannot. Evaluation evidence — interaction audit trails,
output provenance, measured accuracy and bias — has to be **generated while the
system runs**, which means a deployment that did not instrument for it has nothing
to submit when the framework lands. The North American artefacts are a *swap-in*;
the European framework is a *precondition*.

**What to do with it.** Build the harness now and leave the benchmark slot empty
(**P23**). It is the same harness in both regions: the US side fills it with
Apache-2.0 benchmarks as the twelve projects deliver through 2027; the EMEA side
turns its output into a conformance file. This also gives the EU AI Act work
(**P13**) a named successor instrument to track rather than horizontal regulation
alone.

**The honest counterweight:** `tutoring quality evaluation benchmark
license:apache-2.0` still returns **0 repositories**, measured 6 Oct 2026. Neither
instrument has produced a usable artefact yet. The trend is real; the shelf is
still empty.

## 28. Interoperability became a scored line item — and the permissive shelf has a Python-shaped hole

The ninth pass found the demand signal: **39% of districts score interoperability
in their RFP rubrics** (CoSN, Tier 2). That is not a technical preference, it is
**points in a bid**. This pass measured the supply side, payload-verified:

| Standard | Permissive implementations found |
|---|---|
| **LTI 1.3** | **4** — `Cvmcosta/ltijs` (Apache-2.0, 373★, Node), `1EdTech/lti-1-3-php-library` (Apache-2.0, 124★, PHP, **from the standards body**), `Unicon/tool13demo` (Apache-2.0, 27★, Spring Boot), `oxctl/spring-security-lti13` (Apache-2.0, 25★, Spring Security) |
| **OneRoster 1.1 / 1.2** | **1** — `theopenem/OneRoster.NET` (MIT, 6★, .NET), **rostering only, gradebook not implemented** |
| **Caliper Analytics** | **0 found on a permissive licence** |
| **QTI** | not swept |

**The structural finding: there is no Python LTI 1.3 library on the permissive
shelf.** Node, PHP, Java and .NET are served. Python — where essentially all of
the AI tutoring and agent code in this KB is written — is not. So the real
architecture is a Python AI service behind an LTI adapter in a *second* runtime,
and the adapter is a **budgeted component**, not an afternoon's integration work.

Three consequences for how work is scoped:

1. **The LMS choice now implies the integration runtime.** Moodle → the 1EdTech
   PHP library; a Spring estate → `oxctl`/`Unicon`; a Node AI service → `ltijs`.
   Week-one decision, alongside the platform.
2. **Grade passback and analytics streams are builds, not selections.**
   OneRoster.NET does rostering only, and Caliper has no permissive
   implementation here. If the rubric scores either, say "build" in the bid.
3. **A Python LTI 1.3 library is the clearest open-source contribution opening
   this KB has identified** — a gap with a procurement-scored buyer already
   attached to it.

**And a vocabulary warning that is part of the trend.** `OneRoster OR Caliper OR
"LTI 1.3" license:apache-2.0` returns **184 repositories**, led by
`google/caliper` (deprecated Java micro-benchmarking, 818★) and
`hyperledger-caliper/caliper` (blockchain benchmarking, 708★). **Education
standards share names with unrelated ecosystems**, and the result count reads as
ecosystem health when it is mostly a different ecosystem.

## 29. Gap claims built on licence-filtered search are claims about an index, not about the world

This is a methodological trend, and it belongs here because this KB — and every
consultancy doing the same work — **prices engagements on declared absences.**

Measured this pass: [qazasd2518995/prosody](https://github.com/qazasd2518995/prosody)
is listed in GitHub's repository search as **"License: Not specified."** Its
payload at `main/LICENSE` is a **complete, unmodified MIT licence.**

**GitHub's licence field reported unlicensed about a repository carrying an MIT
grant.** The consequence is mechanical: a `license:mit` or `license:apache-2.0`
filter **cannot return** a repository the index believes is unlicensed. So every
zero-result, licence-filtered measurement — the instrument this KB uses to declare
that something does not exist — has a **false-negative floor it cannot see.**

Three of those zero-result measurements were run in this very pass, and are quoted
in `intel/market.md` as evidence that funded projects have not shipped. They stay,
because they remain the best available measurement. **Their meaning changes:**
they are evidence of **absence as the licence index sees it.**

The same pass produced the other half of the lesson. Re-probing the 41
repositories this KB had recorded as ungranted — 10 filenames × 2 branches each,
controls validated 6 of 6 — flipped exactly **one**, and the cause was neither of
the things the previous pass blamed: not the British spelling `LICENCE` (which
flipped **zero** of 41), but the **branch name**, which no pass had ever varied.

**The operational rule, for this KB and for client diligence:** a licence claim
is only as good as the payload read from the repository, under **every** spelling
and **every** branch; and an *absence* claim must state the instrument that
produced it. "There is no permissive X" is not a finding. **"A GitHub repository
search filtered on `license:apache-2.0` returned zero results on this date"** is,
and it is a materially weaker claim — which is the point.

## 30. The ministry tier is being bought by one proprietary vendor across three regions, ahead of the governance capacity

**Tier 2.** OpenAI's **Education for Countries**, launched at Davos 2026, works
directly with ministries of education, public universities and research partners.
Named participants place into three of this KB's four regions:

| Region | Named |
|---|---|
| **EMEA** | Estonia, Greece, Italy (**CRUI**, the rectors' conference), Slovakia, UAE, Jordan |
| **APAC** | Kazakhstan, **Singapore** (Ministry of Education + **GovTech**, added 20 May 2026 at the Education World Forum, London) |
| **LATAM** | **Trinidad & Tobago** |
| **North America** | **none named.** The programme is US-headquartered and contracts with *other* countries' ministries; **no US state or federal education agency is named as a participant.** North America's national-tier analogue is the $26M philanthropic programme with an Apache-2.0 floor (trend 25), which is the opposite acquisition model: it buys open artefacts rather than onboarding ministries. |

**Nine national or sector-wide bodies, one vendor, the ministry tier.** This is the
competitive context for every engagement in this KB, and it changes the pitch in
two specific ways.

**First, the sequencing is the risk.** LATAM is measured at **9% of institutions
with formal evaluation mechanisms** and **8% with a dedicated AI budget** (UNESCO
IESALC, 200 institutions, 19 countries). Trinidad & Tobago is acquiring a national
AI education programme into that. **The vendor is arriving before the capacity to
evaluate the vendor** — which is simultaneously the strongest argument for buying
governance work now and the mechanism by which a closed stack becomes permanent.

**Second, the opening is in the buyers' own language.** Singapore's MOE is
described as *"exploring various AI tools from different partners."* A ministry
that states a multi-partner posture while onboarding one vendor will evaluate
alternatives — and with **GovTech** in the room, the counterparty is an engineering
organisation capable of assessing an open, auditable, data-resident stack on its
merits. The named Singapore use case is **mother tongue language learning**, which
is precisely where this KB's permissive language-substrate shelves are strong and a
single global vendor is weakest.

**And EMEA is the region where this argument is being written into law.** Six EMEA
bodies are in the programme while the Council of Europe drafts a legal instrument
on AI systems in education and a framework for evaluating educational technology
(trend 27). **Sovereignty, auditability and data residency are not positioning in
this region; they are the subject matter of the instrument being drafted.**

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

## Declared gaps — eighth pass, 2026-10-06

- **Trend 21 needs splitting, not another increment.** It currently reads
  *"mother-tongue AI is a three-region capability"*. After this pass the honest
  form is **two claims**: *capability* is at least **four** regions (India,
  Africa, ASEAN, LATAM), while **redistributable** capability is still **two**.
  LATAM has the corpora, the ASR and the MT and cannot license them. Left as a
  declared gap rather than silently renumbered, because the distinction between
  *existing* and *usable* is the whole content of trends 23 and 24.
- **No automated evaluator of tutoring quality — open since the fourth pass,
  unchanged.** TutorIA's **RNF-09** (pedagogical review by **≥2 subject-expert
  teachers per subject before launch**, MIT) is a **human protocol**, and it is
  the first citable one in this KB. It does not close the gap and is not
  presented as closing it.
- **No permissive open-source exam proctoring agent — not re-probed this pass.**
  The seventh pass's sweep stands; recorded so the next pass knows it was
  skipped rather than re-confirmed.
- **North America's general-language channel is saturated.** Four consecutive
  passes, identical facts. The next North America trend must come from district
  RFP language, state education-agency procurement portals, or vendor filings —
  **none of which this KB has ever swept.** Recorded as an exhausted channel, not
  as regional stability.
- **Latam-GPT's licence is single-source.** `huggingface.co`, `latamgpt.org`,
  `interoperable-europe.ec.europa.eu` and `opensourceforu.com` are all
  **EGRESS_BLOCKED** in this environment (4/4), so the model card was **not
  read**. The Llama 3.1 Community License's *properties* are independently
  confirmed from the OSI's published position; the **link** between Latam-GPT
  and that licence is not. Confirm before any client deliverable.
- **The `p184` holder question on the 20 CAi UC repositories is unresolved and
  is not a probe question.** Whether a student federation's template copyright
  validly covers code written by independent teams during an event is a matter
  for counsel. Recorded as a legal open item, not as a licence finding.

## Declared gaps — ninth pass, 2026-10-06

- **Trend 7's tooling gap is funded, not filled.** Assessment remains the
  regulated frontier with no permissive tooling *today* — measured this pass as
  **0 repositories** for `tutoring quality evaluation benchmark
  license:apache-2.0`. What changed is that **three or more of the twelve funded
  projects under trend 25 target exactly this**, through 2027. Recorded as a dated
  gap rather than renumbering trend 7.
- **The proctoring claim in this KB was wrong, and trend 7 should not be read as
  supporting it.** The seventh pass declared *"no permissive open-source exam
  proctoring agent"*; the eighth carried it unchanged. **204 MIT-licensed
  repositories match**, four payload-verified at 18–47★. The surviving claim is
  **maturity**, not existence — and the one framework-grade implementation
  (`lebmatter/exampro`, 72★) is **ungranted**. See `agents/top.md`, ninth pass.
- **Trend 21 still needs splitting, and the eighth pass's note stands
  unactioned.** *Capability* is at least four regions; **redistributable**
  capability is still two. This pass adds a fourth datapoint in the same shape
  from a new region — `AI-EDU-LAB/E-EVAL` (33★, Chinese K12 LLM education
  evaluation benchmark, **no licence payload**) — so the pattern is now recorded
  in **MEA, LATAM and APAC**. Left as a declared gap for a second consecutive
  pass rather than silently renumbered.
- **No primary funder or procurement document was read.** Fourteen hosts are
  **EGRESS_BLOCKED**: `k12-ai-infrastructure.org`, `digitalpromise.org`,
  `unu.edu`, `arxiv.org`, `cosn.org`, `marylandpublicschools.org`, `njsba.org`,
  `web.ped.nm.gov`, `excelined.org`, `marketbrief.edweek.org`,
  `edtechinnovationhub.com`, `www2.fundsforngos.org`, `en.wikipedia.org`,
  `rachel.worldpossible.org` (and `rachel.core2learn.org`). **Trends 25 and 26
  rest entirely on corroborated search summaries.** This is the largest block of
  Tier 2 material this KB has admitted to its durable files; it is labelled as
  such in every table, and it should be the first thing the next pass tries to
  upgrade if egress changes.
- **Seven of cohort 2's eight grantees are unnamed.** Announced 21 Sept 2026;
  only **MMSA & TERC** surfaced. Each unnamed award is an Apache-2.0-or-better
  artefact with a named owner landing inside twelve months — **the single
  highest-value lookup available to the next pass.**
- **Vendor filings remain unswept.** The eighth pass named three North America
  sub-channels: district RFPs ✅, state procurement portals ✅, **vendor filings
  ❌**. Earnings calls, S-1s and 10-Ks of listed edtech vendors are a distinct
  channel and would speak to consolidation and pricing, which no channel in this
  KB currently covers.
- **EMEA and APAC general queries have now failed twice consecutively.** Both
  returned enterprise AI-governance material, not education. The
  **ministry-engineering-org** channel that produced the UK DfE estate this pass
  is the obvious replacement for both and has not been run outside the UK.
  Recorded as exhausted channels, not as regional stability.
- **SciEval and EduEVAL-DB are leads, not findings.** `arxiv.org/pdf/2604.25472`
  and `arxiv.org/pdf/2602.15531` are EGRESS_BLOCKED and a GitHub name sweep
  returned **no repository** for either. Both are directly on the evaluation gap
  and should be re-probed when arXiv is reachable.
- **This KB's licence probe had a spelling bug for nine passes — and the fix was
  already written down.** Pattern **P22**'s gate lists `LICENCE`; **no recorded
  sweep ever ran it**, and **three of six UK ministry MIT grants use it.** Every
  negative result in this pass was re-run against the British spellings and
  survived, but **earlier passes' "ungranted" verdicts on Commonwealth, MEA and
  ministry-adjacent repositories were produced by a query that could not have
  found a British-spelled grant** and are unconfirmed until re-probed. This is
  the seventh instance of the probe-vocabulary failure mode and the first that
  invalidates prior conclusions rather than merely missing new ones.

## Declared gaps — tenth pass, 2026-10-06

- **No permissive Caliper Analytics implementation.** Searched with the licence
  filter; the result set is dominated by two unrelated projects sharing the name.
  If an RFP scores learning-analytics event streams, it is a build.
- **No Python LTI 1.3 library.** Four permissive LTI 1.3 implementations exist
  across Node, PHP and the JVM; none in the language the AI layer is written in.
- **No gradebook in the permissive OneRoster shelf.** `theopenem/OneRoster.NET`
  states it: rostering calls only, grade book not implemented.
- **`OpenLiteracy` returns 0 GitHub repositories**, as do `tutoring quality
  evaluation benchmark license:apache-2.0` and `formative assessment dataset
  classroom`. Three funded, named, dated projects; three measured zeros. **Read
  these three zeros against trend 29** — they are measurements of GitHub's licence
  index, not of the world.
- **Five of the eight Cohort 2 grantees of the $26M programme remain unnamed.**
  Harvard (Ying Xu), Maryland (Jing Liu) and MMSA & TERC are known.
- **The oral reading fluency shelf is two repositories**, one MIT with a single
  commit (`prosody`), one with no licence payload (`ReaDirect-V2`), neither with a
  star. The sixth pass's *"does not exist"* wording is **retired** in favour of
  this denominator.
- **The vendor-filings channel is unreachable, not unswept.** `www.sec.gov` is
  `EGRESS_BLOCKED`. McGraw Hill's and Workday's FY2026 open-source and
  copyleft-risk disclosures are Tier 2 only. The next pass needs a different host,
  not a better query.
- **No primary document was read, and 23 distinct hosts have now been attempted
  across two passes with zero reachable** — including three syndicated mirrors
  tried specifically to bypass a blocked primary host. Every market, funder,
  regulatory and procurement figure in these files is **Tier 2**.
- **Two Learning Equality repositories are ungranted** —
  `kolibri-design-system` and `kolibri-server`, no payload under 20 probed URLs —
  inside an organisation whose other five probed repositories are MIT. **Licence
  posture is not inherited; probe each repository.**
- **The fork direction between `theopenem/OneRoster.NET` and
  `jdolny/OneRoster.NET` is not established.** Byte-identical README and licence,
  both naming `theopenem` as holder; `github.com` returns 403 to `curl` here and
  the rendered page carries no fork banner. Pin the holder-matching copy.
- **APAC's `E-EVAL` and nine LATAM-placed language/hackathon repositories remain
  ungranted after a full 20-URL re-probe.** These negatives now hold under a
  stricter method than the one that produced them, which makes them usable: the
  blocker is licensing, not capability, and not this KB's reach.

## 31. The pedagogy benchmark is no longer missing — it is licensed shut

For three passes this KB recorded the evaluation void as an *absence*: nothing to
measure a tutor against, a $26M philanthropic programme funding the artefact, and an
engagement line that said *build the harness and wait*. Measured properly on
2026-10-06, the absence was a search artefact. **The benchmarks exist. The grants
do not.**

| Benchmark | Institution | ★ | Grant, read from the payload | Usable in client work? |
|---|---|---|---|---|
| `Khan/tutoring-accuracy-dataset` | **Khan Academy, Inc.** | 57 | Custom **"Evaluation Dataset License"** — internal, **non-commercial evaluation only**; **no redistribution, no model training, no production use**; viral over combined datasets. Carve-out: evaluating products *intended for commercial use*, and commercial use of the **insights**, are permitted. | ⚠️ **Borrow, never ship** |
| `eth-lre/mathtutorbench` | **ETH Zurich** (EMNLP 2025 Oral) | 43 | **No payload.** README asserts **CC BY 4.0** in a badge and **CC BY-SA 4.0** in the body. | 🔴 **Ungranted** |
| `Yunfeng-Wan/CSTutorBench` | — | 2 | **CC BY-NC-4.0** | 🔴 **NonCommercial** |
| `shivanireddyk/tutoreval` | one author | 0 | **MIT** | ✅ — and it is a weekend project |

**This is a different trend from "there is no benchmark," and it changes the
deliverable.** A void is filled by building. A wall is navigated by **separating the
instrument from the artefact**: the harness and the rubric are yours and permissive;
the datasets are called at measurement time under their own terms and never vendored,
never trained on, never handed over. The number you deliver is the finding — and
Khan's licence explicitly permits you to bill for it.

The second-order effect is a market one. **An industry whose only credible quality
benchmarks are non-redistributable cannot standardise on them.** Every vendor
measures privately against instruments it cannot publish results from in a
comparative form. That is precisely the condition that makes the EMEA route — a
*reference framework* for evaluation, written as a rule (trend 27) — more durable
than the North American route of funding open artefacts, and it is why a
**permissively licensed pedagogical benchmark is the highest-value open-source
contribution available in this industry right now.** It is a licensing contribution,
not a code one.

## 32. The evaluation tooling for education is being written by governments, and it is permissive

The three most capable evaluation instruments on these shelves are not vendor
products and not academic one-offs:

| Instrument | Who maintains it | Licence | Scale |
|---|---|---|---|
| **Inspect** (`UKGovernmentBEIS/inspect_ai`) | **UK AI Security Institute** | **MIT** | **2,945★**, 779 forks, pushed 2026-10-06 |
| **Moonshot** (`aiverify-foundation/moonshot`) | **AI Verify Foundation** (Singapore **IMDA**) | **Apache-2.0** | 355★, 72 forks, pushed 2026-10-06 |
| **Sunbird** (`project-sunbird/*`) | India's national platform programme | **MIT** | deployed at national tier; 🔴 dormant since 2024 |

**A pattern worth naming: the public sector is now the most reliable source of
permissively licensed AI infrastructure in this industry.** Private open-source
education platforms in this KB trend AGPL-3.0 (LearnHouse 2,320★, CourseLit 1,269★,
Obojobo, Materia) or GPL (Moodle, i-educar, OpenEMIS). The MIT and Apache-2.0 assets
at comparable scale are governmental or government-adjacent: UK AISI, Singapore IMDA,
India's Sunbird, France Université Numérique's Richie (MIT), Switzerland's OpenOLAT
(Apache-2.0), the Ed-Fi Alliance (Apache-2.0).

Three consequences for how an engagement is built and sold:

1. **The permissive layer and the copyleft layer have swapped places.** The
   conventional assumption is permissive infrastructure underneath and copyleft
   applications above. In education it is now **copyleft platforms underneath and
   permissive, government-built evaluation and interoperability tooling around
   them.** Put the client-visible AI in the permissive layer — portal tier (Richie,
   MIT), evaluation tier (Inspect, MIT), protocol tier (pylti1.3, MIT) — and the
   copyleft stays behind an interface.
2. **A government licence is a procurement argument.** "The evaluation harness is
   the UK AI Security Institute's, MIT-licensed" answers a ministry's question about
   independence in one sentence, in a way no vendor claim does.
3. **But a government repository is not a maintained dependency by default.**
   Sunbird is MIT, at national scale, and has not been pushed to since August 2024,
   with one component archived. Inspect and Moonshot were both pushed on the day of
   this pass. **Check `pushed_at`, not provenance.**

## Declared gaps — eleventh pass, 2026-10-06

- **No permissively licensed tutoring-evaluation benchmark exists.** Trend 31. Four
  instruments, one MIT and at 0★. **The gap worth a Globant contribution**, and the
  contribution is a licence, not an algorithm.
- **No oral reading fluency product exists.** Re-measured with the API: **4
  repositories, 6 including forks.** One MIT (`prosody`, 0★, 1 commit), one
  BSD-2-Clause-plus-contribution-clause Android app from 2017 (`labaaoom`, 1★), one
  ungranted even on its real default branch (`ReaDirect-V2`, branch
  `deployment/playstore`), one 0★ calculator. The capability gap stands; the count is
  now exact rather than approximate.
- **`OpenLiteracy` → `total_count` 0.** The Harvard/Ying Xu early-reading project
  funded to close exactly that gap still has no public repository.
- **The Caliper reference implementation is not obtainable.** 1EdTech moved it to
  private repositories on **2023-06-17**; `imsglobal/caliper-python` and
  `concentricsky/badgr-server` both 404, and surviving public forks are 0★. The
  learning-analytics half of the interoperability tier is behind a membership while
  the LTI half stayed open. **Do not promise Caliper emission without pricing a
  membership or a clean-room build.**
- **Five of the eight Cohort 2 grantees of the $26M K-12 AI Infrastructure Program
  remain unnamed, and this gap is not closeable from this environment.** Naming them
  needs a primary document; 23 distinct hosts carrying one were attempted across the
  ninth and tenth passes and **all 23 returned EGRESS_BLOCKED**. Recorded as closed
  to this instrument so no further pass rediscovers it.
- **The LATAM-origin repository shelf does not exist.** `educación IA aprendizaje` →
  10 repositories, **all 0–1★**, one of them a satirical art project. Fifth
  consecutive pass at 0–9★, first measured with a count.
- **~155 of the 172 addresses dropped by this repository's reset are still
  unrecovered**, including the Ed-Fi stack, LibreTexts, OpenStax, the Nextcloud AI
  apps, the xAPI/LRS tier, ~16 Moodle AI plugins and ~20 education MCP servers. They
  are listed in `archive/2026-10-06-pre-reset/`. **A pass spent there will out-yield
  a pass spent on the open internet.**

## 33. The permissive set includes two more licences the standard filter rejects — and one of them is education's own

Trend 15 established that "permissive" is a bigger set than MIT, Apache and BSD. This
pass found the two entries that matter most for this industry, and the first one is not a
curiosity:

**ECL-2.0 — the Educational Community License 2.0.** OSI-approved. It is **Apache-2.0
with exactly one modification**: the patent grant is narrowed so that a contributing
university licenses patents only for the work it contributed, rather than across its
whole portfolio. That clause exists because technology-transfer offices would otherwise
veto university participation in open source. For redistribution and commercial use, it
behaves as Apache-2.0.

It covers the **Apereo** estate — the consortium behind **Sakai** and a large share of
higher education's shared infrastructure. A `license:mit OR license:apache-2.0` filter
rejects all of it. This KB's own filters have been doing so for eleven passes.

**ISC.** OSI-approved, functionally MIT, shorter. It carries
[pie-framework/pie-qti](https://github.com/pie-framework/pie-qti) — a **QTI 2.1/2.2/3.0
player** with bidirectional QTI ↔ PIE transforms, copyright **© 2026 Renaissance
Learning**, a commercial assessment vendor.

**The permissive allow-list for this KB is therefore: MIT, Apache-2.0, BSD (2- and
3-clause), ISC, ECL-2.0.** MPL-2.0 sits just outside it as **file-level weak copyleft** —
usable in a mixed deliverable with per-file discipline, which is a different and much
cheaper constraint than AGPL's network-use clause.

⚠️ **A licence being usable does not make the code usable.** All three ECL-2.0
repositories found this pass have been **archived and read-only since 2019-01-31**. The
right conclusion is "add ECL-2.0 to the filter", not "adopt Apereo's analytics stack" —
for which the live permissive answer is the ADL/Yet Analytics xAPI chain.

## 34. Education's reusable IP lives at the plugin seam of copyleft platforms, not beside them

The most-deployed platforms in this industry are copyleft: **Moodle** (GPL-3.0),
**Open edX** (AGPL-3.0), **OpenEMIS** (GPL-2.0), **i-educar** (GPL-2.0). Eleven passes of
this KB priced that as a constraint on reusable studio IP. **It is more precisely a
constraint on where the IP sits.**

[openedx/XBlock](https://github.com/openedx/XBlock) — the **plugin SDK** that every Open
edX course component is written against — is **Apache-2.0** at **470★**, while the
platform core it plugs into is AGPL-3.0. A component written against the XBlock API is
**yours**, under whatever licence you choose, provided it stays a plugin consumed through
the published API rather than being linked into the platform tree.

Moodle shows the same architecture with the opposite default: its **in-tree** AI plugins
are GPL-3.0 (correctly — 8 of 8 verified this pass), while
[peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server), which reaches
Moodle data **from outside the tree**, is MIT. This KB has recorded that licence-boundary
note for several passes; XBlock generalises it.

**The pattern, stated as a rule for engagement design:**

| Where your code sits | Licence you inherit | Reusable as studio IP |
|---|---|---|
| Inside the platform tree | The platform's (GPL/AGPL) | No |
| Against a **published plugin API** | **Your choice** | **Yes** |
| Outside the platform, over MCP / REST / LTI | **Your choice** | **Yes** |

**So the architectural decision that determines IP ownership is made before any code is
written**, and it is not a licence decision — it is a packaging decision. The LATAM
`TutorIA` specification on this KB's agent shelf already chose correctly
(*"delivered as an Open edX XBlock/plugin"*) without, as far as its documents show,
knowing that the SDK was Apache-2.0.

⚠️ **Get the packaging reviewed by counsel, not by a licence-file read.** The AGPL reaches
derivative works, and whether a plugin is one is a question about linkage and distribution,
not about which repository the licence file lives in.

## 35. Ungranted code clusters by the type of body that published it, not by region

Across the 66 repository addresses resolved this pass, **11 carried no licence grant at
all** — measured against 30+ filename variants on each repository's real default branch,
so these are absences of a grant rather than failures of a probe. They are not scattered:

| Publisher type | Ungranted found | Examples |
|---|---|---|
| **Public-sector bodies and standards groups** | 5 | DG EMPL (`european-digital-credentials`), **FWU** Germany (2 school ontologies), **DINI-AG-KIM**, **IMDA**'s `LLM-Evals-Catalogue` |
| **Individual-maintainer LMS plugins** | 3 | `moodle-tool_aiconnect`, `moodle-local_aihub`, **`moodle-ai-graded-assignment`** |
| **Academic content repositories** | 1 | **`CAHLR/OATutor-Content`** — the content of an **MIT** engine |
| **LATAM individual projects** | 2 | `tutor-adaptativo-ia`, `API-EduAdapt` |

**The inversion is the finding.** The bodies whose output is *most* reusable in principle —
ministries and standards groups publishing curriculum vocabularies and credential models,
whose entire purpose is shared infrastructure — are the **least likely** to attach a grant.
Meanwhile the individual developers publishing tutoring apps mostly do attach one.

**Three operational consequences:**

1. **Organisation-level licence inference is unsafe, even inside a regulator.** The
   `aiverify-foundation` organisation has two Apache-2.0 repositories and one ungranted
   one. Read every payload.
2. **The engine and its content are separately licensed, and the content is the pedagogy.**
   `CAHLR/OATutor` is MIT; `CAHLR/OATutor-Content` — the problem bank and hint trees — is
   ungranted. Anyone scoping an OATutor deployment on the strength of the engine's licence
   has mispriced the asset.
3. 🟢 **Asking is the cheapest unblock in this industry.** A ministry can attach a licence
   in one commit, and the usual reason there is none is that nobody asked. This belongs in
   the first fortnight of a public-sector engagement, in **every** region — it is not an
   EMEA peculiarity, it is a property of public-sector publishing.

## 36. The compliance instrument differs in *kind* by region, and that determines the deliverable

Trend 27 recorded two instruments closing the evaluation void — a cheque and a rule. With
APAC's harness verified this pass, the full picture is that **each region specifies AI-in-
education compliance through a different *kind* of artefact**, and a proposal written for
one region's instrument does not transfer:

| Region | The instrument | Its nature | What you actually deliver |
|---|---|---|---|
| **North America** | State statutes + **district procurement rubrics** (134 bills / 31 states; Ohio's July 2026 written-policy deadline) | A **scoring sheet** and a set of prohibitions | Evidence that scores: Ed-Fi/OneRoster/xAPI conformance, a policy and inventory pack, human-oversight procedures |
| **EMEA** | **EU AI Act**, enforcement from **2 Aug 2026** | A **statute** with a conformity-assessment duty | A conformity file for a high-risk system, before deployment |
| **APAC** | **AI Verify** (IMDA Singapore, **Apache-2.0**) plus binding national laws (Korea 22 Jan 2026, Vietnam 1 Mar 2026, Australia's TEQSA plans) | An **open-source test harness**, extensible by plugin | A **test plugin inside the regulator's own harness** — plus the national readiness documents |
| **LATAM** | 🔴 **Nothing regional.** Brazil's bill, Chile's framework, Colombia's CONPES, Mexico's sectoral rules, all at different speeds; **UNESCO** warns institutions use GenAI without policies | An **institutional vacuum** | The institution's own governance layer — there is no external artefact to conform to |

🆕 **APAC's shape is the strongest of the four and it exists in no other region.** When the
regulator publishes its conformance harness under Apache-2.0 **and** ships a plugin kit
(`aiverify-developer-tools`), compliance evidence can be produced **by the regulator's own
instrument** rather than asserted by the vendor — and an education-specific test profile can
be contributed upstream, where it becomes a reference other implementers must meet.

🔴 **LATAM's shape is the weakest, and it is why the governance engagement is the regional
engagement.** With 92% student and 79% faculty adoption and no instrument at any level, the
deliverable is not conformance — it is the institution's first policy.

## 37. Measured by language rather than by region, the LATAM supply gap is absence, not thinness

Five passes of this KB measured "the LATAM shelf" and found repositories at 0–9★, and
described the result as **thin**. All five measured in **Spanish**.

Measured this pass with `total_count`:

| Query | Result |
|---|---|
| `tutor IA educación aprendizaje` (**Spanish**) | **3** — all 0–1★, one of which no longer resolves. **Live shelf: 2.** |
| `tutor inteligência artificial educação aprendizagem` (**Portuguese**) | 🔴 **0** |

**Brazil is the largest education system in Latin America, and the Portuguese-language
permissive AI-tutoring shelf is empty.** Not immature, not low-star: zero. "Thin" was the
wrong word for a condition that is, in half the region, absence — and the word was wrong
because the measurement was monolingual.

**The generalisable lesson is about measurement, not about Brazil.** A region is not a
language, and a supply claim about a region measured in one of its languages is a claim
about that language. This KB's regional vocabulary is correctly closed to five values
(trend hygiene the compiler depends on), but **the probe underneath a regional claim has to
enumerate the region's languages.** APAC is the obvious next case: every APAC measurement in
this KB to date has been in English or Chinese, which leaves Hindi, Bahasa, Japanese, Korean
and Vietnamese unmeasured — and trend 21's mother-tongue finding says that is where the
demand is.

**What Brazil does have** is copyleft and consequential: `yunger7/enem-api` (**GPL-2.0**, an
API over the national university-entrance exam), `portabilis/i-educar` (GPL-2.0, the largest
free school-management platform), `moodle-mod_maici` (GPL-3.0). And exactly one permissive
Portuguese asset: `thiagoluzin/pemara-edu-mira` (**MIT**, 0★) — whose architecture, **school
LAN, offline-capable, optional AI**, is the regionally correct one.

🟢 **For a LATAM-rooted firm this is the cheapest durable position in this entire KB**: at
`total_count: 0` there is no incumbent to displace, and the publishing cost is one competent
MIT component.

## 38. The permissive AI-native frontier is state-funded and non-Western — and its legal holder is harder to identify than its licence

Trend 14 recorded that the permissive shelf stopped being thin, so the differentiator moved.
Trend 15 recorded that *permissive* is a bigger set than three licence names, and that open
core hides inside directories. This pass puts a third fact beside them, and it changes who
a Globant engagement cites as a reference.

**The most capable permissive AI-native education platform available today is Moroccan and
government-funded.** [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
— **BSD-3-Clause**, 108★ / **192 forks** — ships multi-model tutoring, **local RAG**,
voice/video/**3D-avatar** modes and **RBAC**, and serves **Ollama** in the same
configuration surface as hosted APIs. It comes from the **IRF-SIC Laboratory at Ibn Zohr
University, Agadir**, with the **CRMEF Souss-Massa**, funded by Morocco's **Ministry of
Higher Education**, the **Digital Development Agency** and the **CNRST**.

Set that against the rest of the AI-native permissive field as this KB has measured it:
Mentingo (MIT, a Polish consultancy), Coursemology (MIT, NUS Singapore), Sunbird (MIT, an
Indian foundation at national scale), Oppia (Apache-2.0, a US-origin non-profit). 🟢 **Not
one of the leading permissive AI-native education platforms is a Western commercial
product.** They are **universities, foundations, ministries and small consultancies** —
publishing bodies, in the sense of trend 35. The commercial AI-education market is
proprietary; the permissive shelf that market sits on is **public-sector and academic**,
and increasingly **Global South**.

### The consequence for delivery

🟢 **The sovereign deployment stopped being a build and became a configuration.** Every
pattern in this KB from **P4** onward specifies the data-residency stack component by
component — on-prem serving, local retrieval, typed outputs, checkpointed audit trails —
because no platform shipped it. One now does, under a permissive licence, with a
government as its sponsor. **P33** is the shape that follows.

🟢 **And the reference changes.** A public-sector education buyer in EMEA or LATAM asking
whether sovereign AI tutoring is real can be pointed at a **ministry-funded production
project**, not a vendor pilot. That is a materially different procurement conversation.

### The warning that travels with the trend, and it is the new part

🔴 **On a state-funded academic project, the licence is clean and the holder is not.** The
payload reads:

```
Copyright (c) 2023-2025 Mohamed El hajji On behalf of all R2D-dev
All rights reserved.
```

**`R2D-dev` appears in no public artefact of the project** — not the README, not the
documentation, not the search index. The grant is an unambiguous BSD-3-Clause; the entity
holding it cannot be identified. On a redistribution engagement, the holder is the party a
warranty or indemnity question routes to.

This is trend 15's Langfuse lesson generalised. There, the finding was that *the copyright
holder on a dependency can change under you between passes, and no licence probe will flag
it*. Here it is sharper: **the holder can be unidentifiable from the outset**, and a
licence probe reports the component as fully clear. ⚠️ **A licence check is not a
provenance check.** Record **who grants** alongside **what is granted** — for an academic
or ministry-funded project the two are routinely answered by different documents, and
sometimes the first is not answered at all.

🔵 **Three shapes to probe for, now that the pattern is named:** `All rights reserved.`
sitting above a permissive grant (vestigial, but it stops procurement reviewers); a
copyright range that ends before the current year on an actively developed repository; and
a holder named as an organisation that has no web presence. **None of the three invalidates
a grant. All three are questions a client's counsel will ask**, so answer them in the
diligence pack rather than at the meeting.

## Declared gaps — twelfth pass, 2026-10-06

- 🔴 **No public Caliper reference implementation survives in any language.** The eleventh
  pass established that `IMSGlobal/caliper-python` went private on 2023-06-17. This pass
  confirmed it with a second instrument **and found `1EdTech/caliper-php` is gone too**.
  There is no second language to fall back on. **Do not promise Caliper emission without
  pricing a 1EdTech membership or a clean-room build.** The xAPI alternative *is*
  permissive end to end (profile → pipe → store → conformance suite, all MIT/Apache-2.0),
  so this is a standards choice to make at proposal time, not a capability gap.
- 🔴 **No permissive Open Badges server.** `concentricsky/badgr-server` is gone, confirmed
  twice. Trend 8's verifiable-credential half still has no permissive server implementation.
- 🔴 **The Python LTI 1.3 tier is `total_count: 4` and one library deep.** `pylti1.3`
  (MIT, 138★) is the only entry above 1★, with **51 open issues** and no push since
  2024-08-18; the other three are 0–1★. This is now measured exhaustively rather than
  estimated. **Budget a fork from day one** on any engagement where LMS integration is on
  the critical path. The Java side is healthier (`UOC/java-lti-1.3-provider-example`, MIT).
- 🔴 **No permissive Apache-2.0 AI grading tool.** `automated grading rubric LLM education
  license:apache-2.0` → **`total_count: 0`**. The only permissive answer in this KB remains
  `Selleo/mentingo` (MIT). ⚠️ And a Moodle plugin for the function exists and is
  **ungranted** (`alvarogregori/moodle-ai-graded-assignment`) — the supply is there and the
  grant is not.
- 🔴 **`CAHLR/OATutor-Content` is ungranted.** The MIT engine on this KB's core shelf has an
  **unlicensed content repository**. Its problem bank and hint trees — the pedagogy, i.e.
  the asset — cannot be redistributed. **New this pass, and it changes how OATutor should
  be scoped.**
- 🔴 **The Portuguese-language permissive shelf is `total_count: 0`.** Trend 37. **The
  single clearest contribution opportunity in this KB**, and the contribution is a
  published component, not a licence.
- 🔴 **No oral reading fluency product exists.** Re-measured independently: `total_count: 4`,
  the same four repositories as the eleventh pass (`prosody` MIT 0★; `labaaoom` 2017,
  `NOASSERTION`; `ReaDirect-V2` ungranted on branch `deployment/playstore`; `ORF_Calculator_6th`
  0★). **Holds, now reproduced by two passes with the same count.**
- 🔴 **`OpenLiteracy` → `total_count: 0`.** Still no public repository for the Harvard/Ying Xu
  early-reading project funded to close that gap.
- 🔴 **No education test profile exists for AI Verify.** `aiverify-developer-tools` is
  Apache-2.0 and built for exactly this, and nothing education-specific has been contributed.
  **New this pass. The highest-leverage upstream contribution available in APAC**, because it
  lands inside the regulator's own instrument.
- 🔴 **~89 archive addresses remain unrecovered**, down from ~155. The largest untouched
  block is the **~20-server education MCP cluster** — and **2 of the 4 dead addresses found
  this pass were MCP servers**, so expect decay there and record it as supply data rather
  than re-declaring it as absence.
- ⚠️ **Every "ungranted" verdict in this KB older than the twelfth pass is suspect.** The
  13th failure mode — **case-sensitive licence filenames** — turned a **470★ Apache-2.0**
  repository (`openedx/XBlock`, at `LICENSE.TXT`) into a false absence in this pass's own
  first sweep, and earlier passes used lowercase-only probe sets. **A retroactive re-probe
  with case variants is owed**, and it is cheap.
- ⚠️ **A `total_count` is an upper bound, not a census.**
  `junjie1005/Plataforma-IA-Educativa-Rutas-Personalizadas` is listed by the search index
  and unreachable via `git ls-remote`. Counts from the index should be stated as "indexed",
  and existence confirmed separately, before a count is quoted as a measurement.
- ⚠️ **APAC has never been measured in its own languages.** Hindi, Bahasa Indonesia,
  Japanese, Korean and Vietnamese queries have not been run by any pass of this KB, while
  trend 21 says mother-tongue capability is where the demand sits. **Declared as an
  unmeasured region-language pair, not as an absence** — the LATAM lesson of trend 37 is
  precisely that those are different claims.

## Declared gaps — thirteenth pass, 2026-10-06

**The twelfth pass's gaps all stand.** Nothing above was closed by this pass, and the
Caliper, Open Badges, LTI-Python, AI-grading, OATutor-Content, OpenLiteracy, AI-Verify-profile
and oral-reading-fluency gaps should be read forward unchanged. What follows is what this
pass changed, closed or newly measured.

- 🟢 **Partly closed: "APAC has never been measured in its own languages."** This pass ran
  the mandatory queries in **Japanese** and **Korean** — the first pass of this KB to search
  in either. ⚠️ **The result is a negative, and it is a real measurement.** Japanese
  returned **no education-specific asset at all** (the generalist agent layer, same as
  English). Korean returned **5 candidates, 1 licensed** — and the licensed one
  (`HKUDS/ClawTeam`, MIT, 5.5k★) is **software-engineering infrastructure, not education**.
  🔴 **Still unmeasured: Hindi, Bahasa Indonesia, Vietnamese.** The gap narrows to three
  languages and should not be re-declared as five.
- 🟢 **Confirmed on harder evidence: the Portuguese-language permissive shelf.** Trend 37
  was derived from a two-language instrument. This pass searched **in Portuguese** and found
  **4 candidates, 2 licensed (MIT), at 2★ and 0★**
  (`bonafe/inteligencia-aberta`, `armandokeller/SAEP2026-Agentes-IA-e-Ferramentas`). ⚠️ The
  gap is therefore **no longer `total_count: 0`** — it is *"two MIT assets, neither adopted,
  one not education software"*. **The contribution opportunity of P32 stands and is better
  evidenced**: the absence is of *adopted, reusable* components, not of activity.
- 🔴 **NEW — three forges are unreachable, so the non-GitHub supply picture is unmeasured,
  not empty.** `codeberg.org` (the EU sovereignty forge), `gitee.com` (the China-domestic
  forge) and the European Commission's **Joinup / OSOR** catalogue all return **403 at the
  egress proxy**; `arxiv.org` and `alphaxiv.org` are blocked for the third consecutive pass.
  Every licence fact in this KB rests on `raw.githubusercontent.com` because **it is the
  only code-hosting payload this environment can read**. Two named Codeberg education
  projects — **`lerntools`** (German, privacy-focused digital education) and
  **`lmemsm/delightful-educational-games`** — were surfaced and **deliberately left off every
  shelf**, because an unverifiable row is not a finding. ⚠️ **Read this KB as the permissive
  education shelf *on GitHub*.** The EMEA and APAC pictures are understated by an unknown
  amount, and the EU-hosted forge is precisely the blind spot for the sovereignty story this
  KB sells.
- 🔴 **NEW — avatar-based pedagogy has no obtainable permissive implementation.** The
  **VTutor** cluster has three arXiv papers (`2502.04103`, `2505.06676`, `2505.07736`), a
  live demo and a claimed **CC BY 4.0** licence. Reality: the SDK repository
  (`anonymousStars/vtutor-sdk`) has **no licence payload** across 13 filenames and sits under
  a peer-review anonymisation handle, and the organisation the papers name as its home —
  **`VTutorTools`** — **exists with zero public repositories**. ⚠️ **A new failure mode: the
  named home exists and is empty** — distinct from a dead address and from a mislabelled
  licence. And **CC BY 4.0 is a content licence being applied to an SDK**, which is trend 18
  one step further along. 🟢 The capability is reachable today only by composing
  `livekit/livekit` (Apache-2.0) with the avatar mode `open-tutor-ai-CE` already ships under
  BSD-3-Clause — **pattern P33**. VTutor is a **watch item, not a component**.
- 🔴 **Unmoved for the eighth pass: the Arabic ask.** `781991937/TOFAN-AI-2026` was
  re-probed independently this pass on its real default branch across 13 filenames —
  **still no grant**. The Arabic channel went **0 for 3**. ⚠️ Restating this gap in this file
  has not moved it in eight passes. **The action is an issue opened on the repository**, and
  that is what the next pass should carry rather than another re-probe.
- ⚠️ **NEW — the 14th failure mode: a permissive body with no title line.** A licence
  classifier that matches the payload's **heading** reports a bare **BSD-3-Clause** body as
  *unclassified*, and an automated allowlist gate rejects a genuinely permissive component.
  `open-tutor-ai-CE` is the live example; `crewAIInc/crewAI` is the same shape recorded
  earlier as a parenthetical rather than as a property of the instrument. 🟢 **Classify on
  the operative clauses, not the heading.** Together with the 13th failure mode
  (case-sensitive filenames), **the retroactive re-probe already owed should also drop the
  title-line assumption.**
- ⚠️ **NEW — a trending-log entry is not a shelved asset.** The twelfth pass verified
  `open-tutor-ai-CE` correctly and left it only in `repos/trending.md`; for a day, the best
  permissive AI-native platform available to this practice was absent from `agents/top.md`
  and `verticals/solutions.md`. 🟢 **Rule: a payload-verified asset is shelved in the same
  pass that verifies it.** The ~89 unrecovered archive addresses and the **~20-server
  education MCP cluster** should be worked under that rule — **probe, then shelve what the
  probe grants, before moving on.**
- ⚠️ **NEW — the demand side is saturated at this channel's resolution.** All four regions'
  market figures and regulatory instruments were re-run this pass and came back
  **unchanged**. Future passes should spend their budget on **supply** and re-run the demand
  queries only to catch a regime change — the same discipline already applied to the
  generalist GitHub query, which has now returned **zero new rows for nine consecutive
  passes** (fourteen for the infrastructure query).

## 39. Integration coverage follows the higher-education install base, and K-12 administration is an empty tier

Measured this pass for the first time: the number of open-source integration repositories per
education platform, one platform name per query, licences read from payloads.

| Platform | Integration repos | Best permissive, payload-backed server |
|---|---|---|
| Canvas LMS | **117** | MIT, 278★ |
| Moodle | **86** | MIT, 43★ (+ MIT 18★ new) |
| Brightspace / D2L | **23** | MIT, 57★, on npm |
| Google Classroom | **17** | MIT, **6★** |
| Blackboard Learn | **5** | MIT, 2★ |
| Open edX | **1** | AGPL-3.0 |
| 🔴 PowerSchool (US K-12 SIS) | **0** | none |

**Canvas and Moodle hold 203 of the 249 repositories.** Blackboard, with a large global
university estate, has five. Google Classroom — the widest K-12 reach on the table — has
seventeen, and its best *dedicated* server has six stars. PowerSchool measures zero.

🔵 **The trend is not "K-12 is underserved"; it is that supply tracks who can get
credentials.** An individual developer can obtain a Canvas or Moodle token for their own
course in minutes. Nobody can obtain a district student information system token for a
weekend project. So the open-source tier maps almost perfectly onto *self-serve
authentication*, and stops exactly where institutional authorisation begins.

**Three consequences that decide how an engagement is priced.**

1. **In higher education the connector is not differentiating.** It exists, it is MIT, and it
   is duplicated. Sell configuration, governance, pedagogy and the audit trail.
2. **In K-12 administration there is nothing to adopt and nothing to compete with**, and the
   barrier that emptied the tier — institutional credentials — is one an enterprise
   integrator clears as a matter of course. This is the clearest build-versus-adopt signal
   this KB has produced.
3. **The empty tier and the regulated tier are the same tier.** Student records, guardians,
   enrolment, accommodations. The absence of hobbyist code is not an absence of demand; it is
   the regulated surface declining to be built by hobbyists.

⚠️ **The counter-reading to keep in view:** a tier at `total_count: 0` may also be a tier
served entirely by the platform vendor's own paid integrations. Zero open repositories is a
statement about the open-source shelf, not about whether a client currently has an
integration.

## 40. The MCP server has become a product shape, and the catalogue it is listed in is mostly closed

The official MCP Registry was censused first-hand this pass: **11,505 unique servers** across
31,300 version rows. Filtered on education vocabulary with word boundaries: **102 servers, of
which 71 (70%) carry no source repository at all.**

🔵 **The education tier of the registry is a directory of hosted commercial endpoints with
open-source entries mixed in.** Among the 71: **`com.moodlemcp/moodle`** — *"Connect your
Moodle to AI assistants: courses, content, grading"* — a **closed, hosted connector competing
directly with the 86 open repositories** in that platform's tier; `io.cubite/lms` (hosted LMS
with SCORM/xAPI); `com.skillsail/mcp` (SCORM authoring and export); and a dense US
school-data cluster (`ai.edusignal/districts`, `co.schoolscope/mcp`, `ai.sacs/sacs-mcp`,
`com.olyport/nces-education`, `com.olyport/college-scorecard`).

**What changed, stated as a change:** for two years the open-source education stack competed
with proprietary *platforms*. It now also competes with **proprietary connectors to open
platforms** — a thin, high-margin layer sold in front of software the client already hosts
themselves. That is the same layer a Globant deliverable occupies.

**So the differentiator moves to the three things an endpoint cannot offer**, and they are
the three a client cannot get from a service they do not host: **the code**, **deployment
inside their own boundary**, and **the audit trail**. Keep an observability layer in the stack
(Langfuse, MIT outside `ee/`) so the third is a by-product of running rather than a separate
compliance project.

⚠️ **And a vocabulary warning for proposals.** "It's in the MCP registry" now sounds like a
provenance claim and is not one: the registry says nothing about a licence, **one of six
sampled entries points at a repository that no longer exists**, and its `?q=` search
parameter returns HTTP 200 with the unfiltered page. Being listed is marketing; the payload
is provenance.

## 41. What places an asset is the institution, not the language — and the institution's name is searchable in English

Trend 37 concluded that measured by language rather than region, the LATAM supply gap is
absence rather than thinness. The thirteenth pass then tested language directly — Japanese,
Korean, Arabic, Portuguese — and got **3 licensed finds from 12 candidates (25%), only one of
them education software**, concluding that language was the wrong variable.

This pass replaced the variable with the **name of the platform the asset integrates with**,
run one name at a time: **16 licensed from 20 candidates (80%), and all 16 are education
software.**

🟢 **Two properties make this channel structurally better, not just luckier.**

- **It cannot drift.** Topic queries, star-sorted queries and language queries all collapse
  into the generalist agent layer — this KB has recorded that collapse 45 times, and ten
  consecutive passes of the mandatory generalist query have yielded zero repositories. A
  platform name cannot collapse: `brightspace` returns 23 repositories and every one is about
  Brightspace.
- **It places the finding by region for free**, because a platform is an institution in a
  country. Skolverket places to Sweden, Smartschool to Belgium, KUPID to Korea, NTU COOL to
  Taiwan, SLIIT to Sri Lanka, VGU to Vietnam. No inference step, so no inferred-data error.

**The sharp version of the correction:** the Korean asset `SonAIengine/ku-portal-mcp` (MIT,
13★) already existed when the Korean-language query was run, and that query did not find it.
The platform name **KUPID** did. So the finding is not that non-English search is useless —
it is that **the institution is the unit of placement, and institutions are usually
searchable in English even when their README is not.**

⚠️ **The method caveat that cost this pass a region.** The channel works only with one
platform name per query. `sigaa OR suap OR siga mcp server` — three Brazilian
university-system names — returned **`total_count: 160,659`** and the generalist layer,
because Boolean `OR` lets the highest-volume terms (`mcp`, `server`) dominate. **LATAM's
platform tier therefore remains unmeasured**, and that is recorded as a gap rather than as a
result.

## 42. The national curriculum is becoming a callable API — and the wrapper's licence is not the data's licence

New this pass, and it is a shape rather than a single asset: a **state education authority's
own API estate, wrapped thinly under a permissive licence and published as an agent-callable
server.**

| Authority | Wrapper | Licence (payload read) |
|---|---|---|
| **Skolverket** (Sweden) — Läroplan/syllabus API, Skolenhetsregistret school-unit register, Planned Educations | [isakskogstad/Skolverket-MCP](https://github.com/isakskogstad/Skolverket-MCP), 12★ | 🟢 **MIT**, 1,093 B |
| **Udir** (Norway) — school (NSR) and kindergarten (NBR) registries | [3121n/nor-data-udir-mcp](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **none**, 0 of 20 filenames |

🔵 **Why this matters more than its star counts suggest.** In every regime this KB tracks,
*"aligned to the national curriculum"* is a procurement requirement, and it has been a
**consulting deliverable** — a human reads the syllabus and writes a mapping that is stale on
the day it ships. Where the authority publishes an API and a permissive wrapper exists, the
alignment becomes **a tool call inside the product**, re-evaluated on every run. It is the
input trend 13 implied and pattern P15 lacked.

⚠️ **And it comes with a licensing distinction this KB has not had to make before.**
Skolverket-MCP's copyright line reads **"Skolverket Syllabus MCP Contributors"**, *not the
agency*. So:

- the **MIT grant covers the wrapper** — safe to fork, modify, ship, rebrand;
- the **agency's own terms govern the data** the wrapper returns, and the MIT licence says
  nothing whatsoever about them;
- a proposal that cites "MIT" for a national-curriculum capability is **citing the connector
  and implying the corpus**. Trend 22 priced the corpus; this is the same error arriving
  through a cleaner-looking door.

🟢 **The generalisable move, and nothing about it is Nordic.** Check whether the target
country's education authority publishes an open API; check whether a permissive wrapper
exists; expect to write one. Writing a thin wrapper over a public national API is small,
well-bounded and highly reusable — and **Udir is the proof that the gap is normal**: same
region, same quality of public data, no grant at all.

## Declared gaps — fourteenth pass, 2026-10-06

**Measured and genuinely missing, after first-hand probing this pass.**

1. 🔴 **LATAM's platform-integration tier is unmeasured, by this pass's own error.** SIGAA
   and SUAP were OR'd into one query, which collapsed into the generalist layer
   (`total_count: 160,659`). The only LATAM asset found, `vnschneider/suap-mcp`, has **no
   licence payload** and declares **AGPL-3.0-or-later** in `pyproject.toml` — no grant today,
   and a copyleft constraint if one ever lands. **Next pass: SIGAA and SUAP, one name per
   query.**
2. 🔴 **Zero of the MCP Registry's 102 education servers are LATAM-placed.** Fourth
   independent instrument to return absence rather than thinness for the region. Consistent
   with trend 37.
3. 🔴 **PowerSchool integration tier: `total_count: 0`.** No open-source asset of any licence
   for the dominant US K-12 student information system. This is a build, and the gap is
   structural (credentials), not temporal.
4. ⚠️ **The registry census is incomplete and is reported as a floor.** The page loop ended
   on an empty body at page 313 (31,300 records → 11,505 unique servers). The true index size
   is unknown; resume from the cursor before quoting any denominator from it.
5. ⚠️ **Seven assets are declared-and-ungranted, one of them at 103★.**
   `DMontgomery40/mcp-canvas-lms` — second-highest-starred Canvas MCP server on GitHub —
   ships a `package.json` MIT field and no licence file. Six others the same (five MIT, one
   ISC); one declares AGPL-3.0. **One commit each would unblock them**, and asking is cheaper
   than rebuilding.
6. ⚠️ **No permissive asset found this pass addresses accommodations as a first-class
   surface.** `GarphenGate/moltline-mcp` (MIT) is the only one that even names it among its
   eight skills. Accommodations are a legal requirement in both US and EU school systems, and
   the tier is effectively empty.
7. 🔵 **Negative method result, recorded so the next twelve passes do not re-buy it:** the
   licence-filename **case-variant ladder** (19 extra requests per repository) paid out
   **zero times across 98 repositories** — all 76 payloads sat at plain `LICENSE`. Keep it
   for a single high-value asset whose absence would change a recommendation; do not pay it
   across a census.

## 33. The licence has stopped being the last gate — the access grant is

Every licensing trend in this file (23, 24, 25, 29) answers one question: **may we copy and
redistribute this code?** This pass found the first component in this KB's history where the
answer is an unqualified **yes** and the component still cannot be shipped.

[`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) is MIT,
payload read, 20 tools over the Infinite Campus student information system. Its own README
quotes the vendor's Terms of Use:

> Users may not access, use, or search the Services by any means other than our publicly
> supported interfaces (for example, scraping or using the content to train artificial
> intelligence software).

…then states that the server calls non-public mobile endpoints and that **"IC may treat this
as a ToS violation"**, restricts itself to personal parent/student use, forbids bulk
extraction and model training, and invokes **FERPA and COPPA** on its output.

**Two grants are needed to ship an integration, and only one of them is in the repository:**

| Grant | Who gives it | Where it lives | What a licence audit sees |
|---|---|---|---|
| **Copyright** — may we copy the code? | the maintainer | `LICENSE` | 🟢 everything |
| **Access** — may we call the system? | the **platform vendor** | the vendor's ToU, and the institution's contract | 🔴 **nothing** |

🔴 **This is why the trend matters beyond one repository.** The whole SIS integration tier —
24 permissive assets across seven countries, found this pass — is built on unofficial access
and says so in its own words: *"web scraping"* (`GeovaneSchmitz/sigaa-api`), *"unofficial…
at your own risk"* (`kc0506/ntucool`), repository topic `reverse-engineering`
(`elisaado/somtoday-api-docs`). The licences are clean. The access is not granted by anyone.

⚠️ **The clause to watch is the AI-specific one.** Infinite Campus's ToU does not merely
forbid scraping; it names **"using the content to train artificial intelligence
software"** as a prohibited means of access. This KB has **one** verified instance of that
clause, so it is recorded as a data point and **not** yet asserted as an industry-wide
pattern — but it is the clause that would, if it spreads, make the distinction between
"integrate with" and "train on" a contractual line rather than an ethical one. **Next pass
should read the ToU of PowerSchool, Canvas/Instructure, Moodle-hosting and Google Classroom
and establish whether this is one vendor or the sector.**

🟢 **What to do about it, commercially.** The constraint is not a dead end, it is a scoping
rule: a client engagement that touches a proprietary SIS must budget for the **vendor's
official API entitlement** before any agent work is scoped. Both US K-12 vendors publish
OneRoster endpoints, and this KB's interoperability tier already carries permissive
OneRoster and Ed-Fi implementations. **Prototype on the community client, ship on the
official API.** Operationalised as **P25** and gated by **P26**.

## 34. Permissive supply collects at the edges of platforms it is not allowed to fork

This pass measured both halves of the student information system space and the result is a
structural law, not a coincidence:

| Layer | Assets found | Licence set |
|---|---|---|
| **SIS platforms** (deployable products) | 5, with 1,600+ ★ and 1,000+ forks between them | 🔴 **{GPL-2.0, GPL-3.0}** + one ungranted. **Zero MIT. Zero Apache. Zero BSD.** |
| **SIS clients, wrappers, MCP servers, extensions** | 36 addresses, 24 permissive | 🟢 **22 MIT · 1 Apache-2.0 · 1 BSD-2 · 1 WTFPL** |

🔵 **You cannot fork an open SIS permissively, so all the permissive work happens around it.**
The MIT supply is clients, timetable decoders, MCP servers and browser extensions —
everything that *talks to* a student information system without *being* one. The same shape
holds for learning platforms, where Moodle (GPL-3.0) and Open edX (AGPL-3.0) are surrounded
by an MIT MCP cluster this KB has censused at 98 addresses.

**Three consequences for how an engagement is shaped:**

1. 🟢 **The permissive shelf is reliably an *integration* shelf.** When this KB reports a
   deep permissive tier, expect side-cars and clients, not a product you can brand and
   resell. The exceptions are rare enough to be named individually (Mentingo, OpenMAIC,
   Coursemology, Sunbird).
2. ⚠️ **"Is there an open-source X?" and "is there a permissive open-source X?" have
   different answers at the platform layer in every category this KB has measured.** Ask the
   second question.
3. 🔵 **The copyleft platform is often still the right answer** — it is simply a different
   engagement: deploy-and-extend under GPL obligations, or take the LGPL-3.0 middle path
   (OpenEduCat on Odoo) where a module can stay proprietary. What it is not is a white-label
   product.

## Declared gaps — fifteenth pass, 2026-10-06

Searched this pass; stated so they can be falsified rather than left as silence.

1. 🔴 **No permissive SIS *platform* exists.** Five measured, all GPL-2.0/GPL-3.0 or
   ungranted. If a client needs a brandable, resellable student information system, **there
   is nothing to start from** and this KB has now looked properly.
2. 🔴 **The UK has no permissive MIS integration layer.** `bromcom` 36 repositories (nothing
   above 2★), `"arbor mis"` 7 (nothing above 0★), `"capita sims" school` **0**. Against the
   strongest government MIT estate in this KB. **A clean build opportunity, stated as a gap
   rather than as an absence of evidence.**
3. 🔴 **No Japan-, Korea-, Australia- or India-placed SIS integration asset was found.**
   India's `diksha` is a name collision returning 2,864 irrelevant repositories;
   `samarth ugc` returned 0. The Australia probe (`sentral compass school australia api`)
   was OR'd and therefore weak — **re-run one name at a time before trusting this gap.**
   The entire APAC tier found this pass is one Taiwanese university.
4. ⚠️ **The ministry tier is still unmeasured.** Skolverket (SE) is shelved from the
   fourteenth pass, but Udir (NO), Eduscol (FR), INEP/Censo Escolar (BR), MEXT (JP) and the
   Gulf ministries were not queried by name. **This is the fourteenth pass's instruction 2
   only half-executed — the SIS half is done, the ministry half is not.**
5. ⚠️ **Whether the anti-AI-training ToU clause is one vendor or the sector is unknown.**
   One verified instance (Infinite Campus). Trend 33 names the four ToUs to read next.
6. ⚠️ **The MCP Registry's true index size remains unestablished**, but for a better-understood
   reason than before: the empty page that stopped the fourteenth pass at 31,300 records is a
   **transient fault, not an end-of-index marker** — re-requesting the same cursor returned
   100 servers on 3 of 3 attempts. Any denominator quoted from a walk without retries is a
   floor, not a size. See `repos/trending.md`, fifteenth pass.
7. 🔵 **Negative method result, priced so it is not re-bought:** `curl -sI` against
   `github.com` returns **HTTP 403 for every repository** through this environment's egress
   proxy — 36 of 36, including repositories whose payloads were then read successfully. A
   uniform response across all inputs carries no information. **Use `git ls-remote --symref`
   for existence and `raw.githubusercontent.com` for payloads.**
8. 🟢 **Positive method result worth adopting ahead of the filename ladder:** read the
   **README's own licence link**. `OS4ED/openSIS-Classic` keeps its GPL-2.0 text at
   `docs/License.txt` — mixed case, in a subdirectory, with a byte-order mark — which no
   filename ladder in this KB would have found. The README said where it was, in one request.
