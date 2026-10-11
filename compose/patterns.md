---
industry: education
region: Global
updated: 2026-10-11
---

# Education — compose patterns

**Pass 130, 2026-10-11.** Full rewrite. Six recipes. Each names the actual repos, the licence
posture of the result, how the pieces wire together, and what it does not solve. Every repo cited
is verified in `evidence/verified-repos.2026-10-11.tsv`.

---

## P1 — Auditable AI tutor on an existing LMS *(the default engagement)*

**For:** an institution whose students already use AI and whose board now wants control.
**Timeline:** 8–10 weeks to pilot.

**Stack**

| layer | component | licence |
|---|---|---|
| tutoring engine | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 |
| mastery + decision audit | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| LMS connector | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (Canvas) | MIT |
| launch into LMS | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) (LTI 1.3) | MIT |
| mastery reference model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (BKT) | MIT |

**Wiring.** The agent runs *outside* the LMS and is launched via LTI 1.3, so no platform source is
touched and **no AGPL reciprocity is triggered** — this is the point of the pattern. `canvas-mcp`
gives the agent tools over courses, assignments, submissions and rubrics. `tutor-mcp` holds the
state DeepTutor lacks: per-learner BKT mastery, review scheduling, misconception records, and an
append-only log of *why* each pedagogical decision was made. Grades return to the LMS through LTI
grade passback, never by the agent writing directly to the gradebook.

**Why the audit log is the deliverable.** T1/T2 in `intel/trends.md`: the client's problem is
defensibility. "The agent recommended this exercise because mastery of skill S was estimated at
0.42" is reviewable by a human; "the model suggested it" is not.

**Result licence:** fully permissive (Apache-2.0 + MIT). Shippable as a closed derivative.

**Does not solve:** whether learning improves (see P6). Canvas-specific — for Moodle, swap the
connector for a GPL-3.0 plugin or `onbirdev/moodle-webservice_mcp` (**unlicensed — clear first**).

---

## P2 — Offline-first tutor for low-connectivity deployments *(the unclaimed slot)*

**For:** rural LATAM, Sub-Saharan Africa, South Asia; ministries and NGOs.
**Timeline:** 10–12 weeks.

**Stack**

