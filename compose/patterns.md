---
industry: education
region: Global
updated: 2026-10-17
---

# Compose patterns — Education

> Concrete recipes: named repos, named licences, named wiring. Every component below was
> licence-verified from payload on 2026-10-17
> ([evidence](../evidence/verified-repos.2026-10-17-p264.tsv)).
> Each pattern states the licence boundary — the line the client's proprietary code must stay
> on to keep a copyleft platform from colouring the deliverable.

## P1 — Teacher co-pilot for a national AI-literacy mandate
**Target:** India (Class 3 mandate, AY 2026-27), Mexico (SEP teacher formation), Brazil (MEC basic-education guidance)
**Timeline:** 8–10 weeks to a measurable pilot

```
[instructional_agents  MIT]   multi-agent ADDIE: syllabus -> LaTeX slides -> assessments
        |                      roles: Teaching Faculty / Instructional Designer / TA / Coordinator
        v
[Claw-ED  MIT]                teacher edits and approves before anything reaches a student
        |                      (local-first: curriculum never leaves the institution)
        v
[lineage-skill  Apache-2.0]   every generated artefact stays tied to its source document
        |
        v
[Moodle  GPL-3.0]  <--LTI--  [tsugi  Apache-2.0]      delivery into the installed base
        |
        v
[pykt-toolkit  MIT]           did the teacher formation move learner outcomes?
```

**Wiring:** run `instructional_agents` in its Feedback-Guided mode so a human is in the loop
by construction, not by policy. Deliver through `tsugi` as an LTI 1.3 tool — the agent code
stays MIT/Apache-2.0 and never links against Moodle's GPL.
**Licence boundary:** LTI launch. Everything studio-built sits on the permissive side.
**Why it sells:** three governments are funding exactly this, and
[`intel/market.md`](../intel/market.md) shows Mexico's gap quantified at 76%-vs-36%.

## P2 — Compliant tutoring for the EU AI Act window
**Target:** EMEA higher education and vocational training
**Timeline:** 10–12 weeks; must land before **2027-12-02**

```
[DeepTutor  Apache-2.0]              persistent student model, multi-agent tutoring
        |
        +-- served by --> [Ollama / vLLM, self-hosted]   no prompt leaves the member state
        |
        v
[OpenOLAT  Apache-2.0]  or  [Artemis  MIT]   EMEA-origin, permissive platform
        |
        v
[lrsql  Apache-2.0]  +  [xAPI-Spec  Apache-2.0]   auditable record of every AI interaction
        |
        v
[Moodle 5.1 per-course/per-activity AI toggles]   where Moodle is the installed base
```

**Wiring:** two obligations, two mechanisms. **Transparency (live since 2026-08-02):** an
explicit AI-disclosure interstitial on every `DeepTutor` session entry, logged as an xAPI
statement into `lrsql` so disclosure is provable, not asserted. **High-risk (from
2027-12-02):** any function that determines access, assesses outcomes or influences an
educational path routes through a human-decision step — `DeepTutor` proposes, a named
educator disposes, and `lrsql` holds both records.
**Licence boundary:** the whole stack is Apache-2.0/MIT. Deliberate: an AI Act technical
file is easier to assemble when no component carries network copyleft.
**Why it sells:** the delay created a 14-month window and most clients will read it as a reprieve.

## P3 — Dropout early-warning for a LATAM public university
**Target:** Brazil, Mexico, Colombia, Argentina — Moodle/Chamilo installed base
**Timeline:** 6–8 weeks

```
[Moodle  GPL-3.0]  /  [Chamilo  GPL-3.0]        activity logs, grades, submissions
[academico  MIT]  /  [GibbonEdu  GPL-3.0]       enrolment, attendance, demographics
        |
        v
[lrsql  Apache-2.0]                             one event stream, xAPI vocabulary
        |
        v
[pyedmine  MIT]  or  [pykt-toolkit  MIT]        knowledge tracing + cognitive diagnosis
        |                                        [EduData  Apache-2.0] for baselining
        v
[risk scores + next-best-action]
        |
        v
[Moodle block via tsugi  Apache-2.0]            advisor dashboard, inside the LMS they use
```

