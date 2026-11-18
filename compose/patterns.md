---
industry: education
region: Global
updated: 2026-11-18
---

# Compose patterns — education

Concrete recipes. Each names the exact repos, how they wire together, the licence posture of
the result, and a realistic build estimate. Every repo referenced is verified in
`agents/top.md`, `repos/foundations.md` or `verticals/solutions.md`.

**Licence rule that governs all of these.** Open edX (AGPL-3.0), Canvas (AGPL-3.0) and Moodle
(GPL-3.0) are copyleft. Integrating over **LTI 1.3** or **MCP** keeps your tool a separate
work; forking the platform does not. Where a client needs a proprietary derivative, start from
**Artemis (MIT)**, **Kolibri (MIT)**, **Oppia (Apache-2.0)** or **OpenOLAT (Apache-2.0)** instead.

---

## P1 — Licence-clean AI tutor on a permissive LMS

**For:** any client who needs to keep the result closed, or who has no incumbent LMS.
**Region:** Global. Strongest fit EMEA (EU-origin stack, sovereignty-compatible).

```
ls1intum/Artemis (MIT)                  — LMS core, exercises, cohorts
  └── ls1intum/edutelligence (MIT)      — AI service suite, already integrated
        └── ls1intum/Pyris (MIT)        — LLM microservice behind the Iris tutor
              └── BerriAI/litellm (MIT) — provider gateway + per-course budget caps
                    └── ollama (MIT) or vllm-project/vllm (Apache-2.0)  — self-hosted inference
  └── ls1intum/Ares (MIT)               — automated programming assessment
  └── qdrant/qdrant (Apache-2.0)        — per-course retrieval, payload-filtered by course_id
  └── mem0ai/mem0 (Apache-2.0)          — per-learner memory ("what this student struggled with")
```

**Wiring.** Artemis already speaks to Pyris, so the integration work is configuration, not
code. Point Pyris at `litellm` instead of a provider SDK — that one indirection is what makes
inference swappable and gives you per-course cost caps. Scope every Qdrant query by
`course_id` in the payload filter; cross-course leakage is the most common correctness bug in
education RAG.

**Result licence:** fully permissive (MIT/Apache-2.0). Proprietary extensions are clean.
**Estimate:** 6–8 weeks to a departmental pilot.

---

## P2 — Governed AI tier over an existing Moodle or Canvas (no fork)

**For:** the common case — the client already runs Moodle or Canvas and cannot replace it.
**Region:** Global. LATAM/EMEA for Moodle, North America for Canvas.

```
Incumbent: moodle/moodle (GPL-3.0)  or  instructure/canvas-lms (AGPL-3.0)
   │
   ├── LTI 1.3 route:  Cvmcosta/ltijs (Apache-2.0)        — your tool, separate work
   │     (PHP shops: tsugiproject/tsugi, Apache-2.0)
   ├── MCP route (Canvas): vishalsachdev/canvas-mcp (MIT)  — agent tools over Canvas API
   ├── apereo/cas (Apache-2.0)                             — SSO, role-based access to the AI tier
   │
   └── Your AI tier (kept outside the LMS repo):
         langchain-ai/langgraph (MIT)     — orchestration; policy checks as explicit nodes
         BerriAI/litellm (MIT)            — gateway, per-user/per-course budgets
         HKUDS/LightRAG (MIT)             — graph RAG over the course corpus
         docling-project/docling (MIT)    — PDF/slide ingestion
         SYSTRAN/faster-whisper (MIT)     — lecture transcription
         yetanalytics/lrsql (Apache-2.0)  — xAPI statements for every AI interaction
         appsmithorg/appsmith (Apache-2.0)— teacher review queue
```

**Wiring.** The LMS stays untouched; your tool is an LTI 1.3 tool provider registered in it.
Make the human-review step a LangGraph node that *blocks* — if the teacher queue is down, the
AI output does not reach the student. Emit an xAPI statement to `lrsql` for every AI
interaction, including refusals; that log is both the efficacy evidence and the compliance
artefact. Moodle HQ's own `moodlehq/wiki-rag` (BSD) is the reference for first-party Moodle RAG.

