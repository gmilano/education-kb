---
industry: education
region: Global
updated: 2026-11-17
---

# Compose patterns — education

**Pass `p875`, 2026-11-17** (fifth pass of the day). **Thirteen recipes** — `p875` adds **P12**,
a hardened OpenMAIC classroom built on the licence question this KB has now settled four ways and
on a **student-data exposure in OpenMAIC's default configuration that its own README documents**;
and **P13**, US district policy conformance sold against published state deadlines rather than
against an AI thesis.

🔴 **P11 carries a corrected date.** It was written on a literacy duty "binding since July 2026."
**The duty has applied since 2 February 2025**, and a *second* duty — transparency for chatbots and
AI-generated content — went live **2 August 2026**. **P11's argument strengthens and its dates
change**; see the corrected **T11**. Any P11 deck in circulation must be fixed.

🟡 **A caveat now attaches to every pattern in this file that promises measurement** (P1, P5, P7
especially): **the xAPI Learning Record Store they route telemetry through, `LearningLocker`, has
not been pushed since May 2024.** `p875` found no maintained permissive replacement. Budget a
maintained fork explicitly, or fall back to the LMS gradebook and say so.

**Previous pass note (`p873`):** ten recipes — `p871`'s six, `p872`'s **P7**
and **P8** (and its rewrite of **P2**), plus **P9** and **P10** added by `p873`: a Spanish-language
tutor built on the LATAM-origin base this KB verified for the first time, and an
accessibility-gated public-sector bid. Every repo named below was verified
(existence via `git ls-remote`, licence via the licence bytes on the resolved default branch);
licences are stated inline because in this vertical the licence determines the architecture.
Effort estimates are studio-delivery estimates, not measurements.

---

## P1 — FERPA/LGPD-defensible self-hosted tutor

**Sell to:** North America (FERPA), LATAM (LGPD), EMEA institutions that are not renewing
commercial AI contracts. **Effort: 8–10 weeks.**

The proposition is one sentence: *student data never leaves your tenancy.* That is an
architecture claim, so every component must be self-hostable.

| Layer | Component | Licence |
|---|---|---|
| Tutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 |
| Retrieval | https://github.com/HKUDS/LightRAG (inside DeepTutor) | MIT |
| Model serving | https://github.com/ollama/ollama (pilot) → https://github.com/vllm-project/vllm (cohort scale) | MIT / Apache-2.0 |
| Model gateway | https://github.com/BerriAI/litellm | MIT |
| Ingestion | https://github.com/docling-project/docling + https://github.com/SYSTRAN/faster-whisper | MIT / MIT |
| LMS attachment | https://github.com/Cvmcosta/ltijs | Apache-2.0 |
| Telemetry | https://github.com/LearningLocker/learninglocker | GPL-3.0 (self-hosted, so copyleft is contained) |

**Wiring.** Docling parses the institution's course PDFs and faster-whisper transcribes lecture
capture (pull the video from Opencast if the client already runs it); both feed DeepTutor's
LightRAG index. DeepTutor talks to LiteLLM, never directly to a provider — that single seam is
what lets the institution swap to a sovereign or on-prem model later without touching the
application. `ltijs` wraps the tutor as an LTI 1.3 tool so it launches from inside Moodle,
Canvas or Open edX with grade passback, which means **no fork of the AGPL/GPL platform**.
Every learner interaction is emitted as xAPI to Learning Locker so efficacy can be measured
instead of asserted.

**Why this order:** start with Ollama for the pilot, move to vLLM only when a whole cohort hits
the tutor in one lab session. Swapping is a LiteLLM config change.

---

## P2 — AI-assisted grading with a defensible human-review trail

**Sell to:** LATAM first (LGPD already grants automated-decision review rights), then EMEA
ahead of 2 December 2027, then North America. **Effort: 10–12 weeks.**

**Revised in `p872`.** `p871` built this pattern around the absence of a grading component.
That absence is gone: **ArguLens** (`wwrwbs/AI_AWE`, Apache-2.0) is a real, verified, permissive
essay-scoring system whose **scorer is a grade-independent LightGBM model over 31 explicit
linguistic and discourse features — not an LLM.** That property is the entire compliance case,
so the scorer now replaces a prompt at the centre of this recipe.

| Layer | Component | Licence |
|---|---|---|
| **Scoring engine** | https://github.com/wwrwbs/AI_AWE (ArguLens) | **Apache-2.0** |
| Assessment substrate | https://github.com/openedx/edx-ora2 | AGPL-3.0 |
| Orchestration / policy | https://github.com/langchain-ai/langgraph | MIT |
| Model gateway | https://github.com/BerriAI/litellm | MIT |
| Rubric gold sets | https://github.com/HumanSignal/label-studio | Apache-2.0 |
| Teacher-in-the-loop review | https://github.com/argilla-io/argilla | Apache-2.0 |
| Regression / safety gates | https://github.com/promptfoo/promptfoo | MIT |
| Item rendering | https://github.com/Citolab/qti-components | GPL-3.0 |

**Wiring.** `edx-ora2` owns rubrics, submissions and staff grading — it already has the data
model and the UI. LangGraph sits beside it as an explicit graph: *draft score → confidence
check → below-threshold routes to human → human decision recorded → explanation attached to the
submission.* Model calls go through LiteLLM so the provider is auditable and swappable.
Label Studio builds the rubric-scored gold set from the institution's own historical marking;
Argilla is where teachers review and correct model output, and that correction stream is the
retraining signal. promptfoo gates every prompt change against the gold set so a regression
never reaches a learner.

