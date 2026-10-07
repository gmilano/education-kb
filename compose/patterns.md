---
industry: education
region: Global
updated: 2026-10-07
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
2. Register a tool provider for launch, identity and grade passback.
   🔴 **CORRECTED, twenty-fourth pass of 2026-10-07 — this step named the wrong protocol.** It
   previously specified
   [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP)
   (Apache-2.0, payload 11,357 B). Its head commit is **2016-11-28 — 3,600 days, 9.9 years**, the
   oldest component in any pattern in this KB, and its `README.md` states it supports
   **"LTI 1.1 and the unofficial extensions to LTI 1.0"** — **it does not implement LTI 1.3 at
   all.** LTI 1.1's security model is retired; LTI 1.3 / Advantage is what Canvas, Moodle and
   Open edX certify against and what the procurement rubrics in `intel/market.md` score.
   ⚠️ The organisation name was the tell: **IMSGlobal renamed itself 1EdTech in 2022.**
   🟢 **Use instead, by estate:**
   - **Python / Django** (the usual case here, since steps 4–6 are Python):
     [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) — **MIT** (1,098 B), head commit
     **2026-10-05 (2 d)**, PyPI [`django-lti`](https://pypi.org/project/django-lti/) **v0.10.1
     (61 d)**. Launch in-process; **no second runtime**.
   - **JupyterHub**: [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator)
     — **BSD-3-Clause** (1,528 B), 98 d, LTI 1.3 **and** 1.1, tested against Open edX, Canvas, Moodle.
   - **PHP / Moodle estate**: [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library)
     — **Apache-2.0** (11,343 B), **14 d**.
   - **Node estate**: [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) — Apache-2.0, 1 d.
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
1. [learningequality/kolibri](https://github.com/learningequality/kolibri) (MIT)
   as the platform; runs offline on a classroom server or a single laptop.
2. [learningequality/studio](https://github.com/learningequality/studio) (MIT)
   for curriculum authoring and channel curation.
3. [learningequality/ricecooker](https://github.com/learningequality/ricecooker)
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
   with [learningequality/ricecooker](https://github.com/learningequality/ricecooker)
   (MIT) → [learningequality/kolibri](https://github.com/learningequality/kolibri)
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

## P17 — Oral reading fluency assessment (two repositories in the whole category, one of them MIT)

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

### P17 update, tenth pass of 2026-10-06 — the void has prior art and a funded competitor

Two corrections to the framing above, both measured this pass.

**1. "No open competitor" is no longer accurate — there is prior art, and it is
MIT.** The whole GitHub result set for `oral reading fluency assessment speech` is
**two repositories**:

| Repo | Licence (payload) | ★ | Relevance to P17 |
|---|---|---|---|
| [qazasd2518995/prosody](https://github.com/qazasd2518995/prosody) | **MIT** (`main/LICENSE`, full text read) | 0 | **Implements this pattern's core loop already**: aligns speech to reference text at word level, reports accuracy and WER, **speaking rate in WPM**, misread/omitted/inserted words, and a fluency score from pause pattern and pace. Whisper for ASR, **Levenshtein alignment**, Groq for transcription. Python, **1 commit**. |
| [mendezjerick/ReaDirect-V2](https://github.com/mendezjerick/ReaDirect-V2) | **no payload** (20 URLs) | 0 | Oral reading + comprehension support, TypeScript. Unusable — repository exists, grant does not. |

**Use `prosody` as a reference implementation, not as a dependency.** One commit
and zero stars is not a maintained component, and the licence permits reading it
freely. What it gives you is a **validated shape** for the aligner-and-scorer stage
that the table above leaves as "your code": Levenshtein alignment against the
reference passage, with fluency derived from pause pattern as well as rate. That is
a day of reading that removes a week of design.

Note also that `prosody` calls the **Groq API** for transcription. For the P17
build keep `faster-whisper`/`whisperX` local — the offline and data-residency
properties are the reason this pattern exists.

**2. The funded competitor now has a name, and it is the closest match in the
whole $26M programme.** **Harvard University (Ying Xu)** is a Cohort 2 grantee for
**"OpenLiteracy: An Open-Source AI Infrastructure Suite for Advancing Speech
Foundation Models for Early Word Reading Assessment and Instruction"** (Tier 2),
under the programme's **Apache-2.0-or-better licence floor**. **GitHub returns 0
repositories for `OpenLiteracy`** (Tier 1, 6 Oct 2026) — funded, named, not
shipped.

**What this does to the sequence: nothing, and that is the point.** The 10–12 week
build above stays as specified, because the deliverable that survives OpenLiteracy's
arrival is the **evaluation and the error taxonomy**, not the ASR stack. Structure
the engagement so the transcript-and-timestamp stage is replaceable behind an
interface (**P23**'s socket discipline), and OpenLiteracy becomes a drop-in upgrade
to a validated harness instead of a reason the client's project was wasted.

**And state the licence floor to the client.** Anything the programme funds must be
**at least as permissive as Apache-2.0**, so the upgrade path is contractually safe
to promise — which is a rare thing to be able to say about a dependency that does
not exist yet.

## P18 — Offline voice tutoring (P5 with a voice, LATAM and low-connectivity)

Added sixth pass, 2026-10-06. **Supersedes the voice question left open in P5.**
P5 established offline-first delivery as an equity requirement; it had no
permissive way to make the tutor speak or listen. It does now.

| Layer | Component | Licence (payload) |
|---|---|---|
| Platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (`LICENSE`) |
| Content pipeline | [learningequality/ricecooker](https://github.com/learningequality/ricecooker) | **MIT** |
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
| **Offline ASR / TTS** | [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) **Apache-2.0** (11,358 B) | 🟢 permissive, single grant | 🔵 **Re-picked, pass 24.** Was `vosk-api` + a Piper fork decision (`rhasspy/piper` **archived**, head commit **407 d**; `OHF-Voice/piper1-gpl` **GPL-3.0**). `sherpa-onnx` does **ASR *and* TTS** — plus VAD, keyword spotting and diarization — locally, on **Raspberry Pi and Android**, head commit **2026-10-06 (1 d)**. 🟢 **The Piper fork decision disappears**: one component, one permissive licence, no copyleft branch to argue about |
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

> ⚠️ **Superseded in part by P27 (eleventh pass, 2026-10-06).** This pattern was
> written on the premise that no permissive evaluation harness and no pedagogy
> benchmark existed. Both were search artefacts: **Inspect** (MIT, 2,945★, UK AI
> Security Institute) and **Moonshot** (Apache-2.0, Singapore IMDA) are the harness,
> and four tutoring benchmarks exist — **none of them OSI-licensed**. Read **P27**
> for the corrected component list and the build-system rule that keeps a
> non-redistributable dataset out of the deliverable. The reasoning below about
> building the socket first still holds for the *rubric*; it no longer holds for the
> *runner*.

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

## P25 — The interoperability tier, built to be scored (North America, and anywhere with an LMS)

> 🔵 **Re-corrected in the twenty-fourth pass, 2026-10-07.** The eleventh pass fixed the
> "no Python option" error by naming [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3)
> (MIT, 138★). 🔴 **That library is 1,416 days cold on the commit channel and 1,417 on the release
> channel** (`pylti1p3` v2.0.0, 2022-11-20) — so the correction closed the gap with an abandoned
> project. **Take [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) instead:**
> **MIT** (payload 1,098 B), head commit **2026-10-05 (2 d)**, PyPI
> [`django-lti`](https://pypi.org/project/django-lti/) **v0.10.1, 2026-08-07 (61 d)**, 17 releases.
> ⚠️ Two further corrections to the sentence this replaces: `openedx-lti-tool-plugin` is real and
> Apache-2.0 (payload 11,357 B) but lives at **`eduNEXT/openedx-lti-tool-plugin`**, is **443 days
> cold** and is **not published to PyPI** under that name; and `ucfopen/cookiecutter-python-lti`
> (MIT, 147 d) is a live template whose Flask path **installs a 1,364-day-cold fork at a moving
> branch** — take its Django path. 🔴 The best-maintained Python LTI 1.3 implementation of all,
> [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) (6 d), is
> **AGPL-3.0** and therefore off this shelf by design, not by accident.

Added tenth pass, 2026-10-06. This pattern exists because of a procurement number,
not a technology: **39% of districts score interoperability in their RFP rubrics**
(CoSN, Tier 2, ninth pass). If a third of your buyers assign points to roster and
activity exchange, the integration layer is a **scored deliverable** and it needs to
be specified, licensed and demonstrable — not discovered in integration testing.

**The deliverable:** an AI service that launches from inside the client's LMS with
real identity and course context, reads rosters from the SIS, and produces an
artefact pack that answers an interoperability rubric line by line.

| Stage | Component | Licence (payload) | Why this one |
|---|---|---|---|
| Tool launch, Node estate | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** (`master/LICENSE`) | 373★, the highest-starred genuine LTI 1.3 implementation; turns a service into a full tool provider |
| Tool launch, Moodle estate | [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | **Apache-2.0** (`master/LICENSE.md`, 11,343 B) | 🔵 **Re-picked, pass 24.** The same library the standards body ships — byte-identical payload — but the **live** copy: head commit **2026-09-23 (14 d)** against `1EdTech/lti-1-3-php-library`'s **2,317 d**. Composer name `packbackbooks/lti-1-3-php-library` |
| Tool launch, Python/Django estate | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | **MIT** (1,098 B) | 🆕 **Added pass 24.** Head commit **2 d**, PyPI `django-lti` v0.10.1 (61 d). Removes the second runtime when the AI tier is Django |
| Tool launch, JVM estate | [Unicon/tool13demo](https://github.com/Unicon/tool13demo) | **Apache-2.0** (`master/LICENSE`) | LTI 1.3 in Spring Boot, from a higher-ed systems integrator |
| Tool launch, existing Spring Security | [oxctl/spring-security-lti13](https://github.com/oxctl/spring-security-lti13) | **Apache-2.0** (`master/LICENSE.txt`) | LTI inside an existing Spring Security estate rather than beside it |
| Rostering | [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET) | **MIT** (`master/LICENSE`) | OneRoster 1.1 + 1.2 client, OAuth2 for 1.2. **Rostering only — no gradebook** |
| Audit trail | [langfuse/langfuse](https://github.com/langfuse/langfuse) | **MIT** (with carve-out) | The rubric gap the ninth pass found: **no rubric requires an interaction audit trail**, so it is the differentiator (P24) |
| Evaluation socket | P23 harness | — | The other half of the differentiator, and the EMEA conformance file (trend 27) |

**Wiring, and the decision that comes first.** **Pick the LTI runtime from the
client's estate, not from your preference** — the four implementations are not
interchangeable in effort once a stack exists. Then: LTI 1.3 launch carries
identity, course context and role; your Python AI service sits **behind** that
adapter over an internal API; OneRoster.NET syncs the roster on a schedule;
Langfuse records every interaction with the launch context attached, so an audit
trail is a by-product of the architecture rather than a feature nobody funded.

**The gap you must price, not hide.** 🔵 **CORRECTED, twenty-fourth pass of 2026-10-07: "there is
no Python LTI 1.3 library" was false.** [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
is **MIT**, head commit **2 d**, PyPI `django-lti` **v0.10.1 (61 d)**. 🟢 **If the AI layer is
Django, launch LTI in-process and budget no adapter at all** — that line item disappears from the
bid. ⚠️ The two-process architecture is still right when the AI tier is neither Django nor
JupyterHub, because the only framework-neutral Python implementation is 1,416 days cold; price the
adapter **only after** checking the framework. 🔵 **NARROWED, twenty-fifth pass of 2026-10-07 — "none" is now "one alpha".** [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) (MIT) **vendors `PyLTI1p3`, rebranded** — its README says so — and publishes it as [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 (103 d), one release ever**; head commit **63 d**; **0★**; `Development Status :: 3 - Alpha` with the FastAPI adapter and token minting **unbuilt**; and its `LICENSE` holder is **`Dmitry Viskov`, not its own authors**. **Not "no option", and not a safe dependency either.** Full row in `repos/foundations.md`. Equally: if the
rubric scores **grade passback**, OneRoster.NET does not implement the gradebook,
and if it scores **learning-analytics event streams**, there is **no permissive
Caliper Analytics implementation at all** — both are builds against the spec. Say
so in the response. A rubric line you answered with a library that does not cover
it is worse than one you answered with a costed build.

**Sequence:** estate assessment and runtime choice (1 wk) → LTI 1.3 launch with
identity and context, end to end (2 wk) → OneRoster sync and reconciliation
(2 wk) → Langfuse trail bound to launch context (1 wk) → rubric artefact pack,
line by line (1 wk) → conformance dry-run against the client's own rubric (1 wk).
**8 weeks** to something a procurement officer can score.

**Two warnings.** **Pin `theopenem/OneRoster.NET`**, not the byte-identical
`jdolny/OneRoster.NET` — both are MIT and both name `theopenem` as copyright
holder, so they are one asset at two addresses, and the fork direction is not
establishable from this environment. And **do not sweep for components with the
word "Caliper"**: the search is dominated by `google/caliper` (Java
micro-benchmarking) and `hyperledger-caliper/caliper` (blockchain), which is how a
184-result count turns into five real repositories.

## P26 — Offline-tolerant sync without a platform migration (LATAM, APAC, anywhere intermittent)

Added tenth pass, 2026-10-06. For three passes this KB has answered "offline-first"
with **Kolibri**, which is correct when the client is choosing a platform and wrong
when they already have one. The separable component underneath it is now verified,
and it is MIT.

**The deliverable:** an existing Django application that keeps working, and keeps
syncing, across intermittent connectivity — without adopting a learning platform.

| Stage | Component | Licence (payload) | Why this one |
|---|---|---|---|
| Replication engine | [learningequality/morango](https://github.com/learningequality/morango) | **MIT** (`master/LICENSE`) | **Pure-Python peer-to-peer DB replication for Django.** Marks chosen models syncable; **certificate-based authentication** for data privacy and integrity; change tracking and **data partitioning** designed for low-bandwidth links; SQLite **and** PostgreSQL. 15★, 23 forks, `release-v0.9.x` |
| Shared vocabulary | [learningequality/le-utils](https://github.com/learningequality/le-utils) | **MIT** (`main/LICENSE.txt`) | Constants and utilities shared across the Kolibri toolchain — needed if you ever exchange content with it |
| Content pipeline (optional) | [learningequality/ricecooker](https://github.com/learningequality/ricecooker) | **MIT** (`main/LICENSE`) | Generates Kolibri channels, if the client wants interoperability with that ecosystem |
| Full platform (the alternative) | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (`master/LICENSE`) | Where this pattern stops and the platform choice starts |
| Local inference | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) · [ollama/ollama](https://github.com/ollama/ollama) | **Apache-2.0** · **MIT** | The AI layer has to run where the connectivity is not |

**Wiring.** Morango is a Django app: you declare which models are syncable, give
each device or site a certificate, and let it reconcile. The **partitioning** is
the part to design deliberately — it decides what a given school or device is
allowed to hold, which is a data-protection control as much as a performance one.
Pair it with local inference so tutoring continues while the link is down, and let
only the records sync, not the model traffic.

**Why it is a smaller engagement than it looks.** Nothing here asks the client to
migrate. **Morango is usable independently of Kolibri**, under MIT, with
certificate-based auth already built — which is normally the expensive half of a
sync design. For a ministry or network that already runs a Django SIS or LMS, this
is weeks, not a platform programme.

**Sequence:** syncable-model and partition design (2 wk) → morango integration and
certificate provisioning (2 wk) → conflict and reconciliation testing on forced
disconnection (2 wk) → local inference for the degraded path (2 wk) → multi-site
pilot (2 wk). **10 weeks.**

**Two warnings, both licence-shaped.** **Probe every sibling repository before you
depend on it.** Inside this same organisation,
[kolibri-design-system](https://github.com/learningequality/kolibri-design-system)
and [kolibri-server](https://github.com/learningequality/kolibri-server) returned
**no licence payload** under 20 probed URLs — so the Vue design system in
particular must not be used for client UI on the assumption that the org is MIT.
And `learningequality/studio` carries `Copyright (c) 2021 Foundation for Learning
Equality (internal apps)`: the parenthetical looks like a scope restriction, but
the **full text was read this pass and the permission body is unmodified MIT**.
Use it; the qualifier annotates the holder, not the grant.

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
| Primary literacy, oral reading fluency, or "measure whether the child can read" | **P17** — permissive components, a public dataset and a published baseline; the whole existing category is **two repositories, one MIT at 1 commit** (`prosody`), and Harvard's **OpenLiteracy** is funded to fill it (0 repos today) |
| Offline/low-connectivity **and** the tutor must speak or listen | **P18** — `sherpa-onnx` (Apache-2.0) gives STT+TTS+diarization+VAD in one dependency; **not** Piper |
| ASEAN institution wanting a tutor in Vietnamese, Thai, Malay or Indonesian | **P19** — MIT LMS substrate, Apache-2.0/MIT language shelf, pedagogy layer unbuilt by anyone open or closed |
| Spoken practice in Thai, Vietnamese or Indonesian specifically | **P19 constraint 2** — only Malay has a regional permissive voice toolkit; measure `sherpa-onnx` on real learner audio before promising |
| **Vietnam in scope, at all** | **P20** — Decree 33 makes a RAG tutor high-risk on **corpus provenance alone**, even with no grading, ranking or monitoring |
| Client asks "where did this generated question come from?" | **P20** — the source manifest, with forward tracing from source to item |
| Any engagement that ingests client or curriculum content into a tutor | **P20** alongside **P2** — build the manifest once, it satisfies Vietnam, EMEA Annex III, California AB 1159 and the LATAM governance gap |
| RFP or rubric that **scores interoperability** (39% of US districts do) | **P25** — pick the LTI runtime from the client's estate, and price the Python adapter instead of hiding it |
| Client already runs a **Django** SIS/LMS and needs offline tolerance | **P26** — `morango` (MIT) gives P2P replication with certificate auth; **no platform migration** |
| "We need offline" but the client is **not** choosing a platform | **P26**, not P5 — Kolibri is the answer to a platform question, morango to a sync question |
| Rubric scores **grade passback** or **learning-analytics event streams** | **P25**, costed as a build — OneRoster.NET has no gradebook and there is no permissive Caliper implementation |
| Any absence you are about to put in a client deliverable | **P22**, plus trend 29 — state the instrument that measured it; GitHub's licence field reports MIT repos as unlicensed |

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

## P27 — The tutor-quality evidence pack (the harness is free; the benchmarks are borrowed, never shipped)

**Replaces the "wait for the artefact" half of P23.** P23 was written when this KB
believed no permissive evaluation harness and no pedagogy benchmark existed. Both
beliefs were wrong in different ways, measured 2026-10-06: **the harness exists,
MIT, from a government, at 2,945★**, and **the benchmarks exist and are licensed
shut.** P27 is the pattern that follows from the real situation.

**Sell it when:** the buyer asks "how do we know it teaches?" — a North American
district or university with no mandated evaluation, an EMEA ministry facing AI Act
high-risk classification, an APAC buyer with a sovereignty requirement, or a LATAM
institution among the 91% with no formal evaluation mechanism.

### Components

| Role | Component | Licence (payload-verified 2026-10-06) | Why this one |
|---|---|---|---|
| Evaluation harness | [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) | **MIT** | 2,945★, 779 forks, UK AI Security Institute, pushed 2026-10-06. Datasets → solvers → scorers, model-graded evals, tool use, multi-turn dialog. **Do not write a runner.** |
| Red-team harness | [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) | **Apache-2.0** | Singapore IMDA's AI Verify Foundation. Benchmarking **and** adversarial probing in one tool. The only permissive red-teaming harness in this KB. |
| Pedagogical scorer (yours) | written against Inspect's scorer interface | **your client's** | The billable artefact. Encodes the rubric: does it scaffold, does it withhold the answer, does it detect and correct a misconception, does it over-validate. |
| Reference benchmark #1 | [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) | 🔴 **custom Evaluation Dataset License** | 57★, Khan Academy's own math-tutoring benchmark. **Borrowed at measurement time.** |
| Reference benchmark #2 | [`shivanireddyk/tutoreval`](https://github.com/shivanireddyk/tutoreval) | ✅ **MIT** | 0★, one author — but the **only** OSI-licensed pedagogical benchmark found. Vendorable. |
| 🔴 Excluded | `eth-lre/mathtutorbench` (no payload; README claims CC BY 4.0 *and* CC BY-SA 4.0) · `Yunfeng-Wan/CSTutorBench` (CC BY-NC-4.0) | — | Named here so a later pass does not rediscover them as options. |
| Delivery into the LMS | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | ✅ **MIT** (1,098 B) | 🔵 **Re-picked, pass 24.** Was `dmitry-viskov/pylti1.3`, which is **1,416 d cold (commit) / 1,417 d (release)**. This is head commit **2026-10-05 (2 d)**, PyPI `django-lti` **v0.10.1 (61 d)**. Django; the harness is Python, so it launches in-process. |

### Wiring

```
                        ┌─────────────────────────────────────┐
  client's tutor ──────▶│ Inspect (MIT)                       │
  (any model/arch)      │  tasks → solvers → scorers          │
                        │                                     │
   your rubric ────────▶│  custom pedagogical scorer          │──▶ eval logs
                        │   · scaffolding present?            │     (client's,
                        │   · answer withheld?                │      exportable)
                        │   · misconception corrected?        │
                        │   · sycophancy / over-validation?   │
                        └──────────────┬──────────────────────┘
                                       │
          ┌────────────────────────────┴───────────────────────┐
          │                                                    │
  ┌───────▼─────────────┐                        ┌─────────────▼──────────┐
  │ tutoreval (MIT)     │                        │ Khan dataset (🔴)      │
  │ VENDORED into the   │                        │ MOUNTED read-only at   │
  │ deliverable         │                        │ eval time; NEVER in    │
  └─────────────────────┘                        │ the repo, the image,   │
                                                 │ the training set, or   │
  ┌─────────────────────┐                        │ the handover           │
  │ Moonshot (Apache-2) │                        └────────────────────────┘
  │ adversarial pass:   │
  │ jailbreak → answer  │──▶ red-team report
  │ leakage → unsafe    │
  └─────────────────────┘
```

**The licence boundary is a build-system boundary, not a policy document.** Enforce it
mechanically:

1. The Khan dataset lives **outside** the repository — a mount, a fetch step gated on
   an explicit `--external-benchmarks` flag, or an operator-run command. It must not
   be a git submodule, a vendored directory, a Docker layer, or a fixture.
2. CI fails the build if any path under the benchmark mount is reachable from the
   packaging target. One rule in the packaging config; ten minutes to write.
3. The **eval logs are the deliverable** — scores, traces, per-item verdicts. Those
   are "insights and learnings," which clause 3 of Khan's licence expressly permits
   you to use commercially. The dataset rows are not, and must not appear verbatim
   in a report appendix.
4. **Never fine-tune on it.** The licence prohibits model training in terms, and this
   is the mistake most likely to be made by a well-meaning engineer three sprints in.

### Deliverables

- An Inspect task suite + the custom pedagogical scorer — **MIT/client-owned,
  shippable**.
- A Moonshot red-team configuration and its report.
- The **evidence pack**: scores on the client's own content, scores on `tutoreval`,
  comparative findings from the borrowed benchmarks, and the adversarial report.
- A **licence register** naming each component's grant, and the mechanical rule that
  keeps the borrowed datasets out of the artefact.

### ⚠️ Three warnings that are the point of this pattern

- **Do not quote harness construction as the deliverable.** It is free, MIT, and
  maintained by a government. Quoting it is how a proposal loses on credibility.
  Quote the rubric, the scorer, the evidence pack and the licence hygiene.
- **"We benchmarked against Khan Academy's dataset" is sayable; publishing a
  comparative league table from it is not.** The licence prohibits publication and
  redistribution. Keep the comparison inside the engagement.
- **`mathtutorbench` will be suggested to you.** 43★, ETH Zurich, an EMNLP oral —
  it looks like the obvious choice and it has **no licence payload** and two
  contradictory README claims. Treat as ungranted; say so once, in writing, early.

## P28 — Brazilian public-sector school management with AI on top (GPL-2.0 is the feature)

**Sell it when:** the buyer is a Brazilian municipality, state secretariat or public
school network — the engagement most likely to be mispriced by assuming a copyleft
platform is a problem.

### Components

| Role | Component | Licence (payload-verified 2026-10-06) | Note |
|---|---|---|---|
| School management / SIS | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** (`2.12/LICENSE`) | **718★, 547 forks** — the most-forked platform in this KB. Laravel/PHP, tagged `software-publico`. ⚠️ **Default branch is `2.12`**; `main` serves nothing. |
| Offline sync | [`learningequality/morango`](https://github.com/learningequality/morango) | ✅ **MIT** | Peer-to-peer Django model replication, certificate-authenticated, built for low-bandwidth links. SQLite **and** PostgreSQL. |
| Learner-facing delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | ✅ **MIT** | Offline-first learning platform. |
| Evaluation | **Inspect** (MIT) + the P27 scorer | ✅ | The 9%-with-evaluation-mechanisms gap is the differentiator in this region. |
| LMS-side delivery, if any | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | ✅ **MIT** (1,098 B) | 🔵 **Re-picked, pass 24** (was `pylti1.3`, 1,416 d cold). Python, matches the AI tier's language; head commit **2 d**, PyPI `django-lti` **v0.10.1 (61 d)**. |

### Wiring, and why the licence works in your favour

```
  ┌──────────────────────────┐        ┌─────────────────────────────┐
  │ i-educar (GPL-2.0)       │        │ AI tier — SEPARATE PROCESS  │
  │ enrolment · attendance   │◀──────▶│ (your licence)              │
  │ grades · school records  │  REST  │  · early-warning scoring    │
  │ branch 2.12              │        │  · PT-BR tutoring agent     │
  └───────────┬──────────────┘        │  · evaluated via Inspect    │
              │                       └─────────────────────────────┘
       morango (MIT) ──── certificate-authenticated P2P sync ───▶ school servers
              │
      ┌───────▼────────┐
      │ Kolibri (MIT)  │  offline learner delivery in classrooms
      └────────────────┘
```

**GPL-2.0 has no network clause.** Hosting a modified i-educar for a municipality
triggers **nothing** — unlike the AGPL-3.0 platforms (LearnHouse 2,320★, CourseLit
1,269★, Obojobo, Materia), where serving a modified instance obliges you to offer
source to its users. Obligations attach to **distribution**: if you hand the
municipality a modified i-educar, you hand them its source under GPL-2.0.

**And in Brazilian public procurement that is usually what they are asking for.**
`software-publico` is a classification the platform already carries; a buyer who
expects to own and inspect what they bought is a buyer whose requirement the licence
satisfies for free. **Keep the AI tier in a separate process across a REST boundary**
so it carries your own licence, and the question of whether linking occurred never
arises.

### Deliverables

- i-educar deployment pinned to a branch that exists (**`2.12`** — verify before
  every release; this platform does not use `main`).
- The AI tier as an independently licensed service, PT-BR first.
- morango-based sync so school sites work through intermittent connectivity.
- The P27 evidence pack, in Portuguese — **the artefact 91% of LAC institutions
  cannot produce.**

### ⚠️ Warnings

- **Probe the branch, not the convention.** `main` on i-educar serves no licence and
  no README. A `main`+`master` licence probe reports Brazil's largest free education
  platform as ungranted, which is how a real option gets struck off a shortlist.
- **Do not stage this on the Spanish-language GitHub shelf.** Measured 2026-10-06:
  `educación IA aprendizaje` → 10 repositories, **all 0–1★**, one a satirical art
  project. There is no regional component shelf. The components above are global and
  the regionalisation is yours to build.
- **i-educar is PHP/Laravel and your AI tier is Python.** That is a feature here —
  the process boundary that keeps the licences apart is the same boundary the
  language split would have forced anyway.

## P29 — The permissive xAPI analytics spine, with conformance as the deliverable

**When to use it.** A client needs learning analytics and the procurement scores
interoperability (US K-12 and higher-ed rubrics; EU tenders increasingly the same). The
instinct is to reach for Caliper because 1EdTech brands it. **Caliper has no surviving
public reference implementation in any language** (twelfth-pass gap). xAPI does, and the
whole chain is permissive.

### Components — all verified from payload, 2026-10-06

| Role | Repo | Licence | Branch |
|---|---|---|---|
| **Vocabulary / profile** | [adlnet/xapi-profiles](https://github.com/adlnet/xapi-profiles) | Apache-2.0 | `master` |
| **Transport / transform** | [yetanalytics/xapipe](https://github.com/yetanalytics/xapipe) | Apache-2.0 | `main` |
| **Store (LRS)** | [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | Apache-2.0 | `main` |
| **Conformance proof** | [adlnet/lrs-conformance-test-suite](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** | `master` |
| **LMS event source (Open edX)** | [openedx/event-routing-backends](https://github.com/openedx/event-routing-backends) | ⚠️ AGPL-3.0 | `master` |
| **LMS event source (Sunbird)** | [project-sunbird/sunbird-telemetry-sdk](https://github.com/project-sunbird/sunbird-telemetry-sdk) | MIT | `master` |
| **Rostering / SIS context** | [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | Apache-2.0 | `main` |

### Wiring

1. **Define the profile before emitting anything.** Write an xAPI Profile for the client's
   verbs and activity types using `xapi-profiles` as the structural spec and ADL's public
   index (`xapi.vocab.pub`) to reuse existing vocabulary rather than invent verbs. This step
   is what makes the data answerable later; skipping it produces a statement pile.
2. **Emit.** On Open edX, `event-routing-backends` already produces xAPI — but it is
   **AGPL-3.0 and in-platform**, so treat it as *deployed infrastructure you configure*, not
   code you fork into a deliverable. On Sunbird, use the MIT telemetry SDK. For a bespoke
   tutor, emit directly from your own agent code.
3. **Pipe with `xapipe`**, configured **by the profile from step 1** — that is the design
   point of LRSPipe, and it is what keeps transformation rules out of application code.
   ⚠️ **Pin `yetanalytics/xapipe`. `yetanalytics/lrspipe` is a 404** — the product name is
   not the repository name, and this KB logged that false negative twice.
4. **Store** in `xapi-lrs`, or in the client's existing LRS if they have one.
5. 🟢 **Run `lrs-conformance-test-suite` in CI and ship the report.** This is the step that
   makes the pattern worth more than its parts: the suite tests the MUST requirements of the
   xAPI specification, so the deliverable includes **third-party-specified evidence of
   conformance** rather than a claim. In a rubric-scored procurement (trend 26, trend 36)
   that report is the line item.
6. **Join to roster/SIS context via `edfi-oneroster`** so a statement about a learner can be
   resolved to a class, a school and a term — which is what makes the analytics answer an
   administrator's question rather than a developer's.

### Deliverables

- An xAPI Profile document for the client's domain, published.
- A configured pipe + LRS, deployed.
- 🟢 **A conformance report, re-generated by CI on every change.**
- A roster-joined query layer.

### ⚠️ Warnings

- **Do not promise Caliper.** Price a 1EdTech membership or a clean-room build if the client
  insists, and put the choice in the proposal.
- **AGPL reaches `event-routing-backends`.** Configure and deploy it; do not vendor it into a
  proprietary product.
- **The conformance suite tests an LRS, not your pipeline.** It proves the store conforms. If
  the client needs end-to-end assurance, the profile-validation step in `xapipe` is where you
  add it, and that is custom work.

## P30 — The Apache-2.0 component inside an AGPL platform (how education IP stays reusable)

**When to use it.** A client runs Open edX or Moodle — most do — and wants a bespoke AI
component: a tutor inside a course, an analytics panel, a proctoring or accessibility
side-car. Globant wants the component to be **reusable studio IP** across later engagements.

**The insight (trend 34):** the platform's copyleft binds code *in the platform tree*. The
**plugin SDK** does not have the platform's licence.

### Components

| Role | Repo | Licence | Note |
|---|---|---|---|
| **Plugin SDK (Open edX)** | [openedx/XBlock](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** (`master/`**`LICENSE.TXT`**) | 470★. The API your component is written against. |
| Platform core | `openedx/edx-platform` | ⚠️ AGPL-3.0 | Deployed, configured — **never forked into the deliverable**. |
| **Out-of-tree Moodle access** | [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | 🟢 MIT | Reaches Moodle data from outside the tree, which is why it can be MIT. |
| In-tree Moodle plugins | 8 verified this pass | ⚠️ GPL-3.0 | Correct and unavoidable for in-tree work. |
| **LTI 1.3 delivery (Python)** | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 MIT (1,098 B) | 🔵 **Re-picked, pass 24.** Was `dmitry-viskov/pylti1.3` with *"fork and maintain"* — unnecessary now. Head commit **2026-10-05 (2 d)**, PyPI `django-lti` **v0.10.1 (61 d)**, 17 releases. 🔴 **Do not reach for `openedx/xblock-lti-consumer`** here, however well maintained (6 d): it is **AGPL-3.0**, which defeats this pattern's entire purpose. |
| **LTI 1.3 delivery (Java)** | [UOC/java-lti-1.3-provider-example](https://github.com/UOC/java-lti-1.3-provider-example) | MIT | EMEA/Spain lineage. ⚠️ **1,418 days cold** (measured pass 23) — a reference, not a dependency. |
| Reference specification | `LabSirius/TutorIA` (`docs/`) | MIT | A 13-page spec that already chose this shape. |

### Wiring — the decision tree, in order

1. **Can the component live entirely outside the platform?** Then deliver it over **LTI 1.3**
   (`django-lti` / UOC's Java tool) or **MCP** (`moodle-mcp-server` shape). Cleanest IP
   position, works across LMSs, and it is the only option that is portable between a Moodle
   client and a Canvas client.
2. **Does it need to render inside a course page?** Then write an **XBlock** against the
   Apache-2.0 SDK. Your component, your licence.
3. **Does it need to modify platform behaviour?** Then it is in-tree, it is GPL/AGPL, and
   **it is a client deliverable, not studio IP**. Say so in the proposal and price it as
   bespoke.

Order matters: each step down the tree costs IP, so exhaust step 1 before step 2.

### Deliverables

- A component package under a licence Globant chooses.
- A deployment that configures — never forks — the copyleft platform.
- 🔴 **A written packaging review by counsel**, attached to the engagement.

### ⚠️ Warnings

- **The licence file's location does not settle the AGPL question.** Whether a plugin is a
  derivative work turns on linkage and distribution. **This pattern needs legal sign-off
  once per client architecture** — then it is reusable.
- `XBlock`'s licence is at **`LICENSE.TXT`**, uppercase. A lowercase probe will tell you this
  repository is ungranted. It is not.
- **Moodle's in-tree plugin API gives you no such seam.** For Moodle, step 1 (MCP/LTI from
  outside) is the only route to reusable IP.

## P31 — The education test profile for AI Verify (APAC compliance as an upstream contribution)

**When to use it.** An APAC engagement — Singapore, or any client that accepts IMDA's
framework as a reference — needs demonstrable AI governance for an education deployment.

**The insight (trend 36):** APAC is the only region where the **regulator's own conformance
harness is permissively licensed and designed to be extended**. Compliance evidence can be
produced *by the regulator's instrument* instead of asserted by the vendor.

### Components

| Role | Repo | Licence |
|---|---|---|
| **Governance test framework** | [aiverify-foundation/aiverify](https://github.com/aiverify-foundation/aiverify) | Apache-2.0, 98★ |
| **Plugin / test-widget kit** | [aiverify-foundation/aiverify-developer-tools](https://github.com/aiverify-foundation/aiverify-developer-tools) | Apache-2.0 |
| **Red-team / benchmark assets** | [aiverify-foundation/moonshot-data](https://github.com/aiverify-foundation/moonshot-data) | Apache-2.0 |
| **Pedagogy-knowledge probe** | `AI-for-Education/pedagogy-benchmark` | MIT |
| **Classroom-discourse measurement** | [stanfordnlp/edu-convokit](https://github.com/stanfordnlp/edu-convokit) | MIT |
| ⚠️ Evals index | `aiverify-foundation/LLM-Evals-Catalogue` | 🔴 **ungranted** — cite, do not vendor |

### Wiring

1. **Stand up `aiverify`** against the client's education model or agent.
2. **Build an education test plugin** with `aiverify-developer-tools`. There is **no
   education-specific profile in AI Verify today** (declared gap, twelfth pass), so define
   one: age-appropriateness, curriculum-alignment fidelity, refusal behaviour on assessment
   integrity, and **human-override reachability** — the property US state law and Korea's AI
   Basic Act both require.
3. **Source the test content from permissive instruments, not from benchmarks you cannot
   ship.** `pedagogy-benchmark` (MIT) for pedagogical knowledge; `moonshot-data` for
   adversarial cases; `edu-convokit` to measure discourse quality on real transcripts after
   anonymisation. ⚠️ Several named education benchmarks in this KB are **licence-shut**
   (trend 31) — the harness is free, the benchmarks are often not. Check each one before it
   enters a deliverable.
4. 🟢 **Contribute the profile upstream.** Once merged it becomes a reference other
   implementers must meet, and the client's compliance artefact is then produced by a
   government-recognised tool carrying Globant's contribution.
5. **Pair with national readiness documents**: Korea (AI Basic Act, in force 22 Jan 2026),
   Vietnam (Law 134/2025/QH15, 1 Mar 2026), Australia (TEQSA institutional action plans).

### Deliverables

- A deployed AI Verify instance with an education profile.
- Test reports per release.
- 🟢 An upstream PR to `aiverify-developer-tools`.
- National readiness documents per jurisdiction.

### ⚠️ Warnings

- **Do not infer licences from the organisation.** Two of the three `aiverify-foundation`
  repositories used here are Apache-2.0; `LLM-Evals-Catalogue` in the same org has **no
  grant**.
- **AI Verify validates against principles; it does not confer legal compliance.** Korea's
  and Vietnam's statutes impose duties a test report alone does not discharge.
- **Upstream contribution is a commitment.** A merged profile that then rots is worse for
  the client's evidence than one maintained privately. Budget maintenance.

## P32 — The Portuguese-language permissive component (the LATAM position with no incumbent)

**When to use it.** A Brazilian engagement, or a Globant investment decision about durable
regional IP.

**The insight (trend 37):** measured with `total_count`,
`tutor inteligência artificial educação aprendizagem` returns **0**. The
Portuguese-language permissive AI-tutoring shelf **does not exist** — and Brazil is the
largest education system in the region. There is no incumbent to displace.

### Components

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| **Architecture to copy** | [thiagoluzin/pemara-edu-mira](https://github.com/thiagoluzin/pemara-edu-mira) | **MIT**, 0★ | The only Portuguese permissive asset in this KB. **School-LAN deployment, offline-capable, optional AI** — the architecture Brazilian school infrastructure actually supports. |
| **Offline delivery base** | Kolibri | MIT | Proven offline-first platform. |
| **Exam-domain data** | [yunger7/enem-api](https://github.com/yunger7/enem-api) | ⚠️ GPL-2.0 | **ENEM**, Brazil's national entrance exam. Copyleft — run it as a service, do not vendor it. |
| **School management** | `portabilis/i-educar` (branch **`2.12`**) | ⚠️ GPL-2.0 | Brazil's largest free school-management platform. Fork is published — usually acceptable for a public client (P28). |
| **Local inference** | Ollama | MIT | Per-seat cloud inference is the binding cost constraint in this market. |
| **Lesson generation** | [AkshitIreddy/AI-Powered-Video-Tutorial-Generator](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator) | MIT, 313★ | Runs **local models**; video lessons where bandwidth is scarce but a projector is not. |
| **Project-based LMS** | [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | MIT, 978★ | If the engagement needs a full platform rather than a component. |

### Wiring

1. **Scope it as a component, not a platform.** The gap is a *component* gap; a platform
   competes with `i-educar` and Moodle, which are entrenched and free.
2. **Build Portuguese-first, not Portuguese-translated.** Brazilian curriculum structure
   (BNCC), Brazilian grade levels, Brazilian assessment conventions. A Spanish component with
   translated strings is what the 0 count already reflects — the Spanish shelf has 2 live
   repositories and none of them crossed the language boundary.
3. **Default to local inference (Ollama) with cloud as an opt-in.** Cost, not capability, is
   the constraint.
4. **Deploy to a school LAN**, following `pemara-edu-mira`: no dependence on public internet
   during a lesson.
5. **Publish under MIT**, in Portuguese, with a Portuguese README. 🟢 **The licence and the
   language are the differentiators** — the code is the easy part.
6. **Integrate, do not absorb, the copyleft layer.** Call `enem-api` and `i-educar` over their
   interfaces.

### Deliverables

- An MIT, Portuguese-language, offline-capable education component, published.
- A BNCC-aligned content mapping.
- A school-LAN deployment guide.

### ⚠️ Warnings

- **`pemara-edu-mira` is 0★ and a one-person project.** Copy the *architecture*; do not pin it
  as a dependency.
- **Publishing is the point.** An internal-only component does not take this position — the
  gap is a published-supply gap.
- ⚠️ **Licence hygiene is the regional failure mode, not licence choice.** Two LATAM
  repositories probed this pass carry **no grant at all**. Whatever is built here, attach the
  licence in the first commit.

## P33 — Sovereign avatar-and-voice tutoring, on a platform that already ships it (EMEA first; the same build serves LATAM)

**When to use it.** A public-sector or university client wants conversational AI tutoring
with a **spoken or embodied** interface, and student data **cannot leave the institution or
the region**. Previously this KB answered that request by specifying the stack component by
component (P4) and accepting a 10–12 week build. **It is now mostly a configuration
exercise**, because a permissive platform ships the sovereign path as a setting.

**Why this pattern exists now.** Two facts found in the thirteenth pass:

1. [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
   (**BSD-3-Clause**) ships **local RAG**, **voice / video / 3D-avatar modes**, **RBAC** and
   **Ollama serving** in the same configuration surface as hosted APIs — and is funded by
   Morocco's Ministry of Higher Education, the DDA and the CNRST.
2. The research alternative is **not obtainable**. The **VTutor** animated-pedagogical-agent
   SDK has three papers and a live demo, but no licence payload and an **empty**
   `VTutorTools` organisation. **Do not plan around it.**

### The stack — every component payload-verified permissive

| Layer | Component | Licence | Role |
|---|---|---|---|
| Tutoring platform | [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** | Tutoring loop, learner onboarding, per-learner assistant, avatar presentation, RBAC |
| Model serving | [`ollama/ollama`](https://github.com/ollama/ollama) | MIT | Open-weight models on institutional hardware. **Already a first-class target of the platform** — not an integration |
| Serving at cohort scale | [`vllm-project/vllm`](https://github.com/vllm-project/vllm) | Apache-2.0 | Swap in when concurrency outgrows Ollama |
| Retrieval | [`pgvector/pgvector`](https://github.com/pgvector/pgvector) | **PostgreSQL Licence** (permissive) | Vectors **inside Postgres** — no separate vector store to host, secure and keep in-region |
| Document ingestion | [`opendatalab/MinerU`](https://github.com/opendatalab/MinerU) | Apache-2.0 | Curriculum, textbooks and scanned material into structured text for the local RAG |
| Real-time voice | [`livekit/livekit`](https://github.com/livekit/livekit) | Apache-2.0 | WebRTC transport for spoken practice and oral assessment beyond what the platform ships |
| Audit trail | [`langfuse/langfuse`](https://github.com/langfuse/langfuse) | MIT **outside `ee/`** | Every model call with cost, latency and output — the Article 50 evidence, produced as a by-product |
| Typed decisions | [`pydantic/pydantic-ai`](https://github.com/pydantic/pydantic-ai) | MIT | Any assessment-adjacent output as a validated schema, never free text |
| LMS seam | [`IMSGlobal/LTI-Tool-Provider-Library-PHP`](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | Apache-2.0 | The permissive doorway into an incumbent Moodle / Canvas / Open edX — **side-car, never a fork** |

### Wiring

1. **Stand the platform up against local inference first.** Deploy `open-tutor-ai-CE` with
   **Ollama** as the only configured provider and no hosted API key present. This is the
   step that is a setting rather than a build, and doing it first means the sovereign
   posture is the default configuration rather than a later hardening pass. Prove a tutoring
   turn end to end before adding anything.
2. **Point the local RAG at real curriculum.** Run the client's syllabi, textbooks and past
   papers through **MinerU**, load them into **pgvector** in the platform's own Postgres.
   One database for relational and vector state — one thing to host in-region, back up and
   certify.
3. **Put Langfuse in front of every model call, before the pilot opens.** Retrofitting an
   audit trail after a pilot has run means the pilot has no trail. **Exclude `ee/` from any
   vendored copy and record the holder as ClickHouse, Inc.** as well as the licence.
4. **Wrap every assessment-adjacent output in a `pydantic-ai` schema.** Grades, mastery
   estimates, placement and progression as validated objects with the inputs that produced
   them. This is the P22/P24 artefact the procurement rubric and the Annex III file both
   consume, and it is what makes **human-final** (trend 16) enforceable in code rather than
   in policy.
5. **Add voice only where it is assessed.** The platform's own voice/avatar modes cover
   conversational practice. Reach for **LiveKit** when you need multi-party sessions, oral
   examination with recording, or latency control you must own.
6. **Keep the incumbent.** Enrolment, roster and gradebook stay in the institution's
   existing LMS; integrate over **LTI 1.3** so none of the above inherits AGPL or GPL. The
   tutoring platform is a tool the LMS launches, not a replacement for it.

### Compliance, mapped to the real clock

🟢 **The near-term EU deliverable is labelling, not conformity.** **Article 50 transparency
duties have applied since 2 August 2026.** The Digital Omnibus
(**Regulation (EU) 2026/1744**) deferred **Annex III stand-alone high-risk** obligations to
**2 December 2027** and **Annex I embedded** to **2 August 2028**.

- **Now:** AI interaction is disclosed to the learner, and synthetic output is marked. Steps
  1–3 deliver this.
- **By December 2027:** if the deployment touches admission, evaluation of learning
  outcomes, placement, or exam/behaviour monitoring, it is **Annex III high-risk**. Steps 3
  and 4 are the risk-management, data-governance, human-oversight and record-keeping
  evidence — built in, not retrofitted.
- ⚠️ **Scope the boundary explicitly in the SOW.** A tutor that *practises* is not
  high-risk; the moment its output informs a grade or a progression decision, it is. The
  cheapest compliance decision available is **keeping the tutor on the practice side of that
  line** and routing assessment through the LMS.

### Timeline and the honest caveats

**6–8 weeks** to a governed pilot: ~1 week platform and local inference, ~2 weeks curriculum
ingestion and retrieval, ~1 week observability and typed outputs, ~1 week LTI integration,
2–3 weeks hardening and evidence pack. 🔵 **That is 4 weeks faster than the P4 build it
replaces**, and the saving is entirely in steps 1–2.

- 🔴 **Pin a commit.** 192 forks against 108 stars means much real-world use sits in
  divergent forks nobody tracks.
- 🔴 **Raise the holder question before contract.** The payload reads *"Mohamed El hajji On
  behalf of all **R2D-dev**"*, and **R2D-dev appears in no public artefact of the project**.
  On a redistribution engagement that is the party an indemnity question routes to.
- ⚠️ **Check the open-core line against the client's must-haves.** Theming, SLA and LTS sit
  in the paid Enterprise Edition. The CE grant is unqualified and **this is not a directory
  carve-out like Langfuse's `ee/`** — but the roadmap is set by a party with an incentive to
  keep features above the line. Get the answer in writing at proposal time.
- ⚠️ **Cite the payload, not a catalogue.** Third-party catalogues list this project as
  Apache-2.0; it is **BSD-3-Clause**, confirmed from the payload by two passes at the same
  1,531 bytes. Both are permissive, but the attribution clauses differ.
- 🟢 **For LATAM, this is the same build with a localisation workstream.** The thirteenth
  pass found no LATAM-origin permissive equivalent — the Portuguese channel returned two MIT
  assets at 2★ and 0★. **Localise this platform** (it already serves local models and local
  RAG) rather than waiting for one; pair with **P32** if the localisation work is published
  back as the permissive Portuguese-language component that shelf still lacks.

## P1 update, fourteenth pass of 2026-10-06 — the default engagement shape now has four platform doors, not two

P1 (LTI + MCP side-car tutor) was written when the only platforms with a permissive,
payload-backed MCP side-car were **Canvas** and **Moodle**. Measured this pass, the door
list is four, and the choice is now made on the client's existing LMS rather than on what the
shelf happens to carry:

| Client runs | Side-car to start from | Licence (payload) | ★ |
|---|---|---|---|
| Canvas LMS | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 278 |
| Moodle | [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) · [1alexandrer/moodle-mcp](https://github.com/1alexandrer/moodle-mcp) 🆕 | MIT · MIT | 43 · 18 |
| 🆕 **Brightspace / D2L** | [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) (features, npm) · [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) (**opt-in writes**, circuit breaker, multi-auth) · [pranav-vijayananth/brightspace-mcp-server](https://github.com/pranav-vijayananth/brightspace-mcp-server) (**Apache-2.0**) | MIT · MIT · Apache-2.0 | 57 · 12 · 6 |
| 🆕 **Blackboard Learn / Ultra** | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) — **RBAC middleware in the MCP layer** | MIT | 2 |

⚠️ **Two selection rules this adds.** On Brightspace, take the **feature** server for scope
and read the **multi-auth** one before designing any write path — it is the only asset in the
tier that models TOTP/OAuth/browser auth, retries and circuit-breaking, and LMS auth is where
these integrations actually fail. On Blackboard the tier is five repositories deep, so expect
to fork rather than adopt — and start from `bb-mcp` **because of its RBAC middleware**, which
is the control an education deployment is audited on and which no other asset in the
98-address cluster implements.

## P28 — The K-12 administrative integration (the empty tier, built properly)

**When to use.** A school district, a ministry, or a K-12 group asks for an agent over its
own administrative systems — Google Classroom, a student information system, guardians,
enrolment, accommodations. **This is the pattern for a tier with no incumbent**: Google
Classroom measures 17 open-source integration repositories whose best dedicated server has
**6★**, and PowerSchool measures **`total_count: 0`** (trend 39).

### Components

| Component | Repo | Licence (payload read 2026-10-06) | Role |
|---|---|---|---|
| Workspace-for-Education surface | [Kimmahone/edu-workspace-mcp](https://github.com/Kimmahone/edu-workspace-mcp) | **MIT** (1,087 B) | Docs, Sheets, Slides, **Forms**, Drive, Classroom. **Start here, not from a Classroom-only server** — Forms is where K-12 assessment lives. |
| Classroom reference implementation | [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | **MIT** (1,063 B) | The tier's best dedicated server (6★, 9 forks). Read it for the Classroom API surface; expect to extend it. |
| **Role separation** | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | **MIT** (1,063 B) | Not for Blackboard here — **lift its RBAC middleware pattern.** Teacher, student, guardian and administrator must be distinct principals in the MCP layer, not in the prompt. |
| Accommodations vocabulary | [GarphenGate/moltline-mcp](https://github.com/GarphenGate/moltline-mcp) | **MIT** (1,072 B) | 8 skills across curriculum, classroom, **accommodations**, exam prep. The only asset in this KB that names accommodations as a surface. |
| Typed outputs | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | MIT | Every record-touching decision returns a validated schema, never free text. |
| Orchestration + audit | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT | Checkpoints are the audit trail. |
| Observability | [langfuse/langfuse](https://github.com/langfuse/langfuse) | **MIT outside `ee/`** | Trace every call, cost and output. ⚠️ Keep the deployment out of `ee/`. |
| Retrieval | [pgvector/pgvector](https://github.com/pgvector/pgvector) | PostgreSQL Licence | Vectors inside the district's existing Postgres — no second datastore to secure. |

### Wiring

1. **Scope to read-only for the whole of phase one.** Every component above supports it;
   `edu-workspace-mcp` and the Classroom server are read-first by design. No write path ships
   until the oversight gate in step 5 exists and has been exercised.
2. **Authenticate as the institution, not as a user.** This is the barrier that emptied the
   tier (trend 39) and the one an integrator clears: Google Workspace for Education
   domain-wide delegation, scoped to the minimum API set, with the scope list in the SOW.
3. **Put RBAC in the MCP layer** — the `bb-mcp` pattern. One principal per role; a tool a
   guardian may call is a *different tool* from the teacher's, not the same tool with a
   different prompt. Guardian access to another child's record must be impossible by
   construction, not by instruction.
4. **Index curriculum and policy documents through MinerU → pgvector**, keeping the source
   document id on every chunk so an answer can always be traced to a page.
5. **Gate every write and every consequential read behind a named human.** US state law has
   converged on one testable rule — human judgment is final (trend 16) — and the EU treats
   these systems as high-risk. The gate is a LangGraph node that cannot be bypassed, and
   Langfuse records who passed it.
6. **Handle accommodations as a first-class, logged capability**, using the moltline
   vocabulary. An accommodation is a legal entitlement; an agent that silently fails to apply
   one is a compliance incident, not a bug.

### Deliverables

- A read-only Workspace-for-Education / SIS MCP server deployed inside the district's
  boundary, with per-role tool sets and the scope list documented.
- An RBAC matrix (role × tool × data class), reviewed by the client's counsel.
- A Langfuse trace archive demonstrating every access and every gate decision.
- A written accommodations-handling note: which entitlements the system reads, which it
  applies, and which it explicitly refuses to decide.
- The P22 licence-reliability gate output for every component.

### ⚠️ Three warnings that are the point of this pattern

- 🔴 **Do not start from the ungranted assets in this tier, however convenient.**
  `zainf2327/mcp-classroom` **auto-grades submissions and carries no licence of any kind**;
  `shimahikojin/google-classroom-mcp` likewise; `AStheTECH/mewcp-google-classroom` carries a
  bespoke **"Community License"** that forbids commercial use, hosted service, rebranding and
  anything competitive, with automatic termination on breach. All three are unusable in a
  Globant deliverable and the third is the one most likely to be mistaken for usable.
- ⚠️ **`total_count: 0` for PowerSchool means no *open-source* asset, not no integration.**
  The client may already pay for a vendor integration. Ask before positioning the work as
  greenfield.
- 🔵 **The empty tier is empty because of authorisation, so the credential conversation is
  the critical path.** Start it in week one; it will outlast the build.

## P29 — Curriculum alignment as a tool call (the Skolverket shape, and how to port it)

**When to use.** Any engagement where *"aligned to the national curriculum"* is a
procurement requirement — which, in EMEA and in the APAC mandate regimes, is most of them.
Replaces a human-written mapping that is stale on the day it ships with a call the product
makes on every run (trend 42).

### Components

| Component | Repo / source | Licence | Role |
|---|---|---|---|
| National curriculum surface | [isakskogstad/Skolverket-MCP](https://github.com/isakskogstad/Skolverket-MCP) | **MIT** (payload, 1,093 B) | Sweden: Läroplan/syllabus API, Skolenhetsregistret school-unit register, Planned Educations. The reference implementation to copy. |
| The counter-case to plan for | [3121n/nor-data-udir-mcp](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **none** | Norway's equivalent public data, **no grant**. Read it as the expected state, not the exception. |
| Document ingestion | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Apache-2.0 | For the parts of a curriculum published as PDF rather than API — i.e. most countries. |
| Typed alignment claims | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | MIT | An alignment is a schema — `{objective_id, source_uri, confidence, evidence_span}` — never prose. |
| Orchestration | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT | Re-run alignment as a graph step with checkpoints. |
| Retrieval | [pgvector/pgvector](https://github.com/pgvector/pgvector) | PostgreSQL Licence | Curriculum objectives indexed in-region. |
| Observability | [langfuse/langfuse](https://github.com/langfuse/langfuse) | MIT outside `ee/` | Every alignment claim traceable to the call that produced it. |

### Wiring

1. **Check for an authority API first, then for a wrapper, then expect to write one.** The
   three outcomes, in order of likelihood: public API with no wrapper (write a thin MIT one —
   small, bounded, reusable); public API with an ungranted wrapper (fork the shape, write your
   own grant, or ask for one — see Udir); public API with a permissive wrapper (Sweden — the
   lucky case).
2. **Pin the curriculum version.** A syllabus API returns *today's* curriculum. An assessment
   decision made last term must be explainable against the curriculum as it stood then, so
   persist the objective set with a retrieval timestamp and never resolve historical claims
   against a live call.
3. **Make the alignment claim auditable, not confident.** Each generated item or lesson
   carries `{objective_id, source_uri, evidence_span}` pointing into the authority's own text.
   A reviewer must be able to click from an item to the clause it claims to satisfy.
4. **Re-run alignment on a schedule and diff it.** When the authority changes a syllabus, the
   diff is the client's change notice — and producing it automatically is a sellable
   capability on its own.
5. **Keep the data-terms diligence separate from the licence check**, per the warning below.

### Deliverables

- A curriculum-alignment service with a typed claim schema and per-claim provenance.
- A pinned, versioned local objective set with retrieval timestamps.
- A **data-terms memo**: what the authority's own terms permit for the data (distinct from the
  wrapper's licence), signed off before launch.
- An alignment-diff report, scheduled.
- P22 gate output for the wrapper.

### ⚠️ Two warnings that are the point of this pattern

- 🔴 **The wrapper's licence is not the data's licence, and this is the error the pattern
  exists to prevent.** Skolverket-MCP's copyright line reads **"Skolverket Syllabus MCP
  Contributors"**, *not the agency*. MIT covers the **code**; the **agency's terms govern the
  corpus**. A proposal citing "MIT" for a national-curriculum capability is citing the
  connector and implying the corpus — trend 22's corpus-pricing error arriving through a
  cleaner door.
- ⚠️ **Do not generalise "a permissive wrapper exists" from one country.** Two Nordic
  authorities, same idea, same public-data quality: one MIT, one ungranted. Budget the wrapper
  as work in every country until proven otherwise.

## P30 — Gated auto-grading with a real execution step

**When to use.** Assessment work — the regulated frontier this KB has tracked since trend 7,
and the one where the open-source tier has been thinnest. Three components verified this pass
make a complete loop possible under permissive licences **for the first time in this KB**:
grading from a vendor, execution in a sandbox, and mastery tracking.

### Components

| Component | Repo | Licence (payload read 2026-10-06) | Role |
|---|---|---|---|
| Exam authoring, delivery, **auto-grading** | [ictinnovations/ictexam-mcp](https://github.com/ictinnovations/ictexam-mcp) | **MIT** (1,114 B, **corporate holder**) | Read exams, gradebooks and **per-question item analysis**; parse a paper into a structured exam; publish to students. **Writes are off unless explicitly enabled** — adopt that default, do not reinvent it. |
| 🆕 **Code execution** | [taybenlor/runno](https://github.com/taybenlor/runno) | **MIT** (1,106 B) | WASM/WASI sandbox. **`@runno/mcp` 0.10.6 (MIT on npm)** makes the sandbox agent-callable, so the grader executes the submission instead of predicting its output. |
| Mastery, two families | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) · [HumphreySun98/Smart-Study-Agent](https://github.com/HumphreySun98/Smart-Study-Agent) | MIT · **MIT** (1,067 B) 🆕 | Bayesian Knowledge Tracing (auditable, published) and **RL policy + FSRS scheduling**. Two different defensible answers to *"why this item next"*. |
| Standards conformance | [pie-framework/pie-qti](https://github.com/pie-framework/pie-qti) | ISC | QTI 2.1/2.2/3.0 player, bidirectional QTI ↔ PIE. Keeps the item bank portable. |
| Typed outputs | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | MIT | A grade is a schema with evidence, never a sentence. |
| Orchestration + gate | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT | The oversight gate is a node, and it cannot be routed around. |
| Observability | [langfuse/langfuse](https://github.com/langfuse/langfuse) | MIT outside `ee/` | The evidence pack is a by-product of running. |

### Wiring

1. **Author and deliver through the exam platform's read surface**; keep its write scope off
   until step 5 is in place. Pull **per-question item analysis** — it is the signal that tells
   you whether the *item* is bad rather than the cohort.
2. **Execute, do not predict.** For any submission that is code, run it in `@runno/sandbox`
   via `@runno/mcp` and grade the **actual** output. The model reasons about observed
   behaviour; it never asserts what the code "would" do.
3. **Grade into a typed claim**: `{score, rubric_id, evidence_span | execution_trace,
   confidence}`. Free-text justification is an attachment to the claim, never the claim.
4. **Route low confidence and every high-stakes item to a human**, and record the routing
   decision. US state law has converged on human judgment being final (trend 16); the EU
   treats this as high-risk.
5. **The write-back gate**: no grade reaches the gradebook except through a node that records
   a named human's decision. This is where the ICTExam write scope is finally enabled, and
   never before.
6. **Feed accepted outcomes into the mastery model** — BKT for an auditable, published
   instrument; RL+FSRS where review scheduling matters more than explainability. **Name which
   one, and why, in the deliverable.**

### Deliverables

- An auto-grading pipeline with writes gated behind a named human and traced end to end.
- Execution traces for every code-graded submission, retained with the grade.
- A rubric registry with per-rubric accuracy against the human-reviewed sample.
- Item-analysis reports distinguishing a weak cohort from a bad item.
- A mastery-model selection note: which family, what it can and cannot explain.
- P22 gate output for every component; P27's evidence pack as the external-facing artefact.

### ⚠️ Three warnings that are the point of this pattern

- 🔴 **A browser or WASM sandbox is not an anti-cheat boundary.** Runno protects the host from
  the code, not the assessment from the student. For proctored or high-stakes assessment,
  execution stays server-side; use Runno for formative practice, feedback and teaching.
- ⚠️ **Check Runno's language coverage against the client's actual curriculum.** WASI
  sandboxing covers languages with a WASI target; verify against the published packages
  rather than assuming.
- 🔴 **Borrow no benchmark into the deliverable.** The pedagogy benchmarks this KB has
  measured are licensed shut — Khan's dataset permits evaluation and forbids redistribution,
  production use and training; `CSTutorBench` is CC BY-NC. Evaluate with them where their
  terms allow, ship **none** of them, and keep the harness (P23) as the asset.

## P25 — The SIS integration engagement (wrap an MIT client; do not build the client, do not wait for a licensed MCP server)

**When to use it.** The client is a school district, a university or a federal institute, and
the ask is administrative rather than instructional: attendance, grades, scheduling,
guardian communication, enrolment, "an assistant that answers questions about our student
data." This is the shape of most K-12 engagements and most public-sector higher-education
engagements in Brazil.

**The finding it is built on** (fifteenth pass, `agents/top.md` Finding 4): in the
PowerSchool tier, **both MCP servers are ungranted and three of four API clients are MIT**.
The grant sits exactly one layer below the layer an agent engagement wants. So the cheapest
correct move is to take the licensed layer and write the thin one yourself.

### Components

| Role | Component | Licence (payload-verified 2026-10-06) |
|---|---|---|
| SIS client — Python | [`dougpenny/PyPowerSchool`](https://github.com/dougpenny/PyPowerSchool) | **MIT** |
| SIS client — Node | [`aydenp/PowerSchool-API`](https://github.com/aydenp/PowerSchool-API) | **MIT** |
| SIS client — PHP | [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | **MIT** |
| SIS client — FR | [`bain3/pronotepy`](https://github.com/bain3/pronotepy) | **MIT** |
| SIS client — DE/AT | [`python-webuntis/python-webuntis`](https://github.com/python-webuntis/python-webuntis) | **BSD-2-Clause** |
| SIS client — NL | [`magister-api/magister`](https://github.com/magister-api/magister) · [`elisaado/somtoday.js`](https://github.com/elisaado/somtoday.js) | **MIT** |
| SIS client — BR | [`ivmelo/suap-api-php`](https://github.com/ivmelo/suap-api-php) · [`PucaVaz/sigaa-tools`](https://github.com/PucaVaz/sigaa-tools) | **MIT** |
| **MCP wrapper** | 🔧 **Globant-built** — ~300 lines over the client above | your client's terms |
| Reference design for the wrapper | [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) (20 tools, RBAC-aware) · [`kc0506/ntucool`](https://github.com/kc0506/ntucool) (Rust) | **MIT** — read them, do not necessarily deploy them |
| **Production access path** | OneRoster / Ed-Fi permissive implementations (interoperability tier, tenth pass) | permissive |
| Oversight gate | **P11** (gated generation) | — |
| Access-rights gate | **P26** — **run this first** | — |

### Wiring

1. 🔴 **Run P26 before writing any code.** If the institution has no API agreement with its
   SIS vendor, everything below is a prototype and must be labelled one in the SOW.
2. Pick the MIT client that matches the client's SIS and your delivery language. Vendor it,
   do not fork it — these libraries are small and stable, and the licence lets you.
3. Write the MCP server yourself over the client's own method surface. **Read
   `infinitecampus-mcp` first for its tool decomposition** (academics / daily life /
   documents / messaging / healthcheck) and for its RBAC middleware shape — this is the one
   governance-aware design in the tier.
4. 🔴 **Writes off by default.** Every tool that mutates a student record is opt-in, behind an
   explicit configuration flag, and routed through P11's oversight gate. The SIS is the
   system of record for regulated data; an agent that writes to it without a human gate is
   the single highest-liability thing in this entire KB.
5. Swap the transport, not the tools, when the official API arrives: keep your MCP tool
   signatures stable and re-point them from the community client to the OneRoster/Ed-Fi
   endpoint. **This is the whole reason to own the wrapper layer** — the access path changes
   and your deliverable does not.
6. Scope data egress explicitly: student records are FERPA (US), and under-13 data is
   additionally COPPA; in EMEA this is GDPR Article 9-adjacent and the EU AI Act's Annex III
   education classification applies. **Do not route student records through a shared LLM
   context and do not train on them.**

### Deliverables

- An MCP server the client owns, over a vendored MIT client, with writes gated.
- A P26 access-rights memo naming the vendor, the ToU clauses read, the date read, and
  whether an API agreement exists. **This is a deliverable, not an internal note.**
- A migration note: what changes when the official API entitlement lands (transport only, if
  step 5 was respected).

### ⚠️ Three warnings that are the point of this pattern

1. 🔴 **The community client's licence does not grant API access.** See **P26** and trend 33.
   An MIT licence on a scraper is a grant to copy the scraper.
2. ⚠️ **`GeovaneSchmitz/sigaa-api` (MIT, 61★) is archived and self-describes as a web
   scraper.** It is excellent reference material for how SIGAA's surface works and a poor
   production dependency. Prefer `PucaVaz/sigaa-tools` (MIT, 24★, active).
3. ⚠️ **`shinyquagsire23/InfiniteCampusAPI` is WTFPL** — permissive in substance, not
   OSI-approved, and rejected by name by some corporate allowlists. If the client runs an
   automated licence gate, expect to justify it or choose another client.

---

## P26 — The access-rights gate (run before any component that talks to a system you do not own)

**This is the gate trend 33 made necessary, and it is the first gate in this KB that does not
look at a licence.** P22 (the licence-reliability gate) answers *may we copy this code?*
P26 answers *may we call this system?* **A component must pass both.** Most of the SIS tier
passes P22 cleanly and fails P26.

### The gate — four checks, in order, all cheap

| # | Check | How | 🔴 Fail condition |
|---|---|---|---|
| **A1** | **Is the access path official?** | Read the component's README and source for the endpoints it calls. Compare against the vendor's published API documentation. | The component calls endpoints absent from the vendor's public API docs — mobile-app JSON, portal internals, HTML scraping. |
| **A2** | **What does the vendor's ToU say?** | Fetch the vendor's Terms of Use and search for: *publicly supported interfaces*, *scraping*, *automated access*, *crawl*, *train*, *artificial intelligence*, *reverse engineer*, *derivative*. **Record the URL and the date read.** | The ToU prohibits the means of access the component uses — or prohibits AI training on the content. |
| **A3** | **Does the institution hold an API agreement?** | Ask the client directly: *"do you have an API entitlement with your SIS vendor, and may we see its scope?"* | No agreement, or an agreement that does not cover programmatic third-party access. |
| **A4** | **What regulation attaches to the data?** | Classify the records the component reaches. | Student records without a lawful basis for the processing: **FERPA** (US), **COPPA** (US, under-13), **GDPR** + EU AI Act Annex III (EMEA), LGPD (Brazil). |

### Why all four, and in that order

**A1 is the cheapest and it predicts the other three.** A component that calls undocumented
endpoints will almost always fail A2, and A1 takes one README and one docs page. Run it
first and most candidates resolve in minutes.

**A2 is the one that is invisible to every tool in this KB.** It is not in the repository.
No licence scanner, SBOM, allowlist or payload probe reaches it — it lives on the vendor's
website, and it changes without notice, which is why the gate requires the **date read** to
be recorded next to the verdict.

**A3 is the one that converts a failure into a pass.** The same community client that is
unusable for a district with no entitlement becomes legitimate for a district with one,
because the institution's own contract covers the access. **This is the question that
decides whether the engagement is scoped as a prototype or as production.**

**A4 survives a pass on A1–A3.** Lawful access is not lawful processing. An institution may
be perfectly entitled to its own data and still unable to route it through a third-party
model.

### Outputs, and what each verdict means

| Verdict | Condition | What you may deliver |
|---|---|---|
| 🟢 **PRODUCTION** | A1 official **or** A3 agreement in place, A2 clean for the intended use, A4 lawful basis documented | Ship it. Normal P22 licence rules apply on top. |
| ⚠️ **PROTOTYPE ONLY** | A1 fails, A3 absent, A4 satisfiable | Build it, demo it, **label it in the SOW as a non-production proof of workflow**, and quote the official-API path as the production phase. |
| 🔴 **BLOCKED** | A2 prohibits the use and A3 cannot cure it, **or** A4 has no lawful basis | Do not deliver. Propose the official API or an open platform (⚠️ GPL — see `verticals/solutions.md`). |

### The worked example, from this pass

`chrischall/infinitecampus-mcp`, MIT, 20 tools:

- **A1** 🔴 fails — calls `/campus/api/oneRosterCampus` and `/portal/api/...`; the maintainer
  states these *"are not publicly supported interfaces."*
- **A2** 🔴 fails — [Infinite Campus ToU](https://www.infinitecampus.com/terms/terms-of-use)
  (quoted in the repository's README, read by the maintainer 2026-05-23) forbids access *"by
  any means other than our publicly supported interfaces (for example, scraping or using the
  content to train artificial intelligence software)"*; the maintainer adds that *"IC may
  treat this as a ToS violation."*
- **A3** — unknown per engagement; **this is the question to ask the district.**
- **A4** 🔴 FERPA and COPPA both attach; the repository itself says *"do not… train AI models
  on student records."*

⚠️ **Provenance:** the ToU wording above is quoted from the **repository's README** (the
maintainer dates their reading 2026-05-23); `infinitecampus.com` is egress-blocked from this
environment, so it is **not** first-hand verified here. **A2 therefore carries an explicit
re-read instruction** — that is exactly why the check requires the URL *and the date read*
to be recorded beside the verdict.

**Verdict: 🔴 BLOCKED as a deliverable; ⚠️ PROTOTYPE ONLY where a district authorises it on
its own data; 🟢 the production path is PowerSchool's or Infinite Campus's OneRoster
entitlement.** The licence was never the problem — and that is the whole point of this gate.

🔵 **Note for the proposal, not just the gate.** A cookie-bridge in a repository — such as
the browser extension `infinitecampus-mcp` uses to lift a session token from a logged-in tab
— is evidence that an install base wants agent access its vendor does not yet sell.
**That is a product opportunity to raise with the vendor, and an anti-pattern to decline in
client delivery.**

---

## P25 — Curriculum alignment against a government endpoint (EMEA, Norway shape — and the substitution for everywhere else)

**The problem every other curriculum pattern in this file has had to assume away.** `P9`, `P15`,
`P16` and `P19` all generate or align content "to the national curriculum" — and each one
quietly assumes a lawful, authoritative, machine-readable source of curriculum truth exists.
The sixteenth pass measured that assumption across five ministries: **it holds in one of them.**

In Norway it holds *completely*, and with a written commercial grant.

### Components (every licence payload-verified 2026-10-06)

| Role | Component | Licence |
|---|---|---|
| **Curriculum source of truth** | [`Utdanningsdirektoratet/Grep_SPARQL`](https://github.com/Utdanningsdirektoratet/Grep_SPARQL) — Grep SPARQL endpoint, Norway's **LK20** curriculum as RDF, **in production since 2020-12-07** | 🟢 **NLOD** — *"you are allowed to … use them for commercial purposes"* |
| Curriculum interface docs | [`Utdanningsdirektoratet/KL06-LK20-public`](https://github.com/Utdanningsdirektoratet/KL06-LK20-public) (wiki is the live reference) | 🔴 **ungranted** — read it, do not vendor it |
| Institution roster | [`NKAmapper/school2osm`](https://github.com/NKAmapper/school2osm) — every school in Norway's National School Register | 🟢 **CC0-1.0** |
| UI components | [`Utdanningsdirektoratet/designsystem`](https://github.com/Utdanningsdirektoratet/designsystem) | 🟢 **MIT** |
| Orchestration | LangGraph | 🟢 MIT |
| Local/sovereign inference | Ollama / vLLM | 🟢 MIT / Apache-2.0 |
| Vector + cache | Qdrant | 🟢 Apache-2.0 |
| Delivery surface | Moodle plugin (GPL-3.0, in-tree) **or** an MCP side-car (MIT, external) | see `P1` |
| Oversight gate | `P11` gated-generation gate | — |

### Wiring

1. **Pin the curriculum, do not live-query it.** Pull the LK20 competence aims, subjects,
   programme structures and cross-curricular topics from the Grep SPARQL endpoint **once per
   release**, and store the result with the query, the retrieval date and a content hash.
   🔵 **NLOD permits copying and reshaping, so a pinned local copy is licensed — and a pinned
   copy is the only way a tutor's alignment claim is reproducible three months later.**
2. **Materialise competence aims as addressable entities**, each carrying its official Grep
   identifier. The identifier is the whole point: it is what makes "aligned to LK20 aim
   *X*" checkable by someone who does not trust you.
3. **Index into Qdrant** keyed by competence-aim identifier, not by free text. Alignment is a
   join on an identifier, never an embedding similarity score.
4. **Generation runs through `P11`'s gate**: the model proposes items, each item must cite at
   least one competence-aim identifier that exists in the pinned snapshot, and **an item citing
   an unknown identifier is rejected mechanically, not reviewed.**
5. **Attribution is a build artefact.** Emit the NLOD string — *"Contains data under NLOD, made
   available on data.udir.no"* — into the UI footer and into the export metadata. ⚠️ **No Udir
   logo anywhere**, including slides.
6. **Teacher review before publication** (`P11`), with the citation visible in the review UI so
   the reviewer checks the *aim*, not the prose.

### Deliverables

* A pinned, hashed, dated curriculum snapshot plus the SPARQL queries that produced it.
* An item bank in which **every item cites a real competence-aim identifier**.
* A rejection log: items the identifier gate refused, which is the evidence the gate runs.
* An NLOD attribution and logo-restriction compliance note.
* ⚠️ **A data-liability note**: NLOD disclaims accuracy, so the alignment claim is *yours*.
  Budget a sampling validation and say who signs it.

### ⚠️ Three warnings that are the point of this pattern

1. 🔴 **Do not port this pattern by analogy.** It works because a *specific* state publishes a
   *specific* endpoint under a *specific* licence. France: **no ministry estate** (the one
   curriculum RAG index found is ungranted). Japan: **documents only** — which is exactly why
   `compose/code/jp-cos-curriculum-gate` had to be built. The Gulf: nothing findable.
   🔵 **So in most countries the substitution is: ingest curriculum documents, build the
   alignment index yourself, and evidence it** — billable work in Japan, a free lookup in
   Norway. **The same proposal cannot be priced the same way in both.**
2. ⚠️ **NLOD grants the data, not a system.** `Grep_SPARQL` is endpoint documentation. There is
   no platform here; the client, cache, mapper and generator are yours.
3. ⚠️ **`KL06-LK20-public` and `pifu` are ungranted.** Use them as specifications to read, never
   as code to ship. 🟢 **And ask**: a ministry adding a `LICENSE` file is a one-commit change,
   and it is the highest-leverage upstream request in this KB.

---

## P26 — Early-childhood administration with an assistive-only AI layer (EMEA, municipal)

**A platform tier this file had no pattern for, and a buyer it had no shape for.** Every other
platform pattern here targets K-12, higher education or enterprise L&D. Early-childhood
education (ECEC) is bought by **municipalities**, runs on placement queues and income-based fee
decisions, and is subject to statutory child-ratio compliance.

🟢 **And it has a production open-source platform, adapted by a second city** — which is the
hardest test a public-sector codebase can pass.

### Components

| Role | Component | Licence |
|---|---|---|
| **ECEC platform** | [`espoon-voltti/evaka`](https://github.com/espoon-voltti/evaka) — in production for the **City of Espoo** (Kotlin) | **LGPL-2.1-or-later** — ⚠️ grant is in **`LICENSES/`**, not `LICENSE` (REUSE spec v3.0) |
| **Adaptation precedent** | [`Tampere/trevaka`](https://github.com/Tampere/trevaka) — the same platform for the **City of Tampere**, active 2026-10-06 | **LGPL-2.1** (full 27,030-byte text) |
| Forecasting / analytics | your own module, **linked** against eVaka | 🟢 your licence — see wiring step 1 |
| Orchestration | LangGraph | 🟢 MIT |
| Oversight gate | `P11` | — |
| Compliance profile | `P13` (EU AI Act education profile) | — |

### Wiring

1. **Link, do not fork the core — this is the licence doing architecture.** LGPL-2.1-or-later
   means modifications *to eVaka's own files* must be published, while **your separate modules
   linking against it may stay proprietary**. 🔵 Same middle path this page already argues for
   LGPL-3.0 platforms: **put client-specific value in new modules, contribute core fixes back.**
   ⚠️ **eVaka is REUSE-compliant, so check per-file SPDX headers before assuming every file is
   LGPL** — the repository's default is LGPL-2.1-or-later, not a guarantee about each file.
2. **Read `trevaka` before you quote a timeline.** It is the only existing evidence of what
   adapting eVaka to a second municipality actually costs, and it is a real, current repository
   rather than a vendor estimate.
3. **Build the AI layer on capacity, not on eligibility.** Demand forecasting for placement
   capacity, staffing projections against statutory child ratios, anomaly review on attendance
   records, and caseworker drafting assistance.
4. **Every output is a draft with a named human decision-maker** (`P11`). The gate here is not
   a formality: it is the compliance position.
5. **Run `P13`'s profile** and document the determination.

### Deliverables

* A linked analytics/forecasting module with its own licence boundary documented file-by-file.
* A forecasting model with its training window, inputs and error characteristics stated.
* An oversight-gate record: every AI-touched decision, its human decision-maker, timestamp.
* A `P13` AI Act determination for each AI-touched function.
* ⚠️ A REUSE/SPDX licence inventory of the files you touched — produced by reading
  `LICENSES/` and per-file headers, **not** by reading `LICENSE`.

### ⚠️ Warnings

1. 🔴 **Do not automate placement or fee determination.** These are decisions about access to a
   public service for **small children** — a protected group under the most scrutiny of any
   population in this KB. Automating them is the one thing that converts a municipal reference
   client into a regulatory incident. **Assistive only, human decides, and say so in the
   proposal before the client asks.**
2. ⚠️ **The grant is not where your tooling looks.** eVaka's 1,001-byte `LICENSE` states
   verbatim that it contains *"never the original license texts"*. A probe reads NO-GRANT or
   guesses from prose; the real text is `LICENSES/LGPL-2.1-or-later.txt`. 🔵 **Validate any
   licence instrument against `compose/code/p432-fromscratch-fixture-gate/` first — `evaka` is
   fixture 4 there precisely because the correct answer is "I don't know from this file."**
3. ⚠️ **Child data is the most sensitive category this KB touches.** GDPR, national ECEC law and
   municipal data-protection officers all apply before the AI Act does. Scope the DPO
   conversation into week one.

---

## P27 — Curriculum-aligned tutoring on a national service estate, without forking it (EMEA, Finland shape)

**The pattern this page has needed since the EU AI Act's high-risk duties came into force in
August 2026, and the pass that found the substrate also found the reason not to fork it.**
`P25` works against Norway's Grep because **NLOD grants commercial reuse of the data outright**.
Finland's estate is bigger — **188 live repositories covering curriculum, learner identity, study
records, attainment, admissions and a national OER library** — and is **EUPL**, whose copyleft
reaches network delivery. 🟢 **So this pattern's thesis is a boundary: everything you fork is
MIT/Apache; everything EUPL you only ever call.**

### Components (every licence payload-verified 2026-10-06)

| Role | Component | Licence | Fork or call? |
|---|---|---|---|
| **Curriculum objectives** | [`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet) — national core curriculum + qualification requirements (`master`) | 🟡 **EUPL-1.1** (631 B) | 🔴 **CALL ONLY** |
| **OER content pool** | [`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) — the national OER library, `aoe.fi` (`main`) | 🟡 **EUPL-1.2** (303 B, in subdirectories) | 🔴 **CALL ONLY** |
| **Prior attainment** | [`Opetushallitus/koski`](https://github.com/Opetushallitus/koski) — national study records (`master`) | 🟡 **EUPL-1.1** (653 B) | 🔴 **CALL ONLY** |
| **Identity / provider model** | [`Opetushallitus/oppijanumerorekisteri`](https://github.com/Opetushallitus/oppijanumerorekisteri) + [`organisaatio`](https://github.com/Opetushallitus/organisaatio) | 🟡 **EUPL-1.1** (631 B each) | 🟡 **READ THE MODEL**, write your own code — reading carries no obligation |
| Agent runtime | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 **Apache-2.0** | 🟢 fork freely |
| Tutoring loop | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | 🟢 fork freely |
| **Auditable mastery model** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) — Bayesian Knowledge Tracing | 🟢 **MIT** | 🟢 fork freely |
| Item generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🟢 **MIT** | 🟢 fork freely |
| Source-backed pedagogy | [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) | 🟢 **Apache-2.0** | 🟢 fork freely |
| Tool allowlist | `compose/code/mcp-allowlist-gateway/` | — | — |
| Oversight gate | `P11` | — | — |
| AI Act profile | `P13` | — | — |

### Wiring

1. **Put the licence boundary in the architecture diagram, not in a footnote.** Draw one line:
   north of it, the four Finnish services, reached **only** over HTTP. South of it, your
   Apache/MIT code. 🔵 **Nothing EUPL is ever compiled, vendored, copied or containerised into the
   deliverable** — and because "communication to the public" is Distribution under EUPL Art. 1,
   *hosting* a modified copy for the client is exactly the move that triggers the copyleft.
   **Calling an API is not.**
2. **Pull the objectives from `eperusteet` and cache them as your own derived index**, keyed by
   qualification and objective id. ⚠️ The *data* served by a EUPL-licensed service is not itself
   covered by the code's licence — but **do not assume it is open**: unlike Norway's NLOD, this
   pass established the **code** licence, not a data licence. 🔴 **Establish the terms of the data
   before a commercial deliverable depends on it** — that is one document, and it is not in this
   KB yet.
3. **Retrieve learning material from AOE** over its API and keep AOE's per-resource licence tag
   with every retrieved item. AOE exists to express OER licences (`edit-license` is a first-class
   component of its UI), so the metadata you need is already in the payload — **carry it through
   to the learner-facing citation** rather than discarding it at ingest. `p345-oer-four-forms`.
4. **Build the tutoring loop on `DeepTutor` + `smolagents`**, with the agent's tool surface
   restricted by `mcp-allowlist-gateway` to exactly: curriculum lookup, OER search, prior
   attainment read, item generation. 🟢 **smolagents is the right runtime here specifically
   because its surface is small enough to audit** — which is a conformity argument, not a
   preference.
5. **Do mastery estimation in `OATutor`'s BKT, not in the LLM.** 🔴 **This is the step that makes
   the deployment defensible.** Student evaluation is a **high-risk** function under the AI Act
   from August 2026; a Bayesian knowledge-tracing model has inspectable parameters and a stated
   error characteristic, and an LLM's judgement of mastery has neither. **The LLM explains and
   converses; the BKT decides what the learner knows.**
6. **Read `koski` for prior attainment, never write to it.** Treat it as the system of record it
   is.
7. **Gate every assessment-shaped output through `P11`** with a named human decision-maker, and
   **run `P13`** to produce the AI Act determination per function.

### Deliverables

* An agent layer whose entire dependency tree is MIT/Apache — **auditable in one `pip`/`npm`
  licence report**, with the EUPL services appearing as *endpoints*, not dependencies.
* A derived curriculum index with the provenance of every objective (service, qualification,
  retrieval date).
* A BKT mastery model with parameters, training window and error characteristics stated.
* OER citations carrying each resource's own licence tag end-to-end.
* A `P13` AI Act high-risk determination for the assessment and tutoring functions, plus the
  `P11` oversight record.
* 🟢 **A one-page licence-boundary memo** naming every EUPL service called and asserting that no
  EUPL code is distributed. ⚠️ **This is the document that makes the engagement sellable to a
  public buyer's lawyer** — produce it in week one, not at handover.

### ⚠️ Warnings

1. 🔴 **Do not fork the Finnish estate into a hosted product, and do not route around the
   copyleft via EUPL Art. 5.** The compatibility list is real (GPL-2.0/3.0, AGPL-3.0, LGPL,
   MPL-2.0, EPL, CeCILL, OSL) and the EC's own discussion notes the SaaS obligation **can be
   circumvented** by combining with GPL-3.0. **It is documented, it is contested, and selling it
   as a plan puts the client's compliance on a disputed reading.** Counsel decides, not an
   architect.
2. ⚠️ **The six EUPL-1.1 notices point at `http://www.osor.eu/eupl/`, which returns 403.** The
   repositories do not contain their own terms. **Pin the EUPL text from the EC's dated version**
   in the licence memo; do not cite the repository's URL.
3. 🔴 **Six of the nine repositories' default branch is `master`, not `main`.** Any script in this
   pattern that resolves a branch must use `git ls-remote --symref`. Hardcoding `main` writes
   two thirds of the estate down as missing.
4. ⚠️ **179 of the 188 repositories are unread.** If the engagement needs a service not in the
   component table, **probe its payload before designing against it** — the estate's licence
   picture is sampled, not established.
5. 🔴 **This pattern is Finland-shaped, and the substitution is not automatic.** For Norway use
   `P25` (Grep, NLOD, commercial reuse granted). For everywhere else, **the curriculum substrate
   has to be found before this pattern applies** — and four passes of ministry channels say most
   countries do not publish one.

---

## P28 — A standards-conformant student-data bridge with a no-training attestation (EMEA Sweden shape; the attestation travels to North America)

**Two findings this pass combine into one engagement.** Sweden publishes **SS 12000** — its
national standard for information exchange between school administration systems — with an
**Apache-2.0 reference implementation** from the national agency. North America's procurement
question, meanwhile, has hardened into a contractual term: **California AB 1159 prohibits using
student data to train AI models**, and Idaho SB 1227 imposes data-privacy requirements on school
AI tools. 🟢 **A conformant bridge plus a provable no-training boundary is the same build.**

### Components (licences payload-verified 2026-10-06)

| Role | Component | Licence |
|---|---|---|
| **Standards bridge** | [`Skolverket/dnp-ss12000-reference-api`](https://github.com/Skolverket/dnp-ss12000-reference-api) — SS 12000 reference implementation, Java (`main`) | 🟢 **Apache-2.0** (11,339 B, full text) — 🟢 **liftable into a closed product** |
| LMS tool surface | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) — up to 103 Canvas tools, WCAG scanner, bulk grading | 🟢 **MIT** |
| Moodle surface (out-of-tree) | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🟢 **MIT** |
| Tool allowlist + egress control | `compose/code/mcp-allowlist-gateway/` | — |
| Oversight gate | `P11` | — |
| AI Act profile | `P13` | — |

### Wiring

1. **Lift the SS 12000 reference API as the canonical data shape** for roster, group, enrolment,
   person and activity. 🟢 Apache-2.0 means it can ship inside a closed, hosted product with
   attribution and notices — **no copyleft, no delivery-model constraint.** This is the one
   national-agency asset in this KB you can simply take.
2. **Map every LMS surface onto that shape, not onto each other.** Canvas via `canvas-mcp`,
   Moodle via `moodle-mcp-server` (⚠️ **MIT precisely because it sits outside the GPL Moodle
   tree** — keep it there; an in-tree plugin inherits GPL-3.0).
3. **Terminate all student-data egress at `mcp-allowlist-gateway`.** One process, one allowlist,
   one log. 🔵 **The attestation in step 5 is only as good as the number of places data can
   leave** — make that number one.
4. **Make the no-training boundary a configuration, not a promise:** no student-identifying field
   crosses the gateway to a model provider; retrieval sends objective ids and de-identified
   features; retention windows are declared per field and enforced at the gateway.
5. **Produce the attestation as a build artefact**, generated from the gateway's own allowlist and
   schema — so it cannot drift from the running system. ⚠️ **A hand-written attestation that the
   code can contradict is worse than none**: it is a representation about personal data.
6. **Run `P13`** where the bridge feeds any assessment function, and **`P11`** on every graded
   output. Note `canvas-mcp`'s bulk-grading tools are exactly the surface that turns this into a
   high-risk system — **gate them explicitly**.

### Deliverables

* An SS 12000-conformant bridge with a per-source field-mapping table.
* A gateway allowlist, as code, with the egress log it produces.
* 🟢 **A generated no-training-on-student-data attestation**, traceable to the allowlist and
  schema that enforce it — the artefact AB 1159 makes procurement-relevant and that most
  competitors answer with a sentence in a brochure.
* Per-field retention declarations enforced at the gateway.
* `P13` determinations and `P11` oversight records for graded outputs.

### ⚠️ Warnings

1. ⚠️ **SS 12000 is Swedish.** It is not an EU or Nordic standard by fiat, and **this KB has not
   established** that Finland's services can be reached through an SS 12000 shape. 🔴 **Do not
   imply a regional standard in a deck** — propose it as a data shape you have chosen and can
   defend, which is a true and sufficient claim.
2. 🔴 **The two most interesting Swedish documents are ungranted.**
   `Skolverket/dnp-usermanagement` (7★) and `dnp-provplattform` — the national digital-assessment
   platform and user-management specifications — are **NO-PAYLOAD**. Design against the
   Apache-2.0 reference API, **not** against those specs.
3. ⚠️ **"AI training is prohibited" is a per-vendor fact.** The fifteenth pass read one SIS
   vendor's Terms of Use; four remain unread and egress-blocked. **Cite the district's own
   vendor's ToU, dated, and price the verification** — do not assert a sector norm.
4. 🔴 **Do not let the attestation imply more than it covers.** It is a statement about **this
   deployment's egress**, not about the client's other systems, and the memo must say so in the
   first sentence.


## P34 — Certified-conformant assessment delivery (the first pattern in this KB built on a third party's audit)

**Added in the eighteenth pass of 2026-10-06.** Every component licence below was read from the
repository's own payload on `raw.githubusercontent.com` the same day.

**The engagement this serves:** a client — most often North American K-12 or higher ed, but the
shape travels — is procuring assessment delivery against a rubric that **scores interoperability**
(39% of US districts do, trend 28). They have a legacy item bank in QTI 1.2 or 2.x, an LMS they are
not replacing, and an AI item-generation ambition they cannot yet evidence as safe.

**Why this pattern exists and P11/P15 do not cover it:** those patterns *generate* items. This one
**delivers and scores** them, standards-conformant, with the conformance claim **certified by
1EdTech rather than asserted by us**.

### Components

| Role | Component | Licence (payload-verified 2026-10-06) |
|---|---|---|
| Item player (default) | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** (© 2022-2024 Amp-up.io, LLC) — 🟢 **1EdTech Certified, QTI 3 Basic + Advanced "Delivery"** |
| Item player (Vue front end) | [`amp-up-io/qti3-item-player-vue3`](https://github.com/amp-up-io/qti3-item-player-vue3) | **MIT** (© 2024) |
| Item player (framework-neutral) | [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player) | **MIT** (© 2026 AE Studio) |
| **Legacy migration + scoring + validation** | [`longsightgroup/qti3`](https://github.com/longsightgroup/qti3) | **MIT** (© 2026 Longsight, Inc.) — 12 npm packages, **QTI 1.2 / 2.x → 3 migrator** |
| PHP-side QTI support | [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | **MIT** (© 2026 Kennisnet) |
| LMS doorway | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) or [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | Apache-2.0 — 🔵 **re-picked pass 24**: was `1EdTech/lti-1-3-php-library`, the **2,317-day-cold copy** of the same library (byte-identical payload); this one is **14 d** |
| Item generation | P11's gated generation chain | — |
| Audit trail | [`langfuse/langfuse`](https://github.com/langfuse/langfuse) | MIT **outside `ee/`** — exclude `ee/` from any vendored copy |
| Typed agent outputs | [`pydantic/pydantic-ai`](https://github.com/pydantic/pydantic-ai) | MIT |

### Wiring

1. **Migrate the item bank first, and make it the first deliverable.** `longsightgroup/qti3`'s
   migrator converts QTI 1.2 / 2.1 / 2.2 packages into QTI 3. Run its **validator** over the output
   and treat the validation report as a client-facing artefact. This is the step that stalls
   assessment projects, and it is the step that proves the engagement is real in week one.
2. **Deliver items through the certified player**, served as a side-car behind LTI 1.3 — the P1
   shape. The LMS keeps the roster and the gradebook; the player renders and runs response
   processing. **Do not fork the LMS.**
3. **Score with the player's own response processing**, not with a model. A QTI item carries its
   declared correct responses; scoring it is **deterministic and inspectable**. Keep the model out
   of the scoring path entirely — this is what makes the deployment defensible under the EU AI
   Act's high-risk assessment obligations and under US state law's "human judgment is final" rule
   (§16).
4. **Generate new items with P11's gated chain, then validate them with `qti3` before they ever
   reach a learner.** The generator proposes QTI 3 XML; the validator is the gate; a human approves.
   **A generated item that fails validation never renders** — the standard does half your oversight
   work.
5. **Trace every generation call through Langfuse.** The audit trail is a by-product of normal
   operation, not a separate compliance project.

### Deliverables

- A migrated, **validated** QTI 3 item bank, with the validation report.
- A certified-player delivery tier behind LTI 1.3, with **the issuer and scope of the 1EdTech
  certificate cited by name** in the bid.
- A deterministic scoring path with the model demonstrably outside it.
- A generation pipeline whose output is gated by standards validation **and** human approval.

### ⚠️ Three warnings that are the point of this pattern

1. 🔴 **Verify the certificate at the issuer, not in the README.** This KB read the conformance
   claim from the vendor's own repository. By §23's rule that is a claim to check against its
   issuer — **read 1EdTech's certified-products register and record the certificate's scope and
   date** before it goes in a bid. Declared gap 6 of this pass.
2. 🔴 **Two QTI components on the shelf are copyleft, and one of them is the most mature.**
   [`Citolab/qti-components`](https://github.com/Citolab/qti-components) is **GPL-3.0** (2,456
   commits, Cito's lab) and [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) is **GPL-2.0** —
   *not* compatible with GPL-3.0-only code. If the renderer is on the critical path and Citolab's
   maturity is what you want, **read §43 and ask them**: their README advertises willingness to
   relicense. That is an invitation to negotiate, **never a grant** — settle it in writing before
   any architecture depends on it.
3. 🔴 **Do not cite [`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components).** It
   is a **stale fork** of the Citolab repository, 79 commits behind, 1★. Pin the upstream address.

## P35 — The national open-data MCP client (LATAM, and portable to every CKAN portal in the region)

**Added in the eighteenth pass of 2026-10-06.** This is the pattern that follows from §44: in LATAM
the state publishes **data**, not code, and the only clients that reach it are third-party.

**The engagement this serves:** a LATAM ministry, university system or edtech client needs an agent
that can answer questions against **national education data** — enrolment, establishment directory,
teaching staff, graduates — and there is **nothing to fork from the state**.

### Components

| Role | Component | Licence / status |
|---|---|---|
| The data | **Mineduc Chile, Centro de Estudios** — **21 datasets** via [`datos.gob.cl`](https://datos.gob.cl) and its own *Datos Abiertos* portal | 🔴 **Portal terms of use — read them; the dataset's licence is not the wrapper's licence (§42)** |
| Reference client | [`pipeworx-io/mcp-datos-cl`](https://github.com/pipeworx-io/mcp-datos-cl) | **MIT** (© 2026 **Mojibake Inc.**) — a CKAN **MCP server** for `datos.gob.cl` |
| Second reference | [`gerardbourguett/mcp-chilegob-dataset`](https://github.com/gerardbourguett/mcp-chilegob-dataset) | **MIT** (© 2025, **an individual**) |
| Agent layer | `pydantic-ai` (MIT) or `smolagents` (Apache-2.0) | typed/auditable outputs |
| Local inference | [`ollama/ollama`](https://github.com/ollama/ollama) | MIT — keeps queries in-country |
| Audit trail | `langfuse/langfuse` | MIT outside `ee/` |

### Wiring

1. **Read the portal's terms of use before writing a line.** CKAN is the software; the **dataset
   licence and the portal ToU are separate instruments** and they govern what the client may do with
   the answers. This is step one, not diligence to be done later.
2. **Treat the two existing MCP servers as reference implementations, not dependencies.** Read them,
   credit them, and write a maintained one. Both are MIT so this is permitted; the point is that
   **neither is a supply chain you should put a client on** — see the warnings.
3. **Target CKAN, not Chile.** `datos.gob.cl` is a CKAN instance, and so are most LATAM national
   open-data portals. A client written against **CKAN's API** with the portal as configuration is
   portable across the region at near-zero marginal cost; one written against Chile is not.
4. **Put the agent behind typed outputs and local inference.** Education statistics answered by an
   agent are a reporting artefact; schema-checked outputs beat free text, and `ollama` keeps the
   queries in-country where the procurement asks for it.
5. **Cache and version the data pulls.** National statistical datasets are **revised**. An answer
   that cannot name which release it came from is not usable in a ministry report.

### Deliverables

- A maintained, permissively licensed **CKAN MCP client**, portal-configurable, with the Chilean
  education datasets as the first configuration.
- A terms-of-use memo distinguishing **dataset licence** from **portal ToU** from **wrapper
  licence**.
- A versioned data-pull layer with release identifiers in every answer.

### ⚠️ Four warnings that are the point of this pattern

1. 🔴 **The incumbent is one company and one individual.** `mcp-datos-cl` is held by **Mojibake
   Inc.** and `mcp-chilegob-dataset` by a single named person. Putting a ministry client on either
   is a **supply-chain risk**, and saying so is the honest version of this opportunity — not a
   reason to disparage either repository, both of which are MIT and useful.
2. 🔴 **The data's licence is not the wrapper's licence.** §42, confirmed in a second region this
   pass. An MIT MCP server over a dataset with restrictive terms **grants you nothing about the
   data**. Both instruments must be read.
3. 🔴 **The portal itself was never reached from here.** `datos.gob.cl` is **EGRESS_BLOCKED**
   in this environment, so the **21 datasets** figure and the dataset inventory are **Tier 2** — search
   results, not a first-hand read. The two MCP repositories were verified first-hand. **Confirm the
   portal's contents and its terms of use from a host that can reach it before step 1 is billable.**
4. ⚠️ **This pattern is specified from Chile and Mexico only.** Colombia, Brazil, Peru and Argentina
   were **not** probed this pass. The CKAN-first design is what makes the untested regions cheap to
   add — it is not evidence that they are the same.

## P36 — The accessible-courseware remediation line (North America Title II shape; ports to EMEA under the EAA and to APAC unchanged)

**Added in the nineteenth pass of 2026-10-06.** The first pattern in this KB whose trigger is an
**accessibility** obligation rather than an AI one, and the first whose entire toolchain is
permissive while its *outcome* depends on priced human labour. Read `repos/foundations.md` (engine
tier) and `agents/top.md` (agent tier) before scoping it.

**The buyer and the trigger.** A public school district, community college or public university in
the United States, covered by the **DOJ rule under ADA Title II** (published 2024-04-24, technical
standard **WCAG 2.1 Level AA**). ⚠️ **The date is the thing most proposals will get wrong:** the DOJ
**Interim Final Rule of 2026-04-20** extended compliance to **2027-04-26** for entities serving
≥50,000 people and **2028-04-26** for smaller entities and special districts — DOJ's own reason
being that it had *"overestimated the capabilities (whether staffing or technology) of covered
entities to comply."* 🔵 **Sell the capacity, not the date.** The backlog did not shrink; the buyer
was simply told it has another year, and the extension is documentary evidence that the buyer
cannot staff this alone.

### Components (every licence read from the repository's own payload, 2026-10-06)

| Role | Component | Licence | Why this one |
|---|---|---|---|
| Deterministic web scan, in CI | [IBMa/equal-access](https://github.com/IBMa/equal-access) | **Apache-2.0** | 9 packages: Node CLI, Cypress, Karma, Vitest and **Java** bindings — it runs inside the client's existing pipeline, including a JVM LMS |
| Second opinion / gate | [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | **Apache-2.0** | Local-only execution, so it is quotable under a data-residency clause |
| The criterion ledger | [tomaszboloz/WCAG-Accessibility-Skills](https://github.com/tomaszboloz/WCAG-Accessibility-Skills) | **MIT** | **All 86 active WCAG 2.2 criteria**, each classed automated / semi-automated / **manual**, with a per-criterion manual queue and **zero production dependencies**. This is the component that makes the deliverable an audit rather than a scan |
| Guided human assessment | [microsoft/accessibility-insights-web](https://github.com/microsoft/accessibility-insights-web) | **MIT** | Walks a human through what no engine can decide |
| Agent orchestration | [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) | **MIT** (engine: axe-core, **MPL-2.0**) | v7.0.3, 11 agents, **39 MCP tools**, WCAG 2.2 AA, and it reaches **Office documents, PDF and ePub** — where courseware lives |
| Agent scan tool, no account | [ronantakizawa/a11ymcp](https://github.com/ronantakizawa/a11ymcp) | **MIT** (engine: axe-core, **MPL-2.0**) | 6 tools, `npx`, no API key — the fallback when the client forbids a vendor account |
| OCR for scanned material | [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** | 100+ languages, and **hOCR / ALTO / PAGE** output that a tagging step can consume |
| Searchable-PDF pass | [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | ⚠️ **MPL-2.0** | Text layer + PDF/A. 🔴 **Searchable ≠ accessible** — see warning 2 |
| PDF/UA validation | [veraPDF](https://github.com/veraPDF/veraPDF-library) | 🔴 **Dual GPL/MPL** (`LICENSE.GPL` / `LICENSE.MPL`) | **Invoke as a CLI only** |
| Captions and audio description | [`whisper.cpp`](https://github.com/ggml-org/whisper.cpp) + [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) 🔵 *(re-picked pass 24; was `rhasspy/piper`, archived, head commit 407 d)* | **MIT** + **MIT** | Already on this KB's shelf. Title II's final rule covers **captioning and audio description**; both run on-premise, which is what an education-records clause requires |
| Screen-reader verification | [nvaccess/nvda](https://github.com/nvaccess/nvda) | GPL-2.0+ — **as a test client** | Free and scriptable; "verified with NVDA" costs nothing and is the line a scanner report cannot produce |

### Wiring

1. **Inventory before anything else.** Crawl the estate and classify by *artefact type*, not by
   page: LMS pages, PDFs, ePubs, Office documents, video. ⚠️ **The four have different standards,
   different tools and different unit costs; a single "pages remediated" number is how this
   engagement loses money.**
2. **Gate the web tier in CI.** `equal-access` Node CLI (or its Cypress/Vitest binding) on every
   build, Lighthouse as a second opinion. Fail the build on new violations only — a legacy estate
   will never pass from a standing start, and a permanently red gate gets switched off.
3. **Open the criterion ledger.** Initialise `WCAG-Accessibility-Skills` over the estate. It
   partitions the 86 WCAG 2.2 criteria into automated, semi-automated and manual. 🟢 **The manual
   partition is the quote**: it is the labour nobody can automate away, enumerated per criterion
   before the contract is signed rather than discovered in month three.
4. **Run the agent layer over documents, not pages.** `accessibility-agents` via MCP across the
   Office/PDF/ePub corpus. Its 39 tools produce findings with locations; the agent **triages and
   drafts fixes**, it does not certify.
5. **Scanned material:** Tesseract → structured output (hOCR/ALTO) → OCRmyPDF for a searchable
   PDF/A → **human tagging** → veraPDF CLI to validate PDF/UA. 🔴 **Step four is a person.** There is
   no permissive engine that produces tagged, structurally accessible PDF (searched this pass).
6. **Media:** `whisper.cpp` for captions, human correction pass, `sherpa-onnx` for audio description
   tracks. On-premise throughout.
7. **Verify, then claim.** `accessibility-insights-web` for the guided human assessment, NVDA for a
   real screen-reader run, then a conformance report that states **pass / fail / undetermined per
   criterion** — WCAG-EM's own vocabulary.

### Deliverables

- An estate inventory partitioned by artefact type, with a unit cost per type.
- A CI gate the client owns, on Apache-2.0 components, running in their pipeline.
- **A per-criterion ledger** with the automated / semi-automated / manual split made explicit, and
  the manual queue sized in hours.
- Remediated web tier, remediated document tier, captioned and described media.
- A conformance report in pass / fail / **undetermined** form, naming engine versions and dates.
- An SBOM listing **axe-core (MPL-2.0)**, **OCRmyPDF (MPL-2.0)** and every Apache-2.0/MIT component.
- A regression baseline so the next content upload does not undo the work.

### ⚠️ Five warnings that are the point of this pattern

1. **Never claim "compliant" from a tool.** Automated testing finds a fraction of barriers. Every
   component here says so in its own README — `WCAG-Accessibility-Skills` encodes it as data, and
   even the MIT-over-SaaS adapter this KB rejected ships a coverage disclaimer in every response.
   🔴 **A conformance claim is a human's signature over an engine's evidence.** Say "WCAG 2.1 AA
   conformance claim, supported by X and verified by Y", never "we ran a scanner and it is green".
2. **A searchable PDF is not an accessible PDF.** OCRmyPDF gives you text and PDF/A; **PDF/UA needs
   tags, reading order and structure**, and nothing permissive produces them. ⚠️ **If a proposal
   implies the document estate is automatable, it has mispriced the largest line item in the job.**
3. **MPL-2.0 is fine until someone edits a rule file.** axe-core and OCRmyPDF are **file-level**
   copyleft: unmodified use does not reach the studio's code. **Patching an axe-core rule puts that
   file under MPL-2.0 with source disclosure.** Tune through configuration, and put both in the SBOM.
4. **Do not fork the assistive application.** Cboard is GPL-3.0, AsTeRICS Grid is AGPL-3.0, NVDA is
   GPL-2.0+. Integrate at the **file-format** boundary — generate board sets as data, test against
   NVDA — and no obligation reaches the deliverable (`verticals/solutions.md`).
5. **Do not demo sign-language translation on `sign/translate`.** Its licence is **non-OSI and
   entity-tiered**: free for educational institutions, **separate commercial licence required for
   for-profit organisations**. The client may run it; **the studio may not deliver it.**

### 🔵 Porting the pattern

| Region | What changes | What does not |
|---|---|---|
| **North America** | 🟢 **Nothing — this is the base case the pattern is written from.** The trigger is the DOJ rule under **ADA Title II**, whose deadlines the **2026-04-20 interim final rule** extended by a year to **2027-04-26** (public entities serving ≥50,000) and **2028-04-26** (below that, and special districts); the standard remains **WCAG 2.1 Level AA**, unchanged. 🔵 **Row added in the twentieth pass** because a porting table that omits its own origin reads, from outside, like a region that was never measured | Everything below |
| **EMEA** | The trigger becomes the **European Accessibility Act** (in force **2025-06-28**) and the standard becomes **EN 301 549**. ⚠️ **As of 2026-07-20 no EN 301 549 version had been cited in the Official Journal under the EAA** (v4.1.0 of Nov 2025 still in Public Enquiry and Vote to Aug 2026), **so there is no presumption of conformity to lean on** — which makes the per-criterion evidence ledger *more* valuable, not less. 🔴 **No permissive tool maps findings to EN 301 549 clauses**; the mapping is a studio artefact, and it is reusable IP | The toolchain. EN 301 549 is substantially WCAG 2.1 AA for web content |
| **APAC** | The trigger is a standing mandate, not a deadline: **India** RPwD Act 2016 + **GIGW 3.0** (WCAG 2.1 AA, government portals including education); **Japan** **JIS X 8341-3:2016** ≈ WCAG 2.0 AA, mandatory for government; **Australia** AHRC guidance (April 2025) affirming **WCAG 2.2 AA** under the 1992 DDA, plus the DTA Digital Experience Policy. ⚠️ **Three countries, three WCAG versions — the ledger must be configurable by target version** | Everything else |
| **LATAM** | 🔴 **There is no accessibility deadline to sell against.** The demand driver is a programme — UNICEF's **Accessible Digital Textbooks** — and the economics are the pitch: a conventional accessible textbook takes **6–9 months and up to USD 50,000 per title**, Paraguay has embedded ADTs in national inclusive-education policy, **Uruguay produced the world's first AI-led ADT prototype in 2025**, and Brazil's **PNLD** reaches **40M+ students**. 🟢 **Here the deliverable is the production line itself**, benchmarked against that 6–9-month baseline | The document pipeline (steps 5–6), which *is* the ADT production problem |

---

## P-TRANSITION-EVIDENCE — The transition-evidence mandate (bank the extension instead of spending it)

> ⚠️ **This pattern deliberately carries a name instead of a number.** `compose/patterns.md`
> already defines **P28 three times** (lines 1790, 2205, 2777), and this file's own audit
> (`compose/code/pattern-citation-audit/`) reports **36 patterns defined** against citations
> running into the **P60s** inherited from the pre-reset era. Taking another number would add a
> fourth P28 or a second dangling P37. 🟢 **Cite this pattern as `P-TRANSITION-EVIDENCE`** — the
> prescription of trend 47 ("A knowledge base that corrects itself needs unambiguous pointers"),
> applied to itself rather than only recommended.

**Twentieth pass of 2026-10-06.** Follows from trend **46** ("The date that governs a client's
system is in the transition article…"). Every transition regime this KB found discharges on an
**artefact**, not on a date — and in the EU the extension survives only while *"the design remains
unchanged"*. P28 is the engagement that produces the artefact **without** triggering the change.

🔵 **It is the first pattern in this KB whose selling point is what it does not touch.** Every other
pattern here adds a capability to a client's estate. P28 wraps a frozen high-risk core in evidence,
so the client keeps an extension worth up to **2030-08-02** (EU public authority) or **2027-09-01**
(Vietnam, education) instead of forfeiting it on the day a tutor ships.

**Sell it when:** the client operates an AI system that is **already in service** and falls in a
high-risk category — admissions or placement scoring, automated assessment or grading, proctoring or
behaviour monitoring — and asks what the AI Act, Vietnam's Decision 33 or Peru's reglamento means for
it. ⚠️ **Sell it *before* P1, P3, P11 or P13 on the same system**, because those modify it. P28 is
the phase that establishes the baseline the later phases will be measured against — and if the
client decides not to modify, it is the whole engagement.

### Components

All licences read from the repository's own payload on 2026-10-06; full rows in
`repos/foundations.md`.

| Role | Component | Licence (payload-verified) | Why this one |
|---|---|---|---|
| **System-identity record** | [`mlflow/mlflow`](https://github.com/mlflow/mlflow) | **Apache-2.0** (`LICENSE.txt`) | 28.3k★. **The Art. 111 instrument.** Register the deployed model and its config as a versioned, dated entry. The extension's condition is *"design unchanged"* — this is what makes that a statement with evidence behind it rather than an assurance. |
| **Corpus identity** | [`iterative/dvc`](https://github.com/iterative/dvc) | **Apache-2.0** (`LICENSE`) | 15.9k★. Hashes the training and retrieval corpus in Git. Vietnam's Decision 33 education category 1 turns on *"uncontrolled data sources"*; a hash is the only non-rhetorical answer to it. |
| **Corpus control gate** | [`great-expectations/great_expectations`](https://github.com/great-expectations/great_expectations) | **Apache-2.0** (`LICENSE`) | 11.9k★. Expectation suites over the corpus, run in CI. Turns "the sources are controlled" into a build that fails when they are not. |
| **Behaviour baseline** | [`evidentlyai/evidently`](https://github.com/evidentlyai/evidently) | **Apache-2.0** (`LICENSE`) | 8.0k★. ML **and LLM** observability. Captures how the frozen system behaves *now*, which is what any later modification gets compared against. |
| **Label-free performance watch** | [`NannyML/nannyml`](https://github.com/NannyML/nannyml) | **Apache-2.0** (`LICENSE`) | Estimates performance **without ground truth**. Education's outcome labels arrive a term or a year late; a monitoring plan that waits for them is not a monitoring plan. |
| **Privacy-shaped telemetry** | [`whylabs/whylogs`](https://github.com/whylabs/whylogs) | **Apache-2.0** (`LICENSE`) | 2.8k★. Emits **statistical profiles, not raw records** — the only shape that survives California **AB 1159** (student data may not be used to train models) and the EU data-minimisation posture. |
| **Fairness evidence over the decision** | [`fairlearn/fairlearn`](https://github.com/fairlearn/fairlearn) **or** [`Trusted-AI/AIF360`](https://github.com/Trusted-AI/AIF360) | ✅ **MIT** / **Apache-2.0** | 2.3k★ / 2.9k★. Annex III §3 is admissions, assessment, placement and test monitoring — decisions **about people**. Pick Fairlearn when the client wants MIT and a smaller surface; AIF360 when they want the metric catalogue and mitigation algorithms. |
| **Lineage as a standard** | [`OpenLineage/OpenLineage`](https://github.com/OpenLineage/OpenLineage) | **Apache-2.0** (`LICENSE`) | 2.7k★. So the evidence outlives your pipeline choice and a successor supplier can read it. |
| **Published provenance format** | [`mlcommons/croissant`](https://github.com/mlcommons/croissant) | **Apache-2.0** (`LICENSE.md`) | 907★. Dataset provenance in a format a ministry or an auditor can read without your toolchain. |
| **Accessibility queue (non-modifying)** | [`tomaszboloz/WCAG-Accessibility-Skills`](https://github.com/tomaszboloz/WCAG-Accessibility-Skills) + the engine tier from the nineteenth pass | **MIT** | Remediating the *presentation* estate is billable work that does **not** change the high-risk system's design. The nineteenth pass established there is **no cited standard under the EAA**, so the deliverable is per-criterion evidence — which is what this produces and the big engines do not. |
| 🔴 **Excluded** | [`deepchecks/deepchecks`](https://github.com/deepchecks/deepchecks) (**AGPL-3.0**) · [`sodadata/soda-core`](https://github.com/sodadata/soda-core) (**Elastic License 2.0**, non-OSI) | — | Named so a later pass does not rediscover them as options. |

### Wiring

```
  ┌───────────────────────────────────────────────────────────────┐
  │  CLIENT'S HIGH-RISK SYSTEM — FROZEN. NOT TOUCHED BY P28.      │
  │  admissions scoring · auto-grading · proctoring · placement   │
  └───────────┬───────────────────────────────┬───────────────────┘
              │ read-only telemetry           │ read-only config/model read
              ▼                               ▼
      whylogs (profiles,            MLflow registry entry
      not raw records)              = "this is the system,
              │                       as of this date"
              ▼                               │
      Evidently  ──────┐                      │
      NannyML    ──────┤                      │
      Fairlearn/AIF360 ┤                      │
                       ▼                      ▼
              ┌──────────────────────────────────────┐
              │  EVIDENCE PACK (the deliverable)     │
              │  · design-stability attestation      │
              │  · corpus manifest (DVC + Croissant) │
              │  · GX suite results                  │
              │  · behaviour + fairness baseline     │
              │  · OpenLineage event log             │
              │  · per-criterion WCAG queue          │
              └──────────────────────────────────────┘
                       │
                       ▼
        filed where the regime wants it:
        EU → the client's technical documentation
        Vietnam → the one-stop portal transition plan
        Peru → the algorithmic-transparency mechanism
```

⚠️ **The arrows are deliberately one-way.** The moment a component writes back into the high-risk
system — a retrained model, a changed threshold, a new retrieval source — the pattern has become a
modification and the extension is gone. **Enforce it in the architecture, not in the statement of
work:** read-only credentials on the model and corpus stores, and a separate repository for the
evidence pipeline.

### Deliverables

1. **The design-stability attestation** — a dated, versioned record of the system as it stands, with
   the registry entry and corpus hashes behind it. ⚠️ Written so that a *later* change is detectable
   by comparison, which is the only form that is worth anything.
2. **The corpus manifest** — DVC hashes plus a Croissant description, naming every source and
   whether it is controlled.
3. **The behaviour and fairness baseline** — Evidently reports, NannyML estimates and a **stated
   choice of fairness metric with the reasoning for it**.
4. **The filing** — Vietnam's portal notice and transition plan; the EU technical documentation
   section; Peru's algorithmic-transparency mechanism. 🔵 **Jurisdiction decides the artefact's
   form, not its content.**
5. **The accessibility remediation queue** — per-criterion, with engine, version and who judged what.
6. **The modification register** — the running list of changes the client *wants*, each annotated
   with whether it forfeits the extension. 🟢 **This is the document that sells the next phase**, and
   it is honest: it tells the client what their roadmap costs in compliance terms before they commit.

### ⚠️ Three warnings that are the point of this pattern

🔴 **One. P28 does not make the client compliant, and must never be sold as if it did.** It preserves
an extension and builds the evidence a conformity assessment will need. The assessment itself is
P13's scope. A proposal that blurs the two is the kind of over-claim a regulator reads closely.

🔴 **Two. Check whether the client is a public authority before pricing this.** The EU's
**2030-08-02** date attaches to high-risk AI **intended to be used by public authorities** — a state
university or a ministry gets it; a private tutoring company does not, and for them the governing
date is **2027-12-02** with only the design-stability route available. ⚠️ **The same engagement is
worth four years to one buyer and two months to another.**

🔴 **Three. Two deadlines in this pattern have already passed.** Vietnam's Decree 142 filing was due
**before 2026-06-30**, and Peru's education-sector obligations activated **2026-09-10**. 🟢 **For a
client in either market the first task is not a plan, it is establishing what was missed** — and
saying so in week one is the difference between a remediation engagement and a discovered failure.
⚠️ **And the dates themselves came to this KB through search summaries, not primary texts** (the
legal sources are `EGRESS_BLOCKED` from this environment) — **re-read the instrument before quoting
any of them to a client.**

### How P28 changes by region

| Region | What changes | What does not |
|---|---|---|
| **EMEA** | The prize is the **2030-08-02** public-authority date, and most education buyers qualify. The filing is technical documentation under the AI Act. ⚠️ **No harmonised standard has been cited under the EAA**, so the accessibility half cannot be discharged by naming a standard — it must be per-criterion evidence | The design-stability condition, which is the whole mechanism |
| **APAC** | **Vietnam**: the prize is **2027-09-01** (education's 18-month extension), the filing is the one-stop portal transition plan, and Decision **33/2026/QĐ-TTg** names the three education categories — uncontrolled-source self-learning content, automated assessment/grading/ranking, and **biometric** behaviour monitoring. **Korea**: fines are deferred to ~**2027-07-21**, but 🔴 **generated-content labelling has no grace at all**, so the labelling limb ships immediately | The artefact set |
| **LATAM** | **Peru** is the one market with a live, education-naming obligation — **activated 2026-09-10**, staged **1–4 years from September 2025** by sector and size, requiring algorithmic-transparency mechanisms for high-risk systems. 🔴 **Brazil has no AI statute in force** (PL 2338/2023 still in the Chamber, vote deferred past the October elections), so there the pitch is readiness, not compliance | The evidence pack, which is cheap to re-file once a statute lands |
| **North America** | ⚠️ **There is no transition article, because there is no binding federal high-risk statute.** P28 sells against the **procurement rubric** (see P24) and against **state** duties that attach at enactment — California **AB 1159** on student data, Oklahoma and Maryland on human oversight. The one real date is the DOJ ADA Title II IFR: **2027-04-26** for entities serving ≥50,000, **2028-04-26** below that | The accessibility queue, which is the North American half of this engagement |

---

## P-DEPENDENCY-CLOSURE — The dependency-closure clearance (run it before the proposal, not after the build)

> 🟢 **Cite this pattern as `P-DEPENDENCY-CLOSURE`**, not as a number. The pattern-number space in
> this file has **6 numbers carrying 2–3 competing definitions each** (`P25`–`P30`), and
> `compose/code/pattern-citation-audit/` now asserts against adding a seventh. A content key cannot
> collide and cannot dangle.

**The engagement problem.** Every recommendation in this KB rests on a licence read from the
repository's own `LICENSE` payload — rigorously, reproducibly, and **one declaration short.** A
client contract is not signed against the code a maintainer wrote; it is signed against **the build
you hand over**, which includes everything the manifest pulls in. Measured on this shelf: **4 of 13**
audited projects install something their own licence does not cover, and the single most-starred
asset in this KB — **DeepTutor, Apache-2.0, 40.8k★** — installs **AGPL-3.0-or-pay-Artifex** through
`PyMuPDF`.

**When to run it.** During discovery, before any fixed-price commitment on an open-source education
build. ⚠️ **The cost asymmetry is the entire argument: one command during discovery, versus a
source-disclosure obligation or an emergency commercial licence after a hosted tutor has shipped.**

### The recipe, concretely

| Step | Component | Licence | What it does |
|---|---|---|---|
| 1 | `compose/code/dependency-licence-closure/resolve.py` | this KB | Reads each candidate's manifest from `raw.githubusercontent.com/<slug>/<ref>/<path>` at a **pinned ref**, parses the direct runtime deps, resolves each one against `pypi.org/pypi/<name>/json` or `registry.npmjs.org/<name>`, and classifies it into five classes |
| 2 | `dep_licence.py` classifier | this KB | `NONCOMMERCIAL` → `STRONG-COPYLEFT` → `WEAK-COPYLEFT` → `PERMISSIVE` → `UNKNOWN`, **in that order** — `AGPL`, `GPL` and `LGPL` all contain the substring `GPL`, and collapsing them is the difference between one real finding and forty false ones. **48/48 offline assertions** |
| 3 | the four manifest shapes | — | `pyproject.toml` (PEP 621), `pyproject.toml#<group>` (**PEP 735** — required for Kolibri, whose `[project].dependencies` is literally `[]`), `requirements.txt`, `package.json` (runtime `dependencies` only, never `devDependencies`) |
| 4 | **the positive control** | — | ⚠️ **Do not ship a closure report without one.** At least one target must come back a **genuine zero** — here, `tomaszboloz/WCAG-Accessibility-Skills`, whose manifest confirms its own documented *"no production dependencies"*. An instrument that cannot tell "zero declared" from "I read the wrong file" is measuring nothing |
| 5 | the verdict, written for counsel | — | `BLOCKER` (non-commercial — no linkage argument rescues it) · `REVIEW-STRONG` · `REVIEW-WEAK` · `REVIEW-UNKNOWN` · `CLEAN`. ⚠️ **`REVIEW-*` means "a lawyer should read this row", never "this is a violation"** |
| 6 | the remediation choice | — | For a `REVIEW-STRONG` row: **comply** for the embedding service, **buy** the commercial grant, or **replace** the component. For DeepTutor's `PyMuPDF` the third is usually cheapest — the PDF layer is swappable, and `pypdf` (**BSD-3-Clause**, verified this pass via `license_expression`) is the drop-in candidate to evaluate |

### What the deliverable is

🟢 **A one-page table per candidate: its licence, its declared direct dependency count, its verdict,
and the specific rows that produced the verdict** — plus the three limits stated on the page itself,
because a verdict quoted past its limits becomes wrong data:

1. **Depth 1 only.** Transitive dependencies are not measured. `certifi` (MPL-2.0) is in nearly
   every Python deployment and surfaced here only where it was declared directly.
2. **Linkage is not analysed.** Whether an AGPL import makes the importer a derivative work depends
   on how the thing is used and distributed.
3. ⚠️ **"Not measured" is never reported as "clean."** Workspace roots (`mentingo`, `OpenTutor`)
   keep their runtime deps in `apps/*` and were left explicitly unmeasured.

### Why it sells in all four regions, and differently in each

| Region | The buying reason |
|---|---|
| **North America** | No sector regulator to point at, so **counsel and procurement** are the gate. The closure report is the artefact that clears a district's or university's legal review |
| **EMEA** | Lands inside obligations that already exist — the **EAA** evidence route (no harmonised standard cited) and **AI Act** Annex III duties from **2027-12-02** both reward documented provenance, and a resolved manifest is that class of evidence |
| **APAC** | **Sovereignty is the buying criterion**, and this report is a sovereignty document: it names every third-party grant entering a national deployment. Attaches directly to Vietnam's portal transition plan and Korea's high-impact filings |
| **LATAM** | The permissive stack **is** the budget strategy, so a copyleft dependency threatens the **cost case**, not just the legal one. ⚠️ **Kolibri — the platform this KB's equity pattern is built on — came back `REVIEW-WEAK` with two LGPL rows**, in the region where that matters most |

### Sizing

**2–4 days** for a shelf of 10–15 candidates, most of it reading rather than coding, since the
instrument already exists and runs offline except for the two registry endpoints. 🟢 **Best sold as a
bundled discovery artefact rather than a standalone engagement** — it is a trust signal the client
can verify in one command, and on this KB's own shelf it surfaced a real finding in **4 of 13**
projects.

## P-ONPREM-CLASSROOM — The zero-egress classroom (assignment, grading and mastery with no third-party service in the loop)

**Added in the twenty-second pass of 2026-10-06.** Every component's licence was read from its own
payload this pass or an earlier one; the three new ones came from the GitLab API channel documented
in `agents/top.md`.

**The constraint this answers, in two regions at once.** California's proposed **A.B. 1159** would
bar student data from training AI models unless the use directly benefits the school; a district's
counsel cannot verify that about a SaaS tutor and can verify it about a system with no outbound
calls. In EMEA the same architecture answers **Annex III** deployer duties and data-residency rules
without a transfer assessment. 🟢 **The deliverable is not software, it is a provable data-flow
statement** — and this stack makes it true by construction rather than by contract.

### Components

| Layer | Component | Licence (payload-verified) | Why this one |
|---|---|---|---|
| **Forge** | [`gitlab-org/gitlab-foss`](https://gitlab.com/gitlab-org/gitlab-foss) (GitLab CE), self-hosted | 🟢 **MIT Expat** — ⚠️ with directory carve-outs: `doc/` is **CC BY-SA 4.0**, `ee/` and `jh/` carry their **own** licences (payload, 2,001 B) | The institution already has Git hosting or can stand it up. ⚠️ **Deploy `gitlab-foss`, not the EE package** — the carve-out is the scope-split failure mode of trend 23, in the foundation layer |
| **Assignment workflow** | [`travo-cr/travo`](https://gitlab.com/travo-cr/travo) | 🟢 **BSD-3-Clause** | fetch/submit over the GitLab REST API, terminal **or** Jupyter widget dashboard; works against **any** instance incl. self-hosted; in production in a dozen classes at Paris-Saclay and UQAM. PyPI `travo` 2.1.1 |
| **Notebook grading** | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** | automatic + manual grading with **hidden tests**; Travo drives it directly. v0.9.6 of 2026-09-30 |
| **Non-notebook grading** | [`cjaikaeo/elabsheet`](https://gitlab.com/cjaikaeo/elabsheet) | 🟢 **BSD-2-Clause**, holders named in payload | exercise/exam authoring with automatic answer checking, incl. a compiled-language component. Dockerised in `cjaikaeo/elab-docker` |
| **Mastery / next-task** | [`adaptive-learning-engine/adlete-packages`](https://gitlab.com/adaptive-learning-engine/adlete-packages) + its `moodle/adleteh5p` sibling | 🟢 **MIT** | competence estimation and next-exercise recommendation, with an **H5P** binding already written — the integration P3 has had to hand-build |
| **LMS of record** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) *(confirmed this pass at [olatorg/OpenOLAT](https://gitlab.com/olatorg/OpenOLAT))* | 🟢 **Apache-2.0**, payload read on **two forges** | the only complete LMS in this KB with no copyleft conversation; QTI, SCORM, curriculum, assessment |
| **Standards edge** | [`kbarbounakis/eduapi`](https://gitlab.com/kbarbounakis/eduapi) *(optional)* · [`eduplex-api/cake-api-xapi-proxy`](https://gitlab.com/eduplex-api/cake-api-xapi-proxy) | ⚠️ **LGPL-3.0** · 🟢 **MIT** | 1EdTech **EduAPI** for SIS-side interop (link, do not fold) · **xAPI → LRS** pipe when the LMS cannot emit statements |
| **Inference** | Ollama or vLLM, on the institution's own hardware | 🟢 MIT · Apache-2.0 *(this KB's foundation shelf)* | the only layer that would otherwise call out. **No hosted model endpoint anywhere in this pattern** |
| **Offline tier** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) *(optional)* | 🟢 **MIT** — ⚠️ `REVIEW-WEAK`, two LGPL deps (pass 21) | where connectivity is the constraint rather than residency |

### Wiring

1. **Stand up `gitlab-foss`** inside the institution's network. One group per course; one project
   per assignment template; students' submissions are **forks inside that group**, so every artefact
   stays on the institution's disk.
2. **`pip install travo`** on the student image (JupyterHub, lab machine or BYOD). `travo fetch`
   clones the assignment; `travo submit` pushes the student's fork. The dashboard widget means the
   student never touches Git directly.
3. **Grading splits by artefact type.** Notebooks → nbgrader's autograde + hidden tests, manual
   tranche for the rest. Code and short-answer exercises → **elabsheet**, which authors the task and
   checks the answer. Both run as CI jobs **on the institution's own runners**.
4. **Mastery loop:** push each grading outcome into **ADLETE**; it returns the next task. If the LMS
   is Moodle, `adleteh5p` renders that task as an H5P activity in place; if it is OpenOLAT, drive it
   through QTI items.
5. **The model layer stays local.** Feedback drafting, hint generation and rubric-assisted marking
   call **Ollama/vLLM on-premises**. 🔴 **The oversight gate of `P11` applies unchanged: no
   model-generated mark is final.** This is also the only way the Oregon-style design duties and the
   A.B. 1159-style training-data rule are satisfiable at the same time.
6. **Standards edge last**, and only if procurement scored it: EduAPI for SIS interop, the xAPI proxy
   for statement export to an LRS the institution already runs.

### Deliverables

* A **data-flow statement** naming every egress point — ideally the empty set — reproducible by the
  client in one command (`ss -tunp` on the runner during a grading job).
* A course **pilot**: one real assignment, fetched, submitted, autograded and mastery-routed
  end-to-end.
* A **fork-ownership plan** for elabsheet and ADLETE (see the warnings) with a named maintainer and a
  budgeted hour-count.
* The **licence file set** for the deliverable: BSD-2, BSD-3, MIT, MIT Expat, Apache-2.0 — and, if
  EduAPI is in, the LGPL-3.0 linking note written out.

### ⚠️ Four warnings, which are the point of this pattern

1. 🔴 **Two components are small, and the stack's risk is concentrated there.** elabsheet is **14★**
   with a 2013 copyright line and two named holders; ADLETE is **1★**. Both were committed within the
   last month, both are permissive enough to fork outright, and **the engagement must price owning
   the fork** rather than assume upstream. This is a *deliberate* trade against a SaaS grader: the
   licence and the egress property are worth the maintenance.
2. ⚠️ **`gitlab-foss` is MIT Expat *outside* three directories.** `doc/` is CC BY-SA 4.0 and `ee/`
   carries its own terms. If the client's platform team installs the EE package "because it is the
   same product", the licence premise of this whole pattern changes. Check which package is running
   before writing the licence section of any proposal.
3. ⚠️ **Travo's trust model is GitLab tokens.** Each student authenticates to the forge; the
   workflow's security is the instance's access control, not the tool's. On a self-hosted instance
   that is an advantage — it is the institution's own IAM — but it must be configured, not assumed.
4. 🔵 **Nothing here is an agent, and that is on purpose.** The agentic layer in this pattern is a
   local model doing feedback and hint drafting behind a human gate. **A pattern whose selling point
   is "no data leaves" cannot have an autonomous component calling out**, and every hosted-tutor
   component in this KB does.

### Where it sells, and where it does not

| Region | Fit |
|---|---|
| **North America** | 🟢 **Strongest.** A.B. 1159-shaped data rules, Ohio's district-policy mandate (deadline **2026-07-01**, passed) and Maryland's AI coordinators give it a named buyer with a written obligation. Travo is already a Québec production tool |
| **EMEA** | 🟢 **Strong.** Answers Annex III deployer duties and residency without a transfer assessment; **11 of the 18 rows this pass added are EMEA-origin** (5 verified from a README, 6 inferred), so the local reference base exists |
| **APAC** | 🟢 **Strong where sovereignty is the criterion.** BSD-2 on the grading core means a ministry can fork and localise without publishing — the shortest grant in this KB |
| **LATAM** | ⚠️ **Fits the budget case, with an added step.** The cost argument is the point here, but 🔴 the regional supply this pass measured is **ungranted, not absent** (0 licensed education projects of 674), so a LATAM delivery imports this stack rather than building on local assets. Pair it with the **licence-grant clinic** in `intel/market.md` |

---

## Component currency update, twenty-third pass of 2026-10-07

⏱️ **Measurement window 2026-10-06 ~21:00 UTC → 2026-10-07 00:00 UTC; ages computed against the
reference date 2026-10-06.** Every GitHub repository cited anywhere in this KB was dated via
`git ls-remote` and `git fetch --depth 1 --filter=blob:none`.

🟢 **Read this first, because it is the reassuring half.** Of the **181** repositories wired into
the patterns in this file, **54.7% were touched in the last 30 days and only 18.8% are more than a
year old** — against **33.0%** for `repos/foundations.md`. **These patterns were already composing
from the live subset of the shelf, without ever reading a date.** What follows is a short list of
exceptions, not a rebuild.

### 🔴 P1 — the default engagement shape: both LTI picks are cold, and both have live replacements

| Currently named | Head commit | Age | 🟢 Replace with | Licence (payload) | Head commit |
|---|---|---|---|---|---|
| `1EdTech/lti-1-3-php-library` | 2020-06-03 | 🔴 2,316 d | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **Apache-2.0** (11,343 B) | **2026-09-23** (13 d) |
| `dmitry-viskov/pylti1.3` | 2022-11-21 | 🔴 1,415 d | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | **BSD-3-Clause** (1,527 B) | **2026-07-01** (97 d) |

🟢 **The PHP swap is free.** The two repositories' `LICENSE` payloads are **byte-identical**
(`sha256 78b49eea…`, 11,343 B) and the composer packages are the same library under two names
(`packbackbooks/lti-1p3-tool` vs `imsglobal/lti-1p3-tool`). **This is an upstream swap, not a
migration** — the consortium's republished copy went cold, the author's original did not.

🟢 **The Python swap is a real choice and it closes this KB's most-repeated gap.**
`ltiauthenticator` implements **LTI 1.3 and LTI 1.1** and its README names **Open edX, Canvas and
Moodle** as tested platforms — the three this KB documents. If the tool must be Django rather than
JupyterHub-hosted, use [`Harvard-University-iCommons/django-lti`](https://github.com/Harvard-University-iCommons/django-lti)
(**MIT**, 2025-08-27, ⚠️ copyright vests in the **University of Michigan** despite the Harvard
organisation — note it in the provenance pack).

⚠️ **Do not reach for `ucfopen/cookiecutter-python-lti` without reading its requirements file.** The
template is MIT and 147 days old; its **Flask** path pins
`git+https://github.com/ucfopen/pylti1.3.git@master` — a **fork, 1,363 days cold, at a moving
branch**. Its **Django** path pins `django-lti==0.7.1` and is fine.

### 🔴 P18 — offline voice tutoring: Piper is 406 days cold and the replacement is already in this KB

| Currently named | Head commit | Age | 🟢 Replace with | Licence | Head commit |
|---|---|---|---|---|---|
| `rhasspy/piper` (TTS) | 2025-08-26 | 🔴 406 d | [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (11,357 B) | **2026-10-06** (0 d) |

🟢 **`sherpa-onnx` is already the ASR component of this pattern**, and it does **TTS as well**, so
the swap *removes* a dependency rather than exchanging one. Piper stays usable — MIT, and a frozen
TTS model is a far smaller risk than a frozen protocol library — but new builds should not add it.

### ⚠️ P2 / P24 — the certified QTI player is 472 days old, and that is a disclosure, not a swap

[`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) (MIT, 2025-06-21) is
the **only 1EdTech-Certified permissive asset in this KB**. 🟢 **Keep it.** Certification does not
lapse when maintenance pauses, and the certificate is the strongest procurement artefact on this
shelf. 🔴 **But the date goes in the deck**, because "certified" and "maintained" are now different
facts about the same repository. The live alternative,
[`Citolab/qti-components`](https://github.com/Citolab/qti-components) (0 d), is **LGPL-3.0** — a
different licence conversation, not a drop-in.

### ⚠️ P12 and P16 — two further cold components, flagged without a replacement

| Pattern | Component | Head commit | Age | Status |
|---|---|---|---|---|
| **P12** (pedagogy-aware evaluation) | `ai-edu-lab/E-Eval` | 2024-02-19 | 🔴 960 d | 🔴 **no live permissive replacement found.** `AI-for-Education/pedagogy-benchmark` is 356 d and also ageing |
| **P16** (all-MIT national/state stack) | `project-sunbird/sunbird-lms-mw` | 2020-05-05 | 🔴 2,345 d | ⚠️ the `project-sunbird/*` namespace is **75% cold**; current work is in `sunbird-ed/*`. **Confirm which namespace the client's distribution tracks before week one** |
| **P24** | `theopenem/OneRoster.NET` | 2023-10-13 | 🔴 1,089 d | 🔴 **no live permissive OneRoster implementation exists** — both known ones are 1,089 d. Price the maintenance |

### 🟢 Added to the P22 gate — a fourth point, and it runs over the closure

P22 (the licence-reliability gate) has three points: payload, manifest, detector. **Add a fourth:**

> **P22.4 — currency.** For every component entering a deliverable, record the head-commit date
> (`git ls-remote` + `git fetch --depth 1 --filter=blob:none`; no API needed, and it works where
> `api.github.com/repos/*` returns 403). **Run it over the dependency closure, not the dependency
> list** — a 147-day-old MIT template installing a 1,363-day-old fork at a moving branch is the
> shape this catches, and neither the template's licence nor its own date reveals it.

**Output:** three verdicts. 🟢 **current** (<180 d) — no action. ⚠️ **ageing** (180 d–2 y) —
disclose in the deck with the date. 🔴 **cold** (>2 y) — either name a live replacement or price
the maintenance explicitly as a line item. **Never prune on date alone**: a finished conformant
implementation and an abandoned one look identical to this probe, and only reading the project tells
you which it is.

---

## P-GRANT-CLINIC — the licence-grant clinic (small, fast, and it sells in every region)

**Added in the twenty-third pass of 2026-10-07**, executing pass 22's pre-registered action C and
re-scoping it from a LATAM offer to a global one.

### The finding it monetises

Across the last two passes, **four real, active education projects were measured as carrying no
grant of any kind** — not a restrictive licence, *no licence file at all*. They cannot be adopted,
contributed to, forked, resold or deployed by anyone, **including their own institutions'
partners**, until one file is added.

| Project | Origin | Last activity | What it is |
|---|---|---|---|
| [`angeelrdz-group/nova-aula`](https://gitlab.com/angeelrdz-group/nova-aula) | LATAM (Spanish) | 🟢 2026-10-05 | full-stack education platform: courses, quizzes, analytics |
| [`evertonwilliam/plataforma-de-educacao`](https://gitlab.com/evertonwilliam/plataforma-de-educacao) | LATAM (Portuguese) | 🟢 2026-09-08 | AI-guided software-engineering training track |
| [`ccsl-ufpa/educacaovigiada-org-br`](https://gitlab.com/ccsl-ufpa/educacaovigiada-org-br) | **Brazil — Federal University of Pará** | ⚠️ 2025-12-09 | *Educação Vigiada*, surveillance in education; five years old |
| [`cderda/cargogetgraded`](https://gitlab.com/cderda/cargogetgraded) | 🔴 **North America** (UChicago) | 2026-07-28 | **Carriage** — step-level algebra autograder, Python/SymPy, **piloting Fall 2026** |

🔴 **The fourth row is why this is not a LATAM pattern.** Ungranted-but-real is a **global condition
with a LATAM concentration** — and in LATAM it carries a measured denominator (674 projects across
English, Spanish and Portuguese; **0 with a permissive payload**) that makes the pitch sharper
there than anywhere else.

### Components

Nothing to build. This pattern is **entirely artefact and process**, which is why it fits in a week:

| Artefact | Source |
|---|---|
| licence selection note (MIT / Apache-2.0 / BSD-2 / BSD-3, with the consequence of each stated in one paragraph) | this KB's `repos/foundations.md` licence-boundary section |
| `LICENSE` payload, correct holder line, correct year | the project's own commit history and institutional owner |
| `LICENSES/` directory + **REUSE**-style per-file headers where the project has mixed provenance | the pattern pass 22 measured on `gitlab.com` |
| manifest alignment — `composer.json` / `package.json` / `pyproject.toml` `license` field matching the payload | prevents pass 22's class-3 defect (*the project contradicts itself*) |
| dependency-licence closure report | **P22** gate, points 1–3 |
| currency report | **P22.4**, added above |

### Wiring — the one-week shape

1. **Day 1 — establish there is genuinely no grant.** 🔴 **Enumerate the repository root tree via
   the forge API; do not guess filenames.** This is how Carriage was established as ungranted (21
   root entries, no licence file). Guessing `LICENSE`/`LICENSE.md`/`COPYING` across two branches
   misses `LICENSES/` directories and mis-reports REUSE projects as ungranted.
2. **Day 1 — identify the actual holder.** ⚠️ Rarely the account name. Measured counter-examples:
   `django-lti` is published by **Harvard** and vests copyright in the **University of Michigan**;
   `Verbix-Flutter` is published by `Wahid7852` and names **Swati Sharma**;
   `ucfopen/pylti1.3` names the upstream author. **For a university project the holder is usually
   the institution, and the grant needs the institution's assent, not the committer's.**
3. **Days 2–3 — licence selection workshop.** For a ministry or university the decision is nearly
   always between **MIT** (shortest, most permissive, zero obligations) and **Apache-2.0** (adds an
   explicit patent grant — the one a public institution's counsel usually wants). **BSD-2** is the
   answer when the institution wants the shortest possible text, as `cjaikaeo/elabsheet` chose.
4. **Days 3–4 — add the files and align the manifests.** Payload, holder, year, `LICENSES/`,
   manifest `license` field. Run the P22 gate against the result so the project passes its own
   check.
5. **Day 5 — the closure report.** What the project *installs* may be less permissive than what it
   *grants* (pass 21: 15 of 352 dependencies not permissive). **The grant is not finished until the
   closure is reported**, or the institution has been told, in writing, which dependency constrains
   redistribution.

### Deliverables

- A merged licence grant, or — where the holder is an institution and the repository is quiet — a
  **written grant recommendation addressed to the institution**, which is the realistic output for
  `ccsl-ufpa/educacaovigiada-org-br` (ten months idle).
- Dependency-licence closure report and currency report.
- A one-page reusable licence-selection note the institution can apply to its remaining repositories
  — **this is the part that turns one clinic into a programme.**

### ⚠️ Three warnings that are the point of this pattern

1. 🔴 **Target by activity, not by prestige.** The federal university's project has the best story
   and the worst odds: **ten months idle** means there is no maintainer to accept a merge request,
   so it must be routed through the institution's free-software centre as a policy conversation.
   `nova-aula`, committed the day before measurement, is a merge request and a chat. **Open with the
   live one; the institutional one is the follow-on.**
2. 🔴 **A `LICENSE` file is not a grant.** `Wahid7852/Verbix-Flutter` carries one — 208 bytes
   reading *"No permissions are granted for reuse, distribution, or modification."* Any clinic that
   screens on *presence* will skip the projects that most need it and "fix" nothing. **Screen on
   payload.**
3. ⚠️ **This is not free legal advice, and it should not be priced as a giveaway.** The deliverable
   is a licence decision made by the institution's own counsel with the engineering facts in front
   of them. 🟢 **The commercial logic is that the clinic creates the asset the later engagement is
   built on** — a client cannot buy a platform engagement on code nobody is allowed to modify.

### Regional fit

| Region | Fit |
|---|---|
| **LATAM** | 🟢 **Strongest, and the only region with a measured denominator**: 674 projects, three languages, **0 permissive payloads**. Three named targets, one of them a federal university. Pair with the offline-first and cost arguments of P5 and P21 |
| **North America** | 🟢 **Real and newly evidenced** — Carriage is piloting in US classrooms in Fall 2026 with no grant. Sells alongside the procurement-rubric component register of trend 26 and P24 |
| **EMEA** | 🟢 **Different buyer, same work.** Public-sector publishers here mostly *do* grant, often via **REUSE** and `LICENSES/` directories; the clinic's EMEA form is **correctness and closure** (manifest alignment, REUSE conformance, dependency closure) rather than adding a first grant |
| **APAC** | ⚠️ **Thinnest fit of the four, stated rather than padded.** The region's permissive assets measured in this KB — OpenMAIC, `elabsheet`, the Sunbird estate — already carry grants. The APAC version of this engagement is the **currency** check of P22.4, not the grant |

---

## Added in the twenty-fourth pass of 2026-10-07 — component currency, applied to the patterns rather than reported about them

⏱️ **Ages against the reference date `2026-10-07`.** Channels: the package registries
(`compose/code/registry-recency-channel/`) and `git ls-remote`.

Pass 23 pre-registered action **C**: *"re-pick the cold components in P1 and P18 and re-measure,
rather than only flagging them."* Done, and the pre-registration was wrong about both patterns.

### 🔴 P1 did not have a cold component — it had the wrong protocol

P1 is described here as *"the default engagement shape"*, for when *"the client already runs an LMS,
which is almost always"*. Its step 2 named
[`IMSGlobal/LTI-Tool-Provider-Library-PHP`](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP):

| | measured this pass |
|---|---|
| head commit | 🔴 **2016-11-28 — 3,600 days (9.9 years)**, the oldest component in any pattern here |
| licence payload | 🟢 Apache-2.0, `master/LICENSE`, 11,357 B — the grant was never the problem |
| 🔴 protocol | `master/README.md`: *"support for **LTI 1.1** and the unofficial extensions to **LTI 1.0**"* — **no LTI 1.3** |

🔴 **LTI 1.1's security model is retired. LTI 1.3 / Advantage is what Canvas, Moodle and Open edX
certify against and what every procurement rubric in `intel/market.md` scores.** An engagement
following P1 literally would have built its LMS integration on a withdrawn protocol generation and
then failed the interoperability line of the rubric that justified the project.

⚠️ **Pass 23 dated this repository correctly** — it is the last row of that pass's interoperability
table, at 3,599 d — **and no pass had opened it.** Its licence column there reads `—`, and nothing
checked its protocol version against the step that cited it. **Dating a component and qualifying it
are different acts.**

🟢 **P1 step 2 is rewritten above**, with the pick made from the client's estate: `django-lti`
(Python/Django, MIT, 2 d), `ltiauthenticator` (JupyterHub, BSD-3, 98 d), `packbackbooks` (PHP, 14 d)
or `ltijs` (Node, 1 d). Because P1's steps 4–6 are already Python, **the usual answer is `django-lti`
and the second runtime P1 assumed disappears.**

### 🔵 P18 needed nothing, and pass 23's flag was the error

Pass 23 listed `rhasspy/piper` as *"wired into P18"*. **It is not.** P18 already selected
`sherpa-onnx` and already carries the paragraph *"Why sherpa-onnx and not Piper"*, recording Piper's
archival and its GPL-3.0 successor. 🟢 The commit channel confirms it independently: `piper`'s head
commit is **2025-08-26 (407 d)** and nothing has landed since. **P18 was correct before this pass
and is unchanged.**

### 🟢 Where the cold components actually were

| Pattern | Component | Age | Re-picked to | Age | What the pattern gains |
|---|---|---|---|---|---|
| **P1** | `IMSGlobal/LTI-Tool-Provider-Library-PHP` (🔴 LTI 1.1 only) | 🔴 **3,600 d** | `academic-innovation/django-lti` | 🟢 **2 d** | the right protocol, and **one fewer runtime** |
| **P25**, **P34** | `1EdTech/lti-1-3-php-library` | 🔴 2,317 d | `packbackbooks/lti-1-3-php-library` | 🟢 **14 d** | the **same library**, live copy |
| **P25**, **P27**, **P28**, **P30** | `dmitry-viskov/pylti1.3` | 🔴 1,416 d | `academic-innovation/django-lti` | 🟢 **2 d** | no *"fork and maintain"* caveat |
| **P21** | `vosk-api` **+ an unresolved Piper fork decision** | 🔴 407 d | `k2-fsa/sherpa-onnx` | 🟢 **1 d** | **one component instead of two**, one permissive licence, decision closed |
| **P36** | `rhasspy/piper` (audio description) | 🔴 407 d | `k2-fsa/sherpa-onnx` | 🟢 **1 d** | — |

🟢 **Two of these are simplifications, not swaps.** P21 loses a component *and* a standing
architectural argument: `sherpa-onnx` does ASR **and** TTS — plus VAD, keyword spotting and
diarization — *"running the following functions locally"* on **Raspberry Pi and Android**, under one
Apache-2.0 grant. P1 loses the entire second runtime its two-process architecture existed to host.

### 🔴 The licence boundary that is now explicit in P30

[`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) is the
**best-maintained Python LTI 1.3 implementation in any language** — committed and released **6 days**
ago as `lti-consumer-xblock` v11.4.2 — and it is **AGPL-3.0** (payload 34,520 B). It is the right
component **inside** an Open edX deployment and disqualified from a reusable-IP deliverable, which is
exactly P30's thesis. It is named in P30 as a boundary so that no later pass re-discovers it as a
pick.

## P22.5 — the currency-and-provenance point, added to the licence-reliability gate

**P22** runs three points before a component enters a deliverable, and pass 23 added **P22.4**
(currency over the dependency closure). This pass adds the fifth, because P22.4 would not have caught
either defect found above:

> **P22.5 — Resolve provenance before you trust a date, and read the protocol before you trust the
> provenance.**
>
> 1. **Is the payload's copyright holder the publishing account?** If not, treat it as a **fork
>    hypothesis** (trend 56). Resolve the upstream from the package registry's declared homepage —
>    PyPI `project_urls`, npm `repository`, the composer name — which works where `api.github.com`
>    is 403.
> 2. **Do the remote's tags reach the registry's current release?** `git ls-remote` the tags. A copy
>    topping out six minor versions below the published release is a fork.
> 3. **Is the organisation name current?** An org that has been renamed (`IMSGlobal` → 1EdTech,
>    2022) dates its repositories by construction.
> 4. **Does the component implement the version the rubric scores?** Open the README. A library can
>    be permissive, popular and the wrong protocol generation — which is **three green checks and a
>    failed bid**.
> 5. **Both recency channels, not one.** Head commit **and** latest release. Cold commits with fresh
>    releases means development happens off the default branch — look harder. **Cold on both is
>    abandonment** (`pylti1.3`: 1,416 d and 1,417 d).

⚠️ **And one bound on every date this gate produces:** the registry channel reads the **latest**
release, not the **pinned** one, so an age is a **lower bound on staleness**. A manifest pinning an
old version installs something older than the gate reports, never newer.

## P-UPLIFT — the dependency-uplift engagement (small, honest, and it precedes every adoption)

**Added in the twenty-fourth pass of 2026-10-07.** Not a new capability — a line item this KB has
been recommending adoptions without, in every region.

**Use when:** a client is adopting a permissive education platform or ITS from this KB's shelf
(OATutor, Kolibri, Oppia, Coursemology, Mentingo) and the proposal treats "it is actively
maintained" as sufficient diligence.

**The premise, measured.** A repository's head-commit date and its dependency set's release dates
are **different facts** (trend 57). Across 293 depth-1 dependencies: **30.1% cold over a year,
13.0% pre-2024, median 65 days** — and the per-repository spread is **30× wide**:

| Adoption target | Head commit | Median dependency age | Cold > 1 yr | Sprint-one reality |
|---|---|---|---|---|
| `CAHLR/OATutor` | 🟢 7 d | 🔴 **604 d** | 21/35 | Material-UI **v4** (superseded 2021); `random-seed` 3,967 d |
| `learningequality/kolibri` | 🟢 1 d | ⚠️ 200 d | 14/32 | Python-2-era shims: `zeroconf-py2compat` 1,156 d |
| `oppia/oppia` | 🟢 1 d | 🟢 60 d | 40/152 | bimodal; App Engine tail (`crcmod` 5,923 d) **and** a proprietary Azure Speech SDK |
| `towardsai/ai-tutor-app` | — | 🟢 **9 d** | **0/20** | 🟢 nothing to uplift |

**Wiring.**
1. Run `compose/code/dependency-licence-closure/` over the target's manifests — the licence census.
2. Run `compose/code/registry-recency-channel/` over the result — the age census.
3. Run **P22** including **P22.5** on every component the target itself wires in.
4. Partition the result: **permissive-and-fresh** (adopt), **permissive-and-cold** (uplift, estimate
   it), **copyleft** (architecture decision), **proprietary or ungranted** (replace — and name the
   substitute; for Azure Speech it is `k2-fsa/sherpa-onnx`, Apache-2.0).
5. Deliver the four-way partition as the adoption decision record.

**Deliverables.** The two censuses, the uplift estimate by dependency, the replacement list with
named permissive substitutes, and a one-page adoption recommendation that quotes **the median and
discloses the maximum**.

**Effort:** 1–2 weeks, before the adoption decision rather than after it.

⚠️ **Two warnings that are the point of this pattern.**
🔴 **A green head commit is not a priced adoption.** OATutor is the right technical pick and its
first sprint is a dependency uplift. Saying so wins trust; discovering it in sprint three loses the
account.
🟢 **A cold dependency is not a defect by itself.** `defusedxml` at 2,039 days is a finished security
library. **The deliverable is the partition, not the age**, and the partition requires reading.

---

## P-UPLIFT addendum, twenty-fifth pass — price the uplift from the **pin**, and the number is four times bigger

**P-UPLIFT** was written against the *latest-release* ages of a component's dependencies, which is
the number `registry-recency-channel` produces. This pass resolved the **version specifiers**
(`compose/code/p437-pinned-version/`, 47 controls) and the number a client is actually quoted
changes:

| Across 327 dependency rows of the twelve target repositories | Latest release | **Pinned** |
|---|---|---|
| median age | 57 d | 🔴 **220 d** |
| cold > 1 yr | 27.2% | 🔴 **42.5%** |

🔵 **Why it is this large, and the condition for transferring it: 52% of these rows are pinned
exactly** (`==1.2.3`) and another 30% are capped (`^`, `~`, `<`). Only the remaining 18% resolve
to the latest release. **Check the specifier mix before quoting the ratio**; a `>=`-heavy manifest
shows no gap at all, and `pinned.py` prints the mix.

🔴 **Two rows to re-scope in any live proposal.** `CAHLR/OATutor`: median **604 d → 1,839 d**,
29 of 35 dependencies cold by more than a year. `ronantakizawa/a11ymcp`, which the previous pass
filed as the **cleanest** row in the corpus (0 of 5 cold): it pins `puppeteer` and `puppeteer-core`
at **13.5.0, 2022-03-05 — 1,675 days and twelve major versions behind**. Its median moves from
**14 d to 686 d**. ⚠️ **A clean latest-release row is not a clean build.**

**Added to the pattern's step 1:** run `pinned.py` over the candidate's manifests and deliver the
specifier-class histogram with the age table. The histogram is what tells the client whether the
gap is a maintenance choice (exact pins, a deliberate freeze) or neglect (caps nobody has raised).

---

## P-REGISTRY-ID — resolve a component's identity through its registry before you put it in a bid

**Use when:** you are about to name an open source component in a proposal, an SBOM, an
architecture page or a vendor questionnaire — which is every engagement.
**Outcome:** the name you write is the one its publisher uses, it is not a fork of something
better maintained, and its governance is current.
**Effort:** minutes per component. Every step is one HTTP or `git` call.

**Why it exists.** Measured over the 503 repositories this KB cites, **21 name a repository other
than the one cited**, and of the **494 distinct repositories** those 503 references name, **9
were cited under two different spellings**.
None of that is visible in a browser: GitHub redirects renames and resolves owner names
case-insensitively, so every wrong citation still works. It stops working when a compiler, an SBOM
tool or a procurement reviewer keys on the string.

**Wiring — four calls, in this order, and the order matters:**

1. **Read the manifest for the package NAME.** `pyproject.toml` / `setup.cfg` / `setup.py` /
   `package.json` / `composer.json` / `mix.exs` / `pom.xml`.
   🔴 **Never assume the package is named after the repository.**
   `repo.packagist.org/p2/packbackbooks/lti-1-3-php-library.json` → **404**; the package is
   `packbackbooks/lti-1p3-tool`, **68 releases**. A census keyed on slugs records a maintained
   library as unpublished.
   ⚠️ **`"private": true` ends the resolution here** — a workspace root is never published and its
   `name` is a local label. Skipping this check produced a fork hypothesis against a *deleted*
   repository for an *unrelated* project.
2. **Ask the registry which repository it declares.** `project_urls` / `repository.url` /
   `source.url`. Reachable from this environment: **PyPI · npm · Packagist · Maven Central ·
   Hex · RubyGems · Go proxy**. Not reachable: `api.github.com`, the rendered `github.com` page,
   `crates.io`.
3. **If the declared slug differs, compare heads.**
   `git ls-remote https://github.com/<a> HEAD` against `<b>`.
   🟢 **Same SHA ⇒ one repository under two names** — a rename or a transfer. Update the name;
   there is no lineage question. 🔴 **Different SHAs ⇒ two repositories**, and only now is
   "which is upstream" worth asking.
4. **Date both channels.** Head commit via `git fetch --depth 1 --filter=blob:none`; latest
   release from the registry. 🟢 **Agreement on the same day is the signature of a maintained
   library** — three of the five rows on this KB's LTI shelf do that. 🔴 **Both cold and equal is
   the signature of abandonment**: `pylti1.3` is 1,416 d on one and 1,417 d on the other.

**What it catches, with the counts from 2026-10-07:**

| | n | Example |
|---|---|---|
| component cited at a former name | 6 | `iterative/dvc` → **`treeverse/dvc`**, a transfer between companies |
| component is a derivative of a better-maintained upstream | 9 | `ucfopen/pylti1.3` → `dmitry-viskov/pylti1.3` |
| the registry name collides with an unrelated project | 5 | `frappe/lms` → `molobrakos/lms`, *a Squeezebox interface* |
| component vendors another project wholesale | 2 | `CNIT-Organization/ltitoolkit` vendors `PyLTI1p3`; `Polygl0t/Polygl0t` vendors `llm-foundry` |
| one repository cited under two spellings | 9 | `LearningEquality/kolibri` and `learningequality/kolibri` |

⚠️ **Steps 2 and 3 are a reading list, not a verdict.** The registry can be stale in the other
direction: PyPI's `openbadges` still declares `IMSGlobal/openbadges-validator-core`, the name
1EdTech left behind in 2022, while this KB has the current one. **The head SHA settles which of
the two is out of date; nothing else does.**

🔵 **Sell it as the first hour of a due-diligence engagement, not as a separate line.** It costs
minutes, it is fully evidenced, and the output — *"these four components have moved owner, this
one is a fork, this one vendors a library its licence does not mention"* — is exactly the content
of the governance section a client's procurement team has to fill in and usually cannot.

## `P-GRANT-ENUMERATION` — resolve a component's licence on three channels before you discard it

**The problem it solves.** A candidate component is rejected because a scan reported no licence. On
this KB's own shelf that verdict was wrong for **15 of 87** repositories, and the ones it was wrong
about include an Open edX core API, a dual-licensed PDF/UA validator and a national OER library.

**Why a filename probe is not enough.** Measured 2026-10-07 over the 87 repositories this shelf had
published as unlicensed:

| Channel | Grants found |
|---|---|
| 14 licence filenames, repository root | **0** |
| 41 licence filenames, repository root | 1 |
| 🟢 complete tree enumeration | **9** |
| 🟢 package registry, with an ownership check | **6 more** |

### The recipe

| Step | Tool | Command | What it decides |
|---|---|---|---|
| 1 | `git` | `git clone --filter=blob:none --no-checkout --depth 1 <url>` then `git ls-tree -r --name-only HEAD` | every path at HEAD — no API, no pagination, **13 s for 87 repos** |
| 2 | `compose/code/p441-tree-licence-enumeration/enumerate_licence.py` | pattern-match `licen[cs]e\|copying\|copyright` over all paths, case-insensitively | candidates at **any depth and any capitalisation** |
| 3 | same | fetch each candidate blob, classify with `p436/sweep_payload.py:family_of` | **a path whose payload is not a licence text is a name, not a grant** |
| 4 | same | reject depth > 2 and the container segments (`assets/`, `libraries/`, `plugins/`, `lib/`, `fonts/`…) | the **project's own** grant versus a **vendored dependency's** |
| 5 | `compose/code/p440-unlicensed-registry-grant/grant.py` | read the publisher's declared `license` on PyPI · npm · Packagist · Maven · Hex | a grant made **only in the registry** |
| 6 | same | compare the registry's declared repository URL against the slug | 🔴 **the ownership gate — without it, 7 of 15 grants belong to someone else** |
| 7 | `compose/code/dependency-licence-closure/dep_licence.py` | classify the string | PERMISSIVE · WEAK- · STRONG-COPYLEFT · NONCOMMERCIAL · **NO-GRANT** · UNKNOWN |

### The four verdicts to wire into a gate, and what each means for a deliverable

| Verdict | Meaning | Action |
|---|---|---|
| `OWN-GRANT-*` | a licence text in the project's own tree | 🟢 the strongest evidence; quote the path |
| `REGISTRY-GRANT` | declared by the publisher, absent from the tree | ⚠️ usable; **`P314`** — one written confirmation citing the publisher's own metadata |
| `BUNDLED-GRANT-ONLY` | every grant found belongs to a vendored dependency | 🔴 the project's own grant is still absent — do not quote the dependency's |
| `ABSENCE-ENUMERATED` | no licence text in the **complete** tree and no registry grant | 🔴 now a sustainable finding, which a filename probe could never produce |

### Three failure modes this pattern exists to prevent, each measured

- 🔴 **A name is not a grant.** The first run of step 2 published an **icon component** called
  `copyright/baseline.vue`, an **XSLT transform**, three **vendored** licences and the European
  Commission's `licence-EUPL 1.2-brightgreen.svg` — a **README badge image**. Step 3 removes all six.
- 🔴 **A package is not necessarily yours.** `pnp-v/bo-google-classroom-mcp-server` declares
  `"name": "class"`; npm's `class` is a 2013 Ruby-style class helper at `deadlyicon/class.js`. And
  `Opetushallitus/aoe` resolves to a 2016 hobby package declaring **GPL-3.0**, while the agency's own
  grant is **EUPL-1.2**. Step 6 is the only thing between those and a wrong licence in a client's SBOM.
- 🔴 **A classifier's order is a verdict.** MPL-2.0 §1.12 names the GPL, LGPL and AGPL; EUPL-1.2's
  Appendix names five families. Probe **EUPL, then MPL and EPL, then the GNU family**, or five MPL-2.0
  components get filed as GPL blockers — which is what happened here. ⚠️ And where a payload names more
  than one family and the granting one is not identifiable from the head — `nvaccess/nvda`'s *"GPL v2 or
  later, with two special exceptions"* — **count the marks and hand over a reading list; do not guess.**

🟢 **Effort: 2–3 days to wire steps 1–7 into an existing SBOM step, on any repository corpus.** The
instruments are in `compose/code/` with **70 offline controls** between `p440` and `p441`, and the whole
sweep over 87 repositories runs in under a minute.

⚠️ **Declared limits.** RTF licence payloads are not read (`docs/LICENSE.rtf`, both `OS4ED/openSIS-*`
rows). Maven Central's POM layer answers **429 intermittently**, so a single-shot probe cannot tell a
POM with no licence from a POM that was rate-limited — retry before recording silence. And for **57 of
87** repositories the registry channel has nothing to say at all, because a project that publishes no
package has no metadata to read.

## `P-GRANT-ENUMERATION` step 8 — twenty-seventh pass: classify with BOTH classifiers, because neither is a superset

🔵 **Added 2026-10-07.** Steps 1–7 above answer *"is there a grant, and whose is it?"* — and they
answer it well: 15 of 87 rejected components recovered. **This step answers "what does it say?",
and the measurement behind it is that this repository cannot answer that with one tool.**

⚠️ **Step 3 classifies each payload with `p436/sweep_payload.py:family_of`. That function has no
NonCommercial axis.** Step 7's `dep_licence.py` does carry a `NONCOMMERCIAL` verdict, but it
classifies a **dependency string**, not a licence **payload** — so nothing in steps 1–7 can see a
non-commercial restriction in a repository's own `LICENSE` file.

```sh
# 8. CLASSIFY WITH BOTH, on the same bytes, and reconcile  (P445 / trend 64)
compose/code/p445-classifier-divergence/divergence.py
#    lib/license_family.sh  -> osi_family_of + commercial_use_ok   (NC, Elastic, PolyForm)
#    p436/sweep_payload.py  -> family_of                           (EUPL, MPL-not-GPL)
#    over 412 LICENSED roots: AGREE 369 · VOCABULARY 25 · PYTHON-UNKNOWN 13 · NC-ERASED 5
```

### 🔴 Why one classifier is not enough, measured over 412 payloads

| Case | `family_of` (Python, step 3) | `lib/license_family.sh` | Who is right |
|---|---|---|---|
| **NonCommercial** (5 rows) | 🔴 erased to `CC-BY` | 🟢 `CC-BY-NC-*`, commercial `NO` | **shell** |
| **Elastic / PolyForm** (3) | 🔴 `UNKNOWN` | 🟢 named | **shell** |
| **EUPL** (9) | 🟢 `EUPL` | 🔴 `UNCLASSIFIED` | **Python** |
| **MPL read as GPL** (4) | 🟢 `MPL-2.0` | 🔴 `GPL-3.0` | **Python** |
| **GPLv2 read as LGPL** (4) | 🔴 `LGPL` | 🟢 `GPL-2.0` | **shell** |

🔵 **Each was hardened against the defect the other still has.** Step 7's note above — *"probe EUPL,
then MPL and EPL, then the GNU family"* — is the Python classifier's fix, and the shell classifier
never received it. The shell classifier gained the NC axis in pass 101 (`P312`, 21/21) and the
source-available families in pass 82, and the Python one never received those.
⚠️ **43 of 412 (10.4%) are wrong in one of the two, and which one depends on the family.**

### 🔴 The eight rows this step exists to catch before they reach a bid

A shelf filtered for *redistributable* components on step 3's output **includes all five of these**,
because all five report as plain `CC-BY` — a licence that permits commercial use:

| Repo | Actually | What it is |
|---|---|---|
| [`facebookresearch/seamless_communication`](https://github.com/facebookresearch/seamless_communication) | **CC-BY-NC-4.0** | multilingual speech — the top hit for "open source multilingual speech" |
| [`openstax/osbooks-biology-bundle`](https://github.com/openstax/osbooks-biology-bundle) | **CC-BY-NC-SA-4.0** | open textbook content |
| [`sign/translate`](https://github.com/sign/translate) | **CC-BY-NC-SA-4.0** | sign-language translation |
| [`Yunfeng-Wan/CSTutorBench`](https://github.com/Yunfeng-Wan/CSTutorBench) | **CC-BY-NC-4.0** | CS-tutoring benchmark |
| [`Jona-Zwetsloot/Somtoday-Mod`](https://github.com/Jona-Zwetsloot/Somtoday-Mod) | **CC-BY-NC-SA-4.0** | NL SIS client |

Plus three that bar commercial use with **no `NC` token at all**:
[`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) and
[`sodadata/soda-core`](https://github.com/sodadata/soda-core) (**Elastic**),
[`digillab-lmu/smart-rag`](https://github.com/digillab-lmu/smart-rag) (**PolyForm**) —
source-available, not OSI. **11 of 412 root payloads restrict commercial use; step 3 flags none.**

### 🟢 Two rules for the write-up

1. **Report the commercial axis separately from the family.** `P250` built them as two independent
   axes, and `commercial_use_ok` is the one answering the question a client is actually asking.
   Searching for `NC` inside a family *name* misses the Elastic and PolyForm rows entirely — and
   matches `UNCLASSIFIED`, which contains those letters.
2. **Name the classifier beside the verdict.** *"MIT, per `lib/license_family.sh` on
   `LICENSE@HEAD`"* is auditable; *"MIT"* is not, and on this shelf it is wrong once in ten.

### What step 8 adds to the scoping

| | |
|---|---|
| **Cost** | under an hour on top of steps 1–7 — both classifiers already exist and it needs **no network** |
| **Changes** | the **redistributable** count, which is the number a bid is built on: 11 of 412 move from "usable" to "not billable" |
| **Controls** | `compose/code/p445-classifier-divergence/` — **22 offline**, on top of the 70 between `p440` and `p441` |
| **Sells hardest in** | **EMEA**, where the 9 EUPL rows the shell cannot name are the public-sector tier and the AI Act already imposes documentation duty; and in any engagement that redistributes modified source |
