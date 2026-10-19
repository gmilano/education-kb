---
industry: education
region: Global
updated: 2026-10-19
---

# Foundational repos — education

## Pass 326 · 2026-10-19 (twelfth pass of this date) — fifty-eight rows, and the first of them is not code

**Two rows added — fifty-eight total. Both licences read first-hand on the `raw` channel over the
seven-filename probe space across both candidate branch names.** 🟢 **The headline row is the
largest open artefact this KB has found in the education sector that is not a model or a
framework: `withmarbleapp/os-taxonomy`, 6.1 ★k, 998 forks, 23 commits — a curriculum prerequisite
graph with no code in it at all.**

🔵 **It is in *this* file rather than only in `agents/top.md` because it is the layer everything
else in this KB sits on top of.** Every pattern in `compose/patterns.md` from P1 onward assumes a
client supplies a curriculum spine. **P10 was written because exactly one existed and it covered
one country.** This one covers **seven curricula across the UK, the US and the IB**, and unlike
`cn-math-taxonomy` (CC BY-NC) it can enter a commercial deliverable.

### What was measured, and how

**Licence, first-hand:** `main/LICENSE` and `master/LICENSE` both return 200; the file is **25,289
bytes of genuine Open Data Commons ODbL 1.0 text** (`LICENSE.md`, `LICENSE.txt`, `COPYING` all
404 on both branches — the seven-name probe space is still not optional). The README declares the
split: **ODbL-1.0 for the database** (collection, structure, IDs, relationships) and **CC BY-SA
4.0 for Marble-authored text** (names, descriptions, evidence, prompts, dependency reasons,
cluster summaries). The GitHub sidebar agrees: *"ODbL-1.0, CC-BY-SA-4.0 licenses found."*

**Integrity, first-hand:** `data/manifest.json` carries a SHA-256 per shipped file.
`topics.json` fetched this pass hashes to
`5aa40906ed0095c8af49c8bc2827fa3f10e214892563ea4156c6cde32f9b7e9d` — **the manifest's exact
value.** 🟢 **This is the first dataset in this KB whose contents can be verified against its own
published checksums, and it is the single cheapest thing to ask of every other curriculum
artefact here.**

**Freshness, first-hand, and it corrects every secondary description of this repo in circulation:**
`manifest.generatedAt` is **`2026-10-19T17:32:15.492Z`** — regenerated today. Every roundup and
mirror describing this dataset reports **1,590 topics and 3,221 edges** from the July v1
announcement. **The file as shipped today is 1,591 and 3,225.** 🔵 **Small drift, but it is the
reason this KB pins releases and records checksums rather than quoting a blog: a curriculum that
moves silently under a tutor is a correctness incident, and this one moves.**

### The rows

| Repo | Licence | ★ | Checked | Layer | Why it is foundational |
|---|---|---|---|---|---|
| https://github.com/withmarbleapp/os-taxonomy | 🟢 **ODbL-1.0 (database) + CC BY-SA 4.0 (text)** — `LICENSE` read first-hand on both branches, 25,289 bytes of genuine ODbL text; sidebar agrees. 🔵 **Share-alike, and still commercial**: ODbL binds a *derivative database*, not a *produced work*, so a product built on the graph stays yours. 🔴 `data/curriculum-standards.json` is **not Marble's to relicense** — per-source terms in `PROVENANCE.md` | 6.1k | p326 | **Curriculum data — the spine every pattern in this KB assumed a client would supply** | **1,591 micro-topics, 3,225 prerequisite edges (2,030 hard / 1,195 soft, 100% carrying a prose reason), ages 4–15, eight subjects, 2,189 links into 3,261 standards from seven curricula** (UK NC 2013, CCSS ELA, CCSS Math, NGSS K-5, NGSS MS, C3 Social Studies, IB PYP PSPE). Every topic carries an `assessmentPrompt`; 1,556 carry observable `evidence` descriptors. Ships SHA-256 per file. Separate 23.5 MB `teaching-research.json` covering 1,051 topics — **and naming the 540 it does not cover.** 998 forks, 23 commits, v1 public since 2026-07-08 · **Use it for:** the prerequisite ordering, the age banding and the mastery checks under any tutor; and as the **AI-literacy curriculum** — the entire `Computing` subject is 21 AI topics for ages 5–11 |
| https://github.com/tbh-23/Homestead | 🟢 **MIT** — `LICENSE` read first-hand, *MIT License, `Copyright (c) 2026 Homestead`*, 1,573 bytes. Curriculum data stays under its own ODbL/CC BY-SA terms and is **not vendored** | 15 | p326 | **Reference consumer — the licence boundary, implemented** | **The worked example of how to build a proprietary product on a share-alike dataset.** Fetches `os-taxonomy` from upstream at runtime, caches it outside the repository, and **notifies on upstream topic additions and removals**; the README instructs that the dataset must not be committed. 90%+ mastery gate, independently re-solved mastery tests, Leitner spaced repetition, spaced retry, AI coach grounded in learner progress. 41 commits, 2 forks · **Use it for:** **P13** — and read its attribution string, which is the one ODbL and CC BY-SA actually require |

🔴 **The one thing to check before quoting standard text in a bid.** Four of the seven curricula
ship **codes only** — `ngss-k5`, `ngss-ms`, `c3-social-studies`, `ib-pyp-pspe` — because their
upstream terms do not permit redistribution. **UK NC 2013 ships in full under OGL v3**
(commercial, no share-alike, fixed attribution notice). **Common Core ships in full but remains
under the purpose-limited CCSS Public License**, which does not clearly grant derivative or
sublicensing rights — **so the CCSS records are not ODbL even though they sit in an ODbL
database.** **NGSS is a registered WestEd trademark and commercial use carries a sample-approval
requirement.** The topic→standard links are unaffected throughout.

## Pass 325 · 2026-10-19 (eleventh pass of this date) — fifty-six rows, and the eight that were here all along

**Eight rows added — fifty-six total. Every licence below was read first-hand on the `raw` channel
this pass, over the seven-filename probe space, across five candidate branch names.** 🟢 **Six of
the eight are a promotion, not a discovery, and saying so is the point.** The
**France Université Numérique / FUN-MOOC** stack — the operator of France's national public MOOC
platform — has been measured in `repos/trending.md` since **p127**, re-measured at **p190**,
**p208**, **p212** and **p256**, and **never once carried into this file.** Only `openfun/richie`
ever made it here. **`ralph`, `warren`, `potsie`, `joanie`, `django-lti-toolbox` and `ashley` were
held and unusable, because a row in an append-only history is not a row in a curated starting-point
list.** They are here now, re-verified.

🟢 **And the licence shape of that stack is the exact mirror of p322's, which makes a trend out of
what looked like a one-off.** At **openeduhub** (Germany, publicly funded) p322 found licences
dividing **by architectural layer**: permissive shells, GPL analysers, **an unlicensed inference
core**. At **FUN-MOOC** (France, publicly funded) this pass found **MIT on every layer there is** —
portal CMS, headless ERP, forum, Learning Record Store, analytics viz, Grafana dashboards, LTI
toolkit — with **AGPL-3.0 appearing exactly once, on `openedx-docker`, where it is inherited from
Open edX rather than chosen.** Two publicly funded European education operators; opposite licence
hygiene. **FUN publishes a `handbook` repository of engineering practice and openeduhub does not.**
🔵 **The conclusion for a procurement conversation: public funding does not predict a licence
posture. The operator's engineering maturity does** — and that is observable before you sign, from
the org's own repositories. Full entry in `intel/trends.md`.

🔴 **The caveat that keeps this from being a clean win, stated with the rows:** `warren` says of
itself *"This project is a Proof Of Concept not suitable for production yet"*, and
`django-lti-toolbox` has **no release and has not been pushed since 2024-11-14**. **The spine is
real; two of its seven segments are not load-bearing.** Use `ralph` + `potsie` (Grafana) for the
analytics path and treat `warren` as a reference implementation.

**Two further rows come from outside Europe and one is a new country for this KB:**
**`muhammedalakbarli/imparo`** (MIT, Azerbaijan — grades 1–8, a **154-skill graph** with per-skill
mastery and spaced repetition) and **`LucasSpinola/assistentes-educacionais-com-ia`** (MIT, Brazil,
pt-BR). 🔵 **The Brazilian row is a finding about the channel, not the artefact: LATAM supply
arrived this pass as a *curriculum for building* educational assistants — NLP → LLM → RAG → agents →
learning analytics, free and open — rather than as a product.** That is the third pass in a row in
which the code channel placed a region the policy channel could not.

🟡 **One repair, content-preserving and worth recording because it was invisible:** the three
curriculum-graph rows added at p323 (`haolpku/K12-KGraph`, `razi-03/NCERT-CKG`,
`mizcausevic-dev/curriculum-knowledge-graph`) carried **seven cells in a six-column table** — the
description and the *Use it for* guidance were written as separate cells, so every value after
column five rendered one column to the right. **Merged onto this file's `· **Use it for:**`
convention; no claim altered.** 🔵 A malformed row in a table a compiler reads is a silently wrong
entity, which is the same failure class as a header row left as data.

🔴 **Rejected, recorded so it is not mistaken for supply:** `010Ankushsharma/AdaptaLearn` — DKVMN
knowledge tracing with PPO and a claim of **131M+ interactions** of training data — carries **no
licence file** on the full probe and no way to verify the claim from the repository.


## Pass 324 · 2026-10-19 — ten rows, the integrity tier, and a licence file that is not the grant

**Pass 324 · 2026-10-19 (tenth pass of this date). Forty-eight repos — ten added, all ten measured
first-hand.** Two findings and one closed list. 🟢 **The first finding closes a gap this KB
declared for seven passes**: `intel/trends.md` trend 9 said there was *"no credible open source
AI-detection or academic-integrity project … plus MOSS-style code-plagiarism detectors."* **The
largest of those "MOSS-style" detectors is `jplag/JPlag` — GPL-3.0, 2.0k ★, 376 forks, 5,708
commits, twenty-odd languages, usable as a Java API — which is more maintained than any agent on
these shelves and was never listed.** With it come `NoplagLabs/noplag-engine` (**Apache-2.0**, 86 ★,
winnowing fingerprints in GIN-indexed PostgreSQL) and `thu-cs-lab/jieplag` (**MIT**, 54 ★, Rust).
The gap was a query artefact: the topic `plagiarism-detection` returns what *AI detection* never
did. 🔴 **The second finding runs opposite to every licence defect in this file so far.**
`ZhijieXiong/pyedmine` — the broadest educational-data-mining library this KB has measured, **28
knowledge-tracing models plus cognitive diagnosis, exercise recommendation and learning-path
recommendation over 14 datasets** — ships **the MIT text in `LICENSE`, under someone else's
copyright line (`Stanford Future Data Systems`), while its README says *"All data and code in this
project may be used only for academic purposes."*** Every previous instance here was a README
claiming a grant the repository lacked; **this is the documented grant being narrower than the
licensed one, which is the direction a dependency scanner cannot catch.** 🟢 **And p322's list of
six named-unread `openeduhub` repositories is closed: all six measured.** The two it said to read
first — `its-prep` and `its-data`, the ones `python-kidra` depends on — **both have no licence file
under any of seven candidate names**, as do `topic-statistics` and, on **both** channels,
`oeh-search-frontend`. `mappings` is GPL-3.0 and `skohub-vocabs-oeh-patched` is Apache-2.0.

🔴 **What that does to p322's licence-by-layer reading: the unlicensed set is not the "inference
core", it is the whole substrate plus the UI.** Gateway, models, data loader, token filter **and
the public Angular search frontend** carry no grant. **A studio cannot lawfully reuse any part of
this stack from the search box down to the tokeniser.** And the thinnest shell in the organisation
is the one with no grant on either channel, where the layer rule predicted Apache-2.0 — **so the
layer rule holds for the backend tiers and does not generalise to the UI tier.**

**Licence split recounted over 48, by classifying each row's own licence cell** (rule stated so it
can be re-run: *a README claim with no file in the repository counts as no licence*): 🔴 **no
licence at all (12)**, MIT (11), Apache-2.0 (10), 🟡 GPL-3.0 (6), permissive code with CC BY 4.0
data or content (4), BSD-3-Clause (2), CC0-1.0 (1), MIT code with CC BY-NC-SA 4.0 data (1), and
🔴 **the new shape — MIT file contradicted by an academic-use-only README (1, `pyedmine`)**. The
categories sum to 48. **So 32/48 are usable as software, 12/48 carry no grant at all, and 4/48 are
usable only under a restriction that bites somewhere a scanner does not look.**