**Result licence:** your tier is permissive and separate from the GPL/AGPL core.
**Estimate:** 8–10 weeks including LTI certification and SSO.

---

## P3 — North America K-12 policy-conformant assist (50-state configurable)

**For:** US districts and K-12 vendors facing fragmented state law.
**Region:** North America.

```
virtualryder/edu-ai-agents (MIT)        — governance spine: deny-by-default authz,
                                          student-PII masking, human-in-the-loop enforcement,
                                          tamper-evident audit (FERPA/COPPA/IDEA-504/ADA)
  └── Ed-Fi-Alliance-OSS/Ed-Fi-ODS (Apache-2.0)  — the K-12 data standard across most US states
  └── Policy-config layer  (studio IP)  — per-state rules as data, not code
  └── Deterministic rubric scorer (NOT an LLM) — required by Oklahoma SB 1734
  └── openedx/edx-ora2 (AGPL-3.0) or ls1intum/Ares (MIT) — the grading workflow it feeds
  └── appsmithorg/appsmith (Apache-2.0) — teacher review and override console
  └── yetanalytics/lrsql (Apache-2.0)   — audit + parent-disclosure record
```

**Wiring.** The critical design decision is that **grading scores come from a deterministic
rubric service and the LLM only drafts narrative feedback**, which a teacher approves. That
single split satisfies Oklahoma's prohibition on AI-only grading, Idaho's bar on AI replacing
teachers, and the teacher-review mandates generally — and `virtualryder/edu-ai-agents` is
already built that way, which is why it is the spine rather than a reference.

Model each state's rules as configuration: *AI-only grading permitted (no)*, *parent opt-out
required*, *minimum grade for direct student AI use* (New York A 9190 would set grade 9),
*district framework deadline* (Ohio: 1 July 2026). A district crossing state lines flips a
config value, not a code path. This layer is the defensible studio asset.

**Result licence:** permissive apart from the `edx-ora2` option — prefer `Ares` (MIT) for a
closed derivative.
**Estimate:** 10–12 weeks for the spine plus three states; ~1 week per additional state.

---

## P4 — EMEA AI Act conformity-by-construction (admissions / assessment / proctoring)

**For:** EU institutions and edtech vendors with a hard 2 December 2027 date.
**Region:** EMEA.

```
Classify first: is the system Annex III high-risk?
  admissions · assessment & learning-outcome determination ·
  educational-level assignment · exam monitoring   → YES, obligations from 2026/1744: 2 Dec 2027
  Already banned (since Feb 2025): emotion recognition in schools — do not build it
  Already in force (Aug 2026): Article 50 — tell the student they are talking to an AI

Sovereign-by-default stack (EUA Jan 2026 favours European LLMs):
  ollama (MIT) / vllm-project/vllm (Apache-2.0)   — inference inside the institution
  BerriAI/litellm (MIT)                           — gateway; NO US-hosted API in the data path
  qdrant/qdrant (Apache-2.0)                      — vector store, self-hosted
  ls1intum/Artemis + edutelligence + Pyris (MIT)  — EU-origin, permissive platform tier
  temporalio/temporal (MIT)                       — durable runs; execution history IS the log
  yetanalytics/lrsql (Apache-2.0)                 — xAPI evidence of human oversight
  langchain-ai/langgraph (MIT)                    — oversight + disclosure as explicit nodes
  promptfoo (MIT) + AI-for-Education/pedagogy-benchmark (MIT)  — versioned eval evidence
```

**Wiring.** Three things make conformity cheap later: Article 50 disclosure as a non-bypassable
node (not a UI string), Temporal's execution history as your immutable audit record, and
`promptfoo` running `pedagogy-benchmark` in CI so you can show *when* behaviour changed and
that you tested it. Deliver the Annex III classification memo as the first artefact — it scopes
everything else and is billable on its own.

**Caveat to state to the client in writing:** confirm the 2 December 2027 date against the
Regulation (EU) 2026/1744 text. Many published sources still carry the superseded 2 August 2026
date, and this is the most commonly mis-stated fact in the sector.

