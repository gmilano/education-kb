---
industry: education
region: Global
updated: 2026-10-12
---

# Education — foundational repos

**Pass 139, 2026-10-12.** 🟢 **p138 measured a fifth layer — the published package — and found a
third of the connector tier shipping an SPDX identifier with no licence text. It then registered a
falsifier against itself, and this pass fires it: `ACTION CH` read every shipped text file in all
21 payloads, and 0 of the 9 licence-file-less packages carry their own grant in a source header.**
🔴 **p138's count stands.** 🔴 **A sixth layer is now measured, and it is the one a partial copy
depends on: per-file notice, practised by 1 of 21 rows.** On the other 20, a single file lifted out
of the tree names no holder and no grant. 🔵 **And the repository layer was measured in the same
pass as the payload layer for the first time** — through this KB's already-documented raw-file lane,
not a new one — re-verifying two of this KB's published licence figures byte-exact. Instrument and 24 tests:
[`p139-source-header-grant`](../compose/code/p139-source-header-grant/README.md).

**Pass 138, 2026-10-12.** 🔴 **p137 measured that a licence cell describes a repository root rather
than a whole tree. This pass measured a fifth layer, and it is the only one a client actually
receives: the published package.** `ACTION CD` downloaded **21** education-LMS connector tarballs
(Canvas, Moodle, Brightspace, EduBase), **sha1-verified every one against the registry's own
`shasum`** — 21 of 21 matched — and enumerated every shipped path.

| the layer | what it tells you | measured |
|---|---|---|
| root licence file | what you may do | 🟢 right about the **family** 92% of the time (`p444`) |
| tree enumeration | 🔴 **whom you owe** | 🔴 incomplete for **50%** of the largest rows (`p137`) |
| 🆕 **published payload** | 🔴 **what the client is actually handed** | 🔴 **9 of 21 packages ship NO licence file; 7 of those declare an SPDX id** |

🔵 **`npm install` unpacks a tarball; it does not clone a repository.** A grant that lives only at
HEAD is never conveyed to the person who installs the package — so a licence cell sourced from a
repository can be correct about the repository and wrong about the delivery.

🔴 **The row that matters most is the copyleft one.** `moodle-mcp-server-aql` **0.1.7**
(2026-10-01) declares **AGPL-3.0** across **141 shipped paths** and ships no licence text, while
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) carries a
canonical **34 523-byte** `LICENSE`. 🔵 The strongest obligation on this shelf, conveyed without the
document that states it.

🔴 **And the mechanism is now known rather than guessed**: `canvas-mcp-server` **2.2.3**'s packed
manifest reads `files: ["build/**/*", "README.md", "LICENSE", "package.json"]` — it **names**
`LICENSE` — and its 8 shipped paths contain none. npm omits a `files` entry that does not exist in
the tree, silently. 🔵 **New rule for this page: a manifest that lists a licence is not evidence
that one shipped.**

🟢 **Direction of the error, which decides the remedy.** All nine defective rows are the repository
being *better* than the distribution — **not one package shipped a licence its repository lacked**.
The ask to an upstream is a one-line `files` change, not a relicensing conversation.

Instrument, method, committed 21-row TSV and 7 passing tests:
[`p138-npm-payload-licence`](../compose/code/p138-npm-payload-licence/README.md).

🔴 **This probe reads licence FILES only**, so the `pipwerks` case — a grant in a source-file header
— stays invisible to it. **7 of 21 is a floor, not a count.** `ACTION CH` was registered to close
that hole at the repository layer and **did not run this pass**; it is re-registered.

🔴 **Scope, stated:** npm only, four platform families, one registry search each. PyPI, Maven and
crates were not probed, and `moodler-mcp` — a Python connector on this KB's shelf — **is not on PyPI
at all (404)**, so for part of the shelf there is no payload layer to measure and no registry to
arbitrate a disputed address.

**Pass 137, 2026-10-11.** 🔴 **Every licence cell on this page describes a repository ROOT, and for
half of the largest rows the root is not the whole obligation.** `ACTION BY` enumerated the file
trees of the **20 largest rows on this page** — **224 591 paths** — and found **316** licence-shaped
files outside the root, **242** of them real grants. 🔴 **Ten of the twenty (50%) carry at least one
grant whose copyright holder is not the repository's own.** The refutation threshold was **5%**.
Instrument, tests and per-row results: `compose/code/p137-foreign-holder-tree`.

🔵 **Read this next to [`p444-root-vs-tree-family`](../compose/code/p444-root-vs-tree-family/README.md),
which measured the other half of the same question and looks like it says the opposite.** p444: the
licence **family** read from the root file is the tree's family **92%** of the time. p137: the
**ownership** is incomplete in **50%** of the largest rows. 🟢 **Both are true, and together they
are the rule: a root licence cell predicts what you may DO; it does not predict whom you OWE.**

### 🆕 `ACTION BY` — what the trees carry, per row