**The licence lesson, third shape in three passes.** p322: licences divide **by architectural
layer** across an organisation. p323: **by artefact type** inside a repository — MIT code,
NonCommercial data. p324: **by channel inside a repository, with the restrictive channel being the
prose one** — the file says MIT and the README says academic-only. The first two reduce to
*permissive at the edges, restricted at whatever took the work*. **The third does not reduce to
anything reassuring: it means the licence file is not sufficient evidence of the grant, in either
direction**, and the only safe reading of a repository is every channel it publishes.

**Pass 323 · 2026-10-19 (ninth pass of this date). Thirty-eight repos — three added, all three read
first-hand.** The three are one finding and two corrections. **The finding — `haolpku/K12-KGraph`,
420 ★, NeurIPS 2026 Evaluations & Datasets Track — makes `intel/trends.md` trend 12's headline
wrong.** That trend has said since p319 that *"exactly one country has built"* verified
curriculum-standard data. **Two have.** China's PEP K-12 curriculum now exists as an
evidence-linked knowledge graph with 12 expert annotators at Fleiss' κ = 0.84, a 23,640-question
benchmark and three released checkpoints — **and its data is CC BY-NC-SA 4.0 while its code is
MIT.** Brazil's `bncc-dev` stays the only verified national curriculum whose **data** Globant can
put in a client deliverable. The corrections: **`razi-03/NCERT-CKG`** makes India's gap contested
rather than empty (and has no licence), and **`tsugiproject/tsugi`'s** two-pass open question is
closed with *the repository does not say*. **Licence split over 38: MIT (10), Apache-2.0 (9),
🔴 no licence at all (8), MIT-code-with-CC-BY-4.0-data or -content (4), GPL-3.0 (4),
BSD-3-Clause (2), CC0-1.0 (1), and one README-claims-MIT-with-no-file (`metadata-agent-api`) —
plus the new split shape, **MIT code with CC BY-NC-SA 4.0 data (1 — K12-KGraph)**, which is the
first NonCommercial data licence in this file. So **29/38 are usable as software, 8/38 carry no
grant, and one is usable only as a method.**

**The licence shape is the transferable lesson, and it pairs with p322's.** p322 found licences
dividing **by architectural layer** across one organisation: permissive shells, GPL analysers,
unlicensed inference core. This pass found them dividing **by artefact type** inside one
repository: MIT code, NonCommercial data. **Both reduce to one sentence — permissive at the edges,
restricted at whatever actually took the work.** In Germany that was the inference core; in China
it is the curriculum itself. **A sidebar badge answers neither case**, which is why this file reads
licences off the repository and now has to read them off the README's licence *section* too.

**Pass 322 · 2026-10-19 (eighth pass of this date). Thirty-five repos — twelve added, all sixteen
reads first-hand, all from one organisation.** Pass 321 named six `openeduhub` repositories it had
not read and declared 57 of 67 unenumerated. **This pass enumerated all sixty-seven and read every
AI-era repository in the org.** The twelve rows below are Germany's publicly funded OER metadata
pipeline, service by service, with the licence of each read off the repository rather than the
README — because in this organisation those disagree four times. The structural finding, and the
reason this matters more than any single row, is in the section *"The inference core is the
unlicensed part"* below. **Licence split over 35: MIT (9), Apache-2.0 (8), 🔴 no licence at all (6),
MIT-code-with-CC-BY-4.0-data or -content (4), GPL-3.0 (4), BSD-3-Clause (2), CC0-1.0 (1), and one
repository whose README claims MIT with no licence file behind it (`metadata-agent-api`) — so
28/35 are usable and 6/35 carry no grant.** The p320 line reading "Licence split over 21" below is
superseded by this count; it was already stale by two rows when p322 opened the file.


**Pass 320 · 2026-10-19 (sixth pass of this date). Twenty-one repos** — one added, and it is the
only substantive addition anywhere in this KB this pass. **`adamzammit/LTIPlugin` is the first
artefact this KB has found at the grade-passback seam that carries an OSI-approved licence**
(GPL-3.0) rather than no licence at all; read the row's caveats before scoping it, because it is
not an AI tool and probably not LTI 1.3. The method constraint was **re-tested rather than
inherited** this pass and reproduces exactly: github.com is the only reachable origin, and
`www.future-ed.org`, `www.lw.com` and `www.iesalc.unesco.org` each failed at DNS when attempted
directly.

**Pass 319 · 2026-10-19.** Twenty repos. "Foundational" here means: you would put it *under* an
education product, not ship it as the product. **Checked** says which pass took the licence/star
reading.

**Pass 319 is the largest single addition this file has had, and the find of the pass is Brazilian.**
The `bncc-dev` stack — a character-verified machine-readable national curriculum, an MCP server over
it, and a benchmark that measures what grounding on it is worth — is the artefact every pattern in
this KB has assumed a client would supply. **It exists in exactly one country, it has 22 stars, and
it publishes the number: curriculum hallucination drops from 31.9% to 2.3% when the model queries
it.** Detail below the table.

The pass also closed the `pylti1.3` concentration risk with a real alternative
(`tsugiproject/tsugi`, 4,011 commits, from the author of the LTI specification), added the
institutional-grade **EMEA** autograder this file lacked (`thm-mni-ii/feedbacksystem`, 2,248
commits at 24 stars), and swept GitHub topics **in four languages other than English** — which is
how most of this was found. The method note at the end is the part worth copying.

