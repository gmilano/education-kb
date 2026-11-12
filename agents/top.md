---
industry: education
region: Global
updated: 2026-11-12
---

## 🆕 `p798` — **`ACTION p797-E` inverted on its own premise. `p797` found `5` LATAM-origin agents, `0` with a grant, and concluded the constraint was grant hygiene. `p798` gives that claim a denominator and a control: `78.1%` of `73` in-language rows serve no grant — against `60.4%` of `149` on the English leg. The grant gap is real and it is `1.29×`. 🔴 What is categorical is something else entirely: `94.5%` of the in-language population has ZERO stars and the whole population's MAXIMUM is `5`.**

🟢 **`ACTION p797-E` discharged as a measurement and REFRAMED as a recommendation. `ACTION p797-F` discharged (negative).** 🟢 Machine output: [`latam-grant-census`](../evidence/latam-grant-census.2026-11-12-p798.tsv) · [`en-leg-grant-control`](../evidence/en-leg-grant-control.2026-11-12-p798.tsv) · [`candidate-grant-bytes`](../evidence/candidate-grant-bytes.2026-11-12-p798.tsv) · [`mit-clause-identity`](../evidence/mit-clause-identity.2026-11-12-p798.tsv) · 🔴 [`candidate-grant-bytes-UNCORRECTED-v1`](../evidence/candidate-grant-bytes-UNCORRECTED-v1.2026-11-12-p798.tsv).

### 🔴 The correction: `p797` measured a real gap and named the wrong one

🔴 **`p797`'s `5 of 5` was five hand-reached rows with no denominator. `T931` read it as a LATAM pathology. With a control leg it is not one.**

| Measure | 🇪🇸🇧🇷 `es`/`pt` legs | 🌍 `en` control leg | Ratio |
|---|---|---|---|
| Addresses returned | `73` | `149` | — |
| 🔴 **No licence file at all** | 🔴 **`57` · `78.1%`** | 🔴 **`90` · `60.4%`** | 🟡 **`1.29×`** |
| 🟢 Permissive grant | 🟢 `13` · `17.8%` | 🟢 `50` · `33.6%` | `0.53×` |
| Copyleft | `2` · `2.7%` | `6` · `4.0%` | — |
| 🔴 **Zero stars** | 🔴 **`69` · `94.5%`** | `29` · `19.5%` | 🔴 **`4.8×`** |
| 🔴 **Highest star count in the whole population** | 🔴 **`5`** | `4,912` | 🔴 **`982×`** |
| Rows at `≥20` stars | 🔴 **`0`** | `16` | — |

🔵 **Read the two rows that matter together.** 🟢 **An ungranted repository is the DEFAULT for a small, recent education-agent project in either language** — `60.4%` of the English leg has no licence either, so a licence campaign aimed at LATAM is aimed at a property of young repositories, not of a region. 🔴 **The thing that is specific to the in-language population is that none of it has been adopted by anyone.** `94.5%` at zero stars, a ceiling of `5`, and not one row above `20`.

🟢 **So the engagement advice changes, and it changes away from both of the last two passes' conclusions.** 🔴 **`p797` said: start with a licensing conversation.** 🟢 **`p798` says: for a LATAM engagement, take a global permissive base and localise it — and read the in-language repositories as DESIGN EVIDENCE rather than as dependencies.** 🔵 **They are worth reading precisely because nobody starred them: they show what a teacher in the region actually builds when nobody is watching** — and what they build is offline-capable, Moodle-attached, and delivered over a channel the student already has.

### 🔴 `T935` — the `es` leg is not the LATAM leg, and two of this pass's best rows prove it

