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

**Updated in the fifth pass of 2026-10-06.** The deferral has a regulation number
and a catch: **Regulation (EU) 2026/1744** (*Digital Omnibus on AI*, in force
27 July 2026, CELEX 32026R1744) moved Annex III to 2 December 2027 and Annex I to
2 August 2028, **but left Article 50 transparency untouched — the watermarking
and synthetic-content-marking deadline is still 2 December 2026.** So the
sovereign build below is the December 2027 programme, and there is a small,
separate, nearly-immediate obligation in front of it. **Run P13 before this
pattern**, not after: it classifies the estate and ships the labelling layer.

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
6. **Added in the fifth pass of 2026-10-06 — read a working implementation of
   steps 4 and 5 before building them.**
   [DannyAvilaL/agente_clases](https://github.com/DannyAvilaL/agente_clases)
   (**MIT**, Spanish-language, 0★, 5 commits) is the most concrete offline-first
   education agent this KB has recorded: **Ollama Phi-3 (2 GB)** generating
   per-student Markdown material and exercises, synthesised `.csv` datasets
   injected as tables into local **PostgreSQL**, Google Calendar syncing *down*
   into a local **Radicale** CalDAV server so the system keeps running with no
   internet, a **Streamlit** dashboard for teachers, and a `cron` autopilot that
   prepares classes a week ahead. Two design choices worth copying outright: the
   **2 GB model floor** (it names the laptop-class hardware it runs on), and
   **calendar sync in the offline-safe direction** — cloud is a source, never a
   dependency. 0★ and single-author: **read it, do not pin it.**
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

## P11 — Gated lesson generation (one oversight gate, sold in every region)

Added in the fourth pass of 2026-10-06. This is the pattern that **trend 16**
argues is the highest-reuse build in this KB: four US state legislatures, the EU
AI Act and Beijing all converge on *teacher-in-the-loop plus
no-high-stakes-automation*, so the gate is built once and sold everywhere.

**Use when:** the client has to produce teaching or assessment material at volume
**and** has a statutory human-oversight obligation. That is now the default, not
the exception — Idaho (SB 1227, *"human judgment remains the final authority"*),
Oklahoma (SB 1734, educator supervision + annual parent disclosure), Maryland (AI
Ready Schools Act, 24 districts / 120 days), Ohio (HB 96, deadline **passed**
1 July 2026, so districts are in implement-and-audit), the EU AI Act Annex III, and
China's bar on primary pupils using generative AI independently.

**Outcome:** generated lessons and assessments that **cannot reach a student or a
gradebook** without a named human approving them, with an evidence trail per
decision and a disclosure report the client can file.

**Wiring:**
1. **Generate with OpenMAIC, self-hosted from a reviewed fork.**
   [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (**MIT, 40.0k★**,
   Tsinghua) turns a document or topic into slides, quizzes, HTML simulations and
   PBL scenes. **Pin v1.2.0 or later specifically**: that line is server-first with
   PostgreSQL persistence, so a generation is a **durable job** rather than a
   browser session — which is the only reason a review queue can be bolted on
   without rewriting its execution model. Point inference at whatever model the
   client's data-residency posture permits.
2. **Take the gate design from AI-Teaching-Agent, and re-implement it.**
   [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent)
   (MIT) is the only permissive implementation of this shape in this KB, and it
   is **0★ with no releases — read it, do not pin it.** Take four things: the
   **`WAITING_REVIEW` task state** that blocks publication, the **JSON-Schema-validated
   DSL** for lab/exam/grading artefacts, **sandboxed grading execution that emits
   evidence**, and the **candidate-facing view that strips answers and internal
   grading references**. That last one is the detail teams forget and leak on.
3. **Make the gate unskippable at the type level.**
   [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (MIT): every
   publishable artefact carries non-optional `approved_by`, `approved_at` and
   `source_reference`. An unapproved artefact should fail to **construct**, not
   fail review. Typed boundaries are what turn a policy into a build error.
4. **Choose the generating model on pedagogical evidence, not vibes.**
   [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT) — see **P12**. Record the score in the engagement's decision log; it is
   the cheapest defensible answer to "why this model?"
5. **Trace every generation and every approval.**
   [langfuse/langfuse](https://github.com/langfuse/langfuse) (MIT — **excluding
   `ee/`, `web/src/ee/` and `worker/src/ee/`**, which carry a separate enterprise
   licence; stay out of those paths). The trace is the Annex III technical
   documentation and the Oklahoma parent-disclosure evidence, from one store.
6. **Deliver into the LMS the client already runs** via the Canvas or Moodle MCP
   servers in `agents/top.md` — **probing each one's `LICENSE` payload first**, as
   three of seven in this KB turned out unusable.
7. **Where you cannot host the generator, export instead.** OpenMAIC emits **PPTX
   and interactive HTML**, so a buyer who will not run a Chinese-origin application
   can still take the artefact. Generate in Globant's environment, gate it, hand
   over the deck.

**Effort:** 6–8 weeks for a gated pipeline on one subject and one grade band;
10–12 weeks with multi-cohort capability tiering (compose with **P9**).

**Why this beats competing with Khanmigo.** North Carolina is spending **$10M+
recurring, sole-sourced** on Khanmigo (SB 1006). The tutor is bought; the
**oversight, integration and evidence layer around it is not**, and every statute
above requires one. Sell the gate, not the tutor.

## P12 — Pedagogy-aware model selection and tutor evaluation

Added in the fourth pass of 2026-10-06. Short, cheap, and it answers a question
clients ask in week one that this KB previously could not answer with evidence:
**"which model should teach?"**

**Use when:** scoping any tutoring or content build, and whenever a client asks you
to justify a model choice — or when a regulator asks how tutoring quality is
measured.

**Outcome:** a defensible model choice backed by pedagogical measurement rather
than general-purpose benchmarks, plus a repeatable harness for scoring tutor
behaviour as the deployment evolves.

**Wiring:**
1. **Score candidate models on pedagogical knowledge, not task accuracy.**
   [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark)
   (**MIT**, 12★) evaluates models against **real teacher-qualification exam
   questions**. A model that tops a reasoning leaderboard can still not know how to
   teach, and this is the only instrument in this KB that distinguishes the two.
2. **Score the deployed tutor's *dialogue* on a rubric you re-implement yourself.**
   The one published scheme for this is `AITutor-EvalKit` (EACL 2026):
   **MI** (Mistake Identification), **ML** (Mistake Location), **PG** (Providing
   Guidance), **AC** (Actionability). **Re-implement the four dimensions; do not
   vendor the code** — its paper claims MIT but the repository has **no `LICENSE`
   payload on either branch**, which leaves it legally unlicensed. The rubric is
   published research and free to apply; the code is not safe to ship.
   Filing an issue upstream asking for a `LICENSE` is a cheap, high-value
   contribution — do it at the start of the engagement and the blocker may clear
   before delivery.
3. **Evaluate the voice path separately where it is the primary modality.**
   [AI-for-Education/voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework)
   (MIT) — relevant wherever literacy, device cost or bandwidth binds, which is the
   **LATAM offline-first (P5)** and **African** context rather than the EMEA one.
4. **Run it as a regression gate, not a one-off.** Wire both scores into CI over a
   fixed dialogue set and trace with Langfuse (MIT, minus the `ee/` paths). A model
   or prompt change that lowers PG or AC should **fail the build**; otherwise
   tutoring quality silently decays and nobody can date the regression.

**Effort:** 1–2 weeks as a scoping add-on; 3–4 weeks to run as a standing CI gate.

**Caveat, stated plainly:** these are **1–12★ research-grade repositories**. Vendor
them deliberately, read the code before trusting a score, and expect to maintain
your fork. They are in this KB because they are the only permissive options that
exist for these two functions — not because they are robust.

## P13 — The EU AI Act education profile (the December 2026 / December 2027 split)

Added in the fifth pass of 2026-10-06. **This is the highest ratio of billable
clarity to engineering effort in this KB**, and it has a deadline weeks away.

**Use when:** the client deploys AI anywhere near European education — admission
and access, evaluation of learning outcomes, student level placement, or exam and
behaviour monitoring (Annex III point 3). Also use it as the opening diagnostic on
any EMEA education account, because most of them now believe the deadline was
cancelled.

**The fact the engagement turns on.** **Regulation (EU) 2026/1744** (in force
27 July 2026, CELEX 32026R1744) moved Annex III stand-alone high-risk obligations
from 2 August 2026 to **2 December 2027**, and Annex I embedded to 2 August 2028.
**Article 50 transparency did not move: the watermarking and
synthetic-content-marking deadline is still 2 December 2026.** Clients who heard
"delayed" deferred the labelling work along with the conformity work. The labelling
work is the one that is imminent.

**Outcome:** two deliverables with two dates. **(A)** By December 2026 — every AI
interaction disclosed, every generated artefact marked, every system classified.
**(B)** By December 2027 — Annex III conformity evidence: technical documentation,
risk management, data governance, human oversight, conformity assessment, CE
marking, EU-database registration.

**Wiring:**
1. **Classify first, with the MIT toolkit, not a spreadsheet.**
   [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit)
   (**MIT**, TypeScript, 98 commits) walks the Act's decision tree across six risk
   tiers and emits **61 conformity checklist items** plus **8 document templates**.
   Run its CLI — `npx @eu-ai-act/cli classify`, then `checklist`, then `gaps` —
   over every AI system in the estate. Its web UI is **client-side only, with no
   backend**, which matters: you can hand it to a client's compliance team without
   a data-processing conversation.
2. **Write the education profile. This is the billable artefact and it does not
   exist anywhere.** The toolkit has **no education content and never mentions
   Annex III point 3**. Map its four education categories — admission/access,
   learning-outcome evaluation, level placement, exam/behaviour monitoring — onto
   the 61 checklist items, as a data file in the toolkit's own shape. Ship it as a
   **pull request upstream** as well as a client deliverable: it costs nothing
   extra, and a merged education profile in the canonical MIT toolkit is a
   positioning asset no competitor can take back.
3. **Do the December 2026 labelling work now, because it is small.** Every
   generated lesson, item, feedback string and tutor turn carries a
   machine-readable marker and a learner-visible disclosure. Make it structural
   rather than a convention: reuse **P11 step 3** — artefacts carry non-optional
   `ai_generated`, `disclosure_shown` and `marked_at` fields via
   [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (MIT), so an
   unlabelled artefact fails to construct.
4. **Generate the Annex III evidence from traces you are already keeping.**
   [langfuse/langfuse](https://github.com/langfuse/langfuse) (MIT — stay out of
   `ee/`, `web/src/ee/`, `worker/src/ee/`) is the technical-documentation and
   human-oversight record. The checklist items from step 1 tell you exactly which
   spans you must be able to produce.
5. **Measure the model against the Act's data-governance and robustness asks.**
   [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) (**Apache-2.0**, ETH
   Zurich) pairs a technical interpretation of the Act with a benchmarking suite.
   It is the measurement half of step 1's checklist half.
6. **Keep the human gate from P11.** Annex III human-oversight evidence and the
   gate are the same artefact. Do not build two.

**Effort:** 2–3 weeks for classification plus the education profile on an estate
of a handful of systems; 4–5 weeks to add the December 2026 labelling layer;
10–12 weeks for the full Annex III evidence programme (compose with **P4** and
**P11**).

**Verify before you quote.** EUR-Lex and the Commission's notice are unreachable
from the environment this KB is built in. Every date here is corroborated across
several independent legal analyses and the CELEX id is given for one-step
verification — **check it against EUR-Lex before it reaches a client.**

## P14 — ASEAN: the permissive LMS under the closed products

Added in the fifth pass of 2026-10-06. For Singapore, Malaysia and the wider SEA
higher-education and polytechnic market.

**Use when:** the client is an ASEAN institution teaching **programming or
computer science**, wants to own and rebrand its platform, and has engineering
capacity. Also use it when a client has seen Singapore's AICET products and asked
for "that, but ours."

**The situation.** Singapore has APAC's most operationally mature education AI and
**none of it is forkable**: AICET's **Codaveri** (30,000+ pieces of personalised
programming feedback since 2024), **Softmark** (70,000+ exam scripts in 2025, with
computer-vision grouping of similar answers) and **ScholAIstic** (educators
authoring their own roleplay chatbots, deployed across Social Work, Law and
Nursing at NUS since June 2024) are closed, ministry-funded products. The LMS
beneath Codaveri is **MIT**.

**Outcome:** a client-owned, rebrandable CS-teaching platform with an agent
side-car, built on a permissive substrate that already carries an autograder and
gamification — with the AICET deployment cited as the proof the shape works.

**Wiring:**
1. **Fork [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2)**
   — **MIT, read from `master/LICENSE`, 158★, 78 forks, 15,802 commits.** Note the
   default branch is `master`; `main/LICENSE` 404s. Three components, not one:
   Rails 8 API, React client, **Keycloak** auth. Scope the Keycloak-to-client-IdP
   work in week one; it is the integration that surprises teams.
2. **Size the concentration risk out loud, in week one.** 158★ means a small
   contributor base and realistically NUS-dependent maintenance. If the client's
   engineers will not own the fork, **stop and propose Moodle instead** — this
   pattern is wrong for them. Trading copyleft for a maintenance cliff is only a
   good trade when somebody is standing at the top of it.
3. **Put the tutor beside it, not inside it.** Build the programming-feedback
   agent as a side-car against Coursemology's own submission and assignment
   models — the **P1** shape — so platform upgrades and agent iterations stay
   independent. Codaveri is the existence proof that this integration point works
   at scale on this codebase.
4. **Gate the grading with P11.** Korea's **AI Basic Act** (in force **22 January
   2026**) requires human oversight and documentation for high-impact systems, and
   **Australia's TEQSA** requires an institutional genAI action plan from every
   higher-education provider. The gate is the deliverable both ask for.
5. **Clear model rights per model, never per repository.** If the client wants a
   SEA sovereign model, [aisingapore/sealion](https://github.com/aisingapore/sealion)
   has **no repository `LICENSE` payload** and its README states terms vary by base
   model — Llama3-derived variants restrict commercial use, Gemma-derived variants
   differ. Clear each **Hugging Face model card**, per release, and put the
   result in the decision log. **MaLLaM** (Malaysia, with NVIDIA, 3M+ users via
   YTL/Yes) and **Gemma-SEA-LION-v4-27B-VL** (March 2026) are the current
   candidates.
6. **The ScholAIstic-shaped gap is the follow-on sale.** No permissive project
   anywhere in this KB lets a **non-technical educator author and publish their
   own agent**. P8 produces Agent Skills *for* educators; it does not give them an
   authoring surface. Build that on top of this platform and it is a product, not
   a project.

**Effort:** 8–10 weeks for a branded fork with IdP integration and one side-car
tutor; +4 weeks for the gated-grading layer.

**Why it beats greenfield.** The autograder, submission pipeline, gamification and
a decade of commits are already there under a licence that lets the client resell
the result. Rebuilding that to avoid a 158★ dependency is the more expensive risk.

## P15 — Curriculum-aligned item generation under a sovereignty constraint

Added in the fifth pass of 2026-10-06. India-first, and portable to any
jurisdiction with a national curriculum body and a data-residency requirement.

**Use when:** the client is a ministry, board, state system or publisher that
needs assessment items and lesson material **aligned to a named national
curriculum**, cannot send student or textbook data to a frontier API, and will be
asked in week one whether the output infringes the curriculum body's copyright.

**Outcome:** curriculum-tagged lesson plans, items and marking keys, generated on
open-weight models the client can host, with a written copyright position and a
human-curator gate — i.e. the three things that stop this kind of programme, all
answered.

**Wiring:**
1. **Take the teacher-side workflow from
   [microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot)**
   (**MIT**, Microsoft Research India / VELLM, validated with the **Sikshana
   Foundation**). Two things specifically: the **selection model** —
   curriculum → grade → subject → chapter, which is how a teacher actually thinks
   and how the artefact must be tagged — and the **ingestion pipeline gated by
   human curators**, which is the answer to "where did the source material come
   from?" Its output set is the right target too: lesson plans, real-world
   examples, analogies, hands-on activities, formative and summative assessments,
   exported to **DOCX, PPT and handouts**, plus multi-chapter question banks
   against blueprint formats. **Note its own declared GPT-4o dependency** and
   replace that layer in step 2.
2. **Take the sovereignty and copyright posture from
   [Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI)**
   (**MIT**, CBSE/NCERT grades 9–12). It runs on **open-weight Gemma only**
   (`gemma-4-26b-a4b-it`, failover `gemma-4-31b-it`, temperature 0.2, explicitly
   zero Gemini), routes every model call through a backend so keys never reach the
   browser, and ships a **written copyright argument**: no curriculum-body text is
   stored or reproduced, syllabi and blueprints are treated as public standards,
   and every item is synthesised on demand. **Reuse the argument even when you do
   not reuse the code** — it is the artefact that unblocks procurement.
   *(0★, 7 commits: read it, do not pin it.)*
3. **Serve the weights yourself.** [ollama/ollama](https://github.com/ollama/ollama)
   or [vllm-project/vllm](https://github.com/vllm-project/vllm) inside the
   client's boundary. Low temperature and structured pedagogical prompts are doing
   real work here; keep both.
4. **Make curriculum tags and provenance structural**, via
   [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (MIT): every
   item carries non-optional `curriculum`, `grade`, `subject`, `chapter`,
   `blueprint_section` and `generated_by`. Untagged items are exactly the ones that
   fail an audit.
5. **Gate it with P11 and label it with P13.** The human gate satisfies the
   oversight rules; the labelling satisfies Article 50 if any of this touches
   Europe.
6. **Evaluate the teaching, not the answer.** Re-implement the MathTutorBench
   rubric (trend 18 — read it, do not vendor it) and use
   [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT) to pick which open-weight model teaches best, per **P12**.

**Effort:** 6–8 weeks for one board, one grade band and one subject, self-hosted;
+3–4 weeks per additional subject once the tagging schema is settled.

**Portability.** The pattern is curriculum-shaped, not India-shaped. Substitute the
curriculum body and it serves the UAE's seven-area mandate — which this KB records
as having **no curriculum-aligned permissive pipeline at all** — or any LATAM
ministry, where **P6** should precede it (see `intel/market.md`: 87% of LAC
institutions use AI and only 26% have a strategy for it).

## P16 — The all-MIT national/state stack (APAC, India shape)

Added sixth pass, 2026-10-06. **The only pattern in this KB whose every component
is MIT** — platform, language layer, orchestration and review tool. That matters
because it removes the licence conversation from a public-sector procurement
entirely.

**When to propose it:** a ministry, state education department or large public
system in India or an Indic-language market, where curriculum alignment and
multilingual delivery are requirements rather than features.

| Layer | Component | Licence (payload) |
|---|---|---|
| Platform | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** (`master/LICENSE`) |
| Deployment | [project-sunbird/sunbird-devops](https://github.com/project-sunbird/sunbird-devops) | **MIT** |
| Translation | [AI4Bharat/IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) | **MIT** (`main/LICENSE`) |
| Speech out | [AI4Bharat/Indic-TTS](https://github.com/AI4Bharat/Indic-TTS) | **MIT** (`master/LICENSE.txt`) |
| Speech in | [AI4Bharat/IndicWav2Vec](https://github.com/AI4Bharat/IndicWav2Vec) | **MIT** (`main/LICENSE`) |
| Teacher review | [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** (`master/LICENSE`) |
| Orchestration | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | **MIT** |
| Typed outputs | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | **MIT** |
| Inference | [ollama/ollama](https://github.com/ollama/ollama) | **MIT** |
| Lesson generation | [microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot) | **MIT** — India-built, teacher-side, human-curated by design |

**Wiring.** Sunbird is the system of record and the delivery surface; do not fork
it. Lesson generation runs as a side-car on the Shiksha Copilot shape — curriculum
→ grade → subject → chapter, producing lesson plans, examples, activities and
assessments. LangGraph orchestrates with checkpoints as the audit trail;
pydantic-ai schema-checks every generated item so a malformed assessment cannot
reach a learner. **Shoonya is the mandatory gate**: no generated item publishes
to Sunbird without a named teacher's approval recorded against it. IndicTrans2
translates the approved artefact into the 18+ languages Sunbird already serves;
Indic-TTS voices it; IndicWav2Vec takes spoken answers back. Ollama keeps all
inference inside the ministry's own infrastructure.

**Sequence:** Sunbird + DevOps stand-up (4–5 wk, the real cost — 100+
micro-services) → generation side-car and schema contracts (3 wk) → Shoonya review
loop with named approvers (2 wk) → language layer, two languages first (3 wk) →
remaining languages (1 wk each, parallel). **12–14 weeks** to a reviewed,
multilingual pilot.

**Say this in the pitch:** every line of this stack is MIT, so there is no
copyleft obligation, no per-seat licence and no vendor in the critical path — and
the platform is already a recognised **Digital Public Good** running at national
scale. **Do not propose this outside Indic markets:** NCERT/CBSE/SCERT alignment
is embedded, and undoing it costs more than starting from Coursemology.

## P17 — Oral reading fluency assessment (the open category with no open competitor)

Added sixth pass, 2026-10-06. This is the one pattern here that builds into a
**declared void**: oral reading fluency (ORF) is the highest-volume literacy
measurement in primary education and **every system doing it is proprietary** —
FLORA, Literably, Amplify Text Reading Online, SoapBox Labs, none with a public
repository. The permissive components all now exist.

**The measurement:** a child reads a grade-levelled passage aloud; the system
returns **words correct per minute (WCPM)**, accuracy, and a per-word error list a
teacher can inspect.

| Stage | Component | Licence (payload) | Why this one |
|---|---|---|---|
| Transcript | [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | **MIT** (`master/LICENSE`) | CTranslate2 build — faster and lighter than reference Whisper, same weights |
| Word timings | [m-bain/whisperX](https://github.com/m-bain/whisperX) | **BSD** (`main/LICENSE`) | **The load-bearing choice.** WCPM is a rate, so it is uncomputable without word-level timestamps |
| Offline variant | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`) | Same measurement on a tablet or Pi with **no connectivity**, where the assessment is most needed |
| Alignment/scoring | your code | — | Align transcript against the known passage; classify omissions, insertions, substitutions, self-corrections |
| Evidence trail | [langfuse/langfuse](https://github.com/langfuse/langfuse) | **MIT** (with carve-out) | Every scored attempt traceable — an assessment decision must be defensible |
| Teacher override | [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** | Human adjudication of disputed words; the scores it corrects become your eval set |

**Wiring.** The passage is known in advance, which makes this far more tractable
than open transcription: you are doing **forced alignment against a reference
text**, not open-vocabulary ASR. faster-whisper produces the transcript, whisperX
attaches word-level timestamps, your aligner diffs transcript against reference
and emits WCPM plus a typed error list. **The teacher's judgment is final** — the
system proposes a score and a teacher confirms or overrides it, which is also what
keeps it on the right side of US state law (trend 16) and the EU AI Act's
human-oversight requirement for education (trend 17; P13).

**Evaluate against a public baseline, and say the number.** The **Ghana ORF
Dataset** is publicly available — 130 students aged 9–18, original passages, audio
and human transcriptions — and the published baseline is **Whisper V2 at 10.3%
WER** on Ghanaian students reading aloud (*IJAIED*,
[10.1007/s40593-024-00435-9](https://doi.org/10.1007/s40593-024-00435-9)). Report
agreement with human raters, not WER alone: the client cares whether the system
and a trained rater assign the same WCPM.

**Sequence:** aligner and WCPM scorer against the Ghana dataset (3 wk) →
human-agreement evaluation and error taxonomy (2 wk) → teacher override UI and
Langfuse trail (2 wk) → offline build on sherpa-onnx (2 wk) → classroom pilot
(3 wk). **10–12 weeks** to a measured, reviewable assessor.

**Two warnings.** Accented and child speech is where ASR degrades most, so **the
evaluation is the deliverable** — a fluency score nobody has validated against
human raters is worse than no score. And ORF is **high-stakes assessment**: in the
EU this is Annex III point 3 territory, so run it through P13 before it touches a
real pupil.

## P18 — Offline voice tutoring (P5 with a voice, LATAM and low-connectivity)

Added sixth pass, 2026-10-06. **Supersedes the voice question left open in P5.**
P5 established offline-first delivery as an equity requirement; it had no
permissive way to make the tutor speak or listen. It does now.

| Layer | Component | Licence (payload) |
|---|---|---|
| Platform | [LearningEquality/kolibri](https://github.com/LearningEquality/kolibri) | **MIT** (`LICENSE`) |
| Content pipeline | [LearningEquality/ricecooker](https://github.com/LearningEquality/ricecooker) | **MIT** |
| **Voice, all of it** | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`) |
| Higher-quality TTS | [idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) | **MPL-2.0** (`main/LICENSE.txt`) — the **live fork**, not `coqui-ai/TTS` |
| Local inference | [ollama/ollama](https://github.com/ollama/ollama) | **MIT** |
| Local retrieval | [pgvector/pgvector](https://github.com/pgvector/pgvector) | PostgreSQL Licence — permissive |
| Portuguese model | [Polygl0t/Polygl0t](https://github.com/Polygl0t/Polygl0t) / Tucano 2 | **Apache-2.0** (`main/LICENSE`) |

**Wiring.** Kolibri serves content on a classroom server with no internet;
ricecooker packages the curriculum into channels. **sherpa-onnx provides STT, TTS,
diarization and VAD from a single Apache-2.0 dependency** on the same box — a Pi,
a low-end laptop or an Android tablet — so a learner speaks, is transcribed, gets a
spoken reply, and nothing leaves the room. Ollama runs the tutor model locally;
pgvector keeps retrieval in the Postgres instance already there, with no separate
vector store to host. For Brazil, Tucano 2 (Apache-2.0, 0.5–3.7B) is the
Portuguese-native option and the small sizes are the point on this hardware.

**Why sherpa-onnx and not Piper.** Piper is the better-known offline TTS and the
obvious reach — **and [rhasspy/piper](https://github.com/rhasspy/piper) (MIT) has
been archived read-only since 2025-10-06**, with development moved to
[OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl) under **GPL-3.0**.
Frozen or copyleft, no third option. sherpa-onnx is Apache-2.0, maintained
(2,092 commits), and covers three more capabilities besides. If a client
specifically wants Piper voices, make the frozen-vs-GPL trade explicit in writing
before committing.

**Sequence:** Kolibri + content channels (2 wk) → local inference and retrieval
(2 wk) → sherpa-onnx voice loop with push-to-talk and VAD (3 wk) → language/model
selection and pedagogical tuning (2 wk) → offline-hardware field pilot (3 wk).
**10–12 weeks.**

**The honest regional caveat.** For Spanish and Portuguese this works today. For
most of the world's teaching languages **it does not** — the permissive language
layer exists for Indic languages (MIT) and six Ugandan languages plus Masakhane's
continental MT (Apache-2.0/MIT), **and, added in the seventh pass, ASEAN:
Vietnamese, Thai, Malay and Indonesian (Apache-2.0/MIT — see P19)**. Outside
those three regions, essentially nowhere. Check the target
language against `repos/foundations.md` **before** promising mother-tongue
delivery; where it is missing, the honest scope is data collection first, and
`SunbirdAI/salt` is the model for how that was done well.

## P19 — ASEAN mother-tongue tutor on an all-permissive national stack

Added seventh pass, 2026-10-06. **This pattern did not exist before this pass
because the KB believed its language layer did not exist.** The sixth pass
recorded ASEAN as having no permissive self-hostable language layer, having
searched for sovereign models and correctly found
[SEA-LION](https://github.com/aisingapore/sea-lion) carrying no repository-level
grant. Searching for **toolkits** instead returns a full shelf.

**Every layer below is MIT or Apache-2.0, read from payload on 2026-10-06.**

| Layer | Component | Licence (payload) |
|---|---|---|
| LMS substrate | [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) | **MIT** (`master/LICENSE`) — NUS-origin, 15,802 commits |
| Pedagogy engine | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** (`main/LICENSE`) — BKT + FSRS + prerequisites + misconceptions |
| **Language — Vietnamese** | [undertheseanlp/underthesea](https://github.com/undertheseanlp/underthesea) | **Apache-2.0** (`main/LICENSE`) — 1.8k★, 13 tasks incl. diacritics restoration |
| **Language — Thai** | [PyThaiNLP/pythainlp](https://github.com/PyThaiNLP/pythainlp) | **Apache-2.0** (`main/LICENSE`) — 1.2k★, 6,649 commits, subword tokenization |
| **Language — Malay** | [malaysia-ai/malaya](https://github.com/malaysia-ai/malaya) | **MIT** (`master/LICENSE`) |
| **Voice — Malay only** | [malaysia-ai/malaya-speech](https://github.com/malaysia-ai/malaya-speech) | **MIT** (`master/LICENSE`) |
| **Language — Indonesian** | [IndoNLP/nusa-crowd](https://github.com/IndoNLP/nusa-crowd) | **Apache-2.0** (`master/LICENSE`) — 143 datasets |
| Voice runtime (all other languages) | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`) |
| Local inference | [ollama/ollama](https://github.com/ollama/ollama) | **MIT** |
| Human review stage | [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** (`master/LICENSE`) |

**Wiring.** Coursemology holds courses, submissions and roster and is the system
of record. `tutor-mcp` runs as an **external MCP side-car** — the licence
boundary from `agents/top.md` applies here as everywhere: the pedagogy stays MIT
because it never enters the LMS tree — and owns mastery state (BKT), review
scheduling (FSRS) and the prerequisite graph. The **language toolkit for the
target country sits in front of the model**, doing the work a frontier model does
badly in these languages: `pythainlp` tokenizes Thai (which has no spaces between
words, so this is not optional); `underthesea` restores diacritics and segments
Vietnamese; `malaya` normalizes and tags Malay. Ollama serves the tutor model
locally. For spoken practice, **Malay routes through `malaya-speech`; everything
else routes through `sherpa-onnx`** and must be accuracy-tested per language.
Shoonya is the annotation and review stage for the curriculum corpus — which in
Vietnam is also a compliance artefact, see **P20**.

**Why this is the clearest build-and-own opportunity in APAC outside India.**
The fifth pass established that ASEAN's operationally mature education AI is
**closed** — AICET's Codaveri, Softmark and ScholAIstic run at ministry scale
with no public repository — over an **MIT substrate**. Add the language shelf and
the asymmetry is unusually favourable: **the LMS layer is MIT, the language layer
is Apache-2.0/MIT, and the national-language pedagogy layer is unbuilt by anyone,
open or closed.** There is no incumbent to displace and no licence to negotiate.

**Sequence:** Coursemology deployment and roster integration (3 wk) → `tutor-mcp`
side-car wired over LTI/MCP with mastery state (3 wk) → language toolkit
integration and per-language quality evaluation (3 wk) → curriculum corpus
ingestion through Shoonya review (3 wk) → voice layer, Malay first (2 wk) →
classroom pilot (3 wk). **15–17 weeks.**

**Three honest constraints — state all three in the proposal.**

1. **None of the language shelf is education-specific.** These are general
   toolkits, exactly like AI4Bharat. They make a mother-tongue tutor possible;
   the pedagogy is yours to build. That is the opportunity and also the cost.
2. **Voice is Malay-only on the regional shelf.** Thai, Vietnamese and Indonesian
   have the text layer and no local permissive voice layer. Do not promise spoken
   practice in those three until `sherpa-onnx` or Whisper has been measured on
   the target language with real learner audio.
3. **`nusa-crowd` and `indonlu` are corpora and benchmarks, not runtimes.** For
   Indonesian the shelf gives you data and evaluation, not a deployable
   component. Scope Indonesian as a heavier build than Thai or Vietnamese.

**Do not use `malaysia-ai/malaysian-dataset`** (345★, the organisation's second
most-starred repo) — **no `LICENSE` payload**, while both its code siblings are
MIT. And do not treat SEA-LION as a blanket-licensed option: its grant lives on
each HuggingFace **model card**, so licence review there is **per checkpoint and
recurring**.

## P20 — The corpus-provenance gate (Vietnam Decree 33, and the artefact every regime now wants)

Added seventh pass, 2026-10-06. **P13 is the EU AI Act education profile, built
around the *decision* an AI makes about a learner. This pattern covers the axis
P13 does not have: the *provenance of the corpus*.**

**The rule that creates it.** Vietnam's **Decree 33** (signed 2026-06-30, in
force 2026-08-15), implementing Law No. 134/2025/QH15, lists 46 high-risk AI
systems across six sectors. Its **first** education category is AI providing
**self-learning content from uncontrolled data sources** — so a RAG tutor is
high-risk **even if it grades nothing, ranks nobody and monitors no one**. EU
Annex III point 3 has no equivalent category. **This reaches the default
architecture in this KB directly:** every RAG tutor in `agents/top.md`, and the
ingestion pipeline in **P2**, are in scope in Vietnam on corpus grounds alone.

| Layer | Component | Licence (payload) |
|---|---|---|
| Ingestion + item generation | **P2** pipeline as built | — |
| Human curation gate | [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** (`master/LICENSE`) |
| Grading human-gate reference | [toshieji/moodle-grading-mcp](https://github.com/toshieji/moodle-grading-mcp) | **MIT** (`main/LICENSE`) — writes `readyforreview`, never releases |
| Risk-tier classification + checklist | [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) | **MIT** — six tiers, 61 conformity items, CLI + SDK |
| Model-call trace | Langfuse (as used by [Selleo/mentingo](https://github.com/Selleo/mentingo), **MIT**) | per Langfuse terms — check before shipping |
| Signed provenance | C2PA tooling as recorded in `intel/trends.md` | per implementation |

**The deliverable is a source manifest, and it is billable.** For every document
in the tutor's corpus, record: **what** was ingested (hash and version), **from
where** (URI, publisher, retrieval date), **under what rights** (licence or
permission, with the payload read rather than the badge), **who reviewed it**
(named human, timestamp, approve/reject), and **which generated artefacts derive
from it** (so a withdrawn source can be traced forward to every item it
produced). Shoonya is the only shelved permissive implementation of the review
stage; the rest is schema and plumbing.

**Wiring.** P2 ingests as before, but nothing enters the retrieval index until it
carries a manifest row with a review decision — **fail-closed, on the pattern
`moodle-grading-mcp` uses for grades**: writes require an explicit enable flag
*and* a non-empty allowlist, and every attempt, denial and success is appended to
an audit log. Generated items inherit their sources' manifest IDs, so a
conformity assessor can ask "where did this question come from?" and get an
answer without a code reading. The `eu-ai-act-toolkit` CLI produces the risk-tier
classification and checklist artefacts; run it in CI so the compliance evidence
regenerates with the corpus rather than being assembled once before an audit.

**What it buys you in each region — this is the reason to build it once.**

| Region | What the manifest satisfies |
|---|---|
| **APAC** | Vietnam Decree 33 category 1 directly — the conformity assessment consumes exactly this. Report the risk level to the **Ministry of Science and Technology before use**; assessment before deployment and **maintained throughout** |
| **EMEA** | EU Annex III point 3 data-governance and technical-documentation obligations under P13, and the copyright question every ministry engagement asks in week one |
| **North America** | California **AB 1159** — student data must not train models — is a provenance question in the other direction, and the same manifest answers it |
| **LATAM** | The governance deficit is the measured regional opportunity: **87% of institutions using AI, 26% with a formal strategy, under 10% with formal guidelines.** This is the artefact that closes that gap, and it sells without any regulation compelling it |

**Sequence:** manifest schema and rights-capture fields (1 wk) → Shoonya review
loop with named reviewers (2 wk) → fail-closed index gate with audit log (2 wk) →
forward-tracing from source to generated item (2 wk) → `eu-ai-act-toolkit` run
wired into CI (1 wk) → conformity-assessment dry run against Decree 33's three
education categories (2 wk). **10 weeks**, and it is reusable across every
subsequent engagement in the practice.

**Two things to get right.**

- **Vietnam's biometric narrowing is an opportunity, not a loophole to lean on.**
  Decree 33 category 3 is qualified to behaviour monitoring **using biometric
  data**, so non-biometric analytics — time on task, attempt counts, mastery
  curves — sit outside it, unlike the EU's broader "behaviour monitoring". Scope
  analytics more freely in Vietnam **and** keep the human gate on consequential
  scores regardless: category 2 still captures automated evaluation and ranking.
- ⚠️ **Verify Decree 33 against its own text before this reaches a client.**
  Every legal-publisher domain carrying it is **EGRESS_BLOCKED** in this
  environment (6/6 refused). The three education categories here come from **two
  independently-phrased searches that agreed on all three**; the **biometric**
  qualifier appeared in only one of the two and is the least-confirmed element in
  this pattern. The *engineering* is sound whatever the decree says in detail —
  a source manifest is required by EMEA and useful in all four regions — but do
  not quote the categories as law without reading the law.

## P21 — The LATAM productionisation engagement (a published spec + a working offline core)

**Added in the eighth pass of 2026-10-06.** This pattern exists because the
LATAM gap changed shape: the region has published **the design and the licence,
not the product**. P21 is the engagement that closes that distance, and every
component is MIT and locally authored.

**Use it when:** a LATAM client (Colombia, Chile, Peru, Brazil) wants a tutoring
or practice system for low-connectivity public education, and wants local
provenance in the architecture rather than a US SaaS wrapper.

### Components

| Role | Component | Licence | Why this one |
|---|---|---|---|
| **Requirements baseline** | [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) `docs/TutorIA_Requerimientos.pdf` + `docs/tutoria_architecture.svg` | **MIT** © Grupo Sirius | **13-page spec, v1.0 April 2026**, RF-01…RF-20 + RNF-01…RNF-10, 5-layer architecture. Universidad Tecnológica de Pereira. **The only citable LATAM-authored education-AI requirements document in this KB** |
| **Offline delivery platform** | [learningequality/kolibri](https://github.com/learningequality/kolibri) (+ `kolibri-installer-android`) | **MIT** | Purpose-built, deployed, maintained offline-first LMS; the Android build is the 2 GB-RAM target |
| **Offline-sync reference** | [caiuc/equipo-19-haCAIthon-2026](https://github.com/caiuc/equipo-19-haCAIthon-2026) (EduFlow) | **MIT** © CAi UC — **holder flagged** | ~41 commits showing room-code + IndexedDB + Service Worker + auto-sync in readable form. **Read it; do not vendor it** until the holder is cleared |
| **LMS integration surface** | Open edX XBlock / plugin | AGPL-3.0 (platform) — side-car stays separate | The integration shape TutorIA's RF-01 specifies |
| **Portuguese language layer** | [neuralmind-ai/portuguese-bert](https://github.com/neuralmind-ai/portuguese-bert) | **MIT** © NeuralMind | **886★**, BERTimbau, BrWaC-trained. Brazil-origin, for pt-BR classification/NER/retrieval work |
| **Offline ASR / TTS** | [alphacep/vosk-api](https://github.com/alphacep/vosk-api) **Apache-2.0**; `rhasspy/piper` **MIT** (archived) or `OHF-Voice/piper1-gpl` **GPL-3.0** | mixed | The voice tier from P18; the Piper fork decision is unchanged and must be made explicitly |
| **Human quality gate** | TutorIA **RNF-09** | **MIT** (as text) | *"Al menos **2 docentes por asignatura**"* must pass pedagogical review **before launch**. A written protocol with a quorum — the thing to ship while no automated evaluator exists |

### Wiring

1. **Adopt RNF-04 and RNF-05 as the acceptance criteria, verbatim.** Target
   **2 GB RAM / 3G**; implement **TLS** in transit and **AES-256** at rest under
   **Ley 1581 de 2012 (Habeas Data)**. These are the client's own regulator's
   terms, quoted from a Colombian university's specification — far stronger in a
   proposal than a vendor's own non-functional requirements.
2. **Deploy Kolibri as the delivery platform**, Android build first. Do not
   retrofit sync onto a network-assuming LMS (see `verticals/solutions.md`).
3. **Implement the sync core on EduFlow's design:** teacher-created room +
   6-character join code; assignment packaged as text (**~8 KB per 10
   exercises**); client-side **IndexedDB** store; **Service Worker** app-shell
   cache; queued answers flushed on reconnection. Re-implement from the design —
   the holder flag makes vendoring unsafe.
4. **Keep the agent as a side-car** behind the API layer of TutorIA's
   architecture (CAPA 3), so the Open edX AGPL-3.0 boundary is never crossed —
   identical to P1 and P7's rule.
5. **Gate every consequential output through RNF-09.** Two subject teachers per
   subject sign off before launch; log the sign-off. This is also the artefact
   that satisfies the US human-oversight statutes and EU Annex III if the client
   later operates across regions.
6. **Language:** Spanish-only for v1, per TutorIA's RNF-10. For pt-BR work add
   BERTimbau. **Do not promise indigenous-language support** — see the
   warning below.

### Deliverables

A Kolibri deployment with an offline-capable practice module, a side-car agent
behind the API layer, a signed pedagogical review record per subject, and a
compliance note citing **Ley 1581** with the TLS/AES-256 evidence.

### ⚠️ Two warnings that are the point of this pattern

**1. Do not promise Quechua, Guaraní, Aymara or Nahuatl.** TutorIA's RNF-10
names native languages as a future possibility and Latam-GPT lists them as
roadmap, so a client may well ask. **The capability exists and the rights do
not:** ten of twelve probed repositories in that layer — including **all four
probed AmericasNLP editions, whose 2024 shared task is literally "Creation of
Educational Materials for Indigenous Languages"**, the ASR covering Quechua/Guaraní/Bribri/Kotiria/Wai'khana,
and the Peru MT work — carry **no `LICENSE` payload**, and
`Llamacha/IWSLT2023_Quechua_data` serves an **Apache-2.0** file over data its
README licenses **CC BY-NC-ND**. Scope it as a **data-rights workstream**
(licence conversations with Llamacha, Siminchikkunarayku and the AmericasNLP
organisers) or scope it out. `vosk-api` + `speechbrain`, both Apache-2.0, give
you a permissive pipeline ready for licensed data when it exists.

**2. Latam-GPT is not open source.** If the client asks for the regional
sovereign model: it is **Llama 3.1 Community License** © Meta — **not
OSI-approved**, carrying an Acceptable Use Policy and the 700M-MAU clause.
Usable and genuinely good for Spanish/Portuguese grounding; **not
relicensable**, and it inherits Meta's AUP into the client's product. Do not let
it into a slide that says "open source stack". *(Licence is single-source in this
KB — confirm the model card; see `agents/top.md`.)*

## P22 — The licence-reliability gate (three points, run before any component enters a deliverable)

**Added in the eighth pass of 2026-10-06.** This is not an architecture pattern;
it is the check that protects every other pattern on this page, and it exists
because the eighth pass found **four live cases where this KB's own verification
method returns the wrong answer**.

**Use it when:** any repository is about to become a dependency, a vendored
component, or a named asset in a client deliverable. Always.

### The gate

| # | Check | How | Fails when |
|---|---|---|---|
| **1** | **Payload** | `curl raw.githubusercontent.com/<repo>/<branch>/LICENSE` across `main`/`master` × `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `license`, `license.txt`, `LICENCE` | No file → **no grant.** `AmericasNLP/americasnlp{2021,2023,2024}`, 9 of 11 LATAM indigenous-layer repos |
| **2** | **Asset scope** | Read the README's own licence section. Ask: *what is the thing of value here — code, or data/audio/corpus/weights?* | Payload governs the scripts, README governs the asset, and they disagree. **`Llamacha/IWSLT2023_Quechua_data`: Apache-2.0 payload, CC BY-NC-ND data.** The asset-scope statement is **controlling** |
| **3** | **Holder** | Read the copyright line. Does the holder belong to the project? | Holder is foreign or upstream → grant **inherited, not issued**. `MaybeItsAdam/tutors` (tldraw Inc.); **all 20 `caiuc/equipo-*` repos (© CAi UC, the organiser, not the authoring teams)** |

**Plus one question that no probe answers:** *is this open **source**, or open
**weights** under a bespoke licence?* **Latam-GPT** is described as open source
by the trade press, Brookings and **the European Commission's own Open Source
Observatory**, and is licensed **Llama 3.1 Community** — not OSI-approved. Model
releases are the standing exception to every licence heuristic on this page;
check the model card, never the coverage.

### Why run all three

Each check catches a case the others miss, and in this KB's measured sample each
one has a live failure attached:

- Payload alone → ships a **CC BY-NC-ND** corpus believing it is Apache-2.0.
- Payload + scope → ships 20 MIT repositories whose **copyright belongs to
  someone who did not write them**.
- All three → still calls a **Llama-licensed** model "open source" unless the
  weights question is asked separately.

### Outputs, and what to do with each verdict

- 🟢 **All three clean** → cleared for vendoring. Record repo, branch, filename,
  licence family, holder and probe date in the deliverable's licence register.
- 🟡 **Scope conflict** → usable for the layer the payload actually covers
  (usually scripts), **not** for the asset. Re-implement or license the asset
  separately.
- 🟡 **Holder mismatch** → **read-and-learn only.** Re-implement from the design.
  Clearing it is a question for counsel, not for another probe.
- 🔴 **No payload** → not a dependency. Two options, and the eighth pass
  established which is cheaper: file an upstream `LICENSE` issue
  (**retrospective**, one repo at a time), or — where the work has not been
  written yet — **get the licence into the rules**. CAi UC made an OSI licence a
  condition of hackathon evaluation and **20 licensed repositories appeared in
  eight hours**. For engagements touching LATAM's indigenous layer or MEA, that
  clause is the highest-leverage intervention in this KB. **Name the authors as
  holders, not the organiser** — CAi UC's own template got that wrong and
  flagged all 20 of its outputs at check 3.

## P23 — The benchmark-ready evaluation harness (build the socket before the plug exists)

**Added in the ninth pass of 2026-10-06.** This pattern exists because of a fact
no earlier pass could state: **the permissive evaluation layer this KB has
declared missing since its fourth pass is funded, dated and licence-floored** —
and **has not shipped.**

**Use it when:** a client needs to evidence that its tutoring or assessment AI
works — for a procurement rubric, an EU Annex III file, a board, or a ministry —
and you have found (correctly) that **no Apache-2.0 tutoring-quality evaluator
exists today.** Measured 6 Oct 2026: `tutoring quality evaluation benchmark
license:apache-2.0` → **0 repositories.**

**The strategy:** do not build an evaluator and do not wait for one. **Build the
socket.** Twelve funded projects under a floor of *"at least as permissive as
CC-BY-4.0 (content) or Apache-2.0 (code/models)"* land through 2027; the
engineering job today is a harness whose benchmark layer is a swappable adapter,
so each one drops in as it publishes.

### Components

| Layer | Component | Licence | Status |
|---|---|---|---|
| Harness + adapter interface | **client-owned**, written Apache-2.0 to match the incoming layer | Apache-2.0 | you build this |
| Human quality gate (today's substitute for an automated one) | **TutorIA `RNF-09`** — pedagogical review by **≥2 subject-expert teachers per subject before launch** ([LabSirius/TutorIA](https://github.com/LabSirius/TutorIA)) | **MIT** | ✅ citable now |
| Speech scoring, where oral fluency is in scope | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`, payload-verified) | ✅ now |
| Content + curriculum grounding | [learningequality/kolibri](https://github.com/learningequality/kolibri) + [studio](https://github.com/learningequality/studio) | **MIT** | ✅ now |
| Interaction log (the artefact rubrics omit and regulators want) | client-owned, append-only | Apache-2.0 | you build this |
| **Benchmark slot 1** — science misconceptions in free-form responses | **Learning Equality** (PI Jamie Alexandre) | ≥ Apache-2.0 / CC-BY by grant condition | ⏳ funded 29 Jun 2026, 6–12 mo |
| **Benchmark slot 2** — multimodal formative assessment (**KB-TutorBench**) | **Stanford** (PI Hariharan Subramonyam) | ≥ Apache-2.0 / CC-BY | ⏳ funded, **0 repositories** today |
| **Benchmark slot 3** — ASR leaderboards for education | **National Tutoring Observatory / Cornell** (PI Allison Koenecke) | ≥ Apache-2.0 / CC-BY | ⏳ funded; org has a website, **no code** |
| **Benchmark slot 4** — multimodal formative-assessment dataset | **MMSA & TERC** (Heidi Cian, Ibrahim Dahlstrom-Hakki) | openly licensed per programme | ⏳ funded 21 Sept 2026 |
| Simulated learners for regression testing | **Princeton** (PI Tammy Kwan) — simulated student models | ≥ Apache-2.0 | ⏳ funded |

### Wiring

1. **Define one adapter interface** — `(items, model_under_test) → per-item
   scores + aggregate + provenance`. Every slot above is a dataset plus a scoring
   rule; an adapter that accepts both is all the abstraction needed. Resist a
   framework.
2. **Implement the human gate first, and ship it.** TutorIA's RNF-09 is MIT,
   citable, and the only pedagogical quality protocol in this KB. Two
   subject-expert teachers per subject, reviewing before launch, with sign-off
   recorded. **This is the deliverable that satisfies "human judgment is final"**
   (trend 16) and the oversight columns of the Maryland and Vermont rubrics.
3. **Stand up the interaction log on day one.** Append-only, per-turn, with model
   version, prompt provenance and the grounding documents cited. It costs little
   at the start and is unreconstructible later — and it is the artefact **no
   published US rubric requires and the EU profile does** (**P13**).
4. **Write one reference adapter against a public education benchmark you can
   legally use, to prove the socket works.** Do **not** use
   [AI-EDU-LAB/E-EVAL](https://github.com/AI-EDU-LAB/E-EVAL) (33★, Chinese K12
   education evaluation) as a dependency — **it has no licence payload.** Read it
   for its criteria design, implement your own items, keep your implementation.
5. **Pin the slots in the architecture document by name, owner and expected
   window.** This is the part clients value: the gap is attributed and dated, not
   hidden.
6. **Re-probe the slots each quarter** with P22's gate before vendoring anything
   that lands. A grant condition is a promise about the licence; the **payload is
   still the proof**, and a funder's floor does not exempt a repository from
   checks 2 and 3 (asset scope and holder).

### Deliverables

- An Apache-2.0 harness with a documented adapter interface and one working
  reference adapter.
- A signed RNF-09-style pedagogical review record per subject.
- An append-only interaction log with provenance, plus a short output-generation
  disclosure.
- A **dated gap register**: each benchmark slot, its funded owner, its expected
  window, and what the harness does in the meantime.

### ⚠️ Three warnings that are the point of this pattern

1. **Do not present the funded pipeline as an existing shelf.** Nothing has
   shipped: `KB-TutorBench` → **0 repositories**, `learningequality` filtered on
   `benchmark` → **0 repositories**, the Cornell grantee's org → a website at 0★
   with no payload. Say *funded and expected*, never *available*.
2. **Every funder fact here is Tier 2.** `k12-ai-infrastructure.org` and
   `digitalpromise.org` are EGRESS_BLOCKED in this environment; **no RFP was
   read.** Confirm the licence floor against the primary document before it
   appears in a contract — the whole pattern rests on that one clause.
3. **Apache-2.0, not MIT, is the target licence for your harness.** The incoming
   layer is Apache-2.0 by grant condition. Matching it keeps combination trivial
   and gives the client the patent grant MIT lacks — the one case on this page
   where this KB recommends Apache-2.0 over MIT for new code.

## P24 — Procurement-rubric-ready delivery (North America, and the artefact pack that also clears the EU)

**Added in the ninth pass of 2026-10-06.** In the US the binding specification is
no longer only the statute — it is the **state-mandated evaluation rubric** the
district scores you against.

**Use it when:** the client is a US district, charter network, state agency or a
vendor selling into one — especially in **Maryland** (SB 720, effective 1 Jun
2026: state rubric, local policy within **120 days**, a designated **AI
coordinator**, ~24 districts on the clock for Fall 2026), **Vermont** (rubric of
23 Jan 2026), or **Idaho** / **Alabama** (statutory capability assessments and
pre-training verification).

**The insight:** the rubrics converge on seven criteria — educational value, data
privacy, usability and accessibility, cost, scalability, vendor reputation, age
restrictions — and they **omit** three things: an auditable interaction record,
disclosure of how outputs are generated, and evidence of bias/accuracy/
reliability evaluation. **Ship the omitted three and you exceed every published
rubric, pre-empt its next revision, and produce most of an EU Annex III file at
the same time.**

### Components

| Need | Component | Licence |
|---|---|---|
| Integration that *scores points* (39% of districts rubric-score interoperability) | **LTI + MCP side-car** per **P1** — no fork of the LMS | permissive by construction |
| No vendor training on student records (Idaho / Maryland / Alabama) | **self-hosted inference**, the sovereign stack of **P4** | — |
| Accessibility evidence | WCAG audit against the rubric's own accessibility criterion | — |
| Human-final decisions | **TutorIA RNF-09** review protocol ([LabSirius/TutorIA](https://github.com/LabSirius/TutorIA)) | **MIT** |
| Evaluation evidence | **P23** harness + dated gap register | Apache-2.0 |
| Offline/equity criterion, where present | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** |
| Proctoring, **only if** explicitly required | [AarambhDevHub/exam-cheating-detection](https://github.com/AarambhDevHub/exam-cheating-detection) (47★) or [vincenzo-afk/Proctored-MCQ-Exam-Platform](https://github.com/vincenzo-afk/Proctored-MCQ-Exam-Platform) (36★) | **MIT**, payload-verified |

### Wiring

1. **Obtain the actual rubric before designing.** Maryland's is state-published;
   Vermont's is in its January guidance. **Build the deliverable's evidence index
   as a one-to-one map onto the rubric's rows** — a reviewer scoring your bid
   should never have to search.
2. **Satisfy "no training on student records" architecturally, not
   contractually.** A contractual promise is a clause someone must trust;
   self-hosted inference (**P4**) is a fact they can inspect. Where a hosted model
   is unavoidable, isolate it behind the side-car so student records never cross
   the boundary, and document the boundary.
3. **Integrate via LTI + MCP (P1), never by forking the LMS.** This is now worth
   points, not just maintenance savings.
4. **Add the three missing artefacts** — interaction audit log,
   output-generation disclosure, bias/accuracy/reliability evaluation report (from
   **P23**). Name them in the bid as *exceeding* the rubric.
5. **Name the AI coordinator's workflow.** Maryland requires a designated
   coordinator; a tool that produces a report that person can actually file is
   differentiated from one that produces a dashboard they must interpret.
6. **Reuse the pack in EMEA.** The three omitted artefacts are substantially the
   Annex III evidence of **P13**. Build once, file in both regions — and note the
   direction of travel: **this is the first cross-region compliance reuse in this
   KB that runs from EMEA into North America**, because the EU profile is the
   stricter parent.
7. **Where proctoring is required, scope it carefully.** The MIT proctoring
   options are **18–47★ individual-scale projects**, not products: vendor the
   core, harden it, own it. Do **not** use `lebmatter/exampro` (72★, the
   framework-grade one) — **no licence payload**. And proctoring is biometric
   processing: it pulls the deliverable into Annex III in the EU and into the
   age-restriction row of the Vermont rubric.

### Deliverables

- A rubric-indexed evidence pack, one section per rubric row.
- An architecture note showing where student records do and do not travel.
- Interaction audit log, output-generation disclosure, evaluation report.
- A licence register (**P22** output) for every component, with probe dates.

### ⚠️ Warnings

- **Every statutory and rubric fact in this pattern is Tier 2.**
  `marylandpublicschools.org`, `cosn.org`, `njsba.org`, `web.ped.nm.gov` and
  `excelined.org` are **EGRESS_BLOCKED** here; **no rubric and no RFP was read.**
  Confirm each citation — *especially effective dates and the 120-day clock* —
  against the primary document before it enters a bid.
- **Rubrics are state-specific and moving.** Do not generalise Maryland's to a
  neighbouring state. The *pattern* generalises; the rows do not.
- **Outcomes-based contracting is appearing in tutoring solicitations** (NJSBA RFP
  2026-02). If an outcome clause is in scope, the **P23** harness stops being a
  compliance artefact and becomes the instrument your payment depends on — price
  and staff it accordingly.

## Pattern selection

| Situation | Pattern |
|---|---|
| Client already has an LMS | P1 |
| Needs content or item volume from existing curriculum | P2 |
| Must justify mastery/progression decisions | P3 |
| EU client, assessment in scope | P4 (P1 for the integration) |
| Connectivity/budget constrained, equity mandate | P5 |
| Client must evidence that its tutoring AI works, and no permissive evaluator exists yet | **P23** |
| US district / state agency bid, or selling into one | **P24** (with P1 for integration, P4 for inference) |
| Any repository about to become a dependency | **P22**, always |
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
| US district or state with a 2026 AI statute (ID, OK, MD, OH, CA) | **P11** — one oversight gate satisfies all five, the EU Annex III and Beijing |
| Needs whole lessons generated, not just tutoring dialogue | **P11** (OpenMAIC, MIT, 40.0k★ — pin v1.2.0+ for durable server-side jobs) |
| Competing against an incumbent AI tutor already bought (e.g. Khanmigo) | **P11** — sell the oversight, integration and evidence layer, not a rival tutor |
| Client asks "which model should teach?" or must justify a model choice | **P12** (`pedagogy-benchmark`, MIT) — 1–2 weeks as a scoping add-on |
| Tutoring quality must be measured or must not silently regress | **P12** — re-implement the MI/ML/PG/AC rubric; `AITutor-EvalKit` code is unlicensed |
| Voice is the primary modality (low literacy, low bandwidth, Africa) | **P12** step 3 + **P5** |
| **Any EMEA education account, as the opening diagnostic** | **P13** — most of them believe the August 2026 deadline was cancelled; the 2 December 2026 labelling obligation was not |
| Client must evidence EU AI Act conformity for an education system | **P13** (MIT toolkit + the Annex III point 3 profile you write), then P4 |
| ASEAN institution teaching programming/CS that wants to own its platform | **P14** (fork Coursemology, MIT, 15,802 commits) — and size the 158★ concentration risk in week one |
| Client has seen Singapore's AICET products and wants "that, but ours" | **P14** — the products are closed, the LMS beneath them is MIT |
| Korea or Australia in scope | **P11** gate + **P14** step 4 — Korea's AI Basic Act is live since 22 Jan 2026; TEQSA requires an action plan from every provider |
| National curriculum body **plus** a data-residency constraint | **P15** — open-weight only, with a written copyright position |
| Client asks whether generated items infringe the curriculum body's copyright | **P15** step 2 — reuse CurriculumCraft AI's argument even if you reuse none of its code |
| Teacher-side artefacts (lesson plans, question banks) rather than a student tutor | **P15** step 1 (`microsoft/shiksha-copilot`, MIT) — not P1 |
| LATAM higher ed, and you are choosing where to start | **P6 first** — 87% of LAC institutions use AI, 26% have a strategy; the gap is governance, not technology |
| India or a state/national programme wanting an end-to-end permissive stack | **P16** — AI4Bharat (MIT) + Sunbird (MIT); permissive from language layer to platform |
| Primary literacy, oral reading fluency, or "measure whether the child can read" | **P17** — the only category in this KB with permissive components, a public dataset, a published baseline and **no open competitor** |
| Offline/low-connectivity **and** the tutor must speak or listen | **P18** — `sherpa-onnx` (Apache-2.0) gives STT+TTS+diarization+VAD in one dependency; **not** Piper |
| ASEAN institution wanting a tutor in Vietnamese, Thai, Malay or Indonesian | **P19** — MIT LMS substrate, Apache-2.0/MIT language shelf, pedagogy layer unbuilt by anyone open or closed |
| Spoken practice in Thai, Vietnamese or Indonesian specifically | **P19 constraint 2** — only Malay has a regional permissive voice toolkit; measure `sherpa-onnx` on real learner audio before promising |
| **Vietnam in scope, at all** | **P20** — Decree 33 makes a RAG tutor high-risk on **corpus provenance alone**, even with no grading, ranking or monitoring |
| Client asks "where did this generated question come from?" | **P20** — the source manifest, with forward tracing from source to item |
| Any engagement that ingests client or curriculum content into a tutor | **P20** alongside **P2** — build the manifest once, it satisfies Vietnam, EMEA Annex III, California AB 1159 and the LATAM governance gap |

**Index consistency note (seventh pass, 2026-10-06):** this table was missing
**P16, P17 and P18** — three patterns written by earlier passes and never indexed
here. They are added above with P19 and P20. This is the same failure the seventh
pass found in `agents/top.md` and that `repos/trending.md` recorded in the sixth:
**a finding written into one surface and not propagated to the one a reader
opens.** Checking the index against the pattern headings is now part of a pass.

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
- **Concluding a region has no permissive shelf from a popularity-ordered
  channel.** Added in the fifth pass of 2026-10-06. GitHub topic pages and
  stars-sorted searches rank by adoption, so a 2026 project with four commits from
  a public university in Risaralda is structurally invisible to both. Four passes
  of this KB declared "no India-origin", "no ASEAN-origin" and "no LATAM-origin"
  permissive education project; **one institution-first search refuted all three.**
  When a gap survives several passes, change the channel — and pick one that is
  not ordered by stars.
- **Clearing a model's licence at the repository level.**
  [aisingapore/sealion](https://github.com/aisingapore/sealion) (424★) has **no
  `LICENSE` payload** and its README says terms vary by base model — Llama3-derived
  variants restrict commercial use, Gemma-derived variants differ. A repo-level
  check returns nothing and clears nothing. **Clear rights per model, per release,
  from each Hugging Face model card**, and log the result.
- **Trusting a licence badge.** [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench)
  carries a **CC BY 4.0** badge on README line 3 and a **CC BY-SA 4.0** statement on
  README line 199, with **no `LICENSE` payload** behind either. Three reviewers
  reading the same commit get three different answers. The payload is the licence;
  a badge is a claim about it.
- **Forking a repository because its README is good.**
  [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) is MIT, institutionally
  funded, architecturally sound — and **every code path in its own documented tree
  404s**, with a quickstart pointing at a different repository. Probe the paths the
  README promises, not just the repository root.
- **Telling an EMEA client the high-risk deferral bought them 16 quiet months.**
  **Regulation (EU) 2026/1744** left **Article 50 transparency untouched**: the
  watermarking and synthetic-content-marking deadline is still **2 December 2026**,
  and the duty to classify systems against Annex III is immediate. The clients who
  heard "delayed" and stopped are unlabelled *and* unclassified. Run **P13**.