| Repo | Licence | ★ | Checked | Layer | Why it is foundational |
|---|---|---|---|---|---|
| https://github.com/openfun/ralph | 🟢 **MIT** — `LICENSE.md` read first-hand, *MIT License, `Copyright (c) 2020-present France Université Numérique`*. 🔴 `LICENSE` 404s; only `LICENSE.md` exists, which is why a seven-name probe space is not optional | 51 | p325 | **Learning records — the event spine** | **The learner-event substrate a tutoring agent needs, published MIT by a national public operator, and held in this KB's history since p127 without ever reaching this list.** Three things in one package: an **LRS** (HTTP API collecting **xAPI** statements to the ADL LRS standard), a **CLI** for building UNIX-style data pipelines, and a **library** that fetches, (de)serialises and converts learning events between **xAPI** and **Open edX tracking logs**. Ships as `ralph-malph` on PyPI, `fundocker/ralph` on Docker Hub and an **`openfuncharts/ralph` Helm chart**; Elasticsearch backend; FastAPI + Pydantic; community on the **ESUP** (French higher-ed) Rocket.Chat · **Use it for:** **the retrieval and audit substrate under any tutor you have to prove something about.** Every pedagogical claim in a bid needs an event log that predates the claim; this is the permissive one. 🔵 Note the organisational tell: FUN ran `learninglocker-docker` and **deprecated it to build Ralph** — the incumbent LRS was replaced by the operator's own MIT one |
| https://github.com/openfun/joanie | 🟢 **MIT** — `LICENSE` read first-hand, *MIT License, `Copyright (c) 2021 France Université Numérique`* | 30 | p325 | **Education ERP (headless)** | **The education ERP this KB's vertical tier has been missing a permissive answer for.** Its own words: *"a headless ERP for education to manage course enrollment/subscription, payment and certificates delivery"* — built on **Django REST Framework**, Docker-first, with Terraform scripts and documentation for object-storage media on **OpenStack Swift**. Designed to sit behind `richie` (*"Power up Richie catalog"*) · **Use it for:** **the commercial spine of a training or certification product** — enrolment, subscription, payment, certificate issue — without inheriting a copyleft platform. This is the row that answers *"is there an Odoo for education under a permissive licence"* with a qualified yes: **headless and MIT, but the education ERP proper, not a general business framework with an education module bolted on** |
| https://github.com/openfun/potsie | 🟢 **MIT** — `LICENSE.md` read first-hand, *MIT License, `Copyright (c) 2021-present France Université Numérique`*; sidebar agrees | 11 | p325 | **Learning analytics — dashboards** | **A Grafana dashboard suite for learning analytics, written in Jsonnet with grafonnet — 114 commits.** The production-ready end of the FUN analytics path: where `warren` declares itself a proof of concept, Potsie is dashboards-as-code on an operational stack an institution already runs · **Use it for:** **the teacher- and programme-facing reporting layer over `ralph`**, delivered as reviewable code rather than as clicks in a BI tool. 🟡 Its README does not name Ralph or a datasource explicitly, so the binding is your build — read the Jsonnet, not the prose |
| https://github.com/openfun/warren | 🟡 **MIT** — `LICENSE.md` read first-hand, *MIT License, `Copyright (c) 2023-present France Université Numérique`* — **but see the self-assessment** | 17 | p325 | **Learning analytics — visualisation (reference only)** | *"A visualization platform for learning analytics"* over xAPI, and it states in its own README: 🔴 ***"This project is a Proof Of Concept not suitable for production yet."*** Recorded anyway, for one reason worth more than the code: **its frontend renders inside an LTI iframe** — the operator delivering xAPI analytics to a course chose **LTI** as the surface · **Use it for:** **evidence in the LTI-versus-MCP argument** (`intel/trends.md` trend 6) and as a reference for the Ralph → dashboard binding. 🔴 **Do not propose it as a deliverable component**; it disqualified itself and that honesty is why the row is here |
| https://github.com/openfun/django-lti-toolbox | 🟡 **MIT** — `LICENSE` read first-hand, *MIT License, `Copyright (c) 2020-present GIP FUN MOOC.`*; sidebar agrees | 14 | p325 | **Interoperability — LTI tool provider plumbing** | *"A Django application to build LTI Tool Providers"*, **34 commits, no release, and last pushed `2024-11-14`.** 🔴 **This row is the evidence behind this pass's main finding and should be read as a measurement, not a recommendation: the permissive LTI plumbing exists, a national public operator published it, and it has sat untouched for roughly twenty-three months** while MCP tooling in this same KB ships weekly. The README names no LTI version · **Use it for:** **the argument, and only then the code.** When a client insists the integration must be LTI, this is both the permissive starting point *and* the exhibit for why the agent ecosystem went elsewhere. Budget maintenance you do not get from upstream |
| https://github.com/openfun/ashley | 🟢 **MIT** — `LICENSE` read first-hand, *MIT License, `Copyright (c) 2020-present GIP FUN MOOC.`* | 12 | p325 | **Course discussion / cohort surface** | *"A self-hosted multi-tenant discussion forum for learning"*, Django, from the FUN-MOOC stack · **Use it for:** **the cohort layer a tutor product keeps needing and nobody budgets for.** Multi-tenancy is the part that matters: one deployment across many courses or institutions, which is the shape a studio engagement actually ships in. Also the natural **xAPI emitter** for discussion events feeding `ralph` |
| https://github.com/muhammedalakbarli/imparo | 🟡 **MIT** — `LICENSE` read first-hand, the MIT text. 🔴 **Header reads `Copyright (c) 2017 Contributors` on a repository created `2026-07-01`** — an unedited template, i.e. the grant is intact but the holder and year are fiction | 2 | p325 | **National-curriculum adaptive platform (EMEA — Azerbaijan)** | **The first Azerbaijani artefact in this KB, and the first skill graph here built against a non-EU, non-Anglophone national curriculum.** An adaptive learning platform for **Azerbaijani school pupils, grades 1–8**, described in Azerbaijani: a **154-skill graph (`154 bacarıqlıq qraf`)**, a **per-skill mastery model**, individualised practice and **spaced repetition**, with gamification. Next.js + React + Supabase + Tailwind; pushed 2026-10-09 · **Use it for:** **the template question in any ministry conversation outside the big markets — what does it cost to express a national curriculum as a skill graph?** The answer here is 154 skills and one developer. 🟡 Fix the licence header before a scanner reads it |
| https://github.com/LucasSpinola/assistentes-educacionais-com-ia | 🟢 **MIT** — `LICENSE` read first-hand, *MIT License, `Copyright (c) 2026 Lucas Spinola e contribuidores do projeto AI for Educational Assistants`* | 2 | p325 | **Capability transfer (LATAM — Brazil, pt-BR)** | *"Trilha aberta e gratuita, do zero ao avançado, para construir assistentes educacionais inteligentes"* — a free, open, zero-to-advanced **track for building** intelligent educational assistants: NLP, machine learning, deep learning, transformers, LLMs, **RAG, agents and learning analytics**, as Jupyter notebooks, with Ollama in the stack · **Use it for:** **the enablement half of a LATAM engagement, in the client's language.** Every studio proposal in this region ends with a knowledge-transfer line item that someone then has to write; this is a permissive, Portuguese-language starting point for it. 🔵 **And read it as channel evidence: this pass's LATAM supply arrived as a curriculum, not a product** |
| https://github.com/ZhijieXiong/pyedmine | 🔴 **CONTRADICTORY — `LICENSE` is the MIT text, the README is academic-use-only.** `LICENSE` read first-hand: *MIT License, `Copyright (c) 2023 Stanford Future Data Systems`* — an organisation unrelated to this project, i.e. a copied file whose holder was never updated. README, verbatim: *"All data and code in this project may be used only for academic purposes."* | 82 | p324 | Educational data mining — KT, CD, exercise & path recommendation | **The broadest educational-data-mining library this KB has measured, and the one it cannot use.** *"A unified experimental workflow"* over **four task families**: knowledge tracing (**28 models** — qDKT_CORE, AKT_CORE, DisKT, ATDKT, CLKT, DTransformer, GRKT, HDLPKT, DKT, DIMKT among them), **cognitive diagnosis (7**, incl. NCD, HyperCD), **exercise recommendation (3)** and **learning-path recommendation (4**, LPKT4LPR as simulator), over **14 EDM datasets** (SLP, assist2009/-full/2012/2015/2017, edi2020, junyi2015, moocradar, poj, slepemapy-anatomy, statics2011, xes3g5m; EdNet-KT1 via a preprocessing note; the edi2020 text extension is *"an unofficial extension"*). **Five dataset-splitting settings**, pretrained weights on Hugging Face, a published model leaderboard, and **cold-start, hard-sample and multi-step** evaluation — with the BES metric self-marked *"has not been validated."* 220 commits, 13 forks, **v1.0.0 (15 Aug 2025) described as a stable LTS release**. Referenced codebases per its README: PYKT, EduKTM, EduCDM, RecBole. 🔵 Measured the same pass for comparison: **`pykt-team/pykt-toolkit` is 450 ★ / 139 forks** — earlier cycles of this KB carried pyKT at *"1.2k"*; **450 is the measured figure** · **Use it for:** 🔴 **Do not put it in a deliverable.** The permissive channel is boilerplate with somebody else's copyright on it; the restrictive channel is the author's own specific sentence. **A scanner returns MIT and clears procurement; a reviewer reads the README and stops the engagement** — and this is the first case in this file where the documented grant is *narrower* than the licensed one, which is the direction scanners do not catch. **Use it to choose a model family and to read the splitting settings, then reimplement, or open an issue and get the contradiction resolved in writing.** When a client needs cognitive diagnosis or exercise recommendation and not just KT, this is the map of the field; `pykt-toolkit` remains the thing you can actually ship |
| https://github.com/jplag/JPlag | 🟡 **GPL-3.0** — `LICENSE` read first-hand, the GNU GPL v3, 29 June 2007 text; sidebar agrees | 2.0k | p324 | Assessment integrity — source-code plagiarism & collusion | **The largest and most-maintained artefact in this KB's integrity tier by an order of magnitude, and it was never listed. 376 forks, 5,708 commits, pushed 2026-10-19.** Source-code plagiarism **and collusion** detection across twenty-odd languages — Java, C, C++, C#, Python, JavaScript, TypeScript, Go, Kotlin, R, Rust, Swift, Scala, LLVM IR, Scheme, EMF metamodel and model, SCXML, plain text, plus a multi-language mode — with the README's own caveat that *"maturity varies by language."* *"JPlag can either be used via the CLI or directly via its Java API"*, published on **Maven Central**, with a local report viewer that launches automatically from the CLI: *"No data will leave your computer!"* 🔵 The README makes **no comparison to Moss** — `moss` is a topic tag only · **Use it for:** **For any CS-education or bootcamp engagement this is the integrity layer, not a build.** Twenty-language coverage and a Java API mean it drops behind a service boundary in days. 🟡 **GPL-3.0: deploy it as a service over HTTP and never link it into the client's application** — the same rule this file applies to `text-statistics`. Pair it with `aegis-integrity` (prose and citations) in `compose/patterns.md` **P11**; JPlag covers code, which `aegis-integrity` does not |
| https://github.com/NoplagLabs/noplag-engine | 🟢 **Apache-2.0** — `LICENSE` read first-hand, the Apache 2.0, January 2004 text; description agrees | 86 | p324 | Assessment integrity — verbatim & near-verbatim text matching | **The permissive text-similarity engine the integrity tier needed.** Sentence-window chunks → **winnowing fingerprints stored as a GIN-indexed `bigint[]` in PostgreSQL** → candidate retrieval by fingerprint overlap → **seed-and-extend alignment to exact character ranges.** Five REST endpoints (`POST /v1/checks`, `GET /v1/checks/{id}`, `GET /v1/checks/{id}/report`, `POST /v1/corpus/documents`, `/docs` for OpenAPI), SSE progress per `docs/api.md`, Alembic migrations, `docker compose up`, and a first boot that indexes **~1,000 bundled Wikipedia articles**. Honest about scope: *"This engine detects verbatim and near-verbatim copying"* and *"paraphrase, semantic, and AI-writing detection are on the public roadmap."* Benchmarks stated and bounded: plagdet *"around 0.8+"* with precision ≥ 0.95 on verbatim and lightly obfuscated material, while on the full PAN-PC-11 an L0/L1 engine *"scores near zero by design"* — with an explicit warning against reading one plagdet figure as general accuracy. **6 commits, 76 forks** · **Use it for:** **Take it for the algorithm and the schema; it is a studio-grade reference for fingerprint storage in Postgres, which is the part teams get wrong.** 🔴 **Three cautions:** it is the **open core of the hosted noplag.com** (the hosted side adds live web search; the open engine matches your local corpus only), *"the API ships with no authentication"* so it cannot face a network as given, and **6 commits against 86 stars and 76 forks** is a fork-to-star ratio this KB has not seen on an organically grown repository — read the code before depending on the project |
| https://github.com/thu-cs-lab/jieplag | 🟢 **MIT** — `LICENSE` read first-hand, *MIT License, Copyright (c) 2023 Jiajie Chen, Shengqi Chen* | 54 | p324 | Assessment integrity — code similarity (Rust) | Moss-inspired plagiarism detection **in Rust**, from the Tsinghua CS teaching lab. 1 fork, default branch `master`, last pushed 2026-06-28 · **Use it for:** **The only permissively licensed code-similarity engine in this file with no commercial product behind it** — which makes it the one to embed rather than service-isolate when a client's constraint is GPL avoidance rather than language coverage. 🔴 Smaller and quieter than JPlag: no multi-language story, and APAC-authored with Chinese-language teaching context |
| https://github.com/openeduhub/skohub-vocabs-oeh-patched | 🟢 **Apache-2.0** — `LICENSE` read first-hand, the Apache 2.0, January 2004 text. 🟡 `package.json` says `"license": "Apache License 2.0"`, **which is not a valid SPDX identifier** (`Apache-2.0` is), so an SPDX-strict scanner reads the manifest as unknown rather than as Apache | 0 | p324 | Vocabulary publishing (EMEA) | **A patched fork of `skohub-io/skohub-vocabs`** — hbz NRW and graphthinking GmbH upstream; the `package.json` `repository` field still points at `skohub-io/skohub-vocabs`. *"A simple tool for publishing SKOS vocabularies"*: a static-site generator that parses SKOS with **slash or hash URIs** (slash *"better supported"*), renders full concept pages with **machine-readable JSON-LD per concept**, exposes a basic lookup API, supports a **webhook server that rebuilds a vocabulary from GitHub or GitLab**, and selects display language from the browser or a `?lang=` parameter. **This is the publishing layer behind the `vocabs.openeduhub.de` that `its-data` resolves URIs against** · **Use it for:** **The permissive half of the German stack, and the only `openeduhub` repository whose grant came in from outside.** If a client needs controlled vocabularies published as resolvable, machine-readable SKOS — competency frameworks, subject taxonomies, qualification levels — this is the build. 🟡 Fix the manifest to `Apache-2.0` in your fork before it hits the client's dependency scanner |
| https://github.com/openeduhub/mappings | 🟡 **GPL-3.0** — `LICENSE` read first-hand, the GNU GPL v3, 29 June 2007 text | 0 | p324 | Vocabulary / schema mappings (EMEA) | Vocabulary and schema mappings for the WLO metadata stack. One of p322's six named-unread repositories; measured this pass · **Use it for:** **Service, never linked** — the same GPL-3.0 rule as `metalookup`, `text-statistics` and `discipline-classification`. Its value is as a worked example of mapping one country's education metadata vocabularies onto each other, which is the unglamorous half of every interoperability engagement |
| https://github.com/openeduhub/its-prep | 🔴 **NO LICENCE** — no licence file under any of `LICENSE`, `LICENSE.md`, `LICENSE.org`, `LICENCE`, `COPYING`, `LICENSE.txt`, nor a manifest grant; no sidebar entry | 0 | p324 | NLP substrate (EMEA) | **87 commits. One of the two repositories p322 told this pass to read first, because `python-kidra` depends on it.** *"A generic interface to various NLP tools"* whose stated goal is to *"stream-line the process of defining natural language pre-processing pipelines, particularly in the context of educational resources."* The design is the part worth reading: **every pipeline stage is a filter that returns a subset of a document's tokens and may not modify them**, over an immutable `Document` that retains the full original text — so a pipeline is auditable and reversible by construction. Worked example (`poc_topic_modeling`): drop unwanted universal POS tags → drop stop words → drop lemmas expected to carry little meaning **for learning resources** → drop lemmas by document frequency at both tails. Named-entity and noun-chunk merging; spaCy analysis caches via `save_caches`/`load_caches`; pip or Nix flake. German `de_core_news_lg` (🔴 the README's link beside it points at `de_dep_news_trf`, a different model) · **Use it for:** 🔴 **No grant: cannot be used.** **Reimplement the filter contract — it is ten lines of interface and it is the right design**: keep-or-discard filters over an immutable document, which is exactly what makes an OER ingestion pipeline explainable to a ministry client. The German model dependency means the tuning does not transfer; the architecture does |
| https://github.com/openeduhub/its-data | 🔴 **NO LICENCE** — no licence file under any of seven candidate names, no manifest grant, no sidebar entry | 0 | p324 | Data substrate (EMEA) | **159 commits. The second of the two `python-kidra` dependencies p322 named.** *"A Python library that aids in retrieving and processing large data dumps from elasticdump … primarily for the purpose of training and evaluation of AI tools for the automatic generation of metadata."* Two modules: `its_data.fetch` downloads elasticdump files, turns them into **pandas** data frames and **retrieves labels for URIs and SKOS vocabularies**; `its_data.default_pipelines` ships `flat_classification` and friends. A `download-data` CLI; Nix flake recommended, pip *"untested"*. The schema is the useful part: OEH metadata keys (`properties.ccm:taxonid`, `properties.ccm:educationalcontext`) in, and out come `raw_texts` (title + description), `ids`, **`editor_arr` (an editor-confirmed flag)** and `target_data` with `arr`, `uris`, `labels` and **`in_test_set`** — i.e. the train/test split and the human-confirmation flag are **first-class fields of the data contract**, not a notebook convention. URIs resolve against `vocabs.openeduhub.de` · **Use it for:** 🔴 **No grant: cannot be used.** **Copy the contract, not the code.** `editor_arr` + `in_test_set` as fields of the dataset itself is the cheapest governance win in an OER metadata engagement: it makes *"which of these labels did a human confirm"* and *"which rows may be scored"* answerable from the data rather than from tribal memory |
| https://github.com/openeduhub/topic-statistics | 🔴 **NO LICENCE** — no licence file under any of seven candidate names, no sidebar entry | 0 | p324 | Analytics utility (EMEA) | **9 commits.** *"A very simple application that computes various statistics on WLO topic pages, based on a downloaded copy of the database."* Invoked only as `nix run github:openeduhub/topic-statistics -- --help`; no HTTP surface. Its own *Possible Improvements* section proposes **folding the logic into `meta-qs` rather than running a separate service**, and reading the private ElasticSearch directly instead of a downloaded dump; it links `its-data` for a collection filter · **Use it for:** 🔴 **No grant, 9 commits, and the repository argues against its own existence.** Recorded for completeness and to close p322's list. The transferable observation is organisational: this is what a public operator's analytics looks like before it is a product — a Nix-runnable script over a database dump, with the consolidation already written down |
| https://github.com/openeduhub/oeh-search-frontend | 🔴 **NO LICENCE ON EITHER CHANNEL** — no licence file under any of six candidate names, **and `package.json` has no `license` key at all**; no sidebar entry | 5 | p324 | Public search UI (EMEA) | **1,050 commits on `develop`, 1 fork, 13 open pull requests — the second most-committed repository in the organisation after `oeh-search-etl`.** The **Angular 19.2.14** public search frontend of WirLernenOnline.de. *"In order to use the frontend, you either need a deployed or a locally running instance of Edu-Sharing."* Split into `api` and `wlo-search` (`core`, `preferences`, `search`, `shared`, `template`); Node pinned via `.nvmrc`; configuration injected through `src/env.js` from environment variables in Docker; **Karma unit tests and Cypress E2E**; Husky + lint-staged + Prettier + ESLint; Angular i18n with locales in `src/locale`; and web components built and copied into a **WordPress theme folder** · **Use it for:** 🔴 **No grant: cannot be used — and this row is why the licence-by-layer rule stops at the backend.** p322 read the org as *permissive shells / GPL analysers / unlicensed inference core*; **the thinnest shell of all, a pure UI, has no grant on either channel**, where that rule predicted Apache-2.0. 🔵 Note the asymmetry for diligence: *no `license` key* is a weaker position than a manifest that disagrees with the `LICENSE` file — there is nothing to argue from. **Rebuild the UI; read it for the WordPress-embed pattern**, which is how a ministry portal actually ships a search experience into an existing CMS |
| https://github.com/haolpku/K12-KGraph | **MIT (code) / CC BY-NC-SA 4.0 (data)** — README, verbatim: *"Code (this repository): MIT"*, *"Dataset (graph, benchmark, training data): CC BY-NC-SA 4.0"*; sidebar reads *"MIT licenses found"* | 420 | p323 | Curriculum data + benchmark + training data | **China's national curriculum as a verified, evidence-linked knowledge graph — and the peer-reviewed proof that the `bncc-dev` method generalises.** Accepted to the **NeurIPS 2026 Evaluations & Datasets Track**. Built from **48 People's Education Press (PEP) K-12 textbooks** — Mathematics 23, Physics 9, Chemistry 7, Biology 9. **10,685 KG nodes** (6,579 concepts, 1,364 skills, 652 experiments, 1,171 exercises) and **23,278 edges across 9 edge types**; **every edge carries an `evidence` field linking back to textbook source text**. Verification: **12 subject-qualified expert annotators at Fleiss' κ = 0.84**, automatic **DAG validation of the `is_a` and `prerequisites_for` subgraphs**, and a 3-expert spot-check of stratified benchmark items at **98.4% fully correct**. **K12-Bench: 23,640 multi-select questions** over five task families. **K12-Train: 2,267 instruction–response pairs.** Three checkpoints fine-tuned on K12-Train (Llama3.1-8B, Qwen3.5-2B, Qwen3-4B) on Hugging Face. 67 forks, 16 commits · **The pipeline is MIT and the curriculum is not.** Reuse the **method** — extraction, per-edge evidence linking, DAG validation, the annotation protocol that produced κ = 0.84 — in any jurisdiction; **the graph, benchmark and training data are NonCommercial and ShareAlike and cannot enter a client deliverable anywhere.** This is the strongest argument in this KB for the P10 build: it proves the hard part is doable and is itself licensed out of commercial reach. **Two caveats for anyone quoting it:** the About blurb says *"multimodal training dataset"* while the body describes only text instruction–response pairs, and the README reports expert *review* plus validation — **it does not claim every edge was individually human-verified**, and κ = 0.84 measures annotator agreement on relation labels, not graph completeness |
| https://github.com/razi-03/NCERT-CKG | 🔴 **NO LICENCE** — no sidebar entry, no LICENSE file | 0 | p323 | Curriculum data (India) | **The artefact p322 swept 180 `ncert`/`cbse` repositories for and declared absent — found by changing the query, and it has no grant.** **Class X NCERT Mathematics only**, from **18 PDFs**: 14 chapters (`jemh101`–`jemh114`), two additional chapters (`jemh1a1`, `jemh1a2`), an answer source (`jemh1an`) and a preliminary file (`jemh1ps`). PDF in, **CKG JSON** out. **10,417 CKG nodes, 1,682 semantic nodes, 13,757 provenance-aware edges**, provenance coverage **1,682 / 1,682** — *"every semantic node is required to have source evidence."* The method is the right one: *"prerequisite reasoning is treated separately from textbook ordering"*, and a prerequisite *"must instead be supported by conceptual dependency evidence or an explicit inference procedure"* — a chapter appearing earlier is **not** treated as proof of a prerequisite. 0 forks, 2 commits, no release · **Do not depend on it; do watch it, and consider asking the author for a licence.** It makes India's curriculum gap **contested rather than empty**, which shortens the P10 Variant B window. Two silences matter: the README says **nothing about textbook copyright or whether the 18 NCERT PDFs are bundled** (this KB has already recorded one NCERT project that bundles textbook PDFs), and it **never mentions an LLM**, so whether the edges are model-derived is unknown rather than concealed — the only review language is the generic *"should be sampled and reviewed manually"* |
| https://github.com/mizcausevic-dev/curriculum-knowledge-graph | MIT (sidebar) | 1 | p323 | Higher-ed curriculum analysis | FastAPI service modelling **courses, prerequisites, skills and outcomes** as a graph, with prerequisite and skill-dependency analysis, **pathway bottleneck analysis** and a capstone pathway explorer. Ships `app/data/sample_curriculum.json` as a seeded degree path, so it is not framework-only; its own example names `IS-230` as the highest-bottleneck course and a capstone path of IS-101 → IS-210 → IS-320 → IS-410. **No institution or country stated, and the sample data is not claimed to reflect a real programme.** 0 forks, 10 commits · **A pattern, not a dataset — and the permissive component this KB lacked for higher-ed advising.** Bottleneck analysis over a prerequisite graph is a sellable higher-ed product (which course silently gates a cohort's time-to-degree) and nothing else here implements it. **Also a market signal: the author is already in this KB** — `mizcausevic-dev/mcp-ai-tutor` sits in the FERPA governance cluster. One author building both a compliance auditor and a curriculum graph, each at 0–1 stars, is p322's market-forming shape appearing in a second component |
| https://github.com/openeduhub/python-kidra | 🔴 **NO LICENCE — none in the sidebar, none in the root listing, none in the README** | 0 | p322 | AI service gateway (EMEA) | **137 commits.** *"A unified API to the various AI applications we have built"* for the **IT's JOINTLY** project, used to generate additional or missing metadata. One API in front of seven services: `text-extraction`, `text-statistics`, `topic-statistics`, `its-jointprobability` (Bayesian metadata prediction), `wlo-topic-assistant`, `wlo-classification` and `kea` (links relevant Wikipedia articles, forwarded to an external service). 🔴 **This is the single most useful artefact in the org and it carries no grant at all.** Read it as an architecture document — the service decomposition is the transferable part — and note that one of the seven services it advertises has no public repository (404, see below) |
| https://github.com/openeduhub/its-jointprobability | 🔴 **NO LICENCE — none in the sidebar, no licence file in the root listing, none in the README** | 0 | p322 | Metadata prediction / ML (EMEA) | **200 commits.** Bayesian metadata generation for educational materials: **Pyro**'s ProdLDA topic model trained with black-box variational inference over PyTorch bag-of-words tensors. Predicts **school discipline, university discipline, resource type, target audience, educational context and WLO topic** from raw text via a `/predict` REST endpoint or the `predict_from_texts` method; ships retraining CLIs and runs as a Nix microservice. 🔴 **No grant.** It is also the most interesting single artefact here for a client with a large uncatalogued corpus and no labels budget — which is exactly why the missing licence matters |
| https://github.com/openeduhub/metalookup | 🟡 **GPL-3.0** (sidebar + `LICENSE.txt`) | 5 | p322 | OER compliance / metadata (EMEA) | **623 commits** — the second most-maintained repo in the org and the most maintained one that carries any licence. Extracts and suggests OER metadata from a URL, covering **accessibility, licensing and advertising**: Playwright fetches the page, then it analyses the requests, responses and final rendered HTML, and runs **Lighthouse** to assess accessibility. Deploys as a container set — API, Lighthouse, `browserless/chrome`, optional Postgres cache (SQLite or no cache also supported); `POST /extract` takes `{"url": ...}`, `/_ping` is the health check, Swagger at `/docs`. **Only the API container is meant to be reachable** — **The accessibility-and-licence screen that every public-sector OER procurement asks for, already built.** 🟡 GPL-3.0: run it as a service behind a process boundary and never link it into a client codebase. Field list is in `docs/features.md`, which this KB has not read |
| https://github.com/openeduhub/edu-sharing-python-client | **Apache-2.0** (sidebar + README) | 0 | p322 | Platform client (EMEA) | **519 commits**, tag **v0.3.6**, test report in the README dated 2026-10-01. Async-first Python client for edu-sharing repositories and the **b-api (Bildungs-API)**: search, metadata read and write, collections, publishing — plus access to an **LLM gateway, a text-extraction service and the metadata agent**. **All 389 operations are generated from `openapi.json`**, with `scripts/generate_client.py` able to regenerate the layer from a live instance's spec. **Verified against edu-sharing 11.0.** Pre-1.0 and **not on PyPI — install from Git** — **The licence-clean way into the whole stack, and the row to start from.** Apache-2.0 over a generated client means the integration surface is safe even where the services behind it are not. This is how you touch a GPL-3.0 edu-sharing instance without a linking question |
| https://github.com/openeduhub/metadata-agent-api | 🔴 **README says "Lizenz: MIT" — no `LICENSE`, `LICENSE.md`, `LICENSE.txt` or `COPYING` in the root listing, and the sidebar shows no licence** | 0 | p322 | Metadata extraction engine (EMEA) | **24 commits.** The engine under `metadata-agent-canvas` and the browser plugin: a FastAPI service (Python 3.13+, uvicorn, Docker with Playwright and Chromium for screenshots) that extracts structured metadata in the **WLO/OEH schema** from text, a URL or a repository node, then normalises values, geocodes addresses, validates and can upload to edu-sharing. **Eleven active schemas** — event, learning material, education offer, person, organisation, tool/service, source, didactic planning tool, occupation, prompt. Endpoints: `/generate`, `/extract-field`, `/detect-content-type`, `/validate`, `/export/markdown`, `/upload`, `/upload/verify/{node_id}`, `/screenshot`, `/health`, `/info/schemata`. Responses can carry **per-field origin tags**, the source text and a base64 preview. Providers: `b-api-openai` (default `gpt-4.1-mini`), **`b-api-academiccloud` (`deepseek-r1`)**, native `openai` (`gpt-4o-mini`); default temperature 0.3 — **Per-field origin tags are the provenance feature an education buyer now asks for, and the AcademicCloud provider is a sovereign-inference path through German academic compute.** 🔴 But the grant is a README sentence with no file behind it — treat the schema design and the endpoint surface as the deliverable, not the code |
| https://github.com/openeduhub/text-extraction | 🔴 **NO LICENCE — none in the sidebar, no licence file in the root listing, none in the README** | 0 | p322 | Ingestion (EMEA) | **77 commits.** Extracts clean text from URLs using **trafilatura and markitdown**, explicitly aiming to improve on trafilatura alone and to fall back when extraction fails on JavaScript-heavy sites — the fallback is **Playwright headless Chromium**. Ships real rate limiting (`get_simple_multibucket_limiter`, `domain_mapper`), runs as a library (`from_headless_browser_unlimited`, `from_html_unlimited`), a local service on port 8000 or Docker. 🔴 **No grant** — The per-domain rate limiting is the part most homegrown harvesters lack and the part that gets an engagement blocked by a publisher. Read it, then write your own |
| https://github.com/openeduhub/text-statistics | 🟡 **GPL-3.0** (sidebar + `LICENSE`) | 0 | p322 | Readability (EMEA) | **94 commits.** Microservice computing **estimated reading time** from a 200 WPM baseline adjusted by **Flesch Reading Ease**, plus the Flesch score, a difficulty classification and the **Wiener Sachtextformel** index. `POST localhost:8080/analyze-text` returns the metrics and a version number; runs as a Python package, a Nix flake or a Docker image. **No ML models** — the reading-time adjustment is a fixed exponential formula, and the README says better models could come later — **Reading level is the single most requested differentiation signal in schools work and this computes it with arithmetic, not a model.** The Wiener index is German-calibrated — confirm the formula before applying it to another language. 🟡 GPL-3.0: service boundary only |
| https://github.com/openeduhub/discipline-classification | 🟡 **GPL-3.0** (sidebar + `LICENSE`) | 0 | p322 | Classification / ML (EMEA) | **73 commits.** *"A utility to train and predict subject areas for the WLO project dataset"* — **the canonical home of `wlo-classification`**, which `python-kidra` names and which redirects here; forked from `yovisto/wlo-classification`. Docker + Python + **Keras/TensorFlow**, CherryPy web service on port 8080, returns **the top three disciplines with scores**. The `data` folder ships a **pretrained model, `wirlernenonline.oeh.h5`**, with a class-label file and a tokenizer pickle — **A pretrained subject classifier for a real national curriculum, shipped in the repository** — rare, and the reason this row exists despite 0 ★. 🟡 GPL-3.0 and a redistributed model: keep it behind a service boundary and check the training-data provenance before a client deliverable |
| https://github.com/openeduhub/duplicate-detection | **Apache-2.0** — `LICENSE` read first-hand and it is the Apache 2.0, January 2004 text. 🔴 **The README says "MIT License" and is wrong** | 0 | p322 | Data quality (EMEA) | **25 commits**, 1 fork. FastAPI microservice detecting duplicate and near-duplicate content in the WLO repository by **MinHash over text shingles** — explicitly **not** learned embeddings — plus URL normalisation, title normalisation that strips publisher suffixes, and exact URL matching. `POST /detect/hash/by-node` (with `similarity_threshold`, `search_fields`, `max_candidates`) and `POST /detect/hash/by-metadata` (response-cached); `/health`, Swagger at `/docs`, ReDoc at `/redoc` — **Dedup is the unglamorous step that decides whether an OER catalogue is usable, and hash-based beats embeddings here on cost and explainability** — a MinHash threshold can be defended to a client, a cosine distance cannot. Supersedes the org's dormant `wlo-duplicate-detection` (2022) |
| https://github.com/openeduhub/z-api-runner | 🔴 **NO LICENCE — none in the sidebar, no licence file shown, none in the README** | 0 | p322 | Batch LLM operations (EMEA) | **37 commits** on `master`. *"A Python project which provides a simple swagger api to run a prompt in bulk over a set of collections/materials"* — the batch-inference tier of the pipeline, with `openapi.json` committed, Swagger at `:8001/docs` (`:8083` under `docker compose`). **The README does not name the model or provider**, and this KB has not read `app/` or `requirements.txt`, so the backend is unknown — Bulk-prompt-over-a-catalogue is the operation every OER enrichment engagement needs and nobody budgets for. 🔴 No grant, and an unstated LLM backend — this row is a design reference and a named gap, not a dependency |
| https://github.com/openeduhub/wlo-quellenliste | **Apache-2.0** (sidebar + `LICENSE`). 🔴 **The README's "Lizenz" section says MIT and is wrong** | 0 | p322 | Source registry (EMEA) | **6 commits.** The source directory behind WirLernenOnline, as software rather than a list: a **Python FastAPI** backend that pulls source data from the WLO edu-sharing REST API, merges it with an **editorial correction list** (`quellen_korrektur.csv`) and serves the result, plus an **Angular 18 web component `<wlo-sources>`** rendering tiles, list or statistics. Machine-readable throughout — `quellen_merged.json`, `quellen_stats.json`, semicolon-separated CSV export, JSON endpoints for sources, statistics, metadata and content counts; read endpoints public, writes behind an API key; Swagger at `/docs`. **The repo description calls the platform "WissenLebtOnline" while the body says "WirLernenOnline" — a naming mismatch in the source, recorded as found** — **The editorial-correction-list pattern is the transferable idea**: harvested source metadata is wrong, and a reviewed CSV overlay merged at serve time is how a public operator fixes it without mutating the harvest. Field schema of the JSON/CSV output is not documented — unread |
| https://github.com/openeduhub/its-qna | 🔴 **NO LICENCE — none in the sidebar, no licence file in the visible listing** | 0 | p322 | Question generation (EMEA) | **4 commits.** Generates question–answer pairs about a given text using LLMs. Packaged as OCI images via **nix2container** (`nix run` copies to Podman, Docker or a registry) and runnable directly with `nix run github:openeduhub/its-qna`; the README states the **CUDA variant is currently broken** on an nixpkgs issue. The README names no model, no API and no input/output format — **4 commits and no licence — recorded for completeness, not for use.** It matters only as evidence of where the org intended to go next: automatic assessment-item generation off harvested OER |
| https://github.com/openeduhub/oeh-metadata-vocabs | **CC0-1.0** | 2 | p321 | Curriculum / competency metadata (EMEA) | **938 commits, 7 forks, 5 watchers.** All SKOS vocabulary files for OpenEduHub / WirLernenOnline, as Turtle (`.ttl`) under the namespace `w3id.org/openeduhub/vocabs`, generated into a browsable view with SkoHub-Vocabs at `vocabs.openeduhub.de`. Covers **learning-resource type** (including a LOM-based set, `lom_*`), **educational context, educational level, discipline, school type**, **rights and copyright restriction, cost and price**, **quality criteria** (`quality_*`: data privacy, didactics, language) and **competence frameworks — DigCompEdu, ESCO skills, EQF/DQR levels**. **CC0-1.0 is the most permissive tier this KB has recorded on any asset** — no attribution condition at all. This is the row that corrects the p319 Germany claim below |
| https://github.com/openeduhub/oeh-search-etl | 🔴 **NO LICENCE FILE** | 8 | p321 | Harvesting (EMEA) | The ETL behind WirLernenOnline: Scrapy spiders → Postgres → Elasticsearch, Python 3.13 managed with Poetry, Splash and Playwright containers for rendered sources; **1,397 commits on `master`** — the most heavily maintained artefact in the `openeduhub` org. 🔴 **Read it, do not depend on it.** No LICENSE file was present in the repository root when it was read first-hand at p321 and the page states no licence, so **there is no grant**. The commit count makes it the most tempting harvester in the sector and the missing licence makes it unusable in a client deliverable. Spider count is not stated in the README — `converter/spiders/` is not enumerated on the page, so this KB does **not** have a source count |
| https://github.com/virgiliojr94/book-to-skill | MIT | 35.3k | p319 | Enablement / authoring | Converts a technical book, document folder or source set (PDF, EPUB, DOCX, HTML) into a structured agent skill: `SKILL.md` index, per-chapter files, glossary, patterns, cheatsheet; 228 commits, 3.7k forks. **The MIT licence covers the converter only, explicitly not the books you process with it** — which is the copyright question every "turn our textbooks into a tutor" engagement has to answer on day one. Read first-hand this pass: no agent-directed star solicitation in the README |
| https://github.com/microsoft/ai-agents-for-beginners | MIT | 77.5k | p315 | Enablement | 18 lessons on building agents. Not a dependency — the fastest way to bring an engagement team to a shared baseline |
| https://github.com/HKUDS/LightRAG | MIT | 40.2k | p319 | Retrieval | simple, fast RAG (EMNLP 2025), 10,873 commits, 5.7k forks. **Re-verified first-hand this pass** (the p316 reading was due a re-read): still MIT, unchanged. The course-material grounding layer under a tutor; same lab as DeepTutor, so the two compose without friction |
| https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | p317 | Agent runtime | Minimal code-thinking agent loop; small enough to audit, which matters when a ministry asks how the tutor decides |
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | p315 | Compute | Multi-user notebook server — the delivery substrate for every CS/data curriculum, and what nbgrader and otter-grader plug into |
| https://github.com/learningequality/kolibri | MIT | 1.2k | p318 | Offline delivery | Offline-first learning platform, 39,803 commits on `develop`, 1.0k forks. Re-verified first-hand this pass: still MIT, still the only MIT platform in the sector, and the one that works without connectivity |
| https://github.com/tsugiproject/tsugi | Apache-2.0 | 376 | p319 | Integration (LTI) | "A multi-tenant scalable LTI library and tool hosting environment", plus an administration/management/developer console and an **IMS ContentItem app store**; 4,011 commits, 266 forks, 43 watchers, **Apereo Incubating**, maintained around Dr Chuck (Charles Severance, co-author of the LTI specification); shares low-level IMS libraries with Sakai; PHP, with per-PHP-version branches. **Caveat: the GitHub page does not state which LTI versions or Advantage services it implements** — verify before scoping |
| https://github.com/jcputney/scorm-again | MIT | 356 | p319 | Integration (SCORM) | "A modern, fully-tested JavaScript runtime for SCORM 1.2 and SCORM 2004", LMS-agnostic, logs calls and data when no LMS endpoint is configured; 1,229 commits, 84 forks. **AICC support was removed in v3.0.0; cmi5 and xAPI are roadmap "potential" only.** The route into the large installed base of SCORM courseware that LTI does not reach |
| https://github.com/open-spaced-repetition/fsrs-rs | BSD-3-Clause | 447 | p315 | Scheduling | FSRS optimiser and scheduler in Rust — embeddable retention scheduling, no Anki dependency |
| https://github.com/openfun/richie | MIT | 316 | p315 | Portal/CMS | Education-portal CMS from France Université Numérique. MIT, EMEA-authored, built to front Open edX |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 138 | p319 | Integration | LTI 1.3 Advantage tool implementation, 178 commits. Covers **Deep Linking, Assignment & Grade Services, Names and Roles, Course Groups, Submission Review and Data Privacy Launch** — the whole Advantage surface. This is the repo that gets your agent *into* the client's existing LMS. **Re-verified p319: 84 forks, 39 open issues, still no published release** — pin a commit |
| https://github.com/adamzammit/LTIPlugin | **GPL-3.0** | 14 | p320 | Integration (LTI, outcome passback) | Makes **LimeSurvey act as an LTI provider**: the learner launches a survey or assessment from the LMS and the plugin **returns a score to the gradebook**, as a 0.0–1.0 value computed from a LimeSurvey expression; 97 commits on `master`, LimeSurvey 3.x–7.x. **README documents setup against four platforms — Canvas, Moodle, openEdX and Blackboard** — which makes it the broadest passback reference in this file. **Three caveats, all load-bearing.** (1) **It is not AI** — it is assessment delivery plus outcome passback; the intelligence would be yours. (2) **The page never names an LTI version** and it bundles `LTI-Tool-Provider-Library-PHP`, which points at the **legacy LTI 1.x Basic Outcomes path, not 1.3 Advantage AGS** — read the submodule before scoping. (3) **GPL-3.0 is copyleft**, so it sits with `tutor-gpt`/`lumen`/`LTLTutor` on the far side of this KB's architectural line: run it as a separate service, do not link it into a deliverable. **Its value is as a readable, four-LMS answer to "how does the score actually get back".** No release is published — pin a commit |
| https://github.com/bncc-dev/bncc-dados | **MIT (code) / CC BY 4.0 (data)** | 22 | p319 | Curriculum standard (LATAM) | **Brazil's national curriculum (BNCC) as verified open data**: 1,721 learnings — 1,580 from the three stages of basic education (93 Educação Infantil, 1,304 Ensino Fundamental, 183 Ensino Médio) plus 141 from the Computing complement (Parecer CNE/CEB 2/2022) — with 20 legal milestones and 5 reference profiles, in JSON (canonical), SQLite, SQL dump and CSV, under JSON Schema draft 2020-12. Content version `dados-2026.08`, schema v1.1.0, status stable; 40 commits. Maintained by **Profy Tecnologias Educacionais Ltda**; docs pt with a full en translation |
| https://github.com/bncc-dev/bncc-pacotes | **MIT (code) / CC BY 4.0 (data)** | 9 | p319 | Integration (MCP, LATAM) | Machine interfaces to the dataset: npm `@bncc/dados` 0.7.0 (typed API with embedded data), npm `@bncc/mcp` 0.6.0 (**MCP server, seven tools**: `bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`), PyPI `bncc` 0.5.0, and a hosted MCP endpoint at `mcp.bncc.dev` on Cloudflare Workers **requiring no API key**; 103 commits. Embedded data is synced from a pinned `bncc-dados` commit with version and checksum records; a well-formed code that is missing returns an explanatory error, not `null` |
| https://github.com/bncc-dev/bncc-benchmark | **MIT (code) / CC BY 4.0 (items, results, methodology)** | 9 | p319 | Evaluation (LATAM) | Measures how often LLMs invent BNCC codes and texts with no access to the source: four tasks — direct lookup, existence (including plausible fake codes), open generation, reverse lookup — scored against the verified dataset across five dimensions; 82 commits. Official round `oficial-seca-2026-09`; a held-out item set is never published so memorisation is detectable. **Carries the grounding measurement this KB has never had** |
| https://github.com/thm-mni-ii/feedbacksystem | Apache-2.0 | 24 | p319 | Autograding / feedback (EMEA) | Intelligent tutoring system that checks student submissions automatically, returns an immediate result with suggestions about the mistake, and **aggregates common errors so lecturers can address them in class**; 2,248 commits on `dev`, 147 issues, 94 PRs. Java 11/Gradle, Scala, MySQL, Docker Compose, Kubernetes + Helm for production. **Apache-2.0 © Technische Hochschule Mittelhessen** — institution-built, institution-run. No LMS or LTI integration described |
| https://github.com/elimu-ai/webapp | MIT | 41 | p319 | Offline content delivery | Hosts Android apps and educational content (texts, words, videos, storybooks) per language; the elimu.ai Appstore app pulls and installs it onto devices for **out-of-school children**; 8,075 commits, 68 forks, Java/Spring, REST API consumed by three Android apps. Production deployments listed for **Hindi, Tagalog, Thai, Vietnamese and English**. The org publishes 92 repos including real ML components — `ml-storybook-reading-level`, `ml-storybook-recommender`, `ml-video-recommender`, `ml-event-simulator`, `ml-datasets` — all MIT-org, all under 10 ★ |
| https://github.com/smashburger-dev/argmin | **MIT (code) / CC BY 4.0 (content)** | 6 | p319 | Enablement (EMEA) | A **German-language** browser course on how AI works: 50 lessons, 280+ exercises, 320-entry glossary, from maths basics through linear algebra, ML, deep learning, transformers and generative AI; Python runs in-browser via **Pyodide and the app works offline after first load**; 343 commits; self-hostable. The licence-clean German asset for the EU AI Act Article 4 staff-literacy duty |
| https://github.com/Sunbird-Ed/SunbirdEd-portal | MIT | 41 | p315 | Platform (APAC) | Web portal of Project Sunbird, the stack behind India's national digital-education infrastructure — read the caveat |
| https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service | Apache-2.0 | 12 | p316 | SIS / data standard | Successor to the Ed-Fi ODS/API platform; 1,105 commits. The standards-body reference implementation for student data |
| https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster | Apache-2.0 | 6 | p316 | Rostering | Serves a **OneRoster 1.2** API from data in an Ed-Fi ODS database; 151 commits |

