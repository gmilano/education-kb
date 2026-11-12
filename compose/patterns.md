---
industry: education
region: Global
updated: 2026-11-12
---

# Compose patterns — `p787`

Each recipe names **real, byte-verified repositories**, the grant on each, how they wire together,
and the licensing boundary that keeps client code owned by the client. Grants and `sha`s were read
this pass; see `agents/top.md` and `repos/foundations.md`.

🔴 **The rule that governs every pattern below.** The education platform layer is copyleft. So AI
code lives in one of exactly three places: **(a)** behind an **LTI process boundary**
(`csev/tsugi`, Apache-2.0), **(b)** behind the platform's **web API**, or **(c)** embedded directly —
**only** into a permissive host (Kolibri MIT, Sakai ECL-2.0, OpenOLAT Apache-2.0, nbgrader BSD-3).
Linking proprietary code into Moodle, Open edX, Canvas or Frappe LMS is a licensing decision, not an
implementation detail.

---

## `P787-1` — Defensible AI grading · **North America first, ports to EMEA** · 8–10 weeks

🟢 **The one deliverable that satisfies every jurisdiction that regulates assessment** (`T854`).
Oklahoma bars AI used **solely** for grading; the EU makes final-grade determination Annex III
high-risk. Both are satisfied by the same architecture: **AI proposes, a named human decides, the
system proves it.**

