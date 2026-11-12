---
industry: education
region: Global
updated: 2026-11-12
---

# Compose patterns — `p788`

Each recipe names **real, byte-verified repositories**, the grant on each, how they wire together,
and the licensing boundary that keeps client code owned by the client. Grants and `sha`s were read
this pass; see `agents/top.md` and `repos/foundations.md`.

🔴 **Rule 1, carried.** The education platform layer is copyleft. AI code lives in exactly three
places: **(a)** behind an **LTI process boundary** (`csev/tsugi`, Apache-2.0), **(b)** behind the
platform's **web API or an MCP server over it**, or **(c)** embedded directly — **only** into a
permissive host.

🔴 **Rule 2, NEW this pass (`T861`).** A permissive host is necessary but **not sufficient** for (c).
Its **dependencies** must be read too. 🟢 Audited clean to the first layer: `jupyter/nbgrader`
(`0` of `18`), `CAHLR/OATutor` (`0` of `43`). 🟡 Usable with care: `learningequality/kolibri`
(`2` LGPL of `32`). 🔴 **Not embeddable as-is: `oppia/oppia`, whose `angular-shepherd` dependency is
AGPL-3.0.**

🔴 **Rule 3, NEW this pass (`T864`).** In education the **content** has a rights-holder and the
repository is the cheap part. A permissive grant over a wrapper is not a grant over the exam papers,
textbooks or statutes inside it. **Read the scope clause; ask who owns the content.**

---

## `P788-1` — Defensible AI grading, with the audit trail finally supplied · **North America first; ports to EMEA and Korea** · 8–10 weeks

🟢 **The one deliverable that satisfies every jurisdiction that regulates assessment** (`T854`).
Oklahoma bars AI used **solely** for grading; the EU makes final-grade determination Annex III
high-risk; **Korea's AI Basic Act has named education high-impact since `2026-01-22`** (`T866`).
All three are satisfied by one architecture: **AI proposes, a named human decides, the system proves
it.**

