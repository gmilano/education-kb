---
industry: education
region: Global
updated: 2026-11-17
---

# Compose patterns — education

**Pass `p871`, 2026-11-17.** Six recipes. Every repo named below was verified this pass
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

There is no mature open-source grading agent — verified this pass. So do not promise one.
Build assistance plus a review trail on a battle-tested assessment substrate.

| Layer | Component | Licence |
|---|---|---|
| Assessment substrate | https://github.com/edx/edx-ora2 | AGPL-3.0 |
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

**The critical design rule:** the model **proposes**, a human **disposes**, and the
disposition is logged with its explanation. That is simultaneously the LGPD Article 20
answer, the EU high-risk human-oversight answer, and the reason a faculty senate will approve
it. Architect it in from day one — it cannot be retrofitted.

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

## Pattern selection by region

| Region | Lead with | Because |
|---|---|---|
| North America | P1, then P6 | FERPA plus 134 state bills; grant funding now weights AI |
| EMEA | P4, then P1 | Article 50 is live, 2027 is coming, institutions are not renewing commercial contracts |
| APAC | P3, then P6 | National-programme scale; five divergent regulatory regimes |
| LATAM | P2 and P5 | LGPD review rights are already binding; connectivity and equity mandates |
| Global | P6 | The governance gap is universal |
