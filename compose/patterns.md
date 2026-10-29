---
industry: education
region: Global
updated: 2026-10-29
---

# Compose Patterns — Education

**Pass `p528` · 2026-10-29.** Ten recipes. Every component named below was read
from its repository page this pass, and **every licence was read from the licence
file's own title block** (`raw.githubusercontent.com` is reachable while
`github.com` returns HTTP 403 through the session proxy). No recipe uses a
component this base has not verified.

**The licence rule that shapes all eight:** the mainstream LMS cores are copyleft
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
| Lesson authoring, source-backed | 🆕 [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** · 462★ |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | **MIT** · 387★ |
| Portable output | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 152★ |
| Acceptability gate | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) rubrics | **Apache-2.0** · 601★ |
| Event records | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |

**Wiring.** `canvas-mcp` runs as a separate process and is the *only* thing that
touches Canvas — this is what keeps AGPL-3.0 §13 away from your code. The copilot
calls it for roster, assignment and submission context. 🆕 **`lineage-skill` is the
authoring stage**: feed it the course's own videos, PDFs, transcripts and notes and
it emits lessons that **trace back to that source material** — so a teacher
challenged on "where did this come from" has an answer, and Educhain fills in
items underneath it. Output is emitted as **H5P** so it survives a future platform
migration; every interaction is written to Ralph as xAPI. The k12 rubrics run in CI
against a fixed set of teacher prompts, and a regression there fails the build.

**Hard constraint — build it in, not in the policy doc.** Oklahoma (S.B. 1734) bars
AI as the main basis for high-stakes decisions and requires a written district
policy before 2027-28; Maryland's districts have 120 days from MSDE guidance; Idaho
(S.B. 1227) adds data-privacy duties; Utah (H.B. 218) mandates AI literacy in grade
7/8. The grading path must be **structurally** human-decided: the agent may draft,
a human must commit, and the xAPI record must name who committed. "We have a
policy" is not the deliverable; "the model cannot do it" is.

**Effort.** 6-8 weeks. Weeks 1-2 MCP deployment and auth; 3-5 authoring +
H5P emission; 6 rubric CI; 7-8 audit trail and district pilot.

---

## P548 — EU AI Act conformity scaffolding for an education product (EMEA)

**Brief.** A European edtech vendor, university or ministry needs its grading /
admissions / proctoring AI ready, with the obligations that are already live
satisfied now.

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

🆕 **Sequence against the real dates — and establish which clock the client is on
before anything else.** Regulation (EU) 2026/1744 (Digital Omnibus, OJ 24 Jul 2026,
in force 27 Jul 2026):

1. **Now** — **Article 50 transparency has applied since 2 Aug 2026** and was *not*
   delayed: disclose AI interaction at every touchpoint. Confirm no
   emotion-recognition anywhere in the product (**banned in schools since Feb 2025**).
2. 🆕 **By 2 Dec 2026 (~5 weeks out)** — two new Article 5 prohibitions added by the
   Omnibus phase in. Check the product against them now, not in 2027.
3. **Now → 2027** — risk management, data governance, logging via Ralph,
   human-oversight design, technical documentation. 🆕 National **regulatory
   sandboxes** must exist by 2 Aug 2027: a sandbox slot is a de-risking vehicle,
   as in P550.
4. **By 2 Dec 2027** — conformity assessment for stand-alone Annex III high-risk
   functions (grading, admissions triage, programme assignment, proctoring, access
   to qualifications). 🆕 **2 Aug 2028** if the AI is a safety component of a
   regulated product (Annex I).
5. 🆕 **By 2 Aug 2030 — if, and only if, the client is a public authority** with the
   system *already in service*. State schools and public universities qualify
   across most of the EU.

🆕 **The two-clock rule is the commercial core of this pattern.** A private vendor
has ~25 months; a public institution running an existing system may have ~45. Ask
first, scope second — and never let a public client be told they have 13 months.

