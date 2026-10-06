---
industry: education
region: Global
updated: 2026-10-06
---

# Compose Patterns — Education

Concrete recipes built only from repos verified in `agents/top.md`,
`repos/foundations.md` and `verticals/solutions.md` on 2026-10-06. Every
component names its license, because in this industry the license decides the
architecture.

**The rule behind patterns P1–P6:** the education platform shelf is mostly
copyleft (Moodle GPL-3.0, Open edX / Canvas / Frappe AGPL-3.0). AI built as an
in-tree plugin inherits that license; the same AI built as an external service
over LTI 1.3 or MCP stays permissive. Globant's reusable IP lives in the
side-car.

---

## P1 — LTI + MCP side-car tutor (the default engagement shape)

**Use when:** the client already runs an LMS, which is almost always.
**Outcome:** AI tutoring inside the existing LMS, with Globant's code permissive.

**Wiring:**
1. Leave the LMS untouched — Moodle (GPL-3.0), Canvas (AGPL-3.0) or Open edX
   (AGPL-3.0). No fork, no in-tree plugin.
2. Register a tool provider with
   [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP)
   (Apache-2.0) for launch, identity and grade passback.
3. Expose LMS data to the agent over MCP:
   [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT,
   up to 103 tools, 8 agent skills) for Canvas, or
   [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server)
   (MIT) for Moodle.
