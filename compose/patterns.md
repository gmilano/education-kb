---
industry: education
region: Global
updated: 2026-10-27
---

## 🆕 `p485` — `2026-10-27` — **🔴 ONE RECIPE IS WITHDRAWN AND REPLACED: every pattern naming **Latam-GPT** is void — five repositories, four archived, **all five unlicensed**. 🟢 Its replacement is better anyway, because the region turns out to have 552 forks of deployed school software with no AI layer on it.**

🔵 Every component named below had its `LICENSE` fetched from `raw.githubusercontent.com` **this
pass**, or was cloned at a stated commit this pass or in `p484`. 🔴 Effort ranges remain
**uncalibrated estimates** (`Gap 483-Q`, `Gap 484-V`) — relative ordering, not quotes.

---

### 🔴 `P485-0` — WITHDRAWN: any recipe naming Latam-GPT as a component

🔴 Prior Globant-side patterns named **Latam-GPT** as the LATAM building block. Measured this pass:

| repository | ★ | archived | licence |
|---|---|---|---|
| `latam-gpt/llm-data-eval` | 16 | 🔴 YES | 🔴 **NO LICENCE FILE** |
| `latam-gpt/toxicity-classifier` | 5 | 🔴 YES | 🔴 **NO LICENCE FILE** |
| `latam-gpt/language_identifier` | 3 | no | 🔴 **NO LICENCE FILE** |
| `latam-gpt/fasttext-classifiers` | 0 | 🔴 YES | 🔴 **NO LICENCE FILE** |
| `latam-gpt/training-estimations` | 2 | 🔴 YES | 🔴 **NO LICENCE FILE** |

🔴 **Absent a licence, default copyright applies — all rights reserved.** None of it can be built on,
regardless of intent, and four fifths is frozen. What exists is data-pipeline tooling, not a model or
an education product. 🔵 The recipe is withdrawn rather than patched, and `P485-1` replaces it.

---

### 🟢 `P485-1` — AI layer over a deployed LATAM municipal school system

🔵 **For:** a Brazilian municipality or state secretariat already running `i-educar` — of which there
are plausibly hundreds, given **552 forks against 721 stars**.

| layer | component | licence (verified this pass) |
|---|---|---|
| system of record | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) `2.12` | 🟡 **GPL-2.0** · 18 091 B · `f9c375a1be4a` |
| statutory reporting | [`i-educar-educacenso-package`](https://github.com/portabilis/i-educar-educacenso-package) | files Brazil's **Educacenso** national census |
| reporting surface | [`i-educar-reports-package`](https://github.com/portabilis/i-educar-reports-package) | 🟡 GPL-2.0 (JasperReports) |
| tutoring/ITS seam | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** · 1 072 B |
| agent orchestration | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) `a31d826` tool/MCP layer | 🔴 Apache-2.0, **6 operative deviations** |
| offline edge | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) `dbe14ef` | 🟢 **MIT** · 1 096 B · **`es_419` 96.7 %**, `pt_BR` 95.7 % |

🔵 **Wiring, and the licence boundary is the whole point.** `i-educar` is **GPL-2.0**, so the AI
components must not be linked into it. Keep them in a **separate process** and talk to the system of
record over **HTTP/MCP only**:

1. `tutor-mcp` runs as a standalone **MCP server** (Go, MIT) exposing BKT mastery estimation as tools.
2. A DeepTutor-style host (or any MCP client) consumes those tools and the municipality's own LLM
   endpoint; **no `i-educar` source is imported into either**.
3. Reads from `i-educar` go through its HTTP surface and the reports package; writes go back as
   ordinary records. 🟢 **GPL-2.0 obligations attach to derivative works, and a separate process
   speaking a network protocol is the standard way to stay outside that** — the same boundary
   `krzysztofbury/librus-mcp` documented for this base at `p455` (*"integrate over MCP, never vendor
   the repository"*).
4. Where connectivity is the binding constraint, **Kolibri** carries the learner-facing side offline,
   and it is the only platform on these shelves shipping **`es_419`** — Latin-American Spanish rather
   than `es_ES`.

🟢 **First three use cases, in order of least-AI-risk:** enrolment triage and waitlist ranking over
`pre-matricula-digital` data; **attendance-anomaly detection** (dropout early warning) over
`i-diario-app`'s offline captures; **Educacenso filing assistance** — validating a census submission
before it is filed, which is a checkable, high-value, low-hallucination-exposure task.

🔴 **Blocker to clear before touching the `i-diario` family:** `i-diario`, `i-diario-app` and
`pre-matricula-digital` ship AGPL-3.0 **as a Portuguese translation with zero English text**
(35 325 B, `837b5cf19787`). The grant is, strictly read, undefined — see
[`agents/top.md`](../agents/top.md). 🔵 **Resolve it with the maintainer in writing first.** `i-educar`
itself is unaffected: its GPL-2.0 is the English text.

🟡 Effort: **8–12 weeks** to a single-municipality pilot, uncalibrated.

---

### 🟢 `P485-2` — EU-compliant tutor with the 2026 obligations built in, not deferred

🔵 **For:** an EU institution procuring in 2026 that does not want to retrofit a high-risk
classification in 2027.

| layer | component | licence (verified) |
|---|---|---|
| tutoring core | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** · 1 067 B |
| or ITS over any LLM | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** · 1 072 B |
| eval harness | [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) golden-eval + `/eval` pattern | 🔴 GPL-3.0 — **copy the pattern, not the code** |
| tenancy + guards | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) `multi_user/tool_access.py`, `services/mcp/network.py` | 🔴 Apache-2.0, 6 deviations |
| institutional frame | [`uPortal-project/uPortal`](https://github.com/uPortal-project/uPortal) | 🟢 **Apache-2.0 · 0 deviations** |
| LMS bridge | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) (LTI) | 🔴 Apache-2.0, **§4 labels stripped** |

🔵 **Wiring against the actual dates:**
1. **Article 50 transparency applies from 2 August 2026 and was NOT deferred** — so build the
   disclosure surface now: every generative response marked as AI-produced, at the UI layer, not in a
   policy document.
2. **Article 27 FRIA** is required before a high-risk system goes into use and was not deferred
   either. Wire `lumen`'s **golden-evals-in-CI** pattern as the evidence generator: a FRIA that cites
   a reproducible eval run is defensible; one citing intentions is not. 🔴 `lumen` is GPL-3.0 — take
   the *pattern*, not the source, unless the whole deployment can be GPL.
3. Mount through **uPortal** (the cleanest permissive grant on these shelves) and reach the LMS over
   **LTI via Tsugi**, so an AGPL LMS core is never linked.
4. Per-tenant **deny-by-default tool grants** modelled on DeepTutor's `tool_access.py`, because the
   **2 December 2027** Annex III deadline will ask what the agent was permitted to touch, per user.

🟡 Effort: **10–14 weeks**, uncalibrated. 🔴 Dates are from secondary legal commentary; `eur-lex` is
unreachable through this proxy (`Gap 485-H`).

---

### 🟢 `P485-3` — ministry-scale teacher enablement as a distributable skill

🔵 **For:** an education ministry under a **national curriculum mandate** — India (AI mandatory from
Class 3, AY 2026–27), China (AI in teacher qualification exams), Singapore (Code for Fun from
Primary 4). The constraint is that the users are **teachers in thousands of schools**, so
provisioning a server per school is the thing to avoid.

| layer | component | licence (verified) |
|---|---|---|
| diagnostic teaching loop | [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 🟢 **MIT** · 1 101 B |
| mastery + spaced repetition | [`TovTechOrg/Tov-learn`](https://github.com/TovTechOrg/Tov-learn) | 🟢 **MIT** · 1 063 B |
| understanding check | [`koukekoukej-glitch/feynman-tutor`](https://github.com/koukekoukej-glitch/feynman-tutor) | 🟢 **MIT** · 1 055 B |
| exam/qualification prep | [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) | 🟢 **MIT** · 1 064 B |
| pedagogy backbone | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) (2-sigma) | 🟢 **MIT** · 1 068 B |
| mastery state | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (BKT) | 🟢 **MIT** · 1 072 B |

🔵 **Wiring:** 🟢 **all six components are MIT** — this is the one recipe on the shelf with no copyleft
anywhere in it, which is exactly `T485-1`'s prediction about skill-form projects and the reason this
pattern is cheap to deliver.
1. Ship a **skill bundle**, not an application: the teaching loop, mastery tracking and
   understanding-check behaviours distribute as prompt-and-protocol contracts to whatever host agent
   the ministry has licensed.
2. Mount `tutor-mcp` **centrally** as the one server component, holding BKT mastery state per teacher
   so progress survives across sessions and devices.
3. Use `universal-examprep-skill`'s slide-grounded, page-citation approach for **qualification-exam
   preparation** — China is adding AI to teacher qualification exams, so this is the live use case.
4. 🔵 Localise against the **locale measurements** on [`verticals/solutions.md`](../verticals/solutions.md)
   rather than guessing: ILIAS for `es`/`pt` depth, Kolibri for `es_419` plus offline.

🟡 Effort: **6–10 weeks** for a pilot cohort, uncalibrated.

---

### 🟢 `P485-4` — AI over an institutional LMS without touching its copyleft core

🔵 **For:** a university on Sakai, ILIAS, Chamilo or Moodle wanting an AI surface its legal team will
clear.

| layer | component | licence (verified this pass) |
|---|---|---|
| LMS of record | `sakai` 🔴 **ECL-2.0** · 11 119 B / `ILIAS` GPL-3.0 / `chamilo` GPL-3.0 / `moodle` GPL-3.0 | all **copyleft** |
| bridge | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) — LTI | 🔴 Apache-2.0, §4 labels stripped |
| portal frame | [`uPortal-project/uPortal`](https://github.com/uPortal-project/uPortal) | 🟢 **Apache-2.0 · 0 deviations** |
| agentic RAG reference | [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) | 🟢 Apache-2.0 · 11 386 B · **0 deviations** |
| ITS tools | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** |

🔵 **Wiring:** the AI never enters the LMS process. `towardsai/ai-tutor-app` (LangGraph + FastAPI +
Next.js, 0 Apache deviations — the cleanest reference implementation on these shelves) runs
standalone; **Tsugi carries LTI** between it and the LMS; **uPortal** provides the institutional
front door. 🟢 Permissive code stays permissive; copyleft stays in its own process.

🔴 **Two corrections this recipe must carry.** **Sakai is ECL-2.0, not Apache-2.0** — an engagement
that cleared it through an "Apache-approved" list cleared it under the wrong text, and ECL's patent
grant is **narrower**, limited to the contributor's own contributions. And **Tsugi's Apache text has
§4's `(a)(b)(c)(d)` labels stripped**, so the NOTICE obligation in §4(d) has no label to cite even
though the obligation itself is intact.

🟢 **Localisation, measured rather than assumed:** **ILIAS 99.99 % `es` / 99.98 % `pt`**;
**Sakai 98.6 % `es` / 94.0 % `pt_BR`** across 219 bundle families; **Chamilo** ships `pt_BR` *and*
`pt_PT`. 🔴 Moodle's coverage is **not measurable from its repository** — lang packs ship out-of-tree
— so do not quote a Moodle localisation figure from these shelves.

🟡 Effort: **6–9 weeks**, uncalibrated.

---

### 🔴 Declared gaps

| gap | statement |
|---|---|
| 🔴 **`Gap 485-AG`** | **No recipe here has been built**, and `Gap 484-W` carries forward unchanged. Four patterns, zero running systems. The licence boundaries are reasoned from text, not validated by a legal review or a deployment. |
| 🔴 **`Gap 485-AH`** | **Every effort range is uncalibrated** (`Gap 483-Q`, `484-V`). Relative ordering only; none is a quote and none should reach a client as one. |
| 🟡 **`Gap 485-AI`** | **The GPL-2.0 process-boundary argument in `P485-1` is this base's reading, not counsel's.** It follows the `librus-mcp` precedent and standard practice, but a GPL-2.0 engagement needs a lawyer before code, not after. |
| 🟢 **`Gap 485-AJ`** | **`Gap 484-X` partly closes.** `P485-1` is built on LATAM-origin components (`i-educar` and its packages) for the first time. 🔴 But still **zero LATAM-origin *AI* components** — the only licence-clean regional AI repository found is `CENIA-DEV/multilingual-translator-app` at **1★**, too small to anchor a recipe. |
| 🟡 **`Gap 485-AK`** | **`P485-1` names `i-educar` modules from metadata.** The repository was never cloned (`Gap 485-T`), so its HTTP surface, Educacenso module shape and extension points are inferred from package names and topics — the recipe's integration points are unverified. |

---

## 🆕 `p484` — `2026-10-27` — **🟢 FOUR RECIPES, EVERY NAMED COMPONENT LICENCE-VERIFIED FROM BYTES THIS PASS. The pattern that changed: `P484-1` can now be written at all, because the platform at its centre was finally read — and it carries a licence caveat no earlier pass could have stated.**

🔵 Every repository named below was cloned at a stated commit this pass or in `p483`, or had its
`LICENSE` fetched from `raw.githubusercontent.com` this pass. 🔴 Effort ranges remain **uncalibrated
estimates** (`Gap 483-Q`) — relative ordering, not quotes.

---

### `P484-1` — Self-hosted tutoring platform with per-tenant tool governance

🔵 **For:** a university or ministry that wants an AI tutor it operates itself, with defensible
limits on what the agent may touch per user.

| layer | component | licence (verified) |
|---|---|---|
| platform | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) `a31d826` | 🔴 Apache-2.0, **6 operative deviations** |
| tenancy | DeepTutor `multi_user/tool_access.py` — grant v2, deny-by-default MCP + CLI | — |
| egress control | DeepTutor `services/mcp/network.py` — two postures, connect-time revalidation | — |
| isolation | DeepTutor `services/sandbox/` — `quota.py`, `backends.py`, `runner/server.py` | — |
| institutional data | [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) `96546d9` MCP server as the LMS-side tool source | 🟢 Apache-2.0 (bytes) |

🟢 **Wiring:** run DeepTutor as the MCP **host**; register OpenOLAT's native MCP server as a
deployment-tier server in `mcp.json` (deployment tier keeps the permissive network posture — it is
your own LMS); grant each cohort an explicit MCP tool whitelist, because for non-admin users an
absent grant means **no MCP tools are listed or loadable at all**. Students get read tools;
instructors get the write set; nobody gets the ungranted remainder by default.
🔵 **Why these two and not a build:** DeepTutor supplies the plugin contract, tenancy and sandbox;
OpenOLAT supplies the institutional record and its own MCP surface. Neither half is written here.
🔴 **Diligence item to raise before signing:** DeepTutor's LICENSE deviates from canonical
Apache-2.0 in six operative lines, one inside §4(d)'s NOTICE obligation. The grant clauses
themselves are byte-identical, so this is a review note, not a blocker — but it is **counsel's call,
and it must reach counsel**, which it would not have done before this pass.
🔵 **Effort:** 8–10 weeks. 🟡 Uncalibrated.

---

### `P484-2` — Teacher co-pilot on an existing LMS, without forking the LMS

🔵 **For:** a school system on Canvas that wants teacher-facing AI without touching the LMS.

| layer | component | licence (verified) |
|---|---|---|
| LMS bridge | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) `becd181` — 128 tools | 🟢 MIT · 1 071 B |
| pedagogy content | [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) `135d627` — 173 skills | 🔴 **CC BY-SA 4.0** |
| host | any MCP client; or DeepTutor for multi-user deployments | see `P484-1` |

🔴 **The licence shapes this recipe, so it is stated before the wiring.** The skills **and** the
bundled MCP server are ShareAlike with no patent grant. 🟢 **Use them as authored, with
attribution** — that costs nothing. 🔴 **Do not derive a proprietary skill pack from them**: that
triggers CC BY-SA 4.0 on your deliverable. If the client needs proprietary skills, author them fresh
against the same MCP interface and keep the two sets in separate directories with separate licences.
🔴 **Second control, from `p483`:** of `canvas-mcp`'s 51 write tools, **14 carry none of its three
write-safety mechanisms**, and one of those writes a grade. Gate those 14 behind the host's grant
layer, or exclude them from the teacher whitelist.
🔵 **Effort:** 4–6 weeks. 🟡 Uncalibrated.

---

### `P484-3` — Grounded exam-prep and revision, cheap enough to run at cohort scale

🔵 **For:** a LATAM or APAC institution with real cost pressure and material in slides and PDFs.

| layer | component | licence (verified) |
|---|---|---|
| coach | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | 🟢 MIT · 1 065 B |
| self-hosted workspace | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) — local-first, 10+ providers | 🟢 MIT · 1 068 B |
| RAG reference | [towardsai/ai-tutor-app](https://github.com/towardsai/ai-tutor-app) — LangGraph + FastAPI + Next.js | 🟢 Apache-2.0 · 0 deviations |

🟢 **Wiring:** OpenTutor as the self-hosted workspace (local-first keeps student material on
institutional infrastructure, which is the posture LATAM and MEA buyers ask for); the exam-prep
skill as the study loop — it is built to run on **small cheap models** and cites source pages, which
is the anti-hallucination control the pedagogy requires; `ai-tutor-app`'s LangGraph topology as the
reference for grounding retrieval in a curated corpus rather than the open web.
🟢 **Every component MIT or clean Apache** — this is the recipe with no licence caveat, and that is
why it is the one to lead with when the deliverable must be proprietary.
🔵 **Effort:** 4–5 weeks. 🟡 Uncalibrated.

---

### `P484-4` — Governance-first pilot for a jurisdiction writing its own policy

🔵 **For:** a Canadian board, a MENA ministry or any buyer with **no template above them** — the
situation `Gap 483-L` showed Canada to be in and the EMEA table shows across MEA.

| layer | component | licence (verified) |
|---|---|---|
| platform | DeepTutor `a31d826` — grants, SSRF postures, sandbox quotas | 🔴 Apache-2.0, 6 deviations |
| audit surface | DeepTutor `ToolParameter.sensitive` (secret withholding in traces) + `tool_call_stream.py` | — |
| policy artefact | the deployment's own grant matrix, exported per cohort | deliverable |

🟢 **The insight this pass supplies:** the four multi-tenant education repositories measured by this
base all spend their engineering on **authorisation, isolation and egress** — not on model quality.
A pilot that configures and *documents* those three, then hands the board the grant matrix as its
acceptable-use policy, delivers the artefact the jurisdiction is missing. In Canada there is no
provincial template to copy; in MEA there is a national strategy with nothing beneath it.
🔴 **Do not sell this as compliance with a named instrument.** The EU dates this base holds are not
primary-source verified (`Gap 483-K`), and no MEA jurisdiction in the EMEA table has a published
education-AI procurement standard to comply with.
🔵 **Effort:** 6–8 weeks. 🟡 Uncalibrated.

---

### 🔴 Declared gaps

| gap | statement |
|---|---|
| 🟡 **`Gap 484-V`** | **Every effort range above is uncalibrated** — `Gap 483-Q` carries forward unchanged. No pattern in any pass has been checked against a delivered engagement. |
| 🔴 **`Gap 484-W`** | **No recipe here has been built.** `P484-1`'s central claim — that OpenOLAT's MCP server registers cleanly as a deployment-tier server in DeepTutor's host — is inferred from both codebases' structure and **has not been executed** (`Gap 484-A`). It is the single most load-bearing untested assumption on this shelf. |
| 🔴 **`Gap 484-X`** | **Still zero LATAM-origin components.** `P484-3` is aimed at LATAM and APAC buyers and is assembled entirely from North American and East Asian repositories, because `Gap 484-G` shows this base cannot currently *find* regional ones. The recipe is honest about its parts; the shelf is not yet honest about the region. |

## 🆕 `p483` — `2026-10-27` — **🟢 FOUR RECIPES, ALL BUILT FROM REPOSITORIES READ FIRST-HAND THIS PASS. The pattern that changed: `P483-3` no longer builds an AI assessment pipeline — `OpenOLAT` ships one, so the engagement is oversight configuration plus a FRIA, not construction.**

🔵 Every repository named below was cloned and parsed at a stated commit, or read through the authenticated
GitHub API at `2026-10-27T15:58Z`. 🟡 Effort ranges are this base's estimates and have never been calibrated
against a delivered engagement (`Gap 483-Q`).

---

### 🟢 `P483-1` — Permission-parity gate for any agent surface over an existing LMS

**The control:** an MCP tool must never require fewer permissions than the REST endpoint it wraps, and CI must
fail when it does.

**Wire it:**
1. Copy the invariant from [`Selleo/mentingo`](https://github.com/Selleo/mentingo) `e137ca4`,
   `apps/api/src/mcp/mcp-tool-rest-permission-parity.spec.ts`:
   `expect(Reflect.getMetadata(REQUIRED_PERMISSIONS_KEY, restHandler)).toEqual(mcpPermissions)`.
2. For each tool, resolve the REST handler it delegates to and assert set equality of required permissions —
   **equality, not subset**, so a tool cannot silently widen *or* narrow.
3. Pair with `mentingo`'s scope layer as the reference: `mcp-tool-scope.ts`, `mcp-tool-access.ts`,
   `mcp-student-access.ts`, `mcp-admin-access.ts`, `mcp-auth.guard.ts`.
4. For consent, lift `mcp-oauth.service.ts` + `mcp-consent.controller.ts` + `McpConsent.page.tsx` — an OAuth
   consent flow with a user-facing page, which is what an opt-out requirement (Oklahoma SB 1734) needs.
5. Enforce the same shape in Java against [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) `96546d9`:
   `McpToolScope` + `McpPermissionException` are the hooks; `McpToolProvider`/`McpToolDefinition` the contract.

**Why it is worth the code:** 🟢 it converts the one question every university data-protection officer asks —
*can the assistant do something a logged-in user could not?* — from a review opinion into a build failure.
**Stack:** TypeScript/NestJS (mentingo) or Java (OpenOLAT). **Effort:** 🟡 1–2 weeks to port, then free.

### 🟢 `P483-2` — Wrap the 14: a write-safety shim for `canvas-mcp` before it touches a live tenant

**The problem, measured:** [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) at
`becd181` registers **128** tools; **51** are `CANVAS_WRITE`; **14** carry none of the server's three
write-safety mechanisms, and **`execute_typescript`** (`CODE_EXEC`) carries none either.

**Wire it, in this order:**
1. **Start from the allowlist, not the code.** `core/tool_policy.py` reads `ALLOWED_WRITE_TOOLS`
   (`ALLOWLIST_ENV`) and `_ALL_KEYWORD_TOOLS` covers `CANVAS_WRITE` + `LOCAL_WRITE` only — so
   🔴 **`execute_typescript` must be named explicitly or excluded explicitly**; a write-tool enumeration does
   not reach it.
2. **Deny `grade_with_rubric` on day one.** It writes a grade with no confirmation token, no body guard and no
   `dry_run`, while its bulk sibling `bulk_grade_submissions` has `dry_run`. Route single-student grading
   through the bulk path with `dry_run=True` first, or wrap it in `ConfirmationGuard`.
3. **Extend the existing mechanism, do not invent one.** `core/write_confirmation.py` already provides
   `ConfirmationGuard` / `preview_with_token` / `redeem_confirmation`; `tools/pages.py` and
   `tools/student_calendar.py` are the reference call sites (module-level guard constant, preview, redeem).
4. **Guard the student-name writes.** `comment_on_my_submission` and `post_discussion_entry` post text as the
   student with no mechanism, while `submit_assignment` and `mark_module_item_done` require a token. Match them.
5. **Prefer the read-only server where reads suffice.** [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp)
   is MIT and read-only by design — a smaller attack surface than configuring 128 tools down to 72.
6. **Regression-test the policy by construction**, as this pass did: assert `set(registered) == set(TOOL_EFFECTS)`
   so a new tool cannot ship unclassified. At `becd181` that holds — 128 = 128, 0 unclassified, 0 stale.

**Deliverable:** a pinned fork plus an `ALLOWED_WRITE_TOOLS` value per tenant role (student, instructor, admin).
**Effort:** 🟡 2–3 weeks. **Evidence:** [`evidence/canvas-mcp-write-guard-map.2026-10-27-p483.tsv`](../evidence/canvas-mcp-write-guard-map.2026-10-27-p483.tsv).

### 🟢 `P483-3` — Annex III-ready AI assessment: configure OpenOLAT, do not build it

🔴 **This pattern replaces every earlier "build an AI grading pipeline" recipe in this shelf.** The pipeline
exists, in Apache-2.0 Java, at `96546d9`.

**What you inherit** (`core/commons/services/ai/essay/`, 38 files):
`GibberishPreFilter` · `LanguagePreFilter` · `LengthPreFilter` · **`InjectionPreFilter`** ·
`GradingPlausibilityCheck` · `GradingSuggestion` + `AiGradingTier` + `MarkKind` (output is a **suggestion**,
not a mark) · `AnnotatedParagraph`/`AnnotatedSpan` (span-level evidence) · `FormativeFeedback` (decoupled from
grading) · `RejectionReason` + `EssayGradingIntegrityException` + `EssayGradingPreFilterException` ·
`EssayAiCorrectionService`/`Dao`/`Task` (async, persisted) · `AiUsageLog*` (per-call audit).

**What you build:**
1. **Provider decision.** `services/ai/spi/` → `localonnx` for no-outbound-inference deployments,
   `generic` for a self-hosted endpoint, `anthropic` (via `langchain4j-anthropic`) or `openAI` otherwise.
   This is the EMEA data-residency and the LATAM cost/connectivity answer in the same switch.
2. **Oversight workflow.** Art. 14 human oversight: route `GradingSuggestion` into an instructor review queue;
   never let a tier write a mark unattended. Oklahoma SB 1734 ("AI may not be the primary basis for grading")
   maps onto the same control, so one build serves both jurisdictions.
3. **Opt-in/opt-out.** `AiUserPreferenceService` + `AiModule`/`AiFeature` flags give per-user and per-feature
   switches — the plumbing a parental opt-out requirement needs.
4. **The FRIA.** Art. 27 puts the Fundamental Rights Impact Assessment on the deployer (the institution).
   Deliver the template **and** cite the implemented controls as its technical annex.
5. **Item generation, levelled.** `AiMCQuestionService` + `AiBloomLevel` + `QtiQuestionGenerationTask` emit
   QTI items tagged by Bloom level — which is what a curriculum authority audits (India's Class-3 mandate).

🟡 **Caveat to state in any proposal:** nothing here was executed. The filters are read, not exercised
(`Gap 483-A`), and `GradingPlausibilityCheck`'s actual criteria were not traced. 🔴 The MCP side is a **spike**
— `pom.xml` says `spike S1, 2026-10-02`, and `WhoAmIToolProvider` is the only shipped tool — so do not promise
an agent-driven OpenOLAT surface; promise the AI assessment surface, which is mature.
**Effort:** 🟡 6–10 weeks including FRIA. **Evidence:** [`evidence/openolat-ai-mcp-surface.2026-10-27-p483.tsv`](../evidence/openolat-ai-mcp-surface.2026-10-27-p483.tsv).

### 🟢 `P483-4` — A discovery and selection pipeline that a procurement committee will accept

**The problem:** star-ranked discovery structurally misses institutional edtech (see `repos/trending.md`), and a
star count is not an argument a university committee accepts.

**Wire it:**
1. **Enumerate by organisation.** One query covers a whole foundation's flagships without truncation risk:
   `org:sakaiproject org:uPortal-Project org:opencast org:tsugiproject stars:>0` → 74 repositories, all four
   flagships. 🔴 Do **not** use `org:apereo` — it returns 30 repositories, CAS-only, no LMS.
2. **Enumerate by standards surface, not by AI topic.** `qti`, `scorm`, `lti`, `imsglobal`,
   `common-cartridge` are procurement signals; `ai-tutor` is a developer signal and its census channel returns
   `incomplete_results: true` under load.
3. **Re-address tracked rows directly.** Rows discovered through a search channel vanish when that channel
   degrades — which is how this base lost 3,541★ of tracked repositories for four passes. Use `repo:` qualifiers
   for anything already being tracked.
4. **Score with the sector's own rubric.** [`apereo/oss-rubric`](https://github.com/apereo/oss-rubric)
   (CC-BY-4.0, attribution-redistributable) and
   [`apereo/heosat`](https://github.com/apereo/heosat) — the Higher Education Open Source Assessment Tool,
   published 2026-09-23, **0★**. 🔴 `heosat` declares **no licence**, so apply the rubric, do not ship the tool.
5. **Verify licence at the file, never at the API field.** GitHub reports `NOASSERTION` for OpenOLAT, whose
   LICENSE bytes and every source header say Apache-2.0 — the field is wrong in the direction that **loses** a
   usable grant. A `NOASSERTION` is a prompt to read the file; an `spdx_id` of `mit` attests a detector match,
   not an unmodified grant.
6. **Pin `pushed_at` beside stars.** On sub-1,500★ repositories `pushed_at` is the better liveness instrument:
   `tutor-mcp` has 0 star delta across five passes and committed today.

**Deliverable:** a scored shortlist with a licence measurement per row and a named rubric behind the ranking.
**Effort:** 🟡 1 week per vertical. **Evidence:** [`evidence/discovery-channel-apereo.2026-10-27-p483.tsv`](../evidence/discovery-channel-apereo.2026-10-27-p483.tsv) · [`evidence/zero-star-finds.2026-10-27-p483.tsv`](../evidence/zero-star-finds.2026-10-27-p483.tsv).

### 🔴 Patterns this pass declines to write

🔴 **No "deploy a tutoring agent" recipe.** `DeepTutor` (Apache-2.0, 45,352★) is 88.2% of this base's tracked
star mass and remains **unread** — no clone, no code census, no licence byte-check. Writing a composition
recipe around a repository this base has only ever counted stars for would be padding. See `Gap 483-R`.

🔴 **No LATAM-specific pattern.** The region has this base's best-measured governance gap (87% adoption vs 26%
with a strategy) and **zero represented local tooling** (`Gap 483-O`). The honest recipe is `P483-3` with the
`localonnx`/`generic` provider for cost and connectivity — which is why it is written once, in `P483-3`, rather
than duplicated under a regional heading it cannot support.

### 🔴 Declared gaps

| gap | statement |
|---|---|
| 🟡 **`Gap 483-Q`** | **Every effort range on this shelf is uncalibrated.** No pattern in any pass has been checked against a delivered engagement. The ranges are this base's estimates and should be read as relative ordering, not as quotes. |
| 🔴 **`Gap 483-R`** | **`DeepTutor` is 88.2% of the tracked star mass and has never been read.** Stars, licence, topics and `pushed_at` are API-verified across many passes; the repository has never been cloned, its AI surface never censused, its Apache grant never byte-compared. The largest row in this base is also its least examined, and `p482`'s Apache deviation instrument reported it at +2 tokens from canonical without anyone reading what it does. |
## 🆕 `p482` — `2026-10-27` — **🟢 THE CONTROL SET THESE PATTERNS NEED EXISTS — BUT NO SINGLE REPOSITORY HAS IT, SO THE RECIPES BELOW ARE EXPLICITLY **COMPOSITE**: `canvas-mcp` contributes the declared effect policy and the operator allowlist; `mentingo` contributes the thing `p481` correctly said a confirmation token is not — **an OAuth consent bound to an authenticated user id** — plus Postgres RLS. 🔴 And `P4` is retracted and rebuilt: its licence gate was a token-count diff, which this pass proved cannot tell a widened trademark clause from a reflowed parenthesis. 🟢 Plus a new EMEA pattern, now that an Apache-2.0 platform-scale LMS is on the shelves.**

🔵 Every repository named below was read as source by this base (`p480`–`p482`) or had its grant file fetched
and measured this pass. Nothing here is composed from a description.

---

### 🟢 `P1` — The four-control agent surface over an existing LMS (**the reference pattern**)

**Use when:** a client has a Canvas/Moodle estate and wants instructor- or student-facing agents without
replacing the platform. **Effort: 8–10 weeks.**

| control | from | concretely |
|---|---|---|
| 1. **declare** what each tool does | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) `core/tool_policy.py` | a `TOOL_EFFECTS` dict mapping **every** tool to `READ`/`WRITE`/`LOCAL_WRITE`/`CODE_EXEC`; measured set-equal to registrations at `becd181` — **0 unclassified, 0 stale** |
| 2. **gate existence** by operator policy | same, `ALLOWED_WRITE_TOOLS` | env-var allowlist; **unset on HTTP ⇒ read-only default**; accepts `all`, `none`, or names. A write tool not on the list **is never registered**, so no prompt injection can reach it |
| 3. **bind approval to a human** | [Selleo/mentingo](https://github.com/Selleo/mentingo) `mcp/mcp-oauth.service.ts` | OAuth authorization-code consent: `POST /oauth/authorize` with `decision=approve\|deny`, **refused unless `consent.userId === user.userId`** |
| 4. **enforce reach in the database** | same, `storage/db/tenant-db-runner.service.ts:54` | `SELECT set_config('app.tenant_id', $1, true)` per transaction + **RLS** (44 enablements, 204 policy clauses) |

**Wiring:** fork `canvas-mcp`; keep its policy and allowlist intact. Replace layer 3 — **do not keep the
`ConfirmationGuard` as your approval story.** Its own source says: *"It does NOT prove that a person saw or
approved the preview. The model receives the token and can redeem it itself."* Put `mentingo`'s consent
pattern in front: an authenticated consent record, a rendered authorization page, a `decision` POST, and the
`userId` equality check. Keep the 21 guards as **change-detection** (a changed recipient, body or target voids
the token) — which is what they are genuinely good for — not as human oversight.

🔴 **Do not ship layers 1–2 alone and call it human-in-the-loop.** That is the mislabelling `p481` identified
and this base had published for several passes.

### 🟢 `P2` — EMEA sovereign deployment on a **permissive** platform (**new — the pieces only became available this pass**)

**Use when:** a European university, school network or public body needs self-hosted, auditable, non-copyleft
AI-assisted learning ahead of **2 December 2027**. **Effort: 10–12 weeks.**

**Stack:**
- **Platform:** [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) — **Apache-2.0**, grant body
  **word-identical to canonical through all 1,408 operative tokens** (measured this pass). QTI assessment,
  SCORM, curriculum management already in institutional use. 🟡 Its AI surface is **unread** (`Gap 482-C`), so
  budget the agent layer as **greenfield**.
- **Alternative platform:** [Selleo/mentingo](https://github.com/Selleo/mentingo) — **MIT**, ships the agent
  layer **inside** the product. Pick this when time-to-demo beats maturity; pick OpenOLAT when the client
  procures on institutional track record.
- **Agent surface:** build to `P1`'s four controls.
- **Compliance artefact:** the **Art. 27 FRIA**, which Annex III puts on the **deployer** — the institution,
  not the vendor.

**Why this sells before the deadline:** Art. 4 AI-literacy and Art. 50 transparency duties arrive
**2 August 2026**, and emotion recognition in schools has been prohibited since **February 2025**. The FRIA
and the literacy obligation are billable **now**; the platform work follows them.

🔵 **The oversight argument, concretely:** Art. 14 human oversight is an argument you can only win by pointing
at a mechanism. Point at the allowlist (which write tools exist at all), the consent record (which human
approved, bound to their user id) and the RLS policy (what the agent could reach even if it tried). 🔴 Do
**not** point at a confirmation token.

### 🟢 `P3` — APAC multi-jurisdiction routing (**one deployment, five legal postures**)

**Use when:** a regional education group operates across countries whose rules do not agree.
**Effort: 12–14 weeks.**

The calendar is now **inverted** — Vietnam's education obligations land **1 Mar 2027**, nine months before the
EU's **2 Dec 2027**, and India's Class-3 AI mandate phases in from **AY 2026–27**. So build the jurisdiction
switch first, not last.

**Wiring:** one `canvas-mcp`-derived server per jurisdiction, differing **only** in `ALLOWED_WRITE_TOOLS`:

| jurisdiction | allowlist posture | driver |
|---|---|---|
| 🇻🇳 Vietnam | no automated-assessment or behaviour-monitoring write tools registered | education on the high-risk list, **1 Mar 2027** |
| 🇨🇳 China | content-generation tools registered; AI-literacy curriculum delivery in scope | MoE action plan; **≥8 class hours** in Beijing; AI in teacher qualification exams |
| 🇮🇳 India | curriculum and teacher-training surfaces registered | NEP 2020 Class-3 mandate; **₹500 crore** CoE |
| 🇸🇬 Singapore | full surface, with AI Verify evidence collection switched on | voluntary frameworks as de-facto buyer requirements |
| 🇯🇵 Japan | full surface; emphasise human-centred framing in documentation | AI Promotion Act, no penalties |

🔵 Because the allowlist is **operator-set and runtime-immutable**, the jurisdiction posture is a deployment
artefact an auditor can read — not application logic a reviewer has to trust.

### 🟢 `P4` — **RETRACTED AND REBUILT**: the licence-diligence gate

🔴 **`p481`'s gate is withdrawn.** It compared operative **token counts** against the canonical Apache text and
failed the build on a non-zero delta. This pass proved that gate both over- and under-fires: `OpenOLAT` has a
delta of **+99** and **zero** changes inside the grant, while `onemnemo/mnemo` has a delta of **exactly 0** and
five changed positions. **A distance cannot tell you whether a term moved.**

**The rebuilt gate — positional, and it fits in a CI step:**

1. Fetch the dependency's grant **to a file**; measure the **file** (`Gap 468-A`). Never read a badge, a
   repository description or a comparison table.
2. Fetch the canonical text from the licensor (`https://www.apache.org/licenses/LICENSE-2.0.txt`) and assert
   the reference: **11,358 B · `sha256_16 cfc7749b96f63bd3` · 1,413 operative tokens**. If your tokeniser does
   not reproduce 1,413, **your instrument is wrong** — fix it before judging anyone's licence.
3. Operative text = file truncated at `APPENDIX`, split on whitespace.
4. Align candidate against canonical with a sequence matcher and take the opcodes.
5. **Fail only if an opcode starts before canonical token 1408** (the grant body; `[1408:1413]` is
   `END OF TERMS AND CONDITIONS`). Changes at or after 1408 are trailing prose — that is all OpenOLAT's +99
   tokens are.
6. On an in-grant hit, report the **canonical section** from the start table
   (§1=15 · §2=482 · §3=535 · §4=677 · §5=1002 · §6=1066 · §7=1111 · §8=1195 · §9=1309) and route **only
   those** to counsel.

🟡 **Expected false-alarm reduction on this base's own corpus: 6 flagged → 1 worth a lawyer's time**
(`beltromatti/get-it`, §6 Trademarks, where `reasonable and customary use in` is deleted — and even that
**widens** the exception).

🔴 **The MIT/AGPL trap this gate also catches:** [frappe/frappe](https://github.com/frappe/frappe) is **MIT**
(1,118 B); [frappe/lms](https://github.com/frappe/lms), the application on top of it, is **AGPL-3.0**
(33,893 B). A 2026 comparison site published the framework's licence as the product's. Step 1 catches this in
one `curl`; a dependency manifest never will.

### 🟡 `P5` — Assessment integrity under an agentic LMS (**the verification-gap pattern**)

**Use when:** an institution is deploying agents into a platform that also receives graded work.
**Effort: 6–8 weeks.**

🔴 **The threat is structural, and it comes from this base's own source reads, not a vendor blog.**
`canvas-mcp` classifies **51** tools as `CANVAS_WRITE` **including submission**; `mentingo` exposes
`create_quiz_lesson`, `update_content_lesson` and `request_authoring_upload` among its 142. An agent holding
those tools can **complete coursework inside the platform** — a verification gap no proctoring product closes,
because nothing was proctored.

**Wiring:**
1. **Split the surface.** Two deployments from one codebase: a student-facing server whose
   `ALLOWED_WRITE_TOOLS` is **unset** (read-only by default on HTTP), and an instructor-facing server with a
   named write list. These are different processes with different credentials, **not** roles inside one.
2. **Bind every write to a consent record** per `P1` layer 3, so each mutation carries an authenticated
   `userId`.
3. **Keep the audit trail** — `canvas-mcp` already ships audit logging and FERPA tests among its **45**
   security test files.
4. **Shift the assessment design**, because the controls above cannot verify authorship: process evidence
   (draft history, keystroke patterns), oral examination, tiered AI-use policy.

🔴 **State the limit to the client in writing:** detection does not work. Reported detector false-positive
rates run **5–20%** and fall disproportionately on non-native and neurodiverse students. 🟡 Sell the
assessment redesign, not a detector — and note that these integrity figures are **secondary-source**
(`Gap 482-I`), while the write-surface counts are first-hand.

### 🔵 `P6` — The instrument discipline every pattern above depends on

🔴 This base published **three** wrong counts for the repository it had already cloned: 136 and then 130 tools
where there are **128**; 52 `CANVAS_WRITE` where there are **51**; "60+" security test files where there are
**45**. Every one came from a grep.

**The rule, for any capability claim that reaches a client:**

| never | always |
|---|---|
| `grep -c '@mcp.tool'` | an **AST** walk for decorated function definitions — it gave 128, and the README and the policy dict both agree |
| `grep -oE 'Effect\.[A-Z_]+' \| uniq -c` | parse the **dict literal** — the regex also counts the enum declaration, which is where the extra `CANVAS_WRITE` came from |
| trusting a repository's **description** field | read the **README body** and the **source**; the description still said 102 tools |
| reading `total_count` as a population | check **`incomplete_results`** first — it was `true` this pass, so the census was a timeout, not a count of 21 |

🟢 **And one property you do not need to execute code to verify:** set equality between registered tool names
and policy keys. It is the coverage property `tests/security/test_tool_policy.py` asserts, and measuring both
sets settles it — **0 unclassified, 0 stale, True** — without running a line of third-party code.
## 🆕 `p481` — `2026-10-27` — **🔴 RECIPE CORRECTION, AND IT AFFECTS EVERY PATTERN ON THIS SHELF THAT CLAIMED A HUMAN IN THE LOOP: a preview→confirm token does **not** constitute human approval. The source of the best-guarded repository on this shelf says so explicitly — the model receives the token and can redeem it itself. 🟢 The control that actually stops a prompt injection is an **operator-set allowlist of which write tools exist**, and the patterns below are rewritten around it. 🟢 Plus a new permissive-stack recipe, now that an MIT LMS exists, and a licence-diligence gate built from this pass's own instrument.**

🔵 **Gate posture, unchanged (`Gap 446-A`):** `make hooks` **not attempted**. **No pattern below has been
executed** — the harness refuses `Code from External` (`Gap 481-A`). These are wiring diagrams over components
whose source was read, not tested deployments.

---

### 🔴 Correction first: the four-layer control model, and which layer is which

Read first-hand from [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) `becd181`
(`core/tool_policy.py`, `core/write_confirmation.py`):

| layer | mechanism | binds | survives a prompt injection? |
|---|---|---|---|
| 1 | `ALLOWED_WRITE_TOOLS` env var (operator-set) | **which tools are registered at all** | 🟢 **yes** — the model has no hand in it and no tool can change it at runtime |
| 2 | registration gates `CANVAS_ROLE`, `STUDENT_WRITE_TOOLS`, `EXECUTE_TYPESCRIPT_ENABLED` | which tools are ever built | 🟢 yes — the policy can only *remove*, never restore |
| 3 | `ConfirmationGuard` preview→token→confirm (21 instances, HMAC, single-use, 300 s TTL) | **the request** — target, payload, caller identity | 🔴 **no** — *"It does NOT prove that a person saw or approved the preview"* |
| 4 | the MCP **client's** tool-approval step | **the human** | 🟢 yes, and this is the only layer that does |

🔵 **What to change in any existing recipe:** keep layer 3 — it genuinely prevents a *swapped* target or payload
after preview — but stop describing it as human review. If a pattern needs a human decision, it must come from
layer 4 (the client's approval UI) or from a platform-owned consent screen (see Pattern B).

### 🟢 Pattern A — guarded Canvas co-pilot for US higher ed, FERPA-evidenced

**Components:** [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, 130 tools) ·
[`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) (AGPL-3.0-**only**, deployed, never linked)
· an MCP client with a tool-approval UI.

**Wiring, in order:**

1. Deploy Canvas as a **separate service**. Do not link into it, do not run in-process: Canvas elects
   `AGPL-3.0-only` and, unlike Open edX, ships **no RPC scope clarification** (`p480`). The boundary rests on
   this base's architectural reasoning, so keep the AI service independently deployed and talking HTTP.
2. Run `canvas-mcp` on the **HTTP transport**, where `ALLOWED_WRITE_TOOLS` unset means **read-only by default** —
   the hosted default is the safe one. Confirm 72 read tools register and no write tool does.
3. Enable writes **by name only**, never `all`: e.g. `ALLOWED_WRITE_TOOLS="create_announcement,send_conversation"`.
   `all` excludes `execute_typescript` by design; do not add it.
4. Leave `EXECUTE_TYPESCRIPT_ENABLED` unset. The single `CODE_EXEC` tool runs caller-supplied code **with the
   caller's Canvas token** — in a FERPA context that is the one tool to keep unregistered.
5. Put the human decision in the **client's approval step** (layer 4). The 21 confirmation guards then stop a
   swapped recipient or body between preview and send; they are not the approval.
6. Set `AUDIT_LOG_DIR`. The repo ships `core/audit.py` and `tests/security/test_audit_logging.py` — a US
   engagement must evidence FERPA handling, and `tests/security/test_ferpa_compliance.py` is the reference.

🔵 **Read-only variant:** where only retrieval is needed,
[`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) (MIT, 1,276 LOC) has **26 tools and zero
write calls** (`p480`) — safety by having no write path, which is simpler to argue than a policy to configure.
🔴 Note its 500-item list ceiling and `"private": true` manifest (clone-only, no published package).

### 🟢 Pattern B — permissive full stack for EMEA, with a consent screen the agent cannot mediate

**Components:** [`Selleo/mentingo`](https://github.com/Selleo/mentingo) (**MIT**, 584k LOC, multi-tenant LMS with
`apps/api/src/mcp/`) · Langfuse (`@langfuse/*`, already wired) · `@ai-sdk/openai` or any provider behind it.

**Why this pattern exists:** every previous platform recipe on this shelf had to route around AGPL-3.0 or
GPL-3.0. An MIT LMS removes the source-disclosure question from a hosted deployment entirely — no RPC-boundary
argument required.

**Wiring:**

1. Self-host from `docker-compose.yml`; bring up `docker-compose.langfuse.yml` alongside for LLM tracing from
   day one, because the EU AI Act's **Art. 4 literacy** and **Art. 50 transparency** duties are already in force
   and tracing is how you evidence them.
2. Use the platform's **own** MCP surface rather than bolting a server on: `mcp-admin-tools.ts`,
   `mcp-customization-tools.ts`, `mcp-generic-upload-tools.ts`, `mcp-content-resource.ts`.
3. Route human approval through `mcp-oauth.controller.ts` + `mcp-consent.controller.ts` — a **platform-owned**
   consent grant, out of band of the tool call. This is the layer-4 control, owned by your own deployment.
4. Keep grading, admissions and proctoring **out of scope** until the EU high-risk regime lands
   **2 December 2027**; tutoring, content generation and administrative assistance are the deployable surface now.
5. Rely on `tenant-aware-session` for multi-institution deployments — and verify it, because this base has not
   (`Gap 481-G`).

🔴 **Caveat that belongs in the pitch, not a footnote:** `mentingo` is **99★**. Its licence and architecture are
verified; its institutional maturity, LTI/SCORM support, accessibility conformance and the security of its MCP
tools are **not** (`Gap 481-J`). For a risk-averse institutional client, Pattern A on Canvas remains the
conservative choice.

### 🟢 Pattern C — LATAM: consolidate shadow adoption, do not deploy greenfield

**The demand shape, measured:** 200 higher-education institutions across 19 LAC countries — **87% already using
AI** in at least one area, **74% in teaching and learning**, **26% with a formal strategy** (UNESCO IESALC /
UNU-IAS). Adoption is bottom-up, by individual academics and students.

**Wiring — this is a governance engagement with a technical deliverable:**

1. **Inventory first.** The institution is already running AI; the deliverable is finding it. Nothing is
   installed in step 1.
2. **Put a traced gateway in front of existing use** rather than replacing tools: Langfuse (as in Pattern B)
   against the institution's current providers gives per-faculty visibility and the evidence base for a policy.
3. **Anchor the policy** to the UNESCO **Observatory on AI in Education for LAC** (launched 14 April 2026) and
   the national instrument that applies — CONPES 4144 (Colombia), Peru's INDECOPI-coordinated framework and its
   **regulatory sandboxes**, Uruguay's Council of Europe Framework Convention signature.
4. **Only then** choose a platform. If one is needed, `mentingo` (MIT) avoids the copyleft question;
   `openedx/edx-platform` carries the licensor's own RPC clarification (`p480`) if Open edX is already in place.
5. **Spanish/Portuguese content:** the region's open supply is administrative and copyleft — `i-Educar`
   (GPL-2.0), `i-Diario` (AGPL-3.0), `bncc-dados` (MIT) — so expect to integrate with it, not build on it, and
   expect the AGPL rows to stay separately deployed.

🔴 No LATAM-domiciled agent repository exists in this base's census to compose with. That is a measured gap
across three passes, not a research omission.

### 🟢 Pattern D — a licence-diligence gate, built from this pass's own instrument

**The problem this solves:** `license.spdx_id` said "Apache-2.0" for all 13 repositories measured this pass. Six
of them do not carry the canonical operative text and one has had a permission narrowed. Metadata diligence
cannot see any of it, and byte comparison produces false positives because Apache-2.0 *instructs* you to fill in
its appendix.

**The gate, as run this pass:**

1. Fetch the licensor's canonical text once and store it:
   `https://www.apache.org/licenses/LICENSE-2.0.txt` → **11,358 B**, `sha256 cfc7749b96f63bd3`.
2. For each candidate, fetch `LICENSE` from `raw.githubusercontent.com` (try `main` and `master`;
   `LICENSE`, `LICENSE.txt`, `LICENSE.md` — `haxtheweb/haxcms-php` uses `master/LICENSE.md`, and a 404 on
   `LICENSE` is **not** evidence of no grant).
3. Truncate both at `END OF TERMS AND CONDITIONS` — everything after is the appendix you are meant to edit.
4. Compare as **word tokens**, whitespace-insensitive (canonical = **1,413** tokens). Zero delta ⇒ the grant is
   the canonical grant, whatever the byte count says.
5. Fail the gate on any non-zero delta and **read the diff**; grep the two-marker fingerprint
   (`submitted to the Licensor` + `excluding any notices`) to recognise the known circulating rendering.

🔵 Reusable beyond Apache: the same gate applied to AGPL-3.0 explains `p479`'s byte-count collision
(34,523 B appearing with two different digests) and this pass's Apache collision (11,362 B, two digests, both
verbatim). 🔴 This base holds a canonical reference for **Apache-2.0 only** — MIT, GPL-3.0 and AGPL-3.0 are
still byte-compared (`Gap 481-I`), and MIT cannot be word-compared naively because its text embeds the
copyright line.

### 🟡 Pattern E — composed tutor, unchanged in shape and now with a Go option

**Components:** [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) (Apache-2.0 · 🟡 operative text altered,
4 tokens — see `repos/trending.md`) for tutoring · [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server)
(MIT) for spaced repetition · [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) (MIT, 108k LOC,
`docker-compose.prod.yml`) as a self-hostable tutor · [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp)
(MIT, **Go**, 171k LOC, auth middleware, `Dockerfile`) where the deployment target prefers a single static binary
over a Python runtime.

**Wiring:** retrieval and tutoring in DeepTutor (`pip install deeptutor`, published wheel — `p480`); expose the
learner's review queue through `anki-mcp-server` so the tutor schedules reinforcement rather than re-explaining;
keep the LMS as the system of record behind Pattern A or B.

🔴 **Licence note that changes the paperwork:** DeepTutor's `LICENSE` is **not** the canonical Apache-2.0 text —
4 operative word tokens differ, in the *Contribution*/*Contributor* definitions and the § 4 NOTICE clause. It is
the largest education-AI repository on GitHub at 45,069★ and its grant should be read by counsel, not assumed
from the label. 🔵 Unchanged from `p477`: permissive **code** does not imply permissive **curriculum** — the two
largest education *data* repositories are CC BY-NC and ODbL.
## 🆕 `p480` — `2026-10-27` — **🟢 P14'S LOAD-BEARING ASSUMPTION IS NOW VERIFIED IN SOURCE RATHER THAN ASSUMED FROM A NAME — `canvas-mcp` really cannot write — and the same clone channel hands P14 the grading component `Gap 479-AQ` said did not exist, at the price of that boundary. 🔴 **P16 arm A is withdrawn, not re-estimated**: Fedena is Rails 2.3.5 with no `Gemfile`. 🟢 And P17 is the first recipe on this shelf whose copyleft boundary rests on a sentence the **licensor wrote**, not on this base's architectural reasoning.**

🔵 **Gate posture, unchanged (`Gap 446-A`):** `make hooks` **not attempted** — harness refuses `Code from
External`. **Nothing below is gate-attested.** Frontmatter, closed-vocabulary `region`, pipe-counts,
no-header-as-data and prepend-only re-checked in this session's own code.

---

### 🟢 P14 corrected — the boundary holds on evidence, and the frozen grading gate now has a real alternative

🔵 **What `Gap 479-AP` demanded:** *"P14's whole licence argument rests on `canvas-mcp` being read-only; that
claim is read from its description and name, **not** from its source, its scopes or a transcript. If it can
write, P14's boundary argument collapses."*

🟢 **It does not collapse.** [boyuchengz/canvas-mcp](https://github.com/boyuchengz/canvas-mcp) was cloned at
`a91eeb9` and read in full
([`evidence/clone-tier-source-reads.2026-10-27-p480.tsv`](../evidence/clone-tier-source-reads.2026-10-27-p480.tsv)):
**26 tools, every name `get_*` or `list_*`; a 33-call surface of 20 `getList` + 11 `getOne` + 1 `resolve` +
1 `download`; zero write calls; `request()` passes no `method` option so fetch defaults to GET; the string
`method:` appears nowhere in `src/`; and the exported client has no write primitive to call.**

🟢 **Two source-only facts that change the recipe, not just its justification:**

| finding | effect on P14 |
|---|---|
| 🟢 `getList` refuses a `rel="next"` link whose origin differs from the configured Canvas host, and `download()` omits the token | the component already has the token-exfiltration guard a reviewer would otherwise ask P14 to add |
| 🔴 `MAX_PAGES = 5` × `per_page = 100` = **500 items per list call**, silently truncating | **P14 must add pagination handling or scope to courses under 500 assignments/submissions.** This is a real defect-in-waiting and no description discloses it |
| 🔵 `package.json` is `"private": true` | integration is a **clone and pin**, not `npm install` |

🔴 **And the correction `Gap 479-AQ` needs is internal, not external.** That gap records P14's assessment gate
as a **0★** project *"chosen because the grading census returns zero alternatives."* An alternative has been on
this base's shelves all along — **cited 56 times in retained history**, with its write tools and its
`read_only_hint=True` on 72 of 128 tools already recorded by earlier passes. It was never carried into the
recipe:
[vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) — **308★, MIT, created 2025-02-28,
pushed 2026-10-26, 32,878 LOC, 136 `@mcp.tool` definitions at `becd181`** — and it grades, via
`grade_single_submission` and `grade_with_rubric`. 🔴 **It also writes**: this pass measured **12 write call
sites** at the HTTP-client level (8 `client.post` + 3 `client.put` + 1 `client.delete`), with
`create_assignment`, `edit_page_content` and `delete_assignment_with_confirmation` in the same surface. 🔵 The
12-call-site figure is the new measurement; the tool count is an update to the "102–103" and "128" this base
published from weaker channels.

🟢 **So P14 now has an explicit, documented fork rather than a hidden assumption:**

| arm | components | what you get | what you accept |
|---|---|---|---|
| **A — read-only** *(recommended default)* | [boyuchengz/canvas-mcp](https://github.com/boyuchengz/canvas-mcp) 🟢 MIT + [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) 🟡 Apache-2.0 as the tutoring engine | 🟢 a provably non-mutating integration into the LMS of record — **verified at 33 call sites**, which is an argument you can put in front of a district's counsel and its CISO | 🔴 grading stays human; the agent advises and cannot record |
| **B — read/write** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) 🟢 MIT + DeepTutor | 🟢 rubric-based grading against Canvas from a maintained 308★ project | 🔴 12 write call sites into the system of record, including deletes; **the whole safety argument for arm A is surrendered**, and the write guards are uninspected (`Gap 480-F`) |

🔵 **Wiring, both arms:** Canvas ← MCP server (stdio) ← agent runtime; DeepTutor carries an MCP **client in its
core dependencies**, so it is the tool-calling host rather than something glued to one. Deploy the MCP server as
a separate process; keep the Canvas API token in the server's environment, never in the agent's context.
🔵 **Recommendation: start on arm A, and treat arm B as a second phase gated on a written data-handling
review** — not because arm B is bad, but because arm A's claim is now *provable* and that is a rare asset in a
public-sector procurement.

🔵 **Estimate: not given.** `Gap 479-AO` has flagged every week figure on this shelf as judgement rather than
measurement for three passes; this pass stops producing them (see `Gap 480-AO`).

### 🔴 P16 arm A — withdrawn, not re-estimated

🔵 `Gap 479-AR`: *"P16 arm A is unpriced. Fedena's dependency manifest, Ruby and Rails versions, test suite and
last commit were **not read**; '6–10 weeks if the port is clean' is a sentence, not an estimate."*

🟢 They have now been read, from a clone at `68a84ac`, and the conditional was carrying everything:

| what was read | finding |
|---|---|
| `config/environment.rb` | `RAILS_GEM_VERSION = '2.3.5'` — **Rails 2.3.5, January 2010** |
| boot API | `Rails::Initializer.run` — **removed in Rails 3.0**; the boot/config layer is a rewrite, not an upgrade |
| dependency manifest | 🔴 **no `Gemfile` exists.** Bundler arrived with Rails 3 — there is nothing to audit and the dependency set must be reconstructed |
| the single declared gem | `config.gem 'declarative_authorization', :source => 'http://gemcutter.org'` — **a host renamed in 2010**, over plain HTTP |
| `vendor/plugins` | **14**, a mechanism **removed in Rails 4** — including **`open_flash_chart`** (Flash; no browser runtime since **Dec 2020**) and `fckeditor` (superseded 2009) |
| size | **273,846 LOC** — 62,479 Ruby · 52,214 ERB · **159,153 JS** |
| test suite | **212** spec/test files 🟢 exist — and were **not run** (`Gap 480-A`) |
| domain model | 🟢 intact: **74 models, 50 controllers, 781 views** |

🔴 **"6–10 weeks if the port is clean" is withdrawn.** The port crosses **six Rails majors and the Rails 2→3
rewrite boundary** with no manifest, a dead gem source and a non-functional Flash reporting layer. 🔵 This pass
publishes **no replacement figure**, because substituting one unmeasured number for another is what `Gap 479-AO`
is about.

🟢 **But P16 keeps a usable arm, and the clone is what made it visible.** `Gap 479-M` asked whether a `NOTICE`
carried Fedena's grant; **175 Ruby files carry the full Apache-2.0 per-file header.** So:

| arm | what you take from Fedena | why this survives the audit |
|---|---|---|
| 🔴 **A — port the application** | ~~the running Rails app~~ | **withdrawn** on the evidence above |
| 🟢 **B — take the domain model, not the code** | the Apache-2.0 **schema and domain semantics** for students, enrolment, attendance, exams, fees — 74 models, corroborated across 175 headers | a 2010 Rails *implementation* is a liability; a 2010 *school-administration domain model* is a specification, and it is permissively licensed. Build fresh against it |

### 🟢 P17 — an Open edX AI layer whose copyleft boundary the licensor wrote down

🔵 **Why this recipe is new in kind.** `Gap 478-T`, `Gap 479-R` and `Gap 479-AS` all say the same thing: every
"deployed, not linked" boundary on this shelf is **this base's own architectural reasoning**. For Open edX
specifically, it no longer has to be. `openedx/edx-platform`'s `LICENSE` is **616 bytes longer than the bare FSF
text**, and the extra bytes are a clarification in edX Inc.'s own voice: a *"public, independently available web
service … communicating … by any form of inter-service communication, including but not limited to Remote
Procedure Call (RPC) interfaces, **is not a work based on our copyrighted work**"*, and its source files are
**not** Corresponding Source (full quote and limits: `repos/foundations.md`).

| slot | component | grant | role |
|---|---|---|---|
| platform | [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 **+ the RPC clarification** | courses, enrolment, grades — **left unforked** |
| deployment | [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 | the supported Docker deployment path |
| the AI service | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟡 Apache-2.0 *(non-canonical — read it)* | tutoring engine, **own process, own repo, own licence** |
| spaced repetition | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | 🟢 MIT | retention scheduling as MCP tools |
| pronunciation (language courses) | [Halleck45/OpenPronounce](https://github.com/Halleck45/OpenPronounce) | 🟢 MIT | phoneme-level assessment, self-hosted; **replaces a priced cloud API** |

🔵 **Wiring that matches the clarification's own words, which is the whole point:** run the AI service as a
**separate, independently deployable HTTP/RPC service**. It talks to Open edX over its REST APIs and LTI; Open
edX does **not** import it and it does **not** import Open edX. 🔴 **Do not implement it as an in-process Open
edX plugin or an XBlock** — an in-process extension is plainly *not* what the quoted sentence protects, and that
choice is exactly where the architectural argument would have to resume.

🔴 **Three limits that must travel with this recipe** (`Gap 480-G`): the clarification is the **licensor's stated
interpretation**, not an amendment; it names **edX Inc.**, while the project is now stewarded by the **Axim
Collaborative**; and it is **Open edX only — Canvas carries no equivalent**, so P14 cannot borrow it. **Counsel
reads the sentence; this base does not rule on it.**

### 🟢 P18 — a licence-diligence gate, because this pass found two ways a scanner gets education AI wrong

🔵 Not a product recipe — a **step to insert into any education-AI engagement**, built from this pass's own
findings. It exists because two different failure modes were measured, and both fail in the *permissive*
direction:

| failure mode | measured instance | the check |
|---|---|---|
| 🔴 a **prose claim with no grant file** | [mahseema/aibooks](https://github.com/mahseema/aibooks) — README says `## License` → `[MIT](LICENSE.md)`; `LICENSE.md`, `LICENSE`, `LICENSE.txt` are **all 404 on both branches** | never accept a README licence. Resolve the **file**, at the pinned ref |
| 🔴 a **non-canonical licence body** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (11,408 B) and [SimonsTang/feifei-companion](https://github.com/SimonsTang/feifei-companion) (10,227 B) — both differ from `apache.org`'s 11,358 B text, **in the same three body lines** | **diff the payload against the canonical text**, not its SPDX tag. A digest match is the only clean pass |
| 🔴 an **unread version election** | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) — the `LICENSE` is bare AGPL; the election (**"version 3 of the License"**, no "or later") is in the **per-source-file header** | read a source file's header, not only `LICENSE` |
| 🔴 a **scope clarification hidden in byte count** | [openedx/edx-platform](https://github.com/openedx/edx-platform) — +616 B over the bare text, and those bytes are commercially decisive | diff `LICENSE` against the bare upstream licence text; **investigate any delta** |
| 🔴 **attention without licensability** | [JushBJJ/Mr.-Ranedeer-AI-Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) — **29,550★, no grant at 14 probed paths, no README licence line** | star rank is not a licence signal. Probe before shortlisting |

🟢 **Wiring:** a pre-flight script per candidate repo — `git ls-remote` to pin the ref → fetch `LICENSE` and
every common variant **as a file** → `sha256` against a canonical-text control set → diff on mismatch → grep one
source file's header for a version election → fail closed on 404. 🔵 Across the 305-row union, **19% declare no
grant and a further 12% are `NOASSERTION`**, so this gate changes the shortlist for roughly **one candidate in
three** (`intel/market.md`).

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 480-AO`** | **No recipe on this shelf has been built or run, and this pass stops issuing week estimates.** `Gap 479-AO` and `Gap 478-AI` carry forward: no integration executed, no version compatibility tested, no xAPI profile validated. **P14's boundary is now verified in source; P14 itself is still unbuilt**, and the harness refuses to execute cloned code (`Gap 480-A`). Withdrawing P16-A's figure without replacing it is deliberate. |
| 🔴 **`Gap 480-AP`** | **P17's boundary rests on a quoted sentence this base cannot adjudicate** (`Gap 480-G`/`480-N`): licensor interpretation rather than amendment, naming edX Inc. rather than the Axim Collaborative, covering only a public independently-available service over inter-service communication. **It is a far stronger position than P11–P16 ever had and it is not a legal opinion.** |
| 🔴 **`Gap 480-AQ`** | **P14 arm B is recommended against on an uninspected basis.** `vishalsachdev/canvas-mcp`'s 12 write call sites and 136 tools were inventoried by grep; **no scope model, permission check or confirmation flow was read** (`Gap 480-F`). "It writes" is certain; "its writes are unsafe" was **not** measured and is not claimed. |
| 🔴 **`Gap 480-AR`** | **P16-B asserts a domain model is reusable without modelling it.** 74 models and 781 views were counted, not read; no entity-relationship extract was produced, and whether Fedena's 2010 school-administration semantics fit any current jurisdiction's SIS requirements is **entirely unexamined**. |
| 🟡 **`Gap 480-AS`** | **P18's gate is specified, not implemented.** The five checks are each derived from a measurement this pass actually made, but **no script was written, committed or run against the 305-row union** — the "one candidate in three" figure is arithmetic on the census, not a gate's output. |
| 🟡 **`Gap 480-AT`** | **`Gap 479-AT` carries forward: no recipe was checked for localisation fit.** P17 adds `OpenPronounce` for language courses with **no check of which languages it actually supports** beyond its own English-focused description, and no region other than LATAM has been checked for a permissive curriculum dataset. |

---

## 🆕 `p479` — `2026-10-27` — **🔴 THIS PASS CORRECTS ITS OWN RECIPES BEFORE ADDING ANY: **P11's hand-waved Canvas boundary now has an MIT implementation**, **P12's mastery component has not been pushed since 2024-01-02**, and **P12's record store has 0★ and nothing since 2026-08-08**. 🟢 Three components swapped on measured grounds, then three new recipes — one per region that this pass could actually place — including the first LATAM recipe built on working *software público* rather than on imported parts.**

🔵 Gate posture unchanged (`Code from External`; `make hooks` not attempted; session-local checks green).
Grants in [`evidence/grant-payload.2026-10-27-p479.tsv`](../evidence/grant-payload.2026-10-27-p479.tsv);
maintenance reads in [`evidence/census.2026-10-27-p479.tsv`](../evidence/census.2026-10-27-p479.tsv) and on
`repos/foundations.md`.

---

### 🔴 Corrections to P11, P12 and P13 — three components fail a maintenance or licence check

| recipe · item | component as published | what was measured this pass | 🔁 replacement |
|---|---|---|---|
| **P11 · item 6** | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) *"stays a separate deployed service, reached over LTI/REST — never forked, never linked"* — 🔴 architectural reasoning only (`Gap 478-AL`) | 🟢 [boyuchengz/canvas-mcp](https://github.com/boyuchengz/canvas-mcp) exists: **MIT**, 1,072 B · `4450dee7f762`, 115★, created 2026-10-25, **read-only** MCP server onto Canvas | 🟢 keep Canvas deployed as-is and **add `canvas-mcp` as item 7**: the agent reads courses, assignments and submissions over MCP. Read-only is the feature — nothing the agent does can write to the AGPL-3.0 system |
| **P12 · item 3** | [bigdata-ustc/EduKTM](https://github.com/bigdata-ustc/EduKTM) — knowledge-tracing models behind the sequencing decision | 🔴 **last pushed 2024-01-02** — dormant 2 y 10 m; 267★; Apache-2.0 confirmed | 🔁 [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) — **MIT**, 452★, **pushed 2026-10-18**. Already P11's item 2, so the two recipes converge on one maintained library |
| **P12 · item 5** | [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) — *"embedded PGlite mode for a single-tenant EU deployment"* | 🔴 **0★**, created 2026-03-04, nothing since **2026-08-08**. Grant is sound (Apache-2.0, byte-identical to the control, two passes) but adoption is nil | 🔁 [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) — Apache-2.0, 144★, updated the day of this pass. 🟡 Loses the embedded-PGlite single-binary story; that was the only reason to prefer the 0★ option |
| **P13 · item 6** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) *"fallback, if LGPL is acceptable"* | 🟢 election now read: **LGPL-3.0-or-later** (manifest + header), so the upgrade path is open | 🟢 unchanged, but the fallback is now **licence-qualified** rather than licence-assumed |
| **P13 · premise** | *"permissive school administration where no permissive SIS exists"* | 🔴 **the premise is wrong**: [projectfedena/fedena](https://github.com/projectfedena/fedena) declares **Apache-2.0** in a `NOTICE`, 547★, copyright **2011** | 🟢 P13 survives as *one of two* options; the other is P16 below, which prices the port |

🔵 **The pattern in all three corrections is the same and worth naming:** every one of these components passed a
*licence* check in an earlier pass and failed a *liveness* check in this one. 🟢 A grant tells you whether you may
build on something; it says nothing about whether anyone else does. 🔴 This base graded components on grants for
four passes and could not grade them on liveness until the search channel returned.

---

### 🟢 P14 — LMS-attached tutoring for a North American district, without forking anything

🔵 **The engagement.** A district or university already runs Canvas and is procuring AI tutoring into a falling
faculty-confidence environment (intent to use AI in teaching down 76% → 67%; 26% of US/Canada faculty
enthusiastic). What sells is not autonomy; it is a provable record that a human decided.

| # | component | repo | grant (payload) | role |
|---|---|---|---|---|
| 1 | LMS reader | [boyuchengz/canvas-mcp](https://github.com/boyuchengz/canvas-mcp) | 🟢 **MIT** · 1,072 B · `4450dee7f762` | read-only MCP onto Canvas: courses, assignments, submissions. **No write path exists**, so the AGPL-3.0 system is never touched |
| 2 | tutoring surface | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | 🟢 MIT · 1,105 B · `5baaaf977a28` | BKT-driven ITS from a US research lab; 271★, **pushed the day of this pass** |
| 3 | mastery estimate | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT · 1,066 B · `f5f955194636` | a **computed** mastery state rather than the model's opinion; 452★, maintained |
| 4 | assessment gate | [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent) | 🟢 MIT · 1,069 B *(p478)* | every assessment-shaped artefact passes its human-review step before export. 🔴 0★ — chosen because the grading census returns **zero** alternatives |
| 5 | audit trail | [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 MIT · 1,069 B · `4aa758cb51b2` | each agent turn emitted as an xAPI statement over MCP |
| 6 | record store | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 · 11,357 B · `c71d239df917` | queryable LRS — the district's evidence that a human decided, and the artefact a sceptical faculty senate can audit |

🔵 **Wiring.** `canvas-mcp` and `learnmcp-xapi` are both MCP servers, so one agent runtime mounts both: it *reads*
the course from Canvas and *writes* statements to `lrsql`, and the only write path in the whole design points at
the LRS. `pykt-toolkit` runs as a batch service over the LRS statement stream and returns a mastery vector that
`OATutor` consumes for sequencing; `AI-Teaching-Agent` sits in front of any export back to a human.
🟢 **Every component is permissive and every one except item 4 is demonstrably maintained.**
🔵 **Estimate 7–10 weeks** — judgement, not measurement (`Gap 479-AO`).

### 🟢 P15 — a Brazilian municipal engagement on working *software público*

🔵 **The engagement.** A Brazilian municipal or state secretariat already runs i-Educar — the largest free
school-management system in the country — and wants AI assistance for teachers without touching the system of
record. 🔴 i-Educar is **GPL-2.0** and its gradebook companion i-Diario is **AGPL-3.0 in an unofficial Portuguese
translation**, so the architecture is dictated by licence before anyone designs it.

| # | component | repo | grant (payload) | role |
|---|---|---|---|---|
| 1 | system of record | [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** · 18,092 B · `8177f9751321` | **stays deployed, unmodified, reached over its own HTTP API** — never forked, never linked into the deliverable; 721★ |
| 2 | curriculum spine | [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** · 1,092 B · `e162f8f4b461` | 1,721 BNCC objectives in JSON/SQLite/CSV — the alignment layer, and **permissive**, which the alternatives are not |
| 3 | teacher agent | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | 🟢 **MIT** · 1,078 B *(p478)* | local-first lesson and slide drafting with an **Ollama** adapter — runs inside a school network with no egress |
| 4 | offline delivery | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** · 1,097 B · `3c056b34a476` | learner delivery where connectivity is intermittent; 1,162★, v0.19.5 |
| 5 | audit trail | [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) + [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 MIT + Apache-2.0 | statements out of the agent, into a store the secretariat owns |

🔴 **What this recipe forbids, explicitly.** [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy)
is the best-structured curriculum knowledge graph this base has measured (1,644 knowledge points, 2,403
prerequisite edges, 6,723 problems, 4,165★) and it is **CC BY-NC 4.0 with the tool code inside the grant** — it
**cannot** be used in a paid municipal engagement. Item 2 is the permissive substitute, and it is Brazilian, which
is also why it fits.
🟡 **Licence boundary.** GPL-2.0 has no network clause, so item 1 over HTTP is a cleaner boundary than an AGPL-3.0
system would give — but i-Diario, if in scope, **is** AGPL-3.0, and then item 1's reasoning does not transfer.
🔵 **Estimate 9–13 weeks** — judgement, not measurement (`Gap 479-AO`).

### 🟢 P16 — the permissive-SIS decision, now that one exists

🔵 **The engagement.** A client wants student administration on a permissive base — no GPL, no AGPL, no LGPL — and
P13 was written when this base believed no permissive SIS existed. 🟢 One does. This recipe is the **decision**,
with both arms priced in the same units.

| arm | what you start from | grant | what you are buying | what you are paying |
|---|---|---|---|---|
| **A — port** | [projectfedena/fedena](https://github.com/projectfedena/fedena) | 🟢 **Apache-2.0** *(declared in `NOTICE`, 680 B)* | a working education domain model: students, enrolment, attendance, exams, fees — 547★, 560 forks | 🔴 a **2011** Ruby-on-Rails codebase: framework and Ruby upgrades, dependency archaeology, no measured cadence, and `Gap 479-M` on whether a `NOTICE` is the grant |
| **B — model** | [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** · 11,906 B · `cbac9a0fde05` | party, billing, scheduling and a maintained enterprise spine — 1,143★, updated the day of this pass | 🔴 **the student domain does not exist** and must be modelled; this is P13 item 1, still the largest unestimated piece on this shelf (`Gap 478-AM`) |
| **C — accept LGPL** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0-or-later** *(election read this pass)* | the ready-made education ERP on Odoo | 🔴 copyleft on the module boundary, with an upgrade option now confirmed |

🔵 **How to decide, on this pass's evidence.** 🟢 Arm A is right when the client's constraint is *licence* and the
domain is standard — the Apache-2.0 grant is the whole point and the domain model is already correct. 🟢 Arm B is
right when the client's constraint is *maintenance* and the domain is unusual, because an unmaintained correct
model costs more than a maintained empty one. 🔴 Arm A has never been run here and its upgrade cost is
**unmeasured**, so this recipe does not recommend one arm: it says that the choice is now real and names what to
measure first — Fedena's dependency manifest and last commit date, neither of which this pass read.
🔵 **Estimate: arm A 6–10 weeks *if* the port is clean (unquantified risk); arm B 10–14 weeks; arm C 4–6 weeks** —
judgement, not measurement (`Gap 479-AO`).

### 🔵 One component note for every recipe above

🔵 Four of the five recipes on this shelf now mount **two or more MCP servers in one agent runtime**
(`canvas-mcp`, `learnmcp-xapi`, `tutor-mcp`, `anki-mcp-server` where relevant). 🟢 That is the direct consequence
of Trend 1 on `intel/trends.md`: the unit of supply has become a skill or a server, so composition is increasingly
*mounting*, not *integrating*. 🔴 No pass of this base has ever started two of these servers in the same runtime
and checked that their tool namespaces, auth models and statement vocabularies do not collide — which is now the
single highest-value thing a future pass could actually execute.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 479-AO`** | **None of P14, P15 or P16 has been built or run**, and `Gap 478-AI` carries forward unchanged: no integration executed, no version compatibility tested, no xAPI profile validated against `lrsql`, and every week estimate is judgement. The corrections to P11–P13 are component swaps on measured liveness, **not** re-tested recipes. |
| 🔴 **`Gap 479-AP`** | **`canvas-mcp` is two days old and unexercised here.** P14's whole licence argument rests on it being read-only; that claim is read from its description and name, **not** from its source, its scopes or a transcript. If it can write, P14's boundary argument collapses. |
| 🔴 **`Gap 479-AQ`** | **`Gap 478-AK` persists in a narrower form.** P14's assessment gate is still a **0★** project whose README freezes grading productisation, chosen because the grading census returns zero alternatives. Selection is now on grant, liveness and description — **still never on capability**, because nothing was run. |
| 🔴 **`Gap 479-AR`** | **P16 arm A is unpriced.** Fedena's dependency manifest, Ruby and Rails versions, test suite and last commit were **not read**; "6–10 weeks if the port is clean" is a sentence, not an estimate, and the conditional is carrying all the risk. |
| 🟡 **`Gap 479-AS`** | **P15's licence boundary is architectural reasoning**, like every boundary on this shelf (`Gap 478-AL`): GPL-2.0-over-HTTP is read from the absence of a network clause, not from a determination about this codebase, and i-Diario's AGPL-3.0 **Portuguese translation** compounds the question rather than answering it. |
| 🟡 **`Gap 479-AT`** | **No recipe was checked for localisation fit**, repeating `Gap 478-AN`. P15 is the exception that proves the cost: it exists *because* the APAC-origin curriculum graph could not be used, and its substitute was available only because Brazil happens to have a permissive curriculum dataset. No other region was checked for one. |

---

## 🆕 `p478` — `2026-10-27` — **🟢 `Gap 477-AH` IS CLOSED — P10's entire licensing argument rested on `learnmcp-xapi`'s carried MIT and on `bncc-dados`, whose grant had NEVER been read in any pass; both are now payload reads and both are MIT. 🟢 Three new recipes, every component payload-verified, and each one shaped by a constraint the other shelves measured this pass rather than by what is popular.**

🔵 Gate posture unchanged (`Code from External`; `make hooks` not attempted; session-local checks green).
Grants in [`evidence/grant-payload.2026-10-27-p478.tsv`](../evidence/grant-payload.2026-10-27-p478.tsv).

---

### 🟢 `Gap 477-AH` closed

| component | `p477` status | payload this pass |
|---|---|---|
| [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | MIT, **carried** | 🟢 **MIT** · 1,069 B · `4aa758cb51b2` |
| [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🔴 **never read in any pass** — "open data, from its own README" | 🟢 **MIT** · 1,092 B · `e162f8f4b461`, held by *Profy Tecnologias Educacionais Ltda* |

🔵 P10's licensing argument now rests on two payload reads instead of two descriptions. 🟡 **And it is narrower
than "open data" implied**: MIT covers the repository's contents as distributed by that company; it says nothing
about the BNCC curriculum as a public instrument, which is a separate question this base has not examined.

---

### 🟢 P11 — provable human-in-the-loop tutoring for a US district or university

🔵 **Driven by:** Idaho S.B. 1227 bars AI from replacing teachers (effective 1 July 2026); Ohio, Tennessee and
Maryland require district-level AI policy; ~34 states have guidance; and `intel/trends.md` Trend 1 found that
*open-ended tutor access* lowered grades by 0.37 SD while *course-grounded* tutors raised scores. **Both the law
and the evidence point at the same build: bounded scope plus a provable human decision.**

| # | component | repo | grant (payload) | role |
|---|---|---|---|---|
| 1 | learner surface | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | 🟢 MIT · 1,065 B | topic/document → interactive classroom; 41.6k★ |
| 2 | mastery estimate | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT · 1,066 B | knowledge tracing — a **computed** mastery state, not the LLM's opinion |
| 3 | assessment gate | [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent) | 🟢 MIT · 1,069 B | anything assessment-shaped goes through its human-review step before export |
| 4 | audit trail | [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 MIT · 1,069 B | every turn emitted as an xAPI statement over MCP |
| 5 | record store | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 · 11,357 B | queryable LRS; the district's evidence that a human decided |
| 6 | the LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** · 34,520 B | **stays a separate deployed service**, reached over LTI/REST — never forked, never linked |

🟢 **Wiring.** OpenMAIC is configured against the course's own materials only — that bounded scope *is* the
intervention, per Trend 1. Each turn goes out through `learnmcp-xapi` into `lrsql`, so "what the tutor displaced"
is measurable rather than assumed. `pykt-toolkit` consumes the same xAPI stream to maintain mastery, and
sequencing reads that state instead of asking the model. Anything that could score a student is routed to
`AI-Teaching-Agent`, whose human-review gate produces the artefact a district policy audit needs. Canvas is
touched only over its API: items 1–5 are MIT/Apache-2.0, so **the deliverable's licence stays the studio's**.

🔵 **Estimate 8–11 weeks** — judgement, not measurement (`Gap 478-AI`).

### 🟢 P12 — an EU Annex III high-risk tutoring file, built on the one permissive LMS

🔵 **Driven by:** admissions, grading, placement and proctoring are Annex III **high-risk**; emotion recognition
in schools is **prohibited outright** since 2 February 2025; Article 50 transparency applies from 2 August 2026;
and the Act reaches non-EU systems whose outputs affect EU-located students. 🔴 Note what this recipe **cannot**
use: [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) is the
best-fitting EMEA component at 916★ and its grant was read this pass as **CC BY-SA 4.0** — share-alike follows
its 165 prose skills into any derivative, so it is excluded from a proprietary deliverable by design, not by
oversight.

| # | component | repo | grant (payload) | role |
|---|---|---|---|---|
| 1 | platform | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · 10,982 B | university/corporate LMS — **the only permissive LMS at this scale**; avoids Moodle's GPL-3.0 and Canvas's AGPL-3.0 |
| 2 | adaptive core | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 MIT · 1,073 B | BKT-driven ITS over MCP; EMEA-origin, permissive |
| 3 | mastery models | [bigdata-ustc/EduKTM](https://github.com/bigdata-ustc/EduKTM) | 🟢 Apache-2.0 · 11,367 B | knowledge-tracing models behind the sequencing decision |
| 4 | interop contract | [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 🟢 Apache-2.0 · 11,525 B | the statement vocabulary the logging obligation is written against |
| 5 | record store | [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | 🟢 Apache-2.0 · 11,357 B | xAPI 1.0.3 + 2.0; embedded PGlite mode for a single-tenant EU deployment |
| 6 | human oversight | [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent) | 🟢 MIT · 1,069 B | the review gate in front of every grading-shaped output |

🟢 **Wiring.** Six components, **six permissive grants** — the whole stack is Apache-2.0/MIT, which is what makes
the Annex III documentation tractable: the studio can describe, log and modify every layer it is accountable for.
`tutor-mcp` drives sequencing from `EduKTM`'s mastery estimate; every decision is written as an xAPI statement
into `xapi-lrs`, giving the record-keeping and traceability the high-risk regime expects; `AI-Teaching-Agent`
supplies the documented human oversight on the grading path. 🔴 **Two hard exclusions are part of the design:**
no emotion or affect inference anywhere (prohibited, €35M / 7 % exposure), and **no fully automated grading** —
grading stays decision-support behind item 6.

🟡 **The deadline this recipe must plan against is contested** — 2 August 2026 per several guides, 2 December 2027
per Regulation (EU) 2026/1744 as reported — and 🔴 **EUR-Lex is refused at this environment's gateway**, so build
to the earlier date (`Gap 478-AJ`).

🔵 **Estimate 12–16 weeks** — judgement, not measurement (`Gap 478-AI`).

### 🟢 P13 — permissive school administration where no permissive SIS exists

🔵 **Driven by:** `verticals/solutions.md` established this pass that **no payload-verified permissive student
information system exists** — RosarioSIS is GPL-2.0, Gibbon GPL-3.0, OpenEduCat LGPL-3.0, and GegoK12's MIT claim
has **no repository that resolves at any probed address**. So the permissive spine has to be a general ERP.

| # | component | repo | grant (payload) | role |
|---|---|---|---|---|
| 1 | ERP spine | [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** · 11,906 B | party, enrolment, billing and scheduling on a permissive base; the student domain is modelled on top |
| 2 | offline delivery | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** · 1,097 B | low-connectivity learner delivery — the one permissive **platform** in this base |
| 3 | curriculum spine | [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** · 1,092 B | 1,721 BNCC objectives in JSON/SQLite/CSV — the Brazilian alignment layer |
| 4 | learner records | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 · 11,357 B | xAPI store that survives intermittent connectivity and syncs later |
| 5 | teacher agent | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | 🟢 **MIT** · 1,078 B | local-first lesson/slide drafting with an **Ollama** adapter — runs without egress |
| 6 | fallback, if LGPL is acceptable | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL-3.0 · 8,241 B | the ready-made education ERP — **buy the time instead of building item 1** |

🟢 **Wiring.** OFBiz carries parties, enrolments and scheduling; the student domain is built as OFBiz components
rather than forked from a GPL SIS, which is the whole point — item 1 is Apache-2.0 and items 2–5 are MIT or
Apache-2.0, so **every layer is permissive and no copyleft obligation reaches the deliverable**. Kolibri delivers
content offline and syncs xAPI into `lrsql` when a link appears; `bncc-dados` aligns both to BNCC objectives;
`Claw-ED` runs the teacher's drafting locally against Ollama, so a school with no reliable egress still gets the
AI layer. 🟡 **Item 6 is the honest alternative:** LGPL-3.0 permits linking proprietary modules and is the
**least restrictive copyleft** available here — where the schedule matters more than the licence, take OpenEduCat
and skip the OFBiz build.

🔵 **Estimate 10–14 weeks for items 1–5; 5–7 weeks via item 6** — judgement, not measurement (`Gap 478-AI`).

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 478-AI`** | **None of P11, P12 or P13 has been built or run.** `Gap 477-AI` carried forward unchanged: no integration executed, no version compatibility tested, no xAPI profile validated against `lrsql` or `xapi-lrs`, and every week estimate is judgement. |
| 🔴 **`Gap 478-AJ`** | **P12 is built against a contested date this base cannot settle.** 2 August 2026 vs 2 December 2027 for stand-alone Annex III systems; EUR-Lex is refused at the gateway (`Gap 478-W`). The recipe plans to the earlier date, which is a choice, not a reading. |
| 🔴 **`Gap 478-AK`** | **`Gap 477-AK` worsens: component selection is still on stars, grant and description, never capability.** P11's and P12's human-oversight gate is `AI-Teaching-Agent` — a **0★** project whose own README says grading productisation is frozen, chosen because it is the only MIT project in the category. Its output has not been seen. |
| 🔴 **`Gap 478-AL`** | **P11's premise that Canvas-over-API is not a derivative work is architectural reasoning**, not a reading of Canvas's LTI/REST boundary or of AGPL-3.0 § 13. `Gap 477-AL` applies to all three recipes. |
| 🟡 **`Gap 478-AM`** | **P13 item 1 is the largest unestimated piece in any recipe here.** "Model the student domain on OFBiz" is a sentence; OpenEduCat exists because that work is substantial. The 10–14 week figure is the least supported number on this shelf. |
| 🟡 **`Gap 478-AN`** | **No recipe was checked for localisation fit.** P11's learner surface (`OpenMAIC`) and P13's teacher agent (`Claw-ED`) are both used outside their origin language and curriculum, repeating `Gap 477-AK`'s unassessed localisation risk. |

---

## 🆕 `p477` — `2026-10-27` — **two new recipes built only from components whose grant was read first-hand THIS pass, plus a correction that touches every recipe in retained history: any recipe naming `danny-avila/LibreChat` must read `LibreChat-AI/LibreChat`, and `P7`'s biometric exclusion is now justified by READ CODE rather than by repository descriptions**

🔵 Component grants are the first-hand reads in
[`evidence/grant-payload.2026-10-27-p477.tsv`](../evidence/grant-payload.2026-10-27-p477.tsv) (27 rows);
elections in [`evidence/version-election.2026-10-27-p477.tsv`](../evidence/version-election.2026-10-27-p477.tsv).
🔴 No recipe below uses an AGPL-3.0 or NonCommercial component in a position where a client would need to keep
modifications closed or ship the asset. Where a copyleft component is used it is **deployed, not linked**, and the
recipe says so.

🔴 **Address correction that touches retained history.** Any recipe below or above naming
**`danny-avila/LibreChat`** should read **[`LibreChat-AI/LibreChat`](https://github.com/LibreChat-AI/LibreChat)**
(46,367★, MIT, 1,066 B, read this pass). Same repository, moved to an organisation; the old address still resolves
on git and raw but is **absent from the search index even with `fork:true`**. This is the second such correction
in two passes — `openedx/edx-platform` → `openedx/openedx-platform` was the first.

🟢 **`Gap 476-V` discharged for P7, and it changes the recipe.** P7 excluded `elimu-ai/ml-authentication` on the
strength of a repository description. The component was **cloned and read** this pass: there is no upload path
anywhere in it, so the biometric data never crosses a network boundary — but face crops are written to
`Environment.getExternalStorageDirectory()` under `targetSdkVersion 23`, i.e. **shared storage readable by any
other app on the handset**. 🔴 **P7's exclusion of the component therefore stands and its justification changes
from "we cannot verify the data flow" to "the data flow is verified and the at-rest exposure is the problem."**

---

### 🟢 P9 — Auditable AI tutoring for a US district facing a policy deadline

🔵 **Why this is buildable now:** `intel/market.md` this pass measured the opening — Ohio compels every district to
adopt an AI policy by **1 July 2026** and Oklahoma before 2027–28, while reviewers of the 2026 state bills note
that proposals **do not require vendors to supply auditable interaction records**. The district owes evidence and
no product supplies it. Target region: **North America**.

| # | component | repo | grant (read first-hand) | role |
|---|---|---|---|---|
| 1 | LTI 1.3 entry point | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** · 11,361 B | launches the tutor from inside Canvas as a certified tool |
| 2 | learning record store | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** · 11,357 B | immutable xAPI statement store — **the audit artefact** |
| 3 | agent → LRS bridge | [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | MIT (carried, `Gap 477-AH`) | every tutor turn written as an xAPI statement over MCP |
| 4 | mastery model | [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | 🟢 **MIT** · 1,132 B | Bayesian Knowledge Tracing — defensible mastery claims |
| 5 | scheduler | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** · 1,079 B | FSRS review scheduling |
| 6 | LMS of record | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 🔴 **deployed, not linked** — reached only over LTI/REST |

🔵 **Wiring.** Canvas launches the tutor through `ltijs` (LTI 1.3 Resource Link); the tutor's mastery state comes
from `pyBKT` and its review queue from FSRS; **every** learner-facing turn — prompt, response, model id,
timestamp, learner id — is emitted as an xAPI statement through `learnmcp-xapi` into `lrsql`. The district's
policy evidence is then a query against the LRS, not a vendor report. 🟢 **Licensing:** items 1–5 are permissive
and carry the client's code; Canvas is a deployed system reached across a process boundary, so AGPL-3.0 never
reaches the studio's work. 🔵 **Estimate 7–9 weeks** — judgement, not measurement (`Gap 477-AI`).

### 🟢 P10 — BNCC-aligned tutor for a LATAM ministry, curriculum licence cleared up front

🔵 **Why this recipe exists:** `intel/market.md` this pass found that APAC's best curriculum graph —
`cn-math-taxonomy`, 4,148★ — is **CC BY-NC 4.0** and so cannot be shipped to a paying client, while LATAM's
equivalent is **open data with per-record provenance**. The region usually treated as the thin one holds the asset
that is actually deliverable. Target region: **LATAM**.

| # | component | repo | grant (read first-hand) | role |
|---|---|---|---|---|
| 1 | curriculum spine | [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | open data, provenance per record (`Gap 477-AH`) | **1,721 BNCC learning objectives** in JSON/SQLite/CSV |
| 2 | curriculum access | [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes) | carried | npm/PyPI packages + MCP server — the spine in one line |
| 3 | tutor runtime | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **MIT** · 1,065 B | multi-agent interactive classroom, 41,603★ |
| 4 | mastery model | [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | 🟢 **MIT** · 1,132 B | per-objective mastery against BNCC codes |
| 5 | SIS of record | [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 (carried) | 🔴 **deployed, not linked** — already live in Brazilian municipalities |
| 6 | record store | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** · 11,357 B | xAPI evidence, same audit role as P9 |

🔵 **Wiring.** `bncc-pacotes` serves the BNCC graph to `OpenMAIC` over MCP, so every generated activity carries a
real BNCC objective code rather than a model's guess at one; `pyBKT` tracks mastery **per objective code**, which
is what a secretariat reports on; `i-educar` stays the enrolment and gradebook system of record and is reached only
over its own interfaces. 🟢 **Licensing:** the curriculum is open data with provenance, the tutor and mastery model
are MIT, the SIS is deployed. **Nothing in the deliverable is NonCommercial.** 🔵 **Estimate 8–10 weeks**
(`Gap 477-AI`).

🔴 **The guardrail that makes this sellable in LATAM specifically:** `intel/market.md` records commentary that
classroom AI is spreading there *"often without oversight or guidelines"*, with Brazil's PL 2338 still in the
Chamber of Deputies and Mexico having approved nothing. Arriving with the xAPI audit trail and BNCC traceability
already built is differentiation, not compliance cost — the opposite posture to EMEA, where the Annex III clock
drives the sale.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 477-AH`** | **Three components are named on carried or unread grants:** `learnmcp-xapi` (MIT, carried), `bncc-pacotes` (carried), and `bncc-dados`'s grant was **never read first-hand in any pass** — it is described as open data from its own README. P10's entire licensing argument rests on item 1, and item 1 is the one row in it with no payload read. |
| 🔴 **`Gap 477-AI`** | **Neither recipe has been built or run** — `Gap 476-T`/`Gap 475-V` carried forward unchanged. No integration was executed, no version compatibility tested, no xAPI profile validated against `lrsql`, and both week estimates are judgement. |
| 🔴 **`Gap 477-AJ`** | **P9's premise that no vendor supplies auditable records is read from commentary on the state bills**, not from a procurement review. If Canvas or a major vendor already emits a compliant xAPI trail, P9 rebuilds something a district can buy. |
| 🟡 **`Gap 477-AK`** | **`OpenMAIC` is chosen for P10 on stars and grant, not on capability.** It was not run, and no grading- or teaching-quality evaluation of any agent on these shelves has ever been performed here (`Gap 476-W`). Its Chinese-language origin against a Portuguese-language curriculum is an **unassessed** localisation risk. |
| 🟡 **`Gap 477-AL`** | **"Deployed, not linked" is asserted per recipe, not verified per component.** Whether a given integration genuinely crosses a process boundary — rather than importing an AGPL/GPL library in passing — was not checked by reading either platform's plugin API this pass. |

---


## 🆕 `p476` — `2026-10-27` — **two new recipes and one upgraded, each built only from components whose grant, version election and address were read first-hand this pass — plus the correction that `Gap 475-X`'s "unperformed work inside the recipe" HAS NOW BEEN PERFORMED: OpenEduCat's bundled-library enumeration came back clean, 14 of 14 modules LGPL-3**

🔵 Component grants are the first-hand reads in
[`evidence/grant-payload.2026-10-27-p476.tsv`](../evidence/grant-payload.2026-10-27-p476.tsv); version
elections in [`evidence/version-election.2026-10-27-p476.tsv`](../evidence/version-election.2026-10-27-p476.tsv);
the depth probe in [`evidence/openeducat-depth.2026-10-27-p476.tsv`](../evidence/openeducat-depth.2026-10-27-p476.tsv).
🔴 No recipe below uses an AGPL-3.0 or bespoke-licensed component in a position where a client would need to
keep modifications closed. Where a copyleft component is used it is **deployed, not linked**, and that is
stated in the recipe.

🔴 **Address correction that touches every earlier recipe on this shelf.** Any recipe below or in retained
history naming `openedx/edx-platform` should read **`openedx/openedx-platform`**. Same repository, same HEAD,
same grant — the old address resolves on git and raw but is dead to the search index.

---

### 🟢 P7 — Offline-first primary literacy platform for African deployments, fully permissive, biometrics designed OUT

🔵 **Why this is now buildable:** `Gap 475-M` was closed this pass — there is an African education platform
and its entire stack is **MIT**, the first time this base has had a permissive vertical to build on rather
than a copyleft LMS to work around.

| # | component | repo | grant (read first-hand) | role |
|---|---|---|---|---|
| 1 | platform / CMS / REST API | [elimu-ai/webapp](https://github.com/elimu-ai/webapp) | **MIT** · 1,065 B · `45fc137a7066` | Java/Spring content and app host; the system of record |
| 2 | device shell | [elimu-ai/launcher](https://github.com/elimu-ai/launcher) | **MIT** · 1,065 B · `45fc137a7066` | locked Android launcher giving a fixed instructional path; EGRA/EGMA framing |
| 3 | content distribution | [elimu-ai/appstore](https://github.com/elimu-ai/appstore) | **MIT** · 1,065 B · `45fc137a7066` | pulls/updates APKs and content — **the offline-first hinge** |
| 4 | shared domain model | [elimu-ai/model](https://github.com/elimu-ai/model) | **MIT** · 1,065 B · `45fc137a7066` | one Java library across webapp and Android |
| 5 | reading-level inference | [elimu-ai/ml-storybook-reading-level](https://github.com/elimu-ai/ml-storybook-reading-level) | **MIT** · 1,065 B · `6af12447a42c` | TensorFlow model grading storybook difficulty; on-device capable |
| 6 | tutoring agent | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 11,408 B · `cd2f54e1e506` | multi-agent + RAG tutoring; **run as a service behind the webapp**, not linked into it |
| 7 | 🔴 **a hard exclusion, not a component** | ~~[elimu-ai/ml-authentication](https://github.com/elimu-ai/ml-authentication)~~ | MIT · `203d7d837ceb` | **DO NOT SHIP.** Face recognition on pupils is biometric identification — EU Annex III high-risk from 2 Dec 2027 and high-risk under Vietnam's Decision 33. Replace with a class-roster PIN or teacher-selected pupil list. |

🟢 **Licence boundary: there isn't one to manage.** Every component is MIT or Apache-2.0, so client
modifications may stay closed and nothing has to be isolated out-of-process for licence reasons. 🔵 DeepTutor
is kept behind a service boundary for **operational** reasons (model hosting, cost control), not legal ones.
🔴 **Regulatory boundary: component 7 is the whole of it.** Dropping it takes the estate out of the biometric
category in both jurisdictions; adding it back makes the deployment a conformity-assessment event in the EU
and a third-party-certification event in Vietnam. **Estimated 8–10 weeks** to a deployable pilot on existing
Android hardware.

🔴 **What a client must be told up front:** the top repo has **41★** and its bus factor is unmeasured
(`Gap 476-J`). This is a small project with the right architecture and the right licence — adopting it means
accepting maintenance exposure that Moodle would not carry.

### 🟢 P8 — The human-in-the-loop grading gate: one design that satisfies Vietnam's 1 Mar 2027, the EU's 2 Dec 2027 and US state rules at once

🔵 **Why this is now specifiable:** the scoping qualifier found this pass. Vietnam's Decision 33 treats
listed systems as high-risk **only where the AI output is the sole basis for a decision without meaningful
human review** — so the gate is not a mitigation, it is the thing that decides the risk tier.

| # | component | repo | grant · election (first-hand) | role |
|---|---|---|---|---|
| 1 | LMS of record | [moodle/moodle](https://github.com/moodle/moodle) | **GPL-3.0**, 🟢 `or-later` **elected** (`composer.json` + source notices) | gradebook, roster, audit surface. 🔴 **Deployed, not linked** — no client code compiled against it |
| 2 | grading agent | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | **Apache-2.0** · 11,342 B · `c00cbb6a47a7` | script-driven teaching/marking assistant; client logic lives **here**, in the permissive component |
| 3 | content/assessment authoring | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | **GPL-3.0**, 🟡 bare id — no election | interactive items. **Deployed as a Moodle plugin**, never linked into client code |
| 4 | 🟢 **the gate itself** | — (client-built, in component 2) | — | every AI mark enters the gradebook as a **draft** that a named teacher must confirm or override; the confirm/override event is logged with teacher identity and timestamp |
| 5 | evidence store | client-built | — | retains, per mark: model version, input, draft output, teacher decision, latency. **This is the conformity-assessment artefact** |

🟢 **Why one design covers three regimes.** Vietnam: the AI output is not the sole basis, by construction.
EU: Annex III high-risk duties centre on human oversight, and components 4–5 are that oversight plus its
evidence. North America: the same log answers state transparency rules, and keeping inference self-hosted
answers **California AB 1159**'s bar on training against student data. 🔴 **It does not make the EU
obligations disappear** — grading stays Annex III-listed; the gate and the log are what a conformity
assessment is assessed *on*. **Estimated 6–8 weeks**, plus 2 weeks if self-hosted inference is in scope.

🔴 **The failure mode to design against is auto-confirm.** A gate that teachers clear in bulk with one click
restores "sole basis" in substance while appearing compliant. The log must make bulk-confirm visible —
confirm-rate and dwell-time per teacher are the metrics that show whether the gate is real.

### 🟢 P3 upgraded — `Gap 475-X` discharged: the OpenEduCat enumeration is done, and it came back clean

🔵 `Gap 475-X`: *"P3 ships a `SPLIT_SCOPE` component knowingly… the bundled-library enumeration is
**unperformed work inside the recipe**."* 🟢 It was performed this pass, by shallow clone at HEAD
`46a5d7d400820d471b67b8c019997bfa5d3c873e`.

| question `Gap 475-N`/`475-X` asked | 🟢 measured answer |
|---|---|
| which modules carry which terms? | **14 of 14 declare `LGPL-3`** — uniform, no exceptions |
| what does `openeducat_admission` (the highest-risk module) carry? | **`LGPL-3`**, same as every sibling |
| how many licence files exist below the root? | **zero** — exactly one in the whole 17 MB tree |
| is the `SPLIT_SCOPE` real? | 🟢 **declared, not instantiated** — a forward-looking disclaimer nothing in the tree exercises |
| version election? | 🟢 **`LGPL-3.0-or-later`**, from per-source-file notices in **187 of 209** `.py` files |

🟢 **Effect on the recipe: the pre-delivery blocker is cleared.** P3 may ship
[openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) (899★, `19.0`, LGPL-3.0-or-later)
as its SIS layer with the enumeration **done** rather than pending. LGPL weak copyleft still means
**deploy the modules, do not statically link client code into them**; Odoo-style module boundaries make that
the natural shape anyway. 🔴 **Two residual defects to carry into delivery docs:** the payload points at a
`COPYRIGHT` file that **does not exist in the tree**, and `openeducat_timetable` declares a malformed version
string (`19.0.1.1.0`). Neither changes the terms; both will confuse an automated licence scanner.

### 🔴 Gaps this pass registers

| gap | statement |
|---|---|
| 🔴 **`Gap 476-T`** | **No recipe here has been built or run** — `Gap 475-V` carried forward unchanged. P7 and P8 are compositions of components whose grants, elections and addresses were verified first-hand; **no integration was executed**, no version compatibility tested, and the week estimates are judgement, not measurement. |
| 🔴 **`Gap 476-U`** | **P8's entire premise rests on secondary legal summaries.** The "sole basis / meaningful human review" qualifier is the load-bearing element of the recipe and it was read from law-firm commentary, **not from Decision 33's annex** (`Gap 476-H`). If the annex scopes it differently, P8 is a good design that does not change the risk tier. A client deliverable must read the annex and EUR-Lex first-hand. |
| 🟡 **`Gap 476-V`** | **P7's exclusion of `ml-authentication` assumes the rest of the stack carries no other biometric or monitoring surface.** Only repository descriptions were read; no component was cloned or code-reviewed, so an attention-tracking or camera feature elsewhere in the 66-repo org would be missed (`Gap 476-I`). |
| 🟡 **`Gap 476-W`** | **P8 names `ai-shifu` (329★) as the component carrying client logic** — chosen because it is Apache-2.0 and purpose-built for scripted teaching, not because it was benchmarked against alternatives. No grading-quality evaluation of any agent on this shelf has ever been run here. |

## 🆕 `p475` — `2026-10-27` — **three recipes whose every component's grant was read first-hand at a resolved HEAD this pass, each one specified so the licence boundary AND the regulatory boundary fall where they actually fall**

🔵 Component grants are the first-hand reads in
[`evidence/grant-payload.2026-10-27-p475.tsv`](../evidence/grant-payload.2026-10-27-p475.tsv).
🔴 No recipe below uses an AGPL-3.0 or bespoke-licensed component in a position where a client would
need to keep modifications closed. Where a copyleft component is used, it is **deployed, not linked**,
and that is stated in the recipe.

---

### 🟢 P1 — "Article 50 retrofit": machine-readable AI disclosure across an existing EU school estate

🔵 **Why now:** EU Article 50 transparency has applied since **2 Aug 2026**, and systems already on the
market must carry **machine-readable content marking by 2 Dec 2026** — ~5 weeks from this pass. This is
the nearest hard deadline in this KB.

| part | component | grant | role |
|---|---|---|---|
| LMS of record | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 · `main/COPYING.txt` · 35,147 B | 🔴 **Deployed, not linked.** The marking layer is a separate service; nothing is statically bound into Moodle |
| Marking + disclosure service | new, studio-owned | client's own | Stamps provenance metadata on AI-generated teaching material; renders the "you are interacting with AI" disclosure on chat surfaces |
| Content type layer | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 35,146 B | Interactive content; marking applies at render time |
| Tutoring surface (optional) | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · 11,408 B · `cd2f54e1e506` | The one high-star tutor a client can embed in proprietary code |

🔵 **Wiring:** Moodle emits content events → marking service attaches C2PA-style provenance and a
disclosure flag → H5P render hook and DeepTutor chat surface both read the flag and display disclosure.
🔴 **Boundary:** Moodle and H5P are GPL-3.0 and stay **out-of-process**; the marking service talks to
them over HTTP and the plugin shim stays GPL-3.0 and is published. 🟢 DeepTutor is Apache-2.0 and may
be embedded directly. **Estimated 4–6 weeks** for a single-estate retrofit.

---

### 🟢 P2 — "One codebase, four regions": removable grading-autonomy and biometric modules

🔵 **Why:** the EU bans emotion recognition in education outright; Vietnam regulates biometric
monitoring as high-risk with a **1 Sep 2027** retrofit deadline; US states restrict AI from *replacing*
a licensed educator in grading. One product, three incompatible defaults.

| part | component | grant | role |
|---|---|---|---|
| LMS core | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `master/LICENSE` · 10,982 B · `6dbc5b605ed0` | 🟢 The permissive full LMS — client modifications stay closed |
| Low-connectivity edge | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** · `develop/LICENSE` · 1,097 B | Offline-first deployments; 🟢 **no biometric surface at all** |
| Assistant | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | 🟢 **Apache-2.0** · `main/LICENSE.txt` · 11,342 B | Script-driven teaching agent, embeddable |
| Grading autonomy | **feature flag**, studio-owned | client's own | `SUGGEST_ONLY` (US default) · `SUGGEST_ONLY` + logged human sign-off (EU/VN) · `AUTONOMOUS` (unregulated markets) |
| Biometric/affect | **build-time module**, studio-owned | client's own | 🔴 **Absent from the EU build.** Not a runtime flag — compiled out, because the EU position is prohibition, not conformity |

🔵 **Wiring:** OpenOLAT assessment hooks call a policy gate before any grade is written; the gate reads
a per-deployment region profile (`NA` / `EMEA` / `APAC` / `LATAM`) and either writes, queues for human
sign-off, or refuses. The biometric module is excluded by build profile, not configuration, so an EU
artefact cannot be mis-flagged into compliance. 🔴 **Boundary:** every component is Apache-2.0 or MIT —
**no copyleft anywhere in this recipe**, deliberately, because the whole point is a closed client build.
**Estimated 10–12 weeks.**

---

### 🟢 P3 — "Policy instrumentation for LATAM institutions": the 87 %-adoption / 26 %-strategy gap

🔵 **Why:** UNESCO IESALC measured 87 % of LATAM higher-education institutions already using AI against
26 % with a formal AI strategy. The deliverable is not compliance against a statute — there mostly
isn't one yet — it is the institutional policy and the instrumentation that evidences it.

| part | component | grant | role |
|---|---|---|---|
| SIS / ERP of record | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 · `19.0/LICENSE` · 8,241 B · 🔴 `SPLIT_SCOPE` | Admissions, enrolment, fees. 🔴 **Weak copyleft + bundled libraries disclaimed — walk the tree before shipping** |
| LMS | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | ECL-2.0 · 11,120 B · `0688f62d04f1` | 🟡 Consortium-friendly; patent grant narrowed to the contributor's own contributions (`p474`) |
| Virtual classroom | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 · `v4.0.x-develop/LICENSE` · 7,652 B | 🔴 Deploy **with engagement analytics off** — it is the module that would make this high-risk in EU/VN if the institution later operates cross-border |
| Tool inventory + attestation | new, studio-owned | client's own | Which AI tools are in use, by which faculty, against which policy clause; produces the annual disclosure artefact |
| Tutoring | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 · 11,408 B | Embeddable without licence contamination |

🔵 **Wiring:** OpenEduCat is the identity and enrolment spine; Sakai and BigBlueButton register their
AI-touching features with the inventory service; the attestation layer renders an institutional AI
strategy document populated from live tool registrations rather than a questionnaire. 🔴 **Boundary:**
OpenEduCat and BigBlueButton are LGPL-3.0 — link dynamically, keep studio code in separate modules, and
**enumerate OpenEduCat's bundled-library terms before delivery** (`Gap 475-N`). **Estimated 8–10 weeks.**

---

### 🔴 Gaps these recipes carry

| gap | statement |
|---|---|
| 🔴 **`Gap 475-V`** | **No recipe here has been built or run.** Every one is a composition of components whose *grants* and *addresses* were verified first-hand this pass; **no integration was executed**, no version compatibility was tested, and the week estimates are judgement, not measurement. |
| 🔴 **`Gap 475-W`** | **P1's 2 Dec 2026 deadline and P2's regional profiles rest on secondary legal sources** (`Gap 475-L`, `Gap 475-R`). A client deliverable must re-read EUR-Lex and Decision 33's annex first-hand. The engineering boundaries (out-of-process GPL, build-time exclusion) are sound regardless of the dates; the **urgency** claim is not. |
| 🟡 **`Gap 475-X`** | **P3 ships an `SPLIT_SCOPE` component knowingly.** OpenEduCat is the only open education ERP this base has found, so the recipe uses it and flags it rather than omitting the SIS layer — but the bundled-library enumeration is **unperformed work inside the recipe**, not a caveat about it. |


## 🆕 `p474` — `2026-10-27` — **three recipes whose parts were all grant-verified by payload read this pass: the evidence dossier North America and Europe are both legislating toward, the Brazilian public-education stack with its two AGPL triggers held outside the AI layer, and a national-curriculum agent built on the one country that has published curriculum, interface and benchmark together.**

🔵 Every repository named below was address-resolved by `git ls-remote --symref` and grant-verified
by payload read from `raw.githubusercontent.com` this pass; bytes and digests are in
[`evidence/grant-class.2026-10-27-p474.tsv`](../evidence/grant-class.2026-10-27-p474.tsv) and
[`evidence/grant-lang-scope.2026-10-27-p474.tsv`](../evidence/grant-lang-scope.2026-10-27-p474.tsv).
🔴 No pattern here composes a row whose grant was taken from an index, a README badge or a
comparison table. 🔴 **And no pattern here ships a `SPLIT_SCOPE` corpus into a deliverable** — where
one is used, the boundary is stated.

---

### 🟢 `P474-1` — The evidence dossier: one telemetry spine, three jurisdictions' paperwork

🔵 **When to reach for it.** The client must *show its working* on AI-assisted learning. In the US
that is Idaho SB 1227's framework or Oklahoma's "not the main basis for grading"; in Europe it is
the AI Act's high-risk duties and, shortly, the Council of Europe's evaluation framework; in MEA it
is a national-strategy alignment memo. 🔴 **The trap this avoids:** building a separate compliance
artefact per jurisdiction, when the underlying evidence is the same evidence.

**The parts — all permissive whole-work, all verified this pass or carried from `p473`'s LRS tier:**

| role | repo | grant |
|---|---|---|
| Learning Record Store | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 (`p473`, 11,357 B `c71d239df917`) — SQL-backed, so the client's BI team can query it |
| xAPI pipeline | [openfun/ralph](https://github.com/openfun/ralph) | 🟢 MIT (`p473`, 1,094 B `08ea77291de9`) |
| Reliability evaluation | [kaushikatla-cell/EduSafeBench](https://github.com/kaushikatla-cell/EduSafeBench) | 🟢 MIT — 1,056 B `1126322e2cc8` |
| Tutoring-quality evaluation | [Handshake-AI-Research/studentbench](https://github.com/Handshake-AI-Research/studentbench) | 🟢 MIT — 1,078 B `3cb4c0b9467a` |
| Contamination-proof item generation | [chenhz01/scireason-forge](https://github.com/chenhz01/scireason-forge) | 🟢 Apache-2.0 — 11,938 B `7cae8b289d20` |

**How to wire it.**
1. Every AI interaction emits an **xAPI statement** — actor, verb, object, result, and the model and
   prompt version — into `lrsql`. `ralph` handles ingest and transforms.
2. The **human-oversight gate** is a statement type, not a UI feature: any AI-proposed grade or
   intervention writes a `proposed` statement, and a teacher action writes the `confirmed` or
   `overridden` statement. 🟢 That single pair satisfies Oklahoma's "not the main basis", Idaho's
   "not replacing teachers" and the AI Act's "able to intervene and override" **from one record.**
3. **Evaluation runs on a schedule, not once at launch**: `EduSafeBench` for reliability,
   `studentbench` for tutoring quality, and `scireason-forge` to generate fresh items each cycle.
4. 🟢 **Why `scireason-forge` and not a bigger corpus:** its items are *generated and solver-graded*,
   so there is **no third-party item bank in the deliverable** — and no contamination claim against
   an evaluation whose items did not exist when the model was trained.
5. The dossier is a **view over the LRS**, rendered per jurisdiction. The evidence does not change;
   the template does.

🔴 **The part to refuse:** do not seed the item bank from
[`arquimedes`](https://github.com/richer-richard/arquimedes) despite its 1,038,963 problems. Its
LICENSE retracts the project's own CC BY claim over `problems/`, points at third-party terms, and
**CEMC material is CC BY-NC**. 🟡 Its *harness* (`arquimedes/`, `tools/`) is MIT and may be used.

🔵 **Shape:** 8–10 weeks for the spine plus the first jurisdiction's dossier; each additional
jurisdiction is a template, ~1–2 weeks.

---

### 🔴 `P474-2` — Brazilian public education: an AI layer outside two different copyleft triggers

🔵 **When to reach for it.** A Brazilian municipal or state secretariat runs Portabilis software —
the largest free school-software estate in the country — and wants AI for enrolment triage,
attendance-risk flagging or gradebook assistance.

🔴 **The boundary, measured this pass and not assumed:**

| component | grant (read first-hand) | trigger |
|---|---|---|
| [i-educar](https://github.com/portabilis/i-educar) — school information system | GPL-2.0-or-later, `2.12/LICENSE` 18,092 B `8177f9751321` | 🟡 distribution |
| [i-diario](https://github.com/portabilis/i-diario) — gradebook | 🔴 **AGPL-3.0-or-later**, `1.6/LICENSE` 35,326 B `fe85f94658bf` *(Portuguese)* | 🔴 **network use** |
| [pre-matricula-digital](https://github.com/portabilis/pre-matricula-digital) — enrolment | 🔴 **AGPL-3.0-or-later**, `2.12/LICENSE` 35,326 B `fe85f94658bf` *(Portuguese)* | 🔴 **network use** |

🔴 **Read the licences before you plan the integration, and read them in Portuguese.** Both AGPL
payloads are rendered as *"LICENÇA PÚBLICA GERAL AFFERO GNU"*, which every English-anchored reader
on this base returned as `UNSTATED` until this pass. 🟢 Two of the three components carry the
**network** trigger, and an AGPL network trigger is reached by *serving* — a hosted AI assistant
wired into the gradebook or enrolment flow is inside it.

**How to wire it.**
1. 🟢 **The AI layer is a separate service with its own repository and licence.** It never imports
   Portabilis code, is never deployed in the same process, and holds no vendored copy.
2. 🟢 **Cross the boundary over the database or an HTTP adapter the secretariat owns**, treating
   i-educar/i-diario as a **system of record you do not control** — the same posture `p455` measured
   for Europe's PRONOTE and WebUntis, where the asset was proprietary. Here it is copyleft; the
   architecture is identical.
3. Curriculum grounding comes from [bncc-dados](https://github.com/bncc-dev/bncc-dados) (🟢 **MIT**,
   1,092 B `e162f8f4b461`) — not from scraping the LMS.
4. 🔴 **Public open data is reference only**: São Paulo's
   [dados-educacao](https://github.com/prefeiturasp/dados-educacao) and Paraguay's
   [mec-opendata](https://github.com/mecpy/mec-opendata) are **UNGRANTED at 14 probed paths**. Read
   them to calibrate; do not vendor them.
5. 🟢 Telemetry into the `P474-1` spine, which is permissive and sits on the AI side of the line.

🔵 **What to tell the client in one sentence:** *the AGPL is not a reason to avoid the estate — it is
a reason to keep the AI service on the other side of an interface, which you want anyway because
the secretariat upgrades i-educar on its own schedule.*

🔵 **Shape:** 6–8 weeks, with the first two spent on the licence boundary and the adapter contract.

---

### 🟢 `P474-3` — The national-curriculum agent, built where the full stack already exists

🔵 **When to reach for it.** A ministry or large private group wants an AI tutor or teacher
assistant that is **demonstrably aligned to the national curriculum** — and wants the alignment
auditable rather than asserted.

🟢 **Brazil is the only country on these shelves where all three layers are already published, by
one organisation:**

| layer | repo | grant | what it gives |
|---|---|---|---|
| Curriculum as data | [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** whole-work, 1,092 B `e162f8f4b461` | 1,721 learning objectives, JSON/SQLite/CSV, provenance per record |
| Callable interface | [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes) | 🔴 **SPLIT_SCOPE**, 1,299 B `86bf5f5e6306` | npm + PyPI packages **and an MCP server** — the curriculum as an agent tool |
| Alignment evidence | [bncc-dev/bncc-benchmark](https://github.com/bncc-dev/bncc-benchmark) | 🔴 **SPLIT_SCOPE**, 911 B `d19733bb7540` | 15,300 responses × 17 models, held-out private set against contamination |

**How to wire it.**
1. 🟢 Mount `bncc-pacotes`' **MCP server** as a tool on the agent. Every curriculum claim the tutor
   makes resolves to an objective **code**, not to model recall — which is the whole auditability
   argument.
2. Ground generation on `bncc-dados`; the agent cites the objective it is teaching to.
3. Run `bncc-benchmark` **as the regression gate in CI**, not as a launch-day score. Its
   private held-out set is what makes a repeated score meaningful.
4. Telemetry into `P474-1`, so curriculum alignment becomes part of the same evidence record as
   human oversight.

🔴 **Two licence boundaries to respect, both read first-hand this pass:**
- 🟡 The two `SPLIT_SCOPE` repositories are **MIT in code and CC BY 4.0 in data**, and the published
  npm tarball and PyPI wheel **carry both in one artifact**. 🟢 So shipping them is fine and
  **attribution is owed** — put the CC BY notice in the deliverable's third-party notices, where a
  scanner reporting only `MIT` will not put it for you.
- 🔴 The **name and visual identity are expressly not licensed** (*"O código é livre; a marca
  não"*). The deliverable must not present itself as bncc.dev or use the mark.

🟢 **The replication offer, which is the actual sale.** Mexico, Colombia and Chile have national
curricula and **no equivalent stack**. The scoped engagement is: curriculum → structured open data
with provenance → an MCP server → a contamination-resistant benchmark. 🔵 Brazil is the working
reference implementation, and
[ResultadosUNAM---data](https://github.com/agn3si/ResultadosUNAM---data) (🟢 MIT) and
[chile-hub](https://github.com/cortega26/chile-hub) (🟢 MIT) show the public-data habit already
exists in both of the next two markets.

🔵 **Shape:** 4 weeks to a grounded agent on Brazil; 10–12 weeks per new country, most of it in
turning a curriculum PDF into provenanced structured data.

## 🆕 `p473` — `2026-10-27` — **three recipes built only from grants read first-hand this pass: a telemetry spine with ZERO copyleft in the deliverable, a LATAM public-education stack that crosses two different copyleft triggers and the boundary that keeps them outside the AI layer, and the evidence gate the whole market is asking for and almost nobody can license.**

🔵 Every repository named below was address-resolved by `git ls-remote --symref` and grant-verified
by payload read from `raw.githubusercontent.com` this pass; digests are in
[`evidence/grant-class.2026-10-27-p473.tsv`](../evidence/grant-class.2026-10-27-p473.tsv).
🔴 No pattern here composes a row whose grant was taken from an index, a README badge or a
comparison table.

---

### 🟢 `P473-1` — The xAPI telemetry spine: an auditable AI tutor with no copyleft in the deliverable

🔵 **When to reach for it.** The client needs AI-assisted learning *and* a record of what the AI did
to each learner — because a regulator (EU AI Act high-risk assessment duties), a statute
(Oklahoma SB 1734's "not the main basis for grading") or a procurement team asks for it. 🔴 The
trap this avoids: wiring the AI into an AGPL LMS and owing its source to the client's learners.

**The parts, all permissive, all grant-verified:**

| role | component | grant (read first-hand) |
|---|---|---|
| Tutoring engine | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0, `main/LICENSE` 11,408 B `cd2f54e1e506` |
| Record store | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0, `main/LICENSE` 11,357 B `c71d239df917` |
| Statement pipeline / validation | [openfun/ralph](https://github.com/openfun/ralph) | **MIT**, `main/LICENSE.md` 1,094 B `08ea77291de9` |
| Conformance oracle (test-time only) | [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) | Apache-2.0, `master/LICENSE` 11,357 B `58d1e17ffe51` |
| LMS seam, no linking | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | MIT, `master/LICENSE` 1,072 B |
| Learner-facing dashboards | [tl-its-umich-edu/my-learning-analytics](https://github.com/tl-its-umich-edu/my-learning-analytics) | Apache-2.0, `master/LICENSE` 11,379 B `b89b380a589b` |

**Wiring.**

1. **Emit, don't embed.** The tutor emits one xAPI statement per pedagogical act — not per API call.
   The verbs that matter to a regulator are `experienced`, `answered`, `was-assisted-by` and
   `progressed`; the ones that matter to nobody are token counts. Put the model's identity, prompt
   revision and a decision-provenance flag in the statement's `context.extensions`, because
   *"a human made the grading decision"* is a claim you must be able to serve six months later.
2. **Validate at the edge, store in SQL.** `ralph` (MIT) does Pydantic-level statement validation and
   forwarding; `lrsql` (Apache-2.0) persists to Postgres. 🟢 The reason to pair them rather than pick
   one: `ralph` rejects malformed statements *before* they reach the store, so the store stays
   queryable by the client's own BI team, which is what makes the audit trail usable rather than
   merely present.
3. **Prove conformance against the reference implementation.** Run the same statement set into
   `ADL_LRS` — authored by the body that wrote the Experience API — in CI only. 🔵 It never ships;
   it is the oracle that stops a bespoke statement shape from being discovered by the client's
   auditor instead of by you.
4. **Cross the LMS boundary over the runtime, never the codebase.** Where the incumbent is Moodle
   (GPL-3.0), Canvas (AGPL-3.0) or Open edX (AGPL-3.0), report completion and scores through
   `scorm-again` (MIT) as a SCORM 1.2/2004 runtime, or over LTI. 🟢 **Nothing links to the LMS and
   nothing modifies it**, so neither copyleft trigger fires.
5. **Hand back the dashboards as yours to restyle.** `my-learning-analytics` is Apache-2.0, so the
   learner-facing views can be rebranded and extended inside a proprietary deliverable.

🟢 **Licence result: every shipped component is MIT or Apache-2.0. The copyleft in the deployment is
all pre-existing and all unmodified.**
🔴 **The one place this breaks:** if the client's standard is **IMS Caliper** rather than xAPI, the
only row this base has found is `OpenLRW` — and it is **ECL-2.0**, whose patent grant is
deliberately narrower than Apache-2.0's (`repos/foundations.md`, `Gap 473-B`). That needs its own
counsel review, not a licence-family assumption.

---

### 🟡 `P473-2` — The LATAM public-education stack: two copyleft triggers in one deployment, and where to stand

🔵 **When to reach for it.** A Brazilian municipality or state secretariat engagement. The incumbent
is already installed: [portabilis/i-educar](https://github.com/portabilis/i-educar) has **552
forks**, which is a municipal install base rather than a star count.

🔴 **The hazard, in one table, because the two components look like one product and are not:**

| component | grant, read first-hand | trigger | what fires it |
|---|---|---|---|
| [portabilis/i-educar](https://github.com/portabilis/i-educar) — the SIS | 🟡 **GPL-2.0-or-later**, `2.12/LICENSE` 18,092 B `8177f9751321` | **distribution** | shipping a modified build. 🟢 Hosting it unmodified owes nothing |
| [portabilis/i-diario](https://github.com/portabilis/i-diario) — the gradebook | 🔴 **AGPL-3.0-or-later**, `1.6/LICENSE` 35,326 B `fe85f94658bf`, **payload in pt-BR** | **network use** | modifying it and letting teachers reach it over a network. 🔴 **An AI grading assistant wired into `i-diario` is a modification** |

**Wiring.**

1. **Put the AI layer outside both.** Talk to `i-diario` over its HTTP API as an external service.
   The AI service is yours; the gradebook stays byte-for-byte upstream. 🟢 This is `P473-1` step 4
   applied to a LATAM incumbent, and it is the whole design.
2. **Take the curriculum from a permissive source, not from the SIS.**
   [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) is **MIT** (`main/LICENSE` 1,092 B
   `e162f8f4b461`) and ships the **BNCC's 1,721 learning objectives** in JSON / SQLite / CSV with
   **per-record provenance** and an MCP surface. 🟢 Probed for a separate data licence at three paths,
   all `404` — the MIT grant is the only grant and it covers the compilation. So alignment-to-national-
   curriculum, the first thing a secretariat asks for, is an MIT dependency and not an integration.
3. **Score Portuguese writing on a permissive corpus.**
   [gpassero/uol-redacoes-xml](https://github.com/gpassero/uol-redacoes-xml) (Apache-2.0,
   `master/LICENSE` 11,357 B `b40930bbcf80`) is an ENEM-style essay bank in XML built for pt-BR NLP
   validation — the substrate for an essay-feedback feature that does not have to be trained on the
   client's own student work.
4. **Where connectivity is the constraint, change the core.** [learningequality/kolibri](https://github.com/learningequality/kolibri)
   is **MIT** (`develop/LICENSE` 1,097 B `3c056b34a476`), offline-first by design, 1,012 forks.
   🟢 For a rural deployment it replaces the LMS question entirely and brings no copyleft with it.
5. **Gate on the Brazilian benchmark before go-live** — `P473-3`.

🔴 **Instrument warning that belongs in the runbook, not a footnote:** `i-diario`'s licence is served
**in Portuguese**, so an automated licence screen keyed on English titles reports the single
riskiest component in this stack as *unlicensed*. 🔵 On any LATAM or Iberian engagement, **read the
LICENSE payload by eye** (`Gap 473-C`).

---

### 🟢 `P473-3` — The evidence gate: the thing five independent bodies are asking for, assembled from the two instruments that permit it

🔵 **When to reach for it.** Always, now. `intel/trends.md` Trend 1 records 1EdTech, the OECD,
HolonIQ, Oklahoma SB 1734 and the EU AI Act converging on *demonstrable evidence* inside one window.
🔴 And `agents/top.md` records that the open evaluation tier is **44.4 % ungranted**, so this is the
pattern where the licence decides the architecture rather than the reverse.

**The parts, with their constraints stated as constraints:**

| role | component | grant | where it may run |
|---|---|---|---|
| Trial apparatus inside the LMS | [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | 🟢 Apache-2.0, `development/LICENSE` 11,323 B `6dc0e068dcf3` | 🟢 **anywhere, including the deliverable** |
| Scored baseline, unconditional | [acheamponge/wassce-benchmark](https://github.com/acheamponge/wassce-benchmark) | 🟢 **MIT**, `main/LICENSE` 1,076 B `df8c7a998c17` | 🟢 **anywhere** |
| Scored baseline, curriculum-aligned | [bncc-dev/bncc-benchmark](https://github.com/bncc-dev/bncc-benchmark) | 🟢 code **MIT** `e1ed7acaf9e2` / items **CC BY 4.0** `9b70e1d9a0c9` | 🟢 anywhere, **with attribution** on the item bank |
| Accuracy reference | [Khan/tutoring-accuracy-dataset](https://github.com/Khan/tutoring-accuracy-dataset) | 🟡 bespoke *Evaluation Dataset License*, 2,690 B `53cf7aa78a89` | 🔴 **internal evaluation only.** No redistribution, **no model training**, no production use, not sublicensable — and the restriction propagates into any merged dataset |
| Breadth probe | [kcelestinomaria/overlooked-bench](https://github.com/kcelestinomaria/overlooked-bench) | 🟡 AGPL-3.0 `0d96a4ff68ad` | 🟡 **CI only**, never inside the deliverable |
| Theory-grounded adaptivity | [vanderbilt-data-science/knowledge-spaces](https://github.com/vanderbilt-data-science/knowledge-spaces) | 🟢 MIT, `main/LICENSE` 1,090 B `ed2ed868dffc` | 🟢 anywhere |

**Wiring.**

1. **Separate the gate from the deliverable physically, not by intention.** Two repositories: the
   product, and an `eval/` repository that is never published. The AGPL and bespoke-licensed
   instruments live only in the second. 🔵 This is what makes the Khan dataset usable at all — its
   §3 explicitly permits evaluating *products intended for commercial use* and commercial use of the
   *insights*, while prohibiting the dataset from travelling. Those are compatible with a private
   eval repo and incompatible with a monorepo.
2. **Pick the baseline by the client's exam, not by star count.** `wassce-benchmark` for West
   Africa, `bncc-benchmark` for Brazil. 🔴 Where the client's curriculum has no open benchmark — which
   is most of the world — build the item set from a permissive curriculum source
   (`bncc-dados` MIT shows the shape) rather than from a NonCommercial one. 🔴 **Do not reach for
   [`cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy)** however good it is:
   CC BY-NC 4.0, `19,347 B` `41003d4a7474`, re-read first-hand this pass. 1,644 knowledge points you
   may not sell.
3. **Make the adaptivity falsifiable.** `knowledge-spaces` (MIT) implements **Knowledge Space
   Theory** — prerequisite structure, adaptive assessment, just-in-time instruction planning — so the
   claim *"it adapts"* becomes a prediction about which items a learner can pass, which is a thing a
   benchmark can check. 🔵 A prompt chain cannot be wrong in this way, which is exactly why it cannot
   be shown to be right.
4. **Prove it on the client's own learners with `terracotta`.** Randomised arms inside the live LMS
   over LTI, consent hidden from the teacher, non-consenting participants filtered from exports,
   identifiers stripped. 🟢 Apache-2.0, so the trial apparatus itself can ship as part of the
   platform — the client keeps the ability to re-run the experiment after the engagement ends, which
   is the deliverable a ministry actually wants.
5. **Report provenance, not scores.** Emit each eval run as xAPI into the `P473-1` spine, so
   *"this model, this prompt revision, this item set, this date, this result"* is one query.

🟢 **Why this is the pattern worth leading with commercially.** Capability is commoditised —
`DeepTutor` is Apache-2.0 at 44k★. **Proof is not**: there are **two** unconditionally usable
education evaluation instruments on earth that this base can find, and they are 4★ and 9★. A studio
that can show a regulator how it measured is selling the scarce half.

🔴 **Honest limit on all three patterns.** None has been executed end-to-end on this harness. They
compose grants that were verified first-hand and interfaces that are documented; they are not
integration-tested, and the `i-diario` API surface in `P473-2` in particular is read from its
repository, not exercised.

## 🆕 `p472` — `2026-10-27` — **🟢 SIX RECIPES, EVERY COMPONENT GRANT-VERIFIED BY PAYLOAD THIS PASS, AND EACH ONE NAMED WITH THE LICENCE THAT LETS IT SHIP. 🔴 `P5` exists because the two best curriculum graphs in open source are NonCommercial and ODbL — the recipe is how to get the same asset licitly. 🔴 And `P7` is costed as original work because the measurement layer three regimes and every analyst now demand HAS NO OPEN-SOURCE IMPLEMENTATION.**

🔵 **Component gate, per `p471` and extended by `Gap 472-A`/`Gap 472-B`:** before a repository enters
a deliverable, read its grant **by payload** from `raw.githubusercontent.com` at the default branch,
trying **lowercase `license.txt` / `license.md` and `COPYING.txt`** as well as the usual paths —
`frappe/lms` grants at `develop/license.txt` and Moodle at `main/COPYING.txt`, and a `LICENSE*`-only
probe publishes NO GRANT on both. 🔴 **Do not use `curl -sI https://github.com/…` as the existence
check**: it returned 403 on 31 of 31 live repositories this pass.

### 🟢 `P1` — Permissive AI tutor, zero copyleft, zero NonCommercial · 8–10 weeks

🔵 **For:** a client that must keep its modifications closed and cannot accept AGPL network
disclosure. Every component below is MIT, Apache-2.0, BSD-3 or ECL-2.0.

| Layer | Component | Licence (path read) | Wiring |
|---|---|---|---|
| Tutoring loop | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 — `main/LICENSE`, 11,408 B | Multi-agent tutoring; the engine |
| Retrieval | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 🟢 MIT — `main/LICENSE`, 1,070 B | Graph-RAG over course material. **Same lab as DeepTutor** — licence-compatible and designed to pair |
| Ingestion | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | 🟢 MIT — `main/LICENSE`, 1,088 B | PDFs, slides, figures → the retrieval graph |
| Delivery | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 MIT — `develop/LICENSE`, 1,097 B | Offline-first learner client |
| SIS of record | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 MIT — `main/LICENSE`, 1,094 B | Enrolment, cohorts, staff |
| LMS reporting seam | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 MIT — `master/LICENSE`, 1,072 B | Completion + score into whatever LMS the client runs |

🟢 **Reference implementation for the commercial shape:**
[3yangyang9/DeepTutor-AILearning](https://github.com/3yangyang9/DeepTutor-AILearning) (Apache-2.0,
`main/LICENSE` **byte-identical to upstream's 11,408 B**) already adds **multi-tenancy and metering**
over DeepTutor — platform → institution → campus → teacher → student, with coursebook assessment,
gap diagnosis and points-based billing — and does the attribution correctly: its `README.md` states
it *"is not an official HKUDS/DeepTutor distribution"* and points at `CITATION.cff` and
`THIRD_PARTY_NOTICES.md`. 🔵 **Copy that compliance pattern verbatim** when Globant ships a
DeepTutor derivative.

### 🟡 `P2` — Licence-boundary integration for a client already on Moodle, Canvas or Open edX · 4–6 weeks

🔵 **For:** the common case. The incumbent LMS is **GPL or AGPL** and the client will not disclose
source. The deliverable is as much the **boundary memo** as the code.

1. **Leave the LMS unmodified.** No fork, no patched core, no plugin that links LMS internals —
   any of those create a derivative work.
2. **Integrate over the standard seams only**: **LTI 1.3** for launch and identity, **LMS web
   services / REST** for data, **SCORM 1.2 / 2004** via [scorm-again](https://github.com/jcputney/scorm-again)
   (MIT) for completion and scores. These are protocol boundaries, not linkage.
3. **Put every AI component in a separate service** under a permissive licence — DeepTutor
   (Apache-2.0) and LightRAG (MIT) from `P1`.
4. **Write the boundary memo**: which repository carries which grant, where the process boundary
   sits, and why no derivative of the GPL/AGPL work is distributed. 🔴 For **Canvas** and
   **Open edX/Tutor** state the **AGPL network-use** clause explicitly, because hosting a modified
   build for the client's users would disclose to those users.

🔵 Incumbent grants, all read this pass: Moodle **GPL-3.0** (`main/COPYING.txt`), Canvas
**AGPL-3.0** (`master/LICENSE`, 34,520 B), Open edX **AGPL-3.0** (`master/LICENSE`, 35,136 B),
Tutor **AGPL-3.0** (`release/LICENSE.txt`, 34,523 B), `frappe/lms` **AGPL-3.0**
(`develop/license.txt`).

### 🟢 `P3` — Auto-graded assessment with AI feedback · 6–8 weeks

🔵 **For:** programming or STEM courses where grading is the cost centre.

| Layer | Component | Licence (path read) | Role |
|---|---|---|---|
| Grader | [autolab/Autolab](https://github.com/autolab/Autolab) | 🟢 Apache-2.0 — `master/LICENSE`, 11,324 B | Autograding + course management; **modifiable** |
| or Grader | [Submitty/Submitty](https://github.com/Submitty/Submitty) | 🟢 BSD-3-Clause — `main/LICENSE.md`, 1,542 B | Submission + autograding + TA grading |
| Feedback | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | Turns a failing test into a diagnosed misconception and a next exercise |
| Misconception branching | [oppia/oppia](https://github.com/oppia/oppia) | 🟢 Apache-2.0 — `develop/LICENSE`, 11,358 B | Explorations with explicit misconception paths |
| Report-back | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 MIT | Scores into the client LMS |

🔴 **Do not modify [INGInious](https://github.com/INGInious/INGInious)** (AGPL-3.0, `main/LICENSE`,
34,764 B) if the grader needs changing — use it unmodified behind its LTI seam, or pick Autolab or
Submitty, which are permissive.

### 🟢 `P4` — High-risk assessment pipeline with a built human-in-the-loop · 10–12 weeks

🔵 **For:** EMEA under the **EU AI Act** (admissions, student evaluation and exam scoring are
**high-risk**), North America under **Oklahoma** and **Maryland** human-oversight statutes, and APAC
under **Vietnam's** high-risk classification of automated assessment. 🟢 **Three regimes
independently require the same thing, so build it once as a component — not as a policy document.**

| Layer | Component | Licence (path read) | Role |
|---|---|---|---|
| Gradebook of record | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** — `master/LICENSE`, 11,120 B | The **only permissive LMS with a gradebook of record** |
| or, EMEA-native | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 — `master/LICENSE`, 10,982 B | QTI assessment, SCORM, certification first-class |
| Advisory AI only | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | 🔴 Emits a **recommendation**, never a grade write |
| Psychometric defence | [inuyasha2012/pypsy](https://github.com/inuyasha2012/pypsy) | 🟢 MIT — `master/LICENSE`, 1,068 B | IRT / CAT / cognitive diagnostic models — the statistical justification an auditor will ask for |

🔵 **The component to build** (no open-source equivalent found): a **sign-off gate** that holds every
AI-proposed outcome in a pending state, requires a named human decision, and writes an immutable
record of *who* decided, *when*, *what the AI proposed*, and *whether the human agreed*. 🟢 That
record is simultaneously the EU AI Act audit artefact, the Oklahoma/Maryland oversight evidence, and
the Vietnam compliance trace. 🔴 **Age-gate it too**: NYC's moratorium bars student-facing AI through
eighth grade, so the pipeline needs a per-cohort switch, not a global one.

### 🟢 `P5` — Curriculum knowledge graph without the NonCommercial licence · 6–8 weeks

🔵 **For:** adaptive learning paths. 🔴 **Why this recipe exists:** the two best curriculum graphs in
open source **cannot be sold** — [cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy)
is **CC BY-NC 4.0** (`main/LICENSE`, 19,347 B; 1,644 knowledge points, 2,403 prerequisite edges,
6,723 items) and `withmarbleapp/os-taxonomy` is **ODbL** (recorded `p384`). Shipping either in a paid
engagement is a licence breach. 🟢 **Build the equivalent from the client's own curriculum instead,
and it is better anyway, because it is aligned to their standard.**

1. **Distil the client's material** — [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill)
   (🟢 Apache-2.0, `main/LICENSE`, 11,358 B) turns videos, PDFs, transcripts and notes into
   **source-backed teacher skills**, retaining the citation to the client's own source.
2. **Ingest the long-form material** — [RAG-Anything](https://github.com/HKUDS/RAG-Anything) (MIT) for
   multimodal documents into [LightRAG](https://github.com/HKUDS/LightRAG) (MIT) as the graph store.
3. **Model prerequisites in the client's own data.** Use the **shape** the NC graphs demonstrate —
   knowledge points, prerequisite edges, items per node, a prerequisite diagnostic — as a design
   reference. 🟢 **A schema is not a licensed work; the dataset is.** Copy the structure, never the
   rows.
4. **Serve adaptive paths** through [oppia/oppia](https://github.com/oppia/oppia) (Apache-2.0)
   explorations, with DeepTutor driving the next-step choice.
5. **Deliverable:** the graph is **the client's asset under their own copyright**, which is a better
   commercial outcome than a dependency on a third party's NC dataset.

### 🟢 `P6` — LATAM strategy-first engagement · 6–8 weeks assessment, then build · 8–10 weeks

🔵 **For:** the region's actual condition, which is **not** a tool gap. UNESCO IESALC/UNU-IAS across
200 institutions in 19 countries: **87 % use AI, 74 % in teaching and learning, 26 % have a
strategy** — adoption driven by individuals, not institutions. 🔴 **Selling a tutor into a 26 %-strategy
institution builds shadow AI faster.** Sequence it:

1. **Assessment first.** Benchmark the institution against the **UNESCO Observatory on AI in
   Education for LAC** (launched 14 April at ECLAC, Santiago) and **ILIA 2025** (3rd edition, 20
   economies). Output: where the institution's actual, individual-driven usage sits versus its stated
   policy.
2. **Governance artefact.** The human-sign-off gate from `P4`, plus a data-boundary statement — the
   instrument to cite differs by country: **Uruguay** (Council of Europe Framework Convention
   signatory), **Peru** (regulatory sandboxes), **Colombia** (CONPES 4144), **Mexico** (bill pending,
   no regulator), **Brazil** (Marco Legal da IA, carried from prior passes).
3. **Build respecting the compute constraint.** ILIA 2025 and Intelligent CIO (23 October 2026) both
   name **computing infrastructure** as the binding obstacle, with inequality widening. So:
   [Kolibri](https://github.com/learningequality/kolibri) (🟢 MIT) as the **offline-first** delivery
   core — not a cloud tutor — with [ai-shifu](https://github.com/ai-shifu/ai-shifu) (🟢 Apache-2.0)
   for the Spanish/Portuguese conversational loop.
4. **Expect [Chamilo](https://github.com/chamilo/chamilo-lms)** (🟡 GPL-3.0, `master/LICENSE`,
   35,147 B) as the incumbent in public education, and apply `P2`'s boundary discipline to it.
5. 🔴 **Do not propose a LATAM-origin open-source base.** There is none live: the only one found this
   window, [menthorlabs/menthor](https://github.com/menthorlabs/menthor) (Brazil, Apache-2.0, 582★),
   is **archived**. Say so in the proposal — it is an argument for the engagement, not against it.

### 🔴 `P7` — The learning-gain measurement harness: costed as original work

🔵 **Why it is a recipe and not a component list.** Searched at every star floor this window
(`education agent`, `topic:edtech`, `topic:education-ai`, `topic:lms`, `grading topic:education`,
`topic:curriculum`): **no open-source education-AI evaluation or observability harness exists.**
Meanwhile the **OECD 2026 Digital Education Outlook** argues for purpose-built educational AI, and
multiple sources report systems now **demanding evidence** of improvement in learning quality,
persistence, well-being or job-relevant skills.

🟢 **So the gap is the opportunity — the one layer of this stack with no incumbent.** What can be
assembled, and what must be written:

| Piece | Status | Component |
|---|---|---|
| Item-level psychometrics | 🟢 **exists** | [pypsy](https://github.com/inuyasha2012/pypsy) — MIT, `master/LICENSE`, 1,068 B: IRT, CAT, cognitive diagnostic models, factor analysis, SEM |
| Deterministic outcome signal | 🟢 **exists** | [Autolab](https://github.com/autolab/Autolab) (Apache-2.0) / [Submitty](https://github.com/Submitty/Submitty) (BSD-3) — objective pass/fail per attempt |
| Misconception taxonomy | 🟢 **exists** | [oppia/oppia](https://github.com/oppia/oppia) (Apache-2.0) explorations already encode misconception branches |
| Transport of results | 🟢 **exists** | [scorm-again](https://github.com/jcputney/scorm-again) (MIT) — SCORM 1.2 / 2004 |
| **Agent-level evaluation** | 🔴 **DOES NOT EXIST** | Trace capture per tutoring turn, counterfactual cohorting, learning-gain attribution to agent behaviour. **Original work.** |

🔵 **Cost it honestly in the proposal.** Globant cannot buy or fork this layer, so any engagement
promising learning-gain evidence must carry it as new build. 🟢 Conversely, it is the single piece
of the education-AI stack where there is nothing to be second to.

## 🆕 `p471` — **🟢 THE PATTERN THIS PASS CONTRIBUTES IS A GATE EVERY OTHER RECIPE ON THIS FILE NOW PASSES THROUGH: before a repo enters a deliverable, enumerate its licence paths at every depth — because 14.4 % of these shelves' repositories grant below the root, 66.7 % above 2 000 paths, and one of them is PROPRIETARY inside an otherwise-open tree. 🟢 And the human-review checkpoint that three regimes independently require is specified here as a component, not as advice.**

🔵 Gate not attested (`Gap 446-A`); checks re-implemented in-session and green. Every grant named
below was read first-hand at `HEAD` this pass or is carried with its `p`-number.

### 🟢 Pattern `P471-1` — the pre-vendoring licence gate (run this before every other pattern)

🔵 **Problem.** Every recipe on this file names repositories to compose. A root-path licence read —
which is what this base used for 470 passes, and what a client's own counsel will do — establishes
the grant on the **root tree only**. Measured this pass: **33 of 229** education repositories
(14.4 %) carry a grant below the root; above 2 000 paths it is **66.7 %**.

**Wiring.** Two commands per repository, no API access needed (the GitHub API refuses these repos):

```bash
# 1. the screen — decides whether step 2 is needed at all
git clone --depth 1 --filter=blob:none https://github.com/OWNER/REPO d
git -C d ls-files | wc -l

# 2. the enumeration — every licence path at any depth
git -C d ls-files | grep -Ei '(^|/)(LICEN[CS]E|COPYING|COPYRIGHT|NOTICE|EULA|THIRD[-_]PARTY)([._-][A-Za-z0-9.+-]{1,20})?$'

# 3. for each path found, read the payload and the COPYRIGHT LINE
curl -sS "https://raw.githubusercontent.com/OWNER/REPO/$(git -C d rev-parse HEAD)/PATH" -o p.txt
wc -c < p.txt; sha256sum p.txt; grep -iE 'copyright' p.txt | head -2
```

🔴 **Three decision rules, each earned from a real row this pass:**

| what step 2 returns | classify as | what to do |
|---|---|---|
| grant below root, **copyright = the project** | **R — recovered** | 🟢 The repo *is* granted. `formalms/formalms` → **GPL-2.0** at `html/license.txt`; both these shelves had it refused |
| grant below root, **copyright = a third party** | **V — vendored** | 🔴 The repo grants **nothing**. Vendor from the **upstream** instead — the licence digest identifies it. `Chloris-Blaxk/inno-agent-hub`'s 37 subtree grants all name `© ChantillyAn` or `© Artem` |
| **"All rights reserved"**, no permission sentence | **X — reservation** | 🔴 **Exclude that subtree from the deliverable.** `particify/arsnova-server` → `formatting/LICENSE`, 133 B, names Particify |

🟡 **The one limit, stated so the gate is not over-trusted:** a **copyleft** payload carries the
FSF's copyright, not the project's, so rule R's copyright test is unavailable for GPL/AGPL texts.
For those, read the project's own `README`/`COPYRIGHT` notice to establish the grant's **scope**
(`Gap 471-C`).

🔴 **Do not substitute a name-based heuristic for step 1.** Screening on repository names containing
`plugin`/`integration`/`moodle`/`canvas`/`mcp` was tested this pass and is **anti-predictive**:
8.6 % against the control's 26.0 %. Use the path count.

### 🟢 Pattern `P471-2` — rubric-graded assignment feedback with a reviewable human checkpoint

🔵 **Problem.** The clearest LATAM opportunity on `intel/market.md` (teacher AI use 16–20 points
above the OECD average against 26 % institutional strategy) and the one architecture that clears
three regulatory regimes at once.

**Wiring:**

1. **Grading core** — [`ChantillyAn/homework-grader`](https://github.com/ChantillyAn/homework-grader)
   (**MIT**, 1 068 B · `8755221656d4`, 7★, `master` `5e9aab47822f`). Rubric-driven scoring with
   chain-of-thought, explicit bias mitigation and a PDCA quality cycle. 🟢 26 paths, single root
   grant — `P471-1` clears it in one step.
2. **Evaluation harness** — [`TREMA-UNH/rubric-grading-workbench`](https://github.com/TREMA-UNH/rubric-grading-workbench)
   (**MIT**, 1 068 B · `3f68bfcd4ec5`, 15★, `main` `13aaed5161ec`). University of New Hampshire
   autograding workbench: use it to measure the grader rather than asserting it works. 🟢 The only
   academic-provenance rubric component on these shelves.
3. **Human checkpoint — the regulated part.** Every score is a **proposal** until an educator
   accepts, edits or rejects it. Persist reviewer identity, timestamp, the pre-review score, the
   post-review score and the override reason.
4. **LMS delivery** — over Canvas or Moodle **interfaces**, never by forking. Moodle is GPL-3.0
   (`COPYING.txt` 35 147 B · `8ceb4b9ee5ad`); a Moodle plugin you ship is GPL-3.0 by force.

🔴 **Why step 3 is the product and not a feature.** Vietnam's Decision 33/2026/QD-TTg classes
education AI high-risk **only where the output is the sole basis for a decision without meaningful
human review** — so step 3 keeps the system *out* of the high-risk tier there. The EU AI Act's
Annex III duties require staff able to monitor, intervene, override and shut down — step 3 *is* that
duty. Oklahoma and Maryland bar AI from high-stakes student decisions — step 3 is the evidence.
🟢 **One component, three regimes.** Build it once and reuse it across engagements.

🟡 **Both grading repos are single-maintainer and under 20★. Fork and own them**; do not take a
runtime dependency on either.

### 🟢 Pattern `P471-3` — curriculum-graph tutoring with the grant boundary drawn correctly

🔵 **Problem.** `p470` found `mgarlabx/edukors_graph` is MIT at the root and GPL-3.0-or-later in its
Moodle plugin. This pass found a **third** layer, and it is the one that makes the pattern shippable.

**The three layers, all read at `6bc743c6a5fe`:**

| subtree | grant | ship it? |
|---|---|---|
| root — JSON Schema, standalone player, original resources | **MIT** · 1 087 B · `625342dc4d3d` | 🟢 **Yes**, vendor freely |
| `plugin/edukorsplayer/` — the Moodle integration | **GPL-3.0-or-later** · 35 151 B · `e79e9c8a0c85` | 🔴 Ships as GPL-3.0-or-later. Forced: Moodle is GPL |
| 🟢 `plugin/edukorsplayer/vendor/edukors/` | **MIT** · 1 087 B · `625342dc4d3d` — byte-identical to root | 🟢 **Yes** — extractable under MIT despite its position inside the GPL subtree |

**Wiring:**

1. **Course structure** — `edukors_graph`'s MIT JSON Schema: a course as nodes and prerequisite
   edges in one file. Vendor the **root** and the **vendored `edukors` component**; leave
   `plugin/edukorsplayer/` out of any proprietary deliverable.
2. **Concept graph** — [`AI-First-Community/Bodhi`](https://github.com/AI-First-Community/Bodhi)
   (MIT, 1 095 B · `967480f4f094`, `p470`) for typed concept connections.
3. **Retention** — [`Garuda8887/recall`](https://github.com/Garuda8887/recall) (MIT, 1 099 B ·
   `0bfc98ccf58b`, `p470`): SM-2 spaced repetition over the graph.
4. **Textbook ingestion + Socratic questioning** — [`MXC-CKK/huoshu`](https://github.com/MXC-CKK/huoshu)
   (MIT, 1 059 B · `a005f12beb1c`, `p470`), which already wires RAG.
5. 🔴 **Do not reach for `withmarbleapp/os-taxonomy`** for the graph itself — 1 590 topics and 3 221
   prerequisite edges, and **ODbL-1.0 + CC BY-SA 4.0** at `LICENSE` 25 289 B. A **data** licence with
   share-alike: usable as a reference corpus, not vendorable into a client deliverable.

### 🟢 Pattern `P471-4` — audience response and formative assessment, with a module excluded by name

🔵 **Problem.** `verticals/solutions.md` carried ARSnova as *"NO GRANT — refused"* for several
passes. It is granted. It is also partly proprietary, and the two facts live in the same repository.

**Wiring:**

1. **Backend** — [`particify/arsnova-server`](https://github.com/particify/arsnova-server) (67★,
   Kotlin, containerised, created 2013), **`core/` under GPL-3.0** · 35 147 B · `8ceb4b9ee5ad`.
   Integrate **over its API** from a separately-licensed product; do not fork into a deliverable.
2. 🔴 **Exclude `formatting/`.** 133 B, *"Copyright (c) 2020-present Particify … All rights
   reserved."* No permission sentence of any kind. This is the module a "repo has a LICENSE" audit
   waves through.
3. **Feed results into `P471-2`'s rubric layer** for formative feedback, keeping the human checkpoint.
4. **Offline/low-connectivity delivery** —
   [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (9 subtree licence
   paths, run `P471-1` before vendoring) where the estate is intermittently connected.

🟡 **Licence-compatibility trap inside this pattern.** If the same deliverable also composes
**forma.lms** (**GPL-2.0**, `html/license.txt` 18 346 B · `4e63feff285d`), note that GPL-2.0 and
GPL-3.0-only code **cannot be merged into one binary**. Keep ARSnova and forma.lms as separate
services behind interfaces.

### 🟢 Pattern `P471-5` — institutional AI-governance product (build, because there is nothing to compose)

🔵 **Problem.** The strongest demand signal on these shelves with the weakest supply. LATAM: 87 % of
institutions using AI, **26 %** with a formal strategy, teachers 16–20 points above the OECD average.
Supply: `education governance license:mit` → **61 repositories, maximum 16★**, five of the top eight
off-class.

🔴 **This is a build-from-scratch engagement.** Stated plainly because every other pattern on this
file starts from an existing repo and this one cannot.

**Wiring — the one granted substrate, plus own IP:**

1. **Knowledge substrate** — [`panaversity/ksor`](https://github.com/panaversity/ksor)
   (**Apache-2.0**, 11 342 B · `2f538e0b9e84`, 232★, `p470`): one authoritative knowledge record for
   humans and agents, naming education institutions in its own opening. 🟢 The only granted
   governance-layer component on these shelves — re-read first-hand this pass, 11 342 B confirmed.
2. **Own IP — the four artefacts the survey gap implies:** an institutional AI-use policy register;
   a per-course disclosure record (what AI was used, by whom, for what); assessment-integrity rules
   bound to the curriculum; and the **audit trail from `P471-2` step 3**, which is the same component
   again.
3. **Regulatory mapping** — drive the ruleset from `intel/market.md`'s dated obligations: EMEA
   2 Dec 2027 / 2 Aug 2028, Vietnam 1 Mar 2027, Brazil PL 2.338/2023 and Chile pre-statute,
   Colombia CONPES 4144.
4. 🔴 **EMEA deployments: audit every generative capability before 2 December 2026.** The
   non-consensual intimate imagery and CSAM prohibition applies from that date, schools are a
   primary venue for that harm, and a **prohibition has no conformity route** — the capability is
   prevented or it is unlawful.

🟢 **Why this is the best own-IP opportunity on these shelves:** a 16★ supply ceiling means there is
no incumbent open-source project for a client to adopt instead, and the regulatory deadlines give
the buyer a date.

## 🆕 `p470` — **three recipes, every component's grant read first-hand at `HEAD` this pass, and each one specified so the licence boundary falls where the deliverable splits rather than inside it**

🔵 Every component named below was read first-hand on **2026-10-27**: default ref by
`git ls-remote --symref`, licence payload from `raw.githubusercontent.com` written to a file and the
file measured. 🔴 Two recipes exist because of a *licence partition* rather than a technology
choice, which is new on this file: `Gap 470-A` means a recipe must name **which subtree** of a
component it ships, not only which component.

---

### 🟢 `Pattern BQ` — Governed multi-agent education estate (the "agents cannot contradict the catalogue" build)

**The problem it solves.** `p468` measured 87 % of 200 institutions across 19 countries using AI
against 26 % with a formal AI strategy. The failure that gap produces in practice is concrete: the
tutoring agent, the teaching-assistant agent and the assessment agent each answer from different
curricula, and the institution cannot say which one is authoritative.

| step | component | grant, read first-hand | role |
|---|---|---|---|
| 1 | [`panaversity/ksor`](https://github.com/panaversity/ksor) | **Apache-2.0** · 11 342 B · `2f538e0b9e84` · 232★ | The **system of record**. Load approved curricula, assessment rules, academic policy and standards as the one governed knowledge record. Every agent below reads from it and none holds its own copy |
| 2 | [`mgarlabx/edukors_graph`](https://github.com/mgarlabx/edukors_graph) — **root only** | **MIT** · 1 087 B · `625342dc4d3d` | The **learning-graph schema**: each course as nodes and edges, one JSON file, authored against the KSoR record. 🔴 Ship the schema and the standalone player; **do not ship `plugin/edukorsplayer/`** or the deliverable becomes GPL-3.0-or-later |
| 3 | [`mizcausevic-dev/curriculum-knowledge-graph`](https://github.com/mizcausevic-dev/curriculum-knowledge-graph) | **MIT** · 1 069 B · `a5ed17e0b90a` | Prerequisite and skill-dependency analysis over the graph; **pathway bottleneck** reporting for the registrar. Treat as a reference implementation to fork, not a dependency |
| 4 | [`NouhKhouyi/aula`](https://github.com/NouhKhouyi/aula) | **MIT** · 1 068 B · `b208dbc2fdee` | The learner-facing agent: probes what the student knows, plans the shortest route, **checks each step lands** before advancing. Local-first, bring-your-own-model |
| 5 | [`Garuda8887/recall`](https://github.com/Garuda8887/recall) | **MIT** · 1 099 B · `0bfc98ccf58b` | SM-2 scheduling and forgetting curves, so mastery from step 4 is **retained** rather than re-taught |

**Wiring.** KSoR is the only writeable source of truth; the graph schema is generated *from* it, so a
curriculum change propagates instead of being re-entered. `aula` reads the graph and writes mastery
events; `recall` consumes mastery events and schedules review. The registrar's bottleneck report
reads the graph directly — no agent in the loop, because a registrar's decision should not depend on
a model.

🟢 **Licence outcome: Apache-2.0 + MIT throughout, no copyleft anywhere**, so the whole stack vendors
into a client deliverable with no boundary argument. 🔴 **Conditional on step 2's exclusion** — this
is the first recipe on this file whose permissive status depends on a *subdirectory* being left out.

🔴 **What you are buying and what you are building.** Only `ksor` (232★) is at a scale where
upstream maintenance can be assumed. Steps 2–5 are 17★, 1★, 2★ and 5★, single-maintainer. **Fork and
own all four and budget the maintenance**; do not present them to a client as vendor components.

---

### 🟢 `Pattern BR` — Curriculum-aligned tutor without the NonCommercial corpus

**The problem it solves.** `p467` found the obvious build reaches for a **4 000★ `CC-BY-NC-4.0`**
knowledge graph — unusable in any paid engagement — and specified a replacement it could not source.
This pass sourced it. 🔴 And `Gap 470-B` adds the second trap: a curriculum-*aligned* agent often
grants its code and withholds its curriculum corpus, so the corpus must be chosen as deliberately as
the code.

| step | component | grant, read first-hand | role |
|---|---|---|---|
| 1 | [`MXC-CKK/huoshu`](https://github.com/MXC-CKK/huoshu) | **MIT** · 1 059 B · `a005f12beb1c` · 3★ | Textbook → navigable **knowledge graph**, with Socratic questioning, RAG retrieval and spaced review already wired. Python, 401 tests, on PyPI as `learning-agent` |
| 2 | [`OscarBarreraGithub/syllabusgraph`](https://github.com/OscarBarreraGithub/syllabusgraph) | **MIT** · 1 083 B · `3cc3fae03d97` · 1★ | Builds concepts and relationships **with source evidence attached**, plus an independent review step. This is the component that lets the tutor show what an answer rested on |
| 3 | **the client's own corpus** | 🔴 whatever the client holds | The deliberate choice. The client's licensed textbooks, its own course materials, or openly-licensed material whose terms you have read — **never** a ministry corpus pulled in behind an MIT code grant |
| 4 | [`shihabshahrier/manim-coding-skill`](https://github.com/shihabshahrier/manim-coding-skill) | **MIT** · 1 065 B · `5ce7ed6c2a3e` · 5★ | ManimGL STEM animation as an agent skill — the explainer-video surface, generated on demand from a graph node. Default ref `master` |
| 5 | [`Tissue-for-charlie/exam-kit`](https://github.com/Tissue-for-charlie/exam-kit) | **MIT** · 1 075 B · `3cd67a7398b6` · 3★ | Courseware → **printable, offline** revision outline, self-test bank and knowledge graph. The artefact for estates with poor connectivity or a no-devices-in-exams rule |

**Wiring.** Step 2 builds the concept graph from step 3's corpus with evidence links; step 1 serves it
as a navigable tutor with retrieval bounded to that corpus; step 4 renders a node on demand; step 5
exports an offline revision pack from the same graph. Retrieval is bounded to the client's corpus at
step 1's RAG layer — which is what makes step 3's licence the only content licence in the stack.

🟢 **Licence outcome: MIT throughout the code, and the corpus licence is a single explicit decision
at step 3** instead of an inherited surprise.

🔴 **The trade, stated.** The replacement set's stars are 3, 1, 5, 3 against the NonCommercial
graph's 4 000. You are swapping curation you may not sell for a schema you may, and the population
work is yours. For `taigi-teaching-agent`'s shape — ministry dictionary, official audio, a
third-party TTS — the code is MIT and **none of the valuable data is granted**; read it as a
reference architecture for curriculum alignment, not as a corpus source.

---

### 🟢 `Pattern BS` — EMEA assessment build inside the two-date window

**The problem it solves.** `Regulation (EU) 2026/1744` (OJ L, 24 July 2026; in force 27 July 2026)
moves education's Annex III obligations to **2 December 2027** — sixteen months of runway — while a
**new prohibition applies from 2 December 2026**, five weeks out. A build scoped on the headline
alone gets the first right and the second wrong.

| step | component | grant, read first-hand | role |
|---|---|---|---|
| 1 | [`panaversity/ksor`](https://github.com/panaversity/ksor) | **Apache-2.0** · 11 342 B · `2f538e0b9e84` | The assessment **rubric and rule set** as governed record — versioned, attributable, and the same for every marker |
| 2 | [`laurauguc/grading_assistant`](https://github.com/laurauguc/grading_assistant) (GradeMate) | **MIT** · 1 072 B · `3b21045edbad` · `main` `03a7c3d3b946` | Rubric-criterion marking of written work, teacher-uploadable rubrics. React + Django. 🟢 Re-read first-hand this pass — **byte- and digest-identical** to `p469`'s record |
| 3 | [`vijju9019/GradeAI`](https://github.com/vijju9019/GradeAI) | **MIT** · 1 077 B · `6a1c56b153f8` · `main` `56b8819e0c90` | The **human-review cockpit**: split-screen rubric comparison and score override — the component that keeps a person in the decision. 🟢 Re-read first-hand this pass, **byte- and digest-identical** to `p469` |
| 4 | [`OscarBarreraGithub/syllabusgraph`](https://github.com/OscarBarreraGithub/syllabusgraph) | **MIT** · 1 083 B · `3cc3fae03d97` | Source-evidence links, so each mark cites the rubric criterion and the material it was judged against |
| 5 | 🔴 **a hard exclusion, not a component** | — | **No generative image or video capability anywhere in the estate's learner-facing surface.** From 2 December 2026 the non-consensual intimate imagery / CSAM prohibition applies; it is a prohibition, so there is no risk tier to argue and no conformity route to buy |

**Wiring.** Step 1 holds the rubric; step 2 proposes a criterion-level mark; step 3 requires a human
to confirm or override **before any mark is released** — the model never writes a final grade; step 4
attaches the evidence trail. The deterministic-and-reviewable spine this base has specified since
`p466` is unchanged; what `p470` adds is the date it must be ready by and the capability it must not
contain.

🟢 **Why the sequence matters commercially.** The sixteen-month Annex III deferral means the
assessment product can be *built properly* rather than rushed to an August 2026 date that no longer
exists — and it must be, because the deferral does not change what conformity will require, only
when. 🔴 The December 2026 prohibition is the opposite: not a thing to prepare for, a thing to
**exclude by architecture now**.

🟢 **Licence outcome: Apache-2.0 + MIT, no copyleft**, deliverable as a managed service with no
disclosure duty. 🔴 Steps 2–4 are 4★, 0★ and 1★ — fork-and-own, as `Gap 464-A`'s closure established.

## 🆕 `p469` — **four recipes, every component read first-hand at `HEAD` this pass, every licence boundary drawn where it actually falls**

🔵 Each pattern names the repositories, their grants as read on **2026-10-27**, the wiring, and the
licence boundary that makes it shippable. Where a component is copyleft, the boundary is stated as
a process or protocol edge, not as a hope.

### `P469-1` 🟢 Permissive LMS + copyleft SIS + closed AI layer — the shape that exists because no single product does

🔴 **Why this pattern exists:** searched again this pass, **no permissively-granted product covers
both LMS and SIS**. The only SIS-class systems that resolve are GPL-2.0. So the integration *is*
the architecture.

| layer | component | grant (first-hand) | why this one |
|---|---|---|---|
| LMS core | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** · 10 982 B · `6dbc5b605ed0` | the only permissive full LMS; QTI, SCORM, assessment, curriculum management already present |
| SIS | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) (or [`portabilis/i-educar`](https://github.com/portabilis/i-educar) in Brazil) | GPL-2.0 · 15 214 B · `d954e14e5c75` (18 092 B · `8177f9751321`) | enrolment, scheduling, grades, attendance. 🔵 RosarioSIS' default ref is **`mobile`** — pin it explicitly in CI or a clone lands off-trunk |
| AI service | your code + [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | **MIT** · 1 069 B · `297c4cba7b33` | brings the lab/exam DSL, sandboxed evaluation and a **human-review stop line**; exposes **MCP** tools, so the LMS never imports it |
| inference | Ollama or vLLM, local | permissive | EMEA data-residency and LATAM cost both land here |

**Wiring.** `OpenOLAT` ⇄ AI service over **HTTP/MCP only**. SIS ⇄ AI service over **a read-only
replica or an export job**, never a shared process. Every AI-touched decision writes
`{decision, inputs_hash, model, human_actor, timestamp}` to an append-only log in the AI service.
**Licence boundary:** the Apache-2.0 LMS may be forked and shipped closed; the GPL-2.0 SIS is never
linked, only queried across a process edge, so its copyleft does not reach your code.
**Effort:** 8–10 weeks for the integration and the audit log; the AI layer itself is the fast part.

### `P469-2` 🟢 Human-in-the-loop rubric feedback — the LATAM opportunity, now with granted parts

🔵 `p464` recorded this as the clearest LATAM opportunity with **no granted supply**. There are now
four MIT rows. 🔴 **Fork them; do not depend on them** — 0–4★, single maintainers, one last pushed
in 2023.

| role | component | grant | what to take |
|---|---|---|---|
| rubric + override UI | [`vijju9019/GradeAI`](https://github.com/vijju9019/GradeAI) | **MIT** · `6a1c56b153f8` | the **teacher review cockpit**: split-screen criterion comparison and score override. Take the interaction design and the rubric data model |
| rubric authoring | [`laurauguc/grading_assistant`](https://github.com/laurauguc/grading_assistant) | **MIT** · `3b21045edbad` | curated-vs-uploaded rubric handling; it has a live hosted demo to read behaviour from |
| batch + report | [`KamoliddinS/AI-Assignment-Grader`](https://github.com/KamoliddinS/AI-Assignment-Grader) | **MIT** · `988f496a7b26` | spreadsheet-in, PDF-feedback-out. 27 KB, archived in practice — read it, don't run it |
| curriculum grounding | [`ThallesYVasconcelos/Agente-Educacional`](https://github.com/ThallesYVasconcelos/Agente-Educacional) | **MIT** · `5eaa67118ee6` | **BNCC/PCN/PNLD retrieval with page citations** and EF-code mapping — this is what makes the feedback defensible to a Brazilian school |
| orchestration | LangGraph + Ollama | permissive | as `Agente-Educacional` already wires it; keeps inference local and cheap |

**Wiring.** Submission → rubric criteria retrieved → curriculum grounding retrieved (BNCC/PCN
chunks with page refs) → per-criterion draft score **with citation** → **teacher cockpit: every
score is a proposal until a human commits it** → committed score to the LMS gradebook via LTI
→ append-only decision log.
🟢 **This clears `T469-4` by construction:** no score reaches a student without a recorded human
actor, which is what Oklahoma, Maryland, the EU deployer duty and Vietnam's sole-basis test all
ask for.
**Effort:** 6–8 weeks to a governed pilot in one subject and one grade band.

### `P469-3` 🟢 EMEA AI-literacy and Annex-III-ready assessment — the duty that is already live

🔵 Two deliverables, two clocks. The **AI literacy duty has applied since 2 February 2025** with no
grace period — sellable now. The **high-risk assessment obligations** are reported at **2 December
2027** (`Gap 469-E`, unconfirmed at source) — build inside that window.

| deliverable | component | grant | note |
|---|---|---|---|
| literacy app | [`insolitos/IA_para_aprender`](https://github.com/insolitos/IA_para_aprender) | **MIT** · `a152c15af5d9` | built for Portuguese **school libraries**, 2.º/3.º ciclo and secondary. A working reference for the literacy duty, in an EU member state, under MIT |
| assessment core | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** · `6dbc5b605ed0` | QTI and assessment already built; Apache-2.0 means the conformity work stays yours |
| curriculum graph | [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | 🔴 **ODbL-1.0** · 25 289 B · `77d2692c3d64` | 1 590 micro-topics, 3 221 prerequisite edges. 🔴 **Share-alike on derived databases** — a curriculum graph derived from it must be published under ODbL. Use it to *validate* a graph you built, or accept the obligation knowingly |
| sovereign inference | Ollama / vLLM + local vector store | permissive | districts under data-residency rules are already doing this |

**Wiring.** Literacy module stands alone (fastest revenue). Assessment path:
`OpenOLAT` QTI item bank → AI item generation and distractor analysis → **human item review**
→ conformity artifacts generated as a by-product of the pipeline (risk documentation, logging,
human-oversight record) rather than written afterwards.
🔴 **The ODbL boundary is the trap in this pattern.** Keep `os-taxonomy` out of the delivered
database, or price the publication obligation into the contract. It passes every "has a LICENSE"
screen and is not a software grant.
**Effort:** 4 weeks for the literacy module; 10–12 weeks for the assessment core with conformity
artifacts.

### `P469-4` 🟢 APAC multi-jurisdiction classroom — one stack, a policy layer per country

🔵 Korea in force **22 January 2026**; Vietnam compliance **1 March 2027** with a six-month grace
for systems live before **15 August 2026**; Japan and Singapore voluntary; China registration;
Australia undecided. One configuration cannot serve them, so the **policy layer is the product**.

| layer | component | grant | note |
|---|---|---|---|
| classroom experience | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | **MIT** · 1 065 B · `ba2525637432` | multi-agent interactive classroom, **v1.2.0 2026-10-16**, 41 563★, 6 433 forks — permissive and already being built on |
| tutoring depth | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 11 408 B · `cd2f54e1e506` | 43 930★; lifelong personalised tutoring with RAG |
| policy layer | your LangGraph/equivalent graph, per-jurisdiction nodes | your licence | the deliverable |
| offline / low-bandwidth tier | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** · `3c056b34a476` | for SEA and rural deployments |

**Wiring.** One model stack and one content pipeline. At every **decision point** (assessment,
progression, behavioural flag) the graph routes through a jurisdiction node that sets: whether a
human must commit the decision, what is logged, what is disclosed to the learner, and whether the
system registers with a regulator.
🟢 **Vietnam's sole-basis test is the default setting:** make human commitment mandatory
everywhere, and the strict tier is avoided by construction in every jurisdiction at once; relax it
only where a client's own counsel says so.
🔴 **Named gap:** this pattern's education-native components are **China and Hong Kong only**. One
dedicated leg returned **no** India- or Japan-originated open-source education agent. For an India,
Japan, Korea or SEA engagement, the components are reusable but **nothing here is local**, and
localisation is in scope from day one, not a phase two.
**Effort:** 12–14 weeks for three jurisdictions; each additional jurisdiction is a policy node, not
a fork.

## 🆕 `p468` — **🟢 Three recipes, every component's grant read FIRST-HAND this pass, each stated with the delivery model it can legally be sold under. 🔴 And one recipe exists because of a regulation rather than a technology: automated assessment is named high-risk in three regions under four instruments, so the assessment recipe below is built to keep a human in the decision — not as a courtesy, as the thing that makes it sellable.**

🔵 **Rule for this file, unchanged and enforced:** no component is named below unless its grant
was read from its payload **this pass**, and no recipe mixes a `grant_class` its delivery model
forbids.

### 🟢 `Pattern BM` — Institutional AI-use inventory for a LATAM university (6–8 wk)

🔵 **Why this and not a tutor.** UNESCO IESALC / UNU-IAS: 87 % of 200 LAC institutions use AI
somewhere, 26 % have a strategy. The buyer's first problem is that **nobody knows where AI is
already running**, because adoption came from individual academics. A tutor sold into that
situation adds to the problem it was meant to address.

| component | grant read this pass | role |
|---|---|---|
| [`av-leschinskiy/moodle-mcp`](https://github.com/av-leschinskiy/moodle-mcp) | MIT · 1 078 B · `67b516c28e67` @ `69c36847e7ad` | 🟢 `PERMISSIVE` — read courses, activities and graded items out of the system of record |
| [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) | MIT · 1 078 B · `d0a329112827` @ `d8849a82e9ea` | 🟢 `PERMISSIVE` — **Spanish-language** Moodle teacher agent; its rubric and forum paths are the reference implementation for what faculty are already automating |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | MIT · 1 072 B · `383b85b370e8` @ `86ab328f0e5b` | 🟢 `PERMISSIVE` — SCORM runtime; surfaces imported third-party courseware the LMS tables do not describe |
| [`fabianastudillo/cafe-con-prompts`](https://github.com/fabianastudillo/cafe-con-prompts) | 🟡 `CC Atribución` · 751 B · `c7a4fd88d164` @ `7ac77c6574a0` | 🟡 `CONTENT_NOT_SOFTWARE` — **cited, not vendored.** A catalogue of what Spanish-speaking faculty actually prompt for; use it to seed the inventory's taxonomy, with attribution |

**Wiring.** `moodle-mcp` enumerates courses → for each course, `scorm-again`'s runtime
identifies imported packages the LMS metadata hides → `miyagi`'s tool surface defines the
"automatable faculty action" taxonomy (grade to rubric, answer forum, build quiz) → classify
each observed activity against that taxonomy → the deliverable is an **inventory plus a policy
baseline keyed to it**. 🟢 **Delivery model: anything.** Every software component is
`PERMISSIVE`; the one content component is cited.
🔴 **Do not vendor `cafe-con-prompts`** into a deliverable's source tree — attribution travels
with content, and this grant is published in Spanish.

### 🔴 `Pattern BN` — Human-in-the-loop assessment assistant, built for the obligation (10–12 wk)

🔴 **The constraint comes first.** Automated assessment is named by the EU AI Act (Annex III),
Vietnam's AI Law, Oklahoma and Maryland statute, and NYC DoE guidance. Three of the four bar the
system from *deciding*. 🟢 So the recipe's architecture is **assist-and-evidence**, and that is
also what makes it sellable in all four jurisdictions without a per-region rebuild.

| component | grant read this pass | role |
|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · 11 408 B · `cd2f54e1e506` @ `a31d82624c27` | 🟢 `PERMISSIVE` — the reasoning and memory spine |
| [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) | MIT · 1 078 B · `d0a329112827` @ `d8849a82e9ea` | 🟢 `PERMISSIVE` — rubric-application path against a real Moodle course |
| [`av-leschinskiy/moodle-mcp`](https://github.com/av-leschinskiy/moodle-mcp) | MIT · 1 078 B · `67b516c28e67` @ `69c36847e7ad` | 🟢 `PERMISSIVE` — writes the *proposed* mark and its evidence, never the final mark |
| [`DilawarShafiq/nietzschian-debugger`](https://github.com/DilawarShafiq/nietzschian-debugger) | MIT · 1 071 B · `a7055a6d5672` @ `94e452d3fc83` | 🟢 `PERMISSIVE` — borrow its **withholding** interaction pattern for the student-facing half |

**Wiring.** Submission arrives → `DeepTutor` produces a rubric-dimension analysis with citations
back into the submission → `miyagi`'s rubric path renders it as a draft mark **with every
criterion traceable to a span** → `moodle-mcp` writes it to a *pending* state that a human must
confirm → the confirmation event, the draft, and the human's delta are all persisted as the
oversight record. 🟢 **That persisted delta is the deliverable the regulation actually wants**,
and no component here requires it to be built twice.
🔴 **Never wire `moodle-mcp` to write a final grade.** The write path is the compliance boundary.
🟢 **Delivery model: anything** — all four components are `PERMISSIVE`.

### 🟡 `Pattern BO` — Offline course-authoring for a ministry or school network (8–10 wk)

🔵 **Why AGPL is the right answer here and not a compromise.** EMEA public funding (Denmark's
€200M AI strategy, France's AI for Humanity, the Netherlands' national strategy) flows to
self-hosted public systems, and this is the buyer for whom `NETWORK_COPYLEFT` costs nothing.

| component | grant read this pass | role |
|---|---|---|
| [`ai-swarm-solutions-group/OpenTeacherAgent`](https://gitlab.com/ai-swarm-solutions-group/OpenTeacherAgent) | **AGPL-3.0-or-later** · 34 523 B · `0d96a4ff68ad` @ `59a33fecff73` | 🟡 `NETWORK_COPYLEFT` — intent → interactive exercises → self-contained offline HTML bundle with score tracking. Rust + Vue, single binary |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | MIT · 1 097 B · `3c056b34a476` @ `f72936bd41e5` | 🟢 `PERMISSIVE` — offline-first distribution and the learner record where connectivity is intermittent |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | MIT · 1 072 B · `383b85b370e8` @ `86ab328f0e5b` | 🟢 `PERMISSIVE` — SCORM wrapper so the exported bundle also ingests into the ministry's existing LMS |

**Wiring.** Teacher states an intent → `OpenTeacherAgent` authors exercises and course pages →
export once as its self-contained HTML bundle **and** once wrapped by `scorm-again` → distribute
and collect through `Kolibri` where there is no reliable network → scores reconcile on next sync.
🟡 **Delivery model: self-hosted only.** `OpenTeacherAgent` is AGPL and reaches users served over
a network. 🟢 Keep it in its own process behind a documented interface: the two MIT components
stay separable, so a later SaaS variant can replace the authoring stage without relicensing the
rest. 🔴 **Do not offer this stack as multi-tenant SaaS** without replacing the AGPL component.

### 🔴 Components refused for every recipe this pass, and why

| component | refused because |
|---|---|
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) (2 049★) | 🔴 Bespoke grant: non-commercial only, redistribution prohibited, revenue-share before any commercial deployment, and a **partial-use clause reaching a copied design pattern**. The §7 clause means reading it is a risk, not just vendoring it |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) (4 029★) | 🔴 `CC-BY-NC`. The best curriculum graph available and unusable in any paid engagement |
| [`walkinglabs/modern-llm-notebook`](https://github.com/walkinglabs/modern-llm-notebook) (272★) | 🔴 `CC-BY-NC-SA-4.0`. Would have been the spine of a corporate-upskilling curriculum; NonCommercial forbids it and ShareAlike would propagate into the deliverable |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) (340★) | 🔴 `Elastic-2.0` forbids hosted-service delivery, which is how a university CRM is delivered |
| [`leonine1983/aprendix`](https://github.com/leonine1983/aprendix) | 🔴 **No grant** at ten root paths. The right LATAM product shape; usable only as a **requirements reference** |
| [`rudra496/StealthHumanizer`](https://github.com/rudra496/StealthHumanizer) (189★, MIT) | 🔴 Permissive and refused on purpose: its function is defeating academic-integrity tooling |

---

## 🆕 `p467` — **🟢 Three recipes, every component's grant read FIRST-HAND this pass and stated with its `grant_class`, so each recipe names the delivery model it can legally be sold under. 🔴 And one recipe is a REPLACEMENT: the obvious build for a curriculum-aligned tutor uses a 4 000★ knowledge graph that cannot be used in any paid engagement, so the substitute is specified instead.**

🔵 **Rule for this file, now enforceable:** no component is named below unless its
`grant_class` was read from its payload this pass
([`evidence/grant-class.2026-10-26-p467.tsv`](../evidence/grant-class.2026-10-26-p467.tsv)), and no
recipe mixes a class its delivery model forbids.

### 🔴 `Pattern BL` — Curriculum-aligned adaptive tutor **without the unsellable graph** (8–10 wk)

🔵 **Buyer:** a K-12 publisher, ministry or tutoring provider that wants a tutor which teaches
*against a curriculum*, with prerequisites and diagnostics — the single most-requested education AI
shape, and the one with a licence trap directly in its path.

🔴 **The trap, stated first.** The obvious substrate is
[`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) — 4 027★,
1 644 knowledge points, 2 403 prerequisite edges, 6 723 items, curriculum-aligned, with adaptive
prerequisite diagnostics. It is **`CC-BY-NC-4.0`** (19 347 B · `41003d4a7474`, reproduced
byte-identical to `p466`). **NonCommercial bars every Globant engagement.** Do not plan around it;
it is a *design reference* for graph shape only.

🟢 **The substitute, and what it costs you.**

| layer | component | `grant_class` · grant read first-hand | why this one |
|---|---|---|---|
| curriculum graph | [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 🟡 `COMPOSITE_PER_ASSET` · code **MIT** · 5 789 B `d849ffef4f98` | Standards-aligned instructional content built as a data layer for educational AI. 🔴 **Clear each dataset separately** — `Open` tiers are usable, `Open+Gated` and `Gated` are not covered by any open licence. Budget a licence-clearance task, not an assumption |
| knowledge tracing | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 `PERMISSIVE` · MIT | The reference KT library (BKT/DKT/SAKT and successors); the mastery estimate the tutor sequences against |
| tutoring loop | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `PERMISSIVE` · Apache-2.0 · 11 408 B `cd2f54e1e506` @ HEAD `a31d82624c27` | Lifelong personalised tutoring with persistent learner state. 🟢 Four-pass byte-identical control — the most stable high-star row on these shelves |
| ITS discipline over any LLM | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 `PERMISSIVE` · MIT · 1 073 B `1e05c9440068` @ HEAD `8790a39f254b` | An MCP server that imposes intelligent-tutoring-system structure (BKT) on a plain model — the cheapest way to make the loop pedagogically accountable |
| graph rendering | [`wombats-writing-code/xoces`](https://github.com/wombats-writing-code/xoces) | 🟢 `PERMISSIVE` · MIT · 1 082 B `1115d8b49039` | Chord/tree widgets for hierarchical connected data — renders the prerequisite graph for teachers. 🔴 Dormant since 2025-11; vendor the component, do not depend on the project |
| delivery into the estate | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) + [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 `PERMISSIVE` · MIT · 1 072 B `383b85b370e8` · Apache-2.0 · 10 273 B `73ba74dfaa52` | SCORM/xAPI runtime and LTI hosting: the tutor runs inside the client's existing LMS with no LMS change |

🟢 **Delivery model this is sellable under: all of them.** Every code component is `PERMISSIVE`;
the only encumbrance is per-dataset content clearance. 🔵 **Wiring:** `knowledge-graph` datasets →
prerequisite DAG; `pykt` mastery estimates per node; `DeepTutor` owns the session and learner
memory; `tutor-mcp` constrains each turn to an ITS move; `xoces` renders progress; `scorm-again`
packages, `tsugi` launches.

### 🟢 `Pattern BM` — EMEA institutional LMS modernisation, with the licence chosen to match the buyer (10–12 wk)

🔵 **Buyer:** an EU/EEA university, region or ministry, self-hosting, under the Annex III
**2027-12-02** education deadline with Art. 50 transparency already live.

| layer | component | `grant_class` · grant | the licence decision |
|---|---|---|---|
| platform — **resale case** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 `PERMISSIVE` · MIT · 1 062 B `ceb97717de1f` | 🟢 The EMEA-placed permissive platform this base lacked (Polish, first-hand). Choose this when the client resells or runs multi-tenant |
| platform — **sovereign case** | [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 🟡 `NETWORK_COPYLEFT` · AGPL-3.0 · 34 523 B `8486a10c4393` | 🟢 AGPL is a **feature** for a public body: source availability to users is often a procurement requirement. Never for multi-tenant SaaS |
| module boundary | [`edrys-org/edrys`](https://github.com/edrys-org/edrys) | 🟡 `WEAK_COPYLEFT` · MPL-2.0 · 16 725 B `1f256ecad192` | 🟡 File-level copyleft: new modules stay proprietary, modified Edrys files do not. The safest copyleft to extend |
| accessibility conformance | [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) | 🟡 `STRONG_COPYLEFT` · GPL-3.0-or-later · 35 147 B `8ceb4b9ee5ad` | 🔴 Run as a **service alongside**, never vendored into a proprietary deliverable. Produces the accessibility evidence EU and US duties require |
| obligation triage | [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | 🟢 `PERMISSIVE` · MIT · 1 073 B `b7b08f330649` @ HEAD `41da87feb238` — 🟢 **reproduces `p437` byte-, digest- and HEAD-identical** | 🟢 The one carried tool whose encoded Annex III date is **2027-12-02** citing Reg. (EU) 2026/1744. 🔴 Not `ark-forge/mcp-eu-ai-act`, which hardcodes the superseded 2026-08-02 |
| offline / low-connectivity sites | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) + [`Wakoma/nimble`](https://github.com/Wakoma/nimble) | 🟢 MIT · 1 097 B `3c056b34a476` + 🟡 **CERN-OHL-S** · 13 419 B `d6475a84171f` | 🟡 **New capability, new obligation:** `nimble` gives the physical mesh under Kolibri, and CERN-OHL-S is **strongly reciprocal** — hardware derivatives must publish design sources. Fine for a public buyer, a decision for a commercial one |

🔴 **The one thing this recipe must not do:** mix the AGPL platform with a proprietary multi-tenant
deliverable. Pick the platform row from the delivery model **first**, then build — that is the whole
point of carrying `grant_class` on the row.

### 🟢 `Pattern BN` — LATAM: build-and-localise, because there is nothing to source (6–8 wk)

🔵 **Buyer:** a LATAM university system, ministry or edtech, facing UNESCO IESALC's **87 %**
adoption against **26 %** with a formal AI strategy, and the 92 %-student / 19 %-faculty
assignment-feedback split.

🔴 **Why this recipe is shaped differently from every other on this file.** Measured this pass:
**visible LATAM open-source education supply is 1 row in 103 (1 %)**, and that row
([`menthorlabs/menthor`](https://github.com/menthorlabs/menthor), Apache-2.0, 582★) is
**archived**. 🔴 Two independent passes (`p464`, `p466`) found the repositories matching the
feedback opportunity **ungranted**. 🟢 So this is not a sourcing exercise: **build on
globally-sourced permissive components, localise, and sell the governance deliverable** — the
governance half being precisely the 26 %-with-a-strategy gap.

| layer | component | `grant_class` | the LATAM-specific decision |
|---|---|---|---|
| rubric-based feedback engine | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🔴 `COMPOSITE_PER_ASSET (MIT code + NonCommercial content)` · 1 615 B `86c7be78af8b` | 🟢 **Use the MIT code — research-backed rubric evaluation is exactly the feedback gap.** 🔴 **Do NOT ship the bundled Annotated CLEAR Corpus**: it is `CC BY-NC-SA 4.0`. Substitute client-owned exemplars, which a university has and wants used |
| tutoring / feedback loop | `HKUDS/DeepTutor` | 🟢 `PERMISSIVE` · Apache-2.0 · `cd2f54e1e506` | Localise prompts and learner-model copy to pt-BR / es; the loop itself is language-agnostic |
| ITS structure | `ArnaudGuiovanna/tutor-mcp` | 🟢 `PERMISSIVE` · MIT · `1e05c9440068` | Keeps feedback pedagogical rather than generative-chatty — the faculty-trust blocker behind the 19 % |
| offline / low-bandwidth | `learningequality/kolibri` | 🟢 `PERMISSIVE` · MIT · `3c056b34a476` | Public-university campuses and rural sites; the deployment profile the region actually has |
| pedagogy reference (pt) | `menthorlabs/menthor` | 🟢 `PERMISSIVE` · Apache-2.0 · 11 337 B `36d6788503b8` | 🔴 **Archived — reference only.** Portuguese-language course structure and pedagogy vocabulary, not a dependency |
| governance deliverable | `tomdxb0004/eu-ai-act-risk-checker` as a **template** | 🟢 `PERMISSIVE` · MIT · `b7b08f330649` | 🟡 The EU obligation set is not LATAM law, but the *artefact shape* — risk tier, duty-holder, per-obligation date — is what a 26 %-strategy institution is missing. Re-point it at Brazil's Marco Legal, Colombia CONPES 4144 and Chile's Ley 21.719 |

🟢 **Delivery model: fully sellable**, provided the NC corpus is excluded — which is a
five-minute decision if `grant_class` is on the row and an expensive discovery if it is not.

---

## 🆕 `p466` — **🟢 Three recipes, each built only from rows whose grant was read FIRST-HAND this pass, and each matched to a delivery model by its licence family rather than in spite of it: an AGPL sovereign stack for EMEA institutions, a deterministic-and-reviewable assessment spine that satisfies four jurisdictions' converging requirement, and an LTI/SCORM carrier that turns the 23 % skill supply into something an estate can actually run.**

### 🟢 `Pattern BI` — EMEA sovereign federated learning estate (AGPL by design, 10–12 wk)

🔵 **Buyer:** an EU/EEA ministry, region or university consortium under sovereignty pressure, that
self-hosts. 🟢 **The licence fits the buyer:** every component is AGPL-3.0, which obliges source
availability to users — acceptable and often *desirable* for a public body, and the reason this
stack cannot be resold as multi-tenant SaaS.

| layer | component | grant (read first-hand `p466`) |
|---|---|---|
| schools workspace | [`DD-workspace/DD`](https://gitlab.com/DD-workspace/DD) | 🟡 AGPL-3.0 · 34 588 B · `a7f13bbcc053` |
| cross-institution OER exchange | [`moodlenet/backend`](https://gitlab.com/moodlenet/backend) + [`frontend`](https://gitlab.com/moodlenet/frontend) | 🟡 AGPL-3.0 · `feff6860d5ea` / `6dbb120dadf0` |
| demand-led course formation | [`Openki/Openki`](https://gitlab.com/Openki/Openki) | 🟡 AGPL-3.0 · `57c8ff33c9c0` |
| OER authoring | [`oer/emacs-reveal`](https://gitlab.com/oer/emacs-reveal) | 🔴 **composite** — `LICENSE` is a pointer; per-asset clearance required before any client delivery |
| mounting into the incumbent LMS | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) (LTI) | 🟢 Apache-2.0 · `73ba74dfaa52` |
| inference | self-hosted open-weight serving (carried: Ollama / vLLM) | 🟢 permissive |

**Wiring.** `DD` is the tenant surface per school. MoodleNet federates OER *between* institutions
over ActivityPub, so no central host owns the corpus — this is the technical content of
"sovereignty" and the reason MoodleNet rather than a shared drive. `Openki` handles the courses
that are demand-led (municipal reskilling, adult education) where no institution schedules them.
`tsugi` exposes each as an LTI tool so an existing Moodle/Open edX estate consumes them **without a
fork**. Inference stays on-premises: 🔴 **do not route learner text to a hosted model** — EU
Art. 5(1)(f) prohibits emotion inference outright and Art. 50 marking bites **2026-12-02**.

🔴 **Where it breaks.** All four AGPL components must be delivered as the client's own
self-hosted deployment, with modified source offered to users; a Globant-hosted shared instance
changes the obligation. `emacs-reveal`'s composite licence must be cleared asset-by-asset. `DD` is
a 12★ project — 🔵 treat it as a **fork base with a maintenance budget**, not a supported upstream.

### 🟢 `Pattern BJ` — Deterministic-and-reviewable assessment spine (6–8 wk)

🔵 **Buyer:** any institution that grades at scale under a jurisdiction that regulates it — which
per [`intel/trends.md`](../intel/trends.md) Trend 3 is now Oklahoma, Idaho, the EU, Chile and
Kenya, independently converging on the same three requirements: **deterministic scoring, an
auditable evidence trail, a human arbiter, and no affect inference.**

| layer | component | grant | the requirement it discharges |
|---|---|---|---|
| deterministic spine | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** · 1 512 B · `3a83d5b8e22c` | assign→release→collect→autograde→feedback with a release/solution split; **the score comes from executed tests, not a model** |
| secure execution | [`INGInious/INGInious`](https://github.com/INGInious/INGInious) (carried) | 🟢 permissive | sandboxed automated exercise assessment |
| rubric arbitration | [`erlan775959-code/markwise`](https://github.com/erlan775959-code/markwise) (carried `p465`) | 🟢 MIT · `e33397c72fff` | **double-marks each criterion with two independent graders plus a moderator**, and **verifies in code that every quoted evidence string actually occurs in the work** — invented evidence is flagged |
| arithmetic integrity | [`omerfarooq223/AutoGrader-Agent`](https://github.com/omerfarooq223/AutoGrader-Agent) (carried `p465`) | 🟢 MIT · `78adf0554b1a` | **all totals, deductions and capping computed in Python, not by the model**; template-matched briefs skip the LLM entirely |
| data minimisation | [`oas114/EduShield`](https://github.com/oas114/EduShield) (carried `p465`) | 🟢 MIT · `6c106d9deefc` | mask-then-restore de-identification **client-side, before** anything reaches a hosted model |
| LMS return path | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 MIT · `383b85b370e8` | scores and completion reported back to the incumbent LMS |

**Wiring.** `nbgrader` owns the gradebook and the deterministic score; the LLM layer is **advisory
only** and writes to a separate feedback field that a teacher releases. `markwise`'s two-grader +
moderator loop is the *human arbiter* requirement in code, and its evidence-string check is what
makes the trail auditable rather than merely logged. `AutoGrader-Agent`'s rule — **arithmetic in
Python, never in the model** — is what keeps a score reproducible under appeal. `EduShield` runs
first in the chain. `scorm-again` returns the released result.

🔴 **Where it breaks, and the carried risk exhibit that shows how.** This pattern is void the moment
anyone enables unattended marking. 🔴 `five-plus-one/AI-Marker-Suite` (carried as a **risk exhibit**,
GPL-3.0, 104★) advertises exactly that — *"leave it running overnight, it's all marked by
morning"* — which **bypasses the double-marking arbitration** and breaches Oklahoma SB 1734's
teacher-review duty and KNEC's SBA rule simultaneously. 🔵 Ship the human-release gate as
non-optional, or the architecture's legal value is gone.

### 🟢 `Pattern BK` — Skill-carrier: make the 23 % runnable inside an estate (4–6 wk)

🔵 **The problem this solves.** 9 of 39 visible education repositories now ship as an agent skill
with **no runtime** ([`agents/trending.md`](../agents/trending.md)) — excellent pedagogy, nothing an
institution can deploy, no roster, no gradebook, no audit trail.

| layer | component | grant | role |
|---|---|---|---|
| carrier | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 Apache-2.0 · `73ba74dfaa52` | LTI tool shell: identity, roster, **grade passback** |
| content runtime | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 MIT · `383b85b370e8` | SCORM/AICC reporting for packaged activities |
| pedagogy, as skills | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) (dual-ships) · [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) · [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) · [`ShawnRen57/omni-learning-anything`](https://github.com/ShawnRen57/omni-learning-anything) | 🟢 MIT where probed (`omni-learning-anything` 1 092 B · `f3a9a5d7a599`) | Socratic sequencing · slide-grounded exam coaching **with page citations** · diagnosis-before-instruction · plan generation |
| skill production | [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | 🟢 MIT · `LICENSE.md` 1 068 B · `be9b04bccfb4` | compiles the client's **own** licensed course texts into skills — 🟢 the step that makes the stack defensible, because the corpus is the client's |
| de-identification | [`oas114/EduShield`](https://github.com/oas114/EduShield) | 🟢 MIT · `6c106d9deefc` | client-side masking before any hosted inference |

**Wiring.** `tsugi` is the LTI shell the LMS launches; the skill runs behind it against a host
agent; `EduShield` masks on the way out; any score returns via `tsugi` grade passback or
`scorm-again`. `book-to-skill` is run on the **client's own** licensed material.

🔴 **Where it breaks — and this is the licence trap, stated once more because it is the pass's
headline.** 🔴 **Do not vendor `GarethManning/education-agent-skills`** (914★, the obvious choice):
it is **`CC-BY-SA-4.0`** (1 230 B · `f952182df4eb`), so adaptations inherit ShareAlike into a client
deliverable. 🔴 **Do not use `xiaoyang111222/cn-math-taxonomy`** (4 000★, the obvious knowledge
graph): it is **`CC-BY-NC-4.0`** (19 347 B · `41003d4a7474`) — **NonCommercial, so it is barred from
every paid engagement.** 🟢 Compile the knowledge graph from the client's own curriculum with
`book-to-skill` instead. 🔵 Per `Gap 466-A`: **read the first non-blank line of the payload before
adopting any skill or corpus.**

### 🔴 Not a pattern — the LATAM recipe that cannot be written

🔵 For the **second consecutive pass**, the component the clearest LATAM opportunity needs —
rubric-based assignment feedback in Portuguese/Spanish — **does not exist under a grant**:
`p464`'s row was ungranted, and this pass's Brazilian `henriquegpb/gradesinteli` (86★) is
`NO-ROOT-GRANT` @ HEAD `2ded74019bb2`. 🟢 The one granted LATAM row, `menthorlabs/menthor`
(Apache-2.0), is a teaching **platform** and last pushed **2024-04-21**. 🔴 **So the honest cell is
that `Pattern BJ` must be delivered into LATAM with its rubric layer BUILT, not sourced** — and
built before **2026-12-01**, when Chile's Ley 21.719 brings automated profiling and algorithmic
decisions in scope. That is the costing a LATAM engagement should carry, and it is a build line,
not a reuse line.

## 🆕 `p465` — **🟢 Three recipes, and the first one is the only permissive, audit-defensible marking stack this base can assemble — it became possible this hour. 🔴 The second is an IMPORT-AND-LOCALISE recipe for regions that have a mandate and no supply, which is a shape this file has never carried.**

🔴 **`make hooks` DENIED** (`Code from External`) — twelfth denial in thirteen passes; nothing
below is gate-attested. Every address named below was resolved by `git ls-remote` this pass and its
grant read at the payload; figures are **raw bytes** (`Gap 465-A`).

### 🟢 `Pattern BF` — Audit-defensible rubric marking with ZERO copyleft

🔵 **The problem it solves.** Marking is the highest-demand function in every region on
[`intel/market.md`](../intel/market.md), and until this pass every *adopted* option was GPL-3.0 or
AGPL-3.0 — a source-disclosure event for a hosted deployment. 🟢 A fully permissive path now exists.

| layer | component | grant · `sha256₁₂` | why this one |
|---|---|---|---|
| Marking workflow | [`erlan775959-code/markwise`](https://github.com/erlan775959-code/markwise) | 🟢 MIT · `e33397c72fff` | double-marking + moderator; **code-verified quote evidence**; grader-manipulation and safeguarding flags |
| Deterministic scoring | [`omerfarooq223/AutoGrader-Agent`](https://github.com/omerfarooq223/AutoGrader-Agent) | 🟢 MIT · `78adf0554b1a` | **all arithmetic in Python**, roster-first identity, TF-IDF + char n-gram similarity |
| Student-data shield | [`oas114/EduShield`](https://github.com/oas114/EduShield) | 🟢 MIT · `6c106d9deefc` | client-side mask→send→restore, so identifiers never reach the model |
| Obligation check | [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | 🟢 MIT · carried `p437` | the **post-Omnibus** date oracle (`highRiskAnnexIII: '2027-12-02'`); 🔴 **never** `ark-forge/mcp-eu-ai-act`, which hardcodes the retired 2026-08-02 deadline |

🔵 **Wiring.** `EduShield` masks the submission set in the browser → `markwise` transcribes and
double-marks each rubric criterion, emitting per-criterion scores with quoted evidence →
`AutoGrader-Agent`'s Python engine recomputes every total, deduction and cap so **no number
originates in a model** → disagreements above one rubric level, unverifiable quotes and safeguarding
flags route to a human queue → `EduShield` restores identifiers only for the teacher-facing view.
Run the risk-checker **first**: grading is Annex III point 3, so in the EU this is a high-risk
system from **2027-12-02** and an Art. 50 disclosure obligation **today**.

🔴 **State the weakness to the client, do not hide it.** `markwise` is **0★ and self-declared
Alpha**; `AutoGrader-Agent` is **3★**. This stack buys licence freedom and audit defensibility at
the price of adoption, and the honest alternative is `AI-Marker-Suite` (GPL-3.0, 104★) with its
disclosure boundary accepted. 🟡 Estimate **8–10 weeks** to a defensible pilot, most of it
hardening, not integration.

### 🟢 `Pattern BG` — Import-and-localise for a mandate-without-supply region (MEA)

🔵 **The problem it solves.** `intel/market.md` establishes this pass that MEA has the world's most
aggressive curriculum mandate (UAE KG–G12) and the emptiest open layer (African education ★ ceiling
**12**, Arabic **6**, nothing above a star floor of 5). 🔴 There is nothing regional to compose
from, so composition is the wrong frame: **the recipe is localisation with provenance.**

| step | component | grant | role |
|---|---|---|---|
| 1 · Identifier spine | [`stanleyHayes/ghanaschools`](https://github.com/stanleyHayes/ghanaschools) | 🟢 Apache-2.0 `0be2dbbe5781` | the pattern to **copy**, not the data: stable IDs + **field-level provenance**, and it declares "no personal, student or quality data" |
| 2 · Curriculum carrier | [`shakir-abdo/ch32v003-journey`](https://github.com/shakir-abdo/ch32v003-journey) | 🟢 MIT `b6f5c258ba79` | a working **bilingual Arabic/English** register-level curriculum + simulator — the localisation reference, 22 lessons deep |
| 3 · Offline delivery | [`KajarnakLOKOSSOU2008/edubox`](https://github.com/KajarnakLOKOSSOU2008/edubox) | 🟢 MIT `1196398ae2f6` | offline-first for low-connectivity deployment; 🟡 1★ prototype, carried for its shape |
| 4 · Lab substitute | [`ghwmelite-dotcom/AfriLab`](https://github.com/ghwmelite-dotcom/AfriLab) | 🟢 MIT `fb50db9e444c` | 29 science simulations where physical labs are absent |
| 5 · Grant hygiene | — | — | 🔴 **mandatory gate**: 5 of 20 novel MEA/Africa addresses served **no root grant at all**, and one states only an *intention* to license (`Gap 465-E`). Resolve every candidate at the payload before it enters a client deliverable |

🔵 **Wiring.** Stand up the registry spine first (step 1's *schema*, populated from the client's
ministry data), because every later layer joins on institution identity. Localise step 2's
bilingual pattern — RTL-correct, Arabic-first, English-secondary — rather than translating an
English course. Ship through step 3's offline path and treat connectivity as optional, not
degraded. 🟡 **12–16 weeks**, and the dominant cost is content localisation and grant diligence,
not engineering.

### 🟡 `Pattern BH` — Student-data egress control as a standalone North America engagement

🔵 **The problem it solves.** North America's binding edge has moved to **procurement and data
flow**: Alabama's model policy recommends a data-usage-restriction clause in district contracts and
California's **A.B. 1159** (proposed) would bar training models on student data. 🟢 A district does
not need a tutor to need this.

| layer | component | grant | role |
|---|---|---|---|
| Egress shield | [`oas114/EduShield`](https://github.com/oas114/EduShield) | 🟢 MIT `6c106d9deefc` | mask→send→restore **entirely client-side**; written for Taiwan's PDPA, mechanism is jurisdiction-portable |
| Policy mapping | [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | 🟢 MIT | carried `p437`; use for the EU arm of a multinational district/university |
| Identifier spine | registry pattern per `Pattern BG` step 1 | 🟢 Apache-2.0 | field-level provenance, so a contract clause can be **evidenced** rather than asserted |

🔴 **The honest caveat, carried from the component's own README:** `EduShield` states it provides
technical masking, is **not** legal advice, and does **not** by itself guarantee statutory
compliance. 🟢 Sell it as **an engineering control that makes a procurement clause auditable**, never
as compliance. 🟡 **4–6 weeks**; the deliverable is a data-flow map plus an enforced egress boundary.


## 🆕 `p464` — **🟢 Four recipes. `Pattern BE` is the one this pass's correction unlocks: a university-grade LMS stack with ZERO copyleft anywhere in it, which this base's own headline said was impossible. 🔴 And `Pattern BB` is the first recipe here whose first step is to DECLINE a feature the client asked for, because in the EU that feature has been illegal for 20 months.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was DENIED, and so was every
individual gate.** The harness permission classifier refused both `make hooks` and a direct
`python3` invocation of the repo's own gate scripts (`Code from External`) — **eleven denials in
twelve passes, and one step stricter than `p463`**, which was still permitted to run
`p277-table-structure` and `p383-region-heading-gate` by hand. 🔵 **Nothing below is
gate-attested.** Mitigation, re-implemented in this session's own code rather than the repo's:
frontmatter keys and closed-vocabulary `region` checked on all eight shelves; every new table
checked for separator presence, pipe-count consistency and **no header row published as data**;
append-only proved on both trending shelves by prior-section containment; **every address
introduced this pass re-resolved by `git ls-remote`.**

🔵 **Instrument.** Two first-hand channels, as `p450` and `p463` established:
`git ls-remote <addr> HEAD` (**tree identity**) and
`raw.githubusercontent.com/<addr>/<branch>/LICENSE` (**payload bytes** → size + `sha256₁₂`).
🔴 **The `curl -sI https://github.com/<addr>` probe the ingest brief prescribes is reproduced
unusable, now from a fourth independent direction:** it returns `403` for a live address and for
a nonexistent one *alike* — `openedx/edx-platform` and `gmilano/this-does-not-exist-xyz123` are
indistinguishable through it. No row here rests on it.

🔴 **A channel measurement that is new this pass, and a future pass will misread it if it is not
written down: the GitHub *search* API is not reachable from the `gh` CLI here.**
`gh api "search/repositories?q=..."` returns **`403 — "sessions are bound to their configured
repositories. Use repository-scoped endpoints"`**. Repository search survives **only** through
the MCP `search_repositories` tool; `gh` reaches only the two attached repos. 🔵 A pass that
reaches for `gh` to discover supply will read that `403` as *no results* and publish a nil that
is an artifact of the channel — the exact error class `p463` caught on the web legs.

### 🟢 Cross-pass controls — reproduced before any verdict

| control | published by `p463` | this pass read | verdict |
|---|---|---|---|
| 🟢 `openedx/edx-platform` `LICENSE` | AGPL-3.0 · 35 136 B · `e12d78569742` · HEAD `addd09d7801b` | **35 136 B · `e12d78569742`** · HEAD **`addd09d7801b`** | 🟢 **reproduced, byte-, digest- and HEAD-identical** |
| 🟢 `Vacademy-io/vacademy_platform` `LICENSE` | AGPL-3.0 · 34 523 B · `0d96a4ff68ad` · HEAD `3a9c66db938c` | **34 523 B · `0d96a4ff68ad`** · HEAD **`3a9c66db938c`** | 🟢 **reproduced** |
| 🟢 `DaRL-GenAI/instructional_agents` `LICENSE` | MIT · 1 067 B · `4e085d826a64` · HEAD `f835eb45f508` | **1 067 B · `4e085d826a64`** · HEAD **`f835eb45f508`** | 🟢 **reproduced** |

🔵 **Provenance of every component below.** Addresses marked 🟢 **re-read** were probed first-hand
this pass (`git ls-remote` + payload digest, recorded on the shelves above). Addresses marked
🔵 **carried** are taken from this base's existing cells and were **not** re-probed this hour —
stated so a reader knows which grants are this-hour fresh.

### 🟢 `Pattern BE` — The zero-copyleft redistributable learning stack (the corrected-claim recipe)

🔵 **Why it exists.** `intel/market.md` told readers for two passes that **exactly one** carried
platform was freely redistributable, so every recipe here routed proprietary work across a process
boundary. 🟢 `p464` found a second — **OpenOLAT, Apache-2.0, university-grade** — and with it a
full stack that can be **vendored into a client deliverable with no boundary argument at all**.

| layer | component | grant | basis |
|---|---|---|---|
| LMS / institution | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · 10 982 B · `6dbc5b605ed0` | 🟢 **re-read** @ HEAD `891b9434e822` |
| assessment delivery | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🔵 permissive · 2 058 B · `a5c692f12090` | 🔵 carried (digest stable since `p390`) |
| offline / low-connectivity | `learningequality/kolibri` | 🔵 **MIT** | 🔵 carried |
| interactive content | **H5P** | 🔵 **MIT** | 🔵 carried |
| mastery model | `CAHLR/OATutor` · `CAHLR/pyBKT` | 🔵 **MIT** | 🔵 carried |
| course generation + review schedule | [`Kaiji-Z/dsh-plugin-lookatstudy`](https://github.com/Kaiji-Z/dsh-plugin-lookatstudy) | 🟢 **MIT** · `157154a57ac1` | 🟢 **re-read** |
| learner practice | [`Nauv357/pickq`](https://github.com/Nauv357/pickq) | 🟢 **MIT** · `91192368c03b` | 🟢 **re-read** |
| provenance audit | [`yukunou703/studyproof`](https://github.com/yukunou703/studyproof) | 🟢 **MIT** · `e250f7a46d43` | 🟢 **re-read** |
| privacy-preserving training | `pytorch/opacus` | 🔵 **Apache-2.0** · 10 241 B · `bcf6964d43d8` | 🔵 carried (recovered by `p463`) |

**Wiring.** OpenOLAT is the system of record and the only thing the institution logs into.
`qtiworks` serves items; `lookatstudy` compiles the client's existing course material into a gated
skill tree and owns the **SM-2** review schedule, while `pyBKT`/`OATutor` own the **mastery
estimate** — keep these two separate, because the review scheduler and the mastery model answer
different questions and merging them is how auditability is lost. `pickq` is the learner-side
offline practice surface, syncing attempt records back as events. `studyproof` sits on every
generated explanation and refuses to emit one whose citation it cannot resolve. `opacus` is only
needed if you train on student records.
🟢 **What this buys that no other recipe here can:** the whole stack is Apache-2.0/MIT, so the
integration code, the configuration and the derived course content can be **delivered and
relicensed to the client** without an AGPL conversation. 🔴 **What it costs:** OpenOLAT is Java and
"strongly under-used" per this base's own cell — expect thin community answers and budget a
Java/Spring-capable team, which is the real reason teams default to Moodle and then inherit GPL.
**Effort:** 10–12 weeks to a running pilot.

### 🔴 `Pattern BB` — The EMEA attention-analytics refusal kit (declining a feature as the deliverable)

🔵 **The trigger.** An EMEA edtech or proctoring brief asks for engagement detection, attention
scoring, "is the student focused?", or sentiment from webcam or microphone. 🔴 **Under EU AI Act
Art. 5(1)(f) that is a prohibited practice and has been since 2025-02-02** — penalties to **€35 M
or 7 %** of global turnover, **no consent exception**. This is not a conformity exercise; there is
no lawful way to build it for EU learners.

**The recipe is a substitution table, and it is the proposal artefact.**

| what was asked for | 🔴 verdict | 🟢 lawful substitute that answers the same business question |
|---|---|---|
| webcam attention / emotion score | 🔴 prohibited | **task-level telemetry**: time-on-task, attempt counts, hint requests, abandonment points — behavioural events the learner performs, not inferred affect |
| "disengaged student" alerts | 🔴 prohibited if inferred from affect | **mastery-decay alerts** from `CAHLR/pyBKT` 🔵 carried — a falling mastery estimate is an observation about answers, not about a face |
| exam-integrity monitoring | 🟡 case-by-case; emotion inference out | item-level anomaly signals + 🟢 [`yukunou703/studyproof`](https://github.com/yukunou703/studyproof) (MIT, **re-read**) to audit whether submitted citations resolve |
| "personalised difficulty from engagement" | 🔴 prohibited as specified | 🟢 [`Kaiji-Z/dsh-plugin-lookatstudy`](https://github.com/Kaiji-Z/dsh-plugin-lookatstudy) (MIT, **re-read**) — BKT mastery + SM-2 scheduling drive difficulty from **performance** |

**Wiring.** Put every learner signal through one event schema that is **affect-free by
construction** — if a field cannot be derived from an action the learner took, it does not exist in
the schema. That makes the prohibition an architectural property rather than a policy promise, and
it is what survives an audit. Add 🔵 `pytorch/opacus` if models are trained on the event stream.
🟢 **Deliverable:** the substitution table above, signed off at proposal stage, plus the event
schema. **Effort:** 2–3 weeks as a compliance-and-architecture engagement; it usually precedes a
larger build.

### 🟢 `Pattern BC` — The adoption-mandate kit (Ohio · India · Edomex)

🔵 **The trigger**, and it is the demand class `intel/trends.md` `T2` names: a jurisdiction obliges
institutions to **adopt, promote or govern** AI by a date — **Ohio Rev. Code 3301.24** (policy
required by 2026-07-01, already past), **India** (AI + Computational Thinking from Class 3,
2026-27 session), **Estado de México Art. 61** (promote responsible use at upper-secondary and
higher level). 🟢 The buyer's success criterion is **"the artefact exists and is defensible"**, not
learning gain — which is why this is the one sellable category immune to the efficacy-evidence
blocker.

| deliverable | component | grant |
|---|---|---|
| tool-approval workflow with an enforceable allow-list | 🔵 this repo's own `compose/code/mcp-allowlist-gateway` pattern | 🔵 internal |
| teacher-facing explanation quality | 🟢 [`guicortei/feynman-technique`](https://github.com/guicortei/feynman-technique) | 🟡 **MIT code, corpus NOT MIT** — 🟢 **re-read** |
| measuring capability uplift in teacher training | 🟢 [`junichikatsu/SocraMetry`](https://github.com/junichikatsu/SocraMetry) | 🟢 **MIT** · `7b779e5b512d` — **re-read** |
| citation discipline in produced materials | 🟢 [`yukunou703/studyproof`](https://github.com/yukunou703/studyproof) | 🟢 **MIT** — **re-read** |
| offline delivery where connectivity is the constraint | 🔵 `learningequality/kolibri` | 🔵 **MIT** |

**Wiring.** The allow-list gateway is the spine: every AI tool a teacher may use is an entry with
an owner, a data-handling note and a review date, and the gateway refuses anything unlisted — that
single artefact satisfies the bulk of a 3301.24-style policy duty. `SocraMetry` instruments the
**teacher** cohort, not students: its 5-axis attainment/accuracy/growth output is the evidence an
education authority needs that its NISHTHA-style training spend changed capability.
`feynman-technique` sets the house style for generated explanations — 🔴 **and its carve-out is
load-bearing here: ship the skill, never the quoted corpus**, which rules out bundling its source
material into teacher handbooks. **Effort:** 6–8 weeks per authority; the policy artefact lands in
the first 2.

### 🟢 `Pattern BD` — The defensible-assessment pipeline (Vietnam · Annex III, 2027-12-02)

🔵 **The trigger.** Automated assessment under a regime that demands a **recorded human decision
point** and a reason per determination — Vietnam's July-2026 high-risk designation naming
automated assessment, and Annex III from 2027-12-02.

| stage | component | grant | boundary |
|---|---|---|---|
| item authoring **with a review workflow** | 🟢 [`gygy-open/question-bank`](https://github.com/gygy-open/question-bank) | 🔴 **AGPL-3.0** · `0d96a4ff68ad` — 🟢 **re-read** | 🔴 **institution-hosted service only**; never embedded in a Globant product |
| item delivery | 🔵 [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🔵 permissive | 🟢 vendorable |
| mastery estimate behind each score | 🔵 `CAHLR/pyBKT` · `CAHLR/OATutor` | 🔵 **MIT** | 🟢 vendorable |
| provenance of every generated rationale | 🟢 [`yukunou703/studyproof`](https://github.com/yukunou703/studyproof) | 🟢 **MIT** | 🟢 vendorable |
| training privacy | 🔵 `pytorch/opacus` | 🔵 **Apache-2.0** | 🟢 vendorable |

**Wiring.** `question-bank`'s review workflow is the **authoring-side** human decision point — the
piece this base has been missing, because every prior recipe placed the human only at scoring time,
and a defect introduced at authoring reaches every learner before any scorer sees it. Run it as a
service the institution owns (Docker), with Globant's work on the `qtiworks` and orchestration side
of the process boundary. 🔴 **The Affero obligation is real and specific:** customisations to
`question-bank` itself must be offered to its users, so keep client-specific logic in the
orchestration layer, not in forks of it. Every scored determination emits `{item id, model output,
mastery estimate, resolved citations, human reviewer, reason string}` — that record **is** the
conformity artefact. **Effort:** 8–10 weeks.

🔴 **One gap these four recipes cannot close, stated rather than papered over.** None of them
produces **evidence of learning gain**, because nothing on these shelves does (0 of 12 novel
addresses this pass; sixth consecutive pass). A client who asks "did it work?" still gets a study
design and an instrumented pipeline, **not** an off-the-shelf efficacy harness.

## 🆕 `p463` — **🟢 Five recipes, and the first one is new in kind: `Pattern AW` mines this base's OWN evidence store for silently evicted rows and returned a yield comparable to the discovery channel for ZERO network calls. 🟢 `Pattern BA` is the first end-to-end pipeline on this file with no copyleft anywhere in it, so it can be vendored into a client deliverable without a boundary argument.**

### 🟢 `Pattern AW` — Re-promotion before discovery: mine the base's own evidence files

🔵 **The recipe this pass's headline finding licenses, and it costs zero network calls.** At this
maturity the base's evidence store knows more than its shelves do.

1. Pick the newest `evidence/carried-existence.*.tsv` — it records, per address, the sell-shelf
   files that carried it at that commit.
2. 🔴 **Grade it at its OWN commit first** (`git show <commit>:agents/top.md`). If the claims
   reproduce there, any disagreement with HEAD is **churn, not a ledger defect**. Skipping this
   step is how `p455` published and retracted a 20.6 % defect rate.
3. Diff: every address the file attributes to a sell shelf and that `grep` cannot find on that
   shelf at HEAD is an **eviction**.
4. Split the evictions: still on another sell shelf → **moved** (fine); on none → **dropped**.
5. Re-probe every dropped address on both channels — `git ls-remote <addr> HEAD` and
   `raw.githubusercontent.com/<addr>/<branch>/LICENSE`.
6. Grade each: **no HEAD** → withdrawn, eviction justified; **no payload** → ungranted, justified;
   **untitled/short payload** → notice-only, justified; **GPL/AGPL** → justified off a build-on
   shelf; 🟢 **permissive + live → recover it, with a fresh cell.**

**Yield, measured this pass:** 238 claims → 37 evictions → 16 moved, 21 dropped → **11 justified,
10 recovered** (incl. the base's only differential-privacy row). 🔵 Compare the discovery channel
the same hour: 8 web legs + 6 API queries → 11 granted novel addresses. **Comparable yield; one
of them is free.**

### 🟢 `Pattern AX` — EMEA Annex III tutoring with a privacy boundary · 13-month runway

**The clock:** stand-alone high-risk education systems apply **2027-12-02** (Digital Omnibus, Reg.
(EU) 2026/1744). Admissions, student evaluation and exam scoring are Annex III high-risk, and the
Act reaches non-EU systems whose outputs affect EU students.

**Wiring, named repo by repo:**

- **Tutoring core** — `CAHLR/OATutor` (MIT, carried): Bayesian knowledge tracing, so a mastery
  claim is a traceable state, not a model opinion.
- **Evidence** — `pykt-team/pykt-toolkit` (MIT, carried) to *evidence* learning gain, plus
  [`ai4bharat/indicifeval`](https://github.com/ai4bharat/indicifeval) (MIT, **recovered this
  pass**) where instruction-following has to be scored rather than asserted.
- 🟢 **Privacy control** — [`pytorch/opacus`](https://github.com/pytorch/opacus) (Apache-2.0,
  10 241 B · `bcf6964d43d8`, **recovered this pass**): DP-SGD so a model trained on cohort data
  cannot memorise a student. 🔴 This is the layer every prior EMEA pattern asserted and none
  named a component for.
- **Platform seam** — an Open edX **XBlock** (Apache-2.0) over the AGPL-3.0 platform: proprietary
  work stays across the process boundary, never inside the AGPL tree.
- **Human decision point** — a recorded reason string per determination, which is also what
  Oklahoma's and Maryland's oversight clauses require, so the same build serves both regions.

**Boundary to respect:** Open edX is AGPL-3.0 (35 136 B · `e12d78569742`) and OpenEduCat is
LGPL-3.0 at ref `19.0`. Neither is a tier to relicense. **8–10 weeks** to a conformity-shaped
pilot.

### 🟢 `Pattern AY` — APAC multi-jurisdiction assessment agent · duty is LIVE

**The clock, inverted from EMEA:** Vietnam's July 2026 decision names **education** among six
high-risk sectors, citing **automated assessment** and **behavioural monitoring**, under a law in
force since **2026-03-01**; providers self-classify before deployment. Korea's AI Basic Act is in
force with a penalty grace year; China holds registration + labelling duties.

**Wiring:**

- **Answer core that can survive an audit** —
  [`Queena34/StudyPilot`](https://github.com/Queena34/StudyPilot) (MIT, 1 065 B · `1c49d485d539`):
  answers **only** from the supplied course corpus, **with citations**, and **refuses** when the
  corpus does not cover the question. 🟢 That refusal is the property a self-classification
  dossier can actually point at.
- **Institutional rules as an auditable artefact** —
  [`Andiii208/seu-handbook-skill`](https://github.com/Andiii208/seu-handbook-skill) (MIT, 1 497 B ·
  `965a0edb5701`): the regulation split **per clause with provenance**, so a determination cites
  the rule it applied.
- **Scoring evidence** — [`ai4bharat/indicifeval`](https://github.com/ai4bharat/indicifeval) (MIT)
  for Indic languages; `ai4bharat/anudesh-backend` (MIT) if instruction data must be collected.
- **LMS write-back** — [`bartmassey-upstream/canvas-mcp`](https://github.com/bartmassey-upstream/canvas-mcp)
  (MIT, 1 071 B · `5385a26e2fac`), [`bibo242/blackboard-mcp`](https://github.com/bibo242/blackboard-mcp)
  (MIT, 1 084 B · `d65abf96e389`), and
  [`anonymousonyx22/canvas-lms-student-mcp`](https://github.com/anonymousonyx22/canvas-lms-student-mcp)
  (MIT) for the student-scoped read side. 🔴 **All three were evicted from every sell shelf and are
  recovered this pass** — the whole LMS-connector tier had gone missing.
- **Data residency** — [`rasidi3112/pondok-ai`](https://github.com/rasidi3112/pondok-ai) (MIT,
  1 079 B · `c3dc4b0503f8`): one command stands up Ollama + Open WebUI + RAG + Qdrant +
  OpenAI-compatible API for a whole room, on hardware that never leaves the building.

**12–14 weeks**, and the risk-tier dossier is a deliverable, not a by-product.

### 🟢 `Pattern AZ` — LATAM: integrate over an interface, never vendor, never fork the student tier

**The shape of the demand, measured:** **92 %** of students and **79 %** of faculty engaged, but
only **19 %** of faculty use AI for assignment feedback while **half of students want it**, and
**61 %** of students fear peer misuse (DEC LATAM 2026, 30 000+ responses, 29 institutions).
🔴 **So the sellable thing is assessment feedback with an audit trail, not another tutor.**

**The hard constraint this pass measured:** the Brazilian ENEM/vestibular OSS tier is **6 of 6
ungranted** at 0–1★ — there is nothing there to fork, whatever it looks like.

**Wiring:**

- **Integration boundary** — `mcp-brasil/mcp-brasil` and `p443`'s `siu-guarani-mcp` (Argentine SIU
  Guaraní) as MCP servers in front of the institutional systems of record. 🔵 Every LATAM
  platform holding student records is copyleft (GPL-2.0/GPL-3.0/AGPL-3.0, **0 of 4** permissive),
  so the interface *is* the architecture.
- **LMS** — `bmosoluciones/now-lms` where a platform is needed at all.
- **Feedback core** — [`lowwwbank/anything-to-course`](https://github.com/lowwwbank/anything-to-course)
  (MIT, 1 066 B · `d41346e796d6`, **recovered this pass**) for material → practice, plus
  [`Aisland-SJL/Aisland-teach`](https://github.com/Aisland-SJL/Aisland-teach) (MIT) whose
  restatement check is an integrity answer rather than a detector.
- 🔴 **Do not** build on any address in the LATAM gap table. They are listed so nobody re-finds
  them, not so anybody ships them.

**6–8 weeks** to a faculty-facing feedback pilot at one institution.

### 🟢 `Pattern BA` — Curriculum-to-course pipeline, entirely permissive, entirely new this pass

🔵 Four rows this pass shelved compose into one pipeline with no copyleft anywhere in it:

1. **Curriculum structure** — [`seehiong/eduvis`](https://github.com/seehiong/eduvis)
   (Apache-2.0, 9 831 B · `898c5a5080eb`): a curriculum-aware IR with a schema validator and a
   reference SVG renderer. Pedagogical meaning separated from presentation, so the structure is
   reviewable by a subject expert who does not read code.
2. **Sequencing** — `withmarbleapp/os-taxonomy` (carried; 🔴 **ODbL + CC BY-SA 4.0 content** per
   `p442` — a share-alike **content** obligation, so use it to *order* topics, do not redistribute
   the graph inside a proprietary deliverable).
3. **Course generation** — [`lowwwbank/anything-to-course`](https://github.com/lowwwbank/anything-to-course)
   (MIT): material → retrieval practice + spaced repetition + tutor mode, as an agent skill.
4. **Verification** — [`Aisland-SJL/Aisland-teach`](https://github.com/Aisland-SJL/Aisland-teach)
   (MIT, 1 099 B · `f46f29be1b28`): teaches from the learner's level, then verifies by
   **restatement**. 🔵 Declares its derivation from Matt Pocock's `teach` (MIT) in its README —
   read the README for provenance on every skill-tier row, per `Gap 463-E`.
5. **Delivery, offline** — Kolibri (**MIT** — the only freely redistributable platform row) or
   [`rasidi3112/pondok-ai`](https://github.com/rasidi3112/pondok-ai) (MIT) for a LAN-local stack.

🟢 **Why this one is worth naming:** every component is MIT or Apache-2.0, so the whole pipeline
can be vendored into a client deliverable without a boundary argument — which is **not** true of
any pattern on this file that touches Moodle, Open edX, ERPNext or OpenEduCat. **4–6 weeks.**

## 🆕 `p462` — **No new pattern is added, because no new component was found: the prescribed channel returned 36 tokens and 34 are already wired into the recipes below. 🟢 What changes is that two recipe components are re-pointed to their canonical addresses and one component pair is SPLIT — a recipe that cites `instructional_agents` must now say WHICH one.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was NOT RUN, and the reason is new.**
This pass is executing under a harness whose permission classifier **refused the `make hooks`
invocation outright** (`Code from External`) — not a proxy failure, not a missing target, a refusal
to execute the repository's own Makefile. So **nothing below is gate-attested**, and the gate's
inability to run is itself the standing obstacle: `Gap 446-A` cannot be closed by a pass that is
not permitted to run the gate.

### 🔴 Component address corrections for the recipes below

🟢 No recipe is broken — both aliases still resolve and still serve the correct tree. These are the
addresses a recipe should cite going forward, so that a reader resolving components through the
GitHub index (which no longer resolves the old names) does not read them as missing:

| recipe component, as cited below | address to cite | effect on the recipe |
|---|---|---|
| `openedx/edx-platform` | `openedx/openedx-platform` | none — same tree (`addd09d7801b`), same AGPL-3.0 grant, same XBlock seam |
| `Vacademy-io/vacademy_platform` | `Vacademy-io/vacademy_edtech_platform` | none — same tree (`3a9c66db938c`), same AGPL-3.0 grant |

🔴 **And one component must be disambiguated before it is wired.**
`DaRL-GenAI/instructional_agents` and `Hyan-Yao/instructional_agents` are **two repositories**, not
one address and its alias:

| address | HEAD sha | last push | ★ | grant |
|---|---|---|---|---|
| `DaRL-GenAI/instructional_agents` | `f835eb45f508` | — | — | MIT · 1 067 B · `4e085d826a64` |
| `Hyan-Yao/instructional_agents` | `1c2a9f9e3d26` | 2026-06-18 | **22** | MIT · 1 067 B · `4e085d826a64` |

🔴 **Any recipe that wires "instructional_agents" as a course-generation component is
underspecified until `Gap 462-A` resolves fork direction.** Both carry a real MIT grant, so either
is buildable — but they are not interchangeable, and a recipe that does not name the sha is not
reproducible. 🟢 **Interim rule for a studio: pin the sha, not the name.**

### 🟡 The recipe consequence of the OpenEduCat grant read

🟢 `openeducat/openeducat_erp` is confirmed **LGPL-3.0** by payload read at its default ref `19.0`
(8 241 B · `528f840368`), against an index that says `NOASSERTION`. For any recipe that uses
OpenEduCat as the student-information-system layer, this is the operative constraint:

- 🟢 **LGPL permits use across a dependency boundary** — an Odoo *module* alongside OpenEduCat, or a
  service calling it over its API, does not inherit the copyleft.
- 🔴 **It does not permit relicensing OpenEduCat itself**, and the payload additionally reserves
  bundled external libraries to other GPL-compatible terms **per file** — so a recipe that vendors
  OpenEduCat source into a client deliverable inherits a per-file notice obligation.
- 🟢 **Pin the ref.** A recipe citing `main` gets a 404; the branch is `19.0`.

### 🔴 Why there is no new recipe this pass, stated rather than padded

🟢 Five consecutive passes on four distinct channels — and now on the prescribed channel itself —
have found no unshelved, granted education agent. The composition surface has therefore **not
changed**, and a new recipe written this pass would be a recombination of the same components
rather than a new capability. 🔴 **The honest reading is that the shelf's recipe set is complete
against the current supply**, and the next genuine pattern needs either a new component or a new
client constraint, neither of which this pass found.

## 🆕 `p461` — **Three recipes, each wired only from rows whose grant was verified this pass, and each written to survive the two defects this pass found: alias addresses (`Gap 461-A`) and `NOASSERTION` grants (`Gap 461-B`).**

🔴 **Gate posture per `Gap 446-A`: `make hooks` was NOT RUN.** Nothing below is gate-attested.
🟢 **Composition rule applied throughout:** copyleft platforms are reached **across a process or
API boundary**, never vendored, so the client's own code keeps its licence.

### 🟢 P461-1 — Auditable adaptive tutoring on the Apache seam (North America, 6–8 weeks)

🔵 **Problem it answers:** an Ohio-style district that adopted an AI policy by the 2026-07-01
deadline and must now *evidence* learning gain with student data staying in-house.

```
openedx/openedx-platform (AGPL-3.0, 8 209★)   ← platform, NEVER forked
  └── openedx/XBlock (Apache-2.0, 471★)        ← THE PERMISSIVE SEAM; client code lives here
       │   grant: LICENSE.TXT 11 358 B · cfc7749b96f6   (UPPERCASE .TXT — p460's trap)
       ├── tutoring XBlock
       │     └── CAHLR/OATutor (MIT, 271★) — BKT scaffolded hints, ReactJS
       └── mastery XBlock
             └── pykt-team/pykt-toolkit (MIT, 452★) — DKT/SAKT over courseware event logs
                   └── HFUT-LEC/EduStudio (MIT, 80★) — cognitive-diagnosis cross-check
  inference: self-hosted open-weight model (student data never leaves the tenant)
```

🟢 **Why the seam is the whole design.** Open edX is **AGPL-3.0** and AGPL reaches across a network
boundary, so a hosted fork would oblige publication of the client's work. XBlocks sit behind the
plugin API under **Apache-2.0** — the custom components do **not** inherit the platform's AGPL.
🔴 **Do not** vendor platform code into the XBlock; that collapses the boundary the pattern exists
to create. 🟡 Probe the grant at **`LICENSE.TXT`**, uppercase extension — lowercase 404s, which is
the defect `p460` recorded and nearly published as "no grant".

### 🟢 P461-2 — Compliance scaffolding ahead of the EU deadline (EMEA, 8–10 weeks)

🔵 **Problem it answers:** an EU institution whose automated marking or proctoring becomes
**high-risk on 2027-12-02**, but whose **transparency duty already binds since 2026-08-02**.

```
ILIAS-eLearning/ILIAS (GPL-3.0, 505★)  — or moodle/moodle (GPL-3.0, 7 543★)
  └── REST API boundary ONLY (copyleft stays on its side of the wire)
       ├── disclosure layer        → Art. 50 transparency: every student-facing turn
       │                             declares it is an AI (binding NOW, not delayed)
       ├── human-in-the-loop gate  → no grade is emitted without an educator action
       │                             (Annex III: evaluation of learning outcomes)
       ├── audit log               → immutable record of input, model, output, reviewer
       └── openfun/richie (MIT, 316★) — MIT catalogue/portal front, freely brandable
  inference: artcc/freelingo (AGPL-3.0, 208★) as the Ollama-backed reference for
             self-hosted local models  — study the integration, do NOT vendor (AGPL)
  ⛔ EXCLUDED BY LAW, not by preference: emotion recognition — prohibited in schools
     since 2025-02-02. Do not build it, do not demo it.
```

🟡 **Grey-area warning that changes the build:** predictive dropout / early-warning tooling is
classifiable as **high-risk** on some readings of Annex III. If P461-1's pyKT mastery layer is
deployed in EMEA, it inherits the human-oversight and logging duties — so build the audit log
**first**, not last. 🔵 Sixteen extra months exist (2026-08-02 → 2027-12-02); the transparency
layer does not get them.

### 🟢 P461-3 — National-curriculum teacher enablement (APAC, 4–6 weeks)

🔵 **Problem it answers:** China's compulsory AI subject from age six (≥8 h/student/year in
Beijing) and India's compulsory AI from Class 3 starting **2026–27** both need teacher-facing
material at national scale in the same academic year.

```
course + material generation
  └── Hyan-Yao/instructional_agents (MIT, 22★)   ← CANONICAL ADDRESS
        🔴 NOT DaRL-GenAI/instructional_agents — that address is an ALIAS (Gap 461-A).
           Grant proof: MIT License, 1 067 B · 4e085d826a64,
           copyright line still reads "Copyright (c) 2025 DaRL-GenAI" (a transfer).
        multi-agent ADDIE: syllabus → LaTeX slides → assessment  (EACL 2026)
  ├── delivery / tutoring
  │     └── HKUDS/DeepTutor (Apache-2.0, 43 537★) — persistent learner model, 6 modes
  ├── explanation levelling
  │     └── DreambigOu/ELI5 (MIT, 1 854★) — retarget one explanation across grade bands
  └── localisation check
        └── DAMO-NLP-SG/M3Exam (105★) — multilingual/multilevel exam benchmark
              🟡 grant unresolved this pass — use to EVALUATE, do not redistribute
  ⚠️ DO NOT WIRE IN: ECNU-ICALK/EduChat (975★) — NO GRANT, ~15 months stale.
     It is the obvious APAC choice by reputation and it is unusable.
```

🟢 **Why `instructional_agents` at 22★ and not something bigger.** It is **MIT**, peer-reviewed
(EACL 2026 Main), and carries **120 forks against 22 stars** — a fork-to-star ratio above 5, which
is the signature of a repository people *run* rather than bookmark. 🔵 On this shelf that ratio is
a better adoption signal than ★.

### 🔴 Wiring prohibitions carried forward from this pass

| do not | reason |
|---|---|
| 🔴 vendor `GarethManning/education-agent-skills` (**913**★) | **CC-BY-SA-4.0** — share-alike; the index's `NOASSERTION` hides this |
| 🔴 vendor `24kchengYe/human-skill-tree` (**584**★) | **AGPL-3.0** by payload; also ~7 months stale |
| 🔴 build on `JushBJJ/Mr.-Ranedeer-AI-Tutor` (**29 548**★) | **NO GRANT** — 404 × 3; popularity is not permission |
| 🔴 build on `aaryansamanta/ai-ethos` (**498**★) | **NO GRANT** |
| 🟡 fork `openeducat/openeducat_erp` (**899**★) into proprietary modules | **LGPL-3.0** by payload — **link**, do not fork into |

---
## 🆕 `p460` — **No new pattern, and the reason is `p459`'s: zero granted novel inputs. 🟢 What this pass ships instead is a GATE STEP every existing pattern is missing, forced by a defect this pass found in its OWN instrument — a grant ladder that is case-blind on the filename publishes a false ungranted and discards a usable dependency. 🔴 And the first draft of that gate step had a SECOND defect, caught by running it rather than by reading it.**

🔵 This pass returned **0 granted novel addresses** (34 surfaced, 1 unshelved, that one ungranted at
10 paths — see [`agents/top.md`](../agents/top.md)). Every component a new recipe could be wired
from is already wired into a pattern below.

### 🟢 `P460-A` — the case-insensitive grant ladder, run before any vendoring step

🔴 **The failure it prevents, measured on a carried foundation row this pass:** `openedx/XBlock`
serves **no grant** at `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.txt`, `LICENCE`,
`LICENSE-MIT`, `license`, `MIT-LICENSE` or `NOTICE` on its resolved default ref — and serves
**Apache-2.0** at **`LICENSE.TXT`**. 🔵 A ladder stopping at the lowercase forms concludes
`UNGRANTED` for a permissively licensed dependency: `Gap 455-A`'s expensive direction.

Code, with its controls, at
[`compose/code/p460-grant-ladder/p460a.sh`](code/p460-grant-ladder/p460a.sh):

```bash
#!/usr/bin/env bash
# P460-A — resolve the default ref, then walk grant paths CASE-INSENSITIVELY.
# Separates: GRANTED | POINTER_OR_STUB | REPO_LIVE_NO_GRANT | ADDRESS_DEAD.
set -uo pipefail
repo="$1"   # e.g. openedx/XBlock

ref=$(git ls-remote --symref "https://github.com/$repo" HEAD 2>/dev/null \
      | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
if [ -z "$ref" ]; then echo "$repo ADDRESS_DEAD (no ref)"; exit 0; fi

stems="LICENSE LICENCE COPYING NOTICE LICENSE-MIT MIT-LICENSE LICENSE-APACHE"
# NOTE: the empty extension is a literal "" array entry, NOT produced by
# `eval echo` — an unquoted empty word is dropped by word-splitting and the bare
# stem is then never probed. That defect is what made this ladder's own first
# draft miss plain `LICENSE`; see the retraction below.
exts=("" ".md" ".txt" ".TXT" ".rst" ".MD" ".html")

for s in $stems; do
  for e in "${exts[@]}"; do
    lower=$(printf '%s' "$s" | tr 'A-Z' 'a-z')
    upper=$(printf '%s%s' "$s" "$e" | tr 'a-z' 'A-Z')
    for cand in "$s$e" "$lower$e" "$upper"; do
      url="https://raw.githubusercontent.com/$repo/$ref/$cand"
      code=$(curl -s -o /tmp/p460.payload -w '%{http_code}' --max-time 12 "$url")
      # GATE ON STATUS, never on body: a 404 here is a 14-byte "404: Not Found"
      # that a byte-reader will otherwise shelve as a licence (Gap 453-E(d)).
      if [ "$code" = "200" ]; then
        sz=$(stat -c%s /tmp/p460.payload)
        if [ "$sz" -lt 200 ]; then
          echo "$repo POINTER_OR_STUB $cand ${sz}B"; continue
        fi
        echo "$repo GRANTED $cand ${sz}B $(sha256sum /tmp/p460.payload | cut -c1-12)"
        echo "  title: $(head -2 /tmp/p460.payload | tr -d '\n' | tr -s ' ' | cut -c1-58)"
        exit 0
      fi
    done
  done
done
# Live-but-ungranted is NOT dead: probe a known-present file before concluding.
live=$(curl -s -o /dev/null -w '%{http_code}' --max-time 12 \
       "https://raw.githubusercontent.com/$repo/$ref/README.md")
[ "$live" = "200" ] && echo "$repo REPO_LIVE_NO_GRANT (ref=$ref)" \
                    || echo "$repo UNRESOLVED (ref=$ref)"
```

🟢 **Run, not asserted — controls in all four verdict directions:**

| control | expected | 🟢 emitted |
|---|---|---|
| `openedx/XBlock` — grant at an **uppercase extension** | `GRANTED` | `GRANTED LICENSE.TXT 11358B cfc7749b96f6` |
| `HKUDS/DeepTutor` — grant at the **bare stem** | `GRANTED` | `GRANTED LICENSE 11408B cd2f54e1e506` — **reproduces `p458`** |
| `CAHLR/OATutor` | `GRANTED` | `GRANTED LICENSE 1105B 5baaaf977a28` |
| `Selleo/mentingo` | `GRANTED` | `GRANTED LICENSE 1062B ceb97717de1f` |
| `mwasifanwar/eduadapt-ai` — live, ungranted | `REPO_LIVE_NO_GRANT` | `REPO_LIVE_NO_GRANT (ref=main)` |
| two fabricated addresses | `ADDRESS_DEAD` | `ADDRESS_DEAD (no ref)` ×2 |

### 🔴 The retraction, recorded because it is the whole lesson

🔴 **This pass's first draft of `P460-A` reported `REPO_LIVE_NO_GRANT` for `HKUDS/DeepTutor` and
`Selleo/mentingo` — both of which serve a plain `LICENSE`.** The cause: the extension list was
written as a string `"'' .md .txt …"` expanded with `eval echo`, and an unquoted empty word is
**dropped by word-splitting**, so the bare stem was never probed. 🔴 **A ladder written to fix a
false ungranted shipped a false ungranted of its own, in its first draft, on the highest-★ row on
these shelves.** 🟢 It was caught by **executing the controls**, not by reading the code — the
defect is invisible on inspection and unmistakable on run. 🔵 Same class as `Gap 455-D`'s *"a
defect that failed to travel inside one pass"*, and the standing lesson for this file: **a pattern
containing code is not shippable until its controls have been run in every verdict direction it
claims to separate.**

### 🔴 Where to wire it

Every pattern on this file that clones or vendors a component runs `P460-A` on that component
first and **halts on `REPO_LIVE_NO_GRANT`**. 🔵 It replaces `curl -sI`-style reachability entirely:
per this pass's measurement, `api.github.com/repos/<any-unattached-repo>` returns a **byte-identical
403** for a live repository and a fabricated one, so an existence check built on it cannot fail
safe.

## 🆕 `p459` — **No new pattern. The inputs did not change, and a recipe assembled from unchanged inputs would be a new name for an existing pattern rather than a new capability.**

🔵 This pass returned **0 granted novel addresses** (42 probed, 2 unshelved, both ungranted — see
[`agents/top.md`](../agents/top.md)). Every component a new pattern could be wired from is already
wired into one of the patterns below.

### 🟢 What was checked before declaring this

🔵 Each of the two candidate addresses was tested against the one question that would justify a new
recipe — *does it do a job no carried pattern already does?*

| candidate | job | already covered by |
|---|---|---|
| [`Takamatsu-Hikaru/AI-Research-Guide`](https://github.com/Takamatsu-Hikaru/AI-Research-Guide) | curated study pathway into a field | 🔵 the curriculum-graph tier (`os-taxonomy` + `skillpilot`) already generates pathways from *official* curricula, and is granted |
| [`selmetwa/parallel-arabic`](https://github.com/selmetwa/parallel-arabic) | language reading/practice | 🔵 `artcc/freelingo` (AGPL-3.0, carried) covers the self-hosted language tier; the grant question is the only open one and `parallel-arabic` is **worse** on it (no grant at all) |

🔴 Neither is granted, so neither could be wired into a deliverable pattern even if the job were
novel.

### 🔵 Pattern BD and its predecessors are re-affirmed, not replaced

Every component of **Pattern BD** (the ungradeable-by-itself tutor) was re-probed for liveness this
pass and all resolve at their recorded refs. 🟢 The objection it answers — OECD 2026 finding
chatbot gains vanished once access was withdrawn — is unchanged, and so is the pattern.

🔴 **The honest recommendation this pass makes is not a pattern at all:** the next genuinely new
education recipe will come from a *deeper* channel than the one the encargo prescribes (conference
artefacts, LMS plugin registries, national procurement catalogues), or from one of the eleven
industry shelves that has had no pass in 86 days. See [`intel/trends.md`](../intel/trends.md).

## 🆕 `p458` — **Pattern BD: the ungradeable-by-itself tutor — a tutoring stack whose grader is NOT the model that teaches, wired from four repos verified this pass**

🔵 Every component below was read first-hand at its resolved default ref this pass (grants,
byte counts and digests in [`agents/top.md`](../agents/top.md)). 🟢 This pattern exists because the
objection it answers is now the sector's main one, and it is on file: **OECD 2026** found chatbot
gains vanished or reversed once access was withdrawn, and **1EdTech** reads the sector as having
moved from experimentation to governance. 🔴 A stack whose tutor grades its own output cannot
answer either.

### The wiring

```
                     ┌──────────────────────────────────────────┐
  official curriculum│  enpasos/skillpilot      Apache-2.0      │
  (state/ministry)   │  → prerequisite skill graph + mastery    │
                     └───────────────┬──────────────────────────┘
                                     │ "learner is ready for topic T"
                                     ▼
                     ┌──────────────────────────────────────────┐
                     │  Man0dya/Tutor-AI        Apache-2.0      │
                     │  → 4 separable agents:                   │
                     │    content · questions · eval · feedback │
                     └──────┬──────────────────────┬────────────┘
                            │ question             │ explanation
                            ▼                      ▼
        ┌───────────────────────────┐  ┌────────────────────────────┐
        │ Hussain004/SAMOSA   MIT   │  │ FredMichel/chalkcast  MIT  │
        │ → step audit, EXACT,      │  │ → Manim render, then       │
        │   over finite fields      │  │   VISUALLY VERIFIES it     │
        └───────────┬───────────────┘  └────────────┬───────────────┘
                    │ pass / fail (no LLM)          │ verified asset
                    └───────────────┬───────────────┘
                                    ▼
                     ┌──────────────────────────────────────────┐
                     │  mastery written back to skillpilot      │
                     │  ONLY on a non-LLM pass verdict          │
                     └──────────────────────────────────────────┘
```

### Why each piece, specifically

| Step | Repo | Licence | Why this one and not the model |
|---|---|---|---|
| 1. What to teach next | [`enpasos/skillpilot`](https://github.com/enpasos/skillpilot) | Apache-2.0 | Its prerequisite edges come from a **published state curriculum** (German Gymnasium), so sequencing is defensible to a ministry or school board. Ask the LLM instead and you cannot cite the ordering. |
| 2. Teach and ask | [`Man0dya/Tutor-AI`](https://github.com/Man0dya/Tutor-AI) | Apache-2.0 | Already splits content / question-set / evaluation / feedback into **four separable agents** — so step 3 can replace the evaluator without a rewrite. That seam is the whole point. |
| 3a. Grade maths and stochastics | [`Hussain004/SAMOSA`](https://github.com/Hussain004/SAMOSA) | MIT | Checks **every step** of a derivation exactly over finite fields. Deterministic, auditable, reproducible — three properties an LLM grader does not have. |
| 3b. Grade the explanation asset | [`FredMichel/chalkcast`](https://github.com/FredMichel/chalkcast) | MIT | **Renders then visually verifies** the Manim output, so a broken or misleading animation is caught before a learner sees it. |
| 4. Record mastery | back into `skillpilot` | Apache-2.0 | Write mastery **only** on a step-3 pass. The LLM never writes to the mastery store. |

### The one rule that makes it an engagement claim rather than an architecture diagram

🟢 **Nothing on the LLM's path may write to the mastery store.** The model proposes; `SAMOSA` or
`chalkcast` disposes; only their verdict is persisted. 🔵 That single constraint is what lets a
studio answer "how do you know the learner actually learned it" with an artefact rather than an
assurance — and it is auditable after the fact, because the grader is deterministic and its input
is on disk.

### Regional substitutions, all verified this pass

🔵 The grader and the curriculum source are the parts that must be local; the middle two are not:

| Region | Swap in | Licence | For |
|---|---|---|---|
| **EMEA** | [`barzoj/somtoday-mcp`](https://github.com/barzoj/somtoday-mcp) · [`OmarZen/scholarship-navigator`](https://github.com/OmarZen/scholarship-navigator) | MIT · MIT | Dutch parent-portal reporting · Erasmus Mundus progression advice |
| **EMEA** (🟡 copyleft — reference only) | [`Arudchayan/adam-mcp`](https://github.com/Arudchayan/adam-mcp) | GPL-3.0 | **ILIAS 10** institution-of-record reads (Univ. of Basel) |
| **APAC** | [`IndexFlowing/MandarinClips-mcp`](https://github.com/IndexFlowing/MandarinClips-mcp) · [`mcxiaoxiao/kaoyan-navigator-skill`](https://github.com/mcxiaoxiao/kaoyan-navigator-skill) | MIT · MIT | HSK 3.0-aligned TCSL corpus · 考研 admission sequencing |
| **North America** | [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) (read-only, 26 `GET` tools) · [`RohanMuppa/Brightspace-API`](https://github.com/RohanMuppa/Brightspace-API) | MIT · MIT | Canvas and Brightspace as the system of record |
| **LATAM** | 🔴 **no row verified this pass** | — | 🔵 The channel reached LATAM but returned only already-carried supply (`alejooroncoy/campus-cli`, UPC Peru). Build step 1 from a **national curriculum document**, not from a repo, until a LATAM curriculum-graph address exists. |
| **Global** | [`lilong65190349/mcd-math-journey`](https://github.com/lilong65190349/mcd-math-journey) | MIT | The externally-verified-answer-key technique, portable to any subject with a priced or computable ground truth |

🟡 **Maturity warning, stated because the star counts invite a wrong read:** `skillpilot` is at
3 ★, `SAMOSA` at 2 ★, `chalkcast` at 0 ★. 🔵 These are shelved on provenance and on verifiability,
not on community review. 🟢 For a client engagement, treat Pattern BD as an **architecture to
implement**, taking the technique from each repo, rather than four dependencies to pin.


## 🆕 `p457` — **🟢 Two recipes forced by this pass's measurements: an offline paper-to-psychometrics assessment line for the install base these shelves could not serve, and a licence-drift gate for the failure `p457` caught — a dependency that was MIT when it was shelved and commercial when it was read.**

🔴 **`make hooks` DENIED** (`Code from External`) — twelfth denial in thirteen passes. 🔵 Nothing
below is gate-attested; instrument and controls at
[`compose/code/p457-payload-census/`](../compose/code/p457-payload-census/census.py).

### 🟢 `P457-1` — The offline paper-assessment line (OMR → item analysis → LMS write-back)

🔵 **The engagement:** an exam office or ministry unit that scores MCQ assessments on paper, at
cohort scale, without reliable connectivity — the envelope every server platform on
[`verticals/solutions.md`](../verticals/solutions.md) assumes away. 🟢 Every component is permissive
and every ref is stated, because `p456` proved refs cannot be inherited.

```bash
# 1. Sheet design, scanning, scoring, merit lists -- offline, one machine.
git clone -b main   --depth 1 https://github.com/crispin0007/OMR          # Apache-2.0
# 2. Exam administration: uncertain-mark review, attendance reconciliation, auditable Excel.
git clone -b main   --depth 1 https://github.com/sajidbuet/OMRFlow        # MIT
# 3. Field intake where there is no scanner: phone camera.
git clone -b master --depth 1 https://github.com/Udayraj123/OMRChecker    # MIT  <- master, NOT main
# 4. Item-level psychometrics on the response matrix (already on these shelves).
git clone -b master --depth 1 https://github.com/patriciamar/ShinyItemAnalysis   # GPL-3 (DESCRIPTION)
git clone -b main   --depth 1 https://github.com/philchalmers/mirt              # IRT  <- main
```

🟢 **The wiring, and the reason the stack is more than its parts:** the OMR layer's output is a
**per-item response matrix** — candidate × item × mark. That is precisely the input the
psychometrics tier consumes, so the pipeline runs:

```
scanned sheets ──▶ OMR (crispin0007/OMR | OMRFlow)
                      │  per-item response matrix (CSV)
                      ├──▶ scoring + merit list        ──▶ results to candidates
                      ├──▶ mirt / ShinyItemAnalysis    ──▶ item difficulty, discrimination,
                      │                                     distractor analysis, flagged items
                      └──▶ LMS write-back (optional)   ──▶ Moodle / Canvas gradebook
```

🔴 **Where the LLM goes, and where it must not.** The scoring path is **deterministic and must stay
so** — a mark is read by computer vision against a template, never inferred by a model, because a
contested grade has to be reproducible from the sheet. 🟢 **The model's place is the uncertain-mark
queue and the item review**: `OMRFlow` already exposes a review step for marks its CV layer cannot
resolve, and that queue — not the gradebook — is where an agent earns its keep by proposing a
reading with the cropped bubble image attached for a human to confirm.

🔴 **Two constraints to price, both measured rather than assumed:**
`crispin0007/OMR` is **Windows-only** by its own README, so the offline node is a Windows box —
plan the deployment, don't discover it. And `bthicks/OMR-Grader`, the fourth engine in this space,
is **GPL-3.0** (35 149 B `3972dc9744f6`): it stays behind a service boundary or out of the
deliverable.

🟡 **Pair it with `P457-2` when the cohort includes blind or low-vision candidates** — a paper-first
pipeline is the *worst* case for accessibility, and the remedy is in the next pattern, not in a
caveat.

### 🟢 `P457-2` — The accessible-assessment layer (MathML → braille + speech, on-device)

🔵 **The obligation, not the feature:** accessible instruction and assessment is statutory in the
regions these shelves sell into (IDEA / Section 504; European Accessibility Act). 🟢 The permissive
supply, read first-hand this pass:

```bash
git clone -b main --depth 1 https://github.com/NSoiffer/MathCAT                            # MIT
git clone -b main --depth 1 https://github.com/AVauraTech/assistive-ai-accessibility-suite # MIT
git clone -b main --depth 1 https://github.com/Sais-gallego/braillevision-ocr              # MIT
git clone -b main --depth 1 https://github.com/open-source-accessibility/monarch-message   # MIT
```

🟢 **The line, in the direction the obligation runs:**

```
item content (MathML)  ──▶ MathCAT ──┬──▶ speech, 15 languages (embedded engine commands)
                                     ├──▶ braille: Nemeth / UEB Technical / CMU
                                     └──▶ structural navigation (overviews, drill-down)
                                              │
refreshable device ◀── monarch-message ◀──────┘        (APH Monarch, US school install base)

existing PAPER material ──▶ braillevision-ocr ──▶ text ──▶ speech   (embossed + printed 6-dot)
candidate input modality ──▶ AVaura suite (eye-gaze, air writing, ASL fingerspelling, captions)
                              └─ MediaPipe on-device via WASM, offline fallback
```

🔴 **Why the on-device property is the architectural decision and not a detail:** assessment audio
and braille output for an identified candidate is **student data**. Routing it to a cloud endpoint
puts an accessibility accommodation inside the scope of exactly the rules these shelves track —
California AB 1159 on student data and AI training, GDPR, the EU AI Act's Annex III treatment of
evaluation. 🟢 **MathCAT runs locally and the AVaura suite runs in the browser tab with WASM**, so
the accommodation is deliverable **without a data-transfer argument at all**, which is both cheaper
to ship and the stronger position in a procurement review.

🟡 **Stated as scope, not as a claim:** `MathCAT` is production-grade and DAISY-sourced; the other
three are small projects. Price them as components to harden, not platforms to adopt.

### 🔴 `P457-3` — The licence-drift gate (the step that would have caught `p457`'s one disagreement)

🔵 **The defect being fixed is this base's own.** A shelf cell said **MIT**. The payload at `HEAD`
said **`Pengusto Commercial License 1.0`**, effective **two days** earlier. Nothing about the
address, the stars or the activity changed. 🔴 **Every recipe on this file that names a dependency
without pinning and re-reading its grant has this exposure**, and 3 of 457 carried addresses
re-issued licence text in one 48-hour window.

```bash
# The gate. Run it at vendoring time and in CI -- not once at selection time.
slug=$1; want=$2                      # e.g.  pengusto/google-classroom-mcp  MIT

# 1. Resolve the ref authoritatively. curl -sI returns 403 for every real repo here (Gap 449-A);
#    ls-remote is the channel that works, and it gives you the COMMIT to pin.
read -r _ ref <<<"$(git ls-remote --symref "https://github.com/$slug" HEAD | head -1)"
commit=$(git ls-remote "https://github.com/$slug" HEAD | cut -f1)

# 2. Read the grant AT that ref. No grant there IS the answer -- do not walk to a stale alias
#    looking for a friendlier one (p456's withdrawn-MIT lesson).
for p in LICENSE LICENSE.md LICENSE.txt LICENCE COPYING; do
  code=$(curl -sL -o /tmp/g -w '%{http_code}' "https://raw.githubusercontent.com/$slug/HEAD/$p")
  [ "$code" = 200 ] && break
done

# 3. Grade the TITLE, and record bytes + digest INCLUDING the trailing newline.
head -14 /tmp/g | grep -qiE "$want"  || { echo "DRIFT: $slug no longer grants $want"; exit 1; }
printf '%s\t%s\t%s B\t%s\n' "$slug" "$commit" "$(wc -c </tmp/g)" "$(sha256sum /tmp/g | cut -c1-12)"

# 4. If the payload is a 49-108 byte stub, the grant is in the MANIFEST, not the file.
#    CRAN:  DESCRIPTION -> License:        npm: package.json      Python: pyproject.toml
```

🟢 **Three rules this gate encodes, each paid for by a measurement on these shelves:**

1. 🔴 **Pin the commit, not the branch.** `ls-remote` hands you both in one request.
2. 🔴 **Vendor the grant TEXT into your tree.** `adriasantacreu/google-classroom-mcp` serves **no
   licence file at six paths** — its MIT text is readable only inside the fork that relicensed it.
   If you did not copy it, you cannot now produce it.
3. 🟡 **A stub is not a grant and a manifest can be the grant.** `rstudio/gradethis` serves a
   **49-byte** `LICENSE` carrying a year and a holder; the grant is `DESCRIPTION: MIT + file
   LICENSE`. A payload-only check calls that project ungranted.

🔵 **Scope it honestly:** this gate detects drift at the moment it runs. It does not watch
(`Gap 457-C`), and these three relicensings were found by re-reading all 457 addresses — which is
the cost of not having had the gate.


## 🆕 `p456` — **🟢 Two recipes, both forced by this pass's measurements: a ref-pinned vendoring step that every earlier pattern on this file is missing, and an EMEA national-system adapter built so that the maintainer withdrawal `p456` caught is survivable rather than fatal.**

🔴 **`make hooks` DENIED** (`Code from External`) — eleventh denial in twelve passes. 🔵 Nothing
below is gate-attested; 31 controls run in both directions
([`compose/code/p456-ref-resolution/controls.py`](../compose/code/p456-ref-resolution/controls.py)).

### 🟢 `P456-1` — Ref-pinned platform vendoring (a correction to every pattern on this file)

🔴 **The defect being fixed:** every clone step on this file names a repository without a ref. For
**11 of the platforms these patterns build on, the default branch is a release line**, so those
steps pin silently to whatever the maintainers last promoted — and change meaning between passes.

🟢 **The step, with the refs measured first-hand this pass:**

```bash
# Resolve before you clone. One request, authoritative.
git ls-remote --symref https://github.com/ILIAS-eLearning/ILIAS HEAD
#   ref: refs/heads/release_11   HEAD     <- NOT main, NOT master

# Then pin explicitly, always with -b:
git clone -b release_11        --depth 1 https://github.com/ILIAS-eLearning/ILIAS
git clone -b release           --depth 1 https://github.com/overhangio/tutor
git clone -b 19.0              --depth 1 https://github.com/openeducat/openeducat_erp
git clone -b v4.0.x-develop    --depth 1 https://github.com/bigbluebutton/bigbluebutton
git clone -b v31.0.00          --depth 1 https://github.com/GibbonEdu/core
git clone -b maven/fixes/10.0  --depth 1 https://github.com/edu-sharing/Edu-Sharing
git clone -b 2.12              --depth 1 https://github.com/portabilis/i-educar
git clone -b mobile            --depth 1 https://github.com/francoisjacquet/rosariosis
git clone -b 2.2               --depth 1 https://github.com/krayin/laravel-crm
git clone -b 3.x               --depth 1 https://github.com/RusticiSoftware/TinCanPython
git clone -b public            --depth 1 https://github.com/tl-its-umich-edu/caliper-php-public
```

🔴 **And read the grant at the resolved ref, not at a guessed one.** The one-line rule this pass
installs, after a guessed ref put a withdrawn MIT grant on `agents/top.md`:

```bash
# The grant is what the DEFAULT branch serves. No grant there IS the answer.
curl -sL -w '%{http_code}' https://raw.githubusercontent.com/OWNER/REPO/HEAD/LICENSE
```

🟢 `HEAD` is safe for this and now measured: it pointed at the resolved default branch for
**439 of 439** live addresses, **zero divergences**. 🔴 **What is not safe is walking on to
`master`/`main` when `HEAD` has no licence** — that is how `lanis-mobile/LanisAPI` was shelved as
MIT off a rename alias pointing at `deprecated-0.4.1`. 🔵 Use
[`compose/code/p456-ref-resolution/resolve.py`](code/p456-ref-resolution/resolve.py) to get the
typed verdict (`GRANT_AT_DEFAULT` / `GRANT_OFF_DEFAULT` / `GRANT_ONLY_AT_ALIAS` / `LIVE_NO_GRANT` /
`ADDRESS_DEAD`) rather than a boolean.

### 🟢 `P456-2` — EMEA national-system adapter, built to survive its own upstream

🔵 **The engagement:** a German *Land* or French académie wants an AI assistant over a gradebook or
portal it does not own and the client cannot fork — Schulportal Hessen, PRONOTE, EcoleDirecte,
WebUntis. 🔴 **The measured risk this pass adds:** the client libraries are **withdrawal-prone**
(`T2`). One of `p455`'s eleven was deprecated by its maintainers within a pass; two others are in
maintenance mode or abandoned. 🟢 **So the pattern's whole job is to make the adapter replaceable.**

| layer | what to use | grant (read at the resolved default branch) |
|---|---|---|
| portal client, **isolated** | [`lanis-mobile/liblanis-for-python`](https://github.com/lanis-mobile/liblanis-for-python) (Schulportal Hessen) · [`bain3/pronotepy`](https://github.com/bain3/pronotepy) (PRONOTE) · [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) (DACH timetabling) | **MIT** `1 079` B `66f943b0689f` · **MIT** `1 062` B `4f074ab7dccb` · **MIT** `1 070` B `d2e54565d9bf` |
| agent + tool surface | [`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) — FastAPI + LangGraph, rubric grading with **totals computed in code** | **MIT** `1 071` B `e70d1d08d60a` |
| LMS tools, where a Moodle also exists | [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) (**upstream**, ~140 tools) | **MIT** `1 067` B `66fa873bd85d` |

🟢 **Wiring, and the three constraints are structural rather than advisory:**

1. 🟢 **One adapter interface, one implementation per portal.** Every call to `liblanis`,
   `pronotepy` or `WebUntis` goes through a single `PortalClient` port — read timetable, read
   grades, read homework. 🔴 **Nothing above that port imports the vendor library.** When the next
   upstream is deprecated, you replace one module; `p456` had to replace exactly one.
2. 🔴 **Pin the client, and treat a pre-release as pre-release.** `liblanis` is `1.0.0a1`,
   needs **Python ≥ 3.14** and is **not on PyPI** — so it is vendored from a pinned commit at
   `master`, with `lanis-mobile/LanisAPI@deprecated-0.4.1` kept as a **read-only reference
   implementation**, never as a fallback dependency.
3. 🔴 **Honour the one stated rate limit on these shelves.** WebUntis: never 10 req/s, ≤ 1 800/h,
   in no case > 3 600/h, **permanent blocking** as the penalty — so the portal client sits behind a
   token-bucket limiter and a cache, and the agent is never allowed to drive it directly.

🔵 **Licence boundary:** every row above is **MIT**, so the adapter and agent layer are Globant's
to own and ship. 🔴 **The only GPL path in this tier is
[`arnim279/untis-api-client`](https://github.com/arnim279/untis-api-client)** (GPL-3.0-**or-later**,
declared *and* served), which is also the only one on WebUntis's **public** JSON-RPC API — so the
documented-API route and the permissive route are different repositories, and choosing the
documented one is a copyleft decision. 🟡 **8–10 weeks** for one portal plus the agent surface;
🔴 each additional portal is a new adapter, not a configuration flag.

### 🔴 What these two recipes deliberately do NOT claim

🔴 Neither is gate-attested (`make hooks` denied). 🔴 `P456-2`'s commercial framing rests on EMEA
market figures that are **relayed and uncheckable from this host** (`Gap 455-E`), and EMEA has **no
institution-level adoption rate** on these shelves at all (`Gap 456-D`) — the one on offer is
refused on [`intel/market.md`](../intel/market.md). 🟢 The **licences and refs** in both recipes
are byte-level first-hand reads, and those are the parts a build can be staked on.

## 🆕 `p455` — **Two recipes, built only from grants read first-hand at `HEAD` this pass. `P455-A` is the EMEA engagement this base could not have specified a pass ago; `P455-B` is the licence gate that `Gap 454-C` proves every deliverable here needs and no pass had built.**

🔴 **`make hooks` DENIED** (`Code from External`) — tenth denial in eleven passes.

### 🟢 `P455-A` — EMEA parent/teacher assistant over a closed national school system (6-8 weeks)

🔵 **The shape this is for:** a French or DACH client whose system of record is **PRONOTE**,
**EcoleDirecte**, **Schulportal Hessen** or **WebUntis** — proprietary, closed, un-forkable, and
reachable only through community clients (`Trend 41`). There is no platform to customise, so the
deliverable is an **adapter plus agent layer**, and the whole licensing question is settled before
any model is chosen.

**Wiring, by country, with the grant that permits it:**

| layer | 🇫🇷 France | 🇩🇪🇦🇹🇨🇭 DACH | grant (read this pass) |
|---|---|---|---|
| **1. System-of-record adapter** | [`bain3/pronotepy`](https://github.com/bain3/pronotepy) (PRONOTE) or [`studoo-app/ecole-directe-api`](https://github.com/studoo-app/ecole-directe-api) (EcoleDirecte, PHP) | [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) (timetables) + [`kurwjan/LanisAPI`](https://github.com/kurwjan/LanisAPI) (Schulportal Hessen) | 🟢 **all MIT** — `1 062`/`1 071`/`1 070`/`1 076` B, digests on [`agents/top.md`](../agents/top.md). **Vendorable** |
| **2. Rate governor** *(not optional)* | — | per-tenant token bucket at **<10 req/s, ≤1 800 req/h, hard ceiling 3 600 req/h** | 🔴 The limit is the vendor's, stated by `Suiram1701/WebUntisAPI.Client`; penalty is **permanent blocking** |
| **3. Adapter isolation** | one process per client library, typed DTO out | same | 🟡 The client tier is unofficial and breaks when the vendor moves — `pronotepy` is in maintenance mode, `ecoledirecte.js` abandoned 2023-08-08 |
| **4. Tool surface** | MCP server exposing `get_grades`, `get_timetable`, `get_homework`, `get_absences` — **read-only** | same | 🔵 Follow [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp)'s shape (MIT at root) but 🔴 **never vendor its tree** — `legacy_reference/` is GPL-3.0 |
| **5. Agent** | any permissive framework already shelved | same | 🟢 Keep the adapter boundary so the model layer is replaceable |

🔴 **Two rules this recipe exists to enforce, and both are measured rather than cautious:**

1. 🔴 **Do not take the public-API client into a vendored deliverable.**
   [`arnim279/untis-api-client`](https://github.com/arnim279/untis-api-client) is the only WebUntis
   client on the **documented public** JSON-RPC API, and it is **GPL-3.0-or-later** (`35 562` B
   `72d2f09334f8`). 🟢 Its `or-later` grant is declared *and* served, so it **may** be taken
   forward into a GPL-3.0 service — but then that service is GPL-3.0. 🔵 **The permissive path and
   the documented path are different repositories**; choose one deliberately and write the choice
   into the architecture decision, because it is not recoverable later.
2. 🔴 **The Lanis clients are a copyleft trap in the Rust/TS lane.**
   [`lanis-mobile/lanis-rs`](https://github.com/lanis-mobile/lanis-rs) and
   [`elderguardian/maria`](https://github.com/elderguardian/maria) are both **GPL-3.0-or-later**;
   only `kurwjan/LanisAPI` (Python) is MIT. 🔵 A Python adapter is therefore the vendorable choice
   for Hesse, and the language decision is a **licensing** decision here.

🔵 **Why 6-8 weeks and not 4:** the per-tenant rate governor, the credential handling for
parent/teacher accounts, and one adapter rewrite budgeted against the maintenance tail.

### 🟢 `P455-B` — the pre-ship licence gate, version-aware (2-3 days to wire, runs per build)

🔵 **Why this is a pattern and not a script:** `Gap 454-C` showed this base graded two mutually
incompatible licences as the same constraint for an entire pass, and `Trend 42` shows 11 cells still
cannot answer a compatibility question. Any deliverable assembled from these shelves inherits that.

**Wiring:**

1. 🟢 **Read the grant first-hand, gated on status.** Import
   [`fetch_fast.grant()`](../compose/code/p455-version-axis/fetch_fast.py). 🔴 It must be this
   ladder and not a `HEAD`-only read: `Gap 455-A` measured `kurwjan/LanisAPI` serving **no licence
   at `HEAD` and MIT at `master`**, and a first-live-ref reader reports a false *unlicensed* —
   discarding a usable dependency.
2. 🟢 **Grade with the version axis.**
   [`family_version.family()`](../compose/code/p455-version-axis/family_version.py) — title-anchored
   (a preamble cannot reach it) and version-bearing. 🔴 **Do not import
   `p453-vocabulary-ledger/verify.py::family`**: `Gap 454-A` records its 40-line window as unsound
   and it is still unpatched.
3. 🟢 **Read the forward grant separately.** `only_or_later()` over the whole payload, because the
   election lives in the per-file notice and the *How to Apply* appendix, never the title block.
   🔴 Treat `UNSTATED` as **undecided**, never as permission.
4. 🟢 **Decide with `compatible()`**, which returns `False` for differing GNU versions of one family
   and 🔵 **`None` — "not decided here" — rather than a reassuring `True`** for everything outside
   the GNU axis.
5. 🔴 **Close the dependency tree, not the root.** Apache-2.0 or MIT at the root does not clear the
   tree (`Trend 40`); chain `compose/code/dependency-licence-closure`.
6. 🔴 **Three failure modes to assert against, each one a defect this pass's own instrument had:**
   a registry **200 with a malformed body** read as *"declares no licence"* (`Gap 455-C` — assert
   record **shape**, not status); the compact shorthand **`gplv3`** falling through a normaliser
   that only handled the spaced form (`Gap 455-D`); and 🔴 **a per-subtree grant** that a root-only
   reader cannot see at all — `librus-mcp` is MIT at root and GPL-3.0 under `legacy_reference/`,
   so the gate must probe the **paths the deliverable actually vendors**, not just the repository root.

🔵 **Control discipline, carried from `Gap 454-E`:** run the gate's own assertions in **both**
directions and include a **fabricated negative control** (`nope-…/nope-…` → `ADDRESS_DEAD`), or the
positives are a property of the probe and not a measurement. 34 controls cover the modules above
([`controls.py`](../compose/code/p455-version-axis/controls.py)); three of this pass's four
instrument defects were caught by them before anything was published.

## 🆕 `p454` — **Three recipes, each built only from grants read first-hand at `HEAD` this pass. 🟢 `P454-A` is the licence reader this pass had to build because the carried one mis-grades 2.8 % of payloads; `P454-B` is an Indonesia engagement on four MIT rows; `P454-C` is the three-grant clearance an education deliverable actually needs.**

🔴 **`make hooks` DENIED** (`Code from External`) — ninth denial in ten passes.

### 🟢 `P454-A` — The payload-first licence gate, with the four routes the carried reader lacks

🔵 **Problem it solves.** `p453` established *"the payload at `HEAD` is the grant; the registry
field is a hint"*. This pass found that the **reader of the payload** is itself an error source:
5 of 179 carried payloads (2.8 %) grade wrong, and three of the five grade as `UNREAD` — the
verdict that invites a promotion.

**Wire-up** — [`compose/code/p454-carried-cell-value/`](code/p454-carried-cell-value/):

1. **Fetch gating on `%{http_code}`, never on body length.** `curl -s -w '%{http_code} %{size_download}'`;
   consult the body only on `200`. 🔵 Live control this pass:
   `raw.githubusercontent.com/ckeditor/ckeditor5/HEAD/LICENSE` → **404 with a 14-byte body**
   reading `404: Not Found`. A byte-reader records a 14-byte licence.
2. **Route 1 — title-block anchoring for the GPL family.** Discriminate `AGPL`/`LGPL`/`GPL` on the
   **first non-empty lines only**. A 40-line window fails on GPLv2, whose preamble recommends the
   LGPL at line 15 (`family_title.py`).
3. **Route 2 — the `NOT-OSI` class, tested by the ABSENCE of an affirmative grant.** Do **not**
   enumerate refusals: Nakafa's content licence refuses as *"not public domain, not open content,
   and not free material"*, which no enumeration anticipated. The sound test is *title names a
   licence/policy/terms* **AND** no grant form (`permission is hereby granted…`,
   `redistribution and use…`, an OSI title) appears. 🔴 And never trigger on
   `all rights reserved` — that is the opening line of
   [`davepacheco/node-extsprintf`](https://github.com/davepacheco/node-extsprintf)'s **MIT**
   payload.
4. **Route 3 — in-repo pointer, followed ONE hop.** A payload under `600` B naming another path is
   an absence, not a refusal; resolve it and grade the target (`pointer_target()`).
5. **Route 4 — composite detection by DISTINCT FAMILIES NAMED, never by heading count.** Heading
   count graded `aksara`'s 15 numbered sections as a composite and lost `bncc-pacotes`'s MIT half.
6. **Controls both directions, asserting values EARLIER passes published.** 23 controls; 8 assert
   prior payload digests (`nodetool` `4df3c306ddda`, `escolar` `3b443e863252`, `collegedata-fyi`
   `a3a16c648652`). 🟢 Three of this pass's four reader defects were caught that way and none
   reached a shelf.

🔴 **Known limit, registered as `Gap 454-C`:** `canon()` collapses GPL **versions**, so
`edu-sharing/Edu-Sharing` (npm says `GNU GPL v2`, payload serves **GPL-3.0**) grades `AGREE`
although the two licences are **incompatible**. Add a version axis before trusting a GPL cell.

**Effort:** 1-2 days to port into an existing SBOM step; it is a reader, not a service.

### 🟢 `P454-B` — An Indonesia schools engagement on four MIT rows

🔵 **Context.** Dapodik is the Ministry's single register of schools, teachers and students —
closed, with no open core, like ÉcoleDirecte in EMEA. 🟢 Unlike ÉcoleDirecte, its client layer is
**MIT in three languages at three strata**.

**Stack, all grants read first-hand at `HEAD` this pass:**

| layer | component | grant |
|---|---|---|
| register access (Node services) | [`ardianryan/dapodik-sdk`](https://github.com/ardianryan/dapodik-sdk) | **MIT** · `1 739` B `29e7d361ee3d` |
| register access (PHP estate) | [`adereksisusanto/dapodik-api-php`](https://github.com/adereksisusanto/dapodik-api-php) | **MIT** · `1 105` B `ce39902853af` |
| student identity | [`smantriplw/vervalpd-node`](https://github.com/smantriplw/vervalpd-node) | **MIT** · `1 068` B `0ae5076b1e03` |
| aggregate reporting | [`bantenprov/dapodik-data-guru`](https://github.com/bantenprov/dapodik-data-guru) | **MIT** · `1 072` B `3508ba25c5ad` |
| orchestration | `LangGraph` (MIT) + `LiteLLM` (MIT) — already carried on these shelves | — |

**Wire-up:** `dapodik-sdk` (or `dapodik-api-php` where the client runs PHP) as the register
adapter → `vervalpd-node` as the identity resolver behind it → `dapodik-data-guru` as the
reporting shape to mirror for other provinces → LangGraph nodes for the per-province policy
differences, with LiteLLM holding the model choice so an on-shore model can be swapped in.

🔴 **Two risks to price, not hide.** (a) `vervalpd-node` is a **scraper of a non-documented API**:
budget a change-detection test suite, and treat it as fragility rather than an SLA.
(b) `bantenprov/*` is **one province** (Banten) — the aggregate tier is a template to generalise,
not national coverage.

**Effort:** 6-8 weeks for a provincial pilot with the reporting tier; the register adapters are
days, the policy differences are the work.

### 🟡 `P454-C` — Three-grant clearance for an education deliverable

🔵 **Why.** Education verticals ship curriculum with code, so one artefact carries two legally
different asset classes plus a brand. Found independently on two continents this pass
(`T454-2`).

**The clearance, per asset — three reads, three digests, recorded separately:**

1. **Code grant** — the payload at `HEAD`, via `P454-A`. Record path, bytes, `sha256_12`, date.
2. **Content/data grant** — a *different* file. `bncc-pacotes` → `LICENSE-DADOS.md`
   (`1 108` B `965ba269fac6`, **CC BY 4.0**, with the attribution string the project asks for);
   `aksara` → `CONTENT_LICENSE.md` (`10 053` B `2af44ab89691`, **not open**).
3. **Brand grant** — usually a **withholding**, and it binds the deliverable's UI.
   `bncc-pacotes` withholds wordmark, logo, colours and typography outright; `aksara` →
   `TRADEMARKS.md` (`4 508` B `3ba64345e201`).

🔴 **The failure this prevents, stated concretely:** vendoring `bncc-pacotes` on its registry
`MIT` badge ships **CC BY 4.0 curriculum data with an attribution duty** inside an npm tarball or
a PyPI wheel — the project states both artefacts carry both grants — and a deliverable that
renders that data without the attribution string is out of compliance while every SBOM tool
reports `MIT`.

🟢 **And date the read.** `nakafaai/nakafa.com` moved from Source Available `1.0` (`7 705` B
`de3d94045061`) to `2.0` (`11 997` B `97e8bdc2e3cd`) on `2026-10-24`, and §13 puts **every act
started on or after that date** under the new terms regardless of when the copy was taken. A
clearance without a date is a statement about the past.

**Effort:** half a day per asset the first time, then a CI step.

## 🆕 `p453` — **Three recipes, each built only from grants read first-hand at `HEAD` this pass. 🟢 `P453-A` is the three-probe promotion gate this pass proved is necessary — because a live, MIT-granted, correctly-back-linked package can still have nothing to do with education. 🟢 `P453-B` is a US institution-intelligence engagement that is buildable for the first time. 🟢 `P453-C` is a French parent-facing agent on a closed national SIS.**

🔴 **`make hooks` DENIED** (`Code from External`) — eighth denial in nine passes. Nothing here is
gate-attested; the load-bearing contracts were re-implemented independently and all are green.

---

### 🟢 `P453-A` — The three-probe promotion gate

🔵 **The defect it closes.** `Gap 452-B` asked for a reachability probe before promotion. This pass
built it, ran it on 182 candidates — and then found
[`food-x-technologies/escolar`](https://github.com/food-x-technologies/escolar): **live** at `HEAD`,
**real MIT payload** (1 075 B `sha256₁₂ 3b443e863252`), npm record **back-linking the exact slug**,
and a surface that reads *"Replace properties in json with file contents."* 🔴 **Two probes are not
enough. Three are.**

| # | probe | instrument | what it establishes | what it CANNOT establish |
|---|---|---|---|---|
| 1 | **back-link** | `vocab_probe.norm()` — forge-qualified, case-folded | the registry record belongs to **this** address | that the address is reachable (`Gap 452-B`) or that the licence value is right (`Gap 453-A`) |
| 2 | **reachability** | `vocab_probe.live_probe()` — `raw/HEAD/{9 paths}` → `git ls-remote` | the address resolves **now** | that the repository is on-topic |
| 3 | 🆕 **surface** | first-hand `README.md` read at `HEAD` | what the project **is** | — |

🟢 **Wiring it, concretely:**

```bash
# 1+2: candidate discovery with both probes, writing the spend ledger
python3 compose/code/p453-vocabulary-ledger/run_legs.py
#   -> evidence/vocabulary-spend-ledger.2026-10-26-p453.tsv
#      columns: leg, term, verdict, package, address, reachable, licence_declared,
#               probe_leg, prior_shelf_files, novelty

# 3: grant read title-anchored + byte-exact, for every surviving address
python3 compose/code/p453-vocabulary-ledger/verify.py {owner}/{repo} ...
#   bytes from curl -w '%{size_download}'  (NOT $(...), which strips the
#   trailing newline and runs every count one short -- Gap 450-C defect (b))
#   family from the payload TITLE   (NOT a body grep, which calls every
#   GPLv3 file LGPL -- Gap 450-C defect (a))

# 3b: the probe no instrument can replace -- read the README and decide
curl -s https://raw.githubusercontent.com/{owner}/{repo}/HEAD/README.md | head -40
```

🔴 **Do not skip probe 3 because probes 1 and 2 are green.** On this pass's population that
combination was green for **157** addresses and correct for **6**.

---

### 🟢 `P453-B` — US institution intelligence, keyed to `UNITID` (North America)

🔵 **Why it is buildable only now.** `Gap 452-D` recorded that the US registry layer's *"packaged
permissive form is simply unknown here"*. Five MIT rows later it is known, so the engagement no
longer starts with a data-acquisition project.

| layer | component | grant, read first-hand |
|---|---|---|
| ingestion | [`UrbanInstitute/ipeds-scraper`](https://github.com/UrbanInstitute/ipeds-scraper) | **MIT** · `LICENSE.md` 1 058 B `bac93c5411aa` |
| warehouse | [`paulgp/ipeds-database`](https://github.com/paulgp/ipeds-database) → DuckDB, 27 M rows / 23 tables, 1997-2024 | **MIT** · 1 056 B `1126322e2cc8` |
| query layer | [`scienceforamerica/scipeds`](https://github.com/scienceforamerica/scipeds) (directory + completions, 2025 data) | **MIT** · 1 088 B `e04b31a1be21` |
| current-year disclosure | [`bolewood/collegedata-fyi`](https://github.com/bolewood/collegedata-fyi) — 4 071 archived CDS docs, 1 105-field schema | **MIT** · 1 115 B `a3a16c648652` |

🟢 **The wiring, and the one rule that makes it defensible:**

1. Build the DuckDB warehouse (`uv run python build_database.py`) — one command, ~1 GB.
2. Load the CDS extracts beside it, keyed on zero-padded `UNITID` (`ipeds_id`).
3. 🔴 **Keep the two sources in separate labelled tables and never coalesce a field.** IPEDS is the
   federal baseline; the CDS is school-authored and current-year. They disagree **by
   construction** — and `collegedata-fyi` refuses to blend them for exactly this reason.
4. Put the agent **on top of the warehouse, not on the PDFs**: retrieval over typed rows, with
   every answer citing `(source ∈ {CDS, IPEDS, Scorecard}, year, UNITID)`.

🔵 **The sellable wedge, from this pass's own NA market leg:** **10 %** of US institutions have
formal AI guidelines and **71 %** of teachers are untrained — so the first deliverable is an
institution-intelligence and governance layer, not a tutor. 🟡 All four grants are permissive, so
the deliverable can be closed-source; `collegedata-fyi`'s own figures are **self-reported** from
its 2026-08-06 audit and should be re-counted before they appear in a client deck.

---

### 🟢 `P453-C` — A parent-facing `vie scolaire` agent on a closed national SIS (EMEA / France)

🔵 **The shape.** There is no French LMS to integrate: ÉcoleDirecte holds the record and publishes
no open core, so the connector *is* the platform decision.

| layer | component | grant | why this one |
|---|---|---|---|
| SIS connector | [`androz2091/node-ecole-directe`](https://github.com/androz2091/node-ecole-directe) | 🟢 **Apache-2.0** · 11 357 B `c71d239df917` | 🟢 the **only** build-on client of the three: Élève + Famille auth, `notes`, `devoirs`, `emplois du temps`, `vie scolaire` |
| 🔴 rejected | [`papillonapp/papillon-ed-core`](https://github.com/papillonapp/papillon-ed-core) | 🔴 GPL-3.0 · 35 149 B | strong copyleft propagates into the deliverable |
| 🔴 rejected | [`louislegrain/api-ecoledirecte`](https://github.com/louislegrain/api-ecoledirecte) | 🔴 ISC declared, **no payload** | `Gap 451-C` manifest-only: nothing serves the grant's text |
| parent persona | the `p388` parent/guardian tier already on `agents/top.md` | — | the persona is shelved; only the French record was missing |
| grading | 🔴 **not the LLM** — keep marks as retrieved fields | — | Pattern BC's split-clock rule: Reg. (EU) 2026/1744 Art. 50 is live since 2026-08-02 |

🔴 **The licence step is mandatory here and is the pattern's actual lesson.** npm declares
`node-ecole-directe` as `ISC`; the repository serves **Apache-2.0**. 🟢 Build under **Apache-2.0**
— it is the more obligated reading (retain `NOTICE`, mark modified files) *and* the one that
actually governs, and it adds the patent grant `ISC` does not have. 🔵 A team that trusted the
badge would under-comply on attribution while believing it had fewer obligations.

🟡 **Scope honestly.** ÉcoleDirecte's API is undocumented and unversioned; all three clients track
it by observation. Budget for breakage on the vendor's schedule, and treat `vie scolaire` writes as
out of scope — `p448` measured that 136 of 414 connector tool declarations mutate, and a wrong
write here lands on a child's disciplinary record.

## 🆕 `p452` — **Two recipes, both built only from grants read first-hand this pass. 🟢 `P452-A` is a licence-assurance gate that encodes the one thing this pass proved — that registry corroboration works for npm and fails for PyPI — so an engagement stops treating "it's on a registry" as uniform evidence. 🟢 `P452-B` is an EMEA/Maghreb vocational-training engagement that is buildable because the institution registry finally exists.**

🔴 **`make hooks` DENIED** (`Code from External`) — seventh denial in eight passes. Nothing here is
gate-attested; the four load-bearing contracts were re-implemented by hand and all four are green.

---

### 🟢 `P452-A` — **Dependency licence assurance that knows which half of the tree it can corroborate**

🔴 **The problem it solves, measured not assumed.** `p451` made a rule standing: a registry record is
evidence for a repository only when its own metadata **back-links that exact `owner/repo`**. 🟢 This
pass swept all **71** carried registry-sourced cells and found **0** mis-attributions — but **8 that
cannot be corroborated at all**, and the mechanism is ecosystem-specific: **4 of 6 `ABSENT` plus the
only `PAGES_ONLY` are PyPI**. 🔴 So a single uniform "check the registry" step silently passes the
Node tier and silently produces nothing for the Python tier.

**Wiring, concrete:**

1. 🟢 **Back-link resolver** — [`compose/code/p452-backlink-sweep/sweep.py`](code/p452-backlink-sweep/sweep.py),
   as built and run this pass. For each dependency it reads `registry.npmjs.org/{pkg}`,
   `pypi.org/pypi/{pkg}/json` or `packagist.org/packages/{v}/{p}.json` and emits
   `AGREE` / `DISAGREE` / `FOREIGN_FORGE` / `PAGES_ONLY` / `ABSENT` / `NO_RECORD`.
   🔴 Two defects this pass had to fix in it are load-bearing and must not be reintroduced:
   the normaliser must be **forge-qualified** (a `github.com`-only matcher called PyPI `travo`'s
   exact GitLab back-link `ABSENT`), and a **GitHub Pages** URL must grade `PAGES_ONLY`, never as a
   back-link — `rusticisoftware.github.io/TinCanPython/` matches a naive `grep -i github` and is
   not evidence.
2. 🔴 **Ecosystem routing, which is the whole point.** `AGREE` on npm → accept the registry licence
   as corroboration. **Any PyPI dependency → go straight to the payload**, because the expected
   outcome is `ABSENT`. Payload read is `curl -w '%{size_download}'` against
   `raw.githubusercontent.com/{slug}/HEAD/LICENSE`, recording **bytes + `sha256₁₂`** — never shell
   command substitution, which strips the trailing newline and reads one byte low (`p450`; 11 such
   cells found on these shelves this pass).
3. 🔴 **Hard-fail list, each with a live instance from these shelves:**
   `SEE LICENSE IN LICENSE` → **not a licence, a pointer out of the registry**
   (npm `@geoalgeria/formation-professionnelle`, `@incproctor/proctoring-sdk`; and
   `ale-alejandro/beadkit`, where the repository was withdrawn and **no party can now produce the
   grant** — `Gap 451-C`). No licence field at all → `@imazhar101/mcp-canvas-server` `2.1.3`, which
   registers **227 tools of which 61 are undocumented writes** to an LMS. Version-split grants →
   `dev-cucei-itrans/siiau-api-client`, **`proprietary` on 4 of 7 versions**, so a `^1.0`
   constraint resolves *into* the proprietary band.
4. 🟢 **Store the payload at approval time.** The `geoalgeria` case is the argument: a
   `SEE LICENSE IN LICENSE` grant is recoverable **only while its repository lives**, with no notice
   and no archival copy when it is withdrawn.

🟢 **Stack:** `sweep.py` + `curl` + the repo's own CI. 🟡 **Effort:** 1–2 weeks to wire into a
pipeline. 🔵 **What it buys:** the Python half of an education stack stops being certified by a
check that structurally cannot certify it.

---

### 🟢 `P452-B` — **EMEA / Maghreb vocational-training engagement, keyed on a registry that now exists**

🔴 **Why this was not buildable before this pass.** This base could answer *"what runs a school"* —
eight platforms on [`verticals/solutions.md`](../verticals/solutions.md) — and could not answer
*"which schools exist"* for any region. 🔴 A ministry or group engagement sizes and segments the
estate **before** it picks a platform, so the missing layer was the first one needed.

**Wiring, concrete, every grant read first-hand at `HEAD` this pass or carried with a byte-exact
re-read:**

| layer | component | grant |
|---|---|---|
| 🟢 **Institution registry** *(the join key)* | [`yasserstudio/geoalgeria`](https://github.com/yasserstudio/geoalgeria) — **1 932** vocational establishments (856 CFPA, 182 INSFP, 723 private accredited, 58 DFEPs) from **MFEP / takwin.dz**, **177** MESRS higher-ed, **11 858** schools, **69** wilayas, GPS + capacity + boarding, EN/FR/AR | 🟢 **MIT**, `LICENSE` 1 101 B `sha256₁₂ 691e4ec845d7` |
| 🟡 **Delivery platform** | [`moodle/moodle`](https://github.com/moodle/moodle) — the Maghreb's installed base | 🔴 **GPL-3.0**, `COPYING.txt` 35 147 B *(re-read EXACT this pass)* — **link, don't absorb** |
| 🟢 **Agent access layer** | [`FiredMosquito831/ase-moodle-mcp`](https://github.com/FiredMosquito831/ase-moodle-mcp) — courses, assignments, grades, deadlines; the pattern proven at ASE Bucharest, i.e. **single-institution and permissive** | 🟢 **Apache-2.0**, `LICENSE` 11 358 B `sha256₁₂ cfc7749b96f6` *(re-read EXACT)* |
| 🟢 **Read-only student surface** | [`tcpassos/moodle-student-mcp`](https://github.com/tcpassos/moodle-student-mcp) — official mobile-app web service, **nothing is ever changed on Moodle**, SSO + MFA | 🟢 **MIT**, `LICENSE` 1 069 B `sha256₁₂ 322307ac9d65` |
| 🟢 **Offline tier** *(non-negotiable here)* | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT**, `LICENSE` 1 097 B *(re-read EXACT this pass)* |
| 🟢 **Session-to-documentation** | [`D4vRAM369/pbl-project-chronicler`](https://github.com/D4vRAM369/pbl-project-chronicler) — turns CFPA workshop sessions into reproducible step-by-step records; **French/Arabic instructor cohorts need the translated README path, which exists** | 🟢 **MIT**, `LICENSE` 1 066 B `sha256₁₂ 95576ceceaa3` |

**Sequence:** segment the 1 932 establishments by wilaya, type and capacity from the registry → phase
the rollout territorially against GPS and boarding capacity → stand up Moodle per establishment group
with Kolibri for low-connectivity wilayas → put `ase-moodle-mcp` on the instructor side and
`tcpassos/moodle-student-mcp` on the student side (read-only by construction, so it clears a review
that a write-capable connector does not) → chronicler on practical workshops.

🟡 **Effort:** 10–12 weeks. 🟢 **Licence posture:** the deliverable's own code sits on MIT/Apache-2.0
and only **links** the GPL-3.0 platform.

🔴 **Four cautions, stated so the recipe is not over-sold.** (1) The registry is **data, not
software** — no API, no auth, no runtime. (2) Its three tiers do **not** carry equal authority: the
vocational and higher-education tiers are ministry-sourced (MFEP, MESRS), the **11 858** schools
figure is **OpenStreetMap-derived** and is a volunteer-mapped count, not a census — they must never
be cited as one number. (3) `@geoalgeria/*` declares `SEE LICENSE IN LICENSE` on npm, so
**`P452-A` step 4 applies to this very pattern**: store the payload. (4) 🔴 **One country.** This
pattern is Algeria-specific; the rest of the Maghreb, the Gulf and sub-Saharan Africa have **no
registry asset on these shelves** (`Gap 452-E`), and nothing here should be sold as regional
coverage.

## 🆕 Pattern BD — `p451` **Grant recovery for a withdrawn dependency: how to keep shipping when the repository behind a component disappears, and how to know within one hour whether you can**

🔵 **Why this pattern.** Six addresses on these shelves were withdrawn from GitHub while their
published artifacts stayed installable. 🔴 An engagement discovers this the way `p450` did — a
`404` in CI or an audit — and the question it then has to answer is not *"is it still
installable?"* (it is) but **"do we have a grant, and can we prove it?"** 🟢 This pattern is the
measured procedure, built from the nine resolutions this pass made, and it runs in under an hour.

### 🟢 Step 1 — Establish that your probe can fail, before you trust any negative

🔴 **Do not skip this**: two instruments were caught constant-across-domain on this host, and a
third was caught on a wrong path **in this pass's own code**.

```bash
# both controls are mandatory: a live address AND a fabricated one
for slug in moodle/moodle globant-fabricated-451/does-not-exist; do
  curl -sS -o /dev/null -w "$slug raw=%{http_code}\n" \
    "https://raw.githubusercontent.com/$slug/HEAD/README.md"
  git ls-remote "https://github.com/$slug" >/dev/null 2>&1 \
    && echo "$slug lsremote=OK" || echo "$slug lsremote=FAIL"
done
# expect: moodle 200/OK, fabricated 404/FAIL.  Equal results = the probe is zero bits, STOP.
```

🔴 **Known-bad instruments on this host, each measured:** `curl -sI github.com/{slug}` → `403`
for live, dead and fabricated alike (`p450`); authenticated **GitHub MCP** `get_file_contents` →
identical access-denied for `HKUDS/DeepTutor` and for a fabricated slug (`p451`);
`repo.packagist.org/packages/{v}.json` → `404` **for `laravel/framework`** (`p451`, caught by the
positive control). 🟢 The working paths are `raw.githubusercontent`, `git ls-remote`,
`registry.npmjs.org`, `pypi.org` and **`packagist.org/packages/{v}.json`**.

### 🟢 Step 2 — Go to the registry the component actually ships on, and read the BACK-LINK

```bash
# npm — note that the scoped name may differ from the bare one:
#   thanh01pmt/interactive-quiz-kit publishes as @thanh01.pmt/interactive-quiz-kit
curl -sS "https://registry.npmjs.org/$(printf %s "@thanh01.pmt/interactive-quiz-kit" | sed 's|/|%2f|')" \
  | python3 -I -c 'import json,sys; d=json.load(sys.stdin); v=d["dist-tags"]["latest"]; m=d["versions"][v]; print(v, m.get("license"), m.get("repository",{}).get("url"))'

# PyPI — project_urls is where the back-link lives
curl -sS "https://pypi.org/pypi/unist-blackboard-mcp/json" \
  | python3 -I -c 'import json,sys; i=json.load(sys.stdin)["info"]; print(i["version"], i.get("license"), i.get("project_urls"))'

# Packagist — per-VERSION licences, which is the field that caught siiau-api-client
curl -sS "https://packagist.org/packages/dev-cucei-itrans/siiau-api-client.json" \
  | python3 -I -c 'import json,sys; p=json.load(sys.stdin)["package"]; print(p["repository"], p.get("abandoned")); [print(k, (v.get("time") or "")[:10], v.get("license")) for k,v in sorted(p["versions"].items())]'
```

🔴 **Accept the record as evidence for your address only if the back-link is that exact
`owner/repo`.** On this base's own nine, **2 of the 3 name-hits belonged to a third party** —
`blackboard-mcp` is `felipedias-ie`'s live MIT server, `autograder` is held twice by two unrelated
parties, one of them **GPL-3.0**. Taking the name would have written somebody else's licence onto
your dependency.

### 🟢 Step 3 — Classify what you got, because it decides the engagement, not just the ticket

| what the registry gave you | what you may do | worked example from these shelves |
|---|---|---|
| 🟢 SPDX identifier + matching back-link | 🟢 **Ship.** Vendor the tarball, record the registry JSON as grant evidence, pin exactly | `@thanh01.pmt/interactive-quiz-kit` **MIT** `1.4.10` · PyPI `unist-blackboard-mcp` **MIT** `0.2.0` · npm `rhizome-lms-mcp` **MIT** `0.3.1` |
| 🟡 identifier in the manifest, **no payload** ever shipped | 🟡 **Ship only with legal sign-off** — there is a declaration but no licence text to attach | `@santillana-ai/create-tutor-app` (MIT manifest, tarball carries `README` + templates only) |
| 🔴 identifier **changes across versions** | 🔴 **Pin above the boundary and prove it** | `siiau-api-client`: `proprietary` on `v1.0.0-BETA`…`v1.1.1`, **`BSD-3-Clause` from `v1.1.2`** → constrain `>=1.1.2`, never `^1.0` |
| 🔴 declaration points at a file nobody can serve | 🔴 **Do not ship. Replace the component.** | `beadkit`: npm says `SEE LICENSE IN LICENSE`; that `LICENSE` was in the deleted repo, so **no party on earth can now produce the grant** |
| 🔴 no trace on npm, PyPI **or** Packagist | 🟡 **Unresolved — not "unlicensed".** Treat as a build-or-replace decision; do not write a licence cell | `AI-Matrix-Engine/aidream` |

### 🟢 Step 4 — Replace, with named substitutes from these shelves

🔵 Withdrawal is usually not fatal to the *capability*, only to the address. For the tiers hit this
pass there are live, first-hand-verified replacements:

- **Blackboard** → [`felipedias-ie/blackboard-mcp`](https://github.com/felipedias-ie/blackboard-mcp)
  — **MIT**, `LICENSE` 1 084 B, Ultra courses/content/files/grades/deadlines over the user's own
  browser session (replaces both withdrawn Blackboard addresses).
- **Moodle, student-side** → [`tcpassos/moodle-student-mcp`](https://github.com/tcpassos/moodle-student-mcp)
  — **MIT**, `LICENSE` 1 069 B `sha256₁₂ 322307ac9d65`, official mobile-app web service,
  read-only by construction, SSO + MFA.
- **Moodle, single-institution (EMEA)** → [`FiredMosquito831/ase-moodle-mcp`](https://github.com/FiredMosquito831/ase-moodle-mcp)
  — **Apache-2.0**, `LICENSE` 11 358 B `sha256₁₂ cfc7749b96f6`, BL@ASE / `online.ase.ro`,
  Python 3.10+, CI present.
- **Quiz/assessment authoring** → `@openhpi/quiz-recap` (**MIT**,
  [`christophblessing/quiz-recap`](https://github.com/christophblessing/quiz-recap), 35 versions)
  for the recap surface; 🔴 do **not** reach for `@thanh01.pmt/curriculum-kit` as a replacement
  despite being live and MIT — it declares **no `repository` field**, so there is no address to
  audit (`p280`'s unattributable class).

### 🔴 Step 5 — Make the recovery durable, or you will repeat it next quarter

🟢 **Vendor, do not reference.** Commit the tarball (or a lockfile with integrity hashes) **and**
the registry JSON that carried the back-link and licence, into your own repository. 🔴 The
registry record is the single point of failure once the repository is gone — `beadkit` shows what
remains when the second channel goes too: an installable package with an unknowable grant. 🔵 The
dependency-closure pass still applies on top (`compose/code/dependency-licence-closure`): a
permissive root does not clear the tree (`Trend 40`).

---

## 🆕 Pattern BC — `p450` **The split-clock EU tutor: ship the Article 50 obligations that are live NOW, and isolate the Annex III surface so December 2027 is a conformity deliverable instead of a rewrite — every component's grant and ref read first-hand this pass**

🔵 **Why this pattern and not another "AI tutor" recipe.** `Reg. (EU) 2026/1744` split the EU
compliance clock in two, and no pattern on these shelves is built around the split: **Article 50
transparency has applied since 2 Aug 2026** (machine-readable marking transitional to **2 Dec
2026**), while **Annex III high-risk obligations — learner evaluation, programme assignment,
proctoring, access to qualifications — do not bite until 2 Dec 2027**. 🔴 **A build that treats
those as one deadline gets it wrong in both directions**: it ships non-compliant disclosure today,
and it over-engineers conformity work a year early. This pattern makes the split a boundary in the
code.

### 🟢 Components — grant, ref and size re-read first-hand 2026-10-26 (`evidence/licence-title-anchored.2026-10-26-p450.tsv`)

| role | component | 🟢 grant *(verified this pass)* | ref | why this one |
|---|---|---|---|---|
| Tutor / dialogue agent | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · `LICENSE` 11 408 B | `main` | permissive, so the deliverable is vendorable; the one agent-native tutor on these shelves |
| Courseware generation | [satvik314/educhain](https://github.com/satvik314/educhain) | 🟢 **MIT** · `LICENSE` 1 092 B | `main` | generates the artefacts that Art. 50(2) marking must attach to |
| 🔴 **Mastery / grading decision** | [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) + [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | 🟢 **MIT** · 1 132 B / 1 105 B | `main` | 🔴 **the Annex III surface, and it is deliberately NOT an LLM** — Bayesian Knowledge Tracing is deterministic, inspectable and reproducible |
| LMS launch seam | [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) *(py)* or [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) *(php)* | 🟢 **MIT** 1 070 B / 🟢 **Apache-2.0** 11 343 B | `master` / `main` | LTI 1.3 launch keeps the platform at arm's length — **this is the licence seam** |
| LMS read/write connector | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) · [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | 🟢 **MIT** · 1 071 B / 1 070 B | `main` | the write tier `Gap 447-B` confirmed: `create_course`, `update-syllabus`, publish toggles |
| Interactive content | [edly-io/h5pxblock](https://github.com/edly-io/h5pxblock) | 🟢 **MIT** · `LICENSE` 1 064 B | `master` | 🔴 **loads H5P as runtime content** — never link [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library), **GPL-3.0, 35 146 B** |
| Platform tier *(behind the seam)* | [moodle/moodle](https://github.com/moodle/moodle) **GPL-3.0** 35 147 B · [openedx/edx-platform](https://github.com/openedx/edx-platform) **AGPL-3.0** 35 136 B · [overhangio/tutor](https://github.com/overhangio/tutor) **AGPL-3.0** 34 523 B | 🔴 copyleft | `main` / `master` / 🔴 **`release`** | 🔴 **deployed, never forked into the deliverable** |

### 🟢 Wiring — six steps, and the two boundaries are the whole point

1. **Launch** — the LMS launches the tutor over **LTI 1.3** (`pylti1.3`). 🟢 **Boundary 1, the
   licence seam:** the tutor runs as a separate service reached by signed launch, so Moodle's
   GPL-3.0 and Open edX's AGPL-3.0 never reach the Apache/MIT deliverable. Forking the platform
   would pull copyleft into the client's product; AGPL would reach their *hosted* use.
2. **Disclose, at the first token** — a disclosure interceptor in front of DeepTutor emits the
   Art. 50(1) notice that the learner is interacting with an AI system. 🔴 **Due now, not 2027.**
3. **Generate and mark** — `educhain` produces explanations, quizzes and course outlines; every
   artefact is written with **machine-readable provenance marking** at the moment of generation
   (Art. 50(2)). 🔴 **For content already in a client's library before 2 Aug 2026 the transitional
   deadline is 2 Dec 2026** — a backfill job, and it is the nearest deadline in this pattern.
4. 🔴 **Route every grade-affecting decision to `pyBKT`, never to the model.** The LLM may explain,
   hint, rephrase and tutor; **mastery state, item selection and any score come from BKT over
   OATutor's item bank.** 🟢 **Boundary 2, the Annex III surface:** it is deterministic, replayable
   from the event log, and defensible without interpreting a model.
5. **Human in the loop on the high-stakes path** — a grade, placement or progression
   recommendation is surfaced to an instructor and **never written back as the sole basis for a
   decision**. Write-back uses the MCP connector's authoring tools, **gated on the tool's
   EFFECT, never on `read_only_hint`** (`Gap 448-B`).
6. **Content** — H5P activities render through `h5pxblock` as runtime content, keeping the GPL-3.0
   PHP library out of the link graph.

### 🟢 What step 4 and 5 buy outside the EU — the same boundary satisfies three more regimes

| region | requirement | satisfied by |
|---|---|---|
| **North America** | Oklahoma and Maryland require human oversight and bar AI as the basis of high-stakes student decisions; Charleston County's Jan-2026 policy bars AI as the **sole** basis for discipline, placement and special-education determinations | 🟢 steps **4 + 5**, unchanged |
| **APAC** | 🔴 **Vietnam is the only APAC jurisdiction naming education in its high-risk list** (automated assessment, behavioural monitoring) — and much of it binds only where output is *the sole basis without meaningful human review* | 🟢 step **5** keeps the product outside the binding case |
| **LATAM** | UNESCO IESALC: **87 % adoption, 26 % with any formal AI strategy** — the gap is governance, not capability | 🟢 the event log from step **4** *is* the governance artefact an institution cannot otherwise produce |

🔵 **So the pattern is one build with four regulatory readings**, which is what makes it sellable
beyond a single geography — and the regional cells behind it are **relayed, not first-hand**:
`eur-lex.europa.eu`, `digital-strategy.ec.europa.eu` and `www.unesco.org` are all **403 at CONNECT**
from this host class (`Gap 446-D`, sixteen hosts). 🔴 **A client-facing version of this pattern must
re-read the Official Journal text directly.**

### 🟢 Build gate — wire this pass's probe into CI, because the alternative is shipping a dead address

```bash
# Two-stage reachability + authoritative grant read. Stage 2 is not optional:
# 1 in 20 live addresses on these shelves serves no HEAD/README.md.
probe() {  # $1 = owner/repo
  code=$(curl -s -o /dev/null -w '%{http_code}' "https://raw.githubusercontent.com/$1/HEAD/README.md")
  [ "$code" = 200 ] && { echo "$1 LIVE"; return 0; }
  GIT_TERMINAL_PROMPT=0 git ls-remote --heads "https://github.com/$1" >/dev/null 2>&1 \
    && echo "$1 LIVE (no HEAD/README.md)" || { echo "$1 UNREACHABLE"; return 1; }
}
grant() {  # length is a property of the TRANSFER, never of a shell-captured string
  for p in LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt; do
    read -r c n < <(curl -s -o /tmp/g -w '%{http_code} %{size_download}' \
                      "https://raw.githubusercontent.com/$1/HEAD/$p")
    [ "$c" = 200 ] || continue
    # family from the TITLE (first 6 non-blank lines): GPLv3's closing paragraph
    # recommends the LGPL, so a whole-body grep misreads every GPLv3 file.
    grep -v '^[[:space:]]*$' /tmp/g | head -6 | grep -qi 'LESSER' && f=LGPL \
      || grep -v '^[[:space:]]*$' /tmp/g | head -6 | grep -qi 'AFFERO' && f=AGPL \
      || f=$(grep -v '^[[:space:]]*$' /tmp/g | head -6 | grep -oiE 'apache|mit|general public' | head -1)
    echo "$1 $p $f ${n}B"; return 0
  done; echo "$1 NO-GRANT-AT-5-PATHS"; return 1
}
```

🔴 **Fail the build on `UNREACHABLE` or on a copyleft family appearing in the link graph** — the
two failures this pass found on the shelves themselves: nine unreachable addresses, and one
platform graded `🟢 MIT` in one table and `🟡 GPL-3.0` in another table of the same file.

🔵 **Effort, in the shape these shelves use:** 🟢 **steps 1–3 + 6, 4–5 weeks** (launch seam,
disclosure, marking, H5P) — this is the Art. 50 deliverable and it is due now. 🟢 **Steps 4–5,
4–6 weeks** (BKT mastery, item bank, instructor review, effect-keyed write-back). 🟡 **Annex III
conformity packaging — assessment, human-oversight documentation, post-market monitoring —
scheduled against 2 Dec 2027, not now**, which is the saving the split clock pays for.

🔴 **What this pattern does not do.** It does not make an LLM safe to grade with; it removes the
LLM from grading. It does not cover proctoring or behavioural monitoring — both are Annex III and
Vietnam high-risk, and nothing permissive on these shelves does them defensibly. And it inherits
`Trend 40`: **Apache-2.0 at the root does not clear the dependency tree**, so a dependency-closure
pass (`compose/code/dependency-licence-closure`) is a prerequisite to shipping, not a follow-up.
## 🆕 Pattern BB — `p449` **The effect-keyed courseware-authoring gateway — the first pattern on these shelves that can be wired from a MEASURED write surface rather than an advertised one, plus the two-control verification pre-flight that `Gap 449-A` makes mandatory**

🟢 **Gate posture (`Gap 446-A`): `make hooks` RAN** — fourth trial after three denials; that
gap's settlement is **refuted**, the denial is **intermittent**. 🟢 Arrival **58/62 green,
4 RED**, 🔴 two new and both `p448`'s; three green on exit.

### Why this pattern is now buildable, and what changed under it

🔴 `Pattern AZ` and the patterns before it assumed the community LMS-connector tier was
**read-only** — `p447` carried that claim explicitly. 🟢 `p448` refuted it from source; 🟢 `p449`
corrects the magnitude **upward**: the category write share is **35.8 %** (136/**380**), not
32.9 %, because `p448`'s denominator counted 19 non-tool `name:` fields while its **WRITE
numerator of 62 was EXACT** against the README's own declaration. 🔵 **An agent layer here can
author and publish courseware** — and therefore must be gated.

### The recipe, named repo by repo

| layer | component | grant | first-hand cell | role |
|---|---|---|---|---|
| system of record | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | 🟢 **Apache-2.0** | `LICENSE.txt` **10 172 B** (reproduced by `p449`) | the only permissive SIS on these shelves; the NA state channel mandates API submission to it |
| LMS seam | [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | `LICENSE.TXT` **11 358 B** (reproduced by `p449`) | component boundary into a copyleft LMS without inheriting its grant |
| authoring tools | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) @ `c740624` | MIT (`LICENSE` 1 070 B) | 🟢 **188** tools, 🔴 **62 WRITE** | `create_course`, `create_module`, `create_module_item`, `create_page`, `create_new_quiz`, `grade_submission`, `enroll_user` |
| publish toggles | [`mdweaver/canvas-mcp`](https://github.com/mdweaver/canvas-mcp) | MIT | 89 tools, 🔴 **41 WRITE (46.1 %)** | `toggle-module-publish` (`src/tools/modules.ts:114`), `update-syllabus`, `post-announcement` |
| bulk grading | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | MIT | 128 tools | `bulk_grade_submissions`, `bulk_update_pages` — 🔴 **and the 55 undeclared-hint tools are exactly these** |
| adaptive core | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** (`LICENSE` 1 066 B) | — | knowledge tracing behind the authoring decisions |

### 🔴 The gateway, and the one rule that makes it safe

```
agent ──▶ mcp-allowlist-gateway ──▶ {canvas-lms-mcp, canvas-mcp, moodle-mcp}
             │
             └── keys on the TOOL'S EFFECT, resolved from source, NEVER on read_only_hint
```

🔴 **Do not key the allowlist on `read_only_hint` (`Gap 448-B`).** Measured over
`vishalsachdev/canvas-mcp`'s 128 declarations: `=True` on **72**, `=False` on **1** — and that
one is `download_course_file`, **a read** — with **55 (43.0 %) undeclared, which are exactly the
mutating tools.** 🟢 Resolve effect the way `p449` resolved `Gap 448-C`: a tool is a WRITE iff
its registry entry's enclosing object literal says so in **source**, not in a hint field.
🔵 Wire the write tier behind a human-in-the-loop approval and an audit trail — **governed
adoption is the sellable unit**, and on a 35.8 % mutating surface it is also the liability line.

### 🟢 The verification pre-flight this pattern must run, with TWO controls

🔴 `Gap 449-A`: `curl -sI https://github.com/<slug>` returns **403 on every real repository** on
this host class while `git clone` of the same address succeeds. Any pre-flight built on it fails
**closed on live rows** and would condemn all ~134 shelved addresses.

```sh
# 1 — sound existence+payload probe (NOT github.com HTML, NOT api.github.com)
curl -s -o /dev/null -w '%{http_code}|%{size_download}' \
     "https://raw.githubusercontent.com/$SLUG/$BRANCH/$LICENSE_PATH"
# 2 — control A, a negative: MUST return 404|14
curl -s -o /dev/null -w '%{http_code}|%{size_download}' \
     "https://raw.githubusercontent.com/zzz-fake-org-p449/zzz-fake-repo/main/LICENSE"
# 3 — control B, case: probe the case the SHELF RECORDED (Gap 449-B)
#     openedx/XBlock -> LICENSE.txt 404 x3, LICENSE.TXT -> 200|11358
```

🔵 **Both controls are load-bearing, and each caught a real false negative this pass.** Control A
distinguishes a dead row from a blocked host; control B stops case normalisation from
manufacturing dead rows. 🟡 **Budget:** one `curl` per row plus two controls per sweep — the
cheapest gate on these shelves, and the only one standing between a live address and a
deletion.

### 🔴 What this pattern does NOT cover, stated rather than implied

🔴 No government or analyst primary is reachable from this host (`Gap 446-D`, **thirteen** hosts,
now citing the proxy's own `connect_rejected` log), so every regulatory constraint this pattern
inherits is **relayed**, not primary. 🔴 Pin recency governs whether the cells above still hold:
`Pattern AZ` as corrected by `p448` gives **≥ 7 days → 97.4 %** survival against **48.9 %**
below, and `bruchris` @ `c740624` is **3 days** old at read time — 🟡 inside the band where
roughly **one pin in five** does not survive 24 h. Re-probe before quoting.

---

## 🆕 Pattern BA — `p448` **The CALIBRATED pin-recency pre-flight — and the correction of `Pattern AZ`, published one pass ago on n = 5, whose threshold was wrong, whose budget line was survivorship-biased, and whose refutation of commit volume had the sign backwards**

🔵 **Why this supersedes `Pattern AZ` rather than extending it.** `AZ` (`p447`) built a
pre-flight on **five** observations — one pinning per repository, i.e. one coin flip each — and
published three claims from it. `Gap 447-C` registered the calibration limit itself. `p448` paid
it: **496 observations across 36 shelved repositories**, and the pattern survives in **direction**
while **two of its three published claims do not**.

### 🟢 The instrument: a retrospective simulation, so the calibration needs no waiting

For each repository, for each offset `d` in 1…14 days, ask what a studio pinning at that moment
would have got, and whether it held 24 h later:

```bash
# one observation: would a pin taken at time T still be HEAD at T+24h?
git clone --quiet --filter=blob:none --no-checkout https://github.com/OWNER/REPO /tmp/r
PIN=$(git -C /tmp/r rev-list -1 --before="$T" HEAD)
NXT=$(git -C /tmp/r rev-list -1 --before="$T +1 day" HEAD)
AGE=$(git -C /tmp/r show -s --format=%cI "$PIN")   # how old was that commit when pinned?
[ "$PIN" = "$NXT" ] && echo HELD || echo STALE
```

🟢 **36 blobless clones → 496 observations, in one pass, with no 24-hour wait.**
🟢 **Validated before use**, against a cell this base already published: `Apomera/AlloFlow`'s
refs date to `2026-10-24T12:35:30-04:00` and `2026-10-25T18:50:44-04:00`, reproducing `p447`'s
*"pinned 10-24 12:35, HEAD 10-25 18:50"* **to the minute**.
🟢 **Pre-condition checked, not assumed:** the method needs committer dates to be monotone along
history. Measured over **9 438** adjacent commit pairs in these 36 repositories: **0
inversions**, **36 of 36** repositories clean.

### 🟢 The calibration curve — this is the pattern

| age of the commit **at the moment you pin it** | n | 🟢 P(pin still HEAD after 24 h) |
|---|---|---|
| < 1 h | 33 | 🔴 **6.1 %** |
| 1–6 h | 35 | 🔴 **20.0 %** |
| 6–24 h | 99 | 🔴 **35.4 %** |
| 1–3 d | 81 | 🟡 **71.6 %** |
| 3–7 d | 59 | 🟡 **81.4 %** |
| **7–30 d** | 100 | 🟢 **98.0 %** |
| > 30 d | 89 | 🟢 **96.6 %** |

🔴 **`Pattern AZ`'s threshold was wrong.** `AZ` said **days** → *"settled, the pin will hold,
safe to quote with its date."* At **1–3 days the pin fails 28 % of the time.** The operating
point that earns the word "settled" is **seven days**:

| rule | n above threshold | P(held) |
|---|---|---|
| 🟢 **age at pin ≥ 7 d** | 189 | 🟢 **97.4 %** |
| 🔴 age at pin < 7 d | 307 | 🔴 **48.9 %** |

🔴 **`AZ`'s biconditional was an artefact of n = 5.** It published that
`pinned_commit_date == HEAD-date` **iff** the pin held, *"in every row"*. Over the proper
denominator the biconditional **fails in 44 of the 167** observations with age < 24 h. As a
classifier, `AZ`'s 24-hour rule scores precision **73.7 %**, recall **75.9 %**, accuracy
**83.3 %** — useful, but a tendency, **not an identity**.

🔴 **`AZ`'s budget line was survivorship-biased, and this is the correction a studio will feel.**
`AZ` told engagements to expect *"17 of 18 pins survive 24 h — a cheap minority repair, not a
re-verification campaign."* Over 496 unbiased pinnings: **67.3 % survive. A third of pins die
within 24 hours.** 🔵 The 18-pin sample was drawn from pins **already carried across passes**,
i.e. already selected for having survived.

### 🔴 And the metric `AZ` told you to stop using is in fact a good one — its refutation had the sign backwards

`AZ` published: *"Do NOT grade staleness by commit volume. It is refuted by measurement"*,
because `DeepTutor` (661 commits/30 d) and `frappe/lms` (571) each held their one pin.

| | `Pattern AZ` (n = 5, one pin each) | 🟢 `p448` (n = 36 repos × 14 pinnings) |
|---|---|---|
| commits/30 d vs 24-h stale rate | 🔴 claimed **negative** ("backwards") | 🟢 **Spearman ρ = +0.886** |

| repository | commits / 30 d | `AZ`'s single pin | 🟢 `p448` stale rate over 14 pinnings |
|---|---|---|---|
| `HKUDS/DeepTutor` | **661** | 🟢 held | 🔴 **50.0 %** |
| `frappe/lms` | **571** | 🟢 held | 🔴 **71.4 %** |
| `Apomera/AlloFlow` | 417 | 🔴 stale | 🔴 **85.7 %** |
| `vishalsachdev/canvas-mcp` | 373 | 🔴 stale | 🔴 **92.9 %** |
| `withmarbleapp/os-taxonomy` | 126 | 🟢 held | 🟡 **42.9 %** |
| `Citolab/qti-convert-python`, `LongsightGroup/qti3`, `GeovaneSchmitz/sigaa-api`, `ivmelo/suapbot`, `sebassg/sia-unal-mcp`, `r-huijts`/`mdweaver`/`caleb-media-studio` `canvas-mcp` | low | — | 🟢 **0.0 %** |

🔵 **`AZ` graded each repository on one coin flip and read the noise as the signal.** The two
busiest repositories did hold *that* pin; over fourteen pinnings each they are among the worst.

🟢 **And the two predictors are the same predictor.** commits/30 d vs **mean age-at-pin**:
**ρ = −0.852**. The busiest six repositories present HEADs **3.5–41.7 h** old; the quietest six
present HEADs **555 h to 80 196 h** old. 🔵 **Volume is a repo-level proxy; recency is the
mechanism.** Use recency — it is per-pin, it needs no history window, and it is one command.

### 🟢 Wiring it into an engagement

1. **At SOW / shelving time**, for every commit about to be quoted:
   ```bash
   git clone -q --filter=blob:none --no-checkout https://github.com/OWNER/REPO /tmp/pin && \
   git -C /tmp/pin show -s --format='pin=%h pinned_commit_date=%cI' HEAD && date -u +'now=%Y-%m-%dT%H:%M:%SZ'
   ```
2. **Age ≥ 7 days** → 🟢 cite the HEAD with its commit date beside it. **97.4 %** survival.
3. **Age < 7 days** → 🔴 do **not** put the HEAD in the deliverable. Cite the **grant payload
   cell** instead, and let the HEAD appear only as *"tree seen on `<date>`"*:
   ```bash
   curl -sS "https://raw.githubusercontent.com/OWNER/REPO/HEAD/LICENSE" -o /tmp/L && \
   printf '%s B · %s\n' "$(wc -c < /tmp/L)" "$(sha256sum /tmp/L | cut -c1-12)"
   ```
   🟢 **Why the cell is the safe anchor, measured twice:** `AlloFlow` moved
   `6194e51e8f1f` → `1499a80fd362` while its `LICENSE` stayed **35 442 B · `698099632698`** at
   both refs; and `openSIS`'s `docs/License.txt` re-read this pass is **17 286 B ·
   `224ac3d403e3`**, the published cell to the digit. **Trees move; grants do not.**
4. **Budget honestly.** 🔴 Expect **~33 %** of pins to need repair at 24 h, not 6 % — unless
   every pin cleared the 7-day gate, in which case **~3 %**. 🟢 The gate is the cheap half of
   this pattern; re-verification is the expensive half. Spend on the gate.
5. 🔴 **Never** grade staleness from stars or "last updated" badges (`Trend 46`). 🟡 And do not
   grade it from commit volume either — it *works* (ρ = +0.886) but it is a 30-day
   backward-looking window standing in for a number you can read directly off the commit.

🟡 **Calibration limits, stated rather than hidden:** 496 observations, but **36 repositories,
one industry, one host, one 14-day window**, and the 24-hour horizon is the only one measured —
nothing here calibrates a 1-week or 1-quarter pin → `Gap 448-D`.

---

## 🆕 Pattern AZ — `p447` **The pin-recency pre-flight: a 60-second check that tells you whether the commit you are about to put in a client deliverable will still be there on Monday — and why the metric you would reach for first (commit volume) gets it backwards**

🔵 **The problem this solves.** A studio engagement pins commits: in an SOW appendix, a
`requirements.txt`, a vendored submodule, a slide that says *"verified at `abc123`"*. `p446`
established that a pinned HEAD is a **timestamp, not an identity**. `p447` measured how fast
that timestamp rots, and the answer is **uneven in a way that is predictable** — but not by the
obvious metric.

### 🔴 Do NOT grade staleness by commit volume. It is refuted by measurement.

| repository | commits / 30 d | pin after ~24 h |
|---|---|---|
| `HKUDS/DeepTutor` | **661** | 🟢 still exact |
| `frappe/lms` | **571** | 🟢 still exact |
| `Apomera/AlloFlow` | 417 | 🔴 **stale** |
| `vishalsachdev/canvas-mcp` | 371 | 🔴 **stale — third HEAD in 24 h** |
| `withmarbleapp/os-taxonomy` | 126 | 🟢 still exact |

🔴 The **two busiest** repositories have the **most stable** pins. A 30-day count is
**backward-looking**: it counts a burst that has already ended. `DeepTutor` logged 661 commits
and then went quiet for **seven days**.

### 🟢 The check that works, and it is one command

```bash
# Is the commit I am about to pin on a MOVING tree or a SETTLED one?
git clone --quiet --filter=blob:none https://github.com/OWNER/REPO /tmp/pin && \
git -C /tmp/pin show -s --format='pinned_commit_date=%cI' HEAD && date -u +'now=%Y-%m-%dT%H:%M:%SZ'
```

**Read the gap between `pinned_commit_date` and `now`:**

| gap | tree state | what to do |
|---|---|---|
| **minutes–hours** | 🔴 **moving** — you are pinning mid-burst | Do **not** put the HEAD in the deliverable. Pin the **payload cell** instead |
| **days** | 🟢 **settled** | The pin will hold. Safe to quote with its date |

🟢 **Measured basis:** across the five repositories above, `pinned_commit_date == HEAD date`
**iff** the pin held. Both movers were pinned while the project was still committing —
`AlloFlow` pinned 10-24 12:35 with HEAD at 10-25 18:50; `canvas-mcp` pinned 19:41 with HEAD at
**20:06 the same evening**, stale **25 minutes** after the commit it names.

### 🟢 What to pin INSTEAD, when the tree is moving — and the evidence it is sound

Pin the **grant payload cell**, not the HEAD:

```bash
curl -sS "https://raw.githubusercontent.com/OWNER/REPO/HEAD/LICENSE" -o /tmp/L && \
printf '%s B · %s\n' "$(wc -c < /tmp/L)" "$(sha256sum /tmp/L | cut -c1-12)"
```

🟢 **Why this is safe, measured this pass:** `Apomera/AlloFlow` moved
`6194e51e8f1f` → `1499a80fd362`, and its `LICENSE` is **35 442 B · `698099632698`** at **both**
refs — reproducing a cell this base published **fourteen passes ago** at `p433`, to the digit.
🔵 **The tree moved; the grant did not.** A licence verdict anchored on the cell survives
exactly the churn that invalidates a HEAD.

### 🟢 Wiring it into an engagement

1. **At shelving / SOW time** — run the recency check. Record **pin + pinned-commit-date**, never the pin alone.
2. **Moving tree** → the deliverable cites the **payload cell**; the HEAD appears only as *"tree seen on <date>"*.
3. **Settled tree** → cite the HEAD, with its commit date beside it.
4. **Before any client re-read** — re-resolve with `git ls-remote <slug> HEAD`. 🟢 Budget realistically: **17 of 18** of this base's pins survived 24 h, so this is a **cheap minority repair**, not a re-verification campaign.
5. 🔴 **Never** infer staleness from stars, commit counts or "last updated" badges. `Trend 46` showed those channels over-count supply; this pattern shows they get **churn backwards** too.

🟡 **Calibration limit, stated rather than hidden:** the date axis is **n = 5**. The pin/no-pin
split is **n = 18**. Run it over all ~134 shelved repositories before treating the recency rule
as calibrated — `Gap 447-C`.

---

## 🆕 Pattern AY — `p446` **The lineage pre-flight: a 10-minute gate that runs BEFORE you tell a client how many options they have, because `Trend 46` says the shelf over-counts and `Gap 446-B` says the pin you quoted may already be stale**

🔵 **Why this pattern exists.** Two failures this base measured in one hour, both on the question
an engagement asks first:

- 🔴 **Over-count.** Ten Canvas/Moodle MCP addresses are **six** projects. Quoting ten is a
  credibility loss on the second call, when the client's own engineer runs one `git log`.
- 🔴 **Stale pin.** `vishalsachdev/canvas-mcp`'s HEAD advanced **while this base was measuring
  it**, and `krzysztofbury/librus-mcp` is a commit past the pin this base publishes.

🟢 **The pattern is the cheap check that prevents both**, and it needs no GitHub API — which
matters, because `api.github.com`, `github.com/search` and `codeload.github.com` are all **403**
from this base's host.

### 🟢 The recipe — concrete, with the repos and the commands

**Input:** the candidate address list off `agents/top.md` for the client's platform. Worked here
on the real Canvas/Moodle set.

**Step 1 — resolve, don't trust (≈1 s each).**
```
git ls-remote https://github.com/<owner>/<repo> HEAD
```
🔴 A failure here is a finding, not an error: `Gap 444-B`'s `dev-cucei-itrans/siiau-api-client`
is how a deleted repository presents. Record the sha **with the clock time**, because
`Gap 446-B` is a live hazard on an active repository.

**Step 2 — clone blobless and take the root commit (≈1 s each).**
```
git clone --filter=blob:none <url> ./<owner>~<repo>
git -C ./<owner>~<repo> rev-list --max-parents=0 HEAD    # the project identity
git -C ./<owner>~<repo> rev-list --count HEAD            # the maintenance signal
```
🟢 **Group by root commit. That is the option count.** Here: `afe32c3e1721` ×3,
`731aa116052b` ×2, four singletons → **6 projects, 10 addresses**.

**Step 3 — grade direction inside each group, by full history.**
```
git -C <A> remote add other <url-of-B> && git -C <A> fetch --filter=blob:none other
git -C <A> merge-base --is-ancestor <B-head> <A-head>   # 0 = B adds nothing
git -C <A> rev-list --count <B-head>..<A-head>          # how far behind B is
```
🟢 Take the descendant, **whoever owns it**: in ARM-2 the fork `mdweaver/canvas-mcp` is 4 ahead
of the root `r-huijts/canvas-mcp`.

**Step 4 — grade the grant on the payload cell, not the HEAD.**
```
git -C <d> ls-tree -r --name-only HEAD | grep -iE 'licen|copying'   # the WHOLE tree
git -C <d> cat-file -s HEAD:<path>                                   # bytes
git -C <d> cat-file blob HEAD:<path> | sha256sum | cut -c1-12        # the cell
```
🔴 **Enumerate the tree, never just the root** — `krzysztofbury/librus-mcp` is MIT at the root
and ships a complete **GPL-3.0** at `legacy_reference/LICENSE` (35 149 B · `3972dc9744f6`).
🟢 **sha256-first-12 over raw bytes** is this base's cell convention, validated this pass against
a published cell (`1 071 B · 22e7ab2dbddc`).

**Step 5 — read the upstream's own provenance file if it has one.**
🟢 `krzysztofbury/librus-mcp` ships `LICENSE_REVIEW.md` (9 662 B · `6905cca1f0b4`) with a locked
dependency licence inventory and an explicit scope limit: *"not an all-MIT standalone bundle."*
🔴 **That sentence disqualifies the delivery shape a studio defaults to** — one flattened
container or single-file binary — because `lxml`'s binary wheels can carry **LGPL-2.1 iconv**
and resources the upstream describes as unlicensed. Check it **before** the build review.

### 🟢 What it costs, and what it buys

| | |
|---|---|
| **cost** | ~1 s per repository for steps 1–2, a few minutes for a 10-address list; **no API keys, no GitHub API, no rate limit** |
| **buys** | the option count a client can verify; the address to actually take; a grant verdict over the whole tree; and the one sentence that stops a GPL subtree or an LGPL relink arriving in the shipped artefact |
| **when to run** | 🟢 **before the first scoping call**, and again before the build review — `Gap 446-B` means a pin older than an hour is a date, not an identity |

🔵 **Composes with `Pattern AX`** (the per-platform licence probe): `AX` answers *what does this
platform's supply cost*, `AY` answers *how many suppliers are there really, and which one do I
take*. Run `AY` first — it shrinks `AX`'s input set, here from ten addresses to six.


## 🆕 Pattern AX — `p445` **The per-platform licence probe: a two-hour gate that runs BEFORE you quote a system-of-record integration, because `Trend 45` says you cannot carry the last platform's answer to this one**

🔵 **Why this pattern exists.** This base has now published **three incompatible answers** to
*"what licence is the integration supply around an education system of record?"* — permissive
(`Trend 42`, 8 addresses), mostly-unlicensed (`Trend 43`, 37 addresses), uniformly GPL-3.0
(`p445`, 3 addresses on SIGAA). 🟢 **They are not in conflict; they are three platforms.**
`Trend 45`'s operational form is that the licence distribution is a property of the **platform's
developer community**, so it must be measured per platform and carried across neither regions
nor publisher classes. 🔴 **And `Trend 45` also kills the shortcut that was being used instead:**
publisher class does not predict grant presence (institutional 72.2 % against a 76.3 % baseline,
Fisher p = 0.558, n = 3 932), so *"it's a university, it'll be copyleft"* and *"it's official,
it'll be unlicensed"* are both unavailable.

### Step 1 — Get the platform's NAME, not the institution's (30 minutes, a conversation)

🔴 **This is the step that decides whether the pattern works**, and `p444` recorded walking
into the failure one leg after writing the rule down. Searching the **institution's name**
returns the institution's *teaching output*: `UNMSM` returned **884** coursework repositories;
`Ceibal` returned **238**, all coursework. Searching the **system of record's name** returns its
*integration surface*.

Ask the client: *"what system do your registrar and your students actually log into?"* Known
answers, from this base's own legs:

| country | system of record | this base's finding |
|---|---|---|
| Brazil (federal universities) | **SIGAA** | 🟡 supply exists, uniformly **GPL-3.0**, stale — `Pattern AY` |
| Brazil (federal institutes) | **SUAP** | 🔴 official clients **ungranted**; third-party MIT — `Pattern AW` |
| Argentina | **SIU Guaraní** | 🟢 one MCP server (`p443`) |
| Colombia | **SIA** (UNAL) | 🔴 MCP server exists, **NO GRANT** (`sebassg/sia-unal-mcp`) |
| Mexico (UANL) | **SIASE** | 6 addresses (`p444`) |
| Mexico (UdeG) | **SIIAU** | 🔴 **zero supply** — the one SDK's repository is deleted (`p445`) |
| Chile | **UCampus**, **U-Cursos** | 🟡 thin, and the top-starred hit is a **Chinese homonym** (`p444`) |
| Peru | SIAGIE, PUCP *Campus Virtual*, UNI *SIGA* | 🔴 **twice-nil on two channels** (`p444`, `p445`) |

⚠️ **Two traps this base paid for, apply both.** (1) **The homonym:** a 4–6 letter government
acronym is usually owned by an industrial or ML namespace — `SIMAT` returns **Siemens SIMATIC**,
`SAES` returns **sparse autoencoders**, `GURI` returns an oh-my-zsh theme. Check who operates
the platform, and read the top hit's **language**, before trusting a stars-sorted rank.
(2) **Ministry vs university:** university platforms accumulate third-party supply because the
blocked parties are students who can code; ministry-run K-12 systems do not (`p444`: 6 of 8
university legs paid, **0 of 5** ministry legs did).

### Step 2 — Enumerate the grant, do not read the badge (20 minutes, scripted)

```sh
cd compose/code/lib
. ./probe_payload.sh

# Existence + REAL default ref (never assume `main`: measured counter-examples include
# GibbonEdu/core -> v31.0.00, portabilis/i-educar -> 2.12).
git ls-remote --symref https://github.com/<owner>/<repo> HEAD

# EVERY licence path in the COMPLETE tree, each payload measured where it landed.
probe_repo_all <owner>/<repo>
```

🔴 **Use `probe_repo_all`, not the filename ladder, and not the registry.** Three defects this
base has measured, each of which this step closes:
* **The second grant below the root.** `krzysztofbury/librus-mcp` sells MIT at its root and
  ships complete **GPL-3.0** at `legacy_reference/LICENSE` (35 149 B) beside 20+ `.py` files.
  12 of 134 repositories carried more than one own-grant path; **4 carried more than one
  FAMILY** (`p442`).
* **The registry disagreeing with the payload, in the dangerous direction.**
  `macielti/sigaa-cli`'s PyPI `license` field is **EMPTY** while the repository ships a complete
  **GPL-3.0** payload (35 149 B) — so every registry-reading scanner reports a strongly-copyleft
  package as unlicensed (`p445`).
* **The name without the text.** `DMontgomery40/mcp-canvas-lms` says *"MIT License — see
  LICENSE file"* and ships no such file. That is an upstream **ask**, not a refusal, and must not
  be recorded as a bare absence.

### Step 3 — Compute the distribution and pick the shape (40 minutes)

Tabulate the addresses by family, then read the shape straight off it:

| what the distribution looks like | the shape to quote |
|---|---|
| 🟢 majority **MIT / Apache-2.0 / BSD**, maintained | **vendor it** — fork and extend, shortest path |
| 🟡 majority **GPL-3.0 / AGPL-3.0** | 🔴 **never vendor.** Reimplement against the interface these repos document, on a permissive base — the repos are *specification* (`Pattern AY`) |
| 🔴 majority **no grant at all** | **integrate over an interface you own**, use the licensed third-party client, and send a written licence request upstream (`Pattern AW`) |
| 🔴 **zero addresses** (SIIAU) | **price the integration from scratch** — and say so, because this is the case most often mistaken for "we'll find something" |

🟢 **The deliverable of this pattern is one slide:** the platform's name, the address count, the
family distribution with byte sizes and SHA prefixes, and which of the four shapes follows. It
is produced by `probe_repo_all` plus `lib/measure` and costs about two hours.

🔴 **And the rule that makes it worth running every time:** `Trend 45`'s falsifiable half says a
fourth platform should return a **fourth** distribution. Until two platforms in different
countries return the same one, **the previous engagement's answer has no predictive value for
this one.**

---

## 🆕 Pattern AY — `p445` **A Brazilian federal-university engagement on SIGAA, where the integration supply is real, documented, and GPL-3.0 — so the recipe is REIMPLEMENT, and the three repos are the specification**

🔵 **The situation this answers.** A client is a Brazilian federal university — UFPB, UFRN, UFMG
and the rest of the federal network run **SIGAA** (*Sistema Integrado de Gestão de Atividades
Acadêmicas*) as their system of record. `p443` opened this channel and `p445` measured it end to
end: **the supply exists, in two languages, with a working parser and a documented endpoint
shape — and all of it is GPL-3.0 and 6–10 years old.**

| address | grant, read first-hand 2026-10-25 | HEAD | what it gives you |
|---|---|---|---|
| [`fernandobrito/cursos_ufpb`](https://github.com/fernandobrito/cursos_ufpb) | 🟡 GPL-3.0 · 35 141 B · `cbdcf32a9188` | 2017-01-26 · 168 files | the **endpoint shape** (`/api/curricula`) and the `sigaa_parser` logic |
| [`macielti/sigaa-cli`](https://github.com/macielti/sigaa-cli) | 🟡 GPL-3.0 · 35 149 B · `85b9a51f5603` | 2020-01-04 · 25 files | the **auth flow against any SIGAA instance** by configurable base URL |
| [`fernandobrito/ufpb_sigaa_api_old`](https://github.com/fernandobrito/ufpb_sigaa_api_old) | 🟡 GPL-3.0 · 35 141 B · `4fa17f22c442` | 2016-02-07 · 14 files | the reference shape for "SIGAA behind an HTTP API" |

🔴 **Read the licence column before planning:** GPL-3.0 reaches a distributed derivative. These
three are **specification, not supply.** You read them, you do not ship them.

### The stack, every row verified first-hand on 2026-10-25

| layer | component | grant, measured | why this one |
|---|---|---|---|
| **1. SIGAA adapter** | 🔴 **write it** — a clean-room HTTP client over the auth flow and endpoints the three repos above document | 🟢 **yours** | SIGAA is JSF with **no public REST API**, so the adapter is unavoidable work. Reading GPL-3.0 code to learn an *interface* and writing your own client is the standard move; a lawyer signs off on the clean-room boundary, not an engineer |
| **2. MCP wrapper** | the adapter, exposed as an MCP server | 🟢 **yours** | 🟢 This is the step that makes the whole stack agent-addressable, and `p443`/`p444` show it is the shape that is *missing* in LATAM: `siu-guarani-mcp` exists for Argentina, `sia-unal-mcp` for Colombia carries **no grant**, and there is **nothing** for SIGAA. Build it once, reuse across the federal network |
| **3. LMS** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `LICENSE` 10 982 B | 🟢 **The only Apache-2.0 full LMS in this base's platform tier.** Take it when the client cannot accept copyleft; take Moodle (GPL-3.0) only when they can and already run it |
| **4. LMS agent surface** | [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | 🟢 **MIT** · `LICENSE` 1 063 B · Go | Only if the client is on Moodle: courses, grades, assignments, deadlines over MCP, against any instance. 🔴 If on OpenOLAT, this layer is yours too |
| **5. Knowledge tracing** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** · `LICENSE` 1 066 B | The student model that makes layer 6 honest rather than a chatbot. Feed it the attendance and assessment history the layer-1 adapter pulls |
| **6. Tutor** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · `LICENSE` 11 408 B | Agent-native personalised tutoring with persistent per-student state; runs against local models via Ollama, which matters for a public university's data posture |

### Wiring

```
SIGAA (JSF, no public API)
   │  clean-room HTTP adapter  ← specification: the 3 GPL-3.0 repos (READ, never shipped)
   ▼
your SIGAA adapter ──► your MCP server ──┐
                                         ├──► DeepTutor (Apache-2.0)  ──► student
OpenOLAT (Apache-2.0) ──► MCP surface ───┤        ▲
                                         │        │
pykt-toolkit (MIT) ◄── enrolment, grades, attendance from the adapter
```

🟢 **Why the MCP server is the centre of gravity and not the tutor.** Every agent in layers 4–6
is replaceable; the **adapter plus MCP server over the system of record** is the asset, it is
reusable across every institution in the federal network that runs SIGAA, and it is the one
component for which no licensed supply exists anywhere in LATAM. Build it once, licence it as
you choose, and the tutor becomes a swap.

### 🔴 The two gates before any of this is quoted

1. **The access gate (`P26`), which no licence probe can answer.** A grant answers the
   *copyright* question only. *May we call this system?* lives in the university's own terms of
   use and its data-protection posture, and `p444`'s SIIAU and Chile legs both show student-built
   scrapers operating in exactly that grey zone. 🔴 Get written authorisation from the registrar
   before the adapter touches production; a scraper the students tolerate is not a contract the
   university has signed.
2. **Run `Pattern AX` first.** This recipe is correct for **SIGAA**, measured. 🔴 It is not
   transferable to the next platform — that is precisely what `Trend 45` says. One institution's
   SIGAA deployment may also differ in version and endpoints from UFPB's; the adapter is
   per-instance-configurable for that reason.

---

## 🆕 Pattern AW — `p444` **A licence-clean Brazilian Instituto Federal engagement: Moodle + SUAP + an AI layer, wired from rows verified 2026-10-25 — and the gate that stops you shipping the 49 % you cannot use**

🔵 **Why this pattern and not another tutor recipe.** `p443`'s `Pattern AV` answers *"how do you
find the repositories in a country whose supply this base has never shelved"*. `p444` ran that
move at four more countries and found the next problem: **the addresses exist and half of them
carry no licence**, including the officially-published ones. So `Pattern AW` is the step after
discovery — **turn a found tier into a stack you can actually quote** — and it is built on the
one LATAM ecosystem where every layer now has a verified row.

**Target:** an Instituto Federal (Brazil's federal vocational/technical network — SUAP is its
system of record, confirmed reusable across institutions). **Duration: 8–10 weeks.**

### 🔴 Step 0 — the licence gate, BEFORE the estimate

Run this before a single component is named in a proposal. It is not diligence hygiene; on this
tranche it eliminates **49 %** of candidates, so it changes the estimate.

```bash
# 1. every grant path at the probed HEAD, not just the root row  (p442)
compose/code/p1059-latam-name-channel/probe.sh slugs.txt out/
#    -> NO-GRANT-PATH in the `path` column means NO RIGHT OF USE.  Not "permissive by default".

# 2. does the README claim a DIFFERENT grant from the payload?    (p444, Gap 443-C)
python3 compose/code/p1060-readme-vs-payload/compare.py out/
#    -> README-MORE-PERMISSIVE is the expensive verdict: ipti/br.tag says BSD-3-Clause
#       in its `## Licença` section and ships GNU GPL v2.
```

🔴 **Two gate outputs are disqualifying, not negotiable:** `NO-GRANT-PATH` (no grant exists) and
`README-MORE-PERMISSIVE` (the grant you were told about is not the grant you get). 🟡 A third,
`NO-PAYLOAD` with a live claim, means *a licence was stated and never made* — treat as
disqualifying until the author fixes it, and see Step 4.

### 🟢 Step 1 — the system of record: integrate, do not fork

| layer | row | grant, read first-hand | why this one |
|---|---|---|---|
| system of record | **SUAP** · `suap.ifrn.edu.br` | 🔴 **source not published** | Holds enrolment, grades, attendance, materials. 🔴 **Not forkable** — the only access is its documented **OAuth2** API. Budget zero hosting and zero platform-licence risk; budget *total* API dependency. |
| 🟢 **authentication** | [`django-auth-suap`](https://github.com/django-by-kelsoncm/django-auth-suap) | 🟢 **MIT** · `LICENSE.md` 1 065 B · `113d1a85e628` · HEAD **2026-09-05** | 🟢 **The keystone row.** Django OAuth2 backend for SUAP: 98 `.py`, 92 `.rst` of Sphinx docs, on **PyPI** as `django-suap-auth`, CI + Codecov + pre-commit + `SECURITY.md`, Django **5.2/6.0**, with an `audit/` submodule (middleware, migrations, `audit_archive` command). |
| read seam (PHP) | [`ivmelo/suap-api-php`](https://github.com/ivmelo/suap-api-php) | 🟢 **MIT** · 1 071 B · `8dd4b842ad4d` | 34 ★, the most-starred *licensed* SUAP address. 🔴 HEAD 2021-04-13 — read it as the worked example of the API shape, re-implement against current endpoints. |
| read seam (Ruby) | [`luizpicolo/suap_api`](https://github.com/luizpicolo/suap_api) | 🟢 **MIT** · 1 078 B · `798df9e7634a` | 🔵 Written against **IFMS**, not IFRN — **this row is the evidence that a SUAP integration is reusable across institutes**, which is what makes the engagement repeatable rather than bespoke. |

🔴 **Do NOT use, and say so in the proposal:** [`IFRN/suapi`](https://github.com/IFRN/suapi)
(29 ★), [`ifrn-oficial/cliente_suap_django`](https://github.com/ifrn-oficial/cliente_suap_django)
(29 ★), [`ifrn-oficial/cliente_suap_javascript`](https://github.com/ifrn-oficial/cliente_suap_javascript)
(23 ★). **81 ★ of official, institutionally-maintained OAuth2 client, and not one carries a
grant file** — verified path-by-path this hour. They are the obvious choice and they are the
unusable one (`Trend 44`).

### 🟢 Step 2 — the LMS seam, where GPL-3.0 is the right answer

| layer | row | grant | why |
|---|---|---|---|
| LMS | **Moodle** | GPL-3.0 | Already this base's anchor LMS row; the *AVA* in Instituto Federal usage. |
| 🟢 **LMS↔SIS bridge** | [`moodle-local_suap`](https://github.com/suap-ava-suite/moodle-local_suap) | 🟡 **GPL-3.0** · `LICENSE` 35 161 B · `54b00c9ffd02` · HEAD **2026-10-19** | 🟢 **Live, 94 files, and it is the seam this base could previously only describe for EMEA.** GPL-3.0 here is **coherent, not a cost**: it is a Moodle `local` plugin and Moodle is already GPL-3.0, so the obligation is one the host platform imposes anyway. |

🔵 **The licence boundary of the whole stack, stated plainly:** everything *inside* Moodle is
GPL-3.0 and that is unavoidable and fine; everything on the **service side** (auth, API clients,
the AI layer) is MIT and stays separable. Keep the Moodle plugin a plugin — do not let
GPL-3.0 code cross into the service, and the boundary holds.

### 🟢 Step 3 — the AI layer, from rows already on these shelves

| role | row | grant | wiring |
|---|---|---|---|
| teacher-facing generation | [`GuilhermeScarpini/agente-bncc-professores`](https://github.com/GuilhermeScarpini/agente-bncc-professores) | 🟢 **MIT** | 🟢 **Brazilian curriculum-native**: lesson plans and assessments anchored to **BNCC** codes with a hallucination gate in the product. Feed it the class/subject identifiers that `django-auth-suap` + the SUAP API already resolve. |
| student-facing tutoring | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · `LICENSE` 11 408 B · `cd2f54e1e506` | Agent-native tutoring with persistent learner memory; scope it to the enrolled-subject list from SUAP so it never answers outside the student's actual courses. |
| offline / low-connectivity delivery | **Kolibri** | 🟢 **MIT** · 1 097 B · `3c056b34a476` | Offline-first with local models via Ollama — the row for *campi* and rural extension sites without reliable connectivity. |

🔴 **The EU AI Act scoping gate (`Pattern AP`) still applies even though this is Brazil**, the
moment the institution has European partners or EU-resident students: anything that profiles a
learner — and knowledge tracing does so by construction — cannot use the **Article 6(3)**
exception, and the Annex III deadline is **2 December 2027** (`Regulation (EU) 2026/1744`), while
the **AI-literacy and transparency duties are not deferred at all**.

### 🟢 Step 4 — the one-hour move nobody on this base has tried

🔴 18 of 37 addresses in this tranche are unusable only because nobody chose a licence — among
them an **MCP server** for a Colombian national university (`sebassg/sia-unal-mcp`, live,
TypeScript) and the three IFRN clients above. 🟢 **Open one issue per address asking the author
to add a licence.** It costs an hour, it is the cheapest possible supply expansion, and
`Gap 444-C` exists because no pass here has ever measured whether it works. 🔵 For an
institution-published repository, route it through the institution's open-source or IT
governance contact rather than the GitHub issue tracker — nobody *owns* the licence decision on
`IFRN/suapi`, which is exactly why it has none.

### 🔵 Weeks

| weeks | work |
|---|---|
| 1 | 🔴 **Step 0 gate** over every candidate; disqualify on `NO-GRANT-PATH` / `README-MORE-PERMISSIVE`; open the Step 4 issues immediately so answers arrive while you build |
| 2–3 | SUAP OAuth2 via `django-auth-suap`; the `audit/` submodule wired from day one (an education SIS integration is audited by default, not later) |
| 4–5 | `moodle-local_suap` deployed against the institution's Moodle; LMS↔SIS identity and enrolment reconciliation |
| 6–8 | AI layer: `agente-bncc-professores` for teachers, `DeepTutor` scoped to enrolled subjects; `Pattern AP` scoping gate recorded in writing |
| 9–10 | Kolibri offline delivery for low-connectivity sites; handover with the grant state of **every** component listed in the deliverable |

🔵 **The deliverable includes the licence table.** On this tranche the licence state is not
background paperwork — it decided which half of the ecosystem exists for the client, and the
official components lost.

---


## 🆕 Pattern AV — `p443` **Open a national education market in one day: name the platform, not the capability** — and the four-step engagement that follows, wired from rows verified 2026-10-25

🔵 `Pattern AU` (`p442`) clears **one repository** whose grant nobody here has read.
`Pattern AV` is the step before *that*: how you find the repositories at all in a country whose
supply this base has never shelved — and then what you build from them. It was derived by doing
it: LATAM went from **5 of 116** placed rows on [`agents/top.md`](../agents/top.md) to a shelved
tier in one pass.

### Step 0 — the discovery move, and it is one line

🔴 **Do not search for the capability.** Measured this pass as a controlled pair, same index,
same minute, same platform names, only the query shape differing:

| query | result |
|---|---|
| 🔴 `SIU-Guarani OR SIAGIE OR SIMAT OR SIGAA mcp OR api OR agent`, sort `updated` | 🔴 **10 addresses, zero education.** A proxy list, a TikTok uploader, a WoW raid analyst — the capability words dominated the match and the proper nouns contributed nothing |
| 🟢 `sigaa OR "siu guarani" OR siagie`, sort `stars` | 🟢 **792 matches; 7 of the first 10 were real academic-portal tooling** |

```
# the move, stated so it transfers to any country
#   1. ask the client (or a local) WHAT SYSTEM THE INSTITUTIONS ACTUALLY RUN
#   2. search that proper noun ALONE, sorted by stars
#   3. add NO capability words — they are what a general index is densest in, so they
#      drown a proper noun
#   4. then run `Pattern AU` on every address that comes back
```

🟢 **Why it works, and why this base missed it for 440 passes.** Its EMEA line exists because
somebody searched *Librus*, *IServ*, *Smartschool*, *EduPage*, *Skola24*, *DTU Learn*. Nobody
had typed *SIGAA* or *SIU Guaraní*. 🔴 Earlier passes ran **Spanish and Portuguese** legs and
concluded *"the language was the wrong variable"* — that conclusion was right, and it hid the
correct one for another forty passes. The variable is **the proper noun of the system of
record**, and it is language-independent.

🔴 **Before searching outward, `grep` inward.** Five of the six LATAM addresses this pass
shelved were **already in this base's own append-only record**, found by earlier passes and
promoted by none, and all six are absent from the promotion ledger (`Gap 443-A`). The first
query of any new-market pass is against `agents/trending.md` and `repos/trending.md`.

### Steps 1–4 — the engagement, wired from rows verified first-hand this pass

🔴 **The constraint that shapes everything below**, measured in this tranche: of the four LATAM
platforms that hold student records, **0 of 4 carry a permissive grant**; of the 8 student-side
portal addresses, **6 do** (`Trend 42`). So the AI goes **beside** the system of record, never
inside it.

```
┌─ 1 · READ SEAM (MIT — the part you own) ──────────────────────────────────────┐
│  Argentina  jpmanson/siu-guarani-mcp      MIT  1 074 B · 53d0fa710f43        │
│             17 stdio tools over perfil Docente; READ-ONLY by construction;   │
│             PII behind include_pii=True; GUARANI_BASE_URL per institution    │
│  Brazil     PucaVaz/sigaa-tools           MIT  1 065 B · 75d9af3e2e90        │
│             the most recently maintained SIGAA reader (HEAD 2026-10-20)      │
│             reference model: GeovaneSchmitz/sigaa-api (MIT, 🔴 ARCHIVED)      │
└───────────────────────────────┬──────────────────────────────────────────────┘
                               │  MCP / HTTP — an interface, never a fork
┌──────────────────────────────▼───────────────────────────────────────────────┐
│  2 · SYSTEM OF RECORD (copyleft — integrate, NEVER vendor)                   │
│     ipti/br.tag  🔴 GPL-2.0  18 027 B · 111e1f411730                         │
│     🔴 its README says BSD-3-Clause. THE PAYLOAD GOVERNS.                     │
│     Moodle (GPL-3.0) · Open edX (AGPL-3.0) · Chamilo (GPL-3.0, deep LATAM)   │
└──────────────────────────────┬───────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────────────────────┐
│  3 · AGENT + EVIDENCE (permissive, yours to ship)                            │
│     huggingface/smolagents  Apache-2.0  11 357 B · c71d239df917              │
│     pykt-team/pykt-toolkit  MIT         1 066 B · f5f955194636               │
│       -> the knowledge-tracing layer that makes "adaptive" defensible        │
│     learningequality/kolibri MIT        1 097 B · 3c056b34a476               │
│       -> offline-first; REQUIRED where connectivity is ~50% (India: 53.9%)   │
└──────────────────────────────┬───────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────────────────────┐
│  4 · HUMAN SIGN-OFF (not optional, and already implemented upstream)         │
│     littlecookie0722/AI-Teaching-Agent  MIT — WAITING_REVIEW task per        │
│       artefact, approve/reject recorded  (Pattern AH's shape, shipped)       │
│     kaushikgunasekaren/canvas-grader-mcp MIT — draft for human sign-off      │
│       BY DEFAULT                                                             │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Why step 4 is load-bearing rather than decorative

🟢 `siu-guarani-mcp` is already read-only **by construction** — its author inspected the
attendance, topic and grade-loading forms and **deliberately does not submit them**, leaving
writes on the roadmap. 🟢 That is not a limitation to engineer around; **it is the compliance
posture, free.** Keep it: let the agent draft and let a human commit, which is what EU Annex
III (education, applying **2 Dec 2027**), Vietnam's **Decision 33/2026/QĐ-TTg** high-risk
register and the US state policies on this base's `intel/policy-matrix.tsv` each ask for in
their own words.

### Sizing, and what it is based on

| phase | weeks | what it produces |
|---|---|---|
| 0 · name-the-platform discovery + inward `grep` | **<1** | the country's address list; this pass did Brazil + Argentina in one hour |
| 1 · read seam hardened (auth, rate limits, per-institution base URL, PII gate) | 2–3 | an MCP server a tutoring or advising agent can call |
| 2 · agent + knowledge-tracing evidence layer | 3–4 | an adaptive claim with `pykt` numbers behind it |
| 3 · sign-off workflow + offline tolerance | 2–3 | the artefact a regulator or a ministry asks for |
| **total** | **8–11** | |

🟡 **Bounds, stated rather than implied.** (a) Every connector row here is **unofficial** and
scrapes a portal, so an institutional agreement is a prerequisite — the copyright question is
answered by `Pattern AU`, the **access** question is `P26` and lives in the institution's terms,
not in any payload. (b) `siu-guarani-mcp` is **1 ★ / 6 commits / single author**: read it as the
reference implementation of the seam, not as a dependency — exactly as EMEA's connectors began.
(c) `GeovaneSchmitz/sigaa-api` is **archived and read-only**: it is the best SIGAA *model* in the
open and must not be a build dependency. (d) Step 0 is bought for **Brazil and Argentina only**;
Peru, Colombia, Chile, Mexico and Uruguay are an **unverified nil** (`Gap 443-B`).

---

## 🆕 Pattern AU — `p442` **Clear a repository's licence in four steps that cannot be done in the wrong order**, and the three repositories that each break a different one

🔵 `Pattern AT` (`p441`) clears a **stack** whose grants are already known. `Pattern AU` is the
step before it: the screen you run on a repository **nobody here has read yet**, built out of
this base's four existing instruments in the one order that works. Every component is in the
clone; nothing below is new code.

### The screen

```sh
# 0 · the repository resolves, and its DEFAULT BRANCH is read, never assumed
#     (measured: GibbonEdu/core -> v31.0.00, rosariosis -> mobile, i-educar -> 2.12)
. compose/code/lib/probe_payload.sh
probe_default_branch "$SLUG"

# 1 · ENUMERATE THE TREE.  A filename list can only FIND a licence; only enumeration can
#     say which payload is the grant, or that there is none (P441).
probe_repo_all "$SLUG"            # one row per licence text: path, bytes, family, holder
                                  # ~0.7 s; blobless depth-1 clone, no GitHub API needed

# 2 · FAMILY, from the hardened owner only.  Never re-answer it in a grader (P171).
lib/measure --family <payload>

# 3 · IS THE GRANT ACTUALLY THERE?  A pointer to a licence is not a grant (P1065).
python3 -I compose/code/p439-grant-presence/grant_presence.py --family "$FAM" <payload>
python3 -I compose/code/pass258-content-licence-family/content_licence.py <payload>  # CC/content

# 4 · publish the cell with the primitive, so the row cannot carry P834
lib/measure --cell <payload>      # -> `1 069 B · 262b47ee1fff`
```

🔴 **The order is the pattern.** Step 3 on step 1's *first* answer is what this base did for
441 passes, and it is wrong in both directions: on `ucbds-infra/ottr` the first answer is a
108 B stub that no clause profile can even grade, and on `24kchengYe/human-skill-tree` it is a
notice that makes a well-licensed project look unlicensed.

### The three repositories that break three different steps — each verified 2026-10-25

| step it breaks | repository | what happens without it | what the screen returns |
|---|---|---|---|
| **1 · enumerate** | [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | the ladder returns `LICENSE` **108 B**, family `UNCLASSIFIED` (R's `YEAR:` / `COPYRIGHT HOLDER:` stub) and stops | `LICENSE` 108 B `UNCLASSIFIED` **and** `LICENSE.md` **1 555 B · `1677c5307530`** → **BSD-3, `GRANT-PRESENT`** |
| **1 · enumerate (inverse)** | [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | the root payload (1 134 B · `3fb8cda58638`) grades `GRANT-BY-REFERENCE` → reads as *"project did not grant"* | the grant is at `app/LICENSE` **34 523 B · `0d96a4ff68ad`** (AGPL-3.0) **and** the root notice offers `skills/` under **AGPL-3.0 *or* MIT at the user's option** → a permissive lane |
| **1 · enumerate (subtree copyleft)** | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) | root is MIT 1 071 B · `22e7ab2dbddc`; the row reads *permissive, vendor freely* | 🔴 **GPL-3.0 at `legacy_reference/LICENSE`, 35 149 B · `3972dc9744f6`, `GRANT-PRESENT`**, beside 20+ `.py` files → **integrate over MCP, never vendor** |
| **3 · is the grant there** | [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `LICENSE` 1 230 B is titled CC BY-SA 4.0 and *reads* like a grant | 🔴 `CONTENT-POINTER: not-a-grant` — the payload says *"This is a human-readable notice. The full legal terms are available at …/legalcode"*; the binding text is the canonical 18 375 B one |
| **4 · publish the cell** | this base's own shelves | 19 of 162 published cells carried the capture signature (`P834`) | `cell_of_file` owns the string; `make gate-cell-reproduction` reports **162/162** |

### What to hand a client's counsel

1. The `probe_repo_all` TSV for each component — **every** licence text in the tree, not the
   first one found, with bytes and `sha256₁₂` at a named commit.
2. The `grant_presence` verdict per payload, with the **profile** that judged it
   (`GRANT-PRESENT` / `GRANT-TRUNCATED` / `GRANT-BY-REFERENCE` / `GRANT-UNCALIBRATED`).
3. A one-line disposition per component: **vendor**, **integrate over an interface**, or
   **do not use** — and for a subtree-copyleft repository the disposition is a *boundary*,
   not a yes/no.
4. 🔴 The declared blind spots, because a screen that hides them is worse than none:
   **EUPL-1.2 has no clause profile here** (`Gap 442-C`), **LGPL needs a `GRANT-BY-DESIGN`
   verdict it does not have** (`Gap 440-B`), and **`*-assets/` is not on the vendored-path
   exclusion list**, so a vendored grant in such a directory is typed as the project's own
   (`Gap 442-B`).

### When to run it

🟢 On **every** component before it enters a proposal, and the cost says you can: 134
repositories enumerated in **33 s**, measured this pass. 🔵 Where the client is the one asking
(procurement, a counsel review, an OSPO), steps 1–3 are also the deliverable — a licence
report whose every figure reproduces from a named commit is worth more than a scanner's
summary, and it is the thing this base can hand over that a scanner cannot.

## 🆕 Pattern AT — `p441` The **autograded course stack that is entirely BSD-3, verified clause-by-clause**, and the three screening rules that stop it being badge-deep

🔵 `Pattern AS` (`p440`) maps the **copyleft** obligations a hosting choice triggers.
`Pattern AT` is its permissive counterpart and it is narrower on purpose: one stack, named
repositories, verified payloads, and a CI step a client's counsel can read. 🟢 Every
component below was probed first-hand on **2026-10-25** and graded `GRANT-PRESENT`
clause-by-clause — not from a badge, a README, or a package manifest.

### The stack

| layer | repository | licence, verified 2026-10-25 | why this one |
|---|---|---|---|
| LMS entry | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 BSD-3 · `LICENSE` 1 528 B · `08eebd9662cb` | LTI 1.1/1.3 launch from Moodle, Canvas or Open edX — the client keeps its LMS |
| compute | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3 · 1 475 B · `7069c7e8d60e` 🔴 **untitled payload** | identical environment per cohort member |
| assignment lifecycle | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 · 1 512 B · `3a83d5b8e22c` 🔴 **untitled payload** | release → collect → autograde → return, already solved |
| autograding (Python) | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 BSD-3 · `master/LICENSE` 1 560 B · `6af203d41a01` | container-isolated execution at Berkeley cohort scale |
| autograding (R) | [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | 🟢 BSD-3 · 🔴 **`LICENSE.md` 1 555 B · `1677c5307530`**, *not* the 108 B `LICENSE` | R scripts, R Markdown and R notebooks |
| tutor surface | [`QuantStack/jupyter-ai-tutor`](https://github.com/QuantStack/jupyter-ai-tutor) | 🟢 BSD-3 · 1 532 B · `ccaa70decf0d` | version-controlled `TUTOR.md` persona — the pedagogy stays a reviewable artefact (`Pattern X`) |
| model access | [`jupyterlab/jupyter-ai`](https://github.com/jupyterlab/jupyter-ai) | 🟢 BSD-3 · 1 516 B · `a0be5735cdce` | provider-agnostic LLM plumbing inside JupyterLab |
| offline arm | [`jupyterlite/jupyterlite`](https://github.com/jupyterlite/jupyterlite) | 🟢 BSD-3 · 1 525 B · `574f8a9cab1e` | kernel in the browser, no server — **the APAC answer**: India's Class 3–8 mandate lands on schools at 63.5 % connectivity |

🟢 **One licence family across eight components.** A single obligation set (retain the notice
in source, reproduce it in binaries, no endorsement) applies to the whole stack, and nothing
in it is network-triggered — so the hosting model is **not** constrained the way an AGPL
platform constrains it (`Pattern AS`).

### The wiring

1. **Entry.** `ltiauthenticator` as JupyterHub's authenticator; the LMS stays the roster and
   the gradebook of record. No student identity is minted in the new stack.
2. **Course build.** `nbgrader` owns the assignment source; `otter-grader` (Python) and
   `ottr` (R) own execution. 🔵 Pick one per language and let `nbgrader` call it — running
   both over one assignment doubles the container surface for nothing.
3. **Tutor.** `jupyter-ai` supplies model access; `jupyter-ai-tutor` supplies the persona as
   a committed `TUTOR.md`. 🟢 The persona is reviewed like code, which is what `Pattern X`
   and Arkansas `H.B. 1958`'s *named authorised human* both require.
4. **Offline.** Build the same notebooks into `jupyterlite` for low-bandwidth deployment.
   The autograder stays server-side; only delivery goes to the browser.

### 🔴 The three screening rules — each one a defect measured on this exact stack

1. **Pass the family in; do not read it off the title.** 🔴 Three of the eight payloads
   above carry **no title line at all**, so a title-keyed classifier answers `UNKNOWN` for
   `jupyterhub`, `nbgrader` and `open-tutor-ai-CE`. Take the family from a hardened
   classifier (`compose/code/lib/license_family.sh`) and hand it to the grant check:

   ```sh
   # the family from its hardened owner, the grant from the clauses
   python3 -I compose/code/p439-grant-presence/grant_presence.py \
       --family BSD path/to/LICENSE
   ```

2. **Enumerate the tree; never take the first filename-ladder hit.** 🔴 `ottr` is an R
   package: `DESCRIPTION` says `License: BSD_3_clause + file LICENSE`, so `LICENSE` holds
   **108 B** of `YEAR:` / `COPYRIGHT HOLDER:` and the licence **text** is at `LICENSE.md`.
   A ladder that stops at the first hit reports the most adopted R autograder in this
   industry as **ungranted**. `Gap 441-A`.

3. **`GRANT-PRESENT` is not `GRANT-UNMODIFIED`.** 🔴
   [`open-webui/open-webui`](https://github.com/open-webui/open-webui) — a tempting drop-in
   for the chat surface — is stock BSD-3 **plus a branding restriction plus a Contributor
   Licence Agreement** (2 819 B against ~1 515 B). Every clause is present, so it grades
   `GRANT-PRESENT` and is still **not** an OSI-standard BSD grant. Use `jupyter-ai` for this
   layer, or take `open-webui` with the restriction written into the SOW.

### The deliverable

Run the screen in the client's CI and **commit its output**, exactly as `Pattern AR` does for
the copyleft arm:

```sh
make bsd-variant-census > evidence/licence-verdicts.$(date +%F).tsv
```

🟢 That TSV is the artefact: one row per payload, with bytes, `sha256₁₂`, the variant profile
that judged it and the verdict. 🔵 It answers *"every third-party licence was READ, not
scanned"* with a reproducible measurement rather than an assurance — and for the three
untitled payloads it is the only thing that can.

## 🆕 Pattern AS — `p440` The **copyleft obligation map**: turn "which licence" into "which obligation, triggered by which deployment choice", before the hosting model is fixed

🔵 `Pattern AR` (`p439`) makes *"every third-party licence was READ, not scanned"* a CI
artefact. 🔴 It had a hole that was invisible until this pass: its grant-presence gate
could read MIT, Apache-2.0 and ISC, and **declined on the entire copyleft tier** — which
in education is the LMS, the SIS and the video layer, i.e. the parts the client cannot
replace. `Pattern AS` is the copyleft arm, and it is a **pre-architecture** deliverable:
run before the hosting model is chosen, because after that the obligation is already
incurred.

### The problem, stated the way a client experiences it

An education client picks a platform on features and TCO, hosts it, then modifies it.
🔴 Nothing in that sequence asks *whether the modification must be published*, and the
answer is decided entirely by a clause in a file nobody opened. Open edX and Moodle look
interchangeable on a feature matrix. They are not: one obliges a hosted deployment to
offer its users the Corresponding Source, and the other does not.

### The wiring — concrete, with the repos this base has verified

**1. Resolve the payload, not the badge.** `compose/code/lib/probe_payload.sh`,
**sourced, never re-implemented** (`set +u`, per `p436`). It resolves the default branch
with `ls-remote --symref` — 🔴 three of the ten platforms verified at `p440` are not on
`main` or `master` (`GibbonEdu/core` → `v31.0.00`, `portabilis/i-educar` → `2.12`,
`francoisjacquet/rosariosis` → `mobile`), and a hardcoded branch writes all three down as
ungranted.

**2. Grade the grant against its own licence VERSION.**
`compose/code/p439-grant-presence/grant_presence.py` with `p440`'s version-aware
profiles (`AGPL-3.0`, `GPL-3.0`, `GPL-2.0` alongside MIT / Apache-2.0 / ISC).
🔴 `resolve_version()` first: a complete GPL-2.0 licence is missing four of GPL-3.0's six
operative clauses, so grading the family instead of the version condemns a valid grant.
An unresolvable version returns `GRANT-UNCALIBRATED` — publish it, never suppress it.

**3. Map verdict → obligation → deployment trigger.** This is the deliverable:

| Grant | Trigger | What the client owes | Platforms (verified 2026-10-25) |
|---|---|---|---|
| **MIT / Apache-2.0 / BSD** | — | attribution; Apache-2.0 §4(a) also a **copy of the licence** | `openedx/XBlock`, `huggingface/smolagents`, `learningequality/kolibri` |
| **GPL-2.0** | **distribution** of binaries | complete corresponding source to recipients. 🟢 **No network clause — it predates the question** | `portabilis/i-educar`, `francoisjacquet/rosariosis`, `OS4ED/openSIS-Classic` |
| **GPL-3.0** | **distribution** | corresponding source; anti-tivoisation | `moodle/moodle`, `chamilo/chamilo-lms`, `GibbonEdu/core` |
| 🔴 **AGPL-3.0** | **network interaction** (§13) | modified version's Corresponding Source offered **to the platform's own users** | `openedx/edx-platform`, `instructure/canvas-lms`, `frappe/lms`, `Chocobozzz/PeerTube` |
| 🟡 **LGPL-3.0** | — | 🔴 **not assessed** — incorporation by reference by design (`Gap 440-B`) | `BigBlueButton`, `OpenEduCat` |

**4. Place the AI work on the permissive side of the seam.** The whole point of the map
is that it tells you where to stand. On an AGPL platform, build **through the supported
extension point** rather than in the core: [`openedx/XBlock`](https://github.com/openedx/XBlock)
(Apache-2.0, `LICENSE.TXT` 11 358 B · `cfc7749b96f6`) is the Open edX seam, and the
agents this base shelves — `canvas-grader-mcp`, `littlecookie0722/AI-Teaching-Agent`,
`ls1intum/edutelligence` — are all MIT services that integrate **over an interface**.
🟢 Nothing the studio writes inherits §13.

**5. Ship the third column.** The report has **three** columns — verdict, the clauses
actually found, and what was **not assessed and why**. 🔴 A two-column report renders
"unknown" and "fine" identically (`Trend 38`), and the uncalibrated rows are exactly the
ones with the largest obligations attached.

### What it is worth, and where

🟢 **LATAM is the unexpected winner and the pitch nobody makes.** The region's SIS tier is
**GPL-2.0** — no §13, so a hosted deployment triggers no source-offer obligation to its
users. That is a real, defensible hosting advantage for `i-Educar`, `RosarioSIS` and
`openSIS`, and it is invisible to any tool that grades "GPL" as one thing.
🔵 **EMEA**: GPL-3.0 on Moodle/Chamilo keeps copyleft off the hosting model, which
composes cleanly with the 2 December 2027 Annex III runway (`Pattern AP`).
🔴 **NA and APAC** are the exposed ones — Canvas and Open edX are AGPL — and there the
XBlock/interface seam is the engagement, not a detail.

**Sizing.** 2–3 weeks for a platform estate of this size: ~1 week probing and grading,
~1 week mapping obligations to the client's actual hosting and modification plan, ~1 week
wiring the gate into CI as `Pattern AR` specifies. 🟡 It is cheap because the instruments
exist; it is valuable because it runs **before** the architecture is fixed.

---

## 🆕 Pattern AR — `p439` The **grant-presence gate in the build**: make "every third-party licence was READ, not scanned" a CI artefact, and wire the same gate a client's procurement can run

🔵 **The problem this pattern solves, measured rather than asserted.** `Pattern AQ` (`p438`)
made component clearance an auditable build artefact. 🔴 `p439` found the hole in exactly that
artefact: a licence **scan** passes a payload that contains no grant. Live specimen from
education supply, read 2026-10-25:
[`spragginsdesigns/ai-tutor-webapp`](https://github.com/spragginsdesigns/ai-tutor-webapp),
`LICENSE` **552 B** · `sha256₁₂ 5809eb2eab28`, titled Apache-2.0, holder 🔴 **Vercel, Inc.**,
licence text **not in the repository**. Every instrument on this base graded it
`PERMISSIVE / stock = True / needs_a_human = False`. A clearance report built on a scanner
would have shipped it green.

### The recipe — concrete repos, concrete wiring

🔵 **And the reason this is a pattern rather than a tip**: the principle is old and keeps not
travelling. `P1065` on this base settled in pass 254 that a pointer to a licence is not a
grant; the predicate was implemented for **Creative Commons content licences** and never
reached the instruments that grade MIT, Apache-2.0 and BSD. 🔴 In a client pipeline the same
thing happens by default — the rule lands in whichever scanner surfaced the problem, not in
the one that writes the verdict. **Wire it where the verdict is written.**

**1. The gate itself (build it once, ~1 day).**
[`compose/code/p439-grant-presence/`](./code/p439-grant-presence) in this base is the working
reference: `grant_presence.py` classifies a payload into **GRANT-PRESENT /
GRANT-BY-REFERENCE / GRANT-TRUNCATED / GRANT-UNCALIBRATED** by asking whether the family's
**operative clauses** are present, with 19 controls in `test_grant_presence.py`.

```
make gate-grant-presence     # controls, offline, committed fixtures — CAN go red
make grant-presence-census   # the live dependency set — a MEASUREMENT, always exits 0
```

🔵 **Keep that split in the client's pipeline too.** The controls block a merge; the
population only reports. A gate that goes red because the *dependency set* changed teaches a
team to disable the gate — this base learned that twice (`Gap 435-A`, `Gap 438-B`) and both
times the remedy was the same split.

**2. Wire it where the payloads already arrive.** Compose it with what this base already
carries rather than building a new scanner:

| Stage | Component | Grant | Role |
|---|---|---|---|
| Resolve branch + fetch payload | [`lib/probe_payload.sh`](./code/lib) (this base) | — | `ls-remote --symref` so a non-`main` default (`master`, `develop`, `v31.0.00`) is never read as *ungranted*; README-link rung before the filename ladder |
| Family, by title block | [`lib/license_family.sh`](./code/lib) (this base) | — | `P171`: classify by **title block**, never body substring — GPL-3.0 §13 is titled with AGPL's name |
| 🆕 **Grant presence, by clause** | `p439-grant-presence` | — | the new rung: is the granting text actually here? |
| Orchestrate per dependency | [`temporalio/temporal`](https://github.com/temporalio/temporal) | MIT | one durable workflow per component; retries and the full read history survive a crash |
| Surface the report | [`appsmith`](https://github.com/appsmithorg/appsmith) | Apache-2.0 | the procurement-facing view: filter to `GRANT-BY-REFERENCE` + `GRANT-TRUNCATED` |
| Model indirection (APAC) | [`BerriAI/litellm`](https://github.com/BerriAI/litellm) | MIT | only if the pipeline summarises clauses with an LLM — keeps sovereign models swappable |

**3. The three rungs, in this order, and the order is the whole pattern.**

```
exists?            git ls-remote            -> UNRESOLVED is not "ungranted"
what is it called? family_of (title block)  -> P171
🆕 is it HERE?     grant_presence.classify  -> Gap 439-A
```

**4. The two negative controls to copy, because they are defects this base actually had.**

- 🔴 **Do not key on "the payload says the licence is elsewhere."** That phrase appears
  **verbatim inside the full Apache-2.0 text** — the APPENDIX is part of the licence. Measured:
  the 11 357 B full text carries **all three** reference markers. Ask clauses **first**; let
  the markers only separate `TRUNCATED` from `BY-REFERENCE`.
- 🔴 **Fold typographic quotes before matching anything.** A complete MIT licence that
  typesets “AS IS” with U+201C/U+201D was graded `GRANT-TRUNCATED` by this instrument's first
  draft — a real grant condemned by a punctuation character.
- 🔴 **And do not substitute a byte floor.** BSD stock payloads span **221 B → 1 514 B** on
  this base's corpus, because BSD-0/2/3 are three lengths under one family name.

**5. What ships to the client.** Per-component: slug, resolved default branch, payload path,
bytes, `sha256₁₂`, HEAD SHA, family, **grant verdict**, and for anything not `GRANT-PRESENT`
the **named missing clauses**. 🟢 The two obligations this catches and a scanner cannot —
Apache-2.0 **§4(a)**'s duty to supply a copy of the License, and MIT's notice obligation
against a holder that resolves to nobody — are both *integrator* duties, which is precisely
why they must be found before delivery and not after.

**Effort:** ~1 day for the gate against an existing clearance pipeline (this base's reference
is ~300 lines plus 19 controls); **2–3 weeks** to stand up the whole chain from nothing.
🟡 **Where it pays**: any engagement that **vendors or redistributes** third-party components —
an LMS platform build, a white-labelled tutor, anything shipped to a public-sector buyer. For
a system the client only *calls* over a network, this ranks below `P26` (the access-rights
question, which lives in a Terms of Use and not in a licence).

---

## 🆕 Pattern AQ — `p438` The **component-clearance gate**: make "every third-party part of this stack was read, not scanned" a build artefact the client can audit

🔵 **The engagement this answers.** Any education build that assembles AI components — which
is all of them now. The client's procurement function will ask *"is this open-source stack
clean?"*, their counsel will ask it again at renewal, and the honest answer today is a
scanner report that prints one SPDX identifier per file. 🔴 `p438` measured what that report
misses on this base's own corpus: **9 of 238** committed licence payloads carry an addition
the family column does not describe, and **7 of those 9** are routed by
`bespoke_census.needs_a_human()` as needing **no** human read — `p427`'s own two-family
specimen among them. 🔴 One of the nine addresses this pass graded (**11 %**) carried a
clause, in Chinese, pushing content-copyright liability onto the operator. **On an education
engagement the operator is the school and the content is textbooks.**

🟢 **What makes this sellable rather than hygiene**: the output is not a policy document, it
is a **CI job that fails the build**, plus a signed per-component ledger. The client is buying
the evidence, and the evidence is cheap because the instruments already exist.

### 🟢 Step 1 — resolve each component's real address and grant (do not trust a badge)

Use this base's own probe, **sourced, never re-implemented** — the rule is in
`compose/code/lib/README.md` and has been broken twice on this base:

```bash
set +u                                     # the library needs it; p436 measured why
. compose/code/lib/probe_payload.sh
probe_repo <owner/repo>                    # -> repo, branch, file, bytes, family, holder
```

🔴 Three traps it closes, each measured on real education repositories, not hypothesised:
the default branch is often **not** `main` (`GibbonEdu/core` → `v31.0.00`,
`francoisjacquet/rosariosis` → `mobile`, and this pass's own `eugeniughelbur/doceo` →
`master`); the payload can live in a **subdirectory**; and British `LICENCE` exists in the
wild.

### 🟢 Step 2 — grade the payload on **three** columns, not one

```bash
make bespoke-census PAYLOADS="/path/to/LICENSE"
```

Fail the component into human review when **any** of these holds:

| column | fail condition | why |
|---|---|---|
| `titled_family` | not in {MIT, Apache-2.0, BSD-2/3-Clause, ISC} | the ordinary licence screen |
| `p1054_verdict` | contains an **addition** (e.g. `MIT-BODY-PLUS:unclassified-addition`) | 🔴 **the column `needs_a_human` ignores** — this is the step that is new |
| payload bytes | outside the family's stock band (MIT clusters at **1 055–1 079 B** on these shelves) | the band detects *that* a payload was modified; only a person learns *what* the modification says |

🔴 **Do not substitute `needs_a_human` for this table until `Gap 438-A` is discharged.** On
`p438`'s specimen it returns `no` while the row beside it says `unclassified-addition`.

### 🟢 Step 3 — read the surplus bytes **in their own language**

`p427`'s `conjunctive_grant.classify()` is the right second instrument and returns
`scope: None` here, because its `SCOPE_MARKERS` (`compose/code/p427-conjunctive-grant/conjunctive_grant.py:73`)
are English: `portions of`, `derived from`, `remain under`, `original license`, `third-party`.
🟢 **So the surplus goes to a human with the language named**, and the question put to them is
fixed and answerable in two minutes: *does this clause (a) add a notice obligation, (b) narrow
the subject matter of the grant, or (c) move a liability onto the operator?* 🔵 `p438`'s
specimen is **(b) and (c)**: the repository ships no book content, and the operator carries the
copyright liability for the material it is pointed at.

### 🟢 Step 4 — wire it as a gate and keep the ledger

One job in the client's CI, one TSV in the repository: `component, address, branch, file,
bytes, sha256₁₂, family, addition_verdict, human_read_by, date`. 🟢 `p436`'s ledger lesson
applies and is why the ledger is the artefact: **a claim with no committed row is a claim that
disappears at the next rewrite** — that pass found **176** addresses claimed promoted with no
live row behind them.

### 🟢 A concrete stack this runs over, every row already cleared first-hand on these shelves

| layer | component | grant |
|---|---|---|
| tutoring core | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0, `LICENSE` 11 408 B |
| learner modelling | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT, `LICENSE` 1 066 B |
| LMS seam (no AGPL contact) | [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0, `LICENSE.TXT` 11 358 B |
| offline delivery | [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT |
| pedagogy layer | [smashburger-dev/socratic-workshop](https://github.com/smashburger-dev/socratic-workshop) | MIT, `LICENSE` 1 072 B · `7f3dec641d9f` |
| learner-memory skill | [briannajzhang/personal-tutor](https://github.com/briannajzhang/personal-tutor) | Apache-2.0, `LICENSE` 11 357 B · `c71d239df917` |
| obligation check | [tomdxb0004/eu-ai-act-risk-checker](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | MIT — 🟢 the **post-Omnibus-correct** one per `p437`; `engine.js:32` encodes `2027-12-02` |

🔴 **And one row that this gate is the reason you can still use**:
[fangyuan-3149/book-learning-tutor](https://github.com/fangyuan-3149/book-learning-tutor)
(MIT, `LICENSE` 1 503 B · `54ceeac19921`). Cleared by a scanner, cleared by `needs_a_human`,
and it belongs in a build **only** with its clause in the statement of work. 🟢 Step 3 is what
turns it from a hidden liability into a priced one.

### 🔵 Price and where it goes in the engagement

**2–3 weeks** for the job, the ledger and the first full sweep of an existing estate, then
minutes per new component. 🟢 Sell it as the first phase of any education build and as a
stand-alone diligence piece into an estate someone else assembled — `Pattern AP`'s scoping
gate decides *whether* the product is high-risk; this one decides *whether its parts can be
shipped at all*, and the two are sold together.


## 🆕 Pattern AP — `p437` The **Article 6(3) scoping gate**: decide whether the client's adaptive-learning product is high-risk *before* writing the architecture

🔵 **The engagement this answers.** A client wants adaptive learning, knowledge tracing or
automated grading in the EU. The pitch everyone makes is *"Annex III moved to December 2027,
you have fourteen months"*. 🔴 **That framing loses the engagement**, because it answers the
wrong question. Two things are already true today, and one of them decides the entire
architecture:

| question | answer | when it bites |
|---|---|---|
| Is the product **prohibited**? | Emotion recognition in educational institutions is banned outright, Art. 5(1)(f), narrow medical/safety exception | 🔴 **Since 2 February 2025 — live now** |
| Does it owe **transparency**? | Art. 50: disclose AI interaction, machine-readable marking of synthetic output | 🔴 **Since 2 August 2026 — live now** |
| Is it **high-risk**? | Annex III point 3 — admission, evaluating learning outcomes, level determination, proctoring | 🟡 2 December 2027 |
| 🔵 Can it **escape** high-risk via Art. 6(3)? | Only if it meets one of (a)–(d), poses no significant risk, **and does not profile natural persons** | Decided at design time |

### 🔴 The gate, and why most education AI fails it

Article 6(3) is the only exit from Annex III classification, and the profiling condition
closes it for the architectures this base recommends most. **Knowledge tracing is profiling.**
`pykt-team/pykt-toolkit` (DKT/SAKT/BKT) and `CAHLR/OATutor` (Bayesian Knowledge Tracing), both
on the `agents/top.md` build-on tier, construct a per-learner model of a natural person in
order to work. So:

> 🔴 **If the product adapts to the individual learner, it profiles, the Art. 6(3) exception is
> unavailable, and it is high-risk — full Art. 9–15 obligations.** There is no architecture
> that keeps the adaptivity and sheds the classification.

🟢 **This is good news for the engagement, not bad.** It converts a vague compliance worry
into a fixed, quotable scope of work with a statutory deadline, and it disqualifies competitors
pitching "lightweight" adaptive learning that quietly assumes the exception applies.

### The stack, every grant read first-hand at HEAD on 2026-10-25

| Layer | Component | Grant (payload read first-hand) |
|---|---|---|
| **Scoping decision** | [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) — `engine.js:170-186` implements (a)–(d) + the profiling override | 🟢 **MIT** · 1 073 B · `b7b08f330649` @ `41da87feb238` |
| **Annex IV technical documentation** | [`Hiepler/EuConform`](https://github.com/Hiepler/EuConform) — report generator + CrowS-Pairs bias evaluation | 🟢 **MIT** · 1 073 B · `65335056589f` @ `011a5ad9bea2` |
| **Annex III checklist / agent controls** | [`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit) | 🟢 **MIT** · 1 074 B · `7df20dcdf919` @ `70a4ab8e8a04` |
| **Codebase scan** (not dates) | [`ark-forge/mcp-eu-ai-act`](https://github.com/ark-forge/mcp-eu-ai-act) | 🔴 **MIT** · 1 065 B · `002af8f9b59c` — dates superseded, scanning only |
| **The modelling layer being classified** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) · [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** · 1 066 B · `f5f955194636` / 1 105 B · `5baaaf977a28` |
| **Bias / fairness evidence for Art. 10** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) standard datasets + EuConform bias eval | 🟢 **MIT** |

### How it wires together

1. **Run the scoping decision first, before any model choice.** Open `index.html` from
   `eu-ai-act-risk-checker` (no build step, no backend). Answer as the *provider*. Record the
   tier, the article list and the per-obligation dates it returns, with its citations — this
   becomes the engagement's scoping memo.
2. **Force the profiling question explicitly.** If the product adapts per learner, set
   `profiling = true`. 🔴 Expect `profilingOverride` to fire and the Art. 6(3) exception to
   close. Do not let an optimistic reading of (a)–(d) survive this step; `engine.js:172`
   is the executable version of the rule.
3. **Gate the tool before you trust it** — three greps, because two of the five permissive
   EU-AI-Act tools on these shelves encode the superseded deadline:
   ```bash
   grep -rn '1744'                         # must match
   grep -rn '2027-12-02\|2 December 2027'  # must match
   grep -rn '2026-08-02\|2 August 2026'    # must NOT be a high-risk deadline
   ```
4. **Generate Annex IV documentation from the start.** EuConform's report generator produces
   the technical-documentation shape Art. 11/Annex IV expects. Building it at design time is
   the whole value of the December 2027 runway; retrofitting it is the thing clients pay
   double for later.
5. **Attach Art. 10 data-governance evidence to the modelling layer.** Run the bias
   evaluation over the knowledge-tracing datasets *as a CI artefact*, not a one-off report,
   so the evidence regenerates with every model change.
6. **Settle the two live obligations before go-live, not before the deadline.** Strip or
   never build emotion/affect inference (Art. 5(1)(f), prohibited since February 2025), and
   wire Art. 50 disclosure and synthetic-output marking now — both already apply.

🔵 **What this pattern deliberately does not claim.** None of these tools is legal advice, and
`eu-ai-act-risk-checker`'s own README says several conditions turn on judgements it cannot
make — significant harm, significant risk, whether AI use is obvious. The gate produces a
**defensible, cited scoping position** for counsel to sign off, which is the deliverable;
it does not replace the sign-off.

## 🆕 Pattern AO — `p436` The **assessment-interoperability** engagement: parametric items a client can author, deliver and prove, with no copyleft anywhere in the chain

🔵 **The engagement this answers.** A client with a real examination obligation — a ministry, a
board, a university consortium — needs items that are *generated per learner* (so they cannot be
shared), *delivered in a standard the regulator recognises*, and *provable after the fact*. Until
`p436` this chain could not be assembled from this base's live shelves at all: the repository it
depends on had been silently deleted.

🟢 **The stack, every grant re-read first-hand on 2026-10-25, every licence permissive:**

| layer | component | licence | why this one |
|---|---|---|---|
| 1 · author | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) `packages/core` | **MIT** `1 072` B · `00ed05b90bf8` | the only readable implementation of `qti-template-declaration` / `qti-template-processing` with a real `randomInteger` draw over min/max/step and a constraint-retry loop |
| 1b · emit | `compose/code/p533-qti3-template-emitter/` (this tree) | — | 🟢 the `Gap 238` artefact: regenerates two upstream fixtures **node-for-node**, 43 assertions, 11 of 11 mutations detected. 🔴 `qti3`'s **writer** cannot emit these elements — this is the workaround, and `Gap 240` is to contribute it upstream |
| 2 · render | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** `1 076` B · `7faa621251d7` | QTI 3 item rendering |
| 3 · deliver | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | **BSD-3-Clause** `2 058` B · `a5c692f12090` | QTI 2.1 delivery, **JQTI+** and **MathAssess** for mathematical response processing; live to 2026-06-30 |
| 3b · PHP estate | [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | **MIT** `1 066` B · `27fb6d463569` | the route in when the estate is PHP (i.e. Moodle); published by the **Dutch national education-ICT body** |
| 4 · roster | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | **Apache-2.0** `10 173` B · `a6cba85bc92e` | OneRoster 1.2 over an Ed-Fi ODS — who sits the exam, without touching the SIS |
| 5 · connect | the restored LMS-connector tier on [`agents/top.md`](../agents/top.md) | **MIT / ISC** | push items and pull submissions from the LMS the client already runs (Canvas, Moodle, Blackboard, Classroom) |
| 6 · sign-off | `kaushikgunasekaren/canvas-grader-mcp` (already shelved) | **MIT** | **draft-for-human-sign-off by default** — the staged artefact EU, Vietnamese and US-state oversight rules all require |

### How it wires together

1. 🟢 **Author one template, not N items.** Hand-author the template XML from
   `qti3`'s `packages/fixtures/xml/random-integer-template-reference.xml` (~35 lines), **or** run
   the `p533` emitter to generate it. 🔴 **Do not plan on `qti3`'s `writer` package** — it has
   **0 of 33** exports for these elements (`Gap 39`, refuted for authoring).
2. 🟢 **Let `core` execute the draw.** It parses the declaration, draws over the declared grid,
   derives the answer key **from the draw**, and retries up to 100 times against constraints. The
   per-learner variant and its key are produced by the same pass — which is what makes the result
   defensible.
3. 🟢 **Validate transitively, not by assertion.** The emitter's output matches the fixtures
   `qti3`'s own schema gate validates against the sha256-pinned official ASI schema, so validity
   is inherited. 🔴 **Stated limit**: the official XSD could not be fetched here
   (`purl.imsglobal.org` proxy-blocked, `Gap 56` class), and `qti3`'s suite was **not executed** —
   installing a third-party repository's dependencies is not permitted in this environment.
4. 🟢 **Render and deliver** through layer 2/3, or 3b for a PHP estate.
5. 🟢 **Resolve cohort from layer 4**, so the exam roster is the SIS's answer and not a copy.
6. 🟢 **Return results through layer 5, and gate every grade through layer 6.** Nothing writes a
   grade without a human action.

### Why the licences matter here specifically

🟢 **There is no copyleft anywhere in the chain** — MIT, MIT, MIT, BSD-3-Clause, MIT, Apache-2.0.
🔵 That is unusual on this base and it is the point: the assessment boundary is the one tier where
a client most often needs to **ship a modified binary to a ministry** without publishing it, and
the AGPL platform tier (Open edX, Moodle's GPL) cannot be the carrier for that.

### Cost, and what would sink it

🟡 **Realistic shape: 8–10 weeks** — 2 to wire author→render→deliver on the fixtures, 2 for the
roster seam, 2 for the LMS connector, 2–4 for the sign-off path and the audit trail.
🔴 **What would sink it**: (a) `qti3`'s suite has **never been executed in this environment**, so
first-week work is standing the upstream suite up on a real checkout; (b) `amp-up-io`'s HEAD is
**2025-06-21** — the only stale link in the chain, and the one to re-check before committing;
(c) if the regulator requires QTI **3** delivery rather than 2.1, layer 3 does not satisfy it and
the chain is authoring-and-rendering only.

🔴 **Provenance warning, because this pattern is the reason it matters**: four of these six
components were **off every live shelf until `p436` restored them**, while `Gap 240` stayed open
pointing at one of them. 🟢 `gate-promotion-ledger`'s `C3` control now fails if any of them is
dropped again.

# 🧩 Compose patterns — Education

> Concrete recipes: named repos, named licences, and how they wire together.
> Every component below was licence-verified at a commit SHA on 2026-10-25.

## 🆕 Pattern AN — `p435` The **national school-platform connector** engagement: the EMEA build that does not ask the client to replace anything

🔵 **The engagement this base could not describe until now.** Every platform pattern here
starts by choosing a base — OpenOLAT or Kolibri if the client cannot take copyleft, Moodle
or Open edX if it can. 🔴 **A national school system is not going to migrate.** IServ runs
German state schools, Librus Synergia runs Polish gradebooks, Smartschool runs Flanders,
EduPage runs Slovakia, Skola24 runs Swedish timetables. The buyable engagement is a
**permissive agent layer over the incumbent**, and `p435`'s grade census of this base's own
backlog finally produced the addresses for it.

### The stack, with the grant on every piece — all read first-hand at HEAD on 2026-10-25

| Layer | Component | Grant (payload read first-hand) |
|---|---|---|
| **Platform connector** (pick the client's) | [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) 🇩🇪 · [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) 🇵🇱 · [`MauroDruwel/Smartschool-MCP`](https://github.com/MauroDruwel/Smartschool-MCP) 🇧🇪 · [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) 🇸🇰 · [`CarlSvejstrup/dtu-learn-mcp`](https://github.com/CarlSvejstrup/dtu-learn-mcp) 🇩🇰 · [`Kretiandpleti/skola-24-haos-integration`](https://github.com/Kretiandpleti/skola-24-haos-integration) 🇸🇪 | 🟢 **MIT** · 1 069–1 090 B · digests in `agents/top.md` |
| **Registry / reference data** | [`DFE-Digital/get-information-about-schools`](https://github.com/DFE-Digital/get-information-about-schools) 🇬🇧 · [`hyunbinseo/neis-school-info`](https://github.com/hyunbinseo/neis-school-info) 🇰🇷 | 🟢 **MIT** · `LICENCE` 1 116 B · `e18299fd1942` / 1 068 B · `e82e1769aaaf` |
| **Curriculum authority** | [`oaknational/oak-curriculum-api`](https://github.com/oaknational/oak-curriculum-api) 🇬🇧 | 🟢 **MIT** · 1 077 B · `0eeb9d32caed` |
| **Agent runtime** | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 **Apache-2.0** · 11 357 B · `c71d239df917` |
| **Teacher-facing capability** | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) (ships its own evals) · [`oaknational/oak-ai-lesson-assistant`](https://github.com/oaknational/oak-ai-lesson-assistant) | 🟢 **Apache-2.0** 11 357 B · `58d1e17ffe51` / 🟢 **MIT** 1 077 B · `d150aadcccd2` |
| **Assessment evidence** | [`kit-sdq/autograder`](https://github.com/kit-sdq/autograder) (explainable, check by check) · [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) (academic integrity) | 🟢 **MIT** · 1 068 B · `30a0bc0d48b4` / 1 084 B · `881163366572` |
| **Eval gate** | [`Teachable-AI-Lab/tutor_gym`](https://github.com/Teachable-AI-Lab/tutor_gym) · [`shuangyan123/tutorbench`](https://github.com/shuangyan123/tutorbench) | 🟢 MIT / Apache-2.0 (code) — see `repos/foundations.md` Tier 9 |
| **Obligation check** (dates) | [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | 🟢 **MIT** 1 073 B · `b7b08f330649` @ `41da87feb238` — `engine.js:32` encodes Annex III = **2027-12-02** citing Reg. (EU) 2026/1744 |
| **Obligation check** (codebase scan) | [`ark-forge/mcp-eu-ai-act`](https://github.com/ark-forge/mcp-eu-ai-act) | 🔴 **MIT** 1 065 B · `002af8f9b59c` — scanning only. **`p437`: its encoded deadline is the superseded `2026-08-02` and is test-pinned — do NOT take dates from it** |

### How it wires together

1. **Pick the connector by the client's platform, not by preference.** One of the six rows
   above, or Moodle/Canvas from `verticals/solutions.md` if that is what they run. The
   connector is read-only on first delivery — `iserv-mcp`'s single write tool
   (`mark_parentletter_read`) stays disabled until step 6.
2. **Pin the connector.** Every one of these is an *unofficial* client; fork it and pin the
   commit named in `agents/top.md`. 🔴 Do not depend on the upstream default branch for a
   system of record.
3. **Resolve the institution against the registry.** GIAS in England, NEIS in Korea; the
   school's URN or code becomes the tenancy key for everything downstream. Without this the
   deployment has no stable identifier for "which school".
4. **Anchor content to the curriculum authority** where one publishes — Oak's API for
   England. 🟢 `Trend 11` says jurisdictional curriculum content is the defensible layer;
   this is how you get it without licensing it.
5. **Run the teacher-facing capability only.** Lesson planning, differentiation, marking
   support, administration. 🔴 **No student-facing generative surface in phase 1** — see the
   age gate below.
6. **Gate every write behind the staged artefact.** Draft → named human → recorded
   approval → write. This is `Pattern AH`'s draft-and-sign, unchanged, and it is what makes
   the connector's write tools safe to enable.
7. **Ship the evidence pack with the build**, not after it: `tutor_gym` / `tutorbench` for
   the capability, `autograder`'s per-check output for the marking claim, `dolos` for the
   integrity question the buyer will ask.

### 🔴 The six things that will bite, named up front

1. 🔴 **Every connector is unofficial, and the READMEs say so.** `iserv-mcp` warns that
   instances differ and to test against the school's own installation; `dtu-learn-mcp` is a
   student project and tells you to use it with your own account only. **No API stability
   promise, no vendor escalation path.** Price a connector-maintenance line into the
   engagement; it is not a one-off integration.
2. 🔴 **An age gate is a hard requirement in two jurisdictions and a design requirement in
   all of them.** Norway prohibits generative AI for grades 1–7 from the start of the
   2026–27 school year and permits grades 8–10 only under direct teacher supervision;
   NYCPS has a 2K-8 moratorium. 🟢 `Trend 32` has the requirement table — a per-learner
   grade band enforced at the model boundary, plus **supervision mode as a distinct runtime
   state**, not a UI toggle.
3. 🔴 **The age gate needs the learner's age, which is new PII exposure.** Take the band
   from the roster system of record, never infer it, never persist it past the session, and
   never send it to the model provider. A compliance feature that creates a data-protection
   breach is the most common way this build fails its own audit.
4. 🔴 **Student credentials are the connector's authentication model.** Most of these clients
   authenticate as the *user* — a student's or parent's own login. 🔴 **An institutional
   deployment cannot hold those**, so phase 1 is teacher-account scoped and any
   student-scoped feature needs the platform vendor at the table, which returns you to
   point 1.
5. 🟡 **Germany has no federal buyer.** Education is *Länder* competence and there is no
   federal school AI strategy; sixteen Länder are sixteen procurements. 🟢 Name the Länder
   programme in the pitch — **AI4Teachers** (Rhineland-Palatinate, multiplier model) or
   Bavaria's 15 model schools — because that is the budget line that already exists.
6. 🟡 **The EU obligation clock is not the delivery clock.** Annex III for stand-alone
   education AI runs to **2 December 2027**; Article 50 transparency has applied since
   **2 August 2026**. 🔴 A teacher-facing build in scope of Article 50 has a *live*
   obligation today, which is the half that gets forgotten.

### 🟢 Why the proposal is stronger than a platform build, in one line each

- **The client's own ministry already published the code.** Udir's exam administration
  (Apache-2.0), three DfE services (MIT), Oak's curriculum API and lesson assistant (MIT) —
  a proposal can cite the buyer's own repositories rather than a vendor's case study.
- **Nothing is replaced**, so there is no migration risk line to argue away.
- **Every component is permissive**, so the derivative ships without a copyleft conversation
  — which is not true of any Moodle-based alternative.
- **The teacher-facing scope clears an age restriction by construction**, so Norway's
  prohibition and NYCPS's moratorium are not objections to be managed.

### Shape and duration

| phase | weeks | output |
|---|---|---|
| 0 — address audit (`Pattern Z`) + connector selection | 1 | the six-row table narrowed to one, pinned at a commit |
| 1 — registry + curriculum anchoring | 2 | institution resolved, curriculum reachable, tenancy key fixed |
| 2 — teacher-facing capability + eval gate | 3–4 | the capability and the evidence pack that scores it |
| 3 — age gate + supervision mode + PII review | 2 | `Trend 32`'s requirement table satisfied and reviewed |
| 4 — write path behind draft-and-sign | 2 | connector write tools enabled, approvals recorded |
| **total** | **10–11 weeks** | a permissive agent layer over the platform the client already runs |

🟡 **What this pattern does not claim.** It is a *teacher-facing* build. A student-facing
tutor over a national platform is a different engagement with a different legal surface, and
in Norwegian primary education from late August 2026 it is **not available at all**.

## 🆕 Pattern AL — `p432` The IEP drafting assistant that is **not** a system of record (the one NA special-education engagement that is legal by construction)

**Why this pattern exists.** `Pattern AH` establishes draft-and-sign as the architecture that
satisfies US state law, the EU AI Act and Vietnam's decree at once. Special education in North
America is where that architecture stops being good practice and becomes the **statutory
requirement**: IDEA and §504 make the IEP a legal instrument, Oklahoma and Maryland bar AI as the
sole basis for a high-stakes student decision, and Charleston County names special-education
determination explicitly. `Trend 28` shows this is simultaneously the thinnest-supplied surface in
the whole industry — so this is a build with no incumbent, not an integration.

### The stack, with the grant on every piece — all read at HEAD on 2026-10-25

| Layer | Component | Grant (payload, read at HEAD) | Why this one |
|---|---|---|---|
| Knowledge + boundary | [`robotros/California-IEP-AI-project-kit`](https://github.com/robotros/California-IEP-AI-project-kit) | **MIT** · `LICENSE` 1 064 B · `2524a8e74f10` @ `ff1ae0ce30e7` | Two pinned roles (CA Essential Standards analyst; IEP goal generator), Light (3 md) / Full (8 md) editions, CDE-sourced, with the "no autonomous student-record action" boundary written into its own README. |
| Deployment shell | [`67tallchris/iep-builder`](https://github.com/67tallchris/iep-builder) | **MIT** · `LICENSE` 1 068 B · `523f156051cf` @ `b39df0e9a4a1` | Svelte + Cloudflare Pages Functions + D1, **bring-your-own-key**. A per-district instance that holds no vendor key and no central student store. |
| Draft-and-sign engine | [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp) | **MIT** · `LICENSE` 1 076 B · `2bcdae923d26` | Already produces a draft-for-review **by default**. Reuse its review-state machine; retarget the artefact from a grade to an IEP goal set. |
| Review-state audit trail | [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | **MIT** · `LICENSE` 1 069 B · `297c4cba7b33` @ `b90bd88a2899` | Raises each artefact as a `WAITING_REVIEW` task and **records the approve/reject decision**. This is the enforcement `robotros`' kit declares in prose but does not implement. |
| Progress monitoring | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) + [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** / **MIT** | An IEP goal needs *measurable* progress. BKT/DKT gives a non-LLM, auditable model of mastery — defensible to a district in a way an LLM's opinion is not. |
| Parent-facing layer | [`dougdevitre/access-to-education`](https://github.com/dougdevitre/access-to-education) | **MIT** · `LICENSE` 1 068 B · `68657618a157` @ `f8abd70707ba` | ~120 k words of IEP navigation, family–school communication and advocacy content, MIT-granted. Serves `Trend 10`'s unserved parent persona from the same deployment. |
| Offline marking | [`rwrife/rubric-desk`](https://github.com/rwrife/rubric-desk) | **MIT** · `LICENSE` 1 062 B · `ec0b7dad19a4` @ `010a44006014` | Optional. Where staff mark away from connectivity. 🟡 Created 2026-10-25 — fork it. |
| Differentiated delivery | [`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) | 🔴 **AGPL-3.0-or-later** · `LICENSE` 35 441 B · `d8d2ea7ef0a1` @ `6194e51e8f1f` | Optional, and **over HTTP only**. UDL/WCAG/AAC/TTS differentiation. Network copyleft over a hosted engine: never vendor, never link, never fork into the deliverable. |

**Seven MIT pieces and one deliberately quarantined AGPL one.** No component in the required path
carries a copyleft obligation.

### How it wires together

1. **Pin the jurisdiction first.** Load the `robotros` Full edition (8 knowledge files) for
   California, or re-author it against the state's own standards authority for anything else. The
   kit is a *template for jurisdiction pinning*, not a national answer — Arizona's `iep-builder`
   exists separately for the same reason.
2. **Stand up the shell per district.** `iep-builder`'s Cloudflare + D1 + BYOK shape, so the key
   belongs to the district and the data never transits a studio tenant.
3. **Take an authorised, de-identified baseline.** The kit requires this and warns that typed
   redaction is *not* de-identification — so de-identify in the pipeline, not in the prompt.
4. **Generate a draft goal set, never an entry.** Reuse `canvas-grader-mcp`'s draft default.
5. **Enforce the boundary in code.** Wrap every artefact in `AI-Teaching-Agent`'s
   `WAITING_REVIEW` task with a recorded approve/reject and reviewer identity. 🔵 **This step is
   the pattern.** Without it you have shipped `robotros`' disclaimer, not its discipline.
6. **Write nowhere.** The authorised commercial system of record (PowerSchool Special Programs,
   Frontline, SEIS) receives the signed output by human action. There is no open-source
   special-education system of record — `verticals/solutions.md` — so the constraint is forced, and
   it happens to be the compliant design.
7. **Monitor progress with a model you can show.** OATutor + pyKT for mastery estimates against
   each goal; an LLM narrative *on top of* those numbers, never instead of them.
8. **Serve the parent from the same instance** with the `access-to-education` corpus.

### 🔴 The six things that will bite, named up front

1. **No evaluation exists for this category.** `p431`'s tutor-evaluation tier (`tutor_gym`,
   `tutorbench`) does not score IEP goal quality, and no IEP benchmark surfaced. **Budget to build
   the eval**, and say so in the proposal — a quality claim here is currently unprovable with open
   tooling.
2. **Every component is a seed.** 0, 0 and 1 star; two created within eleven days of this pass; no
   second contributor anywhere. Fork and own, pin to the SHAs above, and price maintenance in.
3. **`robotros`' kit is prose, not a runtime.** No model is named and nothing enforces its
   boundary. Step 5 is the billable core; a client who thinks they are buying the kit is mistaken.
4. **FERPA is not certifiable by any component here**, and the kit says so explicitly. The
   authorisation path is a client-side legal workstream running in parallel — surface it in week 1,
   not at UAT.
5. **AGPL contamination risk is concentrated in one optional step.** If `AlloFlow` is adopted,
   hold it behind a network interface and write the boundary into the architecture document. The
   temptation to fork "just the differentiation bit" is how AGPL enters a deliverable.
6. 🆕 `p433` **THE JURISDICTION CHECK IS NOW THE FIRST GATE, AND NEW YORK CITY IS WHY.** This
   pattern assumes draft-and-sign is sufficient because no US rule bars an AI *draft* of an IEP —
   only AI as the *sole basis* for the decision. 🔴 **That assumption is no longer safe
   everywhere.** NYC Public Schools' **March 2026 preliminary** guidance was reported to place
   **"development of special education and 504 plans"** on its **red / prohibited** tier — not
   "not the sole basis", but prohibited. NYC then **enacted** a student-facing generative-AI
   moratorium for 2026-27 (2026-09-02, grades 2K-8, ~600,000 students). 🟡 **Whether the
   plan-development prohibition survived into the enacted policy could not be established**
   (`Gap 433-B`), and the enacted text that *is* quoted names IEP/504 only as an **exemption**
   from the ban for assistive technology — the opposite direction.
   🔵 **So the instruction is procedural, not a verdict.** Do not pitch this pattern into a
   district until its own rule is read: in the largest US district the answer may be *prohibited
   outright*, which no amount of human-sign-off architecture cures. Week 1's "jurisdiction pinning"
   (below) stops being a formality and becomes a **go/no-go**: pin the district's own AI policy,
   not just the state statute, and get the red-tier list in writing. **Charleston County and NYC
   are now two independent NA districts naming special education explicitly** — treat
   district-level prohibition as the base case to disprove, not the edge case.

   🔴 🆕 `p434` **ANSWERED, AND THE ANSWER IS THE RESTRICTIVE ONE: IN NYCPS THIS PATTERN'S CORE
   STEP IS PROHIBITED.** `Gap 433-B` is **closed**. The current NYCPS *Guidance on Artificial
   Intelligence and Screen Time* carries a **"Red: Do Not Proceed"** tier in its Traffic Light
   Approach, and that tier names **IEP and 504 plan development** with the operative sentence
   *"All special education documents are developed by qualified professionals"*, citing **IDEA**
   and **Chancellor's Regulation A-710**. A second independent outlet states that educators may
   not use AI in grading, care and counselling, behavioural monitoring, **or crafting IEPs or 504
   accommodations**. 🔵 **Two secondaries, consistent; no primary read — `Gap 433-C`'s ceiling
   applies** (`schools.nyc.gov` is 403 at this host's egress).

   🟢 **And the apparent contradiction `p433` could not resolve was never a contradiction — it is
   a SCOPE distinction, which is the part to carry into a client conversation.** The two clauses
   govern different subjects:

   | Instrument | Subject | Effect on an IEP |
   |---|---|---|
   | Red tier, Traffic Light Approach | **Staff** use of AI to *develop* the document | 🔴 **Prohibited** — a qualified professional develops it |
   | 2K-8 moratorium **exemption** | **Student-facing** assistive technology delivered *under* an existing IEP/504 | 🟢 **Exempt** from the ban — it may continue |

   🔵 So the exemption permits *delivering* accommodations a plan already grants; it says nothing
   about *writing* the plan, and the red tier forbids that. `p433` read an exemption for one
   subject as evidence about the other.

   🔴 **The consequence for this pattern, stated without softening.** In NYCPS, `Pattern AL`'s
   step 4 — *"generate a draft goal set"* — is **the prohibited act**, not a safe-harbour version
   of it. Draft-and-sign does **not** cure it, because the rule is addressed to who may *develop*
   the document rather than to who may *approve* it. 🟢 **What remains sellable in NYCPS** is the
   non-drafting surface of this same stack, and it is not small: progress monitoring (OATutor +
   pyKT against existing goals), the parent-facing `access-to-education` layer, and
   accommodation *delivery* under an already-signed plan — all three sit outside the red tier and
   the third is explicitly exempted. 🔵 **Sell the stack minus step 4**, and say why in the
   proposal rather than letting a district's counsel find it.

   🔴 **Second NA procurement fact from the same leg, and it gates timing rather than scope.** The
   NYCPS chancellor directed principals to **pause all educational-software purchases** pending
   updated AI guidance. For the largest US district the near-term motion is therefore a
   **no-cost pilot or a standards conversation**, not a purchase order — price the engagement
   accordingly instead of forecasting a close.

### Shape and duration

**10–14 weeks** to a district pilot: 2 weeks jurisdiction pinning and authorisation path, 3 weeks
shell + draft-and-sign enforcement, 3 weeks progress monitoring, 2 weeks parent layer, 2–4 weeks
evaluation build and review cycles. 🔵 Longer than `Pattern AJ` (evidence-gated tutor pilot)
because there is no incumbent base to start from — which is also why there is no incumbent vendor
to displace.

🔴 **Where this pattern does NOT apply.** It is US-shaped. England's EHCP process and the
inclusive-education mandates of Brazil, Chile and Colombia have **no open-source tooling at all**
(searched this pass; nil result). Outside North America this is a from-scratch build with the
`robotros` kit as a structural reference only.

---

## 🆕 Pattern AM — `p433` The **teacher-facing courseware factory**: the build that is legal in NYC *because* no student ever touches the model

**Why this pattern exists.** `Trend 30` establishes that the binding US rule is now the
**district's**, and that the districts prohibit by **grade band** and by **who faces the model**:
NYC bars student-facing generative AI in grades 2K-8 and companion chatbots in *every* grade, while
**explicitly retaining teacher-facing AI for lesson planning and translation**. Katy ISD draws the
same kind of line at grade 6. 🟢 **That is not a constraint to work around — it is a specification.**
A system whose only user is a teacher, and whose output is courseware a human approves before any
student sees it, is sellable into the single largest US district *today*, in the grade bands where
every student-facing product is currently barred. It is also, by construction, outside EU AI Act
Annex III: it neither scores a student nor determines access to education.

### The stack, with the grant on every piece — all read at HEAD on 2026-10-25

| Role | Component | Grant | HEAD | Payload |
|---|---|---|---|---|
| Authoring chain (the core) | [cabbage2000-lab/textbook-writer-skills](https://github.com/cabbage2000-lab/textbook-writer-skills) | **MIT** | `e2b825072ba5` | `LICENSE` 1 064 B · `0d5a33d13ca9` |
| Source-material ingest | [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | **MIT** | `f8849746d85c` | `LICENSE.md` 1 122 B · `15ce43afa44a` |
| STEM grounding (physics) | [122-syf-wcy/PhysicsOS](https://github.com/122-syf-wcy/PhysicsOS) | **Apache-2.0** | `a25c6ee26583` | `LICENSE` 11 356 B · `f1a2e5fccede` |
| Orchestration | [huggingface/smolagents](https://github.com/huggingface/smolagents) | **Apache-2.0** | `96f33faaf028` | `LICENSE` 11 357 B · `c71d239df917` |
| Delivery base — AI *inside* | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | `d073ad444fe5` | `LICENSE` 10 982 B · `6dbc5b605ed0` |
| Delivery base — offline/equity | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | `44a4e68aac3e` | `LICENSE` 1 097 B · `3c056b34a476` |
| Delivery base — Open edX client | [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** | `c73c4bb42aa7` | `LICENSE.TXT` 11 358 B · `cfc7749b96f6` |
| Did it work? | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `ccbaf37b07e3` | `LICENSE` 1 066 B · `f5f955194636` |
| Regression on prompt change | [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | **Apache-2.0** (code) | `f9d69c7ce3e1` | `LICENSE` 11 358 B · `cfc7749b96f6` |

🟢 **Nine components, nine permissive grants, zero copyleft in the required path** — and no
quarantined AGPL step at all, unlike `Pattern AL`. This is the cleanest licence position of any
pattern on this file.

### How it wires together

1. **Ingest** — teacher drops the syllabus, textbook chapters, slide decks and standards documents
   into `learn-from-materials`. It produces a **traceable** knowledge base: every extracted claim
   keeps a pointer back to the source page. **Keep that traceability; it is the audit artefact**
   that answers "where did this lesson come from?" later.
2. **Author** — `textbook-writer-skills` runs its gated UbD chain over that KB: teaching
   positioning → five-part gate → chapter-tree gate → four-stage chapter writing → review. 🟢 **Do
   not remove its gates.** Its verify-or-flag behaviour — recompute STEM claims, check humanities
   citations word-by-word, emit *"needs author confirmation"* where it cannot verify — is the
   single most valuable property in the stack, because it converts the model's uncertainty into a
   teacher's task queue instead of into confident prose.
3. **Ground the STEM** — for physics, route generated worked examples through `PhysicsOS`: the
   physics engine **executes** the scenario, so a wrong number is caught by simulation rather than
   by a reviewer's eye. This is the only component in this base that can falsify its own output.
   🔵 Physics only; there is no equivalent for chemistry or biology (see the limits below).
4. **Orchestrate** — `smolagents` holds the chain. Two reasons over a heavier framework: it is
   minimal enough that the gate logic stays legible in review, and it is **EU-domiciled**, which is
   a procurement answer in EMEA rather than a technical one.
5. **The approval gate — this is the pattern, not a step in it.** Nothing reaches a learner until a
   named teacher approves it. Store approver identity, timestamp, the model and version used, and
   the diff between generated and approved text. **This record is the product** in a district that
   must show AI did not decide anything.
6. **Deliver** — publish approved courseware into the base: **OpenOLAT** when the client needs a
   full LMS and can take the AI layer *inside* the platform (the only Apache-2.0 LMS, so this is
   lawful); **Kolibri** where connectivity or equity is the constraint; an **XBlock** component
   when the client is already on Open edX and the Apache-2.0 seam keeps your code out of the
   platform's AGPL reach.
7. **Measure** — `pykt-toolkit` over the resulting activity data for knowledge tracing, so the
   claim "this courseware worked" is defensible rather than rhetorical. `tutorbench` as the
   **regression** harness: re-run it on every prompt or model change, because a silent quality
   regression in a courseware factory ships to every class at once.

### 🔴 The four things that will bite

1. **`textbook-writer-skills` is 37 ★ with 12 forks and no second maintainer.** Fork it, pin
   `e2b825072ba5`, and price maintenance in. Its gates are the asset; a fork that strips them to
   "go faster" deletes the reason to choose it.
2. **`learn-from-materials` carries an author-key flag.** Its MIT payload names
   `Copyright (c) 2025 virgiliojr94` while the owner is `dmoshehun-prog` and the repository was
   created 2026-09-08. **The MIT grant stands** — but before vendoring into a client deliverable,
   raise it with the maintainer and record the answer. `agents/trending.md` `p433` has the detail.
3. **`PhysicsOS` grounds physics and nothing else.** Do not generalise its guarantee. For
   non-physics STEM the stack is back to `textbook-writer-skills`' recompute-or-flag, which is
   honest but weaker. Say which subjects are grounded in the proposal.
4. **Copyright of the *source* material is the client's problem and it will land on you.** Ingesting
   a commercial textbook into a KB and generating derived courseware is a licensing question about
   the textbook, not about any component here. Surface it in week 1. 🔵 This is the one risk in
   this pattern that no licence read on these shelves can clear.

### Shape and duration

**6–8 weeks** to a teacher-piloted factory: 1 week ingest and traceability, 2 weeks authoring chain
and gate tuning against the client's standards, 1 week STEM grounding where applicable, 1 week
approval workflow and audit record, 1–2 weeks delivery into the chosen base, 1 week measurement
wiring. 🟢 **Shorter than `Pattern AL` (10–14 weeks) for a structural reason**: there is no
jurisdiction go/no-go to clear first, because teacher-facing-with-human-approval is the lane the
restrictive districts *left open on purpose*.

🔵 **Where this pattern is the wrong answer:** a client who wants a student-facing tutor. Say so
plainly and move them to `Pattern AJ` or `Pattern AI` — and tell them which grade bands they can
sell it into, which in NYC today is high school only, and never as a companion chatbot.

## 🆕 Pattern AJ — `p431` The evidence-gated tutor pilot (the deliverable that survives a board review in NA, EMEA and APAC)

**The problem it solves.** Every tutoring pilot this base can already build stalls at the same
question: *how do you know it teaches well?* Until this pass there was no permissive answer — the
scorer was either a closed vendor or an ungranted academic benchmark. There is now. This pattern
ships the **evidence**, not the tutor, and the tutor rides along.

### The stack, with the grant on every piece — all read at HEAD on 2026-10-25

| Layer | Component | Grant | HEAD |
|---|---|---|---|
| Tutoring runtime | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | `e24c8456e5f7` |
| Evaluation fixture | [`Teachable-AI-Lab/tutor_gym`](https://github.com/Teachable-AI-Lab/tutor_gym) | **MIT** | `772f5cdca5dd` |
| Regression engine | [`shuangyan123/tutorbench`](https://github.com/shuangyan123/tutorbench) | **Apache-2.0** (code) | `f9d69c7ce3e1` |
| Mastery measurement | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `ccbaf37b07e3` |
| Human-sign-off surface | [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | **MIT** | `b90bd88a2899` |
| LMS seam (if Open edX) | [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | `c73c4bb42aa7` |
| Offline delivery (if needed) | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | `44a4e68aac3e` |

**Permissive end to end.** No GPL, no AGPL, no ungranted code. The client owns the deliverable.

### How it wires together

1. **Fork `tutor_gym` on day one.** Its last commit is 2025-09-10; treat it as a fixture you now
   maintain, not a dependency you track. Pin the fork SHA in the client's repo.
2. **Stand up `OATutor` as the tutoring runtime** and point `tutor_gym`'s `oatutor` backend at it:
   `python llm_tutor_eval.py --tutor-kind oatutor --profile oa_compl-aug.prof --model <model>`.
   This is the step that normally costs adapter work and here costs none — the binding already exists.
3. **Run the *student* direction too** (`llm_stu_eval.py`). A simulated-learner run is what produces
   a defensible claim about *learning* rather than about *answer quality* — and it is the half most
   pilots skip.
4. **Wrap the scored runs in `tutorbench` as a regression suite.** This is the piece that makes the
   evidence *durable*: when a prompt, model or curriculum changes, the same scenarios re-run and the
   diff is the artefact. Wire it into CI as a merge gate.
5. **Ground mastery claims in `pykt-toolkit`** (BKT/DKT) rather than in model self-report, so the
   adaptivity claim is a measurement, not a narrative.
6. **Route every student-affecting output through `AI-Teaching-Agent`'s `WAITING_REVIEW` queue**, so
   each action carries a recorded human approve/reject. That record is the oversight evidence.
7. **Deliver the evidence pack**: scored baseline, simulated-learner results, regression suite in CI,
   human-sign-off log, and the licence read for every component.

### Why the same artefact clears three jurisdictions

| Region | What it is asked for | Which step answers it |
|---|---|---|
| **North America** | Oklahoma / Maryland: no high-stakes AI decision without human oversight; district board review | Step 6 (sign-off log) + step 7 (scored baseline) |
| **EMEA** | Article 50 transparency **from 2 Aug 2026**; Annex III conformity by **2 Dec 2027** (Reg. (EU) 2026/1744) | Steps 4 and 7 — the regression suite is the start of the conformity file |
| **APAC** | Vietnam's high-risk list names automated assessment (obligations **1 Mar 2027**); Korea's AI Basic Act **in force 22 Jan 2026** | Steps 3, 4 and 6 |
| **LATAM** | UNESCO IESALC: 87% adoption, 26% with a strategy — the governance gap | The whole pack, sold as assurance attached to the platform (`Trend 21`) |

### 🔴 The four things that will bite, named up front

1. **`tutor_gym` is 13.5 months stale.** Budget the fork in week 1. Do not present it as maintained.
2. **`tutorbench` is three licences, not one.** Apache-2.0 for the engine, **CC-BY-4.0 for the
   scenario content** (attribute it), and a **brand policy** over the name — keep “TutorBench” off
   the client's product and marketing.
3. **The harnesses are English-first** (`Gap 431-A`). For LATAM and APAC, **scope scenario
   translation as a line item**. The CC-BY-4.0 content grant makes re-authoring lawful; it does not
   make it free.
4. **This pattern scores tutoring, not grading** (`Gap 431-C`). If the client's real exposure is
   assessment — and under NA, EMEA and APAC statutes it usually is — **say so explicitly in the
   proposal** and scope a bespoke rubric harness. Do **not** reach for
   [`sdrangan/llmgrader`](https://github.com/sdrangan/llmgrader): its licence forbids commercial use.

### Shape and duration

**6–8 weeks** for a single-subject pilot with the evidence pack, assuming the client already runs an
LMS. Add **2–3 weeks** for scenario localisation outside English. The fork of `tutor_gym` is a
permanent maintenance line to hand over at the end, and the proposal should say so.

## 🆕 Pattern AH — The draft-and-sign grader (the one architecture that satisfies NA, EMEA and APAC at once)

**The problem.** Three regulatory regimes independently converged on the same requirement,
by different routes: Oklahoma and Maryland prohibit AI as the **sole basis** for high-stakes
student decisions; the EU AI Act classes **grading** as high-risk (now due 2 Dec 2027 under
Regulation (EU) 2026/1744); Vietnam's decree names **automated assessment** high-risk with
March 2027 compliance. One architecture satisfies all three — and it is cheaper than the
autonomous version, not more expensive.

**The recipe.**

| Layer | Component | Licence (verified @ 2026-10-25) | Why this one |
|---|---|---|---|
| Grading agent | [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp) | MIT · `c47e8b3ac2ae` | **Emits a draft for human sign-off by default.** The compliance artefact is the default behaviour, not a bolt-on. |
| LMS seam (Canvas) | [`semyonfox/canvas-mcp`](https://github.com/semyonfox/canvas-mcp) | MIT · `e317c4b7bf10` | Broader Canvas surface when the grader alone is too narrow. |
| LMS seam (Open edX) | [`openedx/XBlock`](https://github.com/openedx/XBlock) | Apache-2.0 · `c73c4bb42aa7` | Keeps your code out of AGPL reach. |
| LMS seam (Google Classroom) | [`vTanco/google-classroom-mcp`](https://github.com/vTanco/google-classroom-mcp) | MIT · `9ba0070eff2f` | 🔴 **Use this address, not `pengusto`'s** — see below. |
| Defensible scoring | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | MIT · `ccbaf37b07e3` | A knowledge-tracing model you can show a regulator, behind the LLM's prose. |
| Agent runtime | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | Apache-2.0 · `96f33faaf028` | Minimal, EU-domiciled. |

**Wiring.** Agent proposes score + rationale → writes **draft** into the LMS via MCP →
instructor reviews in their normal grading UI → sign-off event is the audit record.
pyKT runs alongside to produce a mastery estimate that does **not** depend on the LLM, so
the score has a defensible basis when challenged.

🔴 **The trap this pattern exists to avoid:** `pengusto/google-classroom-mcp` was the
recommended Google Classroom lane in three earlier passes and **relicensed to proprietary
on 2026-10-23**, with a clause naming educational institutions as requiring a paid
agreement. The MIT bytes survive at `vTanco` (verified by digest equality, `a01639b20880`).
**Re-read every component licence at its SHA before an engagement commits.**

**Effort:** 6–8 weeks to a governed pilot on an existing Canvas estate.

## 🆕 Pattern AI — Offline-first tutoring where connectivity and equity are the constraint

**The problem.** Argentine AI use runs **75% in high-SES and 42% in low-SES** groups. A
cloud-dependent deployment widens a 33-point gap and the client will be measured on it.

**The recipe.** [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
(**MIT**, `44a4e68aac3e`) as the platform — the only MIT platform on the shelf and built
offline-first — with [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
(**BSD-3**, `196c547291da`) running local models through Ollama for the tutoring surface,
and [`satvik314/educhain`](https://github.com/satvik314/educhain) (**MIT**, `38adb1e9459d`)
generating localised Spanish/Portuguese content **ahead of deployment**, synced on the
occasional connection.

🟢 **Every component is permissive and every one runs without egress** — which is also the
data-residency story for LGPD (Brazil) and Ley 1581 (Colombia). No per-token cost is the
reason this survives a public-sector budget.

**Effort:** 8–10 weeks including content localisation.

---

## Pattern AG

### 🆕 `p408` — the India DPI engagement: MIT the whole way down, with the fork check as step 0

🔵 **When to reach for it.** An APAC/India engagement where the client is a state education
department, a DIKSHA-adjacent programme or a CBSE/NCERT-aligned private network, and the
requirement is in-country inference plus a permissive grant the client can extend without
publishing the extension. 🟢 This is the one stack on these shelves that is **MIT at every layer**.

**Step 0 — the fork-provenance check, and it is not optional here.**
🔴 `p408` found a fork of Sunbird documentation carrying **AGPL-3.0** while upstream is **MIT**,
returned *above* upstream by search. Before any Sunbird address enters a proposal, pin the grant to
the ref:
```bash
git ls-remote --symref https://github.com/<slug> HEAD          # the REAL default ref (Sunbird docs = dev, portal = master)
git clone -q --depth 1 --filter=blob:none --no-checkout https://github.com/<slug> r
git -C r cat-file -s HEAD:LICENSE                               # 1,072 B ≈ MIT · 34,520 B ≈ AGPL-3.0
git -C r fetch -q --depth=1000 origin "$(git -C r symbolic-ref --short HEAD)"
git -C r log --format='%h %cI %s' --follow -- LICENSE            # did the grant CHANGE, and in which direction?
```
🟢 The last line is the one `p404`'s gate exists for: **direction is only establishable from full
history**, and a byte-identical blob sha against upstream's pre-relicence blob proves *frozen*
rather than *re-licensed*.

**Step 1 — the platform.** [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal)
(`master`, 🟢 MIT) as the content-and-delivery spine, with
[`Sunbird-Ed/SunbirdEd-mobile-app`](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) (`main`,
🟢 MIT) where a handset is the real client. 🔴 **Budget the staleness, do not discover it:** 311 d
and 399 d since HEAD respectively. Fork at a pinned SHA, run the client's own dependency and CVE
sweep before week 1 ends, and price a maintenance line. 🔴 Do **not** name
`Sunbird-Ed/sunbird-learning-platform` in a deliverable — it does not resolve.

**Step 2 — the offline edge.** [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
(🔴 `develop`, 🟢 MIT) for low-connectivity districts, which is most of the addressable footprint
and already this shelf's most important repo for that constraint.

**Step 3 — the assessment layer.** [`Naitik-xd/CurriculumCraft-AI`](https://github.com/Naitik-xd/CurriculumCraft-AI)
(`main`, 🟢 MIT, HEAD **2026-10-03**) for CBSE/NCERT Grades 9–12 item generation. 🟢 Take its
*constraint* as the requirement, not just its code: it is built to generate without reproducing
verbatim NCERT text, which is the copyright exposure a client's counsel will actually ask about.
🔴 It is **public beta** and says so — wire it behind human review, never as the graded instrument.

**Step 4 — inference, in country.** `CurriculumCraft-AI` already targets **open-weight Gemma**, so
serve it locally rather than re-architecting: this is the APAC data-residency posture without a
sovereign-cloud contract.

**Step 5 — grounding, and the licence trap to avoid.** Use
[`crpf-mitadt/Indian-AI-for-Education`](https://github.com/crpf-mitadt/Indian-AI-for-Education) as
the **discovery index** for Indian ASR/TTS/OCR and translation assets. 🔴 **It is CC0-1.0 over the
document only** — every asset it names keeps its own grant, so each one re-enters at Step 0. Never
cite the index as the licence for anything inside it.

**Shape of the engagement.** 10–12 weeks: 1 week for Step 0 across every address plus the CVE
sweep; 4 weeks portal fork, pin and deploy; 2 weeks Kolibri edge sync; 3 weeks assessment layer
behind review; 1–2 weeks local-inference hardening.
🟡 **What this pattern does NOT give you:** multi-tenancy (no Sunbird row here claims it), a current
upstream to pull from, or a compliance story. For the last of those, Vietnam's Decision 33 and
Korea's `AI Basic Act` are the APAC instruments — see [`intel/market.md`](../intel/market.md) — and
India's own posture is a separate read this base has not closed.

## 🆕 `p406` — a standing existence check becomes a step in every pattern, and `Pattern C` gets a dated APAC variant

### 🟢 `Pattern Z` — the pre-engagement address audit, now a command rather than a habit

🔴 **Every pattern on this shelf names repositories, and 1.94 % 🔵 *(`p407`; `p406` published 2.20 %, counting 7 non-repositories as decay)* of the addresses this base carries do
not resolve.** Two of them are **inside a recipe on this very file**. 🟢 The check is now one command
and it needs no clone budget:

```bash
# offline: what the shelves name (no network)
make carried-existence-census                 # -> 2 682 addresses over nine shelves

# online: does each one still answer?  p293's control pair gates every verdict
make carried-existence-sweep                  # ~2.5 min at 12 workers, ~17 probes/s
WORKERS=6 make carried-existence-sweep        # throttling is retried serially, never
                                              # counted as decay
```

🔵 **Wire it as the first step of an engagement, before a single repo is cloned.** The channel is
`git ls-remote --symref`, so it costs **no object transfer** — which is why this is affordable where
`api.github.com` answers `403` on a scoped session and a clone-per-address does not fit any budget.

| what it returns | what to do with it |
|---|---|
| `EXISTS-PUBLIC` | 🟡 the address answers **today**; maintenance is a separate question (`p173`) |
| `EXISTS-NO-REFS` | 🔴 **an EMPTY repository.** It EXISTS and ships nothing — a 404 check passes and the dependency is still vapour |
| `ABSENT-OR-PRIVATE` | 🟡 absent, private **or MOVED** — probe a guessed successor before deleting a row |
| `CHANNEL-ERROR` | 🔵 says nothing about the slug. Retry serially; never read as decay |

🔴 **And the step this pattern must NOT skip: adjudicate by reading the sentence, not the verdict.**
All 12 unresolvable addresses on `agents/top.md` turned out to be **already documented as dead** —
cited as warnings and as specimens, not as recommendations. A sweep reads addresses, not prose
(`Gap 406-A`). 🟢 The realised loss on this base was **zero**; the instrument's value is that the
**next** one is caught the same hour rather than whenever a pass happens to clone it.

### 🟢 `Pattern AA` — repair a dead address instead of deleting the row

**Worked example, verified this pass end to end.**

```bash
# 1. the sweep flags it
grep -P '\tABSENT-OR-PRIVATE\t' evidence/carried-existence.2026-10-23-p406.tsv
#    apereo/opencast   ABSENT-OR-PRIVATE   -   agents/top.md;repos/foundations.md;...

# 2. probe guessed successors — the ORG move is the common shape
python3 -I compose/code/p293-slug-existence-oracle/slug_oracle.py --online \
        opencast/opencast apereo-opencast/opencast
#    EXISTS-PUBLIC   opencast/opencast        153d1b15c93afa5bf915ee31cdfec75ecfc5284e

# 3. read the grant at the pin — a successor's licence is NOT inherited from the row
git clone --depth 1 https://github.com/opencast/opencast /tmp/oc && head -3 /tmp/oc/LICENSE
#    Educational Community License, Version 2.0 (ECL-2.0)
```

🟢 **Result: a dead foundation row became a live one with its grant re-read**, and `repos/foundations.md`
already carried both the successor and a redirect row — so the repair was a **confirmation**, which is
the cheapest possible outcome. 🔴 **Step 3 is not optional:** `apereo/opencast` and `opencast/opencast`
are different licensors as far as this base is concerned, and ECL-2.0 is **not** on the MIT/Apache
shortlist a proposal usually prices against.

### 🟡 `Pattern C` variant — the APAC education compliance pack, priced to the RIGHT date

🔴 **This file's `Pattern C` and `intel/market.md`'s opportunity 5 both priced an education
engagement against Vietnam's `2027-03-01`. That is the all-other-sectors date.** 🟢 Education's is
**`2027-09-01`** for a system live before **2026-08-15**, and **`2027-03-01`** only for one deployed
inside the six months after Decision 33 took effect.

**The recipe, unchanged in parts and re-dated in one:**

| layer | what | why |
|---|---|---|
| **1 — system of record** | **Moodle** (GPL-3.0) or **Open edX** (AGPL-3.0); **OpenOlat** (Apache-2.0) or **Kolibri** (MIT) where copyleft is refused | 🟢 the **0 %-decay** tier — see `T83` |
| **2 — integration** | [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) *(MIT, npm)* or [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) *(MIT, crates.io)* — 🟢 **both re-probed `EXISTS-PUBLIC` this pass** | 🔴 the **5 %-decay** tier: pin a version and vendor the client, per `Pattern Z` |
| **3 — agent** | compose, don't adopt: LangGraph/CrewAI over the layer-2 tools | the volatile layer stays replaceable |
| **4 — conformity** | the **Annex III** pack from the EMEA engagement, re-mapped | 🟢 **portable** — EU → Vietnam → Mexico, adapts far cheaper than it rebuilds |

🔵 **The dated argument to a client, stated correctly:** a system **already live before 2026-08-15**
has until **2027-09-01**; a **new** one has **six months** from go-live under the post-Decision-33
clause. 🔴 **The cutoff has already passed**, so for any engagement starting now the six-month clause
governs — which is a *tighter* deadline than the one the old row quoted, reached by getting the law
right rather than by rounding toward urgency. 🟡 **Bound:** no primary text was read — every policy
host answers `ENOTFOUND` on this session — so this rests on five concurring law-firm readings.
Counsel confirms before it goes in a proposal.

### 🔵 One recipe step retired

🔴 `compose/patterns.md`'s step *"8. Re-check dead addresses. Four in common circulation do not
resolve…"* named **four** addresses and asked the reader to re-check them **by hand**. 🟢 Superseded
by `Pattern Z`: the population is **2 682**, not four, and the check is a make target.

---

## 🆕 `p405` — the layer-2 Moodle MCP choice was a GPL-or-vendor-a-commit decision, and it is not any more

🔴 **`p404` wrote this file's layer-2 decision tree and closed it with:** *"`peancor` is the only
permissive option measured here, and its **0 tags** means the pattern vendors a pinned commit rather
than tracking a release."* 🟢 **Refuted, with two addresses, both read first-hand from full clones on
2026-10-23.** 🔵 The reason `p404` could not see them is a method fact worth keeping: it measured the
slug **`moodle-mcp-server`**, and these are **`moodle-mcp`** — a different slug for the same
engagement question.

```
layer 2 of Pattern I (the network boundary), Moodle side — REVISED, pick by DEPLOYMENT not by grant:

  no Moodle-side install possible (no admin, no token, SSO/2FA in the way)
      -> falkenslab/moodle-mcp                MIT  1,067 B   npm @falkenslab/moodle-mcp
         Node + Playwright; drives a REAL BROWSER SESSION as the teacher
         + nothing to install in Moodle: no web-service token, no plugin, no administrator
         + ~230 tools; works on any Moodle 4.5 / 5.x the user can already log into
         + students pseudonymised to the model (A-7KQ2XM), de-aliased only on the operator's box
         + 6 tags v0.1.0..v0.5.0, 194 commits, HEAD 1 d        <- A PUBLISHED RELEASE
         - a browser session is a seat, not a service: it acts AS one teacher, not as the site

  Moodle Web Services available, and IT wants one binary to deploy
      -> G36maid/moodle-mcp                   MIT  1,064 B   crates.io moodle-mcp
         Rust (rmcp 3.5, edition 2024, Rust 1.88); single static binary, stdio
         + Moodle 3.7 -> 5.x via the mobile-app web service; CI + Codecov
         + 7 tags v0.1.0..v0.2.1, 163 commits, HEAD 3 d       <- A PUBLISHED RELEASE
         + SSO driver for NTUST, credentials mode verified at NTNU (Taiwan)
         - student-first tool surface: a teacher-side workflow needs the option above

  GPL-3.0 acceptable (internal tooling, or the client owns the deployment)
      -> lmscloud-io/moodle-mcp-server        GPL-3.0  35,148 B   Python/fastmcp
         + 3 tags; root commit by Marina Glancy (Moodle core provenance)
         - copyleft: it cannot sit inside a proprietary layer-3

  same Node runtime as ltijs / lti-tool, and MIT required
      -> peancor/moodle-mcp-server            MIT  1,064 B   TypeScript/Node
         - 0 tags: still vendor a pinned commit.  NO LONGER the only permissive option

  wire-up, all cases, unchanged:
      Moodle core_ai provider  ->  HTTP/MCP  ->  your layer-3 (retrieval, grounding, eval)
      ADORSYS-GIS/moodle-aiprovider_openaicompatible  is layer 1 (GPL, thin, contributed back)
```

🟢 **The decision axis changed, and that is the useful part.** `p404`'s tree branched on **grant**,
because grant was the only thing that distinguished the two addresses it had. 🔴 **With four options,
grant stops discriminating** — three of the four are MIT — and the question becomes *what can you
actually install on the client's Moodle?* 🔵 **Ask the client's LMS administrator one question before
choosing:** *can we have a web-service token?* A `no` eliminates two of the four options and makes
`falkenslab` the answer; a `yes` opens the Rust binary, which is the one a school IT department will
sign off on.

🟡 **A config line this pattern needs, same class as `p404`'s.** `falkenslab` runs a **browser session
as a real user**, so it inherits that user's permissions and **nothing narrows them server-side**.
🔴 The limits are enforced in the MCP server's own config, which means **the agent's blast radius is a
client-side setting**. 🟢 Pin it in the engagement's config, enable read-only or course-scoped mode
explicitly, and treat *"students are pseudonymised"* as a property to verify in the deployment rather
than to quote from the README.

### 🟢 New, concrete: picking an LMS MCP server when the client's LMS is NOT Moodle

🔴 **This file and [`verticals/solutions.md`](../verticals/solutions.md) have cited LMS MCP servers by
bare slug, and the slug is a name-collision group of up to 20 addresses.** 🟢 Measured
2026-10-23 — 42 addresses, 269 pairs — the heads are:

```
pick by the client's LMS; each line is a MEASURED family head, not the first search result:

  Canvas      -> vishalsachdev/canvas-mcp          MIT 1,071 B  1,089 commits  23 tags  1 d
                 + root-commit author of ELEVEN of the 20 Canvas addresses
                 ! do NOT clone bartmassey-upstream/canvas-mcp: the slug says upstream and
                   the root commit says fork (1,001 commits, DIVERGED-FORK)
                 ! r-huijts/canvas-mcp is a SEPARATE project (root 2024-12-12, Fontys NL),
                   61 commits, 3 tags, npm - keep it if you want the npm package, and know
                   that mdweaver/canvas-mcp is its 3-commit superset with 0 tags

  Blackboard  -> alanwtom/blackboard-mcp           MIT 1,065 B     26 commits   1 tag   1 d
              or felipedias-ie/blackboard-mcp      MIT 1,084 B     21 commits   3 tags  9 d
                 ! the largest Blackboard address is 28 commits: READ these, do not depend
                   on them.  Budget writing your own.
                 ! bibo242/blackboard-mcp shows 28 commits and is the ANCESTOR of
                   felipedias-ie - its extra commits are on refs unreachable from its HEAD

  Brightspace -> RohanMuppa/brightspace-mcp-server MIT 1,068 B    472 commits   6 tags  1 d
                 ! THREE of the four Brightspace addresses are this one author's lineage.
                   Price it as a single-maintainer dependency and say so in the SOW.
                   The only independent address is 7 commits, Apache-2.0, 374 d.

  Moodle      -> see the revised layer-2 tree above: TEN independent implementations,
                 the only genuinely uncollapsed supply of the four platforms.
```

🔵 **Why the "!" lines are the valuable part of this recipe.** Each one is a wrong clone a studio would
otherwise make from the search index: a fork named `upstream`, a 28-commit repository that looks newer
than its own descendant, and a four-address "ecosystem" that is one person. 🟢 Instrument, 12 controls
and all 269 graded pairs:
[`compose/code/p405-group-lineage/`](code/p405-group-lineage/README.md) ·
[`group-lineage.2026-10-23-p405.tsv`](../evidence/group-lineage.2026-10-23-p405.tsv).

---


## 🆕 `p404` — two recipes on this file named the wrong address, and the fix is one line each

🟢 **Both corrections come from full-history clones read on 2026-10-23**, with the instrument and its
9 controls at [`code/p404-fork-direction/`](code/p404-fork-direction/README.md).

| recipe cell | was | 🟢 **is** | why it matters to a build |
|---|---|---|---|
| **`Pattern I` layer 1** — the `core_ai` provider plugin | *"cloned from `ADORSYS-GIS/…` **or** `lmscloud-io/…`"*, described as two independent vendors | 🟢 **Clone [`ADORSYS-GIS/moodle-aiprovider_openaicompatible`](https://github.com/ADORSYS-GIS/moodle-aiprovider_openaicompatible)** — **8 d**, Moodle 5.0+ CI matrix, listed in the Moodle Plugins directory. `lmscloud-io` is its **origin** and is **93 d** | 🔴 *"Either"* sends half of engagements to a dormant address. The two are **one lineage** — `CONTENT-COPY`, direction `lmscloud-io` → `ADORSYS-GIS` — not a choice between vendors |
| **`Pattern` LTI/Go-JVM** — the Go options | `peregrine-lti` **679 d** and `macewan-cs/lti` **1,918 d** | 🟡 Add [`astiusa/lti`](https://github.com/astiusa/lti) — **794 d**, MIT, a **strict superset** of `macewan-cs` (89/89 commits reachable) | 🟢 The *conclusion* is unchanged — **do not put a client's identity flow on any of them** — but the file was 1,125 days out on the freshest permissive Go option, and that number is what a client challenges |

🟡 **A config line `Pattern I` now needs.** `ADORSYS-GIS` **dropped** `$plugin->supported = [500, 502]`
when it republished, keeping only `$plugin->requires = 2025041400`. 🔴 So the live plugin declares **no
Moodle upper bound** and Moodle will not warn on an untested major. 🟢 **Pin the Moodle version in the
engagement's own config** and treat the plugin's compatibility as unstated rather than open.

### 🟢 New, concrete: choosing a Moodle MCP server, which is an MIT / GPL-3.0 decision, not a name

🔴 **`moodle-mcp-server` is two independent implementations** — **0 shared commits AND 0 shared trees**
— and this base has cited the bare plugin name. The two differ in **language and in grant**, so the
name alone cannot carry a recommendation:

```
layer 2 of Pattern I (the network boundary), Moodle side — pick by grant, not by name:

  proprietary or MIT/Apache deliverable
      -> peancor/moodle-mcp-server          MIT  1,064 B 845ac6ac9e57   TypeScript/Node
         + same runtime as ltijs / lti-tool, so one Node service carries LTI *and* MCP
         - 0 tags: vendor a commit, do not "install" it; 243 d, so budget maintenance

  GPL-3.0 acceptable (internal tooling, or the client owns the deployment)
      -> lmscloud-io/moodle-mcp-server      GPL-3.0 35,148 B 8b1ba204bb69  Python/fastmcp
         + 3 tags v1.0.0..v1.0.2 - the ONLY published artefact of the two
         + root commit by Marina Glancy (Moodle core provenance) - read it either way
         - copyleft: it cannot sit inside a proprietary layer-3

  wire-up, both cases:
      Moodle core_ai provider  ->  HTTP/MCP  ->  your layer-3 (retrieval, grounding, eval)
      ADORSYS-GIS/moodle-aiprovider_openaicompatible  is layer 1 (GPL, thin, contributed back)
```

🟢 **The boundary is what makes this a free choice**: GPL-3.0 is not network copyleft, so a GPL layer-2
MCP server still leaves layer 3 ownable — 🔴 but only if the client accepts shipping a GPL component at
all. 🔵 Where they will not, `peancor` is the only permissive option measured here, and its **0 tags**
means the pattern vendors a pinned commit rather than tracking a release.

---

## 🆕 `Pattern I` — 🆕 `p403` The India engagement: an in-language tutor you can actually *prove*, with a deterministic eval gate

🔵 **The engagement this answers.** India's mandate makes **AI and computational thinking compulsory
from Class 3 from the 2026–27 academic year** (see [`intel/market.md`](../intel/market.md) → APAC). A
ministry or large-group client will ask for a tutor in Hindi and at least one other state language. 🔴
**The thing that sinks these pitches is not the tutor — it is being unable to demonstrate that the
tutor is correct in a language the buyer's own reviewers read.** An English benchmark plus
*"the model is multilingual"* is not evidence, and an LLM-judge score is not evidence a reviewer can
re-run.

🟢 **What `p403` makes newly possible:** the eval half is now available, permissive, in-language and
**rule-based**, so it runs in CI and returns the same number to the client as it does to you.

### The stack, with the grant on every piece

| role | component | grant | why this one |
|---|---|---|---|
| **Tutor runtime** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | Lifelong learner memory + RAG grounded in the learner's own uploaded materials; the largest education-native permissive base on these shelves. Apache-2.0 keeps the patent grant a government buyer's counsel will look for. 🔵 Swap in [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) (🟢 **MIT**) instead **if** the client wants generated whole-classroom delivery and central model governance — see `Pattern Q`. |
| **🆕 Eval gate (the new piece)** | [`AI4Bharat/IndicIFEval`](https://github.com/AI4Bharat/IndicIFEval) | 🟡 **MIT** code · **`CC-BY-4.0`** dataset | **14 Indic languages + English**, verifiable **rule-based** constraints, bundled `lm-evaluation-harness`. 🟢 **Deterministic — no LLM judge** — so it belongs in CI, and the client can re-run it themselves. |
| **🆕 In-language ground truth** | [`AI4Bharat/Anudesh-Backend`](https://github.com/AI4Bharat/Anudesh-Backend) | 🟢 **MIT** | `projects → tasks → users/review` workflow with organizations and workspaces: the machinery for getting teachers to author and review in-language rubrics and answer keys, with an audit trail. 🔴 Default ref **`master`**, **0 tags** — vendor a pinned commit. |
| **Mastery model** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) + [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 **MIT** | Bayesian Knowledge Tracing the client can inspect and **re-estimate on their own logs** — "adaptive" as a parameterised model, not a prompt. |
| **Retention** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** | FSRS spaced repetition + knowledge graph, and runs on local open-weight models with no key — the data-residency path. |
| **LMS surface** | client's **Moodle** | 🔴 **GPL-3.0** | Reach it through the plugin API, **do not fork** — `Pattern A` and the GPL-adapter sandwich in `Pattern Q`. |
| **Teacher AI-literacy material** | [`matsuolab/lecture-ai-engineering-2026-hi`](https://github.com/matsuolab/lecture-ai-engineering-2026-hi) | 🔴 **NO GRANT** | 🔴 **Reference only — do not vendor, do not redistribute, do not quote into deliverables.** Read it for *sequencing*: it is U Tokyo Matsuo Lab's `AIE2026` localised Hindi-first, and students build a learning agent progressively across the course. 🟢 That progression is the useful artefact; re-author it yourself. |

### How it wires together

1. **Ingest and ground.** Client curriculum (NCERT / state board) → DeepTutor's RAG store. 🔵 There is
   no permissive **Indian** curriculum graph on these shelves — `os-taxonomy` is NGSS/Common Core and
   its data is `ODbL-1.0 AND CC-BY-SA-4.0`. 🔴 **State that as a build item in the SOW**; `Pattern H`'s
   *"ground on a curriculum graph you must not fork"* rule applies, and `p388`'s BC and BNCC servers are
   the shape to copy, not reuse.
2. **Author ground truth in Anudesh.** One `project` per subject-grade; `tasks` are prompt +
   expected-constraint sets written **by the client's own teachers**; reviewers approve. 🟢 Output is a
   constraint set in `IndicIFEval`'s verifiable form, not free-text opinions.
3. **Gate the build in CI.** Run `IndicIFEval` (`indicifeval-ground` for native items,
   `indicifeval-trans` for translated) per target language on every model or prompt change. 🔴 **Fail
   the build on per-language regression, not on an aggregate** — an aggregate hides Odia collapsing
   while Hindi improves, which is precisely the failure a state buyer will find first.
4. **Adapt and retain.** OATutor/pyBKT fit mastery on the client's real logs; OpenTutor's FSRS
   schedules review. Both MIT, both inspectable.
5. **Deliver through Moodle's plugin API.** No fork, so no GPL obligation on the client's own IP.

### 🔴 The three things that will bite, named up front

- **`CC-BY-4.0` on the benchmark data.** Commercial use is fine; **attribution is not optional**. 🟢
  Put the AI4Bhārat attribution in the eval report and in any published score — the deliverable is the
  report, so the obligation travels with it. The MIT grant on the harness does **not** cover the data
  (`T36`, fourth instance).
- **These are research assets, not products.** `IndicIFEval` has **6 refs**; `Anudesh-Backend` has **0
  tags** and a `master` default ref. 🟢 Pin commits, vendor, and own the maintenance — that *is* the
  billable value, and it should be priced as such rather than discovered in month three.
- **14 languages is the benchmark's reach, not the tutor's.** 🔴 Scoring in Marathi does not mean
  teaching in Marathi. 🟢 Use the gate to **decide which languages to promise** — ship the three that
  pass and name the rest as phase two, rather than promising fourteen and failing in public.


**🆕 Pass `p401` · reads and commit both 2026-10-23.** 🟢 **One new pattern, and it exists because
the licence census forced its shape.**

## 🆕 `Pattern Q` — the GPL-adapter sandwich: Arabic-first AI on a Moodle base without surrendering the IP

🔵 **Why this pattern and not a tutor demo.** Two measurements from this pass fix the architecture
before any product decision: the Gulf mandates are **statutory and dated** (`SA` and `AE`
`curriculum_mandate` `MANDATED`, 2025/26), and **every one of the 51 readable grants in the Moodle
plugin family is `GPL-3.0-or-later`**. 🔴 So the obvious build — put the clever part in a Moodle
plugin — gives the clever part away. 🟢 The pattern puts the GPL boundary where it costs nothing.

### The three layers, with the licence of each stated

| layer | component | licence | why it is here |
|---|---|---|---|
| **1 · in-platform adapter** *(GPL, thin, contributed back)* | A `core_ai` provider plugin, 🆕 🟢 **cloned from [`ADORSYS-GIS/moodle-aiprovider_openaicompatible`](https://github.com/ADORSYS-GIS/moodle-aiprovider_openaicompatible)** *(`p404`: the live address, **8 d**; [`lmscloud-io`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible) is its origin and is **93 d** — `CONTENT-COPY`, direction established)* | 🟡 **GPL-3.0-or-later** *(read from `version.php`; **no licence file** at any ladder path)* | Moodle's own supported extension point, so no core patching and no upgrade debt. 🟢 Both vendors' `classes/provider.php` is **byte-identical at 3,963 B** — a de-facto standard shim. 🔵 Keep it thin: auth, request shaping, error mapping. Nothing proprietary crosses into it. |
| **2 · the boundary** | An **MCP server** the plugin calls over the network | 🟢 **Yours — MIT/Apache or closed** | 🔵 GPL-3.0 is **not** network copyleft. Code the plugin merely *calls* across a process boundary is not a derivative work of it, which is what makes layer 3 ownable. 🔴 This boundary is the entire point of the pattern; collapse it and layer 3 becomes GPL. |
| **3 · the grounding and the IP** | Arabic curriculum corpus + retrieval + evaluation | 🟢 **Yours**, seeded from **MIT** sources | Seed content from [`openaziz00-sudo/Arab-Artificial-Intelligence`](https://github.com/openaziz00-sudo/Arab-Artificial-Intelligence) (**MIT**, 1,650 Arabic prompts / 17 categories) and teacher-facing scaffolds from [`kazoya/build-your-own-agent-ar`](https://github.com/kazoya/build-your-own-agent-ar) (**MIT**). 🔴 **Do NOT seed from** [`sartaj1995/arabic-tutor`](https://github.com/sartaj1995/arabic-tutor) (100 levels, 1,367 exercises — **no grant at the ladder**) or [`michaelsboost/ArabEngo`](https://github.com/michaelsboost/ArabEngo) (**CC-BY-NC-4.0**, NonCommercial). |

### Wiring it, concretely

1. **Fork the provider plugin** and point its endpoint at your gateway, not at a model vendor.
   🔵 Read the grant from `version.php`, not from the GitHub sidebar — 27 of this family's 51
   grants have **no licence file to read**.
2. **Stand the MCP server up outside the LMS**, exposing exactly the tools the curriculum needs
   (retrieve-objective, generate-practice, grade-free-text, explain-in-Arabic). 🔵 The parent- and
   teacher-facing MCP servers already on [`agents/top.md`](../agents/top.md) are the shape to copy.
3. **Ground on the corpus you own**, aligned to the UAE MoE's **seven curriculum areas** for an
   AE engagement and to the National Curriculum Center's scope for `SA`.
4. **Keep the evaluation harness on your side of the boundary.** 🟢 It is the deliverable the EU AI
   Act's Annex III conformity assessment will want evidence of for any EMEA client whose system
   touches assessment — and the same artefacts serve a Gulf ministry procurement.
5. **Contribute layer 1 upstream.** 🔵 It is GPL anyway; contributing it buys maintenance you would
   otherwise owe, and credibility with the one platform the client already runs.

### 🔴 What this pattern does NOT claim

🔴 **There is no Arabic-first platform to start from.** The entire permissive Arabic education
supply found on 2026-10-23 is **three repositories, 4 ★ at best, all created within six weeks**
([`arabic-supply-leg`](../evidence/arabic-supply-leg.2026-10-23-p401.tsv)). 🟢 Layer 3 is **built,
not assembled**, and the pattern says so rather than implying a stack exists. 🔵 That is also the
argument for moving now: the demand is statutory and the supply is not yet anybody's.

🔴 **And the one component that would make this cheap is the one that is unlicensed.**
`sartaj1995/arabic-tutor`'s 1,367 structured exercises are the single richest Arabic content asset
this base has found, and with **no grant at any ladder path** they cannot be used. 🟢 **An email to
that maintainer asking for an explicit MIT grant is a lower-cost first move than building the
corpus** — and it is the kind of ask that succeeds, because the repository already reads as
intended-open.

**🆕 Pass `p400` · reads and commit both 2026-10-23 — sixth pass of the day.** 🔴 **No pattern
was added: the one unshelved address this pass found is unlicensed, and there is nothing to
compose with an unlicensed repository.** 🟢 **Both axes of the two-axis pre-flight got sharper
anyway, and one of them got sharper in the dangerous direction.**

🟢 **The jurisdiction axis — APAC is no longer a blank.** Every recipe here is gated on
*(licence × jurisdiction)*, and the jurisdiction axis reads
[`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv). 🔴 **Until this pass that file answered
every APAC teaching-mandate query with a single `NOT_ESTABLISHED` row** — and in a pre-flight a
blank reads as *"no rule"*, which is the dangerous direction to be wrong in. 🟢 It now answers
with **seven** rows. The two that change a build:

- 🟢 **`CN-BJ | curriculum_mandate | MANDATED | 2025-09-01`** — **≥ 8 class-hours per academic
  year across all Beijing primary and secondary schools.** 🔵 Any recipe here that ships a
  tutoring or courseware surface into Beijing acquires a **contact-hour accounting**
  obligation: the deliverable must be able to *evidence* hours delivered per learner per year,
  which is an LRS/record-layer requirement, not a model requirement. 🔵 This base already holds
  the record-layer supply problem (`p396`: one 15 ★ MIT MCP bridge, 419 days dead, is the whole
  agent↔LRS supply) — 🔴 **so the obligation now has a named instrument and the stack to satisfy
  it is still the thinnest tier on these shelves.** That pairing is the pattern-relevant fact.
- 🟡 **`IN-CBSE | curriculum_mandate | MANDATED | 2026-27`, with `IN | NOT_ESTABLISHED`** — a
  recipe aimed at Indian Classes 3–5 must deliver **into Mathematics and "The World Around
  Us"/EVS**, because that is where the curriculum puts it; a standalone "AI for Class 3" surface
  is **mis-shaped for the only instrument that binds**, and AI proper does not begin until
  Class 6. 🔴 There is **no board exam**, so no assessment-integration pressure — which removes
  a requirement most recipes here would have assumed.

🟢 **The licence axis — the gate that admits candidates to a recipe now exists as code.**
Patterns here compose named repositories, so a pattern is only as good as the claim that its
parts are real and carried. 🔴 **That claim was being made with a bare-name grep**, which is a
substring match (`400-C`). 🟢 [`p400-candidate-membership`](code/p400-candidate-membership/README.md)
answers it by exact address over **both** of this base's address channels, and reports
`NAME-SUBSTRING-ONLY` as its own class so a candidate can no longer be dropped silently.
🔵 **Use it before adding a repository to any recipe below:**

    python3 -I compose/code/p400-candidate-membership/membership.py classify owner/name

🔴 **And the honest limit, stated so the pre-flight is not oversold:** the licence axis can be
settled first-hand from this session (`raw.githubusercontent.com` → **301**, payloads served);
the jurisdiction axis **cannot** (every policy host → **000**). 🔵 So every row in
`policy-matrix.tsv` is band `reported` by construction, and a recipe gated on jurisdiction is
gated on a single-channel claim. **Say so in the engagement, and re-read the instrument from a
session with egress before a deliverable depends on it.**

**🆕 Pass `p399` · reads and commit both 2026-10-23 — fifth pass of the day.** 🔴 **No pattern
was added, because no new supply arrived to compose with** — the supply legs returned seven
candidate addresses of which six were shelved and the seventh is not education-native.

🟢 **The two-axis pre-flight gets materially better without a single pattern changing.** Every
recipe here is gated on *(licence × jurisdiction)*, and the jurisdiction axis reads
[`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv). 🔴 **Until this pass that file answered
every LATAM teaching-mandate query with a blank** — 11 rows across `ai_literacy_instruction` and
`curriculum_mandate`, none of them LATAM — 🔴 **and a blank in a pre-flight reads as "no rule",
which is the dangerous direction to be wrong in.**

🟢 **It now answers with six rows.** The one that changes a build:

- 🔴 **`CO` · `Ley 2626 de 2026` · MANDATED · binding on official schools.** Any pattern here
  delivering curriculum or AI-literacy content into Colombian **public** education now has a named
  statute to conform to, and 🔴 **a `Feb 2027` deadline for the curricular guidelines** — which is
  the date an engagement plans against, not the **2026-08-24** sanction date.
- 🔵 **`AR`, `CL`, `MX`, `BR`, `UY` · ADVISORY_NONBINDING · `PE` · ADOPTED.** These bind nothing and
  must not be pitched as compliance drivers; they are **adoption** signals, and the honest use is
  scoping a pilot's ministry alignment, not selling a compliance deliverable.

🔵 **Recorded here as a change to how the existing recipes are gated, not as a new recipe** — the
same judgement `p398` made for the `OpenMAIC` commit-pinning rule. `Gap 399-A`.

**🆕 Pass `p398` · reads and commit both 2026-10-23 — fourth pass of the day.** 🔴 **No pattern was
added or amended, because no new supply arrived to compose with.** Eight search legs returned one
address this base did not hold, and 🔴 **it is archived** — which disqualifies it as a pattern
component outright. 🔵 **The one recommendation change is a pinning rule, not a new recipe:** every
pattern here that names [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) should pin a
**commit**, not a tag — `v1.3.0-rc.1` (2026-10-22) opened while `v1.2.0-rc.1` (2026-10-04) had still
not reached stable, so a tag-based dependency on this project has nothing stable to point at. 🔵
Recorded here rather than as a new pattern because it changes **how** the existing ones are built,
not **what** they are. `Gap 398-C`.

**Pass `p397` · reads and commit both 2026-10-23 — third pass of the day.** 🟢 **`p396` ranked
re-running the xAPI 2.0 bake-off second, on the grounds that *"three claimants at 1 star between them
will move fast or die; either outcome changes the recommendation."* They moved — and they did not
move together.** One new pattern, and `Pattern AE` amended rather than restated. Evidence:
[`record-layer-redating`](../evidence/record-layer-redating.2026-10-23-p397.tsv) ·
[`shelf-lineage`](../evidence/shelf-lineage.2026-10-23-p397.tsv).

## 🟢 `Pattern AE` AMENDED — the xAPI 2.0 bake-off now has an activity ranking

🔵 `Pattern AE` told a studio to adjudicate three zero-star LRS claimants itself, because *"reputation
cannot decide this."* That still stands. 🟢 **What `p397` adds is the one signal that was missing:
which of them is actually being built.** Dated on the git channel, never on the HTML "Updated" column
(`396-G`):

| candidate | stack | `p396` | `p397` HEAD | days | reading |
|---|---|---|---|---|---|
| [`nurullahturkoglu/xapi-dotnet`](https://github.com/nurullahturkoglu/xapi-dotnet) | ASP.NET Core | "under 75 d" | `0d47d65` 2026-10-21 | 🟢 **1** | 🟢 **under active daily development** |
| [`codetakt/kiva`](https://github.com/codetakt/kiva) | Rust, F\* proofs | "under 75 d" | `addf100` 2026-10-21 | 🟢 **2** | 🟢 **also moving**; 🔵 still the only one whose README *withdraws its own conformance claim* |
| [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) | TypeScript/Hono/Postgres | "under 75 d" | `4d18e0c` 2026-08-08 | 🔴 **75** | 🔴 **has not moved at all** since `p396` measured it |

🟢 **So the "all three are under 75 days" sentence has split into two live projects and one
stalled one**, and the bake-off order changes accordingly: 🟢 **run `xapi-dotnet` and `kiva` first**,
and treat `xapi-lrs` as the control rather than a contender until it commits again.

🔴 **The tooling half of `Pattern AE` is the part that has aged, and it matters more than the
candidates.** [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
is 🟢 MIT, 78 ★ — and **`5bc232d`, 2025-09-04, 413 d**, unchanged. 🔵 **You are asked to certify
2.0 conformance with a suite that has not been touched in fourteen months**, while the implementations
it judges change weekly. 🟢 [`yetanalytics/lrs-test-runner`](https://github.com/yetanalytics/lrs-test-runner)
(Apache-2.0, **6 d**) and [`yetanalytics/xapi-schema`](https://github.com/yetanalytics/xapi-schema)
(**6 d**) are both live, so the **CI harness around the suite is maintained even though the suite is
not.** 🔴 **Quote that asymmetry to a client before you quote a pass rate.**

## 🆕 `Pattern AF` — prove provenance BEFORE you prove the licence, in two commands

**When.** Any engagement that is about to adopt, fork or warrant an open-source education component
— and especially when the candidate came out of a search result rather than a standards document.

🔴 **Why it goes first.** A licence read **cannot** tell a fork from its upstream: the payload is
usually byte-identical, so the grant channel is blind by construction (`395-A`). A star read cannot
tell a rename from a fork either: GitHub answers on the old organisation path indefinitely and shows
the same stars. 🔴 **On these shelves, 8 of 15 shared-root pairs were renames and 7 were real
forks** — and nothing short of comparing commits separates them.

**The recipe, and it needs no API, no HTML and no credentials.**

1. **Root commit** — shared root means shared ancestry:
   `git clone --filter=blob:none --no-checkout -q https://github.com/OWNER/REPO d && git -C d rev-list --max-parents=0 HEAD`
2. **HEAD** on the same clone: `git -C d rev-parse --short=12 HEAD`
3. **Adjudicate**: same root + same HEAD → **one artefact, two addresses** (fold them, cite the
   current path); same root + different HEAD → **a real fork** (now decide which side to carry);
   distinct roots → **unrelated** despite the shared name; either side unresolvable → **inconclusive**,
   never "independent".
4. 🟢 **Then date both sides**, because step 3 tells you the fork is real and nothing about whether
   anyone maintains it. `T40` is the cautionary case: `ucfopen/pylti1.3` is a genuine institutional
   fork of `dmitry-viskov/pylti1.3`, and **both are over 1 370 days dead.**
5. **Only now read the grant**, and read it by enumerating the tree
   (`git ls-files | grep -iE '(licen[cs]e|copying)'`) rather than guessing filenames — that is how
   this pass found [`gradescope/autograder_samples`](https://github.com/gradescope/autograder_samples)
   ungranted at root with vendored third-party MIT two directories down.

🟢 **Wired and runnable:** `bash compose/code/p397-shelf-fork-audit/lineage.sh OWNER_A/REPO OWNER_B/REPO`,
with `make shelf-fork-candidates` deriving the candidate pairs from the shelves themselves and
`make gate-shelf-fork` holding 11 controls. 🔴 **Stated limit:** a squashed or re-rooted fork reads as
independent — no false positives, possible false negatives.

🔵 **Cost: two blobless clones per pair, a few seconds each.** `p397` ran 21 pairs inside one pass.

### 🆕 `p402` AMENDMENT — a cheaper front door, and the missing step 3b

🟢 **Front door: `git ls-remote` needs NO clone.** Comparing the **full ref set** of two addresses
answers the identity question for the price of one network round-trip each:

```sh
git ls-remote https://github.com/OWNER/REPO | sort | sha256sum   # ref-set fingerprint
```

Identical ref set → **one repository**. 🔴 **Identical HEAD alone is NOT identity** — `p370` demoted
five pairs from `STALE` to `DISTINCT` on exactly that, because *a redirect serves ONE repository, so
a different ref set is a different repository*. `sharziki`↔`rohanmuppa` `purdue-mcp` share HEAD
`6922f1f301dd` and have **5 vs 3** refs; `Halleck45`↔`chinobv` `openpronounce` share HEAD
`74bc17ea406e` and have **10 vs 4**. 🔵 Use the clone arm (steps 1–2) when you need the **root**, to
separate a rename from an unrelated repo that merely shares a name.

🔴 **Step 3b, which this pattern was missing.** Step 3 says *"fold them, cite the current path"* and
gives **no way to find that path**. The ref set proves *one repository*; it never says *which
address is canonical*. 🟢 **The channel that does: fetch EITHER address over HTTPS and read the
header/breadcrumb of the page you LAND ON.** GitHub serves a rename or transfer as a redirect, the
fetcher follows it, and the page names the canonical owner — plus the archive banner, the licence
and any `forked from` parent in the same read.

🔴 **The trap, stated because it cost this base ~52 passes.** The redirect is followed **silently**,
so two stale addresses both report *"not a fork"* with **identical star counts** — indistinguishable
from two independent repositories. *Same stars · no fork line · two owners* is the signature.
🟢 It is how `p402` found that `ease`'s canonical address is **neither** candidate in the register
but a third owner, [`openedx-unsupported/ease`](https://github.com/openedx-unsupported/ease), and
closed `ACTION ZZ-al`.

🔵 **Engagement rule.** Warrant the **canonical** address, not the one in the search result — and
when the canonical owner is named `*-unsupported` or carries an archive banner, that **is** the
stewardship finding. Read it before promising a client a maintained dependency.

**🆕 Pass `p396` · reads and commit both 2026-10-23.** Two patterns, both built on grants and dates
read first-hand this pass:
[`record-layer-dating`](../evidence/record-layer-dating.2026-10-23-p396.tsv).

## 🆕 `Pattern AD` — the agent that writes to the institution's record, not just its own memory

**When.** The client needs to show *someone else* — an accreditor, a regulator, a district board, a
parent — what the AI did and what the learner actually demonstrated. This is every North America K-12
engagement under Oklahoma-style teacher-review and opt-out rules, every EU deployer under Article 26
logging, and the governance sale that `intel/market.md` identifies as the LATAM entry point.

🔴 **Why you cannot just use the agent's memory.** `DeepTutor`, `inno-agent` and every other tutoring
agent on this shelf keep private, vendor-shaped memory designed for conversational continuity. It is
not an evidence record, it does not survive replacing the agent, and no registrar will read it
(`T37`).

**Components, all dated this pass.**

| Role | Component | Licence | Age | Note |
|---|---|---|---|---|
| Record store (Python shop) | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 MIT | 🟢 10 d | France Université Numérique; Open edX Aspects' own LRS |
| Record store (JVM shop) | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 | 🟢 21 d | 144 ★; SQLite/Postgres/MariaDB/MySQL |
| Record store (.NET shop) | [`nurullahturkoglu/xapi-dotnet`](https://github.com/nurullahturkoglu/xapi-dotnet) | 🟢 Apache-2.0 | 🟢 1 d | 🔴 0.x, 1 ★ — gate on a conformance run |
| Platform emitter (Moodle) | [`davidpesce/moodle-logstore_xapi`](https://github.com/davidpesce/moodle-logstore_xapi) | 🔴 GPL-3.0 | 🟢 2 d | 82 ★; GPL because every Moodle plugin is |
| Agent ↔ LRS bridge | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 MIT | 🔴 **419 d** | **the weak link — see below** |
| Launch into the LMS | `packbackbooks/lti-1-3-php-library` / `ltijs` / `lti-tool` (`p395`) | 🟢 permissive | 🟢 1–9 d | pick by runtime |

**Wiring.** Agent → MCP (`learnmcp-xapi`) → LRS (`ralph` or `lrsql`); LMS → emitter
(`moodle-logstore_xapi`) → *the same* LRS; agent launched from the LMS over LTI 1.3 so the learner
identity on both paths is the same subject. 🔵 **The single design decision that makes this worth
building:** the agent's statements and the platform's statements land in **one** store against **one**
identity, so "what did the AI do for this student" and "what did this student do" are one query.

🔴 **Scope this honestly at estimate time.** `learnmcp-xapi` is 15 ★ and has not moved in fourteen
months. 🟢 It is MIT, it is small, and the xAPI statement shapes it needs are specified — so treat it
as **a reference to fork and own, budgeted as build, not as a dependency**. Anyone quoting it as
maintained third-party infrastructure will be wrong by about a year.

**Effort.** 6–8 weeks for a single-LMS, single-agent deployment on an existing Moodle or Open edX;
add 3–4 weeks to own the MCP bridge properly rather than vendoring it.

## 🆕 `Pattern AE` — choosing an xAPI 2.0 LRS when every candidate has zero stars

**When.** The client specified xAPI 2.0 / IEEE 9274.1.1 — increasingly common in defence, aviation,
regulated corporate training and any procurement written against the current standard.

🔴 **The situation, measured.** No adopted open-source LRS implements 2.0. `lrsql` (144 ★) and Ralph
(51 ★) are both 1.0.3. The three claimants hold **one star between them**: `pelotech/xapi-lrs` (0 ★,
TypeScript/Hono/Postgres), `codetakt/kiva` (0 ★, Rust, F* proofs) and `nurullahturkoglu/xapi-dotnet`
(1 ★, ASP.NET Core). 🔴 **Reputation cannot decide this**, and each project's own conformance claim
is self-reported — `kiva`'s README goes so far as to withdraw its own repository blurb, saying
equivalence with the 2025 edition *"has not been established"* and that source traceability *"does
not establish implementation conformance."*

🟢 **So adjudicate it yourself, with permissive tooling that already exists.**

1. Stand up each candidate against a **throwaway** Postgres — the suite persists data and its README
   warns it *"should not run against a production LRS endpoint."*
2. Run [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
   (🟢 MIT, 78 ★, Node) with `--xapiVersion 2.0.0`, then again with `1.0.3` — a conformant 2.0 LRS
   must still accept 1.0.x statements.
3. On the JVM, drive the same suite from CI with
   [`yetanalytics/lrs-test-runner`](https://github.com/yetanalytics/lrs-test-runner) (🟢 Apache-2.0,
   6 d) so the result is a build artefact rather than a screenshot.
4. 🟡 Read failures with judgement: a .NET implementer reports the suite *"sometimes expects more
   than the standard requires"* *(secondary)*, and the suite is **413 days old** while all three
   candidates are under 75 days. A failure is a conversation, not a disqualification.

🟢 **Hedge the choice structurally.** `pelotech/xapi-lrs` states its schema matches `lrsql` v0.9.5's
Postgres shape, so an `lrsql` database can be taken over. 🔵 This pass's fork arm confirms the two are
**independent codebases, not a fork** (distinct root commits `b1bfc0f67292` vs `f9e81c891b9a`) — so
this is genuine schema compatibility between rivals, which is the rare case where a client can start
on the 144 ★ 1.0.3 store and migrate to the 0 ★ 2.0 store without a data conversion.

**Effort.** 2–3 weeks for the bake-off and a reproducible CI conformance job; the result is reusable
across every later engagement on this layer, which is the main reason to do it once properly.


# Compose patterns — education

**🆕 Pass `p395` · reads and commit both 2026-10-23.** Two patterns, both built on grants and **dates**
read first-hand this pass: [`verified-repos`](../evidence/verified-repos.2026-10-23-p395.tsv) ·
[`lti-layer-dating`](../evidence/lti-layer-dating.2026-10-23-p395.tsv).

## 🆕 `Pattern AC` — the JVM-or-Go client's LTI edge (the one this base could not quote before)

**When.** The client's platform team owns **Java** or **Go**, and an agent has to launch from their
Moodle, Canvas, Blackboard or D2L. This is most enterprise work and much of European public sector.

🔴 **Why the obvious route is closed.** The only permissive **Java** LTI 1.3 core is
[`UOC/java-lti-1.3-core`](https://github.com/UOC/java-lti-1.3-core) (MIT) — **1,193 days dead**. The
Go options are [`StevenWeathers/peregrine-lti`](https://github.com/StevenWeathers/peregrine-lti)
(Apache-2.0, **679 d**, pre-1.0 API), [`macewan-cs/lti`](https://github.com/macewan-cs/lti) (MIT,
**1,919 d**, self-declared unstable, **deep linking unimplemented**) and 🆕
[`astiusa/lti`](https://github.com/astiusa/lti) (MIT, **794 d**, a `p404`-measured **strict superset**
of `macewan-cs` — which inherits the same instability warning, untouched by its two extra commits). 🔴 An unmaintained library doing
**OAuth 2 / JWT signing and key rotation** is a *security* dependency — the same argument that
demoted `1EdTech/lti-1-3-php-library`. Do not put a client's identity flow on any of the three.

**Wire it like this.**

1. **LTI edge — [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool)** (🟢 MIT, HEAD **1 d**,
   `@lti-tool/core` v1.3.2). Serverless-native: Lambda, Workers, Hono, with OIDC, **Assignment and
   Grade Services**, Names and Role Provisioning, Deep Linking and Dynamic Registration all
   implemented, and the session store chosen at deploy time. 🟡 Prefer
   [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (🟢 Apache-2.0, **9 d**, 207 npm releases)
   instead when the client wants a long-running Node process and already runs Mongo.
2. **The hop.** The edge validates the launch, then forwards a **signed, short-lived internal token**
   carrying only `sub`, context, roles and the resource link to the JVM/Go service. 🔵 The agent never
   parses an LTI message, which is the whole point: the standards surface stays in the runtime where
   it is maintained.
3. **The agent** stays in Java or Go — the client's own service, unchanged.
4. **Grades back** through the edge's AGS client, never direct from the agent. One component holds the
   platform credentials.

🟢 **Why this beats forking a dead library:** `lti-tool` is 1 day old and `ltijs` 9, so key rotation
and spec drift are somebody's job. 🔴 **Cost to state in the proposal:** one extra deployable and one
extra network hop — *and* `lti-tool` is **8 ★ with no production claim** (its README's
*"Production-ready security features"* heading is about the security section, not the project), so
pilot it; `ltijs` is the safer default for a ministry. 🔵 Note this is the architecture `p391`
recommended for Python and `p392` correctly withdrew when `django-lti` turned up live at 2 days. **It
stands for Java and Go because the dating says so, not because it is the usual advice.**

## 🆕 `Pattern AD` — a learner-facing agent shell with a curriculum you are actually allowed to ship

**When.** The client wants a personal tutor that remembers a learner across months, and the
deliverable must survive a legal review.

1. **Shell — [`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent)** (🟢 MIT, **1.3k ★**, HEAD
   **10 d**). You get the parts that are expensive to build: **L1** learner profile, **L2** a native
   wiki knowledge base, **L3** session records with cross-conversation retrieval, a **cron scheduler**
   for proactive check-ins, and a workspace-scoped **Practice Lab** with an in-browser terminal.
   🔵 It sits on the Pi coding-agent SDK (MIT) *without modifying its kernel*, so the upgrade path is
   npm, not a fork.
2. 🔴 **Do NOT ship its skill library.** The companion
   [`Chloris-Blaxk/inno-agent-hub`](https://github.com/Chloris-Blaxk/inno-agent-hub) — skills and
   workspace presets — is **ungranted on every arm** (no licence file, no manifest field, no README
   grant, all three enumerated). Read it for shape; author your own.
3. **Curriculum — granted sources only.** [`oppia/oppia`](https://github.com/oppia/oppia)
   (🟢 Apache-2.0) for misconception-aware lesson structure, and
   [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (🟢 MIT) when the
   deployment is offline-first. 🔴 **Avoid grounding the tutor on
   [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) without legal sign-off**
   — `ODbL-1.0 AND CC-BY-SA-4.0`, and the **CC-BY-SA half reaches generated content**, so a curriculum
   document produced from it can inherit share-alike. That is `Pattern H`'s warning, and it is the
   trap this pattern is most likely to fall into.
4. **Launch from the LMS** with `Pattern AC`'s edge, so the tutor is reachable where students already
   are.
5. 🔴 **Regulatory stop, before any design work.** The moment this agent **grades**, **assigns a
   learner to a programme**, **assesses their appropriate level**, or **monitors behaviour during a
   test**, it is **Annex III ¶3 high-risk** in the EU and needs the human-in-the-loop and
   documentation posture. 🔴 And **no emotion inference, ever, in an EU educational setting** — that is
   prohibited outright, not assessable. Keep the memory layers descriptive (what was practised, what
   was missed) and never affective.

🟡 **Honest limits.** `inno-agent` is a **single-learner companion** — there is no cohort, roster or
teacher dashboard in it, so an institutional pilot needs that built. Its IM channels ship as **Feishu
and WeChat**, so a non-APAC deployment replaces the messaging layer. And at **10 days old with a June
2026 technical report**, it is a strong pilot base, **not** a ministry platform this quarter.

**🆕 Pass `p394` · reads 2026-10-22, committed 2026-10-23.** Two new patterns, both built on grants
read at the payload this pass. 🟢 **`Pattern AB`** — the **R statistics course graded automatically**,
closing the hole `p393` named when it pointed out that this base's most-adopted *maintained*
autograder grades R
while the shelves held no R components; its delivery layer is permissive (`gradethis` MIT, `learnr`
Apache-2.0, `ottr` BSD-3) and its measurement layer is GPL behind a process boundary, and its last
step is **the only offline assessment loop in this base** (`cran/exams` NOPS: printed, scanned, marked
automatically, paper audit trail). 🟢 **`Pattern AC`** — **give teachers an assistant builder instead
of building their assistants**, on **LAMB** (GPL-3, UPC Barcelona + UPV/EHU, peer-reviewed), which
publishes each teacher-authored assistant into Moodle as an **LTI external tool** so the LMS is never
forked. 🔴 Both patterns carry a hard stop at grading: under the EU AI Act, systems that grade
learners or influence access to qualifications are **high-risk and require conformity assessment
before deployment**, so the grading step is scoped as a separate assessed workstream rather than sold
in the same phase.

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/compose-patterns.md`](../archive/2026-10-22-p383-pre-rewrite/compose-patterns.md).

Every repo named here was verified first-hand on 2026-10-22 —
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv). Licences are read from the
payload at the repository's **real default ref**, which for 13 of 58 live addresses is not `main`.

**The governing constraint for all of these:** the platform tier is copyleft, the agent tier is
permissive. Every pattern below therefore puts a **documented interop boundary** — LTI 1.3, MCP, or
web services — between client-owned code and the platform. None of them forks an LMS.

🆕 **`p389`** adds **`Pattern Q`** (the generated classroom, the greenfield answer when there is no
LMS to bolt onto), gives **`Pattern B`** a maintained mastery model, and gives **`Pattern D`** two
components that remove its server. Every repository named in those changes was **dated** this pass —
last commit at the real default ref:
[`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv). 🔵 **Read a date as a cost line:**
a permissive repository nobody has touched in eight months is something you *vendor and maintain*, not
something you *integrate* — which is why `Pattern B` vendors `pybryt` and why `Pattern Q` pins a ref.

---

## Pattern A — Tutor over the client's existing LMS (no fork, no copyleft exposure)

**For:** a client who already runs Moodle or Canvas and wants a tutor that knows the actual course.

**Wiring:**
1. **Expose the LMS.**
   - *Moodle:* install **`webservice_mcp`** from Moodle's own plugin directory (Moodle 4.5–5.2,
     latest release 23 Jul 2026). It serves Moodle's external functions as **MCP tools over
     JSON-RPC 2.0**, gated on the `webservice/mcp:use` capability. Configured inside Moodle — no
     patch to core, so **no GPL obligation reaches your agent**.
   - *Canvas:* [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (**MIT**) for courses,
     assignments, submissions, grading, rubrics, students; or the fork
     [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (**MIT**) which adds office-hour
     appointment groups, syllabus read/write, student groups and course-content copy.
   - 🆕 `p390` *Open edX:* skip the MCP hop and run **inside** the platform as an **XBlock** — and the licence maths
     works out better than it looks. The platform is **AGPL-3.0**, but the component API your plugin imports,
     [`openedx/XBlock`](https://github.com/openedx/XBlock), and the [`xblock-sdk`](https://github.com/openedx/xblock-sdk)
     you develop against are both **Apache-2.0** (`LICENSE.TXT`, both dated 2026-10-22). **So the XBlock you write can stay
     MIT or proprietary while running in an AGPL host** — no fork, no LTI hop, and full access to course state.
     [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Colombia) is the working proof.
     🔴 **Check the boundary per package, not per org:** [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning)
     and the `frontend-app-*` MFEs are **AGPL-3.0**, so an import from those pulls network copyleft straight back in.
     Keep the plugin's dependency list to `XBlock` plus your own code and audit it in CI.
   - 🟡 **Grant status, corrected:** the plugin repo
     [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) has **no
     root licence file**, but `version.php` carries the full **GPL-3.0-or-later** header Moodle
     requires of every plugin — so it is granted, and GPL is survivable because you reach it over
     JSON-RPC rather than linking to it.
     [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) is
     **manifest-only MIT** (`package.json` declares it; the file it names is absent from the tree).
     🔴 **Do not use** [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp): no licence file
     **and** no `license` field in `pyproject.toml` — genuinely no grant to redistribute.
2. **Ground it in the course material.** [infiniflow/ragflow](https://github.com/infiniflow/ragflow)
   (**Apache-2.0**) over the course files, with
   [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)
   (**Apache-2.0**) for the PDF/DOCX/PPTX/scan reality. If the client has lecture video,
   [opencast/opencast](https://github.com/opencast/opencast) transcripts are the richest corpus
   available and nobody is using them.
3. **Give it pedagogy and memory.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
   (**Apache-2.0**) for persistent learner memory plus material-grounded tutoring. If the client
   wants explanation *pitched* to the learner's state rather than merely retrieved, look at
   [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) — but it is **GPL-3.0**, so
   run it as a separate service, not as a library inside the deliverable.
4. **Front it.** [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**) — SSO,
   per-user quota, provider routing and the **audit log** that gets the build past a data-protection
   officer. (Not `open-webui`: its `LICENSE` is 2,819 B of BSD-3 text **plus** a branding
   restriction and a CLA.)
5. **Prove it.** [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
   (**MIT**) with [MMLU](https://github.com/hendrycks/test) (**MIT**) and
   [GSM8K](https://github.com/openai/grade-school-math) (**MIT**), scored on the client's own
   subject mix, before and after.

**Licence posture:** client-owned code is MIT/Apache/BSD throughout. The only copyleft component is
the LMS itself, reached over a published protocol. **Deliverable stays closed if the client wants it
closed.**

---

## Pattern B — Autograding that assesses the approach, not just the output

**For:** CS, data-science and engineering programmes drowning in submissions.

**Wiring:** [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) (**BSD-3**) for
identical per-cohort compute → [jupyter/nbgrader](https://github.com/jupyter/nbgrader)
(**BSD-3**) for the release/collect/autograde/return lifecycle →
[ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) (**BSD-3**, default ref
`master`) for container-isolated grading at cohort scale →
[microsoft/pybryt](https://github.com/microsoft/pybryt) (**MIT**) to check **how** the student got
there, not only whether the answer matched →
[jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) (**BSD-3**) so the LLM explains
*why* the approach was wrong, inside the notebook the student is already in.

**Why this combination:** pybryt is the piece everyone misses. An LLM that reviews output rewards
the student who guessed; pybryt's annotations let you detect the *intended method* and then have the
model give feedback on the method. **Fully permissive — BSD-3 and MIT only, zero copyleft.**

🔴 🆕 `p387` **Vendor pybryt; do not install it.** PyPI `pybryt` has shipped nothing since
**v0.7.0, 2022-04-28** — four and a half years — so a client support contract cannot rest on it as a
dependency. The pattern does not change: copy the annotation approach (and, licence permitting under
its MIT grant, the code) into the deliverable and maintain it there, with the maintained BSD-3
halves of this stack (`nbgrader`, `otter-grader`) carrying the running infrastructure. Dates:
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv).

🟢 🆕 `p388` **And the notebook-tutor half now has a maintained component, which changes what you
vendor.** [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) (**BSD-3**,
`main` · `139bb11`, **v0.3.2, 7 releases, → 2026-09-25**, from a known Jupyter-ecosystem maintainer)
replaces the ad-hoc "wire `jupyter-ai` into the grading loop" step with a component built for exactly
this job:

- A per-cell **Explain Code** button sends the cell source, the kernel language, **the error
  traceback**, and the preceding cells up to the last markdown cell **as the exercise statement** —
  so the model sees the task, not just the broken line.
- 🟢 **The tutor persona lives in a `TUTOR.md`, discovered by walking up from the notebook's
  directory to the server root.** Each course, module or folder carries its own pedagogy **in version
  control**. This is the single most useful thing on this shelf for a client engagement: *"AI must
  not give the answer"* stops being a prompt someone pasted and becomes a reviewable file in the
  course repository, diffable and auditable per cohort.
- 🟢 **`reference_solution` and `evaluation_criteria` ride in cell metadata, ROT13-encoded** so they
  are not casually readable by a student holding the notebook — the same instinct as `pybryt`'s
  annotations, shipped in a maintained package.

**Revised wiring:** `jupyterhub` → `nbgrader` → `otter-grader` for the lifecycle and
container-isolated grading (all BSD-3, all maintained) → **`jupyter-ai-tutor`** for the in-notebook
explanation layer, configured by a per-course `TUTOR.md` → **vendored `pybryt` annotations** for
approach assessment, maintained inside the deliverable as `p387` requires. 🔵 Note the division of
labour this produces, and it is the one the guardrail below wants anyway: `jupyter-ai-tutor` **explains
and never grades**, `nbgrader`/`otter-grader` grade and never explain. 🟡 It requires
`jupyter-ai-jupyternaut` (<0.1) for the agent, so pin that bound.

🟢 🆕 `p389` **And the missing third component: the mastery model.** Everything above assesses a
*submission*. Nothing in it answers the question a programme director actually asks — **which skills
has this student mastered, and what should come next** — and this base has carried that gap while
recommending a dependency that stopped shipping in 2022. The maintained answer is
[**CAHLR/pyBKT**](https://github.com/CAHLR/pyBKT) (**MIT**, real ref `master`, **last commit
2026-10-21 — 1 day**), from UC Berkeley's CAHLR, who also maintain
[**OATutor**](https://github.com/CAHLR/OATutor) (**MIT**, `main`, **1 day**) as the tutoring front end
built on it.

- **What it adds to this wiring:** fit **Bayesian Knowledge Tracing** on the client's *own*
  `nbgrader`/`otter-grader` outcome logs — one row per (student, skill, attempt, correct) — and you get
  per-skill **learn, guess, slip and forget** parameters plus a running mastery probability per student.
- 🟢 **Why it is the defensible choice and not just the available one:** those four parameters are
  **inspectable numbers a client can argue with**, re-estimated on their own cohort. "The model thinks
  Ana has not mastered partial fractions, with these parameters fitted on this data" survives a
  procurement review; "the LLM judged her weak" does not. North American and Maryland-style rules that
  bar AI from high-stakes decisions about students are satisfiable here precisely *because* the
  decision rule is a published model rather than a generation.
- **Revised wiring, end to end:** `jupyterhub` → `nbgrader` → `otter-grader` (lifecycle + isolated
  grading) → **`pyBKT`** fitted on the outcome log (mastery per skill) → **`jupyter-ai-tutor`** with a
  per-course `TUTOR.md` for in-notebook explanation → **vendored `pybryt` annotations** for approach
  assessment. 🟢 **Still fully permissive: BSD-3 and MIT only, zero copyleft.** 🔵 The sequencing
  matters: `pyBKT` decides *what to work on*, the tutor explains *why the attempt failed*, and the
  graders remain the only components that produce a grade.
- 🟡 **Cold start is the real constraint**, not the licence: BKT needs interaction history. For a new
  cohort, serve `OATutor`'s scaffolds with default parameters, log, and re-fit at the end of the first
  module — and say so in the estimate rather than discovering it in week three.

**Guardrail:** where DC-style rules apply, AI must not be the grader of record. Configure the LLM as
a **feedback generator with a human grade-of-record** and keep the audit trail; that configuration is
the deliverable, not a disclaimer. 🆕 `p389` The same rule governs the mastery model: a BKT mastery
probability is **advisory input to a human decision**, and the moment it auto-finalises anything
consequential it is the "sole basis for a decision without meaningful human review" that Vietnam's
Decision 33/2026 and EU Annex III both reach.

---

## Pattern C — Citation-grounded academic assistant (and the EU compliance story that comes free)

**For:** higher-ed research support, library services, graduate programmes.

**Wiring:** [Future-House/paper-qa](https://github.com/Future-House/paper-qa) (**Apache-2.0**) as
the answer engine → [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar)
(**Apache-2.0**) or [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib)
(**Apache-2.0**) for multi-paper synthesis →
[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) (**Apache-2.0**)
for ingest → [LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**) as the campus gateway.
For guided-inquiry assignments, [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
(**Apache-2.0**) as the student-facing research scaffold.

**The compliance argument:** paper-qa **declines to answer** without retrieved evidence. Under
**EU AI Act Art. 50** (transparency, live from **2 Aug 2026** — *not* delayed by Regulation (EU)
2026/1744) a system that cites its sources and refuses otherwise is dramatically easier to document
than one that generates fluently. Build the refusal behaviour in, then point at it in the
conformity file. **Fully Apache-2.0/MIT.**

---

## Pattern D — Offline-first deployment for connectivity-constrained regions

**For:** LATAM, African and rural APAC deployments — including the nine countries in the Google.org
AI-literacy rollout (Argentina, Brazil, Chile, Colombia, Dominican Republic, El Salvador, Mexico,
Peru, Uruguay).

**Wiring:** [learningequality/kolibri](https://github.com/learningequality/kolibri) (**MIT**,
default ref 🔴 `develop`) as the edge runtime — offline-first by design, not a degraded mode →
a small local model on the same device for the tutoring loop →
[FSRS](https://github.com/open-spaced-repetition/fsrs4anki) (**MIT**) for scheduling review, because
retention is the one outcome measurable without a network →
content authored in [H5P](https://github.com/h5p/h5p-php-library) — 🟡 **GPL-3.0, keep it as
runtime content, not linked code** → periodic sync to the central LMS over
[LTI 1.3](https://github.com/Cvmcosta/ltijs) (**Apache-2.0**) when a link is available. 🆕 `p392` **Use a maintained implementation, and pick it by language — all three majors have one.** **Python:** [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (🟢 MIT, PyPI v0.10.1, HEAD 2026-10-20) **in-process** for a Django agent, or [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (🟢 BSD-3) for a JupyterHub. **Node:** `ltijs` (Apache-2.0, npm v7.0.7, 2026-10-06), or [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 MIT, npm `@lti-tool/core` v1.3.2) when the target is **Lambda or Cloudflare Workers**. **PHP:** `packbackbooks/lti-1p3-tool` (Apache-2.0, packagist v6.4.4). 🔴 **Not** the standards-body copy `p390` cited (2,333 days stale) and **not** `pylti1.3` (1,431 days) — but `p391`'s conclusion from that second fact, *"a Python agent sits behind a Node or PHP edge rather than speaking LTI itself"*, is **withdrawn**: `Gap 391-A` is closed and the extra service comes out of the budget.

**Why FSRS matters here:** it has published parameters, so "the student is retaining more" is a
number you can defend to a ministry, offline, without telemetry.

🟢 🆕 `p389` **Two components that remove a server from this pattern, which is the cost line that
actually kills offline deployments.**

1. **Lesson delivery with no application server at all.**
   [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (**MIT**, committed **0 d**) exports a
   finished classroom as **one self-contained offline HTML file that plays the lesson** (or as a PPTX
   that keeps every scene). 🔵 **So the authoring server and the delivery target separate cleanly:**
   generate lessons once where there is power and bandwidth — a ministry office, a regional hub, a
   studio — and ship HTML files to the edge, where they need nothing but a browser. That is a
   fundamentally cheaper edge than "a Kolibri server per school", and the two compose: Kolibri remains
   the catalogue, progress store and sync layer; the exported HTML is the content it serves. 🟡 The
   export is a *playback* artefact — the agentic mid-lesson chat needs the server — so scope it as
   narrated, interactive courseware, not as a tutor that answers back offline.
2. **Notebook exercises with no per-student compute.**
   [jupyterlite/jupyterlite](https://github.com/jupyterlite/jupyterlite) (**BSD-3**, 6 d) runs the
   kernel **in the browser via WebAssembly**: no container, no install, no server, and it works offline
   once the page is cached. For a CS or data-science module this deletes the single largest
   infrastructure line in `Pattern B` at the edge. 🟡 No server also means no server-side autograding —
   collect the notebook and grade it with `nbgrader` when a link is available.

🔵 **What this pattern now says to a ministry.** The old answer was "a server per school, syncing when
it can." The 2026 answer is **generate centrally, deliver as files, compute in the browser, sync
progress when a link exists** — and every component in it is MIT or BSD-3, so the ministry owns the
deliverable outright. 🔴 One licence caution unchanged: H5P content stays **runtime content** under
GPL-3.0, never linked code.

---

## Pattern E — Sovereign EMEA public-sector stack

**For:** European public-sector clients demanding both data sovereignty and code ownership.

**Wiring:** **[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, default ref `master`)**
as the platform — **the only major open-source LMS a studio can extend with closed code** →
[serlo/serlo.org](https://github.com/serlo/serlo.org) (**Apache-2.0**) or
[oppia/oppia](https://github.com/oppia/oppia) (**Apache-2.0**, default ref `develop`) for structured
content → [openfun/richie](https://github.com/openfun/richie) (**MIT**, default ref `master`) as the
public catalogue → permissive agents over LTI 1.3 → all EU-hosted.

**The alternative, when the client insists on the openDesk lineage:** **ILIAS (GPL-3.0, default ref
`release_11`) + OpenProject behind a single SSO** — the ZenDiS pattern, and ZenDiS co-develops with
France's DINUM (LaSuite). 🔴 **But do not quote "8,600 schools":** that figure traces to a single
news item, and this pass found **no school deployment of openDesk in any source**. Named users are
administrative bodies. Sell the architecture, not the number.

**Dated compliance roadmap to attach to the bid** — this is the part competitors get wrong:
| obligation | when | status |
|---|---|---|
| Art. 4 AI literacy (every organisation using AI) | **since 2 Feb 2025** | 🔴 already binding |
| Emotion recognition in education | **prohibited since 2 Feb 2025** | 🔴 design it out |
| Art. 50 transparency | **from 2 Aug 2026** | 🔴 **not delayed** |
| Stand-alone high-risk education systems (admissions, assessment, proctoring, AI-detection in assessment, path-steering personalisation) | **2 Aug 2026 → 2 Dec 2027** per **Regulation (EU) 2026/1744** (OJ 24 Jul 2026) | 🟢 14 months of runway |

---

## Pattern F — Teacher-facing instructional assistant (the pattern the market and the regulator agree on)

**For:** LATAM and ANZ especially, where student-facing generative AI is either commercially
unproven or politically restricted.

**Wiring:** [satvik314/educhain](https://github.com/satvik314/educhain) (**MIT**) for lesson plans,
quizzes and question banks → [openedx/edx-ora2](https://github.com/openedx/edx-ora2)
(**AGPL-3.0**, run as the platform's own service) for rubric-based open-response assessment with
the human grade-of-record → [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) (**MIT**) so the
prompt pipeline has a metric attached instead of being hand-tuned →
[academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**, Spanish built in) or
[openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) (**LGPL-3.0**, default ref
🔴 `19.0`) where the administrative record has to move too.

**Why it sells:** HolonIQ's 2026 LATAM EdTech 100 finds regional AI concentrated in **teacher-facing
instructional tools rather than consumer tutoring**; Brazil's PL 2.338/2023 reportedly targets
**student selection**; DC bans AI in grading, discipline, IEP and teacher evaluation; ANZ shows the
highest ban support in the Ipsos 2026 data. **Teacher-facing-only must be an architectural switch,
not a retrofit.**

---

## Pattern G — Provenance and labelling in the generation path (APAC, overdue)

**For:** anything shipped into **India** (amended IT Rules: prominent labels **and provenance
markers** on AI-generated content from **20 Feb 2026**) or **China** (AI-content labelling measures
applicable from **1 Sep 2025**; 988 services filed by 30 Jun 2026).

**Wiring:** label and sign **at generation**, not at display — every artefact an education agent
emits (generated question, feedback text, summary, image) carries a label and a provenance record
from the moment it is created; the LMS stores the record alongside the artefact (Moodle web services
/ MCP, Canvas API) so an audit can reconstruct what was machine-made months later; the student-facing
surface renders the label rather than deriving it.

**Why it is a build, not a memo:** if labelling happens in the UI, every export, API call and
copy-paste strips it. The requirement is on the content, so the marker belongs in the content
record. Most tutoring products shipped into IN/CN today do not do this and are already out of time.

---

## Pattern H — 🆕 `p384` Prerequisite-aware tutoring, grounded on a curriculum graph you must **not** fork

**For:** the adaptive-learning engagement everyone pitches and nobody can substantiate — "the tutor
knows what the learner is missing". The missing ingredient was never the model; it was a
machine-readable map of what must be mastered **before** the next topic. One now exists.

🔴 **Read this first.** [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)
is licensed **ODbL** (`main/LICENSE`, 25,289 B), a **share-alike database licence**, and it has
**no code grant**. The whole pattern is built around keeping it on the right side of §4.4:

| what you do | ODbL clause | obligation |
|---|---|---|
| Tutor **output** grounded in the graph — next-topic choice, lesson plan, explanation, diagnosis | **§4.3** *Produced Work* | 🟢 **Attribution notice only.** Nothing to release. ODbL supplies the wording: *"Contains information from DATABASE NAME, which is made available here under the Open Database License (ODbL)."* |
| Shipping the graph **extended or merged** — client topics added, standards remapped, graph re-cut | **§4.4** *Derivative Database* | 🔴 **Share-alike.** Must be publicly used only under ODbL / a later ODbL / a compatible licence. §4.4(b): extracting *"the whole or a Substantial part of the Contents into a new database"* **is** a Derivative Database. |

🟢 **So the architectural rule is one sentence: join, never merge.** The client's curriculum data
stays in the client's own store; the taxonomy stays a read-only input resolved at query time. Break
that rule and the client's curriculum map becomes an ODbL obligation.

**Wiring:**
1. **Load the graph read-only, in its own store.** `data/topics.json` (1,930 micro-topics, each with
   a plain-language description, mastery **evidence** criteria, a type — conceptual / procedural /
   representational / language / meta — subject, domain and an approximate age range) and
   `data/dependencies.json` (4,102 edges, `topicId` → `prerequisiteId`, each tagged `hard`/`soft`
   with a one-line reason). 🔵 Keep it in a **separate schema or database** from anything client-
   specific, and never write client rows into it — that separation *is* the §4.4 firewall, and it
   should be visible in the deployment diagram so counsel can see it.
2. **Map the client's own curriculum to it by reference, not by insertion.** A join table
   `client_objective_id → topicId` in the **client's** store. The taxonomy's standards alignments
   (**NGSS, Common Core, UK National Curriculum**, Australian curriculum — Mathematics 442
   alignments across 325 topics, English 630/267, Science 245/131, HASS 210/124) usually give you
   the hook. 🟡 Unmapped client objectives are a **finding to report**, not a gap to paper over.
3. **Diagnose with the graph, not with the model's intuition.** Walk the DAG backwards from the
   failed topic over `hard` edges to find unmet prerequisites. This is a **graph traversal, not a
   generation** — deterministic, inspectable, and the reason the pattern can survive an audit that
   a pure-LLM "diagnosis" cannot. Treat `soft` edges as ranking hints only.
4. **Attach the tutor.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (**Apache-2.0**) for
   persistent learner memory plus RAG over the learner's materials, with the traversal result from
   step 3 injected as the lesson objective. Teacher-facing variant: feed the same unmet-prerequisite
   list to [satvik314/educhain](https://github.com/satvik314/educhain) (**MIT**) to draft the
   remediation worksheet — which is the side of the market that is actually growing (Trend 5).
5. **Schedule the retention.** [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki)
   (**MIT**) over the mastered topics. The graph says *what* to review next; FSRS says *when*, with
   published parameters. 🟢 Together they make "personalisation" two measurable quantities instead
   of a claim.
6. **Deliver it through the client's existing LMS**, per **Pattern A** — `webservice_mcp` for
   Moodle, [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (**MIT**) for Canvas. For
   K-12 student records, [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (**GPL-2.0**,
   ref `master`) over its API — never linked.
7. **Prove it on the prerequisite claim specifically.**
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (**MIT**) with
   [GSM8K](https://github.com/openai/grade-school-math) (**MIT**) for the multi-step maths chain.
   🟢 The honest measurement here is not a headline score: it is **whether remediating the
   prerequisite the graph identified improves the dependent topic**. That is an A/B the client has
   never been offered, and it is the whole value of the pattern.
8. **Ship the attribution notice.** §4.3 costs one line in the product's about page and the
   documentation. Put it in at step one; retrofitting a notice after a client review is avoidable
   embarrassment.

🟡 **Scope the research claim honestly.** The taxonomy's teaching-research payload
(`data/teaching-research.json`, ~24 MB) covers **1,049** topics — Science and Mathematics — and the
maintainers state that **881 topics have no research in this release**. "Research-backed guidance"
is true for roughly half the graph. Check which half a client's subject mix lands in **before** the
claim reaches a deck.

🔵 **Coverage note:** `v1` is primary/elementary and strongest on the Australian and US/UK
standards. Secondary and vocational curricula are not covered — for those, this pattern is the
*shape* to build, with the client's own map in place of the taxonomy.

**Licence posture:** client-owned code is MIT/Apache throughout. Two non-permissive components, both
held at arm's length: the **taxonomy** (ODbL, read-only input, joined never merged — §4.3 notice
only) and the **LMS/SIS** (GPL, reached over a published protocol). **Deliverable stays closed.**

---

## Pattern M — 🆕 `p385` The agent-native classroom (when the client has **no** LMS to bolt onto)

**Pattern A inverts the usual build: an agent over the client's existing LMS. Pattern M is for the
engagement where there is no LMS worth integrating** — corporate L&D, a bootcamp, a professional body,
a ministry pilot — and the deliverable is the learning loop itself, not a Moodle plugin.

**The shape.** The classroom is an **MCP server**; the agent is bring-your-own and replaceable. That
inversion is what makes it worth a pattern: the client is not buying a model, so a model swap (or a
provider outage, or a procurement decision two years out) does not invalidate the asset.

| layer | component | licence | why this one |
|---|---|---|---|
| Classroom / state | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | 🔴 AGPL-3.0 (`main`) · 🟢 MIT at `v0.1.0` | ~50 MCP tools over courses, lessons, graded exercises and a persistent learner memory. Read **Pattern L step 10 before you pick a ref** — this decision is the whole procurement question |
| Retention scheduling | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 MIT | learn-shell schedules flashcards with FSRS already; use the upstream parameters so retention is a published model, not a vendor claim |
| Course material ingest | [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | 🟢 Apache-2.0 | the client's PDFs, DOCX and slide decks are the corpus |
| Grounding | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 🟢 Apache-2.0 | document-aware retrieval over that corpus |
| Measurement | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 MIT | the before/after on the client's own subject mix, which `intel/trends.md` Trend 2 makes a procurement precondition |
| Gateway / audit | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | per-user quota and an audit log, which is what gets it past a DPO |

**Wiring.** The agent reaches learn-shell over MCP (JSON-RPC), exactly the boundary Pattern A uses to
stay clear of Moodle's GPL — so the agent code and the prompt/curriculum assets stay the client's.
`unstructured` → `ragflow` builds the grounding index; the agent writes lessons, exercises and
flashcards **into learn-shell** so the evidence of teaching outlives the context window; FSRS decides
what comes back and when; `lm-evaluation-harness` runs the before/after.

🔴 **Three things to say out loud in the pitch, because they are real:**
1. **AGPL reaches hosted use.** If you deploy `main` for the client as a service, the AGPL obligations
   attach to the deployment. The MIT `v0.1.0` tag avoids that and costs you every fix since
   2026-08-16. There is no third option, and this is the decision, not a detail.
2. **v1 is single-machine and unauthenticated by the maintainer's own description.** It is a pilot
   substrate. Multi-tenant auth, isolation and backup are *your* scope — budget them, do not discover them.
3. **It is one maintainer's project.** Weigh that against what it replaces: the alternative is building
   course/lesson/exercise/memory state from scratch, which is the part of this pattern nobody costs correctly.

🔵 **When NOT to use this.** If the client already runs Moodle, Canvas or Open edX, **Pattern A is
strictly better** — the learner records, rostering and gradebook already exist and integration beats
migration. Pattern M is for a greenfield loop, and its honest competitor is not an LMS but a spreadsheet.

## Pattern N — 🆕 `p386` Harden a student-side LMS MCP server into one an institution can deploy

**When to use it.** The client runs **Blackboard, D2L/Brightspace, Canvas or Moodle** and wants an
agent over it. As of `p386` there is a granted community MCP server for **every** one of those
platforms (see [`agents/top.md`](../agents/top.md#the-blackboard-and-d2l-supply-measured)) — so this
is never a greenfield build. 🔴 But **11 of the 12 granted Blackboard/D2L servers authenticate as the
signed-in student**: they ride the user's own browser SSO session, hold whatever rights that user
holds, and have no audit trail. **Licence-clean and still undeliverable.** This pattern is the gap
between the two.

**The parts.**

| role | pick | licence | why this one |
|---|---|---|---|
| Blackboard, institution-grade start | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | 🟢 MIT | The only server on these shelves that targets the **official Blackboard Learn REST API** and claims OAuth2, a role gate, FERPA handling, rate limiting, PII scrub and a JSON audit log. 🟡 Self-claims — **verify by execution before you quote them** |
| D2L start | [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | 🟢 MIT | Multi-strategy auth (TOTP/OAuth/browser), retry + circuit-breaker + cache, **opt-in** writes. The nearest thing to a hardening base on D2L |
| Canvas start | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | 🟢 MIT | The clean default; [mdweaver](https://github.com/mdweaver/canvas-mcp) fork adds office hours and syllabus write |
| Moodle start | [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | 🟡 GPL-3.0-or-later, header-granted | First-party route: it is in **Moodle's own plugin directory**, and the agent reaches it over JSON-RPC so GPL never reaches the agent — **Pattern A**'s boundary |
| Identity / gateway | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | SSO, per-user quota and the audit log that gets a deployment past a DPO |
| Jurisdiction gate | [`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv) | — | A granted licence does not make **grade write-back** lawful where you are deploying it |

**The work, in order — this is the whole deliverable.**

1. **Replace the session with a service identity.** Swap browser-session auth for the platform's
   own OAuth2 / API-key flow against a **service account scoped to the courses in scope**. If the
   chosen server cannot do this (most cannot), this step is a fork, and it is the reason the
   engagement exists.
2. **Scope by role, server-side.** Student / instructor / admin tool sets, enforced in the server,
   never in the prompt. A model that *can* call `update_grade` and is *asked not to* is not a
   control.
3. **Split read from write, and default write off.** Ship read-only first; put every mutation behind
   an explicit per-deployment flag. `JhostinAleck/brightspace-mcp`'s opt-in-writes design is the
   shape to copy.
4. **Gate grade write-back on the jurisdiction, before any code.** Several jurisdictions in the
   policy matrix gate or prohibit automated grading outright — Oklahoma and Maryland bar AI from
   high-stakes student decisions, the EU AI Act puts assessment in Annex III high-risk, Vietnam
   names automated assessment explicitly, and Illinois SB 2909 reaches *teacher* evaluation. 🔴 This
   gate decides the product's tool list, so run it in week one, not at security review.
5. **Add an audit trail that answers a DPO's actual question**: who (service identity + end user),
   which tool, which course, which record, when, and what the platform returned. Structured JSON to
   the client's existing log sink.
6. **Pin the contract, not the login page.** Pin the vendor API version and put contract tests
   around the tools you use; a student-side server breaks silently when the vendor restyles SSO.
7. **Carry the attribution the payload actually requires** — per **Pattern L step 11**. If you
   started from a fork-family server, the NOTICE file may owe **two** credits.
8. **Prove it before handover.** Execute the maintainer's claims rather than quoting them: run the
   role gate against an under-privileged token, confirm the audit record exists for every mutation,
   and confirm the PII scrub on a real transcript.

🟢 **Why this sells.** It is small, bounded, and the client can show the output to their
data-protection officer — and it is available on every major LMS today, because the licences are
already clear. 🔴 **Say the honest part too:** on D2L all six granted servers are student-side, so
step 1 there is a genuine build and should be costed as one, not as a configuration.

## Pattern O — 🆕 `p387` The LATAM engagement, built on what the region already shipped

**For:** a Brazilian or Spanish-speaking LATAM client — ministry, municipality, university or
school network — where the deliverable has to be in the local language, aligned to the *national*
curriculum, and deployable by an institution rather than demoed to one.

**The premise this pattern corrects:** the LATAM supply is not empty. Every component below is a
real address with a grant read first-hand on 2026-10-22.

**Wiring, Brazil (the fully-specified case):**

1. **Start from the national curriculum, not from a prompt.**
   [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores)
   (**MIT**, `main`) already anchors generation to **BNCC** skill codes and **discards an invented
   code before the teacher sees it**. Keep that gate and extend it: the gate *is* the trust story,
   and it is the same mechanism `Pattern H` specifies against a curriculum graph.
2. **Deliver through the LMS the client runs, never a new portal.** On **Moodle**, the
   `webservice_mcp` plugin per **Pattern A**; on **Open edX**, start from
   [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) (**MIT**, `main`), which is already an
   XBlock/plugin with a teacher statistics panel, TTS and cross-session context.
   🔴 **Licence boundary, non-negotiable:** TutorIA's MIT grant covers *the plugin*. Open edX is
   **AGPL-3.0** and hosting it is hosting AGPL software. Keep the agent a **separate service** the
   plugin calls over HTTP, keep the plugin thin, and the client's AGPL obligations stay exactly
   where they were before you arrived.
3. **Integrate the student-record system over its API.**
   [portabilis/i-educar](https://github.com/portabilis/i-educar) (**GPL-2.0-or-later**, real default
   ref **`2.12`**) is what a Brazilian municipality is running. Read rosters and write results
   through its API; **do not fork it** — the fork pulls GPL into the deliverable and buys nothing.
   (Its sibling `i-diario` is AGPL-3.0; check per repository, not per organisation.)
4. **Make it multi-tenant before anyone calls it a pilot.** A school network is many tenants. On
   Moodle, [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager)
   (**GPL-3.0-or-later**, in `version.php`) supplies exactly this — per-role provider routing, rate
   limits, per-tenant enable/disable, usage monitoring — and it reaches the agent over its own API,
   so the copyleft stays on the Moodle side. On Open edX, build the tenant boundary per
   **Pattern N** steps 1–5.
5. **Run it where connectivity is the constraint**, which is the actual deployment profile for
   TutorIA's own users (rural Risaralda) and for most of the nine Google.org rollout countries:
   [Kolibri](https://github.com/learningequality/kolibri) (**MIT**, default ref `develop`) per
   **Pattern D**, with a local open-weight model behind the AI manager's **Ollama** tool rather than
   a metered API.
6. **Schedule retention, in the local language.**
   [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) (**MIT**) for the scheduler; the
   content language is a data property, not a code property, so this layer ports unchanged.
7. **Measure in the language of instruction, and publish the baseline.**
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (**MIT**) with
   Portuguese/Spanish task sets built from the client's own past assessments. 🔴 Do **not** ship an
   English benchmark number as evidence for a Portuguese deployment.
8. **Say out loud what you are adding.** The agents exist and are MIT; **tenancy, support,
   governance and curriculum QA are the deliverable.** That is a defensible studio pitch and an
   honest one — and it is cheaper for the client than the rebuild a "no LATAM supply" story implies.

**Spanish-speaking variant:** swap step 1's BNCC grounding for the client's national curriculum
standard, keep TutorIA (Spanish-first) at step 2, and use
[academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**, Spanish built in) or
[Chamilo](https://github.com/chamilo/chamilo-lms) (GPL-3.0) where no SIS/LMS is in place.

🟡 **Two addresses this pattern deliberately does not use, and why.**
[Daniel-ux1026/Tutor-Inteligente](https://github.com/Daniel-ux1026/Tutor-Inteligente) (Peru) is the
offline-first PWA tutor with explainable difficulty selection that step 5 would otherwise want — it
has **no grant at any of eight probed paths**, so it cannot enter a deliverable, and asking its
author to add a licence is the cheapest possible contribution to the region's supply.
[henriquebotelhogomes/educacao](https://github.com/henriquebotelhogomes/educacao) (Brazil, RAG
tutor, default ref `master`) is ungranted for the same reason.

---

## Pattern P — 🆕 `p388` The parent and guardian surface (and the FERPA line that splits it in two)

**For:** a K-12 district, school group or education provider that is being asked — by statute, by
families, or by its own board — to make a student's progress legible to parents, and an engagement
that wants a real deliverable rather than another policy PDF.

🔴 **Read this first: this is two different products, and conflating them is how the engagement
fails.** The code is the same; the obligations are not.

| | **P-1 · parent-side** | **P-2 · district-side** |
|---|---|---|
| Who holds the credential | the **parent**, for their own child | the **institution** |
| What a read is | a parent exercising their own access | a **FERPA-governed disclosure of an education record** |
| Tenancy | none needed — single user, single family | **full multi-tenant**, per-district, per-role |
| Who buys | a provider bundling it, or nobody (it is a tool, not a sale) | the district, through procurement |
| Build cost | days | the real engagement |

**Components (all verified first-hand 2026-10-22 — [`verified-repos`](../evidence/verified-repos.2026-10-22-p388.tsv)):**

- **Infinite Campus (SIS):** [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp)
  — `main` · `971d58f`, 🟢 **MIT** (1,067 B), **47 npm releases → 2026-10-19**. 20 tools over **Campus
  Parent**: schedule, assignments (`missingOnly`), grades plus a 14-day recent window, **attendance
  events with codes and comments**, behavior, food service, documents, standardized **assessment
  scores**, fees, and messaging from three distinct sources. Linked districts auto-discovered via
  **CUPS SSO**; `FeatureDisabled`-aware, so a district with a module switched off degrades instead of
  erroring — which is what makes it deployable across a group of districts rather than one.
- **Canvas (LMS):** [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp)
  — `main` · `428b78b`, 🟢 **MIT** (1,067 B), **43 releases → 2026-10-16**. 18 `canvas_*` tools held
  to the **read-only observer scope** (`canvas_list_observees` is the hinge), plus student
  self-access. Four auth modes in priority order. 🟢 Copy its download hardening rather than
  re-inventing it: host-pinned to the Canvas origin, confined to a download directory, never writes
  through a symlink, new files `0600`.

### Wiring P-1 (parent-side) — days, not weeks

1. Parent installs the MCP server locally against **their own** portal credential (token, OAuth, or
   session). Nothing is hosted; no institutional agreement is needed because no institutional
   credential is used.
2. Keep it **read-only**. Both servers are already scoped that way; do not add write tools. A parent
   agent that can submit work on a child's behalf is an academic-integrity incident waiting to be
   filed.
3. Add a **digest** rather than a chat surface: *"what changed this week, what is missing, what is
   due."* 🔵 The persona's actual job is **noticing**, not conversing — the portal already answers
   questions, badly, and nobody logs in.

### Wiring P-2 (district-side) — the real engagement

1. 🔴 **Do not host the parent-side tool for the district.** The moment the credential is
   institutional, every read is a FERPA disclosure. Build the institutional path deliberately:
2. **Put the district's own identity in front of it.** Parent identity comes from the district IdP,
   and **the parent↔student relationship is authoritative from the SIS** — never from a claim the
   agent accepts. `ic_list_students` / `canvas_list_observees` define the blast radius of the whole
   system, so that relationship check is the security boundary, not a feature.
3. **Borrow the tenancy layer that already exists.** This is the same problem `p386` identified for
   student-side LMS servers, and `Pattern A`'s answer applies unchanged: per-tenant configuration,
   per-role rate limits and usage monitoring — on Moodle,
   [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager) is the
   worked example to copy the *shape* of.
4. **Log every read as a disclosure, not as a request.** Who asked, for which student, which fields,
   under which relationship, at what time. 🔵 This log is the deliverable a district's counsel signs
   off on, and it is cheap to build on day one and near-impossible to retrofit.
5. **Keep the model away from the record where you can.** Fetch and render deterministically;
   use the model for **summary and prioritisation over data already authorised**, not as the thing
   that decides what to fetch. Smaller surface, smaller disclosure, cheaper review.
6. **Ship the translation layer — it is the actual product.** Gradebook rows are not an answer to
   *"is my kid okay?"* Convert to plain language, in the family's language, at a reading level the
   district specifies, with **no inference about the child beyond what the record states**. A tool
   that volunteers *"your child seems disengaged"* has invented an education record.

**Guardrails:**
- 🔴 **No predictions, no risk scores, no labels.** A parent-facing risk score about a student is
  the high-stakes automated decision Oklahoma and Maryland's frameworks are written to restrain, and
  under the EU AI Act Annex III it is squarely high-risk. Report the record; do not score the child.
- 🔴 **Attendance, behavior, food-service and fee data are the sensitive tail.** `infinitecampus-mcp`
  exposes all four. Free-lunch status and behavior records are the fields a district will refuse last
  and worry about most — scope them out explicitly unless the district asks for them in writing.
- 🟡 **Both servers authenticate as a person.** Treat credential custody as the top risk in the
  design review; a stored parent credential in a studio-hosted service is the worst of both worlds.
- 🔵 **Multiple children, multiple districts.** `ic_list_districts` + CUPS SSO exist because families
  span districts. Test the two-children-two-districts case before a demo; it is the common case and
  the one that breaks naive implementations.

**Why this pattern is worth having at all:** it is the only education surface this base has found
with **granted, maintained components and no incumbent vendor** — the parent portal is a feature of
the SIS, not a market. And **family transparency is already in the statutes** (Oklahoma SB 1734
names it; Maryland's Chapter 634 is built on guidance districts hand down), so the buyer has an
obligation and no product. 🔵 See `Trend 10` in [`intel/trends.md`](../intel/trends.md).

---

## Pattern Q — 🆕 `p389` The generated classroom, governed (and what it supersedes in `Pattern M`)

**For:** a client with **no usable LMS** — a corporate academy, a ministry training programme, a
vocational provider, a new institution — who needs **teachable lessons in weeks, not a platform in
quarters**. Also the fastest credible answer to the EMEA teacher-training demand recorded in
[`intel/market.md`](../intel/market.md): the UAE has **22,000 teachers and education professionals**
to train on a curriculum that became compulsory by Cabinet decision.

**The base:** [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 🟢 **MIT** (read from the
payload at `main` @ `269fde2d991f`; `package.json` agrees), Tsinghua University, **committed
2026-10-22**, ~41.3k ★, **JCST 2026** paper, grown out of the internal **MAIC** system and validated
on **700+ students**. 🔴 **Pin `v1.2.1` (2026-10-18), not head.** Head is `v1.3.0-rc.1`, and the
project states breaking upgrade conditions with **no rollback below that release** — a pilot does not
want to be the first to find that out.

### Wiring

1. **Stand up the authoring server.** Node ≥ 22.19, pnpm ≥ 10, **PostgreSQL 16**, a long-running
   server (🔴 **not Vercel** — Vercel deployments are capped at the 1.1.x line, so "we'll host it
   serverless" is a downgrade). Generation is **server-first** from v1.2.0: it survives closed tabs and
   restarts, which is what makes it usable by teachers rather than by engineers.
2. **Write the governance file first, before any content.** `openmaic.yml` declares **providers** and
   assigns every AI use — a named **slot** (`llm`, `course.outline`, slide content, TTS, web search,
   `video`) — to one of them, with keys referenced as `${VAR}` from `.env.local`. 🟢 **Three settings
   are the compliance deliverable, not configuration:** pin each slot to the provider under the
   client's own contract; set the server to **forbid user-supplied keys**, so no teacher can route
   student work through an unvetted account; and set unused capabilities to `null` rather than leaving
   them available. 🔵 **This file is the artefact that answers a district's or ministry's AI policy
   question** — *which model saw student input, under whose contract* — in one reviewable, diffable
   page. Almost nothing else in this base can answer it at all.
3. **Ground the content in the client's curriculum, not in the model.** Feed the jurisdiction's own
   material through the **knowledge base** (v1.3.0 line) or as per-course uploads — parsed once and
   reused — and where a standards graph exists, drive the lesson plan from it rather than from a
   prompt: [`os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) (🔴 **ODbL-1.0 — a database
   licence; reach it over a service, do not fork it into the deliverable**, per `Pattern H`), or
   [`bc-curriculum-mcp-server`](https://github.com/pdg6/bc-curriculum-mcp-server) (**MIT**) for a
   North American engagement — 🟡 whose crawl is **209 days** old, so budget the re-crawl its MIT grant
   permits.
4. **Keep the record of record outside it.** 🔴 OpenMAIC has **no enrolment, no gradebook of record,
   no transcripts and no stated LTI story**. Pair it with the administration base the client already
   runs or should: [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (GPL-2.0, over its API),
   [academico](https://github.com/academico-sis/academico) (**MIT**) at SME scale,
   [i-educar](https://github.com/portabilis/i-educar) (ref `2.12`) for Brazilian municipal work, or
   [OpenEduCat](https://github.com/openeducat/openeducat_erp) (LGPL-3.0) where an ERP is wanted.
   **Completion and scores flow out of OpenMAIC into that system; identity and enrolment flow in.**
5. **Add the mastery model it does not have.** Quiz results are events, not a mastery estimate. Fit
   [`pyBKT`](https://github.com/CAHLR/pyBKT) (**MIT**, 1 d) on the quiz log per skill, as in the
   revised `Pattern B`, and use it to choose the next lesson. 🟢 This is also what keeps the
   high-risk-assessment line on the right side: the progression decision becomes **a published model
   plus a human review step**, not a generation.
6. **Deliver to the edge as files.** Export each finished classroom as **one offline HTML file** (or
   PPTX). See `Pattern D` — authoring stays central, delivery needs only a browser.
7. **Run the models where the data has to stay.** **Lemonade** for local inference and **FunASR** for
   local ASR are supported paths, not forks — so a deployment that may not send audio or text
   off-premises is a configuration change.

### Why this supersedes `Pattern M` for institutional delivery

`Pattern M` is built on [learn-shell](https://github.com/sf-shenfeng/learn-shell), whose v1 is
explicitly **single-machine and unauthenticated**, and whose grant is **AGPL-3.0 at `main`** (MIT only
at tag `v0.1.0`). That is a fine shape for an individual learner and an impossible one for an
institution. OpenMAIC is **MIT at head**, server-first, multi-user, with central model governance and
a published security practice — five releases since September 2026 carrying SSRF, DNS-rebinding,
token-expiry and provider-redirect fixes under **GHSAs**. 🔵 **Keep `Pattern M` for the
bring-your-own-agent, one-learner case; use `Pattern Q` whenever a client is the buyer.**

### Guardrails

- 🔴 **Auto-graded quizzes are the regulated surface.** Assessment is **Annex III high-risk** in the
  EU and named explicitly in **Vietnam's Decision 33/2026/QD-TTg**. The trigger in both is a decision
  taken on the system's output **without meaningful human review**, so ship the human review step for
  anything consequential and keep its audit trail. A practice score is not consequential; a module
  pass that gates progression is.
- 🔴 **Simulated classmates must be labelled.** An AI teacher with a voice and AI peers in a classroom
  is exactly the surface **EU AI Act Art. 50** transparency and China's labelling rules address, and
  `Pattern G` already covers the mechanics. Label in the UI, not in the terms of service.
- 🟡 **Generated content is a draft until a teacher signs it.** The 2026 procurement trend is evidence
  of instructional benefit; a lesson nobody reviewed cannot be put in front of a class at a client's
  reputational risk. Make teacher review a workflow state, and bill it — it is the part of the
  engagement that is actually about teaching.
- 🟡 **Language and regional fit:** interface is **EN + zh-CN** and the provider catalogue is built for
  a market that includes DeepSeek and Kimi. For a Gulf or LATAM engagement, **localisation of the
  teaching surface is a line item**, and there is no Arabic-first alternative in the open-source supply
  (see `intel/market.md`, EMEA).

---

## Pattern V — 🆕 `p390` The spoken tutor, and the two things that make or break it

**For:** learners who cannot or will not type their way through a lesson — early grades, low typing
fluency, shared-device households, visually impaired learners, and language learning where
*pronunciation is the skill being assessed*. This is also the pattern that reaches the LATAM and
APAC households `Trend 10` describes, where the phone is the only device.

**Why it is a separate pattern:** a voice tutor is not a text tutor with TTS bolted on. Two
properties decide whether a child keeps talking to it, and neither is in the LLM:

1. **Turn-taking.** The tutor must know when the learner has stopped speaking, tolerate a
   four-second pause while a 9-year-old thinks, and **stop talking the moment it is interrupted**.
2. **Latency budget.** Past roughly a second of silence the learner starts talking over it, and the
   session degrades into collision recovery.

**Wiring:**

1. **Do not write the voice loop.** [`livekit/agents`](https://github.com/livekit/agents)
   (🟢 **Apache-2.0**, dated 2026-10-22) is the substrate: full-duplex WebRTC transport, pluggable
   STT/LLM/TTS, **turn detection, interruption and barge-in handling**. All three legs are
   provider-swappable, which is what makes step 4 possible.
2. **Start from the working reference.** [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent)
   ("Manu", 🟢 **MIT**, dated 2026-10-07) is a pt-BR maths tutor on exactly that substrate, scaling
   its explanation from 1st grade to university. 🔴 Its README says **"in development" with no public
   deployment** — take the pipeline and the prompt-scaffolding, not a production claim.
3. 🔴 **Put a symbolic checker behind any arithmetic.** Manu's correctness layer is the LLM itself.
   For a maths tutor that is the one unacceptable gap: route every numeric or algebraic claim through
   SymPy (or the client's own CAS) and have the agent *read back* the verified result. A spoken wrong
   answer is harder for a learner to catch than a written one — there is no transcript to re-read.
4. **Localise the ASR, not just the prompt.** Accent and dialect coverage is where regional voice
   tutors fail. [`mozilla/common-voice`](https://github.com/mozilla/common-voice) ships **CC0-1.0**
   corpora across ~130 language variants (pt-BR, es-419 variants, Hindi, Bengali, Kiswahili) — use
   them to *evaluate* candidate ASR models on the client's actual learner population before picking
   one, and to fine-tune where the gap is real. 🟢 CC0 means no attribution and no share-alike, so
   this is safe in a commercial deliverable. 🟡 MPL-2.0 covers the **platform code**, not the corpora.
5. **Keep the mastery model outside the voice path.** Voice is an I/O channel, not a pedagogy.
   [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) (🟢 MIT, dated 2026-10-22) holds the Bayesian
   Knowledge Tracing state so "what comes next" survives a dropped call and stays inspectable — which
   is also what makes the decision auditable under step 6.
6. 🔴 **Voice raises the compliance stakes, so settle three things before the pilot.**
   - **Biometrics.** A voice recording is biometric data under GDPR Art. 9 and most LATAM regimes
     (Brazil's LGPD included). Default to **transcribe-and-discard**, keep no audio unless the client
     has a lawful basis and a retention policy, and write that down.
   - **Emotion inference is prohibited in EU education** (AI Act, in force since 2 Feb 2025) — and
     voice is the modality vendors are most tempted to infer affect from. Do not ship it in EMEA,
     and strip it from any upstream SDK feature you enable.
   - **Disclosure.** AI Act Art. 50 applies from **2 Aug 2026**: a synthetic voice must be
     disclosed as synthetic. Say it in the first turn, in the learner's language, every session.
7. **Measure it as a tutor, not as a demo.** Score the *transcripts* with
   [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness)
   (🟢 MIT) on the client's own item bank, and track interruption rate and mean response latency
   alongside learning gain — a tutor that is pedagogically right and 1.5 s slow will still be
   abandoned.

**Licence position:** Apache-2.0 substrate + MIT reference + CC0 data + MIT mastery model — the whole
chain is permissive, so this pattern can ship as a closed client deliverable with attribution only.

**What this pattern does not solve:** there is **no granted, maintained open-source voice tutor for
an African or South Asian language** on these shelves. See `Gap 390-A`.

## Pattern W — 🆕 `p391` Qualify the district *before* the pitch (North America)

**For:** a North America K-12 engagement, at the stage before anyone has written code — choosing
which districts to approach, and pricing a pilot against a budget that actually exists. Every other
pattern here answers *what to build*; this one answers *for whom, and with whose money*.

**Why it is a pattern and not a sales note:** US school AI spending is not discretionary in the way
enterprise AI spending is. It comes from identifiable federal, state and local lines, and the
largest flexible federal line — **Title I** — is allocated on **Census child-poverty counts**, not
on enrolment. A pilot proposed without that number is priced blind, and a district with a high
poverty count and a low per-pupil spend is a different conversation from the inverse.

**Wiring:**

1. **Pull the universe.** [`pipeworx-io/mcp-education-data`](https://github.com/pipeworx-io/mcp-education-data)
   (🟢 **MIT**, HEAD 2026-10-21) — `education_find_districts` for a state returns every local
   education agency with its **LEA id**, school count, enrolment and teacher counts. The `leaid` is
   the join key for everything below.
2. **Add the budget.** `education_district_finance` on that `leaid` returns revenue split
   **federal / state / local** and expenditure by function, with **per-pupil spending computed**.
   🔴 **The survey lags the directory by 1–2 years** — quote it as "FY-whatever per-pupil", never as
   current-year, or the first CFO in the room ends the meeting.
3. **Add the federal lever.** `education_child_poverty` returns Census **SAIPE** counts and rates of
   children 5–17 in poverty by district — the figures Title I formulas run on. High poverty rate plus
   low per-pupil spend identifies districts with *federal* money and *no* incumbent vendor: the
   cheapest pilot to land and the hardest to displace later.
4. **Add the surface.** `education_find_schools` carries **charter/magnet status, grade range and
   free/reduced-price lunch counts** per school, so the pilot can be scoped to named schools rather
   than to a district abstraction.
5. **Then pick the build.** Hand the shortlist to whichever pattern fits the client's platform —
   `Pattern F` (teacher-facing, the one the market and the regulator agree on) is the usual answer at
   this budget, `Pattern N` if they run an LMS already.

🔴 **Three things to decide before the first call, not after.** The integration is **unofficial** and
not affiliated with the upstream provider — fine for your own targeting, not something to resell as a
data product. The default path is a **hosted gateway** (`gateway.pipeworx.io`): the underlying data is
public federal data, but the **query pattern is not** — which districts a studio is sizing up is
commercially sensitive, so self-host before running this against a named client list. And a scoped
endpoint lists roughly **30 shared gateway meta-tools** alongside the four that matter, so budget the
context or connect once to the full gateway rather than to several pack endpoints.

🔵 **Regional honesty.** This is a **North America–only** instrument: it is NCES/Census data and has
no EMEA, APAC or LATAM analogue on these shelves. The equivalent question in those regions is still
answered by hand — recorded as `Gap 391-B` rather than left to look like coverage.

## Pattern X — 🆕 `p391` Keep the client's pedagogy as a separate, reviewable artefact

**For:** any tutoring engagement that will be audited, handed over, or argued about — which, under
EU AI Act high-risk obligations and most North American district procurement, is all of them. Also
the pattern for a studio that wants the *teaching* it built to outlive the *runtime* it shipped on.

**Why it is a separate pattern:** in nearly every tutor on these shelves, the pedagogy is diffused
through the application — prompt fragments, conditional branches, UI copy. That makes two things
expensive that clients ask for routinely: *show me the teaching policy* and *change the teaching
policy without a release*. [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor)
(🟢 **MIT**, HEAD 2026-10-21) is the first row here built the other way round, and it is worth copying
even where the repository itself is not used.

**The split, which is the whole point:**

| | owns | where it lives |
|---|---|---|
| [`universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) (🟢 **MIT**, → 2026-09-24) | **what to teach next**: diagnosis, teaching moves, pacing, when a check is passed, what the next step is | its own repository, versioned independently |
| [`dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (🟢 **MIT**) | **where it is kept**: learner state, the diagnosis map, structured lessons, the UI | the runtime, which contains **no teaching logic at all** |

**Wiring:**

1. **Put the pedagogy in a versioned repository of its own**, as prose and rules rather than code:
   diagnosis strategy, teaching moves, mastery criteria, escalation. This is the artefact a client
   reviews, a subject expert edits without a developer, and an auditor reads **without reading the
   application**. It is also the thing a studio can hand over at the end of an engagement.
2. **Make the runtime record decisions, never make them.** The runtime stores what the teaching layer
   decided and renders it; every pedagogical choice arrives from the policy artefact. Test this by
   grepping the runtime for teaching rules — if `if blocked, explain the prerequisite` lives in the
   application, the separation has already leaked.
3. **Put the assessment behind a pure function.** [`intellectif/learning-kit`](https://github.com/intellectif/learning-kit)
   (🟢 **MIT**, HEAD 2026-10-18) — `@intellectif/lk-core` gives schemas, a **pure scoring engine**,
   **rubric and deferred grading**, attempt plans and redaction, with no runtime dependency beyond
   Zod. Scoring that is a pure function is unit-testable by the client and readable by a regulator;
   **deferred grading keeps a human marker in the loop by construction**, which is what high-risk
   assessment obligations ask for rather than something to retrofit.
4. **Emit evidence, do not hoard it.** `lk-core`'s **xAPI builder** sends statements to the client's
   own LRS — [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) where one is needed — so the learning
   record stays the client's property and the tutor stays replaceable.
5. **Launch it from the LMS over a maintained LTI edge — in the agent's own language.** 🆕 `p392`
   For a **Django** agent, [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
   (🟢 **MIT**, PyPI `django-lti` v0.10.1, HEAD **2026-10-20**): one installed app, one middleware,
   one migration, **no second service**. For a **JupyterHub**,
   [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (🟢 **BSD-3-Clause**).
   For **Node**, [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (🟢 **Apache-2.0**, npm v7.0.7)
   or [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 **MIT**) if the deployment is
   serverless. 🔴 `p391`'s *"the edge is Node or PHP regardless of what the agent is written in"* is
   **withdrawn** — `Gap 391-A` is closed. The constraint that remains is a **licence** one: the
   best-maintained Python implementation, `openedx/xblock-lti-consumer`, is **AGPL-3.0**.

🔴 **What this pattern does not give you.** `dsh-diagnostic-tutor` is **v0.1.1 and early by its own
account**: no PDF or document ingestion, no RAG, no flashcards, no analytics, and **a route never
marks knowledge as mastered**. It also **requires DeepSeek Harness** — it is a harness extension, not
a standalone application, so an engagement that cannot adopt that harness should copy the *structure*
(steps 1–2) onto a tutor it can deploy, not adopt the repository. 🟢 Take the separation; shop for the
runtime.

## Pattern L — Clear a repository for reuse by **subtree**, not by its licence badge

**The one durable result of the `p3xx` apparatus**, kept as a procurement gate rather than a
narrative. Run it before any repo enters a client deliverable.

1. **Resolve the real default ref first.** `git ls-remote --symref https://github.com/<slug> HEAD`.
   **13 of 58 live addresses verified in `p383` are not on `main`** — `master`, `develop`, `dev`,
   `release`, `development`, `release_11`, and OpenEduCat's `19.0`; `p384` adds **openSIS-Classic
   → `master`**. A `main`-assuming read reports "no licence" for every one of them, and that false
   negative looks exactly like a real one.
2. **Probe more than one path — eight, not seven.** In order: `LICENSE`, `LICENSE.md`,
   `LICENSE.txt`, `LICENCE`, `COPYING`, `LICENSE-MIT`, `license`, and 🆕 **`docs/License.txt`**
   (with `doc/LICENSE` as its variant). Verified instances where the grant is *not* at `LICENSE`:
   **Moodle → `COPYING.txt`**, **Frappe LMS → `license.txt`** (lowercase),
   **ai-shifu → `LICENSE.txt`**, **lm-evaluation-harness → `LICENSE.md`**,
   **H5P → `LICENSE.txt`**, and 🆕 **openSIS-Classic → `docs/License.txt`** (17,286 B, stock
   GPL-2.0, *"Version 2, June 1991"*, corroborated by `"version 2 of the License"` headers in
   `index.php` and `Modules.php`). 🔵 `p384` added the eighth path because the seven-path read
   returned "ungranted" for **the most widely deployed open-source SIS in K-12** — a repository with
   a perfectly ordinary grant sitting one directory down.
3. **Check for a split grant.** **[microsoft/autogen](https://github.com/microsoft/autogen)**: root
   `LICENSE` is **CC-BY-4.0** (18,649 B, "Attribution 4.0 International"); the **code** grant is a
   separate file, `LICENSE-CODE` = **MIT**. One file read gives you the wrong answer either way.
   Conversely, confirm a split grant is **absent** before assuming one:
   [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) has **no** code grant —
   `LICENSE-CODE`, `LICENSE.code`, `CODE_LICENSE` and `licenses/LICENSE` all **404** — so its ODbL
   is the only grant on offer, for the tooling as well as the data.
4. **Compare byte length against the stock text.** A licence whose length is off is a licence that
   was edited. **[open-webui/open-webui](https://github.com/open-webui/open-webui)**: `LICENSE` is
   **2,819 B** against stock BSD-3's ~1,500 B — BSD-3 text **plus** a branding restriction and a
   CLA, self-titled "Open WebUI License". Not an OSI-standard grant.
5. **Read the manifest and the source headers before you call anything ungranted.** 🔴 **`p383`'s
   own first draft failed this step and `gate-enumeration` refused it.** Five repositories had no
   licence file at any of the seven paths; only **two** turned out to be ungranted.
   `DMontgomery40/mcp-canvas-lms` and `general-mudkip/d2l-mcp-server` declare
   `"license": "MIT"` in `package.json` (**manifest-only** — reusable, but record the line and ask
   for the file). `onbirdev/moodle-webservice_mcp` carries the full **GPL-3.0-or-later** header in
   `version.php`, as Moodle requires of every plugin — **granted, with no licence file at all.**
   Probe `package.json`, `pyproject.toml`, `composer.json`, the `README`'s licence section and the
   main source file's header before rejecting a repository;
   🆕 `p385` — **but read what that section *says*, not that it *exists*.** Two failure modes, both on
   these shelves: [moarshy/mcp-tutor](https://github.com/moarshy/mcp-tutor) has a `## License` heading whose
   entire body is *"This project is experimental and intended for educational and research purposes"* —
   which grants **nothing**, while satisfying any check that asks "is there a licence section?";
   [h9-tect/AI-Roadmaps](https://github.com/h9-tect/AI-Roadmaps) states *"provided under the
   [MIT License](LICENSE)"* and **that `LICENSE` link 404s**. A prose assertion is weaker evidence than a
   manifest field, which is weaker than the text itself — grade them separately and never as "MIT"; a file-only read would have wrongly
   rejected three of five, including the plugin Moodle's own directory distributes.
6. **Only now treat "no licence" as a hard stop — and it is a hard stop.** Two live, functional,
   actively advertised repositories survive every check above with no grant anywhere:
   `loyaniu/moodle-mcp` (no `license` field in `pyproject.toml` either) and
   `Seechange-edu/act-ai-tutor-backend` (no manifest at all). 🔵 Both were **re-probed at the new
   eighth path in `p384` and remain ungranted.** No grant means no right to redistribute, whatever
   the README invites you to do.
7. **Ask what the grant covers, not just what it is.** A valid, unmodified, correctly-recognised
   licence can still leave the part you are shipping ungranted — stock **ODbL** governs a database's
   *rights*, by its own preamble **not the contents of the database individually**. If you ship
   derivatives of the *contents* on the strength of "licence: ODbL-1.0", you have no grant for the
   part you shipped. Record the answer **per subtree** (`data/`, `docs/`, `scripts/`), and record
   "not stated" as distinct from "not granted".
   🟢 🆕 **This step was written abstractly in `p383`. `p384` gave it its first real instance** —
   `os-taxonomy`, ODbL, no code grant — and the concrete reading is now **Pattern H** below. The
   step was right in advance, which is reason to trust it on the next data artefact: education runs
   on standards, item banks and curriculum maps, so this will not be the last one.
8. **Re-check dead addresses.** Four in common circulation do not resolve: `apereo/opencast`,
   `edx/openassessment`, `openedx/openassessment`, `OpenEduCat/OpenEduCat`. Live replacements in
   [`repos/foundations.md`](../repos/foundations.md).
9. 🆕 **Confirm there is a *tree*, not just a *ref*.** `git ls-remote` on
   [projectfedena/fedena](https://github.com/projectfedena/fedena) returns two heads — and every
   content path at `master` (`README`, `README.md`, `LICENSE`, `Gemfile`, `app`) returns **404**.
   **`ls-remote` proves a ref, not a payload**, so step 1 can pass on a repository that has nothing
   in it to licence. A vendor article lists this slug as an Apache-2.0 SIS; the correct record is
   **"nothing read"** — neither granted nor ungranted. Any address census built on resolution alone
   over-counts the supply.

10. 🆕 **Read the grant at the ref you are shipping — the licence is a property of the *ref*, not of the
    repository.** [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) is **AGPL-3.0** at
    `main` (`LICENSE`, 34,523 B, stock) and **MIT** at tag **`v0.1.0`** (`LICENSE`, 1,081 B,
    *"Copyright (c) 2026 Learn Shell contributors"*). Both were read first-hand in `p385`; the project
    relicensed on **2026-08-16**. 🔵 This base already knew relicensing happens —
    `snflwr-ai/snflwr.ai` went AGPL-3.0 → proprietary (`p241`), `AIHawk` went MIT for releases after a date.
    What `p385` adds is the **direction that favours the buyer**: permissive → copyleft, with the permissive
    grant **still retrievable at a tag**. 🔴 The trap in both directions is a cached audit. "We cleared that
    repo as MIT last quarter" is a statement about a ref that has moved. Record **slug + ref + licence +
    date-read**, never slug + licence — and re-read before each release, not once per engagement.
    🟡 And when you pin a tag to keep a permissive grant, say out loud what it costs: a frozen tree, no
    upstream fixes, and a maintainer who has signalled they do not want that code used on those terms.

11. 🆕 `p386` **Classify a byte-length anomaly before you judge it — "longer than stock" has two
    opposite meanings.** Step 4 says a non-stock length means the text was edited. True, and `p386`
    found the benign half of that read, which a length check alone cannot distinguish from the
    hostile one:

    | repo | bytes | the excess is | what you do |
    |---|---|---|---|
    | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 2,819 (BSD-3 ≈1,500) | 🔴 **added restriction** — branding clause + CLA | walk away, or get written permission |
    | [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | 1,200 (MIT ≈1,065) | 🟢 **added attribution** — inline notice, *"Portions … derived from brightspace-mcp-server, Copyright (c) 2026 Rohan Muppa, used under the MIT License"* | ship it, carry the extra notice |
    | [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP) | 2,181 | 🟢 **two complete MIT grants concatenated** — its own plus `d2l-cli`, © 2026 Aaryan Kapoor | ship it, carry **both** notices |
    | [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 11,906 (Apache-2.0 ≈11,358) | 🟢 **ASF's appended notice text** | ship it, keep `NOTICE` |

    🔵 **So the test is not "is the length stock?" but "does the delta add a condition or a
    credit?"** Added conditions are procurement stops. Added credits are NOTICE-file entries — and
    they are *obligations you inherit silently*: ship `D2L-MCP` and you owe attribution to a project
    you never chose, which no SBOM built from a licence **identifier** will tell you.
    🟡 Record the delta's content, not just the byte count.

12. 🆕 `p386` **Count grants, not addresses — and never let a count of zero reads print as
    "ungranted".** For four passes [`agents/top.md`](../agents/top.md) said *"Blackboard has nine
    servers and not one verified grant; D2L has six and the only one checked is ungranted"*, and
    concluded both platforms needed a permissive server built. `p386` probed all fifteen: **6 MIT on
    Blackboard, 6 MIT on D2L**. 🔴 The grants existed; the reads did not. A harvest column headed
    *"distinct slugs"* answers **how many addresses exist**; `LIVE-GRANTED` / `LIVE-NOGRANT` answers
    **how many were read**. When the second number is zero the honest word is **unread**, and the
    cost of the wrong word here was a false build recommendation on two platforms.
    🔵 Before any shelf states a supply gap, state which census it is quoting.

13. 🆕 `p387` **Date the artefact you are about to ship, in the registry.** A grant tells you whether
    you *may* use it; a publish date tells you whether anyone is still there. Read the package name
    from the manifest at the real default ref, then:
    `curl -s https://registry.npmjs.org/<name>` → `dist-tags.latest`, `time.created`,
    `time.<latest>`, `versions.<latest>.license`, `.repository`; or
    `curl -s https://pypi.org/pypi/<name>/json` → `info.version`, `info.license`,
    `releases[*].upload_time`. 🟢 Three usable outputs: a **second, independently published grant**
    (a manifest-only MIT becomes an MIT published to a registry); a **maintenance date** that
    survives `api.github.com` being 403; and the discovery that an address ships **no artefact at
    all**, which is a different conversation with a client than "it is old". 🔴 `p387` found a
    four-and-a-half-year-stale dependency inside a pattern on this page, a 16-month-stale server
    recommended for its tool count, and an "institution-grade" server with no release.

14. 🆕 `p387` **A manifest's package name is not proof of a publication — match the registry back to
    the slug.** [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server)
    declares the npm name **`class`**, and npm's `class` is an unrelated **2013** package by
    `deadlyicon`. Keyed on the name alone, a recency sweep would have printed *"MIT, published
    2013-08-15"* onto a Google Classroom row. 🟢 **The check:** accept a registry row only when its
    `repository` field — or the links in its description — point back at the same slug; otherwise
    record `NOT PUBLISHED` and say so. The same check collapses fork families for free: four
    Blackboard addresses declare `blackboard-mcp` and **one** publication exists, its `repository`
    naming `felipedias-ie`; `mdweaver/canvas-mcp` carries upstream's scoped name
    `@r-huijts/canvas-mcp`. **Count the artefact, not the slug.**

11. 🆕 `p388` **If the repository is unreadable, read the *artefact*. The manifest is a claim; the
    tarball is the evidence.** `git ls-remote` distinguishes two states a 404 conflates: a
    **credentials prompt means the repository exists and is closed**, not absent. For such a package
    — and **6 of 32 addresses probed in `p388` are in this state while publishing to npm
    normally** — the published tarball is still readable and is **the licence that actually ships**:
    ```
    curl -s https://registry.npmjs.org/<pkg> | jq -r '.versions[.["dist-tags"].latest].dist.tarball'
    curl -s <tarball> | tar -tz | grep -i -E 'license|copying'      # is a grant shipped at all?
    ```
    🔴 **This is how `p388` established that a major publisher's tutoring SDK is ungranted.**
    `@santillana-ai/typescript-tutor-sdk` — **115 published versions** — has **no `license` field in
    `package.json`**, **no licence file anywhere in its 896,006-byte tarball**, and **no `repository`
    field at all**; its sibling scaffolder claims `"license": "MIT"` in the manifest while shipping
    **no licence file either**. Neither the repo (private) nor the badge (absent) could have settled
    it; the artefact did.
    🔵 **Three sub-rules:**
    **(a)** A manifest reading **`"SEE LICENSE IN LICENSE"` that points into an unreadable
    repository is not a grant** — it is a circular reference
    — [ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit) is the worked example, and 🆕 `p390` re-confirmed its repository is **still unreadable**, so the circle is still closed.
    **(b)** Steps 1–10 clear a repository **by subtree**; when there is no readable subtree, *this*
    step is the only one available, and it can only ever yield 🟡 manifest-only or 🔴 ungranted —
    **never a clean clearance**.
    **(c)** 🔴 Check **which** package in a scope carries the grant. Here the MIT claim sits on the
    *scaffolder* and the **dependency a client's code would actually import carries nothing**. Read
    the licence of the package you will `import`, not of the one you will `npx` once.

**Channel note, so this is reproducible:** `curl -sI https://github.com/...` returns **403** through
this sandbox's agent proxy and `api.github.com` returns **403**. `git ls-remote --symref` and
`raw.githubusercontent.com` both work, and together they are a stronger check than a HEAD request —
one proves the address and its real ref, the other reads the grant itself.

🟢 🆕 `p389` **Step 11, and it makes steps 1–10 one command.** A **blobless shallow clone** does the
whole gate in ~1.2 s, from the payload, with no API and no credentials:

```bash
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/&lt;owner&gt;/&lt;repo&gt; r
git -C r symbolic-ref --short HEAD    # the real default ref (step 1)
git -C r ls-tree --name-only HEAD     # is there a LICENSE at all, and where (steps 2-3)
git -C r show HEAD:LICENSE            # the grant text itself (step 4)
git -C r show HEAD:package.json       # the manifest that must agree with it (step 5)
git -C r log -1 --format='%H %cI'     # ← NEW: who still works on this, and when
```

🔵 **Why the last line belongs in a procurement gate and not just in a research note.** The gate has
only ever answered *may we use this*. It now also answers *will we be alone on it* — and the two
produce different estimates. **A permissive grant plus an eight-month-old HEAD is a vendoring
decision with a maintenance line**, which is precisely the call this base made for `pybryt` after
reading a *registry* date; the clone reads it for any repository, published package or not. 🟡 Read
the date against the artefact: a release branch can trail a default ref
([instructure/canvas-lms](https://github.com/instructure/canvas-lms), `master` **175 days** behind its
moving `stable/*` branches), and a finished specification is not decaying. 🔴 And the limit, **re-measured at `p392` and narrower than it was**: the `git` channel itself gives no
stars, forks or releases — but `github.com/{owner}/{repo}` answers **200 via WebFetch** (403 via
curl), so **stars, forks, commit counts and release tags are readable again**, and `api.github.com`
answers **200** while refusing **by scope** rather than outright (`/search/*` is closed by design).
**Discovery** remains web search and package registries; **verification** is first-hand; and
**popularity** is back, per tool. See [`channel-state`](../evidence/channel-state.2026-10-22-p392.tsv).

## Pattern Y — 🆕 `p392` Exam integrity the client can defend, without becoming a high-risk deployer

**For:** a client — a university, a certification body, a bootcamp — who asks for proctoring, and
whose actual requirement is *"we must be able to defend a result if it is challenged"*.

🔴 **Read this first, because it is the whole pattern.** For four passes these shelves said proctoring
had *"no credible permissive open-source option"*. That was wrong (`Gap 391-C`, closed this pass). But
the granted supply covers **deterministic lockdown and event telemetry**, while the **inference**
layer — identity matching, gaze, multi-face, behavioural scoring — is absent, roadmapped, or the
proprietary service an AGPL workflow brokers (`Trend 20`). 🟢 **That asymmetry is a gift, not a
shortfall:** the half you can build permissively is the half that is explainable in an appeal, and the
half you cannot is the half that makes the client a **deployer of an Annex III high-risk system** with
standalone obligations from **2 Dec 2027**.

**Wiring:**
1. **Signals in the browser, permissively.**
   [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) (🟢 **MIT**, 1,069 B,
   manifest agrees, HEAD **2026-09-28**, npm v0.5.1): tab-switch, right-click, DevTools shortcuts,
   clipboard events, camera state, **faces**, audio loudness, and **virtual-camera / loopback /
   screen-share detection**. Face detection is `@vladmandic/face-api` 1.7.15 on TF.js, **in the
   browser**. 🔴 **Two things to change before a pilot:** self-host the model weights (it loads
   face-api **and** its weights from jsDelivr by default — a supply-chain and data-residency defect in
   any EU or public-sector deployment, and the README documents the self-hosted path), and read all
   46 commits — this is **1 ★ and one maintainer**, so vendor it and own it.
   🟡 *Alternative when you need lockdown rather than detection:*
   [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) — 398 commits,
   HEAD **2026-10-13** — blocks copy/paste/cut, right-click, selection and shortcuts and reports eight
   named violation types. 🔴 Its grant is a **CONFLICT** (Apache-2.0 in the payload, `ISC` in
   `package.json` and on npm): both readings are permissive, so it is usable, but get the two files
   reconciled before a client depends on it. 🔴 And its AI features are marked *"(To be Done)"* — do
   not quote them.
2. **Keep the record, not the video.** Both components POST to an endpoint **you** build. Store the
   **event trail** (what happened, when, on which element) and resist storing webcam frames: snapshots
   are off by default in `proctoring.js`, and leaving them off is a defensible default, not a
   limitation. Audio is analysed in memory and discarded — say so in the privacy notice.
3. **Put the decision in a human's hands, in the workflow.** The attempt/review state machine already
   exists: [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) (🔴 **AGPL-3.0**,
   253 releases, `master` HEAD **2026-10-22** — re-read first-hand this pass) if the client runs Open edX — brokered over the platform boundary, not forked — or
   [`intellectif/learning-kit`](https://github.com/intellectif/learning-kit)'s (🟢 **MIT**)
   **deferred grading** when you are building the assessment surface yourself. **No automatic
   flagging decides anything**; a flagged attempt opens a review task.
4. **Launch and report over LTI 1.3, in the agent's own language.**
   [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (🟢 MIT) for a
   Django service, [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 MIT) for a
   serverless one — so the integrity result lands in the gradebook of record as an **LTI AGS score**
   with a reviewable note attached, rather than in a side system nobody audits.
5. **Write the Art. 50 and Annex III position down before you build.** Students are told, in advance,
   which signals are collected and what a flag does; the review path and the appeal path are named; the
   retention period is set. 🟢 This is cheap here **because** step 1 does no inference — the honest
   disclosure is short.

**Effort:** 4–6 weeks for steps 1–4 on an existing assessment surface; step 5 is a day of writing and
the thing that gets the deployment approved.

🔴 **What this pattern refuses to build, and tell the client why:** automated cheating *verdicts*,
identity verification from a webcam, and gaze or emotion scoring. The permissive supply does not have
them, the obligations land on the client rather than on us, and a flag that cannot be explained in an
appeal is a liability dressed as a feature.

## Pattern Z — 🆕 `p392` Size and price a Brazilian education engagement before the first meeting

**For:** a LATAM pitch — a municipal or state network, a private group — where the honest answer to
*"how big is this?"* has until now been *"we will need to scope it."* `Pattern W` does this for a US
district; this is the Brazilian instrument, and it is the closure of `Gap 391-B` for one country.

**Wiring:**
1. **Install the access layer.** [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil)
   (🟡 **MIT — code only**, 1,072 B; PyPI **`mcp-brasil` v0.14.0**, 18 releases; HEAD **2026-08-18**):
   an MCP server over **70 Brazilian public sources**, 533 tools, **66 of them keyless**, with large
   datasets cached locally and queried through embedded **DuckDB**. No procurement, no API key, no
   vendor.
2. **Query the school census.** `censo_escolar` (INEP) is the per-school base: network, enrolment,
   infrastructure. Build the target list — how many schools, which bands, which municipalities — and
   put a **per-school number** in the proposal instead of a range. `enem` adds outcome context where
   the engagement is secondary-level.
3. **Match it to the platform the client already runs.**
   [`portabilis/i-educar`](https://github.com/portabilis/i-educar) (🔴 GPL-2.0-or-later, real default
   ref **`2.12`**) is the municipal SIS a Brazilian engagement actually meets;
   [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) (GPL-3.0) for Portuguese/Spanish
   course delivery. Integrate **over the boundary** — web services or LTI 1.3 — so the copyleft stays
   on their side of it (`Pattern A`).
4. **Put the agent in Portuguese, from the shelf.** Tier 4 of [`agents/top.md`](../agents/top.md)
   holds the LATAM-native, Portuguese-first granted agents; `Pattern O` is the full regional build.
5. 🔴 **State the three limits in the proposal, in writing.** The bundled INEP data is a **2023
   snapshot** — currency is the risk, not the licence; the project's own `SOURCES.md` asks you to
   **validate a sample to confirm anonymisation**; and `mcp-brasil` is **not an official government
   service**, so a ministry-facing document cites **INEP** as the source and this as the access path.
   🟢 Its LGPD handling is genuinely documented: education is graded *RISCO ALTO*, the 2022 withdrawal
   and 2024 anonymised resumption are recorded, and `COLUNAS_DISTINCT_PERMITIDAS` whitelists aggregate
   columns only — no `NU_INSCRICAO`, name or CPF.

**Effort:** 2–3 days to a priced, school-level proposal; the integration in step 3 is the engagement.

🔴 **And know what you are walking into.** `Trend 21`: five live 2026 LATAM tenders, **none asking for
open source** — they buy subscriptions and licences. This pattern makes the *total-cost* argument
possible; it does not make the procurement ask for it.

## Pattern AA — 🆕 `p393` The LATAM SME delivery stack, entirely permissive, with billing already in it

**When to reach for this.** A LATAM client — a training provider, a professional body, a private
school group, a corporate academy — needs to **deliver and sell courses in Spanish** and wants to own
closed extensions. Every incumbent regional base is copyleft: **Chamilo** GPL-3.0, **i-educar**
GPL-2.0-or-later, **Moodle** GPL-3.0, **frappe/lms** AGPL-3.0. Until `p393` this shelf had to answer
either *"take the GPL"* or *"build a platform."*

🟢 **The base, and it is new to these shelves:**
[`bmosoluciones/now-lms`](https://github.com/bmosoluciones/now-lms) — **Apache-2.0**, payload read
first-hand (10,915 B, `sha256`₁₆ `a9c4042d767d`, © 2021–2024 BMO Moreno Berroteran Ortiz Soluciones,
**S.A., Nicaragua**), `main` · `53dcb60`, HEAD **2026-08-31 — 52 d**, **676 files, 505 commits, 57
releases**, PyPI `now-lms` v2.0.4. Flask/Python; courses, delivery, certificates and **monetisation**
in the box.

### The stack

| layer | component | grant | why this one |
|---|---|---|---|
| **Platform** | [`bmosoluciones/now-lms`](https://github.com/bmosoluciones/now-lms) | 🟢 **Apache-2.0** | The only Spanish-language LMS on these shelves you can fork, extend and **ship closed**. Flask — a studio reads the whole thing in a day. |
| **Tutor / agent** | the LATAM-native agent tier on [`agents/top.md`](../agents/top.md) | 🟢 MIT | Three granted regional options; one ships as an Open edX plugin, so prefer the standalone ones here. |
| **Interop edge** | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) 🟢 MIT, + [`…/django-lti-dynamic-registration`](https://github.com/Harvard-University-iCommons/django-lti-dynamic-registration) 🟢 MIT | 🟢 MIT | 🔴 **Django, and `now-lms` is Flask** — see the honest caveat below. Needed only when the client must appear **inside someone else's LMS**. |
| **Autograding** (technical courses) | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) 🟢 BSD-3 (**161 ★**, 197 releases) + [`edulinq/autograder-py`](https://github.com/edulinq/autograder-py) 🟢 MIT | 🟢 permissive | Grading and submission halves respectively. Both Python, both beside the platform's own runtime. |
| **Assessment import** | [`vosslab/qti_package_maker`](https://github.com/vosslab/qti_package_maker) | 🟡 **LGPL-3.0** | Ingest existing question banks as QTI. 🟡 **Link it, do not fork it** — LGPL permits the first and not the second. |
| **Public-data sizing** | [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | 🟡 MIT (code only) | For a **Brazilian** engagement, size the market from INEP `censo_escolar` before the first meeting — `Pattern Z`. |

### Wiring it

1. **Fork `now-lms`, pin the Apache-2.0 payload into the delivery record.** Record bytes and
   `sha256`, per `Pattern L` step 1. The appendix is **filled in**, not narrowed — that is the benign
   non-stock case, and worth noting in the record so a later reviewer does not re-raise it.
2. **Keep the agent out of the platform process.** The tutor talks to `now-lms` over HTTP and holds
   its own store. 🔵 This is `Pattern A`'s rule and it survives here for a different reason: not
   copyleft containment, but so the platform fork stays rebaseable onto a 57-release upstream.
3. **Add autograding only for the courses that need it.** `otter-grader` runs containerised; invoke
   it as a job, not in the request path.
4. **Decide the interop edge explicitly, and this is where the caveat bites** (below).
5. **Bill through the platform's own monetisation**, which is the reason to pick this base over
   `academico`. Verify it against the client's local payment rails before promising it — Nicaraguan
   defaults are not Brazilian or Mexican ones.

### 🔴 The caveats, because this base's own history says to write them next to the recipe

- 🔴 **21 ★, and that is the real risk, not the licence.** One company, 505 commits, no multi-tenancy
  claim. **Fork it and plan to own it** — budget maintenance as if upstream may stop. Do not put a
  ministry on it; `Pattern O` and Chamilo remain the public-sector answer.
- 🔴 **The LTI edge is Django and `now-lms` is Flask.** All five Python LTI implementations
  (`p393`, refuting `Gap 391-A` a second time) are **Django** apps or JupyterHub authenticators. If
  the client must launch from a third-party LMS, the edge is a **separate Django service** beside the
  Flask app. 🔵 Note what this is and is not: `p391` published *"the interop edge must be a separate
  runtime"* as a **language** claim and was wrong; here it is a **framework** claim about one specific
  pairing, and it is a deployment line to cost, not an architecture verdict.
- 🟡 **Three of the four non-platform components are copyleft or weak-copyleft** once assessment import
  enters. Keep QTI conversion (`Citolab`, GPL-3.0) and packaging (LGPL-3.0) as **arm's-length tools**
  invoked by a pipeline; nothing copyleft links into the delivered fork.
- 🔴 **Do not reach for the `timeback-*` OneRoster/QTI clients**, however well they fit on paper:
  147 releases, MIT **declared**, and a **source repository that does not resolve** (`Gap 393-B`,
  `Trend 23`). You cannot warrant a grant you cannot read.

🟢 **What the client gets that they cannot buy:** a Spanish-language delivery platform they own
outright, with billing, autograding and an AI tutor — assembled from **four permissive grants read at
the payload**, on a base whose entire source a studio can audit in an afternoon.

## Pattern AB — 🆕 `p394` The statistics and data-science course, graded automatically, including where the network is not

**When to reach for this.** The client teaches **R** — statistics, biostatistics, econometrics,
data science, any quantitative methods course — and wants automated feedback at cohort scale.
🔵 `p393` flagged that this base's most-adopted *maintained* autograder **grades R** while the shelves held no R
components at all; this pattern is the hole closed. 🟢 **And its last step is the only offline
assessment loop in this entire base**, which is what makes it worth reaching for in LATAM and APAC
rather than only in a well-connected university.

**The components, and the licence boundary runs between steps 3 and 5.**

| # | step | component | grant |
|---|---|---|---|
| 1 | Serve identical compute to the cohort | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause |
| 2 | Author the tutorial the student works inside | [`rstudio/learnr`](https://github.com/rstudio/learnr) | 🟢 **Apache-2.0** *(10,472 B, `60a581bccd57`)* |
| 3 | Grade the exercise and answer back | [`rstudio/gradethis`](https://github.com/rstudio/gradethis) | 🟢 **MIT** *(1,078 B, `48c18e68ffed`)* |
| 4 | Batch-autograde submitted scripts and notebooks | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) + [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | 🟢 BSD-3-Clause both |
| 5 | **Generate the exam** in the LMS's own format | [`cran/exams`](https://github.com/cran/exams) | 🔴 **GPL-2 \| GPL-3 — service boundary** |
| 6 | Calibrate the items after the fact | [`philchalmers/mirt`](https://github.com/philchalmers/mirt) · [`cran/catR`](https://github.com/cran/catR) · [`ShinyItemAnalysis`](https://github.com/patriciamar/ShinyItemAnalysis) | 🔴 **GPL — service boundary** |
| 7 | Carry the generated exam into the LMS | QTI 2.1 / Moodle XML, per `p393`'s **Tier 8** standards layer | per that tier |

**Wiring it.**

1. **Steps 1–4 are your product and they are permissive.** `learnr` renders the tutorial, `gradethis`
   supplies the per-exercise predicate (`grade_this_code()` against a model solution for mechanical
   exercises; `grade_this()` where you must inspect the student's actual object), `ottr` handles
   batch submission. 🟢 A closed-source product may embed all four.
2. **Steps 5–6 run as a separate service, invoked over a process boundary.** 🔴 `cran/exams`, `mirt`,
   `catR` and `ShinyItemAnalysis` are **GPL**; call them as a job — stdin/stdout, a queue, an HTTP
   worker — and never link them into the product. 🔵 Same discipline `Pattern A` and `Pattern O` apply
   to Moodle and Open edX, applied here for the same reason.
3. **Record the disjunctive choice once, in writing.** `cran/exams` is **GPL-2 *or* GPL-3 at the
   licensee's election**. Pick a rung, write down which and why, and keep it with the engagement's
   licence register — downstream compatibility differs between the two, and "GPL" alone is not an
   answer a client's counsel will accept.
4. **Step 5's output is the integration point, and it is wide.** `exams2qti21()`, `exams2moodle()`,
   `exams2canvas()`, `exams2blackboard()`, `exams2ilias()`, `exams2openolat()` — verified from the
   `R/` source filenames in the clone. 🟢 So one authored item bank feeds **whichever** LMS the client
   already runs, which is the opposite of the usual per-platform rewrite.
5. 🟢 **Then NOPS, which is the step nothing else here can do.** `cran/exams` emits a standardised PDF
   that is **printed, sat on paper, scanned, and marked automatically**. 🔵 Use it where the network
   is unreliable, where invigilation must be physical, or where the institution needs a **paper audit
   trail** it can produce years later. 🔴 It is also the honest answer to the finding on
   [`intel/market.md`](../intel/market.md) that **assessment is the lowest-adoption AI use case among
   LATAM faculty**: if the reluctance is about connectivity, invigilation and auditability rather than
   about AI, NOPS addresses the actual objection instead of arguing with it.

🔴 **Two things this pattern does not claim.** **(1)** `ottr` has **3 ★** — the adoption sits on the
Python parent, so you are deploying a lightly-used component and should budget to read its source.
**(2)** `learnr`'s HEAD is **343 days** old. That reads as stable rather than abandoned — the movement
is in `gradethis` (**126 d**) — but it is a dependency whose maintenance a studio should check before
year three, not a vendor commitment.

🔴 **And a provenance warning that will bite at review.** `cran/exams`, `mirt`, `catR`, `TAM` and
`ShinyItemAnalysis` carry **no licence file at any path** — their grant is the `License:` field in
`DESCRIPTION`, which is what CRAN enforces. 🔵 **GitHub's sidebar therefore shows no licence for any of
them**, so a reviewer checking the UI will report five granted GPL packages as unlicensed. Put the
`DESCRIPTION` line in the licence register, not a screenshot of the repository page (`Gap 394-B`).

## Pattern AC — 🆕 `p394` Give teachers an assistant builder instead of building their assistants (EMEA, Moodle)

**When to reach for this.** The client is a **university or school group already running Moodle**,
their teachers keep asking for subject-specific AI assistants, and a studio cannot profitably build
one assistant per course. 🟢 **LAMB inverts the unit of delivery**: the studio delivers the *builder*
and governs it; teachers author the assistants themselves, with no code.

**The components.**

| # | step | component | grant |
|---|---|---|---|
| 1 | The assistant builder and manager | [`Lamb-Project/lamb`](https://github.com/Lamb-Project/lamb) | 🔴 **GPL-3.0** *(35,349 B, `17fe6d0ffa96`)* |
| 2 | Publish each assistant into the LMS | **LTI external tool** — LAMB's own publishing path | 1EdTech LTI |
| 3 | Graded assignments against an assistant | [`Lamb-Project/lamba`](https://github.com/Lamb-Project/lamba) | 🔴 **GPL** |
| 4 | The LMS itself | Moodle | 🔴 GPL-3 |
| 5 | Models, where sovereignty is required | open-weights served locally — LAMB states it shares no user information with model providers and can run on *"open source and open weights models running on your compute"* | per model |

**Wiring it.**

1. **The whole stack is copyleft and that is fine here**, because nothing in it is a product a studio
   resells. 🟢 Moodle is GPL-3, LAMB is GPL-3, LAMBA is GPL — the engagement is **deployment,
   integration, governance and training**, not licensing. 🔵 This is the one shape where the copyleft
   frontier on [`repos/foundations.md`](../repos/foundations.md) costs nothing.
2. **Step 2 is why this is a pattern and not a tool.** Assistants arrive in Moodle as **LTI external
   tools**, so the LMS stays untouched: no plugin to maintain against Moodle's upgrade cycle, no
   fork, and the assistant can be withdrawn without a migration. 🟢 Same architecture `Pattern A`
   prescribes for every agent going into a copyleft LMS, except here the upstream project already
   did it.
3. **Read the tree before you read the badge.** 🔴 LAMB carries **three grants**: root GPL-3,
   `lamb-kb-server-stable/` with its own stock GPL payload, and a **vendored `open-webui/` under
   verbatim BSD-3-Clause** (1,510 B, `6c4b8d8034b9`). `Pattern L` is the procedure; this repository is
   why `Pattern L` exists. 🔵 Check the vendored Open WebUI copy's licence **at the pin you deploy** —
   upstream Open WebUI added branding restrictions in later releases, and the copy vendored here is
   the plain BSD-3 one.
4. **Sovereignty is a configuration, not a port.** Step 5 is the reason to shortlist LAMB for an
   EMEA engagement at all: it is designed to run against locally-served open-weights models and
   states that no user information reaches a model provider. 🟢 That answers the EU AI Act data
   questions in the architecture rather than in a DPA annex.
5. 🔴 **Size it as a high-risk deployment the moment it touches grading.** `lamba` grades assignments.
   Under the EU AI Act, systems that **grade learners, assign them to programmes or influence access
   to qualifications** are **high-risk and need a conformity assessment before deployment** (see
   *EMEA* on [`intel/market.md`](../intel/market.md)). 🟢 So: ship step 2 (assistants that tutor and
   explain) first and get it in front of teachers; treat step 3 (assistants that grade) as a
   **separate, later, assessed workstream**. Selling them as one phase is how an integration project
   becomes a compliance project mid-delivery.

🔴 **The maturity caveat, stated here and not only in the evidence file.** LAMB's own Moodle.org thread
(Feb 2026) describes it as *"at a very beta stage"* with *"a few universities running pilots"*, and the
repository is **one squashed commit** with HEAD **2 d**. 🟢 It is university-authored, peer-reviewed in
*Computer Standards & Interfaces*, and visibly active — **a strong pilot base**. 🔴 It is **not** a
ministry-scale platform, there is no multi-tenancy claim this base has verified, and an engagement
that needs one should read `Pattern O`'s tenancy discussion first. 🔵 Propose it as a pilot with a
named exit, and say so to the client in the first meeting rather than the third.