| row | tree paths | non-root licence files | real grants | 🔴 foreign holders | verdict |
|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | **67 589** | 96 | 87 | 🔴 **66** | `FOREIGN_HOLDER_IN_TREE` |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 18 127 | 76 | 58 | 🔴 **13** | `FOREIGN_HOLDER_IN_TREE` |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 13 231 | 28 | 22 | 🔴 **17** | `FOREIGN_HOLDER_IN_TREE` |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 25 823 | 17 | 13 | 🔴 **10** | `FOREIGN_HOLDER_IN_TREE` |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 5 137 | 14 | 10 | 🔴 **10** | `FOREIGN_HOLDER_IN_TREE` |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 9 273 | 18 | 11 | 🔴 **9** | `FOREIGN_HOLDER_IN_TREE` |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 22 662 | 23 | 22 | 🔴 **4** | `FOREIGN_HOLDER_IN_TREE` |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 4 826 | 2 | 2 | 2 | `FOREIGN_HOLDER_IN_TREE` |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 17 073 | 6 | 1 | 1 | `FOREIGN_HOLDER_IN_TREE` |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 5 749 | 8 | 8 | 1 | `FOREIGN_HOLDER_IN_TREE` |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 7 405 | 13 | 8 | 🟢 **0** | `OWN_HOLDER_ONLY` |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | 2 489 | 1 | 1 | 🟢 **0** | `OWN_HOLDER_ONLY` |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 1 345 | 14 | 🟡 **0 readable** | 0 | 🟡 unreadable class |
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 664 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`frappe/lms`](https://github.com/frappe/lms) | 1 606 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 249 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | 118 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`openedx/codejail`](https://github.com/openedx/codejail) | 43 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | 193 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 692 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |

### 🔴 The two findings inside the 50% that change a delivery decision

🔴 **`instructure/canvas-lms` is AGPL-3.0 at the root and ships an MIT LTI Advantage implementation
four levels down.** `gems/lti-advantage/LICENSE.txt` is **MIT, held by a named individual (Nathan
Mills)**. 🟢 **The LTI Advantage code inside the dominant North-American LMS is the permissive part
of it** — which is a different sentence from anything this page has published about Canvas, and the
one a studio needs before it decides to reimplement rather than extract. (The same tree also carries
`rick olson`'s `attachment_fu` and `Coolite Inc.`'s date library.)

🆕 **`classroomio/classroomio` (AGPL-3.0) vendors ten MIT-licensed agent-skills packs** —
`skills/*/LICENSE`, held by three outside individuals. 🔵 **This is a 2026-shaped obligation**: the
skills are exactly the part a client redistributes, and their grants are not the platform's.

🔵 **The rest of the 50% is front-end vendoring and the FSF's own text**: Fonticons, Twitter's
Bootstrap, Tiny Technologies' editor, Michael Bostock's d3, Ivan Sagalaev's highlight.js, Adobe's
cmaps, the PDFium Authors, Google's Liberation data, Mozilla; plus **The Trustees of Columbia
University** and the Apache Software Foundation inside Sakai, and a Debian maintainer's packaging
copyright inside Kolibri. The FSF appears as a holder **21 times** — a vendored licence body, not a
third-party grant, and counted because a notice obligation attaches to it too.

### 🔴 Three defects this probe produced before it produced a finding — stated, because the first two were wrong in the direction of a finding

1. 🔴 **An empty path list counted as one path**, so seven of twenty rows were first reported as
   carrying a non-root licence file they do not have. `printf '%s\n' "$empty" | grep -c ''` is 1.
2. 🔴 **Sakai's `content-copyright` i18n bundles matched on the WORD "copyright"** and produced seven
   false grants out of translated UI strings.
3. 🔴 **A four-filename licence sweep over 16 candidate rows called `kstateome/lti-launch`
   unlicensed. Tree enumeration found `License.txt` — LGPL-3.0, 7 651 B.** One of this pass's two
   absence verdicts was false, which is `p288-agpl-casefold` biting this KB a second time, and is
   why the committed instrument matches case-insensitively and ships a regression test for it.

🟡 **And one limit that keeps 50% a floor rather than an estimate:** this instrument reads licence
**files**. A grant inside a source header — the `pipwerks` case p136 corrected — is invisible to it.
🔴 **`Crosstalk-Solutions/project-nomad` defeats the method entirely**: `ROOT_ONLY` over 664 paths,
while composing Kiwix, Kolibri and Ollama **as container images**, so its real third-party
obligations are nowhere in its tree.

### 🆕 One row added to the interoperability layer, and it is university-owned

| repo | licence *(payload-read)* | ★ | last push | holder class | why it is foundational |
|---|---|---|---|---|---|
| [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | 🟢 **LGPL-3.0** (`License.txt`, 7 651 B; `pom.xml` `<licenses>` agrees) | **UNMEASURED** | **2026-09-30** | 🟢 **US public university** (Kansas State University, Office of Mediated Education) | 🔴 **The only repository in this KB that maps a verified LTI launch onto a per-user OAuth grant** — `ltiSession.getEid()` → `OauthTokenService.getRefreshToken(userId)` → Canvas as that user. LTI **1.1** (OAuth 1.0a consumer model), Spring/Java, 34 paths. 🟢 **The first university-owned row in this page's standards tier**, and the pattern `P13` now copies. 🔴 LGPL + Java: port the pattern, not the file |

---

**Pass 135, 2026-10-11.** 🟢 **The assessment and course-content layer is added — the part of the
standards stack p134's interoperability section pointed at and did not reach.** p134 finished with
LTI, OneRoster, Ed-Fi and xAPI. Finishing the register (`ACTION BN`) found that **SCORM carries an
order of magnitude more code than any of them**, and that two of the six remaining standards have
almost no supply at all. Rows are below under *The assessment and content layer*.

🔴 **Every licence cell added this pass was established by hash, and the method matters more than
any single row.** `compose/code/p135-licence-sha-identity` discharges `ACTION BP` and **refutes its
premise**: not one payload in a 26-repo corpus is a whitespace variant of its canonical text. They
differ by **line wrap width** (SPDX wraps at ~105 columns, real `LICENSE` files at ~72), by
**typographic punctuation** (SPDX's GPL-3.0 uses curly quotes; shipped `COPYING` files use ASCII),
and by **the licence steward editing its own text** — two such edits are now known for GNU, the
`http`→`https` change and 🔴 **the FSF's move of `why-not-lgpl.html` from `/licenses/` to
`/philosophy/`, which was the entire remaining difference on five GPL-3.0 payloads.**
🟢 **Result: 21 of 26 resolved to a named SPDX identifier; the 5 that did not each have a named
cause, and 2 of them are correctly unmatched** because the text genuinely is not canonical.

🔴 **Two rows added this pass carry the defect this page exists to catch.**
[`pipwerks/scorm-api-wrapper`](https://github.com/pipwerks/scorm-api-wrapper) — **391★, 130 forks,
pushed 2026-09-18 — has no licence file under any of eight probed filenames**, and
[`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) is published
**unlicensed and archived by the US Department of Defense body that authored both SCORM and xAPI.**
Neither can be used in a client deliverable. Both are measured absent, not inferred.
<!--corrected by p136: see "The pipwerks correction" below. The `pipwerks` half of this paragraph is
wrong about rights and right about files -- a grant IS declared, in `package.json` and the source
header. The `adlnet` half is not re-measured this pass and stands as written.-->

## 🔴 The `pipwerks` correction — `ACTION BR`, and the sentence this page got wrong

**Pass 136, 2026-10-11.** `ACTION BR` asked for the **dependency closure** of the unlicensed
`pipwerks/scorm-api-wrapper` across this KB's own rows, predicting refutation *"if no published row
depends on it."* 🔴 **The action was discharged and it answered a bigger question than it asked: the
premise of five pages of this KB is wrong.**

| what p135 published | what p136 measured |
|---|---|
| *"no licence file exists under 8 probed filenames"* | 🟢 **TRUE.** Re-confirmed; the repository's whole tree is `package.json`, `readme.md` and three source files |
| *"there is no grant, so there is no right to use it"* | 🔴 **FALSE.** `package.json` carries `"license": "MIT-style license: http://pipwerks.mit-license.org/"`, and `src/JavaScript/SCORM_API_wrapper.js` lines 11–12 carry *"Copyright (c) Philip Hutchison / MIT-style license: …"* |
| *"391★, 130 forks, pushed 2026-09-18"* — a live dependency | 🔴 **HEAD commit is 2018-09-06.** The manifest version is `1.1.20160322`. `pushed_at` moved in 2026; the code did not |
| *"the blast radius is unmeasured"* | 🟢 **Measured. One** published row on this KB's pages depends on it |

🟢 **The one dependant, and how it hides.** Seven manifest types were probed across the 324 repo
rows on this KB's non-log pages; **150 rows exposed at least one manifest**, and the only
`pipwerks` hit in any of them is **pipwerks' own `package.json`**. 🔴 **A manifest probe is the
wrong instrument**: [`numbas/Numbas`](https://github.com/numbas/Numbas) (Apache-2.0, Newcastle
University) **vendors the file** at `runtime/scripts/SCORM_API_wrapper.js` — version
**`v1.1.20121005`**, four years behind upstream's own manifest — with the copyright and MIT-style
header **intact**. GitHub code search finds **293 files** named `SCORM_API_wrapper.js` carrying that
header, including [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) and
[`sr258/scorm-h5p-wrapper`](https://github.com/sr258/scorm-h5p-wrapper), both in the H5P family this
KB tables on `verticals/solutions.md`.

🔵 **So the rule this page should carry is about the grant's LOCATION, not its existence.** A
filename probe measures files. A grant can live in a package manifest, a source header, or a URL —
and when it travels inside a **vendored file**, the header travels with it while the version does
not. 🔴 **The residual risk is real but different from the one this page published**: the terms are
declared, *unread* (the host is refused in this channel — DNS failure on `http`, 403 CONNECT on
`https`) and **not an SPDX identifier**, since *"MIT-style"* names no standard text.

**Pass 134, 2026-10-11.** 🟢 **This page gains the layer it was missing: the interoperability
standards an institution procures against.** `instructure/ims-lti` has sat at the bottom of this
page for many passes, described correctly as *"the integration path that avoids touching platform
source"* — and this KB never followed that sentence anywhere. Followed, it leads to **`Cvmcosta/ltijs`
(Apache-2.0, 373★, pushed 2026-10-06)**, which is larger and far more active than the row that
pointed at it, and to the first **vendor- and government-owned** repositories this KB has ever
tabled. See the new section *The interoperability layer* below, and `agents/top.md` → *Standards-native
agents*.

🟢 **`ACTION BG` is also discharged on this page** — the mirror detector p133 asked for was built and
run, one of its three proposed signals works, and `P133-A`'s inference about Canvas is narrowed. See
*The mirror rule, measured* below.

**Pass 132, 2026-10-11.** p131's rows carried forward unchanged (they were verified hours earlier
in the same date window); 🔴 **one new row changes this page's headline recommendation and refutes
this page's own flagship gap** — see `README.md` → Pass 132, `P132-C`. These are the systems a
client already runs, or would sensibly adopt, and that AI work gets attached to. Licence is the
first column that matters: it decides whether Globant can ship a derivative at all.

🔴 **Read this before trusting a licence cell.** GitHub's `license.spdx_id` reports **`NOASSERTION`
("Other")** whenever its matcher does not recognise a `LICENSE` file as a known template. That is
*not* a finding of "no grant", and p130 published it as one. Where this KB has **read the payload**,
the payload wins and the cell below says so.

## The platforms

| repo | licence | stars | last push | origin | why it is foundational |
|---|---|---|---|---|---|
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | **9 241** | 2026-10-10 | North America (Blindside Networks, Canada) | The open virtual-classroom stack: WebRTC audio/video, whiteboard, breakouts, recordings. LGPL means linking is fine; modifying the library itself carries reciprocity. The place live-session AI (transcription, attention, summarisation) attaches. |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | **8 195** | 2026-10-10 | North America (Open edX / Axim) | The LMS + Studio behind MOOC-scale deployments. **Renamed:** this repo was `openedx/edx-platform`; the old URL still resolves and the README says "formerly known as edx-platform". Write the new name — earlier passes of this KB cite the old one. |
| [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | **7 473** | 2026-10-09 | APAC (Moodle HQ, Perth, Australia) | The most deployed LMS in the world, ~2 000 plugins. **Important for delivery:** this GitHub repo is a *public mirror* of `git.moodle.org` — pull requests do not go here, and it publishes no GitHub releases. Contribution goes through Moodle's own tracker and git server. 🟢 **Its mirror is live (pushed 2026-10-09), which is exactly why Canvas's frozen one was mistaken for a quiet project rather than a stopped job.** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | **6 863** | 2026-04-30 **(mirror frozen — not inactivity)** | North America (Instructure, US) | The dominant LMS in North American higher ed and the one with the richest third-party API surface — which is why every MCP connector on the agent shelf targets Canvas first. 🔴 **Corrected by p133: this KB called it "the quietest of the major platforms" for four passes and that was a measurement error.** The repo's own topics include **`gerrit-mirror`**, and `instructure/analytics` carries the identical `pushed_at` **one second later** (14:52:10 / 14:52:11 on 2026-04-30) — a batch export, not a human push. 🟡 **The correct statement: the public GitHub mirror has been frozen since 2026-04-30, so GitHub is not a usable activity signal for Canvas, and anyone diffing this tree to track upstream has been reading a stale copy for five months.** Development is in Instructure's Gerrit; `updated_at` still moves daily. |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** | **6 845** | 2026-10-11 | Global (Oppia Foundation) | An online learning platform built around structured, explorable lessons with built-in misconception handling. **The only major education platform under a permissive licence** — so the one a client can fork into a closed product without reciprocity. Underrated for exactly that reason. Android client: [`oppia/oppia-android`](https://github.com/oppia/oppia-android) (Apache-2.0, 418). |
| [`frappe/lms`](https://github.com/frappe/lms) | AGPL-3.0 | **3 299** | 2026-10-11 | APAC (Frappe, India) | Modern, actively developed LMS on the Frappe framework — so it sits next to Frappe/ERPNext finance and HR data without integration work. The strongest APAC-origin platform here. |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | AGPL-3.0 | 2 336 | 2026-10-11 | unplaced | Next-generation learning platform, Python/Next.js, AI features first-class rather than bolted on. Young, fast-moving. |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | AGPL-3.0 | 1 717 | 2026-10-11 | unplaced | Education platform aimed at companies running cohort training. Relevant to corporate-L&D engagements rather than academic ones. |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 1 237 | 2026-10-09 | North America (Apereo Foundation) | Long-lived Java academic LMS. ECL-2.0 is Apache-2.0 with an educational-community patent tweak — **permissive**, and the licence most people misread as restrictive. Strong fit where a client already runs Java/Oracle estate. |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | AGPL-3.0 | 1 127 | 2026-10-08 | EMEA (Overhang.IO, France) | The Docker-based Open edX distribution — in practice *the* supported way to stand up and upgrade Open edX. A large first-party plugin ecosystem, all AGPL-3.0: `tutor-mfe` (micro-frontends), `tutor-cairn` (real-time analytics), `tutor-discovery`, `tutor-credentials`, `tutor-jupyter`, `openedx-scorm-xblock`. If the engagement is Open edX, it is a Tutor engagement. |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | 1 141 | 2026-10-10 | Global (Learning Equality) | Offline-first learning platform for low- and no-connectivity classrooms; content syncs by LAN or USB. **MIT-licensed**, which with its offline design makes it the single best base for rural LATAM, African and South Asian deployments. Content tooling: [`learningequality/studio`](https://github.com/learningequality/studio) (MIT, 192). |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1 009 | 2026-10-10 | EMEA (Chamilo Association, Belgium) | LMS built around ease of use and accessibility, with real institutional adoption in Francophone Europe and Spanish-speaking LATAM. The most LATAM-relevant of the EMEA-origin platforms. |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read) | 886 | 2026-10-09 | APAC (India) | Education *ERP* — admissions, students, faculty, timetabling, fees — built on Odoo. The natural target for the administrative automation nobody else serves. 🔴 **Licence corrected by p131.** GitHub's API reports `NOASSERTION` and p130 published that as "review terms before use". This KB had already **read `master/LICENSE` in full — 8 241 bytes, genuinely LGPL-3.0** — and used that read to *retract* an even earlier "no grant" row. p130 reinstated the retracted claim by trusting the API field over its own evidence. **LGPL on an LGPL Odoo base: linking is fine, modifying the module itself carries reciprocity.** |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | 2026-10-10 | EMEA (Germany) | Mature German LMS with strong standards and accessibility compliance — relevant precisely because EMEA procurement weighs those heavily. |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **NOASSERTION** | 447 | 2026-10-09 | EMEA (frentix, Switzerland) | Java LMS widely deployed in Swiss/German universities. Licence reads as "Other" to GitHub (it is Apache-2.0-based in its own documentation) — **verify before building**. |

## The offline / low-connectivity stack (added by p132 — and it refutes this page's own gap)

🔴 **This page has carried, for several passes, that "the offline slot is the cleanest unclaimed
opportunity in this KB". It is not unclaimed.** It is occupied by the second-largest repository
anywhere in this KB.

| repo | licence | stars | origin | why it is foundational |
|---|---|---|---|---|
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 🟢 **Apache-2.0** | **39 444** | unplaced | **Offline-first knowledge and education server**: Wikipedia, thousands of books, courses, maps and optional local AI, all on hardware the client owns with no internet required. Architecturally a **Docker orchestration layer over containerised tools** — **Kiwix** powers the Information Library, **Kolibri** powers the Education Platform, **Ollama** powers the AI Assistant (the installer provisions Ollama on the host; an external OpenAI-compatible endpoint is also supported). 🟢 **Permissive, so a client can ship a derivative.** 850 commits, updated the day of this pass. |
| [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) | 🟡 **UNREAD** | 20 | unplaced | macOS / Apple Silicon port, bundling Ollama, Open WebUI, Kiwix, Kolibri and FlatNotes. Useful as a single-machine pilot before committing to the Docker stack. Licence not measured this pass. |
| [`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI) | 🟡 **UNREAD** | 2 | **APAC (India)** | Offline LMS for Class 10 Maths and Science on the Indian curriculum: FastAPI + React + RAG over structured chapter data with a local Ollama model, gamified quizzes, LAN-only operation, and a claimed Kolibri integration. 🔴 **Duplicate pair** with [`Tushar-cy/Ai-edge-learning-hub`](https://github.com/Tushar-cy/Ai-edge-learning-hub) (same owner, byte-identical description). Small, but the only row that targets a *named national curriculum* offline. |

🔵 **Why eleven passes missed it, and why the probe was not at fault.** p131 ran `kolibri stars:>2`,
got 86 repos, correctly resolved 3 to the Learning Equality family and 0 with AI. **The probe was
valid; the conclusion was false.** NOMAD *composes* Kolibri as a container and never names it in
its description — the dependency appears only in the README architecture. **A dependency is not
always visible in the metadata of the thing that depends on it.**

🟢 **What this changes for an engagement.** The low-connectivity offer stops being *"build an
offline tutor"* and becomes *"deploy and extend an Apache-2.0 stack that already composes content,
library and local inference"* — faster, cheaper and far more defensible in a procurement
conversation. Kolibri (MIT) remains the right content layer; what changed is that the integration
around it already exists. See `compose/patterns.md` → P2.

## Administrative automation — the first optimiser (added by p132)

| repo | licence | stars | origin | what it gives you |
|---|---|---|---|---|
| [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | 1 | **APAC (India)** | Conflict-free academic timetable generation under **India's NEP 2020**: electives, faculty availability, courses, rooms, balanced workloads, scenario simulation, manual overrides, exports, and a natural-language interface over MCP. 🟢 **The "most-cited driver, least-served tier" finally has a repo, and it is an optimiser rather than an LLM wrapper.** 🔴 One star — a reference design, not a dependency. |

## 🟢 The interoperability layer — how AI attaches without touching platform source *(new, p134)*

🔴 **Read this section before proposing a fork of anything above it.** Every platform in *The
platforms* is AGPL-3.0, GPL-3.0, LGPL-3.0 or ECL-2.0, and this KB spends a lot of words on which
reciprocity obligation bites when. 🟢 **The standards below make most of that moot:** a tool
launched over **LTI 1.3** runs as a separate application with its own licence, talking to the LMS
over HTTP. It never links platform code, so it inherits **no** copyleft obligation from Moodle,
Canvas or Open edX — and it is *invited in* by a client ID the institution issues and can revoke,
rather than holding a user's password.

| repo | licence | stars | last push | holder class | why it is foundational |
|---|---|---|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** (payload-read) | **373** | **2026-10-06** | named individual | 🟢 **The reference LTI 1.3 Advantage tool provider, and the headline addition to this page.** OIDC launch, Deep Linking, AGS grade passback, NRPS rosters. **1.8× the stars of `ims-lti` and pushed five days before this pass** — where `ims-lti` is Instructure's library for *their* platform, this is the platform-independent one. If an engagement puts AI inside an existing LMS, this is the integration dependency. |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** (payload-read) | 138 | 2024-08-18 | named individual | The Python LTI 1.3 Advantage library (Django/Flask). 🔴 **Dormant ~2 years**, and that is the most consequential staleness on this page: Python is where the agent frameworks live, so the LTI binding for an agent build is the least-maintained link in the chain. |
| [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** (payload-read) | 6 | **2026-10-09** | 🟢 **standards body** | Serves a **OneRoster 1.2 API from an Ed-Fi ODS**. The bridge between the two US K-12 data standards, written by the body that owns one of them. 🟢 **Stars are the wrong measure here: this is the row that makes a US K-12 rostering story procurement-safe.** |
| [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 **Apache-2.0** (payload-read) | 7 | 2026-07-30 | 🟢 **platform vendor (Google)** | Conformance tests for a OneRoster integration. 🟢 **The only test suite in this KB that proves an integration correct rather than asserting it.** |
| [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 🟢 **0BSD** (payload-read, 711 B) | 10 | 2026-05-11 | named individual (noreply addr) | TypeScript OneRoster SDK. 🟢 **0BSD — the most permissive licence in this KB; it drops even attribution**, so a derivative carries no notice obligation at all. |
| [`AlexMeiling/wiseflow-api-integration-packages`](https://github.com/AlexMeiling/wiseflow-api-integration-packages) | 🟢 **MIT** (payload-read; holder **"UNIwise ApS"**) | 3 | 2026-06-11 | 🟢 **platform vendor (EMEA, Denmark)** | Integration packages for the **WISEflow** assessment platform — user creation, flow setup, assessor allocation, **grade passback**. 🟢 **A European assessment vendor publishing its own MIT integration path**: the cleanest EMEA counterparty in this KB, and the opposite of the unsanctioned-connector problem. |
| [`openfun/warren`](https://github.com/openfun/warren) | **MIT** | 17 | **2026-10-11** | 🟢 **national public operator (EMEA, France)** | Learning-analytics visualisation over **xAPI**. Same owner as [`openfun/richie`](https://github.com/openfun/richie) below — 🟢 **France Université Numérique now gives this KB two MIT rows, and this one was pushed on the day of this pass.** The dashboard layer over an LRS. |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | 15 | 2025-08-29 | named individual | 🟢 **The only repo found that bridges an AI agent to a sanctioned standard**: an MCP server that records and retrieves learning activity through an xAPI Learning Record Store. 🔴 **15 stars, last push ~14 months ago** — load-bearing and unmaintained, which is precisely why it is a build item rather than a dependency. Full tier in `agents/top.md`. |
| [`adlnet/MasterObjectModel`](https://github.com/adlnet/MasterObjectModel) | **Apache-2.0** | 12 | 2025-07-03 | 🟢 **government (US DoD ADL Initiative)** | xAPI profile for lifetime learner tracking, from the body that authored xAPI. The modelling reference for an LRS schema. |
| [`mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK`](https://github.com/mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK) | 🔴 **no licence field** | 0 | 2026-04-14 | 🟢 **government (Minnesota Dept of Education)** | C# SDK for a US state's Ed-Fi ODS API. 🔴 **The best-owned row on this page and unusable, because it carries no grant** — the recurring shape of this KB in one line. |

🔵 **The licence asymmetry is worth stating plainly, because it inverts this page's usual advice.**
*The platforms* are copyleft almost without exception and the one permissive major platform
(`oppia/oppia`, Apache-2.0) is the one nobody asks for. 🟢 **The interoperability layer is
permissive almost without exception** — Apache-2.0, MIT and 0BSD, with named vendor and government
holders. **So the licence-safest way to build on a copyleft platform is to not build on it at all,
and to attach over a standard instead.**

🔴 **And the honest limit of this section:** these are libraries, conformance tests and profiles.
They are the plumbing a security review passes. **None of them contains any AI**, and the one row
that joins them to an agent has 15 stars and has not been pushed in over a year.

## 🟢 The mirror rule, measured — `ACTION BG` discharged *(p134)*

p133 corrected a four-pass claim that `instructure/canvas-lms` was *"the quietest of the major
platforms"*, having found the topic `gerrit-mirror` and a sibling repo sharing its `pushed_at` one
second later. 🟢 **`ACTION BG` asked for that to become a detector before any further freshness
claim published. It was built and run over the 40 most-recently-updated `instructure` repositories,
and the result is mixed in a useful way.**

| proposed signal | verdict | measurement |
|---|---|---|
| **a topic containing *mirror*** | 🟢 **WORKS — and the defect is a lane, not a row** | **5 of 40** repos carry `gerrit-mirror`: `canvas-lms`, `dockerfiles`, `switchman`, `screencap`, `outrigger`. `ACTION BG`'s refutation condition (*"refuted if `canvas-lms` is the only mirror"*) is **not met** |
| **two repos in an org sharing `pushed_at` to the second** | 🔴 **DOES NOT GENERALISE — retire it** | across 40 repos, **no timestamp is shared by more than one repo.** p133's own evidence was two *adjacent* seconds (`:10` and `:11`), not a shared one; generalised into a detector it finds nothing |
| **a README naming an upstream elsewhere** | 🟡 **NOT TESTED** this pass | would need a payload read per repo; the topic field is cheaper and sufficient |

🔴 **And the measurement narrows `P133-A`'s inference.** p133 concluded 2026-04-30 was *"the date
their export to GitHub stopped running"*. 🟢 **It was not: sibling mirrors in the same org received
exports on 2026-09-30 (`switchman`) and 2026-10-08 (`dockerfiles`)** — three days before this pass.
**The Gerrit export job is running; `canvas-lms` specifically stopped receiving it.** Whether that
is a disabled export, a renamed upstream branch or a deliberate halt is not visible from here, and
this KB should not guess. 🟢 **p133's operative conclusion survives intact and is the one to quote:
`pushed_at` on `canvas-lms` is not an activity signal.** Its stronger causal story does not.

🟢 **The control that makes the rule usable:** [`instructure/ims-lti`](https://github.com/instructure/ims-lti)
carries **no** mirror topic and was pushed **2026-10-02**. **So within one org, some repos are
mirrors and some are GitHub-native, and the topic tells you which.** `pushed_at` is a valid
freshness signal for `ims-lti` and an invalid one for `canvas-lms` — which means freshness must be
checked per repo, never per organisation.

### 🔴 p136 runs the rule over the whole corpus — and 44% of its hits are not mirrors at all

`ACTION BU` asked for p135's successor signal (README **byte-identity**, which p135 called *"a
verdict"* against licence grouping's *"lead"*) to be applied corpus-wide. **1 389 READMEs fetched
over 1 528 published rows → 71 byte-identical clusters, 25 of them cross-owner** — twelve times
`ACTION BU`'s refutation threshold, so **not refuted**. 🔴 **But the word "verdict" does not
survive:**

| lineage verdict | clusters | what it means here |
|---|---|---|
| `ALIAS` — **identical ref set** | 🔴 **11** | **One repository under two slugs.** GitHub keeps answering a renamed owner or repo name, so the "two owners" are one |
| `DIVERGED_FORK` — shared commit shas | 5 | A real fork; count the connector once |
| `FORK_AT_TIP` — same HEAD, different ref sets | 4 | A fork that has not diverged yet |
| `ATTRIBUTION_STRIPPED_COPY` — identical root tree, **zero** shared commits | 1 | the ENEM cluster (`ACTION BW`, below) |
| `SQUASHED_COPY` — one side a single commit | 1 | `0awei0/kt`, and it **dropped the upstream MIT file** |
| `UNRESOLVED` — measurement not taken | 🔵 3 | **said, not guessed** |

🔴 **One of the eleven aliases lands on a conclusion this KB published.** `agents/trending.md`
reasoned about `theopenem/OneRoster.NET` versus `jdolny/OneRoster.NET` — *"both licences name
`theopenem` as copyright … so pin `theopenem`"* — when the two slugs have an **identical ref set**
(`3f4540f9706d9099`) and are **one repository**. The pin is harmless; the reasoning was about a
distinction that does not exist. 🟡 `KI-Campus/LRS` and `openHPI/openLRS` are the same case across
*both* a rename and a transfer.

🔴 **And 37 further clusters are this KB citing one repository under two spellings** — `Elgg/Elgg`
and `elgg/elgg`, `Schroedinger-Hat/certo` under **three**, eight `Opetushallitus/*` pairs. That is
`p443`'s case-collision class measured across the whole corpus for the first time.

🟢 **The rule, generalised for this page.** Freshness must be checked per repo (p134).
**Identity must be checked before freshness**: resolve the slug to a repository by **ref set**, then
ask about forks, then ask about dates. Instrument, six verdicts and 10 tests:
`compose/code/p136-lineage-verdict/`.

## 🟢 The assessment and content layer — added by p135

The standards an institution procures against do not stop at rostering and grade passback. Two more
carry real code: **SCORM**, which packages and tracks course content, and **QTI**, which carries
assessment items. This is where an AI engagement touching *content* or *assessment* attaches.

| system | repo | licence *(hash-verified)* | ★ | pushed | owner | why it is foundational |
|---|---|---|---|---|---|---|
| **Adapt Framework** | [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | 🔴 **GPL-3.0** 🆕 *(p136: `UNMATCHED` → `RESOLVED` at ratio `0.997431`, holder **"2013 ADAPT LEARNING"**, 11 opcodes and not one an added clause)* | **630** | **2026-10-10** | Adapt community | The largest repo in the whole standards stack. Authoring toolkit producing responsive, accessible, multi-language courses that emit **both SCORM and xAPI**. 🔵 Copyleft: run it as a tool, do not link it |
| **OpenOlat** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟡 **Apache-2.0 + attribution** | **447** | 2026-10-09 | frentix GmbH / Univ. of Zurich | 🟢 **A full Java LMS this KB had never tabled**, with QTI, SCORM, curriculum management, assessment and lecture management built in. The permissive full-featured LMS this page's flagship gap says does not exist — see the verdict below |
| **scorm-again** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | **354** | 2026-10-09 | individual | The modern SCORM 1.2 / 2004 runtime. **Offline-first**, TypeScript, actively maintained. 🟢 **The permissive replacement for the unlicensed `pipwerks` wrapper** |
| **Numbas** | [`numbas/Numbas`](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0** | 215 | 2026-10-09 | 🟢 **Newcastle University (UK)** | Browser-based e-assessment, strongest in mathematics, SCORM-packageable. **Institution-owned and permissive** — the cleanest base for assessment work before the 2027 clocks. 🆕 **p136: it vendors `pipwerks`' SCORM wrapper** (`runtime/scripts/SCORM_API_wrapper.js`, `v1.1.20121005`, header intact) — the only `pipwerks` dependant on this KB's pages, and a reminder that Apache-2.0 at the root says nothing about a vendored subtree |
| **QTI 3 item player** | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** | 30 | 2026-04-07 | amp-up.io | The reference renderer for QTI 3 assessment items, with a four-component sibling family from the same vendor |
| **Mentingo** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 92 | **2026-10-10** | Selleo (PL) | 🟢 **An AI-native LMS under a permissive licence** — AI mentor, role-play, SCORM and xAPI, white-label, self-hosted. Small, but the only row where the AI is the platform's architecture rather than a bolt-on |
| **1EdTech validator** | [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) | 🟢 **Apache-2.0** | 17 | 2026-09-23 | 🟢 **1EdTech (the standards body)** | Conformance validation for **Open Badges and Comprehensive Learner Record**. The second conformance suite this KB has found, and the steward's own |

🔴 **Do not reach for these two, and the reason is the licence, not the code**

| repo | ★ | problem |
|---|---|---|
| [`pipwerks/scorm-api-wrapper`](https://github.com/pipwerks/scorm-api-wrapper) | **391** | 🆕 **p136: the reason changed.** The grant is **declared by reference** (`package.json` + source header, *"MIT-style license"* at a host refused in this channel) — so *"confers no rights whatsoever"* is withdrawn. Reach instead for `scorm-again` because **HEAD here is 2018-09-06** and *"MIT-style"* is not an SPDX id, not because there is no grant |
| [`cybercussion/SCOBot`](https://github.com/cybercussion/SCOBot) | 164 | **CC-BY-SA-4.0, and the file is only the 837-byte human-readable deed.** ShareAlike copyleft, no patent grant, and a content licence applied to code |

### 🔴 What this layer does NOT have

| standard | supply measured this pass |
|---|---|
| **Caliper Analytics** | 🔴 **One repository, 0★, no licence, last touched 2023.** The standard for carrying learning events to an analytics layer has no usable open-source client in any language |
| **Comprehensive Learner Record** | 🔴 **One real repository** — the 1EdTech validator above. The other two hits are an empty 2018 repo and a student project |
| **LTI Deep Linking**, probed alone | 🔴 **One repository, which declares in its own description that Deep Linking is not supported.** In practice it exists only inside `ltijs` |

## Supporting infrastructure

| repo | licence | stars | what it gives you |
|---|---|---|---|
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | 470 | The component framework for custom learning activities inside Open edX. Permissively licensed even though the platform around it is AGPL — so a custom XBlock is the lowest-friction way to put an AI activity inside Open edX. |
| [`openedx/codejail`](https://github.com/openedx/codejail) | **Apache-2.0** | 476 | Sandboxed execution of untrusted code. Directly reusable wherever an agent runs learner-submitted or model-generated code — an auto-grader for programming courses, for instance. |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | 354 | Modern SCORM/AICC/xAPI runtime in TypeScript. The bridge between legacy courseware a client already owns and anything new. |
| [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | 316 | Django/React CMS for building course catalogues and education portals in front of Open edX. From France Université Numérique, so it is proven at national scale in EMEA. |
| [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | **MIT** | 263 | The H5P interactive-content family (Norway); the Moodle binding is [`h5p/moodle-mod_hvp`](https://github.com/h5p/moodle-mod_hvp) (GPL-3.0, 157). The standard way to ship interactive activities into an existing LMS. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | 404 | Laravel/Filament school-management platform for small and mid-size institutions. MIT, so the most forkable administrative base here. |
| [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | **MIT** | 203 | LTI tool-provider/consumer library. LTI is how an external AI tool gets launched from inside any compliant LMS — the integration path that avoids touching platform source, and therefore avoids AGPL reciprocity entirely. |

## The system-of-record tier (restored by p131)

p130's declared gaps said *"`openeducat_erp` (licence unclear) and `academico` (small) are the whole
field."* 🔴 **They are not.** This KB read a system-of-record tier in an earlier pass and p130's
rewrite dropped it. Restored here, because "there is no open-source SIS" and "every open-source SIS
is copyleft" are completely different briefings for a client.

| repo | licence | why it matters | the catch |
|---|---|---|---|
| [`frappe/education`](https://github.com/frappe/education) | **NOASSERTION** (API) — read terms | **662★**, pushed 2026-10-05, 454 forks. Full school management on Frappe: students, programmes, fees, assessment. Sits beside ERPNext finance/HR with no integration work. | Licence does not resolve to an OSI identifier via the API; GPL-3.0 in the Frappe family's own documentation. **Read `LICENSE` before committing** — this is exactly the row class p130 got wrong. |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read) | 886★. The Odoo-based ERP; the broadest functional coverage of the tier. | Odoo module, so you inherit the Odoo ecosystem *and* its constraints. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | **404★**, pushed 2026-10-07. Laravel/Filament. **The only permissive SIS**, so the only forkable base for a closed client product. Carries the topic `student-information-system`. | Small, and aimed at small-to-mid institutions rather than a university of record. |
| **RosarioSIS** | GPL-2.0 | A genuine student information system with real deployments. | GPL-2.0 — the most restrictive option here. |
| **Gibbon** | GPL-3.0 | School platform with a long institutional track record. | GPL-3.0 reciprocity. |
| **openSIS** / **Fedena** | copyleft / mixed | Named in this KB's earlier reads of the tier; both long-lived. | Neither is permissive; verify the current edition's terms, since both have had commercial forks. |

🔵 **Provenance of the four rows without links.** RosarioSIS, Gibbon, openSIS and Fedena are
carried from **this KB's own earlier read of the tier** (`agents/trending.md:5160`, which recorded
`RosarioSIS mobile@899f6da` GPL-2.0, `Gibbon v31.0.00@683d2c4` GPL-3.0 and `OpenEduCat 19.0@1c95cef`
LGPL-3.0 at specific commits). 🔴 **They were NOT re-verified this pass and are deliberately listed
without links** — a row this pass did not measure does not get presented as one it did. Re-verify
before quoting them to a client; the three linked rows above were verified this pass and are in
`evidence/verified-repos.2026-10-11-p131.tsv`.

**The honest summary for a client:** there are **at least six** open-source systems of record. Exactly
**one** (`academico`, MIT) can become a closed derivative; one more (`openeducat_erp`, LGPL-3.0)
permits linking without reciprocity. The rest are GPL-family. 🔴 **So the gap is not supply — it is
that the system-of-record tier is almost entirely copyleft**, which is a licensing conversation at
the start of an engagement, not a missing-software conversation.

## How to choose, in one paragraph

If the client already runs a platform, the platform is chosen and the only question is the
attachment point: **LTI** (`ims-lti`) to stay outside the codebase and outside AGPL reciprocity, an
**XBlock** (Apache-2.0) inside Open edX, a **plugin** inside Moodle (GPL-3.0 reciprocity on the
plugin), or **MCP** against the platform API (see `agents/top.md`). If the client is greenfield and
wants to own a closed derivative, the shortlist is short because of licensing, not features:
**`oppia/oppia`** (Apache-2.0), **`sakaiproject/sakai`** (ECL-2.0), **`learningequality/kolibri`**
(MIT) and **`academico-sis/academico`** (MIT). Everything else on this page is copyleft, and the
AGPL rows commit a hosted-service client to reciprocal source release. 🟢 **And if the constraint
is connectivity rather than licensing, start from `Crosstalk-Solutions/project-nomad`
(Apache-2.0, 39 444★) instead of assembling the stack yourself** — it already composes Kolibri,
Kiwix and a local model, and it is permissive enough to fork.

## Declared gaps

- **No permissively licensed, full-featured LMS at the scale of Moodle or Canvas.** Oppia
  (Apache-2.0) and Sakai (ECL-2.0) are the permissive options and neither is a drop-in replacement
  for either. 🟢 **SURVIVES.**
- ~~**No open-source student information system of record.** `openeducat_erp` (licence unclear) and
  `academico` (small) are the whole field.~~ 🔴 **REFUTED by p131** — see the system-of-record tier
  above: at least six systems, read by an earlier pass and dropped by p130's rewrite. 🟢 **The
  surviving gap is that the tier is almost entirely copyleft, with `academico` (MIT) the lone
  permissive base — and that no AI *agent* targets any of them** (`agents/top.md`).
- **Canvas is the quietest major platform** (last push 2026-04-30, ~5 months) 🔴 **and it is now
  ~5.5 months quiet, unchanged on re-check this pass.** Worth raising explicitly before
  recommending it as an actively developed base — it is still the richest API surface in the
  sector, which is why every connector targets it.
- ~~**Three Kolibri-family repos, zero AI on any of them.** A valid re-probe this pass
  (`kolibri stars:>2` → 86 repos) resolves the family to three Learning Equality repos; the other
  83 are name collisions. **The offline slot is still the cleanest unclaimed opportunity in this
  KB** (`intel/trends.md` → T8).~~ 🔴 **REFUTED BY p132.** The family resolution was right —
  [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT, 1 141★),
  [`learningequality/studio`](https://github.com/learningequality/studio) (MIT, 192★),
  [`learningequality/kolibri-design-system`](https://github.com/learningequality/kolibri-design-system)
  (52★) — **and the conclusion drawn from it was wrong.**
  [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
  (**Apache-2.0, 39 444★**) runs Kolibri as its education container beside Kiwix and Ollama, and
  does not contain the string `kolibri` in its description. 🟢 **The surviving gaps are narrower and
  real: (a) no AI project builds *inside* Kolibri itself** — NOMAD orchestrates it from outside and
  the Learning Equality repos carry no AI; **(b) nothing offline targets LATAM.** The one
  curriculum-specific offline row found is Indian (`Tushar-cy/Offline-AI`), and LATAM — where this
  KB argues offline is a first-class requirement rather than an edge case — has none.
  🟡 **Also note a new collision source: Aleph Alpha ships a 78B model called "Kolibri".**

### 🟡 p135's verdict on this page's flagship gap

- **"No permissively licensed, full-featured LMS at the scale of Moodle or Canvas."**
  🟡 **NARROWED, and honestly it is weaker than it was.**
  [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) is **447★**, pushed 2026-10-09, under
  **Apache-2.0** (with two attribution statements replacing the appendix — permissive in effect),
  and it ships QTI, SCORM, curriculum management, assessment and lecture management in one Java
  codebase. It is a real, maintained, permissive, full-featured LMS, and **this KB had never listed
  it.** 🔴 **The gap survives only in its "at the scale of Moodle or Canvas" clause** — OpenOlat is
  447★ against Moodle's order of magnitude more, and its deployment base is concentrated in
  German-speaking Europe. 🔵 **For an EMEA engagement that clause may not matter**, and this is now
  the first permissive answer this page can give to *"we want off Moodle's GPL."*
- 🆕 **The offline gap gains a permissive component it did not have.**
  [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (MIT, 354★) lists `offline-first`
  among its own topics and implements the SCORM runtime client-side. 🟢 **That is the missing piece
  between `T8`'s offline requirement and standards-tracked course delivery** — a learner can
  complete tracked content with no connectivity and reconcile later. It still does not close *"no
  AI project builds inside Kolibri itself"*, and it still is not LATAM-originated.

### 🆕 Gaps this page opens after p135

- ~~**The sector's most-used SCORM library is unlicensed, and the blast radius is unmeasured.**~~
  🟢 **CLOSED AND CORRECTED by p136 (`ACTION BR`).** A grant is declared (manifest + source header);
  the blast radius on this KB's own pages is **one row**, `numbas/Numbas`, by **vendoring** rather
  than by manifest; and the sector-level reach is **293 files** carrying the header. 🔴 **What
  replaces it is narrower**: the declared body is unreadable in this channel and *"MIT-style"* is
  not an SPDX identifier, so the row's terms are *declared and unread* — and `pipwerks`' HEAD commit
  is **2018-09-06**, which makes it a stale dependency regardless of its licence.
- 🔴 **No permissive Python library exists for Open Badges.** Both Python rows are copyleft
  (LGPL-2.1 and LGPL-3.0). The permissive credential work is in **Rust** (`impierce`, Apache-2.0)
  and **Java** (`1EdTech`, Apache-2.0), which is a language mismatch for most AI engagements.

### 🆕 Gaps this page opens after p136

- 🔴 **This page's dependency picture is manifest-shaped, and the sector's is not.** `ACTION BR`
  measured 150 of 324 rows exposing at least one of seven manifest types; the one dependency that
  mattered was **vendored**, invisible to all seven. Until a tree-level probe runs (the instruments
  exist — `compose/code/p275-tree-enumeration`, `p441-tree-licence-enumeration`), **every "no
  dependants" statement on this page is a statement about manifests**.
- 🔴 **A root licence says nothing about a vendored subtree, and this page tables root licences.**
  `numbas/Numbas` is Apache-2.0 at the root and carries an MIT-style third-party header four levels
  down. Of the 24 rows in this page's platform and standards tables, **the number whose vendored
  subtrees have been read is zero.** 🔵 **This is `p969-root-only-licence-reach` one level deeper.**
  p93 measured that the grant ladder cannot see a **per-directory** licence (`bncc-dados`: code at
  the root, data one directory down). p136 measures that it cannot see a **third-party header inside
  a vendored file** either — same blind spot, and the vendored case is the common one in a sector
  whose code moves by copying.
- 🟡 **Three `UNRESOLVED` lineage clusters remain** (`education-ai-suite`, `OpenPronounce`,
  `agents-radar`). Each needs one clone per side; none is an education-supply row, which is why they
  were left — recorded so the 25-cluster figure is not read as 25 resolved.