🔴 **`p797` labelled every `es`-leg find "LATAM-origin". `p798` opened the payloads and two of the strongest are SPANISH.** 🔴 [`danielgalanv/oral-ia`](https://github.com/danielgalanv/oral-ia)'s `NOTICE` names *Universidad Politécnica de Madrid*; [`ANFAIA/SkillNet`](https://github.com/ANFAIA/SkillNet) publishes from `skillnet.es`. 🟢 **Both are EMEA and are placed as EMEA below.**

🔴 **And origin cannot be resolved at scale from this session: `gh api users/{login}` is REFUSED** (*"sessions are bound to their configured repositories"*), as is `gh api repos/{owner}/{repo}`, while `gh api search/*` answers normally. 🔵 **So language is the only origin signal available in bulk, and language is exactly the signal that fails here.** 🟢 **Declared, not papered over: every `es`-leg row below whose payload does not name a country is placed `LATAM?` — a question mark this base has not used before and should use whenever the evidence is a query language rather than a document** → `p798-A`.

### 🟢 `7` rows added — grant byte-verified, blob sha and HEAD commit sha beside every one

🟢 All byte-verified on the blobless-clone channel (`T923`'s rule: `curl -sI` cannot distinguish a live address from an invented one here). 🟢 Recency from `search/repositories`, because `repos/{owner}/{repo}` is refused this session.

| Agent | Repo | Grant (byte-verified) | ★ | Last push | Region | What it is, and why it is here |
|---|---|---|---|---|---|---|
| 🟢 **miyagi** `NEW` | [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) | 🟢 **MIT · `1,078 B` · blob `1998b8260d0e` · HEAD `968d0713f7a3`** | `0` | `2026-11-11` | EMEA 🇪🇸 | 🟢 **The human-in-the-loop requirement, implemented rather than promised.** A teacher's assistant that prepares a subject *with* the teacher and, in their Moodle course, **asks before anything reaches a student**. 🔵 **Every regulator in this base demands a named human decision-maker; this is the first row whose README states the gate as its headline feature** |
| 🟢 **chispa-mcp** `NEW` | [`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp) | 🟢 **MIT · `1,066 B` · blob `a304e1253c64` · HEAD `b8d40f2527cd`** | `0` | `2026-11-12` | LATAM? | 🟢 **An education MCP server with `77` tools that runs with the teacher's own permissions** — stdio, npm-packaged. 🔴 **It is also `p792-D` made concrete: `77` tools over classroom management is the largest education MCP attack surface this base has recorded, and no independent security or data-governance evaluation of ANY education MCP server has been published.** 🔵 Cite the architecture; gate it before it touches a roster |
| 🟢 **oral-ia** `NEW` | [`danielgalanv/oral-ia`](https://github.com/danielgalanv/oral-ia) | 🟢 **Apache-2.0 · `11,358 B` · blob `57bc88a15a0e` · HEAD `c5e433674702`** 🔴 **+ `NOTICE` `571 B` carve-out** | `0` | `2026-11-10` | EMEA 🇪🇸 | 🟢 Local self-study assistant with RAG, built under a Universidad Politécnica de Madrid teaching-AI pilot grant. 🟢 **Its `NOTICE` is the most useful `571` bytes in this pass — see `T936`** |
| 🟡 **asistente-docente-sin-conexion** `NEW` | [`Ignacio-Ghub/asistente-docente-sin-conexion`](https://github.com/Ignacio-Ghub/asistente-docente-sin-conexion) | 🔴 **GPL-3.0 · `35,149 B` · blob `f288702d2fa1` · HEAD `ab739c9765fa`** | `0` | `2026-11-03` | LATAM? | 🟡 **A teacher's assistant that runs with NO INTERNET.** 🔵 **The single most LATAM-shaped design in the census and it is copyleft, so boundary-only** — read the architecture, do not link the code |
| 🟢 **Claw-ED** `NEW` | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | 🟢 **MIT · `1,078 B` · blob `ec5640f4f262` · HEAD `18f2e223cdd1`** | `65` | `2026-09-19` | Global | 🟢 **Highest-starred education-domain row added this pass.** Local-first teaching assistant that starts from the teacher's EXISTING lesson plans and produces lessons they review and edit. 🟢 Ships a `SECURITY.md` and a versioned release (`v9.18.2026.1`); 🟡 self-described Beta |
| 🟢 **SkillNet** `NEW` | [`ANFAIA/SkillNet`](https://github.com/ANFAIA/SkillNet) | 🟢 **Apache-2.0 · `10,758 B` · blob `ac436c04442f` · HEAD `cf2fa524cbd1`** | `24` | `2026-10-15` | EMEA 🇪🇸 | 🟢 Turns an organisation's own material into courses, **grounded** tutors and adaptive interfaces — one person to one organisation. 🔵 The closest thing in this pass to the corporate-L&D shape of an enterprise engagement |
| 🟢 **ai-tutor-app** `NEW` | [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) | 🟢 **Apache-2.0 · `11,386 B` · blob `6903d3d27ad6` · HEAD `7a498edabed9`** | `34` | `2026-10-22` | Global | 🟢 Agentic-RAG tutor over a real course corpus (LangGraph + FastAPI). 🔵 A working reference for *"tutor grounded in OUR curriculum"*, which is the request every engagement opens with |

🟡 **Graded and NOT shelved, with the reason stated:** [`XAIHT/Tlamatini`](https://github.com/XAIHT/Tlamatini) (MIT · `1,062 B` · blob `6d93cdbdf7d0`, ★`15`) — see `T937`, its README asserts a restriction MIT does not grant. [`Fazmin/AILearningGuide`](https://github.com/Fazmin/AILearningGuide) (MIT · `1,081 B`, ★`254`) and [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) (MIT · `1,076 B`, ★`93`) are **learning content, not agents an engagement composes** — recorded in [`agents/trending.md`](trending.md) rather than shelved here. [`Man0dya/Tutor-AI`](https://github.com/Man0dya/Tutor-AI) (Apache-2.0 · `10,251 B`, ★`17`) is sound and undifferentiated against `ai-tutor-app`. [`matheusmontelro/plataforma-agentes-ia`](https://github.com/matheusmontelro/plataforma-agentes-ia) (MIT · `1,073 B`, ★`5`) is the **most-starred in-language row in the entire census** and is a local install guide, which is itself the finding above.

### 🔴 `T936` — the best `571` bytes in this pass: an author carved the CONTENT licence out himself

🔴 **`T916` established that in education the content licence is the half you cannot afford to lose, and that GitHub's classifier silently drops it.** 🟢 **[`danielgalanv/oral-ia`](https://github.com/danielgalanv/oral-ia) does the opposite, unprompted, in `571` bytes:** its `NOTICE` states that the Apache-2.0 grant covers *"el código, las pruebas, las especificaciones y la documentación propios"* and explicitly **does NOT** cover *"el material docente ni los textos de documentos de terceros usados en el piloto"* — which keep their holders' rights — **nor the language models, which have their own licences.**

🟢 **This is the shape this base has been describing for three passes and had never found written down by an author.** 🔵 **It is also a deliverable: an engagement that ships a tutor over a client's curriculum needs exactly this file, and now there is a `571`-byte precedent to copy instead of a lawyer to brief** → [`compose/patterns.md`](../compose/patterns.md) `P798-2`.

### 🔴 `T937` — a fourth place to hide a restriction: the README, under an unmodified MIT

🔴 **`T914` said the restriction can be in a different FILE. `T925` said a different REPOSITORY. [`XAIHT/Tlamatini`](https://github.com/XAIHT/Tlamatini) says it can be in the README, inside an HTML comment, under a byte-canonical MIT grant:** *"Tlamatini Author Banner — do not remove (Angela's name is kept in every build)."*

🔴 **MIT requires the copyright notice to survive in copies of the SOFTWARE. It does not require a banner to survive in every BUILD, and it grants the right to modify.** 🟡 **So the licence and the README disagree, and the README is the one a contributor reads.** 🔵 **Not a refusal — an MIT grant is an MIT grant — but a row where the author's expectation and the author's licence are not the same document, which is the thing to settle in writing before using it in a client deliverable.** 🟢 **This base already owns the instrument for exactly this read: [`compose/code/p1060-readme-vs-payload/`](../compose/code/p1060-readme-vs-payload/), built pre-reset and never pointed at the current shelf** → `p798-B`.

### 🔴 `T938` — `p795-A`'s byte-size band is a regression against `p135`, and the mechanism is the author's name

🔴 **`p795-A` filters MIT grades by byte size, with a canonical band of `1,066`–`1,072 B`. Four MIT payloads measured this pass span `1,062`–`1,096 B` and their clause text is BYTE-IDENTICAL** — md5 `aeb812008e99` over all four once the copyright line is removed:

| Row | Bytes | Copyright line | `p795-A` verdict |
|---|---|---|---|
| [`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp) | `1,066` | `Copyright (c) 2026 jeffercbs` | 🟢 inside band |
| [`XAIHT/Tlamatini`](https://github.com/XAIHT/Tlamatini) | `1,062` | `Copyright (c) 2026 XAIHT` | 🔴 **OUTLIER** |
| [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) | `1,078` | `Copyright (c) 2026 Francisco Vargas Ruiz` | 🔴 **OUTLIER** |
| [`hwl668/Scientific-learning-skills-`](https://github.com/hwl668/Scientific-learning-skills-) | `1,096` | `Copyright (c) 2026 Scientific Learning Skills Contributors` | 🔴 **OUTLIER** |

🔴 **The `34`-byte spread is the length of the copyright holder's name and nothing else. `3` of `4` clean MIT rows are flagged, and the flag rate rises with the length of the author's name.** 🔵 **An instrument that fires more often on `Scientific Learning Skills Contributors` than on `jeffercbs` is measuring names, not riders.**

🟢 **And this base already solved it, `660` passes ago.** 🔴 **[`compose/code/p135-licence-sha-identity/`](../compose/code/p135-licence-sha-identity/) says so in its own README** — *"every real MIT file carries a copyright line the SPDX template leaves as a placeholder, so a real MIT payload NEVER hashes to the canonical MIT text"* — and its `body` normalisation level **removes copyright notices as spans** and reports `TEMPLATE_MATCH`, with `MODIFIED_SUPERSET` for *"MIT + a visible-attribution clause"*, which is precisely the rider class `p795-A` was written to catch. 🔵 **`p795-A` did not improve on `p135`; it replaced an exact instrument with a proxy for it.** 🟢 **The fix is to re-point the filter, not to build a third one** → `p798-C`. 🔴 **Declared: `p135` was READ this pass, not RUN — executing committed repository code is refused in this session, so the four-row identity above is measured by this pass's own command and `p135` is cited from its README and source.**

## 🆕 `p797` — **`ACTION p796-D` discharged on the Spanish and Portuguese legs, and the answer is the opposite of the one five passes assumed: LATAM-origin education agents are NOT hidden behind the English query shape. They exist, they are weeks old — and `5` of `5` serve NO LICENCE. Plus `ACTION p796-A` BUILT after three carries.**

🟢 **`ACTION p796-D` DISCHARGED for `es` + `pt`, and partially for `zh` · `ja` · `ko`** (the East-Asian legs returned policy instruments rather than repositories — see [`intel/market.md`](../intel/market.md)). 🟢 Machine output: [`latam-apac-inlanguage-discovery`](../evidence/latam-apac-inlanguage-discovery.2026-11-12-p797.tsv).

### 🔴 The finding: the supply is real and unshippable

🔴 **Five passes recorded `0` LATAM-origin intake and blamed `T883`, the English-query shape. The in-language leg finds five addresses in one hour. Every one of them is `NOASSERTION` — no licence file, no grant of any kind — and none has more than ONE star.**

| Address | Leg | ★ | Grant | Pushed | 🔴 Verdict |
|---|---|---|---|---|---|
| [`nifalconi/educational-agents`](https://github.com/nifalconi/educational-agents) | 🇪🇸 `es` | `1` | 🔴 **NONE** | `2026-11-10` | 🔴 **REFUSED.** Spanish-first agent library with `es`-LATAM parameter names, out of a *Niñas Pro* course — 🔵 **the most interesting design in the set and the clearest example of the problem** |
| [`giovanayngrid-gk/multiagent-ai-tutor`](https://github.com/giovanayngrid-gk/multiagent-ai-tutor) | 🇧🇷 `pt` | `0` | 🔴 **NONE** | `2026-10-30` | 🔴 **REFUSED.** LangGraph-era stack done right for a constrained budget: LangChain + Llama 3 on local Ollama + Streamlit |
| [`svrodela/curso_agentes_ia`](https://github.com/svrodela/curso_agentes_ia) | 🇪🇸 `es` | `0` | 🔴 **NONE** | `2026-11-08` | 🔴 **REFUSED.** Course material |
| [`comercisandro/RecursoEducativoAbierto`](https://github.com/comercisandro/RecursoEducativoAbierto) | 🇪🇸 `es` | `0` | 🔴 **NONE** | `2026-10-14` | 🔴 **REFUSED.** An *open* educational resource that is not openly licensed |
| [`alesdrobysh/miguelito`](https://github.com/alesdrobysh/miguelito) | 🇪🇸 `es` | `0` | 🔴 **NONE** | `2026-07-08` | 🔴 **REFUSED.** Spanish tutor on Telegram with long-term memory and twice-daily practice prompts — 🔵 **a dosage design in the wild** |

🔵 **What this changes about the LATAM offer.** 🔴 **Discovery was never the constraint.** 🟢 **The constraint is grant hygiene, and it is addressable in a way a supply gap is not:** three of the five were pushed within the last six weeks and have one or zero stars, so an author is reachable and has no incentive to refuse. 🟢 **For a LATAM engagement the move is a licensing conversation with a named author, not a search** — and until one happens, the shippable base stays the global permissive layer this file already holds.

### 🟢 `ACTION p796-A` — the dosage instrument, BUILT

🟢 **Three passes scoped it and none built it. [`compose/code/p797-dosage/`](../compose/code/p797-dosage/) is the smallest honest version:** sessions triggered · accepted · turns per accepted session · practice-days-with-a-turn, over a tutor-agnostic event log, with a one-function Canvas adapter for [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT) and `11` offline controls spanning the four field kinds. 🔴 **Its own first control caught its first defect, and the defect is the industry's:** it took the median over only the students who practised, reading `2.5` where the honest answer is `2`, because it had silently dropped the student who was offered the tutor twice and never took a turn — 🔵 **the student `T907` says dominates the population.** 🟢 **A dosage metric that excludes the zeros measures the engaged, and the engaged were never the question.**

### 🟢 Stars re-measured exactly this pass

| Row | ★ `p797` | Grant | Pushed | |
|---|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **`58,622`** | 🟢 Apache-2.0 | `2026-11-07` | 🔴 **The search channel reported ~`45,224` for the same window — a `-23%` error in a secondary source, and the reason this base re-measures rather than quotes** |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **`43,392`** | 🟢 MIT | `2026-11-12` | 🟢 Pushed the day of this pass |
| [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) | 🟢 **`41,804`** | 🟢 MIT | `2026-11-01` | 🟢 `+3` on `p796`'s `41,801` |
| [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | 🟢 **`933`** | 🔴 GPL-3.0 | `2026-02-20` | 🔴 **`9` months unpushed.** Theory-of-mind tutor; copyleft, so boundary-only |

🟢 **`datawhalechina/hello-agents` surfaced a second time on the `zh` leg and stays REFUSED** — `CC-BY-NC-SA-4.0`, NonCommercial **and** ShareAlike (`p771-B`). 🔵 **No search result mentioned its licence; this base's triage is ahead of the channel that keeps proposing it.**

## 🆕 `p796` — **`ACTION p795-B` discharged, and the licence-FILE count found the pattern it was pointed at plus one it was not: on the rows this base recommends for white-labelling, the permissive grant covers the CODE and the brand assets are carved out separately — `CC BY-ND 2.5` on an LMS logo, a clause-`4` branding rider, an `8,877 B` embedding licence. `4` agents added. `p795-A`, `p795-C` and `p795-F` also discharged.**

🟢 **`ACTION p795-A`, `p795-B`, `p795-C` (for its located target) and `p795-F` all discharged this pass.** 🔴 **`p795-D` NOT done, third carry. `p795-E` and `p795-H` partially addressed. `p794-F`/`T906` still undischargeable from this session.** 🟢 Machine output: [`licence-file-and-grant-block-census`](../evidence/licence-file-and-grant-block-census.2026-11-12-p796.tsv) · [`mit-bsd-bytesize-filter`](../evidence/mit-bsd-bytesize-filter.2026-11-12-p796.tsv) · 🔴 [`licence-block-census-UNCORRECTED-v1`](../evidence/licence-block-census-UNCORRECTED-v1.2026-11-12-p796.tsv).

### 🔴 The pass's headline: the licence that lets you ship the code is not the licence that lets you put the client's name on it

🔴 **`T900` found a branding rider on one row and this base read it as a rider problem. `p796` counted licence FILES across `174` addresses and it is structural — `3` independent instances, every one on a row this base actively recommends** (`T914`):

| Row | Published grade | 🔴 What the second licence file says |
|---|---|---|
| 🔴 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 | 🔴 **`NOTICE.TXT` (`14,412 B`, never opened here): the logo and icons are `CC BY-ND 2.5` — `NoDerivs`** |
| 🔴 [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | 🟢 BSD-3-Clause | 🔴 Clause `4` bars altering the branding (`T900`); 🆕 **a third file, `LICENSE_HISTORY`, carries TWO grants (MIT + BSD)** |
| 🔴 [`metabase/metabase`](https://github.com/metabase/metabase) | 🔴 AGPL-3.0 | 🔴 **`4` licence files, `1` OSI grant. The embedding carve-out is `8,877 B` with NO recognised grant** |

🔵 **Grading the root `LICENSE` alone finds none of the three.** 🟢 **For an engagement whose deliverable is a white-labelled platform, the brand layer is a separate licence question and must be graded as one.**

### 🔴 `T915`/`T916` — `5` rows serve more than one grant, and a classifier that answers anyway drops the CONTENT licence

🟢 **`5` of `174` rows carry more than one grant; `3` of the `5` carry them inside a SINGLE file**, so no file count can see them: `odoo` (LGPL-3.0 + full GPL-3.0, `43,529 B`), `rrule` (its own BSD + bundled `python-dateutil`'s), `uchit/mcp-regulated-ai-compliance` (Apache-2.0 + CC), plus `open-webui` (`3` grants / `3` files) and `kumaken-1` (MIT code + CC BY 4.0 content).

🔴 **`3` of the `5` are `NOASSERTION` in GitHub's SPDX against a `15.6%` base rate — a ~`3.9×` enrichment, so abstention is a cheap screen.** 🔴 **The `2` GitHub DID grade are both code/content splits, and in BOTH it reported the CODE licence and silently dropped the CONTENT licence** — `kumaken-1` → `MIT` (dropping CC BY 4.0 on every quest text and printable), `uchit` → `Apache-2.0` (dropping the CC grant). 🔵 **In education that is the wrong half to lose: the content licence governs the curriculum.**

### 🟢 `4` rows added — byte-verified, star-exact, placed

| Agent | Repo | Licence (byte-verified) | ★ | Last push | Region | What it is |
|---|---|---|---|---|---|---|
| 🟢 **ai-engineering-hub** `NEW` | [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) | 🟢 **MIT · `1,066 B`** | `41,801` | `2026-11-01` | Global | 🟢 **Highest-starred row added here in several passes.** Runnable agent/RAG curricula — the teaching corpus for an engagement's own engineers |
| 🟢 **AI-Teaching-Agent** `NEW` | [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | 🟢 **MIT · `1,069 B`** | `0` | `2026-08-23` | Global | 🟢 Labs, exams and grading as structured DSLs with **human review** and sandboxed evaluation, CLI + MCP. 🔵 Grading path self-described MVP — cite the shape, which is `P794-2`'s architecture |
| 🟢 **ai-tutor-agent** `NEW` | [`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) | 🟢 **MIT · `1,071 B`** | `0` | `2026-11-09` | APAC 🇻🇳 | 🟢 FastAPI + LangGraph tutor with **Socratic hint escalation** and **answer-leak checking before send**; 🟢 **rubric totals computed in code, not by the model** |
| 🟡 **AITutorAgent** | [`Ebimsv/AITutorAgent`](https://github.com/Ebimsv/AITutorAgent) | 🟢 **MIT · `1,072 B`** | `15` | 🔴 `2025-06-03` (`17` mo) | Global | 🟡 `p794` candidate, now graded. 🔴 Stale at `17` months. Reference only |

🟢 **All four sit in `1,066`–`1,072 B` — inside canonical MIT, so `p795-A`'s filter passes them clean.** 🔵 That is the new filter working on intake rather than on history.

### 🔴 `T921` — `p795-A` discharged, and its own data source was the thing that was wrong

🟢 **`5` byte-size outliers of `91` MIT/BSD rows. `PageLM` — the row the action was written for — is flagged, so `p795-G`'s control is satisfied.** 🟢 `paes-mcp` (`2,018 B`) benign as predicted. 🆕 `rrule` (`3,493 B`) is **two BSD grants, not a rider.**

🔴 **`daddysystem/nextgen-learn` is the finding: [`evidence/rider-gate.2026-11-12-p795.tsv`](../evidence/rider-gate.2026-11-12-p795.tsv) grades it `MIT`; the bytes are `Boost Software License 1.0` and GitHub's SPDX agrees.** 🟢 **The published rows in this file and in [`repos/foundations.md`](../repos/foundations.md) already said `BSL-1.0 (Boost)` and needed no change.** 🔵 **An action specified as "a filter, not a new measurement" inherits every defect of the artefact it filters** → `p796-H`.

### 🔴 `T917` — `3` over-reports in this pass's own instruments, `0` shipped

🔴 **The first grant counter reported `32` multi-grant rows; the true count is `5`.** 🔵 It keyed on the licence NAME, and a `35,147 B` GPL-3.0 text names itself at line start four times. 🔴 **All `4` of my controls were short permissive files, so none could exhibit the defect — `p795-G`'s rule protects against a false zero and does nothing about a false alarm.** 🟢 Rebuilt on per-grant version lines: `9` of `9` controls across both kinds. 🔴 Two residual `grep -c` line-vs-occurrence errors corrected (`kumaken-1` `3`→`2`, `OpenOLAT` `2`→`1`). 🟢 **The uncorrected artefact is published beside the corrected one so the `32`→`5` correction is re-derivable.**

### 🔴 Corrected in place below

| Row | Was | 🟢 Now |
|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | "the permissive LMS for an EMEA engagement" | 🔴 **Apache-2.0 code + `CC BY-ND 2.5` logo and icons.** Still the permissive EMEA LMS; 🔴 **brand assets must be REPLACED, not modified** |
| [`jkbrzt/rrule`](https://github.com/jkbrzt/rrule) | BSD-3-Clause · `3,493 B` | 🔴 **TWO BSD-3-Clause grants** — its own plus bundled `python-dateutil`. Attribution obligation doubled |
| [`ankitects/anki`](https://github.com/ankitects/anki) | AGPL-3.0 · `1,930 B` | 🔴 **The `1,930 B` is a POINTER, not a grant: `AGPL-3.0-or-later` **plus** BSD-3 contributed portions** (`T919`) |
| [`hedyorg/hedy`](https://github.com/hedyorg/hedy) | — | 🟢 **`EUPL-1.2` · `13,827 B` · ★`1,697`** — a family this base's clause set lacked (`T918`) |
| [`metabase/metabase`](https://github.com/metabase/metabase) | per-file carve-out noted | 🟢 **Carve-out now SIZED: `4` files, `1` OSI grant, `8,877 B` of embedding terms with no grant** |
| [`DSpace/DSpace`](https://github.com/DSpace/DSpace) | BSD-3-Clause, anthology unopened | 🟢 **Anthology opened: `721` deps, GPL policy verified, ~`13` LGPL entries** (`T920`) |


## 🆕 `p795` — **`p794-B`'s rider gate was blind to the row that motivated it, and rebuilding it on the bytes found an MIT grant sentence used as camouflage. `p794-A` discharged: the `ARCHIVED` count is CLOSED at `3`, and the real exposure is staleness.**

🟢 **`ACTION p794-A`, `ACTION p794-B` and `ACTION p794-C` (for `oppia`) all discharged this pass.** 🔴 **`p794-F` is NOT discharged and cannot be by this session** — all `6` primary-source domains still fail at `CONNECT` (`T906` persists). 🔴 **`p794-D`, `p794-E` and `p794-H` not reached; carried.** Machine output: [`evidence/rider-gate.2026-11-12-p795.tsv`](../evidence/rider-gate.2026-11-12-p795.tsv) and [`evidence/maintenance-sweep.2026-11-12-p795.tsv`](../evidence/maintenance-sweep.2026-11-12-p795.tsv).

### 🔴 The pass's headline: a gate keyed on a classifier cannot find what makes that classifier abstain

🔴 **`p794-B` specified the rider gate as "exceed the canonical size **for its family**". Keyed on GitHub's SPDX family, it flagged `0` of `167` rows — including `open-webui/open-webui`, the `★158,483` branding-rider row that is the entire reason the action existed.** 🔵 **A rider is *why* the classifier returns `NOASSERTION`, so rows with riders are exactly the rows with no family to compare against.** 🔴 **`46` of `167` rows — `27.5%` — have no GitHub SPDX family at all.** 🟢 **Rebuilt on the licence bytes (title line + clause count + restriction vocabulary), the gate reproduces `6` of `6` controls and yields `T908`, `T910`, `T911`, `T912` and `T913`.**

### 🔴 `T908` — the MIT grant sentence as camouflage, and THIS BASE'S OWN probe would fall for it

🔴 [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) `LICENSE.md` `8,563 B` `e1de68833d1c` opens with the **canonical MIT grant sentence verbatim**, then narrows it inside the same sentence to *"personal, educational, or **non-commercial** research purposes"*, then adds a heading reading **"Prohibition on Redistribution"**.

🔴 **This base's multilingual grant probe keys on exactly that phrase. Measured by grant phrase alone, `PageLM` grades MIT.** 🟢 **Byte size is the discriminator that holds: `8,563 B` vs canonical MIT `1,070 B` = `+700%`.** 🔵 **`T902` said a missed restriction costs more than a missed grant. `T908` says both can arrive in one sentence — and the grant is written first.**

### 🔴 `T909` — `UNGRADED` answers "which family", and this base reads it as "can we ship it"

🟢 Keep `UNGRADED` for the family; 🔴 **carry a CONSEQUENCE beside it.** Corrected in place below for the two rows where the consequence is absolute.

### 🟢 `ACTION p794-A` discharged — four states across `167` rows, and the archived layer is closed

| State | Count | vs `p794` |
|---|---|---|
| 🟢 LIVE-MAINTAINED | `155` | — |
| 🔴 LIVE-ARCHIVED | `3` | 🟢 **`0` new in `164` further rows — `T901`'s "floor" is refuted; it was a count** |
| 🟡 EMPTY | `2` | unchanged |
| 🔴 ABSENT | `0` | unchanged |

🔴 **The field nobody had read is `pushed_at`: `9` rows are stale beyond `24` months with no archived flag**, led by [`jkbrzt/rrule`](https://github.com/jkbrzt/rrule) (★`3,752`, `2024-06-27`) which this base recommends as a primitive, and [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) (`2018-07-16`, 🔴 **`88` months**), whose grant `p790` spent a pass rescuing. 🔵 **Full table in [`repos/trending.md`](../repos/trending.md).** 🟢 **`archived` is the flag a maintainer sets; `pushed_at` is the one they cannot forget.**

### 🟢 `12` rows added — byte-verified, star-exact, placed

| Agent | Repo | Grant, on the bytes | ★ (exact) | Last push | Region | Verdict for Globant |
|---|---|---|---|---|---|---|
| **MCP for Beginners** | [`microsoft/mcp-for-beginners`](https://github.com/microsoft/mcp-for-beginners) | 🟢 **MIT** · `1,141 B` · `9e841e7a26e4` | `17,644` | 🟢 `2026-11-11` | Global | 🟢 **Internal enablement, not a client deliverable.** The MCP curriculum to put under the studio's own engineers before an education-MCP engagement |
| **Education agent skills** | [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | 🟡 **CC-BY-SA-4.0** · `1,230 B` · `c1286baf485e` | `977` | 🟢 `2026-11-03` | EMEA 🇬🇧 | 🟡 **`165` evidence-grounded skills for teachers and school leaders — the richest teacher-facing skill pack measured here.** 🔴 **ShareAlike reaches a derivative pack: a client-specific fork must itself be published CC-BY-SA.** 🔴 GitHub said `NOASSERTION`; the bytes say otherwise |
| **Exam-prep skill** | [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) | 🟢 **MIT** · `1,065 B` · `86368b24a966` | `380` | `2026-10-27` | APAC 🇨🇳 | 🟢 Cross-session memory + handout provenance as an anti-hallucination device. 🔵 Built for 公务员 civil-service exams; the provenance pattern ports anywhere |
| **Colloquium** | [`natolambert/colloquium`](https://github.com/natolambert/colloquium) | 🟢 **MIT** · `1,071 B` · `fa99b0d5d035` | `367` | 🟢 `2026-11-10` | North America 🇺🇸 | 🟢 Markdown-native slides for academics building with agents — the lecture-artefact layer this base had no row for |
| **AI Shifu** | [`ai-shifu/ai-shifu`](https://github.com/ai-shifu/ai-shifu) | 🟢 **Apache-2.0** · `11,342 B` · `0150fcb2599f` | `332` | 🟢 `2026-11-12` | APAC 🇨🇳 | 🟢 Permissive conversational teaching platform, actively pushed. A deployable alternative to the AGPL tutors |
| **Bloom** | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | 🟢 **MIT** · `1,069 B` · `c8351ac37830` | `305` | `2026-10-20` | APAC 🇨🇳 | 🟢 Tutor that models *how* a learner learns and adapts teaching style — the learner-model layer, permissively licensed |
| **DeepTutor-AILearning** | [`3yangyang9/DeepTutor-AILearning`](https://github.com/3yangyang9/DeepTutor-AILearning) | 🟢 **Apache-2.0** · `11,408 B` · `ae1dbfc5e74c` | `290` | `2026-10-09` | APAC 🇨🇳 | 🟢 **Multi-tenant** platform for offline training institutions: platform → institution → campus → teacher/student. 🔵 The only row here with a tenancy model built in, which is the shape a training-provider client actually buys |
| **Moodle AI Skill Navigator** | [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) | 🟡 **GPL-3.0** · `35,153 B` · `a0ca524c0129` | `281` | 🟢 `2026-11-07` | Global | 🟡 **AI tutoring, quizzes, mind maps and RAG over course materials as a Moodle plugin.** 🟢 **GPL-3.0 is correct and unavoidable here** — Moodle plugins inherit it; this is the "AI on top of the incumbent LMS" path, not a replacement |
| **Diagnostic tutor skill** | [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 🟢 **MIT** · `1,102 B` · `b5c46c4fb03c` | `267` | 🟢 `2026-11-11` | APAC 🇨🇳 | 🟢 **Diagnosis-first**: identifies the misconception before teaching, with no mode or command surface. 🔵 Closest public artefact to the dosage/engagement instrument `p794-E` asks for |
| **Freelingo** | [`artcc/freelingo`](https://github.com/artcc/freelingo) | 🔴 **AGPL-3.0** · `34,514 B` · `128919466b58` | `261` | 🟢 `2026-11-12` | EMEA 🇪🇸 | 🔴 **AGPL-3.0 §13 reaches a hosted service** — language-learning platform, local or cloud LLMs. 🟡 Fine for an institution hosting it; a licensing decision before any client-branded SaaS |
| **StudyAI** | [`zuhairhalawa/studyai`](https://github.com/zuhairhalawa/studyai) | 🟢 **MIT** · `1,069 B` · `df4c8912c038` | `249` | `2026-10-24` | Global | 🟢 **Local-first** university study platform: lecture slides in, spaced repetition out. 🔵 Pairs with `jkbrzt/rrule` for the scheduling half |
| **Claw-ED** | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | 🟢 **MIT** · `1,078 B` · `ec5640f4f262` | `65` | `2026-09-19` | Global | 🟢 Local-first teaching assistant producing **editable** lesson drafts and student materials — editability is the teacher-trust property `p790` identified |

🔵 **The shape of this week's supply is the SKILL PACK, not the application.** 🟢 Four of the twelve are prompt/skill bundles for an existing harness: `0` infrastructure to deploy, and the licence is the only integration question — which is why `education-agent-skills`' ShareAlike is the most consequential licence fact in the table.

### 🔴 `3` candidates graded and REFUSED, with the reason

| Candidate | ★ | 🔴 Why not |
|---|---|---|
| 🔴 [`Oriole-FDU/Wisepen`](https://github.com/Oriole-FDU/Wisepen) | `125` | 🔴 **Business Source License 1.1** · `4,539 B` · `06d125b6096c` — **source-available, NOT open source.** GitHub said `NOASSERTION`. 🔵 **BSL is a licence family new to this base's education corpus** — note it is *not* the Boost `BSL-1.0` already recorded at `p789`; same abbreviation, opposite meaning |
| 🔴 [`Nutlope/llamatutor`](https://github.com/Nutlope/llamatutor) | `2,053` | 🔴 **No root licence file.** LIVE and pushed `2026-10-23` — 🔴 **the highest-starred ungranted education row ever measured here.** With no grant there is nothing to ship |
| 🔵 [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | `168` | 🔵 `UNGRADED` + consequence (`T909`): `LICENSE.md` is a `5,789 B` *"licensing framework"* explainer splitting code from content, **not a grant instrument.** 🟡 Promising as a trusted-instructional-content data layer; ask upstream for a real grant first |

### 🔴 Corrected in place below

| Row | Was | 🟢 Now |
|---|---|---|
| 🔴 [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 🔵 `UNGRADED` | 🔵 `UNGRADED` **+ 🔴 NON-COMMERCIAL · REDISTRIBUTION PROHIBITED** — cannot be in a client deliverable in any form (`T908`, `T909`) |
| 🔴 [`1edtech/caliper-spec`](https://github.com/1edtech/caliper-spec) | 🔵 `UNGRADED` | 🔵 `UNGRADED` **+ 🟡 implementable, NOT redistributable**; IMS is sole arbiter of compliance (`T909`) |
| 🔴 [`frappe/education`](https://github.com/frappe/education) | `19 B` grant, unresolved since `T905` | 🔴 **`DECLARED-GPL-3.0-NO-GRANT-TEXT`** — `license.txt` is `19` bytes reading `License: GNU GPL V3`, blob `beca17940a71`. No grant instrument exists (`T913`) |
| 🔴 [`Tzxser/aipha-learning-os`](https://github.com/Tzxser/aipha-learning-os) | 🔴 PROPRIETARY | 🟢 **Confirmed PROPRIETARY on re-read** — *"Public visibility does not make the original AIpha source open source"*; no derivative works. Grade stands |

## 🆕 `p794` — **a licence CORRECTION on the `★158,480` row this base green-flagged, and a third existence state the instrument still could not see: `ARCHIVED`.**

🟢 **`ACTION p793-A` and `ACTION p793-B` both discharged across `170` addresses** — every repository address in the six live files, not just `agents/top.md`'s `122`. 🔵 **Three instruments ran, each on a different channel**: three-state existence (`git ls-remote` + ref count), a **multilingual** root-grant probe on blobless trees + lazy blob reads, and `gh api search/repositories` for exact stars **and** GitHub's own SPDX verdict. Machine output: [`evidence/master-row-measurements.2026-11-12-p794.tsv`](../evidence/master-row-measurements.2026-11-12-p794.tsv).

| Gate | Result |
|---|---|
| 🟢 Addresses swept, all three instruments | **`170`** · 🟢 **`0` clone failures** |
| 🟢 Existence re-graded three-state (`p793-A`) | **`168` LIVE · `2` EMPTY · `0` ABSENT** — 🟢 **`0` corrections** |
| 🔴 **Rows ARCHIVED upstream — an axis no instrument here has ever read** | 🔴 **`3`**, and the word *archived* appeared **`0` times** in this base |
| 🟢 Licence grades cross-checked against GitHub's SPDX classifier | 🟢 **`118` of `118` AGREE · `0` disagree** |
| 🟢 Rows where the **bytes** beat GitHub's `NOASSERTION` | 🟢 **`23`** |
| 🔴 **Licence grades this pass CORRECTED** | 🔴 **`1`** — [`open-webui/open-webui`](https://github.com/open-webui/open-webui) (`T900`) |
| 🟢 Star counts re-measured **exactly** (no longer carried forward) | 🟢 **`164` of `170`** · `6` LIVE but absent from the search index (`T903`) |
| 🔴 Defects in **this pass's own instruments**, all caught before publication | 🔴 **`5`** |

### 🔴 `T900` — the correction: `open-webui` is **not** BSD-3-Clause, and the clause that makes the difference bars white-labelling

This base publishes Open WebUI twice — [`repos/foundations.md`](../repos/foundations.md) *"the quickest compliant front end for a school-hosted model"* and [`verticals/solutions.md`](../verticals/solutions.md) 🟢 *"BSD-3-Clause"* — on a `2,819 B` licence file. 🔴 **Canonical BSD-3-Clause has exactly three numbered clauses. This file has four.**

> `4.` Notwithstanding any other provision of this License, and as a material … from altering, removing, obscuring, or replacing any **"Open WebUI" branding**, including but not limited to the name, logo, or any visual … alteration of the "Open WebUI" branding shall constitute a **material** breach.

🔴 **Corrected grade: `BSD-3-Clause + branding rider` — not OSI-conformant, and it prohibits precisely the act a Globant engagement performs on a delivery surface: putting the client's name on it.** 🔵 Two details make this a trap rather than an oversight:

| Detail | Why it defeats a reader |
|---|---|
| 🔴 The repository ships **three** root licence files — `LICENSE` (`2,819 B`, ridered), `LICENSE_HISTORY` (`2,872 B`, 🟢 **clean BSD-3-Clause**) and `LICENSE_NOTICE` (`721 B`) | 🔴 **Opening the wrong one of three gives the wrong answer**, and `LICENSE_HISTORY` is the one that reads clean |
| 🟢 GitHub's classifier says `NOASSERTION` here | 🟢 **The classifier was more honest than this base's hand grade** — the one row in `141` where that is true |
| 🟢 Byte size would have caught it | 🟢 Canonical BSD-3-Clause is ≈`1,500 B`; this is **`2,819 B`** — `p790-F`'s size-triggered gate works, it was simply never pointed here |

🔵 **`T900` is the seventh recorded way to misread a licence, and the first that is additive: a rider does not change the title line, the clause language or the family — it appends.** Family matching cannot see it. 🟢 **Clause count can**: `3` for BSD-3, `2` for BSD-2, anything more is a rider.

### 🔴 `T901` — `ARCHIVED` is a third existence state, and this base recommends three archived repositories

🟢 `p793` split existence into LIVE · EMPTY · ABSENT and that was right. 🔴 **It is still not enough: `git ls-remote` returns `rc=0` with `refs ≥ 1` for a repository that is archived, read-only and years stale — a signature identical to a healthy one.** The signal is free in the same call that returns stars.

| Row | Where this base recommends it | 🔴 Last push | What it costs |
|---|---|---|---|
| 🔴 [`MaharaProject/mahara`](https://github.com/MaharaProject/mahara) `★120` | `repos/foundations.md` + `verticals/solutions.md` — *"ePortfolio, the natural home for skills-based credentialing"* | 🔴 **`2023-11-16`** | 🔴 **Three years stale, read-only.** 🔵 And this base did canonicity work on this very row (*"`mahara/mahara` is DEAD"*) — so **resolving to the canonical owner is not resolving to a maintained repository** (`T887` extended) |
| 🔴 [`MyScript/MyScriptJS`](https://github.com/MyScript/MyScriptJS) `★357` | `repos/foundations.md` 🆕 + `verticals/solutions.md` — *"the input primitive for a maths tutor on a tablet"*, 🟢 **"Rescued"** at `p786` | 🔴 **`2021-01-04`** | 🔴 **Nearly six years stale.** 🔵 **A licence rescue is not a viability rescue** — `p786` cleared the grant axis and no pass has ever checked the maintenance axis |
| 🟡 [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) `★54` | `repos/foundations.md` 🆕 + `verticals/solutions.md` — *"the vocabulary an EU public-sector client will expect"* | 🟡 **`2024-02-14`** | 🟡 **Milder: a published data model may legitimately freeze.** 🔴 But an EMEA client is being pointed at an archived Commission repository without being told it is archived |

🔵 **The fix is one field, and it is already in this pass's evidence:** `archived` from `gh api search/repositories`. 🟢 **Existence now needs four states — LIVE-MAINTAINED · LIVE-ARCHIVED · EMPTY · ABSENT.**

### 🟢 `p793-B` discharged — and the multilingual probe's real finding is the opposite of the one predicted

🔴 **`p793-B` predicted that English-only clause matching *under-reports* usable repositories, LATAM especially.** 🟢 **Measured across `170` addresses with grant phrases in `20` languages — English, Spanish, Portuguese, German, French, Italian, Dutch, Polish, Russian, Ukrainian, Turkish, Indonesian, Chinese, Japanese, Korean, Hindi, Arabic, Vietnamese, Thai, Hebrew — plus the Creative Commons families: exactly ONE non-English grant exists on this whole corpus**, [`goyanedelv/paes-mcp`](https://github.com/goyanedelv/paes-mcp) (Spanish MIT), which `T864` already had. 🟢 **The prediction is refuted at the grant layer: `19` added languages bought `0` new rows.**

🔴 **But the sweep found language-blindness doing something far worse than under-reporting, and `T902` is the sharper form of `T848`:**

| | |
|---|---|
| Row | [`luscitiosus/Dirigo`](https://github.com/luscitiosus/Dirigo) `362 B`, Spain 🇪🇸 |
| 🔴 What an English-only CC probe returns | 🔴 **`CC-BY-4.0`** — permissive, commercially usable |
| 🟢 What the bytes say | 🟢 **`CC BY-NC-SA 4.0`** — *"licencia Creative Commons Atribución-**NoComercial**-**CompartirIgual** 4.0"* |
| 🔴 Why | 🔴 **The sub-family tokens are English-only.** `NoComercial` is not `NonCommercial`; `CompartirIgual` is not `ShareAlike`. Matched `0` times each |

🔴 **Language-blindness on a restriction does not cost you a row — it STRIPS THE RESTRICTION and hands you a NonCommercial repository graded as permissive.** 🟢 Under-reporting loses an opportunity; over-reporting puts a commercially barred repository into a client deliverable. 🔵 **This base is not exposed** — `T863` already graded `Dirigo` correctly by hand — but any probe built from `p793-B`'s brief would have been. 🟢 **Remedy shipped**: NC · ND · SA token sets in `13` languages, re-run, `Dirigo` now grades `CC-BY-NC-SA-4.0`.

### 🔴 The `5` defects in this pass's own instruments

| # | Defect | Caught by |
|---|---|---|
| 1 | 🔴 **The address extractor admitted a command template.** `github.com/OWNER/REPO` from a fenced code block in `repos/foundations.md` swept as an address and returned `ABSENT` — the pass's only `rc=128` | 🟢 Reading the one `ABSENT` row instead of counting it. 🔵 This base **already** rejects that shape; my extractor did not |
| 2 | 🔴 **The clause set had no `ECL-2.0` — this industry's own licence.** `sakaiproject/sakai`, `opencast/opencast` and `SakaiXAPI-Provider` came back `UNRECOGNISED`. 🔴 **ECL-2.0 is Apache-2.0 with a narrowed patent grant and the string `"Apache License"` appears `0` times in it** | 🟢 All three were already graded `ECL-2.0` by hand here. 🔵 A *multilingual* probe that omits the sector's licence is tuned for the wrong axis |
| 3 | 🔴 **A grant-shaped root filename is not a grant.** `NOTICE`, `COPYRIGHT`, `LICENSE_HEADER`, `LICENSE.header`, `COPYRIGHT_NOTICE`, `LICENSE-EMBEDDING`, `LICENSE_NOTICE` and a **`19`-byte pointer** all admitted as grants | 🟢 Reading all `17` `UNRECOGNISED` files. 🔵 **`0` were new absences** — every one sat on a row this base had already graded correctly |
| 4 | 🔴 **CC sub-family detection was English-only** → `T902`, above | 🟢 A control on a row with a known Spanish grant |
| 5 | 🔴 **Family matching is blind to additive riders** → `T900`, above | 🟢 Clause counting, after GitHub's `NOASSERTION` disagreed with my confident `BSD-3-Clause` |

🔵 **`4` of the `5` are one mistake: I graded on a proxy — a filename, a clause set, a family, an English token — instead of reading the bytes.** That is `p792-G` and `p793-G` arriving together, and the instrument that caught most of them was **this base's own published record**, which disagreed with my probe and was right every time.

### 🟢 `4` rows added — byte-verified, star-exact

| Agent | Repo | Grant, on the bytes | ★ (exact) | Last push | Region | Verdict for Globant |
|---|---|---|---|---|---|---|
| 🟢 **tutor-mcp** 🆕 | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** · `1,073 B` · `7f7f7a24de57` | `102` | 🟢 **`2026-11-12`** | EMEA 🇫🇷 | 🟢 **The category this base was missing.** It has MCP servers that reach *into* systems of record (`p792`) and tutors that *are* applications — this is **the tutor itself as an MCP server**, so an Intelligent Tutoring System attaches to any MCP-speaking host instead of owning the front end. `1,279`-file tree, pushed today |
| 🟢 **kaogong-skill** 🆕 | [`KeWang0622/kaogong-skill`](https://github.com/KeWang0622/kaogong-skill) | 🟢 **MIT** · `1,083 B` · `68908d0d445e` | `241` | `2026-10-12` | APAC 🇨🇳 | 🟢 **Teaching-as-a-skill, third instance, and the first for high-stakes exam preparation** — Chinese civil-service (考公) exam prep packaged as a coding-agent skill set. `51` files. 🔵 Confirms the packaging shift `p792` recorded is not a one-off |
| 🟡 **ai-tutor-agent** 🆕 | [`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) | 🟢 **MIT** · `1,071 B` · `9075c1821610` | 🔴 **`0`** | `2026-11-09` | APAC 🇻🇳 | 🟡 **Listed for its shape, not its traction — and the `0` is published, not hidden.** FastAPI + LangGraph, Socratic hints, rubric grading, session memory, offline demo mode: the cleanest minimal reference for the architecture this base recommends. `58` files |
| 🟡 **ai-engineering-from-scratch** 🆕 | [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) | 🟢 **MIT** · `1,070 B` · `61442168db9a` | 🟢 **`78,560`** | 🟢 **`2026-11-12`** | Global | 🟡 **The largest MIT education-adjacent repository this base has ever measured — and it is NOT a client deliverable.** `542` lessons, `11,299` files, teaching AI engineering to engineers. 🔵 **Place it correctly: an internal enablement asset for the studio's own staff**, not an education-sector product |

### 🟢 Star counts — no longer carried forward

🔴 **This base's README states star counts are carried forward because `github.com` and `api.github.com` return `403`.** 🟢 **That limitation is now lifted: `gh api search/repositories` with batched `repo:` qualifiers answers `10` addresses per call and returns the exact integer, the SPDX verdict, the push date and `archived`.** `164` of `170` re-measured.

| Row | Published here | 🟢 Re-measured `2026-11-12` |
|---|---|---|
| [`ollama/ollama`](https://github.com/ollama/ollama) | — | 🟢 **`186,787`** MIT |
| [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | — | 🟢 **`158,480`** 🔴 `NOASSERTION` → `T900` |
| [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | — | 🟢 **`79,500`** MIT |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | `58,585` | 🟢 **`58,596`** Apache-2.0 |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | `43,365` | 🟢 **`43,389`** MIT |
| [`moodle/moodle`](https://github.com/moodle/moodle) | — | **`7,607`** GPL-3.0 |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | — | **`1,239`** 🟢 **`ECL-2.0` — GitHub's classifier agrees with the bytes** |

### 🔴 `T903` — a search-index miss is not an absence, and owner casing is not canonical

🔴 **`6` of `170` addresses are absent from `search/repositories` and every one of them clones and serves refs**, including [`openedx/edx-platform`](https://github.com/openedx/edx-platform) — among the largest repositories in this sector: `DaRL-GenAI/instructional_agents` · `NikolasSchaeffner/lehrer-agent` · `cosark/OpenTutor` · `csev/tsugi` · `foradian/fedena` · `openedx/edx-platform`. 🟢 **Verified LIVE on the git channel with `git ls-remote --symref`.** 🔵 `p793-G` instantiated for a new instrument: **name the blind spot before recording the zero.**

🟢 **And the same call hands over a canonicity signal for free — it normalises owner casing.** Two addresses this base publishes come back cased differently: `1edtech/caliper-spec` → 🟢 **`1EdTech/caliper-spec`**, `anonymousonyx22/brightspace-d2l-mcp` → 🟢 **`AnonymousOnyx22/brightspace-d2l-mcp`**.

### 🟢 `T904` — the `20` ungranted LIVE rows reproduce this base's record exactly

🟢 **`20` LIVE repositories serve no recognised root grant, and all `20` were already recorded here as ungranted, refused or absent. `p794` adds no absence and removes none.** The two the base's own `19`-row list does not name — [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) and [`formalms/formalms`](https://github.com/formalms/formalms) — are both recorded elsewhere in this file set (*"NO GRANT SERVED"* at this exact address, and the any-depth-title gate). 🔵 **`formalms` adds one detail worth keeping:** its licences live at `html/lib/System/license/license_<language>.txt` — a **localised, non-root licence directory**, the one shape where a multilingual probe would pay off and the one shape that still grants nothing to the host.

### 🔴 Corrected in place below — stale rows that contradict this base's own corrections

| Row | 🔴 Stale text still published | 🟢 This pass |
|---|---|---|
| `Bestisco/My-WASSCE-Companion` · `Elite2828/ACE-AI-Tutor` | 🔴 *"DEAD — `git ls-remote` `rc=2`, re-probed and confirmed"* in the rejected-rows table, **contradicting `p793`'s own correction `20` lines above** | 🟢 **`rc=0`, `0` refs, `0` `HEAD` — ALIVE and EMPTY, reproduced.** 🔴 **`rc=2` is not reproducible on any of the three states** and should never have been published |
| `Kosudo/nextSIS` | 🔴 **`PROPRIETARY`** still published in `repos/foundations.md` and `verticals/solutions.md` after `p790` corrected it | 🟢 **`GPL-3.0`**, `39,890 B`, reproduced on the bytes |

### 🔴 `T905` — the `sha=` column is not one hash function, and some of it is neither

🔴 **Byte sizes in this base reproduce exactly. The `12`-char `sha` beside them does not.** Measured against `git rev-parse HEAD:<path>` (controlled: `rev-parse` ≡ `git hash-object` ≡ `ls-tree` blob, exact on `sakaiproject/sakai`):

| Row | Bytes | Published `sha` | 🟢 git blob sha | What the published value actually is |
|---|---|---|---|---|
| `frappe/education` | `19` 🟢 | `beca17940a71` | 🟢 `beca17940a71` | 🟢 **git blob sha — correct** |
| `frappe/education` | `19` 🟢 | `1fcecf395312` | `beca17940a71` | 🔴 **`sha256` of the content** — same file, same pass |
| `frappe/education` | `19` 🟢 | `61408d3da518` | `beca17940a71` | 🔴 **Neither** — unidentified |
| `VictorOsondu/ai-adoption-education` | `752` 🟢 | `2e9c34096bf9` | `e51a2ad5fd53` | 🔴 **`sha256`** |
| `sakaiproject/sakai` | `11,120` 🟢 | `593c74e1c7a5` | `2d2098a91927` | 🔴 **Neither** |
| `luscitiosus/Dirigo` | `362` 🟢 | `9ed32d5c2577` | `3e22da8fe678` | 🔴 **Neither** |
| `Kosudo/nextSIS` | `39,890` 🟢 | `60e422c7d93e` | `01fa8c8c4c6e` | 🔴 **Neither** |
| `THU-MAIC/OpenMAIC` | `1,065` 🟢 | `717b69cbe2f4` | `76abc5f13261` | 🔴 **Neither** |

🔴 **One file in one pass carries three different hash values, so this is internal, not drift: the column mixes at least two hash functions and contains values matching neither.** 🟢 **Byte size is the reproducible provenance anchor — `8` of `8` exact.** 🔵 **Treat every `sha=` in this base as unverified until re-measured**, and record which function produced it. `p794`'s own shas are `git rev-parse HEAD:<path>`, truncated to `12`.

---
## 🆕 `p793` — **the whole list re-measured on an independent instrument in `11` seconds: `103` root grants sized and sha'd, `0` licence grades corrected, `2` existence verdicts corrected.**

🟢 **`ACTION p792-B` discharged across all `122` repository addresses in this file**, carrying `p791-E` (tree audit) and `p791-F` (byte sizes) in one sweep as instructed. 🔵 **Method is deliberately different from the channel that produced these rows**, so agreement means something: blobless tree enumeration (`git clone --filter=blob:none --no-checkout --depth 1` + `git ls-tree -r --name-only`), root-only grant selection, extension filtering, non-root grants treated as **vendored**, and the grant bytes then read on the `raw` channel. Full machine output at [`evidence/licence-tree-gate-corrected.2026-11-12-p793.tsv`](../evidence/licence-tree-gate-corrected.2026-11-12-p793.tsv).

| Gate result over `122` addresses | Count |
|---|---|
| 🟢 `ROOT_GRANT` — path, **byte size and `12`-char blob sha now recorded** | **`103`** |
| 🔴 `NO_ROOT_GRANT` | **`19`** |
| 🔴 Clone failures | 🟢 **`0`** |
| 🟢 **Licence grades this sweep CORRECTED** | 🟢 **`0` of `122`** |
| 🔴 Existence verdicts this sweep corrected | **`2`** (`T892`) |

🟢 **Controlled before use, on the two rows `T886` recorded as the gate's known failure modes — correct in both directions:** `mingxuanyan07-lgtm/ai-for-education-showcase` → `NO_ROOT_GRANT` with `2` vendored paths, correctly **not** rescued; `oppia/oppia` → `ROOT_GRANT` Apache-2.0 `11,358 B` with `vendored_nonroot=0`, correctly **not** flagged.

### 🔴 `p793` CORRECTS two existence verdicts — "DEAD" was wrong, and the right answer is commercially better

| Address | Published | 🟢 Measured at `p793` | What it means |
|---|---|---|---|
| [`Bestisco/My-WASSCE-Companion`](https://github.com/Bestisco/My-WASSCE-Companion) | 🔴 DEAD | 🟡 **ALIVE, EMPTY** — `rc=0`, **`0` refs**, clones, no `HEAD`, `raw` `404` | 🟢 An author who claimed the name and has not pushed |
| [`Elite2828/ACE-AI-Tutor`](https://github.com/Elite2828/ACE-AI-Tutor) | 🔴 DEAD | 🟡 **ALIVE, EMPTY** — same signature | 🟢 Same — reachable, and a *future* row |

🔵 **Ghana's measured position therefore improves**: not `11` repositories of which `2` are dead ends, but `11` of which `2` are authors mid-intent — the same outreach channel as a licence request. Mechanism, the three-state instrument that replaces exit-status grading, and the one unreproducible detail are all at [`intel/trends.md`](../intel/trends.md) → `T892`.

### 🟢 The `19` ungranted rows — confirmed, and now split into three states rather than one

🟢 **Every one of the `19` was already recorded by this base as ungranted, refused or absent. `p793` adds no new absence and removes none** — it separates them:

| State | Rows |
|---|---|
| 🟡 **ALIVE but EMPTY** (`0` refs) | `Bestisco/My-WASSCE-Companion` · `Elite2828/ACE-AI-Tutor` |
| 🟡 **ALIVE, essentially empty** (`1` file) | `RAFCERAY/horizonia` |
| 🔴 **ALIVE with a real tree and no root grant** | `7irelo/aptiverse` (`1,726`) · `ghwmelite-dotcom/brilla-study-platform` (`2,012`) · `tosinamuda/teacher-agent-itu-hackathon` (`3,375`, `1` vendored) · `MRiARC/VidyaSetu` (`908`) · `kaikai52125/NeoTutor` (`521`) · `mingxuanyan07-lgtm/ai-for-education-showcase` (`189`, `2` vendored) · `TaoYu-ds/TutorMesh` (`143`) · `redoneabouaali-lab/najih` (`141`) · `NikolasSchaeffner/lehrer-agent` and `lehrer-tools/lehrer-agent` (`103` each) · `narumi-mase/osaka-lesson-dataset` (`26`) · `silja-graf/Didaktikus-…-LP21` (`23`) · `A-R007/Multi-Agent-Study-Assistant` (`19`) · `NSK-394/schoolbridge-mcp` (`19`) · `SoukhyadP991/Multilingual-NCERT-Doubt-Solver` (`18`) · `zulfahmi93/susun-jadual` (`10`) |

🔵 **Tree size is the ranking signal for a licence request**: `7irelo/aptiverse` 🇿🇦 (`1,726` files) and `ghwmelite-dotcom/brilla-study-platform` 🇬🇭 (`2,012` files) are substantial bodies of work one e-mail away from being usable, while a `10`-file repository is not worth the ask.

### 🟢 The copyleft rows re-graded on a second instrument — GPL-3.0 and AGPL-3.0 separated by bytes

🟢 **`7` of `7` match this base's published grade.** The discriminator is byte size plus the count of the word *affero*, and 🔴 **a bare grep for "affero" gets it backwards**, because GPL-3.0's §13 is titled *"Use with the GNU Affero General Public License"* — the **sixth** recorded way to misread a licence here (`T894`).

| Row | Bytes | `affero` | Verdict |
|---|---|---|---|
| `CREARED-EDU-CO/GenPrompt-Pre-ICFES-11` · `dpaul0501/OpenVidya` · `amosblomqvist/learnharness` | `34,523` | `15` | 🔴 **AGPL-3.0** |
| `Prady029/NCERT-AI-Teacher-Assistant` · `chc-chupea/news-grade-reader` · `plastic-labs/tutor-gpt` | `35,149` | `3` | 🔴 **GPL-3.0** |
| `Kosudo/nextSIS` | `39,890` anthology | `3` | 🔴 **GPL-3.0** — matches `p790`'s correction |

🔵 **Why Globant should care which one:** AGPL-3.0 §13 reaches a **hosted** service, which is how a client engagement would ship; GPL-3.0's does not.

### 🔴 The gate's own defect, and it re-created a failure mode within minutes of reading about it

Four rows came back `UNRECOGNISED` from my clause-grep. 🟢 **All four were already graded correctly by hand in this file** — so the finding is about the instrument, not the data:

| Row | Why the gate failed | Correct grade |
|---|---|---|
| 🔴 `goyanedelv/paes-mcp` | 🔴 **My clause set was English-only** — the grant reads *"Se concede permiso, libre de cargos"* | 🟢 **MIT (Spanish text)** — `T864`, re-confirmed |
| 🔴 `Tzxser/aipha-learning-os` | 🔴 **A path name matched (`COPYRIGHT_NOTICE`) on a file that grants nothing** — *"All rights reserved… Public visibility does not grant permission"* | 🔴 **PROPRIETARY** — matches |
| `gabrielmahia/shule-ai` · `luscitiosus/Dirigo` · `nahisaho/teacher-genai-playbook` | Creative Commons clause text, not software-licence clause text | 🔴 **CC BY-NC-ND 4.0 · CC BY-NC-SA 4.0 · CC BY-NC 4.0** — all match |

🟢 **Two rules the gate now carries: a path name selects a candidate and only the clauses decide; and the clause set must be multilingual.** 🔵 `T848` (language-blindness) was written down one pass ago and this pass's brand-new instrument reproduced it immediately — the strongest available evidence that it is the **default** behaviour of a probe written in English, not an accident.

### 🔴 Dependency grants — `ACTION p792-A` discharged, and `kolibri`'s row survives with its argument strengthened

🟢 **"2 LGPL of 32" is EXACT**, and the `32` is now identified: the **Python `base` dependency group in `pyproject.toml`**, every entry `==`-pinned, resolved against PyPI at each pin → `zeroconf-py2compat==0.19.17` (LGPL-2.1) and `json-schema-validator==2.4.1` (classifier LGPL, 🔴 **`license` field empty**). Both distribution-triggered, not network-triggered.

🔴 **The npm side had never been measured.** `kolibri` is a pnpm workspace of `40` importers whose root `package.json` declares **`0`** runtime dependencies. Resolved across all importers at locked versions: **`208`** runtime packages — 🟢 **`0` GPL/LGPL/AGPL**, `175` MIT, `10` Apache-2.0, `9` BSD, `5` ISC, `5` other permissive, `1` MPL-2.0 (`mathquill@0.10.1`), `1` dual `(MPL-2.0 OR Apache-2.0)` (`dompurify@3.4.17` → 🟢 elect Apache-2.0), and **`1` with no grant at all**:

| 🔴 `@khanacademy/mathjax-renderer@3.0.2` | Declared by `kolibri/plugins/perseus_viewer` → `dependencies` |
|---|---|
| Registry metadata at the pin | 🔴 `license` absent |
| 🟢 **The published tarball** (`336,573 B`) — what actually ships | 🔴 **No `LICENSE`/`NOTICE`/`COPYING` at any path** |
| Upstream `Khan/mathjax-renderer` | 🔴 **`git ls-remote` `rc=128` — address does not resolve** |

🔵 **So `kolibri`'s residual licence risk is one plugin, not the platform**: `mathquill` (MPL-2.0, file-level) and the ungranted package above are both declared by `perseus_viewer`, the exercise renderer that ships to learners. Everything in core is permissive. Evidence: [`evidence/kolibri-npm-lockfile-resolved.2026-11-12-p793.tsv`](../evidence/kolibri-npm-lockfile-resolved.2026-11-12-p793.tsv) · [`evidence/kolibri-pypi-pinned-resolved.2026-11-12-p793.tsv`](../evidence/kolibri-pypi-pinned-resolved.2026-11-12-p793.tsv) · `T895`, `T896`.

### 🟢 Canvas MCP's auth model, read before any offer was written (`ACTION p792-D`)

[`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) — MIT, `1,071 B`, `3c7307584ae4`, `529`-file tree. 🟢 **`p792-D`'s premise is partly refuted:** it ships a structured audit trail (`core/audit.py`, `215` lines) that **masks identifiers** (`/courses/12345/users/678` → `/courses/***/users/***`) and logs executed code as a **SHA-256 hash**, three deployment overlays, an outbound-blocked sandbox, token rotation and its own prior security reviews. 🔴 **But its hardened flags are labelled *"pending feature wiring"* and *"some flags are placeholders"*** — including `MCP_CLIENT_AUTH_MODE=api_key_or_mtls` and `LOG_REDACT_PII=true` — and its token layer authenticates *clients to the server*, while `SECURITY.md` states that the Canvas credential underneath **"has full access to your Canvas account"**. 🔵 Full reading and the corrected commercial framing: `T897`, and the recipe at [`compose/patterns.md`](../compose/patterns.md) → `P793-1`.

### 🟡 Star counts this pass — one channel open, one closed

🟢 `gh api search/repositories` with a `repo:` qualifier is **open** and returns exact integers: **[`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) `58,585★`, Apache-2.0, pushed `2026-11-07`** — confirming the `58.5k` this base carried. 🔴 `curl https://github.com/…` and `api.github.com/repos/…` are both **`403`** in this session, so page-channel star reads were unavailable and every other star figure in this file is **carried forward from a prior pass, not re-measured at `p793`**.

## 🆕 `p792` — **a new category: agents that reach INTO the system of record. Plus one canonicity trap, `6` rows added, `1` tree cleared.**

🟢 **Method unchanged from `p791`.** Existence via `git ls-remote` (exit status read directly). Grant by **anchored title lines** in the served licence bytes. Trees enumerated with `git clone --filter=blob:none --no-checkout --depth 1` + `git cat-file`. Stars are `search/repositories` reads with a `repo:` qualifier, which return **exact integers**. 🔴 **New channel caution this pass (`T885`): a `200` from `raw.githubusercontent.com` on `.../master/...` does NOT prove a `master` branch exists** — the host aliases the legacy name to the default branch. Every row below is addressed by its **real default branch**, read from `git ls-remote --symref`.

### 🟢 MCP into the systems of record — the shift this pass records

🔵 **Every pass of this base has collected *tutors*: agents that teach a learner.** `p792` records a different and more commercially useful shape — agents that hold **authenticated, tool-scoped access to the platform the institution already runs**. Grading, enrolment, assignments and submissions are where an education client's actual work sits, and these are the first permissive rows this base has that reach it.

| Agent | Repo | Grant, on the bytes | ★ (exact) | Last push | Verdict for Globant |
|---|---|---|---|---|---|
| 🟢 **Canvas MCP** 🆕 | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · `1,071 B` · `3c7307584ae4` | `323` | `2026-11-12` | 🟢 **The most immediately useful row this pass, and the canonical one.** An MCP server over **Canvas LMS** — the LMS a North American higher-ed client is most likely to be running — exposing courses, assignments, submissions, grading and announcements as agent tools, plus agent skills. 🟢 **`529` files, exactly ONE licence path, MIT:** single-family tree, clean to the gate. 🟢 Pushed today. 🔵 Community project, **not** an Instructure product — Instructure documents the REST/GraphQL APIs and LTI 1.3, not an MCP server of its own |
| 🟢 **Gradescope MCP** 🆕 | [`Yuanpeng-Li/gradescope-mcp`](https://github.com/Yuanpeng-Li/gradescope-mcp) | 🟢 **MIT** · `1,068 B` · `0e01db542a01` | `8` | `2026-11-12` | 🟢 **Small but precisely placed: MCP access to Gradescope**, the assessment platform that holds the submissions and rubrics in a large share of university STEM courses. 🟢 `80` files, ONE licence path — clean. 🔴 `★8`: read it as a working reference for how the auth and rubric surfaces are shaped, not as a dependency |
| **AutoGrader-Agent** 🆕 | [`omerfarooq223/AutoGrader-Agent`](https://github.com/omerfarooq223/AutoGrader-Agent) | 🟢 **MIT** · `1,077 B` · `b6f57bd5a4ab` | `3` | `2026-11-02` | 🟡 Rubric-driven automated grading with feedback generation. 🔵 Placed because **grading is the task education clients ask for first** and this base held no permissive grading agent at all — but at `★3` it is a pattern to read, not a build to adopt |

🔴 **`T887` — the canonicity trap, and it nearly put the wrong row in this file.** The first Canvas MCP this pass found was [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) — **MIT, `1,070 B`, `1acff129baf3`, `501` files, `★10`** — surfaced top-of-list by a `grading agent` query. It is a real, granted repository and it is **not canonical**. A name sweep returns `vishalsachdev/canvas-mcp` at **`★323`** (`529` files, `1,071 B`, different sha), then `boyuchengz/canvas-mcp` at `★119` (MIT), then 🔴 `DMontgomery40/mcp-canvas-lms` at `★104` **ungranted**. 🔵 **`1,070` vs `1,071` bytes and `501` vs `529` files is what a derivative looks like.** 🟢 **Rule, extending `p790`'s `janestreet`/`jane-street` finding: when a repository implements a named third-party protocol or platform, sweep the name before writing the row — the first hit is ranked by query match, not by canonicity.**

### 🆕 Teaching-as-a-skill and instructional design — three more permissive rows

| Agent | Repo | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **hsk-tcsl-skills** 🆕 | [`jw-wuzhen/hsk-tcsl-skills`](https://github.com/jw-wuzhen/hsk-tcsl-skills) | 🟢 **MIT** · `1,108 B` · `dd5503456a1e` | `12` | APAC | Agent skills for **HSK** and *teaching Chinese as a second language* — level-aware vocabulary and grading against a published proficiency scale. 🟢 **A curriculum-standard-aware skill set**, which is the shape `p791`'s `socratic-tutor` finding predicted would spread |
| **addie-instructional-designer** 🆕 | [`XiucuiGuan/addie-instructional-designer`](https://github.com/XiucuiGuan/addie-instructional-designer) | 🟢 **MIT** · `1,099 B` · `9030c75868f8` | `1` | Global | 🟢 **The first row in this base that automates the INSTRUCTIONAL DESIGN method rather than the teaching** — an agent that walks **ADDIE** (Analyse, Design, Develop, Implement, Evaluate). 🔵 `★1`, so it is a template; but ADDIE is the vocabulary a corporate-learning or ministry client uses to specify work, and no other row speaks it |
| **agent-craft** 🆕 | [`Annyfee/agent-craft`](https://github.com/Annyfee/agent-craft) | 🟢 **MIT** · `1,064 B` · `caea6648b806` | `536` | APAC | Agent-building toolkit surfaced by a Chinese-language 教学 (*teaching*) query. 🔵 **Not education-specific** — placed here with that stated, because it is the largest permissive result the in-language teaching query returns and it is what a Chinese-language team would reach for |

### 🔍 Carried rows, re-measured this pass

| Agent | Grant | ★ (exact) | Note |
|---|---|---|---|
| **DeepTutor** | 🟢 Apache-2.0 · `11,408 B` control reproduced | `58,575` | 🟢 Still the strongest permissive spine in the sector. `58,508` (`p790`) → `58,554` (`p791`) → **`58,575`** |
| **Study-Mate** | 🟢 **`TREE[MIT + MIT + OFL]`** | `1,436` | 🟢 **`p791-D` discharged — cleared on the full `363`-file tree.** The addition is `lib/katex/fonts/LICENSE`, **SIL OFL `4,616 B`**, unread at `p791`. Carry the OFL file, keep font names intact |

### 🔴 `p792` REFUSES nothing new, and re-confirms `5` absences instead

🟢 **The `5` standing ungranted rows were re-probed on the tree channel — a third consecutive confirmation.** These are the targets of `ACTION p791-A`, and the drafted requests are now in [`intel/licence-requests/`](../intel/licence-requests/).

| Repo | Files in tree | Licence paths | ★ | Last push | Status |
|---|---|---|---|---|---|
| [`narumi-mase/osaka-lesson-dataset`](https://github.com/narumi-mase/osaka-lesson-dataset) | `26` | 🔴 **`0`** | `0` | `2026-06-30` | 🔴 Ungranted. Japan's best education-AI artefact |
| [`silja-graf/Didaktikus-KI-Spezialist-f-r-Unterrichtsplanung-und-Beurteilung-nach-LP21`](https://github.com/silja-graf/Didaktikus-KI-Spezialist-f-r-Unterrichtsplanung-und-Beurteilung-nach-LP21) | `23` | 🔴 **`0`** | `0` | `2026-08-23` | 🔴 Ungranted. 🟢 **Full slug recovered this pass** — this base had carried it elided as `Didaktikus-…-LP21`, and an elided slug is not an address (see defect `D4`) |
| [`SoukhyadP991/Multilingual-NCERT-Doubt-Solver`](https://github.com/SoukhyadP991/Multilingual-NCERT-Doubt-Solver) | `18` | 🔴 **`0`** | `2` | `2026-01-13` | 🔴 Ungranted |
| [`TaoYu-ds/TutorMesh`](https://github.com/TaoYu-ds/TutorMesh) | `143` | 🔴 **`0`** | `1` | 🟢 **`2026-11-12`** | 🔴 Ungranted — **and pushed today**, so the author is active and reachable. 🟢 The best of the five to ask |
| [`mingxuanyan07-lgtm/ai-for-education-showcase`](https://github.com/mingxuanyan07-lgtm/ai-for-education-showcase) | `189` | 🟡 **`2` — and NEITHER grants the repo** | `0` | `2026-11-05` | 🔴 **Still ungranted, and this is `T886`.** The two paths are `Rethlas/LICENSE` (Apache-2.0, `11,558 B`) and `scripts/vendor/katex/LICENSE.txt` (MIT, `1,107 B`) — **both vendored subdirectories**. There is **no root grant**. A licence-path *count* would have rescued this row wrongly |


## 🆕 `p791` — two agents added, one count corrected, one candidate REFUSED, one tree re-audited

🟢 **Method unchanged from `p790` and extended once.** Existence via `git ls-remote` (exit status read directly). Grant by **anchored title lines** in the served licence bytes, reported as a **set** when the file is an anthology (`T875`). Stars are claim-channel reads of `search/repositories` with a `repo:` qualifier, which return **exact integers**. 🟢 **New instrument this pass:** `git clone --filter=blob:none --no-checkout --depth 1` followed by `git cat-file -p HEAD:<path>` — it enumerates the whole tree, is case-exact, and fetches only the blobs actually read. It is now the cheapest byte channel this base has, and it is what settled `T882`.

| Agent | Repo | Grant, on the bytes | ★ (exact) | Last push | Verdict for Globant |
|---|---|---|---|---|---|
| **Study-Mate** 🆕 | [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | 🟢 **MIT** · `1,064 B` · `1b105b8e1b6b` | `1,436` | `2026-11-06` | 🟢 **Added, and the most directly reusable new row this pass.** A multi-agent builder turns a one-sentence goal into a private course, then a **course-scoped RAG tutor** teaches it with **per-lesson citations**. 🟢 The citation scoping is the valuable part: it is the architecture that answers *"where did the tutor get this?"* — the question every education client asks. 🟡 `363` files; vendors KaTeX (`lib/katex/LICENSE`, MIT) — clean to the first layer |
| **tutor-gpt** 🆕 | [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | 🔴 **GPL-3.0** · `35,149 B` · `f288702d2fa1` | `932` | `2026-02-20` | 🟡 **Added with two warnings, because the trend digests that surface it state neither.** A *diagnosis-first* tutor — it reasons about the learner's state before answering, which is the pedagogically interesting part. 🔴 **It is GPL-3.0, not permissive**, so it is a boundary deployment, never an embed. 🔴 **And it is `~9` months stale** (`2026-02-20`), so treat it as a reference architecture to read, not a dependency to adopt. 🔵 Its licence is also a live `T875` specimen: §13 at line `552` *names* the Affero GPL and a substring grader returns `AGPL-3.0` — the grant is GPL-3.0 |
| **Educhain** ✏️ | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🟢 **MIT** · `1,092 B` · `b46290b36e7f` | 🔴 **`388`** | `2026-05-29` | ✏️ **CORRECTED — this base published `~9k★` (cycle 2) and `~12k★` (cycle 3). The exact count is `388`**, and a full name sweep finds no `educhain` anywhere above `★22`, so the figure described no real repository (`T881`). 🟢 **The tool is still genuinely useful** — MIT, document/YouTube-to-course generation — but it is a small, six-month-stale project and must be presented as one |
| **OpenMAIC** 🔍 | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟡 **`TREE[MIT root + LGPL + ARPHIC-PL + OFL + bespoke-CN font]`** · root `1,065 B` · `76abc5f13261` | `43,376` | `2026-11-12` | 🔍 **Carried row, re-audited on the full `4,388`-file tree, and the root grant is not the tree's grant (`T882`).** Tsinghua MAIC's multi-agent interactive classroom; the largest education-specific agent repository this base holds after DeepTutor, and pushed today. 🟢 Root and all `7` first-party sub-packages are MIT. 🔴 `packages/mathml2omml` is **LGPL**; the renderer ships **three font grants**, one of them a non-OSI Chinese-language licence with **no-rename** and **no-resale-as-product** terms. 🟢 Usable — **carry the font licences and keep font names intact** |
| **DeepTutor** 🔍 | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · `11,408 B` (control reproduced) | `58,554` | `2026-11-07` | 🟢 **Carried, and still the single strongest permissive starting point in the sector.** 🔵 **Count re-read this pass: `58,554`.** For scale on how fast this row moves, this base published `~22k` at cycle 2 and `~24k` at cycle 3; search-channel digests put it near `52,800` on `2026-11-01`. 🟢 Apache-2.0, agent-native, actively pushed — the default spine for a tutoring engagement |

### 🔴 `p791` REFUSES one candidate, and says why

| Candidate | Why it was surfaced | Why it is REFUSED |
|---|---|---|
| [`A-R007/Multi-Agent-Study-Assistant`](https://github.com/A-R007/Multi-Agent-Study-Assistant) | A GitHub trend digest presents it as *"6 specialized agents for personalized education"* — exactly the shape this base collects | 🔴 **There is no licence file anywhere in its tree.** `19` files enumerated on a blobless clone, `0` match `licen|copying|legal|terms|notice`; `search/repositories` independently returns `license: none`. 🔴 **No grant means no rights** — not "permissive by default". `★66`, last push `2025-11-04`, so it is also a year stale. 🔵 It is listed here rather than silently dropped, so the next pass does not spend the same probe on it |

🔵 **This refusal is the brief's rule working as intended: `fewer real rows always beat padding`.** `p791` adds `2` agents, corrects `1` count, re-audits `2` trees and refuses `1` candidate — and the refused row is the one a star-ranked digest would have published.


# Education AI agents — `p790`

**Every row below was verified this pass on two byte channels:** existence via `git ls-remote`
(exit status read directly, never through a pipe), and the licence grant by **clause presence** in
the served `LICENSE` bytes. No row is carried on a vendor claim, a star ranking or a blog.

🔴 **New rule this pass, and it reverses one of this base's own published verdicts (`T875`).** A
licence file may **quote other licences**. Grading one by substring presence is therefore unsound in
both directions: GPL-3.0's own §13 *names* the GNU Affero GPL, and a bundled dependency's
`All rights reserved.` line sits inside a file whose own grant is open. **A file containing `N`
licence titles is an ANTHOLOGY and has no single family** — it is graded by anchored title lines and
reported as a set. `Kosudo/nextSIS` is the row this cost, and it is corrected below.

> **Channel discipline (`T844`, amended this pass — `T860`).** Repository existence and licence
> bytes are **byte-verified**. 🔴 **The page channel is GONE this pass:** `github.com` returns
> `403` through this session's proxy for every non-attached repository, and so does
> `api.github.com/repos/{owner}/{repo}`. 🟢 **Stars below are claim-channel reads of
> `search/repositories` with `repo:` qualifiers — which return EXACT integers**, not GitHub's
> rounded `58.5k`, and which reproduced every rounded page-read `p787` published. Every market,
> adoption and regulatory figure in this base remains **search-channel testimony**.

**Controls for this pass:** 7 of 7 known-good rows reproduced the bytes this base already recorded
(`HKUDS/DeepTutor` 11,408 B · `moodle/moodle` 35,147 B · `sakaiproject/sakai` 11,120 B ·
`frappe/lms` 33,893 B · `hedyorg/hedy` 13,827 B · `jupyter/nbgrader` 1,512 B · `oppia/oppia`
11,358 B). 2 planted negatives were DEAD as designed. 🔴 **6 defects in this pass's own
instruments were caught by those controls and fixed before any verdict shipped** — see
`intel/trends.md` `T860`–`T863`.

🔴 **The one thing to read before using this file.** `p787-D` is discharged below and it changes how
every row here must be read: **a repository-level grant says nothing about the grant on its
dependencies, and 4 of the 7 highest-star permissive education repos carry copyleft in their
declared direct dependencies.** See `## Dependency grants` at the foot of this file.

## The two poles — both APAC-origin, both permissive at the repository level

| Agent | Address | Grant, on the bytes | ★ (exact) | Region | What it is |
|---|---|---|---|---|---|
| **DeepTutor** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · `11,408 B` · `60fb3bdfddb3` | `58,508` | APAC | Lifelong personalised tutoring workspace — tutoring, retrieval over the learner's own materials, practice, mastery tracking. **The most permissively-granted mature tutor in the sector.** ⚠️ **`pyte` (LGPL-3.0) is a declared direct dependency** (`T861`) |
| **OpenMAIC** | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | MIT · `1,065 B` · `717b69cbe2f4` | `43,365` | APAC | Tsinghua's Open Multi-Agent Interactive Classroom — turns a topic or document into a classroom with AI teacher and AI classmates, generating slides, quizzes, simulations and PBL activities. ⚠️ **2 of 181 direct dependencies are copyleft:** `mathml2omml` (LGPL-3.0-or-later) and `jszip` (`MIT OR GPL-3.0-or-later`, so the MIT arm must be **elected in writing**) |

## Teaching-as-a-skill — the packaging shift, now with a derivative in the wild

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **agent_skills** (`socratic-tutor`) | [`janestreet/agent_skills`](https://github.com/janestreet/agent_skills) | MIT · `1,120 B` · `7c6715c29548` | `6,813` | North America | Jane Street's skill set; the `socratic-tutor/` skill turns an LLM into a strict tutor — diagnostic, skill map with levels 0–5, one question at a time, spaced review, final assessment. **Tutoring shipped as a skill directory, not an application.** Canonical owner is `janestreet`; `jane-street/agent_skills` is DEAD |
| **socratic-tutor** `NEW` | [`nuwaves/socratic-tutor`](https://github.com/nuwaves/socratic-tutor) | MIT · `1,143 B` · `2e34df6e23bd` | `2` | Global | 🟢 **The first downstream derivative of the above, created `2026-11-09`** — the same skill extracted as a standalone, installable unit with saved progress. `T851` predicted this packaging would travel; it has, in under a week |
| **china-k12-teacher-skills** | [`myvipbackup2/china-k12-teacher-skills`](https://github.com/myvipbackup2/china-k12-teacher-skills) | Apache-2.0 · `11,359 B` · `f1c6c4420e7d` | `3` | APAC | China-localised K-12 teacher skills with curriculum-aware lesson planning |

## EMEA — the gap `p787` recorded as empty, and it is not

🟢 **`ACTION p787-E` discharged by refutation (`T862`).** `p787` searched for a European-origin
open-source education agent **in English**, found only sovereign-LLM infrastructure, and recorded the
slot as empty. Querying the same slot in **Dutch, German, French and Greek** returned agents on the
first attempt. Every row below is byte-verified and **new to this base**.

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **onderwijsin/agents** `NEW` | [`onderwijsin/agents`](https://github.com/onderwijsin/agents) | **MIT** · `1,079 B` · `0b3eabc034fa` | `0` | EMEA | 🟢 **The find that refutes `T856`.** Provider-agnostic AI plugins and skills for Dutch **onderwijs** (education). 🔵 Found by querying `onderwijs AI agent`, which returned **exactly one** repository — this one. At `0★` it is below every star floor this base has ever used |
| **sherpa** `NEW` | [`SeydinaBANE/sherpa`](https://github.com/SeydinaBANE/sherpa) | **MIT** · `1,063 B` · `6411f2de98c1` | `0` | EMEA | French-language exam-preparation tutor: **grounded RAG with citations** plus agents. 🔵 Citation-grounding is the single feature `T859` argues an education deliverable most needs |
| **parcours-maths-ia** `NEW` | [`Warok-dev/parcours-maths-ia`](https://github.com/Warok-dev/parcours-maths-ia) | **MIT** · `1,066 B` · `51dc673f15a0` | `0` | EMEA | 2D educational maths game for French **CE1–CE2** with automatic exercise generation — curriculum-specific, primary-level |
| **dowze** `NEW` | [`Louisdelez/dowze`](https://github.com/Louisdelez/dowze) | **MIT** · `1,068 B` · `2a30b43ecd06` | `0` | EMEA | French lifelong-learning AI tutor, explicitly framed as a **bien commun** (commons) |
| **skepsis** `NEW` | [`ionpetro/skepsis`](https://github.com/ionpetro/skepsis) | **MIT** · `1,072 B` · `31a864169289` | `3` | EMEA | Teaches the Greek hiding inside everyday English in 3-minute lessons; ships a web app **and an MCP server**, so another agent can teach from it |
| **eagle-aig** `NEW` | [`LIST-LUXEMBOURG/eagle-aig`](https://github.com/LIST-LUXEMBOURG/eagle-aig) | **Apache-2.0** · `11,358 B` · `99cecb066ecf` | — | EMEA | 🟢 **Luxembourg Institute of Science and Technology** — a national public research institute. **Rescued from this base's ungranted class this pass** (`p787-B`): it was filed as an absence and has carried Apache-2.0 all along |
| 🟢 **EduAgentic** `NEW` | [`kamalelafoui/Agentic-AI-EdTech-J33-J34`](https://github.com/kamalelafoui/Agentic-AI-EdTech-J33-J34) | 🟢 **MIT** · `1,071 B` · `7685db14663f` | `0` | EMEA (francophone) | 🟢 **The first EMEA row in this base that is an MCP **server** plus an A2A multi-agent system rather than an application** — six EdTech tools exposed over **MCP**, agents that **discover and delegate** over **A2A**, and a Streamlit dashboard to observe both. Dated `2026-11-11`. 🟢 **`100 % synthétiques · 0 apprenant réel`** — the author states on the record that no real learner data is present, which is the declaration an EMEA deployment has to make anyway. 🔵 Francophone, authored under a *Centre des Très Petites Entreprises Solidaires* programme; **the country is not stated in the repository and is not inferred here** |

### 🟢 `elimu-ai` — a 66-repository MIT African education ecosystem this base was already citing

🔴 **This base cited `elimu-ai` at `agents/trending.md:24964` and never placed it.** It surfaced only
because it was the **single false positive** of `p787-A`'s login-validity clause (`T863`). All seven
core repositories are **MIT, `1,065 B`, identical licence text, pushed within the last week.**

| Repo | Address | Grant, on the bytes | ★ | Role |
|---|---|---|---|---|
| **webapp** | [`elimu-ai/webapp`](https://github.com/elimu-ai/webapp) | MIT · `1,065 B` · `f471cb573ae3` | `41` | Hosts the Android applications and the educational content library |
| **appstore** | [`elimu-ai/appstore`](https://github.com/elimu-ai/appstore) | MIT · `1,065 B` · `65a7ab4e8d50` | `29` | On-device APK download/install/update — **content delivery without an app store**, which is the binding constraint it is built for |
| **ml-authentication** | [`elimu-ai/ml-authentication`](https://github.com/elimu-ai/ml-authentication) | MIT · `1,065 B` · `0a7a6bb02ab6` | `16` | On-device student authentication. ⚠️ Biometric identification of children — read `T854` and EU Art. 5 before deploying this in EMEA or North America |
| **launcher** | [`elimu-ai/launcher`](https://github.com/elimu-ai/launcher) | MIT · `1,065 B` · `b50a175a7056` | `9` | Android launcher that constrains the device to a single instructional path |
| **ml-storybook-reading-level** | [`elimu-ai/ml-storybook-reading-level`](https://github.com/elimu-ai/ml-storybook-reading-level) | MIT · `1,065 B` · `119642b8b1c3` | `8` | 🟢 ML model predicting a storybook's reading level — **a real, permissive levelling model**, which no other row in this base supplies |
| **ml-storybook-recommender** | [`elimu-ai/ml-storybook-recommender`](https://github.com/elimu-ai/ml-storybook-recommender) | MIT · `1,065 B` · `940048e2cc32` | `3` | Predicts likability of unread storybooks |
| **model** | [`elimu-ai/model`](https://github.com/elimu-ai/model) | MIT · `1,065 B` · `5f16dd17e351` | `4` | Shared library across the webapp and the Android apps |

## APAC — `ACTION p787-F` discharged, and the three countries differ completely

### 🟢 India — the region's richest curriculum-specific supply

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| **OpenVidya** `NEW` | [`dpaul0501/OpenVidya`](https://github.com/dpaul0501/OpenVidya) | 🔴 **AGPL-3.0** · `34,523 B` · `1224dcd5693b` | `2` | 🟢 **The most strategically interesting row of the pass: an OpenMAIC derivative redesigned for NCERT/CBSE.** 🔴 **And it relicensed upward** — OpenMAIC is MIT, this fork is AGPL-3.0. MIT permits that, and it means the India-localised classroom **cannot** be embedded in a client deliverable the way its parent can |
| **RAG-Enhanced-NCERT-Tutor** `NEW` | [`praj2408/RAG-Enhanced-NCERT-Tutor`](https://github.com/praj2408/RAG-Enhanced-NCERT-Tutor) | MIT · `1,072 B` · `adf4c082db90` | `5` | Retrieval-grounded tutor over the **NCERT** national curriculum |
| **CBSE_Home-Tutor** `NEW` | [`mandarab76/CBSE_Home-Tutor`](https://github.com/mandarab76/CBSE_Home-Tutor) | MIT · `1,077 B` · `f987f634f5e0` | `1` | **CBSE** tutor spanning classes 1–12 |
| **ai-agent-to-learn-faster-and-better** `NEW` | [`abhijeetgupta23/ai-agent-to-learn-faster-and-better`](https://github.com/abhijeetgupta23/ai-agent-to-learn-faster-and-better) | MIT · `1,071 B` · `df69fd3331dd` | `4` | Adaptive tutor that personalises **lesson modality** from a learning-science knowledge graph |
| **FunctionVisualizer-V3** `NEW` | [`Adarsh-61/FunctionVisualizer-V3`](https://github.com/Adarsh-61/FunctionVisualizer-V3) | MIT · `1,056 B` · `10099c811f61` | `3` | Interactive NCERT mathematics visualisation |
| **NCERT-AI-Teacher-Assistant** `NEW` | [`Prady029/NCERT-AI-Teacher-Assistant`](https://github.com/Prady029/NCERT-AI-Teacher-Assistant) | 🔴 GPL-3.0 · `35,149 B` · `5e24bf860660` | `5` | Lesson plans and question sets for teachers. 🔴 Copyleft |

🟢 **`p787-F`'s India finding, stated plainly:** India's gap was never supply, it was **vocabulary**.
`tutor agent education India curriculum` returned `0`. `NCERT AI` returned **`330`**.

### 🟢 South Korea — placed for the first time, behind a semantic trap

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| **spring-ai-tutor** `NEW` | [`jungtaejin/spring-ai-tutor`](https://github.com/jungtaejin/spring-ai-tutor) | MIT · `1,069 B` · `8ca838adabcc` | `0` | Korean tutoring API on Spring AI — structured output, conversation memory, tool calling, SSE streaming |
| **Haeksim** `NEW` | [`Seongbong-Ha/Haeksim`](https://github.com/Seongbong-Ha/Haeksim) | MIT · `1,069 B` · `242b3f09aa73` | `0` | 핵심 ("core") — an NLP AI learning-tutor project |

🔴 **The trap, recorded because it will recur.** Korean **교육** means both *education* and
*corporate training*. The query `AI 교육 에이전트` returned `20` repositories of which **almost none
are education agents** — they are agent-training course materials (a Samsung practitioner
curriculum, "AI maestro" week-4 coursework). 🟢 The productive query was `학습 튜터 AI`
(*learning tutor*), which returned `12`. **A word that means two things returns the wrong head.**

### 🟢 Japan — the measured gap, DISCHARGED, and it was a category error (`p789`)

🔴 **`p788` measured Japan at `3` repositories and called it this base's only *measured* supply
gap, surviving in-language querying.** 🟢 **It does not survive the right *category*.** Japanese
education-AI work is published under **`校務`** (*kōmu* — school administrative duties), not under
tutoring vocabulary. The supply is **administrative and curricular, not conversational** — the
opposite of the Indian and Chinese supply this base has placed (`T870`).

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| 🟢 **jp-k12-digital-ai-textbook** `NEW` | [`masa-san-jp/jp-k12-digital-ai-textbook`](https://github.com/masa-san-jp/jp-k12-digital-ai-textbook) | 🟢 MIT · `1,068 B` · `d7c583c9f444` | `1` | 🟢 **The best Japan-origin education artefact this base has placed, and it is permissive.** All `12` grades (小1–高3), aligned to the **next 学習指導要領** *and* the **UNESCO AI Competency Framework** |
| 🟢 **school-office-generative-ai-30** `NEW` | [`kumaken-1/school-office-generative-ai-30`](https://github.com/kumaken-1/school-office-generative-ai-30) | 🟢 **MIT · `1,102 B` · `c42f19d27c4d`** (`LICENSE-CODE`) **+ CC BY 4.0 · `925 B` · `738b8fc14a61`** (`LICENSE-CONTENT`) | `0` | 「生成AI 30のチャレンジⅡ〜校務編〜」 — `30` graded exercises on real school-administration tasks for staff who have finished an introductory course. 🔵 Its split grant is defect `7` of this pass (`T869`) |
| 🟡 **tracen-ai-tazuna** `NEW` | [`naritaroad/tracen-ai-tazuna`](https://github.com/naritaroad/tracen-ai-tazuna) | 🟢 MIT · `1,067 B` · `5aff4e618c56` | `0` | A school **administrative** AI proof-of-concept. 🔴 **Barred from client work despite its grant:** an unofficial *Uma Musume* fan project — MIT covers the authors' code, never the franchise's trademarks or characters |

🔴 **The one that is barred, which is the useful half of the finding.**
[`nahisaho/teacher-genai-playbook`](https://github.com/nahisaho/teacher-genai-playbook) — teacher
generative-AI training material for classroom *and* `校務` use, the most engagement-shaped Japanese
artefact found — is **CC BY-NC 4.0 · `1,222 B` · `92625a14d19b`. NonCommercial: it cannot be used in
a paid engagement.** The search channel said `NOASSERTION`; the bytes name the bar precisely.
🔴 Also measured: [`chc-chupea/news-grade-reader`](https://github.com/chc-chupea/news-grade-reader)
**GPL-3.0 · `35,149 B` · `3972dc9744f6`** — grade-levelled news rewriting against MEXT curriculum
guidance, copyleft, and it states in terms that it is *not* MEXT-endorsed.

🔵 **Measured Japanese totals, so the shape of the supply is on the record:** `校務 AI` → **`5`** ·
`塾 AI 学習` → **`7`** · `学習指導要領 AI` → **`2`** · `教育 LLM 日本語` → **`1`** ·
`授業 支援 AI 教材` → **`0`**. 🔴 [`narumi-mase/osaka-lesson-dataset`](https://github.com/narumi-mase/osaka-lesson-dataset)
remains **ungranted** and remains worth asking for.

### 🟢 Malaysia — `p789`'s declared gap, DISCHARGED (`p790`)

🔴 `p789` recorded Malaysia as one of its three thinnest *measured* regions at **`1`, ungranted**.
🟢 **It is now placed, and the repository is granted.**

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| 🟢 **StudyLah** `NEW` | [`haziqhalifi/StudyLah`](https://github.com/haziqhalifi/StudyLah) | 🟢 MIT · `1,069 B` · `c6ee7bb5db4a` | `0` | 🟢 **Malaysia placed.** Adaptive learning for **SPM Form 5 Mathematics**: diagnostic quiz inferring misconceptions per topic, next-question selection from weakest topic + recent accuracy trend, generated MCQs targeting measured skill gaps, spaced-repetition scheduling — and **explanations written in Bahasa Malaysia**. 🔵 It also matches *explanation style* (step-by-step / formula-first / shortcut / analogy) to measured accuracy, which is a pedagogy choice almost no row in this base makes explicit. ⚠️ Hackathon-origin, single contributor |

🔵 **Measured Malaysian totals, so the shape is on the record:** `AI tutor SPM Malaysia` → **`1`** ·
`tutor AI pendidikan Malaysia` → **`0`**. 🔴 **The supply is one repository.** It is placed because it
is real and granted, not because it is deep — and the national demand behind it is large
(`intel/market.md`, APAC).

### China

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| **AI-tutor** `NEW` | [`qiyuxi24/AI-tutor`](https://github.com/qiyuxi24/AI-tutor) | MIT · `1,065 B` · `046f65596541` | `4` | Knowledge-graph-driven guidance agent: knowledge map, learning path, learner profile, question generation. `413` test cases, L1–L4 live-API evaluation, BM25 gating with RRF hybrid retrieval — **the most explicitly evaluated small agent in this base** |
| **VeryMath-textbook-copilot** | [`VeryMath/VeryMath-textbook-copilot`](https://github.com/VeryMath/VeryMath-textbook-copilot) | Apache-2.0 · `11,338 B` · `1183af0d8197` | `21` | Textbook pane beside a coding-agent pane: explanations, exercises, mind maps, knowledge graphs, LaTeX courseware |
| **Math-Modeling-Agent-Flow** | [`mantou6666/Math-Modeling-Agent-Flow`](https://github.com/mantou6666/Math-Modeling-Agent-Flow) | MIT · `1,067 B` · `69b2a4f15995` | `28` | Four-stage Solver→Paper pipeline for the CUMCM / MCM-ICM modelling competitions |
| **xuelian-agent** | [`llwand1/xuelian-agent`](https://github.com/llwand1/xuelian-agent) | MIT · `1,062 B` · `956783be029f` | — | Chinese-language study agent |

## 🟢 School operations — `p788`'s standing gap, discharged with `5` permissive rows (`p789`)

🔴 **`p788`: "School-operations agents (timetabling, attendance, safeguarding) — still no
permissive row."** 🟢 **There are five, and the category has a genuine architectural signature: a
constraint solver with a human approval gate, not a chatbot** (`T874`).

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| 🟢 **schoolflow-agent** `NEW` | [`Zahraishag/schoolflow-agent`](https://github.com/Zahraishag/schoolflow-agent) | 🟢 MIT · `1,081 B` · `1b7481d92d0f` | `0` | Global | 🟢 **The row the gap was asking for.** Timetable **disruptions**, teacher absences and substitutions, with **human-approved** schedule updates. 🔵 The approval gate is the project's own design, not this base's retrofit |
| 🟢 **school-timetable-timefold-case-study** `NEW` | [`paoloantinori/school-timetable-timefold-case-study`](https://github.com/paoloantinori/school-timetable-timefold-case-study) | 🟢 MIT · `1,081 B` · `12e2a597e655` | `1` | Global | 🟢 **The reference architecture for the category:** a real **constraint solver** (Timefold) on Quarkus, driven by coding agents. Scheduling is a solver problem with an LLM at the edges |
| 🟢 **Timable** `NEW` | [`Nayak-indie/Timable`](https://github.com/Nayak-indie/Timable) | 🟢 Apache-2.0 · `11,357 B` · `c71d239df917` | `1` | Global | High-school timetabling on **OR-Tools** + Streamlit. The second independent solver row, which is what makes it a pattern rather than a project |
| 🟢 **classcharts-agent** `NEW` | [`shan8851/classcharts-agent`](https://github.com/shan8851/classcharts-agent) | 🟢 MIT · `1,066 B` · `65ef4f07f833` | `0` | EMEA 🇬🇧 | 🟢 **Read-only** CLI and agent skill over **ClassCharts** (UK homework/behaviour system). 🔵 A deliberately read-only attachment to a live school system — the safest first integration, and this base's second EMEA LMS/MIS attachment point after `brightspace-d2l-mcp` |
| 🟢 **TIMETABLE-SOFTWARE** `NEW` | [`jeevanjacob1/TIMETABLE-SOFTWARE`](https://github.com/jeevanjacob1/TIMETABLE-SOFTWARE) | 🟢 MIT · `1,056 B` · `1126322e2cc8` | `0` | Global | Clash-free generator on React + TypeScript + Supabase — the web-stack variant of the same job |
| 🟢 **ai-adoption-education** `NEW` | [`VictorOsondu/ai-adoption-education`](https://github.com/VictorOsondu/ai-adoption-education) | 🟢 **CC BY 4.0 content + MIT code**, one `752 B` file · `2e9c34096bf9` | `2` | Global | 🟢 **Safeguarding-first** AI adoption guidance for schools and higher ed, with task-suitability and assessment-integrity material. 🔵 Search channel said `NOASSERTION`; the bytes grant **commercial** use with a named attribution string |

🔴 **Ungranted in this category and worth asking for:**
[`NSK-394/schoolbridge-mcp`](https://github.com/NSK-394/schoolbridge-mcp) — an MCP server giving
agents **role-based** access to school ERP data (attendance, fees, student records). 🔵 Role-based
access over an SIS is exactly the control surface a school engagement needs.
🔴 [`zulfahmi93/susun-jadual`](https://github.com/zulfahmi93/susun-jadual) 🇲🇾 — Malaysian
*sekolah rendah/menengah* timetabling, ungranted; **Malaysia remains unplaced.**

## 🟢 Africa — Nigeria and South Africa placed for the first time (`p789`)

🔴 **`p788`: "African national curricula other than Kenya's CBC and Morocco's Bac — none found."**
🟢 **They exist in quantity.** `WAEC AI tutor` alone returns **`35`** repositories. 🔴 **And `32` of
them serve no grant** — the ratio is the finding, not the count (`T871`).

| Agent | Address | Grant, on the bytes | ★ | Country | What it is |
|---|---|---|---|---|---|
| 🟢 **Offline-First-Android-AI-Tutoring-App** `NEW` | [`thesavvybyjude/Offline-First-Android-AI-Tutoring-App`](https://github.com/thesavvybyjude/Offline-First-Android-AI-Tutoring-App) | 🟢 MIT · `1,070 B` · `a2fe733bd153` | `1` | 🇳🇬 NG | 🟢 **The headline African row, and the artefact `p788` asked for by name.** `p788` flagged an offline NCERT doubt-solver as "exactly the shape a low-connectivity engagement needs" **and had to file it ungranted**. This is that shape for Africa **with a grant**: on-device LLM, RAG over the **WAEC/NERDC** curriculum, spaced repetition |
| 🟢 **ai-tutor-app** `NEW` | [`nitoni-jim/ai-tutor-app`](https://github.com/nitoni-jim/ai-tutor-app) | 🟢 MIT · `1,074 B` · `d33e0685ea0f` | `1` | 🇳🇬 NG | Intelligent tutoring system over **WAEC / NECO / JAMB** — all three Nigerian examination boards in one tree |
| 🟢 **waec-ai-tutor** `NEW` | [`Ass-Gaye/waec-ai-tutor`](https://github.com/Ass-Gaye/waec-ai-tutor) | 🟢 MIT · `1,065 B` · `54383781845a` | `0` | 🇳🇬 NG | The third permissive WAEC row of the `35` |
| 🟢 **homework-hero-sa** `NEW` | [`Masondo86/homework-hero-sa`](https://github.com/Masondo86/homework-hero-sa) | 🟢 MIT · `1,070 B` · `88eb94d99d6c` | `0` | 🇿🇦 ZA | 🟢 **South Africa placed for the first time.** Homework scheduling and learner accountability on the **CAPS** curriculum — an operations tool, not a tutor |
| 🟢 **nextgen-learn** `NEW` | [`daddysystem/nextgen-learn`](https://github.com/daddysystem/nextgen-learn) | 🟢 **BSL-1.0 (Boost) · `1,338 B` · `c9bff7573892`** | `0` | 🇿🇦 ZA | Free **CAPS**-following study site with an AI tutor. 🟢 **A licence family new to this base:** Boost is permissive, OSI-approved, and waives attribution for object-code-only distribution |

#### 🔴 Tanzania, Ghana and Kenya — probed this pass, and NOT discharged (`p790`)

🔴 **`p789` named Tanzania (`0`), Ghana (`1`, ungranted) and Malaysia (`1`, ungranted) as its
thinnest measured regions. Malaysia is discharged above. The two African ones are not, and the
reasons differ.**

| Country | What was measured | Verdict |
|---|---|---|
| 🔴 🇹🇿 **Tanzania** | `elimu AI Tanzania` → **`2`**. One is ungranted (`kadioko/ElimuAI`, Swahili e-learning with M-Pesa). The other, [`sangadanson1-dot/-Vet-IDEA-TZ`](https://github.com/sangadanson1-dot/-Vet-IDEA-TZ), **is MIT · `1,067 B` · `238c1bbb3bc0`** | 🔴 **NOT DISCHARGED — and the MIT row is a CATEGORY ERROR IN THE OPPOSITE DIRECTION FROM JAPAN'S (`T877`).** Read in Swahili, `Vet Idea TZ` serves **wafugaji na wataalamu wa mifugo** — livestock keepers and veterinary professionals. It teaches **afya ya wanyama, magonjwa, chanjo, lishe** (animal health, disease, vaccination, nutrition). 🟢 It is real, granted, AI-bearing education — **veterinary extension education, not school education.** 🔵 Placing it would have discharged the gap on paper and left a client engagement with nothing. **Tanzania's school-education agent supply is still `0`** |
| 🔴 🇬🇭 **Ghana** | `WASSCE AI tutor` → **`11`**; `Ghana education AI tutor curriculum` → **`0`**. `5` probed on the byte channel: `3` ALIVE serving **no grant**, 🔴 **`2` CORRECTED at `p793` from "DEAD" to ALIVE-BUT-EMPTY** (`Bestisco/My-WASSCE-Companion`, `Elite2828/ACE-AI-Tutor` — both `rc=0` with **zero refs**; they clone, hold no `HEAD`, and `raw` serves `404`. 🟢 **Existing, owner-claimed, never pushed — so `2` reachable authors, not `2` dead ends.** `T892`) | 🔴 **NOT DISCHARGED, and now QUANTIFIED rather than estimated.** `p789`'s "`1`, ungranted" understated the supply by about `10×` and read the grant correctly. 🟢 **Ghana's WASSCE supply is substantial and its grant rate is `0`** — the same shape `T871` recorded for Africa generally, measured at one country. 🔵 **And the search index is stale here specifically:** `2` of `5` addresses it returned no longer exist |
| 🔴 🇰🇪 **Kenya** | `AI tutor Kenya CBC curriculum` → **`3`**, all probed. `2` serve no grant | 🔴 **The third is a HARDER bar than an absence.** [`gabrielmahia/shule-ai`](https://github.com/gabrielmahia/shule-ai) — KCPE/KCSE prep on the **CBC** syllabus answering in Kiswahili — serves **`209 B` · `9dd285c3704d`: Creative Commons `CC BY-NC-ND 4.0`**. 🔴 **NonCommercial *and* NoDerivatives — it cannot be used in a paid engagement and cannot be modified at all**, which bars even the adaptation a curriculum row exists for. 🔵 **The search channel indexed it `NOASSERTION`.** Third consecutive pass in which index silence hid a grant, and the second in which the hidden grant was a *bar* (`T863`) |

🔵 **The useful sentence for an African engagement, now measured across four countries:** Nigeria and
South Africa are **placed and granted** (`5` rows above); **Ghana, Kenya and Tanzania have real
supply and no usable grant.** The remedy is the same in all three and it is not engineering — it is
an upstream licence request, carried as `ACTION p790-B`.

🔵 **Measured African totals, so the remaining gaps are informed ones:** `WAEC AI tutor` → **`35`**
(`3` permissive) · `CAPS curriculum South Africa AI` → **`10`** (`2` permissive) ·
`Nigeria curriculum AI tutor` → **`6`** · `BECE Ghana AI education` → **`1`**, and it is ungranted
([`ghwmelite-dotcom/brilla-study-platform`](https://github.com/ghwmelite-dotcom/brilla-study-platform),
BECE/WASSCE/NSMQ) · `NECTA Tanzania education AI` → 🔴 **`0` — a measured zero, not an unexamined silence.**

🔴 **Ungranted and worth asking for:** [`7irelo/aptiverse`](https://github.com/7irelo/aptiverse) 🇿🇦
`4★` — CAPS-aligned practice tests with **auditable marking**, the highest-starred and most
engagement-shaped African artefact found; and
[`tosinamuda/teacher-agent-itu-hackathon`](https://github.com/tosinamuda/teacher-agent-itu-hackathon)
🇳🇬 — *Plan-to-Tutor*, a **teacher-in-the-loop** agent on the Nigerian curriculum from the
**ITU AI for Good** Lab hackathon. 🔵 Teacher-in-the-loop and auditable marking are the two design
choices this base keeps recommending — both found in African repositories, both ungranted.

## Tutors and adaptive engines

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | MIT · `1,105 B` · `fae8cc474484` | `279` | North America | UC Berkeley (CAHLR) adaptive tutoring with **Bayesian Knowledge Tracing** mastery estimation. 🟢 **`0` of `43` direct dependencies are copyleft — the cleanest dependency tree measured this pass** |
| **OpenTutor** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | MIT · `1,068 B` · `cfe41f874290` | `175` | Global | Block-based adaptive learning workspace that runs locally. 3 specialist agents (Tutor, Planner, Layout), 10+ LLM providers. 🟢 `1` direct dependency, `0` copyleft. ⚠️ `cosark/OpenTutor` is a FORK at `0★` |
| **examprep-agent** `NEW` | [`ZeKaiNie/examprep-agent`](https://github.com/ZeKaiNie/examprep-agent) | MIT · `1,065 B` · `83fad934ea90` | `1` | Global | Study agent that teaches **only** from the learner's own slides and homework — a scoping constraint, not a limitation |
| **claude-study-agent** `NEW` | [`dymchenkko/claude-study-agent`](https://github.com/dymchenkko/claude-study-agent) | MIT · `1,067 B` · `527f9ac590a0` | `3` | Global | University-course study agent built on a coding-agent host, learning from the learner's own slides and PDFs |
| **lessonfolk** `NEW` | [`CGSeb/lessonfolk`](https://github.com/CGSeb/lessonfolk) | MIT · `1,063 B` · `7710ddf025ab` | `3` | Global | Learn AI from zero to advanced with an agent as the tutor |
| **algebench** `NEW` | [`ibenian/algebench`](https://github.com/ibenian/algebench) | MIT · `1,063 B` · `6794217849f9` | `8` | Global | Interactive **3D** maths visualiser with an agentic tutor — concepts explored through live simulation |
| **rag-tutor** `NEW` | [`villadalmine/rag-tutor`](https://github.com/villadalmine/rag-tutor) | **Apache-2.0** · `7,450 B` · `b0bc280f04ec` | `2` | Global | Sovereign, local-first tutor over technical books: hybrid RAG + agentic loop + MCP server. 🔴 **GitHub indexes this `NOASSERTION`; the bytes are Apache-2.0 with all `9` operative sections verified individually** — the `3,907 B` shortfall is the omitted non-operative APPENDIX only (`T845`: length is not a verdict) |
| **Thesaurus** `NEW` | [`Ahhsaaaaan/Thesaurus`](https://github.com/Ahhsaaaaan/Thesaurus) | Apache-2.0 · `11,343 B` · `dc29f0d739ff` | `0` | Global | Classroom knowledge base: teachers upload course documents, students query them over RAG |
| **Learning-Agent-System** | [`VaishnaviSingh-Analyst/Learning-Agent-System`](https://github.com/VaishnaviSingh-Analyst/Learning-Agent-System) | MIT · `1,086 B` · `fb2da327c928` | — | Global | LangGraph tutor on Ollama: checkpointed learning paths, tiered 5-3-2 assessment, a 70% pass bar, Feynman-style re-teaching |
| **no-vibe** | [`rizukirr/no-vibe`](https://github.com/rizukirr/no-vibe) | MIT · `1,065 B` · `5b8cb2f6d072` | `48` | Global | Turns a coding agent into a tutor that reads the learner's level and adapts — pedagogy applied to the agent rather than the content |
| **llm-edu-suite** `NEW` | [`ZoodiacR/llm-edu-suite`](https://github.com/ZoodiacR/llm-edu-suite) | MIT · `1,065 B` · `da605cdaf27e` | `3` | Global | Learn LLM engineering by building and measuring each layer — tokenizer, transformer, pre-training |
| 🟢 **coursewright** `NEW` | [`shivarajbakale/coursewright`](https://github.com/shivarajbakale/coursewright) | 🟢 MIT · `1,072 B` · `4fd5e20735ab` | `0` | Global | Name a subject; **a team of agents writes the course** — chapters from first principles, step-by-step diagrams, quizzes, projects, notes beside every chapter, and a tutor that answers **from the generated course only**. 🔵 The scoping constraint (`examprep-agent`'s virtue) applied to *generated* rather than supplied material |
| 🟢 **spanish-tutor-ai** `NEW` | [`MrEug3n1o/spanish-tutor-ai`](https://github.com/MrEug3n1o/spanish-tutor-ai) | 🟢 MIT · `1,069 B` · `6f0ebd566861` | `0` | Global | 🟢 **The most complete local-only tutor this base has placed, and the sovereignty pattern's best single reference.** Runs **entirely on local open-source models — no API keys, no per-token bill** — and checks its own work: chat tutor with tools, synthetic-data generator, retrieval over grammar notes, a **QLoRA-fine-tuned** article checker, and an agent that **plans each day's lesson itself**. Wrong quiz answers return the topic to tomorrow's plan. 🔵 Named for the language taught, not a region — it is `P788-4`'s missing reference implementation |
| 🟢 **Multimodal-RAG-AI-Tutor-Agent** `NEW` | [`yashpandey2409/Multimodal-RAG-AI-Tutor-Agent`](https://github.com/yashpandey2409/Multimodal-RAG-AI-Tutor-Agent) | 🟢 MIT · `1,068 B` · `59d3fe71eea6` | `0` | Global | Multimodal retrieval-grounded tutor — the multimodal variant of the citation-grounded shape `T859` argues an education deliverable most needs |
| **learnharness** | [`amosblomqvist/learnharness`](https://github.com/amosblomqvist/learnharness) | 🔴 **AGPL-3.0** · `34,523 B` · `cb25c8e49b85` | — | Global | Agent harness for learning difficult subjects. 🔴 **Copyleft: network-use triggers source disclosure** — reference or separately-deployed service only |

## Assessment and grading

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **GradeAI** | [`orancs11/GradeAI`](https://github.com/orancs11/GradeAI) | MIT · `1,061 B` · `93bd8bebe253` | `4` | Global | Automated grading. Small, but the grant is clean and the scope is exactly what EU Annex III and several US states now regulate |
| **instructional_agents** | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | MIT · `1,067 B` · `f835eb45f508` | — | Global | Multi-agent generation of instructional material and courseware |

## LATAM

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **TutoriasITA** | [`Frangersal/TutoriasITA`](https://github.com/Frangersal/TutoriasITA) | MIT · `1,077 B` · `3184f6e7f75a` | `7` | LATAM | Institutional tutoring system, **Tecnológico Nacional de México, Campus Acapulco** |
| **TutorLSM** | [`ftrujillo36/TutorLSM`](https://github.com/ftrujillo36/TutorLSM) | Apache-2.0 · `11,357 B` · `ae26aa487282` | `0` | LATAM | **Mexican Sign Language (LSM)** learning and practice — accessibility supply in Spanish, permissively granted |
| **paes-mcp** | [`goyanedelv/paes-mcp`](https://github.com/goyanedelv/paes-mcp) | **MIT (Spanish text)** · `2,018 B` · `84e7f6106b38` · 🔴 **SCOPE-LIMITED** | `0` | LATAM | MCP server over Chile's **PAES** university-admission test. 🔴 **CORRECTION TO `p787` (`T864`): the MIT grant covers the SOURCE CODE AND DOCUMENTATION ONLY.** The licence text states in terms that it does *not* — and *could* not — cover the PAES items, figures and answer keys, whose rights belong to **DEMRE, Universidad de Chile**; that material is included from freely published official sources for educational use with attribution. **`P787-3` was built on this row as though the corpus were MIT. It is not** |
| **teams-facultad-mcp** | [`Matias-Sanmiguel/teams-facultad-mcp`](https://github.com/Matias-Sanmiguel/teams-facultad-mcp) | MIT · `1,088 B` · `17b51f4db2b0` | `0` | LATAM | Local MCP server over Teams Educación — coursework, announcements, documents |
| **Tlamatini** `NEW` | [`XAIHT/Tlamatini`](https://github.com/XAIHT/Tlamatini) | MIT · `1,062 B` · `b1f06f7e736f` | `15` | LATAM | Speak an idea, build the real thing: voice-driven AI into code, 3D worlds and hardware. 🔵 **`Tlamatini` is Nahuatl for *one who knows*** — named in an Indigenous Mexican language, which is why no English query reaches it |
| 🟢 **bncc-lesson-generator** `NEW` | [`iagommendes/bncc-lesson-generator`](https://github.com/iagommendes/bncc-lesson-generator) | 🟢 MIT · `1,068 B` · `171e1db7278e` | `0` | LATAM 🇧🇷 | 🟢 **BRAZIL PLACED FOR THE FIRST TIME, and against the country's brand-new national framework.** Open-source lesson-plan generator aligned to the **BNCC**: the teacher fills an ordinary form, the system assembles the pedagogical prompt behind the scenes and returns a structured A4/PDF plan. **"Zero-prompt para o professor"** — the teacher never writes a prompt, which is the single biggest adoption barrier `T876` names. Next.js + TypeScript; the public demo runs on mocked data, real generation needs your own key |
| 🟢 **mi_icfes** `NEW` | [`jolicastrog/mi_icfes`](https://github.com/jolicastrog/mi_icfes) | 🟢 MIT · `1,068 B` · `1c05d19ed1d3` | `0` | LATAM 🇨🇴 | 🟢 **COLOMBIA PLACED FOR THE FIRST TIME.** PWA that **predicts** a **Saber 11** result. ⚠️ **Read the use before the grant:** predicting a student's state-examination outcome is score *prediction*, not tutoring — under the EU AI Act this shape is Annex III high-risk, and it is the one LATAM row in this base that a North American or EMEA client could not simply re-deploy |
| 🟢 **awesome-ia-sala-de-aula** `NEW` | [`ciro-maciel/awesome-ia-sala-de-aula`](https://github.com/ciro-maciel/awesome-ia-sala-de-aula) | 🟢 **CC0-1.0** · `7,049 B` · `be5467501439` | `0` | LATAM 🇧🇷 | Curated register of classroom AI assistants **with each one's minimum age and privacy posture, and the Brazilian education rules that apply**. 🟢 **CC0 is a new licence family for this base and the most permissive grant it holds** — a public-domain dedication, no attribution condition at all. 🔵 Its subject matter is exactly `P790-1`'s compliance input |
| 🔴 **GenPrompt-Pre-ICFES-11** `NEW` | [`CREARED-EDU-CO/GenPrompt-Pre-ICFES-11`](https://github.com/CREARED-EDU-CO/GenPrompt-Pre-ICFES-11) | 🔴 **AGPL-3.0** · `34,523 B` · `1ca3134446d7` | `4` | LATAM 🇨🇴 | Generator producing thousands of distinct Pre-**ICFES** grade-11 prompts — **the highest-starred Colombian education-AI repository measured**. 🔴 **Copyleft, and network use triggers disclosure:** reference or separately-deployed service only, never embedded in a client deliverable |

## 🟡 The largest permissive education-agent repository set this base has met — and what it actually contains

| Address | Grant, on the bytes | Measured | Verdict |
|---|---|---|---|
| 🟡 **education-ai-ecosystem** `NEW` | [`jinlize-tech/education-ai-ecosystem`](https://github.com/jinlize-tech/education-ai-ecosystem) | 🟢 **Apache-2.0** · `11,358 B` · `b59ceae4181d` · licence sha `cfc7749b96f6` | **`132` repositories in the org; `100` of `100` sampled are Apache-2.0** | 🟡 **Real grant, real scale, and by its OWN README mostly unbuilt** |
| 🟡 **edu-ai-usage-policy-agent** `NEW` | [`jinlize-tech/edu-ai-usage-policy-agent`](https://github.com/jinlize-tech/edu-ai-usage-policy-agent) | 🟢 **Apache-2.0** · `11,358 B` · `dab9f0cd5a3c` · **identical licence sha `cfc7749b96f6`** | — | 🟢 The one member most relevant here: an **AI-usage-policy** agent, which is the artefact every regulated engagement in `intel/market.md` needs |

🟢 **The claim checked out and the honesty is the finding.** The hub declares **`130` products — `97`
Skills and `33` Agents**, each in its own repository, all Apache-2.0. `search/repositories` returns
**`132`** repositories for the owner and **`100` of `100`** sampled carry Apache-2.0, so *the
licensing claim is true at scale* — this is, by a wide margin, the largest permissively-granted
education-agent repository set this base has ever measured.

🔴 **And its own README states what it has not got:** `WorkBuddy platform validation: 0/130,
NOT_EXECUTED` · `GitHub Release verified: 30/130` · *"They do not prove WorkBuddy parsing,
installation, model behavior, review, or publication."* Sampled agent repositories are described
`Agent | … | Planned / 待研发` — **planned / to be developed.** The agents are organised by business
centre (招生营销 admissions-marketing, 教学教研 teaching-research, 教务运营 academic-operations,
财务运营 finance, 人力组织 HR, 校区标准化 multi-campus standardisation).

🔵 **So it is placed as `2` rows with a measured org count, not as `33` agents (`T878`).** Writing
"`33` education agents, Apache-2.0" would have been the single largest padding event available to
this base this pass, and the repository itself supplies the refutation. 🟢 **What it is genuinely
worth:** a **product taxonomy for the education back office** — the `8`-centre decomposition is
reusable intelligence even where the code is not, and `edu-ai-usage-policy-agent` addresses a need
`P790-1` has to meet anyway.

## Agent-adjacent infrastructure this base composes with

| Component | Address | Grant, on the bytes | ★ | Region | Role |
|---|---|---|---|---|---|
| **brightspace-d2l-mcp** `NEW` | [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | **MIT** · `1,200 B` · `a873478a6b4e` | — | North America | 🟢 MCP server over **D2L Brightspace** — the third major North American LMS, and until now the only one this base had no attachment point for. Rescued from the bespoke bucket this pass |
| **xapi-service** `NEW` | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | **MIT** · `1,070 B` · `685c342129c5` | — | Global | 🟢 **xAPI learning-record service, MIT — rescued from this base's ungranted class.** This base called its Caliper/QTI/xAPI cluster "its most dead cluster"; the live, permissive half of it was filed as an absence |
| **xapi-validation** `NEW` | [`LearningLocker/xapi-validation`](https://github.com/LearningLocker/xapi-validation) | **MIT** · `1,070 B` · `13ffff748515` | — | Global | xAPI statement validation — the evidence layer under any audit-trail claim |
| **mcp-regulated-ai-compliance** | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | Apache-2.0 · `12,227 B` · `72e4b0734bcc` | — | Global | MCP compliance layer — Art. 27 FRIA evidence for every regulated-deployment recipe here |
| **collect** `NEW` | [`getodk/collect`](https://github.com/getodk/collect) | **Apache-2.0** · `10,494 B` · `2344bb9c5da4` | — | Global | ODK Collect — offline mobile data collection. The field-survey instrument for a readiness diagnostic where connectivity fails |
| **ai-agents-for-beginners** | [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | MIT · `1,141 B` · `4bcf574c06d3` | — | Global | 18-lesson agent course. Curriculum, not a runtime — the fastest onboarding path for a studio squad |
| **annotated_deep_learning_paper_implementations** `NEW` | [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | **MIT** · `1,082 B` · `db59a04a8a2c` | — | Global | Annotated implementations of DL papers — rescued from the ungranted class; a teaching corpus under a permissive grant |

## Dependency grants — `ACTION p787-D` discharged, and it is this pass's headline

🔴 **A repository-level grant describes one file. It does not describe what the project pulls in.**
Direct dependencies were read from each project's own manifest and each dependency's grant from the
npm or PyPI registry (`ingest/p788-dep-audit`). 🔵 **Transitive dependencies were NOT audited** —
this is the first layer only, and the first layer was already enough to change four rows.

| Repo | Repo grant | Direct deps | Copyleft found | Verdict |
|---|---|---|---|---|
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | `171` | 🔴 **`angular-shepherd` — AGPL-3.0** | 🔴 **The most serious finding of the pass.** This base lists Oppia under *"build on these, link them, **ship them in client code**"*. An **AGPL-3.0** dependency in a browser-delivered bundle is the hardest copyleft there is, and network delivery is its trigger. **Remove or replace `angular-shepherd` before Oppia goes into a client deliverable** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | `32` | 🔴 `zeroconf-py2compat` (LGPL-2), `json-schema-validator` (LGPL) | 🟡 This base's *"most valuable permissive row"* carries **two** LGPL dependencies. 🟢 **LGPL tolerates dynamic linking**, which is how Python imports work, so Kolibri stays usable — but the components must remain replaceable and their source available. **Not the unqualified MIT story the base has been telling** |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | `27` | 🔴 `pyte` — LGPL-3.0 | 🟡 The sector's **#1 agent at `58,508★`** carries a copyleft dependency. `pyte` is a terminal emulator — likely droppable. **Check whether the tutoring path needs it at all** |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 MIT | `181` | 🔴 `mathml2omml` (LGPL-3.0-or-later); 🟡 `jszip` (`MIT OR GPL-3.0-or-later`) | 🟡 `p787` found `mathml2omml` as a bundled workspace package; it is **also a declared dependency**. 🔵 **`jszip` is NEW and is dual-licensed** — a dual grant is permissive only if you **elect** the MIT arm, in writing, on the record |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | `43` | 🟢 **none** | 🟢 **Clean.** One unresolvable private scope (`@common/global-config`) is unpublished, not unlicensed |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 | `18` | 🟢 **none** | 🟢 **Clean — and this is the component that anchors `P788-1`, the flagship grading pattern.** The one row a regulated deliverable most depends on is the one that audits cleanest |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 MIT | `1` | 🟢 **none** | 🟢 Clean |

🟢 **The number to carry into a client conversation: 4 of 7.** Four of the seven highest-star
permissive education repositories carry copyleft in their **declared direct dependencies**, and in
every case the repository's own `LICENSE` file says nothing about it. 🔵 **The two that audit clean
— `nbgrader` and `OATutor` — are the two this base's grading pattern already rests on**, which is
luck rather than design, and is now on the record as a reason to keep resting on them.

## 🔴 CORRECTION TO THIS BASE — `Kosudo/nextSIS` is NOT proprietary (`p790`)

🔴 **This base published, at `p787-B` and again at `p789`: *"PROPRIETARY, newly measured … a
`39,890 B` licence file is not evidence of an open grant — it is evidence of a long one."* That
verdict is FALSE, and the reasoning that produced it is the thing worth keeping.**

🟢 **Measured this pass.** The address is alive at `60e422c7d93e` — **the exact sha this base
recorded**, so nothing moved. Its grant is served at **`license.txt`** (lowercase, `.txt`), which is
why `p789`'s `11`-path probe reported `NO-GRANT-SERVED` and mine did too until the tree was
enumerated. The file is `39,890 B` · `cd7a49230f22`, and it is a **licence anthology** with a table
of contents:

| § | Contents | Whose terms |
|---|---|---|
| 1 | Overview | nextSIS |
| 2 | **nextSIS GNU General Public License Version 3** | 🟢 **nextSIS's own grant — full operative GPL-3.0 text, `Version 3, 29 June 2007`, `5 ×` `TERMS AND CONDITIONS`** |
| 3 | CodeIgniter License | EllisLab, Inc. (bundled framework) |
| 4 | Twitter Bootstrap License | Bootstrap (bundled front end) |

🔴 **The single `All rights reserved.` in the file is at line `703`. It is the second line of §3 —
`Copyright (c) 2008 - 2011, EllisLab, Inc.` — and EllisLab's very next clause reads `You are
permitted to use, copy, modify, and distribute the Software`.** So the line this base graded on
does not belong to nextSIS, **and the licence it does belong to is not proprietary either.** The
verdict was wrong twice over on one line.

🟢 **Corrected verdict: `Kosudo/nextSIS` is `GPL-3.0`** — a named, open-source Student Information
System. 🔴 **Copyleft, so it is flagged, not cleared:** deploy it as a separate system and integrate
at its boundary; **never embed it in a proprietary client deliverable.** 🟢 **But it moves from
`barred` to `usable-with-care`, and it is the only open SIS this base holds** — against `T852`'s
point that the famous names are copyleft, this is one more confirmation, not an exception.

🔵 **Why this is a method change and not an erratum (`T875`):** my own instrument graded the same
file **`AGPL-3.0`**, because GPL-3.0's §13 *names* the GNU Affero GPL, and it fired the NonCommercial
bar, because GPL-3.0 §6 *uses the word* "noncommercial". **Three different probes, three different
wrong answers, one cause: a licence file that quotes other licences cannot be graded by substring
presence.** The grader now matches **anchored title lines** and reports a **set**, and `nextSIS`
reads `ANTHOLOGY[GPL-3.0, +CodeIgniter]`. This is the same defect class as `metabase`'s
split-by-directory finding, **split by section instead.**

## 🔴 Probed this pass and NOT usable

| Address | Finding | Why it is barred |
|---|---|---|
| [`Tzxser/aipha-learning-os`](https://github.com/Tzxser/aipha-learning-os) | ALIVE · `aa476a6a6a03` · `1,296 B` bespoke | 🔴 **PROPRIETARY**, now graded rather than left `UNGRADED`. Source-available multi-agent learning OS |
| [`metabase/metabase`](https://github.com/metabase/metabase) | ALIVE · `6006cc9c65dd` · `855 B` | 🔴 **SPLIT BY DIRECTORY, not one licence.** AGPL-3.0 outside `enterprise/`, **Metabase Commercial License** inside it. 🟢 Reporting one family for this repo would be the error; the boundary is the fact. Same shape as `764-C` |
| [`luscitiosus/Dirigo`](https://github.com/luscitiosus/Dirigo) | ALIVE · `9ed32d5c2577` · `362 B` | 🔴 **CORRECTION — this base's published reason was WRONG.** `p786` recorded *"a file named `LICENSE` containing a Latin boast and no grant of any kind"*. The Latin boast is line 1; **lines 3–5 grant CC BY-NC-SA 4.0, in Spanish, with a link to the Spanish legal code**, and a scope clause excluding the downloaded BOE/BOC statutory texts. Still barred commercially — but **NonCommercial is a harder bar than an absence, and the stated reason was false** (`T863`) |
| [`cosark/OpenTutor`](https://github.com/cosark/OpenTutor) | ALIVE · MIT · fork of `zijinz456/OpenTutor` at `0★` | 🔴 **Not a distinct project** |
| [`gabrielmahia/shule-ai`](https://github.com/gabrielmahia/shule-ai) | ALIVE · `01d074b6aaf3` · **`209 B` · `9dd285c3704d`** | 🔴 **`CC BY-NC-ND 4.0` — NonCommercial AND NoDerivatives.** Kenya's CBC/KCSE tutor answering in Kiswahili. **Barred twice: not in a paid engagement, and not modifiable at all.** 🔵 Indexed `NOASSERTION` by the search channel |
| [`Bestisco/My-WASSCE-Companion`](https://github.com/Bestisco/My-WASSCE-Companion) · [`Elite2828/ACE-AI-Tutor`](https://github.com/Elite2828/ACE-AI-Tutor) | ✏️ **ALIVE but EMPTY — `rc=0`, `0` refs, no `HEAD`** · 🔴 **`p794` CORRECTS the stale text here**, which still read *"DEAD — `rc=2`, re-probed and confirmed"* and contradicted `p793`'s correction in this same file | 🟡 **Returned by the search channel and ALIVE-BUT-EMPTY on the byte channel — authors who claimed a name and never pushed.** `2` of the `5` Ghanaian addresses probed. 🔵 A search result is a claim; `rc` is the fact |
| [`lehrer-tools/lehrer-agent`](https://github.com/lehrer-tools/lehrer-agent) ≡ [`NikolasSchaeffner/lehrer-agent`](https://github.com/NikolasSchaeffner/lehrer-agent) | Both ALIVE · **identical `HEAD` `3ddcfbbabc56`** · neither serves a licence | 🔴 **ONE German teacher agent, carried by this base as TWO ungranted rows.** 🟢 **`ACTION p787-G` discharged mechanically (`T865`):** `p787` said only a page read could separate a fork from a project. **Identical `HEAD` sha proves it on the byte channel**, and the page channel is `403` this pass |
| [`narumi-mase/osaka-lesson-dataset`](https://github.com/narumi-mase/osaka-lesson-dataset) | ALIVE · `212cb10e48eb` · no licence on 10 filenames × 3 branches | 🔴 Japan's best education-AI artefact, **ungranted**. An upstream licence request, not a permanent exclusion |
| [`silja-graf/Didaktikus-…-LP21`](https://github.com/silja-graf/Didaktikus-KI-Spezialist-f-r-Unterrichtsplanung-und-Beurteilung-nach-LP21) | ALIVE · `8d747cda689e` · no licence | 🔴 A **Swiss LP21-curriculum** lesson-planning and assessment agent — the single most engagement-shaped EMEA artefact found, and ungranted. 🔵 **Ask for this one** |
| [`RAFCERAY/horizonia`](https://github.com/RAFCERAY/horizonia) · [`redoneabouaali-lab/najih`](https://github.com/redoneabouaali-lab/najih) · [`MRiARC/VidyaSetu`](https://github.com/MRiARC/VidyaSetu) · [`TaoYu-ds/TutorMesh`](https://github.com/TaoYu-ds/TutorMesh) · [`kaikai52125/NeoTutor`](https://github.com/kaikai52125/NeoTutor) · [`SoukhyadP991/Multilingual-NCERT-Doubt-Solver`](https://github.com/SoukhyadP991/Multilingual-NCERT-Doubt-Solver) · [`mingxuanyan07-lgtm/ai-for-education-showcase`](https://github.com/mingxuanyan07-lgtm/ai-for-education-showcase) | all ALIVE · none serving a licence | 🔴 **7 further ungranted agents, placed by region so the absence is useful:** FR, Morocco, IN, CN, CN (a DeepTutor re-implementation on LangGraph), IN (offline NCERT doubt-solver), CN (auditable multi-agent maths teaching). 🟢 These are **licence requests**, and three of them are the best artefact found for their country |

## Counts — `p792` (see the `p793` block above for this pass's sweep)

| | Count |
|---|---|
| Agents and components listed with a byte-verified grant | **75** (was 62) |
| of which **permissive** (MIT · Apache-2.0 · ECL-2.0 · BSD · BSL-1.0 · **CC0-1.0** · CC BY 4.0 content) | **69** |
| of which copyleft, flagged | **8** (`learnharness` AGPL-3.0, `OpenVidya` AGPL-3.0, `GenPrompt-Pre-ICFES-11` AGPL-3.0, `NCERT-AI-Teacher-Assistant` GPL-3.0, **`nextSIS` GPL-3.0 — corrected from "proprietary" this pass**, `frappe/lms` AGPL-3.0, `news-grade-reader` GPL-3.0, `frametell` AGPL-3.0) |
| 🟢 **NEW to this base this pass** | **13** |
| Placed **LATAM** | **9** (was 5) — 🟢 **🇧🇷 Brazil and 🇨🇴 Colombia placed for the first time** |
| Placed **APAC** | **17** (6 India · 2 Korea · 5 China · 3 Japan · **1 Malaysia**) — 🟢 **Malaysia placed, `p789` gap discharged** |
| Placed **EMEA** | **20** (7 agents + 7 `elimu-ai` + 5 Africa + 1 🇬🇧) |
| Placed **North America** | **4** |
| Placed **Global** | **21** |
| Probed and rejected | **25** (1 split-by-directory, **3** NonCommercial — one of them also NoDerivatives, 1 fork, 1 duplicate address pair, **17** ungranted, 🔴 **`2` ALIVE-BUT-EMPTY — corrected at `p793` from "DEAD" (`T892`)**) · 🟢 **`1` row LEFT this bucket: `nextSIS`** |
| 🔴 Rows whose published verdict this pass CORRECTED | **1** — [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS), **proprietary → GPL-3.0**, on a licence *anthology* graded by one line belonging to a bundled dependency |
| 🔴 Defects found in this pass's OWN instruments, by controls, before publication | **7** — `0` found by inspection |
| 🟢 Controls reproduced exactly before any verdict shipped | **10 of 10** known-good rows · `3` planted negatives DEAD as designed |

### Where the three declared gaps of `p789` stand

| `p789` gap | `p790` disposition |
|---|---|
| 🇲🇾 **Malaysia** (`1`, ungranted) | 🟢 **DISCHARGED** — `haziqhalifi/StudyLah`, MIT, SPM Form 5 mathematics in Bahasa Malaysia |
| 🇬🇭 **Ghana** (`1`, ungranted) | 🔴 **NOT discharged, and RE-MEASURED at `11` repositories with `0` grants** — `p789` understated the supply ~`10×` and read the grant rate correctly. `2` of `5` probed addresses are DEAD |
| 🇹🇿 **Tanzania** (`0`) | 🔴 **NOT discharged.** `2` repositories exist; the only granted one (MIT) is **veterinary extension education**, not school education — a category error in the opposite direction from Japan's (`T877`) |

🟢 **The honest summary of this pass: `1` region placed, `1` region placed for two countries, `2`
regions measured and still empty, and `1` of this base's own published verdicts reversed.** 🔴 **The
reversal is the most valuable item**, because the instrument that produced it — grading a licence
file by substring presence — is still in use everywhere else licence files are read, and three
independent probes got three different wrong answers from the same file.

🔵 **The thinnest regions are now Tanzania (`0` school-education agents, measured), Ghana (`11`
repositories, `0` grants) and Kenya (`3` repositories, `0` usable grants — one barred `NC-ND`).** All
three are measured; none is inferred; and all three have the same remedy, which is a licence request
rather than an engineering task.