**Licence split over 21: MIT (8), Apache-2.0 (5), BSD-3-Clause (2), MIT-code-with-CC-BY-4.0-data or
-content (5), GPL-3.0 (1 — `LTIPlugin`, new in p320) — 21/21 usable, 15/21 under a pure permissive
software licence.** The GPL-3.0 row is the first copyleft entry this file has ever carried, and it
is carried deliberately: **a copyleft licence is a constraint on how you deploy, not a bar on
reading or running it.** Keep it behind a process boundary and it stays usable; link it into a
client deliverable and it does not. The five dual-licensed rows
(the three `bncc-dev` repos, `argmin`, and by extension the eval tier in `agents/top.md`) are the
new shape in this file and they need handling: **CC BY 4.0 is attribution-only, so the data is
commercially usable, but it is data, and the attribution has to appear in the deliverable.** Put
the credit line in the product, not in a licence register nobody reads.

The structural fact is unchanged: **the copyleft in this industry lives entirely in the LMS/platform
tier** (`verticals/solutions.md`), and everything you would put *under* a product is permissive.

## Pass 323: the Tsugi question, closed with a negative answer — and what it does to the LTI risk

p319 recorded Tsugi as *"the newly recorded alternative"* to `pylti1.3`, **"with an unresolved
question about which LTI versions it implements."** p322 carried the question forward untouched.
**Read first-hand this pass, and the repository does not answer it.**

