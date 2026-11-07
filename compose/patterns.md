---
industry: education
region: Global
updated: 2026-11-07
---

# 🧩 Composition patterns — Education

> Concrete recipes. Every component named below was verified on 2026-11-04, and the nine components cited by 🆕 **P38** were re-verified on 2026-11-05 at p669 (`git ls-remote --symref`, real default ref on all nine) (existence + licence payload + stars where shown) and appears in `agents/top.md`, `repos/foundations.md` or `verticals/solutions.md`.
> 🔄 **Re-counted from the `## P` headings at p685: `61` patterns, `P1`–`P61`, `0` duplicated numbers and `0` gaps — measured, and the previous figure was stale by five.** 🔄 **Re-derived at p687: `63` patterns, `P1`–`P63`, `0` duplicated numbers and `0` gaps.** `62` carried in (p686 filed `P62`), `P63` added this pass. 🔵 Numbered from `max(## P)`, not from the last heading in file order — the rule this header exists to enforce. It read `56` (`p681`'s correct count); `P57`–`P60` were filed beneath it without it being re-counted, and `p685` adds **P61**. 🔵 **Unlike the row counts on the three shelf files, this one is derived from headings, which are unique — so it is a stale *figure*, not an ambiguous *identifier*.** Contrast `intel/trends.md`, where four `T` numbers each denote two different trends and `156` references point at them (see the banner at the top of that file). The heading this replaces said `50`, which was already `4` stale when p680 opened — and the re-count caught a live defect in the process: **p680's own new pattern was first written as `P53`, a number p679 had already used**, because `P54` existed and the highest number is not the last heading in file order. 🔵 **Never number a new pattern from the bottom of the file; number it from `max(## P)`.**
> 
> **The licence rule that governs all `55` patterns below — 🔄 previously re-counted from the `## P` headings at p677 (`48` at p676, plus **P49** and **P50**); 🔧 **p677 also publishes a second number these pages had never separated — `distinct` versus `total`.** The shelf files carry `59`/`58`, `128`/`128` and `61`/`58` rows-to-distinct-subjects respectively, so a count re-derived from rows is not an inventory count; see [`intel/trends.md`](../intel/trends.md) **T62**. The pattern count below is derived from headings, which are unique, so it is unaffected — 🔄 re-counted from the `## P` headings at p676 (`46` at p675, plus **P47** and **P48**; `ingest/derive-counts.py` independently derives `P-1..P-48`) — 🔄 re-counted at p675 (`40` at p671, `45` at p674, plus **P46**); the header had drifted to `40` while five patterns were added beneath it, which is the same stale-denominator defect p671 fixed:** keep proprietary work in the agent layer (MIT/Apache) and in Apache-2.0 XBlocks. Never fork a GPL/AGPL platform for a managed service.

## Base architecture

```
[LMS / SIS — stock, unmodified: Moodle GPL-3.0 | Open edX AGPL-3.0 | Canvas SaaS]
        │  REST / MCP  (process boundary = licence boundary)
        ▼
[MCP server layer — MIT]
   canvas-mcp (317★)  ·  Moodle REST adapter  ·  SIS adapter
        ▼
[Orchestration — LangGraph (MIT)]
        ▼
[Agents — MIT / Apache-2.0]
   DeepTutor (Apache-2.0, 55k★)   — 1:1 lifelong tutoring
   OpenMAIC  (MIT, 42.7k★)        — multi-agent classroom
   OATutor   (MIT, 276★)          — BKT mastery tutoring
   Instructional Agents (MIT, 490★) — course material generation
   Bloom     (MIT, 302★)          — adaptive lesson sequencing
   AI-Shifu  (Apache-2.0, 331★)   — course authoring from expert intent
   GenMentor (CC0-1.0, 136★)      — goal-oriented session planning
        ▼
[Mastery + retention — pyKT (MIT, 457★) / BKT  ·  fsrs-rs (BSD-3, 456★) scheduling]
        ▼
[Delivery — Kolibri (MIT, offline-first) · Richie portal (MIT) · WhatsApp · avatar (Open TutorAI CE, BSD-3) · LMS-native]
```

---

## P73 — The Iberoamerican school-administration spine, **procured rather than assembled** (public school network, state or municipal secretariat, school group: 5–7 weeks) 🆕 new at p693

🔧 **This pattern amends `P71`, and the amendment is the point.** `P71` opens *"there is no `es`/`pt` education agent to fork, so the deliverable is **assembly**"* — correct about **agents**, and p693 showed it was over-generalised to the whole layer. The probe `p691` ran asked for a **subject** (`educación`, `aprendizaje`, `escolar`); asked for a **product** instead (`gestão escolar`, `diário de classe`, `boletim escolar`, `avaliação docente`, `secretaria escolar`), the same index returned **`473` repositories and `13` real education systems, `9` novel to this base** (`T107`). 🟢 **So the administrative spine *is* procurable in Spanish and Portuguese. The tutoring and assessment surface still is not** — `P71` remains the right pattern for that half, and these two compose.

**The wiring — every part licence-verified at p693, payload read at the real default ref:**

| Layer | Part | Licence (byte-read) | Why this one |
|---|---|---|---|
| Attendance, incidents, guardian comms | **BuscApp** ([`eemtijca/buscapp`](https://github.com/eemtijca/buscapp)) | 🟢 MIT `1,088 B` `7a3744cad4f5` | 🟢 **The grant's copyright holder is a named Ceará state school** — this is school software written by a school, so the domain model is the real one (incident records, absence *justifications*, guardian messaging) rather than an SIS vendor's abstraction. Ships a **risk-prioritisation ranking** dashboard and an **LGPD** export/anonymisation decision record (`docs/adr/014`) — the data-protection answer is already in the repository. PWA, per-profile data isolation, CodeQL in CI. |
| Grades ↔ LMS ↔ institutional roster | **UFMG Sheet Generator** ([`h3ct0r/ufmg_notas_excel_sheet_webapp`](https://github.com/h3ct0r/ufmg_notas_excel_sheet_webapp)) | 🟢 MIT `1,073 B` `63d843ef7c0e` | The seam where LATAM public-institution delivery actually breaks: merges **class-diary CSVs** with **Moodle export CSVs** into one roster and emits a formatted Sheet over service-account or user OAuth, streaming progress on a WebSocket. FastAPI + Pandas. Nothing else on these shelves addresses this seam. |
| Teaching-quality loop (collection end) | **AvaliaDocente** ([`ajacs10/AvaliaDocente`](https://github.com/ajacs10/AvaliaDocente)) | 🟢 MIT `1,093 B` `dd945341baf6` | Anonymous, structured student evaluation of staff **and of methodologies**, scoped so a student sees only their own course-year subjects. |
| Teaching-quality loop (narrative end) | **dossier-comment-reflector** ([`pisan-labs/dossier-comment-reflector`](https://github.com/pisan-labs/dossier-comment-reflector)) | 🟢 MIT `1,068 B` `d6dc3e9441c3` (p692) | Turns the evaluation CSVs into twelve themes and a before/after comparison around a **stated teaching change**. 🟢 **Pairing these two closes the loop**: collection in Iberia/LATAM form, narrative in the North American tenure form (`693` North America). |
| Practice/placement management | **Mesa de Servicio** ([`DanielDev87/virtual-center-app`](https://github.com/DanielDev87/virtual-center-app)) | 🟢 Apache-2.0 `11,358 B` `93f0abad8891`, **verbatim §1–§9** | Structured on **ADDIE** explicitly, ships production runbooks, and carries a **DOI** (`10.5281/zenodo.18841367`) — a citable artefact, which is rare on this shelf. ⚠️ Re-read its scope first: it has renamed itself toward *service desk*. |
| Content substrate, Spanish-primary | **Open-Security-Labs** ([`ValentinTorassa/Open-Security-Labs`](https://github.com/ValentinTorassa/Open-Security-Labs)) | 🟢 Apache-2.0 `11,371 B` `d0b38e10547e`, **verbatim §1–§9** | Spanish-primary courseware whose labs **execute** rather than describe. This is the line item `P71` says a Spanish-language delivery otherwise has to translate. |
| Grounded content generation | **study.cybercirujas** ([`villadalmine/study-cybercirujas`](https://github.com/villadalmine/study-cybercirujas)) | 🟢 Apache-2.0 `10,765 B` `aa2da1f507e6`, **verbatim §1–§9** | Generation grounded in a **frozen source document** (the vendor's official syllabus), with deterministic checks, a published `GUARDRAILS.md` separating *blocks* from *warns*, and human merge. Runs **offline against a local model** — the same connectivity constraint `P71` builds Kolibri for. |

**Build sequence.**

1. **Week 1 — pick the spine and read its grant before anything else.** `buscapp` if the unit is a school or a municipal network (its domain model already matches); `virtual-center-app` if the unit is placements and practice centres. 🔴 **Run the `archived` flag on every address before forking** — `692-A` found eleven dead repositories on these shelves, two of them published as step 1 of a fork instruction, and `ls-remote` plus `pushed_at` **cannot** detect it (`692-B`).
2. **Weeks 1–3 — the data-protection work is a fork decision, not a later phase.** `buscapp` already carries an LGPD export/anonymisation ADR; **read it and keep it**, because re-deriving it costs more than the fork. For Spain or Portugal the same artefact is a **GDPR** record and the ADR is the draft. 🔵 For a Brazilian public buyer, hold [`ipti/br.tag`](https://github.com/ipti/br.tag) alongside as **census context** — it is live and **GPL-2.0**, so it informs the data model and must not be linked into a proprietary deliverable (`P32`'s boundary: separate process, API calls, no linking).
3. **Weeks 2–4 — wire the grade seam, read-mostly.** `ufmg_notas_excel_sheet_webapp` between the class diary and Moodle. **The agent proposes; a human posts.** Keep write scope off the record of attainment — which is also what keeps the deployment outside the high-risk category in every regime this base tracks (`P71` step 3's rule, and Vietnam's *"official basis for assessing learning outcomes"* qualifier).
4. **Weeks 4–6 — close the teaching-quality loop.** `AvaliaDocente` for collection, `dossier-comment-reflector` for the narrative. Pin the rubric version per decision.
5. **Weeks 6–7 — evidence pack.** Grant digests for every forked component (the table above is the starting state), the `archived`-flag audit from step 1, the LGPD/GDPR record from step 2, and the human-approval trail from step 3.

🟢 **Why this sells.** The region's demand case is `87%` of institutions using AI against `26%` with a strategy, `55%` with no AI budget and **`9%` measuring outcomes** (UNESCO IESALC). **The administrative spine is the part a `55%`-no-budget buyer can actually authorise**, because it replaces spreadsheet-and-WhatsApp operations with something auditable and the licence cost is zero. The tutoring layer — the expensive, `P71`-shaped half — follows once the spine is in production and the measurement gap (`terracotta`, `Gap 673`) has something to measure.

🟡 **What this pattern does not claim.** These parts have **no integration history together**, and four of the seven sit below `50★` — `h3ct0r/ufmg_notas_excel_sheet_webapp` at `1★` and `Debaq/LabSim` at `2★` are filed on what they *do*, not on adoption. 🔴 **Two placements in the table are orthographic inferences at MEDIUM confidence** (`AvaliaDocente`, and `Gestao-Escolar` if substituted as the spine), overturnable by one registry fact — see `T108`. 🔴 **And `Gestao-Escolar`'s author calls it *"em desenvolvimento"***: do not put it under a live student record without reading the migrations first.


## P71 — The Spanish/Portuguese tutoring surface, **assembled rather than forked** (LATAM ministry, state secretariat, university or edtech: 6–8 weeks) 🆕 new at p691

🔴 **The premise is a measured absence, not a market guess.** `p691` probed the Spanish/Portuguese permissive supply directly — seven single-term legs against `search/repositories`, `90` repositories, `19` novel and permissive, and **`0` education AI agents** (table at [`../intel/market.md`](../intel/market.md) under `LATAM`). There is no `es`/`pt` education agent to fork. 🔵 **And the shelf's `5` LATAM rows are a floor on that channel rather than the region's true supply, because GitHub free-text matches name, description and topics — not README.** So the deliverable is **assembly**, and every part below is already licence-verified on these shelves.

**The wiring, part by part — each one permissive, each one already on a shelf:**

| Layer | Part | Licence | Why this one |
|---|---|---|---|
| Delivery, offline-first | **Kolibri** `@develop:platforms/android` 🔴 *(address corrected p692 — `kolibri-installer-android` is archived)* | MIT (monorepo root payload re-read at p692, ref `develop`, `1,097 B`, sha256₁₂ `3c056b34a476`) | The binding constraint in LATAM public education is **connectivity, not model quality**. Kolibri runs the whole learning surface with no egress and syncs opportunistically — and the MIT grant means the Android delivery path is commercially redistributable. |
| Mastery engine | **OATutor** ([`CAHLR/OATutor`](https://github.com/CAHLR/OATutor)) | MIT | Bayesian Knowledge Tracing with a **frozen scoring rubric** and LTI into the institutional LMS. Peer-reviewed, UC Berkeley. This is the part that must not be an LLM: mastery estimates have to be reproducible to survive an audit. |
| Agent-facing contract | **tutor-mcp** ([`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp)) | MIT | Exposes BKT + FSRS + prerequisite skill graphs behind **one MCP tool** with a frozen rubric. The agent *calls* pedagogy rather than improvising it — which is what makes the tutoring layer swappable and the grading layer defensible. |
| Retention scheduling | **fsrs4anki** / `open-spaced-repetition` | MIT | A scheduler with published parameters, so the spacing decisions are explainable to a ministry rather than emergent from a prompt. |
| Institutional surface | **moodle-mcp** ([`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp)) **or** **canvas-mcp** ([`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)) | MIT / MIT | Moodle dominates LATAM public higher education; Canvas dominates the private and corporate estate. Both bridges are MIT, so the LMS choice does not change the licence position. |

**Build sequence.**

1. **Weeks 1–2 — stand up the spine, not the model.** Kolibri as the delivery shell; OATutor's BKT behind `tutor-mcp` so the mastery contract exists before any agent touches it. Freeze the rubric and check it into the repo: it is the artefact an auditor will ask for.
2. **Weeks 2–4 — localisation is the work, and it is content work.** The agents on these shelves are not language-limited; the **curriculum alignment** is. Map to the actual standard in play (Brazil's BNCC, Mexico's *Aprendizajes Clave*, Chile's *Bases Curriculares*) and carry the standard's own codes as first-class identifiers. 🔵 **This base already holds the cautionary case**: a Brazilian curriculum-code artefact whose benchmark scored *"refused a fake code"* separately from *"reproduced a real one"* and found faithfulness collapsing **`88% → 3%`** across models. **Validate against a private held-out set of real and fabricated codes; a model that invents a plausible BNCC code is worse than one that declines.**
3. **Weeks 4–6 — wire the LMS and keep the gradebook out of reach.** Connect `moodle-mcp` or `canvas-mcp` read-mostly. The agent proposes; a human posts. Keep the write scope off the record of attainment.
4. **Weeks 6–8 — evidence pack.** Mastery estimates reproducible from logs, rubric version pinned per decision, human-approval trail on anything that reached a learner's record.

🟢 **The regulatory read, and it is the reason step 3 is drawn that way.** LATAM has **no Annex III analogue** — `p691`'s demand leg re-confirmed `716` regulatory instruments across `23` countries with **`~45%`** of institutions holding or developing AI guidance against **`~70%`** in Europe and North America. **So the EU conformity pack is not required, and selling it as mandatory is misrepresentation.** 🔵 **But build to the line anyway, because the line is already drawn elsewhere and it is cheap to stay under it.** Vietnam's Decision `33/2026/QD-TTg` makes automated assessment high-risk **only** where the output is *"used as the official basis for assessing learning outcomes, evaluating competencies, or ranking learners"*. That qualifier is the most portable design rule in this document: **a formative tutor that never issues the record of attainment stays outside the high-risk category in every regime this base tracks** — EU Annex III, Vietnam, and whatever LATAM adopts next. Step 3 keeps the deployment on the safe side of it by construction, not by policy.

🟡 **What this pattern does not claim.** It is assembled from parts with no integration history together; the `6–8` weeks is build time for the spine, and the curriculum-code validation in step 2 is the step most likely to overrun, because it is the only one whose acceptance criterion depends on content this base has measured a model failing.


## P69 — Licence attestation over an education software estate (EMEA public sector, university consortia, edtech due diligence: 3–4 weeks) 🟢 new at p690

🔵 **Sell this when the client's own tooling has already failed.** `p690` measured the failure mode precisely: of `339` education repositories, **`44` return `NOASSERTION` or `NONE` from GitHub's own licence detector while carrying a real, readable grant** ([`T99`](../intel/trends.md)). A client's SCA gate reports those as **`unknown licence`**, and `unknown` cannot be risk-assessed — so the procurement review stops, and nobody can say whether the blocker is real. **This pattern converts `unknown` into a named family with payload evidence.** It is `3–4` weeks, needs no agent, and is the cheapest credible first engagement in the regions this base keeps calling underserved.

**Who buys it.** A European ministry, agency or university consortium standing up a platform on public-sector code; an acquirer doing diligence on an edtech target; any institution whose dependency tree reaches `Opetushallitus`, `OpenOLAT`, `INGInious`, `PrairieLearn`, `code-dot-org` or the `scrosseye` corpora.

**The stack — all of it already in this base, none of it bought.**

| Step | Tool | What it produces |
|---|---|---|
| 1. Enumerate the estate | `git ls-remote --symref <url> HEAD` per dependency | The **real default ref** — not `main` by assumption. `feedbacksystem` is `dev`, `code-dot-org` is `staging`, `kolibri-design-system` is `develop`, `ILIAS` is `release_11`. 🔴 **Resolve the branch before you clone** |
| 2. Ask the index first | `gh api search/repositories -f q='repo:o/n repo:o/n …'` (`15` per call) | `license.spdx_id`, `stargazers_count`, `pushed_at`, `archived`, `fork`. Cheap triage: everything that comes back with a real SPDX id needs no further work |
| 3. Read the payload for every divergence | `curl -sSL --fail` on `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`, **and `docs/`** at the ref from step 1 | Byte count + `sha256` + the first lines. 🔴 **`--fail` is not optional** — without it a `404` becomes a short document and the report becomes fiction (`T92`, `T100`) |
| 4. Classify against the five modes | [`T99`](../intel/trends.md) | EUPL-blind · MIT+provenance · Apache-appendix-filled · split grant · off-root/manifest-only |
| 5. Resolve the *tree*, not the repository | `package.json` / `composer.json` / `pom.xml` licence fields, vendored directories | `OpenMAIC` is MIT with an **LGPL-3.0-or-later** `packages/mathml2omml` inside it. 🔴 **The licence unit is the dependency graph** (`T16`) |
| 6. Attest | One row per dependency: family, version, grant path, bytes, `sha256`, evidence class, and the obligation in one sentence | The deliverable |

**The four findings to price into the statement of work, because they recur.**

1. 🔴 **EUPL is invisible and version-split.** `11` `Opetushallitus` repositories read as unlicensed; [`koski`](https://github.com/Opetushallitus/koski) is `LICENSE.txt` `653 B` **EUPL-1.1**-or-later and [`ataru`](https://github.com/Opetushallitus/ataru) is `LICENSE.md` `296 B` **EUPL-1.2**-or-later. **They are different instruments.** The EUPL's *Distribution or Communication* definition reaches making the Work available over a network, so **the boundary is not GPL's** — a hosted deployment can trigger reciprocity where a GPL analysis would say it does not.
2. 🔴 **Non-commercial limbs hide inside permissive repositories.** [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) is MIT **code** with `CC BY 4.0` prompts and **`CC BY-NC-SA 4.0` on both annotated corpora**; the upstream [`scrosseye/CLEAR-Corpus`](https://github.com/scrosseye/CLEAR-Corpus) and [`scrosseye/persuade_corpus_2.0`](https://github.com/scrosseye/persuade_corpus_2.0) both return `NONE`. **An `NC` corpus cannot ship in a commercial deliverable** — and it is reached through a repository whose headline licence is MIT.
3. 🔴 **Assets are carved out separately from code.** [`code-dot-org`](https://github.com/code-dot-org/code-dot-org) is Apache-2.0 *for source and assets* with artwork, graphics, sounds, lectures, videos, logos, characters and fonts **enumerated as proprietary** in a `4,271 B` `NOTICE`. A K-12 derivative that reuses the look is a different conversation from one that reuses the engine.
4. 🟡 **A manifest field is a declaration, not a grant.** [`kolibri-design-system`](https://github.com/learningequality/kolibri-design-system) declares `"license": "MIT"` in `package.json` with **no licence file on any branch**. Depend on it if the client accepts the risk — but write down that the warranty is thin.

🔴 **Two guards that make the report trustworthy, both of them lessons this pass learned the hard way.** (i) **Never grep a README for a licence family.** `p690`'s own probe read *"Apache 2"* out of [`openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic)'s README and nearly contradicted a correct `GPL-2.0` finding — the string was `Apache 2.4 or above`, the **web-server requirement**. (ii) **Never retire a dependency on a search miss.** `5` live repositories are absent from GitHub's search index (`T100`); liveness is `git ls-remote`'s answer, not the index's silence.

**Deliverable.** A signed attestation table over the estate, a one-page obligation summary per licence family, and a red list of the limbs that cannot enter a commercial derivative. 🟢 **Follow-on is natural:** the client now knows which parts of their stack they may close, which is the question `P11`, `P14` and `P21` all begin with.

## P70 — The Vietnam Article 34 deadline: the same auditable-tutoring deliverable, three months earlier than Europe's (APAC education operations: 8–10 weeks) 🟢 new at p690

🟢 **Why this pattern exists as its own entry.** This base has been selling the EU's **2 December 2027** Annex III date as the forcing function for auditable AI in education. `p690` confirmed a harder, earlier date in APAC: **Vietnam's Law on Artificial Intelligence No. 134/2025/QH15** (passed `2025-12-10`, `429`–`5`; in force **`2026-03-01`**; `8` chapters, `35` articles, three-tier risk regime) gives systems already running at commencement **18 months** where the sector is **education** (with healthcare and finance) under **Article 34** — 🔴 **a compliance date of `1 September 2027`.** The statute's education limb is explicit: AI must suit learners' age and development, **prevent risks in the assessment and classification of learners**, and protect data and privacy.

🔴 **What is confirmed and what is not, because the pitch must not outrun the evidence.** 🟢 Confirmed on two further independent channels this pass: the law's identity, its passage date, its commencement, and the `18`-month education transition. 🟢 The earlier channel conflict is resolved by **separation** — the *Digital Technology Industry Law* is a different instrument. 🔴 **Still not primary-verified:** the high-risk list itself, **Decision 33/2026/QD-TTg** (reported `46` systems across `6` sectors, with **contradictory effective dates** of `15 August 2026` and `1 January 2026`), and implementing **Decree 142/2026/ND-CP** (reported effective `1 May 2026`). 🔵 **Quote the statute and the Article 34 date. Do not quote the Decision's list or dates to a client without reading the Gazette text first** — and price that reading as the first task of the engagement.

**The build is `P67`'s, with the date and the evidence schema changed.** Reuse it rather than re-scoping:

| Layer | Component | Why |
|---|---|---|
| Tutoring surface | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) (MIT, `42,883★`) or [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | APAC-origin, permissive, and `OpenMAIC` is the largest multi-agent classroom in open source. 🔴 **Resolve its tree:** `packages/mathml2omml` is **LGPL-3.0-or-later** |
| The prohibition, in the tool surface | `P64`'s pattern — the agent **cannot** post a grade or a classification on its own | Article 34's education limb is about *assessment and classification of learners*. 🟢 **`T95`: human-in-the-loop is becoming a property of the tool surface, not a sentence in the policy** — and a statute that names classification is why |
| Evidence spine | `LTI` in, `xAPI` out — [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs), [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator), [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | `P17`'s spine unchanged. Every inference, its inputs, the human decision that followed, timestamped and queryable |
| Rubric scoring | [`microsoft/LLM-Rubric`](https://github.com/microsoft/LLM-Rubric), [`jacobphillips99/protorubric`](https://github.com/jacobphillips99/protorubric) | 🔴 **Not [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) for a commercial deliverable** — its two annotated corpora are `CC BY-NC-SA 4.0` (`P69`, finding 2) |
| Sovereignty | Self-hosted weights per `P9` | Vietnam's regime is extraterritorial in the same direction as Korea's; keep inference inside the client's jurisdiction and the data-protection limb answers itself |

🔵 **The commercial line.** A multinational with APAC education operations hits **Vietnam before Europe** — `1 September 2027` against `2 December 2027` — and `P67`'s deliverable satisfies both, because an auditable decision trail and a tool surface that cannot act alone are what *both* statutes require. 🟢 **Sell one build against two deadlines, and lead with the earlier one.** Alongside it, **Australia's TEQSA** requirement that every higher-education provider file an institutional action plan on generative-AI risk remains the only education-*specific* regulator obligation this base has found in any region — a smaller, faster engagement with the same evidence spine underneath.

## P66 — The Brazilian public-education intelligence desk (state or municipal secretariat: 5–7 weeks) 🟢 new at p689

**Buyer:** a Brazilian **secretaria de educação** — state or municipal — or a consultancy bidding one. **The premise is that this engagement does not open with a tutor.** It opens with *how many schools do we have, in what condition, how many enrolled, what does the IDEB say, what did FNDE transfer, how did this cohort score on the ENEM* — and every one of those is a question about federal statistics that is answerable in week one under MIT.

```
Mcp-Brasil/mcp-brasil  (MIT, 1,071 B · faa268455c36, 1,857★, 287 forks, main @ 2efb258370b1)
  ├── LIVE APIs — no dataset load, answers on day one
  │     ├── inep   → índices educacionais: IDEB, indicadores, pesquisas        (4 tools)
  │     └── fnde   → repasses, merenda escolar, PNATE, transporte escolar      (4 tools)
  └── LOCAL DuckDB datasets — opt in via  MCP_BRASIL_DATASETS=inep_censo_escolar,inep_enem
        ├── inep_censo_escolar → ~180k schools: infrastructure, enrolments, 2023   (7 tools)
        └── inep_enem          → ~3.9M registrants: scores + socioeconomic profile (6 tools)
                                 first load = minutes (download + ingest); then milliseconds
  │
  └── ANALYSE  ZhijieXiong/pyedmine (MIT, 1,084 B · 05d651fe74ff, 84★)
        cognitive diagnosis + learning-path recommendation over the ENEM response data
        ⚠️ ENEM microdata is a POPULATION sample, not this client's learners — use it
           for cold start and for benchmarking the client's cohort against the state
  │
  └── SYSTEM OF RECORD (only if the client runs, or will run, the i-educar family)
        portabilis/i-educar  (GPL-2.0, default ref 2.12)   ← student records, already on the verticals shelf
        portabilis/i-diario  (AGPL-3.0, default ref 1.6)   ← diário de classe: attendance, lessons, grades
        🔴 copyleft: configure-and-host, never white-label.  Resolve BOTH bare-version default refs
           with  git ls-remote --symref  before cloning — a hardcoded `main` fails silently.
  │
  └── DELIVER  a read-only MCP surface + three briefings the secretariat cannot currently produce:
        school-infrastructure gap map · enrolment-vs-transfer reconciliation · ENEM cohort benchmark
```

**Weeks 1–2** stand up `mcp-brasil` with `inep` and `fnde` live only; produce the first briefing from live APIs alone — **this is the credibility milestone and it needs no data engineering**. **Weeks 3–4** enable the two DuckDB datasets, reconcile school counts against the client's own rolls (expect them to disagree; the disagreement is usually the most valuable finding of the engagement). **Weeks 5–6** cognitive diagnosis over ENEM with `pyedmine`, benchmarked against the client's cohort. **Week 7** if and only if the client runs i-educar: scope the `i-diario` integration as a separate statement of work.

🟢 **Why this is the strongest LATAM pattern on this page.** Every component is real, verified at p689, and `mcp-brasil` is MIT at `1,857★` with `287` forks — this is not a research prototype. The data layer is *public*, so there is no procurement gate on the inputs and no student-privacy exposure in the first four weeks: ENEM and Censo Escolar microdata are published aggregates and the client's own LGPD-governed records are not touched until the i-educar step, which is optional.

🔴 **Three risks to price explicitly.** (1) **The datasets are 2023** — current enough for structural analysis, wrong for anything presented as this year's position; say so in the deck. (2) **First DuckDB load is minutes and the download is large** (the repository's dataset tier spans ~100 MB–1.6 GB across all features) — run it before the demo, not during. (3) **`i-diario` and `i-educar` are copyleft with bare-version default refs**; the clone trap is documented at `p646-J` and this pattern repeats it because it keeps happening.

## P67 — Auditable agent tutoring for an EU Annex III deployer (university, exam board, EMEA K-12 authority: 8–10 weeks) 🟢 new at p689

**Buyer:** an institution inside the EU that wants agent tutoring touching assessment or personalised learning, and therefore becomes a **deployer of a high-risk system** under AI Act Annex III. **The premise: the hard requirement is not quality, it is explainability plus a record — and an LLM alone can supply neither.**

```
CORRECTNESS LAYER  ★ the load-bearing component, and the reason this pattern exists ★
  ideas-edu/ideas  (Apache-2.0, LICENSE.txt 11,558 B · 49bbe9114e49, 28★, master @ de4d9742c350)
    domain reasoners that COMPUTE the next correct step and the feedback for a wrong one
    shipped domains: mathematics · linear algebra · logic · Haskell (Ask-Elle) · communication skills
    → the LLM is demoted to language and dialogue.  It never certifies a step.
        │
DIALOGUE LAYER
  any shelved tutor runtime (HKUDS/DeepTutor, CAHLR/OATutor for BKT-structured STEM)
    constrained to phrase what the reasoner computed — not to derive it
        │
EVIDENCE LAYER   ← non-negotiable, and the piece almost every pilot omits
  DavidLMS/learnmcp-xapi (MIT, 1,068 B · 7795c106bbd2, 16★)   ← agent writes/reads xAPI statements
    └── yetanalytics/lrsql (Apache-2.0)                       ← the Learning Record Store itself
        🔵 p656 recorded lrsql as the ONLY permissive LRS; learnmcp-xapi is its agent-side counterpart
        🔴 learnmcp-xapi last pushed 2025-08-29 — fork and own it, do not depend on it
        │
WRITE BOUNDARY  ← borrow the p688 shape rather than inventing one
  kaushikgunasekaren/canvas-grader-mcp (MIT)  demonstrates the contract: 12 read-only tools,
    4 local-only, exactly 3 that write, EACH requiring confirm=true, grades staged on disk until then
  → specify every agent write to the LMS/SIS the same way: staged, explicit, second human act
        │
LMS SURFACE  — pick by what the institution actually runs
  smlfg/ilias-mcp (MIT, 1,078 B · 83d1c38c2069)  ILIAS + Moodle  ← the only ILIAS address in this KB
  peancor/moodle-mcp-server (MIT) · vishalsachdev/canvas-mcp (MIT)   ← both already shelved
        │
DESIGN REVIEW ARTEFACT
  vishalsachdev/learning-design-pillars (MIT, 1,070 B · 57c0458f2b22)
    the Four Pillars framework as loadable skills — an inspectable design rationale to put in front
    of an ethics or academic-standards committee, which a model prompt is not
```

**Weeks 1–2** scope to the domains `ideas` actually covers and *refuse the rest* — this is the decision the pattern lives or dies on. **Weeks 3–5** reasoner behind an MCP surface; LLM wired to phrase, never to derive; every turn emitting an xAPI statement from the first commit. **Weeks 6–7** write boundary with `confirm=true` on every mutating tool, staged locally, plus the deployer documentation pack. **Weeks 8–10** pilot on one cohort with the LRS as the single source of truth for what happened.

🟢 **What the client can state afterwards, which is the actual deliverable:** *what was said, why it was said (traceable to a computed rule, not a sampled token), and that a record exists in a store we own.* 🔵 The AI-literacy duty has applied since 2 February 2025 and the Digital Omnibus softened it from 27 July 2026 to *measures that support* literacy — so documentation and training are compliance artefacts here, not overhead, and `learning-design-pillars` is billable as one.

🔴 **Four risks.** (1) **`ideas` coverage is per-domain** — outside the shipped reasoners this is new work, and it is research-grade work. (2) **`28★`, Haskell**: budget a Haskell-capable engineer or an FFI boundary. (3) **`learnmcp-xapi` is fourteen months dormant** — fork at the pinned SHA. (4) 🔴 **The high-risk commencement date for education is genuinely unsettled** — *August 2026* against Regulation (EU) 2026/1744's *2 December 2027* — and this base **cannot verify it from this session** because `eur-lex.europa.eu` and `europarl.europa.eu` do not resolve under this network policy. **Make the client's counsel own that date. Do not put it in a slide as settled.**

## P68 — Competency and credential spine with rostering that actually works (corporate academy, professional body, multi-campus HE: 6–8 weeks) 🟢 new at p689

**Buyer:** an organisation that must answer *which people hold which verified competencies* across more than one delivery system — a corporate academy, a professional certifying body, a multi-campus university. **The premise: this base's interop coverage was xAPI (activity), LTI (launch) and SCORM (packaging), and none of those answers *who is in this class* or *what competency does this credential assert*.** Both gaps closed at p689.

```
ROSTERING  ← the layer that was missing
  theopenem/oneroster.net (MIT, 1,065 B · 5e308a037c69, master @ 4f96365d3108)
    OneRoster / 1EdTech: orgs · courses · classes · enrolments · users
    the format a US district or a multi-campus registry actually hands a vendor
    🔴 index-unaddressable: `repo:` returns HTTP 422, so verify with git ls-remote --symref
       (dots in the name are NOT the cause — control `repo:socketio/socket.io` returns 1)
        │
COMPETENCY + CREDENTIAL
  iblai/lms (MIT, 1,062 B · d9d62c94b512, 112★, pushed 2026-11-06)
    course discovery · competency tracking · digital credentials · workforce development
    TypeScript/Next.js — the clearest permissive competency model on these shelves
        │
DELIVERY  — pick ONE, they are not interchangeable
  pacewisdomhq/TutorLoom (Apache-2.0, 11,361 B · a7f87303f2e9, 89★)
    ★ MULTI-TENANT FROM THE FIRST COMMIT — tenant isolation is the expensive thing to
      retrofit into Moodle or Open edX, and this is the only shelved LMS that ships it
    Python 3.13 / Django 6 / DRF 3.16 / PostgreSQL 15+ / React 19 / Flutter mobile
    🔴 born 2026-10-07 — one month old.  89★ / 18 forks is real traction and real immaturity.
       Fork at a pinned SHA; do not track its main.
  — or Moodle / Open edX if the client already runs one (both copyleft; see P2 / P3)
        │
EVIDENCE   yetanalytics/lrsql (Apache-2.0) over xAPI   ← already shelved, still non-negotiable
        │
PRACTICE SURFACE (technical curricula only)
  SJRiz/pytogether (MIT, 1,072 B · c8df073d1320, 262★)
    browser-based collaborative IDE: multi-cursor editing, shared drawing canvas, voice
    🔵 it makes the KEYSTROKES observable — the input a knowledge-tracing model wants
       and almost never gets, because graders only ever see the finished submission
        │
MODELLING   ZhijieXiong/pyedmine (MIT) + pykt-team/pykt-toolkit (MIT, already shelved)
    pyedmine adds cognitive diagnosis and path recommendation on top of pure knowledge tracing
```

**Weeks 1–2** model the competency framework with the client's subject-matter owners — *slowest step, not a technical one*. **Weeks 3–4** `oneroster.net` against the client's registry or HRIS; reconcile rosters before any content work. **Weeks 5–6** `iblai/lms` for competency and credential issuance, xAPI out to `lrsql`. **Weeks 7–8** delivery surface, and `pytogether` + `pyedmine` only if the curriculum is technical.

🟢 **Why it is sellable:** permissive end to end, so the deliverable can be closed and client-branded — no copyleft in the chain unless the client's own LMS brings it. 🔴 **Two honest warnings.** `TutorLoom` is one month old: the forking rate says the shape is right, the age says pin the SHA and own the fork. And `oneroster.net` has **no readable star count or push date** — GitHub's search index cannot name the slug (HTTP 422), so its existence, default ref and MIT grant were verified by `ls-remote` and payload read only. **Treat it as a correct-shaped reference implementation to read and adopt, not as a maintained dependency**, until someone can see its activity.

## P63 — Randomised, auto-graded assessment at university scale, with the AI layer built rather than licensed
*Added p687. Every component verified first-hand on 2026-11-07 (real default ref via `git ls-remote --symref`, grant payload read at that ref) and filed on this base's shelves the same pass.*

**The problem.** A university or a large training provider wants assessment that cannot be answered by copying: every learner gets a different instance of the same problem, graded automatically, with an AI layer that explains a wrong answer and proposes the next item. The obvious starting point is [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) — and **the one directory you would want is the one directory that is not open source.**

**The constraint that shapes everything.** PrairieLearn's `LICENSE` (`37,237 B`, sha256₁₂ `548cbfae567a`) is four licences in one file. The Community Edition is **AGPL-3.0**; University of Illinois and outside-contributor portions are **MIT**; all client-side JavaScript is **AGPL-3.0**; and `apps/prairielearn/src/ee/` plus **`apps/course-agent/`** are proprietary Enterprise Edition — both carrying the identical `2,538 B` / `cfd0235081fa` payload that gates production use on a paid contract with PrairieLearn, Inc. 🔴 **So: use the platform, do not read the agent, and build your own.**

**The recipe.**

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Assessment engine | [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) CE, ref `master` | 🔴 AGPL-3.0 (CE) | Question-as-code: a Python generator emits a randomised instance plus its computed answer. Run it **as a service**, never vendored |
| Untrusted code execution | [`judge0/judge0`](https://github.com/judge0/judge0), ref `master` | 🔴 GPL-3.0 | Sandboxed, resource-capped execution in `60+` languages behind an API. Service-side, so GPL-3.0 never reaches the deliverable |
| Exam integrity | [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server), ref `master` | 🟡 MPL-2.0 | File-level copyleft — add your proctoring hooks as **new files** under your own licence |
| Agent layer (**you build this**) | [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills) + [`read2017/learn-anything-with-AI`](https://github.com/read2017/learn-anything-with-AI) | 🟢 Apache-2.0 / MIT | The mastery-gate loop and the skill scaffolding, both permissive, replacing the gated `apps/course-agent/` |
| Mastery model | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) + [`condecon/adaptivetesting`](https://github.com/condecon/adaptivetesting) | 🟢 permissive (already shelved) | Bayesian knowledge tracing and adaptive item selection decide *which* randomised instance comes next |
| Live cohort layer | [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework) | 🟢 Apache-2.0 | Synchronous in-class rounds; reference implementation, not a maintained dependency (no push since 2026-03) |

**How it wires.** PrairieLearn CE is the system of record for items, instances and grades, reached only over its HTTP API. Code-answer questions delegate execution to Judge0 rather than running in the engine. Every graded event writes to pyBKT, which updates a per-learner mastery estimate; `adaptivetesting` reads that estimate to pick the next item's difficulty, and PrairieLearn generates a fresh randomised instance at that difficulty. Your agent — Apache-2.0 skills on your own runtime — sits beside the engine, reads the grade event plus the generator's known-correct answer, and produces the explanation. SEB Server fences the summative sessions.

**Licence boundary, stated once.** Three copyleft components (AGPL-3.0, GPL-3.0, MPL-2.0) all sit **behind service boundaries you operate**; everything you write and ship — the agent, the skills, the mastery orchestration, the client UI you author — stays yours. 🔴 **Two hard lines:** do not fork PrairieLearn CE into a managed multi-tenant product (AGPL-3.0 reaches network users), and do not copy from `apps/course-agent/` or `apps/prairielearn/src/ee/` at all, at any ref, for any purpose.

**Effort.** `10`–`14` weeks to a running pilot for one faculty: `3`–`4` weeks standing up CE + Judge0 and authoring the first `30` question generators (the real cost is generator authoring, not integration), `3` weeks on the mastery loop, `3`–`4` weeks on the agent layer, `1`–`2` weeks on integrity and rollout.

🔵 **Region note.** PrairieLearn is placed **North America** on its own grant payload (*"University of Illinois Board of Trustees"*), and the question-as-code model is the dominant convention in US engineering faculties — so this pattern lands with least friction on a North America engagement. In **EMEA** the AGPL-3.0 service boundary needs stating explicitly against procurement rules, and under the EU AI Act assessment-grading is **Annex III high-risk** with stand-alone obligations now applying from **2027-12-02** (Digital Omnibus `(EU) 2026/1744`) — time to build the audit trail in, not a reason to defer. In **APAC**, Australia's TEQSA already requires providers to file genAI action plans, for which the mastery-and-provenance trail this pattern produces is directly usable.

## P1 — Canvas agent pilot (fastest credible pilot: 3–4 weeks)
**Best fit:** North America HE, any Canvas client. **Licence exposure:** none — the LMS is the client's SaaS.

| Component | Repo | Licence |
|---|---|---|
| LMS bridge | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT |
| Tutor | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT |
| Orchestration | LangGraph | MIT |

**Wiring:**
1. Deploy `canvas-mcp` against the client's Canvas instance with a scoped API token — read-only on enrolments and assignments for the pilot. Its ~102–128 tools cover courses, assignments, submissions and grades.
2. Run Bloom as the learner-facing agent. It already works as a Claude Code skill, so the first demo needs no web build at all.
3. Point Bloom's context at `canvas-mcp` tools so lessons reference the student's *actual* upcoming assignments.
4. Instrument from day one (see P5) — Canvas pilots are judged on measured outcomes.

**Why it wins:** no platform migration, no licence question, and a working demo inside a week. This is the pattern to lead with when a client says "we already have an LMS".

---

## P2 — Moodle + out-of-tree tutor (LATAM public sector, EMEA K-12: 6–8 weeks)
**Best fit:** the Moodle installed base — dominant in LATAM and much of EMEA.
**Licence exposure:** none, if you respect the process boundary.

| Component | Repo | Licence |
|---|---|---|
| LMS | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 — **stock** |
| Tutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 |
| Local inference | Ollama | MIT |
| Portal (optional) | [openfun/richie](https://github.com/openfun/richie) | MIT |

**Wiring:**
1. Leave Moodle **unmodified**. Enable Moodle Web Services and mint a scoped service token.
2. Stand up DeepTutor as a separate service. Its persistent learner model is the whole point — give it durable storage, not an ephemeral container.
3. Build a thin REST adapter (yours, MIT) that pulls course structure, activity logs and grades from Moodle into DeepTutor's student model.
4. For EMEA/LATAM data residency, back DeepTutor with local models via Ollama so learner data never leaves the jurisdiction.
5. Surface the tutor through Moodle's AI placements, or through a Richie (MIT) portal when the client wants their own branded front end.

**The licence reasoning:** a separate process talking to Moodle over REST is not a derivative work of Moodle. A Moodle plugin containing your tutor logic *would* be, and would owe GPL-3.0 on distribution. Keep the boundary at the network call.

---

## P3 — Open edX + XBlock, licence-contained (corporate academies, national platforms: 8–10 weeks)
**Best fit:** MOOC-scale and corporate L&D. **This is the only licence-safe shape for Open edX.**

| Component | Repo | Licence |
|---|---|---|
| Platform | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | **AGPL-3.0** — **stock** |
| Component SDK | [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** ← your code lives here |
| Classroom agent | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT |
| Content generation | [DaRL-GenAI/instructional_agents](https://github.com/DaRL-GenAI/instructional_agents) | MIT |

**Wiring:**
1. Deploy Open edX **unmodified**. This is not a style preference: modifying an AGPL-3.0 platform and operating it as a service obliges you to offer modified source to its users.
2. Write an XBlock (Apache-2.0) as the in-course surface. The XBlock is a thin client — it renders and relays, holding no business logic.
3. Run OpenMAIC outside the platform as the lesson engine. Its LangGraph orchestration and AI-classmate simulation are what the XBlock embeds.
4. Use `instructional_agents` offline to generate the course scaffold (syllabus → LaTeX slides → assessments) before the cohort starts, cutting designer time on the critical path.
5. Keep all proprietary work in the XBlock and the external services. The AGPL obligation never attaches.

**Delivery note:** step 1 is the whole pattern. Teams that "just patch one thing" in the platform create a disclosure obligation that is extremely hard to unwind later.

---

## P4 — Mastery-based adaptive sequencing (STEM, K-12: 8–12 weeks)
**Best fit:** clients who want explainable mastery estimates, not free-form chat.

| Component | Repo | Licence |
|---|---|---|
| ITS + BKT | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT |
| KT models | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT |
| LMS link | LTI (OATutor native) / canvas-mcp | MIT |

**Wiring:**
1. Deploy OATutor and connect it to the LMS over **LTI** — native, standards-based, no custom bridge.
2. Author or port problem sets with scaffolded hints into OATutor's content format. **This is the real cost of the pattern** — budget content work, not just engineering.
3. Train pyKT models on the client's historical interaction data to initialise mastery priors, instead of starting every learner from a cold BKT prior.
4. Expose mastery estimates to teachers as a dashboard. Explainability is the selling point here; do not hide the model behind a chat box.

**Honest scoping:** pyKT is a 457-star research library and OATutor is 276 stars. Both are solid and peer-reviewed, neither is a turnkey product. Promise explainable mastery modelling as an *engineering build*, not a component drop-in.

---

## P5 — Governance and measurement wrapper (sell this first, especially in LATAM)
**Best fit:** every region; the strongest standalone offer in LATAM and EMEA.
**Why first:** >50% of teachers in Chile and Brazil use AI while <10% of institutions have guidelines. The client's missing piece is control, not capability.

**Not a single repo — a layer wrapped around P1–P4:**

1. **Policy enforcement at the MCP boundary.** Every tool call from an agent to an LMS passes through the MCP server. That is the natural place for allow/deny rules, PII redaction and per-jurisdiction policy nodes. Implement it there, once, rather than inside each agent.
2. **Per-region policy nodes in the LangGraph graph.** Regulation has diverged (EMEA horizontal and dated; US state patchwork; India labelling from 20 Feb 2026; LATAM pending). Branch on jurisdiction in the graph:
   - **EMEA:** no emotion recognition (banned since Feb 2025); Article 50 AI-disclosure on every learner-facing surface (live since 2 Aug 2026); admissions/assessment/placement flagged high-risk ahead of **2 Dec 2027**.
   - **India:** synthetic-content labelling on generated material (from 20 Feb 2026).
   - **North America:** teacher-in-the-loop on anything touching instruction (Idaho SB 1227 bars AI replacing teachers); district policy artefacts (Ohio, Maryland).
3. **Audit log of every agent action against student data** — this is the specific thing the Bridges 2026 survey says leaders are withholding access over. Shipping it unblocks the rest of the engagement.
4. **Measurement harness, attached before launch:** pre/post assessment, 30-day retention, teacher hours saved. The July 2026 scoping review of 474 studies found the field's evidence fragmented; a pilot that cannot demonstrate an effect will not renew.

**Deliverables:** institutional AI policy, the technical controls that enforce it, the audit trail, and the measurement report. Spanish and Portuguese for LATAM. Repeatable across peer institutions with little rework — which is what makes it a product rather than a project.

---

## P6 — Retention engine: mastery + scheduling behind one MCP surface (4–6 weeks)
**Best fit:** any client whose pilot has to show a measured outcome — which, per `intel/trends.md` **T10**, is now most of them.
**Licence exposure:** none. Every component is MIT or BSD-3-Clause.

| Component | Repo | Licence |
|---|---|---|
| Mastery + scheduling tool surface | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT (96★) |
| Scheduling engine | [open-spaced-repetition/fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) | **BSD-3-Clause** (456★) |
| Reference scheduler + optimiser | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | MIT (4.1k★) |
| Knowledge-tracing models | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT (457★) |
| LMS reach | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) or a Moodle REST adapter | MIT |

**Wiring:**
1. Deploy `tutor-mcp` as the single tool surface. It already packages Bayesian Knowledge Tracing, FSRS spaced repetition, prerequisite skill graphs and a frozen scoring rubric — do not rebuild these.
2. Link `fsrs-rs` for the scheduling computation. It is the embeddable engine (bindings for C, Python, Node.js, Dart and PHP in sibling repos), and **the computation is local**: no model call, no per-review token cost. Use `fsrs4anki`'s optimiser as the reference for fitting parameters per learner from their own review history.
3. Train or initialise pyKT models on the client's historical interaction data so mastery priors are not cold.
4. Pull the review-eligible item set from the LMS over `canvas-mcp` or a Moodle REST adapter, and write completion back.
5. Report **retention at 30 and 90 days** as the headline metric, not engagement.

**Why this is the pattern to attach to every other one:** FSRS ships inside Anki from v23.10, so this is validated at consumer scale rather than research-grade — unusual on this shelf. It is permissive end to end, it computes on-device or server-side with no inference cost, and retention is the outcome institutions actually measure. It is the cheapest credible answer to "show me it worked".

**Honest scoping:** FSRS schedules *review of known items*. It does not teach, and it needs an item bank with stable identities. If the client has no item bank, that is the first deliverable, and it is content work.

---

## P7 — Offline-first, permissive all the way down (6–8 weeks)
**Best fit:** Sub-Saharan Africa, rural South Asia, Pacific islands, and any deployment where connectivity cannot be assumed.
**Licence exposure:** none — and uniquely on this page, **not even at the platform layer**.

| Component | Repo | Licence |
|---|---|---|
| Learning platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (1.2k★) |
| Local inference | Ollama | MIT |
| Review scheduling | [open-spaced-repetition/fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) | **BSD-3-Clause** |
| Tutor (optional, when a device can run it) | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT |

**Wiring:**
1. Deploy Kolibri on a classroom server or directly on devices. ⚠️ **Resolve the branch first** — the default is `develop`; the release lines are `release-v0.19.x` and `release-v0.20.x`. Deploy from a release line, not from `develop`.
2. Run a small local model via Ollama on the classroom server. Learner data never leaves the premises, which is a connectivity answer *and* a trust answer — it is the posture African edtech builders have independently converged on.
3. Compute review scheduling with `fsrs-rs` on the device. This is the part that genuinely requires no network: no model call per review.
4. Sync to a central instance opportunistically, when connectivity appears. Design every workflow to be correct if the sync never happens.
5. Keep the proprietary layer in the Kolibri derivative itself — **MIT permits this**, which no other platform on this shelf does.

**Why it is strategically distinct:** every other pattern here keeps a stock copyleft platform and puts the IP in an out-of-tree agent layer. This is the one pattern where Globant can ship a closed product end to end, platform included. For a regional offering sold repeatedly across markets, that difference compounds.

**Honest scoping:** Kolibri is not an institutional LMS. There is no Moodle-class gradebook, no enrolment-at-scale, no large third-party plugin ecosystem. If the client needs institutional course management, this is the wrong base and **P2** is the right one.

---

## P8 — Moodle agent pilot, adopt-and-harden (LATAM public sector, EMEA K-12: 5–7 weeks)
**Best fit:** the ~60% of this KB's addressable market that runs Moodle — LATAM public education, EMEA K-12, Spanish- and Portuguese-speaking institutions.
**Licence exposure:** none in your code. The agent bridge is MIT and talks to Moodle over REST, so nothing you write becomes a GPL derivative.
**This is P1's twin for the other LMS, and it costs more. Price it that way.**

| Component | Repo | Licence | Role |
|---|---|---|---|
| Moodle agent bridge | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | MIT (1,064 B), **27★** | 22 tools over Moodle Web Services: courses, assignments (read + submit), forums, files-as-markdown, grades, schedule, messaging, quiz attempts, plus `call_ws_function` as the escape hatch. Rust, `rmcp`. States validation against Moodle 3.7 → 5.x |
| Permission model to copy | [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) | MIT (1,072 B), 4★ | Do not deploy it — **borrow its defaults**: writes and teacher grading off behind explicit env flags, token from browser SSO stored locally |
| Tutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 (55k★) | Persistent learner model. Self-host with local models for residency |
| Mastery + scheduling | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT (96★) | BKT + FSRS behind one tool surface — attach **P6** |
| Local inference | Ollama / vLLM | MIT / Apache-2.0 | Keeps learner data in-jurisdiction |

**Wiring:**
1. Stand up stock, unmodified Moodle. Enable Web Services and mint a dedicated service account with the **narrowest** capability set that the tool list needs — not an admin token.
2. Deploy `moodle-mcp` **out-of-tree**, in its own process. Pin the commit, not a branch. ⚠️ **Clone `G36maid/moodle-mcp`, not `thc1006/moodle-mcp`** — the latter ranks higher in search, is a fork, and is 43 commits behind.
3. **Harden before piloting, and bill for it.** This is the step that distinguishes P8 from P1: at 27★ the bridge has no meaningful external review. Audit token handling and storage; set writes to off-by-default behind explicit flags (`moodler-mcp`'s model); constrain or disable `call_ws_function`, which by design reaches *any* Moodle web service and is the broadest privilege in the stack; run your own integration tests against the client's actual Moodle version rather than trusting the 3.7 → 5.x claim; add rate limiting.
4. Point DeepTutor at the bridge. Attach `tutor-mcp` for mastery and review scheduling (**P6**).
5. Contribute the hardening upstream. It is cheap, it removes the single-maintainer risk from the client's position, and it is the honest basis for recommending a 27★ dependency at all.
6. Wrap in **P5** governance before anything student-facing goes live.

**Honest scoping — say all three of these out loud in the proposal:**
- **The Moodle agent layer is ~12× less reviewed than the Canvas one** (27★ against `canvas-mcp`'s 317★). That asymmetry is structural, not temporary. **P8 is genuinely more expensive than P1 and the difference is the hardening step**, not margin.
- **Six of the eight permissive Moodle servers measured have ≤4 stars.** There is no mature alternative to fall back to. If `G36maid/moodle-mcp` proves unsuitable after audit, the next step is a build, so run the audit in week one, not week four.
- **Do not reach for `csmediapro/moodle-mcp-server`** as the "more commercial-looking" option. It is **AGPL-3.0** with paid Premium Plugins, and an AGPL network-served agent defeats the entire out-of-tree containment that makes this pattern licence-safe.

---

## P9 — Sovereign, curriculum-grounded tutoring on education open weights (8–10 weeks)
**Best fit:** EMEA public education under data-residency constraints; Sub-Saharan African and other offline-first deployments; **and any Korean or Vietnamese client that needs an agent demonstrably off the system of record** (`intel/trends.md` **T15**).
**Licence exposure:** 🔴 **one unresolved gate — read it before scoping, not before delivery.**

| Component | Repo / artefact | Licence | Role |
|---|---|---|---|
| Curriculum-grounded model | [haolpku/Omni-Edu](https://github.com/haolpku/Omni-Edu) — OmniEdu-9B-FP8 (~11.09 GiB) or 27B-FP8 (~28.30 GiB) | **Apache-2.0 code; weight licence NOT NAMED** ⚠️ | K-12 subject competence, curriculum grounding, diagnostic reasoning, pedagogical scaffolding — in the weights rather than the prompt |
| Model toolkit + evaluation | `omniedu` (PyPI, same repo) | Apache-2.0 | Unified interface, OpenAI-compatible serving, image inputs, JSONL batch inference, 12-benchmark eval suite |
| Serving | vLLM / Ollama | Apache-2.0 / MIT | Single-GPU FP8 serving, no egress |
| Delivery platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (1.2k★, branch `develop`) | Offline-first content delivery, learner progress, coach tooling |
| Review scheduling | [open-spaced-repetition/fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) | **BSD-3-Clause** (456★) | On-device scheduling, zero inference cost |
| Mastery estimation | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT (457★) | Knowledge tracing priors |

**Wiring:**
1. 🔴 **Gate zero, before any engineering: read the OmniEdu weight licence on its Hugging Face card** (`lhpku20010120/Omni-Edu-9B` / `-27B`, and the `-FP8` variants). The repository's Apache-2.0 grant covers the **code**; the README says only that *"Model weights and third-party datasets and benchmarks retain their respective licenses"*, the backbones are Qwen, and `huggingface.co` did not resolve in the session that verified this pattern. **If the weight terms are not commercially usable, this pattern collapses to P7 with a general model** — so resolve it in the first conversation, not the first sprint.
2. Serve the FP8 checkpoint on a single GPU via vLLM. FP8 is the whole point: 37–44% smaller than BF16, which is what moves this from a research artefact to a deployable one.
3. Evaluate on the client's own curriculum with the `omniedu` suite **before** committing to the model. The published results are self-reported (27B: K12-Bench 63.12 EM / 76.69 F1, MathFish 85.89, EDUMATH MaC 86.95, MathTutorBench Scaffold 78.74) and — in the authors' own words — *"Benchmark performance does not establish classroom learning gains."* Take them at that value.
4. Deliver through Kolibri for offline-first, or through the client's LMS via **P8** / **P1** where there is connectivity.
5. Add `fsrs-rs` for review scheduling and pyKT for mastery priors — both compute locally, so the offline story stays intact.
6. **For Korea and Vietnam specifically:** keep the agent off the system of record and document that boundary as a deliverable. Vietnam's high-risk trigger bites only where results are *the official basis* for assessing or ranking learners; Korea names student assessment in its high-impact definition. A formative-only architecture with evidence is a materially smaller compliance programme than conformity work on a graded system.

**Why this pattern exists:** it is the first on this page where the *model* knows the curriculum rather than the prompt carrying it. That matters most exactly where general hosted models are hardest to use — in-jurisdiction, offline, or kept deliberately away from graded decisions. One artefact answers the binding constraint in three regions.

**Honest scoping:** the weight-licence gate is real and unresolved; a K-12 model trained on a Chinese-authored corpus needs curriculum-alignment evaluation per market before anyone claims grounding; and at 590★ / 9 commits this is a young repository with concentrated maintainer risk.

---

## P10 — AI-literacy delivery against a funded mandate (6–8 weeks per cohort)
**Best fit:** the mandate wave this KB tracks — **Canada's** National AI Literacy Initiative (one million entry-level post-secondary students, 3,000+ educators), **Saudi Arabia's** mandatory undergraduate AI literacy, **EU AI Act Article 4**, **Kenya's** strategy commitment with no framework yet written, **Idaho's** AI-literacy standards, the **UAE's** all-levels programmes.
**Licence exposure:** none. Every component is MIT.
**This is the one pattern on this page whose deliverable is curriculum and teacher capacity rather than software** — and it is the pattern that fits the largest publicly-funded commitments in this KB.

| Component | Repo | Licence | Role |
|---|---|---|---|
| Curriculum base | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | **MIT** (41.1k★, 6.6k forks) | 93+ runnable projects on LLMs, RAG, agents and MCP, tiered beginner (22) / intermediate (48) / advanced (23), plus an `ai-engineering-roadmap`. MIT ⇒ a commercial, closed, client-branded derivative is permitted |
| Delivery vehicle | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT (42.7k★) ⚠️ see gate | Multi-agent classroom with AI teachers *and* AI peers. **12 locales across 11 languages including Portuguese (Brazil), Spanish (Mexico), Arabic, Vietnamese, French, German** — the broadest localisation on this shelf |
| Platform | client's Moodle / Canvas / Open edX via **P8** / **P1** / **P3** | — | Enrolment, completion, credentialing |
| Retention | **P6** (`tutor-mcp`, `fsrs-rs`) | MIT / BSD-3-Clause | Literacy that is assessed once is forgotten; schedule the review |
| Measurement | **P5** governance + evaluation wrapper | — | The funder will ask what changed |

**Wiring:**
1. Fork `ai-engineering-hub` and cut the tiers down to the mandate's actual scope. A ministry asking for AI literacy for first-year undergraduates needs the 22 beginner projects, not all 93. Resist shipping the whole hub.
2. ⚠️ **Licence gate on OpenMAIC before it enters a deliverable.** The repository is MIT, but `packages/mathml2omml` is **LGPL-3.0-or-later** (7,652 B payload; `"license": "LGPL-3.0-or-later"` in its own `package.json`), it is declared `"workspace:*"` in the root manifest, and `build:packages` compiles it as **step one**. A built deliverable links it. Either keep that component dynamically replaceable with its source offered — LGPL permits this and it is an architecture decision, not a blocker — or excise the MathML-to-OOXML path if the client does not need Word/PowerPoint export. Decide at design time; retrofitting replaceability into a bundled JS build is expensive. Note also that OpenMAIC has only been MIT since **v0.3.0 (2026-06-28)** and the prior licence is not named in the repository, so pre-June history has no answer for a diligence question.
3. Localise with OpenMAIC's existing locales rather than translating a course. pt-BR and es-MX are already there, which covers the LATAM mandates; Arabic covers the Gulf.
4. Run cohorts through the client's own LMS (**P8** for Moodle, **P1** for Canvas) so completion lands in the system of record and credentialing works.
5. Attach **P6** so literacy is retained and **P5** so the funder gets outcome evidence rather than attendance.

**Why this is commercially distinct:** the AI-literacy mandates are *funded* and *dated*, and they cannot be satisfied by a tutoring agent — a client cannot buy curriculum from a chatbot. `ai-engineering-hub` at 41.1k★ is the most-adopted permissive asset of its kind, and the licence is the whole reason it is here: the nearest alternative, `GarethManning/education-agent-skills` (949★), is **CC BY-SA 4.0**, whose ShareAlike term forces any derivative skill library to be CC BY-SA and so rules out a closed client deliverable. Same category, opposite answer, and the permissive option is 43× more adopted.

**Honest scoping:** `ai-engineering-hub` is *AI-engineering* material for developers — it is the right base for undergraduate, vocational and educator-upskilling cohorts, and the **wrong** base for K-12 AI literacy, which this KB has no permissive curriculum for and which remains an open gap. Contextualising and pedagogically sequencing the content is the real work; the repository is raw material, not a course.

---

## P11 — Permissive institutional LMS, closed deliverable (greenfield HE, EMEA public sector: 10–12 weeks) 🟢 new at p653

**The only pattern in this file where the institutional platform itself permits a closed derivative.** Use it when the client is *choosing* a platform rather than extending one — a new faculty, a national programme, a public-sector training body, a migration off a commercial LMS.

```
OpenOlat  (Apache-2.0, 449★/32,210 commits, branch OpenOLAT_21.1)
  ├── PostgreSQL JDBC 42.7.14 (BSD-2-Clause)   ← NOT MySQL Connector/J: see below
  ├── langchain4j 1.23.0 (Apache-2.0, already in pom.xml)
  │     ├── langchain4j-open-ai     ──► Ollama or vLLM on in-jurisdiction hardware
  │     │                                (OpenAI-compatible wire protocol: config, not code)
  │     ├── langchain4j-anthropic   ──► hosted fallback where egress is permitted
  │     └── langchain4j-embeddings  ──► embeddings computed in-process
  ├── Apache Lucene (Apache-2.0, already in pom.xml) ← semantic course search, no egress
  └── fsrs-rs (BSD-3-Clause) via JNI/sidecar  ← review scheduling
```

**Week 1–2** — stand up OpenOlat from `OpenOLAT_21.1` (never from `master`; see the branch section). Specify **PostgreSQL** in the architecture document and say why in one line.
**Week 3–5** — wire `langchain4j-open-ai` to a client-hosted Ollama or vLLM endpoint. No new dependency, no fork. Prove the no-egress claim with a network capture, not a diagram.
**Week 6–8** — course-content semantic search over Lucene + `langchain4j-embeddings`; this is the demo that lands with faculty.
**Week 9–12** — mastery and scheduling: `fsrs-rs` as a sidecar, exposed through the **P6** MCP surface so the tutor and the LMS share one retention model.

🔴 **The one licence decision that makes or breaks the closed deliverable.** Of 270 declared dependencies, exactly one is copyleft: **MySQL Connector/J (GPL-2.0 + Universal FOSS Exception)**. The exception covers combination with OSI-approved open source licences — it does **not** cover a closed proprietary derivative, which is the whole reason for choosing this platform. PostgreSQL JDBC (BSD-2-Clause) is already in the tree and a first-class backend. **Specify PostgreSQL and the tree is permissive end to end.** Verified absent from the tree: iText (AGPL-3.0) and JasperReports (LGPL), the two usual Java-LMS killers; Hibernate is 7.4.14 and hibernate-validator 9.1.6, both Apache-2.0 eras.

⚠ **Price the skill-set, not the licence.** Java/Spring/Hibernate is heavier than PHP-Moodle or Python-Open edX, there is no plugin marketplace of Moodle's scale, and the contributor base is concentrated around one vendor (frentix GmbH). P11 buys a licence position and a residency story. It does not buy a cheaper build, and a proposal that implies otherwise will be wrong by week 6.

## P12 — The OpenOlat agent bridge: build the thing that does not exist (6–8 weeks) 🟢 new at p653

**The cleanest greenfield position in this KB.** The LMS-bridge picture across the three platforms this base tracks is **Canvas 317★ → Moodle 27★ → OpenOlat 0**: `openolat-mcp`, `frentix/openolat-mcp` and `OpenOLAT/openolat-mcp` were all probed at p653 and **none resolves.**

Why this is a better build than it looks, on three counts that do not usually co-occur:

1. **No incumbent to displace.** Unlike Moodle (seven MIT servers competing at ≤27★, where the work is hardening someone else's code — see **P8**), there is nothing to fork and no upstream to negotiate with.
2. **No copyleft to route around.** Patterns A, B and C all exist to keep proprietary work *outside* a platform that cannot absorb it. OpenOlat is Apache-2.0, so **the agent can live in-tree, in the same Maven build**, and the deliverable can still be closed.
3. **The LLM layer is already there.** `langchain4j` with OpenAI, Anthropic and embeddings modules is in `pom.xml` today, so the bridge does not need to ship a model client.

```
Weeks 1–2   Read OpenOlat's REST surface + the langchain4j wiring already in-tree.
            Borrow the permission model from GhaithAlHallak8/moodler-mcp (MIT):
            browser SSO → locally-stored token; writes and grading OFF by default
            behind explicit env flags. It is the safest default posture this KB
            has measured in any LMS bridge — copy it rather than re-deriving it.
Weeks 3–5   MCP server over the official SDK. Tool surface modelled on
            G36maid/moodle-mcp (MIT, 22 tools: identity, courses, assignments
            read+submit, forums, files-as-markdown, grades, schedule, messaging)
            — a proven taxonomy, re-implemented against OpenOlat's API.
Weeks 6–8   Attach a tutor: zijinz456/OpenTutor (MIT, 166★) for local-first, or
            Bloom (MIT) for the fastest demo. Gate every write behind the
            WAITING_REVIEW shape from littlecookie0722/AI-Teaching-Agent.
```

🟢 **Contribute it upstream under Apache-2.0 and the strategic return exceeds the engagement fee.** This is the one place in this KB where Globant could own the reference integration for an entire platform rather than the third fork of someone else's.

## P13 — Assessment: adopt-and-harden a research decomposition (10–14 weeks) 🟢 new at p653

**The one pattern here where the production artefact does not exist yet and Globant would create it.** Four passes established that there is no adopted permissive education assessment tool; p653 established that there is permissive, education-specific, peer-reviewed *research* supply. That changes the engagement from "build a grader" to "productise a published decomposition", which is scopeable.

```
ArguLens / wwrwbs/AI_AWE  (Apache-2.0 by reference, arXiv:2608.17356)
  ├── discourse-move classifier
  ├── grade-independent LightGBM scorer over 31 linguistic/discourse features
  └── label-aware feedback generator        ← the part clients actually want
        │
        ├── calibration layer  ◄── microsoft/LLM-Rubric (MIT, 45★)
        │      calibrate rubric outputs against THIS client's human raters
        │
        └── human-approval gate ◄── littlecookie0722/AI-Teaching-Agent (MIT)
               WAITING_REVIEW state + Docker-sandboxed evaluation + no auto-publish
```

**Why these three and not one.** ArguLens supplies the education-specific decomposition and, unusually, *grade-independent* features — which is what makes it portable to a curriculum it was not trained on. `LLM-Rubric` supplies the mechanism ArguLens lacks and that every institution demands: calibrating machine scores against the client's own markers, so the output is defensible in an appeals process. `AI-Teaching-Agent` supplies the review-state machine, and its shape — explicit approve/reject, sandboxed execution, **no automatic publishing** — is the shape an Annex III high-risk deployment needs anyway.

🔴 **Three constraints to put in the proposal, not discover in week 9.**
- 🔧 **The training corpus does not come *in the repository* — but it is not academic-use-only, and p675 corrects that.** This bullet read *"Persuade 2.0 is academic-use-only"* for 618 passes. 🟢 **The copyright holder's own repository grants it `CC BY 4.0`**: [`scrosseye/persuade_corpus_2.0`](https://github.com/scrosseye/persuade_corpus_2.0), README `2,081 B`, sha256₁₆ `2f984c8712650050`, `main` @ `5bdbad1175d1` — *"The data is provided under Creative Commons Attribution 4.0 International License (CC BY 4.0)."* Attribution only; no NonCommercial, no ShareAlike. 🔵 **And the `CC BY-NC-SA 4.0` reading is the same author's *other* corpus:** `scrosseye/CLEAR-Corpus` grants `NC-SA` in the same one-sentence form, one token apart. PERSUADE 1.0 ([`scrosseye/PERSUADE_corpus`](https://github.com/scrosseye/PERSUADE_corpus), README `3,486 B`, sha256₁₆ `809c25c2379d639e`) grants `CC BY 4.0` too. The `academic-use-only` reading came from `ArguLens`'s own notice; **both readings are third parties to the grant.** 🔴 **What stays true:** the data is **not in the repo** (two Google Drive links, the test set a password-protected zip), so a retrain is still a *fetch-and-attribute* step rather than a dependency — and the client's own marked scripts remain the better corpus for any non-US, non-English construct. See [`../agents/trending.md`](../agents/trending.md) `675-A`.
- **Bias is documented by the authors, not discovered by you.** ArguLens's own licence file carries the notice: AES systems inherit bias from training data (Persuade 2.0 is US middle-school argumentative essays), and it is *"intended for research and assistive use, not for high-stakes automated decisions without human oversight."* Quote that in the proposal. It is the authors' own framing and it is the correct one.
- **Adoption is zero.** 2★ / 2 commits and 0★ / 30 commits. These are artefacts, not projects: budget for reading papers and writing tests, and do not price it as integration.

⚠ **Scope it as assistive scoring with human sign-off, never as autonomous grading.** Under EU AI Act Annex III, evaluating learning outcomes is high-risk; Washington DC's 2026 policy bars AI from grading outright. The deliverable that is legal in both places is the one that scores and explains while a human decides.

## P14 — Corporate L&D as a closed, client-branded product (EMEA / North America enterprise: 8–10 weeks) 🟢 new at p655

**Buyer:** a corporate L&D or compliance function, not an academic institution. They expect *their* brand on the product and will not accept a licence conversation.

```
Selleo/mentingo (MIT, 106★, main)                 ← fork; MIT permits a closed, rebranded derivative
  ├── already in core, read from the manifest at p655:
  │     ai 7.0.148 + @ai-sdk/openai 4.0.8 + @ai-sdk/workflow 2.0.80   (Vercel AI SDK)
  │     langchain 0.3.34 · pgvector retrieval on PostgreSQL 16
  │     LiveKit  → real-time voice role-play, scored automatically
  │     Langfuse → per-interaction trace = the compliance audit trail
  │     multi-tenant + white-label + SCORM export + 6 UI languages
  ├── swap the model provider for Ollama (MIT) or vLLM (Apache-2.0) when the client requires on-prem
  └── jupyter/nbgrader (BSD-3-Clause) only if the curriculum is technical — otherwise the
        in-core scenario assessment engine is sufficient and already scored
```

**Weeks 1–2** fork, rebrand, stand up Postgres 16 + pgvector / Redis / S3-compatible storage in the client's region; **EU-only residency is a configuration choice here, not a paid tier**. **Weeks 3–5** harden: this is a 1,397-commit, 106★ codebase — budget the security review, the load profile (its own `perf:load`/`perf:stress`/`perf:soak` suites exist and should be run against the client's concurrency target) and multi-tenancy isolation testing explicitly. **Weeks 6–8** author the first compliance track against the scenario assessment engine; wire Langfuse traces into the client's evidence store. **Weeks 9–10** recertification and expiry rules, then pilot cohort.

**Why this is not Pattern F.** F is OpenOlat for institutional higher education — a different buyer, a longer cycle, and one that does not need rebranding. **Say the trade out loud in the proposal:** Moodle (GPL-3.0), Open edX (AGPL-3.0) and Canvas (AGPL-3.0) are mature and copyleft; Mentingo is MIT and young. You are buying licence freedom with hardening effort. Quantify the hardening rather than hiding it.

**Do not** present 106★ as adoption. Present it as what it is: the only MIT platform where multi-tenancy, white-labelling and the agent are all in core.

## P15 — Autograded technical curriculum, permissive end to end (bootcamps, CS faculties, data academies: 6–8 weeks) 🟢 new at p655

**Buyer:** anyone teaching code, data or quantitative methods at cohort scale — and this KB's **largest unserved segment until p655**, because it searched for education tools and this stack files itself as infrastructure.

```
JupyterHub (BSD-3-Clause, 8,362★, main)           ← one isolated, authenticated, resource-capped env per learner
  ├── LTI auth → the client's existing Moodle / Canvas / Open edX stays the front door
  │                (no migration, no copyleft contact: the LMS is a separate process)
  ├── Kubernetes spawner for cohort scale; Docker spawner for a pilot
  └── jupyter/nbgrader (BSD-3-Clause, 1,370★, main)
        release → collect → autograde → manual grade → feedback
        ├── deterministic per-cell tests score what is checkable      (no LLM, no hallucination surface)
        ├── microsoft/LLM-Rubric (MIT, 45★) scores what is not: prose, design rationale, code quality,
        │     calibrated against this client's own human raters       ← the calibration is the deliverable
        └── formgrader + gradebook → the human decision boundary, which several jurisdictions now require
              └── Ollama (MIT) or vLLM (Apache-2.0) inside the client network for the rubric model
```

**Weeks 1–2** JupyterHub on the client's Kubernetes, LTI into their existing LMS, environment images per course. **Weeks 3–4** nbgrader assignment structure; port one real existing assignment and reproduce its historical grades — **that reproduction is the credibility test, run it before anything else is promised.** **Weeks 5–6** LLM-Rubric for the non-deterministic dimensions, calibrated on a sample the client's own graders have already scored; report the agreement statistic honestly, including if it is poor. **Weeks 7–8** cohort pilot, grader training, appeals workflow.

**The licensing story is the simplest on this page: BSD-3-Clause, BSD-3-Clause, MIT, MIT — no copyleft anywhere, no AGPL network trap, closed derivative permitted throughout.** Only Pattern E (Kolibri offline) matches it, and E does not cover assessment.

🟢 **Amended at p657 — scope this against P19 before proposing it.** This pattern is correct for a *course-level* engagement where the client's LMS stays the front door and Jupyter is the work surface. It is **not** the right answer at faculty or institution scale, because p657 shelved four permissive production autograders this pattern predates: `Artemis` (MIT, 826 ★), `Autolab` (Apache-2.0, 808 ★), `Submitty` (BSD-3-Clause, 805 ★) and `otter-grader` (BSD-3-Clause, 162 ★). **Two concrete substitutions.** First, if the curriculum includes **R** — statistics, econometrics, quantitative methods — use `otter-grader` rather than `nbgrader`: same BSD-3-Clause licence, same assignment source, and it grades R, which `nbgrader` does not. Second, if the client needs submission handling, plagiarism workflow, TA assignment, regrade requests and an appeals trail, those are **built** in `Submitty` and would be months of bespoke work here. Choose P15 for one course or one cohort; choose **P19** for a faculty.

**State the boundary explicitly and in writing:** this grades submitted work; it does not establish **who** submitted it. **No permissively-licensed proctoring or assessment-integrity tool was found in five passes of searching** (see `repos/foundations.md`). If the client needs identity assurance, that is a commercial tool and a separate line item — do not imply this stack provides it.

## P16 — Retention that writes into a scheduler people already use (4–5 weeks) 🟢 new at p655

A narrower, faster sibling to **P6**, enabled by one row added at p655.

```
ankimcp/anki-mcp-server (MIT, 544★, main, v0.27.0 "active beta")
  └── exposes decks, notes, note types, cards, scheduling and review state over MCP
       ├── ArnaudGuiovanna/tutor-mcp (MIT, 96★) → mastery: BKT + prerequisite graph + frozen rubric
       ├── CAHLR/pyBKT (MIT, 291★, master)      → interpretable mastery estimates when a board must audit them
       └── the agent of choice (any MCP client) decides WHAT to schedule; FSRS decides WHEN
            └── FSRS already ships inside Anki from v23.10 — fsrs4anki (MIT) / fsrs-rs (BSD-3-Clause)
```

**Why this is worth a separate pattern.** Every other retention design in this KB reimplements scheduling. This one does not: the learner keeps the client they already have, the scheduler is the one with consumer-scale production proof, and the agent's job shrinks to *selection* — which is the part a tutor is actually good at. **4–5 weeks** because there is no platform to stand up: weeks 1–2 wire the two MCP servers behind one agent, week 3 define the card-generation and selection policy against real course material, weeks 4–5 run a cohort and measure retention against the client's existing baseline.

⚠️ `anki-mcp-server` self-describes as **active beta at v0.27.0**. Pin the version, read the changelog before upgrading, and do not put it on a critical path for a graded outcome without a fallback.

## P17 — The evidence spine: LTI in, xAPI out, nothing forked (4–6 weeks) 🟢 new at p656

Not a standalone engagement — the layer that goes **underneath** P1–P16 and makes any of them provable. Every pattern above eventually meets the same two questions: how does our thing appear inside the LMS the client already runs, and how do we show it worked. Ten rows added at p656 answer both, and all of them are permissive.

```
THE CLIENT'S EXISTING LMS  (Moodle GPL-3.0 / Canvas / Brightspace / Open edX AGPL-3.0 / OpenOlat Apache-2.0)
  │
  │  ── LTI 1.3 launch ──▶  no fork, no copyleft inherited: an LTI tool is a separate work
  │
  ├── tsugiproject/tsugi (Apache-2.0, 377★, master)        → PHP: LTI13, AGS, NRPS, Deep Linking, unit tests
  ├── dmitry-viskov/pylti1.3 (MIT, 138★, master)           → Python/Django/Flask  ⚠️ 2 yrs quiet, pin it
  └── jupyterhub/ltiauthenticator (BSD-3, 73★, main)       → launches JupyterHub (BSD-3) + nbgrader (BSD-3)
       │
       ▼
  THE AGENT LAYER  (yours, proprietary — MIT/Apache deps only)
       │   e.g. HKUDS/DeepTutor (Apache-2.0) · ArnaudGuiovanna/tutor-mcp (MIT) · CAHLR/pyBKT (MIT)
       │
       ├── content the client already owns:
       │     jcputney/scorm-again (MIT, 362★, 0 open issues) → plays SCORM 1.2/2004, AICC, cmi5
       │     ⚠️ authored in H5P (GPL-3.0) or Adapt (GPL-3.0)? call it, never fork it
       │
       ├── assessment:
       │     numbas/Numbas (Apache-2.0, 216★) → maths/quantitative, randomised, partial credit
       │     jupyter/nbgrader (BSD-3, 1,370★) → notebook autograding
       │
       ▼
  THE EVIDENCE SPINE  ◀── the deliverable that converts a pilot into a renewal
       RusticiSoftware/TinCanJS (Apache-2.0, 208★)  → emits xAPI statements from content
            ⚠️ 3 yrs quiet: vendor and audit it; the protocol is frozen so this is survivable
       adlnet/xAPI-Spec (Apache-2.0, 955★)          → the statement shapes to conform to
       yetanalytics/lrsql (Apache-2.0, 144★, main)  → 🔴 THE ONLY LIVE PERMISSIVE LRS
            runs on SQLite / PostgreSQL / MySQL · actor, verb, object, result, timestamp
            └── query it for: time-on-task, attempt counts, mastery trajectory, cohort deltas
```

**Why this is a pattern and not a footnote.** P5 has sold "governance and measurement" since early in this KB's life without naming a single component, and T10 and T19 have recorded for many passes that the evidence base is this sector's weakest point. The gap was never that the measurement substrate did not exist — `lrsql` has been verified in this repository's logs under the words *"el candidato de producción permisivo"* — it was that it had never reached a shelf. **An Apache-2.0 LRS is the difference between "the tutor seems to help" and a queryable statement log a client's own analysts can audit.**

**Timeline 4–6 weeks**, on top of an existing engagement: week 1 stand up `lrsql` against the client's database of record and agree the statement vocabulary (this is the only genuinely hard design step — a vague verb set makes the whole log unanalysable); weeks 2–3 wire the LTI launch so the tool appears inside their LMS with their roster and no second login; week 4 instrument the agent and the content to emit statements; weeks 5–6 build the cohort-delta queries and hand the client the dashboard **plus the SQL**, because a measurement they cannot re-run themselves will not survive a change of sponsor.

🔴 **Two risks to put in the proposal, not discover later.**
1. **`lrsql` is a single point of failure.** It is the only live, maintained, permissively-licensed LRS. `LearningLocker/learninglocker` (584★) is GPL-3.0 *and* dormant since 2024-05-30; `adlnet/ADL_LRS` is Apache-2.0 but ~12 months quiet. One Clojure project, nine open issues. If the client needs a supported LRS with a vendor SLA, that is a commercial product and this pattern does not apply.
2. **Four of the ten components are over a year quiet and none is archived**, so GitHub's staleness signal never fires. Read `pushed_at` before `stars` on this layer and pin every version.

**Where this does not apply.** A greenfield build with no incumbent LMS (use P11 or P15 and own the whole stack), and any engagement where the client's measurement requirement is a compliance artefact rather than an analytical one — a regulator wanting a transparency notice under EU AI Act Article 50 is not asking for an LRS.

## P18 — Adaptive assessment, permissive end to end (ministries, national platforms, professional certification: 10–14 weeks) 🟢 new at p657

**Buyer:** anyone who must place a learner on a scale defensibly — a ministry running a national diagnostic, a professional body certifying candidates, a university placing students into streams. **This is the pattern this KB has pointed at since P4 without being able to name the item-selection component.** Now it can.

```
the client's existing item bank (usually PDF/Word, sometimes QTI)
  └── bigdata-ustc/EduNLP (Apache-2.0, 64★)        ← parse items: text + formulae + figures → structured objects
        └── CALIBRATE item parameters (difficulty, discrimination)
              ├── eribean/girth (MIT, 127★)  or  17zuoye/pyirt (MIT, 111★)   ← 1PL/2PL/3PL + polytomous
              └── tswsxk/EduData (Apache-2.0, 83★)  ← public response data for COLD START, before the
                                                        client has any of its own  ⚠️ not the client's learners
        └── DIAGNOSE which skills are held
              └── bigdata-ustc/EduCDM (Apache-2.0, 203★)  ← IRT · MIRT · DINA · NeuralCD
                    └── CAHLR/pyBKT · pykt-team/pykt-toolkit  ← mastery over time (already shelved)
        └── SELECT the next item   ★ the load-bearing component ★
              └── douglasrizzo/catsim (BSD-3-Clause, 153★, branch `dev`, v0.9.1)
                    initialisation · item selection · ability estimation · stopping rule,
                    each pluggable, plus SIMULATION to test the design before any learner sees it
                    └── bigdata-ustc/EduCAT (MIT, 77★) only if the client wants the learned-policy comparison
  └── DELIVER:  ls1intum/Artemis (MIT) quiz exercises  or  numbas/Numbas (Apache-2.0) in-browser
  └── RECORD:   yetanalytics/lrsql (Apache-2.0) over xAPI  ← the audit trail, non-negotiable
```

**Weeks 1–3** parse and structure the real item bank; agree the skill model with the client's subject experts — *this is the deliverable that takes longest and it is not a technical task*. **Weeks 4–6** calibrate on whatever historical response data exists; if none, fit on `EduData` and state in writing that the parameters are provisional. **Weeks 7–9** `catsim` simulation: run synthetic cohorts against the calibrated bank and report test length, measurement error and exposure rates **before** anything is promised about shortening the test. **Weeks 10–12** pilot delivery with the full xAPI trail. **Weeks 13–14** recalibrate on the pilot's own responses — which is the point at which the parameters become real.

🟢 **Why this is defensible where an LLM-scored adaptive test is not.** Every step is a **published, inspectable, five-decade-old statistical method**. Under EU AI Act Annex III, Korea's high-impact scope and US state guardrails, "we selected item 14 because the maximum-information criterion at the current ability estimate chose it" is an answer; "the model decided" is not. **Explainability here is a property of the algorithm, not a feature to build.**

⚠️⚠️ **The two risks to price explicitly, because this pattern hides them better than any other on this page.** First, **six of the seven components are dormant** — `EduNLP` (2024-03), `EduData` (2023-05), `EduCDM` (2024-10), `EduCAT` (2024-08), `girth` (2022-09), `pyirt` (2023-08); only `catsim` is live (2026-11-01). The mathematics does not rot, but **the engagement is adopting maintenance responsibility for unmaintained code and must bill for it.** Second, **`catsim`'s default branch is `dev`** — clone `main` and you get nothing. Third, **calibration needs response volume**: below a few hundred responses per item the parameters are noise, and a proposal that promises adaptivity on a cold bank is promising something it cannot deliver in the pilot window.

## P19 — Autograded faculty at institution scale: adopt and harden, do not build (CS / engineering faculties, technical universities: 8–12 weeks) 🟢 new at p657

**Buyer:** a faculty or university that grades code, proofs, diagrams or quantitative work at cohort scale and is currently doing it with teaching assistants, spreadsheets and goodwill. **The premise of this pattern is that Globant writes no grader.**

```
PICK ONE PLATFORM — they are not interchangeable:

  ls1intum/Artemis (MIT, 826★, `develop`, v10.3.1) — TUM        ← choose when AI is wanted in-tree
    ├── programming · text · modeling (Apollon, MIT) · quiz · file upload
    ├── Atlas: competencies, learning paths, analytics
    ├── Iris (LLM tutor) · Athena (feedback SUGGESTION) · Hyperion (exercise authoring)
    │     ALL configuration-gated, OFF by default  ← the procurement feature, not a limitation
    └── ls1intum/Pyris (MIT) → point at the CLIENT's Ollama / vLLM endpoint, never a public API

  Submitty/Submitty (BSD-3-Clause, 805★/1,119 forks, `main`, v26.10.04) — RPI
    └── choose when the SUBMISSION and HUMAN-GRADING workflow is the hard part:
        TA assignment, regrade requests, appeals trail, plagiarism workflow — all built

  autolab/Autolab (Apache-2.0, 808★, `master`) — CMU
    └── choose for containerised programming autograding with a clean separation:
        autolab/Tango (Apache-2.0) is the sandboxed execution service and runs standalone

  + ucbds-infra/otter-grader (BSD-3-Clause, 162★) for the R half of the curriculum
  + jupyter/nbgrader (BSD-3-Clause) if the work surface is notebooks → see P15
```

**Weeks 1–2** deploy on the client's own infrastructure; **LTI into the incumbent LMS so it stays the front door** (Pattern I / P17 — no migration, no copyleft contact). **Weeks 3–5** migrate real existing exercises and **reproduce their historical grades — run this before anything else is promised**, exactly as P15 requires; it is the credibility test and it is cheap. **Weeks 6–8** enable at most one AI subsystem, for one cohort, and **calibrate `Athena`'s suggestions against the client's own graders, reporting the agreement statistic honestly including if it is poor.** **Weeks 9–10** appeals workflow and grader training. **Weeks 11–12** xAPI trail into `lrsql` and the governance pack: which subsystem was enabled, for whom, what it touched, where the human decided.

🟢 **What Globant is actually selling, and it is worth more than a grader.** Deployment, integration, exercise migration, calibration against the client's raters, the appeals and governance workflow, and grader training. ⚠️ **Say out loud in the proposal that the platform is existing open source** — a client who later discovers that a "custom platform" was MIT software from TUM has a legitimate grievance, and the honest version is the stronger pitch anyway: six universities already run this code.

⚠️ **The same hard boundary as P15, restated because it does not move:** this grades submitted work; it does not establish **who** submitted it. **No permissively-licensed proctoring or assessment-integrity tool has been found in any pass** (see **T20**). Identity assurance is a commercial tool and a separate line item.

## P20 — Spoken-language assessment, self-hosted (LATAM and APAC language programmes, corporate English training: 6–8 weeks) 🟢 new at p657

**Buyer:** a language school, a ministry's English programme, or a corporate training function currently paying per utterance to a cloud speech API — or doing nothing because that cost did not scale.

```
learner records a target sentence (phone or browser, no special hardware)
  └── Halleck45/OpenPronounce (MIT, 184★) — CPU-only, `pip install openpronounce`
        returns: score · mispronounced words with sounds ACTUALLY HEARD in IPA ·
                 per-word confidence · transcription · pitch + energy curves
        ├── Kyubyong/g2p (Apache-2.0, 936★)          ← English target pronunciation
        ├── CUNY-CL/wikipron (Apache-2.0, 376★)      ← Spanish · Portuguese · hundreds more
        └── liguozheng-ac/japanese-speech-xray (MIT, 177★) ← pitch-accent languages (JA, ZH)
  └── launch inside the client's LMS over LTI 1.3  (Pattern I / P17 — tsugi or pylti1.3)
  └── record every attempt to yetanalytics/lrsql (Apache-2.0) over xAPI
        → the cohort-level progress curve, which is what the buyer is actually paying for
```

**Weeks 1–2** stand up `OpenPronounce` in the client's estate and **score a sample of the client's own recordings against their own teachers' judgements — report the correlation before anything else happens.** **Weeks 3–4** target-language lexicon from `g2p` (English) or `wikipron` (everything else); set the scoring thresholds *with* teachers rather than for them. **Weeks 5–6** LTI launch from the existing LMS; xAPI statements into `lrsql`. **Weeks 7–8** pilot cohort and the progress reporting.

🟢 **The commercial case is a line item the client already pays.** `OpenPronounce` is positioned by its own author as a self-hosted alternative to **Azure Pronunciation Assessment**: a metered per-utterance cloud cost becomes a CPU container. And because **voice is biometric-adjacent personal data**, keeping it on-premise *removes* an EMEA cross-border transfer question rather than answering it — the compliance argument and the cost argument are the same deployment decision.

⚠️ **Three boundaries, all of which belong in the proposal in writing.** (1) **Phoneme accuracy is not fluency and not a CEFR level** — it does not replace a human oral examiner, and a proposal implying otherwise will fail its first expert review. (2) `OpenPronounce` is **184 ★ with a single maintainer**: pilot against real recordings before committing, and budget to carry it. (3) The better-known project in this layer, `Thiagohgl/ai-pronunciation-trainer` (525 ★), is 🔴 **AGPL-3.0** — usable as a deployed service, **never** as the client's product; if a client has already found it, that licence difference is the reason to choose `OpenPronounce` despite lower adoption.

## P21 — Verifiable skills credentials, closed derivative permitted (corporate academies, professional bodies, workforce programmes: 6–8 weeks) 🟢 new at p657

**Buyer:** anyone whose completions currently end in a PDF certificate — a corporate academy, a professional body, a government reskilling programme. **Skills-based credentialing is a named 2026 buying trend (1EdTech, see T34) and the permissive supply for it is one project (T33).**

```
learner completes assessed work
  └── the assessment itself: Artemis (MIT, P19) or the adaptive test from P18
        └── evidence recorded to yetanalytics/lrsql (Apache-2.0) over xAPI
              ← the credential must POINT AT evidence, or it is a PDF with extra steps
  └── learningeconomy/LearnCard (MIT, 70★, `main`)   ★ the only permissive issuer ★
        Issue · Earn · Store · Share · Map
        standards read from the monorepo's own package list this pass:
          @learncard/vc-plugin · vc-api-plugin        → W3C Verifiable Credentials, VC-API
          @learncard/openid4vc-plugin · sd-jwt-vc-plugin → OpenID4VC, SD-JWT-VC
          @learncard/didkit-plugin · didkey-plugin · did-web-plugin · chapi-plugin → DIDs, CHAPI
        └── ships its own AGENT SKILL: `npx @learncard/cli skill install`
              → an agent from agents/top.md can issue and verify directly
```

**Weeks 1–2** the **competency model** — which skills exist, what evidence counts, who may assert it. This is the deliverable and it is a facilitation task, not an engineering one; `Artemis`'s Atlas competencies or a 1EdTech CASE framework can carry it. **Weeks 3–4** `LearnCard` issuance wired to the assessment's completion events, each credential referencing its xAPI evidence. **Weeks 5–6** holder wallet and verification flow; decide `did:web` (institution-anchored, simplest to explain to a registrar) versus `did:key`. **Weeks 7–8** recognition — the part that determines whether the credential has value: at least one external party that will *accept* it.

🟢 **Licence position is unusually clean: MIT throughout**, so the client's branded wallet and issuer are a closed derivative. **Every alternative in the layer is copyleft** — `tahrir` AGPL-3.0, `certo` AGPL-3.0, `openbadgeslib` LGPL-3.0, `badgr-ui` AGPL-3.0 **and archived** (**T33**). If a client has already piloted a badge platform, the licence is very likely why it cannot become their product.

⚠️ **Two risks, and the second is the one that kills these projects.** (1) **`LearnCard` is 70 ★ with 42 open issues and one sponsoring organisation** — the same single-vendor shape **T28** flags for `lrsql`, and both appear in this stack, so a proposal resting on P21 is resting on two single-vendor dependencies. Name them. (2) **A credential nobody accepts is worth nothing.** Standards conformance (W3C VC, OBv3, OpenID4VC) is necessary and not sufficient; **the engagement must deliver at least one relying party that will honour the credential**, and if the client cannot name one, build the evidence layer (`lrsql`) first and the credential later.

## P22 — A national or district K-12 coding platform, MIT end to end (ministries, state education departments, large districts: 10–14 weeks) 🟢 new at p658

**Buyer:** a ministry, state education department or large district that wants its *own* branded coding environment — its curriculum, its language, its hardware, its data residency — and has been quoted a per-seat SaaS price for Code.org or a commercial equivalent. **The whole stack below is MIT, so the deliverable can be a closed, branded product.**

```
MakeCode core — microsoft/pxt (MIT, 1,105 B, `master`, 2,314★, pushed 2026-11-05)
  │   blocks ⇄ JavaScript ⇄ Python on ONE AST; compiles IN-BROWSER; runs offline
  ├── target: microsoft/pxt-microbit  (MIT, 1,143 B, `master`, 806★)   → micro:bit hardware
  ├── target: microsoft/pxt-arcade    (MIT, 1,162 B, `master`, 550★)   → game-based CS curriculum
  └── block layer underneath: RaspberryPiFoundation/blockly (Apache-2.0, `main`, 13,600★)
        ★ note the OWNER: transferred from Google 10 Nov 2025 (T36). Cite the new address. ★
  │
  ├── hardware lab, no egress: openblockcc/openblock-desktop (MIT, `main`, 302★)
  │     + microbit-foundation/micropython-microbit-v2 (MIT, `master`) for firmware
  │
  └── LMS boundary — process boundary = licence boundary (base architecture above)
        Moodle (GPL-3.0) or Open edX (AGPL-3.0), STOCK, reached over LTI 1.3 via
        Cvmcosta/ltijs (Apache-2.0, 11,361 B — see p646)
        └── evidence out: yetanalytics/lrsql (Apache-2.0) over xAPI  → P17 / P21
```

**Weeks 1–3** stand up `pxt` with one target and reskin it — this is configuration, not a fork, and the demo that wins the engagement is the client's own logo on a block editor compiling their curriculum's first lesson in a browser with the network off. **Weeks 4–7** curriculum encoding: the blocks the client's syllabus actually needs, authored as a MakeCode extension, plus localisation. **Weeks 8–10** hardware path, if any — micro:bit is the cheapest credible option and its firmware is MIT. **Weeks 11–14** LTI integration into the existing LMS and xAPI telemetry, so the ministry can answer "did it work?" (**T19**'s outcome gap).

🟢 **Licence position: MIT throughout the layer you modify**, Apache-2.0 one level down in Blockly. No copyleft anywhere in the build path, so a branded closed derivative is permitted. 🔴 **Do not reach for Code.org for this** even though it looks like the closer fit: its code is Apache-2.0 but its courseware is carved out and may not be embedded in another format, and its Minecraft assets need a separate agreement with Microsoft (**T39**). **Do not fork `scratch-gui`** — AGPL-3.0, and this is a hosted service (**T40**).

⚠️ **Risks.** (1) `pxt` is Microsoft-governed and single-vendor; it is MIT, so a fork is always available, but roadmap influence is nil — name it. (2) **Curriculum content is the real cost**, not the editor; a proposal that prices the platform and not the lessons will be re-scoped in month two. (3) Blockly's stewardship changed hands a year ago and client SBOMs will still say `google/blockly` (**T36**) — budget an afternoon for alias reconciliation rather than discovering it in a security review.

## P23 — The block-to-text bridge with an LLM tutor inside the workspace (secondary schools, coding academies, CS faculties: 6–8 weeks) 🟢 new at p658

**Buyer:** anyone whose learners have outgrown blocks and stall on text. This is the highest-attrition moment in a coding curriculum and almost nothing addresses it — the tooling either keeps learners in blocks forever or drops them into a bare editor.

```
learner in a Blockly workspace
  └── TutoriaLLM/TutoriaLLM (MIT, 1,068 B, `main`, 303★, pushed 2026-11-03)  🇯🇵 APAC
        the ONLY permissive agent this base has found that watches the BLOCK
        WORKSPACE and guides inside it, rather than chatting beside it
        └── self-hosted; bring your own model via the LMS-side gateway
  │
  ├── progression step 1 — show the text:  leopard-js/leopard (MIT, 1,200 B, `master`, 168★)
  │     converts an existing Scratch project to READABLE JavaScript
  │     → the learner sees THEIR OWN project as code: the single best motivator available
  ├── progression step 2 — write the text: aspizu/goboscript (MIT + BSD-3-Clause subtree, `main`, 577★)
  │     a text language that COMPILES BACK to .sb3, so the project keeps running
  │     → and it is now in git: diffable, reviewable, assignable
  └── progression step 3 — run it fast:   forkphorus/forkphorus (MIT, 1,124 B, `master`, 150★)
        MIT runtime, replaces AGPL-3.0 scratch-vm (T40)

  evidence out → lrsql (Apache-2.0) over xAPI; grading → P19 (Artemis, MIT)
```

**Weeks 1–2** deploy `TutoriaLLM` self-hosted against the client's model endpoint and encode two lessons; measure where learners actually stall before changing anything. **Weeks 3–4** wire the `leopard` conversion as a *lesson step* — "here is your project as JavaScript" — not as an export button nobody clicks. **Weeks 5–6** `goboscript` for the first text-authored assignment, committed to git, so the CS faculty can review code rather than screenshots. **Weeks 7–8** optional: `forkphorus` as the runtime and xAPI telemetry on the block→text transition itself, which is the metric the client has never had.

🟢 **Licence position: MIT throughout.** ⚠️ **`goboscript` carries a conjunctive grant** — MIT for the project plus **BSD-3-Clause** scoped to `tools/sb3_definitions.json` and `tools/sb3_schema.json` (p382 subtree class). Both are permissive and the BSD attribution obligation is narrow, but it must appear in the client's notices. ⚠️ **The second copyright line in that payload reads "Massachusetts Institute of Technology" — the institution, not the licence.** Do not let it be transcribed as "MIT" in an SBOM; it is the BSD-3-Clause grant on the Scratch schema files.

⚠️ **Risk.** `TutoriaLLM` is 303 ★ with a small maintainer base and a Japanese-first community; it is MIT and self-hosted, so the downside is maintenance, not lock-in. If the client cannot accept that, the fallback is P4's tutoring stack plus a hand-built `leopard` step — more work, no agent in the workspace.

## P24 — The learner-owned study graph, driven by a local model, evidenced to the institution (5–7 weeks) 🟢 new at p659

**Who buys it:** universities and professional-certification bodies that want a study/revision tool for enrolled learners but cannot send course materials or learner performance to a third-party API — the EMEA sovereignty buyer, the LATAM public-sector buyer, and any APAC client inside South Korea's or Vietnam's assessment rules.

**What makes it buildable now:** p659 verified `OPTIMETA/PAIDEIA-mcp` (MIT) — the study engine behind `PAIDEIA` as a **standalone local MCP server**, with no dependency on any vendor's agent runtime. That is the piece that turns a consumer plugin (**T41**) into something an institution can host. It is the same move **P6** made for retention, one layer up.

```
THE LEARNER'S OWN COURSE MATERIALS  (lecture PDFs, scanned problem sets, past papers)
  │   ingest, on the institution's hardware — nothing leaves the building
  ├── Tesseract OCR                       → scanned/handwritten problem sets
  └── Qwen3-VL via ollama/ollama (MIT, 1,058 B payload read p659)  → figures, diagrams, equations
       │
       ▼
  OPTIMETA/PAIDEIA-mcp  (MIT, 1,068 B payload read p659, local MCP server)
       │   builds the per-course study graph: error patterns, homework-density weighting,
       │   strategy grading, cheatsheet — emitted as Markdown/LaTeX FILES, not rows in a vendor DB
       │
       ├── scheduling layer — do NOT reimplement it:
       │     open-spaced-repetition/fsrs-rs (BSD-3-Clause)  → the retention primitive, per T13
       │
       ├── model layer, client-controlled:
       │     ollama/ollama (MIT) serving an open-weight model on the client's own GPU
       │     ⚠️ no API key anywhere in this diagram — that is the deliverable, not a constraint
       │
       ▼
  THE EVIDENCE SPINE  (P17 — this is what makes it an institutional sale, not a download)
       ├── in:  dmitry-viskov/pylti1.3 (MIT) → LTI 1.3 launch from Moodle / Canvas / Brightspace /
       │        Open edX / OpenOlat. An LTI tool is a SEPARATE WORK: GPL-3.0 Moodle and AGPL-3.0
       │        Open edX impose nothing on your code.
       └── out: yetanalytics/lrsql (Apache-2.0) → xAPI statements into the institution's OWN LRS
                (adlnet/ADL_LRS, Apache-2.0, is the alternative)
       │
       ▼
  YOUR LAYER  (proprietary, closed — every dependency above is MIT / Apache-2.0 / BSD-3-Clause)
       course-pack onboarding, cohort dashboards, faculty review of generated material
```

**Weeks 1–2.** Stand up `PAIDEIA-mcp` against `ollama` on the client's hardware with one real course's materials. The acceptance test is adversarial and worth writing into the SOW: **pull the network cable and the system still works.** If it does not, something is calling out and the sovereignty claim is void.

**Weeks 3–4.** Wire `fsrs-rs` for scheduling and the LTI 1.3 launch, so the tool opens from inside the LMS the learners already use. No fork of the LMS at any point.

**Weeks 5–7.** The xAPI spine into the client's own LRS, and the faculty review surface — a human signs off generated study material before a cohort sees it.

🔵 **Why the licence stack is the sellable part.** Every component is MIT, Apache-2.0 or BSD-3-Clause, verified by first-hand payload read: `PAIDEIA-mcp` MIT, `ollama` MIT, `fsrs-rs` BSD-3-Clause, `pylti1.3` MIT, `lrsql` Apache-2.0. **Your layer can be closed and client-branded**, and nothing in the graph forces disclosure. Contrast **P2** and **P3**, where the copyleft LMS has to be held at arm's length by construction.

🔴 **Three things this pattern must not be sold as.**
1. **Not an assessment system.** The moment its output becomes the official basis for a grade or a ranking it is **Annex III high-risk** in the EU (2 December 2027), **high-impact** under South Korea's AI Basic Act, and inside Vietnam's `Decision 33/2026/QD-TTg` list. Keeping it demonstrably *formative* — a study aid the learner drives, never a system of record — is an **architecture deliverable**, and `intel/market.md` APAC says why that scoping line is itself billable.
2. **Not a proctoring or monitoring tool.** Nothing here watches a learner. Keep it that way: exam monitoring is high-risk and emotion recognition in schools has been prohibited in the EU since February 2025.
3. **Not evidence of adoption.** `PAIDEIA-mcp` carries `2` stars. It is a 2026 repository with one author and a single push on its creation date (`2026-06-14`). 🔴 **Pin the commit, read the code before it goes near a client, and budget for maintaining it yourself** — this is an adopt-and-harden of a small codebase, which is the honest framing, and the same caution `agents/top.md` attaches to every low-star row.

## P53 — The LTI assistant builder, rebuilt permissive (EMEA higher education, before the Dec 2027 Annex III date: 8–10 weeks) 🟢 new at p679

**The case this answers.** A European university wants what `Lamb-Project/lamb` demonstrates — academics building their own course-grounded AI assistants, delivered *inside* Moodle rather than beside it — but Globant must ship a closed derivative, and LAMB is **GPL-3.0**. So LAMB is the **reference design, not the codebase**. Read it to copy the shape; build on permissive parts.

**What to take from the reference, explicitly.** Four design decisions that are the valuable part and are not themselves licensable: (1) the assistant is **course-scoped**, grounded in that course's own materials, not a campus-wide chatbot; (2) delivery is over **IMS LTI 1.3**, so the assistant inherits the LMS's identity, roster and gradebook context and the institution adds no new user directory; (3) assistants are **exportable as JSON**, which is what makes a catalogue portable between departments and institutions; (4) the **teacher authors and tests before publishing** — the approval gate is in the product, not in a policy document.

**Wiring, permissive end to end.**
1. **LTI launch + identity** — `dmitry-viskov/pylti1.3` (MIT) for the 1.3 handshake, or `jupyterhub/ltiauthenticator` (BSD-3) where the target is a notebook estate. The LMS stays unforked; this is the single most important licence decision in the pattern.
2. **Assistant definition as data** — a JSON schema per assistant (persona, grounding corpus pointer, retrieval policy, refusal rules, rubric if it assesses). Version these in the client's own repository; they are the deliverable the institution keeps.
3. **Grounding** — course materials into a vector store; where the client is in a jurisdiction with a published curriculum, ground against the standard rather than only the slides.
4. **Tutoring behaviour** — adopt `braiinz94/braiinz-education` (Apache-2.0, EMEA-placed, French-curriculum aligned): it already separates a **Socratic tutor** from a **practice coach** from a **diagnostician**, which maps onto three assistant types rather than one prompt.
5. **Evidence out** — xAPI statements per interaction into an LRS (`yetanalytics/lrsql`), so the conformity file writes itself.

**Why the date matters.** Annex III stand-alone obligations move to **2027-12-02**. An assistant that only *tutors* is not high-risk; the moment it influences admission or assessment it is. Build the tutoring catalogue now, keep the assessment path behind the same LTI surface, and the high-risk conformity work lands as a scoped follow-on rather than a re-architecture. 🔴 **Do not** fork Moodle, and do not vendor any LAMB source into the deliverable.

## P54 — Grounded tutoring with a *published* hallucination number (LATAM ministries, Brazilian networks: 6–8 weeks) 🟢 new at p679

**The case this answers.** UNESCO IESALC measured **87%** of LATAM higher-education institutions using AI with only **26%** holding any formal framework, and Cetic.br measured **53%** of Brazilian school administrators using AI against **22%** with guidelines. The buyer's real question is therefore not "can you build a tutor" but **"can you prove it does not invent the curriculum"**. For Brazil, that question is now answerable with a number instead of an assurance — which no other region in this base can match.

**The stack, all permissive, all one family.**
1. **Curriculum as data** — `bncc-dev/bncc-dados` (MIT code / CC BY 4.0 data): **1,721** learning objectives (1,580 across the three stages of basic education + **141** from the Computing complement, *Parecer CNE/CEB 2/2022*), each carrying competencies, organisation context and **provenance including a PDF locator** back to the official document. The provenance field is the audit trail; do not strip it.
2. **Agent access** — `bncc-dev/bncc-pacotes`: `npx -y @bncc/mcp` gives any MCP-speaking agent the curriculum as tools, with `@bncc/dados` (npm) and `bncc` (PyPI) for direct use. A hosted MCP endpoint exists at `mcp.bncc.dev` over streamable HTTP with no API key — **use it for the pilot, self-host it for production**, because a ministry deliverable should not depend on someone else's uptime.
3. **Grounding discipline** — the tutor resolves every curriculum claim through the MCP tool and **cites the objective code**; ungrounded curriculum assertions are refused rather than paraphrased.
4. **The proof** — `bncc-dev/bncc-benchmark` (MIT + CC BY 4.0). Run your configuration against it and report **two** numbers, not one: **text fidelity** (the published round spans **88% → 3%** across 19 models) and **fake-code acceptance** (a mid-table model still accepted **10%**). Report the ungrounded baseline beside the grounded result — the delta is the engineering value, and it is the slide that closes the governance conversation.
5. **Governance wrapper** — because only 22–26% of these institutions have a framework, bundle the policy artefacts (acceptable-use, data boundary, human-review rule, incident path) with the benchmark output as the evidence appendix. **Sell this first**; it is what the buyer lacks.

**Delivery notes.** Pair with `GuilhermeScarpini/agente-bncc-professores` (MIT, LATAM-placed) for the teacher-side generator, and note that `THU-MAIC/OpenMAIC` ships **Portuguese (Brazil)** and **Spanish (Mexico)** locales, so an APAC-built classroom platform is a legitimate delivery vehicle in the region. 🔴 **Compliance:** `bncc-pacotes`' licence carves the **name and visual identity** out of the grant — a Globant derivative must not present itself as `bncc.dev`, and the canonical mark is declared in a repository (`bncc-dev/bncc-site`) that is **not public**, so get the attribution wording agreed in writing rather than inferred. 🔴 **Scope honestly:** this pattern is **Brazil-specific**. No equivalent curriculum-plus-benchmark stack exists for Mexico, Colombia, Chile or Argentina in this base — for those, P26 becomes "build layer 1 first", which is a different and longer engagement.

## P64 — Grading assistance that *cannot* post a grade on its own (EMEA higher education before the Dec 2027 Annex III date; North America districts under FERPA: 5–7 weeks) 🟢 new at p688

**The problem this solves.** Annex III of the EU AI Act names *evaluation of learning outcomes* as high risk, and both it and US state guidance discharge on evidence that a human decided. Most AI-grading pilots produce a grade and a promise. This one produces a grade, a staged artefact, and an audit trail — by construction.

**The stack, every component permissive:**

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| Grading surface | [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp) | 🟢 **MIT** (`1,076 B`, `2bcdae923d26`) | `12` read-only / `4` local-only / **`3` Canvas writers, each requiring `confirm=true`**; grades staged on the grader's disk; anonymous and moderated assignments read-only by construction |
| Course surface (breadth) | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** | ~102–128 tools plus agent skills; use it for everything *except* the grade write |
| Learner-side mirror | [`AnonymousOnyx22/canvas-lms-student-mcp`](https://github.com/AnonymousOnyx22/canvas-lms-student-mcp) | 🟢 **MIT** (`1,072 B`, `ed912ca72d9e`) | `21` tools, `20` read-only; the exception writes an `.ics` on the learner's own machine. Gives the pilot a learner view with **zero** write surface into the institution |
| Evidence spine | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | xAPI Learning Record Store; one statement per `stage_grade` → `post_staged_grades` transition **is** the human-decision record |
| Mastery layer (optional) | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** | Bayesian Knowledge Tracing and a frozen rubric behind one tool surface, if the client wants per-skill rather than per-assignment judgement |

**Wiring.** One MCP client (Claude Code / Cursor / Codex) mounts `canvas-grader-mcp` **and** `canvas-mcp`; the grader server holds the only Canvas write path. A thin adapter subscribes to the grader's staging directory and emits two xAPI statements to `lrsql` — `proposed` when a grade is staged, `confirmed` with the actor identity when `post_staged_grades` runs with `confirm=true`. Per-course grading guidelines live in `set_grading_guidelines`, on the grader's machine, never in the model's context by default.

**Weeks.** `1` Canvas token scoping + read-only verification against a sandbox course · `2` grader mount, rubric ingest, staging review with two real graders · `3` `lrsql` + adapter, statement schema agreed with the institution's data office · `4` pilot on one course, every posted grade traced end to end · `5` exception handling (anonymous/moderated assignments, late policy, regrades) · `6–7` second faculty, documentation pack.

🔴 **Say this out loud in the room, because the README does:** confirmation gating is an **authority** control, not a **data** control. Student work still reaches the model behind the client. The data half is a hosting decision — self-hosted weights, or a contracted provider with the institution's DPA — and it is **not** solved by this pattern. A conformity story needs both halves; selling one as both is how a pilot fails its first audit.

🟢 **Licence position:** MIT + MIT + MIT + Apache-2.0. **A closed, client-branded derivative is permitted end to end**, which is what makes this resellable rather than a one-off.

## P65 — Integrating with a state-operated platform across an AGPL boundary (German Länder, EMEA public sector: 8–10 weeks) 🟢 new at p688

**The problem this solves.** A German state already runs [`AIS.chat`](https://github.com/FWU-DE/ais-chat) (formerly `telli`) — FWU, DigitalPakt Schule, 16 Bundesländer, 12 live as of 09/2026. The instinct is to fork it. **The grant forbids that commercially:** AGPL-3.0 (`34,523 B`, `8486a10c4393`), and network use is distribution, so a hosted state-branded fork owes modified source to teachers and pupils.

**The motion is therefore beside it, not inside it:**

1. **Leave `ais-chat` unforked.** It is the chat surface the Land already procured and operates. Integrate; do not vendor it into your tree.
2. **Build the layers it does not have, as separate services with documented interfaces** — curriculum alignment, assessment, analytics, LMS bridging. Keep every line of this out of the AGPL source tree so the obligation does not reach it.
3. **Bridge to the school-side systems with permissive components already on this shelf:** [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) (MIT, Rust, 22 tools, assignments read *and* submit) for Moodle states; [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (🟢 Apache-2.0, `449★`) where a permissive institutional LMS is in play — and note `gh api` still reports its SPDX as `NOASSERTION` while the payload is byte-exact Apache-2.0, so read the payload in the client's due-diligence pack.
4. **Use the state's own vocabulary.** NRW's **KIMADU** programme (University of Siegen) splits didactic agents into **`Lehrpartner`** (teacher-side planning) and **`Lernpartner`** (pupil-side), with a **`KRAFT+` meta-agent** for teachers. That taxonomy maps one-to-one onto the shelf: `canvas-grader-mcp`/`moodle-mcp` are `Lehrpartner`, `canvas-lms-student-mcp`/`moodle-student-mcp` are `Lernpartner`. **Proposing in the client's own terms is free and it lands.**
5. **Price the procurement correctly.** Six Länder signed a framework worth **up to €67.5M** for the open-source **KoDaS** platform. This is not a pilot-sized buyer, and the comparable is an infrastructure programme, not a tool licence.

**Weeks.** `1–2` read the AGPL boundary with counsel; write down exactly which repositories are touched and which are not · `3–4` interface contract with the Land's operator (auth, logging, data residency; `F13`-style BITBW-operated hosting is the regional precedent) · `5–7` build the adjacent service · `8` licence-hygiene review: dependency graph, not just the top-level repo — `T16`'s rule applies, and `OpenMAIC`'s LGPL-3.0 `mathml2omml` workspace package is the standing example of how a permissive headline hides a copyleft leaf · `9–10` conformity documentation and handover.

🔵 **Why this pattern generalises beyond Germany.** Finland's `Opetushallitus` family is **EUPL-1.1/1.2**, Germany's is **AGPL-3.0**: European public education infrastructure is converging on reciprocal licences, not permissive ones. **"Integrate across a licence boundary" is becoming the default EMEA public-sector shape**, and the studios that can state the boundary precisely will win work from the ones that fork first and read the grant later.


## Choosing a pattern

| Client situation | Pattern | Why |
|---|---|---|
| Already on Canvas | **P1** | No migration, no licence exposure, fastest demo |
| Already on Moodle (LATAM/EMEA) | **P2** | Meets the dominant installed base; local models for residency |
| MOOC / corporate academy on Open edX | **P3** | Only licence-safe Open edX shape |
| Wants explainable mastery (STEM) | **P4** | BKT + pyKT; budget content authoring |
| Uses AI already, controls nothing | **P5** | Sell governance first, then P1–P4 |
| Pilot must prove an outcome | **P6** | Permissive end to end, retention measurable, no per-review inference cost. Attach it to any other pattern |
| Ministry/district wants its OWN branded coding platform | **P22** | MIT end to end, offline-capable, closed derivative permitted |
| Learners stall moving from blocks to text | **P23** | The one permissive agent that works inside the block workspace |
| Connectivity cannot be assumed | **P7** | The only pattern with no copyleft component anywhere, and the only one that works offline |
| Needs a full education ERP (finance, HR) | **P2 + OpenEduCat** | `openeducat/openeducat_erp` (LGPL-3.0, 905★) on Odoo. ⚠️ default branch is `19.0` and `20.0` exists — resolve it |
| Already on Moodle and wants a **real agent**, not just REST glue | **P8** | Names the bridge P2 left as a placeholder. `G36maid/moodle-mcp` (MIT, 27★) — adopt and harden; **price the hardening, it is not P1** |
| Data residency, offline, **or** must stay off the graded system of record (Korea, Vietnam) | **P9** | Curriculum knowledge in the weights, FP8 on one GPU, no egress. 🔴 Resolve the OmniEdu weight licence first |
| Has a funded AI-literacy mandate (Canada, Saudi, Kenya, EU Art. 4) | **P10** | The deliverable is curriculum and teacher capacity, not software. MIT base at 41.1k★ permits a closed client derivative |
| 🟢 **Choosing a platform rather than extending one** — new faculty, national programme, migration off a commercial LMS | **P11** | The only pattern whose institutional platform is itself permissive. Apache-2.0 course management, `langchain4j` already in-tree. ⚠ Specify PostgreSQL, not MySQL; price the Java skill-set |
| 🟢 **Wants to own a reference integration rather than rent one** | **P12** | OpenOlat has **no** agent bridge at any address. No incumbent, no copyleft to route around, agent can live in-tree, and the result is contributable upstream under Apache-2.0 |
| 🟢 **Needs grading or written-feedback at scale** | **P13** | The only pattern where the production artefact does not exist yet. Permissive, education-specific, peer-reviewed *research* supply (ArguLens) + calibration to the client's own markers (`LLM-Rubric`) + an approval gate. ⚠ Assistive scoring with human sign-off only — never autonomous grading |
| 🟢 **Has an incumbent LMS and must prove the pilot worked** — i.e. almost every engagement | **P17** | The layer under all the others: LTI 1.3 in (no fork, no copyleft inherited), xAPI out to an Apache-2.0 LRS. **Attach it to any pattern above.** 🔴 `yetanalytics/lrsql` is the only live permissive LRS — scope that dependency explicitly |
| 🟢 **Must meet the April 2026 US ADA accessibility deadline** | **not a product** | `ucfopen/UDOIT` (GPL-3.0) is the only real tool and there is **no permissive alternative**. Client-operated deployment, bill the remediation, ship no derivative. See `intel/market.md` → North America |

## 🔴 What these patterns deliberately avoid

- **No pattern forks a GPL or AGPL platform.** 🔴 **Count corrected at p656: fifteen of twenty-six** verified platforms on `verticals/solutions.md` are copyleft (this line previously read "ten of fourteen", stale since p655 and again after p656 shelved the H5P, Adapt, UDOIT, TAO and Learning Locker rows); forking one for a managed service is the single most expensive mistake available in this industry. **P7 is the exception that proves the rule** — it can own its platform layer precisely because Kolibri is MIT.
- 🟢 **Two exclusions from the previous version of this list are withdrawn.**
  - `OpenEduCat` was excluded as **HTTP 404**. The project is live at **`openeducat/openeducat_erp`** (LGPL-3.0, 905★, default branch `19.0`); only the published address was dead. It is now the recommended base when a client needs a full education ERP, and LGPL-3.0 is a better licensing position than the `frappe/lms` (AGPL-3.0) substitute that was recommended in its place.
  - `tutor-mcp` was excluded at **0 stars**. That measured `kvnloo/tutor-mcp`, which is a **fork**; the upstream `ArnaudGuiovanna/tutor-mcp` has **96★ / 13 forks** and is the backbone of **P6**.
- **Still excluded:** `awesome-ai-llm4education` (**no licence**, 221★) and `eduadapt-ai` (**no licence**, 26★), both previously published here as MIT and neither of which is. Added to the exclusion list at p651: `GarethManning/education-agent-skills` (949★ but **CC BY-SA 4.0** — ShareAlike, so a derivative skill library cannot be proprietary); `virtualryder/edu-ai-agents` (4★ and a **modified MIT payload with the limitation-of-liability paragraph removed**); `mthatipamula/educational-assessment-ai-agent-platform`, `luffycodes/Tutorbot-Spock` and `Micel357/Edu-mentor-AI` (**no licence file**); `CodeBreez/collejo` (MIT but **archived read-only since 2024-05-16**).
- **No pattern includes proctoring or emotion recognition.** Emotion recognition in schools is banned in the EU; exam monitoring is high-risk there and, since 22 January 2026, student assessment in K-12 is high-impact under South Korea's AI Basic Act with fines expected from around January 2027. No permissively-licensed open source option was found in any case.

## 🔴 Resolve the licence of the *tree*, not the repository — five live cases

Reading `LICENSE` is necessary and not sufficient. Four components these patterns use carry obligations their repository badge does not mention; the fifth row is the case where the manifest read came back **clean**, which is the result that makes a pattern scopeable. All five were read from bytes or from a manifest field verbatim on 2026-11-04.

| Component | Badge | Actual obligation in the tree | What to do in a pattern |
|---|---|---|---|
| **OpenMAIC** (P10, P3) | MIT | `packages/mathml2omml` is **LGPL-3.0-or-later** (7,652 B), `"workspace:*"` in the root manifest, built as step one of `build:packages` | Keep it dynamically replaceable with source offered, or excise the MathML→OOXML export path. Design-time decision |
| **OmniEdu weights** (P9) | Apache-2.0 *(code)* | **No named grant for the weights.** README: *"Model weights and third-party datasets and benchmarks retain their respective licenses."* Backbones are Qwen | Read the Hugging Face card before scoping. Gate zero of P9 |
| **open-moodle** (not used) | MIT | Depends on **PyMuPDF (AGPL-3.0)** | Excluded from P8 for this reason. An AGPL dependency in a network-served agent defeats out-of-tree containment |
| 🟢 **OpenOlat** (P11, P12) | Apache-2.0 | **Clean, and verified rather than assumed.** 270 declared dependencies contain exactly one copyleft item: the *optional* **MySQL Connector/J** (GPL-2.0 + Universal FOSS Exception), whose exception covers OSI-approved open source licences but **not** a closed derivative. Verified absent: iText (AGPL-3.0), JasperReports (LGPL). Hibernate 7.4.14 / validator 9.1.6 are Apache-2.0 eras, not the old LGPL-2.1 Hibernate | **Specify PostgreSQL JDBC 42.7.14 (BSD-2-Clause), already a first-class in-tree backend.** One line in the architecture document and the tree is permissive end to end. This is the whole cost of the only clean copyleft exit on this shelf |
| **csmediapro/moodle-mcp-server** (not used) | "free use, no closed-source repackaging" | Plain **AGPL-3.0**, 34,523 B, plus paid Premium Plugins | Excluded from P8. Marketing language is not a licence; read the payload |

**The check to run once per engagement, in week one:** read `LICENSE` from bytes; then read `package.json`, `pyproject.toml` and `Cargo.toml` for every bundled or workspace component; then, for any model, read the weight card separately from the code licence. Five of the **six** grant-defect classes this KB has catalogued pass a licence-badge check. The sixth — *grant by reference*, where the Apache-2.0 notice stands in for the terms, as in `wwrwbs/AI_AWE` (P13) — **fails** the badge check and is nonetheless usable, so a short grant file is a reason to read it rather than to reject the project.

## 🔴 Resolve the branch before you clone — five live cases on this shelf

Every pattern above assumes you check out the right thing, and on this shelf the default branch is frequently not it:

| Repo | Default branch | What goes wrong |
|---|---|---|
| `openeducat/openeducat_erp` | **`19.0`** | A hardcoded `main`/`master` builds nothing; a hardcoded `19.0` silently keeps building the old major, because `20.0` already exists |
| `francoisjacquet/rosariosis` | **`mobile`** | A default clone gives you the mobile branch, not the release line, among 44 branches that are otherwise version numbers |
| `learningequality/kolibri` | **`develop`** | A default clone gives you development code; deploy from `release-v0.19.x` or `release-v0.20.x` |
| `OpenOLAT/OpenOLAT` | `master` | `master` is the development trunk, not a release. **Deploy from `OpenOLAT_21.1`** (latest tag `OpenOLAT_21.1.2`); live release branches run `OpenOLAT_18.0` → `OpenOLAT_21.1`. The naming is `OpenOLAT_<major>.<minor>` — note the all-caps prefix, which differs from the repository's own mixed-case `OpenOlat` branding and from the `OpenOlat_20.0.pre2` tag, so a generated branch name will not match |
| `GeminiLight/gen-mentor` | `main`, and that is the problem | `main` is a browser-only Next.js demo app. **The multi-agent Python implementation its WWW '25 paper describes is on branch `v0.1-demo`** — so the default gives you a demo, not the evaluated system |

The fix is one command, and it belongs in any ingest or deployment script rather than in a human's memory:

```bash
git ls-remote --symref https://github.com/<owner>/<repo> HEAD   # returns the real default branch
```

Then read the README for which branch carries the artefact you actually want — resolving the default is necessary and, as `gen-mentor` shows, not always sufficient.

## P25 — Early-years computational thinking with no device budget and no copyleft (6–8 weeks) 🟢 new at p660

**The engagement this answers.** A ministry, a school network or a foundation wants computational thinking for ages 5–10, at system scale, on hardware that does not exist yet, and wants a derivative it can brand and operate. Every earlier pattern on this page assumed either a device per learner or an AGPL platform. This one assumes neither.

**Why it is new at p660.** Until this pass the base held that the Scratch family's only permissive surfaces were `scratch-blocks` and `forkphorus` — components, not a product. Org enumeration found **ScratchJr under BSD-3-Clause** and a **live, MIT, browser-only micro:bit stack**. Those two facts together make a permissive early-years programme buildable for the first time in this KB.

```
          ┌─────────────────────── LEARNER SURFACE — pick ONE by age ───────────────────────┐
  ages 5–7   scratchfoundation/scratchjr        BSD-3-Clause  1,508 B  707★  `develop`
             └─ 🔴 dormant since 2022-07-22 → FORK AND OWN; budget the maintenance line
  ages 8–10  microbit-foundation/python-editor-v3   MIT  1,083 B  84★  `main`  (pushed 2026-11-04)
             └─ microbit-foundation/micropython-microbit-v2-simulator  MIT  1,117 B  21★
                └─ 🟢 THE BOARD RUNS IN THE BROWSER — zero hardware per learner
          └────────────────────────────────────────────────────────────────────────────────┘
                                   │  project files (.sb / .hex / .py)
                                   ▼
  ┌──────────────── ASSESSMENT — grades the ARTEFACT, not the prose ────────────────┐
    scratchfoundation/scratch-analysis   BSD-3-Clause  1,520 B  36★  `develop`
      structure · composition · complexity  →  your own rubric weights (closed, BSD permits it)
    microbit-foundation/cctd-ml-machine   MIT  1,126 B  10★   AI-literacy module:
      learner trains a gesture classifier on sensor data = "what is a model", by building one
  └─────────────────────────────────────────────────────────────────────────────────┘
                                   │  scores + evidence
                                   ▼
  ┌──────────────── PLUMBING — all permissive, all already on this base ────────────┐
    ollama/ollama        MIT  1,058 B   local model: feedback in-country, no per-seat API cost
    pylti1.3             LTI 1.3 launch from the client's existing LMS (Moodle stays stock)
    yetanalytics/lrsql   xAPI statements → the learning record the ministry reports on
  └─────────────────────────────────────────────────────────────────────────────────┘
```

**Licence boundary — the whole point of the pattern.** Every component above is BSD-3-Clause, MIT or Apache-2.0. There is **no GPL and no AGPL anywhere in the chain**, so the derivative can be closed, branded and sold as a managed service. Contrast the obvious-looking alternative: building on `scratch-gui` (AGPL-3.0) means hosting it as a service triggers network copyleft over your modifications, and building on `Scratch_1.4` drags in GPL-2.0 **plus** a runtime attribution obligation in the `Help > About` dialog (**T42**).

🔴 **Do not put the curriculum in scope on these terms.** `RaspberryPiFoundation/scratch-curriculum` is the natural lesson material and it is **CC BY-NC-SA 4.0** — NonCommercial, so it cannot be shipped in a paid programme at all (**T42**). Either license it separately and directly from the Raspberry Pi Foundation, or author lessons as a billable deliverable. The permissive content exception is `scratchfoundation/scratchjr-website` (BSD-3-Clause, live to 2026-08-20), which is a genuinely reusable starting point for teacher-facing material.

**Sequence.**
- **Weeks 1–2** — Fork ScratchJr, stand the simulator stack up behind the client's LMS via `pylti1.3`, and get one class of each age band producing project files. Do not build assessment yet; find out what learners actually make first.
- **Weeks 3–4** — Wire `scratch-analysis` over the collected projects and calibrate rubric weights against teacher judgement on a sample. This is where the value is: the complexity metrics are off-the-shelf, the weighting is the client's pedagogy and is yours to keep.
- **Weeks 5–6** — Add `cctd-ml-machine` as the AI-literacy unit and emit xAPI to `lrsql`, so the programme reports against the AI-literacy mandates this KB tracks (`intel/market.md`, North America and EMEA legs) rather than against seat counts.
- **Weeks 7–8 (conditional)** — Local-model feedback via `ollama` only if the client has a data-residency requirement; otherwise skip it and save the inference engineering.

**What to tell the client up front.** The ScratchJr fork is **four years cold**. That is not a defect for a fork-and-own engagement — it means the upstream will not surprise you — but it does mean there is no community fixing iOS/Android build breakage for you, and that maintenance line must be in the price. The micro:bit half is the opposite: pushed yesterday, so it needs tracking rather than owning. Scoping the two halves the same way is the mistake this pattern exists to prevent.

## P26 — Accessibility remediation where three quarters of it can be a closed product (institutions under the April 2026 US ADA deadline: 8–12 weeks) 🟢 new at p661

**The engagement this answers.** A large US public university or community-college system is under the **April 2026 ADA Title II** obligation and has a backlog of inaccessible course content: thousands of hours of uncaptioned lecture video, mathematics rendered as images, and HTML course pages that have never been audited. Until p661 this base answered that engagement with *"there is no permissive supply — sell services, ship no derivative"* (`intel/trends.md` **T29**). **That answer was wrong for three quarters of the work.**

**Why it is new at p661.** T29's blanket claim was withdrawn when the mandate was decomposed into the capabilities it actually creates. Three of four have production-grade permissive answers that this base had measured in its own logs and never shelved — `openai/whisper` is **MIT at `111,975★`** and is named in both append-only logs as *"the ASR baseline"*. Only the fourth is copyleft-locked. **The licence boundary runs between capabilities, not around the engagement**, and that is what makes a product possible here for the first time.

```
  BACKLOG IN  ─────────────────────────────────────────────────────────────────────
   lecture video · recorded lectures · podcasts         course HTML · PDFs · math
         │                                                       │
         ▼                                                       ▼
  ┌──── 🟢 PERMISSIVE — CLOSED DERIVATIVE PERMITTED ────────────────────────────┐
  │                                                                             │
  │  CAPTIONING  (biggest piece of the work by volume)                          │
  │    openai/whisper            MIT   1,063 B   111,975★   `main`              │
  │      └─ self-host: no per-minute vendor fee, no student audio leaving        │
  │         the estate → the data-residency answer sells this on its own        │
  │                                                                             │
  │  MATHEMATICS                                                                │
  │    NSoiffer/MathCAT          MIT   1,065 B   ★ unmeasured   `main`          │
  │      └─ MathML → speech (15 languages) + braille (Nemeth, UEB, CMU)         │
  │         + structural navigation · DAISY-sourced                             │
  │      └─ 🔴 needs MathML IN, so OCR/authoring is YOUR integration work       │
  │                                                                             │
  │  AUDIT / TRIAGE / REPORTING                                                 │
  │    GoogleChrome/lighthouse   Apache-2.0   11,358 B   31,019★   `main`       │
  │      └─ runs LOCALLY, nothing leaves the machine → quotable under an        │
  │         EMEA/LATAM data-residency clause as well as a US one                │
  │      └─ audits only; produces the WORKLIST, performs no repair              │
  │                                                                             │
  │   ⇒ wrap these three behind ONE MCP surface + a queue. This is the          │
  │     BRANDED, CLOSED DELIVERABLE. MIT and Apache-2.0 both permit it.         │
  └─────────────────────────────────────────────────────────────────────────────┘
         │  worklist: defect → file → owner → status
         ▼
  ┌──── 🔴 COPYLEFT — DEPLOY, DO NOT DERIVE ───────────────────────────────────┐
  │  IN-PLACE WCAG REPAIR INSIDE THE LMS COURSE                                │
  │    ucfopen/UDOIT   GPL-3.0   35,147 B   117★   `main`   (pushed 2026-11-04)│
  │      └─ scans Canvas content, explains defects, fixes many in place        │
  │      └─ STILL THE ONLY PRODUCTION TOOL. Run it inside the client's own     │
  │         estate, unmodified. Bill the remediation and the integration.      │
  │         Ship NO derivative of this component.                             │
  └────────────────────────────────────────────────────────────────────────────┘
         │  evidence of remediation
         ▼
  yetanalytics/lrsql   Apache-2.0   144★   ← xAPI statements per remediated asset
      (the evidence spine from P17 — reuse it, do not build a second one)
```

**Wiring, concretely.**

1. **Triage first, because it sizes the contract.** Run `lighthouse` headless across the course estate's public HTML and emit one row per defect. This is a worklist, not a fix, and it is the only step that tells the client how big the backlog is. Lighthouse is Apache-2.0, so the triage dashboard is yours.
2. **Captioning queue.** Self-host `whisper`, feed it the video backlog, emit WebVTT. Two commercial arguments, both stronger than the technical one: there is **no per-minute vendor fee** at estate scale, and **no student audio leaves the institution**, which is the clause that kills most SaaS captioning bids in public-sector procurement. Human review of the output is a billable line, not a defect — budget it explicitly.
3. **Mathematics path.** Route MathML through `MathCAT` for speech and braille. 🔴 **Scope this honestly:** MathCAT needs MathML as input, so if the client's maths is page images the conversion step is *your* work and is the larger half of the task. Do not price this alongside captioning as if it were the same kind of job.
4. **One MCP surface over all three.** `caption_asset`, `audit_page`, `render_math_accessible`, each returning a status the queue can track. This wrapper plus the triage dashboard **is the product**, and MIT + Apache-2.0 permit it to be closed and client-branded.
5. **UDOIT last, and at arm's length.** Deploy it unmodified in the client's estate for in-place Canvas repair. Do not import it, do not link it, do not fork it into the product tree. It is GPL-3.0 and it is the one component that must stay a deployed tool rather than a dependency.
6. **Evidence out.** Write an xAPI statement per remediated asset into `lrsql` (Apache-2.0), reusing **P17**'s spine rather than building a second one. The institution needs to *show* compliance, not merely achieve it, and a dated statement per asset is the artefact an auditor accepts.

**What to say in the proposal.** *"Most of this programme is a product we can build and brand; the last mile inside Canvas is a tool we deploy and operate for you."* That sentence is the whole value of this pattern, and until p661 this base could not say it.

**🔴 What this pattern does not claim.** The **April 2026 deadline itself is carried from secondary sources** and has never been read in primary form by this base — confirm it against the rule text before it anchors a contract date. `MathCAT`'s adoption is **unmeasured**: three independent channels refused the address at p661 (`gh api search/repositories` `422`, `gh api repos/` `403`, HTML `403`), so its licence and existence are first-hand facts and its popularity is not. And `lighthouse` is a **general-purpose** web auditor, not an education tool — it will flag defects in LMS chrome that the institution does not own, so the worklist needs a scoping filter before anyone is handed it.

## P27 — The licence-provenance gate, as the first two weeks of any education engagement (2 weeks, then a standing gate) 🟢 new at p662

**The engagement this answers.** A studio is about to build on an open source education platform. Procurement will run an SBOM and SPDX scan before anything ships, and the scan will return answers that are *wrong in both directions* on the exact repositories this KB recommends. Somebody has to be able to say, in a review, why a `NOASSERTION` is harmless and why a published comparison table is not. That is a two-week deliverable, and it pays for itself the first time it stops a fork.

**Why it is new at p662.** p658 established licence-truth as a billable deliverable on the `TurboWarp/extensions` case. p662 supplies the specimens that make it a *gate* rather than an audit: a controlled set in which the scanner's verdict is wrong in each direction, with the payload held constant across the pair that matters.

```
  ┌──── 🟢 THE GATE — THREE PERMISSIVE TOOLS, ALL VERIFIED 2026-11-05 ─────────┐
  │                                                                           │
  │  anchore/syft                  Apache-2.0  LICENSE  11,357 B              │
  │    sha256₁₂ c71d239df917   9,832★   `main`   pushed 2026-11-04            │
  │      └─ SBOM generation from images, dirs and archives → SPDX + CycloneDX  │
  │                                                                           │
  │  aboutcode-org/scancode-toolkit  Apache-2.0 + CC-BY-4.0  `develop`        │
  │    apache-2.0.LICENSE  11,357 B  sha256₁₂ c71d239df917   (the CODE)       │
  │    cc-by-4.0.LICENSE   18,651 B  sha256₁₂ 2a82ac9bbc3e   (the licence DB) │
  │    NOTICE 2,333 B      2,662★   pushed 2026-11-02                         │
  │      └─ reads grants out of a SOURCE TREE, which is the axis `syft` misses │
  │      └─ 🔴 DUAL-LICENSED: the tool is Apache-2.0, the licence DATA is      │
  │         CC-BY-4.0. Shipping its output means carrying attribution.        │
  │                                                                           │
  │  CycloneDX/cyclonedx-cli       Apache-2.0  LICENSE  11,341 B              │
  │    sha256₁₂ 6c29f22a4a73   555★   `main`   pushed 2026-10-19              │
  │      └─ convert / merge / diff SBOMs → the format procurement asks for     │
  │      └─ 🔧 p662 corrected this base's own ledger verdict (`unstated`)      │
  └───────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
  ┌──── 🔴 WHAT THE GATE IS FOR: FOUR SPECIMENS, FOUR FAILURE MODES ──────────┐
  │                                                                           │
  │  1. SCANNER SAYS NOASSERTION, GRANT IS CLEAN — filename axis              │
  │     scancode-toolkit    gh api → NOASSERTION                              │
  │     anchore/syft        gh api → Apache-2.0                               │
  │       └─ SAME PAYLOAD. Both 11,357 B, both sha256₁₂ c71d239df917.         │
  │          The only variable is the FILENAME: `apache-2.0.LICENSE`          │
  │          vs `LICENSE`. Controlled specimen for `558-B` / `572-B`.         │
  │                                                                           │
  │  2. SCANNER SAYS NOASSERTION, GRANT IS CLEAN — appended-text axis         │
  │     OpenOLAT/OpenOLAT   LICENSE 10,982 B  sha256₁₂ 6dbc5b605ed0           │
  │       └─ sections 1–9 byte-identical to canonical; APPENDIX removed,      │
  │          two provenance statements appended. Mechanism = `659-F`.         │
  │       └─ 🟢 CONTRAST: cyclonedx-cli FILLED the appendix in place          │
  │          (`Copyright OWASP Foundation`, brackets `{}`) and still          │
  │          classifies Apache-2.0. Completing it is safe; removing it        │
  │          and appending is not.                                           │
  │                                                                           │
  │  3. A PUBLISHED TABLE SAYS MIT, THE REPO SAYS AGPL — the expensive one    │
  │     learnhouse/learnhouse  LICENSE 34,523 B  sha256₁₂ 8486a10c4393        │
  │       └─ AGPL-3.0 on `dev` AND on `main`. gh api agrees. 2,448★.          │
  │       └─ A current LMS comparison puts it under "MIT/Apache …             │
  │          maximum flexibility". Network-use clause, hosted deployment.    │
  │                                                                           │
  │  4. GRANT IS FORMALLY PERFECT AND NAMES NO LICENSOR                       │
  │     lebmatter/exampro  license.txt 1,069 B  sha256₁₂ 002c2696d92b        │
  │       └─ stock MIT whose copyright line is literally                      │
  │          `Copyright (c) [year] [fullname]`. Passes every badge check.    │
  │          Legally unattributable. Catalogued at `p202`, specimen `661-A`. │
  └───────────────────────────────────────────────────────────────────────────┘
```

**Wiring, concretely.**

1. **Resolve the ref before anything else.** `git ls-remote --symref <repo> HEAD`. Four of the repositories named on this page do not default to `main` — `scancode-toolkit` is `develop`, `OpenOLAT` is `master`, `oppia` is `develop`, `learnhouse` is `dev`. A grant read against `/main/` by habit is a grant read of the wrong branch, and specimen **3** — [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) — was nearly missed this way. See *"Resolve the branch before you clone"* above.
2. **Enumerate the filename space, do not trust one probe.** `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENSE.TXT`, `COPYING`, `COPYING.txt`, `LICENCE`, `license`, **and `<spdx-id>.LICENSE`** — that last form is what hid `scancode-toolkit`'s clean Apache grant from a five-filename ladder.
3. **Byte-read and digest every grant.** Record `path`, `bytes`, `sha256₁₂` and the copyright line. A byte count is the cheapest tamper check there is, and it is what distinguishes specimen **2** from a genuine licence change. 🔴 **Name the canonical copy any `−N B` delta is measured against**: `apache/.github` serves Apache-2.0 at `11,357 B` and `apache.org` at `11,358 B`, so an unattributed delta is ambiguous by `1 B` (p662's standing rule).
4. **Run [`anchore/syft`](https://github.com/anchore/syft) for the dependency tree and [`aboutcode-org/scancode-toolkit`](https://github.com/aboutcode-org/scancode-toolkit) for the source tree.** They answer different questions and the gate needs both: `syft` sees declared package metadata, `scancode` sees grants actually present in files. The licence unit is the dependency graph, not the repository — the section above this one has the five live cases.
5. **Normalise to CycloneDX and hand procurement the diff, not the scan.** [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli) converts and *diffs*, so the standing gate is a diff against last release: new grant, changed grant, or disappeared grant. Three states, each with an owner.
6. **Ship the rebuttal file with the SBOM.** One row per `NOASSERTION`, each with the mechanism (filename / appended text / no grant at all), the digest, and the sentence that closes it. This is the artefact that turns a two-week audit into a gate somebody can sign.

**What to say in the proposal.** *"Your scanner will flag the largest permissive LMS in this stack as unlicensed, and it is wrong. It will also pass a platform that a published comparison table calls MIT and which is actually network-copyleft, and that one would have cost you the source of your product. We will give you the evidence for both, in the format your procurement team already reads, and a diff-based gate that keeps answering the question after we leave."*

**🔴 What this pattern does not claim.** It does **not** constitute legal advice and it does **not** resolve clause-level residuals — a dual-licensed component like `scancode-toolkit` carries an attribution obligation that counsel, not a scanner, has to price. The four specimens are verified first-hand at `2026-11-05`; the *generalisation* that scanners err in both directions at a measurable rate is **not** quantified by this pass on a sampled population, and `572-B` is the only rate figure this base holds for the filename axis.

## P28 — Spanish-language tutoring inside Open edX, for a public university that cannot send student data anywhere (LATAM public higher education, rural and regional campuses: 8–10 weeks) 🟢 new at p663

🔵 **Why this pattern exists now.** Until p663 this base had **no placed LATAM agent row at all**, so every LATAM engagement had to be composed from APAC and North American parts and localised. It now has two Colombian rows, and — more usefully — a **worked reference for the hardest part of the job**, which is not the tutor but the *integration*. Open edX is the platform tier this region actually runs, and `LabSirius/TutorIA` is the only agent on this shelf that lands **inside** it.

### The parts

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| Platform | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | **AGPL-3.0** | The incumbent across LATAM public higher education. ⚠️ **Copyleft — it is the host, never the derivative.** You deploy it; you do not fork it into a client-branded product. |
| **Integration reference** | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | **MIT** (1,069 B, © *Grupo Sirius*) | 🟢 **The pattern's keystone.** An **Open edX XBlock/plugin**, so the tutor sits inside the course, enrolment and grading objects instead of talking to them over REST. Built for **rural higher education in Risaralda** at Universidad Tecnológica de Pereira — the same institutional shape as the client. **Read it as an integration reference, do not ship it: `0★`, 4 commits.** |
| Tutor engine | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | Carries the persistent learner model, which `TutorIA` does not. This is the swap that turns the reference into a product. |
| Programming track | [`AndresGuido9820/trabajo2-agente-tutor`](https://github.com/AndresGuido9820/trabajo2-agente-tutor) | **MIT** (1,085 B) | 🟢 **Pyodide in the browser** — learner code runs client-side, so there is **no sandbox to operate or secure**, the single largest hidden cost in a CS tutoring build. Spanish-language and Socratic by construction. `0★` but **151 commits / 314 tests**. |
| Model | Ollama + an open-weight model, on university hardware | — | The binding constraint in this pattern is egress, not capability. |
| Mastery | [`kvnloo/tutor-mcp`](https://github.com/kvnloo/tutor-mcp) | MIT | BKT + FSRS behind one MCP tool surface, so mastery estimates are explainable to a faculty committee. |
| Evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) + [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | **P17**'s spine. Non-negotiable here — see *Why the statement log is the deliverable* below. |

### How it wires together

1. **Weeks 1–2 — run P27 first, and run it on the two Colombian rows specifically.** `TutorIA` ships **two addresses for one work**: its own README's clone command points at the predecessor [`Sof1SP/TutorIA`](https://github.com/Sof1SP/TutorIA), whose grant names **a different licensor** (© *Sofia Soto Parra*, 1,073 B) from the one you are adopting (© *Grupo Sirius*, 1,069 B). **Settle in writing which grant the derivative takes before any code is copied.** This is not pedantry — it is the one defect in this pattern that cannot be fixed later.
2. **Weeks 2–4 — stand up Open edX and lift the XBlock boundary from `TutorIA`.** Take its *shape* — how it registers, where it reads enrolment, how it writes grades, how the teacher statistics panel is mounted — and reimplement against your own MIT code. 🔴 **Keep the AGPL boundary clean:** the XBlock talks to the platform through published extension points, so your plugin stays separately licensed. Nothing you write enters `edx-platform`.
3. **Weeks 4–6 — swap the engine.** `TutorIA`'s backend is FastAPI calling a hosted model API. Replace it with **DeepTutor against local Ollama**. This is the step that converts a 4-commit artefact into something with a persistent learner model and no egress path.
4. **Weeks 5–7 — add the programming track.** Mount `Profe Bit`'s **Pyodide execution model** as the CS course type. Its one-SQLite-database-per-course design maps cleanly onto Open edX course keys, and its OpenAI-compatible client already points at Ollama with a base-URL change.
5. **Weeks 6–8 — wire the evidence spine.** Every tutor turn, mastery update and grade writes an xAPI statement into `lrsql`.
6. **Weeks 8–10 — faculty acceptance.** Expose mastery estimates through `tutor-mcp` so a committee can see *why* the system judged a learner ready.

### 🔵 Why the statement log is the deliverable, not a nice-to-have

LATAM's regulatory position is the **least settled** of the four regions this base tracks — only Peru has an enacted AI law, Brazil's bill is pending. It is tempting to read that as "fewer obligations, ship faster". **That is the wrong read for a public university**, for two reasons this base has already measured: a public institution procures against *institutional* accountability rules that exist whether or not an AI statute does (Universidad de los Andes counted **716** AI-related instruments and rules in the region), and student data is **minors' and protected data under LGPD and its peers regardless**. The statement log is what lets the university answer "what did the system do to this student" in a region where nobody has yet told it which form that answer must take. 🟢 **Build it first and the eventual statute is a reporting change, not a re-architecture.**

### ⚠️ What this pattern does not claim

- **Neither Colombian row is production software.** `0★`, 4 and 151 commits, no external review, and `trabajo2-` in the name of one marks it as coursework. They are **prior art and an integration reference**. A proposal that lists them as dependencies is misreading this page; a proposal that says *"the Open edX integration boundary has a published reference implementation from a peer institution"* is reading it correctly — and that is worth real weeks.
- **The tutor quality comes from DeepTutor, not from the LATAM rows.** What the LATAM rows contribute is **placement, language and integration shape** — which is precisely what a localisation exercise usually gets wrong and what a client committee will probe hardest.
- **This is not a Moodle pattern.** Moodle dominates much of LATAM schooling, and its bridge field tops out at **27★** across seven MIT servers (**P8**). This pattern is for the Open edX half of the region, and the two are not interchangeable.

## P29 — Licence remediation first: turn LATAM's most-used education agents into a base you can actually build on (2–3 weeks of relationship work, then 6–8 weeks of product) 🟢 new at p664

🔵 **Why this pattern exists, and why it is unlike every other one in this file.** Every other pattern here starts from a permissively-licensed component and composes. This one starts from the measurement at **T32**: in Brazil, the education agent with **2,988 stars and 367 forks** (`digitalinnovationone/dio-agent`, built by **DIO**, a major Brazilian technology-education platform) has **no licence file at all**, while the three permissive LATAM rows on `agents/top.md` have **zero stars between them**. Adoption and licensability are inversely correlated. So the first move is not engineering — it is **getting a licence file upstreamed** — and it unlocks more value per week than any build on this page.

### The parts

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| **The remediation target** | [`digitalinnovationone/dio-agent`](https://github.com/digitalinnovationone/dio-agent) | 🔴 **NONE** — no file at `LICENSE`, `LICENSE.md`, `LICENSE.txt` or `COPYING`; `gh api spdx = null` | **2,988★ / 367 forks**, pushed 2026-10-29. The most-adopted LATAM education agent this base has measured. 🔴 **Unusable as-is by anyone, including its own forkers.** This is the asset the pattern is about |
| **The fallback base** | [`ThallesYVasconcelos/Agente-Educacional`](https://github.com/ThallesYVasconcelos/Agente-Educacional) | 🟢 **MIT** (1,089 B) | 🟢 **The template that already works.** BNCC-keyed lesson plans (`EF01`–`EF04`), page-cited answers over MEC documents, LangGraph supervisor, ChromaDB + `bge-m3`, Ollama-first, FastAPI **MCP server**, Giskard evals. If remediation fails, this is where the build starts instead |
| School/fee system | [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **MIT** (1,094 B) | **411★ / 153 forks**, Laravel + Filament. 🟢 **The permissive SIS** — enrolments, attendance, grades, invoicing can be extended and shipped **closed**. The GPL-2.0 alternatives (RosarioSIS, openSIS) cannot |
| Platform | `moodle/moodle` **or** `openedx/openedx-platform` | GPL-3.0 / AGPL-3.0 | Whatever the client already runs. ⚠️ **Host, never derivative** |
| Model | Ollama + an open-weight model on client hardware | — | EduRAG already defaults this way; `gpt-4o-mini` is its fallback, not its base case |
| Evaluation | [`OpenEuroLLM/JudgeArena`](https://github.com/OpenEuroLLM/JudgeArena) | Apache-2.0 | Swappable **local** judge, so lesson-plan and answer quality is scored without student work leaving the building |
| Evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 | **P17**'s spine. The `<1/3-of-PoCs-reach-P&L` problem is a measurement problem |

### How it wires together

1. **Weeks 1–2 — the licence conversation, and run `P27` on everything first.** Grade the grant of every candidate before writing a line (`P27` is the standing gate). Then approach DIO with a *specific, small ask*: add a permissive `LICENSE` file. Bring the argument, not the request — **367 forks are currently in an unlicensed position**, which is a liability for DIO's own community and a trivially fixable one. 🔵 **Budget this as relationship work with a named publisher, not as a legal negotiation.** The deliverable is a file.
2. **Week 2 — fork the decision, honestly.** If a licence lands, the 2,988-star base becomes composable and the pattern continues on it. **If it does not, drop it and continue on `Agente-Educacional`** — that branch is why this pattern has a fallback column and why it is not a gamble. ⚠️ Never ship a derivative of an unlicensed repository while waiting for an answer.
3. **Weeks 3–5 — harden the BNCC spine.** Take EduRAG's corpus design — BNCC + PCN + PNLD with **output keyed to official skill codes** — and make it the product's contract. A lesson plan that emits `EF02MA03` is auditable by a Brazilian school inspector in a way that a generated paragraph is not. Replace its Self-RAG check with `JudgeArena` running a local judge, so faithfulness scores become reproducible artefacts.
4. **Weeks 4–6 — attach the administrative half, closed.** Mount **Academico** for enrolment, attendance and invoicing. 🟢 **This is the licence-tier payoff of `664-C`:** MIT means the fee-and-enrolment surface can be re-branded and shipped as the client's own product. Filament makes the admin surface generated resource work rather than bespoke CRUD.
5. **Weeks 6–7 — platform bridge.** Expose the assistant to whatever LMS the client runs, via the MCP server EduRAG already ships. Keep the boundary at the process edge so the GPL/AGPL host never contaminates the derivative.
6. **Weeks 7–8 — the evidence spine and the strategy document.** xAPI statements into `lrsql`, and a formal AI strategy artefact. **UNESCO IESALC measured 87% of LATAM higher-education institutions using AI with only 26% holding a formal strategy** — the document is not overhead, it is the thing 74% of the market is missing and can cite a denominator for.

### 🔵 Why the licence ask is the highest-leverage two weeks in the region

A studio entering LATAM can spend those weeks building a tutor that will be the region's fourth `0★` permissive agent, or it can spend them converting a **2,988-star, 367-fork** community asset into something the whole region can build on — including the studio. The second outcome creates a reusable base, standing with a major Brazilian education publisher, and a public contribution that costs no engineering. It is also reversible at no cost: step 2 is a clean fork point.

### ⚠️ What this pattern does not claim

- **It does not claim DIO will say yes.** The pattern is built so that a no costs two weeks and loses nothing — the fallback base is already verified MIT and already does the job.
- **It does not claim `dio-agent` is good software.** Nobody on this base has assessed its quality; **it cannot be read as a dependency at all until it has a grant**, which is the point. Stars measure adoption, not fitness.
- **It does not generalise beyond Brazil on this evidence.** **T32** is measured on Brazilian repositories in one pass. The Spanish-language legs at p663 and p664 surfaced only research-scale addresses, so there was no high-adoption Spanish-speaking case to grade.
- **`Agente-Educacional` is `0★` prior art, not a product.** 46 commits, 0 forks, no external review, and its README names no institution — only an LLM course. The engagement is to harden it; the BNCC corpus design is what is being reused, not the code quality.

## P30 — The sovereign course AI an EU institution can authorise in one meeting (EMEA public higher education and K-12: 6–8 weeks) 🟢 new at p664

🔵 **Why this pattern exists now.** Until p664, every EMEA data-residency conversation on this base was answered with an *architecture* — "OpenTutor or wordlink can run with no egress" — and not with a **named reference deployment at a European institution**. `RUC-Digital-Media-Lab/RUCAI` (MIT, Roskilde University's Digital Media Lab, Denmark) changes that, and it does so on the one design detail that matters to a data-protection officer: **the teacher surface and the student surface are separate artefacts, with separate credentials and separate document scope.**

### The parts

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| **Reference deployment** | [`RUC-Digital-Media-Lab/RUCAI`](https://github.com/RUC-Digital-Media-Lab/RUCAI) | 🟢 **MIT** (1,075 B) | 🟢 **The pattern's keystone, and the first EMEA agent row on `agents/top.md`.** FastAPI + PostgreSQL/pgvector, Ollama for embeddings *and* chat, async ingestion, source-traced answers, **password-protected student instances scoped to selected material**, `deploy/` scripts for an Ubuntu VM under systemd. ⚠️ `0★` pilot software; placement provisional (`664-H`) |
| Platform | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** (10,982 B) | The permissive institutional LMS, **and EMEA-built** — its grant payload names the OLAT Zentrum at the University of Zurich. ⚠️ Default branch `master` |
| Administration | [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **MIT** | Enrolment, attendance, grades, invoicing — shippable closed |
| Retention | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | MIT | Ships **FSRS 4.5 in-tree** and runs with no API key. Supplies the scheduling primitive `RUCAI` has no opinion about (**T13**, **P6**) |
| Model | Ollama, on institution hardware — `bge-m3` + `gemma3:12b` are RUCAI's defaults and are env-var swappable | open weights | The whole premise. A procurement officer who has specified *"EU-hosted, open weights, local deployment"* — as TU Eindhoven's published tool guidance does — is describing this row |
| Evaluation | [`OpenEuroLLM/JudgeArena`](https://github.com/OpenEuroLLM/JudgeArena) | Apache-2.0 | 🟢 **Local judge backend**, from the EU's own publicly funded programme. The Annex III *"show me this is fit for assessment"* evidence, produced without egress |
| Evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 | **P17**'s spine; the logging and human-oversight record the Act asks for |

### How it wires together

1. **Week 1 — `P27` on every component, then stand RUCAI up as-is.** 🔴 **Resolve the address before cloning:** RUCAI's own README Quick Start points at [`Frederikmh90/RUCAI`](https://github.com/Frederikmh90/RUCAI), the author's personal account, while this pattern cites the **organisation** address. Both resolve to the identical `HEAD ebdaae609e529cbe3c0696d7f74de18d8ebf605a` and the identical payload (`sha256₁₂ 2e9f1f76d670`), so there is no content risk — but `gh api` cannot see the personal one at all (`664-D`), so **automation must be written against the organisation address**. Its `deploy/` scripts give a working Ubuntu VM + pgvector + systemd install; the README is explicit that they are operational helpers, not a production installer.
2. **Week 2 — the demo that ends the egress argument.** Upload the client's own course readings; show answers with sources; publish a student instance; then **pull the network cable and do it again**. Everything runs against local Ollama. This is a half-day, and it is the meeting the whole engagement turns on.
3. **Weeks 2–4 — harden the two surfaces.** `RUCAI` is pilot software: the teacher auth is `.env` credentials with an optional users file. Replace it with the institution's SSO, put per-course retention on the uploaded-document store, and make the student-instance password policy institutional. 🔵 **Keep the two-artefact separation intact — it is the reason this row was filed.**
4. **Weeks 3–5 — attach platform and administration.** Mount it alongside **OpenOlat** (Apache-2.0, so the integration layer can be closed) and **Academico** for the administrative tier. The whole stack below the LMS is now permissive, which means the deliverable can be the client's branded product rather than a published derivative.
5. **Weeks 4–6 — add retention.** Lift **OpenTutor**'s in-tree FSRS to schedule review over the same ingested material. `RUCAI` answers questions; it does not decide *when* a learner should see something again.
6. **Weeks 5–7 — the Annex III file.** `JudgeArena` with a local judge scores answer groundedness against the uploaded corpus on a repeatable schedule; `lrsql` holds the statement log; the human-oversight record names who reviewed what. 🔵 **Date it to December 2027, not August 2026** — the Digital Omnibus moved stand-alone Annex III obligations, and most published guidance is stale (**T7**, **T15**, and the EMEA section of `intel/market.md`).
7. **Weeks 7–8 — dual UK/EU conformity, if the client sells into both.** The UK DfE's **generative AI product safety standards for education (January 2026)** are a product-standards regime, not a risk-classification one. The same evidence base satisfies both; nobody is currently selling that as one artefact.

### ⚠️ What this pattern does not claim

- **`RUCAI` is not production software and the pattern does not pretend otherwise.** `0★`, 0 forks, one author, ~46 commits, explicitly *"research software developed for a pilot teaching context"*. What it contributes is a **validated shape** and an institutional reference — the hardening in steps 3–4 is the actual work.
- **Its EMEA placement is provisional.** The MIT grant, the code and the architecture are first-hand; the Roskilde affiliation is not — `zenodo.org` and `cambridge.org` are unreachable from the session that filed it (`664-H`). **Read `DOI 10.5281/zenodo.20622874` before putting "Roskilde University" in a client deck.**
- **It does not make anyone AI-Act compliant.** It produces the artefacts an Annex III assessment needs. Classification, DPIA and conformity are the institution's, with counsel.
- **`JudgeArena` knows nothing about education.** 19★, general evaluation infrastructure, filed because education's gap is measurement and this is permissive measurement. It will not tell you whether a rubric is pedagogically sound.

## P31 — The teacher-side pilot that passes a data-governance review, and is graded by a rubric the client can read (K-12 and vocational, North America and EMEA: 4–6 weeks) 🟢 new at p665

🔵 **Why this pattern exists now.** Every teaching-assistant pilot this base has scoped has failed one of two reviews: the **data** review (what leaves the building) or the **evidence** review (how anyone knows the output is any good — **T10**, **T19**). Until p665 this base had no permissive component that answered the second one; `anthropics/k12-teacher-skills` ships `evals/` with its rubrics, and that turns a demo into an acceptance test.

### The parts

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| **Teacher application** | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | 🟢 **MIT** (`1,078 B`) | 🟢 **The keystone.** Local-first: ingests the teacher's own PDF/DOCX/PPTX corpus, builds a **teaching-style profile**, emits a teacher DOCX + student DOCX + PPTX bundle. `clawed serve` gives a local dashboard and API; the provider is chosen in a wizard, so it can be pointed at Ollama. On PyPI at `9.18.2026.1` |
| **Pedagogy + the grading instrument** | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 **Apache-2.0** (`11,357 B`) | Four skills — plan creation, **differentiation into below/at/above tiers**, lesson prep, and a formative check whose **distractors come from documented misconceptions** — plus `evals/`, the only eval framework on any shelf here. ⚠️ Its Learning Commons Knowledge Graph is a hosted connector outside the grant: **take the skills and the rubrics, not the graph** |
| **Diagnosis before instruction** | [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 🟢 **MIT** (`1,102 B`) | The student-facing half, and the only row here that establishes the gap before teaching into it. Needs a host runtime |
| **Delivery into the incumbent LMS** | [`Menkoban/KI-Unterrichtswerkstatt`](https://github.com/Menkoban/KI-Unterrichtswerkstatt)'s Moodle pipeline | 🟢 **MIT** (`1,065 B`) | 🟢 **The reason this pattern clears the data review.** It emits a themed Moodle course as an **`.mbz` course backup** — a file, handed to whoever administers the Moodle. **No API token, no web service enabled, no plugin installed, no egress.** Compare `moodle-mcp` (27 ★), which needs live web-service credentials |
| **Model** | Ollama on school or district hardware | MIT | Makes “nothing leaves the building” a fact rather than a configuration |
| **Retention, if the pilot proceeds** | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) + [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | FSRS timing and BKT mastery behind MCP surfaces (**P6**, **T13**) |

### Wiring

1. **Week 1 — corpus and profile.** `clawed ingest ./lessons/` over one teacher's real material for one subject and one year group. The teaching-style profile is the deliverable of this week; nothing is generated for students yet.
2. **Week 2 — load the pedagogy, then write the acceptance test first.** Install `k12-teacher-skills` as a plugin into the same runtime. 🟢 **Lift `evals/` before generating anything** and agree its rubrics with the client's head of department as the pilot's pass/fail criteria. *This step is the pattern.* A pilot with a rubric agreed in week 2 is an evaluation; the same pilot with a rubric written in week 6 is a sales demo.
3. **Week 3 — generate, differentiate, check.** Produce lesson bundles for one unit; run `k12-lesson-differentiation` to get the three tiers; attach a `k12-check-for-understanding` item to each lesson. Every artefact is reviewed and edited by the teacher in Word and PowerPoint — the hand-edit is the feature, not a gap.
4. **Week 4 — deliver without touching the LMS's credentials.** Run the `KI-Unterrichtswerkstatt` Moodle pipeline over the unit and hand the administrator an `.mbz`. 🔵 **Record in the pilot report that no LMS web service was enabled** — this is the sentence that gets the second unit approved.
5. **Weeks 5–6 — score against the week-2 rubric and decide.** Add `universal-diagnostic-tutor-skill` only if the teacher-side scores pass; a diagnostic tutor in front of students is a different review.

⚠️ **Honest limits.** `Claw-ED` is self-labelled **Beta** at 64 ★ and `KI-Unterrichtswerkstatt` is a 1 ★ repository four days old at p665: both are **adopt-and-harden bases, not installs**, and the pilot must be staffed accordingly. The `.mbz` route is one-way — it ships a course in, it does not read grades back out; for that you still need `moodle-mcp` or LTI (**Pattern I** in `verticals/solutions.md`). And `k12-teacher-skills`' maths check-for-understanding is **maths**: for other subjects the rubric transfers, the misconception bank does not.

## P32 — Integrating with a European ministry's open stack without inheriting the EUPL (EMEA public sector: 10–14 weeks) 🟢 new at p665

🔵 **Why this pattern exists now.** p665 filed the first **EUPL** tier on `verticals/solutions.md`: seven `Opetushallitus` repositories in which the Finnish National Agency for Education runs its production learner stack in public. The reflex — fork it, brand it, host it — is the one move the licence punishes, because the EUPL counts making the Work available **online** as distribution. The pattern is the other move.

### The parts

| Layer | Component | Licence | Role |
|---|---|---|---|
| **Curriculum authority** | [`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet) | 🟠 **EUPL-1.1+** | The national core curriculum and qualification requirements as a **service with a data model**. Read it; do not vendor it |
| **Statutory learner plan** | [`Opetushallitus/ehoks`](https://github.com/Opetushallitus/ehoks) | 🟠 **EUPL-1.1+** | The personal competence development plan — what “personalisation” means in a European tender |
| **Intake / attainments / identity** | [`ataru`](https://github.com/Opetushallitus/ataru) · [`suorituspalvelu`](https://github.com/Opetushallitus/suorituspalvelu) · [`oppijanumerorekisteri`](https://github.com/Opetushallitus/oppijanumerorekisteri) | 🟠 **EUPL-1.2+ / 1.1+** | Applications, completed studies, learner identifier |
| **Your agent layer** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) or [`RUC-Digital-Media-Lab/RUCAI`](https://github.com/RUC-Digital-Media-Lab/RUCAI) | 🟢 MIT | **Separate process, separate repository, separate grant.** Calls the services over HTTP; links no EUPL code |
| **Synchronous teaching** | [`apache/openmeetings`](https://github.com/apache/openmeetings) | 🟢 **Apache-2.0** | 🆕 Live classroom with whiteboard, recording and LMS plugins — the permissive answer where BigBlueButton is LGPL-3.0 |
| **Evaluation** | [`OpenEuroLLM/JudgeArena`](https://github.com/OpenEuroLLM/JudgeArena) | Apache-2.0 | Local judge backend from the EU's own programme — the Annex III fitness evidence |
| **Oversight record** | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 | xAPI statements as the human-oversight log (**P17**) |

### Wiring

1. **Draw the boundary before the first commit, and write it down.** The EUPL components run as **their own services**, deployed unmodified, reached only over their HTTP APIs. Your code lives in its own repository under MIT or Apache-2.0 and links **no** EUPL library. Process separation plus network calls is the boundary; a vendored module or a static link is not.
2. **Pin and document each service's version and payload.** Each repository's grant, bytes and branch go in the project's licence register — `eperusteet`/`oppijanumerorekisteri`/`organisaatio` serve the **identical** `632 B` payload (`sha256₁₂ 7c5df5c3eacb`), `ataru` is EUPL-**1.2**, `suorituspalvelu` is EUPL-1.2 **on `main` while the rest are on `master`**. ⚠️ `gh api` reports every one of the seven as `NOASSERTION`: **read the file, not the sidebar**.
3. **Model the curriculum from `eperusteet`, do not re-key it.** Ground the agent's retrieval in the authority's own structures (units, competence requirements, assessment criteria) so that “standards-aligned” is a join, not a claim.
4. **Treat `ehoks` as the personalisation contract.** Your agent proposes; the statutory plan records. Writing a proposal back into the plan is a governance decision, not an integration task — scope it as a separate phase with the ministry's own data controller.
5. **Fix anything you must fix upstream, in the open.** If a service needs a change, contribute it to the ministry's repository under its EUPL rather than carrying a private fork: the patch stays theirs, your stack stays permissive, and the procurement story improves.
6. **If a fork becomes unavoidable, re-scope commercially before writing code.** Then the EUPL travels with your hosted service, and the appendix's compatibility list (GPL-2.0, AGPL-3.0, EPL, MPL-2.0, LGPL, OSL, CeCILL, LiLiQ) is the only relicensing room you have. ⚠️ **It does not contain MIT or Apache-2.0.**

⚠️ **Honest limits.** This stack is **Finland's**, in Finnish, built for Finnish statute — the *shape* generalises to other EU member states, the data model does not. Star counts (0–11 ★) are meaningless here and are not an adoption signal either way: this is one deployment with a nation behind it. And none of these seven repositories contains any AI — **this pattern buys an integration surface and a licence posture, not a model.**

## P33 — A curriculum-grounded teacher agent that grounds against the *local* curriculum, not a PDF (LATAM or EMEA K-12: 8–10 weeks) 🟢 new at p666

🔵 **Why this pattern exists now.** Every curriculum-grounded agent on `agents/top.md` grounds itself in a *document*. p666 filed the two halves that make grounding an **integration** instead: [`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet) publishes the **national** core curriculum as a service, and [`Opetushallitus/eperusteet-ylops`](https://github.com/Opetushallitus/eperusteet-ylops) is how a school or municipality derives its **local** curriculum from it. On the LATAM side, [`GuilhermeScarpini/agente-bncc-professores`](https://github.com/GuilhermeScarpini/agente-bncc-professores) is a working **MIT** reference for binding generation to official skill codes.

### The parts

| Layer | Component | Licence | Role |
|---|---|---|---|
| Curriculum source (EMEA) | [`Opetushallitus/eperusteet-ylops`](https://github.com/Opetushallitus/eperusteet-ylops) + [`eperusteet`](https://github.com/Opetushallitus/eperusteet) | 🟠 **EUPL-1.1-or-later** | The local curriculum *and* the national core it derives from, as data with a model — **read over the API, never forked** (see `P32`) |
| Curriculum source (LATAM) | BNCC skill codes, bound as in [`GuilhermeScarpini/agente-bncc-professores`](https://github.com/GuilhermeScarpini/agente-bncc-professores) | 🟢 **MIT** (code) | The reference implementation of code-level binding: semantic search over skills → generation → editable questions → PDF. ⚠️ The BNCC texts carry their own terms, separate from this MIT code |
| Agent runtime | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | Multi-mode delivery and the persistent learner model (`55,260★` at p666, payload `11,408 B` re-read and reproduced) |
| Lesson/assessment generation | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | 🟢 MIT | ADDIE multi-agent materials generation, driven **from the curriculum codes** rather than from a prompt |
| Assessment content | [`Opetushallitus/ludos`](https://github.com/Opetushallitus/ludos) | 🟠 EUPL-1.1-or-later | Where EMEA scope needs items an authority issued rather than items a model wrote |
| Local model runtime | [`ollama/ollama`](https://github.com/ollama/ollama) | 🟢 MIT | Keeps learner data on-premise — the usual condition in a public K-12 tender |

### Wiring

1. **Resolve the curriculum object first, before any model call.** EMEA: pull the municipality's local curriculum from `eperusteet-ylops` and its national parent from `eperusteet`. LATAM: load the BNCC skill set and index it exactly as `agente-bncc-professores` does. 🔴 **The deliverable is a *skill-code → content* mapping, not a chat log** — this is what makes output inspectable by someone who does not trust the model.
2. **Generate against the code, not the topic.** Drive `instructional_agents` with a skill code as the unit of work, so every generated plan, slide and item carries the code it serves. One code in, one traceable artefact out.
3. **Serve assessment from the authority where one exists.** In EMEA, prefer a `ludos` item over a generated one and record which you used; in LATAM, generate but keep the answer key editable, as `agente-bncc-professores` already does.
4. **Deliver through `DeepTutor`**, whose persistent learner model is keyed to the same curriculum codes, so "where is this student" is answerable in the inspector's vocabulary.
5. **Run the model locally via `ollama`** and keep the curriculum service calls read-only.

🔴 **The two things that make this fail, both stated up front.** (1) **Licence boundary**: the EUPL tier is copyleft whose *"Distribution or Communication"* reaches making the Work available online — so `eperusteet*` and `ludos` are **integrated against over the network and never vendored into your tree** (`P32` is the full shape). (2) **`agente-bncc-professores` is `0★`, `0` forks, one author** — a reference implementation of the binding, **not a maintained dependency**. Read it, reimplement the binding in your stack, credit it.

🟢 **Why the pattern is worth the weeks.** "Curriculum-aligned" is the claim every edtech vendor makes in a K-12 tender and almost none can evidence. This produces an artefact that is aligned **by construction and traceable code by code** — and in Finland's case, traceable to the ministry's own service.

## P34 — Early-childhood education: start from the national register, not from the learning app (EMEA public sector: 6–8 weeks to a scoped pilot) 🟢 new at p666

🔵 **Why this pattern exists now, and what it corrects.** `p660` went looking for permissive **early-years** assets and found *learning* tools — ScratchJr (BSD-3-Clause, dormant since 2022), the micro:bit stack (MIT). Useful, and not what an ECEC engagement is about. p666's org enumeration found [`Opetushallitus/varda`](https://github.com/Opetushallitus/varda) — **the national early-childhood-education register**: children, guardians, placements, staff, fee decisions, under **EUPL-1.1-or-later**, pushed `2026-10-27`.

### The parts

| Layer | Component | Licence | Role |
|---|---|---|---|
| Record system | [`Opetushallitus/varda`](https://github.com/Opetushallitus/varda) | 🟠 **EUPL-1.1-or-later** | Reference data model for national ECEC administration — placements, staffing ratios, fee decisions. Python/Django on PostgreSQL |
| Identity / organisation | [`Opetushallitus/organisaatio`](https://github.com/Opetushallitus/organisaatio) + [`oppijanumerorekisteri`](https://github.com/Opetushallitus/oppijanumerorekisteri) | 🟠 EUPL-1.1-or-later | Provider and learner identifiers — the join keys the register assumes |
| Agent layer (**your IP**) | [`CrewAI`](https://github.com/crewAIInc/crewAI) or [`LangGraph`](https://github.com/langchain-ai/langgraph) | 🟢 MIT | Placement-matching, staffing-ratio checks, fee-decision drafting, multilingual guardian correspondence |
| Model runtime | [`ollama/ollama`](https://github.com/ollama/ollama) | 🟢 MIT | On-premise — this is children's data under GDPR, and no other posture survives procurement |
| Learning layer, *if* the scope reaches it | [`scratchfoundation/scratchjr`](https://github.com/scratchfoundation/scratchjr) (BSD-3-Clause) / micro:bit MIT stack | 🟢 permissive | Added **after** the record layer, never instead of it. ⚠️ ScratchJr is dormant since `2022-07-22` — fork-and-own with a priced maintenance line (`660-I`) |

### Wiring

1. **Read `varda`'s data model as the specification.** The valuable artefact is not the Django code — it is the set of entities and obligations a national regulator considers complete for ECEC. Clone to read, scope from the model.
2. **Build the agents outside the EUPL boundary**, speaking to the register over its API. Placement matching and staffing-ratio compliance are the two with an immediate operational payoff.
3. **Keep every model call local via `ollama`**, and keep guardian-facing output drafted-not-sent: an ECEC fee decision is an administrative act.
4. **Only then** consider a learning layer, and treat ScratchJr's dormancy as a cost line rather than a footnote.

🔴 **The honest limit.** `varda` is `3★`. That is not adoption evidence and must not be sold as it: 🟢 **it has exactly one deployment and a country behind it.** For a ministry or municipal buyer that is the stronger fact; for a private buyer it is irrelevant, and this pattern is not for them.


## P35 — Make it stick, and prove it: the retention layer as a product, with the objective function as a client decision (any sector delivering training at scale: 6–8 weeks) 🟢 new at p667

🔵 **Why this pattern exists now.** Every engagement that generates learning material eventually meets the same question from the buyer: *does any of this actually stick, and how would we know?* Until p667 this base could only answer "use FSRS" — true, and a dead end, because it offered no trade-off and no citation. `p667` filed sixteen permissive rows that turn retention from a library choice into an **architecture choice** with four explicit decisions (see **T49**). This pattern is how you walk a client through those decisions in one engagement.

### The parts

| Layer | Component | Licence | Role |
|---|---|---|---|
| Scheduler — option A | [`open-spaced-repetition/fsrs-rs`](https://github.com/open-spaced-repetition/fsrs-rs) | 🟢 **MIT** | Optimises **predicted recall**. The incumbent, consumer-scale, already on `repos/foundations.md`. Pick this when the client's goal is retention at a fixed review budget. |
| Scheduler — option B | [`maimemo/SSP-MMC`](https://github.com/maimemo/SSP-MMC) | 🟢 **MIT** (`1,064 B`, read at p667) | Optimises **total review cost to reach a target recall**. Research code, lift the algorithm. Pick this when the client's goal is *time-to-competence* — certification, onboarding, compliance training. |
| The citation | [`Human-Centric-Machine-Learning/memorize`](https://github.com/Human-Centric-Machine-Learning/memorize) | 🟢 **MIT** (`190★`, `master`) | Code **and real data** for the **PNAS 2019** spaced-repetition optimisation result. This is what you put in the deck when the client asks who says so. |
| Item bank — adopt | [`nastaso/cloudcertprep`](https://github.com/nastaso/cloudcertprep) | 🟢 **MIT** (`246★`) | **1,469 real questions** (AWS CLF-C02, AIF-C01). Start here for any cloud/AI certification programme instead of writing items. |
| Item bank — generate | [`assafkip/claudemy`](https://github.com/assafkip/claudemy) + [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) | 🟢 MIT | Already on `agents/top.md`; both generate **with cited sources**, which is the provenance requirement this pattern depends on. |
| Card store (**the governance trick**) | [`kitschpatrol/yanki-obsidian`](https://github.com/kitschpatrol/yanki-obsidian) | 🟢 **MIT** (`200★`) | Cards live as **plain Markdown in a git repository** and sync to Anki. Generated items become reviewable in a pull request. |
| Delivery — hand-off | [`repeat-space/anki-apkg-export`](https://github.com/repeat-space/anki-apkg-export) | 🟢 **MIT** (`182★`) | Writes a `.apkg` **file** with no Anki installed — the artefact you attach to an email or ship in a build. |
| Delivery — in-product | [`olmps/memo`](https://github.com/olmps/memo) | 🟢 **BSD-3-Clause** (`1,870★`) | Flutter, so one codebase gives iOS + Android + desktop. ⚠ Pushed 2024-07-29 — **adopt the codebase, budget for the fork.** |
| Agent surface | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) + [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 MIT | Already on `agents/top.md`: the agent drives scheduling and mastery through MCP rather than reimplementing either. |

### Wiring

1. **Make the client choose the objective function in week 1, on the record.** Recall-at-budget (FSRS) or cost-to-mastery (SSP-MMC). This is a business decision disguised as a technical one, and it determines everything downstream. Put the PNAS result in front of them so the choice is argued, not asserted.
2. **Decide adopt-or-generate for the item bank.** If the domain is a certification with a public blueprint, `cloudcertprep` proves the bank is cheap to adopt. If the domain is the client's own material, generate with `claudemy`/`lumen` — **and keep the citations**, because step 3 depends on them.
3. **Put the cards in git as Markdown via `yanki-obsidian`.** This is the step that makes the whole thing auditable: every generated item arrives as a diff with its source citation, a subject-matter expert approves it in a pull request, and the review history is the evidence artefact. **Do this before building any UI** — it costs a day and it is what survives a governance review.
4. **Wire the scheduler behind MCP** (`anki-mcp-server` for scheduling state, `tutor-mcp` for the mastery model) so the tutoring agent reads and writes the real schedule instead of carrying its own.
5. **Pick the delivery form last, from the hand-off requirement.** A `.apkg` file (`anki-apkg-export`) if the learner already uses Anki or the client wants an artefact; a branded app (`olmps/memo`, BSD-3) if it must carry the client's name; the vault-native route (`LearnKit`) if the cohort is technical and local-first matters.
6. **Instrument from day one and report against the chosen objective.** Whichever function was picked in step 1 is the one the final report must measure, or the engagement has no verdict.

🔴 **The honest limits.** `SSP-MMC` and `memorize` are **research code, not libraries** — you are lifting an algorithm and owning the implementation, which is real effort and should be a line in the estimate. `olmps/memo` has not been pushed since July 2024; adopting it means forking it. And none of this answers whether the *content* is any good — retention scheduling makes correct material stick and makes wrong material stick just as well, so step 2's citation requirement is load-bearing, not decoration.

🟢 **Why this sells.** It is the only pattern in this file where the governance answer and the product are the same artefact: a git repository of cited, expert-approved, version-controlled learning items with a published scheduler behind it. **T3** says governance is the buying trigger; this is the cheapest place in the whole stack to satisfy it.

## P36 — The licence-provenance triage, extended: rank the claim before you ask for the grant (1 day, as the front half of P27) 🟢 new at p667

🔵 **Why this exists.** `P27` established licence provenance as the first two weeks of any education engagement, on the correct principle that a licence **identifier is not a licence** and the payload must be read. `p667` adds the case `P27` does not cover: **what to do when there is no payload at all.** This happens constantly outside English-language open source — `p666` measured 4 of 6 non-English candidates with no grant payload, and `p667` measured 3 of 6 — and the right response is not a uniform "reject", because the three forms it takes are worth very different things.

### The triage

| What you find | Specimen measured at p667 | Verdict | What to do |
|---|---|---|---|
| **Complete grant text inlined in the README**, no `LICENSE` file | [`MiradoAndreas/learning-plateform-ai`](https://github.com/MiradoAndreas/learning-plateform-ai) — verbatim canonical MIT in a fenced block, and `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `LICENCE.md`, `COPYING` **all 404** | 🟢 **Usable.** The grant exists and is complete; only its location is non-standard. | Normalise the grant text against the canonical template (wrap-insensitive). If it matches, proceed — and open a one-line pull request adding `LICENSE`. This is the cheapest licence remediation there is. |
| **A prose sentence naming a licence** — and check whether it is a *split* grant | [`JRS1986/KISchule`](https://github.com/JRS1986/KISchule) — *"Texte: CC BY-SA 4.0. Code: MIT."* | 🟠 **More restrictive than it looks.** | Work out which half you actually want. This repository is almost entirely Markdown lesson material, so **the asset is CC BY-SA** — share-alike — and only the build script is MIT. A search leg reported it as "MIT-licensed". |
| **A shields.io badge** | [`AiltonRock22/ia-professores`](https://github.com/AiltonRock22/ia-professores) — `![Licença](…badge/licença-MIT-blue.svg)` linked to `LICENSE`; `LICENSE`, `LICENSE.md`, `LICENCA`, `LICENCA.md` all **404** | 🔴 **Worthless as a grant.** No licence text exists anywhere in the repository. | Do not use it, and do not record it as MIT. Ask the maintainer to add a payload; until they do there is nothing to rely on. **This is the mechanism behind search engines' false licence reports** — the summariser reads the badge. |
| **A short bespoke payload** — read it, do not classify it | [`learningfactory-io/ki-werkstatt`](https://github.com/learningfactory-io/ki-werkstatt) — `LICENSE` serves `200` at `413 B` | 🔴 **Proprietary.** *"Alle Rechte vorbehalten… jede kommerzielle Nutzung… nicht gestattet."* | A served `LICENSE` is **not** evidence of a grant — this one is a reservation of rights. Any payload under ~800 B is bespoke by definition and must be read in full by a human. |

### Wiring it into the P27 gate

1. **`git ls-remote --symref` first**, for existence and the **real default branch** — 27% of the addresses p667 verified are not on `main`, and reading a payload at the wrong ref is how a licence gets mis-recorded.
2. **Try the payload at 8 filenames** (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `LICENSE-MIT`, `COPYING`, `LICENSE.rst`, `license`) at that ref. A 404 on all eight means **run this triage**, not "unlicensed".
3. **If a payload exists, grade it on the title line and record the bytes** — never on body text. `p666` showed a body-text classifier grades the full EUPL as AGPL-3.0 off its compatibility appendix. **Abstention is the correct output** for an unrecognised title.
4. **Decompose any non-zero residual before calling it a mutation.** `p667` found `telekom/ki-in-schulen` at `+123`, which the predictor flagged `BODY-MUTATED` and which decomposes exactly into a URL line, a blank line, a **second copyright holder** and 1 B of re-wrap — the grant text is verbatim MIT. A positive residual means *look*, not *reject*.
5. **Strip leading blank lines and uniform indentation before any byte comparison.** `campfirium/foliole` reads canonical Apache-2.0 `+1` on one prepended newline; `microsoftarchive/Learn-LTI` is uniformly indented four spaces, which defeats a copyright-line detector anchored at byte 0.

🟢 **Why a client pays for this.** It is one day, it runs before any architecture work, and it is the difference between a shipped product and a renegotiation. The failure it prevents is specific and common: **a repository that advertises MIT in its README badge, and has no licence at all.**

## P37 — AI in the system of record, without inheriting the system of record's licence (any region, K-12 or small HE, 6–8 weeks)

🔵 **What this is for.** A client runs a school or a small institution on an open source SIS and wants AI in it — predicted grades, attendance triage, a parent-facing enquiry agent, report-card drafting. `T50` is why this is not the usual engagement: on this layer the adoption is copyleft (`rosariosis` GPL-2.0 at `652★`, `openSIS-Classic` GPL-2.0 at `349★`) and the only permissive system of record is `academico-sis/academico` (MIT, `411★`). The default move — fork the thing the client already runs and add AI to it — produces a derivative of a GPL-2.0 work, and on this layer that work holds student records, so the question is never hypothetical.

🟢 **The pattern: put the agent *beside* the SIS, not inside it, and make the process boundary the licence boundary.**

**Weeks 1–2 — gate, before any code.** Run **`P36`** (rank the licence claim) then **`P27`** (the licence-provenance gate) against the client's actual deployed tree, not the upstream repo. Byte-read the grant at the real default ref — `667-K` and `668-H` between them give four claim-forms, and two of this pass's three specimens were on `master`, not `main`. Deliverable: the client's own dependency graph with a licence per node, per `T16`, because **the licence unit is the graph, not the repository**.

**Weeks 2–4 — the boundary.** Stand the agent up as a separate service that talks to the SIS over its HTTP API and its database read replica. Nothing links against SIS code; nothing is compiled into it. Concretely:
- **Orchestration:** `LangGraph` (MIT) — the reference stack per `T2`, with the policy nodes `P6` uses for multi-jurisdiction rules.
- **SIS bridge:** the SIS's own REST API. `rosariosis` and `openSIS-Classic` both expose one; `academico` (MIT) can be linked against directly if the client is on it, and that is the one case where this pattern collapses into the cheap version — **check first, because it changes the estimate by two weeks.**
- **Retention/scheduling,** where the use case is revision or intervention timing: the layer `p667` filed and `T49` describes — FSRS and the `SSP-MMC` scheduler, permissive, already in production elsewhere.
- **Serving:** `Ollama` or `vLLM` on client infrastructure, for the data-residency reason `P30` sets out; this layer holds student records, so a hosted API is a governance conversation, not a technical default.

**Weeks 4–6 — the teacher-facing half.** Per `T35` and the 2026 consensus, ship to **teachers first**, not students: draft-and-confirm only, with the human edit as the committed action. `P31` is the pilot shape that passes a data-governance review; reuse its rubric rather than inventing one.

**Weeks 6–8 — the compliance artefact.** Produce the deployer documentation the client is actually obliged to hold. **EMEA:** AI used for student evaluation is Annex III high-risk, now applying from **`2027-12-02`** per the Digital Omnibus (`T7`, `T15`) — but **Article 50 transparency applies from `2026-08-02` and Article 4 AI literacy has applied since `2025-02-02`**, so two of the three obligations are live today and only the heavy one moved. **North America:** state-level, not federal; if the deployment touches grading, discipline or IEP decisions, check the jurisdiction first — DC's 2026-27 policy bans AI from exactly those four uses. **APAC:** South Korea's AI Basic Act (in force `2026-01-22`) and Vietnam's Law on AI (`2026-03-01`, with an 18-month education transition) are both binding and neither is education-specific (`T12`). **LATAM:** governance is the gap, not adoption — 87% of surveyed institutions use AI and 26% have a strategy, so the artefact itself is often the differentiator.

🔴 **When not to sell this.** If the client's requirement is genuinely *inside* the SIS — a field on a form, a column in the gradebook — this pattern does not deliver it, and `T50` option (a) or (b) is the honest answer. Say which one and what it costs. 🔵 **The failure mode this pattern exists to prevent is a fork of a GPL-2.0 student-records system shipped as a client-owned product, which is a licence problem discovered at the end of the engagement rather than in week one.**

## P38 — The multi-campus rollout: one agent layer, many institutions, per-tenant configuration (any region, higher education consortia or multi-campus groups, 8–10 weeks) 🟢 new at p669

🔵 **What this is for.** A client is not one institution. It is a university system, a consortium, a national network or a private group with several campuses — each with its own LMS tenant, its own API-token policy, its own data-governance committee, and frequently a *different LMS*. Every pattern above this one assumes a single institution, and the gap shows up immediately in delivery: the pilot works at campus A and the second deployment is a rewrite.

🟢 **Why it is in this file now, and what it rests on.** `669-R2` found the missing piece by accident, while reading repository text for a different purpose. [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) ships **six named institution presets in its own README** — `--purdue`, `--suny`, `--tudelft`, `--cuny`, `--leiden`, `--mcgill` — spanning **three countries and two regions**. That is not a location fact, it is an **architecture fact: the bridge is multi-tenant by construction**, and no other LMS bridge on `agents/top.md` declares per-institution configuration at all. 🔴 **It is also why that row is deliberately left `Global (unplaced)`** — placing a six-country switch list in one region would have been wrong, and `669-D` records the refusal.

**The pattern: make the tenant a configuration object, and the LMS bridge the only tenant-aware layer.**

**Weeks 1–2 — enumerate the tenants before writing anything.** For each campus, record four things and nothing else: which LMS and version, who issues API tokens and under what policy, which jurisdiction's rules bind it, and whether student data may leave the campus. 🔵 **The token policy is the one people skip and the one that stops rollouts.** `vishalsachdev/canvas-mcp`'s README exists partly to document this: it names **University of Illinois Urbana-Champaign** as an institution where self-service API access is unavailable *to everyone*, students and staff alike. A rollout plan that assumes per-user tokens dies at the first campus like that. Budget an admin-issued service-token conversation per tenant.

**Weeks 2–4 — the bridge layer, one adapter per LMS, tenant as a flag.**
- **Brightspace / D2L:** [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) — adopt its preset mechanism as the house pattern rather than inventing one, and extend the list; also [`AnonymousOnyx22/brightspace-d2l-mcp`](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) as a second reading.
- **Canvas:** [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, `317★`, **North America** — documentary) for the read/write surface, and [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) (MIT, `119★`) where the governance committee requires **read-only**. Diff the two per tenant; do not assume one.
- **Moodle:** the MCP field on `agents/top.md` — dominant in LATAM and much of EMEA, so in a mixed group this adapter is usually the second one built, not the last.
- **Open edX:** `TutorIA` as an XBlock/plugin, which lands *inside* the platform's own course surface rather than beside it.
- **Standards fallback, for any tenant whose LMS has no bridge:** [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT) for LTI 1.3 launch and [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) where the surface is notebooks. **LTI is the lowest common denominator across every LMS in this list and it is the reason a mixed-LMS group is tractable at all.**

**Weeks 4–6 — one agent layer, zero tenant knowledge.** Orchestration on `LangGraph` (MIT) per `T2`, with the tutor chosen from the shelf by use case — `DeepTutor` (Apache-2.0) where a persistent learner model is the point, `Bloom` for the fastest demo, `OATutor` (MIT) where the client wants explainable mastery estimates. 🔵 **The rule that makes this a rollout instead of N projects: the agent layer receives a tenant context object and never branches on institution.** Everything institution-specific — base URL, token source, field mappings, retention rules — lives in the bridge's per-tenant config. Per `669-R2`, that is exactly the seam the Brightspace bridge already cuts.

**Weeks 6–8 — per-tenant evidence, one schema.** [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (Apache-2.0) as the LRS with [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec), **one statement schema across all campuses with the tenant on the actor or context**. This is what lets the group compare campuses, which is usually the real reason a consortium is buying centrally — and per `T10` and `T19` the evidence layer is the sector's weak point, so it is also the differentiator.

**Weeks 8–10 — the per-jurisdiction compliance split, which is where a multi-region group costs more than a single-country one.** A mixed group does **not** have one compliance posture: **North America** — California's `AB 1159` prohibits training on student data, so a tenant there constrains the *architecture*, not just the paperwork; several states now mandate district-level policies (`SB 720` and others). **EMEA** — student evaluation is Annex III high-risk from **`2027-12-02`** after the AI Omnibus (`T7`, `T15`), with the UK on DfE/Ofqual national rules in the meantime. **APAC** — Korea's AI Basic Act is in force; Vietnam's law names education; **Australia is Threshold Standard 5.2 and TEQSA guidance, *not* a filing mandate** — see the rejection on `intel/market.md`, reproduced by four independent leg runs. **LATAM** — no binding education-AI statute in most countries, so the constraint is the institution's own framework, which per UNESCO IESALC only `26%` of them have. 🔵 **Scope the compliance artefact per jurisdiction and reuse the technical work across all of them; that ratio is the commercial case for doing it centrally.**

🔴 **When not to sell this.** If the group has one LMS, one jurisdiction and one data-governance authority, this is over-engineered — use `P37` or the single-institution patterns and keep the tenant object out. And if the campuses are genuinely autonomous buyers, the per-tenant conversations in weeks 1–2 are a sales process, not a sprint: say so before the timeline is agreed.


## P39 — The zero-install course factory, with the copyleft taken out and the provenance left in (any region; North America and EMEA public sector first: 5–7 weeks) 🆕 new at p670

**The problem it solves.** A client wants AI-generated course material — syllabus, slides, assessments, lecture video — and the two questions that actually stop the deal are *“where did this content come from?”* and *“what licence are we shipping?”* Every pattern on this page before P39 answered the first by bolting provenance on. **p670 found an artefact that answers it natively and fails the second**, so this pattern is a remediation, not an integration.

**The components — every one verified on 2026-11-05 at p670.**

| Component | Repo | Licence | Role |
|---|---|---|---|
| Course factory | [`DaRL-GenAI/instructional_agents_studio`](https://github.com/DaRL-GenAI/instructional_agents_studio) | **MIT** (`1,093 B`, read this pass) | Browser-only ADDIE pipeline: 6 deliberations → chapters → slides → scripts → homework/lab/quiz → midterm/final with blueprints and answer keys → narrated or animated video. **Provenance tab hashes every input a stage consumed and flags stale stages; audit trail logs every model call, edit, prompt change, approval and export.** |
| Pipeline (server-side) | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | **MIT** | The Python original (EACL 2026). Same three-agent deliberation; use when generation must run on the client's infrastructure rather than in a browser tab. |
| ⚠️ **The component to remove** | [`ranuts/document`](https://github.com/ranuts/document) + ONLYOFFICE `sdkjs`/`web-apps` | 🔴 **AGPL-3.0** (both verified at p670) | **Not shipped — downloaded on first run** into `~/.cache/instructional-agents/editor/<version>/`, or, if absent, replaced by a **hosted editor at `edit.chaxus.com`**. This is the whole reason P39 exists. |
| System of record | [`moodle/moodle`](https://github.com/moodle/moodle) (GPL-3.0, `7,587★`) or [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) (**AGPL-3.0**) | GPL-3.0 / **AGPL-3.0** | Where the generated course is delivered. Integrate across the boundary — see **P37**. 🔧 **Two repairs at p671, and the second is worse than the first:** the address was the `edx-platform` redirect, *and* this cell read **`Apache-2.0`** — the exact error `repos/foundations.md` records as *"the most consequential error in this KB"*. It was corrected on that page and **never propagated here**, so a pattern told the reader an AGPL platform was permissive. |
| LMS bridge | [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) (MIT, `27★`) · [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) (MIT, `62★`) | MIT | Push the finished course in. **For D2L prefer `RohanMuppa` — the other D2L bridge dropped from `29★` to `12★` at p670 (`repos/trending.md` `670-R3`).** |
| Retention | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) (MIT, `546★`) + [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, `96★`) | MIT | Turn the generated quiz items into a scheduled review loop instead of a one-off deliverable. See **P6** and **P35**. |

**Week 1 — the licence surgery, and it comes first because it decides whether there is a project.** Stand the studio up and **confirm the exposure yourself rather than trusting this page**: read its `NOTICE`, then run it and watch what it fetches. 🔴 **Two independent problems, two different fixes.** *(a) The AGPL editor:* the studio needs it only to render and hand-edit `.pptx`/`.docx`. **Set `IA_EDITOR_DIR` to a permissive renderer and never let the ONLYOFFICE build onto the client's estate** — the `.pptx` write path is a layout engine the studio already owns, so the editor is an *editing convenience*, not the generator. If hand-editing is required, keep it **out of process**: the client opens the deliverable in their own Office or LibreOffice install, which is what the studio's own README assumes anyway. *(b) The hosted fallback:* `edit.chaxus.com` must be **blocked at the network layer, not merely unconfigured** — a fallback that activates when a download fails is a fallback that will activate in production. 🟢 **Deliverable of week 1: a one-page licence-and-egress finding, signed off before any content is generated.** This is **P36**'s triage with p670's amendment — read the `NOTICE`, and ask what the artefact downloads on first run.

**Weeks 2–3 — generate one real course, and make the provenance the demo.** Take a module the client already teaches and regenerate it. Run the six ADDIE deliberations in full mode, not quick mode, and **use the Prompt tab to put the client's own instructional standards into the system prompt** before each stage — that edit is logged, which is the point. Feed the client's `.pptx`/`.potx` so the decks come out in their own theme. 🟢 **What to show the governance committee is not the slides — it is the Provenance tab:** every input hash, every stale stage flagged, every model call, every human approval, exportable as JSON/Markdown. **North America is the first market for this** because `134` AI-in-education bills across `31` states (`intel/market.md`) have made traceability the procurement question; **EMEA is the second** because Annex III point 3 puts assessment generation in scope regardless of whether the deferral to `2 December 2027` holds.

**Weeks 3–5 — the human gate, wired as a gate.** The studio's **re-run-with-comments** path revises any stage from instructor comments and logs the request. Configure the engagement so **no generated assessment reaches a learner without a named approval recorded in the audit trail** — which is also how you satisfy the “humans accountable for high-stakes decisions” condition in US federal grant guidance and the deployer duties under the AI Act. 🔴 **Do not automate grading in this pattern.** Generation and assessment-of-record are different risk tiers; keep the read-only posture **P31** and `boyuchengz/canvas-mcp` were filed for.

**Weeks 5–7 — delivery and retention, so the output is a course and not a folder.** Push the generated course into Moodle or Brightspace over the MIT bridge, **integrating across the licence boundary rather than forking the platform** (**P37**). Then take the generated quiz items into `anki-mcp-server` and schedule them with `tutor-mcp`'s mastery model — **the client decides the objective function, per P35.** Without this step the engagement ships content; with it, the engagement ships learning the client can measure.

🔴 **When not to sell this.** If the client's deliverable must be hand-edited in a browser as part of the workflow, the AGPL editor is not removable and **this pattern becomes a copyleft engagement** — price it as one or walk. If the client has no governance requirement at all, the provenance machinery is overhead and `P8`-style generation is cheaper. And if the content must never leave the client's premises, **start from the Python pipeline, not the studio** — the browser edition's advantage is zero install, which is worth nothing behind an air gap.

🔵 **The honest caveat on the artefact itself.** `0★`, `48` commits, one author, first commit `2026-09-23`. **This is pre-adoption code and the pattern treats it as a base to adopt and harden, not a product to resell** — the same posture `agents/top.md` takes on `moodle-mcp` at `27★`. What it buys is a six-week head start on the provenance layer, which is the part clients will not accept hand-waving on.

## P40 — The open-source inventory that detects a change of owner, not just a broken link (any region; 1 week to build, then standing) 🆕 new at p671

**The problem it solves.** Every education engagement that touches open source produces an inventory: the LMS, the plugins, the agent layer, the accessibility stack, the licences. That inventory is then re-checked on a schedule, and **the check is almost always "does the URL still resolve and does the licence file still say what it said"**. Both of those questions keep returning *yes* after a dependency has changed hands, because GitHub honours a rename redirect indefinitely and the grant bytes travel with the repository. Measured at `p671` on this base's own shelves: `2` of `197` addresses pointed at repositories that had **moved to a different owner**, and at both dead addresses `git ls-remote`, `raw.githubusercontent.com` and a `sha256` of the licence payload all passed (`intel/trends.md` **T52**). One of the two had been published as a rename `145` passes earlier and was still wrong on `9` places across `3` pages — so the failure is not detection-once, it is detection-as-a-standing-check.

**Why a client should care, in one sentence.** The licence tells you what you may do; the owner tells you who will still be maintaining it, who can relicense it, and whose governance you have just inherited — and a rename is the moment that changes.

**The components — every one verified on 2026-11-05 at p671.**

| Component | Repo / call | Licence | Role |
|---|---|---|---|
| Liveness + real default ref | `git ls-remote --symref https://github.com/<slug> HEAD` | n/a (git protocol) | Establishes the repository answers **and** the real default branch. `p668-P` measured `54%` of addresses off `main`; a reader that assumes `main` or `master` reads nothing. **Never sufficient on its own — this is the call that passes at a dead address.** |
| Grant payload | `raw.githubusercontent.com/<slug>/<real-ref>/LICENSE` | n/a | Read the bytes, hash them. Also passes at a dead address — at `p671` the AGPL payload had an **identical `sha256`** at both the live and the renamed-away Open edX address. |
| **Owner-change detector** | `gh api -X GET search/repositories -f q='repo:<slug>'` then, on `422`, `q='user:<owner>'` | n/a | **The one call that sees a rename.** `≥1` = indexed and current; `0` = owner indexed, repo not (live but unindexed — dated, not flagged); **`422` + owner `≥1` = RENAMED OR MOVED AWAY.** Controlled on `18` probes at both signs (`repos/trending.md` `671-J`). |
| Batch transport | same call, `q='repo:a/b repo:c/d …'`, 15 slugs per call | n/a | Space-separated `repo:` qualifiers are **implicitly OR-ed**, so a 200-dependency inventory costs `14` calls, not `200`, against a `30/min` cap. Batch poisoning does not occur: one absent or unindexed slug does not invalidate the batch. |
| New-address resolution | `gh api -X GET search/repositories -f q='user:<new-owner>'` or `q='<repo-name>'` | n/a | Enumerate the owner the move pointed at. At `p671` this is also what produced the pass's only new filing — `daisy/MathCATForPython`, found by enumerating `user:daisy` after the `MathCAT` move resolved. |
| Scheduler | [`temporalio/temporal`](https://github.com/temporalio/temporal) | **MIT** | Run it as a durable weekly workflow per client, with the per-dependency verdict as workflow state so a verdict that *changes* raises an event instead of being overwritten. |
| Reporting surface | [`appsmithorg/appsmith`](https://github.com/appsmithorg/appsmith) | **Apache-2.0** | The inventory as a page the client's own procurement or legal reader opens: slug, owner, licence, grant hash, last verdict, **and `owner_changed_on`**. |

**How to wire it — 5 steps.**

1. **Extract the slugs from what the client actually runs**, not from a spreadsheet: the plugin directory, the `requirements`/`package.json`, the Docker images. Keep the **exact case** — GitHub's git and raw channels are case-insensitive and **the search index is not**, and case-folding your own slugs manufactures `422`s that look exactly like renames (`671-O`, and `compose/code/p288-agpl-casefold` registered the same class two years of passes earlier).
2. **Batch the slugs 15 per `search/repositories` call** and record `stargazers_count`, `license.spdx_id`, `pushed_at` for everything that comes back.
3. **For every slug that did not come back, probe it alone**, then probe its owner. Apply the three-way verdict: `≥1` current · `0` live-but-unindexed, date the figure and move on · **`422` + owner `≥1` → owner-change alarm.**
4. **On an alarm, resolve the new address and prove identity before you edit anything**: `git ls-remote --symref` at both names must return the **same `HEAD` sha**, and the grant payload should be **hashed, not counted** — `671-R` has a specimen whose byte count is canonical to the byte while its `sha256` is not, because a prepended blank line and a missing final newline cancel in length. At `p671` the copyright line surviving the move unchanged (*"Copyright (c) 2022 NSoiffer"* under a new org) is what settled the `MathCAT` case.
5. **Treat the result as a governance finding, not a link fix.** Re-read the grant at the new address, record the new owner, and put the question in front of the client: *this dependency is now stewarded by someone else — does that change our support assumption, our relicensing exposure, or our contribution path?*

🔴 **The failure mode this pattern does not fix, stated so it is not oversold.** A `422` whose **owner is also `422`** is not a rename — the owner is simply absent from the search index, and `p671` has a live specimen (`Frederikmh90/RUCAI`). Those addresses are unresolvable on every channel this pattern uses and the honest output is *unmeasured*, not an alarm. 🔵 **And the detector sees owner changes, not archival, not abandonment, not a maintainer quietly handing over commit rights** — it fires on the one event GitHub records as a redirect.

🔵 **Why this is worth a week.** It is five API-call shapes and a table. The thing it buys is that the inventory stops answering a question nobody asked — *"is the link alive?"* — and starts answering the one procurement actually asks: *"is this still the same project, owned by the same people, under the same terms?"*


## P41 — The course factory that ends in a review schedule, not a document (any region; 4–6 weeks) 🆕 new at p672

🔵 **The seam this closes.** This KB has carried the *authoring* half and the *retention* half of self-study on separate shelves for dozens of passes: `T49` established retention as a layer with a choice of objective function, and `p667` filed the scheduling and `.apkg`-writing pieces. What was missing was the join — something that turns raw material into a course **whose output is already shaped like a review schedule**. `p672` filed it.

**The wiring, concretely:**

| Role | Component | Licence | What it does here |
|---|---|---|---|
| Course compiler | [`lowwwbank/anything-to-course`](https://github.com/lowwwbank/anything-to-course) | **MIT** (`1,066 B`, `sha256₁₂ d41346e796d6`, residual 0) | Material (docs, slides, transcripts, a codebase, or a bare topic) → observable capabilities → lessons → practice → checkpoints → **a spaced review plan**. Portable `SKILL.md`; runs on Claude Code, Claude.ai, Codex, Gemini CLI, Cursor |
| Scheduler | FSRS (see `repos/foundations.md`, `T49`) | **BSD-3-Clause** / MIT per implementation | Takes the review plan's items and schedules them. `T49`'s point applies: **the objective function is a client decision** — retention target vs total study time — not a default to inherit |
| Delivery surface | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) + the `.apkg` writer (`p667`, `repos/foundations.md`) | **MIT** | Puts the scheduled deck behind an MCP tool an agent can drive, against the one spaced-repetition client with consumer-scale adoption |
| Tutor loop | [`rizukirr/no-vibe`](https://github.com/rizukirr/no-vibe) | **MIT** (`1,065 B`, `sha256₁₂ 0eddd198e9a1`, residual 0) | Optional second mode: where `anything-to-course` *builds* the course, this one **withholds the artefact** and makes the learner produce it — diagnostic placement, approved roadmap, transfer-task checks |

🔵 **Why the order matters, and it is the whole pattern.** The naïve build is *generate content → bolt on reminders*, and it fails because a review schedule over material that was never decomposed into **observable capabilities** has nothing to schedule except pages. Running the compiler first means the scheduling unit is a capability with a check attached, which is what FSRS can actually act on. **Everything upstream of scheduling and everything downstream of authoring already existed here as permissive parts; the sequence is the contribution.**

⚠️ **Scope honestly.** Every component is MIT and verbatim, and every component is a **single-digit-to-double-digit-star project** (`33★` and `46★` for the two new ones). This is a 4–6 week integration on top of other people's weekend code: budget hardening, not just wiring, and read `agents/top.md`'s standing note that documented permissive prior art is not an adoptable production base. The deliverable a client should pay for is the **capability decomposition and the objective-function choice** — those are durable; the glue is not.

## P42 — Rubric-first assessment: score against a published rubric, gate on a human, and let the model do neither (any region; LATAM and EMEA first; 5–7 weeks) 🆕 new at p672

🔵 **Why this pattern exists now and could not be written before p672.** `agents/top.md` has tracked an *assessment gap* across many passes, and its honest statement has been: permissive, education-specific assessment software exists **only as research artefacts** — the incumbents it names run at `2★`/2 commits and `0★` with the author's grading track frozen. `p672` filed [`maruf009sultan/AIELTS-WRITING`](https://github.com/maruf009sultan/AIELTS-WRITING) (**MIT**, `1,071 B`, `sha256₁₂ dc421f44c477`, residual 0, `23★`, live demo), which is not a better model — it is a better **frame**: it scores against the **four published IELTS criteria** (Task Achievement, Coherence & Cohesion, Lexical Resource, Grammatical Range & Accuracy) rather than a rubric the repository invented.

**The pattern, in order:**

1. **Start from a rubric you did not write.** An externally-published, institution-owned rubric (IELTS bands, a national curriculum's achievement standards, a faculty's own marking scheme). 🔵 **This is the step that makes the system auditable**, because a disagreement becomes *"the score does not match criterion 3"* rather than *"the AI was wrong"* — and under **EU AI Act Annex III** an education scorer must be explainable against something. A model-invented rubric cannot be appealed.
2. **Make the scorer emit per-criterion evidence, not a number.** Band *plus* the span of text that drove it. Reference implementation: the `AIELTS-WRITING` decomposition above; the peer-reviewed alternative for the dialogue case is [`iwangjian/Coding-Tutor`](https://github.com/iwangjian/Coding-Tutor)'s **turn-level verifier** (Apache-2.0, canonical payload, ACL 2025 Findings).
3. **Gate on a human, in the state machine, not in the policy document.** `p653` recorded `littlecookie0722/AI-Teaching-Agent`'s explicit `WAITING_REVIEW` state as the one design worth copying from that layer. **A review step that exists only in a policy PDF is not a control.**
4. **Log the statement, not the session.** Reuse the LATAM statement-log component (`p656`, `intel/market.md`): what was claimed, against which criterion, on which evidence, reviewed by whom.

🟢 **The regional fit, and it is the clearest demand-to-supply match `intel/market.md` records.** UNESCO's severe regional teacher shortage in LATAM makes **teacher time** the binding constraint, and marking written work is its largest single consumer — while the region's governance posture (`87%` of HEIs using AI, `26%` with a formal strategy, `55%` with no AI budget) means the *governance wrapper is the product* as much as the scorer is. In EMEA the same build is sold against **Annex III explainability and post-market surveillance** instead of against teacher hours.

🔴 **The hard constraint, stated so nobody mis-sells this.** `23★`, `0` forks, `0` open issues, pushed `2026-01-10`, single author — and `agents/top.md`'s integrity-layer finding applies with full force: **a research-scale repository must not be carried into a high-stakes deployment.** This pattern is for **formative** assessment — practice, feedback, drafting — where a wrong score costs a student an afternoon, not a qualification. Summative use is a different engagement with a different liability profile, and the honest answer there is still that **the production artefact does not exist yet** and would be built, not adopted. 🔴 **And do not reach for `July-Tea/EssayMate` (`39★`) to fill the gap**: its grant is **CC BY-NC-SA 4.0** — NonCommercial — which bars the derivative entirely, a fact two separate classifiers got wrong (`672-D`, `T53`).

## P43 — The interop spine: put an agent inside the LMS and the SIS without touching either (any region; North America and EMEA public sector first; 6–8 weeks) 🆕 new at p673

**The problem this solves.** Every engagement on this base has the same hidden cost: the agent is the easy part, and **getting it legitimately inside the institution's systems is the expensive part**. `T50` says the system of record is copyleft and barely adopted; the instinct is to replace it, which no client will fund. `T54` says you do not have to — the layer above it is permissive and specification-complete. This pattern is that layer, wired.

**Components — all byte-read permissive, all on this base's shelves:**

| Role | Component | Licence | Why this one |
|---|---|---|---|
| LMS launch + identity + grade return | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | Apache-2.0 | Certified LTI 1.3 / Advantage. Moodle, Canvas, Blackboard, D2L, Open edX all launch it with roles and course context already negotiated. `373★`, pushed `2026-11-05`. |
| Rosters + enrolments | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) (Apache-2.0) or [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) (MIT, ⚠️ 3 yrs stale) | Apache-2.0 / MIT | OneRoster 1.2 **in front of** the SIS. The SIS keeps its licence and its vendor; you consume a standard. |
| Learning records | [`openfun/ralph`](https://github.com/openfun/ralph) (MIT) or [`Apereo…/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) (ECL-2.0) | MIT / ECL-2.0 | xAPI statements out of the agent into a real LRS. `ralph` for a light deployment, `OpenLRW` for a warehouse. |
| Assessment items | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | MIT | Agent emits **portable** QTI 3 items, not a vendor's JSON. Zero runtime dependencies. |
| Credentials out | [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | Apache-2.0 | Issue and verify Open Badges against the spec. |
| The agent itself | any row on `agents/top.md` — e.g. [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) (Apache-2.0) for tutoring, [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) (Apache-2.0) for code feedback | Apache-2.0 | Swappable. **That is the point of the spine.** |

**Wiring, in order.**

1. **Stand up `ltijs` as the tool provider.** It owns the LTI handshake and the platform registration. Do this first: it is what makes everything downstream *attributable to a real student in a real course* rather than to an API key.
2. **Point `ltijs`'s grade-return service at the agent's output**, not the reverse. The LMS gradebook stays the system of record for grades — you never write grades through a side channel.
3. **Put `edfi-oneroster` (or `OneRoster.NET`) beside the SIS, read-only.** Roster in, nothing out. This is the step that avoids the `T50` relicensing trap and the step a client's security review will actually read.
4. **Emit every agent decision as an xAPI statement into `ralph`.** Not logs — statements, with actor, verb, object and the LTI context from step 1. This is what makes step 5 and `P44` possible at all.
5. **Gate every write-back behind a human**, per `P42`. `bruchris/canvas-lms-mcp` is the one row on this base that can write grades and comments from an MCP client; that capability is exactly why it needs the gate.
6. **Emit credentials through `openbadges-validator-core`** only where the programme actually awards something.

**What to tell the client, and what not to promise.** 🟢 The integration surface is free to build on and **standards-certified**, so it survives an LMS or SIS migration — which is the real sales argument, because every institution has lived through one. 🔴 These components are **thinly maintained** (`OneRoster.NET` three years stale, `OpenLRW` ~14 months, `openbadges-validator-core` ~12): fork them, pin them, and **put their maintenance in the estimate**. 🔴 Byte-read every grant yourself at the real default ref before shipping — `T55`, and note four of this layer's repositories default to `master`/`develop`/`development`/`dev`, so a tool reading `main` reports *no licence*.

**Regional fit.** **North America** first: the NC/Maryland procurement calendar on `intel/market.md` names the **data**, and this pattern is a data-interface deliverable with a statutory driver. **EMEA** second: the same spine is the Annex III evidence trail (see `P44`). **LATAM**: `ltijs` is itself Brazilian-built (UFMA/UNA-SUS) — the reference is local. **APAC**: fits TEQSA's per-provider action plans.

## P44 — Prove the intervention worked, or stop claiming it did (any region; EMEA first as AI Act evidence; 4–6 weeks on top of P43) 🆕 new at p673

**The problem this solves.** Every AI-in-education claim this base has read for `25` passes is **someone's self-report**. `T49` wanted a real measurement layer; `p673` found it. This pattern turns "the tutor improved outcomes" from a marketing sentence into a defensible number — and in EMEA it does double duty as the artefact an Annex III high-risk deployment is **required** to produce.

**Components:**

| Role | Component | Licence |
|---|---|---|
| Randomised assignment + outcome collection **inside a live course** | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | Apache-2.0 (`11,323 B`, residual `0`) |
| LTI launch context (which student, which course, which condition) | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | Apache-2.0 |
| Statement store the outcomes are read from | [`openfun/ralph`](https://github.com/openfun/ralph) | MIT |
| Curriculum ground truth the outcome is measured *against* | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) (Brazil) — or the local equivalent | MIT |
| Judge, where the outcome is open-ended | [`OpenEuroLLM/JudgeArena`](https://github.com/OpenEuroLLM/JudgeArena) | Apache-2.0 |

**Wiring.**

1. **Install `terracotta` into the LMS over LTI** and define the experiment **before** the agent ships: two conditions, the outcome measure, the consent text. An experiment designed after the result is not an experiment.
2. **Let `terracotta` assign the condition; let the agent read it from the LTI launch** via `ltijs`. The agent must not choose its own condition — that is the whole discipline.
3. **Collect outcomes into `ralph`** as xAPI, keyed to the `terracotta` condition and the LTI context.
4. **Score against a published rubric**, per `P42` — and where the rubric is a national curriculum, score against `bncc-dados`'s `1,721` provenance-tracked objectives rather than a model's recollection of them. Where the outcome is open-ended, swap judges with `JudgeArena` and report **judge disagreement**, not a single score.
5. **Report the counterfactual, including when it is null.** A pattern that cannot return "no effect" is not a measurement pattern.

**Why this sells.** 🟢 **EMEA:** the Omnibus moved stand-alone Annex III duties to **`2027-12-02`** — a fixed window, not relief. Logging, human oversight and data governance must be *evidenced*, and this is that evidence, assembled from permissive European public-sector components (`ralph` is France Université Numérique's). 🟢 **LATAM:** UNESCO IESALC measured `87%` adoption against `26%` with any framework, `55%` with no budget, public universities at **`4%`** — the binding constraint is governance capacity at near-zero spend, and every component here is licence-free to build on. 🟢 **North America:** an RCT result is what survives a school-board meeting. 🔴 **The honest caveat:** `terracotta`'s placement was **refused** by this base — it is widely associated with a US university, but its own files name no country, and an association this base cannot read first-hand is not a placement. Its *function* is verified by byte read and its licence is Apache-2.0 at residual `0`; its *provenance claim* is not this KB's to make.

## P45 — The grant evidence pack: ship a licence claim a client's counsel can re-derive, byte for byte (any region; EMEA and North America public sector first; 2–3 weeks, then standing) 🆕 new at p674

**The problem this solves.** A studio hands over an open-source-derived deliverable with a dependency licence report. The client's counsel asks the only question that matters: *how do I know this is the grant that was actually in the tree?* An SPDX label does not answer it — `p672`/`p673` measured that index labels on this base's own corpus are **wrong in both directions**. And p674 found that even a *byte count plus digest* does not answer it if the figures were captured rather than measured: the `Opetushallitus/compleap` cell was internally consistent — size and hash agreed with each other — and **both described bytes the repository does not serve.**

**What to wire together.** Every piece below was exercised at p674 in a session where `api.github.com` and the GitHub HTML page were both `403`, so the recipe is deliberately built from channels that survive that.

| Layer | Use | Grant |
|---|---|---|
| Default-ref resolution | `git ls-remote --symref <url> HEAD` | — |
| Payload fetch | `raw.githubusercontent.com/<repo>/<ref>/<path>` | — |
| Payload measure | `wc -c < file` and `sha256sum file` — **from the file, never from `$(…)`** | — |
| Tree enumeration | `git clone --filter=blob:none --no-checkout --depth 1` + `ls-tree -r` | — |
| Package cross-check | `pypi.org/pypi/<name>/json`; the npm/Maven equivalents | — |
| Spaced-repetition / LMS targets as applicable | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) MIT · [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) Apache-2.0 | MIT / Apache-2.0 |

**How to build it.**

1. **Resolve the ref before anything else.** `ls-remote --symref` — never hardcode `main`. This base has measured real default branches of `develop` (`oppia`), `master` (`blend-ed/openedx-mcp`, `numbas`), `2.12`, `mobile` and `v31.0.00`. A payload read at the wrong ref is evidence about nothing.
2. **Fetch the payload to a FILE, and measure the file.** This is the whole of `P834`. `body=$(curl …)` strips the payload's *entire* trailing newline run, so both the size and the digest come out describing different bytes. p674 found `5` such cells on this base's own shelves, with runs of `1` and `2`.
3. **Record size *and* digest, and treat a size alone as unresolved.** `11 357 B` is simultaneously the `apache/.github` canonical and the **stripped** size of the `apache.org` canonical (`11 358 B`). Only the digest separates them: `58d1e17ffe51` versus `cfc7749b96f6`. Pin both in the pack as reference rows so a reviewer can tell a correct cell from an artefact.
4. **Enumerate the tree before asserting an absence.** A filename ladder can only *find* a grant; sustaining "there is no licence" needs the full tree. And enumerate before asserting a *presence* too — p674 cleared the new `instructional_agents-skills` row by confirming all four advertised skills ship as `SKILL.md` **plus** `scripts/*.py`, rather than trusting the README's table.
5. **Add a package channel for every component that publishes one.** It is an *independent* grant statement and a liveness signal. p674's decisive case: [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) is **absent from GitHub's search index** (`repo:` → `total_count 0` while `org:` returns its own siblings), so its stars and metadata are unreachable — but PyPI `instructional-agents` v1.1.1 supplies `MIT`, the OSI classifier, and 3 releases. Without the package channel that component looks dead; with it, it is verified.
6. **Run the arithmetic as a control, both signs.** Re-measure a cell you believe is correct, not only ones you suspect. p674's first arm flagged `OpenOLAT`, `campfirium/foliole` and `towardsai/ai-tutor-app` and **withdrew all three**: each publishes the correct figure and *also quotes `11 357` as the canonical it was measured against. A check that pairs any address with any number on the same line cannot tell a claim from a reference — **scope the audit to the cell.**
7. **Hand over the script, not just the table.** The deliverable is a re-derivation: counsel runs it and gets the same digests, or the pack has failed.

**Effort.** 2–3 weeks to build and calibrate against components whose grants are already known (calibrate *before* trusting: p674 validated its instrument against six of this base's published cells — `11 408`, `1 065`, `1 531`, `7 048`, `1 105`, `1 067`/`4e085d826a64` — and reproduced all six, with the `P171` GNU control clean at both signs). Then it runs per release.

**Why this sells.** 🟢 **EMEA:** Article 50 transparency duties have applied since `2026-08-02` and stand-alone Annex III education duties land `2027-12-02`; both need provenance a deployer can evidence, and a re-derivable pack is that evidence. 🟢 **North America:** procurement in state and district education increasingly asks for software provenance, and an SPDX label is not provenance. 🟡 **APAC:** the specific trap this pack catches is live here — `haolpku/Omni-Edu`'s Apache-2.0 grant **covers code only** and explicitly does not grant the model weights, which a repository-level licence report will miss entirely. 🔵 **LATAM:** `87%` of regional universities use AI and only `26%` have a formal strategy; a pack that answers the licence question in writing removes the cheapest reason for a procurement to stall.

⚠️ **What this pattern does NOT do, stated because the house style requires it.** A payload answers the **copyright** question only. Whether a system may be *called* — a third party's Terms of Use, an API's acceptable-use policy, the access-rights gate — is invisible to every probe here. This base has measured an MIT component that is unshippable for exactly that reason.

## P46 — Automated writing evaluation you may actually sell: train on the one corpus whose holder granted commercial use (North America first; 7–9 weeks) 🆕 new at p675

**Why this pattern exists now and could not have been written at p674.** This base held every education writing corpus as non-commercial. 🟢 **PERSUADE is not, at either release, read at the author's own repositories** — and that correction is what makes this sellable rather than merely demonstrable.

```
marked scripts ──► feature + rubric layer ──► calibration ──► human gate ──► feedback to teacher
                            │
                   ┌────────┴─────────┐
                   │                  │
   scrosseye/persuade_corpus_2.0   microsoft/LLM-Rubric (MIT, 45★)
   🟢 CC BY 4.0 — 25k+ US grade     calibrate rubric outputs against
   6–12 argumentative essays,       THIS client's human raters
   human-scored, per-element
   proficiency + demographics
                   │
   wwrwbs/AI_AWE (ArguLens, Apache-2.0) — education-specific, grade-INDEPENDENT decomposition
                   │
   learning-commons-org/evaluators (🟢 MIT code ONLY) — feedback-quality + text-complexity evaluators
                   │
   littlecookie0722/AI-Teaching-Agent (MIT) — WAITING_REVIEW gate, no auto-publish
```

**Wiring it, in the order that keeps the licence clean.**
1. **Fetch PERSUADE 2.0 from the holder's links and record the attribution line in the repo that will ship.** CC BY 4.0 obliges attribution, a licence link and an indication of changes — three lines in a `DATA_NOTICE.md`, and the obligation is discharged. Cite Crossley, Baffour, Tian, Franklin, Benner & Boser (2024), *Assessing Writing* 61.
2. **Take `ArguLens` for the decomposition, not for the weights.** Its grade-independent features are the portable part; its own notice documents the bias inherited from a US middle-school corpus, so that notice travels into your model card verbatim rather than being rediscovered in UAT.
3. **Use `learning-commons-org/evaluators`' MIT *code* and nothing else from it.** 🔴 Its prompts are `CC BY 4.0` (usable, attribute) but its **annotated** CLEAR and PERSUADE editions are `CC BY-NC-SA 4.0` — and `SA` reaches a fine-tune. Ship the evaluator harness; leave the annotated corpora on their site.
4. **Calibrate on the client's raters with `LLM-Rubric` before any accuracy claim.** The number that sells is agreement with *this* client's markers, not a benchmark score.
5. **Gate every output on a human with `AI-Teaching-Agent`'s `WAITING_REVIEW` state.** No auto-publish, ever.

🔴 **The three hard lines, and they are licence lines rather than engineering ones.**
- 🔴 **`scrosseye/CLEAR-Corpus` must not enter the training set, the eval set that ships, or any fine-tune.** `CC BY-NC-SA 4.0` at source — confirmed at the holder, not inferred. Use it only as a held-out yardstick inside the client's own estate, and say so in writing.
- 🔴 **Neither corpus has a licence file.** The grant is a sentence in a README. 🟢 So the evidence pack from **P45** is not optional here: pin the README commit (`5bdbad1175d1` / `dbf1cf0df30b`), the byte count and the digest, because a README can be edited and a `404` on `LICENSE` gives counsel nothing to re-derive.
- 🔴 **PERSUADE 2.0 is English, US, grades 6–12.** 🔵 It is **not** a Spanish or Portuguese writing corpus, and the construct does not transfer. A LATAM engagement starts from the client's own marked scripts aligned to `bncc-dev/bncc-dados` (MIT) — longer, and the more defensible deal.

⚠ **Scope it as assistive feedback to a teacher, never as a score of record.** EU AI Act Annex III makes evaluating learning outcomes high-risk; Vietnam's `Decision 33/2026/QD-TTg` triggers on results serving as *"the official basis"* for assessment; several US state policies bar AI from grading outright. 🟢 **Feedback-to-a-teacher sits outside all three triggers and is where the budget is anyway.**

## P47 — The offline-first classroom stack: AI that works where the connection does not (LATAM public sector, APAC rural, Sub-Saharan Africa; 6–8 weeks to a deployable appliance) 🆕 new at p676

**Why this pattern exists now and could not have been written at p675.** For six consecutive passes the APAC and LATAM legs of `intel/market.md` have reported the same thing: the binding constraint on classroom AI in those regions is **infrastructure and connectivity**, not model quality. This base had no answer — every pattern on this page assumed an API call leaves the building. `p676` filed the substrate: **`Crosstalk-Solutions/project-nomad`** (Apache-2.0, `42,342★`), an offline-first knowledge and education *server*, plus **`learningequality/studio`** (MIT), the authoring half of the Kolibri stack whose player this base has carried since `p10`.

```
   ┌──────────────── ONE APPLIANCE, NO UPLINK REQUIRED ────────────────┐
   │                                                                   │
   │  Crosstalk-Solutions/project-nomad   🟢 Apache-2.0  42,342★       │
   │  offline Wikipedia · offline maps (ProtoMaps) · knowledge library │
   │                              │                                    │
   │         ┌────────────────────┼────────────────────┐               │
   │         ▼                    ▼                    ▼               │
   │  ollama (MIT)         learningequality/     academico-sis/        │
   │  Qwen3-8B or          kolibri + studio      academico             │
   │  Llama-3.1-8B         🟢 MIT  (`unstable`)  🟢 MIT  411★          │
   │  on-device            curriculum channels   enrolment · grades    │
   │  inference            aligned to the        attendance · billing  │
   │         │             LOCAL curriculum      (multi-tenant SIS)    │
   │         └────────────────────┬────────────────────┘               │
   │                              ▼                                    │
   │              kolibri-design-system  🟡 MIT (package.json)         │
   │              low-bandwidth accessible UI, $50-tablet-grade        │
   └───────────────────────────────────────────────────────────────────┘
                                  │
                   syncs opportunistically, when a link exists
                                  ▼
                   ralph (MIT, xAPI LRS) ──► openSTEF-style reporting
                   the ministry's dashboard, fed in batches not streams
```

**Wiring, concretely.**
1. **`project-nomad` is the host, not a component.** Install it on the appliance (a mini-PC or a Pi-class box with an SSD). It already ships the offline corpora, the web server and the service management; do not rebuild that layer.
2. **`ollama` alongside it, same box**, serving one 7–8B instruct model. This is the only decision with a hardware consequence: budget 8–12 GB RAM for the model and keep the context short. The tutor is *not* going to be as good as a frontier model and the pattern does not need it to be — its job is explanation and question generation against material that is already on disk.
3. **`learningequality/studio` off-box, during the build phase.** Curriculum alignment is editorial work done once, by the client's own teachers, against the local curriculum — Brazil's BNCC (`bncc-dev/bncc-pacotes`, MIT + CC BY 4.0, filed `p676`), a provincial standard, a ministry framework. The output is a published Kolibri channel, which is a file. 🔴 **Studio's default branch is `unstable`** — pin a commit, do not track the branch.
4. **`academico-sis/academico` as the system of record on the same appliance.** This is what `T60` buys you: the SIS is **MIT**, so enrolment, attendance and grades live *inside* the tenant model, and the AI layer reads them directly instead of through an adapter in front of a GPL core. At ministry scale you would instead use `P43`'s interop spine in front of the incumbent SIS — that is the `T54` answer and it is the right one *there*.
5. **`ralph` for the sync boundary.** Record xAPI statements locally; ship them when a link appears. The LRS is the only component that must tolerate hours of disconnection and then a burst, which is what it was built for.

**What to tell the client, and what not to promise.** 🟢 This deploys and it keeps working through an outage, which is the thing every cloud pilot in these regions fails at. 🔴 **Do not promise frontier-model tutoring quality** — an 8B model on-device is good at explaining material in front of it and bad at open-ended reasoning, and a pilot sold on the former succeeds while one sold on the latter does not. 🔵 **The licence story is clean end to end**: Apache-2.0 host, MIT model runner, MIT SIS, MIT curriculum packages — **no copyleft anywhere in the stack**, which is unusual enough on this page to be worth putting in the proposal.

**Estimate.** 6–8 weeks to a deployable, reproducible appliance image: 1–2 weeks appliance + model sizing and burn-in, 2–3 weeks curriculum channel authoring with the client's teachers (the long pole, and it is *their* time more than yours), 1–2 weeks SIS tenancy and data migration, 1 week sync and reporting. Then per-site imaging is hours, not weeks.


## P48 — Turn the lecture archive you already have into the thing people asked for: searchable, cited, answerable video (EMEA and North America higher education; 5–7 weeks) 🆕 new at p676

**Why this pattern exists now.** Universities recorded everything from 2020 onward and can find none of it. `p676` filed **`opencast/opencast`** (ECL-2.0, `509★`) — the open platform that already owns lecture capture, encoding, publishing and distribution at institutional scale, with Moodle, Open edX, Canvas and Brightspace integrations in place. The AI work is not building a video platform; it is attaching to the one the client is already running.

```
  Opencast (🟢 ECL-2.0, branch `develop`)
  capture ──► encode ──► publish ──► distribute
     │            │           │
     │            │           └──► existing LMS integration, UNCHANGED
     │            │
     │            └──► media + the schedule/series METADATA
     │                 (course, term, lecturer, date — already correct,
     │                  because Opencast scheduled the recording)
     ▼
  whisper.cpp or faster-whisper  🟢 MIT / Apache-2.0
  transcript + word-level timestamps
     │
     ▼
  segment on the transcript, not on fixed windows
  (topic shift ≈ slide change; keep the timestamp range)
     │
     ▼
  qdrant  🟢 Apache-2.0        ◄── embed segment + its Opencast metadata
     │
     ▼
  answer layer: retrieve segments ──► cite "Lecture 7, 24:13"
     │                                 and DEEP-LINK into Opencast's player
     ▼
  ralph  🟢 MIT (xAPI LRS) ──► which questions, which lectures, which gaps
                               ──► back to the lecturer as a weekly report
```

**Wiring, concretely.**
1. **Read Opencast's metadata, do not re-derive it.** The series and episode records already carry course, term, lecturer and date, because Opencast scheduled the capture. Every "AI video search" project that starts from a folder of `.mp4` files spends its first three weeks reconstructing metadata that exists. 🔴 **Checkout `develop`** — Opencast's default branch is not `main`, and a build script that assumes otherwise fails silently.
2. **Transcribe with word-level timestamps.** The timestamp is the whole product: an answer that cannot deep-link back into the player is a worse version of the LMS search the client already dislikes.
3. **Segment on topic shift, not on a fixed window.** A 50-minute lecture is 6–12 topics; fixed 30-second chunks split definitions in half and retrieve badly.
4. **Cite, always, with a deep link.** This is the single feature that decides whether lecturers endorse or resist the tool: a cited answer is reviewable, so a wrong one is a bug report rather than an argument about AI.
5. **Close the loop with xAPI.** Questions asked against Lecture 7 are the most direct signal a lecturer has ever had about which fifteen minutes of their teaching did not land. Deliver it as a weekly report to the lecturer and **not** to their head of department — `intel/market.md`'s EMEA leg has flagged for several passes that evaluation-adjacent framing is what stalls these deployments, and under the EU AI Act anything touching **student evaluation** is Annex III high-risk (duties from **2027-12-02**). 🟢 **A tool that reports to the lecturer about their own lecture is not evaluating a student**, and keeping it that way is a design constraint, not a disclaimer.

**Licence note.** 🟢 **ECL-2.0 is Apache-2.0 with the patent grant narrowed to the contributor's own contributions** — permissive, OSI-approved, and the licence the education sector wrote for itself. Globant may build and ship a commercial derivative. The rest of the stack is MIT/Apache-2.0. **No copyleft in this pattern either**, which is why Opencast rather than a Moodle plugin is the attachment point.

**Estimate.** 5–7 weeks: 1 week Opencast integration and metadata extraction, 1–2 weeks transcription at archive scale (GPU-bound; this is the cost line — price it against the hours of video, not the number of courses), 1–2 weeks segmentation and retrieval tuning, 1 week the answer-and-citation UI, 1 week the lecturer report. 🔵 **Pilot on one department's single term first** — archive-wide transcription before anyone has validated the retrieval quality is the most common way this pattern burns its budget.


## P49 — The classroom that watches itself, on hardware the institution owns (EMEA data-residency, APAC rural, Sub-Saharan Africa; 7–9 weeks to a deployable appliance) 🆕 new at p677

**The gap it fills.** Every classroom-analytics pitch in this sector — attendance, participation, engagement, session summaries, lecture capture — has had to send audio and video to a hosted API. In an EMEA public-sector tender, a Gulf private-school group under KHDA guidance, or any Annex III assessment scoping, **that single architectural fact loses the deal before the pedagogy is discussed**, and the offline-first programmes this base tracks across Sub-Saharan Africa (`agents/trending.md` `677-I`) cannot use it at all. `P47` built an offline *delivery* appliance; **P49 is the offline *observation* appliance**, and until p677 this base had no permissive component for it.

### The parts — all verified, all on the shelves

| Role | Component | Licence | Where filed |
|---|---|---|---|
| Multimodal classroom pipeline + **hardware benchmarking** | [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | **Apache-2.0** (`11,351 B`, `3f17cff4210f`) | `repos/foundations.md` 🆕 p677 |
| Local inference runtime | `ollama/ollama` (or OpenVINO directly, bundled above) | **MIT** | `repos/foundations.md` |
| Offline content + learner shell | `learningequality/kolibri` | **MIT** | `repos/foundations.md` |
| Synchronous classroom client (when the room is also remote) | [`netless-io/flat`](https://github.com/netless-io/flat) | **MIT** (`1,062 B`, `8fa1566550df`) | `verticals/solutions.md` 🆕 p677 |
| Launch from the incumbent LMS / record the evidence | `Cvmcosta/ltijs` (LTI 1.3) + `yetanalytics/lrsql` (xAPI) | **Apache-2.0** / **Apache-2.0** | `repos/foundations.md` |
| Curriculum grounding (England) | [`oaknational/oak-open-curriculum-ecosystem`](https://github.com/oaknational/oak-open-curriculum-ecosystem) | **MIT** (file spelled `LICENCE`) | `repos/foundations.md` 🆕 p677 |

### How it wires together

1. **Weeks 1–2 — benchmark before you quote.** Run the suite's **own benchmarking tools** on two or three candidate boxes (CPU-only, integrated GPU, NPU) against the client's real room audio. 🔵 **This is the step no other pattern in this base can perform, and it is the one that decides the margin:** the deliverable of week 2 is a hardware bill of materials with measured throughput, not an estimate.
2. **Weeks 3–5 — stand up Smart Classroom on-premise.** ASR plus speaker diarization for the session transcript; multi-camera pose detection and student re-identification only if the client's DPIA permits it — **default them off.** Summarisation, mind-map and session-report generation run locally through OpenVINO. Nothing leaves the building.
3. **Weeks 5–7 — the evidence spine, reused from `P17`/`P43`.** Launch the teacher-facing report from the incumbent LMS over **LTI 1.3**; write every observation as **xAPI** statements into `lrsql`. 🔵 **The statement log is the deliverable the buyer's counsel reads**, and it is what turns "AI watched the class" into an auditable record with a retention policy.
4. **Weeks 7–9 — harden.** The suite's README says **reference and demonstration, explicitly not production**: this is where the engagement's real work sits — auth, multi-tenancy, upgrade path, model pinning, failure modes when a camera drops. **Quote it as hardening, not as integration.**

### 🔴 What this pattern does not claim

- ⚠️ **`2★`, no release, no tag.** `education-ai-suite` is adopt-and-harden, and a client must be told that the upstream is a vendor reference project, not a maintained product. Pin a commit.
- 🔴 **Pose detection and re-identification of students are the highest-risk features in this entire base.** Under the EU AI Act, **emotion recognition in educational settings has been prohibited since February 2025**, and behavioural inference sits adjacent to it; Vietnam's **Decision No. 33/2026/QD-TTg** names behavioural analysis in education as high-risk. **Ship the audio pipeline by default and treat video as a separately scoped, separately consented module** — or do not ship it.
- ⚠️ **`netless-io/flat` is MIT but builds against Agora's commercial RTC SDK.** The client is free; the transport is metered. Price the minutes or plan a WebRTC substitution.
- 🔵 **Curriculum grounding is national.** The Oak row serves England. For Brazil use `bncc-dev/bncc-pacotes` (MIT code + CC BY 4.0 data), for Germany `telekom/ki-in-schulen`. **There is no supranational curriculum source and this pattern does not pretend otherwise.**

## P50 — Publish a shelf a client's engineer can trust: the filing gate (any region; 1 week, then a standing gate) 🆕 new at p677

**Why this is a pattern and not an internal chore.** Globant hands clients curated technology shelves — *these are the permissive bases, these are the licences, build here*. p677 measured what happens without a filing gate: on this base's own shelves, **`6` of `11` rows a provenance ledger recorded as published were absent**, one address was claimed-as-filed by **two passes `25` days apart**, and **`4` duplicate rows** inflated two headline counts, one pair carrying **opposite recommendations for the same repository**. 🔵 **Every one of those defects would have reached a client as either a missing option or contradictory advice, and none is a research failure.** The research was right. See `T61`, `T62`.

### The gate — four checks, no network, seconds to run

| # | Check | Implementation | What it catches |
|---|---|---|---|
| 1 | **Filing assertion** | For every *“filed to” / “promoted to”* cell, `grep -iF <address> <path the cell names>` | A row the ledger says is shelved and is not. Caught all `7` p677 defects |
| 2 | **Distinct-subject count** | Extract the address from the **subject column only**; compare row count to distinct count | Duplicate rows, which a row-count re-derivation cannot see |
| 3 | **Cell arity** | Every row's `\|`-count against its own table header | A stray `\|` that silently eats a cell — `p674` lost `1,190` characters of published rationale this way |
| 4 | **Contradiction scan** | For any duplicated subject, diff the recommendation cells | Two rows, one repository, opposite advice — the `frappe/lms` case |

### How to wire it

1. **Day 1–2** — implement as a pre-commit hook over the shelf files. Checks 1–3 are pure text; check 4 flags for human review rather than deciding. 🔵 **Case-insensitive address matching is not optional**: a naive check reports `autolab/autolab` missing when the shelf says `autolab/Autolab`, and a gate with false positives gets switched off.
2. **Day 3–4** — run it over the existing corpus and **triage, do not auto-fix.** A missing row may be an unfiled finding worth filing (as at p677, where all six were legitimate and were filed) or a row deliberately refused. **The gate reports; a human dispositions.**
3. **Day 5, then standing** — fail the build on checks 1 and 3, warn on 2 and 4.

### 🔵 Why a client buys this

- **It is the cheapest credibility artefact in a knowledge-engineering engagement.** A shelf whose every provenance claim is machine-verified against its own target is a different product from one that merely cites sources well.
- 🔵 **It generalises to any RAG or knowledge pipeline that writes both an index and a corpus** — the index is an assertion about the corpus, and almost nobody asserts it. The failure mode is identical: retrieval cites a document the corpus does not contain.
- ⚠️ **It does not improve research quality and must not be sold as if it did.** It closes the gap between what was found and what was published — which, on the evidence of p677, is where this class of system actually loses its accuracy.

## P51 — Ship a branded mobile learning app over the institution's existing LMS, without inheriting its copyleft (North America and EMEA higher education; 6–8 weeks) 🆕 new at p678

**The client situation.** A university or consortium already runs **Open edX** and will not replace it. They want a branded mobile app with an AI study assistant. Legal has previously blocked mobile work on the grounds that Open edX is `AGPL-3.0` and a distributed app would have to carry the same obligation.

**Why the objection does not apply to the app.** p678 byte-read both official clients' grants at their real default refs: **[`openedx/openedx-app-android`](https://github.com/openedx/openedx-app-android) and [`openedx/openedx-app-ios`](https://github.com/openedx/openedx-app-ios) are `Apache-2.0`** — `11,356 B`, digest `43070e2d4e532684`, **byte-identical to each other**, so this is one deliberate decision by the owner across both platforms. The AGPL obligation stays with the **server the institution already operates and does not distribute**.

**The build.**

1. **Fork the clients, not the platform.** `openedx-app-android` (Kotlin) and `openedx-app-ios` (Swift). You are rebranding an app that `62` and `34` other forks have already rebranded — `f/★ = 1.632` and `1.097`, ranks `#3` and `#5` on this base's deploy-per-institution census. **Read those forks before starting; the customisation seams are already worn.**
2. **Leave the LMS alone.** The apps speak the existing Open edX APIs. No server patch, so no AGPL-triggering distribution and no upgrade debt.
3. **Add the assistant behind MCP, not in the app.** Stand up the study assistant as an MCP server beside the LMS and have the app call it. For the Moodle-flavoured equivalent of this seam this base holds [`Faixiang/Moodle-MCP`](https://github.com/Faixiang/Moodle-MCP) (MIT, `193★`) and [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) (MIT); for a vendor-authored RAG+MCP reference to adapt, [`moodlehq/wiki-rag`](https://github.com/moodlehq/wiki-rag) (**BSD-3-Clause**, Moodle HQ's own) — ⚠️ **it ingests MediaWiki, not courses**, so take its MCP/RAG structure, not its ingest path.
4. **If the tool must launch from inside the LMS too, go through LTI.** `1EdTech/LTI-Tool-Provider-Library-PHP` or `basiclti-util-java` (both `Apache-2.0`, from the body that owns the spec) as the **reference to port** — ⚠️ last pushed `2018` and `2022`. For live LTI 1.3 use [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT, `f/★ 0.609`).

**Licence posture to hand legal, in one line.** App binary: `Apache-2.0` fork, commercially licensable. Server: untouched `AGPL-3.0`, operated not distributed. Assistant: your code behind an MCP boundary. **Three grants, three deliverables, no commingling.**

🔴 **Do not skip:** byte-read the grant of **every** repository you ship code from, at its real default ref. `678-F` is the counter-example in the same family — `THU-MAIC/MAIC-UI` (`184★`) is the UI of a permissively granted classroom and has **no grant payload at all**.

## P52 — The offline-first classroom appliance, now buildable end to end from permissive parts (LATAM public sector, APAC rural, Sub-Saharan Africa; 5–7 weeks to a deployable image) 🆕 new at p678

**What changed at p678.** This base has recommended Kolibri as the offline LMS since `p1`, but held **none of its delivery surface** — so `P47` described an appliance without naming how it reaches a device. Both halves are now shelved under MIT, grants byte-read:

| Layer | Repo | Grant (read at p678) | Note |
|---|---|---|---|
| Server / content | Kolibri core (on the verticals shelf) | MIT | the existing recommendation |
| **Tablet** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) `@develop:platforms/android` | 🟢 **MIT** `1,097 B` sha256₁₂ `3c056b34a476` (monorepo root, re-read p692) | 🔴 **ADDRESS CORRECTED AT p692.** [`kolibri-installer-android`](https://github.com/learningequality/kolibri-installer-android) reports **`archived=true`**; its README's first line reads *“This repository has been archived! The Android app has been moved to the Kolibri monorepo”*. The replacement path was probed and returns `200`. 🔴 **real default ref is still `develop`** — a pipeline guessing `main` reads `404` and reports *no licence* |
| **Desktop** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) `@develop:platforms/desktop-app` | 🟢 **MIT** `1,097 B` sha256₁₂ `3c056b34a476` (monorepo root, re-read p692) | Windows / macOS / Linux. 🔴 **ADDRESS CORRECTED AT p692** — [`kolibri-app`](https://github.com/learningequality/kolibri-app) is `archived=true` and states the move itself; path probed `200` |
| School admin | [`biprodas/school-erp`](https://github.com/biprodas/school-erp) | 🟢 **MIT** `1,069 B` `d9beb4f20b37203f` | Next.js + NestJS + Postgres 17 + Redis, `51★ / 37` forks |
| Local inference | `ollama` (on the foundations shelf) | MIT | keeps the appliance offline |

**The build.**

1. **Start from the installer path, not the installer repository — corrected at p692.** 🔴 **The instruction this pattern carried from p678 to p691 — “Fork `kolibri-installer-android` at `develop` and `kolibri-app`” — forks two archived trees.** Both were consolidated into the Kolibri monorepo. Fork **[`learningequality/kolibri`](https://github.com/learningequality/kolibri) at `develop`** and build from **`platforms/android`** (APK) and **`platforms/desktop-app`** (desktop bundle); both paths were probed at p692 and return `200`. The grant is unchanged — the monorepo root is MIT (`1,097 B`, sha256₁₂ `3c056b34a476`) — so the commercial-redistribution conclusion this pattern rests on survives the move. 🔵 **Estimate impact: none on licence, small and real on build engineering** — a monorepo fork pulls the whole platform tree rather than a thin installer repo, and the build is invoked from a subdirectory, so budget the first APK as integration work rather than as a clone. These are the artefacts that produce an APK and a desktop bundle; everything else is content and configuration.
2. **Put the model on the box.** `ollama` with a small instruct model, bound to localhost. **No uplink in the data path** — which is simultaneously the connectivity answer and the strongest EMEA/LATAM data-residency answer: the data never leaves the building.
3. **Wire the administration layer only if the client asks for it.** `biprodas/school-erp` covers admissions, academics, people, finance and reporting on a TypeScript stack most studio teams already staff. ⚠️ Single maintainer — **scope a fork, not a vendor relationship.**
4. **Ship a signed image plus a sync window.** The appliance runs standalone; content and gradebook deltas reconcile when a connection appears.

**Why this sells where it sells.** LATAM's measured position is **`87%` of institutions using AI against `26%` with any formal framework** (UNESCO IESALC / UNU-IAS, ~`200` institutions in `19` countries) — demand without a control layer. An appliance whose data path is local is the shortest route to a governable deployment, and in EMEA the Annex III high-risk deadline for stand-alone education systems now sits at **`2027-12-02`**, which is schedule, not blocker.

🔵 **Pair with `P47`**, which this pattern completes rather than replaces: `P47` set the architecture, P52 names the parts and their verified grants.

🔴 **Known gap, stated:** none of these repositories' own files name a jurisdiction, and all eight owner accounts have no `location` set (`678-I`). The regional fit above is argued from **where the deployment constraint binds**, not from provenance — weaker evidence, labelled as such.

## P55 — The technical-academy curriculum spine: three permissive curricula, three regions, three languages, one assessment layer (CS faculties, bootcamps, graduate-conversion programmes; 4–6 weeks to a running cohort) 🆕 new at p680

**What changed at p680.** This base's learn-to-code layer held `21` addresses and had recorded two defects in it: **no member placeable in North America**, and **no non-English member at all**. Both are closed. The three curricula below were filed at p680 with their grants byte-read against canonical MIT (`1,079 B`, `2ec9e6e61ed8`), and **all three operative bodies are verbatim**:

| Role | Repo | Grant (read at p680) | Region | `f/★` | Note |
|---|---|---|---|--:|---|
| **Algorithms / CS fundamentals** | [`BedirT/ACM-ICPC-Preparation`](https://github.com/BedirT/ACM-ICPC-Preparation) | 🟢 **MIT** `1,074 B` `9908478c70da` | North America | `0.274` | 🔴 default ref is **`master`**; `2,546★`, maintained since 2016 |
| **AI / ML, French, with a .NET track** | [`jsboige/CoursIA`](https://github.com/jsboige/CoursIA) | 🟢 **MIT** `1,075 B` `d5305ab1bbe1` | EMEA | 🔴 **`9.563`** | Jupyter; **C#/Python twins** on .NET Interactive, plus Lean 4 |
| **Agent construction, Chinese** | [`hyyhf/agent-book-code`](https://github.com/hyyhf/agent-book-code) | 🟢 **MIT** `1,080 B` `35c4b4f6b5b9` | APAC | `0.153` | 🔴 copyright line names a *different* project (`680-G`) |
| **Integrity / similarity** | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | MIT (already on this base) | EMEA | — | 🔴 **the only live permissive option in its layer** (`680-B`) 🔵 *(region detail, moved out of the closed-vocabulary `Region` column at p682: Ghent University)* |
| **Autograding** | [`anubislms/anubis`](https://github.com/anubislms/anubis) | MIT (foundations shelf, p677) | Global | — | distributed LMS for automated CS assignment grading 🔵 *(region detail, moved out of the closed-vocabulary `Region` column at p682: unplaced)* |
| **Retention** | `fsrs4anki` / `fsrs-rs` (foundations shelf) 🔵 *(region detail, moved out of the closed-vocabulary `Region` column at p682: unplaced)* | MIT / BSD-3-Clause | Global | — | scheduling, per `P35` |

**The build.**

1. **Pick the spine by the cohort's language, not by star count.** English/algorithms → `ACM-ICPC-Preparation`. French/AI with enterprise .NET exposure → `CoursIA`. Chinese/agent engineering → `agent-book-code`. All three are MIT, so all three can be forked, rebranded and extended under a client's own terms; none needs a licence conversation.
2. **Fork at the real default ref.** `ACM-ICPC-Preparation` is on **`master`**. A pipeline that assumes `main` reads `404` and reports *no licence* — the defect class `P52` also carries.
3. **Run the cohort on an incumbent LMS over LTI, never fork the platform** — `Pattern I` on `verticals/solutions.md`. The curricula above are *content*; they do not want to be a platform.
4. **Add `anubis` for autograding and `dolos` for similarity before the first assignment is due**, not after. 🔴 **Scope the integrity layer explicitly:** `dolos` is the only live permissive tool in that layer, and if the client rejects it the alternatives are GPL-3.0 (`jplag/JPlag`) or building. Say so in the SOW rather than discovering it in week five.
5. **Close the loop with retention.** Export the cohort's wrong answers into an FSRS schedule (`P35`) so the curriculum keeps teaching after the module ends.

**How to read adoption on these three, because the usual instrument is wrong here.** `CoursIA` shows `16★` and **`153` forks** — `f/★ = 9.563`, nine times this base's census maximum. That is a **class running on it right now**, one fork per learner, and a `stars:>40` filter drops it outright. 🔵 **Rank curricula by forks, platforms by `f/★` near `1`, and reference material by stars** — see `intel/trends.md` **T71**.

🔴 **Known gap, stated:** no LATAM-origin curriculum is available for this pattern. Nine topic heads were swept at p680, six of them for the first time, and **not one novel LATAM-origin address was placeable** (`680-B`). A LATAM cohort runs this pattern on the EMEA or North America spine, translated — which is a real cost to put in the estimate, not a detail.

## P56 — Courseware from the open-textbook corpus: a permissive pipeline over a copyleft publishing stack (EMEA and North America higher education, LATAM ministries on budget; 5–7 weeks to a running course) 🆕 new at p681

**The ask this answers.** An institution or ministry wants course material it owns, aligned to its own syllabus, without licensing a publisher's content and without paying per-seat for a frontier model to hallucinate a textbook. It already has access to the open-textbook corpus; what it does not have is a way to get from *9,601 books on 28 networks* to *a taught, assessed course*.

**Why this is newly buildable at p681, and it is a licence argument before it is an engineering one.** The publishing layer is copyleft — `pressbooks/pressbooks` is **GPL-3.0**, `PreTeXtBook/pretext` is **GPL-2-or-3** — so the obvious move (fork a platform, brand it) carries source disclosure. The pipeline below never forks either one. See `intel/trends.md` **T74**.

### The parts, each verified at p681

| role | project | licence, byte-read | note |
|---|---|---|---|
| corpus reader | [`johnnyrobot/pressbooks-cli`](https://github.com/johnnyrobot/pressbooks-cli) | 🟢 **MIT** `1,073 B` sha256₁₂ `48c3921fa1fc` | 28 networks / `9,601` books; **no account, key or token**; text, JSON, HTML, PDF, EPUB out |
| catalogue lookup | [`8enSmith/mcp-open-library`](https://github.com/8enSmith/mcp-open-library) | 🟢 **MIT** `1,065 B` sha256₁₂ `44e077ec4d7e` | `100★`; **a book catalogue, not OER** — use it to resolve editions and authors, never as a licence check |
| teaching + progression | [`ChrisWhiteSr/teach-skill`](https://github.com/ChrisWhiteSr/teach-skill) | 🟢 **MIT** `1,234 B` sha256₁₂ `2c14f42cf1a6`, upstream `mattpocock/skills` MIT `1,068 B` sha256₁₂ `0e7ac423bf2c` | mastery-learning loop with **placement before teaching**; course content is plain Markdown course-files |
| teacher-facing artefacts | [`dh2211/edu-agents`](https://github.com/dh2211/edu-agents) | 🟢 **MIT** `1,082 B` sha256₁₂ `7eb4eb733011` | lesson plans, worksheets, quizzes with answer keys, rubrics, differentiation — **validator fails any skill with no `Guardrails` section** |
| authoring / export | [`PreTeXtBook/pretext`](https://github.com/PreTeXtBook/pretext) | 🔴 **GPL-2-or-3** | 🔵 **run it, never derive from it** — single-source XML → HTML + PDF + EPUB across a process boundary |
| retention | [`open-spaced-repetition/fsrs-rs`](https://github.com/open-spaced-repetition/fsrs-rs) | 🟢 permissive (held, `P35`) | schedule what the cohort got wrong |
| delivery | incumbent LMS over **LTI** (`Pattern I`, `verticals/solutions.md`) | — | 🔴 **never fork the LMS** |

### Wiring it

1. **Select, do not generate.** `pressbooks-cli` enumerates and caches the networks, then searches **locally** — the upstream `search` parameter is accepted and discarded, so enumeration must come first. Pull candidate chapters as JSON. 🔵 **This is the step that makes the pattern cheap:** the content already exists and is openly licensed; the model's job is mapping and adaptation, not authorship.
2. **Record the per-book licence at selection time, as data.** Open licensing is **per book**, not per network, and nothing in the toolchain checks it. Store the licence string beside every extracted chapter in the same row as its source URL and retrieval date. 🔴 **Do not use `mcp-open-library` for this** — Open Library indexes commercial books and carries no OER signal. Treat a missing licence as excluded, not as permitted.
3. **Map to the client's syllabus**, then author the gaps in **PreTeXt XML** — one source, and HTML, PDF and EPUB fall out of the same build. Invoke `pretext` as a CLI from your own code. 🔴 **Nothing of yours may link into it**; the process boundary is the licence boundary.
4. **Generate the teaching surface with `edu-agents`** — objectives, unit and lesson plans, worksheets, quizzes with answer keys, rubrics, differentiation. 🟢 **Keep the `Guardrails` validator in CI**: it is the only mechanical safety floor in this stack, and it is the reason this library is in the pipeline rather than a larger one.
5. **Place, then teach, with `teach-skill`.** Run its browser onboarding app to place each learner *before* the first lesson, then drive the mastery loop over the course-files produced in step 4. 🔵 **Placement is the step that separates this from a chatbot over a PDF**, and it is the step most tutoring agents on `agents/top.md` skip.
6. **Deliver over the institution's existing LMS via LTI** (`P51`), and **close the loop with FSRS** (`P35`) on every item the cohort got wrong.
7. **Instrument progression from the start**, not at the end: `P44`'s evidence shape is what lets the client claim the course worked, and in EMEA it is also the Annex III evidence they will need.

### What to tell the client before the SOW is signed

🔴 **Four of the seven parts are at `0★`.** `pressbooks-cli`, `teach-skill` and `edu-agents` are `0★ / 0 forks`, and `edu-agents` has **twenty minutes** between its `created_at` and its `pushed_at`. **This pattern is a permissive, verified *starting point*, not an adoptable product.** Price hardening — tests, error handling, upgrade path, an owner — as the main line of the estimate, and say so.

🔴 **The access layer is a measured gap, which is both the risk and the reason to go now.** No MCP server or agent bridge exists for **LibreTexts, OpenStax, the Open Textbook Library or OER Commons** — all four probed at p681, all four nil (`repos/foundations.md` `681-H`). So `pressbooks-cli` is the only permissive corpus reader in the field: it is a single point of failure *and* the only one of these parts that solves something genuinely hard. Its README documents four hostile properties of the live service it works around. **Contribute upstream rather than re-implementing**; an institution-specific fork of the network list is the one fork worth owning.

🟢 **Where it sells first, and why.** **EMEA higher education** before the `2027-12-02` Annex III date, because the pipeline produces its own provenance trail — every chapter carries its source URL, licence and retrieval date, which is most of what a conformity file wants about training and content inputs. **North America** on the open-textbook affordability brief, where the per-student saving is already a budget line. 🟢 **LATAM ministries on the strongest fit of the three:** UNESCO IESALC measured **55% of institutions with no AI budget at all**, and this pattern's marginal cost per course is corpus access plus adaptation — not per-seat inference over a generated textbook. Pair it with `P47`/`P52` to run on institution-owned hardware.

🔴 **Known gap, stated:** the corpus is overwhelmingly English. `pressbooks-cli`'s bundled networks are North American and European, and no Spanish- or Portuguese-language OER network was located this pass. **For a LATAM engagement, step 1 is a network-discovery exercise, not a search** — and the bundled-list mechanism is the right place to put the answer.


## P57 — The Moodle agent with the write surface split by audience: one read-only server for learners, one draft-only server for graders, one gated server for registrars (any region running Moodle; 3–4 weeks to a pilot cohort) 🆕 new at p682

**What changed at p682.** This base held three agent-reachable surfaces into Moodle and **all three could write**, which meant `P42`'s human gate had to sit in front of every one of them — including the learner-facing question-answering use case, where a gate makes no sense and a write tool is pure liability. [`fabioov/moodle-mcp`](https://github.com/fabioov/moodle-mcp) (**MIT**, filed at p682) closes that hole: **every tool is read-only by construction**, so there is nothing to gate. The pattern is the resulting split — *the audience determines which server is mounted, and the server's tool surface enforces it, not a prompt.*

### The parts — all on these shelves, all byte-read

| Role | Repo | Grant | Write surface | Region |
|---|---|---|---|---|
| **Learner-facing Q&A** | [`fabioov/moodle-mcp`](https://github.com/fabioov/moodle-mcp) | 🟢 **MIT** `1,107 B` sha256₁₂ `4649f967df1b` | 🟢 **none — read-only by construction** (`get_site_info`, `list_courses`, `get_course_contents`, assignments, deadlines, grades, forums, notifications) | Global |
| **Grader-facing** | [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) | 🟢 **MIT** | 🟡 **drafts only** — fetches submissions, writes **unreleased** grade drafts (`7` tools, stdio); a human releases | Global |
| **Registrar / admin** | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) (`45★`) | 🟢 **MIT** | 🔴 **full write** — courses, students, assignments, quizzes. **`P42` gate mandatory** | Global |
| **Grading judgement + calibration** | [`yasserhegazy/lab-grader-skill`](https://github.com/yasserhegazy/lab-grader-skill) | 🟢 **MIT** | builds the rubric from the assignment and **waits for approval before grading anyone**; 5-student pilot to calibrate; emits `grades.csv` + a **Moodle import CSV** | EMEA |
| **Grounding on Moodle's own docs** | [`moodlehq/wiki-rag`](https://github.com/moodlehq/wiki-rag) (`53★`) | 🟢 **BSD-3-Clause** | read-only; MediaWiki → Milvus, exposed as **MCP + OpenAI-compatible endpoints**. **Owned by Moodle HQ** | Global |
| **The platform** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** | — | Global |

### How it wires together

1. **Mount by audience, and let the tool surface be the permission model.** Students get `fabioov/moodle-mcp` and nothing else — no write tool exists in the process, so no prompt, system message or jailbreak can cause a grade to move. Graders get `toshieji/moodle-grading-mcp`, whose worst case is an **unreleased draft**. Registrars get `peancor/moodle-mcp-server` behind the `P42` gate. 🔵 **This is the whole point: three trust levels implemented as three binaries, not as three instructions.** A single full-write server with "please only read" in the prompt is the same system with the safety property deleted.
2. **Keep the model off the rubric.** `lab-grader-skill` derives the rubric from the assignment file and **blocks until a human approves it**, then grades a **5-student pilot** so the grader can calibrate before anything runs at scale. Grade the cohort only after the pilot is signed off.
3. **Escalate on confidence, not uniformly.** Grade in parallel with cheap models; route only flagged, low-confidence and calibration-spot-check cases to a stronger model. This is what makes a 300-student cohort affordable.
4. **Write back through the CSV, not through the API, for the first term.** `lab-grader-skill` emits a **Moodle import CSV**; importing it is a human action with a diff the registrar can read. Promote to `toshieji`'s draft-write path once the institution trusts the numbers, and to `peancor`'s full-write path only if it ever genuinely needs to.
5. **Ground answers in Moodle's own documentation with `wiki-rag`** — and note *who owns it*: Moodle HQ. For "how does this institution's Moodle behave" questions, that beats a general model guess, and it is **BSD-3-Clause**, so it composes freely.
6. **Stay outside the GPL boundary.** Every component above is a **separate process talking to Moodle over its web-services API** — the `T74` shape. None of it links Moodle's code, so none of it inherits **GPL-3.0**. 🔴 **The boundary breaks the moment you fork Moodle or write a plugin that runs in-process**: a plugin is a derivative work, and the MIT client you built becomes a GPL obligation. If the pilot's conclusion is "we need a Moodle plugin", that is a licensing decision for the client's counsel, not a sprint item.

### 🔴 What this pattern does not claim

- **Adoption.** `fabioov/moodle-mcp` is at **`0★ / 0 forks`, `12` commits**. It is filed for the *shape* of its tool surface, not for traction, and a client should read it end to end before mounting it — which is cheap precisely because it is small and read-only. `peancor/moodle-mcp-server` was last pushed **`2026-02-22`** and is **~8 months stale**; verify it against the institution's Moodle version before quoting it.
- **That read-only means safe.** It means **no writes**. A read-only server still exposes grades, submissions and forum content to whatever model is behind it — so the data-protection question (where the tokens live, which model sees student records, what the EU AI Act Article 50 transparency duty requires from **`2026-08-02`**) is unchanged and must be answered separately.
- **That the grading is accurate.** `lab-grader-skill`'s AI-authorship and copying detectors emit **evidence and a question to ask the student**, not verdicts. Under the EU AI Act, assessment of learning outcomes is **Annex III high-risk** (obligations now **`2027-12-02`**), and anything that looks like automated academic-integrity judgement needs a human decision-maker on the record.

## P58 — The narrated algorithm: a permissive visualisation engine under a tutoring agent, with the animation as the assessed artefact (CS faculties and bootcamps, all four regions; 3–4 weeks to a graded module) 🆕 new at p683

**The gap this closes.** This base's tutoring tier *explains* algorithms in prose. Nothing on the shelves *draws* one step-by-step under a permissive grant, so every CS-faculty engagement has so far either shipped text or pulled in a proprietary visualiser.

**The parts, all byte-verified at p683:**

| role | repo | grant | why this one |
|---|---|---|---|
| visualisation + stepping engine | [`vkaravir/JSAV`](https://github.com/vkaravir/JSAV) | 🟢 MIT (`MIT-license.txt`, `1,095 B`, `05e0a5ea02c8`) | array / tree / graph / list primitives, forward **and backward** stepping, and a **grading hook** on interactive exercises. Live since `2011` |
| tutor that narrates and questions | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | already the shelf's tutoring default; supplies the persistent learner model |
| teacher-corpus constraint | [`JuneYaooo/teacher-to-skills`](https://github.com/JuneYaooo/teacher-to-skills) | 🟢 Apache-2.0 (`11,358 B`, `cfc7749b96f6`) | binds the narration to the faculty's **own** lecture notes, so the explanation matches the course, not the model's prior |
| retention scheduling | [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | 🟢 MIT (`1,079 B`, `021bff58ad26`) | schedules the re-visit of a *step* the learner got wrong, not of a flashcard |
| code-level feedback | [`pedal-edu/pedal`](https://github.com/pedal-edu/pedal) | 🟢 MIT (`1,103 B`, `ffaa010382b0`) | analyses the student's Python submission, so the trace and the code are graded together |

**How they wire together — the one non-obvious join.** JSAV's exercise grader emits a **step sequence** (the learner's model of the algorithm), not a score. Feed that sequence, not a grade, to DeepTutor as the learner-model update; feed the *first divergent step* to `py-fsrs` as the item to reschedule; and feed `pedal`'s analysis of the submitted code to the same tutor turn so the agent can say *"your trace is right and your loop bound is off by one"* — which is two different failures that a single score collapses into one.

**Build order (3–4 weeks).** Week 1: JSAV exercise + grading hook over one algorithm, no agent — confirm the step sequence is capturable. Week 2: `teacher-to-skills` over the faculty's lecture notes; DeepTutor narrating from that corpus only. Week 3: `py-fsrs` on divergent steps + `pedal` on submissions. Week 4: a graded module with the animation as the artefact of record.

🔴 **Two cautions that are licence and provenance facts, not opinions.** (`1`) JSAV's grant is at `MIT-license.txt` — a path a fixed-case probe reports as *no grant* (`683-B`); a client's own OSS review will hit this, so hand them the path and the digest. (`2`) JSAV carries **`35` open issues on `116★`** and its grant names two holders in two institutions — fine for MIT, but there is no single counterparty for a warranty.

🔵 **Region fit.** All four. The content is mathematics, so no localisation of the *algorithm* is needed — only of the narration, which is where `teacher-to-skills` (measured APAC, `55.7 %` CJK) already does the work.

## P59 — The permissive institutional platform play: replace a GPL university LMS derivative with a fork-and-own permissive one (EMEA universities, LATAM ministries; 6–8 weeks to a branded pilot) 🆕 new at p683

**The gap this closes, and it is a licence gap rather than a feature gap.** Until p683 this base's institutional platform tier was **copyleft in every region that matters for a branded derivative**: Moodle (GPL-3.0), Chamilo (GPL-2.0), ILIAS (GPL-3.0), Open edX (AGPL-3.0), RosarioSIS (GPL-2.0). A client who wants a *branded, closed* derivative of the platform itself — not a plugin beside it — had no permissive starting point on this page. Two rows filed at p683 change that.

| region | platform | grant | the state it is in |
|---|---|---|---|
| **EMEA** | [`MaMpf-HD/mampf`](https://github.com/MaMpf-HD/mampf) | 🟢 **MIT** (`1,088 B`, `c88be2cc0844`) | running at Universität Heidelberg (`mampf.mathi.uni-heidelberg.de`); Rails + PostgreSQL; media graph, quizzes, submissions, tutorial groups |
| **LATAM** | [`NewSchoolApp/newschool-backend`](https://github.com/NewSchoolApp/newschool-backend) | 🟢 **Apache-2.0** (`11,357 B`, `c71d239df917`) | NestJS + MySQL behind an OpenAPI/Swagger contract; course delivery, gamification, certificates |
| **either, as the integration seam** | [`hei-school/hei-admin-api`](https://github.com/hei-school/hei-admin-api) | 🟢 **MIT** (`1,098 B`, `dfe4c34bee60`) | OpenAPI-first school administration — students, fees, attendance, results |

**The agentic layer goes on top unchanged**, because all three expose a contract rather than a UI: the shelf's Moodle/Canvas MCP pattern (`P57`) transfers directly — one read-only surface for learners, one draft-only surface for graders, one gated surface for registrars.

**Build order (6–8 weeks).** Weeks 1–2: stand the platform up and **re-derive its data model from the running instance**, not from the README. Weeks 3–4: the runtime migration — this is the real cost and it is known in advance, see the cautions. Weeks 5–6: MCP surfaces + the agent layer. Weeks 7–8: branding, the client's SSO, and an accessibility pass.

🔴 **Price these three before quoting, because each is a measured fact and not a risk.** (`1`) **NewSchool runs on Node 12, which is end-of-life** — the migration is week one of the real work, not a stretch goal. (`2`) **MaMpf carries `85` open issues on `43★`**: this is fork-and-own; upstream will not carry a client's roadmap. (`3`) **MaMpf's default ref is `next` and HEI's is `preprod`** — CI, licence scanners and dependency bots that assume `main` will silently read nothing (`683-C`).

🔵 **Why a client buys this over a Moodle plugin.** A Moodle derivative that ships to a ministry as *their* platform triggers GPL source disclosure on the derivative. These do not. That is the entire argument, and it is worth more than any feature on the comparison grid — but it only holds if the fork stays clear of GPL plugins, so the dependency audit is part of week one.

## P60 — Assessment integrity a regulator will accept: three decidable controls instead of an AI detector (EMEA and APAC compliance-driven, LATAM at zero infrastructure cost, North America on Canvas/Gradescope; 4–6 weeks to a graded pilot) 🆕 new at p684

**The demand is statutory on four continents** — Ofqual (UK, March 2026), UK DfE product safety standards (January 2026), EU Annex III assessment obligations binding `2027-12-02`, Vietnam's Decision `33/2026/QD-TTg` naming automated assessment high-risk, TEQSA's mandatory generative-AI risk plans in Australia, and UNESCO IESALC's `87 %`-adoption / `26 %`-strategy split across Latin America.

🔴 **Do not build or resell an AI-text detector.** `T79`: the evasion side is already productised (`Cam3L1/ghost-skill` targets GPTZero, Turnitin, Originality.ai, ZeroGPT and CopyLeaks by name), a classifier is obsolete the week it ships, and — decisively for a regulated buyer — a probability score **cannot be evidenced**. Every control below returns a fact a human can re-check.

### The three controls, and what each one decides

| # | Control | Repo | Licence | Decides | Cannot be gamed by |
|---|---|---|---|---|---|
| `1` | **Structural code similarity** | [`OSLL/code-plagiarism`](https://github.com/OSLL/code-plagiarism) `codeplag` v0.6.5 | 🟢 MIT (`1,086 B`) | Whether two submissions share an **AST**, for Python 3 / C / C++ | Renaming, reformatting, reordering, comment rewriting |
| `2` | **Citation existence** | [`DSL4-Digital/RefExists`](https://github.com/DSL4-Digital/RefExists) | 🟢 MIT (`1,076 B`) | Whether each reference **resolves** on Crossref / arXiv / Semantic Scholar, and whether it is **retracted** | Nothing — a DOI resolves or it does not |
| `3` | **Authorship by examination** | [`pisan-labs/code-viva`](https://github.com/pisan-labs/code-viva) | 🟢 MIT (`1,067 B`) | Whether the student can answer questions about **their own** functions and names | Any text generator, because the artefact is the student's live answer |

🟢 **Optional fourth, deterministic half only:** [`sunilgentyala/academicguard`](https://github.com/sunilgentyala/academicguard) (MIT, `1,082 B`) for **IEEE / Elsevier / ACM / IET / BCS** style conformance. Ship the style checker, **disable its AI-detection module** — it is the component that reintroduces the problem this pattern exists to avoid, and style conformance sells to a research office as a service rather than as an accusation.

🟢 **Optional fifth, for research-integrity offices and APAC data-sovereignty buyers:** [`WuP1ao0/ManuSift`](https://github.com/WuP1ao0/ManuSift) (MIT, `1,077 B`) — 52 offline detectors over paper PDFs and Source Data tables (image reuse, table-fabrication fingerprints, statistical inconsistency), exposed over **MCP** and requiring **no API key**, so nothing leaves the institution.

### Wiring it to the LMS the client already runs

All three controls consume files, not APIs, which is why this composes without touching the LMS licence boundary (`T27`, `T16`):

- **North America / anywhere on Canvas or Gradescope** — `code-viva` imports a Gradescope export (`submission_metadata.yml`), a Canvas *Download submissions* bundle, or a GitHub Classroom assignment by org and repo directly. For an agentic loop over Canvas, front it with [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) or [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp); for grader-side drafting, [`jlouisbru/Canvas-grading-with-AI`](https://github.com/jlouisbru/Canvas-grading-with-AI).
- **Anywhere on Moodle** — apply **P57** unchanged: a read-only MCP server for learners, a **draft-only** server for graders, a gated server for registrars. [`fabioov/moodle-mcp`](https://github.com/fabioov/moodle-mcp) and the Moodle MCP family on `agents/top.md` supply the surface. The integrity verdicts land as grader-visible drafts, **never as an automatic penalty**.
- **Brightspace / D2L institutions** — [`AnonymousOnyx22/brightspace-d2l-mcp`](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) is the only permissive route this base has verified.

### Sequence (4–6 weeks)

1. **Week 1 — the decidable baseline, no AI at all.** Stand up `codeplag` over last term's archived submissions and run `RefExists` over the reference lists of a completed cohort. 🟢 **This step produces the client's first defensible integrity number and uses no LLM**, which is the right order: it establishes a measured baseline before anything generative is introduced, and it is the artefact a regulator or accreditor actually asks for.
2. **Week 2 — the viva loop.** Import one real assignment through `code-viva`, generate orals for a sample cohort, and have two human markers rate question quality. Bots including `github-classroom[bot]` are already excluded upstream; confirm that exclusion against the client's own CI identities before trusting a flag.
3. **Weeks 3–4 — LMS surface and the escalation policy.** Wire whichever MCP route matches the client's LMS, with every verdict written as a **draft for a human marker**. 🔴 **Write the escalation policy before the first production run, not after:** which verdicts auto-close, which open a conversation, which reach a misconduct panel, and who sees a false positive first. In the EU this is an Annex III deployer obligation from `2027-12-02`, not a nice-to-have.
4. **Weeks 5–6 — residency and evidence.** For EMEA data-residency and APAC sovereignty buyers, swap any hosted inference for the local-first stack (`T21`) and add `ManuSift`'s offline kernel. Ship an evidence bundle per verdict — AST match pairs, unresolved DOIs, viva transcripts — because the deliverable a regulated institution buys is the **audit trail**, not the score.

### Why it is sellable, in the client's own words

🟢 **It inverts the conversation from suspicion to assurance.** A detector tells a student they are probably guilty and cannot show why. These three tell an institution *this reference does not exist*, *these two files are the same program*, *this student explained their own code* — each one re-checkable by a human and survivable in an appeal.

🟢 **Cost floor is near zero where it needs to be.** `RefExists` is fully client-side with nothing to host and `codeplag` is a PyPI install, so controls `1` and `2` are a complete, deployable deliverable for the `55 %` of LATAM universities with no AI budget line. Controls `3`–`5` are what a funded North American, EMEA or APAC institution adds on top.

⚠️ **Say the maturity out loud in the proposal.** These are `16★`, `2★` and `2★` repositories — `T79` measured `0` live permissive assets above `20★` in this entire category. That is the opportunity (there is nothing to out-licence) and it is the risk (Globant is taking on maintenance). Price the fork-and-own, and vendor the dependencies.

## P61 — The grant-boundary lockfile: pin dependencies by slug **and** payload digest, and scan vendored subtrees 🟢 new at p685

**The problem this solves is not hypothetical, and p685 measured it on this base's own two largest rows.** A bare repository name does not identify a grant. `THU-MAIC/OpenMAIC` is **MIT**; `kolbyzhu5/OpenMAIC` and `ChengZhuo2025/OpenMAIC` are both **AGPL-3.0** with a byte- and hash-identical payload (`34,523 B`, sha256₁₂ `0d96a4ff68ad`). `HKUDS/DeepTutor` is **Apache-2.0**; `rddy/deeptutor` is **MIT**. `patchy631/ai-engineering-hub` is **MIT**; a same-name repository under `SlickbitTechnologies` carries **no grant at all**. A build that resolves a dependency by name — a README instruction saying *"clone OpenMAIC"*, a vendoring script, a model-context tool that searches by name — can put copyleft, or no licence, under a closed deliverable without a single error being raised.

**And the root `LICENSE` is not sufficient on its own.** This base already found that `THU-MAIC/OpenMAIC` vendors `packages/mathml2omml/LICENSE` under **LGPL-3.0-or-later** (`7,652 B`) beneath an MIT root. A root-only check passes that repository and still ships copyleft.

### Components — all verified first-hand at p685

| Role | Component | Grant, pinned by digest |
|---|---|---|
| Classroom agent | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | MIT · `1,065 B` · `ba2525637432` |
| 1:1 tutor | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · `11,408 B` · `cd2f54e1e506` |
| Curriculum | [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) | MIT · `1,066 B` · `93123909818c` |
| Existence oracle | `git ls-remote --symref <url> HEAD` | — |
| Payload oracle | `raw.githubusercontent.com/<slug>/<ref>/LICENSE` | — |

### Wiring

```
grants.lock   (committed, reviewed like any lockfile)
──────────────────────────────────────────────────────
slug                      ref    path                            bytes   sha256_12  spdx
THU-MAIC/OpenMAIC         main   LICENSE                          1065    ba2525637432  MIT
THU-MAIC/OpenMAIC         main   packages/mathml2omml/LICENSE     7652    <pinned>      LGPL-3.0-or-later
HKUDS/DeepTutor           main   LICENSE                         11408    cd2f54e1e506  Apache-2.0
patchy631/ai-engineering-hub main LICENSE                         1066    93123909818c  MIT
```

1. **Resolve existence by slug, never by name.** `git ls-remote --symref https://github.com/<slug> HEAD` returns the real default ref for a live repository and fails loudly for one that does not exist. Every dependency entry is an owner-qualified slug; a bare name is a lint error.
2. **Fetch each pinned path and hash the file, not a shell capture.** Write the payload to a file and hash the file — `sha256sum <file>`, never `$(curl ...)`, which strips the trailing newline and silently produces a different digest (this base burned several passes on exactly that, see `intel/trends.md` **T56**).
3. **Enumerate vendored subtrees, not just the root.** Walk the dependency for every `LICENSE*`, `COPYING*` and `*/LICENSE*` and require each one to be in `grants.lock`. An unpinned grant file appearing in a subtree fails the build — that is the `mathml2omml` case.
4. **Fail on drift in either direction.** A changed digest means the upstream grant was edited; a new path means a subtree arrived. Both are licence events and both require a human.
5. **Gate the deliverable boundary, not the repository.** Copyleft entries in `grants.lock` are allowed to exist — they are allowed only on the far side of a process boundary, per this file's base architecture. The lockfile is what makes that rule checkable instead of aspirational.

### Why a digest and not an SPDX string

`gh api search/repositories` reports `license.spdx_id`, and it is a *classifier's opinion* of the payload. This base has found it wrong in both directions — `NOASSERTION` on a clean Apache-2.0 payload (`thm-mni-ii/feedbacksystem`), and an `11,357`/`11,358 B` pair of Apache-2.0 canonicals that no SPDX string can distinguish. **The digest is the fact; the SPDX string is a label on it.** Pin the fact.

🔴 **One honest limit.** The `raw.githubusercontent.com` oracle returns `404` both for a repository that does not exist and for a file that is simply absent from a live repository — p685 ran that control at both signs. So step 1 is not optional: existence must come from `ls-remote`, and only then does a `404` from step 2 mean *"this repository ships no grant at that path"* rather than *"this repository is not there"*.


---

## P62 — The solver-grounded tutor: let a domain solver be the examiner and the LLM only the narrator (STEM faculties and engineering upskilling, all four regions; 4–6 weeks to a graded module) 🆕 new at p686

**The problem.** Every tutor on this base's agent shelf asks a single model to decide whether the learner is right *and* to explain why. That conflation is the source of the sector's standing objection — a confidently wrong tutor is worse than no tutor — and it is why the one statutorily forced demand in this industry (academic integrity, **T79**) has almost no permissive supply behind it. **Prompting does not fix it**; the examiner and the explainer have to be different components. p686 found two independent permissively-licensed instances of the fix (**T90**), in Go and in CFD, and neither is big enough to adopt as a dependency — so the pattern is the deliverable.

### The wiring

1. **Oracle (decides correctness).** A deterministic domain solver, run first and treated as ground truth. Verified permissive options this base holds: **OpenFOAM** behind [`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server) (Apache-2.0, `10,708 B`, `e0ae7f268ba5`) for fluids/thermal; **KataGo** behind [`wimi321/GoAgent`](https://github.com/wimi321/GoAgent) (MIT, `1,061 B`, `6c9fc83bf6f2`) for sequential decision-making; **SymPy** or a CAS for symbolic algebra; and the autograders in [`inducer/relate`](https://github.com/inducer/relate) (**MIT/X**, `1,145 B`, `66ff89ebf05f`) for numeric and symbolic coursework.
2. **Narrator (never adjudicates).** The LLM receives *the learner's answer, the solver's answer, and the delta* — never the question alone — and is constrained to explaining the delta. **If the solver returns no verdict, the narrator must say so rather than supply one.** This is the whole control, and it is enforced in the prompt contract plus a hard gate that drops any narration emitted without a solver verdict attached.
3. **Delivery surface.** [`inducer/relate`](https://github.com/inducer/relate) (MIT/X) for a university course with versioned content, timed exams and a grade book — **the only permissively-licensed platform on this base's vertical shelf that natively autogrades mathematical work**; or **OpenOlat** (Apache-2.0, `10,982 B`, `6dbc5b605ed0`) where an institutional LMS is required and a closed layer must remain lawful.
4. **Retention (schedules the re-ask).** Every solver verdict is a graded event, so it drives scheduling directly. **Cold start → [`fasiha/ebisu`](https://github.com/fasiha/ebisu)** (Unlicense/public domain, `1,211 B`, `7e12e5df4bae`): Beta posterior over recall, closed-form update, calibrated uncertainty, **no training corpus** — correct for a new course with no review history. **Once logs exist → FSRS** (already held by this base). **TypeScript-only delivery → [`VienDinhCom/supermemo`](https://github.com/VienDinhCom/supermemo)** (MIT, `1,065 B`, `08acbb3df12d`), which is also the honest baseline when the client asks what the AI scheduler is beating.
5. **Evidence (makes it procurable).** Persist `(learner answer, solver verdict, narration, timestamp, model+solver versions)`. That record is what a regulator or accreditor actually asks for, and it is produced as a by-product rather than retrofitted — it satisfies the Maryland-class district-coordinator evidence obligation (North America), a **TEQSA** institutional action plan (APAC), and the accreditation-linked governance UNESCO recommends for LATAM.

### Components — all verified first-hand at p686

| Role | Component | Grant, pinned by digest | Ref |
|---|---|---|---|
| Oracle (CFD) | [`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server) | Apache-2.0 · `10,708 B` · `e0ae7f268ba5` | `main` @ `8d14e2031146` |
| Oracle (sequential play) | [`wimi321/GoAgent`](https://github.com/wimi321/GoAgent) | MIT · `1,061 B` · `6c9fc83bf6f2` | `main` @ `edc6efa15a9a` |
| Oracle + delivery (maths coursework) | [`inducer/relate`](https://github.com/inducer/relate) | MIT/X · `1,145 B` · `66ff89ebf05f` | `main` @ `e201e11b860c` |
| Delivery (institutional LMS) | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 · `10,982 B` · `6dbc5b605ed0` | `master` @ `47e5d30a8323` |
| Retention (cold start) | [`fasiha/ebisu`](https://github.com/fasiha/ebisu) | Unlicense/PD · `1,211 B` · `7e12e5df4bae` | ⚠️ **`gh-pages`** @ `497f87bc59c1` |
| Retention (TS baseline) | [`VienDinhCom/supermemo`](https://github.com/VienDinhCom/supermemo) | MIT · `1,065 B` · `08acbb3df12d` | `master` @ `8093cde2b80d` |

**Every grant above is MIT, MIT/X, Apache-2.0 or public domain — the pattern carries no copyleft and no CC component, so a closed derivative is lawful end to end.** Pin each by payload digest per **P61**, and scan vendored subtrees before shipping.

### 🔴 Honest limits — state these before the pattern is sold

- **It needs a checkable oracle, and most of the curriculum does not have one.** Fluids, mechanics, mathematics, code, symbolic algebra, board games: yes. Essay feedback, language production, history, design: **no**, and no amount of wiring changes that. Scope the engagement to the decidable part of the syllabus and say which part that is.
- **Both reference implementations are small and partly dormant** — GoAgent `58★`, `openfoam-mcp-server` `127★` with last push `2026-01-18` (`10` months, and OpenFOAM's own releases have moved past it). Treat both as **reference implementations of the architecture, not maintained dependencies**; budget for re-implementation against the current solver release.
- **The solver becomes the correctness ceiling.** A mis-specified CFD case produces a confident wrong verdict that the narrator will faithfully explain — the failure mode moves from the model to the case setup, which is *better* because it is inspectable and versionable, but it does not disappear. Review cases as assessment artefacts.
- **`ebisu`'s default ref is `gh-pages`, not `main`.** Any ingest or vendoring step that assumes `main`/`master` reads nothing and fails silently.

## 🆕 P72 — Defensible automated assessment: a grounded generator, a refusal path, and a published attack run against it before delivery 🟢 new at p692

**Who it is for.** A university, examination board or ministry that wants AI in **learner assessment** — which the EU AI Act places in Annex III, with stand-alone high-risk obligations from **2 December 2027** (`T7`, `T15`). The engagement question is never *“can the model grade?”*; it is *“can you show the regulator why this grade stands, and what happens when it cannot?”*

**Why this pattern exists now.** p692 found the three pieces that make this answerable from permissive components, and they had to be found separately — one is a generator that refuses, one is an assessor with a peer-reviewed evaluation, and one is a **public MIT-licensed attack** on exactly this class of system.

| Role | Component | Grant (payload read at p692) | What it contributes |
|---|---|---|---|
| **Course + assessment generator** | [`groundworklms/coursewright`](https://github.com/groundworklms/coursewright) | 🟢 **Apache-2.0** `11,358 B` sha256₁₂ `cfc7749b96f6`, operative body **verbatim** | Objectives + source passages → lesson, pre-test, **parallel-form** post-test, flashcards, scenario, as JSON. Every artefact token-overlap-checked against its source passage; ungrounded pieces return `refused:true` with a reason instead of inventing |
| **Criterion-referenced assessor** | [`ecnu-sea/SEA`](https://github.com/ecnu-sea/SEA) | 🟢 **Apache-2.0** `11,357 B` sha256₁₂ `c71d239df917`, operative body verbatim | Structured review of a written submission against criteria, **EMNLP 2024 Findings**, East China Normal University |
| **Red team (run it before the client does)** | [`Michael-Jiahao-Zhang/game-the-llm-reviewer`](https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer) | 🟢 **MIT** `1,091 B` sha256₁₂ `0f34fd1ee3c1` | Meaning-preserving rewrites that move an LLM assessor's verdict. `219★` — **better known than any defence in the layer** |
| **AI-authorship check** | [`THUROI0787/absent-author`](https://github.com/THUROI0787/absent-author) | 🟢 **MIT** `1,129 B` sha256₁₂ `80141ebabf3b` | Evidence list + skills for submissions no human author stands behind |
| **Human-in-the-loop write gate** | [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp) | 🟢 **MIT** `1,076 B` | Already on [`agents/top.md`](../agents/top.md): `12` read-only tools, `4` local-only, and `3` that write to Canvas, each requiring `confirm=true` |
| **Delivery surface** | Moodle or Open edX (verticals shelf) | 🔴 GPL-3.0 / AGPL-3.0 | Read the copyleft before the integration shape is chosen — plug-in boundary, not a fork |

**The build.**

1. **Make grounding a precondition, not a prompt.** Feed `coursewright` the objectives **each paired with the passage that grounds it**. Its token-overlap check runs before anything ships, so an objective with no supporting passage comes back `refused:true` rather than as a plausible fabricated lesson. **Keep the refusals — they are the artefact the conformity file needs**, because they are the written record of the system declining rather than guessing.
2. **Separate generation from assessment, and keep both auditable.** Generate with `coursewright`, assess with `SEA`. Both are Apache-2.0 with **graded** payloads — the operative body of each was compared normalised against `apache.org`'s own text this pass, not read off a badge (`p676-A`: a badge and a byte count both decided nothing).
3. **Attack your own grader before delivery.** Run the `game-the-llm-reviewer` rewrites against the assessor on a held-out set and **measure the score shift**. A pipeline whose grades move under meaning-preserving rewrites is not defensible under Annex III. This is a one-week task and it is far cheaper than discovering it in a conformity assessment — or in a student appeal.
4. **Never let the model write the grade.** The write boundary is `canvas-grader-mcp`'s shape: proposals are staged locally, and the three tools that post to the LMS each require an explicit `confirm=true`. Annex III wants a human decision-maker; make that a property of the **tool surface**, not of a policy document.
5. **Record what you could not check.** `absent-author` gives authorship *evidence*, not proof. Say so in the deliverable. `T106` is explicit that student-submission integrity still has no permissive supply worth shipping — do not let a research-tier tool be sold as a plagiarism detector.

**Estimate.** `8`–`10` weeks for a single faculty or examination board: `2` weeks on objective/passage ingestion (this is the real work — someone must pair every objective with its source), `2` on the generator and refusal plumbing, `2` on the assessor and rubric calibration, `1` on the red-team run and its report, `2`–`3` on LMS integration and the confirmation gates.

**Regional notes.**
- 🔴 **EMEA** — this is the pattern's home market: the Annex III date is the forcing function, and the refusal path is the deliverable a notified body can read.
- 🔵 **North America** — no equivalent conformity regime; sell it on **appeal defensibility** and on the four US states that in `2026` require district-level AI policy. FERPA governs where submissions and comments are processed.
- 🔵 **APAC** — three of the five components are APAC-origin (`SEA` at ECNU; the research-skill layer is largely Chinese-language). Korea's AI Basic Act (in force `22 Jan 2026`) and Vietnam's AI law (`1 Mar 2026`, with an **18-month education transition**) make the governance story saleable before the EU date lands.
- 🔴 **LATAM** — the measured gap is `87%` of institutions using AI against `26%` with any framework (UNESCO IESALC). **State the translation cost in the estimate rather than hiding it:** `coursewright`'s artefacts are English-structured and `SEA`'s evaluation is English-language, so a Spanish- or Portuguese-language cohort adds a real localisation line item on both the generator's output templates and the assessor's criteria. p692's supply sweep placed **`0`** novel LATAM-origin addresses — a sixth consecutive nil — so assume you are translating, not adopting.