4. Tutoring engine: [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
   (Apache-2.0) via its WebSocket API or Python SDK, one TutorBot workspace per
   learner so memory is per-student.
5. Orchestrate with [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
   (MIT); type every boundary with [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (MIT).
6. Serve models through [ollama/ollama](https://github.com/ollama/ollama) (MIT)
   when residency is required, or a commercial API when it is not.

**Why this order:** step 1 is what keeps steps 4–6 permissive. Reverse it — write
a Moodle plugin — and the tutor becomes GPL-3.0 and stops being reusable IP.

**Watch:** LTI grade passback is a consequential decision path. Put the P4
human-oversight gate in front of it before any grade is written back.
**Effort:** 6–8 weeks for a single-LMS pilot.

---

## P2 — Curriculum ingestion → item bank

**Use when:** the client has curriculum in PDFs and textbooks and needs
assessment items or lesson content at volume.

**Wiring:**
1. [opendatalab/MinerU](https://github.com/opendatalab/MinerU) (Apache-2.0)
   parses PDFs, textbooks and scanned material into structured text.
2. [satvik314/educhain](https://github.com/satvik314/educhain) (MIT) generates
   MCQs, open-ended items, lesson plans and flashcards from that text.
3. Validate every generated item against a schema with pydantic-ai (MIT) —
   reject rather than repair malformed items.
4. Route items into the LMS question bank: Moodle qbank, or Open edX via
   [overhangio/tutor](https://github.com/overhangio/tutor) (AGPL-3.0) for
   deployment.
5. **Human review before any item goes live.** Not optional — see below.

**Hard constraint:** there is no permissive open source auto-grader (declared gap,
re-searched 2026-10-06). Generate items and feedback automatically; keep scoring
human-gated. This also satisfies Oklahoma/Maryland human-oversight statutes and
EU AI Act Annex III.
**Effort:** 4–6 weeks.

---

## P3 — Mastery-tracked adaptive practice

**Use when:** the client needs adaptive sequencing *and* has to justify why a
learner was judged to have mastered something.

**Wiring:**
1. [CAHLR/OATutor](https://github.com/CAHLR/OATutor) (MIT) supplies Bayesian
   Knowledge Tracing — an inspectable, parameterised mastery estimate per skill,
   published at CHI '23 with follow-up in PLOS ONE.
2. LangGraph (MIT) runs the per-skill state machine: practice → BKT update →
   branch to remediation, hinting or advance.
3. DeepTutor (Apache-2.0) generates hints and explanations at the remediation
   node; its Capabilities layer is the right place for a multi-turn
   remediation dialogue.
4. Persist BKT parameters and LangGraph checkpoints together — that pairing *is*
   the audit record of why the system decided what it decided.

**Why BKT rather than asking a model:** under EU AI Act high-risk assessment
rules and Brazil's PL 2.338 risk tiers, "the LLM said so" is not a defensible
mastery claim. A BKT posterior with known priors is.
**Effort:** 6–10 weeks.

---

## P4 — EMEA sovereign, Annex III-ready deployment

**Use when:** EU client, assessment or access decisions in scope. The AI Act
defers stand-alone high-risk obligations to **2 December 2027** — that deferral
is the design window, not a reason to wait.

**Wiring:**
1. Inference stays in-region: ollama (MIT) or vLLM on-prem, open-weight models
   (Llama, Mistral). No student data to a third-party API.
2. pydantic-ai (MIT) for typed, schema-validated outputs at every boundary —
   structured decisions are auditable, prose is not.
3. LangGraph (MIT) checkpoints as the immutable decision trail: inputs, model
   version, intermediate state, output, timestamp.
4. OATutor (MIT) BKT for any mastery or progression claim, so the assessment
   logic is explainable independently of the model.
5. **A human-oversight gate as a required graph node** before any grade, access
   or progression decision is committed. The gate records who approved what.
6. [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core)
   (Apache-2.0) if competency claims leave the institution.

**Deliverable is two things:** the system, and the Annex III conformity
documentation it generates. Sell both.
**Effort:** 10–14 weeks. Reuses directly for Brazil PL 2.338 readiness.

---

## P5 — Offline-first equity deployment (LATAM and low-connectivity)

**Use when:** connectivity, device or budget constraints are real — which per
CEPAL covers much of LATAM, where >50% of Chilean and Brazilian teachers already
use AI but <10% of institutions have the capacity to support it.

**Wiring — a fully MIT stack, no copyleft anywhere:**
1. [LearningEquality/kolibri](https://github.com/LearningEquality/kolibri) (MIT)
   as the platform; runs offline on a classroom server or a single laptop.
2. [LearningEquality/studio](https://github.com/LearningEquality/studio) (MIT)
   for curriculum authoring and channel curation.
3. [LearningEquality/ricecooker](https://github.com/LearningEquality/ricecooker)
   (MIT) to package existing client or ministry content into Kolibri channels.
4. ollama (MIT) with a small quantised model on the local server for offline
   tutoring and question answering — no egress, no per-token cost.
5. Sync opportunistically when connectivity appears; never assume it.
6. For Spanish-first public-sector clients that require a conventional LMS
   instead, substitute [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms)
   (GPL-3.0) — accepting the copyleft, and keeping the AI as a P1 side-car.

**Positioning:** pair with UNESCO's LAC AI-in-Education Observatory (launched
14 April 2026) and lead with teacher enablement and governance, which is the
measured gap, rather than with software alone.
**Effort:** 4–6 weeks for a pilot site; the content pipeline dominates.

---

## P6 — Client capability build (enablement)

**Use when:** the client's own staff must own the system afterwards — which is
how an engagement becomes a programme rather than a project.

**Wiring:**
1. [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
   (MIT, 18 lessons) as the core track; its samples target MAF, which is the
   framework you want taught.
2. [huggingface/agents-course](https://github.com/huggingface/agents-course)
   (Apache-2.0) as the second track for framework-agnostic grounding, and
   [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)
   (MIT) for a cohort-tested syllabus.
3. [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)
   (MIT) as the prerequisite for non-AI staff;
   [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
   (Apache-2.0) or [mlabonne/llm-course](https://github.com/mlabonne/llm-course)
   (Apache-2.0) for the deep track.
4. [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub)
   (BSD-3-Clause) to give the whole cohort an identical environment on day one.
5. Teach on **Microsoft Agent Framework (MIT)**, not AutoGen — AutoGen is in
   maintenance mode and will not receive new features.

**Effort:** 3–4 weeks to stand up, then runs continuously.

---

## P7 — Admin automation on an LGPL platform (the module, not the side-car)

**Added 2026-10-06.** The first six patterns all route around copyleft by building
a side-car. On the *administrative* shelf that is not forced, and routing around a
constraint that is not there costs you integration depth for nothing.

**Use when:** the client's pain is administrative — admissions triage, enrolment,
fee reconciliation, attendance follow-up, exam scheduling — rather than tutoring,
and they do not already run a committed SIS.

**Outcome:** AI-assisted administration inside the ERP, with Globant's module able
to stay proprietary.

**Wiring:**
1. Platform: [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp)
   (**LGPL-3.0**, 884★, 775 forks, v19.0, Odoo/Python). Admissions, student info,
   courses, exams, finance, attendance, library, HR already exist — do not rebuild
   them.
2. **Respect the LGPL boundary, because it is what buys you the proprietary
   option.** Do not fork OpenEduCat's own files: changes to them stay LGPL-3.0.
   Build a *separate* Odoo module that links against it through documented
   interfaces. That module can be proprietary.
3. Agent layer in the module: [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
   (MIT) for typed, validated outputs on every record it writes, orchestrated with
   [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) (MIT) so each
   administrative decision carries a checkpointed trail.
4. Documents in: [opendatalab/MinerU](https://github.com/opendatalab/MinerU)
   (Apache-2.0) for transcripts, certificates and application attachments.
5. Inference: [ollama/ollama](https://github.com/ollama/ollama) (MIT) on-prem —
   admissions data is exactly the category California AB 1159, EU residency
   practice and India's DPDP constrain.
6. If the client needs admin automation with **zero** copyleft exposure anywhere
   in the tree, substitute [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework)
   (Apache-2.0, Java) and accept that you are building the education domain model
   yourself.

**Watch:** admissions is an Annex III high-risk use case under the EU AI Act —
"AI used in education access" is named explicitly. An admissions agent is a
high-risk system, not back-office convenience. Put the P4 oversight gate on any
admit/reject path, and keep the agent on triage, completeness checking and
summarisation rather than the decision.

**Watch also:** if the client already runs an SIS, do not migrate them. Gibbon
(GPL-3.0), RosarioSIS (GPL-2.0) and openSIS (GPL-2.0) are all copyleft, so there
P1's side-car shape returns. RosarioSIS being GPL-**2.0** also means it is not
license-compatible with GPL-3.0-only code — check before combining anything.
**Effort:** 5–7 weeks for a single-process pilot (admissions triage is the usual
first one).

---

## P8 — Course materials → source-backed Agent Skills

**Added 2026-10-06.** P2 turns curriculum into an *item bank*. This turns it into
**portable agent skills**, which is a different and more reusable asset: the
institution's own pedagogy, loadable by any of the 40+ MCP-speaking clients.

**Use when:** the client's differentiator is *how they teach* — a methodology, a
sequencing, a body of worked examples — and it currently lives only in lecture
recordings, slide decks and a few senior instructors' heads.

**Outcome:** the institution's teaching method as versioned, source-attributed
skills, usable inside the LMS and outside it.

**Wiring:**
1. Capture: [opencast/opencast](https://github.com/opencast/opencast) (ECL-2.0,
   permissive) for the lecture corpus if it is not already recorded.
2. Structure: [opendatalab/MinerU](https://github.com/opendatalab/MinerU)
   (Apache-2.0) for PDFs, textbooks and scanned handouts.
3. Distil: [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill)
   (**Apache-2.0**, 448★, Python) — videos, PDFs, transcripts and notes into
   source-backed teacher Agent Skills. It preserves source attribution, extracts
   instructor methodology and orders practice tasks progressively, which is
   precisely the part a generic summariser throws away.
4. Deliver into the LMS: the 8 agent skills already shipped by
   [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT,
   up to 103 tools, v1.13.0) are the reference shape and the delivery path for
   Canvas; [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server)
   (MIT) for Moodle.
5. Deliver offline too: package the same distilled material into Kolibri channels
   with [LearningEquality/ricecooker](https://github.com/LearningEquality/ricecooker)
   (MIT) → [LearningEquality/kolibri](https://github.com/LearningEquality/kolibri)
   (MIT). One distillation, two delivery modes — this is what makes the pattern pay
   in LATAM and low-connectivity contexts.
6. Local authoring assist: [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED)
   (MIT, 60★) for local-first lesson drafting, so draft materials never leave the
   institution.

**Why source-backed is the whole point:** provenance back to the instructor's own
materials is defensible under the high-risk regimes in a way a fine-tune is not,
and it is what lets a faculty member accept the output. A skill that cannot cite
its source will not survive faculty review.

**Watch:** IP and consent. Lecture recordings carry instructor performance rights
and student voices and faces; third-party course content carries licensing terms.
Settle who owns a distilled skill — institution, instructor, or Globant — in the
SOW, before the first ingest. This is also the LATAM depth play: with 92% of
students and 79% of faculty already using AI but 88% of faculty engaging only
shallowly, the gap is integration into real teaching practice, which is exactly
what a skill built from their own course does.
**Effort:** 4–6 weeks for one programme; the second programme is roughly half,
because the pipeline is reused and only the corpus changes.

---

## P9 — Curriculum-mandate delivery with age-gated capability (UAE / China shape)

Added in the third pass of 2026-10-06. This is the only pattern in this KB driven
by a **funded obligation** rather than by a constraint, and the only one where the
regulator has specified the access-control model for you.

**Use when:** a ministry or provincial authority has made AI instruction
compulsory and the institution has to deliver curriculum-aligned material and
trained teachers against a deadline. Live today in the **UAE** (Cabinet, May 2025 —
KG to Grade 12 from the 2025–26 school year, seven content areas, inside an
existing subject with no added school hours, specially trained teachers) and in
**China at provincial level** (Beijing: ≥8 hours a year in every primary and
secondary school from 1 September 2025; Guangdong: 6 hours a year in lower grades
rising to one hour a fortnight in grades 10–11).

**Outcome:** curriculum-aligned content across the mandated areas, a teacher
enablement track, and a system that **structurally cannot** give a younger cohort
unmediated generative AI.

**Wiring:**
1. **Ingest the official curriculum framework first, not the textbooks.**
   [opendatalab/MinerU](https://github.com/opendatalab/MinerU) (Apache-2.0) over
   the ministry's published framework — for the UAE, the seven areas: foundational
   concepts, data and algorithms, software use, ethical awareness, real-world
   applications, innovation and project design, and policies and community
   engagement. The framework is the schema everything else is checked against.
2. **Generate against the framework, with the area as a required field.**
   [satvik314/educhain](https://github.com/satvik314/educhain) (MIT) for items,
   lesson plans and flashcards;
   [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (MIT) to make
   `curriculum_area`, `grade_band` and `source_reference` **non-optional** on every
   generated artefact. An item that cannot name its area and grade band is not
   deliverable, and a typed boundary is what makes that a build error rather than a
   review finding.
3. **Produce the ethics and civics material deliberately.** Two of the UAE's seven
   areas — ethical awareness, and policies and community engagement — are not
   technique. Generic AI-literacy content does not cover them, and they need
   age-appropriate treatment per grade band. Budget for them as their own content
   stream; this is the part a competitor's pipeline will skip.
4. **Build the age gate as a routing layer, not a prompt instruction.**
   [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) (MIT) with
   the cohort's grade band as graph state, and **distinct graphs per band**:
   - primary → **no independent generative-AI path exists in the graph.** The pupil
     reaches teacher-mediated and pre-generated material only. Beijing bars
     independent generative-AI use by primary pupils, so this must be a structural
     absence, not a refusal the model is asked to perform;
   - secondary lower → generated content with teacher review before release;
   - secondary upper → interactive tutoring, still with the teacher as approver on
     anything that lands in a grade.
   A capability tier the system cannot exceed is auditable; a system prompt asking
   it not to is not. **No permissive component implements this** — see the declared
   gap in `intel/trends.md` — so it is yours to build, and it is the reusable part.
5. **Protect the teacher's role in the design.** China prohibits teachers from
   substituting AI for core instructional duties, so the teacher-facing surface is
   preparation, differentiation and review — never autonomous delivery to the class.
   [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill)
   (Apache-2.0) to turn the ministry framework and the teacher's own materials into
   source-backed skills is the right shape here: it amplifies the teacher's method
   instead of replacing it.
6. **Run inference in-country.** [ollama/ollama](https://github.com/ollama/ollama)
   (MIT) or vLLM. For the UAE and China alike, assume the student-data boundary is
   non-negotiable and that this is also what makes the deployment affordable at
   provincial scale.
7. **Trace everything.** [langfuse/langfuse](https://github.com/langfuse/langfuse)
   (MIT outside `ee/`) on every call. The mandate will be inspected, and per-call
   cost, latency and output is the evidence. Exclude `ee/` from any vendored copy.
8. **Deliver the teacher track as a product, not a slide deck.** The UAE mandate
   funds "specially trained teachers".
   [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
   (MIT) and [huggingface/agents-course](https://github.com/huggingface/agents-course)
   (Apache-2.0) as the base; localise it and map each module to the mandated areas
   so the client can evidence coverage.

**Why this order:** the framework in step 1 is what makes steps 2 and 3 auditable,
and the graph topology in step 4 is what makes the age restriction a property of
the system rather than a promise about it. Reverse steps 4 and 2 — generate first,
gate later — and you end up filtering outputs at runtime, which is both weaker and
harder to evidence.

**Watch:** the mandates are **provincial in China**, so hour counts and grade
boundaries differ between Beijing and Guangdong. Parameterise the hour allocation
and the grade bands; do not hard-code one province's numbers. And verify the
current framework text with the client's ministry contact — a curriculum mandate is
revised more often than a statute.

**Reuse:** build this once and it satisfies the oversight requirements of EU AI Act
Annex III, the Oklahoma and Maryland human-oversight statutes, Korea's high-impact
classification and Singapore's IMDA agentic framework, because **Beijing's
restriction is the strictest of them.** The age-gating layer is the genuinely novel
asset — nothing permissive implements it.
**Effort:** 10–14 weeks for one grade band across the mandated areas, plus 3–4
weeks per additional band once the graph topology exists.

---

## P10 — Enterprise L&D on a permissive platform (fork it, brand it, resell it)

Added in the third pass of 2026-10-06. Every other platform pattern in this KB
assumes the platform is copyleft and routes around it. This one does not, and the
commercial shape is different as a result.

**Use when:** the client is a corporate L&D, onboarding or compliance-training
buyer — not an academic institution — and wants a platform they own rather than a
per-seat subscription.

**Outcome:** a white-labelled, self-hosted, AI-native LMS. Globant's extensions are
MIT, the platform is MIT, and **the deliverable is the whole product** rather than a
side-car attached to someone else's.

**Wiring:**
1. **Fork [Selleo/mentingo](https://github.com/Selleo/mentingo) (MIT).** 91★, 29
   forks, TypeScript, maintained by Selleo (Poland). Its README states the intent
   directly: *"MIT — modify, white-label and resell, no copyleft obligation."* There
   is no copyleft to architect around, so **do not build a side-car here** — that is
   P1's answer to a problem this platform does not have.
2. **Keep its stack and extend it.** PostgreSQL 16 +
   [pgvector/pgvector](https://github.com/pgvector/pgvector) (PostgreSQL License)
   for retrieval, Redis, S3-compatible storage, Node.js 22+. One database, no
   separate vector store.
3. **Swap the model layer for residency.** It ships Vercel AI SDK + OpenAI and
   LangChain; replace with [ollama/ollama](https://github.com/ollama/ollama) (MIT)
   or vLLM where the client's data cannot leave. This is the one substitution the
   architecture expects.
4. **Keep Langfuse and treat it as the compliance artefact.**
   [langfuse/langfuse](https://github.com/langfuse/langfuse) is already wired in and
   traces every call's cost, latency and output. Exclude `ee/`, `web/src/ee/` and
   `worker/src/ee/` from the vendored copy — those directories are **not** MIT.
5. **Use the automated grading where it belongs, and gate it where it does not.**
   Mentingo grades open-ended behavioural and problem-solving answers automatically
   with actionable feedback. For formative practice, ship it. For anything that
   gates certification, promotion, pay or a regulatory qualification, **put a human
   approval checkpoint in front of it** — the licence changed, the oversight
   obligation did not.
6. **Lean on the voice layer for compliance training.**
   [livekit/livekit](https://github.com/livekit/livekit) (Apache-2.0) under
   Mentingo's AI mentor runs real-time role-play for sales, compliance and
   customer-support scenarios and scores the attempt. Role-play with a scored
   transcript is a far better compliance-evidence artefact than a completion tick.
7. **Integrate rather than replace, via SCORM 1.2 export.** Mentingo exports SCORM
   1.2 and ships an OpenAPI/Swagger spec with a generated typed client. When the
   client already runs an incumbent LMS, author in Mentingo and **feed** the
   incumbent — a much easier sale than a platform migration.
8. **Multi-tenancy is already there.** It is multi-tenant and white-label out of the
   box, which is what makes one build serviceable across several client brands.

**Why this order:** step 1 is the whole pattern. The instinct this KB has trained —
never touch the platform, always build the side-car — is correct against Moodle,
Canvas and Open edX and **wrong here**, and following it costs integration depth
for no legal benefit.

**Watch:** Mentingo is an **L&D** product. No LTI 1.3, no SIS integration, no
gradebook semantics for credit-bearing courses, no institutional reporting; SCORM
1.2 is the L&D interchange format, not an academic one. **Do not sell it to a
university as a platform** — there it is a reference implementation and a component
donor. Also note it is 91★ and single-company-maintained: budget for carrying your
own fork, and read the upstream commit history before committing a client to it.

**Effort:** 6–8 weeks to a branded pilot with the model layer swapped; 10–12 weeks
with in-region inference and a human-approval gate on certification paths.

---

## Pattern selection

| Situation | Pattern |
|---|---|
| Client already has an LMS | P1 |
| Needs content or item volume from existing curriculum | P2 |
| Must justify mastery/progression decisions | P3 |
| EU client, assessment in scope | P4 (P1 for the integration) |
| Connectivity/budget constrained, equity mandate | P5 |
| Client staff must own it afterwards | P6, alongside any other |
| Pain is administrative, no committed SIS yet | **P7** (module on LGPL-3.0 OpenEduCat) |
| Pain is administrative, SIS already committed | P1's side-car shape — Gibbon/RosarioSIS/openSIS are all copyleft |
| Differentiator is *how they teach*, locked in recordings and senior staff | **P8** |
| LATAM higher ed: adoption already universal, integration shallow | **P8** for depth, P6 for faculty capability |
| Singapore/APAC agentic-governance requirement in scope | any pattern, built to the IMDA four dimensions (see `intel/trends.md` §11) |
| Ministry/province has **mandated** AI instruction (UAE, Beijing, Guangdong) | **P9** — the only pattern driven by a funded obligation rather than a constraint |
| Cohort includes primary-age pupils, or China is in scope | **P9**, for the age-gating graph specifically — a prompt instruction will not do |
| Corporate **L&D** buyer who wants to own the platform | **P10** (fork Mentingo, MIT) — explicitly *not* P1 |
| Academic institution, however L&D-shaped the ask sounds | P1; Mentingo is a component donor here, not a platform |
| Needs spaced repetition / retention reached by an agent | `ankimcp/anki-mcp-server` (MIT, 53 tools) inside P1, or OpenTutor (MIT) for FSRS 4.5 built in |

## Anti-patterns

- **Writing an in-tree LMS plugin for reusable IP.** It inherits GPL-3.0/AGPL-3.0.
  Use P1.
- **Promising autonomous grading.** Amended 2026-10-06: a permissive auto-grader
  now *does* exist — `Selleo/mentingo` (MIT) grades open-ended behavioural and
  problem-solving answers — but **only for corporate L&D**, with no academic,
  rubric- or curriculum-aligned grader on the shelf, and the oversight obligation
  is unchanged. Annex III, the Oklahoma and Maryland statutes and Korea's
  high-impact classification are indifferent to licence. Keep the human gate on
  any consequential score, and when you tell a client the grader exists, tell them
  the gate stays in the same breath.
- **Building a side-car against a permissive platform.** Against Mentingo (MIT)
  there is no copyleft to route around, and the side-car reflex costs integration
  depth for no legal benefit. Use P10 and fork it. The mirror of the OpenEduCat
  anti-pattern below.
- **Enforcing an age restriction with a system prompt.** Beijing bars primary
  pupils from independent generative-AI use. A refusal the model is asked to
  perform is not a control; a graph with no generative path for that cohort is.
  Use P9 step 4.
- **Withdrawing a KB entry on a single-owner probe.** The second pass of
  2026-10-06 removed OpenTutor after probing `tutornew/OpenTutor` (8★, unlicensed)
  when the real project was `zijinz456/OpenTutor` (MIT, 130★, FSRS 4.5, 12 blocks,
  LOOM knowledge graph). A 404 is evidence about one owner's repository, never
  about a project. Enumerate owners before withdrawing — a withdrawal needs a
  stronger probe than an addition.
- **Allowlisting only `MIT / Apache-2.0 / BSD`.** That filter rejects Sakai,
  Opencast and Kuali Rice (all **ECL-2.0**, the Apache-2.0 text with an
  education-narrowed patent grant) and pgvector (**PostgreSQL License**) — four
  genuinely permissive components. Allowlist MIT, Apache-2.0, BSD, ECL-2.0,
  PostgreSQL License and ISC.
- **Trusting a repo-level licence badge on an open-core project.**
  `langfuse/langfuse` is MIT *except* `ee/`, `web/src/ee/` and `worker/src/ee/`,
  and its copyright holder is now ClickHouse, Inc. Read the carve-out paths and
  record the holder, then exclude those directories from any vendored copy.
- **Reading "Kuali is ECL-2.0" off the brand.** True of Kuali Rice, false of Kuali
  Financial System and Kuali Coeus (both AGPL-3.0). The diligence unit is the
  repository, never the foundation or the vendor.
- **Specifying AutoGen.** Maintenance mode; `LICENSE` at HEAD is CC-BY-4.0.
- **Taking `frappe/lms` as MIT.** It is AGPL-3.0 at `license.txt`; the comparison
  blogs are wrong.
- **Pinning a DeepTutor fork.** `cloudtoolbox/deeptutor` (7★) and others mirror
  the description and license without the history. Pin `HKUDS/DeepTutor`.
- **Treating an APAC sovereign model as an education product.** They are base
  models with no pedagogy layer; that layer is the work.
- **Depending on an unlicensed repo because it looks mature.**
  `DMontgomery40/mcp-canvas-lms` has 103★, 54 tools and **no license**;
  `loyaniu/moodle-mcp` has 38★ and none either. No license means all rights
  reserved — it cannot ship in a client deliverable. Probe the license in week one,
  before the feature comparison.
- **Recording "unlicensed" after probing only the repo root.**
  `OS4ED/openSIS-Classic` 404s on every root-level license filename while its real
  GPL-2.0 license sits at `docs/License.txt`, linked only from the README. Probe
  filename × extension, then read the README for a license link, then conclude.
- **Building a side-car against an LGPL-3.0 platform out of habit.** On OpenEduCat
  a separate proprietary module is permitted; routing around a constraint that is
  not there costs integration depth for nothing. Use P7.
- **Selling adoption into LATAM higher education.** 92% of students and 79% of
  faculty already use AI. The gap is depth — 88% of faculty engage only minimally.
  Sell integration and faculty capability, not enablement-from-zero.
- **Telling an EMEA client the AI Act does not apply yet.** General application
  started 2 August 2026. Only the high-risk obligations are deferred (Annex III
  stand-alone to 2 December 2027, embedded to 2 August 2028).
- **Chasing a search hit without a reachability probe.** `planejaia/OpenMAIC-Brasil`
  reads like a Brazil-origin multi-agent classroom with a v1.0.0 release and
  returns HTTP 404 on every branch and file. `curl -sI` before it reaches a
  proposal.