| layer | component | licence |
|---|---|---|
| platform | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | MIT |
| content pipeline | [`learningequality/studio`](https://github.com/learningequality/studio) | MIT |
| local inference | a small open-weights model served on-device | model-dependent |
| mastery state | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| interactive content | [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | MIT |

**Wiring.** Kolibri already solves content distribution without connectivity (LAN or USB sync).
Add a locally served small model and `tutor-mcp` keeping learner state in Kolibri's own store, so
the tutor works with the network off and syncs mastery when a link appears. Author activities as
H5P so the same content renders if the institution later moves to Moodle or Open edX.

**Why this is strategically the best pattern in the KB.** MIT top to bottom, no incumbent (no AI
project on Kolibri was found this pass), and **data never leaves the device** — which discharges
most of the privacy obligation in US state law, the EU AI Act and Brazil's pending PL 2338 by
construction rather than by policy. The regulatory tailwind and the engineering choice point the
same way.

**Result licence:** MIT throughout.

**Does not solve:** small-model quality is the binding constraint; scope to one subject and
validate before widening. Requires device-management capability the client may not have.

---

## P3 — Policy-to-implementation compliance layer *(North America, hard deadlines)*

**For:** a US district or university facing a mandate — e.g. **Ohio's 1 July 2026 policy
requirement**, California AB 1159's ban on training with student data, Oklahoma/Maryland human-
oversight rules.
**Timeline:** 6–8 weeks.

**Stack**

| layer | component | licence |
|---|---|---|
| tool inventory | LMS connectors as discovery instruments: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp), [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | MIT |
| decision log | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| sandboxing | [`openedx/codejail`](https://github.com/openedx/codejail) | Apache-2.0 |
| no-source-touch integration | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | MIT |

**Wiring.** Three artefacts, in order. **(1) Inventory:** enumerate via the LMS API every external
tool, LTI registration and integration touching student data — most institutions cannot currently
produce this list. **(2) Routing with proof:** put every model call behind one gateway that records
destination, payload class and retention terms, so "no student data reached a training endpoint" is
a query result, not an assurance. **(3) Gates:** any high-stakes output — grades, placement,
discipline, admissions — is advisory only and requires recorded human approval, satisfying
Oklahoma/Maryland-style rules and aligning with the EU's eventual Annex III duties.

`codejail` sandboxes learner- or model-generated code if the engagement includes auto-grading for
programming courses.

**Result licence:** permissive.

**Does not solve:** the policy text itself (that is counsel's work). This builds the technical means
to comply with it and the evidence of compliance.

---

## P4 — EMEA conformity-by-design build *(before December 2027)*

**For:** an EU institution that will fall under Annex III when high-risk duties apply.
**Timeline:** 10–12 weeks.

**Stack**

| layer | component | licence |
|---|---|---|
| platform | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) or [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) or Moodle | GPL-3.0 |
| public portal | [`openfun/richie`](https://github.com/openfun/richie) | MIT |
| step-level feedback | [`ideas-edu/ideas`](https://github.com/ideas-edu/ideas) | Apache-2.0 |
| mastery audit | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| integration | LTI 1.3 via [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | MIT |

**Wiring.** Build to the obligations **already in force**, not the postponed ones: Article 4 AI
literacy (since February 2025) and the **prohibition on emotion recognition in education** (since
2 February 2025). Architecturally: no affect/emotion inference anywhere in the system — products
built for other markets ship it and it is illegal here; grading and admissions remain human
decisions with the agent advisory only, which keeps the deployment out of the heaviest Annex III
duties by design; `ideas-edu/ideas` provides deterministic, domain-reasoned step-level feedback for
maths and logic, which is defensible to a regulator in a way LLM free-text is not; Richie (MIT,
proven at French national scale) fronts it.

**Why ILIAS/Chamilo rather than Canvas.** EMEA procurement runs on these, scores standards and
accessibility compliance in tenders, and neither has any AI-on-top — an open field.

**Watch:** Council adoption of the Digital Omnibus. If it fails, the original high-risk dates snap
back and this timeline compresses hard.

**Does not solve:** no open-source proctoring or academic-integrity system exists, and proctoring is
squarely Annex III. Do not promise it.

---

## P5 — Teacher-capacity tooling at national scale *(APAC mandates)*

**For:** ministries and large private networks facing curriculum mandates — **India from Class 3 in
2026-27**, China from age six.
**Timeline:** 8–10 weeks to a usable generator; longer to scale.

**Stack**

| layer | component | licence |
|---|---|---|
| content generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | MIT |
| pedagogy/skill library | [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | **NOASSERTION — review first** |
| interactive output | [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | MIT |
| platform | [`frappe/lms`](https://github.com/frappe/lms) or Moodle | AGPL-3.0 / GPL-3.0 |
| delivery at scale | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) where connectivity is poor | MIT |

**Wiring.** The bottleneck in a national mandate is teachers, not students: curriculum, lesson
plans, question banks and assessments in volume, in local languages. `educhain` generates the
artefacts; the skills library supplies pedagogical structure; output is authored as **H5P** so it
renders on whatever platform each state or network runs. Human review stays in the loop per
artefact — content entering a national curriculum needs a named approver, and India's AI-content
labelling rules apply to generated material.

**Licence caution, twice.** `educhain` publishes **no GitHub releases** and its README's version
history stops at **v0.3.13 (October 2024)** — pin a commit and expect to maintain it.
`education-agent-skills` reads as **NOASSERTION**: read the terms before any client reuse.

**Does not solve:** teacher training itself. ~a quarter to a third of the APAC public wants AI out
of classrooms (Ipsos 2026), so adoption is a change-management problem, not a software one.

---

## P6 — Learning-outcome evaluation harness *(the missing instrument)*

**For:** any client who will be asked "did it work?" — and the differentiator none of them can
currently buy.
**Timeline:** 4–6 weeks, runs alongside P1–P5.

**Stack**

| layer | component | licence |
|---|---|---|
| mastery ground truth | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (BKT) | MIT |
| decision + mastery log | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| structured lesson model | [`oppia/oppia`](https://github.com/oppia/oppia) | Apache-2.0 |
| interaction telemetry | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (xAPI) | MIT |
| multi-agent baseline | [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | CC0-1.0 |

**Wiring.** No open-source harness measures whether agentic tutoring improves learning (T7), so
build the measurement as a deliverable. BKT parameters from `OATutor` give a quantitative,
inspectable mastery estimate independent of the tutor's self-assessment; `tutor-mcp` logs every
decision with the mastery state that produced it; xAPI via `scorm-again` captures interaction
telemetry from existing courseware so a pre-intervention baseline exists; Oppia's lesson model
encodes misconceptions explicitly, giving labelled targets to measure against. Run a holdout: same
content, tutor on and off, compare mastery trajectories and retention at a fixed interval.

**Why it closes every other pattern.** The OECD's 2026 Outlook asks for **durable learning gains**;
US state mandates ask for evidence that high-stakes decisions were sound; EU Annex III will ask for
documented performance. One harness answers the pedagogical question and three regulatory ones.

**Does not solve:** it measures, it does not teach. And it needs a holdout design the institution
must agree to — negotiate that at contract time, not at delivery.

---

## Pattern selection, one line each

| if the client… | run |
|---|---|
| already runs Canvas/Moodle and wants control | **P1** |
| serves low-connectivity learners | **P2** |
| faces a US state mandate with a date | **P3** |
| is an EU institution touching admissions/grading | **P4** |
| is a ministry facing a curriculum mandate | **P5** |
| will be asked whether it worked | **P6** — always, alongside the others |

**Cross-cutting constraints.** Prefer **LTI 1.3** over forking any AGPL platform. Never ship
emotion recognition into an EU deployment. Treat `NOASSERTION`/unlicensed components as unusable
until counsel clears them, however many stars they have. Pin commits for repos with no releases.