| | `pylti1.3` | `tsugiproject/tsugi` |
|---|---|---|
| Licence | MIT | **Apache-2.0** (sidebar) |
| ★ / forks | 138 / 84 | **376 / 266** |
| Commits | 178 | **4,011** |
| Published release | **none** | **none** — Releases section empty |
| LTI version stated | LTI 1.3 (by name) | **none stated anywhere in the README** |

The closest the README comes is *"Tsugi is a multi-tenant scalable LTI library and tool hosting
environment"* and *"this code also implements an IMS ContentItem App store."* **ContentItem is the
LTI 1.1-era content-selection message**, which hints at the older generation without declaring it.
None of LTI 1.1, LTI 1.3, LTI Advantage, Deep Linking, Names and Role Provisioning Services or
Assignment and Grade Services appears in the text.

**Three consequences, in the order they bite a bid:**

1. **An LTI integration cannot be scoped from Tsugi's README.** Version support has to be
   established by reading 4,011 commits of source or by asking the maintainer. That is a
   discovery task with an unknown answer, not a dependency choice — **price it as the former.**
2. **The LTI 1.3 concentration risk this KB has flagged for four passes is unrelieved and should
   now be stated at full strength:** one maintained library carrying the integration seam
   (`pylti1.3`, MIT, 39 open issues, **no release tags**), a substantial Apache-2.0 alternative that
   does not say what protocol version it speaks, and **three artefacts at the agent end of the same
   seam with no licence at all** (`blamb/lti-tutor`, `Plugin-Feedback-Canvas`, and the pattern
   recorded in `agents/top.md`). **Nothing at this seam has a release tag.**