**Result licence:** fully permissive, self-hostable, no US data path.
**Estimate:** 4 weeks for classification + documentation; 12–14 weeks for the governed build.

---

## P5 — LATAM governance-and-enablement retrofit (the 53/22 gap)

**For:** institutions already using AI without guidelines — 53% of Brazilian administrators use
AI, 22% have policies; 87% of regional universities use AI, 26% have a strategy.
**Region:** LATAM.

```
Week 1–2  Discovery: what AI is already in use, by whom, on what student data
Week 2–4  Policy pack: acceptable-use, disclosure, assessment-integrity, data handling
             (anchor to Brazil PL 2338/2023's pending obligations — it covers education)
Week 3–6  Technical retrofit, not replacement:
             BerriAI/litellm (MIT)         — put every existing AI call behind one gateway,
                                             with per-department budget caps and full logging
             yetanalytics/lrsql (Apache-2.0) — xAPI record of AI use (the missing evidence)
             appsmithorg/appsmith (Apache-2.0) — teacher disclosure + override console
             openfun/ralph (MIT)           — alternative LRS if Python/French-stack preferred
Week 4–8  Teacher enablement (the real deliverable; TALIS says they already use AI)
             patchy631/ai-engineering-hub (MIT) — staff upskilling material
Ongoing   Portuguese/Spanish pedagogical localisation of an APAC/EMEA-origin tutor:
             HKUDS/DeepTutor (Apache-2.0) or THU-MAIC/OpenMAIC (MIT)
Public sector (Brazil):
             portabilis/i-educar (LGPL)    — SIS built around Brazilian regulatory requirements
Low-connectivity:
             learningequality/kolibri (MIT) + iiab/iiab (LGPL) + ollama (MIT) — fully offline tutor
```

**Wiring.** The `litellm` gateway is the highest-leverage single move: it converts "AI is
happening somewhere in our institution" into a metered, logged, budgeted channel in days,
without asking anyone to stop what they are doing. Everything else builds on that visibility.

**Why localisation rather than build:** there is effectively no LATAM-origin open education
agent (only `warleysr/ankipa`, an Anki add-on). Localising DeepTutor or OpenMAIC is faster and
the pedagogical localisation is itself the billable differentiation.

**Estimate:** 6–8 weeks.

---

## P6 — APAC multi-jurisdiction deployment with content provenance

**For:** regional edtech or a multinational operating across Korea, China, India and Japan.
**Region:** APAC.

```
langchain-ai/langgraph (MIT)  — one graph, per-jurisdiction policy nodes:
    VN  → Law on AI 134/2025/QH15 + Decree 142 + Decision 33/2026/QD-TTg (eff. 15 Aug 2026):
          EDUCATION IS STATUTORY HIGH-RISK (3 of 46 listed systems — behavioural monitoring,
          learner ranking, automated assessment). Existing systems: comply by 1 Sep 2027.
          New systems: 1 Mar 2027. Notification to MOST; registration can be refused.
          *** Build this node FIRST: it is the earliest statutory deadline in the region. ***
    KR  → AI Basic Act (in force 22 Jan 2026): risk classification + oversight duties.
          2026 is a guidance-first grace period; decrees still being finalised.
    CN  → service-type rules + AI-content labelling; Cybersecurity Law AI clause (1 Jan 2026)
    IN  → IT Rules: prominent labels + provenance markers on generated content (20 Feb 2026)
    AU  → no AI statute, but TEQSA moved to a REGULATORY-LED posture in 2026 and inspects the
          genAI action plan the provider already filed (all 203 providers, 2024, 100% response).
          The client's own action plan is the requirements document — read it before scoping.
          Binding layer: Higher Education Standards Framework (Threshold Standards).
          Schools: Australian Framework for Generative AI in Schools + state additions.
    JP  → promotion-first + voluntary guidelines, NO education-specific statute (confirmed
          absence, p890) → lowest-friction pilot geography

Provenance emitted at generation time (NOT retrofitted):
    every generated item carries model, version, prompt hash, timestamp, generator identity
    yetanalytics/lrsql (Apache-2.0) — provenance + interaction record
    temporalio/temporal (MIT)       — reproducible generation runs

Content pipeline tuned for the region:
    opendatalab/MinerU (Apache-2.0)   — CJK textbooks and formulas; beats Western-trained parsers
    SYSTRAN/faster-whisper (MIT)      — multilingual lecture transcription

Tutor core (APAC-origin, permissive — partner, don't rebuild):
    HKUDS/DeepTutor (Apache-2.0)      — agentic personalised tutoring, HKU
    THU-MAIC/OpenMAIC (MIT)           — multi-agent classroom, Tsinghua, v1.4.2 (2026-11-09)
    netless-io/flat (MIT)             — interactive classroom with whiteboard
```