| Component | Address | Grant | Deps | Role |
|---|---|---|---|---|
| Autograding core | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 · `1,512 B` | 🟢 `0`/`18` | Release → collect → autograde → **manual review step already in the model** |
| Cohort serving | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3 · `1,475 B` | — | Multi-user delivery |
| Mastery estimate | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT · `1,105 B` | 🟢 `0`/`43` | Bayesian Knowledge Tracing — turns one score into a defensible mastery claim |
| **Audit trail** `NEW` | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | 🟢 **MIT** · `1,070 B` | — | 🟢 **The piece this pattern was missing.** A real **xAPI Learning Record Store** — every proposal, evidence pointer and decision-maker stored as a validated statement rather than in a hand-rolled table |
| Statement validation `NEW` | [`LearningLocker/xapi-validation`](https://github.com/LearningLocker/xapi-validation) | 🟢 **MIT** · `1,070 B` | — | Rejects malformed records at write time, so the trail is admissible later |
| Review loop | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 MIT · `1,072 B` | — | Stateful graph: propose → flag low-confidence → escalate to human |
| Compliance evidence | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | 🟢 Apache-2.0 · `12,227 B` | — | Art. 27 FRIA artefacts; Korea impact-assessment artefacts |
| LMS attachment | [`csev/tsugi`](https://github.com/csev/tsugi) | 🟢 Apache-2.0 · `10,273 B` | — | LTI launch from Moodle / Canvas / Sakai — **no derivative work** |
| D2L attachment `NEW` | [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | 🟢 **MIT** · `1,200 B` | — | 🟢 For the third major North American LMS, which this base previously could not reach |

**Wiring.** nbgrader autogrades → LangGraph scores confidence per item → above threshold the
proposal queues for the instructor, below it escalates immediately → **the instructor's decision is
the grade of record** → OATutor updates mastery → every proposal, evidence pointer and decision-maker
is written as a **validated xAPI statement** to the record store → the tool launches via Tsugi LTI
(or the D2L MCP server), so **nothing links to the LMS**.

🟢 **Why it sells:** "AI never determines a grade" is simultaneously the Oklahoma compliance line,
the EU Annex III posture, the Korean impact-assessment answer and the teacher-trust line.
🟢 **And the whole stack is BSD/MIT/Apache with the two load-bearing components audited clean to
the first dependency layer** — which, after `T861`, is a claim worth making explicitly.

---

## `P788-2` — Offline-first tutor for low-connectivity classrooms · **LATAM + Africa (EMEA)** · 10–12 weeks

🟢 **The only pattern here that works with no reliable internet.** 🔴 **Amended this pass:** Kolibri
remains the right host, but its two LGPL dependencies must be handled, and this pass adds a real
African ecosystem to build with rather than around.

| Component | Address | Grant | Role |
|---|---|---|---|
| Platform + content + sync | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** · `1,097 B` | Offline-first delivery, curated openly-licensed library, teacher tools, legacy hardware, syncs when a link appears. ⚠️ **`zeroconf-py2compat` and `json-schema-validator` are LGPL** — keep them dynamically linked and replaceable, with source available |
| **Content delivery without an app store** `NEW` | [`elimu-ai/appstore`](https://github.com/elimu-ai/appstore) · [`elimu-ai/launcher`](https://github.com/elimu-ai/launcher) | 🟢 **MIT** · `1,065 B` | 🟢 On-device APK download/install/update and a launcher that constrains the tablet to one instructional path — **built for exactly this constraint, in East Africa, and permissive** |
| **Reading-level model** `NEW` | [`elimu-ai/ml-storybook-reading-level`](https://github.com/elimu-ai/ml-storybook-reading-level) · [`ml-storybook-recommender`](https://github.com/elimu-ai/ml-storybook-recommender) | 🟢 **MIT** · `1,065 B` | 🟢 **Permissive ML for levelling and recommending storybooks** — no other row in this base supplies a levelling model, and this one runs without a network |
| Tutoring loop | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 · `11,408 B` | Mastery tracking, retrieval over local materials, practice. ⚠️ **`pyte` is LGPL-3.0 — check whether the tutoring path needs it at all** |
| Mastery model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT · `1,105 B` | BKT on-device; no inference call needed to estimate mastery. 🟢 `0`/`43` copyleft deps |
| Local inference | Ollama / small open-weight model | 🟢 varies — **verify per model** | On-device generation; no data leaves the school |
| Exercise rendering | [`Khan/perseus`](https://github.com/Khan/perseus) | 🟢 MIT · `1,052 B` | Interactive items without network round-trips |
| Handwriting / maths input `NEW` | [`MyScript/MyScriptJS`](https://github.com/MyScript/MyScriptJS) | 🟢 **Apache-2.0 (by ref)** · `570 B` | 🟢 Pen input for maths on a tablet — the natural input mode where keyboards are not |
| Accessibility (MX) | [`ftrujillo36/TutorLSM`](https://github.com/ftrujillo36/TutorLSM) | 🟢 Apache-2.0 · `11,357 B` | Mexican Sign Language practice — real inclusion, permissively granted |
| Baseline survey `NEW` | [`getodk/collect`](https://github.com/getodk/collect) | 🟢 Apache-2.0 · `10,494 B` | Offline data collection for the pre/post measurement a funder will ask for |

**Wiring.** Kolibri is the shell and content store → elimu-ai's launcher and appstore handle device
provisioning and content updates where there is no Play Store → the reading-level model grades the
local library, so the tutor recommends at the learner's level **without an inference call** →
DeepTutor's loop runs against locally held material → OATutor's BKT keeps mastery on-device so a
learner progresses with the link down → Ollama serves generation locally → Perseus renders items and
MyScriptJS accepts pen input → ODK Collect captures baseline and endline → sync pushes everything
when connectivity returns.

🔵 **Data residency falls out for free**, which pre-answers the governance question LATAM and African
institutions cannot currently answer (`T855`: `9%` evaluate their AI use).

---

## `P788-3` — Spanish-language admissions-prep agent · **LATAM** · 6–8 weeks

🔴 **This pattern is REPAIRED, not carried.** `P787-3` was built on `goyanedelv/paes-mcp` as though
Chile's PAES corpus were MIT. 🔴 **It is not (`T864`):** the MIT grant covers **the source code and
documentation only**, and the licence says in terms that it does not — and could not — cover the
PAES stems, figures and answer keys, whose rights belong to **DEMRE, Universidad de Chile**. That
material is included from freely published official sources, for educational use, with attribution.

| Component | Address | Grant | Role |
|---|---|---|---|
| Exam access tool | [`goyanedelv/paes-mcp`](https://github.com/goyanedelv/paes-mcp) | 🟢 MIT (Spanish text) · `2,018 B` · 🔴 **SCOPE-LIMITED** | MCP server over Chile's **PAES**. 🟢 **The code is yours to build on; the items are DEMRE's.** Use it to *reach* officially published material, with attribution — not as a corpus you own |
| Agent runtime | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 Apache-2.0 · `11,357 B` | Minimal runtime — this does not need a full graph |
| Tutoring protocol | [`nuwaves/socratic-tutor`](https://github.com/nuwaves/socratic-tutor) | 🟢 **MIT** · `1,143 B` | 🟢 **New and better suited than last pass's choice:** the Socratic skill already extracted as a standalone installable unit with saved progress. **Translate the skill, not the code** |
| Institutional reference | [`Frangersal/TutoriasITA`](https://github.com/Frangersal/TutoriasITA) | 🟢 MIT · `1,077 B` | A working LATAM institutional tutoring flow (TecNM) |
| Mastery record | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | 🟢 **MIT** · `1,070 B` | Per-domain mastery as validated xAPI statements |
| Student records | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 GPL-2.0 · `15,214 B` | SIS with strong Spanish localisation — 🔴 **integrate over its API only, never link** |

**Wiring.** paes-mcp exposes officially published past-paper material as MCP tools, **with DEMRE
attribution carried through to anything the learner sees** → smolagents drives the session → the
`socratic-tutor` skill supplies the pedagogy, translated to Spanish as a **prompt asset** → mastery
per PAES domain is written as xAPI statements → pushed back through the RosarioSIS API across a
process boundary.

🔴 **Three cautions, one of them new.** (1) **The exam content is not licensed to you** — a
commercial deliverable needs a conversation with DEMRE, and this is the general case in education,
not a quirk (`T864`). (2) `paes-mcp`'s MIT text is a **Spanish translation** — valid, but confirm
with the maintainer. (3) Admissions is **Annex III high-risk in the EU**, **high-impact in Korea**
and regulated in several US states — if this pattern is ported, the prep/decision distinction must
be explicit: **preparing a candidate is not scoring one.**

---

## `P788-4` — EU-sovereign tutoring and assessment layer, built with European components · **EMEA** · 12–14 weeks

🔴 **Rewritten.** `P787-4` was premised on `T856` — that Europe had funded the substrate and built
no education layer. 🟢 **`T862` refutes that:** the European layer exists, it is permissive, and it
was invisible only because the queries were in English. The pattern is now **European components on
European models**, not foreign components on European models.

🔴 **The deadline that sells it: `2027-12-02`** (Annex III, per Regulation (EU) 2026/1744). 🔴 **And
what is already in force and therefore not optional:** Art. 5's **emotion-recognition ban in
education** (since `2025-02-02`) and Art. 50 transparency (since `2026-08-02`).

| Component | Address / project | Grant | Role |
|---|---|---|---|
| Permissive EU LMS | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 · `10,982 B` | Swiss-origin university LMS — permissive, so embed directly |
| **EU agent/skill layer** `NEW` | [`onderwijsin/agents`](https://github.com/onderwijsin/agents) | 🟢 **MIT** · `1,079 B` | 🟢 **The Dutch education plugin-and-skill collection whose absence this base had recorded as fact.** Provider-agnostic, so it survives a change of sovereign model |
| **Citation-grounded tutor** `NEW` | [`SeydinaBANE/sherpa`](https://github.com/SeydinaBANE/sherpa) | 🟢 **MIT** · `1,063 B` | 🟢 **Grounded RAG with citations** — provenance as an architectural property. 🔵 The direct technical answer to `T859`, where a national AI policy was withdrawn for citing invented sources |
| Sovereign model | OpenEuroLLM · GPT-NL · Apertus · Teuken · Mistral | 🔴 **verify per model** | EU-resident inference. 🔴 Grants **not** byte-verified this pass — check before committing |
| Human-in-loop grading | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 · `1,512 B` | Keeps final-grade determination with a person. 🟢 `0`/`18` copyleft deps |
| Audit trail | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | 🟢 **MIT** · `1,070 B` | The Art. 27 evidence has to live somewhere auditable |
| FRIA evidence | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | 🟢 Apache-2.0 · `12,227 B` | Fundamental-rights impact assessment artefacts |
| **EU data vocabulary** `NEW` | [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) | 🟡 EUPL-1.2 · `13,865 B` | 🟢 **The European Commission's own** learning and credential model — the vocabulary a public-sector client will be asked to speak. 🟡 A standard, not linked code |
| Interop | [`open-education-api/specification`](https://github.com/open-education-api/specification) | 🟡 EUPL-1.2 · `13,827 B` | OOAPI — courses, offerings, enrolments, results |
| Lecture capture | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 ECL-2.0 · `11,340 B` | Transcription, chaptering, summarisation into the tutor's corpus |
| Classroom language | [`hedyorg/hedy`](https://github.com/hedyorg/hedy) | 🟡 EUPL-1.2 · `13,827 B` | Gradual programming language, `1,697★` |

**Wiring.** OpenOLAT is the host → `onderwijsin/agents` supplies the education skill layer →
`sherpa`'s citation-grounded retrieval answers learner questions **with sources attached** → an
EU-resident model serves inference → nbgrader holds assessment with a named human decision-maker →
every high-risk decision path emits FRIA evidence **from day one rather than retrofitted**, stored
as validated xAPI → OOAPI and the European Learning Model carry records between institutional
systems → Opencast feeds lecture material into retrieval.

🔵 **Two European artefacts to ask for rather than build.**
🔴 [`silja-graf/Didaktikus-…-LP21`](https://github.com/silja-graf/Didaktikus-KI-Spezialist-f-r-Unterrichtsplanung-und-Beurteilung-nach-LP21)
is a **Swiss LP21-curriculum** lesson-planning and assessment agent — the most engagement-shaped
EMEA artefact found this pass — **and it carries no licence**. So does
🔴 [`lehrer-tools/lehrer-agent`](https://github.com/lehrer-tools/lehrer-agent) (🇩🇪). 🟢 **An upstream
licence request is cheaper than rebuilding either**, and `Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider`
is worth the same request: it bridges the permissive LMS to the permissive record store.

---

## `P788-5` — Multi-agent classroom, localised and provenance-labelled · **APAC** · 8–10 weeks

🟢 Takes the region's strongest permissive asset and adds what its regulation now requires.
🔴 **Amended twice this pass:** Korea now binds education (`T866`), and the obvious India shortcut is
a licensing trap (`T868`).

| Component | Address | Grant | Role |
|---|---|---|---|
| Classroom generator | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 MIT · `1,065 B` | Topic/document → classroom with AI teacher and classmates: slides, quizzes, simulations, PBL. ⚠️ **Exclude or isolate `mathml2omml` (LGPL-3.0-or-later), and ELECT the MIT arm of `jszip` (`MIT OR GPL-3.0-or-later`) in writing** |
| Curriculum skills | [`myvipbackup2/china-k12-teacher-skills`](https://github.com/myvipbackup2/china-k12-teacher-skills) | 🟢 Apache-2.0 · `11,359 B` | Curriculum-aware lesson planning, localised to China K-12 — **the template for re-targeting a curriculum** |
| India curriculum reference | [`praj2408/RAG-Enhanced-NCERT-Tutor`](https://github.com/praj2408/RAG-Enhanced-NCERT-Tutor) · [`mandarab76/CBSE_Home-Tutor`](https://github.com/mandarab76/CBSE_Home-Tutor) | 🟢 MIT · `1,072 B` / `1,077 B` | 🟢 **NCERT and CBSE retrieval tutors under MIT** — the permissive India layer `p787` recorded as missing |
| India school data | [`gsidhu/udise-district-dump`](https://github.com/gsidhu/udise-district-dump) | 🟢 MIT · `1,075 B` | **UDISE** school census — district-level targeting for a national programme |
| Knowledge-graph tutoring | [`qiyuxi24/AI-tutor`](https://github.com/qiyuxi24/AI-tutor) | 🟢 MIT · `1,065 B` | Knowledge map + learning path + learner profile + question generation, with `413` test cases and L1–L4 live-API evaluation — **the evaluation harness this pattern otherwise lacks** |
| Korea delivery | [`jungtaejin/spring-ai-tutor`](https://github.com/jungtaejin/spring-ai-tutor) | 🟢 MIT · `1,069 B` | 🟢 Spring AI tutoring API — structured output, memory, tool calling, SSE. **The JVM stack a Korean enterprise client already runs** |
| Subject depth | [`VeryMath/VeryMath-textbook-copilot`](https://github.com/VeryMath/VeryMath-textbook-copilot) | 🟢 Apache-2.0 · `11,338 B` | Textbook explanations, exercises, knowledge graphs, LaTeX courseware |
| Delivery surface | [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | 🟢 BSD-3 · `2,819 B` | Self-hosted front end over a school-controlled model |
| Provenance + impact assessment | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | 🟢 Apache-2.0 · `12,227 B` | 🔴 **India's amended IT Rules require prominent labels and provenance markers on AI-generated content from `2026-02-20`** — generated courseware is in scope. 🔴 **Korea's AI Basic Act requires transparency and impact assessment for high-impact AI, and education is named** |

**Wiring.** OpenMAIC generates the classroom → the China K-12 skills pack is the template for
re-targeting to NCERT/CBSE, a Korean curriculum or Kenya's CBC → the NCERT/CBSE MIT tutors supply
India-specific retrieval → `qiyuxi24/AI-tutor`'s evaluation harness measures whether the
localisation actually works → Open WebUI or the Spring AI service delivers → **every generated
artefact carries a provenance label and origin marker at the point of generation, not as a later
pass.**

🔴 **The India trap, stated plainly (`T868`).** [`dpaul0501/OpenVidya`](https://github.com/dpaul0501/OpenVidya)
*is* OpenMAIC already redesigned for NCERT/CBSE — and it is **AGPL-3.0** where OpenMAIC is MIT. MIT
permits that relicensing, and the consequence is that the ready-made localisation **cannot be
embedded in a client deliverable the way its parent can.** 🟢 **Localise from the MIT parent
yourself; read it for reference, do not vendor it.**

🔴 **Regulatory routing.** Korea (in force now) and Vietnam (automated assessment) both make scoring
the regulated surface. **If this pattern generates quizzes that *score* students, route scoring
through `P788-1`'s human-in-the-loop design.**

---

## `P788-6` — Institutional AI-readiness programme · **LATAM first, portable to all regions** · 4–6 weeks diagnostic + remediation

🟢 **Not a build — the offer that matches the measured deficit** (`T855`). `87%` of LATAM
universities use AI, `26%` have a strategy, `9%` evaluate it; `53%` of Brazilian school
administrators use AI and `22%` have guidelines; **>`50%` of teachers in Chile and Brazil already
use AI against <`10%` of institutions with guidelines.** 🔴 **There is no education-specific
regulator to sell against in Brazil, Mexico or Chile** — so the instrument is institutional risk.

| Component | Address | Grant | Role |
|---|---|---|---|
| Governance scaffold | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | 🟢 Apache-2.0 · `12,227 B` | Policy, logging and assessment artefacts |
| Inventory of actual use | [`Matias-Sanmiguel/teams-facultad-mcp`](https://github.com/Matias-Sanmiguel/teams-facultad-mcp) | 🟢 MIT · `1,088 B` | MCP over Teams Educación — surfaces **where unmanaged AI use already is** |
| **Measurement instrument** `NEW` | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) + [`xapi-validation`](https://github.com/LearningLocker/xapi-validation) | 🟢 **MIT** · `1,070 B` | 🟢 **Instrumenting the `91%` who do not evaluate requires somewhere to put the evidence.** This is it, and it is permissive |
| **Field survey** `NEW` | [`getodk/collect`](https://github.com/getodk/collect) | 🟢 Apache-2.0 · `10,494 B` | Offline baseline and endline data collection — works where the institution's connectivity does not |
| External frame | UNESCO Observatory on AI in Education for LAC (launched `2026-04-14`, Santiago) | — | 🔴 Search-channel. Partners include CAF, CENIA, CETIC.br, ECLAC, Tec de Monterrey, Fundación Ceibal, IRCAI. **Use its indicators so findings are not merely a vendor's opinion** |
| Offline constraint | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT · `1,097 B` | Where connectivity, not policy, is the real blocker |

**Wiring.** Inventory actual AI use (it is already happening — teachers out-adopt the OECD by ~20
points) → score the institution against UNESCO Observatory indicators → collect baseline evidence
with ODK where systems cannot → write the policy the `74%` without a strategy lack → **instrument
the `91%` that do not evaluate, using the xAPI record store so "we measured it" is a record rather
than a claim** → remediate the highest-risk surface first, which is assessment, via `P788-1`.

🟢 **Why this lands.** It does not ask an institution to admit it is behind on technology; it offers
to make what it is **already doing** defensible. 🔵 **And it ports:** in EMEA against the Art. 27
FRIA and `2027-12-02`; in **Korea against the AI Basic Act's in-force impact-assessment duty**; in
North America against state mandates (Maryland SB 720/HB 1057, Ohio, North Carolina `2026-12-31`);
in India against provenance labelling.

---

## `P788-7` — The grant gate · **Global** · a probe, not a document

🟢 **Committed as `ingest/p788-grant-gate.sh`, with `--controls`.** Run it before writing any
repository into this base or into a client shortlist. 🔴 **Ten rules, four of them added this pass
because this pass's own controls caught six defects in its own instruments** (`T863`).

1. **Existence** — `git ls-remote https://github.com/$OWNER/$REPO HEAD`, with the **exit status read
   directly**. 🔴 Never pipe it; you will read `head`'s status and every negative control will pass.
2. **Fetch licence bytes** over `{main,master,develop}` × `LICENSE`, `LICENSE.md`, `LICENSE.txt`,
   `license`, `license.txt`, `COPYING`, `COPYING.txt`, **`LICENCE`**, `LICENCE.md`, `LICENSE-MIT`.
   🔵 Case **and spelling** vary — `jkbrzt/rrule` serves the **British** `LICENCE`.
3. **Match appendix-bearing licences FIRST** — **EUPL-1.2** and **CeCILL** name other licences in
   their compatibility lists, so any family check run before them claims the wrong one (`T849`).
4. 🔴 **NEW — find the title by SCANNING for a line that IS a licence title, at any depth.** A fixed
   window is the wrong instrument: Odoo defers to line 3, `INGInious` to line 9 behind a prose scope
   caveat, and the next file will exceed whatever budget you choose. 🟢 Anchoring on a line that *is*
   a title still excludes **GPL-3.0 §13's prose mention of Affero**, which is never a line of its own.
5. 🔴 **NEW — grade abbreviations as titles.** `frappe/education` serves **19 bytes**:
   `License: GNU GPL V3`. Matching only expanded names scores a real grant `UNGRADED`.
6. **Grade MIT on its four clauses in four languages**, and **match each clause as a SET of
   circulating renderings** — 🔴 **NEW: `paes-mcp` says `partes sustanciales` where the `T848` fix
   required `porciones sustanciales`, so the repaired probe still failed.** Report a translation as
   `MIT(translated:xx)`.
7. 🔴 **NEW — never let an accent decide a verdict.** `grep` matches bytes: `SIN GARANT.A` cannot
   match `SIN GARANTÍA`, because `Í` is two bytes. Keep patterns ASCII up to the first accent and
   declare the locale.
8. **Recognise a grant BY REFERENCE.** The standard Apache short notice is a real grant and it is
   `570 B` long. 🔴 **Never use byte length as an integrity signal** (`T845`) — this base filed
   `MyScript/MyScriptJS` as a "proprietary notice" because the file was short.
9. 🔴 **NEW — measure bytes ON THE FILE.** `$(curl …)` strips the trailing newline and under-reports
   every licence by exactly `1 B`.
10. 🔴 **NEW — report a SCOPE LIMITATION and a SPLIT, rather than a family.** A grant that excludes
    part of the repository (`paes-mcp`, `Dirigo`, `INGInious`) or differs by directory (`metabase`)
    is not described by a family name, and the boundary is the fact (`T864`).

🟢 **And two rules about the method rather than the bytes.**
**Run known-good and planted-negative controls BEFORE trusting any verdict** — all thirteen recorded
failure modes were found by a control on a row this base had already published, and **none by
inspection**. 🔴 **A repo-level grant is not a dependency audit** — run
`ingest/p788-dep-audit.py` (`T861`), and remember it reads the **first layer only**.

---

## `P788-8` — The discovery gate · **Global** · new this pass

🔴 **NEW, and it exists because `T862` cost this base a whole region.** `p787` recorded EMEA as
having no education agents. The agents were there; the queries were in English.

**Before recording any regional absence:**

1. **Query in the region's language**, not in English about the region.
   `tutor education AI … Netherlands` → **`0`**. `onderwijs AI agent` → **`1`**, MIT.
2. **Query the region's own curriculum vocabulary** — `NCERT`, `CBSE`, `PAES`, `LP21`, `CBC`, `Bac`,
   `UDISE`. `tutor agent education India curriculum` → **`0`**. `NCERT AI` → **`330`**.
3. 🔴 **Check whether the word means two things.** Korean **교육** is both *education* and *corporate
   training*, so the obvious query returns agent-training **course material**. **학습** (*learning*)
   returned the real head.
4. **Use NO star floor.** The row that refuted `T856` has `0★`; so do three of the five French and
   Dutch finds. A star floor under-reports every non-English region (`T837`).
5. **Check the base's own files before declaring an absence.** `elimu-ai` — `66` MIT repositories —
   was cited at `agents/trending.md:24964` and never placed.
6. 🟢 **Two addresses with the same `HEAD` sha are ONE project** (`T865`). Cheap, needs no page read,
   and it caught this base double-counting one German repo as two rows.
7. **If the slot really is empty, say so in the region's own terms and show the queries.** Japan is
   a genuine gap: `AI 教育 エージェント` → **`3`**, best artefact ungranted. 🟢 **That is a finding.
   Silence is not.**