3. **It strengthens the case for avoiding the seam entirely where the client allows it.** This is
   the architectural argument behind **P8** (permissive-LMS build, no LTI boundary) and trend 6
   (**MCP, not LTI, is where agent integration is actually happening**). Tsugi's silence is not a
   defect in Tsugi — it is a 4,011-commit project that predates the question. **It is evidence that
   the LTI ecosystem's documentation layer has not followed LTI 1.3**, and that is the risk to carry
   into a bid.

**Recorded so p324 does not re-open it:** the question is answered as far as the README can answer
it. The remaining way to resolve it is reading `src/` or contacting the maintainer, and **that is a
task, not a search.**

## Declared gaps — pass 323, searched and measured

- **No permissively licensed verified curriculum dataset outside Brazil.** Two countries have built
  the artefact; **exactly one licensed the data for commercial use.** Searched: `curriculum
  knowledge graph`, `prerequisite dataset`, NCERT and CBSE by name, and the Chinese PEP artefact by
  name. This is now the precise form of trend 12's claim.
- **No licensed NCERT/CBSE curriculum artefact.** The one that exists (`razi-03/NCERT-CKG`) has no
  LICENSE file, two commits and one grade of one subject.
- **No public code for EduClaw-Bench, EduFair-Bench or ELBench** — three 2026 education benchmarks,
  three papers, zero repositories (`agents/top.md`).
- **No release tag anywhere at the LTI seam.** Both libraries, neither tagged.
- **Still-unswept GitHub-topic languages, corrected.** p319's untested list read *Arabic, Hindi,
  Japanese, Korean, French, Indonesian*. **Chinese was never on it and should have been** — it holds
  the largest curriculum artefact in this file, and this pass found it **in English**, which is its
  own small lesson about when the language sweep is and is not the binding constraint. The six
  languages above remain unswept.

## The `bncc-dev` stack — the artefact every pattern in this KB assumed a client would supply

Three repositories under the `bncc-dev` organisation, maintained by **Profy Tecnologias
Educacionais Ltda** (Brazil), together do what no other source in this sector does: they turn a
**national curriculum standard into verified, machine-readable, permissively licensed
infrastructure, and then measure what it is worth.**

**1 — The data (`bncc-dados`, 22 ★, 40 commits).** 1,721 learnings: 1,580 from the BNCC's three
stages of basic education (Educação Infantil 93 objectives, Ensino Fundamental 1,304 skills, Ensino
Médio 183 skills) plus the **141-item Computing complement** added by Parecer CNE/CEB 2/2022, with
20 legal milestones and 5 reference profiles. JSON is canonical; SQLite, a SQL dump and CSV are
generated; JSON Schemas are draft 2020-12. Content version `dados-2026.08`, schema v1.1.0, declared
stable.

**The verification discipline is the part to copy.** Per its own documentation: the 1,580 BNCC-2018
texts were checked **character by character against the homologated PDF**; the 141 Computing texts
against the Parecer's annex; a code sweep confirms no missing or extra codes; `validar.py` runs
**30 contract and completeness checks**; the pipeline is reproducible and **CI fails on
divergence**; and every decision taken about an inconsistency in the source is recorded in
`DECISOES.md`. Licensing is split deliberately — **MIT for the pipeline, CC BY 4.0 for the data**,
on the stated reasoning that the compilation, structure and curation are Profy's work while the
normative BNCC texts are official acts.

**2 — The interfaces (`bncc-pacotes`, 9 ★, 103 commits).** npm `@bncc/dados` 0.7.0 (typed API,
embedded data), npm `@bncc/mcp` 0.6.0 (**MCP server with seven tools**: `bncc_lookup`,
`bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`,
`bncc_progressao_ei`), PyPI `bncc` 0.5.0, plus a **hosted MCP endpoint at `mcp.bncc.dev` on
Cloudflare Workers that needs no API key**. Embedded data is synced from a pinned `bncc-dados`
commit with version and checksum records in each package's `dados/VERSAO.json`. A well-formed code
that is absent returns an explanatory error rather than `null` — a small decision that prevents a
tutor from silently inventing a standard.

**3 — The measurement (`bncc-benchmark`, 9 ★, 82 commits), and this is the number to take to a
client.** The benchmark asks models about BNCC codes and texts with no access to the source, across
four tasks: direct lookup, **existence (which tests whether a model accepts plausible fake codes)**,
open generation, and reverse lookup. Score is the mean of five dimensions — recognising real codes,
rejecting fake ones, text fidelity, reverse lookup, correct citation in open generation. A held-out
item set is never published so memorisation remains detectable, and v0.3.0 moved to direct provider
APIs and corrected the judge rubric, making it incomparable with v0.2.0.

Its **grounding study (8 models, 300 items)** reports:

| Condition | Hallucination rate |
|---|---|
| No source available | **31.9%** |
| Curriculum data pasted into the prompt | **0.2%** |
| Model queries the `bncc.dev` MCP server | **2.3%** |

— an average drop of **30.6 points**. A 95% bootstrap confidence interval is reported; its bounds
are not shown on the page.

**This is the first quantified grounding claim in this KB.** Every pattern here has asserted that
retrieval grounding matters; now there is a published, reproducible, regionally specific number for
how much, on a national curriculum, with the MCP route costing about 2 points against pasting the
data in. Use it: *"on Brazil's national curriculum, an ungrounded model invents a standard about a
third of the time; querying the verified source takes that to roughly two percent."*

**Three caveats, stated because the repository states them:**

- **The maintainer declares a conflict of interest.** Profy ships commercial products that run LLMs
  on the BNCC. The disclosure is in the repository; treat the benchmark as credible-and-interested,
  the way you would a vendor-run benchmark that publishes its method and its held-out set.
- **The page's own totals disagree.** The README describes the official round as 19 models × 900
  responses with 17,100 raw responses published; the About line says 15,300 responses from 17
  models. **Cite the round identifier (`oficial-seca-2026-09`) and the per-model design, not the
  total**, until the discrepancy is resolved.
- **Model-level results are a snapshot and the labels are the benchmark's own.** Its published
  top five are GPT-6 Astra 94.7 (88% faithful text, 3% fake-code acceptance), Claude Fable 5.1 81.8
  (80%, 0%), Muse Spark 1.3 79.4 (73%, 10%), Gemini 3.1 Pro 78.0 (67%, 3%) and Claude Opus 5 76.8
  (71%, 4%), with faithful-text rates across all models ranging from 88% down to **3%**. **The
  ranking will be stale within a quarter; the 88%-to-3% spread will not be** — and that spread,
  not the leaderboard, is the argument for grounding over model selection.

**Why this is in the foundations file and not the market file.** It is a dependency you would put
under a product today: the data is CC BY 4.0, the code is MIT, the MCP server is hosted and
keyless, and nothing about it is experimental. For any engagement touching Brazilian basic
education — public-sector, private-network or edtech-vendor — **this is the curriculum spine, and
the benchmark is the acceptance test.** See pattern **P10**.

## The pylti1.3 concentration risk now has a real alternative, not just an index

Pass 317 flagged this and it remains the correct thing to worry about: **every pattern in this KB
crosses the LMS boundary through `pylti1.3`** — one MIT library, 138 stars, 178 commits, a single
maintainer and 39 open issues with no visible release cadence. That belongs in the risk section of
any SOW that depends on it, and it still does.

**Pass 319 found the alternative itself: `tsugiproject/tsugi` — Apache-2.0, 376 ★, 266 forks,
4,011 commits, Apereo Incubating.** It describes itself as "a multi-tenant scalable LTI library and
tool hosting environment", doubles as an administration/management/developer console, implements an
**IMS ContentItem app store**, shares low-level IMS libraries with Sakai, and is maintained around
**Dr Chuck — Charles Severance, co-author of the LTI specification**. It keeps per-PHP-version
branches (`master`, `php-80-x`, `php-74-x`, `php-72-x`) and its README notes production servers
pulling updates every 30 minutes.

**Against `pylti1.3`'s 178 commits and single maintainer, that is a different class of artefact** —
and it is Apache-2.0, which is the tier Globant prefers. **Two honest caveats:**

