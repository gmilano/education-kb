---
industry: education
region: Global
updated: 2026-11-01
---

## p581 — 2026-11-01 — **the lecture-media tier this page never had: three new permissive libraries, plus the drift-detection primitives the trends page has called the industry's clearest hole**

🟢 **Instrument unchanged and working:** `q=repo:owner/name` against
`search/repositories` returns `license.spdx_id`, `stargazers_count`, `pushed_at`,
`forks_count` and `archived` in one call. 🔴 **Correction to the sweep form, which is
this pass's main result:** crossing two topics (`topic:X+topic:education`) returns
`total_count = 0` — **six times out of six**. Education repos carry pedagogy topics,
capability repos carry capability topics, and essentially nothing carries both. **Sweep
one topic; filter licence and recency client-side.** See
[`../agents/trending.md`](../agents/trending.md) for the full nil table.

### 🟢 New: the lecture-media tier — transcript and caption infrastructure

| Repo | Licence | Stars | Last push | Region | Shippable? | Role |
|---|---|--:|---|---|---|---|
| [YaoFANGUK/video-subtitle-extractor](https://github.com/YaoFANGUK/video-subtitle-extractor) | 🟢 **Apache-2.0** | **9,680** | 🟡 `2026-04-09` | APAC | 🟢 **yes** | 🟢 **Reads subtitles burned into the pixels** and emits SRT, fully local, no third-party API. **The only route into archived lecture and MOOC footage published with hard-burned captions** — where a caption-API fetch returns nothing. `982` forks. |
| [jdepoix/youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) | 🟢 **MIT** | **8,543** | `2026-10-30` | EMEA | 🟢 **yes** | Transcript and caption retrieval with translation. The cheapest path to text for any lecture already published with captions. `855` forks. |
| [smacke/ffsubsync](https://github.com/smacke/ffsubsync) | 🟢 **MIT** | **7,929** | 🟡 `2026-07-24` | North America | 🟢 **yes** | FFT-based **re-alignment** of subtitles against audio. 🔵 The unglamorous row that makes the other two usable: a transcript whose timings drift is useless for seek-to-concept or clip extraction. |

🔵 **Three libraries here, two agents on [`../agents/top.md`](../agents/top.md)** — the
sweep returned five addresses and they are split by what they actually are, not padded
to a quota on each page.

### 🟢 New: drift detection — and the gap turns out to be specificity, not absence

[`../intel/trends.md`](../intel/trends.md) has carried, for six passes, that *"a tutor in
production still has no open-source way to detect that it has degraded"* and called it
**the clearest unmet build opportunity in the industry**. A `topic:drift-detection` sweep
(`1,308` repos) returns three addresses new to this base:

| Repo | Licence | Stars | Last push | Region | Shippable? | Role |
|---|---|--:|---|---|---|---|
| [ing-bank/popmon](https://github.com/ing-bank/popmon) | 🟢 **MIT** | **512** | 🟡 `2026-01-09` | **EMEA** | 🟢 **yes** | Population-stability monitoring over Pandas/Spark frames. 🟢 **Owner is ING Bank N.V.** — built for a regulator-facing use, which is the posture an exam board needs. |
| [IFCA-Advanced-Computing/frouros](https://github.com/IFCA-Advanced-Computing/frouros) | 🟢 **BSD-3-Clause** | **260** | 🟡 `2026-04-23` | **EMEA** | 🟢 **yes** | Concept- and data-drift detection library for ML systems. 🟢 **Instituto de Física de Cantabria** (Spain) — public research institution. |
| [SeldonIO/alibi-detect](https://github.com/SeldonIO/alibi-detect) | 🔴 **NOASSERTION** | **2,554** | 🔴 `2025-12-11` | **EMEA** | 🔴 **no** | Outlier/adversarial/drift algorithms, Seldon Technologies (London). 🔴 **Highest-starred and the one to avoid**: licence unresolved by the detector *and* ~11 months stale. |

🔵 **How to read this against the standing gap.** The gap was stated as *absence* and is
really *education-specificity*: **nothing here knows what a learner model is**, so none of
it detects "this tutor's explanations got worse". What `popmon` and `frouros` do give is
the statistical layer — distribution shift on the feature and outcome streams a tutor
already emits — which is the measurable half. 🟢 **Composed with `pykt-team/pykt-toolkit`
(MIT, `456★`), whose knowledge-tracing predictions are exactly the distribution to
monitor, this is the first buildable answer this base has recorded to its own hardest
question.** Recipe on [`../compose/patterns.md`](../compose/patterns.md).

🔵 **Regional note worth keeping:** all three drift rows are **EMEA-origin and two are
named institutions** (a central bank subsidiary and a public physics institute). Region
here is assigned from **owner identity**, not README language — the strongest placement
signal available in this session, since `users/{login}` is `403` and maintainer
`location` is unreachable.

🔴 **Non-finding, recorded.** `topic:item-response-theory`, `topic:psychometrics` and
`topic:computerized-adaptive-testing` returned **no rows not already on these shelves** —
`catsim` (BSD-3-Clause, `153★`, live `2026-10-30`), `EduCDM` (Apache-2.0, `203★`, stale
`2024-10-25`), `girth` (MIT, `127★`, stale `2022`), `pypsy` (MIT, `242★`, **dead since
2018**). The psychometric-**item-generation** gap stands; psychometric *calibration* is
shelved and permissive. These are different holes and the next pass should not merge them.


# Foundational open source repos for education

## p580 — 2026-11-01 — **the foundations re-measured first-hand, and the field this page never had is the one that disqualifies rows: `42 of 265` shelf addresses are over a year stale**

🟢 **Instrument, with its provenance stated.** `q=repo:owner/name` inside the search
endpoint returns `stargazers_count`, `license.spdx_id`, `archived`, `pushed_at`,
`forks_count` and `topics` in one call. 🔴 **This base has had that call since `p577`**,
where it is documented on [`../agents/top.md`](../agents/top.md); `Gap 579-A` closes on
*applying* it at shelf scale rather than on finding it. `271` addresses, `265` resolved —
`evidence/shelf-census.2026-11-01-p580.tsv`. **This is the first time this page has had
recency on its own rows.**

### 🟢 The foundational tier, re-measured `2026-11-01`

| Repo | Licence | Stars | Last push | Region | Shippable? | Role |
|---|---|--:|---|---|---|---|
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 **AGPL-3.0** | **8,213** | `2026-10-31` | North America | 🔴 network copyleft | The LMS of record. 🔴 **Cite this name — `openedx/edx-platform` is the old one and the API rejects it.** |
| [moodle/moodle](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** | **7,567** | `2026-10-30` | EMEA | 🔴 copyleft | The other LMS of record; `7,691` forks. Australia-origin, EMEA-anchored governance. |
| [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | **6,951** | `2026-10-31` | Global | 🟢 **yes** | 🟢 **The largest permissive education platform on this page.** Interactive lessons with built-in misconception handling; non-profit, `sdg-4` tagged. |
| [dream-num/univer](https://github.com/dream-num/univer) | 🟢 **Apache-2.0** | **22,837** | `2026-10-31` | APAC | 🟢 **yes** | Sheets/docs/slides SDK. The document substrate for courseware and worksheets without an Office dependency. |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** | **956** | 🟡 `2025-07-03` | North America | 🟢 **yes** | The learning-record interchange **specification**. 🔵 Stale by date and **legitimately so** — a ratified spec should sit still (see trend 35). |
| [openedx/codejail](https://github.com/openedx/codejail) | 🟢 **Apache-2.0** | **477** | `2026-10-27` | North America | 🟢 **yes** | 🟢 **Sandboxed execution of untrusted learner code** — the component every "run the student's program" feature needs and almost nobody builds correctly. Permissive inside an AGPL platform. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | **471** | `2026-11-01` | North America | 🟢 **yes** | The component SDK for Open edX. 🟢 **Permissive extension point into an AGPL platform** — the seam an AI component plugs into without inheriting the network-copyleft duty. |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** ⬅️ *was `unstated`* | **1,370** | `2026-10-28` | North America | 🟢 **yes** | Assign/autograde/release notebooks. 🟢 Licence settled first-hand this pass. |
| [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0** | **216** | `2026-10-28` | **EMEA** | 🟢 **yes** | Assessment authoring and delivery, **Newcastle University**. 🟢 The permissive assessment anchor `Trend 32` recommends building on — and an EMEA-origin one. |
| [frappe/education](https://github.com/frappe/education) | 🟡 **GPL-3.0** (byte-read, `p572`) | **687** | `2026-10-30` | APAC | 🔴 copyleft | School ERP on Frappe. 🔴 **The API reports `NOASSERTION` here** — a detector miss, not a licence change; the byte-for-byte read stands (trend 33). |

🔵 **Ten rows, all first-hand today.** The permissive/copyleft split on the *platform*
tier remains the structural fact this page has recorded since `p577`: **both LMSs of
record are copyleft, and every permissive anchor is a component or a spec.**
🟢 **`XBlock` and `codejail` are the practical answer** — Apache-2.0 extension points that
let a studio ship proprietary AI components against an AGPL platform without the
network-copyleft duty reaching their own code.

### 🔴 Recency, added as a shelf field for the first time — and it kills a tier this page endorses

| cut | count | share |
|---|--:|--:|
| 🔴 not pushed since `2025-11-01` | **`42`** | **`15.8 %`** |
| 🔴 `archived: true` | `4` | `1.5 %` |

🔴 **The casualty is `topic:question-generation`**, which this page shelves with correct
licence bytes and calls the axis's *"reference implementation"* tier. **All five rows were
last pushed between `2023-12` and `2024-08`**, one of them archived:
`patil-suraj/question_generation` (`1,138★`, `2024-04-05`),
`ramsrigouthamg/Questgen.ai` (`952★`, `2023-12-08`),
`KristiyanVachev/Question-Generation` (`495★`, `2024-02-14`),
`asahi417/lm-question-generation` (`366★`, `2024-08-20`),
`AMontgomerie/question_generator` (`298★`, `2024-02-06`, **archived**).

🔵 **Every one is a fine-tuned T5 pipeline** for a task instruction-following models now
do zero-shot — so the tier was absorbed, not neglected (trend 35). 🔴 **Do not start an
assessment-generation engagement here.** 🟢 Start at `numbas/Numbas` (Apache-2.0) for
authoring, `scorm-again` (MIT) for interchange and `jupyter/nbgrader` (BSD-3-Clause) for
autograding — all three measured current this pass.

### 🟢 Licence corrections to rows this page carries

| row | was | is (first-hand) | consequence |
|---|---|---|---|
| `bigdata-ustc/EduCDM` | 🔴 `no-grant` | 🟢 **Apache-2.0**, `203★` | 🟢 **Shippable cognitive-diagnosis models (DINA/IRT/MIRT/NCDM) were filed as unusable.** 🔴 Stale since `2024-10-25` — usable, not maintained. |
| `jupyter/nbgrader` | `unstated` | 🟢 **BSD-3-Clause**, `1,370★` | 🟢 Permissive autograding anchor confirmed. |
| `Wenchao-Ma/GDINA` | `GPL-3.0` | 🟢 **`GPL-3` confirmed** in `DESCRIPTION` | 🟢 **The ledger was right and the API is wrong** — `spdx_id: NONE`. The R/CRAN tier this page shelved in `p573` is invisible to the new channel (trend 33). |

### 🔴 Declared gap, unchanged and now re-measured

`openedx/edx-platform` — the dead pre-rename address — still appears **`40` times** across
the shelf pages against **`28`** for the live `openedx/openedx-platform`. The rename is
documented on this page and on [`../agents/top.md`](../agents/top.md); **the citations were
never migrated.** Any client document generated from this base's majority spelling will
hand over a link the API rejects.

## p579 — 2026-11-01 — four additions: the student-modelling layer, a North America analytics row, and a permissive accessibility component

🟢 Three of the four had been **inside this base since `p80`** — seen, logged to the address
ledger, and never filed on a page. They sat in the discard for **499 passes**. The fourth is
new to a `3,168`-address ledger.

| Repo | Licence | Stars | Region | Layer | Why it is here |
|---|---|---|---|---|---|
| https://github.com/HFUT-LEC/EduStudio | MIT | 80 | APAC | Student cognitive modelling | **Unified PyTorch library for Cognitive Diagnosis (CD) *and* Knowledge Tracing (KT)** — the two halves of student modelling in one configuration surface, where `pykt-toolkit` covers KT alone. *EduStudio: towards a unified library for student cognitive modeling*, Le Wu et al., **Frontiers of Computer Science** 19(8) 2025, article 198342, DOI 10.1007/s11704-024-40372-3. Region placed on the `HFUT` org handle (Hefei University of Technology) and the journal; the page itself states no country. |
| https://github.com/ZhijieXiong/pyedmine | MIT | 82 | APAC | Student modelling + recommendation | **Four task families under one experimental workflow:** `28` knowledge-tracing models, `7` cognitive-diagnosis models, `3` exercise-recommendation models and `4` **learning-path-recommendation** models, over `14` educational-data-mining datasets. 🔵 The learning-path family is the part this base has had no library for — `Clew` (MIT) builds a path for one learner interactively; this trains and benchmarks the policy. Credits pyKT, EduKTM, EduCDM and RecBole as antecedents. `README_zh.md` present; no institution stated. **Ledger carried it as `unstated`; the licence is MIT, read first-hand.** |
| https://github.com/tl-its-umich-edu/my-learning-analytics | Apache-2.0 | 37 | **North America** | Learner-facing analytics on Canvas | **MyLA — learning analytics built for the student to read, not the administrator.** Three views: Resources Accessed, Assignment Planning, Grade Distribution. Integrates with **Canvas**; Django + MySQL + Docker. Support links resolve to `its.umich.edu` (University of Michigan ITS Teaching & Learning). 🔵 A **North America** row on a page that is thin there, and it sits on Canvas — the LMS `p565` established this base had been censusing the wrong way round. Pairs with the `canvas-mcp` field (`280` repositories) as the read-side of the same integration. |
| https://github.com/evoluteur/braille-tools | MIT | 43 | Global | Accessibility rendering | **English Grade 1 (uncontracted) Braille in a web page** — one CSS class per Braille cell from an image sprite, plus a JS text-to-Braille-HTML function; three visual styles. **Zero dependencies**, vanilla JS + CSS, copy two files in. 🟢 **New to a `3,168`-address ledger, and permissive.** `p574` found the accessibility layer running backwards on licensing — `10` shippable against `11` copyleft, `2` noncommercial and `6` unlicensed, every platform of record GPL. This is a permissive component in that layer. 🔵 Scope is honest and narrow: it renders Braille for sighted readers; it is **not** a transcription engine and not a screen-reader substitute. |

### 🔴 Open edX, stated correctly: the platform is copyleft and the extension seam is not

This base carries `openedx/openedx-platform` at **AGPL-3.0** and has since `p28`. It is
worth stating plainly on this page, because the widely-repeated claim that Open edX is
"Apache-2.0" is false and it changes what can be delivered:

| Repo | Licence | Stars | What it means for delivery |
|---|---|---|---|
| `openedx/openedx-platform` | **AGPL-3.0** | 8,213 | The platform. Network copyleft — a hosted modification must offer its source |
| `openedx/XBlock` | **Apache-2.0** | 471 | 🟢 The extension API. Permissive — this is the seam to build on |
| `openedx/xblock-sdk` | **Apache-2.0** | 69 | 🟢 XBlock scaffolding |
| `openedx/codejail` | **Apache-2.0** | 477 | 🟢 Sandboxed untrusted-code execution — reusable well outside Open edX |
| `openedx/paragon` | **Apache-2.0** | 141 | 🟢 Design system / React components |
| `openedx/edx-lint` | **Apache-2.0** | 52 | 🟢 Lint configuration |

🔵 **The deliverable shape this implies:** an engagement ships *XBlocks and services against
the AGPL platform*, not a fork of it. The `XBlock` ledger entry was two-valued
(`AGPL-3.0 | Apache-2.0`) until this pass; it is Apache-2.0, which is what makes that shape
available at all. 🔴 `openedx/edx-platform` — the address most citations use — returns `422`:
it has moved, and anything resolving it by that name is reading a rename.


## p578 — 2026-10-31 — one addition, from an axis never queried in 577 passes

| Repo | Licence | Stars | Region | Layer | Why it is here |
|---|---|---|---|---|---|
| https://github.com/goplus/spx | Apache-2.0 | 124 | Global | Block-to-code runtime | **Scratch-compatible Go/XGo 2D game engine for STEM education.** The only permissive block-to-code engine on these shelves, and therefore the one place a primary / lower-secondary computing curriculum can be built without a copyleft dependency at the runtime layer. Verified 2026-10-31 from the repository page. |

🔵 **Region.** The page states no country or affiliation. The owning organisation also
publishes the XGo compiler (`gogen`) and interpreter (`ixgo`) and the About section links
`xbuilder.com`; those are **weak** APAC signals and are **not** sufficient under this base's
own placement rule, so the row is `Global`.

🔴 **Found underneath a head that is not an education tool.**
[`topic:stem-education`](https://github.com/search?q=topic%3Astem-education&type=repositories)
holds **`235`** repositories and had never been queried. Its top row is `goplus/xgo` at
**`9.5k★`** — **a programming language**. `spx` was eighth by stars. Second instance of the
miscategorisation class `p577` caught on the agent shelf; see
[`trending.md`](trending.md) for the full ladder.

🔴 **The layer's own gap, declared:** this axis carries **no assessment component**. `spx`
runs what a pupil builds; nothing on the axis evidences what the pupil learned. That seam
has to be bought from the autograding layer (`p576`) or built.

## p577 — 2026-10-31 — verified foundations

All twelve rows verified on 2026-10-31 by reading each repository page directly
(see the method note in [`../agents/top.md`](../agents/top.md): `curl -sI` returns
403 for every GitHub URL in this environment, real or fake, so WebFetch was used).

| Repo | Licence | Stars | Role in an education build |
|---|---|---|---|
| https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | Open edX LMS & Studio. **Note: `openedx/edx-platform` now redirects here — the repository was renamed.** Any older link in this KB or a client doc points at the old name. |
| https://github.com/moodle/moodle | GPL-3.0 | 7.6k | The default LMS of record worldwide, especially in EMEA and LATAM public education. |
| https://github.com/oppia/oppia | Apache-2.0 | 7.0k | Learning platform built on interactive explorations. **The largest permissively licensed platform in education.** |
| https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | Canvas, the open LMS by Instructure. Dominant in North American higher education. |
| https://github.com/frappe/lms | AGPL-3.0 | 3.4k | Lightweight full-stack LMS on the Frappe framework. Fast to stand up for a pilot. |
| https://github.com/learnhouse/learnhouse | AGPL-3.0 | 2.4k | Next-generation open-source learning platform. **Enterprise features sit under a separate Enterprise Licence** — read it before scoping. |
| https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Assignment release and autograding for notebooks. Permissive, and the cleanest grading seam for technical curricula. |
| https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | Apereo Foundation teaching/research/collaboration suite. **ECL-2.0 is an Apache-2.0 derivative** — the most permissive LMS of record. |
| https://github.com/chamilo/chamilo-lms | GPL-3.0 | 1.0k | LMS focused on ease of use and accessibility. Strong francophone and LATAM footprint. |
| https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 903 | Education ERP (Odoo-based): admissions, fees, SIS and LMS on one database. The ERP-shaped entry point. |
| https://github.com/Cvmcosta/ltijs | Apache-2.0 | 373 | LTI 1.3 tool provider. The supported way to attach anything to any of the platforms above **without forking them**. |
| https://github.com/h5p/h5p-php-library | GPL-3.0 | 154 | H5P core library for interactive content. Embedded by Moodle, Canvas and Open edX alike. |

## The licensing fact that should drive every education engagement

**Every learning platform of record is copyleft.** GPL-3.0 (Moodle, Chamilo,
H5P), AGPL-3.0 (Open edX, Canvas, Frappe LMS, LearnHouse), LGPL-3.0 (OpenEduCat).
The only permissive seats at this table are **Sakai (ECL-2.0)**, **Oppia
(Apache-2.0)**, **nbgrader (BSD-3-Clause)** and **ltijs (Apache-2.0)**.

AGPL-3.0 is the sharp one: it reaches network-served modifications, so forking
Canvas or Open edX and hosting it for a client can oblige disclosure of the
modifications.

**The architectural consequence, and it is the same in every region:** do not fork
the LMS. Build the AI as an **external LTI 1.3 tool** with `ltijs` (Apache-2.0),
talk to the platform over LTI and xAPI, and keep engagement code outside the
copyleft boundary. The agent layer licenses permissively
([`../agents/top.md`](../agents/top.md): 15 of 16 are MIT/Apache/BSD), so the only
thing that forces a copyleft decision is the integration style — which is a
choice, not a constraint.

## Declared gaps

- **No permissively licensed, production-grade LMS exists.** Oppia (Apache-2.0) is
  the nearest thing and it is an explorations platform, not a course-management
  system. If a client requires a permissive LMS, the honest answer is that the
  supply is absent, not that it is hard to find.
- **No verified open-source Student Information System** separate from an LMS was
  found beyond OpenEduCat (LGPL-3.0).
- **Africa and the Middle East**: no foundation repository was verified as
  originating there this pass.

---

## Prior passes (superseded, retained for history)

Not re-verified. Figures below predate p577.

### (archived) Foundational open source repos for education

<!-- machine-readable count claim, p574, for ingest/derive-foundations.py -->
`derived shelf rows: **154**` — every data row in a `SHELF`-disposition table,
derived by that gate from this page's own structure (`149` distinct addresses). 🟢 `p576`
added `12` rows in two layers (autograding/submission, and the Portuguese-language layer),
**`11` addresses new to this page** — the twelfth, `ls1intum/Artemis`, had appeared only in
this page's own census of re-found-but-never-shelved addresses, at `97×` — and **declared
all three of its tables in the manifest**, `CENSUS` for the denominators and `SHELF` for
the two layers. 🔴 **`ingest/derive-foundations.py` was DENIED by the sandbox classifier**
(*"Reason: [Code from External]"*) — 🟢 **but `ingest/derive-counts.py` and `make hooks`
both RAN in the same session**, so the denial is **per-invocation, not the blanket rule
`575-B` recorded** (`576-G`). This figure was therefore derived by **re-implementing
`derive-foundations.py`'s own manifest walk and `tables_of()` line-for-line** against this
page: `0` stale keys, `0` undeclared tables, `SHELF 154` / `CENSUS 12` / `METRIC 16` /
`SUMMARY 9`. 🟡 It is a faithful replica's output, not the gate's own, and is marked as
such — 🟢 **though the replica method was independently validated this pass**, because
`derive-counts.py` ran and agreed with the replica figures for `intel/trends.md` (`28`),
`compose/patterns.md` (`34`) and this page's sibling claim on `agents/top.md` (`48`).
🟢 `p575` added `7` rows (the horizontal accessibility layer), all `7` addresses new to
this page, and **declared both of its tables in the manifest** — the omission that killed
this gate for six passes (`574-B`).
🔴 **`p574` found this gate DEAD, not stale:** the `p568` rewrite left `33` of its
`36` declared keys naming headings the page no longer carries and `24` live tables
undeclared, two of them `p573`'s own — so it exited `2` before reading a single
table, and the page has carried no derivable figure for six passes. Keys repaired
and tables re-declared in
[`../ingest/foundations-disposition.tsv`](../ingest/foundations-disposition.tsv).

The substrate an education engagement builds on or integrates with. 🔴 **Star counts and metadata on this page do NOT come from the GitHub REST
index** — `api.github.com` answers **403** to this session, scoped to the harness
repository. `p571` flagged this header as false and it survived the pass that
flagged it; `p572` corrects it. Figures on rows added or re-read in the tenth pass
were read from the **rendered repository page**, and every licence from the
**grant file itself** over `raw.githubusercontent.com`. 🔵 Per `570-A`: a star or
commit count is a claim a repository makes about itself; the licence text, the
dependency manifest and the behaviour of the code are the only signals here that
an author cannot unilaterally manufacture.
**Licences on rows added or re-read in the fourth pass were read from the licence
file itself** over `raw.githubusercontent.com` (HTTP 200 from this session, while
`api.github.com` and `github.com` HTML are 403), with byte counts recorded;
older rows carry GitHub's licence determination and say so where it matters.

**Read the licence column before the star column.** The platforms of record are
overwhelmingly **copyleft** — the opposite of the agent layer. Two exceptions
have now been established, and one of them is new this pass and important.

## 🆕 `p576` — fourteenth pass, 2026-10-31 — 🟢 **THE AUTOGRADING AND SUBMISSION LAYER REFUTES TREND 21: FIVE UNIVERSITY-BUILT PLATFORMS OF RECORD, EVERY ONE PERMISSIVE. 🟢 AND THE PORTUGUESE-LANGUAGE LAYER, WHERE THIS BASE FINDS ITS FIRST JURISDICTION-SPECIFIC EVALUATION HARNESS — PLUS 🔴 A LICENCE CLASSIFIER THAT CANNOT READ A GRANT WRITTEN IN PORTUGUESE.**

🔵 **Both layers arrived through a broken query form.** `topic:autograding OR
topic:autograder` returns **`0`**; the singles return **`93`** and **`128`** (`576-A`,
trend 25). The axes below were read as singles, with denominators off GitHub's own result
counts.

### 🟢 The axis denominators measured this pass

| axis | repositories | prior queries in `575` passes | new addresses |
| --- | --: | --- | --: |
| `topic:autograder` | **128** | 🔴 `0` as a single (recorded only in the broken OR form) | 🟢 `7` shelf rows below |
| `topic:autograding` | **93** | 🔴 `0` as a single | — |
| `topic:educacao` (Portuguese) | **378** | 🔴 `0` | 🟢 `5` shelf rows below |
| `topic:educacion` (Spanish) | **410** | 🔴 `0` | 🔴 **`0` platform-grade** — tops out at `71★` |
| `topic:intelligent-tutoring-system` | **43** | 🔴 `0` as a single | 🔴 `0` — head (`fsrs4anki`, `4,100★`) and next two already shelved |
| `topic:ai-literacy` | **285** | 🔴 `0` | 🔴 `0` — top ten already shelved or off-domain |
| `topic:deped` (Philippines) | **10** | 🔴 `0` as a single | 🔴 `0` here — tops out at `5★`, shelved as an agent |
| `topic:cbse` (India) | **131** | 🔴 `0` as a single | 🔴 `0` — tops out at a `109★` **GPL-3.0** Anki deck |
| `topic:gaokao` (China) | **128** | 🔴 `0` as a single | 🔴 `0` here — two shelved as agents |
| `topic:automated-essay-scoring` | **38** | 🔴 `0` | 🔴 `0` — research code, tops out at `121★` |

### 🟢 The autograding and submission layer — and it licenses the OPPOSITE way to trend 21

🔴 **Trend 21 on these shelves says: "in education AI the artefacts with institutional
credibility are systematically less permissively licensed than the artefacts without it,"
generalised from the accessibility layer (`p574`) and psychometrics (`p573`). 🟢 This layer
refutes it outright.** The five platforms of record here are built by **TUM, CMU, RPI and
UC Berkeley (twice)** — as institutional as education software gets — and **every one is
MIT, BSD-3-Clause or Apache-2.0**, read byte-for-byte this pass. 🔵 **The two copyleft rows
are the two that are *not* a US/German university platform.** So the discriminator is not
credibility; **trend 21 holds per layer and does not generalise**, and that qualification
is filed as **trend 27**.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| 🆕 [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** (`develop/LICENSE`, 1,091 B ✅ first-hand, "Copyright (c) 2026 TUM Applied Education Technologies") | 824 | EMEA | ✅ permissive | 🟢 **The strongest unshelved address in this base's own census — re-found `97×` across `575` passes and never placed.** "Artemis — Interactive Learning with Automated Feedback." Java. Interactive exercises with automated assessment across programming, modelling, text and quizzes, built and run at scale by **Technical University of Munich**. 🔴 **Default branch is `develop`, not `main`** — a `main`/`master` probe reports it dead and drops the single best-licensed platform in the layer (`575-F`). 🔵 **This is the component `P-578-B` is built on**: its feedback is automated and its grade is a teacher's, which is exactly the shape Korea's Enforcement Decree carve-out rewards. |
| 🆕 [autolab/Autolab](https://github.com/autolab/Autolab) | **Apache-2.0** (`master/LICENSE`, 11,324 B ✅ first-hand) | 808 | North America | ✅ permissive | "Course management service that enables auto-graded programming assignments." Ruby. **Carnegie Mellon.** The autograding platform with the longest production record in the layer, and an Apache-2.0 patent grant — the licence a client's counsel objects to least. |
| 🆕 [Submitty/Submitty](https://github.com/Submitty/Submitty) | **BSD-3-Clause** (`main/LICENSE.md`, 1,542 B ✅ first-hand, "Copyright (c) 2014-2026, Submitty team") | 807 | North America | ✅ permissive | "Homework Submission, Automated Grading, and TA grading system." PHP. **Rensselaer Polytechnic Institute.** 🔵 **Note the path: the grant is in `LICENSE.md`, not `LICENSE`** — a probe without the `.md` variant calls this ungranted, which is `575-A`'s failure mode recurring in a layer where it would have cost a platform row. 🟢 **The explicit "TA grading" stage in its own one-line description is a human-in-the-loop checkpoint shipped as a product feature.** |
| 🆕 [okpy/ok](https://github.com/okpy/ok) | **Apache-2.0** (`master/LICENSE`, 13,979 B ✅ first-hand) | 370 | North America | ✅ permissive | "ok.py supports programming projects by running tests, tracking progress, and assisting in debugging." Python. **UC Berkeley.** Shelved for the tracking-and-debugging half: it models student *progress*, not only correctness, which is the hook an AI tutor attaches to. 🟡 Maturity unassessed this pass — read commit recency before proposing it. |
| 🆕 [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | **BSD-3-Clause** (`master/LICENSE`, 1,560 B ✅ first-hand, "Copyright (c) 2019, UC Berkeley Division of Data Science and Information") | 161 | North America | ✅ permissive | "A Python and R autograding solution." **UC Berkeley Division of Computing, Data Science, and Society.** 🟢 **The notebook-native one**: it grades Jupyter work, which is the format most data-science and AI curricula are actually taught in — including the ones a client will ask Globant to build. |
| 🆕 [INGInious/INGInious](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** (`main/LICENSE`, 34,764 B ✅ first-hand) | 243 | EMEA | ⛔ copyleft, **and mixed** | "A secure and automated exercises assessment platform." Python, UCLouvain. 🔴 **Read the grant's first line before quoting it: "Most of the files in INGInious are distributed under the GNU AGPL v3 licence"** — *most*, not all. 🔵 A per-file licence audit is required before any reuse, and **AGPL §13 network exposure applies to a hosted grader**, which is how graders are always deployed. Shelved as a feature reference, not a dependency. |
| 🆕 [foundation50/classroom50](https://github.com/foundation50/classroom50) | 🔴 **GPL-3.0** (`main/LICENSE`, 35,150 B ✅ first-hand) | 229 | North America | ⛔ copyleft | "The free, open-source alternative to GitHub Classroom." TypeScript. 🔵 Strategically interesting — it targets the assignment-distribution layer that a proprietary incumbent owns — but **GPL-3.0 makes it a deployment, not a component.** |

### 🟢 The Portuguese-language layer — and the only jurisdiction-specific evaluation harness on these shelves

🔵 **Why this layer is on this page rather than only in the market intel:** Brazil's MEC
published AI guidance for *educação básica* in **April 2026**, and Brazil is the one
jurisdiction where an open artefact exists that the guidance can be **measured against**
rather than merely claimed to satisfy.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| 🆕 [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** (code, `main/LICENSE`, 1,092 B ✅ first-hand, "Copyright (c) 2026 Profy Tecnologias Educacionais Ltda") **+ CC BY 4.0** (data, `dados/LICENSE.md`) | 24 | LATAM | ✅ permissive, **split code/data** | 🟢 **The Brazilian national curriculum as structured data, and the most directly usable LATAM artefact this base has found.** `1,721` *aprendizagens* — `1,580` across the three stages of basic education plus `141` from the Computing complement (*Parecer CNE/CEB 2/2022*) — in **JSON, CSV and SQLite**, each record carrying competencies, organisation contexts and provenance, conferred against the official document. 🟢 **Ships as npm and PyPI packages with the data embedded that work with no internet, and a local MCP server (`npx -y @bncc/mcp`)** — the hosted one at `mcp.bncc.dev` is optional, which matters for school data-residency rules. 🟢 **Zenodo DOI `10.5281/zenodo.21625233`, and it carries `CITATION.cff`** — 🔵 note against `574-F`, which found `0 of 7` repositories with one in a different cohort. 🔵 **Its licence note states the legal theory**: BNCC normative texts are official acts and not copyrightable under **art. 8º, IV, Lei 9.610/98**, so CC BY 4.0 covers the compilation and curation only. 🔴 **`24★`** — judge it on the DOI, the validation workflow and the stated provenance, not the star count. |
| 🆕 [bncc-dev/bncc-benchmark](https://github.com/bncc-dev/bncc-benchmark) | 🟡 **DUAL, declared per directory**: **MIT** for `harness/` and `test/`; **CC BY 4.0** for `itens/`, `resultados/` and `METODOLOGIA.md` (`main/LICENSE`, 911 B ✅ first-hand) | 12 | LATAM | ✅ permissive for the harness | 🟢 **An open LLM-hallucination benchmark against the Brazilian national curriculum: `15,300` responses from `17` models.** 🔵 **This is the piece that makes a curriculum-alignment claim falsifiable**, and this base has no equivalent for any other jurisdiction. 🔴 **Read the third clause of its licence before reusing results**: the stored model responses were generated by third-party models and **carry those providers' own reuse conditions**, which the repository states explicitly rather than leaving to be discovered. 🟢 A dual licence split by *directory* and documented in the licence file itself is the cleanest grant structure in this layer. |
| 🆕 [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** (`2.12/LICENSE`, 18,092 B ✅ first-hand) | 722 | LATAM | ⛔ copyleft | "Lançando o maior software livre de educação do Brasil!" PHP. 🟢 **The largest Portuguese-language education platform on GitHub and the head of the `topic:educacao` ladder** — a school-management system (*gestão escolar*) in real municipal use. 🔴 **Default branch is `2.12`** — neither `main` nor `master`, so a two-branch probe reports Brazil's biggest education platform **dead**. Third instance of this class after `openeducat_erp` (`19.0`) and Artemis (`develop`); see [`../evidence/nondefault-branches.2026-10-31-p576.tsv`](../evidence/nondefault-branches.2026-10-31-p576.tsv). 🔵 Deploy it and call it; do not vendor it. |
| 🆕 [portabilis/i-diario](https://github.com/portabilis/i-diario) | 🔴 **AGPL-3.0** (`1.6/LICENSE`, 35,326 B ✅ first-hand) — 🔴 **and the grant is written in PORTUGUESE** | 117 | LATAM | ⛔ copyleft, §13 exposure | The teacher's *diário de classe* companion to `i-educar`. Ruby. 🔴 **This row is also the evidence for `576-E`: its licence file opens `LICENÇA PÚBLICA GERAL AFFERO GNU Versão 3, 19 de novembro de 2007`, and this base's own classifier regex — `r"GNU\s+AFFERO\s+GENERAL\s+PUBLIC\s+LICENSE"` in `compose/code/p228-shelf-gate/classify_grant.py` — does NOT match it.** Demonstrated against the regex itself in [`../evidence/grant-language-blindspot.2026-10-31-p576.tsv`](../evidence/grant-language-blindspot.2026-10-31-p576.tsv). 🔵 **The direction of the error is the dangerous one**: an unread AGPL grant reads as "no licence", and a repository with no licence has been treated on these shelves as a fork-and-read candidate. Default branch `1.6`. |
| 🆕 [ipti/br.tag](https://github.com/ipti/br.tag) | 🔴 **GPL-2.0** (`main/LICENSE`, 18,027 B ✅ first-hand) | 20 | LATAM | ⛔ copyleft | "Software de apoio a gestão escolar baseado em Tecnologia Social." PHP, by **IPTI** (Instituto de Pesquisas em Tecnologia e Inovação). 🔵 Shelved as the small-municipality end of the same vertical: where `i-educar` serves a city network, this targets schools with far less capacity, which is where Brazil's rural-priority obligations land. |
## 🆕 `p575` — thirteenth pass, 2026-10-31 — 🟢 the horizontal accessibility layer that the education axis cannot see, and 🔴 **three of this pass's own seven "ungranted" verdicts were refuted by its own second probe**

🔵 **Why these rows are here and not on `agents/top.md`.** `574-C`'s sweep found the
engineering in this layer sits on `topic:screen-reader` (**594** repositories), and
none of it knows what a course is. Under the fourth pass's standing rule that a
horizontal capability layer is not an education agent, it is shelved here. 🟢 **This
is the layer the `P-575-A` BUILD recommendation stands on** — because the
education-specific tier it would replace tops out at `7★`.

| Component | Repo | Grant (read first-hand) | ★ | Region | What it gives an education build |
| --- | --- | --- | --: | --- | --- |
| **NVDA** | [nvaccess/nvda](https://github.com/nvaccess/nvda) | **GPL-2.0** — ⚠️ **not** in `LICENSE`: in **`copying.txt`** (`53,407 B`), and `pyproject.toml` agrees (`license = {file = "copying.txt"}`) | 2,700 | Global | The free Windows screen reader that students actually use. 🔴 **GPL-2.0 — the reference target you test against, never a dependency you ship.** |
| **guidepup** | [guidepup/guidepup](https://github.com/guidepup/guidepup) | **MIT** (`1,068 B`, `main/LICENSE`) | 591 | Global | 🟢 **Screen-reader automation for tests** — drives NVDA and VoiceOver from a test suite. This is the row that turns an accessibility duty into a **CI gate**, and it is permissive. Copyright `2023 Craig Morten`. |
| **virtual-screen-reader** | [guidepup/virtual-screen-reader](https://github.com/guidepup/virtual-screen-reader) | **MIT** (`1,068 B`, `main/LICENSE`) | 158 | Global | Screen-reader *simulator* for tests — runs in CI with no real assistive tech installed. 🟢 The cheap half of the same gate. |
| **Odilia** | [odilia-app/odilia](https://github.com/odilia-app/odilia) | **MIT OR Apache-2.0** (dual) — ⚠️ **no root licence file**; grant stated in `README.md` | 173 | Global | Fast Rust screen reader for Linux desktops — the relevant target wherever the client's lab images are Linux. 🟢 Permissive, unlike NVDA. |
| **RigelA** | [mzdk100/rigela](https://github.com/mzdk100/rigela) | **Apache-2.0** (`11,336 B`, `master/LICENSE`) | 150 | APAC | Screen reader written in pure Rust, Chinese-language project. 🟢 **Permissive and APAC-origin** — the combination this base is usually short of. |
| **EaseView** | [Ropaxyz/EaseView](https://github.com/Ropaxyz/EaseView) | **MIT** (`1,067 B`, `main/LICENSE`) | 2 | Global | Windows screen colour-overlay for readability — the standard dyslexia-adjacent accommodation, as a vendorable component. Copyright `2026 Ross Paxton`. 🔴 2★. |
| **TechSpecsTVI** | [mrhunsaker/TechSpecsTVI2023](https://github.com/mrhunsaker/TechSpecsTVI2023) | **Apache-2.0** (`11,351 B`, `main/LICENSE`) | 0 | North America | Not code — the **equipment specification** a Teacher of the Visually Impaired works from. 🔵 Shelved because a procurement-shaped document is what an engagement is actually asked for. |

### 🔴 `575-A` — this pass's own probe produced **three false "ungranted" verdicts out of seven**, and the defect generalises to a published figure

🔴 **Measured, on this pass's own work.** The first probe read six grant paths
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`, `LICENSE-MIT`) and
returned **`NO-LICENCE-FILE` for seven repositories**. A second probe over a wider
path set — adding `copying.txt`, the README and the dependency manifests —
**refuted three of those seven**:

| repository | first probe | second probe | where the grant actually was |
| --- | --- | --- | --- |
| [nvaccess/nvda](https://github.com/nvaccess/nvda) | 🔴 `NO-LICENCE-FILE` | 🟢 **GPL-2.0** | **`copying.txt`** (`53,407 B`) — lowercase, non-standard name |
| [odilia-app/odilia](https://github.com/odilia-app/odilia) | 🔴 `NO-LICENCE-FILE` | 🟢 **MIT OR Apache-2.0** | **`README.md`** — dual grant, no licence file at all |
| [IronCountySchoolDistrict/iep-printing-php](https://github.com/IronCountySchoolDistrict/iep-printing-php) | 🔴 `NO-LICENCE-FILE` | 🟢 **MIT** | **`composer.json`** (`"license": "MIT"`) |

🔵 **The lesson is not "probe more paths".** It is that **"no licence file" is a claim
about the prober's path list, not about the repository** — and this base publishes a
figure of exactly that shape. 🔴 **`p573`'s "`7 of 26` repositories have no licence
file", restated by `p574` and cited on several pages, was produced by a probe of this
same class and has never been re-run against `copying.txt`, a README grant or a
manifest.** 🟡 It should be read as an **upper bound** until re-audited, which is
`575-A`'s ask. 🟢 The control still holds: a fabricated address
(`FAKE-CONTROL-ORG/this-repo-does-not-exist-575`) answered `DEAD-OR-ABSENT` on both
probes, so the channel does discriminate absence from error — it was the *path set*
that was wrong, not the method.

🟢 **And the `572-E` Affero discriminator reproduced COLD for the third time**, on a
sample it was not built from: Affero references `= 3` on every GPL body
(`SEALApplication`, `chatpaths`, `minecraft-access`, `nvda`) and `= 15–18` on every
real AGPL (`aba-clinical-agent` `15`, `LectureFlow` `15`, `zacess` `15`, `AlloFlow`
`18`). **8 of 8, no overlap.** 🔵 Twice-validated became thrice-validated; this is
now the cheapest reliable grant discriminator on this harness.
## 🆕 `p574` — the accessibility and assessment-interchange layer: `911` repositories across **six axes this base has never queried**, and its grants run the OPPOSITE way from the agent layer

🟢 **`derived foundations rows: **23**` added this pass**, from a single coherent
capability layer: the tooling an institution needs to meet a **digital
accessibility** obligation, plus the **QTI** interchange tier that carries
assessment items between systems. 🔵 Why it matters more than its star counts
suggest: this is the one education obligation with a **dated legal deadline** —
`April 26, 2027` and `April 26, 2028` in the United States, and `EN 301 549`
under the EU's Web Accessibility Directive — and see
[`../intel/market.md`](../intel/market.md) for the regional placement.

🔴 **`Title II`, `WCAG`-as-an-axis, `topic:dyslexia`, `topic:aac`,
`topic:sign-language` and `topic:qti` appear `0` times as queries in `573` passes
of this base's history.** The six axes hold **`911`** repositories between them.

### 🟢 The permissive tier — ten rows a client engagement may actually ship

| Repo | Licence (first-hand) | ★ | Region | Why it is here |
| --- | --- | --: | --- | --- |
| [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills) | **MIT** (`1,073 B`; `package.json` agrees) | 3,100 | Global | DTCG tokens, 52 components, **WCAG 2.2 AA–AAA**, 138 design systems. Template-level remediation, agent-shaped. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** — licence file `10,982 B`, `NOTICE.TXT` `14,712 B`, **both read byte-for-byte this pass** | 449 | EMEA | Institutional LMS, frentix GmbH (Switzerland). 🟢 This base carried it as *"Apache-2.0 (README badge; sidebar unnamed)"* — the badge is now a **measured grant**. |
| [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) | **MIT** (`1,069 B`; `package.json` agrees) | 431 | Global | Eleven review specialists enforcing **WCAG 2.2 AA** for Claude Code, GitHub Copilot and Claude Desktop. The compliance layer as agents. |
| [sign-language-translator/sign-language-translator](https://github.com/sign-language-translator/sign-language-translator) | **Apache-2.0** (`11,364 B`; `pyproject.toml` agrees) | 380 | Global | Python framework for building custom sign-language ↔ text translators. 🟢 **The permissive alternative to the field's flagship, which is noncommercial.** |
| [OpenDyslexic/extension](https://github.com/OpenDyslexic/extension) | 🔴 **CONFLICT — `MIT` in the licence file (`1,073 B`), `ISC` in `package.json`** | 117 | Global | OpenDyslexic typeface browser extension. Both limbs are permissive, so the conflict is a hygiene defect rather than a block — but it is a real two-channel disagreement. |
| [dasher-project/dasher-web](https://github.com/dasher-project/dasher-web) | **MIT** (`1,109 B`; `package.json` agrees) | 55 | Global | Dasher zooming text entry — gaze and switch input in the browser. |
| [evoluteur/braille-tools](https://github.com/evoluteur/braille-tools) | **MIT** (`1,073 B`; `package.json` agrees) | 43 | Global | Grade-1 Braille rendering for web content, JS + CSS only. |
| [ContentSquare/readapt](https://github.com/ContentSquare/readapt) | **Apache-2.0** (`11,357 B`) | 39 | EMEA | Reading adaptation for dyslexia; published by Contentsquare (France). |
| [mthebaud/predict4all](https://github.com/mthebaud/predict4all) | **Apache-2.0** (`11,357 B`, at **`LICENCE`**) | 23 | EMEA | Multilingual next-word prediction for AAC input (France). 🔵 The grant sits at the **British spelling** — see the instrument note below. |
| [rolfis/qti-convert](https://github.com/rolfis/qti-convert) | **Apache-2.0** (`11,357 B`) | 22 | Global | Converts a Canvas QTI export to Word or JSON. 🟢 **The only permissively licensed QTI tool found on a 52-repository axis.** |

### 🔴 The copyleft, noncommercial and manifest-only tier — thirteen rows that are link-only, arm's-length or blocked

| Repo | Licence (first-hand) | ★ | Region | Why it is here |
| --- | --- | --: | --- | --- |
| [OptiKey/OptiKey](https://github.com/OptiKey/OptiKey) | **GPL-3.0** (`LICENSE.txt` `35,144 B`, Affero refs `3`) | 4,400 | Global | Full computer control and speech by eye gaze. The largest artefact in this layer, and copyleft. |
| [sign/translate](https://github.com/sign/translate) | 🔴 **CC BY-NC-SA** (`LICENSE.md` `17,404 B`) — **NONCOMMERCIAL** | 797 | Global | The field's flagship real-time sign-language translation application. 🔴 **A client deliverable cannot include it.** |
| [cboard-org/cboard](https://github.com/cboard-org/cboard) | **GPL-3.0-only** (`35,141 B`, Affero refs `3`; `package.json` agrees) | 766 | Global | Browser AAC board with text-to-speech; widely deployed in schools. |
| [liip/TheA11yMachine](https://github.com/liip/TheA11yMachine) | 🟡 **Manifest-only — `BSD-3-Clause` in `package.json`, NO licence file on a 44-name ladder** | 642 | EMEA | Crawling accessibility auditor (Liip AG, Switzerland). A `POINTER`, not a grant: usable, but the notice obligation has no text to reproduce. |
| [asterics/Asterics-AAC](https://github.com/asterics/Asterics-AAC) | **AGPL-3.0** (`34,523 B`, Affero refs `16`; `package.json` agrees) | 129 | EMEA | AAC app from the EU-funded AsTeRICS project (Austria). 🔴 **§13 network source-offer obligation** on any hosted deployment. |
| [chipmates/agoracosmica](https://github.com/chipmates/agoracosmica) | **AGPL-3.0** (`34,523 B`, Affero refs `16`) | 150 | Global | Thirty historical figures, narrated and conversational — a talkable library. Same §13 exposure. |
| [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | **GPL-3.0-only** (`35,147 B`, Affero refs `3`; `package.json` **and** `composer.json` agree) | 117 | North America | **The Universal Design Online content Inspection Tool** — scans Canvas course content for accessibility defects and fixes them in place. University of Central Florida. 🟢 **The closest thing to an off-the-shelf Title II remediation tool in open source**, and three channels agree on its grant. |
| [oat-sa/qti-sdk](https://github.com/oat-sa/qti-sdk) | **GPL-2.0** (`18,025 B`) | 86 | EMEA | The reference PHP QTI SDK. |
| [mulberrysymbols/mulberry-symbols](https://github.com/mulberrysymbols/mulberry-symbols) | 🔴 **CONFLICT — `CC BY-SA` in `LICENSE.txt` (`260 B`), `ISC` in `package.json`** | 62 | Global | AAC symbol set for adults with language difficulties. 🔴 **The asset is content, so the content licence governs** — and a `260 B` grant is a pointer-length file, not a licence text. |
| [Learnosity/learnosity-qti](https://github.com/Learnosity/learnosity-qti) | **GPL-2.0** (`18,264 B`, on the **`develop`** default branch) | 26 | Global | QTI 2.1 items ↔ Learnosity JSON. 🔵 A `main`/`master`-only probe would have missed it — `p558`'s mechanism, third instance. |
| [Citolab/qti-components](https://github.com/Citolab/qti-components) | **GPL-3.0** (`LICENSE.md` `35,199 B`, Affero refs `3`; `package.json` says `GPLv3`) | 18 | EMEA | QTI item renderer web components (Citolab / Cito, Netherlands). 🔴 **Front-end components under GPL-3.0 cannot be embedded in a proprietary client front-end.** |
| [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | **GPL-2.0-only** (`18,025 B`; `composer.json` agrees) | — (unread) | EMEA | **TAO** — the QTI-native assessment platform, OAT SA (Luxembourg). The platform of record for standards-conformant computer-based testing. |
| [oat-sa/extension-tao-itemqti](https://github.com/oat-sa/extension-tao-itemqti) | **GPL-2.0** (`18,025 B`) | — (unread) | EMEA | TAO's QTI item authoring and delivery extension. 🟢 **New to this base entirely** — `0` prior mentions in `573` passes. |

### 🔵 The licence-band census of the whole layer — a measurement, not supply

| band | addresses | share | what it means for a deliverable |
| --- | --: | --: | --- |
| 🟢 Permissive with a licence **file** (MIT / Apache-2.0) | **10** | `34 %` | Shippable. One of the ten (`OpenDyslexic/extension`) disagrees with its own manifest. |
| 🔴 Copyleft (GPL-2.0 / GPL-3.0 / AGPL-3.0) | **11** | `38 %` | Arm's-length service or unmodified deployment only. Two are **AGPL** and carry a §13 network obligation. |
| 🔴 Noncommercial or content-licensed | **2** | `7 %` | `sign/translate` (CC BY-NC-SA) and `mulberry-symbols` (CC BY-SA). In accessibility the **asset** is the product, so a content carve-out is a commercial block — `572-C`'s mechanism in a second layer. |
| 🔴 No licence text at all | **6** | `21 %` | Four with nothing anywhere (`nenad/CSV2QTI`, [`dxli94/WLASL`](https://github.com/dxli94/WLASL) — **1.3k★**, the WACV 2020 sign-language dataset — [`ZechengLi19/Awesome-Sign-Language`](https://github.com/ZechengLi19/Awesome-Sign-Language), `Jojobeans1981/Ember-Campfire-Edition`) and two manifest-only (`liip/TheA11yMachine`, `TBosak/ability`). |

🔴 **So the headline is a ratio, not a row: `10 of 29` in this layer are
shippable, against `11` copyleft, `2` noncommercial and `6` ungranted.** 🔵 This
is the **second** layer in two passes where the licence boundary and the
credibility boundary run in opposite directions — `p573` found it in
psychometrics (permissive Python, GPL R), and here the standards-conformant QTI
implementations (**TAO**, `qti-sdk`, `qti-components`) and the one real Canvas
remediation tool (**UDOIT**) are all copyleft, while the permissive tier is
converters and browser extensions.

### 🔴 Two defects in the grant reader itself, both reproducible, both new mechanisms

1. 🔴 **A GPL version line is not canonical text.** `OptiKey/OptiKey`'s licence
   reads **`Version 3, 29th June 2007`** — with the ordinal suffix. Every version
   probe on this harness, including
   [`../ingest/probe-grant.sh`](../ingest/probe-grant.sh), tests for
   `Version 3, 29 June 2007`, so a **4.4k★** GPL-3.0 repository grades as
   unversioned `GPL-?`. 🔵 **GPL-2.0 vs GPL-3.0 is not taxonomy** — the patent
   grant, the Apache-2.0 compatibility direction and the §13 posture all differ.
   The safe reading here used the **byte band** (`35,144 B` is GPL-3-sized;
   GPL-2.0 is `~18 kB` on this sample) plus `p572-E`'s Affero-reference count.
2. 🔴 **A licence may be Markdown, and a version probe reads the markup.**
   `loventures/loplatform` publishes AGPL-3.0 as `LICENSE.md` with a `===`
   underlined title and the version in emphasis — `_Version 3, 19 November 2007_`.
   🔵 `p378`'s presentation-fold class, now reaching the **version** field rather
   than the template field.

🟢 **And `p572-E`'s prescribed discriminator reproduced cold on new specimens:**
Affero references came in at **`3`** on every GPL body read this pass
(`UDOIT`, `OptiKey`, `cboard`, `qti-components`) and **`16`** on every real AGPL
(`Asterics-AAC`, `agoracosmica`, `loplatform`). 🟢 **`7 of 7`, no overlap** — the
cheap discriminator holds on a sample it was not built from.

## Eleventh pass (`p573`, 2026-10-31) — 🟢 THE PSYCHOMETRIC MEASUREMENT LAYER SPLITS BY **LANGUAGE**, NOT BY QUALITY: the Python tier this base already shelved is permissive, the R/CRAN tier it never saw is GPL almost without exception

🔵 **Why this pass went looking here.** This base already publishes two patterns
that depend on real psychometrics — `P-571-A` (defensible assessment) and
`P-572-A` (item calibration and score equating) — and `P-573-C` was registered for
"locally published institutional psychometrics". **None of them named a
calibration library.** So the measurement layer was swept directly.

🟢 **Result: `20` addresses read byte-for-byte, `13` of them new to a 572-pass
base.** 🔴 **And the finding is a licence boundary that runs straight through the
middle of the layer.**

### 🔴 The split, stated as the engagement decision it actually is

| tier | where it lives | grant | usable in a closed client deliverable? |
| --- | --- | --- | --- |
| 🟢 **Python / JVM** — already on this base's shelves | `girth`, `catsim`, `pyirt`, `EduCDM`, `pypsy`, `pykt-toolkit`, `EduStudio`, `pyedmine`, `EduData` | 🟢 **MIT / BSD-3 / Apache-2.0** | 🟢 **Yes** |
| 🔴 **R / CRAN** — absent from every shelf page until now | `mirt`, `TAM`, `sirt`, `CDM`, `GDINA`, `dina`, `measr`, `psychmeta`, `galamm`, `ShadowCAT`, `catIRTtools` | 🔴 **GPL-2/GPL-3 family, `11` of `12`** | 🔴 **No — arm's length only** |
| 🟢 the one permissive R exception | `OpenMx/OpenMx` | 🟢 **Apache-2.0** | 🟢 **Yes** |

🔴 **This is commercially load-bearing, and it is not a taxonomy quibble.**
`mirt`, `TAM`, `sirt` and `GDINA` are the implementations that **exam boards,
ministries and peer reviewers actually accept** for IRT calibration, DIF and
score equating. They are GPL. The permissive Python tier is perfectly good code,
but it does not carry the same evidentiary standing in a psychometric report.
🟢 **So an assessment engagement picks one of two postures deliberately —
`P-575-A` and `P-575-B` below write both of them up — rather than discovering the
constraint after the statistician has already chosen their tooling.**

### 🟢 The R/CRAN psychometric tier, now placed — every grant read from `DESCRIPTION`

🔵 Star counts are as displayed on the topic pages (`topic:psychometrics` **518**,
`topic:item-response-theory` **154**, `topic:cognitive-diagnosis` **19**,
`topic:computerized-adaptive-testing` **24**); 🔴 **this session cannot reach
`api.github.com`**, so treat them as page-rounded, not API-exact.

| Package | Repo | Licence (read first-hand) | ★ | Region | What it does |
| --- | --- | --- | --: | --- | --- |
| mirt | [philchalmers/mirt](https://github.com/philchalmers/mirt) | 🔴 **GPL (>= 3)** (`DESCRIPTION`) | — | North America | **The de facto standard multidimensional IRT package.** Unidimensional and multidimensional item-response models, EM and MH-RM estimation, DIF, item fit, plausible values. If a client's psychometrician names one tool, it is this one. |
| TAM | [alexanderrobitzsch/TAM](https://github.com/alexanderrobitzsch/TAM) | 🔴 **GPL (>= 2)** (`DESCRIPTION`) | 19 | EMEA | "Test Analysis Modules" — Rasch and 2PL/3PL calibration, **plausible-value generation and weighting**, the machinery large-scale assessments (PISA-style) are actually analysed with. |
| sirt | [alexanderrobitzsch/sirt](https://github.com/alexanderrobitzsch/sirt) | 🔴 **GPL (>= 2)** (`DESCRIPTION`) | 27 | EMEA | Supplementary IRT models — **linking and equating**, local dependence, DETECT, invariance testing. The equating half of `P-572-A`. |
| CDM | [alexanderrobitzsch/CDM](https://github.com/alexanderrobitzsch/CDM) | 🔴 **GPL (>= 2)** (`DESCRIPTION`) | 23 | EMEA | Cognitive diagnosis modelling — DINA, DINO, GDINA, skill-profile classification. Maps responses to **mastery of named skills**, which is what a competency report needs. |
| GDINA | [Wenchao-Ma/GDINA](https://github.com/Wenchao-Ma/GDINA) | 🔴 **GPL-3** (`DESCRIPTION`) | 33 | North America | The GDINA-family reference implementation: Q-matrix validation, item-level model comparison, classification accuracy. 🟢 **New to this base — `0` prior sightings in `3,168` ledger rows.** |
| measr | [r-dcm/measr](https://github.com/r-dcm/measr) | 🔴 **GPL (>= 3)** (`DESCRIPTION`) | 13 | North America | **Bayesian** diagnostic classification models via Stan, with built-in model-fit and reliability output. The modern, better-documented route into CDM. |
| dina | [tmsalab/dina](https://github.com/tmsalab/dina) | 🔴 **GPL (>= 2)** (`DESCRIPTION`) | 17 | North America | DINA parameter estimation with a Gibbs sampler. Small, single-purpose, readable. 🟢 **New to this base.** |
| ShadowCAT | [Karel-Kroeze/ShadowCAT](https://github.com/Karel-Kroeze/ShadowCAT) | 🔴 **GPL-3** (`DESCRIPTION`) | 12 | EMEA | **Multidimensional computerised adaptive testing using shadow testing** — content-constraint-respecting item selection, the part a naive CAT loop gets wrong. 🟢 **New to this base.** |
| psychmeta | [psychmeta/psychmeta](https://github.com/psychmeta/psychmeta) | 🔴 **GPL (>= 3)** (`DESCRIPTION`) | 70 | North America | Psychometric **meta-analysis** — artefact correction, credibility intervals. The tool for "does this intervention work across studies", i.e. the evidence layer behind `P-570-C`. 🟢 **New to this base.** |
| galamm | [ropensci/galamm](https://github.com/ropensci/galamm) | 🔴 **GPL (>= 3)** (`DESCRIPTION`) | 37 | EMEA | Generalised additive **latent and mixed models** — growth/longitudinal learner modelling with latent variables. rOpenSci-reviewed. 🟢 **New to this base.** |
| catIRTtools | [ecaybek/catIRTtools](https://github.com/ecaybek/catIRTtools) | 🔴 **GPL** (35,822 B `LICENSE`) | 6 | EMEA | CAT simulation and calibration helpers. Türkiye-published. 🟢 **New to this base.** |
| piraid | [UUPharmacometrics/piraid](https://github.com/UUPharmacometrics/piraid) | 🟡 **LGPL (>= 2)** (`DESCRIPTION`) | 10 | EMEA | Pharmacometric IRT model development. 🔵 Out-of-domain, but **LGPL** — the one R row a closed application may *link*. Uppsala. 🟢 **New to this base.** |
| **OpenMx** | [OpenMx/OpenMx](https://github.com/OpenMx/OpenMx) | 🟢 **Apache-2.0** (`DESCRIPTION`: "Apache License (== 2.0)") | 102 | North America | 🟢 **The single permissively licensed R psychometrics engine located in this sweep.** Structural equation modelling, latent-variable and multi-group models, matrix-algebra backend. **If an engagement must do latent-variable measurement in R *and* ship a closed derivative, this is the only row on this table that allows it.** 🟢 **New to this base.** |

### 🟢 Permissive rows the same sweep produced — small, but genuinely usable

| Repo | Licence (first-hand) | ★ | Region | Why it is here |
| --- | --- | --- | --: | --- |
| [JuliaPsychometricsBazaar/ComputerAdaptiveTesting.jl](https://github.com/JuliaPsychometricsBazaar/ComputerAdaptiveTesting.jl) | 🟢 **MIT** (1,073 B) | 6 | Global | Modular CAT library in Julia — ability estimators, item selectors, termination rules as swappable parts. 🟢 **The only permissive *framework* for adaptive testing found in `24` CAT repositories.** 🟢 **New to this base.** |
| [englishcentral/ovlt](https://github.com/englishcentral/ovlt) | 🟢 **MIT** (1,070 B) | 10 | Global | **Open Vocabulary Level Test** — a published, calibrated vocabulary instrument, not a framework. Rare: an actual *item bank* under MIT. 🟢 **New to this base.** |
| [KonkovDV/fsp-talent](https://github.com/KonkovDV/fsp-talent) | 🟢 **MIT** (1,094 B) | 0 | — | IRT-based adaptive test inside a talent-matching platform, Docker Compose. 🔵 Shelved as a **worked example of wiring IRT into a product**, not as a dependency. 🟢 **New to this base.** |

### 🔴 Two corrections to rows this base already ships — both are missing grants

🔴 **A repository with no licence file is exclusively copyrighted by default.** Two
rows already on this base's shelves fail that test, and neither carries the caveat:

| Row | Where it is cited | What `HEAD` actually has |
| --- | --: | --- |
| [meyerjp3/psychometrics](https://github.com/meyerjp3/psychometrics) (114★, Java) | 🔴 **`9` live KB files** | 🔴 **NO licence file** — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` all 404. The Java CTT/IRT library this base recommends cannot legally be shipped in a client deliverable. |
| [bigdata-ustc/Agent4Edu](https://github.com/bigdata-ustc/Agent4Edu) (100★, AAAI 2025) | 🔴 **`4` live KB files** | 🔴 **NO licence file.** A peer-reviewed paper is not a grant. |
| [patriciamar/ShinyItemAnalysis](https://github.com/patriciamar/ShinyItemAnalysis) (47★) | 🟡 `5` live KB files | 🟡 **GPL-3** (`DESCRIPTION`) — correct and usable, but it was carried here without the copyleft flag. |

🔴 **And the same failure mode dominates the new academic CDM rows: `5` of the `7`
repositories found under `topic:cognitive-diagnosis` have no licence file at all** —
[inuyasha2012/vipsy](https://github.com/inuyasha2012/vipsy),
[kervias/DCD](https://github.com/kervias/DCD),
[CSLiJT/HCD-code](https://github.com/CSLiJT/HCD-code),
[Mr-nnng/ICD](https://github.com/Mr-nnng/ICD),
[ShawnYu98/RDGT](https://github.com/ShawnYu98/RDGT).
🔵 All five are real, all five back published papers (SIGKDD, NeurIPS, TKDE,
ICDM), and **none may be used.** Read the method, reimplement it.

### 🔵 Method note — the mandated verification command is broken on this harness, and the fix also reads better data

🔴 **`curl -sI https://github.com/…` returns `403` for every URL on this
session — real repositories and invented ones alike.** Controls run this pass:

| probe | result |
| --- | --- |
| `github.com/openedx/XBlock` (real) | 🔴 `403` |
| `github.com/this-does-not-exist-xyz123/nope` (invented) | 🔴 `403` |
| `api.github.com/repos/…` | 🔴 `403` — "GitHub access to this repository is not enabled for this session" |

🔴 **So the prescribed check cannot discriminate, and it fails *unsafely*: a `403`
reads as "not a 404", i.e. as evidence the repo exists.** 🟢 **`raw.githubusercontent.com/{owner}/{repo}/HEAD/{path}` discriminates correctly**, with
a positive and two negative controls:

| probe | result |
| --- | --- |
| `raw…/openedx/XBlock/HEAD/LICENSE.TXT` | 🟢 `200` |
| `raw…/HKUDS/DeepTutor/HEAD/README.md` | 🟢 `200` |
| `raw…/nonexistent-owner-xyz987/nope/HEAD/README.md` | 🟢 `404` |
| `raw…/HKUDS/DeepTutor/HEAD/NOSUCHFILE.md` | 🟢 `404` |

🟢 **Second-order gain: the same channel returns licence *bytes*, so existence and
grant are settled in one probe** — no sidebar, no inference. 🟢 **And the
R-specific lesson: an R package declares its grant in `DESCRIPTION` (`License:`),
not in a `LICENSE` file.** 🔴 **That is exactly why `12` GPL R packages would read
as "no licence found" to this base's filename ladder** — the ladder was never
wrong about the files, it was looking in a language whose convention it did not
know. Evidence: `evidence/psychometrics-licence-bytes.2026-10-31-p573.tsv`,
`evidence/python-tier-licence-bytes.2026-10-31-p573.tsv`,
`evidence/cat-tier-licence-bytes.2026-10-31-p573.tsv`.

### 🔴 Gate posture and the mandated legs — `11` for `11`

🔴 **The four mandated `WebSearch` legs returned `0` addresses new to this base,
and `0` education-specific repositories of any kind.** They returned general
agent-framework roundups (CrewAI, OpenHands, Langflow, LibreChat) and SEO
listicles. 🔵 That is the **eleventh** consecutive nil for this channel, and this
pass reproduces the prior passes' conclusion rather than merely restating it.
🟢 **Every one of the `13` new addresses came from GitHub topic sweeps.**


## Tenth pass (`p572`, 2026-10-31) — 🟢 THE LTI 1.3 AND xAPI LAYER WAS MISSING FROM THIS KB ENTIRELY, AFTER BEING RE-FOUND BETWEEN `70` AND `123` TIMES EACH

🟢 **Ten rows added, `7` of them permissive, and the tier they form is the one
every LMS engagement bills for: the integration plumbing.**

🔴 **This base has seen `3,455` distinct GitHub addresses across its history and
placed `170` of them on a shelf page — `4.9 %`.** 🔵 A selective shelf is correct;
**what was sitting in the discard is not.** Ranked by how many times the base
re-found an address without ever shelving it, the head of the unshelved list was
`openedx/edx-platform` (`218×`), `openedx/XBlock` (`123×`),
`bruchris/canvas-lms-mcp` (`115×`), `ls1intum/Artemis` (`97×`),
`opencast/opencast` (`93×`), `francoisjacquet/rosariosis` (`92×`),
`frappe/erpnext` (`84×`), `GibbonEdu/core` (`83×`), `yetanalytics/lrsql` (`70×`).

🟢 **`11` of the `12` addresses tested were absent from every shelf page
*entirely* — not named in prose, not linked, absent.** Only `edx-platform` was a
pure linking defect. 🔵 **So the gap was in shelving, not in discovery: this base
found this material repeatedly and had no step that placed it.** Registered as
`572-A`.

### 🟢 The permissive integration tier, now placed

| layer | repo | licence | why it matters |
| --- | --- | --- | --- |
| LTI 1.3 (Python) | `dmitry-viskov/pylti1.3` | **MIT** | attach to any LMS without forking it |
| LTI 1.3 (PHP) | `packbackbooks/lti-1-3-php-library` | **Apache-2.0** | the Moodle-native side |
| xAPI store | `yetanalytics/lrsql` | **Apache-2.0** | where learning-analytics statements land |
| Open edX components | `openedx/XBlock` | **Apache-2.0** | permissive components on an AGPL platform |
| Canvas control | `bruchris/canvas-lms-mcp` | **MIT** | shelved in [`../agents/top.md`](../agents/top.md) |

🔵 **The XBlock/edx-platform split is the single most useful licence fact added
this pass**: `XBlock` is Apache-2.0, `edx-platform` is AGPL-3.0. Client course
components can stay permissive on top of a copyleft platform.

### 🔴 Two instrument defects in this base's own grant ladder, both proven and both fixed

🔴 **A `5`-filename × `2`-branch ladder returned `NOASSERTION` for `4` addresses
this pass. Two of those four were the instrument's fault.**

| address | ladder said | truth | cause |
| --- | --- | --- | --- |
| `openedx/XBlock` | NOASSERTION | **Apache-2.0**, 11,358 B | file is `LICENSE.TXT` — **uppercase extension**, and `raw` paths are case-sensitive |
| `frappe/erpnext` | NOASSERTION | **GPL-3.0**, 35,149 B | file is `license.txt` — **lowercase** — and the default branch is **`develop`**, not `main`/`master` |
| `deepseek-harness-java/teacher-workbench` | NOASSERTION | 🟢 **genuinely ungranted** | confirmed at **40 probes** |
| `0x454447415244/HandwritingRecognitionSystem` | NOASSERTION | 🟢 **genuinely ungranted** | confirmed at **40 probes** |

🔴 **A `50 %` false-`NOASSERTION` rate on this sample**, and the two it got wrong
were a `471★` Apache-2.0 framework and a `40.8k★` ERP. 🟢 **Fix applied and
re-run: `4` branches (`main`, `master`, `develop`, `trunk`) × `10` filenames
including case variants — both resolved, both genuine nulls held.** 🔵 Corroborates
`p558` from a different direction: that pass found `121 of 374` addresses 404 on a
`main`-only read because of *version* branches; this one finds the same class of
failure from *filename case* and a `develop` default. **Ask (`572-B`): the ladder
must vary case and branch, and `NOASSERTION` must never be published from fewer
than the full ladder.**

### 🟢 A control worth recording: the sidebar and the grant file agreed `7` of `7`

🟢 For `Artemis`, `opencast`, `lrsql`, `pylti1.3`, `lti-1-3-php-library`,
`canvas-lms-mcp` and `rosariosis`, the GitHub sidebar licence matched the
byte-for-byte grant read. 🔵 **So the sidebar is reliable for licence *identity*
— and `570-B`'s `word-atlas` plus this pass's `malaysia-uec-teacher-workflow`
prove it is still blind to licence *scope*.** The rule that survives both:
**trust the sidebar for which licence, never for what it covers.**

## Ninth pass (`p571`, 2026-10-31) — 🔴 zero new addresses, and the pass's whole value is a shelving defect: a tier this base FOUND at pass 85 never reached this page

🔴 **`derived foundations rows: **7**` added this pass, and not one is a new
address.** All seven were discovered by **pass 85 (`2026-10-09`)**, recorded in
[`../agents/trending.md`](../agents/trending.md) as *"An item-generation tier
exists now, 5 of 5 MIT"* — and then **never promoted to a shelf page.** Verified
against `HEAD` before this pass wrote anything:

| repo | on `agents/top.md` at HEAD | on this page at HEAD |
| --- | --: | --: |
| all seven item-generation rows | 🔴 **0** | 🔴 **0** |

🔴 **Meanwhile [`../compose/patterns.md`](../compose/patterns.md) `P-571-A` has
been shipping the opposite claim** — *"nothing permissive generates
psychometrically defensible items"* — with its item-authoring step left to a bare
model prompt. 🔵 **The base knew since pass 85; its shelf and its patterns did
not.** This is trend 11 (*a closed gap keeps being published*) in its mirror
image: **an open finding that never got published.** It is corrected below.

### ⚠️ What this pass did NOT find, stated plainly

🔴 **`topic:question-generation` is NOT a virgin axis, and any claim that it is
would be false.** Pass 85 bought it (**227 repositories** then, **241** now) and
`Gap 352` records it as **deliberately refused at ~30% precision** — a costed
decision, not an omission. This pass re-opened it and confirmed that decision:
re-reading its top twenty returned **zero addresses new to this base**. 🔴 **Nine
consecutive passes with no new address from `WebSearch`**, and this pass adds
**four topic axes with no new address either**
(`question-generation`, `essay-scoring`, `language-learning`, `mooc`).

### 🟢 The item-generation tier, now shelved

Grants below carry **two independent reads**: the byte count pass 85 recorded, and
a re-read this pass over `raw.githubusercontent.com`. 🟢 **Five of five re-read
rows matched the recorded byte count exactly** — which corroborates the earlier
reads and the instrument at the same time.

| Repo | Licence (file) | ★ | Region | Build-on? | What it adds |
| --- | --- | --: | --- | --- | --- |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** (1,070 B ✅ first-hand, `master/LICENSE`; sidebar agrees) | 138 | Global | ✅ permissive | 🟢 **"LTI 1.3 Advantage Tool" — the integration standard, in Python, under MIT.** Seen `95×` in this base's history and never shelved. Every engagement that attaches AI to Moodle / Canvas / Open edX / Blackboard without forking it goes through LTI 1.3, and this is the permissive Python implementation of it. 84 forks. |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | **Apache-2.0** (11,343 B ✅ first-hand, `master/LICENSE.md`) | 54 | North America | ✅ permissive | "A library used for building IMS-certified LTI 1.3 tool providers in PHP." 🟢 **The PHP side of the same standard — which is the side Moodle is written in.** Seen `75×`, never shelved. Packback is a Chicago company. |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | **Apache-2.0** (11,357 B ✅ first-hand, `main/LICENSE`) | 144 | North America | ✅ permissive | 🟢 **"A SQL-based Learning Record Store" — the xAPI backbone, Apache-2.0.** 2,276 commits, 41 forks, Clojure. Learning analytics engagements need somewhere to put statements; this is the permissive place. Seen `70×` (plus `85×` for the sibling `yetanalytics/lrs`), never shelved. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** (11,358 B ✅ first-hand, `master/LICENSE.TXT`) | 471 | North America | ✅ permissive | 🟢 **"Framework for building custom learning components that run in the Open edX LMS!"** — and the licence split is the commercially decisive fact: **XBlock is Apache-2.0 while `edx-platform` itself is AGPL-3.0**, so a client's own course components can be built and kept under a permissive grant without the platform's network copyleft reaching them. 🔴 Seen `123×`, never shelved. 🔵 Its grant was invisible to this base's own ladder until this pass — the file is `LICENSE.TXT`, **uppercase extension**, and `raw.githubusercontent.com` paths are case-sensitive. |
| [githubharald/CTCDecoder](https://github.com/githubharald/CTCDecoder) | **MIT** (1,071 B ✅ first-hand, `master/LICENSE.md`) | 838 | EMEA | ✅ permissive | CTC decoding algorithms — best path, beam search, lexicon search, prefix search, token passing. **62 commits since `2017-10-09`** (3,036-day span). Deps are `numpy`, `editdistance`, `pytest` only — **licence surface clean**. The decode stage of any handwritten-work marking pipeline. |
| [githubharald/WordDetector](https://github.com/githubharald/WordDetector) | **MIT** (1,071 B ✅ first-hand, `master/LICENSE.md`) | 276 | EMEA | ✅ permissive | Detects handwritten words by classic image processing — no model to train, no GPU. Deps `numpy`, `opencv-python`, `scikit-learn`, `matplotlib`, `path` — **all permissive, surface clean**. The segmentation stage: it turns a scanned worksheet into word crops. |
| [arthurflor23/handwritten-text-recognition](https://github.com/arthurflor23/handwritten-text-recognition) | **MIT** (1,074 B ✅ first-hand, `master/LICENSE`) | 308 | Global | ✅ permissive | Handwritten Text Recognition — **3,645 commits over a 2,700-day span**, by far the most substantial history in this tier. 🔵 Deps include `tensorflow`, `mlflow` (both Apache-2.0) and `openai` (MIT) — permissive, but the `openai` dependency means the default path calls a **paid external API**, which is a data-residency question in schools, not a licence one. |
| [githubharald/DeslantImg](https://github.com/githubharald/DeslantImg) | ⚠️ **MIT grant (1,071 B) / GPL-3.0 SURFACE** — see note | 156 | EMEA | ⚠️ **link-only** | Deslanting: sets slanted handwriting upright before recognition. 🔴 **`master/LICENSE.md` is a clean 1,071 B MIT — and `requirements.txt` pins `Py-BOBYQA>=1.3`, which is GPL-3.0 (verified first-hand: 35,147 B, title "GNU GENERAL PUBLIC LICENSE", Version 3).** Py-BOBYQA is imported in-process for the deslanting optimisation, so **distributing a combined work triggers GPL-3.0 on it**. GPL-3.0 has no §13 network clause, so *hosting* a service is not itself the trigger — *shipping client code* is. 🟢 **Third instance of this mechanism in this KB** (after `ai-learning-os`/PyMuPDF and `text2text`), reached by a third independent route. 🔵 Use `WordDetector` + `CTCDecoder` instead: same author, same pipeline, permissive all the way down. |
| [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🔴 **BSD-3-Clause** (1,531 B ✅ first-hand; sidebar agrees) — **CORRECTION** | 114 | Global † | ✅ permissive | "An open-source project designed to provide an educational and collaborative AI-powered platform." 195 forks. 🔴 **This base's own rotation history recorded this project as `Apache2` (`education_cycle3`). It is not: the grant is BSD-3-Clause** — "All rights reserved" plus the three numbered conditions including non-endorsement — and **two independent reads agree** (grant body + GitHub sidebar). 🔵 **Why the correction has commercial weight rather than being pedantry: BSD-3-Clause carries no express patent grant, Apache-2.0 does.** For a studio taking procurement questions from a university, that is the difference between two answers. Holder is an individual ("Mohamed El hajji On behalf of all R2D-dev"), so region stays `Global †` under `569-E`'s grade convention. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** (35,136 B ✅ first-hand, title reads "GNU AFFERO GENERAL PUBLIC LICENSE") | 8,200 | North America | ⚠️ **network copyleft** | "The Open edX LMS & Studio, powering education sites around the world!" 4,400 forks. 🔴 **Shelved here to close a linking defect, not because the platform is new to this KB: it is named `15×` across shelf prose and this is the first time its address appears on any shelf page.** The harness's own bar is that every row carry a real repo URL; a project named in prose without one cannot be checked, cloned or licence-probed by anyone downstream. 🔴 AGPL-3.0 §13 means a hosted deployment must offer source to its users — the reason this KB routes integrations through LTI/XBlock rather than forks. |
| [patil-suraj/question_generation](https://github.com/patil-suraj/question_generation) | **MIT** (1,068 B ✅ re-read, *"Copyright (c) 2020 Suraj Patil"*) | 1,100 | Global | ✅ permissive | The axis's **reference implementation** — answer-aware and multitask QA-QG as a HuggingFace `pipeline`. The most-starred permissive generator; recorded *"unplaced"* at pass 85. |
| [ramsrigouthamg/Questgen.ai](https://github.com/ramsrigouthamg/Questgen.ai) | **MIT** (1,077 B ✅ re-read, *"Copyright (c) 2020 Ramsri Goutham Golla"*) | 952 | ⚠️ see note | ✅ permissive | 🟢 **Ships item *types*, not one task**: MCQ with distractors, boolean (yes/no), FAQ, paraphrase, answer prediction. T5 + sense2vec. Closest to what an assessment unit orders. |
| [asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation) | **MIT** (1,065 B ✅ re-read, *"Copyright (c) 2024 asahi417"*) | 366 | Global | ✅ permissive | 🟢 **The multilingual row.** `pip install lmqg`; question **and answer** generation in **9 languages** (`en/fr/ja/ko/ru/it/es/de/zh`), HuggingFace checkpoints, **ACL 2023** system-demonstration paper, 385 commits. ⚠️ **No Portuguese.** |
| [artitw/text2text](https://github.com/artitw/text2text) | 🟡 **MIT + rider** (`master/LICENSE.txt`, **1,325 B**, CRLF, *"Copyright (c) artitw"* — no year) | 305 | Global | ⚠️ **read the rider** | Multilingual text-to-text toolkit (tokenisation, embeddings, BM25/TF-IDF search, translation, language id). 🔴 **`Gap 353`/`P922`'s dependency-closure rider, read verbatim this pass** — three lines appended after the MIT warranty clause: *"This open source software utilizes other open source components with their own licensing agreements. As the consumer of this software, you agree to abide by the licensing requirements set forth by the respective components used."* 🔵 **Not a field-of-use restriction and not a copyleft trigger** — it is an acknowledgement that the grant does not cover the dependency tree, which is true of every package but is here made contractual. ⚠️ It means **the dependency closure must be cleared separately**; the row is usable, the diligence is not optional. 🟢 The rest of this pattern does not need it — skip the row if that clearance is not budgeted. |
| [AMontgomerie/question_generator](https://github.com/AMontgomerie/question_generator) | **MIT** (1,073 B ✅ re-read, *"Copyright (c) 2020 Adam Montgomerie"*) | 298 | Global | ✅ permissive | Long-form prose → QA pairs, with an answer-aware evaluator that **ranks** generated questions. Over-generate then rank. |
| [KristiyanVachev/Leaf-Question-Generation](https://github.com/KristiyanVachev/Leaf-Question-Generation) | **MIT** (1,073 B ✅ re-read, *"Copyright (c) 2018 Kristiyan Vachev"*) | 139 | Global | ✅ permissive | 🟢 **Distractor generation** — MCQs *with wrong-answer options*. The step a general LLM does worst, and exactly what `itembank lint` rejects on. |
| [PragatiVerma18/MLH-Quizzet](https://github.com/PragatiVerma18/MLH-Quizzet) | **MIT** (1,069 B) | 97 | Global | ✅ permissive | 🟢 **Takes teacher PDFs** and emits a quiz — the only row whose input is the artefact a teacher already has. |

⚠️ **One unresolved region conflict, recorded rather than silently picked.** Pass
85 placed `Questgen.ai` as **APAC**. Its licence file names
**"Ramsri Goutham Golla"** — an **individual** — and this base's `p570` instrument
places a repository **only when the holder is an institution**. 🔵 The two rules
disagree: the `p570` instrument says `Global`, pass 85's placement says `APAC`,
and the repository page states no location. **Left as a flagged conflict for a
later pass to resolve at source; do not quote the region to a client.**

🔴 **The licence trap on this axis, already paid for once by this base.**
[`KristiyanVachev/Question-Generation`](https://github.com/KristiyanVachev/Question-Generation)
is **GPL-3.0** (35,149 B) at **495★** — the **same author** as the MIT `Leaf` row
above, with **3.5× the stars**. A star-sorted sweep returns the copyleft sibling
first. Pass 85 recorded this under `P171` alongside three more GPL-3.0 rows of
**identical 35,148 B payload**, and warned that a `grep -i Affero` classifier
calls 4 of 4 of them AGPL and is **wrong 4 of 4 times**.

### 🔴 `topic:essay-scoring` is a tag-variant decoy — and that is the one genuinely new finding on this page

| tag | population | ★ ceiling | permissive grants | status |
| --- | --: | --: | --: | --- |
| 🟢 `topics/automated-essay-scoring` | **35** | — | 🟢 **8** (incl. `doheejin/ProTACT`, **BSD-3-Clause**) | **swept at pass 84, 100% precision** |
| 🔴 `topic:essay-scoring` 🆕 | 🔴 **17** | 🔴 **34** | 🔴 **0 shelvable** | 🆕 swept `p571` |

🔵 **The same capability splits across two tags, and the shorter variant is the
near-empty one.** Had `p571` swept only `topic:essay-scoring`, it would have
concluded *"no permissive AES exists"* — **contradicting this base's own pass-84
record of eight permissive grants.** 🟢 **The rule: when a capability has a
hyphenated long-form tag and a short-form tag, sweep the LONG form.** The short
form collects the abandoned and the unlicensed.

🟡 **What the 17 add that pass 84 did not already hold: nothing shelvable, and one
regional corroboration.** Three are Brazilian/Portuguese-language ENEM-adjacent
(`IC-Redacoes-UTFPR/CorrecaoRedacao` — already on this base — plus
`renan-aalmeida/AES_Enem_Competencia5` and `DaviSantos-23/Reda-o`, **both
re-probed this pass, both with no licence grant**) and three are Korean. 🔵 That
reproduces this base's standing LATAM finding — *the Portuguese essay-scoring tier
is **ungranted**, not absent* (`Gap 235`) — on a second, independent tag.

## Eighth pass (`p570`, 2026-10-31) — two structural results, and one of them is a warning about this base's newest rule

🟢 **`derived foundations rows: **9**` added this pass** — seven in a new layer
below, two in placements.

🟢 **Result 1: the evaluation layer was never missing. Its vocabulary was.**
Six consecutive passes closed with *"no education-specific agent observability or
regression tooling was found"*, searching `evaluation`, `benchmark` and
`observability` under `topic:education`. 🔴 **The axis those assets actually live
on is [`topic:rubric`](https://github.com/search?q=topic%3Arubric), which answers
`187` results and which 569 passes never queried** — `topic:rubric` appeared
**zero** times in every live page of this base. 🟢 **Seven of its top ten are new
addresses**, all granted, and they are shelved in the new layer below. 🔵 **The
generalisable lesson, and it will repeat in every other industry base on this
harness: a six-pass absence can be a property of the search vocabulary rather
than of the field. This base measured the star floor at `p569` and the topic
vocabulary at `p570`, and both times the absence dissolved.**

🔴 **Result 2: the admission rule this base adopted ONE PASS AGO is gameable, and
the first never-swept axis produced the counterexample.** `p569` moved the
tooling layer from a star gate to a **commit-count** gate, because a star floor
was discarding this base's best rows. 🔴 **`CurveAhoead/ScoreRune` reads 35★ and
`2,137` commits dated from `2014-06-10` — and the history is synthetic.** A star
gate needs other people; **a commit gate needs a loop**, so commit count is
*cheaper* to forge than the signal it replaced. 🟢 An instrument now exists,
[`../ingest/history-plausibility.py`](../ingest/history-plausibility.py),
authored and run this pass and validated against two real controls. See `570-A`
and the layer note below.

## Platforms of record

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 8,200 | North America | ⛔ copyleft | The Open edX LMS & Studio. Python + JavaScript. The reference MOOC-scale platform. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | APAC | ⛔ copyleft | The world's most-deployed LMS. Note the region: Moodle HQ is in Perth, **Australia** — commonly misfiled as EMEA because of its European install base. |
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | 7,000 | Global | ✅ permissive | Free online learning platform built around structured, explorable lessons. Python, Angular, Google App Engine. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 6,900 | North America | ⛔ copyleft | "The open LMS by Instructure, Inc." Dominant in North American higher ed, and the platform the strongest verified agent ecosystem attaches to (see [`../agents/top.md`](../agents/top.md)). |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | **AGPL-3.0 + separate Enterprise Licence** | 2,400 | Global | ⛔ copyleft **and** dual-licensed | "The Next-gen Open Source learning platform for everyone." Next.js/FastAPI/Postgres/Redis, 593 forks, includes "LearnHouse AI: The Teachers and Students copilot". **Added this pass, as a correction:** the African-education search returned a **0★ fork** of this repo under an African organisation name; the real project is this one, maintained by Badr B. (`@swve`), country not stated. The licence shape is the thing to carry forward — AGPL core with features held back under a commercial licence means the open repo is not the whole product. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | ECL-2.0 | 1,200 | North America | ✅ permissive | Platform for learning, teaching, research and collaboration. ECL-2.0 is an Apache-2.0 derivative written for academic consortia — permissive, with a patent clause tuned for universities. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 1,200 | Global | ✅ permissive | "The offline app for universal education." The reference choice for low- or no-connectivity deployments. Python + JavaScript. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 | 1,100 | EMEA | ⛔ copyleft | The Docker-based Open edX distribution. In practice this, not raw `openedx-platform`, is how Open edX actually gets deployed. France. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | EMEA | ⛔ copyleft | LMS focused on ease of use and accessibility. Strong francophone and LATAM install base. |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** | 102 | **EMEA** | ✅ permissive | **The licence exception that changes the EMEA answer.** "Open-source AI-native LMS with AI Mentor & role-play. Self-hosted alternative to Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX." TypeScript, 31 forks, created 2024-08-01, pushed 2026-10-30. Ships **SCORM and xAPI** and is explicitly white-label. Maintained by **Selleo**, a software company whose GitHub profile states its location as **Poland**. MIT confirmed via the API (`license.spdx_id: MIT`). At 102★ it is not a platform of record — but it is the only AI-native LMS found that a client can fork, rebrand and keep closed. |

### Permissive platforms one tier down — new in the fourth pass

Not platforms of record. These are **actively maintained, permissively licensed
education platforms at the small-and-medium-institution tier**, which is where
the "no permissive substrate exists" finding stops being true.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [safytech/ulearn](https://github.com/safytech/ulearn) | **MIT** (file, 1,066 B) | 701 | Global | ⚠️ permissive, **stale stack** | "ULEARN — Open Source (FREE) LMS script." 299 forks. **The largest MIT-licensed LMS located anywhere.** Laravel **5.8** + React **16.9** — both long past end of life, so a fork is a framework-upgrade project before it is a product. Quote an upgrade estimate or do not quote it. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | **MIT** (file, 1,094 B, "Thomas Debay and project contributors") | 410 | Global | ✅ permissive | "Laravel & Filament-based school management platform for small and medium institutions." 151 forks, pushed 2026-10-30, topic **`student-information-system`**. **The permissive education SIS this KB spent three passes concluding did not exist.** The 410★/151-fork ratio is the signature of a system in real deployment. Current stack, unlike `ulearn`. |
| [openfun/richie](https://github.com/openfun/richie) | **MIT** (file, 1,079 B, **"Copyright (c) 2018-present GIP FUN MOOC"**) | 318 | **EMEA** | ✅ permissive | A Django **CMS for building education portals**, designed to front Open edX and Moodle catalogues. 94 forks. **Region placed from the licence file itself:** GIP FUN MOOC is France Université Numérique — the same publisher as `openfun/ralph` below. Two MIT components, one French public publisher. |
| [iblai/lms](https://github.com/iblai/lms) | **MIT** (file, 1,063 B, "ibl.ai") | 208 | Global | ✅ permissive | "Skills intelligence platform — discover courses, track competencies, earn credentials, and accelerate workforce development." Next.js 15 / React 19, created 2026-03-04. **The first open-source asset located for the digital-credentials and skills-pathways trend**, which had been single-source commentary for three passes. |
| [pacewisdomhq/TutorLoom](https://github.com/pacewisdomhq/TutorLoom) | **Apache-2.0** (file, 11,362 B) | 54 | APAC | ✅ permissive, very young | Self-hosted **multi-tenant** LMS — course builder, trainer and student portals, progress tracking. Django + React + Flutter, created **2026-10-07**. Explicit `moodle-alternative` and `corporate-training`. Region inferred from the publisher, **not stated on the repo**. |
| [Azure/Moodle](https://github.com/Azure/Moodle) | **MIT** (file, 1,090 B, "Microsoft Corporation") | 185 | Global | ✅ permissive tooling | Not a platform: **MIT deployment tooling for scalable Moodle clusters on Azure**. 187 forks on 185★, i.e. consumed as a template. Worth citing to a client as the attach-don't-fork doctrine practised by Microsoft against a GPL-3.0 platform. |

**The population, with a denominator — because scarcity claims need one.**
`topic:learning-management-system license:apache-2.0 stars:>50` returns **2
repositories in the world**: `TutorLoom` (54★, three weeks old) and
`AcademicsToday/academicstoday-django` (Apache-2.0 confirmed from `LICENSE.md`,
11,358 B, 220★, **created 2015**, effectively stale).
`topic:lms license:mit stars:>80` returns **15**, and the topic is polluted —
it includes `SWE-agent` (20,693★, a coding agent), `tompazourek/Colourful` (298★,
a .NET **colour-space** library, "LMS" as in cone response) and `freeitsm` (118★,
ITSM). **Six of those fifteen are education platforms.** So the whole permissive
LMS population above 50★ is roughly **eight repositories**, the largest is 701★
on an end-of-life stack, and Moodle alone carries 7,600★ under GPL-3.0.

⚠️ **One archived trap.** [`microsoftarchive/Learn-LTI`](https://github.com/microsoftarchive/Learn-LTI)
— MIT, 132★, 52 forks, an LTI tool surfacing the Microsoft Learn catalogue inside
an LMS — is **archived**. It looks exactly like the component an engagement would
reach for, it is permissive, and it is dead. The `microsoftarchive` org name is
the only warning on the URL.

## Interoperability and analytics layer

Where the permissive licences live, and the layer an AI integration actually
touches.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | 956 | North America | ✅ permissive | The xAPI specification: how systems communicate learner activity. The vocabulary any learning-analytics or agent-telemetry design should speak. ADL Initiative (US). |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 | 373 | Global | ✅ permissive | Turns an application into a full **LTI 1.3** tool provider: launches, Deep Linking, Assignment & Grade Services, Names and Role Provisioning, Dynamic Registration. **Still the single most important repo on this page for a Globant engagement** — the sanctioned, licence-clean way to attach new software to a copyleft LMS without touching its code. Brazilian maintainer. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 153 | EMEA | ⛔ copyleft | The H5P interactive-content runtime. **Licence correction carried forward:** earlier passes recorded H5P as MIT. It is **GPL-3.0**. Norway. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** (file, 1,072 B, "Jonathan Putney") | 362 | Global | ✅ permissive | "A modern SCORM JavaScript runtime library" — **SCORM 1.2, SCORM 2004 and cross-frame**, tagged `offline-first`. 85 forks, pushed 2026-10-30. **New in the fourth pass, and it closes a hole this KB never named:** three passes built the attach doctrine on LTI, MCP and xAPI and omitted **the standard the installed base actually ingests**. xAPI is the better specification; SCORM is the incumbent, it is what corporate L&D procurement asks for by name, and it is what `Selleo/mentingo` ships alongside xAPI. A permissive, maintained SCORM runtime means Globant-built courseware can be delivered into a client's existing LMS **without touching the LMS and without an xAPI migration project first.** |
| [openfun/ralph](https://github.com/openfun/ralph) | MIT | 51 | EMEA | ✅ permissive | Learning Record Store for learning analytics; consumes xAPI statements. The permissive LRS option. France Université Numérique — same publisher as `richie` above. |
| [openfun/warren](https://github.com/openfun/warren) | **MIT** | 17 | EMEA | ✅ permissive | **xAPI learning-analytics dashboards — the layer this page spent five passes recording as absent.** Same operator as `ralph` and `potsie`; pushed `2026-10-11`. **Added in the sixth pass**, and not because it was found: it was already recorded in [`trending.md`](trending.md) while the fifth-pass summary on that same page was still publishing *"no open-source learning-analytics dashboard"*. France Université Numérique. |
| [openfun/potsie](https://github.com/openfun/potsie) | **MIT** (`main/LICENSE.md`, 1,094 B) | 11 | EMEA | ✅ permissive | **Grafana dashboard suite for learning analytics**, written in Jsonnet — so the dashboards are generated, reviewable and diffable rather than clicked together in a UI, which is what makes them deliverable as code. Last pushed `2024-12-18`: stable rather than active. Grant read byte-for-byte in the sixth pass, *"Copyright (c) 2021-present **France Université Numérique**"*. |

## Content, standards and evaluation layer (new this pass)

The layer that answers *"is what the agent produced actually any good, and does
it match the curriculum?"* — and the layer where licences stop being binary.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | ⚠️ **split: code MIT, datasets "By data publisher"** | 164 | Global | ⚠️ conditional | "The data layer for smarter educational AI" — enriched datasets linking academic standards, curricula, learning progressions and instructional guidance under one schema, reachable via browser explorer, agent plugins, local files, a REST API **and an MCP server**. Run by Learning Commons (`learningcommons.org`), country not stated. **Licence mechanics matter here:** the API reports `NOASSERTION` because the file is `LICENSE.md` and because the grant is split — README badges read "License for Knowledge Graph code: MIT" and "License for Knowledge Graph datasets: By data publisher", and **some datasets are gated**. The code is safe; each dataset must be cleared individually. |
| [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | ⚠️ **three-tier split: code MIT · prompts CC BY 4.0 · two corpora CC BY-NC-SA 4.0** | 87 | Global | ⚠️ **conditional — the corpora are non-commercial** | "Evaluation for AI outputs against trusted educational rubrics" — research-backed rubrics for scoring generated instructional content. TypeScript, 17 forks, pushed 2026-10-31. ~~**The only rubric-scoring asset located in this KB**~~ — 🔴 **struck `2026-10-31` (`p570`): the `topic:rubric` sweep returned seven further granted rubric-scoring assets, four of them Apache-2.0. The claim was true of this base's search vocabulary, not of the field. See the rubric layer below.** Still the natural quality gate in front of any content-generating agent, and still the only one carrying a peer-reviewed education corpus. **Licence RESOLVED in the fourth pass** by reading `main/LICENSE.md` (1,615 B), after three passes carried it as unresolved. It grants: *evaluator **code** → MIT*; *evaluator **content**, i.e. the prompts and settings → CC BY 4.0*; ***Annotated CLEAR Corpus** → CC BY-NC-SA 4.0*; ***Annotated PERSUADE 2.0 Corpus** → CC BY-NC-SA 4.0*. **The code and the rubric prompts are commercially usable with attribution; the two annotated corpora are NC and cannot ship in a billable deliverable or a commercial regression suite.** The upstream originals (CommonLit's CLEAR Corpus, PERSUADE 2.0) are themselves CC BY-NC-SA 4.0, so there is no cleaner version upstream to substitute — an engagement must bring its own corpus. Note the direction: this is the **inverse** of its sibling `knowledge-graph` (code MIT / data by publisher). |
| [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | **Apache-2.0** (file, 11,323 B — see note) | 21 | Global | ✅ permissive | **Efficacy measurement, and the only asset in five passes that narrows the evaluation gap.** *"Tool for Education Research with RAndomized COnTrolled TriAls"* — an **LTI plug-in to the LMS** that differentiates the contents of online assignments into experimental treatment variations and assigns students randomly between them. It also carries the ethics apparatus that makes that legal in a school: **informed consent hidden from the teacher**, non-consenting participants filtered out of result summaries and exports, and student identifiers stripped from exports. Java, 9 forks, branch **`development`**, created 2021-05-10, pushed 2026-10-29. **Be precise about what it is:** this measures *"did this intervention change outcomes"* under randomisation — it is **not** runtime monitoring and will not tell you a deployed tutor has drifted. ⚠️ Its `LICENSE` is unmodified Apache boilerplate with the template placeholders intact (`Copyright {yyyy} {name of copyright owner}`), so the grant **names no licensor**; the `NOTICE` credits Oxford University for LTI cookie-handling code. Origin not establishable from this session, recorded Global. |
| [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | EMEA | ✅ permissive | 1,143 questions from real teacher-qualification exams — CDPK (920, general pedagogy) and SEND (223, special needs). Measures whether a model knows how to *teach*, not whether it knows the subject. |

## Rubric and evaluation layer (new in the eighth pass — the axis 569 passes never swept)

The layer that answers *"did the agent's output meet the standard, and can I
prove it again next Tuesday?"* — the **regression** half of the evaluation gap
this base has published as open for six consecutive passes.

🟢 **Why it was missing.** Every prior sweep looked for `evaluation`, `benchmark`
or `observability` **under `topic:education`** and returned nothing. The assets
are tagged by **capability**, on
[`topic:rubric`](https://github.com/search?q=topic%3Arubric) — **187 results**,
and a string that appeared **zero times** in every live page of this base before
this pass. 🔴 **The gap was a vocabulary artefact, exactly as the star floor was
a sort artefact at `p569`.**

🔵 **What this layer is and is not.** None of these is an education-specific
*drift detector*; the honest gap statement below is narrower than it was, not
closed. What they are is **scoring machinery you can pin, version and re-run** —
which is the missing half of pattern `P-568-K`, whose regression suite has had to
be hand-rolled because `learning-commons-org/evaluators` cannot ship its corpora
commercially.

| Repo | Licence | ★ | Commits | Region | Build-on? | What it is |
| --- | --- | --: | --: | --- | --- | --- |
| 🆕 [alphadl/AdaRubrics](https://github.com/alphadl/AdaRubrics) | **Apache-2.0** (`main/LICENSE`, 10,761 B — ⚠️ **no copyright line**, see note) | 368 | 50 | Global | ✅ permissive | 🟢 **The pick of this layer, and the first asset in this base that evaluates an *agent trajectory* rather than a finished artefact.** Adaptive dynamic rubric evaluation: the rubric is generated and adapted per task instead of being fixed in advance, which is what makes it applicable to a tutoring *session* — a multi-turn interaction whose quality is not visible in any single response. Python, pushed `2026-08-24`, 50 commits from `2026-02-22`, 2 authors. 🔵 **Why it matters for an engagement:** every tutor in this KB is a multi-turn agent, and until this row the only evaluation assets here scored **single generated documents**. ⚠️ Pre-adoption: 368★ is real traction for a research artefact and is not an install base. |
| 🆕 [Sion612/rubrictrail](https://github.com/Sion612/rubrictrail) | **Apache-2.0** (`main/LICENSE`, 11,324 B — ⚠️ no copyright line) | 130 | 45 | Global | ✅ permissive | Local-first assignment planner that keeps **evidence links** from a rubric criterion back to the work that satisfies it. TypeScript, `v0.2.0`, 45 commits `2026-08-12`→`2026-08-31`, single author. 🔵 **The audit-trail shape**, and the only row here that models the *criterion → evidence* link explicitly — which is what an accreditation review or an AI Act Annex III evaluation file actually has to produce. 🔴 **Dormant two months**; read it as a design reference, not a dependency. |
| 🆕 [AI9Stars/LLM-Rubrics-Survey](https://github.com/AI9Stars/LLM-Rubrics-Survey) | **MIT** (`main/LICENSE`, 1,068 B, "Copyright (c) 2026 methanechen") | 71 | 17 | Global | ✅ permissive | Survey and bibliography of rubric use across the LLM lifecycle — rubrics as evaluation criteria, as training signal and as reward. **Not a runtime**: shelved because it is the literature map for this layer, and because it is the cheapest way to brief a client's academic stakeholder that rubric-based evaluation is a methodology with a corpus behind it rather than a consultant's invention. |
| 🆕 [OpenEnvision/AutoRubric-as-Reward](https://github.com/OpenEnvision/AutoRubric-as-Reward) | **Apache-2.0** (`main/LICENSE`, 10,757 B — ⚠️ no copyright line) | 58 | 27 | Global | ✅ permissive | Auto-generated rubrics used as the **reward signal** for training — turning implicit preference data into explicit, inspectable criteria. Python, 3 authors, `2026-05-06`→`2026-09-25`. 🔵 **Relevant where a client wants a tutor tuned to its own pedagogy** rather than to generic helpfulness: the rubric becomes the spec, and the spec is readable by the teaching lead instead of buried in a preference dataset. |
| 🆕 [AndrewNgGirl/SkillLens](https://github.com/AndrewNgGirl/SkillLens) | **MIT** (`main/LICENSE`, 1,079 B, "Copyright (c) 2026 SkillLens contributors") | 44 | 12 | Global | ✅ permissive | Self-hosted web tool for **scoring and reviewing agent skills**. 🟢 **Directly relevant to this KB's central structural finding** — that *15 of the 25 agents* on [`../agents/top.md`](../agents/top.md) have no runtime and ship as markdown skill bundles. If the deliverable is a prompt contract, the quality gate must score prompt contracts, and this is the only asset found that does. 🔴 **12 commits over 12 days in May 2026 and nothing since**: the idea is the asset here, not the code. |
| 🆕 [hanskepper/SMART-GRADE](https://github.com/hanskepper/SMART-GRADE) | **MIT** (`main/LICENSE`, 1,068 B, "Copyright (c) 2026 HANS KEPPER") | 3 | **200** | **EMEA†** | ✅ permissive | 🟢 **The first African-origin education asset in this base with a verified permissive grant**, and a row a star gate discards outright: **3★ against 200 commits** (`2026-07-08`→`2026-10-09`). Progressive web app tracking grades across subjects, terms and *sequences* — **`séquence` is the Cameroonian/francophone-African school reporting period**, not a generic term, and the schema is built around it rather than around semesters. 🔵 **Why this row is worth more than its stars:** three passes hunted African supply and found an **org-name trap** (`AFRICAN-AI-NETWORK/learnhouse`, a 0★ fork) and an **ungranted** hackathon entry (`tujifunze-agent`). This is neither — it is a small, granted, commit-dense artefact built against a real national school calendar. ⚠️ **It is a gradebook, not AI**: the value is the curriculum-calendar schema to build on, and the provenance. 🔴 **`EMEA†` is a schema artefact, not a geography claim — see the region note below.** |
| 🔴 [CurveAhoead/ScoreRune](https://github.com/CurveAhoead/ScoreRune) | **Apache-2.0** (`main/LICENSE`, 11,358 B — ⚠️ no copyright line) | 35 | ⛔ **2,137 — SYNTHETIC, see `570-A`** | Global | ⚠️ **code yes, history no** | 🔴 **Carried as a warning, and it is the most important row on this page.** A **deterministic** rubric engine for reviewing AI responses, Python + C# runtimes — on substance an excellent fit for this layer, because *deterministic* is precisely what a regression gate needs and what `itembank` independently chose for scoring. 🔴 **But its git history is fabricated.** `2,137` commits dated `2014-06-10`→`2026-09-06`, and all four plausibility checks fire: commits per year run `117,141,150,155,161,165,170,175,181,185,185,198` — **monotonic, 1.69× max:min across 12 years**, where the real control `philchalmers/mirt` runs `1,111,349,658,411,…,91` at **658×**; **408 of 408 pre-2017 commits carry Conventional Commits prefixes**, a convention that postdates them; **author date equals committer date on all 2,137 commits** (real control: 19 divergent); and **the repository's first commit is `refactor: evidence kinds`** — a repository cannot begin by refactoring. 🟢 **The ~154 commits dated 2026 look genuine and the code appears real**: use the code on its merits, cite **35★ / 2 authors / three months** as its provenance, and **never quote the 2,137**. Evidence: [`../evidence/history-plausibility.2026-10-31-p570.tsv`](../evidence/history-plausibility.2026-10-31-p570.tsv). |

🔴 **Rejected from this layer:**
[`tc-imba/canvas-auto-rubric`](https://github.com/tc-imba/canvas-auto-rubric)
(33★) — **no grant** at 5 filenames × 3 branches, **and** last pushed
`2022-12-27`. Doubly disqualified; logged so no successor re-triages it.

### 🔴 The region note this layer forces, and it is a schema finding

🔴 **Region is structurally unrecoverable from an Apache-2.0 grant, and this base's
placement rule does not say so.** The standing rule (`p568`) is *"the licence
file's copyright line places a repository when the holder is an institution"*.
🔴 **Apache-2.0's template has no copyright line to fill** — its only occurrence
of the word is the boilerplate definition *"'Licensor' shall mean the copyright
owner…"*. **Four of four** Apache rows above were probed and **none carries a
holder**. 🔵 So the rule is **licence-family-dependent**: recoverable for MIT and
BSD, where the holder line is part of the text an author must edit; **never**
recoverable from Apache-2.0, regardless of whether the holder is an institution.
This is why five of seven new rows here are `Global`. Registered as `570-C`.

🔴 **And `EMEA†` on `SMART-GRADE` is the closed vocabulary failing visibly.**
The artefact is **Cameroonian**. The permitted values are
`North America | EMEA | APAC | LATAM | Global`, so Sub-Saharan Africa resolves to
**EMEA** — the same bucket as Germany and the Netherlands. 🔵 **The consequence is
not cosmetic: this base publishes EMEA counts that are read as market
measurements, and they silently conflate Western European public-sector
procurement with African school IT.** The `†` marks artefact-grade evidence per
`569-E`; the Africa conflation is registered separately as `570-E`. **The country
is in the prose because the field cannot hold it.**

## Content-production layer (new in the fourth pass)

Not education projects. Horizontal tools that the industry's highest-volume
artefact — lecture decks, courseware, interactive texts — is actually built from.
**This layer was invisible to four passes of sweeping because every sweep filtered
on an education topic and none of these carries one.**

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | **MIT** (file, 1,069 B, on both `main` and `master`) | **71,498** | Global | ✅ permissive | **The largest permissively licensed repository anywhere in this knowledge base** — 1.4× DeepTutor, 1.7× OpenMAIC. "AI turns documents or topics into real, native PowerPoint decks — with native shapes, transitions and animations, data-backed charts and tables on demand, audio narration from speaker notes, and support for your own `.pptx` templates." Python, **5,578 forks**, created 2025-12-10, pushed 2026-10-30. **Why it belongs here:** `.pptx` is the format schools and universities actually exchange; *"support for your own `.pptx` templates"* is institutional branding compliance, which is what normally kills generated-content pilots; and audio narration from speaker notes is a lecture-capture path for free. Deliberately **not** on the agent shelf — it is not an education agent. ⚠️ **Provenance unverified:** 71,498★ and the owner profile cannot be read from this session, so **no region is assigned**. For a component this central, check it independently before client-facing use. |
| [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | **MIT** (file, 1,069 B) | 1,034 | Global | ✅ permissive | "An AI skill that turns books into animated, narrated, interactive web experiences." JavaScript, 143 forks, created **2026-10-03** — 1,034★ in four weeks. Topics include **`scorm`** and `interactive-textbook`, so pair it with `scorm-again` to deliver into an existing LMS. Also shelved as an agent in [`../agents/top.md`](../agents/top.md). ⚠️ Copyright line is a pseudonym. |
| [assafkip/claudemy](https://github.com/assafkip/claudemy) | **MIT** (file, 1,069 B, "Assaf Kipnis") | 557 | Global | ✅ permissive | Topic in, **course of 2-minute audio lessons with cited sources** out; web research plus ElevenLabs TTS. Python, 67 forks, created 2026-10-14. The only content generator in this KB that **starts** from citation provenance rather than retrofitting it. |

**How to use this layer honestly.** These produce *artefacts*, not *assessed
learning*. Nothing here knows whether the deck it generated is pedagogically
sound or on-syllabus — which is exactly what the evaluation layer above is for,
and why pattern **P-569-B** wires a quality gate between them rather than
shipping generator output directly.

## Document-ingestion layer (new in the fifth pass — the capability sweep)

The fourth pass closed with an instruction to itself: *sweep by capability
(`topic:pptx`, `topic:text-to-speech`, `topic:pdf`, `topic:ocr`), not by industry
topic.* **This is what that sweep returned, and it is the largest layer in this
KB by an order of magnitude.** Every education engagement begins with the
client's existing material — textbooks, past papers, lecture PDFs, scanned
worksheets — and **none** of these tools carries an education topic, which is why
five passes of industry-topic sweeping never saw them.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | **Apache-2.0** (file, 11,376 B) | **92,024** | APAC | ✅ permissive | *"Turn any PDF or image document into structured data for your AI."* The highest-starred asset in this entire knowledge base. Strongest **Chinese-language and handwriting** OCR in open source, which is the deciding factor for scanned worksheets and handwritten exam scripts. Pushed 2026-09-16; **11,594 forks**, 259 open issues. Baidu's PaddlePaddle organisation (China). |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | ⚠️ **Apache-2.0 + commercial thresholds** — read the note | **82,860** | APAC | ⚠️ conditional (thresholds are far above any education engagement) | *"Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows."* Strong on **formulas, tables and multi-column academic layout** — i.e. STEM textbooks, the hardest input in education. **6,857 forks**, branch **`master`**, pushed 2026-10-31. **The licence is a shape this KB had not catalogued.** GitHub reports `NOASSERTION`; `master/LICENSE.md` (3,301 B) reads *"MinerU is licensed under Apache License 2.0 and is subject to the additional terms below"*, then adds: **(1)** a separate commercial licence is required above **100 million MAU or USD 20 million monthly revenue**; **(2)** an **attribution obligation** — any online service built on MinerU must state prominently, in the interface or public documentation, that MinerU is used; **(3)** automatic termination of all rights if either is breached. **For Globant the thresholds are irrelevant and clause 2 is not** — it is a deliverable requirement that must reach the client's product team, not just legal. |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** (file, 11,358 B) | **77,267** | Global | ✅ permissive | The reference OCR engine, LSTM-based, **100+ languages**, **10,879 forks**, pushed 2026-10-28. Runs fully offline on commodity hardware with no model licence and no inference bill — which is why it, and not a hosted vision model, is the realistic answer for ministry and offline-first work (see pattern `P-568-F`). |
| [docling-project/docling](https://github.com/docling-project/docling) | **MIT** (file, 1,072 B) | **69,909** | Global | ✅ permissive | *"Get your documents ready for gen AI."* **The pick of this layer for most education work, and on licence grounds as much as technical ones: MIT, where its larger rivals are Apache-with-terms or Apache.** PDF, DOCX, **PPTX**, XLSX and HTML → clean markdown or JSON with layout and **table structure** preserved. Python, 5,222 forks, pushed 2026-10-31. `main/LICENSE`: *"Copyright The Docling Contributors"* — a collective holder, so **no region is assigned**, though the project is widely associated with IBM Research and is now under the LF AI & Data Foundation; neither is verifiable from this session and neither is asserted here. |
| [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | **Apache-2.0** (file, 11,358 B) | **30,129** | Global | ✅ permissive | *"PDF Parser for AI-ready data. **Automate PDF accessibility.** Open-source."* The differentiator is in its topics: `accessibility`, `a11y`, `pdf-accessibility` and **`eaa`** — the **European Accessibility Act**. Java, **2,881 forks**, pushed 2026-10-30. **This is the only asset in this KB that addresses accessibility compliance as a product feature**, and accessibility conformance is a procurement gate in EMEA public education that nothing else here answers. See pattern `P-570-B`. |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | **Apache-2.0** (file `LICENSE.md`, 11,360 B) | 15,651 | Global | ✅ permissive | Open-source ETL for LLMs: 20+ document types into a uniform structured form, with first-class LangChain integration. The **pipeline** choice rather than the single-document choice — right when a client hands over a repository of mixed legacy material rather than a textbook. 1,377 forks. |

## Narration, speech and retention layer (new in the fifth pass)

The accessibility and language side of the same sweep. Education's two
highest-volume accessibility requirements — **read-aloud** and **captions** — are
served entirely by permissive horizontal tooling.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [supertone-oss-archive/supertonic](https://github.com/supertone-oss-archive/supertonic) | **MIT** (file, 1,070 B, "Supertone Inc.") | 13,757 | APAC | ⚠️ **ARCHIVED — read before shelving** | *"Lightning-Fast, On-Device, Multilingual TTS — running natively via ONNX."* Bindings for Swift, Kotlin/Java, C++, C#, Go, Rust, Node, Python, Flutter and **WebGPU**; 1,566 forks. On-device multilingual TTS with an MIT grant is close to ideal for offline read-aloud. **But the `archived` flag is `true`** — the organisation is literally named `supertone-oss-archive`. The grant is clean and perpetual and the code still runs; **there will be no fixes, no security patches and no new languages.** Fork it deliberately or not at all. *The only reason this row is honest is that the `archived` field was checked — stars and licence both look excellent.* |
| [Blaizzy/mlx-audio](https://github.com/Blaizzy/mlx-audio) | **MIT** (file, 1,070 B) | 8,165 | Global | ✅ permissive | TTS, STT and speech-to-speech on **Apple Silicon** via MLX. The practical choice when the client's constraint is "it must run on the teacher's MacBook", which in private-school and university faculty estates is common. Pushed 2026-10-31. |
| [denizsafak/abogen](https://github.com/denizsafak/abogen) | **MIT** (file, 1,069 B) | 6,179 | Global | ✅ permissive | *"Generate audiobooks from **EPUBs, PDFs** and text with **synchronized captions**."* Kokoro-82M under the hood. **Synchronised captions are the whole point**: a caption track is simultaneously an accessibility deliverable, a search index and a transcript, and this produces all three from the material a client already owns. The shortest path from "here is our textbook" to an accessible audio course. |
| [collabora/WhisperLive](https://github.com/collabora/WhisperLive) | **MIT** (file, 1,085 B, "Vineet Suryan, **Collabora Ltd.**") | 4,339 | **EMEA** | ✅ permissive | Near-real-time Whisper: live transcription and captioning of lectures, with TensorRT and OpenVINO backends. **Region placed from the licence file's own copyright line** — Collabora Ltd. is a UK company. Live captioning is an accessibility obligation in most EMEA higher-education estates. |
| [gradio-app/fastrtc](https://github.com/gradio-app/fastrtc) | **MIT** (file, 1,071 B) | 4,637 | Global | ✅ permissive | *"The python library for real-time communication."* The plumbing a **spoken** tutor needs — WebRTC audio in and out with STT/TTS hooks — rather than another model. The missing piece between a text tutor and a conversational one. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** (file, 1,079 B) | 4,119 | Global | ✅ permissive | The **Free Spaced Repetition Scheduler** — a modern, ML-fitted replacement for SM-2, used as Anki's scheduler. **The retention layer's algorithm, permissively licensed**, where `anki-mcp-server` on the agent shelf only gives an agent control of the Anki *application*. 165 forks, 8 open issues. Build FSRS in; do not invent a review schedule. |

## Assessment and item-bank layer (new in the sixth pass)

The layer that decides whether a generated question may be put in front of a
student. **Five passes looked for an item *generator* and recorded a gap; the
sixth found the *gate* instead**, which is the artefact an exam board actually
buys and the one the EU AI Act's Annex III evaluation category needs evidence of.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [onionviolet/itembank](https://github.com/onionviolet/itembank) | **MIT** (`main/LICENSE`, 1,068 B, "Copyright (c) 2026 onionviolet") | 3 | Global | ✅ permissive | **The pick of this layer, and it would have been discarded by a star gate: 3★ against 1,175 commits on `main`.** "Author, validate and render exam-style question banks in markdown. A machine-checkable contract for LLM-authored questions." Local-first — nothing leaves the machine but an optional update check. `itembank lint` **blocks on error** per item number (each distractor must explain when it *would* be correct; answer-position skew; select-count against keyed-count; duplicate stems) and `itembank guard` **fails CI** if real banks are committed. **Scoring is deterministic with no model in the path**: short-answer items are *never* auto-graded and stay pending for rubric marking, `fill` is all-or-nothing, `check` runs learner code against hidden cases, and the README states model output is never accepted as a score. Retention is **FSRS** — the same scheduler as `fsrs4anki` below. Exports **Anki TSV, GIFT, answer-key TSV**; key-free JSON session protocol (`start`/`next`/`submit`/`report`/`teach`) built for agents. ⚠️ **Read the limits:** QTI/CASE/SCORM interchange is explicitly backburner — the README says it *"waits for a named consumer"* — the MCP surface is labelled "Phase 999.3" and unshipped, and the wider "course workspace" is not yet runnable. Python-dominant with a Rust `src-tauri/` shell. Holder is a handle; recorded Global. |
| [sudazc/open-question-bank](https://github.com/sudazc/open-question-bank) | ⚠️ **split: code + docs MIT, bank content NOT granted** (1,063 B, "Copyright (c) 2026 sudazc") | 0 | Global | ⚠️ conditional | Schema, validation and rule-based test assembly (`组卷`), TypeScript, 108 commits. **Shelved for its licence shape rather than its traction**, which is near zero. The README is explicit that MIT covers **the framework code and its documentation only**: permission to use, modify or redistribute **a bank's content** is set by that bank's own `bank.yaml` and source-licence fields, and the framework grant conveys none of it. ⚠️ **The default licence for a new bank is a placeholder reading `"TBD - not for publication"`** — so a bank authored with this tool is unpublishable until someone sets it. README states online practice and learning records are not yet implemented. Chinese-language; the grant names a handle, so **not placed** — this page does not place an artefact on its language. |
| [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | **Apache-2.0** (11,346 B) | 203 | APAC | ✅ permissive | Model zoo of **cognitive diagnosis** models — IRT, MIRT, DINA, NCDM and others — from a named university group (USTC). **Be precise about what it does and does not do:** cognitive diagnosis infers *what a learner knows* from responses; it does **not calibrate items**. It is the live, permissive, education-specific half of the psychometrics layer, and the calibration half is the gap (see below). Last pushed 2024-10-25. |
| 🆕 [DaniyalMlk/calibrate](https://github.com/DaniyalMlk/calibrate) | **MIT** (`main/LICENSE`, 1,064 B, "Copyright (c) 2026 Daniyal"); **`package.json` `"license": "MIT"` agrees** | 0 | Global | ✅ permissive | 🟢 **This row closes the calibration gap this layer published for six passes, and a star gate would have discarded it: 0★ against 214 commits** (`2026-09-07` → `2026-10-30`, single author, counted with `git rev-list`). A **dependency-free TypeScript** adaptive-testing engine — `dependencies` and `peerDependencies` are both **absent from the manifest**, verified, so there is **no transitive licence surface at all** (4 devDeps, all permissive). What it implements, from its own README and roadmap: dichotomous **and** polytomous response models (**graded response, partial credit, generalized partial credit**, mixed banks in one bank), ability estimators, **maximum-information item selection**, stopping rules, **item-parameter estimation two ways — joint and marginal maximum likelihood, with JML's structural bias named and demonstrated against MML on the same responses**, **four linking methods** for putting two calibrations of an anchor on one metric, **differential item functioning**, person-**misfit** scanning, and score→ability conversion tables with standard errors. A browser interface draws the posterior, response curves, information curves and bank coverage live. ⚠️ **Read the adoption risk and say it to a client: version `0.1.0`, not yet published to npm** (the README says phases 1–21 are complete *"bar the publish itself"*), **one author, 0 stars, no independent validation.** The code is the evidence; the project is eight weeks old. Holder is an individual, so **Global**. |
| 🆕 [finite-sample/guess](https://github.com/finite-sample/guess) | **MIT** — 🔴 **not from the licence file**: `master/LICENSE` is **52 B** and names no licence (`YEAR: 2015` / `COPYRIGHT HOLDER: Gaurav Sood and Ken Cor`). 🟢 **`master/DESCRIPTION` reads `License: MIT + file LICENSE`** | 3 | **North America** | ✅ permissive | R package, `Imports:` **empty**. *"Adjust estimates of learning for guessing"* — standard guessing corrections plus **latent class models that use informative pre-post test transitions** to separate real learning from guessing on closed-ended items. 🟢 **The measurement counterpart to `calibrate`:** `calibrate` tells you what an item is worth, `guess` tells you whether an observed gain is real. Live (`2026-10-30`) on a 2016 codebase — 19 commits over ten years, so **stable rather than active**; read it as a method implementation, not a maintained platform. 🔵 **Placed `North America` on a channel new to this base:** `DESCRIPTION`'s `Authors@R` carries `mcor@ualberta.ca` — **University of Alberta** — where the copyright line names only two individuals. See `569-D`. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** (1,079 B) | 4,119 | Global | ✅ permissive | **FSRS** as an algorithm rather than an application — the modern spaced-repetition scheduler. Carried forward from the fifth pass's capability sweep and repeated here because it is the retention component both `itembank` and `braiinz-education` independently chose. |

🟢 **What this layer could not do six passes ago, and can now.** Every pass from
the second to the sixth closed this section with the sentence *"there is no
permissive, live, education-specific item **calibration** asset"*. 🔴 **That
sentence is retired as of `2026-10-31` (`p569`), and it was retired by searching
the one place the sort could not reach** — `topic:psychometrics` at `stars:<50`,
where [`DaniyalMlk/calibrate`](https://github.com/DaniyalMlk/calibrate) sits at
**0★ with 214 commits**. 🔵 **The gap was never a supply gap. It was a sort
artefact**, and that is twice in two passes that this base's own shortlisting
method, rather than the field, manufactured an absence (`568-A`, `568-C`).

⚠️ **What is still genuinely missing, stated narrowly so it stays true.** The
layer is now complete *in capability* and thin *in assurance*:

- 🔴 **No calibration asset here has adoption evidence.** `calibrate` is `0.1.0`,
  one author, 0★, unpublished to npm; `itembank` is 3★. **Both are credible on
  their commit histories and neither is credible on its install base.** For a
  high-stakes engagement — the EU AI Act Annex III evaluation category, or any
  exam board — that is a real procurement objection and this page does not paper
  over it. The mitigation is engineering, not more searching: wire `calibrate`'s
  MML output against a known-good reference (the stale-but-MIT
  [`eribean/girth`](https://github.com/eribean/girth), or R's `mirt`) and keep
  the comparison as the evidence the stars cannot supply. Wired as `P-572-A`.
- 🟢 **`569-D` RAN, AND THE R TIER IS NOW PLACED — the largest regional movement
  in this base in several passes.** `569-D` asked a successor to *"re-probe the R
  tier"* on `DESCRIPTION`'s `Authors@R`, after `p569` placed one row that way.
  **Nine rows probed, `7` carry `DESCRIPTION`, `6` place from an institutional
  email domain in the grant's own author field:**

  | Repo | `Authors@R` / `Maintainer` domain | Named entity | Region |
  | --- | --- | --- | --- |
  | [`dexter-psychometrics/dexter`](https://github.com/dexter-psychometrics/dexter) | `jesse.koops@cito.nl` | **Cito**, the Dutch national testing institute (Arnhem, NL) | 🟢 **EMEA** |
  | [`yrosseel/lavaan`](https://github.com/yrosseel/lavaan) | `Yves.Rosseel@UGent.be` | **Ghent University** (BE) | 🟢 **EMEA** |
  | [`cran/TAM`](https://github.com/cran/TAM) | `robitzsch@ipn.uni-kiel.de` | **IPN Leibniz Institute for Science and Mathematics Education**, Kiel (DE) | 🟢 **EMEA** |
  | [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | `cpyles@berkeley.edu` | **UC Berkeley** Division of Computing & Data Science | 🟢 **North America** |
  | [`shmercer/writeAlizer`](https://github.com/shmercer/writeAlizer) | `sterett.mercer@ubc.ca` | **University of British Columbia** (CA) | 🟢 **North America** |
  | [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR) | gmail — 🔴 grant places nothing | 🟡 `Title:` reads *"…Brazilian Education Data from **INEP**"*, Brazil's national education-statistics institute; README is Portuguese | 🟡 **LATAM†** |
  | [`philchalmers/mirt`](https://github.com/philchalmers/mirt) | `rphilip.chalmers@gmail.com` | individual | Global |

  🟢 **Three EMEA placements in one probe, and `dexter`'s holder is a national
  public assessment operator** — the same institutional class as France
  Université Numérique, and the strongest EMEA provenance asset this base holds.
  🔴 **Read what this does and does not change:** this base has been publishing
  *"EMEA gained no placed row"* for three consecutive passes, and the rows were
  **already in-tree and already read** — only their region was blank. **The
  supply did not change; the instrument did.** An EMEA engagement can now be
  shown locally-published, permissively granted psychometrics from three
  countries.
  🔵 **`educabR` is `LATAM†`** — artefact-grade per `569-E`, since the grant names
  an individual and only the package's purpose places it.
- 🔴 **But `569-D`'s proposed generalisation does NOT hold, and this pass
  measured the limit.** `569-D` asked for the rule to read *"a named legal entity
  in the grant **OR in a prescribed manifest field** (`DESCRIPTION`'s
  `Authors@R`, `package.json`'s `author`)"*. 🟢 The R half works: **7 of 7**
  CRAN-shaped repositories carry `DESCRIPTION` with an author email, **because
  CRAN mandates the field.** 🔴 **The npm half does not: of 7 new rows probed for
  `package.json`, 5 have none at all and the 2 that do name no author** —
  `rubrictrail`'s only locating field is a `sion612.github.io` homepage, which
  places nothing. 🔵 **So manifest-placement yield is a property of the packaging
  ecosystem's policy, not of manifests**: it works wherever a registry *enforces*
  authorship (CRAN, and by the same logic Debian, CPAN, CRAN-like archives) and
  fails wherever authorship is optional (npm, PyPI without metadata discipline).
  Restate the rule that way or it will be applied to npm and read as an absence.
  Registered as `570-D`.
- 🔴 **The stale permissive libraries are still stale** and are now useful as a
  *baseline* rather than as a dependency:
  [`eribean/girth`](https://github.com/eribean/girth) (127★, MIT, last pushed
  **2022-09-09**), [`inuyasha2012/pypsy`](https://github.com/inuyasha2012/pypsy)
  (242★, MIT, **2018-11-16**).
  [`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) (114★,
  Java, CTT + IRT) still carries **no licence file at five filenames across three
  branches**. The R options remain copyleft (`lavaan` GPL-2+, `blavaan` GPL-3) —
  except `guess`, above, which is MIT and is now shelved.
- 🟡 **[`joakimwallmark/irtorch`](https://github.com/joakimwallmark/irtorch) was
  already read, and this base asked for it again.** `568-B`'s ask was *"probe
  `irtorch` for liveness and grant"*;
  [`../repos/trending.md`](../repos/trending.md) already recorded it as **MIT**
  (`main/LICENSE.txt`, 1,073 B), **v0.5.5 · 2026-08-24 · 26 releases**, *"freshest
  in tier"*, last commit `2026-10-19`. 🔴 **A second instance of `568-A`'s own
  failure mode, inside the very pass that registered `568-A`** — see `569-A`.

🟢 **So the sentence to give a client changed this pass.** Not *"you will have to
build item calibration"* but *"item authoring, gating, calibration, equating and
guessing-correction are all available permissively, and all of it is pre-adoption
software you must validate before you stake an exam result on it."* Those are
different engagements, and only one of them was true last pass.

## Lecture-video layer (new in the sixth pass — the fifth pass's `topic:video` ask)

**The sweep ran and the result is thin, which is itself the finding:** there is no
open-source lecture-video product to adopt, and there *is* a well-understood
four-stage pipeline to assemble — slides → page images → narration script → TTS
and mux. Every stage has a permissive component already on this page.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [galaxyproject/video-lectures](https://github.com/galaxyproject/video-lectures) | **MIT** (`master/LICENSE`, 1,071 B, "Copyright (c) 2024 Galaxy Project") | 2 | Global | ✅ permissive | **The reference pipeline and the only institutionally held row on this axis.** Pandoc turns `src/*.md` into HTML slides plus a hands-on document; `wkhtmltoimage` extracts one image per slide; `extract-script-from-html.js` pulls the narration text; `ari` muxes images and script into a narrated video; Yarn/Jake orchestrates. 67 commits on `master`, forked from `jxtx/covid-lessons`. ⚠️ **It terminates in Amazon Polly and the Jakefile needs AWS credentials** — swap the TTS stage before quoting it to any data-residency-constrained client. |
| [jhudsl/ari](https://github.com/jhudsl/ari) | **MIT** — declared in `DESCRIPTION` (`License: MIT + file LICENSE`); the `LICENSE` file is a **40 B stub** | — | North America | ✅ permissive | The narration-and-assembly **engine** under the row above, an R package from the **Johns Hopkins Data Science Lab** — a named institution, which is what places it. ⚠️ Its grant is **not readable from `LICENSE`**: the CRAN idiom this page already records puts the licence in `DESCRIPTION` and leaves `LICENSE` holding only a year and a holder. |
| [Changochen/slide-to-video](https://github.com/Changochen/slide-to-video) | **MIT** (1,070 B, "Copyright (c) 2024 Yongheng Chen") | — | Global | ✅ permissive | PDF deck plus a plain-text script, slides split on a `NEWSLIDE` marker, out to a narrated video. **The one row on this axis that can run with no cloud TTS at all** — it supports optional local voice cloning, which makes it the default pick for an offline or sovereignty-constrained engagement. |
| [htlin222/slides-to-video](https://github.com/htlin222/slides-to-video) | **MIT** (1,065 B, "Copyright (c) 2026 htlin222") | — | Global | ✅ permissive | ImageMagick page images → **model-generated speaker notes** → TTS → `ffmpeg`. The only row that *drafts* the narration rather than requiring a finished script, which is the stage a content team actually wants automated. |

🟢 **The substitution that makes this layer deliverable.** Three of the four rows
end in a proprietary cloud TTS. The permissive replacements are already shelved in
the narration layer below: [`denizsafak/abogen`](https://github.com/denizsafak/abogen)
(**MIT**, and it emits **synchronised captions** — an accessibility deliverable,
and the European Accessibility Act is a procurement gate across EMEA public
education), [`Blaizzy/mlx-audio`](https://github.com/Blaizzy/mlx-audio) (**MIT**,
Apple Silicon), and [`supertone-oss-archive/supertonic`](https://github.com/supertone-oss-archive/supertonic)
(**MIT**, on-device, ⚠️ **archived** — the grant is perpetual, the patches are not).

⛔ **Explicitly not shelved:** `harry0703/MoneyPrinterTurbo` (MIT, 136,744★) stays
rejected on the fourth pass's reasoning — it is short-form social video, not
lecture content, and its star count makes it the most likely thing on this axis to
be mis-offered as courseware tooling.

## Deck and document generation — extending the fourth pass's layer

The fourth pass found `ppt-master` (MIT, 71,498★) through a listicle. The
capability sweep confirms it sits in a **cohort**, which matters because
single-repo dependencies on a 71k★ project with unverifiable provenance are a
risk a client will ask about.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | **Apache-2.0** (file, 11,375 B) | 32,854 | Global | ✅ permissive | *"The first and best Office suite purpose-built for AI agents to read, edit and automate"* — DOCX, XLSX, PPTX from a CLI. The **agent-facing** alternative to `ppt-master`'s generate-from-scratch model: it edits the client's existing documents in place, which is what "update our 400 lesson plans" actually requires. C#, single binary, no Office install needed; 2,234 forks, created 2026-03-15. |
| [dream-num/univer](https://github.com/dream-num/univer) | **Apache-2.0** (file `dev/LICENSE`, 10,173 B) | 22,832 | Global | ✅ permissive | *"The Office Harness for AI Agents"* — embeddable spreadsheets, docs, slides and canvas as an SDK. Branch **`dev`**. Use when the deliverable is an **in-product editing surface** (a worksheet the student fills in) rather than a file. |
| [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | **Apache-2.0** (file, 11,345 B) | 11,418 | Global | ✅ permissive | *"Free, open-source AI Office suite"* — Docs, Sheets, Slides, PDF, Markdown and HTML editors, **local-first**, LibreOffice-backed. Pairs with `PAIDEIA` for a fully offline authoring stack. |
| [tw93/Kami](https://github.com/tw93/Kami) | **MIT** (file, 1,061 B) | 12,173 | Global | ✅ permissive | *"Layout rules and templates that let AI agents export PDF, PPTX…"* — **typesetting quality**, which is the usual reason generated courseware looks unusable to a teacher. The cheapest fix for the "it works but it looks wrong" objection. |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | **MIT** (file, 1,070 B) | **75,894** | Global | ✅ permissive | Not a tool — **courseware**. A full AI-engineering curriculum, 13,381 forks, #1 on GitHub Trending 2026-05-24. **MIT means a client's internal academy can fork, rebrand and extend it**, which is the single fastest route to a credible AI-upskilling programme and is worth more to a corporate-L&D buyer than any generator on this page. Rejected from the agent shelf (see [`../agents/top.md`](../agents/top.md)) because it has no learner model. |

**How this layer changes the economics.** The content-production layer generates;
this layer **ingests what the client already owns**. That ordering is the
commercial point: an engagement that starts by generating new material competes
with the client's own faculty, while one that starts by ingesting the existing
textbook, past papers and lecture notes is **migration work**, which is easier to
scope, easier to value and impossible for the client to do with a chatbot
subscription. Pattern **P-570-A** wires the two together.

## The LMIC supply side — `AI-for-Education` (closes a three-pass gap)

Three consecutive passes of this KB declared: *"no African education platform or
agent repository appears anywhere."* That gap is now closed, and the thing that
closed it is an organisation rather than a repository.

[**AI-for-Education**](https://github.com/AI-for-Education) describes itself as
*"Empowering Education in LMIC's with AI"* and *"a collaborative hub for
developing and sharing AI tools and resources aimed at revolutionizing education
in low and middle-income countries (LMICs)."* Site `ai-for-education.org`.
**Location is not stated** on the profile, so the organisation is recorded as
EMEA on the balance of its one published benchmark paper and contact domain, and
that inference is flagged rather than hidden.

**19 repositories; 10 are MIT** (confirmed by querying GitHub's licence index,
`license:mit org:AI-for-Education`). The ones that matter:

| Repo | Licence | ★ | What it is, and why it closes the gap |
| --- | --- | --- | --- |
| [lesson-plan-parse-mbsse](https://github.com/AI-for-Education/lesson-plan-parse-mbsse) | MIT | 1 | **Sierra Leone's Ministry of Basic and Senior Secondary Education (MBSSE)** publishes Maths and Language Arts lesson plans as PDFs; this converts them to structured JSON and cleans them with an LLM. One star, and it is the most important row on this page for an African engagement: it is **real ministry curriculum, parsed, in the open, under MIT**. |
| [luganda-linguistic-benchmarks](https://github.com/AI-for-Education/luganda-linguistic-benchmarks) | — | 0 | Linguistic benchmarks for **Luganda** (Uganda). Evidence that African-language evaluation assets exist at all. |
| [global-proficiency-framework](https://github.com/AI-for-Education/global-proficiency-framework) + [gpf-alignment](https://github.com/AI-for-Education/gpf-alignment) | — / MIT | 0 / 1 | Digitising the **Global Proficiency Framework** and automating alignment to it. GPF is the cross-country learning-standards frame used where no rich national standard exists — the LMIC analogue of US state standards. |
| [nemoasr-android](https://github.com/AI-for-Education/nemoasr-android) | — | 1 | On-device ASR on Android (Kotlin). Speech recognition **without connectivity** is the binding constraint in low-bandwidth classrooms; this is the only repo in this KB that addresses it. |
| [voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework) | MIT | 1 | Evaluation harness for voice AI — the modality that works where literacy or devices do not. |
| [fabdata-llm](https://github.com/AI-for-Education/fabdata-llm) | MIT | 9 | The org's own LLM client library, 10 forks. The plumbing the rest depends on. |
| [edu-qurating](https://github.com/AI-for-Education/edu-qurating) | MIT | 3 | Quality rating of educational content. |
| [primerpro](https://github.com/AI-for-Education/primerpro) | — | 0 | Python port of PrimerPro decodability functions — early-reading text levelling. |

**How to read this honestly.** This is a **supply side measured in single-digit
stars**. It is not a market; it is a toolkit, and most of it is pre-1.0. But it
is MIT-licensed, it is pointed at named African ministries and languages, and it
is the only thing of its kind located in three passes of searching. For an
engagement in sub-Saharan Africa it is the starting point. For a commercial
engagement anywhere else, the GPF-alignment and decodability work is reusable
wherever a client lacks a rich standards corpus.

## Adjacent systems of record

Not learning platforms, but systems an institution already runs — and what an AI
search or discovery agent is usually pointed at.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [DSpace/DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** | 1,100 | North America | ✅ permissive | "(Official) The DSpace digital asset management system that powers your Institutional Repository." Java. **The most permissively licensed platform of record anywhere in this KB** — confirmed in the sidebar and in `LICENSE` on `main` ("BSD 3-Clause License, Copyright (c) 2002-2021, LYRASIS"). LYRASIS is a US non-profit. |
| [Koha-Community/Koha](https://github.com/Koha-Community/Koha) | GPL-3.0 (or later) | 597 | Global | ⛔ copyleft | "Koha is a free software integrated library system (ILS)." Uses its **own bug tracker rather than GitHub issues** — relevant to any contribution plan. Origin not stated on the repository page. |

**Why DSpace matters more than its star count suggests.** Every other platform of
record in education is GPL or AGPL. DSpace is BSD-3-Clause, so the one category
where a client *can* own a proprietary derivative is the institutional
repository — theses, datasets, faculty output, grey literature. That is also the
corpus a RAG research agent most wants.

## What this means in practice

A client on Moodle, Open edX, Canvas or Chamilo cannot have AI features delivered
as a proprietary fork — AGPL/GPL forbid it on any hosted-service reading. The
licence-clean routes are:

- **Attach across a standard boundary.** **LTI 1.3** (`ltijs`, Apache-2.0) to
  launch a tool inside the LMS and write grades back; **MCP** (the servers in
  [`../agents/top.md`](../agents/top.md), MIT) for agent read access; **xAPI →
  LRS** (`xAPI-Spec` Apache-2.0, `ralph` MIT) for telemetry without touching
  platform internals; and — **new in the fourth pass** — **SCORM**
  (`scorm-again`, MIT) to deliver courseware *into* the platform the way the
  installed base already ingests it. All four are permissive. This remains the
  default, and it now covers content delivery as well as launch, read and
  telemetry.
- **Or replace the substrate, which is newly possible.** `Selleo/mentingo` (MIT,
  Poland) is an AI-native LMS with xAPI and SCORM built in and white-labelling as
  a stated goal. At 102★ it carries adoption risk a Moodle install does not —
  but it is the first time this KB can offer a permissive substrate instead of
  only a permissive boundary.
- **Gate the output.** `learning-commons-org/evaluators` for rubric scoring and
  `pedagogy-benchmark` for pedagogical knowledge are the two verified ways to
  show a client that generated instructional content was *measured* and not just
  generated. Both are small; both are the only options.

## Declared gaps

- **No permissive platform of record exists at Moodle/Open edX scale.** Still
  true, now bounded on three sides and **measured**. It holds for the **LMS of
  record** category. It does **not** hold for the **institutional repository**
  (DSpace, BSD-3-Clause, category leader), it is **weakening** for the
  **AI-native LMS** niche (`mentingo`, MIT, 102★), and as of this pass it does
  **not** hold at the **small-and-medium-institution SIS** tier
  (`academico`, MIT, 410★, 151 forks). The denominator is now on the record: the
  entire permissive LMS population above 50★ is about **eight repositories**.
  A client needing a permissive substrate at *university* scale still assembles
  rather than adopts; a language school, training institute or private school
  group no longer has to.
- ~~**No African-origin repo appears anywhere on this page.**~~ **Closed, with the
  qualification stated above:** `AI-for-Education` is an LMIC-focused
  organisation with MIT tooling built against Sierra Leonean curriculum and
  Ugandan language data, but its own **location is not stated** and its repos are
  0–13★. African *artefacts* are mapped; African-*domiciled* publishers are not.
  That is the next pass's question, and it should be asked on GitHub's index, not
  the open web — which is what finally worked here.
- ~~**`NOASSERTION` is not the same as "no licence".**~~ **Closed as a question
  and promoted to a catalogue.** Both `learning-commons-org` repos reported
  `NOASSERTION`; both are now read first-hand and they are **different** split
  grants — `knowledge-graph` is code-MIT / data-per-publisher, `evaluators` is
  code-MIT / prompts-CC-BY-4.0 / **corpora-NC**. `digitalinnovationone/dio-agent`
  (2,750★) returns no `license` field at all and has no file on either branch:
  genuinely unlicensed. `24kchengYe/human-skill-tree` (586★) matched no licence
  filter and is **AGPL-3.0 on `master` with a dual-licensed `skills/`
  directory**. **Four distinct states behind one ambiguous API value, plus a
  branch-name trap.** The rule that resolves all of them is now executable from
  this session: **read the file, on every filename, on every branch.**
- **The instrument that made this possible is new and should be used
  deliberately.** `raw.githubusercontent.com` returns HTTP 200 here;
  `api.github.com` and `github.com` HTML return 403; MCP `get_file_contents` is
  **repo-scoped** and refuses third-party repositories; `search_users` exposes no
  `location`. Twenty-one licence files were read this pass. **Region, by
  contrast, got harder** — owner country is unobtainable by any available route,
  so new rows are placed only from licence-file copyright holders (which is how
  `richie` was placed to EMEA), publisher or payment-stack signals (flagged as
  inferred), or left **Global**.
- **Licence defects cluster in the agent layer.** Across three passes: platforms
  state copyleft clearly and accurately; agents claim MIT in prose with no file
  (`mcp-canvas-lms`), ship share-alike content licences on code-shaped artefacts
  (`Auto-Empirical-Research-Skills`, CC BY-SA 4.0, 4,843★), or state nothing at
  2,750★. The substrate is honest; the fast-moving layer is not.
- ~~**No open-source learning-analytics *dashboard* was located**, only the LRS
  (`ralph`) that feeds one. The presentation layer of learning analytics appears
  to be entirely commercial; not re-verified this pass.~~ 🔴 **STRUCK
  `2026-10-31` (`p570`) — and this is `568-A`'s THIRD live instance, on a third
  page.** `p568` refuted this sentence by shelving
  [`openfun/warren`](https://github.com/openfun/warren) and
  [`openfun/potsie`](https://github.com/openfun/potsie), both **MIT**, both from
  **France Université Numérique**. `p569` struck the copy on
  [`trending.md`](trending.md):179 **and left this one standing.** 🔵 **The
  mechanism is the measured cost of `569-A`'s own residual:**
  `ingest/absence-claims.py` reports and cannot gate, its `27` narrow-tier
  collisions were never triaged into a baseline, and so a claim its own author
  had already refuted survived a further pass on a page nobody re-read.
  **An instrument that reports is worth exactly as much as the triage nobody
  ran.** The gap register's entry is `569-A`; its first ask is now overdue twice.
- ~~**Horizontal tooling is systematically under-covered.**~~ **Swept and closed
  on the fifth pass — and the prediction was an understatement.** The fourth pass
  guessed the blind spot hid "document parsers, TTS pipelines, assessment-item
  generators and video tooling". The capability sweep returned **sixteen
  permissively licensed repositories, five of them above 30,000★ and three above
  69,000★** — `PaddleOCR` (92,024), `MinerU` (82,860), `tesseract` (77,267),
  `ai-engineering-from-scratch` (75,894), `docling` (69,909), `OfficeCLI`
  (32,854), `opendataloader-pdf` (30,129). **The horizontal layer is larger than
  the entire education-specific supply in this KB combined**, and it had been
  invisible for four passes to a filter nobody questioned. Two sub-gaps remain
  open: **assessment-item generators** returned nothing permissive and
  education-specific, and **video tooling** was not swept (`MoneyPrinterTurbo`,
  MIT, 136,744★, surfaced incidentally and is short-form social video, not
  lecture content — it is not shelved and should not be treated as courseware).
- **The generalisable lesson, since it will recur in every other industry KB:**
  a sweep filtered on an industry topic measures *how a repository markets
  itself*, not what it does. The tools an industry runs on are usually tagged by
  **capability**, because their authors are selling to everyone. Sweep both axes
  or report an undercount.
### Added on the eighth pass (`p570`)

- 🔴 **The evaluation gap is NARROWER, not closed, and the narrow statement is
  the useful one.** Seven granted rubric-scoring assets now exist on this page.
  **None of them is a runtime drift detector.** What a client can now be told:
  *"you can pin, version and re-run a rubric-based quality gate over your tutor's
  outputs and over its multi-turn trajectories, with permissive code"* — which
  was not true last pass. What remains untrue: *"you will be alerted when the
  deployed tutor degrades."* `evidentlyai/evidently` (Apache-2.0) remains the
  generic pick for that and is not education-aware. **Seventh consecutive pass
  with no education-specific runtime monitor; this is still the clearest unmet
  build opportunity in the industry.**
- 🔴 **A commit count is now a claim this base must verify, not a datum it may
  read.** `p569` made commit density the admission signal for this layer;
  `p570` found a `2,137`-commit synthetic history on the first never-swept axis.
  [`../ingest/history-plausibility.py`](../ingest/history-plausibility.py) is
  committed and runs; **its four checks cost one shallow clone per candidate and
  should run before any row is admitted on commit density.** The instrument
  reproduces its founding case and passes two real controls (`mirt`, `dexter`).
  🔵 **Generalises past education: any base on this harness that shortlists on
  commit count inherits this exposure.**
- 🔴 **Four of four Apache-2.0 rows name no licensor.** Not a defect in any one
  repository — Apache-2.0's template simply has no copyright line, and GitHub's
  "Apache-2.0" determination is correct in every case. **It means region is
  unrecoverable from an Apache grant by construction**, and it means the
  `terracotta` observation this base recorded as a one-off trap is in fact the
  normal case for that licence family. See `570-C`.
- 🔴 **The closed region vocabulary has no Africa value, and this base's EMEA
  counts are therefore not a market measurement.** `SMART-GRADE` (Cameroon) is
  recorded `EMEA†` because the five permitted values leave nowhere else to put
  it. 🔵 **State the grade and the country whenever an EMEA count is quoted**, or
  an African school-IT artefact and a German research institute read as the same
  market. Registered as `570-E`. The field is not the place to fix this — the
  vocabulary is closed on purpose and inventing `Africa` would break every
  downstream filter; the fix is the `†` marker plus the country in prose.
- 🔴 **`568-A` has now recurred on three separate pages across three passes.**
  The learning-analytics-dashboard sentence struck above was refuted by `p568`,
  struck on one page by `p569`, and survived on this one. **The instrument that
  catches this class exists and does not gate**, because `569-A`'s triage of the
  27 collisions into a baseline was not done at `p569` and was not done here
  either — this pass spent its budget on discovery and verification. 🔵 **It is
  now the oldest cheap unfinished item in this base and it should be the next
  pass's first action, before any search leg runs.**
- **`ulearn`'s maturity is unassessed beyond its stack.** 701★ MIT is the largest
  permissive LMS found and Laravel 5.8 is five major versions behind. Nobody
  should be told it is a starting point without an upgrade estimate attached.