**Wiring.** Labelling is a dated legal requirement in two of the four markets, so provenance
metadata is emitted by the generator and stored with the artefact — retrofitting labels across
an existing content library is the expensive path. `MinerU` is the specific reason this pattern
differs from P2: CJK textbook extraction quality determines whether the whole RAG tier works.

**Mandatory non-technical workstream.** Korea attempted a national AI-digital-textbook rollout
from 2025 and reduced it to optional status within a year after teacher and parent backlash.
Budget a named teacher- and parent-consent workstream. **Cite Korea when a client wants to skip
it** — the failure was social, not technical, and it is the cheapest lesson available.

**Sequencing added in p890.** Vietnam's clock (1 March 2027 for new systems) expires **before**
the EU's 2 December 2027, so an Annex-III-grade oversight architecture built for EMEA should be
*reused* here rather than rebuilt — and it is needed sooner. Australia inverts the usual sales
motion: the provider has already written and filed a genAI plan and is now being held to it, so
the engagement is implementation of an existing commitment, not persuasion.

**Estimate:** 12–14 weeks for two jurisdictions; ~3 weeks per additional jurisdiction. Add
~2 weeks for the Vietnam node (the high-risk list is closed and specific, so classification is
quick, but notification and registration are procedural).

---

## P7 — Evidence-of-efficacy tier (attach to any of the above)

**For:** any engagement that will face a procurement office or regulator asking "did it work?"
**Region:** Global.

```
yetanalytics/lrsql (Apache-2.0)                     — xAPI statements for every interaction
  └── openfun/ralph (MIT)                           — alternative LRS (Python stack)
AI-for-Education/pedagogy-benchmark (MIT)           — pedagogical ability, not subject knowledge
EleutherAI/lm-evaluation-harness (MIT)              — subject-knowledge benchmarks, extensible
promptfoo/promptfoo (MIT)                           — CI regression gates on prompts/models
HumanSignal/label-studio (Apache-2.0)               — rubric calibration, grading gold sets
argilla-io/argilla (Apache-2.0)                     — teacher feedback collection and curation
open-spaced-repetition/fsrs4anki (MIT)              — evidence-backed review scheduling,
                                                      instead of an invented schedule
```

**Wiring.** Build the gold set with teachers in `label-studio` *before* the tutor ships; it is
both the eval baseline and the rubric-calibration artefact. Wire `promptfoo` into CI so a model
or prompt change that regresses pedagogy fails the build. Use `fsrs4anki`'s FSRS scheduler
rather than having an agent invent review intervals — there is real evidence behind it.

**Why this pattern exists.** No credible primary evidence of learning gains from AI at scale
was found in this pass; the widely quoted "42% improvement" style figures trace to blogs with
no primary study. Almost no vendor ships a measurement tier, every regulator is converging on
demanding one, and a client who can answer the question has something their competitors cannot
buy.

**Estimate:** 3–4 weeks, and it makes every other pattern defensible.

---

## P8 — Per-institution AI metering, cost attribution and exit (the Jisc specification)

**For:** any institutional engagement in the UK, and increasingly anywhere a procurement office
reviews an AI contract. **Region:** EMEA primarily; the architecture is Global.
**New in pass p890.**