- **Its GitHub page does not state which LTI versions or Advantage services it implements.** No
  mention of LTI 1.3, Advantage, Deep Linking, AGS or Names and Roles; ContentItem is
  Deep-Linking-adjacent but not the same claim. **Verify the Advantage surface against the
  repository and the Tsugi documentation before it goes in a proposal** — this is the single
  highest-value verification item for pass 320, and it is one page load.
- **It is PHP.** For a Python shop that is a real cost; for a client already running Moodle or any
  PHP stack it is an advantage.

Also recorded for integration breadth: **`jcputney/scorm-again` (MIT, 356 ★, 1,229 commits)**, a
tested JavaScript runtime for **SCORM 1.2 and SCORM 2004**, LMS-agnostic, which reaches the large
installed base of SCORM courseware that LTI does not. **AICC support was removed in v3.0.0, and
cmi5/xAPI are roadmap "potential" only** — do not promise either.

Carried from pass 318: **`1EdTech/ltibootcamp`** (127 ★, 47 commits), a curated index of LTI 1.3
implementations maintained under the **1EdTech GitHub organisation** — the standards body itself.
It maps the library landscape across seven languages:

| Language | Implementations it names |
|---|---|
| Python | **PyLTI 1.3** (Flask/Django examples), UCF Flask starter template, `django-lti`, Robotest test tool (FastAPI), Open Learning LTI 1.3 Platform (Django) |
| JavaScript / Node | **ltijs** (1.3 core and services), Blackboard Node tool provider, Atomic LTI Worker |
| PHP | IMS 1.3 library and demo tool, TAO hosted test platform, OAT libraries (1.3 core, Deep Linking, Names & Roles, Symfony bundle) |
| Java | Unicon Spring Boot demo, UOC LTI 1.3 library + Spring Boot library + provider example |
| .NET | `LtiAdvantagePlatform` example platform (andyfmiller) |
| Ruby | Atomic Jolt LTI starter app |
| Rust | Atomic Forge |
| Other | An AWS LTI "shim" service |

**Three caveats, and they are not small:**

- **The repository itself has no LICENSE file.** It is an index of links, so there is little to
  licence, but it cannot be vendored and it is not in the table above for that reason.
- **It is stale.** Its only two content folders are `barcelona_2019` and `europe_tech_2020`, and
  it carries 47 commits. Entries may be dead; the LTI 1.3 specification has moved since 2020.
- **Its own README disclaims vetting:** *"The resources listed here are for information only and
  have not been vetted."* It sits under the 1EdTech organisation but reads as a community-curated
  list open to pull requests — treat it as a starting index, not a standards-body endorsement.

**What it is worth anyway:** the mitigation question for `pylti1.3` was previously answered with a
hand-wave ("reference implementations exist in other languages"). It now has specifics. If a
client's stack is Node, **`ltijs`** is the route — and it is the library `blamb/lti-tutor` chose to
implement working deep linking and AGS passback against Moodle (see `agents/top.md`). If the stack
is Java, the UOC libraries are the named option. **Verify any entry against its own repository
before scoping on it**; the index is five years stale and unvetted by its own admission.

## The method that found most of pass 319: search GitHub topics in the region's own language

This KB has written "a star-ranked search cannot see this sector's infrastructure" for three passes
without changing its search. Pass 319 changed it: **GitHub topic pages were swept in Portuguese,
Spanish, German and Dutch, and in the two curriculum-specific Indian tags.** The results are
asymmetric, and the asymmetry is itself a regional finding.

| Topic swept | What it surfaced |
|---|---|
| `educacao` (pt) | **Infrastructure.** `portabilis/i-educar` (720 ★, **34,948 commits**, school management, `verticals/solutions.md`), `portabilis/i-diario` (117 ★, 15,834 commits), `ipti/br.tag` (20 ★, 3,959 commits, offline sync for rural schools), and **the entire `bncc-dev` curriculum stack** |
| `educacion` (es) | **Teaching materials, almost exclusively.** 370 repos; the top entries are Spanish-language JavaScript and Python course guides, a Moodle–SENCE attendance plugin (29 ★), vocational-training course material, a Uruguayan school-finder (`datauy/ElijoEstudiar`, 5 ★). **No AI infrastructure, no curriculum data** |
| `ncert` + `cbse` (India) | **Hobby projects.** 55 + 125 repos; nothing above 15 ★ that is curriculum infrastructure. Detail in `agents/top.md` |
| `bildung` (de) | **One usable asset and one warning.** `smashburger-dev/argmin` (MIT + CC BY 4.0, 343 commits, German AI course, offline-capable) and `davidpomerenke/lernplattform` (GPL-3.0, **archived 2021-01-01**, which pointed to "wir lernen online" as its successor). Also **a 13-repository single-author cluster of near-identical "tech evangelism" pages at 1 star each** — topic pages can be padded, which is one more reason the ★ column is noise |
| `onderwijs` (nl) | **Rostering glue, no AI.** `sikkepitje/TeamSync` (9 ★, PowerShell, syncs Magister school records into Microsoft School Data Sync) and two open secondary-school course repos (`wiskunde.opmaat`, `natuurkunde.opmaat`) |
| `oer` (en, for contrast) | 419 repos of **textbooks and course materials**, nothing describing curriculum or competency metadata, and no AI |
| `pendidikan` (id) | **42 repos, and exactly one AI artefact.** `RozhakDev/EduPintarIPAS` (**MIT**, 20 ★, **1 commit**, Flask, **Azure AI Language Custom Question Answering**) answers `IPAS` science-and-social-studies questions for Indonesian year-6 pupils off a QA set the README says was built from the official `SD` curriculum, and is aimed explicitly at **3T regions** (*tertinggal, terdepan, terluar* — underdeveloped, frontier, outermost) where tutoring is scarce. Everything else in the topic is school administration at 0–4 ★ — enrolment (`PPDB-online`), tuition (`aplikasi-spp`), facilities (`sisp`), a boarding-school monitor. **The curriculum-grounded-QA pattern exists in Indonesian; the engineering behind it does not — one commit is a demo, not a dependency** |
| `enseignement` (fr) | **40 repos, zero AI.** Almost entirely teaching material for the French system: the `NSI` computer-science specialism at lycée, `CAPES` oral topic lists, LaTeX maths and geometry courses, a Python teaching IDE (`Pydiderot/pydiderotIDE`). The one infrastructure artefact, `ValbionGroup/Gadia` (**MPL-2.0**, 6 ★, 63 commits, Laravel/Blade school-life management — timetable, class notebook, grades, absences, canteen), was **archived by its owner on 2025-10-28 and is read-only**, and its README already warned the features were not guaranteed. **France's tag is pedagogy, not platform** |
| `kyoiku` (ja) | **1 repo, 0 ★.** `mitsurutech/joho-puroguramingu-renshu` — 48 Python, SQL and web (HTML/CSS/JS) exercises for Japanese high-school *jōhō*, starter code, deliberately no solutions. No AI, no infrastructure |
| `gyoyuk` (ko) | **The topic page exists and holds 0 repositories.** GitHub's own wording: "hasn't been used on any public repositories, yet". **This is the cleanest negative in the table — not a thin result, an empty one** |
| `shiksha` (hi) | **3 repos, ceiling 3 ★.** `arhaanb/shiksha` (3 ★, last touched 2022-04-07), `shiksha-platform/documentation` (1 ★, 2022-01-20, no description) and an **archived** `.shiksha` domain-name extract. No AI, and the two real ones have been untouched for four years |
| `taleem` (ar/ur) | **1 repo, 1 ★** — an Urdu-language Islamic blog of 370+ articles on static HTML. **Not education infrastructure, and the slug does not answer the Arabic question** — see the slug finding below |

**Two conclusions, and the second is the commercial one.**

1. **Adopt this as standing method.** Every regional gap this KB has declared was declared from
   English-language searches. One Portuguese topic page produced a verified national curriculum
   dataset, an MCP server, a published benchmark and a 34,948-commit SIS. **Before declaring a
   regional absence, sweep the topic in the region's language** — and record which language you
   swept, so the next pass knows what was actually tested.
2. **The gap is not uniform, and it is not about talent.** Brazil has curriculum-standard
   infrastructure because someone built it to a verification standard and licensed it cleanly.
   Spanish-speaking LATAM, India, Germany and the Netherlands do not have an equivalent — in the
   topics swept — and in India's case there is a hard curriculum mandate arriving in 2026-27 with
   nothing underneath it. **That is a build-once opportunity with a named template** (`bncc-dev`)
   and a named buyer (any ministry, board or national edtech with a mandate and no data layer).
   Pattern **P10**.

**Limits of the claim, stated so pass 320 does not over-read it.** These were topic-page sweeps of
the first ~20 repositories per topic, not exhaustive searches; GitHub topics are
author-applied, so an unlabelled repository is invisible to this method; and only six topics in
five languages were swept. **"Not found in the topics swept" is the finding. "Does not exist" is
not.** Untested and worth a pass: Arabic, Hindi, Japanese, Korean, French and Indonesian topic
tags, and the `wirlernenonline` organisation, whose GitHub org page could not be read this pass.

## Pass 322: `openeduhub` enumerated in full — and the inference core is the unlicensed part

**All 67 public repositories were enumerated this pass**, closing p321's declared gap
(*"57 of the 67 were not listed on the first page and remain unenumerated"*). The method matters
because it is reusable: **the org listing had to be paged under two different sort orders.** Sorted
by stars, the first page shows the metadata plumbing of 2020–2023; sorted by last push — the default
— the first page shows the AI-era services, and **six of the twelve repositories added above do not
appear on the star-sorted first page at all.** A star-ranked sweep of this organisation finds the
dead code and misses the live pipeline.

### What the org actually is, by date rather than by star count

| | Count |
|---|---|
| Public repositories | **67** |
| Pushed in 2026 | **17** |
| Last pushed 2020–2022 | **30** |
| Archived | **5** (`metaqs-api-old`, `metaqs-frontend-old`, `oeh-search-editor-backend`, `oeh-metadata-specs`, `wlo-chat-gpt-block`) |
| Read first-hand by this KB | **16** — four at p321, twelve at p322 |

**The archived list contains the org's first AI attempt.** `wlo-chat-gpt-block` (JavaScript, last
touched **August 2023**, archived) is a WordPress ChatGPT block. The line that replaced it is the
metadata-agent line read above — **extraction, review and classification, not conversation.** A
public operator tried the chatbot first, archived it, and spent the next three years building a
metadata pipeline instead. That is the single most useful thing in this pass for a studio pitch, and
it is recorded as a trend reading in `intel/trends.md`.

### The finding: licence divides by architectural layer

| Layer | Commits | Licence | What it means for an engagement |
|---|---|---|---|
| Shells — review UI, REST wrapper, browser plugin, path editor, tutor, judge, source registry, dedup | 60 + 11 + 6 + 10 + 1 + 6 + 25 = **119** | **Apache-2.0**, or claimed as such | Take them. Two of the seven claim a licence the repository does not carry — check before you ship |
| Analysers and classifiers | 623 + 94 + 73 = **790** | 🟡 **GPL-3.0** | Run as services behind a process boundary; never link |
| **Inference core** — gateway, Bayesian predictor, text extraction, bulk prompt runner, QA generation, harvester | 137 + 200 + 77 + 37 + 4 + 1,397 = **1,852** | 🔴 **none** | **No grant. Reimplement, or negotiate a licence with the operator** |
| API client | **519** | **Apache-2.0** | Take it — and it is the only large permissive artefact in the org |

**The permissive surface contains none of the organisation's machine learning.** Every model, every
harvester and the gateway that fronts them is unlicensed; the Apache-2.0 repositories are
interaction layers of between 1 and 60 commits. Pass 321 read the one unlicensed repo it found as a
lapse. Over sixteen reads it is not a lapse — **it is where the org's effort went, and the licence
file is what never followed it.** For Globant this is the rare case where the *engagement* is the
finding: a public operator sitting on 1,852 commits of unlicensed, publicly funded ML is a
licence-remediation conversation, not a fork.

### The README-versus-LICENSE hazard, four instances in one org

`duplicate-detection` and `wlo-quellenliste` both say **MIT** in the README and ship an
**Apache-2.0** `LICENSE`; `metadata-agent-api` says **MIT** with **no licence file in the root**;
`metadata-agent-canvas` says **Apache-2.0** with **no licence file in the root**. The `LICENSE`
file of `duplicate-detection` was opened and read first-hand to settle it — it is the Apache 2.0,
January 2004 text. **Rule applied from here: the licence file governs; a README claim with no file
behind it is not a grant.** Two of these four understate the grant and two assert one that does not
exist, so the error is not conservative in either direction.

