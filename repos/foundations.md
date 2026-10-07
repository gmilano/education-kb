---
industry: education
region: Global
updated: 2026-10-07
---

## 🟢 Thirty-eighth pass, 2026-10-07 — the item-calibration layer, declared missing at pass 25 and unreachable since the reset

**Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-07**, 16 licence filenames × `main` **and** `master`, and classified on the **title block**
(`P171`). **No star counts are claimed** (`P479` — this session is repo-scoped, so popularity metrics
are out of scope by construction). ⏱️ **Fifth pass of this date** (34–37 all ran earlier).

🟢 **This pass closes a gap this KB declared for itself at pass 25 and then lost.** Not a gap found in
the industry — a gap found in **this repository's own open-gap register**, which the `2026-10-06`
reset left behind in `archive/`.

### 🔴 `P483` — the reset dropped the open-gap register, so a declared gap became uncollectable

`archive/2026-10-06-pre-reset/repos-foundations.md:6019` carries **Gap 39**, opened at **pass 25**,
and it is specific to the point of being a work order:

> *"Hay *item banking* y hay entrega certificada; **no hay análisis de ítems** (TRI/IRT, calibración de
> dificultad) empaquetado y permisivo que cierre la cadena. … **Es acotado y construible:** escribir N
> variantes con el *writer*, entregarlas con `qti3-item-player` y **calibrar con una librería IRT de
> Python**."*

🔴 **That sentence appears nowhere in the live tree.** Measured: `calibración de dificultad` and
`análisis de ítems` return **0 hits** outside `archive/`. 🔵 **So twelve passes have run since the reset
over a shelf that had already worked out what was missing, what it was worth, and how to close it —
and none of them could see it.**

> **`P483`.** A reset or re-scope must carry forward the **open-gap register** as live content. A gap
> claim that survives only in an archive is **worse than no gap claim**: the work of identifying it has
> been paid for, and the claim is no longer reachable by the passes that could close it. 🔵 **`P469`
> withdrew a gap that was false. This is the opposite failure — a gap that was true and went
> uncollectable.**

### 🔴 `P484` — and the probe that found it published two wrong numbers on the way

🔴 **This pass's first draft claimed the industry gap outright: *"psychometrics: zero coverage across
1,087 shelved slugs."*** It was produced by an **English-only** grep — `psychometric`,
`item-response` → **0 files**. 🔴 **The corpus is bilingual.** Passes up to the reset wrote in Spanish:

| Spelling probed | Files | Verdict on the draft claim |
|---|---|---|
| `psychometric` · `item response` | **0** | the draft's only evidence |
| 🔴 `psicometr` | **5** | 🔴 **refutes it** |
| 🔴 `testing adaptativo` | **5** | 🔴 **refutes it** |
| 🔴 `IRT` | **19** | 🔴 **refutes it** |
| `2PL` · `3PL` | **0** | 🟢 survives — see below |

🔴 **And the corrective probe was itself wrong by two orders of magnitude.** `grep -ril TRI` reported
**105 files**; `grep -roh '\bTRI\b'` reports **1 occurrence** in the whole tree. The 105 was
case-insensitive substring noise inside ordinary words. 🔵 **The run that corrected a false gap claim
simultaneously published a false coverage count, in the same command, from the same missing word
boundary.**

> **`P484`.** Probe a gap claim in **every language the corpus uses**, with **word boundaries**
> (`\b`), and count **occurrences, not files**. A file count over a case-insensitive substring is not a
> measurement of coverage. 🔵 **And the single real `TRI` hit was the declared gap itself** — so the
> correct probe would have found `P483` directly instead of arriving at it by accident.

### 🟢 What survives, stated precisely — and it is the half that matters

🟢 **The KB holds the *education-data-mining* measurement layer and always did**: `EduCDM`
(IRT/MIRT/DINA), `EduKTM` (knowledge tracing), `EduCAT` (CAT policy), `EduNLP` — the BigData Lab @USTC
shelf, archived at pass 87. 🔴 **What it holds nowhere, in either language, is a library that *fits item
parameters from response data*.** `2PL` and `3PL` were named **zero times** across the whole KB **before this pass** — 58,633 lines, `archive/` included.

🔵 **The distinction is the whole finding, and it is a delivery distinction, not a taxonomic one.** The
USTC layer models the **learner** (what does this student know?). The absent layer calibrates the
**instrument** (is item 7 harder than item 12, and by how much, with what standard error?). 🔴 **Gap 39
needs the second one, and a high-stakes exam is indefensible without it**: without measured
equivalence, scores across item variants are not comparable.

### 🟢 Foundations added this pass — the IRT / CAT estimation tier, 8 permissive rows

🟢 **All eight read from payload. Maintenance is tiered separately, because `P260` applies: "there is a
package" is not "there is maintenance".**

