---
industry: education
region: Global
updated: 2026-10-14
---

## Pass 201 — 2026-10-14 — RECIPES FROM THIS PASS'S VERIFIED COMPONENTS

🔵 **Every repo named below had its default branch resolved by `git ls-remote --symref` and its
licence read from its own blob this hour**, then cross-checked against the KB's shared
`family_of` *(`65`/`65` agreement)*. 🟢 **Licences are inline because in education the licence
decides whether a pattern can ship at all** — and this pass found a permissive option at every
layer where p200 had copyleft only.

### 🔴 P201-1 — Grading modernisation: EXTEND, do not build *(North America / EMEA, 6–8 wks)*

🔴 **This pattern exists to retire p200's advice to build a grader.**

| step | component | licence *(blob, bytes)* | why this one |
|---|---|---|---|
| 1. base platform | [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) *(branch `develop`)* | 🟢 **MIT** · `1 091` B | Already carries `gen-ai` **and** `text-exercises`; exam mode; `396` forks; a university runs it in production |
| 2. or, if TA workflow dominates | [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | 🟢 **BSD-3-Clause** · `1 542` B | Automated **and** TA grading in one system; `1 109` forks |
| 3. execution sandbox | [`autolab/Tango`](https://github.com/autolab/Tango) | Apache-2.0 *(API field; not blob-read this pass)* | Standalone REST autograding service — isolates untrusted student code |
| 4. notebook lane | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** · `1 560` B | Python **and R**; pairs with `jameskermode/mograder` (**MIT**) for Marimo |
| 5. 🟢 **the part you actually build** | LLM free-text feedback behind Artemis's feedback interface, with every suggestion written to an append-only record | — | 🟢 **The ONLY genuine white space measured on this shelf** |
| 6. audit trail | `ralph` xAPI store *(KB row)* + the `aiact-50-2-*` marking instruments in [`compose/code/`](code/) | — | 🔵 Suites run `427`/`427` this pass, so the gate is executable here |

🟢 **Wiring:** Artemis exercise → Tango sandbox for code, LLM reviewer for prose → **both write a
statement to `ralph` before the grade is shown** → human confirms. 🔴 **Hard rule: the LLM
proposes, a human disposes, and the record shows which.** That is literally the requirement
Oklahoma, Maryland, Colorado, Texas, the EU AI Act, Vietnam and Australia converge on.
🔵 **Licence gate:** Artemis MIT and Submitty BSD-3 are both safe for a closed deliverable;
🔴 **do NOT start from `INGInious` (AGPL-3.0) for a hosted engagement** however good its LTI is.

### 🟢 P201-2 — The LATAM corpus tutor: wire `60 000★` of curriculum to an agent *(LATAM, 5–7 wks)*

🟢 **The region's open-source output is corpus, not platform — so build the platform-shaped half
and keep the corpus as data.**

| step | component | licence | role |
|---|---|---|---|
| 1. corpus | [`Universidade-Livre/ciencia-da-computacao`](https://github.com/Universidade-Livre/ciencia-da-computacao) `20 921★` · [`mouredev/Hello-Python`](https://github.com/mouredev/Hello-Python) `37 754★` · [`Universidade-Livre/matematica`](https://github.com/Universidade-Livre/matematica) `1 417★` · [`natayadev/dataengineering-roadmap`](https://github.com/natayadev/dataengineering-roadmap) `903★` | 🔴 **READ EACH LICENCE FIRST** — content repos are where `CC-BY-NC-*` lives *(p200 found `NonCommercial` on a curriculum row)*; none was blob-read this pass | Spanish/Portuguese curriculum, already structured as learning paths |
| 2. pedagogy engine | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** · `1 073` B | BKT mastery estimation behind an MCP tool call, in Go |
| 3. memory | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🟢 **MIT** · `1 074` B | Spaced repetition as tool calls — no scheduler to write |
| 4. delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** · `1 097` B | Offline-first; the region's connectivity reality |
| 5. public data | [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | 🟢 **MIT** · `1 072` B | `70` Brazilian public APIs for enrolment/census context *(Brazil engagements)* |

🟢 **Wiring:** ingest a curriculum repo's markdown tree as the syllabus graph → `tutor-mcp`
holds mastery per node → the LLM only renders explanation and quizzes → `anki-mcp-server`
schedules review → Kolibri serves it offline. 🔵 **Every piece MIT, so the deliverable can be
closed** — 🔴 **except the corpus, whose licence is the one thing this recipe must check per
repo.**

### 🟢 P201-3 — Moodle-side tutoring and deadline agent *(LATAM / EMEA, 6–8 wks)*

🔵 **Carried from p200 and upgraded with this pass's reads.** Moodle is **GPL-3.0** (`35 147` B)
and Chamilo is 🆕 **GPL-3.0-or-later** — **integrate over Web Services, never fork into a closed
deliverable.** 🟢 Add the `8` Moodle MCP servers p200 enumerated **minus the `3` that grant
nothing** *(`loyaniu/moodle-mcp`, `haanhtuandev/vgu-mcp` and one declaring MIT with no grant)*,
with [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) (**MIT**) as the
tool layer. 🟢 Put [`Selleo/mentingo`](https://github.com/Selleo/mentingo) (**MIT**, SCORM +
xAPI) beside it when the client wants **new** courseware in a closed deliverable rather than
Moodle extension — **that is the option p200's table did not have.**

### 🟡 P201-4 — Lecture capture to searchable, cited video *(EMEA, 8–10 wks)*

| step | component | licence *(blob, bytes)* |
|---|---|---|
| 1. capture + distribution | [`opencast/opencast`](https://github.com/opencast/opencast) *(branch `develop`)* | 🟡 **ECL-2.0** · `11 340` B |
| 2. player | [`polimediaupv/paella`](https://github.com/polimediaupv/paella) *(branch `develop`)* + [`paella-core`](https://github.com/polimediaupv/paella-core) | 🟢 **ECL-2.0** · `9 915` B — 🆕 **grant FOUND this pass at lowercase `license.txt`**; `paella-core` byte-identical |
| 3. transcription + index | local Whisper + a vector store | per component |
| 4. tutor over the lecture | [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) pattern | 🟢 **MIT** · `1 065` B — **it already cites the source page**, which is what a lecture answer needs |

🔴 **Mandatory gate before the SOW:** `ECL-2.0` is Apache-2.0 **with the § 3 patent grant narrowed
to "the needs of the education communities"** *(read from `paella`'s own blob, line `7`)*. 🟡 **If
the deliverable will be reused outside education, that narrowing is a question for counsel, not
a label for a scanner.** 🟢 p201 removes the previous blocker: the grant text now exists and can
be put in front of a lawyer.

### 🟢 P201-5 — Governance evidence plane: the `82`-point gap as a product *(all regions, 4–6 wks)*

🟢 **The best-evidenced opportunity in the KB: `92`% student use against `10`% of institutions
with formal guidelines; `87`% LATAM use against `26`% with a strategy; `87`% APAC agent
encouragement against `47`% with governance.** The client has already adopted and cannot
evidence it.

| step | component | licence | role |
|---|---|---|---|
| 1. event spine | `ralph` xAPI store *(KB row)* | — | Every AI interaction with a learner becomes a statement. 🔵 **p200 established authority is server-assigned and read-filtered in all four backends** |
| 2. marking + provenance | [`compose/code/aiact-50-2-*`](code/) | KB-internal | AI Act Article 50 marking; 🟢 **suites executable in this configuration — `427`/`427` this pass** |
| 3. review UI | `Appsmith` *(Apache-2.0, KB row)* | Apache-2.0 | Where a human signs off |
| 4. policy routing | `LangGraph` *(MIT, KB row)* | MIT | One graph, a policy node per jurisdiction |

🟢 **Six jurisdictions, one control plane:** Oklahoma, Maryland, 🆕 Colorado, 🆕 Texas, the EU AI
Act, Vietnam's Law `134/2025/QH15` *(🟡 in-force date published as both `2026-03-01` and
`2027-03-01` — `ACTION NU` unresolved)* and Australia all reduce to **a human stays accountable
for high-stakes decisions about a student, with a record.**

### 🟢 P201-6 — Pre-engagement licence gate, now an executable checklist *(all regions, 2–4 days)*

🔵 p200 made this billable; **p201 makes it mechanical, because every step below was run on real
repos this hour.**

1. 🟢 **Resolve the default branch first** — `git ls-remote --symref <url> HEAD`. 🔴 **`11` of
   `35` repos measured this pass use neither `main` nor `master`** (`release_11`, `15.0`,
   `release`, `dev`, `v2`, `mobile`, `develop`). **Hardcoding `main` produces a false
   *"no licence file"* — which is exactly how p200 lost `paella`'s grant.**
2. 🟢 **Probe the full path vocabulary**, not `LICENSE`: `LICENSE{,.md,.txt}`, **lowercase
   `license.txt`**, `LICENCE`, `COPYING{,.txt}`, `COPYING.LESSER`, **`docs/License.txt`**,
   `LICENSE/LICENSE`. 🔵 Use [`compose/code/lib/licence_path.sh`](code/lib/) — suite `33`/`33`.
3. 🟢 **Read the grant from `raw.githubusercontent.com`, not from the API's licence field.**
   🔴 Measured on `topic:lms stars:>200`: the API resolves **`23`/`32`**; blobs lift it to
   **`29`/`32`**; `NOASSERTION` was readable **`6`/`6`** times. **`NOASSERTION` means *unmatched
   text*, not *unlicensed*.**
4. 🟢 **Classify with [`compose/code/lib/license_family.sh`](code/lib/)** — `family_of`, suite
   `207`/`207`, and `65`/`65` on today's blobs. 🔴 **Never write a new classifier: the GPL-3.0
   text contains *"GNU Affero General Public License"* in its own § 13, and every pass that
   greps for the phrase re-earns the defect** *(p77, p200 — `P237`)*.
5. 🆕 🟢 **Read the whole notice for SCOPE.** `pupilfirst` and `leemons` open with the same
   sentence and end in **MIT** and **Fair Code** respectively; `human-skill-tree` grants
   `skills/` under **AGPL OR MIT** and `app/` under **AGPL only**. **Emit `(path → grant)`, not
   one label.**
6. 🆕 🟢 **Check the project's own notice for the version policy.** Chamilo's `license.txt` says
   **"version 3 … or (at your option) any later version"** — `GPL-3.0-**or-later`**, invisible in
   the licence text itself.
7. 🔴 **Flag the three failure classes before shortlisting:** non-OSI dressed as open source
   (`leemons`, Fair Code), **no grant on any channel** (`LMS-Laravel` `505★`, `LearnPress`
   `275★`), and **narrowed patent grants** (`ECL-2.0`: Sakai, Opencast, paella).

🟢 **Deliverable:** one TSV per candidate repo — `slug · branch · path · bytes · family · scope
map · verdict` — in the shape of
[`evidence/topic-lms-licence-coverage.2026-10-14-p201.tsv`](../evidence/topic-lms-licence-coverage.2026-10-14-p201.tsv).
🔵 **Seven steps, two days, and it has now caught a wrong licence, a missing grant, a non-OSI
licence and a false absence on four separate `500★`+ repositories.**


## Pass 200 — 2026-10-14 — RECIPES FROM THIS PASS'S VERIFIED COMPONENTS

🔵 **Every repo named below was verified alive today by `ls-remote --symref`, with its licence
read from its own blob and its star count read from the GitHub REST API.** Licences are inline
because in education the licence decides whether a pattern can ship at all — and this pass found
four repos with real adoption whose licence a single-file scan gets wrong.

### P200-1 — Moodle-side tutoring and deadline agent *(LATAM / EMEA, 6–8 wks)*

**Why this pattern now:** Moodle is the installed base across LATAM public universities and
EMEA public education, and as of this pass its MCP layer is real — but choosing by star count
picks an unlicensed repo.

| Layer | Component | Licence | Wiring |
|---|---|---|---|
| LMS integration | [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) `43★` | **MIT** `1 064` B | 🟢 **Fork it.** `43★` is a reference, not a dependency; the fork is the client's asset and its maintenance is a line item |
| Adaptive block | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) `141★` | **MIT** `1 068` B | Material → notes, quizzes, flashcards; local-first, so it can run inside the institution |
| Mastery model | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) `266★` | **MIT** | Take the **Bayesian Knowledge Tracing** model, not the UI — this is the part that makes "adaptive" mean something |
| Policy gate | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) `43 258★` | **MIT** | Explicit state machine: the institution's rules as nodes, not as prompt text |
| Retention | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) `515★` | **MIT** `1 074` B | 🆕 Spaced repetition under agent control — the one retention primitive that is already adopted |

🔴 **Do not use `loyaniu/moodle-mcp` despite its `42★` — it grants nothing on any path or
manifest.** Same for `haanhtuandev/vgu-mcp`. 🔵 **Moodle itself is `GPL-3.0`, not AGPL** *(this
pass re-read the blob; see [`repos/foundations.md`](../repos/foundations.md))*, so integrating
over Web Services is clean and **hosting the result does not trigger disclosure** — which it
would on Open edX or Canvas, both genuinely AGPL.

### P200-2 — Courseware shipped as an agent skill *(APAC-first, 4–6 wks; the port is the LATAM/NA play)*

**Why:** the `11`-repo skill layer found this pass *(see [`intel/trends.md`](../intel/trends.md)
trend 1)* has solved distribution — the learner installs into a tool they already use. `9` of the
`11` are MIT, and **none is Spanish, Portuguese or US-curriculum.**

1. **Grounding pattern** — copy [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill)
   (**MIT**, `307★`): teach **from the client's own slides, citing page numbers**, cropping
   figures. 🟢 **Provenance is the anti-hallucination control** and it is also the evidence trail
   a procurement review asks for.
2. **Interaction pattern** — [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill)
   (**MIT**, `245★`) for diagnosis-first sequencing, plus
   [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) (**MIT**, `284★`) for Socratic questioning.
3. 🔴 **Skill-tree content — read the licence scope before copying.**
   [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) (`572★`)
   grants its **`skills/` `SKILL.md` files under AGPL-3.0 *OR MIT, at your option*** and its
   **`app/` under AGPL-3.0 only.** 🟢 **Take the `skills/` payload under MIT. Do not take `app/`.**
   The scope lives inside a `1 134`-byte notice, so a scanner reporting "AGPL" would have made
   this pattern look impossible.
4. **Vertical shape** — [`KeWang0622/kaogong-skill`](https://github.com/KeWang0622/kaogong-skill)
   (**MIT**, `175★`) shows the commercial form: **one high-stakes exam, one skill.** The LATAM
   analogues are ENEM (Brazil), the Mexican COMIPEMS/EXANI and Colombia's Saber 11 — 🟢 **and
   this pass measured that no Spanish-language equivalent exists on GitHub above `30★`.**

### P200-3 — Human-oversight control plane for high-stakes decisions *(NA + EMEA + APAC, 10–12 wks)*

🟢 **The highest-value pattern in this pass, because one build is billable in four
jurisdictions** *(see [`intel/market.md`](../intel/market.md) → Global)*: **Oklahoma and
Maryland** statute, the **EU AI Act** Annex III.3, **Vietnam's Law No. 134/2025/QH15** (in force
1 March 2026, reaching foreign companies) and **Australia's** proposed guardrails all require
that a human stay accountable for admissions, grading and placement decisions.

| Layer | Component | Licence | Role |
|---|---|---|---|
| Decision graph | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) `43 258★` | **MIT** | Every high-stakes edge passes through an explicit approval node. **The graph is the audit artefact** a conformity assessment asks to see |
| Rubric evidence | [asu2304/auto-assessment-agent](https://github.com/asu2304/auto-assessment-agent) `0★` | **MIT** | 🟢 **Read the design, not the repo:** criterion-level, evidence-backed scores with deterministic score auditing. That audit trail *is* the compliance deliverable |
| Approval queue | [johnswyou/autograder](https://github.com/johnswyou/autograder) `0★` | **MIT** | Its README insists on human approval before release — the right default, already expressed |
| Teacher surface | [laurauguc/grading_assistant](https://github.com/laurauguc/grading_assistant) `4★` | **MIT** | Teachers upload **their own** rubrics; keeps the human the author of the standard |
| Evidence corpus | [opencast/opencast](https://github.com/opencast/opencast) `508★` | 🔴 **ECL-2.0** | Lecture capture to ground decisions in what was actually taught. 🔴 **Patent scope is narrowed to education use — counsel reviews this before the SOW** |

🔴 **Build, don't buy, and say so in the proposal: these three grading repos total `4` stars.**
🟢 That is the commercial case rather than an objection to it — the control plane is sellable
*because* nobody is giving it away, and the regulatory deadlines are already set.

### P200-4 — Permissive SIS plus an AI layer for a school group *(LATAM, 8–10 wks)*

**Why the licence drives this one entirely:** of the seven most-adopted open school-management
systems, **exactly two are permissive, and the most-starred is AGPL.**

- **Base, pick one:** [`4jean/lav_sms`](https://github.com/4jean/lav_sms) (**MIT** `1 072` B,
  `1 042★`) for a single institution, or 🟢 [`yungifez/skuul`](https://github.com/yungifez/skuul)
  (**MIT** `1 069` B, `409★`) **when there are many schools — it is built multi-tenant**, which
  is the shape of a group or ministry deployment. Both Laravel/PHP.
- 🔴 **Not** [`hrshadhin/school-management-system`](https://github.com/hrshadhin/school-management-system)
  (`1 145★`) — **AGPL-3.0** `34 522` B; hosting it for a client can compel source disclosure.
  🔴 **Not** `ProjectsAndPrograms/school-management-system` (`206★`) — no grant anywhere.
  🟡 `frappe/education` (`665★`) only if the client is already on ERPNext — and note its licence
  is a **`19`-byte reference**, so the grant cannot be established from the repo.
- **AI layer:** dropout/early-warning scoring over the SIS's own attendance and grade tables,
  with **LangGraph** (**MIT**) gating any intervention that reaches a student or parent, per
  `P200-3`. 🔵 Pair with **Kolibri** (**MIT** `1 097` B) where connectivity is the binding
  constraint rather than pedagogy.
- 🟢 **Governance deliverable, and it is the one the client will actually pay for:** the UNESCO
  IESALC finding that **`87%` of LATAM institutions use AI while `26%` have a strategy** means
  the written AI policy — and the mapping from that policy into the LangGraph gates above — is
  the engagement, not an appendix to it.

### P200-5 — Lecture capture to searchable, grounded course corpus *(EMEA / North America, 6–8 wks)*

- [`opencast/opencast`](https://github.com/opencast/opencast) (**ECL-2.0**, `508★`, branch
  `develop`) for automated capture and distribution — 🟢 **the piece no LLM framework provides
  and every "ask your lectures" product needs.**
- Player: [`polimediaupv/paella`](https://github.com/polimediaupv/paella) (`63★`) — 🟡 **declared
  `ECL-2.0` in `package.json` with no licence blob at `15` path/branch combinations.** Resolve
  that with the maintainers before it ships; do not infer the grant from the manifest.
- Grounding: [`stanford-oval/storm`](https://github.com/stanford-oval/storm) (**MIT**, `31 633★`)
  for outline-and-cite over the transcript corpus, with
  [`assafelovic/gpt-researcher`](https://github.com/assafelovic/gpt-researcher)
  (**Apache-2.0**, `30 093★`) where source-backed briefs are wanted.
- 🔴 **Step zero, and it is not optional: an ECL-2.0 patent-scope review.** The licence narrows
  the § 3 patent grant to *"the needs of the education communities."* If the deliverable serves a
  non-education licensee, that is a question for counsel **before** the statement of work.

### P200-6 — Licence-surface audit as a billable pre-engagement gate *(any region, 1–2 wks)*

🟢 **New pattern, and this pass is its own evidence: five distinct licence surfaces were found in
a single afternoon, all on repositories with real adoption.** A studio that runs this gate before
a proposal avoids discovering a copyleft obligation after the architecture is fixed.

The checks, each with a measured instance from this pass:

1. **Resolve the default branch first** (`ls-remote --symref`) — `rosariosis` uses `mobile`,
   `ILIAS` uses `release_11`, `openeducat` uses `19.0`, `opencast` uses `develop`. A read at
   `main` returns nothing and *looks* like "no licence."
2. **Probe case variants** — `LICENSE.TXT` (uppercase, `openedx/XBlock`) **and** `license.txt`
   (lowercase, `frappe/erpnext`, `GPL-3.0`, `35 149` B). `raw.githubusercontent.com` is
   case-sensitive.
3. **Probe non-root paths** — `OS4ED/openSIS-Classic` keeps `GPL-2.0` at `docs/License.txt`
   (`17 286` B, **with a UTF-8 BOM** that breaks a strict first-line match).
4. **Measure the payload, then ask whether it is a grant at all** — `frappe/education`'s
   `license.txt` is **`19` bytes** of claim; `human-skill-tree`'s is a **`1 134`-byte notice**
   against a `~34 500`-byte AGPL body.
5. **Read scope inside the notice** — `human-skill-tree` grants `skills/` under **MIT or
   AGPL at the licensee's option** and `app/` under AGPL only. **Per-directory scope changes the
   answer from "unusable" to "usable in part."**
6. 🔴 **Never classify GPL vs AGPL by searching for "Affero."** The GPL-3.0 text contains that
   phrase in § 13. Use the **title line plus the mention count: `3` = GPL-3.0, `15` = AGPL-3.0**,
   measured on `8` blobs this pass with no overlap. 🔵 This distinction decides whether a client
   may host the result.
7. **Never take the licence from an API or a manifest** — `polimediaupv/paella` reports
   `ECL-2.0` from both while granting nothing in any file.

🟢 **Deliverable:** a per-component table of *grant / scope / path / byte count / channel*, and
an explicit list of components that **cannot** enter a closed deliverable. 🔵 **In this pass's
own corpus that list would have had five entries** — and three of them are the most-starred
option in their category.

## Pass 199 — 2026-10-14 — RECIPES FROM THIS PASS'S VERIFIED COMPONENTS

Every repo named below was verified alive with its licence read from its own blob **today**.
Licences are stated inline because in education the licence decides whether a pattern can ship.

### P199-1 — Canvas tutoring + grading assist over an existing LMS *(North America, 6–8 wks)*

**The pattern that fits the crowded NA market: do not rebuild the LMS, attach to it.**

```
Canvas LMS (AGPL, client-hosted — untouched)
  └─ vishalsachdev/canvas-mcp (MIT, v1.14.0 Oct 2026) ......... 102 tools, 8 skills
       └─ microsoft/agent-framework (MIT) ..................... orchestration (NOT AutoGen)
            ├─ mem0ai/mem0 (Apache-2.0) ....................... per-student longitudinal memory
            ├─ infiniflow/ragflow (Apache-2.0) ................ course corpus w/ citations
            ├─ docling-project/docling (MIT) .................. textbook/PDF → structured text
            ├─ BerriAI/litellm (MIT) .......................... per-student cost cap + provider swap
            └─ langfuse/langfuse (MIT) ........................ traces = the audit evidence
```

**Wiring:** fork `canvas-mcp` (you will own it — there is no official server). Point Docling at
the course materials, index into RAGFlow, require a citation on every tutor answer. Give each
student a mem0 namespace keyed to the Canvas user id so the tutor remembers across a term.
Enforce the budget in LiteLLM per student id, not per tenant — a runaway loop is a per-student
cost event. Ship Langfuse from day one: the traces are what you show an accreditor.
🔴 **Do not let the agent write grades in v1.** Canvas MCP servers *can* grade
(`bruchris/canvas-lms-mcp` exposes it); that authority is what gets a pilot cancelled.

### P199-2 — Defensible AI grading: deterministic core, agentic margin *(Global, 8–10 wks)*

**Addresses the live objection (`intel/trends.md` #8): graders are challenged, so build for
challenge.**

```
jupyter/nbgrader (BSD) or ucbds-infra/otter-grader (BSD) .. deterministic tests = the score of record
  └─ asu2304/auto-assessment-agent (MIT) ................... criterion-level rubric scoring w/ evidence
       └─ johnswyou/autograder (MIT) ........................ handwritten work: locate → transcribe → rubric
            └─ laurauguc/grading_assistant (MIT) ............ teacher-facing rubric review UI
                 └─ langfuse/langfuse (MIT) .................. every score's full trace, retained
```

**Wiring:** code and maths that *can* be tested deterministically are graded by nbgrader/otter —
no model in that path. The agents only score what tests cannot reach (reasoning, prose, working
shown), and must emit **per-criterion evidence quotes**, which is precisely what
`auto-assessment-agent` provides and why it is the pick over a generic LLM call. Route every
agent score into `grading_assistant` as a *proposal*; a human approves before release —
`johnswyou/autograder`'s own README demands this. Retain the Langfuse trace for the full appeals
window.
🟢 **The sellable artefact is the appeal pack**: for any contested grade, the deterministic
result, the rubric criteria, the evidence quotes and the model trace.

### P199-3 — EU AI Act conformity harness for assessment AI *(EMEA, 10–12 wks)*

**Assessment and proctoring AI are Annex III high-risk; stand-alone duties apply
2 December 2027, generative transparency now.**

```
langchain-ai/langgraph (MIT) ....... explicit graph; each edge is an auditable control point
  ├─ node: PROHIBITED-USE GATE ..... hard-refuse emotion recognition (banned since 2026-02-02, €35M/7%)
  ├─ node: TRANSPARENCY ............ AI-interaction disclosure (obligation is live now)
  ├─ node: HUMAN OVERSIGHT ......... no automated high-stakes decision leaves without sign-off
  ├─ node: BIAS PROBE .............. cohort-sliced scoring deltas, re-run per release
  └─ sink: langfuse (MIT) .......... logging + technical documentation evidence
       on: OpenOLAT (Apache-2.0) or ILIAS (GPL-3) ... permissive / German-market LMS base
       infra: ollama (MIT) or vllm-project/vllm (Apache-2.0) ... inference stays in-perimeter
```

**Why LangGraph and not a prompt:** conformity requires you to *demonstrate* a control exists.
A graph node that cannot be bypassed is demonstrable; a system-prompt instruction is not.
🟢 Pick **OpenOLAT** when the client needs to embed platform code in something proprietary — it
is the only major LMS here under Apache-2.0. Keep inference local via Ollama/vLLM so the data
story and the sovereignty story are the same story.
🔵 Verify the transparency date against the Official Journal before contracting — sources this
pass gave both **2 August 2026** and **2 November 2026**.

### P199-4 — Offline-first public-education tutor *(LATAM, 8–10 wks)*

**Built for the binding constraint — connectivity and language, not pedagogy.**

```
learningequality/kolibri (MIT) ............. offline-first platform + content sync
  └─ ollama (MIT) ........................... small local model on-prem/on-device
       ├─ rhasspy/piper (MIT) ............... local TTS (runs on a Raspberry Pi) — accessibility + low literacy
       ├─ open-spaced-repetition/py-fsrs (MIT) ... FSRS retention scheduling, NOT Anki (AGPL)
       ├─ CAHLR/OATutor (MIT) .............. BKT mastery model — lift the model, leave the Firebase UI
       └─ docling (MIT) .................... national curriculum PDFs → structured content
   LMS base where one exists: chamilo/chamilo-lms (GPL-3, Spanish-origin)
   grounding option: Latam-GPT (Chile, Feb 2026, Spanish/Portuguese-first)
```

**Wiring:** everything in the student path runs with **no internet**. Kolibri syncs opportunistically.
Use `py-fsrs` for scheduling and OATutor's **BKT** for mastery estimation — two small,
inspectable, MIT models instead of one large opaque one, which also survives a 2 GB model budget.
Piper matters more than it looks: TTS is the accessibility and low-literacy path, and it runs on
a Pi.
🔴 **Match the funding reality**: the regional AI-education market is **tens of millions**
(Brazil ~`$61.1M`, Mexico ~`$59.2M`), and the committed money is donor and public programme
(Google.org/Raspberry Pi `$4.6M` → `1.25M` students by 2028, train-the-trainer). **Price and
staff this as a public-programme delivery, not an institutional software sale.**

### P199-5 — National AI-literacy curriculum delivery at mandate scale *(APAC, 12–14 wks)*

**China: compulsory from age six. India: compulsory from Class 3 in 2026–27. The gap is teachers.**

```
panaversity/learn-agentic-ai (MIT, 4.4k★) ... existing agentic-AI syllabus to adapt, not write
  └─ Open edX (AGPL) via overhangio/tutor (AGPL-3.0) ... MOOC-scale teacher cohorts
       ├─ openedx/XBlock (Apache-2.0, LICENSE.TXT) ..... custom assessment components, no platform fork
       ├─ jupyterhub/jupyterhub (BSD) ................. live coding for every trainee
       ├─ jupyter/nbgrader (BSD) ...................... deterministic autograding at cohort scale
       ├─ opencast/opencast (ECL-2.0) ................. lecture capture → reusable corpus
       └─ langgraph (MIT) ............................. per-jurisdiction policy nodes
```

**Wiring:** the deliverable is **teacher capability**, so the platform is a teacher-training MOOC,
not a student product. Extend via XBlock so upgrades do not become merges. One LangGraph policy
node per jurisdiction — China's algorithm filing and synthetic-content labelling, India's
20 February 2026 intermediary rules, **Vietnam's high-risk listing of automated assessment and
behavioural monitoring** — because APAC has no common framework to code against once.
🟢 Opencast turns each delivery into reusable assets, which is what makes the second country
cheaper than the first.

### P199-6 — Moodle-attached tutor for the global installed base *(Global, 4–6 wks)*

**Moodle is the widest installed base (EMEA public education, LATAM universities); this is the
fastest credible pilot in the catalogue.**

```
Moodle (GPL-3) — untouched, Web Services REST enabled
  └─ Jawadh-Salih/moodle-mcp-server (MIT, Go) ...... 14 tools, moodle_mobile_app token
       └─ huggingface/smolagents (Apache-2.0, 29.8k★) ... minimal code-thinking agent loop
            ├─ llama_index (MIT) ...................... retrieval over course content
            ├─ mem0 (Apache-2.0) ..................... learner memory across sessions
            └─ litellm (MIT) ......................... cost ceiling per learner
```

**Wiring:** the MIT Go server needs **no Moodle plugin install** — it rides Web Services with the
`moodle_mobile_app` token, so IT approval is a token and a capability
(`gradereport/user:view` for grades), not a deployment. That is why this pattern is 4–6 weeks.
🔴 **It has `0` stars.** Treat it as a reference implementation you fork and harden, and budget
the hardening. 🔴 **The alternative `csmediapro/moodle-mcp-server` is AGPL-3.0** — viable for an
internal institutional tool, a trap for a hosted multi-tenant service.
🔴 **Scope guard:** `submit_assignment` is in the tool list. An agent that can submit on a
student's behalf is an academic-integrity incident; disable it in v1.

### 🔵 Component licence ledger for the patterns above

| Can embed and sublicense freely | Needs an explicit client decision |
|---|---|
| canvas-mcp, moodle-mcp-server *(Jawadh-Salih)*, agent-framework, smolagents, LangGraph, mem0, RAGFlow, Docling, LiteLLM, llama_index, Langfuse, Ollama, vLLM, Piper, Whisper, Kolibri, py-fsrs, OATutor, XBlock, nbgrader, otter-grader, OpenOLAT, Oppia, Richie, Jitsi, the `3` MIT graders | **AGPL:** Open edX, Tutor, Canvas LMS, Anki, INGInious, `csmediapro/moodle-mcp-server` · **GPL:** Moodle, Chamilo, ILIAS, H5P, Pawtograder, Frappe Education, Gibbon, RosarioSIS · **LGPL:** BigBlueButton, OpenEduCat, autograder-server · **ECL-2.0:** Sakai, Opencast |

🟢 **Note the asymmetry deliberately:** the *agent and infrastructure* layer is almost entirely
permissive, while the *platform* layer is almost entirely copyleft. **That is the architectural
argument for attaching to the LMS rather than forking it** — it is a licensing argument before
it is an engineering one.
## Pass 198 — 2026-10-14

🆕 🟢 **`P0a` fired for the third consecutive pass and paid most in the pass where the
instruments could not run: `6` of p196's `7` pre-registered actions were answered from the
register alone, with `bash <repo script>` DENIED all pass.** 🟢 `P0a` stays step one, and this
pass adds the gate its own data forced and the pattern APAC's new law opened.

### 🟢 `P0a` — Read the register before building the instrument — **MEASURED THREE TIMES, keep it**

🔵 Wiring unchanged *(see p195/p196 below)*. 🟢 **Yield this pass:**

| p196's pre-registered action | what `P0a` returned | what it saved |
|---|---|---|
| classify the `3` root payloads | 🟢 `P441`'s `result.2026-10-07.tsv` + `p196-none-tree-reach` | the slugs and paths, already enumerated |
| the interoperability-layer re-read | 🟢 `p196-none-tree-reach` *(`Lumi`, `own_subtree=15`)* | the `15` paths did not have to be rediscovered |
| notice-form band | 🟢 `P420` *("size does not identify")*, `p196-copyleft-band` | the identity half; only the **anchor** half was new |
| case-fold de-dup + `494` census | 🟢 `p288-agpl-casefold`, `p196-population-diff` | 🔴 **the instruments exist and could not be RUN** |
| `${BASH_SOURCE[0]}` fixture fix | 🟢 `p560-epl-mpl-version-read/test_versions.sh` *(the pattern already done right)*, `p176-suite-exit-sweep` *(the silent-skip class)* | the correct idiom, already in the tree |
| *(the seventh was `P0a` itself)* | — | — |

🔴 **The honest footnote, and it is new:** `P0a` protects against re-deriving what exists. 🔴 **It
does not tell you whether you can RUN what exists.** 🟢 **`P0b`-style lane census must precede
`P0a`'s output being turned into a plan** — see `P197-D`.

### 🆕 🟢 `P197-D` — Census the lanes BEFORE planning the pass *(new step zero)*

🔵 **Why:** p196 pre-registered `7` actions. 🔴 **`3` were impossible before the pass began**,
because the execution door had shut, and nothing in the plan would have revealed it.

```
  STEP -1   lane census  -> can I reach bytes?   (raw lane)
                         -> can I reach trees?   (git clone --filter=blob:none)
                         -> can I resolve HEAD?  (git ls-remote --symref)
                         -> can I RANK?          (GitHub MCP search_repositories)
                         -> can I EXECUTE MY OWN REGISTER?   <-- the row p196 lacked
  STEP  0   P0a: grep compose/code/ + the four pages for prior art
  STEP  1   plan only actions whose lane is OPEN; pre-register the rest as BLOCKED, named
```

🟢 **Wiring:** `evidence/lane-census.2026-10-14-p198.tsv` is the template — one row per lane,
one column per pass, and the **door** named separately from the destination *(p196's rule)*.
🟢 **Exit condition:** if a pre-registered action's lane is closed, it is recorded as **BLOCKED
with the lane named**, never silently dropped and never attempted and half-reported.

### 🆕 🟢 `P197-E` — The licence-truth gate, and it does NOT use a filename list

🔵 **Why:** `5` education rows this pass have their grant somewhere other than where a reader
looks, and 🔴 **this pass's own sweep would have published `AutoGen` as `CC-BY-4.0`** because a
first-match list stopped at `LICENSE` and never reached `LICENSE-CODE`.

```
  ┌─ 1. RESOLVE the branch ──────────────────────────────────────────────┐
  │  git ls-remote --symref <url> HEAD                                   │
  │  NEVER guess main/master -- 10 of 30 education rows are neither,      │
  │  and a guessed 404 is a FALSE ABSENCE                                 │
  └───────────────────────────┬──────────────────────────────────────────┘
  ┌───────────────────────────▼──────────────────────────────────────────┐
  │  2. ENUMERATE the tree                                               │
  │  git clone --filter=blob:none --no-checkout --depth 1 && ls-tree -r   │
  │  the ONLY channel that sustains an absence  (P441)                    │
  └───────────────────────────┬──────────────────────────────────────────┘
  ┌───────────────────────────▼──────────────────────────────────────────┐
  │  3. CLASSIFY EVERY licence-named entry -- not the first one           │
  │  compose/code/p198-title-line-family/family_title_line.py             │
  │  title line in DOCUMENT order; defeats GPL-3 §13 AND GPL-2 preamble   │
  └───────────────────────────┬──────────────────────────────────────────┘
  ┌───────────────────────────▼──────────────────────────────────────────┐
  │  4. SEPARATE own-grant from vendored                                  │
  │  root / own subtree  vs  node_modules, vendor/, assets/*/libraries/   │
  │  (Lumi: 15 texts, ALL vendored, 0 own -- the layer grants nothing)    │
  └───────────────────────────┬──────────────────────────────────────────┘
  ┌───────────────────────────▼──────────────────────────────────────────┐
  │  5. FAIL CLOSED on: CC-BY-NC, CC-BY-SA, any CC for CODE, AGPL for a   │
  │     hosted deliverable, NOASSERTION, and <1 KB "pointer" licences     │
  └──────────────────────────────────────────────────────────────────────┘
```

🟢 **Concrete wiring for a studio intake:** run steps `1`–`4` over the client's candidate
dependency list; emit one row per repo with `slug`, `branch`, every licence path, family from
bytes, byte count, and `own|vendored`. 🔴 **Gate the engagement on step `5`, not on a GitHub
sidebar.** The five rows this pass caught —
`autogen`/`formalms`/`fedena`/`frappe-education`/`openSIS` — are all rows a sidebar gets wrong.

🔵 Declared limits are in [`compose/code/p198-title-line-family/README.md`](code/p198-title-line-family/README.md):
English-only grant detection, and one family per file *(a multi-notice file needs `P441`'s
`names_multiple`)*.

### 🆕 🟢 `P197-F` — One assessment-conformance build, FOUR jurisdictions

🔵 **Why now:** 🆕 **Vietnam's AI law *(`2026-03-01`)* names automated assessment and
behavioural monitoring as high-risk, with compliance due `2027-03-01` and reach over foreign
providers.** 🟢 Korea's AI Basic Act names education high-impact; the EU's Annex III names
assessing learning outcomes; North American districts bar AI as the **sole basis** for
high-stakes determinations. 🟢 **Four regulators, independently drafted, one component.**

```
            ┌─ the ASSESSMENT path, treated as the regulated path ─────────┐
            │  tutor / assessment agent                                     │
            │  DeepTutor (Apache-2.0) | oppia (Apache-2.0) | OATutor (MIT)  │
            └───────────────────────┬──────────────────────────────────────┘
      ┌─────────────────────────────▼───────────────────────────────────────┐
      │ HUMAN-IN-THE-LOOP GATE   (Idaho: AI may not replace teachers;       │
      │                           Charleston: not the SOLE basis)           │
      │  -> compose/code/agent-tool-receipts-port/  per-action receipts      │
      └─────────────────────────────┬───────────────────────────────────────┘
      ┌─────────────────────────────▼───────────────────────────────────────┐
      │ MARKING / PROVENANCE     (EU Art.50 in force 2026-08-02;            │
      │                           China: binding content labelling)         │
      │  -> compose/code/aiact-50-2-marking/   provenance fields             │
      │  -> compose/code/aiact-50-2-pack/      aiact-50-2.xsd                │
      │  -> compose/code/aiact-50-2-spans/     which spans are AI-authored   │
      └─────────────────────────────┬───────────────────────────────────────┘
      ┌─────────────────────────────▼───────────────────────────────────────┐
      │ POLICY STATE, dated and diffable                                     │
      │  OK S.B.1734's four clauses as a SCHEMA; VT H.B.650 vendor duty;      │
      │  CA A.B.1159: student data must NOT train models                      │
      │  -> compose/code/p598-register-freshness-gate/                        │
      └─────────────────────────────┬───────────────────────────────────────┘
      ┌─────────────────────────────▼───────────────────────────────────────┐
      │ JURISDICTION PROFILE  (one policy node per market, same pipeline)    │
      │  EU | Vietnam | Korea | US-state   -> LangGraph policy nodes          │
      └─────────────────────────────────────────────────────────────────────┘
```

🟢 **Why the stack is permissive end to end:** `DeepTutor` `Apache-2.0` *(`11 408` B, from
bytes)*, `oppia` `Apache-2.0` *(`11 358` B)*, `OATutor` `MIT` *(`1 105` B)*, `kolibri` `MIT`
*(`1 097` B)* for the offline tier. 🔴 **Deliberately NOT in this stack:** `ChatTutor`
*(`AGPL-3.0`)*, `lumen` *(`GPL-3.0`)*, `Open edX`/`Canvas`/`tutor` *(`AGPL-3.0`)* — a hosted
assessment service under Affero owes source disclosure to its users.

🔵 **Sequencing, from the dates:** Article `50` binds **now** → build the marking layer first.
Vietnam's `2027-03-01` is the next hard deadline → the jurisdiction profile second. EU Annex III
*(`2027-12-02`, contested)* → last. 🔴 **`4`–`6` weeks for the marking layer, `8`–`10` for the
jurisdiction profile**, on the basis that every primitive above already exists in this KB.

### 🆕 🟢 `P197-G` — The LATAM engagement IS the governance artefact

🔵 **Why:** 🟢 **`87`% of `200` LATAM higher-ed institutions use AI in at least one area;
`26`% hold a formal AI strategy** *(UNESCO IESALC, `19` countries)*. 🔴 A `61`-point gap. 🟡 EMEA
shows the same shape at `10`% of `450`+ institutions.

🟢 **So the deliverable is not a tutor. It is the instrument that lets an institution say what
its tutors may do** — and it is the same four clauses North America already legislates:

| clause | the artefact | the primitive |
|---|---|---|
| approved / prohibited uses | a machine-readable use register, enforced at the tool boundary | 🟢 `agent-tool-receipts-port/` |
| data protection + minimisation | a data-flow inventory the system **emits** | 🔴 a vendor duty under VT H.B.`650` |
| learner / family transparency | disclosure of which spans the AI authored | 🟢 `aiact-50-2-spans/` |
| periodic review | dated, diffable policy state | 🟢 `p598-register-freshness-gate/` |

🟢 **Deploy tier for the region:** `kolibri` *(MIT, offline-first)* where connectivity is the
binding constraint; `chamilo-lms` has deep LATAM install base but is 🔴 `GPL-3.0`, so pair it
rather than fork it. 🟢 **Institutional channel:** UNESCO's LAC Observatory *(launched
`2026-04-14`, Santiago)* is the reference point a proposal can cite.

🔴 **Named gap this pattern must not paper over:** no binding national AI-in-education
regulation was found in any LATAM jurisdiction. 🟢 **That is why the artefact is institutional
policy, not statutory compliance** — and the pattern is honest about selling the former.

## Pass 197 — 2026-10-14

🟢 **`P0a` fired for a second consecutive pass**, and this time it is cheap to say what it
saved: `P441` *(a filename list cannot be fixed by widening it)*, `P237` *(do not rewrite a
hardened classifier)*, `P742` *(a grant can live in a file's body)*, `P502` *(absence must not
present itself as a verdict)*, `Gap 440` *(a correction that lands on one page and not the
others)*, `Gap 441` *(measure an instrument against the rows it ACCUSES)* and p139's header
channel were **all cited, none re-derived.** 🔴 **And `Gap 441` was cited and then committed
anyway**, by this pass's own comparator — see `P198-B`.

🔵 **A note on ids before the patterns.** p196 labelled its pattern set `P197-*`. This pass
**is** `197`, so the scheme collides with its own calendar on the very next pass that uses it.
This pass continues at `P198-*` rather than renaming anyone's work, and pre-registers the
decision: **anchor a pattern id to the pass that WROTE it.**

### 🆕 🟢 `P198-A` — Deliver INSIDE the LMS: the plugin stack, with the grant stated at every layer

🔵 **Why now:** the AI in this market is arriving as **plugins**, not as integrations beside the
platform *(`T317`)*. The buyer is the LMS administrator, the permission model is the platform's,
and the licence is the platform's too.

```
   agent / orchestrator  (yours — any licence)
            │  MCP
            ▼
   onbirdev/moodle-webservice_mcp        ← the seam: MCP over Moodle's own web services
            │  Moodle web-service API (tokens, capabilities, roles)
            ▼
   bycs-lp/moodle-local_ai_manager       ← GOVERNANCE: providers, quotas, per-tenant policy
            │
            ├── bycs-lp/moodle-block_ai_chat      ← the learner/teacher chat surface
            ├── marcusgreen/moodle-qtype_aitext   ← LLM-graded free text (see P198-C)
            ├── cgrevisse/moodle-qbank_genai      ← generative question bank
            └── human2human-ai/moodle-tool_human2human ← oral exams, role plays, debates
```

| layer | licence, read this pass | what it obliges |
|---|---|---|
| `onbirdev/moodle-webservice_mcp` | *(on shelf)* | the seam — keep it a seam, do not fork it |
| 🟢 `bycs-lp/moodle-local_ai_manager` | 🟢 **`GPL` in `255`/`278` source headers** | a derivative is `GPL`. 🔵 **There is no licence FILE — the grant is per file, and it is still a grant** |
| 🟢 `bycs-lp/moodle-block_ai_chat` | 🟢 `GPL` in `64`/`91` headers | same |
| 🟢 `marcusgreen/moodle-qtype_aitext` | 🟢 `GPL` in `40`/`50` headers | same |
| 🟡 `human2human-ai/moodle-tool_human2human` · `cgrevisse/moodle-qbank_genai` | 🟡 `GPL-3.0` *(`35 149` / `35 178` B)* | same, stated in a file |
| 🟢 **`microsoft/moodle-ai-assistant`** | 🟢 **`MIT`** *(`1 084` B)* | 🟢 **the only permissive seat in the layer** — the one row a client may fork into a closed internal build |

🟢 **The build rule:** keep **your** agent and prompt assets **outside** the plugin tree, speak
to the platform through the MCP seam, and accept `GPL` for anything that lands inside it.
🔴 **The anti-pattern:** putting proprietary logic in a plugin fork and discovering the
obligation at hand-over — the plugins carry no licence file, so a casual check reports *«no
licence»* and the obligation is invisible until someone reads a `.php` header.

### 🆕 🟢 `P198-B` — The licence gate is FOUR channels, and each answers a question the others cannot

🔵 **Why now:** this pass measured one row read four ways and got four different answers, three
of which would be published as *«no licence»*.

```
  1. EXISTENCE      git ls-remote --heads --tags          → REFS / EMPTY / ABSENT (three states)
  2. PATHS          clone --filter=blob:none + ls-tree -r → is_licence_path over the COMPLETE tree
  3. BYTES          git cat-file -p HEAD:<path> > file    → size_of_file + family_of   (never $(...))
  4. HEADERS        p139/headers.py over the tree         → SPDX / COPYRIGHT / GRANT_MIT|APACHE|GPL
     ── and the one that does NOT exist: a DECLARATION reader for prose (see the limit below)
```

| verdict | what it permits |
|---|---|
| 🔴 `ABSENT` *(`rc=128`)* | nothing — the address is dead. 🔴 `apereo/opencast`, `yourusername/scholarmate` |
| 🆕 🔴 `EMPTY` *(reachable, `0` refs)* | nothing, **and it is a different fact**: the repository exists and has no files. 🔴 `cdweaver1992/edfi-mcp-server`, `openfresno/edgenuity-aeries-grade-passback` |
| 🟢 grant at root or in subtree, family read | use under that family's terms |
| 🟢 **no licence file, grant in source headers** | 🟢 **use under that family's terms — this is a grant** *(`3` of `3` Moodle plugins)* |
| 🔴 no grant on any path and none in any header | 🔴 **do not recommend** — 🔴 **and do not call it *«all rights reserved»***: the header channel cannot see a CC declaration |

🔴 **The measured limit, with this corpus's own proof.**
[`xiaolai/the-craft-of-selfteaching`](https://github.com/xiaolai/the-craft-of-selfteaching)
declares `CC-BY-NC-ND` in its `README.md`; this KB has known it since p854, **with a committed
fixture that is byte-identical to the live file**. The classifier answers 🟢 `CC-BY-NC-ND-3.0`
on **the declaration line** and 🔴 `UNCLASSIFIED` on **the whole file** — and the extraction
that makes the difference **lives in the test, not in `lib/`.** 🔵 So no channel of this KB has
it, and channel `4` must report `NO-HEADER-GRANT`, which is what it measured.

🔴 **And the gate's own instrument accused two innocent rows this pass.** A byte figure near a
slug is not that slug's licence size: one was a **README size** the page itself labelled, the
other belonged to **a second slug named in the same table cell** — `Gap 441`, cited at the top
of this very section and then committed. 🟢 **Two rules, now in the instrument with `10`/`10`
tests, two of which are those two accusations:** a figure whose preceding `24` characters say
`README`/`paths`/`★`/`LOC` is not a licence size, and **a line naming another slug cannot
accuse.**

### 🆕 🟢 `P198-C` — Build the assessment path so the REGULATOR's constraint is the architecture

🔵 **Why now:** Maryland `S.B. 720` *(in force `2026-06-01`)* bars AI as the **primary basis**
for grading, discipline or placement; Idaho bars AI from replacing teachers; the EU prohibits
**emotion inference in educational institutions** outright *(Article `5`)*.

```
   learner response
        │
        ▼
   marcusgreen/moodle-qtype_aitext   ← the model PROPOSES a grade + feedback
        │                              (GPL in 40/50 headers)
        ├──► proposal recorded  ─────────────┐
        ▼                                     │  both rows persisted
   teacher review (Moodle capability check)    │  = the S.B. 720 evidence
        │                                     │
        ├──► accepted / overridden  ──────────┘
        ▼
   grade of record  +  xAPI statement via ralph  ← task-level evidence, NOT affect
```

- 🟢 **The deliverable is the override trail**, not the grader. A system that cannot show a human
  disposition per graded item cannot be sold into Maryland, and the same artefact answers
  Vermont's annual vendor certification and Chile's Ley `21.719` profiling record — 🟢 **one
  build, three jurisdictions**.
- 🔴 **Do not ship affect analytics in EMEA at all.** Not a toggle: Article `5` prohibits
  emotion inference in educational institutions. 🟢 Replace it with `xAPI` task evidence through
  `ralph`, which this KB has already measured, including its deliberate exclusion of the
  asserting authority from de-duplication.
- 🟡 **Oral assessment is the newest surface and it is `GPL-3.0`:**
  [`human2human-ai/moodle-tool_human2human`](https://github.com/human2human-ai/moodle-tool_human2human)
  *(created `2026-10-05`)*. 🔵 Treat it as a base to configure, not to fork, unless the client
  accepts `GPL`.

### 🆕 🟢 `P198-D` — Ship a BILL OF MATERIALS with anything H5P-based, and build it by HOLDER

🔵 **Why now:** [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) enumerates
`6 348` paths and `15` licence texts. 🔴 **`14` belong to Joubel, H5P, Oliver Tacke and
CKSource; `1` is a `259 095` B EULA; `0` are Lumi's own.**

```
  ls-tree -r  →  is_licence_path  →  cat-file → family_of  →  grep -m1 copyright  →  GROUP BY holder
                                                                                        │
                        ┌───────────────────────────────────────────────────────────────┘
                        ▼
      holder == the repo's owner ?  ── no ──►  THIRD-PARTY NOTICE  (goes in the BoM)
                        │ yes
                        ▼
              the project's own grant
```

- 🔴 **Why the path list fails here:** `is_bundled` excludes `node_modules`, `vendor`,
  `third_party`… and these texts live under **`assets/h5p/libraries/`** — a path no exclusion
  list anticipated. 🟢 **The copyright holder identifies them; the path does not.** `P441`'s
  lesson, one layer up.
- 🔴 **And `is_licence_path` counts `eula` as a grant.** An EULA is a restriction. 🔵 Measured
  here, pre-registered, **not patched in the pass that promoted the predicate to `lib/`**
  *(`P237`, and a byte-identity control that would break)*.
- 🟢 **The client artefact:** the notice file a buyer needs for an H5P deliverable is **not the
  platform's licence** — it is a per-holder list of `14` grants, and producing it is an hour of
  work with the four channels of `P198-B` already wired.

### 🆕 🟢 `P198-E` — An instrument this studio ships must be invocation-independent

🔵 **Why now:** this KB's own shared suite reported **three different denominators** from six
invocation forms, and the worst form printed a total while the classifier had never loaded.

| rule | why |
|---|---|
| 🟢 resolve the script's own directory **once, absolute, BEFORE any `cd`** | `$0` and `${BASH_SOURCE[0]}` are relative to the **invocation** cwd |
| 🟢 resolve it **physically** *(`readlink -f`)* | through a symlink, the path names the link, and its siblings are not the script's siblings |
| 🟢 make loading a dependency a **hard gate** *(check the `source`, assert a function exists)* | otherwise a failed load degrades into failures **and a printed total** |
| 🟢 give every fixture-dependent block a **presence canary** | a `SKIP` to stderr lowers the denominator without lowering the numerator |
| 🟢 run it from **≥4 forms in CI**, including through a symlink | one form passing is not path independence — `../lib/suite.sh` passed **by luck** |

🟢 Runnable against any suite: `SUITE_UNDER_TEST=<path> p197-suite-path-independence/run_from_dirs.sh`
*(`19`/`19`, four of five cases negative)*.

## Pass 196 — 2026-10-14

🆕 🟢 **`P0a` was installed as a gate one pass ago. This pass it FIRED, and the saving is
measured: it answered `3` of p195's `4` pre-registered actions before a line of code was
written, and one of those three had been pre-registered as an instrument this KB proved does
not work four passes earlier.** 🟢 **`P0a` stays step one, and this pass adds the two patterns
that close `P0b`'s stated limits.**

### 🟢 `P0a` — Read the register before building the instrument — **MEASURED, keep it**

🔵 Unchanged from p195; the wiring is in that section below. 🟢 **What is new is its yield:**

| p195's pre-registered action | what `P0a`'s grep returned | what it saved |
|---|---|---|
| copyleft byte bands | 🟢 **`P420`** — *"size does not identify"*, with pristine sizes already recorded; `P419` for the header read | the identity half was already answered; only the **narrowing** half was new |
| `docs/`+`legal/`+`.github/` probe | 🔴 **`P441`** — *"widening a list cannot fix a list"*, with a suite and three prior failures on the same row | 🔴 **the whole instrument. It was already refuted** |
| population re-extract | 🟢 **`p192`'s population rule**, quotable verbatim from `repos/foundations.md` | the rule did not have to be re-invented, so the diff is comparable |
| *(the fourth was `P0a` itself)* | — | — |

🟢 **Exit condition, restated because it paid:** if a hit describes the defect, **cite it and
spend the pass elsewhere.** 🔴 Three consecutive passes had recorded this failure before the
gate existed; this is the first pass where the gate ran first and the recurrence did not happen.

🔴 **The honest footnote: the gate protects the headline, not every line.** This pass's own
population extractor shipped **two list-widenings** *(`repos/..`, then `repos/...`)* and its
throwaway `12`-name licence probe **missed `frappe/education`** at lowercase `license.txt`.
🟢 **Run `P0a` against the small instruments too, not just the pass's headline build.**

### 🆕 🟢 `P0c` — The tree channel: how to sustain an ABSENCE, not just fail to find a presence

🔵 **This closes `P0b`'s stated limit** *("this reads the ROOT only")*, which stood open from
p195 through `p969`. 🔵 Wiring: [`compose/code/p196-none-tree-reach/`](code/p196-none-tree-reach/),
suite **`24`/`24`**.

```bash
# WHEN: any time you are about to report "no licence" / "no file of kind X".
# WHY : a filename list can only FIND.  To sustain an ABSENCE you must ENUMERATE (P441).
#       Measured on this shelf: 19 root filenames missed a ROOT grant on 3 of 88 rows.

# 1. the CHANNEL — commit + trees, no blobs.  Needs no API (api.github.com is 403 here).
git clone --filter=blob:none --no-checkout --depth 1 "https://github.com/$SLUG" "$D"
git -C "$D" ls-tree -r --name-only HEAD          # the COMPLETE tree, unpaginated

# 2. the two PURE predicates — offline-testable, and the only place conventions live.
#    is_licence_path()  : basename rules + the REUSE convention LICENSES/<SPDX-ID>.txt
#    is_bundled()       : node_modules/ vendor/ third_party/ .venv/ dist/ ... (imported, P126)

# 3. the four VERDICTS — note that only the first is unreachable by a filename list.
#    ABSENCE-ENUMERATED | OWN-GRANT-AT-ROOT | OWN-GRANT-IN-SUBTREE | BUNDLED-GRANT-ONLY
bash compose/code/p196-none-tree-reach/tree_reach.sh out.tsv slugs.txt
```

| cost, measured | |
|---|---|
| `88` repositories, full tree each | 🟢 **`0` clone failures** |
| rows a `19`-name root ladder got wrong | 🔴 **`12` of `88`** — `3` at the root, `9` in subtree |
| the figure it corrects | 🟢 **`18.8`% → `16.2`%** genuinely ungranted |

🔴 **Three guards, each bought with a failure:**

| guard | the failure |
|---|---|
| 🔴 **Match licence paths case-INSENSITIVELY** | `LICENSE.TXT`, `License.txt`, `License`, `license.txt`, `package/license` are all real rows on this shelf that case-sensitive lists missed |
| 🔴 **Handle `LICENSES/<SPDX-ID>.txt`** | the REUSE convention puts the SPDX id in the **basename**, so a basename-only probe is blind. 🔵 **v1 of this very instrument failed here and its own suite caught it** |
| 🔴 **Exclude vendored paths BEFORE counting** | `Tushar-cy/Ai-edge-learning-hub` has `359` bundled licence files and **`0` of its own.** Without the exclusion it reads as richly licensed |

🟡 **Its own limit, stated:** a clone per repository is far heavier than `4.6` HTTP probes.
🟢 **So the shape is: root ladder for the census, tree channel for every `NONE` it returns.**
Never the tree channel for all `468`.

### 🆕 🟢 `P0d` — A byte band is a SET of intervals, because licences are bimodal by convention

🔵 Wiring: [`compose/code/p196-copyleft-band/`](code/p196-copyleft-band/), suite **`32`/`32`**
*(carrying p195's seven permissive assertions unchanged — `P237`)*.

```bash
. compose/code/p196-copyleft-band/band_copyleft.sh
band_verdict AGPL-3.0 34523     # IN-BAND
band_verdict LGPL-3.0  7651     # IN-BAND  <- short form, GPL-3.0 BY REFERENCE
band_verdict LGPL-3.0 43529     # IN-BAND  <- odoo/odoo: FULL form, GPL-3.0 BY VALUE
band_verdict LGPL-3.0 20000     # OVER     <- the TROUGH between two legitimate forms
band_verdict AGPL-3.0   723     # UNDER    <- read it: a GNU short NOTICE, a valid grant
```

🔴 **Why a set and not an interval:** `LGPL-3.0` has **two** legitimate published forms
*(`7 651` B and `42 098` B)*. 🟢 **A single `lo`/`hi` band calls `odoo/odoo` narrowed, which is
wrong.** 🟢 The general rule: **a control that assumes one canonical form per category misreads
the publisher convention, not the content.**

🔴 **Two rules that are not optional:**

| rule | why |
|---|---|
| 🔴 **Anchor to a reference OUTSIDE the instrument** (`P417`) | this pass used SPDX `license-list-data` **plus** the shelf's modal size, and inherited p195's ±`10`% width rather than tuning one. 🔴 A band fitted until the answer looks tidy measures the author |
| 🔴 **The band is a TRIGGER TO READ, never a verdict** | 🟢 **`4` of `83` flagged; `4` of `4` were false positives for narrowing.** `3` were the GNU short-notice form *(a valid grant that LOOKS like `Gap 421`'s non-grants)* and `1` was a missing non-operative appendix |

🔵 **`P420` still holds and bounds this:** size does **not** identify. Three `AGPL-3.0` texts
here are `34 523` B exactly with different digests. Identity stays `P392`'s *(FILE, digest)*
pair; family stays `P419`'s `n=2` header read.

### 🆕 🟢 `P0e` — Two lanes, two purposes: discover on the channel, deliver on the bytes

🔵 Measured this pass: `13` rows cross-checked, 🟢 **`11` agree, `0` diverge, 🔴 `2` API-blind.**

```bash
# DISCOVERY — the GitHub MCP ranked channel.  Answers where curl api.github.com is 403.
#   gives: slug, stars, pushed_at, license.spdx_id.   0 DIVERGE on 13 rows -> trust the RANKING.
#   query that worked: topic:education language:Python stars:>300 pushed:>YYYY-MM-DD
#   KNOWN LIMITS: unfiltered queries exceed the response size limit; some narrow
#                 variants return total_count:0; language filter biases toward Python.

# DELIVERY — the raw lane, every time, no exceptions.
#   NEVER let license.spdx_id decide a deliverable.  Measured counter-examples:
#     TrenTorch/TrenTorch   NOASSERTION -> PolyForm Noncommercial 1.0.0, 4 635 B -> BARRED
#     frappe/education      NOASSERTION -> 19 bytes: "License: GNU GPL V3"      -> declaration
curl -sL -o p.txt -w '%{http_code}' "https://raw.githubusercontent.com/$SLUG/HEAD/$PATH"
. compose/code/lib/payload_measure.sh && family_of_file p.txt && commercial_use_ok "$(cat p.txt)"
```

🔴 **The rule in one line: `NOASSERTION` is a BLIND SPOT, not a soft "unknown."** On this
sample it meant a non-commercial bar once and a `19`-byte declaration once — never *"probably
permissive."*

🟡 **And organisation reputation does not transfer:** `frappe/lms` carries a real `33 893`-byte
`AGPL-3.0`; `frappe/education` carries `19` bytes. **Same publisher. Read the row, not the owner.**

### 🆕 🟢 `P197-A` — One marking layer, two jurisdictions *(EU Article 50 + China labelling)*

🔵 **Why now:** Regulation (EU) `2026/1744` deferred **Annex III** education high-risk to
`2027-12-02` but 🔴 **left Article `50` transparency in force since `2026-08-02`** — and China
already requires **binding AI-content labelling.** 🟢 **Same instrument class, two markets, one
build.**

```
            ┌─ generation ─────────────────────────────────────────────┐
            │  tutor / assessment agent  (DeepTutor, oppia, Anubis…)   │
            └───────────────────────┬──────────────────────────────────┘
                                    │ every AI-authored artefact
            ┌───────────────────────▼──────────────────────────────────┐
  MARKING   │ compose/code/aiact-50-2-marking/   -> provenance fields  │
  LAYER     │ compose/code/aiact-50-2-pack/      -> aiact-50-2.xsd     │
            │ compose/code/aiact-50-2-spans/     -> which SPANS are AI │
            └───────────────────────┬──────────────────────────────────┘
            ┌───────────────────────▼──────────────────────────────────┐
  AUDIT     │ compose/code/agent-tool-receipts-port/  -> per-action    │
            │ compose/code/action-gap-crosscheck/     -> claim vs act  │
            └──────────────────────────────────────────────────────────┘
                                    │
            ┌───────────────────────▼──────────────────────────────────┐
  EXPOSURE  │ compose/code/aiact-50-2-exposure/  -> what is UNMARKED   │
            └──────────────────────────────────────────────────────────┘
```

🟢 **Deliverable today, not in `2027`**: anything already on an EU market since `2026-08-02`
owes Article `50` marking. 🔴 **Run `aiact-50-2-exposure/` first** — it reports what is
*unmarked*, which is the finding a client pays for. 🔵 `aiact-50-2-emitter-gap/` records where
the emitter side is still missing.

### 🆕 🟢 `P197-B` — The North America deliverable is a policy-conformant configuration

🔵 **Why:** `77` AI-in-classroom bills across `27` states, ≈`33`–`35` states with K-12 guidance,
and ≥`5` states obliging **districts** to hold AI policies. 🟢 **Oklahoma S.B. `1734` names the
four clauses, so treat them as a schema, not prose:**

| clause | what the build owes it | the primitive |
|---|---|---|
| approved / prohibited instructional uses | a machine-readable use register, enforced at the agent's tool boundary | 🟢 `agent-tool-receipts-port/` — per-action receipts |
| data protection and **minimisation** | a data-flow inventory produced **by** the system | 🔴 Vermont H.B. `650` makes this a **vendor** duty, certified annually |
| family transparency | learner-facing disclosure of what the AI did | 🟢 `aiact-50-2-spans/` — which spans are AI-authored |
| periodic review | dated, diffable policy state | 🟢 `p598-register-freshness-gate/` |

🔴 **Idaho bars AI from replacing human teachers** → 🟢 **teacher-in-the-loop as a hard
architectural constraint in this region, not a configuration flag.** Gate every
grade-affecting action on a human approval receipt.

🟢 **Concrete base pairing**, all byte-verified permissive:
[`CTFd/CTFd`](https://github.com/CTFd/CTFd) *(`Apache-2.0`, `11 314` B)* for graded challenges
**or** [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) *(`MIT`, `1 083` B)* for
autograding + per-student IDE, [`oppia/oppia`](https://github.com/oppia/oppia) *(`Apache-2.0`,
`11 358` B)* for the branching lesson sequence, receipts layer above. 🟢 **All three carry a
patent grant; `MIT` does not** — which matters in a regulated procurement.

### 🆕 🟢 `P197-C` — Build the assessment path as the REGULATED path

🔵 **Why:** `DeepTutor`'s two releases this week *(`v1.6.14`, `2026-10-08`: visual practice, a
learning journal, managed plugins)* move it from *explanation* to **assessable sequence with
retained state**. 🔴 **That is precisely the surface Brazil's PL `2338/2023` would call
high-risk *(educational evaluation)* and the EU's Annex III already does.** 🟢 **The product
trend and the regulation are converging on the same feature.**

```
 learner ──► tutor agent (DeepTutor / open-tutor-ai-CE)
                 │
                 ├─ explanation path ──► low regulatory weight
                 │
                 └─ ASSESSMENT path ──► 🔴 HIGH-RISK in EU Annex III (2027-12-02)
                                        🔴 HIGH-RISK in BR PL 2338/2023 (educational evaluation)
                                        │
                      ┌─────────────────▼──────────────────┐
                      │ explainability + audit, FROM DAY 1 │
                      │  action-gap-crosscheck/  claim≠act │
                      │  agent-tool-receipts-port/         │
                      │  aiact-50-2-spans/   AI-authored   │
                      └────────────────────────────────────┘
```

🟢 **Separate the two paths in the architecture**, so the regulated obligations attach to the
assessment surface only. 🔴 **Do not pre-build to Brazil's draft clauses** — PL `2338/2023` is
still in the Chamber of Deputies and the text can change. 🟢 Build the **audit primitives**,
which every version of the clause will want.

### 🟢 `P197-D` — Pick the base from the bytes, because the open web is wrong in the expensive direction

🔴 **Measured this pass against a web sweep that itself said *"sources disagree on several
licenses"*:**

| platform | the web | 🟢 the bytes | cost of believing the web |
|---|---|---|---|
| 🔴 `openedx/edx-platform` | AGPLv3 **or** Apache-2.0 | 🟢 **`AGPL-3.0`** `35 136` B | 🔴 an undisclosed **network-use disclosure** duty on a hosted deliverable |
| 🔴 `sakaiproject/sakai` | *"Apache 2.0"* | 🟢 **`ECL-2.0`** `11 120` B | 🔴 a patent grant **scoped to education**, assumed general |

🔴 **Both web errors run permissive — the direction that costs a client.** 🟢 **The permissive
platform-grade short list, byte-verified:**

| base | 🟢 licence | bytes | use it for |
|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 `Apache-2.0` | `10 982` | a **full university LMS**, permissive — rare |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | `1 097` | **offline-first** delivery *(India Class `3`, LATAM low-connectivity)* |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 `Apache-2.0` | `11 358` | branching lessons with learner state |
| [`CTFd/CTFd`](https://github.com/CTFd/CTFd) | 🟢 `Apache-2.0` | `11 314` | graded challenges, teams, scoring |
| [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 `MIT` | `1 083` | autograding + per-student cloud IDE |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 `ECL-2.0` | `11 120` | 🟡 permissive, **patent grant scoped to education** |

🔴 **Never base a client deliverable on:** `canyongbs/advisingapp` *(`Elastic` — source-available,
and still the only AI-native higher-ed CRM here, with **no permissive replacement found**)*,
`TrenTorch/TrenTorch` *(`PolyForm` non-commercial)*, or the `3` NirDiamant tutorial repositories
*(non-commercial, byte-identical licences)*.

## Pass 195 — 2026-10-14

🆕 🟢 **Every pattern on this page inherits a licence gate from p194. This pass makes the gate
RUNNABLE OVER A WHOLE SHELF instead of over a payload at a time, and the cost is now
measured: `468` slugs, `2 167` probes, `0` throttles, one script run.**

🔴 **And the pass's own lesson goes at the top, because it is a pattern too:** p195 built a
band control whose entire finding set was already registered here as `P1054`, `P1056` and
`Gap 421`. 🟢 **`P0a` below is the step that would have prevented it, and it is now step one of
every engagement AND of every pass.**

### 🆕 🟢 `P0a` — Read the register before building the instrument *(10 minutes, before any code)*

```bash
# Run this BEFORE writing a classifier, a sweep, or a "new" control.
CLASS="licence narrowed clause commercial split-scope"      # the defect class, in words
ls compose/code/ | grep -iE 'licen|grant|clause|scope|family'
grep -rliE "$(echo "$CLASS" | tr ' ' '|')" compose/code/*/README.md | head
grep -rniE 'P1054|P1056|P171|P250|P237|Gap 421' agents/top.md repos/foundations.md \
     verticals/solutions.md intel/trends.md compose/patterns.md | head
```

🟢 **Exit condition: if any hit describes the defect, CITE it and spend the pass elsewhere.**
🔴 **p194 registered this failure one pass ago — *"it read p193's summary table as the state of
knowledge"* — and p195 repeated it against its own census TSV. Second consecutive recurrence,
which is why it is a gate and not advice.**

### 🟢 `P0b` — The licence gate, now at SHELF scale *(one script run, ~4 minutes for 468 repos)*

🔵 Wiring, concrete: [`compose/code/p195-shelf-licence-census/`](code/p195-shelf-licence-census/).

```bash
# 1. the CHANNEL — raw.githubusercontent.com.  Measured: 2 167 probes, 0 throttles, 0 refusals.
#    github.com HTML and api.github.com are BOTH refused at the proxy (403) — do not design on them.
# 2. the CLASSIFIER — sourced, never forked (P237).  207/207 assertions today.
. compose/code/lib/payload_measure.sh        # brings in lib/license_family.sh

# 3. the CENSUS — 19-filename root ladder, first 200 wins, status-gated.
cat slugs.txt | xargs -P 8 -I{} \
  bash compose/code/p195-shelf-licence-census/shelf_licence_census.sh --one {}

# 4. the TRIAGE — byte band inside the claimed family; flags modified grants for a human.
bash compose/code/p195-shelf-licence-census/delivery_verdict.sh <slug>
```

🔴 **Three guards that are not optional, each bought with a measured failure:**

| guard | the failure it prevents |
|---|---|
| 🔴 **Gate on the HTTP CODE, never on the body** | `raw.githubusercontent.com` returns a **`14`-byte `404: Not Found`** body. A classifier fed that without a status check will classify it. 🔵 `lib/probe_payload.sh:96` already guards this; p195's own spot-check forgot and had to retract a verdict mid-pass |
| 🔴 **`NONE` requires a CLEAN ladder** | if any probe returned `403`/`429`/`5xx`, the verdict is `INDETERMINATE`, never `NONE`. At census volume, *"all `404`"* is exactly what throttling forges |
| 🔴 **Walk the WHOLE ladder when the family is `UNCLASSIFIED`** | `shmercer/writeAlizer`'s first `200` is a **`47`-byte `usethis` template stub**; the real grant is `LICENSE.md`, `1 076` B, `MIT`. First-hit-wins loses it |

🟡 **And the limit, stated: this reads the ROOT only.**
[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) returns `NONE` at root and
carries `GPL-2.0` at `docs/License.txt` *(`17 286` B)*. 🔵 `p969-root-only-licence-reach`.

### 🟢 `P1` — The shelf-wide licence-provenance audit, as a sellable 2-week deliverable

🔵 **Who buys it:** any client with an inherited education codebase, in **every** region — this
is the one deliverable p195 can price identically for North America, EMEA, APAC and LATAM.

| step | what runs | what the client gets |
|---|---|---|
| `1` | `P0b` over the client's dependency slugs | a byte-verified licence column, **not an API field** |
| `2` | separate the `AGPL-3.0` set | 🔴 the rows where **self-hosting for a third party triggers disclosure** |
| `3` | separate the no-licence-at-root set, then probe `docs/`, `legal/`, `.github/` | 🔴 all-rights-reserved rows **vs** `p969` artefacts — a real distinction, measured |
| `4` | run the band triage | 🔴 the `≈6`% that need a lawyer's eyes, instead of `100`% |
| `5` | hand over the TSVs and the two scripts | the client can **re-run it**, which is what makes it an audit and not an opinion |

🟢 **Measured yield on this KB's own shelf: `41` Affero rows, `88` root-`NONE`, `5`
source-available, `2` non-commercial, `16` needing a human read out of `281` permissive.**
🔴 **Of `281` rows that a licence FIELD would have cleared, three bar commercial use outright.**

### 🟢 `P2` — A deliverable LMS, built only from rows that passed the gate

🔴 **Do not start from the installed base.** Open edX *(`AGPL-3.0`, `35 136` B)*, Canvas
*(`AGPL-3.0`, `34 520` B)* and `frappe/lms` *(`AGPL-3.0`, `33 893` B — **not `MIT`**, p193) all
reach a hosted deliverable's own modifications.

| role | repo | licence *(bytes, this pass)* |
|---|---|---|
| LMS core | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 `Apache-2.0` *(`10 982`)* |
| LMS core, alt | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 `ECL-2.0` *(`11 120`)* — patent grant scoped to education |
| offline / low-bandwidth | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` *(`1 097`)* |
| lecture capture | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 `ECL-2.0` *(`11 340`)* |
| learning record store | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 `MIT` *(`1 094`)* |
| sandboxed code execution | [`taybenlor/runno`](https://github.com/taybenlor/runno) | 🟢 `MIT` *(`1 106`)* — *"or via MCP"* |
| curriculum payload | `microsoft/ML-For-Beginners` · `generative-ai-for-beginners` · 🆕 `ai-agents-for-beginners` | 🟢 `MIT` *(`1 141`, one byte-identical file across all three)* |

🔵 **Wiring:** Sakai or OpenOLAT as the gradebook and roster of record → `runno` as the
execution sandbox the tutor calls → `ralph` as the xAPI sink that records every agent action
against a learner → the Microsoft curriculum set as the content the tutor teaches from.
🔴 **The glue is where the licence risk now lives** *(see T2)*: `1EdTech`'s LTI example tool and
`adlnet`'s SCORM→xAPI wrapper **grant nothing at root**, so write the adapter or get a grant in
writing — do not vendor them.

### 🟢 `P3` — LATAM: the `92`% / `26`% governance inventory *(6–8 weeks)*

🔵 **The measured premise:** `92`% of students and `79`% of faculty engaging with AI
*(Digital Education Council LATAM `2026`, >`30 000` responses)* against **`26`% of institutions
with a formal framework** *(UNESCO IESALC + UNU-IAS, `200` institutions, `19` countries)*.

| step | detail |
|---|---|
| `1` | inventory what is **already** in use — adoption is bottom-up, driven by individual academics and students, so the register comes before the policy |
| `2` | run `P0b` over every tool found; 🔴 expect source-available rows that look open in a search result |
| `3` | write the framework around actual use. 🔵 Name the instrument in every number — **framework `26`% ≠ published policy ≈`30`%** |
| `4` | instrument it: `ralph` *(`MIT`)* as the record, so the framework has evidence and not just prose |
| `5` | 🟡 target **private non-profits first** — `84`% adoption against `68`% public and `52`% private for-profit, and the planning capacity to buy |

🔴 **Do not build on `menthorlabs/menthor`** — still `archived: true`, third pass.
🟢 [`alcastaro/opendata-latam-mcp`](https://github.com/alcastaro/opendata-latam-mcp) is `MIT`
*(`1 557` B, band-checked)* and is the live LATAM-origin row.

### 🟢 `P4` — EMEA: the sovereign teaching stack *(10–12 weeks)*

🔵 **The constraint that drives it:** the EU AI Act puts education AI in the high-risk class,
and 🔴 **this KB has no `2026` EMEA vendor ranking after four passes of searching** — so sell
against the measured `31`-point intra-EU adoption spread, not against a market-share story.

| role | repo | why this one |
|---|---|---|
| agent teaching base | 🆕 [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) | 🟢 `MIT` *(`1 067` B)*, **local LLM, no cloud API calls** — the sovereignty shape, finally permissive. 🔴 `≈796`★: a starting point, not a dependency |
| LMS | `OpenOLAT` *(`Apache-2.0`)* or `Sakai` *(`ECL-2.0`)* | 🟢 permissive, so the Annex III obligations attach to the client's system and not to a copyleft upstream |
| record / audit | `openfun/ralph` *(`MIT`)* | 🟢 Art. `50` transparency needs an exportable record |
| curriculum | Microsoft `MIT` set | 🟢 one licence, three courses |

🟡 **Pitch workload, evidence outcomes.** Sanoma's `>20 000` teachers put AI's effect on
**learning outcomes** at `16`% while intent to use it for **preparing materials** rose — the
objection to pre-empt is measured, so lead with the teacher's time and prove the learner's
result separately.

### 🆕 🟢 `P5` — APAC: build for mandate REVERSIBILITY *(12–14 weeks)*

🔴 **New this pass, and Korea is the completed case.** An August `2025` law demoted Korea's AI
digital textbooks to **supplementary material**, uptake fell `37`% → `19`%, and ≈`10` publishers
sued for ≈`₩200` bn in June `2026`. 🟡 **The reported causes are classroom technical failure,
data-privacy objection and teacher/parent opposition — not model quality.**

| step | detail |
|---|---|
| `1` | 🔴 **Make the deliverable outlive the programme**: standards-based content *(QTI / SCORM / xAPI)* plus an exportable learner record. Nothing programme-specific in the data layer |
| `2` | 🟢 **Build to China's WRITTEN requirements as a spec**: curriculum from ≈age `6`, **minimum `8` h/year**, 🔴 **primary pupils barred from independent generative-AI use** — so the agent is **teacher-mediated by construction**, not by configuration — and teachers barred from replacing core teaching duties |
| `3` | 🟢 **Japan's window is dated**: `220` textbooks, `11` subjects, fiscal year from **April `2027`** |
| `4` | 🔴 **Treat APAC curriculum as content-licensed until read**: `microsoft/ai-edu` ships a **custom Chinese-language tutorial-materials notice**, not `MIT` *(`4 806` B, read this pass)* |
| `5` | 🔴 **Quote no APAC adoption rate.** This KB has none, two passes running |

### 🟢 `P6` — North America: the enforcement-evidence pattern *(4–6 weeks)*

🔵 **The premise, re-measured this pass:** there is **no sector regulator** — no FDA-equivalent
for edtech — state guidance is largely non-binding, and 🔴 **FERPA and COPPA carry the legal
weight.** So the sellable artefact is **evidence**, not policy.

| step | detail |
|---|---|
| `1` | `ralph` *(`MIT`)* as the LRS: every agent action against a student, exportable |
| `2` | agent layer **over** the Canvas API — 🔴 **never a fork**, `canvas-lms` is `AGPL-3.0` *(`34 520` B)* |
| `3` | 🔴 **a per-DISTRICT policy switch, not per-state**: `31` legislating states against Katy ISD's K-`6` ban and NYC's `8`th-grade moratorium |
| `4` | map the record to **FERPA/COPPA** obligations, and to California AB `1159` where student data must not train models |

### 🔴 What these patterns still cannot source from permissive OSS

| need | status |
|---|---|
| 🔴 **Student-success / advising CRM** | 🔴 **The only AI-native row is [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) and it is `Elastic`** *(`3 860` B, read this pass)* — source-available. **No permissive row exists** |
| 🔴 **Education ERP or SIS under MIT/Apache** | 🔴 Searched again this pass; **none**. `openeducat_erp` is `LGPL-3.0` *(`8 241` B)*, `openSIS` `GPL-2.0`, `rosariosis` `GPL-2.0`. 🟢 **Recommend the LGPL route openly**: a client's own modules link it without becoming copyleft |
| 🔴 **Licensed LTI / SCORM / xAPI reference implementations** | 🔴 `1EdTech` and `adlnet` reference repos **grant nothing at root** |
| 🔴 **Production-agent curriculum an enterprise may use** | 🔴 Unchanged from p194: the best-known corpus is **non-commercial** |
| 🔴 **A copyleft band for the triage control** | 🔴 No band for `AGPL-3.0`/`GPL-3.0`/`ECL-2.0`, so the **`77` copyleft rows are unchecked for `P1054`-style narrowing.** Pre-registered for p196 |
## Pass 194 — 2026-10-14

🆕 🔴 **Every pattern below now carries a licence gate as step `0`, because this pass measured
that `49.7`% of the stars on education's trending repositories carry no right to commercial
use.** 🟢 The gate is not new code — it is
[`compose/code/lib/license_family.sh`](code/lib/license_family.sh), this KB's hardened
classifier, `207`/`207` assertions today, which classified all `35` of this pass's payloads and
reached `NONCOMMERCIAL-NOT-OSI` on a bespoke licence it had never seen.

### 🟢 `P0` — The licence gate every other pattern starts with

🔵 **Two commands, and they are the two this KB already owns.** 🔴 Do **not** write a third
classifier: `P237` exists because passes `77` and `194` both did, and both reintroduced `P171`.

```sh
# 1. the licence CHANNEL — bytes, not a badge, not an API field
curl -sS -o LIC -w '%{http_code}' "https://raw.githubusercontent.com/$SLUG/HEAD/LICENSE"

# 2. the licence CLASSIFIER — title block, never the body
. compose/code/lib/license_family.sh
family_of "$(cat LIC)"      # -> MIT | Apache-2.0 | GPL-3.0 | AGPL-3.0 | ECL-2.0
                            #    LGPL-3.0 | CC-BY-4.0 | NONCOMMERCIAL-NOT-OSI | UNCLASSIFIED
```

🔵 **Why both halves.** The channel matters because `github.com`, `api.github.com` and
`codeload.github.com` are all `403` from this environment while the raw host is `200`. The
classifier matters because **GPL-3.0's §`13` names the Affero licence**, so a body grep marks
every GPLv3 payload `AGPL-3.0` — and a `404` on `LICENSE` alone is not *"unlicensed"* until
`19` filenames and the README have been probed *(this pass published four such verdicts that
way)*.

🔴 **Gate rule for a Globant engagement:** `NONCOMMERCIAL-NOT-OSI`, `CC-*-NC-*` and
`UNCLASSIFIED`-with-no-file are **STOP**. 🟡 `AGPL-3.0` is **ask** — permitted commercially, with
network-use disclosure. 🟢 `MIT`, `BSD`, `Apache-2.0`, `ECL-2.0` are **go**.

### 🟢 `P1` — A deliverable curriculum platform, built only from `go` rows

🔵 **The problem this solves:** a team that assembles the obvious best-known corpora ships a
course it cannot sell. 🔴 `RAG_Techniques` *(`29 858`★)*, `agents-towards-production`
*(`21 692`★)* and `prompt-eng-interactive-tutorial` *(`38 564`★)* are all **STOP** rows.

| layer | repo | licence *(bytes, this pass)* |
|---|---|---|
| curriculum | 🟢 [`microsoft/generative-ai-for-beginners`](https://github.com/microsoft/generative-ai-for-beginners) | 🟢 `MIT` *(`1 141` B)* |
| curriculum | 🟢 [`microsoft/ML-For-Beginners`](https://github.com/microsoft/ML-For-Beginners) | 🟢 `MIT` *(`1 141` B)* |
| graded exercises | 🟢 [`guipsamora/pandas_exercises`](https://github.com/guipsamora/pandas_exercises) | 🟢 `BSD-3-Clause` *(`1 515` B)* |
| **runs the learner's code** | 🟢 [`taybenlor/runno`](https://github.com/taybenlor/runno) | 🟢 `MIT` *(`1 106` B)* |
| delivery platform | 🟢 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 `ECL-2.0` *(`11 120` B)* |
| offline / low-bandwidth delivery | 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` *(`1 097` B)* |
| open-weight tutor models | 🟡 Qwen3.6-27B · Mistral-Small-4 | 🟡 `Apache-2.0` *(secondary — **gate before use**)* |

🔵 **Wiring.** `runno` is the keystone: it executes a learner's code **in the browser and over
MCP**, so the tutor agent grades by *running* a submission rather than by asking a model whether
it looks right. 🟢 `pandas_exercises` supplies tasks with known-good solutions → `runno` executes
both → the model explains the diff. 🔵 Curriculum from the two Microsoft `MIT` repos is delivered
through `sakai` *(`ECL-2.0`, permissive)* or `kolibri` *(`MIT`, offline-first)*.
🔴 **Not through `openedx` or `canvas` unless the client accepts Affero.**

🟡 **Honest limit:** this stack has **no assessment-integrity layer** and this KB has never
measured one trending. 🔴 It is build-not-buy, and should be scoped as such.

### 🟢 `P2` — The licence-provenance audit, as a sellable `2`-week deliverable

🔵 **Why it sells now, in every region:** `49.7`% of education's trending stars are
commercially barred, and a client's own inventory was almost certainly assembled from roundups.
🔴 This KB has corrected a published `MIT` that was Affero *(p193, `frappe/lms`)* and produced an
Affero that was GPL *(p194, `moodle`)* — **both from reading something other than the bytes.**

```
for each dependency and vendored corpus in the client's inventory:
  1. resolve the slug            -> raw lane, README.md 200/404 proves existence
  2. fetch the licence payload   -> raw lane, 19 candidate filenames
  3. classify                    -> lib/license_family.sh  (NEVER a fresh grep)
  4. record slug, path, BYTES, family, channel, date
  5. verdict: go / ask / STOP
```

🟢 **The byte count is the deliverable's integrity check**: it lets the next audit tell a
re-read from a restatement. 🔵 This pass's own output is the worked example —
[`evidence/licence-from-bytes-rawlane.2026-10-14-p194.tsv`](../evidence/licence-from-bytes-rawlane.2026-10-14-p194.tsv)
and [`evidence/libcross-license-family.2026-10-14-p194.tsv`](../evidence/libcross-license-family.2026-10-14-p194.tsv),
`35` payloads, `30`/`35` agreeing with the hardened classifier and `0` substantive divergences.

### 🟢 `P3` — LATAM: the `87`%-adoption / `26`%-strategy inventory

🔵 **The measured opening** *(UNESCO IESALC, `200` institutions, `19` countries)*: `87`% use AI
somewhere, `74`% in teaching and learning, **`26`% have a formal strategy**, adoption bottom-up.
🟢 **So the first deliverable is not a pilot — it is an inventory plus a governance frame over
use that is already happening.**

| layer | choice | why |
|---|---|---|
| delivery | 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) `MIT` | 🟢 offline-first — the durable permissive LATAM base |
| 🔴 avoid | [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor) `Apache-2.0` | 🔴 **ARCHIVED** — the only other permissive row with LATAM reach |
| Spanish study content | 🔴 [`midudev/libros-programacion-gratis`](https://github.com/midudev/libros-programacion-gratis) | 🔴 **no licence file** — **LINK, do not vendor** |
| counterparties | 🟢 UNESCO LAC Observatory *(Santiago, `2026-04-14`)* + CAF, CENIA, CETIC.br, ECLAC, Santillana, Tec de Monterrey, ProFuturo, Ceibal | 🟢 public-sector entry runs through these — **no region-wide education-AI regulation exists** |

🔵 **The Spanish-lane constraint is measured, not assumed:** the one Spanish-language education
repository trending this week carries no grant, and `45`% of LAC institutions have AI guidance
against `≈70`% in Europe and North America.

### 🟢 `P4` — EMEA: pick the licence before the `2027-12-02` Annex III date

🔵 **The measured opening:** teacher AI use `63`% *(Sanoma, `>20 000` teachers, `14` countries)*
while belief that AI improves **learning outcomes** sits at `16`%, flat across three waves.
🔴 **The buyer has bought adoption and has not bought evidence** — so the deliverable is measured
instructional effect, not another assistant.

| decision | 🟢 take | 🔴 instead of |
|---|---|---|
| LMS, client keeps its modifications | 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) `Apache-2.0` *(Switzerland)* · [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) `ECL-2.0` | 🔴 [`openedx`](https://github.com/openedx/openedx-platform) `AGPL-3.0` · [`canvas-lms`](https://github.com/instructure/canvas-lms) `AGPL-3.0` |
| lecture capture | 🟢 [`opencast/opencast`](https://github.com/opencast/opencast) `ECL-2.0` | — |
| existing Moodle estate | 🟢 **`GPL-3.0` — hosting a modified Moodle does NOT by itself trigger disclosure** | 🔴 **do not tell the client it is Affero** *(p194's own near-miss)* |

🔵 **Timing:** Annex III education obligations apply from **`2027-12-02`** *(p193, resolved by
convergence)* — so `2026`–`2027` is the architecture window. 🔴 **The `31`-point Eurostat spread
means a pan-European rollout priced off Nordic readiness fails in Romania, Italy and Bulgaria.**

### 🟢 `P5` — APAC: build to China's and Japan's written requirements

🔵 **China's MOE guidelines are an architecture specification, not a policy mood:** curriculum
from ≈age `6`, **minimum `8` hours a year** for the youngest cohort, **primary pupils barred from
using generative AI independently**, **teachers barred from using AI to replace core teaching
duties.**

🟢 **What that forces, concretely:** a **teacher-in-the-loop, pupil-indirect** design — the agent
drafts, a teacher releases; the pupil never holds an open generative session. 🔵 This KB's
standing accountability finding supplies the missing half: **a receipts layer that records who
released what**, since no measured agent layer can currently say who acted.

| layer | choice | note |
|---|---|---|
| hours/coverage tracking against the `8`-hour floor | 🟢 `sakai` `ECL-2.0` or `kolibri` `MIT` | 🟢 permissive |
| teacher-release gate + receipts | 🟢 build *(no permissive OSS measured)* | 🔴 named build-not-buy |
| 🔴 do **not** start from | [`frappe/lms`](https://github.com/frappe/lms) `AGPL-3.0` · [`openeducat_erp`](https://github.com/openeducat/openeducat_erp) `LGPL-3.0` | 🔴 both APAC-origin, **both copyleft** — p193's correction, re-verified from bytes this pass |

🆕 🟢 **Japan has a dated procurement window:** `220` textbooks across `11` subjects for the
fiscal year starting **April `2027`** passed second screening carrying generative-AI content —
localisation, adaptation and teacher training around that cohort is scoped and dated.
🔴 **Korea: assert nothing.** The rollout status is contested in this KB's own sources.

### 🟢 `P6` — North America: the enforcement-evidence pattern

🔵 **The measured opening:** `134` AI-in-education bills across `31` states, Ohio's district
framework deadline already passed, **California AB `1159`** *(bar student data for AI training)*
and **Oklahoma/Maryland** *(human oversight, no high-stakes AI decisions about students)* —
against two flagship districts running **moratoria**.

🟢 **All of those are audit obligations, and none is answered by a policy document.** The
deliverable is an evidence trail: **which model saw which student record, who approved the
action, and what the retention was** — on a permissive base *(`sakai` `ECL-2.0`, `kolibri`
`MIT`)*, with `P0`'s licence gate run over the client's existing inventory first.

🔴 **The one thing not to do:** satisfy an AB-`1159`-style obligation with a corpus that bars
commercial use. 🟢 `49.7`% of education's trending stars would fail that check, and `P0` catches
it in two commands.

### 🟡 What these patterns still cannot source from permissive OSS

🔴 **Assessment integrity / proctoring** — nothing permissive measured trending.
🔴 **Student-records (SIS/ERP)** — the permissive end of this market is LMS and lecture capture;
`openeducat_erp` is `LGPL-3.0` and `rosariosis` is `GPL-2.0`. 🔴 **Agent accountability receipts**
— standing gap, named build-not-buy for several passes. 🟡 **An eval layer** — the one candidate
measured, [`ahmedEid1/Lumen`](https://github.com/ahmedEid1/Lumen) *(`llm-as-judge` evals)*, is
`GPL-3.0`. 🟢 **Stated as gaps with their licences, so a scoping conversation starts from what is
missing rather than discovering it in week three.**

## Pass 193 — 2026-10-14

🆕 **Four new patterns. Three of them exist because this pass caught this KB making the exact
mistake each one prevents.**

### 🆕 🔴 Pattern 25 — The licence cliff gate *(half a day, run before any repo reaches a proposal)*

🔴 **The problem, with this pass's base rates rather than a worry:** `5` of `5` education
repositories created in `2026` above `300`★ have **no licence file at all**; `9` of `30` shelf
rows return `NOASSERTION` from GitHub's licence field and `1` returns `null`; and of those
`10`, **`4` hide a licence that bars or encumbers client delivery.** 🔵 **GitHub's licence
field has a `0`% hit rate on the cases that would stop a delivery.**

**Step 1 — read the licence from BYTES, never from the field.** Blobless, no checkout, one
clone per repo, seconds each:

```bash
licence() {                                   # licence <owner/repo>
  d=$(mktemp -d)
  git clone --filter=blob:none --no-checkout --depth 1 -q "https://github.com/$1" "$d" 2>/dev/null \
    || { echo "UNREACHABLE $1"; return; }
  f=$(git -C "$d" ls-tree HEAD --name-only | grep -iE '^(licen[sc]e|copying)' | head -1)
  if [ -z "$f" ]; then
    echo "NONE        $1  paths=$(git -C "$d" ls-tree -r HEAD --name-only | wc -l)"   # all rights reserved
  else
    echo "$(git -C "$d" cat-file -p HEAD:$f | grep -viE '^\s*$' | head -1 | cut -c1-60)  [$(git -C "$d" cat-file -s HEAD:$f) B]  $1"
  fi
  rm -rf "$d"
}
```

**Step 2 — classify into THREE buckets, not two.** 🔴 `NONE` is not *"permissive by
default"*, it is all rights reserved; `NOASSERTION` is **UNREAD**, not *"unknown, probably
fine"*.

| bucket | what it means for delivery | examples measured this pass |
|---|---|---|
| 🟢 **permissive** | build, modify, deliver, keep changes | `OpenOLAT` `Apache-2.0`, `sakai` `ECL-2.0`, `kolibri` `MIT`, `runno` `MIT` |
| 🟡 **copyleft — architecture decision** | usable, but decide the boundary in the PROPOSAL | `frappe/lms` `AGPL-3.0`, `openeducat_erp` `LGPL-3.0`, `moodle` `GPL-3.0` |
| 🔴 **barred or unread** | do not quote, do not plan a sprint | `enkidevs/curriculum` `CC-BY-NC-SA`, `PageLM` community licence, `Mr.-Ranedeer` **none**, `advisingapp` **unread** |

**Step 3 — byte size is a tell.** 🔵 A file claiming `MIT` that is `8 563` B is not MIT
*(`PageLM`)*; `MIT` is ≈`1 070` B and Apache-2.0 ≈`11 300` B. 🔴 A `189` B licence file is a
sentence, and the sentence is usually `NonCommercial`.

🟢 **Wire it to Pattern 24** *(existence probe)*: `ls-remote` says `LIVE`/`EMPTY`/`ABSENT`,
this says `PERMISSIVE`/`COPYLEFT`/`BARRED`, and the recovered channel adds `archived`. Three
gates, one pre-engagement script, every row on the shelf priced before the estimate.

### 🆕 🟢 Pattern 26 — The four-lane channel probe *(one hour, run before declaring any source dead)*

🔴 **The problem it prevents, measured on this KB:** thirteen passes published *"GitHub
Trending: NOT MEASURED"* and one published *"the API is gone"*. 🔵 **Both were a gated lane
inside the measuring environment.** The trending surface answered on the first try through a
lane that had never been separated out.

**Step 1 — read the error BODY, not the status code.**

```bash
curl -sS -o body.json -w 'code=%{http_code} ip=%{remote_ip}\n' "$URL"; cat body.json
```

🔵 This pass: `403`, `249` B, and the body said
*"sessions are bound to their configured repositories"* — 🟢 **an intermediary refusing a
path, in vocabulary GitHub does not use.**

**Step 2 — ask the gate something it WILL answer.** `gh api rate_limit` returned a complete
live quota *(`core 15 000/15 000`, `search 30/30`)* — 🟢 **proving the credential was valid
and entirely unspent.** 🔴 A dead channel cannot return a live quota.

**Step 3 — enumerate the lanes separately and record each one's verdict.**

| lane | probe | this pass |
|---|---|---|
| direct `HTTP` | `curl` | 🔴 `403` *(gated)* |
| CLI | `gh api` | 🔴 `403` *(same gate)* |
| MCP server | `search_repositories` | 🟢 open — `30`/`30` rows with stars |
| page fetch | agent fetch of the HTML surface | 🟢 **open — trending recovered** |

**Step 4 — distinguish *gated* from *unreachable*, because the follow-up differs.**
🔵 `curl -w '%{remote_ip}'`: six government hosts all resolved to **`127.0.0.1`** — a DNS
null-route. 🔴 **Gated → try another lane. Null-routed → stop spending calls, record as
structurally unreachable.**

🟢 **The deliverable is a one-page channel register per engagement**, listing lane × source ×
verdict × date. 🔴 Without it, a `0` from a blocked lane is published as a fact about the
world, and nobody downstream can tell the difference.

### 🆕 🔴 Pattern 27 — EMEA Art. `50` estate triage *(2 weeks, deadline already passed)*

🔴 **The problem:** nearly every briefing — this KB's own p192 included — quotes
**`2026-12-02`** for AI transparency marking. 🔵 **That is the date for generative systems
ALREADY on the market.** 🔴 **Anything placed on the market after `2026-08-02` has been in
scope for ten weeks.**

**Step 1 — inventory with PLACEMENT DATES, which almost no institution has.** Pull the
deployed estate from the platform the client already runs:
🔵 `moodle/moodle` *(plugin register + install dates)*, `chamilo/chamilo-lms` *(`68` native
MCP tool definitions, `47` of them writes)*, `instructure/canvas-lms` *(LTI registrations)*,
`openedx/openedx-platform` *(XBlock install log)*.

**Step 2 — split into the two cohorts.**

| cohort | obligation | date |
|---|---|---|
| 🔴 placed on market after `2026-08-02` | Art. `50` marking | **in force now** |
| 🟡 generative, already on market before it | Art. `50` marking | `2026-12-02` |
| 🔵 Annex III *(admissions, grading, learning-outcome evaluation, level-of-education decisions)* | full high-risk regime | `2027-12-02` — Reg. (EU) `2026/1744`, substance unchanged |
| 🔴 emotion recognition in education | **prohibited** | live since `2025-02-02` |

**Step 3 — make the marking auditable, not just present.** 🔵 Wire
[`openfun/ralph`](https://github.com/openfun/ralph) *(`Apache-2.0`, LRS)* behind the estate so
each AI interaction emits an xAPI statement carrying the system identifier and its placement
cohort. 🔴 **Marking that cannot be evidenced after the fact is a screenshot, not a control.**

**Step 4 — the `2027-12-02` programme follows from the same inventory**, which is why the
triage is sold first and the conformity work second.

🟢 **Why it closes: the trigger has already fired, the client almost certainly believes it has
not, and the evidence either exists in the LMS or does not — a two-week scope with a binary
answer.**

### 🆕 🟡 Pattern 28 — The Affero-safe APAC architecture *(2–3 weeks of design, before any code)*

🔴 **The problem this pass created and then caught:** p192 recommended an APAC engagement
start on `frappe/lms` *"permissively licensed"*. 🔴 **It is `AGPL-3.0`** *(`license.txt`,
`33 893` B)*. 🔵 **Affero reaches modifications served over a network** — on a hosted LMS,
that is the client's own differentiating work.

**Step 1 — keep the copyleft platform as a PLATFORM and nothing more.** Run
[`frappe/lms`](https://github.com/frappe/lms) *(`AGPL-3.0`)* or
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) *(`LGPL-3.0`,
Odoo-based)* unmodified, at a pinned release. 🔴 **Every line added inside that tree is a line
you may owe its users.**

**Step 2 — put the proprietary work in a separate service, across a network boundary.**
Agent-side, permissively licensed, talking to the platform through its public API or an MCP
adapter: 🔵 [`taybenlor/runno`](https://github.com/taybenlor/runno) *(`MIT`)* for sandboxed
code execution, [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit)
*(`MIT`)* for knowledge tracing, [`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server)
*(`Apache-2.0`)* as the worked example of a domain tutor exposed over MCP.

**Step 3 — if the client wants the platform itself modified, change platform.** 🟢
[`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) *(`Apache-2.0`)* and
[`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) *(`ECL-2.0`)* are the two
fork-safe platforms on this shelf. 🔴 Neither is APAC-origin, and saying so early is cheaper
than saying it at handover.

**Step 4 — reference design, explicitly not a dependency.**
[`jude-miller-dev/Milky-institute-online`](https://github.com/jude-miller-dev/Milky-institute-online)
*(`367`★, `786` paths, Spring Cloud, course-recommendation agent as a first-class service)*
shows the service split an APAC institutional LMS wants. 🔴 **It has no licence file — read it
for the architecture, clone nothing.**

🟢 **The decision this pattern forces into the proposal — platform modified vs. platform
wrapped — is the one that costs the most to reverse, and `AGPL` vs `MIT` is a single word in
a table that nobody re-reads.** 🔵 This pass is the proof: the word was wrong for one pass and
it inverted a regional recommendation.
## Pass 192 — 2026-10-14

🆕 **Three new patterns, all built from what the recovered channel makes possible, plus one
amendment to `Pattern 2`.**

### 🆕 🟢 Pattern 24 — The pre-engagement shelf audit *(1 day, run before the estimate)*

🔴 **The problem it prevents, measured on this KB's own `472`-row shelf:** `5` of `12`
vertical platforms do not default to `main`/`master`; `1` canonical slug is a rename that
clones fine forever; `4` repositories are published under two spellings; `2` published rows
are empty repositories; and a `833`★ curriculum repo is `NonCommercial`. 🔵 **Every one of
those is discovered on day `1` of delivery or day `1` of the audit. The price difference is
the pattern.**

**Step 1 — existence, with the exit code as the verdict.** 🔴 **Not `wc -l`:**

```bash
# three states, not two: LIVE / EMPTY / ABSENT
probe() {
  out=$(git ls-remote "https://github.com/$1" 2>/dev/null); rc=$?
  if   [ "$rc" -ne 0 ];                        then echo "ABSENT $1"   # exit 128
  elif [ -z "$out" ];                          then echo "EMPTY  $1"   # resolves, 0 refs
  else echo "LIVE   $1 $(echo "$out" | head -1 | cut -c1-12)"; fi
}
```

🔵 **`git ls-remote … | wc -l` prints `0` for ABSENT and `0` for EMPTY** — the `fatal:` goes to
stderr. This KB read `0 refs` as *"does not exist"* in `706` places because its negative
controls only ever tested absent repositories.

**Step 2 — rename and duplicate detection, free, over step 1's output.** Group by HEAD sha;
any sha claimed by two slugs is a rename *(GitHub redirects the old name silently)* or an
owner-case variant *(two entities for one repository, downstream)*.

**Step 3 — `archived` and `default_branch`, which git cannot see.** One search call per
batch of repos; assert `len(items) == len(repo: qualifiers)` and re-probe the difference
**singly**, because a batch drops unresolvable slugs without erroring and the singleton
reports `Validation Failed`.

**Step 4 — licence from bytes, never from a badge or an API field:**

```bash
git clone --filter=blob:none --no-checkout --depth 1 -q "https://github.com/$SLUG" t
git -C t ls-tree -r --name-only HEAD | grep -iE '^(LICEN[CS]E|COPYING)'
git -C t cat-file -s "HEAD:LICENSE"   # size, so a 189 B one-liner is visible as such
git -C t show   "HEAD:LICENSE"
```

🟢 **Deliverable: a four-column table — `exists` / `live` / `licence id + bytes` /
`default_branch` — for every repository in the proposed architecture.** 🔵 `enkidevs/curriculum`
fails column `3` at `189` bytes; `menthorlabs/menthor` fails column `2`; both Ed-Fi rows fail
column `1`.

### 🆕 🟢 Pattern 25 — A tutor that can RUN the learner's work

🔴 **What every AI-tutor demo lacks:** the tutor discusses code it cannot execute, so it
cannot see a failure it did not predict. 🟢 **Two permissive repositories close it, both
MCP-reachable:**

| component | repo | licence *(bytes)* | role |
|---|---|---|---|
| sandbox | [`taybenlor/runno`](https://github.com/taybenlor/runno) | `MIT` *(`1 106` B)* | WASI/WASM execution **in the browser or over MCP** — no server-side code execution to secure |
| domain tutor | [`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server) | `Apache-2.0` *(`10 708` B)* | the worked reference: a real solver behind Socratic questioning |
| learner model | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | `MIT` | knowledge tracing over the attempt stream |
| record | [`openfun/ralph`](https://github.com/openfun/ralph) | — | xAPI LRS for the attempt + verdict events |

**Wiring:** learner submits → `runno` executes in the sandbox and returns **stdout, stderr and
exit code** → the tutor agent receives the *verdict*, not the prediction → it questions
against the actual failure → each attempt is emitted as an xAPI statement to `ralph` → `pykt`
consumes the stream for mastery estimates.

🔴 **The accountability caveat this KB has proven `8` passes running: `ralph` cannot compare
the asserting authority, so the statement says the learner acted when the AGENT acted.**
🟢 Fix it in the integration layer: stamp an agent actor and the tool-call id on every
statement before `ralph` sees it, and keep the learner as `object`-side context. 🔵 Do not
expect the LRS to do it — the dedupe exclusion is mandated by the xAPI spec itself.

### 🆕 🟡 Pattern 26 — Skill-layer pedagogy over a harness the client already has

🔵 **The trend from `intel/trends.md` T1, as a buildable recipe.** The unit is a few files of
pedagogy, not a deployment:

| component | repo | licence | 🔴 the licence constraint that decides the architecture |
|---|---|---|---|
| skill corpus | [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `CC-BY-SA-4.0` *(`1 230` B)* | 🔴 **ShareAlike = copyleft on CONTENT.** Derived skills must be shared alike — fine for a client's internal corpus, 🔴 **not** for a proprietary product |
| index | [`O0000-code/awesome-academic-skills`](https://github.com/O0000-code/awesome-academic-skills) | `CC0-1.0` | 🟢 public domain — liftable wholesale |
| code-explanation skill | [`mohi-devhub/antivibe`](https://github.com/mohi-devhub/antivibe) | `MIT` *(`1 065` B)* | 🟢 `15` paths; `MIT`, so it can be absorbed into a product |
| adaptive tutor | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | *(see this KB's licence register)* | self-hostable web app + skill |
| 🔴 **excluded** | [`enkidevs/curriculum`](https://github.com/enkidevs/curriculum) | `CC-BY-NC-SA-4.0` | 🔴 `NonCommercial` — **bars client delivery entirely.** `833`★ and `5 345` paths of content nobody can bill against |

🟢 **The architecture decision falls out of the licence column, not the feature column:** put
`CC-BY-SA` content in the client's own corpus and keep the `MIT`/`CC0` pieces in anything
shipped. 🔵 **Run Pattern 24 step `4` on every skill repo before designing**, because this
layer's assets are content, and content is `CC-*` until its bytes say otherwise.

### 🟡 Amendment to Pattern 2 *(Chamilo Art. `50(2)` marking retrofit)*

🟢 **Add Pattern 24 as step `0`, and the reason is specific.** Chamilo's `default_branch` is
`master`; Moodle `5.3`'s tree is now `public/`-prefixed; `openedx/edx-platform` is a rename
that still clones. 🔴 **A marking retrofit is a path-rooted change across an estate**, so a
runbook that assumes `main` and stable paths breaks on `42`% of this shelf — after the
estimate is signed. 🔵 The retrofit itself is unchanged: `47` write tools, `0` audit rows, no
confirm handshake, `2026-12-02`.
## Pass 191 — 2026-10-14

🆕 🟢 **One new pattern, and three amendments — two of them REPRICING steps this KB published
yesterday, one of them a licence correction that changes nothing commercially and had to be
made anyway.** Every repository named below was read at a pinned `HEAD` this pass, or had its
grant read over `raw.githubusercontent.com` with the HTTP code checked.

### 🆕 Pattern `37` — governing an agent layer the platform already shipped *(4–6 weeks)*

🔴 **The premise changed under this KB's feet.** Patterns `35` and `36` assume the studio
*chooses* an MCP server. Chamilo `2.1.0` ships `68` tool definitions natively, `47` of them
writes, with `0` audit rows. 🟢 **So the deliverable is no longer an agent; it is the
accountability layer around one that is already there.**

| step | what it is | built from | measured basis |
|---|---|---|---|
| `1` | 🔴 **Count the surface from DEFINITIONS, never from the docs.** `#[McpTool(name:)]` attributes in `src/CoreBundle/Mcp/` and `src/CoreBundle/Service/Mcp/` | [`P1060`](code/p191-chamilo-agent-surface/README.md) *(`16`/`16` controls)* | `68` tools found; the server's own `instructions:` block names **`0`** of them |
| `2` | 🟢 **Read the role gate and the default allowlist.** `McpAccessPolicy::DEFAULT_ALLOWED_ROLES` — `ADMIN` and `COURSEMANAGER` true, five roles false — and confirm `security.mcp_enabled` is the kill switch | `src/CoreBundle/Service/Mcp/McpAccessPolicy.php`, `McpServerAccessSubscriber.php` | malformed JSON **fails closed**; `/mcp` returns `404` when disabled |
| `2a` | 🔴 **Classify the `47` writes by REVERSIBILITY, by hand, and write the list down.** This is the step `Gap 438` and `Gap 442` exist to force | the write list in [`result.2026-10-14.tsv`](code/p191-chamilo-agent-surface/result.2026-10-14.tsv) | Open edX got this wrong in one release and has not noticed in four |
| `3` | 🔴 **Put a scoped-key gateway in front of `/mcp`**, because the platform cannot narrow a key below the user. One key per `(tool-set, purpose)`, mapped to a Chamilo service account per role | `compose/code/mcp-allowlist-gateway` *(this KB's own)* | `McpAccessPolicy::canUse()` is **one boolean for `68` tools** |
| `4` | 🔴 **Add the audit row the platform does not write** — tool, caller, key id, payload digest, outcome, before the write — and make the gateway refuse the call if the row cannot persist | `openedx-mcp`'s own ordering is the reference design | `0` `audit` and `0` logger references across `67` Chamilo MCP sources |
| `5` | 🟡 **Add a confirm handshake for the irreversible subset from `2a`.** Bind the token to `sha256(tool, user, payload)` so one changed byte invalidates it | `openedx-mcp` `guards.py` `issue_confirm_token` / `consume_confirm_token` | `confirm` occurs in Chamilo tool DESCRIPTIONS and in `0` enforcement sites |
| `6` | 🔴 **Gate `generate_student_success_feedback` behind a human sign-off** and keep the draft out of the learner's record until signed | `compose/code/grading-draft-gate` *(this KB's own)* | AI feedback about a named learner is **Annex III point `3` by name**, duty `2027-12-02` |
| `7` | 🟢 **Keep the credential model; do not rebuild it.** `sha256(random_bytes(32))`, `hash_equals`, masked display, `revokedAt`, `lastUsedAt`, plus OAuth 2.1 at `/.well-known/oauth-protected-resource/mcp` | the platform, unchanged | 🟢 this is the half Chamilo already does properly — rebuilding it is waste |

🔵 **Why `4` before `5`:** a confirm handshake without an audit row tells you an action was
approved and still not who approved it. 🔴 **And both are cheaper than they look** — the
gateway is one reverse proxy and one table — **because the platform supplies the hard half:
`48` enforced role checks in `18` of `67` files, which this pattern does not re-implement.**

### 🔴 Amendment to Pattern `35` *(Open edX agent layer)* — step `2a` is now MANDATORY, and the version is pinned

🟢 `ACTION NL` and `ACTION NM` closed from five `sha256`-verified sdists, and the result makes
the step unavoidable rather than advisable:

- 🔴 **`reset_attempts` has carried `write:users` without `destructive` since `0.1.1`**, and
  `tool_views.py` is byte-identical `0.1.2` → `0.1.5`. There is no release in which this was
  right, so **no version pin fixes it** — the gateway must add the scope.
- 🔴 **`has_delete_permission` is absent from all five releases** and `admin.py` is
  byte-identical from `0.1.2` *(`sha256` `3be322597768`)*. The audit log's delete path has
  never been guarded. Step: override it in the deployment, and remove Django's default bulk
  delete action.
- 🟢 **Pin `0.1.5` anyway**, and record the digest *(`bfc7e7b0e3b1f1fe…`)*: the package
  declares **no repository address and ships no changelog**, so a digest is the only identity
  the artefact has. 🔵 Bus factor `1`, and that belongs in the risk register, not a footnote.

### 🆕 Amendment to Pattern `36` *(the learner-record trail)* — step `6` is MANDATORY, and the reason is the SPECIFICATION

🟢 `ACTION NP` closes limb `1` and **corrects this KB's own framing**: `openfun/ralph` *does*
enforce authority — it is server-assigned on write unless the caller holds `authority/write`,
and all four backends filter by it on read. 🔴 **But `statements_are_equivalent` excludes
`authority` because the xAPI specification excludes it**, by ralph's own docstring. 🔵 **So
the hole is in the standard and is present in every conforming LRS; no vendor can patch you
out of it.**

| step | change | why |
|---|---|---|
| `6` | 🔴 **MANDATORY: compare the asserting `authority` in your own ingest layer before you `PUT`**, and reject a re-`PUT` from a different authority instead of letting the LRS answer `204` | the LRS is *conforming* when it discards it; your integration is the only place the comparison can live |
| 🆕 `6a` | 🔴 **NEW: never forward a `PUT` through ralph if attribution matters downstream.** `POST` enriches authority then forwards; `PUT` forwards then enriches, and `forwarding.py` sends `json=statements` verbatim — so a forwarded `PUT` carries the client's own unvalidated `authority` while the local copy is correct | two call orders, eleven lines apart, in `api/routers/statements.py` |
| 🆕 `6b` | 🟡 **NEW: treat the `all` scope as `authority/write`.** `UserScopes.is_authorized` expands `all` to include it, so a convenience key can assert any agent as the asserting authority | `src/ralph/api/auth/user.py:47` |

### 🟢 Amendment to every pattern naming `GemMate` — the licence was wrong, the pattern is not

🔴 [`linyeping/GemMate`](https://github.com/linyeping/GemMate) is **`Apache-2.0`**
*(`LICENSE`, `11 305` B)*, not the `MIT` this file published twice since p172. 🟢 **Both
remain permissive, so no step and no estimate changes** — and the correction is made anyway,
because a licence column that is right about the family and wrong about the id is still a
licence column a client's counsel will read. 🔵 Last commit `2026-05-21`: the dormancy that
`ACTION NV` will measure shelf-wide is already visible on this row.

### 🟡 And one composition this pass can now name honestly

🟢 [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
*(`165` skills, `20` domains, `CC-BY-SA-4.0`)* composes with
[`O0000-code/awesome-academic-skills`](https://github.com/O0000-code/awesome-academic-skills)
*(`CC0-1.0`)* and [`kvnloo/tutor-mcp`](https://github.com/kvnloo/tutor-mcp) *(`MIT`)* into a
pedagogy layer over any platform's agent surface. 🔴 **With one hard boundary: `CC-BY-SA` is
copyleft on CONTENT.** Prompts and skill text derived from it must be licensed alike, so it
belongs in a client's *configuration*, never inside a proprietary deliverable. 🟢 The `CC0`
index has no such constraint and can be lifted wholesale.

## Pass 190 — 2026-10-14

🆕 🟢 **One new pattern, and three amendments that REPRICE steps this KB published
yesterday — two of them CHEAPER because a control turned out to exist, one of them newly
MANDATORY because a control turned out to be missing. Every repository named below was read
as source at a pinned `HEAD` this pass, or had its grant read over
`raw.githubusercontent.com/<slug>/HEAD/<path>` with the HTTP code checked.**

### 🔴 Amendment `1` — Pattern `35` step `1` must ENUMERATE. It may never scope from a README

🟢 Step `1` already said *"enumerate from the server's own definitions, not its README"*.
`ACTION NF` was pre-registered to test whether that caution was necessary or merely prudent.
🔴 **It is necessary, and the margin is larger than drift:**

| | measured |
|---|---|
| tool definitions in the build | 🆕 **`33`** — `14` reads, `19` writes |
| tool names in the README | 🔴 **`0`.** It carries `8` DOMAIN LABELS in an ASCII diagram and defers tool docs to a PyPI README |
| 🔴 and p189's own cell marked *"verbatim"* | dropped `reports` from those labels — which is where the pre-registered figure `7` came from |

🟢 **Step `1` is REWRITTEN as a hard gate: scope from `@mcp.tool()` / `audited_write`
definitions, and record the count. If a README names no tools, say so — do not infer a
surface from a diagram.** 🟡 **The audit estimate rises from `2`–`3` weeks to `3`–`4`** for a
server of this size, because `19` write tools each need a scope, a reversibility and a
confirm-state read, and that is now `19` rows of work rather than `6`.

### 🟢 Amendment `2` — Pattern `35` steps `3`, `4` and `6` get CHEAPER on this platform

🔴 Step `3` published *"On the Open edX facade, nothing — `is_staff` is the whole control"*.
🟢 **REFUTED from the code.** [`openedx-mcp`](https://pypi.org/project/openedx-mcp/) `0.1.5`
*(`AGPL-3.0`; sdist `43 185` B, **`sha256` verified** against PyPI's declared digest)*
carries, enforced:

| control | where |
|---|---|
| 🟢 **nine scopes** — `read`, `write:enrollment`, `write:users`, `write:roles`, `grant:admin`, `write:certificates`, `write:reports`, `write:courses`, `destructive` | `models.py` `Scope`, enforced by `auth.require_scopes()` |
| 🟢 **`destructive` is ADDITIVE** — a delete needs its domain scope **and** `destructive` | `guards.audited_write` |
| 🟢 **single-use confirm token** bound to a `sha256` of `(tool, user, payload)`; one changed byte invalidates it | `_rails.issue/consume_confirm_token` |
| 🟢 **per-`(key,tool)` rate limits** tuned to blast radius — `bulk_enroll` `5`/`300`s, `request_retirement` `5`/`600`s | `_rails.RATE_LIMITS` |
| 🟢 **audit row written BEFORE the write**, write refused if it cannot persist | `guards.audited_write` |
| 🟢 **keys `SHA-256`-hashed, shown once, revocable, expiring, privilege re-checked LIVE** | `models.MCPKey`, `auth.MCPKeyAuthentication` |

🟢 **So step `4`'s allowlist gateway drops from "build it" to "configure the scopes that
already exist" — days, not weeks — and step `3` can be demonstrated to a client as a
`403` with `{"required": […], "missing": […]}` rather than built.** 🟢 Step `6` stands:
`/health` really is unauthenticated, by name, in `auth.py`.

🔵 **The method note that earns its place: p189 read the LICENCE from bytes and the AUTH
MODEL from a README in the same pass, and published both at the same confidence. The licence
held; the auth model did not.** A README's security sentence is a claim. A decorator is a fact.

### 🔴 Amendment `3` — Pattern `35` step `2` gains TWO mandatory sub-steps, and they are the ones that bite

🔴 **`2a` — classify by REVERSIBILITY, from the code, never from the scope's NAME.** On this
very platform the guard is **inverted on the pair that matters**:

| tool | scope | `destructive`? | reality |
|---|---|---|---|
| 🔴 `reset_student_attempts` *(audits as `reset_attempts`)* | `write:users` | 🔴 **NO** | `delete_module=True` **deletes the learner's `StudentModule` row** — their submitted state for that block — and fires score-changed signals. **No undo** |
| 🟢 `deactivate_user` | `write:users` | 🟢 **YES** | flips `is_active=False`; `request_retirement`'s own docstring calls it *"the reversible `is_active` flag"* |

🔵 **A key minted `["read","write:users"]` specifically so it cannot delete CAN delete a
learner's work, and CANNOT deactivate an account.** 🟢 Deliverable: a reversibility table per
tool, signed by the client, before any key is minted.

🔴 **`2b` — EU work: run the emotion-inference screen, and report CLASS A and CLASS B
separately.** Use [`p190-affect-inference-scan`](code/p190-affect-inference-scan/README.md)
*(`P1058`, `19`/`19` tests)*. 🔴 **Art. `5(1)(f)` is a live PROHIBITION since `2025-02-02` at
EUR `35`M or `7`% of worldwide turnover and was NOT deferred by the Omnibus.** 🟢 `ACTION NH`
measured this KB's three proctoring rows: **all three CLEAR** — 🔴 **one of them only because
`outputFaceBlendshapes` defaults to `false`.** 🔵 **`outputFaceBlendshapes: true` is ONE LINE
that moves a system from a `2027` duty into a live prohibition. That single sentence is the
screen's commercial justification.** 🔴 And report CLASS B *(face, gaze, head pose)* as an
Annex III **duty**, never as a prohibition: a CLASS B hit misreported blocks a usable row.

### 🆕 🟢 Pattern `36` — the agent ATTRIBUTION audit: who acted, and can it be erased?

🔵 **Why it exists.** p189 asserted that nobody protects the durable record of a human
decision about a learner. 🔴 **p190 measured two unrelated codebases and the claim is wrong
in an instructive way: both DO protect the record. Neither protects the ACTOR.** That is a
narrower, demonstrable, vendor-neutral finding — and it is the one a regulator, a DPO or an
exam board actually asks about, because a trail that cannot say **who** is not a trail.

| step | component | licence, as measured this pass | what it does |
|---|---|---|---|
| `1` | 🟢 **Find the attribution columns.** In every audit or statement store, list the fields naming the ACTOR, and for each ask: is it compared, and can it be deleted? | — | 🔵 one table. It is the whole deliverable of step `1` |
| `2` | 🔴 **Read the DELETE path, not just the write path.** On [`openedx-mcp`](https://pypi.org/project/openedx-mcp/): `MCPAuditLogAdmin` blocks `add` and `change` and freezes every field — and **never overrides `has_delete_permission`**, which Django defaults to `user.has_perm("delete_mcpauditlog")`, with the default **"Delete selected objects"** bulk action intact | 🔴 `AGPL-3.0` *(`34 524` B)* | 🔵 `add`, `change`, `delete` — enumerate all three. One of the three is where this fails |
| `3` | 🔴 **Read the CASCADE.** `MCPAuditLog.key` and `.user` are `on_delete=models.SET_NULL`: **deleting a key or a user NULLs attribution on every row it produced** — no delete permission on the log required | 🔴 same | 🔴 **The second path, and the one nobody looks for.** Change to `PROTECT`, or snapshot actor identity into the row at write time |
| `4` | 🔴 **Read the EQUIVALENCE function, not only the conflict response.** [`openfun/ralph`](https://github.com/openfun/ralph)'s `statements_are_equivalent` *(`src/ralph/utils.py:167`)* compares `{actor, verb, object, id, result, context, attachments}` plus `timestamp`/`version` **only when present in both** — and **excludes `authority` and `stored` by name** | 🟢 **`MIT`** — 🆕 `LICENSE.md` `1 094` B, complete grant read this pass *(`LICENSE` itself `404`s)* | 🔴 A re-`PUT` differing only in `authority` answers **`204` and is SILENTLY DISCARDED**. The record is safe; the conflicting claim vanishes |
| `5` | 🟢 **Snapshot the actor, do not reference it.** Write actor identity as immutable text into the record *(and into the object-lock copy from Pattern `32` step `3b`)*, so no cascade can null it | — | 🟢 the cheapest durable fix in this pattern |
| `6` | 🟢 **Reject on attribution mismatch at ingest.** Mint statement ids per authority, or refuse a duplicate id from a different authority instead of answering `204` | — | 🟢 one guard in the ingest proxy. **Adds no weeks** |
| `7` | 🔴 **Tie retention to retirement.** `_rails.redact()` redacts `{confirm_token, password, key, secret, token}` and **NOT `username` or `email`** — so `request_retirement`'s own audit row **permanently stores the username of a learner retired to remove their PII**, and no hook connects the two | 🔴 `AGPL-3.0` | 🔴 **The first question a DPO asks, and it is answerable from source.** One retention rule, one redaction entry |
| `8` | 🟢 **Anchor what must outlive the platform** as `OB 3.0` / W3C VCs: [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget), [`brody-0125/signet-campus`](https://github.com/brody-0125/signet-campus), [`iblai/wallet`](https://github.com/iblai/wallet) | 🟢 all **`MIT`** | 🔵 attribution durable by **cryptography**, not by an admin permission |

🟡 **Estimate: `2` weeks for steps `1`–`4`** *(the read — and it is a READ, so it is quotable
at fixed price)*, **`+2`–`3` for `5`–`7`**, **`+3`–`4` for `8`** where credentials must be
portable. 🟢 **Steps `1`–`4` produce the document that justifies the rest, exactly as in
Pattern `35`.**

🔵 **Where it applies by region.**
🔴 **EU** — Annex III education duties *(admissions, evaluation of learning outcomes, student
placement, exam/behaviour monitoring)* land `2027-12-02`, but **`Art. 50` transparency and
the GPAI obligations have been LIVE since `2026-08-02`** and **`Art. 50(2)` marking is due
`2026-12-02` — seven weeks out**; pair this pattern with the four `aiact-50-2-*` instruments
this KB already ships.
🔴 **APAC first, not last** — **Vietnam** names automated assessment and behavioural
monitoring high-risk with compliance by **`2027-03-01`** *(grace only for systems running
before `2026-08-15`)*, **nine months BEFORE the EU**; **Korea's** AI Basic Act *(in force
`2026-01-22`)* requires **human monitoring and intervention**, which steps `5`–`6` evidence
directly.
🟢 **North America** — Ohio, Tennessee and Oklahoma require district AI policies and Oklahoma
bars AI as the **main basis** for a high-stakes decision about a student; 🔴 sell against a
buyer whose enthusiasm **fell nine points** *(US/Canada faculty intent `76`% → `67`%)*, so
lead with trust, not capability. Maryland's **district AI coordinators** are the named buyer.
🟢 **LATAM** — no national rule in Brazil, Mexico, Colombia or Chile, so this is **risk
management**, not compliance; it lands on an installed base that is already permissive
*(`38`% of organisations use open-source AI; Mexico `65`%, Brazil `46`%)* and already
using AI shallowly *(`79`% of faculty, `88`% minimal-to-moderate)*.
🟢 **Gulf** — `4` of `4` states now have a **curriculum** instrument and only Saudi Arabia
governs **AI used ON learners**, so lead with build-and-train and offer this pattern as the
governance that is not yet required.

### 🔴 Amendment `4` — a sourcing rule for every pattern in this file, forced by the channel

🔴 **`github.com` HTML and `api.github.com` were `403` for this entire session**, so no star
count, commit date or topic membership in this file was refreshed this pass. 🟢 **Licences,
tool definitions and code were all read at primary fidelity over `git` and `raw`.**
🔵 **So when quoting any pattern here: the LICENCE and the CODE are current; the ATTENTION
metrics are stale by construction.** Where a pattern's justification rests on a repository
being actively maintained, say that the maintenance signal was not re-measured.

Evidence: [`openedx-mcp-tool-surface`](../evidence/openedx-mcp-tool-surface.2026-10-14-p190.tsv) ·
[`ralph-equivalence-subset`](../evidence/ralph-equivalence-subset.2026-10-14-p190.tsv) ·
[`proctoring-affect-inference`](../evidence/proctoring-affect-inference.2026-10-14-p190.tsv) ·
[`licence-path-case-published`](../evidence/licence-path-case-published.2026-10-14-p190.tsv) ·
[`channel-inversion-github-blocked`](../evidence/channel-inversion-github-blocked.2026-10-14-p190.tsv)

## Pass 189 — 2026-10-14

🆕 🟢 **One new pattern, and three amendments that REPRICE steps this KB published yesterday
— two of them cheaper, one of them re-justified. Every repository named below had its grant
read this pass over `raw.githubusercontent.com/<slug>/HEAD/<path>` with the HTTP code
checked.**

### 🟢 Amendment `1` — Pattern `32` step `3` repriced. `3c` is already TRUE; `3b`'s reason CHANGES

🔵 p188 added steps `3a`–`3d` and pre-registered `ACTION NA` to settle whether `ralph`'s LRS
**refuses** an overwrite or lets `INDEX` through. 🟢 **Limb `1` fired. It refuses — in code,
on both write paths.**

| path | lines | measured |
|---|---|---|
| 🟢 `PUT` | `624`–`700` | on an existing id the handler queries first, then: not equivalent → `HTTPException(409 CONFLICT, "A different statement already exists with the same ID")`, **returning before `BACKEND_CLIENT.write` is reached**. Equivalent → bare `return`, no write, `204` |
| 🟢 `POST` | `163`–`210`, `728`–`736` | `_filter_existing_statements`, docstring verbatim: *"Drop statements already stored; raise on conflicting duplicates."* Non-equivalent → `409`; equivalent ids are **removed from the write set**; an all-duplicate batch writes nothing and answers `204` |
| 🟢 source comment | `686`–`689` | verbatim: *"The LRS specification calls for deep comparison of duplicate statement ids. In the case that the current statement is not equivalent to one found in the database we return a 409, otherwise the usual 204."* 🔵 The refusal is **deliberate and documented in the code** |
| 🔴 `POST` partial-success | `739`–`790` | opt-in bulk backfill *(issue `#622`)* tolerates **validation** errors per item but **not** an id conflict: `409`, `PartialSuccessError(index=-1)`, `inserted_ids=[]` — the whole batch rejected. 🟢 "Partial success" does not weaken the id guarantee |

🔴 **And limb `2`'s own wording was MIS-SPECIFIED, which is worth recording.** It listed
*"returns `204`"* as evidence of overwriting. `204` is the `xAPI` spec's response for an
**idempotent duplicate** — here it is the evidence of **refusal**, not of a write. A limb
that names a status code has to name what the code means in the protocol.

🟢 **So the steps reprice:**

| step | status after this pass |
|---|---|
| 🟢 `3c` **PIN the operation type** | 🟢 **CHEAPER THAN WRITTEN — at the API layer it is already true.** Keep the CI check for the backend path, but do not budget build time for the API behaviour. 🔵 And it is **demonstrable in one live `409`** rather than argued |
| 🔴 `3b` **WORM target** | 🔴 **STAYS MANDATORY — and its justification CHANGES, which makes it an easier sell.** It is not there to stop the application; the application already refuses. **It is there to stop the OPERATOR** — `BaseOperationType` declares `DELETE`/`UPDATE`, default `INDEX` overwrites, and `--es-op-type` exposes all four on the CLI. 🔵 "Who do you trust with Elasticsearch credentials" is a better question in a DPO meeting than "is your LRS immutable" |
| 🟢 `3a`, `3d` | unchanged. 🟢 `3d`'s rule is vindicated: the `409` was found by **reading the code**, not the docs — p188 established `README`, `docs/index.md` and `docs/features/backends.md` carry **zero** hits for `delet|retention|immutab|append-only|WORM` |

🟡 **Estimate holds at `8`–`10` weeks for steps `1`–`3`, with weeks moving from `3c` to `3b`.**

### 🔴 Amendment `2` — Pattern `33`'s Open edX row, corrected a SECOND time, and the licence is the catch

🔵 p187 priced it at `12`–`14` weeks *("nothing exists")*; p188 corrected that to `8`–`10`
*(no server exists, but an official MCP CLIENT does, and its docs say it "will never expose
MCP server functionality")*. 🟢 **`ACTION NB` limb `1` fired: a server exists.**

| if the client runs Open edX | adopt | licence, measured | what you still build | weeks |
|---|---|---|---|---|
| 🆕 🟡 **agent surface** | 🆕 [`blend-ed/tutor-contrib-openedxmcp`](https://github.com/blend-ed/tutor-contrib-openedxmcp) `v0.2.0` — Tutor plugin; installs the [`openedx-mcp`](https://pypi.org/project/openedx-mcp/) Django app *(REST facade `/api/mcp/`, `/api/mcp/cms/`)* and runs an MCP streamable-http container behind Caddy at `mcp.<LMS_HOST>` | 🔴 **`AGPL-3.0`** *(`34 524` B, `200`)*, corroborated by `pyproject.toml` and the README badge | review, key management, tool allow-listing, deployment | 🟢 **`4`–`6`** *(from `8`–`10`)* |

🟢 **How to wire it, concretely:**

1. `pip install tutor-contrib-openedxmcp` → `tutor plugins enable openedxmcp` →
   `tutor images build openedx openedxmcp` → `tutor local launch` → `tutor local do init`
   *(creates the `MCPKey` tables)*. 🟢 Pin the Django app explicitly:
   `tutor config save --append OPENEDX_EXTRA_PIP_REQUIREMENTS=openedx-mcp==<version>` —
   🔵 **two artefacts ship separately, so pin both or you have an unpinned supply chain.**
2. Mint a key in Django admin *(**Open edX Admin MCP → MCP keys**)*; the client sends it and
   the facade forwards it as `X-MCP-Key`. 🔴 **Authorisation is `is_staff`/`is_superuser`,
   evaluated live at the facade — there is no per-tool scope.** So a key is an admin key.
3. 🔴 **GATE THE TOOL LIST BEFORE ANYTHING ELSE.** The LMS side exposes, verbatim,
   *"people, enroll, analytics, certs, **retire**"*; the CMS side *"course authoring,
   modulestore"*. **`retire` deletes a learner record and `is_staff` is the only thing in
   front of it.** Put the existing [`mcp-allowlist-gateway`](code/mcp-allowlist-gateway/README.md)
   pattern between the client and `mcp.<LMS_HOST>` and allow-list read tools only until the
   client has signed off on the write set.
4. 🔴 **Close `/health`.** The README states it is unauthenticated for probes — acceptable
   inside a cluster, not on a public Caddy route.
5. 🔴 **Price the `AGPL` before the weeks.** Deploying it unmodified is ordinary use.
   **Extending it ships the extension under `AGPL-3.0`** — and because it is a network
   service, the Affero clause reaches users of the hosted instance. 🔵 For a client who
   wants a proprietary agent layer, the `4`–`6` weeks is the wrong number: the right answer
   is a clean-room facade against Open edX's own REST APIs, back at `8`–`10`.
6. 🔴 **Bus factor `1`★, `v0.2.0`.** Fork and vendor it; do not take a dependency on the
   upstream release cadence.

🔵 **Why it was missed for two passes, and the rule it produces:** the repository is not
tagged `open-edx`, `mcp` **or** `mcp-server`, and a quoted `"edx-platform"` + `mcp` search
returns *"Your search did not match any repositories"*. 🟢 **Rule: an absence established
from topic pages is a statement about TAGS. Before publishing "nothing exists", run an
unquoted repository search.**

### 🟢 Amendment `3` — Pattern `34` step `1` gets the path list it was missing

🔵 Pattern `34` *(the split-scope licence audit)* opens by fetching the licence file.
🔴 **Its path list was case-sensitive and missed a real grant** —
[`openedx/XBlock`](https://github.com/openedx/XBlock) carries `LICENSE.TXT` *(`11 358` B,
verbatim Apache-2.0)* and this KB published it as `NO_LICENCE_FILE`.

🟢 **Step `1` is replaced with [`P1057`](code/p1057-licence-path-case/README.md)**
*(`16`/`16` tests)*:

| `1a` | 🟢 fetch over `/HEAD/`, never `main`/`master` — **`HEAD` resolves the default branch**, so the branch guess disappears and the probe cost halves |
|---|---|
| `1b` | 🟢 read the **manifest** first: PEP 639 `license-files` *(`pyproject.toml`)* and npm `licenseFile` **name the path**. 🔴 Authoritative but rare — `1` of `64` rows. 🔴 A licence **string** *(`license = "MIT"`)* is not a licence **path** |
| `1c` | 🟢 then the **case variants** — `LICENSE`, `LICENSE.TXT`, `LICENSE.txt`, `LICENCE`, `COPYING`, … 🟢 Measured yield over `14` grant-absent rows: **`224` probes, `0` further grants**, so expect this step to find nothing and run it anyway |
| `1d` | 🆕 🟢 for an **R** package, read `DESCRIPTION`: *"License: MIT + file LICENSE"* means the `~47`-byte `LICENSE` is **complete**, not a stub |

🆕 🔵 **And a trap for step `4`:** a `CC` identifier beside a **named third party** is an
attribution, not a scope split. [`Bbar0n234/learnflow-ai`](https://github.com/Bbar0n234/learnflow-ai)
reads *"This product includes IP geolocation data by IPinfo, licensed under CC BY-SA 4.0"* —
a dependency notice shaped exactly like a content-half grant.

### 🆕 🟢 Pattern `35` — the agent-reachable destructive-tool audit, before the agent ships

🔵 **Why it exists.** This pass found an MCP server whose tool list includes `retire` on the
same day it proved the LRS beneath it refuses overwrites. 🔴 **The agent layer is being
built faster than the guarantees underneath it**, and three jurisdictions now require a
durable record of a human decision about a learner. 🟢 This pattern is the two-week piece of
work that finds the gap before a client's agent does.

| step | component | licence, as measured | what it does |
|---|---|---|---|
| `1` | 🟢 **ENUMERATE the tool surface from the server's own definitions**, not its README. Use the existing [`p139-tool-count-drift`](code/p139-tool-count-drift/README.md) check | — | 🔴 a README's tool list is marketing. The count drifts |
| `2` | 🟢 **CLASSIFY each tool by what it DESTROYS**: nothing / mutable state / a durable record about a person. 🔴 On `tutor-contrib-openedxmcp` that is `retire`, `enroll` and `certs` on the LMS side and `modulestore` on the CMS side | — | the output is a one-page list a DPO can read |
| `3` | 🔴 **TEST each destructive tool against the store beneath it, with a LIVE call.** Does anything refuse? 🟢 On [`openfun/ralph`](https://github.com/openfun/ralph) the answer is a documented `409` on both write paths. 🔴 On the Open edX facade, nothing — `is_staff` is the whole control | 🟢 `ralph` `MIT` *(`1 094` B)* | 🔵 never a config review. The `409` and the successful delete are both artefacts you keep |
| `4` | 🟢 **GATE the write set** with [`mcp-allowlist-gateway`](code/mcp-allowlist-gateway/README.md) in front of the server; read-only until the client signs the write list | — | 🟢 reversible, and it ships in days |
| `5` | 🔴 **DUAL-WRITE the durable records to an object-lock bucket** *(Pattern `32` step `3b`)* | — | 🔴 the only step that survives a credentialed operator **or** a mis-scoped agent key |
| `6` | 🟢 **CLOSE the probe endpoints.** `tutor-contrib-openedxmcp` serves `/health` unauthenticated | — | cluster-internal is fine; a public Caddy route is not |
| `7` | 🟢 **ANCHOR the credential.** Where the artefact must outlive the platform, issue it as **`OB 3.0` / W3C Verifiable Credentials**: [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget), [`oneorigin-2-0/dcc-credential-co-writer-monorep`](https://github.com/oneorigin-2-0/dcc-credential-co-writer-monorep), [`iblai/wallet`](https://github.com/iblai/wallet), [`MrPrinceAli/proven`](https://github.com/MrPrinceAli/proven), [`brody-0125/signet-campus`](https://github.com/brody-0125/signet-campus) | 🟢 all **`MIT`** | 🔵 durable by **cryptography** rather than by an application-layer refusal. 🔴 Avoid the old side — `obadgen` `AGPL-3.0`, `openbadgeslib` `LGPL` |

🟡 **Estimate: `2`–`3` weeks for steps `1`–`4`** *(the audit and the gate)*, **`+4`–`6` for
`5`–`7`** *(the durable-record work)*. 🟢 **Steps `1`–`4` are the ones to quote first: they
are cheap, reversible, and they produce the document that justifies `5`–`7`.**

🔵 **Where it applies by region.** 🔴 **EU** — Art. `5(1)(f)` is live since `2025-02-02`,
so step `2` must also flag any tool inferring **emotion** from biometric data *(penalty
ceiling EUR `35`M or `7`% of turnover)*; proctoring tools are an explicit grey area.
🔴 **Vietnam** — automatic grading or ranking is high-risk by statute. 🔴 **Oklahoma** — AI
may not be the main basis for high-stakes decisions about students. 🔴 **South Korea** —
education is a "high-impact AI" sector requiring human monitoring and intervention.
🟢 **LATAM** — no national rule found, so sell steps `1`–`4` as **risk management**, against
the Digital Education Council finding that faculty's lowest adoption is in **assessment**.

Evidence: [`ralph-append-only`](../evidence/ralph-append-only.2026-10-14-p189.tsv) ·
[`openedx-mcp-server`](../evidence/openedx-mcp-server.2026-10-14-p189.tsv) ·
[`licence-path-case`](../evidence/licence-path-case.2026-10-14-p189.tsv)

## Pass 188 — 2026-10-14

🆕 🟢 **One new pattern and three amendments, two of which REPAIR a step this KB published
as sound. Every repository named below had its grant read over the raw channel this pass
with the HTTP code checked.**

### 🔴 Amendment `1` — Pattern `32` step `3` was NOT sound. It needs a WORM store

🔵 p187 published Pattern `32` with step `3` as *"PERSIST it as `xAPI` — an LRS **outside**
the LMS, so deleting a course in the LMS cannot reach the record"*, and pre-registered
`ACTION MX` to check `ralph`'s retention surface before treating that as complete. 🟢 **It
was right to wait. Limb `2` fired.**

| what was checked at `HEAD 91fef112` | measured |
|---|---|
| 🟢 LRS HTTP API | 🟢 route decorators are **`get`, `put`, `post` and nothing else** — there is **no `@router.delete`.** A statement cannot be deleted over the LRS API |
| 🔴 `xAPI` voiding | 🔴 `voidedStatementId` is accepted; its own description reads **"*Not implemented* Id of voided Statement to fetch"** |
| 🔴 storage layer | 🔴 `BaseOperationType` declares **`DELETE`** *("deletes an existing record")* and **`UPDATE`** *("updates or overwrites an existing record")*; `--es-op-type` exposes them as a **first-class CLI option** |
| 🔴 default write mode | 🔴 `default_operation_type = INDEX`, which *"creates a new record with a specific ID"* — a re-write carrying an existing statement id **OVERWRITES** |
| 🔴 append-only / WORM / retention mode | 🔴 **zero occurrences across `6` files read.** The one `"Immutability"` string is the `xAPI` `format=canonical` docstring, about Activity/Verb REPRESENTATION — not a storage guarantee |
| course-scoped deletion | 🔵 does not exist either way; deletion is per-record, by id, at the backend |

🔴 **So step `3` as written bought LESS than it claimed.** Putting the record outside the
LMS does stop the LMS from reaching it — 🟢 that half is true and worth having — 🔴 **but it
does not make the record durable. Its protection is the absence of an HTTP route, and
anyone with Elasticsearch or MongoDB credentials bypasses it using ralph's own CLI.**

🟢 **Step `3` is REPLACED:**

| step | component | licence, as measured | what it contributes |
|---|---|---|---|
| `3a` | 🟢 **KEEP `ralph` as the LRS** — [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **`MIT`** *(`LICENSE.md`, `1 094` B)* | 🟢 still the right choice: `xAPI` in a standard format, run at national scale by France Université Numérique, and **append-only to the agent**, which is the actor you are defending against most of the time |
| 🆕 `3b` | 🔴 **ADD A WORM TARGET BESIDE IT.** Dual-write every oversight statement to object storage with an **object-lock / retention-pinned** bucket | — *(infrastructure, not a repo)* | 🔴 **this is the step that makes the record survive a credentialed insider.** The LRS stays queryable; the lock-bucket copy is the evidence |
| 🆕 `3c` | 🟢 **PIN the operation type.** Set the backend operation type explicitly and **refuse `DELETE`/`UPDATE`/`INDEX`-over-existing** in the deployment's own configuration and CI check | — | 🟢 cheap, and it closes the default: `INDEX` overwrites by design, so leaving the default in place is a decision, not an accident |
| 🆕 `3d` | 🟢 **VERIFY WITH A LIVE DELETE, never a config review** | — | 🔵 the same rule p187 set for `dotty-tutor`'s `ondelete` clauses. Attempt the delete through both the API and the backend, and keep the output |

🟡 **Estimate grows: steps `1`–`3` move from `6`–`8` weeks to `8`–`10`.** 🔴 **Step `2`
remains the whole value and step `3b` is now second — if a client declines both, the rest
of the pattern is decoration.**

🟢 **And the sales argument got stronger, not weaker.** Two unrelated, well-built projects
now show the same defect class *(see [`intel/trends.md`](../intel/trends.md) Trend `1`)*.
🔵 **That means a studio can walk into a meeting, run one live delete against whatever the
client already has, and show the audit trail disappear.** It is a demonstration, not a
claim.

### 🔴 Amendment `2` — Pattern `33`'s Open edX row is wrong in BOTH directions

🔵 p187's row read 🔴 *"Open edX — **nothing exists** — the whole adapter. Price it as a
build"*, at `12`–`14` weeks. 🟢 **`ACTION MV` read `topics/open-edx` at both sort orders and
the Open edX org itself. The absence of a SERVER holds; "nothing exists" does not.**

| if the client runs… | adopt | licence | what you still have to build |
|---|---|---|---|
| 🔴 🟢 **Open edX** | 🟢 **[`openedx/openedx-ai-extensions`](https://github.com/openedx/openedx-ai-extensions) — the OFFICIAL `MCP` CLIENT and workflow framework.** 🟢 **Do NOT rebuild this half** | 🔴 **`AGPL-3.0`** *(`34 523` B)*, and 🔴 **"experimental" / "proof-of-concept" by its own `README.rst`** | 🔴 **the SERVER half, permanently.** Its docs state *"does not run or host MCP servers"* and **_"will never expose MCP server functionality"_**. Build a `FastMCP` server over Open edX's existing REST APIs; the docs' own `mcp_example_server` is a `roll_dice` demo behind `ngrok`, marked not for production, and is useful only as a transport template |

🟡 **Revised estimate: `8`–`10` weeks, not `12`–`14`.** 🔵 The orchestration, tool-wiring
and model-plumbing half is official and exists; what remains is one `FastMCP` server plus
the governance wrapper. 🔴 **But two risks go in the SOW, not the appendix: the official
client is `AGPL-3.0`** *(so a hosted derivative triggers network-copyleft — the exact
question a client building a commercial tutoring service must answer before step `1`)*,
🔴 **and it is experimental by its author's own description. A proof-of-concept is not a
platform, and its interfaces will move.**

🟢 **And delete the licence explanation from the pattern.** p187 attributed the Open edX
gap to `AGPL`. 🔴 **This KB's own Moodle rows refute it — `GPL-3.0` is strong copyleft and
carries three independent `MCP` servers.** 🔵 The cause is Open edX's plugin architecture
and a stated policy, which is a far more durable fact: a licence can be dual-licensed; a
documented design decision cannot be waited out. 🟢 **Say that in the meeting; it is the
difference between "wait for upstream" and "this is yours to own".**

### 🆕 🟢 Pattern `34` — the split-scope licence audit, before the course ships

🔵 **Why this is a pattern and not a checklist item:** `ACTION MW` ran `P1054` over all
`46` rows these pages publish as `MIT` and found **two** whose content half is **`CC BY
4.0`**, not `MIT`. 🟢 **Education repositories are code PLUS content by construction** — a
course is notebooks, a tutor is an item bank, a de-identifier is a term list — 🔴 **so the
half a studio actually delivers to a client is routinely the half under a different
licence.**

| step | what | component / instrument | why |
|---|---|---|---|
| `1` | 🟢 **Classify every licence file, don't pattern-match it** | 🟢 [`compose/code/p1054-mit-plus-clause`](p1054-mit-plus-clause/README.md) *(`14` tests)* + 🆕 [`compose/code/p1056-split-scope-licence`](p1056-split-scope-licence/README.md) *(`16` tests)* | 🔴 `P1054` catches a NARROWED grant *(`graspful`'s anti-SaaS clause under MIT's body)*; 🆕 `P1056` catches a SPLIT one. **Both pass a body-matching classifier as `MIT`** |
| `2` | 🟢 **Probe three channels, not one** | the licence file · a **second** licence file *(`LICENSE-DATA`, `LICENSE-CC`)* · **the README's `## License` section** | 🔴 `spedlex` declares its split in the README and ships the CC text in `LICENSE-DATA`. A root-anchored `LICENSE`-only probe reads it as clean `MIT` — which is what this KB did |
| `3` | 🔴 **Ask which half you are selling** | — | 🔴 **This is the step that costs money if skipped.** For [`ktwyw/python-for-engineers`](https://github.com/ktwyw/python-for-engineers) the notebooks ARE the product; for [`siskinskai/spedlex`](https://github.com/siskinskai/spedlex) the `data/`, `schema/` and term lists ARE the repo. In both, the deliverable is the `CC BY` half |
| `4` | 🟢 **Carry the attribution into the deliverable** | — | 🟢 `CC BY` is a cheap obligation and a perfectly good one — 🔴 **but it is irrevocable and it travels.** A white-labelled client course built on `CC BY` notebooks breaches on delivery |
| `5` | 🔴 **Read every sub-`1`kB licence file by hand** | — | 🔴 Four distinct shapes now sit on this shelf and only ONE is a grant: the `CRAN` stub *(grant in the manifest, `47` B)*, the TITLE-ONLY stub *(no permission clause, `46` B)*, ALL-RIGHTS-RESERVED borrowing MIT's warranty disclaimer *(`842` B)*, and 🆕 **source-available non-commercial** *(`No-Suggest/NoSuggest`, `417` B)*. 🔴 **`P1054` returns `NOT-MIT-BODY` for the last one and says nothing — a `NOT-MIT-BODY` verdict is not a clean bill** |
| `6` | 🟡 **Treat a README licence claim as a cue to re-probe, never as a grant** | — | 🔵 the rule p186 settled for BADGES, now with two more instances: `moodle-quizsmith` and `moodle-5-1-authentic-relay` both claim `MIT` in prose with no grant at `15` licence paths or `22` header paths. 🔴 **And both are Moodle-plugin-shaped, where Moodle's rules require `GPL`** |

🟡 **Estimate: `3`–`5` days as a fixed-price package per `20`–`30` candidate repositories**,
run BEFORE the architecture is chosen. 🟢 **Sell it as risk reduction with a named
precedent:** `graspful` is agent-first course authoring that *"looks like the best find of
the pass"* and breaches on delivery for any hosted client service, and `spedlex` is an
asset this KB itself published under the wrong licence for three passes.

### 🟢 Amendment `3` — Pattern `32` step `5` gets a licence correction, and it is ours

🔴 **Step `5` names [`siskinskai/spedlex`](https://github.com/siskinskai/spedlex) as
`MIT` *(`1 076` B)*. The code is `MIT`. The VOCABULARY — `data/`, `schema/` and the term
lists in `sources/` — is `CC BY 4.0`, shipped as `LICENSE-DATA` at `17 023` B.** 🟢 The
component stays in the pattern, unchanged and still recommended; the licence column now
reads **`MIT` (code) + `CC BY 4.0` (data)**, and step `4` of Pattern `34` applies to it.

🔵 **This is the single most load-bearing instance of the new shape on this shelf**, because
`spedlex` is used INSIDE a client's student-data de-identification pipeline. 🟢 Attribution
has to appear in the client's own deliverable, and that is a sentence in a SOW, not a
surprise in a review.

### 🟢 Routing additions to existing patterns, grants verified this pass

| pattern | addition | licence |
|---|---|---|
| Pattern `33` | 🟢 **[`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi)** for the LTI layer — written by the author of the LTI specification | 🟢 `Apache-2.0` *(`10 273` B)* |
| Pattern `33` | 🟢 **[`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)** where the client is on Django | 🟢 `MIT` *(`1 098` B)* |
| Pattern `33` | 🟢 **[`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT)** as the permissive LMS target when the client has no incumbent — 🔴 but it has **no `MCP` surface**, so it is a Pattern `33` BUILD, not an adopt | 🟢 `Apache-2.0` *(`10 982` B)* |
| Pattern `32` | 🟢 **[`numbas/Numbas`](https://github.com/numbas/Numbas)** for assessment authoring and marking where the oversight record needs an item bank under it | 🟢 `Apache-2.0` *(`11 357` B)* |
| 🟢 **a LATAM engagement** | 🟢 **[`academico-sis/academico`](https://github.com/academico-sis/academico)** — a permissive SIS, `404`★, **built in-region**. 🔵 For twelve passes this KB said no permissive SIS existed | 🟢 `MIT` *(`1 094` B)* |
| 🟢 **the credential layer** *(new)* | 🟢 **[`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget)** + **[`oneorigin-2-0/dcc-credential-co-writer-monorep`](https://github.com/oneorigin-2-0/dcc-credential-co-writer-monorep)** + **[`iblai/wallet`](https://github.com/iblai/wallet)** | 🟢 `MIT` *(`1 080` / `1 087` / `1 063` B)* |

🔵 **Why the credential layer belongs in Pattern `32` and not in a pattern of its own yet:**
it is the only artefact in this stack that is durable by **cryptography** rather than by
convention, and Pattern `32` is entirely about durability. 🟡 Promoted to its own pattern
once one of those rows is measured in production rather than read.

## Pass 187 — 2026-10-14

🆕 🟢 **Two new patterns and three amendments. Every repository named below had its grant read over
the raw channel this pass with the HTTP code checked, and one amendment is a REPAIR to a step p186
published as blocked.**

### 🆕 🔴 Pattern `32` — the human-oversight record that survives the course being deleted

🔵 **The regulatory driver is now in three regions at once:** Oklahoma and Maryland moving to
require human review and bar AI from high-stakes student decisions; the EU `AI Act` naming
education access and assessment high-risk; 🔴 **and Vietnam naming educational assessment a
statutory high-risk sector.** 🟢 **All three require proof that a human reviewed the machine. This
pattern is about not losing it.**

🔴 **The failure this pattern exists to prevent, measured this pass.**
[`dotty-tutor`](https://github.com/ningkaikok/dotty-tutor)'s `apps/api/persistence/schema.py`
*(`19 405` B, `Apache-2.0`)* holds `teacher_review_events`, whose `corrected_assessment` column
records a teacher overturning an AI grade. 🔴 **It carries `ondelete="CASCADE"` on TWO parents —
`class_id → learning_classes` and `assignment_id → assignments`.** 🔵 **Delete a finished class, or
one assignment, and the evidence that a human corrected the model is silently gone.** 🟢 This is not
a defect peculiar to one project: **course-shaped schemas treat the class as the aggregate root and
cascade everything below it, which is correct for pedagogy and wrong for audit.**

| step | component | licence, as measured | what it contributes |
|---|---|---|---|
| `1` | 🟢 **ADOPT the vocabulary** — [`dotty-tutor`](https://github.com/ningkaikok/dotty-tutor)'s `teacher_review_events` | 🟢 `Apache-2.0` *(sidebar + full text)* | 🟢 **`action` is `CHECK`-constrained to `('reviewed','overturned','mastery_override')`** — "a human looked", "a human overruled the model", "a human set mastery directly". 🟢 **Take these three values as they stand**; they are very close to what a regulator means by meaningful oversight. Columns worth keeping: `learner_id`, `question_id`, `knowledge_point_id`, `mastery_score` *(`0`–`1`, `CHECK`ed)*, `corrected_assessment`, `note`, `created_at` |
| `2` | 🔴 **REJECT the parentage.** Re-point the oversight log OUT of the course aggregate | — | 🔴 **Drop both `CASCADE`s.** The record's lifetime is the institution's retention obligation, not the class's. 🟢 Follow the same schema's own better instinct: `knowledge_point_id` has **no** `ondelete` |
| `3` | 🟢 **PERSIST it as `xAPI`** — [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **`MIT`** *(`LICENSE.md`, `1 094` B)* | 🟢 An LRS **outside** the LMS, so deleting a course in the LMS cannot reach the record. `51`★, run at national scale by France Université Numérique. 🔵 `xAPI` is also what a procurement officer already knows how to ask for |
| `4` | 🟢 **GATE the model** — [`Principled-Evolution/gopal`](https://github.com/Principled-Evolution/gopal) | 🟢 **`Apache-2.0`** *(`11 357` B)* | `Rego` policies incl. `FERPA`; drops into an `OPA` gate a client may already run. 🟢 Add [`Polycentric-Labs/regrails`](https://github.com/Polycentric-Labs/regrails) *(`Apache-2.0`)* where **Title IV** is in scope |
| `5` | 🟢 **DE-IDENTIFY before retrieval** — [`siskinskai/spedlex`](https://github.com/siskinskai/spedlex) + [`ashutoshrana/haystack-ferpa-filter`](https://github.com/ashutoshrana/haystack-ferpa-filter) | 🟢 **`MIT`** *(`1 076` B)* / 🟢 **`Apache-2.0`** *(`12 101` B)* | special-education PII/PHI vocabulary, and a `FERPA` pre-filter for Haystack pipelines |
| `6` | 🟢 **SCOPE BY ROLE, not by filter** — [`ZachRouan/district-brain`](https://github.com/ZachRouan/district-brain) | 🟢 **`MIT`** *(`1 066` B)* | role-scoped district RAG, locally hosted. 🔵 Scoping at retrieval survives a review; filtering after it does not |

🟢 **Why a client buys this:** it is the one deliverable that answers *"show me a human reviewed
it"* in a form that outlives the course, the term and the LMS migration.
🟡 **Estimate: `6`–`8` weeks** for steps `1`–`3` against one LMS, `+3`–`4` weeks for `4`–`6`.
🔴 **Step `2` is the whole value and it is one schema decision — if a client declines it, the rest
of the pattern is decoration.**

### 🆕 🟢 Pattern `33` — the LMS as an agent tool surface, without writing an adapter

🔵 **p186's Pattern `31` used `sisu-mcp` and read it as a SIS story. `ACTION MR` shows it was the
first row of a populated layer — so this is the general form, per platform.**

| if the client runs… | adopt | licence | what you still have to build |
|---|---|---|---|
| 🟢 **Moodle** | [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) *(courses, assignments, grades)* **or** [`onbirdev/moodle-webservice_mcp`](https://github.com/onbirdev/moodle-webservice_mcp) *(in-tree, as a web-service plugin)* | 🟢 `MIT` *(`1 063` B)* / 🟢 `GPL-3.0-or-later` 🔴 **in the PHP file headers only** | 🟢 **nothing on the read path.** Add [`valentineus/moodle-webhooks`](https://github.com/valentineus/moodle-webhooks) *(`GPL`)* for push, since `MCP` is all pull |
| 🟢 **Canvas** | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) + 🟢 [`chaz-clark/canvas-toolbox`](https://github.com/chaz-clark/canvas-toolbox) for the `FERPA`-safe wrapper | 🟢 `MIT` *(`1 072` B)* | the approval gate — 🔵 match **IgniteAI**'s shape, which is what Canvas clients will expect: permission-scoped, approval at key moments |
| 🟢 **Brightspace / D2L** | [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) *(`57`★)* | *(recorded earlier)* | tenancy and audit |
| 🟢 **A university SIS** | [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) | 🟢 `MIT` *(`package.json` only, `999` B)* | 🟢 nothing — **read-only is the server's design, not a promise in a SOW** |
| 🟢 **`SCORM` content** | [`kemalyy/edumints-scorm-mcp`](https://github.com/kemalyy/edumints-scorm-mcp) + [`-skill`](https://github.com/kemalyy/edumints-scorm-skill) | 🟢 `MIT` *(`1 069` B)* | 🟢 authoring is covered; add [`scormflow/scorm-engine`](https://github.com/scormflow/scorm-engine) *(`MIT`, `1 079` B)* to **run** `SCORM`/`xAPI`/`cmi5` with an LRS |
| 🔴 **Open edX** | 🔴 **nothing exists** | — | 🔴 **the whole adapter. Price it as a build** *(`Gap 427`)* |
| 🔴 **Chamilo / OpenOLAT / Sakai** | 🔴 **nothing found** | — | 🔴 as above |

🟢 **Then make it measurable** — [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta)
*(`Apache-2.0`, `11 323` B, `21`★, default branch `development`)* runs **randomised experiments on
live assignments inside the LMS**. 🔵 **It is the only component on this shelf that lets a client
find out whether the agent helped, rather than assert it** — and in a market where `9`% of LATAM
institutions evaluate what they deployed, that is the differentiator, not the tutor.

🟡 **Estimate: `4`–`6` weeks** to a governed pilot on Moodle, Canvas, Brightspace or Sisu;
🔴 **`12`–`14` weeks** on Open edX, and the difference is entirely `Gap 427`.

### 🟢 Amendment `1` — Pattern `29` takes step `2b`. `ACTION MQ` settled `Gap 424`

🔴 **`readerbench-java` ships NO Portuguese pipeline.** `core-services/pom.xml` declares its
language modules explicitly — `language-de`, `-en`, `-es`, `-fr`, `-it`, `-nl`, `-ro` — and
🔴 **there is no `language-pt`.** 🟢 **The probe discriminates: it can see seven languages, and
Portuguese is absent from all three resource families** *(language model, `wordlists-*`,
`wordnet-*`)*.

🔴 **Worse for LATAM than the limb anticipated: Spanish is PARTIAL too.** `language-es` exists but
there is **no `wordnet-es` and no `wordlists-es`** — and the lexical resources are what the textual
complexity features consume. 🟢 **So Pattern `29` takes step `2b`: the blocker is FEATURE
EXTRACTION, not translation, and the `pt-BR` estimate doubles.** 🔵 **An `es` writing-assessment
engagement must now carry the same warning** — previously this KB would have treated Spanish as
served. 🔴 **`Gap 372` does NOT close**: there is still no permissive production-grade essay-scoring
library, and the activity the `AI Act` names high-risk most explicitly remains the one with the
least open supply.

### 🟢 Amendment `2` — Pattern `24`'s human-review tables: the block was a wrong PATH, and the count was wrong

🟢 **`ACTION MP` limb `1` FIRES, so `Gap 422` is NOT structural.** p186 probed
`routers/review_routes.py`; the repository is a **monorepo** and the file is at
`apps/api/routers/review_routes.py`. 🟢 Both named routers resolve, and their imports are flat
module names on `apps/api`'s path *(`answer_evaluator`, `application.services.learning_funnel`,
`domain.learning.mastery_policy`, `auth_context`, `observability`)*.

🔴 **And the measurement corrects p186's premise rather than confirming it: there is NO
`quality_review_*` cluster — `0` occurrences in the schema — and the human-review surface is not
`12` tables. It is ONE table, `teacher_review_events`, with `11` columns and `2` `CHECK`
constraints.** 🟢 Pattern `24`'s *"`12` human-review tables, UNVERIFIED"* row is therefore
**retired and replaced** by Pattern `32` step `1`. 🔵 **Two of this pass's limbs fired by correcting
a cheap wrong guess about a path or a population — the same lesson p186 wrote, now with a second
and third instance.**

### 🟢 Amendment `3` — Pattern `27` keeps its ASK step, unused, for a third pass

🔴 **`ACTION MN` is NOT RUN for the third consecutive pass**, and the reason is unchanged: opening
licensing issues on third parties' repositories is an outward-facing write, and this run is
unattended with no live authorisation. 🟢 **Recorded as a decision for a human, not quietly
dropped.** 🔵 The queue it would work, in order, is now longer and better evidenced:
[`Nasus20202/MoodleMCP`](https://github.com/Nasus20202/MoodleMCP) *(no grant, a clean `MCP`
implementation)*, [`mohamurshid/ElimuAnalytics`](https://github.com/mohamurshid/ElimuAnalytics)
*(no grant, `IRT` for Kenya's `CBC` — a rare regional asset)*,
[`alfredang/AI-LMS-TMS`](https://github.com/alfredang/AI-LMS-TMS) *(no grant, `19`★)*, then
p186's `MoKangMedical/digital-sage`, `dotty-tutor` *(complete `Apache-2.0`, no named licensor)*
and `xueyoujing-companion`.

## Pass 186 — 2026-10-14

🆕 🟢 **Two new patterns and three amendments. Every repository named below had its licence read over
the raw channel during this pass, and two of the amendments are REPAIRS to steps p185 published as
complete.**

### 🆕 🟢 Pattern `31` — the read-only student record as agent tools, with the override that survives

🔵 **The seam [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) opened: a real
university SIS exposed as `MCP` tools, read-only by design rather than by configuration.** 🟢 **This
is the first pattern on this shelf where the agent reads the student record WITHOUT a bespoke
adapter, and where *"it cannot write"* is a property of the server.**

| step | component | licence | the seam, as measured |
|---|---|---|---|
| `1` | [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) | 🟢 **`MIT`** *(`package.json`, `999` B — 🔴 no licence file)* | `sisu_connect` / `sisu_status` / `sisu_disconnect` for the session; `sisu_studies`, `sisu_attainments` for study status and grades; enrolments, timetable, plan, catalogue. 🟢 **READ-ONLY, stated** |
| `2` | [`Simon-Initiative/lti-example-tool`](https://github.com/Simon-Initiative/lti-example-tool) | 🟢 **`MIT`** *(`package.json`, `1 005` B)* | 🟢 the `LTI` handshake, so the agent launches FROM the LMS with the institution's identity rather than beside it. Gleam, `docker compose up` |
| `3` | audit of every agent turn | 🟢 **`Apache-2.0`** | 🟢 **adopt `dotty-tutor`'s `prompt_*` cluster AS IT STANDS** — `prompt_revisions` *(`9` cols)*, `prompt_heads` *(`2`)*, `prompt_release_events` *(`7`)*. `ACTION MJ` verified the FKs carry **no `ondelete`**, so a released prompt cannot be deleted out from under its release event |
| `4` | the human override | 🔴 **fix before adopting** | 🔴 **do NOT copy `teacher_review_events` as written.** `class_id` and `assignment_id` are `ondelete="CASCADE"`, so deleting a class deletes `corrected_assessment` — the teacher's override of the machine. 🟢 **Change both to `RESTRICT` and assert it with a LIVE delete** |
| `5` | mastery state | 🟢 **`MIT` / `Apache-2.0`** | 🔵 the knowledge-tracing cluster p185 told this KB to stop screening: [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) *(`446`★, `MIT`)*, [`bigdata-ustc/EduData`](https://github.com/bigdata-ustc/EduData) *(`312`★, `Apache-2.0`)* |

🔴 **Price these three honestly.** `sisu-mcp` targets ONE SIS product *(Sisu, by Funidata, run by the
Finnish universities)* at `0`★ and `v0.1.0` — **outside the Nordics it is a design to copy, not a
dependency**; the same `7`-tool surface over Banner, SITS or an Ed-Fi ODS is the actual build.
`lti-example-tool` is `"version": "0.0.1"` and *"example"* by name — **a handshake reference, not a
product.** 🟢 **And both grants live only in `package.json`, so the licence note in a client's SBOM
has to say where it was read.**

🔵 **Where it applies:** any engagement where an agent must answer *"how is this student doing?"*
against the institution's own record. 🟢 **Its selling property is negative capability:** the agent
demonstrably cannot change a grade, and that is checkable in the server, not asserted in a document.

### 🆕 🟢 Pattern `32` — the licence due-diligence pass, as a priced work package

🔵 **This pass recovered `4` permissive rows from repositories this KB had written off and moved `2`
to DO-NOT-USE on text a byte count cannot distinguish. The sequence is repeatable and it is the
cheapest value a studio can hand a client in week one.** 🟢 **Run it in this ORDER — each step exists
because the one before it returned a wrong answer on a row this KB measured.**

| step | probe | the row that forced it |
|---|---|---|
| `1` | **licence FILE, all three casings and `14` paths** — `LICENSE`, `License`, `license`, `LICENCE`, `COPYING`, `LICENSE.txt`, `docs/LICENSE`, … | 🔴 [`open-spaced-repetition/fsrs4anki-helper`](https://github.com/open-spaced-repetition/fsrs4anki-helper) is `MIT` in a file named **`License`**. The channel is case-sensitive |
| `2` | **READ the file; check BYTES against the licence it names** | 🔴 `MoKangMedical/digital-sage` serves `46` B: a title, a holder, **no permission clause**. 🔴 `ShuyunYuan/talentcoach` serves `842` B of *"all rights reserved"* that COPIES `MIT`'s warranty disclaimer |
| `3` | **the ECOSYSTEM MANIFEST** — `package.json`, `DESCRIPTION`, `pyproject.toml`, `pom.xml`, `Cargo.toml`, `composer.json`, … | 🔴 [`Simon-Initiative/lti-example-tool`](https://github.com/Simon-Initiative/lti-example-tool) and [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) have **no licence file at all**; the grant is one npm field. 🔵 `shmercer/writeAlizer` serves a `47` B `CRAN` stub with the grant in `DESCRIPTION` |
| `4` | **bare-token scan of README headings** *(`P1049` limb `1`)* | 🔴 `tianshuo/trainingllm`'s entire grant is the word `MIT` under `## License` |
| `5` | **whole-README identifier scan** *(`P1049` limb `2`)*, then read every hit | 🔴 `xiaolai/the-craft-of-selfteaching` grants in a Chinese sentence with no heading. 🟡 `ACTION MK` measured the `NOISE` filter's total cost at **`1` row**, already recovered — so keep the filter |
| `6` | **treat a licence BADGE as a cue to re-run step `1`, never as a verdict** | 🔴 p185 closed `Zenglian990/AI_Tutor_Release` as *"badge-only"*. The repo serves `LICENSE`, `1 068` B, full `MIT` text. **The badge was true** |

🟢 **Instruments, with tests, runnable offline:**
[`compose/code/p1052-stale-absence`](code/p1052-stale-absence/README.md) *(steps `1`–`3`, `13`
checks)* and [`compose/code/p1049-bare-token-grant`](code/p1049-bare-token-grant/README.md) *(steps
`4`–`5`, plus `noise_cost.py` for step `5`'s calibration)*.

🔴 **Two honest limits to quote with the work package.** A grant-text matcher flags proprietary
licences that borrow `MIT`'s disclaimer, so **step `2` is a human read and cannot be automated
away**. And the manifest limb reads `11` formats but **not** `Moodle` / `WordPress` plugin file
headers, where a `GPL` grant conventionally lives — 🔵 **so for a plugin-shaped repository the
absence is not yet established** *(`ACTION MO`)*.

### 🟢 Pattern `28`, amendment — the lecture-capture pattern has a CLASS NAME, and a language limit

🔵 **`ACTION MM` found the seam Pattern `28` step `3` described only as *"a workflow operation"*.**

🟢 **Step `3` is now specific: implement
`org.opencastproject.transcription.api.TranscriptionService`** — a public `api` module,
`ECL-2.0`, `7` methods: `startTranscription` *(two overloads)*, `getGeneratedTranscription`,
`transcriptionDone`, `transcriptionError`, `getLanguage`, `getReturnValues`. 🟢 **Asynchronous with
callbacks, which is the shape an agent wants.** 🔵 **`getReturnValues` is the channel for anything
beyond the transcript — confidence, diarisation, the agent's own metadata.**

🆕 🔴 **And the amendment that changes a quote: `getLanguage()` returns a single `String`.** 🔴 **One
registered provider instance declares ONE language.** 🟢 **So the pattern gains a step: register one
provider instance per language and route on the series' language in the workflow.** 🔵 **For LATAM
*(`pt-BR` + `es`)* and much of EMEA, multiply configuration and testing by the language count — and
`opencast` still ships **`0`** `pt-BR`/`pt-PT` catalogues of `17`, so Brazil carries a translation
project on top.

### 🔴 Pattern `29`, amendment — the `pt-BR` path is TRAINING, and the blocker moved again

🔵 **`ACTION ML` settled it, and limb `2` fired on two independent grounds.**

🔴 **`essay-br` *(`MIT`)* labels `5` ANALYTIC ENEM competences `c1`…`c5` at `0`–`200` in steps of
`40`, summing to `0`–`1000`.** 🔴 **`writeAlizer` *(`MIT`, `v1.7.4`)* predicts ONE holistic *"overall
writing quality"* score — `rb_mod3all` returns three GENRE predictions *(narrative / expository /
persuasive)* and their mean.** 🔵 **Genre is not rubric. There is no mapping to measure; there is an
absence of one.** 🔴 **And `DESCRIPTION` says `Language: en-US`, over `1 316` English ReaderBench
features.**

🟢 **Pattern `29` is therefore re-priced as a TRAINING project, in this order:**

| step | what | licence |
|---|---|---|
| `1` | 🔴 **FIRST, settle `Gap 424`** — does [`readerbench/readerbench-java`](https://github.com/readerbench/readerbench-java) have a PORTUGUESE pipeline? Its README names no languages; `3` probed resource paths `404` | 🟢 `Apache-2.0` *(`10 758` B)* |
| `2a` | 🟢 **if yes** — extract `RB.*` features over `essay-br`, then train `5` ordinal models *(one per competence)* against the human labels. 🔵 `writeAlizer`'s importer and model-registry shape are the template, not its weights | 🟢 `MIT` + `Apache-2.0` |
| `2b` | 🔴 **if no** — the blocker was never the model and never the licence: it is FEATURE EXTRACTION, and the recipe becomes a `pt` feature pipeline before any scoring work | — |
| `3` | 🟢 report per-competence, never a single number. 🔵 ENEM is analytic; a holistic score is not a defensible output for a Brazilian assessment | — |
| `4` | 🔴 carry Matta, Mercer & Keller-Margulis (`2023`) on BIAS in automated writing scores into the proposal. 🟢 **A `pt-BR` model trained on one corpus needs a fairness section before it needs a demo** | — |

🔴 **State the honest headline to a client in one sentence: there is no open-source `pt-BR` essay
scorer today, and whoever builds it owns the reference.** 🟢 **`ACTION MQ` is a one-probe question
that decides whether the first week is training or feature engineering.**

### 🟡 Pattern `24`, amendment — adopt HALF of `dotty-tutor`'s audit layer, and fix the other half first

🔵 **p185 amended Pattern `24` to *"stop building and start adapting"* and pre-registered `ACTION MJ`
to check column by column before the amendment counted as complete. 🟢 It was right to wait: the
verdict SPLITS.**

| cluster | columns | verdict |
|---|---|---|
| 🟢 **`prompt_revisions` + `prompt_heads` + `prompt_release_events`** | **`18`** | 🟢 **ADOPT AS IS.** `content_hash`, `body`, `base_revision_id`, `created_by`, `previewed`; and release events carrying `action`, `revision_id` and **`previous_revision_id`** — 🟢 **lineage, not just a timestamp.** All `3` FKs carry no `ondelete`, so the release record survives a revision delete |
| 🔴 **`teacher_review_events`** | **`11`** | 🔴 **DO NOT ADOPT AS IS.** `class_id` → `learning_classes` and `assignment_id` → `assignments` are both `ondelete="CASCADE"`. 🔴 **Deleting the class deletes `corrected_assessment`, the human's override of the machine** |
| 🔴 **`quality_review_*`** *(`12` tables)* | **not measured** | 🔴 **NOT RUN.** The store modules' paths appear in no document, `6` guessed paths `404`, and there is no tree listing here *(`Gap 422`)*. 🔵 **Treat the `12` tables as UNVERIFIED, not as present** |

🟢 **The sentence this amendment exists to make sayable:** *"we adopted a permissive, published
prompt-governance schema unchanged, and we repaired the one FK that would have deleted the teacher's
override."* 🔵 **Both halves of that sentence are checkable, and the second half is the one a
regulator cares about.**

## Pass 185 — 2026-10-14

🆕 🟢 **Three new patterns and two amendments, and every repository named below had its licence read
over the raw channel during this pass — not carried from a prior one.**

### 🆕 🟢 Pattern `28` — data-resident lecture capture with local transcription and an agent over the transcript

🔵 **The layer this shelf had `0` rows for until `ACTION ME` read
[`opencast/opencast`](https://github.com/opencast/opencast).** For a university under a
data-residency constraint, this is the only permissive path measured on this shelf where **no
learner audio leaves the institution.**

| step | component | licence | the seam, as measured |
|---|---|---|---|
| `1` | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **`ECL-2.0`** *(`11 340` B)* | `oc_series` for the course, `oc_scheduled_extended_event` for the recording, `oc_assets_snapshot` for the versioned media, `oc_acl_managed_acl` for access |
| `2` | `modules/speech-to-text-impl/…/engine/WhisperCppEngine.java` + `etc/…WhisperCppEngine.cfg` | 🟢 in-tree | 🟢 **a LOCAL engine. Swap `VoskEngine` for lower cost, `WhisperEngine` for quality — all three ship** |
| `3` | `modules/speech-to-text-workflowoperation` | 🟢 in-tree | 🟢 **the named attachment point: a workflow operation, so the agent is configuration, not a fork** |
| `4` | `oc_transcription_service_provider` / `oc_transcription_service_job` | 🟢 in-tree | 🟢 **the provider abstraction is in the SCHEMA — a new provider is a row** |
| `5` | retrieval over the transcript + `oc_search` | — | 🔵 the published index already exists; the agent reads it rather than re-indexing the media |
| `6` | audit of every agent turn | 🟢 **`Apache-2.0`** | 🟢 **borrow the shape from [`ningkaikok/dotty-tutor`](https://github.com/ningkaikok/dotty-tutor): `tutor_turn_requests`, `tutor_tool_events`, `model_call_metrics`** |

🔴 **Price these two honestly in the first conversation:** `230` modules is a platform to operate,
not a library to import; and **`0` of `opencast`'s `17` locale catalogues is `pt-BR` or `pt-PT`**, so
a Brazilian deployment starts with a translation project *(`es-ES` and `gl-ES` are present, so a
Spanish-language engagement does not)*.
🟢 **Contributing back is cheap: upstream ships `AGENTS.md` and `CLAUDE.md`.**

### 🆕 🟡 Pattern `29` — `pt-BR` essay scoring, priced as TRAINING rather than inference

🔵 **`Gap 372` has been this KB's longest-standing capability gap. `ACTION MF` closed its PERMISSIVE
half and this pattern states what is still missing, because an engagement that assumes inference
will fail in week two.**

| step | component | licence | what it actually does |
|---|---|---|---|
| `1` | [`lplnufpi/essay-br`](https://github.com/lplnufpi/essay-br) | 🟢 **`MIT`** *(`1 114` B, UFPI)* | 🟢 **`6 577` Brazilian secondary-school essays, human-graded on the five ENEM competencies `c1`…`c5` + total, `417` prompts, `13.0` MB** |
| `2` | [`readerbench/readerbench-java`](https://github.com/readerbench/readerbench-java) | 🟢 **`Apache-2.0`** *(`10 758` B)* | the feature extractor — emits the `RB.*` columns |
| `3` | [`shmercer/writeAlizer`](https://github.com/shmercer/writeAlizer) v`1.7.4` | 🟢 **`MIT + file LICENSE`** | `import_rb()` → `preprocess()` → `predict_quality()`; the contract is the **`1 316`-column** `sample_rb.csv` header |
| `4` | `inst/metadata/artifacts.csv` | 🟢 committed | 🟢 **`50` artefacts, `24` of them `rb_*` *(no gated tool)*, every one with a pinned `sha256`** — mirror these before the engagement starts |
| `5` | a human review gate | 🟢 **`Apache-2.0`** | 🟢 **`dotty-tutor`'s `quality_review_*` cluster (`9` tables) + `teacher_review_events` is the shape; do not invent one** |

🔴 **The honest verdict, and it is the point of the pattern:** `writeAlizer`'s `rb_*` models are
trained on **English** writing samples. 🟢 **For English, steps `1`–`4` are an inference pipeline
today.** 🔴 **For `pt-BR`, `essay-br` is TRAINING DATA and the deliverable includes fitting and
validating a model per competency — a different scope, a different price, and a different
conversation about accuracy.** 🔵 **`ACTION ML` is pre-registered to settle the rubric mapping
rather than let this pattern imply it.**

🔴 **And the regulatory step nobody may skip:** automated essay scoring is *evaluation of learning
outcomes*, an **Annex III** high-risk use. 🔵 **Whatever the application date turns out to be
*(reported moved to `2027-12-02`, unverifiable from here)*, the deliverable needs the audit trail,
the human-review record and the Article `50`(2) marking from day one — the marking obligation is
reported due `2026-12-02`, which is the nearer deadline.**

### 🆕 🟢 Pattern `30` — the licence read order, forced by `9` overturns and `4` false presences in one pass

🔵 **This replaces *"check the licence"* with a sequence, because this pass measured every step
failing on at least one row.**

| step | question | what fails without it |
|---|---|---|
| `1` | Does the slug EXIST? `git ls-remote` | 🔴 `apereo/opencast` cost five passes of *"unprobed"* and one second of `ls-remote` |
| `2` | Licence FILE, over `raw.githubusercontent.com`, in **both cases** of the filename | 🔴 `pipwerks` has no `README.md` but a `readme.md`, and its grant lives there |
| `3` | Licence heading — including `Licence`, `Licencia`, `版权协议`, `ライセンス` | 🔴 `a5anka` writes `## Licence`; a `License`-only grep reports nothing |
| `4` | The BODY, with no keyword suppression | 🔴 `haolpku/Omni-Edu`'s `Apache-2.0` was suppressed by a `third-party` filter — a self-inflicted false negative on a `225`★ row |
| `5` | **Whose** licence is it? Exclude dependency inventories | 🔴 `jadrianlg16/learning-tutor` lists three dependency licences inside a section that reserves all rights |
| `6` | If the README names a FILE, does the file exist? | 🔴 `DMontgomery40/mcp-canvas-lms` points at an absent `LICENSE` — the most dangerous form, because both channels look settled |
| `7` | Is the token a GRANT or a CLAIM? | 🔴 a `shields.io` badge, *"MIT — demo use only"*, *"open source for educational purposes"* — none of the three is a licence |
| `8` | Is there an identifiable LICENSOR? | 🔴 `dotty-tutor` has a complete `Apache-2.0` with `Copyright [yyyy] [name of copyright owner]` unfilled, no `NOTICE`, no contact — harder to clear in review than a short `MIT` with a name |
| `9` | Is there a SECOND grant for content or weights? | 🔴 `Omni-Edu` carves out model weights; `BloodCoded_Agentic` releases `data/knowledge/` under `CC BY-SA 4.0` in a README sentence with no file |

🟢 **Instrument for steps `3`–`4`:** [`compose/code/p1049-bare-token-grant`](code/p1049-bare-token-grant/README.md).

### 🟡 Pattern `27` amended — run `P1049` BEFORE the ask

🔴 **Pattern `27` *(the unlicensed-supply triage)* sent a studio straight to the ASK when the best
schema in a shortlist had no grant.** 🟢 **Step `0` is now: run the bare-token pass. `9` of `61`
*"unlicensed"* rows on this shelf were already granted, `6` of them permissively — an email asking
for a licence that already exists is the most expensive kind of cheap step.**
🔵 **And when an ASK is still needed, prefer a row whose grant is COMPLETE but whose LICENSOR is
missing** *(`dotty-tutor`: one sentence to fix)* **over a row with no grant at all**
*(`xueyoujing-companion`: a decision for the holder, not a correction)*.

### 🟡 Pattern `24` amended — stop hand-building the Annex III audit layer

🔴 **Pattern `24` builds a decision-audit layer by hand, because the only schema this KB had seen
with one was unlicensed at `2`★.** 🟢 **`dotty-tutor` declares it under `Apache-2.0`: `9`
agent-audit tables *(`tutor_turn_requests`, `tutor_tool_events`, `tutor_observation_events`,
`model_call_metrics`, …)*, `3` prompt-governance tables *(`prompt_heads`, `prompt_revisions`,
`prompt_release_events`)* and `12` human-review tables *(`quality_review_*`, `teacher_review_events`,
`ai_reviews`, `review_tasks`)*.** 🔵 **`ACTION MJ` will check those `24` tables column by column
against the pattern's requirement before this amendment is treated as complete — until then, adapt
and verify, do not assume.**

## Pass 184 — 2026-10-13

🆕 🟢 **One new pattern, two amendments, and both amendments are repairs to steps that this pass
measured failing.**

### 🆕 🟢 Pattern `27` — the unlicensed-supply triage

🔴 **The number that forces this pattern: `3` of `10` rows screened from GitHub's own education
topic pages have NO grant** — no licence file on any path, no grant text anywhere, not even the
word in `33` `.md` files. 🔴 **And the best schema in the sample is one of them:**
[`ZQR1101/xueyoujing-companion`](https://github.com/ZQR1101/xueyoujing-companion), `22` tables
including `students`, `concepts`, `mastery_states`, `mastery_snapshots`, `diagnosis_reports`,
`evidences`, `path_decisions`, `learning_reflections` and `rag_traces` — **a mastery model with the
decision-audit layer Pattern `24` otherwise builds by hand.** 🔵 **At `2`★.**

**The triage, in order, when a shortlisted row has no grant:**

1. 🔴 **Confirm the absence with THREE probes, not one.** A per-path licence-file search
   *(`Gap 370`: a root-anchored probe reported `0` on `formalms`, which holds `19`)*; a grant-TEXT
   search *(*"Permission is hereby granted"*, *"GNU GENERAL PUBLIC"*, *"Apache License"*)*; and
   🆕 **a BARE-TOKEN search over `README` headings** *(`P1049` — `trainingllm`'s entire grant is the
   word `MIT` under `## License`, invisible to the first two)*.
2. 🟢 **Price the ASK before pricing the build.** A low-star holder is a reachable person: one issue
   naming `MIT` or `Apache-2.0`, with the engagement context, costs minutes. 🔵 **`ACTION MC` runs
   this on `xueyoujing-companion` and records the latency, so the next proposal can quote a real
   response time instead of a hope.**
3. 🔴 **Never ship against an unlicensed tree while the ask is open.** 🔵 **Unlicensed is all rights
   reserved; a permissive-looking README, a star count and an open issues tab change nothing.**
4. 🟢 **Extract the SCHEMA, which is not the code.** 🔵 **A table list read from a repository is a
   design fact, and this KB's own patterns are built from design facts** *(Pattern `24` came from
   reading `civil-ai`'s audit tables)*. 🟢 **Re-implementing a `22`-table design you have read is a
   normal engagement; copying its code is not.** 🔴 **Where the design is itself protected is
   counsel's question, and a studio asks it before it builds.**
5. 🟡 **Carry the row as BLOCKED, not as rejected.** 🔵 **A grant can arrive in one commit, and a
   row that was blocked for a licence is the cheapest row to promote later** — the reading is
   already done.

🔵 **Where this pattern applies: at the point a shortlist is handed to a delivery lead. 🟢 Its
output is a row-by-row *buildable / blocked / ask-pending* split, with the ask already sent.**

### 🔴 Pattern `25`, amendment — step `3` was measuring a vocabulary, not a schema

🔵 **Step `3` said: *"count the DOMAIN entities — grep the persistence models for `course`,
`lesson`, `enrollment`, `assessment`."*** 🔴 **Measured this pass, that step fails in BOTH
directions:**

| direction | row | what the grep says | what is true |
|---|---|---|---|
| 🔴 false POSITIVE *(`T310`)* | `open-tutor-ai-CE` | packages named `courses/`, `classrooms/`, `learners/` | 🔴 `4` of them are `30`-byte docstrings; the schema is OpenWebUI's chats |
| 🆕 🔴 false NEGATIVE *(`T314`)* | `ai-shifu` | **`0`** tables named `course`, `lesson`, `enrollment`, `assessment`, `quiz`, `grade`, `student`, `classroom`, `cohort`, `teacher` | 🟢 **a versioned authoring model, `8`-state per-learner progress, and an entitlement table — under `shifu`, `outline_item`, `progress_record`, `course_auth`** |

🟢 **Step `3`, replaced:** **LIST the entity declarations and READ the list.** Dump every
`__tablename__`, `CREATE TABLE`, `_name` or model class in the tree, then read the names and the
columns of the three or four that look load-bearing. 🔵 **The list is bounded — `71` for
`ai-shifu`, `15` for a render pipeline, `22` for `xueyoujing-companion` — so reading it is cheaper
than defending a grep.** 🔴 **A vocabulary grep is never a read, in either direction.**

🆕 🔴 **And two probe defects this pass measured, both generic enough to carry into the recipe:**

- 🔴 **`P1048`: anchor your declaration pattern.** `_name *=` also matches `_rec_name`, whose values
  are FIELD names — `17` occurrences in `openeducat_erp`, which is why a first count said `102`
  distinct models where the anchored count says `88`. 🔵 **An unanchored probe manufactures entities
  that are columns.**
- 🔴 **The corpus screen has a `75`% false-positive rate** *(`ACTION LZ`, `3` of `4` flags)*:
  `Thumbs.db` matched `\.db$`; a SOURCE directory named `embedding/` matched twice; documentation
  PDFs matched a `documents/` rule. 🟢 **Keep the corpus check as a screen with a PROVENANCE read
  attached** — the file name cannot tell `example_upload_images.pdf` *(own fixture)* from
  `Machine - Learning - Tom Mitchell.pdf` *(a publisher's book)*. 🔴 **It is not a census column.**
- 🆕 🔴 **And it cannot see the runtime case at all** *(`Gap 414`)*: `writeAlizer` commits `0` model
  objects and downloads `18` at runtime. 🔵 **Any row with a `download()` entry point has a second
  grant that no clone will show — add a one-line check for one.**

### 🟢 Pattern `26`, amendment — the boundary is MEASURED, and the line is `_inherit`

🔵 **Pattern `26` proposed the SIS engagement as modules: deploy `openeducat_erp` unmodified, add
nothing inside `openeducat_*`, build the missing `OneRoster` / `LTI 1.3` / `Ed-Fi` layer as new
addons, keep the AI in a separate permissive service.** 🟢 **The architectural claim is now
measured at `HEAD 46a5d7d`:**

- 🟢 **`0`** occurrences of `odoo.addons.openeducat` in any `.py` file in the tree.
- 🟢 **`218`** `env['op.*']` accesses by model-name string — *openeducat's own* `14` modules cross
  their own boundaries exactly this way.
- 🟢 Inter-module coupling is `__manifest__.py` `depends`, which is **data, not an import**.

🟢 **So *"add, do not patch"* is architecturally sound: a new addon reads and writes the `59` `op.*`
business models through the registry without importing openeducat's Python.**

🟡 **The amendment: `_inherit` is the line.** `55` anchored `_inherit` declarations exist in the
tree, and `_inherit = 'op.course'` from a new addon **extends openeducat's model in place.**
🔵 **Reading `op.*` and extending `op.*` are different acts — the first adds a model beside the
library, the second alters the library's own.** 🔴 **Whether `LGPL-3.0` §`5` treats
registry-mediated inheritance as *"a work that uses the Library"* is a question for counsel, and
the pattern now carries that line instead of a one-liner that implies an answer.** 🟢 **Practical
instruction unchanged and now justified: new models and `env[]` reads, yes; `_inherit` into
`op.*`, ask first.**

🔴 **Entity count corrected inside the pattern: `59` business models, not `141`** *(`88` `_name`
declarations + `55` `_inherit` extensions = `143`, which is how that figure arose)*. 🔵 **Budget
modules against `59` entities.**

### 🟡 Pattern `5`, amendment — the LATAM localisation line item shrinks

🟢 **`ai-shifu` ships `ar-SA`, `de-DE`, `en-US`, `es-ES`, `fr-FR`, `th-TH`, `ur-PK`, `zh-CN` — the
first `es` catalogue on this shelf.** 🔵 **So Pattern `5`'s *"every LATAM build carries an explicit
localisation line item"* becomes: **a DIALECT ADAPTATION line item** *(`es-ES` → `es-419`)* for a
row that already has Spanish, and a full localisation line item everywhere else. 🔴 **`pt-BR` is
still absent from every row on the shelf, so a Brazilian engagement pays the full price.**

## Pass 183 — 2026-10-13

🆕 🟢 **One new pattern, two amendments, and the amendment to Pattern `25` is a repair: the recipe
was missing the cheapest step in it.**

### 🆕 🟢 Pattern `26` — the SIS engagement, which is modules and not a build

🔵 **The problem this pattern answers has been in this KB as an absence for `16` passes: a client
needs a student-information system, `0` permissive ones exist, and *"budget a build"* is the
answer that absence implies.** 🆕 🟢 **`ACTION LR`'s by-product makes a cheaper answer defensible:
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) *(`LGPL-3.0`,
`HEAD 46a5d7d`)* carries **`141` Odoo models across `13` modules** — admissions, examinations,
marksheets, attendance, fees, library — and `T162`'s missing interoperability layer is exactly
where a studio's work goes.**

**The recipe:**

1. 🟢 **Deploy `openeducat_erp` unmodified**, on Odoo. 🔵 `op.admission`, `op.course`, `op.batch`,
   `op.exam`, `op.marksheet.register`, `op.attendance.sheet`, `op.academic.year`, `op.fees.terms`
   and `op.grade.configuration` are already modelled. **Do not re-model them.**
2. 🔴 **Write NOTHING inside `openeducat_core` or any `openeducat_*` module.** 🔵 **`LGPL-3.0`
   reaches the module you modify; a module you ADD beside it is yours.** 🟢 **This is the whole
   licence strategy and it is one sentence: add, do not patch.**
3. 🟢 **Build the interoperability layer as new modules** — the `T162` gap. 🔵 A `OneRoster`
   roster-sync module, an `LTI 1.3` launch module, an `Ed-Fi` export module. 🟢 **Each is a new
   addon that reads `op.*` records through Odoo's ORM, so each stays closed if the client wants it
   closed.**
4. 🟢 **Put the AI layer in a separate service, not in an addon.** 🔵 Pair with
   [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) *(`MIT`)* for assessment or
   [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) *(`Apache-2.0`)*
   for automated grading — both `ROUTE`-grade and both permissive, so the AI work carries no
   copyleft at all.
5. 🟢 **Make every agent action auditable from day one** with
   [`compose/code/agent-tool-receipts-port/`](code/agent-tool-receipts-port/README.md) — the
   schema is `MIT`-derived and runs on stdlib `sqlite3`.
6. 🔴 **Price three risks explicitly, because none of them is an engineering surprise:** Odoo
   coupling *(its licence posture and upgrade cadence come with the choice)*; the bundled-dependency
   warning in `openeducat`'s own licence header *(*"external libraries… may be published under
   other GPL-compatible licenses"* — a dependency closure is a separate job)*; and the open-core
   declaration *(a free self-hosted Community Edition against paid Enterprise staff seats)*.
7. 🟡 **Route the resale question to counsel.** 🔵 **`LGPL` linking semantics for Python/Odoo
   addons are a legal reading, not a measurement.** 🟢 Say *"weak copyleft, scoped to the modules
   you edit"* and stop there.

🟢 **What this pattern replaces:** a from-scratch SIS estimate. 🔵 **What it costs:** an `LGPL`
conversation and an Odoo dependency. 🟢 **What it buys:** `141` entities a studio does not write,
and a deliverable — the standards layer — that is genuinely missing rather than invented.

### 🔴 Pattern `25`, amendment — the recipe was missing its first step

🔵 **Pattern `25` is the pre-engagement read: clone, count tables, read the licence payload,
grade.** 🔴 **`ACTION LR` ran it on `3` rows this pass and all `3` turned out to be already in
this KB's census, with settled licences. A screening recipe that re-screens read rows measures
recall, not prediction.**

🟢 **Step `0`, adopted:** **grep the census for the slug BEFORE anything else.** 🔵 **If the row is
already there, the question is not *"what is this"* — it is *"which layer is still unmeasured"*,
which is a different and usually cheaper read.

🆕 🔵 **And `T313`, which is why step `0` pays for itself: a row with a verified licence is not a
read row.** 🔴 **All `3` rows re-read this pass had settled grants and `0` had a settled schema —
and in all `3` the schema is what decided them** *(a Stripe billing schema; `141` real SIS
entities; a committed textbook corpus)*. 🟢 **So the census pre-check does not skip work, it
RE-TARGETS it: from the grant, which is cheap and binary and already done, to the entity list,
which is expensive and deciding and usually missing.**

🆕 🟢 **Step added to the body of the recipe — the corpus check:** 🔴 **after reading `LICENSE`,
look for a committed index, corpus or model checkpoint** *(`db/*.sqlite3`, `*.bin`, `documents/`,
`*.pdf`, `*.safetensors`)*. 🔵 **A vector index is a derivative of what it was built from, and the
code licence does not reach it.** 🟢 **`TeachGPT` is cleanly `MIT` and ships a commercial textbook
plus its embeddings — the trap is invisible in the licence file.**

### 🟢 Pattern `24`, amendment — the auditable assessment stack now has a RUNNING artefact

🔵 **Pattern `24` was written at p182 as a reading recommendation: borrow `civil-ai`'s
`agent_tool_receipts` and `assessment_policy_versions`.** 🟢 **`ACTION LV` ported them. `18`
checks, `0` failures, stdlib `sqlite3` only, at
[`compose/code/agent-tool-receipts-port/`](code/agent-tool-receipts-port/README.md).** 🔵 **The
pattern can now hand a client code instead of a citation.**

🆕 🔴 **Two amendments the port forced, and both are deployment facts the schema cannot express:**

| 🆕 finding | what Pattern `24` must now say |
|---|---|
| 🔴 **SQLite's `PRAGMA foreign_keys` is OFF by default** | 🔴 **An `ON DELETE RESTRICT` policy FK enforces NOTHING until a connection turns it on.** 🟢 **The pattern's verification step is no longer *"the migration has the FK"* — it is *"a live connection refuses the delete"*, which the port asserts in a test, and which also reproduces the ORPHAN when the pragma is off |
| 🔴 **`RESTRICT` on the policy, `CASCADE` on the receipt** | 🔴 **Deleting the parent agent run deletes its receipts.** 🟢 **So the pattern gains a requirement the source does not have: if the record must survive, the receipt's parent FK cannot be `CASCADE`.** 🔵 **The rule a grade was given under is protected; the evidence that an agent applied it is not** |

🟢 **The honest framing for a client, which is better than the one Pattern `24` had:**
🔵 ***"we have audit tables"* is a claim about a schema; *"the record survives a delete"* is a
claim about a deployment.** 🟢 **Only the second is worth anything to a regulator, and only the
second can be demonstrated — which is what the `18` checks do.**

🟢 **Where this lands in a proposal:** North American human-oversight expectations and EU Annex III
documentation want the same artefact, and the EU date is `2` December `2027` *(Regulation (EU)
`2026/1744`)*, so this is build-now work with a known deadline rather than remediation. 🔵 **Two
procedural facts worth adding to the Annex III conversation this pass** *(see
[`intel/market.md`](../intel/market.md))*: **conformity assessment is INTERNAL CONTROL** for most
Annex III education systems absent real-time biometrics, and **a voluntary Code of Practice on
transparency has been available since `31` July `2026`** — cheap to adopt, visible to a reviewer.

## Pass 182 — 2026-10-13

🆕 🟢 **Two amendments that make existing patterns CHEAPER, one new pattern that is the audit
stack a North American district and an EU Annex III deployment both need, and one new pattern that
turns this pass's `3`-in-`4` overturn rate into a priced pre-engagement step.**

### 🟢 Pattern `22`, amendment — the multi-tenant claim is VERIFIED, so the estimate stands

🔵 **Pattern `22` told a studio not to budget for adding a tenant key when starting from
[`tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp). That rested on a schema read.
🆕 `ACTION LN` read the query layer and the claim HOLDS.**

🟢 **What you are actually inheriting, and it is more than a column:**

1. 🟢 **A typed boundary.** `models/principal.go:33` — `TenantScope{TenantID, UserID,
   MembershipID, EnrollmentID, LearnerID}`. **`36`** `Store` methods across **`14`** files take it
   as their first argument after `ctx`, so an unscoped persistence call does not compile.
2. 🟢 **Fail-closed admission.** `TenantScope.Validate()` rejects absent or ambiguous identity;
   `auth/middleware.go:171` `WithPrincipal` *"admits only a fully validated, single-tenant
   identity into a business context"* and errors otherwise; `GetPrincipal` re-validates on read.
3. 🟢 **Predicates where rows are fetched.** **`350`** `tenant_id` predicates across **`75`**
   files in `db/`.
4. 🟢 **Anti-replay you did not have to think of.** `SessionBindingID()` =
   `sha256(tenantID ‖ membershipID ‖ userID)`, to stop a session opened in tenant A being replayed
   with another membership of the same global user in tenant B.
5. 🟢 **Tests that assert REFUSAL**, not just success: `TestWithPrincipalRejectsMissingTenant`,
   `TestAssessmentReviewRejectsForeignTenantAndInvalidPages`,
   `TestClientCredentialsGrantIssuesTenantBoundAccessTokenOnly`,
   `TestVerifyJWTClaimsRejectsTenantlessAndOldTokens`, `saas_noisy_neighbor_load_test.go`.

🟡 **The one thing to check in week `1`:** the code says `LearnerID` is *"retained during the
expand/backfill migration"* and `EnrollmentID` is optional until an enrollment is selected.
🟡 **Read the migration state before you quote a date — not because tenancy is unfinished, but
because the learner key is mid-move.** 🟢 `LegacyTenantID = "tenant_legacy"` is documented as a
real tenant, not a wildcard, so legacy rows are inside the model rather than exempt from it.

### 🟢 Pattern `20`, amendment — delete the IdP precondition

🔴 **Pattern `20` was about to carry *"the client operates a Keycloak"* as a precondition for the
institutional route.** 🆕 🟢 **`ACTION LQ` establishes it does not.**

| step | before | 🆕 after |
|---|---|---|
| identity | 🔴 *"client must operate a Keycloak / IdP"* — a procurement conversation | 🟢 **Nothing required.** `app.saml.enabled` defaults to `false` in [`feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem)'s `application.yaml`; `SecurityConfig.kt:184` has an unconditional `formLogin`; `saml2Login` is the conditional branch |
| what you can offer instead | — | 🟢 **`fbs-identity-service` is ITSELF an OIDC provider** — client `fbs-web-shell`, signing key alias `identity-signing`, its own access-token and authorization-code TTLs. Put other services behind it |
| when the client's IT asks for SSO | 🔴 blocked on procurement | 🟢 **A configuration**: set `APP_SAML_ENABLED=true` and the IdP metadata vars. `docs/saml-local-keycloak.md` + `application-saml-local.yaml` are the worked local example |

🟢 **Net effect: the institutional route starts in week `1` instead of after an identity-platform
decision.**

### 🆕 🟢 Pattern `24` — the auditable assessment stack, for North America and EU Annex III at once

🔵 **The problem both regimes pose is the same one: prove a human decided, prove which policy was
in force, and prove what the agent did.** 🟢 **Every piece below is permissive and was measured
this pass or last.**

| layer | repo | licence | what it contributes |
|---|---|---|---|
| **1. platform + identity** | [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) *(institutional)* or [`tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) *(multi-tenant SaaS)* | `Apache-2.0` / `MIT` | cohorts, roles, own auth. `tutor-mcp` additionally gives enforced tenancy |
| **2. the audit schema — borrow it, do not invent it** | [`civil-ai`](https://github.com/zhangl1001/civil-ai) | `MIT` | 🆕 **`assessment_policy_versions`** *(`001_foundation.sql:104`, referenced by FK with **`ON DELETE RESTRICT`** at `:211`)* and **`agent_tool_receipts`** *(`032_agent_tool_receipts.sql`, indices on `status, updated_at` and `business_idempotency_key`)* |
| **3. the receipt write path** | same | `MIT` | 🆕 **A real state machine to copy**: `claim()` → `Prepared` → `Running` → `Succeeded`/`Failed`/`Unknown`, via `DurableAgentToolExecutor.ts`, with `replace(receipt, expectedVersion, guard)` optimistic concurrency and a `120 000`-char content cap |
| **4. grading with a human checkpoint** | [`feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | `Apache-2.0` | automated checkers whose output a human adjudicates — 🆕 and no IdP needed |
| **5. integrity evidence** | [`dolos`](https://github.com/dodona-edu/dolos) | `MIT` | similarity detection, executed and calibrated by this KB *(Pattern `1`, with its upper bound)* |
| **6. adjudication record** | [`tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | `MIT` | `assessment_adjudications`, `assessment_review`, `assessment_review_journal` already modelled, all tenant-scoped |

🟢 **How to wire it.** Keep the agent NON-ADJUDICATING *(Pattern `3`)*: the agent writes a
`agent_tool_receipts` row before acting and transitions it after, the grade it proposes lands in
`assessment_review`, and a human's decision writes `assessment_adjudications`. Pin every automated
decision to the `assessment_policy_versions` row in force at that moment — the `ON DELETE RESTRICT`
FK means the policy cannot later be deleted out from under the decision it governed.

🟢 **What it buys, per region.** 🇺🇸 **North America:** Oklahoma/Maryland-style *"human oversight,
no high-stakes AI decision"* is satisfied structurally, and per-state policy becomes a row rather
than a branch. 🇪🇺 **EMEA:** Annex III *(access decisions, outcome evaluation, exam monitoring,
`2` Dec `2027`)* asks for exactly this record. 🌏 **APAC:** Vietnam's `1` Mar `2027` compliance
date arrives first and names automated assessment explicitly.

🔵 **Honest scope note: steps `2` and `3` are a SCHEMA and a pattern to port, not a library to
import — `civil-ai` is an app, not a package. Budget the port; it is still cheaper than designing
the audit model.**

### 🆕 🟢 Pattern `25` — the pre-engagement read, priced

🔴 **This pass screened `4` unread candidates from published metadata and reading overturned `3`
of them** *(`ACTION LR`, `n=4`)*: an `MIT`-listed LMS that is `AGPL-3.0`, an *"educational agent
platform"* that is a CRM, and an *"educational platform"* with `0` course entities.
🟢 **So make the read a step, not an assumption.**

**The recipe, in order, per candidate. Each step is a few seconds on these trees.**

1. 🟢 **Clone shallow.** `git clone --depth 1 <url>`. 🔵 **In this environment that is also the
   only reliable existence check: `github.com` and `api.github.com` answer `403` (`gap 140`), so
   `curl -sI` verifies nothing and a successful clone of the exact path verifies more.**
2. 🔴 **Read the LICENCE as a FILE and size it.** Not the roundup, not the badge, not the API
   field. `frappe/lms` is `33 893` B of Affero where a `2026` roundup printed `MIT`.
3. 🔴 **Count the DOMAIN entities, not the tables.** Grep the persistence models for `course`,
   `lesson`, `enrollment`, `assessment`. 🔵 `open-tutor-ai-CE` has `4 702` files and `0` of them.
4. 🔴 **Find the identity STORE, not the word `auth`.** A `users` table or a `class User`.
   `DeepTutor` keeps users in a JSON file; `anki-mcp-server`'s `auth` is an MCP client credential.
5. 🟢 **For any claimed capability, find the WRITE SITE or the ENFORCEMENT POINT.** `INSERT INTO`
   for an audit table; a scope type and a middleware for tenancy. 🔵 This is what separated
   `civil-ai` and `tutor-mcp` *(real)* from a schema that merely reads as architecture.
6. 🔴 **Check the four lexical traps before believing a probe:** `session` *(study, not auth)*,
   `xapi` *(a README comment)*, `enrollment` *(a marketing follow-up sequence)*, `keycloak`
   *(a default registration name, not a dependency)*.
7. 🟢 **Check the locale catalogue** for the engagement's language. 🔴 **No shelf row carries `es`
   or `pt-BR`** — on a LATAM engagement that is a line item, found in step `7` rather than in
   week `6`.

🔵 **Where this pattern applies: before a shelf row enters a proposal. 🟢 Its output is a verdict
plus the evidence that produced it, which is also what a client should be shown instead of a star
count** *(none is obtainable here anyway — `gap 140`)*.

### 🟡 Pattern `5`, amendment — LATAM, with the gap now measured

🔵 **Pattern `5` said *"import the components, sell the governance"*. 🆕 Both halves get sharper.**

🟢 **Sell the governance — the number is `87`/`26`.** UNESCO IESALC `2026`: `87`% of `200`
institutions across `19` countries use AI somewhere, **`26`% have a formal AI strategy**. 🔵 **That
`61`-point gap IS the engagement: policy, oversight checkpoints and the audit trail from Pattern
`24`, sold to institutions that already have the adoption and cannot defend it.** Anchor to the
UNESCO LAC Observatory *(April `2026`: CAF, CENIA, CETIC.br, ECLAC, Tec de Monterrey, ProFuturo,
Fundación Ceibal)*, Colombia's CONPES `4144` and Uruguay's Council of Europe convention signature.

🔴 **Import the components — and price the localisation.** `ACTION LP` searched in Spanish and
Portuguese, cloned every candidate, and found **`0` LATAM-origin and `0` LATAM-localised rows**.
🟢 **No shelf row has an `es` or `pt-BR` catalogue. So every LATAM build carries an explicit
localisation line item** — and the one row that proves it is achievable is
[`open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE), which maintains `ar-MA`,
`fr-FR` and `en-US` side by side *(and `lumen`, p181, which holds an i18n-parity TEST — copy that
idea regardless of its `GPL-3.0`)*.


## Pass 181 — 2026-10-13

🆕 🟢 **Two new patterns, one amendment that ADDS A BOUND rather than a step, and one pattern whose
cost line finally has numbers in it.** 🔵 **Everything below names specific repositories at
specific commits, with the measurement that justifies each choice.**

### 🆕 🟢 Pattern `22` — the MULTI-TENANT route, for a client who sells to many institutions

🔵 **Why this is new:** every route this KB has published assumed ONE institution per deployment.
🟢 **[`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) *(`MIT`, `1 073` B,
`md5 6ef9d4b578ace4e94d9ae2f1e6054688`)* is the first row on this shelf that models tenancy
itself** — `tenant_id` resolved in `auth/console.go`, `auth/oauth.go` and `auth/learn.go`, an
`Institution` selector in its own login template, and `cohorts`, `cohort_trainers`,
`cohort_statistics`, `cohort_concept_statistics`, `cohort_badge_statistics`, `account_tokens`,
`audit_events`, `billing_provider_events` and `assessment_adjudications` among `240` `CREATE TABLE`
statements across `694` files of Go.

**The wiring, part by part:**

1. 🟢 **Tenancy + identity + billing — `tutor-mcp` as shipped.** Do not add a tenant key; it is
   already the axis the schema turns on *(`tenant` in `151` files, `bcrypt` in `29`, `oauth` in
   `84`)*. 🟢 **`billing_provider_events` means per-tenant commercial metering is modelled, which is
   the part a studio usually writes from scratch.**
2. 🔴 **The interoperability layer is YOURS to build.** `tutor-mcp` has **no `LTI`, no `SCORM`, no
   `QTI`** *(measured `0`)*. 🔵 **This is the pattern's one real cost and it must be quoted up
   front** — see Pattern `23` for the cheapest way to buy the `SCORM` half instead of building it.
3. 🟢 **Integrity — [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) `2.9.3` at threshold
   `0.85`**, with `-i` supplied only when the assignment ships a real handout *(Pattern `1`, as
   amended below)*.
4. 🟢 **Audit evidence — already present.** `audit_events` + `assessment_adjudications` are what a
   human-oversight mandate *(Oklahoma, Maryland)* and an EU Annex III file both ask to see.
5. 🟡 **Model surface — bring your own.** It is an `MCP` server, so the agent runtime is the
   client's choice rather than a vendor lock.

🟢 **Where it fits:** a ministry, a university system, a training provider, or any client reselling
to institutions. 🔵 **Quote the `LTI` build as a discovery item, not a line item, until the client's
institutions are known — half of them may accept `SCORM` instead.**

### 🆕 🟢 Pattern `23` — the permissive `SCORM` bridge, which replaces a build with a configuration

🔵 **The problem it solves:** a permissive non-Java route cannot receive an `LTI 1.3` launch
*(`T305`)*, so content and results cannot flow to the institution's incumbent LMS. 🟢 **But
`SCORM 1.2` CAN flow, and [`Selleo/mentingo`](https://github.com/Selleo/mentingo) *(`MIT`,
`1 062` B, `md5 88f104b7644947b4a8b6e71f4972c02f`, `HEAD 242a9324fe48`)* implements BOTH
directions** — verified in code this pass, not in its README.

| direction | what exists in the tree | where |
|---|---|---|
| 🟢 **export** | own workspace packages `@repo/scorm-export-generator` *(`manifest-builder.ts`, `package-builder.ts`, `course-json-builder.ts`, `runtime-assets.ts`)* and `@repo/scorm-export-runtime` *(a standalone browser player: `src/player/index.html`, `main.ts`)*; `scorm-again@3.0.4` on the web app | `packages/scorm-export-*` |
| 🟢 **import** | `apps/api/src/scorm/scorm.service.ts`, `scorm-storage-paths.ts` with a TENANT-scoped prefix `getScormPackagePrefix(tenantId, packageId)`, `native-archive-import-scorm.e2e-spec.ts`, and real `imsmanifest.xml` fixtures *(`single`, `multi`)* | `apps/api/src/scorm/`, `apps/api/src/native-archive/` |

**The wiring:**

1. 🟢 **Author in the permissive stack** — `mentingo` *(or your own)*.
2. 🟢 **Export `SCORM 1.2`** with `@repo/scorm-export-generator`; the runtime player ships inside the
   package, so the incumbent LMS needs no plugin.
3. 🟢 **Hand the package to the incumbent** — `Moodle` *(`GPL-3.0`)*, `Canvas` *(`AGPL-3.0`)*,
   `Open edX` *(`AGPL-3.0`)*. 🟢 **You never link against their code, so no copyleft obligation
   arises on your side.**
4. 🟡 **Accept the limit honestly:** `SCORM 1.2` carries completion and a score. 🔴 **It does not
   carry the rich interaction data `xAPI` would — and `mentingo` has NO `xAPI`** *(`1` match, inside
   an HTML comment)*. 🔵 **If the client needs per-interaction telemetry, this pattern does not
   deliver it and nothing permissive on this shelf does.**

🔵 **`T311`: for a studio, `SCORM` is the permissive interoperability floor and `LTI` is the
ceiling. The floor is reachable today with `MIT` code; the ceiling is Java-only.**

### 🟢 Pattern `1` — AMENDED at step `2` with an UPPER bound *(`ACTION LB`, discharged)*

🔴 **What p179 did:** made the `-i` template-exclusion step CONDITIONAL on a scaffolded assignment,
reasoning that a bigger handout would matter. 🔴 **That reasoning was never measured.** 🟢 **It is
now, over `7` rungs spanning a `510`× ratio range on a real `MIT` corpus with a ground truth:**

| template | lines | ratio *(template ÷ mean submission)* | median `\|Δsim\|` | honest-work ceiling | separation |
|---|---|---|---|---|---|
| *(none — baseline)* | `0` | `0` | — | `0.6720` | `+0.3178` |
| shared imports *(`≥6` modules)* | `1` | `0.0033` | `0.00000` | `0.6720` | `+0.3178` |
| shared imports *(`≥3`)* — p179's template | `10` | `0.0329` | `0.00064` | `0.6720` | `+0.3066` |
| shared imports *(`≥2`)* | `13` | `0.0428` | `0.00025` | `0.6720` | `+0.3083` |
| 🟢 **one handout module** | `42` | `0.1382` | `0.00816` | 🟢 **`0.6004`** | 🟢 **`+0.3766`** |
| 🟢 **three handout modules** | `155` | `0.5099` | 🟢 **`0.02347`** | `0.5951` | `+0.3581` |
| 🔴 shared lines *(`≥3`)* | `300` | `0.9868` | `0.00862` | `0.6251` | `+0.2922` |
| 🔴 shared lines *(`≥2`)* | `512` | `1.6842` | `0.01412` | `0.6016` | 🔴 **`+0.2897`** |

🟢 **Limb `1` fires on the letter — the effect crosses `0.02` at ratio `0.51`.** 🔴 **But it is NOT
monotonic, and the honest reading is more useful than the limb was:**

- 🔴 **Below ratio `0.05`, `-i` does nothing.** Median `|Δsim|` `≤0.00064`. 🔵 **p179's limb-`2`
  result was correct FOR ITS RATIO and was over-generalised to the step.**
- 🟢 **Between ratio `0.1` and `0.5`, `-i` earns its place** — the honest-work ceiling drops
  `0.6720` → `0.6004` and the separation a grader relies on WIDENS by up to `+0.0588`.
- 🔴 **Above ratio `1.0`, `-i` is HARMFUL.** The known positive erodes from `0.9898` to `0.8912` and
  the separation falls BELOW the no-template baseline.

**So step `2` of Pattern `1` now reads:**

> 🟢 **Supply `-i` with the assignment's actual handout — and only that.** 🔴 **Never a
> machine-generated *"shared lines"* template, and never a template approaching the submission's own
> size: past ratio `1.0` it removes the evidence.** 🟢 **If there is no handout, skip `-i`; at
> header scale it changes nothing.**

🆕 🟡 **And one caution on the published threshold: `0.85`'s margin is not constant.** The worst
known positive falls from `0.9898` *(no template)* to `0.8912` *(ratio `1.68`)* — so the headroom
above `0.85` shrinks from `0.1398` to `0.0412`. 🔵 **The threshold survives the whole ladder, but a
team that both raises the threshold AND supplies a large template will start missing renames.**

### 🟡 Pattern `20` — the cost line it was missing *(`ACTION LG`, limb `2`)*

🔴 **p180 pre-registered *"stand up a running `OpenOLAT` and record the wall-clock cost"*. It was
not measured, and the reason is a policy, not a property of `OpenOLAT`:** `mvn package` on a cloned
subject tree is refused by this harness's external-code policy *(`T303`)*. 🟢 **So the pattern gets
STATIC cost proxies, which are honest and still useful:**

| line item | measured | how to quote it |
|---|---|---|
| 🟢 build shape | **`1`** Maven module → one WAR | 🟢 Simple build graph; CI is not the risk |
| 🟡 dependency resolution | `186` declared dependencies, `24` plugins | 🟡 One slow first resolution; nothing exotic |
| 🔴 **schema discovery** | 🔴 **`385` `CREATE TABLE` in `322 754` B of shipped PostgreSQL schema** | 🔴 **This is the spike. Quote a discovery sprint sized against `385` tables** — against `257` entities for `Artemis` and `34` tables for `OpenTutor` |
| 🟢 runtime | Tomcat `10.0`/`10.1` + PostgreSQL | 🟢 Standard institutional hosting |

🔵 **`T294` stands, restated: this KB has NO evidence about `OpenOLAT`'s boot time and will not get
any here. Pattern `20` quotes a sized discovery spike, and now says what it is sized against.**

### 🔴 Pattern status board

| pattern | status after p181 |
|---|---|
| **`1`** academic integrity | 🟢 **AMENDED — step `2` gains an upper bound, measured** |
| **`2`** Article `50` marking | 🟡 **Ordering holds** *(transparency before conformity)*. 🔴 One sub-point unresolved: whether Article `50` began `2` Aug `2026` is secondary-only *(`gap 110`, carried as `ACTION LM`)* |
| **`18`** appliance → cohort | 🟢 Unchanged, and cheaper now: 🆕 **`tutor-mcp` supplies the tenancy that Pattern `18` told a studio to build** |
| **`19`** buy the adapter shape | 🟢 Unchanged |
| **`20`** permissive institutional stack | 🟡 **Cost line added** *(`385` tables, `186` deps)*; boot time still unknown |
| **`21`** grafting identity onto an appliance | 🆕 🟢 **A third route added: `DeepTutor`'s `USERS_FILE` + optional PocketBase proxy is a MIGRATION target, not a greenfield build** — the concepts *(roles, admin bootstrap, a user store)* already exist and need moving into the schema |
| **`22`** multi-tenant route | 🆕 🟢 **NEW** |
| **`23`** permissive `SCORM` bridge | 🆕 🟢 **NEW** |

### 🆕 🟢 The screening recipe, promoted out of the pass notes because it is reusable

🟢 **`T290` is now a procedure, and it costs about `3` seconds per candidate:**

1. `git clone --depth 1` the candidate.
2. Count entity declarations **across all file types**, not just `*.sql` — 🔴 `DeepTutor` scores
   `0` on a `*.sql`-only probe and has `69`.
3. 🔴 **READ the table names.** `InterviewMentor`'s `20` tables are `dim_customer`/`fact_orders`
   teaching fixtures; `feedbacksystem`'s German tables are a SQL playground for students.
   🔵 **In an education corpus, teaching SQL is a product feature, so a table count over-reports
   by design *(`T300`)*.**
4. Probe identity by CONCEPT, not by one word — `users`, `candidate_profiles`, `learners`,
   `benutzer` — and 🔴 **check whether the store is in the schema at all** *(`DeepTutor`: a JSON
   file)*.
5. 🔴 **Always pass `git grep -I`.** Without it, `mentingo` reports `LTI` support from a `.webp`, a
   `.png` and an `.mp4` *(`T301`)*.
6. Only now look at ★ — and treat it as a measure of how easy the thing is to TRY, not of whether a
   cohort can use it.

## Pass 180 — 2026-10-13

🆕 🟢 **Two new patterns, two amendments, and the amendment to Pattern `2` is a CORRECTION rather
than a refinement: its clock was wrong in kind, not in value.** 🟢 **The pass's new capability is
that Python dependencies now install here (`ACTION LC`, limb `1` fired), which changes what a
pattern may prescribe as verifiable.**

### 🆕 🟢 Pattern `20` — the PERMISSIVE institutional stack, which this KB could not write until now

🔵 **Why it could not be written before:** every full LMS on this shelf was `AGPL-3.0`, `GPL-3.0`,
`LGPL-3.0` or education-scoped `ECL-2.0`, so every institutional recipe had to route around a
copyleft core. 🟢 **`ACTION LE` read [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT)
past its `Apache-2.0` grant and it is a full platform: `440` `@Entity`, `419` `@Table`, `497`
DAO/Manager classes, `199` schema files, Oracle+PostgreSQL+MySQL, its own auth, and `LTI 1.3`.**

**The wiring, named part by part:**

1. 🟢 **System of record —
   [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT)** *(`Apache-2.0`, `10 982` B,
   `md5 6ba3198de8e95979d5895c0827d34bc0`, `HEAD 8494a140b2ca`)*. Courses, enrolments, grades and
   `QTI` *(`1 201` files)* item banks live here. 🟢 **Apache-2.0 means a white-labelled deployment
   and a proprietary AI module beside it need no copyleft conversation.**
2. 🟢 **Identity — OpenOLAT's own.** Wire the institution's existing IdP through
   `LDAPAuthenticationProvider` *(`ldap` in `158` files)* or `Shibboleth` *(`147` files)*; add
   nothing. 🔵 **This is the step every other pattern in this file has had to BUILD.**
3. 🟢 **Assessment — [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis)** *(`MIT`,
   `1 091` B)* attached over `LTI 1.3`. 🟢 **Both ends are verified: OpenOLAT carries `252`
   `LTI 1.3`-specific files (`lti13`/`AssignmentAndGradeService`/`DeepLinking`); Artemis ships
   `LTI 1.3` with Assignment-and-Grade-Services and a nightly Moodle interop test (p178).**
   🔵 **Grades flow back over AGS — do not build a grade bridge.**
4. 🟢 **Integrity — [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos)** *(`MIT`,
   `1 084` B)*, `@dodona/dolos@2.9.3` from npm. 🟢 **Threshold `0.85`, as MEASURED at p179:
   identifier renaming scores `1.0000`, honest sibling code reaches `0.6720`, and the empty band
   between them is `0.3066` wide.** 🔴 **Do not ship the `0.7` clients ask for — it sits `0.028`
   above the honest-work band.**
5. 🟢 **The AI layer — extend, do not invent.** 🟢 **OpenOLAT already carries `openai` in `33`
   files, `llm` in `34` and `ollama` in `13`, with `457` `restapi` files.** 🔵 **`ollama` upstream
   means a self-hosted model path exists before the studio arrives — which is what answers both the
   EU's data questions and California `AB 1159`'s training-data restriction.**
6. 🟢 **Provenance — Article `50(2)` marking from DAY ONE.** 🔴 **Not deferred: see Pattern `2`'s
   amendment below.**

🔴 **The honest cost line, because this pattern is the one most likely to be over-sold:**
🔴 **`OpenOLAT` is `14 809` Java files and `2 624 333` lines, built with `pom.xml`. This KB READ it;
it has not BUILT or RUN it.** 🔵 **Quote a discovery spike to stand up a dev instance before quoting
the engagement.** 🟢 **Pre-registered as `ACTION LG`.**

### 🆕 🟢 Pattern `21` — grafting identity onto an APPLIANCE, two ways, with the cheaper one named

🔵 **The problem this solves is now precisely bounded:** 🟢 **`3` of `8` read shelf rows have no
identity at all** — [`Bloom`](https://github.com/Li-Evan/Bloom) *(`7` tables, `16` write endpoints,
`docker-compose`, `auth` `0`)*, [`Study-Mate`](https://github.com/Miaotofu01/Study-Mate) *(`0` DBs,
`0` servers)* and
[`universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) *(`auth` `0`)*.
🔴 **Each serves exactly one learner per deployment, and a cohort is what a client buys.**

**Route A — BORROW the institution's identity *(cheaper; prefer it)*.** Put the appliance behind an
`LTI 1.3` launch from Pattern `20`'s `OpenOLAT` *(or the client's Moodle/Canvas)*. The launch
carries a stable subject identifier and a context (course) claim; key every appliance row on those
instead of adding a user table. 🟢 **Nothing in `Bloom` has to learn about passwords, and the
institution stays the system of record for who the learner is.** 🔴 **Limit: the appliance still
cannot tell two learners apart in its own UI — it inherits per-launch scope, so it suits a
single-course tool, not a persistent portfolio.**

**Route B — GRAFT a real identity layer.** 🟢 **Copy the shape from
[`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor), which is `MIT` and already has
it:** `users` and `auth_sessions` tables, `class User(Base)`, `services/auth/jwt.py` with
`create_access_token` + `create_refresh_token` + `decode_token` over `jose`, `bcrypt` hashing,
`alembic` migrations, and `user_id` threaded through `202` files. 🔵 **`Bloom` even DECLARES the
right dependencies — `python-jose[cryptography]`, `bcrypt`, `email-validator` — with `0` import
sites for any of them, so the graft is additive, not a rewrite** *(`T285`)*.

🟢 **Verification is now possible for this pattern, which it was not at p179:** 🟢 **`Bloom`'s full
declared dependency set — `15` packages including the `dev` group — installs cleanly here
(`fastapi`, `sqlalchemy 2.1.4`, `uvicorn 0.54.0`, `python-jose`, `bcrypt`, `pytest`,
`ruff 0.17.0`), exit `0`.** 🔴 **Running the subject's own suite is still gated — by harness policy
now, not by the network.**

### 🔴 Pattern `2`, amendment — the clock was wrong in KIND, and the fix inverts the advice

🔴 **Pattern `2` sequenced an EU engagement against *"two clocks"*, treating `2` December `2027` as
a secondary-sourced date under an UNAMENDED AI Act, with the November `2025` *"digital omnibus"*
flagged as a live risk that might move it.** 🟢 **`ACTION LF` settles it: the omnibus was ADOPTED as
Regulation (EU) `2026/1744` — signed `8` July `2026`, OJ `24` July `2026`, in force `27` July
`2026`.**

| obligation | Pattern `2` said | 🆕 corrected |
|---|---|---|
| Annex III high-risk *(admissions, learning-outcome evaluation, exam monitoring)* | `2` Dec `2027`, secondary, at risk of moving | 🟢 **`2` Dec `2027`, now the ADOPTED legal date — deferred from `2` Aug `2026`** |
| Annex I embedded high-risk | not sequenced | 🆕 `2` Aug `2028` *(deferred from `2` Aug `2027`)* |
| Article `50` transparency / synthetic-content marking | treated as part of the same clock | 🔴 **UNCHANGED AND LIVE SINCE `2` Aug `2026`. The omnibus did not touch it** |
| Article `5` prohibitions | not sequenced | 🆕 🟡 two NEW prohibitions phase in `2` Dec `2026` |

🔵 **`T295`: *"the AI Act was delayed"* is false as said to an education client, and the error is
expensive in the wrong direction.** 🟢 **The step a studio can defer is the conformity
documentation for an assessment engine. The step it CANNOT defer is marking synthetic output —
which is the one teams assume the delay covers.** 🟢 **So Pattern `2`'s ordering INVERTS: ship the
Article `50(2)` marking work FIRST, then the Annex III conformity file against a `2` December
`2027` date that is now legally fixed rather than provisional.**

🟡 **Carried risk, recorded not relied on:** whether the adopted text kept the *"conditional on
harmonised standards"* framing. 🔴 **`eur-lex.europa.eu` is `403` on `curl` and `ENOTFOUND` on the
second channel; `gap 110` holds on three channels.** 🔵 **Quote the date; do not quote the
mechanism.**

### 🟢 Pattern `2`'s Article `50(2)` recipe — `ACTION KZ`'s diagnosis DISCHARGED, and p178's note refined

🟢 **The subject is unmoved for a sixth pass:**
[`AkshitIreddy/AI-Powered-Video-Tutorial-Generator`](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator),
`HEAD 9c260890214d`. 🟢 **`/usr/bin/python3.13` is present, as p178 required.**

🔴 **p178 recorded that `_artifact_provenance` *"is the ONLY producer of the `provenanceRecords`
list the gate reads, and its returned dict has no `c2paStatus` key"*.** 🟢 **The second half is
confirmed by direct read. The first half needs refining, and the refinement makes the repair
smaller:**

| finding, read this pass | consequence |
|---|---|
| 🟢 `_artifact_provenance` is at `services/pipeline/src/alystria/generation/workflow.py:2492`; it reads `metadata_json` out of the `artifacts` table and forwards `6` metadata keys by `metadata.get(...)` — `origin`, `rightsStatus`, `licenseId`, `creator`, `attribution`, `sourceUri`, `modelRevision` | 🟢 **The propagation mechanism already exists and is used seven times. `c2paStatus` is simply not among the keys forwarded** |
| 🆕 🟢 **`c2paStatus` IS produced upstream — by `licensed_media_workflow.py:259` and `:290`, which write `"c2paStatus": "absent"` into the artifact metadata AND into the candidate record** | 🔴 **So p178's *"only producer"* is not right: a producer it did not name writes the field into the very store `_artifact_provenance` reads from** |
| 🆕 🟢 **`contracts/generated_schema_registry.py:106` lists `c2paStatus` among the REQUIRED properties of `AssetProvenance`** | 🟢 **The schema already demands the field. `ACTION KZ` limb `2` — *"it breaks → the repair is a schema change"* — is REFUTED in advance: the schema is already right** |

🟢 **So the repair is one line in the returned dict —
`"c2paStatus": str(metadata.get("c2paStatus", "absent"))` — placed beside the six keys already
forwarded the same way.** 🔴 **`ACTION KZ`'s VERIFICATION limb is NOT discharged: executing the
subject's own suite from inside its tree was refused this pass by the harness's external-code
policy, so the `53`/`53` claim is unproven and is not asserted.** 🔵 **`T298`: a diagnosis, a
specified one-line repair and an honest *"not verified"* is a better carry than a third consecutive
*"NOT ATTEMPTED"* — the next pass starts from a line number instead of a question.**

🆕 🟡 **A citation-hygiene note this pass owes itself:** 🟡 **p178 cited `generation/workflow.py:2515-2516`
and `:2520-2534`; the file is at `services/pipeline/src/alystria/generation/workflow.py` and the
function begins at `2492`.** 🔵 **Same pinned `HEAD`, so the drift is in the CITATION, not the
subject. Cite paths from the repository root or the next pass re-finds the file by hand.**

### 🟢 Pattern `7`, amendment — the institutional assessment stack gains a permissive base

🟢 **Pattern `7` wired `Artemis` + `dolos` + an institutional LMS and had to assume the LMS was
copyleft.** 🟢 **Replace the base with `OpenOLAT` (Pattern `20`, step `1`) and every link in the
chain is both code-verified AND permissive:** `Apache-2.0` → `MIT` → `MIT`. 🔵 **`4` of the
`17` routing rows in [`verticals/solutions.md`](../verticals/solutions.md) are code-verified, and
this chain uses three of them.**

### 🔴 What this pass did NOT verify

- 🔴 **`ACTION LB` — `dolos`'s `-i` as a function of template-to-submission ratio — NOT ATTEMPTED.**
  Carried to p181. 🔵 **Pattern `1` step `2` therefore keeps its CONDITION as written at p179 and
  gains no new evidence.**
- 🔴 **No subject repository was BUILT or RUN.** 🟢 Dependencies install; execution is
  policy-gated *(`T297`)*.
- 🔴 **`Selleo/mentingo` is still unread past its licence for a fourth pass** — the cheapest
  outstanding read on the shelf, and the only row claiming both `scorm` and `xapi`.

## Pass 179 — 2026-10-13

🆕 🟢 **`ACTION KW` is DISCHARGED after being carried unattempted through two passes, and it
AMENDS Pattern `1` at two steps — one of which Pattern `1` prescribed unconditionally and should
not have.** 🟢 **`dolos` has now been EXECUTED by this KB rather than read: `@dodona/dolos@2.9.3`
from npm, Node `v22.22.0`, two full runs over a `15`-file corpus of real `MIT` education code with
a ground truth this KB built itself.**

### 🟢 Pattern `1`, amendment `1` — step `4` finally has a NUMBER instead of a warning

p178's step `4` said: *"treat the report threshold as a per-dataset guess, never as a policy"* —
correct, and unusable, because a client has to pick one anyway.

| what was measured | similarity |
|---|---|
| 🟢 **every identifier renamed** *(the transform students actually perform)* | 🟢 **`1.0000`** |
| 🟢 renamed **and** top-level blocks reordered | 🟢 `0.9898` |
| 🔴 **honest sibling code** sharing a framework, an ORM, a test style and an author | 🔴 **`0.6720`** |

🟢 **So: identifier renaming does not work against `dolos` at all — it fingerprints the parse
tree.** 🔴 **And the false-positive surface is real and high: structurally similar honest work
reaches `0.6720`, with `1 307` tokens of overlap and a longest common fragment of `56`.**

🟢 **The usable number is the GAP: `0.3066`, empty.** 🔵 **Put the threshold in the empty band,
near `0.85`.** 🔴 **A `0.7` threshold — the round number every client reaches for — sits `0.028`
above the honest-work band and will flag honest work on the next, slightly more similar, pair.**
🟡 **This is a defensible sentence for an academic-integrity committee, and it is derived from a
corpus rather than asserted.**

### 🔴 Pattern `1`, amendment `2` — step `2`'s `-i` is CONDITIONAL, and it was prescribed as a rule

p178's step `2` said: *"supply the template before the first run: `dolos run -M 0.5 -i template.js`"*.
🔴 **Measured against four criteria fixed BEFORE the numbers were seen, template exclusion changed
NOTHING on this corpus:**

| criterion | result |
|---|---|
| top-`5` pair membership changes | 🔴 `False` — identical sets |
| a known positive moves `≥ 2` ranks | 🔴 `False` — all three moved `0` |
| median `|Δ similarity| ≥ 0.02` | 🔴 `False` — median **`0.00064`**, max `0.04515` |
| positive/negative separation changes sign | 🔴 `False` |

🔵 **`T284`, and this is the honest reading rather than the flattering one: `-i` can only matter
when the handed-out template is a LARGE FRACTION of the submission.** Here the template was `10`
shared `import` lines against modules of `2`–`63` KB, so the excluded fingerprints were
negligible.

🟢 **Pattern `1` keeps `-i`, and step `2` now carries the CONDITION:**

> **Supply `-i template` when the assignment is SCAFFOLDED** — a handed-out skeleton the student
> fills in, where the template is a double-digit percentage of the submitted file. 🔴 **For
> free-form assignments over a shared framework, `-i` buys a median `0.0006` and the step should
> not be sold as a control.** 🟢 **`-M <fraction>` (automatic common-code detection) is the
> control that does the work on an unscaffolded corpus, and it was already step `3`.**

### 🆕 🟢 Pattern `18` — taking an APPLIANCE to a cohort, which is the shape the new supply forces

🔵 **Why this pattern exists:** the two largest new permissive rows this pass read are
`MIT`, well-built, and have **no user**. 🔴 **`Bloom`: `7` tables, `16` write endpoints,
`docker-compose` — and `auth` `0`, `login` `0`, `jwt` `0`, `oauth` `0`, `users` `0`, `tenant` `0`,
no `User` entity.** 🟢 **One learner per deployment. The gap between that and a class of `30` is
an engagement, and it is a well-shaped one.**

**Components, every one licence-body read in this KB:**

| component | licence | role |
|---|---|---|
| [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) `HEAD b3918981bb34` | 🟢 `MIT`, `1 069` B, `md5 d3ac8ed0a50bd8de7d9c2ad5be4248ab` | the pedagogy and the data model you keep: `FastAPI` + `SQLAlchemy`, `7` entities, React `19` front end |
| [`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) **or** [`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) | 🟢 both `Apache-2.0` | 🟢 **BUY the identity layer, do not build it** — p136's standing finding, and `Bloom` is the case it was waiting for |
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 `MIT`, `1 091` B | the enrolment and `LTI 1.3` + AGS surface if the institution needs grade passback into its LMS |
| [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) `@2.9.3` | 🟢 `MIT`, `1 084` B | integrity, at the `0.85` threshold measured above — only if the appliance ever collects code |

| step | what you actually do | why, measured |
|---|---|---|
| `1` | **Read the manifest LAST.** Count import sites before scoping the auth work | 🔴 **`Bloom`'s `pyproject.toml` declares `python-jose[cryptography]`, `bcrypt`, `email-validator` and `python-multipart`. Import sites: `0`, `0`, `0`, `0`. A manifest-based estimate scopes this at zero and is wrong (`T285`)** |
| `2` | **Add the `User` entity and a tenant key to all `7` tables** — `courses`, `syllabi`, `lessons`, `annotations`, `feedbacks`, `learning_events`, `learning_recommendations` | 🔴 **Every one of them is currently single-tenant by omission, so this is a migration on the whole schema, not a new table** |
| `3` | **Put the bought OAuth broker in front of the `16` write endpoints** *(`12` `POST`, `1` `PUT`, `3` `DELETE`)* before anything else ships | 🔴 **Behind **P13**, mandatory: these endpoints write to the learner record with no identity today** |
| `4` | **Keep `SQLite` only through the pilot.** `docker-compose.yml` pins `DATABASE_URL=sqlite:///./data/bloom.db` on a named volume | 🟡 **Fine for one learner, wrong for a cohort — and the swap is cheap now and expensive after the migration in step `2`** |
| `5` | **Do NOT fork the LMS to reach the cohort.** Integrate over `LTI 1.3` — `Artemis` already ships it with AGS grade passback and a nightly Moodle interop test | 🔴 **The two biggest LMS options are `AGPL-3.0` (`openedx/edx-platform` `35 136` B, `instructure/canvas-lms` `34 520` B): a hosted fork inherits the disclosure obligation** |
| `6` | 🔴 **Budget the test suite as UNKNOWN, not as present.** `backend/tests/` has unit and integration directories | 🔴 **This KB could NOT run them: PyPI is unreachable from this environment (`uv sync` → `tunnel error`), so the suite is READ and not SEEN GREEN (`gap 139`, `ACTION LC`)** |

🟢 **Timeline shape:** the identity migration (steps `2`–`3`) is the critical path and it touches
every table; the `LTI` limb (step `5`) is parallelisable and well-specified; the pedagogy — the
part the client is actually buying — needs no work at all. 🔵 **That inversion is the pattern's
whole point: with this new supply, the differentiating logic is free and the plumbing is the
engagement.**

### 🟡 Pattern `19` — when the client's agent host is not decided, buy the ADAPTER shape

🔵 **[`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate)** *(`MIT`, `1 064` B,
`md5 5ebdff604182e1633fc88ea842500b97`, `HEAD 23387dbc4118`)* is not shelf-eligible as a product —
`0` databases, `0` web frameworks, `0` auth libraries. 🟢 **It is worth reading anyway, as a
reference architecture for a problem Globant clients have: `199` files of TypeScript and ESM that
run ONE skill set inside FOUR vendor runtimes — DeepSeek Harness (`cordis.patch.yml`,
`dsh-plugin.mjs`), Google Antigravity, OpenAI Codex and ChatGPT Work.**

| step | what you actually do |
|---|---|
| `1` | **Separate the skill CONTENT from the host ADAPTER in the repository layout from day one** — `Study-Mate` keeps `preset/`, `templates/` and `schemas/` away from `bin/*-plugin.mjs`, and that is why four hosts cost it one tree |
| `2` | **Write the adapter per host, never the skill per host.** A skill rewritten per runtime is the cost this pattern exists to avoid |
| `3` | **Treat the host as a swappable dependency in the contract**, because the author of a `925`★ project is betting it is |
| `4` | 🔴 **Do not promise state.** There is no persistence here at all; anything the client needs remembered across sessions is yours to build (see Pattern `18`) |

🟡 **Status, declared: `Study-Mate` was read past its licence (`ACTION KX`) but NOT run.** 🔵 **The
architecture claim above is from the file tree and the manifest; the behaviour is unverified.**

### 🔴 Still unexecuted in this file

- 🔴 **`ACTION KN` — the `76` grant-path probe lists — is carried a FOURTH pass**, and this pass
  it finally cost something real: `p117`'s name list lacks `COPYING.txt`, so
  [`moodle/moodle`](https://github.com/moodle/moodle) was published `NO-LICENCE-FILE` until the
  name was tried by hand. `p250`'s list carries it. 🔵 **A cosmetic debt that produces a false
  absence on the world's largest LMS is not cosmetic (`gap 135`).**
- 🔴 **`ACTION KZ` — propagating `c2paStatus` through `_artifact_provenance` — NOT ATTEMPTED.**
  Pattern `2`'s Article `50(2)` recipe therefore still rests on p178's `53`/`53`, with edit `4`
  reading its own default rather than the store.


## Pass 178 — 2026-10-13

🆕 🟢 **`gap 136` — the oldest live debt in this KB, carried for three passes — is CLOSED, and the
pattern it blocked is now the only compliance recipe here whose every step has been EXECUTED.**
🆕 🔴 **And the way it closed matters more than that it closed: the fix this KB prescribed for three
passes is UNEXECUTABLE as written.**

### 🆕 🟢 Pattern `2` — Article `50(2)` marking, MEASURED END TO END

🟢 **Subject, pinned:**
[`AkshitIreddy/AI-Powered-Video-Tutorial-Generator`](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator),
`MIT`, `9c260890214df68ad8fd0d681d3e77a6a7b7ea9f` — **still `HEAD` at a fifth consecutive pass**,
`905` files, `272` Python, `46` security tests.

🔴 **Step `0`, and nobody had hit it because nobody had run the suite: the project needs Python
`≥3.12`.** `src/alystria/providers/types.py:414` declares `class ProviderResult[T]`, PEP `695`
generic syntax. 🔴 **On this environment's default `python3` (`3.11.17`) the security suite cannot
even IMPORT — `37` tests run, `1` import error, `10` tests never collected.** 🟢 **Under
`/usr/bin/python3.13` it is `46`/`46` GREEN.** 🔵 **Record the interpreter next to the test count or
the number means nothing. p175 and p176 both published *"`46` security tests"* without one.**

| stage | result | note |
|---|---|---|
| pristine, `python3.11` | 🔴 **`37` run, `1` import ERROR** | PEP `695` syntax — environmental, not a defect |
| pristine, `python3.13` | 🟢 **`46`/`46` GREEN** | 🟢 **first reproduction of this baseline in this KB** |
| + edits `1`+`2` | 🔴 **`2` errors, exactly the `2` PREDICTED** | `test_apache_two_generated_asset_allows_transformed_commercial_export`, `test_mit_starter_audio_allows_transformed_commercial_export` |
| + the PRESCRIBED test fix | 🔴 **STILL `2` errors — the prescription is WRONG** | `ValidationError: valid C2PA records require a hash, signer, and verification time` |
| + the CORRECTED test fix | 🟢 **`46`/`46` GREEN** | `C2paRecord(C2paStatus.VALID, HASH, "Alystria", NOW)` |
| + edit `4` + `7` new real-record tests | 🟢 **`53`/`53` GREEN** | the whole patch, exercised |

🔴 **Why the prescription could not work, and it is a self-inflicted error this KB had the facts to
avoid:** `ACTION KI`/`ACTION KR` prescribed *"pass `c2pa=C2paRecord(C2paStatus.VALID)` in the two
`GENERATED` test constructions"*. 🔴 **`C2paRecord.__post_init__` (`provenance.py:52-60`) raises
unless a `VALID` record also carries `manifest_sha256`, `signer` AND `verified_at`.**
🔵 **p174 ALREADY recorded that constraint — *"`C2paRecord` structurally requires a `signer` for
`VALID` (`provenance.py:55-60`)"* — and called the certificate the only procurement line item. Two
published facts in the same file contradicted each other for three passes because nobody executed
either (`T282`'s sibling: a prescription repeated is not a prescription tested).**
🟢 **The corrected fix is still `2` insertions and it reaches `46`/`46`.**

🔴 **And the compliance consequence of that constraint, which is the real finding for a client:
after edits `1`+`2` there is NO status a `GENERATED` asset can carry that passes the export gate
without a signing certificate.** `NOT_APPLICABLE` is refused by edit `1`; `ABSENT` and `INVALID` are
refused by the gate; `VALID` is structurally impossible without `manifest_sha256` + `signer` +
`verified_at`. 🔵 **So p176's *"no certificate, no external tool, no fifth file — the cheapest
compliance movement available anywhere on this shelf"* is WRONG for generated assets. The metadata
half is cheap; the moment the gate refuses `NOT_APPLICABLE`, the certificate moves from Step `C`
onto the critical path. Price it at the start of the engagement, not at the end.**

#### 🆕 🔴 Two NEW defects, found by running a real record instead of reading the code

🟢 **The record used is not invented: its key names are the ones `_provenance_quality_gate` reads,
and its shape is the dict `_artifact_provenance` returns.**

| # | defect | evidence | consequence |
|---|---|---|---|
| 🆕 🔴 **`1`** | **the builder never carries the field the gate needs** | `_artifact_provenance` (`generation/workflow.py:2520-2534`) is the ONLY producer of the `provenanceRecords` list, and its returned dict has **no `c2paStatus` key** | 🔴 **edit `4` reads its own DEFAULT (`"absent"`), not the store. `gap 136`'s *"nothing exports"* claim HOLDS — but the mechanism is a missing field, not a refused value. 🔵 Worse, because it is silent** |
| 🆕 🔴 **`2`** | **`origin` is written in a spelling the enum does not have** | `licensed_media_workflow.py:259`/`:290` and `music_workflow.py:159`/`:301` store `"origin": "licensedMedia"`; `OriginKind` spells it `"licensed-media"`; `workflow.py:2515-2516` rewrites anything unrecognised to `GENERATED` | 🔴 **every licensed stock asset reaches the gate labelled GENERATED. So edit `1` refuses LICENSED MEDIA, not just synthetic media — a blast radius p176 did not predict** |

🟢 **Both are asserted as tests, not as prose:**
[`compose/code/p178-real-record-gate/test_p178_real_record_marking.py`](code/p178-real-record-gate/test_p178_real_record_marking.py)
— `7` tests, all passing, including the CONTROL that an unpatched reader lets an unmarked record
through a gate that requires marking. 🔵 **That control is the test the project does not have, and
patterns.md has been asking for it since p174.**
🟢 **The patch as a diff:**
[`aiact-50-2-edits-1-2-4.p178.patch`](code/p178-real-record-gate/aiact-50-2-edits-1-2-4.p178.patch)
— `79` lines; `7` insertions in `provenance.py`, `5` changed in `gates.py`, `1` in
`generation/workflow.py`, `2` in the test file.
🟢 **Ledgers:**
[`evidence/aiact-50-2-green.2026-10-13-p178.tsv`](../evidence/aiact-50-2-green.2026-10-13-p178.tsv)
and
[`evidence/aiact-50-2-real-record.2026-10-13-p178.tsv`](../evidence/aiact-50-2-real-record.2026-10-13-p178.tsv).
🔴 **Nothing was reported upstream and nothing should be from an unattended pass. The diff is here
for a human to take.**

#### 🟢 The build order for a client, with what each step now costs

| step | effort | buys | measured? |
|---|---|---|---|
| `1` — honour the stored status *(edit `4`)* | 🟢 **`1` line** | the gate stops being fed a constant | 🟢 **YES — and it exposes defect `1`: the field is never propagated** |
| `2` — propagate `c2paStatus` through `_artifact_provenance` | 🟡 **`1`–`2` lines, UNMEASURED** | the gate reads the STORE instead of a default | 🔴 **NO — `ACTION KZ`** |
| `3` — fail closed on synthetic origin *(edits `1`+`2`)* | 🟢 **`12` insertions** | `GENERATED` can no longer self-exempt | 🟢 **YES — `2` predicted breaks, both fixed in `2` insertions** |
| `4` — fix the `origin` spelling in the two writers | 🟡 **`4` lines, UNMEASURED** | licensed media stops being relabelled `GENERATED` | 🔴 **NO — and until it is done, step `3` refuses stock photos** |
| `5` — procure a signing certificate | 🔴 **procurement, not engineering** | 🔴 **the ONLY way a `GENERATED` asset exports at all after step `3`** | 🟢 **the necessity is now MEASURED, not inferred** |
| `6` — thread `c2patool` from `native_controls.py:1113` | 🟡 **`5` files + a test** | the VISIBLE marking duty | 🔴 **NO — insertion point known (`editor_export.py`, after `:885`, BEFORE `:907`)** |

🔵 **Sequence note that survives every date conflict: steps `1`–`4` are code and can ship inside a
normal engagement; step `5` is a purchase order with a lead time; step `6` is the only part that
touches the encoder. Marking is a `2026` duty, Annex III conformity is a `2027` roadmap
([`intel/trends.md`](../intel/trends.md)).**

### 🆕 🟢 Pattern `7` — the institutional assessment stack, every link code-verified

🔵 **New this pass because `ACTION KT` made it possible: for the first time this KB can hand a
university a topology in which every component has been read past its licence, and name what each
one does NOT do.**

| layer | component | licence · pin | why this one |
|---|---|---|---|
| LMS of record | [`moodle/moodle`](https://github.com/moodle/moodle) *(or [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) for permissive)* | 🔴 `GPL-3.0` *(at `COPYING.txt`)* · 🟢 `Apache-2.0` | the institution almost always already has one; `Moodle` is the LMS `Artemis` is nightly-tested against |
| exercises, exams, grading | 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`**, `1 091` B · pin `develop@8c158741c38e`, `v10.3` | `257` JPA entities, `528` write endpoints, own auth, `LTI 1.3` tool with Deep Linking + AGS |
| the wire between them | `LTI 1.3` + **AGS** | — | `Lti13Configurer` `27`, `Lti13AgsClaim` `9`, `ags` `305`, `DeepLinking` `60`, **`NightlyLtiMoodleInteropTest` in CI** — grades flow BACK, which is the limb that usually fails in integrations |
| AI authoring | 🟢 **`Hyperion`, inside `Artemis`** | — | verified variant generation *(programming variants built, quiz variants validity-checked)*, MCQ generation, consistency checks. 🟢 **needs Spring AI + an LLM endpoint only** |
| AI tutoring / lecture search | 🟡 [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris) | 🟡 **`MIT`**, `1 089` B · pin `d7b2c095204e` | 🔴 **`12`★, `16` open issues — OPTIONAL. Deploy only if semantic lecture search is in scope** |
| integrity | 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`**, `1 084` B · pin `44925b867ce7` | `20` languages, `19` vendored grammars; 🟢 **returns NO verdict, which is what keeps it outside Annex III** |
| SCORM / xAPI, if contractual | 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | 🔴 **`Artemis` declares `SCORM` `0` and `xAPI` `0`. This row is not optional if the contract names them** |
| rostering | 🟢 [`edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) *(read)* / [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) *(Canvas read+write)* | 🟢 `Apache-2.0` / 🟢 `MIT` | 🔴 **`Artemis` has `OneRoster` `0` and `Ed-Fi` `0`; enrolment is a separate integration, always** |
| local inference, where sovereignty requires | `ollama` + `weaviate` | — | 🟡 **the path EXISTS — `ollama` in the Iris test stack and the Weaviate global-search config — and it is NOT the paved road: `spring.ai.openai` has `7` config keys, `spring.ai.model` has `1`** |

🔴 **Wiring order, because the usual mistake is to start with the AI:**
**(`1`)** stand `Artemis` up from `deployment/docker/docker-compose.yml` on a PINNED sha — `develop`
moved during the hour this pass ran; **(`2`)** register it as an `LTI 1.3` tool in the LMS and prove
Deep Linking + a grade round-trip through AGS *before* any AI work — this is the limb with a nightly
test to copy from; **(`3`)** turn on `Hyperion` with an LLM endpoint and NO `Pyris`; **(`4`)** add
`dolos` as a separate service and keep it non-adjudicating — a human reads the clusters;
**(`5`)** add `scorm-again` and the rostering layer only if the contract names them;
**(`6`)** decide the inference location LAST, because it is the only choice the architecture does
not force.
🔴 **The four conditions, carried verbatim into any deck:** `Artemis` **adjudicates** and is
therefore an Annex III stand-alone high-risk system in the EU *(`2` December `2027`)*; it speaks
**ONE standard**; it names **`FERPA` nowhere**, so a US deployment inherits that work; and its
**self-hosted AI limb rests on a `12`★ microservice**.
🟢 **What it buys that nothing else in this KB does: `proctor` `0`, `webcam` `0`, `emotion` `0`.
The Article `5` prohibition on emotion recognition is cleared ARCHITECTURALLY, and that is a
property you cannot retrofit onto a proctoring vendor.**

### 🆕 🟢 Pattern `8` — the instrument-adoption gate, generalised for client platform teams

🔵 **This pass found that a correct primitive had sat unused in this repository's own library for
`103` passes while `10` instruments kept the broken idiom
([`intel/trends.md`](../intel/trends.md), `T280`). The pattern is the remedy, and it transfers
directly to any client with a platform team.**

| step | here | at a client |
|---|---|---|
| `1` — name the defect as a CLASS, not an incident | `P834`: a command substitution strips the whole trailing newline run | *"which of our measurements round-trip through a shell variable?"* |
| `2` — ship the correct primitive | `size_of_file` in `lib/payload_measure.sh` | the shared helper, in the shared place |
| `3` — keep the BROKEN form as a named control | `size_of_capture_BROKEN`, with *"never use this to publish a figure"* | the anti-pattern, executable, so the suite can assert the divergence |
| 🆕 **`4` — make the absence FAIL** | [`check_channel.sh`](code/p178-byte-channel-census/check_channel.sh): exits `1` on any unmarked stripping site; `6`/`6` on its own suite | 🔵 **the step everyone skips. Steps `1`–`3` are documentation; step `4` is the control** |
| 🆕 **`5` — allowlist deliberate controls, and say why in the source** | `2` controls, plus this gate's own test fixture — 🟢 **which the gate caught on its first run** | a gate that cannot be allowlisted gets disabled; one that logs its exceptions stays on |

🟢 **Measured result: `12` findings in `12` files across `10` instruments, `0` false positives after the
comment-line filter, `6`/`6` suite including the `0`/`1`/`3` trailing-newline control.**
🔴 **Honest state: the gate makes the debt visible and does NOT repair it — `0` of the `12` sites were
repaired this pass. `ACTION KY` takes all `12`, and one of them (`p324`, which pipes the body through `head` before counting)
may not accept the mechanical swap.**

## Pass 177 — 2026-10-13

🟢 **Five patterns. Patterns `1`–`3` are buildable today from rows this KB has now read past their
licences; pattern `4` is the method that produced them, with the two traps that fired while it ran;
pattern `5` is the region where the components must be imported and says so.**

### 🆕 🟢 Pattern `1` — assessment integrity, with a VERIFIED detector and its wiring cost named

🔵 **Components, both `MIT`, both licence-body read:**
[`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) at `HEAD` `44925b867ce7` *(`1 084` B,
`md5 00ffc342d555c4129ee54e3286818d50`)* — 🟢 **read past its licence at p177, `ACTION KQ`** — plus
[`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) at `513588f3077f` for rostering if the
institution runs Canvas.

| step | what you actually do | why, measured |
|---|---|---|
| `1` | **Pick the tokenizer by extension, from the registry — not from the docs page.** `20` languages ship: `bash c cpp c-sharp python php modelica ocaml java javascript elm go groovy r rust scala sql typescript tsx verilog`, with `19` vendored `tree-sitter` grammars | 🔴 **`docs/about/languages.md` lists `11` and trails off. Quoting the docs undersells the tool by `9` languages, `Modelica`, `Verilog`, `R`, `Scala`, `Groovy` and `OCaml` among them — which is exactly the set an engineering faculty needs** |
| `2` | **Supply the template before the first run:** `dolos run -M 0.5 -i template.js solutions/*.js` | 🔴 **`options.ts:54` sets `defaultMinSimilarity = 0`: an unconfigured run filters NOTHING, and the docs themselves warn the shared scaffolding will dominate the similarity score** |
| `3` | **Add automatic common-code detection:** `-m <int>` *(max files a fragment may appear in)* or `-M <fraction>`; combinable with `-i` | 🟢 **These three controls ARE the false-positive story — `falsePositive` and `confidence` appear `0` times in `513` files** |
| `4` | **Treat the report threshold as a per-dataset guess, never as a policy.** `guessSimilarityThreshold` in `web/src/api/utils/cutoff.ts` takes a local minimum and floors it at the mean of pairwise similarities; `SingleLinkageClustering` drops edges below it | 🔴 **It moves with the cohort. A client who hears *"the threshold"* will think it is a standard they can cite in an appeal** |
| `5` | **Budget the LMS wiring as custom work.** `Moodle` `0`, `webhook` `0`, Canvas LMS `0` | 🔴 **The `29` `canvas` hits are the HTML5 element and `D3` rendering. There is NO LMS integration — `Dodona` (`193` hits) is the one platform it is built for** |
| `6` | **Deploy from the shipped images:** `Dockerfile.cli`, `Dockerfile.web`, `docker-compose.yml` | 🟢 **CLI for batch, web for the report** |
| `7` | **Name the student side in the same meeting.** [`sgaofen/vibe-schooling`](https://github.com/sgaofen/vibe-schooling) *(`MIT`, `1 064` B, `80`★)* — Canvas named `19`×, topics `canvas-lms` + `exam-automation` | 🔴 **The attack is browser and MCP automation against a live LMS; the defence is batch similarity over submitted code. 🔵 They do not operate on the same surface, so integrity has to be designed into the ASSESSMENT SHAPE — oral defence, process evidence, in-session artefacts** |

🔴 **What this pattern does NOT buy:** `0` interop standards (`OneRoster`, `Ed-Fi`, `SCORM`, `xAPI`,
`Caliper`, `LTI`, `QTI` all `0`) and `0` mentions of `FERPA` or `GDPR`. 🔵 **The data-protection
story is the integrator's to write, and in EMEA it is the deliverable.**

### 🆕 🟢 Pattern `2` — sequencing an EU education engagement against TWO clocks, not one

🔴 **The mistake this pattern exists to prevent: being told *"education is high-risk under the AI
Act, act now"*, which is true about classification and wrong about timing by `14` months.**

| duty | applies from | what you build, in this engagement |
|---|---|---|
| 🔴 **Article `50` transparency** | **`2` August `2026`** — in force | disclosure in the tutoring and authoring surfaces |
| 🔴 **Article `50(2)` marking of synthetic content** | **`2` December `2026`** — 🔴 **`50` days** | 🟢 **p176's MEASURED patch, below** |
| 🟡 **Annex III stand-alone high-risk** *(access, progression, assessment, exam scoring — where education sits)* | 🟡 **`2` December `2027`** *(Digital Omnibus)* | conformity-assessment roadmap, not code |
| 🟡 **Annex I embedded** | 🟡 **`2` August `2028`** | out of scope for most education work |

🟢 **So the marking work is the only part with a deadline inside a normal engagement, and it is
already specified against a named repository at named lines** —
[`AkshitIreddy/AI-Powered-Video-Tutorial-Generator`](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator),
`MIT`, pinned `9c260890214df68ad8fd0d681d3e77a6a7b7ea9f`: edit `1` in `security/provenance.py`,
edit `2` in `security/gates.py`, edit `4` the one-liner at `generation/workflow.py:3018`.
🔴 **Carry p176's two warnings with it or the patch misleads:** the suite goes `2`/`46` red on edits
`1`+`2` *(fix: pass `c2pa=C2paRecord(C2paStatus.VALID)` in the two `GENERATED` test
constructions)*, and the one-line edit `4` passes `46`/`46` **because `0` tests reference the field
at all** — 🔴 **all three writers store `"absent"`, which the export gate refuses, so the correct
repair turns the gate RED on every real asset. That is the right compliance position and a breaking
change on the same line.**
🔴 **Every date here is search-layer secondary — `eur-lex` and `digital-strategy.ec.europa.eu` are
NXDOMAIN from this environment (`gap 110`), and sources conflict on the Omnibus's operative status
and on whether `50(2)` is `2` December `2026` or `2` February `2027`.** 🔵 **Sequence work against
this table; put a date in a contract only on counsel.**

### 🆕 🟢 Pattern `3` — the non-adjudicating architecture, because it is the only one that clears both regimes

🔵 **The rule: keep the EVIDENCE inside the system and push the JUDGEMENT outside it.**

| layer | component | licence | what it must NOT do |
|---|---|---|---|
| rostering | [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) *(Canvas institutions)* or [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) *(standards-native, read-only)* | `MIT` / `Apache-2.0` | 🔴 **never write a grade back automatically** |
| integrity evidence | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | `MIT` | 🟢 **it structurally cannot adjudicate — no `confidence`, no verdict, `0` pass/fail in `513` files** |
| delivery | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) *(`SCORM` in AND out)* or [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) *(`QTI`, `SCORM`, `Apache-2.0`)* | `MIT` / `Apache-2.0` | 🔴 **no automated progression decision** |
| decision | 🟢 **a human review queue — the deliverable, not the gap** | — | 🔴 **no auto-escalation, no auto-sanction** |

🟢 **Why this is commercial and not merely ethical, in two regions at once:** Annex III attaches
high-risk status to systems that *determine* access, progression or assessment, and **Oklahoma and
Maryland bar AI from high-stakes decisions about students while requiring human oversight.**
🔵 **The same architectural property — no verdict — keeps the build out of the EU's high-risk class
AND inside what two US states permit at all.** 🔴 **Invert it and you buy a conformity assessment,
a prohibition, and an appeals process (`T277`).**

### 🆕 🟢 Pattern `4` — read a repository past its licence, with the two traps that fired doing it

🔵 **The recipe that produced `ACTION KQ`, written down because both of its failure modes are
seductive:**

| step | do this | the trap |
|---|---|---|
| `1` | **Clone at the `HEAD` you already recorded**, `git clone --depth 1 --single-branch`, and re-assert the sha | 🟢 **`dolos` was `44925b867ce7` at p175 and p177 — a controlled read, not a fresh one** |
| `2` | **Name the artefact that would have to exist, then look for THAT** *(`T265`)* | 🔴 **not the standard's name. `canvasapi` names `LTI` `7` times and implements `0` standards** |
| `3` | **Grep the WHOLE repository, never a subset** | 🔴 **`ACTION KQ`'s first probe searched `lib/`, `cli/`, `docs/` and was about to publish *"`threshold` `0`"* and *"`cluster` `0`"*. True counts: `16` and `178`. 🔵 A scope-limited grep reports its scope, and it fails in the flattering direction (`T276`)** |
| `4` | **Disambiguate every token before reporting it** | 🔴 **`canvas` matched `29` times in `dolos` and `0` were Canvas LMS — every hit was the HTML5 element or `D3`. Check `Canvas LMS`/`canvas-lms`/`instructure` separately (`T265`)** |
| `5` | **Quote `md5`, not a byte count, as the identity of a licence** | 🔴 **`8` of `12` byte counts in this KB are short by exactly `1` — a trailing `LF` the reading channel drops. `md5` reproduced exactly on independent reads (`T275`)** |
| `6` | **Enumerate branches before trusting a branch label** | 🔴 **`raw` serves `master` as an alias to the default branch where no `master` exists, `200` and byte-identical; it does NOT do the reverse (`T273`, `ACTION KO`)** |

### 🆕 🟡 Pattern `5` — LATAM: import the components, sell the governance

🔴 **Stated plainly because it is the eleventh pass it has been true: there is `0` LATAM-originated
open-source education supply in this KB.** 🟢 **The demand evidence, by contrast, is the best this KB
holds anywhere — UNESCO IESALC with UNU-IAS across `200` institutions in `19` countries.**

| finding | figure | what it means for the build |
|---|---|---|
| 🟢 adoption | **`87%`** use AI in ≥`1` area; **`74%`** in teaching and learning | the pilot phase is over |
| 🔴 governance | 🔴 **`26%`** have a formal AI strategy | 🟢 **the engagement is the policy layer, not the model layer** |
| 🟢 operator precedent | Uruguay's **Ceibal: `75%`** of public-school teachers using AI tools | a national reference to design against |
| 🟢 K-12 demand | Brazil **`56%`** of secondary teachers *(TALIS `2024`)* vs OECD **`36%`** | teacher-facing, not student-facing, is the wedge |
| 🟡 regulation | Brazil PL `2.338/2023` in the Chamber; Chile risk-based bill; Colombia CONPES `4144` to `2030` | 🔴 **nothing in force — design to the EU's shape and you are ahead of all three** |

🟢 **The stack:** [`Kolibri`](https://github.com/learningequality/kolibri) (`MIT`, offline-first) as
the spine for low-connectivity deployment, [`Selleo/mentingo`](https://github.com/Selleo/mentingo)
(`MIT`, `SCORM` both directions) where connectivity allows, and Pattern `3`'s non-adjudicating
architecture as the governance artefact the `74%`-adopting, `26%`-strategy institution actually
needs. 🔵 **Localisation into Spanish and Portuguese and the governance deliverable are the value
added. There is no local open-source leverage to claim, and claiming it would be the one thing this
file has never done.**


## Pass 176 — 2026-10-13

🟢 **Five patterns. Pattern `1` is REFINED by a measurement; patterns `2`–`5` are new, and every one
of them names the repositories, the licences and the wiring rather than a capability.**

### 🆕 🟢 Pattern `1` — Article `50(2)` marking on a permissive video pipeline, MEASURED

🔵 **Component:** [`AkshitIreddy/AI-Powered-Video-Tutorial-Generator`](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator),
`MIT`, pinned at `9c260890214df68ad8fd0d681d3e77a6a7b7ea9f` — **still `HEAD` at a fourth consecutive
controlled re-read**. `905` files, `272` Python, `46` security tests.
🟢 **p175 specified this patch and labelled its effect a PREDICTION. p176 ran it. The prediction was
right to the test name, so the recipe below is measured, not proposed.**

| step | file and line | edit | measured effect |
|---|---|---|---|
| `1` | `security/provenance.py`, after the provider/model/revision clause *(line `143`)* | refuse `C2paStatus.NOT_APPLICABLE` when `origin == GENERATED`, in `AssetProvenance.__post_init__` | **`7` insertions** |
| `2` | `security/gates.py`, the accepted-status set *(lines `260`–`262`)* + `OriginKind` added to the import at line `11` | accepted set becomes `{VALID}`, plus `NOT_APPLICABLE` only when origin is not `GENERATED` | **`5` insertions / `5` deletions** |
| `4` | `generation/workflow.py:3018` | 🟢 **read `value.get("c2paStatus")` instead of hardcoding `C2paRecord(C2paStatus.NOT_APPLICABLE)`** — the gate already reads twelve other fields off the same record | **`5` insertions / `1` deletion** |

🟢 **Run it on `python3.12` with stdlib `unittest`, `PIL` stubbed, and `sys.path` set INSIDE a runner
script — not via `PYTHONPATH`, because `python3 -I` ignores the environment (`T271`).**

| stage | result |
|---|---|
| pristine | 🟢 **`46`/`46`** |
| edits `1`+`2` | 🔴 **`2` errors**: `test_apache_two_generated_asset_allows_transformed_commercial_export`, `test_mit_starter_audio_allows_transformed_commercial_export` |
| edit `4` alone | 🟢 **`46`/`46`** |
| `1`+`2`+`4` | 🔴 **the same `2`** |

🟢 **How to fix the two breakages, concretely:** both are `GENERATED`-asset constructions that pass
no `c2pa=` keyword, so they inherit the `NOT_APPLICABLE` default that edit `1` now refuses. **Pass
`c2pa=C2paRecord(C2paStatus.VALID)` in those two test constructions.** 🔵 **`0` tests in the
repository pass a `c2pa=` kwarg today, so there is no existing convention to match — you are
establishing it.**
🔴 **The production consequence, which is the part that belongs in the statement of work rather than
the pull request:** all three writers store `"absent"`, `C2paStatus("absent")` is `ABSENT`, and
`ABSENT` is what the gate refuses. **After edit `4`, nothing exports until a signing certificate
exists.** 🟢 **That is correct behaviour `50` days out, and it has to be scoped as procurement plus
code, never as code alone (`gap 136`).**

### 🆕 🟢 Pattern `2` — the Canvas-institution stack, with its own threat model wired in

🔵 **For the engagement shape this KB sees most: an institution already running Canvas that wants AI
on top without replacing the system of record.** 🟢 **Every component is `MIT`.**

| layer | component | licence | wiring |
|---|---|---|---|
| roster + sections | [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 `MIT`, `1 130` B | `Canvas(base_url, token)` → `course.get_enrollments()`, `course.get_sections()`, `account.get_enrollment_terms()`. `Bearer` auth, `per_page=100` pagination that follows the next link, `RateLimitExceeded` to back off on. 🟡 **`sis_section_id:`/`sis_course_id:` prefixes address objects by the SIS's own ids — use them as the join key, not Canvas's internal ids** |
| integrity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 `MIT`, `1 083` B | run as a BATCH over each assignment's submissions pulled through `canvasapi`; key reports by the `sis_*` id so results survive a Canvas re-import |
| content interop | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | wrap third-party `SCORM`/`AICC`/`xAPI` packages so Canvas's own player is not the constraint |
| credentials | [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 `MIT`, `1 080` B | issue **Open Badges `3.0`** on completion. 🔴 `OpenOLAT`'s badge module is `OB2` only — do not pair those two and expect W3C VCs |
| 🔴 **threat model** | 🔴 [`sgaofen/vibe-schooling`](https://github.com/sgaofen/vibe-schooling) | 🟢 `MIT`, `1 063` B | 🔴 **NOT a dependency. Read it to see what the student side automates against Canvas quizzes — `canvas-lms` + `exam-automation`, `80`★ — and test the assessment design against it** |

🔴 **The condition that must appear on the slide: `canvasapi` is `MIT`, Canvas is not.** Instructure
publishes the core under `AGPL-3.0` and sells the operated product, so this stack is permissive
**around** a non-permissive system of record.
🔴 **And `0` word-boundary matches for OneRoster, Ed-Fi, SCORM, xAPI or Caliper inside `canvasapi`:
it speaks Canvas's API, not a standard.** 🟢 **If the client needs standards-native rostering
instead, the route is [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster)
(`Apache-2.0`) — `OneRoster 1.2`, `24` GETs, `0` writes.** 🔵 **Pick by which you need: writes, or
portability. No permissive row here gives both.**

### 🆕 🟢 Pattern `3` — adaptive tutoring with a real prerequisite graph underneath it

🔴 **The hole this closes: every adaptive-tutoring recipe in this KB has had a tutor and a scheduler
and no DEPENDENCY GRAPH — the thing that says which objective unlocks which.**

| layer | component | licence | wiring |
|---|---|---|---|
| 🆕 prerequisite graph | [`wwlwgo/cn-primary-math-knowledge-graph`](https://github.com/wwlwgo/cn-primary-math-knowledge-graph) | 🟢 `MIT`, `1 117` B, `113` files | a JSON-schema'd micro-objective dependency dataset. Load as the DAG; topologically sort to get the next unlocked objective |
| tutoring | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 `MIT` | drives the session; take the next objective from the DAG rather than from the model's judgement |
| spaced repetition | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🟢 `MIT` | schedule review of MASTERED objectives over MCP, keyed by objective id |
| 🆕 item generation, verified | [`Scorpioyyy/verichalk`](https://github.com/Scorpioyyy/verichalk) | 🟢 `MIT`, `1 066` B, `4 198` files | generate practice items for an objective and verify each one three ways — solver, blind re-solve, curriculum-boundary check — before it reaches a learner |

🔵 **Why the pairing is more than a list: the graph and the generator are grounded in the SAME
national curriculum, so objective ids and item scope agree without a mapping layer.**
🔴 **Limits, stated: both new rows are APAC-curriculum-specific, `7`★ and `6`★, licence-verified and
nothing else. Coverage, accuracy and item quality are UNMEASURED.** 🟢 **Treat the pattern as the
SHAPE to build and these two as the reference implementations to read, not to ship.**

### 🆕 🟢 Pattern `4` — grading an inherited codebase's test suite without grading your own argv

🔵 **Reusable on any client codebase, and p176 learned it the expensive way on its own.**
🔴 **Running `665` scripts in this repository with `python3 -I` reported `36` test files CRASHING.
`35` of those `36` pass without the flag.** `-I` implies `-P` from Python `3.11`, so the script's
own directory is NOT placed on `sys.path` — and every test that imports the module beside it raises
`ModuleNotFoundError`.
🟢 **The recipe:**
1. Run every script from inside its own directory, with a timeout, recording the **exit code**.
2. Run the whole sweep **twice** — isolated and non-isolated — and report both rates. A rate from
   one invocation is a statement about that invocation.
3. Classify every non-zero exit by what the script PRINTED, and separate *"wanted an argument"* and
   *"the network is denied here"* from *"it disagrees with the repository"* and *"it cannot execute"*.
4. 🔴 **Expect the classifier to be wrong first.** p176's first iteration left `88` exits unnamed;
   a second iteration named `36` of them — `35` shell scripts refusing a missing `$1`, and `4` suites
   reporting their own score in prose (*"`7`/`10` controls passed"*) that no `FAILED`-matching rule
   could see. 🔵 **A third class remains: a usage line in SPANISH (`uso:`), which an English-only
   cue list cannot find.**
5. Restore the tree to `HEAD` afterwards, unconditionally — **`11` committed files in `7`
   instruments were rewritten by the sweep**, plus `2` created.
🟢 **Instrument: [`compose/code/p176-suite-exit-sweep/`](compose/code/p176-suite-exit-sweep).**

### 🆕 🟢 Pattern `5` — one grant-path vocabulary instead of seventy-six

🔴 **The defect, measured: `76` independent hardcoded grant-path probe lists in this repository.
`48` carry the British `LICENCE`. `3` carry `COPYING.md`.** 🔵 **So *"extend the probe list"* is not
an edit, it is a migration across `76` call sites (`T272`).**
🟢 **The recipe, and it is deliberately boring:** put ONE ordered path vocabulary in
`compose/code/lib/`, import it, and make the absence claim name the vocabulary VERSION it was
reached with. 🟢 **Then an absence claim is falsifiable: *"`0` of `16` paths, vocabulary `v1`"* can
be re-run when the vocabulary grows; *"no grant file"* cannot.**
🟢 **And the stronger test, when the tree is small enough to afford it: ENUMERATE instead of
probing.** `ACTION KJ` settled a shelf row by listing **all `5` branches** of
`JushBJJ/Mr.-Ranedeer-AI-Tutor` — `55` file-paths, `0` grant-shaped at any case — which is a claim
no longer path-list-dependent at all. 🔵 **Probe when you must; enumerate when you can; and say
which one you did.**
🟢 **Instrument: [`compose/code/p176-grant-path-vocabulary/`](compose/code/p176-grant-path-vocabulary).**

## Pass 175 — 2026-10-13

🆕 🟢 **p174's headline recipe gets CHEAPER and p174's headline count gets CORRECTED, in the same
pass and for the same reason: `ACTION KH` wrote the patch instead of specifying it.**
🔴 **The correction first, because a client reads the number: *"four edits"* is wrong as published.**
Edit `3` cannot be made in four files — the signer path has to come from
`native_controls.py:1113`, a FIFTH file — unless it is given a default of `None`, which keeps the
count at four and makes the marking step inert unless a caller opts in. 🔵 **That is `T258`'s own
defect reproduced by the fix for it: a compliance step nothing sets.**
🆕 🟢 **The improvement second, and it is larger than the correction: edit `4` needs no signer, no
`c2patool` and no certificate.** The project already stores a real `c2paStatus` and its export
quality gate throws it away.

### 🆕 🟢 Pattern 1 — Article `50(2)` and China's Art. `5`: the ONE-LINE half, and the procurement half

🔵 **Subject:** [`AkshitIreddy/AI-Powered-Video-Tutorial-Generator`](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator)
`MIT`, pinned at `9c260890214d` — **still `HEAD` at p175**, so this is a third controlled re-read of
the same `905` files.
🔵 **Why this row:** it is the most provenance-literate project on the shelf, and the thing it
generates — synthetic video with a presenter voice — is in scope of **both** the EU's Art. `50(2)`
marking backstop (`2 Dec 2026`) and China's Art. `4` explicit and Art. `5` implicit labelling duties
(live since `1 Sep 2025`).

#### 🟢 Step A — the metadata duty, in ONE line, for free

🟢 **The finding that makes this cheap.** The project's own generated schema registry lists
`c2paStatus` as a **REQUIRED** property of `AssetProvenance`. Three writers set it:
`licensed_media_workflow.py:259`, `licensed_media_workflow.py:290` and `project_assets.py:246` all
write `"absent"`, and `visual_candidates.py:276` and `:611` read it with `"absent"` as the default.
🔴 **Then `_provenance_quality_gate` (`generation/workflow.py:2979`) reads TWELVE fields off each
stored provenance record — `assetId`, `sha256`, `origin`, `rightsStatus`, `licenseId`, `creator`,
`attribution`, `sourceUri`, `providerId`, `modelId`, `modelRevision`, `consentIds` — and DISCARDS
the thirteenth, hardcoding `C2paRecord(C2paStatus.NOT_APPLICABLE)` at line `3018`.**

| status the pipeline stores | status the gate is handed | what the gate does with `c2pa_required=True` |
|---|---|---|
| 🟢 `"absent"` | 🔴 **`NOT_APPLICABLE`** | 🔴 **passes — the finding is laundered away** |
| 🟢 `"absent"` | 🟢 **`ABSENT`** *(after the fix)* | 🟢 **fires `['export.c2pa']`** |

🟢 **The edit:**

```python
# generation/workflow.py:3018 — before
                    c2pa=C2paRecord(C2paStatus.NOT_APPLICABLE),
# after
                    c2pa=C2paRecord(C2paStatus(str(value.get("c2paStatus", "absent")))),
```

🔵 **`T269` — the defect is DATA LOSS, not a missing control.** `ABSENT` is the one status that makes
the gate fire and `NOT_APPLICABLE` is the one that makes it pass; the code reads the first and writes
the second. 🟢 **No certificate, no external tool, no fifth file. This is the cheapest compliance
movement available anywhere on this shelf.**
🔴 **And the diligence question it generalises into, for any pipeline a client brings:** *"which
field does your gate read, and which one does your writer store?"* A gate fed a constant is a gate
that cannot fail.

#### 🟡 Step B — fail closed on synthetic origin, `2` edits, `13` insertions, WRITTEN

🟢 **Applied this pass by exact-string replacement, so a silent miss is impossible, and the diff
exists:**

| # | file : line | edit |
|---|---|---|
| `1` | `security/provenance.py` : after `143` | refuse `C2paStatus.NOT_APPLICABLE` when `origin == GENERATED`, in `AssetProvenance.__post_init__`, immediately after the existing provider/model/revision clause |
| `2` | `security/gates.py` : `260-262` + the import at `11` | build the accepted set per asset — `{VALID}` always, plus `NOT_APPLICABLE` only when `origin is not GENERATED`, which keeps the exemption for `USER` and `SCREEN_CAPTURE` where marking genuinely does not apply |

🔴 **Cost, PREDICTED and labelled as such: `2` of the `46` security tests break** —
`test_apache_two_generated_asset_allows_transformed_commercial_export` and
`test_mit_starter_audio_allows_transformed_commercial_export`, both of which construct a `GENERATED`
asset with full provider/model/revision and **no `c2pa=` kwarg**, so both are born
`NOT_APPLICABLE`. 🟢 **A third `GENERATED` construction,
`test_generated_assets_require_model_revision`, is already inside `assertRaises` and the
pre-existing clause fires first, so it is unaffected.**
🔴 **p175's post-patch run was REFUSED three times by this session's execution-permission layer
after the pristine run was allowed, so that cost is a static reading rather than a measurement
(`gap 132`). `ACTION KI` takes it.**
🔵 **What the prediction means for an upstream conversation, if it holds: the project's own tests
ENCODE the permissive default, so this is a behaviour change to negotiate, not a defect to report.**
🟢 **`0` tests in the repository pass a `c2pa=` kwarg at all — which is the sentence to open that
conversation with.**

#### 🔴 Step C — the visible marking duty, and the honest cost

🔴 **`c2patool` appears in `0` of the `905` files.** The encoder is external FFmpeg, invoked
shell-free by `argv` through `SubprocessEditorExportRunner.run` with a caller-supplied `ffmpeg_path`
(`editor_export.py:93-113`), so **the seam is real** — but a signer path has to reach it.
🟢 **The insertion point is a line number, not a layer:** after `verify_editor_delivery`
(`editor_export.py:885`) and **BEFORE** `store.cas.add_file` (`:907`). 🔴 **Sign after the
content-addressed insert and the recorded hash is the hash of UNMARKED bytes.**
🔴 **Two ways to write it, and both carry a cost a client should choose deliberately:**

| option | files touched | the catch |
|---|---|---|
| 🟡 `c2patool_path: Path | None = None` on `render_editor_timeline` | 🟢 **`4`** | 🔴 **inert unless a caller opts in — `T258`'s defect, rebuilt** |
| 🟢 thread it from `native_controls.py:1113` | 🔴 **`5`** | 🟢 **actually runs; p174's *"four edits"* figure is wrong** |
| 🟢 **recommended** | `5` + a test | 🟢 **take the fifth file, and add the test the project does not have: assert the gate FIRES when the flag is on and the status is absent** |

🔵 **Still not engineering: a signing certificate.** `C2paRecord` structurally requires a `signer`
for `VALID` (`provenance.py:55-60`), and no certificate exists in the tree. 🟢 **That is now the ONLY
procurement line item on this path, and it buys the VISIBLE marking duty alone — Step A already
satisfies the metadata half.**

#### 🟢 The build order, with what each step buys

| step | effort | buys |
|---|---|---|
| 🟢 **A** — read the stored status | 🟢 **`1` line, `0` dependencies** | 🟢 **the gate starts working. China Art. `5` metadata posture becomes truthful** |
| 🟡 **B** — fail closed on `GENERATED` | 🟡 **`13` insertions, `2` files, `2` tests to renegotiate** | 🟡 **synthetic output can no longer ship unmarked by default** |
| 🔴 **C** — sign the artefact | 🔴 **`5` files + a certificate** | 🟢 **EU Art. `50(2)` and China Art. `4` visible marking** |

🔵 **Run them in that order.** A, B and C are independent, and A is the one that makes the other two
observable — until the gate reads a real status, every change to it is untestable.

### 🆕 🟢 Pattern 2 — size any population exactly, in one request *(SUPERSEDES p174's partition)*

🟢 **Use the authenticated MCP repository search.** `topic:education license:mit pushed:>=<t0-180d>`
returns **`total_count: 8197`** — an exact integer, no rounding, one request, with the top `100` rows
and their full topic lists in the same response.
🔴 **Do NOT reach for p174's `17`-window `pushed:` partition first.** It works, it agreed to
`-0.07%`, and it costs `17` paced requests around a `429` that arrived after `3` reads this pass.
🟢 **Keep it as the fallback for when the authenticated channel is unavailable** — the windows must
be disjoint, each must come back under `~1 000` to read as an exact integer, and each rounded parent
should be split until its parts sum to it.
🔴 **The new channel's limit, so nobody plans around a capability it lacks: it answers SEARCH and
refuses per-repository FILE reads by session scope.** 🟢 **Wire all three:**

| job | channel |
|---|---|
| 🟢 population counts, star-ordered rows, topics | 🟢 **MCP repository search** — `1` request, exact |
| 🟢 licence BODY and byte count | 🟢 **`raw.githubusercontent.com/<owner>/<repo>/HEAD/<path>`** via `curl` |
| 🟢 `HEAD` sha without a clone | 🟢 **`git ls-remote <url> HEAD`** |
| 🟢 tree size, file counts, greps | 🟢 **`git clone`**, then measure locally |

### 🆕 🟢 Pattern 3 — verify an interop claim by ARTEFACT, never by token

🔴 **The failure this pattern exists to prevent, measured this pass:** `grep -ri "ed-fi"` returned
`55` files on a candidate SIS and the matches were `red-fill`; `edfi` returned `176` and the matches
were `normalizedField`; `lti` returned `325` and the matches were `LevelTile` and `ModalTitle`.
**`0` survived at word-boundary precision.**
🟢 **The recipe, which is two commands and a table:**

```bash
# 1. the honest count — word boundaries, and report BOTH numbers
grep -riE '\bed[-_]?fi\b|\boneroster\b|\blti\b|\bscorm\b|\bxapi\b|\bcmi5\b' --exclude-dir=.git .
# 2. when a token survives, show what it matched before believing it
grep -rioh '........<token>........' --exclude-dir=.git . | sort | uniq -c | sort -rn | head
```

🟢 **Then look for the ARTEFACT, not the name:**

| claim | the artefact that must exist |
|---|---|
| rostering | an `/ims/oneroster/v1p1/` route, or an `EdFi` client class with named resources |
| content packaging | a `imsmanifest.xml` reader, or a `cmi5`/`SCORM` runtime |
| tracking | an xAPI or Caliper STATEMENT emitter with an LRS endpoint |
| multi-tenancy | a tenant column, a schema-per-customer migration, or a row-level policy |
| federated auth | an OIDC discovery URL, a SAML metadata endpoint, or a JWKS fetch |

🔵 **Report both counts in any deliverable.** *"`55` mentions, `0` implementations"* is a finding a
client can act on; *"`55` mentions"* alone is a claim that will not survive their own engineer.
🟢 **And when the answer is negative, say what the repository DOES have** — the candidate SIS has
`48` real school-shaped Prisma models and hand-rolled cookie sessions. 🔵 **A row that is only
negative tells a client nothing about whether to fork it.**

### 🆕 🟢 Pattern 4 — EMEA assessment-integrity stack, now buildable permissively

🔴 **Until this pass this KB answered assessment integrity with design patterns only** — oral
defence, process evidence, detection-scepticism — because no permissive tool existed to name.
🟢 **Now one does, and the stack is three `MIT` repositories from three institutions:**

| layer | repo | licence *(body read)* | institution |
|---|---|---|---|
| 🟢 **integrity — code similarity** | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | `MIT`, `1 083` B | 🟢 **Ghent University** (`ugent.be`) |
| 🟢 **exercises, autograding, exam mode** | [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | `MIT`, `1 090` B | 🟢 **TU Munich** |
| 🟢 **LMS of record / corporate L&D** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | `MIT`, `1 062` B | — *(ships a licence GATE, `T208`)* |

🟢 **How to wire it:** `Artemis` owns the exercise and exam lifecycle and already autogrades;
`Dolos` runs over the submission corpus `Artemis` collects and reports similarity clusters rather
than verdicts; `mentingo` carries `SCORM` import AND export, so it is the row that moves content in
and out of an existing institutional estate.
🔵 **Why the provenance matters commercially: two of the three are owned by universities, which is
the provenance a European institutional buyer trusts most** — and `Artemis` is a teaching system TUM
runs itself, not a research artefact.
🔴 **What is NOT verified, and must be said in the same breath: licence body, holder and `HEAD` only.**
No interop, tenancy, auth model, dependency closure or build for any of the three new rows
(`gap 134`). 🟢 **`ACTION KM` verifies the first of them by artefact, per Pattern `3` — which is the
discipline that should have been applied to p174's SIS row.**
🔵 **And pair it with the regulatory frame from [`intel/market.md`](../intel/market.md): automated
grading and proctoring are Annex III high-risk with `26` months to `2 December 2027`, while Art. `26`
and `27` deployer duties are live now.** An integrity stack is the part of that programme a client
can start this quarter.

## Pass 174 — 2026-10-13

🆕 🟢 **The headline recipe of this pass is a PATCH, not a platform: Article `50(2)` marking is
addable to this shelf's best-equipped row from OUTSIDE the project, in four edits, at line numbers
this pass read. `50` days to the obligation.**

### 🆕 🟢 Pattern 1 — Article `50(2)` marking, as a patch to a named repository at named lines

🔵 **Subject:** [`AkshitIreddy/AI-Powered-Video-Tutorial-Generator`](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator)
`MIT`, pinned at `9c260890214d` — **still `HEAD` at p174**, so this is a controlled re-read of the
same `905` files p173 measured.
🔵 **Why this row:** it is the most provenance-literate project on the shelf. It already has the
C2PA vocabulary, the gate, the export manifest type, and a sidecar habit. `ACTION KA` asked whether
that is enough to MARK output. It is not, and the gap is now specified to the line.

| # | edit | file : line | what it does |
|---|---|---|---|
| 1 | reject the default for synthetic origin | `services/pipeline/src/alystria/security/provenance.py` : `138-143` | the `GENERATED` clause already demands provider + model + revision; extend it to refuse `C2paStatus.NOT_APPLICABLE` |
| 2 | stop the gate exempting its own subject | `services/pipeline/src/alystria/security/gates.py` : `260-262` | drop `NOT_APPLICABLE` from the accepted set **when origin is `GENERATED`** — keep it for `USER` and `SCREEN_CAPTURE`, where marking genuinely does not apply |
| 3 | 🟢 **sign the artefact** | `services/pipeline/src/alystria/editor_export.py` : **between `885` and `907`** | after `verify_editor_delivery` and **BEFORE** `store.cas.add_file`, run `c2patool` over `selected_output` in place. Sign after the CAS insert and the recorded hash is the hash of UNMARKED bytes |
| 4 | carry the signer's record | `services/pipeline/src/alystria/generation/workflow.py` : `3018` | replace the hand-written `C2paRecord(C2paStatus.NOT_APPLICABLE)` with the record the signer returns |

🟢 **Why it is a patch and not a fork — measured, not assumed.** The encoder is **external FFmpeg**,
invoked shell-free by `argv` through `SubprocessEditorExportRunner.run` with a caller-supplied
`ffmpeg_path` (`editor_export.py:93-113`). Nothing is vendored and nothing is closed, so there is a
seam to insert into. 🔵 **And the project already writes sidecars at `886-906`** — captions as
`.vtt`/`.srt`, attributions as `alystria.editor.credits.v1` — so a C2PA manifest arrives in a shape
the codebase already has.
🔴 **The one-line trap, and it is the whole reason step `2` exists.** p173 reported the flag
*"defaults off"*. **Flipping it on changes nothing:** the gate accepts `{VALID, NOT_APPLICABLE}`,
and `NOT_APPLICABLE` is the **default** every asset is born with (`provenance.py:125`). Measured by
constructing the gate directly on a `GENERATED` asset:

| `c2pa_required` | asset `c2pa` status | findings the gate returns |
|---|---|---|
| `False` | `NOT_APPLICABLE` *(the default)* | `[]` |
| 🔴 **`True`** | 🔴 **`NOT_APPLICABLE`** *(the default)* | 🔴 **`[]` — synthetic output passes a gate that is switched ON** |
| 🟢 `True` | `ABSENT` | 🟢 `['export.c2pa']` |
| 🟢 `True` | `VALID` | 🟢 `[]` |

🔴 **And the suite cannot catch it, which is why `ACTION KA`'s second limb fired.** `46` of `46`
tests pass with the flag `False` and `46` of `46` pass with it `True` — byte-identical, under
`python3.12 -I`. **`c2pa_required` is never set in any test in the repository:** all four
`ExportGateInput` constructions in `tests/security/test_provenance_gates.py` pass positional
arguments that stop before it. 🔵 **A flag no test sets is a flag whose default is the behaviour.**
🔵 **What is still NOT engineering:** a signing certificate. `C2paRecord` structurally requires a
`signer` for `VALID` (`provenance.py:55-60`), and no certificate exists in the tree. 🟢 **That is a
procurement line item on an engagement, and the only one left on this path.**

### 🆕 🟢 Pattern 2 — size any population exactly, on a channel that rounds

🔵 **The need:** a client asks *"how big is the open-source AI-education landscape"* and every
figure this KB could quote above `1 000` was two significant figures (`T252`, `gap 125`).
🟢 **The recipe, and it needs nothing but the channel you already have:**

1. Take the query whose count you need. Anchor: `topic:education license:mit pushed:>=2026-04-16`.
2. Read the rendered `github.com/search` total. **At or below ~`1 000` it is already exact — stop.**
3. Above it, partition on a field that holds **one value per repository** — `pushed:` date windows
   work, star bands do not partition cleanly — and read each window's exact integer.
4. Any window that still comes back rounded, **split it again** until every part is exact.
5. **Sum.** Then check each rounded parent against the sum of its parts as an agreement control.
6. Pace the requests: the channel returns `429` after roughly `7`–`10` reads in a short window.

🟢 **Result on the anchor: `17` windows, `8 191` repositories** — against *"`8.2k`"*. Controls:
`448 + 783 = 1 231` → *"`1.2k`"*, `655 + 389 + 307 + 819 = 2 170` → *"`2.2k`"*.
🔴 **State the caveat with the number:** the windows are read over ~`40` min, so a repository pushed
mid-sweep is counted twice and the total is an **upper bound** — a handful of rows at the measured
push rate, not a digit.

### 🆕 🟡 Pattern 3 — the Middle East / Africa engagement, now that the repository column is measured

🔴 **Start from the measurement, because it changes the shape of the engagement.** `16` query
formulations across two channels returned **`0`** repositories that are permissive AND active AND
education-vertical AND placed in MEA. 🟢 **But three of the four measurable candidates fail only on
ACTIVITY, and the fourth only on LICENCE.** A dormant `MIT` repository is not a dead end — **it is
a fork with no licence conversation.**

| step | component | licence | why |
|---|---|---|---|
| 1. **local curriculum reference — fork it** | [`37743/Classroom-VR`](https://github.com/37743/Classroom-VR) | 🟢 `MIT` *(`1 078` B)* | Egyptian senior-secondary biology curriculum with RAG grounding, `ejust.edu.eg`. **`323` days dormant**, so inherit it rather than wait for it |
| 2. **offline-first delivery** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | connectivity is the binding constraint in most of the region, not model quality |
| 3. **governance pack first, not last** | the licence-evidence instruments in [`compose/code/`](../compose/code) | 🟢 in-repo | `6` in `10` African higher-education institutions have **no** AI governance framework (WISE/Ashesi, `47` institutions, Feb `2026`). The deliverable a ministry can sign is the gap |
| 4. **Gulf compulsory-curriculum delivery** | carried from p173's Pattern `3` | — | UAE and KSA mandate school AI from `2025/26`; the MANDATE is strongest where the repositories are absent |

🔵 **How to say it to a client without overclaiming:** *"there is no maintained open-source
education-AI project originating in your region that we can build on — we checked `16` ways. There
are three we can fork, and the licences permit it."*

### 🟢 The component roster — RE-STATED IN FULL at p174, per `P170-C`/`T216`

🟢 **The same `74` rows covering `83` distinct repositories, carried forward unchanged from p173.
Under *"only the newest block is canonical"*, a component this KB once routed and does not re-state
is LOST from the compiled view however true it remains below.**
🟡 **Licences and `HEAD`s are p172's reads, carried forward verbatim through p173. p174 re-read
exactly one of them — `AkshitIreddy/AI-Powered-Video-Tutorial-Generator`, at the same sha — and
this line is the disclosure for the other `82`.**

| layer | component | licence | from |
|---|---|---|---|
| tutoring engine | [`ai-shifu/ai-shifu`](https://github.com/ai-shifu/ai-shifu) `7e3a34e24354` | 🟢 `Apache-2.0` | p172 P2 |
| retention scheduler | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) `f0142f28e8ed` — FSRS | 🟢 `MIT` | p172 P2 |
| practice surface | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) `e0e347f7f399` | 🟢 `MIT` | p172 P2 |
| host LMS | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) `242a9324fe48` — **EMEA** | 🟢 `MIT` | p172 P2 |
| rostering | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 `Apache-2.0` | p172 P2 |
| packaging | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | p172 P2 |
| 🟢 **assessment delivery** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** | p172 P6 |
| 🆕 🟢 **item generation reference** | [`niansia/taiwan-exam`](https://github.com/niansia/taiwan-exam) | 🟢 **`MIT`** | p172 P6 |
| 🆕 🟡 **threat model, not a dependency** | [`sgaofen/vibe-schooling`](https://github.com/sgaofen/vibe-schooling) | 🟢 **`MIT`** | p172 P6 |
| 🟢 **lightweight / offline LMS** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | p172 P6 |
| 🟡 **or, if Moodle is already deployed** | 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 **`GPL-3.0`** | p172 |
| 🔴 **do NOT use** | 🔴 [`moodlehq/moodle-enrol_oneroster`](https://github.com/moodlehq/moodle-enrol_oneroster) | 🔴 **`GPL-3.0`** | p172 |
| 3. **Where the learning happens** | 🟢 Any permissive tutor from `agents/top.md` — [`DeepTutor`](https://github.com/HKUDS/DeepTutor) *(Apache-2.0)*, [`Bloom`](https://github.com/Li-Evan/Bloom) *(MIT)*, [`universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) *(MIT)* | 🟢 **Apache-2.0 / MIT** | p172 |
| 5. 🟢 **OB 3.0 AUTHORING — already built and permissive** | 🟢 [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **MIT** *(`LICENSE`, 1 080 B)* | p172 |
| 6. 🔴 **The build: OB 3.0 ISSUANCE and SIGNING** | 🔴 **Nothing permissive ISSUES one.** [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) is **LGPL-3.0** *(`LICENSE.txt`, 7 650 B)*, `1 ★` | 🔴 **copyleft, and unmaintained-thin** | p172 |
| 7. **Mastery evidence independent of the rule** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** *(1 066 B)* | p172 |
| 1. **Experiment design and assignment** | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | 🟢 **Apache-2.0** (`LICENSE`, 11 323 B, resolves on `main` and `master`) | p172 |
| 2. **Evidence capture** | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **MIT** (🆕 `LICENSE.md`, 1 094 B — 🔴 **plain `LICENSE` is `404`, a `P50` instance**) | p172 |
| 1. **System of record** — leave it alone | [`moodle/moodle`](https://github.com/moodle/moodle) 🔴 GPL *(`COPYING.txt`)* **or** [`openedx/edx-platform`](https://github.com/openedx/edx-platform) 🔴 AGPL-3.0 | copyleft | p172 |
| 2. **Tutoring surface** — a separate process | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) 🟢 **MIT**, Go | 🟢 permissive | p172 |
| 3. **Content grounding** | [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) 🟢 **MIT**, LangGraph + FastAPI | 🟢 permissive | p172 |
| Tutor client | [`michael-borck/study-buddy`](https://github.com/michael-borck/study-buddy) — Electron + local Ollama, no internet | 🟢 **MIT** | p172 |
| On-device mobile | [`linyeping/GemMate`](https://github.com/linyeping/GemMate) — Gemma on local hardware, Dart | 🟢 **MIT** | p172 · 🔴 **p191 CORRECTION: `Apache-2.0`** |
| 🟢 **Pedagogy** | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) *(283 ★)* or [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) *(243 ★)* | 🟢 **MIT, 1 069 B / 1 102 B** | p172 |
| 🟢 **Institutional boundary** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) *(Apache-2.0, 376 ★)* for LTI, or an external MCP server — [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) *(MIT, 290 ★)* | 🟢 **Apache-2.0 / MIT** | p172 |
| 🟢 **Platform, if greenfield** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) *(92 ★)* · [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **MIT, 1 062 B** · 🟢 **Apache-2.0, 10 982 B** | p172 |
| 🟢 **SIS inputs** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** | p172 |
| records + agent surface | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) **v1.2.0** | 🟢 **Apache-2.0** | p172 |
| **LMS core** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | p172 |
| **tool launch** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** | p172 |
| **launch (Python)** | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** | p172 |
| **rostering SDK** | [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 🟢 **0BSD** | p172 |
| **conformance proof** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 **Apache-2.0** | p172 |
| **statistics / benchmarks** | [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 **MIT** | p172 |
| tutoring engine | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | p172 |
| LMS connector | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (Canvas) | MIT | p172 |
| launch into LMS | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) (LTI 1.3) | MIT | p172 |
| mastery reference model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (BKT) | MIT | p172 |
| 🆕 **orchestration (start here)** | [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | **Apache-2.0** | p172 |
| content pipeline | [`learningequality/studio`](https://github.com/learningequality/studio) | MIT | p172 |
| interactive content | [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | MIT | p172 |
| single-machine pilot | [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) | 🟡 UNREAD | p172 |
| tool inventory | LMS connectors as discovery instruments: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp), [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | MIT | p172 |
| sandboxing | [`openedx/codejail`](https://github.com/openedx/codejail) | Apache-2.0 | p172 |
| platform | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) or [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) or Moodle | GPL-3.0 | p172 |
| public portal | [`openfun/richie`](https://github.com/openfun/richie) | MIT | p172 |
| step-level feedback | [`ideas-edu/ideas`](https://github.com/ideas-edu/ideas) | Apache-2.0 | p172 |
| content generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | MIT | p172 |
| pedagogy/skill library | [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | **NOASSERTION — review first** | p172 |
| platform | [`frappe/lms`](https://github.com/frappe/lms) or Moodle | AGPL-3.0 / GPL-3.0 | p172 |
| structured lesson model | [`oppia/oppia`](https://github.com/oppia/oppia) | Apache-2.0 | p172 |
| multi-agent baseline | [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | CC0-1.0 | p172 |
| **pedagogical benchmark** | [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) (ETH Zurich, EMNLP 2025 oral) | 🔴 **none declared** — run/cite only | p172 |
| **failure-mode dataset** | [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) (Khan Academy) | 🔴 **bespoke eval-dataset licence** — run/cite only | p172 |
| connector | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** | p172 |
| assessment + gradebook | [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) | **MIT** | p172 |
| build velocity | [`SaadRahman01/moodle-mcp`](https://github.com/SaadRahman01/moodle-mcp) + [`claude-moodle-dev`](https://github.com/SaadRahman01/claude-moodle-dev) | **MIT** | p172 |
| API surface map | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) · [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) · [`HAL-XP/mcp-pronotes`](https://github.com/HAL-XP/mcp-pronotes) · [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) | MIT *(🔴 `librus-mcp`: MIT 2.x only — `legacy_reference/` is **GPL-3.0-only**)* | p172 |
| identity | [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) as the reference shape — Okta OIDC/SAML, OAuth 2.0, **SCIM** | 🔴 unlicensed — **pattern only, do not vendor the code** | p172 |
| system of record | [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | p172 |
| — or — | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **LGPL-3.0** (payload-read) | p172 |
| — or — | [`frappe/education`](https://github.com/frappe/education) | 🔴 **read `LICENSE` first** (API says `NOASSERTION`) | p172 |
| agent scaffold | [`sandraschi/classroom-mcp`](https://github.com/sandraschi/classroom-mcp) | **MIT** | p172 |
| optimiser | [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | p172 |
| reference: grade passback | [`filipecalegario/auto-sigaa`](https://github.com/filipecalegario/auto-sigaa) | **MIT** | p172 |
| reference: workload report | [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) | 🔴 **AGPL-3.0** | p172 |
| reference: Argentina | [`eugeborzone/Auto_Grade_Guarani`](https://github.com/eugeborzone/Auto_Grade_Guarani) | 🔴 **unlicensed** | p172 |
| API surface: SUAP | [`joojdev/academic-tracker-mcp`](https://github.com/joojdev/academic-tracker-mcp) (**MIT**) + [`frjunioalves/suap-mcp`](https://github.com/frjunioalves/suap-mcp) (🔴 unlicensed) | mixed | p172 |
| API surface: SIGAA | [`Agso-o/sigaa-calendar`](https://github.com/Agso-o/sigaa-calendar) (🟡 GPL-3.0), [`RubsNeto/SigaaUI`](https://github.com/RubsNeto/SigaaUI) (**MIT**), [`trindadetiago/sigaa-caiu`](https://github.com/trindadetiago/sigaa-caiu) (**MIT**) | mixed | p172 |
| **PoC scaffold** | [`paurushrai/lti-1.3-node-nextjs-starter`](https://github.com/paurushrai/lti-1.3-node-nextjs-starter) | **MIT** | p172 |
| **learner state / audit** | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | p172 |
| **analytics surface** | [`openfun/warren`](https://github.com/openfun/warren) | **MIT** | p172 |
| **enterprise auth** | [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) (pattern only), plus the second instance against a real institution — [`P1ckle3/blackboard-mcp`](https://github.com/P1ckle3/blackboard-mcp) (UQ, Okta SSO) | 🔴 **both UNLICENSED — read, do not fork** | p172 |
| **Broker** | 🔴 **"your ~300 lines"** | 🟢 **BUY**: [`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) (**Apache-2.0**, Go, MCP auth spec **2025-11-25**, RFC 9728 + 8707 + 9068, JWKS-verified upstream OIDC, PKCE, DPoP, token exchange, **56 test files**) — or [`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) (**Apache-2.0**, 60★) to front an existing MCP server *"without code modification"* | p172 |


### 🆕 🟢 Added to the roster by p174 — licence body read, `HEAD` verified, nothing more

| layer | component | licence | from |
|---|---|---|---|
| 🆕 spaced-repetition tutor over a CLI agent | [`kirilxd/claude-tutor`](https://github.com/kirilxd/claude-tutor) `ce194694eca9` — `SM-2`, `139` ★ | 🟢 **`MIT`** *(`1 063` B)* | p174 `ACTION KB` |
| 🆕 marking-path subject, read to the line | [`AkshitIreddy/AI-Powered-Video-Tutorial-Generator`](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator) `9c260890214d` | 🟢 **`MIT`** | p174 Pattern 1 |
| 🆕 🟡 **fork candidate, dormant by design of the market** | [`37743/Classroom-VR`](https://github.com/37743/Classroom-VR) `48e70069a13d` — Egypt, curriculum-grounded | 🟢 **`MIT`** *(`1 078` B)* | p174 Pattern 3 |

🟢 **Gate output at commit: re-stated in full and verified with
[`check_lost_rows.py`](../compose/code/p171-cross-block-gate/check_lost_rows.py) before the commit,
across [`verticals/solutions.md`](../verticals/solutions.md) and this file.**
## Pass 173 — 2026-10-13

🟢 **Four recipes. Three are new; one CORRECTS p172's Pattern `1` step `4`, which told a reader the
hard part of Article `50(2)` marking was already built. p173 read that code and it is not.**
🔴 **Citation rule unchanged, per `ACTION IQ`: a non-commercial or no-grant repository may appear
as EVIDENCE but never as a build step. [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM)
(revocable Community License) and [`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor)
(no grant file) are cited nowhere below as components.**

### 🆕 🔴 Pattern 1 — CORRECTION to p172's marking wrapper, step `4`

🔴 **p172 wrote: *"Extend its gates from INPUT provenance to OUTPUT marking — the hard part is
built, pointed the other way."* p173 read the subsystem at `9c260890214d` and that sentence is
half wrong in the expensive direction.**

| what p172 implied was built | what is actually there |
|---|---|
| a provenance subsystem that could be pointed at output | 🟢 **TRUE and better than implied** — `AssetProvenance`, `ConsentRecord`, `Ingredient`, `ExportProvenanceManifest`, `347`-line `gates.py`, `20`+ tests |
| *"the hard part is built"* | 🔴 **FALSE. The hard part is a SIGNER and there is none in `905` files** — the four C2PA states in the Python enum (`NOT_APPLICABLE`, `ABSENT`, `VALID`, `INVALID`) are all VERIFICATION states |
| a gate you could flip on | 🟡 **It exists and defaults OFF**: `ExportGateInput.c2pa_required: bool = False` |
| the pipeline's own generated output | 🔴 **`generation/workflow.py:3018` writes `c2pa=C2paRecord(C2paStatus.NOT_APPLICABLE)`** |

🟢 **So wire it this way instead, and the order is the point — the certificate is the critical path,
not the code:**

1. **Procure the signing identity FIRST.** An X.509 certificate from a CA in the C2PA trust list.
   A self-signed certificate produces a manifest every validator marks untrusted, which is worse
   than no manifest in a compliance conversation. 🔴 **Lead time here, not in engineering.**
2. **Add the emitter at the mux/encode boundary** — [`contentauth/c2pa-rs`](https://github.com/contentauth/c2pa-rs)
   (🟢 **`MIT OR Apache-2.0`**, dual-licensed; the crate is `c2pa`, still `0.x` beta with breaking
   changes in minor versions, and v`2` claims by default). `c2patool` from the same org for the CLI
   path. 🔴 **Beware the search result: `iptc/c2pa-rs` also resolves. `contentauth/c2pa-rs` is the
   one whose README carries the CAI badges and the dual `LICENSE-MIT` / Apache files.**
3. **Add `SIGNED` to the Python enum** so the gate can distinguish *"we signed this"* from
   *"someone else's manifest verified"*. The TypeScript contract at
   `packages/contracts/src/media.ts:21` **already has the word** (`"signed" | "verified" | ...`) —
   the vocabulary exists in the repo and is missing from the layer that enforces (`T245`).
4. **Flip `c2pa_required` to `True`** and run the project's own suite. 🟡 **`ACTION KA` is
   registered to measure whether it passes unmodified — if it does, the gate was never the
   obstacle.**
5. **Stop the transcode from eating the mark.** `packages/themes/src/starterKitCatalog.ts:92` sets
   `c2paStatus: derived ? "absent" : "present-embedded"` with the note *"the optimized WebP
   derivative does not"*. 🔴 **Every derivative step is a place a credential dies (`T256`). Re-sign
   after each one, or carry a sidecar and say in the deliverable that it is a sidecar.**
6. **Add the HUMAN-readable notice separately.** `ConsentRecord.synthetic_media_disclosure` is the
   SUBJECT's consent, not the LEARNER's notice. Article `50(2)` marking is machine-readable;
   Article `50(4)` deepfake disclosure is human-readable. **Two obligations, and this shelf has
   neither pointed at the learner (`T246`).**

🔵 **Keep p172's steps `1`–`3` for text and packaging — the SCORM choke point, the marking emitters
in `compose/code/aiact-50-2-*`, and the exposure scan. The correction is to step `4` only.**

### 🆕 🟢 Pattern 2 — a shortlist that does not lie about size or liveness

**Problem.** Two independent defects measured this pass: the tag this KB counts on is one `1` of
`12` of its own shelf rows use (`T255`), and the `180`-day *"active"* filter admits `25.2%`
repositories unpushed for `90` days (`T242`). **A shortlist built the usual way is both too narrow
and too dead.**

**Wire it — three steps, no `api.github.com`, no paid data:**

| step | how | why it is this and not the obvious thing |
|---|---|---|
| 1. **widen the tag** | run the sweep on `topic:education`, `topic:edtech`, `topic:ai-tutor` AND `topic:ai-education`, with the same `license:` + `pushed:` filters. Strings in [`compose/code/p173-dormancy-bands/queries.txt`](../compose/code/p173-dormancy-bands/queries.txt) | `ai-education` is a research-flavoured tag; practitioners tag the thing they built. `~61×` difference on the same filters |
| 2. **band for dormancy before enumerating** | re-run each query with a moving `pushed:>=` bound and subtract. `4` queries give the whole distribution without listing a single repository | enumeration costs `14` rendered pages per population; banding costs `4` and is exact under `1 000` |
| 3. **confirm liveness by COMMIT, per candidate** | `git clone --depth 1 --filter=blob:none --no-checkout <url>` then `git log -1 --format=%cI` | `pushed:` counts tags, merges and side branches. The commit date is the only field that means *"someone is working on this"* |

🔴 **And record the channel's PRECISION with the count (`T252`): above `1 000` the rendered page
returns *"8.2k"*. A four-figure number from this channel is an order of magnitude. Do not put it in
a deck as a market size.**

### 🆕 🟢 Pattern 3 — Gulf compulsory-curriculum delivery, with the attribution handled

**Where this applies.** The UAE and Saudi Arabia have made AI education compulsory across public
schooling (UAE from age four, `KG`→grade `12`; `24 000`+ educators through the national upskilling
week for `2026–2027`). Egypt started AI curricula in the `2025-26` year. 🟢 **The buying centre is
a ministry or a large public system, and the ask is DELIVERY AT SCALE, not persuasion.**

| layer | component | licence | why this one |
|---|---|---|---|
| institutional LMS | [**OpenOLAT**](https://github.com/OpenOLAT/OpenOLAT) | 🟢 `Apache-2.0` *(§`1`–`9` verbatim)* | `QTI` + `SCORM` + curriculum + assessment in one tree. Carry its `2` attribution statements |
| low-connectivity edge | [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 `MIT` | the offline row; the same choice that serves rural LATAM and Africa |
| teacher-facing AI mentor | [**Selleo/mentingo**](https://github.com/Selleo/mentingo) `242a9324fe48` | 🟢 `MIT` | AI mentor inside an LMS, `SCORM` in AND out, and it ships `licenses.config.yaml` — a licence gate to LIFT, not just a dependency |
| rostering | [**Ed-Fi-Alliance-OSS/edfi-oneroster**](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 `Apache-2.0` | `OneRoster 1.2`, `24` GETs, `0` write routes — read-only by construction, which a ministry security review will like |
| assessment integrity | 🟡 [**niansia/taiwan-exam**](https://github.com/niansia/taiwan-exam) | 🟡 `MIT` root | 🔴 **swap `PyMuPDF` (`AGPL-3.0`-or-commercial) for `pypdf` (`BSD-3`), already in the same `requirements.txt`, BEFORE routing** |
| packaging | [**jcputney/scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | the delivery choke point, and where marking goes |

🆕 🟢 **The step this pass adds, and it is cheap insurance: run the licence manifest before the
deliverable, not after.** If the stack pulls a Java-era component tree —
[`Sakai`](https://github.com/sakaiproject/sakai) is the live example — a scanner will report
*"`34` BSD"* over `licenses/` and **`25` of those are `Apache-1.1`**, which carries a clause-`3`
acknowledgment BSD does not: *"This product includes software developed by the Apache Software
Foundation"*. 🟢 **Use `compose/code/p173-apache11-family/sweep_family.sh` against the manifest
directory and put the acknowledgment in the end-user documentation. Attribution debt found after
delivery is a re-release; found before, it is a line of text.**
🔴 **`0` of this stack originates in the region (`gap 124`). Say so, and price localisation —
Arabic-first content, ministry reporting formats — as build and not as configuration.**

### 🆕 🟢 Pattern 4 — Africa governance-first, because the policy is the gap

**Where this applies.** `6` in `10` of `47` surveyed African higher-education institutions have no
formal AI governance framework (WISE/Ashesi, February `2026`); adoption is *"low to moderate"*;
under `2%` of African edtech startups build AI for higher education against `64%` for K-12.
🟢 **Unlike the Gulf, the first deliverable here is not a platform.**

| phase | what ships | anchored on |
|---|---|---|
| 1. **policy scaffolding** | institutional AI-use policy, assessment-integrity rules, staff capability baseline | South Africa's Draft National AI Policy Framework *(comment March `2026`, implementation `2027–2028`)*, Kenya's National AI Strategy `2025–2030`, Rwanda's `2023` National AI Policy |
| 2. **assessment integrity before tutoring** | detection-sceptical rules *(UCT's own framework calls AI detection tools unreliable)*, plus oral/viva and process-evidence designs | the `5` of `12` assessment-CARRYING shelf rows (`T234`), and 🔴 **`sgaofen/vibe-schooling` as a THREAT MODEL, never a dependency** |
| 3. **platform, offline-first** | [**Kolibri**](https://github.com/learningequality/kolibri) (🟢 `MIT`) at the edge, [**Moodle**](https://github.com/moodle/moodle) (🔴 `GPL-3.0`, `88` grant documents) where an institution already runs it | the routing table in [`verticals/solutions.md`](../verticals/solutions.md) |
| 4. **only then, AI on top** | the permissive tutor stack of p172's Pattern `2` | all `MIT`/`Apache-2.0`, `HEAD`-verified |

🔴 **Two constraints to state in the proposal rather than discover: the equity skew is documented —
sources warn AI education becomes an elite preserve without rural targeting — and `0` of the
components above originate in Africa, so local capability transfer is part of the scope or the
engagement leaves nothing behind.**
🟢 **The donor channel is real and is aimed at exactly this: the Gates Foundation committed
~`US$4.0M` in July `2026` to fine-tune OPEN-SOURCE small models for Sub-Saharan classrooms and
build a local edtech ecosystem. An open-source-first proposal is funding-aligned here in a way it
is not in most regions.**
### 🟢 The component roster — RE-STATED IN FULL at p173, per `P170-C`/`T216`

🟢 **`74` rows covering `83` distinct repositories, carried forward from p172's six recipes. Under
*"only the newest block is canonical"* a component this KB once routed and does not re-state is
LOST from the compiled view however true it remains below — and p173's first draft dropped `77` of
them. The gate caught it before commit, which is the second consecutive pass where
[`check_lost_rows.py`](../compose/code/p171-cross-block-gate/check_lost_rows.py) has fired on the
pass that ran it.**
🟡 **Licences and `HEAD`s are p172's reads carried forward verbatim. p173 re-read none of them and
this line is the disclosure. The only component whose STATUS p173 changes is step `4` of Pattern
`1`, corrected above.**

| layer | component | licence | from |
|---|---|---|---|
| tutoring engine | [`ai-shifu/ai-shifu`](https://github.com/ai-shifu/ai-shifu) `7e3a34e24354` | 🟢 `Apache-2.0` | p172 P2 |
| retention scheduler | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) `f0142f28e8ed` — FSRS | 🟢 `MIT` | p172 P2 |
| practice surface | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) `e0e347f7f399` | 🟢 `MIT` | p172 P2 |
| host LMS | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) `242a9324fe48` — **EMEA** | 🟢 `MIT` | p172 P2 |
| rostering | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 `Apache-2.0` | p172 P2 |
| packaging | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | p172 P2 |
| 🟢 **assessment delivery** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** | p172 P6 |
| 🆕 🟢 **item generation reference** | [`niansia/taiwan-exam`](https://github.com/niansia/taiwan-exam) | 🟢 **`MIT`** | p172 P6 |
| 🆕 🟡 **threat model, not a dependency** | [`sgaofen/vibe-schooling`](https://github.com/sgaofen/vibe-schooling) | 🟢 **`MIT`** | p172 P6 |
| 🟢 **lightweight / offline LMS** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | p172 P6 |
| 🟡 **or, if Moodle is already deployed** | 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 **`GPL-3.0`** | p172 |
| 🔴 **do NOT use** | 🔴 [`moodlehq/moodle-enrol_oneroster`](https://github.com/moodlehq/moodle-enrol_oneroster) | 🔴 **`GPL-3.0`** | p172 |
| 3. **Where the learning happens** | 🟢 Any permissive tutor from `agents/top.md` — [`DeepTutor`](https://github.com/HKUDS/DeepTutor) *(Apache-2.0)*, [`Bloom`](https://github.com/Li-Evan/Bloom) *(MIT)*, [`universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) *(MIT)* | 🟢 **Apache-2.0 / MIT** | p172 |
| 5. 🟢 **OB 3.0 AUTHORING — already built and permissive** | 🟢 [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **MIT** *(`LICENSE`, 1 080 B)* | p172 |
| 6. 🔴 **The build: OB 3.0 ISSUANCE and SIGNING** | 🔴 **Nothing permissive ISSUES one.** [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) is **LGPL-3.0** *(`LICENSE.txt`, 7 650 B)*, `1 ★` | 🔴 **copyleft, and unmaintained-thin** | p172 |
| 7. **Mastery evidence independent of the rule** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** *(1 066 B)* | p172 |
| 1. **Experiment design and assignment** | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | 🟢 **Apache-2.0** (`LICENSE`, 11 323 B, resolves on `main` and `master`) | p172 |
| 2. **Evidence capture** | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **MIT** (🆕 `LICENSE.md`, 1 094 B — 🔴 **plain `LICENSE` is `404`, a `P50` instance**) | p172 |
| 1. **System of record** — leave it alone | [`moodle/moodle`](https://github.com/moodle/moodle) 🔴 GPL *(`COPYING.txt`)* **or** [`openedx/edx-platform`](https://github.com/openedx/edx-platform) 🔴 AGPL-3.0 | copyleft | p172 |
| 2. **Tutoring surface** — a separate process | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) 🟢 **MIT**, Go | 🟢 permissive | p172 |
| 3. **Content grounding** | [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) 🟢 **MIT**, LangGraph + FastAPI | 🟢 permissive | p172 |
| Tutor client | [`michael-borck/study-buddy`](https://github.com/michael-borck/study-buddy) — Electron + local Ollama, no internet | 🟢 **MIT** | p172 |
| On-device mobile | [`linyeping/GemMate`](https://github.com/linyeping/GemMate) — Gemma on local hardware, Dart | 🟢 **MIT** | p172 · 🔴 **p191 CORRECTION: `Apache-2.0`** |
| 🟢 **Pedagogy** | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) *(283 ★)* or [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) *(243 ★)* | 🟢 **MIT, 1 069 B / 1 102 B** | p172 |
| 🟢 **Institutional boundary** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) *(Apache-2.0, 376 ★)* for LTI, or an external MCP server — [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) *(MIT, 290 ★)* | 🟢 **Apache-2.0 / MIT** | p172 |
| 🟢 **Platform, if greenfield** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) *(92 ★)* · [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **MIT, 1 062 B** · 🟢 **Apache-2.0, 10 982 B** | p172 |
| 🟢 **SIS inputs** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** | p172 |
| records + agent surface | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) **v1.2.0** | 🟢 **Apache-2.0** | p172 |
| **LMS core** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | p172 |
| **tool launch** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** | p172 |
| **launch (Python)** | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** | p172 |
| **rostering SDK** | [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 🟢 **0BSD** | p172 |
| **conformance proof** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 **Apache-2.0** | p172 |
| **statistics / benchmarks** | [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 **MIT** | p172 |
| tutoring engine | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | p172 |
| LMS connector | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (Canvas) | MIT | p172 |
| launch into LMS | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) (LTI 1.3) | MIT | p172 |
| mastery reference model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (BKT) | MIT | p172 |
| 🆕 **orchestration (start here)** | [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | **Apache-2.0** | p172 |
| content pipeline | [`learningequality/studio`](https://github.com/learningequality/studio) | MIT | p172 |
| interactive content | [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | MIT | p172 |
| single-machine pilot | [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) | 🟡 UNREAD | p172 |
| tool inventory | LMS connectors as discovery instruments: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp), [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | MIT | p172 |
| sandboxing | [`openedx/codejail`](https://github.com/openedx/codejail) | Apache-2.0 | p172 |
| platform | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) or [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) or Moodle | GPL-3.0 | p172 |
| public portal | [`openfun/richie`](https://github.com/openfun/richie) | MIT | p172 |
| step-level feedback | [`ideas-edu/ideas`](https://github.com/ideas-edu/ideas) | Apache-2.0 | p172 |
| content generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | MIT | p172 |
| pedagogy/skill library | [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | **NOASSERTION — review first** | p172 |
| platform | [`frappe/lms`](https://github.com/frappe/lms) or Moodle | AGPL-3.0 / GPL-3.0 | p172 |
| structured lesson model | [`oppia/oppia`](https://github.com/oppia/oppia) | Apache-2.0 | p172 |
| multi-agent baseline | [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | CC0-1.0 | p172 |
| **pedagogical benchmark** | [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) (ETH Zurich, EMNLP 2025 oral) | 🔴 **none declared** — run/cite only | p172 |
| **failure-mode dataset** | [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) (Khan Academy) | 🔴 **bespoke eval-dataset licence** — run/cite only | p172 |
| connector | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** | p172 |
| assessment + gradebook | [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) | **MIT** | p172 |
| build velocity | [`SaadRahman01/moodle-mcp`](https://github.com/SaadRahman01/moodle-mcp) + [`claude-moodle-dev`](https://github.com/SaadRahman01/claude-moodle-dev) | **MIT** | p172 |
| API surface map | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) · [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) · [`HAL-XP/mcp-pronotes`](https://github.com/HAL-XP/mcp-pronotes) · [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) | MIT *(🔴 `librus-mcp`: MIT 2.x only — `legacy_reference/` is **GPL-3.0-only**)* | p172 |
| identity | [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) as the reference shape — Okta OIDC/SAML, OAuth 2.0, **SCIM** | 🔴 unlicensed — **pattern only, do not vendor the code** | p172 |
| system of record | [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | p172 |
| — or — | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **LGPL-3.0** (payload-read) | p172 |
| — or — | [`frappe/education`](https://github.com/frappe/education) | 🔴 **read `LICENSE` first** (API says `NOASSERTION`) | p172 |
| agent scaffold | [`sandraschi/classroom-mcp`](https://github.com/sandraschi/classroom-mcp) | **MIT** | p172 |
| optimiser | [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | p172 |
| reference: grade passback | [`filipecalegario/auto-sigaa`](https://github.com/filipecalegario/auto-sigaa) | **MIT** | p172 |
| reference: workload report | [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) | 🔴 **AGPL-3.0** | p172 |
| reference: Argentina | [`eugeborzone/Auto_Grade_Guarani`](https://github.com/eugeborzone/Auto_Grade_Guarani) | 🔴 **unlicensed** | p172 |
| API surface: SUAP | [`joojdev/academic-tracker-mcp`](https://github.com/joojdev/academic-tracker-mcp) (**MIT**) + [`frjunioalves/suap-mcp`](https://github.com/frjunioalves/suap-mcp) (🔴 unlicensed) | mixed | p172 |
| API surface: SIGAA | [`Agso-o/sigaa-calendar`](https://github.com/Agso-o/sigaa-calendar) (🟡 GPL-3.0), [`RubsNeto/SigaaUI`](https://github.com/RubsNeto/SigaaUI) (**MIT**), [`trindadetiago/sigaa-caiu`](https://github.com/trindadetiago/sigaa-caiu) (**MIT**) | mixed | p172 |
| **PoC scaffold** | [`paurushrai/lti-1.3-node-nextjs-starter`](https://github.com/paurushrai/lti-1.3-node-nextjs-starter) | **MIT** | p172 |
| **learner state / audit** | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | p172 |
| **analytics surface** | [`openfun/warren`](https://github.com/openfun/warren) | **MIT** | p172 |
| **enterprise auth** | [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) (pattern only), plus the second instance against a real institution — [`P1ckle3/blackboard-mcp`](https://github.com/P1ckle3/blackboard-mcp) (UQ, Okta SSO) | 🔴 **both UNLICENSED — read, do not fork** | p172 |
| **Broker** | 🔴 **"your ~300 lines"** | 🟢 **BUY**: [`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) (**Apache-2.0**, Go, MCP auth spec **2025-11-25**, RFC 9728 + 8707 + 9068, JWKS-verified upstream OIDC, PKCE, DPoP, token exchange, **56 test files**) — or [`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) (**Apache-2.0**, 60★) to front an existing MCP server *"without code modification"* | p172 |

🟢 **Gate output at commit: `routed-in-history: 83 | routed in newest block: 83 | LOST: 0` across
[`verticals/solutions.md`](../verticals/solutions.md) and this file.**

## Pass 172 — 2026-10-13

🟢 **Six recipes. Every repository named below is `HEAD`-verified this pass or carries a body-read
licence from a named prior pass, and every copyleft or non-commercial component is flagged AT the
point it is named rather than in a footnote.**
🔴 **Citation rule this file follows, per `ACTION IQ`: a non-commercial or no-grant repository may
appear as EVIDENCE but never as a build step. [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM)
(revocable Community License) and [`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor)
(no grant file) are therefore cited nowhere below as components.**

### 🆕 🔴 Pattern 1 — the Article `50(2)` marking wrapper (`50` days, build this first)

**Problem.** `0` of `13` generating rows on this shelf can mark output as synthetic
(`ACTION JQ`). The deadline is `2 December 2026`.

**Why a wrapper and not a patch.** The exposure is spread across `13` repositories in `4`
languages. Marking at the *delivery boundary* is one component; marking inside each generator is
thirteen forks you then maintain.

**Wire it:**
1. **Delivery boundary** — [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (`MIT`, `882f3b8c7498`). Every generated lesson becomes a SCORM/xAPI package here. This is the single choke point for text, and the only row this KB classifies as `pack`.
2. **Mark on the way through** — `compose/code/aiact-50-2-marking` emits the marking; `aiact-50-2-spans` computes WHICH spans are synthetic when a lesson mixes human and generated text; `aiact-50-2-pack` bundles the declaration.
3. **Prove coverage** — `compose/code/aiact-50-2-exposure` + `compose/code/p172-aiact-shelf19/scan_p172.sh` re-run per release. 🔴 **Both need network — they clone and fetch. Budget for that in an air-gapped review (`ACTION JQ` limb 2 FIRED).**
4. **For synthetic audio/video** — route through [`AkshitIreddy/AI-Powered-Video-Tutorial-Generator`](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator) (`MIT`, `9c260890214d`), which already ships `services/pipeline/src/alystria/security/provenance.py` and `test_provenance_gates.py`. 🟡 **Extend its gates from INPUT provenance to OUTPUT marking — the hard part is built, pointed the other way.**

🔵 **What this does not do: Article `50(2)` wants a machine-readable mark, and a SCORM manifest
field is machine-readable to a SCORM player, not to a general detector. Pair with `C2PA` on media
assets. Say this limit out loud rather than claiming conformity.**

### 🆕 🟢 Pattern 2 — permissive adaptive tutor, no licence conversation

**Components, all `MIT`/`Apache-2.0`, all `HEAD`-verified at `t0 = 2026-10-13T10:55:53Z`:**

| layer | component | licence |
|---|---|---|
| tutoring engine | [`ai-shifu/ai-shifu`](https://github.com/ai-shifu/ai-shifu) `7e3a34e24354` | 🟢 `Apache-2.0` |
| retention scheduler | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) `f0142f28e8ed` — FSRS | 🟢 `MIT` |
| practice surface | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) `e0e347f7f399` | 🟢 `MIT` |
| host LMS | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) `242a9324fe48` — **EMEA** | 🟢 `MIT` |
| rostering | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 `Apache-2.0` |
| packaging | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` |

**Wiring.** `edfi-oneroster` supplies the class list → `mentingo` holds enrolment and the record →
`ai-shifu` generates the lesson for a learner profile → `OpenTutor`'s FSRS decides WHEN the learner
sees it again → `anki-mcp-server` is where the review actually happens → `scorm-again` packages it
and carries the Pattern 1 mark.
🟢 **`mentingo` ships `licenses.config.yaml`, a licence gate. LIFT IT — point it at your own
dependency set. It is the only row on this shelf that ships its own compliance control.**
🔴 **Known gap: `mentingo`'s gate FAILS `Sakai` (`T208`). If the client is a Sakai institution, the
gate will reject the host platform; expect that conversation and have `OpenOLAT` (`Apache-2.0`)
ready as the alternative.**

### 🆕 🟡 Pattern 3 — exam generation, with the dependency fixed before you ship

**This is the assessment route this KB routed for the first time this pass, and it needs one repair.**

1. **Generator** — [`niansia/taiwan-exam`](https://github.com/niansia/taiwan-exam) (`MIT`, `e2193181c95c`, `593` files, `129` commits in the 30 days to p172, `89` test files). Produces original mock exams with worked solutions and official layout.
2. 🔴 **REPAIR FIRST.** Its `requirements.txt` pins **`PyMuPDF`**, whose PyPI metadata reads *"Dual Licensed - GNU AFFERO GPL 3.0 or Artifex Commercial License"*. The `MIT` root does not reach the closure (`ACTION JR`).
   🟢 **The fix is cheap: `pypdf` (`BSD-3-Clause`) is ALREADY a dependency in the same file.** Move parsing to `pypdf`; `PyMuPDF`'s `AGPL` limb is its rendering path. If rendering is genuinely needed, buy the Artifex commercial licence and record it.
3. **Honour its DATA carve-out.** `references/attribution-and-forks.md` states that third-party exam papers, passages, photographs and fonts *"remain separately governed and are not licensed by this project's MIT declaration."* 🟢 **Generate; do not redistribute the bundled reference PDFs.**
4. **Delivery** — [`ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) has the strongest built-in exam tooling of any platform here. 🔴 **`GPL-3.0` — reciprocal. For a permissive delivery path use [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (`Apache-2.0`), whose `QTI` support is the exchange format you want anyway.**
5. 🔴 **Threat-model integrity.** [`sgaofen/vibe-schooling`](https://github.com/sgaofen/vibe-schooling) (`MIT`, `80`★) is Canvas-LMS + `MCP` exam automation advertising *"get 4.0 GPA without learning"*. 🔴 **CITED AS A THREAT, NEVER A COMPONENT.** The attack tooling is permissive and deployable; design proctoring assuming it is present. 🔴 **And note Annex III point `3` makes the DEFENCE high-risk: monitoring prohibited behaviour during tests is in scope from `2 December 2027`.**

### 🆕 🟢 Pattern 4 — the licence-evidence pack a client reviewer will actually ask for

**Problem this pass proved.** A root grant is not a closure, a manifest is not a map, and a
classifier's family name is not a licence. All three failed on real trees this pass.

**Wire it, in this order — each step catches what the previous one cannot:**
1. **Root grant** — `compose/code/grant-ladder-v4`. Reads the body, not the GitHub badge.
2. **Tree-wide grants** — `compose/code/p441-tree-licence-enumeration`. 🔴 **`Moodle` reports `193` grant-named paths and only `88` are grant DOCUMENTS; `105` are PHP files carrying a per-file header (`T223`). Classify, do not count.**
3. **Dependency closure** — `compose/code/dependency-licence-closure` + `p438-depth2-closure`. 🔴 **This is the step that catches `taiwan-exam`'s `AGPL` `PyMuPDF` under an `MIT` root. A root-only review passes that repository.**
4. **Manifest attribution** — `compose/code/p172-manifest-attribution`. 🔴 **New this pass. On `Sakai`'s `licenses/`: `8` of `86` paths are proprietary Sun click-through agreements, `8` are copies of a generic family file carrying no component evidence, `1` is a 130-byte pointer and not a grant at all.**
5. **Family identity** — `compose/code/lib/license_family.sh`, 🔴 **with the `Apache-1.1` correction applied by hand (`T232`): it answers `BSD` for the Apache Software License 1.1, which is `25` of `Sakai`'s `86` paths. A scanner report saying *"34 BSD"* over that tree is `~25` files wrong.**

🔵 **Run them in order and report the DISAGREEMENTS, not just the verdicts. Every finding this pass
came from two instruments disagreeing about one payload.**

### 🆕 🟢 Pattern 5 — the LATAM governance engagement (`87%` deployed, `26%` governed)

**The fact it rests on.** UNESCO IESALC: `200` institutions, `19` countries, `87%` using AI in at
least one area, `74%` in teaching and learning, **`26%` with a formal AI strategy**.

**This is not a tooling engagement.** Deliver, in this order:
1. **An AI-use policy and an approval process.** The **European Schools** network is the quotable precedent for *"we have not approved anything yet, and here is the process"* — defensible, and it exists.
2. **Oversight gates in the workflow, not in a document.** `compose/code/grading-draft-gate` — an AI-proposed grade stays a DRAFT until a human commits it. 🟢 **This is literally the control Oklahoma and Maryland now require of US districts, which means one build serves both regions.**
3. **Evidence of instructional benefit.** The thing HolonIQ and `1EdTech` both report buyers now demanding, and the thing `26%`-governance institutions cannot produce.
4. **Low-connectivity substrate** — [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (`MIT`, `5d47c94a8ecc`), offline-first.
5. **Partner channel** — UNESCO's **Observatory on AI in Education for Latin America and the Caribbean** (launched `14 April 2026`) and **Ceibal** in Uruguay (`75%` of public-school teachers already using these tools).

🔴 **Scope honestly: this KB has no commercial map of LATAM edtech vendors or funders. Four passes
have searched and four have found multilateral and public actors only. Do not present a competitive
landscape this KB does not have.**

### 🆕 🟢 Pattern 6 — pedagogy-as-skill, the cheapest thing on this page

**Observation.** The three repositories that entered this KB this pass with real teaching logic
ship **no runtime at all** — they are agent skills and Markdown.

| component | licence | region | what it contributes |
|---|---|---|---|
| [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) `075c1895d255` | 🟢 `MIT` | **APAC** | 🟢 **decides whether to explain, ask, drill or STOP — a stopping rule, which no other row on this shelf models** |
| [`TovTechOrg/Tov-learn`](https://github.com/TovTechOrg/Tov-learn) `290af750671a` | 🟢 `MIT` | **EMEA** | interactive tutor as an agent skill |
| [`timothywarner-org/ai901-cert-buddy-claude`](https://github.com/timothywarner-org/ai901-cert-buddy-claude) | 🟢 `MIT` | Global | vendor-certification prep — the corporate-L&D shape |

**Wire it.** Load the skill into the host agent; put [`Selleo/mentingo`](https://github.com/Selleo/mentingo)
(`MIT`, enterprise L&D, **EMEA**) underneath it for enrolment, records and SCORM; let the skill
decide pedagogy and the LMS own the record.
🔴 **Article `50(2)` still applies.** This KB classifies these rows `gen-ind` — the host agent
generates, so the obligation lands on the deployer. 🟢 **A skill with no runtime cannot mark its own
output; the mark has to come from Pattern 1's boundary. This is the clearest case for marking at
delivery rather than at generation.**
## 🆕 🟢 `P171-A` — family identity comes from the TITLE *(p171 — Global)*

🟢 **`P170-A` decides IF a candidate carries a grant. `P171-A` is the step after it: WHICH grant,
and is it compatible with the outer one. It exists because p170's `129` and `193` were counts
without families, and because p171's first attempt at families was wrong on `3` of `Sakai`'s `72`
blobs — caught by READING them, not by the tally.**

```sh
# step 7  SOURCE FILES ARE NOT GRANTS. Exclude .php/.js/.java/.py/... before classifying.
#         Moodle headers every php file with a GPL notice AND ships admin/tool/licensemanager/,
#         whose filenames all contain "license". The conventions multiply: 105 of 193.
# step 8  IDENTITY FROM THE TITLE, line-anchored -- never a family name matched anywhere in
#         the body. LGPL-2.1 section 3 names the ordinary GPL, so an anywhere-match reads
#         LGPL as dual GPL+LGPL. Keep prose references in a SEPARATE column.
# step 9  NORMALISE WHITESPACE before any phrase match. Legal text is hard-wrapped at ~70
#         columns: "GNU General Public\nLicense" defeats a flat search.
# step 10 STRIP MARKDOWN before title matching: "# Apache License", "**TinyMCE**",
#         "[GNU General Public License ...](http://...)". Formatting, not law, is what
#         defeats these patterns -- so tolerate formatting.
# step 11 KNOW THE RECIPROCAL FAMILIES BY NAME: EPL, MPL, CDDL, IPL-1.0, CPL-1.0. An unknown
#         family does not fail loudly -- it falls through to whatever prose it happens to
#         contain. junit-3.8.1's IPL-1.0 was read as GPL+MPL+Python.
# step 12 CARVE OUT GPL-3.0 section 6(b): "allowed only occasionally and noncommercially" is
#         a condition on a conveying METHOD, not a non-commercial restriction. Every full
#         GPL-3.0 body trips a naive search, including Moodle's own COPYING.txt.
```

🟢 **Implementation and `10` of `10` regression tests:
[`compose/code/p171-inner-grant-classify/`](code/p171-inner-grant-classify/). Every test case is a
body p171 actually read, and the first five are the five it first got wrong.**

## 🆕 🟢 `P171-B` — the cross-block gate, with the population fixed *(p171 — Global)*

🔴 **`P170-C` was specified at p170 and implemented at p171, and its first shape reported `372` lost
rows across `3` files — `P471`, a gate that marks everything controls nothing.**

| attempt | produced | why it was unsound |
|---|---|---|
| 🔴 **every repo on a line carrying a licence identifier** | 🔴 **`372` findings** | 🔴 **wrong POPULATION: these files carry `190`-row CENSUS tables (MCP servers, LTI libraries, QTI players) that no pass offered as recommendations. A newest block that does not re-state a census has lost nothing** |
| 🟢 **restricted to ROUTING tables — headed `need`, `engagement` or `layer`** | 🟢 **`7` findings, `98%` cut** | 🟢 **a routing table answers *"what should a client use"*. A census answers *"what exists"*** |
| 🟢 **plus `casefold` on the slug** | 🟢 **`6`** | 🟢 **GitHub owners are case-insensitive and this KB writes `openolat/OpenOLAT` and `OpenOLAT/OpenOLAT` in one file (`T226`)** |

🟢 **And it caught p171's OWN first draft dropping `3` rows p170 had carried (`ILIAS`, `RosarioSIS`,
`openSIS-Classic`) — the gate working against the pass that wrote it, which is the only real test of
a gate like this.**
🔴 **It reports and never auto-fixes. Of `6` flagged rows, `5` were RESTORED and `1`
([`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia)) was a DELIBERATE removal: p169
measured it abandoned. A gate that had *"corrected"* it back would have re-recommended a dead
package.**
🟢 **Implementation: [`compose/code/p171-cross-block-gate/`](code/p171-cross-block-gate/).**

## 🆕 🟢 `P171-C` — the `50`-day Article `50(2)` marking pattern *(p171 — EMEA)*

🔴 **The nearest binding EMEA obligation on this shelf is NOT Annex III high-risk. The BASE
instrument is `Regulation (EU) 2024/1689` — the AI Act, whose Annex III point `3` puts education in
scope and whose Article `50` carries the transparency duty. `Regulation (EU) 2026/1744`, the
*"Digital Omnibus on AI"*, is a VERIFIED AMENDING act: it moved Annex III high-risk to
`2 December 2027` and left Article `50` untouched at `2 December 2026` (`ACTION JL`, `T217`).
Name `2024/1689` first in any client material.**
🟢 **This KB is unusually well placed for it — the tooling already exists and runs offline:**

| layer | asset | what it does |
|---|---|---|
| 🟢 **marking** | [`compose/code/aiact-50-2-marking/`](code/aiact-50-2-marking/) | 🟢 **emits the provenance marking, with a fixtures provenance policy** |
| 🟢 **packaging** | [`compose/code/aiact-50-2-pack/`](code/aiact-50-2-pack/) | 🟢 **packs it against `aiact-50-2.xsd`** |
| 🟢 **exposure** | [`compose/code/aiact-50-2-exposure/`](code/aiact-50-2-exposure/) | 🟢 **scans a tree for which surfaces are exposed** |
| 🟢 **spans** | [`compose/code/aiact-50-2-spans/`](code/aiact-50-2-spans/) | 🟢 **locates the spans that need marking** |

🟢 **Wiring, concretely: run `aiact-50-2-exposure` over the delivery repo; for every generative
surface it finds, emit marking via `aiact-50-2-marking` and validate with `aiact-50-2-pack` against
the `XSD` in CI. On an LMS engagement the surfaces are the ones that generate learner-facing text —
in [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) the assessment and feedback paths; in
[`Selleo/mentingo`](https://github.com/Selleo/mentingo) the course-content paths.**
🔴 **Pre-registered as `ACTION JQ`: no row on this shelf has yet been shown to emit a conformant
marking, so treat the above as a BUILD, not an integration.**

## 🆕 🟢 `P171-D` — an assessment-integrity stack, which is the gap the vertical is pointing at

🔴 **`ACTION JN` found the vertical's live edge is assessment (`4` of `5` new finds), that Annex III
point `3` names *"monitoring and detecting prohibited behaviour of students during tests"*, that
Vietnam's and Korea's statutes name automated assessment — and that a `80`-★ `MIT` tool exists whose
stated purpose is defeating exactly that.**

| layer | repo | licence *(body read)* | role |
|---|---|---|---|
| 🟢 **assessment delivery** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** | 🟢 **`QTI` + `SCORM` + assessment built in, and the only permissive institutional LMS verified here** |
| 🟢 **item interop** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 **`SCORM 1.2`/`2004` + `AICC` at the content boundary** |
| 🆕 🟢 **item generation reference** | [`niansia/taiwan-exam`](https://github.com/niansia/taiwan-exam) | 🟢 **`MIT`** | 🆕 🟢 **original item authoring WITH worked solutions and formal layout — the shape a client asks for and nobody on this shelf had** |
| 🆕 🟡 **threat model, not a dependency** | [`sgaofen/vibe-schooling`](https://github.com/sgaofen/vibe-schooling) | 🟢 **`MIT`** | 🔴 **READ IT, DO NOT SHIP IT. It documents the Canvas + `MCP` + TTS + smart-glasses attack path against proctored assessment. An integrity design that has not read it is guessing** |
| 🟢 **marking / disclosure** | [`compose/code/aiact-50-2-*`](code/) | — | 🟢 **`P171-C`. Generated items are synthetic content and fall under Article `50`** |
| 🟢 **licence gate** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) → `licenses.config.yaml` | 🟢 **`MIT`** | 🟢 **lift the file on day one; `3` of its `19` identifiers are not SPDX, so tighten before trusting** |

🔴 **Two decisions to RECORD before writing code, both from this shelf's own measurements: (1) a
North American district engagement may not use AI to assign grades or make disciplinary decisions
(New York City, March `2026`), so the human-decision boundary is architecture, not policy; (2)
`Sakai` would FAIL `mentingo`'s gate (`T208`), so if both are in scope the gate's allowlist is a
negotiated artefact, not a default.**
## 🆕 🟢 `P170-A` — the licence gate, with a PREDICATE at last *(replaces `P169-A`, p170 — Global)*

🟢 **`P169-A` fixed the gate's denominator (enumerate the tree) and its typography (the fold). p170
found the remaining defect is the PREDICATE: it decides a legal question from a path string, and it is
wrong in both directions — by `58%` under on `penecho`, by `93%` over on `OpenEduCat` (`T213`).**

```sh
# step 0  FOLD typography before any diff (unchanged from P169-A step 0)
#         curly quotes -> ASCII, (C) for ©, http:// -> https://
# step 1  CANDIDATES: broad name match, tree-wide, exhaustive. Never root-only.
git -C "$repo" ls-tree -r --name-only HEAD | grep -Ei 'licen|copying|notice' > candidates.txt
# step 2  PREDICATE (NEW): content-test every candidate. A filename is not a grant.
while IFS= read -r p; do
  git -C "$repo" cat-file -p "HEAD:$p" \
    | grep -qiE 'Permission is hereby granted|Apache License|GNU (GENERAL|LESSER|AFFERO)|Eclipse Public License|Mozilla Public License|Redistributions of source code|Permission to use, copy, modify, and/or distribute|Educational Community License' \
    && echo "$p"
done < candidates.txt > grants.txt
# step 3  DEDUP by blob, not by path. 32 paths in penecho hold 26 distinct grants.
while IFS= read -r p; do git -C "$repo" rev-parse "HEAD:$p"; done < grants.txt | sort -u | wc -l
# step 4  MULTI-FAMILY: count families PER FILE, never first-match-wins.
#         ink-lab-LICENSE.txt bundles 3 packages and 2 families; an ordered
#         case statement reads it as whichever family it tests for first.
# step 5  ELECTION: a dual licence is an OPTION, not an obligation.
#         JSZip "MIT or GPLv3" -> elect MIT, record the election.
#         EPL-2.0 Exhibit A naming GPL-3.0-or-later is an unfilled FORM, not an election.
# step 6  Diff the root body against canonical, folded, and locate every hunk BY SECTION.
#         An APPENDIX deviation is not an operative deviation (OpenOLAT, DeepTutor).
```

🟢 **Why step `6`'s section locating matters, with both outcomes from this pass:**

| repo | folded diff vs canonical | where the hunks are | verdict |
|---|---|---|---|
| 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟡 `90` added / `159` removed | 🟢 **ALL at or after word `1410` — entirely inside the `APPENDIX`** | 🟢 **`Apache-2.0`. Operative §`1`–`9` identical. Carry the `2` attribution notices** |
| 🔴 [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟡 `40` added / `29` removed | 🔴 **`3` in §`1` and §`4(d)`, `1` in the `APPENDIX`** | 🟡 **`Apache-2.0` in effect — `0` of `4` deviations change a right, ALL `4` defeat a hash scanner** |

🔵 **Same instrument, two different answers, and neither is *"the badge says Apache so it's Apache"*.**

## 🆕 🟢 `P170-B` — the duplicate-action-label gate *(p170 — Global)*

🔴 **`ACTION JF` was registered twice in one pass, by `agents/top.md` and `intel/open-gaps.md`, for
two unrelated tasks (`T218`). Both were done, so nothing was lost — but *"`ACTION JF` was
discharged"* is now ambiguous in the permanent record.**

🔴 **p170's first three attempts at this gate were unsound, and they are recorded because the gate IS
the deliverable:**

| attempt | what it produced | why it was unsound |
|---|---|---|
| 🔴 **`grep -c` on the raw label** | 🔴 **`10` labels with `19`–`41` *"definitions"* each** | 🔴 **a label appears legitimately in every pass that JUDGES it. Counting occurrences flags the whole tree — which is `P471`: a gate that marks everything controls nothing** |
| 🔴 **the same, plus `awk '{print $2}'`** | 🔴 **the string `` `ACTION `` on every row** | 🔴 **`awk` splits on the space INSIDE the label, so the gate could not name what it flagged** |
| 🔴 **restricted to register SECTIONS** | 🔴 **flagged p170's OWN `JJ`–`JN`** | 🔴 **`README.md` summarises the register in prose and `agents/top.md` links to it; both sit inside register-titled sections and neither DEFINES anything** |
| 🟢 **restricted to register TABLE ROWS** | 🟢 **`0` duplicates among p170's own labels** | 🟢 **a definition is the row carrying the action's FALSIFIER. Prose in the same section is a reference** |

🟢 **The gate, with its reasoning in the docstring:
[`code/p170-newest-block-gate/check_action_labels.py`](code/p170-newest-block-gate/check_action_labels.py)**

```sh
python3 -I compose/code/p170-newest-block-gate/check_action_labels.py \
  README.md agents/top.md intel/open-gaps.md intel/market.md intel/trends.md \
  verticals/solutions.md repos/foundations.md repos/trending.md \
  agents/trending.md compose/patterns.md
```

🟢 **From p171 actions are registered in ONE place — `intel/open-gaps.md`, with falsifiers —
`README.md` summarises and `agents/top.md` links, neither defining.**
🟡 **Standing backlog, measured rather than hidden: `17` HISTORICAL labels are defined in a register
table in BOTH `README.md` and `intel/open-gaps.md`. They predate `T218` and are not retro-fixed. The
gate exists to stop the eighteenth.**

## 🆕 🟢 `P170-C` — the cross-block consistency gate *(p170 — Global)*

🔴 **`T216`: `OpenOLAT` is licence-verified at `verticals/solutions.md:784` and absent from the
routing table at line `39` of the same file. Append-only plus *"only the newest block is canonical"*
means a row not re-stated is lost from the compiled view while staying true in the history.**

```sh
# For each repo URL that appears anywhere in a file WITH a verified licence verdict,
# assert it also appears in that file's NEWEST routing table. Report, do not auto-fix:
# a row may be absent deliberately (refuted, archived, superseded) and that is a
# human call -- but it must be a CALL, not an omission nobody noticed.
```

🟢 **Run it over `verticals/solutions.md`, `repos/foundations.md` and `agents/top.md` — the three
files with routing tables. Pre-registered as `ACTION JM`.**

## 🆕 🟢 `P170-D` — a permissive education stack, every row licence-verified at p170

🟢 **Concrete, and every licence below was read as a BODY on the open channel this pass or last. No
row is here on the strength of a badge.**

| layer | repo | licence *(body read)* | HEAD | why this one |
|---|---|---|---|---|
| 🟢 **LMS core** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** §`1`–`9` verbatim | 🟢 `2026-10-12` | 🟢 **the only PERMISSIVE institutional LMS with `QTI`, `SCORM`, curriculum and assessment built in. Patent grant included** |
| 🟢 **lightweight / offline LMS** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | 🟢 `2026-10-12` | 🟢 offline-first — the low-connectivity LATAM and APAC deployments |
| 🟢 **SCORM interop** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | 🟢 `2026-10-09` | 🟢 **`SCORM` `1.2` / `2004` + `AICC`. The only repo on this shelf where grant-named paths and grant bodies agree exactly (`1` and `1`)** |
| 🟢 **course delivery + licence hygiene** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 `MIT` | 🟢 `2026-10-10` | 🟢 **ships `licenses.config.yaml` — `19` allowed identifiers, `13` package exceptions. Lift this file as the project's own gate** |
| 🟢 **tutoring agent** | [`ai-shifu/ai-shifu`](https://github.com/ai-shifu/ai-shifu) | 🟢 `Apache-2.0` | 🟢 **`2026-10-13` (`0` d)** | 🟢 the most active permissive tutoring agent on the shelf |
| 🟢 **spaced-repetition / recall** | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🟢 `MIT` | 🟢 `2026-10-11` | 🟢 **`MCP` server — composes into an agent runtime without a fork** |
| 🟢 **courseware / AI literacy** | 🟢 `P168-C` tier | 🟢 `MIT` | 🟢 carried | 🟢 **`53` verified locales including `es` and `pt-BR` — the India Class-`3` and Alabama mandates** |

### 🟢 How to wire it, and the two decisions to record before writing code

🟢 **1. `OpenOLAT` as the system of record; `scorm-again` at the content boundary.** `OpenOLAT` already
speaks `QTI` and `SCORM`, so `scorm-again` is for the packages it must EMIT to a client's existing
LMS — and `mentingo` emits `SCORM` `1.2` only (`gap 103`), so `2004` export belongs here.
🟢 **2. `ai-shifu` and `anki-mcp-server` behind an agent boundary, not inside the LMS.** Both are
permissive, so a fork is legally cheap; keeping them behind `MCP` keeps the `AGPL-3.0` question from
ever arising if a copyleft component is added later.
🟢 **3. Lift `mentingo`'s `licenses.config.yaml` on day one and run `P170-A` against it.** Two things
it will catch immediately, both verified this pass: `ECL-2.0` is NOT in its `19` identifiers, so
`Sakai` is refused (`T208`); and `OpenOLAT`'s body is not byte-identical to canonical `Apache-2.0`,
so a hash-matching scanner flags a clean licence.
🔴 **4. RECORD TWO DECISIONS IN WRITING, before code:**

| decision | why it cannot be deferred |
|---|---|
| 🟢 **`OpenOLAT`'s `2` attribution statements will be carried into every redistribution** | 🟢 **it is the only obligation its appendix swap creates, and it is trivial to honour and easy to lose in a build** |
| 🔴 **the scanner's hash-match failures are EXPECTED for `OpenOLAT` and `DeepTutor`** | 🔴 **`P169-A`/`P170-A` establish both are permissive in effect; without a recorded decision a scanner stops the build and someone swaps a clean component for a worse one** |

🔵 **If the engagement needs a SIS, there is no permissive option — ninth consecutive pass. The
routes are `RosarioSIS` or `openSIS-Classic` (both `GPL-2.0`, both active) or `OpenEduCat`
(`LGPL-3.0`, `1` grant file in `1 345` files, cleanest to audit). `Forma LMS` is NOT an option: a
source calls it `Apache-2.0` and it is `GPL-2.0` verbatim.**

## 🆕 🟢 `P169-A` — the licence gate, folded and tree-wide *(replaces `P168-A`, p169 — Global)*

🔴 **Why it replaces `P168-A`: both of p169's own first readings were wrong, in two different places,
and each error produced a finding that looked real. A gate that fires on typography or misses a grant
file in `docs/` is worse than no gate, because its output looks authoritative.**

**Recipe, seven steps. Every step runs on a channel confirmed open in a fresh container (p169).**

```bash
REPO=HKUDS/DeepTutor
SHA=$(git ls-remote https://github.com/$REPO HEAD | cut -c1-12)

# STEP 5 FIRST (T209): enumerate the TREE, not the root. Treeless clone - no blobs (P169-B).
git clone -q --depth 1 --filter=blob:none --no-checkout https://github.com/$REPO /tmp/t
git -C /tmp/t ls-tree -r --name-only HEAD | grep -Ei 'licen|copying|notice|legal'
#   -> root LICENSE *and* THIRD_PARTY_NOTICES.md *and* anything under docs/ or vendor/

# STEP 1: title-line family, from the body - never from a badge or a repo page
curl -sS "https://raw.githubusercontent.com/$REPO/$SHA/LICENSE" -o /tmp/body
grep -m1 -v '^[[:space:]]*$' /tmp/body

# STEP 0: FOLD before diffing (T205). SPDX texts carry 246 curly quotes and 1 (c) glyph;
#         FSF ASCII bodies carry none. Unfolded, a clean GPL-3.0 reads as 71 deviations.
fold(){ perl -CSD -pe 's/[\x{201C}\x{201D}]/"/g; s/[\x{2018}\x{2019}]/\x27/g;
                       s/\x{00A9}/(C)/g; s|http://|https://|g' "$1" \
        | tr -s '[:space:]' '\n' | grep -v '^$'; }

# STEP 2: canonical word diff. Apache from apache.org; everything else from SPDX on raw.
curl -sS https://www.apache.org/licenses/LICENSE-2.0.txt -o /tmp/canon
#   or: raw.githubusercontent.com/spdx/license-list-data/main/text/<SPDX-ID>.txt
diff <(fold /tmp/canon) <(fold /tmp/body)
```

| step | what it answers | the failure it prevents |
|---|---|---|
| 🆕 🟢 **`0`. FOLD** | 🟢 **is a difference typographic or real?** | 🔴 **`T205` — `71` phantom word hunks on a clean `GPL-3.0`** |
| 🟢 `1`. title-line family | 🟢 what does the body CALL itself? | 🔴 `Sakai` published as *"Apache-derived"* |
| 🟢 `2`. canonical word diff | 🟢 is it the licence it names? | 🔴 **`T206` — `DeepTutor`'s altered section `4(d)`** |
| 🟢 `3`. permissive-set membership | 🟢 will a real gate accept it? | 🔴 **`T208` — `ECL-2.0` and `EPL-2.0` are in NO allow-list** |
| 🟢 `4`. body-contains-its-family | 🟢 does it contain the text it promises? | 🔴 `T201` — `OpenEduCat`; `T212` — `Fedena` |
| 🆕 🔴 **`5`. ALL grant files, TREE-WIDE** | 🔴 **how many grant surfaces are there?** | 🔴 **`T209` — `openSIS-Classic`'s `GPL-2.0` lives in `docs/`; `T207` — `penecho` has `36`** |
| 🟢 `6`. resolve every pointer | 🟡 do its references exist? | 🔴 `T202` — `Chamilo`'s two `404`s |

🟡 **Honest limit: step `6` cannot complete in this container. `fsf.org` and `gnu.org` are unreachable
(`T211`), so `GPL`/`AGPL` pointers come back UNRESOLVED — which is not the same as broken, and must be
recorded as unresolved.**

## 🆕 🟢 `P169-B` — the treeless clone: inventory without blobs *(new, p169 — Global)*

🔴 **p168 answered *"which grant files exist?"* with `10` full clones: `623 MB`, `11 684` files.**
🟢 **p169 answered it for `13` repositories in `3.1 MB` — and got a strictly LARGER answer.**

```bash
git clone -q --depth 1 --filter=blob:none --no-checkout https://github.com/$REPO /tmp/t
git -C /tmp/t ls-tree -r --name-only HEAD        # every path, no blob downloaded
git -C /tmp/t log -1 --format=%cs                # HEAD date, read not inferred
curl -sS "https://raw.githubusercontent.com/$REPO/$SHA/<path>"   # only the bodies you want
```

🟢 **Use it for: does this file exist · what is in this tree · how many files · what is the HEAD date ·
which modules declare which licence.** 🔴 **Clone blobs only when you must read MANY files from one
tree.** 🔵 **The rule in one line: a path list is free, a blob is not.**
🟢 **Measured this pass: `1 345` files censused in `OpenEduCat`, `63` non-root grant files found across
`12` agent rows, `4` SIS candidates dated — all without downloading a single source file.**

## 🆕 🟢 `P169-C` — the engagement licence gate, forked from a real one *(new, p169 — all four regions)*

🔵 **Every engagement needs a licence allow-list and most are written from scratch, badly. `p169` found
a working one on this shelf and it is `1 119` bytes.**

**Recipe:**
1. 🟢 **Fork [`Selleo/mentingo`](https://github.com/Selleo/mentingo)'s `licenses.config.yaml`
   (`MIT`, so you may) as the starting allow-list: `19` identifiers, `13` package exceptions.**
2. 🔴 **Add the two licences this KB has measured as MISSING from it, each with a recorded decision:**
   - 🔴 **`ECL-2.0`** — `Sakai`, the permissive LMS route. The decision to record is `T200`'s patent
     limb: contributions by institutionally employed authors carry a narrowed grant. **Allow for USE;
     flag for CONTRIBUTION.**
   - 🔴 **`EPL-2.0`** — `penecho`'s vendored `elkjs 0.12.0` layout worker. **Allow as an unmodified,
     separately licensed component; refuse if modified.**
3. 🟢 **Add `ECL-2.0` and `EPL-2.0` to the scanner's identifier map too — `3` of `mentingo`'s `19`
   entries (`Apache`, `BSD`, `Apache License 2.0`) are not SPDX ids, so the gate matches declared
   strings and will silently miss a correctly-tagged `ECL-2.0`.**
4. 🟢 **Fill in `licenses.comment.md` — `0` bytes upstream. One line per exception: what it is, why it
   is allowed, and whether the component is modified or embedded.**
5. 🟢 **Run `P169-A` on every repo the gate admits, because the gate reads DECLARATIONS and `P169-A`
   reads BODIES. `8` of `26` bodies this KB has read deviate from their declaration.**

🟢 **Deliverable shape: a checked-in config, a one-page decision record per exception, and a CI step.
That is the form the compliance burden is already taking in these repositories — meet the client there
rather than with a policy PDF.**

## 🆕 🟡 `P169-D` — the dual-licence escape hatch, priced honestly *(new, p169 — Global)*

🔵 **For a client who wants an `AGPL-3.0` component and cannot accept `AGPL-3.0`.** 🟢 **`penecho` is
the only row on this shelf with a NAMED commercial path (`T207`), so this recipe exists — but its cost
is procurement, not engineering, and it must be said first.**

| step | what to do |
|---|---|
| 🟢 **`1`** | 🟢 **Establish which limb actually binds. Running an UNMODIFIED copy — internally or commercially — needs nothing: the project says so in `COMMERCIAL-LICENSE.md`. Most clients stop here** |
| 🔴 **`2`** | 🔴 **If the client will modify and offer it as a network service, or ship it inside a proprietary product, or combine it with AGPL-incompatible code — the commercial licence is required** |
| 🔴 **`3`** | 🔴 **Open the negotiation BEFORE the architecture depends on it. Terms are *"negotiated separately with the applicable copyright holder"*, with no published price or timeline** |
| 🟡 **`4`** | 🟡 **Handle the carve-outs separately: `elkjs 0.12.0` (`EPL-2.0`) and several `MIT` vendored modules are NOT under the repository default, per the `NOTICE`** |
| 🟡 **`5`** | 🟡 **Note the CLA and the trademark reservation: contributions are assigned on terms that let the owner keep dual-licensing, and the name, wordmark and logo are not granted with the code** |

🔴 **The alternative to price against: `Open edX`'s `AGPL-3.0` RPC carve-out behind an API boundary
(`gap 107` — a licensor statement, not counsel), which needs no negotiation at all.**


## 🆕 🟢 `P168-A` — the licence-body gate: read the grant, not the family name *(replaces the family-name check, p168 — Global)*

🔵 **What changed from `P167-D`:** 🟢 **`P167-D` replaced body-substring matching with a TITLE-LINE
probe, which is correct and cheap. `ACTION IX` ran it across `10` bodies and found that the title
line is only STEP 1: `3` of `7` recommended platforms carry a grant the title line does not describe.**

### 🟢 The gate, in the order the failures actually occur

| step | probe | what it catches | measured this pass |
|---|---|---|---|
| 🟢 **1** | TITLE-LINE family (`P167-D`) | 🟢 the family, correctly — including `GPL-3.0` §13's Affero string (`T190`) | 🟢 **`10` of `10` families correct** |
| 🆕 🟢 **2** | **word-level diff vs canonical, after whitespace normalisation** | 🟢 appended paragraphs, removed appendices, substituted clauses | 🟢 **`+615` chars in `edx-platform`, `+97/−166` words in `OpenOLAT` — both CONTROLS reproduced** |
| 🆕 🟢 **3** | **is the family name in SPDX's permissive set at all?** | 🔴 **`ECL-2.0` — a real OSI licence that no `MIT`/`Apache`/`BSD` allow-list contains (`T200`)** | 🔴 **`1` of `7`** |
| 🆕 🟢 **4** | **does the body CONTAIN the family it declares?** | 🔴 **`OpenEduCat` promises the `GPL-3.0` text and ships `0` of it (`T201`)** | 🔴 **`1` of `7`** |
| 🆕 🟢 **5** | **enumerate ALL root grant files, not the first one found** | 🔴 **`Chamilo`'s `license.txt` elects `-or-later` where `LICENSE` elects nothing (`T202`)** | 🔴 **`1` of `7`** |
| 🆕 🟢 **6** | **resolve every pointer the grant file makes** | 🔴 **`Chamilo`'s `documentation/license.html` and `credits.html` are both `404`** | 🔴 **`2` of `2` dead** |

### 🔴 The canonical channel is a dependency, and it can be denied

🔴 **`gnu.org` is a `403` POLICY DENIAL at this container's gateway, so the FSF plain text is NOT
available as canonical.** 🟢 **SPDX's `license-list-data` on `raw.githubusercontent.com` is `200`
and is what `P168-A` uses.** 🔴 **SPDX REFLOWS its text, so a byte diff against it is meaningless —
the diff MUST be word-level after collapsing whitespace, and `©`/`'`/`"` must be folded first.**
🟢 **Calibration that proves the point: `35 147` and `35 149` are the SAME `GPL-3.0` at two FSF
revisions, one URL apart (`philosophy/` → `licenses/why-not-lgpl.html`). Byte size is not identity,
and p167 was right to retire the band.**

### 🟢 Wiring it

```
for each recommended repo:
  branch := git ls-remote --symref <repo> HEAD        # the git channel, always open
  for name in LICENSE LICENSE.txt LICENSE.md COPYING COPYING.txt LICENCE license.txt:
      body := curl raw.githubusercontent.com/<repo>/<branch>/<name>   # 200 or skip
      # enumerate ALL of them - step 5 exists because Chamilo has two
  family := first title line matching a known licence name       # step 1
  diff   := word-diff(normalise(body), normalise(SPDX[family]))  # step 2
  flag if family not in PERMISSIVE_SET                           # step 3
  flag if family's own body text is absent from body             # step 4
  for each path the body references: curl it, flag 404            # step 6
```

🟡 **Cost, measured: `10` bodies over `9` repos in one pass, `0` clones, all on `raw`. This is the
cheapest gate on the shelf and it changed `3` of `7` verdicts.**

## 🆕 🟢 `P168-B` — SCORM export: verify the MANIFEST, never the feature list *(new, p168 — Global)*

🔵 **Why:** 🔴 **`mentingo`'s prose says *"can export courses as SCORM 1.2 packages"*; p166 counted
`103` `scorm_2004` markers in the tree; `gap 103` asked which was right. Both were — of different
halves of the pipeline.**

### 🟢 The probe, and it is four lines

🟢 **Read the manifest emitter and grep the EMITTED XML, not the repo:**

| probe | `mentingo` `242a9324fe48` | reads as |
|---|---|---|
| `<schemaversion>` | 🔴 **`1.2`, hardcoded at `manifest-builder.ts:30`** | 🔴 **SCORM `1.2`** |
| `xmlns:adlcp` | 🔴 **`adlcp_rootv1p2`** | 🔴 **SCORM `1.2`** |
| `xmlns` | 🔴 **`imscp_rootv1p1p2`** | 🔴 **IMS CP `1.1.2`** |
| `imsss` / `adlseq` / `adlnav` | 🔴 **`0` occurrences in the whole package** | 🔴 **no `2004` sequencing is possible** |

🟢 **One template literal, one `return`, no version parameter — so this is `1.2`-ONLY by
construction, not `2004`-untested.**

### 🔴 The lossy round trip, which is the part worth selling against

🔴 **`renderLessonResources()` filters `lesson.type === "scorm"` and re-emits each IMPORTED `SCO` as
`<resource type="webcontent" adlcp:scormtype="sco">` inside the `1.2` manifest.**
🔴 **Import a SCORM `2004` package → export the course → the output DECLARES `1.2` and the `2004`
sequencing rules were never carried. Nothing warns.**
🟢 **Recipe when a client needs `2004`: keep `mentingo` (`MIT`) for authoring and delivery, and put
`jcputney/scorm-again` (`MIT`, `1 072 B` clean licence body, verified this pass) on the runtime
side, emitting the `2004` manifest yourself. Both permissive, both auditable, neither forked.**

## 🆕 🟢 `P168-C` — the courseware tier: an AI-literacy engagement that starts translated *(new, p168 — all four regions)*

🔵 **Why:** 🟢 **`T199` found that *"open source AI agents education"* returns AI-literacy CURRICULA,
not education agents. Rather than discard them, `P168-C` places them — because `H.R. 8747` proposes
to fund exactly this in US schools and LATAM's `26%`-strategy figure demands exactly this training.**

| repo | licence *(body-read)* | what it is | wire it as |
|---|---|---|---|
| 🟢 [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **`MIT` (`1 141 B`)** | 🟢 **`12`-lesson course, `53` locales** | 🟢 **the spine — fork, strip the vendor SDK lessons, keep the structure** |
| 🟢 [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) | 🟢 **`MIT` (`1 091 B`)** | 🟢 **builds ONE agent, local LLM, no frameworks** | 🟢 **the no-cloud track for a data-resident institution** |
| 🟢 [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) | 🟢 **`MIT` (`1 070 B`)** | 🟢 **model internals → retrieval → agent runtimes** | 🟢 **the advanced track for a CS faculty** |
| 🟢 [`moodle/moodle`](https://github.com/moodle/moodle) or [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🔴 `GPL-3.0` / 🟢 `MIT` | the delivery platform | 🟢 **`mentingo` if you need `MIT` end-to-end; `Moodle` if the institution already runs it** |

🟢 **Locale coverage, verified file by file on the raw channel — this is what makes it a regional
pattern rather than a US one:** 🟢 **LATAM `es` + `pt-BR` + `pt-PT`; APAC `23` locales
(`ja ko zh-CN zh-HK zh-MO zh-TW hi bn ta te ml mr pa ne ur km kn my th vi id ms tl`); EMEA `28`
including `ar he fa tr sw` and `pcm`; `53` distinct locales in total.**
🔴 **Instrument note, and it is a trap: probing bare `zh` or bare `pt` returns `404`. Chinese and
Portuguese exist ONLY region-qualified. A locale probe that reports *"no Chinese"* is wrong.**
🟡 **Honest scoping: this is courseware, not an agent. It does not belong on the agent shelf and
`T199` says why. What it gives a studio is a `4`-week AI-literacy engagement with the content cost
already paid and the translation cost already paid.**

## 🆕 🟡 `P168-D` — the cross-pass baseline, and the denominator that actually blocks it *(amends `P166`'s churn instrument, p168 — Global)*

🔵 **What changed:** 🔴 **p166 held `ACTION IR` open believing the constraint was PASS LENGTH.
p167 agreed and solved it by committing a baseline. p168 measured it and the constraint is
COVERAGE.**

| anchor | span to p168 `t0` | changed | denominator |
|---|---|---|---|
| 🟢 `p155` commit | 🟢 **`12 h 38 min 59 s`** | 🟢 **`0`** | 🔴 **`3` of `12` rows only** |
| 🟢 `p156` commit | 🟢 **`11 h 37 min 28 s`** | 🟢 **`0`** | 🔴 **`6` of `12` rows only** |
| 🟡 `p164` commit | 🟡 `3 h 36 min 05 s` | 🔴 `1` *(`ai-shifu`)* | 🟢 **`12` — the oldest FULL-`12` anchor that exists** |
| 🟢 `p167` `t1` RECORDED | `0 h 06 min 22 s` | 🟢 `0` | 🟢 `12` |

🔵 **So an action asking for `≥6` hours at denominator `12` cannot discharge at p168 however long
the pass runs — the full-`12` sha set is only `3.6` hours old.** 🟢 **The rule this adds, and it
generalises past churn: an instrument's reach is bounded by its COVERAGE HISTORY, so a pass should
commit the full-population baseline BEFORE the question that needs it is registered, and a register
should state the denominator alongside the interval.**
🟢 **Handoff, exact: p168's `t0` is a RECORDED full-`12` baseline at `2026-10-13T06:46:52Z`. The
first pass at or after `12:46:52Z` takes the `≥6`-hour full-`12` reading with no new instrument.**

## 🆕 🟢 `P167-A` — the capability census, with the GUARD'S OWN three defects measured and closed *(amends `P166-A`, p167 — Global)*

🔵 **What changed from `P166-A`:** 🟢 **`P166-A` added comment-stripping and asked whether the
anti-claim it found was a one-repo curiosity or a class. `ACTION IU` ran it across `15` pinned trees
(`7 723` capability-term occurrences) and the answer is: a CLASS on the comment axis, a SINGLE REPO
on the language axis.** 🔴 **And running it at scale found THREE defects in the guard itself, one of
which is the exact error class this shelf exists to catch.**

### 🆕 🔴 The three defects in `P166-A`'s comment limb, each measured separately

| defect | mechanism | citation | before → after | killed |
|---|---|---|---|---|
| 🆕 🔴 **(a) marker collision** | 🔴 **`/*` inside a TypeScript template literal, `//` inside `https://`, `#` inside `#fff`** | `Selleo/mentingo` `apps/web/app/config/routeAccessConfig.ts:140` | `1 140` → `934` | 🔴 **`206` — `18.1%`** |
| 🆕 🔴 **(b) unterminated span** | 🔴 **`<code>/*</code>` in documentation HTML opens a block comment that never closes, so the span runs to EOF and EVERY later hit in that file is misreported as a comment** | `openolat/OpenOLAT` `doc/openolat-architecture.html:679` | `934` → `925` | 🔴 **`9`** |
| 🆕 🔴 **(c) language limb** | 🔴 **a missing TRAILING `\b`: `para` matched *"**para**llel"* and *"**para**meter"*, `sin` matched *"**sin**ce"* and *"**sin**gle"*** | `openolat/OpenOLAT` `src/test/java/org/olat/selenium/AssessmentTest.java:90` | `176` → `3` | 🔴 **`173` — `98.3%`** |

🔴 **Defect (c) is the finding that should sting.** 🔵 **`P164-A` exists because a naive `lti` grep
matched `facu`+`lti`+`es`. p167 then wrote the language limb that detects the anti-claim and omitted
the trailing boundary on its own stopword list — reproducing the shelf's founding error class inside
the instrument built to catch it.** 🟢 **`98.3%` of the *"non-English comment"* population was that
one missing character.**

🟢 **THE CONTROL THAT MAKES THE CORRECTION PUBLISHABLE:** 🟢 **`Selleo/mentingo` `README.md:246` —
the `T187` anti-claim — survives all three corrections unchanged.** 🟢 **So p166's headline finding
is untouched; what collapsed is only the population around it.**

### 🟢 What `ACTION IU` measured — `15` trees, `5` standards

| | measured |
|---|---|
| 🟢 capability-term occurrences | **`7 723`** across `15` pinned trees |
| 🟢 in code | **`6 798`** — `88.0%` |
| 🟡 **in a comment or doc block** | **`925`** — `12.0%` |
| 🔴 **in a NON-ENGLISH comment** | 🔴 **`3`** — `0.04%`, and **all `3` are in `Selleo/mentingo`'s README** |
| 🔴 **trees with ZERO capability terms** | 🔴 **`10` of `15`** |

🟢 **`ACTION IU`'s falsifier required `0` repositories other than `Selleo/mentingo` to carry a
capability term inside a comment. Measured: `5` repositories do** — `openedx/edx-platform` (`387`),
`openolat/OpenOLAT` (`275`), `Ed-Fi-Alliance-OSS/edfi-oneroster` (`238`), `Selleo/mentingo` (`23`),
`zijinz456/OpenTutor` (`2`). 🟢 **Falsifier SILENT: `T187` is a class on the comment axis.**
🟡 **But split the axes honestly — on the LANGUAGE axis mentingo is still the only instance on this
shelf, so the anti-claim's *foreign-language* limb remains a one-repo observation.**

### 🆕 🔴 STEP 8, new: an anti-claim is EVIDENCE, not a VERDICT — resolve it against code

🔴 **`ACTION IU` found a SECOND Polish anti-claim in mentingo that p166 never cited —
`README.md:293`, immediately under the heading *"Does Mentingo support SCORM?"*:**

> `<!-- TODO(weryfikacja): czy jest import SCORM? jeśli tak, dopisać zdanie. jeśli nie - zostaw jak jest -->`
> 🟢 *"TODO(verification): is there SCORM import? if yes, add a sentence. if not — leave as is."*

🟢 **The published prose above that comment says only: *"Mentingo can export courses as SCORM 1.2
packages."*** 🔴 **The code says otherwise, and emphatically:**

| evidence | measured |
|---|---|
| 🟢 import endpoints | **`4`** — `@Post("import/init")`, `@Post("import/tus")`, `@Patch("import/tus/:packageId")`, `@Post("import/:packageId/complete")` |
| 🟢 import worker | `apps/api/src/scorm/scorm-import.worker.ts` |
| 🟢 resumable upload service | `scorm-tus-upload.service.ts` *(tus protocol)*, `scormTusUploadService` |
| 🟢 typed job payloads | `InitScormImportBody` ×`21`, `ScormImportResult` ×`17`, `ScormImportJobData` ×`13`, `StreamedScormImportJobData` ×`12` |
| 🟢 e2e coverage | `native-archive-import-scorm.e2e-spec.ts`, `scorm.controller.e2e-spec.ts` |
| 🟢 service size | `scorm.service.ts` `2 014` LOC, `scorm.controller.ts` `518` LOC, `119` SCORM paths |

🔴 **So this anti-claim UNDERSTATES a capability that is fully in-tree.** 🔵 **`T187` read the first
anti-claim as *"upstream is telling you the capability is not there"* — and for xAPI and LTI 1.3
that reading survives, because the code channel independently reads `0` outside the comment.**
🔴 **For SCORM import it would have been WRONG. The comment is a stale documentation TODO, not a
capability statement.** 🟢 **STEP 8: every anti-claim gets a code probe for the SAME capability
before it becomes a verdict, and the verdict is the CODE's.**

### 🆕 🟡 The seventh false-positive class: the ANALOGY claim

🟡 **`zijinz456/OpenTutor` returns exactly `2` hits for `xapi`, and `0` of them are code:
`apps/api/services/analytics/events.py:1` and `:36`, both reading `xAPI-inspired`.**
🟢 **The module emits its own event schema with its own verb list and names xAPI only as the thing
it RESEMBLES.** 🔴 **Verdict: `xAPI` ABSENT in `zijinz456/OpenTutor` — not conformant, not
integrable, no LRS will accept it.** 🟡 **Also found: `OneRoster-style` ×`1` in
`Ed-Fi-Alliance-OSS/edfi-oneroster` `docs/PRD.md`, where the capability IS real, so the marker is a
trigger for a code probe and never a verdict on its own.**
🔵 **Add `(inspired|like|style|flavoured|compatible)` to the probe: it is cheap, and a client who
reads *"xAPI"* on a feature list and gets *"xAPI-inspired"* has bought an integration that does not
exist.**

🟢 **Deliverable: `P166-A`'s matrix, plus a per-hit comment/code/anti-claim/analogy classification.**
🟢 **Effort: unchanged, `2`–`4` days for a five-platform landscape.**
[`evidence/comment-guard-census.2026-10-13-p167.tsv`](../evidence/comment-guard-census.2026-10-13-p167.tsv)
[`evidence/comment-guard-defects.2026-10-13-p167.tsv`](../evidence/comment-guard-defects.2026-10-13-p167.tsv)

---

## 🆕 🟢 `P167-B` — `P166-B` AMENDED: read rostering, now entity-by-entity *(amends `P166-B`, p167 — Global; strongest in North America)*

🟢 **`ACTION IV` discharged `P166-B`'s one unshippable dependency (`gap 102`) by reading
`Ed-Fi-Alliance-OSS/edfi-oneroster`'s routes at HEAD rather than its summary.**

| field | p166 published | 🆕 p167 measured |
|---|---|---|
| 🔴 **GET endpoints** | 🔴 *"`14` GET endpoints"* | 🟢 **`24` rostering GETs — `12` entities × `2` shapes (collection + `/:id`)**. 🔴 **Neither the code nor the README says `14`** |
| 🟡 **entities** | 🟡 **unestablished — the whole of `gap 102`** | 🟢 **`12`: `academicSessions`, `gradingPeriods`, `terms`, `classes`, `courses`, `demographics`, `enrollments`, `orgs`, `schools`, `users`, `students`, `teachers`** |
| 🟡 **write-back** | 🟡 *"a separate decision this shelf has not measured"* | 🟢 **MEASURED: `router.post` / `.put` / `.patch` / `.delete` = `0` across the entire app. READ-ONLY, confirmed rather than assumed** |
| 🟢 **not a stub** | — | 🟢 **`oneRosterController.js` `264` LOC + `OneRosterQueryService.js` `594` LOC, `261` tracked paths** |
| 🟢 **authorisation** | — | 🟢 **every route carries `authorizeEndpoint('<scope>')`; `6` scopes: `users`, `orgs`, `classes`, `courses`, `enrollments`, `academicsessions`** |

🟢 **`ACTION IV`'s falsifier required that the endpoints NOT include both users and enrolments.**
🟢 **Both are present — `users` in three shapes (`users`, `students`, `teachers`) and `enrollments`
in two. Falsifier SILENT. `P166-B` is AMENDED, not withdrawn, and `gap 102` is CLOSED.**

🟢 **The wiring is unchanged from `P166-B`** — `edfi-oneroster` (Apache-2.0, body-read `10 173 B`)
in front of the district's system of record; the LMS consumes OneRoster 1.2 over HTTP rather than
through a platform plugin, keeping rostering OUTSIDE the GPL boundary (`P156-A`); LTI 1.3 carries
tools and grade passback. 🟢 **What changes is the SCOPING SENTENCE a client can now be given:**

> 🟢 **`12` rostering entities, read-only, with per-scope authorisation, on Apache-2.0.**
> 🔴 **Any write-back — enrolment changes flowing INTO the SIS — is a build, not a configuration.**

🟢 **Effort: `4`–`6` weeks for read rostering into an existing LMS, unchanged.**
[`evidence/oneroster-endpoints.2026-10-13-p167.tsv`](../evidence/oneroster-endpoints.2026-10-13-p167.tsv)

---

## 🆕 🟢 `P167-C` — read the licence BODY for an addendum, because `edx-platform`'s changes what you may build *(new, p167 — Global)*

🔵 **The problem this solves:** 🔴 **this shelf's licence gate classifies a family and stops.**
🔴 **`ACTION IW` read all `14` bodies on disk and found that `2` of them carry APPENDED text the
family name does not predict — and in one case the addendum is the most commercially significant
sentence in the file.**

🟢 **`openedx/edx-platform`, `LICENSE` `35 136 B`, AGPL-3.0 by title probe, with `10` appended lines:**

> 🟢 **"EdX Inc. wishes to state, in clarification of the above license terms, that any public,
> independently available web service offered over the network and communicating with edX's
> copyrighted works by any form of inter-service communication, including but not limited to Remote
> Procedure Call (RPC) interfaces, is not a work based on our copyrighted work within the meaning of
> the license."** 🟢 **And: *"Corresponding Source" … do not include source code files for programs
> used solely to provide those public, independently available web services.*"**

🔴 **Bare AGPL-3.0 §13 is this shelf's stop-ship gate (`P37`) precisely because a network service
triggers source disclosure.** 🟢 **This addendum carves out exactly that case: a separately
deployed service talking to Open edX over RPC is declared not a derivative work, and its source is
declared outside Corresponding Source.** 🔵 **So an architecture this shelf would have refused on
licence grounds is explicitly permitted by the licensor — IF the integration stays service-to-service
over the network and does not link into the platform.**

| 🟢 what the addendum permits | 🔴 what it does NOT touch |
|---|---|
| 🟢 **a separate AI tutoring / analytics service called over RPC or HTTP** | 🔴 **in-process code: an XBlock, a Django app, a patch, a fork — all still AGPL-3.0** |
| 🟢 **keeping THAT service's source closed** | 🔴 **modifications to `edx-platform` itself, which must still be offered to users under §13** |

🟢 **The recipe:** 🟢 **(1) classify the family from the TITLE LINE (`P167-D`); (2) `diff` the body
against the canonical FSF/ASF text for that family; (3) read every appended or removed paragraph and
record it as a TERM, not as a byte count; (4) decide the integration boundary from the addendum.**
🔴 **Second instance found: `openolat/OpenOLAT`'s Apache-2.0 body carries two *"Additional license
statement"* attribution sections (OLAT / University of Zurich, and frentix GmbH). Attribution, not a
grant change — but it is why its body is `10 982 B` and not `10 173 B`.**
🟢 **Deliverable: a per-dependency licence sheet whose rows are TERMS, not family names.**
🟢 **Effort: `1`–`2` days for a twenty-dependency closure, and it is the cheapest legal risk
reduction on this shelf.**
[`evidence/licence-bands.2026-10-13-p167.tsv`](../evidence/licence-bands.2026-10-13-p167.tsv)

---

## 🆕 🟢 `P167-D` — classify a licence by its TITLE LINE; the size band is formally broken *(replaces `P48`'s bands, p167 — Global)*

🔴 **`P48` published size bands — Apache-2.0 `11 357`–`11 358 B`, GPL-3.0 `35 121`–`35 147 B`.**
🔴 **`ACTION IW` re-derived them from all `14` bodies on disk: the published bands match NOTHING.**
🟢 **Falsifier SILENT — `T184` was drift, not an artefact of two outliers.**

| family | n | measured min | measured max | own spread |
|---|---|---|---|---|
| 🟢 `MIT` | `4` | `1 062` | `1 074` | `12 B` |
| 🔴 `PROPRIETARY` *(PageLM Community)* | `1` | `8 563` | `8 563` | — |
| 🟢 `Apache-2.0` | `4` | `10 173` | `11 408` | 🔴 **`1 235 B`** |
| 🔴 `AGPL-3.0` | `4` | `34 522` | `35 136` | 🔴 **`614 B`** |
| 🔴 `GPL-3.0` | `1` | `35 149` | `35 149` | — |

🔴 **The band test is not stale — it is UNSOUND, and one comparison shows why: `AGPL-3.0`'s measured
maximum (`35 136`) and `GPL-3.0`'s measured minimum (`35 149`) are `13 B` apart, while `Apache-2.0`'s
spread WITHIN one family is `1 235 B` — `95×` larger.** 🔵 **A discriminator whose between-class gap
is two orders of magnitude smaller than its within-class spread cannot classify. No correction to
the numbers fixes that; the instrument has to be replaced.**

🟢 **And the four mechanisms behind the spread are all measurable, none of them a terms difference
except the last:**

| mechanism | evidence | Δ |
|---|---|---|
| 🟢 `http://` vs `https://` in the FSF URLs | `ChatTutor` `34 522` vs `Echo-Loop` / `penecho` `34 523` | 🟢 **`1 B`** |
| 🟢 line re-wrapping of the *"how to apply"* block | same two bodies, `660` vs `661` lines | 🟢 **`~1 B`** |
| 🟢 the *"APPENDIX: How to apply"* section present or absent | `edfi-oneroster` `10 173` *(`0` × `APPENDIX`)* vs `DeepTutor` `11 408` | 🟡 **`~1 200 B`** |
| 🔴 **a licensor ADDENDUM** | `openolat/OpenOLAT` `+809 B`, `openedx/edx-platform` `+613 B` | 🔴 **the only one that changes TERMS** |

### 🆕 🔴 And the family probe itself has a false-positive class

🔴 **A substring probe for `"GNU AFFERO GENERAL PUBLIC LICENSE"` matches EVERY GPL-3.0 body.**
🟢 **Mechanism, cited: GPL-3.0 §13 is titled *"Use with the GNU Affero General Public License"* —
`plastic-labs/tutor-gpt`'s `LICENSE` contains the Affero string `3` times, at lines `552`, `556` and
`559`, while its title line reads `GNU GENERAL PUBLIC LICENSE`.**
🔴 **Probe the body and `tutor-gpt` reads AGPL-3.0. It is GPL-3.0.**

🟢 **`P167-D`, the replacement instrument:**

1. 🟢 **Read the TITLE LINE only** — `head -3`, matched against `GNU (AFFERO )?GENERAL PUBLIC
   LICENSE`, `Apache License` + `Version 2.0`, `MIT License`. 🟢 **Verified on all `14` bodies:
   `tutor-gpt` → GPL-3.0, `edx-platform` → AGPL-3.0, `ChatTutor` → AGPL-3.0, no misclassification.**
2. 🔴 **Never infer a family from byte size** — size is now a CORROBORATION field only.
3. 🟢 **`diff` against the canonical text and read every appended paragraph** (`P167-C`).
4. 🟡 **A title that names a family is still not a grant** — `CaviraOSS/PageLM` opens with MIT's
   grant sentence verbatim at `8 563 B` and is non-commercial and revocable (`T160`).
5. 🟢 **A missing file is a verdict, not an error** — `JushBJJ/Mr.-Ranedeer-AI-Tutor` has no licence
   body at p167 as at p166.

🟢 **Effort: minutes per dependency, and it replaces a test that could not have worked.**
[`evidence/licence-bands.2026-10-13-p167.tsv`](../evidence/licence-bands.2026-10-13-p167.tsv)

---

## 🆕 🟢 `P166-A` — the capability census, with the SIXTH false-positive class and the guard that FINDS the capability but cannot make it usable *(amends `P165-A`, p166 — Global)*

🔵 **What changed from `P165-A`:** 🟢 **`P165-A` added false-NEGATIVE guards and asked whether they
earn their keep. `ACTION IP` ran it on `moodle/moodle` (`67 589` paths) and `Selleo/mentingo`
(`4 753` paths) and the answer is `2` of `3`.** 🔴 **It also found a sixth false-positive class that
no boundary, binary or i18n guard catches, because the text is prose and it is in the repository on
purpose.**

### 🆕 🔴 The sixth false-positive class: the ANTI-CLAIM

🔴 **`Selleo/mentingo` returns exactly `1` hit for `xapi` and exactly `1` for `lti` — the SAME
line, `README.md:246`. It is inside an HTML comment, in Polish, and it reads:**

> `<!-- ETAP 3 - do potwierdzenia przez zespół, NIE publikować bez weryfikacji: … pentest,`
> `xAPI/LTI, mapowanie na NIS-2 / art. 8e KSC, retencja i usuwanie danych. -->`

🟢 **“STAGE 3 — to be confirmed by the team, DO NOT PUBLISH WITHOUT VERIFICATION.”**
🔴 **So the only hit for two standards across the whole tree is an unpublished internal roadmap item
that upstream has explicitly marked as unverified.** 🔵 **This is not a weak claim. It is an
ANTI-claim: upstream is telling you the capability is not there.**

| guard | what it kills | p166 status |
|---|---|---|
| 🟢 `\b` word boundaries | 🔴 kebab-case collisions — 🆕 **`labeled-field` ×`457` in Moodle, `changed-files`, `selected-file`, `localized-field` in mentingo** | 🆕 🟢 **`510` of `514` literal `ed-fi` hits on Moodle are ONE token; the guard takes both trees to `0`** |
| 🟢 `grep -I` | 🔴 raw bytes in assets | 🟢 kept |
| 🟢 `--exclude='*.po'` | 🔴 i18n catalogue collisions | 🟢 kept |
| 🟢 `--exclude-dir={node_modules,vendor,build,dist}` | 🔴 vendored bundles | 🟢 kept |
| 🆕 🔴 **strip HTML/code COMMENTS before counting a doc hit** | 🆕 🔴 **the anti-claim** | 🆕 🟢 **flipped `2` mentingo verdicts** |

🆕 🔴 **And note WHERE p165's and p166's collisions differ. p165 found camelCase and underscore
tokens (`ableExtendedFilter`, `uploadedFile`, `lastModifiedField`); p166 found kebab-case
(`labeled-field`, `changed-files`). The class spans at least three naming conventions and the
DOMINANT token is different in every codebase**, so a reviewer who memorised p165's token list
would not have recognised Moodle's. 🟢 **Never carry a token denylist between repositories; carry
the GUARD.**

### 🟢 Which false-negative guard earned its keep — `2` of `3`

| guard | verdicts changed | the finding |
|---|---|---|
| 🔴 **spec-URL probe** | 🔴 **`0`** | 🔵 **It CORROBORATED every verdict and flipped none. `imsglobal.org/spec/lti` ×`287` and `purl.imsglobal.org` ×`441` on Moodle, where the name probe had already answered; `imsglobal.org/spec/oneroster` ×`0` and `ed-fi.org` ×`0`, which is an absence confirmed on a second, language-independent channel.** 🟢 **Keep it — a corroborated absence is worth more to a client than a bare one** |
| 🟢 **sibling probe** | 🟢 **`2`** | 🟢 **`moodlehq/moodle-enrol_oneroster` EXISTS. Moodle's OneRoster goes ABSENT → IMPLEMENTED-IN-SIBLING. And mentingo's SCORM PLAYER is `jcputney/scorm-again` (MIT), pinned `3.0.4`** |
| 🟢 **config-vs-code split** | 🟢 **`2`** | 🟢 **mentingo's xAPI and LTI 1.3 go from *"1 hit, indeterminate"* to ABSENT-with-an-anti-claim. On Moodle it changed nothing: the hits are in `public/lib/lti1p3`, `public/mod/scorm`, `public/lib/xapi` — code, not manifests** |

🟢 **`ACTION IP`'s falsifier is SILENT: `4` verdict changes across `2` guards.**
🔵 **But `T176`'s lesson repeats with a new face — the guard that earns nothing on one axis
(spec-URL) is the one that makes an ABSENCE defensible, which is a different kind of value from
flipping a verdict.**

### 🆕 🔴 STEP 7, new and non-negotiable: run `P164-D` on the SIBLING, immediately

🔴 **The sibling probe is the guard most likely to flip a verdict TO a capability — and that is
exactly when it is most dangerous, because a flip reads like good news.**

🟢 **`moodlehq/moodle-enrol_oneroster`, measured the moment it was named:**

| field | value | consequence |
|---|---|---|
| 🟢 existence | 🟢 **EXISTS**, `134` tracked paths | 🟢 the capability is real |
| 🔴 **HEAD date** | 🔴 **`2021-01-20`** | 🔴 **`2 091` days stale — `11.6×` `P164-D`'s `180`-day threshold** |
| 🔴 **licence** | 🔴 **`GPL-3.0`, `35 149 B` body-read** | 🔴 **no permissive path, and `P37`'s stop-ship gate applies** |

🔴 **So Moodle's OneRoster verdict is IMPLEMENTED-IN-SIBLING and UNUSABLE in the same breath.**
🟢 **Report both, in that order, always.** 🔵 **A verdict of *"yes, via a plugin"* that omits
*"last touched in January 2021, and it is GPL"* is worse than a verdict of *"no"*, because the
client budgets for integration instead of for a build.**

🟢 **Deliverable: the per-platform matrix of `P165-A`, plus a SIBLING row carrying HEAD date, age in
days, tracked paths and licence family for every sibling named.** 🟢 **Effort: unchanged, `2`–`4`
days for a five-platform landscape.**

---

## 🆕 🟢 `P166-B` — OneRoster rostering on a PERMISSIVE licence, for a platform that has none *(new, p166 — Global; strongest in North America)*

🔵 **The problem this solves:** 🔴 **`P165-B` priced OneRoster rostering as *"bespoke, never
assume"* because OpenOLAT measured `0`. `ACTION IP` now measures `0` in `moodle/moodle` too, and
mentingo's `0` as well — so `3` of the `3` platforms this shelf recommends have NO OneRoster.**
🔴 **The one Moodle plugin that does it is `GPL-3.0` and `2 091` days stale.**
🟢 **But the shelf already held the answer, and nobody had composed it: `ACTION IS` found it on
the shelf at `89` hits before p166 measured anything.**

| layer | choice | licence | measured basis |
|---|---|---|---|
| 🟢 **OneRoster server** | 🟢 [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`**, body-read `10 173 B` | 🟢 **HEAD `7442047`, `2026-10-12` — `1` day old. `261` tracked paths. Serves **OneRoster 1.2** over `14` GET endpoints** |
| 🟢 **LMS / system of record** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **`Apache-2.0`** | 🟢 **LTI 1.3 in-tree, `145` files / `18 067` LOC (`T171`)** |
| 🟡 **or, if Moodle is already deployed** | 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 **`GPL-3.0`** | 🟢 **LTI 1.3 `423` paths, SCORM `166`, xAPI `99` — all in-tree (p166)**. 🔴 **OneRoster and Ed-Fi `0`** |
| 🟢 **content interop** | 🟢 **SCORM, in-tree on both** | 🟢 — | 🟢 **Moodle `public/mod/scorm` `121` paths; OpenOLAT `65` Java files** |
| 🔴 **do NOT use** | 🔴 [`moodlehq/moodle-enrol_oneroster`](https://github.com/moodlehq/moodle-enrol_oneroster) | 🔴 **`GPL-3.0`** | 🔴 **`2 091` days stale. `P164-D` says drop it** |

🟢 **Wiring:** 🟢 **(1) stand `edfi-oneroster` up as the rostering API in front of the district's
system of record — it is Apache-2.0, so it can be relicensed into a client product; (2) the LMS
consumes rosters from it over OneRoster 1.2 rather than through a platform plugin, which keeps the
rostering surface OUTSIDE the GPL boundary (`P156-A`); (3) LTI 1.3 carries tools and grade
passback, in-tree on both candidate platforms; (4) `P164-C`'s provenance port and `P163-C`'s off
switch ship with any evaluative AI, not after.**

🟢 **Why it holds up in a room:** 🟢 **it is the first composition on this shelf that gives a client
OneRoster rostering with no copyleft obligation and no abandoned dependency.** 🔵 **Strongest in
North America, where OneRoster is the de-facto district rostering expectation and where Oklahoma's
and Maryland's human-oversight bills and Colorado `SB 26-189`'s safe harbour (`T177`) all land on
the same build.**
🟡 **Honest scoping note: `edfi-oneroster` serves 🔴 ~~`14`~~ → **`24`** GET endpoints over `12` entities — this is READ rostering, and p167 measured `0` write routes (`T189`, superseded by `P167-B`).**
🔴 **Write-back, and Ed-Fi ODS itself, are a separate decision this shelf has not measured.**
🟢 **Effort: `4`–`6` weeks for read rostering into an existing LMS.**

---

## 🆕 🟢 `P165-A` — the capability census, corrected for BOTH its biases *(amends `P164-A`, p165 — Global)*

🔵 **The problem this solves:** 🟢 **`P164-A` guarded against FALSE POSITIVES and was right to —
`620` naive `Ed-Fi` hits on OpenOLAT, `0` real.** 🔴 **p165 established that the same instrument is
biased in the OPPOSITE direction too, and a probe correcting only one bias still gives a client the
wrong answer — in `T142`'s case a FALSE ABSENCE.**

🟢 **The recipe:**

0. 🆕 🟢 **GREP THE SHELF FIRST.** 🔴 **p165 re-derived six findings this KB already held, because
   it measured before it read (`T175`).** 🟢 **Before any clone: grep the KB for the platform, the
   standard and the instrument. It is the cheapest step and it was the one skipped.**
1. 🟢 **Pin the tree** — `git ls-remote --symref`, then `git clone --depth=1`.
   🔵 **Plain depth-1 for content work, not blobless** *(`P164-B`)*. 🔴 **Resolve the default
   branch; do not assume `main` — OpenOLAT and edx-platform are both `master`.**
2. 🟢 **Guard the FALSE POSITIVES — five classes now:**

   | guard | class it kills |
   |---|---|
   | 🟢 `\b` word boundaries | 🔴 `facu`*`lti`*`es-icon.svg` *(p164)* and 🆕 **the `-ed`+`fi` camelCase collision: `ableExtendedFilter` ×`577`, `lastModifiedField`, `uploadedFile` (`T170`)** |
   | 🟢 `grep -I` | 🔴 raw bytes in PNG/JPEG assets *(p164)* |
   | 🟢 `--exclude='*.po'` | 🔴 Danish `Samlet` matching `saml` *(p164)* |
   | 🟢 `--exclude-dir={node_modules,vendor,build,dist,static/js}` | 🔴 vendored bundles — xAPI's only OpenOLAT hits were inside `pdf.js` build artefacts |

   🔴 **Keep all of them even when one contributes nothing: on `lti` in OpenOLAT boundaries did
   `93%` and binaries `0.3%`; on OpenEduCat the weighting was reversed (`T176`).**
3. 🆕 🔴 **Guard the FALSE NEGATIVES, which `P164-A` did not address:**

   | risk | fix |
   |---|---|
   | 🔴 **naming convention** | 🔴 **`lti_1p3` (Python/Django, `15` files in edx-platform) returns `0` in OpenOLAT, which implements LTI 1.3 in `145` files as `LTI13`.** 🟢 **Probe the SPEC URL — `imsglobal.org/spec/lti` — which is language-independent and hits both** |
   | 🔴 **plugin architecture** | 🟢 **`T142`. Read migration and config filenames: `..._move_course_edit_lti_fields_enabled_flag_model_to_lti_consumer.py` names its own sibling** |
   | 🔴 **config vs code** | 🔴 **edx-platform's only SCORM hits are `envs/mock.yml`; its xAPI hits are `requirements/*.txt`, `uv.lock`, a migration, an ADR. Declaring a dependency is not implementing a standard** |
4. 🟢 **Report FOUR verdicts:** 🟢 **IMPLEMENTED-IN-TREE · IMPLEMENTED-IN-SIBLING *(name the repo
   AND read its licence)* · CONFIG-ONLY · ABSENT.**
5. 🔴 **Licence every sibling you name.** 🟢 **This step produced `T172`: the Open edX constellation
   is AGPL at every layer, so "use the plugin" does not escape the gate.** 🟢 **Corroborate on
   PyPI/npm, which agreed with all three `LICENSE` bodies.**
6. 🟢 **Quantify what you find.** 🔵 **"LTI 1.3 is present" and "LTI 1.3 is `145` files and
   `18 067` LOC of platform-side implementation" are different sentences in an estimate.**

🟢 **Deliverable: a per-platform matrix — standard × naive × guarded × path hits × verdict ×
implementing repo × that repo's licence — plus the TSV.** 🟢 **Effort: `2`–`4` days for a
five-platform landscape.**

## 🆕 🟢 `P165-B` — standards-based AI assessment on a PERMISSIVE licence *(new, p165 — Global; strongest in EMEA and North America)*

🔵 **The problem this solves:** 🔴 **every prior assessment pattern here had to trade capability
against licence. Open edX has the interop surface and is AGPL at every layer (`T172`); Moodle is
GPL-3.0; OpenEduCat has no standards surface at all (`T161`).** 🟢 **`T171` measured a platform
that resolves the trade-off.**

| layer | choice | measured basis |
|---|---|---|
| 🟢 **platform** | 🟢 **[`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT), `Apache-2.0`** | 🟢 **licence body-read; HEAD `e4be14f0`, `2026-10-12`, `25 823` paths** |
| 🟢 **tool interop** | 🟢 **LTI 1.3, in-tree** | 🟢 **`145` files / `18 067` LOC: `LTI13Platform`, `LTI13Dispatcher`, `LTI13Key` (JWKS), `LTI13DeepLinkingEnum`, `LTI13ContentItem`** |
| 🟢 **content interop** | 🟢 **SCORM, in-tree** | 🟢 **`65` Java files: `ScormCourseNode`, `ScormAssessmentHandler`, `ScormAssessmentConfig`** |
| 🟢 **grading provenance** | 🟢 **port OpenOLAT's own `o_ai_essay_correction`** | 🟢 **`T165` (p164): already persists `a_prompt_template_version`, `a_content_hash_at_call`, `a_tier`, and the answer as an immutable `@Lob`** |
| 🟢 **rubric as data** | 🟢 **`P158-A`** | 🟢 **precondition for re-grading an old submission against the rubric it was actually graded by** |
| 🟢 **the off switch** | 🟢 **`P163-C`** | 🟢 **auditable disable path for the grader** |
| 🟢 **retention** | 🟢 **`P161-B`** | 🟢 **~`4` hours, and mandatory wherever provenance is retained** |
| 🔴 **what you must BUILD** | 🔴 **OneRoster / Ed-Fi rostering, and xAPI** | 🔴 **measured ABSENT (`T170`, `T171`). Price as bespoke; never assume** |

🟢 **Wiring:** 🟢 **(1) OpenOLAT is the system of record AND the LTI 1.3 platform, so external
tools attach as tools; (2) the AI grader runs OUTSIDE core as an LTI 1.3 tool — which satisfies
`P160-B`'s *"keep the evaluative action outside core"* rule by a STANDARD rather than a convention;
(3) grades return over AGS line-item/score endpoints, present in-tree; (4) every correction writes
prompt-template version, content hash and tier, ported from `o_ai_essay_correction`; (5) the rubric
is a versioned data artefact (`P158-A`); (6) `P163-C`'s off switch and `P161-B`'s retention job
ship WITH it, not after.**

🟢 **Why it holds up in a room:** 🟢 **the regulator's likely question — *which prompt graded this
student, against which rubric, and who could switch it off* — is answered by a schema that already
ships upstream, on a platform a studio can relicense into a client product, with the two standards
that carry most integrations implemented in-tree.**
🔵 **Strongest in EMEA (Annex III point 3 evidence posture; OpenOLAT is Swiss-originated) and in
North America, where Colorado `SB 26-189`'s deemed-compliance safe harbour requires exactly a
documented human-review-and-correction process (`T177`).**
🟢 **Effort: `8`–`12` weeks for a graded pilot on one course, including retention job and off
switch.** 🔴 **Add rostering only against a measured requirement.**

## 🆕 🟢 `P164-A` — the capability-claim audit *(new, p164 — Global)*

🔵 **The problem this solves:** 🔴 **`ACTION IJ` measured three vendor-stated interoperability
standards on `openeducat/openeducat_erp` and found `0` of `3` implemented — while a naive grep
reported `23` hits.** 🔴 **A client inherits claims like these from a vendor page, an RFP answer
or a previous integrator, and the cost of discovering they are false lands in week six.**

🟢 **The recipe, which runs in minutes per repository and needs no API:**

1. 🟢 **Establish the repo exists and pin the tree** — `git ls-remote --symref`, then
   `git clone --depth=1 --filter=blob:none --no-checkout`. 🟢 **Record HEAD sha, default branch
   and last-commit date in the report; a capability claim without a tree is not checkable.**
2. 🟢 **Path census first** — `git ls-tree -r --name-only HEAD`. 🟢 **Costs `236 KB` on a
   `1 345`-path repo and often answers the question outright.**
3. 🔴 **Then the content sweep, and use a PLAIN `--depth=1` clone for it, not the blobless one**
   *(`P164-B`: checking out a blobless clone fetches blobs one at a time and is slower than
   downloading everything once).*
4. 🟢 **Grep with all three guards, because each one caught a real false positive here:**

   | guard | the false positive it kills |
   |---|---|
   | 🟢 `grep -I` *(skip binaries)* | 🔴 `lti` matched raw bytes in `2` PNG + `2` JPEG assets |
   | 🟢 `\b` word boundaries | 🔴 `facu`*`lti`*`es-icon.svg` ×14; `requir`*`ed-fi`*`eld` in a comment |
   | 🟢 `--exclude='*.po'` *(i18n catalogues)* | 🔴 Danish `Samlet` (*"total"*) matched `saml` ×`10` |

5. 🟢 **Probe the sibling-repository hypothesis before concluding** — 🔵 **the capability may
   legitimately live elsewhere.** 🟢 **`git ls-remote --symref` against the obvious names costs
   seconds; five candidates were ABSENT here, which is what made the verdict safe.**
6. 🟢 **Report the three outcomes separately: IMPLEMENTED, ABSENT, or ABSENT-FROM-OPEN-TREE
   (may exist in a commercial edition).** 🔵 **The third is the honest verdict for OpenEduCat and
   it is the one a client can act on without accusing a vendor of lying.**

🟢 **Deliverable: a one-page table per platform — claim, path hits, verified hits, verdict —
plus the TSV.** 🟢 **Effort: `2`–`4` days for a five-platform landscape.**
🔵 **Why it sells: it is cheap, it is adversarial in the client's favour, and it produces a
procurement artifact rather than an opinion.**

---

## 🆕 🟢 `P164-C` — pin evaluative-AI provenance by PORTING OpenOLAT's schema *(replaces `P163-B`'s build, p164 — Global; strongest in EMEA)*

🔵 **What changed from `P163-B`:** 🟢 **`P163-B` designed this. `ACTION IK` found it already
SHIPPED, in Apache-2.0, in production** *(`T165`)*. 🔵 **A port of working code is a far easier
sell than a bespoke compliance build, so the pattern is restated around the reference
implementation.**

🟢 **The reference, read at `openolat/openolat` HEAD `e4be14f0`,
`EssayAiCorrection.java:120-127`, `@Table(name = "o_ai_essay_correction")` — one row per graded
correction:**

| column | what it pins | why a regulator cares |
|---|---|---|
| 🟢 `a_prompt_template_version` *(40)* | WHICH prompt graded this answer | 🟢 the instructions governing the model are part of the documentation obligation |
| 🟢 `a_content_hash_at_call` *(64)* | WHICH rubric content it was graded against | 🟢 editing a rubric later cannot silently rewrite a past mark |
| 🟢 `a_tier` | the length tier assigned | 🟢 makes the pre-filter's decision auditable |
| 🟢 `a_student_answer` *(`@Lob`, `updatable = false`)* | the answer itself, immutable | 🟢 the artifact cannot drift after the fact |

🟢 **The upstream comment is itself the design rationale worth quoting to a client: these fields
*"used to live on `o_ai_usage_log`"* and were moved because *"they belong to the correction,
which is the context of the AI call"*.** 🔵 **Audit provenance belongs on the graded artifact,
not on the cost ledger.**

🟢 **How to wire it, per platform on this shelf:**

| target | the gap | the port |
|---|---|---|
| 🔴 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) *(MIT)* | 🔴 Langfuse resolves the judge prompt FIRST; repo YAML is a silent, schema-unchecked fallback (`T156`) | 🟢 **Add `prompt_source` (`remote`\|`repo`), `prompt_version` and `prompt_sha256` to `ai_mentor_judgements`, written at judgement time.** 🟢 **Then make the `.catch(() => undefined)` fallback LOUD: record the substitution rather than swallowing it** |
| 🔴 [`moodle/moodle`](https://github.com/moodle/moodle) *(GPL-3.0)* | 🔴 the effective system instruction is admin `actionconfig` JSON on `ai_providers`; `ai_action_register` stores `model`, `prompttokens`, `completiontokens` — **no prompt identity** (`T164`) | 🟢 **Add an instruction hash column to `ai_action_register` and write it in `abstract_processor`.** 🟢 **One column; it makes every Moodle AI action reconstructable** |
| 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) *(Apache-2.0)* | 🟢 **nothing — this IS the reference** | 🟢 **Use it as the upstream exemplar in the client's design review** |

🟢 **Why `OpenOLAT` is the one to start from:** 🟢 **Apache-2.0 with a patent grant, a `1.4 MB`
sparse checkout for the whole AI subsystem (`107` Java files), and a schema that already passed
someone's review.** 🔵 **The engagement is *"port a proven audit schema into your LMS"*, not
*"let us invent your compliance model"*.**

🟢 **Effort: `2`–`3` weeks per platform.** 🟡 **Honest scoping note: this buys RECONSTRUCTABILITY,
which is one input to an Article 12 / Article 14 story — not a compliance certificate.**
🔵 **And per `T163` the Annex III deadline may now be `2027-12-02`, which makes this
*do it properly* work rather than *do it yesterday* work.**

---

## 🆕 🟢 `P164-D` — the maintenance-first shortlist *(new, p164 — Global)*

🔵 **The problem this solves:** 🔴 **`T149` closed the `★` column permanently: this session
cannot read a star count for any third-party repository, and `T150` showed the secondary channel
disagreeing with itself by `>2×`.** 🔴 **So the usual shortlist heuristic — *"pick the
most-starred"* — is unavailable AND was never the right question.**

🟢 **The substitute, measured for all twelve shelf rows this pass at `3 060 KB` total
(`P164-A`'s recipe in [`repos/foundations.md`](../repos/foundations.md)):**

| signal | command | what it tells an engagement |
|---|---|---|
| 🟢 **HEAD commit age** | `git log -1 --format=%cI` on a blobless clone | 🟢 **is anyone still here?** `3` of this shelf's `12` rows are `277`, `334` and `378` days old |
| 🟢 **Tag count + latest tag** | `git ls-remote --tags` | 🟢 **release DISCIPLINE.** `118` tags (mentingo) is a team; `0` tags is a prototype — `3` of `12` have none |
| 🟢 **Tracked paths** | `git ls-tree -r --name-only HEAD \| wc -l` | 🟢 **is it a project or a prompt?** One row has `12` files |
| 🟢 **Existence** | `git ls-remote --symref` *(`P54`)* | 🟢 survives the `curl -sI` trap, which `403`s on every repo in this session |

🟢 **Apply as a filter before any licence or capability work:** 🔴 **drop anything over `~180`
days stale unless it is a spec or a frozen reference** 🟢 **· prefer tagged releases for anything
a client will depend on** 🟢 **· read the licence body only for what survives** *(licence reads
are the expensive step; this ordering saves most of them).*

🔵 **Why this is better than stars even where stars ARE available:** 🟢 **a star count measures
attention at an unknown past moment; a HEAD date and a tag list measure whether the project will
still be there at the end of the engagement.** 🟢 **`T159`.**

---

## 🟢 `P163-A` — make a graded-AI pre-filter fair across writing systems *(new, p163 — Global; strongest in APAC and EMEA)*

🔵 **The problem this solves:** 🟢 **`ACTION IG` found OpenOLAT's two graded-path gates passing
valid answers in nine scripts** — 🔴 **but with `5×` less tolerance for Devanagari and `10×` less
for astral Han than for English, and with `0` non-Latin regression tests to stop that drifting
into refusals.** 🔵 **A gate that refuses an answer never reaches a human, so this is an ACCESS
control, not a quality one.**

🟢 **The repos and the measured facts, all at `openolat/openolat` HEAD `e4be14f0`:**

| component | what it is | the measured defect |
|---|---|---|
| 🟢 `GibberishPreFilter.java` *(124 LOC)* | letter-ratio floor `0.45` + trigram-entropy floor `1.5` | 🔴 `Character.isLetter()` is false for `Mn`/`Mc`, so Devanagari matras and Arabic harakat are not letters. Vocalised Arabic margin **`0.102`** vs English **`0.526`** |
| 🟢 the same, `letterRatio()` | `letters` per CODE POINT ÷ `text.length()` in CODE UNITS | 🔴 astral Han scores exactly **`0.500`**; **`5`** ideographic full stops push an 18-ideograph answer under the floor |
| 🟢 `AiGradingTier.java` *(123 LOC)* | word count, with a CJK `chars/3` branch | 🔴 `isCJK` lists `3040–30FF`, `4E00–9FFF`, `AC00–D7AF` only. Ext A, Compatibility Ideographs and NFD Jamo fall off it. 🔴 Thai has no branch at all and is undercounted **`~14×`** |
| 🔴 `GibberishPreFilterTest.java` | the regression net | 🔴 **`6` cases: English, German, mash, symbols, blank, short. ZERO non-Latin** |
| 🔴 `AiGradingTierTest.java` | the regression net | 🔴 **its only CJK cases are `"好".repeat(150)` and `"字".repeat(300)`** — one repeated character, which is not language |

🟢 **How to wire it, in the order that survives review:**

1. 🟢 **Port the corpus first, as TESTS, not as a patch.**
   [`compose/code/p163-script-equity-gate/`](code/p163-script-equity-gate/README.md) ships a
   Python replication validated against **all `15` upstream oracle cases** plus a nine-script
   corpus of content-matched answers. 🟢 **Those nine rows go straight into
   `src/test/java/org/olat/core/commons/services/ai/essay/` as JUnit cases.** 🔵 **They PASS today
   — which is exactly why they are contributable: a test that locks in current correct behaviour
   is an easy merge, and it is the thing that makes the later fixes safe.**
2. 🟢 **Fix `letterRatio()`'s denominator** — count both numerator and denominator in code
   points (`text.codePointCount(0, text.length())`). 🟢 **One line; it moves astral Han from
   `0.500` to `1.000` and removes the `10×` margin collapse.**
3. 🟢 **Count combining marks as letters for the ratio's purpose** — a `Mn`/`Mc` code point is
   part of a letter, not symbol spam. 🟢 **`Character.getType(cp)` against
   `NON_SPACING_MARK`/`COMBINING_SPACING_MARK`.** 🟢 **This moves vocalised Arabic from `0.552` to
   `~0.99` and Hindi from `0.591` to `~0.98`, and it does NOT weaken the control: the symbol-spam
   case stays rejected at `0.000` because digits and punctuation are neither letters nor marks.**
4. 🟢 **Extend `isCJK`** with `3400–4DBF` (Ext A), `F900–FAFF` (Compatibility),
   `20000–2A6DF` (Ext B) and `1100–11FF` (Jamo).
5. 🟢 **Give Thai, Khmer, Lao and Burmese a branch.** 🔵 **They have no inter-word spaces, so
   `split("\\s+")` is meaningless on them. 🟢 **The `chars/3` heuristic already in the file is the
   cheap, consistent answer; a segmenter (ICU `BreakIterator`) is the correct one.** 🟡 **Pick the
   heuristic for parity with CJK and say so in the comment.**
6. 🟢 **Re-run the nine-script corpus and confirm the controls still reject.**

🟢 **Why it is billable and upstreamable at once:** 🟢 **Apache-2.0 with a patent grant, a `7.0 MB`
sparse working tree, `~400` LOC of production code in scope, and a test suite whose gap is
demonstrable in one command.** 🔵 **An engagement that contributes steps 1–4 upstream and keeps
step 5's segmenter as client work gets goodwill and a differentiator from the same budget.**

🟢 **Effort: `1.5`–`2` weeks** *(step 1 alone is `2`–`3` days and is worth shipping on its own)*.

---

## 🟡 `P163-B` — pin the provenance of an evaluative prompt *(new, p163 — Global; strongest in EMEA)*

🔵 **The problem this solves:** 🔴 **`T156` — `Selleo/mentingo` fetches its AI judge's system
prompt from an external prompt-management service FIRST and treats the repository's own template
as a silent fallback, skipping the schema check on the remote path.** 🔴 **So for a high-risk
Annex III evaluative feature, the instructions that governed a given mark are not in the artifact
store and are not recorded with the mark.** 🔵 **And this is the DEFAULT integration shape for
prompt-management tooling, so the pattern is reusable far beyond this repository.**

🟢 **The four facts to put in front of a client, all at `242a9324`,
`apps/api/src/ai/services/prompt.service.ts:275-293`:**

| # | fact |
|---|---|
| 1 | 🔴 remote-first: `langfuseClient.prompt.get(id)` is tried before `this.prompts.get(id)` |
| 2 | 🔴 the remote branch compiles `vars as Record<string,string>` and **never reaches** the `Value.Check(prompt.varsSchema, vars)` that guards the local branch |
| 3 | 🔴 activation is by env var presence (`LANGFUSE_PUBLIC_KEY` + `LANGFUSE_SECRET_KEY`), `baseUrl` from `LANGFUSE_BASE_URL`/`LANGFUSE_HOST`, default `http://localhost:3002` |
| 4 | 🔴 `.catch(() => undefined)` — an outage substitutes a different prompt **silently** |

🟢 **The recipe, and every piece of it already exists in the repo:**

1. 🟢 **Record the prompt identity ON the judgement.** 🟢 **`ai_mentor_judgements` already stores
   `max_score_at_judgement` per criterion for exactly this reason — editing a rubric later must
   not rewrite a past mark.** 🟢 **Add `prompt_source` (`'repo'` | `'remote'`),
   `prompt_version` and `prompt_sha256` alongside it.** 🔵 **The precedent is in the schema; this
   is applying the platform's own principle to the prompt.**
2. 🟢 **Make the resolution order a CONFIGURED decision, not an accident of env vars.** 🟢 **A
   `PROMPT_SOURCE` setting with three values — `repo-only`, `repo-preferred`, `remote-preferred` —
   defaulting to `repo-only` for evaluative capabilities.**
3. 🟢 **Apply `Value.Check` on BOTH branches.** 🟢 **One moved line; it closes fact 2 outright.**
4. 🟢 **Fail CLOSED on an evaluative capability.** 🔴 **A silent fallback is acceptable for a
   welcome message and not for a mark.** 🟢 **For `judgePrompt`, a remote-fetch failure under
   `remote-preferred` should refuse to grade rather than grade under different instructions.**
5. 🟢 **Emit the Annex IV artifact.** 🟢 **A per-deployment report: every prompt id, its source,
   its hash, and the count of judgements rendered under each.** 🔵 **This is the deliverable a
   regulator or an appeal actually asks for, and nothing else in the stack produces it.**

🟢 **Why it is the strongest EMEA deliverable on this shelf:** 🟢 **two of the three platforms in
the Annex III evaluative tier are EU/EEA-built, and the one with the MOST permissive licence is
the one with this gap.** 🔵 **The engagement is small, defensible, and jurisdiction-neutral — an
auditability control sells into the North American *"regulatory vacuum"* on the same evidence.**

🟢 **Effort: `3`–`4` weeks**, of which steps 2–4 are a few days and step 5 is most of the work.

---

## 🟢 `P163-C` — an auditable off switch for an AI grader *(new, p163 — Global; strongest in LATAM and APAC)*

🔵 **The problem this solves:** 🔴 **`T157` — `Selleo/mentingo` has NO off switch for its AI
judge.** 🔴 **`AI_RUNTIME_SOURCES` is `{CORE, LUMA}` with no `OFF` member, and
`resolveSource()`'s `enabled: false` branch returns `CORE` — it changes the PROVIDER, it does not
stop the grading.** 🟡 **The only way to stop it is to leave a rubric unconfigured, which throws
`aiJudgeConfigurationMissing`** — 🔵 **an off switch by omission, not a control anyone can find,
document or audit.**

🟢 **The contrast that makes the case:** 🟢 **OpenOLAT's `essay-grading` flag SHIPS `false`**
*(`T145`)*. 🔵 **Same regulatory tier, same evaluative function, opposite default.**

🟢 **The recipe:**

1. 🟢 **Add `OFF` to the source enum.**
   `AI_RUNTIME_SOURCES = {OFF:"off", CORE:"core", LUMA:"luma"}`. 🟢 **Then
   `resolveSource()` returns `OFF` when `capabilityStatus?.enabled === false`,** and
   `judgeMentor()` throws a typed `AiCapabilityDisabledException` instead of calling
   `judgeCore()`. 🔵 **The three-line change is the whole mechanism; everything below is what makes
   it auditable.**
2. 🟢 **Default evaluative capabilities to OFF.** 🟢 **`AiMentorJudge` ships disabled; an
   administrator turns it on deliberately, and that act is what the audit trail records.**
3. 🟢 **Make the switch per-tenant.** 🟢 **All `7` judge tables already carry `tenant_id` with an
   RLS default and an FK to `tenants`** *(`T145`)* — 🟢 **so a per-tenant flag needs no new
   isolation model, only a row.** 🔵 **This is what a LATAM or APAC rollout actually needs: one
   institution's policy committee can disable AI grading without affecting another's.**
4. 🟢 **Log every transition.** 🟢 **Who enabled or disabled grading, for which tenant, when, and
   under which `prompt_sha256`** *(from `P163-B`, which is why the two compose)*.
5. 🟢 **Surface it in the learner-facing path.** 🟢 **When the judge is `OFF`, the lesson completes
   through the human-marking route rather than erroring** — 🔵 **otherwise the switch is a kill
   switch nobody dares use, which is the same as not having one.**

🟢 **Why it lands in LATAM and APAC first:** 🔴 **LATAM has roughly three institutions in four
using AI with NO published policy** *(UNESCO IESALC `26%`, DEC `30%` — corroborated this pass)*.
🟢 **An institution in that position needs an evaluative feature it can switch off while the
policy is written, and `T157` says the MIT platform cannot do it today.** 🟢 **In APAC, Singapore's
exams are proctored with AI prohibited while `75%` of its teachers use AI in their work — a
boundary that is only enforceable if the grading feature has a real, documented off state.**

🟢 **Effort: `2`–`3` weeks.** 🟢 **Composes directly with `P162-D` (multi-tenant AI assessment on
MIT) and `P163-B` (prompt provenance): together they are a single coherent Annex III readiness
engagement on a permissive platform** — 🔵 **`P162-D` builds the feature, `P163-C` lets the client
turn it off, `P163-B` lets them prove what it did.**

---

## 🆕 🟢 `P162-B` — close the injection gap on the path that GRADES *(new, p162 — Global; strongest in EMEA and APAC)*

🔵 **The problem this solves:** 🔴 **`T144` — OpenOLAT hardens the AUTHOR's course content in code
and defends the STUDENT's answer with a sentence in a system message. The evaluative path is the
Annex III path, and it is the one with an adversarial author.** 🟢 **The platform already contains
everything the fix needs; nothing has to be invented.**

🟢 **What exists, measured in the tree at `e4be14f0`:**

| asset | where |
|---|---|
| 🟢 `AiContentHardener.harden()` — `14` injection regexes, `5` HTML tags, `javascript:` URLs, redaction markers, typed `Issue(severity, patternId, match, offset)` | `src/main/java/org/olat/core/commons/services/ai/content/AiContentHardener.java` |
| 🟢 `INJECTION_PATTERNS`, already `public static final` and already reused once | same file; reused at `GeneratedItemValidator.java:163` |
| 🟢 The pre-filter chain the fix slots into | `EssayFormativeFeedbackService.java:143` → `:154` → `:163` |
| 🟢 The rejection vocabulary to extend | `RejectionReason`, `EssayGradingPreFilterException` |
| 🟢 The ledger that will evidence it | `o_ai_usage_log`, `33` columns; `logPreFilterRejection()` at `:279` |

🟢 **The recipe, and note which of the two options to pick:**

```java
// A FOURTH pre-filter, alongside LengthPreFilter / GibberishPreFilter / LanguagePreFilter.
// Place it in EssayFormativeFeedbackService.grade() AFTER the length check (so a megabyte of
// injection is refused on length first) and BEFORE AiGradingTier.classify().
public final class InjectionPreFilter {
    public static final String WARNING_INJECTION = "ai.essay.warn.injection.detected";

    public static Optional<RejectionReason> check(String studentAnswer) {
        if (studentAnswer == null || studentAnswer.isEmpty()) return Optional.empty();
        for (Pattern p : AiContentHardener.INJECTION_PATTERNS) {
            if (p.matcher(studentAnswer).find()) {
                // FLAG, do not refuse: a refusal is a denial of assessment to a learner who may
                // simply have quoted the phrase. Route to human marking instead.
                return Optional.of(new RejectionReason(WARNING_INJECTION, p.pattern(), null));
            }
        }
        return Optional.empty();
    }
}
```

🔴 **Do NOT call `harden()` on the student answer.** 🔵 **`harden()` REWRITES its input, and
rewriting a learner's submission before grading it is indefensible in an appeal — the mark would
be computed against text the student did not write.** 🟢 **Scrub the AUTHOR's content; FLAG the
learner's.**

🟢 **The three-line policy decision the client must make, and it is theirs not ours:**

| on detection | consequence | who it suits |
|---|---|---|
| 🟢 **Flag + route to human marking** | 🟢 no learner is graded by a manipulated prompt; no learner is refused | 🟢 **the default — recommend this** |
| 🟡 Flag + grade anyway, annotate for the coach | 🟡 cheap, keeps throughput | 🟡 low-stakes formative practice |
| 🔴 Refuse the submission | 🔴 denies assessment on a regex match | 🔴 **only with an appeals route attached** |

🟢 **Effort: `~4` hours plus the policy conversation. One new class, one call site, one language
string, one test class modelled on `AiContentHardenerTest` (`194` LOC, already in the repo).**
🔵 **Sell it as the first work package of an Annex III engagement, never as a vulnerability
report — the platform's oversight design is the reason it is worth adopting.**
[`evidence/injection-defence-by-path.2026-10-13-p162.tsv`](../evidence/injection-defence-by-path.2026-10-13-p162.tsv)

---

## 🆕 🟢 `P162-C` — the Annex III gate Moodle core does NOT enforce *(new, p162 — Global; strongest in North America and EMEA)*

🔵 **The problem this solves:** 🟢 **This shelf has been telling clients that Moodle core sits
outside the AI Act's evaluative tier because it ships `4` actions and `0` of them grade.**
🔴 **`ACTION IE` established that this is a fact about what core SHIPS, not a gate core ENFORCES.**

🟢 **The reach, measured:**

| link in the chain | evidence |
|---|---|
| a placement is an ordinary subplugin | `version.php` + `db/access.php` + `db/services.php` + `classes/external/` in both core placements |
| it declares its own actions | `placement::get_action_list(): array` returns class NAMES |
| core does not filter them | `manager.php:75-77` calls `$pluginclassname::get_action_list()`; no allowlist |
| the dispatcher takes any subclass | `manager.php:191` — `process_action(base $action)` |
| the action owns its own writes | `aiactions/base.php:50` — `abstract public function store(...): int`; `get_tablename()` overridable at `:118` |
| the gradebook is a global function | `public/lib/gradelib.php:64` — `grade_update($source, ...)`, `$source` a free-text label, no caller check |

🔴 **So: install one third-party `aiplacement_*` plugin that grades, and the institution is in the
high-risk tier, with no technical signal that it happened.**

🟢 **The recipe — three controls, all configuration and reporting, no platform fork:**

```bash
# 1. INVENTORY. What AI plugins are installed, and which are not core?
#    Core ships exactly two placements. Anything else is a third-party evaluative risk.
php admin/cli/cfg.php --component=core_ai          # provider + action state
ls public/ai/placement/                             # expect: courseassist, editor. Anything else -> review
# 2. GATE. Pin the plugin set and make installs a reviewed event, not an admin convenience.
#    $CFG->disableupdateautodeploy = true;  in config.php
#    plus a code-review step on any aiplacement_* / aiprovider_* addition.
# 3. EVIDENCE. The ledger already exists -- turn it into a standing report.
#    ai_action_register  -> per-call: user, course, context, provider, model, tokens, success, timings
#    ai_policy_register  -> per-user policy acceptance, with a reportbuilder report shipped
```

🟢 **Deliverable: a one-page *"which AI actions can write to a gradebook in this installation"*
report, a pinned plugin set, and the two reports core already provides, scheduled.**
🔴 **Pair it with `P161-B`** — 🔴 **the ledger retains `prompt` and `generatedcontent` verbatim and
nothing ever deletes them, so standing up the evidence without the retention job creates a new
problem while solving an old one.**
🟢 **Effort: `~1` week including the policy write-up. Sells to any public institution already on
Moodle, which is most of them.**
[`evidence/placement-gradebook-reach.2026-10-13-p162.tsv`](../evidence/placement-gradebook-reach.2026-10-13-p162.tsv)

---

## 🆕 🟢 `P162-D` — multi-tenant AI assessment on MIT, using the judge that already ships *(new, p162 — Global; strongest in LATAM and APAC)*

🔵 **The problem this solves:** 🔴 **A client who needs AI assessment, a permissive licence AND
multi-tenancy has had no answer on this shelf: Moodle core does not grade, OpenOLAT is
single-tenant in this respect, `edx-platform` is AGPL with `0` AI files, and every greenfield
recipe meant building rubric storage, score provenance and an oversight story from nothing.**
🟢 **`Selleo/mentingo` (MIT) ships all three.**

🟢 **What you are adopting, read from `242a9324` this pass:**

| requirement | the code that answers it |
|---|---|
| 🟢 **Author owns the bar, not the model** | 🟢 `ai_judge_configurations.passing_threshold_percent`; the model never receives the threshold |
| 🟢 **Rubric with worked anchors** | 🟢 `ai_judge_score_guidance(score, description, example)`, `UNIQUE(criterion_id, score)` — a description AND an example per score point |
| 🟢 **Verdict computed in server code** | 🟢 `judgeEvaluation.ts:74-85` — `passed = score >= ceil(maxScore × passingThresholdPercent / 100) && blockingErrors.length === 0` |
| 🟢 **Model cannot exceed its allowance** | 🟢 `judgeEvaluation.ts:26` THROWS *"AI Judge awarded a score outside the configured range"* — refuses rather than silently clamping |
| 🟢 **No learner failed on a hallucinated blocker** | 🟢 `judge.service.ts:100-125` re-sends each candidate blocking error in a SECOND verification call and drops it unless confirmed |
| 🟢 **A past mark survives a rubric edit** | 🟢 `ai_mentor_judgement_criteria.max_score_at_judgement` |
| 🟢 **Internal vs learner-facing text separated** | 🟢 `blocking_error_description` vs `learner_safe_feedback`, two columns by design |
| 🟢 **Multi-tenancy** | 🟢 **all `7` judge tables carry `tenant_id` with an RLS default and an FK to `tenants`** |
| 🟢 **SCORM interop** | 🟢 in-tree generator + runtime, player `scorm-again@3.0.4` (MIT) — closure MIT over MIT |

🔴 **What you must add, stated up front so the estimate is honest:**

- 🔴 **`4 753` tracked files against Moodle's `67 589`.** 🔵 **This is a product, not a platform:
  no LTI, no xAPI** *(`T127`, re-confirmed by manifest this pass)*, **no Open Badges issuance.**
- 🔴 **The judge is schema-present and NOT behind a feature flag** — 🟢 **unlike OpenOLAT's
  `ai.feature.essay-grading.enabled=false`, there is no off switch to point a regulator at.**
  🟢 **Add one, as an explicit configuration gate, in week one.**
- 🟡 **The injection surface on its graded path was NOT assessed this pass** *(`ACTION IH`)* —
  🟢 **run `P162-B`'s reasoning over it before go-live, not after.**

🟢 **Effort: `6`–`8` weeks to a governed pilot — rubric authoring UI exists, judge exists,
tenancy exists; the work is the off switch, the injection filter, the retention policy and the
institution's appeals route.** 🔵 **In LATAM this lands directly on the `87%`/`26%` gap: a
tenant-per-institution deployment with the governance artefacts built in is cheaper than
retrofitting policy onto `200` institutions' existing tools.**
[`evidence/evaluative-tier-tri-platform.2026-10-13-p162.tsv`](../evidence/evaluative-tier-tri-platform.2026-10-13-p162.tsv)

---
## 🆕 🟢 `P161-A` — AI that GRADES, on a platform that already implements the oversight the regulator will ask for *(new, p161 — Global; strongest in EMEA and APAC)*

🔵 **The problem this solves:** 🔴 **Evaluative AI in education is high-risk under the EU AI
Act's Annex III, named in Korea's AI Basic Act as high-impact, and listed in Vietnam's
`134/2025/QH15`.** 🔴 **Every studio answer to date has been a governance deck wrapped around a
general LLM call.** 🆕 🟢 **`openolat/OpenOLAT` (Apache-2.0) ships the whole oversight apparatus
as code, and it ships it OFF.**

🟢 **What you are adopting, all verified in the tree at `e4be14f0` this pass:**

| requirement a regulator or auditor raises | the code that answers it |
|---|---|
| *"Is the human the decision-maker?"* | 🟢 `GradingSuggestion` carries RAW SIGNALS; its own holistic score is documented *"advisory only, server-side weighting is authoritative"*. 🟢 The gradebook number is computed by OpenOLAT |
| *"Did the student consent?"* | 🟢 `AiCorrectionConsentController` — `allow-once` / `allow-always` / `deny`, at quiz start |
| *"What stops a nonsense call?"* | 🟢 `GibberishPreFilter` *(trigram entropy `1.5` bits, letter ratio `0.45`)*, `LanguagePreFilter`, `LengthPreFilter` — all BEFORE the provider is called |
| *"How do you express uncertainty?"* | 🟢 `Confidence{LOW,MEDIUM,HIGH}`, `OffTopicFlag{NONE,LIKELY_OFF_TOPIC,GIBBERISH,LANGUAGE_MISMATCH}`, `Severity{MINOR,MAJOR}` |
| *"Reproduce this mark."* | 🟢 `o_ai_essay_correction.a_content_hash_at_call` + `a_prompt_template_version` |
| *"Where did the data go?"* | 🟢 `o_ai_usage_log`, `33` columns: provider, requested model vs responding model, temperature, `top_p`, token counts including cache and reasoning tokens, latency, finish reason, invocation id |
| *"Does it leave the country?"* | 🟢 `GenericAiSPI` takes any OpenAI-compatible `base.url` *(vLLM, Ollama, a sovereign endpoint)*; 🟢 `LocalOnnxSPI` runs an admin-uploaded ONNX embedding model IN-PROCESS |

### The recipe

```bash
# 0. Fork-and-own. Apache-2.0, default branch is `master`, committed today.
git clone --depth=1 https://github.com/openolat/OpenOLAT

# 1. Decide the regulatory posture FIRST. These four lines are the scope boundary.
#    olat.properties — all four ship `false`.
ai.feature.mc-question-generator.enabled       # generative, low risk
ai.feature.image-description-generator.enabled # generative, accessibility win
ai.feature.essay-generation.enabled            # generative, low risk
ai.feature.essay-grading.enabled               # EVALUATIVE -> Annex III. This one is the decision.

# 2. Keep the inference inside the jurisdiction.
ai.generic.preset.enabled=true
ai.generic.preset.base.url=https://llm.internal.<client>/v1   # vLLM or Ollama
#    Embeddings need no endpoint at all: upload model.onnx via LocalOnnxModelAdminController.

# 3. Wire the evidence BEFORE the pilot, not after.
#    - o_ai_usage_log  -> the per-call record (AiUsageLogAdminController ships the UI)
#    - o_ai_essay_correction -> the mark, its prompt template version and its content hash
#    - add the retention job from P161-B. Neither table purges itself.

# 4. Calibrate the pre-filters on the client's own corpus.
#    GibberishPreFilter.ENTROPY_THRESHOLD = 1.5 and MIN_LETTER_RATIO = 0.45 are
#    the project's own stated defaults, annotated "tune after the first real corpus".
#    For CJK cohorts check AiGradingTier.classify() — it counts CJK codepoints, not words.
```

🟢 **What the studio actually sells:** 🔴 **not the grading** *(it is in the box)* —
🟢 **the calibration run, the retention policy, the Annex III conformity file assembled from
`o_ai_usage_log` and `o_ai_essay_correction`, and the human-in-the-loop workflow around
`GradingSuggestion`.** 🔵 **`6–8` weeks, and the client owns an Apache-2.0 platform at the end
of it.**

🔴 **Say this plainly in the first workshop:** 🔴 **turning the flag on is the moment the
institution becomes a deployer of a high-risk AI system.** 🟢 **Leaving the other three on while
that one stays off is a perfectly coherent product, and is where most clients should start.**

---

## 🆕 🟢 `P161-B` — the retention job neither platform ships, and it is four hours of work *(new, p161 — Global; mandatory wherever `P160-B` or `P161-A` is deployed)*

🔵 **The problem this solves:** 🔴 **Moodle's AI subsystem keeps every prompt and every response
forever** *(`ai_action_generate_text`, `ai_action_summarise_text`, `ai_action_explain_text`
hold `prompt` + `generatedcontent`; `ai_action_generate_image` holds `prompt`, `revisedprompt`
and `sourceurl`)*. 🔴 **`public/ai` has no `db/` directory, no scheduled task, no settings page
and `0` matches for `retention|purge|cleanup|expiry`.** 🔴 **OpenOLAT is the same shape:
`AiUsageLogDAO` has no delete method, and `o_ai_essay_correction.a_student_answer` is
`text NOT NULL`.**
🟢 **This is not a defect report. Both projects implemented subject-access and erasure
properly** *(Moodle: `806`-LOC privacy provider, export plus three delete paths, all six tables
declared; OpenOLAT: `UserDataDeletable` on `EssayAiCorrectionService`)*. 🔴 **They implemented
erasure ON REQUEST and left periodic minimisation to the deployer. The deployer is the client,
and the client does not know.**

### The recipe — Moodle

```php
// local/aiRetention/classes/task/purge_ai_actions.php  (GPL-3.0, lives beside core)
// Scheduled task. Deletes the PAYLOAD rows, keeps the ai_action_register INDEX row,
// so the audit trail a regulator asks for survives and the student text does not.
foreach (['generate_text','summarise_text','explain_text','generate_image'] as $a) {
    $DB->delete_records_select("ai_action_{$a}",
        "id IN (SELECT actionid FROM {ai_action_register}
                 WHERE actionname = :a AND timecreated < :cutoff)",
        ['a' => $a, 'cutoff' => time() - $retentiondays * DAYSECS]);
}
// Then null the free-text error column on the index rows older than the same cutoff.
```

🟢 **Why payload-only:** 🟢 **`ai_action_register` carries no student text — `userid`,
`contextid`, `courseid`, `provider`, `model`, token COUNTS, timings.** 🔵 **Keeping it is what
answers Oklahoma's and Maryland's oversight clauses and Ohio's policy deadline; deleting the
payload is what answers GDPR Article `5(1)(e)`.** 🟢 **They are not in tension once the two
tables are treated differently.**

🟡 **The generic alternative, if the client will not take a plugin:** `tool_dataprivacy`
purposes with retention periods plus `tool_dataprivacy\task\delete_expired_contexts` —
🔴 **remember it is gated on `tool_dataprivacy/automaticdatadeletionapproval`, which ships `0`,
and that it expires whole CONTEXTS, so it cannot keep the index and drop the payload.**

### The recipe — OpenOLAT

```sql
-- Nightly. The usage log has no student text, so it can be kept long and aggregated.
-- The corrections table holds the essay itself and is the one with a clock on it.
DELETE FROM o_ai_essay_correction
 WHERE creationdate < now() - interval '180 days'
   AND a_status IN ('DONE','FAILED');
-- Keep o_ai_usage_log: 33 columns of cost, latency and provider behaviour, no PII payload
-- beyond fk_identity, which UserDataDeletable already handles on account deletion.
```

🟢 **Deliverable, and it is small:** 🟢 **a retention period agreed with the DPO, one scheduled
task, one line in the privacy notice, and a report that shows the job ran.**
🔵 **Four hours of engineering attached to a conversation nobody has had.** 🔴 **Sell it with
`P160-B` and `P161-A`, never after them.**

---

## 🆕 🟢 `P161-C` — `P160-A`, with STEP 7 and the cost note the last pass could not have written *(amends `P160-A`, p161 — Global)*

🟢 **`P160-A` stands. Two additions, both measured this pass.**

🆕 **STEP 7 — read the MIGRATIONS before publishing a capability as present.**

```bash
# T141: edx-platform has 23 non-test `badge` paths and a whole lms/djangoapps/badges app.
# Its models were DELETED in 2023 and the files stayed.
find $DIR -path '*/migrations/*' -name '*.py' | xargs grep -l 'DeleteModel\|RemoveField' \
  | sed 's|/migrations/.*||' | sort -u
# For a non-Django platform the equivalent is the schema-upgrade directory:
#   Moodle  -> public/lib/db/upgrade.php
#   OpenOLAT-> src/main/resources/database/postgresql/alter_*.sql
```

🆕 **STEP 8 — on a plugin-architecture platform, the dependency manifest is a SECOND instrument.**

```bash
# T142: lti13 / lti1p3 / ltiadvantage all return 0 in edx-platform. The capability is real and
# it is `lti-consumer-xblock`; learning records are `event-routing-backends`.
grep -nE 'lti|xapi|caliper|credential' $DIR/requirements/edx/base.txt   # or package.json, pom.xml
# A zero in the tree + a hit in the manifest = PRESENT, out of repo, with its own licence.
```

🔴 **And the cost correction, because this pass bought it:**

| instrument | measured cost | verdict |
|---|---|---|
| 🟢 `git ls-remote --symref` | ~`0` | always first *(`P53`, `P54`)* |
| 🟢 `--depth=1` clone | `339 MB` OpenOLAT, `207 MB` edx-platform | 🟢 the right instrument for DISCOVERY |
| 🔴 `--depth=1 --filter=blob:none` | 🔴 **`752 MB` on Moodle — NO saving** | 🔴 **the checkout re-fetches every blob. Add `--no-checkout` if you only need paths** |
| 🟢 `raw.githubusercontent.com` | kilobytes | 🟢 **the right instrument once the path is KNOWN** — two reads would have replaced the `752 MB` above |

---

## 🆕 🟢 `P160-A` — the capability census when the API is CLOSED, with the three contaminations removed *(new, p160 — Global)*

🔵 **The problem this solves:** 🔴 **`api.github.com` refuses every repository this session is not
configured for (`T137`), so topics, stars and `pushed_at` are gone.** 🔴 **And the fallback this
shelf reached for — counting paths whose name contains a token — over-counts three ways and
invents absences a fourth** *(`T136`)*.
🟢 **The clone channel is better than what it replaces for CAPABILITY questions, because it
carries file CONTENT; it is worse for ATTENTION questions, because it carries no metadata.**

🟢 **The gate, in order:**

```bash
REPO="owner/name"; DIR="/tmp/census/$(basename $REPO)"

# STEP 0 (P54) — existence and default branch, before any absence means anything.
BR=$(git ls-remote --symref "https://github.com/$REPO" HEAD | awk '/^ref:/{sub("refs/heads/","",$2);print $2}')
[ -z "$BR" ] && { echo "$REPO: DOES NOT EXIST OR IS PRIVATE"; exit 1; }
SHA_REMOTE=$(git ls-remote "https://github.com/$REPO" HEAD | cut -f1)

# STEP 1 — one shallow clone. Trees AND content, no metadata layer in between.
git clone --depth=1 --single-branch -q "https://github.com/$REPO" "$DIR"
[ "$(git -C $DIR rev-parse HEAD)" = "$SHA_REMOTE" ] || echo "WARN: head drifted mid-clone"

# STEP 2 (T136a) — DISAMBIGUATE the token before counting. `lti` matches `multi`.
RAW=$(find $DIR -path '*/.git' -prune -o -ipath '*lti*' -print | wc -l)
CLEAN=$(find $DIR -path '*/.git' -prune -o -ipath '*lti*' -print | grep -viE 'multi' | wc -l)

# STEP 3 (T136b) — ATTRIBUTE every hit. A vendored SDK is somebody else's capability.
find $DIR -ipath '*tenant*' | grep -vE 'lib/(google2-service|aws-sdk)|node_modules|vendor/'

# STEP 4 (T136c) — take the VOCABULARY from the platform, not from a fixed list.
#   LTI 1.3 is `lti13` in OpenOLAT, `ltiadvantage` + `lib/lti1p3` in Moodle.
#   Probe BOTH spellings and treat a zero on one spelling as no evidence at all.

# STEP 5 (T135) — a capability can be an EXPORT PIPELINE or a MODULE, so grep CONTENT
#   for the standard's own identifiers, not for the product word.
grep -rilE 'OpenBadgeCredential|VerifiableCredential|credentialSubject|ob/v3p0' \
     --exclude-dir=.git --exclude-dir=node_modules "$DIR"

# STEP 6 — licence from the body (P56, 33 paths) and recency from the log.
git -C $DIR log -1 --format='%ad|%h' --date=short
```

🟢 **What each step cost and caught, measured on five platforms this pass:**

| step | caught |
|---|---|
| 🟢 **STEP 2** | 🔴 **`375` false `lti` hits in Moodle (`30.6%`), `128` in OpenOLAT (`33.0%`)** |
| 🟢 **STEP 3** | 🔴 **`62 of 62` Moodle *"tenant"* paths are vendored — the capability is ABSENT** |
| 🟢 **STEP 4** | 🔴 **two FALSE ABSENCES that a fixed token list would have published as findings** |
| 🟢 **STEP 5** | 🟢 **`mentingo`'s `119` SCORM files, which a schema census missed** *(`T135`)*; 🔴 **`0 of 5` platforms issuing OB 3.0** |
| 🟢 **STEP 6** | 🔴 **`openlxp-xia` `228` days stale on an EOL Django pin** |

🔴 **Cost, stated honestly: `1.3 GB` of clone traffic for five repositories** *(Moodle alone is
`746 MB` / `67 589` files)*. 🟢 **This is a PLATFORM-tier instrument. Do not run it over a
100-row census — for that, `raw` + `P56` is still the right gate.**

---

## 🆕 🟢 `P160-B` — governed AI on Moodle: use the ledger that is already there, and keep the evaluative action OUTSIDE core *(new, p160 — Global; strongest in North America, EMEA and LATAM)*

🔵 **The problem this solves:** 🔴 **three regulatory regimes now ask an institution to EVIDENCE
its AI use — Oklahoma and Maryland's human-oversight clauses, Ohio's district policy deadline,
the EU AI Act's Art 50 transparency duty — and LATAM's `87%` adoption against `26%` strategy is
the same problem without a statute.** 🔴 **`P158-A` answered it by assembling Langfuse traces and
rubric tables on a greenfield MIT platform.** 🟢 **That is the wrong answer for a client who
already runs Moodle, and most public institutions do.**

🟢 **What this pass measured, and it changes the build** *(`T139`, `repos/foundations.md`)*:

| layer | what Moodle core ALREADY ships | licence |
|---|---|---|
| 🟢 **Provider abstraction** | 🟢 **`public/ai/provider/{anthropic,awsbedrock,azureai,deepseek,gemini,ollama,openai}`** — `209` files | 🟡 GPL-3.0, in core |
| 🟢 **Sovereign option** | 🟢 **`ollama` is a core provider** — no egress, no fork | 🟡 GPL-3.0 |
| 🟢 **Per-call audit ledger** | 🟢 **`ai_action_register`: `userid`, `contextid`, `courseid`, `provider`, `model`, `prompttokens`, `completiontokens`, `success`, `errorcode`, `timecreated`, `timecompleted`** | 🟡 GPL-3.0 |
| 🟢 **Consent evidence** | 🟢 **`ai_policy_register` + `policy_acceptance_report.php` + a `reportbuilder` system report** | 🟡 GPL-3.0 |
| 🟢 **Cost control** | 🟢 **`public/ai/classes/rate_limiter.php`** | 🟡 GPL-3.0 |
| 🟢 **Learning records** | 🟢 **`public/lib/xapi` — `78` paths** | 🟡 GPL-3.0 |
| 🟢 **Federation** | 🟢 **LTI 1.3 as platform AND tool, with AGS, NRPS, Deep Linking, JWKS** | 🟡 GPL-3.0 |

🟢 **The recipe:**

| step | what to do | why this way |
|---|---|---|
| 1 | 🟢 **Configure, do not fork. Turn on `core_ai` with the `ollama` provider pointed at the institution's own inference, and leave Moodle UNMODIFIED** | 🟢 **`P156-A`'s rule: an unmodified GPL platform is not a derivative, so the studio's deliverable stays permissive** |
| 2 | 🟢 **Switch on the AI policy gate and the acceptance report** | 🟢 **This is the artefact an Ohio district, an Oklahoma appeal or an Art 50 enquiry actually asks for, and it is `0` lines of code** |
| 3 | 🔴 **Put every EVALUATIVE capability OUTSIDE core, behind LTI 1.3** | 🔴 **Core AI has four actions and none grades or places a learner. 🟢 Keeping assessment in an LTI tool keeps the Annex III high-risk surface EXPLICIT, versioned and separately auditable — and keeps it out of the institution's LMS upgrade path** |
| 4 | 🟢 **Build the evaluative tool on `P158-A`'s shape: rubric criteria as DATA, `pykt-toolkit` (MIT) as a second non-LLM mastery estimate, the human signing** | 🟢 **Satisfies the human-oversight clauses without putting a prompt in the decision path** |
| 5 | 🟢 **Pass grades back over AGS; pull roster over NRPS; emit xAPI statements to the institution's LRS** | 🟢 **All four surfaces measured present in Moodle this pass** |
| 6 | 🔴 **For a MULTI-DISTRICT estate, use one Moodle instance per tenant** | 🔴 **Moodle core has NO tenancy — its `62` *"tenant"* paths are vendored (`T136`). Moodle Workplace has it and is PROPRIETARY. 🟢 `mentingo` (MIT, PostgreSQL RLS) is the single-deployment alternative, and it does not speak LTI** |
| 7 | 🟡 **For CREDENTIALS, issue Open Badges `v2` from core now and treat OB 3.0 as a separate build** | 🔴 **Moodle is `OPEN_BADGES_V2` only (`132` references, `V3` never). 🟢 `P159-A` is the upgrade; authoring is MIT (`opensalt/OB3DefinitionWidget`), signing is unbuilt** |

🟢 **Why this is cheaper than `P158-A` for an existing-Moodle client:** 🟢 **layers 1, 2, 3 and 5
of `P158-A` — trace, tenancy-adjacent audit, provider abstraction, record emission — are already
installed.** 🔴 **What remains billable is the evaluative tool, the rubric data model and the
integration.** 🟡 **`4–6` weeks against `P158-A`'s `8–10`, and the client keeps its LMS.**
🔴 **Licence line to state in the SOW: the Moodle side is GPL-3.0 and stays unmodified; the LTI
tool is the studio's own work and can be licensed freely.**

---
## 🆕 🟢 `P159-A` — the credential-issuing build, and it is the first pattern on this shelf with a DATED demand figure above it and a NAMED permissive platform below it *(new, p159 — Global; strongest in North America and EMEA)*

🔵 **The problem this solves:** 🟢 **employers and institutions are moving to skills-based
recognition, and the demand is now measured rather than asserted** — 🟢 **1EdTech's Badge Count
2025 reports `40%` of badge platform providers already issuing Open Badges 3.0, `2 694 271`
OB 3.0 achievements and `6 269 066` Comprehensive Learner Records, against `74 million`+ badges
issued in total.**
🔴 **The open-source supply is one spec version behind.** 🟢 **`openolat/OpenOLAT` (Apache-2.0,
`447 ★`) ships a real Open Badges module — `156` paths, `Badge`, `Assertion`, `Criteria`,
`Profile`, `Identity`, `BadgeClass`, LinkedIn push, and a rule engine that awards
automatically.** 🔴 **It is Open Badges `v2`: `0` matches for `OpenBadgeCredential`,
`VerifiableCredential` or an `openbadges/v3` package.**
🟢 **The authoring surface for `v3` already exists and is permissive** — [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget),
**MIT** — 🔴 **so what is genuinely missing is ISSUANCE: serialising and SIGNING a W3C Verifiable
Credential.**
🔵 **So the engagement is not *"build a credentialing system"*. It is *"take a working
Apache-2.0 issuer to the version buyers are asking for."***

🟢 **The recipe — issue from the platform, upgrade at the edge:**

| layer | repo / artefact | licence | why this one |
|---|---|---|---|
| 1. **Issuer + award rules** | [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) `org/olat/modules/openbadges` | 🟢 **Apache-2.0** *(`LICENSE`, 10 982 B, body-read on `master`)* | 🟢 **`BadgeCriteria.isAwardAutomatically()` plus a composable `List<BadgeCondition>` and `allConditionsMet(courseEntry, uce, recipient)`.** 🔵 **Conditions bind to COURSE ELEMENTS via `CourseElementDAO` — the award is a rule over real outcomes, not a prompt** |
| 2. **Evidence the badge points at** | same — QTI 2.1 *(`660` paths)* + SCORM *(`154` paths)* | 🟢 Apache-2.0 | 🟢 **A badge whose `Criteria` dereferences an actual assessment attempt is the difference between a credential and a sticker** |
| 3. **Where the learning happens** | 🟢 Any permissive tutor from `agents/top.md` — [`DeepTutor`](https://github.com/HKUDS/DeepTutor) *(Apache-2.0)*, [`Bloom`](https://github.com/Li-Evan/Bloom) *(MIT)*, [`universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) *(MIT)* | 🟢 **Apache-2.0 / MIT** | 🟢 **Federated in over LTI 1.3 — OpenOLAT is a Platform (`lti13.platform.iss`), so the tutor is a Tool and keeps its own licence** |
| 4. **Grade back, roles out** | same — LTI **AGS** *(`LineItem`, `LineItemScore`)* and **NRPS** *(`Member`, `Context`)* | 🟢 Apache-2.0 | 🟢 **The tutor posts a score; the score satisfies a `BadgeCondition`; the badge issues. No custom integration** |
| 5. 🟢 **OB 3.0 AUTHORING — already built and permissive** | 🟢 [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **MIT** *(`LICENSE`, 1 080 B)* | 🟢 **A Vue widget that produces an Open Badge **v3** achievement DEFINITION.** 🔵 **The authoring half of the upgrade exists — do not rebuild it** |
| 6. 🔴 **The build: OB 3.0 ISSUANCE and SIGNING** | 🔴 **Nothing permissive ISSUES one.** [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) is **LGPL-3.0** *(`LICENSE.txt`, 7 650 B)*, `1 ★` | 🔴 **copyleft, and unmaintained-thin** | 🟢 **Write a `v3` EMITTER beside OpenOLAT's `v2` package: take the `BadgeClass` and `Assertion` rows, serialise them as a W3C Verifiable Credential, sign it, and manage the keys.** 🔵 **Authoring is solved; issuance is the deliverable the client cannot buy** |
| 7. **Mastery evidence independent of the rule** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** *(1 066 B)* | 🟢 **A non-LLM second opinion on whether the learner knows it, so a contested award has two instruments behind it** |

🟢 **Wiring, concretely:**
1. 🟢 **Model the credential as a `BadgeClass` with `Criteria` that name course elements** — not
   free text. 🔵 **The criterion must be dereferenceable, or the credential cannot be defended.**
2. 🟢 **Set `isAwardAutomatically()` and compose the `BadgeCondition` list** so issuance is a
   consequence of assessment, never a manual act. 🔵 **This is the same *"decision as data"*
   principle `P158-A` applies to grading.**
3. 🟢 **Federate the tutor in over LTI 1.3 and let AGS post the score.** 🟢 **Because OpenOLAT is
   Apache-2.0, `P156-A`'s process boundary is not even needed here** — 🔵 **the licence boundary
   that forces it with Moodle or Open edX simply is not present.**
4. 🟢 **Emit `v2` today** *(it works, and it is `74M` badges' worth of installed base)*, 🟢 **and
   ship the `v3`/VC emitter as the differentiated layer** — 🟢 **authoring the `v3` definition with
   the MIT widget rather than writing a form.**
5. 🔴 **Do NOT promise xAPI.** 🔴 **Neither permissive platform on this shelf emits it** —
   OpenOLAT: `0` matches on four spellings; `mentingo`: `0` in its schema.

🔴 **Where it does NOT fit:** 🔴 **a client who needs xAPI statements into an existing LRS**
*(nothing permissive supplies it)*; 🔴 **a client who must issue OB 3.0 on day one with no build
budget** *(authoring is MIT and ready, but the only ISSUANCE library is LGPL-3.0 at `1 ★`)*.
🟡 **Tenancy note:** 🟢 **OpenOLAT's organisations are hierarchical with per-node roles, which
suits one institution with internal structure.** 🔴 **For many unrelated customers on one
deployment, `mentingo`'s database-level RLS is the stronger guarantee — and it has no LTI.**

🟢 **Effort:** 🟢 **`4–6` weeks to a working `v2` issuing pipeline with a federated tutor**;
🟡 **`8–10` weeks including a signed OB 3.0 / W3C VC emitter and the key management it implies.**

---

## 🆕 🟢 `P56` — the licence gate, CORRECTED again, because `P158-B` reported *"no licence"* for Moodle *(new, p159 — supersedes `P158-B`)*

🔵 **The problem this solves:** 🔴 **`P158-B` was run on a known-answer control of 15 platform
rows and returned `NO_LICENCE_FILE` for `4` of them** — 🔴 **Moodle, ERPNext, Frappe LMS and
`openedx/XBlock`, all of which are licensed and none of which uses a path on the 9-path list.**
🔴 **And its STEP 2 (`head -5`) misclassified a PolyForm Noncommercial licence as
*"All rights reserved"*, because the family name line sat at line 14 behind a preamble.**

🟢 **The corrected gate — the ORDER is the fix, and so is the path list:**

```bash
REPO="owner/name"

# STEP 0 (P54) — does it exist? A 404 means nothing until this passes.
BR=$(git ls-remote --symref "https://github.com/$REPO" HEAD 2>/dev/null \
     | awk '/^ref:/{sub("refs/heads/","",$2); print $2}')
[ -z "$BR" ] && { echo "$REPO: DOES NOT EXIST OR IS PRIVATE — not a finding"; exit 1; }

# STEP 1 (P53 + T129) — probe the repo's OWN default branch, over 33 paths, not 9.
#   8 of this shelf's 15 platform rows do NOT default to `main`:
#   master x5, plus release_11 (ILIAS), 20.0 (Odoo), 19.0 (OpenEduCat), develop (Frappe x2).
for p in LICENSE LICENSE.md LICENSE.txt LICENSE.rst LICENCE LICENCE.md LICENCE.txt \
         License License.md License.txt Licence Licence.md Licence.txt \
         license license.md license.txt licence licence.md licence.txt \
         COPYING COPYING.txt COPYING.md COPYING.LESSER COPYRIGHT COPYRIGHT.txt \
         NOTICE NOTICE.txt LICENSE-MIT LICENSE-APACHE LICENSE-BSD \
         docs/LICENSE.md LICENSE/LICENSE LICENSES/LICENSE; do
  curl -sf "https://raw.githubusercontent.com/$REPO/$BR/$p" -o /tmp/lic && { echo "BODY: $p"; break; }
done

# STEP 2 (T131) — SPDX line FIRST. It is the author's own declaration.
grep -ioE 'SPDX-License-Identifier:[[:space:]]*[A-Za-z0-9.+-]+' /tmp/lic | head -1

# STEP 3 (T131) — else the family TITLE line, scanning top-down, first match wins.
#   NOT head -5 (a preamble pushes the title below it: PolyForm at line 14).
#   NOT a whole-body scan either (AGPL-3.0's text cites the GPL in §13 — 3 rows matched
#   two families each). The whole-body scan is a DETECTOR for a preamble, never the classifier.
grep -inoE 'GNU AFFERO GENERAL PUBLIC LICENSE|GNU LESSER GENERAL PUBLIC LICENSE|\
GNU GENERAL PUBLIC LICENSE|Apache License|MIT License|BSD [0-9]-Clause|Mozilla Public License|\
Business Source License|PolyForm (Noncommercial|Strict|Perimeter)|Elastic License|\
Server Side Public|All rights reserved|Community License|Creative Commons' /tmp/lic | head -1

# STEP 4 (T130) — the completeness floor belongs to the FAMILY, not to the file.
```

🟢 **The per-family completeness floor — `T130`:**

| family | complete body is | below that you have |
|---|---|---|
| 🟢 **MIT / ISC** | `~1 000 – 1 300 B` | — *(complete at 1 kB)* |
| 🟢 **Apache-2.0** | `~11 kB` | 🔴 a NOTICE or a stub |
| 🔴 **GPL / AGPL / LGPL-3.0** | `~30 – 36 kB` | 🔴 **the HEADER NOTICE, not the licence** |

🔴 **The trap this catches that `P158-B` did not:** 🔴 **`24kchengYe/human-skill-tree` (`571 ★`)
carries an `1 134 B` file GitHub files as AGPL-3.0.** 🔴 **At `1 134 B` that is the header notice.**
🟢 **p158's single *"under ~`1 000 B`"* floor does not fire; a per-family floor does.**

🟢 **The four tiers are unchanged from `P158-B`** *(permissive → copyleft → source-available by
design → no grant)*, 🟢 **with one addition:** 🟡 **`GRANT ASSERTED, TEXT ABSENT`** — 🟡 **the
family is named in a `NOTICE` or in README prose but no licence text exists in the tree
(`openedx/XBlock`; and `T117`'s eight prose-MIT instances).** 🔵 **Usable with legal review,
not shippable on the strength of the claim alone.**

🟢 **Cost: one `ls-remote` and at most 33 `curl`s per repository.** 🟢 **`118` repositories were
gated this way in p159** *(100 census rows, 15 platform rows, 3 new entrants)*. 🔴 **The upgrade
from 9 paths to 33 changed `6` verdicts, `4` of them on rows this shelf recommends to clients.**
## 🆕 🟢 `P158-A` — the auditable-assessment build, and it is the first pattern on this shelf whose rubric is DATA rather than a prompt *(new, p158 — Global; strongest in North America and EMEA)*

🔵 **The problem this solves:** 🔴 **two regulators now constrain the ARCHITECTURE of educational
AI, not its paperwork.** 🔴 **Oklahoma and Maryland ban AI from making high-stakes decisions about
students and require human oversight.** 🔴 **The EU AI Act puts EVALUATIVE use — systems that
assess learning outcomes or influence a learner's path — in the Annex III high-risk tier, on
every reading of a contested date.**
🔴 **A grading agent whose rubric lives in a prompt cannot satisfy either: there is nothing to
audit, nothing to version, and no way to show WHY an attempt failed.**

🟢 **The recipe — the rubric is a table, the model is a worker:**

| layer | repo / artefact | licence | why this one |
|---|---|---|---|
| 1. **Platform + rubric store** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** *(`LICENSE`, 1 062 B, body-read p158)* | 🟢 **Ships `aiJudgeConfigurations`, `aiJudgeCriteria`, `aiJudgeScoreGuidance`, `aiJudgeBlockingErrors` and per-judgement tables.** 🔵 **Rubric criteria, score guidance and HARD-FAIL conditions are database rows — the only artefact on this shelf that models a grading decision as data** |
| 2. **Tenancy boundary** | same — PostgreSQL 16 **Row-Level Security** | 🟢 MIT | 🟢 **Least-privilege runtime role; *"a bug in application code cannot read another tenant's rows."*** 🔵 **One deployment, many districts or many group companies** |
| 3. **Mastery evidence, independent of the judge** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | 🟢 **DKT / AKT / SAKT knowledge tracing.** 🔵 **A SECOND, non-LLM estimate of whether the learner knows it — so the human reviewer sees two instruments, not one** |
| 4. **Verification, not generation** | `P156-D`'s pattern | — | 🟢 **The model proposes; the rubric row decides; the human signs** |
| 5. **Trace** | **Langfuse** *(already wired in `mentingo`)* | — | 🟢 **Per-judgement traces are the audit artefact a regulator or an appeal actually asks for** |

🟢 **Wiring, concretely:**
1. 🟢 **Author the rubric as rows** — one `aiJudgeCriteria` row per criterion, `aiJudgeScoreGuidance` for the band descriptors, and `aiJudgeBlockingErrors` for conditions that fail the attempt **regardless of total score** *(the plagiarism case, the safety-critical procedural error, the mandatory-training miss)*.
2. 🟢 **The model scores against criteria it cannot edit.** 🔵 **The prompt carries the criteria; the criteria do not live in the prompt.**
3. 🟢 **`pykt-toolkit` consumes the interaction stream** and returns a mastery estimate from the learner's history, computed without the LLM.
4. 🔴 **Nothing auto-decides.** 🟢 **A judgement row plus its blocking-error rows plus the mastery estimate render as a reviewer's queue item; the human's sign-off is the decision of record.**
5. 🟢 **Langfuse holds the trace; the judgement tables hold the reasons.** 🔵 **Versioned rubric rows mean *"what was the rule when this attempt was graded?"* has an answer.**

🔴 **The boundary, stated because `p158` found it the hard way:** 🔴 **`mentingo` does NOT speak
LTI 1.3 or xAPI** — 🟢 **`0` occurrences in a `104`-table schema, confirmed p158.**
🟢 **So this pattern is for CORPORATE L&D, compliance training and greenfield K-12/HE builds
where `mentingo` IS the platform.** 🔴 **For an institution with an existing LMS estate, keep
`P156-A`: Moodle or Open edX unmodified at layer 1, federated over LTI 1.3 + AGS, and take the
rubric idea across as your own tables.**

🟢 **Sell it as:** 🟢 **North America — district AI-policy compliance for Maryland, Idaho,
Oklahoma and Virginia, where the mandate is per-district and repeats hundreds of times; Ohio and
Tennessee as remediation, the `2026-07-01` deadline having passed.** 🟢 **EMEA — Annex III
readiness, architected to `2026-08-02` and relieved if `2027-12-02` holds.**
🟢 **Timeline: 6–8 weeks** *(rubric modelling 2, judge + review queue 3, `pykt` integration 2,
overlapping)*.

---

## 🆕 🔴 `P158-B` — the licence gate, CORRECTED to classify by family and to prove the repository exists *(new, p158 — Global; supersedes the probe in `P157-B` and `P156-E`)*

🔵 **The problem this solves:** 🔴 **`P156-E` and `P157-B` test whether a licence file EXISTS.
p158 showed that test is wrong twice over.**
🔴 **`10 of 10` `NOASSERTION` rows have licence files — and `6` of them forbid commercial use.**
🔴 **And two nonexistent repository names produced exactly the output a licence-less repository
produces, so absence was being read out of a `404` that meant *"no such repo."***

🟢 **The corrected gate — four steps, in this order, and the order is the fix:**

```bash
REPO="owner/name"

# STEP 0 (NEW, P54) — does it exist? A 404 means nothing until this passes.
BR=$(git ls-remote --symref "https://github.com/$REPO" HEAD 2>/dev/null \
     | awk '/^ref:/{sub("refs/heads/","",$2); print $2}')
[ -z "$BR" ] && { echo "$REPO: DOES NOT EXIST OR IS PRIVATE — not a finding"; exit 1; }

# STEP 1 (P53) — probe the repo's OWN default branch, not "main".
for p in LICENSE LICENSE.md LICENSE.txt LICENCE LICENSE-MIT COPYING COPYING.LESSER license LICENSE.rst; do
  curl -sf "https://raw.githubusercontent.com/$REPO/$BR/$p" -o /tmp/lic && { echo "BODY: $p"; break; }
done

# STEP 2 (P48 + T124) — classify by the FAMILY NAME LINE, never by size or by the sidebar.
head -5 /tmp/lic | grep -iE \
 'MIT License|Apache License|BSD [0-9]|GNU (Affero|Lesser)? ?General Public|Mozilla Public|\
Business Source License|PolyForm (Noncommercial|Strict|Perimeter)|Elastic License|\
Server Side Public|All rights reserved|Community License'

# STEP 3 — the four-tier verdict (P51, extended by p158).
```

🟢 **The four tiers, and what a studio does with each:**

| tier | signature | verdict |
|---|---|---|
| 🟢 **Permissive** | `MIT`, `Apache License 2.0`, `BSD`, `CC0` | 🟢 **Ship** |
| 🔴 **Copyleft** | `GNU General Public`, `GNU Affero` | 🟡 **Ship only across a process/protocol boundary** *(`P156-A`)*. 🔴 **AGPL: HOSTING is distribution** |
| 🆕 🔴 **Source-available by DESIGN** | 🔴 **`Business Source License`, `PolyForm Noncommercial`, `PolyForm Strict`, `Elastic License`, `Server Side Public`, anything named `… Community License`** | 🔴 **STOP. A client engagement is commercial use.** 🔵 **Do not open an issue — the author has already decided** |
| 🔴 **No grant** | 🔴 **`All rights reserved`, or nothing on 9 paths after STEP 0 passed** | 🔴 **Default all-rights-reserved.** 🟡 **A README MIT sentence is INTENT, not a grant** *(`T117`: `8` instances across p157–p158)* |

🔴 **Two traps this gate now catches that the old one did not:**
- 🔴 **`CaviraOSS/PageLM` opens with MIT's literal grant sentence and is titled *"PageLM Community License"* — non-commercial and REVOCABLE.** 🟢 **STEP 2 reads the title line, so it fires.**
- 🔴 **`andremadstop/learning-nc`'s `LICENSE` is `723 B`** — 🟢 **the AGPL HEADER notice, not the licence. 🔵 **A body under `~1 000 B` for a long-form family means the text is incomplete; record it as unresolved, not as AGPL.**

🟢 **Cost: one `ls-remote` and at most nine `curl`s per repository.** 🟢 **`33` repositories were
gated this way in p158 with zero clones.**

---

## 🆕 🟢 `P158-C` — find the repository BEFORE the star sort does *(new, p158 — Global; APAC-weighted in practice)*

🔵 **The problem this solves:** 🔴 **a star-sorted topic view shows a studio what was popular last
year.** 🔴 **Five passes of mandated web queries returned listicles and courses and not one
education repository** *(`P143-L`)*.

🟢 **The recipe — one search call, run every pass:**

```
topic:ai-tutor created:>YYYY-MM-DD stars:>10     # sort=stars, order=desc
topic:edtech   created:>YYYY-MM-DD stars:>20
topic:ai-education / topic:knowledge-tracing / topic:learning-analytics
```

🟢 **What it returned on `2026-10-12`, with every licence read from the body:**

| row | ★ | licence | what to do with it |
|---|---|---|---|
| 🟢 [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | **894** | 🟢 **MIT** | 🟢 **Study the route-planning + spaced-repetition loop; `894 ★` in ~25 days means the UX is landing** |
| 🟢 [`VeryMath/VeryMath-textbook-copilot`](https://github.com/VeryMath/VeryMath-textbook-copilot) | 18 | 🟢 **Apache-2.0** | 🟢 **Drives a coding agent over ACP as the teaching engine and emits LaTeX Beamer courseware.** 🔵 **The most directly reusable new row for content production** |
| 🟢 [`wildcat430524/StepsToGreat`](https://github.com/wildcat430524/StepsToGreat) | 22 | 🟢 **MIT** | 🟢 **A Markdown teaching protocol — compose it as a SKILL onto a governed platform** *(`P49`)*, zero runtime |
| 🟢 [`huaxx-lab/LeetLens`](https://github.com/huaxx-lab/LeetLens) | 16 | 🟢 **MIT** | 🟢 **FSRS against real submission history — the scheduling component, not the whole app** |

🔴 **Run `P158-B` on every row before any of it enters a deliverable**, and 🔴 **discount for age:
these are weeks old, single-author, and have no maintenance record.** 🔵 **Use them as
components and references; `P156-A`'s platform layer stays Moodle, Open edX, OpenOLAT or
`mentingo`.**

🟢 **The division of channels, now a rule:** 🟢 **web search for REGULATION and market structure;
the GitHub search API for CODE.** 🔴 **Using either for the other's job is five passes of nulls.**

---

## 🆕 🟢 `P157-A` — the efficacy-evidence stack, and it closes a gap by COMPOSITION rather than by finding a product *(new, p157 — Global)*

🔵 **The problem this solves:** 🔴 **2026 buyers increasingly require evidence that a tool
improves learning before they purchase, and there is NO tutor evaluation harness in open
source** — 🔴 **a direct search this pass matched `122` repositories and `0 of 15` top rows were
on-domain.** 🟢 **But the three pieces needed to MEASURE an intervention all exist, are
permissive, and nobody has wired them together.**

🟢 **The recipe — three permissive repos and the LMS the client already runs:**

| layer | repo | licence *(body-read this pass)* | what it contributes |
|---|---|---|---|
| 1. **Experiment design and assignment** | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | 🟢 **Apache-2.0** (`LICENSE`, 11 323 B, resolves on `main` and `master`) | 🟢 **A randomised-controlled-trial plug-in FOR the LMS. It does condition assignment, consent and treatment delivery inside the course the student is already in.** 🔵 **This is the piece everyone assumes does not exist** |
| 2. **Evidence capture** | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **MIT** (🆕 `LICENSE.md`, 1 094 B — 🔴 **plain `LICENSE` is `404`, a `P50` instance**) | 🟢 **A Learning Record Store: xAPI statements in, queryable learning records out.** 🟢 **MIT, so the pipeline ships inside a client product** |
| 3. **Mastery estimate** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** (`LICENSE`, 1 066 B) · 446 ★ | 🟢 **DKT / AKT / SAKT knowledge tracing — turns the interaction stream into a mastery trajectory instead of a post-test score** |
| 4. **System of record** | the client's Moodle / Open edX / Canvas / Sakai | 🔴 copyleft — **untouched** | 🟢 **Roster, gradebook and enrolment stay authoritative.** 🟢 **Terracotta attaches as an LTI 1.3 tool, so no fork** |

🟢 **Wiring, concretely:**
1. 🟢 **Terracotta is registered as an LTI 1.3 tool in the LMS.** A course's experiment defines
   conditions (e.g. tutor-assisted vs control) and Terracotta handles consent and random
   assignment per student, inside the normal course flow.
2. 🟢 **The tutoring surface under test** — `DeepTutor` (Apache-2.0) or `ai-shifu`
   (Apache-2.0), or the `P156-A` composition — **emits xAPI statements for every interaction**
   to `ralph`.
3. 🟢 **`ralph` stores the statements and exposes them for query**; the LMS gradebook supplies
   outcomes back through **LTI AGS**.
4. 🟢 **`pykt-toolkit` consumes the per-learner interaction sequence from `ralph` and returns a
   mastery trajectory**, so the comparison between arms is a learning curve rather than a single
   score.
5. 🟢 **The deliverable is a pre-registered result on the client's own students** — 🔵 **which is
   the artefact a procurement committee asked for and no vendor can supply about someone
   else's cohort.**

🟢 **Licence posture: layers 1–3 are Apache-2.0 / MIT / MIT.** 🟢 **Nothing links against the
LMS's GPL or AGPL code** — Terracotta attaches over LTI, which is a protocol boundary.
🔵 **So the whole harness is permissive and the client keeps their platform.**

🔵 **Why this is the most defensible thing on this shelf:** 🔴 **every competitor sells a tutor.**
🟢 **This sells the evidence that the tutor worked** — 🟢 **and `terracotta` at `21 ★` means
nobody is competing for it.**

## 🆕 🟢 `P157-B` — the licence gate, as a procedure a studio can actually run before a repo enters a deliverable *(new, p157 — Global)*

🔵 **The problem this solves:** 🔴 **this pass measured three instruments giving three different
answers about the same four repositories** *(`T117`)*, and 🔴 **three repositories whose licence
a single-channel probe declared absent and which are in fact licensed** *(`P53`)*.
🔴 **Either error, shipped, is a legal finding on a client engagement.**

🟢 **The gate — four checks, all free, none needing a clone:**

| # | check | channel | what it catches |
|---|---|---|---|
| 1 | 🟢 **Resolve `default_branch` FIRST** | GitHub metadata *(`search_repositories`)* | 🔴 **`P53`. Three instances this pass, all `master`-default: `openbadgeslib`, `my-learning-analytics`, `openedx/edx-platform`.** 🔵 **Older and institutional repositories are exactly the foundational tier, and they are exactly the ones still on `master`** |
| 2 | 🟢 **Read the licence BODY on `raw`, probing `LICENSE*`, `LICENCE*`, `COPYING*` and `license`, and record the path that answered** | `raw.githubusercontent.com` | 🔴 **`P50`. `moodle` keeps the GPL in `COPYING.txt`; `ralph` only in `LICENSE.md`.** 🔴 **A sweep stopping at `LICENSE` publishes *"Moodle: no licence"*** |
| 3 | 🟢 **Compare the body against the metadata `license` field and treat ANY disagreement as an unfinished measurement** | both | 🔴 **`T117`. This is what caught `P53` twice.** 🔴 **Never break the tie by preferring a channel — go find the ref or the path** |
| 4 | 🟢 **If no licence file exists, read the README for a prose claim, then enumerate refs with `ls-remote` and re-probe** | `raw` + `git ls-remote` | 🔴 **`P51`'s three tiers. `4 of 15` rows claim MIT in prose with no licence text; `2 of 15` explicitly DECLINE to grant; `9 of 15` say nothing at all** |

🟢 **The verdict is one of four values, not two:**

| verdict | what it means commercially |
|---|---|
| 🟢 **GRANTED — body read, family identified** | 🟢 **Proceed under that licence's terms** |
| 🟡 **CLAIMED — prose only, no licence text** | 🟡 **Open an issue asking the author to add the file. Do NOT ship until they do.** 🔵 **Usually a one-day fix, and it converts the row** |
| 🔴 **DECLINED — the author states private, personal-use or non-commercial** | 🔴 **Stop. No amount of stars changes it.** 🔵 **`PageLM` at `2 029 ★` is this** |
| 🔴 **UNKNOWN — nothing, on any ref or path** | 🔴 **Default all-rights-reserved. Treat as closed source** |

🔵 **The cost of the gate is four cheap calls per repository.** 🔴 **The cost of skipping it,
measured on this shelf's own history, is a published claim that the most-deployed LMS in the
world has no licence, and a published claim that the reference implementation of Open Badges 3.0
has none either.** 🟢 **Both were caught by check 1 or 3.**

## 🆕 🟢 `P157-C` — the credentialing product, built because there is nothing to adopt *(new, p157 — Global, strongest in EMEA and LATAM)*

🔵 **The demand:** 🟢 **2026 trend sources name digital credentials and micro-credentials against
employer skills-based hiring.**
🔵 **The supply:** 🔴 **`29` repositories in the whole `topic:open-badges` population, an `85 ★`
ceiling, and the standards-complete library at `1 ★`.**
🟢 **So this is the one lane on this shelf where the correct advice is BUILD, and where a studio
could plausibly own the reference implementation.**

🟢 **The recipe — the standard does the hard part, so the build is integration, not invention:**

| layer | repo / standard | licence | role |
|---|---|---|---|
| 1. **Issue / verify / revoke** | [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) | 🟡 **LGPL-3.0** (🆕 `master/LICENSE.txt`, 7 650 B) | 🟢 **Open Badges 3.0 as W3C Verifiable Credentials: JWT-VC issuance, verification, and Bitstring Status List revocation.** 🟡 **LGPL — LINK it as a library, do not modify it, and the product stays yours** |
| 2. **Author the achievement** | [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **MIT** (`LICENSE`, 1 080 B) | 🟢 **A Vue widget for defining an Open Badge 3.0 achievement — the authoring surface, already built** |
| 3. **Decide WHEN to award** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | 🟢 **A mastery threshold from a knowledge-tracing model, not a course-completion tick.** 🔵 **This is the differentiator: a credential backed by a learner model rather than by attendance** |
| 4. **Evidence trail** | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **MIT** | 🟢 **The xAPI record that substantiates the claim if an employer or auditor challenges it** |
| 5. **Where it attaches** | the client's LMS over **LTI 1.3 + AGS** | 🔴 copyleft, untouched | 🟢 **Grades and completion come from the system of record** |

🟢 **Wiring:** 🟢 **`ralph` accumulates interaction evidence → `pykt-toolkit` returns a mastery
estimate → crossing the threshold triggers `openbadgeslib` to issue a signed Open Badges 3.0
credential whose achievement definition was authored in the `OB3DefinitionWidget` → the badge is
verifiable by any W3C VC verifier, with the `ralph` record as the evidence trail → revocation
runs through the Bitstring Status List.**

🟢 **Licence posture: one LGPL library LINKED (layer 1), everything else MIT.** 🟢 **The
deliverable stays the client's.** 🔴 **Do not vendor the LGPL source into the product tree —
link it, and say so in the SBOM.**

🔵 **Regional fit:** 🟢 **EMEA** — a credential is a pedagogical artefact, not an evaluative
decision, so it sits on the permitted side of the Commission's `2026-05-19` line *(and a
credential that automatically gates access to education would cross it, which is the design
constraint)*. 🟢 **LATAM** — the UNESCO LAC Observatory (`2026-04-14`, ECLAC Santiago) and the
`68%`-adopting / `26%`-governing public-university segment make this a regional-programme sale
rather than a per-institution one.

## 🆕 🟢 `P156-A` — the licence-safe LMS composition, and it is the same in all five regions *(new, p156 — Global)*

🔵 **The problem this solves:** 🔴 **every client already runs Moodle (GPL) or Open edX
(AGPL-3.0)**, 🔴 **so a forked-and-resold platform is a source-disclosure event** — and on Open
edX the AGPL reaches a *hosted* derivative, not just a shipped one.

🟢 **The recipe — three processes, one licence boundary:**

| layer | repo | licence | why this one |
|---|---|---|---|
| 1. **System of record** — leave it alone | [`moodle/moodle`](https://github.com/moodle/moodle) 🔴 GPL *(`COPYING.txt`)* **or** [`openedx/edx-platform`](https://github.com/openedx/edx-platform) 🔴 AGPL-3.0 | copyleft | 🟢 **Unmodified. Enrolment, gradebook and roster stay authoritative here** |
| 2. **Tutoring surface** — a separate process | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) 🟢 **MIT**, Go | 🟢 permissive | 🟢 **An Intelligent Tutoring System exposed as an MCP server** — so any host agent calls it as a tool |
| 3. **Content grounding** | [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) 🟢 **MIT**, LangGraph + FastAPI | 🟢 permissive | 🟢 **Agentic RAG over a curated course corpus — the client's own material, not the open web** |
| 4. **Mastery model** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) 🟢 **MIT** | 🟢 permissive | 🟢 **DKT / AKT / SAKT knowledge tracing — answers *"does the student know it?"* with a model, not a vibe** |
| 5. **The wire** | **LTI 1.3** *(Moodle, Open edX, Canvas, Sakai, ILIAS, Chamilo all speak it)* + the LMS REST API | — | 🟢 **A protocol boundary is not a derivative work.** 🔵 **This is the whole trick** |

🟢 **Wiring, concretely:** 🟢 **LTI 1.3 launch from the LMS carries the signed user + context
claims** → 🟢 **the agent host resolves the learner, then calls `tutor-mcp` for the pedagogy and
the `ai-tutor-app` RAG service for the course material** → 🟢 **`pykt-toolkit` consumes the
interaction stream and returns a mastery estimate** → 🟢 **grades go BACK through **LTI AGS**
(Assignment and Grade Services) so the LMS gradebook stays the system of record.**
🔴 **Nothing in layers 2–5 links against GPL or AGPL code**, so 🟢 **the deliverable stays MIT
and the client keeps their LMS.**

🔵 **If the client wants to own the platform too:** 🟢 **swap layer 1 for
[`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) (Apache-2.0) or
[`Selleo/mentingo`](https://github.com/Selleo/mentingo) (MIT)** — 🟢 **the only two LMS rows on
this shelf a studio can fork without a copyleft obligation.**

## 🆕 🟢 `P156-B` — the governance-retrofit engagement, built for the `87% / 26%` gap *(new, p156 — LATAM primary, Global applicable)*

🔵 **The demand this answers is measured, not assumed:** 🟢 **UNESCO IESALC `2026-09-09`, 200
institutions / 19 countries — `87%` already use AI, `74%` in teaching and learning, and only
`26%` have a formal AI strategy.** 🟢 **The incumbent tool is `ChatGPT` / `Copilot` / `Gemini`,
which the institution never procured** *(`T115`)*.
🔴 **So the sale is NOT another tutor.** 🟢 **It is a sanctioned path for what staff already do.**

🟢 **The recipe:**

1. 🟢 **Discovery instrument** — 🔵 **there is no open-source tool for this, and that is worth
   saying**: the audit of which assistants are already in use is a services deliverable, not a
   repo.
2. 🟢 **Sanctioned gateway** — 🟢 **a single MIT/Apache agent host in front of the models**, with
   the institution's data boundary, logging and per-role policy. 🟢 **Compose
   [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT) behind it so
   the pedagogy is a tool, not a prompt.**
3. 🟢 **Curriculum grounding** — 🟢 **[`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app)
   (MIT)** so answers cite the institution's corpus.
4. 🟢 **Policy artefact** — 🔵 **the written AI-use policy is itself the billable item in
   several jurisdictions.** 🟢 **Ohio requires one per district** *(deadline `2026-07-01`, now
   past)*; 🟢 **Oklahoma `SB 1734` requires one per district before 2027–28.**
5. 🟢 **Evidence loop** — 🟢 **[`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit)
   (MIT)** for mastery estimates, 🔴 **and a stated gap: there is still NO open-source harness
   that evaluates the TUTOR**, so the evaluation design is bespoke.

🔵 **Why this sequences well commercially:** 🟢 **steps 1 and 4 are short, funded by a compliance
line, and produce the access needed for steps 2–3.**

## 🆕 🟢 `P156-C` — the offline / data-residency build *(new, p156 — LATAM, EMEA-Africa, APAC emerging)*

🔵 **The constraint UNESCO names as the real blocker:** 🔴 **policy frameworks are useless
without reliable IT infrastructure, internet access and teacher training**, and 🔴 **parts of
APAC and Africa are still meeting basic educational needs.**
🟢 **Also the EMEA data-residency case, where Article 5 bans emotion inference in schools
outright and a cloud round-trip is the compliance question.**

🟢 **Every row MIT, every row runs with no internet:**

| layer | repo | licence |
|---|---|---|
| Platform | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) — offline-first by design | 🟢 **MIT** |
| Tutor client | [`michael-borck/study-buddy`](https://github.com/michael-borck/study-buddy) — Electron + local Ollama, no internet | 🟢 **MIT** |
| On-device mobile | [`linyeping/GemMate`](https://github.com/linyeping/GemMate) — Gemma on local hardware, Dart | 🟢 **MIT** · 🔴 **p191 CORRECTION: `Apache-2.0`** |
| Spaced repetition | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) — Anki as a tool surface | 🟢 **MIT** |
| Mastery | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** |

🟢 **Wiring:** 🟢 **Kolibri serves content on the LAN; `study-buddy` runs the tutor against a
local Ollama model; `anki-mcp-server` holds the review schedule; `pykt-toolkit` runs the mastery
model on the same box.** 🟢 **Sync to the cloud is optional and batched** — 🔵 **which is what
makes it quotable under a data-residency requirement.**

## 🆕 🟢 `P156-D` — verify the answer instead of generating it *(new, p156 — Global)*

🔵 **The 2026 buyer demand is evidence of instructional benefit, and a generative tutor cannot
produce it about its own correctness.** 🟢 **Two rows found this pass do something structurally
different:**

| repo | licence | what it verifies |
|---|---|---|
| 🔴 [`ZelinZhou-THU/stem-tutor-agent`](https://github.com/ZelinZhou-THU/stem-tutor-agent) | 🔴 **AGPL-3.0** | 🟢 **Checks each STEP of a maths solution with **SymPy** and finds the root cause, then generates targeted practice.** 🟢 **Symbolic, so the verdict is not a model's opinion** |
| 🟢 [`HumphreySun98/Smart-Study-Agent`](https://github.com/HumphreySun98/Smart-Study-Agent) | 🟢 **MIT** | 🟢 **Reinforcement learning picks the next action, **FSRS** picks the review time, and the LLM is used ONLY to write quizzes** |

🟢 **The pattern:** 🟢 **put a DETERMINISTIC judge (SymPy, a unit test, a scheduler like FSRS)
between the learner and the model**, 🟢 **and use the model only where its output is cheap to
check.** 🔵 **This is also the cheapest architecture to run, because the model is off the hot
path.**
🔴 **Licence note:** 🔴 **`stem-tutor-agent` is AGPL-3.0** — 🟢 **read it for the SymPy
step-checking approach and reimplement, or deploy it internally where AGPL's network clause is
satisfied.** 🟢 **`Smart-Study-Agent` is MIT and can ship as-is.**

## 🆕 🔴 `P156-E` — the licence gate that must run BEFORE any of the above *(new, p156 — Global)*

🔴 **`17 of 80` rows on `topic:ai-tutor` cannot be used by a studio, and the topic page shows
stars, language and description for all 17 without a hint of it.**

🟢 **The gate, in order, each step cheap:**

1. 🟢 **Fetch the licence BODY** on `raw.githubusercontent.com`. 🔴 **Never trust a badge** — this
   shelf has a row whose badge contradicts its tree.
2. 🟢 **Probe `COPYING*` too, not just `LICENSE*`** *(`P50`)*. 🔴 **`moodle/moodle` returns 404 on
   six `LICENSE*` paths and keeps the GPL in `COPYING.txt`** — a `LICENSE*`-only sweep publishes
   *"Moodle has no licence."*
3. 🟢 **Classify on the WHOLE BODY, not the name line** *(`P48` + `T105`)*.
   🔴 **`ZelinZhou-THU/stem-tutor-agent`'s file opens with a BOM and the line *"STEM Tutor
   Agent"*, and is a full AGPL-3.0 text.**
4. 🔴 **Treat `UNCLASSIFIED` as the finding, never as a default-to-MIT** *(`T104`)*.
   🔴 **`Tzxser/aipha-learning-os` is 1 296 B — inside the MIT short-form band — and grants
   NOTHING** (*"does not make the original AIpha source open source"*).
   🔴 **`lilialla/bandwise` is PolyForm Noncommercial 1.0.0: *"SOURCE-AVAILABLE, not open
   source"*, commercial use needs a separate licence.**
5. 🟢 **Diff a suspicious preamble against UPSTREAM** *(`T116`)*. 🟢 **OpenEduCat's bundled-externals
   carve-out is verbatim Odoo boilerplate with a dangling `COPYRIGHT` pointer** — 🟢 **one fetch
   of `odoo/odoo/master/LICENSE` settles it.**
6. 🔴 **Size proves nothing** *(`P44` refuted)*: measured collisions at **32 B** (MIT vs AGPL short
   form), **138 B** (Apache vs ECL), **11 B** (GPL-3.0 vs AGPL-3.0).

🔵 **Run this before a row enters a proposal, not after.**

## 🆕 🔴 `P48` — classify a licence by its NAME LINE; the body SIZE cannot tell the families apart *(new, p155 — Global)*

🔵 **The problem this replaces.** `P44` step 4 told you to confirm a licence family by the
body's byte size. 🔴 **p155 measured three collisions that break it**, and the worst two are on
the pairs that matter most to a studio
([`evidence/band-collision.2026-10-12-p155.tsv`](../evidence/band-collision.2026-10-12-p155.tsv)):

| collision | bytes | gap | the loss |
|---|---|---|---|
| 🔴 **MIT cluster vs AGPL-3.0 SHORT FORM** | 1 062–1 102 vs **1 134** | 🔴 **32 B** | 🔴 **Strongest copyleft read as most permissive licence** |
| 🔴 **Apache-2.0 vs ECL-2.0** | 10 982 *(and 10 227–11 408 across Apache bodies)* vs **11 120** | 🔴 **138 B** — 🔴 **and the Apache range BRACKETS ECL entirely** | 🔴 ECL-2.0's narrowed patent grant |
| 🔴 **GPL-3.0 vs AGPL-3.0** | 35 147 vs **35 136** | 🔴 **11 B** | 🔴 **"Network use counts as distribution"** |

🆕 🔴 **p166 footnote on the `11 B` figure:** 🔴 **the canonical texts may sit `11 B` apart, but the
bodies THIS SHELF has actually body-read do not reproduce that adjacency — observed GPL-3.0 clusters
at `35 149 B` and observed AGPL-3.0 at `34 522`–`34 523 B`, about `626 B` apart.**
🟢 **Do not build a discriminator on either number.** 🔵 **Read the name line.**

### The recipe

**Inputs:** a repository slug. **Cost:** one `curl`.

1. 🟢 **Fetch the body on the `raw` channel** (`P45`): try branches `main`, `master`,
   `develop`, and filenames `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license.txt`, `COPYING`,
   `COPYING.txt`. 🔴 **A wrong path must `404`** or the probe proves nothing.
   🔵 **`frappe/education` is the reason `develop` and `license.txt` are both on that list,
   and `moodle/moodle` is the reason `COPYING.txt` is.**
2. 🟢 **Read the NAME LINE — the first match of the licence-name strings**, in this order:

   ```
   GNU AFFERO GENERAL PUBLIC LICENSE      ->  AGPL
   GNU LESSER GENERAL PUBLIC LICENSE      ->  LGPL
   GNU GENERAL PUBLIC LICENSE             ->  GPL
   Educational Community License          ->  ECL
   Apache License                         ->  Apache
   MIT License / BSD n-Clause / Mozilla   ->  as named
   ```

   🔴 **The order is not cosmetic.** An AGPL body contains `GNU GENERAL PUBLIC LICENSE` in its
   own preamble and an LGPL body appends the GPL text wholesale, 🔴 **so a naive order reads
   `canvas-lms` as GPL and `openeducat_erp` as GPL.** 🟢 **Pin the order with a test.**
3. 🟢 **Read the VERSION separately** (`Version 2` vs `Version 3`), because `P43`'s whole
   question lives there. 🔵 **`rosariosis` is GPL-**2**.0, not 3** — a secondary source said
   only *"GPL"*.
4. 🟢 **Use SIZE only as an ANOMALY flag, never as a confirmer:**
   - 🔴 **Body under ~2 KB that names a GNU licence → a GRANT BY REFERENCE or SHORT FORM.**
     `frappe/education` = **19 B** `License: GNU GPL V3`; `24kchengYe/human-skill-tree` =
     **1 134 B** AGPL-3.0. 🔴 **Neither is classifiable by any detector, GitHub's included.**
   - 🔴 **Body that classifies as a permissive family but is far too LARGE → a proprietary
     licence wearing a permissive opening** (`P411`: `PageLM`, 8 563 B "MIT" —
     🔴 **NON-COMMERCIAL and REVOCABLE; amended inline by `ACTION IQ`, p166**).
   - 🔴 **A size inside the right band proves nothing** — that is the whole point of this gate.
5. 🟢 **Then run `P47`**: the root grant may be a property of the PATH. 🔵 **Two instances now
   — `scibly-dev/scibly` (`ee/` proprietary) and `openeducat/openeducat_erp`, whose own
   preamble says bundled externals *"may be published under other GPL-compatible licenses."***
6. 🟢 **Then run `P44` step 5** — enumerate the other surfaces and compare on the FAMILY.
   🔵 **And treat a comparison article's licence column as a hypothesis** (`T96`: three of
   three platform licences were wrong or imprecise in secondary sources this pass).

🟢 **Result in production:** **19 of 19** bodies classified by name line this pass with zero
ambiguity, across MIT, Apache-2.0, ECL-2.0, LGPL-3.0, GPL-2.0, GPL-3.0, AGPL-3.0 full-text and
AGPL-3.0 short-form. 🔴 **Zero of those three collisions are detectable by size.**

---

## 🆕 🟢 `P49` — compose a pedagogy SKILL onto a governed platform *(new, p155 — Global)*

🔵 **The problem.** A studio is asked for an AI tutor. 🔴 **The two obvious answers are both
wrong:** build on the institution's LMS and inherit AGPL (Canvas, Open edX) or GPL (Moodle);
or ship a standalone app and inherit the institution's whole compliance surface with no
integration. 🟢 **`T98` supplies a third shape**, and the pieces below are all verified on this
shelf.

### The recipe

| layer | the piece | licence | why this one |
|---|---|---|---|
| 🟢 **Pedagogy** | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) *(283 ★)* or [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) *(243 ★)* | 🟢 **MIT, 1 069 B / 1 102 B** | 🟢 **A skill: no runtime, no deployment.** 🟢 **`Bloom` ships as a skill AND a hostable app — the migration path is already written** |
| 🟢 **Memory / retention** | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) *(515 ★)* | 🟢 **MIT, 1 074 B** | 🟢 **Spaced repetition as an MCP tool surface the skill can call** — retention stops being a promise |
| 🟢 **Learner model** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | 🟢 **Knowledge tracing: the evidence layer buyers now demand.** 🔵 **Feeds the diagnosis the tutor skill opens with** |
| 🟢 **Institutional boundary** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) *(Apache-2.0, 376 ★)* for LTI, or an external MCP server — [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) *(MIT, 290 ★)* | 🟢 **Apache-2.0 / MIT** | 🟢 **Nothing of Moodle's GPL or Canvas's AGPL-3.0-ONLY reaches your code** (`P43`) |
| 🟢 **Platform, if greenfield** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) *(92 ★)* · [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **MIT, 1 062 B** · 🟢 **Apache-2.0, 10 982 B** | 🟢 **The two permissive substrates.** 🔵 `mentingo` for fork-and-own, `OpenOLAT` for institutional procurement |
| 🟢 **SIS inputs** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** | 🟢 **Attendance/grades/scheduling for dropout prediction** — 🔴 **go out to its API, never build inside** |

### Wiring it

1. 🟢 **The skill is the product and it holds the pedagogy only.** Diagnose, then teach — the
   shape `universal-diagnostic-tutor-skill` ships.
2. 🟢 **The host agent supplies model, memory and tool access.** 🔵 **This is why the skill
   layer costs almost nothing to deliver and almost nothing to license.**
3. 🟢 **The boundary layer carries every institutional duty the skill cannot:** FERPA logging
   (`zavora-ai/mcp-student-records`' demonstrable artefact), the EU AI Act deployer duties, the
   human-approval gate Oklahoma `SB 1734` requires, and the parental opt-out.
   🔴 **A skill cannot be a data controller. Do not pretend otherwise.**
4. 🟢 **`pyKT` closes the loop** and produces the evaluation evidence the 2026 buyer asks for
   before purchase.
5. 🔴 **Run `P48` on every row before you ship**, and 🔴 **`P47` on any row with a carve-out.**

🔵 **Why this sells.** 🟢 **EMEA:** keep the skill on the pedagogical side of the
`2026-05-19` Commission guideline line and the Annex III high-risk tier does not attach;
the boundary layer carries the FRIA when it does. 🟢 **North America:** Oklahoma `SB 1734`'s
approval gate and opt-out live in the boundary layer, so one architecture serves every district
on a statutory deadline. 🟢 **LATAM:** IESALC's 87%-doing / 26%-governing gap is a governance
sale, and this shape makes governance a separable, auditable layer. 🟢 **APAC:** Korea's pilot
year is design time, and Vietnam's extraterritorial high-risk classification lands on the
boundary layer — which is where you want it.

🔴 **What this pattern does NOT solve:** 🔴 **region placement is unverified for most skill
rows** (`ACTION HA`), 🔴 **`mentingo` is unassessed beyond licence and stars** (`ACTION HC`),
and 🔴 **no credentialing piece exists on this shelf at all** (`ACTION HE`).


## 🆕 🟢 `P46` — measure the POPULATION in one call, then spend the body-reads where they matter *(new, p154 — Global)*

🔵 **The problem this replaces.** p153 priced a ten-row shelf at **one rendered-page fetch per
repository for stars** plus **one shallow clone per repository for a licence**. 🟢 **The
authenticated GitHub API returns stars, forks, topics, language, `pushed_at` AND GitHub's
detected licence for up to 100 repositories in a single call.** 🔴 **What it will NOT do is
read a third-party file** — `get_file_contents` refuses any repository not attached to the
session. 🟢 **So the API tells you WHICH bodies to read, and the body channel reads them.**

### The recipe

**Inputs:** an industry and the narrow topics that name it.
**Cost:** 1 call per topic + 1 `ls-remote` per shortlisted row + 1 raw fetch per FLAGGED row.

1. 🟢 **Enumerate by NARROW topic, never by free text** (`T95`).
   `topic:ai-tutor` · `topic:edtech` · `topic:knowledge-tracing` ·
   `topic:intelligent-tutoring-system` · `topic:grading`.
   🔴 **`topic:a OR topic:b` is REJECTED** — *"logical operators only apply to text, not to
   qualifiers"* — so budget one call per topic.
   🔴 **And do not reach for the broad topic**: `topic:education` scored **50%** on-domain
   against `topic:ai-tutor`'s **93%**.
2. 🔴 **Never let a short generic term into an `OR` over `in:name,description`.**
   `moodle OR canvas-lms OR lms OR openedx mcp` returned **60 059 rows** of generic MCP
   infrastructure. 🟢 **An `OR` of a three-letter token is a sieve with no mesh.**
3. 🟢 **Sort by stars, request `perPage: 30`, and ask for the FULL output.**
   🔴 **The minimal output omits the `license` object entirely** — which is the one field this
   pattern exists to collect.
4. 🟢 **Triage on the licence field into THREE buckets, not two.**
   - 🟢 **a real SPDX id** (`MIT`, `Apache-2.0`, `BSD-3-Clause`, …) → shortlist; body-read only
     before you quote it (`P38`).
   - 🟡 **`"spdx_id": "NOASSERTION"`** → 🟢 **a licence file EXISTS and could not be matched.
     THIS IS THE HIGH-VALUE BUCKET.** Every bespoke, open-core and proprietary-masquerading
     licence this shelf has been burned by lands here: `PageLM` (`P411` —
     🔴 **NON-COMMERCIAL and REVOCABLE; amended inline by `ACTION IQ`, p166**), `scibly` (`T92`).
     🔴 **Read the body. Always.**
   - 🔴 **the `license` key ABSENT** → no licence file at all. 🔴 **No grant: do not ship.**
     3 of 3 such rows were confirmed by probing 8 paths each this pass.
5. 🟢 **Verify existence and `HEAD` with `ls-remote`, and parse it correctly** (`T94`).
   `git ls-remote <url> HEAD` can return **two lines** — `i-educar` advertises
   `refs/remotes/origin/HEAD`. 🔴 **Match `\tHEAD$`; never `head -1`**, because order is not
   guaranteed. 🔴 **Include a slug that cannot exist**; if it returns a SHA, void the run.
6. 🟢 **Read freshness from `pushed_at`, never `updated_at`** (`T93`) — they were **115 days**
   apart on the first row tested.
7. 🟢 **Publish the whole population, not the shortlist.** The 248-row TSV is what lets the
   next pass say "40% of this was already on the shelf" instead of guessing.

### 🟢 What it bought, measured on this pass

| | p153's way | 🆕 `P46` |
|---|---|---|
| 248 rows measured for ★ + licence | 🔴 **~496 round trips** (248 fetches + 248 clones) | 🟢 **10 calls** |
| bodies actually read | 10 clones | 🟢 **5 raw fetches, aimed by the triage** |
| rows found that the shelf lacked | — | **6 new, on-domain, ≥30 ★** |
| known-liar row re-tested | `lumen` needed a clone | 🟢 **the API returned `GPL-3.0` directly** |

🔴 **What it does not buy.** 🔴 **The licence field is a DETECTED surface, not the governing
one.** It agreed with the tree on 6 of 6 rows this pass, including the one row whose badge
lies — 🔴 **but six observations are not a law, and `P38` still forbids quoting a licence you
have not read from the body.**

---

## 🆕 🔴 `P47` — the PATH-LICENCE gate: before you fork, ask which DIRECTORY you are standing in *(new, p154 — all regions)*

🔴 **The instance that forces this pattern:** `scibly-dev/scibly` — an AI-native learning
platform — is **AGPL-3.0 at its root and PROPRIETARY, non-production-only, inside `ee/`.**
🔴 **A scanner that reads one root `LICENSE` reports "AGPL-3.0" and is wrong about part of the
tree.** 🔴 **And `P44`'s size check PASSES on it**: 34 739 B is inside the AGPL band, so the
check confirms a conclusion that holds only outside `ee/`.

🔵 **Why a pattern and not a footnote.** 🟢 **Open core is the dominant commercial shape in
education software** — a permissive or copyleft core with an enterprise directory — and this
shelf's entire licence model assigns **one licence per repository**. 🔴 **That model cannot
represent the thing it is auditing.**

### The recipe

**Inputs:** a repository you intend to fork, vendor or ship.
**Cost:** 1 raw fetch for the root body + 1 per carve-out named + 1 directory listing.

1. 🟢 **Read the root body FIRST — the whole body, not the first marker.**
   🔴 **The carve-out lives in the PREAMBLE, above the pasted licence text**, which is exactly
   where a marker-matcher never looks.
2. 🟢 **Grep the root body for carve-out grammar before you classify it.**
   `portions` · `namely` · `files that reside under` · `directory` · `licensed separately` ·
   `licensed, not sold` · `ee/` · `enterprise`.
   🟢 **One of those in the first 500 bytes means the repository has more than one licence.**
3. 🟢 **Enumerate EVERY licence file in the tree, not just the root one.**
   Probe `ee/LICENSE`, `enterprise/LICENSE`, `pro/LICENSE`, `packages/*/LICENSE`. 🔴 **A
   wrong path must 404**, or the probe proves nothing — a deliberately wrong path on
   `jupyter/nbgrader` returned **404** this pass, so the channel is honest.
4. 🔴 **Read what the enterprise licence actually PERMITS, not what it is called.**
   `scibly`'s is 1 287 B and permits *"view, copy, and modify … for non-production purposes
   only — development, testing, and evaluation."* 🔴 **That forbids the only thing a client
   engagement does with code.**
5. 🟢 **Record the licence as a PAIR, path → licence**, in the evidence TSV. A single-valued
   licence column is a data-model bug once `T92` is known.
6. 🔴 **Decide BEFORE the first sprint, not before go-live** (`P28`'s lesson, one level up).
   The decision is: 🟢 **use the core only and delete the enterprise directory in your fork**,
   🟢 **buy the enterprise grant**, or 🔴 **walk away** — and the first of those requires a CI
   check that the directory never reappears through a merge.

### 🟢 The gate as a one-liner a studio can actually run

```bash
# flag every candidate whose root licence carves out a path, and list the inner licences
for slug in $(cat candidates.txt); do
  body=$(curl -s "https://raw.githubusercontent.com/$slug/main/LICENSE")
  echo "$body" | head -c 500 | grep -qiE 'portions|namely|reside under|licensed separately|licensed, not sold' \
    && echo "PATH-LICENCE SUSPECT: $slug"
done
```

🔴 **Run it on every `NOASSERTION` row the API returns** (`P46` step 4), because that is where
these live: 🟡 **32 of this pass's 248 rows are `NOASSERTION`, and exactly one has been
opened.** 🔵 **`ACTION GS`.**

### 🔴 Which of this shelf's rows must go through this gate

| row | ★ | why |
|---|---|---|
| 🔴 [`scibly-dev/scibly`](https://github.com/scibly-dev/scibly) | 42 | 🔴 **CONFIRMED path-licensed.** AGPL-3.0 + proprietary `ee/` |
| 🔴 [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 2 029 | 🔴 `P411`'s casualty: a proprietary licence opening with the MIT grant verbatim, 8 563 B |
| 🟡 [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 340 | 🟡 `NOASSERTION`, AI-native higher-ed platform, UNREAD |
| 🟡 [`inducer/relate`](https://github.com/inducer/relate) | 437 | 🟡 `NOASSERTION`, course + assessment environment, UNREAD |
| 🟡 [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 243 | 🟡 `NOASSERTION`, secure assessment, UNREAD |
| 🟡 [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | 849 | 🟡 `NOASSERTION`, 165 teacher-facing skills, UNREAD |
| 🟡 [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 159 | 🟡 `NOASSERTION`, *"the data layer for smarter educational AI"*, UNREAD |

## 🆕 🟢 `P44` — audit the licence SURFACES before you shortlist, because the badge can lie *(new, p153 — all regions)*

🔴 **The instance that forces this pattern:** `ahmedEid1/lumen` — 88 ★, the only complete
learner-facing product in this shelf's agent tier — **declares MIT on its README badge and
in `apps/backend/pyproject.toml`, and ships a GPL-3.0 `LICENSE`.** 🔴 **Two of three
surfaces are wrong and both wrong ones understate copyleft.**

🔵 **Why a pattern and not a warning.** A shortlist is built from front doors: a badge, a
sidebar, a package manifest. 🟢 **All three are derived surfaces. Exactly one governs.**

### The recipe

**Inputs:** a candidate list of repository slugs.
**Cost:** one shallow clone per candidate, or 🟢 **one `raw` fetch per candidate if you only
need the body** (`P45`).

1. 🟢 **Verify existence and freshness without a clone.**
   `git ls-remote <url> HEAD` → existence + `HEAD` SHA, one round trip.
   🔴 **Include a slug that cannot exist.** If it returns a SHA, your channel is lying and
   every row is void.
2. 🟢 **Read the licence BODY, not a label.**
   `raw.githubusercontent.com/<owner>/<repo>/<branch>/LICENSE` — try `main`, `master`,
   `develop`, and the filenames `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license.txt`,
   `COPYING`, `COPYING.txt`. 🔴 **A wrong path must 404**, or the probe proves nothing.
3. 🟢 **Classify by distinctive marker, AGPL before LGPL before GPL.**
   🔴 **An AGPL body contains the string `GNU GENERAL PUBLIC LICENSE` in its own preamble**,
   so a naive marker order reads `canvas-lms` as GPL. Pin the order with a test.
4. 🟢 **Check the body SIZE against the family.** MIT ≈ **1 062–1 105 B**, Apache-2.0 ≈
   🆕 🔴 **CORRECTED by p166 — the bands published here were too narrow and this shelf's own
   evidence already contradicted them.** 🟢 **Measured, body-read, on this shelf:**
   Apache-2.0 = **10 173 B** *(appendix-less variant — `edfi-oneroster`)* **· 11 342 B · 11 408 B**;
   GPL-3.0 = **35 149 B** *(reproduced on TWO repositories: `tutor-gpt` p165, `moodle-enrol_oneroster`
   p166)*; AGPL-3.0 = **34 522–34 523 B**.
   🔴 **The Apache-2.0 spread is `1 235 B` wide and BIMODAL: bodies that carry the
   *"APPENDIX: How to apply the Apache License"* section run ~`11.3`–`11.4 KB`; bodies that end at
   *"END OF TERMS AND CONDITIONS"* run ~`10.2 KB`. Both are Apache-2.0.**
   🔵 **Which is the point of this gate: these corrections make the size test LESS usable, not
   more, and `P48`'s thesis — classify by the NAME LINE — is strengthened by every one of them.**
   🔴 **A 1 070-byte file that classifies MIT is probably MIT; an 8 563-byte one that
   classifies MIT is `PageLM`** (`P411`) — a proprietary licence opening with the MIT grant
   verbatim. 🔴 **And a ~20-byte file is a GRANT BY REFERENCE** (`frappe/education`:
   `License: GNU GPL V3`) which no detector can classify, GitHub's included.
5. 🟢 **Enumerate the OTHER surfaces and compare on the FAMILY.**
   Badge (`README`), metadata (`package.json`, `pyproject.toml`, `Cargo.toml`,
   `composer.json`, `setup.py` — 🔵 **including one level into `apps/`, `packages/`,
   `services/`, which is where `lumen` hides its contradiction**), and
   `SPDX-License-Identifier` headers.
   🔴 **Decode the badge first.** shields.io escapes `-` as `--` and `_` as space:
   `license-Apache--2.0-blue.svg` **is** `Apache-2.0`, and a non-greedy capture reads
   `Apache`, 🔴 **which manufactures a false contradiction** (`T90` — this shelf published
   one before catching it).
   🟢 **Compare on the family**, so `-only` vs `-or-later` is not a disagreement — that is a
   separate question (`T81`, and `P43` decides on it).
6. 🟢 **Report, do not resolve.** `SINGLE` / `AGREE` / `DISAGREE` / `UNCLASSIFIED` /
   `NONE`. 🔴 **A `DISAGREE` is a legal question**, and an unclassifiable body is
   `UNCLASSIFIED`, 🔴 **never silent agreement** (`P42`).

### The decision it produces

| verdict | what to do |
|---|---|
| 🟢 `AGREE`, permissive | 🟢 **Shortlist.** 8 of 10 agent-tier rows |
| 🔴 `DISAGREE` | 🔴 **Treat the FILE as binding.** 🟢 Read it as a reference architecture; 🔴 **do not fork** unless the deliverable can carry the file's licence |
| 🔴 `NONE` (0 surfaces) | 🔴 **Not shippable.** `hesham0-0nasser/tutor-lms-mcp` — useful reading, undeliverable |
| 🟡 `UNCLASSIFIED` / grant-by-reference | 🟡 **Usable, unquotable.** Clone and read, or ask the maintainer. 🔴 **Never put it in a proposal from a table** |

### Wire-up

- 🟢 **Instrument:** [`p153-declaration-surfaces`](code/p153-declaration-surfaces/README.md)
  — `surfaces.py` + **36 offline tests**, no network.
- 🟢 **Put it in CI as a gate** over the client's own dependency list, the way `P35` gates a
  manifest contract: a new dependency whose surfaces `DISAGREE` fails the build.
- 🟢 **Evidence shape:** one TSV row per subject with every surface and its location
  (`evidence/declaration-surfaces.2026-10-12-p153.tsv`), so a reviewer can re-read the file
  you read.

### 🔴 What it does not do

🔴 **It does not resolve a contradiction**, rank by fitness, or read a licence out of a
release asset. 🔴 **`SPDX` coverage is sampled** (capped at 4 000 source files per subject),
so on a large tree that surface is a sample. 🔴 **And it says nothing about vendored
files** — a notice inside `node_modules/` is somebody else's grant (`T86`, `ACTION GF`).

---

## 🆕 🟢 `P45` — size the population with `ls-remote` BEFORE you spend clone budget *(new, p153 — Global)*

🔴 **The instance:** p152 spent **2.4 GB** and most of a pass's budget on six clones, and
**nine of fourteen pre-registered actions went unreached because of it**. 🔴 **p153 then
re-cloned from scratch, because the container is ephemeral and clones do not persist.**

🟢 **The fix is to separate three questions that a clone answers all at once, expensively:**

| question | cheap channel | cost |
|---|---|---|
| **Does it exist? Is it fresh?** | 🟢 `git ls-remote <url> HEAD` | 1 round trip, **no tree** |
| **What is its licence?** | 🟢 `raw.githubusercontent.com/<o>/<r>/<br>/LICENSE` | 1 round trip, **no clone** |
| **How many stars / forks?** | 🟢 `WebFetch github.com/<o>/<r>` | 1 render |
| **What is IN the tree?** | 🔴 `git clone --depth 1 --single-branch` | 🔴 **the whole tree** |

🟢 **Measured this pass: 18 of 18 `ls-remote` OK and 16 of 18 licences read, with zero
clones.** 🟢 **The agent tier's 10 clones cost 187 MB** — spent deliberately, because the
surface audit genuinely needs the tree.

### The recipe

1. 🟢 **`ls-remote` the whole candidate list**, with a non-existent slug as a control.
   🔴 **If the control returns a SHA, stop.**
2. 🟢 **`raw`-fetch the licence body** for every survivor; record **body bytes** alongside
   the classification (`P44` step 4).
3. 🟢 **Now decide what deserves a clone.** Only questions that need file-level evidence —
   a surface audit, a notice census, a gate detector, a test run.
4. 🟢 **Record the clone cost in the pass's own evidence**, so the next pass budgets from a
   number instead of a feeling: *"10 of 10 OK, 187 MB, under a minute,
   `--depth 1 --single-branch`."*
5. 🔴 **Assume the clones are GONE next pass.** 🔵 Never pre-register an action whose plan
   begins *"starting from the clones already on disk"*.

### 🔴 The channel rule this pattern depends on

🔴 **Never write "the GitHub channel".** This pass measured **five different answers from
one host**:

| URL class | `curl` | `WebFetch` | `git` |
|---|---|---|---|
| `github.com/<o>/<r>` | 🔴 **403** | 🟢 renders | 🟢 `ls-remote` OK |
| `raw.githubusercontent.com/…/LICENSE` | 🟢 **200** | — | — |
| `github.com/…/releases/download/<tag>/<file>` | 🟢 **302 → 206** | — | — |
| `github.com/…/releases/expanded_assets/<tag>` | 🔴 **403** | 🔴 absent from page | — |
| `api.github.com/repos/…` | 🔴 refused | 🔴 refused | — |

🟢 **Name the exact URL refused and the exact URL that answered** (`ACTION GE2`). 🔵 **p152
wrote that a releases page "collapses" its asset lists; it does not — the endpoint that
fills them returns 403 to this session.** 🔴 **A sentence about a "channel" hid a fact about
one path.**

---

## 🆕 🟢 `P42` — never publish a ZERO without the denominator that makes it a measurement *(new, p152 — Global)*

🔴 **p151 published *"0 elections across 1 513 files"*. That figure cannot be read.** A tree
with **zero** GNU per-file notices and a tree with **16 905** notices that each decline to
elect both report "0 elections" — 🔴 **and they are opposite facts about the same question.**

🔵 **The rule**: a zero is a measurement only when the population that COULD have been
non-zero is counted beside it.

### Step 1 — name the thing that would have had to exist

🟢 For an election: a **GNU per-file notice**. For a tool count: a **router entry**.
For a region: a **region-bearing host**. 🔵 **If you cannot name it, the zero is not yet a
measurement** — it is an absence of looking.

### Step 2 — count it in the same walk, not in a second pass

🟢 `notice_files` is one `if` inside the loop that was already reading every header:

    if GNU_NOTICE.search(t):
        notices += 1

🔵 **A denominator that needs its own pass will not get written.** This one cost one line.

### Step 3 — report the pair, always, and let the classes separate themselves

🟢 **Measured over the six education verticals, the single verdict `SILENT` became four:**

| class | subject | notices | what the zero MEANS |
|---|---|---|---|
| `NO_NOTICE` | `learningequality/kolibri` | **0 of 4 350** | 🟢 permissive — nothing to elect in |
| `ROOT_ONLY` | `openedx/edx-platform` | **0 first-party** | 🟡 licence in the root file alone |
| 🔴 `DECLINING` | `instructure/canvas-lms` | 🔴 **16 905 of 19 286** | 🔴 **not silent — an election by omission** |
| `NOTICE_NO_VERSION` | p151's seven small rows | **17 of 1 513** | 🟢 GNU named, no version to elect from |

### Step 4 — go back and re-read the old zero

🟢 **The denominator re-read p151's own published null**: all **17** notice-bearing files
across the seven small rows never reach a version, and 🔴 **two rows have ZERO notices across
1 020 files.** 🟢 **`T81` still holds for them — for a cause nobody had measured.** 🔵 **A
denominator usually confirms the old finding and always changes what it means.**

### 🔴 What `P42` does NOT solve

- 🔴 **It does not tell you whose file it is.** `canvas-lms`' 16 905 notices are
  first-party; `sakai`'s 12 are not. 🔵 That is `T86` and `ACTION GF`, a different question.
- 🔴 **It does not fix a wrong matcher.** A denominator beside a blind matcher gives you a
  confident wrong answer with a population attached — 🔵 which is exactly how `T85` was
  found, and only because the denominator and the matcher disagreed.

---

## 🆕 🟢 `P43` — the FORK-LICENCE decision: read the election before you choose the platform *(new, p152 — all regions)*

🔵 **The engagement shape**: a client wants an AI layer on an open-source LMS and will fork
it. 🔴 **The licence IDENTITY (`GPL-3.0`, `AGPL-3.0`) does not decide this. The licence
TERM — the `-only` / `-or-later` election — does**, and it is readable from the tree in
under a minute per platform.

### Step 1 — clone shallow, and only the platforms actually shortlisted

    git clone --depth 1 --single-branch https://github.com/moodle/moodle          <dir>/moodle_moodle
    git clone --depth 1 --single-branch https://github.com/instructure/canvas-lms <dir>/instructure_canvas-lms

🟢 **Measured: 6 platforms, 2.4 GB, 6 of 6 OK, under two minutes.** 🔵 `--depth 1` is enough
— the election is at `HEAD`, not in history.

### Step 2 — run both surfaces, because one of them is blind

    python3 compose/code/p152-vertical-election/election_verticals.py <dir>   # or-later + the notice denominator
    python3 compose/code/p152-vertical-election/omission.py          <dir>   # the -only-by-OMISSION form

🔴 **Run the second one.** The first reports `instructure/canvas-lms` as `SILENT`; the second
reports **16 896** files electing **AGPL-3.0-only**. 🟢 **`T85`.**

### Step 3 — read the answer off the table, and it is a real decision input

| platform | ★ | licence | election | what the client's fork may become |
|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | **7.5k** | GPL-3.0 | 🟢 **`-or-later`** | 🟢 **GPL-3.0 or any later GPL** — a future relicensing route exists |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | **6.9k** | AGPL-3.0 | 🔴 **`-only`** | 🔴 **AGPL-3.0 ONLY, plus §13 network-use at v3's wording. No route out.** |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | **8.2k** | AGPL-3.0 | 🟡 **unstated per-file** | 🟡 **ask upstream** — 🔵 though its README says *"version 3 … unless otherwise noted"* |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **1.1k** | 🟢 **MIT** | 🟢 **n/a** | 🟢 **anything** — 🔵 the only one of the four with no copyleft conversation |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | **9.2k** | LGPL-3.0 | 🟢 **`-or-later`** | 🟢 **link, do not absorb** — and the or-later route exists |

### Step 4 — check the hit is the SUBJECT's before you act on it

🔴 **`sakaiproject/sakai` reads `-or-later` and it is false.** The single hit is
`library/src/webapp/js/trimpath-template-latest.js` — *"Copyright (C) 2004, 2005 Metaha"*,
a bundled library. 🟢 **Sakai is ECL-2.0 and elects nothing.** 🔵 **So for any row with a
LOW notice count (`sakai` 12, `edx-platform` 1), open the hit and read its copyright
holder.** 🔴 **`SKIP_DIRS` will not do it for you** — neither bundled copy is under
`vendor/`. 🟢 **High counts are safe** (`moodle` 14 024, `canvas-lms` 16 905 — first-party).

### Step 5 — wire the AI layer on top, without inheriting the copyleft

🟢 **The pattern that keeps the client's model code out of the copyleft**: the LMS stays
unmodified behind its own licence, and the agent talks to it over MCP.

| piece | repo | licence | role |
|---|---|---|---|
| **Canvas connector** | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** | 🟢 **184 code files, head `2026-10-11`** — the largest, most active Canvas MCP this shelf has measured |
| **records layer with an authorisation boundary** | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | 🟢 **Apache-2.0** | 🟢 **23 approval-gated writes, FERPA-logged, 24 tests** — 🔴 **and 1 ★, so nobody will find it by searching** |
| **offline / low-connectivity front** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 🟢 the permissive escape hatch when the copyleft answer is unacceptable |

🔵 **Why this ordering matters commercially.** 🟢 **An MCP connector under MIT, talking to an
unmodified AGPL LMS over a network boundary, does not make the client's agent code AGPL.**
🔴 **Forking `canvas-lms` to add the same feature inside the tree does** — and on the
`-only` election, permanently at version 3. 🟢 **Step 3 is therefore a build-vs-connect
decision, not a legal footnote.**

### 🔴 What `P43` does NOT solve

- 🔴 **It is not legal advice and the election is not the whole licence.** AGPL §13's
  network-use trigger applies whether or not the election is or-later; 🟢 the election decides
  only what a derivative may MOVE to.
- 🔴 **`openedx/edx-platform` has no per-file answer**, so this pattern returns *"ask
  upstream"* for one of the four majors. 🟢 Named rather than guessed.
- 🔴 **No star count is exact.** `7.5k` carries the shelf's `K-3CIFRAS` band; only the
  agent-tier figures (`140`, `40`, `1`) are exact as rendered.
- 🔴 **The instrument cannot attribute a notice to a holder yet** (`ACTION GF`), which is why
  Step 4 is a human read and not a flag.

---

## 🆕 🟢 `P40` — ask a licence question ONCE: put it in `lib/`, not in the next instrument *(new, p151 — Global)*

🔵 **This is `P263`'s rule, paid.** The rule has been written on this shelf since pass 88:
*while the question does not live in `compose/code/lib/`, every new instrument reimplements
it and chooses the bug again.* 🔴 **`T77` is the invoice.** Three published modules carried
a copy of the same `identify()`; every copy carried the same body-substring rung for the
GNU family; **5 of 7 GNU rows were published wrong and the id `GPL` was published ZERO
times in 150 passes.**

### Step 1 — find out how many copies there really are

🔴 **Count delegations separately from copies.** p150 recorded *"three published copies"*.
🟢 **There were two copies and one delegation**: `p149-common-title-licence.identify_ext()`
calls `p147`'s `identify()`, so patching two files fixed all three. 🔵 **A census of copies
that counts delegations as copies overstates the work and understates the coupling.**

### Step 2 — move the question, do not re-type it

🟢 [`compose/code/lib/licence_identity.py`](code/lib/licence_identity.py) now owns it, and
`p145-licence-census` and `p147-licence-language` **import** it. The surface:

| question | function | reads |
|---|---|---|
| which licence is this file? | `title_spdx()` | the **TITLE LINE** only — the name must *be* the line |
| independently, which licence? | `clause_licence()` | AGPL-3.0 §13 *"Remote Network Interaction"* |
| do the two agree? | `agree()` | `AGREE` / `TITLE_ONLY` / `DISAGREE` / `UNDETERMINED` |
| what did the old matcher say? | `retired_identify()` | the published ladder, **in its published order** |

### Step 3 — keep the broken version, deliberately

🔴 **`retired_identify()` must stay wrong.** A reproduction that quietly fixes either
ordering defect — the Apache rung ahead of the GNU rungs, AGPL ahead of GPL — cannot measure
what was published. 🟢 **Both orderings are asserted as REQUIRED behaviour of the repro**, so
a later tidy-up breaks the suite instead of silently erasing the evidence.

### Step 4 — prove the replacement costs no coverage before you ship it

🔴 **A narrower surface that answers less often is a trade, not a fix.** 🟢 **Measured:
39 of 39** licence files across the 58-row census carry a readable title line, and
**4 of 52** published rows change id — **0 outside the GNU family**. 🔵 **Re-publish the
census in the same pass, and diff it against the published artefact row by row.**

### Step 5 — do not correct in the pass that measured

🟢 **`ACTION EU`'s rule.** p150 measured `T77` and deliberately left the three copies
unpatched; p151 patched them. 🔵 **The one pass of delay is what makes the diff a test
rather than a tautology.**

### 🔴 What `P40` does NOT solve

- 🔴 **The README-heading question is still copied.** p151's re-published census reads
  **10** strict-unlicensed where p147's multilingual matcher reads **8** — the two
  Portuguese rows `T63` named. 🔵 **`ACTION FW`** moves that question to `lib/` too.
- 🔴 **`lib/` has no import test.** Nothing fails if a fourth module re-types the ladder
  instead of importing it. 🔵 **`ACTION FX`.**

## 🆕 🟢 `P41` — declare the identifier SPACE and the SCOPE before claiming a citation dangles *(new, p151 — Global)*

🔵 **A "dangling reference" check is the cheapest audit a knowledge base can run and the
easiest one to run wrongly.** 🔴 **p150 reported `P240` as cited-and-never-allocated.** 🟢 **It
resolves** — `compose/code/p239-table-integrity/README.md:17`, the region-column
completeness axis, allocated at pass 78.

### Step 1 — enumerate the spaces. There are three here, sharing one `P` prefix

| space | allocated by | count |
|---|---|---|
| **patterns** | a `## `P35` — …` heading on `compose/patterns.md` | **41** after this pass, max `P41` |
| **module axes** | a table row in `compose/code/*/README.md` whose first cell is the bare id | **23** after this pass |
| **pass findings** | being reported in a pass; cited bare (`P138`) or qualified (`P150-A`) | **174** passes nameable |

### Step 2 — declare the scope, and expect the number to move by two orders of magnitude

| scope | cited | dangling |
|---|---|---|
| the **6 pages rewritten each pass** | 48 | 🟢 **0** |
| …plus `intel/open-gaps.md` | 354 | 🔴 **260** |
| …plus the two trending pages and the README | 745 | 🔴 **685** |

🔴 **Four of this shelf's ten content files are append-only pass history, not three.** 🔵
**Every one of the 260 is a previous-generation id** (the range P469 to P1047, written here
without backticks because it is a numeric range and not a citation) surviving in a verdict
row written before the **2026-10-06 reset restarted the pattern space at `P1`**. 🟢 **A
historical record is not a defect**, which is why `scope` and `spaces` are arguments of the
gate rather than constants inside it. 🆕 **`T82`.**

### Step 3 — the CI step

    python3 compose/code/p151-identifier-spaces/identifier_spaces.py .   # exit != 0 on a dangling id
    python3 compose/code/p151-identifier-spaces/test_identifier_spaces.py # 25 tests, offline

### 🔴 What `P41` does NOT solve

- 🔴 **The thesis register is not gated.** `ACTION FR` built it as a file
  (`evidence/thesis-register.2026-10-12-p151.tsv`) and found **17 of T1..T80 with no
  definition anywhere** — `T39` cited **24** times among them. 🔵 **`ACTION FY`.**
- 🔴 **A generation boundary is not expressible.** The gate can exclude a page; it cannot say
  *"ids below P469 on this page belong to generation 1"*. 🔵 **`ACTION FZ`.**

## 🆕 🟢 `P38` — the licence-IDENTITY gate: never quote a licence your matcher read from the body *(new, p150 — all regions)*

🔴 **Why this pattern exists: this KB got it wrong on five rows and published the wrong answer
for nine passes.** `T77`. A studio that repeats the mistake tells a client that a usable repo
is unusable, or — worse — that a GPL-2.0 repo is `LGPL`.

🔵 **Run this before any repository's licence reaches a slide, an SBOM or a procurement memo.**

### Step 1 — read the TITLE LINE, not the body

    python3 compose/code/p150-gpl-affero-discrimination/run_gpl_affero.py <clones-dir>

🔴 **Do not grep the licence text for a licence name.** Every GNU licence names its siblings:

| file | contains the phrase | a body matcher returns |
|---|---|---|
| **GPL-3.0** | *"Use with the GNU **Affero** General Public License"* (§13 title) | 🔴 **AGPL-3.0** |
| **GPL-2.0** | *"you may want to use the GNU **Lesser** General Public License instead"* | 🔴 **LGPL** |

🟢 **The licence name must BE the line.** First five non-blank lines, name occupying the whole
line, version read from the same line or the next.

### Step 2 — confirm on the operative clause, and require agreement

| licence | the clause that proves it |
|---|---|
| **AGPL-3.0** | §13 **"Remote Network Interaction"** — 🟢 **a plain GPL file cannot contain it** |
| **GPL-3.0** | §13 **"Use with the GNU Affero General Public License"** |
| **GPL-2.0** | 🔴 **no §13 at all** |

🟢 **Ship the verdict only when title and clause agree.** On `DISAGREE`, stop and read the file
by hand — it is hand-edited or genuinely dual-licensed, and both cases need a human.

### Step 3 — for a dual-licensed repo, measure FILE REACH, not badge order

🔴 **`T80`.** A split-licence file states which half governs which paths. **Count the files.**

    # ishands/upstack — the worked example
    find . -name '*.js' -not -path './.git/*' | wc -l    #  3  → MIT
    find . -name '*.md' -not -path './.git/*' | wc -l    # 64  → CC-BY-SA-4.0

🔴 **`ishands/upstack` badges MIT first and MIT reaches 3 of 82 files.** 🟢 **The 64 markdown
files that ARE the product are ShareAlike** — so its tutor prompts cannot go into a
proprietary client deliverable, whatever the first badge says.

### Step 4 — carry the version, because it changes the obligation

| id | distribution copyleft | network copyleft | patent grant |
|---|---|---|---|
| **GPL-2.0** | 🔴 yes | no | 🔴 **NONE** |
| **GPL-3.0** | 🔴 yes | no | 🟢 yes |
| **AGPL-3.0** | 🔴 yes | 🔴 **yes** | 🟢 yes |
| **LGPL-3.0** | 🟡 library-scoped | no | 🟢 yes |

🔵 **`GPL` with no version is not an answer.** `qxbao/qldt-hanu-mcp` was filed as bare `LGPL`
and is **GPL-2.0** — full copyleft with no patent grant, on a row a studio would have treated
as link-and-go.

#### 🔴 And the `-only` / `-or-later` election is UNSTATED on this shelf — do not imply it is readable

🔴 **`ACTION FO` (p151) measured it and the answer is zero.** Across the **7** GNU-family
rows, **1 513** source files scanned: **0** per-file `or (at your option) any later version`
notices, **0** `-only` statements, **0** `SPDX-License-Identifier` lines carrying an
election. 🟢 **The positive control — the same matcher over the licence BODIES — fires 7 of
7**, so the null is a property of the rows and not of the instrument.

🔴 **Never read the election from the licence file. 🆕 `T81`.** GPL-3.0's own appendix,
*"How to Apply These Terms to Your New Programs"*, contains *"either version 3 of the
License, or (at your option) any later version"* — so a body search returns `OR_LATER` for
**every** verbatim GNU file, including one whose author elected `-only`. 🔵 **That is `T77`'s
defect class one layer down**: a phrase correct as a phrase and wrong as a test.

🔵 **What to say in a room.** For all seven rows the election is unstated, so a derivative
cannot rely on *"or later"* and must be planned against the **stated version only**. Ask the
upstream author; do not infer it from the LICENSE file.

    python3 compose/code/p151-election-surface/test_election.py   # 24 tests, offline

### Step 5 — the CI step

    python3 compose/code/p150-gpl-affero-discrimination/test_gpl_affero.py   # 35 tests, offline

🟢 **Validated against six vertical platforms whose licences were known independently** —
`moodle/moodle` **GPL-3.0**, `openedx/edx-platform` **AGPL-3.0**,
`instructure/canvas-lms` **AGPL-3.0**, `sakaiproject/sakai` **ECL-2.0**,
`learningequality/kolibri` **MIT**, `bigbluebutton/bigbluebutton` **LGPL-3.0**. 🟢 **Six of
six, and all three GNU families distinguished.**

### 🔴 What `P38` does NOT solve

- 🔴 **It does not distinguish `GPL-3.0-only` from `GPL-3.0-or-later`.** That election lives in
  per-file headers and it decides what a derivative may relicense to. 🔵 **`ACTION FO`.**
- 🔴 **It reads the licence file at the repository root.** A monorepo with per-package licences
  needs `p441-tree-licence-enumeration` run alongside it.
- 🔴 **It is not legal advice and does not read a NOTICE file**, which is where an Apache-2.0
  row's attribution obligations actually live.


## 🆕 🟢 `P39` — adopting a PROMPT-LAYER education agent: audit what it withholds *(new, p150 — APAC first, portable)*

🔴 **A new artefact class this shelf had no category for.** Two of the five rows found in p150
ship **no server, no API and no code**: the whole product is instructions.

| row | licence | what it ships | region |
|---|---|---|---|
| [`flysheep-ai/education-skills`](https://github.com/flysheep-ai/education-skills) | **MIT** | **5** Agent Skills for the Chinese 高考 — science, liberal arts, Chinese, English, general-tech | 🟢 **APAC (China)** |
| [`ishands/upstack`](https://github.com/ishands/upstack) | 🔴 **MIT (3 files) / CC-BY-SA-4.0 (64)** | Socratic framework: productive struggle, calibrated hints, learning journal | unplaced |
| [`krishna16-origin/ai-tutor`](https://github.com/krishna16-origin/ai-tutor) | **MIT** | one 1 006-line Flask file whose substance is a quiz-generation prompt | unplaced |

🔴 **Every tool-surface probe on this shelf returns ZERO against these rows** —
`p148-rust-surface`, `p141-agent-surface-gate`, `p145-surface-payload-repair` all count
declared tools, and there are none. 🔴 **Zero is indistinguishable from "not measured", so a
prompt-layer row looks like an empty row.**

### Step 1 — invert the axis: measure the REFUSALS, not the tools

🔵 **A tutoring agent's safety property is what it declines to do.** Extract and review, by
hand, every instruction of these three kinds:

| axis | what to find | worked example |
|---|---|---|
| **hold-back** | does it withhold the answer until the learner attempts? | `upstack`: *"withholds the full answer until you've genuinely attempted the climb"* |
| **answer-key handling** | is the key hidden from the learner, and is its position randomised? | `krishna16-origin/ai-tutor`: *"Randomize the correct option position… never make every answer the same letter"* |
| **scope binding** | is it bound to a named curriculum or exam? | `education-skills`: bound to 高考 subject splits; `AI_Tutor_Release`: 人教版 grades 1–9 |

### Step 2 — diff against the upstream before adopting a fork

🔴 **`T79`, and this is the step that pays for the pattern.** A prompt-layer fork's README can
claim an extension while the diff is a deletion.

    git clone --depth 1 https://github.com/krishna16-origin/ai-tutor   trunk
    git clone --depth 1 https://github.com/maxew6/ai-tutor-project     fork
    diff trunk/app.py fork/app.py

🔴 **Six lines differ, and four of them are safeguards the fork REMOVED** — the
answer-position randomisation and the note that the key is hidden until reveal. 🟢 **Adopt the
trunk. Six lines of `diff` is the whole audit, and nothing else on the row would have told
you.**

### Step 3 — gate the licence by file reach, not by badge

🔵 **Run `P38` step 3.** 🔴 **`upstack`'s prompts are ShareAlike**: usable, improvable,
**not** carryable into a closed deliverable. 🟢 **`education-skills` is MIT across all 20
files** and is the one to fork for a China-facing engagement.

### Step 4 — wire it to a connector, because a prompt layer has no data

🟢 **The prompt layer carries pedagogy and no state.** Pair it with the tiers that have both:

    persona / hold-back rules   flysheep-ai/education-skills  (MIT)         ← what to teach
    learner state + mastery     ArnaudGuiovanna/tutor-mcp     (MIT, Go)     ← BKT, review scheduling
    auditable mastery estimates CAHLR/OATutor                 (MIT)         ← BKT, not an LLM's opinion
    LMS surface                 vishalsachdev/canvas-mcp      (MIT)         ← courses, assignments, grades
    governance gate             zavora-ai/mcp-student-records (Apache-2.0)  ← FERPA logging, approval gate

🟢 **`P35`'s data-layer caveat is RESOLVED as of p151** (`ACTION FF`): its approval gate is
real, fail-closed on four conditions, was bypassable in-process (`ACTION FD`), and 🟢 **two
lines of the subject's own code close the consumer-side bypass.** 🔴 **The residual is the
in-crate surface** (`T83`), held by a CI gate rather than by the type system.

### 🔴 What `P39` does NOT solve

- 🔴 **Step 1 is a HAND review.** No instrument on this shelf measures a refusal rule. 🔵
  **`ACTION FS`** registers the probe; until it lands this pattern is a checklist, not a gate.
- 🔴 **It does not test that the hold-back actually holds.** A prompt saying it withholds
  answers is a claim about behaviour, and behaviour needs a live session — the same gap
  `ACTION FD` hit on `P35`'s conditions 2–4.
- 🔴 **The two China-placed rows are placed by SUBJECT, not by author.** 人教版 and 高考 place
  the market; they do not establish where the authors are or who supports the code.

## 🆕 🟢 `P36` — place a vendor by region without trusting a suffix: exclude non-institutional hosts *(new, p149 — all regions, LATAM first)*

🔵 **Region placement is the column every Globant engagement is judged on and the one this
shelf is weakest at.** `P23` places a vendor from commit timezones; `P24` reads a tenancy
hostname. 🔴 **p149 measured what both lanes actually read, and a third of the placing hosts
are not institutions at all.**

### 🔴 The defect, measured

Over **50 clones**, the host channel placed rows on a nationally-bound ccTLD without ever
asking *whether the host is an institution*. 🔴 **Four non-institutional kinds, all measured:**

| kind | instance on this shelf | what it did |
|---|---|---|
| **platform / shortener** | `youtu.be` | 🔴 **placed an Egyptian-authored row in EMEA** — `.be` is Belgium |
| 🆕 **developer tooling** | `sh.rustup.rs` | 🔴 **placed an AUSTRALIAN row in EMEA** — `.rs` is Serbia, read out of a `curl … \| sh` install line |
| 🆕 **news media** | `feeds.bbci.co.uk`, `www.cbc.ca`, `www3.nhk.or.jp`, `news.ltn.com.tw`, `critica.com.pa` + 4 more | 🔴 **9 hosts across FOUR regions in one subject** — an RSS fixture list, which held the row in `CONFLICT` under every exclusion mode |
| 🆕 **government portal** | **17** hosts under `.gob.pe` | 🟡 **right answer, wrong reason** — the row is Peruvian, but it was placed by a stronger channel; on a row without one, 17 ministry hosts would have decided it |
| **bare `.edu`** | `bb.edu`, `phet.colorado.edu`, `professor-site.edu` | 🔴 **a registration date, not a country** — one row holds `dspace.mit.edu` **and** `cv.uoc.edu` (Barcelona) |

### The recipe

1. **Name the strongest channel and stop there.** A host assigned to a `BASE_URL`-shaped
   constant beats a URL in prose, which beats a publisher field, which beats an author
   email. 🟢 **`P144-V`'s rule — *"the institution is where it deploys; the author is wherever
   they were sitting"* — holds, and this pattern is how you apply it without a git history.**
2. **Exclude by ROLE, not by suffix.** 🔴 **Never drop a ccTLD** — `.be`, `.rs`, `.co`, `.ly`,
   `.io`, `.me` and `.to` are sold as vanity suffixes *because they read as words*, and a real
   `kuleuven.be` or `bg.ac.rs` must keep its placement. 🟢 **Name the hosts**: shorteners,
   video platforms, package and toolchain installers, news media, and government portals that
   are not the deploying institution.
3. **Refuse placeholders by token.** Split each label on `-` as well as `.` and refuse
   `example`, `myschool`, `your-university`, `demo`, `test`. 🔴 **This shelf produced three
   false placements on `*.example.edu`-shaped hosts before the rule existed**, all in the
   reassuring direction.
4. **Treat a bare `.edu` as a LEAD, never a placement.** Keep it in its own column so the
   evidence survives the demotion.
5. **Cross-check against a second, independent channel** and classify every row into six
   states, so *"both placed and they agree"* is never counted with *"only one could answer"*.
   🟢 **`INSTITUTION_ONLY` is the result worth having** — net new coverage at zero
   contradiction cost.
6. **Read the disagreements by name.** 🔵 **Do not average two channels.** On this shelf a
   single `DISAGREE` row named the whole defect twice: first `bb.edu`, then `sh.rustup.rs`.

### What it buys, per region

| region | why it matters here |
|---|---|
| **LATAM** | 🟢 **The biggest win.** Two-channel coverage **37 → 39 of 44**, almost all LATAM, because the timezone lane was declining `-0300` as ambiguous while the host lane could answer |
| **APAC** | 🔴 **The clearest error.** An Australian vendor was being placed in EMEA by a Rust installer URL |
| **EMEA** | 🟢 Protects real `.be`/`.rs`/`.no` institutions from a suffix-level fix that would have cost them their placement |
| **North America** | 🔵 **Removes a false positive**: `bb.edu` had placed a row here, and the offset channel disagreed |

### 🔴 What `P36` does NOT solve

🔴 **It cannot tell a deploying institution from one merely cited.** A university named in a
README because the author studied there looks exactly like one the server points at, unless
the host sits in an assignment. 🔴 **And the exclusion list is a list** — it holds the kinds
this shelf has met, and the next corpus will carry a kind it does not. 🟢 **Which is why step
5 is not optional**: a second channel is what turns an unknown kind into a visible
`DISAGREE` instead of a silent placement.

🔵 **Instruments**: [`p149-placement-exclusions`](code/p149-placement-exclusions/README.md)
(**26 tests**), [`p148-channel-agreement`](code/p148-channel-agreement/README.md) (**11**),
[`p147-npm-region`](code/p147-npm-region/README.md) (**15**).

## 🆕 🟢 `P35` — the manifest-contract CI gate: prove the governance claim instead of citing it *(p148, RENUMBERED by p149 — Global, deploys per-region)*

> 🔴 **`P35` was published by p148 as `P32`, and `P32` was already taken** — p147 had
> allocated it to the multilingual licence gate, which is still `P32` below. 🔵 **Two live
> patterns carried one identifier for a pass.** 🟢 **The first allocation keeps the number and
> this one moves**, which is why every p148 reference to "`P32`'s CI gate" means `P35`.
> 🔵 **`T75`**: this shelf allocates pattern numbers from a high-water mark it does not
> re-read, and the same habit produced the thesis-number collisions `P144-F` recorded.
> 🟢 **`ACTION FM` registers the one-line gate that would have caught it.**

### 🟢 `P35`'s data-layer gap is CLOSED by p151 — and the fix is two lines

> 🔵 **This heading read *"`P35` does NOT reach the data layer"* for three passes.**
> 🟢 **`ACTION FF` (p151) closed it.** The gap was real, the fix is two lines of the
> subject's own code, and both halves are now measured rather than argued.

🟢 **The change, in `zavora-ai/mcp-student-records`:**

```diff
-pub struct StudentServer { pub store: Arc<StudentStore> }
+pub struct StudentServer { store: Arc<StudentStore> }
+
+impl StudentServer {
+    pub fn new(store: Arc<StudentStore>) -> Self { Self { store } }
+}
```

plus the **one** call site (`src/main.rs`): `StudentServer { store }` →
`StudentServer::new(store)`.

🔵 **Why a privacy keyword is the whole consumer-side fix.** A Rust integration test is its
own crate, and p149 demonstrated its bypass from `tests/` — so the bypass it demonstrated
*is* the bypass a downstream consumer has, and that is exactly the boundary `pub`/private
closes. Measured:

| tree | the bypass | the repository's own suite |
|---|---|---|
| **HEAD** | 🔴 compiles and PASSES — `place_hold` returns `active == true` with no approval | 🟢 24 pass |
| **patched** | 🟢 **FAILS TO COMPILE** — `E0616` ×2 on the field reads, `E0451` on the struct literal | 🟢 24 pass + constructor control |

🔴 **What the two lines do NOT close, and say so in the room — 🆕 `T83`.** `pub`/private is a
*module* boundary, so a future module **inside** the crate can still reach `self.store` and
call a `pub fn` write. Closing that needs a sealed approval token threaded into all **23**
write signatures — a 23-site change to a repository this KB does not own. 🟢 **So the
recommendation splits: ship the two-line change, and hold the in-crate surface with the
gate in CI.**

    python3 compose/code/p151-approval-field-closure/field_gate.py <crate>   # exit 1 on HEAD, 0 patched
    python3 compose/code/p151-approval-field-closure/test_field_gate.py      # 19 tests, offline

### 🔵 The gap as p149 measured it, kept because the fix only means something against it

🔴 **`ACTION FD` (p149) proved the approval gate this pattern certifies is bypassable
in-process.** 🟢 **The gate itself is strong**: it runs first in the generated `call_tool` and
is fail-closed on four conditions (tool in `approval_tools`; protocol exactly `2026-07-28`;
sealed `request_state` bound to this caller and tool; `input_responses["approval"]["action"]
== "accept"`). 🔴 **But it lives at the protocol boundary only.** In `mcp-student-records`,
`StudentServer.store` is `pub` and every gated write is a `pub fn` on `StudentStore`, so
🔴 **six distinct approval-gated writes succeed with no approval, no protocol version and no
sealed state** when the crate is embedded as a library rather than run as a server.
🟢 **The bypassed write is still FERPA-logged**, so the audit trail survives; the approval
does not.

🟢 **So pitch `P35` as an MCP-surface control PLUS the two-line data-layer fix above**, and
🔴 **name the in-crate surface as the residual** (`T83`). 🔵 **p149's and p150's instruction to
scope the data layer out is SUPERSEDED, not deleted** — it was right while the fix did not
exist. 🟢 **And pin THREE surfaces, not two**:
the router's 46 names against the manifest's 46, **and** the manifest's 23
`requires_approval = true` names against the macro's 23 `approval_tools` — which p149 measured
**set-identical**, and which the repository's own suite checks for **11 of 23**, never as a set.
🟢 **`ACTION FF`** and 🟢 **`ACTION FH`** carry both halves.

🟢 **`P31` recommends `zavora-ai/mcp-student-records` as a records layer because its
`mcp-server.toml` declares a risk class and an approval requirement per tool.** 🔴 **p148
proved that contract holds today and that nothing keeps it holding.** `P35` is the four-file
gate that closes it, and it is the pattern to ship in week one of any engagement that quotes
the manifest to a procurement reviewer.

🔵 **Why this is a pattern and not a chore.** The sale in `P31` is *"23 of 46 writes are
approval-gated and the manifest says so."* 🔴 **If a later release adds `delete_student` to
the router and not to the manifest, every slide in that deck becomes false and no test
anywhere fails.** 🟢 **The gate costs one CI job.**

### The recipe — concrete repos, concrete wiring

| step | artefact | what it does |
|---|---|---|
| 1 | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) **v1.2.0**, Apache-2.0 | the records layer: **46** tools, Rust, `rmcp` 3.1.2, FERPA access log |
| 2 | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) **ECL-2.0** | the LMS. 🟢 **Permissive, so the stack carries no copyleft** |
| 3 | [`p148-rust-surface`](../compose/code/p148-rust-surface/README.md) | 🟢 **the gate.** Reads the router's `#[tool(` sites inside `#[tool_router]` and the manifest's `[[tools]]`, and fails on set inequality |
| 4 | [`p146-empty-walk-guard`](../compose/code/p146-empty-walk-guard/README.md) | 🟢 **the refusal.** A gate that reads zero files must fail the build, not pass it |
| 5 | [`p147-scope-parity`](../compose/code/p147-scope-parity/README.md) | the same idea on the auth axis, if the deployment fronts the server with `ahmedEid1/lumen`-style scopes |

### The gate, as a CI step

    # fails the build if the manifest and the router have drifted
    python3 compose/code/p148-rust-surface/rust_surface.py ./mcp-student-records \
      | tee surface.txt
    grep -q 'ACTION EP       SET_IDENTICAL' surface.txt || exit 1
    grep -q 'ACTION EO       counts AGREE'  surface.txt || exit 1

🟢 **Measured output on v1.2.0, this pass:** `router tools 46`, `manifest tools 46`,
`counts AGREE`, `SET_IDENTICAL`, `router_only -`, `manifest_only -`, `order identical True`.

🔴 **Three failure modes the gate catches that a count check does not**, each pinned by a
test in the instrument's **14**:

| drift | what `len() == 46` does | what `P35` does |
|---|---|---|
| a tool renamed on one side only | 🔴 **passes** — still 46 and 46 | 🟢 **fails**, naming `router_only` and `manifest_only` |
| a tool added to the router, another dropped from it | 🔴 **passes** | 🟢 **fails** |
| the gate run against a tree it cannot read | 🔴 **passes with `0 == 0`** | 🟢 **refuses** — `NO_RUST_SURFACE_READ` |

🔵 **The third is the one that matters most and is the least obvious.** 🔴 **The repository's
own `tests/manifest_test.rs` asserts `m.tools.len() == 46` and checks that eleven named
writes require approval — all read from the manifest, none compared against the code.** 🟢 **A
manifest that agrees with itself is not a contract.**

### 🔵 Per-region framing — the same gate, four different sales

| region | the clock | how `P35` is sold |
|---|---|---|
| **APAC** | 🔴 **nearest in the world** — Vietnam **2027-03-01** / **2027-09-01**; Korea ~**2027-01** | 🟢 **Conformity evidence.** Vietnam designates third-party certification for some listed systems; a machine-checked tool-and-risk-class inventory is the artefact that assessment wants |
| **EMEA** | Annex III **2027-12-02**; Art. 4 literacy duty **live since 2025-02-02** | 🟢 **Annex III record-keeping.** The manifest is the system description; `P35` is the evidence it is current |
| **North America** | no federal statute; **MD/OK** require human oversight and bar AI from high-stakes student decisions | 🟢 **`requires_approval` as the oversight control**, named per tool. 🔵 **Maps onto the AASA student framework's "no AI determining grades or discipline"** |
| **LATAM** | 🔴 **no education-specific statute**; **87% adoption / 26% strategy** | 🟢 **The governance layer itself is the product** — there is no compliance deadline to sell against, and a verifiable control inventory is what an institution with no framework can adopt whole |

🔴 **One honest limit, the same one `P31` carries.** This is a **tool surface over a records
store**, not a registrar. A client needing enrolment workflows, fees, timetabling and report
cards out of the box is choosing between **LGPL-3.0 (OpenEduCat)**, **GPL-2.0 (RosarioSIS)**
and a build — 🔴 **and `Fedena`, which 2026 comparison tables call the permissive option,
ships no licence body and was last committed in 2012** (`verticals/solutions.md`, p148).
🟢 **Have that conversation in week one.**

### 🔴 What `P35` does NOT solve

- 🔴 **It proves names match, not that behaviour matches.** `record_grade` carrying
  `requires_approval = true` is a declaration; that the server *enforces* it is a separate
  test this KB has not written.
- 🔴 **It is Rust-only as built.** The same gate for the shelf's Python and TypeScript rows
  needs the equivalent reader; `p143-surface-gate-repair` is the nearest existing one, and
  🔴 **no row on this shelf outside `mcp-student-records` ships a declared manifest to compare
  against** — three carry bidirectional pins, in three incompatible formats (`P144-F`).
- 🔴 **`"*"` wildcard scopes defeat the auth half.** If step 5 is used, mint clients with an
  explicit scope list: `"*"` is the shipped default on **2 of 3** `lumen` client-minting
  paths and `has_scope()` short-circuits on it (`P147-H`).
## 🆕 🟢 `P31` — the permissive system-of-record stack, with governance that passes a procurement review *(new, p147 — North America first, portable)*

🟢 **This is `P30` extended down into the records layer, which `P30` could not reach**
because every SIS-shaped row on this shelf was copyleft or unlicensed. 🆕 **One
Apache-2.0 row changes that.**

| layer | component | licence | why this one |
|---|---|---|---|
| records + agent surface | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) **v1.2.0** | 🟢 **Apache-2.0** | 🟢 **46 tools**, `mcp-server.toml` manifest, **23 of 46 approval-gated**, **FERPA access log** |
| learning platform | **Sakai** | 🟢 **ECL-2.0** | 🟢 **the only permissive major LMS** (p146) |
| agent runtime | **`rmcp` 3.1.2** (in-tree) or any MCP client | 🟢 Apache-2.0 / MIT | 🟢 the server speaks MCP over stdio — no bespoke protocol |
| identity | OAuth client-credentials with an **explicit scope list** | — | 🔴 **never the wildcard default** — see `P147-H` |
| audit | the server's own FERPA access log + `requires_approval` flags | 🟢 in-tree | 🟢 **evidence, not a policy document** |

### 🟢 How to wire it

1. 🟢 **Stand up `mcp-student-records` against the institution's SIS.** `cargo build`;
   `mcp-server.toml` is the tool manifest and the governance contract in one file.
2. 🟢 **Read `mcp-server.toml` BEFORE writing any agent logic.** Every tool carries a
   `risk_class` and a `requires_approval` flag. 🔵 **Build the approval UI off that file,
   not off a list you maintain by hand** — `tests/manifest_test.rs` keeps it honest in CI.
3. 🔴 **Gate the 11 named FERPA-sensitive writes through human approval**, because the
   manifest already says they require it: `record_grade`, `record_attendance`,
   `send_communication`, `set_student_status`, `add_accommodation`, `enroll`,
   `add_guardian`, `record_mastery_evidence`, `place_hold`, `release_hold`,
   `assign_intervention`. 🟢 **`send_communication` is typed `ExternalWrite`** — treat it
   as leaving the institution, because it does.
4. 🟢 **Put Sakai beside it, not under it.** The two share no code, so ECL-2.0 and
   Apache-2.0 compose with no copyleft anywhere in the stack.
5. 🔴 **Add the parity test the repository does not have.** Nothing compares the manifest's
   46 names against the router's 46 `#[tool]` names; the counts meet at the literal `46`.
   🟢 **A ten-line test asserting set identity closes the one real gap in this row**, and
   [`p147-scope-parity`](code/p147-scope-parity/README.md) is the shape to copy.

🔵 **Why this clears procurement.** A school asks three questions: *can we use it* (🟢
Apache-2.0), *which tools can change a student's record* (🟢 23 of 46, named in a committed
file), *can you prove a human approved each one* (🟢 the approval flag plus the FERPA access
log). 🔴 **No other row on this shelf answers all three from the repository.**

🔴 **Two honest limits.** It is **Rust**, which is not most studios' default for this layer.
And 🔴 **this shelf's own surface instruments cannot measure it** — `lang_of` has no `.rs`
(`T64`) — so the 46 figure here comes from reading `#[tool(` attributes and the manifest,
not from the gate that measured every other row.

**Effort: 6–8 weeks** for a single-institution deployment with the approval UI and the
parity test, excluding SIS data mapping.

---

## 🆕 🟢 `P32` — the multilingual licence gate, before any LATAM connector is adopted *(new, p147 — LATAM, portable)*

🔴 **`T63` is not a curiosity; it is a procurement hazard.** This KB scored 9 connector rows
as having **no grant at all**, and **2 of them declare one** — in Portuguese and Spanish, on
the region whose system-of-record rows this KB recommends most often as entry points.

### 🟢 The gate, as four checks run in order

1. 🟢 **Licence FILE first**, by name: `LICEN[CS]E`, `COPYING`, `UNLICEN[CS]E`,
   `LICENSE-MIT`, `LICENSE-APACHE`, with or without `.md`/`.txt`/`.rst`.
2. 🟢 **Identify by BODY, not by identifier.** `Permission is hereby granted, free of
   charge` is MIT whatever the README calls it; `GNU AFFERO GENERAL PUBLIC LICENSE` is
   AGPL-3.0 even when an `MIT` token appears lower in the same file.
3. 🆕 🟢 **README headings in the languages the rows are WRITTEN in**, not just English:
   `licen[cs]e | licen[cçs]a | licencia | lizenz | licenza`, plus the inline forms
   `licenciado sob`, `licenciado bajo`, `bajo la licencia`, `sob a licença`,
   `unter der Lizenz`.
4. 🆕 🟡 **Informal grants, flagged and never promoted.** *"Usted es libre de copiar y
   modificar"* is a permission, not a licence: it says nothing about warranty, patents,
   attribution or redistribution. 🟢 **Score it `UNIDENTIFIED` and escalate to legal** —
   it is materially different from silence and materially different from a licence.

🟢 **Run the baseline alongside the extension and diff them.** That is how this pass could
say *"the baseline reproduces p145's value for all 44 rows, so the pattern is the only
variable"* — and how it could show **2 rows changing with zero false positives among the 34
`FILE` rows**. 🔵 **Without the control, a new pattern's wins are indistinguishable from its
mistakes.** [`p147-licence-language`](code/p147-licence-language/README.md), **13 tests**.

### 🔴 Two traps this gate is built around

🔴 **A README that cites a `LICENSE` file which was never committed.**
`frjunioalves/suap-mcp` says *"Veja o arquivo `LICENSE` para detalhes"* and `git ls-files`
matches nothing. 🟢 **Score `README_ONLY`, never `FILE`** — the declaration is real and the
file a compliance review wants does not exist.

🔴 **A monorepo whose licence does not ship.** `moodle-mcp-server-aql` declares AGPL-3.0,
the repository carries the full **661-line** body at its root, and the tarball carries
nothing — because `packages/server/package.json` has a **16-glob `files` allowlist** with no
`LICENSE` and no `LICENSE` inside the package directory. 🔵 **npm's automatic inclusion
looks in the package directory and does not reach up.** 🟢 **Check the repository before
concluding a published package is unlicensed**, and 🔴 **check the package before
concluding a licensed repository ships its grant.**

**Effort: 1 week** to build and run across a candidate set, including the baseline control.

---

## 🆕 🔴 `P33` — the refusal harness: never let an instrument answer a question it had no input for *(new, p147 — all regions)*

🔵 **Three of this pass's six theses are one shape**: a measurement that was never taken,
published in the shape of one, always at the reassuring value.

| cause | how it presents | real example |
|---|---|---|
| 🔴 exclusion drops the payload | `0 files` → "not a server" | npm `dist/` tier, **7 rows**, 2 passes |
| 🔴 artefact is not the kind read | `git ls-tree` on a tarball | **8** npm rows (`T59`) |
| 🆕 🔴 language outside the map | `.rs` unmapped → `0 files` | 🔴 **a 46-tool Apache-2.0 SIS** |
| 🆕 🔴 pattern cannot express the target | `licen[cs]e` vs `Licença` | **2** LATAM rows (`T63`) |

### 🟢 The recipe

1. 🟢 **At every point a verdict is formed, assert that input was seen.**
   `walked_or_refuse(files, root, excluded)` from
   [`p146-empty-walk-guard`](code/p146-empty-walk-guard/README.md) — four lines, and it
   preserves the distinction that matters: **zero files walked withholds a verdict; files
   walked with no match keeps one.**
2. 🟢 **Wrap, do not rewrite.** [`p147-guard-harness`](code/p147-guard-harness/README.md)
   calls each instrument's **own** enumeration function and refuses at zero, so the bytes
   that produced published figures stay reproducible. 🔴 **Editing them in place would
   destroy every future pass's ability to say "the baseline reproduces."**
3. 🔴 **Never let the harness carry a copy of what it inspects.** `P146-D`'s census read
   itself as compliant because it held the guard tokens as regexes, inflating the exact
   number it existed to report. 🟢 **A test asserts the harness holds no exclusion set.**
4. 🟢 **Run the negative control and read it.** This pass's control over 220
   (clone, instrument) pairs returned **2 refusals** — and those two were the Rust row that
   nobody had noticed. 🔵 **The control found the finding.**
5. 🆕 🟢 **Extend the idea past the walk to the pattern.** A matcher that cannot express its
   target must not return "absent." 🔵 **`licen[cs]e` returning `NONE` on a `## Licença`
   heading is the same bug as a gate returning `NOT_AN_MCP_SERVER` over zero files.**

🔵 **The one line worth carrying out of this pattern:** 🟢 **an instrument must distinguish
"I looked and it is not there" from "I could not look."** 🔴 **Every figure this KB has
withdrawn in five passes failed that test, and not one failed on the measurement itself.**

**Effort: 2–3 days** to add the guard and a harness to an existing instrument set; the
negative control is the expensive part and the part that pays.

---

## 🔴 `P34` — mint MCP clients with explicit scopes, because the shipped default is `"*"` *(new, p147 — all regions)*

🔴 **`ahmedEid1/lumen` publishes an RFC 8414 metadata document with a per-tool scope
vocabulary, and then defaults to a wildcard that collapses it.**

| path | default |
|---|---|
| `app/api/v1/admin_mcp_clients.py:66` | 🔴 `Field(default_factory=lambda: [WILDCARD_SCOPE])` |
| `app/cli.py:478` | 🔴 `scope_list = [WILDCARD_SCOPE]` |
| `issue_token` with an explicit list | 🟢 intersected against the grant (`auth.py:102`) |

🔴 **`has_scope()` short-circuits on `"*"`** (`principal.py:87`), so **8 of 9 tools are
reachable by any authenticated principal** — including **`grade_review_card`**, which
changes a student's record, and `create_course_draft`. 🟢 **`ingest_url_to_draft` is not:
its `admin` posture gate is independent of scope and still fires** (`server.py:123`).

🔵 **So the recipe is one line long and it is the third path in the table.** 🟢 **Always
pass an explicit scope list when minting a client**, and 🟢 **scope it to the read tools
unless a write is genuinely required.**

🟢 **And add the assertion the repository is missing**, which is not the obvious one:

    set(scopes_supported) - {WILDCARD_SCOPE} == set(all_tool_names())

🔴 **A plain bidirectional equality would FAIL on this correct repository**, because the
wildcard is a designed member of the scope set and not of the tool set. 🔵 **Name the
wildcard; do not count past it.** [`p147-scope-parity`](code/p147-scope-parity/README.md),
**9 tests**.

**Effort: 1 day**, and it is the highest ratio of risk removed to work done on this page.

---

## 🆕 🟢 `P30` — the all-permissive education stack, end to end *(new, p146 — all regions)*

🟢 **This KB can now name a complete education stack with no copyleft anywhere in it.** It
could not before p146, because the licence of the platform layer had never been read
(`P146-V`) and 🔴 **the platform everyone reaches for first is the wrong one for this**:
Open edX and Canvas are both **AGPL-3.0**, whose network clause triggers on exactly the
hosted multi-tenant shape they are deployed in.

| layer | repo | licence | why this row |
|---|---|---|---|
| **LMS core** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | 🟢 **Apache-2.0 with a narrowed §3 patent grant. OSI-approved, copyleft: no.** The only major LMS you may fork and modify without reciprocal obligation |
| **tool launch** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** | LTI 1.3 Advantage tool provider — OIDC launch, Deep Linking, AGS grade passback, NRPS. **373★**, pushed **2026-10-06** |
| **launch (Python)** | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** | Where the agent framework is Python. 🔴 **Dormant since 2024-08-18 — pin it and expect to maintain it** |
| **rostering** | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** | OneRoster 1.2 API over an Ed-Fi ODS, **from the standards body's own org** |
| **rostering SDK** | [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 🟢 **0BSD** | 🟢 **Drops even the attribution requirement.** 🟡 Single-individual holder on an org-named repo |
| **conformance proof** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 **Apache-2.0** | 🟢 **How you prove the rostering connector is correct, maintained by Google's own org** |
| **statistics / benchmarks** | [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 **MIT** | UNESCO UIS + OECD EAG over SDMX, no API key. **10 tools, all `readOnlyHint: true`**, `tools.lock.json` SHA-256 pin |
| **instrument hygiene** | `compose/code/p146-empty-walk-guard` | — | 🟢 **In CI, so no verdict is ever formed over an empty file set** (`T42`) |

### How to wire it

1. **Sakai is the system of record.** Deploy it as-is first; do not fork on day one. 🟢 **The
   ECL-2.0 escape hatch is worth having and not worth using early.**
2. **The agent is a separate service, launched over LTI 1.3** via `ltijs`. The institution
   issues a client ID and can revoke it. 🔴 **No stored student password, no scraping** —
   this is the answer to the credential blocker this KB has carried since p135.
3. **Rostering comes from `edfi-oneroster`, not from the agent.** The agent asks
   OneRoster who is in the class; it never reads the SIS directly.
4. **Grades go back over AGS**, which `ltijs` implements — so the write surface is the
   standard's, not yours. 🔵 **Pair this with `P24`'s draft-first gate: write a draft, never
   a final grade** (and see `P29`, because in two jurisdictions this is now the regulated
   act).
5. **Prove it with the Google conformance suite** before the client's security review asks.
6. **`global-education-mcp` supplies benchmark context** — read-only, annotation-complete.
   🔴 **Its upstream hosts (`api.uis.unesco.org`, `sdmx.oecd.org`) are blocked in this
   environment**, so it is unexercised here; the licence and annotations are read, the
   runtime is not.

🔴 **What this pattern does NOT claim.** No row above was re-measured this pass — the clone
channel is refused (`P146-A`) — so licences are **page and payload readings carried from
p134–p145**, not fresh `LICENSE`-file reads. 🔴 **`T21`/`P145-I` is this KB's own evidence
that a declaration and a shipped grant diverge**, and the Sakai row in particular is a
badge reading only. 🔵 **Verify the three load-bearing rows (`sakai`, `ltijs`,
`edfi-oneroster`) against their payloads before a contract depends on them.**

---

## 🆕 🔴 `P29` — the jurisdiction gate: build against the clock that bites FIRST *(new, p146 — all regions)*

🔴 **This KB had the regulatory sequence backwards for two passes.** `T40` said APAC's
compliance surface was horizontal and not about education. 🔴 **Korea's AI Basic Act names
student evaluation in Article 2(4)(j)**, it has been in force since **2026-01-22**, and
with MSIT's grace period its penalties bite around **2027-01** — 🔴 **roughly eleven months
BEFORE the EU's Annex III date of 2027-12-02.**

### Step 1 — place the engagement, then read the clock, in this order

🔵 **The region is the field; the jurisdiction is its own column** — a cell reading
`APAC — Korea` is not a region cell, and this KB's own `P240` gate enforces that.

| region | jurisdiction | instrument | education in scope? | bites |
|---|---|---|---|---|
| **APAC** | Korea, K-12 | AI Basic Act, Art. 2(4)(j) | 🔴 **YES — student evaluation** (early childhood, elementary, secondary) | **2026-01-22**, penalties ≈ 🔴 **2027-01** |
| **APAC** | Korea, higher ed | same | 🟢 **NO — outside item (j)** | — |
| **APAC** | Japan | innovation-first, no categorical prohibitions | 🟢 no vertical item | — |
| **APAC** | India | 🔴 no binding cross-sector AI law | via data protection | 🔵 **a privacy engagement** |
| **EMEA** | EU | AI Act Annex III, as amended by **Reg. (EU) 2026/1744** | 🔴 **YES — 4 use cases, EVERY level** | 🔴 **2027-12-02** |
| **EMEA** | EU | 🔴 **emotion recognition in education** | 🔴 **PROHIBITED OUTRIGHT** | 🔴 **in force since 2025-02** |
| **EMEA** | EU | Article 4 AI-literacy duty | applies to deployers | 🟢 **in force since 2025-02-02** |
| **EMEA** | EU, public institutions | Article 27 FRIA | impact assessment | with Annex III |
| **North America** | US states | state law, **no federal instrument** | varies by state | 🔴 **read the bill's LAST ACTION, not a tracker's label** (`T57`) |
| **LATAM** | region-wide | 🔴 **no national AI-in-education regulation found** | — | 🔵 **the absence of a deadline is the sales trigger** (`T1`) |

### Step 2 — check the build against the four regulated use cases, by name

🔵 **The EU's Annex III education entries are not abstract — they are the four things an
education agent is usually built to do:**

| use case | regulated in EU | regulated in Korea |
|---|---|---|
| **admission / access to a programme** | 🔴 **yes** | 🟢 no |
| **assessment of learning outcomes** | 🔴 **yes** | 🔴 **yes (K-12)** |
| **assignment of education level** | 🔴 **yes** | 🟢 no |
| **monitoring/proctoring during tests** | 🔴 **yes** | 🟢 no |
| tutoring, practice, content generation, lesson prep | 🟢 **none of the above** | 🟢 none |

🟢 **The gate's output is a scope decision, and it is usually cheap.** A tutoring, practice
or lesson-preparation agent touches none of the four. 🔴 **A grading agent touches one in
both jurisdictions, and a proctoring agent touches a prohibited class in the EU if it
infers affect at all** — and this KB holds two shelf rows in the affect-detection class.

### Step 3 — make the deadline the proposal, not the risk section

🔵 **`T1` says the market is the adoption-governance gap, and the gap has a different shape
in each region** — so the same stack is sold three ways:

- **North America** — 🟢 **the deadline is the trigger.** 24 of 35 states that introduced
  AI-education legislation have enacted something; a district with a compliance date needs
  an audit trail. 🔴 **Verify the instrument's last action before you quote it.**
- **EMEA** — 🟢 **two duties are already live.** Article 4 AI-literacy and the emotion-
  recognition ban are in force today; Annex III is 14 months out. 🔵 **Sell readiness for
  the live ones, preparation for the deferred one.**
- **APAC** — 🔴 **the K-12 layer is regulated NOW in Korea and the university layer is
  not.** 🔵 **The inverse of the EU, and the one place this KB's prior framing would have
  mispriced the work.**
- **LATAM** — 🔴 **no deadline exists.** Brazil: **53% of administrators using AI, 22% of
  schools with guidelines.** 🟢 **The governance artefact IS the deliverable** — the policy,
  the audit trail and the staff training, not only the agent.

### 🔴 What this gate cannot do

- 🔴 **It is built on secondary sources.** `eur-lex.europa.eu` and `capitol.texas.gov` are
  unreachable from this environment, and no primary Korean text was read. 🔵 **`Reg. (EU)
  2026/1744` and the scope of Korea's item (j) are both carried on secondary authority.**
  `ACTION EL`.
- 🔴 **It is not legal advice and the significance test is not mechanical.** Korea's listed
  domain is necessary, not sufficient: a system qualifies only if it may significantly
  affect life, safety or fundamental rights, 🟢 **and a formal MSIT determination can be
  requested.** The EU's Annex III has its own carve-outs.
- 🔴 **`T56` is a risk this gate does not price.** Korea both regulates education and
  withdrew its flagship classroom programme — statutory status removed **2025-08-04**,
  adoption **37% → 19%** within 2025. 🔵 **A pipeline resting on a national mandate can
  lose the mandate**, and nothing in a compliance gate detects that.

---

# Education — compose patterns

**Pass 145, 2026-10-12.** 🆕 **`P27` is added: the measurement-population gate — prove your
instrument read the files before you believe its verdict.** 🆕 **`P28` is added: the
connector grant gate, which stops a build on the 18 of 52 rows that ship no grant and names
the three LATAM system-of-record rows it catches.** 🔁 **`P18` is amended at step 1** — the
tree to measure is decided by the package's declared entry point, not by a name list. 🔁
**`P21` is recaveated**: two of the three "pins" found since are one-directional.

## 🆕 🔴 `P27` — the measurement-population gate: prove the instrument read something *(new, p145 — Global)*

🔴 **This pattern exists because this KB published a tier share computed over zero files for
two passes.** `surface_gate2.py` excluded `dist` and `build` by name; 7 of 8 npm packages
ship their whole payload under those names; the instrument walked **0 files**, found **0
`mcp` tokens**, and emitted `NOT_AN_MCP_SERVER` — which reads exactly like a measurement.

🔵 **Any instrument with a skip list can do this to you, and on a client engagement it will
do it on the vendor's package rather than on a KB row.**

### Step 1 — make an empty population an ERROR, never a value

```python
files = list(walk(root))
if not files:
    raise EmptyPopulation(root)      # 🔴 NOT "no registrations found"
```

🔴 **The single highest-value line in this pattern.** A verdict and a vacuum must not share
a representation. Every scanner you write or adopt gets this guard before it gets features.

### Step 2 — print the population, not just the verdict

```
subject                              artefact  admitted  files  verdict
mcp-canvas-lms-1.0.5                 PAYLOAD   dist      16     BOUNDED_STATIC
_n35da_brightspace-mcp-0.4.0         SOURCE    -         17     DYNAMIC_UNBOUNDED
```

🟢 **`artefact` and `admitted` as columns are what makes the npm correction auditable.** A
reviewer can see *which tree* produced each number without rerunning anything. 🔵 **If your
output cannot answer "what did you read?", it cannot be reviewed.**

### Step 3 — decide exclusions by the property, not by the name

For a published package, the shipped tree is whatever its own metadata points at:

```bash
jq -r '.main, .module, (.bin|if type=="object" then .[] else . end), .exports' package.json
```

Admit a `dist`/`build` tree **only** when every declared entry resolves inside it and no
source exists beside it. 🟢 **That admits the seven npm payloads and still excludes a
committed `dist/` in a git checkout** — which is `T37`'s double count, foreclosed by rule
rather than by vigilance.

### Step 4 — reproduce the old numbers before you publish new ones

🟢 **Run the unmodified instrument first and check it still returns the published table.**
This probe's baseline reproduced p143 row for row (agent 50%, foundations 0%, github-only
33%, npm 100% n=1), 🔵 **so every difference afterwards was attributable to one of two
deliberate changes** rather than to drift, environment or a different clone.

### Step 5 — cross-check against a second instrument and keep both numbers

🔴 **Do not reconcile a disagreement by preferring your own instrument.**
`@imazhar101/mcp-canvas-server` reads **227 `BOUNDED_STATIC`** under descriptor counting and
**18 dynamic sites** under site counting. 🟢 **Both are published.** The first answers "how
many tool definitions exist?", the second "where are they attached?", 🔵 **and a client
asking "how many tools does this connector have?" needs to be told which question they are
asking.**

### 🔴 What this gate cannot do

🔴 **It does not prove reachability.** A tree that was read, and registrations that were
found, still do not establish that the server runs them — `p140`'s limit, unchanged.

## 🆕 🔴 `P28` — the connector grant gate: run it before the first sprint, not before go-live *(new, p145 — all regions)*

🔴 **18 of 52 connector rows on these shelves ship no grant a client can rely on; 9 carry no
licence of any kind.** 🔵 **That is a third of the shelf, and the rows it catches are not the
marginal ones** — they include the largest tool surface on the github-only tier and three
LATAM system-of-record connectors this KB recommends as entry points.

### Step 1 — classify the grant into four states, never two

```bash
# FILE | PKG_ONLY | README_ONLY | NONE  —  see compose/code/p145-licence-census
python3 licence_census.py "vendor-connector=$CLONE=candidate"
```

🔴 **`ls LICENSE` is the wrong test.** 🔵 **A licence identifier is not a licence** (`P138`):
`PKG_ONLY` means `package.json` says `"license": "MIT"` and no text ships. 🔴 **7 of 8 npm
connectors on these shelves are `PKG_ONLY` or `README_ONLY`** — an identifier naming terms
nobody shipped.

### Step 2 — identify the licence from the BODY, before trusting any string in it

```python
for rx, name in BODY_HINTS:      # Apache preamble, AGPL header, MIT grant sentence…
    if rx.search(text):
        return name
return SPDX.search(text)         # only as a fallback
```

🔴 **A file saying "MIT" in a comment above the Apache text is Apache.** Body first,
identifier second — not the other way round.

### Step 3 — stop the build on copyleft, and stop it harder on copyleft + extensibility

🔴 **`moodle-mcp-server-aql` is the worked example to show a client.** It declares
**AGPL-3.0**, ships no licence text, and **`.push()`es a tool descriptor per discovered
plugin** at `dist/server/factory.js:131`. 🔵 **Copyleft obligations attach to modification,
and a plugin architecture is an invitation to modify** — so the two properties compound
rather than add.

🟢 **The Moodle rows to use instead**: `eth-moodle-mcp` (18 tools) and
`@ink-waffle/moodle-mcp` (16), both MIT-declared. 🔴 **Both still `PKG_ONLY`** — carry the
caveat, do not pretend it away.

### Step 4 — check the fork parent before you abandon an unlicensed row

```bash
git log --reverse --format='%H %ae %s' | head -3    # does history start at a fork?
```

🔵 **An unlicensed fork of a licensed parent is a different problem from an original work
with no grant**: the parent's terms may already cover the code. 🟢 **`p136-lineage-verdict`
is the instrument**; `ACTION EE` runs it over the eight.

### Step 5 — escalate a consortium-published row differently from a hobby row

🔴 **`SIU-Toba/docker-guarani` is unlicensed and published under the SIU-Guaraní
consortium's own organisation.** 🔵 **You cannot route around that by emailing one author** —
it needs the consortium, and that is a procurement conversation with a lead time, not a
licence question. 🟢 **Raise it in week one or it lands in week twelve.**

### 🔴 The row where this gate and the compliance gate meet

`eugeborzone/Auto_Grade_Guarani` — 🔴 **auto-grading, no licence at all, LATAM.**
🔵 **Auto-grading is the named EU high-risk use case (`T3`) and LATAM is the region with the
highest teacher-adoption base (`T41`).** 🔴 **The row sitting on the most demand and the most
regulation is the row with no grant.** 🟢 **Name it in the engagement's first risk register,
not its last.**

## 🔁 `P18` AMENDED at step 1 — the tree to measure is declared, not named *(p145 — Global)*

🔴 **Previous step 1 said "measure the shipped tree" and left "shipped" to a name list.**
That name list excluded `dist` and `build`, and on 7 of 8 npm connectors the excluded tree
was the only tree there was.

### The amended step 1

1. Read `package.json`'s `main`, `module`, `bin`, `exports`.
2. If **every** declared entry resolves inside a `dist`/`build` tree **and no source file
   exists outside it** → that tree is the shipped source. Measure it. Record `PAYLOAD`.
3. Otherwise → the built tree is an artefact beside its own source. Exclude it, measure the
   source. Record `SOURCE`.
4. 🔴 **If the resulting population is empty, raise — do not report a verdict** (`P27`
   step 1).

🟢 **`@n35da/brightspace-mcp` is the regression test**: it ships `lib/` + `server.mjs`, reads
`SOURCE`, and its 17 sites are unchanged from p143. 🔵 **The one row the old rule got right
must keep reading the same, or the new rule is not a repair.**

## 🔁 `P21` RECAVEATED — most "pins" are one-directional, and a one-directional pin is a floor *(p145 — Global method)*

🔵 **`P21` asks for a committed bidirectional pin: a golden list checked for `missing` AND
`extra`.** Since it was written, four candidate pins have turned up and 🔴 **only one is
bidirectional.**

| row | what it pins | direction |
|---|---|---|
| 🟢 `divyarthjain/vtop-bhopal-mcp` | `EXPECTED_TOOLS`, 17 names, checks `missing` **and** `extra` | 🟢 **bidirectional** |
| 🟡 `malkreide/global-education-mcp` | SHA-256 lockfile over 10 tools | 🟢 content-exact |
| 🔴 `oliverhruby/edupage-mcp` | classification manifest, 31 tools | 🔴 **manifest, not assertion** |
| 🔴 **`ahmedEid1/lumen`** 🆕 | `TOOL_SPECS` (9) → OAuth `scopes_supported` | 🔴 **tools ⊆ scopes only** |
| 🔴 **`nitsuah/bb-mcp`** 🆕 | `src/manifest.ts`, 17 named schemas; test checks uniqueness + RBAC | 🔴 **no surface parity check** |

🔴 **So when you adopt a vendor's "we pin our tools" claim, read the assertion, not the
file.** `lumen` will not fail if a scope is added without a tool; `bb-mcp` will not fail if a
schema stops being registered. 🟢 **Both are still worth having** — they make the surface
statically enumerable, which is what resolved both rows' `DYNAMIC_UNBOUNDED` verdicts — 🔵
**but they bound the surface from one side and `P21`'s gate must supply the other.**

🟢 **`ACTION EG` builds the missing half for `lumen`** by extending its existing assertion to
check scopes → tools, and will state whether the two sets are in fact equal.


**Pass 144, 2026-10-12.** 🆕 **`P25` is added: the surface-pin gate — require a committed
bidirectional pin before connecting a connector, and generate one when it is missing.** 🆕 **`P26`
is added: the npm connector reachability-and-licence gate, which stops a build on an AGPL row and
on a declared-but-dead repository.** 🔁 **`P18` is amended at steps 2 and 5** — measure the
SHIPPED tree, publish the DEFAULT configuration, and stop reading `gated=0` as "no gate".
🔁 **`P23` is recaveated**: its discriminator needs a calendar span, not a commit count.

## 🆕 🟢 `P25` — the surface-pin gate: require a committed pin, or generate one *(new, p144 — Global)*

**Use when** an engagement is about to connect an education MCP connector to a live LMS, and
someone needs a machine-checked answer to *"what can this thing do to a student's record?"*

🔴 **A static tool count is not that answer**, and `P144-G` shows why: this KB scores
[`divyarthjain/vtop-bhopal-mcp`](https://github.com/divyarthjain/vtop-bhopal-mcp) as
`DYNAMIC_UNBOUNDED` — 0 literal sites, 4 dynamic — while the repository's own test pins **17
named tools**. 🟢 **A committed bidirectional pin beats static analysis because it runs the
server.**

### Step 1 — look for an existing pin, in three places, because there is no standard

🔴 **Three real instances on this shelf use three incompatible formats.** Check all three:

| mechanism | reference implementation | what it pins |
|---|---|---|
| **SHA-256 lockfile** at repo root | [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) → `tools.lock.json` (MIT, 10 tools) | name + annotations + description per tool |
| **Classification manifest** test | [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) → `tests/e2e/test_manifest.py` (MIT, 31 tools) | 🟢 **identity AND write capability** |
| **Golden name array** | [`divyarthjain/vtop-bhopal-mcp`](https://github.com/divyarthjain/vtop-bhopal-mcp) → `scripts/test-published.ts` (Apache-2.0, 17 tools) | the exact name set, `missing` and `extra` |

🟡 **Reject a one-directional pin.** `Piyushtanwani/DAU-buddy`'s
`tests/test_prompt_tool_catalogue.py` says so itself — *"Only one direction is asserted"* — and
`felipedias-ie/blackboard-mcp`'s `test/protocol.test.ts` asserts `tools.length >= 20`. 🔴 **A
floor permits a surface to grow silently**, which is the thing the gate exists to prevent.

### Step 2 — if there is no pin, generate one over the SHIPPED tree

```bash
# the descriptor-counting instrument, over the tree the package actually ships
python3 -I compose/code/p140-live-surface-bound/surface_bound.py <shipped-src-dir>

# and the name SET, which is what parity actually means
python3 -I compose/code/p144-npm-source-parity/namesets.py \
        row=<bundle-or-dist-dir>=<shipped-src-dir>
```

🔴 **Do not point either instrument at a repository root.** `P144-A`: `canvas-mcp-server` and
`mcp-canvas-lms` **commit their own `dist/`**, so a clone holds source *and* a stale bundle, the
tool reads 3 and 2 server instances, and a **54-tool** server reports **0** as `MULTI_SURFACE`.

### Step 3 — copy `edupage-mcp`'s shape, not the lockfile's

🟢 **Classify every tool into disjoint classes and assert both directions:**

1. every live tool from `list_tools()` is accounted for in exactly one class — **no unaccounted**;
2. every name in the manifest still exists — **no stale**;
3. **polled ∩ write = ∅** and **polled ∩ auth/local = ∅**.

🔵 **Class 2 — write-capable — is the deliverable.** It is the machine-checked list of tools that
can change a student's record, and it is what a school's procurement is actually asking for. 🔴 **A
SHA-256 lockfile does not produce it**; it pins identity and says nothing about capability.

### Step 4 — wire the gate into CI, and make adding a tool fail

🟢 **Steal `edupage-mcp`'s contract verbatim**: *"Adding a new tool (or deleting one) must update
this manifest — the test fails."* 🔵 **That sentence is the whole control.** A surface that cannot
change without a human editing a classification file is a surface a deployment can reason about.

### Step 5 — pin the CONFIGURATION too, not just the tool set

🔴 **`P144-D`**: `krzysztofbury/librus-mcp` has **35** tools with every feature on and **31** by
default, because `send_message` defaults to `False` — and the **4-tool gap is exactly the write
surface**. 🟢 **Record the flag values the pin was taken under**, or the pin describes a server
nobody deployed.

### 🔴 What this gate cannot do

🔴 **It cannot see a gate in another file.** `T38`: librus-mcp has three real feature gates and
`surface_gate2.py` reports `gated=0`, because `if config.features.send_message:` lives in
`server.py` while the sites it controls live in `send_tools.py`. 🔵 **Read the registration
helpers' call sites by hand**, and treat `gated=0` as "no gate in the same file".

---

## 🆕 🔴 `P26` — the npm connector gate: reachability and licence, before the first sprint *(new, p144 — Global)*

**Use when** an engagement proposes to build on an education connector published to npm. 🔴 **Five
of the eight on this shelf fail this gate**, so run it before anyone estimates.

### Step 1 — resolve source through THREE metadata fields, not one

```bash
curl -sS "https://registry.npmjs.org/$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1],safe=''))" "@scope/pkg")"
# then read, in order: .repository.url  ->  .homepage  ->  .bugs.url
```

🟢 **`mcp-canvas-lms@1.0.5` has no `repository` field and IS placeable from `homepage`** →
[`MisterCommand/mcp-canvas-lms`](https://github.com/MisterCommand/mcp-canvas-lms). 🔵 **A missing
`repository` is not a dark package**; `P138-H` recorded it as one and `P144-B` corrects that.

### Step 2 — verify with `git ls-remote`, never with `curl`

```bash
GIT_TERMINAL_PROMPT=0 git ls-remote https://github.com/<owner>/<repo> HEAD
```

🔴 **`curl -sI https://github.com/<owner>/<repo>` returns `403` in this environment for live and
dead repositories alike**, so it cannot distinguish them. 🟢 **`git ls-remote` prints a SHA for a
live repo and prompts for credentials for a dead one** — which is how
`@owen-x-tech/canvas-mcp`'s **declared** `owentaylor/canvas-mcp` was shown to be dead.

### Step 3 — do not attempt the sourcemap route; it is closed

🔴 **Three of the eight packages ship `.map` files and ZERO carry `sourcesContent`.**
`@ink-waffle/moodle-mcp` ships **18** maps and not one has source bytes. 🔵 **A map gives original
path names and no original code**, so an unsourceable package stays unsourceable.

### Step 4 — read the licence at HEAD, and stop on copyleft

| package | repo licence | verdict |
|---|---|---|
| `canvas-mcp-server@2.2.3` | 🟢 MIT | 🟢 build |
| `mcp-canvas-lms@1.0.5` | 🟢 MIT | 🟢 build |
| `moodle-mcp-server-aql@0.1.7` | 🔴 **AGPL-3.0** | 🔴 **STOP-SHIP as a dependency** |
| `@ink-waffle/moodle-mcp`, `eth-moodle-mcp` | 🟡 MIT *declared in npm only* | 🟡 **unverifiable — treat as unknown** |

🔴 **The readable Moodle connector is copyleft and the permissive ones are unreadable.** 🔵 **That
is the Moodle supply position in one line**, and p138's rule applies: *a licence identifier is not
a licence.*

### Step 5 — check the repository for an unlicensed row before reading its code

🔴 **`P144-Q`**: [`Piyushtanwani/DAU-buddy`](https://github.com/Piyushtanwani/DAU-buddy) is the
**largest tool surface on the github-only tier — 40 literal tools, 176 commits — and has no
licence file at HEAD.** 🔴 **No licence means no grant.** 🔵 **It is still worth reading as a design
reference**, which is a different permission from building on it, and the distinction belongs in
the engagement's notes rather than in a developer's head.

---

## 🔁 `P18` AMENDED at steps 2 and 5 — measure the shipped tree, publish the default *(p144 — Global)*

🔴 **Three amendments, each from a defect that reached a published figure.**

1. 🔴 **Step 2 — measure the SHIPPED tree, and name it explicitly.** Pointing the instrument at a
   repository root reads committed `dist/` and test servers: a **54**-tool server read **0**.
   🟢 **The exclusion list that makes this work is `{legacy_reference, scripts}`** —
   `P144-H` shows the other nine names in `NOT_SHIPPED` are inert, and `P144-I` shows that
   narrowing to `legacy_reference` *alone* re-admits `scripts/` and inflates librus 35 → 37.
2. 🔴 **Step 5 — publish the DEFAULT configuration's count, not the maximum.** librus-mcp is
   **31** by default and **35** with every feature on. 🔵 **Quote 31 and state the 35.**
3. 🔴 **Step 5 — compare NAME SETS, not counts.** Two trees can both read 14 and name different
   tools; `namesets.py` reports `bundle_only` and `source_only` for exactly this reason.

---

## 🔁 `P23` RECAVEATED — the discriminator needs a calendar span, and bots must be stripped *(p144 — LATAM, Global method)*

🔴 **Two corrections, both from `ACTION DT`.**

1. 🔴 **The requirement is CALENDAR SPAN, not commit volume.** `nitsuah/bb-mcp` has **241
   commits** and cannot be placed, because its whole history runs **2026-03 → 2026-10** — eight
   months lying wholly inside one northern DST period. 🔵 **No number of commits inside a single
   summer contains a winter observation.**
2. 🔴 **Use strict windows, or the recipe manufactures LATAM rows.** A split at Apr–Oct / Nov–Mar
   puts **March and November** in the "winter" bucket, and both hold a DST transition; US Eastern
   is already `-0400` through most of March. 🔴 **This probe's first draft placed `nitsuah` as
   year-round `-0400` — Bolivia or Paraguay — purely from the bucket boundary.**
   🟢 **Use `Dec/Jan/Feb` against `Jun/Jul/Aug` and discard the rest.**
3. 🔴 **Strip bot commits first.** `P144-P`: **9 of 44 rows** carry bot commits and
   `nitsuah/bb-mcp` is **32.4% bot**, with `dependabot` committing at **both `+0000` and
   `-0400`**. 🟢 **`author_window.py` filters `[bot]@`, `dependabot`, `copilot@` and
   `github-actions`.**

🟢 **And prefer the institution over the author when both are available.** `ruud0/aula-virtual-mcp`
is placed **EMEA (Spain)** on `server.py:19`'s hardcoded
`BASE_URL = "https://aula-virtual.unav.edu"` — Universidad de Navarra — while its author commits
at `+0200` in May and `-0400` in September. 🔵 **The institution is where the software deploys;
the author is wherever they were sitting.**

**Pass 143, 2026-10-12.** 🔁 **`P18` is CORRECTED — its tool-surface enumeration misses four
static registration shapes, and on one row it inverts the answer.** 🆕 **`P23` is added: the
timezone recipe that placed a vendor in Colombia from commit metadata alone.** 🆕 **`P24` is
added: how to read a vendor-tenancy hostname without booking the vendor.**

🔵 **Register note.** `P23` and `P24` are the next numbers in the **current** register,
restarted at `P1` by the 2026-10-06 reset. A `P` number resolves against this page; a `P`
number inside a dated log section resolves against the register current on that date.

## 🔁 `P18` CORRECTED — a tool-surface enumeration must recognise FOUR static shapes, not two *(p143 — Global)*

`P18`(a)/(b) tells a studio to enumerate an MCP server's tool surface by finding registration
sites and classifying each as literal or dynamic. 🔴 **The recipe as written misses four static
shapes and misclassifies a fifth**, and
[`p143-surface-gate-repair`](code/p143-surface-gate-repair/README.md) measured the cost on real
rows.

| shape | how it appears | the old recipe | corrected |
|---|---|---|---|
| decorator, name literal | `@mcp.tool(name="x")` | 🟢 `LITERAL` | 🟢 `LITERAL` |
| 🔴 decorator spanning lines | `@mcp.tool(\n  annotations={…},\n)` | 🔴 **invisible** | 🟢 `LITERAL` |
| 🔴 decorator with no `name=` | `@mcp.tool(description="…")` | 🔴 **`DYNAMIC` — wrong** | 🟢 `LITERAL` (name is `fn.__name__`) |
| 🔴 indirection decorator | `@_tool`, where `_tool` → `server.tool(…)(fn)` | 🔴 **invisible** | 🟢 `LITERAL` |
| 🔴 call-applied decorator | `server.tool(annotations=x)(get_grades)` | 🔴 **invisible** | 🟢 `LITERAL` |
| registration in a loop | `for t in TOOLS: server.add_tool(t.name, …)` | 🟢 `DYNAMIC` | 🟢 `DYNAMIC` |

**Step (a), as it must now read:**

> (a) 🔴 **Parse the source; do not grep it.** Use the language's own parser — `ast` for
>     Python — because every shape above except the first is invisible to a line-oriented
>     regex, and a nested multi-line decorator is what defeats one. Count a site as **static**
>     whenever the tool's NAME is fixed by the source at import, 🔴 **including when no `name=`
>     is written at all**: a bare decorator takes the function's own name, and that is the most
>     static shape there is, not the least.

**Step (b), as it must now read:**

> (b) 🔴 **Exclude trees the package does not ship before counting anything** — on these
>     shelves `legacy_reference/`, `scripts/`, `examples/`, `docs/`, plus tests. 🔴 **Report
>     the whole-tree and shipped-tree counts separately and look at any row where they
>     disagree.**

🔴 **The row that proves step (b) is not pedantry.** `krzysztofbury/librus-mcp` was published by
this KB as `DYNAMIC_UNBOUNDED` on **0 literal / 23 dynamic**. The shipped server has
🟢 **35 literal registrations and 0 dynamic**, and all 23 of the measured sites were in
`legacy_reference/src/server.py` and `scripts/qualify_native.py`. 🔵 **The verdict was not
imprecise; it was about a different program.**

🟢 **Validation to copy into the runbook:** a repaired enumeration must reproduce a count you
already know by hand. This one hits **31** on `oliverhruby/edupage-mcp` (p142's hand read) and
**10** on `malkreide/global-education-mcp` (its own committed lockfile). 🔵 **Two independent
agreements are what make the other numbers worth believing.**

## 🆕 `P23` — place a vendor's jurisdiction from commit metadata, using DST as the discriminator *(p143 — LATAM, Global method)*

**The problem.** You need to know where a supplier is, and the usual signals fail: the ccTLD is
ambiguous (`.co` is Colombia *and* a generic registration), the corporate site is unreachable,
and the repository metadata carries nothing.

**Recipe.**

1. **Clone every repository the organisation publishes** — not one. 🔵 eduNEXT: 5 repositories,
   1 485 commits, 63 authors.
2. 🔴 **Do not pool the offsets.** A repository's commits come from many people, and two zones
   pool into exactly the shape one ambiguous zone would. This step was run and returned `MIXED`
   on 5 of 5 — a wasted measurement, recorded so it is not repeated.
3. **Group by author**, and for each author collect the set of commit offsets **and** whether
   they committed inside the DST window (take Apr–Oct) and outside it (Jan, Feb, Dec).
   🔵 Report March and November separately; whole months cannot resolve a transition week.
4. 🟢 **Apply the discriminator.** Among candidate zones that share an offset, use the one
   that differs in *whether it moves*:
   - `-0500` in **both** windows, never `-0400` → a non-DST `-0500` zone: **Colombia, Peru,
     Ecuador**. 🔴 Rules out US Eastern (would be `-0400` in July) **and** US Central (would be
     `-0600` in January).
   - `-0400` in July + `-0500` in January → **US Eastern**.
   - `-0400` in **both** windows → a non-DST `-0400` zone: **Venezuela, Bolivia**. 🔴 Rules out
     Atlantic Canada, which goes to `-0300`.
   - one window only → 🔴 **`UNDETERMINED`. Do not assign it to the majority.**
5. **Corroborate on the author mail DOMAIN**, never the address. 🟢 eduNEXT: `edunext.co` on
   **998 of 1 485 commits (67%)**, and on 6 of the 13 booked authors.
6. 🔴 **State the residual.** The channel does not separate Colombia from Peru or Ecuador.
   🟢 **The `region` field is determined; the country is an inference from the mail domain**, and
   the two are reported as different strengths of claim.

🔴 **When NOT to use it.** A single repository, or an organisation with fewer than ~10 authors
in the Americas, will not produce enough both-window authors to book anything. 🔵 **And publish
domains only** — a contributor's personal address is not a studio's to post.

## 🆕 `P24` — read a vendor-tenancy hostname without booking the vendor *(p143 — Global)*

**The problem.** SaaS LMS deployments live at `<tenant>.blackboard.com` /
`.instructure.com` / `.brightspace.com`. A tenancy names an **institution** precisely and
carries **no country**, and the same domain also carries the vendor's entire estate.

**Recipe.**

1. Extract every `*.{blackboard,instructure,brightspace,moodlecloud,schoology,canvaslms}.{com,net,org}`
   host from tracked source.
2. 🔴 **Classify into four buckets and resolve only the last:**
   - **`VENDOR_INFRA`** — multi-label hosts (`basic-doc-viewer.eu.api.blackboard.com`) and a
     deny-list of vendor labels (`developer`, `api`, `files`, `community`, `docs`, `support`,
     `status`, `login`, …). 🔴 **`developer.blackboard.com` was 19 of the matches in a 44-row
     population. This bucket is the majority and it places nothing.**
   - **`PLACEHOLDER`** — `example`, `your-*`, `my*`, `school`, `institution`, `tenant`.
   - **`OPAQUE`** — `alt-5f0d0e6d23ee0`: a real tenancy whose label is a hash. 🔵 Report, never
     resolve.
   - 🟢 **`TENANCY`** — a **single** label that is an institution's own abbreviation.
3. 🔴 **Resolve a tenancy label only against an explicit, hand-checked table.** There is no rule
   that derives an institution from three letters, and 🔴 **an unrecognised label is
   `TENANCY_UNRESOLVED` and places nothing.** Guessing an institution out of an abbreviation is
   how a `region` field gets poisoned.
4. 🔵 **Record where the evidence sits.** A host in a connector's configured login URL
   (`BB_LOGIN_URL=https://ncat.blackboard.com/`) is stronger than one in a test fixture
   (`ntnu.blackboard.com` in a captured course page) — the first is what the code must reach,
   which is `T29`'s standard.

🔴 **Expected yield, so nobody budgets for more:** 44 repositories produced **2** resolvable
tenancies, one of which was already placed by another channel. 🟢 **Run it once on a
population, take the rows it gives you, and do not build a standing instrument** — `ACTION DK`'s
falsifier fired at exactly this point, and the honest conclusion was to hand-note the one row
and retire the channel.

**Pass 142, 2026-10-12.** 🔴 **`P20` step 2 is CORRECTED — it told a studio to make one licence
election for veraPDF and the election is per-module.** 🆕 **`P21` is added, and like `P19` it is
sourced from a row that already ships the control rather than needing one wrapped around it.**
🆕 **`P22` is added: the regional-placement recipe this KB used to withdraw its own ten-pass
LATAM finding, written so a studio can run it on any shelf.**

🔵 **Register note.** `P21` and `P22` are the next numbers in the **current** register, restarted
at `P1` by the 2026-10-06 reset. 🔴 **The append-only logs carry an unrelated pre-reset `P22`
(*"`P22` check 4"*), and `compose/code/licence-grant-gate/README.md` cites `P22`/`P22.5` in that
older sense.** A `P` number resolves against this page; a `P` number inside a dated log section
resolves against the register current on that date.

## 🔁 `P20` step 2 CORRECTED — the licence election is per COORDINATE, not per project *(p142 — Global)*

`P20` step 2 as written instructs a studio to *elect* between GPL-3.0 and MPL-2.0 for veraPDF,
the PDF/UA validator used when course material carries an accessibility obligation.
🔴 **`ACTION DF` refuted the premise.**
[`p142-verapdf-module-grant`](code/p142-verapdf-module-grant/README.md):

| coordinate a build actually resolves | effective licence | election needed? |
|---|---|---|
| `org.verapdf:core:1.30.3` | **GPL-3.0 *or* MPL-2.0**, inherited at depth **4** | 🟢 **yes — elect MPL-2.0** |
| `org.verapdf:validation-model:1.30.3` | **GPL-3.0 *or* MPL-2.0**, inherited at depth **4** | 🟢 **yes — elect MPL-2.0** |
| 🔴 `org.verapdf:verapdf-xmp-core:1.30.3` | 🟢 **BSD-3-Clause — its own declaration** | 🔴 **NO. There is no dual offer to elect from** |
| 🔴 `org.verapdf:verapdf-library:1.30.3` | the dual offer, in a parent | 🔴 **no jar exists — nothing resolves here** |

**Step 2, as it must now read:**

> 2. For each veraPDF **coordinate in the dependency graph**, walk the `<parent>` chain and record
>    the nearest `<licenses>` block. 🔴 **Do not record one licence for the project.** Elect
>    MPL-2.0 where a dual offer is inherited; record BSD-3-Clause for `verapdf-xmp-core`, which
>    makes no offer to elect from. 🔴 **No veraPDF jar ships licence text**, so the bill of
>    materials must carry the POM coordinate and chain depth as its evidence, not a file path.

🔵 **And one trap to put in the runbook.** `org.verapdf:xmp-core` — the coordinate p141 named — is
`404` on Central. It came out of `<modules><module>xmp-core</module></modules>`, and
🔵 **a `<module>` entry is a source-tree path, not an artifactId.** Never derive a coordinate from
a `<modules>` block.

## 🆕 🟢 `P21` — pin your tool surface with a committed lockfile *(p142 — EMEA)*

**Sourced from:** [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp)
(MIT) and [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) (MIT), which
between them already implement both halves.

**The problem it solves.** This KB has built four instruments to detect tool-surface drift —
`p139-tool-count-drift`, `description-drift-audit`, `p141-agent-surface-gate`,
`p142-github-only-tier` — because a connector's tool set changes without its version changing,
and a client discovers that at runtime. 🔴 **And `@owen-x-tech/canvas-mcp` shows the failure mode
at its worst**: a README claiming **150+ tools** against **62** served, on a row whose repository
no longer exists.

**The recipe, concretely.**

1. **Annotate every tool at its registration site**, using MCP's own `ToolAnnotations` —
   `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`, `title`. 🟢 **Copy
   `edupage-mcp`'s shape**: a module-level table mapping tool name → annotation class, with
   named classes rather than inline dicts:

   ```python
   _READ                 = {"readOnlyHint": True,  "destructiveHint": False, "idempotentHint": True}
   _WRITE_DESTRUCTIVE    = {"readOnlyHint": False, "destructiveHint": True,  "idempotentHint": True}
   _WRITE_NON_IDEMPOTENT = {"readOnlyHint": False, "destructiveHint": True,  "idempotentHint": False}
   TOOL_ANNOTATIONS = {"get_grades": _READ, ..., "send_message": _WRITE_NON_IDEMPOTENT}
   ```

   🟢 **`edupage-mcp` has 31 of 31 tools classified and 12 of 31 declared as writes** — the first
   row on any of these three tiers whose write count is quotable rather than derived.

2. **Emit a `tools.lock.json`**: one SHA-256 per tool over its *signature* — annotations,
   description and input schema. 🟢 **`global-education-mcp` ships exactly this**, and its own
   logging wrapper preserves `__doc__` *"damit der `tools.lock.json`-Hash stabil bleibt"*.

3. **Fail CI when the lockfile and the source disagree**, and require the diff in the PR that
   changes a tool. 🔵 **This is the step that converts the file from documentation into a
   control.**

4. **In the engagement contract, reference the lockfile hash rather than a tool count.** A count
   in prose is what drifted; a hash cannot.

5. 🔴 **Enumerate per `P18` (a)–(d) anyway, on the deployment you are actually given.** A
   lockfile pins what the build registers. It does not pin what a `GATED` or `DYNAMIC` server
   serves under someone else's configuration, and `P18`'s amendment still governs that.

🔴 **Known limit, stated so it is not discovered later.** A lockfile makes a surface *checkable*,
not *bounded*: a `DYNAMIC` server that walks a table assembled at runtime can ship a stable
lockfile and serve a different set. 🔵 **`P21` and `P18` are complements** — `P21` proves the
build has not changed, `P18` measures what the deployment serves.

## 🆕 🟢 `P22` — place a repository's region on two weak channels in conjunction *(p142 — all regions)*

**Sourced from:** this KB withdrawing its own ten-pass finding. 🔵 **Written up as a pattern
because the failure it prevents is one every studio doing regional sourcing will hit.**

**The problem.** You need to know where a candidate repository comes from — for a regional
engagement, a data-residency question, or a procurement conversation. 🔴 **Neither obvious channel
works alone**: author email domains are free-mail six times out of eight, and the commit UTC
offset is ambiguous across regions for **every American country**.

**The recipe.**

1. **Read the commit offsets**, not the author names. `git log --format=%ad --date=format:%z`.
   An offset is written by the author's machine and cannot be edited by a later reader.
2. 🔴 **Refuse to book any offset shared across two regions.** `-0300`, `-0400`, `-0500`,
   `-0600`, `-0700` are each shared between North America and LATAM; `+0000` is what a CI
   container writes and is evidence of nothing.
3. 🔴 **Then look at what you refused.** If the refusals cluster in the region reporting zero,
   your zero is about the instrument — `T32`. 🟢 **Always print a second region's count as a
   control**, even when nobody asked for it; an implausible zero beside a plausible one is what
   makes the plausible one checkable.
4. **For the refused rows, extract hardcoded hostnames from tracked source** — excluding
   `node_modules`, vendored trees, lockfiles and placeholder hosts. 🔵 **Require three or more
   labels**: `service.name.tld` is a host the code must reach; `name.tld` is a registrable name,
   and `scraper.py` is neither.
5. **Book only where every country-bearing host agrees on one of the candidate regions.**
   Disagreement stays `UNMAPPED`. 🟢 **The conjunction of an ambiguous offset and a single-region
   ccTLD host is publishable where neither half is** — `T33`.
6. 🔴 **Exclude ccTLDs that are filename extensions.** `.py` Paraguay / Python, `.do` Dominican
   Republic / Struts action, `.cu` Cuba / CUDA, `.cl` Chile / OpenCL — and 🔴 **declare the
   coverage you lose**, because the alternative is booking Paraguay off `auth.py`.
7. 🔴 **Do not treat `.edu` as a US signal.** `aula-virtual.unav.edu` is the Universidad de
   Navarra, in Spain, on a pre-2001 registration. Record it as corroboration; wait for a ccTLD.
8. 🔴 **Do not let `\b` end your hostname match.** `123.dkr.ecr.us-east-1.amazonaws.com` parses
   as the `.us` host `dkr.ecr.us` — a cloud region identifier booked as a country.
9. 🟢 **Validate against a row you already placed by another method.** This KB's control is
   `campus-cli`, placed in Peru passes ago by reading its README and re-placed by the instrument
   from 16 hardcoded `upc.edu.pe` hosts.

**What it bought, on 44 rows:** the offset channel placed **23** (12 EMEA, 11 APAC, 🔴 **0
American**); the conjunction placed **16 of the 19** it had refused — 🟢 **13 LATAM and 3
Canada**. Instruments: [`p142-origin-at-scale`](code/p142-origin-at-scale/README.md) and
[`p142-americas-disambiguation`](code/p142-americas-disambiguation/README.md), 21 tests between
them, every homograph regression pinned.

**Pass 140, 2026-10-12.** 🆕 **`P19` is added, and it is the first pattern on this page sourced
from a row that already SHIPS the control rather than needing one wrapped around it.** 🔁 **`P18`
is amended at step 5**: enumerate per *deployment configuration*, not per package — because
`ACTION CP` established that a connector's tool surface is a property of its flags.

## 🔁 `P18` amended again at step 5 — a static tool count is a BOUND only on the npm connector tier *(p141 — Global)*

p140 amended step 5 to enumerate per **configuration**, because `tutor-mcp`'s surface moves with
`deps.Institution` and `REGULATION_GOAL`. 🔴 **`ACTION CZ` shows the amendment was both too
narrow and too broad.**

| | npm connector tier | 🔴 agent-server tier |
|---|---|---|
| rows measured | 8 *(p140)* | 4 *(p141)* |
| 🔴 **dynamic registration** — name from an expression | 1 — **12%** | 🔴 **2 — 50%** |
| flag-gated registration | 0 | 🔴 **0** |

🔵 **So gating is one row's maturity, not a tier property — and the thing that actually defeats a
static enumeration is DYNAMIC registration, which is the majority shape one tier up.**

### The amended step 5

> 5. **Enumerate the tool surface with the method the tier requires, and say which you used.**
>
>    a. **Grep for name literals** at registration sites. 🟢 On the npm connector tier this is
>       sufficient and *provably* so: a single server instance + literal names + no gate forces
>       the live `tools/list` to equal the static count, for 7 of 8 measured rows.
>
>    b. 🔴 **Then count registration sites whose name comes from an EXPRESSION** —
>       `for (const t of TOOLS) server.registerTool(t.name, …)`,
>       `@mcp.tool(name=name)` inside a walk over a spec table. **If that count is non-zero,
>       step (a)'s number is meaningless and must not be reported.** Resolve the collection
>       instead: `ahmedEid1/lumen` serves **10** tools from 10 `ToolSpec(` entries where a
>       literal count returns **1**; `nirholas/ai-tutor-mcp` serves **2** where it returns **0**.
>
>    c. 🔴 **Then look for gating ONE INDIRECTION UP, not at the registration site.**
>       `tutor-mcp` gates in `tools/tools.go`, where `registerGetNextActivity(server, deps)` is
>       called inside `if deps != nil && deps.Institution` — while the name literal sits in an
>       `addTool(…)` helper two frames away. 🔵 **No lexical test at the name site can see this**,
>       which is why `p141-agent-surface-gate`'s Go lane fails its own control and publishes no
>       Go verdict. Read the central register function by hand.
>
>    d. **Report the method, the tier and the residual uncertainty**, in the delivery document.
>       🔴 **"62 tools" with no method attached is the number that produced p140's 61-tool blind
>       spot.**

🟢 **Tooling**: [`p140-live-surface-bound`](code/p140-live-surface-bound/README.md) for
TypeScript/JavaScript, [`p141-agent-surface-gate`](code/p141-agent-surface-gate/README.md) for
Python `FastMCP`, JavaScript and hand-rolled PHP. 🔴 **Neither covers Go**; that one is manual.

---

## 🆕 `P20` — The three-layer due-diligence gate: run it before the first sprint, in under an hour *(new, p141 — Global)*

🔵 **This pass measured four numbers a buyer would want before signing, none of which appears in
any market report on `intel/market.md`, all four from published artefacts in under an hour.**
`P20` is that hour, written down as a gate with named components.

### What it answers, and why each question has burned this KB

| layer | the question | what goes wrong if you skip it |
|---|---|---|
| **1. Grant** | Where is the licence, really? | 🔴 **5 of 9 Maven coordinates declare nothing in their own POM.** `org.verapdf:verapdf-library` — the PDF/UA accessibility validator — is **dual GPL-3.0 / MPL-2.0** two levels up, and a scanner reading the named coordinate reports *"no licence"* |
| **2. Payload** | Does the grant travel with the code you will copy? | 🔴 **`openedx-core` 1.9.1: 0 licence files, 0 SPDX headers, 0 copyright lines in 237 files across six packages**, under an **AGPL-3.0-only** distribution. Lift `openedx_tagging/` and the obligation travels silently |
| **3. Data** | What does it actually store about a learner? | 🔴 **96 of 118 tables in `tutor-mcp` are declared only in Go source.** A DPIA that enumerates `db/*.sql` finds `learners.email` and misses `pedagogical_decisions`, `assessment_attempts` and `audit_events` |

### The stack

| role | component | licence |
|---|---|---|
| grant resolution, Maven | [`p140-pom-parent-chain`](code/p140-pom-parent-chain/README.md) — walks `<parent>` upward, XML-parsed, `<licenses>` only as a direct child of `<project>` | KB-internal |
| grant resolution, npm/PyPI | [`p138-npm-payload-licence`](code/p138-npm-payload-licence/README.md) + [`p141-package-grant-layer`](code/p141-package-grant-layer/README.md) | KB-internal |
| notice injection | `P17`'s build step — the remedy for layer 2 | — |
| schema enumeration | [`p141-schema-location`](code/p141-schema-location/README.md) — `CREATE TABLE` across `.sql` **and** embedded migration bodies, comments stripped | KB-internal |
| tool-surface enumeration | `P18` as amended above | — |
| origin / accountability | [`p141-repo-origin-layer`](code/p141-repo-origin-layer/README.md) — compiled-in hosts, Maven `groupId`, commit offsets, with ambiguous offsets refused | KB-internal |

### How it wires together

1. **Resolve every coordinate's grant to a file, not a field.** For Maven, run the parent-chain
   walk and record the **depth** at which the grant appears. 🔴 **Continue past a silent
   ancestor** — `org.sonatype.oss:oss-parent:7` is the shared grandparent of two chains on this
   shelf and declares nothing. For an artefact that is `<packaging>pom` or `war`
   (`verapdf-library`, `org.jasig.ssp:ssp`), 🔴 **there is no jar to inspect**; resolve the
   modules consumers actually pull.
2. **For every dual or multi-licence grant, ELECT in writing.** veraPDF offers MPL-2.0 beside
   GPL-3.0; the election is free and is irrecoverable later if nobody made it.
3. **Decide what will be COPIED rather than depended on**, and run `P17`'s notice injection on
   exactly that subtree. 🔵 **This is the step that pays for the whole gate**: `openedx_tagging/`
   is 56 files that today carry no grant at all.
4. **Enumerate the schema from source, not from `.sql`.** Then diff the result against the DPIA's
   table list. 🔴 **On the one subject measured, that diff is 96 tables wide.**
5. **Enumerate the tool surface per `P18` (a)–(d)**, and treat any non-zero dynamic-registration
   count as a hard stop on reporting a tool number.
6. **Record accountability, or record that you cannot.** 🔴 **5 of 8 npm connector rows on these
   shelves declare no repository in any published version**, and one declares an unreadable one —
   so for those rows the honest entry in a vendor register is *"no accountable publisher
   identified"*, not a guess from the package name.

### Shape of the engagement

**1 day**, run by one engineer before the first sprint, on a laptop. No vendor contact, no NDA,
no running of third-party code — 🟢 **every measurement above was taken from published
registry artefacts and `git clone`**, which is why it fits in a day and why it can be re-run on
every dependency bump.

### Why it wins the room

🔵 **Because every one of its findings is a sentence a procurement officer can act on, and none
of them requires trusting the vendor's description.** *"Your accessibility validator is
GPL-3.0-or-MPL-2.0 and nobody has elected"*; *"the 56 files you are about to copy carry an AGPL
obligation and no notice"*; *"your DPIA lists 22 tables and the system has 118"*. 🟢 **And the
gate's own instruments are committed with tests, controls and their failures recorded** — three
of them corrected themselves this pass, one withheld a verdict because its control failed. 🔵
**A due-diligence tool that publishes its own limits is the only kind a client should accept.**

---

## 🔁 `P19` STRENGTHENED — the oversight primitive is enforced by the DATABASE, not by the agent *(p141 — EMEA)*

p140 adopted `tutor-mcp`'s one-way `mark_domain_high_stakes` as `P19`, on the strength of a
missing inverse tool and a typed evidence policy. 🟢 **`ACTION CX` found the layer underneath it,
and it is stronger than p140 could claim.**

`pedagogical_decisions` — declared in `db/pedagogical_contract_schema.go`, not in any `.sql` file
([`p141-schema-location`](code/p141-schema-location/README.md)):

| guarantee | mechanism | enforced by |
|---|---|---|
| append-only | `pedagogical_decisions_no_update BEFORE UPDATE … RAISE(ABORT, 'pedagogical decisions are immutable')`; Postgres `tutor_immutable_pedagogical_decision()` `FOR EACH ROW` | 🟢 **the engine** |
| tenant isolation the table owner cannot bypass | `ENABLE` **and** `FORCE ROW LEVEL SECURITY` + policy on `current_setting('app.current_tenant')` | 🟢 **the engine** |
| one decision per graded attempt | `assessment_attempts.decision_id REFERENCES pedagogical_decisions(id)` + `CREATE UNIQUE INDEX idx_assessment_decision_once … WHERE decision_id IS NOT NULL` | 🟢 **the engine** |
| 🟢 **the recommendation and the assessment cannot drift apart** | `assessment_decision_scope` refuses the insert unless `json_extract(p.snapshot_json, '$.contract.target_concept') = NEW.concept_id` **and** the recommended activity type matches, at the pinned `curriculum_version` | 🟢 **the engine** |

### What to steal, concretely

🔵 **Not the code — the shape.** Three rules, portable to any stack and cheap to add:

1. **Make the decision log append-only in the database**, with a trigger that raises. 🔴 **An
   application-level "we never update this" is not an audit trail**; it is a convention that
   survives until the next migration script.
2. **Bind the decision to the artefact it produced, with a unique index and an immutability
   trigger on the identity columns.** 🟢 This is what lets you answer *"was this learner graded
   against the thing the system recommended?"* with a query instead of an investigation.
3. **Type the evidence that can clear a safety gate.** `tutor-mcp`'s own policy string:
   `"trusted human_review evidence is required; host_llm and external_service evaluations do not
   satisfy this gate"`. 🔵 **The model cannot certify itself** — and `FORCE ROW LEVEL SECURITY`
   is what stops a privileged service account from editing the record of that refusal.

🟡 **The caveats are unchanged and still belong in the room**: alpha, one maintainer, 🔴 its
institutional tier is undocumented, and 🔴 **three undocumented writes in that tier —
`draft_formation`, `publish_formation`, `add_formation_concepts` — author the curriculum a cohort
is assessed against.** 🟢 **Adopt the three rules; do not adopt the dependency without `P20`
step 4.**

---

## 🔁 `P18` amended at step 5 — enumerate per CONFIGURATION, because the surface moves with the flags *(p140 — Global)*

p139 wrote `P18` step 5 as *"call `tools/list` on the running server and diff again — because
registration is not behaviour"*, and pre-registered `ACTION CP` to test whether that step was
needed at all. 🔴 **It is needed, and for a different reason than p139 gave.**

🟢 **On the npm connector shelf, registration IS behaviour.** All eight downloadable rows are a
single server instance registering literal tool names with no gate, so the live `tools/list` is
*forced* to equal the static build count — provable from the payload, without running anything
([`p140-live-surface-bound`](../compose/code/p140-live-surface-bound/README.md)). For those rows,
a static count is sound.

🔴 **The step survives because of the rows that are not shaped like that**, and this pass found
both failing shapes:

| shape | instance | what breaks |
|---|---|---|
| 🔴 **deployment-flag gating** | `ArnaudGuiovanna/tutor-mcp`: `deps.Institution`, `REGULATION_GOAL`, `deps.OAuthGranularScopes` | **55** names in the build; its own CI test asserts a live list of **46**. 🔵 No payload read can tell you which flags a client sets |
| 🔴 **dynamic registration** | `@owen-x-tech/canvas-mcp`: `for (const tool of tools) httpMcp.registerTool(tool.name, …)` | **1** name literal on the HTTP path; **62** tools served |
| 🔴 **two server instances** | same package, `--http` vs stdio | two surfaces under one version number |

### The amended step 5

> 5. Call `tools/list` **against each configuration the engagement will actually run** —
>    every transport the client will connect on, and every feature flag the contract enables —
>    and diff each result against the documentation *and against the other configurations.*
>    🔴 **Record the flag set beside the count.** A tool count with no configuration attached is
>    not a measurement.

🔵 **The practical consequence for a delivery team is a line item, not a philosophy**: if the
contract turns on an institutional tier, the tier's tools are the ones least likely to be
documented. On `tutor-mcp` that is exactly where the three undocumented writes are.

## 🆕 `P19` — Adopt the one-way high-stakes gate as the engagement's oversight primitive *(new, p140 — Global)*

🔵 **Every high-risk control this page has specified until now was something Globant builds AROUND
a component.** `P15` ships an Article 50 obligation, `P16` assembles a Decision 33 dossier, `P18`
gates a connector whose writes nobody enumerated. 🟢 **`ACTION CT` found a row that ships the
control itself, in MIT-licensed source, and it is better than what this page has been
specifying.**

### The primitive, as [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) implements it

`mark_domain_high_stakes` applies a **one-way** classification to a learning domain. Once set:

| property | implementation |
|---|---|
| 🟢 **irreversible from the agent tier** | **no inverse tool exists** — this pass searched for `unmark_*`, `clear_*`, `unset_*`, `reset_*` and found none |
| 🟢 **rationale recorded in code** | `db/store.go`: *"Downgrading safety classification requires an operator-controlled process that is outside the learner-facing MCP trust boundary."* |
| 🟢 **evidence provenance is typed** | returns `"policy": "trusted human_review evidence is required; host_llm and external_service evaluations do not satisfy this gate"` |
| 🟢 **capabilities withdrawn, not warned about** | returns `demonstrated_claims_allowed: false`, `intrusive_notifications_allowed: false` |
| 🟢 **degradation is explicit** | returns `degraded_components: ["human_review_evidence_readback"]` rather than failing silently |

🔵 **The design idea worth stealing is that the model cannot certify itself.** A `host_llm`
evaluation is *typed as insufficient*, so "the AI reviewed it" is not a path through the gate.
🔴 **That is the one property every regulator in this KB's matrix is reaching for and almost no
implementation expresses** — EU AI Act **Article 14** human oversight, **Annex III** grading and
ranking, Vietnam's **Decision 33/2026/QĐ-TTg**, and the Oklahoma and Maryland statutes requiring
human oversight and barring AI from high-stakes decisions about students.

### Why this row is inside the regime at all

🔴 Not a judgement — its schema
([`p140-agent-tier-pii`](../compose/code/p140-agent-tier-pii/README.md)):

- `learners.email` — `TEXT UNIQUE NOT NULL`, a **direct identifier**
- `affect_states` — a **per-session psychological profile** keyed `UNIQUE(learner_id, session_id)`:
  `energy`, `subject_confidence`, `satisfaction`, `perceived_difficulty`, `next_session_intent`,
  `autonomy_score`
- **27 of its 55 tools are writes**, including `submit_assessment_attempt`,
  `publish_curriculum_revision`, `update_learner_profile`, `record_affect`

🔵 **p138 established that Vietnam's Decision 33 names psychological assessment in its education
high-risk list.** `affect_states` is that, persisted, per session. A deployment of this row is
inside Annex III *and* Decision 33 on the strength of its schema alone.

### The stack

| layer | component | licence | why |
|---|---|---|---|
| oversight primitive | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) `mark_domain_high_stakes` | 🟢 **MIT** | the gate, and MIT means it can be lifted into client code |
| adaptive core *(same row)* | its `algorithms/` — BKT, FSRS, IRT, KST | 🟢 **MIT** | 286 test files against 279 source files |
| LMS attachment | the sanctioned-integration stack of `P11` (LTI AGS, OneRoster, xAPI/LRS) | permissive | `P19` governs decisions; `P11` moves them |
| connector gate | `P18` as amended above | — | the LMS write surface still needs enumerating per configuration |
| dossier | `P16` (Decision 33) / `P15` (Article 50) | — | `P19` produces the oversight *evidence* those dossiers assert |

### How it wires together

1. **Lift the gate, not the product.** The engagement adopts the *contract* —
   one-way classification, typed evidence provenance, no self-certification, explicit
   degradation — into whatever system of record the client already runs. 🟢 **MIT permits
   copying the source outright**, which is why this is `P19` and not a build-from-scratch.
2. **Bind the classification to the client's high-stakes definition.** For an EMEA client that is
   Annex III (admission, evaluation, exam scoring, proctoring); for a Vietnamese deployment it is
   Decision 33's list *including psychological assessment*; for Oklahoma or Maryland it is the
   statute's "high-stakes decisions about students".
3. **Make the inverse operator-only.** 🔴 **Reproduce the absence of the inverse tool.** If a
   downgrade path exists in the agent tier, the gate is advisory and the dossier claim is false.
4. **Type the evidence, do not merely log it.** `human_review` must be a distinct, trusted kind
   that `host_llm` and `external_service` cannot satisfy. 🔵 **Most "human in the loop" builds
   fail precisely here** — they record who clicked, not what class of evaluator it was.
5. **Enumerate the surface per configuration** (amended `P18` step 5). On this row, enabling the
   institution tier turns on `draft_formation`, `publish_formation` and `add_formation_concepts` —
   🔴 **three undocumented writes that author the curriculum a cohort is assessed against.**
6. **Carry the degradation signal into the dossier.** `degraded_components` is the field an
   auditor needs and the one hand-rolled implementations omit.

### Shape of the engagement

**6–8 weeks.** Weeks 1–2: map the client's high-stakes definition onto the classification and
confirm the statutory list that applies. Weeks 3–5: lift and bind the gate, with the
operator-only downgrade path built outside the agent trust boundary. Week 6: enumerate every
configuration's tool surface and document the tier the vendor did not. Weeks 7–8: assemble the
`P15`/`P16` dossier around the oversight evidence the gate now produces.

### Why it wins the room

🔵 **It inverts the usual conversation.** The standing pitch has been *"your AI tutor needs
governance we will build"*. This one is *"a working implementation of the oversight duty exists
under MIT, we have read its schema and its gate, and here is what it does that your current build
does not — the model cannot sign off on itself."* 🔴 **And the honest caveat is part of the
pitch**: the row is **alpha**, single-maintainer, and its own institutional tier is undocumented.
🟢 **Globant is adopting a contract, not a dependency** — which is the version of this argument
that survives procurement.

**Pass 139, 2026-10-12.** 🟢 **`P13` is revised a fifth time — and this time from an EXECUTION
rather than a reading.** `ACTION CL` ran the adapter against a live server: the protocol half is
cheaper than p138 estimated and the integration half is dearer, in a specific and fixable way.
🆕 **`P18` is added** because 62 undocumented write tools across nine connectors is not a caveat on
`P17`, it is its own gate.

## 🔁 `P13` rewritten — the grant goes in the store, and the server runs as a process *(fifth revision, p139)*

🟢 **Executed, not estimated.** p138's fourth revision rested on reading
[`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp)'s `OAuthStore` interface.
`ACTION CL` seeded a fixture grant and drove the real server over HTTP. Full transcript and harness:
[`p139-oauthstore-adapter`](../compose/code/p139-oauthstore-adapter/README.md).

**What the run proves:**

| step | result |
|---|---|
| `POST /oauth/token`, `grant_type=refresh_token`, grant pre-seeded | 🟢 **HTTP 200** |
| token issued | 🟢 `mcpat_…`, `Bearer`, `expires_in: 3600` |
| scopes from the seeded grant | 🟢 `canvas:read canvas:write` |
| refresh rotation (single-use, OAuth 2.1 §6.1) | 🟢 **rotated** |
| 🟢 **Canvas contacts during the entire flow** | 🟢 **0**, measured by a sentinel listener |
| grant store at rest | 🟢 **`scrypt` + AES-GCM, no plaintext** |

🔵 **So an institution that already holds Canvas refresh tokens — from an LTI launch, a prior
consent, or a service account — can mint MCP tokens for its own clients with no user redirect and no
Canvas call.** That is the whole premise of `P13`, and it is now demonstrated rather than inferred.

🔴 **The cost moved, it did not vanish.** `dist/http.js` calls `main()` at module top level with no
`import.meta.main` guard, so `import { createHttpHandler } from 'canvas-lms-mcp/http'` parses the
**importer's** `process.argv` and calls `process.exit(1)`. 🔴 **The `oauthStore` config seam is
therefore unreachable by import**, and the per-module `.d.ts` tree describes the source rather than
the bundled payload (`AuthorizationServer`, `ClientResolver`, `CanvasOAuthClient` are **not**
exported; only five symbols are).

### The build, as it actually has to be done

```text
1.  Seed:   FileOAuthStore.open(path, keySecret)
              → putClient({ clientId, clientSecretHash: sha256(secret),
                            grantTypes: ['authorization_code','refresh_token'],
                            source: 'preregistered' })
              → putGrant({ id, clientId, scopes, resource,
                           canvasUserId, canvas: { accessToken, refreshToken, expiresAt } })
              → putToken({ hash: sha256(refresh), kind: 'refresh', grantId, … })
              → flush()
2.  Run:    CANVAS_AUTH_PROFILE=oauth_brokered \
            CANVAS_MCP_ISSUER=https://… CANVAS_BASE_URL=https://canvas.inst.edu \
            CANVAS_OAUTH_CLIENT_ID=… CANVAS_OAUTH_CLIENT_SECRET=… \
            CANVAS_MCP_OAUTH_STORE=/var/lib/…/store.json \
            CANVAS_MCP_OAUTH_STORE_KEY=… \
            node dist/http.js serve --port 8097
3.  Verify: GET /.well-known/oauth-authorization-server   ← take endpoint paths from HERE
            POST /oauth/token  (NOT /token — that is a 404)
```

🔵 **Take the endpoint paths from the metadata document.** This pass lost a run posting to `/token`;
the issuer mounts OAuth under `/oauth`, and `authorization_endpoint`, `token_endpoint`,
`registration_endpoint` and `revocation_endpoint` are all advertised.

| element | estimate |
|---|---|
| 🟢 brokered token flow against a pre-seeded grant | 🟢 **hours — it works as shipped** |
| the LTI→grant seeding job (`kstateome/lti-launch` → `putGrant`) | **3–5 days** |
| 🔴 process supervision, store key management, rotation/backup of the encrypted store | 🔴 **3–5 days — this is the new line item** |
| 🟡 *optional* fork or one-line patch adding a `main` guard, if an in-process embed is required | 🟡 **1 day + a maintenance burden** |
| **total** | 🟢 **~1.5–2 weeks, and the risk has moved from protocol to plumbing** |

🔴 **Two licence conditions to settle before this ships.** `canvas-lms-mcp` is **MIT and ships its
`LICENSE` in the payload** (🟢 clean, verified p138). But `edu.ksu.ome.lti:lti-launch` **1.4.7** is
**LGPL-3.0 and ships NO licence text in its jar** — so step 1's dependency obliges a notice the
artefact does not provide, and the text must be taken from
[the repository](https://github.com/kstateome/lti-launch) and shipped deliberately. 🔵 **Run `P17`
over both before writing any of this.**

## 🆕 `P18` — The tool-surface gate: enumerate what the connector can DO before anyone connects it *(new, p139 — Global)*

🔴 **Why this is a gate and not a checklist item.** Across the nine published LMS connectors
measured this pass: **411 tools registered, 249 documented, 162 undocumented — and 62 of those
mutate the LMS.** One package registers **227** tools and documents **96**, with **61 undocumented
writes** including `bulk_update_grades`, `grade_submission`, `create_user`, `update_user_login` and
🔴 **`update_sso_settings`**. 🔵 **"Grading or ranking learners" is named high-risk by EU AI Act
Annex III and Vietnam's Decision 33/2026/QĐ-TTg. A duty cannot be discharged against a capability
nobody enumerated — and the README is what procurement reads.**

**The recipe**

| step | what you do | tool |
|---|---|---|
| 1 | Pull the **payload**, not the repo. Verify the registry's own digest (sha1 on npm, sha256 on PyPI, `.sha1` on Maven) | `p138-npm-payload-licence`, `p139-pypi-maven-payload` |
| 2 | Count **registered** tools in the shipped build across all three idioms — `registerTool(…)`, `{ name, …, inputSchema }`, and a module exporting `name` + `inputSchema` | [`p139-tool-count-drift`](../compose/code/p139-tool-count-drift/README.md) |
| 3 | Diff against the package's own documentation → the **undocumented** set | same |
| 4 | Partition the undocumented set by **write verb** → the **governance** set | `count_tools.is_write_tool` |
| 5 | Call `tools/list` on the **running** server and diff against step 2 — registration is not behaviour, and a stub is not a capability | your MCP client |
| 6 | For every write tool reaching grades, identity or enrolment: either **disable it at the gateway** or **file it in the conformity dossier** (`P16`) / Annex III technical documentation (`P15`) | `mcp-allowlist-gateway` |
| 7 | Re-run at **every dependency bump**. `@imazhar101/mcp-canvas-server` went 2.1.3 on 2026-10-01; the tier publishes weekly | CI |

🔵 **Step 6 is where this pattern pays for itself**: this KB already carries
[`mcp-allowlist-gateway`](code/mcp-allowlist-gateway/README.md), so the remediation is configuration
of something that exists, not a build.

🔴 **Two preconditions this gate also catches, both found this pass:**

- 🔴 **A package may contain no server at all.** `@exhabition/brightspace-mcp` is an **82-line
  loader** that downloads a Rust binary from GitHub Releases, `chmod 0o700`s it and `spawn`s it with
  **no checksum or signature**. Steps 2–4 correctly return **0** and tell you nothing; step 1 and a
  read of `bin/` are what catch it.
- 🔴 **A package may contain no code at all.** `openedx-learning` **0.33.0** and **0.33.1** are
  **1 479-byte** wheels holding only `dist-info` metadata, down from **257 553 B** at 0.32.0. 🔵 **Pin
  `0.32.0`** and make "artefact is non-empty" an assertion in step 1.

**Effort:** 🟢 **2–3 days to stand up for one connector family, then minutes per bump in CI.**
**Deliverable:** a signed tool inventory, a diff against vendor documentation, and a gateway
allowlist — 🔵 **which is exactly the artefact an Annex III or Decision 33 reviewer asks for and
that no vendor currently supplies.**


---

**Pass 139 — second probe lane (`ACTION CH`), 2026-10-12.** 🔁 **`P17` is rewritten one pass after it was added, and the change makes
it shippable.** p138 created it as a gate that proves what you are about to redistribute; `ACTION
CH` then measured that **0 of 9** licence-file-less packages carry a grant in their source either,
and that **only 1 of 21** rows on the whole shelf practises per-file notice. 🔴 **So a gate that
only checks for a root licence file passes 11 packages whose grant any partial copy silently
drops.** `P17` now gates both layers and ships a notice-injection step. 🆕 **`P18` is added** for
the AGPL row, because it is the one finding on this shelf that should stop a delivery rather than
annotate it. 🔵 **No pattern is added from the search channel: 11 searches returned 0 new rows.**

## 🔁 `P17` rewritten — the two-layer licence gate, plus the notice the build must inject *(second revision, p139 — Global)*

**The problem p138's version missed.** A gate that asks *"does the payload contain a licence
file?"* splits this shelf 12 / 9 and calls the 12 clean. 🔴 **But a root licence file discharges
redistribution of the whole package and nothing about a single file.** A developer who copies one
module out of a clean MIT connector into a client's codebase carries **no holder and no grant** on
20 of 21 rows — and that copy, not the tarball, is what ends up in the client's repository.

### The stack

| component | licence *(payload-verified this pass)* | role |
|---|---|---|
| [`p139-source-header-grant`](code/p139-source-header-grant/README.md) | this KB | reads every shipped text file; reports own-grant vs `VENDORED` vs none. **24 tests** |
| [`p138-npm-payload-licence`](code/p138-npm-payload-licence/README.md) | this KB | the root-file layer, sha1-verified against the registry's `shasum`. **7 tests** |
| 🟢 [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) | 🟢 **MIT** (`LICENSE` ships; notice in **100 of 118** files) | 🟢 **the reference implementation of the output** — copy its header convention verbatim |

### How it wires together

1. **Gate A — the root layer.** For each dependency, download the published tarball, **sha1-verify
   it against the registry's own `shasum`**, and enumerate paths. No licence file and no SPDX id →
   🔴 **block**. SPDX id without text → 🔴 **block** and fetch the grant from the repository.
2. **Gate B — the file layer *(new)*.** Read every shipped text file. 🔵 **Report own-grant,
   `VENDORED` and none as three separate counts, never two** — a notice in minified output is a
   bundled dependency's and must not be credited to the package. A dependency at **0%** own-notice
   is not blocked; it is **flagged for step 3**.
3. **Inject on copy.** Any file lifted out of a flagged dependency and into the client's tree gets
   a header naming **that dependency's** holder and grant, applied by a build step, not by hand.
   This is the deliverable that makes Gate B worth running.
4. **Resolve the dangling references.** 🔴 A vendored notice pointing at a `LICENSE file in the
   root directory` that does not ship is an **unresolved** reference, not a satisfied one — fetch
   the named text and vendor it alongside.
5. **Pin and re-run per release.** Both gates read a *version*, and 5 of the 21 rows published
   inside eleven days.

### Why it wins the room

🔵 **It converts a licence column into a build step.** The client's question is never *"what does
the table say?"* but *"what is in our repository and can we ship it?"* — and on this shelf the
honest answer requires reading the bytes twice, at two layers.

## 🆕 `P37` — Stop-ship gate for the one copyleft row on this shelf *(p139, RENUMBERED by p150 — Global)*

🔴 **`moodle-mcp-server-aql` 0.1.7 declares AGPL-3.0, ships 141 paths and 71 text files, and
carries no grant at either the file layer or the header layer.** Its repository
([`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server)) carries the
canonical text, re-verified this pass at **34 523 B**, first line `GNU AFFERO GENERAL PUBLIC
LICENSE`. 🔵 **The grant exists; the distribution drops it.**

### Why this is a pattern and not a footnote

AGPL-3.0 is the strongest obligation on this shelf, and §13 reaches **network use** — which is
exactly how an MCP server is deployed. 🔴 **A client who installs this package into a hosted
tutoring or administration service takes on a source-provision duty over a network boundary, and
the artefact that arrived tells them nothing about it.** Two of three signals a reviewer would
check are silent: no licence file, no header. Only the manifest's `"license": "AGPL-3.0"` says so.

### Shape of the engagement

1. **Detect before install.** Gate A of `P17` catches it: SPDX `AGPL-3.0`, licence file absent.
2. **Decide at the network boundary, not the repository boundary.** If the service is reachable by
   users, §13 is live. 🔵 This is a **hosting-architecture** question, and it belongs with the
   client's counsel before an estimate, not after one.
3. **If the answer is no, the alternative is on the same shelf and is permissive.** The Moodle
   connector tier carries MIT rows with licence files present —
   [`verticals/solutions.md`](../verticals/solutions.md) and
   [`agents/top.md`](../agents/top.md) place them. 🔵 **`P7` already describes the permissive route
   onto Moodle**; this pattern is the gate that routes a client into it.
4. **If the answer is yes, vendor the grant the distribution dropped** — fetch the 34 523-byte text
   from the repository and ship it with the deployment, per `P17` step 4.

### Why it wins the room

🔴 **It is the only finding in this KB that can stop a delivery**, and it is three facts long: a
declared copyleft licence, a network-deployed server, and no notice in the artefact. 🟢 **Raising
it before the build is a credibility event; discovering it at a client's security review is the
opposite.**

**Pass 137, 2026-10-11.** p136's fourteen recipes retained. 🔴 **`P13` is rewritten again and
shrinks again** — from p136's three-to-four-week buy-and-adapt to **an adapter of about two weeks**,
because `ACTION BX` found the per-user mapping already implemented in a university-owned library and
the MCP half already implemented in an MIT one. 🆕 **`P15` is added because the EU deferral changed
which obligation is late**: Annex III high-risk moved to 2027-12-02 and **Article 50 did not move**.
🆕 **`P16` is added because Vietnam's education conformity duties are in force as of 2026-08-15** —
the first such regime anywhere, and this KB had no recipe for it.

🔵 **Every component named below was read this pass or in a prior pass with the licence established
from the payload.** Where a component was **not** read in source, the row says so.

## 🔁 `P13` rewritten — the adapter is an `OAuthStore` implementation *(fourth revision, p138)*

🟢 **`ACTION CE` discharged in source, and the one unknown in the third revision is now a published
interface.** p137 left the adapter as *"about two weeks"* of work whose shape was inferred. This pass
read `bruchris/canvas-lms-mcp`'s OAuth module and the shape is no longer inferred:

| p137's open question | p138's measurement |
|---|---|
| Does the broker implement the **RFC 8707** binding the LTI seam lacks? | 🟢 **Yes, by name.** `src/auth/oauth/authorization-server.ts` (**978 lines**) carries `normalizeResource()` — *"Canonical comparison for RFC 8707 `resource` values (§7)"* — plus **PKCE `S256`**, `registration_endpoint` with **dynamic client registration**, `/.well-known/oauth-authorization-server`, and a `canvas:write` scope. `resource-server.ts` (195 lines) publishes `/.well-known/oauth-protected-resource` (**RFC 9728**) and performs the **audience** check |
| Does wiring it require forking either library? | 🟢 **No.** `CanvasMCPServerConfig` takes `oauthStore?: OAuthStore`, documented *"Embedders may supply their own implementation"*. `OAuthStore` exposes `putClient`, `putGrant`, `putToken`, `putPendingAuthorization`, over a `Grant` carrying `CanvasConnection { refreshToken }` |
| Can a verified LTI `sub` be injected directly? | 🔴 **No — and this is the adapter's entire reason to exist.** The subject is established by `CanvasOAuthClient`, which redirects the user to Canvas. No path accepts an external assertion |

🔵 **So `P13` step 2 and step 3 collapse into one deliverable with a known signature**: implement
`OAuthStore`, seed it from the launch, hand it to the server constructor.

**Shape of the work (≈2 weeks, one engineer) — revised steps 2–3.**
1. Stand up `ltijs` v7 as the tool; take `sub`, `deployment_id` and the course context from the
   verified launch (the `LaunchContext` v7 hands the handler). *Unchanged.*
2. 🔁 **Implement `OAuthStore`** against the institution's own session store, keyed by the launch
   `sub`. Obtain the per-user Canvas refresh token in the shape `kstateome/lti-launch` proves
   (`/beginOauth` for that user → `storeToken(userId, refreshToken)`) and `putGrant` a `Grant`
   carrying it as `CanvasConnection { refreshToken }`.
   🔴 **Create the grant up front.** `store.ts` carries *"Update only, never create (QA S7, #356)"*
   on the Canvas-refresh path — a lazy upsert on first token call will not work.
3. 🔁 **Construct the server with `{ oauthStore, authProfile: 'oauth_brokered' }`.** The brokered flow
   then issues an audience-bound MCP token for the launching user **without the Canvas redirect**,
   because the grant is already present. 🟢 **No fork of `ltijs`, no fork of `canvas-lms-mcp`.**
4. Pseudonymise before anything leaves the boundary: `canvas-lms-mcp` ships
   `src/pseudonym/pseudonymizer.ts`. 🟢 **And it fails closed** — when `sharedAcrossCallers` is
   undeclared the factory treats the deployment as shared and **throws** rather than guess if the
   environment asks for reverse lookup. *Build on that default; do not switch it off.*
5. 🔴 **Acceptance tests that make the pattern honest** — three now, not one:
   - a valid MCP token for a *different* audience must be refused (*"Access token was not issued for
     this resource"*);
   - a token without the `canvas:write` scope must leave write tools **blocked**, which `http.ts`
     decides at `outcome.scopes.includes('canvas:write')`;
   - a pasted `X-Canvas-Token` must get a **`400`** under the brokered profile.
6. 🔴 **Pin the dependency by payload, not by identifier.** `canvas-lms-mcp` **2.2.0** on npm is
   clean (378 paths, `package/LICENSE` present, published **2026-10-10**) — but 9 of 21 packages on
   this shelf ship no licence text, so verify the one you pin. See `P17`.

🔴 **What still kills this build is unchanged:** an institution whose LMS is **not** Canvas. The
broker and the launch mapping are both Canvas-specific, and the Brightspace and Moodle connectors
hold credentials instead of brokering them. 🟡 **For Brightspace, `D2L_PASSWORDLESS=true` plus a
token-paste path is the stopgap** — a stopgap, not the pattern.

## 🆕 `P17` — The licence-payload gate: prove what you are about to redistribute *(new, p138 — Global)*

**The engagement.** Any engagement that ships open-source components to a client — so, effectively,
all of them. 🔴 **`T17` measured that 9 of 21 published education-connector packages carry no licence
text, 7 of them while declaring an SPDX identifier.** A studio that reads licences from repositories
and ships artefacts from registries is checking a different object from the one it delivers.

**Why this is a pattern and not a checklist item.** 🔵 **The defect is invisible to every tool a
studio normally uses.** `npm ls --json` reports the identifier from the manifest; so do licence
scanners that read `package.json`. Both report `MIT` for a package whose tarball contains no licence
file at all. The only way to see it is to enumerate the payload.

**The stack.**

| piece | component | licence | role |
|---|---|---|---|
| the probe | [`p138-npm-payload-licence`](code/p138-npm-payload-licence/README.md) — in this KB | — | 🟢 **Runs as-is.** Takes package names, emits one TSV row each: version, publish time, SPDX id, `files` field, path count, licence file. **sha1-verifies every tarball against the registry's own `shasum`** and refuses to report a row whose bytes do not match |
| licence family classification | `compose/code/lib/license_family.sh` — in this KB | — | classifies the grant text once found, so a payload licence can be checked against the declared identifier rather than merely counted |
| the gate | the probe's exit path, wired into CI | — | fail the build when a dependency the client will receive ships an identifier with no text |

**How it wires together.**
1. Resolve the dependency set you will actually ship (not the dev tree) to exact versions.
2. Run `scan_npm_payload.sh` over those names; keep the TSV as a **build artefact**, because it is
   the evidence, and it is dated and reproducible.
3. 🔴 **Fail on `spdx_id != ABSENT && licence_file == NONE`** — the declared-but-absent class. That is
   the one where the client is told an obligation exists and handed nothing to satisfy it.
4. 🟡 **Warn, do not fail, on `spdx_id == ABSENT && licence_file == NONE`.** Two live packages on this
   shelf are in that state with no `repository` field either (`@imazhar101/mcp-canvas-server`,
   `@n35da/brightspace-mcp`). 🔵 **Nothing to read, nobody to ask — the correct action is not to ship
   them, which is a sourcing decision rather than a build failure.**
5. 🟢 **Escalate copyleft rows to a block.** `moodle-mcp-server-aql` declares **AGPL-3.0** over 141
   paths with no text. A permissive row missing its notice is an attribution defect; a copyleft row
   missing its text is a conveyance defect, and for an AGPL component attached to a GPL platform
   (this KB's `P7` route) it is the one that reaches the client's own obligations.
6. 🟢 **When a row fails, the ask upstream is small and specific**: all nine defects measured are the
   repository being *better* than the distribution, so the fix is one `files` entry in `package.json`,
   not a licensing negotiation. Open that PR; it is a two-line change and it fixes it for everyone.

**Shape of the engagement.** 🔵 **Two days to wire, then free forever.** It is not a billable
workstream; it is the thing that keeps a licence column from being wrong in the one place it matters.

🔴 **What this pattern does NOT cover, stated so nobody over-trusts it.** It reads licence **files**
only, so a grant in a source-file header reads as `NONE` — p137's `pipwerks` correction proved that
case is real, which means the gate **over-reports** and every failure needs a header read before
anyone writes to an upstream. It covers **npm** only: PyPI, Maven and crates need the same probe
against their own payload formats, and some rows have no payload layer at all (`moodler-mcp` is not
on PyPI). 🔵 **Use it as a gate on what you ship, never as a licence verdict on a project.**

## 🔁 `P13` rewritten — sanctioned MCP access to an LMS with no new credential *(third revision, p137)*

**The engagement.** An institution wants agents to act inside its LMS *as the person who launched
them*, with no personal access token pasted anywhere and no password held by the tooling. 🔴 **p135
called this a 4–6-week build. p136 called it a 3–4-week buy-and-adapt. p137 measures it as an
adapter**, because three of the four pieces exist.

| piece | component | licence | status after this pass |
|---|---|---|---|
| terminate the launch | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) **v7.0.7** | 🟢 Apache-2.0 | 🟢 Verifies an LTI 1.3 launch correctly. 🔴 **v7 is a TypeScript rewrite: Node 24+, no session cookies (`localStorage` + postMessage storage), `Provider` constructed not `setup()`** — budget the migration if the client is on v5 |
| map launch subject → per-user grant | [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | 🔴 **LGPL-3.0**, Java/Spring | 🆕 **The pattern, proven in production code**: `ensureApiTokenPresent()` → `getRefreshToken(eid)` → `/beginOauth` for that user → `storeToken(userId, refreshToken)`. 🔴 **Port the pattern, not the file**: LGPL + Java against a Python/TS agent stack |
| issue the agent's own audience-bound token | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) `--auth-profile oauth_brokered` | 🟢 MIT | 🆕 **Already an OAuth 2.1 authorization + resource server**: RFC 9728 protected-resource metadata, audience check, `canvas:read` scope, revocation, Canvas refresh, **`400` to a pasted `X-Canvas-Token`** |
| generic IdP instead of Canvas | [`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) or [`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) | 🟢 Apache-2.0 | carried from p136: JWKS-verified `id_token`, refuses to issue with no subject claim, RFC 8707 resource binding |
| 🔴 **the bespoke part** | the LTI 1.3 → broker adapter | — | 🔴 **Still nothing maps a verified 1.3 `id_token` onto an RFC 8707-bound MCP token.** Proven in code, not assumed: `ltijs` v7 mints only `client_credentials` with the **tool's** client id as `sub` |

**Shape of the work (≈2 weeks, one engineer).**
1. Stand up `ltijs` v7 as the tool; take `sub`, `deployment_id` and the course context from the
   verified launch (the `LaunchContext` v7 hands the handler).
2. Persist a per-user upstream grant in the `OauthTokenService` shape — `get` / `store` / `update`
   keyed by the launch subject. 🔵 **This is the piece `lti-launch` proves is sufficient.**
3. Point `canvas-lms-mcp`'s `oauth_brokered` profile at that store, so the MCP access token it issues
   is bound to the same subject and carries its own audience.
4. Pseudonymise before anything leaves the boundary: `canvas-lms-mcp` ships
   `src/pseudonym/pseudonymizer.ts`.
5. 🔴 **Acceptance test that makes the pattern honest**: a request bearing a *valid* MCP token for a
   *different* audience must be refused. That string exists in the implementation — *"Access token
   was not issued for this resource"*.

🔴 **What still kills this build:** an institution whose LMS is **not** Canvas. `canvas-lms-mcp`'s
broker is Canvas-specific, `lti-launch` is Canvas-specific, and the Brightspace and Moodle
connectors on the shelf hold credentials instead of brokering them. 🟡 **For Brightspace,
`D2L_PASSWORDLESS=true` plus a token-paste path is the stopgap** — and it is a stopgap, not the
pattern.

## 🆕 `P15` — Ship the Article 50 obligation that did NOT move, while the high-risk clock runs *(new, p137 — EMEA)*

**The engagement.** A European institution or edtech vendor was told to be conformity-ready by
**2026-08-02**. 🔴 **That date moved to 2027-12-02 for Annex III** (education) under **Regulation
(EU) 2026/1744** (in force 2026-07-27). 🟢 **Article 50 transparency did not move: it applied from
2026-08-02**, with a grace period to **2026-12-02** for systems already on the market. So the
client's *late* obligation is the marking one, and the expensive one has fourteen months.

| step | component | licence | what it does |
|---|---|---|---|
| mark synthetic output | `compose/code/aiact-50-2-marking` | this KB | Article 50(2) marking surface, with tests |
| package the provenance | `compose/code/aiact-50-2-pack` | this KB | an XSD-validated marking pack |
| find what is already exposed | `compose/code/aiact-50-2-exposure`, `-spans` | this KB | which outputs and spans fall under the duty |
| disclose at the interaction boundary | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) v7 launch handler | 🟢 Apache-2.0 | the launch is where a learner meets the system, so it is where the disclosure belongs |
| keep the conformity file open | `intel/policy-matrix.tsv` | this KB | 🟡 Annex III duties by **2027-12-02**: a tracked file, not a sprint |

🔵 **Why this sells in October 2026 and not in 2027:** the deferral was granted because harmonised
standards and national authorities were not ready, so **the control set a client will be audited
against does not exist yet** — while the marking duty is already enforceable. 🟢 **Do the enforceable
half now and keep a dated register for the deferred half.** 🔴 **One conflict to disclose to a
client rather than hide**: one source dates the already-on-market grace to **2027-02-02** rather than
2026-12-02; treat 2026-12-02 as the planning date and say why.

## 🆕 `P16` — Conformity dossier for an education AI system under Vietnam's Decision 33 *(new, p137 — APAC)*

**The engagement.** A platform operating in Vietnam runs one of the **three education classes** that
Decision **33/2026/QD-TTg** made high-risk, **effective 2026-08-15**: self-study content generated
from uncontrolled sources; **testing, grading or ranking learners**; behaviour monitoring using
biometric data. Duties: conformity assessment, **registration in the National AI Database**, human
oversight, incident reporting.

| duty | how this KB's shelf discharges it | component | licence |
|---|---|---|---|
| **human oversight** on grading | 🟢 **Never let the agent be the grader**: draft-only, human commit | `compose/code/grading-draft-gate` + [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) read tools | this KB / 🟢 MIT |
| **bounded write surface** | 🟢 `EDUBASE_READONLY` + per-toolset selection + `destructiveHint` is the pattern to copy: a connector that can be *configured* to be unable to write | [`EduBase/MCP`](https://github.com/EduBase/MCP) | 🟢 MIT |
| 🔴 **no uncontrolled-source self-study content** | serve retrieval from an institution-controlled corpus only; offline-first stacks make the boundary physical | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (🟢 MIT) + [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) (🟢 Apache-2.0) | 🟢 permissive |
| **no biometric monitoring** | state it as a *design exclusion* in the dossier; the cheapest conformity argument is the capability you do not ship | — | — |
| **identity, so the oversight claim is auditable** | `P13`'s broker chain: a token bound to the launching person, not a shared key | `ltijs` v7 + `canvas-lms-mcp` + `lti-launch` pattern | 🟢/🟢/🔴 LGPL |
| **incident reporting** | one append-only log per tool call with the subject the broker established, not the one the caller claimed | this KB's `mcp-allowlist-gateway` notes | this KB |

🔴 **What this pattern cannot yet do, said plainly.** The decree's **transition date for systems
already running is contradictory across the two briefings this KB could reach** (2027-09-01 vs an
unspecified additional period from 2026-08-15), and **no Vietnamese-language read of the decree has
been done** (`ACTION CG`). 🔴 **There is also no Vietnamese-owned repository anywhere on this KB's
pages**, so every component above is foreign-owned — which is itself a procurement risk in a
jurisdiction that registers systems nationally. 🟡 **Scope a dossier, not a certification.**

---

**Pass 135, 2026-10-11.** p134's twelve recipes retained; 🔴 **`P13` is added and it is a
prerequisite for `P11`, not an alternative** — p135 read the source of all three agent bridges and
found that two accept the user's identity on trust, so the pattern this KB has been recommending as
its new default **ships an agent that will act on whatever subject the caller claims**. 🟢 **`P14`
is added** from the content and assessment layer the standards register finished this pass. Fourteen
recipes. Each names the actual repos, the licence posture of the result, how the pieces wire
together, and what it does not solve.

🔵 **Every licence stated in `P13` and `P14` was established by sha256 identity against canonical
SPDX texts** (`compose/code/p135-licence-sha-identity`), not from a GitHub badge — and two popular
components are flagged out of `P14` for exactly that reason.

**Pass 132, 2026-10-11.** p131's seven recipes retained; 🔴 **P2 is re-based on a real 39 444-star
stack instead of a greenfield build** and **P8 and P9 are added** from the SIS/portal tier found
this pass (see `README.md` → Pass 132). Nine recipes. Each names the actual repos, the licence
posture of the result, how the pieces wire together, and what it does not solve. Repos cited are
verified in `evidence/verified-repos.2026-10-11.tsv` and
`evidence/verified-repos.2026-10-11-p132.tsv`.

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

## P2 — Offline-first tutor for low-connectivity deployments *(re-based by p132: the slot is occupied, and that is good news)*

**For:** rural LATAM, Sub-Saharan Africa, South Asia; ministries and NGOs.
**Timeline:** 10–12 weeks.

**Stack**

| layer | component | licence |
|---|---|---|
| 🆕 **orchestration (start here)** | [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | **Apache-2.0** |
| education platform | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) *(NOMAD's education container)* | MIT |
| reference library | **Kiwix** *(NOMAD's Information Library — offline Wikipedia and books)* | GPL-3.0 family |
| local inference | **Ollama** *(NOMAD's AI Assistant; external OpenAI-compatible endpoint also supported)* | MIT |
| content pipeline | [`learningequality/studio`](https://github.com/learningequality/studio) | MIT |
| mastery state | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| interactive content | [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | MIT |
| single-machine pilot | [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) | 🟡 UNREAD |

🔴 **Re-based by p132. Do not build this stack from parts — it exists.** Earlier versions of this
pattern called the slot unclaimed and specified an integration of Kolibri + a local model from
scratch. [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
(**Apache-2.0, 39 444★**, 850 commits) already orchestrates exactly those pieces as Docker
containers: Kiwix for the library, **Kolibri for the education platform**, Ollama for the AI
assistant. It is the second-largest repo in this KB.

**Wiring, revised.** Stand up NOMAD first and confirm the three containers on the client's target
hardware — that is now a deployment task, not an integration project. Then add the two things NOMAD
does not do: **`tutor-mcp` for durable learner state** (BKT mastery, review scheduling,
misconceptions) persisted locally and reconciled on next sync, and **H5P activities** authored
through Kolibri Studio so the same content survives a later move to Moodle or Open edX. Pilot on a
single machine with the macOS port before committing to the Docker estate.

**Why this remains the strategically strongest pattern in the KB — more so now.** Permissive top to
bottom (Apache-2.0 orchestration over MIT components; **check Kiwix's GPL-3.0 terms if you intend to
modify it rather than run it**), and **data never leaves the device**, which discharges most of the
privacy obligation in US state law, the EU AI Act and Brazil's pending PL 2338 by construction
rather than by policy. 🟢 **The difference from the old version is commercial: the client is buying
weeks of deployment and curriculum work on a proven stack, not months of integration risk.** That
is an easier sale and a defensible one.

**Timeline, revised:** **5–7 weeks** (was 10–12), because the integration layer is no longer yours
to build.

**Result licence:** Apache-2.0 orchestration over MIT components; audit Kiwix if modified.

**Does not solve:** small-model quality is still the binding constraint — scope to one subject and
validate before widening. Still requires device-management capability the client may not have.
🔴 **And the opportunity gap is now geographic, not technical: nothing offline targets LATAM.**
The one curriculum-specific offline project found is Indian
([`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI)), so a Spanish- or
Portuguese-curriculum NOMAD deployment is unclaimed, permissively licensed, and now cheap.

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

## P6 — Learning-outcome evaluation harness *(the instrument exists; it is unshippable)*

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
| **pedagogical benchmark** | [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) (ETH Zurich, EMNLP 2025 oral) | 🔴 **none declared** — run/cite only |
| **failure-mode dataset** | [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) (Khan Academy) | 🔴 **bespoke eval-dataset licence** — run/cite only |

**Wiring.** 🔴 **p130 built this pattern on the claim that no benchmark exists. Two do** (T7), and
starting from them removes weeks of design — so this pattern is now *two layers*, and the licence
boundary between them is the whole point.

**Layer 1 — borrow the published task structure (do not ship it).** Run `mathtutorbench` against
the candidate tutor for open-ended *pedagogical* capability (scaffolding, hint quality, when to
withhold the answer), and use `Khan/tutoring-accuracy-dataset` as the known-failure-mode set for
maths tutoring. 🔴 **Neither may be redistributed inside a client deliverable**: `mathtutorbench`
declares no licence and its README names two different ones, Khan's is a bespoke 2 690-byte
"Evaluation Dataset License". **Run them in your own environment, report the scores, ship neither
the data nor a derived fixture set.** If the client needs a shippable suite, re-author the task
*shapes* against their own curriculum — the ideas are not the asset, the labelled data is.

**Layer 2 — build the outcome half, which genuinely does not exist.** Both benchmarks measure tutor
behaviour, not whether a student learned. BKT parameters from `OATutor` give a quantitative,
inspectable mastery estimate independent of the tutor's self-assessment; `tutor-mcp` logs every
decision with the mastery state that produced it; xAPI via `scorm-again` captures interaction
telemetry from existing courseware so a pre-intervention baseline exists; Oppia's lesson model
encodes misconceptions explicitly, giving labelled targets to measure against. Run a holdout: same
content, tutor on and off, compare mastery trajectories and retention at a fixed interval.

**Why it closes every other pattern.** The OECD's 2026 Outlook asks for **durable learning gains**;
US state mandates ask for evidence that high-stakes decisions were sound; EU Annex III will ask for
documented performance. One harness answers the pedagogical question and three regulatory ones.

**Does not solve:** it measures, it does not teach. It needs a holdout design the institution must
agree to — negotiate that at contract time, not at delivery. 🔴 **And the two borrowed benchmarks
are maths-only**: for any other subject, Layer 1 has no published instrument and the shapes must be
authored from scratch.

---

## P7 — Moodle agent on the permissive side of the GPL boundary *(the route p130 said did not exist)*

**For:** any client on Moodle — the most deployed LMS in the world — that wants an AI layer it can
own, without taking on GPL-3.0 reciprocity on its own code.
**Timeline:** 5–7 weeks.

**Stack**

| layer | component | licence | why this one |
|---|---|---|---|
| platform (untouched) | [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | Left entirely alone. **Nothing is forked and no plugin is written**, so no reciprocity is triggered. |
| connector | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** | Standalone MCP server against Moodle's **web-service API**. Verified MIT by two independent instruments. 🔴 **Quiet since 2026-02-22 and publishes no tags — pin a commit.** |
| assessment + gradebook | [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) | **MIT** | Exams, gradebooks, item analysis, with **writes off by default** — the right default for anything touching grades. Corporate holder, LTI path. |
| durable learner state | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | BKT mastery, review scheduling, misconception tracking, auditable pedagogical decisions. LMS-agnostic. |
| launch surface | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | **MIT** | LTI 1.3 launch with signed identity and grade passback, so the UX lives inside Moodle while the code lives outside it. |
| build velocity | [`SaadRahman01/moodle-mcp`](https://github.com/SaadRahman01/moodle-mcp) + [`claude-moodle-dev`](https://github.com/SaadRahman01/claude-moodle-dev) | **MIT** | Live moodledev.io docs, Hooks API, XMLDB and Jira as agent tools; plus plugin-building skills if a plugin ever does become necessary. |

**Wiring.** Moodle's web-service API is the whole trick: enable the web-service functions the use
case needs, issue a scoped token per service, and point the MIT MCP servers at it. The agent gets
courses, assignments, submissions and grades as tools; `tutor-mcp` holds the mastery state between
turns so the tutor is not re-deriving the learner from the transcript each time; `ictexam-mcp`
handles anything assessment-shaped with writes explicitly enabled only where a human approves.
Learner-facing UX enters through **LTI 1.3**, not a plugin. **Every line Globant writes stays MIT or
client-proprietary**; the only GPL-3.0 artefact in the deployment is Moodle itself, unmodified.

**Why this pattern exists.** p130's pages told a reader that Moodle had *no permissively licensed
MCP route* and that the options were a GPL-3.0 in-tree plugin or an unlicensed web-service plugin.
That was false in both directions, and the cost of the error is the whole engagement shape: it
pushes a client toward writing a GPL plugin when a clean-room MIT side-car was available.

**Checks before proposing it.** Confirm the client's Moodle has web services enabled and tokens
issuable — some managed hosts disable them. Pin commits (`peancor` has no tags). Keep grade writes
behind human approval: automated grading is **Annex III high-risk** in the EU from 2027-12-02 and is
restricted by several US state rules now (`intel/policy-matrix.tsv`).

**Does not solve:** deep in-page Moodle UX. If the client insists the AI live inside a Moodle
activity rather than an LTI launch, a GPL-3.0 plugin becomes unavoidable — and the reciprocity is on
the plugin, not the client's other code.

---

## P8 — Sanctioned connector for a national school platform *(new, p132 — EMEA's clearest unmet need)*

**For:** the vendor or ministry behind a national K-12 platform — **Librus** (Poland), **EduPage**
(Slovakia/Czechia), **Pronote** (France), **IServ** (Germany) — or a large school group running one.
**Timeline:** 8–10 weeks.

🔵 **Why this pattern exists.** p132 found that all four platforms already have open-source MCP
connectors, mostly MIT, written by pupils and parents — and **every one is an unofficial
password-scraper with no DPA, no audit trail, and (for `librus-mcp`) no 2FA support**. The vendors
have no agent story at all. So the work is not *"can an agent reach this platform"* — that is proven
and published — it is *"make it legitimate"*.

**Stack**

| layer | component | licence | role |
|---|---|---|---|
| API surface map | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) · [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) · [`HAL-XP/mcp-pronotes`](https://github.com/HAL-XP/mcp-pronotes) · [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) | MIT *(🔴 `librus-mcp`: MIT 2.x only — `legacy_reference/` is **GPL-3.0-only**)* | 🟢 **read as documentation**; keep the endpoint map, discard the auth |
| identity | [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) as the reference shape — Okta OIDC/SAML, OAuth 2.0, **SCIM** | 🔴 unlicensed — **pattern only, do not vendor the code** | replaces the stored pupil password |
| audit | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) FERPA-logging approach | **Apache-2.0** (payload-read) | per-access logging a regulator can read |
| policy gate | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) for auditable pedagogical decisions | MIT | keeps inference out of high-stakes calls |
| launch surface | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) where the platform speaks LTI | MIT | avoids touching platform source |

**Wiring.** Lift the endpoint map from the existing MIT connectors — that is the weeks of
undocumented-API archaeology you do not repeat. Replace the credential model wholesale: the agent
authenticates through the platform's own SSO with scoped, revocable tokens provisioned by SCIM, and
**never holds a pupil credential**. Every read is logged with actor, subject, field and purpose.
Write operations stay off by default; grade and attendance writes require a human confirmation step.
Ship it as a vendor-sanctioned integration, not a scraper.

🔴 **The compliance work is the deliverable, not overhead.** For all four platforms the subjects are
children, so: a **DPA with the vendor**, a lawful-basis analysis, a **DPIA**, data-minimised scopes
(a timetable agent does not need disciplinary records), and retention limits. Annex III of the AI
Act is not triggered by reading a timetable — but it *is* triggered the moment the same connector
feeds grading or admissions, which is the second phase every client will ask for. **Architect the
boundary now** (`P4`).

**Result licence:** your own code; MIT inputs read as reference only. 🔴 **Do not vendor
`sis-demo`** (unlicensed) or `librus-mcp`'s `legacy_reference/` (GPL-3.0-only).

**Does not solve:** it needs the platform vendor at the table. Without their cooperation this is
still a scraper, and should not be built. 🟢 **The pitch to the vendor is that pupils are already
scraping them with stored passwords and no 2FA** — a sanctioned surface is a security improvement
for the vendor, not just a feature.

---

## P9 — Administrative automation on an open-source system of record *(new, p132 — the real hole)*

**For:** institutions running, or willing to adopt, an open-source SIS/ERP — mid-size universities,
school groups, ministries. **Timeline:** 10–12 weeks.

🔵 **Why this is the sharpest opportunity in the KB after p132.** The SIS *agent* gap is closed —
there are 21 connectors — but **every single one targets a proprietary or institution-hosted
portal.** The open-source systems of record have **zero** agent coverage between them, while
administrative automation remains the most-cited adoption driver. **The connector effort has gone to
the platforms a studio cannot fork and avoided the ones it can.**

**Stack**

| layer | component | licence | note |
|---|---|---|---|
| system of record | [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | 🟢 **the only permissive SIS** — the one base a client can own as a closed derivative |
| — or — | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **LGPL-3.0** (payload-read) | broadest functional coverage; **linking is fine**, modifying the module carries reciprocity |
| — or — | [`frappe/education`](https://github.com/frappe/education) | 🔴 **read `LICENSE` first** (API says `NOASSERTION`) | pick when the client already runs ERPNext |
| agent scaffold | [`sandraschi/classroom-mcp`](https://github.com/sandraschi/classroom-mcp) | **MIT** | 🟢 standalone, ~42 tools, teaching-agent roles — **the reference design to read** (1★; do not depend on it) |
| optimiser | [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | conflict-free timetabling under India's NEP 2020 — the only real optimiser found |
| audit | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | **Apache-2.0** | FERPA-style per-access logging |
| identity | SCIM/OIDC per [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) | 🔴 unlicensed — pattern only | institutional SSO, scoped tokens |

**Wiring.** Pick the system of record on the licence question first, because it is irreversible:
**`academico` (MIT)** if the client wants to own a closed product, **`openeducat_erp` (LGPL-3.0)** if
they want coverage and will call it from outside without modifying it. Put an MCP server in front of
it modelled on `classroom-mcp`'s tool taxonomy — students, enrolment, assignments, courseware,
progress — reading through the platform's own permission model rather than around it. Attach the
timetable optimiser as a *tool the agent calls*, not as something the model does: scheduling is a
constraint-satisfaction problem and an LLM is the wrong instrument for it. Wrap everything in
per-access logging and SCIM-provisioned scoped tokens from day one.

🟢 **The commercial shape is better than the tutoring engagements.** Timetabling, enrolment and fee
chasing have a measurable baseline (hours of registrar time, scheduling conflicts per term, days to
produce a timetable), so the business case writes itself — unlike tutoring, where the client is
buying an unproven learning-outcome claim (`P6`). And the regulatory exposure is far lower: **a
timetable is not Annex III.**

**Result licence:** MIT throughout if built on `academico`; LGPL-3.0 linking obligations if on
`openeducat_erp` and the module is modified.

**Does not solve:** 🔴 **the client has to be willing to run an open-source SIS**, and most
institutions of record run a proprietary one — which is why the 21 connectors target those instead.
Realistically this lands at mid-size institutions, new campuses and ministry programmes rather than
at a university replacing Banner or SITS. 🔴 **Both scaffold rows are 1★** — read them as reference
designs and expect to own the code.

---

## P10 — Grade and workload passback for a LATAM national academic system *(new, p133 — the first pattern this KB can ground in LATAM rows)*

**For:** Brazilian federal universities (**SIGAA**) and federal institutes (**SUAP**), Argentine
universities on the **SIU-Guaraní** consortium stack. **Timeline:** 6–8 weeks for the first faculty,
plus 3–4 weeks per additional campus. 🟢 **The shortest, lowest-risk engagement in this file.**

🔵 **Why this pattern exists now and could not be written before.** For four passes this KB reported
"no LATAM-origin supply" and recommended LATAM work on market share alone. `ACTION BE` refuted that
with **12 addresses** — and three of them are doing the *same unglamorous job in two countries*:
**moving grades and workload into a national system of record that a human is currently retyping.**
🟢 **That is not a guess about demand; it is three independent people having already built it.**

🔴 **And the demand number is on the same page.** IESALC's 200-institution survey puts
**administration at 34.1%** adoption — second-lowest of four areas — while the Digital Education
Council's LATAM 2026 survey finds **50% of students want AI-assisted feedback and only 19% of faculty
give it** (`intel/market.md` → LATAM). **The bottleneck is the teacher's data-entry time, and that is
exactly what this pattern removes.**

**Stack**

| layer | component | licence | note |
|---|---|---|---|
| reference: grade passback | [`filipecalegario/auto-sigaa`](https://github.com/filipecalegario/auto-sigaa) | **MIT** | 🟢 **start here.** Pushes a spreadsheet of grades into SIGAA. MIT, 9★ — the one forkable staff-facing row |
| reference: workload report | [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) | 🔴 **AGPL-3.0** | **Read, do not fork.** Org-owned, drafts a lecturer's **RIT** from SUAP via CLI **and** MCP — the closest thing to a product in this tier. Its *architecture* is the deliverable here, not its code |
| reference: Argentina | [`eugeborzone/Auto_Grade_Guarani`](https://github.com/eugeborzone/Auto_Grade_Guarani) | 🔴 **unlicensed** | Pattern only. Proves the identical need on SIU-Guaraní |
| API surface: SUAP | [`joojdev/academic-tracker-mcp`](https://github.com/joojdev/academic-tracker-mcp) (**MIT**) + [`frjunioalves/suap-mcp`](https://github.com/frjunioalves/suap-mcp) (🔴 unlicensed) | mixed | 🟢 **Two independent MCP implementations of the same SUAP surface** — cross-read them to separate the real API from one author's assumptions |
| API surface: SIGAA | [`Agso-o/sigaa-calendar`](https://github.com/Agso-o/sigaa-calendar) (🟡 GPL-3.0), [`RubsNeto/SigaaUI`](https://github.com/RubsNeto/SigaaUI) (**MIT**), [`trindadetiago/sigaa-caiu`](https://github.com/trindadetiago/sigaa-caiu) (**MIT**) | mixed | The published map of SIGAA's undocumented screens. 🔴 Read `sigaa-calendar` for its *surface*, not its code — GPL-3.0 |
| agent scaffold | [`sandraschi/classroom-mcp`](https://github.com/sandraschi/classroom-mcp) | **MIT** | tool taxonomy for courses/assignments/scores (1★ — reference design) |
| audit | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | **Apache-2.0** | per-access logging; the LGPD analogue of its FERPA model |
| the counterparty | [`SIU-Toba`](https://github.com/SIU-Toba) (Argentina) | 🔴 unlicensed, dormant since 2017 | 🟢 **The SIS consortium is itself on GitHub** — the only named sanctioned-integration counterparty in this KB (`P8`) |

**Wiring.** Three steps, in this order, and the order is the whole point.

1. **Build the importer, not the agent.** A deterministic job that takes an instructor's grade
   spreadsheet, validates it against the course roster pulled from SUAP/SIGAA, and writes it back
   through the institution's own authenticated session. **No model in this path.** `auto-sigaa` is
   the worked example; fork it. 🔵 **Grade entry is a correctness problem, not a language problem —
   an LLM in the write path converts a 2-hour chore into an unauditable liability.**
2. **Put the LLM only where the text is.** Two jobs, both safe: (a) *reconciliation* — explain in
   Portuguese or Spanish why 3 of 180 rows failed validation, which name matched no enrolment, which
   grade is out of range; (b) *narrative drafting* — the prose sections of a workload report
   (`expeditto`'s RIT), always **as a draft the lecturer edits and submits.** 🔴 **Never
   auto-submit:** a drafted report a human signs is administrative support; an auto-filed one is an
   automated decision about staff performance.
3. **Then, and only then, add the MCP surface.** Once the importer is correct and logged, expose it
   as MCP tools modelled on `academic-tracker-mcp` so the instructor can ask *"how many of my
   students are missing a grade for unit 2"*. 🟢 **This ordering is what makes the engagement
   financeable: step 1 has a measurable baseline (hours per term per lecturer, error rate,
   days-late on grade submission) before any AI spend is defended.**

**Credentials — the one blocker, and LATAM has a better answer than EMEA.** Every reference row above
logs in as its author. 🔴 **Do not ship that.** But unlike Librus or Pronote, **the counterparty here
is reachable**: SIGAA and SUAP are *public-sector* systems (SIG/UFRN-derived and IFRN-derived
respectively, both federal), and SIU-Guaraní is published by a **university consortium that already
has a GitHub org**. 🟢 **A federal institute can authorise its own integration — which is precisely
what pattern `P8` cannot get from a private EMEA vendor.** Get an institutional service account and
a DPA under **LGPD** (Brazil) or **Ley 25.326** (Argentina) before the first write.

**Result licence:** MIT throughout, if built from `auto-sigaa` + `academic-tracker-mcp` +
`classroom-mcp` and `expeditto`/`sigaa-calendar` are read rather than copied. 🔴 **Track that
boundary in the repo:** the two most useful references are **AGPL-3.0** and **GPL-3.0**, and this
pattern's whole commercial value depends on not importing them.

**Does not solve:** 🔴 **this is administrative plumbing, not pedagogy** — it will not satisfy a
client who came for a tutor (`P1`). 🔴 **It is per-platform**, so a Brazilian federal university
(SIGAA) and a federal institute (SUAP) are two integrations, not one. 🟡 **And every reference row is
0–20★ with a bus factor of one** — budget to own the code, and read `P8` before promising the
institution a sanctioned path.

---

## P11 — The sanctioned-integration agent: MCP over LTI AGS, OneRoster and an LRS *(new, p134 — and it is the pattern the other ten have been working around)*

🔴 **Every connector-based pattern in this file carries the same unpriced risk**, and `P8` names it:
the open-source connectors authenticate as a student with a stored portal password against a
platform that never sanctioned it. 🟢 **p134 found that the sanctioned path is not a research
project — it is a mature, permissive, institution-owned standards stack — and that the one missing
piece is the agent binding.** This pattern is that binding, and every dependency in it is already
chosen and licence-verified.

**Use it when:** the client runs **Canvas, Moodle, Blackboard, Open edX, Sakai, D2L or ILIAS** (i.e.
anything LTI-compliant), AND the engagement has to survive a security review, a procurement process,
or a data-protection assessment. 🟢 **Which is to say: almost every real engagement, as opposed to
every demo.**

### The stack, with licences this pass verified by payload read

| layer | component | licence | why this one |
|---|---|---|---|
| **launch + identity** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** (11 361 B, holder named) | 373★, pushed 2026-10-06. OIDC launch, JWKS, Deep Linking, **AGS**, NRPS. The tool is **invited in** by a client ID the institution issues and can revoke — no stored password anywhere in the design |
| *(Python alternative)* | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** (1 070 B) | 138★. 🔴 **Dormant since 2024-08-18 — budget maintenance for it, or put the LTI edge in Node and the agent in Python** |
| **PoC scaffold** | [`paurushrai/lti-1.3-node-nextjs-starter`](https://github.com/paurushrai/lti-1.3-node-nextjs-starter) | **MIT** | A template *over* `ltijs` with Dynamic Registration and PostgreSQL — days, not weeks, to a first launch |
| **grade write-back** | **LTI AGS**, via `ltijs` | — | Writes to the LMS gradebook **through the platform's own service**, which is the sanctioned equivalent of what the LATAM teacher-facing rows do by scraping (`P10`) |
| **rostering** | [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 🟢 **0BSD** (711 B) | TypeScript OneRoster 1.2 SDK. **0BSD drops even attribution** — the least encumbered dependency in this KB |
| **rostering (US K-12)** | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** (10 173 B) | Serves OneRoster 1.2 from an **Ed-Fi ODS** — the standards body's own bridge, pushed 2026-10-09 |
| 🟢 **conformance proof** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 **Apache-2.0** | **Run these and hand the client the output.** The only test suite in this KB that proves an integration correct rather than asserting it |
| **learner state / audit** | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | 🔴 **The load-bearing and least-maintained link: 15★, last push 2025-08-29.** An MCP server that records and retrieves learning activity via an **xAPI LRS**. **Expect to fork and own it** |
| **analytics surface** | [`openfun/warren`](https://github.com/openfun/warren) | **MIT** | xAPI learning-analytics dashboards from **France Université Numérique**, pushed 2026-10-11 |
| **enterprise auth** | [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) (pattern only) | 🔴 **no licence — read, do not fork** | The worked example of **Okta OIDC/SAML + SCIM** provisioning. 🟢 Second instance now exists against a real institution: [`P1ckle3/blackboard-mcp`](https://github.com/P1ckle3/blackboard-mcp) (UQ, Okta SSO, 🔴 unlicensed) |
| **access logging** | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) (pattern only) | 🟢 Apache-2.0 (notice-block form) | **FERPA access logging as a first-class feature** — the audit-trail design to copy |
| **pedagogical state** | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | BKT mastery, review scheduling, auditable pedagogical decisions, LMS-agnostic — so it sits behind the LTI edge rather than inside the LMS |

### How it wires together

1. **The LMS launches the tool over LTI 1.3.** `ltijs` validates the OIDC handshake and the platform
   JWT. 🟢 **The agent now knows who the learner is, in which course, with what role — signed by the
   platform, with no credential of the learner's held anywhere.**
2. **Roster context comes from OneRoster**, not from scraping a class list: `oneroster-ts` against
   the institution's rostering endpoint, or `edfi-oneroster` over an Ed-Fi ODS in US K-12.
3. **The agent runs** — any framework; `tutor-mcp` supplies mastery and scheduling state so the
   pedagogy is auditable rather than an LLM's opinion.
4. **Learner activity is written to an LRS as xAPI statements** through `learnmcp-xapi`. 🟢 **This is
   the step that makes the whole thing defensible:** every interaction lands in a store the
   institution owns, in a standard format, queryable for an audit or an impact study.
5. **Grades go back over AGS**, into the LMS gradebook, through the platform's own service.
6. **`warren` renders the analytics** over the same xAPI data — so the evaluation harness (`P6`) and
   the product read from one store.
7. **Access is governed by the institution's IdP** (Okta OIDC/SAML + SCIM per `sis-demo`) and
   **every record access is logged** (per `mcp-student-records`).

### Shape of the engagement

**8–12 weeks to a defensible pilot in one course**, on the assumption that the client's LMS admin
can register an LTI tool — 🔴 **confirm that in week one; it is the only hard external dependency,
and in a large institution it is a ticket, not a conversation.**

- **Weeks 1–2** — LTI registration; `ltijs` launch working end to end; rostering endpoint identified
  and the **Google conformance tests run against it**.
- **Weeks 3–5** — LRS stood up; fork and harden `learnmcp-xapi` (🔴 **assume this is real work: 15
  stars, 14 months quiet**); xAPI statement vocabulary agreed with the client's institutional
  research team.
- **Weeks 6–8** — the agent itself, with `tutor-mcp` for mastery state; AGS grade passback;
  human-in-the-loop review on every write.
- **Weeks 9–12** — IdP integration and SCIM; FERPA/GDPR access logging; `warren` dashboards; the
  conformance and audit artefacts packaged as deliverables.

### Why it wins the room

🟢 **The security review is the deliverable, not the obstacle.** Against any of the 43 portal
connectors, the honest answer to *"where does the student's password live?"* is "in our config".
Here the answer is **"we never have one"** — and there is a conformance-test output, an audit log and
a standards-based record store to hand over with it. 🟢 **And it is the only pattern in this file
whose dependencies are owned by the Ed-Fi Alliance, Google, the US DoD and a French public
operator**, which is a different procurement conversation from one about student projects.

🔴 **What to tell the client honestly.** The standards layer is mature; **the agent binding is one
unmaintained 15-star repository and you are adopting it.** `learnmcp-xapi` and `pylti1.3` are the
two components to price as *owned*, not *consumed*. 🔴 **And no repository in this stack has been
code-audited by this KB** — the licences are payload-verified and the activity is metadata-verified,
but *"uses the public REST API"* is read from descriptions, not source. **Read the code in week one.**

🔴 **Where this pattern does not apply, and say so early.** The LATAM national systems
(SIGAA, SUAP, SIU-Guaraní, SAES, Q-Acadêmico) and the EMEA K-12 platforms (Librus, EduPage, Pronote,
IServ) **publish no LTI, no OneRoster and no Ed-Fi.** There is no sanctioned door to walk through,
which is why that supply is scrapers. For those clients the route is **`P8`** (negotiate with the
vendor) or **`P10`** (work inside the institution's own mandate), not this.

## P12 — Assessment and feedback agent built for the 2027 clocks *(new, p134)*

🟢 **Why this pattern exists separately from `P1`:** assessment and feedback is the **fastest-growing
segment of this market (44.36% CAGR,** `intel/market.md`**)** and simultaneously **the most regulated
activity in every region this KB covers.** Those two facts are usually treated as a tension. 🟢
**They are the offer:** build the fast-growing thing in the way the compliance clocks will require,
and the compliance work becomes the differentiator instead of the tax.

**The three clocks, which are closer than they look:**

| jurisdiction | obligation | date |
|---|---|---|
| **EU** | education uses in **Annex III high-risk**; 🔴 **emotion inference in education prohibited outright since 2025-02-02** | 🔴 **2027-12-02** |
| **Oklahoma** | every district to adopt a written AI policy | 🔴 **before the 2027-28 school year** |
| **Maryland** | an **AI coordinator** per school system; AI literacy in state standards | 🔴 **by June 2027** |

**The build:** `P11`'s stack, with the agent specialised to **grading open-ended responses and
generating feedback**, plus:

- 🔴 **No affect, emotion or behavioural inference, at all.** Prohibited in EU education settings
  since 2025-02-02 and the single fastest way to make the deliverable unshippable. This rules out
  three of the four permissive proctoring rows in `agents/top.md` by construction.
- 🟢 **Human-in-the-loop on every grade that reaches a student**, logged, with the model's rationale
  retained. AGS write-back happens **after** review, not instead of it.
- 🟢 **Every decision written to the LRS as xAPI** — which is what turns "we had oversight" into
  evidence that oversight happened.
- 🟢 **Evaluate against a real benchmark and say which:** [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench)
  for pedagogical quality, [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset)
  for known maths-tutoring failure modes. 🔴 **Both are ungranted — run them, cite them, ship
  neither** (`P6`, `T7`).
- 🟢 **Exam/item plumbing, if the client needs it:** [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp)
  (MIT, corporate holder, **writes off by default**, LTI path) is the most procurement-friendly
  assessment connector on the shelf.

**The counterparties p134 adds, which make this sellable rather than speculative:**

- 🟢 **UNIwise ApS (Denmark)** — a Nordic/UK digital-assessment vendor publishing its **own MIT
  integration packages** covering **assessor allocation and grade passback**
  ([`AlexMeiling/wiseflow-api-integration-packages`](https://github.com/AlexMeiling/wiseflow-api-integration-packages),
  licence payload-read, holder *"UNIwise ApS"*). **A vendor that already ships a permissive
  integration path is the shortest route to a sanctioned assessment engagement in EMEA.**
- 🟢 **Jisc's AI marking and feedback pilots across 38 UK colleges and universities** — a named
  sector programme already running, and the obvious place to look for outcome evidence rather than
  vendor claims.
- 🟡 **Open Assessment Technologies (Luxembourg)**, vendor of **TAO**, publishing
  [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import) — 🟡 GPL-2.0, so read
  before forking.

🔵 **The demand signal to open the conversation with:** UK university student AI use went from
**66% to 92% in one year**, and in LATAM **87% of universities use AI while 26% have a strategy and
9% evaluate it.** 🟢 **Nobody is arguing about whether students use AI. The unanswered question is
whether the institution can show what its own AI did** — and that is this pattern.

## 🟢 P13 — The identity broker in front of a standards MCP server *(new, p135; **rewritten by p136 from BUILD to BUY-AND-ADAPT**)*

### 🆕 p136 — the broker is a product now, and only the adapter is yours

**Pass 136.** p135 wrote this pattern around **"your ~300 lines"** because no row in this KB
terminated a verified identity before calling an MCP server. 🔴 **`ACTION BS` probed the
professional register and found six repositories that do**, so the middle row of the stack table
below is **no longer bespoke**:

| layer | p135 said | 🆕 p136 says |
|---|---|---|
| Identity termination (LTI) | `Cvmcosta/ltijs`, Apache-2.0 | 🟢 unchanged |
| **Broker** | 🔴 **"your ~300 lines"** | 🟢 **BUY**: [`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) (**Apache-2.0**, Go, MCP auth spec **2025-11-25**, RFC 9728 + 8707 + 9068, JWKS-verified upstream OIDC, PKCE, DPoP, token exchange, **56 test files**) — or [`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) (**Apache-2.0**, 60★) to front an existing MCP server *"without code modification"* |
| **LTI→broker adapter** | *(not separated out)* | 🔴 **BUILD — and this is the only bespoke code on the path.** Map the verified launch's `sub`, roles, `deployment_id`, course context and AGS endpoints onto the broker's subject, audience and scopes |
| Agent surface | `bb-mcp` / `learnmcp-xapi`, MIT | 🟢 unchanged — and behind the gateway they need no edits |

🔵 **Why the broker existed where nobody looked.** It was built by the **cloud-infrastructure**
community for MCP generally, not by edtech: querying `mcp oauth resource server` finds it,
`ai education identity` does not. 🟢 **That is clause 5 of `agents/top.md`'s vocabulary rule paying
for itself**, and it is the reason this pattern's price drops by weeks.

🔴 **What is NOT bought, stated precisely.** None of the six terminates an **LTI 1.3 launch**; they
terminate OIDC, OAuth and managed IdPs. LTI's launch is OIDC-shaped and `ltijs` already verifies it
correctly, so the adapter is a mapping rather than a protocol implementation — but it is **yours**,
it is where the security review will look, and `topic:lti` + `topic:mcp` across all of GitHub is
**two repositories, neither implementing LTI**.

🟢 **Revised engagement shape: 3–4 weeks, not 4–6.** Week 1: LTI developer key and a verified
launch (unchanged). Week 2: stand up `mcp-oauth` or the gateway against the institution's IdP —
configuration, not code. Week 3: the adapter, with the same two tests p135 specified (an unasserted
subject is refused; `role:admin` cannot be self-granted) **plus one the bought component makes
cheap** — that a token minted for course A cannot be replayed against course B, which is RFC 8707
resource binding and already implemented. Week 4: the security review.

🔵 **One caution that comes with buying.** `giantswarm/mcp-oauth` is **14★**. The capability is
excellent and the bus factor is not; `atrawog/mcp-oauth-gateway` (60★) and
[`NapthaAI/http-oauth-mcp-server`](https://github.com/NapthaAI/http-oauth-mcp-server) (108★, MIT)
are the alternates, and a client's security team will ask about exactly this. **Vendor-in the
component, pin the version, and read the 56 tests — they are the strongest evidence any of the three
offers.**

---

**Why this pattern exists** *(p135's original, kept because the mechanism is unchanged)*. p134 established that the sanctioned path (P11) removes the credential
blocker, and that is correct: a tool launched over LTI holds no user credential. 🔴 **p135 read the
source of all three agent bridges and found that two of them accept the user's identity on trust**
(`intel/trends.md` → `T13`, `agents/top.md` → `ACTION BL`). **P11 as written ships an MCP server
that will act on whatever subject the caller claims.** This pattern is the missing component, and it
is small.

### The problem, in one table

| component | what it proves about the user |
|---|---|
| `Cvmcosta/ltijs` (Apache-2.0, 373★) | 🟢 **Verified.** Platform-signed JWT, signature checked against platform keys, nonce tracked |
| `nitsuah/bb-mcp` (MIT) | 🔴 **Nothing.** `caller_identity` is a tool argument the client fills in; the README states it is *"trusted at face value"*, and `role: "admin"` bypasses the course-entitlement gate |
| `DavidLMS/learnmcp-xapi` (MIT) | 🔴 **Nothing.** The actor is `ACTOR_UUID` from the environment — one process per student |

🔵 **So the verification exists at the LMS boundary and is thrown away before the agent acts.** The
broker's whole job is to carry it across.

### The stack

| role | component | licence |
|---|---|---|
| Identity termination | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) — LTI 1.3 launch, OIDC, signature verification, nonce replay protection | 🟢 Apache-2.0 *(hash-verified, p135)* |
| Broker | ~~**your ~300 lines.**~~ 🆕 **p136: BUY IT.** [`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) (Apache-2.0) or [`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) (Apache-2.0). What stays yours is the **LTI→broker adapter**: map the launch's verified claims onto the broker's subject, audience and scopes | 🟢 **Apache-2.0** *(payload-read, p136)* |
| Agent surface | [`nitsuah/bb-mcp`](https://github.com/nitsuah/bb-mcp) or [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi), called **only** by the broker | 🟢 MIT *(both hash-verified)* |
| Record | the institution's LRS (xAPI) or the platform's own API | — |
| Audit | `bb-mcp`'s structured access log, SHA-256-hashed subjects, kept | 🟢 MIT |

### How it wires together

1. The user launches the tool from the LMS. `ltijs` validates the `id_token` signature against the
   platform's JWKS, checks the nonce, and yields **claims the institution signed**: subject, roles,
   context (course), and the AGS/NRPS endpoints available for this launch.
2. The broker mints a **short-lived token** carrying only those claims, scoped to that course.
3. Every MCP call goes through the broker, which fills `caller_identity` **from the verified claims,
   never from the agent**. The MCP server's own RBAC, FERPA gate and course-entitlement check then
   operate on a subject that was actually proven.
4. 🔴 **Network-close the MCP server.** `bb-mcp` fails closed without `MCP_API_KEY` and TLS on a
   non-loopback host — keep that, and additionally make the broker the only route to it. Its
   `MCP_API_KEY` authenticates *the client*, not the user; the broker supplies the user.
5. Writes (grade passback) go over **LTI AGS** where available, so the write is authorised by the
   same launch that authenticated the user.

### Why it wins the room

🟢 **It is the answer to the only question that stops these projects in security review:** *"what
stops the agent claiming to be someone else?"* With P11 alone the honest answer is "nothing, we
trust the client application" — which is `bb-mcp`'s documented design and a finding in any audit.
With P13 the answer is **"the LMS signed it, we verified the signature, and the agent never supplies
the subject."**

🔴 **State the FERPA/GDPR consequence plainly to the buyer.** `bb-mcp` gates its restricted tools on
a `ferpa_authorized: true` flag that **the calling application asserts**. Unbrokered, that flag is
the agent asserting its own authorisation to see protected education records. Brokered, it is
derived from a verified role. **That is the difference between a control and a comment.**

### Shape of the engagement

**4–6 weeks.** Week 1: LTI developer key in the client's LMS and a working verified launch.
Weeks 2–3: the broker, with tests that prove an unasserted subject is refused and that `role:admin`
cannot be self-granted. Weeks 4–5: wire one MCP server behind it, one read tool and one write tool.
Week 6: the security review the client was always going to run.

🔵 **What it does not solve.** It does not make `learnmcp-xapi` multi-tenant — that repo is one
process per `ACTOR_UUID` and last saw a commit on **2025-08-29**, so budget a fork. It does not give
you Caliper analytics, which have **no open-source client at all**. And it does not remove the need
for P6: brokered identity makes the audit trail trustworthy, not the pedagogy effective.

## 🟢 P14 — Standards-native content and assessment pipeline *(new, p135)*

**For the client that asks for AI-generated course content or assessment items and needs them to
work in the LMS it already owns.** p135's register found that the content and assessment standards
carry far more code than this KB had recorded, and all the pieces below are permissive **except
where flagged**.

| role | component | licence |
|---|---|---|
| Item authoring | [`metyatech/markdown-to-qti`](https://github.com/metyatech/markdown-to-qti) — Markdown → QTI 3.0 XML; 🟢 carries the topic `agent-tool` | 🟢 MIT |
| Item rendering/preview | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) (30★) or [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) (TypeScript, pushed 2026-10-09) | 🟢 MIT |
| Assessment engine | [`numbas/Numbas`](https://github.com/numbas/Numbas) — **Newcastle University**, strongest for mathematics, SCORM-packageable | 🟢 Apache-2.0 |
| Course packaging | [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) (630★) — responsive, accessible, multi-language, emits SCORM **and** xAPI | 🔴 **GPL-3.0 — run it, do not link it** |
| Runtime/tracking | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (354★) — SCORM 1.2/2004, **offline-first** | 🟢 MIT |
| Legacy migration | [`Citolab/qti-convert`](https://github.com/Citolab/qti-convert) — QTI 2 → QTI 3 | 🔴 **GPL-3.0** (holder: **Stichting Cito**) |
| Conformance | [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) for badges/CLR; `googleworkspace/oneroster-integration-conformance-tests` for rostering | 🟢 Apache-2.0 |

**How it wires together.** The agent generates items as **Markdown**, not as XML — `markdown-to-qti`
owns the schema so the model never has to. Items render in the QTI player for human review before
anything ships. Reviewed items go into Adapt (run as a tool; the client owns the output) or Numbas
for maths, and export as a **SCORM package** the client's existing LMS already knows how to ingest.
`scorm-again` carries the runtime client-side, so completion tracking survives a lost connection and
reconciles later.

🟢 **Why this shape and not an LMS plugin.** Nothing in it touches platform source, so it is
licence-neutral with respect to the client's LMS — it works against Moodle (GPL), Canvas (AGPL),
Open edX (AGPL) and OpenOlat (Apache) identically, because **a SCORM package is a SCORM package.**
That is the same argument P11 makes for launch and rostering, applied to content.

🔴 **Two licence traps on this path, both measured this pass.** Do **not** reach for
`pipwerks/scorm-api-wrapper` (**391★ and no licence file of any kind** — use `scorm-again`), and do
**not** reach for `cybercussion/SCOBot` (**164★, CC-BY-SA-4.0, and the file is only the
human-readable deed** — a ShareAlike content licence on code, with no patent grant). Both are
popular, which is exactly why they get picked by default.

🔵 **What it does not solve.** Accessibility still needs human review — Adapt is built for it, which
helps, but generated content is not conformant because the framework is. And there is **no
conformance suite for QTI**, so "the item is valid QTI 3" rests on the player accepting it.

## Pattern selection, one line each

| if the client… | run |
|---|---|
| already runs Canvas/Moodle and wants control | **P1** |
| serves low-connectivity learners | **P2** |
| faces a US state mandate with a date | **P3** |
| is an EU institution touching admissions/grading | **P4** |
| is a ministry facing a curriculum mandate | **P5** |
| is a Brazilian or Argentine institution on SIGAA / SUAP / SIU-Guaraní | **P10** |
| wants a teacher's admin time back, with a measurable baseline | **P10**, then **P9** |
| will be asked whether it worked | **P6** — always, alongside the others |
| runs **Moodle** and wants to own its AI layer | **P7** |
| is the **vendor** of a national K-12 platform, or runs one at scale | 🆕 **P8** |
| wants **administrative** automation and will run open-source as its record | 🆕 **P9** |
| 🆕 runs **any LTI-compliant LMS** and the build must pass a security review or DPIA | 🟢 **P11** — *the new default where P1 was the old one* |
| 🆕 wants **AI grading or feedback**, in the EU, Oklahoma or Maryland | 🟢 **P12**, on **P11**'s stack |
| 🆕 is a **US K-12 district or state agency** with an Ed-Fi ODS | 🟢 **P11**, via `edfi-oneroster` |
| 🆕 is an **assessment platform vendor** rather than an institution | 🟢 **P12** — and see UNIwise as the precedent |
| 🆕 will put an agent in front of a **system of record**, or faces a security review or DPIA | 🔴 **P13 — mandatory, and before P11 ships, not after** |
| 🆕 asks for **AI-generated course content or assessment items** for an LMS it already owns | 🟢 **P14** |
| 🆕 needs tracked content delivery to work **offline** | 🟢 **P14** (`scorm-again` is offline-first), with **P2** |
| 🆕 is a **German-speaking-Europe** institution wanting off Moodle's GPL | 🟢 **OpenOlat** as the base (Apache-2.0 + attribution), then **P11** |
| 🆕 runs **Brightspace / D2L** | 🟢 **P11** shape with [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) (MIT) as the read surface — 🔴 **behind P13**, and audit its write surface first: it was not source-read |
| 🆕 asks *"can we buy the identity layer rather than build it?"* | 🟢 **P13 as rewritten by p136** — buy `giantswarm/mcp-oauth` or `atrawog/mcp-oauth-gateway` (both Apache-2.0), build only the LTI adapter |
| 🆕 **ships any open-source component to a client** — so, every engagement | 🟢 **P17** — two days to wire, and it catches the defect `npm ls` and manifest-reading licence scanners both report as `MIT` |
| 🆕 will attach an **AGPL-3.0 connector to a GPL platform** (the **P7** route) | 🔴 **P17 first, as a blocking gate** — `moodle-mcp-server-aql` declares AGPL-3.0 over 141 shipped paths and ships no licence text |
| 🆕 runs **Canvas** and wants the broker wired without forking anything | 🟢 **P13 fourth revision** — implement `OAuthStore`, `putGrant` the per-user Canvas refresh token, pass it to the server constructor |
| 🆕 runs **Moodle** and wants a permissive connector with its own test discipline | 🟢 [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) (**MIT**, Go, committed `go vet`/`staticcheck`/`-race`/coverage) — 🔴 **but audit its write surface: 19 tools in source, 14 documented, and `submit_journal` and `update_assignment` appear in neither** |
| 🆕 wants to **reuse an open skills/prompt library** in a client deliverable | 🔴 Read the licence first: `GarethManning/education-agent-skills` is **CC-BY-SA-4.0 by deed** (847★) — **ShareAlike propagates into the client's adaptations** |

**Cross-cutting constraints.** Prefer **LTI 1.3** over forking any AGPL platform. Never ship
emotion recognition into an EU deployment. Treat unlicensed components as unusable
until counsel clears them, however many stars they have — and treat **`NOASSERTION` as "unread",
not "unusable"**: GitHub reports it whenever its matcher does not recognise a `LICENSE` file, and
this KB has now resolved **both** such rows by reading the payload (`openeducat_erp` → **LGPL-3.0**,
8 241 B; `OpenOLAT` → **Apache-2.0 with two attribution statements**, p135). 🔴 **And `NOASSERTION`
is biased towards institution-derived projects**, because appending institutional attribution is
exactly what defeats a licence matcher — so the rows it mislabels are disproportionately the ones an
education engagement most wants to use (`intel/trends.md` → `T14`).

🆕 **p136 splits `NOASSERTION` once more, because two of its causes have opposite remedies.**
**(a) GRANTED, BODY ELSEWHERE** — the grant is declared in a manifest, a source header or a URL
rather than in a `LICENSE` file. `pipwerks/scorm-api-wrapper` declares *"MIT-style license"* in
`package.json` **and** in `src/JavaScript/SCORM_API_wrapper.js`; `GarethManning/education-agent-skills`
and `cybercussion/SCOBot` ship the **Creative Commons deed** with the legal code off-repository.
🟢 **Remedy: read the manifest and the file headers before concluding anything, and fetch the named
standard text from the SPDX mirror on GitHub** — which works even when the publisher's own host is
unreachable. 🔴 **But a *bespoke* referenced text (`pipwerks`' personalised "MIT-style") stays
genuinely unknown: that one needs a question to the author.**
**(b) THE GRANT WAS DROPPED BY A COPY** — [`0awei0/kt`](https://github.com/0awei0/kt) re-uploads an
**MIT** project in one commit without its `LICENSE` file. 🟢 **Remedy: resolve the lineage and read
the UPSTREAM's grant** (`compose/code/p136-lineage-verdict/`, `intel/trends.md` → `T15`).
🔵 **One line to carry both: ask where the grant IS, not whether a file is.**

Pin commits for repos with no releases. **Benchmarks and datasets need the same licence
screen as code** — the two education benchmarks that exist are both ungranted.

🆕 **Three cross-cutting rules added by p132:**

1. 🔴 **Distinguish three licence states, never conflate them.** **Granted-but-unmatched**
   (`NOASSERTION` over a real grant — `mcp-student-records` is **Apache-2.0** carried as a
   ~745-byte notice block; `openeducat_erp` is **LGPL-3.0** at 8 241 bytes), **silent** (no licence
   file — `sisu-mcp`, `sis-demo`, `DAU-buddy`), and **deliberately withheld**
   (`graduation-project-advisor`: *"Private / TBD"*). Only the first is buildable.
2. 🔴 **Check for mixed licences inside a single repo.** `krzysztofbury/librus-mcp` is **MIT at
   2.x** over a `legacy_reference/` directory that remains **GPL-3.0-only**. A whole-repo fork
   inherits the stricter term; exclude the directory or do not fork.
3. 🔴 **Never adopt a student-built portal connector as a dependency.** They authenticate as the
   pupil with a stored password against an unsanctioned platform, and the ones that work are the
   ones with 2FA disabled. 🟢 **Read them for the API surface map, then rebuild the auth layer**
   (`P8`).

🆕 **Three cross-cutting rules added by p134:**

4. 🟢 **Reach for the standard before the connector.** If the client's platform speaks **LTI 1.3**,
   **OneRoster** or **Ed-Fi**, that is the integration — and it is permissively licensed, vendor- or
   government-owned, and holds no user credential. **Scraping is for platforms that publish no door**
   (the LATAM national systems, the EMEA K-12 platforms), not a general technique.
5. 🔴 **`NOASSERTION` is not biased toward "actually fine" — it is biased toward "unusual".** This
   KB has corrected several `NOASSERTION` rows *upward* (`openeducat_erp` → LGPL-3.0,
   `mcp-student-records` → Apache-2.0) and that run created an expectation p134 broke:
   [`tha-guy-nate/tha-edfi-runner`](https://github.com/tha-guy-nate/tha-edfi-runner) is **MIT plus an
   added clause requiring a visible link to the repo or PyPI page in any publicly available
   application** — a **user-visible obligation inside the client's product**, not a notice in a
   THIRD-PARTY file. **GitHub's matcher was right to flag it.** Read the payload to find out *which*
   way it is unusual, and never to confirm that it is fine.
6. 🟢 **Ask for a conformance test and hand over its output.** `googleworkspace/oneroster-integration-conformance-tests`
   is currently the only one this KB has found, for any standard in this industry. **Where a
   conformance suite exists, running it is the cheapest credibility in the engagement; where none
   exists — LTI AGS, Ed-Fi, and all 43 portal connectors — "it works" is a developer's assertion,
   and that is worth stating in the proposal rather than leaving a client to discover.**

🆕 **Two cross-cutting rules added by p136:**

7. 🔴 **Resolve the repository before you cost the component.** Two rows can be one repository: p136
   measured **11** slug pairs on this KB's own pages with **identical git ref sets** — a rename or a
   transfer that GitHub still answers — plus **37** more that differ only in capitalisation. 🟢 **In
   a proposal this matters twice**: a "two independent implementations" claim can be one, and a
   "well-forked, actively maintained" claim can be one repository counted twice. **Check the ref set
   (`git ls-remote`), then the shared commits, then the dates** — `compose/code/p136-lineage-verdict/`.
8. 🔴 **A declared field is a claim; source and payload are measurements — say which you used.**
   Two source reads have each overturned a cell this KB had published: `learnmcp-xapi`'s docstrings
   name a **JWT** trust anchor the project has no dependency on (p135), and `ictexam-mcp`'s `lti`
   **topic** describes a separate Moodle module while the MCP server itself logs in with an admin
   **password** (p136). 🟢 **Before any auth or standards claim reaches a client deliverable, clone
   the repository and read the three files that matter** — the config loader, the HTTP client and the
   tool definitions. It took under ten minutes per repository in this environment.