**Wiring:** pull through Moodle's REST API into `lrsql` — never read the LMS database
directly, or the integration dies at the next platform upgrade. Train with `pykt-toolkit`'s
standard splits so the accuracy claim is comparable to published baselines instead of
self-graded. Use `pyedmine` when the client wants a recommendation, not just a prediction.
**Licence boundary:** REST + LTI. No studio code links to GPL internals.
**Why it sells:** Brazil's digital-sovereignty framing makes self-hosted inference the
policy-preferred architecture, not the budget option.

## P4 — Education skill pack for a client's existing assistant
**Target:** any region; clients who already run an AI assistant
**Timeline:** 3–4 weeks

```
[Bloom  MIT]                             adaptive tutoring skill
[universal-diagnostic-tutor-skill  MIT]  diagnose the misconception first
[universal-examprep-skill  MIT]          teach from the client's own slides, page-cited
[anki-mcp-server  MIT]                   spaced repetition behind MCP
[tutor-mcp  MIT]                         tutoring loop behind MCP
        |
        v
[client's assistant]  -- MCP -->  [institutional content + Anki decks]
```

**Wiring:** ship skills, not an application. The MCP servers expose the institution's
content and the learner's review schedule; the skills carry the pedagogy. `fsrs4anki` (MIT)
or `fsrs-rs` (BSD-3-Clause) supplies the scheduler so retention is managed by a real
algorithm rather than a prompt.
**Licence boundary:** every component MIT or BSD-3. Nothing to negotiate.
**Why it sells:** this is **T2** in [`intel/trends.md`](../intel/trends.md) — the fastest-moving
shape in education open source, and the cheapest engagement to start.
**Avoid:** `education-agent-skills` (873 stars) is **CC-BY-SA-4.0**. Superb reference,
ShareAlike on derivatives — read it, do not vendor it into a proprietary pack.

## P5 — Integrity-first assessment where student-facing AI is restricted
**Target:** US states barring AI from high-stakes decisions (OK, MD), NYC K-8 moratorium districts
**Timeline:** 6–8 weeks

```
[Artemis  MIT]              programming/modelling/text exercises, automated FEEDBACK
        |                    (feedback, explicitly not autonomous grading)
        v
[dolos  MIT]                source-code plagiarism detection across submissions
        |
        v
[Numbas  Apache-2.0]        randomised maths assessment; SCORM-packaged output
        |
        v
[scorm-again  MIT]          runs that SCORM inside the institution's existing LMS
        |
        v
[teacher sign-off]  ------>  grade of record
```

**Wiring:** the architecture encodes the regulation. No AI output becomes a grade without a
named educator's action; `Artemis` produces feedback and evidence, the teacher produces the
grade. `Numbas` randomisation means per-student variants, which is integrity by design
rather than detection after the fact.
**Licence boundary:** fully permissive, and `scorm-again` keeps legacy content in place —
no content migration in the SOW.
**Why it sells:** in restricted jurisdictions this is the AI story that is unambiguously
permitted (see **T8**).

## P6 — AI-native corporate L&D, no LMS legacy
**Target:** enterprise L&D, North America and EMEA
**Timeline:** 5–7 weeks

```
[mentingo  MIT]                      AI-native LMS: AI mentor w/ voice role-play + auto-scoring,
        |                             AI course builder (policy docs -> structured courses),
        |                             open-ended answer grading, bring-your-own-key
        +-- traces --> [Langfuse]     cost, latency and mentor output, per call
        +-- exposes --> [MCP]         the client's assistant can drive the LMS
        |
        v
[fsrs4anki  MIT]                     spaced repetition for compliance-knowledge retention
        |
        v
[lrsql  Apache-2.0]  + [xAPI-Spec]   completion and competency evidence for audit
```

