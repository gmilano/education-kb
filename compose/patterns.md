---
industry: education
region: Global
updated: 2026-11-12
---

## 🆕 `p801` — `P801-1` … `P801-3`

🟢 **Every grant named below is a PAYLOAD read at `HEAD` this pass (`T954`), with byte size and title line — not a classification.** 🔵 **That is the difference from `p800`, which had to tell you to re-read every grant before shipping.** 🔴 **Still re-read them at YOUR `HEAD`: a grant is a fact about a commit, and all three recipes pin commits for that reason.** 🔴 **Root licence files only — no dependency-tree audit, so vendored code under other terms is out of scope.**

## `P801-1` — The sovereign permissive education stack (EMEA 🇪🇺 · first time this base can name one)
**The problem it solves:** an EMEA public-sector or university client is told by Council text `ST-14902/26` to reduce dependence on non-European AI tools, and is simultaneously unable to accept the AGPL network clause that every LMS on this base's shelf carried until today.

🟢 **Why this pattern exists now and not at `p800`:** `T960`. [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) is a **byte-verified Apache-2.0** LMS (`10,982 B`, title line `Apache License · Version 2.0, January 2004`, affero×`0`, `HEAD` `7a30c692b249`). 🔴 **Its GitHub sidebar names no licence, which is why classification-based shelves never surfaced it.**