**Where ArguLens goes in the graph.** Its three components are separately replaceable, which is
why it fits here rather than dictating the architecture. The **Qwen2.5-7B LoRA discourse
classifier** labels each sentence `claim`/`data`/`counterclaim`/`rebuttal` — that labelling is
itself the feedback artefact a student can argue with. The **LightGBM scorer** produces the
number, and because it reads 31 measured features it is **reproducible on re-run and inspectable
feature by feature**. The **feedback generator** (local Qwen2.5-14B-Instruct via vLLM) is the only
LLM in the scoring path, and it writes prose rather than deciding grades. Serve the classifier and
the generator through ArguLens's `vllm` backend mode; route the feedback model through LiteLLM via
its `api` backend so the provider stays auditable.

**Two work items that are not optional, priced into the 10–12 weeks.**
1. **Re-fit the scorer on the client's own graded corpus.** ArguLens ships trained on **Persuade
   2.0 — US middle-school argumentative essays**, and its README warns about training-data bias
   and generalisation. For a LATAM engagement this is decisive: **nothing in this system has been
   shown to transfer to Spanish or Portuguese.** Use Label Studio to build the local gold set
   from historical marking, then re-fit. Budget this as a work package, not a tuning step.
2. **Treat it as v0.1.0 software.** Adapter weights ship as a separate release asset and the
   README restricts the tool to "research and assistive" use. Hardening, packaging and an
   upgrade path are Globant's scope. Say so in the proposal — it is a credibility gain, and
   hardening a real Apache-2.0 base is a much cheaper proposition than greenfield.

**The critical design rule:** the model **proposes**, a human **disposes**, and the
disposition is logged with its explanation. That is simultaneously the LGPD Article 20
answer, the EU high-risk human-oversight answer, and the reason a faculty senate will approve
it. Architect it in from day one — it cannot be retrofitted.

**And it now has a third payoff, which is the strongest selling point in this file.** Vietnam's
**Decision 33/2026/QD-TTg** lists AI that conducts exams, assesses learning outcomes or ranks
learners as a high-risk education system — but reporting indicates the listings bite only where
**AI output is the sole basis for a decision without meaningful human review.** A genuine
human-disposition step therefore does not merely satisfy the high-risk obligations; it can keep
the system **out of the high-risk tier altogether**. The same architecture answers three
jurisdictions. (Vietnamese dates and the law's number are unresolved across secondary sources —
see `intel/market.md` gaps — so confirm against primary text before contracting.)

---

## P3 — Multi-agent course generation for a ministry or large programme

**Sell to:** APAC national programmes (the Accenture/Google benchmark), EMEA public sector,
LATAM ministries. **Effort: 6–8 weeks to a working pilot.**

| Layer | Component | Licence |
|---|---|---|
| Course generation | https://github.com/THU-MAIC/OpenMAIC | MIT |
| Courseware target | https://github.com/oppia/oppia | Apache-2.0 |
| Item UI | https://github.com/Khan/perseus | MIT |
| Source ingestion | https://github.com/datalab-to/marker | Apache-2.0 |
| Grounded drafting | https://github.com/stanford-oval/storm | MIT |
| Pedagogical QA | https://github.com/AI-for-Education/pedagogy-benchmark | MIT |

**Wiring.** marker converts the ministry's existing syllabus and textbook PDFs to clean
markdown. OpenMAIC generates the course — AI teacher plus AI classmate agents, project-based
milestones — and exports to PPTX and HTML; STORM drafts grounded explainer material with a
citation trail where the source corpus is thin. Rather than leaving the output in OpenMAIC,
port the validated lessons into **Oppia** explorations, because Oppia's misconception-specific
feedback model is what turns generated content into actual remediation, and it is Apache-2.0.
Render practice items with Perseus.

**The gate that makes this credible:** run `pedagogy-benchmark` against the model you intend
to use *before* generating a national curriculum with it, and publish the CDPK and SEND
scores in the proposal. Everything in this stack is permissive — the whole pattern can be
delivered as a commercial product.

---

## P4 — EU AI Act conformance retrofit (the 2027 clock)

**Sell to:** EMEA. **Effort: 4 weeks for the Article 50 slice; 12–14 weeks for high-risk
readiness.** This is time-boxed work with a date on it, which makes it an easy sale.

| Layer | Component | Licence |
|---|---|---|
| Policy orchestration | https://github.com/langchain-ai/langgraph | MIT |
| Gateway / audit log | https://github.com/BerriAI/litellm | MIT |
| Durable audit trail | https://github.com/temporalio/temporal | MIT |
| Evidence & red-teaming | https://github.com/promptfoo/promptfoo | MIT |
| Local inference (data residency) | https://github.com/ollama/ollama or https://github.com/vllm-project/vllm | MIT / Apache-2.0 |
| Human oversight UI | https://github.com/argilla-io/argilla | Apache-2.0 |

**Wiring, in the order the deadlines fall.**
1. **Already in force — audit and remove.** Article 5(1)(f) has banned emotion inference in
   education since 2 February 2025. Sweep the client's stack for engagement, attention or
   sentiment detection and remove it. This is a finding, not a feature.
2. **Live from 2 August 2026 — Article 50 disclosure.** Every learner-facing chatbot must
   declare it is AI. A LangGraph pre-node that injects and logs the disclosure, plus LiteLLM
   recording that it happened, closes this in weeks.
3. **2 December 2027 — high-risk readiness** for admissions, assessment and proctoring:
   logging, human oversight, accuracy documentation, data governance. Temporal gives a durable
   record of every automated decision and its inputs that survives restarts; Argilla is the
   human-oversight surface; promptfoo produces the accuracy and robustness evidence pack.

**Caveat to state to the client:** `eur-lex.europa.eu` is unreachable from this session, so
confirm Regulation (EU) 2026/1744's education timing against the primary text before signing
to a date.

---

## P5 — Offline-first tutoring for low-connectivity deployment

**Sell to:** LATAM (rural Brazil, Mexico, Andean region), APAC (rural India), ministry equity
programmes. **Effort: 6–8 weeks.** This is where LATAM is genuinely better served by a
different architecture rather than a cheaper version of the online one.