**Note.** Regulation (EU) 2026/1744 was cross-checked across multiple secondary
sources across two passes, **not read from the Official Journal**. The 2 Dec 2027,
2 Aug 2028 and Article 50 dates are corroborated by several sources; **the 2 Aug
2030 public-authority date rests on one**. Read the regulation before any of this
reaches a client deliverable, and that date before it reaches a public one.

**Effort.** 10-12 weeks for the scaffolding; the audit-and-remediate slice for the
already-live obligations (Article 50, emotion recognition, the 2 Dec 2026
prohibitions) is **2-3 weeks, needs no new technology, and sells on its own.**

---

## P549 — Multi-agent classroom on the APAC cores (Global, APAC-sourced)

**Brief.** Fastest credible tutoring prototype available. Use it for a pilot in any
region — the supply is APAC-academic, the deployment need not be.

| Role | Component | Licence |
|---|---|---|
| Lifelong tutor + learner memory | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 49.0k★ · v1.7.0 (2026-10-28) |
| Multi-agent classroom roles | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** · 41.8k★ · v1.3.0 (2026-10-29) |
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
  🆕 Use `lineage-skill` (Apache-2.0) for the authoring leg: source-backed output
  means the labelling obligation is met structurally.
- 🆕 **Vietnam** — the risk-based AI law gives **education an 18-month transition**
  for systems already in service: the softest APAC landing for a product already
  running elsewhere, and the right first port.
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
| Authoring, source-backed | 🆕 [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** · 462★ |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | **MIT** · 387★ |
| Single-teacher reference shape | 🆕 [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | **MIT** · 63★ |
| Portable output | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 152★ |
| Rubric gate | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | **Apache-2.0** · 601★ |

**Wiring.** i-educar is **GPL-2.0 and must stay across a service boundary** — read
enrolment, attendance and performance signals over its API/DB into your own
permissive service; never link it. `lineage-skill` and Educhain generate plans and
items; H5P makes the output portable into Chamilo, Moodle or Kolibri. **Kolibri is
the connectivity answer**: a cloud-only tutor is undeployable in the municipalities
that run i-educar, so generate centrally and *ship* content packages offline.

🆕 **Read Claw-ED before designing the teacher UX.** It is MIT, 63★, local-first,
works from the teacher's own curriculum files, and is explicit that it is
**single-teacher-per-instance, not multi-tenant**, with student-facing features
labelled experimental. That boundary is exactly the gap a studio fills — and the
repo is an honest map of where the hard part starts.

**De-risking vehicle.** Run the pilot inside **Brazil's ANPD AI regulatory sandbox
(open through December 2026)**. That produces a compliance narrative that survives
**PL 2338/2023** becoming law. 🆕 **Peru** also has sandboxes and a phased rollout,
so the same play works there; **Colombia** has CONPES 4144 (Feb 2025) as the policy
hook; **Mexico's** risk-based bill is still only in the Senate, so there is no
compliance anchor to sell against there yet.

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
| Known-bad controls, mislabelled | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) 2.1k★ (bespoke non-commercial, grant at `LICENSE.md`), [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) 340★ (Elastic-2.0), [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) 5.1k★ (CC-BY-**NC**-4.0) |
| 🆕 Known-bad control, **self-contradicting** | [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) 91★ — sidebar `GPL-3.0`, **README badge `License: MIT`**, licence file `GNU GENERAL PUBLIC LICENSE Version 3` |
| Known-bad filename control | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) — 107.5k★, grant at `LICENSE.txt`, **no licence type named on the page**; read this pass as **Apache-2.0** |
| 🆕 Known-bad **ungranted** controls | [A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) **64★** (no licence file; README says only *"open source and available for educational purposes"*), [idoforgod/Vibe-learning-AgenticWorkflow](https://github.com/idoforgod/Vibe-learning-AgenticWorkflow) 25★ (sidebar "License" link **anchors into the README**), [tosuki/moodle-mcp](https://github.com/tosuki/moodle-mcp) (search result claimed MIT; no licence file) |
| 🆕 Known-bad **per-app** control | [frappe/lms](https://github.com/frappe/lms) **AGPL-3.0** vs [frappe/education](https://github.com/frappe/education) **GPL-3.0** — same vendor, same framework, two regimes |
| Known-good controls | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0), [learningequality/kolibri](https://github.com/learningequality/kolibri) (MIT), [sakaiproject/sakai](https://github.com/sakaiproject/sakai) (ECL-2.0) |

**The seven rules, each earned from a real failure.**
1. **Grade from the title block, never a body sentence.** PageLM's licence *opens*
   with *"Permission is hereby granted, free of charge…"* and then prohibits
   redistribution outright and requires a **revenue-share agreement before any
   commercial deployment**. A body-matching probe calls that MIT.
2. **Try `LICENSE`, `LICENSE.txt`, `LICENSE.md` and `license.txt`.** One filename
   misfiles a **107.5k★** asset as ungranted; Frappe's grant is at `license.txt`,
   PageLM's at `LICENSE.md`. Try `main`, `master` *and* `develop`.
3. **Never drop a `NonCommercial` qualifier** when naming a family.
4. **Case-insensitive matching, or none.** A GPL-2.0 payload that happens to
   mention *"GNU Lesser General Public License"* in its preamble cross-reference
   will grade as LGPL under a case-sensitive matcher —
   [oat-sa/tao-core](https://github.com/oat-sa/tao-core) (GPL-2.0, 64★) is the live
   example.
5. 🆕 **When the README badge and the sidebar disagree, the licence file decides.**
   A badge is a claim; a licence file is the grant. (`lumen`.)
6. 🆕 **Record "no licence file" as a verdict, not a blank.** An absent grant is a
   *harder* blocker than a bad one — there is no counterparty to negotiate an
   exception with. Stars do not imply a grant: 64★ bought none.
7. 🆕 **Grade per app, not per vendor** (`frappe/*`), and **never** accept a search
   result or a blog roundup as the licence channel — three of the controls above
   were mis-described by one.

🆕 **Channel note, and it is reusable.** With `github.com` and `api.github.com`
returning HTTP 403 through the session proxy, **`raw.githubusercontent.com` is
still reachable** — so the gate should fetch the licence *file* directly rather
than scrape a sidebar badge. That is both the cheaper channel and the more
authoritative one, and it is what rules 1, 5 and 6 require. A ~20-line shell loop
over `{branch} × {filename}` printing the first four non-blank lines is the whole
implementation.

**Output.** A **four**-band verdict per repository — *permissive / copyleft-integrate
only / not usable / **ungranted*** — with the licence filename, the branch, the
title line read, and the byte size recorded. The last two bands never reach an
architecture diagram.

**Effort.** 1 week to stand up, then **seconds** per repository.

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
against DeepTutor's **49.0k**. Everyone is shipping tutors; almost nobody is
measuring teaching. 🆕 The **OECD 2026 Digital Education Outlook** reportedly tells
institutions to prefer **purpose-built educational AI over general-purpose tools** —
this harness is how you evidence that claim rather than assert it.

🆕 **Two regional angles the benchmark's own provenance opens up.**
- **LATAM / Spanish.** The repository credits **Chile's Agencia de la Calidad de la
  Educación and CPEIP** for the exams CDPK is built from. Running it in Spanish,
  against Chilean teacher-certification standards, answers *"does this model know
  how to teach **here**"* — and CENIA already co-chairs the ECLAC regional AI
  working group, so there is a named counterpart.
- **EMEA / SEND.** Special educational needs and disabilities is where European
  regulators and parents apply the most pressure and where essentially no vendor
  can show evidence. `SEND` is half of this benchmark and it is MIT.

**Effort.** 2-3 weeks standalone; it should be folded into every other pattern here
rather than sold alone.

---

## 🆕 P553 — The Moodle agent bridge (the build nobody has done)

**Brief.** Moodle has the sector's largest install base and plugin ecosystem and
**no credible agent bridge.** Canvas has one at 308★; the entire Moodle-MCP field
tops out at **27★**. This is the clearest build opportunity on this base, and it
is a *build*, not a fork.

| Role | Component | Licence |
|---|---|---|
| The platform (not forked) | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 · 7.6k★ |
| Nearest prior art — the lineage head | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | **MIT** · **27★** |
| Secondary prior art | [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) (claims ~230 tools, Moodle 4.5/5.x) | **MIT** · 2★ |
| ⛔ Do **not** start here | [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | **AGPL-3.0** · 1★ |
| Reference architecture to copy | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** · 308★ |
| Portable output | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 152★ |
| Event records | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |

⚠️ **Why the field is empty — corrected `p528`, and the correction changes the
recipe.** `p527` wrote that the field *"resolves to roughly three codebases."* It
does not. A thirteen-address census — **twelve probed first-hand this pass**, the
thirteenth a duplicate carried from `p527` — found **eleven independent codebases
plus two forks**, four languages, tool counts from **8 to ~230**, **37 stars across every
counter read**, and 🟢 **ten of the eleven under MIT.** The forks are real
(`thc1006` → `G36maid`; `triffon` → `falkenslab`, via its
`Copyright (c) 2026 Falkenslab` line) and `tosuki/moodle-mcp` is genuinely
ungranted — but they are two of thirteen, not the shape of the field. Full census:
[`../repos/foundations.md`](../repos/foundations.md).

🔵 **So this is a consolidation, not a greenfield build**, and that is cheaper and
more defensible. Four MIT pieces to take, each verified `p528`:

| Take | From | Why that one |
|---|---|---|
| Typed tool surface + tested version matrix (3.7 / 4.5 / 5.2) | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) · MIT · 27★ · Rust | The only one that names three live-tested Moodle versions |
| Two-flag write gate + `confirm=true` on destructive calls | [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) · MIT · 3★ | Best-governed write model in the census (32 read / 8 write, writes off by default) |
| Course-whitelist boundary (`MOODLE_DEV_COURSE_WHITELIST`, prod writes off) | [leshamblin/MoodleMCP](https://github.com/leshamblin/MoodleMCP) · MIT · 2★ | The only one that separates dev from prod write scope |
| Zero-dependency posture (stdlib only, single file) | [Faixiang/moodle-mcp](https://github.com/Faixiang/moodle-mcp) · MIT · 2★ | Makes the institutional security review short |

🟢 **The asset worth owning is the vocabulary, not the server.** No two of the
eleven name the same operations the same way, and three contradict their own
READMEs on tool count (Faixiang 6 vs 8, leshamblin 70 vs 67, falkenslab 140 vs
~230). **Publish the tool schema as a spec and the server as its reference
implementation.** 🔴 Do not take `sonstellar969/open-moodle` as a starting point
despite its MIT grant: it links **AGPL-3.0 PyMuPDF**. See **P556**.

**Wiring.** Build the server **permissively (MIT/Apache-2.0) and out-of-process**,
speaking **Moodle Web Services** — never link Moodle's GPL-3.0 code, and never
vendor the AGPL-3.0 implementation into the deliverable. Start from
`G36maid/moodle-mcp` (MIT) for the tool surface and **copy `canvas-mcp`'s shape**
for everything else: it is the mature one, and it already answers the questions
this build will hit (auth scoping, student-vs-educator tool split, per-role skill
packaging, a security-release cadence). Two design commitments worth making up
front, both learned from the field above:

1. **Read-write, but gated.** `csmediapro` chose read-only to be safe; that is the
   right default and the wrong ceiling. Separate read tools from write tools and
   require an explicit human commit on anything that touches a grade — which is
   also what Oklahoma S.B. 1734 requires in P547.
2. **State a tool count that is true.** `falkenslab` says ~230 in the README and a
   search summary said 140; `canvas-mcp` says 102 in About and 128 in the README.
   The whole category has a credibility problem that costs nothing to avoid.

Emit **H5P** for generated content and write every interaction to **Ralph** as
xAPI, as in P547 — the bridge is only half the deliverable, the audit trail is the
other half.

**Why Globant specifically.** Moodle's plugin directory is distribution for free,
and a permissive MCP server is the one component in this sector that **every**
Moodle engagement afterwards reuses. It is the highest-leverage reusable asset on
this base, and today's bar to clear is 27 stars.

**Effort.** 8-10 weeks to a credible first release (4-5 for the tool surface on
Web Services, 2 for auth and role scoping, 2-3 for H5P/xAPI and docs). Publish it;
the field is empty.

---

## 🆕 P554 — Governance over the AI already in the building (LATAM-led, globally applicable)

**Brief.** UNESCO IESALC + UNU-IAS surveyed **200 LATAM higher-ed institutions in
19 countries: 87% already use AI, 26% have a formal AI strategy**, and adoption is
driven by **individual faculty and students, not institutional policy**. These
institutions do not need to be sold AI. They need control of the AI already
running, unmanaged, inside them. This is consulting-led with a software tail, and
it is the highest-probability LATAM opening on this base.

| Role | Component | Licence |
|---|---|---|
| Audit substrate (xAPI) | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |
| Acceptability yardstick | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) rubrics | **Apache-2.0** · 601★ |
| Model-fitness evidence (ES, Chilean standards) | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** · 13★ |
| Integrity, explainable | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** · 355★ |
| Incumbent systems (integrate only) | [i-educar](https://github.com/portabilis/i-educar) GPL-2.0 · [chamilo](https://github.com/chamilo/chamilo-lms) GPL-3.0 · [moodle](https://github.com/moodle/moodle) GPL-3.0 | copyleft — service boundary |
| Mastery ground truth | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | **MIT** · 274★ |

**Wiring — four stages, and the first two sell on their own.**

1. **Inventory (2-3 weeks).** Find the AI actually in use. Bottom-up adoption means
   it is in individual faculty's tools, not in procurement records, so this is
   interviews and traffic analysis, not a vendor list.
2. **Policy and classification (2-3 weeks).** Sort each use by whether it touches a
   high-stakes decision — grading, admissions, progression. That is the same
   classification Annex III forces in EMEA (P548) and Oklahoma forces in NA (P547),
   which is why this pattern ports.
3. **Enforcement in code (4-6 weeks).** Human-in-the-loop on every high-stakes path,
   enforced structurally rather than by policy; Dolos for integrity findings that
   survive an appeal; OATutor BKT wherever a mastery claim is being made.
4. **Audit trail (2-3 weeks).** Ralph as the xAPI store, so "is the AI helping, and
   who decided what" becomes answerable retrospectively instead of arguable.

**Why the benchmark belongs here.** CDPK is built on **Chile's own
teacher-certification exams** (Agencia de la Calidad de la Educación, CPEIP,
credited on the repo). Run in Spanish against Chilean standards, it turns stage 2
from a policy document into **evidence** — and **CENIA** co-chairs the ECLAC
regional AI working group alongside **Uruguay's AGESIC**, so there is a named
institutional counterpart rather than a cold call. UNESCO's **Observatory on AI in
Education for LAC** (launched Santiago, 14 April 2026) is the other door.

**Where it ports.** The 87/26 split is the sharpest *measured* instance of a
global pattern: 70% of higher-ed institutions in Europe and North America have
guidance "in place or in development" — the second half of that phrase is this
engagement. Lead with the UNESCO number in LATAM because it is regional and
primary; lead with the regulation in EMEA (P548) and with state statute in NA
(P547). **Same four stages, different opening sentence.**

**Caveat to carry into the pitch.** CENIA finds **13 of 19 LAC countries** have not
begun early AI adoption in schools, and adoption in urban schools concentrates in
better-resourced private institutions. **This pattern fits the 87%, not the
greenfield** — for the greenfield, run P550 with Kolibri.

**Effort.** 10-15 weeks end to end; stages 1-2 are a **4-6 week standalone
assessment** and the natural door-opener.

---

## 🆕 P555 — Portuguese-language curriculum and assessment stack (LATAM, Brazil)

**Brief.** Everything in this recipe is **Brazilian, MIT and verified**, which is
what makes it new: for seven passes this base held that LATAM contributed *data*
and not *code* to the agent legs. It does not. The recipe grounds a teacher-facing
agent in Brazil's own curriculum (**BNCC**) and marks student writing against
Brazil's own examination (**ENEM**) — no translation layer, no US rubric wearing a
Portuguese label.

| Role | Component | Licence | Verified |
|---|---|---|---|
| Essay marking, 5 ENEM competencies | [dsvi-b/corretor-enem](https://github.com/dsvi-b/corretor-enem) | **MIT** · 7★ | `p420`, re-read `p528` |
| Curriculum grounding (BNCC `EF01`–`EF04`, PCNs) | [ThallesYVasconcelos/Agente-Educacional](https://github.com/ThallesYVasconcelos/Agente-Educacional) | **MIT** · 0★ | `p528` |
| LMS seam | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) (or **P553**'s consolidation) | **MIT** · 27★ | `p528` |
| Pedagogical evaluation | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** · 13★ | `p527` |
| Retention | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** · 4.1k★ | `p527` |
| Event records | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ | `p527` |
| Local inference | Ollama (the EduRAG reference runs `llama3.2` / `qwen2.5` / `mistral` / `gemma2`) | — | `p528` |

**Wiring.**

1. **Take `corretor-enem` as a skill, not a service.** It is *agent-agnostic by
   design*: no API, no ML, no model weights — a methodology plus a local SQLite
   corpus of **11,147 examiner-marked essays**, which the agent reads to anchor
   its scores. 🟢 **That is why it belongs at the bottom of the stack:** the
   marking rationale is inspectable and the corpus is the citation. Methodology
   credited to **Silva & Araujo (UFPE, 2024)**; corpora to `rafaelanchieta/essay`
   and `lplnufpi/essay-br`.
2. **Copy EduRAG's grounding architecture, do not depend on it.** 0★ and a
   university course's final project — but it is the cleanest reference this base
   has for curriculum grounding: page-level citations into **MEC** documents,
   BNCC-code identification for an arbitrary activity, a **Self-RAG** check
   before answering, and **Giskard** for evaluation. Re-implement that shape on
   your own stack (LangGraph + ChromaDB + `bge-m3` embeddings is what it uses).
3. **Attach to the LMS over MCP**, never by forking Moodle (GPL-3.0).
4. **Evaluate with `pedagogy-benchmark` before and after.** It carries **CDPK**
   and **SEND**, and its ground truth comes from Chile's Agencia de la Calidad de
   la Educación and CPEIP — 🔵 **so the evaluation instrument is also LATAM**, and
   a procurement conversation can be held entirely in regional evidence.
5. **Write every marking event to Ralph (xAPI)** so the audit trail survives the
   agent.

🔴 **State the maturity honestly to the client.** The two Brazilian components
total **7 stars, 1 fork and zero releases**. They are *correct* and they are
*unproven at scale*. Price the engagement as "harden and operate verified
reference code", not "integrate a maintained dependency" — and expect to become
the de-facto maintainer of both. ⚠️ `corretor-enem`'s own page calls its output
**an estimate, not an official score**; that sentence belongs in the deliverable's
UI, not just in its README.

**Timeline.** 6–8 weeks to a marked-essay pilot in one school network. **Region:
LATAM.**

## 🆕 P556 — The grant-union gate (run inside P551)

**Brief.** `p551` reads the repository's licence file. `p528` found two ways that
is not enough, both in live education repos, and both would pass a repo-level
probe.

| Failure | Instance, verified `p528` | What the probe sees | What ships |
|---|---|---|---|
| 🔴 **Transitive copyleft** | [sonstellar969/open-moodle](https://github.com/sonstellar969/open-moodle) | **MIT** | Links **PyMuPDF (AGPL-3.0)** for PDF extraction — the page says so itself. Network copyleft reaches the hosted deliverable. |
| 🟡 **Non-code grant** | [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) · **926★** | sidebar names **no licence**; README badge reads CC BY-SA 4.0 | **CC BY-SA 4.0** — a *content* licence. ShareAlike propagates to adaptations, no patent grant, and the code/content line is undrawn across a 157-tool MCP server and 165 prose skills. |

**The gate, four commands and two questions.**

1. `curl -s raw.githubusercontent.com/<repo>/<branch>/README.md` → **does the
   address resolve at all?** A 404 everywhere is *absent*, not *ungranted*.
   (`belentani7/aprende-brasil`: a search summary described 205 modules and a
   tutor named "Nilo"; the repository does not exist.)
2. Read the **licence file's title block** — not the badge, not the sidebar.
3. **Enumerate the dependency licences** (`requirements.txt`, `pyproject.toml`,
   `package.json`, `Cargo.toml`) and take the **union**. 🔵 *The grant you ship is
   the union of the grants you link.*
4. Ask **what the licence was written to cover.** CC BY-SA on an executable skill
   library and MIT on a corpus are both category errors; only the first is
   currently common, and it is on the largest education-skills repo in the field.

**Output.** One row per component: address resolves (y/n) · grant from title
block · dependency grants · union verdict · *written for code or for content*.
🟢 **Any `ShareAlike`, `NonCommercial` or `AGPL` in the union stops the fork
decision**, whatever the top-level badge says.

## Pattern selection

| If the brief is… | Run |
|---|---|
| Any engagement, before anything else | **P551** licence gate |
| Canvas-based district or university (NA) | **P547** |
| EU vendor, university or ministry with grading/admissions/proctoring AI | **P548** — *establish public vs private clock first* |
| Fastest credible tutoring pilot, any region | **P549** |
| Teacher-facing, PT/ES, public sector (LATAM) | **P550** |
| 🆕 Moodle client, or a reusable asset worth owning | **P553** |
| 🆕 Institution already using AI without a strategy (the 87%) | **P554** |
| 🆕 Brazilian school network, PT-BR curriculum or ENEM marking (LATAM) | **P555** |
| 🆕 Any fork decision — run **after** P551's title-block read | **P556** grant-union gate |
| A claim about learning outcomes needs defending | **P552**, folded into the above |

**Components not used, and why:** `advisingapp` (Elastic-2.0 — forbids the hosted
shape), `PageLM` (non-commercial, revenue-share), `cn-math-taxonomy`
(CC-BY-NC-4.0), 🆕 `lumen` (**GPL-3.0**, despite its own README badge saying MIT),
🆕 `csmediapro/moodle-mcp-server` (AGPL-3.0 — see P553), 🆕
`A-R007/Multi-Agent-Study-Assistant`, `idoforgod/Vibe-learning-AgenticWorkflow`
and `tosuki/moodle-mcp` (**ungranted — no licence file at all**), 🆕
`sonstellar969/open-moodle` (MIT, but links **AGPL-3.0** PyMuPDF — see **P556**),
🆕 `GarethManning/education-agent-skills` (**CC BY-SA 4.0**, 926★ — a real grant
with a ShareAlike condition, usable only where the derivative can be published),
🆕 `henriquebotelhogomes/educacao` and `Fatima0923/AssessmentAI` (**ungranted**).
All of them look usable to a careless probe. See **P551** and **P556**.