**Why this pattern exists.** Jisc, with Universities UK, GuildHE and the Association of
Colleges, published what is effectively a buyer-side specification: transparent pricing,
demonstrable value, meaningful institutional choice, protection of existing functionality,
**granular usage and cost controls**, interoperability, **data portability** and safeguards
against **vendor lock-in**. The trigger is usage-based pricing replacing per-seat licences, and
institutions paying several times over for overlapping AI embedded in different platforms. A
companion Jisc/EAUC report found vendors seldom publish institution-level usage at all. Every
other pattern in this file answers a regulator; **this one answers the person who signs the
cheque**, and they have written the requirements down.

```
Request path — attribution is established before inference, not inferred afterwards:

  apereo/cas (Apache-2.0)            — SSO; the identity that carries
                                       institution / faculty / course / role claims
    └── Cvmcosta/ltijs (Apache-2.0)  — LTI 1.3 launch; course + role context from the LMS,
                                       so the tool detaches from any one platform
        └── BerriAI/litellm (MIT)    — gateway: ONE virtual key per cost centre
                                       (institution → faculty → course), hard budget caps,
                                       provider-agnostic so the model layer stays swappable
            ├── ollama/ollama (MIT)  — local inference: the zero-marginal-cost tier
            ├── vllm-project/vllm (Apache-2.0) — self-hosted at throughput
            └── hosted API           — the exception, and now a visibly priced one

Metering and export — OpenTelemetry, because OTel IS the portability answer:

  traceloop/openllmetry (Apache-2.0, 7,541★)  — PREFERRED. OTel-native LLM tracing: the
                                                usage data lands in the observability stack
                                                the institution already runs. Nothing to
                                                migrate on exit because nothing was captive.
  openlit/openlit (Apache-2.0, 3,088★)        — OTel-native alternative with cost tracking
  Helicone/helicone (Apache-2.0, 6,287★)      — gateway-level logging and cost attribution
  (langfuse/langfuse, 37,577★ — LARGEST BUT SPLIT LICENCE: "MIT Expat" core, separate
   enterprise licence on ee/, web/src/ee/, worker/src/ee/, packages/shared/src/server/ee/;
   copyright now ClickHouse, Inc. Diligence before it enters a client deliverable.)

Evidence that the spend bought something:

  yetanalytics/lrsql (Apache-2.0)             — xAPI: usage joined to learning interactions,
                                                which is how "demonstrable value" stops being
                                                a slide and becomes a query
  qdrant/qdrant (Apache-2.0)                  — embeddings in a store the CLIENT owns
```

**Wiring.**

1. **Mint one `litellm` virtual key per cost centre, not per application.** Attribution has to
   exist at request time; a report that infers which faculty spent what is the thing the Jisc
   statement is complaining about.
2. **Carry institution/faculty/course/role from CAS and the LTI 1.3 launch into the gateway
   key** — the LMS already knows the context, so do not rebuild a hierarchy beside it.
3. **Emit OTel spans, not vendor events.** This is the single decision that satisfies data
   portability: the institution can point the exporter at its own collector on day one, and
   nothing has to be extracted on exit.
4. **Set hard caps, not alerts.** Usage-based pricing without a ceiling is the exposure; a
   budget cap that returns a graceful degradation (local `ollama` model instead of a hosted
   call) keeps the service up while the cost stays bounded.
5. **Write the exit into the build:** documented export of usage data, embeddings, prompts and
   content, plus an LTI 1.3 integration that the client can repoint at another tool. Deliver it
   as a runbook, because an untested exit is not an exit.
6. **Price per learner-outcome, not per token.** The buyer has stated publicly they will not
   sign per-token exposure.

**What makes this defensible.** None of the four metering repos is built for education: they
know about users and projects, not institutions, faculties, courses and cohorts. **Mapping an
OTel LLM-metering layer onto an academic hierarchy, with LTI-derived context and per-cost-centre
budget enforcement, is genuine studio IP** — it answers a published, signed, sector-wide
requirement, and no vendor currently ships it.

**Caveat.** The Jisc statement is a request to suppliers, not a regulation. It carries no
penalty. Its force is commercial: it is signed by the bodies representing most of UK higher and
further education, and it tells you precisely what a tender will ask.