| Layer | Component | Licence |
|---|---|---|
| Learning platform | https://github.com/learningequality/kolibri | MIT |
| Offline server bundle | https://github.com/iiab/iiab | LGPL |
| Offline corpus | https://github.com/kiwix/kiwix-tools | GPL-3.0 |
| Local model | https://github.com/ollama/ollama | MIT |
| Tutor | https://github.com/HKUDS/DeepTutor (ingests Kiwix archives natively) | Apache-2.0 |
| Retention scheduler | https://github.com/open-spaced-repetition/fsrs4anki | MIT |

**Wiring.** Internet-in-a-Box provides the turnkey school server on low-cost hardware; Kolibri
is the learner-facing platform with its own sync model for intermittent connectivity. Kiwix
ZIM archives supply the offline corpus — and **DeepTutor already ingests Kiwix archives**,
which is the connection that makes a genuinely offline tutor possible rather than a degraded
online one. Ollama runs a small quantised model locally. FSRS schedules review so that scarce
device time is spent on what the learner is about to forget.

**Design constraint:** pick the model to fit the hardware first, then design the pedagogy
around its real latency. Everything syncs opportunistically when a link appears; nothing
blocks on the network.

---

## P6 — Institutional AI governance console

**Sell to:** everywhere — this is T3 turned into a product. **Effort: 8–10 weeks.**

Only ~a quarter of faculty report a formal institutional AI policy while ~8 in 10 students use
AI routinely. The gap is the product.

| Layer | Component | Licence |
|---|---|---|
| Gateway, budgets, per-user keys | https://github.com/BerriAI/litellm | MIT |
| Front door for staff & students | https://github.com/danny-avila/LibreChat | MIT |
| Policy graph per jurisdiction | https://github.com/langchain-ai/langgraph | MIT |
| Durable decision log | https://github.com/temporalio/temporal | MIT |
| Learning telemetry | https://github.com/openedx/openedx-aspects | Apache-2.0 |
| Safety regression | https://github.com/promptfoo/promptfoo | MIT |

**Wiring.** LibreChat is the sanctioned front door — self-hosted, multi-model, per-user auth —
which is what converts shadow AI use into governed use. All traffic goes through LiteLLM for
per-department budgets, rate limits and a complete call log. LangGraph holds the policy as
code with jurisdiction-specific nodes: FERPA redaction for North America, Article 50
disclosure for EMEA, content labelling for China, LGPD review rights for Brazil. Temporal
keeps the decision log durable; Aspects reports usage against learning outcomes; promptfoo
runs safeguarding checks on every policy change.

**Why LibreChat and not Open WebUI:** verified this pass, Open WebUI's licence clause 4
prohibits removing its branding above **50 end users per rolling 30 days** without an
enterprise licence. A white-labelled campus deployment would be a material breach. LibreChat
is plain MIT. This is exactly the kind of detail that only reading the licence bytes catches.

---

## P7 — Outcome-validated tutoring deployment (the pattern that survives the evidence)

**Sell to:** every region, and especially any public institution with an access mandate.
**Effort: 12–16 weeks including a measurement window.**

**This pattern exists because of a finding, not a technology.** A 2026 RCT across **2,379
undergraduates** found that access to a course-integrated GenAI tutor **reduced final grades by
0.37 SD** and LMS participation by **0.90 SD**, with **larger losses among first-generation
students**. A separate RCT found AI tutoring **combined with structured group work** produced the
largest gains of any arm. See `intel/trends.md` **T9**.

The conclusion is not "don't deploy tutors". It is that **deploy-and-measure-usage is the arm that
lost**, and it is the default motion of the entire industry. This pattern sells the arm that won.

| Layer | Component | Licence |
|---|---|---|
| Tutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 |
| Pedagogical policy as code | https://github.com/langchain-ai/langgraph | MIT |
| Model gateway | https://github.com/BerriAI/litellm | MIT |
| LMS attachment | https://github.com/Cvmcosta/ltijs | Apache-2.0 (`master`) |
| Interaction telemetry | https://github.com/LearningLocker/learninglocker | GPL-3.0 (self-hosted) |
| Outcome analytics | https://github.com/openedx/openedx-aspects | Apache-2.0 |
| Model pedagogical capability | https://github.com/AI-for-Education/pedagogy-benchmark | MIT |
| Safeguarding gates | https://github.com/promptfoo/promptfoo | MIT |

**Wiring — and the three design decisions that distinguish it.**

1. **Build the measurement before the tutor.** `ltijs` launches the tutor inside the client's
   Moodle/Canvas/Open edX so **section-level assignment is possible** — which is what makes a
   real comparison design available instead of a satisfaction survey. Learning Locker captures
   every interaction as xAPI; Aspects joins it to grades and participation. Stand this up first,
   on the existing course, to get a **baseline**. Without a baseline the 0.37 SD effect is
   undetectable, and a client who cannot detect it is exposed to it.
2. **Encode the pedagogy as refusal, not availability.** The negative trial's mechanism was
   participation collapse — an always-available answer source substituting for effortful work.
   So LangGraph holds an explicit policy graph that **withholds**: hint ladders before answers,
   mastery gates before progression, attempt requirements before explanation, and escalation to a
   human teacher rather than an easier answer. DeepTutor's mastery tracking and learning paths
   supply the state these nodes read. A tutor that will not simply answer is the product.
3. **Pair it with structured human interaction.** The winning arm combined AI with group work.
   So the deliverable includes the **course design** — mandatory structured peer sessions, AI
   use integrated into them rather than offered alongside them. This is instructional-design
   scope, and it is the part a product vendor cannot sell.

**Instrument the equity question explicitly.** Disaggregate outcomes by first-generation status
and any other access category the institution tracks, from the baseline onward. The published
harm was concentrated there; a bid that raises this proactively, with a monitoring plan, wins
against competitors who have not read the literature.

