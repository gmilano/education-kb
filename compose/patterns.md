---
industry: education
region: Global
updated: 2026-10-29
---

# Compose Patterns — Education

**Pass `p532` · 2026-10-29.** **Twenty-one** recipes. Every component named below was read
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

> 🔴 **`p529`: superseded in scope by [`P558`](#-p558--the-moodle-bridge-generator-the-build-the-field-actually-needs).**
> The premise below — *"the entire Moodle-MCP field tops out at 27★"* — is wrong.
> The field is **222 addresses**; its ceiling is **52★ and ungranted**; its
> permissive leader is **45★ and eight months stale**. 🟢 **The conclusion
> survives and strengthens** — there is still no credible, shippable bridge — but
> *"nobody has done this"* becomes *"hundreds have each done it once, for one
> campus."* **P553 remains valid as a single-client build.** When the client is
> buying a capability rather than one integration, run **P558** instead.

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

## 🆕 P557 — Mastery-tracked tutoring with real retention (Global)

**Brief.** Every "AI tutor" demo answers questions. Almost none **model what the
learner knows** or **schedule the review that makes it stick** — the two things
fifty years of cognitive science say decide the outcome. Both halves now exist
permissively and neither needs building.

| Role | Component | Grant | Verified `p529` |
|---|---|---|---|
| Tutoring + **mastery estimate** | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | API + title block · **57★** · Go · pushed 28 Oct 2026 · topics name **`bkt`** |
| Retention **algorithm** | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | API + title block · **4,119★** · 165 forks |
| Retention **surface** the learner keeps | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | **MIT** | API · **538★** |
| Independent mastery baseline | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | **MIT** | API · **274★** · BKT, published |
| Does the model teach acceptably? | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | API · 13★ · CDPK + SEND |
| Event records in a standard shape | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI/LRS · 51★ |

**Wiring.** `tutor-mcp` mounts as an MCP server beside whatever assistant the
client already licenses — it is not an application, so there is no UI to
displace. It holds the learner model; every turn updates a **BKT** estimate per
skill. When a skill crosses mastery, the agent emits a card through
`anki-mcp-server` and **`fsrs4anki` owns the interval** — do not invent a review
schedule, the problem is solved and the solution is MIT. `ralph` receives xAPI
statements so the mastery trace lives in a standard store rather than a vendor
table. `OATutor` is the control: run the same cohort against a published BKT
implementation and compare, because *"our tutor tracks mastery"* is a claim an
institution will ask you to prove.

🟢 **Why this composition and not a bigger one.** Every component is **MIT**,
every one was verified twice this pass, and the whole stack is **out-of-process**
— so it drops beside a GPL Moodle or an AGPL Canvas without touching either.
**8–10 weeks.** 🔴 **Gate it with `P551` + `P556`:** all six rows are
*repository*-level verdicts, and `fsrs4anki` ships Python/Jupyter with a real
dependency tree.

## 🆕 P558 — The Moodle bridge **generator** (the build the field actually needs)

**Brief.** 🔴 **`P553` assumed a missing product. The measurement says otherwise:
the field has 222 addresses, 14 of the top 26 bridge exactly one named
university, and nobody has consolidated anything.** You cannot consolidate
repositories whose purpose is to be institution-specific. **What is missing is
not a bridge — it is the thing that produces a bridge**, with the safety and
audit properties an institution's legal and data-protection review will demand.

| Role | Component | Grant | Note |
|---|---|---|---|
| Tool-vocabulary reference | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | **MIT** · 27★ | The only one naming three live-tested Moodle versions (**3.7, 4.5, 5.2**) |
| **Write-gating** reference | [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) | **MIT** · 3★ | Writes off by default behind two flags; `confirm=true` on destructive calls — **the best governance model in the field** |
| Scope-boundary reference | [leshamblin/MoodleMCP](https://github.com/leshamblin/MoodleMCP) | **MIT** · 2★ | `MOODLE_DEV_COURSE_WHITELIST`, `MOODLE_PROD_ALLOW_WRITES=false` |
| Architecture to copy wholesale | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** · 308★ | The field's one proven LMS bridge |
| The platform — **never forked** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 · 7.6k★ | Bridge stays out-of-process |
| Per-tenant worked examples | [`iDavi/usp-mcp`](https://github.com/iDavi/usp-mcp) (🔴 GPL-3.0), [`Equisdo/fich-mcp`](https://github.com/Equisdo/fich-mcp) (**MIT**), [`changazo/udesa-mcp`](https://github.com/changazo/udesa-mcp) (**Apache-2.0**) | mixed | **Read for requirements, do not vendor.** USP is GPL-3.0 — copying it into a permissive core relicenses the core |
| Audit trail | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ | Every tool call becomes an xAPI statement |

⛔ **Do not start from** [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp)
(52★, **no licence file** — the field's most-starred artefact is unshippable),
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server)
(**AGPL-3.0**), `threos/mcp4lms` (**AGPL-3.0**), or
[`sonstellar969/open-moodle`](https://github.com/sonstellar969/open-moodle)
(MIT repo, **AGPL-3.0 PyMuPDF** in the artefact — `P556` catches this one).

**Wiring.** One permissive core (`MIT`/`Apache-2.0`) implementing a **named tool
vocabulary** taken from `G36maid`, with three properties the hand-built instances
almost never have: **read-only by default**, writes behind an explicit per-course
allowlist (`leshamblin`) plus confirmation on destructive calls
(`moodler-mcp`), and **token custody** that never puts a Moodle Web Services
token in a shared config. Per-institution output is **configuration plus a
capability manifest**, not a fork: endpoint, enabled tools, course scope, data
residency. `ralph` makes every call auditable, which is what converts this from
a student project into something a DPO signs off.

🔵 **Why it sells.** The per-campus bridges cluster in **LATAM and APAC**, where
institutions build because nobody sells them this; **North America builds none**,
because NA institutions buy integration. So the same artefact is a *cost
reduction* in LATAM/APAC — a day instead of a semester, with governance attached
— and a *product* in NA. **10–12 weeks for the core + 1 week per tenant.**
🔴 Gate with `P551` + `P556` before any row above enters a deliverable.

## 🆕 P562 — The computational course, served from inside the LMS (Global; EMEA/North America first)

**When.** The client teaches anything where the student writes code or runs a
notebook — data science, statistics, engineering, bioinformatics — and the ask is
"put AI in the course". 🔴 **The pedagogical part is not the hard part; serving
500 students a reproducible environment, authenticated out of the LMS, is.** This
pattern is entirely permissive and almost entirely assembly.

**The stack, bottom to top — every piece verified this pass.**

| Layer | Repo | Licence | Role |
|---|---|---|---|
| Compute | [jupyterhub/kubespawner](https://github.com/jupyterhub/kubespawner) | BSD-3-Clause · 611★ | One notebook pod per student, with per-student CPU/RAM limits as config |
| …or, on a cluster | [jupyterhub/batchspawner](https://github.com/jupyterhub/batchspawner) | BSD-3-Clause · 207★ | Spawn into Slurm/PBS/LSF when the client's compute is a research queue |
| …or, for a pilot | [jupyterhub/dockerspawner](https://github.com/jupyterhub/dockerspawner) | BSD-3-Clause · 543★ | One host, Docker, one afternoon |
| Identity | [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | BSD-3-Clause · 73★ | 🔴 **The load-bearing row.** LTI launch from Moodle/Canvas/Brightspace — no second login |
| …or SSO / directory | [jupyterhub/oauthenticator](https://github.com/jupyterhub/oauthenticator) · [ldapauthenticator](https://github.com/jupyterhub/ldapauthenticator) | BSD-3-Clause · 443★ / 214★ | OIDC where the tenant has SSO; LDAP/AD where it has a directory, which in EMEA public-sector estates it does |
| Assignment lifecycle | [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | BSD-3-Clause · 1 370★ | Release, collect, autograde, manual-grade, return |
| …or a full platform | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** · 823★ | Use instead of nbgrader when exercises span programming, modelling and text, and an exam mode is required |
| The agent | any shelf row from [`../agents/top.md`](../agents/top.md) | MIT/Apache-2.0 | Runs **inside the student's own kernel**, so it reads the code they wrote rather than a paraphrase of it |

**Wiring.**
1. Deploy the hub with `kubespawner` (or `batchspawner` on HPC). Pin the image.
2. Register the hub as an **LTI 1.3 tool** in the LMS and configure
   `ltiauthenticator`. 🟢 This is the step that makes it a course rather than a
   demo: the student clicks the assignment in Moodle and lands in their own
   server, already identified.
3. Install `nbgrader` for release/collect/autograde. Keep the autograder
   deterministic — the model never decides the mark.
4. Attach the agent in the kernel with a **read-only** view of the student's
   notebook and an explicit refusal to emit the solution cell. The agent's
   output is a hint and a next step; `nbgrader` produces the grade.
5. Emit xAPI statements to an LRS ([yetanalytics/lrsql](https://github.com/yetanalytics/lrsql),
   Apache-2.0) so engagement and hint-use are measurable rather than anecdotal.

🔴 **Two traps, both measured.** The official JupyterHub deployment tutorial
([`jupyterhub-tutorial`](https://github.com/jupyterhub/jupyterhub-tutorial),
202★) is **archived by its owner** — write your own runbook and do not cite it
to the client. And [`wrapspawner`](https://github.com/jupyterhub/wrapspawner)
(65★), which is what you reach for to let students choose a profile, was last
pushed **2025-08-16**: pin it.

**Why this is the pattern and not a shopping list.** Every row is
BSD-3-Clause or MIT, so the deliverable can be proprietary; the only copyleft in
the picture is the LMS you are *attaching to*, and LTI is a protocol boundary,
not a linkage. 🟢 **The licence question answers itself.**

---

## 🆕 P563 — Adaptive assessment a ministry would accept (LATAM-led, globally applicable)

**When.** The client wants "personalised testing" and the buyer is a ministry, a
board or a university registrar — i.e. somebody who will ask **how the score was
derived**. 🔴 An LLM choosing the next question is not an adaptive test; it is an
unaudited one.

**The stack.**

| Layer | Repo | Licence | Role |
|---|---|---|---|
| Psychometrics | [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** · 153★ | IRT item banks, item selection, ability estimation, stopping rules — **the audited core** |
| Item interchange | [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** · 6★ | QTI 3 items, so the bank outlives the vendor |
| Item *generation* | a shelf agent + the client's curriculum | MIT/Apache-2.0 | Drafts candidate items **into the bank**, never into the exam |
| Curriculum anchor | [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) (Brazil, MIT) · the client's own standard elsewhere | MIT | Each item carries the objective it tests, with provenance |
| Retention | [open-spaced-repetition/fsrs.js](https://github.com/open-spaced-repetition/fsrs.js) | **MIT** · 180★ | Schedules the *review*, which is a different job from scoring |
| Records | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 · 144★ | xAPI statements per response |

**Wiring.** The agent writes items; a human calibrates them; `catsim` selects and
scores; `fsrs.js` schedules the revisit. 🔴 **The line that makes it defensible:
the model is upstream of the item bank and nowhere near the score.** Every
delivered item has IRT parameters estimated from real responses, and the
ability estimate comes from `catsim`, which is 153★ of published method rather
than a prompt.

🟢 **Why LATAM-led.** `catsim`'s author is in Brazil and
[`Dramoscuello/simic`](https://github.com/Dramoscuello/simic) already does the
ICFES Saber 11 shape in Colombia; `bncc-dados` carries **1 721** BNCC objectives
with per-record provenance. 🔵 The region has the exam culture, the standards as
open data and now the psychometrics — which is a stronger starting position than
any other region holds for this pattern.

---

## 🆕 P564 — The transitive-grant answer, retrieved rather than built (run inside `P551`)

**When.** Always, before the deliverable ships — and specifically when `P551`'s
shelf-level licence check has passed and somebody asks the real question:
**what grant does this thing carry once its dependencies are counted?**

🔴 **`Gap 528-C` scoped a dependency-grant enumerator as a build for four
passes. It did not need building.**

| Tool | Licence | Use it when |
|---|---|---|
| [aboutcode-org/scancode-toolkit](https://github.com/aboutcode-org/scancode-toolkit) | **Apache-2.0** (engine) · 🟡 **CC-BY-4.0** (licence datasets) | You need the **evidence**: it detects licences, copyrights, package manifests and **direct dependencies**, and processes manifest and lockfile formats to Package URLs. This is the artefact you hand a client's legal team. |
| [oss-review-toolkit/ort](https://github.com/oss-review-toolkit/ort) | **Apache-2.0** · 2 109★ | You need a **gate in CI**: the *Analyzer* resolves dependencies across package managers, the *Evaluator* runs policy-as-code, and it emits SPDX/CycloneDX plus attribution documents. |
| [anchore/syft](https://github.com/anchore/syft) | **Apache-2.0** · 9 792★ | You need the **deployed artefact's** bill of materials, from the image rather than the source tree. |

**Wiring.** `ort analyze` → `ort evaluate` with a policy that fails on AGPL-3.0
reaching a shipped binary → `scancode` over the same tree for the evidence pack
→ `syft` over the built image, so the claim covers what actually runs.

🔴 **Read `scancode`'s dual grant before redistributing.** The engine is
Apache-2.0; the reference licence data is **CC-BY-4.0**, so shipping the rule set
inside a product carries attribution duties. 🔵 **That is exactly the
"granted, but not under a code licence" band this base opened at `p528`, and it
appears here in the tool you would use to check for it.**

---

## 🆕 P565 — Brightspace, the third LMS (North America first)

**When.** The client runs **D2L Brightspace** — which, in North American higher
education, a large share of them do, and which this base had no agent row for
until this pass.

**The stack.** [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server)
(**MIT, 60★**, npm-published, works against any tenant) for grades, due dates,
assignments, announcements, rosters, syllabus and content · a shelf agent from
[`../agents/top.md`](../agents/top.md) as the reasoning half ·
[`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (**Apache-2.0, 373★**) if
the deliverable must also appear *inside* the LMS as a tool rather than only
beside it · [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) for the
record.

**Wiring.** MCP for the read path and the teacher-facing write path (grades,
comments); LTI 1.3 via `ltijs` for placement and launch; AGS for grade passback
when the tool owns the activity. 🔴 **Do not fork Brightspace** — it is not open
source at all, which makes the API and LTI the *only* boundaries, and therefore
makes this the cleanest of the three LMS patterns rather than the hardest.

🔵 **Parity note, stated because it is the reason this pattern exists:** the
shelf now carries Canvas ([`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp),
MIT, 308★; [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp),
MIT, for the **write** half) and Brightspace, and for Moodle still carries a
**build** (`P553`, `P558`) rather than a row. 🔴 **Moodle — the largest LMS in
the world — remains the one with no credible off-the-shelf bridge**, and that
has now been true across four passes.

---

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

---

## 🆕 P559 — The SIS agent, permissive end to end (the greenfield `p530` found)

**Why this is the pass's best build.** Every bridge field this base has censused
is crowded: Moodle has **222** addresses, Canvas has dozens. Crossing
`topic:student-information-system` with MCP returns **nothing** — and as of
`p530` there is a **permissive** SIS to build it against, so the whole stack can
ship under MIT.

**Components, all verified at `p530`.**

| Role | Component | Grant |
|---|---|---|
| Records core | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 MIT · 409★ · Laravel + Filament |
| Agent surface | an MCP server over Academico's Eloquent models | 🟢 yours |
| Standards bridge | [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | 🟢 Apache-2.0 · LTI launch into the LMS |
| Mastery model | [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | 🟢 MIT · BKT |
| Event sink | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 · xAPI LRS |

**Wiring.**

1. Stand up Academico. Because it is **MIT**, the agent goes **in-process** — a
   Filament panel plus an `artisan` command — instead of the out-of-process
   sidecar every copyleft core forces. This is the step no other records platform
   in this sector permits.
2. Expose a read/write MCP server over the Eloquent models: enrolment, attendance,
   grades, fees. **Scope writes to an explicit allow-list**; advising agents that
   can silently change a grade are the reason institutions refuse them.
3. Launch it inside the institution's existing LMS over **Tsugi** (LTI 1.3), so
   staff meet it where they already work rather than in a second system.
4. Emit every interaction as **xAPI** into `lrsql`. This is the audit trail that
   answers "what did the agent do", and it is the artefact a procurement review
   asks for.
5. Fit **pyBKT** on the attendance + grade history so "this student is at risk"
   is a mastery estimate with a literature behind it, not a model's opinion.

**Grant check (run P556 before quoting).** Academico MIT · Tsugi Apache-2.0 ·
pyBKT MIT · lrsql Apache-2.0 → 🟢 **the union is permissive; the artefact is
shippable.** 🔴 Verify Academico's own `composer.json` tree — Filament is MIT but
the direct-dependency scan is still the engagement's control, not this base's
(`Gap 528-C`).

**Shape:** 8–10 weeks. **Region:** Global; strongest where small and medium
private institutions buy directly rather than through a ministry — **LATAM and
EMEA**.

---

## 🆕 P560 — Grounding a tutor in the institution's own lectures and standards

**The failure this avoids.** A tutor grounded in a general corpus answers
plausibly and off-syllabus, which is precisely the objection faculty raise. The
components to ground it in the institution's *own* material are permissive and
have been in this base's history for twenty passes unused.

| Role | Component | Grant |
|---|---|---|
| Source material | [opencast/opencast](https://github.com/opencast/opencast) | 🟡 ECL-2.0 · lecture capture, 509★ |
| Source → teachable unit | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | 🟢 Apache-2.0 · 462★ · source-backed skills |
| Legacy content bridge | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 MIT · 361★ · SCORM 1.2/2004 runtime |
| Maths marking | [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 Apache-2.0 · CAS-backed e-assessment |
| Retention | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | 🟢 MIT · spaced repetition |
| Event sink | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 |

**Wiring.**

1. Opencast already holds the lectures — most universities running it have years
   of recordings. Pull transcripts from its existing pipeline; **do not build a
   capture system**.
2. Feed transcripts plus the course PDFs through **lineage-skill**, whose output
   is *source-backed*: each generated lesson traces to the material it came from.
   That traceability is the faculty-acceptance argument, so do not substitute a
   generic summariser.
3. Mount the institution's existing SCORM packages through **scorm-again** so the
   tutor can reference and sequence content the institution already licensed.
4. For quantitative subjects, mark with **Numbas** rather than the model.
   Numbas's CAS judges mathematical *equivalence*; an LLM asked to mark algebra
   grades the string. 🔵 This is the single highest-value substitution in the
   recipe.
5. Push mastery events to **lrsql**; schedule review through
   **anki-mcp-server** so the learner keeps the deck when the engagement ends.

**Grant check.** ECL-2.0 (Apache-like, narrowed patent clause) · Apache-2.0 ·
MIT · Apache-2.0 · MIT → 🟢 permissive union. 🟡 ECL-2.0's patent clause is
narrower than Apache-2.0's — flag it in the engagement's legal review; it is not
a trap, but it is not Apache-2.0 either.

**Shape:** 10–12 weeks. **Region:** EMEA first — Opencast and Numbas are both
European-consortium/university projects with existing installed bases there.

---

## 🆕 P561 — The ledger as a billable artefact (productising `Gap 529-A`)

**The insight is `p530`'s own failure.** This base spent ~400 passes
rediscovering addresses it already held, and a **one-file index** surfaced 97
unused permissive components in a single run. A client's engineering
organisation has the same pathology in its own repos, wikis and ADRs.

| Role | Component | Grant |
|---|---|---|
| The compaction | [`../ingest/address-ledger.py`](../ingest/address-ledger.py) | 🟢 this base's |
| Grant resolution | [`../ingest/probe-grant.sh`](../ingest/probe-grant.sh) | 🟢 this base's · 159 filename variants, branch resolved |
| Knowledge tracing of *components*, not learners | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT |

**Wiring.**

1. Point the ledger at the client's own corpus. One row per artefact:
   `address · first_seen · last_verdict · filed_on · last_measured`.
2. Run `probe-grant.sh` over every address for a **grant census**. Expect what
   `p530` found: a minority permissive, a long ungranted tail, and at least one
   licence asserted in a wiki that the repository does not carry.
3. Rank by **distinct mentions without adoption**. That number is the cost of
   rediscovery, and it is the number that justifies the engagement.
4. Put the index **in front of** the process that keeps losing things, not after
   it. 🔴 `p528` named a rewrite as the cause and repaired the symptom; the debt
   recurred one pass later because the control sat downstream.

**Three defects to carry in, each of which cost this base a pass.**
🔴 Case-sensitivity: `LICENSE.txt` ≠ `LICENSE.TXT` — generate variants, never
list them. 🔴 Default branches: **15% of addresses** are not `main`/`master`
(`develop`, `dev`, `mobile`). 🔴 Search excludes forks unless the query says
`fork:true`, and forks are not lesser objects — one was an **IMS-certified**
library.

**Shape:** 3–4 weeks for a first census; the instrument is already written.
**Region:** Global. 🔵 Best sold to organisations with long-lived internal
platform estates — which in this sector means ministries and university systems.

---

## 🆕 P565 — The disconnected classroom, served end to end (LATAM rural, Africa; Global wherever connectivity is assumed away)

🔵 **The engagement this answers.** A ministry or NGO programme where the
deliverable has to work in schools with intermittent power and no reliable
uplink. Every other recipe on this page assumes a reachable model endpoint. This
one does not, and `p532` is the first pass that can name a **permissive server
side** for it.

**Components, all read first-hand this pass:**

| Component | Repo | Grant (title block) | Stars | Role in the recipe |
|---|---|---|---|---|
| Offline server + local assistant | [Crosstalk-Solutions/Project-NOMAD](https://github.com/Crosstalk-Solutions/Project-NOMAD) | 🟢 **Apache-2.0** | **41.3k** | The box. Self-contained offline knowledge/education server, ≈5 GB disk and <1 GB RAM for the server itself, terminal install on Ubuntu 26.04 / 24.04 / Debian 12, **local AI assistant included**. |
| Curriculum + learner model | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 1.2k | The learner-facing half: curriculum structure, progress and offline sync — the part NOMAD does not model. |
| Content studio | [learningequality/studio](https://github.com/learningequality/studio) | 🟢 **MIT** | — | Authoring and channel packaging for the Kolibri side, so a ministry curates its own corpus rather than shipping someone else's. |
| Mastery assessment | [beltromatti/get-it](https://github.com/beltromatti/get-it) | 🟢 **Apache-2.0** | 1.1k | Turns the PDFs a school already has into concept-level mastery maps. 🟡 24-hour hackathon origin — take the architecture, rewrite the shell. |
| Spaced repetition | [open-spaced-repetition/fsrs.js](https://github.com/open-spaced-repetition/fsrs.js) | 🟢 **MIT** | 180 | Scheduling that survives a device being offline for a week. |

**Wiring.**
1. **NOMAD is the deployment unit**, one per school: it already bundles content
   serving plus a local model, so the AI tier has no egress dependency.
2. **Kolibri runs beside it on the same box** and owns the learner model and
   curriculum tree; NOMAD owns the corpus, the tooling and the assistant. Neither
   project duplicates the other's half, which is why the pairing is clean.
3. **`get-it`'s mastery decomposition runs against the school's own PDFs**, with
   the local model as its engine instead of an account-based CLI.
4. **`fsrs.js` schedules review** entirely on-device; nothing in the loop needs a
   round trip.
5. **Sync is Kolibri's**, opportunistic — when an uplink appears, progress leaves
   and curated channels arrive. Treat connectivity as an event, never a
   precondition.

🔴 **The licence reading that makes this shippable.** Apache-2.0 + MIT
throughout, so a studio can ship proprietary extensions on top. 🔵 Contrast the
LMS cores in [`../verticals/solutions.md`](../verticals/solutions.md), which are
almost entirely AGPL/GPL — **the permissive surface in this sector is the
integration and delivery layer, not the platforms**, and that is exactly the
surface this recipe is built on.

**Shape:** 8–10 weeks to a pilot on real hardware; the long pole is **content
curation and teacher training**, not code. 🔴 Budget hardware per school and say
so in the proposal — this is the one recipe on this page with a unit cost.
**Region:** LATAM rural and Africa first; applicable anywhere a client's
connectivity assumption is weaker than the demo's.

---

## 🆕 P566 — One agent, four LMS platforms (Global; North America and EMEA first)

🔵 **The engagement this answers.** A university system or district running
**more than one** LMS — which is the normal case after any merger, federation or
decade of procurement — that wants one assistant across all of them rather than
four integrations.

🟢 **`p532` is the first pass where this recipe is possible**, because the
Blackboard bridge was the missing fourth and it had been sitting in this base's
own history, MIT-licensed, described in eight passes and filed in none.

| Platform | Bridge | Grant (title block) | Stars |
|---|---|---|---|
| **Canvas** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** | 308 |
| **Blackboard Learn** | 🆕 [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | 🟢 **MIT** | 2 |
| **Brightspace (D2L)** | [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | 🟢 **MIT** | 60 |
| **Moodle** | 🆕 [MarcosNahuel/moodle-mcp](https://github.com/MarcosNahuel/moodle-mcp) | 🟢 **MIT** | 1 |

**Wiring.**
1. **Normalise at the tool boundary, not in the agent.** The four servers do not
   share a tool vocabulary — `p528` measured that across the Moodle field alone —
   so define one internal verb set (`list_courses`, `get_roster`,
   `post_announcement`, `read_submissions`, `write_grade`) and adapt each bridge
   to it. This is the actual deliverable; the bridges are upstream.
2. **Run each bridge as its own process** behind that façade, so a platform
   outage degrades one tenant rather than the assistant.
3. **Keep writes behind an approval step.** Grades and placement are exactly what
   NYC's red tier and the EU AI Act's high-risk list cover — see **P548** and the
   `p532` regional table in [`../intel/market.md`](../intel/market.md). Reads can
   be direct; writes are proposals a human confirms.
4. **Adopt `bb-mcp`'s own argument deliberately:** *"the integration logic lives
   here, not in the client."* One façade, many clients.

🔴 **State the maturity honestly in the proposal.** Two of the four bridges are
**1★ and 2★**. These are *correct starting points with a permissive grant*, not
adopted dependencies — the studio **forks and owns** them, and prices that in.
🟢 What the permissive grant buys is the right to do exactly that: `p529`'s
census found the Moodle MCP field's most-visible option is **AGPL-3.0** and its
**52★ ceiling is ungranted**, so forking an MIT 1★ server beats depending on a
copyleft 52★ one.

**Shape:** 6–8 weeks for two platforms, +2 per additional platform once the
façade exists. **Region:** Global; North America and EMEA first, where
multi-LMS estates and Blackboard/Brightspace share are concentrated.