**Estimate:** 5–7 weeks on top of an existing AI tier; ~9 weeks standalone. The exit runbook
and the per-cost-centre hierarchy are the long poles, not the tracing.

---

## P9 — Integrity by assessment redesign, not detection

**For:** any higher-education or senior-secondary client currently buying, piloting or being
pressured to buy AI-detection tooling.
**Region:** Global. Strongest fit **North America (Canada especially)** and **EMEA**; also the
compliant answer to the **UAE** exam-context prohibition.
**Added:** p891. Evidence behind it: **T10** in `intel/trends.md`.

### Why this pattern exists

Detection is being removed as a control by institutional counsel, not by faculty. All six
Canadian universities in a 2026 review declined to enable or endorse AI detection, privacy
cited at four; Concordia bars staff from using online detectors outright; UBC cites a Privacy
Impact Assessment. Sending student work to a third-party detector is a disclosure event under
FOIPPA/FIPPA, GDPR, and the US state student-data statutes — **California AB 1159 bars using
student data to train AI models at all**. Meanwhile the EU Council's October 2026 conclusions
ask member states for **academic-integrity policies**, and the UAE's classroom guide bans AI
**during exams and assessments**. Every regional signal asks for a *process control*. None asks
for a *classifier*.

**Sell this as the replacement for a detection line item that is about to be cancelled.**

### Stack

```
Incumbent LMS (Moodle GPL-3.0 / Canvas AGPL-3.0 / Open edX AGPL-3.0)
  │   integrate over LTI 1.3 — never fork; keeps your work a separate work
  ├── ls1intum/Artemis (MIT) ................ where a permissive core is available:
  │     └── ls1intum/edutelligence (MIT) .... already-integrated AI tier
  │                                           exercise + rubric model to copy
  ├── Submission-process instrumentation ..... draft history, revision timeline,
  │     (LMS-native: Moodle assign plugin /    time-on-task — product evidence
  │      Canvas submission API via            replaced by process evidence
  │      vishalsachdev/canvas-mcp, MIT)
  ├── openedx/edx-ora2 (AGPL-3.0) ........... open-response + peer/self/staff grading;
  │                                           the seam for structured oral defence
  ├── CAHLR/OATutor (MIT) ................... A/B-testable tutoring instrumentation —
  │                                           use it to prove the redesign worked
  ├── langchain-ai/langgraph (MIT) .......... rubric-reasoning agent as explicit,
  │                                           auditable policy nodes (not a verdict)
  ├── AI-for-Education/pedagogy-benchmark (MIT)  eval gate before anything touches a cohort
  └── ollama (MIT) / vllm-project/vllm (Apache-2.0) + BerriAI/litellm (MIT*)
        *litellm is MIT outside `litellm/enterprise/`; that directory is separately
         licensed. Use the OSS paths — see repos/foundations.md.
        └── student work never leaves the institution — this is what makes the PIA pass
```

### The design rule that makes it defensible

**No component emits a judgement about whether a student used AI.** The agent tier grades
*reasoning against a rubric* and surfaces *process artefacts* to a human marker. The integrity
finding is always made by a person, from evidence the student can see and contest. That is what
survives a privacy review, an appeal, and EU AI Act Article 14 human-oversight design — which
is deferred to **2 December 2027** but is the standard the architecture should already meet.

### Deliverables

1. **Assessment-redesign programme** — rubrics that grade reasoning, drafts and version history
   as graded artefacts, supervised in-class components, oral defence for a sampled subset.
2. **Process-evidence instrumentation** in the incumbent LMS, over LTI 1.3.
3. **Privacy artefact** — PIA, vendor-assessment template, data-flow diagram showing inference
   is local. In Canada this is the document that unlocks procurement.
4. **Appeals runbook** — how a contested finding is reviewed, by whom, on what evidence.
5. **Efficacy measurement** — attach **P7**; OATutor's instrumentation is the cheapest route to
   a defensible before/after.

### Licence posture