**What the client buys:** not a tutor, but **evidence about their own students** — plus the
tutor. `pedagogy-benchmark` supports the model-selection claim; the trial design supports the
outcome claim. Nobody in this market is selling the second one.

---

## P8 — Vietnam / APAC high-risk de-escalation audit

**Sell to:** APAC, Vietnam first, then South Korea ahead of real enforcement.
**Effort: 4–6 weeks for the audit, then per-system remediation.**

**Vietnam has handed services firms a specification.** Decision **33/2026/QD-TTg** names **46
high-risk AI systems across six sectors**, and **education is one of them** — covering AI that
**conducts examinations, assesses learning outcomes or ranks learners**, and AI that **monitors
and analyses learner behaviour using biometric data or other automated monitoring mechanisms**.

**The leverage:** reporting indicates many listings apply only where **AI output is the sole
basis for a decision without meaningful human review**. So for each system there are two paths —
**de-escalate** it out of the tier by inserting genuine human review, or **conform** and carry the
full obligations. Deciding which, per system, is the engagement.

| Layer | Component | Licence |
|---|---|---|
| System inventory & decision log | https://github.com/temporalio/temporal | MIT |
| Policy-as-code, per jurisdiction | https://github.com/langchain-ai/langgraph | MIT |
| Human-review workflow | https://github.com/openedx/edx-ora2 | AGPL-3.0 |
| Reviewer interface | https://github.com/argilla-io/argilla | Apache-2.0 |
| Explicable scoring (replaces LLM scoring) | https://github.com/wwrwbs/AI_AWE | Apache-2.0 |
| Gateway & call audit | https://github.com/BerriAI/litellm | MIT |
| Evidence & reporting | https://github.com/openedx/openedx-aspects | Apache-2.0 |

**Wiring.** Inventory every education AI system against the three listed education categories.
For each, decide de-escalate or conform. De-escalation is concrete engineering, not paperwork:
route the decision through `edx-ora2`'s human workflow with Argilla as the reviewer surface,
replace LLM scoring with ArguLens's feature-based scorer so the human reviewer has something
inspectable to review, and record every disposition durably in Temporal so "meaningful human
review" is **evidenced** rather than asserted. LangGraph carries the per-jurisdiction policy
nodes, which is what lets the same platform serve Vietnam, Korea, the EU and Brazil — the
human-review requirement is substantially the same shape in all four.

**Biometric monitoring is the one to advise against, not remediate.** Vietnam lists it, and the
EU has **banned emotion inference in education outright since 2 February 2025** (AI Act Art.
5(1)(f)). There is no de-escalation path for a prohibited practice. Recommend removal.

**Pair it with the curriculum mandate.** **MOET Decision 2422** (with Decision 5588) requires
**12 periods per class per year of AI content for grades 1–12** — a nationwide courseware and
teacher-training demand signal, and a second, separately-funded engagement off the same client
relationship. `microsoft/ai-agents-for-beginners` (MIT) and `huggingface/agents-course`
(Apache-2.0) are white-labellable bases for the teacher-facing material.

**Caveat to carry into any proposal:** Vietnam's AI Law number (134/2025/QH15 vs 91/2025/QH15)
and its compliance dates (1 Mar 2027 / 1 Sep 2027 vs 1 Jul 2027 / 1 Jul 2029) **conflict across
secondary law-firm sources**, and this session could read none of the primary texts. Scope a
local-counsel check as the first task of the engagement.

---

## P9 — Spanish-language sovereign tutor on a LATAM-origin base

**Sell to:** LATAM ministries, public universities, rural and regional higher-education
programmes — and any client for whom *"built in the region"* is part of the evaluation.
**Effort: 8–10 weeks** to a pilot, of which **3–4 weeks is completing someone else's backend**.
New in `p873`, and it is the first pattern in this file whose core component is LATAM-origin.

| Layer | Component | Licence |
|---|---|---|
| Tutor backend (base) | https://github.com/LabSirius/TutorIA — **clone `feature/refactor-to-v2-requirements`, NOT `main`** | MIT |
| LMS | https://github.com/openedx/edx-platform | AGPL-3.0 |
| LTI launch (the piece to add) | https://github.com/Cvmcosta/ltijs | Apache-2.0 |
| Local inference | https://github.com/ollama/ollama | MIT |
| Model-swap seam | https://github.com/BerriAI/litellm | MIT |
| Vector store | PostgreSQL + `pgvector` (already wired in TutorIA's `docker-compose.yml`) | PostgreSQL licence / Apache-2.0 |
| Document ingestion | https://github.com/docling-project/docling | MIT |
| Telemetry for outcome measurement | https://github.com/LearningLocker/learninglocker | GPL-3.0 |
| Offline variant | https://github.com/learningequality/kolibri | MIT |

**Why start from TutorIA rather than DeepTutor.** DeepTutor is far more mature and should still be
the default for most builds (see **P1**). Choose TutorIA when the engagement is **Spanish-language,
public-sector and regional**, because three things come with it that maturity cannot buy: a
Colombian public university and a **Minciencias**-funded provenance, a **named pedagogical
director** and teacher-training framework, and a design brief that is already *rural higher
education* rather than a generic tutor localised afterwards. In a ministry evaluation that
provenance is worth more than feature count.

**Wiring, in the order that de-risks fastest.**

1. **Clone the right branch.** `git clone -b feature/refactor-to-v2-requirements
   https://github.com/LabSirius/TutorIA`. **`main` contains documentation only**, and the
   `Sof1SP/tutorIA` address in the README has no code in any branch. Budget a day to confirm what
   you actually have before promising anything.
2. **Stand up the backend as-is.** `docker-compose.yml` brings up `pgvector/pgvector:pg16` plus
   Ollama with an init container. Pull `nomic-embed-text` (**768-dim, matched to
   `content_chunks.embedding`** — a different embedding model means a migration, not a config
   change). Set **`require_embedding_model: true`** in production so a misconfigured RAG stack
   fails at boot instead of silently degrading. Run Alembic; ignore the `create_all` bootstrap the
   code's own `TODO(tech-debt)` tells you to delete.
3. **Seed the pedagogy, don't hard-code it.** Prompt templates live in the database (**RF-21**,
   `python -m app.db.seed prompts`). This is where the client's pedagogical framework — and
   **P7**'s scaffolding, hint ladders and mastery gates — is expressed. Treat it as the main
   configuration surface, co-authored with the client's academics.