**Wiring:** feed existing policy and knowledge-base documents into the AI course builder,
then use role-play scenarios for compliance and sales enablement with auto-scoring as
formative — never summative — signal. Langfuse tracing gives the client per-call cost
visibility from day one, which is usually the first question procurement asks in month two.
**Licence boundary:** MIT throughout.
**Why it sells:** retrofitting Moodle for corporate L&D costs more than starting on a base
that already has the agent, the tracing and the MCP endpoint.

## P7 — Sovereign tutoring deployment, air-gapped
**Target:** Brazil (MEC digital sovereignty), EMEA public sector, defence/government training
**Timeline:** 8–10 weeks

```
[Open TutorAI CE  BSD-3-Clause]      multimodal tutoring: voice, video, 3D avatars, Docker-first
        |
        +-- inference --> [Ollama / vLLM on-premise]    no external API
        v
[OpenOLAT  Apache-2.0]               Apache-2.0 LMS: no copyleft anywhere in the stack
        |
        v
[lrsql  Apache-2.0]                  all records on-premise
```

**Wiring:** every component runs inside the perimeter and the entire stack is
permissive — which matters when a government client wants to audit, modify and redistribute
internally without GPL obligations following the artefact. Open TutorAI's avatar and voice
layer is the differentiator where face-to-face interaction is culturally expected.
**Licence boundary:** none to manage. That is the point of this pattern.
**Why it sells:** Brazil's MEC *Referencial* asks for national solutions reducing dependence
on global platforms. This is that, literally.

## Component quick reference

| Need | Component | Licence |
|------|-----------|---------|
| Tutoring agent | `HKUDS/DeepTutor` | Apache-2.0 |
| Course material generation | `DaRL-GenAI/instructional_agents` | MIT |
| Human-reviewed lesson drafting | `SirhanMacx/Claw-ED` | MIT |
| Source provenance for generated content | `JuneYaooo/lineage-skill` | Apache-2.0 |
| Automated assessment + feedback | `ls1intum/Artemis` | MIT |
| Maths e-assessment | `numbas/Numbas` | Apache-2.0 |
| Code plagiarism detection | `dodona-edu/dolos` | MIT |
| Knowledge tracing | `pykt-team/pykt-toolkit` | MIT |
| Tracing + diagnosis + recommendation | `ZhijieXiong/pyedmine` | MIT |
| Education datasets | `bigdata-ustc/EduData` | Apache-2.0 |
| Spaced repetition scheduler | `open-spaced-repetition/fsrs4anki` · `fsrs-rs` | MIT · BSD-3 |
| LTI tool framework | `tsugiproject/tsugi` · `pylti1.3` | Apache-2.0 · MIT |
| Learning record store | `yetanalytics/lrsql` + `adlnet/xAPI-Spec` | Apache-2.0 |
| SCORM runtime | `jcputney/scorm-again` | MIT |
| Permissive LMS | `OpenOLAT/OpenOLAT` | Apache-2.0 |
| AI-native LMS | `Selleo/mentingo` | MIT |
| Multimodal tutoring platform | `Open-TutorAi/open-tutor-ai-CE` | BSD-3-Clause |
| MCP: spaced repetition · tutoring | `ankimcp/anki-mcp-server` · `tutor-mcp` | MIT |

**Do not compose:** `CaviraOSS/PageLM` (non-commercial, redistribution prohibited),
`GarethManning/education-agent-skills` (CC-BY-SA-4.0 ShareAlike),
`GeminiLight/awesome-ai-llm4education` (no licence served),
`human-skill-tree` / `freelingo` / `lumen` (AGPL/GPL — network copyleft on hosted delivery).

## Declared gaps

- **No pattern for autonomous grading.** No open-source grading agent with meaningful
  adoption was found, and the three largest regulated markets (US states, EU, Brazil) are all
  moving to require human decision-makers. The absence is deliberate.
- **No APAC-origin component** appears in any pattern above, because none surfaced this pass.
  P1 serves APAC's largest mandate with non-APAC components; that is the honest state of the
  shelf, not a preference.
