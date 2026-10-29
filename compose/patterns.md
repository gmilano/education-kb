---
industry: education
region: Global
updated: 2026-10-29
---

# Compose Patterns — Education

**Pass `p526` · 2026-10-29.** Six recipes. Every component named below was read
from its repository page during this pass, and every licence stated is the licence
served on 2026-10-29. No recipe uses a component this base has not verified.

**The licence rule that shapes all six:** the mainstream LMS cores are copyleft
(Moodle GPL-3.0, Open edX / Canvas AGPL-3.0). Agents stay **permissive and
out-of-process**, talking over MCP, LTI 1.3, REST or xAPI. Where a recipe forks,
it forks a permissive core.

---

## P547 — Canvas-attached teacher copilot (North America)

**Brief.** A district or university on Canvas wants lesson prep, feedback drafting
and routine answers, without touching grades and without forking an AGPL core.

| Role | Component | Licence |
|---|---|---|
| LMS (not forked) | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 · 6.9k★ |
| Integration seam | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** · 308★ · v1.16.0 |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | **MIT** · 387★ |
| Portable output | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 152★ |
| Acceptability gate | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) rubrics | **Apache-2.0** · 601★ |
| Event records | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |

**Wiring.** `canvas-mcp` runs as a separate process and is the *only* thing that
touches Canvas — this is what keeps AGPL-3.0 §13 away from your code. The copilot
calls it for roster, assignment and submission context; Educhain generates items;
output is emitted as **H5P** so it survives a future platform migration; every
interaction is written to Ralph as xAPI. The k12 rubrics run in CI against a fixed
set of teacher prompts, and a regression there fails the build.

**Hard constraint — build it in, not in the policy doc.** Oklahoma bars AI as the
primary basis for grading, discipline or placement, and Maryland, Idaho, Oklahoma
and Virginia require district-level AI policies in 2026. The grading path must be
**structurally** human-decided: the agent may draft, a human must commit, and the
xAPI record must name who committed. "We have a policy" is not the deliverable;
"the model cannot do it" is.

**Effort.** 6-8 weeks. Weeks 1-2 MCP deployment and auth; 3-5 generation + H5P
emission; 6 rubric CI; 7-8 audit trail and district pilot.

---

## P548 — EU AI Act conformity scaffolding for an education product (EMEA)

**Brief.** A European edtech vendor or ministry needs its grading / admissions /
proctoring AI ready for **2 December 2027**, with the obligations that are already
live satisfied now.

| Role | Component | Licence |
|---|---|---|
| Permissive LMS core (forkable) | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** · 449★ |
| Governance-provenance alternative | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 · 505★ |
| xAPI record store (the audit substrate) | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |
| Integrity, explainable | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** · 355★ |
| Pedagogy evidence | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** · 13★ |

**Wiring.** Fork OpenOLAT (Apache-2.0 — proprietary extensions are fine). Ralph is
not analytics here, it is the **conformity artefact**: logging and traceability are
Annex IV obligations, and an xAPI store gives them in a standard shape rather than
a bespoke table nobody can audit. Dolos handles integrity *without* an LLM, because
a finding presented at an appeal must be explainable. The pedagogy benchmark
produces the accuracy-and-performance evidence the technical documentation needs.

**Sequence against the real dates.**
1. **Now** — Article 50 transparency has applied since **2 Aug 2026**: disclose AI
   interaction at every touchpoint. Confirm no emotion-recognition anywhere in the
   product (**banned in schools since Feb 2025**).
2. **Now → mid-2027** — risk management, data governance, logging via Ralph,
   human-oversight design, technical documentation.
3. **By 2 Dec 2027** — conformity assessment for the high-risk functions.

**Note.** **Regulation (EU) 2026/1744** was cross-checked across several secondary
sources this pass, not read from the Official Journal. Confirm at source before
this appears in a client deliverable.