4. **Build the three things that are missing.** This is the honest bulk of the work: **(a)** a
   learner-facing frontend — or skip it entirely and go straight to step 5, which is usually
   better; **(b)** a real **LTI 1.3 launch** via `ltijs`, because TutorIA's existing Open edX
   integration is a **data-sync gateway (RF-22) on APScheduler, not a launchable tool**; **(c)** a
   test suite — `pytest` and `pytest-asyncio` are already declared in `requirements.txt` and there
   are no tests.
5. **Prefer LTI-in-platform over a bespoke UI.** It is less work, and it inherits the platform's
   accessibility conformance — see **P10**.
6. **Keep the model seam.** TutorIA defaults to local Ollama (`llama3.2`) through an
   OpenAI-compatible client with a `request_router` (**RF-23**). Put **LiteLLM** behind that seam
   so the same deployment can move to a bigger local model, to **Latam-GPT** weights, or to a
   hosted endpoint on one config change — which is exactly the clause ministries ask for.
7. **Instrument from day one.** Learning Locker captures xAPI so **P7**'s measurement plan has
   data. Do not skip this: the region's measured governance gap is that **9% of institutions
   evaluate their AI implementation at all**, which makes measurement the differentiator.

**Say this plainly to the client, because it converts a risk into a selling point.** TutorIA is an
early-stage backend, not a product; the work is completing a funded public-university project, and
the frontend, LTI plugin and tests are **specified by its own README and absent from its code**.
Contributing those upstream under MIT is a visible, creditable contribution to a national research
programme — a materially better story than a private fork, and one a public client can cite in its
own reporting.

**Licence note.** TutorIA is MIT, so there is no copyleft constraint on your additions. Open edX
is **AGPL-3.0**: integrate over **LTI** rather than forking `edx-platform`, and the obligation
stays on the platform side of the boundary.

---

## P10 — Accessibility-gated public-sector bid

**Sell to:** any public-sector or publicly funded buyer — US federal and state (**Section 508**),
EU and UK public bodies (**EN 301 549**, **European Accessibility Act**, in force since
**28 June 2025**), and any university procurement with a VPAT requirement. **Effort: 4–6 weeks**
as a workstream attached to another pattern, not a standalone build. New in `p873`.

**The problem this pattern exists to solve.** Across this KB's entire agent inventory, **exactly
one education-native agent publishes an accessibility conformance statement**:
`CAHLR/OATutor`. If conformance gates the procurement, a bespoke agent UI means commissioning an
audit and remediating an unknown quantity of findings — on your own budget, before you can bid.

| Layer | Component | Licence | Role in the conformance story |
|---|---|---|---|
| Conformant host UI | https://github.com/moodle/moodle | GPL-3.0 | Moodle core and mobile are **stated** to be WCAG 2.2 AA certified. **Request the VPAT/ACR** — this is a vendor claim this session could not verify |
| Launch mechanism | https://github.com/Cvmcosta/ltijs | Apache-2.0 | LTI 1.3 launch with grade passback; the agent runs as a tool *inside* the conformant UI |
| Agent with its own statement | https://github.com/CAHLR/OATutor | MIT | The fallback when the agent itself must carry conformance: Section 508 / WCAG documented, React, static-deployable |
| Accessible assessment rendering | https://github.com/Citolab/qti-components | GPL-3.0 | QTI 3 standards-compliant item rendering |
| Open-response workflow | https://github.com/openedx/edx-ora2 | AGPL-3.0 | Human-reviewed assessment rather than proctoring (see **P2**, **T8**) |
| Content conversion | https://github.com/docling-project/docling | MIT | Structured extraction — the input side of making generated content accessible |

**Wiring, and the order matters.**

1. **Decide where conformance lives before writing any UI.** Two viable answers: the agent runs
   **inside a platform that already holds a statement** (cheapest, and the default recommendation),
   or you adopt **OATutor**, the one agent carrying its own. A bespoke front end is the third
   answer and it is the expensive one.
2. **Launch over LTI 1.3 with `ltijs`.** Keep every learner-facing surface inside the platform's
   chrome. Use custom UI only for staff-facing surfaces, where the procurement bar is lower.
3. **Treat generated content as in-scope — this is the step everyone skips.** An accessible
   platform routinely serves inaccessible embedded content: the SCORM package, the PDF workbook,
   the generated slide deck. **Anything the agent emits inherits the obligation.** So constrain
   generation: alt text required for every generated image, heading structure enforced in generated
   documents, no colour-only encoding in generated charts, captions and transcripts for any
   narrated output, and reading order asserted in exported PDFs. Make these **template and
   prompt-level constraints** (in P9 that means the seeded prompt templates) and then test the
   output, not the prompt.
4. **Add the WCAG 2.2 criteria that specifically bite learning products**: target size, dragging
   movements, consistent help, accessible authentication — the last one matters because login
   puzzles and cognitive tests are common in exam flows and are now explicitly in scope.
5. **Automate what automation can catch, then stop pretending it is enough.** Wire `axe-core` into
   CI for regressions, and budget a **manual audit with assistive-technology users** for the claim
   itself. Automated tooling catches a minority of real failures; a conformance statement built
   only on it will not survive scrutiny.
6. **Produce the artifact the buyer actually asked for:** a VPAT/ACR covering the deployed
   configuration, with known limitations stated. A statement with honest exceptions wins bids;
   an overclaim fails an audit later, which is worse than losing.

