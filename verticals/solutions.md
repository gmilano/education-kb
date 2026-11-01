---
industry: education
region: Global
updated: 2026-11-01
---

## 🆕 p592 — 2026-11-01 — this page's standing advice is no longer argued from examples: every platform of record on this shelf was re-measured, and the licence split is structural

### 🟢 The measurement, stated before the conclusion

`gh api -X GET search/repositories`, `2026-11-01`, **`192 of 192`** curated addresses across
[`../agents/top.md`](../agents/top.md) and [`../repos/foundations.md`](../repos/foundations.md)
— the first full-shelf sweep in this base. The composition census is on
[`../repos/trending.md`](../repos/trending.md); what this page needs from it is the
**platform tier**, re-measured row by row.

| platform of record | licence, measured | stars | last push | forkable by a studio? |
|---|---|--:|---|---|
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 🔴 `LGPL-3.0` | **`9,262`** | `2026-10-30` | 🔴 no — integrate |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 `AGPL-3.0` | **`8,214`** | `2026-11-01` | 🔴 no — integrate |
| [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | 🔴 `GPL-3.0` | **`7,814`** | `2026-10-30` | 🔴 no — integrate |
| [moodle/moodle](https://github.com/moodle/moodle) | 🔴 `GPL-3.0` | **`7,569`** | `2026-10-30` | 🔴 no — integrate |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 `AGPL-3.0` | **`3,361`** | `2026-10-30` | 🔴 no — integrate |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 `AGPL-3.0` | **`2,440`** | `2026-11-01` | 🔴 no — integrate |
| [classroomio/classroomio](https://github.com/classroomio/classroomio) | 🔴 `AGPL-3.0` | **`1,736`** | `2026-11-01` | 🔴 no — integrate |
| [codelitdev/courselit](https://github.com/codelitdev/courselit) | 🔴 `AGPL-3.0` | **`1,292`** | `2026-11-01` | 🔴 no — integrate |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`** | **`1,240`** | `2026-10-30` | 🟢 **yes** — Apache-derived, no share-alike |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 `AGPL-3.0` | **`1,131`** | `2026-10-29` | 🔴 no — but it is the *supported* way to operate Open edX |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 `GPL-3.0` | **`1,019`** | `2026-11-01` | 🔴 no — integrate |
| [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | 🟢 **`MIT`** (text) | **`981`** | 🔴 `2025-12-09` | 🟡 **yes, but** ~11 months stale |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 `GPL-2.0` | **`649`** | `2026-10-28` | 🔴 no — integrate |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 `GPL-3.0` | **`507`** | `2026-10-31` | 🔴 no — integrate |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** | **`103`** | `2026-11-01` | 🟢 yes — but small |

### 🟢 The conclusion this page can now assert rather than illustrate

🔵 **The platform tier is copyleft and the agent tier is permissive, and that is not a
coincidence of sampling — it is `192 of 192`.** `MIT` alone accounts for **`100`** rows of
the whole shelf and the permissive subtotal is **`130`** (`67.7 %`), yet **not one** of the
four largest platforms of record carries a permissive licence.

🟢 **So the build-vs-integrate rule is settled, and it is a licence rule before it is an
architecture rule:**

- 🟢 **Integrate, never fork**, at the platform layer — over **LTI 1.3**
  ([`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs), `Apache-2.0`, `373★`), **xAPI**,
  **SCORM**, or an MCP server against the LMS API
  ([`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp), `MIT`, `310★`).
  🔵 The seam keeps studio code permissive because it never links into the GPL/AGPL work.
- 🟡 **Fork only Sakai**, if a fork is genuinely required. `ECL-2.0` is the only permissive
  licence at institution scale on this shelf. 🔴 Weigh it honestly: Sakai is `1,240★` against
  Moodle's `7,569★` and Open edX's `8,214★`, so a fork buys licence freedom at a real cost in
  ecosystem, plugins and client familiarity.
- 🔴 **Do not propose `pupilfirst` as a default.** It is genuinely `MIT` (by text — the API
  reports `NOASSERTION` and hides it), but it has not been pushed since **`2025-12-09`**.
  Adopt it deliberately, with a maintenance position stated in the proposal, or not at all.
- 🔴 **Do not promise a proctoring platform.** `SafeExamBrowser` is `MPL-2.0` and current
  (`361★`, `2026-10-30`); `Proctoring-AI` is a stale component. Gap `585-B`/`585-G` is still
  open: a studio ships SEB plus an agent.

🔵 **Three archived rows remain on this page's wider tier lists and all three stay flagged**
rather than deleted, because an archived repo is still the answer to *"why are we building
this?"*: `adlnet/SCORM-to-xAPI-Wrapper` (unlicensed **and** archived, last push `2017-10-02`,
published by the body that authored SCORM), `raccoongang/edx_xblock_scorm` (`Apache-2.0`,
archived, `2023-05-26`), and `kantord/LibreLingo` (`AGPL-3.0`, archived). 🟢 **`3 of 3` were
already correctly marked before this pass** — the full sweep found **`0`** unflagged defects
anywhere on the curated shelves.

---

## 🆕 p591 — 2026-11-01 — the systems-of-record question this page has never answered: the permissive ERP/CRM tier is `24,087★` large and none of it is education-specific, while every education-specific ERP is copyleft — plus a mandated-leg licence claim that is false

### 🔴 The claim this page must not repeat

🔵 **The mandated vertical leg** (`open source platform education ERP CRM MIT Apache`) ran
in full this pass. 🔴 **It asserted that iDURAR ERP/CRM is *"fully open-source under the MIT
license"*.** Byte-read `2026-11-01`:
[`idurar/idurar-erp-crm`](https://github.com/idurar/idurar-erp-crm) carries a `34,230`-byte
**GNU AFFERO GENERAL PUBLIC LICENSE** and the GitHub API agrees. 🔵 **Recorded here because
this is the page a scope estimate is built from**, and a permissive ERP that is actually
network copyleft changes a delivery model, not a footnote.

### 🟢 The tier, measured — every grant title-anchored per `591-A`

| Platform / component | Licence | Stars | Last push | Region | Customisable with AI on top? |
|---|---|--:|---|---|---|
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | 🟢 **MIT (text, 1,078 B)** | **24,087** | `2026-11-01` | APAC | 🟢 **Yes — and this is the recommendation when the client wants admissions and enquiry management.** Laravel/PHP CRM, permissive, pushed the day of measurement. An AI layer attaches as a Laravel package: lead scoring, enquiry triage, applicant Q&A. 🔵 Default branch `master`. |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0 (text, 11,906 B)** | **1,148** | `2026-11-01` | Global | 🟢 **Yes, and it is the governance-safe choice.** ASF top-level project; accounting, HR, manufacturing, CRM. 🔵 Pick this when the client's procurement cares more about foundation governance than about velocity. Java. |
| [cortezaproject/corteza](https://github.com/cortezaproject/corteza) | 🟢 **Apache-2.0 (text, 11,358 B)** | **2,183** | `2026-10-20` | EMEA | 🟢 **Yes — the low-code option.** Go-based CRM/application platform. 🔵 The permissive analogue of the Odoo-module pattern `openeducat` uses: model the education domain as Corteza modules instead of forking an LMS. |
| [marmelab/atomic-crm](https://github.com/marmelab/atomic-crm) | 🟢 **MIT (text, 1,105 B)** | **1,420** | `2026-10-30` | EMEA | 🟢 **Yes — the fastest start.** React/TypeScript on Supabase. 🔵 Use when the deliverable is a bespoke student-lifecycle CRM the studio owns outright, not a configured product. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0 (text)** | **903** | `2026-10-29` | APAC | 🟡 **Yes, from the outside.** The education ERP — admissions, fees, attendance, library, exams. 🟢 **LGPL-3.0 is the friendliest copyleft on this page:** a *separate* AI module that calls its API keeps its own licence. 🔴 Edits to its own files carry back. 🔵 Default branch `19.0`. |
| [frappe/education](https://github.com/frappe/education) | 🔴 **GPL-3.0 (text)** | **688** | `2026-10-30` | APAC | 🔴 **Attach over the API only.** School ERP on Frappe. |
| [idurar/idurar-erp-crm](https://github.com/idurar/idurar-erp-crm) | 🔴 **AGPL-3.0 (text, 34,230 B)** | **8,931** | 🟡 `2026-08-14` | Global | 🔴 **No.** 🔴 The leg claimed MIT; it is network copyleft. See above. |
| [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | 🔴 **GPL-3.0 (text, 35,151 B at `COPYING`)** | **7,814** | `2026-11-01` | EMEA | 🔴 **Attach, do not fork.** Broad module coverage, strong francophone and LATAM install base — so it is the system a LATAM client may already be running. |
| [idempiere/idempiere](https://github.com/idempiere/idempiere) | 🔴 **GPL-2.0 (text, 15,057 B)** | **675** | `2026-10-30` | Global | 🔴 **Attach, do not fork.** 🔵 API said `NOASSERTION`; its `LICENSE.md` opens with `<center>` — HTML-wrapped (`591-B`). |

### 🟢 The build-vs-buy answer, in one paragraph

🔵 **The education-specific ERP tier is copyleft without exception** — `openeducat_erp`
(LGPL-3.0) and `frappe/education` (GPL-3.0) are the only two, and this page has now
confirmed there is no permissive education ERP at any size. 🟢 **So there are exactly two
honest delivery models.** (1) **Attach**: take the client's existing education ERP as the
system of record and build the AI as a *separate* service over its API — lawful under
LGPL-3.0 and the only option under GPL-3.0/AGPL-3.0, and it is what
[`erseco/python-moodle`](https://github.com/erseco/python-moodle) does for the LMS tier.
(2) **Build the domain**: start from `krayin`, `corteza`, `atomic-crm` or
`ofbiz-framework` — all permissive, all pushed within two weeks of measurement — and model
admissions/fees/attendance yourself, which the studio then owns. 🔴 **What is not available
is the middle path**: forking a ready education ERP and shipping it as a proprietary
product. Nobody licenses that.

### 🔵 The customise-with-AI-on-top set, restated with this pass's additions

🟢 The pattern this page exists to document — **real systems that take AI on top** — now
reads, by tier:

| Tier | Buy / adopt | Grant | Attach AI how |
|---|---|---|---|
| LMS of record | **Moodle** (GPL-3.0), **Open edX** (AGPL-3.0) | 🔴 copyleft | Over the API — [`erseco/python-moodle`](https://github.com/erseco/python-moodle) (MIT) or [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) as an LTI 1.3 tool |
| LMS, **forkable** | **Sakai** (ECL-2.0), **OpenOLAT** (Apache-2.0), **Kolibri** (MIT, offline-first) | 🟢 permissive | Fork and embed directly |
| Student-lifecycle CRM | 🆕 **krayin** (MIT), 🆕 **atomic-crm** (MIT), 🆕 **corteza** (Apache-2.0) | 🟢 permissive | Build the education domain on top |
| Education ERP | **openeducat_erp** (LGPL-3.0), **frappe/education** (GPL-3.0) | 🔴 copyleft | Separate module over the API |
| Courseware emit | **LiaScript-Exporter** (BSD-3-Clause), **scorm-again** (MIT), **Numbas** (Apache-2.0) | 🟢 permissive | See `P-590-A` |
| Assessment review | **idstack** (MIT), 🆕 **blind-review-skill** (MIT) | 🟢 permissive | Gate before ship |
| 🆕 Figures for STEM courseware | 🆕 **geometry-dsl** (MIT) | 🟢 permissive | Compile the diagram instead of generating it |

---

## 🆕 p590 — 2026-11-01 — the delivery tier's build-vs-buy answer is rewritten: `p589` told a client to buy one dependency and build the generator, and there are at least six permissive generators — plus the first measured instrument for telling an ecosystem from a single supplier

### 🔴 What this page's sibling got wrong, and why a vertical page has to care

🔵 **The commercial question this tier answers** is *"do we build the courseware generator
or buy it?"* 🔴 **`p589` answered "build it": buy `scorm-again`, add `scorm-h5p-wrapper`,
build the generator, depend on nothing else.** Re-walked `2026-11-01` that is wrong, and
the correction changes a scope estimate rather than a footnote.

| Platform / component | Licence | Stars | Last push | Region | Customisable with AI on top? |
|---|---|--:|---|---|---|
| [LiaScript/LiaScript-Exporter](https://github.com/LiaScript/LiaScript-Exporter) | 🟢 **BSD-3-Clause** | **29** | `2026-10-30` | EMEA | 🟢 **Yes — and it removes most of the generator.** One Markdown-shaped source exports to **SCORM 1.2, SCORM 2004, IMS, xAPI, H5P, PDF, ePub and Web**, with presets for Moodle, ILIAS and OPAL. 🔵 README read first-hand. The AI layer authors the LiaScript source; the exporter handles every target format. |
| [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 Apache-2.0 | **216** | `2026-10-28` | EMEA | 🟢 **Yes.** Newcastle University's browser-based assessment engine, with its own `23,811`-byte SCORM storage runtime. 🔵 The buy answer whenever the deliverable is assessment rather than narrative courseware. |
| [erseco/python-moodle](https://github.com/erseco/python-moodle) | 🟢 **MIT (text, 1,071 B)** | **10** | `2026-10-22` | EMEA | 🟢 **Yes — and it is the attach-over-API handle for the AGPL LMS of record.** Pythonic CLI and library that drives a Moodle instance over web sessions. 🔵 Exactly `573-B`'s rule made concrete: **automate the client's Moodle, do not fork it.** |
| [kemalyy/edumints-scorm-mcp](https://github.com/kemalyy/edumints-scorm-mcp) | 🟢 **MIT (text, 1,069 B)** | **9** | `2026-10-14` | Global | 🟢 **Yes.** Self-hostable MCP server that assembles SCORM-compliant courses — the emit step as agent tools. |
| [Didask/scol-r](https://github.com/Didask/scol-r) | 🟢 **MIT (text, 1,063 B)** | **15** | `2026-10-27` | EMEA | 🟡 **Yes, with a caveat.** Shareable Cross-Origin Learning Resources, a SCORM successor from a French vendor. 🔵 Permissive and live, but a client LMS that only ingests SCORM will not take it — offer it as the modern path, not the compatible one. |

🟢 **The corrected answer to give a client:** buy `scorm-again` for the runtime, **buy
`LiaScript-Exporter` if the source is Markdown-shaped courseware**, buy `Numbas` if the
deliverable is assessment, add `scorm-h5p-wrapper` for H5P sources and the two MCP servers
if the pipeline is agent-driven — **and build the generator only after those five are ruled
out.** 🔴 `p589`'s answer put a generator build in every courseware scope; this one does not.

### 🆕 The procurement instrument this page did not have: distinct owners

🔴 **A liveness count cannot tell an ecosystem from one prolific publisher, and this page
has only ever published liveness.** Measured across the three interchange axes
`2026-11-01`:

| axis | live permissive repos | 🆕 distinct owners | 🆕 live ÷ owners | verdict for a procurement decision |
|---|--:|--:|--:|---|
| `topic:scorm` | `42` | 🟢 `39` | 🟢 `1.08` | 🟢 Real ecosystem — a dead dependency can be swapped |
| `topic:xapi` | `35` | 🟢 `27` | 🟢 `1.30` | 🟢 Real ecosystem — buy the client library, do not write one |
| `topic:qti` | `14` | 🔴 **`7`** | 🔴 **`2.00`** | 🔴 **One supplier.** `8 of 14` are `metyatech`, all pushed in one six-day window, none above `2★` |

🔵 **So for a QTI engagement the honest advice is:** treat the `metyatech` set as **one
supplier, not eight options**; stand on `feyst/qti3-validator` or `Citolab/qti-playground`
if a third-party dependency is required; otherwise **speak QTI 3.0 directly** — the schemas
are published by 1EdTech and the XML is tractable — and carry the maintenance yourself
knowingly. 🟢 Full measurement on [`../repos/trending.md`](../repos/trending.md); the trend
is `Trend 42`.

### 🟢 `573-B` restated, because this page is where it is load-bearing

🔵 **`573-B` (registered by `p573`, and until `p590` it was cited here without ever being
registered in the gap register):** *there is no permissively licensed, university-scale
open-source SIS; the one MIT option (`academico`) is scoped to "small and medium
institutions"; therefore a registrar-scale SIS engagement attaches to the client's existing
system over its API — it does not fork one.* 🟢 **Unchanged this pass, and
`erseco/python-moodle` is the first row on this page that implements the rule for the LMS
tier as well as asserting it for the SIS tier.**

---


## p589 — 2026-11-01 — the courseware *delivery* tier, measured: every engagement that hands material to a client's existing LMS is an EMIT job, and the emit tier has exactly two live permissive dependencies out of `235` repositories

### 🔴 The tier this page never named, and why it matters commercially

Every tier on this page below is about the platform a client **runs**. 🔵 **This one is about
the format a client's platform **accepts** — and it is the tier most engagements actually
touch**, because a studio is far more often asked to put courseware *into* Moodle, Open edX
or Canvas than to replace them.

🟢 **The format is SCORM** (1.2 and 2004) and it is a published ADL specification.
🔴 **Its open-source tooling is dead.** Measured `2026-11-01`, `topic:scorm` walked to
exhaustion — `235` repositories, full table on
[`../repos/foundations.md`](../repos/foundations.md):

| what a studio needs | what exists | verdict |
|---|---|---|
| a SCORM **runtime** (the API a package talks to) | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) — MIT, `362★`, pushed `2026-10-28` | 🟢 **adopt — the one safe dependency on the axis** |
| an **authoring source format** → SCORM | [`sr258/scorm-h5p-wrapper`](https://github.com/sr258/scorm-h5p-wrapper) — MIT, `58★`, pushed `2026-10-29` | 🟢 **adopt if the source is H5P** |
| a **React** front end for SCORM content | [`S4-NetQuest/react-scorm-provider`](https://github.com/S4-NetQuest/react-scorm-provider) — MIT, `67★` | 🔴 **build it** — last push `2023-01-06` |
| an **Open edX** SCORM block | [`raccoongang/edx_xblock_scorm`](https://github.com/raccoongang/edx_xblock_scorm) — Apache-2.0 | 🔴 **build it** — `archived: true` |
| a SCORM → **xAPI** bridge | [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) — `99★` | 🔴 **build it** — **unlicensed and archived, last push `2017`, and ADL authored SCORM** |
| a courseware **authoring toolkit** | [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) — `632★` | 🔴 **reference only** — GPL-3.0 |
| a SCORM **content API** | [`cybercussion/SCOBot`](https://github.com/cybercussion/SCOBot) — `165★`, live | 🔴 **do not vendor** — **CC BY-SA 4.0**, reciprocal, no patent grant |

### 🔵 The customisation rule for this tier, stated the way the other tiers are

🟢 **Buy the runtime, build the generator.** 🔴 **`56.6 %` of the axis (`133 of 235`) carries no
licence at all**, so "adopt an open-source SCORM stack" is not a sentence a proposal may
contain. 🔵 **The defensible position** — and it is a *better* commercial position than
adopting, because the generator is the billable artefact:

> *"We depend on one MIT library for the runtime contract, we generate the packages, and the
> packages open in the LMS you already own. Nothing we ship carries a copyleft or
> ShareAlike obligation."*

🟢 **This composes cleanly with the platform tiers above:** the client keeps its copyleft
LMS of record (Moodle GPL-3.0, Open edX AGPL-3.0, Chamilo GPL-3.0 — all strong in LATAM and
EMEA), and the studio never touches it. 🔵 **A SCORM package is the cleanest licence
boundary in this whole file** — it crosses into the platform as *content*, not as linked
code, which is the one seam no copyleft licence reaches through.

🔴 **The open question, declared:** `589-E`. The same decay has **not** been tested on
`topic:xapi` or `topic:qti`. If xAPI's tooling is alive, the rule above is specific to
SCORM; if it is dead too, this page's whole interchange layer needs re-grading and
`Trend 41` becomes a statement about **maintenance**, not about specifications.


## p588 — 2026-11-01 — the virtual-classroom tier gets a PERMISSIVE platform of record, carried unfiled in this base since `p525`; and two platform licences that secondary sources got wrong, which this page already had right

### 🟢 The tier `p587` filled with a copyleft platform has a permissive one

`p587` placed the virtual-classroom tier with [`bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton)
(**9,262★**, 🔴 LGPL-3.0, *"link, don't modify"*). That was the right row and an incomplete
tier: **there is an Apache-2.0 platform in the same tier**, and this base has been carrying
its address on a *permissive-unshelved candidate list* since `p525`
(`compose/code/p525-title-anchored-grant/permissive_unshelved.txt`) without ever filing it.

| Tier | Platform | Licence (from licence file) | Stars | Last push | May a studio fork and ship it? | The AI play |
|---|---|---|--:|---|---|---|
| 🆕 **Virtual classroom — permissive option** | [apache/openmeetings](https://github.com/apache/openmeetings) | 🟡 **Apache-2.0** for the project's own code, **plus an in-payload third-party block** (MIT, BSD variants, EPL, EDL, some `NOASSERTION`, and **Oracle Free Use Terms**) | **688** | `2026-10-26` | 🟡 **Yes for the ASF code — read the bundle first.** Apache-2.0 permits fork, modify and closed redistribution; the declared dependencies do not all share that grant | 🟢 **Same raw material as BigBlueButton — recordings, whiteboard events, chat, collaborative docs — without the LGPL boundary to engineer around.** Conferencing, whiteboard, polls and document collaboration on Kurento. ASF governance, so the trademark and release process are predictable |

🔴 **Why it is 🟡 and not 🟢, precisely.** The licence payload is Apache-2.0 followed by a
dependency enumeration — the exact shape `P1024` predicts, and the tell is that the file is
far above pristine Apache-2.0 length. Most entries are permissive. **At least one is not an
open-source grant at all (Oracle Free Use Terms), and several read `NOASSERTION`.** 🟢 **The
consequence is narrow and worth stating so nobody over-reads it:** forking and shipping
OpenMeetings' *own* code is clean; shipping a *binary distribution* that bundles those
dependencies is a build-configuration question for counsel, not a platform-choice question.

🔵 **Against BigBlueButton, for an engagement.** BBB is **13× larger** and purpose-built for
teaching (breakouts, learning-analytics-grade recording). OpenMeetings is smaller and more
general. 🟢 **Pick BBB when the client wants the pedagogy and will accept linking; pick
OpenMeetings when the deliverable must be forkable, re-branded and shipped closed** — which
is the one thing BBB's LGPL makes awkward and the reason this row matters at all.

### 🔵 Two platform licences this page already had right, and the secondary channel got wrong

This pass's search leg described [`frappe/lms`](https://github.com/frappe/lms) as
**MIT-licensed and self-hostable**, and asserted [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT)
as Apache-2.0 with no verification. Re-measured against the platform API and this page:

| Row | What the secondary source said | Measured `2026-11-01` | This page already said |
|---|---|---|---|
| `frappe/lms` | 🔴 **"MIT (no restrictions)"** | 🔴 **AGPL-3.0**, 3,360★, branch `develop` | 🟢 **AGPL-3.0** — correct, on three tables |
| `OpenOLAT/OpenOLAT` | 🟡 "Apache 2.0", unsourced | 🟢 **Apache-2.0** (API `NOASSERTION`; licence text read) | 🟢 **Apache-2.0 (text)** — correct |
| `francoisjacquet/rosariosis` | — | 🔴 **GPL-2.0**, default branch **`mobile`** | 🟢 **GPL-2.0**, and it already flags the `mobile` branch |
| `chamilo` | — | 🟡 `repo:chamilo/chamilo` returns **no result** | 🟢 **`chamilo/chamilo-lms`** — the correct address, already carried |

🔴 **So the measured error rate of the secondary channel on platform licences this pass was
`2 of 4`, and both errors ran in the dangerous direction** — reporting a network-copyleft
platform as MIT is the mistake that puts a client's proprietary work at risk. 🟢 **The base
was right on all four, including the address that looks dead.** The `chamilo` miss is `p586`'s
own trap verbatim: **a wrong address is indistinguishable from a deleted repository**, and
the fix was an org search, not a deletion. 🔵 **Nothing on this page needed correcting; this
is a control that passed, recorded so the next pass does not re-run it.**

---

## p587 — 2026-11-01 — the virtual-classroom and assessment tiers, placed; and the unlicensed SIS re-confirmed rather than re-discovered

Every licence below read from the repository's own licence file on **2026-11-01**. Two tiers
this page had named but not filled now have a platform of record each.

| Tier | Platform | Licence (from licence file) | Stars | Last push | May a studio fork and ship it? | The AI play |
|---|---|---|--:|---|---|---|
| 🆕 **Virtual classroom** | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0** | **9,262** | `2026-10-31` | 🟡 **Link, don't modify.** LGPL permits proprietary code to *link* against it; changes to BBB itself carry back | 🟢 **The richest AI surface on this page and the least contested**: recordings, transcripts and whiteboard events are the raw material for lecture summarisation, participation analytics and auto-generated revision material. The AI sits **beside** BBB consuming its recordings — no fork, no copyleft exposure. 🔴 Default branch is `v4.0.x-develop`, not `main`. |
| 🆕 **Assessment / problem-driven courses** | [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn) | 🔴 **Split grant** — AGPL-3.0 CE **+** proprietary `apps/prairielearn/src/ee/` **+** AGPL-3.0 on *all* client-side JS **+** MIT portions | **527** | `2026-11-01` | 🔴 **No** | 🟡 **Read it, do not ship it.** Its question-generation and auto-grading model is the best open reference for problem-driven assessment, and its licence file is the reason a studio builds its own: the AGPL reaches the compiled client JavaScript, which is the part a client would want branded. |
| 🆕 **Skills / competency taxonomy** | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL-1.0** — a **data** licence, not a software one | **7,489** | `2026-10-30` | 🟡 **Counsel question** — share-alike attaches to *derived databases* | 🟢 The spine for competency mapping, course-to-job alignment and reskilling paths. Build a **produced work** on it freely; 🔴 publishing an *enriched taxonomy* means publishing the enrichment. See `587-E`. |
| 🆕 **LTI 1.3 interchange (PHP)** | [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | 🟢 **Apache-2.0** | **124** | 🔴 `2024-08-20` | 🟢 **Yes** | 🟢 The reference implementation **under the standards body's own org** — 1EdTech writes LTI. 🔴 ~26 months stale, so pin and test. 🔵 Same codebase as the `packbackbooks` address this page already carries: **1EdTech is where it moved.** |

### 🔵 The unlicensed SIS: re-confirmed, and this page was already right

[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) — **347★, pushed
`2026-10-26`, no licence file at five paths on `master`, API licence `NONE`.**

🟢 **This page's existing row already says exactly that** — *"Actively maintained and
unlicensed. A student information system with no grant is `BLOCK` regardless of how current
it is."* 🔵 It is recorded here because `p587` re-measured it from a different channel and
reached the identical verdict, which is **confirmation, not a finding** — and because a
naive sweep this pass flagged this row as self-contradictory when it is not. Full account at
`587-A` on [`../agents/top.md`](../agents/top.md).

---

## p586 — 2026-11-01 — the education ERP tier, found and licence-resolved: what a studio may customise, and the one licence that makes an AI side-car legal without a fork

🟢 **The question this page exists to answer** — *which real education systems can a studio
put AI on top of, and under what licence* — now has an answer at every tier **except one**.
Every licence below was read from the repository's own licence file on **2026-11-01**, not
taken from the GitHub API, which reports `NOASSERTION` for two of these rows.

### The tiers, and what each one permits

| Tier | Platform | Licence (from licence file) | Stars | Last push | May a studio fork and ship it? | The AI play |
|---|---|---|--:|---|---|---|
| **Education ERP** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0 (text)** | **903** | `2026-10-29` | 🟡 **Not a fork — a side-car** | 🆕 **The "Odoo for education".** Admissions, fees, attendance, library, hostel, exams on one database, built as **Odoo modules**. 🟢 LGPL-3.0 is *weak* copyleft: a separate module calling its API **keeps its own licence**. So the AI goes in as a standard Odoo extension and stays proprietary. 🔴 Edits to its own files must be published. |
| **LMS of record** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0 (text)** | 1,240 | `2026-10-30` | 🟢 **Yes** | ECL-2.0 is Apache-2.0 with the patent grant narrowed for education. Higher-ed consortium governance. **The one platform of record a studio may lawfully fork, modify and ship.** |
| **LMS of record** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0 (text)** | 449 | `2026-10-30` | 🟢 **Yes** | Swiss-governed, used across DACH higher education. API says `NOASSERTION`; the licence text says Apache-2.0. **Re-read and confirmed at `p586`.** |
| **Offline-first platform** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT (text)** | 1,163 | `2026-11-01` | 🟢 **Yes** | 🟢 **The highest-leverage permissive platform for LATAM, Africa and rural APAC** — built for the connectivity conditions that defeat cloud LMSs. Branch `develop`. |
| **Course environment** | [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT (text)** | 437 | `2026-11-01` | 🟢 **Yes** | Git-versioned course content and auto-graded work. UIUC. |
| **LMS of record** | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 **AGPL-3.0** | **8,213** | `2026-11-01` | 🔴 **No** | 🟢 **But the extension points are permissive**: [`XBlock`](https://github.com/openedx/XBlock) (Apache-2.0) and [`codejail`](https://github.com/openedx/codejail) (Apache-2.0) let proprietary AI plug in **without inheriting network copyleft**. Stand it up with [`overhangio/tutor`](https://github.com/overhangio/tutor). 🔴 Cite *this* address — `openedx/edx-platform` is the pre-rename name and returns `422`. |
| **LMS of record** | [moodle/moodle](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** | 7,567 | `2026-10-30` | 🔴 **No** | The largest installed base in EMEA and LATAM public education. 🟢 Attach via **LTI 1.3** ([`ltijs`](https://github.com/Cvmcosta/ltijs), Apache-2.0) and the AI stays outside the GPL boundary entirely. |
| **LMS of record** | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** | 6,893 | 🟡 `2026-04-30` | 🔴 **No** | North American higher-ed default. 🟡 **~6 months since last public push — the slowest-moving platform of record on this page.** Attach via LTI or [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, 310★, FERPA-aware). |
| **SIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** | 649 | `2026-10-28` | 🔴 **No** | 🆕 Scheduling, grades, attendance, billing. Strong francophone and LATAM base. 🔵 Default branch is **`mobile`**. |
| **School management** | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** | 410 | `2026-10-28` | 🟢 **Yes** | The only permissive row in the student-records tier — and it is school management, **not** an ERP. Laravel + Filament. |

### 🔴 The one tier with no permissive option at any size

**Systems of record for students and money.** `openeducat_erp` is LGPL-3.0,
`frappe/education` is GPL-3.0, `rosariosis` is GPL-2.0; the only permissive row
(`academico`, MIT, 410★) is school management rather than an ERP. 🔴 **An engagement that
needs to fork an education ERP cannot.** Gap `586-D`.

🟢 **And that is survivable, because of how the licences happen to fall.** Both routes into
a copyleft system of record keep a studio's AI proprietary **without a fork**:

| Route | Boundary that protects the studio's code | Works against |
|---|---|---|
| **Odoo module side-car** | LGPL-3.0's module boundary — a separate module calling the API keeps its own licence | `openeducat_erp` |
| **Permissive extension point** | `XBlock` / `codejail` are Apache-2.0 *inside* an AGPL platform | Open edX |
| **LTI 1.3 tool provider** | The AI is a separate service; the LMS never links it | Moodle, Canvas, Sakai, ILIAS, **any** LMS |

🔴 **So the standing rule for this page is: never fork a platform of record to add AI.**
Fork only when the client needs the platform itself changed — and then only Sakai,
OpenOLAT, Kolibri or relate, the four that permit it.

### 🔵 Customisation surfaces, measured

| Surface | Repo | Licence | Stars | Last push | What it buys |
|---|---|---|--:|---|---|
| LMS-agnostic attachment | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 | 373 | `2026-10-31` | Full LTI 1.3 tool provider in Node — into any LMS without forking it |
| LMS-agnostic attachment (Python) | [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | 🟢 MIT | 138 | 🔴 `2024-08-18` | 🔴 ~26 months stale and still the only maintainable permissive Python option — gap `585-E`, and the cheapest contribution play in this industry |
| Open edX extension | [openedx/XBlock](https://github.com/openedx/XBlock) | 🟢 Apache-2.0 | 471 | `2026-11-01` | The permissive seam into an AGPL platform |
| Untrusted learner code | [openedx/codejail](https://github.com/openedx/codejail) | 🟢 Apache-2.0 | 477 | `2026-10-27` | Sandboxed execution — the component every "run the student's program" feature needs |
| Canvas, agent-native | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 🟢 MIT | 310 | `2026-11-01` | 102 tools, 8 agent skills, FERPA-aware. Univ. of Illinois |
| Legacy content | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 MIT | 362 | `2026-10-28` | SCORM runtime in JS |
| Assessment | [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 Apache-2.0 (text) | 216 | `2026-10-28` | Browser e-assessment, maths emphasis. Newcastle University |
| Autograding | [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | 🟢 BSD-3-Clause | 1,370 | `2026-10-28` | Notebook assignment, autograde, release |
| Exam lockdown | [SafeExamBrowser/seb-win-refactoring](https://github.com/SafeExamBrowser/seb-win-refactoring) | 🔴 MPL-2.0 | 361 | `2026-10-30` | Sector standard; file-level copyleft — compose alongside, do not modify |

---

## p585 — 2026-11-01 — the forkable tier: four platforms of record a studio may lawfully modify and ship, two of them recovered from a licence field this base had wrong

🔴 **This page's standing licence rule — *"every platform of record is copyleft"* — is
false, and the two corrections in the body of this file are marked in place.** Four
platforms of record are permissive. Each licence below was read from the repository's own
licence file on **2026-11-01**, not taken from the GitHub API.

### 🟢 The forkable platform tier — adopt, modify, ship

| Platform | Repo | Licence | Stars | Last push | Region | What you may do with it |
|---|---|---|--:|---|---|---|
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0 (text)** | **1,240** | `2026-10-30` | North America | 🟢 **Fork, modify, ship closed.** ECL-2.0 is Apache-2.0 with the patent grant narrowed for education — its own text says so. Higher-ed consortium governance, 1,020 forks. **The default choice when a client wants to own the platform.** |
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT (text)** | **1,163** | `2026-11-01` | Global | 🟢 **Fork, modify, ship closed.** Offline-first by design — built for low-connectivity deployment. 1,016 forks. **The right base for LATAM, African and rural APAC engagements**, where a cloud LMS fails on infrastructure rather than on features. |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0 (text)** | **449** | `2026-10-30` | EMEA | 🟢 **Fork, modify, ship closed.** Swiss-governed, used across DACH higher education. 🔴 This page already said Apache-2.0 while `repos/foundations.md` carried `NOASSERTION` — the contradiction is resolved in favour of this page. |
| **relate** | [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT (text)** | **437** | `2026-11-01` | North America | 🟢 **Fork, modify, ship closed.** Git-backed, versioned course content with auto-graded work — the only platform here whose content model is a repository, which makes it the natural fit for engineering and CS curricula. UIUC. |

### 🟢 The permissive operations tier — SIS, portals and credentials

| Platform | Repo | Licence | Stars | Last push | Region | Role |
|---|---|---|--:|---|---|---|
| **academico** | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** | **410** | `2026-10-28` | Global | 🟢 **The only permissive SIS of any size found.** School management for small/medium institutions; Laravel + Filament. Everything larger in this tier is copyleft. |
| **richie** | [openfun/richie](https://github.com/openfun/richie) | 🟢 **MIT** | **318** | `2026-11-01` | EMEA | CMS for the education **portal** in front of an LMS — catalogue, enrolment funnel, marketing. France Université Numérique. |
| **iblai/lms** | [iblai/lms](https://github.com/iblai/lms) | 🟢 **MIT** | **208** | `2026-10-30` | Global | Skills-intelligence layer: competency tracking and credentials over existing course delivery. |
| **pupilfirst** | [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | 🟢 **MIT (text)** | **981** | 🔴 `2025-12-09` | APAC | Asynchronous online school with reviewed submissions. 🟢 Permissive and the API hid it. 🔴 **~11 months without a push** — adopt deliberately, not by default. |

### 🔴 The copyleft platforms — attach to, do not fork

Still the larger half of the market by deployment, and the correct posture is **attachment
via a permissive extension point**, never a fork.

| Platform | Licence | Stars | Attach how |
|---|---|--:|---|
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 AGPL-3.0 | **8,213** | 🟢 **`XBlock`** (Apache-2.0) for components, **`codejail`** (Apache-2.0) for untrusted learner code, **`tutor`** to stand it up. Proprietary AI lives in the XBlock, not in a fork. |
| [moodle/moodle](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | **7,567** | 🟢 **LTI 1.3** via `ltijs` (Node, Apache-2.0) or `pylti1.3` (Python, MIT). The agent stays outside the GPL boundary. |
| [frappe/lms](https://github.com/frappe/lms) · [frappe/education](https://github.com/frappe/education) | 🔴 AGPL-3.0 · GPL-3.0 | 3,360 · 688 | 🟢 Frappe REST API. 🔵 `frappe/education`'s grant is at `develop/license.txt` — lowercase, non-default branch. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 | **1,019** | 🟢 LTI. Strong LATAM and francophone install base — worth knowing for regional engagements. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 GPL-3.0 | 507 | 🟢 LTI; strong native assessment module, so compete on AI feedback rather than on item delivery. |
| [claroline/Claroline](https://github.com/claroline/Claroline) | 🔴 AGPL-3.0 (text) | 349 | 🟢 LTI. API reported `NOASSERTION`; resolved from licence text this pass. |
| [INGInious/INGInious](https://github.com/INGInious/INGInious) | 🔴 AGPL-3.0 (text) | 243 | 🟢 Containerised secure grading — a reference design for sandboxing, not a fork target. UCLouvain. |

🔵 **The rule this page should carry going forward**, replacing the withdrawn one:
**the platform tier splits — four forkable permissive platforms of record, the rest
copyleft — while the extension and interchange tier (`XBlock`, `codejail`, `ltijs`,
`pylti1.3`, `scorm-again`, `Numbas`) is almost entirely permissive.** A studio's licence
exposure is therefore a *choice*, not a constraint imposed by the industry.


## p584 — 2026-11-01 — **the SIS / gradebook / proctoring platform tier, measured with denominators — and the licence rule for this page rewritten: the platform tier is copyleft with exactly ONE permissive exception, and that exception is licensed under education's own licence**

🔵 **`583-A` token-check, published first.** Of `11` platform addresses measured:
**`3` FILED** (`openSIS-Classic`, `academico`, `rosariosis`), **`7` UNFILED**, **`1` NEW`**.

### 🔴 The licence rule on this page was stated too strongly, and the counterexample was already on it

This page says *"No permissive production LMS"* (line ~296) and *"uniformly copyleft"*
(line ~68); `intel/trends.md` `Trend 36`, filed last pass, says the platform tier is
*"copyleft without exception."*

🟢 **Measured this pass across `13` platform rows above `1,000★` on five axes:**

| grant | rows | rows named |
|---|--:|---|
| 🔴 AGPL-3.0 | **`6`** | `frappe/lms` `3,360★` · `learnhouse` `2,438★` · `classroomio` `1,736★` · `courselit` `1,291★` · `overhangio/tutor` `1,131★` · `hrshadhin/school-management-system` `1,152★` |
| 🔴 GPL-3.0 | `3` | `Unifiedtransform` `3,003★` · `chamilo/chamilo-lms` `1,019★` · (+1 off-axis) |
| 🔴 GPL-2.0 | `1` | `course-tencent-cloud` `1,175★` |
| 🟢 **ECL-2.0 — permissive** | **`1`** | **`sakaiproject/sakai` `1,240★`, pushed `2026-10-30`** |
| 🟡 MIT | `2` | `SWE-agent` (🔴 **not an education platform** — `Trend 29`) · `4jean/lav_sms` (🔴 cold `2024-03-06`) |

🟢 **The corrected rule, which is what a studio actually needs to hear:** *the education
platform tier is copyleft everywhere except Sakai, and Sakai is permissive under
**ECL-2.0** — the Educational Community License, an Apache-2.0 derivative written for this
sector — not under MIT or Apache.* **Sakai is the one platform of record a studio may fork
and ship.** Byte-read `11,120 B`, `master/LICENSE`, this pass.

🔵 **Why this matters more than the licence trivia:** every delivery rule on this page has
been shaped by "you may not ship a modified platform." That rule is still right **six times
out of seven**, and now it has a named exception, so an engagement that genuinely needs a
forked platform of record has exactly one legal starting point instead of none.

### 🟢 The platform and gradebook tier, shelved

| platform | address | grant | ★ | pushed | tier | note |
|---|---|---|--:|---|---|---|
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** (`11,120 B` ✅) | 1,240 | `2026-10-30` | LMS of record | 🟢 **The one forkable platform of record.** Apereo Foundation; research universities |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** | 649 | `2026-10-28` | SIS of record | The head of the SIS axis. 🔵 Client-owned code, never shippable IP |
| **Academico** | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** (`1,094 B`) | 410 | `2026-10-28` | SIS, small/medium | 🔵 Already filed. **Below Trend 36's `1,000★` bar**, which is why it does not carry the exception — Sakai does |
| **openSIS Classic** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🟡 **NOASSERTION** by API — a queue, not a verdict | 347 | `2026-10-26` | SIS of record | 🔵 Already filed; re-measured |
| **Koakademy** | [yukazakiri/koakademy](https://github.com/yukazakiri/koakademy) | 🔴 **AGPL-3.0** | 9 | `2026-11-01` | academic management | 🔴 **UNFILED `36×` — the highest re-find count this base has recorded.** Pushed today. Student-lifecycle platform |
| **e-gradebook-platform** | [kadusic1/e-gradebook-platform](https://github.com/kadusic1/e-gradebook-platform) | 🔴 **AGPL-3.0** | 0 | `2026-03-28` | gradebook | 🆕 **Multi-tenant with database-per-tenant isolation** — the only row on these shelves that solves the multi-district tenancy problem explicitly |
| **Safe Exam Browser** | [SafeExamBrowser/seb-win-refactoring](https://github.com/SafeExamBrowser/seb-win-refactoring) | 🟡 **MPL-2.0** (`16,726 B` ✅) | 361 | `2026-10-30` | exam lockdown | 🔴 **UNFILED `65×`.** ETH Zürich; the sector-standard lockdown client. 🟡 File-level reciprocity — shippable with care |
| **Eloom LMS** | [eloompty/Eloom-LMS-International](https://github.com/eloompty/Eloom-LMS-International) | 🟢 **MIT** | 0 | `2026-10-06` | LMS, training providers | 🔴 **UNFILED `8×`.** For training providers and colleges |
| **WalnutEdu SIS** | [laveshparyani/walnutedu-student-management](https://github.com/laveshparyani/walnutedu-student-management) | 🟢 **MIT** | 3 | `2026-09-26` | SIS module | 🆕 A **Frappe v15** app — i.e. it inherits the ERPNext/Frappe framework stack this page already tracks |
| **Sakai attendance** | [sakaicontrib/attendance](https://github.com/sakaicontrib/attendance) | 🟢 **ECL-2.0** (`11,120 B` ✅) | 14 | `2026-09-01` | LMS extension | 🔴 **UNFILED `16×`.** The worked example of extending Sakai through its own contrib channel |

🔴 **The proctoring tier is where the licensing collapses.** `MyProctor.ai` (`236★`),
`GodsEye`, `sanket2000/proctoring` and the bulk of the `150`-row `topic:proctoring` axis
carry **no licence at all**; `eLearning-BS23/moodle-quizaccess_proctoring` (`30★`) is
`NOASSERTION`; `meefik/ITMOproctor` is GPL-3.0 and cold since `2023`. 🟢 **The only
shippable artefacts at the proctoring boundary are `SafeExamBrowser` (MPL-2.0) and the two
MIT agent rows shelved on `agents/top.md` this pass.** 🔵 **Delivery consequence:** quote
proctoring as *integration with SEB plus a custom agent*, never as "adopt an open-source
proctoring platform" — there is no licensed one to adopt.


## p583 — 2026-11-01 — **the interchange layer that bolts a copyleft LMS to anything else, and the licence rule that decides what a studio may ship**

🔵 **Source:** `538` repositories across `topic:lti`, `topic:xapi`, `topic:qti`,
`topic:lti-provider`, grants byte-read. Records:
[`integration-axis-sweep`](../evidence/integration-axis-sweep.2026-11-01-p583.tsv),
[`grants-byte-read`](../evidence/grants-byte-read.2026-11-01-p583.tsv).
🔵 **The SIS/ERP platform leg was not re-run this pass** — `p581` ran it and returned
nothing new, and `p582` re-confirmed the tier as uniformly copyleft.

### 🟢 The delivery rule, measured: the glue is permissive, the platform is not

| layer | licence shape | what a studio may do |
|---|---|---|
| 🔴 **platform of record** | Moodle **GPL-3.0** · Open edX **AGPL-3.0** · Chamilo **GPL-2.0** · ILIAS **GPL-3.0** · OpenEduCat **LGPL-3.0** · Gibbon **GPL-3.0** | 🔴 **Deploy and configure; do not ship a modified fork as a product.** AGPL on Open edX reaches network use. |
| 🟢 **interchange / integration layer** | **`22 of 33`** measured rows permissive (`66.7 %`) — MIT, Apache-2.0, BSD-3-Clause | 🟢 **Build on, embed, relicense-compatible, ship.** This is where the billable artefact lives. |
| 🟡 **the one permissive platform seat** | OpenOlat — **Apache-2.0 by byte-read**, `NOASSERTION` by API (`Trend 31`) | 🟢 The option when the client is *choosing* rather than remediating. |

🟢 **So the vertical recipe is not "replace the LMS".** It is: leave the copyleft platform
in place, and deliver a permissive interchange layer plus the agent on top of it. That is
the shape every pattern on `compose/patterns.md` now assumes.

### 🟢 The bolt-on layer, by what a client actually asks for

| the ask | the permissive component | licence (byte-read) | ★ | `pushed_at` | region |
|---|---|---|--:|---|---|
| "launch our tool from inside Canvas/Moodle/Open edX" | [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (`1,528 B`) | 73 | `2026-10-05` | North America |
| same, but our stack is **Go** | [StevenWeathers/peregrine-lti](https://github.com/StevenWeathers/peregrine-lti) | 🟢 **Apache-2.0** (`11,357 B`) | 7 | `2025-11-20` | Global |
| same, but our stack is **Laravel/PHP** | [swisnl/laravel-lti-provider](https://github.com/swisnl/laravel-lti-provider) | 🟢 **MIT** (`1,108 B`) | 4 | `2026-08-28` | EMEA |
| "store and query what learners did" | [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) · [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | 334 · 144 | `2025-11-14` · `2026-10-27` | North America |
| "prove the integration is conformant" | [adlnet/lrs-conformance-test-suite](https://github.com/adlnet/lrs-conformance-test-suite) · [adlnet/CATAPULT](https://github.com/adlnet/CATAPULT) | 🟢 **MIT** · **Apache-2.0** | 78 · 59 | `2025-09-04` · `2026-01-20` | North America |
| "move our item bank in and out" | [examplary/qti](https://github.com/examplary/qti) · [metyatech/markdown-to-qti](https://github.com/metyatech/markdown-to-qti) · [rolfis/qti-convert](https://github.com/rolfis/qti-convert) | 🟢 **MIT** · **MIT** · **Apache-2.0** | 2 · 2 · 22 | `2026-10-12` · `2026-09-19` · `2026-06-08` | Global |
| "render items in our own front end" | 🔴 [Citolab/qti-components](https://github.com/Citolab/qti-components) | 🔴 **GPL-3.0** | 18 | `2026-10-30` | EMEA |
| "pipe Moodle events into the LRS" | 🔴 [davidpesce/moodle-logstore_xapi](https://github.com/davidpesce/moodle-logstore_xapi) | 🔴 **GPL-3.0** | 82 | `2026-10-29` | Global |

🔴 **The two rows a studio cannot ship are the two closest to the UI.** Item *rendering*
(`Citolab/qti-components`, GPL-3.0) and the Moodle *event bridge*
(`moodle-logstore_xapi`, GPL-3.0) are both copyleft, and both are the maintained option of
record on their axis. 🟢 **Renderer alternative:** `ewels/starlight-quiz` (Apache-2.0,
`10★`, `2026-09-08`) renders Markdown-authored items — a different authoring contract, but
permissive. 🔵 **Moodle-bridge alternative: none measured.** A Moodle plugin is GPL by the
platform's own plugin rule regardless of the axis's shape, so this is a *build-in-place*,
not a *ship*, and it should be priced as client-owned code.

### 🔴 The gap this layer still has, stated rather than left silent

🔴 **No permissive, framework-independent LTI 1.3 library for Python.**
`dmitry-viskov/pylti1.3` (MIT, `138★`) is the most-starred Python option and was last
pushed **`2024-08-18`** — `26.5` months. The maintained permissive options are Go,
Laravel and JupyterHub-bound. 🔵 **This is a language gap, not an ecosystem gap** (see
`intel/trends.md`, where the broader claim is withdrawn), and for a Python-stack client it
is the single highest-value thing a studio could contribute back.


## p582 — 2026-11-01 — **the authoring and accessibility layers that bolt onto a copyleft LMS, and the four dead integration rows this page should stop offering**

🔵 **The mandated vertical leg (`open source platform education ERP CRM MIT Apache`) was
not re-run this pass.** `p581` ran it and returned nothing new, and
[`../intel/trends.md`](../intel/trends.md) has ruled the mandated web legs *"a regression
test, not a source"*. 🟢 **The structural fact this page carries is unchanged and was
re-confirmed by `p580`'s census:** the platform tier — Moodle (GPL-3.0), Open edX
(AGPL-3.0), Canvas (AGPL-3.0), OpenEduCat (LGPL-3.0), RosarioSIS (GPL-2.0), openSIS (GPL),
Sakai (Apache-2.0 being the exception) — is **uniformly copyleft**, so the permissive
opportunity is always the *layer on top*, never the platform.

🟢 **That is exactly what this pass adds: `8` permissive layers**, every field verified
first-hand `2026-11-01` with `q=repo:owner/name`.

### 🟢 New customisable layers — all permissive, all live

| Layer | Repo | Licence | Stars | Last push | Region | The seam it bolts onto |
|---|---|---|--:|---|---|---|
| **Courseware ingestion** | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 🟢 **MIT** | **193,266** | `2026-10-28` | North America | Bulk-convert an institution's existing `.docx`/`.pptx`/PDF estate into text a Moodle or Open edX AI layer can index |
| **Lesson-slide generation** | [gitbrent/PptxGenJS](https://github.com/gitbrent/PptxGenJS) | 🟢 **MIT** | **6,339** | 🟡 `2025-11-28` | Global | Emits real `.pptx` — teachers keep editing in the tool they already use, which is what kills most generated-courseware pilots |
| **Document assembly** | [dotnet/Open-XML-SDK](https://github.com/dotnet/Open-XML-SDK) | 🟢 **MIT** | **4,617** | `2026-10-27` | North America | Institutional template compliance: inject generated content into the client's own branded `.docx`/`.pptx` |
| **Print/PDF output** | [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) | 🟢 **BSD-3-Clause** | **9,750** | `2026-10-30` | EMEA | Worksheets, report cards, certificates, transcripts — from HTML/CSS the institution controls |
| **Live classroom surface** | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 🟢 **MIT** | **134,943** | `2026-10-31` | Global | Embeddable collaborative whiteboard — the synchronous layer an LMS does not provide |
| **Live captioning / access** | [QuentinFuxa/WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit) | 🟢 **Apache-2.0** | **11,196** | `2026-10-31` | Global | Real-time captions + diarisation + translation on a lecture stream — an accessibility obligation, not a feature |
| **Lecture localisation** | [liuzhao1225/YouDub-webui](https://github.com/liuzhao1225/YouDub-webui) | 🟢 **Apache-2.0** | **5,785** | `2026-10-30` | APAC | Re-voice an existing course library into another language without re-recording it |
| **Handwritten-work capture** | [datalab-to/chandra](https://github.com/datalab-to/chandra) | 🟢 **Apache-2.0** | **12,655** | `2026-10-22` | North America | Phone photo of a worksheet → structured text, incl. **handwriting and tables** |

🔵 **The two rows that change what this page can promise.** `WeasyPrint` and `PptxGenJS`
mean generated material can leave the system **in the institution's own formats and
branding**. Every platform on this page is a web application; every institution
communicates in PDF and PowerPoint. 🟢 **That gap was unbridged on this page until now**,
and it is permissive at both ends.

### 🔴 Four integration rows on this page's axis are dead, and two are unlicensed

🟢 From the `p580` census, re-cut this pass (`evidence/shelf-dead-rows.2026-11-01-p582.tsv`):

| Repo | Stars | Licence | Last push | Verdict |
|---|--:|---|---|---|
| `IronCountySchoolDistrict/iep-printing-php` | 1 | 🔴 **NONE** | 🔴 `2017-03-29` | **9.5 years, unlicensed.** Stop citing entirely |
| `microsoftarchive/Learn-LTI` | 132 | MIT | 🔴 `2023-05-03` | Owner namespace is `microsoftarchive` — **abandoned by declaration** |
| `tc-imba/canvas-auto-rubric` | 33 | 🔴 **NONE** | 🔴 `2022-12-27` | Unlicensed; not usable |
| `fotinikafida/text-to-moodle` | 3 | CC0-1.0 | 🔴 `2023-08-24` | 3★; a sample, not a component |
| `dmitry-viskov/pylti1.3` | 138 | MIT | 🔴 `2024-08-18` | 🟡 **LTI 1.3 is the live standard** — the dead row here is load-bearing. 🟢 **CORRECTED `p584`:** a maintained permissive replacement exists for the **Django** case — [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (MIT, `26★`, `2026-10-28`). The gap is real only for the **framework-independent** slot |

🔴 **`pylti1.3` is the one that matters.** LTI 1.3 is how any AI layer legitimately
attaches to Moodle, Canvas or Open edX, and the base's only shelved implementation has
been cold for 27 months. 🟢 **Declared as a gap rather than papered over:** a permissive,
maintained LTI 1.3 library is a prerequisite for most of the recipes on
[`../compose/patterns.md`](../compose/patterns.md), and this pass did not find one. **The
next pass should sweep `topic:lti` and `topic:lti-provider` singly** — the corrected query
form, on an axis never swept with it.


## p581 — 2026-11-01 — **the media and monitoring layers a vertical deployment needs, and the licence shape of the SIS/ERP tier re-confirmed as uniformly copyleft**

🔵 **The mandated vertical leg (`open source platform education ERP CRM MIT Apache`) ran
and returned nothing new** — `OpenEduCat` (LGPL-3.0), `RosarioSIS` (GPL-2.0), `openSIS`
(GPL), `Gibbon`, `ERPNext`/`frappe/education` (GPL-3.0), `OpenOLAT`. 🔴 **All already
shelved, and the structural fact this page has recorded for many passes reproduces
exactly: there is no permissively licensed student-information system.** The administrative
tier of education software is copyleft end to end; `Fedena`-as-Apache-2.0 appears in one
vendor comparison table and **is not corroborated** — do not quote it.

🟢 **What that means for a studio engagement, unchanged and worth restating:** you do not
replace the SIS. You **integrate against it** and keep proprietary work on the permissive
side of a seam — `openedx/XBlock` and `openedx/codejail` (both Apache-2.0) inside Open edX
(AGPL-3.0), `tsugiproject/tsugi` (Apache-2.0) over LTI into Moodle (GPL-3.0),
`jcputney/scorm-again` (MIT) as the SCORM runtime.

### 🟢 New customisable layers, verified first-hand `2026-11-01`

| Platform / library | Licence | Stars | Region | Where it sits in a vertical deployment |
|---|---|--:|---|---|
| [YaoFANGUK/video-subtitle-extractor](https://github.com/YaoFANGUK/video-subtitle-extractor) | 🟢 **Apache-2.0** | **9,680** | APAC | 🟢 **Lecture-archive ingestion.** Institutions sitting on years of recorded lectures with **captions burned into the video** have no caption file to fetch; this is the only permissive route to text. The precondition for search, tutoring or quiz generation over an existing archive. |
| [nexmoe/VidBee](https://github.com/nexmoe/VidBee) | 🟢 **MIT** | **11,026** | APAC | Transcription + **speaker diarisation** — separates lecturer from student contributions, which is what makes seminar and viva recordings usable rather than just lectures. |
| [smacke/ffsubsync](https://github.com/smacke/ffsubsync) | 🟢 **MIT** | **7,929** | North America | Caption re-alignment. Required for **accessibility compliance** on a re-encoded archive, where timings drift and a misaligned caption track fails audit. |
| [ing-bank/popmon](https://github.com/ing-bank/popmon) | 🟢 **MIT** | **512** | EMEA | 🟢 **Monitoring layer for a deployed tutor or grader.** ING Bank provenance means it was built to be shown to a supervisor — the posture an exam board or ministry needs. |
| [IFCA-Advanced-Computing/frouros](https://github.com/IFCA-Advanced-Computing/frouros) | 🟢 **BSD-3-Clause** | **260** | EMEA | Drift detection on learner-model outputs. Public-institution provenance (Instituto de Física de Cantabria). |

🔵 **Why the monitoring rows belong on a *verticals* page and not only on a repos page.**
Under the EU AI Act timetable this base tracks, stand-alone education systems that grade
work, screen applicants or supervise exams are Annex III high-risk with obligations from
**2 December 2027** (embedded systems **2 August 2028**), and Article 50 transparency
duties from **2 August 2026**. 🟢 **Post-market monitoring is a named obligation, and
until this pass this base had no permissive component to satisfy it with.** `popmon` and
`frouros` are not education-aware — that is the honest limit — but they are the
statistical half, and they are MIT and BSD-3-Clause.

🔴 **Still genuinely absent at the vertical layer**, searched and not found: an
open-source **psychometrically defensible item generator** (calibration tooling exists —
`catsim`, `EduCDM` — generation does not), and any **education-specific** runtime
regression harness for a deployed tutor.


# Vertical education platforms (customisable with AI on top)

## p580 — 2026-11-01 — **every platform on this page re-measured first-hand, and `5 of 10` have no usable licence verdict from the new channel**

🟢 **Instrument.** `q=repo:owner/name` returns licence, stars, `archived` and `pushed_at`
in one call — a call this base has had since `p577` and applied at shelf scale for the
first time this pass (`Gap 579-A`). All figures below are first-hand, `2026-11-01`.

| Platform | Repo | Licence | Stars | Last push | Region | AI layer it accepts |
|---|---|---|--:|---|---|---|
| **Open edX** | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 **AGPL-3.0** | **8,213** | `2026-10-31` | North America | 🟢 **Via `XBlock` (Apache-2.0) and `codejail` (Apache-2.0)** — permissive seams that keep a studio's own AI component out of the network-copyleft duty. The single most important structural fact on this page. |
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** | **7,567** | `2026-10-30` | EMEA | Plugins + **LTI 1.3** external tools; keep the AI service out-of-process and talk LTI. |
| **Oppia** | [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | **6,951** | `2026-10-31` | Global | 🟢 **The permissive platform.** Misconception-aware interactive lessons — the natural host for an adaptive-hinting agent with no licence friction at all. |
| **DSpace** | [DSpace/DSpace](https://github.com/DSpace/DSpace) | 🟢 **BSD-3-Clause** | **1,105** | `2026-10-30` | EMEA | 🟢 Institutional repository. Permissive — the place to put RAG over a university's own research and theses. |
| **openeducat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0** (byte-read; 🔴 API says `NOASSERTION`) | **903** | `2026-10-29` | APAC | The **Odoo-pattern** row: LMS **and** SIS in one PostgreSQL schema — admissions, fees, library, hostel. SCORM 1.2/2004, xAPI, LTI 1.3, OneRoster, Ed-Fi. India-origin. |
| **Submitty** | [Submitty/Submitty](https://github.com/Submitty/Submitty) | 🟢 **BSD-3-Clause** | **807** | `2026-10-31` | North America | 🟢 Homework submission + autograding + **explicit TA grading stage** — a human-in-the-loop checkpoint shipped as a product feature. **Rensselaer Polytechnic.** |
| **frappe/education** | [frappe/education](https://github.com/frappe/education) | 🟡 **GPL-3.0** (byte-read; 🔴 API `NOASSERTION`) | **687** | `2026-10-30` | APAC | School ERP on the Frappe/ERPNext stack. |
| **Gibbon** | [GibbonEdu/core](https://github.com/GibbonEdu/core) | 🔴 **GPL-3.0** ⬅️ *was `unstated`* | **636** | `2026-10-30` | EMEA | 🟢 **Licence settled first-hand this pass.** School management for the K-12 tier; UK/HK-origin. |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟡 **Apache-2.0** (byte-read; 🔴 API `NOASSERTION`) | **449** | `2026-10-30` | **EMEA** | 🟢 **The permissive EMEA LMS** — Swiss-origin, used across DACH universities. The row to reach for when AGPL is a blocker in Europe. |
| **openSIS** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 **`NONE`** | **347** | `2026-10-26` | North America | 🔴 **Actively maintained and unlicensed.** A student information system with no grant is `BLOCK` regardless of how current it is. |

### 🔴 The measurement caveat this page must carry

🔴 **`5 of 10` rows above return `NOASSERTION` or `NONE` from the new channel** —
`openeducat_erp`, `frappe/education`, `OpenOLAT`, `INGInious` and `openSIS`. Four of those
five have a real grant that this base read byte-for-byte in earlier passes;
**only `openSIS` is genuinely ungranted.** 🔵 `NOASSERTION` means GitHub's detector found
a licence file it could not match to an SPDX id — frequently because the project ships a
modified or multi-part grant — and it is **not** evidence of a missing licence.

🟢 **So the rule for this page: the cheap channel sets stars and recency; the licence
column stays byte-for-byte.** See trend 33 on [`../intel/trends.md`](../intel/trends.md).

🟢 **Nothing on this page is archived and only `INGInious` is near the staleness line** —
the vertical-platform tier is the healthiest tier in this base, in sharp contrast to the
question-generation tier, which is entirely abandoned (trend 35).

## p579 — 2026-11-01 — two additions, both MIT, and the operations tier is where the permissive licences are

🔴 **CORRECTED `p585` (2026-11-01):** the claim *"every platform of record is copyleft"* is **false** and was withdrawn as `Trend 36`. Four platforms of record are permissive and forkable: **Sakai** (ECL-2.0, 1,240★), **OpenOLAT** (Apache-2.0, 449★), **Kolibri** (MIT, 1,163★) and **relate** (MIT, 437★) — all four read from their own licence files. See [`../repos/foundations.md`](../repos/foundations.md). The statement below is retained as written for history.


🟢 The pattern `p578` noticed holds and strengthens: **every permissive platform on this
page is an operations system, and every platform of record is copyleft.** The two rows
below were first seen at `p188` and `p200` and sat unshelved for **391** and **379** passes.

| Platform | Repo | Licence | Stars | Category | Where it is strong | AI layer to add on top |
|---|---|---|---|---|---|---|
| Skuul | https://github.com/yungifez/skuul | **MIT** | 468 | **Multi-school operations (SIS)** | School groups and networks — it models **organisations and campuses** as first-class, so one install runs many schools. Covers student records, academic calendars, attendance, gradebooks, timetables, fees, family access, staff, programmes, facilities, boarding and library | Attendance and fee-payment risk scoring; timetable generation under constraints; parent-facing progress and absence summaries from the gradebook. 🔵 **The permissive alternative to the GPL SIS tier** — `RosarioSIS` (GPL-2.0, `649★`), `Unifiedtransform` (GPL-3.0, `3,003★`), `GibbonEdu/core` (GPL-3.0, `636★`). Laravel 13 / Livewire 4 / PHP 8.4 / MySQL 8 / Redis. 🔴 **Read the README before quoting a plan:** V3 is still being prepared, and the project warns that a V2 → V3 upgrade can lose data. Pin V2 or wait |
| Marsha | https://github.com/openfun/marsha | **MIT** | 151 | **Media delivery for courses, via LTI** | The layer between an LMS and video that institutions usually buy. Self-hosted video and document host with transcoding, adaptive-bitrate playback and subtitles; plugs into **Open edX and Moodle over LTI**, so it needs no fork of either | Subtitle and transcript generation, lecture summarisation and chaptering, and search across spoken course content. Django + React + video.js; PeerTube runners for transcoding; S3/Celery; Terraform + Docker. 🔵 **The media seam the AGPL platform question does not touch** — LTI integration means the AGPL of Open edX never reaches your code. Region EMEA on the `openfun` org, placed as on these shelves since `p6` (`richie`, `warren`, `potsie`); the page itself states no affiliation |

### 🔴 The licence map of this page, re-measured this pass

| Platform | Licence | Stars | Shippable without copyleft obligation? |
|---|---|---|---|
| **Skuul** | **MIT** | 468 | 🟢 yes |
| **Marsha** | **MIT** | 151 | 🟢 yes |
| MyClass (`tutor-management-app`) | MIT | 110 | 🟢 yes |
| `academico-sis/academico` | MIT | 410 | 🟢 yes |
| OpenOlat | **Apache-2.0** (file-verified) | 449 | 🟢 yes |
| Sakai | **ECL-2.0** | 1,240 | 🟡 Apache-derived, read it |
| OpenEduCat | **LGPL-3.0** (file-verified) | 903 | 🟡 weak copyleft, linking permitted |
| Moodle | GPL-3.0 | 7,567 | 🔴 no |
| Open edX | **AGPL-3.0** | 8,213 | 🔴 no — network copyleft |
| Chamilo | GPL-3.0 | 1,019 | 🔴 no |
| Frappe LMS / Education | AGPL-3.0 / **GPL-3.0** | 3,358 / 687 | 🔴 no |
| RosarioSIS | GPL-2.0 | 649 | 🔴 no |

🔵 **The decision this table actually makes.** The teaching platform is copyleft almost
everywhere, and that is survivable — you deploy Moodle or Open edX unmodified and integrate
over **LTI / xAPI**, which is what `Marsha` demonstrates and what keeps your own code
yours. The **operations** tier (SIS, tutoring businesses, media, media delivery) is where
permissive licences exist, and it is therefore where a customised, resellable Globant asset
can actually live. 🔴 Building a *fork* of the LMS is the one shape to refuse: on Open edX
it is AGPL, so hosting it obliges you to publish the modifications.

### 🔴 Two addresses on this page that have moved

| Cited as | Response | Live address |
|---|---|---|
| `OpenEduCat-Inc/OpenEduCat` | **`422`** — the owner no longer resolves | `openeducat/openeducat_erp` (**LGPL-3.0**, `903★`) |
| `openedx/edx-platform` | **`422`** — moved | `openedx/openedx-platform` (**AGPL-3.0**, `8,213★`) |


## p578 — 2026-10-31 — one addition, and it is the first *permissive* operations system on this page

| Platform | Repo | Licence | Stars | Category | Where it is strong | AI layer to add on top |
|---|---|---|---|---|---|---|
| MyClass | https://github.com/t1112000/tutor-management-app | **MIT** | 110 | **Tutoring-business operations** | Private tutors, tutoring centres, shadow-education providers — the tier that has no LMS and runs on spreadsheets | Scheduling and billing are already modelled, so the AI work is demand forecasting, churn and attendance risk, and parent-facing progress summaries. Attach `Clew` (MIT) for the learning path and `GeoChat` (Apache-2.0) for maths sessions |

🟢 **Why this row matters more than its star count.** Every system of record on this page is
copyleft — GPL, AGPL, LGPL, with `Sakai` (ECL-2.0) the one permissive exception at the LMS
tier. **`MyClass` is MIT and it is an operations system**, not a seam: students, schedules,
bills, Next.js 15 + Postgres, Sequelize migrations, NextAuth, Docker, self-hosted. For the
first time on this page a client's system of record can be **forked** rather than integrated
around. 🔵 That inverts the standing recommendation (*"deploy these and call them over their
APIs"*) **for this tier only** — it does not touch the LMS tier, where the conclusion stands.

🔵 **Region: APAC, on the application's own design** — `Asia/Ho_Chi_Minh` timezone, VND
currency formatting and a Vietnamese quick-start section. The owner is an individual account
and the page states no country, so this is the lower-confidence placement channel, not the
grant.

🔴 **Scope it honestly.** `110★`, an individual maintainer, and no multi-tenant or
accounting-compliance claim on the page. It is the right base for a **tutoring-centre
pilot** and the wrong base for a ministry. The tier it serves — private supplementary
tutoring — is also the tier most exposed in APAC regulatory swings, which belongs in the
risk section of any proposal built on it.

## p577 — 2026-10-31 — verified platforms and the AI layer each one accepts

These are the real systems a client already runs, or would plausibly adopt. All
licences and star counts verified 2026-10-31 from the repository pages. The last
column is the part Globant builds.

| Platform | Repo | Licence | Stars | Category | Where it is strong | AI layer to add on top |
|---|---|---|---|---|---|---|
| Moodle | https://github.com/moodle/moodle | GPL-3.0 | 7.6k | LMS | EMEA and LATAM public education, ministries, universities | LTI 1.3 tutor tool via `ltijs`; feedback generation modelled on `thm-mni-ii/feedbacksystem`; xAPI out to `openfun/potsie` dashboards |
| Open edX | https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | LMS / MOOC | National and corporate MOOC programmes; the shape national deals take | Same LTI tool; `educhain` for item banks; do **not** fork — AGPL reaches network-served modifications |
| Canvas | https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | LMS | North American higher education | `terracotta` (Apache-2.0) for randomised evaluation of the intervention; `nbgrader` for technical autograding; LTI tutor |
| Oppia | https://github.com/oppia/oppia | Apache-2.0 | 7.0k | Explorations / content platform | Low-bandwidth and underserved contexts | The one platform you can fork freely. Generate explorations with `educhain`, validate with `pedagogy-benchmark` |
| Frappe LMS | https://github.com/frappe/lms | AGPL-3.0 | 3.4k | LMS | Fast pilots, corporate L&D | Stand up in days for a pilot; attach the same LTI tool rather than modifying it |
| LearnHouse | https://github.com/learnhouse/learnhouse | AGPL-3.0 | 2.4k | LMS | Modern self-hosted deployments | Check the **separate Enterprise Licence** on enterprise features before scoping |
| Sakai | https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | LMS / research collaboration | Research universities (Apereo) | **The permissive platform of record** (ECL-2.0 derives from Apache-2.0) — the right base if the client refuses copyleft |
| Chamilo | https://github.com/chamilo/chamilo-lms | GPL-3.0 | 1.0k | LMS | Francophone and LATAM, accessibility-focused | Spanish-language content generation; accessibility-first tutor UI |
| OpenEduCat | https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 903 | **Education ERP / SIS** | Institutes needing admissions, fees, SIS and LMS on one database | The Odoo-of-education: admissions triage, fee-collection prediction, timetable optimisation as Odoo modules |
| H5P | https://github.com/h5p/h5p-php-library | GPL-3.0 | 154 | Interactive content | Embedded inside Moodle, Canvas and Open edX | Generate H5P content types from curriculum text; it is the content format all three LMSs already render |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Autograding | Technical and data curricula | Permissive. LLM-assisted partial-credit feedback on top of deterministic autograding |
| ltijs | https://github.com/Cvmcosta/ltijs | Apache-2.0 | 373 | **Integration layer** | Every platform above | Not a platform — the seam. This is where the AI service lives |

## How to read this table

The first ten rows are the systems of record and are almost all copyleft. The last
two are the permissive tools you actually build with. **ltijs is the keystone**: it
is what lets a permissively licensed AI service serve a copyleft LMS without the
licence question ever arising.

OpenEduCat is the direct analogue of Odoo for ERP — one database spanning
admissions, fees, student records and learning — and is the only verified
open-source system in this set that covers SIS as well as LMS. It is LGPL-3.0,
which is materially weaker copyleft than AGPL and permits linked modules.

## Declared gaps

- **No permissive production LMS.** Sakai (ECL-2.0) is the closest, at 1.2k stars.
- **No verified open-source proctoring or assessment-delivery platform** was found
  that is both permissive and maintained.
- **QTI and accessibility tooling licenses backwards** from the rest of the
  stack — the platforms of record in that layer are copyleft. Carried from a prior
  pass and not re-verified here.

---

## Prior passes (superseded, retained for history)

### (archived) Vertical education platforms

Real, deployed systems that run an institution's operations — the education
equivalent of Odoo for ERP. These are the systems a client already has, and the
systems an AI layer gets attached to.

## 🆕 `p576` — fourteenth pass, 2026-10-31 — 🟢 **BRAZIL'S VERTICAL SYSTEM OF RECORD, FOUND ON A LANGUAGE AXIS THIS BASE HAD NEVER QUERIED — AND ITS DEFAULT BRANCH IS `2.12`, SO A `main`/`master` PROBE CALLS THE LARGEST PORTUGUESE-LANGUAGE EDUCATION PLATFORM ON GITHUB DEAD**

🔵 **The axis:** `topic:educacao` holds **`378`** repositories and had **never been queried
in `575` passes** — it was reachable only through `topic:educacion OR topic:educacao`,
which returns **`0`** (`576-A`, trend 25). Its Spanish counterpart `topic:educacion`
(**`410`**) 🔴 **has no platform tier at all**: it tops out at `71★`, a JavaScript course.

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| **i-Educar** | [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** (`2.12/LICENSE`, 18,092 B ✅ first-hand) | 722 | LATAM | 🟢 **"Lançando o maior software livre de educação do Brasil!"** — municipal *gestão escolar*: enrolment, student records, grades, reporting. PHP. The system a Brazilian municipal network already has, and therefore the system an AI layer gets attached to. 🔴 **Default branch `2.12`.** Third instance of the non-default-branch class on these shelves after `openeducat_erp` (`19.0`) and `Artemis` (`develop`). |
| **i-Diário** | [portabilis/i-diario](https://github.com/portabilis/i-diario) | 🔴 **AGPL-3.0** (`1.6/LICENSE`, 35,326 B ✅ first-hand) — 🔴 **grant written in Portuguese** | 117 | LATAM | The teacher-facing *diário de classe*: attendance, marks, lesson records, syncing to i-Educar. Ruby. 🔴 **`576-E`'s evidence**: the licence opens `LICENÇA PÚBLICA GERAL AFFERO GNU Versão 3` and this base's own classifier regex cannot match it. 🔵 **AGPL §13 matters here specifically** — this is the component a teacher reaches over the network. |
| **pré-matrícula digital** | [portabilis/pre-matricula-digital](https://github.com/portabilis/pre-matricula-digital) | 🟡 not read this pass | 21 | LATAM | Enrolment-vacancy and waiting-list management, integrated with i-Educar. Listed for completeness of the family; 🟢 **alive — `ls-remote` resolves `HEAD` to `2.12`** — 🔴 **but the grant was NOT read this pass, so do not treat it as cleared.** |
| **br.tag** | [ipti/br.tag](https://github.com/ipti/br.tag) | 🔴 **GPL-2.0** (`main/LICENSE`, 18,027 B ✅ first-hand) | 20 | LATAM | School management "baseado em Tecnologia Social", by **IPTI**. The small-municipality end of the same vertical — which is where Brazil's rural-priority obligations land. |

🔴 **The whole Brazilian vertical is copyleft**, every row of it. 🔵 **So the engagement
shape is fixed by the licences before anyone argues about it: deploy these and call them
over their APIs; put the AI in a separate process with its own licence.** That is the same
conclusion `P-568-A` reached for copyleft LMSs, now with a Portuguese-language system of
record to name. 🟢 **And the permissive piece that makes the pairing worth selling sits one
page over**: [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) (**MIT** code,
**CC BY 4.0** data) supplies the national curriculum as structured data with a **local MCP
server** — see `P-578-A`.

## 🆕 `p575` — thirteenth pass, 2026-10-31 — 🔴 **the education ERP vertical: the search leg implied MIT/Apache, the licence file says LGPL-3.0, and the default branch is `19.0`**

🔵 **Why this row needed a correction and not just an entry.** The mandated
`open source platform education ERP CRM MIT Apache` leg returned **OpenEduCat** as
the education-specific answer and said its licence was not stated — correctly
flagging that it should be checked. 🔴 **Checked: it is `LGPL-3.0`, not MIT and not
Apache-2.0.** Anyone who took the leg's framing at face value would have planned a
vendoring strategy the grant does not permit.

| Platform | Repo | Licence (read first-hand) | Default branch | Region | What it runs |
| --- | --- | --- | --- | --- | --- |
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | **LGPL-3.0** (licence file `8,240 B`, opening line *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE"*) | 🔴 **`19.0`** — not `main`, not `master` | Global (India-origin vendor) | Student information and institution ERP built **on the Odoo framework**: admissions, students, faculty, courses, batches, attendance, exams, library, fees. 🟢 **The education-sector Odoo this page has pointed at generically for passes without naming the licence or the branch.** |

🔴 **The branch finding is the reusable one.** `git ls-remote --symref` resolves
`openeducat_erp`'s `HEAD` to **`19.0`** — the Odoo-style release-numbered branch. 🔵 A
probe that assumes `main` or `master` **does not get a wrong answer, it gets a 404 and
reports the repository dead** — the exact failure mode `P977` recorded for
`openedx/edx-platform`'s heads→tags move, now reproduced on a second platform. 🟢 Any
grant, version or manifest read against this repository must resolve `HEAD` first.

🟢 **What LGPL-3.0 means here, stated as the engagement decision.** LGPL is the
*weak* copyleft rung: you may **link** proprietary code against it and ship that
combination, provided the LGPL'd component itself stays LGPL and remains replaceable.
🔵 So for OpenEduCat the doctrine is slightly softer than this base's standing
"attach, do not fork" rule: **an AI layer that calls OpenEduCat over its API or as a
separate Odoo module is clean, and a patch to OpenEduCat's own files is LGPL and must
be published.** 🔴 It is still not a codebase to absorb into a proprietary product.

🔵 **Where this sits against the rest of the page.** Every platform of record on these
shelves is now confirmed copyleft — Moodle (GPL-3.0), Open edX (AGPL-3.0), TAO
(GPL-2.0), UDOIT (GPL-3.0), Cboard (GPL-3.0), OpenEduCat (**LGPL-3.0**). 🟢 **OpenEduCat
is the weakest rung of the six**, which makes it the most permissive system of record
this industry offers — and that is a genuinely useful thing to know before an ERP
engagement.

🔴 **Not shelved, and why:** [`fotinikafida/text-to-moodle`](https://github.com/fotinikafida/text-to-moodle)
(`3★`) produces restorable Moodle `.mbz` course packages — relevant to the platform
this page's largest row runs — but its grant is a **Creative Commons** licence
(`7,047 B`), which is a *content* licence, not a software licence. 🔵 Usable as
courseware, not as a component.
## 🆕 `p574` — twelfth pass, 2026-10-31 — 🟢 THE ASSESSMENT-DELIVERY AND ACCESSIBILITY VERTICAL, which this base has never held: **TAO** is the QTI platform of record and it is `GPL-2.0`

🔵 **Why this page needed it.** Every row above runs *teaching* or *records*. The
third system an institution actually operates is **assessment delivery** — the
thing that must survive an audit, an appeal and an accommodation request — and
this page held no row for it. 🔴 The adjacent obligation is dated: in the United
States `April 26, 2027` / `April 26, 2028` under the ADA Title II web rule, and in
the EU `EN 301 549` under the Web Accessibility Directive. See
[`../intel/market.md`](../intel/market.md).

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| **TAO** | [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | **GPL-2.0-only** (licence file `18,025 B`; `composer.json` agrees) | — (unread) | EMEA | The **QTI-native** computer-based testing platform, OAT SA (Luxembourg). Item banking, delivery, proctored sittings, results. Used by ministries and exam boards; the reference implementation standards-conformance arguments are made against. 🔴 **GPL-2.0 — deploy it, do not vendor it.** |
| **TAO / QTI items** | [oat-sa/extension-tao-itemqti](https://github.com/oat-sa/extension-tao-itemqti) | **GPL-2.0** (licence file `18,025 B`) | — (unread) | EMEA | TAO's item authoring and rendering extension — the part that reads and writes **QTI** itself. 🟢 New to this base entirely: `0` mentions in `573` passes. |
| **UDOIT** | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | **GPL-3.0-only** (`35,147 B`; `package.json` **and** `composer.json` agree) | 117 | North America | The Universal Design Online content Inspection Tool: scans a **Canvas** course's content for accessibility defects and fixes them in place. University of Central Florida. 🟢 **The nearest thing to an off-the-shelf Title II remediation tool in open source.** |
| **Cboard** | [cboard-org/cboard](https://github.com/cboard-org/cboard) | **GPL-3.0-only** (`35,141 B`; `package.json` agrees) | 766 | Global | Browser-based **AAC** board with text-to-speech, used in classrooms for non-verbal learners. Deployed, multilingual, and the obvious host for an AI symbol-prediction layer. |

🔴 **All four are copyleft, and that is the finding, not an accident of
sampling.** The permissive supply in this layer is converters and browser
extensions (see [`../repos/foundations.md`](../repos/foundations.md)); the
*platforms* are GPL. 🔵 **The engagement shape that follows** is the one `p557`
established for the education-ERP vertical: **client-hosted, deployed unmodified,
customisation in separately licensed extensions, patches upstream.** It is a
services engagement, not a product one — and it is sellable precisely because the
deadline is the client's, not the vendor's.

🟢 **One existing row corrected on this page by a first-hand read:** `OpenOlat`'s
licence cell said *"Apache-2.0 (README badge; sidebar unnamed)"*. The licence file
at `master` is **`10,982 B` of Apache-2.0**, with a `14,712 B` `NOTICE.TXT`
alongside. The badge was right; it is now **measured**, which is the difference
between a citation and a claim.

## Eleventh pass (`p573`, 2026-10-31) — 🟢 THE SIS AXIS IS NOW MEASURABLY EXHAUSTED: `topic:student-information-system` (**187**) read 20 deep, **zero** new, and every platform-grade row was already on this page

🔵 **This is a completeness result, and it is the first one this page can
actually defend.** Earlier passes added SIS rows opportunistically. This pass
swept the axis GitHub itself names for the category and compared every top row
against this base's `3,168`-row address ledger.

| axis | repositories | rows read | new to this base |
| --- | --: | --: | --: |
| 🟢 [`topic:student-information-system`](https://github.com/topics/student-information-system) | **187** | 20 | 🟢 **0 — and that is the finding** |

🟢 **The three platform-grade rows in the axis's top 20 are all already shelved
here, with grants read first-hand in earlier passes:**
[francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis)
(649★, **GPL-2.0**), [academico-sis/academico](https://github.com/academico-sis/academico)
(410★, **MIT**), [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic)
(347★, **GPL-2.0**). 🟢 **So the claim this page could not previously make is now
measured: for open-source student information systems, this KB holds the
deployable population, not a sample of it.**

### 🔴 And the reason the axis looks bigger than it is

🔴 **Below ~300★ the axis is almost entirely student coursework, not software an
institution could run.** Rows 4–20 of the top 20 include a C# WPF desktop app
(20★), a Django "student data application" (15★), several PHP admin-panel
exercises (7–12★), two unofficial scraping APIs for commercial SIS products
(Follett Aspen, SRM University), and — tagged `student-information-system` — **a
bike-rental app for students near a university campus** (7★).

🔵 **Consequence for this page, stated as a rule:** the open-source SIS field has
a **hard floor at roughly 300★**, below which the tag stops denoting
institution-grade software. 🟢 **That floor is a genuine property of this
category and not of GitHub's star distribution generally** — compare
`topic:learning-management-system`, where this KB has shelved real platforms at
**10★**, **54★** and **102★** (`euron-open-lms`, `TutorLoom`, `Mentingo`). 🔴 **So
"sweep below the star floor", which this base adopted as a general rule in
`P-572-C`, is productive for LMS and agent axes and wasteful for SIS.** The rule
needs a per-axis qualifier, and this is the first counter-example measured.

### 🔵 What this means for an engagement

🟢 **The permissive/copyleft shape of the SIS layer is now settled and it is
uncomfortable:** of the three deployable systems, **two are GPL-2.0** — which
carries *no patent grant* and is *not* upgrade-compatible with GPL-3.0 code — and
the one **MIT** option (`academico`) is explicitly scoped to "small and medium
institutions". 🔴 **There is no permissively licensed, university-scale open-source
SIS.** That absence has now been tested against the correctly named axis rather
than inferred, and it is the single most important procurement fact on this page:
**a registrar-scale SIS engagement attaches to the client's existing system over
its API; it does not fork one.** Registered `573-B`.


## Tenth pass (`p572`, 2026-10-31) — 🟢 FIVE PLATFORMS ADDED, ONE OF THEM **MIT**, ALL FIVE RE-FOUND BETWEEN `83` AND `93` TIMES WITHOUT EVER BEING SHELVED

🟢 **`ls1intum/Artemis` is the headline: a full academic platform under MIT**,
from TU München, with the university named inside the grant itself. Every other
platform on this page is GPL-, AGPL-, LGPL- or ECL-licensed. 🔵 For a client who
wants to modify a platform and keep the modifications, Artemis is the only row
here that allows it.

🔴 **All five were absent from every shelf page in this KB** while this base's own
sweeps returned them `83`–`93` times each. The audit behind that number is
`572-A`, recorded in [`../repos/foundations.md`](../repos/foundations.md):
**`3,455` addresses seen across the base's history, `170` ever shelved.**

🟢 **Two platform categories this page was missing entirely are now filled:**
**lecture capture** (`opencast`, ECL-2.0) and a **true SIS** (`rosariosis`,
GPL-2.0 — enrolment, scheduling, attendance, billing, which is not what an LMS
does). 🟢 And the **ERP** the already-shelved `frappe/lms` is built on —
`frappe/erpnext`, `40.8k★` with an Education module — is now on the page beside it.

🔵 **Licence posture across this page, stated once so an engagement can read it
off:** `Artemis` **MIT** → fork freely · `opencast` **ECL-2.0**, `Sakai`
**Apache-2.0** → fork, mind the narrowed patent grant · `Odoo`/`OpenEduCat`
**LGPL-3.0** → link, don't modify · `Moodle`/`Gibbon`/`ILIAS`/`i-educar`/`ERPNext`
**GPL-2.0/3.0** → attach over API or LTI · `Open edX`/`Canvas`/`frappe-lms`
**AGPL-3.0** → §13 network source-offer obligation on any hosted deployment.

## Education ERP / Student Information Systems

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| Artemis | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | 🟢 **MIT** (1,091 B ✅ first-hand; sidebar agrees) | 824 | EMEA | 🟢 **The most permissively licensed full academic platform in this KB, and it was absent from every shelf page while being re-found `97` times.** "Artemis - Interactive Learning with Automated Feedback": programming exercises with automatic assessment, quizzes, modelling, text and file-upload exercises, exam mode. 396 forks. 🟢 **Region is first-hand, not inferred: the grant's own copyright line reads *"Copyright (c) 2026 TUM Applied Education Technologies"*** — Technische Universität München, under `p571`'s institution-holder instrument. 🔵 **Compare the field: Moodle GPL-3.0, Open edX AGPL-3.0, Canvas AGPL-3.0, ILIAS GPL-3.0, Sakai Apache-2.0 — Artemis is MIT.** For a client that wants to ship a modified platform without publishing the modifications, this is the only row on this page that permits it outright. |
| Opencast | [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** (11,340 B ✅ first-hand; sidebar agrees) | 509 | EMEA | "The free and open source solution for automated video capture and distribution at scale." 260 forks. 🔵 **ECL-2.0 is the Educational Community License — an Apache-2.0 derivative, OSI-approved, whose patent grant is narrowed to the contributing institution's own claims** rather than Apache's broader grant. Permissive and buildable; the patent-clause difference is the one thing to put in front of a procurement lawyer. The lecture-capture layer nothing else on this page provides, and it was absent from every shelf while being re-found `93` times. |
| ERPNext | [frappe/erpnext](https://github.com/frappe/erpnext) | **GPL-3.0** (35,149 B ✅ first-hand, `develop/license.txt`) | 40,800 | APAC | "Free and Open Source Enterprise Resource Planning (ERP)." 13,400 forks — **the largest star count on this page by a factor of ten**, and it was absent from every shelf page. Ships an **Education** domain module (students, programs, enrolment, assessment, fees, instructors). India (Frappe Technologies). 🔴 Copyleft: attach over its REST API rather than fork, the same posture this KB takes to Odoo and i-educar. 🔵 **Its grant was invisible to this base's ladder until this pass: the file is lowercase `license.txt` and the default branch is `develop`.** The sibling `frappe/lms` (AGPL-3.0) was already shelved — the ERP it is built on was not. |
| RosarioSIS | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | **GPL-2.0** (15,214 B ✅ first-hand, Version 2, `affero=0`) | 649 | Global | "RosarioSIS Student Information System for school management." 395 forks, PHP, with a GitLab mirror the README names as co-primary. 🔵 **A true SIS — enrolment, scheduling, grades, attendance, billing, discipline — which is a different product from an LMS and a category this page was thin on.** Widely deployed in Spanish- and French-speaking school systems; the project ships localisations including `es` and `fr`. 🔴 **GPL-2.0, not 3** — so it carries no patent grant and no §13, and it is *not* upgradeable-by-default. Attach, do not fork. Re-found `92` times, never shelved. |
| Gibbon | [GibbonEdu/core](https://github.com/GibbonEdu/core) | **GPL-3.0** (35,121 B ✅ first-hand — 🔴 **not AGPL**; sidebar agrees) | 636 | Global | "Gibbon is a flexible, open source school management platform designed to make life better for teachers, students, parents and leaders." 428 forks, PHP. 🔴 **This base's naive copyleft detector called it AGPL-3.0; the licence title line reads "GNU GENERAL PUBLIC LICENSE" and the three Affero mentions are GPL-3.0's own §13 cross-reference.** The distinction decides whether a hosted deployment owes source to its users — GPL-3.0 does not. Re-found `83` times, never shelved. |
| Odoo | [odoo/odoo](https://github.com/odoo/odoo) | **LGPL-3.0** (file, not sidebar) | 55,400 | EMEA | "Odoo. Open Source Apps To Grow Your Business." The canonical open-source ERP and the comparison point this KB is measured against. The sidebar names **no** licence; `LICENSE` on the default branch (`20.0`) states *"Odoo is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3)"*. A closed application may *link* it; modifications to Odoo itself stay open. This explains OpenEduCat's LGPL-3.0 by inheritance. Odoo SA is Belgian; the repository page does not state a location. |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | 3,400 | APAC | "Easy to use, 100% open source LMS." Built on the Frappe framework, so it inherits Frappe's ERP primitives. India. |
| OpenEduCat | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 902 | APAC | "Comprehensive Open Source ERP for Educational Institutes" — admissions, students, faculty, courses, exams, library, fees. **LGPL-3.0, not MIT/Apache**: linkable from closed applications, but modifications to it stay open. OpenEduCat's own website names Odoo as its underlying framework; the GitHub page never mentions Odoo. India. |
| i-educar | [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 | 722 | LATAM | *"Lançando o maior software livre de educação do Brasil!"* School management for Brazilian municipal education secretariats (*Secretarias de Educação*) and public schools. **The reference LATAM public-sector education platform** and the most important row here for a Brazilian government engagement. |
| Academico | [academico-sis/academico](https://github.com/academico-sis/academico) | **MIT** (licence file, 1,094 B) | 410 | Global | **The permissive education SIS this page spent three passes concluding did not exist.** "Laravel & Filament-based school management platform for small and medium institutions" — topic `student-information-system`, 151 forks, pushed 2026-10-30, copyright "Thomas Debay and project contributors". A client at this tier — language school, training institute, private school group — **can fork it, rebrand it and keep the derivative closed.** It is not a platform of record and should never be offered as a Moodle or OpenEduCat replacement at university scale; the 410★/151-fork ratio does say it is in real deployment rather than starred and abandoned. Region not stated; recorded Global. |
| Frappe Education | [frappe/education](https://github.com/frappe/education) | **GPL-3.0** (resolved from `license.txt`) | 687 | APAC | "Open source education / school management system." Note it is **GPL-3.0, not AGPL-3.0** like Frappe's other projects, and not LGPL like its OpenEduCat neighbour. Copyleft either way: attach, do not fork. India. |
| openSIS Classic | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | **GPL-2.0** (pinned) | 347 | North America | Web-based PHP/MySQL Student Information System. OS4ED (US). The README points to `docs/License.txt`, which is **GPL version 2, June 1991** — *not* GPL-3.0. The distinction is load-bearing: GPL-2.0 has no patent grant and is incompatible with GPL-3.0-only code. Default branch is `master`; there is no `main`. |

## Learning platforms used as the vertical system

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | APAC | The default institutional LMS worldwide; the vast plugin ecosystem is the customisation surface. Perth, Australia. |
| LearnHouse | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | **AGPL-3.0 + separate Enterprise Licence** | 2,400 | Global | "The Next-gen Open Source learning platform for everyone." Next.js / FastAPI / Postgres / Redis, 593 forks, ships "LearnHouse AI: The Teachers and Students copilot". **Added this pass.** The licence shape is the lesson: an AGPL core with features withheld under a commercial licence means the public repo is not the whole product — check feature parity before promising a self-hosted build. Maintainer Badr B. (`@swve`); country not stated. |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | EMEA | LMS built around ease of use and accessibility; notable francophone and LATAM deployments. |
| OpenOlat | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** (licence file `10,982 B`, read first-hand `p574`; `NOTICE.TXT` `14,712 B`) | 449 | EMEA | "Learning Management System OpenOlat," by **frentix GmbH, Switzerland**. A permissively licensed *institutional* LMS — rare, and one a commercial derivative could be built from. |
| Mentingo | [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** | 102 | **EMEA** | **The new permissive option, and the one to read carefully.** "Open-source AI-native LMS with AI Mentor & role-play. Self-hosted alternative to Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX." TypeScript, 31 forks, pushed 2026-10-30. Ships **SCORM and xAPI**; white-label is a stated goal; topics include `corporate-training` and `compliance-training`, so the natural fit is **enterprise L&D rather than a university registrar**. Selleo's GitHub profile states **Poland**. MIT per the API. At 102★ with 105 open issues it carries adoption risk a Moodle install does not — but it is the only AI-native LMS a client can fork, rebrand and keep closed. |
| ULEARN | [safytech/ulearn](https://github.com/safytech/ulearn) | **MIT** (licence file, 1,066 B) | 701 | Global | **The largest MIT-licensed LMS located anywhere**, 299 forks. And the stack is the whole story: **Laravel 5.8 + React 16.9**, both long past end of life. Permissive and forkable in principle; in practice a fork is a framework-upgrade project before it is a product. Quote the upgrade or do not quote the platform. |
| Richie | [openfun/richie](https://github.com/openfun/richie) | **MIT** (licence file, 1,079 B) | 318 | **EMEA** | A Django **CMS for building education portals**, designed to front Open edX and Moodle course catalogues. 94 forks. **Region placed from the licence file's own copyright line — "GIP FUN MOOC"**, i.e. France Université Numérique, the same publisher as the MIT LRS `openfun/ralph`. The catalogue-and-marketing tier of an institution's estate, permissively licensed, from a European public publisher. |
| ibl.ai LMS | [iblai/lms](https://github.com/iblai/lms) | **MIT** (licence file, 1,063 B) | 208 | Global | "Skills intelligence platform — discover courses, track competencies, earn credentials, accelerate workforce development." Next.js 15 / React 19, created 2026-03-04. **The first open-source asset located for the digital-credentials and skills-pathway trend**, which had been carried for three passes on a single standards-body source. Workforce-development buyer, not a registrar. |
| TutorLoom | [pacewisdomhq/TutorLoom](https://github.com/pacewisdomhq/TutorLoom) | **Apache-2.0** (licence file, 11,362 B) | 54 | APAC | Self-hosted **multi-tenant** LMS: course builder, trainer and student portals, progress tracking. Django + React + Flutter, created **2026-10-07** — three weeks old. Explicitly `moodle-alternative` and `corporate-training`. One of only **two** Apache-2.0 repositories in the world under `topic:learning-management-system` above 50★. Region inferred from the publisher and **not stated on the repo**, so treat the placement as soft. Too young to carry an engagement. |
| Euron Open LMS | [euron-sde-team/euron-open-lms](https://github.com/euron-sde-team/euron-open-lms) | **MIT** (licence file, 1,132 B) | 10 | APAC | Created **2026-10-26** — five days old, and recorded as a watch item rather than an option. Course catalogue, HLS-video classroom, quizzes, reviewed assignments, **verifiable certificates**, Stripe **and Razorpay** billing with subscriptions, Terraform for AWS. **Two India signals**: the copyright holder is "ENGAGESPHERE TECHNOLOGY **PRIVATE LIMITED**" and the Razorpay integration is India-specific. 16 forks on 10★ at five days is an unusual ratio and worth re-reading next pass. |
| FreeLingo | [artcc/freelingo](https://github.com/artcc/freelingo) | **AGPL-3.0** | 217 | — | Self-hosted AI language-learning platform: local or cloud LLMs, CEFR study plans, AI tutor, voice conversation, flashcards, spaced repetition. Technically the most complete vertical language-learning stack found — and **AGPL-3.0**, so it is an adopt-as-is system, not a build-on base. Author Arturo Carretero Calvo; **location not stated**, so no region is assigned. |

## Adjacent institutional systems

Not learning platforms, but always in the estate, and usually where an AI search
or discovery agent is actually pointed.

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| DSpace | [DSpace/DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** | 1,100 | North America | The institutional repository — theses, datasets, faculty output, grey literature. **The only permissively licensed platform of record in this KB.** Java; LYRASIS (US non-profit). |
| Koha | [Koha-Community/Koha](https://github.com/Koha-Community/Koha) | GPL-3.0 (or later) | 597 | Global | Integrated library system — catalogue, circulation, acquisitions. Contributions go through the project's **own bug tracker, not GitHub issues**. |

## Learning-analytics stack — a vertical system in its own right (new in the sixth pass)

**Every platform above is copyleft or near it, which is why this page's doctrine
is *attach, do not fork*.** The sixth pass found that the attach target with the
cleanest licence position is not an LMS at all — it is a **complete
learning-analytics stack, all MIT, all from one national public operator**, that
sits beside any of the platforms above and speaks a standard rather than touching
their code.

| Component | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| LRS (store) | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** (`main/LICENSE.md`, 1,094 B) | 51 | EMEA | Learning Record Store: ingests **xAPI** statements from any LMS, tutor or agent. The system of record for learner activity. |
| Dashboards | [openfun/warren](https://github.com/openfun/warren) | **MIT** | 17 | EMEA | xAPI learning-analytics dashboards over the LRS. Pushed `2026-10-11` — the active component of the three. |
| Dashboards-as-code | [openfun/potsie](https://github.com/openfun/potsie) | **MIT** (`main/LICENSE.md`, 1,094 B) | 11 | EMEA | **Grafana** dashboard suite written in **Jsonnet**, so dashboards are generated, diffable and code-reviewed rather than clicked together. Pushed `2024-12-18` — stable, not active. |

🟢 **Why this belongs on a page about vertical systems.** All three grants were
read byte-for-byte in the sixth pass and all three name the same holder —
*"Copyright (c) 2020-present / 2021-present **France Université Numérique**"* —
the French national public operator that also publishes `richie`. That makes this
**the strongest institutionally placed EMEA row anywhere in this KB**: the region
is read off the grant, not inferred from language or timezone.

🟢 **The engagement shape.** A client on Moodle (GPL-3.0), Chamilo (GPL-3.0) or
OpenEduCat (LGPL-3.0) cannot have a closed derivative of their platform. They
*can* have a **closed, white-labelled analytics product** built on this stack,
attached over xAPI, with no platform code touched and no copyleft reaching the
deliverable. 🔵 `scorm-again` (MIT) and `ltijs` (Apache-2.0) are the other two legs
of the same doctrine; this is the one that answers *"and what do the dean and the
registrar actually look at?"*

⚠️ **Two honest caveats before it is quoted.** `potsie`'s last push is
**December 2024** — the Grafana suite is stable rather than maintained, and
Grafana itself is **AGPL-3.0**, so the *dashboards* are MIT while the *runtime
rendering them is copyleft*: ship it as a deployed service, not as a linked
component in a closed product. And at 51/17/11★ this is a small-community stack —
credible because of who publishes it, not because of its adoption numbers.

🔴 **Recorded against this KB's own error.** This stack was already in the
repository while [`../repos/trending.md`](../repos/trending.md) was still
publishing *"no open-source learning-analytics dashboard"*. The components were
never missing; the index was wrong. See `568-A` in
[`../intel/open-gaps.md`](../intel/open-gaps.md).

## Self-hosted measurement-first learning platform (new in the seventh pass)

🟢 **A platform class this page has never carried: one whose selling point is
that it *audits whether learning happened*, not that it delivers content.**
Found at `stars:<50` on the band `568-C` named — **1★, 1,313 commits, 4 authors**
since `2026-08-31`, counted with `git rev-list`.

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| AI Learning OS (砚席) | [swsgbl/ai-learning-os](https://github.com/swsgbl/ai-learning-os) | ⚠️ **SPLIT — MIT root (`main/LICENSE`, 1,084 B) but `services/api/` carries AGPL-3.0 combination obligations.** See the carve-out below; **do not read this row as "MIT"** | 1 | **APAC** (by artefact, not by grant — see note) | Self-hosted, **server-authoritative** learning platform. Server owns timing, scoring and idempotent submission; **item projections exclude answers** (an "answer-isolation invariant"). An 11-stage learning-sprint state machine runs *contract → **equivalent pre/post test** → concept map → plan → core study → targeted practice → **transfer check** → post-test → report → spaced re-test*. Six-state mastery rule chain (3 independent pairs + 2 contextual + a delay/transfer pair) over **FSRS** scheduling. **Local ASR/TTS — the README states voice audio never leaves the machine.** BYOK multi-vendor LLM keystore (server-side encryption, last-4 display only, three-layer SSRF defence). Clients: Web PWA, Android, **HarmonyOS**. 🟢 **The part that matters for this KB:** a *learning-effect audit pipeline* with **CTT item analysis, mastery-simulation validity (publisher reports AUC 0.913), metacognitive calibration (gamma) and pre/post effect sizes — gated in CI.** |

### ⚠️ The licence carve-out, read from the publisher's own `NOTICE.md`

🔴 **A LICENSE-file read — this base's primary instrument — returns `MIT` for this
repository and that answer is dangerously incomplete.** `main/NOTICE.md` states
the split itself:

| scope | licence |
| --- | --- |
| `apps/android/`, `apps/harmony/`, `apps/web/`, `services/console/`, docs | 🟢 **MIT** |
| 🔴 **`services/api/`** | 🔴 **AGPL-3.0 combination obligation** |

🔴 **The mechanism is a single dependency, not a publisher's choice.**
`services/api` links **PyMuPDF (AGPL-3.0)** in-process to parse PDF textbooks.
`NOTICE.md` spells out AGPL-3.0 §13: *offer the service over a network and you
must give that service's users the complete corresponding source of your
deployment, modifications included.* Private local use does not trigger it.

🔴 **For Globant specifically this is a prohibition on the default path, not a
threshold.** A studio that hosts and operates a client's deployment of
`services/api` owes that deployment's source to its users — the same class of
finding as `Arize-ai/phoenix`'s Elastic License (`p568`), reached by a completely
different route.

🟢 **And the remedy is named, costed and small**, which is why this row is shelved
rather than rejected. `NOTICE.md` itself gives two exits: buy a commercial
PyMuPDF licence from Artifex, or **replace the parser**. The rest of
`services/api` is MIT-compatible by its own dependency table (FastAPI, SQLAlchemy,
Alembic, `py-fsrs`, `onnxruntime` all MIT; `rapidocr-onnxruntime` and CosyVoice
Apache-2.0; `httpx` BSD-3). **Swapping one PDF parser for a permissive one
(`pypdf`, BSD-3; `pdfplumber`, MIT) removes the AGPL obligation from the whole
platform.** That is a scoped engineering task, and it is the first thing to quote
on an engagement that wants this stack. Wired as `P-572-B`.

🔵 **On the region field, stated precisely.** The grant names *"AI Learning OS
contributors"* — **not an institution**, so this base's licence-holder instrument
(`p568`) does **not** place it. It is recorded **APAC on artefact evidence
instead**: a HarmonyOS / 深开鸿 client target, a `ChinaTextbook` catalogue
integration, and Chinese-language documentation throughout. 🔴 **Those are two
different grades of evidence and this page does not pretend otherwise** — see
`569-E`.

## Ninth pass (`p571`, 2026-10-31) — 🔴 two platform axes swept, no new platform; and `topic:mooc` is a large, correctly-named, nearly empty channel

🔴 **No row added.** Two axes never swept *for platforms* were opened —
[`topic:mooc`](https://github.com/topics/mooc) (**661** repositories) and
[`topic:language-learning`](https://github.com/topics/language-learning)
(**4.8k**) — and **every platform they returned is already on this page or on this
base**: `gazpachu/hypatia`, `INRIA/scikit-learn-mooc`,
`xiaochong0302/course-tencent-cloud`, `designfuchen/word-atlas`,
`mengxi-ream/read-frog`, `echo-loop/Echo-Loop`, `umlx5h/LLPlayer`.

🟢 **One grant newly read this pass:**
[`umlx5h/LLPlayer`](https://github.com/umlx5h/LLPlayer) is **GPL-3.0** at
**4,400★** — the media player for language learners carried on this page without a
licence column. ⛔ Copyleft; attach, do not fork.

### 🔵 The structural finding: a 661-repository axis named after a delivery model contains almost no delivery software

🔴 **Exactly two of `topic:mooc`'s top twenty are platforms, and both are
disqualified** — `gazpachu/hypatia` (**GPL-2.0**, 651★, README states the project
is *"currently in hibernation"*) and `xiaochong0302/course-tencent-cloud`
(**GPL-2.0**, 1,200★, already shelved). The other eighteen are:

- **Course materials and solution repositories** — `fastai/course-v3`,
  `INRIA/scikit-learn-mooc` (⚠️ **CC-BY-4.0**, a *content* licence on a code repo;
  EMEA/INRIA, France), Coursera assignment answers, algorithm-course sample code.
- 🔴 **Downloaders and attendance-automation scrapers** — `Foair/course-crawler`,
  `MoocDownloader/MoocDownloader`, and `cxOrz/chaoxing-signin`, which automates
  check-in on 学习通. **Tools built to extract from or game MOOC platforms, not to
  run them.**

🔵 **So an axis can be large, precisely named for the thing you want, and still
hold nothing shelvable — and that is a different result from an unswept axis.** 🟢
It is now measured rather than assumed, which is what stops a later pass buying it
again. 🔴 Note this is *not* the low-precision failure `P909` describes: `mooc`
is a single word but has **no meaning outside education**, so by `P923`'s
selection rule it should have been a good channel. **`P923` predicts precision,
not shelvability** — the rows are on-topic and still unusable.

🔴 **`topic:language-learning` (4.8k) yields no platform either, and its leaders
are consumer apps under copyleft** — `read-frog` **GPL-3.0** (10,200★),
`Echo-Loop` **AGPL-3.0** (4,600★), `LLPlayer` **GPL-3.0** (4,400★). ⛔ The AGPL row
is the one to flag to a studio that *hosts* client solutions: AGPL reaches a
hosted service, so it is a **prohibition, not a threshold**. 🟢 `word-atlas`
(3,500★) from that axis is **already on this page**, which serves as a negative
control confirming the sweep reached the right population.

## Eighth pass (`p570`, 2026-10-31) — no new platform qualified, and the content-grant lesson now belongs on this page

🔴 **Measured null, stated rather than left silent.** Four GitHub topic axes
never swept in 569 passes were queried this pass — `topic:rubric` (187 results),
`topic:spaced-repetition` (3.2k), `topic:academic-integrity` (121),
`topic:automated-grading` (49). 🔴 **None returned a vertical education platform.**
The eight new addresses they produced are **evaluation tooling and learning
apps**, shelved in [`../repos/foundations.md`](../repos/foundations.md). The
platform tier of this industry is not discoverable on capability axes — it is
found, as this page's own history shows, on `topic:lms`, `topic:sis` and
`topic:student-information-system` with a licence filter.

### 🔴 The finding this page must absorb: a content carve-out can live INSIDE the MIT file

🟢 `568-D` established the convention this page already applies — a single
`Licence` column plus an inline ⚠️ marker naming the carve-out. 🔴 **`p570` found
the sixth instance and a mechanism that defeats every check this base runs**, and
although the repository itself is a learning app rather than a platform, **the
mechanism is most dangerous here**, because a vertical education platform *ships
curriculum content* by definition.

[`designfuchen/word-atlas`](https://github.com/designfuchen/word-atlas)
(**3,500★ in six days**) carries `main/LICENSE` at **1,299 B** — standard MIT is
~1,068 — and the surplus is a `Scope:` clause in the MIT body itself:

> *"This license covers project code, original interface artwork, and technical
> documentation. Vocabulary learning content, third-party media, and generated
> recordings are governed separately by `CONTENT_LICENSE.md`."*

| scope | licence |
| --- | --- |
| code + UI design | **MIT** |
| Fraunces typeface | **SIL OFL 1.1** |
| wordlist (`data/`), illustrations, audio recordings | **CC BY 4.0** — *"to the extent of the rights the maintainers can grant"* |

🔴 **Three tiers, and the attribution-encumbered tier is the entire product
value.** 🔴 **Plus a disclosure that decides procurement:** the content was
produced by AI models — LLM text, image-model illustrations, **ElevenLabs
synthetic audio** — auto-validated and **not reviewed entry by entry**, supplied
as-is with **no accuracy warranty**, and the maintainers **hedge whether they
hold the rights they are granting.**

🔵 **The checklist item for every platform on this page, stated as a rule because
four separate mechanisms have now been catalogued:** a platform's grant must be
read for **four** carve-out shapes, and only the first is visible to a licence
API —

1. a **separate content licence** for datasets or curricula (`knowledge-graph`,
   `open-question-bank`);
2. a **per-directory** grant (`human-skill-tree`'s dual-licensed `skills/`);
3. an **obligation inherited from an in-process dependency**
   (`ai-learning-os`, AGPL-3.0 via PyMuPDF — *nobody chose it*);
4. 🆕 **a scope clause inside the permissive file's own body** (`word-atlas`) —
   which a `NOTICE` read, a per-directory check and a dependency audit **all
   miss**, because the file that limits the grant *is* the grant.

🔴 **The operational consequence for a client deliverable: if a platform ships
content, "MIT" on the repository is a statement about the code and about nothing
else, until the content tier has been read by name.**

## How to read this page

**The operations layer is copyleft almost without exception — but the exception
list has grown from three to nine, and that is this pass's correction.**
Permissive rows above: **Academico** (MIT, SIS), **ULEARN** (MIT, stale stack),
**Richie** (MIT, EMEA portal CMS), **ibl.ai LMS** (MIT, credentials),
**TutorLoom** (Apache-2.0, 3 weeks old), **Euron Open LMS** (MIT, 5 days old),
**OpenOlat** (Apache-2.0), **Mentingo** (MIT) and **DSpace** (BSD-3-Clause). Two
more permit linking from closed code (Odoo, OpenEduCat, LGPL-3.0). Everything
else — and every platform of record — is GPL or AGPL. 🔴 **CORRECTED `p585`: false — Sakai
(ECL-2.0), OpenOLAT (Apache-2.0), Kolibri (MIT) and relate (MIT) are permissive platforms
of record.** Note what the permissive
list is made of: **one row above 700★, three created in the last eight weeks, and
one on an end-of-life framework.** Permissive and *ready* are different claims. The AI-on-top strategy is therefore
not a matter of taste — it is forced by licensing:

1. **Do not fork the platform of record.** Under GPL/AGPL the derivative must be
   released; under AGPL that triggers on network use, which is how these systems
   are always deployed.
2. **Attach across a standard boundary instead** — LTI 1.3 via `ltijs`, LMS data
   via MCP, telemetry via xAPI into an LRS. All permissive. See
   [`../repos/foundations.md`](../repos/foundations.md).
3. **Where a permissive substrate is genuinely required**, the choice is now
   buyer-shaped rather than scarce: **OpenOlat** (Apache-2.0, 449★) for an
   institution, **Academico** (MIT, 410★) for a small or medium school,
   training institute or language school needing an **SIS**, **Mentingo** (MIT,
   102★) for AI-native corporate L&D, **Richie** (MIT, 318★) for the catalogue
   and portal tier, **ibl.ai LMS** (MIT, 208★) where **credentials and
   competencies** are the point, and **DSpace** (BSD-3-Clause) for the
   institutional repository. None of them is a platform of record, and saying so
   is part of the recommendation.
4. **Check for a withheld-features licence.** `learnhouse` is AGPL **plus** an
   Enterprise Licence. A dual-licence core is the one shape that looks open in a
   licence column and is not open in a feature matrix.
5. **Deliver courseware over SCORM, not only over LTI.** `jcputney/scorm-again`
   (MIT, 362★ — see [`../repos/foundations.md`](../repos/foundations.md)) is a
   maintained SCORM 1.2 / 2004 runtime. Every platform on this page ingests
   SCORM; it is what procurement asks for by name. Three passes of this KB built
   the attach doctrine without it.

## Declared gaps

- **No MIT- or Apache-licensed education ERP/CRM comparison exists.** The
  prescribed search `open source platform education ERP CRM MIT Apache` returned,
  for the **fourth** pass running, OpenEduCat's own marketing glossary (ten
  localised copies of two glossary pages) plus general-purpose CRMs — none
  education-specific. The *commentary* gap is now a settled property of the
  channel.
- **"There is no permissively licensed education ERP" was stated too broadly
  last pass, and this pass corrects it.** The finding holds for **ERP at
  platform-of-record scale**: that category is LGPL (OpenEduCat, Odoo) or
  GPL/AGPL (Frappe ×2, i-educar, openSIS) without exception, and a client wanting
  a proprietary derivative at that scale still builds on a *general* permissive
  ERP framework. It does **not** hold one tier down: `academico-sis/academico`
  (**MIT**, 410★, 151 forks, `student-information-system`) is a permissively
  licensed, actively maintained education SIS for small and medium institutions.
  **The correction matters because of how the earlier version was phrased** — as
  a conclusion "firm enough to state as a finding rather than a gap". It was
  firm about the wrong scope. The search that found the counter-example was an
  index query (`topic:lms license:mit stars:>80`), not a web search; the web
  channel returned the same vendor glossary for the fourth time.
- **The ERP/CRM commentary gap reproduced for a fifth pass, with the same
  artefact.** `open source platform education LMS SIS MIT Apache` returned
  **nine of ten results from `openeducat.org`** — the same vendor comparison and
  glossary pages in ten localisations that passes two through four recorded. At
  five consecutive passes this is no longer worth re-running: **the web channel
  has one answer for this query and it is an advertisement.** Index queries
  (`topic:lms license:mit`) are the only channel that has ever returned a
  counter-example here.
- **One genuinely useful thing the web channel did surface: Sakai.**
  [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) is **Apache-2.0**,
  stewarded by the **Apereo Foundation**, and originated in a 2004 consortium of
  Michigan, Indiana, MIT and Stanford. It is already recorded in
  [`../repos/foundations.md`](../repos/foundations.md) and is **cross-referenced
  here deliberately**, because it is the one *institutional LMS of record* with a
  permissive licence — and this page's central doctrine ("do not fork the platform
  of record") has a real exception in it that a reader of this page alone would
  miss. The honest qualifier from the same sources: Sakai has a **smaller
  community and slower release cadence** than Moodle, which is why it is not the
  default recommendation despite the better licence.
- **Two licence facts worth pinning, since both circulate wrongly.** Open edX is
  **AGPL-3.0**, not Apache — the MIT-and-Harvard origin story leads people to
  assume otherwise, and the licence is the opposite of what that history
  suggests. Canvas publishes its core under **AGPL-3.0**. Both are attach-only.
  `dotLRN`, which appears in older academic literature as an MIT-origin LMS, was
  **not verified this pass** and should not be offered to anyone.
- **No LATAM education ERP outside Brazil** surfaced again this pass. `i-educar`
  remains the single LATAM row and it is Brazil-specific.
- **Nextcloud (files) and Jitsi (conferencing) are still unverified.** Real
  systems, commonly paired with the above, outside what has been checked.
- **Four of the nine permissive rows are too young or too stale to recommend,
  and the page should not be read as nine options.** `TutorLoom` is three weeks
  old, `euron-open-lms` five days, `ibl.ai LMS` eight months, and `ULEARN` runs
  on two end-of-life frameworks. The genuinely usable permissive set today is
  **OpenOlat, Academico, Richie, Mentingo and DSpace** — and only DSpace is a
  category leader.
- 🔴 **No vertical platform was discoverable on a capability axis — a null worth
  recording so it is not re-run.** Four never-swept axes (`topic:rubric`,
  `topic:spaced-repetition`, `topic:academic-integrity`,
  `topic:automated-grading`; denominators `187 / 3.2k / 121 / 49`) returned
  **zero** platforms. 🔵 **This is the mirror image of the fifth pass's
  capability-sweep finding:** sweeping by capability finds the *horizontal*
  supply and the *tooling*; the platform tier only answers to platform topics
  with a licence filter. **Both axes are required, and they return different
  layers** — do not substitute one for the other.
- 🔴 **A fourth carve-out mechanism now exists and the page's reading rule is
  updated above.** `word-atlas`'s grant is limited by a `Scope:` clause **inside
  the MIT file**, which no instrument this base runs would catch — not the
  licence API, not a `NOTICE` read, not a per-directory check, not a dependency
  audit. 🔵 **For this page the exposure is structural rather than incidental:
  every platform here that ships curriculum, item banks or media has the same
  surface**, and only `knowledge-graph`, `evaluators`, `open-question-bank` and
  `ai-learning-os` have actually been read for it. **The remaining rows are
  unread on their content tier**, and that is a stated gap rather than a clean
  bill.
- **Mentingo's maturity is unverified beyond its metadata.** MIT, Poland, xAPI
  and SCORM are confirmed from the API and profile. Whether it can actually carry
  an institutional deployment — SSO, accessibility conformance, data residency,
  migration from Moodle — was **not** tested and should not be implied to a
  client from its presence on this page. 105 open issues on 31 forks is the one
  number that argues for caution.