**Effort.** 10-12 weeks for the scaffolding; the audit-and-remediate slice for the
already-live obligations is 2-3 weeks and can be sold on its own.

---

## P549 — Multi-agent classroom on the APAC cores (Global, APAC-sourced)

**Brief.** Fastest credible tutoring prototype available. Use it for a pilot in any
region — the supply is APAC-academic, the deployment need not be.

| Role | Component | Licence |
|---|---|---|
| Lifelong tutor + learner memory | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 48.9k★ · v1.7.0 (2026-10-28) |
| Multi-agent classroom roles | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** · 41.7k★ · v1.3.0 (2026-10-29) |
| Mastery estimation, published | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | **MIT** · 274★ |
| Retention | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) + [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** · 538★ / **MIT** · 4.1k★ |
| Records | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |

**Wiring.** DeepTutor owns the long-lived learner model (three-layer memory,
learning paths, mastery gates). OpenMAIC supplies the classroom *cast* — lecturer,
peer, assistant — when the pedagogy calls for social learning rather than 1:1.
**Replace any prompt-claimed mastery with OATutor's Bayesian Knowledge Tracing**:
it is the one published estimator on these shelves, and "the model says the student
has mastered it" is not a measurement. Mastered items are pushed into the learner's
**own** Anki deck via the MCP server, scheduled by FSRS — so the learning survives
the end of the engagement. Everything lands in Ralph as xAPI.

**Why both large repos.** DeepTutor is depth-over-time for one learner; OpenMAIC is
breadth-of-role in one session. They solve different halves and neither subsumes
the other.

**Regional adjustments.**
- **India / China** — AI-content labelling is mandatory (India from **20 Feb 2026**).
  Attach provenance metadata at authoring time, in the H5P package, not afterwards.
- **ANZ** — public opinion leans toward *banning* AI in schools. Lead with Dolos
  integrity and the audit trail; demo the controls before the tutor.

**Effort.** 4-6 weeks to a defensible pilot; 2 weeks for a demo on DeepTutor alone.

---

## P550 — Teacher-first lesson preparation in PT/ES (LATAM)

**Brief.** The LATAM market has already moved to the teacher as buyer (Teachy's
position, and the 2026 EdTech 100 shows upskilling losing ground). Build for the
teacher, in Portuguese and Spanish, and integrate with the incumbent rather than
replacing it.

| Role | Component | Licence |
|---|---|---|
| Incumbent school management (integrate only) | [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 · 722★ |
| Accessible LMS, thin IT | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 · 1.0k★ |
| Offline-first delivery | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** · 1.2k★ |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | **MIT** · 387★ |
| Portable output | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 152★ |
| Rubric gate | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | **Apache-2.0** · 601★ |

**Wiring.** i-educar is **GPL-2.0 and must stay across a service boundary** — read
enrolment, attendance and performance signals over its API/DB into your own
permissive service; never link it. Educhain generates plans and items; H5P makes
the output portable into Chamilo, Moodle or Kolibri. **Kolibri is the
connectivity answer**: a cloud-only tutor is undeployable in the municipalities
that run i-educar, so generate centrally and *ship* content packages offline.

**De-risking vehicle.** Run the pilot inside **Brazil's ANPD AI regulatory sandbox
(open through December 2026)**. That produces a compliance narrative that survives
**PL 2338/2023** becoming law, and it is a concrete reason to start now rather than
wait for the statute.

**Greenfield read.** CENIA finds **13 of 19 LAC countries studied** have not yet
introduced early AI adoption in schools — national AI-literacy programmes with no
incumbent to displace. Google.org's **$4.6M across nine countries, 1.25M students
by 2028** is the co-funding context.

**Effort.** 6-8 weeks. Add 2-3 weeks for i-educar integration per municipal variant.

---

## P551 — Licence due-diligence gate (run this first, every engagement)

**Brief.** Before any of the above. Education repositories mis-grade more often
than any other vertical this base has measured, and the failures are expensive
rather than cosmetic.

| Role | Component |
|---|---|
| Known-bad controls | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) 2.1k★ (bespoke non-commercial), [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) 340★ (Elastic-2.0), [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) 5.1k★ (CC-BY-**NC**-4.0) |
| Known-bad filename control | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) — 107.5k★, grant at `LICENSE.txt`, **no licence type named on the page** |
| Known-good controls | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0), [learningequality/kolibri](https://github.com/learningequality/kolibri) (MIT), [sakaiproject/sakai](https://github.com/sakaiproject/sakai) (ECL-2.0) |

**The four rules, each earned from a real failure.**
1. **Grade from the title block, never a body sentence.** PageLM's licence *opens*
   with *"Permission is hereby granted, free of charge…"* and then prohibits
   redistribution outright and requires a **revenue-share agreement before any
   commercial deployment**. A body-matching probe calls that MIT.
2. **Try `LICENSE`, `LICENSE.txt` and `LICENSE.md`.** One filename misfiles a
   **107.5k★** asset as ungranted — and when the page names no licence either, the
   file has to be read, not inferred.
3. **Never drop a `NonCommercial` qualifier** when naming a family.
4. **Case-insensitive matching, or none.** A GPL-2.0 payload that happens to
   mention *"GNU Lesser General Public License"* in its preamble cross-reference
   will grade as LGPL under a case-sensitive matcher —
   [oat-sa/tao-core](https://github.com/oat-sa/tao-core) (GPL-2.0, 64★) is the live
   example.

**Output.** A three-band verdict per repository — *permissive / copyleft-integrate
only / not usable* — with the licence filename, the title line read, and the byte
size recorded. Anything in the third band never reaches an architecture diagram.

**Effort.** 1 week to stand up, then minutes per repository.

---

## P552 — Pedagogy evaluation harness (the differentiator)

**Brief.** Answer "does this actually teach?" with a number, before a client asks
and before a competitor can.

| Role | Component | Licence |
|---|---|---|
| Pedagogical knowledge benchmarks (CDPK, SEND) | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** · 13★ |
| Teacher-workflow eval rubrics | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | **Apache-2.0** · 601★ |
| Mastery ground truth | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) (BKT) | **MIT** · 274★ |
| Longitudinal signal | [openfun/ralph](https://github.com/openfun/ralph) (xAPI) | **MIT** · 51★ |

**Wiring.** Run CDPK and SEND across the candidate models at model-selection time —
the result is a model choice you can defend in writing, which is a different
artefact from a preference. Run the k12 rubrics in CI over a fixed prompt set so a
model or prompt change that degrades teaching quality fails the build. Use OATutor
BKT as ground truth for mastery claims. Ralph supplies the longitudinal arm: did
mastery *hold* at 30 days, not just at the end of the session.

**Why this is worth its own pattern.** The pedagogy benchmark has **13 stars**
against DeepTutor's **48.9k**. Everyone is shipping tutors; almost nobody is
measuring teaching. That asymmetry is a sales advantage today and table stakes
within a year — and the SEND benchmark additionally speaks to special educational
needs, which is where the duty-of-care questions in procurement actually land.

**Effort.** 2-3 weeks standalone; it should be folded into every other pattern here
rather than sold alone.

---

## Pattern selection

| If the brief is… | Run |
|---|---|
| Any engagement, before anything else | **P551** licence gate |
| Canvas-based district or university (NA) | **P547** |
| EU vendor or ministry with grading/admissions/proctoring AI | **P548** |
| Fastest credible tutoring pilot, any region | **P549** |
| Teacher-facing, PT/ES, public sector (LATAM) | **P550** |
| A claim about learning outcomes needs defending | **P552**, folded into the above |

**Components not used, and why:** `advisingapp` (Elastic-2.0 — forbids the hosted
shape), `PageLM` (non-commercial, revenue-share), `cn-math-taxonomy`
(CC-BY-NC-4.0). All three look permissive to a careless probe. See **P551**.