Clean. Everything load-bearing is MIT/Apache-2.0 and reached over LTI 1.3, so a GPL/AGPL
incumbent LMS stays a separate work. `edx-ora2` is AGPL — use it **in place** inside an existing
Open edX deployment, do not vendor it into a proprietary derivative.

### Estimate

**8–11 weeks.** Assessment redesign with faculty is the long pole, not the engineering —
budget roughly 40% of the effort for workshops and rubric development, and expect the
privacy artefact to gate go-live in Canada and EMEA. A detection-replacement framing shortens
the sales cycle considerably, because the budget already exists.

### Where it does not apply

Where a regulator has mandated proctoring or automated assessment outright — **Vietnam**, where
automated assessment is statutorily high-risk under Decision 33/2026/QD-TTg with an 18-month
education transition. There the engagement is **P6** plus conformity work, not this pattern.

## P10 — National curriculum-mandate delivery: teacher enablement at system scale

**New in pass p892.** Written once for **India** and **Saudi Arabia** because the two
engagements are the same build with the curriculum corpus and the language swapped. Also fits
Vietnam's 12-periods-per-year mandate and, with the student tier removed, the EU Article 4
staff-literacy duty.

### Why this pattern exists

Every other pattern in this file answers a constraint on AI *use*. This one answers a state
mandate to *teach* AI, which T11 establishes across India, Saudi Arabia, Vietnam, the UAE,
North Carolina and the African Union strategy. The distinguishing facts:

- **The curriculum already exists and the client owns it.** NCERT/CBSE in India; the National
  Curriculum Center in Saudi Arabia. **Do not author courseware.** Authoring it is both out of
  scope and politically unwinnable.
- **The constraint is teacher capacity, stated explicitly by the buyers** — 240,000 teachers in
  training in KSA (60,000 reached), and India's own commentary that adding a subject is not the
  same as preparing teachers to teach it.
- **The buyer is a ministry or board**, so evidence of coverage is a contractual artefact, not
  a nice-to-have.

### Stack

Every repo named is verified in this KB with licence and last-push date.

**1. Curriculum ingestion — the client's own documents, never a generic corpus**

| Component | Repo | Licence |
|---|---|---|
| PDF/DOCX curriculum → structured text | `docling-project/docling` | MIT |
| Heavier layout/formula extraction | `opendatalab/MinerU` | Apache-2.0 (SPDX NOASSERTION) |
| Retrieval over the ingested curriculum | `HKUDS/LightRAG` or `infiniflow/ragflow` | MIT / Apache-2.0 |
| Vector store the client owns | `qdrant/qdrant` | Apache-2.0 |

**2. Model layer — swappable, because sovereignty differs by market**

| Component | Repo | Licence |
|---|---|---|
| Gateway, per-district keys and budget caps | `BerriAI/litellm` | **MIT except `litellm/enterprise/` — do not vendor that path** |
| Local/self-hosted inference | `ollama/ollama` · `vllm-project/vllm` | MIT / Apache-2.0 |

Keep the gateway even if the first deployment calls a hosted API. It is what lets the Saudi
build answer a national-AI-company requirement and the Indian build answer a data-residency
one without re-architecture (T6).

**3. Teacher-facing generation — the actual deliverable**

| Component | Repo | Licence |
|---|---|---|
| Lesson/slide/quiz generation from curriculum | `THU-MAIC/OpenMAIC` | MIT |
| Local-first lesson-prep design reference | `SirhanMacx/Claw-ED` | MIT — **read it, do not pin it** (last push 2026-09-19) |
| Exercise/item rendering | `Khan/perseus` | MIT |
| Orchestration with explicit policy nodes | `langchain-ai/langgraph` | MIT |
| Durable long-running enrolment/cohort workflows | `temporalio/temporal` | MIT |

**4. Delivery and reach**

| Component | Repo | Licence |
|---|---|---|
| Training delivery to teachers | `oppia/oppia` (Apache-2.0) if greenfield; integrate to the client's LMS over **LTI 1.3** with `Cvmcosta/ltijs` (Apache-2.0) if not | Apache-2.0 |
| Low-bandwidth / offline cohorts | `learningequality/kolibri` | MIT |
| Admin and cohort-tracking console | `appsmithorg/appsmith` | Apache-2.0 |