**The regulatory clock, secondary-sourced** (all EU primary sources are unreachable from this
session): the **European Accessibility Act** has applied since **28 June 2025**, and the next
**EN 301 549** revision aligning it to **WCAG 2.2 AA** is reported as due in the Official Journal
in **late 2026**. Treat WCAG 2.2 AA as the target now, not 2.1.

**Pair with:** **P4** in EMEA (the same buyer, the same conformance documentation habit, the same
2027 clock) and **P9** in LATAM, where launching inside Moodle or Open edX removes the frontend
TutorIA does not have — a conformance requirement and a missing UI cancelling each other out.

---

## P11 — EU AI-literacy duty conformance pack (the clock that is already running)

**Sell to:** EMEA — EU schools, school networks, ministries and universities as **deployers**.
**Effort: 6–8 weeks.** **New in `p874`.**

**Why this exists as a separate pattern from P4.** P4 sells against the EU AI Act's education
high-risk tier, which the Digital Omnibus deferred to **2 December 2027**. This one sells against a
duty that **is already binding**: the AI Act's **AI-literacy obligation on deployers**, reported as
applying to institutions from **July 2026**. P4 is a 2027 budget line. **P11 is a 2026 one**, aimed
at the same buyer, producing the same documentation habit, and it is the natural on-ramp to P4.

**The three things that make it closeable** — all newly established in `p874`:

| Element | Value | Use in the pitch |
|---|---|---|
| Measured deficit, **one population, one instrument** | **79%** of European secondary students use AI for schoolwork; **47%** were ever shown how — a **32-point gap**. OpenAI/ThinkYoung, 5,000 students aged 13–19, 10 European countries, fieldwork Apr–May 2026 | The business case. Not a vendor projection — a measurement on the buyer's own population |
| Teacher-side corroboration | **73%** of teachers use AI for planning and materials, **67%** for tests and rubrics (European School Education Platform, Apr 2026) | Staff are already in scope; this is not a future risk |
| **Delivery standard** | **EC/OECD AILit Framework**, 18 June 2026 — **4 dimensions**, **19 competences**, learner expectations, classroom scenarios. Non-binding, product-neutral, developed with CodeAI, feeds **PISA 2029** | The spine. Converts "support AI literacy" into 19 auditable line items |

### Stack — fully permissive, every licence byte-read

| Layer | Component | Licence |
|---|---|---|
| Competence spine | **EC/OECD AILit Framework** — 19 competences, 4 dimensions | Non-binding public framework (not code) |
| LMS launch / transport | https://github.com/Cvmcosta/ltijs — **LTI 1.3 / Advantage**, branch `master` | Apache-2.0 |
| Assessment + feedback core | https://github.com/moocupv/lti-ai-grader — LLM grading, configurable prompts, multi-language templates, Open edX- and Moodle-tested | Apache-2.0 |
| Model vetting evidence | https://github.com/AI-for-Education/pedagogy-benchmark — 1,143 teacher-qualification-exam questions (CDPK 920 / SEND 223) | MIT |
| Telemetry (xAPI/analytics) | https://github.com/openedx/openedx-aspects — reusable outside Open edX | Apache-2.0 |
| **Evidence store** (the attestation record) | 🟢 **This KB's own built component: `compose/code/p292-decision-evidence-store/`** — append-only, tamper-evident, offline, **106 passing controls** | Globant-built |
| Governance register | The institutional console from **P6** | — |

### How to wire it — and the one engineering task that is not optional

1. **Map the 19 AILit competences to the institution's existing curriculum and staff-development
   plan.** Output is a matrix: competence → where it is taught → who is accountable → what evidence
   exists. **This artifact *is* the deliverable** that discharges the literacy duty; the software
   only feeds it.
2. 🔴 **Swap `lti-ai-grader`'s transport. This is the pattern's critical path.** It ships **LTI
   1.1**, which signs with **OAuth 1.0a** and is the **deprecated** generation — 1EdTech has been
   retiring it and many institutions disable it outright. Keep its genuinely reusable parts (the
   grading core, prompt configuration, multi-language templates, and the LMS-tested grade round
   trip); **replace the LTI 1.1 receiver with `ltijs`** for a 1.3/Advantage launch with **AGS**
   grade passback, NRPS rosters and Deep Linking. Budget **1.5–2 weeks**. 🔴 **Do not deliver an
   OAuth 1.0a transport into an engagement that extends past 2027** — the high-risk tier brings
   logging and traceability duties you would then be defending on deprecated plumbing.
3. **Deliver the literacy assessment and formative feedback *inside the LMS*** via the 1.3 launch,
   so students and staff meet it in Moodle, Canvas, Open edX, Blackboard or D2L rather than in a
   new tool nobody adopts. This is also what keeps the build copyleft-safe: you attach over LTI
   rather than forking Moodle (GPL-3.0) or Open edX (AGPL-3.0).
4. **Separate telemetry from attestation — they are two components and conflating them is how a
   literacy claim stops being defensible.**
   - **Telemetry:** completion and interaction events as **xAPI into Aspects**. High-volume,
     mutable, analytical. This is the same spine **P7** needs for outcome measurement — build it
     once.
   - 🟢 **Attestation: the append-only decision record, already built in this KB at
     `compose/code/p292-decision-evidence-store/`** (106 offline controls, tamper-evident, no
     network). A literacy duty is discharged by showing **who was trained on which of the 19
     competences, when, on whose decision, and on what evidence** — that is a *decision record*,
     not an event stream, and a regulator asking the question a year later needs a record that
     cannot have been quietly rewritten. 🔵 **Reuse, do not rebuild:** `p291` costed this component
     as *"the one item a client would pay for"* and it is the second recipe family in this file to
     terminate in it. Run `python3 test_decision_store.py` before shipping.