**The wiring:**
1. **Platform** — [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT), 🟢 **Apache-2.0**, self-hosted in an EU/CH region. 🟢 **No source-disclosure trigger on network serving, and an explicit patent grant.**
2. **Attachment layer** — [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi), 🟢 **Apache-2.0** (`10,273 B`, affero×`0`, `HEAD` `5f19a322c39b`). LTI across a service boundary.
3. **Agent runtime** — [`microsoft/agent-framework`](https://github.com/microsoft/agent-framework), 🟢 **MIT** (`1,141 B`, `HEAD` `c7e50ccd9037`). 🔴 **Not `microsoft/autogen`: ARCHIVED at `61.8k★`** (`p800`), and still named as a live option by indexed roundups.
4. **Model gateway** — [`BerriAI/litellm`](https://github.com/BerriAI/litellm) at `HEAD` `f0021859a71f`, 🟢 **MIT outside `litellm/enterprise/`** (`T955`). 🔴 **Add a CI gate that FAILS the build if anything under `litellm/enterprise/` is imported or packaged** — that one check is what keeps this stack MIT, and it is checkable precisely because the grant partitions by directory and not by feature flag.
5. **Learning measurement** — [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit), 🟢 **MIT** (`1,066 B`), for knowledge-tracing so the tutoring claim is testable.

🟢 **Grant posture of the whole stack: Apache-2.0 + MIT, no copyleft, no network clause, EU-hostable.** 🔵 **That sentence is the deliverable** — it is the one thing no prior pass of this base could write.

🔴 **Price the risk honestly:** `OpenOLAT` is `451★` with `165` forks. 🔴 **Thin community, Java, no release listed on the rendered page.** 🔵 **Budget for in-house platform capability, and say so in the proposal** — the licensing risk is gone, the continuity risk is not.
🟡 **Plan to the EARLIER AI Act date (August `2026`), not the Digital Omnibus deferral to `2027-12-02`** — the obligations are identical work and the earlier date is compliant under both readings.
🔵 **Effort: `10`–`12` weeks** to a governed pilot: platform deploy `3`, LTI agent boundary `3`, gateway + CI licence gate `1`, measurement `2`, AI Act deployer documentation `2`.

## `P801-2` — The licence-truth gate (Global · a `3`-hour build that this pass proves pays for itself)
**The problem it solves:** a studio starts an engagement on a dependency list whose licences came from GitHub's sidebar, a roundup article or a paper. 🔴 **All three were wrong somewhere in this pass.**

🔴 **The three failure modes, each measured this pass, not hypothesised:**

| Failure | Instance | What the bytes said |
|---|---|---|
| 🔴 **A roundup asserts a permissive grant** | `frappe/lms` named MIT by an indexed "best LMS `2026`" list | 🔴 **AGPL-3.0**, `33,893 B`, affero×`16` (`T959`) |
| 🔴 **A PAPER asserts a grant its repo does not serve** | `kaushal0494/AITutor-EvalKit`, `EACL 2026` demo, *"MIT-licensed"* | 🔴 **No licence blob anywhere in the tree** (`T961`) |
| 🔴 **A blank sidebar is read as "no licence"** | `litellm`, `OpenOLAT`, `fedena` — all three blank | 🟡 **dual-by-directory** · 🟢 **clean Apache-2.0** · 🔴 **genuinely nothing** (`T956`) |

**The wiring** — the instrument is in this repo at [`ingest/grant-bytes-p801.sh`](../ingest/grant-bytes-p801.sh), and it is `40` lines:
1. For each dependency: `git init` · `git remote add origin https://github.com/OWNER/NAME` · `git -c protocol.version=2 fetch --depth 1 --filter=blob:none origin HEAD`. 🟢 **Trees only — no checkout, no full clone.**
2. Read the root tree, pick the licence blob **case-insensitively** (`LICENSE`, `LICENCE`, `COPYING`, with `.md`/`.txt`/`.rst`). 🔴 **Defect `D1` this pass: `awk BEGIN{IGNORECASE=1}` is a gawk extension and is IGNORED by some `awk`s, so a lowercase `license.txt` reports as "no licence". That nearly published `frappe/lms` as ungranted.** Fold case in `grep -iE`.
3. `git cat-file blob <sha>` — 🟢 the partial clone fetches that ONE blob lazily.
4. Classify on the **title line** plus the `Version` line. 🔴 **Defect `D2`: a whole-file grep for `GNU AFFERO` classifies GPL-3.0 as AGPL-3.0, because GPLv3 §`13` is titled *"Use with the GNU Affero General Public License"*.** 🟢 **Discriminator: affero×`3` = GPL-3.0, affero×`16` = AGPL-3.0.**
5. Record size, raw `sha256`, and a normalised clause hash with copyright lines stripped. 🔴 **Never fingerprint a grant by SIZE across repositories** — one AGPL-3.0 appeared at `35,136` / `34,523` / `34,524` / `33,893 B` this pass.
6. **Fail the build** on: `NO_ROOT_LICENCE_BLOB`, a copyleft family where the architecture assumes permissive, or a payload hash that CHANGED since the last pinned commit.

🟢 **Run it in CI against pinned commits, so a grant that changes under you breaks a build instead of a contract.** 🔵 **Effort: `3` hours. It found a mislicensed LMS, an ungranted EACL toolkit and a dual-grant boundary in one afternoon.**

## `P801-3` — Institution-issued agent authority on a copyleft LMS, with the grant boundary drawn (NA 🇺🇸 · Global)
**The problem it solves:** the client runs Moodle or Open edX — 🔴 **copyleft, and the installed base is essentially all copyleft** — and wants agents doing registrarial and course work. 🔴 **`P800-1` established the authority model; `P801-3` adds the licensing boundary that makes it shippable.**

🔵 **`P800-1` still governs the integrity framing and is not superseded:** `T953` — the LMS cannot distinguish an agent from a student, and Instructure marked a block-agent-logins request *"Will not consider"*. 🟢 **So integrity is assessment DESIGN, never detection.**

**The wiring, with every boundary byte-justified:**
1. **System of record** — [`moodle/moodle`](https://github.com/moodle/moodle) 🔴 **GPL-3.0** (`35,147 B`, affero×`3`) or [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) 🔴 **AGPL-3.0** (`35,136 B`, affero×`16`). 🟢 **Use the canonical Open edX slug** — `ACTION p800-A`; the old `openedx/edx-platform` is a transparent redirect but is invisible to `search/repositories` (`T950`).
2. 🔴 **The boundary.** Moodle is GPL-3.0 — copyleft on **distribution**, 🟢 **no network clause**, so hosting a modified Moodle is not itself a disclosure trigger. Open edX is AGPL-3.0 — 🔴 **serving it over a network IS a trigger.** 🔵 **The two are not interchangeable and this base's shelves have repeatedly written them as if they were.**
3. **Write path** — [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp), 🔴 **byte-verified AGPL-3.0** (`34,524 B`, affero×`16`, `HEAD` `1c5424da9de3`). 🔴 **Deploy as a separate network service. Never link it into client code**, or the client's code takes the AGPL with it.
4. **Deployment** — [`overhangio/tutor`](https://github.com/overhangio/tutor), 🔴 **AGPL-3.0 too** (`34,523 B`). 🔵 **Byte-level aside that validates the method: `tutor` and `openedx-mcp` differ by exactly `1` raw byte and share the normalised clause hash `3e6500ef9d88…`.**
5. **Agent side, kept permissive** — [`microsoft/agent-framework`](https://github.com/microsoft/agent-framework) **MIT** + [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) **Apache-2.0** across the LTI boundary. 🟢 **Permissive agent, copyleft platform, service boundary between them — the copyleft does not cross.**
6. **Authority controls** — scopes, confirmation tokens and an audit trail per `P800-1`, because `openedx-mcp`'s `27` LMS tools reach `deactivate_user`, `request_retirement`, `invalidate_certificate` and `bulk_enroll`.
7. **Evaluation** — 🔴 **you cannot take [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) as MIT** (`T961`: no grant served, whatever the paper says). 🟢 **Use [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (MIT, `1,066 B`) for knowledge tracing, and file an issue asking `AITutor-EvalKit` for the `LICENSE` its paper promises** (`ACTION p801-D`).

🔴 **`p792-D`, TENTH pass: no independent security or data-governance evaluation of ANY education MCP server exists.** 🔵 **With registrarial reach, that gap is the client's risk to accept explicitly, in writing, before go-live** — not a footnote.
🔵 **Effort: `8`–`10` weeks.** 🟢 **In North America, lead with the dated statutory deadline** — NC Session Law `2026-41` requires district policies by `2027-06-30` — rather than with the agent capability.

## 🆕 `p800` — `P800-1` … `P800-3`

🔵 **Each pattern names the repositories, the grant under which each may be used, and the wiring.** 🔴 **Every grant below is a GitHub sidebar CLASSIFICATION or a README assertion, not a byte-verified payload** — the clone channel was unavailable this pass (`T952`). 🔴 **Before any of these ships, re-read the grants on the clone channel.** 🔴 **`P800-1` supersedes nothing, but it REPLACES the detection framing that any assessment-integrity conversation defaults to, because `T953` shows the LMS cannot tell an agent from a student and its vendor has declined to try.**

## `P800-1` — Institution-issued agent authority for an LMS (NA 🇺🇸 · Global)
**The problem it solves:** a client wants agents to do registrarial and course work in their LMS, and their actual exposure is the opposite case — student-side agents already inside sessions the platform cannot distinguish from a human.

**Components**
- 🔴 [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) — **AGPL-3.0** · `3★` · **as a REFERENCE DESIGN, not a dependency.** It is the only education MCP server in this base that writes: `27` LMS tools + `8` CMS tools against Open edX **Ulmo**, Django app + Tutor plugin, LMS at `^api/mcp/`, CMS at `^api/mcp/cms/`, streamable-http with an `X-MCP-Key` bearer token.
- 🟢 [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) — **Apache-2.0** · `377★` — the LTI seam, so the agent host enters Moodle/Canvas/Sakai/Open edX **without linking their copyleft core**.
- 🟢 [`microsoft/agent-framework`](https://github.com/microsoft/agent-framework) — **MIT** · `14.7k★` — the orchestration host. 🔵 **Chosen over a Python-only framework specifically because it ships .NET**, and university and ministry IT estates that refuse a Python agent host will run .NET.
- 🟢 [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) — **MIT** · `44.9k★` — where the engagement is already Python; its durable state and human-review interrupts map directly onto the confirm-token step below.

**The wiring — and the three controls are the deliverable, not the tools**
1. **Re-implement, do not deploy.** AGPL-3.0 on a server-side plugin reaches your modifications and network delivery is the trigger. 🟢 **Lift the DESIGN: three controls, re-implemented under your own grant.**
2. **Scope-gate every tool.** `read` · `write:courses` · `destructive`, exactly as the reference partitions them. A token issued for `read` cannot reach `deactivate_user`.
3. **Confirm-token the high-impact calls.** `deactivate_user`, `request_retirement`, `invalidate_certificate`, `bulk_enroll` are **registrarial** — an agent calling them is exercising institutional authority, not assisting a learner. 🟢 **Two-step: the agent proposes and receives a token; a NAMED human redeems it.** This is `LangGraph`'s interrupt or `Agent Framework`'s handoff, not new machinery.
4. **Append-only audit table, rate limits on writes.** Every write lands with actor, scope, token and timestamp.
5. **Terminate agent identity at the institution.** Agents get their own issued credentials; **no agent ever wears a student's session.**

**Why it sells:** 🟢 scope-gating, confirm tokens and an audit trail are the three things a university or ministry procurement asks for, and `T953` gives the client a reason they cannot defer — **their LMS vendor has stated it will not block student-side agents, and UI-driving agents cannot be detected server-side.** 🟢 **Pair it with assessment-design work rather than a detection tool**, which is also defensible on the record: detection tools are reported as unreliable and as risking false accusations.
**Effort:** `8`–`10` weeks for the authority layer against one LMS; `+4` weeks per additional LMS through the LTI seam.
🔴 **Open risk, ninth pass (`p792-D`): no independent security or data-governance evaluation of any education MCP server exists.** Budget the review; do not assume the reference design was audited.

## `P800-2` — A mastery measurement layer that survives an audit (Global · EMEA 🇪🇺)
**The problem it solves:** every education proposal claims improved learning, and almost none can produce a number a third party can re-derive. 🔵 **This is the pattern that makes `AI proposes, a human decides, the system PROVES it` into something shippable** — the base has had the slogan since `p79x` and no measurement row until now.

**Components**
- 🟢 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) — **MIT** · `461★` — PyTorch knowledge tracing with standardised preprocessing of the standard datasets and the commonly compared DL models. 🟢 **The point is REPRODUCIBILITY: a published model on a public dataset, so the client's own analysts can re-run the claim.** 🔴 No tagged releases — pin a commit.
- 🟢 [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) — **MIT** · `279★` — Bayesian Knowledge Tracing in a deployable React tutor, static-site deployable with optional logging and LTI. 🟢 **`p799` audited its dependency tree CLEAN** — the one row in this base with no copyleft contamination.
- 🟢 [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) — **MIT** · `175★` — local-first learner-facing surface: material → notes, quizzes, flashcards, adaptive tutor; `10`+ providers, spaced repetition, knowledge graph. 🔵 **Use THIS address, not the `0★` fork this base carried (`T950`).**
- 🟢 [`ollama/ollama`](https://github.com/ollama/ollama) — **MIT** · `186.8k★` — inference inside the jurisdiction.
- 🟢 [`qdrant/qdrant`](https://github.com/qdrant/qdrant) — **Apache-2.0** · `35.5k★` — grounding store.

**The wiring**
1. `OATutor` or `OpenTutor` is the learner surface; every interaction emits a `(learner, skill, item, correct, timestamp)` event. **Define the skill model BEFORE any content is authored** — retrofitting one is the reason most of these projects cannot produce a number.
2. `pyKT` consumes the event stream offline and fits the knowledge-tracing model. 🟢 **Report against a PUBLISHED dataset as a baseline alongside the client's own cohort**, so the method is separable from the data.
3. `OATutor`'s BKT drives live mastery decisions; `pyKT` is the audit and the model-selection channel. 🔵 **Two models on purpose: the fast one acts, the rigorous one is accountable.**
4. Grounding in `Qdrant`, inference via `Ollama` — 🟢 **so an EMEA deployment keeps learner data in-jurisdiction and needs no DPIA for a third-party model.**
5. **Evidence out:** per-skill mastery curves and the pinned model commit. 🟢 **Under EU AI Act Annex III, learning-outcome evaluation is high-risk from `2027-12-02` — a reproducible mastery model is the technical-documentation artefact that obligation will ask for**, built before the deadline rather than after.

**Why it sells:** 🟢 it is the only pattern here whose output a regulator, an accreditor and a CFO all read the same way. 🔵 **And it inverts the APAC critique this base carries** — adaptive-tutoring products optimising standardised-test performance — by measuring *mastery* against a published model instead of test deltas.
**Effort:** `6`–`8` weeks for the measurement layer over an existing tutor; `10`–`12` weeks greenfield including the skill model.

## `P800-3` — Rubric grading where the licence risk is in the CORPUS (Global)
**The problem it solves:** a client wants automated scoring of written work with feedback, and the licence review looks at the repositories and misses the thing that actually blocks commercial use.

**Components**
- 🟡 [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) (ArguLens) — **Apache-2.0** · `2★` — discourse-move classifier + LightGBM scorer + LLM feedback generator, Gradio UI, reported mean QWK `0.813` cross-validated, runs locally. 🔴 **`2★` research code: read it as a METHOD, not a dependency.**
- 🟢 [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) — **BSD-3-Clause** · `1.4k★` — 🟢 **`p799` audited it CLEAN, and it already anchors `P788-1`** — the human-in-the-loop grading spine.
- 🟢 [`microsoft/agent-framework`](https://github.com/microsoft/agent-framework) (**MIT**) or [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) (**MIT**) — review-queue orchestration with a human gate.
- 🟢 [`ollama/ollama`](https://github.com/ollama/ollama) — **MIT** — local inference, so student writing never leaves the institution.

**The wiring**
1. 🔴 **Resolve the corpus question FIRST, before any engineering.** `AI_AWE` is Apache-2.0 and its base models are Apache-2.0 on Hugging Face, 🔴 **but PERSUADE 2.0, the training data, is NON-COMMERCIAL.** 🟢 **A permissive repository can be commercially unusable because of its DATA** — a class this base's licence work had not met. **Either licence the corpus, or train on client-owned work under a data agreement, or do not ship the trained artefact.**
2. Take the ARCHITECTURE regardless, because it is the part that survives: a **discourse-feature classifier + a transparent scorer (LightGBM) + an LLM confined to FEEDBACK TEXT**. 🟢 **The score is produced by an auditable model and the generative component never decides the grade** — which is what every regulator in this base and the OECD `2026` reading require.
3. `nbgrader` holds rubric, submissions and the human override; nothing reaches a transcript without a named human releasing it.
4. 🔴 **Report QWK on the client's own double-marked sample.** `0.813` is the paper's cross-validated figure, 🔴 **and its authors note human-rater comparison is still future work.** Do not quote it as a client-facing accuracy claim.
5. `Ollama` for feedback generation in-jurisdiction.

**Why it sells:** 🟢 it is the pattern that passes a legal review for the reason nobody expects — the engagement arrives already knowing that the corpus, not the code, is the blocker — and the architecture puts a transparent model on the decision and the LLM only on the prose.
**Effort:** `6`–`8` weeks on an existing rubric and a client-owned corpus; 🔴 **add the corpus-licensing timeline, which is legal and not engineering, and has in this sector been the longer of the two.**

## 🆕 `p799` — `P799-1` … `P799-4`

🔵 **Each pattern names the repositories, the grant under which each may be used, and the wiring.** 🔴 **`P799-2` REPLACES the LATAM-governance framing every pass since `p795` has carried, because `T949` measured the rate against a global control and it does not survive.**

## `P799-1` — LATAM 🇻🇪🇵🇪🇨🇴: the offline, ministry-grounded teacher assistant

🟢 **Why this pattern exists now.** 🟢 **`p799` found six independent offline-first education agents in one week's in-language intake, and placed three of them to a country on government-document evidence.** 🔵 **Offline is not a degraded mode in this market; it is the requirement.** 🔴 **And `T949` says the governance pitch is not the regional differentiator — this is.**

**The build:**

| Layer | Use | Grant | Why this one |
|---|---|---|---|
| 🟢 **Curriculum corpus** | [`Ignacio-Ghub/asistente-docente-sin-conexion`](https://github.com/Ignacio-Ghub/asistente-docente-sin-conexion) → `web/api/curriculo/*.json` as the **SHAPE**, re-populated from the client jurisdiction's ministry | 🔴 **GPL-3.0 code — boundary-only. Copy the SCHEMA, not the source** | 🟢 `11` files carrying `nivel`, `grado` and per-area `fuentes` citing `mppe.gob.ve` documents with publication months. 🟢 **The only ministry-cited curriculum structure in this base** |
| 🟢 **Agent base** | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **MIT `1,065 B`** | 🟢 `43,394★`, permissive, document → interactive classroom. 🟢 Localise it per `P798-1` rather than building from scratch |
| 🟢 **Local inference** | **Ollama** with a quantised instruct model — the Venezuelan row runs `gemma4:e4b-it-qat` at `6.1 GB` | 🟢 MIT | 🟢 **A `6.1 GB` model on a teacher's laptop is the proven envelope**, measured in the field rather than estimated |
| 🟢 **Scheduling / mastery** | [`leandroeaguilar/aulento`](https://github.com/leandroeaguilar/aulento) — FSRS v5 | 🟢 **MIT `1,072 B`** | 🟢 **Puts the learning claim on a published algorithm, not the model** — which is what an academic council will interrogate |
| 🟢 **Delivery** | Laptop-as-server over classroom Wi-Fi to teachers' phones (the Venezuelan topology); 🟢 Android offline client per [`chasquimallx-byte/yachay-wasi`](https://github.com/chasquimallx-byte/yachay-wasi) | 🔴 **`yachay-wasi` is UNGRANTED — architecture only** | 🟢 No cloud dependency, no per-seat connectivity assumption |
| 🟢 **Accessibility** | [`RowanFalcao/inclusign-ai`](https://github.com/RowanFalcao/inclusign-ai) for Libras / sign-language translation | 🟢 **MIT `1,252 B`** | 🟢 Satisfies a Brazilian inclusion requirement and NA's ADA driver from one component |

🟢 **Two non-negotiable design rules, both taken from the Venezuelan author rather than invented here:**
🟢 **(1) The support alert is a RULE, not the model** — *"El aviso sale de una regla simple, no de la IA."* 🔵 A consequential judgement about a child must have a basis a teacher can read and a regulator can audit; every instrument in [`intel/market.md`](../intel/market.md) demands exactly that.
🟢 **(2) Declare the gap on screen.** Where the ministry has published no content document for an area, the UI says so instead of generating. 🔵 **That single behaviour is the difference between a tool a school inspectorate accepts and one it bans.**
🟢 **(3) Statutory grading scales are data, not configuration guesses** — the Venezuelan row implements *art. `108` del Reglamento de la LOE* (`A`–`E` Primaria, `1`–`20` Media General, pass `10`). 🟢 Capture the client jurisdiction's equivalent BEFORE the first sprint.

**Sequence:** `2` weeks curriculum ingest + ministry citation model → `3` weeks `OpenMAIC` localisation → `2` weeks FSRS mastery layer → `2` weeks offline topology and device testing → `1` week rule-based alerting and gap-declaration UI. 🟢 **`10` weeks, and the curriculum ingest is the only step that cannot be compressed.**

## `P799-2` — Global: the appraisal-and-governance RETROFIT (replaces the LATAM-governance pitch)

🔴 **What this replaces.** 🔴 **Five passes have treated "adoption outpaces governance" as a LATAM opportunity.** 🟢 **`T949`: LATAM's `26%` formal strategy sits between Coursera's global `20%` and IREX's global `34.2%`. The gap is `1.32×` — the same size as `p798`'s "real but modest" grant gap, and nothing like `T940`'s categorical `4.8×`.** 🟢 **So this is a GLOBAL offer, and pricing it as a regional one leaves the larger market unserved.**

🔵 **The actual shape of the problem, which is what makes it sellable:** `94%` of higher-ed professionals use AI at work while `54%` know of any institutional guideline; `86%` of students use AI in their studies; `~26%` of faculty report a formal policy. 🟢 **The institution did not choose these tools — its staff and students already adopted them. So the engagement is a RETROFIT over an existing, unsanctioned estate, never a greenfield deployment.**

**The build:**

| Layer | Use | Grant | Why this one |
|---|---|---|---|
| 🟢 **Estate discovery** | An inventory of what staff and students already use, before any policy is drafted | — | 🔵 **Policy written against an imagined estate is the `54%`-awareness failure reproduced at the client's expense** |
| 🟢 **Appraisal training** | 🔴 **The `11%` figure is the target: faculty able to critically evaluate AI output with rigorous methodology** | — | 🔵 **This is the deliverable LATAM asks for and the global market needs equally.** A policy PDF is free; appraisal capability is not |
| 🟢 **Grounding layer** | [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) agentic-RAG over the institution's own corpus | 🟢 **Apache-2.0 `11,386 B`** | 🟢 Converts an ungrounded assistant into one answering from the client's curriculum — the OECD `2026` Digital Education Outlook's "purpose-built rather than general-purpose" recommendation, implemented |
| 🟢 **Content boundary** | [`danielgalanv/oral-ia`](https://github.com/danielgalanv/oral-ia)'s `571`-byte `NOTICE` as the template | 🟢 **Apache-2.0** | 🟢 **`T936`: the grant covers code, tests, specs and own docs; NOT teaching material, NOT third-party texts, NOT the models.** 🔵 Ship this file with every curriculum-grounded deliverable |
| 🟢 **Disclosure + logging** | Article `50`-style disclosure and interaction logging, switched on from day one | — | 🟢 Binds in EMEA from August `2026` and is cheap now, expensive retrofitted |

**Sequence:** `2` weeks estate discovery → `2` weeks policy drafted against the measured estate → `4` weeks grounding layer → `3` weeks faculty appraisal programme → ongoing. 🟢 **`11` weeks.** 🔵 **Sell the appraisal programme first where there is no budget line, because it is the half that creates the budget holder.**

## `P799-3` — APAC 🇻🇳: remediation inside Vietnam's `18`-month transition

🔴 **A dated, statutory trigger.** 🔴 **Vietnam's Law on Artificial Intelligence took effect `2026-03-01` and classifies AI used in EDUCATION as HIGH-RISK, with an `18`-month transition for systems already in operation.** 🟢 **So any AI already in a Vietnamese classroom has a remediation window with an end date, and the ministry's `12` periods per class per year of AI content for grades `1`–`12` is a delivery opportunity sitting beside it.**

**The build:**

| Layer | Use | Grant | Why this one |
|---|---|---|---|
| 🟢 **Classification + gap assessment** | Map each deployed system against the statute's high-risk obligations | — | 🟢 **The transition is a clock, so the first deliverable is a dated remediation plan, not a platform** |
| 🟢 **Per-jurisdiction policy nodes** | 🔴 **Do NOT ship one global policy.** Korea's AI Basic Act (in force Jan `2026`) and Taiwan's statute are comprehensive; Vietnam names education high-risk; Japan, Australia and India are lighter-touch | — | 🔵 **Four regimes, one product — so the policy must be a swappable node, which is `P798-6`'s APAC shape confirmed by a new statute** |
| 🟢 **Agent base** | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) · [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **MIT `1,065 B` · Apache-2.0 `11,408 B`** | 🟢 Both APAC-origin and permissive. 🔵 **Prefer `DeepTutor` where counsel asks about patent exposure — Apache-2.0 carries a patent grant, MIT does not** |
| 🟢 **Curriculum delivery** | The `12`-periods/year AI content mandate, grades `1`–`12` | — | 🟢 A funded, named curriculum requirement with national scope |

🟡 **Price against the incumbent shape:** NTU Singapore gave **every** undergraduate Gemini Enterprise, AI Studio and Vertex AI from August `2026`. 🔵 **Whole-institution vendor procurement is the competitor, so compete on grounding, governance and jurisdictional fit rather than on model access.**

## `P799-4` — North America: the dated compliance package, with accessibility attached

🟢 **Why dates make this sellable.** 🟢 `~134` AI-in-education bills across `31` states in `2026`; four states (Maryland, Idaho, Oklahoma, Virginia) now mandate **both** state guidance and district-level policy adoption. 🔴 **North Carolina `Session Law 2026-41` supplies the calendar: state model policy `2026-12-31`, local school-unit policies `2027-06-30`, teacher training `2028-06-30`.**

**The build:**

| Layer | Use | Grant | Why this one |
|---|---|---|---|
| 🟢 **District policy kit** | One model policy, instantiated per school unit against the state deadline | — | 🟢 **A statutory due date is the budget argument.** Replicable across `31` states with different dates |
| 🟢 **Product constraints, applied as code** | 🔴 No training on student data (`AB 1159`, `SB 1227`); 🔴 no AI as direct instructor (`HB2400`); 🔴 grade-`9`+ gate with a diagnostics / special-education carve-out (`A 9190`) | — | 🔵 **These are product-shape constraints, not policy text — they must be enforced in the system, and the carve-out means the gate needs a role, not a birthdate** |
| 🟢 **Teacher gate** | [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) — asks before anything reaches a student | 🟢 **MIT `1,078 B`** | 🟢 **Implements "no AI as direct instructor" as an architecture** rather than a promise |
| 🟢 **Accessibility** | [`RowanFalcao/inclusign-ai`](https://github.com/RowanFalcao/inclusign-ai) | 🟢 **MIT `1,252 B`** | 🟢 Against the April `2026` ADA accessibility deadline for large public institutions — 🔵 a second, independently funded driver in the same account |
| 🟢 **Grounding** | [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) | 🟢 **Apache-2.0** | 🟢 District-corpus grounding, so claims are checkable |

**Sequence:** `1` week state-law mapping → `3` weeks model policy + district instantiation → `4` weeks product-constraint enforcement and teacher gate → `3` weeks accessibility remediation → `2` weeks teacher training design. 🟢 **`13` weeks, and it lands before `2027-06-30` if it starts inside Q1.**

## 🆕 `p798` — `P798-1` … `P798-4`

🔵 **Each pattern names the repositories, the grant under which each one may be used, and the wiring.** 🔴 **`P798-1` replaces the LATAM advice `P797-1` gave, because the measurement it rested on has been corrected** (`T940`).

## `P798-1` — LATAM 🇧🇷🇲🇽: localise a global base, mine the in-language repos for requirements

🔴 **Why this replaces `p797`'s LATAM recipe.** 🔴 `p797` recommended opening a licensing conversation with in-language authors to unlock a regional base. 🟢 **`p798` measured the population: `73` addresses, `78.1%` ungranted (against `60.4%` on the English control leg), `94.5%` at zero stars, maximum `5` stars, `0` rows above `20`.** 🔵 **There is no in-language base with a community to inherit. Licensing one unlocks a project nobody has used.**

**The build:**

| Layer | Use | Grant | Why this one |
|---|---|---|---|
| Platform | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 + 🔴 `TRADEMARK.txt` (`3,367 B`) | The regional default. 🔴 **Build and operate freely; do NOT name the deliverable *Moodle* or sell *"Moodle services"* without written permission or partner status** (`T924`, and see [`verticals/solutions.md`](../verticals/solutions.md) for what the licensed route does and does not publish) |
| Tutor | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | ★`58,622`, re-measured exactly at `p797`. The base with an actual community |
| Teacher gate | [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) | 🟢 MIT · `1,078 B` | 🟢 **Read its Moodle integration and its ask-before-send gate.** EMEA-origin, permissive, tiny — copy the shape |
| Offline path | [`Ignacio-Ghub/asistente-docente-sin-conexion`](https://github.com/Ignacio-Ghub/asistente-docente-sin-conexion) | 🔴 GPL-3.0 | 🔴 **ARCHITECTURE ONLY — copyleft, do not link.** Read how it degrades with no connectivity |
| Delivery channel | `p797`'s [`alesdrobysh/miguelito`](https://github.com/alesdrobysh/miguelito) | 🔴 none | 🔴 **Ungranted — read, do not use.** Its dosage design (twice-daily practice prompts over a messaging app) is the citable part |
| Evidence | [`compose/code/p797-dosage/`](code/p797-dosage/) | — | 🟢 Sessions triggered · accepted · turns per accepted session · practice-days-with-a-turn, **counting the students who never took a turn** |
| Content boundary | `P798-2` below | — | 🟢 The `571`-byte `NOTICE` |

🟢 **The requirements document, taken from repositories with zero stars** (`T940`): **offline-capable · LMS-attached · delivered over a channel the student already has · nothing reaches a student without a teacher's action.** 🔵 **That list is not in any analyst report in this base and it is what the region's own developers build when nobody is watching.**

🔴 **Compliance anchor:** `Parecer CNE/CP nº 15/2026`, homologated `2026-11-10` — prohibitions effective on publication, **`12` months for policies, governance instruments and CONTRACTS.** 🔴 **`CITED, NOT READ`: `www.gov.br` refused again this pass.** 🟢 Commercial anchor: **`92%` of students and `79%` of faculty using AI against `30%` who think their institution has responded** (Digital Education Council LATAM `2026`, with Tecnológico de Monterrey), and 🔴 **`4%` of PUBLIC universities with any AI budget** (UNESCO IESALC) — 🟢 **so price it as one instrument with one named owner, not a department.**

🟢 **Timeline:** `6`–`8` weeks to a Moodle-attached, teacher-gated tutor with dosage evidence and the `NOTICE` in place. 🔵 Deliverable one is the evidence, not the tutor — it is what the `12`-month clock asks for.

## `P798-2` — Global: the `571`-byte content boundary, as a week-one deliverable

🔴 **The problem, measured three passes running.** 🔴 A deliverable mixes four layers with four owners — **platform code · studio code · the CLIENT's curriculum · the model weights** — and `T916` found that GitHub's classifier, on a code/content split, reports the code licence and **silently drops the content licence.** 🔴 In education the content licence is the one that governs the curriculum.

🟢 **The template, copied from [`danielgalanv/oral-ia`](https://github.com/danielgalanv/oral-ia)'s `NOTICE`** (`571 B`, Apache-2.0 row, written by the author under a Universidad Politécnica de Madrid pilot — `T936`):

```
<DELIVERABLE NAME>
Copyright <YEAR> <CLIENT / STUDIO>

This product includes software developed under <ENGAGEMENT / GRANT>.

The <Apache-2.0 | MIT> licence of this repository covers the code, the tests, the
specifications and our own documentation. It does NOT cover the teaching material, nor
third-party document texts used in the pilot, which retain the rights and conditions of
their holders; nor the language models, which carry their own licences.
```

🟢 **Wire it as a gate, not a document:** add the file in week one; have the repository's CI assert it exists and names all four layers; and put the same four sentences in the SOW. 🔵 **Four sentences, written before the first curriculum file is committed, forecloses the argument that the client's curriculum was swept into an open-source grant by sitting next to code.**

🔴 **Where it does NOT help:** it is a statement about grants, not a grant (`T919`'s class). It does not clear the brand layer — that is `TRADEMARK.txt`, `NOTICE` brand carve-outs and, on the `frappe` family, a policy in a DIFFERENT repository (`T925`).

## `P798-3` — Global: gate an education MCP server before it touches a roster

🔴 **Why now.** 🔴 `p792-D` has stood unclaimed for six passes: **no independent security or data-governance evaluation of any education MCP server has been published.** 🟢 **`p798` makes it concrete: [`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp) (🟢 MIT · `1,066 B` · blob `a304e1253c64`) exposes `77` classroom-management tools over stdio and runs with the teacher's own permissions.** 🔵 **`77` tools at a teacher's permission level is the largest education MCP surface this base has recorded, and the design is sound — which is exactly why it will be copied.**

**The gate, assembled from rows this base already holds:**

| Step | Use | Grant |
|---|---|---|
| Enumerate the surface | [`compose/code/mcp-allowlist-gateway/`](code/mcp-allowlist-gateway/) | — |
| Classify each tool read vs write | 🟢 **Write tools touching a roster, a grade or a parent contact are the high-risk set** — Annex III, education | — |
| Require a named human decision for every write to a grade | [`compose/code/p797-dosage/`](code/p797-dosage/) logs the decision and the dosage | — |
| Adversarial test | [`opena2a-org/damn-vulnerable-ai-agent`](https://github.com/opena2a-org/damn-vulnerable-ai-agent) | 🟢 Apache-2.0 · ★`150` |
| Reference tutor to gate | [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) | 🟢 Apache-2.0 · ★`34` |

🟢 **Regulatory hook that makes it billable rather than virtuous:** 🔴 🇻🇳 Vietnam requires **pre-deployment registration** of education AI in the National AI Database (`2026-03-01`); 🔴 🇦🇺 **TEQSA compels an institutional generative-AI action plan from every provider**; 🟢 🇪🇺 **Art. `50` transparency is live now** and Art. `27` FRIA is owed by public deployers. 🔵 **Three jurisdictions already require the artefact this gate produces.**

🟢 **Timeline:** `3`–`4` weeks for the gate plus a written evaluation of one server. 🔵 **And if it is published, it is the first of its kind** — `p792-D` closes.

## `P798-4` — EMEA 🇪🇺: sell the half of the AI Act that did not move

🟢 **The split is the whole commercial point and it is now four-source corroborated** (`T939`): 🟢 **Art. `50` transparency has applied since `2026-08-02` and was NOT deferred**; 🔴 **Annex III standalone high-risk — education — moved to `2027-12-02`** by `Regulation (EU) 2026/1744` (OJ `2026-07-24`, in force `2026-07-27`). 🔵 **The expensive work has `13` months of slack. The cheap work is already late.**

**The build:**

| Layer | Use | Grant |
|---|---|---|
| Platform | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 code · 🔴 **logo and icons `CC BY-ND 2.5` — brand assets must be REPLACED, not edited** (`T914`) |
| Course/material agent | [`ANFAIA/SkillNet`](https://github.com/ANFAIA/SkillNet) | 🟢 Apache-2.0 · `10,758 B` · ★`24` · 🇪🇸 |
| Teacher gate | [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) | 🟢 MIT · `1,078 B` · 🇪🇸 |
| Local/self-study path | [`danielgalanv/oral-ia`](https://github.com/danielgalanv/oral-ia) | 🟢 Apache-2.0 · `11,358 B` · 🇪🇸 — 🟢 and the `NOTICE` of `P798-2` |
| Art. `50` marking | [`compose/code/aiact-50-2-marking/`](code/aiact-50-2-marking/) · [`aiact-50-2-pack`](code/aiact-50-2-pack/) | — |
| Art. `27` FRIA + evidence | [`compose/code/p797-dosage/`](code/p797-dosage/) | — |

🟢 **The sales line, from the strongest EMEA datapoint in this base: `63%` of European teachers use AI and `16%` believe general-purpose AI improves outcomes** (Sanoma, `>20,000` teachers, `14` countries). 🔵 **A `47`-point gap is a market that has already tried the generic tool and rejected it** — 🟢 **corroborated this pass by a six-country adult-education study finding teachers adopting AI autonomously, with no regulatory framework, and naming applied professional development as the shared priority.** 🔵 **That is a services engagement, and the OECD's `2026` Digital Education Outlook supplies the pitch in one clause: AI helps learning only when pedagogy stays in control.**

🟢 **Timeline:** `4` weeks to Art. `50` conformity on an existing deployment (the late, cheap work), then `10`–`12` weeks to Annex III readiness ahead of `2027-12-02`. 🔴 **Sequence it that way round** — the deferral removed urgency from the expensive half only.

## 🆕 `p797` — `P797-1`–`P797-5`

🟢 **Every pattern here is anchored to a COMPELLED document with a date, or to a measured refusal.** 🔴 **`P797-2` is new and global: the brand-layer clearance is now a week-one gate with a procedure, because `6` of `37` platform addresses carry a restriction the root `LICENSE` does not mention and one of them is not in the repository at all.**

### 🟢 `P797-1` — LATAM 🇧🇷 · **the `12`-month compliance clock, sold as an instrument and not a department**

| | |
|---|---|
| 🔴 **The compelled document** | 🔴 **`Parecer CNE/CP nº 15/2026`, homologated `2026-11-10`. Prohibited practices effective on publication; `12` months for systems and institutions to adjust policies, governance instruments and CONTRACTS; four risk levels; permanent CNE monitoring** |
| 🔴 **The constraint that sets the price** | 🔴 **UNESCO IESALC: `8%` of LATAM universities have ANY dedicated AI budget — `4%` among PUBLIC ones.** 🟢 So the deliverable is an instrument with ONE named owner, not an evaluation office |
| 🟢 **Build** | 🟢 [`compose/code/p797-dosage/`](../compose/code/p797-dosage/) (the four dosage metrics, `11` controls) + [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, auth model read at `p793`) for the system of record + [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT) where connectivity is the binding constraint + a risk-classification register mapping each AI use to one of the Parecer's four levels |
| 🟢 **Why it lands** | 🟢 **The Parecer compels governance over CONTRACTS, and `87%` of these institutions already use AI with `9%` evaluating it. The artefact they must produce in `12` months is exactly the artefact nobody has: evidence of who decided what, and whether the thing was used** |
| 🔴 **Say this out loud** | 🔴 **The instrument is `CITED, NOT READ` (`T933`) — quote the number, let the client's counsel read the text. 🟢 Do NOT sell the March `2026` `Referencial`'s mention of open-source solutions as an obligation; it is a stated direction** |
| Shape | `6`–`8` weeks, one owner, one dashboard |

### 🔴 `P797-2` — GLOBAL · **the week-one brand-layer clearance, with the procedure and the family rule**

🟢 **`P796-5` proposed this on three instances. `p797` ran it on `37` addresses and it survives contact: `6` bespoke restrictions, `23` stock reservations, `25` clean.** The procedure, in the order that finds things:

1. 🟢 **Enumerate the ROOT TREE, do not grade the root `LICENSE`.** `git clone --filter=blob:none --bare` then `git ls-tree HEAD` — `37` addresses in `100` seconds, `0` failures ([`ingest/p797-brand-layer-gate.sh`](../ingest/p797-brand-layer-gate.sh)). 🔴 **`curl -sI` cannot do this: it returns `403` for a live address and an invented one alike** (`T923`).
2. 🟢 **Read every non-`LICENSE` candidate: `NOTICE*`, `TRADEMARK*`, `BRAND*`, `COPYRIGHT*`, `LICENSE_*`.** `OpenOLAT`'s `NoDerivs` logo clause is in `NOTICE.TXT`; `Moodle`'s policy is in `TRADEMARK.txt`; `metabase`'s carve-out is in `LICENSE-EMBEDDING.txt`.
3. 🟡 **Grade three-state.** Apache-2.0 §`6` and GPL-3.0 §`7(e)` decline trademark rights in EVERY repository that carries them — `23` of the `29` term-matching files. 🔵 **A two-state gate reports them and means nothing.**
4. 🆕 🔴 **Then clear the FAMILY, not the address** (`T925`). `frappe/education` and `frappe/lms` are brand-clean by inspection and brand-restricted in fact, from `frappe/erpnext`.
5. 🟢 **Record the kind of every sha you write** (`T926`): `blob` or `HEAD`, never a bare `12`-hex.

🔵 **Cost: under two hours on any shortlist.** 🔴 **Value: on `Moodle` — the platform to assume if a client has an LMS — the restricted act is MARKETING the deliverable, not building it, and the licensed route is the Certified Partner programme. That is a commercial decision for week one.**

### 🟢 `P797-3` — APAC 🇰🇷 · **the post-mandate offer: sell to the school, prove it to the teacher**

🔴 **The evidence: `34.2%` → `5.2%` in twelve months once adoption became discretionary** (`T932`). 🟢 **The buyer that remains is `1,900` lead schools that CHOSE, plus AI-subject 인정 교과서 piloting `1H 2027`.** 🟢 **Build:** a teacher-controlled narrow-scope tutor on [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) (MIT, ★`43,392`) or [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) (Apache-2.0, ★`58,622`) + `p797-dosage` reporting **acceptance** and **practice-days** per class, not licences issued. 🔵 **The pitch is one sentence: the last national rollout lost `94.8%` of its schools, and the only defence is a number that shows the teachers who kept choosing it.** 🔴 **`0` Korean procurement documents have been reached — this is an argument, not a tender, and it must be presented as one.**

### 🟢 `P797-4` — APAC 🇨🇳 · **the only contribution-shaped entry in this base**

🟢 **`教科信〔2026〕1号` commissions a state-sponsored OPEN-SOURCE community — the `启悟学习社区`, led by 上海交通大学 — alongside the `国家教育智能算力服务平台` (BUPT-led), `23` education-purpose large models and `13` subject-vertical models.** 🔵 **Every other regional route in this base is procurement-shaped; this one is contribution-shaped, and contribution is a route a foreign studio can actually take.** 🟢 **Build:** publish a reusable component against the national platform's interfaces (assessment rubric scoring, curriculum alignment) under MIT/Apache-2.0, with the `p797-dosage` metrics as the evaluation artefact. 🔴 **Say the limits: the plan is read through secondary coverage, the platform's interface documentation has not been reached from this session, and no procurement route is established.**

### 🟢 `P797-5` — EMEA · **transparency now, conformity by `2027-12-02`** (re-anchored, unchanged in substance)

🟢 **Art. `50` transparency has applied since `2026-08-02` and was NOT deferred; Annex III standalone high-risk moved to `2027-12-02` (`Regulation (EU) 2026/1744`).** 🔵 **So the expensive work has `13` months of slack and the cheap work is already late.** 🟢 **Build:** the disclosure layer first (every AI-assisted artefact labelled at the point of production, a named human decision-maker per decision class, an Art. `27` FRIA skeleton for the deployer) on a permissive base — 🔴 **and NOT on `OpenOLAT` if the deliverable is white-labelled, because its logo and icons are `CC BY-ND 2.5`** (`T914`). 🟢 **`63%` of European teachers use AI; `16%` think the generic tool improves outcomes. Sell into the `47`-point gap.**

## 🆕 `p796` — **five patterns. The regional four are each anchored to a COMPELLED document with a date — `Regulation (EU) 2026/1744`'s Art. `50`, Vietnam's registration, TEQSA's action plan, North Carolina's `SL 2026-41`. `P796-5` is a week-one gate productised from `T914`, because on three platforms this base recommends, white-labelling is barred or restricted by a licence file nobody opened.**

### 🟢 `P796-1` — The Art. `50` transparency pack: sell what `2026/1744` did NOT defer · **EMEA** · 5–7 weeks

🔵 **Why this pattern exists, and why it replaces a pattern in this file.** 🔴 `P792-3` and `P794-2` were both timed against an Annex III high-risk deadline of `2026-08-02`. 🔴 **`Regulation (EU) 2026/1744` moved that to `2027-12-02` (`T922`), so both patterns' urgency is gone.** 🟢 **But Art. `50` transparency was NOT deferred — it has applied since `2026-08-02`.** 🔵 **So the expensive work got a `16`-month reprieve and the cheap work is already overdue. That inversion is the sale.**

**The wiring, named to artefacts:**
1. **Disclosure surface** — every AI-generated turn labelled at the point of delivery. Build it into the tutor boundary, not the UI chrome: [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (🟢 **MIT**, ★`102`, 🇫🇷) is the only European-origin tutor-as-MCP-server in this base, and an MCP boundary is the natural place to stamp provenance on every response.
2. **Evidence spine** — [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) (Apache-2.0, `12,227 B`) for Art. `27` FRIA artefacts. 🔴 **Licence note from this pass: that file carries TWO grants — Apache-2.0 AND a Creative Commons grant — and GitHub reports only the Apache half (`T916`). Read both before vendoring; the CC half governs its documents, which is what you will reuse.**
3. **Teacher-controlled trigger** — the `T907` finding holds regardless of the deadline shift: `96%` uptake, `⅓` dosage, `≈0.06` SD. 🟢 Carry `P794-1`'s engagement trigger forward unchanged.
4. **Delivery surface** — [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (🟢 Apache-2.0, `10,982 B`, pushed `2026-11-12`) remains the permissive European LMS. 🔴 **But `NOTICE.TXT` licenses its logo and icons `CC BY-ND 2.5` — replace the brand assets, do not modify them (`T914`).**
5. **Schools-sector surface, if the client is K-12** — [`hedyorg/hedy`](https://github.com/hedyorg/hedy) (🟢 **`EUPL-1.2`**, ★`1,697`, pushed `2026-11-06`). 🔴 **`EUPL-1.2` is copyleft with a statutory compatibility list (`T918`); treat it as you would GPL for redistribution purposes, and note it is the Commission's own licence — which is an argument *for* it in a public-sector bid, not against.**
6. **Named human decision-maker** — a role, in the contract, with a logged identity on every consequential decision. 🟢 This is the one component that satisfies NA, EMEA, APAC and LATAM simultaneously.

🟢 **The pitch in one line:** *"Your conformity deadline moved to December 2027. Your disclosure obligation started in August 2026. We close the second now and leave you ready for the first."*

🔵 **Why 5–7 weeks:** disclosure, logging and a decision register are small, well-bounded builds. 🔴 **No conformity assessment in scope — that is the `2027` engagement, and selling it now is selling against a deadline that no longer exists.**

### 🟢 `P796-2` — The compelled-document factory: one evidence instrument, two regulators · **APAC 🇻🇳 🇦🇺** · 8–10 weeks

🔵 **Why this pattern exists.** 🔴 **`Gap 254` has said for several passes that APAC coverage here is regulation-only, with no compellable hook. `p796` found two, both with dates:**

| Jurisdiction | The compelled document | 🔴 Who must produce it |
|---|---|---|
| 🇻🇳 **Vietnam** | 🔴 **Pre-deployment registration in the National AI Database** — education is a high-risk category under the Law on AI, effective **`2026-03-01`** | Every operator of an education AI system |
| 🇦🇺 **Australia** | 🔴 **An institutional action plan addressing generative-AI risks, required by TEQSA** | 🟢 **EVERY higher-education provider in the country** |

🟢 **The insight that makes this one engagement rather than two: both documents want the same evidence** — an inventory of AI systems, a risk classification per system, a named human decision-maker, a record of oversight, and an outcome-measurement commitment. 🔵 **The regulator differs; the artefact differs only in its labelling.**

**The wiring:**
1. **System inventory** — enumerate AI touchpoints from the LMS itself via [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT) where Canvas is the system of record. 🟢 **An inventory read from the LMS is defensible; one assembled from interviews is not.**
2. **Risk classification** — map each system to the local category (Vietnam's high-risk list; TEQSA's risk domains). 🟢 Reuse [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance)'s FRIA structure as the template — 🔵 **EU-shaped, which is an advantage: the EU structure is a superset of both.**
3. **Oversight record** — the named-decision-maker log from `P796-1`, unchanged.
4. **Outcome commitment** — 🟢 **the dosage instrument (`p795-E`, still unbuilt) is what both regulators will eventually ask for and neither can be fobbed off on.** 🟢 Scope it here as the second deliverable: sessions triggered · accepted · turns per session · practice-days-with-a-turn.
5. **Tutor behind the boundary, if one is in scope** — [`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) (🟢 **MIT**, `1,071 B`, 🇻🇳, pushed `2026-11-09`): Socratic hint escalation, answer-leak checking before send, 🟢 **and rubric totals computed in code rather than by the model — which is exactly what a regulator wants to hear about an assessment system.**

🟢 **Export angle worth stating in the first meeting:** 🔴 **APAC ed-tech selling proctoring or admissions tools into the EU is in Annex III, so `2027-12-02` is an APAC export deadline.** 🟢 One evidence pack, three jurisdictions.

🔴 **Declared limit: `0` procurement documents reached for Vietnam or Australia** — these are statutory and regulator obligations, not tenders. 🟢 The buyer is the institution's registrar or DVC, not a procurement portal.

### 🟢 `P796-3` — Local-policy conformance for the US district pipeline · **North America 🇺🇸** · 6–8 weeks

🔵 **Why this pattern exists.** 🟢 **`134` AI-in-education bills across `31` states in `2026`, and `35`+ states with departmental guidance, produce a shape no other region has: a state model policy followed by hundreds of LOCAL policies, each with its own deadline.**

🟢 **The calendar is the pipeline:**

| Jurisdiction | Instrument | Deadline |
|---|---|---|
| 🇺🇸 **North Carolina** | **Session Law `2026-41`** | 🔴 **Model policy `2026-12-31`** → **local school-unit policies `2027-06-30`** → teacher PD `2028-06-30` |
| 🇺🇸 **Maryland** | state law | 🔴 **District AI policies by autumn `2026`** |
| 🇨🇦 **Ontario** | mandatory `2026-27` PA-day topic, 🔴 **no province-wide memorandum** | 🟢 **The buyer is the board — and there are `72`** |

🔵 **The commercial observation that matters: a district does not need a policy written — the state writes the model. It needs to PROVE it is following the one it adopted.** 🔴 **No district can produce that evidence today.**

**The wiring:**
1. **Policy-to-control mapping** — take the adopted local policy and decompose each clause into a checkable control (disclosure present · student data not used for training · human review on consequential decisions · grade-level restriction honoured). 🟡 **`NY A 9190`-style grade-level limits and `CA AB 1159`-style training-data bars are the two clauses most likely to appear, so build those controls first.**
2. **Instrumentation at the LMS** — [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT) to read actual usage. 🟢 **Evidence that a control holds must come from the system, not a survey.**
3. **Engagement trigger** — [`P794-1`](compose/patterns.md) unchanged: the `T907` trial says the binding constraint is dosage under teacher control, and a district's own PD deadline (`2028-06-30` in NC) is the lever.
4. **Teacher-side authoring** — [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) (🟢 **MIT**, `1,069 B`): labs, exams and grading as explicit DSLs with human review and sandboxed evaluation. 🔵 **A DSL artefact IS the audit trail — the lesson and its review are the same object.** 🟡 Its grading path is self-described MVP; use the structure, build the grader.
5. **Reporting** — 🔴 **run [`metabase/metabase`](https://github.com/metabase/metabase) as its own AGPL-3.0 application behind SSO and link to it.** 🔴 **`p796` sizes the reason: its embedding carve-out is `8,877 B` of terms containing no OSI grant at all (`T914`), and embedding into a district-branded portal is precisely what it governs.**

🔵 **Why 6–8 weeks:** the policy already exists and the LMS already exists. The build is the control mapping and the evidence reader.

🔴 **Declared gap: no spend figure for Canada or Mexico**, so Ontario and SEP engagements are scoped on policy and adoption evidence, not on a budget benchmark.

### 🟢 `P796-4` — The institutional evaluation office, priced for a `4%` budget · **LATAM 🇺🇾 🇧🇷 🇨🇱 🇨🇴 🇨🇷** · 6–8 weeks

🔵 **Why this pattern exists, and why `p796` re-prices it.** 🟢 **The gap is measured and extreme: `87%` of Latin American universities use AI, `26%` have a formal strategy, `18.5%` have institution-wide policies, `9%` have formal evaluation mechanisms** (UNESCO IESALC 2026, `200` institutions, `19` countries). 🔴 **And the constraint is now measured too: `8%` have a dedicated AI budget, and among PUBLIC universities it is `4%`.**

🔴 **So the `p794`/`p795` framing — an evaluation *office* — is priced above what `96%` of public institutions can buy.** 🟢 **`p796` re-scopes it as an INSTRUMENT with an institutional owner, not a department.**

**The wiring:**
1. **One measurement, not a programme** — the dosage instrument: sessions triggered · accepted · turns per session · practice-days-with-a-turn, read from the LMS. 🟢 **`p795` verified that no published open-source implementation of this exists**, which makes it the clearest unclaimed artefact in this base.
2. **Read from the system of record** — [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT), or the Moodle plugin boundary where Moodle is in place.
3. **Tutor behind the boundary** — [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT) or the institution's existing tutor; 🟢 **the instrument must not assume a particular tutor, because PUC Chile already runs `194` pedagogical agents across ~`100` courses and its own stated gap is outcome measurement.**
4. **Spanish/Portuguese-first surface** — 🔴 **and a licence caution this base learned the hard way: [`luscitiosus/Dirigo`](https://github.com/luscitiosus/Dirigo)'s `362 B` Spanish licence is `CC BY-NC-SA 4.0`, which an English-only probe graded as `CC-BY-4.0`, silently stripping NonCommercial (`T902`). 🔴 NonCommercial bars a client deliverable. Read restriction vocabulary in the local language first.**
5. **Publication target** — 🟢 **new this pass: UNESCO has launched a regional Observatory on AI in Education for Latin America and the Caribbean, and has partnered with Chile's CENIA.** 🔵 **An institution that can feed an observatory has a reason to fund the instrument, and a citation it can use.**

🟢 **The pitch:** 🔴 *"`87%` of your peers use AI. `9%` can say whether it works. `4%` of public universities have a budget for finding out."* 🟢 **So we build the measurement, not the office** — and the regulatory environment reinforces it: 🇨🇱 **Chile's bill replaces EU-style conformity assessment with self-classification, which is cheaper to comply with and harder to PROVE.** 🟢 **Self-classification raises the value of evidence, it does not lower it.**

🔴 **Declared limit: no AI-in-education statute in Brazil, Mexico or Chile, so there is no deadline to sell against.** 🟢 The sale is made on the evaluation gap, which is measured, and on 🆕 **Cetic.br's `53%`-use / `22%`-guidelines split in Brazil**, which is the same gap at school level.

### 🟢 `P796-5` — The brand-layer licence gate, week one · **Global; every engagement in this file** · 3–5 days

🔵 **Why this pattern exists.** 🔴 **Nearly every engagement in this file ends in a white-labelled deployment, and `p796` found that on THREE platforms this base recommends, the brand assets are licensed more restrictively than the code (`T914`) — a fact invisible to grading the root `LICENSE`.**

**The gate, and it is five commands, not a project:**
1. **List the root tree, not the root `LICENSE`.** `git clone --filter=blob:none --bare --depth 1` then `git ls-tree --name-only HEAD`. 🟢 **`176` addresses in `16` seconds at `12` parallel, `0` failures — cost is not the obstacle; nobody had asked.**
2. **Count licence FILES.** 🔴 **`13` of `174` rows in this base carry two or more; `metabase` has `4`, `DSpace` has `4`, `open-webui` has `3`.**
3. **Count GRANTS inside each file, keyed on per-grant VERSION LINES** (`Version 3, 29 June 2007`, `Version 2.0, January 2004`, …) — 🔴 **never on the licence NAME, which recurs four times inside a single GPL-3.0 text and over-reported `32` rows where `5` were real (`T917`).**
4. **Grep the non-`LICENSE` files for brand vocabulary** — `logo`, `icon`, `branding`, `trademark`, `NoDerivs`, `ND`. 🔴 **This is the step that finds `OpenOLAT`'s `CC BY-ND 2.5` logo clause, which sits in `NOTICE.TXT`, `14,412 B`, a file this base had never opened.**
5. **Grade the DELIVERY question separately from the SHIPPING question.** 🟢 Three outcomes, and they are genuinely different:

| Finding | Example | 🟢 Verdict |
|---|---|---|
| 🔴 Branding alteration is a **material breach** | `open-webui` clause `4` | 🔴 **No white-labelled delivery. Internal tool only, or negotiate** |
| 🟡 Brand assets are **`NoDerivs`** | `OpenOLAT` `CC BY-ND 2.5` | 🟢 **Ship it — REPLACE the logo and icon set.** `ND` forbids modifying theirs, not shipping yours |
| 🔴 The **embed** has its own non-OSI terms | `metabase` `LICENSE-EMBEDDING.txt`, `8,877 B` | 🟢 **Run it standalone behind SSO and link to it.** Do not embed in a client-branded surface |

🟢 **Sell it as the first week of any platform engagement, or run it unbilled as a qualification step** — 🔵 **the alternative is discovering in week ten that the deliverable cannot carry the client's name.** 🟢 **`3` for `3` on rows this base had already recommended, which is the honest argument for making it standing rather than optional.**


## 🆕 `p795` — **four patterns. `P795-1` is the one this base has been missing: AI inside the LMS of record rather than beside it. `P795-2` is a licence-clearance service productised out of this pass's own instrument.**

### 🟢 `P795-1` — AI inside the LMS of record, as a plugin · **Global; EMEA and North America first** · 6–8 weeks

🔵 **Why this pattern exists, and why it is late.** 🔴 Every platform pattern in this file so far proposes a system: Moodle, Canvas, Open edX, Sakai, Chamilo. 🔴 **An institution with a working LMS of record is not buying a replacement**, and this file had no catalogued artefact for the other shape until this pass.

**The wiring, named to artefacts:**
1. **Delivery surface** — [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) (🟡 **GPL-3.0**, `35,153 B`, ★`281`, pushed `2026-11-07`) as the in-Moodle plugin: tutoring, quizzes, mind maps and RAG over the course's own materials.
2. **Retrieval corpus** — the client's existing Moodle course files. 🟢 **No content migration, which is where LMS-replacement projects die.**
3. **Model routing** — a self-hosted gateway so prompts never leave the institution's boundary; [`ollama/ollama`](https://github.com/ollama/ollama) (MIT, ★`186,787`) for the local-inference option EMEA clients ask for first.
4. **Diagnostic layer** — [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) (🟢 **MIT**, `1,102 B`) to make the tutor identify the misconception before teaching, not after.
5. **Provenance** — the handout-sourcing approach in [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) (🟢 **MIT**, `1,065 B`): every answer cites the course material it came from. 🟢 **This is the answer to the `16%`-efficacy-belief problem — a teacher can check the citation.**
6. **Analytics** — 🔴 **run [`metabase/metabase`](https://github.com/metabase/metabase) as its own AGPL-3.0 application behind SSO and LINK to it. Do NOT embed `app-embed.js` in a client-branded surface (`T912`).**

🔴 **The licence decision to make before writing a line, stated to the client in week one:** 🔴 **a Moodle plugin inherits GPL-3.0, permanently, and there is no permissive option inside Moodle's plugin boundary.** 🟢 **For most institutional clients this is fine — they are deploying, not redistributing.** 🔴 **It is NOT fine for a client who intends to resell the plugin as a product**, and that question must be asked before week two. 🟢 **If the answer is "resell", switch to [`ai-shifu/ai-shifu`](https://github.com/ai-shifu/ai-shifu) (🟢 Apache-2.0, `11,342 B`) as a standalone surface and integrate via LTI instead.**

🟢 **Why 6–8 weeks and not 10–12:** no data migration, no new system of record, no procurement of a platform. 🔵 The work is the plugin, the retrieval corpus and the governance sign-off.

### 🟢 `P795-2` — Open-source licence clearance for an education AI programme · **Global; sellable in every region** · 3–4 weeks

🔵 **This pattern is this pass's instrument, productised — and `p795` is the evidence it is needed.** 🔴 **In one sweep of `167` repositories this base found: a `★158,483` row that cannot be white-labelled, a `★50,301` row whose embed file forbids removing the vendor's logo, an MIT-looking licence that is non-commercial and bars redistribution, a `★2,053` row with no licence at all, a `★125` row that is Business Source License 1.1, and a `★707` row whose "licence" is `19` bytes of prose.** 🟢 **Every one of those is a finding a client's own procurement would have missed, and four of them were missed by GitHub's classifier.**

**The deliverable, and it is an artefact not a report:**
1. **Address extraction** from the client's manifests and the repositories they intend to build on.
2. **Four-state existence** — `git ls-remote` exit status + ref count, plus `archived` and `pushed_at` from `gh api search/repositories` (`10` × `repo:` per call). 🟢 **LIVE-MAINTAINED · LIVE-ARCHIVED · EMPTY · ABSENT, plus a staleness band.**
3. **Grant grading from the BYTES** — blobless bare clone, `cat-file -s` and `-p` on root licence files. 🔴 **Match the first non-blank line only, never a body substring (`T910`).**
4. **The rider gate** — byte size against the family's canonical size (`>25%` = read it), numbered-clause count against the family's, and a restriction vocabulary (NC / ND / SA / branding / field-of-use) 🔴 **scoped by family so the GPL does not vote against itself (`T911`)**, in every language the corpus contains.
5. **Licence-FILE count per repository** — 🔴 **`metabase` has four and the dangerous one governs a single file (`T912`).**
6. **A family field AND a consequence field** per row (`T909`). 🟢 **"Can we ship it" is the question the client is actually asking.**
7. **Dependency licences at the RESOLVED version** — lockfile pins read against `pypi.org` / `registry.npmjs.org` per version. 🔴 **`T884`: a licence is a property of a version.**

🟢 **Controls are part of the deliverable, not the methodology section:** plant a known-absent address, a known-ridered licence, and a non-English grant, and show they are detected. 🔵 **This pass's gate returned `0` flags on its first build and was only known to be broken because a control fired.**

🟢 **Why it sells in every region:** it is pre-engagement work with a fixed scope, it produces a defensible artefact for counsel, and 🟢 **it is the cheapest possible way to discover that the surface you planned to white-label cannot be white-labelled** — before the design review, not after.

### 🟢 `P795-3` — Vietnam automated-assessment conformity, now against a DATED instrument · **APAC 🇻🇳** · 10–12 weeks

🟢 **`P791-1` was written at `p791` against an anticipated Vietnamese instrument. `p795` supplies the dates, so the pattern is now sellable rather than speculative.**

🔴 **The facts to lead with:** Vietnam's AI law took effect **`2026-03-01`**, and a **July 2026 decision classes certain education AI systems — automated assessment specifically — as HIGH-RISK.** 🟢 **Separately, Vietnam's Ministry of Education has set AI content hours for grades `1`–`12`**, so two budget lines exist in the same ministry.

🟢 **Sell them together, in this order:** (1) a conformity assessment for any automated-assessment system the client already runs or intends to procure — 🔴 **high-risk classification means documentation, risk management and human oversight, and the grade must be reserved to the teacher**, which is this base's standing `P788-1`/`P790-1` rule and is now a statutory requirement rather than a design preference; (2) curriculum-delivery work against the grades `1`–`12` AI content hours, reusing the `P793-2` provincial-delivery shape.

🟢 **Artefacts:** [`ai-shifu/ai-shifu`](https://github.com/ai-shifu/ai-shifu) (Apache-2.0) as the permissive delivery surface, [`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) (MIT, 🇻🇳-origin, added `p794`) as the in-country reference, and the diagnostic/provenance skills from `P795-1` for the audit trail. 🔴 **Do not propose `CaviraOSS/PageLM` here or anywhere else — non-commercial, redistribution prohibited (`T908`).**

### 🟢 `P795-4` — Institutional AI evaluation office · **LATAM 🇺🇾 🇧🇷 🇨🇱 🇨🇴 first; ports to North America** · 6–8 weeks

🟢 **The pitch is one pair of numbers: `87%` of LATAM institutions use AI in at least one area, and `9%` evaluate whether it works** (UNESCO IESALC, `200` HEIs, `19` countries). 🔴 **`55%` have no AI budget at all**, so the engagement must be funded from an existing programme line — 🟢 **which is why it is scoped as an evaluation office rather than a platform.**

**The deliverable:**
1. **A measurement artefact first**, as `P793-1` was: sessions triggered · accepted · turns per session · practice-days-with-a-turn — 🟢 **the dosage instrument `p794-E` identifies as the scarce component**, read from the institution's LMS.
2. **An institutional AI policy** mapped to the **OECD AI Principles** (adopted by Argentina, Brazil, Chile, Colombia, Costa Rica, Mexico and Peru) — 🔴 **NOT to a sectoral education statute, because no LATAM country has one** (declared in `intel/market.md`).
3. **A baseline and a second measurement** at week 6, so the client owns a before/after rather than a pilot anecdote.
4. **Institutional partners to name in the bid:** UNESCO's **Observatory on AI in Education for LAC** (launched April 2026 at ECLAC, Santiago), **Tecnológico de Monterrey**, **CENIA** (Chile); and **Ceibal** (Uruguay, `75%` of public-school teachers using AI) and **Cetic.br** (Brazil, `22%` of schools with guidelines) as the data sources a ministry already trusts.

🟢 **Why it ports to North America without redesign:** `4` states (**Idaho, Maryland, Oklahoma, Virginia**) now mandate district-level AI policy adoption, and roughly a quarter of faculty report a formal institutional AI policy. 🔵 **Same deliverable, different driver — statutory mandate instead of an evaluation gap.** 🔴 **In the US add the `April 2026` ADA accessibility obligation**, which reaches purchased edtech and not only what the client built.

### 🔴 Still unwritable, and why

🔴 **An EMEA pattern with a conformity DEADLINE on it.** 🔴 The EU AI Act's high-risk education obligations reportedly moved from `2026-08-02` to `2027-12-02`, and `T906` blocks the primary source that would settle it. 🟢 **`P792-3` and `P794-2` remain valid in SCOPE** — the emotion-recognition ban and AI-literacy duty are in force since `2025-02-02` and are not contested. 🔴 **Do not put the date on a slide until counsel confirms it.**

## 🆕 `p794` — **four patterns, one per region, and the first is a reversal of what every prior pattern here optimised**

🔵 **`T907` changed the premise.** Thirteen passes of this base have ranked **tutors**. The strongest trial ever run on an AI tutor reports `96%` uptake, `⅓` dosage and `0.06` SD — 🔴 **so the tutor was not the scarce component, and three of the four patterns below are built around that.**

### 🟢 `P794-1` — Engagement-triggered tutoring: put the tutor on the LMS event, not on a button · **North America first** · 8–10 weeks

🔴 **The failure mode is measured, not hypothesised.** Khanmigo in `18` Tennessee middle schools: **`96%` of students used it, the median student messaged it on about `⅓` of practice days, two-year ITT `≈0.06` SD** against `0.2`–`0.4` SD for high-dosage human tutoring. 🟢 **Khan Academy's own 2026 fix was to stop waiting to be invoked and auto-activate during practice.** 🔵 **The product lesson generalises: a tutor behind a button is a tutor that is not used, and no model upgrade repairs that.**

**What this pattern builds:** not a tutor — **a trigger policy that owns when the tutor appears**, with the tutor itself as a replaceable component behind MCP.

**The wiring**

1. **Tutor as a tool, not an application.** [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) — 🟢 **MIT, `1,073 B`, `7f7f7a24de57`**, `1,279`-file tree, pushed `2026-11-12`, `★102`. 🔵 **This is why it is the right shape:** it exposes the Intelligent Tutoring System *as an MCP server*, so the trigger owns the interaction and the tutor is swappable. 🟡 **At `★102` it is a seed — pin a sha and expect to co-maintain.**
2. **Read the moment of difficulty from the system of record.** [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, `1,071 B`, `★323`) for Canvas; `P793-1` already specifies the hardening this server needs and the per-tool allowlist it cannot get from the Canvas API. 🔴 **Deny-by-default stays: the trigger reads submissions and attempts; it does not write grades.**
3. **Trigger policy as an explicit graph, not prompt text.** [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) — 🟢 **MIT, `★44,865`**. Nodes: *attempt failed twice on the same objective* · *time-on-task exceeded without submission* · *quiz item below mastery threshold* → offer the tutor **in the practice surface**, not in a side panel. 🟢 **Make every trigger a named, logged, teacher-overridable rule** — this is what you will be asked to evidence.
4. **Dosage is the primary metric, before any outcome metric.** Instrument *sessions triggered · sessions accepted · turns per session · practice days with ≥1 tutor turn*. 🔴 **The Khanmigo trial failed on the fourth of those and nobody was watching it.** 🟢 Ship the dosage dashboard in week 3, before the tutor is tuned.
5. **Teacher control is the regulatory hinge and the pedagogical one.** Teacher activation, a maximum-interaction cap, and no automated grade — 🟢 **Singapore's MOE independently shipped exactly these three guardrails on its own Learning Assistant**, so the design is defensible by precedent as well as by argument.
6. **Model serving stays local where the data does.** [`ollama/ollama`](https://github.com/ollama/ollama) (MIT, `★186,787`) for single-site, [`vllm-project/vllm`](https://github.com/vllm-project/vllm) (Apache-2.0, `★96,826`) for district scale.

🔴 **Licence constraint to state at kickoff:** 🔴 **do NOT reach for [`open-webui/open-webui`](https://github.com/open-webui/open-webui) as the delivery surface.** `T900` — its `LICENSE` carries a fourth clause making alteration of *"Open WebUI" branding* a **material breach**, so it cannot be delivered under the client's name. 🟢 In this pattern the surface is the LMS the client already owns, which sidesteps the problem entirely.

🟢 **Why it closes in North America now:** **North Carolina's state model policy is due `2026-12-31`** with local policies `2027-06-30`, **Ohio's deadline has already passed**, and 🇨🇦 **Ontario has made "Cyber Safety and Artificial Intelligence" a mandatory `2026-27` Professional Activity topic with no province-wide policy** — `72` boards each needing their own. 🔵 **A triggered-tutoring deployment with a dosage dashboard and a rule log is the artefact that satisfies a board policy and shows an effect.**

### 🟢 `P794-2` — Purpose-built tutoring against the `63/16` gap, with the FRIA as the first deliverable · **EMEA** · 10–12 weeks

🟢 **`p794` finally has the EMEA demand number, and it is better than an adoption rate.** **`63%` of European teachers use AI; `16%` believe general-purpose AI improves learning outcomes** (Sanoma Learning European Teacher Survey 2026, `>20,000` teachers, `14` countries); **`52%` are asking for clear guidelines**; 🔴 **`10` of `23` ministries have a GenAI position at all.** 🔵 **A `47`-point gap between use and believed benefit is not a market to be educated — it is a market that has already tried the generic tool and rejected it.**

**The wiring**

1. **Lead with the obligation that is already in force, not the one that is deferred.** 🔴 **Art. 50 transparency has applied since `2026-08-02`; Art. 27 FRIA is required now; the Art. 5 emotion-recognition ban is live.** Annex III high-risk for education is **`2027-12-02`**. 🟢 **The FRIA is the paid first deliverable and the reason the rest of the engagement exists.** This base ships the marking and exposure scanners for Art. 50 at [`compose/code/aiact-50-2-marking/`](code/aiact-50-2-marking/) and [`aiact-50-2-exposure/`](code/aiact-50-2-exposure/).
2. **Platform: permissive, and now with the patent caveat measured.** [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) (**ECL-2.0**, `11,120 B`, `2d2098a91927`) or [`opencast/opencast`](https://github.com/opencast/opencast) (**ECL-2.0**, `11,340 B`, `66581567bcbb`) where lecture capture matters. 🔴 **Say this to the client's counsel, because no prior pass here said it:** ECL-2.0 is Apache-2.0 with **§3's patent grant narrowed** — for a contributor employed by an institution it reaches only patent claims where *the author is also the inventor* **and** the institution may grant under its research-funding agreements. 🟡 **Copyright permissions are identical to Apache-2.0; patent coverage is materially thinner, and these codebases are overwhelmingly university-contributed.** 🟢 Ship it; do not tell a procurement officer "it's basically Apache".
3. **Purpose-built, curriculum-aligned tutoring — the thing the `16%` figure says is missing.** [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) (Apache-2.0, `★58,596`) as the spine; align content to the national instrument rather than a generic syllabus — 🇮🇪 Ireland's *Guidance on AI in Schools*, 🇮🇹 Italy's Ministry of Education and Merit guidelines (November 2025), 🇫🇮 Finland's National Agency recommendations, and the Commission's **March 2026 AI-and-data-ethics teacher guidelines**.
4. **Evidence instrumentation is the deliverable that closes the belief gap.** Pre/post on a named objective set, dosage from `P794-1`'s metric list, and an effect estimate the institution can publish. 🔵 **Benchmark honestly against `0.06`–`0.14` SD, not against vendor claims** — a client who is told the realistic number and then beats it is a reference; one told `70%` improvement is a churn event.
5. **Sovereignty by default.** [`ollama/ollama`](https://github.com/ollama/ollama) or [`vllm-project/vllm`](https://github.com/vllm-project/vllm) on institution-controlled hardware; retrieval over institutional content only.
6. 🔴 **Do not build the credential layer on [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) without telling the client it is ARCHIVED** (`T901`, last push `2024-02-14`). 🟡 It is still the right vocabulary — a published model may legitimately freeze — but the client, not the engagement, should decide to depend on a read-only Commission repository.

🟢 **Why it closes:** the obligation is live, the belief gap is measured, and 🔴 **`22%` of Greek schools and `12%` of European schools on average have no AI rules at all** — so the governance artefact has a buyer even where the tutor does not yet.

### 🟢 `P794-3` — NCERT Classes III–VIII AI-curriculum delivery at national scale · **APAC 🇮🇳** · 10–12 weeks

🟢 **Writable for the first time: `p793-D` reached the Indian instrument, and it is a curriculum mandate rather than a statute.** **NCERT, with CBSE, has introduced a dedicated Computational Thinking and AI curriculum for Classes `III`–`VIII` from the `2026-27` academic year; the Grade `9`–`12` AI curriculum is finalised.** Governance is named: an **NCERT textbook-development team for Classes `11`–`12`**, a **CBSE expert committee chaired by Prof Karthik Raman (IIT Madras)**, and the **Department of School Education and Literacy** coordinating CBSE, NCERT, **KVS**, **NVS** and state/UT departments under an **"AI for Public Good"** framing. 🔴 **Wording discipline: the primary release says "introduced", not "mandatory"** — do not put "mandatory" in a proposal.

**The wiring**

1. **Content spine mapped to the curriculum, stage by stage** — Classes III–V interactive and concrete, VI–VIII computational thinking, IX–XII the finalised AI subject track. Deliver against NCERT/CBSE structure, not a generic AI-literacy syllabus.
2. **Generation at curriculum scale, permissive and APAC-origin.** [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) — **MIT root, `1,065 B`, `76abc5f13261`, `★43,389`**, `4,388`-file tree. 🔴 **Carry `p793`'s tree finding into procurement: the root grant is not the tree's grant** — `TREE[MIT root + LGPL + ARPHIC-PL + OFL + bespoke-CN font]`. 🟡 The font grants travel with the artefact; keep the notices.
3. **Multilingual delivery is the hard part and the differentiator.** KVS and NVS span every state language. 🔵 Build the content pipeline language-parameterised from day one — and note this base's own lesson: 🔴 **[`SoukhyadP991/Multilingual-NCERT-Doubt-Solver`](https://github.com/SoukhyadP991/Multilingual-NCERT-Doubt-Solver) is ungranted**, so the obvious head start cannot be used until its author grants a licence.
4. **Offline-first for the schools that need it most.** [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT) — and `p793`'s audit is the procurement answer: core is clean, `0` GPL-family across `208` locked runtime packages, 🔴 **with the residual risk confined to one plugin (`perseus_viewer`, via `@khanacademy/mathjax-renderer@3.0.2`, which ships with no grant).** 🟢 Drop that plugin or replace the renderer.
5. **Teacher-facing tooling, grade reserved to the teacher** — the same gate as every other jurisdiction in this base, and the one that makes the deployment portable.
6. **Assessment-integrity material** rather than detection theatre; task-redesign guidance travels better than a classifier.

🔴 **Honest scoping note:** this pattern is built from the curriculum instrument and verified supply. 🔴 **No Indian procurement document was reachable** (`T906`), so pricing, tender route and state-level purchasing remain unmodelled — the named next channel is state tender portals.

### 🟢 `P794-4` — Institutional agent fleet with the evaluation layer the sector is missing · **LATAM 🇨🇱 🇧🇷 🇨🇴** · 8–10 weeks

🟢 **`p794` found LATAM's reference deployment, and its own stated gap is the engagement.** **Pontificia Universidad Católica de Chile runs `194` pedagogical agents across nearly `100` courses** — 🔴 **and is still expanding its measurement of learning outcomes.** 🔵 **Scale is proven in Spanish; effect is not.** The same gap appears verbatim in Singapore (the minister said MOE lacks outcome data) and region-wide (`9%` evaluation coverage).

**Why LATAM first:** 🟢 **teacher adoption leads the world** — 🇧🇷 `56%` · 🇨🇱 `55%` · 🇨🇴 `53%` · 🇨🇷 `52%` against `41%` for reference countries (IADB **Nota CIMA 37**, from TALIS 2024) — 🟢 **AI training ranks first among PD needs in Chile and Costa Rica and second in Brazil and Colombia**, and 🔴 **there is no AI-in-education statute in Brazil, Mexico or Chile.** 🔵 **No deadline to sell against means the sale must be made on evidence, which is precisely what is absent.**

**The wiring**

1. **Fleet management before fleet expansion.** `194` agents across `100` courses is already past the point where per-course prompt maintenance works. 🟢 Model each agent as a versioned configuration — objective set, tool scope, escalation rule, owner — in one registry, and make the registry the deployment unit.
2. **Evaluation harness as the primary artefact.** Per-agent: objective coverage, dosage (`P794-1`'s metric list), escalation rate to a human, and a pre/post instrument per course. 🟢 **Report in SD against the `0.06`–`0.14` benchmark** so the institution's result is interpretable and publishable.
3. **Orchestration, permissive.** [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) (MIT, `★44,865`) or [`huggingface/smolagents`](https://github.com/huggingface/smolagents) (Apache-2.0, `★30,336`) for the lighter agents.
4. **A Spanish-language, curriculum-anchored reference already exists and is permissive.** [`goyanedelv/paes-mcp`](https://github.com/goyanedelv/paes-mcp) — 🟢 **MIT, in Spanish (`"Se concede permiso, libre de cargos"`), `2,018 B`** — Chile's PAES as an MCP server: the model for anchoring an agent to a national assessment rather than to a generic subject.
5. 🔴 **Licence trap to avoid, measured this pass.** [`luscitiosus/Dirigo`](https://github.com/luscitiosus/Dirigo) looks like a Spanish school-leadership regulation asset and 🔴 **it is `CC BY-NC-SA 4.0`, NonCommercial, stated in Spanish** (`T902`) — barred in a paid engagement, and an English-only licence probe grades it `CC-BY-4.0`. 🔵 **In this region, read the licence in the language it was written in.**
6. **Analytics, with the copyleft named.** 🔴 [`metabase/metabase`](https://github.com/metabase/metabase) is **AGPL-3.0 on the bytes** (`★50,301`, and GitHub's classifier says `NOASSERTION`) — 🔴 **AGPL §13 reaches a hosted service, which is how this would ship.** 🟢 Deploy it as a separate service the institution operates, or use [`jupyter/notebook`](https://github.com/jupyter/notebook) (BSD-3-Clause, `★13,464`) for the evaluation reporting instead.
7. **Teacher-pipeline tie-in where it is funded.** 🇨🇱 **"Futuros Docentes en IA"** (March 2026 — Ministerio de Ciencia with CRUCH, UMCE, CENIA, Kodea) is installing AI capability in CRUCH universities running teacher-education programmes. 🟢 **An evaluation harness is a natural contribution to a consortium whose purpose is capability, and it is the cheapest route to a public reference.**

🔵 **Why this is the region's clearest unclaimed offer:** every other region is buying governance against a deadline. 🟢 **LATAM has adoption, no deadline, a `194`-agent reference deployment and `9%` evaluation coverage — so the product is proof, and nobody is selling it.**

---
## 🆕 `p793` — **two patterns, both named to artefacts measured this pass**

### 🟢 `P793-1` — Certify an education MCP deployment into the systems of record · **North America first (Canvas), ports to EMEA** · 8–10 weeks

🔴 **The opportunity `p792-D` identified, re-aimed after measurement.** The premise was "no LMS vendor ships an official MCP server, community servers hold tokens that reach student records, and no independent evaluation exists". 🟢 **Two of three hold. The third does not:** [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT) already ships an audit trail with identifier masking, code-hash logging, three deployment overlays and its own security reviews. 🔵 **So the engagement is not "your server is insecure" — it is "your controls are designed and explicitly unwired, and an institution cannot pass Annex III on a placeholder."** That is both truer and easier to sell.

**What you are handed, and what is actually missing**

| Designed and present | 🔴 Declared but labelled *"pending feature wiring"* / *"placeholder"* |
|---|---|
| `core/audit.py` — `log_data_access`, `log_code_execution`, `log_access_change`, `_sanitize_endpoint` ID masking | `MCP_CLIENT_AUTH_MODE=api_key_or_mtls` · `MCP_CLIENT_API_KEY_REQUIRED=true` · `MCP_CLIENT_CERT_AUTHORITY` (`enterprise.env`) |
| `core/access/tokens.py` — HMAC client tokens (`oid`/`jti`/`exp`) | `TOKEN_STORAGE_BACKEND=keyring` (`public.env`) |
| Sandbox with `TS_SANDBOX_BLOCK_OUTBOUND_NETWORK=true`, enterprise host allowlist | `LOG_REDACT_PII=true` (*"some flags are placeholders"*) |
| `scripts/rotate-canvas-token.mjs`, security CI | 🔴 **Per-tool authorisation above an account-scoped Canvas token — does not exist and cannot, at the Canvas API** |

**The wiring**

1. **Pin the base.** `vishalsachdev/canvas-mcp` at a read sha; `1,071 B` MIT grant verified — no licence negotiation.
2. **Finish the three placeholder paths** as the project's own comments specify: client API-key *or* mTLS enforcement, keyring-backed token storage, and a real `LOG_REDACT_PII` implementation with a test that fails when a student identifier reaches a log line.
3. **Add the layer Canvas cannot give you.** The upstream token is account-scoped, so put a **per-tool allowlist and a role gate in front of the server**: deny `bulk_grade_submissions` and `get_student_submission` by default; enable per course, per role, per time window. 🟢 This is the control that makes the account-scoped token survivable.
4. **Reserve the grade to a named human.** `bulk_grade_submissions` is Annex III point 3. Wire it as *propose → named human decides → system proves it* — the architecture `P787-1` established and every jurisdiction that regulates at all accepts.
5. **Produce the evidence pack**: FRIA (Art. 27, 🔴 **already required**, not deferred), the audit-log schema with the masking rules, token lifecycle and rotation runbook, FERPA and GDPR data-flow maps, and the Annex III technical documentation for **`2027-12-02`**.
6. **Extend the same frame to the second server**: `Yuanpeng-Li/gradescope-mcp` (MIT) on the assessment side.

🟢 **Why it closes:** the client already runs Canvas, staff are already pointing MCP clients at it, and the credential in play is account-scoped. 🔵 **The deliverable is a certified deployment plus the Annex III evidence pack — repeatable across every Canvas institution, and the 13-month runway is the deadline that funds it.**

### 🟢 `P793-2` — Provincial AI-curriculum delivery against China's five-ministry Action Plan · **APAC 🇨🇳** · 10–12 weeks

🟢 **The first `P79x` pattern this base can write for China**, because `T898` finally reached the instrument: **《"人工智能+教育"行动计划》, 教科信〔2026〕1号**, issued jointly by 教育部 · 国家发展改革委 · 工业和信息化部 · 科技部 · 国家数据局, signed `2026-04-02`.

**Why it is a programme and not a pilot:** the Plan writes AI education into **local** curriculum systems, with each locality issuing its own course guide specifying objectives, content and **class-hour requirements** — so procurement is provincial and there are many buyers, against one national instrument. It also commits to strengthening K-12 AI education bases, to supporting **rural and remote** schools through the national platform, to revising the compulsory-education and senior-secondary information-technology curriculum standards, and to drafting **人工智能应用安全评估指标 (AI application security assessment indicators)**. Target: deep AI–education integration by **2030**.

**The wiring**

1. **Content spine against the national guideline.** Map deliverables to 《中小学人工智能通识教育指南》 and 《中小学生生成式人工智能使用指南（2025年版）》 by stage, with the class-hour structure the provincial guides require.
2. **Agent layer, permissive and APAC-origin — no licensing negotiation.** [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) (MIT, `1,065 B`, `76abc5f13261`) for generated interactive classrooms with AI teachers and peers; [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) (Apache-2.0, `11,408 B`, `ae1dbfc5e74c`, **`58,585★`**, pushed `2026-11-07`) for lifelong-memory tutoring. 🔵 Both Chinese-origin, which is a procurement advantage here rather than a neutral fact.
3. **Delivery to rural and remote schools: offline-first.** [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT) — and `p793` has the licensing checklist for it: core is clean, `0` GPL-family in `208` resolved runtime packages; if Perseus exercises are in scope, carry the `mathquill` MPL-2.0 notice and resolve `@khanacademy/mathjax-renderer@3.0.2`, which ships with **no grant** (`T896`).
4. **Teacher-facing tooling** against 《教师生成式人工智能应用指引》, with the grade reserved to the teacher — the same gate as every other jurisdiction.
5. 🔴 **Build the security-assessment evidence now, before the indicators land.** 人工智能应用安全评估指标 is in draft; a vendor that can already evidence data flows, logging and human-decision points is positioned when it issues. 🟢 **This is the earliest-mover item in the pattern.**

🔵 **Honest scoping note:** this pattern is built from the ministry instrument and this base's verified supply. It does **not** include a data-residency or ICP/filing analysis, which a real engagement in this market needs and this base has not measured.

### 🔴 Still unwritable, and why — `p792-E` discharged for `1` of `4`

🟢 China placed at ministry level with a document number. 🔴 **India, Australia and Singapore remain unplaced at ministry level**, so no `P79x` pattern can be written for them. What `p793` reached is national AI regulation, not education-ministry procurement: 🇰🇷 Korea's AI Basic Act **in force `2026-01-22`** with a "high-impact AI" category; 🇯🇵 Japan's AI Promotion Act (in force `2025-06-04`, **no penalties**) plus a new Cabinet AI Basic Plan; 🇸🇬 Singapore with **no binding AI statute** and IMDA's Model AI Governance Framework for Agentic AI (`2026-01-22`) plus AI Verify; 🇮🇳 India signalling dedicated AI legislation in July 2026, with AI-content labelling rules already applying. 🔵 **The named gap is procurement and curriculum documents from the education ministries of India, Australia and Singapore — and the channel that works is the in-language query, proven four passes running.**

## 🆕 `p792` — **four patterns, each named to repos verified this pass**

🔵 **Rule 1, carried and now narrower:** in education the platform a client already runs is almost always copyleft, so AI code lives at its edge. 🟢 **`p792` adds Rule 1a: the edge can be an MCP server, and the MCP server can be MIT even when the platform is AGPL.** 🔴 **Rule 2, strengthened by `T884`:** before you embed anything, resolve its **lockfile** — a licence read at `latest` is not the licence you ship.

### 🟢 `P792-1` — Canvas-native grading and course-ops agent (North America, higher ed)

**The engagement shape:** a university runs Canvas; faculty want grading help and course operations; IT will not accept code inside an AGPL LMS.

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Way in | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 MIT `1,071 B` | Canonical Canvas MCP: courses, assignments, submissions, grading, announcements as tools. **Calls Canvas, never links it** — the AGPL stays on the far side of the boundary |
| Grading logic | [`omerfarooq223/AutoGrader-Agent`](https://github.com/omerfarooq223/AutoGrader-Agent) | 🟢 MIT `1,077 B` | Rubric-driven grading + feedback generation. 🔴 `★3` — **fork it, read it, do not depend on it** |
| Rubric source | [`Yuanpeng-Li/gradescope-mcp`](https://github.com/Yuanpeng-Li/gradescope-mcp) | 🟢 MIT `1,068 B` | Only if the client also runs Gradescope. 🔴 `★8` — reference shape |
| Design method | [`XiucuiGuan/addie-instructional-designer`](https://github.com/XiucuiGuan/addie-instructional-designer) | 🟢 MIT `1,099 B` | Gives the deliverable the **ADDIE** vocabulary the client's instructional designers already specify work in |

**Wiring.** Canvas MCP runs as a service with a **scoped** institutional token — not an admin token. The grading agent reads submissions and the rubric through MCP tools, proposes a grade and feedback, and **writes nothing back without a human action**; Canvas's own gradebook stays the system of record. Keep the agent in its own process so its licence is yours to choose.

🔴 **The part that is actually the sale, and it is not the agent.** An MCP server holding a Canvas token reaches **student records** → **FERPA**. No independent security or data-governance evaluation of *any* education MCP server has been published. 🟢 **Deliverable: token scoping, per-tool allowlisting, audit logging of every tool call, and a data-protection review — before the first grading run.** Budget it as a named workstream, because the client's counsel will ask and nobody upstream has an answer. **Estimate: 6–8 weeks**, of which ~2 are governance.

### 🟢 `P792-2` — Cited-answer tutor on the client's own curriculum (Global; the answer to the evidence problem)

**The engagement shape:** the client has been told "AI tutor" and is sceptical, because **only `45 %` of the most-used edtech tools have ESSA-tier published evidence** and the chatbot-as-tutor pitch is visibly fading.

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Spine | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 `11,408 B` · `★58,575` | The strongest permissive tutoring platform in the sector, actively pushed |
| Citation architecture | [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | 🟡 `TREE[MIT + MIT + OFL]` | **Course-scoped RAG with per-lesson citations** — read it for the scoping design, which is the part that answers *"where did the tutor get this?"* |
| Lessons engine | [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 `11,358 B` | 🟢 **Newly available (`T884`)** — interactive lessons that behave like tutoring. Pin `angular-shepherd@11` and `shepherd.js@8`; **gate the major bump in CI** |
| Offline reach | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT `1,097 B` | Where connectivity is the binding constraint. 🟡 Two LGPL packages — keep them replaceable, source available |

**Wiring.** Ingest the client's *own* curriculum as the only retrieval corpus. Every tutor answer carries a **per-lesson citation into that corpus**, and an answer with no citation is a refusal, not a guess. `oppia` supplies the practice loop; mastery state drives what the tutor teaches next.

🔴 **Two deliverable rules.** *(1)* 🟡 **Carry the OFL file** and keep font names intact — Study-Mate ships KaTeX fonts under SIL OFL (`4,616 B`), and KaTeX turned up in **three** repositories this pass, so assume it is present (`T889`). *(2)* 🔴 If the Python service is **distributed** rather than hosted, `oppia`'s `mutagen==1.47.0` is **GPL-2.0-or-later** and direct — replace it or carry copyleft at that boundary. `requirements.in` has `29` direct entries, so substitution is bounded. **Estimate: 8–10 weeks.**

### 🟢 `P792-3` — EU AI Act high-risk conformity runway for an education deployment (EMEA)

**The engagement shape:** an EMEA education client has an AI system in or near production and a **hard date**.

🟢 **The date is settled (`T888`): high-risk obligations, education included, apply from `2027-12-02`** — deferred by the Digital Omnibus (political agreement `2026-05-07`). 🔴 **From today that is roughly `13` months.** The deferral is a selling window, not a reprieve.

| Step | What it produces | Built with |
|---|---|---|
| 1. Classify | A written determination of whether the system is high-risk, and why. Education uses that score, assess or admit are the ones that land in scope | The client's own use cases against the Act's education heading |
| 2. Human oversight | A reviewable decision point for every consequential output, with the human action logged | 🟢 The `P792-1` boundary: the agent **proposes**, the gradebook records a human act |
| 3. Provenance | Per-answer citations into a known corpus, retained and auditable | 🟢 `Study-Mate`'s citation scoping; `DeepTutor` as the spine |
| 4. Technical documentation | Dependency and grant inventory **resolved from lockfiles**, per `T884` | 🟢 `yarn.lock` / `requirements.txt` resolution, npm + PyPI per-version licences |
| 5. Pedagogical control | Evidence that pedagogy governs the system, not the model | 🔵 OECD *Digital Education Outlook 2026*; EU Council conclusions on teachers in the AI era (`2026-05-11`); Eurydice (`2026-09-22`) |

🟢 **The strongest argument available to this engagement is a real one, and it is `T888`'s South African case**: a government **withdrew its own national AI policy** (Notice `3978` of `2026`, Gazette `54840`, `2026-06-12`) because the draft contained **AI-hallucinated references**. 🟢 **Verification discipline is not a technical nicety — it is the thing whose absence retracted a national policy.** **Estimate: 10–12 weeks**, run in parallel with the build, not after it.

### 🟢 `P792-4` — Ministry-programme delivery against a named instrument (APAC 🇰🇷 · LATAM 🇨🇴)

**The engagement shape:** a public-sector education buyer whose obligations come from a document with a number. 🔵 **This pattern exists because `T891` keeps proving that the instrument is findable only in the local language** — and a proposal that cites it by number is a different proposal.

| Region | The instrument to cite | The deliverable it creates |
|---|---|---|
| 🇰🇷 **APAC** | **MOE personal-information management standards** for learning-support software selected as 교육자료 (**July 2026**); the **16 AI subjects** programme (**August 2026**, teacher-led, 교육자료 → 인정교과서, with MSIT and 10 provincial offices); AIDT expanding toward 2028 | 🟢 A **privacy-compliance and teacher-workload** deliverable. 🔴 Teachers' organisations publicly criticised the standards for shifting responsibility and workload onto teachers — **that grievance is the scope**: tooling that discharges the standard *without* adding teacher work. 🔵 Programme scale reported at **₩1.4tn** and **4.83M students' data** |
| 🇨🇴 **LATAM** | **CONPES 4144 de 2025** (national AI policy); **Directiva 01 of `2026-03-05`** (safe, ethical, inclusive, pedagogical ICT/AI integration in schools); the **Decálogo de IA para la Educación Superior** | 🟢 Close the **`92 %` use / `30 %` published-policy** gap: an institutional AI-use policy written against the Decálogo and Directiva 01, plus the tooling to evidence compliance. 🔵 **Latam-GPT** (UNESCO–CENIA) is the sovereignty-flavoured model option the region is asking for |

**Wiring, both regions.** Same technical spine as `P792-2`. 🟢 **What changes is the artefact set**: the proposal cites the instrument by number, the audit log is shaped to what that instrument asks to see, and the model choice answers a sovereignty question rather than a benchmark. 🔴 **Do not reuse an English-language regional summary for either** — both countries' operative documents exist only in their own language, and `p791` ran an English LATAM leg and got institutional structure instead of ministry policy. **Estimate: 6–8 weeks** per country, the ministry-document reading being the first week.

🔴 **Declared gap on this pattern:** **China, India, Australia and Singapore have no ministry-level instrument placed in this base**, so `P792-4` cannot be written for them yet. 🔵 **Cost to fix: one in-language leg per country** — the channel is now proven three times (`NCERT`, `학습 튜터`, Spanish-language Colombian ministry vocabulary).


## 🆕 `p791` — three recipes, and `Rule 4`

🔴 **Rule 4, NEW this pass (`T882`).** Rule 2 says read the dependencies. **Rule 4 says read the TREE, in every language it is written in.** A root `LICENSE` governs the root. `THU-MAIC/OpenMAIC` is MIT at the root and ships an **LGPL** package plus **three font grants**, one of them a non-OSI Chinese-language licence forbidding renaming and resale-as-product. Before any repository is handed to a client, enumerate it and grade every grant found:

```bash
git clone --filter=blob:none --no-checkout --depth 1 https://github.com/OWNER/REPO /tmp/x
git -C /tmp/x ls-tree -r --name-only HEAD | grep -iE 'licen|copying|legal|terms|notice'
git -C /tmp/x cat-file -p HEAD:PATH        # lazily fetches only that blob
```

🔵 **And `Rule 5`, from `T880`:** `NOASSERTION` on a licence API is **not** a verdict. It means the matcher failed, which happens both when there is no grant (`frappe/education`, `19 B`) and when there is a perfectly good one (`Gego-K12/gegok12`, `1,150 B` MIT defeated by an HTML comment and curly quotes). **Read the bytes.**

---

## `P791-1` — Vietnam high-risk conformity for automated assessment · **APAC 🇻🇳 first** · 10–12 weeks

🔴 **Why this exists.** Vietnam's **Law on Artificial Intelligence** (in force `2026-03-01`) is the only instrument this base has found that **names education as high-risk and names automated assessment and behavioural monitoring inside it**. Compliance lands `2027-03-01` (six-month grace for systems already running; one source says September 2027). **The clock is real and the work is now.**

| Layer | Repository | Grant | Role |
|---|---|---|---|
| Tutoring spine | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | Learner interaction; patent grant matters for a regulated deliverable |
| Marking, human-reserved | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 · `0/18` deps copyleft (`T861`) | Autograding where the **grade is proposed, never written** |
| Policy boundary | [`csev/tsugi`](https://github.com/csev/tsugi) | 🟢 Apache-2.0 | LTI process boundary into Moodle/Canvas without inheriting copyleft |
| Orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 MIT | **One policy node per jurisdiction** — the shape that survives six APAC regimes |

🟢 **Wiring.** `tsugi` exposes the agent as an LTI tool to the institution's LMS, so no copyleft reaches client code. `langgraph` holds a **jurisdiction node** evaluated before any assessment action: it decides whether automated marking is permitted, whether a human must confirm, and what must be logged. `nbgrader` computes a **proposed** grade; the teacher commits it. `DeepTutor` never sees the gradebook.

🔴 **The two conformity artefacts that are the actual deliverable:** (a) an **immutable decision log** — every automated assessment action, its inputs, the policy node's verdict, and the human who confirmed it; (b) a **behavioural-monitoring register** stating what is *not* collected, because the statute names monitoring and the cheapest way to comply is to be able to prove absence. 🔵 Sell the log, not the tutor.

---

## `P791-2` — Institutional AI governance made operational · **LATAM 🇧🇷 🇲🇽 first** · 6–8 weeks

🔴 **Why this exists.** LATAM's measured gap is not capability, it is governance: **`87%` of institutions use AI, `26%` have a strategy; `92%` of students and `79%` of faculty already engage with it; in Brazil `53%` of administrators use AI and `22%` of schools have guidelines.** 🟢 **Shipping another tutor addresses nothing. The unmet need is a policy that is enforced rather than published.**

| Layer | Repository | Grant | Role |
|---|---|---|---|
| Platform (already deployed) | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 — **boundary only** | System of record; untouched |
| Boundary | [`csev/tsugi`](https://github.com/csev/tsugi) | 🟢 Apache-2.0 | LTI tool; client code stays the client's |
| Course-scoped tutor | [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | 🟢 MIT · `1,064 B` | 🟢 **Its per-lesson citation scoping is the governance primitive** — it answers *"where did this come from?"* per answer |
| Policy engine | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 MIT | Acceptable-use rules as a graph, **swappable per country** |
| Evidence | [`metabase/metabase`](https://github.com/metabase/metabase) | 🟡 split-by-directory (read which part) | Disclosure and usage reporting for the rectorate |

🟢 **Wiring.** The institution's acceptable-use policy is authored as **configuration, not prose**: per course, whether AI assistance is permitted, whether it must be disclosed, and whether it may touch credited work. `langgraph` enforces it at request time; `Study-Mate` serves answers **with citations scoped to that course's own materials**, which is what makes a disclosure claim checkable; `metabase` produces the per-faculty report that turns `26%`-have-a-strategy into `100%`.

🔴 **Brazil and Argentina must be separate policy bundles from day one** — Brazil is converging on an EU-style framework and signed a Brazil–EU agreement (June 2026) while Argentina's executive has backed keeping AI unregulated. 🔵 Same product, two bundles; `Ceibal` and `Latam-GPT` are the references that open the public-sector conversation.

---

## `P791-3` — Offline-first, teacher-facing AI under a curriculum mandate · **Africa 🇰🇪 🇳🇬 first** · 8–10 weeks

🔴 **Why this exists, and why it is NOT a tutor.** Kenya's **National AI Strategy 2025–2030** and Nigeria's **NERDC directive** create a curriculum mandate; every source on the continent names the same binding constraint — **teacher capacity, electricity, connectivity and devices**, not model quality. 🔴 **A cloud-only student chatbot fails here for reasons unrelated to AI.**

| Layer | Repository | Grant | Role |
|---|---|---|---|
| Offline spine | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT · 🟡 `2` LGPL of `32` deps | Runs without connectivity; syncs opportunistically. The one proven offline platform in this base |
| School system of record | [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | 🟢 **MIT** · `1,150 B` | 🟢 **Permissive, so the agent can be an in-process module** — no LTI boundary needed (`p791`, `T880`) |
| Lesson generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🟢 MIT · `★388` | Document-to-course generation, run **batch and offline**. 🔴 Present it at its real size, not the `~12k★` this base once published (`T881`) |
| Local inference | `ollama` | 🟢 MIT | On-premise model; no per-token cost, no connectivity dependence |

🟢 **Wiring.** Generation happens **where the power is** — a district office or teacher-training centre — not in the classroom: `educhain` turns syllabus documents into lesson material in batch, output is packaged into `kolibri` channels, and schools sync by whatever means they have, including sneakernet. The agent inside `gegok12` is **teacher-facing**: it drafts lesson plans, assembles differentiated worksheets and prepares marking schemes. 🟢 **Because `gegok12` is MIT and its one vendored dependency is MIT, that agent ships as a module inside the system of record** — the only place in this base where that is licensing-clean for an SIS.

🔵 **The deliverable is teacher time, measured.** Baseline the hours a teacher spends on planning and marking, then report the delta. Against the constraint every African source names, that number is the business case — and it is the same number whether or not the connectivity ever arrives.


# Compose patterns — `p790`

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

## `P790-1` — BNCC lesson planning + AI-assisted marking with the grade RESERVED to the teacher · **LATAM 🇧🇷 first** · 8–10 weeks

🔴 **Why this exists now and not next quarter.** `Parecer CNE/CP nº 15/2026` was homologated
`2026-11-10` (`DOU` `2026-11-11`, reported) and gives Brazilian institutions **`12` months to
adapt** — so roughly **`2027-11-10`**. It **permits** AI-assisted correction of essays and
dissertative questions and **reserves the mark to the teacher**; bars penalising a student on an
AI-detector output alone; and bars unsupervised AI use **up to `5º ano`**. 🟢 **That is a
human-in-the-loop mandate, not a ban — and it is a specification.** `T876`.

🟢 **Every component below is byte-verified on this base.**

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Lesson planning | [`iagommendes/bncc-lesson-generator`](https://github.com/iagommendes/bncc-lesson-generator) | 🟢 MIT `1,068 B` · `171e1db7278e` | **BNCC**-aligned plans from an ordinary form — **`zero-prompt para o professor`**, which removes the adoption barrier that kills teacher tooling |
| Marking assist | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 `1,512 B` | 🟢 **The cleanest audited component in this base** — `0`/`18` copyleft at layer 1. 🟡 Layer 2 adds MPL-2.0 (`certifi`) and LGPL-2.1 (`paramiko`), **neither triggered by this deployment** (`T872`) |
| Mastery / adaptivity | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT `1,105 B` | Bayesian Knowledge Tracing, and **`0` of `43` direct dependencies are copyleft** |
| Compliance input | [`ciro-maciel/awesome-ia-sala-de-aula`](https://github.com/ciro-maciel/awesome-ia-sala-de-aula) | 🟢 **CC0-1.0** `7,049 B` | Classroom AI tools **with each one's minimum age and privacy posture and the Brazilian rules that apply** — the `5º ano` age gate has a source, not an assumption |
| Policy agent | [`jinlize-tech/edu-ai-usage-policy-agent`](https://github.com/jinlize-tech/edu-ai-usage-policy-agent) | 🟢 Apache-2.0 `11,358 B` | 🟡 **Reference only** — `0/130` platform-validated by its own README (`T878`). Take the shape, write the code |
| Evidence trail | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) + [`xapi-validation`](https://github.com/LearningLocker/xapi-validation) | 🟢 MIT `1,070 B` each | Every suggestion, every teacher override and every final mark as a validated xAPI statement |
| FRIA evidence | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | 🟢 Apache-2.0 | Carries the same deliverable into an EMEA port |

### The wiring, and the one gate the whole pattern exists for

```
teacher form  ──>  bncc-lesson-generator  ──>  lesson plan (A4/PDF)
                                                    │
student work ──>  nbgrader  ──>  AI first-filter ──> SUGGESTED score + rationale
                                                    │
                                        ┌───────────┴────────────┐
                                        │  🔴 TEACHER DECISION   │  <-- the mark is assigned HERE
                                        │  (no default, no       │      and nowhere else
                                        │   auto-accept, no      │
                                        │   timeout-to-approve)  │
                                        └───────────┬────────────┘
                                                    │
                            xapi-service  <─────────┴──> OATutor (mastery update)
                                   │
                            validated statement: suggestion, override, final mark, actor, timestamp
```

🔴 **Three implementation rules that are the difference between compliant and not:**

1. 🔴 **No auto-accept and no timeout-to-approve.** A suggested score that becomes final because
   nobody clicked is an **AI-assigned mark**. The teacher action must be affirmative and recorded.
   🔵 `schoolflow-agent`'s human-approved schedule gate is the design precedent in this base.
2. 🔴 **AI-detector output must not reach any disciplinary path.** Brazil bars penalising a student
   on a detector alone. 🟢 **The safe build is not to ship a detector in this pipeline at all** —
   the risk is unbounded and the regulatory upside is zero.
3. 🔴 **Age gate at `5º ano`.** Student-facing AI must be off, not merely supervised, for educação
   infantil and anos iniciais. 🟢 The *teacher*-facing half of the pattern (planning, marking assist)
   is unaffected by the age rule, which is why it is the half to deliver first.

🟢 **Why it is defensible commercially:** `P788-1` sold "defensible AI grading" on a US/EMEA audit
argument. 🟢 **In Brazil the audit trail is now a dated legal requirement with a deadline**, and the
pattern's weakest commercial feature — that the teacher still does the work — **is the compliance
feature.** 🔴 Vendors leading with autograders cannot sell into Brazilian basic education at all.

🔵 **Ports, with the change named each time:** 🇺🇸 **Florida** (AI barred on graded work *unless the
instructor allows* → the same affirmative-action gate, instructor-scoped) · 🇺🇸 **New York A 9190**
(grade-9 gate instead of `5º ano`) · 🇪🇺 **EMEA** (Annex III assessment, reported `2027-12-02`, plus
**Art. 50 transparency already in force since `2026-08-02`** — so the disclosure UI ships first) ·
🇰🇷 **Korea** (AI Basic Act in force `2026-01-22`, automated assessment in the high-impact category).
🟢 **One gate, five jurisdictions** — `T853`/`T854` is now a product decision rather than an
observation.

🔴 **Stated limits.** The `DOU` text was **not read** (two research hosts do not resolve in this
session), so the `2026-11-10` date and the `12`-month window are **reported, not verified**
(`ACTION p790-C`). `bncc-lesson-generator` is `0★` and single-contributor — **fork it, do not depend
on it.** And its MIT grant covers its code: **it makes no claim about the BNCC**, which is a public
MEC instrument, and `0` of this pass's `5` new permissive rows carry a scope clause either way
(`T864`).

## `P789-1` — School-operations agent: timetable disruption and substitution, with an approval gate · **North America + EMEA first; APAC-portable** · 8–10 weeks

🟢 **The pattern `p788` could not write, because the category had no permissive row. It has five now
(`T874`), and they agree about architecture: a real constraint solver with an LLM at the edges and a
human gate before any write.** 🔵 Nobody in this category asks a language model to produce a
timetable — a plausible-looking timetable is a school day that does not work.

| Component | Address | Grant | Role |
|---|---|---|---|
| **Solver core** | [`paoloantinori/school-timetable-timefold-case-study`](https://github.com/paoloantinori/school-timetable-timefold-case-study) | 🟢 MIT · `1,081 B` · `12e2a597e655` | 🟢 **Timefold on Quarkus** — the reference wiring. Hard constraints stay hard |
| Solver alternative | [`Nayak-indie/Timable`](https://github.com/Nayak-indie/Timable) | 🟢 Apache-2.0 · `11,357 B` · `c71d239df917` | **OR-Tools** + Streamlit, if the client is Python-shop rather than JVM |
| **Disruption agent** | [`Zahraishag/schoolflow-agent`](https://github.com/Zahraishag/schoolflow-agent) | 🟢 MIT · `1,081 B` · `1b7481d92d0f` | 🟢 Absences and substitutions with **human-approved** schedule updates — the gate is the project's own design |
| MIS attachment 🇬🇧 | [`shan8851/classcharts-agent`](https://github.com/shan8851/classcharts-agent) | 🟢 MIT · `1,066 B` · `65ef4f07f833` | 🟢 **Read-only** against a live UK homework/behaviour system |
| LMS attachment 🇺🇸🇨🇦 | [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | 🟢 MIT · `1,200 B` · `a873478a6b4e` | D2L Brightspace over MCP |
| Orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 MIT · `1,072 B` | Stateful graph: detect → propose → **halt for approval** → write |
| Audit trail | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | 🟢 MIT · `1,070 B` | Every proposal and every approver stored as a validated statement |
| Adoption/safeguarding frame | [`VictorOsondu/ai-adoption-education`](https://github.com/VictorOsondu/ai-adoption-education) | 🟢 CC BY 4.0 content + MIT code · `752 B` | Safeguarding-first task-suitability guidance — the **policy** half of the deliverable |

**Wiring.** The MIS/LMS connector detects the disruption (absence, room loss) → `schoolflow-agent`
assembles the affected set → **the solver** (Timefold or OR-Tools) produces feasible substitution
options under the school's hard constraints → the LLM's only jobs are **translating plain-English
policy into constraints** and **explaining why an option was rejected** → LangGraph halts → a named
human approves → only then is the schedule written → the proposal, the options, the approver and the
timestamp go to the xAPI store.

🟢 **Why it sells:** it targets the one budget line every school already has — **cover and
timetabling staff time** — and it needs no change to assessment policy, which is where every AI
conversation in education currently stalls. 🔵 **Jurisdictional fit:** in the EU this is deliberately
*not* a high-risk system (it schedules staff and rooms, it does not evaluate students), so it ships
today under Article 50 transparency instead of waiting for `2027-12-02`. 🟢 In North America it is a
direct answer to the district AI-policy deadlines (Ohio `2026-07-01`, North Carolina `2027-06-30`).
🔴 **The caution to state in the proposal:** timetabling and attendance touch children's personal
data. The read-only attachment and the approval gate are not conveniences — they are what keeps this
category deployable. 🔴 **Ask upstream for** [`NSK-394/schoolbridge-mcp`](https://github.com/NSK-394/schoolbridge-mcp):
role-based agent access to school ERP data is the right control surface and it is ungranted.

---

## `P789-2` — Offline WAEC/NERDC exam-prep tutor for low-connectivity classrooms · **EMEA (West + Southern Africa)** · 8–10 weeks

🟢 **`P788-2` was the offline-first pattern built on components this base had to file as ungranted.
This is the same shape with the grants present** (`T871`), against real national examination boards.

| Component | Address | Grant | Role |
|---|---|---|---|
| **On-device tutor core** | [`thesavvybyjude/Offline-First-Android-AI-Tutoring-App`](https://github.com/thesavvybyjude/Offline-First-Android-AI-Tutoring-App) | 🟢 MIT · `1,070 B` · `a2fe733bd153` | 🟢 **The load-bearing row:** on-device LLM, RAG over the **WAEC/NERDC** curriculum, spaced repetition — already offline-first by design |
| Board coverage | [`nitoni-jim/ai-tutor-app`](https://github.com/nitoni-jim/ai-tutor-app) | 🟢 MIT · `1,074 B` · `d33e0685ea0f` | **WAEC / NECO / JAMB** in one tree — the three Nigerian boards |
| Third WAEC row | [`Ass-Gaye/waec-ai-tutor`](https://github.com/Ass-Gaye/waec-ai-tutor) | 🟢 MIT · `1,065 B` · `54383781845a` | Cross-check and component reuse |
| 🇿🇦 CAPS operations | [`Masondo86/homework-hero-sa`](https://github.com/Masondo86/homework-hero-sa) | 🟢 MIT · `1,070 B` · `88eb94d99d6c` | Homework scheduling and learner accountability for the South African port |
| 🇿🇦 CAPS content | [`daddysystem/nextgen-learn`](https://github.com/daddysystem/nextgen-learn) | 🟢 **BSL-1.0** · `1,338 B` · `c9bff7573892` | CAPS-following study material. 🔵 Boost — permissive, and *weaker* than MIT on attribution |
| **Offline delivery** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟡 MIT · `1,097 B` | Proven offline learning platform. 🔴 `T861`: LGPL at layer 1 — dynamic linking only |
| Mastery model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT · `1,105 B` | Bayesian Knowledge Tracing — audited clean at layer 1 |
| Device delivery without a store | [`elimu-ai/appstore`](https://github.com/elimu-ai/appstore) | 🟢 MIT · `1,065 B` | 🟢 APK delivery **without an app store** — the distribution problem this pattern actually has |
| Local inference | [`ollama/ollama`](https://github.com/ollama/ollama) | 🟢 MIT | Quantised small model on-device; no per-token cost, no connectivity assumption |

**Wiring.** Kolibri carries the curriculum packages and sync; the on-device tutor runs a quantised
model locally with RAG over the WAEC/NERDC corpus; OATutor's BKT turns attempts into a mastery
estimate that survives being offline; spaced repetition schedules the next session **on the device**;
`elimu-ai/appstore` distributes updates where Play Store access is unreliable; everything syncs
opportunistically when a connection appears.

🟢 **Why it sells:** it is priced against **cost per learner with no connectivity assumption and no
per-token bill**, and it targets national examinations that millions of families already pay for.
🔵 **Port to South Africa** by swapping the corpus for CAPS and adding `homework-hero-sa`; the
architecture is unchanged. 🔴 **Scope boundary, stated up front (`T864`):** these grants cover code.
**Past examination papers are the boards' copyright** — WAEC, NECO, JAMB and the South African DBE —
so a client engagement needs a content licence or must generate practice items rather than reproduce
past papers. **This is the single most likely way for this pattern to fail legal review.**
🔴 **Ask upstream for** [`7irelo/aptiverse`](https://github.com/7irelo/aptiverse) (CAPS practice with
**auditable marking**) and [`tosinamuda/teacher-agent-itu-hackathon`](https://github.com/tosinamuda/teacher-agent-itu-hackathon)
(**teacher-in-the-loop**, ITU AI for Good) — the two best-designed African artefacts found, both ungranted.

---

## `P789-3` — Japanese school-administration (`校務`) automation and curriculum alignment · **APAC 🇯🇵** · 6–8 weeks

🟢 **Japan is placed for the first time (`T870`), and the pattern follows the supply rather than the
assumption.** Japan is not publishing tutoring agents; it is publishing **school administration and
curriculum alignment**. 🔵 Selling a conversational tutor into a Japanese school is selling against
the grain of what its teachers are actually automating.

| Component | Address | Grant | Role |
|---|---|---|---|
| **Curriculum spine** | [`masa-san-jp/jp-k12-digital-ai-textbook`](https://github.com/masa-san-jp/jp-k12-digital-ai-textbook) | 🟢 MIT · `1,068 B` · `d7c583c9f444` | 🟢 All `12` grades aligned to the **next 学習指導要領** *and* the **UNESCO AI Competency Framework** — national and international alignment in one tree |
| **Staff enablement** | [`kumaken-1/school-office-generative-ai-30`](https://github.com/kumaken-1/school-office-generative-ai-30) | 🟢 **MIT `1,102 B`** (code) **+ CC BY 4.0 `925 B`** (content) | 🟢 `30` graded exercises on **real `校務` tasks**. 🔵 CC BY on the content means a client may **adapt and republish** the training material — commercially |
| Operations core | [`Zahraishag/schoolflow-agent`](https://github.com/Zahraishag/schoolflow-agent) + solver (`P789-1`) | 🟢 MIT / Apache-2.0 | Substitution and disruption handling, approval-gated |
| Orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 MIT · `1,072 B` | Approval-gated workflow graph |
| Local inference | [`ollama/ollama`](https://github.com/ollama/ollama) · [`vllm-project/vllm`](https://github.com/vllm-project/vllm) | 🟢 MIT / Apache-2.0 | On-premises serving — the default posture for Japanese public-sector data |

**Wiring.** The curriculum spine supplies the alignment vocabulary (grade, subject, competency); the
`校務` exercise set becomes the staff-training track and the task inventory of what to automate first;
the operations core automates the highest-frequency administrative tasks behind an approval gate;
inference runs on-premises.

🟢 **Why it sells:** Japan's **AI Promotion Act** is promotion-first and carries no penalty regime,
and the Cabinet's second-phase AI Basic Plan (`2026-07-14`) actively encourages adoption — so the
engagement is **not** a compliance project. It is **teacher workload**, in a country whose teacher
hours are a standing national issue, with adoption climbing fast from a low base (Microsoft: 56th in
H1 2025 → 48th in Q1 2026). 🔴 **And the resistance is real and rising:** Ipsos 2026 puts support for
banning AI in schools at `29%` in Japan, up from `21%`. **Lead with administrative relief for staff,
not with anything that touches instruction or assessment.**
🔴 **Two grant traps, both measured this pass.**
[`nahisaho/teacher-genai-playbook`](https://github.com/nahisaho/teacher-genai-playbook) is the most
engagement-shaped Japanese teacher-training artefact and it is **CC BY-NC 4.0 — unusable in a paid
engagement**. [`naritaroad/tracen-ai-tazuna`](https://github.com/naritaroad/tracen-ai-tazuna) is MIT
but an **unofficial *Uma Musume* fan project** — the grant covers the authors' code, never the
franchise's IP. 🔴 **Ask upstream for**
[`narumi-mase/osaka-lesson-dataset`](https://github.com/narumi-mase/osaka-lesson-dataset) — Osaka City
Education Center lesson plans, still ungranted after two passes.

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