| Component | Address | Grant | Role |
|---|---|---|---|
| Autograding core | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 · `1,512 B` | Release → collect → autograde → **manual review step already in the model** |
| Cohort serving | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3 · `1,475 B` | Multi-user delivery |
| Mastery estimate | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT · `1,105 B` | Bayesian Knowledge Tracing — turns one score into a defensible mastery claim |
| Review loop | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 MIT · `1,072 B` | Stateful graph: propose → flag low-confidence → escalate to human |
| Compliance evidence | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | 🟢 Apache-2.0 · `12,227 B` | Art. 27 FRIA artefacts, decision logs |
| LMS attachment | [`csev/tsugi`](https://github.com/csev/tsugi) | 🟢 Apache-2.0 · `10,273 B` | LTI launch from Moodle / Canvas / Sakai — **no derivative work** |

**Wiring.** nbgrader autogrades → LangGraph scores confidence per item → above threshold, the
proposal queues for the instructor; below it, escalates immediately → the instructor's decision is
the grade of record → OATutor updates mastery → every proposal, evidence pointer and decision-maker
is written to the compliance log → the whole tool launches via Tsugi LTI, so **nothing links to the
LMS**.

🟢 **Why it sells:** "AI never determines a grade" is both the Oklahoma compliance line and the
teacher-trust line. 🔵 Entire stack is BSD/MIT/Apache — no copyleft anywhere in the client's code.

---

## `P787-2` — Offline-first tutor for low-connectivity classrooms · **LATAM + Africa (EMEA)** · 10–12 weeks

🟢 **The only pattern here that works with no reliable internet**, which is the binding constraint
across rural LATAM and much of Africa — and the reason Kolibri's **MIT** grant matters so much.

| Component | Address | Grant | Role |
|---|---|---|---|
| Platform + content + sync | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** · `1,097 B` | Offline-first delivery, curated openly-licensed library, teacher tools, runs on legacy hardware, syncs when a link appears. **MIT ⇒ embed the AI layer directly** |
| Tutoring loop | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 · `11,408 B` | Mastery tracking, retrieval over local materials, practice |
| Mastery model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT · `1,105 B` | BKT — works on-device, no inference call needed to estimate mastery |
| Local inference | Ollama / small open-weight model | 🟢 varies — **verify per model** | On-device generation; no data leaves the school |
| Exercise rendering | [`Khan/perseus`](https://github.com/Khan/perseus) | 🟢 MIT · `1,052 B` | Interactive items without network round-trips |
| Accessibility (MX) | [`ftrujillo36/TutorLSM`](https://github.com/ftrujillo36/TutorLSM) | 🟢 Apache-2.0 · `11,357 B` | Mexican Sign Language practice — a real inclusion component, permissively granted |

**Wiring.** Kolibri is the shell and content store → DeepTutor's tutoring loop runs against
*locally* held material → OATutor's BKT keeps mastery state on-device so a learner progresses with
the link down → Ollama serves generation locally → Perseus renders items → sync pushes mastery and
usage when connectivity returns.

🔵 **Data residency falls out for free**, which pre-answers the governance question LATAM
institutions cannot currently answer (`T855`: `9%` evaluate their AI use).

---

## `P787-3` — Spanish-language admissions-prep agent · **LATAM** · 6–8 weeks

🟢 Built on the artefact that proves this base's own instruments were under-reporting the region
(`T848`): Chile's `paes-mcp`, MIT, `0★`, **licensed in Spanish**.

| Component | Address | Grant | Role |
|---|---|---|---|
| Exam data tool | [`goyanedelv/paes-mcp`](https://github.com/goyanedelv/paes-mcp) | 🟢 MIT (Spanish text) · `2,018 B` | MCP server over an open repository of Chile's **PAES** admission test |
| Agent runtime | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 Apache-2.0 · `11,357 B` | Minimal runtime — this does not need a full graph |
| Tutoring protocol | [`janestreet/agent_skills`](https://github.com/janestreet/agent_skills) → `socratic-tutor/` | 🟢 MIT · `1,120 B` | Diagnostic → skill map 0–5 → one question at a time → spaced review. **Translate the skill, not the code** |
| Institutional tutoring | [`Frangersal/TutoriasITA`](https://github.com/Frangersal/TutoriasITA) | 🟢 MIT · `1,077 B` | Working reference for a LATAM institutional tutoring flow (TecNM) |
| Student records | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 GPL-2.0 · `15,214 B` | SIS with strong Spanish localisation — 🔴 **integrate over its API only, never link** |

**Wiring.** paes-mcp exposes real past-paper items as MCP tools → smolagents drives the session →
the `socratic-tutor` skill supplies the pedagogy, translated to Spanish as a **prompt asset** →
mastery per PAES domain is written back through the RosarioSIS API across a process boundary.

⚠️ **Two cautions.** `paes-mcp`'s MIT text is a **Spanish translation** — valid, but confirm with the
maintainer before building a commercial deliverable on it. And admissions is **Annex III high-risk
in the EU** and regulated in several US states — if this pattern is ever ported out of LATAM, the
prep/decision distinction must be explicit: preparing a candidate is not scoring one.

---

## `P787-4` — EU-sovereign tutoring and assessment layer · **EMEA** · 12–14 weeks

🟢 **Fills the measured gap in `T856`:** Europe has funded the substrate and has not built the
education layer. 🔴 Deadline that sells it: **`2027-12-02`** (Annex III, per Regulation (EU) 2026/1744).

| Component | Address / project | Grant | Role |
|---|---|---|---|
| Permissive EU LMS | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 · `10,982 B` | Swiss-origin university LMS — **permissive, so embed directly** |
| Sovereign model | OpenEuroLLM · GPT-NL · Apertus · Teuken | 🔴 **verify per model** | EU-resident inference. 🔴 Grants were **not** byte-verified this pass — check before committing |
| Tutoring loop | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 · `11,408 B` | The mature tutoring engine; EU-hosted |
| Human-in-loop grading | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 · `1,512 B` | Keeps final-grade determination with a person |
| FRIA evidence | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | 🟢 Apache-2.0 · `12,227 B` | Art. 27 fundamental-rights impact assessment artefacts |
| Interop | [`open-education-api/specification`](https://github.com/open-education-api/specification) | 🟡 EUPL-1.2 · `13,827 B` | OOAPI — courses, offerings, enrolments, results. 🟡 **A standard, not linked code** |
| Lecture capture | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 ECL-2.0 · `11,340 B` | Transcription, chaptering, summarisation |

**Wiring.** OpenOLAT is the host → DeepTutor serves tutoring against an EU-resident model → nbgrader
holds assessment with a human decision-maker → every high-risk decision path emits FRIA evidence
from day one rather than retrofitted → OOAPI carries records between institutional systems →
Opencast feeds lecture material into the tutor's retrieval corpus.

🔴 **Build the compliance artefacts first, not last.** The institution is a **deployer** under the
Act, and a deployer's FRIA cannot be reconstructed after the fact. 🔵 Note also what is **already in
force** and therefore not optional: Art. 5's **emotion-recognition ban in education** (since
`2025-02-02`) and Art. 50 transparency (since `2026-08-02`) — an engagement that defers everything
to 2027 is already non-compliant on both.

---

## `P787-5` — Multi-agent classroom, localised and provenance-labelled · **APAC** · 8–10 weeks

🟢 Takes the region's own strongest permissive asset and adds what its regulation now requires.

| Component | Address | Grant | Role |
|---|---|---|---|
| Classroom generator | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 MIT · `1,065 B` | Topic/document → classroom with AI teacher and classmates: slides, quizzes, simulations, PBL. ⚠️ **Exclude or isolate `packages/mathml2omml` (LGPL-3.0-or-later)** |
| Curriculum skills | [`myvipbackup2/china-k12-teacher-skills`](https://github.com/myvipbackup2/china-k12-teacher-skills) | 🟢 Apache-2.0 · `11,359 B` | Curriculum-aware lesson planning, localised to China K-12 — **the template for localising to another curriculum** |
| Subject depth | [`VeryMath/VeryMath-textbook-copilot`](https://github.com/VeryMath/VeryMath-textbook-copilot) | 🟢 Apache-2.0 · `11,338 B` | Textbook explanations, exercises, knowledge graphs, LaTeX courseware |
| Delivery surface | [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | 🟢 BSD-3 · `2,819 B` | Self-hosted front end over a school-controlled model |
| Provenance | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | 🟢 Apache-2.0 · `12,227 B` | 🔴 **India's amended IT Rules require prominent labels and provenance markers on AI-generated content from `2026-02-20`** — generated courseware is in scope |

**Wiring.** OpenMAIC generates the classroom → the skills pack re-targets it from China K-12 to the
client's curriculum (the pattern to copy for a CBC, CBSE or national curriculum) → VeryMath supplies
subject depth → Open WebUI delivers → every generated artefact carries a provenance label and
origin marker at the point of generation, not as a later pass.

🔴 **Vietnam check:** its 2026-07 rules flag education as high-risk **citing automated assessment**.
If this pattern generates quizzes that *score* students, that is the regulated surface — route
scoring through `P787-1`'s human-in-the-loop design.

---

## `P787-6` — Institutional AI-readiness programme · **LATAM first, portable to all regions** · 4–6 weeks diagnostic + remediation

🟢 **Not a build — the offer that matches the measured deficit** (`T855`). `87%` of LATAM
universities use AI, `26%` have a strategy, `9%` evaluate it; `53%` of Brazilian school
administrators use AI and `22%` have guidelines. 🔴 **There is no regulator to sell against in
Brazil, Mexico or Chile** — so the instrument is institutional risk, not a deadline.

| Component | Address | Grant | Role |
|---|---|---|---|
| Governance scaffold | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | 🟢 Apache-2.0 · `12,227 B` | Policy, logging and assessment artefacts |
| Inventory of actual use | [`Matias-Sanmiguel/teams-facultad-mcp`](https://github.com/Matias-Sanmiguel/teams-facultad-mcp) | 🟢 MIT · `1,088 B` | MCP over Teams Educación — surfaces coursework and announcements, i.e. **where unmanaged AI use already is** |
| External frame | UNESCO Observatory on AI in Education for LAC (launched `2026-04-14`, Santiago) | — | 🔴 Search-channel. Partners include CAF, CENIA, CETIC.br, ECLAC, Tec de Monterrey. **Use its indicators so findings are not merely a vendor's opinion** |
| Offline constraint | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT · `1,097 B` | Where connectivity, not policy, is the real blocker |

**Wiring.** Inventory actual AI use (it is already happening — teachers out-adopt the OECD by ~20
points) → score the institution against UNESCO Observatory indicators → write the policy the `74%`
without a strategy lack → instrument the `91%` that do not evaluate → remediate the highest-risk
surface first, which is assessment, via `P787-1`.

🟢 **Why this lands.** It does not ask an institution to admit it is behind on technology; it offers
to make what it is **already doing** defensible. 🔵 **And it ports:** in EMEA the same programme runs
against the Art. 27 FRIA and `2027-12-02`; in North America against state policy mandates (North
Carolina `2026-12-31`); in APAC against India's provenance rules and Vietnam's high-risk listing.

---

## `P787-7` — The grant gate · **Global** · a probe, not a document

🟢 **`ACTION p786-A` discharged.** `p786` specified this gate as a *record*; this pass made it the
*probe*, and it caught three defects in its own instrument before any verdict shipped (`T857`).

**Run it before writing any repository into this base, or into a client shortlist:**

1. **Existence** — `git ls-remote https://github.com/$OWNER/$REPO HEAD`, with the **exit status read
   directly**. 🔴 Never pipe it into `head`; you will read `head`'s status and every negative control
   will pass.
2. **Fetch the licence bytes** — `raw.githubusercontent.com/$OWNER/$REPO/{main,master,develop}/` over
   `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license.txt`, `COPYING`, `COPYING.txt`, `LICENCE`,
   `LICENSE-MIT`. **Case and spelling vary** (`T842`).
3. **Match appendix-bearing licences FIRST** — **EUPL-1.2** and **CeCILL** name other licences in
   their compatibility lists, so any family check run before them claims the wrong one (`T849`).
4. **Decide copyleft family on the TITLE LINE only** — 🔴 **GPL-3.0 §13 names the Affero licence**, so
   a whole-file grep grades Moodle as AGPL. Also catch the line-3 deferral (`T847`).
5. **Grade MIT on its four clauses, in four languages** — *permission granted · substantial portions ·
   without warranty · in no event shall*, matched in **English, Spanish, Portuguese and French**, and
   report a translation as `MIT(translated)` (`T848`).
6. 🔴 **Never use byte length as an integrity signal** (`T845`). A `1,002 B` file can contain none of
   MIT's clauses while a `1,061 B` file contains all four.
7. **Run known-good and planted-negative controls BEFORE trusting any verdict** — 🟢 every one of the
   five recorded failure modes was found by a control, none by inspection.
8. **A repo-level grant is not a dependency audit** — OpenMAIC is MIT with an LGPL-3.0-or-later
   workspace package inside it.