5. **Run `pedagogy-benchmark` against whichever model backs the tool** and put the score in the
   conformance pack. It is the only published instrument that lets an institution say *why* this
   model is pedagogically fit, and the **SEND** split (223 questions on special educational needs
   and disabilities) answers the access question a public buyer will ask.
6. **Register the deployment in the P6 governance console** — deployer obligations, the literacy
   matrix, the model-vetting score, the incident route — so the 2027 P4 conformance work is an
   extension rather than a restart.

### Why Globant wins this one

The hyperscalers hold the **ministry model contracts** — OpenAI's education partnerships run
through **Estonia** (*AI Leap*, ChatGPT access bundled with teacher training), **Slovakia**,
**Greece** (a May 2026 framework requiring teacher oversight and data protection) and **Italy**, a
deliberately government-first, country-level strategy. **That is precisely why the literacy,
governance and conformance layer is open:** it must be **independent of the model vendor** to be
credible to a regulator, it is **services-shaped** so it cannot be bought as a product, and it is
**product-neutral by design** because AILit itself endorses no products. A competitor reselling a
model contract cannot also be the party certifying that the deployment discharges the buyer's legal
duty.

🔴 **Scoping honesty, to be said in the room.** The **July 2026** start date for the literacy duty
is **secondary-sourced** — no EU primary text is reachable from this KB's session (`eur-lex`,
Council and Parliament hosts are all refused), and **the enforcement mechanics against a school are
unverified and may be weak**. So **do not pitch a sanction on a date.** Pitch the **measured
32-point gap** and the **published framework**, with the legal duty as context. The engagement is
justified by the measurement whether or not a penalty ever materialises — and that is a stronger
position than a compliance threat that a client's own counsel may deflate.

---

## P12 — Hardened multi-agent classroom on OpenMAIC (the one with real adoption)

**Sell to:** APAC national-curriculum programmes, EMEA and LATAM universities needing generated
course material at scale. **Effort: 6–8 weeks.** **New in `p875`.**

**Why this pattern exists.** `p875` measured the shelf (**T12**): **two** open-source education
platforms have real user communities, and OpenMAIC (**43,808 stars, MIT, pushed today**) is the
one built for *course generation* rather than one-to-one tutoring. **Its licence is now settled
beyond argument** — the project relicensed to MIT on **2026-06-28**, which is why its own site and
every pre-July listicle still say AGPL-3.0, and why a pre-relicence AGPL fork (`kolbyzhu5/OpenMAIC`)
circulates in search results. Four channels agree on MIT. **Commercial use is permitted free of
charge by the README's own words.**

| Layer | Component | Licence |
|---|---|---|
| Classroom generation | https://github.com/THU-MAIC/OpenMAIC | **MIT** |
| LMS transport | https://github.com/Cvmcosta/ltijs (LTI 1.3 + AGS passback) | Apache-2.0 |
| Model serving | https://github.com/ollama/ollama → https://github.com/vllm-project/vllm | MIT / Apache-2.0 |
| Model gateway | https://github.com/BerriAI/litellm | MIT (⚠ SPDX `NOASSERTION`) |
| Curriculum spine (optional) | https://github.com/withmarbleapp/os-taxonomy | 🔴 **ODbL-1.0 — database share-alike** |
| Ingestion | https://github.com/docling-project/docling | MIT |

### 🔴 The hardening task that makes this a pattern rather than a demo

OpenMAIC's own README states that site-wide access is gated by a single `ACCESS_CODE` variable and
that **unset is the default in `.env.example`**:

> *"When it is unset… `middleware.ts` checks no credential and every route, the API included, is
> reachable: an unconfigured deployment is not gated, and there is no second enforcement point."*

**A default OpenMAIC deployment in a school tenancy is a student-data exposure on day one.** Rate
limiting only engages behind a trusted proxy with `TRUST_PROXY_HEADERS=true`. Budget these as named
line items, not as "hardening":

1. **Provision `ACCESS_CODE`** from a secret manager; fail the deploy if unset (CI gate, not a
   runbook note).
2. **Add the second enforcement point OpenMAIC does not have** — put `ltijs` in front so the only
   path in is an authenticated **LTI 1.3 launch from the institution's LMS**, and bind the app to
   a private network so the API is not routable from the public internet.
3. **Set `TRUST_PROXY_HEADERS=true` behind the institution's reverse proxy** so rate limiting is
   actually active.
4. **Pen-test the API surface specifically**, not just the UI — the README is explicit that the API
   shares the single gate.

🔵 **Why this sells.** Every competitor demoing OpenMAIC is demoing the default configuration. **An
engagement that opens by naming this defect, with the vendor's own README as the citation, is
immediately credible** — and the fix is four tasks, not a rebuild.

🟡 **Scope honestly:** if the client plans to publish an extended curriculum database derived from
`os-taxonomy`, the **ODbL share-alike obligation attaches to that database**. Either keep
client-specific curriculum in a separate store you do not redistribute, or budget the obligation.
It is not an MIT-class component and must not be presented as one.

---

## P13 — US district AI-policy conformance, sold against a published calendar

**Sell to:** North America K-12 districts and state education agencies. **Effort: 4–6 weeks per
district, 10–12 weeks for a state model policy.** **New in `p875`.**

**Why this pattern exists.** `p875` found that the US state layer has moved from advisory guidance
to **dated mandates** (`intel/market.md`, North America). That converts an open-ended "AI strategy"
conversation into a procurement calendar with named deadlines:

| Jurisdiction | Obligation | Date |
|---|---|---|
| **Ohio** | District AI policy required | **1 Jul 2026 — already passed** |
| **North Carolina** | State model policy | **31 Dec 2026** |
| **North Carolina** | Local district policies | **30 Jun 2027** |
| **North Carolina** | Teacher training | **30 Jun 2028** |
| **Maryland** | 24 districts adopt aligned policy | **120 days** from state guidance |
| **Idaho** | Local boards set policy | **before the 2027–28 school year** |