**5. Evidence — the part that gets the contract renewed**

| Component | Repo | Licence |
|---|---|---|
| Pedagogical-quality eval gate on generated material | `AI-for-Education/pedagogy-benchmark` | MIT |
| Per-district/per-cohort usage and cost attribution, OTel-native | `traceloop/openllmetry` | Apache-2.0 |

### How it wires together

1. Ingest the ministry's curriculum with `docling` → chunk → embed → `qdrant`. **This corpus is
   the only authority the generation tier may cite.**
2. `langgraph` runs the generation flow with the policy checks as explicit nodes: grade-band
   check, curriculum-citation check, provenance-label emission, language check. Explicit nodes
   are what make the flow auditable to a ministry.
3. `litellm` fronts every model call, keyed per district so cost attribution exists from day one.
4. `OpenMAIC` generates the teacher's lesson, slides and quiz items; `perseus` renders items.
5. `pedagogy-benchmark` gates output on pedagogical quality before a teacher ever sees it.
6. Delivery through `oppia`, or into the client's existing LMS over LTI 1.3 via `ltijs`;
   `kolibri` carries the offline cohorts.
7. `openllmetry` emits coverage and cost per district into whatever observability stack the
   ministry already runs — which is also the portability answer (T9).

### The design rules that make it defensible

- **Retrieval over the ministry's curriculum, never training on it, and never on student or
  teacher data.** California AB 1159 forecloses the training architecture outright; building
  the no-training version once makes the same stack sellable in every market.
- **Emit provenance labels at generation time.** India's amended IT Rules require prominent
  labels and provenance markers on AI-generated content from **20 February 2026** (T7).
  Retrofitting a national content library is the expensive path.
- **Grade-banding is a policy node, not a prompt.** India's mandate is Classes III–VIII; the
  UAE prohibits under-13 and below-Grade-7 use entirely. The same deployment must be able to
  answer both, and a prompt instruction is not an answer a regulator accepts.
- **Teacher-in-the-loop is the product.** Generated material is a draft a teacher edits and
  approves, and the approval is logged. This is T1's oversight requirement and also the only
  posture that survives T8's consent problem.

### Deliverables

1. Curriculum-grounded lesson-preparation service, grade-banded, provenance-labelled.
2. Teacher training-delivery tier with per-cohort completion evidence.
3. Coverage and cost dashboard by district, exportable (the ministry's reporting obligation).
4. Policy-node configuration per jurisdiction — grade bands, prohibitions, labelling.
5. Evaluation report from `pedagogy-benchmark` on generated material, as an acceptance gate.

### Licence posture

Clean. Every component is MIT or Apache-2.0 except the carve-out in `litellm/enterprise/` (do
not vendor it) and `kolibri`'s MIT core, which is fine. **If the client's LMS is Moodle
(GPL-3.0) or Canvas (AGPL-3.0), integrate over LTI 1.3 and the deliverable stays a separate
work** — the single most important licence decision in this pattern (see `README.md`, fact 1).

### Estimate

**14–18 weeks** to a first district or regional cohort: 3–4 weeks curriculum ingestion and
retrieval quality, 4–5 weeks generation tier and policy nodes, 3–4 weeks delivery integration,
2–3 weeks evidence tier, 2 weeks evaluation and acceptance. Longer than every other pattern
here because the buyer is public-sector and acceptance is formal.

### Where it does not apply

- **Not for institutional self-service markets.** If the buyer is a single university, this is
  P2 or P8, not P10.
- **Not where no mandate exists.** Without a funded state programme this becomes speculative
  courseware, which is a product business and not a services engagement.
- **Not as a route to selling a student tutor.** The mandate is teacher capacity (T11). A
  student-facing tutor sold against it is the wrong deliverable, and every open tutor this KB
  tracks is English- or Chinese-first — in India and Saudi Arabia that is a localisation
  project, not a dependency.