| Repo | Licence (payload) | Hit path · bytes | Second channel (`P482`) | Why it earns a row |
|---|---|---|---|---|
| 🆕 [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | 🟢 **MIT** | `master/LICENSE` · 1,121 B | 🟢 PyPI `MIT`, Homepage → **same slug** | 🟢 **The delivery-grade choice.** Bayesian IRT on **Pyro/PyTorch**, GPU-accelerated, variational inference; **1PL (Rasch), 2PL and 4PL** implemented, vague **or hierarchical** priors. **v0.7.1, 34 releases, last upload 2026-03-24** |
| 🆕 [`joakimwallmark/irtorch`](https://github.com/joakimwallmark/irtorch) | 🟢 **MIT** — 🔴 **body text, no title line** (`P487`) | `main/LICENSE.txt` · 1,073 B | 🟢 `pyproject.toml` `license={text="MIT"}` · PyPI `MIT`, Homepage → **same slug** | 🟢 **The freshest in the tier. v0.5.5, 26 releases, last upload 2026-08-24.** PyTorch-based IRT with GPU support. ⚠️ **Attribution unresolved** — the grant's copyright holder is a packaging-template default (`P487`) |
| 🆕 [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** | `main/LICENSE` · 1,514 B | 🟢 PyPI `license_expression: BSD-3-Clause` (⚠️ Homepage → author domain, not slug) | 🟢 **The adaptive-selection engine.** Reusable CAT engine + simulator: initialisation, item-selection, ability-estimation and stopping rules as swappable strategies. **v0.21.0, 34 releases, last upload 2026-04-08.** 🔴 **Subject of `P485` — cite this slug, not "catsim"** |
| 🆕 [`condecon/adaptivetesting`](https://github.com/condecon/adaptivetesting) | 🟡 **MPL-2.0** | `main/LICENSE` · 16,661 B | 🟡 PyPI `license: None` — **registry under-reports the payload** | 🟢 **Maintained CAT package, v1.2.1, 13 releases, last upload 2026-06-29.** ⚠️ **MPL-2.0 is file-level copyleft** — weaker than GPL, but modified MPL files must stay MPL. In-tree is viable; **changes to its own files are publishable** |
| 🆕 [`eribean/girth`](https://github.com/eribean/girth) | 🟢 **MIT** | `master/LICENSE.txt` · 1,064 B | 🟡 PyPI `MIT`, Homepage → author **Pages** domain (owner-level, not slug) | 🟢 **Marginal-ML / conditional estimation plus synthetic IRT data generation** — the fixture generator the tier otherwise lacks. 🔴 **Stale: v0.8.0, last upload 2021-11-11** |
| 🆕 [`junchenfeng/pyirt`](https://github.com/junchenfeng/pyirt) · [`17zuoye/pyirt`](https://github.com/17zuoye/pyirt) | 🟢 **MIT** — **byte-identical on both slugs** | `master/LICENSE.txt` · 1,083 B **each** | 🟢 PyPI Homepage → `junchenfeng/pyirt`; Download archive → `17zuoye/pyirt` | 🟢 **EM-based 2PL estimation, built for an operating edtech platform** (17zuoye / 一起作业). 🔵 **Subject of `P488` — two slugs, one name, grants agree byte for byte.** 🔴 **Stale: v0.3.4, last upload 2019-07-18** |
| 🆕 [`mhw32/variational-item-response-theory-public`](https://github.com/mhw32/variational-item-response-theory-public) | 🟢 **MIT** | `master/LICENSE` · 1,064 B | ⚠️ none — not packaged | 🔵 **Reference implementation, not a dependency.** PyTorch code for *"Variational Item Response Theory: Fast, Accurate and Expressive"* — the method `py-irt` productised. Shelve as the **method citation** for a defensibility annex |
| 🆕 [`inuyasha2012/pypsy`](https://github.com/inuyasha2012/pypsy) | 🟢 **MIT** | `master/LICENSE` · 1,068 B | 🟡 PyPI `MIT` | 🔵 **Breadth reference: MIRT, GRM, CAT, CDM, FA and SEM in one package.** 🔴 **Effectively abandoned: v0.1.5, last upload 2016-04-04 (10 years).** Read it for **algorithm coverage**, do not ship it |

### 🔴 `P486` — a permissive repo payload does not license a vendored proprietary UI

🆕 [`hicsail/opencat-pro`](https://github.com/hicsail/opencat-pro) (**BYO-CAT**, Boston University SAIL)
probes clean: 🟢 **MIT**, `master/LICENSE`, **1,106 B**. 🔴 **And it is not usable as it stands.** Its own
`README.md` says so twice:

> *line 6:* *"The platform uses **Accessible+** to provide section 508 compliant user interface. Please
> **purchase a license** … if you wish to use BYO-CAT for development."*
> *line 176:* *"The UI framework is based on **Accessible+**. **A valid license is required to use this
> in production.**"*

🔴 **So the MIT grant covers the authors' code and not the interface the product ships.** A
filename-and-payload probe returns `LICENSED · MIT · OK` and is **right about the repository and wrong
about the deliverable**.

🟢 **This instrument already names the class as a known limit and this is its first measured education
instance.** `compose/code/p473-probe-commercial-gate/README.md` → *"Monorepo and open-core carve-outs
are not detected. A repo-level permissive payload can coexist with a proprietary `ee/` subtree."*
🔵 **The carve-out here is not a subtree — it is a purchased third-party asset named only in prose**,
which no path-aware read of the tree would catch either.

🔵 **The rule this yields is `P486`, and it is **defined once**, in `verticals/solutions.md` — the shelf it governs, since it is a statement about **platform** rows.** 🔴 **Cited here, not redefined: a duplicate definition makes every prior citation of the number ambiguous retroactively (`P481`).**

### 🟢 What the tier does to the in-tree / side-car decision

| Need | In-tree, permissive | Licence |
|---|---|---|
| Fit item parameters (1PL/2PL/4PL), maintained | 🟢 `nd-ball/py-irt` **or** `joakimwallmark/irtorch` | MIT |
| Adaptive item selection + simulation | 🟢 `douglasrizzo/catsim` | BSD-3-Clause |
| Synthetic response data for fixtures | 🟢 `eribean/girth` | MIT (stale) |
| CAT with file-level copyleft tolerated | 🟡 `condecon/adaptivetesting` | MPL-2.0 |
| 🔴 A ready-made CAT **web platform** | 🔴 **still none that is cleanly usable** | `opencat-pro` is MIT **+ paid UI** (`P486`) |

🟢 **The chain Gap 39 asked for is now permissive end to end**, and every link was re-read from payload
this pass:

| Link | Repo | Licence (payload) | Bytes |
|---|---|---|---|
| Write N parametric item variants | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | 🟢 **MIT** · `main/LICENSE.md` | 1,072 |
| Deliver them (QTI 3) | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** · `main/LICENSE` | 1,076 |
| Calibrate difficulty / prove equivalence | [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | 🟢 **MIT** · `master/LICENSE` | 1,121 |
| Select adaptively from the calibrated bank | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** · `main/LICENSE` | 1,514 |

🔵 **See `P491` in `compose/patterns.md` for the wiring.** 🟢 **MIT · MIT · MIT · BSD-3 — no copyleft
anywhere in the chain**, which is what makes it a product component rather than a side-car.

### ⚠️ Gaps this pass searched for and did **not** close — stated so silence is not read as coverage

| Gap | Searched | Result |
|---|---|---|
| 🔴 **A permissive CAT *web platform*** | `opencat-pro`, `EduCAT`, CAT platform searches | 🔴 **Open.** The only candidate carries a paid UI (`P486`) |
| 🔴 **Psychometric equivalence *between generated variants*** | the second half of Gap 39 | 🔴 **Still open, and still unmeasured.** This pass supplies the **calibration** library; nobody has published the **equivalence study** for an LLM-generated variant family on this stack |
| ⚠️ **An `R`-tier row (`philchalmers/mirt`)** | — | ⚠️ **Not probed this pass.** 🔵 `MIRT` appears 4× in the corpus but only as an **algorithm name inside `EduCDM`'s description** — the R package itself is unshelved. Stated as unprobed, not as absent |
| 🔴 **LLM item-generation agents with a real slug** | `ExamEow`, `S.E.S.`, `ExamGen` surfaced in prose | 🔴 **Unresolved — no owner slug recoverable for any of the three.** Recorded as leads, not findings |

## 🟢 Thirty-seventh pass, 2026-10-07 — the copyleft tier measured correctly for the first time, and the Java tier gets a second channel

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07** (16 filenames
× `main`/`master`), each verdict **anchored to the payload's title block** rather than to body tokens
(**`P171`**; the new-instrument fixture gap that let it recur is **`P480`**, written up in
`agents/top.md`). **No star counts** — see `P479` for why the stated reason
has been wrong for 36 passes.

### 🔴 Why this file needed a copyleft pass at all

🔵 **These shelves are overwhelmingly copyleft one tier down, and that tier had never been
payload-measured as a group.** `P171`'s third reopening is what forced the question: a bare-word NonCommercial test
reported **GPL-3.0 and AGPL-3.0 payloads as commercially prohibited**, because **§6 of both contains
*"allowed only occasionally and `noncommercially`"***. 🔴 **If the shelf's dominant family can be
silently mis-barred by the instrument, then the family's rows need to carry their own measured
evidence**, not an inherited label.

| Repo | 🟢 Licence (payload → title block) | Bytes · path | Why it is a foundation |
|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 **GPL-3.0** — *"GNU GENERAL PUBLIC LICENSE Version 3"* | **35,146 B** · `main/COPYING.txt` | 🔵 **The reference every other LMS is measured against**, PHP, continuous since 2002, deepest plugin catalogue in the category. 🔴 **GPL-3.0: an AI deliverable is a *plugin* or an out-of-process service, never a fork you keep closed.** ⚠️ **Licence is at `COPYING.txt`, not `LICENSE`** — a probe that omits `COPYING*` reads the world's most deployed LMS as ungranted |
| [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | **10,982 B** · `master/LICENSE` | 🟢 **Re-confirmed independently this pass.** Still the **permissive full-LMS foundation** (pass 35, `P467` withdrawn) — Zurich-stewarded, Java. 🟢 **EMEA.** 🔵 **The only row in this tier where "extend it in-product" needs no licence conversation** |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **ECL-2.0** — *"Educational Community License, Version 2.0"* | **11,340 B** · `develop/LICENSE` | Lecture capture, processing and delivery. 🟢 **Shelf slug confirmed correct**: `apereo/opencast` resolves nothing on any branch or filename; `opencast/opencast` resolves on **`develop` and `master`**. 🔵 **This file already recorded that correction at `:1123` — the probe reproduced it rather than finding it** |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🟢 **GPL-2.0** | **15,214 B** · `master/LICENSE` | SIS / school ERP: students, grades, scheduling, attendance, billing, discipline, food service, **Moodle LMS integration in-tree**. 🔴 **GPL-2.0 — the strictest row in the SIS tier**; side-car only |
| [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | 🟢 **LGPL** | **8,240 B** · `master/LICENSE` | Odoo-based education ERP — admissions, students, faculty, courses, **plus LMS delivery**, which most free SIS platforms omit. 🔵 **LGPL is the softest copyleft in this tier**: linking a separate AI service is clean, modifying the library is not |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | **1,096 B** · `master/LICENSE` | 🟢 **The permissive offline-first row.** Designed for low-connectivity and low-resource deployment — 🔵 **the only foundation here whose architecture already assumes the constraint that defines LATAM, EMEA-Africa and rural APAC engagements**, and it is **MIT**, so it can be extended in-product without a licence conversation |

### 🆕 The Java LMS tier finally has a second channel — `repo.maven.apache.org` is reachable

🔴 **Every prior pass cross-checked licences through PyPI or npm, which left the Java tier — Sakai,
OpenOLAT, Opencast, Kuali — on a single channel.** Measured this pass:

| Channel | Result |
|---|---|
| 🆕 `repo.maven.apache.org/maven2/org/sakaiproject/` | 🟢 **200** |
| 🆕 `repo.maven.apache.org/maven2/org/olat/` | 🟢 **200** |
| `search.maven.org/solrsearch/select` | 🔴 **403** — the Solr API is blocked |

🔵 **So the route exists but it is *browse by groupId path*, not search.** A POM's `<licenses>` block is
a **manifest-layer** declaration (`p289`, `p294`), which makes it a genuine independent channel for the
tier that has had none. ⚠️ **Not yet exercised on a POM payload this pass — recorded as a measured,
open route, not as a completed cross-check.** Next pass should close it on `OpenOLAT` and `Sakai`.

### 🔵 What the licence spread actually means for a delivery decision

| Tier | Permissive option | Reality |
|---|---|---|
| **LMS** | 🟢 **`OpenOLAT`** (Apache-2.0) | the rest — Moodle GPL-3.0, Canvas AGPL-3.0, Open edX AGPL-3.0, Sakai ECL-2.0 — is copyleft or patent-narrowed |
| **SIS** | 🟢 **`rubelw/OSSS`** (Apache-2.0, ⚠️ workflow logic unfinished) | openSIS GPL · RosarioSIS GPL-2.0 · OpenEduCat LGPL |
| **Offline / low-resource** | 🟢 **`Kolibri`** (MIT) | 🔵 **no copyleft competitor at all in this niche on these shelves** |

🔴 **The pattern is consistent and it is the single most useful sentence this file can give an
engagement: in open source education there is usually exactly *one* permissive option per tier, and
every other option is copyleft.** 🔵 **So the licence choice is not a preference, it is a selection of
one — and if that one is immature (`OSSS`) the honest answer is a side-car, not a fork.**

## 🟢 Thirty-sixth pass, 2026-10-07 — the permissive in-tree option reaches the SIS tier

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07** (16 filenames
× `main`/`master`), **re-classified through `compose/code/lib/license_family.sh`** and cross-checked
against the registry each project publishes. No star counts: `api.github.com` **403**, `github.com`
**403**. Cumulative channel census in `agents/top.md` — 🆕 **`registry.npmjs.org` is newly measured
reachable (200)** and is the second-channel route for the JS/PHP tier.

### 🟢 The structural find: the SIS tier now has an Apache-2.0 member

Pass 35 withdrew `P467` and promoted `OpenOLAT` (Apache-2.0, Zurich) as **the permissive full-LMS
foundation this KB had all along**. 🔵 **That left the parallel question open one tier down, and this
shelf never asked it: the LMS tier had an in-tree option, but did the *SIS* tier?** Every student
information system on these shelves is copyleft — **openSIS GPL, RosarioSIS GPL-2.0, OpenEduCat
LGPL-3.0** — so every engagement touching enrolment, attendance, grades or fees has been a side-car by
default.

| Repo | Licence (payload → shared classifier) | Cross-channel | Language | Why it is a foundation |
|---|---|---|---|---|
| 🆕 [`rubelw/OSSS`](https://github.com/rubelw/OSSS) | 🟢 **Apache-2.0** — `main/LICENSE`, **11,363 B** → `Apache-2.0`, commercial use **OK** | 🟢 **Three channels.** `pyproject.toml` → `license = { text = "Apache-2.0" }`; **PyPI `open-schools`** → `License :: OSI Approved :: Apache Software License`, with `repository` resolving back to this repo (identity confirmed, not just licence) | Python (FastAPI) + TypeScript (Next.js) | 🟢 **The first Apache-2.0 student information system on these shelves — the SIS counterpart to what `OpenOLAT` is for the LMS tier.** FastAPI + **Keycloak SSO** + SQLAlchemy + PostgreSQL; modules for governance, student info, accounting, activities and transportation. 🔵 **And the agent tier is inside the tree, not bolted on**: `Ollama + MetaGPT + A2A` are named in the stated architecture, so an AI deliverable extends the SIS **as a module** rather than integrating with it across a boundary. 🟢 **Region: North America**, placed on its **data model** — districts as top-level tenant, district transportation, district accounting, board governance (`P474`) |

⚠️ **The maturity caveat is load-bearing and belongs in any deck that names this repo.** The README opens
with a self-declared warning — *"OSSS is still being developed"* — and records, dated **7 Nov 2026**,
that the **state machine and workflow/gate logic are still being built**. 🔴 **For a system whose whole
job is enrolment and grade workflows, that is the core, not the periphery.** Shelve it as the
**pilot-tier permissive SIS and the architecture to study**, not as a production migration target. 🔵 **A
foundation can be the right *reference* while being the wrong *dependency*, and this shelf should say
which it means.**

### 🟢 Also added — two foundations that are corpora as much as code

| Repo | Licence | Region | Why it is a foundation |
|---|---|---|---|
| 🆕 [`AI-for-Education/lesson-plan-parse-mbsse`](https://github.com/AI-for-Education/lesson-plan-parse-mbsse) | 🟢 **MIT** (`main/LICENSE`, **1,065 B** → `MIT` / **OK**), © Fab Data | 🟢 **EMEA** | 🟢 **A national curriculum as structured data.** Sierra Leone **MBSSE** Maths and Language Arts lesson plans — all grades, Primary + JSS + SSS — parsed from PDF into JSON and LLM-cleaned. **Ships the corpus** (raw, parsed, cleaned `.json.gz`), so it is a *dataset* foundation and not only a parser. 🔵 **Rule-based parsing with LLMs confined to the cleaning step** — the auditable division of labour, and the reason the output is trustworthy enough to build on |
| 🆕 [`eduagarcia/lm-evaluation-harness-pt`](https://github.com/eduagarcia/lm-evaluation-harness-pt) | 🟢 **MIT** (`main/LICENSE.md`, **1,067 B** → `MIT` / **OK**) | 🟢 **LATAM** | 🟢 **The measurement foundation for Portuguese-language delivery.** EleutherAI harness fork adapted to Portuguese; the evaluation suite behind the **Open Portuguese LLM Leaderboard**, backed by **CEIA, Federal University of Goiás (UFG), Brazil**. **Direct-response** evaluation (not log-probs only) so instruction-tuned chat models are measurable at all; automatic chat-template detection; **vLLM** and **LiteLLM** backends so local and API models are compared on one harness; F1-macro and Pearson aligned to each benchmark's own metric. 🔵 **This is the foundation that turns "which model for Brazil?" from a vendor conversation into a measurement** |

### 🔵 What this does to the in-tree / side-car table

| Tier | Permissive, in-tree option | Copyleft members forcing a side-car |
|---|---|---|
| **Full LMS** | 🟢 `OpenOLAT` (Apache-2.0, EMEA) · `Eloom LMS` (MIT, unplaced) | Moodle GPL-3.0+, Open edX AGPL-3.0, Chamilo GPL-3.0, ILIAS GPL |
| **Assessment delivery** | 🟢 `qtiworks` (BSD-3-Clause, EMEA) | — |
| 🆕 **SIS / school ERP** | 🟡 `OSSS` (Apache-2.0, NA) — **pilot-tier only** | openSIS GPL, RosarioSIS GPL-2.0, OpenEduCat LGPL-3.0 |
| **Offline-first** | 🟢 `Kolibri` (MIT) | — |
| **Evaluation** | 🟢 `AITutor-EvalKit` (MIT) · 🆕 `lm-evaluation-harness-pt` (MIT, LATAM) | — |
| **Curriculum corpora** | 🆕 `lesson-plan-parse-mbsse` (MIT, EMEA) | 🔴 **and this is the tier where `CC BY-NC` appears — see `P473`** |

🔴 **One standing caution this shelf must now carry, because it did not before.** The three tiers above
that hold **content** rather than code — curriculum corpora, item banks, courseware — are where
**NonCommercial** licences live. `CRSS-AI/agentic-se-course-early-2026` was probed this pass and is
**`CC-BY-NC-4.0`, commercial use prohibited**; a filename-based probe called it `GRANTED` (`P473`).
🟢 **Every content-tier row on this shelf must carry `P250`'s commercial-use column explicitly**, because
for content, unlike for code, a permissive-looking licence file is genuinely often not a permissive
grant.

### ⚠️ Gaps this pass searched for and did not close — stated so silence is not mistaken for coverage

- 🔴 **Mexico.** Searched explicitly (`open source education AI project Brazil Mexico Latin America
  github 2026`). **No Mexico-origin permissive education asset surfaced.** LATAM representation on these
  shelves remains **Brazil and Chile** (`lm-evaluation-harness-pt` UFG; `Latam-GPT`/CENIA recorded
  earlier). ⚠️ **Scope: this is a statement about what these queries reached, not about Mexico.**
- 🔴 **A permissive, production-maturity SIS.** `OSSS` is Apache-2.0 **and self-declared incomplete on
  exactly the workflow logic a SIS exists for.** The gap is **maturity**, not licence, and it is a
  different gap from the one pass 35 withdrew.
- 🔴 **`AI-for-Education/fabdata-llm-retrieval`** — an end-to-end RAG platform from an organisation whose
  **other seven repositories this KB already shelves**, and it serves **no licence payload**. 🔵 Worth a
  direct enquiry: this is the single highest-value ungranted repo on these shelves, and the fix is an
  email, not a search.

## 🔴 Thirty-fifth pass, 2026-10-07 — the EMEA gap this shelf declared for three passes is withdrawn

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07**, branch-
and case-aware (12–19 filenames × `main` and `master`), **cross-checked against the registry or
build descriptor each project publishes** where one exists. No star counts: `api.github.com` **403**,
`github.com` **403**, and the GitHub MCP route an earlier pass used is outside this session's
repository scope. Cumulative channel census in `agents/top.md`.

### 🔴 `P467` is WITHDRAWN. The EMEA permissive gap was a property of this shelf, not of the industry

> **Superseded text:** *"no EMEA-origin permissive education foundation."* Asserted here for three
> consecutive passes. 🔴 **It is false.** Two EMEA-origin, permissive, education-specific assets were
> already recorded elsewhere in this KB while this shelf denied their existence. Both were re-read
> from payload on 2026-10-07 and are **promoted onto this shelf below**. Root cause and the
> transferable rule: **`P469`** in `agents/top.md`. 🔴 **And the gate that should have caught this
> already existed and passed 27/27 while judging nothing — its filters are Spanish-only and this
> claim was written in English (`P471`).** Instrument: `compose/code/p471-gap-gate-language/`
> (**16/16**). Recipe: **`P45`** in `compose/patterns.md`.

🔵 **What survives from `P467`, unchanged and still valuable:** nine European and public-sector forges
(`code.europa.eu`, `gitlab.opencode.de`, `codeberg.org`, `framagit.org`, `git.fsfe.org`,
`forge.apps.education.fr`, `invent.kde.org`, `salsa.debian.org`, `joinup.ec.europa.eu`) return
**000** from this environment, re-confirmed this pass for `codeberg.org` and `joinup`. **The EUPL
tier really is invisible here.** 🔴 **What does not survive is the inference that was hung on it.**
Unreachable forges mean *this instrument is partially blind to EU public-sector code*; they never
meant *no permissive EMEA education asset exists*. The second claim was refutable by `grep` against
this KB's own shelves, and nobody ran it.

### 🟢 Foundations added this pass — the two that disprove the withdrawn claim

| Repo | Licence (payload) | Cross-channel | Language | Why it is a foundation |
|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** (`master/LICENSE`, **10,982 B**, verbatim Apache-2.0 preamble) | 🟢 `master/pom.xml` `<licenses>` → `Apache 2.0 Open Source L6icense` pointing at `apache.org/licenses/LICENSE-2.0`; 🟢 **second forge** `gitlab.com/olatorg/OpenOLAT` (payload Apache-2.0, 10,982 B) | Java | 🟢 **The permissive full-LMS foundation this KB has had all along and never shelved here.** Teaching, learning, **assessment**, curriculum management, QTI, SCORM, communication; modular course-authoring toolkit; architecture stated for low resource consumption and scalability. 🔴 **Origin: Switzerland** — OLAT began at the **University of Zurich**, now maintained by **frentix GmbH**. 🔵 **Licence consequence, and it is the big one: this is the only complete LMS on these shelves that an engagement can extend *inside the tree* without the copyleft conversation.** Moodle is GPL-3.0-or-later, Open edX AGPL-3.0, Chamilo GPL-3.0, ILIAS GPL, OpenEduCat LGPL-3.0 — all of which force the side-car architecture. **Apache-2.0 removes that constraint.** 🔴 **Branch is `master`** — a `main`-only probe reports it ungranted. |
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause** (`master/LICENSE.txt`, **2,058 B** — *"distributed under the 3-clause BSD license… This license is famously liberal"*) | — not published to a registry | Java | 🟢 **A permissive, standards-based assessment-delivery foundation, EMEA-origin.** Three components: the **QTIWorks Engine** (QTI 2.1 delivery + rendering), **JQTI+** (Java library to read, write, model and manipulate QTI 2.1 items and tests), and the **MathAssess extensions** for advanced mathematical assessment. From the **University of Edinburgh**. 🔵 **This is the piece that makes assessment migration tractable**: QTI 2.1 in, QTI 2.1 out, with a permissive library for programmatic item manipulation — so item banks can be transformed without a vendor. 🔴 **`master`-only.** ⚠️ The licence text itself *urges* contributing back; **that is an exhortation in the preamble, not a condition** — the operative grant is plain BSD-3-Clause. |

### 🟢 Third permissive platform row — and the platform channel was not saturated after all

| Repo | Licence (payload) | Cross-channel | Why it is here |
|---|---|---|---|
| [`eloompty/Eloom-LMS-International`](https://github.com/eloompty/Eloom-LMS-International) | 🟢 **MIT** (`main/LICENSE`, **1,062 B**) | 🟢 `README` MIT badge agrees; 🔴 **not on Packagist** — so this row is **payload + badge**, not payload + registry, and says so | 🆕 Laravel **13**, PHP **8.3+**, **42 `nwidart/laravel-modules` modules all enabled by default**, **five web portals over a single codebase**, token-authenticated REST API for mobile clients, Laravel Reverb + standalone Socket.IO for realtime. Covers the vocational/HE lifecycle end to end: agent-sourced application → offer letter → enrolment → intake scheduling → attendance → **assessment** → fees → certificates → alumni. 🟢 **MIT, which makes it the most permissive full LMS on these shelves.** ⚠️ **Region not determinable** — the `README` names no country, governing body or qualifications authority. **Recorded as unplaced rather than guessed**, per this KB's closed-vocabulary rule. |

🔴 **Prior passes recorded the platform channel as "saturated, verified by grep"** (`repos/trending.md:1597`,
`:3751`). 🔵 **Two permissive platform rows arrived this pass through that same channel.** The grep
was over *this KB's contents*, which proves the shelf had those names — it was never evidence that
the world had no others. **`P469` is the same error in a second place.**

### 🔴 `P470` — Forma LMS: a confidently published Apache-2.0 claim that no channel here confirms

Secondary sources this pass name **Forma LMS** (Italian fork of Docebo, pre-commercialisation) as
**Apache-2.0**, and recommend it *specifically* for teams needing permissive licensing.
[`formalms/formalms`](https://github.com/formalms/formalms) **exists** (`master/README.md` → 200) and:

| Channel | Result |
|---|---|
| Payload — 19 licence filenames × `main` + `master` (incl. `LICENSE.TXT`, `gpl.txt`, `COPYING.txt`) | 🔴 **nothing** |
| `packagist.org/packages/formalms/formalms.json` | 🔴 **404** |
| `master/composer.json` | 🔴 **absent / unparseable** |

⚠️ **Recorded as `licence unverified`. It is NOT shelved as a permissive foundation.** 🔵 **This is a
sharper failure than a missing licence**: the claim is *specific*, *permissive* and *published as the
reason to adopt*. A dependency manifest that trusted the article would have carried an unverifiable
permissive assertion about a **platform tier** — the tier where a licence error is most expensive,
because it decides in-tree versus side-car. 🔵 **The rule: a licence is a document you read, not a
recommendation you inherit.**

### 🟢 Registry re-reads this pass — 2 rows, 0 disagreements

`canvasapi` → **MIT** free-text **+ OSI MIT classifier** · `kolibri` → **MIT** + **OSI MIT
classifier**. Both agree with the payload rows already on this shelf.

### 🆕 Instrument: the Rust registry is closed

| Stack | Endpoint | Pass-35 reachability | Consequence |
|---|---|---|---|
| Rust | `crates.io/api/v1/crates/{crate}` | 🔴 **403** — 🆕 **first measured this pass** | [`raif-s-naffah/xapi-rs`](https://github.com/raif-s-naffah/xapi-rs) and every future Rust row stay **payload-only**. 🔵 Recorded so no later pass counts Rust among the available second channels — the registry tier is **Python, Node, PHP and JVM, not five stacks** |
| JVM | `repo1.maven.org/maven2` | 🟢 **200** | 🔵 **No longer idle in effect**: OpenOLAT's licence was cross-checked against its `pom.xml` `<licenses>` block via `raw` — the same declaration Maven Central serves. The JVM tier now has a worked precedent |

## 🟢 Thirty-fourth pass, 2026-10-07 — the Canvas client was missing, and the EMEA gap gets its reach restated

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07**, branch-
and case-aware (13 filenames × `main` and `master`), **cross-checked against the registry each
project publishes to** where one exists. No star counts: `api.github.com` **403**, and the GitHub MCP
route an earlier pass used is **outside this session's repository scope** (see `agents/top.md`).
Consolidated 20-channel census in `agents/top.md`; `P465` records why it needed consolidating.

### 🟢 Foundations added this pass

| Repo | Licence (payload) | Cross-channel | Language | Why it is a foundation |
|---|---|---|---|---|
| [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **MIT** (`master/LICENSE`, 1,130 B) | 🟢 PyPI `canvasapi` → `MIT License` + **OSI MIT classifier** | Python | 🔴 **A real gap, and an awkward one: this KB carries six Canvas MCP servers and never carried the Canvas REST client they all sit on.** A maintained, MIT, object-oriented Python wrapper over the Canvas LMS API — courses, enrolments, assignments, submissions, **gradebook writes**, quizzes, LTI. From **UCF Open** (University of Central Florida), the same group as `UDOIT`, `Materia`, `Obojobo` and this shelf's `cookiecutter-python-lti`, all already here. 🔵 **Canvas itself is AGPL-3.0 and this client is MIT** — the client talks HTTP from outside the tree, so the deliverable inherits nothing. **Sixth independent instance of this KB's platform-copyleft / integration-permissive rule.** 🔴 **Branch is `master`** — a `main`-only probe reports it ungranted. |
| [`soumics/llm-rag-assistant`](https://github.com/soumics/llm-rag-assistant) | 🟢 **MIT** (`main/LICENSE`, 1,070 B) | — not published to any registry | Python | The retrieval / embedding / **citation-checking** core reused by the MIT `soumics/adaptive-ai-tutor` (`agents/top.md`). Local-first: embeddings and generation served by **Ollama**, `faiss-cpu` index, and **citation verification as a first-class component rather than a prompt instruction**. 🔵 **Citation checking is the piece most tutor prototypes skip and the first thing an education client asks about.** ⚠️ **`P466`** — distributed only as a pinned GitHub archive zip, **403** from this environment. |
| `edx-opaque-keys` (PyPI) | 🟡 **`AGPL-3.0-only`** (registry declaration) | — | Python | 🆕 **Not previously recorded in this KB.** A core Open edX key/identifier library, and **network copyleft**. Recorded because it extends the Open edX licence asymmetry by one brick: the platform tier is AGPL **including its small utility libraries**, so "it's just a helper package" is not a route out of the copyleft. |

### 🟡 `P467` — the EMEA gap: still a gap, with its reach now stated in full

This shelf has declared for three consecutive passes that it can find **no EMEA-origin permissive
education foundation**. This KB already records that the European Commission's **Joinup/OSOR**
catalogue and **Codeberg** are unreachable from this environment. This pass re-measured that and
**extended it with three forges never named here before**:

| European / public-sector forge | HEAD | GET | Previously recorded here? |
|---|---|---|---|
| `code.europa.eu` — the European Commission's own GitLab | **000** | **000** | yes |
| `gitlab.opencode.de` — German federal/state public-sector forge | **000** | **000** | yes |
| `codeberg.org` — EU-hosted, the main non-US community forge | **000** | **000** | yes |
| `framagit.org`, `git.fsfe.org` | **000** | **000** | yes |
| 🆕 `forge.apps.education.fr` — **French Ministry of Education** | **000** | **000** | 🆕 **no — first measured this pass** |
| 🆕 `invent.kde.org`, `salsa.debian.org` | **000** | **000** | 🆕 **no — first measured this pass** |

🔴 **Nine European and public-sector forges unreachable, against `raw.githubusercontent.com` 200 and
`gitlab.com` 200.** The EUPL tier this KB made machine-readable in pass 28 is, by construction, the
tier most likely to live where this instrument cannot look: **EUPL is the European Commission's own
licence, and the Commission publishes to `code.europa.eu`.**

⚠️ **This does not convert the gap into coverage. It is still a gap and it is now three passes old.**
What it fixes is the *wording*. The defensible sentence is: **"no EMEA-origin permissive education
foundation was found through the forges this environment can reach, and nine forges where EU
public-sector code is most likely to live returned 000."** 🔵 **Consequence: never quote this KB's
thin EMEA shelf to a client as market evidence.** It is partly an artefact of the collection
instrument. Ask the client's own procurement which national forge they publish to.

🟢 **One EMEA-origin asset did arrive this pass through a reachable channel** —
[`macsnoeren/genai-open-assessment`](https://github.com/macsnoeren/genai-open-assessment), **GPL-3.0**,
Netherlands (full row in `agents/top.md`). Copyleft, so it does not fill the *permissive* EMEA gap;
it is the first EMEA-origin higher-education assessment framework on any shelf here.

### 🟢 The registry tier by language — re-consolidated after `P465`

Earlier passes used these registries and proved they discriminate; the pass-33 census dropped them.
Restated here as one table so the next pass inherits the instrument rather than re-deriving it:

| Stack | Registry endpoint | Reachability | Read this pass | Education relevance |
|---|---|---|---|---|
| Python | `pypi.org/pypi/{pkg}/json` | 🟢 **200** | `kolibri` MIT · `xblock` Apache-2.0 · `openedx-learning` AGPL-3.0 · `edx-proctoring` AGPL-3.0 · 🆕 `edx-opaque-keys` **AGPL-3.0-only** · `nbgrader` BSD · `otter-grader` BSD-3-Clause · 🆕 `canvasapi` MIT · `pylti1p3` MIT · `frappe` MIT | Open edX, Jupyter-grading, Kolibri tiers |
| Node / TS | `registry.npmjs.org/{pkg}` | 🟢 **200** | `ltijs` **Apache-2.0, v7.0.7** · `@promptster/rubric` MIT | LTI tool-provider tier |
| PHP | `packagist.org/packages/{v}.json` | 🟢 **200** | `moodle/moodle` → **`GPL-3.0-or-later`** | **The Moodle tier — the largest installed base in this industry** |
| JVM | `repo1.maven.org/maven2` | 🟢 **200** | 🔴 **nothing — still unused** | Sakai, OpenOLAT, Opencast, all payload-verified only |

⚠️ **`P468` — the registry tier has a measured miss rate and never overrules payload.** `crewai`
publishes with **no licence metadata whatsoever**; `chamilo/chamilo-lms` is **404 on Packagist**
despite being a major PHP LMS on this shelf; **8 of 20** PyPI rows gave only free text with no OSI
classifier. 🔵 **Where both channels answer and agree, the row is as well-evidenced as this KB can
make it. Where only one answers, the row must say which one** — rather than reading as doubly
verified.

### 🟢 Substrate re-verification — twelve rows, second source, no movement

No new rows. Recorded because pass 32's T1 is that a licence claim decays, and this is the cheapest
way to re-check one:

| Package | Registry declaration | Note |
|---|---|---|
| `faster-whisper` | **MIT** + OSI classifier | the practical ASR choice for a local tutor |
| `openai-whisper` | **MIT** | reference implementation |
| `coqui-tts` | **MPL-2.0** + OSI classifier | 🟡 **weak copyleft, file-level.** Linking is fine; a quietly patched fork is not. |
| `sentence-transformers` | **Apache-2.0** | embeddings |
| `qdrant-client`, `chromadb` | **Apache-2.0** | vector stores |
| `vllm` | **Apache-2.0** | self-hosted inference — the sovereignty tier |
| `litellm` | **MIT** | provider abstraction |
| `docling` | **MIT** | 🔵 document → structured text; the curriculum-ingestion front door (`P2`) |
| `marker-pdf` | **Apache-2.0** | PDF → Markdown |
| `unstructured` | **Apache-2.0** | mixed-format ingestion |
| `librosa` | **ISC** | audio features — oral-fluency work |
| `mediapipe`, `opencv-python` | **Apache-2.0** both | on-device vision — the local proctoring tier |

🔵 **All twelve permissive or weak-copyleft, none a surprise.** A re-check is supposed to be boring;
when it is not, you have found something.

## 🟢 Thirty-third pass, 2026-10-07 — the regional-corpus layer, and a gap repo that was licensed all along

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07**, with a
branch- and case-aware prober (13 filenames × `main` and `master`). No star counts:
`api.github.com` **403**, github.com landing pages **403** on both HEAD and GET. 🆕 Two further
channels measured and **closed this pass**: `eur-lex.europa.eu` **000**, `huggingface.co` **000**.

### Foundations added this pass

| Repo | Licence (payload) | Region | Role |
|---|---|---|---|
| [`latam-gpt/anonymization-filter`](https://github.com/latam-gpt/anonymization-filter) | 🟢 **MIT** (1072 B, © 2025 GonzaloFuentes1) | LATAM | PII anonymisation filter from the **Latam-GPT** corpus pipeline. 🟢 **The regional primitive this shelf was missing:** a Spanish/Portuguese-language scrubber that sits *in front of* any model, which is what makes a student-data pipeline defensible under LATAM data-protection regimes and under CA A.B. 1159-style rules in North America |
| [`latam-gpt/lm-evaluation-harness`](https://github.com/latam-gpt/lm-evaluation-harness) | 🟢 **MIT** (1067 B, © 2020 **EleutherAI**) | LATAM | Regional evaluation entry point. ⚠️ **A fork** — the grant is EleutherAI's, so treat it as a regionally-configured upstream and cite accordingly |
| [`latam-gpt/syco-bench`](https://github.com/latam-gpt/syco-bench) | 🟢 **MIT-0** — *MIT No Attribution* (903 B, © 2025 Tim Duffy) | LATAM | Sycophancy benchmark. ⚠️ **MIT-0 is a distinct licence from MIT**: it waives attribution. Harmless here, but it must not be recorded as "MIT" in a licence inventory |
| [`biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent`](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent) | 🟢 **MIT** (1068 B, `master/LICENSE`, © 2026 Prem Biswal) | Global | 🔴 **Previously filed on this shelf's reject list.** Belongs in foundations as much as in agents: it is a **from-scratch, dependency-light reference implementation** of explainable behavioural risk scoring — logistic regression, anomaly detection, risk decay and fusion written out rather than imported. Read it as the maths layer under any assessment-integrity build |

🔵 **Why the anonymisation filter is the important one.** The other two LATAM rows are evaluation
tooling with upstream holders. This one is **original regional work** on the problem every education
engagement in the region hits first: student data cannot leave the institution un-scrubbed, and
English-trained PII detectors under-perform on Spanish and Portuguese names, document identifiers and
address forms. 🟢 **It composes directly with the local-first grading stack** already on this shelf —
scrub, then score on the client's own hardware, and no student text reaches a frontier API.

### ⚠️ What this pass could NOT establish, and will not imply

🔴 **The model layer of this industry is unverifiable from this environment.** `huggingface.co`
returns **000** (egress-blocked), so **no weights licence anywhere in this KB is payload-verified** —
including **Latam-GPT's** 70B SFT checkpoint, widely reported under the **Llama 3.1 Community
Licence**. That licence is **not OSI-approved** and carries acceptable-use and naming conditions.
**Treat every weights-licence statement in this KB as a secondary-source claim** (`P464`).

🔵 **The practical consequence for foundations work:** prefer compositions where the permissively
licensed *code* is yours to vendor and the *weights* are a swappable, client-chosen dependency. Every
pattern on the `compose/` shelf that names an open-weights model is one Hugging Face terms change
away from needing a re-read, and this pass cannot do that re-read.

### 🟢 The Open edX licence picture, extended to proctoring

The pass-32 split (AGPL-3.0 core, Apache-2.0 `XBlock`) now has a third measured layer:

| Layer | Repo | Licence (payload) | Bytes | Consequence |
|---|---|---|---|---|
| Core platform | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟡 **AGPL-3.0** | 35136 | self-host freely; redistribution of a modified platform is a licence event |
| Extension point | [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | 11357 (`master/LICENSE.TXT`) | the surface an agent plugs into, and may keep proprietary |
| Proctoring subsystem | [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | 🟡 **AGPL-3.0** | 35119 (`master/LICENSE.txt`) | 🆕 **the integrity layer is copyleft too** — so an integrity *agent* must sit outside it |

🟢 **Which is exactly what the two MIT proctoring agents added this pass do.** The permissive
proctoring work lives *outside* both AGPL-3.0 trees and communicates over APIs — the fifth
independent instance of the rule that **the licence boundary is the integration boundary**.

## 🟢 Thirty-second pass, 2026-10-07 — the Open edX licence asymmetry, stated precisely

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07.** No star
counts: `api.github.com` **403**, github.com landing pages **403 on both HEAD and GET** — three
channels measured, three closed.

### 🔵 The one thing to know before quoting an Open edX engagement

This shelf has carried Open edX components for many passes without stating the licence split in one
place. Both halves were read from payload this pass:

| Layer | Repo | Licence (payload) | Bytes | What it means commercially |
|---|---|---|---|---|
| Core platform | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟡 **AGPL-3.0** | 35136 | Network copyleft. Fine to **self-host for a client**; a licence event if you redistribute a modified platform or expose it as a modified service you own |
| Extension point | [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | 11357 (`master/LICENSE.TXT`) | Permissive. The surface an agent plugs into, and the surface you can keep proprietary |

🟢 **The architecture follows from the table, not from taste.** Build the agent **as an XBlock, or as
an external service talking to Open edX over its APIs**, and the AGPL stays confined to a platform
the client self-hosts. Fork `edx-platform` to embed the agent and you have taken on AGPL-3.0 for the
whole deliverable. [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Colombia, added
to `agents/top.md` this pass) is a working instance of the permissive shape: an MIT tutor agent
living inside an Open edX deployment without touching the platform's licence.

⚠️ **This is the same in-tree vs side-car boundary** this KB recorded for `peancor/moodle-mcp-server`
(MIT, *because* it sits outside the GPL-3.0 Moodle tree) and for `Jawadh-Salih/moodle-mcp-server`
(MIT, added this pass). 🔵 **Three independent instances now: the licence boundary *is* the
integration boundary.** When the platform is copyleft and the agent must not be, the agent goes
outside the tree and talks over an API. That is not a workaround — it is the design.

### Foundations added this pass

| Repo | Licence (payload) | Region | Role |
|---|---|---|---|
| [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | 🟢 **Apache-2.0** (11350 B) | Global | Intel's education reference stack: libraries, microservices and **benchmarking** tools over **OpenVINO**, targeting Intel CPU / iGPU / NPU. 🔵 **The only foundation on this shelf that answers "what hardware does this need?"** — the question that decides whether an on-prem school deployment is affordable |
| [`prometheus-eval/prometheus-eval`](https://github.com/prometheus-eval/prometheus-eval) | 🟢 **Apache-2.0** (10141 B) | Global | Rubric-conditioned evaluator with **open weights**. The piece that lets assessment scoring run on infrastructure the client controls, instead of posting student work to a frontier API |
| [`paper-instruments/rubric`](https://github.com/paper-instruments/rubric) | 🟢 **MIT** (1076 B, © 2025 The LLM Data Company) | Global | Weighted rubrics as a **data structure**, provider-agnostic. Makes a grading decision reproducible and auditable after the fact — which is what a conformity assessment asks for |

🔵 **Why these three belong on the *foundations* shelf rather than with the agents.** None of them is
an education product. Each is a layer underneath one, and together they close the gap this shelf has
had all along: **an education deliverable that must not send student data to a third party now has a
complete permissive stack** — `education-ai-suite` for the accelerated local inference and the
hardware sizing, `prometheus-eval` for open-weight scoring, `rubric` for the auditable criteria.
That stack is the direct technical answer to EU AI Act Annex III and to the US state student-data
statutes catalogued in `intel/market.md` this pass.

### 🔴 Correction to this shelf's verification instrument — `P453`, `P454`, `P458`

**`openedx/XBlock` was returned `ABSENT` by this KB's own prober**, and it is a real repository,
correctly licensed Apache-2.0, already on this shelf. Three independent defects produced that one
false negative:

- **`P453`** — `raw.githubusercontent.com` paths are **case-sensitive**. Proven by negative control:
  `pykt-team/pykt-toolkit/main/LICENSE` **200**, `…/license` **404**, `…/LiCeNsE` **404**. XBlock's
  licence file is **`LICENSE.TXT`** — caps extension — which was not in the probe list.
- **`P454`** — the existence fallback probed only `README.md`. XBlock ships **`README.rst`**
  (200; `README.md` 404), so the fallback also reported it missing.
- **`P458`** — XBlock's **own README links a licence path that 404s**
  (`…/blob/master/LICENSE.txt`, lowercase extension). A verifier that follows the README's link
  concludes "licence missing" on a correctly licensed repo. `pyproject.toml` is the tiebreaker:
  `license = "Apache-2.0"`, `license-files = ["LICENSE.TXT"]`.

⚠️ **The direction of this error is the expensive one.** Every defect here turns a **true row into a
deletion**. This KB has spent many passes guarding against *over*-claiming a licence; `P453`/`P454`
are the first recorded defects that destroy correct rows instead, and they would do it silently,
reported as a 404. 🔵 **Any `ABSENT` verdict recorded in this KB before this pass should be
re-probed with the corrected name list before it is acted on** — in particular for `.rst`-documented
and Python-packaging repos, where both defects land together.

### 🟢 Re-reads this pass — two foundations re-confirmed from payload

| Repo | Payload | Verdict |
|---|---|---|
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `master/LICENSE`, 11120 B | 🟢 **ECL-2.0**. Payload opens *"Educational Community License, Version 2.0 … consists of the Apache 2.0 license, modified…"* — corroborates pass 30's lineage reading **from the payload text itself**, and the row stays on the permissive allowlist |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `master/LICENSE`, 8241 B | 🟢 **LGPL-3.0**, genuinely LGPL. Payload: *"published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 … Since the LGPL is a set of additional permissions on top of the GPL…"*. **Independently corroborates pass 28's negative half** — the linking conversation for this component is real, and the linking exception is really there |

🔵 **The `openeducat` re-read is worth more than a tick.** Pass 28 corrected seven rows `LGPL → GPL-2.0`
and kept four as genuinely LGPL; that correction inverted a commercial answer, so the negative half
needed independent confirmation rather than trust. One of the four is now confirmed by a separate
run, with the payload's own words. The remaining three are **not** re-measured here.

### 🔴 Declared gap — EMEA foundations, second consecutive pass

Searched for EUPL / Apache / BSD education foundations of EMEA origin (Germany, France, Nordics,
EU public sector). **Nothing new found.** Institutional activity exists — Central European
University announced a GitHub collaboration in April 2026 on open AI teaching materials — but it
produced **no repository with a verified permissive grant** in this window. The EUPL public-sector
tier that pass 28 made machine-readable gained **zero rows** this pass. ⚠️ **This is an informed
gap, not coverage**, and it is now two passes old: EMEA is the region where this KB's shelf is
thinnest while being the region with the hardest compliance requirements (`intel/market.md`).

# Foundational Repos — Education

Infrastructure Globant can build an education solution *on top of*. These are not
education products; they are the permissively licensed layers underneath one.
Licenses read from each repo's own `LICENSE` payload on 2026-10-06.

## 🟢 Thirtieth pass, 2026-10-07 — the flagged rows on this shelf were not wrong, and the three that still need a second look

🔴 **Execution of this tree's suites was DENIED this pass** (`[Code from External]`), so no total in
this file is affirmed as measured today (`P107`), and pass 28's four pre-registered sweeps — including
the downstream propagation of the corrected `family_of` to `holder.tsv`, `homepage.tsv`, the `p250`
commercial sweep and the `p419` copyleft census — **did not run**. They carry forward. 🔴 **Reporting
them as "nothing moved" would be a fabricated negative.**

🟢 **What did get settled.** Pass 28's reconciler flagged **29 rows** across this KB as the corpus
contradicting itself on licence; **13 were adjudicated first-hand this pass and none is a
contradiction.** Three of the flagged rows are foundations on this shelf, and all three are fine:

| Row | Flagged because | Verdict |
|---|---|---|
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | prose names **MIT** and **LGPL** | 🟢 **MIT.** The LGPL is two *dependencies*, and the prose already scoped it (`REVIEW-WEAK`, *"two LGPL deps"*) |
| [`opencast/opencast`](https://github.com/opencast/opencast) | prose names **ECL-2.0** and **Apache-2.0** | 🟢 **Both true.** ECL-2.0 *is* an Apache-2.0 derivative — the sentence is a lineage statement, and the row stays on the permissive allowlist |
| [`dequelabs/axe-core`](https://github.com/dequelabs/axe-core) | prose names **GPL** and **MPL-2.0** | 🟢 **MPL-2.0.** The "GPL" is the **`Was` column of pass 28's own correction table** on this shelf |

⚠️ **The useful warning for this file specifically: a correction table manufactures a false
contradiction.** This shelf publishes `Was → Is` rows every time a classifier is fixed, and an
instrument that reads cells without reading which column they are in will count every `Was` as a live
claim. Four of the 29 abstentions were created *by* pass 28 in the act of fixing five rows correctly.

⚠️ **Still genuinely open on this shelf, unchanged from pass 28 and not re-measured here:** the seven
`LGPL → GPL-2.0` rows below are components an engagement **links against**, and the GPL-2.0 has no
linking exception. That is the one correction in this area that changes a commercial answer, and it
stands.

## 🔴 Licence corrections — twenty-eighth pass, 2026-10-07

**Seven repositories on this shelf are `GPL-2.0` and were filed `LGPL`** (`P452`), and the
difference is the whole reason the LGPL exists: it grants a linking exception that the plain GPL
does not. All seven are components an engagement **links against** rather than forks, which is
exactly the case the exception covers.

| Repo | Was | 🔴 Is | Region | Role |
|---|---|---|---|---|
| [`OpenEMIS/core`](https://github.com/OpenEMIS/core) · [`openemis/core`](https://github.com/openemis/core) | LGPL | **GPL-2.0** | Global | ministry-scale education MIS — 🔴 **two rows, one repository**, a live case collision |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | LGPL | **GPL-2.0** | LATAM | Brazilian municipal school system |
| [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) | LGPL | **GPL-2.0** | EMEA | QTI assessment SDK |
| [`oat-sa/lib-lti1p3-core`](https://github.com/oat-sa/lib-lti1p3-core) | LGPL-2.1 | **GPL-2.0** | EMEA | certified LTI 1.3 core — see the regression note below |
| [`inepdadosabertos/api`](https://github.com/inepdadosabertos/api) · [`yunger7/enem-api`](https://github.com/yunger7/enem-api) | LGPL | **GPL-2.0** | LATAM | Brazilian national exam data |

🟢 **The negative half: four rows are genuinely LGPL and did not move** —
[`Tampere/trevaka`](https://github.com/Tampere/trevaka) (2.1),
[`untisapi/untis4j`](https://github.com/untisapi/untis4j) (3.0),
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (3.0),
[`espoon-voltti/evaka`](https://github.com/espoon-voltti/evaka) (REUSE notice). For those, the
dynamic-linking conversation is real.

**The cause.** `family_of` probed LGPL before GPL over `text[:4000]`. The GNU licences name each
other inside their own texts, so the window decided the verdict: GPL-2.0's Preamble recommends the
LGPL at character **784** (inside the window), GPL-3.0's closing notes do so at **34,143**
(outside). Every GPL-2.0 payload came back LGPL; every GPL-3.0 payload came back right. Fixed by
resolving the GNU family from the payload's title region first.

🔵 **A free cross-check this corpus already had the data for: the byte size refutes the label.**
GPL-3.0 is ~35 kB, GPL-2.0 ~18 kB, LGPL-2.1 ~26.5 kB, LGPL-3.0 ~7.6 kB. This file published
`Citolab/qti-components` as *LGPL-3.0 (35,199 B payload)* and `oat-sa/lib-lti1p3-core` as
*LGPL-2.1 (18,091 B)* — both sizes contradict both labels, and no fetch was needed to see it.

### 🔴 The regression, which is the finding worth carrying

`oat-sa/lib-lti1p3-core` was not mis-stated by accident. The pre-reset archive carries **GPL-2.0**
for it in **nine** places, with payload size and fingerprint (`18.091 B`, `f9c375a1be4a`), once as a
deliberate, argued finding:

> *"🔴 **La excepción que rompe la simetría y hay que mirarla:** `oat-sa/lib-lti1p3-core` **es**
> librería de protocolo y aun así es **GPL-2.0**. La regla «librería ⇒ permisivo» no es ley: es
> correlación de 3 de 4. Se dice en vez de redondearla."*

After the 2026-10-06 reset it was rewritten as LGPL-2.1 — the answer the defective classifier gives
— and `intel/market.md` published EMEA architecture advice on it concluding *"neither is a
blocker."* Both the row and that paragraph are corrected this pass. **A correct human reading was
destroyed by an instrument, and the instrument was wrong.**

### 🟡 The EUPL tier, now machine-readable, and it is nine repositories

Nine rows moved `UNKNOWN → EUPL`: eight `Opetushallitus/*` Finnish national education services
(🆕 including [`valtionavustus`](https://github.com/Opetushallitus/valtionavustus), the ninth, which
pass 26's prose did not name) plus
[`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model).
🔵 The eight Finnish grants are **short reference notices (296–654 B), not the full licence text**.
⚠️ **EUPL Article 1's "Communication" covers network use**, so the EUPL binds a hosted service the
way AGPL does — the fact that matters for a managed service delivered to a European ministry.

## Core stack

15 rows, all verified on 2026-10-06. Four further infrastructure rows were added in
the third pass of the same day — see the section below.

| Repo | License (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [ollama/ollama](https://github.com/ollama/ollama) | MIT (`LICENSE`) | model serving | Runs open-weight models on-prem or on a classroom server. This is the answer to EMEA data-residency and to LATAM connectivity/cost constraints — student data never leaves the institution. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | MIT (`LICENSE`) | agent framework | Typed, validated agent outputs. When an assessment decision must be defensible, a schema-checked output beats free text. |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT (`LICENSE`) | orchestration | Graph-structured, checkpointed agent state. The checkpoints double as the audit trail a high-risk education deployment needs. |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | MIT (`LICENSE`, body text — no title line) | orchestration | Role-based multi-agent teams; maps cleanly onto tutor / assessor / reviewer separations. |
| [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) — ⚠️ **now `OpenHands/OpenHands`**; both paths serve head `9f05599`, see the canonical-name table below | MIT (`LICENSE`) | coding agents | For the build itself and for CS-education use cases where students need a sandboxed coding agent. |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | MIT (`LICENSE`) | agent framework | Python + .NET. The right default for clients already on a Microsoft stack, and the successor path off AutoGen. |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 (`LICENSE`) | agent framework | Smallest auditable surface of the frameworks here. |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Apache-2.0 (`LICENSE.md`) | document ingestion | Turns textbooks, PDFs and scanned curricula into structured text. This is the front door of every content-generation pipeline in `compose/patterns.md`. |
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | BSD-3-Clause (`LICENSE`, modified-BSD body) | lab environment | Multi-user notebook serving for a cohort. The standard way to hand 200 students an identical environment. |
| [jupyter/notebook](https://github.com/jupyter/notebook) | BSD-3-Clause (`LICENSE`) | lab environment | The notebook itself. |
| [learningequality/ricecooker](https://github.com/learningequality/ricecooker) | MIT (`LICENSE`) | content pipeline | Python framework for packaging arbitrary content into Kolibri channels. The ETL half of the offline-first pattern. |
| [learningequality/studio](https://github.com/learningequality/studio) | MIT (`LICENSE`) | content authoring | Curriculum authoring and channel curation that feeds Kolibri. |
| [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | Apache-2.0 (`LICENSE`) | LMS integration | LTI tool-provider implementation. The permissive doorway into a copyleft LMS — see the license-boundary note in `agents/top.md`. |
| [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) — 🟢 **the KB has the current name; PyPI `openbadges` still declares the pre-2022 `IMSGlobal/...`**, same head `0a66b52` | Apache-2.0 (`LICENSE`) | credentialing | Open Badges validation. Relevant to the skills-economy trend: competency claims a third party can verify. |
| [opencast/opencast](https://github.com/opencast/opencast) | ECL-2.0 (`LICENSE`) | lecture capture | Video capture, processing and delivery for universities. ECL-2.0 is an Apache-2.0 derivative, so it is **permissive** — the recorded-lecture corpus it produces is the natural input to the P2 ingestion pipeline. |

## Added in the third pass of 2026-10-06

Four infrastructure rows, each probed this pass. Three of them exist because
`Selleo/mentingo` (MIT) demonstrated a leaner sovereign stack than the one this KB
had been assembling by hand — see `verticals/solutions.md`.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | **PostgreSQL License** (`LICENSE`) — permissive, BSD-like | retrieval | Vector similarity search **inside PostgreSQL**. Removes a whole component from a sovereign deployment: no separate vector database to host, secure, back up and keep in-region. Where this KB previously reached for a dedicated vector store, reach for this first. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | **MIT, with a carve-out** (`LICENSE`) — see the warning below, and ⚠️ **the holder on that payload is `ClickHouse, Inc.`, not Langfuse** (the dual-licence wrapper was copied in, holder line and all). The grant text is MIT-Expat and unaffected; the **named grantor is a company that does not own the code**, which is a line a legal review will stop on | LLM observability | Traces every model call with cost, latency and the actual output. In a high-risk education deployment this is the **audit trail produced as a by-product of normal operation**, rather than as a separate compliance project. The single highest-leverage addition to every pattern in this KB. |
| [livekit/livekit](https://github.com/livekit/livekit) | **Apache-2.0** (`LICENSE`) | real-time voice | WebRTC infrastructure for spoken practice, oral assessment and role-play. The permissive path to voice tutoring, which is otherwise a proprietary-API-shaped problem. |
| [KualiCo/rice](https://github.com/KualiCo/rice) | **ECL-2.0** (`LICENSE.txt`) — permissive | higher-ed middleware | Application framework, workflow and eDocLite document routing built for and by the higher-education community. Java, 4★, 12 forks. **In maintenance mode** by its own README — vendor and fork it, do not present it as a living upstream. Full estate breakdown in `verticals/solutions.md`. |

### Two licence warnings on the rows above

**Langfuse is MIT *except* its `ee/` directories, and the copyright holder is now
ClickHouse, Inc.** The `LICENSE` payload is explicit: content under `ee/`,
`web/src/ee/` and `worker/src/ee/` is governed by a separate enterprise licence at
`ee/LICENSE`; everything outside those paths is MIT Expat. The copyright line reads
**"Copyright (c) 2023-2026 ClickHouse, Inc."** Two consequences: a repo-level "MIT"
badge is **not** sufficient diligence on an open-core project — the carve-out is by
*directory*, so the probe has to read the payload and the paths, not the badge. And
the copyright holder on a dependency can change under you between passes, which
nothing in a licence probe will flag. Build against the MIT paths, exclude `ee/`
from any vendored copy, and record the holder as well as the licence.

**pgvector is under the PostgreSQL License, not MIT, Apache-2.0 or BSD by name.**
It is permissive and BSD-like, and a naive allowlist that string-matches
`MIT|Apache|BSD` will reject it. Together with ECL-2.0 (Sakai, Opencast, Kuali
Rice) that is **four** genuinely permissive licences this KB relies on that a
three-name allowlist throws away. The allowlist for an education engagement is:
**MIT, Apache-2.0, BSD (2/3-clause), ECL-2.0, PostgreSQL License, ISC** — and read
the payload for carve-outs before trusting any of them.

## Added in the fourth pass of 2026-10-06

Channels new to this KB: **paper-to-repository tracing** (arXiv, ACL Anthology)
and a **GitHub-organisation sweep**. Licences read from each repository's own
`LICENSE` payload via `raw.githubusercontent.com`.

| Repo | Licence (read from payload) | ★ | Role in a build |
|---|---|---|---|
| [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** (`LICENSE`, © 2026 THU-MAIC) | **40.0k** | **The content-generation spine.** Tsinghua's Open Multi-Agent Interactive Classroom: topic or document → slides, quizzes, HTML simulations and PBL scenes, delivered by AI teacher + AI classmate agents with TTS and a shared whiteboard; exports PPTX and interactive HTML. v1.2.0-rc.1 (2026-10-04) is **server-first with PostgreSQL persistence**, so generation survives a closed tab or restart. TypeScript / Next.js / React. |
| [AI-for-Education/fabdata-llm](https://github.com/AI-for-Education/fabdata-llm) | **MIT** (`LICENSE`) | 9 | Multi-provider LLM interface and chatbot management. A small, readable alternative to a heavyweight gateway when the deployment has to stay auditable. Python. |
| [AI-for-Education/fabdata-parsedoc](https://github.com/AI-for-Education/fabdata-parsedoc) | **MIT** (`LICENSE`) | 2 | Document text extraction, parsing and summarisation — the ingest stage ahead of any content pipeline. Python. Pair with or compare against `opendatalab/MinerU` already on this shelf. |
| [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** (`LICENSE`) | 12 | **Model-selection instrument.** Scores LLMs on *pedagogical knowledge* using teacher-qualification exam questions, rather than on task accuracy. The only thing on this shelf that answers "which model should teach this?" with evidence. Python. |
| [AI-for-Education/voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework) | **MIT** (`LICENSE`) | 1 | Evaluation harness for **voice** interfaces — the modality that binds where literacy, device cost or bandwidth do. Python. |

**Star counts, stated plainly.** OpenMAIC is a flagship at 40.0k★. The four
`AI-for-Education` libraries are **1–12★ research-grade code** and should be read
and vendored deliberately, not pinned as if they were maintained infrastructure.
They are listed because this KB had **no permissive entry at all** for pedagogical
model selection or voice evaluation, and because they are the **first
Africa-placed repositories it has recorded** — the organisation's work is built
for **Sierra Leone's MBSSE** and for **Uganda** (Luganda).

**One sibling in that organisation is not usable:**
[`Luganda-linguistic-benchmarks`](https://github.com/AI-for-Education/Luganda-linguistic-benchmarks)
has **no `LICENSE` payload** (`README.md` 200, `LICENSE` 404). Five MIT siblings do
not license the sixth.

## Added in the fifth pass of 2026-10-06

**Channel: institution-first search** — funding bodies, ministries, universities
and research groups, queried by name in English and Spanish. All licences read
from each repository's own `LICENSE` payload via `raw.githubusercontent.com`.

| Repo | Licence (read from payload) | ★ | Role in the stack |
|---|---|---|---|
| [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) | **MIT** (`master/LICENSE`, © 2023 Coursemology.org) | **158** · 78 forks · **15,802 commits** | **LMS core, permissive.** NUS-origin gamified learning platform: Rails 8 API, React client, Keycloak auth. "Currently supported by the AI Centre for Educational Technologies" and the deployment host for Singapore's **Codaveri** programming tutor. The one MIT LMS in this KB with a decade-scale commit history |
| [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) | **MIT** (`main/LICENSE`, 2026) | 8 · 2 forks · 98 commits | **Compliance scaffolding.** Six-tier risk classifier over the Act's decision tree, **61 conformity checklist items** (risk management, data governance, documentation, human oversight), **8 document templates**. CLI + zero-dependency TypeScript SDK + client-only Next.js UI. **No education content** — supply the Annex III point 3 profile yourself (pattern P13) |
| [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) | **Apache-2.0** (`main/LICENSE`) | not read this pass | **Compliance measurement.** ETH Zurich framework pairing a technical interpretation of the AI Act with a generative-model benchmarking suite. Use it for the evidence the checklist above asks for |
| [crpf-mitadt/Indian-AI-for-Education](https://github.com/crpf-mitadt/Indian-AI-for-Education) | **CC0-1.0** (`main/LICENSE`) | not read this pass | **Regional index, not a dependency.** Curated map of Indian education AI: datasets, models, ASR, TTS, OCR, machine translation, infrastructure, benchmarks, research. CC0 means the map is free of attribution obligations; **every item it indexes still needs its own payload probe** |

### Coursemology is the licence answer to the Moodle question

This KB's platform shortcut has sent "needs permissive IP with no copyleft
exposure" to Frappe LMS and Kolibri, because Moodle, Open edX, Chamilo, Sakai and
ILIAS are all GPL-family. Coursemology changes that answer for **higher-education
and CS-teaching** engagements specifically:

| | Moodle / Open edX | Coursemology |
|---|---|---|
| Licence | GPL-3.0 / AGPL-3.0 family | **MIT** |
| Client fork, rebranded and resold | copyleft obligations attach | **no copyleft exposure** |
| Commit history | very large | **15,802 commits** |
| Community size | enormous | **158★ — small, and that is the real risk** |
| AI integration today | plugin / XBlock side-car | AICET's Codaveri already runs on it, closed source |

**The honest trade.** You swap a copyleft obligation for a **maintenance
concentration risk**: 158★ means a small contributor base and, realistically,
NUS-dependent maintenance. Take Coursemology where the client wants to own and
rebrand the platform outright and has engineering capacity; stay on Moodle or Open
edX where community breadth and plugin supply matter more than licence purity.
Do not present it as a drop-in Moodle replacement — its data model and its Keycloak
dependency are not Moodle's.

### A licence warning that applies per model, not per repository

[aisingapore/sealion](https://github.com/aisingapore/sealion) (424★) is the
substrate anyone would reach for to build a Southeast Asian education layer, and
it has **no `LICENSE` payload** at any probed path. Its README §Licensing says
the project embraces MIT "as much as possible; however, the exact licensing terms
may vary depending on the underlying base model's restrictions" — Llama3-derived
variants carry **commercial-use restrictions**, Gemma-derived variants carry
different terms again — and directs you to each model's **Hugging Face model
card**.

**So: clear rights per model, per release, before a SEA sovereign-model education
engagement is scoped.** A repository-level licence check on `sealion` returns
nothing, and a studio that stops there will have cleared nothing at all.

## Added in the sixth pass of 2026-10-06 — the speech and language substrate

Every tutor elsewhere in this KB is, by default, **mute and monolingual**. This
shelf is the layer that fixes that, and before this pass the KB had **no entry for
it at all**. Licences read from each repository's own `LICENSE` payload via
`raw.githubusercontent.com` on 2026-10-06; star/fork/commit counts read from the
repository page. Discovery narrative in `agents/trending.md`, sixth pass.

### Speech — recognition, synthesis, diarization

| Repo | Licence (payload) | ★ / commits | Role |
|---|---|---|---|
| [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`) | **15.1k** / 2,092 | **The headline addition.** STT **+** TTS **+** speaker diarization **+** VAD in one permissive tree, running **with no Internet connection** on Android, iOS, HarmonyOS, Raspberry Pi, RISC-V and x86 servers, with bindings for 12 languages. Replaces four dependencies with one and is the component the offline-first pattern was missing |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | **MIT** (`master/LICENSE`) | 25.7k / 267 | **The ASR to deploy.** CTranslate2 reimplementation of Whisper — faster, lower memory, same weights |
| [openai/whisper](https://github.com/openai/whisper) | **MIT** (`main/LICENSE`) | **110k** / 171 | The reference implementation and the accuracy baseline to quote |
| [m-bain/whisperX](https://github.com/m-bain/whisperX) | **BSD** (`main/LICENSE`) | — | **Word-level timestamps** plus diarization. The timestamps are what turn a transcript into a *fluency measure* — see P17 |
| [speechbrain/speechbrain](https://github.com/speechbrain/speechbrain) | **Apache-2.0** (`main/LICENSE`) | 11.9k / **10,611** | PyTorch toolkit: 200+ training recipes over 40+ datasets, 20 speech and text tasks. The bridge when a language needs a model trained rather than downloaded |
| [espnet/espnet](https://github.com/espnet/espnet) | **Apache-2.0** (`master/LICENSE`) | 10.0k / **27,378** | End-to-end speech toolkit with the deepest recipe archive here. First stop for a language nothing off-the-shelf covers |
| [huggingface/parler-tts](https://github.com/huggingface/parler-tts) | **Apache-2.0** (`main/LICENSE`) | 5.6k / 199 | Prompt-controllable TTS — the voice is described in text, so register can be tuned per age group without retraining |
| [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo) — ⚠️ **now `NVIDIA-NeMo/NeMo`**; both paths serve head `50c71db`, see the canonical-name table below | **Apache-2.0** (`main/LICENSE`) | — | Full speech + LLM training stack where GPUs are available |
| [pytorch/audio](https://github.com/pytorch/audio) | **BSD** (`main/LICENSE`) | — | Audio primitives underneath the above |
| [idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) | **MPL-2.0** (`main/LICENSE.txt`) | 2.3k / **5,309** | Voice cloning and XTTS-class synthesis, **actively maintained** at Idiap Research Institute (Switzerland). PyPI `coqui-tts`. **Use this, not the 46.1k★ original** — see the warnings below |

### Language — translation and local-language models, placed by region

| Repo | Licence (payload) | ★ / commits | Region | Coverage |
|---|---|---|---|---|
| [AI4Bharat/IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) | **MIT** (`main/LICENSE`) | 478 / 124 | APAC | Translation across **all 22 scheduled Indian languages**, with script unification across Devanagari, Perso-Arabic and others |
| [AI4Bharat/Indic-TTS](https://github.com/AI4Bharat/Indic-TTS) | **MIT** (`master/LICENSE.txt`) | 406 / 58 | APAC | TTS in **13** languages: Assamese, Bengali, Bodo, Gujarati, Hindi, Kannada, Malayalam, Manipuri, Marathi, Odia, Rajasthani, Tamil, Telugu |
| [AI4Bharat/IndicWav2Vec](https://github.com/AI4Bharat/IndicWav2Vec) | **MIT** (`main/LICENSE`) | 121 / 131 | APAC | ASR pretrained on **40** Indian languages; fine-tuned for Bengali, Gujarati, Hindi, Marathi, Nepali, Odia, Tamil, Telugu, Sinhala, plus Kannada and Malayalam |
| [AI4Bharat/IndicLLMSuite](https://github.com/AI4Bharat/IndicLLMSuite) | **MIT** (`master/LICENSE`) | — | APAC | Data and recipe suite for building Indic LLMs |
| [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** (`master/LICENSE`) | 72 / 69 | APAC | *"Open source platform to annotate and label data at scale."* The **human-in-the-loop stage** every pattern in this KB specifies, and the only shelved tool that implements it |
| [SunbirdAI/salt](https://github.com/SunbirdAI/salt) | **Apache-2.0** (`main/LICENSE`) | 15 / 303 | EMEA | **Uganda.** Translation (~25k sentences), ASR (~5k) and **studio-recorded TTS data (~5k, professional voice actors)** across English (Ugandan/Kenyan accents), **Luganda, Swahili, Ateso, Lugbara, Acholi, Runyankole**. Two AfricaNLP papers |
| [masakhane-io/masakhane-mt](https://github.com/masakhane-io/masakhane-mt) | **MIT** (`master/LICENSE`) | 327 / 645 | EMEA | **Africa-wide.** Machine translation from a 1,000-participant, 30-country community. **226 forks against 327 stars** — a deployment signal, not a vanity one |
| [masakhane-io/masakhane-ner](https://github.com/masakhane-io/masakhane-ner) | **Apache-2.0** (`main/LICENSE`) | — | EMEA | Named-entity recognition for African languages |
| [Polygl0t/Polygl0t](https://github.com/Polygl0t/Polygl0t) | **Apache-2.0** (`main/LICENSE`) | 27 / 379 | EMEA | **University of Bonn** Polyglot initiative. LLM training/eval foundry, FineWeb-2 pipeline, "support for thousands of languages." Home of **Tucano 2** (0.5–3.7B Portuguese, arXiv 2603.03543) |
| [Nkluge-correa/Tucano](https://github.com/Nkluge-correa/Tucano) | **Apache-2.0** (`main/LICENSE`) | 86 / 29 | LATAM *(origin)* | Portuguese-native open LLM suite, peer-reviewed in *Patterns* ([10.1016/j.patter.2025.101325](https://doi.org/10.1016/j.patter.2025.101325)). **Archived 2026-02-24** — still usable, no longer developed. Successor is the Bonn-hosted row above |

### Five licence warnings on the rows above — read before selecting any of them

**1. Piper relicensed, and the permissive version is frozen.**
[rhasspy/piper](https://github.com/rhasspy/piper) is **MIT** (`master/LICENSE.md`,
© 2022 Michael Hansen), 11.3k★ — and **archived read-only since 2025-10-06**, its
notice pointing to [OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl),
which is **GPL-3.0** (`main/COPYING`). Piper is the offline-TTS default of Home
Assistant and NVDA and runs on a Pi 4, so it is the natural reach for low-cost
classroom voice. **There is no option that is both permissive and maintained.**
Deliberately **not shelved above**: use `sherpa-onnx` (Apache-2.0) or
`idiap/coqui-ai-TTS` (MPL-2.0) instead, and reach for Piper only with the
frozen-vs-copyleft trade made explicitly and in writing.

**2. The 46.1k★ Coqui repository is not the live one.**
[coqui-ai/TTS](https://github.com/coqui-ai/TTS) is **MPL-2.0** and **unmaintained**
— the company wound down. The Idiap fork shelved above has **5,309 commits against
the original's 4,668**. Depend on the fork; cite the original only for history.

**3. SeamlessM4T is non-commercial — a hard reject.**
[facebookresearch/seamless_communication](https://github.com/facebookresearch/seamless_communication)
carries **Attribution-NonCommercial 4.0 International** in `main/LICENSE`. It is
the first result for "open source multilingual speech" and **cannot be used in
billable work**. Compose Whisper (MIT) + IndicTrans2 (MIT), or sherpa-onnx
(Apache-2.0), to reach the same capability.

**4. SEA-LION has no repository-level grant, by design.**
[aisingapore/sea-lion](https://github.com/aisingapore/sea-lion) has **no `LICENSE`
payload** (3 branches × 6 filenames probed). Its README states the terms *"may
vary depending on the underlying base model's restrictions"* — Llama-derived
variants may carry Meta's commercial restrictions — and directs you to each
HuggingFace **model card**. **The licence is a property of the checkpoint, not the
project**, so an APAC engagement must review it per model file and **re-review on
every checkpoint change**. Not shelved as a dependency for this reason.

**5. An unlicensed catalogue is still unlicensed.**
[AI4Bharat/indicnlp_catalog](https://github.com/AI4Bharat/indicnlp_catalog) has
**no `LICENSE` payload** despite five MIT siblings in the same organisation. Use
it to *find* resources; probe every resource it names. (Same shape as
`AI-for-Education/Luganda-linguistic-benchmarks` in the fourth pass — and note
that `SunbirdAI/salt` above is the **Apache-2.0 answer to that specific
rejection**, covering Luganda and five more Ugandan languages.)

### Why this shelf changes the architecture, not just the feature list

Three consequences worth stating, because they are not obvious from the table:

- **Voice stops being a proprietary-API-shaped problem.** `sherpa-onnx` alone
  delivers STT, TTS, diarization and VAD under Apache-2.0 on embedded hardware.
  Spoken practice, oral assessment and role-play become deployable where there is
  no connectivity and no per-token budget.
- **Mother-tongue instruction becomes a permissive capability in two regions.**
  India (22 languages, MIT) and Uganda/Africa (6 Ugandan languages Apache-2.0,
  plus Masakhane's continental MT, MIT) can be served from the shelf. **Elsewhere
  it cannot** — see the regional honesty note in `intel/market.md`.
  **⚠️ SUPERSEDED by the seventh pass of 2026-10-06: it is at least three
  regions.** ASEAN has a permissive layer across **Vietnamese, Thai, Malay and
  Indonesian** — `underthesea` (Apache-2.0, 1.8k★), `pythainlp` (Apache-2.0,
  1.2k★, 6,649 commits), `malaya` + `malaya-speech` (both MIT) and `nusa-crowd`
  (Apache-2.0, 143 datasets). See the seventh-pass section below. The sixth pass
  reached "two regions" by searching for sovereign **models** and finding
  SEA-LION unlicensed; the toolkits were one query away in another language.
- **Masakhane licenses three repositories three ways** — MIT, Apache-2.0 and GPL
  inside one owner. The fourth pass's rule was "five MIT siblings do not license
  the sixth." The stronger rule: **sibling licences need not even share a
  class.** Probe every repository, every time.

## Added in the seventh pass of 2026-10-06 — the ASEAN language substrate, and trend 21 falsified

**Channel new to this KB this pass: native-language search.** Earlier passes
searched in English and, in the fourth pass, Spanish and Portuguese. This pass
searched in **Japanese, Korean, Arabic and Bahasa/Thai/Vietnamese**. The sixth
pass had closed with a clean, falsifiable claim — *"mother-tongue AI is a
two-region capability"*, India and Africa, with ASEAN explicitly named as the
place where *"the nearest thing, SEA-LION, has no repository-level licence at
all."*

**That claim is wrong, and this is the shelf that falsifies it.** ASEAN has a
permissive, self-hostable language layer covering **five languages across four
countries**, most of it Apache-2.0, some of it with more commits than anything
on the India shelf. It was invisible to six passes because **SEA-LION is a
sovereign *model* and these are language *toolkits*** — a different noun, and
nobody had searched for the noun.

Licences read from each repository's own `LICENSE` payload via
`raw.githubusercontent.com` on 2026-10-06; star/fork/commit counts read from the
repository page the same day. **13 repositories probed, 13 resolved.**

### Language — ASEAN, placed by country

| Repo | Licence (payload) | ★ / forks / commits | Country | Coverage |
|---|---|---|---|---|
| [undertheseanlp/underthesea](https://github.com/undertheseanlp/underthesea) | **Apache-2.0** (`main/LICENSE`) | **1.8k** / 307 / 1,276 | **Vietnam** | The largest asset on this shelf. 13 Vietnamese tasks — sentence segmentation, text normalization, **diacritics restoration**, word segmentation, POS, chunking, NER, classification, sentiment, language detection, dependency parsing, translation and TTS. **v9.3.0 rebranded the project to an "Open-source Agentic AI Toolkit"** with multi-provider agent support (OpenAI, Azure OpenAI, Anthropic Claude, Google Gemini) layered over the Vietnamese NLP core |
| [PyThaiNLP/pythainlp](https://github.com/PyThaiNLP/pythainlp) | **Apache-2.0** (`main/LICENSE`) | **1.2k** / 304 / **6,649** | **Thailand** | *"Thai natural language processing in Python."* Sentence, word and **subword** tokenization — the hard problem in a script with no spaces — plus POS tagging, romanization and **IPA transliteration**, spelling correction, soundex, collation, number-to-text, and a `thainlp` CLI. v5.3.8, Python 3.9+, self-declared **"Project Status: Active."** The deepest commit history of any language toolkit in this KB outside the general speech shelf |
| [malaysia-ai/malaya](https://github.com/malaysia-ai/malaya) | **MIT** (`master/LICENSE`, © 2018 huseinzol05) | 530 / 141 / 961 | **Malaysia** | *"Natural-Language-Toolkit library for bahasa Malaysia, powered by PyTorch."* NER with a named-entity framework, POS, sentiment, emotion, subjectivity, language detection and normalization. Pretrained models on HuggingFace (`mesolitica`); docs at `malaya.readthedocs.io` |
| [malaysia-ai/malaya-speech](https://github.com/malaysia-ai/malaya-speech) | **MIT** (`master/LICENSE`, © 2020 HUSEIN ZOLKEPLI) | 291 / 51 / 755 | **Malaysia** | *"Speech-Toolkit library for Malaysian language, powered by PyTorch."* The **only ASEAN-placed permissive speech toolkit** found; ships a `malay_vits` TTS path. Pair with `sherpa-onnx` for the offline runtime |
| [IndoNLP/nusa-crowd](https://github.com/IndoNLP/nusa-crowd) | **Apache-2.0** (`master/LICENSE`) | 292 / 64 / 992 | **Indonesia** | *"A collaborative project to collect datasets in Indonesian languages."* **143 registered datasets** behind standardized dataloaders, built by a credited multi-institution consortium; paper *NusaCrowd: Open Source Initiative for Indonesian NLP Resources* ([arXiv:2212.09648](https://arxiv.org/abs/2212.09648)). Contributors earn **co-authorship by contribution points** — a governance model worth copying for a ministry corpus engagement |
| [indobenchmark/indonlu](https://github.com/indobenchmark/indonlu) | **Apache-2.0** (`master/LICENSE`) | — (not read this pass) | **Indonesia** | Indonesian natural-language-understanding benchmark — the evaluation half of the row above |

### Read this shelf honestly — three qualifications

- **None of it is education-specific.** Exactly like AI4Bharat on the India
  shelf, these are general-purpose language toolkits. They make a mother-tongue
  tutor *possible*; they do not make one. The pedagogy layer is still yours to
  build, which is the opportunity (**P19**).
- **Only one covers speech.** `malaya-speech` is the single ASEAN-placed
  permissive speech toolkit here. Thai, Vietnamese and Indonesian have the
  **text** layer and no local **voice** layer, so spoken practice in those three
  languages routes through the general shelf — `sherpa-onnx` (Apache-2.0) or
  Whisper/faster-whisper (MIT) — and must be accuracy-tested per language rather
  than assumed.
- **Two of these are corpora-and-recipes, not runtimes.** `nusa-crowd` and
  `indonlu` give you data and evaluation; they are not something you deploy. Size
  the engagement accordingly.

### One more licence warning, and the first measured counter-example to it

[malaysia-ai/malaysian-dataset](https://github.com/malaysia-ai/malaysian-dataset)
— **no `LICENSE` payload** (2 branches × 6 filenames probed), and at **345★** it
is the organisation's **second most-starred repository**, ahead of
`malaya-speech`. Its two code siblings are both MIT. **Not shelved. Not
shippable.**

This is the **second time this KB has found the pattern in the same shape**: the
sixth pass recorded `AI4Bharat/indicnlp_catalog` as unlicensed among five MIT
siblings. Two independent organisations, two regions, and in both the repository
without a grant is the **data/catalogue** one while the **code** repositories are
permissive. A tempting rule follows — *the data layer is where the grant goes
missing* — and this pass **measured its counter-example in the same sweep**:
`IndoNLP/nusa-crowd` is a dataset hub of 143 corpora and it is **Apache-2.0**.

**So state it as a prior, not a law: on a data or catalogue repository, assume no
grant until the payload says otherwise — and probe it, because one in three
cedes.** The operational rule is unchanged and now carries three instances
instead of one: **probe every repository, every time, and probe the dataset
sibling separately from the code.**

## Added in the eighth pass of 2026-10-06 — the LATAM language substrate, and where it stops

The seventh pass falsified "mother-tongue AI is a two-region capability" by
searching ASEAN for language **toolkits** instead of sovereign **models**. The
eighth pass ran the same move at the one gap this KB called its firmest: **no
LATAM-origin permissive education project.**

**The move works at the majority-language layer and fails at the indigenous
layer — and it fails for a reason this shelf has seen before in MEA.**
Licences read from each repository's own `LICENSE` payload.

### Language — Spanish and Portuguese, permissive and real

| Repo | Licence (payload) | ★ / forks / commits | What it is |
|---|---|---|---|
| [neuralmind-ai/portuguese-bert](https://github.com/neuralmind-ai/portuguese-bert) | **MIT** (`master/LICENSE`, © 2020 NeuralMind — Fabio Capuano de Souza, Rodrigo Nogueira, Roberto de Alencar Lotufo) | **886** / 139 / 20 | **BERTimbau** — BERT-Base and BERT-Large for **Brazilian Portuguese**, trained on **BrWaC** for 1M steps with whole-word masking. State of the art on NER, STS and RTE at publication. **Brazil-origin, and the first Brazil-origin permissive asset on this shelf** |
| [alphacep/vosk-api](https://github.com/alphacep/vosk-api) | **Apache-2.0** (`master/COPYING`) | — | Offline ASR for 20+ languages including **Spanish and Portuguese**, Raspberry-Pi-class hardware, Python/Java/C#/Node bindings. Permissive, maintained — **global-origin, not LATAM** |

`speechbrain/speechbrain` (Apache-2.0) on the sixth-pass shelf remains the
bridge when a language needs a model **trained** rather than downloaded.

### Language — indigenous languages of the Americas: the capability is there, the grant is not

| Repo | Licence state (payload) | Coverage |
|---|---|---|
| [Llamacha/IWSLT2023_Quechua_data](https://github.com/Llamacha/IWSLT2023_Quechua_data) | ⚠️ payload **Apache-2.0**, README **CC BY-NC-ND 3.0** — **scope conflict, see below** | **Peru** — ~1h40m aligned Quechua–Spanish speech + pointers to 60h transcribed Siminchik audio. Southern Quechua |
| [pywirrarika/naki](https://github.com/pywirrarika/naki) | **GPL-3.0** (`master/LICENSE`) | Curated NLP research and engineering index for Native American languages |
| [AmericasNLP/americasnlp2021](https://github.com/AmericasNLP/americasnlp2021) | **No `LICENSE` payload** | Shared task — **Aymara** (6,531 pairs), **Nahuatl** (16,145), **Quechua** (125,008) |
| [AmericasNLP/americasnlp2022](https://github.com/AmericasNLP/americasnlp2022) | **No `LICENSE` payload** | Second probed edition |
| [AmericasNLP/americasnlp2023](https://github.com/AmericasNLP/americasnlp2023) | **No `LICENSE` payload** | Third probed edition |
| [AmericasNLP/americasnlp2024](https://github.com/AmericasNLP/americasnlp2024) | **No `LICENSE` payload** — 404 at root **and** in both task subdirectories | MT into indigenous languages, **plus Shared Task 2: "Creation of Educational Materials for Indigenous Languages"** — sentence-transformation and fill-in-the-blank exercise generation, data and baselines shipped. **No root `README.md`; existence confirmed via `master/ST1_MachineTranslation/README.md`** |
| [monirome/asr-indigenous-languages](https://github.com/monirome/asr-indigenous-languages) | **No `LICENSE` payload** | Fine-tuned ASR: **Quechua, Guaraní, Bribri, Kotiria, Wai'khana** |
| [UBC-NLP/IndT5](https://github.com/UBC-NLP/IndT5) | **No `LICENSE` payload** | Text-to-text transformer for **10** indigenous languages |
| [aoncevay/mt-peru](https://github.com/aoncevay/mt-peru) | **No `LICENSE` payload** | *"Peru is Multilingual, Its Machine Translation Should Be Too?"* |
| [aoncevay/quechua-nlp](https://github.com/aoncevay/quechua-nlp) | **No `LICENSE` payload** | Standard Southern Quechua data for NLP |
| [Llamacha/IWSLT2025_Quechua_data](https://github.com/Llamacha/IWSLT2025_Quechua_data) | **No `LICENSE` payload** | The 2025 edition — **same organisation, licensed 2023 and not 2025** |
| [jnehring/awesome-low-resource-languages](https://github.com/jnehring/awesome-low-resource-languages) | **No `LICENSE` payload** | Endangered / low-resource language resource index |

**Ten of twelve carry no grant at all.** **AmericasNLP** — the flagship academic
venue for the indigenous languages of the Americas — has run **four probed
editions (2021, 2022, 2023, 2024) without a `LICENSE` file in any of them**, and
its 2024 edition ships the one task on this shelf that is **explicitly an
education task**: *"Creation of Educational Materials for Indigenous
Languages"*, with data and baseline scripts and no grant. The same author
(`aoncevay`) licensed neither of two repositories; the same organisation
(`Llamacha`) licensed one edition and not the next.

### ⚠️ The `Llamacha` scope conflict — it defeats this shelf's own method

Every licence on this shelf is read from the repository's own `LICENSE` payload.
Do that to `Llamacha/IWSLT2023_Quechua_data` and you get **complete, unambiguous
Apache-2.0** from `main/LICENSE`.

**The README says otherwise:**

> All audio recordings are property of Siminchikkunarayku and Llamacha.
> This work is licensed under a Creative Commons
> **Attribution-NonCommercial-NoDerivs 3.0 Unported License**.

**NonCommercial and NoDerivs — unusable in commercial client work.** The Apache
file plausibly covers the repository's scripts; the **data**, which is the only
reason to clone it, is NC/ND.

**This is a third licence trap, distinct from the two this KB already tracks.**
`p184` catches a holder foreign to the project. The seventh pass's
MathTutorBench case catches a file that contradicts itself internally. This is
**a correct, complete licence file applied to the wrong scope.**

**Rule for this shelf, from this pass forward: for any repository whose value is
data, audio, a corpus or model weights, the payload is necessary and not
sufficient.** Read the README's licence section too, and treat the
**asset-scope** statement as controlling for the asset.

### Why this shelf matters even though most of it is unusable

**Because it is the exact layer a regional tutor needs next, and it is one
`LICENSE` file per repository away from being usable.**

`LabSirius/TutorIA`'s own **RNF-10** specifies Colombian Spanish for v1.0 *"con
posibilidad futura de soportar **lenguas nativas**"*. Latam-GPT lists indigenous
languages as roadmap. So the demand is written down in two places, and the
supply — corpora, ASR for five languages, MT, benchmarks, a T5 for ten
languages — **already exists, funded and published.** What is missing is
redistribution rights.

**This is the MEA diagnosis in a second region.** The seventh pass concluded of
MEA: *"the binding constraint is not interest, funding or capability — it is
licensing hygiene. Three `LICENSE` files would change the regional answer."*
That sentence is now true of the LATAM indigenous layer word for word, and the
eighth pass found a **remedy that works prospectively**: a submission rule in a
university event's terms produced **20 licensed repositories in eight hours**
(see `agents/top.md`, the CAi UC holder warning, and `intel/market.md`).

**For an engagement:** a Quechua or Guaraní tutor is blocked on **data rights,
not on modelling**. Budget the licence conversation with Llamacha,
Siminchikkunarayku and the AmericasNLP organisers as a project line item, not an
afterthought — and note that `vosk-api` (Apache-2.0) plus `speechbrain`
(Apache-2.0) give you a permissive *pipeline* into which licensed data can be
dropped the moment it exists.

## Added in the ninth pass of 2026-10-06 — a ministry's MIT estate, and the offline stack's real licence shape

Channel: the **funder and procurement channel** and its government twin, the
**education-ministry engineering organisation**. Nine passes had swept
hackathons, universities, ministries *by name*, funding bodies, GitHub topic
pages and academic papers. **None had swept a ministry's own GitHub org.**

### The UK Department for Education estate — government-grade, production, MIT

`DFE-Digital` is the UK Department for Education's engineering org. It runs
**live national education services** in the open, under MIT. Licences read from
payload:

| Repo | Licence | ★ | Lang | Role |
|---|---|---|---|---|
| [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | **MIT** (`main/LICENCE`) | 38 | Ruby | The national service for applying to teacher-training courses |
| [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | **MIT** (`main/LICENSE`) | 27 | Ruby | National teaching job-listing service |
| [DFE-Digital/get-into-teaching-app](https://github.com/DFE-Digital/get-into-teaching-app) | **MIT** (`master/LICENCE`) | 25 | Ruby | Teacher-recruitment site and candidate journey |
| [DFE-Digital/publish-teacher-training](https://github.com/DFE-Digital/publish-teacher-training) | **MIT** (`main/LICENSE`) | 12 | Ruby | Provider course publishing + candidate discovery |
| [DFE-Digital/register-trainee-teachers](https://github.com/DFE-Digital/register-trainee-teachers) | **MIT** (`main/LICENCE`) | 12 | Ruby | Trainee registration for initial-teacher-training placements |
| [DFE-Digital/get-information-about-schools](https://github.com/DFE-Digital/get-information-about-schools) | **MIT** (`main/LICENCE`) | 9 | C# | GIAS — the national schools register |
| [DFE-Digital/education-benchmarking-and-insights](https://github.com/DFE-Digital/education-benchmarking-and-insights) | **MIT** (`main/LICENSE`) | 5 | C# | Compares one school's metrics against similar institutions |

### What this estate is good for, stated precisely

**It is administrative software, not AI, and it closes no AI gap in this KB.**
Taken for what it is, it is the first thing of its kind on these shelves:

1. **Reference architecture for education workflow at national scale.** Five of
   the seven are Ruby services that have run a country's teacher pipeline.
   For an EMEA public-sector engagement, *"here is how a ministry built this, and
   you may read and reuse the code"* is a stronger opening than a vendor demo.
2. **Schemas you will have to integrate with anyway.** GIAS is the UK's
   authoritative schools register; `register-trainee-teachers` and
   `publish-teacher-training` encode the ITT domain model. Any UK education
   engagement meets these data structures eventually — and here they are, MIT.
3. **A benchmarking component with the right shape.**
   `education-benchmarking-and-insights` does school-to-peer-group comparison —
   the data layer under any "how is my school doing" analytic, and the natural
   grounding source for a reporting agent.
4. **Procurement credibility.** An MIT licence from a ministry is the cleanest
   possible answer to the public-sector question *"can we actually own and audit
   this?"*

**What it is not:** none of it is AI, none of it is a tutor, and its star counts
(5–38★) reflect government repos that are consumed as services rather than
forked. **Do not read low stars as low maturity here** — these are production
systems for a national education system. It is the one place in this KB where
the star signal is actively misleading in the *opposite* direction to usual.

### ⚠️ The licence-filename warning that changes this KB's method

**Four of these seven grants are in a file spelled `LICENCE`.** Pattern **P22**'s
gate lists that spelling; **no recorded sweep in this KB has ever run it.** Every
probe set written down across nine passes — `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `COPYING`, `license.txt` — **matches none of these four files.** With the old set,
`apply-for-teacher-training`, `get-into-teaching-app`,
`register-trainee-teachers` and `get-information-about-schools` would all have
been recorded as **ungranted**. They are MIT.

**The probe set is now `LICENSE{,.md,.txt}`, `LICENCE{,.md,.txt}`, `COPYING`,
`COPYRIGHT`, `license.txt`, both branches.** Any earlier pass's "no grant"
verdict on a Commonwealth, MEA or ministry-adjacent repository should be treated
as **unconfirmed until re-probed** — those are exactly the repositories that
spell it the British way.

### Measured rejections from the same organisation

| Repo | ★ | Why rejected |
|---|---|---|
| `DFE-Digital/gias-query-tool` | 17 | **No licence payload.** The SQL query layer over GIAS — the most immediately useful tool in the org, and ungranted. Sixth pass running in which the most-reached-for asset of a sweep has no grant |
| `DFE-Digital/rsd-ai-libs` | 0 | **No payload.** *".NET library for building and evaluating Azure AI Foundry agents with guardrails, Azure AI Search, and MCP server support"* — a ministry building MCP agent tooling, which corroborates trend 4; unusable as code, citable as a signal |
| `DFE-Digital/sts-ai-support` | 1 | No licence shown on the org listing; not individually payload-probed |
| `DFE-Digital/ai-briefing-tool-prototype` | 0 | Non-production prototype; no licence shown |
| `DFE-Digital/rsd-common-ai-services` | 0 | Provisioning scaffolding; no licence shown |

**The asymmetry is the strategic finding:** the DfE's **administrative** tier is
production-grade and MIT; its **AI** tier is prototype-grade and unlicensed. A
consultancy's opening in EMEA public-sector education is therefore *not* "you
need a platform" — they built one — but **"your AI layer is five unlicensed
prototypes at zero stars, and your administrative layer is a licensed national
asset; let us build the first on top of the second."**

### The offline delivery stack, licence shape corrected

The eighth pass built the offline-first tier around Kolibri and EduFlow but could
not resolve RACHEL. Resolved this pass, and the stack's licensing is not what the
page implied:

| Repo | Payload | Licence | Usable? |
|---|---|---|---|
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | `develop/LICENSE` | **MIT** | ✅ re-confirmed — the platform answer |
| [kiwix/kiwix-tools](https://github.com/kiwix/kiwix-tools) | `main/COPYING` | **GPL-3.0** | ⚠️ copyleft — see below |
| [kiwix/libkiwix](https://github.com/kiwix/libkiwix) | `main/COPYING` | **GPL-3.0** | ⚠️ copyleft |
| [kiwix/kiwix-android](https://github.com/kiwix/kiwix-android) | `main/COPYING` | **GPL-3.0** | ⚠️ copyleft |
| [openzim/libzim](https://github.com/openzim/libzim) | `main/COPYING` | **GPL-2.0** | ⚠️ copyleft, and GPL-2.0 ≠ GPL-3.0 for compatibility |
| [rachelproject/contentshell](https://github.com/rachelproject/contentshell) | **none** | README: *"Creative Commons - BY, SA, NC"* | ❌ **NonCommercial — do not ship** |

**Three warnings on that table:**

1. **RACHEL is out.** `contentshell` *is* RACHEL — the PHP CMS that serves
   content on RACHEL devices — and its only licence statement is a **content
   licence with NonCommercial, applied to software**, with no payload to weigh
   against it. Creative Commons advises against CC for software; either reading
   (unlicensed, or NC) stops a commercial deliverable. **Cite RACHEL as prior
   art for offline delivery; ship Kolibri.**
2. **The ZIM layer is GPL, and that is an architecture decision, not a
   footnote.** Offline Wikipedia/Wikibooks content ships as ZIM, and the entire
   reference implementation — `libzim` (GPL-2.0), `libkiwix`, `kiwix-tools`,
   `kiwix-android` (GPL-3.0) — is copyleft. You may deploy it; you may not
   statically link it into a proprietary client deliverable without taking the
   obligation. **Keep Kiwix as a separate process behind an HTTP boundary** —
   exactly the side-car reasoning this KB already applies to MCP — and the
   client's own code stays unencumbered.
3. **GPL-2.0 and GPL-3.0 in one dependency tree** (`libzim` vs `libkiwix`) is a
   combination to raise with counsel if anything is being linked rather than
   invoked. Process separation makes the question moot, which is a second reason
   for the side-car.

## Added in the twenty-first pass of 2026-10-06 — no new rows, and a second licence on the existing ones

🔵 **This pass adds no foundational repositories, and the reason is structural rather than a dry
sweep.** The declared-dependency channel does not discover projects; it **re-prices the ones already
here**. Every row on this shelf carried one licence — its own. The rows below now carry a second: the
licence of **what they install**.

⚠️ **The platform channel was re-probed and remains saturated**, verified by grep rather than
assumed: OpenEduCat, Open edX, Moodle, Sakai, OLAT/OpenOLAT, Chamilo, Gibbon, Frappe, `.LRN` all
already shelved. The one name new to the result set, **`CK-ERP`** — a 32-module education / ERP / CRM
/ MRP system — is recorded here as a **measured non-finding**: the most recent release note in the
result set is from **2010** and it is Drupal-6 era. 🔴 **Abandonware, not a shelf candidate.**

### What the foundation shelf installs

| Foundation row | Its licence | Direct deps | Closure verdict |
|---|---|---|---|
| `oppia/oppia` | Apache-2.0 | **152** | 🔴 **REVIEW-STRONG** — `mutagen` is `GPL-2.0-or-later`; `certifi` MPL-2.0; `orjson` `MPL-2.0 AND (Apache-2.0 OR MIT)`; `azure-cognitiveservices-speech` `Other/Proprietary License`. **148 of 152 clean** |
| `learningequality/kolibri` | MIT | **32** | ⚠️ **REVIEW-WEAK** — 2 LGPL rows, 2 unreadable. ⚠️ Measurable only via `[dependency-groups] base`; both canonical fields answer "nothing" and both are wrong |
| `huggingface/smolagents` | Apache-2.0 | 6 | 🟢 **CLEAN** — the smallest permissive surface on the shelf, now verified on both layers |
| `microsoft/agent-framework` | MIT | 1 | ⚠️ **CLEAN but uninformative** — `agent-framework-core[all]==1.20.0`; the closure is one level down |

🟢 **The operational consequence for foundation selection:** where two foundations are otherwise
comparable, **the one with the smaller declared surface is the cheaper one to clear legally**, and
that is now a measured property rather than an instinct. smolagents at 6 declared dependencies and
Oppia at 152 are not the same procurement task even when both say Apache-2.0.

### 🔴 The evidence tooling the twentieth pass went looking for is still absent — and now so is one more layer

⚠️ **The twentieth pass recorded zero occurrences of `mlflow`, `dvc`, `evidently`, `whylogs`,
`great_expectations`, `croissant`, `OpenLineage`, `fairlearn` and `AIF360`.** 🔴 **A dependency-licence
audit is the same shape of missing instrument one layer further down:** this KB can now resolve a
licence per dependency, but it has **no SBOM layer** — no `syft`, no `cyclonedx`, no
`pip-licenses`/`license-checker` row anywhere on the shelf. 🔵 **Recorded as a declared gap with a
named next step rather than as a new row, because this pass did not verify any of those tools against
an education deployment and will not shelf what it has not read.**

## Teaching-content repos (for enablement, not for production)

| Repo | License (read from payload) | Note |
|---|---|---|
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | MIT (`LICENSE`) | 18 lessons, 76.5k★ |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | MIT (`LICENSE`) | the GenAI prerequisite track |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Apache-2.0 (`LICENSE.txt`) | builds a GPT-class model in PyTorch; >100k★ class resource |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Apache-2.0 (`LICENSE`) | roadmap + notebooks |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | Apache-2.0 (`LICENSE`) | agent track |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | MIT (`LICENSE`) | APAC-origin, large cohort programme |
| [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | MIT (`LICENSE@main`) | production agentic-RAG — the missing middle between an agent demo and a deployed retrieval system |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | MIT (`LICENSE@main`) | AI-engineering track, trending through 2026 |

## Repos checked and deliberately not recommended

Recording these saves the next pass the probe.

| Repo | Finding |
|---|---|
| [microsoft/autogen](https://github.com/microsoft/autogen) | Maintenance mode, no new features; `LICENSE` at HEAD is CC-BY-4.0 (dual with MIT). Use `microsoft/agent-framework` instead. |
| [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0**, not MIT. Widely mis-reported as MIT by LMS comparison blogs. The license lives at `license.txt` (lowercase) — `LICENSE` returns 404, which is how the misreport propagates. |
| [cloudtoolbox/deeptutor](https://github.com/cloudtoolbox/deeptutor) | 7★ fork of `HKUDS/DeepTutor`. Correct Apache-2.0 license, no history. Pin the HKUDS origin. |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | **Unlicensed.** 103★, 54 tools, v2.3.0 — and no `LICENSE` on any branch, no license statement in the README. Default copyright: all rights reserved. The most dangerous repo in this KB precisely because it looks mature. |
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | **Unlicensed.** 38★, Python, no `LICENSE` on any branch, none in README. |
| [tutornew/OpenTutor](https://github.com/tutornew/OpenTutor) | **Unlicensed.** 8★, 5 commits. Recorded in an earlier cycle of this KB as "MIT, ~900★" — wrong on both counts. Withdrawn; see `agents/top.md`. |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | AGPL-3.0 **plus** a paid premium-plugin tier. Legally usable, commercially the worst shape on the shelf for reusable studio IP. |
| [planejaia/OpenMAIC-Brasil](https://github.com/planejaia/OpenMAIC-Brasil) | **404 — does not exist.** Surfaced by search as a Brazil-origin multi-agent classroom, v1.0.0 "released 2026-08-27". Every file 404s on four branches and the repo page returns HTTP 404. Recorded so the next pass does not chase it again. |
| [frappe/erpnext](https://github.com/frappe/erpnext) | GPL-3.0 at `license.txt` (lowercase) — usable, but listed here because it shares `frappe/lms`'s probe trap: `LICENSE` returns 404. |
| [kuali/kfs](https://github.com/kuali/kfs) | **AGPL-3.0** (`LICENSE`). Kuali Financial System. Same consortium as the permissive Kuali Rice — the licence is per repository, not per foundation. |
| [kuali/kc](https://github.com/kuali/kc) | **AGPL-3.0** (`license.txt`, lowercase). Kuali Coeus research administration. Third live instance of the lowercase-`license.txt` probe trap, after `frappe/lms` and `frappe/erpnext`. |
| [kuali/rice](https://github.com/kuali/rice) | Correct licence (ECL-2.0) but **DEPRECATED** by its own README, which points to `KualiCo/rice`. Pin the KualiCo location. |
| `kuali/student`, `KualiCo/student`, `kuali/coeus` | **Not reachable** — `README.md` 404s on all three. Kuali Student (the SIS) is not at the path its name implies; recorded so the next pass does not re-probe these. |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | **AGPL-3.0**, 563★. Competency skill tree, K-12 to career. Reference for competency-graph design only. |
| [artcc/freelingo](https://github.com/artcc/freelingo) | **AGPL-3.0**, 156★. Self-hosted AI language learning. |
| [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) | **GPL**, 88★. Learner-owned course generation. |
| [yh2072/edgameclaw](https://github.com/yh2072/edgameclaw) | **AGPL-3.0**, 71★. Game-based course conversion. |
| [A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) | **Unlicensed**, 61★. Its README's licence section reads only *"This project is open source and available for educational purposes"* — prose that imitates a grant. No licence, no holder, no redistribution right. |
| [idoforgod/Vibe-learning-AgenticWorkflow](https://github.com/idoforgod/Vibe-learning-AgenticWorkflow) | **Unlicensed**, 24★. No `LICENSE` and no licence mention anywhere in the README. |

## Method note

License probes need both axes — filename *and* extension. `LICENSE`,
`LICENSE.md`, `LICENSE.txt`, `license.txt`, `COPYING` and `COPYING.txt` are all
in live use across this shelf, and probing only `LICENSE` produces false
negatives (`frappe/lms` and `moodle/moodle` both hide from a single-path probe).
A badge or a comparison blog is not a license reading.

A licence probe also needs a third axis: **path depth**. `OS4ED/openSIS-Classic`
404s on every root-level candidate — `LICENSE`, `LICENSE.md`, `COPYING`,
`license`, `License.txt`, `GPL-LICENSE.txt` — while its real licence sits at
**`docs/License.txt`** (GPL-2.0), pointed to only by a Markdown link in the
README. So the probe order that actually works:

1. root filename × extension variants;
2. if all 404, **read the README for a licence link** before recording a gap;
3. follow that link and read the payload.

Skipping step 2 produces a false "unlicensed" verdict on a correctly licensed
project — the mirror image of the false-MIT error `frappe/lms` causes. Both
failure modes now have a live example. Only after step 3 fails is "unlicensed"
a finding: that is how `DMontgomery40/mcp-canvas-lms`, `loyaniu/moodle-mcp` and
`tutornew/OpenTutor` were confirmed above, each checked against eight filename
variants on three branches *and* its README.

**A fourth axis, added 2026-10-06 (third pass): the OWNER.** A 404 or an
unlicensed verdict on `owner/name` is evidence about *that owner's repository
only* — never about the project. The second pass of 2026-10-06 withdrew this KB's
OpenTutor entry after probing `tutornew/OpenTutor` (8★, unlicensed) and the real
project was `zijinz456/OpenTutor` (**MIT, 130★, FSRS 4.5, 12 blocks, LOOM knowledge
graph**) all along. Every other probe lesson in this file guards against a false
*positive*; that one was a **false negative that deleted a true finding**, which is
the more expensive direction because the result is a confident denial rather than a
wasted probe. So: **before withdrawing an entry, enumerate the owners publishing
under that project name.** A withdrawal needs a stronger probe than an addition.

**A fifth axis: the DIRECTORY.** An open-core project can be permissive at the root
and proprietary in a subtree. `langfuse/langfuse` is MIT except `ee/`,
`web/src/ee/` and `worker/src/ee/`, which carry a separate enterprise licence — and
its copyright holder is now ClickHouse, Inc. A repo-level licence badge cannot
express that. Read the payload, note the carve-out paths, and record the copyright
holder alongside the licence so a change of holder between passes is visible.

Repo *location* needs the same care: `apereo/opencast` is a **404**, and the live
repository is `opencast/opencast` (ECL-2.0). An org-renamed project will fail a
reachability probe while the project itself is perfectly healthy — re-probe the
name before recording a gap. The converse also happens: `planejaia/OpenMAIC-Brasil`
is a confident search result for a repository that genuinely does not exist —
**re-probed on 2026-10-06 it still 404s on all four** candidate branches (`main`,
`master`, `develop`, `v1.0.0`).

**Two rules added in the fourth pass of 2026-10-06, because that last example was
read wrongly for three passes.**

1. **A 404 on a suffixed name obliges you to query the base name before you record
   a gap.** `OpenMAIC-Brasil` is absent; **`OpenMAIC` is not.** The upstream is
   [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — **MIT, 40.0k★,
   Tsinghua University** — now the largest permissive asset in this KB and listed
   on the core shelf above. This KB carried the absence as evidence through three
   passes while a forty-thousand-star implementation of the same idea sat one query
   away.
2. **A repository name is not a provenance claim.** `-Brasil`, `-India`, `-LATAM`
   are strings an author typed. Attribute region from the **owner account, the
   commit history or the README** — never from the slug. The no-LATAM-origin gap
   was partly argued from this filename; it has since been re-established on
   channels that do not depend on one, including a Spanish/Portuguese-language
   search (see `agents/top.md`).

**And sweep the organisation behind any interesting repository.** Topic pages rank
by stars, so they structurally hide small orgs: the `AI-for-Education` sweep in the
same pass returned six repositories, five MIT, that no topic page had ever shown
this KB — and they are the only Africa-placed code it holds.

## Added in the tenth pass of 2026-10-06 — the interoperability tier, and the sync engine under the offline platform

Two shelves this pass, both payload-verified, both arriving from a demand signal
rather than from a search for interesting code.

**All licences below were read from the repository's own payload** via
`raw.githubusercontent.com`, probed across **10 filenames × 2 branches**
(`LICENCE`/`LICENSE`/`licence`/`license`/`COPYING`, `.md` and `.txt` variants, on
`main` and `master`). The probe was validated against 6 known-payload controls
first; **6 of 6 resolved.** Star counts read from the rendered repository page the
same day.

### The interoperability tier — because 39% of district RFPs score it

The ninth pass found the procurement number: **39% of districts score
interoperability in their RFP rubrics** (CoSN, Tier 2). That makes the integration
layer a **scored deliverable**, not plumbing — and this is the entire permissive
shelf for it, split by runtime.

| Repo | License (read from payload) | ★ (2026-10-06) | Runtime | What it is |
|---|---|---|---|---|
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 (`master/LICENSE`) | 373 | Node / TypeScript | Turns an application into a fully integratable **LTI 1.3 tool provider**. The highest-starred genuine LTI project, and the default when the AI layer is a Node service. |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | Apache-2.0 (`master/LICENSE.md`, 11,343 B) | — | PHP | LTI 1.3 library published by **the standards body itself**. The reference implementation; the natural pairing when the LMS is Moodle. | 🔵 **Row re-pointed, pass 24.** This was `1EdTech/lti-1-3-php-library`, whose head commit is **2020-06-03 — 2,317 d**. The live copy of the *same* library (byte-identical payload) is the `packbackbooks` original, head commit **2026-09-23 (14 d)**. ⚠️ The 124★ figure belonged to the 1EdTech copy and is not transferable, so it is withdrawn rather than moved — no ★ was readable this pass (`github.com` and `api.github.com` are 403 here). |
| [Unicon/tool13demo](https://github.com/Unicon/tool13demo) | Apache-2.0 (`master/LICENSE`) | 27 | Java / Spring Boot | LTI 1.3 tool in Spring Boot, from a long-standing higher-ed systems integrator. **The JVM entry point** — which is the stack most enterprise education clients already run. |
| [oxctl/spring-security-lti13](https://github.com/oxctl/spring-security-lti13) | Apache-2.0 (`master/LICENSE.txt`) | 25 | Java / Spring Security | LTI 1.3 for Spring Security, built on its OAuth2 support. Use this one when the client already has a Spring Security estate and wants LTI inside it rather than beside it. |
| [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET) | **MIT** (`master/LICENSE`) | 6 (8 forks) | .NET | OneRoster 1.1 and 1.2 client. OAuth2 for 1.2, consumer credentials for 1.1. **Rostering calls only — gradebook is not implemented**, which is a scope limit to check against the rubric before you promise it. |

**Three warnings on this shelf.**

1. **Pin the right OneRoster.NET.** [jdolny/OneRoster.NET](https://github.com/jdolny/OneRoster.NET)
   is **also MIT** (`master/LICENSE`) and serves a byte-identical `README.md`
   (md5 `110b2e3439d86b6055821de382d90d61`, 2,048 bytes) and byte-identical
   licence text. **Both licences name `theopenem` as holder.** One asset, two
   addresses; the fork direction is **not established** in this environment
   (`github.com` → 403 to `curl`, no fork banner in the rendered page). Pin
   `theopenem`, whose owner matches the copyright line.
2. **"Caliper" is a homonym and it will waste a sweep.** `OneRoster OR Caliper OR
   "LTI 1.3" license:apache-2.0` returns **184 repositories**, led by
   `google/caliper` (818★, deprecated Java micro-benchmarking) and
   `hyperledger-caliper/caliper` (708★, blockchain benchmarking). Four of the top
   eight have nothing to do with 1EdTech Caliper Analytics. **The result count is
   not the ecosystem size.**
3. 🔵 **CORRECTED, twenty-fourth pass of 2026-10-07. This said "there is no Python LTI 1.3 library
   on this shelf". It is false, and there is now a live one.** Node, PHP, Java and .NET are
   covered, and so is Python: [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) —
   **MIT** (payload 1,098 B, © The Regents of the University of Michigan), head commit
   **2026-10-05 (2 d)**, published to PyPI as [`django-lti`](https://pypi.org/project/django-lti/)
   **v0.10.1 on 2026-08-07 (61 d)**. It is **Django**-coupled. For a JupyterHub tool,
   [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (BSD-3-Clause,
   98 d) implements LTI 1.3 **and** 1.1 and is tested against Open edX, Canvas and Moodle.
   ⚠️ **What is genuinely absent is a live *framework-agnostic* Python implementation:** the only
   framework-neutral one, `dmitry-viskov/pylti1.3`, is **1,416 days cold on the commit channel and
   1,417 on the release channel**. 🔴 And the best-maintained Python LTI 1.3 implementation of all,
   [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) (committed and
   released 6 d ago), is **AGPL-3.0** — right inside Open edX, unusable as reusable IP. So the
   contribution opening narrows from "a library" to "a framework-neutral library", and the
   adapter-in-another-runtime workaround below is **no longer required** when the AI tier is
   Django. 🔵 **NARROWED, twenty-fifth pass of 2026-10-07 — "none" is now "one alpha".** [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) (MIT) **vendors `PyLTI1p3`, rebranded** — its README says so — and publishes it as [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 (103 d), one release ever**; head commit **63 d**; **0★**; `Development Status :: 3 - Alpha` with the FastAPI adapter and token minting **unbuilt**; and its `LICENSE` holder is **`Dmitry Viskov`, not its own authors**. **Not "no option", and not a safe dependency either.** Full row in `repos/foundations.md`.

### The Learning Equality substrate — the sync engine, not just the app

This KB has recommended offline-first delivery for three passes while recording
the *application* (Kolibri) and not the machinery under it. The organisation holds
**238 repositories**. Probed this pass:

| Repo | License (read from payload) | ★ (2026-10-06) | What it is |
|---|---|---|---|
| [learningequality/morango](https://github.com/learningequality/morango) | **MIT** (`master/LICENSE`) | 15 (23 forks) | **Pure-Python peer-to-peer database replication engine for Django.** Marks chosen application models syncable; **certificate-based authentication** protecting data privacy and integrity; change-tracking and data-partitioning constructs designed for low-bandwidth links; works on **SQLite and PostgreSQL**. Branch `release-v0.9.x`. Built for Kolibri, **usable independently** — this is the component that makes an offline-first architecture real rather than aspirational. |
| [learningequality/le-utils](https://github.com/learningequality/le-utils) | **MIT** (`main/LICENSE.txt`) | not read this pass | Constants and utilities shared across Kolibri, Ricecooker and Studio. The shared vocabulary layer; required by anything that generates Kolibri channels. |

**And the two that came back ungranted, inside that same organisation:**

| Repo | License probe result | Consequence |
|---|---|---|
| [learningequality/kolibri-design-system](https://github.com/learningequality/kolibri-design-system) | **no payload** (20 URLs) | Vue design system. Repository exists (`main/README.md` resolves). **Do not ship client UI from it** on the assumption that the org is MIT. |
| [learningequality/kolibri-server](https://github.com/learningequality/kolibri-server) | **no payload** (20 URLs) | Performance and caching access layer for Kolibri with multi-core support. **The repository exists** — its README is `main/README.rst`, not `README.md`. **No licence payload under any of 20 URLs.** Treat as unlicensed until a payload is read. |

**Two of four new probes in the MIT-friendliest organisation on these shelves came
back ungranted.** An organisation's licence posture is not inherited by its
repositories. "They're the Kolibri people" is not a licence.

**A scope concern raised and refuted.** `learningequality/studio`
([repo](https://github.com/learningequality/studio), already on these shelves)
declares `Copyright (c) 2021 Foundation for Learning Equality (internal apps)`.
A parenthetical qualifier inside a copyright line is exactly the shape this KB
treats as a possible narrowed grant. **Full text read this pass: the permission
body is standard, unmodified MIT with no field-of-use restriction.** The
parenthetical annotates the holder, not the grant. **Full MIT** — recorded so the
next pass does not re-litigate it.

### Why these two shelves belong on the same page

Morango answers *how the data gets there* when connectivity is intermittent. The
LTI/OneRoster tier answers *how it gets into the systems the client already runs*,
against a rubric that scores exactly that. Together they are the two ends of a
delivery that an RFP can actually score — and both ends are permissive, which is
the whole reason this file exists.

## Added in the eleventh pass of 2026-10-06 — the evaluation layer, and the Python protocol layer

Licences read from each repository's own payload on `raw.githubusercontent.com` on
2026-10-06; metadata (stars, forks, `default_branch`, `fork`, `pushed_at`) from the
GitHub REST search API, reachable this pass through the session's GitHub MCP server.

**All four rows are reinstatements of addresses this repository's own reset dropped
earlier the same day** — they are in `archive/2026-10-06-pre-reset/`. See
`repos/trending.md` for the 172-address audit.

### The evaluation layer — the one infrastructure tier this KB had been describing as missing

| Repo | Licence (read from payload) | ★ (2026-10-06) | Forks | Why it is foundational |
|---|---|---|---|---|
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | **MIT** (`main/LICENSE`) | **2,945** | 779 | **Inspect**, from the **UK AI Security Institute**. A general LLM-evaluation framework: datasets → solvers → scorers, with model-graded evals, tool use and multi-turn dialog built in, and third-party Python packages able to add scoring and elicitation techniques. **This is the harness.** An education engagement supplies the dataset and the rubric; it should not supply the runner, the logging, the sandboxing or the scoring plumbing. Pushed on the day of this pass. |
| [aiverify-foundation/moonshot](https://github.com/aiverify-foundation/moonshot) | **Apache-2.0** (`main/LICENSE.md`) | 355 | 72 | **Moonshot**, from the **AI Verify Foundation** (Singapore IMDA's AI-testing community). Benchmarking **and red-teaming** of any LLM application in one modular tool. The red-team half has no permissive equivalent in this KB, and for an education deployment — where the adversary is a bored fifteen-year-old with unlimited attempts — it is not optional. Pushed on the day of this pass. |

**Why both, rather than one.** Inspect measures whether the system is *right*;
Moonshot measures whether it can be made to *misbehave*. Education buyers in every
region this KB tracks now ask for both, and the two licences (MIT and Apache-2.0) are
compatible with each other and with a commercial deliverable. **Neither ships any
education content** — which is exactly why they are in `foundations.md` and the
benchmarks are not.

### The protocol layer — Python

| Repo | Licence (read from payload) | ★ | Branch | Why it is foundational |
|---|---|---|---|---|
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** (`master/LICENSE`, 1,070 B) | **138** | `master` | `PyLTI1p3` — **LTI 1.3 Advantage** tool implementation with Django and Flask adapters. Most AI tutoring code in this KB is Python, and LTI 1.3 is how it reaches a learner inside an institution's LMS. ⚠️ **Last push 2024-08-18**: treat as a stable protocol library, pin the version, and budget for maintaining your own fork if the spec moves. |
| [Pearson-Advance/openedx-lti-tool-plugin](https://github.com/Pearson-Advance/openedx-lti-tool-plugin) | **Apache-2.0** (`main/LICENSE`) | 5 | `main` | Makes an **Open edX** instance act as an LTI 1.3 *tool*, so an existing Open edX estate can be consumed by another institution's LMS rather than replaced. Pushed 2026-09-11. |

### A probe-set correction that belongs in this file

Every licence in `foundations.md` is read from a payload URL, and a payload URL needs
a branch. The tenth pass probed `main` and `master`. **Read `default_branch` from the
API instead**: this pass found a 2,320★ platform on `dev` (`learnhouse`), a 718★
platform on `2.12` (`portabilis/i-educar`) and one repository on
`deployment/playstore`. On a `main`+`master` probe all three read as **ungranted**,
and two of them are merely **copyleft** — a delivery constraint, not an absence.

## Added in the twelfth pass of 2026-10-06 — the xAPI/LRS tier, the Ed-Fi stack, and the Apache-2.0 seam inside an AGPL platform

Every branch below came from `git ls-remote --symref … HEAD` and every licence from the
`raw.githubusercontent.com` payload on that branch, on 2026-10-06. No licence here was
taken from a sidebar, a badge or an organisation-level assumption — the
`aiverify-foundation` rows are the reason why: two repositories in that organisation are
Apache-2.0 and a third, in the same org, carries no licence at all.

### The row that changes platform strategy — Open edX's plugin SDK is Apache-2.0

| Repo | Licence (payload) | ★ | Branch | Why it is foundational |
|---|---|---|---|---|
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** (`master/`**`LICENSE.TXT`**) | **470** | `master` | The **XBlock SDK** — the component and plugin API every Open edX course component is written against. Python. |

**This matters out of proportion to the row.** Open edX's platform core
(`openedx/edx-platform`) is **AGPL-3.0**, and this KB has correctly priced the platform
as copyleft since its first pass. But the surface a studio actually writes on — a
client-specific interactive component, an AI tutor delivered inside a course, a
proctoring or analytics side-car — is an **XBlock**, and the XBlock SDK is
**Apache-2.0**. A component built against it is **your** component: Globant can build,
keep and redistribute it without inheriting the platform's AGPL obligations, provided it
stays a plugin and is not linked into the platform tree. The LATAM `TutorIA`
specification already on this KB's agent shelf specifies exactly this shape — *"delivered
as an Open edX XBlock/plugin"* — and this row is the licence evidence that the shape is
sound.

⚠️ **The boundary is the deliverable, not the repository.** AGPL-3.0 reaches anything
that becomes part of the platform process in a way that creates a derivative work; it
does not reach a separately licensed plugin consumed through a published plugin API. Get
the packaging reviewed before you promise a client a proprietary component — the
distinction is the whole engagement, and it is a legal review, not a licence-file read.

*Found at `LICENSE.TXT` — uppercase extension. A nine-name lowercase probe reports this
repository as ungranted; see the 13th failure mode in `agents/top.md`.*

### The xAPI / LRS tier — the learning-analytics half, recovered

The eleventh pass declared the learning-analytics side of the interoperability tier
behind a membership, on the evidence of Caliper. **That is true of Caliper and false of
xAPI.** xAPI's tooling is permissive and alive:

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [adlnet/lrs-conformance-test-suite](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** (`master/LICENSE`) | **77** (52 forks) | `master` | **The conformance instrument.** Node.js suite that tests an LRS against the **MUST** requirements of the xAPI specification. From **ADL** (Advanced Distributed Learning, the US Department of Defense initiative that authored xAPI). This is how you *prove* an analytics deliverable conforms rather than asserting it — and in a procurement where interoperability is a scored line item (trend 28), a conformance run is the evidence. |
| [adlnet/xapi-profiles](https://github.com/adlnet/xapi-profiles) | **Apache-2.0** (`master/LICENSE`) | **60** (33 forks) | `master` | The **xAPI Profiles specification** — structure, communication and processing — plus context, library and ontology files. ADL also runs a public profile index at `xapi.vocab.pub`. The vocabulary layer: what a statement *means*, not just how it is transported. |
| [yetanalytics/xapipe](https://github.com/yetanalytics/xapipe) | **Apache-2.0** (`main/LICENSE`) | 17 (9 forks) | `main` | **LRSPipe** — xAPI statement forwarding and middleware, governed directly by xAPI Profiles. Clojure. ⚠️ **The product name is not the repository name**: `yetanalytics/lrspipe` is a 404 and this KB recorded that false negative twice. Pin the address, not the brand. |
| [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | An LRS implementation. The store at the end of the pipe. |

**What this adds up to:** a permissive xAPI chain exists end to end — **profile**
(vocabulary) → **pipe** (transport and transformation) → **LRS** (store) →
**conformance suite** (proof). All four are MIT or Apache-2.0. An analytics deliverable
can be built, kept and redistributed by Globant on this chain. **Caliper cannot be, and
xAPI can** — and the two standards are not interchangeable, so this is a design decision
to make at proposal time, with the licence as one of the inputs.

### The Apereo learning-analytics tier — permissive, under a licence the filter misses, and dormant

| Repo | Licence (payload) | ★ | Branch | State |
|---|---|---|---|---|
| [Apereo-Learning-Analytics-Initiative/OpenLRS](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS) | **ECL-2.0** (`master/LICENSE`) | 47 (38 forks) | `master` | 🔴 **Archived by the owner on 2019-01-31, read-only.** Superseded by OpenLRW; the README says all new development moved there. |
| [Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | **ECL-2.0** (`master/LICENSE`) | not read this pass | `master` | Dormant. |
| [Apereo-Learning-Analytics-Initiative/OpenDashboard-api](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) | **ECL-2.0** (`master/LICENSE`) | not read this pass | `master` | Dormant. |

🆕 **ECL-2.0 is the Educational Community License 2.0, and it belongs in this KB's
permissive set.** It is **OSI-approved** and it is **Apache-2.0 with one modification**:
the patent grant is narrowed so that a contributing university licenses patents only for
the contributed work, not across its whole portfolio — written precisely so that
universities could contribute to open source without their technology-transfer offices
blocking it. For redistribution and commercial use it behaves like Apache-2.0.

**This is trend 15 — "permissive is a bigger set than MIT, Apache, BSD" — with the
education sector's own licence as the example.** A `license:mit OR license:apache-2.0`
filter rejects the entire Apereo estate, and Apereo is the consortium behind Sakai and
much of higher education's shared infrastructure. **Add `ECL-2.0` to the permissive
allow-list.**

⚠️ **And then do not adopt these three anyway.** The licence is fine; the code has been
read-only since January 2019. They are a **reference architecture and a vocabulary
source**, and the live permissive alternative is the ADL/Yet Analytics xAPI chain above.
The useful lesson is the licence, not the repositories.

### The Ed-Fi stack — Apache-2.0, and the US K-12 data standard

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** (`v6.2.0/LICENSE`) | 46 (13 forks) | 🆕 **`v6.2.0`** | The **Ed-Fi Data Standard** — the schema that enables interoperability among US K-12 education data systems. Latest release v6.2.0, which is also the default branch. |
| [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | **OneRoster** over Ed-Fi — rostering interoperability, the 1EdTech standard that *did* stay open. |
| [Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | Integration with **Clever**, the rostering provider most US districts actually run. The bridge between the standard and the installed base. |

**Why this is the North America procurement asset.** US K-12 procurement increasingly
scores interoperability directly (trend 26, trend 28), and Ed-Fi is the standard those
rubrics name. The schema, the OneRoster bridge and the Clever integration are all
**Apache-2.0**. ⚠️ **The MCP side-car is gone**: `Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP` is
recorded in this repository's archive and no longer resolves. Agent access to Ed-Fi over
MCP is a **build**, and it is a well-shaped, small one — the schema is published and
permissive.

*The default branch here is `v6.2.0`. This is the cleanest example in the KB of why the
branch must be read rather than guessed: the Apache-2.0 licence of the US K-12 data
standard is invisible to a `main`+`master` probe.*

### The interoperability tier — Python and Java LTI 1.3, measured exhaustively

The tenth pass declared *"no Python LTI 1.3 library exists on the permissive shelf"*;
the eleventh pass refuted it from this repository's own archive. This pass **measured the
whole tier** with the MCP search API — `lti 1.3 advantage language:Python` →
**`total_count: 4`**, which is the complete set, not a page of it:

| Repo | Licence (payload) | ★ | Branch | Verdict |
|---|---|---|---|---|
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** (1,070 B) | **138** (83 forks) | `master` | **The only viable one.** Django and Flask adapters. ⚠️ **51 open issues**, last push 2024-08-18. |
| [blackboard/BBDN-lti-1p3-tool-example](https://github.com/blackboard/BBDN-lti-1p3-tool-example) | **Apache-2.0** (`main/LICENSE`) | 1 | `main` | 🆕 **Blackboard's own** Python/Flask LTI 1.3 example with AWS deployment. A vendor-authored reference — useful for reading how a major LMS expects a tool to behave. Last updated 2022. |
| [glenn-watt/lti-1p3-reference-tool](https://github.com/glenn-watt/lti-1p3-reference-tool) | **MIT** (`main/LICENSE`) | 0 | `main` | 🆕 Flask reference tool implementing **OIDC, JWKS validation, AGS, NRPS and Deep Linking from first principles**. 0★ and three months old, so it is **code to read**, not a dependency — but it is the only one that covers all four LTI Advantage services explicitly. |
| [CNIT-Organization/ltitoolkit](https://github.com/CNIT-Organization/ltitoolkit) | **MIT** (`main/LICENSE`) — ⚠️ **the holder is `Dmitry Viskov`, not this project** | 0 | `main` | 🔴 **REWRITTEN, twenty-fifth pass of 2026-10-07 — this row said "PyPI-published" and that is wrong under this name.** `pypi.org/pypi/ltitoolkit` is **404**; the package is published as **[`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) 0.1.0, uploaded 2026-06-26 (103 d), one release ever**, and the repo's own README says *"Published via Git (no PyPI required)"*. **And the row omitted the only thing about it that matters: its `src/ltitoolkit/core/` is, in its README's words, the "vendored LTI 1.3 engine (PyLTI1p3, rebranded)".** See the correction block below. |

🔴 **CORRECTED, twenty-fifth pass of 2026-10-07 — two figures in the table above were
stale and the row that resolves the tier was mis-described.**

⚠️ *"has not been pushed since August 2024"* is wrong: `dmitry-viskov/pylti1.3`'s head commit
is **2022-11-21**, measured over `git` by pass 23 and re-measured this pass, and its last PyPI
release, `pylti1p3` **2.0.0**, is **2022-11-20**. Both channels agree and both are **1,416
days**. Pass 24 published the right figure in `agents/trending.md` and this table kept the
wrong one — the third reproduction of the propagation failure recorded in `intel/market.md`.

🟢 **And the KB's own answer to its most-repeated supply gap was already sitting in the last
row of this table.** Pass 24 spent its headline establishing that *"the only framework-neutral
Python LTI 1.3 implementation (`pylti1.3`) is abandoned on both channels"*. Measured this pass
by the **licence-holder channel** — `CNIT-Organization/ltitoolkit` ships a `LICENSE` whose
holder is `Dmitry Viskov`, which is the fork signal trend 56 defines — and then confirmed by
opening its README:

> `src/ltitoolkit/core/   # vendored LTI 1.3 engine (PyLTI1p3, rebranded) — internal`

**So the framework-agnostic path is not dead; it is early.** The honest shelf:

| | `ff-ltitoolkit` (`CNIT-Organization/ltitoolkit`) |
|---|---|
| licence payload | 🟢 MIT (`main/LICENSE`) |
| ⚠️ licence **holder** | 🔴 `Dmitry Viskov` — **the vendored engine's holder, carried over.** The repo publishes **no grant naming its own authors** for the new code |
| PyPI | 🟢 `ff-ltitoolkit` **0.1.0**, 2026-06-26, **103 d** — the only release |
| head commit | ⚠️ **2026-08-05, 63 d** — alive, but two months without a commit on a project whose README says three of its five subsystems *"are being built"* |
| scope today | 🟢 OIDC/JWT launch, AGS, NRPS, Deep Linking, Dynamic Registration declared; 🔴 **FastAPI adapter, Dynamic Registration and token minting are Phase 2–5, unbuilt** |
| declared status | 🔴 *"early development (v0.1.0)"*, `Development Status :: 3 - Alpha` |

🔵 **The sentence that replaces trend 28's, narrower and finally true in three directions:**
the **Django** path is alive (`academic-innovation/django-lti`, MIT, 2 d); the **JupyterHub**
path is alive (`jupyterhub/ltiauthenticator`, BSD-3-Clause, 98 d); and the **framework-agnostic**
path is a **single 0★ alpha that vendors the abandoned library rather than replacing it**, with
one release and no grant of its own. **Read as a procurement answer that is better than "there
is none" and much weaker than "there is one."** If an engagement's LMS integration is on the
critical path and the tool is not a Django app, budget for maintaining the vendored engine
yourself — the alpha has already done the vendoring, which is the work, and has not yet done
the adapters.

⚠️ **One figure in the table above is left as published and should not be re-used:** the
`total_count: 4` came from the MCP search API, which this environment no longer reaches.
`ff-ltitoolkit` is reachable only through PyPI and `git`, and `pypi.org/pypi/ltitoolkit` is a
404 — **a tier census run by repository search would have missed the package name entirely.**

**The Java side is healthier, and it is EMEA-placed:**

| Repo | Licence (payload) | ★ | Branch | Verdict |
|---|---|---|---|---|
| [UOC/java-lti-1.3-provider-example](https://github.com/UOC/java-lti-1.3-provider-example) | **MIT** (`master/LICENSE`) | 8 (12 forks) | `master` | **EMEA / Spain** — a working LTI Advantage tool webapp built on the LTI libraries of the **Universitat Oberta de Catalunya**, a large European distance-learning university. The Java counterpart to `pylti1.3`, carrying a European institution's own production lineage. |

### The assessment-standards tier — QTI, and an ISC licence from a commercial vendor

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [pie-framework/pie-qti](https://github.com/pie-framework/pie-qti) | 🆕 **ISC** (`master/LICENSE`, © 2026 **Renaissance Learning**) | 4 (1 fork) | `master` | **QTI player for 2.1, 2.2 and 3.0**, plus bidirectional QTI ↔ PIE transforms with a CLI for batch conversion. Ships an item player and a multi-item assessment player. TypeScript. |
| [Citolab/qti-convert](https://github.com/Citolab/qti-convert) | **GPL-3.0** (`main/LICENSE`) | not read this pass | `main` | QTI conversion tooling from **Cito** (the Dutch national assessment institute). Real and maintained — but GPL-3.0, so a conversion step built on it is a copyleft deliverable. |

🆕 **ISC belongs on the permissive allow-list too.** It is OSI-approved and functionally
equivalent to MIT — a two-clause permission grant with no added conditions — just shorter.
A `license:mit OR license:apache-2.0 OR license:bsd` filter misses it.

**And note who holds the copyright: Renaissance Learning**, a commercial assessment
vendor, publishing a QTI player under ISC. Trend 7 has called assessment "the regulated
frontier and the tooling gap" for eleven passes. The gap is narrower than that on the
**standards-conformance** side: a permissive QTI player exists, at 4★, from a vendor
with a real assessment business. It is still wide on **AI-generated grading**, where
`license:apache-2.0` + automated rubric grading measures **`total_count: 0`** this pass
and the only permissive answer in this KB remains `Selleo/mentingo` (MIT).

### Classroom-discourse and research infrastructure

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [stanfordnlp/edu-convokit](https://github.com/stanfordnlp/edu-convokit) | **MIT** (`main/LICENSE`) | 117 (16 forks) | `main` | Stanford NLP: anonymise → annotate → analyse classroom talk. Full entry in `agents/top.md`. |
| [EduNLP/EduCoder](https://github.com/EduNLP/EduCoder) | **MIT** (`main/LICENSE`) | 3 | `main` | Human-vs-LLM transcript annotation workspace. Full entry in `agents/top.md`. |
| [jupyterhub/jupyterhub-deploy-teaching](https://github.com/jupyterhub/jupyterhub-deploy-teaching) | **BSD** (`master/LICENSE`) | not read this pass | `master` | 🆕 **Absent from every earlier pass of this KB**, live or archived, except one archive mention. Reference deployment of **JupyterHub for a teaching environment** — the standard way CS and data-science courses give every student a server-side notebook. BSD. The infrastructure layer under any coding-course engagement. |
| [aiverify-foundation/aiverify](https://github.com/aiverify-foundation/aiverify) | **Apache-2.0** (`main/LICENSE`) | 98 (32 forks) | `main` | **APAC / Singapore** — AI governance *testing framework* from the **AI Verify Foundation** under **IMDA**, validating AI systems against internationally recognised principles through standardised tests. The compliance-evidence instrument for an APAC deployment, built by the regulator's own foundation. |
| [aiverify-foundation/aiverify-developer-tools](https://github.com/aiverify-foundation/aiverify-developer-tools) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | Plugin and test-widget development kit for AI Verify. How you add an **education-specific** test to a government-recognised harness. |
| [aiverify-foundation/moonshot-data](https://github.com/aiverify-foundation/moonshot-data) | **Apache-2.0** (`main/LICENSE.md`) | not read this pass | `main` | Test assets, datasets, metrics and attack modules for Moonshot (the red-teaming/benchmark harness already on this shelf). |
| `aiverify-foundation/LLM-Evals-Catalogue` | 🔴 **ungranted** | — | `main` | **No licence file**, under 30+ name variants on the real default branch. A catalogue of LLM evaluations — the index, not the code. **Treat as reading material, cite it, do not vendor it.** Three repos in one government foundation's organisation: two Apache-2.0, one ungranted. |

### One correction to this KB, with the payload as evidence

The 123rd-pass note in `repos/trending.md` records:

> *"Discrepancia registrada sin normalizar: el `LICENSE` de `edrys` mide 16.724 B y la
> AGPL íntegra mide ~34–35 KB en este corpus — es AGPL ABREVIADA."*

🔴 **`edrys-org/edrys` is `MPL-2.0`, not an abbreviated AGPL.** Read this pass from
`main/LICENSE` (16,725 B): the first line is **`Mozilla Public License Version 2.0`**,
and the full MPL-2.0 text is ~16.7 KB — the size is not a truncated AGPL, it is a
complete MPL. The only occurrence of "Affero" in the file is inside **MPL §1.12's
secondary-licence definition**, which names the LGPL and AGPL as compatible licences.
That boilerplate is what a substring search found.

**This changes the delivery constraint, not just the label.** MPL-2.0 is **file-level
weak copyleft**: modified MPL files must stay MPL and be published, but the work can be
combined with proprietary code in a larger program without that program becoming MPL.
AGPL would have added a network-use obligation that MPL has none of. `edrys` — a
live-classroom platform — is therefore **usable in a mixed-licence deliverable** with
per-file discipline on the files you touch. It was priced as unusable.

**The method lesson is the general one:** a size comparison identifies a *discrepancy*,
and only the first line of the payload identifies a *licence*. Size told pass 123 to look
again, which was right; it then answered the question it had only raised.

## Added in the thirteenth pass of 2026-10-06

One row, and it is on this shelf rather than the education shelf for a reason.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [bonafe/inteligencia-aberta](https://github.com/bonafe/inteligencia-aberta) | **MIT** (`LICENSE`) | reference architecture | **Not education software.** A Brazilian civic-analysis agent platform (Bonafé · Américo, 2★, Python) whose *stack* is the one this KB keeps assembling by hand for a sovereign deployment: **FastAPI + LangGraph + PostgreSQL + Qdrant, in Docker, multi-tenant, deployable locally and federating across machines**. Read it as a **worked reference for the LATAM sovereign pattern**, not as a component to ship. Its design goals — end-to-end source traceability, user control over what is shared, voice and natural-language access for low-literacy users — are the same requirements an education deployment under LATAM constraints carries, written out by someone who shipped them. |

### Why a 2★ repository is worth a row

Because this shelf's job is to answer *"what do we build on"*, and the scarce thing in a
sovereign education build is not a component — every component here is permissive and
available — it is a **worked wiring of them that someone has already debugged**. This KB
has four patterns (P4, P5, P26, P32) that specify a LATAM or data-residency stack
component by component. `inteligencia-aberta` is an independent implementation of
substantially that stack, by Brazilian authors, under MIT, with the traceability
requirement treated as a first-class design goal rather than an afterthought.

⚠️ **The star count is the correct signal to ignore here, and the fork count is the one to
watch.** It has **2 stars and 0 forks** — nobody has deployed it. Use it as a design
reference and a code read; do not present it to a client as a maintained dependency.

### What this pass did not add, and why

🔴 **No new serving, orchestration or retrieval layer was found.** The mandatory
infrastructure query (`open source platform education ERP CRM MIT Apache`) returned
**OpenEduCat, RosarioSIS, openSIS, Gibbon and Fedena** — *five returned, five already
inventoried on the SIS/ERP shelf in `verticals/solutions.md`*. That is the **fourteenth
consecutive pass** in which the generalist infrastructure query has returned zero new
rows, and it is now safe to say what that means: **the foundational layer for an education
build is saturated and stable.** The scarcity has moved entirely to the education-specific
layer above it, which is where the last several passes have correctly been spending their
probes.

🔴 **The non-GitHub forge channel could not be opened.** `codeberg.org`, `gitee.com` and
the European Commission's Joinup/OSOR catalogue are all **unreachable from this
environment** (403 at the egress proxy). Every licence fact on this shelf rests on
`raw.githubusercontent.com`, which is the only code-hosting payload this environment can
read. Two named Codeberg education projects were surfaced and **deliberately not shelved**,
because they could not be payload-verified. Full measurement in `agents/trending.md`,
Finding 4.

## Added in the fourteenth pass of 2026-10-06 — the sandbox layer, and the index that is not a shelf

One infrastructure row, and it is the highest-starred find of the whole pass. It arrived
through the platform-name channel (`agents/trending.md`, fourteenth pass) as a by-product:
searching for education platform integrations surfaced the layer underneath the one thing
education software does that no other industry's software does — **run a student's code**.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [taybenlor/runno](https://github.com/taybenlor/runno) | **MIT** (`LICENSE`, 1,106 B; © Benjamin Taylor) | code sandbox | **773★.** Runs code in many languages inside a **WebAssembly/WASI sandbox** — in the browser with no server, or in Node. Four published packages, all **MIT on npm**: `@runno/runtime` 0.10.0 (web components for runnable examples), `@runno/sandbox` 0.10.2 (secure sandbox for Node and other JS runtimes), `@runno/wasi` 0.10.0 (isomorphic WASI runner) and 🆕 **`@runno/mcp` 0.10.6 — the sandbox exposed as an MCP server**. |

### Why this is a foundations row and not a curiosity

Every CS-education pattern in this KB has had the same unsolved component: **where does the
student's code run?** The existing answers on this shelf are JupyterHub (a multi-user server
per cohort) and OpenHands (a coding agent with its own sandbox). Both are servers you operate.

Runno moves execution **into the learner's browser**, which changes three things an education
engagement is costed and audited on:

- **Data residency becomes trivial for the execution step.** Student code never reaches a
  server, so there is no execution-side transfer to document in an EMEA deployment. The
  sovereignty argument this KB makes with Ollama for inference, Runno makes for execution.
- **Per-seat cost goes to zero and scales with the cohort's own devices.** No container per
  student, no idle notebook servers — the LATAM and offline-first cost constraints in P5
  apply to execution too, and this is the component that answers them.
- 🆕 **`@runno/mcp` makes the sandbox agent-callable**, which is the piece that was missing:
  a tutor agent can now *execute* a learner's submission and reason about the actual output
  rather than predicting it. Pair it with the auto-grading assets in `agents/top.md`
  (fourteenth pass) and the grading loop has a real execution step under a permissive licence.

⚠️ **Two limits to state before it enters a proposal.** WASI sandboxing covers languages
with a WASI target — check the language a client's curriculum actually teaches against the
published package list rather than assuming coverage. And a browser sandbox is **not** an
anti-cheat boundary: it protects the host from the code, not the assessment from the student.
For proctored assessment the execution still belongs server-side.

### The MCP Registry — an index this KB now uses, and what it is not

`registry.modelcontextprotocol.io` is reachable here and was measured first-hand this pass
(method, traps and counts in `repos/trending.md`, fourteenth pass). It belongs on this page
only as a **channel**, never as a dependency:

- **11,505 unique servers** across 31,300 version rows — a record is not a server, and the
  figure is a **floor** because the page loop ended early.
- **102 education-vocabulary servers, of which 71 (70%) ship no source repository.** It is a
  catalogue of hosted endpoints with open-source entries mixed in, not a source shelf.
- 🔴 Its `?q=` parameter returns **HTTP 200 and the unfiltered page** — a silent no-op. Do
  not quote a count from it.
- 🔴 One listed server's repository **no longer exists**. A registry entry is not an
  existence proof; `ls-remote` still is.

**The rule for this page:** the registry is a good place to *find* candidates and a
disqualifying place to *source* them. Nothing enters this shelf from a registry listing
without an `ls-remote` resolution and a licence payload on its real default branch.

## Added in the fifteenth pass of 2026-10-06 — the SIS/MIS client layer, and why it belongs in *this* file

The assets found this pass are not education products and they are not agents. They are the
**client libraries that speak a student information system's protocol** — the layer an
education agent stands on when the engagement is administrative rather than instructional.
Full rows, stars and country placement in `agents/top.md` (fifteenth pass). This file records
what they are *for*, and the two things that decide whether you may use them.

Licences read from each repository's own payload on 2026-10-06; default branches confirmed
with `ls-remote --symref`.

### The layer, by protocol family

| Repo | Licence (payload) | Language | Speaks to |
|---|---|---|---|
| [`bain3/pronotepy`](https://github.com/bain3/pronotepy) | **MIT** | Python | PRONOTE (FR) |
| [`python-webuntis/python-webuntis`](https://github.com/python-webuntis/python-webuntis) | **BSD-2-Clause** | Python | WebUntis (DE/AT) |
| [`aydenp/PowerSchool-API`](https://github.com/aydenp/PowerSchool-API) | **MIT** | Node.js | PowerSchool (US) |
| [`dougpenny/PyPowerSchool`](https://github.com/dougpenny/PyPowerSchool) | **MIT** | Python | PowerSchool (US) |
| [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | **MIT** | PHP | PowerSchool (US) |
| [`magister-api/magister`](https://github.com/magister-api/magister) | **MIT** | PHP | Magister 6 (NL) |
| [`elisaado/somtoday.js`](https://github.com/elisaado/somtoday.js) | **MIT** | TypeScript | SOMtoday (NL) |
| [`ivmelo/suap-api-php`](https://github.com/ivmelo/suap-api-php) | **MIT** | PHP | SUAP (BR) |
| [`Projeto-SIAC/suap-wrapper`](https://github.com/Projeto-SIAC/suap-wrapper) | **MIT** | Node.js | SUAP (BR) |
| [`PucaVaz/sigaa-tools`](https://github.com/PucaVaz/sigaa-tools) | **MIT** | Python | SIGAA (BR) |
| [`untisapi/untis4j`](https://github.com/untisapi/untis4j) | ⚠️ **LGPL-3.0** | Java | WebUntis (DE/AT) |
| [`shinyquagsire23/InfiniteCampusAPI`](https://github.com/shinyquagsire23/InfiniteCampusAPI) | ⚠️ **WTFPL v2** | Java | Infinite Campus (US) |

🟢 **Ten of the twelve are MIT or BSD, and together they cover six countries in four
protocol families.** Measured by *placed* permissive infrastructure, this is the broadest
single shelf this KB has added in one pass.

### ⚠️ Two warnings, and the second one is the reason this shelf is not a green light

**1. The licence is not the binding constraint here. The vendor's Terms of Use is.**

Every library above talks to a **proprietary, closed SIS**. The MIT grant covers the client
code; it says nothing about whether you may call the endpoint. The tier documents this
itself — `GeovaneSchmitz/sigaa-api` describes itself as *"uma biblioteca de **Web
Scraping**"*, `kc0506/ntucool` as *"**unofficial** … use it at your own risk"*, and
`chrischall/infinitecampus-mcp` quotes Infinite Campus's ToU forbidding access *"by any
means other than our publicly supported interfaces (for example, scraping or using the
content to train artificial intelligence software)"* before stating that it does exactly
that. Full treatment in `agents/top.md`, Finding 2; the gate that operationalises it is
**P26** in `compose/patterns.md`.

🔵 **The practical rule: these libraries are excellent for a prototype, a migration, or a
one-off data rescue the institution itself authorises — and they are not a production
integration path unless the institution holds an API agreement with its vendor.** When it
does, the same libraries become legitimate, because the institution's own credentials and
contract cover the access. **The asset is fine. The access needs paperwork.**

**2. Three licence shapes on this shelf would fail an automated allowlist, two of them
wrongly.**

- ⚠️ **`WTFPL v2`** (`shinyquagsire23/InfiniteCampusAPI`, 474 B payload, Sam Hocevar
  copyright) — maximally permissive in effect, **not OSI-approved**, and rejected by name by
  many corporate allowlists. Usable in substance; expect to justify it, and expect some
  clients to refuse it on the name alone.
- ⚠️ **`LGPL-3.0`** (`untisapi/untis4j`) — the middle path this KB already documents for
  OpenEduCat: dynamic linking keeps your code yours, modifications to the library itself must
  be published.
- 🔴 **`CC BY-NC-SA 4.0`** (`Jona-Zwetsloot/Somtoday-Mod`) — **NonCommercial. Not usable in
  client work at all**, and a content licence applied to software besides.

⚠️ **And read these families with the shared classifier, not a fresh one.** This pass's
from-scratch probe script mislabelled four payloads on this shelf as
Creative Commons/NonCommercial — three GPL-3.0 and one AGPL-3.0 — because GPL-3.0 §6 contains
the word *"noncommercially"*. 🟢 **`compose/code/lib/license_family.sh` already gets all of
them right**, because it gates the Creative Commons branch on a CC marker before reading
NonCommercial as an attribute. **Source the library.** See `agents/top.md`, method note 2.

### The costliest absences on this shelf

| Repo | ★ | Why it matters |
|---|---|---|
| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | **214** | The JavaScript WebUntis client, highest-starred ungranted asset in the tier. 6 filenames probed on `master`: **nothing**. |
| [`Litarvan/pronote-api`](https://github.com/Litarvan/pronote-api) | 192 | The multi-language PRONOTE API. **Ungranted.** `pronotepy` (MIT, 241★) is the answer for Python. |
| [`IFRN/suapi`](https://github.com/IFRN/suapi) | 28 | ⚠️ Published by the **federal institute that operates SUAP** — and ungranted, while an individual's client is MIT. One file, one commit, a public institution: **the most answerable upstream ask in this pass.** |
| [`NCSIS/InfiniteCampus-Vendor-Integration`](https://github.com/NCSIS/InfiniteCampus-Vendor-Integration) | 13 | Vendor-integration PowerShell, ungranted. |

🔵 **Pattern across all four: the ungranted assets cluster at the *most useful* layer** — the
general-purpose client and the official-institution publication — while the permissive ones
are language-specific ports and student tools. The same shape this KB recorded in the Canvas
MCP cluster, now reproduced in a completely different tier.

### What this adds to the architecture menu

The interoperability tier added in the tenth pass (OneRoster, Ed-Fi, xAPI/LRS) and this
client layer answer the **same** question by **different** routes, and the difference is
entirely about who authorised the access:

| Route | Grant on the code | Grant on the data | Use it for |
|---|---|---|---|
| **Official API** (OneRoster / Ed-Fi, permissive implementations already shelved) | permissive | **the institution's contract with its vendor** | 🟢 production |
| **SIS client library** (this shelf) | permissive (10 of 12) | ⚠️ **none — often contrary to vendor ToU** | prototype, migration, authorised rescue |

🟢 **Read together, they are the strongest architectural recommendation this KB can make for
an administrative engagement: prototype on the client library to prove the workflow in days,
then ship on the official API path.** The prototype is cheap and the production path is
contractual, and conflating them is how an engagement discovers in month three that its
integration was never licensable.

---

## Added in the sixteenth pass of 2026-10-06 — the national curriculum tier, and a licence family this KB had no row for

The ministry channel (`repos/trending.md`, sixteenth pass) produced an infrastructure tier this
KB has described as *assumed* in two patterns and never shelved: **the national curriculum, as
a machine-readable service, with a written commercial grant.**

### The curriculum-data tier

| Repo | Branch | Licence (read from payload) | Bytes | What it gives you |
|---|---|---|---|---|
| [`Utdanningsdirektoratet/Grep_SPARQL`](https://github.com/Utdanningsdirektoratet/Grep_SPARQL) | `main` | 🟢 **NLOD** (`LICENSE.md`) — **commercial use granted in writing** | 1,783 | Norway's national curriculum (**LK20**) as **queryable RDF over a SPARQL endpoint, in production since 7 Dec 2020**. Competence aims, subjects, programmes, cross-curricular topics — addressable, not scraped. |
| [`Utdanningsdirektoratet/KL06-LK20-public`](https://github.com/Utdanningsdirektoratet/KL06-LK20-public) | `master` | 🔴 **NO-PAYLOAD** (30+ filename variants) | 0 | Documentation of the revised **Grep-data interface** for the LK20 reform, plus example files. The live service's own docs are in the repo wiki. |
| [`fnshr/kyo-kan`](https://github.com/fnshr/kyo-kan) | `master` | 🟢 **CC0-1.0** | 6,555 | Japan's **MEXT official kanji-by-grade tables** (*gakunenbetsu kanji haitōhyō*) as structured open data. Small, and the only MEXT-derived asset found. |
| [`NKAmapper/school2osm`](https://github.com/NKAmapper/school2osm) | `master` | 🟢 **CC0-1.0** | 6,555 | Extracts every school from Norway's **National School Register (NSR)**. An institution roster, free of restriction. |

### The education-microdata tier (LATAM)

| Repo | Branch | Licence (read from payload) | ★ | What it gives you |
|---|---|---|---|---|
| [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR) | `main` | 🟢 **MIT** — ⚠️ declared in **`DESCRIPTION`**, not `LICENSE` | 15 | **CRAN** package v1.2.0.9000. Download + process **INEP** microdata: Censo Escolar, ENEM, SAEB, Censo da Educação Superior, ENADE, ENCCEJA, IDD, CPC, IGC, CAPES, FUNDEB. **Eleven national instruments behind one MIT API.** |
| [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | `main` | 🟢 **MIT** (1,072 B) | 1,805 | 70 Brazilian public APIs as MCP tools, 13 of them education. 🟢 **Canonical — identity settled in the seventeenth pass** (root-commit comparison; `dasgltd/mcp-brasil` is a 0★ fork of this address). |
| [`inepdadosabertos/api`](https://github.com/inepdadosabertos/api) | `master` | 🔴 **GPL-2.0** (18,025 B) | 45 | Civil-society open-data API over INEP. ⚠️ **Created 2014** — treat as reference, not as a dependency, and note it is *not* INEP's own. |
| [`lucasmation/microdadosBrasil`](https://github.com/lucasmation/microdadosBrasil) | `master` | 🔴 **NO-PAYLOAD** | 174 | Reads Brazilian public microdata (CENSO, PNAD). The most-starred of this group and the one you cannot use. |

### 🟢 NLOD belongs on this KB's permissive allow-list — in the data tier

The twelfth pass added **ECL-2.0** and **ISC** to the allow-list because the standard
"MIT/Apache/BSD" filter rejected two licences that are permissive in substance. **NLOD is the
same correction, one tier down: it governs data, not code.**

Quoted from the payload (the licence ships bilingually, Norwegian and English):

> *"You are allowed to copy and make available, change and/or merge data sets described here
> with other data sets, and **to use them for commercial purposes**."*

| NLOD condition | What it costs a Globant deliverable |
|---|---|
| Attribution in a prescribed string — *"Contains data under NLOD, made available on data.udir.no"* | 🟢 A footer line. |
| **The Udir logo may not be used** without a separate agreement | 🟢 Trivial — and a trap only if a designer drops a ministry crest into a client deck to imply endorsement. |
| Data must not be presented misleadingly, distorted or misrepresented | 🟢 Already required by the EU AI Act transparency duties this KB tracks. |
| No liability for errors in the data | ⚠️ Real: a curriculum-alignment claim you make is **yours**, not the ministry's. Budget a validation step. |
| **No share-alike. No non-commercial clause.** | 🟢 **This is the whole point.** The output is yours to license as you wish. |

⚠️ **Read the boundary precisely, because it is easy to overclaim.** NLOD grants the **data**.
`Grep_SPARQL` is *documentation of an endpoint* — there is no substantial codebase to vendor.
The SPARQL client, cache, mapping layer and item generator are yours to write or to take from
the permissive shelves above.

### The public-sector application tier — permissive, and read correctly

| Repo | Branch | Licence (read from payload) | What it is |
|---|---|---|---|
| [`Utdanningsdirektoratet/PAS2-Public`](https://github.com/Utdanningsdirektoratet/PAS2-Public) | `master` | 🟢 **Apache-2.0** (11,325 B) | The openly published portion of Norway's **national exam administration system**. A ministry's production exam code, patent-granted. |
| [`Utdanningsdirektoratet/designsystem`](https://github.com/Utdanningsdirektoratet/designsystem) | `main` | 🟢 **MIT** (1,079 B) | The directorate's design system, on top of `digdir/designsystemet`. Active 2026-10-02. **A government-grade accessible component set for education UIs.** |
| [`Utdanningsdirektoratet/xmldataimport`](https://github.com/Utdanningsdirektoratet/xmldataimport) | `master` | 🟢 **MIT** (1,079 B) | Loads XML test data into SQL Server for data-driven automated tests. |
| [`Utdanningsdirektoratet/PAS-scoop-public`](https://github.com/Utdanningsdirektoratet/PAS-scoop-public) | `master` | 🟢 **Apache-2.0** (11,357 B) | Scoop bucket for the PAS toolchain. |
| [`Utdanningsdirektoratet/VFKL`](https://github.com/Utdanningsdirektoratet/VFKL), `VFKL_rebase` | `main` | 🟢 **MIT** (1,063 B) | ⚠️ **Both archived**, and the copyright holder is **Altinn** (Norway's national digital platform), not Udir — a cross-agency reuse worth knowing about, and a holder-mismatch of the kind `p184` exists to catch. |
| [`Utdanningsdirektoratet/pifu`](https://github.com/Utdanningsdirektoratet/pifu) | `master` | 🔴 **NO-PAYLOAD** | **PIFU** — Norway's person-data/rostering flow spec for education. ⚠️ **The interoperability tier's Norwegian entry, and it is ungranted.** |

### 🟢 Why this shelf changes a conclusion rather than lengthening a list

The tenth pass shelved the interoperability tier and the twelfth pass the xAPI/LRS tier, both
on the finding that **39% of district RFPs score interoperability**. Both shelves were built
from *vendor-neutral standards bodies*. This one is built from **a state**, and it answers a
question those could not:

🔵 **In Norway, "curriculum-aligned" is a verifiable claim rather than a marketing one** — there
is a government endpoint to align *against*, and a licence that lets you bill for the
alignment. In every other country this KB covers, P15 and P16 have had to **assume** such a
source exists. ⚠️ **The sixteenth pass measured that it usually does not:** France publishes
teachers' material and no ministry estate, Japan publishes PDFs plus a CC0 kanji table, the
Gulf publishes nothing findable. **Norway is the exception that shows what the other four are
missing** — and `P25` is written so the Norwegian case is the reference implementation and the
others are a documented substitution.

---

## Added in the seventeenth pass of 2026-10-06 — a national standard you can lift, and a national estate you cannot

The channel was the **ministry tier as `org:`**. Two agencies had an estate; they split along a
line that decides how each one enters an engagement.

### 🟢 The permissive row — a national interoperability standard, Apache-2.0

| Repository | Branch | Licence (payload-verified) | ★ | Why it belongs on this shelf |
|---|---|---|---|---|
| [`Skolverket/dnp-ss12000-reference-api`](https://github.com/Skolverket/dnp-ss12000-reference-api) | `main` | 🟢 **Apache-2.0** (`LICENSE`, 11,339 B, full text) | 5 | **Reference implementation of SS 12000**, the Swedish national standard for information exchange between school administration systems — published by the national agency itself, Java, permissive. 🟢 **The rostering/SIS-interop layer this KB has been missing a permissive entry for:** `p230-rostering-layer-axis` exists because every prior candidate on that layer was copyleft, vendor-hosted or ungranted. |

🔵 **Why one row matters more than its star count.** Everything else this KB shelves on the
student-data layer is either a *platform* (which you adopt whole) or a *client* for someone's
proprietary API. A **standard with a permissive reference implementation** is the third thing:
you can implement it, ship it inside a closed product, and the other end of the wire is a
national specification rather than a vendor's roadmap. ⚠️ **5★ is not a maturity signal here** —
a reference implementation of a national standard is used by integrators who do not star it.

### 🟡 The Finnish estate — nine of 188, read correctly, and shelved with a condition

**`org:Opetushallitus` has 188 public repositories, all live on the day they were read.** Nine
payloads read from the real default branch (**six are `master`**):

| Repository | Branch | Licence (payload-verified) | ★ | Layer it supplies |
|---|---|---|---|---|
| [`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet) | `master` | 🟡 **EUPL-1.1** (631 B) | 3 | **National core curriculum + qualifications** (ePerusteet). Finland's analogue of Norway's Grep. |
| [`Opetushallitus/koski`](https://github.com/Opetushallitus/koski) | `master` | 🟡 **EUPL-1.1** (653 B) | 23 | **National study records** — qualifications and study rights in one service. |
| [`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) | `main` | 🟡 **EUPL-1.2** (303 B ×2, **in subdirectories**) | 0 | **National OER library** (`aoe.fi`), 6,829 commits. |
| [`Opetushallitus/ataru`](https://github.com/Opetushallitus/ataru) | `master` | 🟡 **EUPL-1.2** (295 B) | 11 | **Admissions application forms** — generic form generation. |
| [`Opetushallitus/organisaatio`](https://github.com/Opetushallitus/organisaatio) | `master` | 🟡 **EUPL-1.1** (631 B) | 4 | **Register of providers and institutions** — the join key for the rest. |
| [`Opetushallitus/oppijanumerorekisteri`](https://github.com/Opetushallitus/oppijanumerorekisteri) | `master` | 🟡 **EUPL-1.1** (631 B) | 1 | **National learner identity** (learner-number registry). |
| [`Opetushallitus/ehoks`](https://github.com/Opetushallitus/ehoks) | `master` | 🟡 **EUPL-1.1** (631 B) | 1 | **Personal competence-development plans** (vocational). |
| [`Opetushallitus/suorituspalvelu`](https://github.com/Opetushallitus/suorituspalvelu) | `main` | 🟡 **EUPL-1.2** (652 B) | 0 | **Attainment service** (2025, newest). |
| [`Opetushallitus/valtionavustus`](https://github.com/Opetushallitus/valtionavustus) | `master` | 🟡 **EUPL-1.1** (652 B, **(c) 2026**) | 8 | **State-grant administration** for providers. |

🔴 **179 of the 188 are unread, not absent.** This table is a sample chosen by stars and by
domain relevance, and it should be read as such.

### ⚠️ The condition on the Finnish rows, stated once and precisely

**The EUPL is OSI-approved, so these are open source.** What makes them different from every
other row on this shelf is **where the copyleft reaches**:

| Question | Answer |
|---|---|
| May we read, study, run and modify it? | 🟢 Yes. |
| May we **call these services** from our own agent over their APIs? | 🟢 **Yes, and the licence is irrelevant to that** — calling is not distribution. |
| May we fork it into a **hosted** client product and keep our changes closed? | 🔴 **No.** EUPL Art. 1 assimilates *"communication to the public"* to distribution, so **SaaS delivery triggers the copyleft, AGPL-style**. |
| May the combined work be relicensed? | 🟡 **Yes — EUPL Art. 5 carries a compatibility list** (GPL-2.0/3.0, AGPL-3.0, LGPL, MPL-2.0, EPL, CeCILL, OSL). ⚠️ Compatible-licence terms *prevail on conflict*, and the EC's own discussion notes the SaaS obligation can be circumvented that way. **Do not build a commercial plan on that route without counsel.** |

🔵 **The shelving rule this produces:** the Finnish estate belongs on this shelf as a **domain
model and an integration target**, not as a starting codebase. It is the most complete public
description of how a national education system's data actually fits together — curriculum,
provider register, learner identity, study records, attainment, plans, grants — and reading it
is free of licence consequence. **Forking it into a hosted product is the one move that is not.**

### 🔴 And the instrument cannot see any of it

`grep -c -i eupl compose/code/lib/license_family.sh` → **0**. Traced through the code (it could
not be executed this pass), every payload above lands on `UNCLASSIFIED`: the EUPL ships as a
**300–650 B grant notice with no title block**, and the classifier is a title-block classifier by
design. 🟢 **Until a grant-notice anchor exists, these nine rows are the only EUPL rows this KB
can defend, because they were read by hand.** That work is instruction 1 for the next pass.


## Added in the eighteenth pass of 2026-10-06 — the certified assessment tier, and a national agency's metadata layer

**Channel new to this KB this pass: the standards-body conformance register** — searching by
**standard + conformance certification** rather than by topic, star count, funder or institution.
Every licence below was read from the repository's own payload on `raw.githubusercontent.com`
on 2026-10-06. Star counts, where given, were read the same day via `WebFetch`; cells that say
*not read this pass* say so rather than carrying an inferred number.

### QTI 3 — assessment item delivery, and the first externally certified permissive asset in this KB

Trend 28 swept LTI 1.3, OneRoster and Caliper and recorded **QTI as "not swept"**. Swept now, and
it is the **best-served** standard on the permissive shelf, not the worst.

| Repo | Licence (read from payload) | ★ / forks | Why it matters for an education engagement |
|---|---|---|---|
| [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** (`main/LICENSE`, © 2022-2024 Amp-up.io, LLC) | 30 / 6 | 100% JavaScript QTI 3 item player, **1EdTech Certified for QTI 3 Basic *and* Advanced "Delivery" conformance**. 🟢 The only asset in this KB that is **both permissive and third-party certified** — fork it, brand it, and the conformance claim in the bid is somebody else's audit, not your assertion |
| [`amp-up-io/qti3-item-player-vue3`](https://github.com/amp-up-io/qti3-item-player-vue3) | **MIT** (`main/LICENSE`, © 2024 Amp-up.io, LLC) | not read this pass | Vue 3 build of the same component. Use when the client front end is already Vue |
| [`longsightgroup/qti3`](https://github.com/longsightgroup/qti3) | **MIT** (`main/LICENSE.md`, © 2026 Longsight, Inc.) | 5 / 2 | TypeScript reference implementation — **667 commits, 12 npm packages**: parsing, validation, rendering, **scoring**, and **migration from QTI 1.2 / 2.x into QTI 3**. The migrator is the part nobody else ships, and legacy item banks are the reason most assessment projects stall |
| [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player) | **MIT** (`main/LICENSE`, © 2026 AE Studio) | not read this pass | Framework-agnostic npm renderer with full response processing. The neutral option when the front-end framework is not yet chosen |
| [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer) | **MIT** (`main/LICENSE`, © 2026 metyatech) | not read this pass | QTI 3.0 item HTML rendering utilities. Smallest surface of the five |

#### Two QTI assets that are **not** permissive — read this before the architecture, not after

| Repo | Licence (read from payload) | The constraint |
|---|---|---|
| [`Citolab/qti-components`](https://github.com/Citolab/qti-components) | **GPL-3.0** (`main/LICENSE.md`) | 19★ / 10 forks, **2,456 commits** — the most mature renderer here, and copyleft. Citolab is the software lab attached to **Cito**, the Netherlands' national assessment institute. ⚠️ Its README states: *"the licensing is GPLv3 — if you want to use it in another way, feel free to ask!"* The **payload is GPL-3.0** and the **holder advertises negotiability**. That is an *invitation to dual-license*, it is invisible to any payload-reading classifier, and it is a **conversation to have before you design around the licence**. See trends §43 |
| [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) | **GPL-2.0** (`master/LICENSE`) | PHP SDK from the TAO assessment platform. **GPL-2.0, not 3.0** — so it is **not licence-compatible with GPL-3.0-only code**. Same trap as `francoisjacquet/rosariosis` in `verticals/solutions.md`. Check before combining |

🔴 **And one fork that nearly entered this shelf as a public-body asset.**
[`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components) (1★, 0 forks) is **forked
from `Citolab/qti-components`** — identical root commit `de8b27b`, **2,377 commits against
upstream's 2,456, so 79 behind**. Caught by running `git clone --filter=blob:none --no-checkout`
**before the row was written**. Pin the Citolab address; do not cite the Kennisnet one.

### Kennisnet — the Dutch national education-ICT agency, metadata and vocabulary layer

**[Stichting Kennisnet](https://github.com/Kennisnet)**, the Netherlands' public agency for ICT in
education, publishes **29 repositories**. Nine probed this pass: **6 MIT, 1 GPL-3.0** (the stale
fork above), **2 NO-PAYLOAD**. These are the layer an AI content pipeline needs and that nobody
should write twice.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [`Kennisnet/pylom`](https://github.com/Kennisnet/pylom) | **MIT** (`master/LICENSE`, © 2017 Kennisnet) | metadata — **Python** | Reads and writes **IMS-LOM** learning-object metadata records. 🟢 **A permissive Python library for an education standard** — see the correction to trend 28 below |
| [`Kennisnet/py-eduterm-client`](https://github.com/Kennisnet/py-eduterm-client) | **MIT** (`master/LICENSE`, © 2018 Kennisnet) | curriculum vocabulary — **Python** | Client for **Eduterm**, the Dutch curriculum-vocabulary service. The curriculum-alignment tool call of P29, already written, in the language the agents are written in |
| [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | **MIT** (`main/LICENSE`, © **2026** Kennisnet) | assessment | QTI 3 support library, **published this year**. The permissive PHP path into QTI, where `oat-sa/qti-sdk` is GPL-2.0 |
| [`Kennisnet/phpNLLOM`](https://github.com/Kennisnet/phpNLLOM) | **MIT** (`master/LICENSE`, © 2017 Stichting Kennisnet) | metadata | **NL-LOM**, the Dutch national application profile of LOM. The worked example of how a country profiles a global metadata standard |
| [`Kennisnet/phpEdurepSearch`](https://github.com/Kennisnet/phpEdurepSearch) | **MIT** (`master/LICENSE`, © 2015 Stichting Kennisnet) | discovery | Client for **Edurep**, the national learning-resource search index. A national OER index with a permissive client is a **content source you may query without a licence negotiation** |
| [`Kennisnet/OaiPmh`](https://github.com/Kennisnet/OaiPmh) | **MIT** (`main/LICENSE`, © 2024 Kennisnet) | harvesting | OAI-PMH implementation — the protocol national repositories actually expose |
| [`Kennisnet/qti-editor-angular`](https://github.com/Kennisnet/qti-editor-angular) | 🔴 **NO-PAYLOAD** (`main`+`master` × 6 filenames, all 404) | authoring | QTI editor. **Ungranted — do not vendor it** |
| [`Kennisnet/edurep-xslt`](https://github.com/Kennisnet/edurep-xslt) | 🔴 **NO-PAYLOAD** (`main`+`master` × 6 filenames, all 404) | transforms | Edurep XSLTs. **Ungranted** |

⚠️ **Nine of 29 probed, chosen by stars and domain relevance.** The estate's ungranted rate is
**sampled, not established** — the same shortfall pass 17 declared for Opetushallitus's 188
repositories, and it is carried as a declared gap rather than rounded off.

### 🔵 The correction this section forces on trend 28

Trend 28 concluded that the permissive shelf has a **"Python-shaped hole"** — *"Python, where
essentially all of the AI tutoring and agent code in this KB is written, is not [served]."*

**Half of that survives.** ~~There is still **no permissive Python LTI 1.3 library**, which is the
claim trend 28 actually measured.~~ 🔵 **WITHDRAWN, twenty-fourth pass of 2026-10-07** — [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
is **MIT**, head commit **2 d**, PyPI `django-lti` **v0.10.1 (61 d)**. What survives is only the
narrow form: **no live *framework-agnostic* permissive Python LTI 1.3 library**. 🔵 **NARROWED, twenty-fifth pass of 2026-10-07 — "none" is now "one alpha".** [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) (MIT) **vendors `PyLTI1p3`, rebranded** — its README says so — and publishes it as [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 (103 d), one release ever**; head commit **63 d**; **0★**; `Development Status :: 3 - Alpha` with the FastAPI adapter and token minting **unbuilt**; and its `LICENSE` holder is **`Dmitry Viskov`, not its own authors**. **Not "no option", and not a safe dependency either.** Full row in `repos/foundations.md`. And `pylom` and
`py-eduterm-client` are **MIT Python libraries for education standards**, so Python *is* served for
**metadata and curriculum vocabulary** as well.

🟢 **The hole is LTI-shaped, not Python-shaped — and that makes the contribution opening cheaper,
not smaller.** It is one protocol, with a procurement-scored buyer already attached (39% of US
districts score interoperability in the RFP rubric). Corrected in place in `intel/trends.md` §28.

## Added in the nineteenth pass of 2026-10-06 — the conformance-engine tier, which nineteen passes never recorded

**Channel: the regulatory-citation channel** — sweeping for implementations of the exact technical
standard a binding rule names (WCAG 2.1 AA, WCAG 2.2 AA, EN 301 549, PDF/UA) rather than by topic.
Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-06, across `main` / `master` / `develop` and 7–11 filename variants. Star and fork counts
were read from the rendered repository page the same day (`api.github.com` is 403 here).

**Why these belong in *foundations* and not in trending:** none of them is new, none is
education-specific, and that is the point — they are the deterministic substrate that every
accessibility claim in a client deliverable has to rest on, and this KB's accessibility work so far
recorded the **agent** layer (`Community-Access/accessibility-agents`, MIT) without the engines
underneath it. An agent that reports WCAG findings with no engine beneath it is producing an
opinion, not evidence.

### The permissive engines — Apache-2.0 and MIT

| Repo | Licence (read from payload) | ★ / forks | What it gives you |
|---|---|---|---|
| [IBMa/equal-access](https://github.com/IBMa/equal-access) | **Apache-2.0** (`master/LICENSE`) | **780 / 108** | IBM Equal Access Accessibility Checker. **Nine packages** in one repo: `accessibility-checker-engine` (the rules), `accessibility-checker` (Node), `accessibility-checker-extension` (browser devtools), **`java-accessibility-checker`**, `cypress-accessibility-checker`, `karma-accessibility-checker`, `vitest-accessibility-checker`, `rule-server`, `report-react`. JavaScript. 🟢 **The pick when the deliverable must run in the client's CI**, and the only engine here with a **JVM** binding — which matters on a Java LMS estate. |
| [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | **Apache-2.0** (`main/LICENSE`) | **30.9k / 9.8k** | Audits pages for accessibility alongside performance and best practices. **Runs locally and sends nothing to a remote server** — which is what makes it quotable under an EMEA data-residency clause. CLI, Node module, or Chrome DevTools. 🟡 Its a11y category is axe-core-derived and deliberately partial: a gate, not an audit. |
| [microsoft/accessibility-insights-web](https://github.com/microsoft/accessibility-insights-web) | **MIT** (`main/LICENSE`, © Microsoft Corporation) | **955 / 182** | Chrome/Edge extension for assessing web accessibility. TypeScript. 🟢 **The differentiator is the guided assessment workflow** — it walks a human through the criteria a scanner cannot decide, which is the half of a conformance claim that automation cannot produce. |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** (`main/LICENSE`) | **76.8k / 10.8k** | OCR engine, **100+ languages**, LSTM line recogniser. Outputs plain text, **hOCR**, **ALTO**, **PAGE**, PDF and text-only PDF. 🟢 **The entry point for scanned textbooks** — and the structured output formats are what make a downstream tagging step possible at all. ⚠️ Latest tagged release on the page is **5.0.0 (2021-11-30)** while development continues on `main`; pin a distribution package rather than the tag. |

### The weak-copyleft engines — usable, with two obligations

| Repo | Licence (read from payload) | ★ / forks | The obligation |
|---|---|---|---|
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | ⚠️ **MPL-2.0** (`master/LICENSE`) | **7.6k / 954** | Accessibility engine for automated web UI testing; **WCAG 2.0, 2.1 and 2.2 at A, AA and AAA**, multi-locale, 5,586 commits on `develop`. 🟢 **MPL-2.0 is file-level copyleft: using it unmodified as a dependency does not reach the studio's own files.** ⚠️ **Two things do bite** — it must appear in the client's SBOM with its licence, and **editing a rule file puts that file under MPL-2.0 with source-disclosure attached**. Tune through configuration, never by patching rules. 🔵 **This is the engine inside every MIT accessibility agent in this KB** (`accessibility-agents` declares `@axe-core/cli`; `a11ymcp` declares `axe-core` and `@axe-core/puppeteer` at runtime), so the inheritance is not optional — it is the shelf. |
| [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | ⚠️ **MPL-2.0** (`main/LICENSE`) | **34.9k / 2.4k** | Adds an OCR text layer to scanned PDFs, deskews, and emits **PDF/A**. Python; Linux/macOS/Windows/FreeBSD. Wraps Tesseract. 🟢 Same file-level reasoning as axe-core — invoke it as a tool and nothing propagates. 🔴 **Read the limit precisely: a searchable PDF is not an accessible PDF.** It produces no tags, no reading order and no structure, so it does **not** satisfy PDF/UA. |

### 🔴 The gap this tier makes visible — validation is served, remediation is not

| Need | Permissive option | Status |
|---|---|---|
| Scan web content against WCAG | equal-access (Apache-2.0), axe-core (MPL-2.0), Lighthouse (Apache-2.0) | 🟢 **Well served** |
| Guide the manual half of a claim | accessibility-insights-web (MIT) | 🟢 Served |
| OCR a scanned textbook | Tesseract (Apache-2.0) | 🟢 Served |
| Make a scanned PDF searchable | OCRmyPDF (MPL-2.0) | 🟡 Served, and **not the same thing** as accessible |
| **Validate PDF/UA** | [veraPDF/veraPDF-library](https://github.com/veraPDF/veraPDF-library) | 🔴 **Dual GPL / MPL** — `LICENSE.GPL` and `LICENSE.MPL`, ⚠️ **filenames outside every shortlist this KB probes** (present on `master` and `integration`, absent from `main`), so an 11-filename sweep reports it ungranted while the grant is in the root |
| **Produce tagged, accessible PDF/UA** | — | 🔴 **Nothing permissive found.** Searched PDF/UA remediation, tagged PDF, structure tagging, accessible PDF generation |
| Reference the **EN 301 549** clause set | — | 🔴 **Nothing** except an MIT adapter to a paid API (`agents/top.md`) |

🔵 **The rule this yields for a proposal:** everything up to *"here is a per-criterion finding with
evidence"* can be built on Apache-2.0 and MIT with two MPL-2.0 tools invoked unmodified. Everything
past *"and here is the remediated PDF"* is **human labour on a copyleft validator**. ⚠️ **Scope and
price the document estate separately from the web estate.** They look like one deliverable in a
statement of work and they are not.

### 🟢 Why this shelf changes a conclusion rather than lengthening a list

This KB has recorded, across several passes, that permissive education supply collects at the
*edges* of platforms it may not fork. The conformance tier is the clearest instance yet and it
inverts the usual complaint: **the measuring layer is permissive and the end-user application layer
is copyleft** (`cboard` GPL-3.0, `AsTeRICS-Grid` AGPL-3.0, `pa11y` LGPL-3.0, `nvda` GPL-2.0+ in
`copying.txt` — see `verticals/solutions.md`). 🟢 **Since the billable work is remediating the
client's own estate rather than shipping an assistive application, the half a studio needs is the
half that is permissive.** That is a better position than this KB has been able to report for any
other tier in education, and it is worth stating plainly in a capability deck.

---

## Added in the twentieth pass of 2026-10-06 — the evidence tier, which every transition article actually asks for

**Channel new to this KB this pass: the transition-provision channel** — reading each
binding instrument's **transitional article** instead of its entry-into-force date. Full
findings in `agents/trending.md`; the regional consequences in `intel/market.md`; the
delivery recipe in `compose/patterns.md` **P28**.

The channel produced a supply question this KB had never asked. Every transition regime
found this pass discharges on an **artefact**, not on a date:

| Regime | What the extension is conditional on | The artefact that proves it |
|---|---|---|
| **EU AI Act Art. 111** | the design of the high-risk system **remaining unchanged** | a versioned, dated record that the deployed system is the same system |
| **Vietnam** Decree 142/2026/ND-CP | a **transition plan** filed on the one-stop portal | the plan, plus the inventory behind it |
| **Vietnam** Decision 33/2026/QĐ-TTg, education category 1 | self-learning content **not** drawn from *"uncontrolled data sources"* | dataset provenance and validation records |
| **EU Annex III §3** (admissions, assessment, placement) | bias and accuracy obligations | fairness measurements over the decision, retained |
| **EMEA, per the nineteenth pass** | 🔴 **no harmonised standard cited under the EAA**, so no presumption of conformity | evidence is the *only* route — there is no standard number to point at |

🔴 **Nineteen passes recorded none of the tooling that produces these artefacts.** Grep
confirmed it before this shelf was written: `mlflow`, `dvc`, `evidently`, `whylogs`,
`great_expectations`, `croissant`, `OpenLineage`, `fairlearn`, `AIF360` — **zero
occurrences across all eight files.** The KB had the obligations and the pedagogy, and
nothing in between.

### The shelf — all licences read from the repository's own payload on 2026-10-06

Stars and descriptions read from each repository page the same day via `WebFetch`
(`github.com` is 403 to `curl` through this environment's proxy; `raw.githubusercontent.com`
is not). **Ten rows, all verified.**

| Repo | Licence (payload path) | ★ / forks | Lang | What it does, and why an education engagement needs it |
|---|---|---|---|---|
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | **Apache-2.0** (`LICENSE.txt`) | 28.3k / 6.4k | Python | *"The open source AI engineering platform for agents, LLMs, and ML models."* Model registry with versioned stages. **This is the Art. 111 instrument**: the registry is what lets you state, with dates, that the system in service is the system that was placed in service. |
| [iterative/dvc](https://github.com/iterative/dvc) — 🔴 **now `treeverse/dvc`**; both paths serve head `56e5982` and PyPI `dvc` declares `Source: github.com/treeverse/dvc`. See the canonical-name table below | **Apache-2.0** (`LICENSE`) | 15.9k / 1.3k | Python | *"Data Versioning and ML Experiments."* Versions the **corpus** alongside the model, in Git. The answer to Vietnam's *"uncontrolled data sources"* trigger is a hash, and this produces it. |
| [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) | **Apache-2.0** (`LICENSE`) | 11.9k / 1.9k | Python | *"Always know what to expect from your data."* Declarative data validation. Turns "the curriculum corpus is controlled" from an assertion into a suite that fails a build. |
| [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | **Apache-2.0** (`LICENSE`) | 8.0k / 946 | Python | ML **and LLM** observability — evaluate, test and monitor any AI-powered system or pipeline. The regression baseline the nineteenth pass said a remediation contract has to ship. |
| [Trusted-AI/AIF360](https://github.com/Trusted-AI/AIF360) | **Apache-2.0** (`LICENSE`) | 2.9k / 912 | Python | Fairness metrics for datasets and models, explanations for them, and bias-mitigation algorithms. Annex III §3 is **admissions, assessment and placement** — decisions about people. |
| [whylabs/whylogs](https://github.com/whylabs/whylogs) | **Apache-2.0** (`LICENSE`) | 2.8k / 145 | Python | Data logging that emits **statistical profiles rather than raw records** — visibility into data quality over time with privacy-preserving collection. The shape that survives a student-data rule (see California **AB 1159**). |
| [OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage) | **Apache-2.0** (`LICENSE`) | 2.7k / 540 | Java | *"An Open Standard for lineage metadata collection."* A generic model of run, job and dataset entities. Lineage as a **standard**, so the evidence outlives your pipeline choice. |
| [fairlearn/fairlearn](https://github.com/fairlearn/fairlearn) | **MIT** (`LICENSE`) | 2.3k / 522 | Python | *"A Python package to assess and improve fairness of machine learning models."* The **MIT** option on this shelf — the one with no notice obligation at all. |
| [NannyML/nannyml](https://github.com/NannyML/nannyml) | **Apache-2.0** (`LICENSE`) | ★ not read this pass | Python | Post-deployment performance estimation **without ground-truth labels**. Education's labels arrive a term or a year late; this is the tier that does not wait for them. |
| [mlcommons/croissant](https://github.com/mlcommons/croissant) | **Apache-2.0** (`LICENSE.md`) | 907 / 125 | Python | *"A high-level format for machine learning datasets."* Dataset metadata as a published format — the interchange layer for a provenance claim a regulator or a ministry can read. |

### Measured rejections from the same sweep

Recorded so a later pass does not re-probe them as options.

| Repo | Licence (payload) | Verdict |
|---|---|---|
| [deepchecks/deepchecks](https://github.com/deepchecks/deepchecks) | 🔴 **AGPL-3.0** (`LICENSE`) | Reject for reusable IP. Testing and validation for ML and LLM systems — capable, and the network clause reaches a hosted validation service. |
| [sodadata/soda-core](https://github.com/sodadata/soda-core) | 🔴 **Elastic License 2.0** (`LICENSE`) | Reject. **Not OSI-approved**; the payload opens *"Elastic License 2.0 … Acceptance: By using the software, you agree to…"*. A data-quality tool whose own licence is the risk it would be bought to manage. |

### Read this shelf honestly — three qualifications

🔵 **None of these is an education project.** This is general-purpose MLOps and
responsible-AI tooling. It earns a place in an education KB for one reason: the
transition articles found this pass are discharged by artefacts, and nothing already on
this KB's shelves produces them. ⚠️ **Do not present this tier as education IP** — present
it as the plumbing under a billable education-specific rubric, exactly as P27 treats
`inspect_ai`.

⚠️ **The fairness pair is a measurement tool, not a compliance verdict.** AIF360 and
Fairlearn compute metrics; which metric is the *right* one for an admissions decision is a
legal and pedagogical judgement that has to be made and documented per engagement. A
dashboard of eleven fairness metrics with no stated choice among them is not evidence.

🟢 **The licence shape of this tier is unusually clean** — nine of ten permissive, eight
Apache-2.0 and one MIT, every one read from its own payload. That is a better result than
the platform tier, the assistive tier or the language tier has ever returned in this KB,
and it means the evidence layer is the one part of an Annex III delivery with no licence
negotiation in it at all.

## Added in the twenty-second pass of 2026-10-06 — the interoperability layer, found on a forge this KB had never searched

Channel: the **GitLab REST API v4** (discovery + metadata + payload). Controls, limits and the
detector-error table are in `agents/top.md`; the instrument is in
`compose/code/gitlab-api-channel/`. 25 search terms → **534 unique projects** → the rows below are
the ones that are *infrastructure* rather than product.

🟢 **Why this shelf cared about the sweep at all:** trend 28 of this KB records an
**interoperability hole** — the standards (xAPI, LTI, 1EdTech) are scored line items in
procurement, and the permissive implementations were missing. **Three of the rows below are
standards plumbing**, and they were invisible to every previous pass because every previous pass
searched one forge.

| Repo | Licence (read from payload) | ★ · last activity | Placement | Why it is a foundation |
|---|---|---|---|---|
| [`kbarbounakis/eduapi`](https://gitlab.com/kbarbounakis/eduapi) | ⚠️ **LGPL-3.0** (`LICENSE`; GitLab's detector says `other`) | 0 · 2026-05-15 | ⚠️ EMEA *(README names **Universis**; Greece inferred)* | **An implementation of the 1EdTech EduAPI specification**, built for the **Universis** Greek higher-education student-information project. The first EduAPI implementation in this KB. ⚠️ **LGPL-3.0** — the middle path this KB already documents for Odoo/OpenEduCat: link against it, do not fold it into a proprietary binary |
| [`eduplex-api/cake-api-xapi-proxy`](https://gitlab.com/eduplex-api/cake-api-xapi-proxy) | 🟢 **MIT** (`LICENSE`) | 0 · 2026-08-31 | ⚠️ **unplaced** — no country evidence in repo or README | PHP proxy that forwards **xAPI** statements to an **LRS**, as a CakePHP plugin over `cake-rest-api`. Tiny, single-purpose, permissive — the cheapest way to put a compliant statement pipe in front of an LRS when the LMS cannot speak xAPI itself |
| [`TIBHannover/oer/wordpress-oersi-plugin`](https://gitlab.com/TIBHannover/oer/wordpress-oersi-plugin) | 🟢 **MIT** (`LICENSE`) | 1 · **2026-10-02** | EMEA (Germany) | WordPress integration of **OERSI**, the German higher-education **search index for Open Educational Resources**, with Elasticsearch indexing. From **TIB Hannover** (the German National Library of Science and Technology) — a public-institution-maintained OER discovery layer, MIT, actively committed |
| [`adaptive-learning-engine/adlete-packages`](https://gitlab.com/adaptive-learning-engine/adlete-packages) | 🟢 **MIT** (`LICENSE`) | 1 · **2026-10-02** | ⚠️ EMEA *(inferred)* | ADLETE adaptive-learning engine, monorepo of components; sibling `adaptive-learning-engine/moodle/adleteh5p` binds it to **H5P** inside Moodle. Full entry in `agents/top.md` |
| [`travo-cr/travo`](https://gitlab.com/travo-cr/travo) | 🟢 **BSD-3-Clause** (`LICENSE`) | 8 · **2026-10-06** | EMEA (France) + NA (Québec) | Assignment-distribution and grading infrastructure over **any** GitLab instance, **nbgrader**-integrated. Pairs with [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) (BSD-3-Clause, 1.4k★, v0.9.6 of 2026-09-30) already on this shelf. PyPI `travo` 2.1.1 |
| [`learntech-rwth/omilaxr-ecosystem/v2/omilaxr`](https://gitlab.com/learntech-rwth/omilaxr-ecosystem/v2/omilaxr) | 🔴 **AGPL-3.0** (`LICENSE`) | 1 · 2026-07-03 | EMEA (Germany) | **OmiLAXR** — authoring framework for modular **learning-analytics modules in XR** (VR/AR), from RWTH Aachen's Learning Technologies group. 🔴 Recorded and **excluded from delivery** on licence; kept because it is the only XR-learning-analytics framework this KB has located at all |
| [`particify/dev/foss/arsnova-lms-connector`](https://gitlab.com/particify/dev/foss/arsnova-lms-connector) | 🟢 **MIT** (`LICENSE`) | 3 · 🔴 **2022-09-12** | EMEA (Germany) | Proxy exposing **course-membership data from LMSs under one unified API** — from the ARSnova/Particify audience-response project. 🔴 **The first row in this KB marked dead by measurement rather than by inference:** `last_activity_at` is four years old. Read it as a design, not a dependency |
| [`git-classrooms/git-classrooms`](https://gitlab.com/git-classrooms/git-classrooms) | 🟢 **MPL-2.0** (`LICENSE`, detector agrees) | 3 · 2026-06-16 | ⚠️ **unplaced** (namespace only) | GitHub-Classroom-equivalent for self-hosted GitLab. ⚠️ **A publish-only mirror**: its own description points upstream to a GitHub repository, so the GitLab copy is a *host*, not the project. MPL-2.0 is file-level copyleft — usable alongside proprietary code, not inside the same file |

### ⚠️ The REUSE rows — where the root `LICENSE` is a map and not a grant

| Repo | Root `LICENSE` | The real licence set, enumerated from `/repository/tree?path=LICENSES` |
|---|---|---|
| [`oer/emacs-reveal`](https://gitlab.com/oer/emacs-reveal) | **517 B** REUSE pointer | **4**: `GPL-3.0-or-later`, `CC-BY-4.0`, `CC-BY-SA-4.0`, `CC0-1.0` |
| [`oer/oer-reveal`](https://gitlab.com/oer/oer-reveal) | **516 B** REUSE pointer | **6**: the same four plus `LicenseRef-MIT-HEH-JL`, `LicenseRef-MIT-JL` — two **custom references**, which SPDX permits and no classifier can resolve |

🔵 **Pass 107 had already rejected `oer/emacs-reveal` on licence and kept it as a design.** What is
new is that the licence **set** is now enumerated rather than sampled: an OER toolchain splits
**code under GPL-3.0-or-later** from **content under CC-BY/CC-BY-SA/CC0**, and a `LicenseRef-`
entry means the project wrote its own terms. 🔴 **For this KB's method the consequence is blunt:
on a REUSE repository, reading the root payload — the rule that bought twenty passes of accuracy —
returns a notice board.** The answer lives in `LICENSES/` and in per-file SPDX headers, and only a
tree listing finds it.

### 🔴 What this sweep did **not** find, with the denominator attached

534 unique projects, 25 terms, one forge. **Not found, searched for explicitly:**

| Looked for | Terms used | Result |
|---|---|---|
| a permissive **LTI 1.3 tool provider** | `lms ai`, `learning management system`, `student information system` | 🔴 **0** — the LTI-shaped hole of trend 28 is still open on a second forge |
| a permissive **knowledge-tracing / BKT-IRT** library | `knowledge tracing`, `adaptive learning`, `learning analytics` | 🔴 **0** — `OATutor` (MIT) and the ADLETE engine above remain the only mastery assets in this KB |
| an **MCP server for education** on GitLab | `education agent`, `edtech ai`, `classroom ai` | 🔴 **1 candidate, unusable** — `sheikhcoders/interleaved-learning-mcp` carries **no licence payload at all**. Every education MCP server this KB holds is still GitHub-hosted |
| a **LATAM-origin** education project | all 25 terms | 🔴 **1 LATAM-plausible of 534**, and its placement is an inference from Portuguese-language naming, not a declaration — see `intel/market.md` |

---

## Added in the twenty-third pass of 2026-10-07 — the interoperability tier, re-picked by date

⏱️ **Measurement window 2026-10-06 ~21:00 UTC → 2026-10-07 00:00 UTC; ages computed against the
reference date 2026-10-06.** Licences below were read from the repository's own payload via
`raw.githubusercontent.com` on 2026-10-06. Head-commit dates come from
`git fetch --depth 1 --filter=blob:none`, the channel that works while `api.github.com/repos/*`
returns 403.

🔴 **This file is the coldest shelf file in the KB: of its 230 GitHub references, 33.0% have not been
touched in a year and 18.3% not since before 2024** — against 18.8% and 6.6% for
`compose/patterns.md`. "Foundational" has been doing duty as a synonym for "long-established". This
section fixes the worst instance and dates the rest.

### 🔴 The correction: this file recommends the cold fork of a live library

| | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) |
|---|---|---|
| licence payload | **Apache-2.0**, 11,343 B, `sha256 78b49eea…` | **Apache-2.0**, 11,343 B, `sha256 78b49eea…` |
| composer `name` | `packbackbooks/lti-1p3-tool` | `imsglobal/lti-1p3-tool` |
| composer `description` | *"A library used for building IMS-certified LTI 1.3 tool providers in PHP."* | *(none)* |
| head commit | 🟢 **2026-09-23 (13 d)** | 🔴 **2020-06-03 (2,316 d)** |

🟢 **Byte-identical licence file. Same library. 2,303 days apart.** The consortium's republished copy
stopped; the author's original did not. **Use `packbackbooks/lti-1-3-php-library`.** Nothing in the
licence, the description or the ★ would have surfaced this — only the date.

### The permissive LTI 1.3 shelf, by runtime and by date

| Runtime | Repo | Licence (payload) | Head commit | Age | Verdict |
|---|---|---|---|---|---|
| **Node / JS** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** (11,360 B) | 2026-10-06 | 🟢 0 d | 🟢 **pick** |
| **PHP** | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **Apache-2.0** (11,343 B) | 2026-09-23 | 🟢 13 d | 🟢 **pick** |
| **Java / Spring** | [`oxctl/spring-security-lti13`](https://github.com/oxctl/spring-security-lti13) | **Apache-2.0** (11,357 B) | 2026-10-06 | 🟢 0 d | 🟢 **pick** |
| **Python** | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | **BSD-3-Clause** (1,527 B) | 2026-07-01 | 🟢 97 d | 🟢 **pick** — LTI 1.3 **and** 1.1, tested against Open edX, Canvas, Moodle |
| **Python / Django** | [`Harvard-University-iCommons/django-lti`](https://github.com/Harvard-University-iCommons/django-lti) | **MIT** (1,097 B) | 2025-08-27 | ⚠️ 405 d | ⚠️ usable; ageing |
| **Python (scaffold)** | [`ucfopen/cookiecutter-python-lti`](https://github.com/ucfopen/cookiecutter-python-lti) | **MIT** (1,129 B) | 2026-05-12 | 🟢 147 d | ⚠️ **Django template only** — see the warning below |
| **Elixir** | [`Simon-Initiative/lti_1p3`](https://github.com/Simon-Initiative/lti_1p3) | **MIT** (1,082 B, © Carnegie Mellon University) | 2026-03-13 | 🟢 207 d | 🟢 usable (OLI Torus) |
| **PHP (assessment vendor)** | [`oat-sa/lib-lti1p3-core`](https://github.com/oat-sa/lib-lti1p3-core) | 🔴 **GPL-2.0** (18,091 B) — *corrected pass 28, `P452`; was filed LGPL-2.1* | 2026-07-16 | 🟢 82 d | 🔴 **strong copyleft, and it is a LIBRARY** — there is no LGPL linking exception here, so linking it into a deliverable carries the obligation. The archive called this *"the exception that breaks the symmetry"* and it was right |
| Python | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | MIT (1,069 B) | 2022-11-21 | 🔴 1,415 d | 🔴 **do not start here** |
| Python | [`ucfopen/pylti1.3`](https://github.com/ucfopen/pylti1.3) | MIT (1,069 B, © Dmitry Viskov) | 2023-01-12 | 🔴 1,363 d | 🔴 fork, also cold |
| PHP | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) | Apache-2.0 (11,343 B) | 2020-06-03 | 🔴 2,316 d | 🔴 **superseded by its own upstream** |
| PHP | [`IMSGlobal/LTI-Tool-Provider-Library-PHP`](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | — | 2016-11-28 | 🔴 3,599 d | 🔴 **9.9 years** — remove from any proposal |
| Java | [`UOC/java-lti-1.3-provider-example`](https://github.com/UOC/java-lti-1.3-provider-example) | MIT | 2022-11-18 | 🔴 1,418 d | 🔴 example only, cold |
| Java | [`Unicon/tool13demo`](https://github.com/Unicon/tool13demo) | — | 2024-10-31 | 🔴 705 d | 🔴 demo only, cold |

### 🔴 Three corrections this table forces on standing text in this file

1. **"There is no Python LTI 1.3 library on this shelf"** (stated **four** times in this file, the
   most of any file in this KB) is **false**. It was already false when a later pass reinstated `pylti1.3`; it is now false twice
   over, and the asset that closes it — `jupyterhub/ltiauthenticator`, BSD-3-Clause, 97 days — has
   been cited elsewhere in this KB three times without ever being counted. The gap was an artefact
   of **how this KB filed the repository**, not of supply. (Trend 29, applied to this KB's own
   index; trend 50, because the earlier correction never left its pass-scoped section.)
2. **The LTI-shaped hole of trend 28 is closed.** Five live permissive implementations across five
   runtimes. What remains is not a hole but a **selection discipline**: three of the four
   implementations this KB had been naming are cold.
3. ⚠️ **`Harvard-University-iCommons/django-lti` has a holder mismatch** — published by Harvard's
   iCommons organisation, MIT payload vesting copyright in **the Regents of the University of
   Michigan**. The grant is clean; the counterparty is not the one the URL implies. Record it in any
   provenance pack.

### ⚠️ Recency is not inherited — the rule this adds to the dependency work of the twenty-first pass

Pass 21 resolved 352 dependencies and measured them **by licence**. None were measured **by date**.
The first one checked shows why that matters.
[`ucfopen/cookiecutter-python-lti`](https://github.com/ucfopen/cookiecutter-python-lti) is MIT and
**147 days old**. Its Flask template's `requirements.txt` ends:

```
git+https://github.com/ucfopen/pylti1.3.git@master
```

| Defect | Detail |
|---|---|
| 🔴 stale | resolves to a fork whose head commit is **2023-01-12 — 1,363 days** |
| 🔴 not upstream | the fork, not `dmitry-viskov/pylti1.3`, and not PyPI |
| 🔴 unreproducible | pinned to **`@master`**, a moving branch, so two builds a month apart differ |

🟢 **Its Django template does it correctly**, pinning `django-lti==0.7.1`. **Rule: a component's own
head-commit date says nothing about the dates of what it installs. Run the P22 gate over the
dependency closure, not the dependency list.**

### The rest of the foundation shelf, dated

| Repo | Head commit | Age | Note |
|---|---|---|---|
| [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) | 2026-10-06 | 🟢 0 d | **Apache-2.0**; ASR **and** TTS — the replacement for Piper in P18 |
| [`Citolab/qti-components`](https://github.com/Citolab/qti-components) | 2026-10-06 | 🟢 0 d | 🔴 **GPL-3.0** (35,199 B payload) — *corrected pass 28; was filed LGPL-3.0.* 🔵 **The size already said so:** GPL-3.0 is ~35 kB and LGPL-3.0 is ~7.6 kB, so the byte count published beside the label refuted it without a fetch |
| [`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components) | 2026-07-20 | 🟢 78 d | |
| [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 2025-06-21 | 🔴 **472 d** | MIT, **1EdTech Certified** — certification does not lapse when maintenance stops, but disclose the date |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | 2025-09-04 | 🔴 397 d | |
| [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) | 2024-12-16 | 🔴 659 d | |
| [`theopenem/OneRoster.NET`](https://github.com/theopenem/OneRoster.NET) | 2023-10-13 | 🔴 1,089 d | the only OneRoster implementation on this shelf, and it is cold |
| [`rhasspy/piper`](https://github.com/rhasspy/piper) | 2025-08-26 | 🔴 406 d | MIT; superseded for new work by `sherpa-onnx` |
| [`AI4Bharat/IndicTrans2`](https://github.com/AI4Bharat/IndicTrans2) | 2025-10-03 | 🔴 368 d | liveliest member of a substrate that is **87.5% cold, 0% in 30 days** |
| [`coqui-ai/TTS`](https://github.com/coqui-ai/TTS) | 2024-02-10 | 🔴 969 d | already flagged for relicensing; now also dated |

### 🔴 Declared gaps from this pass, with the denominator attached

| Looked for | How | Result |
|---|---|---|
| a **live permissive OneRoster** implementation | head-commit date over every OneRoster reference in this KB | 🔴 **0 of 2** — `theopenem/OneRoster.NET` and `jdolny/OneRoster.NET`, both 1,089 d |
| a **live permissive Caliper** implementation | same | 🔴 **0** — and `1EdTech/caliper-java` now 404s because **the consortium announced a move to private repositories**; `1EdTech/caliper-spec` last touched 2019 |
| a **live** permissive **knowledge-tracing / BKT-IRT** library | recency over the mastery tier | ⚠️ `CAHLR/OATutor` is **6 days** old — 🟢 this gap is *not* a recency gap; it remains a breadth gap |
| anything on **LATAM self-hosted forges** (`.edu.br`, `.edu.mx`, `.cl`) | 15 hosts × 3 endpoints | 🔴 **unmeasurable** — 000 on all 45 requests, and a deliberately bogus host also returns 000, so the probe cannot separate "absent" from "egress denied". **No supply conclusion is drawn** |

⚠️ **That last row is recorded so it is not mistaken for coverage.** A channel that cannot
distinguish absence from denial produces no finding in either direction.

---

## Added in the twenty-fourth pass of 2026-10-07 — the interoperability tier re-pointed at its upstreams

⏱️ **Ages against the reference date `2026-10-07`.** Channel: the package registries
(`compose/code/registry-recency-channel/`), plus `git ls-remote` tag enumeration.

**Two rows on this shelf pointed at forks, and both forks were cold.** The rows are re-pointed
above; this section records what replaced them and why the detection generalises.

### The LTI 1.3 shelf, by runtime, both channels

| Runtime | Pick | Licence (payload) | Head commit | Age | Latest release |
|---|---|---|---|---|---|
| **Python / Django** | 🆕 [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 **MIT** (1,098 B) | 2026-10-05 | 🟢 **2 d** | 🟢 [`django-lti`](https://pypi.org/project/django-lti/) **v0.10.1**, 61 d |
| **Python / JupyterHub** | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (1,528 B) | 2026-07-01 | 🟢 98 d | 🟢 v1.6.3, 195 d |
| **Node** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 (11,360 B) | 2026-10-06 | 🟢 **1 d** | 🆕 🟢 npm [`ltijs`](https://www.npmjs.com/package/ltijs) **7.0.7, 2026-10-06 — 1 d** |
| **PHP / Moodle** | 🔁 [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | 🟢 Apache-2.0 (`master/LICENSE.md`, 11,343 B) | 2026-09-23 | 🟢 **14 d** | 🆕 🟢 Packagist [`packbackbooks/lti-1p3-tool`](https://packagist.org/packages/packbackbooks/lti-1p3-tool) **v6.4.4, 2026-09-23 — 14 d**, 68 releases |
| **JVM / Spring Security** | [`oxctl/spring-security-lti13`](https://github.com/oxctl/spring-security-lti13) | 🟢 Apache-2.0 (11,357 B) | 2026-10-06 | 🟢 1 d | 🆕 🟢 Maven Central `uk.ac.ox.ctl:spring-security-lti13` **0.3.7, 2026-10-06 — 1 d**, 23 versions |
| **Elixir** | [`Simon-Initiative/lti_1p3`](https://github.com/Simon-Initiative/lti_1p3) | 🟢 MIT (1,082 B, © Carnegie Mellon University) | 2026-03-13 | 🟢 208 d | 🆕 🟢 Hex [`lti_1p3`](https://hex.pm/packages/lti_1p3) **0.11.0, 2026-03-13 — 208 d** |
| **Python, framework-neutral** | ⚠️ [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) — **alpha, vendors `PyLTI1p3`** | 🟢 MIT, ⚠️ holder `Dmitry Viskov` | 2026-08-05 | ⚠️ 63 d | ⚠️ PyPI [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 — 103 d**, one release |

🆕 **The release column was four dashes until the twenty-fifth pass, and the reason was that this
KB had only ever used two registries.** `pypi.org` and `registry.npmjs.org` serve Python and Node;
the PHP, JVM and Elixir rows had no release channel at all. **Three further registries are
reachable from this environment and were probed for the first time on 2026-10-07:**

| Registry | Endpoint | Status |
|---|---|---|
| **Packagist** (PHP) | `repo.packagist.org/p2/<vendor>/<pkg>.json` | 🟢 200 |
| **Maven Central** (JVM) | `repo1.maven.org/maven2/<group path>/<artifact>/maven-metadata.xml` | 🟢 200 |
| **Hex** (Elixir / Erlang) | `hex.pm/api/packages/<name>` | 🟢 200 |
| RubyGems · Go module proxy | `rubygems.org/api/v1/gems/<n>.json` · `proxy.golang.org/<mod>/@v/list` | 🟢 200, no shelf row needs them yet |
| *(still blocked)* | `api.github.com/repos/*` · rendered `github.com` · `crates.io` | 🔴 403 |

🟢 **Every row on this shelf now agrees across two independent channels**, and on three of the
five rows the head commit and the release are the **same day** — the signature of a maintained
library, and the exact inverse of `pylti1.3`'s 1,416/1,417.

⚠️ **The PHP row carries the lesson that makes the channel usable: the package name is not the
repository name.** `repo.packagist.org/p2/packbackbooks/lti-1-3-php-library.json` is a **404**;
the composer package is **`packbackbooks/lti-1p3-tool`**, and only its own `composer.json` says so.
🔵 **A registry census keyed on repository slugs would have recorded "not published" for a library
with 68 releases.** Read the manifest for the name, then query the registry — never the other way.

🔴 **And the same probe closes the cold-fork case from a third direction.** `1EdTech`'s copy
declares the composer name **`imsglobal/lti-1p3-tool`**, which Packagist **404s**, and its
`composer.json` declares **no licence at all** while the repository ships Apache-2.0. Commit date,
payload identity and now registry presence all agree: the standards body's copy is the dead one.

🔵 **So the "framework-neutral Python" cell is no longer empty, and it is the only row on this
shelf whose two channels disagree in the dangerous direction** — a release 103 days old against a
commit 63 days old, on a project whose own README says three of its five subsystems are unbuilt.
`dmitry-viskov/pylti1.3` remains **1,416 days cold on the commit channel and 1,417 on the release
channel** (`pylti1p3` v2.0.0, 2022-11-20), and `ff-ltitoolkit` **vendors it rather than replacing
it**. The contribution opening is still one protocol binding wide; what changed is that someone
has started, alone, at `0★`.

### 🔴 Rows removed from this shelf, and the reason each was wrong

| Removed | Why |
|---|---|
| `1EdTech/lti-1-3-php-library` | 🔴 Head commit **2020-06-03 — 2,317 d**. It is the standards body's **fork** of `packbackbooks/lti-1-3-php-library`; pass 23 established byte-identical Apache-2.0 payloads (11,343 B) under two composer names. The upstream was committed **14 days** ago. ⚠️ Its **124★** was the fork's audience and is withdrawn rather than transferred |
| `IMSGlobal/LTI-Tool-Provider-Library-PHP` *(was cited by `compose/patterns.md` P1, not by this file)* | 🔴 Head commit **2016-11-28 — 3,600 d**, and its `README.md` states support for **"LTI 1.1 and the unofficial extensions to LTI 1.0"** — **it does not implement LTI 1.3**. ⚠️ `IMSGlobal` became **1EdTech in 2022**, so the org name alone dated it |
| `openedx/openedx-lti-tool-plugin` | 🔴 **The slug does not exist** — `git ls-remote` returns no ref, and PyPI 404s on that name. The real project is **`eduNEXT/openedx-lti-tool-plugin`** (Apache-2.0, 11,357 B) and it is ⚠️ **443 days cold and unpublished to PyPI**, so "available permissive Python option" overstated it |

### 🔵 The licence boundary this tier actually has — read this before quoting the shelf

[`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) is the
**best-maintained Python LTI 1.3 implementation in any language**: head commit **6 d**, released
**6 d** ago as `lti-consumer-xblock` v11.4.2. Its payload is **AGPL-3.0, 34,520 B**.

🟢 Inside an Open edX deployment it is the correct component. 🔴 As reusable Globant IP it is
unusable, which is the premise of **P30**. **State it that way in a bid**: the permissive Python LTI
shelf is not empty, it is *younger and thinner than the copyleft one* — a materially different
sentence from "no Python LTI library exists", which this file asserted for fourteen passes.

### What the installed tier does to this shelf's foundation rows

The 293 depth-1 dependencies of the twelve repositories whose manifests pass 21 resolved were dated
this pass. **30.1% are more than a year old; 13.0% predate 2024; the median is 65 days.** Against
the citing tier's 23.0% / 11.1% / 42 days, **the installed tier is 1.31× colder on the cold bucket**
— the direction pass 23 predicted, at a smaller magnitude than its motivating example implied.

🔴 **Two foundation rows carry the divergence:** `learningequality/kolibri` (head commit 1 d, median
dependency **200 d**, 14/32 cold, including `json-schema-validator` at **3,894 d** and
`zeroconf-py2compat` at 1,156 d — Python-2-era compatibility shims still in the manifest) and
`CAHLR/OATutor` (head commit 7 d, median **604 d**). 🟢 Two read cleanly on both axes:
`towardsai/ai-tutor-app` (median 9 d, **0/20** cold) and `HKUDS/DeepTutor` (median 62 d).

⚠️ **Three licence corrections to the pass-21 closure**, all from the registry classifiers:
`python-dateutil` is **permissive** (Apache-2.0 **and** BSD classifiers) despite a `license` field
reading *"Dual License"*; `semver` is **BSD** despite a field containing the raw notice text; and
🔴 `azure-cognitiveservices-speech`, declared by `oppia/oppia`, is **proprietary** — *"License ::
Other/Proprietary License"*, empty licence field. Full census in `intel/trends.md` §57.

---

## Twenty-fifth pass, 2026-10-07 — the shelf measured whole: 503 slugs, one denominator

Every pass before this one measured a *sample* of the shelf. `p170`'s published denominator is
**200 slugs from 2026-10-03**, and pass 66 left the reservation *"the sweep is redone when
`slugs.input.txt` incorporates this pass's additions"* standing. It stood for twenty-four passes.

🔵 **The denominator this pass uses is every `github.com/owner/repo` cited in the six
non-append-only shelf files: 503 slugs. Only 62 of them are in `p170`'s 200. 441 had never been
measured.** Instrument: `compose/code/p436-fork-hypothesis/` (6 controls, offline).

| Layer | Result |
|---|---|
| licence payload, `raw.githubusercontent.com/<slug>/HEAD/<14 filenames>` | 412 `LICENSED` · 87 `UNLICENSED` · 4 `UNREACHABLE` |
| head commit date, `git fetch --depth 1 --filter=blob:none` | 🟢 **501 of 503 dated** |
| licence family | MIT 215 · Apache-2.0 72 · GPL 40 · AGPL-3.0 23 · LGPL 11 · BSD 10 · ECL-2.0 8 · CC-BY 7 · ISC 2 · CC0 2 · unclassified 22 |

### Liveness of the live-cited shelf, against the reference date `2026-10-07`

| | 503-slug live shelf | pass 24's 884-repo citing tier |
|---|---|---|
| median head-commit age | **48 d** | 42 d |
| committed in 2026 | 72.3% | 73.5% |
| 🔴 cold > 1 yr | **24.8%** | 23.0% |
| 🔴 cold > 2 yr | **16.6%** | 11.1% (pre-2024) |
| committed within 7 d | 31.5% | — |

⚠️ **Read the first comparison, not the headline.** You would expect what a KB *recommends* to be
fresher than what it merely *mentions*. **Measured, it is not** — the live shelf is 48 d against
42 d, and colder on both cold buckets. Nothing in this KB's selection process favours recency, and
this is the number that says so.

🔴 **The 25 coldest rows the KB still cites**, led by `foradian/fedena` **5,108 d (2012-10-12)**,
`inepdadosabertos/api` 4,525 d, `Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor`
3,808 d, `shinyquagsire23/InfiniteCampusAPI` 3,658 d,
`IMSGlobal/LTI-Tool-Provider-Library-PHP` 3,600 d (the row pass 24 removed from **P1**),
`kuali/kc` 3,561 d, `fnshr/kyo-kan` 3,518 d, `kuali/rice` 3,430 d. Full table:
`compose/code/p436-fork-hypothesis/recency.2026-10-07.tsv`.

### 🔴 Six rows on this shelf are cited at a repository's FORMER name

A GitHub rename or transfer leaves the old path working as a redirect, so nothing in a browser
shows that anything has moved. The discriminator costs one call and is exact:
`git ls-remote <old> HEAD == git ls-remote <new> HEAD` ⇒ **one repository, two names**. Found by
asking each repo's **package registry** which repository it declares as its homepage, then
comparing heads.

| Cited here as | The registry declares | Shared head | Direction |
|---|---|---|---|
| [`All-Hands-AI/OpenHands`](https://github.com/All-Hands-AI/OpenHands) | `OpenHands/OpenHands` | `9f05599` | 🔴 the project moved; the KB has the old name |
| [`NVIDIA/NeMo`](https://github.com/NVIDIA/NeMo) | `NVIDIA-NeMo/NeMo` | `50c71db` | 🔴 same |
| [`iterative/dvc`](https://github.com/iterative/dvc) | `treeverse/dvc` | `56e5982` | 🔴 same — and this one is a **transfer between companies**, not a rename |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | `TryxAPI/lrs-conformance-tests` | `5bc232d` | 🔴 same |
| [`stanfordnlp/edu-convokit`](https://github.com/stanfordnlp/edu-convokit) | `rosewang2008/edu-convokit` | `d845ffd` | ⚠️ one repository under two names, **537 d cold either way** |
| [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | `IMSGlobal/openbadges-validator-core` | `0a66b52` | 🟢 **the reverse** — the KB has the post-2022 name and the **registry metadata is stale** |

🔵 **The last row is why this is a channel and not a rule.** Five times the KB was behind the
repository; once the registry was behind the KB. **The head SHA settles it; neither source is
authoritative on its own.** The names are left as published above with a pointer, because both
paths resolve and rewriting a working citation buys nothing — what was missing was the note.

### 🔴 Seven MIT licence files on this shelf name no copyright holder at all

Under **P179**, a licence file is an *identifier* or a *cession*: a cession names a grantor, a year
and the terms. These seven are MIT texts with the terms and **no grantor**:

| Slug | What the copyright line says |
|---|---|
| [`AbdelStark/eu-ai-act-toolkit`](https://github.com/AbdelStark/eu-ai-act-toolkit) | `Copyright (c) 2026` — a year and nothing else |
| [`AkizumiFox/NTU-COOL-Assignment-Status-Viewer`](https://github.com/AkizumiFox/NTU-COOL-Assignment-Status-Viewer) | `Copyright (c) 2025` — same |
| [`koukekoukej-glitch/feynman-tutor`](https://github.com/koukekoukej-glitch/feynman-tutor) | `Copyright (c) 2026` — same |
| [`r1ckyIn/canvas-ed-mcp`](https://github.com/r1ckyIn/canvas-ed-mcp) | `Copyright (c) 2025` — same |
| [`lebmatter/exampro`](https://github.com/lebmatter/exampro) | 🔴 `Copyright (c) [year] [fullname]` — **the template placeholder, shipped verbatim** |
| [`nguyentrieu210/edu`](https://github.com/nguyentrieu210/edu) | 🔴 same placeholder |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | the copyright line is **absent** |

⚠️ **This is a weaker defect than a wrong licence and a real one.** The MIT grant text is present
and unambiguous in all seven; what is missing is the party making the grant. For a client
redistribution review that is a question someone has to answer, and the repository does not.
🔵 **`adlnet/lrs-conformance-test-suite` is the one to care about** — ADL's xAPI conformance suite
is a standards artefact an engagement cites in a bid, and it is the one with no copyright line.

🔴 **The KB could not see any of this until this pass, because its own instrument could not return
the class.** `p184`'s copyright regex used `\s*` between the word *copyright* and the capture;
`\s` matches a newline, so `Copyright (c) 2026` followed by a blank line **reached across it and
published the next paragraph of the licence as the holder**. All seven were filed as
`HOLDER-UNRELATED` with a sentence of MIT boilerplate in the holder column. Fixed with four new
controls — three negatives and the positive that forbids an instrument answering `NO-HOLDER`
always — in `compose/code/p184-holder-mismatch/` (now 19/19).

## Nine repositories this shelf had written off have their own grant — found by enumerating the tree, 2026-10-07

Pass 25's licence probe used **14 filenames at the repository root** and published **87** slugs as
shipping no licence. `p441` replaces the filename list with a complete tree enumeration — a
`--filter=blob:none --no-checkout --depth 1` clone plus `git ls-tree -r`, which lists every path at
HEAD with no API and no truncation, in **13 seconds for all 87**:

| Instrument | Grants found in the 87 |
|---|---|
| 14 filenames, rooted (`p436`) | **0** |
| 41 filenames, rooted (`p440/widen.py`) | 1 |
| 🟢 complete tree enumeration (`p441`) | 🟢 **9** |

| Repo | Licence | Where it actually is | The axis a filename list cannot reach |
|---|---|---|---|
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | `LICENSE.TXT` | **extension case** |
| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | **MIT** | `License` | **a third capitalisation** |
| [`nvaccess/nvda`](https://github.com/nvaccess/nvda) | **GPL-2.0-or-later with two exceptions** | `copying.txt` | **lowercase `COPYING`**, which the probe list carries only in uppercase |
| [`veraPDF/veraPDF-library`](https://github.com/veraPDF/veraPDF-library) | ⚠️ **GPL-3.0 + MPL-2.0**, dual | `LICENSE.GPL` **and** `LICENSE.MPL` | **family suffix** — two grants cannot both live in a file called `LICENSE` |
| [`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) | 🟡 **EUPL-1.2** | `aoe-web-backend/LICENSE` · `aoe-web-frontend/LICENSE`, 303 B each | **depth** |
| [`cs341-illinois/coursebook`](https://github.com/cs341-illinois/coursebook) | 🔴 **NCSA** (code — *not* MIT, corrected in the twenty-seventh pass) **+ CC-BY-4.0** (content, output) | `LICENSE/LICENSE.code` · `LICENSE.original` · `LICENSE.output` | **a licence DIRECTORY holding three grants** |
| [`learningequality/kolibri-server`](https://github.com/learningequality/kolibri-server) | **GPL** | `debian/copyright` | **the Debian packaging convention** |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) · [`OS4ED/openSIS-Responsive-Design`](https://github.com/OS4ED/openSIS-Responsive-Design) | 🔴 **unread — RTF** | `docs/License.txt` plus a `docs/LICENSE.rtf` the classifier cannot read | **format**, which is a limit and not an absence |

🔵 **[`cs341-illinois/coursebook`](https://github.com/cs341-illinois/coursebook) is the row that makes
the whole case.** Separate grants for the **code** (**NCSA** — corrected in the twenty-seventh pass from MIT; the
University of Illinois/NCSA licence quotes MIT's grant sentence verbatim, so a classifier probing
for that sentence returns MIT), the **original content** and the **output**
(CC-BY-4.0) is the *correct* structure for a course repository, and it is the structure a single `LICENSE`
file cannot express. A rooted filename probe therefore reports a teaching repository with exemplary
licensing hygiene as having none at all. For a client who wants a course scaffold whose content and
code licences are separable — which is what every corporate-academy engagement needs — this is the
shape to copy.

⚠️ **`nvaccess/nvda` is GPL-2.0-or-later *with two special exceptions*, and the exceptions are the
point.** The grant is not a plain GPL row: `copying.txt` opens *"NVDA is available under the GNU
General Public License version 2 or later, with two special exceptions"*, one of which permits linking
with certain non-GPL code. 🔴 **This KB's family classifier returns `LGPL` for that payload**, because
the exception text names the LGPL — see the limit recorded in trend 62. **Read the file before quoting
a verdict on NVDA**; it is the screen reader every accessibility engagement in the EMEA public sector
will meet, and "GPL" and "GPL with a linking exception" are different answers to a client's question.

### 🟡 The EUPL tier was machine-unreadable in this KB until this pass

[`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) is one of **eight Finnish national
education services** this shelf already lists under **EUPL-1.1 or EUPL-1.2** — `eperusteet`, `koski`,
`ataru`, `organisaatio`, `oppijanumerorekisteri`, `ehoks`, `suorituspalvelu` and `aoe`. Nine of this
KB's files discuss the EUPL in prose. 🔴 **And both of its licence classifiers returned `UNKNOWN` for
the string**, so the single tier a European public-sector engagement starts from was invisible to every
automated check this repository runs.

Both now recognise it, classified **STRONG-COPYLEFT**, with six controls:

- 🔴 **Article 5 carries a copyleft obligation, and Article 1's definition of "Communication" covers
  network use** — so the EUPL binds a **hosted service**, not only a shipped binary. For a SaaS
  deliverable built on an EUPL component that is the clause that decides the engagement.
- ⚠️ **EUPL-1.2's Appendix lists GPL-2.0, AGPL-3.0, LGPL-2.1, MPL-2.0 and EPL-1.0 as compatible
  licences**, which is a **re-licensing option for derivative works** and not a softening of the EUPL
  itself. Nothing in this KB treats it as one.
- 🔵 The Appendix is also why the classifier has to probe EUPL **first**: an EUPL payload carries the
  marks of five other families, exactly as an MPL-2.0 payload carries three GNU marks.
- 🟢 **Commercially it is workable and it is the licence the European Commission recommends for
  public-sector software**, so an EMEA public-sector engagement should expect it rather than treat it
  as an exception.

### 🔴 Five MPL-2.0 repositories were filed as GPL by this KB's own instrument, while its prose had them right

`p436`'s family classifier probed the GNU family before Mozilla's. MPL-2.0 **section 1.12** defines
*"Secondary License"* by naming the GNU **GPL-2.0, LGPL-2.1 and AGPL-3.0**, so every MPL-2.0 payload
carries all three marks:

| Repo | Filed | Actually, from the first line of its payload |
|---|---|---|
| [`dequelabs/axe-core`](https://github.com/dequelabs/axe-core) | GPL | **MPL-2.0** |
| [`ocrmypdf/OCRmyPDF`](https://github.com/ocrmypdf/OCRmyPDF) | GPL | **MPL-2.0** |
| [`coqui-ai/TTS`](https://github.com/coqui-ai/TTS) | GPL | **MPL-2.0** |
| [`idiap/coqui-ai-TTS`](https://github.com/idiap/coqui-ai-TTS) | GPL | **MPL-2.0** |
| [`edrys-org/edrys`](https://github.com/edrys-org/edrys) | GPL | **MPL-2.0** |

🟢 **Every one of the five is already described correctly as MPL-2.0 in this file and in
`agents/top.md`** — the prose was right and the measurement was wrong, which is trend 61. 🔴 **The
commercial verdict inverts between the two answers:** GPL is strong copyleft and a blocker for a
client deliverable; MPL-2.0 is **file-level** copyleft, so using the component unmodified as a
dependency does not reach the studio's own files. **Four of the five are tools a studio would reach
for** — `axe-core` is the engine inside every MIT accessibility agent on this shelf, and this KB's own
`a11ymcp` row declares it at runtime.

🔵 **The symptom needed no fetch: the published family distribution over 412 licensed payloads
contained ZERO MPL-2.0 rows.** Fixed by probing EUPL, then MPL and EPL, before the GNU family, with
**15 controls** that pair each positive against a GNU payload which must not move.

## Added in the twenty-ninth pass of 2026-10-07 — corrections to the licence column, and the EUPL tier gains a version

No new foundational layers. What changed is the **licence column on layers this page already
recommends** — and here a wrong licence is worse than a missing row, because these are the
pieces a client build links against.

🔵 **All of it came from one file pass 28 never opened.** Pass 28 repaired three defect
classes in `sweep_payload.family_of`. `lib/license_family.sh` — the **shared** classifier,
sourced by 27 instruments — still carried all three.

### 🟢 Five repositories are MPL-2.0, not GPL

| Repo | published | 🟢 corrected | Layer |
|---|---|---|---|
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | `GPL-3.0` | **MPL-2.0** | accessibility testing |
| [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | `GPL-3.0` | **MPL-2.0** | document ingestion |
| [coqui-ai/TTS](https://github.com/coqui-ai/TTS) | `GPL-3.0` | **MPL-2.0** | speech synthesis |
| [idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) | `GPL-3.0` | **MPL-2.0** | speech synthesis (maintained fork) |
| [edrys-org/edrys](https://github.com/edrys-org/edrys) | `GPL-3.0` | **MPL-2.0** | live classroom |

🔴 **The cause, and this is the second time this KB has paid for it.** MPL-2.0 **§1.12**
defines *"Secondary License"* by naming *"the GNU General Public License, Version 2.0, the
GNU Lesser General Public License, Version 2.1, the GNU Affero General Public License,
Version 3.0"* — so **every MPL-2.0 payload carries all three GNU marks**, and a classifier
probing the GNU family first takes the payload.

⚠️ **Pass 26 measured this, named these exact five repositories, fixed it, and wrote it up —
in the other classifier.** Three passes later the identical defect sat in
`lib/license_family.sh`, on the same five rows. `P237` said a correction living in prose is
not a control. `P454` adds: **a correction living in one of two implementations is not one
either.**

🟢 **Why it matters for selection, not bookkeeping.** MPL-2.0 is **file-level** copyleft: you
may link it into a proprietary application and must publish changes only to the MPL files.
GPL-3.0 is **project-level**. Recorded as GPL, all five looked like they would infect a
client deliverable; they do not. **Two of the five are the TTS layer**, so the speech
substrate this KB recommends for offline and mother-tongue tutoring was marked unusable and
is not.

### 🟢 The EUPL public-sector tier now resolves to a version — and it is mostly 1.1

`lib/license_family.sh` had **no EUPL branch at all** before this pass (`P453`), so all nine
EUPL payloads read `UNCLASSIFIED` from it. They now resolve, with the version:

| Repo | 🟢 family | Region | Country |
|---|---|---|---|
| [Opetushallitus/ehoks](https://github.com/Opetushallitus/ehoks) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/eperusteet](https://github.com/Opetushallitus/eperusteet) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/koski](https://github.com/Opetushallitus/koski) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/oppijanumerorekisteri](https://github.com/Opetushallitus/oppijanumerorekisteri) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/organisaatio](https://github.com/Opetushallitus/organisaatio) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/valtionavustus](https://github.com/Opetushallitus/valtionavustus) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/ataru](https://github.com/Opetushallitus/ataru) | **EUPL-1.2** | EMEA | Finland |
| [Opetushallitus/suorituspalvelu](https://github.com/Opetushallitus/suorituspalvelu) | **EUPL-1.2** | EMEA | Finland |
| [european-commission-empl/European-Learning-Model](https://github.com/european-commission-empl/European-Learning-Model) | **EUPL-1.2** | EMEA | EU |

⚠️ **Read this before building on the tier: six of nine are EUPL-1.1, not 1.2.** The two
versions carry **different compatibility lists** — 1.2's Appendix adds licences 1.1's does
not — so a build composing this tier with GPL, MPL or EPL components cannot treat the `EUPL`
label as uniform. Resolve the version per repository, which is now possible.

🔵 **Both of the tier's shapes need covering.** The eight Finnish services carry **no licence
title at all**: they open on a copyright line and concede in prose — *"Licensed under the
EUPL, Version 1.1 or — as soon as they will be approved by the European Commission —
subsequent versions"*. Only the Commission's own payload ships the full licence text with the
name as a title. A title probe alone misses eight of nine; a grant-phrase probe alone misses
the one that matters most.

🔴 **The consequence nobody had stated.** With the family `UNCLASSIFIED`, `P250`'s gate never
fired on these nine, so their **commercial-use verdict came from the body token match**
rather than from an identified family — the route `P171` declares unsafe. The answer it gave
is right (**the EUPL permits commercial use**), but it was right **by luck**, across the whole
EMEA public-sector tier, for every pass before this one.

### 🔴 And one correction where the grant is not in the root at all

| Repo | published | 🟢 corrected | Where the grant actually is |
|---|---|---|---|
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | `LGPL?` | **GPL-2.0** | `docs/License.txt`, 17,286 B — **no root licence exists** |
| [OS4ED/openSIS-Responsive-Design](https://github.com/OS4ED/openSIS-Responsive-Design) | `LGPL?` | **GPL-2.0** | same |

Neither appears among the 412 root payloads this shelf sweeps. They are the clearest case on
this page for why `p441`'s tree enumeration exists: **for these two the subtree is the only
licence evidence there is**, and until this pass the family read from it was wrong.

### ⚠️ One layer still unreadable by the Python classifier, declared not patched

[opendatalab/MinerU](https://github.com/opendatalab/MinerU) — the PDF/document → structured
text layer under curriculum parsing — answers **Apache-2.0** from the shell and `UNKNOWN`
from `sweep_payload.family_of`. Its `LICENSE.md` says *"MinerU is licensed under Apache
License 2.0"*, naming licence and version in one token, and the Python probe requires a
separate `"version 2.0"` string, so every **prose** declaration of Apache is excluded. The
row on this page is **Apache-2.0** and correct; the instrument disagrees, and the fix is
pre-registered rather than applied to a file pass 28 rewrote hours earlier.

## Added in the thirty-first pass, 2026-10-07 — the DIKSHA service tier

| Repo | Licence (read from payload) | ★ | Region | Why it is foundational |
|---|---|---|---|---|
| [`project-sunbird/sunbird-lms-service`](https://github.com/project-sunbird/sunbird-lms-service) | **MIT** (`master/LICENSE`, "Copyright (c) 2018 Project Sunbird") | not read this pass | APAC | The LMS service tier of **Sunbird**, India's education digital public infrastructure and the stack behind **DIKSHA** — national-scale, and **MIT**, which is rare at this scale in public-sector education. With `Sunbird-Ed/SunbirdEd-portal` (MIT, already shelved) this gives a licence-clean LMS core to put agents on top of, rather than retrofitting Moodle's GPL-3.0 tree. |
| [`bojieli/ai-agent-book`](https://github.com/bojieli/ai-agent-book) | **Apache-2.0** (`main/LICENSE`) | not read this pass | APAC | Redistributable agent-engineering curriculum — the enablement layer of an engagement, usable in client-facing training material because Apache-2.0 permits it. |

⚠️ **Not added, and why.** [`pawtograder/platform`](https://github.com/pawtograder/platform) is the
most architecturally interesting thing found this pass (MCP server over a real gradebook) but is
**GPL-3.0-or-later** — it belongs in `agents/top.md` with a copyleft flag, not in a foundations shelf
that implies a proprietary-safe base. `datawhalechina/hello-agents` is **CC BY-NC-SA 4.0** and
`a5anka/ai-lab-2026-africa-agent-manager` carries **no licence file**; neither is a foundation.

Verification: licence payloads over `raw.githubusercontent.com`, 404 negative control run in the same
pass. `curl -sI github.com` is 403 via this session's proxy; `api.github.com` is 403, so no star
counts were read.