🔵 **Ohio's passed deadline is the warmest lead in this file.** A cohort of districts is either in
breach or has adopted school-boards-association template language nobody has mapped to their actual
deployed tools. **The first deliverable is an inventory, and almost nobody has one.**

**The build.** This is a governance engagement with a small software spine — reuse **P6**'s console:

| Layer | Component | Licence |
|---|---|---|
| Governance console / inventory register | **P6** stack — https://github.com/appsmithorg/appsmith | Apache-2.0 |
| Policy-to-tool mapping store | https://github.com/qdrant/qdrant | Apache-2.0 |
| Data-boundary enforcement for any AI in scope | https://github.com/BerriAI/litellm (self-hosted gateway, logging off by default) | MIT |
| Evidence of student-data handling | district SIS + https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | Apache-2.0 |

**Deliverables, in the order a district needs them:** (1) inventory of every AI tool actually in
use, including the ones teachers adopted without procurement; (2) mapping of each to the state's
required policy clauses; (3) a data-boundary architecture showing where student records go;
(4) board-ready policy text; (5) the teacher-training plan the 2028 clause will require.

### 🔴 Sell this in BOTH directions or lose half the market

The regulatory current is not uniformly pro-adoption. **New York** has a proposal to limit
classroom AI below ninth grade; **California AB 1159** bars using student data to train AI models;
**New Mexico** let districts opt out of a state-mandated AI reading tool after privacy backlash.
🟡 **Restriction compliance is the same engagement with the same artifacts** — inventory, mapping,
data boundaries, board text. **A North America offer that only works if the client is expanding AI
use will be unsellable in a growing list of states.** Pitch it as *"know what you are running and
prove it meets your state's rule"*, which is true whichever way the rule points.

🟡 **Source caveat to carry internally:** the state counts (~33–35 states with guidance; 134 bills
across 31 states) come from trackers, several vendor- or advocacy-run, that disagree at the
margins. **The dates above recur consistently across sources; the counts are directional. No
primary statute was readable from this session** — confirm the specific statute before a district
signs.

---

## Pattern selection by region

| Region | Lead with | Because |
|---|---|---|
| North America | 🟢 **`p875`: lead with P13** — Ohio's district-policy deadline passed 1 Jul 2026, North Carolina's state model policy is due 31 Dec 2026 and local policies 30 Jun 2027, Maryland runs a 120-day clock and Idaho's boards must act before the 2027–28 school year. Sell against the calendar, and sell restriction-compliance too (NY sub-grade-9 proposal, CA AB 1159). Then: P1, then P6, then P7 | FERPA plus 134 bills in 31 states; MD/ID/OK/VA mandate district policy and NC's model-policy deadline is **31 Dec 2026**. Only **32%** of administrators report an institution-wide policy and **87%** of faculty wrote their own — P6 consolidates that. P7 matters because the published harm fell hardest on first-generation students, which every access-mandated institution must answer. |
| EMEA | 🟢 **P11 first**, then P4, then **P10**, then P1 | 🟢 **`p874` reorders this row: lead with P11.** The AI-literacy duty on deployers 🔴 **has applied since 2 February 2025 (`p875` correction — `p874` said July 2026)**, and **Article 50 transparency for chatbots and generated content went live 2 August 2026**, so TWO duties are already in breach today while the high-risk tier is deferred to **2 Dec 2027** — so P11 is the engagement with a *live* duty, a **measured 32-point deficit** (79% of European students use AI, 47% were shown how) and a **published standard** (EC/OECD AILit, 19 competences). It is also the on-ramp to P4 for the same buyer. Then: Article 50 disclosure is live (2 Aug 2026), the education high-risk tier lands 2 Dec 2027, and institutions are declining to renew commercial AI contracts. **P10** because the European Accessibility Act is already in force and EN 301 549 is realigning to WCAG 2.2 AA — and only one agent in this KB carries a conformance statement. For Gulf engagements, KHDA has already published school-level guidance, so lead with compliance implementation rather than policy authorship. For African engagements, the integration surfaces are Chamilo and Kolibri (**P5**), and regional code is largely unlicensed (**T10**) — so lead with licensing and partnership, not a fork. |
| APAC | **P8**, then P3, then **P12** | 🟢 **`p874` puts a dated deadline behind this row.** Vietnam's **Law No. 134/2025/QH15** has been in force since **1 Mar 2026** and existing **education** systems must comply by **1 September 2027** — **three months before the EU's 2 Dec 2027**, making it the nearest hard deadline in education AI. **Decision 33/2026/QD-TTg** (46 high-risk systems, effective 15 Aug 2026) is a published specification with a human-review carve-out, and **MOET Decision 2422** mandates 12 periods of AI content per class per year for grades 1–12. South Korea's AI Basic Act has been in force since 22 Jan 2026. P3 for national-programme scale. |
| LATAM | **P9**, then P2 and P5, then P7, then **P12** | **P9** is new and leads now: TutorIA is MIT, Colombian, Spanish-language, rural-first and ministry-funded — the only LATAM-origin base this KB has verified, and provenance counts in a public evaluation. LGPD automated-decision review is already binding. **87%** of institutions use AI, **26%** have a strategy and **9%** evaluate — so P7's measurement layer is the gap, and P2 must budget re-fitting ArguLens for Spanish and Portuguese. |
| Global | P6, then P7 | The governance gap is universal (only **31%** of faculty are meaningfully involved in AI policy) and nobody is measuring outcomes. |

**If you read only one line of this file:** the two patterns no competitor is selling are **P7**
(outcome evidence about the client's own students) and **P8** (de-escalating out of a statutory
high-risk tier by design). Both are services-shaped, both are defensible with citations, and
neither can be bought as a product. **`p873` adds a third candidate: P9** — not because the
technology is novel, but because *"we are completing a Colombian public university's MIT-licensed
tutor and contributing it back"* is a position a competitor reselling a US product cannot occupy
at any price.
