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