### Declared gaps from this pass — searched, measured, not found

| Gap | What was measured |
|---|---|
| `openeduhub/wlo-topic-assistant` | **404.** `python-kidra` advertises it as one of seven bundled services; it has no public repository under this org |
| `kea` (Wikipedia article linking) | Not a repository in this org — `python-kidra`'s README says requests are **forwarded to an external service**, which this KB has not identified |
| `z-api-runner`'s LLM backend | **Unstated** in the README; `app/` and `requirements.txt` were not read, so the model and provider are unknown |
| `metalookup`'s extracted field list | In `docs/features.md` and `docs/acceptance.md`, **not read this pass** — so this KB has the capability but not the field schema |
| `wlo-quellenliste`'s JSON/CSV field schema | **Not documented** on the repository page; would need the code or the live API docs |
| `topic-statistics`, `its-prep`, `its-data`, `mappings`, `skohub-vocabs-oeh-patched`, `oeh-search-frontend` | Named in the census, **not read.** Listed so pass 323 does not re-discover them — `topic-statistics` and `its-prep` are the two that `python-kidra` depends on |
| Non-GitHub primary sources | Still unreachable. `www.digitaleducationcouncil.com` failed at DNS this pass; **everything in `intel/` remains snippet-sourced** |

## Pass 321: the p319 to-do list, executed — and the Germany claim it corrects

Pass 319 ended its sweep section with a named to-do: *"Untested and worth a pass: Arabic, Hindi,
Japanese, Korean, French and Indonesian topic tags, and the `wirlernenonline` organisation, whose
GitHub org page could not be read this pass."* **All seven were attempted at p321.** Six are
negatives and are in the table above, written down rather than left as silence. The seventh is the
find of the pass.

### 1. The correction: Germany *does* have a competency-metadata layer, and this file said it did not

Pass 319 concluded, from the `bildung` and `oer` sweeps, that **"Spanish-speaking LATAM, India,
Germany and the Netherlands do not have an equivalent"** to Brazil's `bncc-dev` curriculum stack,
and that the `oer` topic held "nothing describing curriculum or competency metadata." **For Germany
that is now wrong, and the artefact is better licensed than the Brazilian one.**

`openeduhub/oeh-metadata-vocabs` is **CC0-1.0** with **938 commits** and carries SKOS vocabularies
for educational context, level, discipline and school type, rights and copyright restriction, cost
and price, machine-readable quality criteria, and the **DigCompEdu, ESCO and EQF/DQR competence
frameworks** — published under a stable `w3id.org` namespace with a browsable SkoHub front end.
That is a competency-metadata layer by any reading.

**Why p319 missed it, and the lesson is about method rather than luck.** The repository is tagged
for neither `bildung` nor `oer`; it lives in an organisation p319 looked for **under the wrong
name**. `github.com/wirlernenonline` is **404**. The account is `openeduhub`, and the only way this
pass reached it was by searching the *project* name and reading the owners off the results. **A
topic sweep cannot see an untagged repository, and an org sweep cannot see an org whose GitHub
handle differs from its public brand.** Both failure modes are now demonstrated, not hypothesised.

### 2. The slug finding — why "sweep the topic in the region's language" needs one more rule

`https://github.com/topics/教育` returns **404**. GitHub topic slugs are ASCII-normalised, so a CJK
term cannot be typed in as a topic even when it is the word the region actually uses. The sweeps
that worked were the **transliterations** — `kyoiku`, `gyoyuk` — and one of those turned out to hold
zero repositories. So p319's standing method gains a clause: **sweep the region's language, and for
non-Latin scripts sweep the romanisation, because the topic namespace will not accept the script.**
Pass 319 could not have discharged "Japanese, Korean" by typing the obvious thing.

### 3. What `openeduhub` is, and why a 0 ★ org is worth a section

**67 public repositories.** The org profile describes itself as the account behind
WirLernenOnline.de: *"This OER-Infrastructure makes (O)ER findable and usable in connected
platforms,"* based on **edu-sharing**, WordPress and others — i.e. Germany's publicly funded open
educational resources portal, with its plumbing on GitHub. Four repositories were read first-hand
this pass:

| Repo | Licence | ★ | Commits | What it is |
|---|---|---|---|---|
| `oeh-metadata-vocabs` | **CC0-1.0** | 2 | **938** | SKOS/Turtle vocabularies incl. DigCompEdu, ESCO, EQF/DQR — see the row above |
| `oeh-search-etl` | 🔴 **none** | 8 | **1,397** | Scrapy → Postgres → Elasticsearch harvester — see the row above |
| `tutor-chatbot` | **Apache-2.0** | 0 | 10 | RAG tutor over the WLO API with Bloom-taxonomy analytics — `agents/top.md` |
| `ki-prompt-benchmark` | **Apache-2.0** | 0 | 3 | LLM-as-judge prompt bench, exports `mds.xml` — `agents/top.md` evaluation table |

Also present and unread at p321, named here so p322 does not re-discover them: `metalookup`
(5 ★, Python, domain metadata including licensing), `oeh-search-frontend` (5 ★, TS),
`edu-sharing-python-client` (0 ★), `lernpfadeditor` (learning-path editor with differentiation and
content assignment), `wlo-quellenliste`, `metadata-browser-plugin-fuerAPI`. **57 of the 67 were not
listed on the first page and remain unenumerated.**

**The star counts are 0, 0, 2 and 8, and that is this KB's Ed-Fi lesson repeating in a second
jurisdiction.** The Ed-Fi section below makes the argument from 12 ★ and 6 ★ of US state-adopted
infrastructure. `openeduhub` makes it again from a German federal-state-funded portal with a
1,397-commit harvester at 8 ★. **A star-ranked search cannot see publicly funded education
infrastructure in any region, and two independent instances is no longer a coincidence.**

### 4. The licence split inside one org, which is the practical warning

The same organisation ships **CC0-1.0**, **Apache-2.0** and **no licence at all**, and the
unlicensed repository is the one with the most commits. **Do not infer an org-level licence
posture from one repository.** On this evidence the rule for `openeduhub` is: take
`oeh-metadata-vocabs` (CC0) and the two Apache-2.0 tools freely; treat `oeh-search-etl` as
documentation of a harvesting design and **write your own**, or open an issue asking for a licence
before any engagement depends on it.

## The Ed-Fi finding — the gap this KB declared three passes running, closed in p316

The Ed-Fi Alliance publishes its platform as Apache-2.0 under the `Ed-Fi-Alliance-OSS` GitHub
organisation. The Data-Management-Service has 1,105 commits; `edfi-oneroster` serves OneRoster 1.2
off an Ed-Fi ODS and has 151. Both are Apache-2.0 — the licence tier Globant prefers.

**The stars are 12 and 6, and that is the whole lesson.** A star-ranked search systematically
cannot see public-sector education infrastructure, because it is adopted through state education
agencies and SIS vendors rather than through GitHub. **Pass 318 added a fourth confirmation of
this** — `openedx/openedx-ai-extensions`, the official Open edX AI plugin, has **17 stars and 703
commits** (see `verticals/solutions.md`) — and a fifth datapoint from the opposite direction: a
repo in this sector now openly solicits stars from AI agents (see `agents/top.md`). **Rank
candidates on commit count, release cadence and licence. Stars are noise in both directions.**

Two caveats before scoping on Ed-Fi:
- Neither repo has a published release on its GitHub Releases page. Pin to a commit, not a tag.
- Ed-Fi is a **North American** standard in practice (US state education agencies). It is not a
  route into EMEA, APAC or LATAM rostering, and nothing equivalent was found for those regions.

## Caveats

- **Sunbird's 41 ★ are not a quality signal**, for the same reason Ed-Fi's 12 are not. Government
  adjacent infrastructure in India, adopted through state deployments. Verify the wider
  `Sunbird-Ed` org's component repos before scoping.
- **`ai-agents-for-beginners` is a curriculum, not a library.** It sits here deliberately: 77.5k ★
  of MIT teaching material is a reusable asset for the "train the client's team" phase that ends
  most education engagements.
- **`pylti1.3` is the most load-bearing 138 stars in this KB.** See the mitigation list above.
- **LightRAG + DeepTutor remains the highest-leverage pair in this KB.** Both from HKUDS, both
  permissive, ~82k ★ between them, covering retrieval and tutoring. Pattern P1 is built on it.
  DeepTutor was re-verified p318 (v1.6.15, 2026-10-19); **LightRAG was re-verified first-hand in
  p319 — MIT, 40.2k ★, 5.7k forks, 10,873 commits, unchanged. That re-read is now done.**
- **Kolibri's README describes no AI features.** Re-read first-hand this pass. It is the delivery
  substrate for offline contexts; the intelligence layer is yours to add, which is exactly why it
  is in this file and not in the agent tier.

## Declared gaps — searched, not found

- **No foundational open source repo for student-data privacy compliance** (FERPA / COPPA / GDPR
  record handling). **Sixth pass declaring it — and the first pass where the gap is contested
  rather than empty.** GitHub's `ferpa` topic now holds about a dozen governance projects created
  or last updated in September–October 2026, **every one of them at 8 stars or fewer**: Rego policy
  packs (`Principled-Evolution/gopal`), PII-scrubbing ingestion with hash-chained audit trails
  (`marc-shade/docsingest`), identity-scoped RAG patterns and policy middleware (three repos by
  `ashutoshrana`, the same author as p317's `haystack-ferpa-filter`), a FERPA-safe Canvas toolkit
  (`chaz-clark/canvas-toolbox`), Bedrock agents with PII masking (`virtualryder/edu-ai-agents`) and
  an MCP server that audits tutors for FERPA/COPPA (`mizcausevic-dev/mcp-ai-tutor`).
  **None is a dependency.** But a dozen independent authors starting the same component within two
  months of the **COPPA compliance deadline of 2026-04-22** (see `intel/market.md`) is a market
  forming in real time. The build-once opportunity is still the clearest in the sector and the
  window on it is now visibly shorter. Note that Ed-Fi gives you the data *model* and API, not the
  consent, retention and disclosure machinery around it.
- ~~**No LATAM-authored foundational repo.**~~ **CLOSED PROPERLY THIS PASS, and the correction is
  worth stating precisely because this KB has now been wrong about it twice.** Five passes declared
  the gap. Pass 318 found `openedx/openedx-ai-extensions` (eduNEXT, Bogotá) and had to disqualify it
  from this file: AGPL-3.0 and explicitly not for production. **Pass 319 found three Brazilian
  repositories that qualify without caveats** — `bncc-dados`, `bncc-pacotes` and `bncc-benchmark`
  (Profy, MIT code / CC BY 4.0 data, verified against the homologated curriculum PDF, a hosted MCP
  server, a published benchmark). They are infrastructure, they are permissive, they are
  production-usable today, and **they were found by searching a Portuguese-language GitHub topic.**
  The backdrop figures still stand (Linux Foundation, December 2025: **Mexico 65%, Brazil 46%** for
  organisational use of open source AI) and so does the commercial point — the named LATAM
  education-AI companies (Teachy, Ginia, Vetto, Mattilda, Luca, Letrus, MusíGlota) remain private
  and closed-source — but "LATAM consumes open source and does not write it" is finished as a
  sentence. **Spanish-speaking LATAM is a different matter: the `educacion` topic sweep found
  teaching materials and no infrastructure, so the regional finding is Brazil specifically, not
  LATAM generally.**
- **No EMEA- or APAC-equivalent of Ed-Fi — but the gap now needs splitting in two, because one half
  moved and the other did not.** On **rostering**, nothing comparable was found for Europe or Asia;
  the closest artefact is `sikkepitje/TeamSync` (9 ★, PowerShell, Magister → Microsoft School Data
  Sync), which is one country's glue script, not a standard. On **curriculum standards**, Brazil now
  has `bncc-dev` and **nobody else in this KB does** — the German attempt (`lernplattform`) was
  archived in 2021, the Dutch and Spanish-language topics produced course material rather than data,
  and India's NCERT/CBSE repositories are hobby-scale with no verified dataset at all
  (`agents/top.md`). **Ed-Fi remains North-America-only, and it is a data model plus API, not a
  curriculum.** The two gaps are different products and should be scoped separately.
- **elimu.ai's region is not stated and should not be assumed.** Its GitHub organisation page gives
  its location as "Worldwide"; the `webapp` repository lists production deployments for **Hindi,
  Tagalog, Thai, Vietnamese and English**. This KB has an open MENA/Africa supply gap
  (`verticals/solutions.md`) and elimu.ai does **not** close it on the evidence read this pass —
  its documented deployments are APAC-language-first. Recorded here so no proposal cites it as an
  African platform without checking.
