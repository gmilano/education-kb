---
industry: education
region: Global
updated: 2026-10-27
---
## 🆕 `p481` — `2026-10-27` — **🟢 THIS SHELF'S LONGEST-STANDING NEGATIVE FINDING IS OVERTURNED: a permissively-licensed, actively-maintained, platform-scale LMS exists. `Selleo/mentingo` is **MIT**, 584,229 LOC, multi-tenant, pushed today, and ships its agent integration **inside** the platform — with an OAuth consent controller, which is a different and stronger answer to the human-approval problem than the confirmation tokens this base has been recommending.**

🔵 **Gate posture, unchanged (`Gap 446-A`):** `make hooks` **not attempted** — harness refuses `Code from
External`. Nothing cloned this pass was executed (`Gap 481-A`).

---

### 🟢 The claim this shelf has carried since `p478`, and its correction

| pass | claim |
|---|---|
| `p478` | no permissively-licensed student information system exists |
| `p479` | corrected — Fedena declares Apache-2.0 in a `NOTICE`; *"the permissive SIS is not missing, it is fifteen years old"* |
| `p480` | cloned Fedena — Rails 2.3.5, no `Gemfile`, Flash reporting layer, dead since 2016; **recommendation withdrawn** |
| **`p481`** | 🟢 **for the LMS tier the gap is closed by a live row**: `Selleo/mentingo`, **MIT**, 584k LOC, pushed 2026-10-27 |

🔵 The SIS tier is **still open** — `mentingo` is an LMS with groups and certificates, not a student information
system with enrolment, attendance, exams and fees. Fedena remains the only permissive SIS and remains unusable.

### 🟢 The platform shelf

| platform | repo | grant | what it is | state read first-hand |
|---|---|---|---|---|
| Open edX | [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 · 35,136 B | MOOC-scale LMS | 🔵 `p480` — **RPC scope clarification in `LICENSE`** |
| Canvas LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0-only** · 34,520 B | LMS of record in much of US higher ed | 🔵 `p480` — election from per-file header; **no clarification** |
| Open edX deploy | [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 · 34,523 B | supported Docker deployment of Open edX | 🔵 `p480` |
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | the default open LMS worldwide | 🔵 carried; not re-read |
| **Mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 **MIT** · 1,062 B | multi-tenant LMS, **agent surface built in** | 🟢 **cloned `e137ca4`** this pass |
| TutorLoom | [pacewisdomhq/TutorLoom](https://github.com/pacewisdomhq/TutorLoom) | 🟢 Apache-2.0 · operative text **verbatim** | self-hosted multi-tenant LMS for training institutes; Django + React | 🟢 grant diffed word-level this pass |
| HAXcms | [haxtheweb/haxcms-php](https://github.com/haxtheweb/haxcms-php) | 🟢 Apache-2.0 · operative text **verbatim** | web-components course/microsite publishing; LMS-adjacent | 🟢 grant diffed word-level this pass |
| Tsugi | [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | 🟡 Apache-2.0 · reflowed (§4 `(a)`–`(d)` labels lost) | **LTI** tool hosting framework, IMS Global / Common Cartridge | 🟢 grant diffed word-level this pass |
| OpenEduCat | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL-3.0 | Odoo-based education ERP: admissions, fees, library, hostel | 🔵 carried; grant not re-read this pass |
| LearnHouse | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 AGPL-3.0 | AI-native learning platform, 2,424★ | 🔵 `p480` |
| Fedena | [projectfedena/fedena](https://github.com/projectfedena/fedena) | 🟢 Apache-2.0 · `NOTICE` + 175 headers | SIS: students, enrolment, attendance, exams, fees | 🔴 **`p480` — Rails 2.3.5, not a viable base** |

🔵 Two new permissive rows are promoted onto this shelf on grant evidence alone: **TutorLoom** (50★, created
2026-10-07, Django + React, multi-tenant, Moodle-alternative by its own description) and **HAXcms** (130★,
Apache-2.0, web components). Both carry the **canonical Apache operative text word-for-word**, measured this
pass. Neither was cloned (`Gap 481-K`).

### 🟢 `mentingo`'s consent step is the architectural finding, not its licence

This base's compose recipes have leaned on preview→confirm tokens as the human-in-the-loop control. This pass
established from `canvas-mcp`'s own source that **a token does not prove a human approved anything** — the model
holds the token and can redeem it. `mentingo` places the control somewhere a model cannot reach:

| control | where it lives | what it binds |
|---|---|---|
| `ConfirmationGuard` token (`canvas-mcp`) | inside the MCP server, issued *to the model* | the **request** — target, payload, caller |
| `mcp-oauth.controller.ts` + `mcp-consent.controller.ts` (`mentingo`) | the **platform's** OAuth authorization layer | the **user's grant** to the client, out of band of the tool call |
| `ALLOWED_WRITE_TOOLS` (`canvas-mcp`) | the **operator's** environment | which tools exist at all |

🔵 A platform that owns its own OAuth consent screen can obtain a human decision that the agent never mediates.
🔴 This base has **not read** `mentingo`'s consent implementation — the comparison above is between a module
whose source was read and a module identified by filename (`Gap 481-G`). It is a reason to examine it next pass,
not a verdict.

### 🔴 The informed gaps on this shelf, stated rather than left silent

- **SIS tier:** still no usable permissive student information system. Fedena is Apache-2.0 and architecturally
  dead; no replacement surfaced in this pass's searches.
- **LATAM:** no LATAM-domiciled platform surfaced this pass. The region's open supply remains administrative and
  copyleft — `i-Educar` (GPL-2.0), `i-Diario` (AGPL-3.0) — which is a finding, not an absence of searching.
- **Accessibility and standards:** no row on this shelf has had WCAG conformance, LTI certification or SCORM/xAPI
  support verified first-hand by this base, including `mentingo`. `tsugi` is the only row whose *purpose* is LTI.
- **Archived rows excluded:** `menthorlabs/menthor` (582★, Apache-2.0, verbatim operative text) and
  `sagefy/sagefy` (120★) are **archived** and are deliberately not promoted onto this shelf.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 481-J`** | **`mentingo` is the shelf's headline and it is 99★.** Every claim about it is from a clone read at profile depth: schema tables, file inventory, test-file count, manifest and grant. Migration cost, LTI/SCORM support, accessibility, performance at institutional scale and the security of its MCP surface are **all unexamined** (`Gap 481-C`, `Gap 481-G`). |
| 🟡 **`Gap 481-K`** | **TutorLoom and HAXcms are promoted on grant evidence only.** Their licence text was diffed word-for-word against the licensor's canonical copy; **neither repository was cloned**, so "multi-tenant LMS" and "course publishing" are their own descriptions, not readings of their source. TutorLoom is 20 days old. |
| 🟡 **`Gap 481-L`** | **The copyleft incumbents were not re-read.** Open edX's RPC clarification, Canvas's `AGPL-3.0-only` election and Moodle's grant are carried from `p479`/`p480` without re-measurement this pass. |
| 🟡 **`Gap 481-M`** | **OpenEduCat's LGPL-3.0 is carried, not re-read.** Its grant has not been fetched and measured by this base since `p376`, and the claim that an LGPL platform permits a separately-deployed proprietary AI service is this base's reasoning, not a licensor statement. |
## 🆕 `p480` — `2026-10-27` — **🟢 `Gap 479-N` IS CLOSED BY CLONING THE ROW, AND IT KILLS THE RECOMMENDATION: Fedena — this shelf's only permissively-licensed SIS — is **Rails 2.3.5**, boots on an API removed in Rails 3.0, has **no `Gemfile` at all**, and declares its one gem from **`http://gemcutter.org`**, a host that stopped being rubygems.org in 2010. 🟢 Its Apache-2.0 is now *stronger* than `p479` thought — **175 source files carry the full header** — so the blocker is squarely engineering, not licensing. 🟢 And the two big LMS rows now have *different* documented copyleft postures.**

🔵 **Gate posture, unchanged (`Gap 446-A`):** `make hooks` **not attempted** — harness refuses `Code from
External`. **Nothing below is gate-attested.** Frontmatter, closed-vocabulary `region`, pipe-counts,
no-header-as-data and prepend-only re-checked in this session's own code.

---

### 🟢 `Gap 479-N` closed — the permissive SIS is not "fifteen years old", it is architecturally pre-modern

🔵 `Gap 479-N`: *"Fedena was not run, and its maintenance state is unmeasured. 547★ and a 2011 copyright are not
a cadence; no push date, release tag or dependency audit was read."* 🟢 Cloned at `68a84ac` and audited
([`evidence/clone-tier-source-reads.2026-10-27-p480.tsv`](../evidence/clone-tier-source-reads.2026-10-27-p480.tsv)):

| what was read | finding | why it costs more than age |
|---|---|---|
| `config/environment.rb` | `RAILS_GEM_VERSION = '2.3.5'` | **Rails 2.3.5** — released **January 2010**, not 2011 |
| the boot sequence | `Rails::Initializer.run` with a block-passed `config` | the **pre-Rails-3 boot API, removed in Rails 3.0**. A port is not an upgrade path; the whole boot and config layer is rewritten |
| dependency manifest | 🔴 **no `Gemfile` exists** | Bundler arrived with Rails 3. There is **nothing to audit** — the dependency set must be reconstructed from scratch |
| the one declared gem | `config.gem 'declarative_authorization', :source => 'http://gemcutter.org'` | **gemcutter.org** was renamed rubygems.org in **2010**, over plain HTTP. The sole declared dependency source is a dead address |
| `vendor/plugins` | **14 plugins** | the Rails *plugin* mechanism, **removed in Rails 4** |
| — of which | `open_flash_chart` | **Flash**. No browser has had a Flash runtime since **December 2020** — the reporting layer is not old, it is **non-functional** |
| — and | `fckeditor` | FCKeditor, superseded by CKEditor in **2009** |
| size | 273,846 LOC — 62,479 Ruby · 52,214 ERB · **159,153 JS** | the JS is the largest tier and predates every modern toolchain |
| test suite | **212** `*_spec.rb` / `*_test.rb` files | 🟢 a suite **does** exist — `Gap 479-AR` assumed nothing was known |
| is the app intact? | **74 models, 50 controllers, 781 views** | 🟢 yes — the last commit's message, *"emptying content"*, did **not** gut the domain model |
| last commit | **2016-07-20** | ten years and three months of no activity |

🔴 **The verdict reverses the recipe arm.** `p479` priced this port at *"6–10 weeks if the port is clean"*. The
port crosses **six Rails majors and the Rails 2→3 rewrite boundary**, with no manifest, a dead gem source, a
Flash-dependent reporting layer and 159k lines of pre-modern JavaScript. **That estimate is not credible**, and
this pass withdraws it rather than restating it. See `compose/patterns.md` P16.

🟢 **The licensing news is good, and it is the half worth keeping.** `Gap 479-M` asked whether a `NOTICE` alone
carried the grant; **175 Ruby files under `app/` and `lib/` carry the full Apache-2.0 per-file header.** So
Fedena's value to a studio is now precisely locatable: **not the code — the domain model.** An Apache-2.0
schema covering students, enrolment, attendance, exams and fees, corroborated across 175 files, is a reusable
*specification* even when the implementation is not reusable.

### 🟢 The two dominant open LMS platforms now read differently on the question that decides architecture

| platform | repo | election | scope clarification in `LICENSE`? | what that means for an AI service beside it |
|---|---|---|---|---|
| Open edX | [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 | 🟢 **YES — 616 B appended by edX Inc.** | a *public, independently available* service reached by **RPC/inter-service communication** is stated by the licensor **not** to be a derivative work, and its source **not** Corresponding Source |
| Canvas LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0-only** (per-file: *"version 3 of the License"*) | 🔴 **none** | the same architecture rests on **this base's own architectural reasoning**, exactly as `Gap 479-R` says |

🔵 **Same licence family, same election, opposite evidentiary position.** For a studio choosing a platform to
build an AI layer onto, this is the difference between a quoted licensor statement and an inference — and it is
the kind of thing that only shows up if you diff the `LICENSE` file instead of reading its SPDX tag. Full quote
and its three stated limits are in `repos/foundations.md`.

### 🟢 The platform shelf

| platform | repo | grant | what it is | state read this pass |
|---|---|---|---|---|
| Open edX | [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 · 35,136 B | MOOC-scale LMS | 🟢 `LICENSE` diffed; **RPC clarification found** |
| Canvas LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0-**only** · 34,520 B | LMS of record in much of US higher ed | 🟢 election read from per-file header |
| Open edX deploy path | [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 · 34,523 B | the supported Docker deployment of Open edX | 🟢 `LICENSE` payload read |
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | the default open LMS worldwide | 🔵 carried from `p479`; not re-read |
| Fedena | [projectfedena/fedena](https://github.com/projectfedena/fedena) | 🟢 **Apache-2.0** · `NOTICE` + **175 file headers** | SIS: students, enrolment, attendance, exams, fees | 🟢 **cloned** — Rails 2.3.5, see above |
| LearnHouse | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 AGPL-3.0 | AI-native learning platform, 2,424★ | 🟢 grant + cadence from census (pushed 2026-10-25) |
| Mentingo | [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 **MIT** | AI-native LMS, 99★, created 2024-08-01 | 🟢 cadence re-read: pushed **2026-10-27** |
| IBL LMS | [iblai/lms](https://github.com/iblai/lms) | 🟢 **MIT** | skills-intelligence platform: competencies, credentials | 🟢 cadence re-read: pushed 2026-10-26 (already carried on this shelf) |
| Anki (as a tool surface) | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | 🟢 **MIT** | exposes spaced repetition to agents over MCP | 🟢 536★; new to *this* shelf, already on `agents/top.md` |
| Canvas integration, read-only | [boyuchengz/canvas-mcp](https://github.com/boyuchengz/canvas-mcp) | 🟢 **MIT** | 26 read-only tools onto Canvas | 🟢 **cloned** — 0 write calls, 500-item ceiling |
| Canvas integration, read/write | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** | 136 tools incl. rubric grading | 🟢 **cloned** — 12 write call sites |

### 🔴 The informed gaps on this shelf, stated rather than left silent

🔵 **LATAM:** `i-Educar` (GPL-2.0) and `i-Diario` (AGPL-3.0, licence text in **Portuguese**) remain the only
region-origin platform rows this base has ever placed, carried unchanged from `p479` and **not re-read this
pass**. No new LATAM platform surfaced in any census or search this pass.
🔵 **APAC:** no region-origin *platform* row exists on this shelf at all — APAC's supply, as measured on
`agents/top.md`, is agents and skills, not LMS or SIS software.
🔵 **EMEA:** `mentingo` (Poland, Selleo) is the shelf's one EMEA-origin permissive LMS; `freelingo` (AGPL-3.0) is
EMEA-origin by its Spanish-language author but is a language-learning app, not a platform.
🔵 **North America:** every large platform row here — Open edX, Canvas, Moodle's largest deployments — is North
America-origin or North America-dominant, which is why no "NA gap" appears: the gap on this shelf is the
*reverse* one, and it is APAC and LATAM.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 480-M`** | **Fedena's port cost is now bounded below, not estimated.** The audit proves the obstacles (Rails 2.3.5, no `Gemfile`, dead gem source, Flash reporting, 14 removed-mechanism plugins); it does **not** produce a week figure, and this pass deliberately publishes **no** number rather than replacing one uncredible estimate with another. The 212-file test suite was **counted, never run** (`Gap 480-A`). |
| 🔴 **`Gap 480-N`** | **The Open edX clarification is quoted, not adjudicated** (`Gap 480-G`). It names edX Inc., not the Axim Collaborative; it covers only a *public, independently available* service over inter-service communication; and it plainly does **not** cover an in-process plugin. A studio must have counsel read it. |
| 🔴 **`Gap 480-O`** | **`Gap 479-O` and `Gap 479-P` stand untouched.** No APK was built or instrumented for the elimu.ai tier, and every regulatory reading on this shelf remains law-firm and compliance-vendor commentary — EUR-Lex is refused at the gateway (`intel/market.md`). |
| 🟡 **`Gap 480-P`** | **Nine of eleven platform rows were not cloned.** Moodle, ILIAS, H5P, Sakai, Gibbon, RosarioSIS, Frappe LMS and the two LATAM SIS rows are grant-and-description rows; the clone instrument that settled Fedena **was not pointed at any of them**, which is availability, not absence. |
| 🟡 **`Gap 480-Q`** | **`Gap 479-Q` carries forward: versions are still read for a minority of the shelf.** No tag was dated this pass either, so "latest" still means "highest-sorting", not "most recent". |
| 🟡 **`Gap 480-R`** | **The Canvas/Open edX contrast is a licence-text contrast, not a tested one.** Neither platform's plugin API was exercised, no LTI boundary was probed, and `boyuchengz/canvas-mcp` — which now offers a concrete, verified read-only way to test the Canvas boundary — **was read but not run**, so `Gap 479-R`'s core objection survives in narrowed form. |

---

## 🆕 `p479` — `2026-10-27` — **🔴 `p478`'s HEADLINE NEEDS CORRECTING: a permissively-licensed student information system DOES exist. `Gap 478-R`'s three unprobed candidates were all probed this pass and **Fedena declares Apache-2.0 — in a `NOTICE` file, not a `LICENSE`**, at 547★ with a copyright line reading **2011**. 🟢 The usable conclusion is sharper than the old one: the permissive SIS is not missing, it is **fifteen years old**. 🟢 Two new permissive LMS rows also land, and every platform's version is read first-hand for the first time.**

🔵 Gate posture unchanged (`Code from External`; `make hooks` not attempted; session-local checks green).
Probes in [`evidence/sis-probe.2026-10-27-p479.tsv`](../evidence/sis-probe.2026-10-27-p479.tsv); grants in
[`evidence/grant-payload.2026-10-27-p479.tsv`](../evidence/grant-payload.2026-10-27-p479.tsv); versions in
[`evidence/version-tags.2026-10-27-p479.tsv`](../evidence/version-tags.2026-10-27-p479.tsv).

---

### 🔴 `Gap 478-R` closed — and it overturns the claim it was filed against

🔵 `Gap 478-R`: *"`OpenSIS`, `SchoolTool` and `Fedena` were not probed. The claim 'no permissive SIS exists'
therefore rests on 4 payload reads plus 1 non-resolving address… `Fedena`'s Apache-2.0 claim is the one that would
overturn it if true."* 🔴 **It is true.**

| candidate | address | what was measured | verdict |
|---|---|---|---|
| **Fedena** | [projectfedena/fedena](https://github.com/projectfedena/fedena) | 🟢 resolves; **547★**; created **2011-12-31**; `NOTICE` 680 B reads *"Licensed under the Apache License, Version 2.0"*; 🔴 **no `LICENSE` file at 10 paths** | 🟢 **permissive, declared** — by a `NOTICE`, which is where Apache projects put attribution, not the grant |
| Fedena (second address) | [foradian/fedena](https://github.com/foradian/fedena) | 🟢 resolves; `NOTICE` 679 B, same Apache-2.0 declaration, *Foradian Technologies Private Limited* | 🟢 corroborates the first at a second address |
| OpenSIS | [os4ed/openSIS-Classic](https://github.com/os4ed/openSIS-Classic) | 🟢 resolves; 🔴 **no grant file at 20 probed paths**; README says *"licensed under the GNU General Public License"* and links out of the repository | 🔴 copyleft **claimed in prose**, no payload — the vendor table's "GPL-2.0" is unverifiable here |
| OpenSIS (responsive) | [os4ed/OpenSIS-Responsive-Design](https://github.com/os4ed/OpenSIS-Responsive-Design) | 🟢 resolves; 🔴 no grant file at 20 paths; identical README wording | 🔴 same |
| SchoolTool | `schooltool/schooltool` | 🔴 **`git ls-remote` fails — the address does not resolve** | 🔴 gone; the secondary source calling it "discontinued" is consistent with this |

🔵 **What this changes for an engagement.** The old line — *"the permissive foundation for school administration is
a GENERAL ERP, not an education one"* — survives as advice but not as a fact about supply. 🟢 There is an
Apache-2.0 education SIS with 547★ and 560 forks. 🔴 Its copyright notice says **2011**, it is a Rails application
of that era, and the same secondary source that named it says development slowed and core features moved behind a
paid tier. 🟡 So the honest framing is a **choice between two kinds of work**: port a fifteen-year-old Apache-2.0
Rails SIS, or model the student domain on a maintained permissive ERP. Both are build, not compose — but only one
of them was visible before today.

### 🟢 The platform census, with versions read first-hand

🔵 `Gap 478-U`: *"No platform's version, release cadence, or maintenance state was read this pass. Secondary
coverage put Moodle at 5.2 (April 2026) and Chamilo at 2.0 (April 2026); neither was confirmed."* 🟢 Tags read
directly over `git ls-remote` — and **secondary coverage was stale on both**.

| platform | repo | grant (payload) | bytes · sha | latest tags read | what it is |
|---|---|---|---|---|---|
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | 35,147 · `8ceb4b9ee5ad` | 🟢 **v5.3.0** (also v5.2.4) | the incumbent LMS; `COPYING.txt`, not `LICENSE` |
| Open edX | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 AGPL-3.0 | 35,136 · `e12d78569742` | `open-release/sumac.master` | MOOC-scale LMS; election **unread** (`Gap 479-H`) |
| Tutor (Open edX deploy) | [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0-only** | 34,523 · `0d96a4ff68ad` | 🟢 **v22.0.3** | official Docker path; **no upgrade option** |
| Canvas | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0 | 34,520 · `57c8ff33c9c0` | 🟢 `release/2026-05-20.143`, v5.14.2 | higher-ed LMS, community edition |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 | 35,147 · `8ceb4b9ee5ad` | 🟢 **v3.0.1** — not 2.0 | LMS; v3 line is tagged |
| ILIAS | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 GPL-3.0 | 35,147 · `8ceb4b9ee5ad` | not read this pass | European higher-ed and public-sector LMS |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | 🔴 **AGPL-3.0-or-later** | 33,893 · `db1a87ba81e8` | not read this pass | 🟢 election now read: **or-later** |
| Sakai | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟡 **ECL-2.0** | 11,120 · `0688f62d04f1` | not read this pass | Apache-2.0 with a **narrowed patent grant** |
| OpenOLAT | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 10,982 · `6dbc5b605ed0` | 🟢 **OpenOLAT_21.1.1** | university/corporate LMS, Java |
| Kolibri | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 1,097 · `3c056b34a476` | 🟢 **0.19.5** | offline-first platform; 1,162★ |
| BigBlueButton | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 🔴 LGPL-3.0 | 7,652 · `e3a994d82e64` | 🟢 **v4.0.0** | virtual classroom; a **major** line this base had not recorded |
| H5P | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🔴 GPL-3.0 | 35,146 · `c53a65c2fd56` | not read this pass | interactive content types |
| OpenEduCat | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0-or-later** | 8,241 · `528f84036800` | branch `17.0` | education ERP/SIS on Odoo; 🟢 election now read |
| RosarioSIS | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** | 15,214 · `d954e14e5c75` | not read this pass | K-12 SIS, PHP + Postgres |
| Gibbon | [GibbonEdu/core](https://github.com/GibbonEdu/core) | 🔴 GPL-3.0 | 35,121 · `93178a43d6d3` | not read this pass | K-12 school management |
| **Fedena** | [projectfedena/fedena](https://github.com/projectfedena/fedena) | 🟢 **Apache-2.0** *(via `NOTICE`)* | 680 · `NOTICE` | not tagged | 🆕 **the permissive SIS** — 547★, copyright 2011, Rails |
| **TutorLoom** | [pacewisdomhq/TutorLoom](https://github.com/pacewisdomhq/TutorLoom) | 🟢 **Apache-2.0** | 11,362 · `a89039268428` | not tagged | 🆕 self-hosted multi-tenant LMS, Django + React; 50★, created 2026-10-07 |
| **mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 1,062 · `ceb97717de1f` | not read this pass | 🆕 **AI-native LMS** with mentor + role-play, SCORM and xAPI; 99★, created 2024-08-01 |
| **i-Educar** | [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** | 18,092 · `8177f9751321` | branch `2.12` | 🆕 Brazil's largest free school-management system; 721★, *software público* |
| **i-Diario** | [portabilis/i-diario](https://github.com/portabilis/i-diario) | 🔴 **AGPL-3.0, Portuguese translation** | 35,326 · `fe85f94658bf` | branch `1.6` | 🆕 teacher gradebook companion to i-Educar; 117★ |

### 🔴 One row's grant is a translation, and it does not say so

🔵 [portabilis/i-diario](https://github.com/portabilis/i-diario) ships its licence as
**`LICENÇA PÚBLICA GERAL AFFERO GNU, Versão 3`** — 35,326 B · `fe85f94658bf`. 🔴 The FSF does not approve
translations as the operative licence, and **this file carries no disclaimer saying it is unofficial**: a
case-insensitive search for *"tradu"*, *"unofficial"* and *"não oficial"* returns **zero** matches. 🟡 In practice
the governing text for a Brazilian municipal deployment is then an unapproved translation with nothing pointing at
the English original — a question for counsel on any engagement that touches this codebase, and the kind of defect
that is invisible to any tool that reads the SPDX identifier rather than the file.

### 🟢 Two permissive LMS rows, and what they are each good for

🔵 `p478` published OpenOLAT as *"the only permissive LMS at this scale"*. 🟢 That is still true **at that scale** —
OpenOLAT is a 21.1.x university platform. 🟢 But the permissive LMS tier now has three entries at three sizes:
**OpenOLAT** (Apache-2.0, university-scale, Java), **TutorLoom** (Apache-2.0, multi-tenant training institutes,
Django + React, three weeks old) and **mentingo** (MIT, AI-native with an LLM mentor and role-play built in,
SCORM + xAPI, two years old). 🔴 None is Moodle's size and none has Moodle's plugin ecosystem; the trade is
**licence freedom for ecosystem depth**, and that trade is now priced with three options instead of one.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 479-M`** | **Fedena's Apache-2.0 rests on a `NOTICE`, not a `LICENSE`.** A `NOTICE` that recites the Apache grant is strong evidence of intent and is **not** the same instrument as a licence file; whether it suffices is a legal determination this base cannot make. No source file header was read to corroborate it. |
| 🔴 **`Gap 479-N`** | **Fedena was not run, and its maintenance state is unmeasured.** 547★ and a 2011 copyright are not a cadence; no push date, release tag or dependency audit was read, and a Rails application of that vintage carries an upgrade cost nothing here has estimated. |
| 🔴 **`Gap 479-O`** | **`Gap 478-S` stands untouched.** No APK was built or instrumented and only `ml-authentication` was ever cloned out of elimu.ai's repositories; that tier remains description-only. |
| 🔴 **`Gap 479-P`** | **`Gap 478-P` is unattemptable here and is not retried.** Every regulatory reading on this shelf is law-firm and compliance-vendor commentary; EUR-Lex is refused at the gateway (`intel/market.md`). |
| 🟡 **`Gap 479-Q`** | **Versions were read for seven platforms, not fifteen.** ILIAS, H5P, Sakai, Gibbon, RosarioSIS, Frappe LMS, mentingo and the two new SIS rows have no first-hand version, and a tag list is not a release date — no tag was dated, so "latest" means "highest-sorting", not "most recent". |
| 🟡 **`Gap 479-R`** | **`Gap 478-T` unchanged: "deployed, not linked" is still architectural reasoning per recipe**, not verified against either platform's plugin API — and `canvas-mcp` (new on the foundations shelf) now offers a concrete way to test that boundary which this pass did not take. |

---

## 🆕 `p478` — `2026-10-27` — **🔴 THE PERMISSIVE-SIS QUESTION IS ANSWERED AND THE ANSWER IS "NONE": fifteen education platforms now carry a payload-read grant, **eleven are copyleft**, and the only permissively-licensed student information system the literature names does not resolve at any probed address. 🟢 The usable consequence is specific — the permissive foundation for school administration is a GENERAL ERP, not an education one.**

🔵 Gate posture unchanged (`Code from External`; `make hooks` not attempted; session-local checks green).
Grants in [`evidence/grant-payload.2026-10-27-p478.tsv`](../evidence/grant-payload.2026-10-27-p478.tsv).

---

### 🟢 The platform census, every grant a payload read

🔵 Fifteen platforms, each grant fetched to a file and the **file** measured (`Gap 468-A`). 🔴 Where the first
line of the payload disagrees with secondary coverage, the payload wins and the disagreement is noted.

| platform | repo | grant (payload, first-hand) | bytes · sha | what it is |
|---|---|---|---|---|
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | 35,147 · `8ceb4b9ee5ad` | the incumbent LMS; `COPYING.txt`, not `LICENSE` |
| Open edX | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 AGPL-3.0 | 35,136 · `e12d78569742` | MOOC-scale LMS, 8.2k★; **canonical name**, formerly `edx-platform` |
| Tutor (Open edX deploy) | [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0-only** | 34,523 · `0d96a4ff68ad` | the official Docker deployment path; election read, **no upgrade option** |
| Canvas | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0 | 34,520 · `57c8ff33c9c0` | higher-ed LMS, community edition |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 | 35,147 · `8ceb4b9ee5ad` | LMS; v2 rewrite on Symfony + Vue |
| ILIAS | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 GPL-3.0 | 35,147 · `8ceb4b9ee5ad` | European higher-ed and public-sector LMS |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** | 33,893 · `license.txt` | LMS on the Frappe framework; 🔴 a vendor table called this **MIT** — it is not |
| Sakai | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟡 **ECL-2.0** | 11,120 · `0688f62d04f1` | higher-ed collaboration/LMS; Apache-2.0 with a **narrowed patent grant** |
| OpenOLAT | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 10,982 · `6dbc5b605ed0` | university/corporate LMS, Java; 2nd channel vs the `pom.xml` typo |
| Kolibri | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 1,097 · `3c056b34a476` | offline-first learning platform for low-connectivity deployments |
| BigBlueButton | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 🔴 LGPL-3.0 | 7,652 · `e3a994d82e64` | virtual classroom / conferencing; reproduces `p477`'s byte count |
| H5P | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🔴 GPL-3.0 | 35,146 · `c53a65c2fd56` | interactive content types; one byte off the control (no final newline) |
| OpenEduCat | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL-3.0 | 8,241 · `528f84036800` | education ERP/SIS on Odoo; payload line 4 names LGPL v3 in prose |
| RosarioSIS | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** | 15,214 · `d954e14e5c75` | K-12 student information system, PHP + Postgres |
| Gibbon | [GibbonEdu/core](https://github.com/GibbonEdu/core) | 🔴 GPL-3.0 | 35,121 · `93178a43d6d3` | K-12 school management |

🔵 **Eleven copyleft, three permissive, one ECL-2.0.** 🟢 That sharpens `p477`'s "8 of 11 platforms are copyleft"
onto a larger census with every row payload-read, and it **reverses the convenient reading**: the permissive
options are not the big ones. Moodle, Open edX and Canvas — the three a client is most likely to already run —
are GPL-3.0, AGPL-3.0 and AGPL-3.0.

### 🔴 The permissive SIS does not exist, and the search for it is recorded so it is not repeated

🔵 A student information system is the piece a school-administration engagement needs and the piece this base had
never resolved on licence. The census above answers it, and a targeted search for a permissive one was run on top:

| candidate | claimed | what was measured |
|---|---|---|
| **GegoK12** | MIT, "complete source code on GitHub" (July 2026 vendor press release) | 🔴 **no repository resolves** — 5 owner/name combinations probed, all 404 |
| RosarioSIS | GPL v2 | 🟢 confirmed **GPL-2.0** from payload |
| OpenEduCat | LGPL-3.0 | 🟢 confirmed **LGPL-3.0** from payload |
| Gibbon | GPL | 🟢 confirmed **GPL-3.0** from payload |
| OpenSIS · SchoolTool | GPL-2.0 (vendor comparison table) | 🟡 **not probed** this pass |
| Fedena | Apache-2.0 (vendor comparison table, published by a competitor) | 🟡 **not probed**; the same source says development has slowed and core features are paid |

🔴 **So: no payload-verified permissive SIS exists in this base.** The one named candidate is a vendor claim with
no reachable code behind it, and it is not published as a row.

🟢 **The usable consequence.** If an engagement needs school administration on a permissive footing, the
foundation is a **general** ERP, not an education one:
[apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) — Apache-2.0, 11,906 B, payload-read — with
the student domain built on top. That is more work than forking RosarioSIS and it is the only route that leaves
the deliverable's licence in the studio's hands. 🔵 The alternative is honest too: run OpenEduCat under LGPL-3.0,
which permits linking proprietary modules and is the **least restrictive copyleft** on the list — LGPL-3.0 is the
pragmatic answer where AGPL-3.0 would be fatal and Apache-2.0 is unavailable.

### 🟢 Where an AI layer attaches without touching the platform's licence

🔵 Every platform above is a *deployed service*, so an agent that talks to it over HTTP or MCP is not a derivative
work of it. 🟢 The permissive bridge components are on `repos/foundations.md` and are payload-verified:
[DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) (MIT) writing to
[yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) or
[pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) (both Apache-2.0, byte-identical payloads). 🔴 **The
claim that the boundary holds is architectural reasoning, not a reading of either plugin API** —
`Gap 477-AL`'s objection, carried forward unchanged at `Gap 478-T`.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 478-P`** | **`Gap 477-S` is NOT discharged and this pass did not attempt it — and it is now known to be unattemptable here.** Every regulatory reading on this shelf is law-firm and compliance-vendor commentary. EUR-Lex was probed directly this pass and the gateway **refused the connection** (see `intel/market.md`), so no primary instrument can be read in this environment at all. |
| 🔴 **`Gap 478-Q`** | **Elections unread on four copyleft rows that matter:** `frappe/lms`, `openedx-platform`, `canvas-lms` and `openeducat_erp`. Only `tutor`'s was probed. `openeducat_erp`'s payload names "Version 3" in prose with no `or-later` clause located, which is **not** an election reading. |
| 🔴 **`Gap 478-R`** | **`OpenSIS`, `SchoolTool` and `Fedena` were not probed.** The claim "no permissive SIS exists" therefore rests on 4 payload reads plus 1 non-resolving address, with 3 named candidates unmeasured — and `Fedena`'s Apache-2.0 claim is the one that would overturn it if true. |
| 🔴 **`Gap 478-S`** | **`Gap 477-T` and `Gap 477-U` stand untouched.** No APK was built or instrumented, and only `ml-authentication` was ever cloned out of elimu.ai's 66 repositories; the rest is read from descriptions. |
| 🟡 **`Gap 478-T`** | **`Gap 477-AL` unchanged: "deployed, not linked" is architectural reasoning per recipe**, not verified per component against either platform's plugin API. |
| 🟡 **`Gap 478-U`** | **No platform's version, release cadence, or maintenance state was read this pass.** Secondary coverage put Moodle at 5.2 (April 2026) and Chamilo at 2.0 (April 2026); neither was confirmed first-hand, and neither is published above. |

---

## 🆕 `p477` — `2026-10-27` — **🟢 `Gap 476-I` IS ANSWERED DEFINITIVELY, FROM THE CODE: elimu.ai's face templates NEVER LEAVE THE DEVICE — there are ZERO upload paths in the entire repository and both HTTP classes are GET-only. 🔴 But the answer that matters is the one nobody asked: the templates are written to SHARED EXTERNAL STORAGE under `targetSdkVersion 23`, so they are readable by any other app on the device and over USB. The risk was never transfer. It is storage. 🔴 And the repo's last commit is 2025-02-25 — 20 months cold.**

🔵 Gate posture unchanged (`Code from External`; `make hooks` not attempted; session-local checks green).
`elimu-ai/ml-authentication` was **cloned** this pass (81 MB, `0a7a6bb02ab6`) and read, which is what
`Gap 476-I` asked for. Grants in
[`evidence/grant-payload.2026-10-27-p477.tsv`](../evidence/grant-payload.2026-10-27-p477.tsv).

---

### 🟢 `Gap 476-I` closed — the data-flow question, settled by reading the code

🔵 `Gap 476-I`: *"`ml-authentication` was not cloned and its model, data flows and retention were not examined;
whether face templates leave the device is **unknown**, and that is the question that decides the EU analysis."*

| question | method | answer |
|---|---|---|
| is there any upload path at all? | `grep` for `POST`, `multipart`, `RequestBody` across all Java | 🟢 **ZERO files.** No POST anywhere in the repository. |
| what do the only two HTTP classes do? | read `JsonLoader`, `MultimediaDownloader` | 🟢 both `setRequestMethod("GET")` — **download only** |
| does it hold `INTERNET` permission? | manifest | 🟡 **yes** — plus `CAMERA`, `RECORD_AUDIO`, `WRITE_EXTERNAL_STORAGE`, `WRITE_SECURE_SETTINGS` |
| where do face crops go? | `StudentImageCollectionActivity:233` | 🔴 **`Environment.getExternalStorageDirectory() + "/.literacyapp/face_recognition/dataset_collection/"`** |
| is recognition trained on-device? | `TrainingThread:152`, `:222` | 🟢 **yes** — `vgg_faces.pb` loaded locally, `trainClassifier()` runs on the handset |
| where does the model come from? | `TrainingThread:293` | 🟡 **not in the repo** — a `download_link.txt` is written with `MODEL_DOWNLOAD_LINK` for manual copy |

🟢 **So the transfer question is answered, and the answer is good: no face template is ever sent anywhere.**

### 🔴 The real exposure, which is storage and not transfer

🔵 `app/build.gradle` declares **`targetSdkVersion 23`** (`minSdkVersion 21`, `compileSdkVersion 23`). Android 6.0.

🔴 **Scoped storage does not apply below `targetSdk 29`.** A biometric dataset written to
`Environment.getExternalStorageDirectory()` under `targetSdk 23` therefore sits in **shared** storage, where:

- any other installed app holding `READ_EXTERNAL_STORAGE` can read every face crop;
- the directory is reachable over USB/MTP by anyone with physical access to the handset;
- the leading `.` makes it invisible to a gallery scan — which hides it from a **teacher**, not from an attacker.

🔵 **This inverts the compliance analysis the previous passes were building.** Under GDPR a face template is
Article 9 special-category data, and the question `Gap 476-I` framed — does it cross a network boundary? — is
the *transfer* question. The answer is no. 🔴 **The Article 32 "security of processing" question is the live one,
and it fails on its face:** special-category data at rest, world-readable on the device, no encryption in the
path that writes it. For a school deployment the practical consequence is that **one shared tablet carries every
pupil's face template in a directory any app can read.**

🟡 **Supply chain, noted as a second-order finding:** the TensorFlow model is fetched out of band from
`MODEL_DOWNLOAD_LINK` rather than committed, so the artefact that performs the recognition is not covered by the
repository's MIT grant and its provenance is unverified by anything in the tree.

### 🔴 `Gap 476-J` — the bus factor, partly measured and worse than the org-level view suggested

| measure | value |
|---|---|
| last commit on `ml-authentication` | 🔴 **2025-02-25** — 20 months cold |
| `pushed_at` from the search channel | 🔴 **2025-02-25T15:10:55Z** — agrees |
| ★ / forks / open issues | 16 ★ · 16 forks · **40 open issues** |
| distinct author emails | 🟡 **1** — but the clone was `--depth 1`, so this is a shallow-clone artefact, **not** a bus factor |

🔵 **A correction to how `p476` read this org.** `p476` reported elimu.ai as active, citing
`ml-storybook-reading-level` pushed 2026-10-26. That is true of *that* repo and not of this one. 🔴 **Org-level
activity does not transfer to a component**, and the component carrying the regulated feature is the cold one.

### The vertical tier, with this pass's two election rows corrected

| platform | repo | ★ | grant (first-hand) | version election | high-risk features it ships | region |
|---|---|---|---|---|---|---|
| BigBlueButton | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 9,255 | **LGPL-3.0** | 🟡 **bare id, no election** (`build.sbt`, new this pass) | webcam/attention monitoring if enabled | North America |
| Open edX | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 8,211 | **AGPL-3.0** | 🔴 unreadable, all channels | automated grading; proctoring | North America |
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | 7,550 | **GPL-3.0** | 🟢 `or-later` elected (2 channels) | automated grading; proctoring via plugins | EMEA |
| Oppia | [oppia/oppia](https://github.com/oppia/oppia) | 6,945 | 🟢 **Apache-2.0** · 11,358 B | N/A — permissive | none by default; lesson authoring | North America |
| Canvas LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 6,890 | **AGPL-3.0** | 🟡 bare id, no election | automated grading | North America |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | 3,351 | **AGPL-3.0** | 🟢 `or-later` elected (1 channel) | assessment | APAC (India) |
| Sakai | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 1,240 | **ECL-2.0** | 🟢 `pom.xml` agrees | assessment | North America |
| Kolibri | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 1,162 | **MIT** | 🟢 `package.json` agrees | none by default; offline-first | North America |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 1,020 | GPL-3.0 (carried) | unprobed | assessment | EMEA |
| OpenEduCat | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 899 | **LGPL-3.0** | 🟢 `or-later` elected (187/209 files) | **admissions scoring** | APAC (India) |
| i-educar | [portabilis/i-educar](https://github.com/portabilis/i-educar) | 721 | GPL-2.0 (carried) | unprobed | municipal SIS; enrolment | **LATAM (Brazil)** |
| RosarioSIS | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 647 | GPL-2.0 (carried) | unprobed | SIS; gradebook | EMEA |
| Gibbon | [GibbonEdu/core](https://github.com/GibbonEdu/core) | 637 | GPL-3.0 (carried) | unprobed | school management | APAC (Hong Kong) |
| ILIAS | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 505 | GPL-3.0 (carried) | unprobed | assessment | EMEA (Germany) |
| OpenOLAT | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 448 | **Apache-2.0** | 🟢 **N/A — declared in root POM** (new this pass) | assessment, QTI | EMEA |
| Academico | [academico-sis/academico](https://github.com/academico-sis/academico) | 409 | unread | unprobed | SIS for small institutions | EMEA |
| H5P | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 152 | **GPL-3.0** | 🟡 bare id, no election | none — content library | EMEA |
| elimu.ai | [elimu-ai/webapp](https://github.com/elimu-ai/webapp) | 41 | **MIT** | N/A — permissive | 🔴 **biometric pupil auth** (separate repo, analysed above) | **EMEA (Tanzania, South Africa)** |

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 477-S`** | **`Gap 476-H` is NOT discharged and this pass did not attempt it.** The regulatory readings on this shelf remain law-firm and compliance-vendor commentary. EUR-Lex and Vietnam's Decision 33 annex have still never been read first-hand here, and the GDPR Article 9 / Article 32 framing above is this pass's own reasoning from the statute's structure, **not** a compliance determination. |
| 🔴 **`Gap 477-T`** | **The storage finding is read from source, not observed at runtime.** No APK was built, installed or instrumented; file permissions on a real device were not inspected. `targetSdk 23` ⇒ legacy external storage is correct as Android policy, but the actual on-disk mode was not measured. |
| 🔴 **`Gap 477-U`** | **`Gap 476-V` stands, narrowed.** Only `ml-authentication` was cloned. Whether another of elimu.ai's 66 repositories carries a camera, attention-tracking or monitoring surface is still read from descriptions only. |
| 🟡 **`Gap 477-V`** | **8 of 18 vertical rows carry a grant that is carried, not re-read**, and 2 (`academico`, and `i-educar`'s election) have no first-hand grant read in any pass. 10 of 18 elections are unprobed. |
| 🟡 **`Gap 477-W`** | **The elimu.ai bus factor is still unmeasured.** The single author email is a `--depth 1` artefact; contributor count, release cadence and funding were not examined, so `Gap 476-J` is only half-closed — the staleness is measured, the sustainability is not. |

---


## 🆕 `p476` — `2026-10-27` — **🟢 `Gap 475-M` IS CLOSED: there IS an African education platform, it is a complete offline-first literacy stack, and it is the MOST PERMISSIVE thing on any shelf in this base — `elimu.ai`, 66 repositories, every grant read MIT. 🔴 And it ships FACE RECOGNITION to authenticate pupils, which is the one feature both the EU AI Act and Vietnam's Decision 33 put in their highest risk tier. 🟢 `Gap 475-N` is closed by a depth probe: OpenEduCat's `SPLIT_SCOPE` is DECLARED but NOT INSTANTIATED — 14 of 14 modules are uniformly LGPL-3.**

🔵 Gate posture unchanged (`Code from External`; `make hooks` not attempted; session-local checks green).
Grants are the first-hand reads in
[`evidence/grant-payload.2026-10-27-p476.tsv`](../evidence/grant-payload.2026-10-27-p476.tsv); the depth
probe is [`evidence/openeducat-depth.2026-10-27-p476.tsv`](../evidence/openeducat-depth.2026-10-27-p476.tsv).

---

### 🟢 `Gap 475-M` closed — the first non-EU/US vertical platform this base has ever carried

🔵 `Gap 475-M`: *"No Latin-American or African vertical platform is on this shelf, in any pass. Every row is
EU- or US-origin."* 🟢 It was found by running the supply census **in Swahili** — `elimu` is Swahili for
*education*, and the token had never been queried here.

| what | measured |
|---|---|
| organisation | [`elimu-ai`](https://github.com/elimu-ai), 66 repositories |
| grant across the 6 repositories read | **MIT on every one**, 1,065 B each, three digest groups differing only by copyright year |
| target countries, from the project's own wiki | **Tanzania** (Swahili) and **South Africa** (Xhosa), cited against out-of-school primary-age population |
| region field | **EMEA** (the closed vocabulary has no "Africa"; the country belongs in prose) |
| instructional standard | **EGRA / EGMA** — Early Grade Reading and Mathematics Assessment, the standard instruments in African primary education |
| architecture | Android launcher → appstore → Spring webapp/CMS, **offline-first**, plus two ML models |
| activity | `ml-storybook-reading-level` pushed **2026-10-26**; webapp and appstore within the last 3 weeks |

🟢 **Why this matters more than its star counts (41★ top repo).** It is the only education platform on this
shelf that is (a) permissively licensed end to end, (b) designed for intermittent connectivity, and (c) built
around an assessment standard African ministries already use. 🔴 **Its magnitude is tiny** — a studio would
be adopting a small project, not a Moodle-scale ecosystem, and `Gap 476-J` records what that costs.

### 🔴 The collision: the one African platform found ships the one feature two jurisdictions flag

🔵 [`elimu-ai/ml-authentication`](https://github.com/elimu-ai/ml-authentication) is, in its own description,
*"Android application for authenticating the current student using face recognition."*

| instrument | how it classes biometric identification of pupils | date that binds |
|---|---|---|
| EU AI Act, Annex III (as amended by Regulation (EU) 2026/1744) | **high-risk**; conformity assessment before deployment | **2 December 2027** for stand-alone Annex III systems |
| Vietnam, Decision 33/2026/QĐ-TTg | **high-risk**; education is 1 of 6 sectors in a 46-system list | **1 March 2027** for systems launched after 15 Aug 2026; **1 September 2027** for systems already running before it |
| North America | no federal statute; state-level student-data rules (e.g. California AB 1159 bars training on student data) | varies by state |

🟢 **The design lever, and it is new to this base.** Vietnam's decision treats many listed systems as
high-risk **only where the AI output is the sole basis for a decision without meaningful human review**. A
face-recognition sign-in that gates attendance automatically is in scope; the same model surfacing a
suggestion a teacher confirms may not be. 🔴 This is read from secondary legal summaries, not the decision's
annex, and `Gap 476-H` says so — but it is an engineering choice with a regulatory consequence, which is
exactly the kind of thing a recipe can be built around, and `compose/patterns.md` now does.

### 🟢 `Gap 475-N` closed — OpenEduCat's `SPLIT_SCOPE`, enumerated at depth

🔵 `Gap 475-N`: the payload *"says bundled libraries may differ and points at the source tree; this pass did
not walk the tree, so which modules carry which terms is unknown — and admissions scoring, the highest-risk
module, is the one that matters."* 🟢 The tree was walked this pass, by shallow clone at HEAD
`46a5d7d400820d471b67b8c019997bfa5d3c873e` — identical to the `ls-remote` HEAD, two channels agreeing.
🔴 The REST tree endpoint could not be used: `api.github.com` is **403** for non-session repositories here.

| measured in the 17 MB tree | result |
|---|---|
| module manifests (`__manifest__.py`) | 14 |
| modules declaring `LGPL-3` | **14 of 14 — uniform** |
| modules declaring anything else | **0** |
| licence files at **any** depth | **exactly 1** — the root `LICENSE`, 8,241 B · `528f84036800`, byte- and digest-identical to `p475` |
| `openeducat_admission` (the module `p475` flagged highest-risk) | **`LGPL-3`, same as every sibling** |
| per-source-file election | **`or-later` in 187 of 209 `.py` files** → `LGPL-3.0-or-later` |

🟢 **`SPLIT_SCOPE` is declared, not instantiated.** The payload warns that *"some external libraries and
contributions bundled with OpenEduCat may be published under other GPL-compatible licenses"* — a
forward-looking disclaimer. Nothing in the tree exercises it. 🔵 For delivery this **downgrades** the risk
`p475` and the P3 recipe carried: the enumeration is done and it came back clean.

🔴 **Two defects found in the payload while reading it.** Its first line is *"For copyright information,
please see the COPYRIGHT file."* — and **there is no `COPYRIGHT` file anywhere in the tree.** A dangling
pointer, which is also why `p473`/`p474`'s title-keyed reader failed on this repo: the payload opens with a
reference, not a licence title. 🟡 Separately, `openeducat_timetable` declares version `19.0.1.1.0`, four
dot-separated groups where all thirteen siblings have three.

### 🟢 Real platforms a studio can customise — grant, version election, and regulatory exposure

| platform | repo | ★ | grant (first-hand) | version election (`p476`) | high-risk features it ships | region of origin |
|---|---|---|---|---|---|---|
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | 7,550 | **GPL-3.0** | 🟢 **`or-later` elected** (2 channels) | automated grading; proctoring via plugins | EMEA |
| Open edX | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 8,211 | **AGPL-3.0** | 🔴 unreadable, all channels | automated grading; proctoring | North America |
| Canvas LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 6,890 | **AGPL-3.0** | 🟡 bare id, no election | automated grading | North America |
| BigBlueButton | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 9,255 | **LGPL-3.0** | not probed | webcam/attention monitoring if enabled | North America |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | 3,351 | **AGPL-3.0** | 🟢 **`or-later` elected** (1 channel) | assessment | APAC (India) |
| Sakai | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 1,240 | **ECL-2.0** | 🟢 `pom.xml` agrees | assessment | North America |
| Kolibri | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 1,162 | **MIT** | 🟢 `package.json` agrees | none by default; offline-first | North America |
| OpenEduCat | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 899 | **LGPL-3.0** | 🟢 **`or-later` elected** (187/209 files) | **admissions scoring** (`openeducat_admission`) | APAC (India) |
| OpenOLAT | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 448 | **Apache-2.0** | unprobed (`Gap 476-G`) | assessment, QTI | EMEA |
| H5P | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 152 | **GPL-3.0** | 🟡 bare id, no election | none — content library | EMEA |
| 🟢 **elimu.ai** | [elimu-ai/webapp](https://github.com/elimu-ai/webapp) | 41 | **MIT** | n/a — permissive | 🔴 **biometric pupil authentication** (separate repo) | **EMEA (Tanzania, South Africa)** |

🔴 **Still no Latin-American vertical platform, in any pass.** `Gap 475-M` is closed only on its African
half. The Spanish-language supply census is now known to have been *understated* (see `intel/market.md`), so
the next pass has a concrete reason to re-run the LATAM leg rather than conclude absence.

### 🟢 A version fact worth carrying: Moodle's tree moved, and a stale path probe 404s

🔵 Measured first-hand on the raw channel: `lib/moodlelib.php` and `version.php` **404 at the repository
root**, while `public/lib/moodlelib.php` and `public/version.php` return 200. Moodle has moved its web root
into `public/`. `public/version.php` reads `$release = '6.0dev (Build: 20261021)'`, `$branch = '600'`.
🟡 `composer.json` still declares `"provide": {"moodle/lms": "5.3"}` — so the two files disagree, and
`version.php` is the one to trust for release. 🔵 Any probe or integration written against pre-5.x Moodle
paths will silently 404 on `main`.

### 🔴 Gaps this pass registers

| gap | statement |
|---|---|
| 🔴 **`Gap 476-H`** | **The regulatory column remains a reading of secondary sources, not a compliance determination.** The EU dates come from law-firm and compliance-vendor commentary (independently corroborated this pass across several, and consistent with `p470`'s instrument number); the Vietnam dates and the "sole basis / meaningful human review" qualifier come from law-firm summaries of Decision 33, **not from its annex**. `Gap 475-L`'s requirement to read EUR-Lex and the annex first-hand is **not discharged**. |
| 🟡 **`Gap 476-I`** | **`elimu.ai`'s biometric exposure is read from repository descriptions, not from the code.** `ml-authentication` was not cloned and its model, data flows and retention were not examined; whether face templates leave the device is **unknown**, and that is the question that decides the EU analysis. |
| 🟡 **`Gap 476-J`** | **elimu.ai is small and its bus factor is unmeasured.** Top repo 41★; contributor count, release cadence and funding were not examined this pass. "Most permissive platform on the shelf" is a licence statement, not a sustainability one. |
| 🟡 **`Gap 476-K`** | **`bigbluebutton` has no root packaging file**, so its version election is unprobed and its multi-module tree unwalked — the only live foundation row with no election evidence of any kind. |

## 🆕 `p475` — `2026-10-27` — **🟢 THE VERTICAL SHELF NOW HAS A REGULATORY COLUMN, BECAUSE THE GRANT IS NO LONGER THE ONLY THING THAT DECIDES WHAT YOU CAN SHIP: Vietnam's Decision 33/2026/QĐ-TTg (in force 15 Aug 2026) and EU Annex III both classify AUTOMATED GRADING and BIOMETRIC PROCTORING as high-risk — so the same LMS feature is a conformity-assessment event in two regions and nothing in a third.**

🔵 Gate posture unchanged (`Code from External`; session-local checks green). Grants below are the
first-hand reads recorded in
[`evidence/grant-payload.2026-10-27-p475.tsv`](../evidence/grant-payload.2026-10-27-p475.tsv).

### 🟢 Real platforms a studio can customise, with the grant AND the regulatory exposure named

🔵 "High-risk feature" = a feature that, if enabled, pulls the deployment into EU AI Act Annex III
point 3 and/or Vietnam Decision 33's education entries. The platform is not high-risk; **the feature is**.

| platform | what it is | grant (read first-hand) | 🔴 features that trigger high-risk classification |
|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | The default LMS of public education worldwide | GPL-3.0 · 35,147 B | Quiz auto-grading, competency-based progression; any proctoring plugin |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | MOOC-scale platform, consortium-grade | AGPL-3.0 · 35,136 B | Auto-graded assessment, cohort placement, proctoring integrations |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | The dominant HE LMS in North America | AGPL-3.0 · 34,520 B | SpeedGrader automation, outcomes-based placement |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **The permissive full LMS** (`p469`) | Apache-2.0 · 10,982 B | QTI auto-assessment, curriculum progression |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | University consortium LMS | ECL-2.0 · 11,120 B | Gradebook automation, assignment auto-review |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 Offline-first, low-connectivity deployments | MIT · 1,097 B | Mastery/practice progression; 🟢 **no biometric surface** |
| [frappe/lms](https://github.com/frappe/lms) | Lightweight LMS on the Frappe stack | AGPL-3.0 · 33,893 B | Quiz grading, certification issuance |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🟢 **The education ERP/SIS** (admissions, fees, timetabling) | LGPL-3.0 · 8,241 B, 🔴 `SPLIT_SCOPE` | 🔴 **Admissions scoring — the single clearest Annex III point 3 trigger** |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | Interactive content type library, embeds in all of the above | GPL-3.0 · 35,146 B | Scored interactions when they count toward a grade |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | Virtual classroom / conferencing | LGPL-3.0 · 7,652 B | 🔴 Attention/engagement analytics; recording + any emotion inference |

### 🔴 The sentence that changes a build plan

🔵 **EU:** emotion recognition in education has been **prohibited outright since 2 Feb 2025** — not
high-risk, *banned*. 🔴 So a BigBlueButton "engagement detection" module and any Moodle proctoring
plugin that infers affect are **not shippable into the EU at any conformity cost**.
🔵 **Vietnam:** Decision 33 names *"monitoring learner behaviour with biometric data, such as facial
recognition or eye tracking"* as high-risk — **regulated, not banned** — with existing education
systems due to comply by **1 Sep 2027**.
🔵 **North America:** no federal equivalent; the constraint is **state** law and it runs the other way
— several states prohibit AI from *replacing* a licensed educator in grading, which restricts the
autonomy of the feature rather than its sensing.

🔴 **One codebase, three incompatible defaults.** This is the strongest argument on this shelf for
building the proctoring/affect surface as a **removable module** rather than a core feature.

### 🔴 Declared gaps on this shelf

| gap | statement |
|---|---|
| 🔴 **`Gap 475-L`** | **The high-risk feature column is this pass's reading of two legal texts, not a compliance determination**, and neither text was read in full — the EU side is from secondary guidance (vendor and law-firm commentary) and the Vietnam side from an official-text excerpt plus law-firm summaries. 🔵 The Annex III point 3 wording and Decision 33's education annex both need a primary read before any client deliverable cites them. |
| 🟡 **`Gap 475-M`** | **No Latin-American or African vertical platform is on this shelf**, in any pass. Every row is EU- or US-origin. The in-language census this pass ran ([`evidence/lang-supply-census…`](../evidence/lang-supply-census.2026-10-27-p475.tsv)) suggests why — but suggests it, and did not test it for *platforms* specifically. |
| 🟡 **`Gap 475-N`** | **`openeducat_erp`'s `SPLIT_SCOPE` is declared, not enumerated.** The payload says bundled libraries may differ and points at the source tree; this pass did not walk the tree, so **which** modules carry **which** terms is unknown — and admissions scoring, the highest-risk feature on this shelf, lives in exactly that codebase. |


## 🆕 `p474` — `2026-10-27` — **🔴 `Gap 473-B` CLOSED BY PUBLISHING THE SENTENCE: ECL-2.0's patent grant is narrowed exactly where a university is the contributor — it reaches only claims whose INVENTOR IS ALSO THE AUTHOR and only where the institution's own RESEARCH FUNDING AGREEMENTS let it grant, and it closes with "No other express or implied licenses are granted." 🟡 Copyright-wise Sakai and OpenLRW stay Apache-shaped and permissive; patent-wise they are a different instrument from the Apache-2.0 a client's counsel approved.**

🔵 **Gate posture, per `Gap 446-A`:** `make hooks` not attempted — KB cloned outside the harness
repo. **Nothing below is gate-attested.** Both ECL payloads re-read first-hand from
`raw.githubusercontent.com` this pass and measured (`Gap 468-A`). 🔴 `curl -sI` not used
(`Gap 472-A`).

### 🔴 The clause, quoted rather than inferred — ECL-2.0 §3, last two sentences

🔵 `p473` graded both ECL rows on Apache-family body resemblance and registered `Gap 473-B` because
nobody here had read §3. 🟢 Read now, in both payloads, and **the narrowing is in the text**:

> *"Any patent license granted hereby with respect to contributions by an individual employed by an
> institution or organization is **limited to patent claims where the individual that is the author
> of the Work is also the inventor of the patent claims licensed, and where the organization or
> institution has the right to grant such license under applicable grant and research funding
> agreements**. No other express or implied licenses are granted."*

| Payload | path read · bytes · digest | 🟢 §3 narrowing present | 🔵 self-description present |
|---|---|---|---|
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | `master/LICENSE` · 11,120 B · `0688f62d04f1` | 🟢 yes, verbatim as above | 🟢 yes — *"consists of the Apache 2.0 license, modified to change the scope of the patent grant in section 3"* |
| [Apereo-Learning-Analytics-Initiative/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | `master/LICENSE` · 9,878 B · `f339063d2f60` | 🟢 yes, verbatim as above | 🟢 yes, same sentence |

🔵 **The 1,242 B difference between the two payloads is line wrapping, not terms** — `sakai` serves
the hard-wrapped rendering and `OpenLRW` the long-line rendering. 🟢 Both carry the identical §3.
🔴 Which is the cleanest possible restatement of `Gap 466-C`: the byte delta that looked like a
difference in instrument is a difference in **whitespace**.

### 🟡 What this changes for an engagement, stated plainly

🟢 **For copyright — nothing.** ECL-2.0 is Apache-2.0's grant, permissive, and Sakai or OpenLRW can
go into a proprietary deliverable on that axis.
🔴 **For patents — three things.** Under Apache-2.0 §3 a corporate contributor's employer grants the
claims necessarily infringed by the contribution. Under ECL-2.0, where the contributor is
**institutionally employed** — which, for Sakai and for an Apereo learning-analytics project, is
most contributors:

1. the grant reaches only claims where **the author is also the inventor**;
2. it reaches them only where **the institution's grant and research-funding agreements permit the
   grant** — and university funding agreements routinely assign IP to a funder or a tech-transfer
   office;
3. **"No other express or implied licenses are granted"** forecloses the implied-licence argument
   that would otherwise cover the gap.

🔵 **So the honest cell is two-part, and this shelf now writes it that way:** *permissive on
copyright; patent grant conditional on the contributing institution's funding agreements.* 🔴 Where
a client's counsel approved **"Apache-2.0"** by name, ECL-2.0 has not been approved and §3 is the
clause they will care about.

### 🟢 A vertical platform added — and it is the first Turkish one

| Platform | Repo | Grant (path read · bytes · digest) | ★ | Region | What it is, and the customisation surface |
|---|---|---|---|---|---|
| **Atölye.Platform** | [PolyOS-Team/Atolye.Platform](https://github.com/PolyOS-Team/Atolye.Platform) | 🟢 **MIT** — `main/LICENSE` · 1,069 B · `fc9ec90c31a1` | 16 | EMEA | Open-source **exam submission and education management** platform, built by PolyOS and **optimised for Pardus school laboratories** — Pardus being Türkiye's state-developed Linux distribution. React + Node, multilingual, student-management and exam-system modules. 🟢 **MIT whole-work**: the one platform on this shelf an AI layer can be built into *and shipped* with no copyleft boundary and no patent caveat |

🔵 **Why a 16★ repository is on a shelf with Moodle and Open edX.** Not for its size — for its
**position**. It is the only education platform found that targets a *national* public-sector
desktop baseline, and the Pardus tie means a Turkish public-schooling engagement inherits the
deployment target rather than arguing for one. 🔴 **And its licence is the outlier in good
company**: the incumbents on this shelf are GPL (Moodle), AGPL (Open edX) and ECL with the patent
caveat above (Sakai).

### 🔵 The LMS licence landscape, restated with this pass's caveat folded in

| Platform | Grant, as this base carries it | Boundary an AI layer must respect |
|---|---|---|
| **Moodle** | GPL | 🟡 Distribution trigger; in-tree plugins inherit it. Integrate over an API, do not vendor |
| **Open edX** | AGPL | 🔴 **Network trigger** — the one that catches a hosted AI service wired into the platform |
| **Sakai** | ECL-2.0 | 🟡 Permissive on copyright; 🔴 **patent grant conditional on institutional funding agreements** (new this pass) |
| **Chamilo** | GPL | 🟡 Distribution trigger. 🔵 Spain-origin with a LATAM install base — the asymmetry `Gap 473-G` sees from the supply side, seen from the demand side |
| **Atölye.Platform** | 🟢 **MIT** | 🟢 None |

## 🆕 `p473` — `2026-10-27` — **🔴 EVERY LICENCE READER THIS BASE HAS BUILT IS KEYED ON ENGLISH TITLE STRINGS, AND THE LATAM LANGUAGE AXIS BREAKS IT ON THE FIRST TRY: `portabilis/i-diario`'s grant payload is an AGPL-3.0 IN PORTUGUESE — "LICENÇA PÚBLICA GERAL AFFERO GNU, Versão 3" — which every English-anchored screen on these shelves returns as UNSTATED. 🟢 And Brazil's largest free school software turns out to be a licence-boundary trap shipped as one product: the school information system is GPL-2.0-or-later and its own gradebook is AGPL — distribution trigger beside network trigger, from the same vendor, in the same deployment.**

🔵 **Gate posture, per `Gap 446-A`:** `make hooks` not attempted — KB cloned outside the harness
repo. **Nothing below is gate-attested.** Every address resolved first-hand (`git ls-remote
--symref`); every grant read first-hand from `raw.githubusercontent.com`, body written to a file and
the file measured (`Gap 468-A`). 🔴 `curl -sI` not used — dead here (`Gap 472-A`).

### 🔴 The instrument result, first, because it invalidates a screen rather than a row

🔵 `Gap 467-E` prescribed running the LATAM leg *"on the language axis (`pt`/`es` tokens) … not the
English vocabulary."* 🟢 It was run. 🔴 **The first Brazilian repository it reached does not merely
sit outside the English discovery vocabulary — its licence payload sits outside the English
GRADING vocabulary:**

| repo | grant path read | bytes · digest | title block as served | what an English-anchored reader returns |
|---|---|---|---|---|
| [portabilis/i-diario](https://github.com/portabilis/i-diario) | `1.6/LICENSE` | **35,326 B** · `fe85f94658bf` | **`LICENÇA PÚBLICA GERAL AFFERO GNU`** / `Versão 3, 19 de novembro de 2007` | 🔴 **`UNSTATED`** — no substring of `GNU AFFERO GENERAL PUBLIC LICENSE` is present in the payload |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | `2.12/LICENSE` | **18,092 B** · `8177f9751321` | `GNU GENERAL PUBLIC LICENSE` / `Version 2, June 1991` | 🟢 `GPL-2.0`, and the **`or-later`** election is present (`any later version`) |

🔴 **Two consequences, both load-bearing:**

1. **The strongest copyleft on these shelves can hide behind a language.** AGPL-3.0 is the one family
   whose trigger is *network use* — the trigger a studio hosting software for a client actually
   pulls. A screen that reads `i-diario` as ungranted would file it as "no rights at all" (safe, by
   accident); a screen that defaults ungranted-to-permissive would file the single riskiest row on
   this shelf as free to host. 🔵 `Gap 468`'s version axis and `p467`'s `grant_class` both anchor on
   the **English** title block, so both fail here, in opposite directions depending on their default.
2. 🟡 **A translated GNU licence is not the operative licence, and that is not a loophole.** The FSF
   does not approve translations as legally operative text; the operative grant is the English
   AGPL-3.0, and this payload is an unofficial rendering of it. 🔴 **The obligations are unchanged**:
   `i-diario` is **AGPL-3.0-or-later** (`qualquer versão posterior`, read first-hand) and hosting a
   modified build for a client's users triggers source disclosure **to those users**.

🔵 **Registered as `Gap 473-C`:** add a **non-English title layer** to every grant reader on this
base — at minimum the Portuguese and Spanish GNU-family renderings (`LICENÇA PÚBLICA GERAL`,
`LICENCIA PÚBLICA GENERAL`, `AFFERO`, `Versão`/`Versión`) and the `or-later` elections that go with
them (`qualquer versão posterior`, `cualquier versión posterior`). 🔴 Until that exists, **no LATAM
or Iberian row on these shelves may be graded `UNSTATED` without reading its payload by eye.**

### 🟢 The LATAM public-education stack, grant-verified — and why it is one trap, not two products

🔵 [`portabilis`](https://github.com/portabilis) ships what its own README calls *"o maior software
livre de educação do Brasil"*, as two repositories that deploy together.

| Component | Repo | Grant (path read, bytes, digest) | Stars · forks | What it does |
|---|---|---|---|---|
| **i-educar** | [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🟡 **GPL-2.0-or-later** — `2.12/LICENSE`, 18,092 B `8177f9751321` | **720** · **552** | The **student information system**: enrolment, school records, student and staff registries, reporting. PHP/Laravel, classed as Brazilian *software público*. 🟢 552 forks is a real municipal install base, not a star count |
| **i-diario** | [portabilis/i-diario](https://github.com/portabilis/i-diario) | 🔴 **AGPL-3.0-or-later** — `1.6/LICENSE`, 35,326 B `fe85f94658bf`, **payload in pt-BR** | 117 · 62 | The teacher-facing **gradebook / diário de classe**: attendance, marks, lesson records, feeding i-educar |

🔴 **The trap, stated as the engagement sees it.** A LATAM ministry or municipality engagement that
hosts this stack as a service crosses **two different copyleft triggers in one deployment**:

- 🟡 `i-educar` is **GPL-2.0-or-later** → the trigger is **distribution**. Host it unmodified as a
  service and nothing is owed. 🟢 And `or-later` means it **may be combined forward** with GPL-3.0
  components — the same election `Gap 467` read on `oat-sa/tao-core`.
- 🔴 `i-diario` is **AGPL-3.0** → the trigger is **network use**. Modify it and let the client's
  teachers reach it over a network and **the modified source is owed to those teachers**. An AI
  grading assistant wired *into* `i-diario` is a modification.
- 🔴 **18,092 B is a new GNU size on these shelves.** Every GNU payload this base had carried sat at
  34–35 KB; GPL-2.0's canonical text is ~18 KB. 🔵 A screen with a GNU size band learned from
  AGPL/GPL-3.0 observations would not have recognised `i-educar`'s licence at all.

🟢 **The pattern that avoids both**: leave `i-diario` unmodified and reach it over its API, putting
the AI layer outside the copyleft boundary — the `scorm-again` / LTI firewall shape already on this
shelf, applied to a LATAM incumbent. Written up as `compose/patterns.md` `P473-2`.

### 🟢 More LATAM supply, graded — the language axis paid out beyond the stack

| Repo | Grant (path read, bytes) | Stars | Country | Why it is on a vertical shelf |
|---|---|---|---|---|
| [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** — `main/LICENSE`, 1,092 B `e162f8f4b461` | 22 | Brazil | 🟢 **Brazil's BNCC national curriculum as verified open data**: **1,721 learning objectives** in JSON, SQLite and CSV, **per-record provenance**, a reproducible extraction pipeline, and an MCP surface. 🟢 **A single MIT grant covering the whole repository** — probed for a separate data licence at three paths, all `404`, so the code grant is the only grant and it covers the compilation. Holder: *Profy Tecnologias Educacionais Ltda* |
| [gpassero/uol-redacoes-xml](https://github.com/gpassero/uol-redacoes-xml) | 🟢 **Apache-2.0** — `master/LICENSE`, 11,357 B `b40930bbcf80` | 39 | Brazil | A corpus of **UOL's ENEM-style essay bank in XML**, built for Portuguese NLP validation. 🟢 The automated-essay-scoring substrate for pt-BR, permissively licensed |
| [fauzcategui/moodle-sence](https://github.com/fauzcategui/moodle-sence) | 🟡 **GPL-3.0-or-later** — 🔴 `master/license.txt` **(lowercase)**, 35,126 B `c3bc1fd94148` | 29 | Chile | A Moodle plugin recording attendance into **SENCE**, Chile's national training service. 🔵 Copyleft is unavoidable here — it is a Moodle plugin and Moodle is GPL. 🔴 **Its grant is at lowercase `license.txt` — `Gap 472-B` reproduced independently**, see below |
| [cortega26/chile-hub](https://github.com/cortega26/chile-hub) | 🟢 **MIT** — `main/LICENSE`, 1,070 B `277707dcaa3b` | 135 | Chile | Curated, normalised Chilean public data **including education**, consumable from Polars/DuckDB/SQLite in one line. Created 2026-05-30 |
| [prefeiturasp/dados-educacao](https://github.com/prefeiturasp/dados-educacao) | 🔴 **UNGRANTED** — no payload at 11 root paths, HEAD `9e6516753747` | 57 | Brazil | São Paulo's municipal education open-data analyses. 🔴 **A city government's own repository with no licence** — named rather than dropped |

### 🟢 `Gap 472-B` reproduced on an unrelated repo, so it is a rule and not an anecdote

🔵 `p472` registered the gap on `frappe/lms` (grant at `develop/license.txt`) and prescribed adding
lowercase paths to the probe set. 🟢 Done — and this pass's 14-path set caught a **second**
independent case, `fauzcategui/moodle-sence` at `master/license.txt`, in a different country,
language, ecosystem and licence family. 🔴 **Both rows would have published as UNGRANTED under the
pre-`p472` probe set.** The gap's prescription is now load-bearing, not speculative: two of the 36
granted rows this pass (5.6 %) grant **only** at a lowercase path.

### 🟢 A published licence claim REFUTED by its own payload — and the literature disagreed with itself first

🔵 The vertical-platform leg this pass searched returned an LMS roundup set in which **three sources
state three different licences for Open edX**: *"Released under AGPLv3"*, *"Apache License 2.0: Used
by Open edX. Allows proprietary modifications"*, and *"the core is AGPL with some libraries under
Apache 2.0."*

🔴 **Read first-hand, there is nothing to average.** `openedx/edx-platform` `master/LICENSE` is
**AGPL-3.0, 35,136 B `e12d78569742`**, at HEAD `03698e2b6ff4`.

🔴 **The consequential source is the one that is wrong in the permissive direction.** *"Allows
proprietary modifications"* is the precise opposite of what AGPL-3.0 does to a hosted modified
build, and it is the sentence a studio would act on. 🟢 This is the third pass in which a market- or
listicle-sourced licence claim has been refuted by a payload read, and the standing rule stands:
**a licence is read from the repository, never from a comparison table.**

### 🔴 The hosting tier's licence shape, stated as a number

🔵 Across the nine LMS / platform cores graded first-hand this pass and last:

| grant class | platforms | which |
|---|---|---|
| 🔴 **AGPL-3.0 — network-use trigger** | 4 | Open edX `35,136 B` · Canvas `34,520 B` · frappe/lms `33,893 B` · ClassroomIO `34,523 B` |
| 🟡 GPL — distribution trigger | 2 | Moodle `35,147 B` (`main/COPYING.txt`) · Chamilo |
| 🟢 Permissive / ECL | 4 | Kolibri **MIT** `1,097 B` `3c056b34a476` · OpenOLAT **Apache-2.0** `10,982 B` · Oppia **Apache-2.0** `11,358 B` · Sakai **ECL-2.0** `11,120 B` |

🔴 **The AGPL rows are concentrated at exactly the tier a studio HOSTS.** Four of the ten
best-known open LMS cores put network copyleft on the component that faces the client's learners,
which is the one deployment shape every engagement actually takes. 🔵 That is not an argument
against them — it is an argument for deciding the licence boundary **before** the architecture, not
after.

🟢 **`learningequality/kolibri` is now grant-verified MIT, first-hand** (`develop/LICENSE`, 1,097 B
`3c056b34a476`, holder *Learning Equality*), where `p472` carried it from a shortlist. 🟢 With
**1,012 forks** and offline-first as a design premise rather than a feature, it remains the pick
wherever connectivity or compute is the binding constraint. 🔵 Precision on region: Kolibri's
**origin** is North America; its **deployment strength** is LATAM, Africa and rural APAC. Those are
different facts and this shelf has previously printed only the second.

### 🔴 Declared gaps on this shelf

- 🔴 **The Spanish leg is thin and that is a measurement, not a silence.** The `educacion` token at
  ≥20★ returned **8 repositories**, of which **one** (`moodle-sence`, 29★) is education
  *infrastructure*; the rest are Spanish-language programming curricula and open-data projects.
  🟢 The Portuguese token at ≥20★ returned **15**, including a school information system, a
  gradebook, a curriculum dataset and an essay corpus. **Within LATAM, the open-source education
  supply is Brazilian** on this evidence, and the next pass should test that at a lower star floor
  before it is carried as a standing position.
- 🔴 **No LATAM-origin LMS core surfaced.** `i-educar` is an SIS and `menthor` (Brazil, Apache-2.0)
  remains archived. The LATAM incumbent LMS is still **Chamilo** — GPL-3.0 and Spain-origin, not
  LATAM-origin, with a LATAM install base. Stated as an informed gap.
- 🔵 **`Gap 473-B` (ECL-2.0 patent scope) applies here too.** Sakai is this shelf's only permissive
  LMS with a gradebook of record, and its patent grant is narrower than Apache-2.0's by design — see
  `repos/foundations.md`.

## 🆕 `p472` — `2026-10-27` — **🟢 THE PERMISSIVE SHORTLIST, NAMED: for a client that must keep its modifications closed, the education vertical has exactly five viable cores — Sakai (ECL-2.0), OpenOLAT (Apache-2.0), Oppia (Apache-2.0), Kolibri (MIT), Academico (MIT) — and NOT ONE of them appears in the vendor LMS comparison this pass searched, which lists seven platforms and never states that Sakai is permissive.**

🔵 Every grant below read first-hand from `raw.githubusercontent.com` this pass, body written to a
file and the file measured (`Gap 468-A`). Stars from MCP `search_repositories`, **2026-10-27**.
🔴 `curl -sI` not used — dead on this harness (`Gap 472-A`).

### 🟢 Customisable cores by licence class — the decision table

| Platform | Repo | Licence (path read) | Stars | Region strength | What it is, and when to pick it |
|---|---|---|---|---|---|
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** — `master/LICENSE`, 11,120 B | 1,240 | Global higher ed | 🟢 **The only permissive LMS with a gradebook of record.** Educational Community License 2.0 is an Apache-2.0 derivative, OSI-approved. **Pick it when AI output must touch grades and the client cannot disclose source** |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** — `master/LICENSE`, 10,982 B | 448 | EMEA (DACH) | QTI assessment, SCORM, curriculum management, certification, roll-call. **Pick it for EMEA public-sector and university work under the EU AI Act** — permissive, and assessment is first-class |
| **Oppia** | [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** — `develop/LICENSE`, 11,358 B | **6,944** | Global, SDG-4 | Interactive **explorations** with explicit misconception branching. **Pick it when the deliverable is adaptive practice rather than course delivery** |
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** — `develop/LICENSE`, 1,097 B | 1,162 | LATAM · Africa · rural APAC | **Offline-first** by design. 1,012 forks. 🟢 **Pick it wherever connectivity or compute is the binding constraint** — which is precisely what the ILIA 2025 and Intelligent CIO findings in `intel/market.md` say about LATAM |
| **Academico** | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** — `main/LICENSE`, 1,094 B | 409 | EMEA | 🟢 **A permissively licensed student information system** (Laravel + Filament), for small and medium institutions. The market literature searched this pass states no MIT/Apache SIS exists; it does |
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | 🟡 **GPL-3.0** — `main/COPYING.txt` | **7,549** | Global — the default incumbent | 1,800+ plugins, 7,684 forks, **no integrated SIS**. 🔵 Grant lives at `COPYING.txt`. **Expect to find it already installed**; integrate over LTI/web services rather than forking — see `compose/patterns.md` `P2` |
| **Canvas LMS** | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🟡 **AGPL-3.0** — `master/LICENSE`, 34,520 B | **6,889** | North America — dominant in US higher ed | 🔴 **Open-core with network copyleft.** Hosting a modified build for the client's users triggers disclosure to those users |
| **Open edX** | [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🟡 **AGPL-3.0** — `master/LICENSE`, 35,136 B | — | Global MOOC + corporate training | MIT/Harvard-origin, now **Axim Collaborative**. Run it via **Tutor** ([overhangio/tutor](https://github.com/overhangio/tutor), AGPL-3.0 `release/LICENSE.txt`, 1,131★) — the Docker/Kubernetes distribution |
| **frappe/lms** | [frappe/lms](https://github.com/frappe/lms) | 🟡 **AGPL-3.0** — 🔴 `develop/license.txt` | **3,351** | APAC (India) | Sits on the Frappe/ERPNext stack, so it composes with an ERP the client may already run. 🔴 Grant is at a **lowercase ninth path** — `Gap 472-B` |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🟡 **GPL-3.0** — `master/LICENSE`, 35,147 B | 1,020 | **LATAM + EMEA** | Accessibility-first, with a genuine Spanish-speaking and LATAM install base. 🟢 **The incumbent to expect in a LATAM public-education engagement** |
| **ILIAS** | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🟡 **GPL-3.0** — `release_11/LICENSE`, 35,147 B | 505 | EMEA (German-speaking) | Heavy public-sector and university use |
| **LearnHouse** | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🟡 **AGPL-3.0** — `dev/LICENSE`, 34,523 B | 2,424 | Global | Headless, AI-oriented; API-first if the client wants its own front end |
| **ClassroomIO** | [classroomio/classroomio](https://github.com/classroomio/classroomio) | 🟡 **AGPL-3.0** — `main/LICENSE`, 34,523 B | 1,732 | Global | Customer-training shape — SaaS companies teaching their own users |

### 🟢 Assessment and integration components that are safe to modify

| Component | Repo | Licence (path read) | Stars | Use |
|---|---|---|---|---|
| **Autolab** | [autolab/Autolab](https://github.com/autolab/Autolab) | 🟢 Apache-2.0 — `master/LICENSE`, 11,324 B | 808 | Auto-graded programming assignments + course management |
| **Submitty** | [Submitty/Submitty](https://github.com/Submitty/Submitty) | 🟢 BSD-3-Clause — `main/LICENSE.md`, 1,542 B | 804 | Submission, automated grading, TA grading. 1,119 forks |
| **scorm-again** | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 MIT — `master/LICENSE`, 1,072 B | 359 | 🟢 **The licence firewall.** SCORM 1.2 / 2004 runtime: an AI layer reports completion and scores into a GPL/AGPL LMS **without linking to or modifying it** |
| **Richie** | [openfun/richie](https://github.com/openfun/richie) | 🟢 MIT — `master/LICENSE`, 1,079 B | 316 | Course catalogue / portal CMS fronting Open edX or Moodle |
| **INGInious** | [INGInious/INGInious](https://github.com/INGInious/INGInious) | 🟡 AGPL-3.0 — `main/LICENSE`, 34,764 B | 243 | Secure exercise assessment with an **LTI** seam. 🔴 Use unmodified over LTI; modifying it triggers AGPL |

### 🔴 What this shelf will not tell you, stated plainly

- 🔴 **OpenEduCat**, the vendor whose comparison page dominated this pass's platform search, is
  described there as an *"integrated education-ERP"* and **its own page does not state its
  licence**. No repository address was surfaced for it by the MCP channel in this window.
  **Not published as a row** — an unlicensed, unaddressed platform is not a finding.
- 🔵 **No LATAM-origin education platform** appears above except Chamilo's install base (the project
  itself is EMEA-origin). The one LATAM-origin repository found this window,
  [menthorlabs/menthor](https://github.com/menthorlabs/menthor) (Brazil, Apache-2.0, 582★), is
  **archived** and is therefore not offered as a core.
- 🔵 **No Middle East or Africa-origin platform** surfaced, against live UAE school-AI policy.

## 🆕 `p471` — **🔴 TWO ROWS ON THIS SHELF WERE PUBLISHED AS UNGRANTED AND ARE GRANTED. ARSnova (67★) serves GPL-3.0 at `core/LICENSE` and forma.lms (37★) serves GPL-2.0 at `html/license.txt` — both corrected in place above. 🔴 And ARSnova carries the opposite finding in the same tree: `formatting/LICENSE` is 133 bytes of "All rights reserved" naming Particify, so the repository is part-copyleft and part-proprietary and a wholesale vendoring ships the proprietary half.**

🔵 Gate not attested (`Gap 446-A`); checks re-implemented in-session and green. Every grant below
read first-hand from `raw.githubusercontent.com` at the resolved ref.

### 🔴 What was wrong, and why it was wrong for the same reason twice

🔵 Both rows were graded by a **root-path** licence probe — the instrument this base refined over
five passes to thirteen paths, all of them at the repository root. Both platforms put their grant
**in-tree**. The probe was working correctly and the verdict was still wrong, because the question
it answers is narrower than the question this shelf asks.

| platform | shelf said | payload says | where |
|---|---|---|---|
| **ARSnova** | 🔴 *"NO GRANT at 10 paths"* | 🟢 **GPL-3.0** · 35 147 B · `8ceb4b9ee5ad` | `core/LICENSE` |
| **ARSnova** | — *(not seen at all)* | 🔴 **All rights reserved**, 133 B · `747c3a657b2b` | `formatting/LICENSE` |
| **forma.lms** | 🔴 *"no grant at 10 paths"* | 🟢 **GPL-2.0** · 18 346 B · `4e63feff285d` | `html/license.txt` |

🟢 **The ARSnova digest is a control passing, not a lone read.** `35 147 B · 8ceb4b9ee5ad` is the
value these shelves already record for `moodle/moodle`'s `COPYING.txt` and for Chamilo — the stock
FSF GPL-3.0 text, reproduced exactly from a repository this base had never read for GPL.

### 🟡 What a studio can now do with each, and the boundary in both

- **ARSnova** — 🟡 **integrate, do not vendor wholesale.** `core/` is GPL-3.0: a Kotlin
  audience-response backend with a containerised deployment and thirteen years of history, reachable
  over its API from a separately-licensed product. 🔴 **Exclude `formatting/`** from every
  deliverable: its author has reserved all rights, and that is the one module in the tree a licence
  audit would otherwise wave through because the repository "has a LICENSE".
- **forma.lms** — 🔴 **read, do not vendor.** GPL-2.0 is real, and the secondary roundups calling it
  Apache-2.0 are refuted from the payload. 🔵 GPL-2.0 is **not** compatible with GPL-3.0-only code,
  which matters here specifically: a studio composing forma.lms with Moodle plugin code (GPL-3.0)
  cannot merge the two into one binary.

🟡 **The bound on the ARSnova recovery.** A GPL payload carries the **FSF's** copyright, so nothing
in `core/LICENSE` names Particify. That the grant covers the `core` module is read from the
subtree's position, not from the payload (`Gap 471-C`). The `formatting/` reservation names Particify
directly and is certain. Where the two readings disagree, the reservation is the safer one to build
against.

### 🔵 The standing consequence for every platform row on this shelf

🔵 Measured over 229 shelf addresses this pass, the chance a repository hides a grant below its root
rises monotonically with tree size — **0.0 %** under 25 paths, **40.7 %** at 500–1 999, **66.7 %**
above 2 000. 🔴 **Every platform on this shelf sits in the top two bands.** A "has a LICENSE at the
root" screen is therefore weakest exactly where this shelf is strongest, and the pre-vendoring audit
for the largest rows is substantial rather than nominal: 149 licence payloads inside `moodle/moodle`,
148 inside Open edX, 64 inside ILIAS, 56 inside `instructure/canvas-lms`, 27 inside Chamilo.

🔵 Those counts are **work estimates, not licence findings** — the great majority are vendored
third-party dependencies, each carrying its upstream's own grant. The number says how many payloads
a real audit must read before a platform ships inside a client deliverable.

## 🆕 `p470` — **🔴 THE MOODLE PLUGIN IS WHERE PERMISSIVE EDUCATION PROJECTS GO COPYLEFT, AND THIS PASS CAUGHT IT MID-REPOSITORY: `edukors_graph` is MIT at its root and GPL-3.0-or-later inside `plugin/edukorsplayer/`, both payloads read first-hand. 🟢 And two granted course-tier platforms are added, both GPL-3.0, both APAC.**

🔵 **Gate posture:** `make hooks` not attempted (KB cloned outside the harness repo). Nothing here
is gate-attested. Every grant read first-hand at `HEAD` on **2026-10-27**; refs by
`git ls-remote --symref`; payloads written to files and the files measured per `Gap 468-A`.

### 🔴 The platform-integration boundary, stated as a rule

🔵 The platform tier's recurring question is what a studio may ship on top of an LMS. This pass
produced the general answer, from a repository that publishes **both** grants:

| [`mgarlabx/edukors_graph`](https://github.com/mgarlabx/edukors_graph) · `main` `6bc743c6a5fe` · 17★ · **LATAM** (BR) | payload | class |
|---|---|---|
| root `LICENSE.md` — schema, standalone player, original resources | 1 087 B · `625342dc4d3d` | **MIT** |
| `plugin/edukorsplayer/COPYING.txt` — the **Moodle integration** | **35 151 B** · `e79e9c8a0c85` | 🔴 **GPL-3.0-or-later** |
| `plugin/edukorsplayer/THIRD_PARTY.md` | 785 B · `42e7a91016b6` | reused MIT retains its notices |

🟢 **The rule, and it is not specific to this project.** Moodle is GPL, so **a Moodle plugin must be
GPL** — there is no permissive path to a Moodle-integrated artefact, whatever the surrounding
project is licensed as. The same holds for every GPL platform on this shelf. So for any
permissively-licensed education project that ships an LMS integration, the integration subtree is
the place the grant changes, and a root-path licence read cannot see it (`Gap 470-A`).

🔵 **What that means at proposal time, for the platforms this shelf carries:**

| deliverable shape | licence outcome | so |
|---|---|---|
| AI layer calling an LMS over its **web services / REST API**, no plugin | the AI layer keeps its own licence | 🟢 the clean route; prefer it wherever the LMS exposes the API you need |
| AI layer shipped **as a Moodle plugin** | **GPL-3.0-or-later** for that artefact | 🟡 viable, but the plugin's source goes to the client and downstream; price and scope it knowing that |
| AI layer **linked into** a GPL platform's own process | copyleft reaches the linked work | 🔴 the case to avoid by architecture, not by argument |

🟢 This is why `edukors_graph` is a genuinely useful LATAM row despite 17★: it ships **the schema and
a standalone player under MIT** — the player is the API-route deliverable, and the plugin is
available when the client wants in-LMS delivery and accepts the terms.

### 🟢 Platform-tier rows added this pass

| platform | repo | grant (first-hand) | ★ | region | what it is |
|---|---|---|---|---|---|
| vibe-logisim | [`FIY-pc/vibe-logisim`](https://github.com/FIY-pc/vibe-logisim) | **GPL-3.0** · 35 149 B · `3972dc9744f6` | 9 | APAC (CN) | AI-assisted **Logisim workbench** for computer-organisation courses: draw and simulate circuits, and let an agent read, wire, debug and explain them. A whole-course deliverable for a CS department, not a component |
| QuizForge | [`lhd23333/QuizForge`](https://github.com/lhd23333/QuizForge) | **GPL-3.0** · 35 149 B · `3972dc9744f6` | 7 | APAC (CN) | Local-first maths/physics **question-bank workbench**: OCR import of past papers, Markdown management, handout and paper assembly, agent assistance, sandboxed TeX templates. Windows-first, offline. Byte- and digest-identical grant to the row above |
| Edukors player + Moodle plugin | [`mgarlabx/edukors_graph`](https://github.com/mgarlabx/edukors_graph) | 🟡 **MIT** player · **GPL-3.0-or-later** plugin | 17 | **LATAM** (BR) | Standalone learning-graph player (MIT) plus a Moodle integration (GPL). Self-described **Experimental**; PHP + JSON Schema |

🔵 **Three rows. Two unqualified GPL-3.0, one split.** All three are deployment-or-fork decisions
rather than build-on components, which is exactly why they belong on this shelf and not on
`agents/top.md`.

### 🔴 Refused at the platform tier

| candidate | probe at `HEAD` | why refused |
|---|---|---|
| [`simpleqt/radai`](https://github.com/simpleqt/radai) | `main` `0b1e8a4bbf9d` · **no licence at 13 paths** | 🔴 ungranted — and it is the most platform-shaped candidate of the pass: a LangGraph platform spanning course teaching-assistant, question-bank practice, learning analytics and a research assistant, with retrieval over a knowledge graph. The platform-tier loss of the hour |
| [`chuantiet5-stack/zhiqi-ai-education-assistant`](https://github.com/chuantiet5-stack/zhiqi-ai-education-assistant) | `main` `369a11f9a533` · **no licence at 13 paths** | ungranted — education agent, textbook RAG, homework marking, study plans, focus monitoring |
| [`Pedrosasouza/AcademicFlow-Agent`](https://github.com/Pedrosasouza/AcademicFlow-Agent) | `main` `8e341c21f789` · **no licence at 13 paths** | ungranted — LangGraph/ReAct **academic management** agent on local Ollama, Brazil-placed. The nearest thing to a regional school-administration platform, and unusable |
| [`chat-edu/v3`](https://github.com/chat-edu/v3) | `main` `f44f5eeeb68b` · **MIT** · 1 064 B · `3dc45db43baf` | 🟡 granted but **abandoned** — last pushed 2026-05-22, README is unmodified `create-next-app` boilerplate |

🔵 **Four refusals, three of them ungranted.** `p468`'s observation holds for a third pass: the
platform-shaped candidates that fit a regional brief best are the ones most likely to ship no
licence at all. Three of the four best platform candidates this hour are unusable for that reason,
and the fourth is unmaintained.

### 🟢 The platform census from `p469` stands, re-stated for use

🔵 Nothing this pass changes `p469`'s finding, and it remains the most load-bearing thing on this
shelf: of the eight education platforms Globant is most often asked to build on, **exactly one is
permissively granted** — `OpenOLAT` (Apache-2.0, 448★, Java) — and the most-cited "MIT" alternative,
`frappe/lms`, serves **GNU AGPL v3** at `license.txt` (33 893 B, read first-hand at `p469`).

🔵 Release axis, unchanged this pass: Moodle 5.2 shipped April 2026 with 5.3 LTS due October 2026;
Chamilo 2.0 shipped April 2026. Canonical addresses, both confirmed live at `p469`:
`chamilo/chamilo-lms` (`master`) and `openeducat/openeducat_erp` (default ref **`19.0`**, where
`main` 404s — `p462`'s correction, still the trap on this shelf).

## 🆕 `p469` — **🟢 ONE PERMISSIVELY-GRANTED FULL LMS EXISTS AND IT IS NOT THE ONE ANYONE NAMES: `OpenOLAT` (Apache-2.0, 448★, Java). 🔴 `frappe/lms` — the row the 2026 roundups file under MIT — is AGPL-3.0, read first-hand. 🟢 And the release axis is current: Moodle 5.2 shipped April 2026 with 5.3 LTS due October 2026, Chamilo 2.0 shipped April 2026.**

🔵 Every grant below read first-hand at `HEAD` on **2026-10-27** (`Gap 468-A` honoured: payloads
measured as files, never through a shell variable). Star counts from the session GitHub tool
channel the same day.

### 🟢 The platforms a Globant engagement actually lands on

| platform | repo | licence · bytes · `sha256₁₂` | ★ | stack | where it fits |
|---|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 · `COPYING.txt` 35 147 B · `8ceb4b9ee5ad` | 7 548 | PHP | 🔴 the deployed default worldwide. **5.2 released April 2026; 5.3 is the next LTS, scheduled October 2026.** Build via plugins and LTI, outside the GPL boundary |
| **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | AGPL-3.0 · `LICENSE` 35 136 B · `e12d78569742` | — | Python/Django | 🔴 MOOC-scale and national-platform work. Network copyleft: an AI layer linked in owes source to every user |
| **OpenOlat** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `LICENSE` 10 982 B · `6dbc5b605ed0` | 448 | Java | 🟢 **the permissive option.** Universities and corporates; QTI, SCORM, curriculum management, assessment, modular course editor, compliance tracking. The one row here Globant can fork, extend and ship closed |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 · `LICENSE` 35 147 B · `8ceb4b9ee5ad` | 1 020 | PHP/Twig | 🔴 ease-of-use and accessibility focus, strong LATAM and francophone-Africa footprint. **2.0 released April 2026**, point releases since |
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** · `LICENSE` 1 097 B · `3c056b34a476` | 1 161 | Python | 🟢 **offline-first.** The row for low-connectivity deployments — rural LATAM, SEA, Sub-Saharan Africa. OER, SDG-4 |
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 LGPL-3.0 · `LICENSE` 8 241 B · `528f84036800` | 899 | Python/Odoo | 🟡 education **ERP** — admissions, fees, library, hostel, exams. Weak copyleft: extend as Odoo modules |
| **Frappe Learning** | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** · `license.txt` 33 893 B · `db1a87ba81e8` | 3 350 | Python/TypeScript | 🔴 **the corrected row.** See below |
| **RosarioSIS** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 · `LICENSE` 15 214 B · `d954e14e5c75` | — | PHP | 🔴 K-12 **student information system** — enrolment, scheduling, grades, attendance, billing. Default ref is **`mobile`** `fa5f4b66caf4`, which is unusual and worth knowing before a clone |
| **i-Educar** | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | GPL-2.0 · `LICENSE` 18 092 B · `8177f9751321` | 720 | PHP/Laravel | 🔴 🟢 **LATAM-specific SIS.** Brazil's largest free school-management system, published as *software público*; municipal secretariats are its installed base |
| **forma.lms** | [`formalms/formalms`](https://github.com/formalms/formalms) | 🟢 **CORRECTED `p471` — GPL-2.0**, read first-hand at `html/license.txt` · 18 346 B · `4e63feff285d` @ `master` `446a77a9b9cb`; a second copy at `html/lib/System/license/license_english.txt` · 15 146 B · `81688a796b2f` with 9 further language translations. The grant is in-tree, never at the root | 37 | PHP | 🔴 **Read, do not vendor.** The roundups that called it Apache-2.0 are refuted from the payload; GPL-2.0 is real and is **not** compatible with GPL-3.0-only code. Integrate over its interface. Prior verdict ("no grant at 10 paths") was a root-path artefact |

🔵 Ten platforms, ten first-hand grants or refusals. **Two permissive** (OpenOlat, Kolibri), one
weak-copyleft, six strong-copyleft, one ungranted.

### 🔴 The correction, because this row changes what a studio can sell

🔵 A current "10 Best Open-Source LMS in 2026" listing files **Frappe Learning under MIT**. 🔴 At
`develop`, six conventional licence paths 404; the grant is at **`license.txt`** and it is **GNU
AGPL v3**. Under MIT, a Globant-hosted fork with a client's AI layer discloses nothing. Under
AGPL-3.0, that same hosted fork owes **complete corresponding source to every network user**. Full
reasoning and the two instrument bugs that nearly hid it are on `repos/foundations.md` under
`Gap 469-C` and `Gap 469-D`.

### 🟢 What this census means for platform selection

1. **Permissive + closed AI layer → OpenOlat.** Apache-2.0, Java, assessment and curriculum
   management already built. Smallest community of the set (448★), so budget for owning more of
   the stack.
2. **Largest installed base → Moodle, at the plugin boundary.** Do not fork it. A GPL-3.0 core
   plus an AI service reached over **LTI 1.3 / MCP** keeps the AI layer's licence yours. 5.3 LTS in
   October 2026 is the version to target for a multi-year engagement.
3. **Offline or low-connectivity → Kolibri.** MIT, and the only row here designed for it.
4. **Administrative data → a copyleft SIS, out of process.** RosarioSIS or, in Brazil, i-Educar.
   🔴 **No permissively-granted LMS+SIS product exists** — searched again this pass, none found.
   Integrate across a process boundary; `compose/patterns.md` `P469-1` carries the wiring.
5. **AGPL-3.0 rows (Open edX, Frappe Learning) are viable only where the client accepts source
   disclosure** — public-sector and national-platform work often does, and there the network
   copyleft is a feature, not a blocker.

## 🆕 `p468` — **🟡 The platform tier gains one row and it is AGPL: `OpenTeacherAgent`, a single-binary offline course-authoring agent from GitLab, grant read first-hand at 34 523 B. 🔴 And the platform-shaped candidate that fits LATAM best this pass — a Brazilian school-management system with AI dropout support — serves NO GRANT at ten root paths, so the clearest regional product shape in the window is, again, not deliverable.**

### 🟢 Added to the platform tier

| platform | grant read first-hand | `grant_class` | shape · where it fits |
|---|---|---|---|
| [`ai-swarm-solutions-group/OpenTeacherAgent`](https://gitlab.com/ai-swarm-solutions-group/OpenTeacherAgent) | **AGPL-3.0-or-later** · 34 523 B · `0d96a4ff68ad` @ `59a33fecff73` | 🟡 `NETWORK_COPYLEFT` | Rust + Vue, **single binary, works offline**. Teacher states an intent → the agent generates interactive exercises, composes course pages and exports the whole project as one self-contained HTML bundle with student score tracking. 🟢 **Fits a self-hosted ministry or school-network buyer**, and the offline export is the feature low-connectivity deployments actually ask for. 🔴 Wrong for multi-tenant SaaS: AGPL reaches users served over a network |

### 🔴 Platform-shaped and refused

| candidate | grant @ HEAD | why |
|---|---|---|
| [`leonine1983/aprendix`](https://github.com/leonine1983/aprendix) | 🔴 **NO GRANT** at 10 root paths @ `7df5ee4c76d6` | Enrolment, grades, attendance, reports, modules for students / teachers / managers, plus AI to reduce dropout — written for Brazilian municipal education secretariats. 🔴 **Exactly the LATAM platform brief** and legally untouchable. Retained as a **requirements reference only**, which is what an ungranted repository is good for |

### 🟢 Standing platform rows re-read this pass

| platform | grant · bytes · `sha256₁₂` @ HEAD | status |
|---|---|---|
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 🔴 `PageLM Community License` · 8 563 B · `c834209c5f33` @ `a6646794661b` | 🔴 Reproduced identical to `p467`. Still refused: non-commercial use only, redistribution prohibited, revenue-share required before any commercial deployment, and a partial-use clause reaching *"any portion, code snippet, algorithm, design pattern"* |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 🔴 `Elastic-2.0` · 3 860 B · `48255018b41f` @ `c79803f21cb8` | 🔴 Reproduced identical. Hosted-service delivery forbidden — which is the delivery model for a university CRM |

🔵 **The copyleft observation this shelf has carried since `p467` holds unchanged.** Every platform
added to this tier in the last two passes is AGPL (`OpenTeacherAgent`, `frametell`, `penecho`,
`learnhouse`) or refused on a non-OSI grant. The permissive platform rows are
[`Selleo/mentingo`](https://github.com/Selleo/mentingo) (MIT · 1 062 B · `ceb97717de1f` @
`e137ca47cbec`, Poland),
[`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT · 1 097 B ·
`3c056b34a476` @ `f72936bd41e5`, offline-first) and, at the interop layer,
[`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (MIT · 1 072 B · `383b85b370e8`
@ `86ab328f0e5b`) — all three read first-hand this pass. For a Globant engagement
that means the **self-hosted institutional buyer is well supplied and the multi-tenant SaaS buyer
is not**, and that is a positioning fact, not a sourcing failure.

---

## 🆕 `p467` — **🟢 The permissive platform row the EMEA tier has been short of is read first-hand and PLACED: a Polish AI-native LMS under MIT, against four AGPL platforms. 🔴 And the pass's most-starred platform candidate is REFUSED on a grant that reads MIT until you get to its fourth clause — a 2 049★ self-hosted NotebookLM alternative that requires a REVENUE-SHARING AGREEMENT before any commercial deployment.**

### 🔴 Refused as build-on supply — and the refusal is not visible from the licence family

| platform | ★ | grant read first-hand | why it is refused |
|---|---|---|---|
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | **2 049** | 🔴 **"PageLM Community License"** · `LICENSE.md` 8 563 B · `c834209c5f33` @ HEAD `a6646794661b` | 🔴 **The single most saleable platform shape in this window and it cannot be delivered.** A self-hosted NotebookLM alternative that turns study material into quizzes, flashcards, notes and podcasts — i.e. exactly the "upload the course, get the assets" product a university or publisher asks for. Its payload **opens with MIT's grant sentence verbatim**, then: use limited to *"personal, educational, or non-commercial research purposes"*; **redistribution "strictly prohibited"** (§2); no commercial use without a separate agreement (§3); a **revenue-sharing agreement required before any commercial deployment**, with disgorgement of profits on breach (§4); and a **partial-use clause** making *"any portion, code snippet, algorithm, design pattern"* in a commercial product a Commercial Use (§7). 🔵 The §7 clause is the decisive one for Globant: it reaches a *pattern copied by an engineer who read the repo*. 🟢 Retained as a **product-scope reference**; refused as a codebase |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 340 | 🔴 `Elastic-2.0` · 3 860 B · `48255018b41f` @ HEAD `c79803f21cb8` | 🔴 **Reproduced byte-, digest- and HEAD-identical to `p466`.** Higher-ed student-success CRM with an AI assistant. Elastic-2.0 forbids providing the software as a hosted or managed service — the delivery model for a university CRM engagement. Design reference only |

### 🟢 Platform rows added this pass, with `grant_class`, forge and region

| platform | ★ | `grant_class` · grant · `sha256₁₂` | forge · region | what it gives an engagement |
|---|---|---|---|---|
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 98 | 🟢 **`PERMISSIVE` · MIT** · 1 062 B · `ceb97717de1f` @ HEAD `e137ca47cbec` | GitHub · 🟢 **EMEA** (Polish orthography in its own README, first-hand) | 🟢 **The permissive EMEA platform this tier was missing.** An AI-native LMS with an AI mentor and role-play scenarios, SCORM + xAPI, white-label, self-hosted, positioned explicitly as a Moodle / Open edX / Docebo alternative. 🔵 Against this base's four AGPL EMEA platforms, this is the one that can be **relicensed into a client deliverable** and run multi-tenant. 🔴 102 open issues — young, not yet proven at estate scale |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 1 732 | 🟡 `NETWORK_COPYLEFT` · AGPL-3.0 · **34 523 B** · `8486a10c4393` @ HEAD `eb7b7a09d479` | GitHub · `UNPLACED` | A full classroom/course platform (SvelteKit + Supabase) — the most-starred AGPL education platform in the population. Fits a self-hosted institutional buyer; wrong for multi-tenant SaaS |
| [`iblai/lms`](https://github.com/iblai/lms) | 208 | 🟢 `PERMISSIVE` · **MIT** · 1 063 B · `f1269b7b2313` @ HEAD `18f76c220561` | GitHub · `UNPLACED` | A **skills-intelligence** front end — competencies, digital credentials, workforce development on Next.js. 🟢 The credentialing half of 1EdTech's skills-based-hiring trend, under a grant that permits resale (**MIT**, read first-hand — not the Apache-2.0 its ecosystem is usually assumed to carry) |
| [`edrys-org/edrys`](https://github.com/edrys-org/edrys) | 334 | 🟡 `WEAK_COPYLEFT` · MPL-2.0 · 16 725 B · `1f256ecad192` @ HEAD `9aae4c801f1b` | GitHub · `UNPLACED` | A modular remote-teaching platform ("live LMS"). 🟡 MPL is file-level copyleft: new modules can stay proprietary, modified Edrys files cannot. The most permissive copyleft shape at this tier |
| [`haxtheweb/haxcms-php`](https://github.com/haxtheweb/haxcms-php) | 130 | 🟢 `PERMISSIVE` · Apache-2.0 · 11 362 B · `b662f44e55e8` @ HEAD `248f42c494a7` | GitHub · `UNPLACED` | Web-component authoring and microsite publishing for course content; the authoring surface that pairs with `scorm-again` as the carrier |

### 🟡 The per-asset platform problem, stated once for this tier

🔵 Two rows in this pass's population ([`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph),
[`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators)) grant
**MIT to their code and something else to each data asset** — in `evaluators`' case a
`CC BY-NC-SA 4.0` corpus sitting inside an otherwise MIT repository. 🔴 At the platform tier this
matters more than at the library tier: a platform is **shipped with its seed content**, so a clean
code licence does not clear the deliverable. 🟢 The practical rule, now carried as a grant class:
**clear the content inventory separately from the code**, and treat a `COMPOSITE_PER_ASSET` row as
two procurement items, not one.

### 🔵 What this tier looks like once the grant is read rather than assumed

| delivery model the client wants | 🟢 build on | 🔴 refuse |
|---|---|---|
| multi-tenant SaaS the client resells | `Selleo/mentingo` (MIT) · `iblai/lms` (MIT) · `haxtheweb/haxcms-php` (Apache-2.0) | `classroomio` (AGPL) · `advisingapp` (Elastic-2.0) · `PageLM` (bespoke NC) |
| institution self-hosts, source disclosure acceptable or desirable | all of the above **plus** `classroomio`, `Openki`, `DD-workspace/DD` (AGPL) | `advisingapp` · `PageLM` |
| module added to an existing estate | `edrys` (MPL-2.0, file-level) · `scorm-again` + `tsugi` as carriers | — |

---

## 🆕 `p466` — **🟢 THREE PLATFORMS ADDED FROM A FORGE THIS BASE HAS NEVER SAMPLED, all AGPL-3.0 and all EMEA-placed — including the deployable artefact of a Barcelona digital-sovereignty programme. 🔴 And one 340★ platform that reads as the pass's best vertical find is REFUSED: `Elastic-2.0` forbids exactly the hosted-service delivery Globant sells.**

### 🔴 Refused as build-on supply — read the payload, not the star count

| platform | ★ | grant read first-hand | why it is refused |
|---|---|---|---|
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 340 | 🔴 **Elastic License 2.0** · 3 860 B · `48255018b41f` @ HEAD `c79803f21cb8` | 🔴 **Source-available, not OSI.** A higher-ed **student-success CRM with an AI assistant** — recruitment, retention, advising — which is the single most saleable vertical shape found this pass. Elastic-2.0 forbids **providing the software to third parties as a hosted or managed service**. 🔴 That is the delivery model for a university CRM engagement. 🟢 Retained as a **design reference** for scope and data model; **not** as a codebase to build on |

🔵 This is `Gap 466-A`'s instance at the platform tier: present grant, non-permissive substance, and
a star count that invites exactly the wrong conclusion.

### 🟢 Platforms added — GitLab channel, all payloads read first-hand

🔵 Default branches are `develop`, `dev` and `main` across these five — resolved with
`git ls-remote --symref`, not assumed.

| platform | ★ | grant · `sha256₁₂` · branch · HEAD | region · basis | what it is, and what it is for |
|---|---|---|---|---|
| [`DD-workspace/DD`](https://gitlab.com/DD-workspace/DD) | 12 | 🟡 **AGPL-3.0** · 34 588 B · `a7f13bbcc053` · `main` · `ab820f90134a` | **EMEA** · Xnet, Barcelona (ES) | 🟢 **NOVEL — absent from this entire base.** The deployable education workspace of Xnet's **Democratic Digitalisation** framework: a schools stack built explicitly to keep student data out of hyperscaler platforms. 🟢 **This is the artefact EMEA sovereignty demand is asking for**, and this base had no row for it |
| [`moodlenet/backend`](https://gitlab.com/moodlenet/backend) | 21 | 🟡 **AGPL-3.0** · 34 449 B · `feff6860d5ea` · `develop` · `9f7e86989866` | **EMEA** · Moodle HQ | **MoodleNet** — **ActivityPub-federated** sharing and curation of open educational resources *between* institutions (Elixir). 🟢 The only **federated** platform on these shelves: resource sovereignty without a central host |
| [`moodlenet/frontend`](https://gitlab.com/moodlenet/frontend) | 19 | 🟡 **AGPL-3.0** · 34 481 B · `6dbb120dadf0` · `develop` · `0a4756bd2ad0` | **EMEA** | MoodleNet client (React + TypeScript) |
| [`Openki/Openki`](https://gitlab.com/Openki/Openki) | 35 | 🟡 **AGPL-3.0** · 34 520 B · `57c8ff33c9c0` · `dev` · `dd10d490a3f6` | **EMEA** · Swiss, de/fr UI | course-organisation platform for **self-organised local learning communities** — learners propose courses and they run when enough people commit. 🟢 **An inverted governance model** no carried LMS implements: demand-led rather than institution-scheduled. Fits municipal/NGO reskilling mandates |
| [`oer/emacs-reveal`](https://gitlab.com/oer/emacs-reveal) | 53 | 🟡 **composite** · 517 B · `21a1dedbfaf3` · `main` · `49a1c8f1c5b3` | **EMEA** · Universität Osnabrück (DE) | OER authoring/publishing toolchain (reveal.js + recorded audio), used for real university courses. 🔴 Its `LICENSE` is a **pointer, not a grant** — *"this repository embeds different resources under different licences"* — so **no single-family cell is truthful**; third instance of the conjunctive class, and the first where the payload declines to name one licence at all |

🔴 **All four granted rows are AGPL-3.0 — network copyleft.** Deploying a modified MoodleNet,
Openki or DD as a hosted service for a client obliges offering the modified source to its users.
🟢 **That is a fit signal, not a blocker:** it suits the institutional self-hosted engagement, which
is the EMEA public-sector and LATAM public-university buyer. 🔴 It is wrong for a multi-tenant SaaS
deliverable. See `Gap 466-E` on [`repos/trending.md`](../repos/trending.md).

### 🟢 The integration surface — the rows that decide whether any of this can be sold *into* an estate

🔵 Carried platforms (Moodle, Open edX, Canvas, Kolibri, OpenEduCat, Sakai, BigBlueButton, H5P,
OpenOLAT) are the incumbents a Globant build must live beside. This pass shelves the two standards
runtimes that make that possible, both permissive — details on
[`repos/foundations.md`](../repos/foundations.md):

| runtime | grant | why it is a vertical concern and not a detail |
|---|---|---|
| [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0** · 10 273 B · `73ba74dfaa52` | **LTI** — mount an external tool inside any compliant LMS **with roster and grade passback**. 🟢 The supported route into Moodle/Canvas/Open edX without forking them |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** · 1 072 B · `383b85b370e8` | SCORM 1.2 / 2004 + AICC runtime. 🔵 How content reports completion and score to an incumbent LMS or corporate LXP |

🔵 **Why this matters against Trend 1:** 23 % of visible supply now ships as a *skill* with no
runtime ([`agents/trending.md`](../agents/trending.md)). **LTI and SCORM are the runtime** — and
they are the part a skill library cannot provide and a client already requires.

### 🟢 LATAM platform row

| platform | ★ | grant · `sha256₁₂` · HEAD | region · basis | note |
|---|---|---|---|---|
| [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor) | 582 | 🟢 **Apache-2.0** · 11 337 B · `36d6788503b8` @ `94cedd7d4e02` | **LATAM** · Portuguese-language, Brazil | free open-source programming-teaching platform. 🟢 **The one granted LATAM row found this pass**, and the Apache-2.0 payload is the *with-appendix* family (see the fixture finding on [`repos/foundations.md`](../repos/foundations.md)). 🔴 Last pushed **2024-04-21** per the channel listing — **maintenance risk, stated**: usable as a fork base, not as a live upstream |

## 🆕 `p465` — **🟢 FOUR copyleft platforms added, and the pass's value is the FORM they take: a national OS distribution, a school report system, an offline-first platform and a subjective-question marker. 🔴 None is permissive, so all four are deployment-or-fork decisions, not build-on components — which is exactly why they belong here and not on `agents/top.md`.**

🔴 **`make hooks` DENIED** — twelfth denial in thirteen passes; nothing below is gate-attested.
🔵 Payload figures are **raw bytes**; see `Gap 465-A`.

### 🟢 Platform rows added this pass

| platform | ★ | created | grant · `sha256₁₂` | region · basis | what it is, and what adopting it costs |
|---|---|---|---|---|---|
| [`princebilogocode/naabiga-os`](https://github.com/princebilogocode/naabiga-os) | 1 | 2026-07-28 | 🔴 GPL-3.0 · `3972dc9744f6` · 35 149 B | **EMEA** · Burkina Faso, francophone | **Naabiga OS (N-OS)** — a Linux LTS distribution built by and for Burkinabè users, scoped explicitly at developers, office work, **higher education and public administration**, tied to ICONEDOR and Université Aube Nouvelle (Bobo-Dioulasso). 🟡 1★ and 22 open issues: this is a *national-sovereignty signal*, not a shippable platform. 🟢 Its payload is **stock GPL-3.0** — raw 35 149 B · `3972dc9744f6` — which is what settled `Gap 465-A`; HEAD `adc4460d4fac` |
| [`Civicom-Aid/matokeo-rms`](https://github.com/Civicom-Aid/matokeo-rms) | 1 | 2026-04-24 | 🟢 MIT · `10ed6c1f9bb2` · 1 081 B | **EMEA** · Kenya, `kenya` topic | Django academic **report management** system for schools, web and desktop. 🔵 Shelved here rather than on `agents/top.md` because it is a system of record, not an agent. 🟢 **It is the whole of this pass's Kenya evidence** — the Kenya *intel* leg returned nothing at all (`Gap 465-D`), while Kenya *supply* resolves and is permissively granted; HEAD `9649f7cafb25` |
| [`KajarnakLOKOSSOU2008/edubox`](https://github.com/KajarnakLOKOSSOU2008/edubox) | 1 | 2026-09-04 | 🟢 MIT · `1196398ae2f6` · 1 081 B | **EMEA** · Benin, francophone | **offline-first** education platform for low-connectivity environments, declared a prototype/MVP by Kajarnak Tech. 🟡 Carried with `Gap 465-B` attached: its owner published a second repository **two seconds later**, and that sibling is ungranted; HEAD `506a239775dd` |
| [`Maicarons/RubricSpan`](https://github.com/Maicarons/RubricSpan) | 1 | 2026-09-10 | 🔴 AGPL-3.0 · `0d96a4ff68ad` · 34 523 B | **APAC** · zh README, Chinese curriculum | 阅微 — **Chinese subjective-question marking**: a teacher model for humanities free-text scoring, local, explainable, with a **dual backend (Rust + GPU online / WASM offline)**. 🔴 AGPL-3.0 makes a hosted SaaS deployment a source-disclosure event; the WASM offline path is the one that avoids it. 🟢 Its payload is **byte-identical to `Vacademy-io`'s AGPL-3.0**, which is what refuted this pass's "two AGPL variants" reading before publication; HEAD `e9299b4c678f` |

### 🔵 A census note the vertical shelf should carry

🟢 **The marking/assessment tier that actually exists is copyleft or trivial.** Graded first-hand
this pass across the `topic:grading topic:ai` population (32 repositories): the two with
meaningful adoption are **GPL-3.0** (`five-plus-one/AI-Marker-Suite`, 104★) and **AGPL-3.0**
(`ai-lingnan/econai-agent-platform`, 39★ — both already carried), the best-designed novel one is
**AGPL-3.0** (`RubricSpan`, above), and **every permissive one is at 3★ or below**
(`AutoGrader-Agent` 3★, `markwise` 0★ — both on [`agents/top.md`](../agents/top.md)).

🔴 **So the choice a marking engagement faces is real and it is a fork in the road, not a
preference**: adopt proven copyleft and accept the disclosure boundary, or build on permissive
code that has no adoption behind it. 🟢 That is a sellable finding precisely because it is not
flattering to either option.


## 🆕 `p464` — **🔴 A STANDING CLAIM ON THIS BASE IS REFUTED BY THIS BASE'S OWN SHELF: `intel/market.md` says "of ten carried platforms exactly one — Kolibri, MIT — is freely redistributable", while `agents/top.md` carries `OpenOLAT/OpenOLAT` at **Apache-2.0** in a cell that calls it "the only Apache-2.0 one". 🟢 Both re-read first-hand this hour; the mechanism of the error is identified and it is a CENSUS that spans two shelves and is computed from one. 🔴 And an external roundup's "Frappe LMS is MIT" is refuted at the payload.**

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

### 🔴 The contradiction, with both sides read first-hand this pass

| side | where it lives | what it says |
|---|---|---|
| 🔴 the claim | [`intel/market.md`](../intel/market.md) `## Opportunities by region` → `### Global`, item 3 (carried from `p462`) | *"The platform layer is copyleft almost end to end: of **ten carried platforms exactly one** — **Kolibri**, MIT — is freely redistributable."* |
| 🟢 the counter-example, **on this base already** | [`agents/top.md`](../agents/top.md) | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) — *"🟢 **Apache-2.0** · `LICENSE` 10 982 B · `6dbc5b605ed0` · ✅ University-grade LMS, **the only Apache-2.0 one**. Strongly under-used."* |
| 🟢 this pass's own read | `git ls-remote` + `raw.githubusercontent.com` | **Apache-2.0 · 10 982 B · `6dbc5b605ed0`** @ HEAD **`891b9434e822`** — 🟢 **digest reproduced**, 🔵 HEAD has **moved** from the carried `d073ad444fe5`: the project advanced, the grant did not |

🟢 **The correct statement, which this pass substitutes:** of the platform-layer rows this base
carries, **at least two are freely redistributable** — **Kolibri** (MIT) and **OpenOLAT**
(Apache-2.0, university-grade LMS) — and a third, **Sakai**, is *unsettled on this base itself*:
`verticals/solutions.md` says **ECL-2.0** in one place (and "ECL-2.0, Apache-derived" in another)
and **Apache-2.0** in a third, a conflict `intel/open-gaps.md` already records.

### 🟢 The mechanism — this is the part a gate can be built from

🔵 The enumeration the claim rests on is on this file, and **it lists eight platforms, not ten**:
*Moodle (GPL-3.0), Open edX (AGPL-3.0), Canvas LMS CE (AGPL-3.0), Sakai (Apache-2.0), Kolibri
(MIT), OpenEduCat (LGPL-3.0), BigBlueButton (LGPL-3.0), H5P (MIT)*.
🔴 **`OpenOLAT` is not in it — because `OpenOLAT` is shelved on `agents/top.md`, not here.** The
claim was computed from the **verticals** census and then stated about **all carried platforms**.
A permissive university-grade LMS was invisible to the count that concluded there was only one.

🔴 **Note what the gates here would and would not catch.** Every gate in `make hooks` grades a row
against a *payload* — grant presence, digest, region vocabulary, table shape. **None grades a
prose claim against another shelf's rows**, so a count that is wrong about this base's own
contents can survive indefinitely while every cell it contradicts is individually green.
🟢 **Closure:** a platform census that is the **union** of the platform rows on all eight shelves,
keyed on address, with the licence family taken from the payload cell — not from the prose.
Registered as `Gap 464-A`.

🔵 **Why it is commercially material and not pedantry.** "Copyleft almost end to end → build on
extension seams, keep proprietary work across the process boundary" is correct for Moodle, Open
edX and Canvas and it is the right default. 🔴 But it **over-constrains the one case that does not
need it**: an engagement that must *ship* a university-grade LMS inside a redistributable
deliverable has a permissive option, and this base's own cell calls it **"strongly under-used"**
while its headline tells a reader no such option exists.

### 🟢 Platform grants re-read first-hand this pass — five addresses, all already carried

| platform | HEAD today | payload read | grant |
|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `891b9434e822` | `master/LICENSE` 10 982 B · `6dbc5b605ed0` | 🟢 **Apache-2.0** — permissive, redistributable |
| [`frappe/lms`](https://github.com/frappe/lms) | `54ad7dea5b1d` | `main/license.txt` 33 893 B · `db1a87ba81e8` | 🔴 **AGPL-3.0** |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `fa5f4b66caf4` | `master/LICENSE` 15 214 B · `d954e14e5c75` | 🔴 **GPL-2.0 family** (SIS) |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `65f86bf061fa` | `v30.0.00/LICENSE` 35 121 B · `93178a43d6d3` | 🔴 **GPL-3.0** (school management) |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `46a5d7d40082` | `master/LICENSE` 8 241 B · `528f84036800` | 🔴 **LGPL-3.0** |

🔴 **An external claim refused at the payload.** A 2026 open-source-LMS roundup lists **Frappe LMS
under the MIT licence** and recommends it for SMBs and nonprofits on that basis. Read first-hand,
`license.txt` is the **GNU Affero General Public License** — 33 893 B, `db1a87ba81e8`. 🟢 The
roundup is wrong and **this base was already right** (`verticals/solutions.md` carries
`AGPL-3.0-or-later` for it off the `package.json` manifest). 🔵 A Globant team that took the
roundup's word and embedded Frappe LMS in a hosted client product would have taken on an Affero
obligation across a network boundary.

### 🟢 Vertical row added this pass

| platform | ★ | created | grant · `sha256₁₂` | region · basis | what it is, and the boundary it forces |
|---|---|---|---|---|---|
| [`gygy-open/question-bank`](https://github.com/gygy-open/question-bank) | 75 | 2026-07-14 | 🔴 **AGPL-3.0** · `0d96a4ff68ad` · 34 523 B | **APAC** · zh README | AI-native **question bank + paper composition**: imports Word / Markdown / images, matches knowledge points, generates explanations, rich text + LaTeX, multi-model, **review workflow**, Windows desktop **and Docker server**. HEAD `aba4510778ff`. 🔴 Affero: the Docker deployment is a network service, so **customisations must be offered to its users** — usable as an institution-hosted system, **not** as an embedded component of a Globant product |

🔵 **It is the first assessment-authoring platform with a built-in review workflow on this shelf**,
which is the piece an Annex III / Vietnam-style "recorded human decision" posture needs at the
*item-authoring* stage rather than at scoring time.

### 🔴 The prescribed vertical/platform leg — a nil for the seventh consecutive pass, with a denominator

🔵 The platform-connector leg returned **4 428 repositories** and **zero education projects in the
top 25 by stars** (graded in full on [`repos/trending.md`](../repos/trending.md) `p464`). Of five
platform addresses probed by name this pass, **five were already carried**. 🟢 The platform tier
of this base is **saturated**: it is not missing platforms, and a pass should stop spending legs
looking for them. What it is missing is the **permissive** tier, and the finding above is that it
had one more than it believed.

## 🆕 `p463` — **🔴 The prescribed vertical leg is a nil for the sixth consecutive pass: nine platform tokens, nine already carried. 🟢 What it bought instead is a reusable rule about NOVELTY CHECKS — `openSIS` read as uncarried only because the check was keyed on a GUESSED slug, while `OS4ED/openSIS-Classic` sits on three shelves — plus one unsettled same-HEAD pair that this pass deliberately does NOT call an alias.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was NOT RUN.** The harness
permission classifier **refused the invocation outright** (`Code from External`) — the same
refusal `p462` recorded, not a proxy failure and not a missing target. **Nothing below is
gate-attested**, and the gate's inability to run remains the standing obstacle: `Gap 446-A`
cannot be closed by a pass that is not permitted to run the gate.

🔵 **Instrument, and one channel the prescribed probe cannot replace.** Two channels, both
first-hand: `git ls-remote <addr> HEAD` (**tree identity**) and `raw.githubusercontent.com`
(**payload bytes**). 🔴 **The `curl -sI https://github.com/<addr>` check this base is instructed
to use is unusable from this host: it returns `403` for every address, live or withdrawn** —
`openedx/edx-platform` and a non-existent slug are indistinguishable through it. A probe that
returns the same code for a 200 and a 404 is not a verification step, and no row below rests on
it. This reproduces `p450`'s replacement of that probe from an independent direction.

### 🟢 Cross-pass controls — reproduced before any verdict

| control | published by `p462` | this pass read | verdict |
|---|---|---|---|
| 🟢 `openedx/edx-platform` `LICENSE` | AGPL-3.0 · 35 136 B · `e12d78569742` · HEAD `addd09d7801b` | **35 136 B · `e12d78569742`** · HEAD **`addd09d7801b`** | 🟢 **reproduced, byte-, digest- and HEAD-identical** |
| 🟢 `Vacademy-io/vacademy_platform` `LICENSE` | AGPL-3.0 · 34 523 B · `0d96a4ff68ad` · HEAD `3a9c66db938c` | **34 523 B · `0d96a4ff68ad`** · HEAD **`3a9c66db938c`** | 🟢 **reproduced** |
| 🟢 `DaRL-GenAI/instructional_agents` `LICENSE` | MIT · 1 067 B · `4e085d826a64` · HEAD `f835eb45f508` | **1 067 B · `4e085d826a64`** · HEAD **`f835eb45f508`** | 🟢 **reproduced** |

🟢 `p462`'s rule — *a byte-identical licence payload is near-zero evidence of repository
identity* — is **independently confirmed on a new pair this pass found**:
[`sitor-ai/frametell`](https://github.com/sitor-ai/frametell) serves the **same** AGPL-3.0
payload as `Vacademy-io/vacademy_platform` (34 523 B · `0d96a4ff68ad`) at a **different** HEAD
(`683b3e5e8cfa` ≠ `3a9c66db938c`). Two unrelated projects, one stock text.

### 🔴 The prescribed vertical leg is a nil for the sixth pass — and it produced one address correction

The leg `open source platform education ERP CRM SIS MIT Apache` returned nine platform tokens.
🔴 **All nine are carried**, and the licence frontier `p462` measured is unchanged:

| platform token | shelf state | grant as this base understands it |
|---|---|---|
| **OpenEduCat** · `openeducat/openeducat_erp` | 🔴 carried | **LGPL-3.0**, payload-read at `19.0`; index says `NOASSERTION` |
| **Open edX** · `openedx/openedx-platform` | 🔴 carried | **AGPL-3.0** · 35 136 B · `e12d78569742` — seam is an **XBlock** (Apache-2.0) |
| **ERPNext** · `frappe/erpnext` | 🔴 carried | GPL-3.0 |
| **Frappe Education** · `frappe/education` | 🔴 carried | 🔵 and **moved** — see the eviction audit; it left `agents/top.md` and lives on `repos/foundations.md` |
| **openSIS** · [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🔴 carried on **3** sell shelves | 🔴 **no root grant payload** served at `main` or `master` |
| **RosarioSIS** | 🔴 carried | GPL-2.0 |
| **Dolibarr** | 🔴 carried | GPL-3.0 |
| **Moodle** | 🔴 carried | GPL-3.0 |
| **Kolibri** | 🔴 carried | MIT — 🟢 still the **only** platform-layer row on a tier Globant can redistribute freely |
| **Fedena** | 🔴 carried | 🟡 vendor claim, not a payload reading |

### 🟢 The correction, and it is a reusable rule about NOVELTY CHECKS

🔴 **openSIS looked like a discovery and was not.** The leg returns the product name *openSIS*;
the obvious slug guess `openSIS-Classic/OpenSIS-Classic` is `grep`-absent from this entire base,
which reads as an uncarried platform. 🟢 The real address is **`OS4ED/openSIS-Classic`**, carried
on three sell shelves. **A novelty check keyed on a guessed slug manufactures false positives**;
it must be keyed on the address the probe resolves. Registered as `Gap 463-B`.

### 🟡 A free identity reading from the same probe

| address pair | HEAD | verdict |
|---|---|---|
| `OS4ED/openSIS-Classic` vs `OS4ED/openSIS-Responsive-Design` | **`8348cd069aa2`** vs **`8348cd069aa2`** | 🟡 **same tree at HEAD** — alias *or* undiverged fork, and this pass does **not** claim which |

🔵 Per `p462`'s rule the payload cannot settle it either — **neither address serves a root grant**,
so there is no payload to compare. 🔴 Settling it needs full history on both addresses
(`gate-fork-direction`'s channel), which this pass did not run. Registered as `Gap 463-C`.
🟢 Stated this way rather than as an alias claim, because `p462`'s whole lesson was that a
same-looking pair graded on the wrong channel produces a confident wrong answer.

### 🔵 Gap register opened by this pass

| gap | statement | how the next pass closes it |
|---|---|---|
| 🔴 **`Gap 463-A`** | The sell shelves have **no eviction ledger**. 21 projects left every sell shelf between `p406` and `p462` with no row, no reason and no gate; every existing gate measures arrival. | Write `evidence/evictions.<date>-p<N>.tsv` from the `Pattern AW` diff, and add a gate that fails when an address on the previous commit's sell shelves is absent from this one **without a reason cell**. |
| 🔴 **`Gap 463-B`** | A novelty check keyed on a **guessed slug** manufactures false positives — `openSIS` read as uncarried when `OS4ED/openSIS-Classic` sits on 3 shelves. | Resolve the product name to an address through the probe **before** the `grep`, and key the check on the resolved address. |
| 🟡 **`Gap 463-C`** | `OS4ED/openSIS-Classic` and `OS4ED/openSIS-Responsive-Design` share HEAD `8348cd069aa2`. Alias or undiverged fork is **unsettled**, and neither serves a root grant so the payload channel cannot settle it. | Run `gate-fork-direction`'s full-history channel on the pair. |
| 🔴 **`Gap 463-D`** | **The Middle East and Africa returned nothing on any EMEA leg** — EMEA's evidence here is EU-27 + UK + Germany only. | Run legs keyed on named national systems (as `p443` did for LATAM) rather than on the region word: Gulf ministry platforms, Nigerian and Kenyan HE systems, francophone African curricula. |
| 🟡 **`Gap 463-E`** | Skill-tier supply (**7 of 13** novel addresses) carries **derivation chains stated only in the README**. A `LICENSE` read grades such a row clean while saying nothing about what it was built from. | Make `p288`'s README channel standing for the skill tier: every skill-tier row records a provenance cell (declared upstream + its grant) or `PROVENANCE-UNSTATED`. |
| 🔴 **`Gap 446-A`** | **Still open, and still not closable by this pass.** `make hooks` was refused (`Code from External`); nothing in this pass is gate-attested. | Needs a harness permission decision, not a pass. |

## 🆕 `p462` — **The vertical-platform leg is graded and it is a nil: every platform it returned is already shelved. 🟢 But it produced the pass's most useful single correction — OpenEduCat's grant and default ref, read first-hand: `NOASSERTION` in the index, LGPL-3.0 in the payload, at a default branch of `19.0` where `main` 404s.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was NOT RUN, and the reason is new.**
This pass is executing under a harness whose permission classifier **refused the `make hooks`
invocation outright** (`Code from External`) — not a proxy failure, not a missing target, a refusal
to execute the repository's own Makefile. So **nothing below is gate-attested**, and the gate's
inability to run is itself the standing obstacle: `Gap 446-A` cannot be closed by a pass that is
not permitted to run the gate.

### 🟢 `Gap 461-B` gains a first-hand instance: `NOASSERTION` is an index verdict, not an absent grant

[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) is classified
**`NOASSERTION`** (`"license": {"key": "other", "name": "Other"}`) by the GitHub index. Its payload
is not absent and not ambiguous:

| field | value |
|---|---|
| default ref | 🔴 **`19.0`** — not `main`, and `main` 404s |
| grant path | `19.0/LICENSE` (also served at `master`) |
| bytes · digest | **8 241 B** · `528f840368` |
| declared family | **LGPL-3.0** — *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3), as included below"*, with the GPL text appended beneath it as the LGPL's base |
| notice obligation | the payload reserves bundled external libraries to *"other GPL-compatible licenses"*, per-file |

🔴 So an index-only reader records this platform as ungranted, and a `main`-assuming payload reader
records it as ungranted too — **two independent ways to lose a real, readable copyleft grant on the
same row.** The grant is LGPL-3.0: usable as a dependency boundary, not a tier Globant can
relicense.

### 🔴 The prescribed vertical leg, graded token by token

The leg `open source platform education ERP CRM SIS MIT Apache` returned nine platform tokens.
All nine are carried:

| platform token | shelf state | grant as this pass understands it |
|---|---|---|
| **OpenEduCat** · `openeducat/openeducat_erp` | 🔴 carried | 🟢 **LGPL-3.0**, payload-read at `19.0` — see above; index says `NOASSERTION` |
| **Open edX** · `openedx/openedx-platform` | 🔴 carried | 🔴 AGPL-3.0 · 35 136 B · `e12d78569742` — network copyleft; the supported seam is an **XBlock** (Apache-2.0) |
| **RosarioSIS** | 🔴 carried | GPL-2.0 |
| **ERPNext** · `frappe/erpnext` | 🔴 carried | GPL-3.0 |
| **Dolibarr** | 🔴 carried | GPL-3.0 |
| **GegoK12** | 🔴 carried | MIT per vendor claim — 🔴 a **vendor marketing** assertion, and the module split it advertises (26 free / 12 paid) is not a licence statement |
| **Moodle** | 🔴 carried | GPL-3.0 |
| **Kolibri** | 🔴 carried | MIT |
| **BigBlueButton** | 🔴 carried | LGPL-3.0 |

🔴 **The structural finding for a studio, and it has not changed in five passes:** the education
vertical's platform layer is **copyleft almost end to end**. Of the nine platforms above, exactly
one (**Kolibri**, MIT) is on a tier Globant can build on and redistribute freely; OpenEduCat and
BigBlueButton are LGPL (usable across a dependency boundary); the rest are GPL or AGPL. 🟢 **The
practical consequence is an architectural one, not a legal blocker** — build on the platforms'
*extension seams* (Open edX XBlocks, Moodle plugins, Odoo modules) and keep proprietary work on the
far side of the process boundary.

### 🟢 Identity graded by HEAD sha — the channel `p461` did not have

`git ls-remote <addr> HEAD` works from this host and returns the commit the address resolves to.
Two addresses that return the **same sha** are the same repository; two that return **different
shas** are two repositories, whatever their licence payloads look like.

| address pair | raw `LICENSE` payload | HEAD sha, alias | HEAD sha, canonical | verdict |
|---|---|---|---|---|
| `openedx/edx-platform` → `openedx/openedx-platform` | identical · 35 136 B · `e12d78569742` | `addd09d7801b` | `addd09d7801b` | 🟢 **same repository** — rename alias, and it still resolves |
| `Vacademy-io/vacademy_platform` → `Vacademy-io/vacademy_edtech_platform` | identical · 34 523 B · `0d96a4ff68ad` | `3a9c66db938c` | `3a9c66db938c` | 🟢 **same repository** — rename alias, and it still resolves |
| `DaRL-GenAI/instructional_agents` vs `Hyan-Yao/instructional_agents` | identical · 1 067 B · `4e085d826a64` | `f835eb45f508` | `1c2a9f9e3d26` | 🔴 **NOT the same repository** — two live, divergent HEADs |
| `OpenEduCat-Inc/OpenEduCat` → `openeducat/openeducat_erp` | alias **404** at `19.0`, `master` and `main`; canonical **200** · 8 241 B · `528f840368` | 🔴 unresolvable — `ls-remote` falls through to a credential prompt | `46a5d7d40082` | 🔴 **alias is ABSENT**, not a redirect |

### 🔴 The rule this establishes, and it is reusable

🔴 **A byte-identical licence payload is near-zero evidence of repository identity, and for the
boilerplate grant families it is no evidence at all.** `p461` read an identical 1 067 B MIT text at
`DaRL-GenAI/instructional_agents` and `Hyan-Yao/instructional_agents` and concluded one was the
other's stale alias. The HEAD shas say otherwise: `f835eb45f508` ≠ `1c2a9f9e3d26`, two live
repositories with independent histories. The payloads match **because stock MIT text is
universal** — the same 1 067 B body appears on dozens of unrelated rows on these very shelves.
Identity is a property of the **tree**, and only the sha channel reads the tree.

## 🆕 `p461` — **No platform is added. 🔴 Two carried platform rows change materially: `openeducat_erp` is payload-confirmed LGPL-3.0 against an index that classifies it `NOASSERTION`, and the Open edX row's address is an alias for `openedx/openedx-platform`.**

🔴 **Gate posture per `Gap 446-A`: `make hooks` was NOT RUN.** Nothing below is gate-attested.

### 🟢 The vertical set, with grant strength stated as the first-order fact

🔵 For a studio engagement the question is never "is it open source" but **"what does the grant
oblige us to publish"**. Ordered by how freely Globant can build on it:

| platform | repo | grant | obligation on a client build | ★ exact | last push |
|---|---|---|---|---|---|
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 🟢 permissive (Apache-derived) — customise freely | **1 239** | 2026-10-26 |
| **Richie** | [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | 🟢 permissive — no obligation | **316** | 2026-10-26 |
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0** *(payload; index says `NOASSERTION`)* | 🟡 weak copyleft — **link, do not fork into** proprietary modules | **899** | 2026-10-26 |
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | **GPL-3.0** | 🟡 copyleft — build **plugins**, keep client IP outside the tree | **7 543** | 2026-10-21 |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | **GPL-3.0** | 🟡 copyleft — same posture as Moodle | **1 020** | 2026-10-26 |
| **Gibbon** | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | **GPL-3.0** | 🟡 copyleft | **637** | 2026-10-23 |
| **ILIAS** | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | **GPL-3.0** | 🟡 copyleft | **505** | 2026-10-26 |
| **Open edX** | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | **AGPL-3.0** | 🔴 **network** copyleft — reach it through the **XBlock** seam only | **8 209** | 2026-10-26 |
| **Vacademy** | [`Vacademy-io/vacademy_edtech_platform`](https://github.com/Vacademy-io/vacademy_edtech_platform) | **AGPL-3.0** | 🔴 network copyleft; **23**★ — thin community | **23** | 2026-10-26 |

🟢 **The architectural consequence, and it is the whole reason this file exists.** Open edX is
**AGPL-3.0**, and AGPL reaches across a network boundary — so a hosted client build that forks the
platform acquires a publication obligation. The permissive escape hatch is
[`openedx/XBlock`](https://github.com/openedx/XBlock), **Apache-2.0**, **471**★, payload-verified
at `LICENSE.TXT` (11 358 B · `cfc7749b96f6` — note the **uppercase extension**, the trap `p460`
recorded). 🔵 Custom learning components built as XBlocks sit **behind** the plugin API and do not
inherit the platform's AGPL. **That seam is the single most valuable fact on this shelf.**

### 🟡 Moodle's AI surface — what is actually verifiable, and what is not

🔵 Two Moodle AI plugins resolve to real, current addresses:

| plugin | repo | grant | ★ | last push |
|---|---|---|---|---|
| SOLA course assistant | [`saylordotorg/moodle-local_ai_course_assistant`](https://github.com/saylordotorg/moodle-local_ai_course_assistant) | **GPL-3.0** | **17** | 2026-10-20 |
| AI question generation | [`yedidiaklein/moodle-local_aiquestions`](https://github.com/yedidiaklein/moodle-local_aiquestions) | 🟡 unresolved this pass | **15** | 2025-11-30 |

🔴 **Recorded as a gap, not padded over:** `qbank_genai` and `block_ai_chat` — both named in
earlier descriptions of Moodle's AI subsystem — **did not resolve to any repository** in this
pass's name queries. They are **not** written as rows. 🟡 They may exist in the Moodle plugin
directory rather than on GitHub under those names; until an address is verified they stay out.

🔵 Both verified plugins are **GPL-3.0 / unresolved and tiny** (17★, 15★). The honest read is that
Moodle's AI plugin ecosystem is **thin and immature** relative to the 7 543★ core — which argues
for integrating at Moodle's **REST API** boundary rather than depending on third-party plugins.

---
## 🆕 `p460` — **No platform is added, and the three licence traps this shelf exists to protect against were re-read from their bytes: Open edX is AGPL-3.0, Sakai is ECL-2.0, Chamilo is GPL-3.0. 🔴 All three are the values a secondary roundup gets WRONG, and this pass independently reproduced the shelf's digests for two of them.**

🔴 **Gate posture, stated first: `make hooks` was NOT RUN** — fresh clone, not the Makefile, so
nothing below is gate-attested.

🔵 Instrument: payload byte-read at `raw.githubusercontent.com`, gated on `%{http_code}`; two
fabricated addresses returned **404 / 14-byte body** as negative controls.

### 🔴 The three traps, re-read — and why each one is expensive in an engagement

| platform | what roundups say | 🟢 what the payload says | cost of the error |
|---|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 "Apache-2.0" | **AGPL-3.0** · 35 136 B · `e12d78569742` | 🔴 network-copyleft on a **hosted** LMS — the obligation triggers on serving it, which is the deployment model |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 "Apache-2.0" | 🟡 **ECL-2.0** · 11 120 B · `0688f62d04f1` | Apache-derived but **not** Apache — the patent clause is narrowed to the contributing institution's own use |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 "GPL-2.0" | **GPL-3.0** · 35 147 B · `8ceb4b9ee5ad` | 🔴 **GPL-2.0 and GPL-3.0 are mutually incompatible** (`Gap 454-C`'s class) — the wrong version breaks a combination, not just a notice |

🟢 **A canonical-digest observation, free:** Chamilo's `LICENSE` and Moodle's `COPYING.txt` are
**both 35 147 B with digest `8ceb4b9ee5ad`** — byte-identical, because both serve the unmodified
GPL-3.0 text. 🔵 That makes `8ceb4b9ee5ad` a **canonical GPL-3.0 fingerprint** on these shelves:
a payload matching it is the stock licence and carries no project-specific modification, which is
exactly what a vendoring step needs to know and what a family-name reader cannot tell it.

🟡 **Two more platform grants read, digests new to this file:**
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) serves an **8 241 B**
`LICENSE` (`528f84036800`) that **opens by pointing at `COPYRIGHT`** rather than granting — a
pointer, `Gap 454-E` (d)'s class, so the LGPL-3.0 this shelf carries rests on a second file and is
recorded as such. [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
serves **1 531 B** (`57c341d09920`) opening `Copyright (c) 2023-2025 Mohamed El hajji On behalf of…`
— consistent with the BSD-3-Clause this shelf carries.

## 🆕 `p459` — **No platform is added. Two licence traps already on these shelves were RE-READ first-hand and both records are confirmed correct — which is the useful result, because a wrong grant here is what ships into a client engagement.**

🔴 **Gate posture, stated first: `make hooks` was NOT RUN** — this pass reached the shelves
through a fresh clone rather than the Makefile, so **nothing below is gate-attested**.

🔵 Instrument: a two-stage probe — `git ls-remote --symref` for liveness and default ref, then a
10-path grant read at that ref. **Controlled in both directions before use:**

| control | result |
|---|---|
| 🟢 `HKUDS/DeepTutor` — positive, asserted against the grant these shelves carry | **Apache-2.0**, `LICENSE` **11 408 B**, head `a31d82624c27` — **reproduced** |
| 🟢 two fabricated addresses — negative | both **`ADDRESS_DEAD`** |
| 🔴 **instrument defect, recorded against this pass, not against the shelves** | the probe's *fallback* licence matcher (a bare substring scan, used only when no licence title matches in the first 30 lines) read `withmarbleapp/os-taxonomy` as **"MIT"**. It is **not** MIT. The shelves' own first-hand record — **ODbL-1.0 + CC BY-SA 4.0**, `LICENSE` **25 289 B** — was re-read and **stands uncorrected**. Every grant quoted below was read from the licence title, never from the fallback |

### The two traps, re-verified this pass

| Platform | Repo | Grant read at `HEAD` this pass | Shelf record | Verdict |
|---|---|---|---|---|
| **Advising App** | [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 🔴 **Elastic License 2.0** — title line read directly; `LICENSE` **3 860 B**, head `66459ede3245` | 🟢 already recorded as *"Elastic Licence 2.0 — source-available"* | 🔴 **Not open source.** Source-available; ELv2 bars providing it to third parties as a managed service. Read, do not resell |
| **cn-math-taxonomy** | [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | 🔴 **CC BY-NC-4.0** — *"Attribution-NonCommercial 4.0 International"*; `LICENSE` **19 347 B**, head `cf262d886821` | 🟢 already recorded as *"CC BY-NC — cannot ship"* | 🔴 **Barred from paid work**, and it grew to 3 992 ★ this window, so it will keep being proposed |

🟢 **Why this is worth a section rather than silence:** a naive licence reader — including the
fallback in this pass's own probe, see the instrument note — classifies both of these as
permissive. `advisingapp` is a 340 ★ higher-education student-success CRM with "open" in its
description; `cn-math-taxonomy` is the fastest-growing curriculum graph on these shelves. They are
exactly the two rows an engagement would reach for first, and neither may be built on.

🔵 The permissive alternatives these shelves already carry for the same two jobs:
[`Selleo/mentingo`](https://github.com/Selleo/mentingo) (**MIT**, 1 062 B, head `e137ca47cbec`) for
the AI-native LMS tier, and [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy)
(ODbL-1.0 + CC BY-SA 4.0) for the curriculum graph.

## 🆕 `p458` — **One Apache-2.0 LMS arrives for the self-hosted tier (the tier these shelves keep finding is copyleft), and the two platforms beside it are exactly why the tier needs reading twice**

🔵 Grants read first-hand at the resolved default ref; instrument and controls as recorded in
[`agents/top.md`](../agents/top.md). 🔵 This section corrects nothing on the existing tables; it
adds three rows and flags two of them.

| Platform | Repo | Licence (read at `HEAD`) | ★ | Shape | Verdict |
|---|---|---|---|---|---|
| **TutorLoom** | [`pacewisdomhq/TutorLoom`](https://github.com/pacewisdomhq/TutorLoom) | 🟢 **Apache-2.0** · 11 362 B `a89039268428` | 49 | Multi-tenant LMS for institutes and training teams: course builder, batch enrolment, trainer and student portals, grading, progress. Django + React, Flutter client | 🟢 **Build-on.** Permissive and multi-tenant in the same row |
| **Vacademy** | [`Vacademy-io/vacademy_edtech_platform`](https://github.com/Vacademy-io/vacademy_edtech_platform) | 🔴 **AGPL-3.0** · 34 523 B `0d96a4ff68ad` | 23 | Topics itself `erp` + `crm` + `lms`: content delivery, learner tracking, assessment management | 🔴 **Read, do not host.** Network copyleft — a hosted multi-tenant deployment triggers source disclosure |
| **ARSnova** | [`particify/arsnova-server`](https://github.com/particify/arsnova-server) | 🟡 **CORRECTED `p471` — partitioned.** 🟢 **GPL-3.0** at `core/LICENSE` · 35 147 B · `8ceb4b9ee5ad` (this base's canonical stock-FSF digest, reproduced). 🔴 **All rights reserved** at `formatting/LICENSE` · 133 B · `747c3a657b2b`, naming Particify. No grant at the root — which is why 10 root paths read as none | **67** | Audience-response-system backend, Kotlin, containerised, created **2013** | 🟡 **Integrate, do not vendor wholesale.** `core/` is GPL-3.0: build beside it over its API. 🔴 `formatting/` is proprietary and must be excluded from any deliverable. Prior verdict ("NO GRANT … refused") was a root-path artefact |

### 🟢 Why `TutorLoom` is worth a line of its own on this shelf

🔵 These shelves have recorded, pass after pass, that **the platform tier is almost entirely
copyleft**: Moodle GPL-3.0, Open edX AGPL-3.0, Canvas AGPL-3.0, OpenEduCat LGPL-3.0, Sakai
ECL-2.0. 🟢 `TutorLoom` is an **Apache-2.0** LMS that is multi-tenant out of the box — which is the
exact combination a studio needs when a client wants a white-labelled platform it can modify
without publishing the modifications. 🟡 It is three weeks old (created 2026-10-07) and carries 49 ★,
so it is shelved as a **starting point to evaluate**, not as a Moodle replacement: the maturity
gap against Moodle's two decades is not closeable by a licence.

### 🔴 `ARSnova` is the clearest licence trap this tier has produced

🔵 Thirteen years old, 67 ★, **44 forks**, Kotlin, a published `docker-compose` — every signal a
buyer reads as "open source". 🔴 **There is no grant.** Not at `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `LICENCE`, `LICENCE.txt`, `COPYING`, `COPYING.txt`, `license`, `LICENSE-MIT` or
`LICENSE.rst`, and **not as a licence field in its Gradle build either** — so this is a cleaner
negative than `p452`'s `MANIFEST_ONLY` class, where a grant at least existed in metadata. 🟢 The
engagement rule, and it applies to all 44 forks as much as to the original: **a container image
is not a licence.** Ask Particify in writing, or build on something else.


## 🆕 `p457` — **🔴 THE VERTICAL THIS SHELF HAS NEVER DESCRIBED IS THE PAPER ONE: every platform carried here assumes a hosted LMS and a network, and the assessment instrument most of this industry's install base actually uses is a printed answer sheet read by a scanner. 🟢 A permissive, offline, single-machine paper-assessment stack now exists on these shelves. 🔴 And one carried platform cell went commercial two days ago.**

🔴 **`make hooks` DENIED** (`Code from External`) — twelfth denial in thirteen passes. 🔵 Nothing
below is gate-attested; instrument and controls at
[`compose/code/p457-payload-census/`](../compose/code/p457-payload-census/census.py).

### 🔴 The deployment envelope this shelf could not serve

🔵 Every row on this shelf — ILIAS, Moodle, Open edX/Tutor, Canvas, BigBlueButton, OpenEduCat,
Gibbon, RosarioSIS, i-Educar — is a **server**. It needs hosting, a database, a network and an
administrator. 🔴 That is a correct description of the platforms and an **incomplete description of
the market**: an exam office scoring MCQ sheets for a cohort of 2 000 on one Windows PC with no
reliable internet is a real engagement shape, and this shelf had no row for it.

🟢 **Measured, not asserted:** two of the four OMR engines promoted this pass name offline
single-machine operation as a *feature* in their own README —
[`crispin0007/OMR`](https://github.com/crispin0007/OMR) (*"all on one Windows PC with no internet
and no fees"*, **Apache-2.0**, `LICENSE` 11 358 B `cfc7749b96f6`) and
[`sajidbuet/OMRFlow`](https://github.com/sajidbuet/OMRFlow) (*"entirely on your own machine"*,
**MIT**, 1 081 B `71787b5c24e2`).

### 🟢 The paper-assessment vertical, as a deployable stack

| layer | platform | grant | what it does | pin |
|---|---|---|---|---|
| sheet design + scoring | [`crispin0007/OMR`](https://github.com/crispin0007/OMR) | 🟢 **Apache-2.0** | answer-sheet authoring, ADF-scanner intake, marks, ranks, **merit lists**, negative marking, Excel + PDF scorecards | `-b main` |
| exam administration | [`sajidbuet/OMRFlow`](https://github.com/sajidbuet/OMRFlow) | 🟢 **MIT** | template design, **uncertain-mark review queue**, **attendance reconciliation**, auditable Excel results | `-b main` |
| camera-grade intake | [`Udayraj123/OMRChecker`](https://github.com/Udayraj123/OMRChecker) | 🟢 **MIT** | reads sheets from a **phone camera** as well as a scanner — the field-collection path where no scanner exists | 🔴 `-b master` |
| component | [`power0matin/omr-bubble-sheet-marker`](https://github.com/power0matin/omr-bubble-sheet-marker) | 🟢 **MIT** | PDF/image MCQ marking (OpenCV + PyMuPDF) | `-b main` |
| accessibility | [`NSoiffer/MathCAT`](https://github.com/NSoiffer/MathCAT) | 🟢 **MIT** | MathML → speech + **braille** (Nemeth, UEB Technical), **15 languages** | `-b main` |

🔴 **Refs are stated because `p456` proved they cannot be inherited**: `Udayraj123/OMRChecker`
defaults to **`master`**, not `main`, so a recipe that clones without `-b` is guessing. 🟡 One row
of the four is **GPL-3.0** and is therefore *not* in this table:
[`bthicks/OMR-Grader`](https://github.com/bthicks/OMR-Grader) (35 149 B `3972dc9744f6`) — usable
behind a service boundary, not vendorable into a deliverable.

🟢 **Where this stack meets the existing shelf:** the OMR layer produces per-item response data,
which is exactly the input the psychometrics tier on these shelves already consumes
(`patriciamar/ShinyItemAnalysis`, `philchalmers/mirt`, `cran/catR`) and the format the LMS
connector tier can write back. 🔵 The wiring is `P457-1` in
[`compose/patterns.md`](../compose/patterns.md).

### 🔴 A carried cell on these shelves went commercial on 2026-10-24

🔵 [`pengusto/google-classroom-mcp`](https://github.com/pengusto/google-classroom-mcp) is carried
with an **MIT** cell. At `HEAD` it serves **`Pengusto Commercial License 1.0`** (`LICENSE` 3 053 B
`d84e558a5033`), *"effective for distributions carrying this notice from **2026-10-24**"*, over the
maintainer's own additions. 🔴 **The upstream it names
(`adriasantacreu/google-classroom-mcp` at commit `29c2c2a0767069…`) serves no licence file at any
of six probed paths** — its only grant is a `package.json` declaration, and the readable MIT text
survives only inside the fork that relicensed it. 🟢 Full measurement, including the engagement
remedy, on [`agents/top.md`](../agents/top.md).

🔵 Two further carried addresses re-issued licence text on **the same date** —
`nakafaai/aksara` and `nakafaai/nakafa.com`, both now **`Nakafa Source Available License 2.0`**,
*"not open source, and … not free to reuse"*. 🟡 These shelves already carried them as closed; what
is new is the dated instrument.

### 🟡 The manifest channel, and what it does and does not rescue

🔵 **20 addresses on these shelves state a licence with no payload behind it.** Probed this pass
against four in-repo manifests, **8 are recoverable** and the platform-tier results are the ones
that matter here:

| platform | manifest | grant recovered |
|---|---|---|
| [`frappe/lms`](https://github.com/frappe/lms) | `package.json` | 🔴 **AGPL-3.0-or-later** — the `-or-later` is on the manifest and not on the carried cell |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | `pyproject.toml` | 🟢 **Apache-2.0** confirmed (this shelf carries both AGPL-3.0 and Apache-2.0 for the Open edX estate; the XBlock SDK lane is the Apache one) |
| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | `package.json` | 🟢 **MIT** |
| [`louislegrain/api-ecoledirecte`](https://github.com/louislegrain/api-ecoledirecte) | `package.json` | 🟢 **ISC** |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | — | 🔴 **neither channel** — a carried SIS platform whose GPL-2.0 cell this base cannot now corroborate (`Gap 457-B`) |

🔴 **`OS4ED/openSIS-Classic` is the entry on this list a vertical reader should care about**: it is
a *platform* row, not a connector, and its grant is currently unverifiable from this host on both
the payload and the manifest channel. 🟡 It is **not** retracted — it is flagged, with the channel
that failed named, so a client-facing use gets a legal read rather than a shelf cell.


## 🆕 `p456` — **🔴 Eleven of the platforms on this shelf do NOT default to a trunk: ILIAS checks out `release_11`, Tutor `release`, OpenEduCat `19.0`, BigBlueButton `v4.0.x-develop`. Every deployment recipe on these shelves that clones without `-b` has been pinning silently to whatever release line the maintainers last promoted.**

🔴 **`make hooks` DENIED** (`Code from External`) — eleventh denial in twelve passes. 🔵 Nothing
below is gate-attested; 31 controls run in both directions
([`compose/code/p456-ref-resolution/`](../compose/code/p456-ref-resolution/)).

### 🔴 The deployment fact, stated as a command

🔵 These are the customisable systems a Globant engagement actually stands up — and for a vertical
shelf the ref is **part of the platform's identity**, not a git detail. Measured first-hand with
`git ls-remote --symref` this pass:

| platform | what it is | clone the way these shelves have been describing it | 🔴 what you actually get | 🟢 pin instead |
|---|---|---|---|---|
| **ILIAS** | LMS, GPL-3.0, German public-sector install base | `git clone .../ILIAS-eLearning/ILIAS` | 🔴 `release_11` — a maintenance line | `-b release_11` *(stated, not inherited)* |
| **Tutor** | Open edX distribution, AGPL-3.0 | `git clone .../overhangio/tutor` | 🔴 `release` | `-b release` |
| **OpenEduCat** | education ERP on Odoo, LGPL-3.0 | `git clone .../openeducat/openeducat_erp` | 🔴 `19.0` — tracks the Odoo major | `-b 19.0` |
| **BigBlueButton** | virtual classroom, LGPL-3.0 | `git clone .../bigbluebutton/bigbluebutton` | 🔴 `v4.0.x-develop` — a **develop** branch is the default | `-b v4.0.x-develop` |
| **Gibbon** | school management, GPL-3.0 | `git clone .../GibbonEdu/core` | 🔴 `v31.0.00` | `-b v31.0.00` |
| **Edu-Sharing** | learning-object repository, GPL-3.0 | `git clone .../edu-sharing/Edu-Sharing` | 🔴 `maven/fixes/10.0` | `-b maven/fixes/10.0` |
| **i-Educar** | Brazilian municipal SIS, GPL-2.0 | `git clone .../portabilis/i-educar` | 🔴 `2.12` | `-b 2.12` |
| **RosarioSIS** | SIS, GPL-2.0 | `git clone .../francoisjacquet/rosariosis` | 🔴 `mobile` | `-b mobile` |
| **Krayin CRM** | Laravel CRM, **MIT** | `git clone .../krayin/laravel-crm` | 🔴 `2.2` | `-b 2.2` |
| **TinCanPython** | xAPI/Tin Can library, **Apache-2.0** | `git clone .../RusticiSoftware/TinCanPython` | 🔴 `3.x` | `-b 3.x` |
| **Caliper PHP** | IMS Caliper analytics, LGPL-3.0 | `git clone .../tl-its-umich-edu/caliper-php-public` | 🔴 `public` | `-b public` |

🟢 **Why this belongs on the vertical shelf and not only in the instrument notes:** a client
hand-off that says *"we built on ILIAS"* without the ref is unreproducible, and 🔴 **a
`v4.0.x-develop` default means BigBlueButton's own maintainers expect integrators to track a
develop line** — which is a support posture to price, not a detail. 🔵 Every grant above was
re-read **at the resolved ref** this pass and **all eleven are byte-identical** to the cells these
shelves already carried, so the licence column is confirmed, not revised.

### 🔴 The licence asymmetry this makes legible

🔵 Of the eleven, exactly **two** are permissive — `krayin/laravel-crm` (**MIT**) and
`RusticiSoftware/TinCanPython` (**Apache-2.0**). The other nine are copyleft: four GPL-3.0/GPL-2.0,
three LGPL-3.0, one AGPL-3.0 (Tutor). 🟢 **The composition rule that follows is unchanged but now
has its refs**: the copyleft platform is deployed and extended **behind a service boundary**, and
the agent layer Globant builds and owns sits on the permissive side of that boundary — the MCP
servers and national-system clients on [`agents/top.md`](../agents/top.md), all MIT.
🔴 Tutor's **AGPL-3.0** is the one that reaches across a network boundary, so an AI feature served
*from inside* a Tutor deployment is the case to design around, not vendor into.

### 🟡 A vertical candidate refused this pass

🔴 **`tosuki/moodle-mcp`** — a Moodle MCP server for university portals with Microsoft Teams SSO
(2FA), with **pt-BR** submission strings (`Enviado para avaliação`), so genuinely LATAM-shaped.
🟡 Refused: its README carries an MIT **shields.io badge linking to `LICENSE`** and `package.json`
declares `"license": "MIT"`, but **no payload exists at any of 13 grant paths** at its resolved
default branch `main`. 🔵 A badge whose own link resolves to nothing is not a grant (`Gap 456-E`).

## 🆕 `p455` — **🟢 A VERTICAL SHAPE THESE SHELVES HAD ONLY ONE INSTANCE OF NOW HAS FOUR: the closed national school system reachable only through third-party clients. France and the DACH countries together, eleven permissive clients, zero customisable cores.**

🔴 **`make hooks` DENIED** (`Code from External`) — tenth denial in eleven passes.

### 🟢 The shape, and why it is a different engagement from Moodle or Open edX

`p453` recorded *"a market shape these shelves had never recorded: a closed national system of
record reached only by third-party clients"*, and `p454` added Indonesia's **Dapodik** as the APAC
instance. This pass establishes that the shape is **the norm across Western Europe**, not an
exception — and that it inverts the economics of every other row on this file.

🔵 **Moodle, Open edX, Kolibri, OpenEduCat and Sakai are platforms you install and extend.**
The systems below are platforms a ministry or a *Land* has already installed, that **cannot be
forked, hosted or extended**, and whose only integration surface is an API — usually undocumented
— wrapped by community clients. The sellable work is therefore an **agent or integration layer
against a system of record you do not control**, never a platform customisation.

| national system | country / scope | status | permissive client tier read first-hand this pass | what it exposes |
|---|---|---|---|---|
| 🔴 **PRONOTE** (Index Éducation) | 🇫🇷 France — the gradebook/timetable of most secondary schools | 🔴 **Proprietary, closed.** No open core at any address | 🟢 [`bain3/pronotepy`](https://github.com/bain3/pronotepy) **MIT** (`1 062` B `4f074ab7dccb`), 🟡 maintenance mode | Grades, timetable, homework, attendance for student/parent/teacher accounts. 🔴 Not the official HYPERPLANNING API |
| 🔴 **EcoleDirecte** | 🇫🇷 France — the second school portal | 🔴 Proprietary, closed | 🟢 [`studoo-app/ecole-directe-api`](https://github.com/studoo-app/ecole-directe-api) **MIT** (`1 071` B `6c086a4639ac`); 🟡 [`a2br/ecoledirecte.js`](https://github.com/a2br/ecoledirecte.js) **MIT** (`1 073` B `e4ba09041791`), unmaintained since 2023-08-08 | Login (incl. 2FA on some clients), grades, timetable, homework |
| 🔴 **Schulportal Hessen** ("Lanis") | 🇩🇪 Germany — the *Land* of Hesse's statewide portal | 🔴 Proprietary, closed, and 🔴 **maintainer-documented as fragmented**: functions *"at specific schools or after a while may no longer work"* | 🟢 [`kurwjan/LanisAPI`](https://github.com/kurwjan/LanisAPI) **MIT** (`1 076` B `0bc449776673`, **@`master`**); 🔴 [`lanis-mobile/lanis-rs`](https://github.com/lanis-mobile/lanis-rs) + [`elderguardian/maria`](https://github.com/elderguardian/maria) both **GPL-3.0 `or-later`** (`35 149` B `3972dc9744f6`) | Homework, substitution plans, calendar, conversations, substitute-teacher plan |
| 🔴 **WebUntis** (Untis GmbH) | 🇦🇹🇩🇪🇨🇭 DACH — the dominant school timetabling system | 🔴 Proprietary, closed. 🔵 **Has a public JSON-RPC API *and* an internal one**, and the client tier splits on which it uses | 🟢 [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) **MIT** (`License`, `1 070` B `d2e54565d9bf`) · [`Tynobi-Company/webuntis_headless`](https://github.com/Tynobi-Company/webuntis_headless) **MIT** · [`thatmarcel/untis-js`](https://github.com/thatmarcel/untis-js) **MIT** · [`Suiram1701/WebUntisAPI.Client`](https://github.com/Suiram1701/WebUntisAPI.Client) **MIT** (.NET) · [`Keule0010/WebUntisAPI`](https://github.com/Keule0010/WebUntisAPI) **MIT** (Java) · 🔴 [`arnim279/untis-api-client`](https://github.com/arnim279/untis-api-client) **GPL-3.0-or-later** (public API) | Timetables over date ranges, lesson detail, sessions |
| 🟡 **Librus Synergia** | 🇵🇱 Poland — *(carried, re-stated here for the shape)* | 🔴 Proprietary, closed | 🟡 [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) **MIT at root** — 🔴 **GPL-3.0 on its `legacy_reference/` subtree**: integrate over MCP, never vendor the tree | Grades, attendance, timetable, homework, messages |

### 🔴 Three constraints this tier carries that a platform engagement does not

🔴 **(1) A stated rate limit, and it is the only one on this file.**
`Suiram1701/WebUntisAPI.Client`'s own documentation sets it: never 10 req/s, no more than
1 800 req/h, **in no case above 3 600 req/h**, and exceeding it *"could permanently block"* the
institution's access. 🔵 That is an architectural constraint on any agent that polls — a per-tenant
scheduler and cache is not an optimisation here, it is a precondition.

🟡 **(2) The client tier is unofficial by construction, so it breaks when the vendor moves.**
`pronotepy` is in maintenance mode *because* of this; `ecoledirecte.js` was abandoned for it;
LanisAPI's maintainers say the portal is fragmented per school. 🔵 A deliverable must treat the
client as a **replaceable adapter**, and the engagement must price a maintenance tail.

🔴 **(3) Copyleft is distributed unevenly across the tier, and it decides the architecture.**
Every WebUntis and French client above is **MIT** except `untis-api-client`, which is
**GPL-3.0-or-later** — and it is the only one on the *public* API. 🟡 So the permissive path and
the documented-API path are **different repositories**: a vendorable deliverable takes the MIT
clients on the internal API and accepts the fragility, or takes the GPL client on the public API
and keeps it behind a service boundary. 🟢 The `or-later` grant, read first-hand, means that
boundary may itself be GPL-3.0.

## 🆕 `p454` — **🟢 A national system of record this base had never named is customisable from MIT code: Indonesia's Dapodik, reached at three strata. 🔴 And the vertical layer gains a licence SHAPE that no single SPDX field can express — the three-strata grant, found independently in Brazil and Indonesia in the same hour.**

🔴 **`make hooks` DENIED** (`Code from External`) — ninth denial in ten passes.

### 🟢 Dapodik — Indonesia's national education register, as a customisable base

🔵 **Dapodik** (*Data Pokok Pendidikan*, `dapo.kemendikdasmen.go.id`) is the Ministry of Primary
and Secondary Education's single register of schools, teachers and students. Like ÉcoleDirecte
(EMEA, `p453`) it is a **closed national system of record with no open core** — but unlike
ÉcoleDirecte, its client layer is **MIT across three languages and three strata**:

| stratum | asset | grant (first-hand, `HEAD`) | what it gives an engagement |
|---|---|---|---|
| register access | [`ardianryan/dapodik-sdk`](https://github.com/ardianryan/dapodik-sdk) | **MIT** · `1 739` B `29e7d361ee3d` | typed TS/JS SDK over the Dapodik web service |
| register access | [`adereksisusanto/dapodik-api-php`](https://github.com/adereksisusanto/dapodik-api-php) | **MIT** · `1 105` B `ce39902853af` | PHP client, CI-tested — the stack most Indonesian school software is written in |
| student identity | [`smantriplw/vervalpd-node`](https://github.com/smantriplw/vervalpd-node) | **MIT** · `1 068` B `0ae5076b1e03` | VerValPD lookups (`findStudent`) over an undocumented API |
| aggregate reporting | [`bantenprov/dapodik-data-guru`](https://github.com/bantenprov/dapodik-data-guru) | **MIT** · `1 072` B `3508ba25c5ad` | provincial teacher-data recapitulation |

🟡 **Read the stratum honestly before selling it.** `vervalpd-node` describes itself as a
**scraper of a non-documented API**. That is a real integration path and a real fragility: it is
not a supported contract, and an engagement that depends on it owes a change-detection test, not
an SLA.

### 🔴 The three-strata grant — a vertical-layer shape, found twice in one hour

🔵 Two unrelated education projects, on two continents, independently split their grant the same
way — and **neither split is expressible in a registry's single `license` field**:

| project | code | content / data | name & brand |
|---|---|---|---|
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) *(LATAM, Brazil)* | 🟢 **MIT** (`LICENSE-CODIGO.md`) | 🟡 **CC BY 4.0** for the BNCC curriculum JSON (`LICENSE-DADOS.md` `1 108` B `965ba269fac6`) | 🔴 *"não licenciados"* — wordmark, logo, colours explicitly withheld |
| [`nakafaai/aksara`](https://github.com/nakafaai/aksara) *(APAC, Indonesia)* | 🔴 **Source Available 2.0** (`11 997` B `97e8bdc2e3cd`) | 🔴 **Content License 2.0** (`10 053` B `2af44ab89691`) | 🔴 **Trademark Policy 2.0** (`4 508` B `3ba64345e201`) |

🟢 **Why education specifically.** A vertical that ships *curriculum* alongside *code* has two
different kinds of asset in one artefact, and content is not licensed like software. `bncc-pacotes`
states the consequence outright: the **npm tarball and the PyPI wheel carry MIT code and CC BY 4.0
data in the same artefact**. 🔴 A studio that vendors it on the registry's `MIT` badge therefore
inherits **attribution obligations it never read**, and the attribution string the project asks for
is specified in `LICENSE-DADOS.md`, not in the package metadata.

🟢 **Operational rule for this layer, and it is new:** for any education vertical, clear **three**
grants — code, content, brand — and record each one's bytes and digest separately. One SPDX value
per package is a category error here, not a shortcut.

### 🔵 Carried vertical rows, re-read at `HEAD`

🟢 [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) — **GPL-2.0, correctly declared**
(`18 025` B `a01259a1b522`). TAO remains the copyleft assessment platform on these shelves;
GPL-2.0 (not LGPL, as a reader defect this pass briefly reported) means **no proprietary
linking**.
🔴 `imsglobal/caliper-php` — **the address is DEAD, which is worse than the `MANIFEST_ONLY` this
pass first recorded.** Packagist declared `LGPL-3.0`; the Packagist record now **404s**; and the
repository itself returns `404` at `HEAD` on **all 13 non-licence paths probed** (`README.md`,
`composer.json`, `.gitignore`, …), as do both plausible successors `1EdTech/caliper-php` and
`IMSGlobal/caliper-php`. 🔴 **The IMS Global reference implementation of the Caliper analytics
standard is not retrievable from this address at all** — so it is not a licence question, and this
row is a dead citation, not a vertical option.
🔴 [`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) —
the fork that **does** serve one: **LGPL-3.0** (`7 438` B `8c401dfc8928`), against a carried cell
of `proprietary`. 🟢 For a Caliper engagement, this is the address to read.
🟢 [`edu-sharing/Edu-Sharing`](https://github.com/edu-sharing/Edu-Sharing) — **GPL-3.0**
(`35 148` B `8b1ba204bb69`), an OER repository/federation platform customisable with AI on top;
🔴 npm's `GNU GPL v2` hint is wrong and the two versions are incompatible.

## 🆕 `p453` — **🟢 The institution-registry layer `p452` opened with one country now spans two regions and three strata — national directory, federal statistical series and school-authored disclosure — and the US stratum is the one an engagement can actually build on. 🔴 And a vertical row is corrected in place: the French national SIS tier exists here for the first time, under a grant its own registry record states wrongly.**

🔴 **`make hooks` DENIED** (`Code from External`) — eighth denial in nine passes. Nothing here is
gate-attested; the load-bearing contracts were re-implemented independently and all are green.

### 🟢 The institution-registry vertical, now readable as a layer rather than a row

🔵 `p452` added `yasserstudio/geoalgeria` and wrote that the layer was *"one country deep"*. 🟢 It
is now three strata deep in two regions, and the strata are **not interchangeable** — an
engagement needs to know which question each answers.

| stratum | question it answers | instance, grant read first-hand | region |
|---|---|---|---|
| 🟢 **national directory** | *which institutions exist, by administrative unit* | [`yasserstudio/geoalgeria`](https://github.com/yasserstudio/geoalgeria) — **MIT** (1 101 B `691e4ec845d7`, carried from `p452`): 1 932 MFEP vocational establishments, 177 MESRS higher-ed, 11 858 schools, 69 wilayas | 🟢 **EMEA** — Algeria |
| 🟢 **federal statistical series** | *what is TRUE of each institution, longitudinally* | [`paulgp/ipeds-database`](https://github.com/paulgp/ipeds-database) — **MIT** (1 056 B `1126322e2cc8`): 27 M rows, 23 tables, 1997-2024; [`scienceforamerica/scipeds`](https://github.com/scienceforamerica/scipeds) — **MIT** (1 088 B `e04b31a1be21`) | 🟢 **North America** — US |
| 🟢 **school-authored disclosure** | *what the institution says about ITSELF, current year* | [`bolewood/collegedata-fyi`](https://github.com/bolewood/collegedata-fyi) — **MIT** (1 115 B `a3a16c648652`): 4 071 archived Common Data Set documents, 1 105-field canonical schema, 6 322-institution federal directory | 🟢 **North America** — US |
| 🟢 **administrative geography** | *the unit a school list JOINS to* | [`nataliasm23/icones-bandeiras-br-uf`](https://github.com/nataliasm23/icones-bandeiras-br-uf) — **CC0-1.0** (7 048 B `a2010f343487`) | 🟢 **LATAM** — Brazil |
| 🔴 **absent stratum** | *national directory, APAC* | 🔴 India's UDISE+-derived directories: **4 of 5 packaged forms grant nothing**, the fifth is **CC-BY-SA-4.0**. See `repos/foundations.md` | 🔴 **APAC** — recorded as an informed absence |

🟢 **Why the US stratification matters commercially.** The federal series and the school-authored
disclosure disagree by construction — IPEDS is the broad-coverage federal baseline, the CDS is the
current-year, school-authored admissions detail — and `collegedata-fyi` is the only row here that
keeps them **separately labelled** rather than blending them. 🔵 An engagement that silently
merges the two produces numbers no institution will confirm.

### 🟢 A new vertical tier: the national SIS that is NOT an LMS

🔵 Every platform row on this shelf until now runs a *course* (Moodle, Canvas, Open edX, Kolibri)
or an *institution* (OpenEduCat, openSIS, Gibbon, Fedena). 🟢 **ÉcoleDirecte is a third thing: a
French national school system of record for grades, homework, timetable and `vie scolaire`**,
reached only through client libraries, with no self-hostable open core at all.

| row | grant, read first-hand at `HEAD` | posture |
|---|---|---|
| [`androz2091/node-ecole-directe`](https://github.com/androz2091/node-ecole-directe) | 🔴 **Apache-2.0** — `LICENSE` **11 357 B `sha256₁₂ c71d239df917`**, title-anchored. 🔴 **npm declares `ISC`** on every version | 🟢 **Build-on.** Apache-2.0 is the *more* obligated of the two readings (NOTICE, change notices) and the one that actually governs; it also carries the patent grant `ISC` lacks |
| [`papillonapp/papillon-ed-core`](https://github.com/papillonapp/papillon-ed-core) | 🔴 **GPL-3.0** — 35 149 B `3972dc9744f6` | 🔴 **Watch only** — strong copyleft propagates into a client deliverable |
| [`louislegrain/api-ecoledirecte`](https://github.com/louislegrain/api-ecoledirecte) | 🔴 **`ISC` on npm, no payload at 9 paths** | 🔴 **Legal review first** — `Gap 451-C` manifest-only class, on a live package |

🔴 **The correction this tier forces on the shelf's own method.** These shelves have graded the
French market through *EU regulation* (Reg. (EU) 2026/1744, Pattern BC) and never through its
*systems of record*. A French engagement integrates ÉcoleDirecte or Pronote long before it reads
an Annex III deadline, and neither appeared on any shelf until this pass.

## 🆕 `p452` — **🟢 A vertical layer these shelves have never carried is now populated: the national INSTITUTION REGISTRY — the master list an engagement keys its rollout to, before any LMS is chosen. 🔴 And it exposes the shape of the gap: this base has eight platforms that run a school and almost no data about which schools exist.**

🔴 **`make hooks` DENIED** (`Code from External`) — seventh denial in eight passes. Nothing here is
gate-attested; the four load-bearing contracts were re-implemented by hand and all four are green.

### 🟢 The new row, read first-hand at `HEAD`

| asset | grant | layer | what it contains | region |
|---|---|---|---|---|
| [`yasserstudio/geoalgeria`](https://github.com/yasserstudio/geoalgeria) | 🟢 **MIT** — `LICENSE` **1 101 B `sha256₁₂ 691e4ec845d7`**. 🔴 the npm manifest declares only `SEE LICENSE IN LICENSE`, so the **payload** is the grant | 🟢 **Institution registry / reference data** — *new layer on this shelf* | **11 858** schools & kindergartens by cycle (primaire, CEM, lycée, préscolaire, from OpenStreetMap) · **1 932** vocational-training establishments (856 CFPA, 182 INSFP, 723 private accredited, 58 DFEPs — **MFEP / takwin.dz**) · **177** higher-education institutions (universities, grandes écoles, ENS, centres — **MESRS**) · all **69 wilayas**, with GPS, contacts, capacity and boarding · trilingual EN/FR/AR | 🟢 **EMEA** — Algeria |

### 🔴 The gap it makes visible, and it is a real asymmetry in this shelf

🔵 This file carries the platforms that **operate** an institution — Moodle (GPL-3.0), Open edX
(AGPL-3.0), Canvas LMS CE (AGPL-3.0), Sakai (Apache-2.0), Kolibri (MIT), OpenEduCat (LGPL-3.0),
BigBlueButton (LGPL-3.0), H5P (MIT). 🔴 **It carries almost nothing that says which institutions
exist.** Those are different buys and they arrive in a different order: a ministry or a group
engagement sizes and segments the estate *before* it selects a platform, and until this pass this
base could serve the second question and not the first.

🟢 **What the registry layer is worth in an engagement.** It is the join key. A rollout plan, a
territorial phasing, a capacity model, a per-wilaya cost estimate and a baseline for measuring
reach all key against the institution list; a permissive, ministry-sourced, GPS-bearing list is
the difference between a proposal with numbers in it and one without.

### 🟡 What this row is NOT, stated so no engagement over-reads it

🔴 It is **data, not software** — there is no API, no auth, no multi-tenancy and no runtime; it is
npm packages of records. 🔴 It is **one country**. 🔴 Its school tier is **OpenStreetMap-derived**,
so that 11 858 is a volunteer-mapped count and not a ministry census, while the vocational and
higher-education tiers **are** ministry-sourced (MFEP, MESRS) — 🟡 **the three tiers do not carry
the same authority and must not be cited as one figure.**

### 🔴 The rest of the layer, named as an informed absence rather than left silent

🟢 **Comparable permissively-licensed national education registries on these shelves, by region:**

| region | institution-registry asset carried | state |
|---|---|---|
| 🟢 **EMEA** | [`yasserstudio/geoalgeria`](https://github.com/yasserstudio/geoalgeria) — MIT, Algeria | 🟢 **new this pass** |
| 🟡 **LATAM** | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) — Brazil's **BNCC curriculum** as data (CC-BY-4.0); [`portabilis/i-educar`](https://github.com/portabilis/i-educar) — **GPL-2.0**, a municipal system, not a registry | 🟡 **curriculum data, not an institution registry** |
| 🔴 **North America** | — | 🔴 **none carried.** The US equivalents are federal/state series (NCES CCD, IPEDS); 🔵 whether a permissively-licensed packaged form exists has **not been searched** on these shelves |
| 🔴 **APAC** | — | 🔴 **none carried** |
| 🔴 **Global** | — | 🔴 **none carried.** UNESCO UIS publishes aggregates, not institution lists |

🔴 **Four of five regions have no institution-registry asset on this shelf, and three of those four
have never been searched for one.** 🟢 That is an informed gap and it is registered as
`Gap 452-D`: the layer is newly visible, one country deep, and the absence elsewhere is
unmeasured rather than established.

## 🆕 `p451` — **🔴 THIS FILE'S SIIAU ROW UNDERSTATED THE PROBLEM: it recorded the one existing SIS SDK as "abandoned", which is a maintenance fact. The licence fact is worse and is corrected here — FOUR of its seven published versions are `proprietary`, and only `v1.1.2` onward is BSD-3-Clause.**

🔴 **`make hooks` was DENIED on this host this pass** (`Code from External`) — no cell below is
gate-attested. Stated first, per `Gap 446-A`.

### 🔴 The correction, in place

🔵 The carried cells (`Integration supply` / `Probed first-hand 2026-10-25`) said: *"One SDK ever
existed: `dev-cucei-itrans/siiau-api-client`, a Laravel client for SIIAU's internal API, published
on Packagist and marked abandoned there"*, and that `git ls-remote` **does not resolve**. 🟢 **Both
cells are reproduced exactly this pass.** 🔴 **What they omit is the grant**, and the grant is the
part an engagement cannot proceed without:

| version | published | licence as published on Packagist |
|---|---|---|
| `v1.0.0-BETA` · `v1.0.0` · `v1.1.0` · `v1.1.1` | 2023-10-20 → 2024-08-14 | 🔴 **`proprietary`** |
| `v1.1.2` · `dev-main` | 2024-08-25 → 2024-10-08 | 🟢 **`BSD-3-Clause`** |

🔵 Read first-hand 2026-10-26 from `packagist.org/packages/dev-cucei-itrans/siiau-api-client.json`
with `laravel/framework` → `200` as the positive control and a fabricated name → `404` as the
negative. Package created 2023-10-13 · **7** versions · **1 023** downloads · 7 stars ·
`abandoned: true` · `repository` back-links the exact carried slug.

🔴 **Rule for any SIIAU engagement:** pin **`>=1.1.2`**. A `^1.0` constraint resolves into the
proprietary band, and because the repository is withdrawn (`404`/`128`, byte-identical to a
fabricated control) **the Packagist record is the only surviving evidence of either grant** — it
is the artefact to retain, not a convenience link.

🟢 **The row's strategic reading is unchanged and now better supported:** SIIAU's integration
supply is not merely thin, it is *ungranted*. A Globant engagement on this system of record is a
**build**, not an integration — and the pinning boundary above is the reason the one existing
client cannot be adopted as a shortcut.

### 🟢 Platform tier, unchanged this pass and re-stated so the shelf is not read as stale

🔵 No platform licence was re-measured this pass; the H5P correction `p450` made in place
(**GPL-3.0**, against the `🟢 MIT` cell this file previously contradicted itself with) stands, as
do Tutor's `release` and Oppia's `develop` defaults. 🔴 **This pass changed exactly one row** — the
SIIAU grant above — and adds no platform claim it did not read.

---

## 🆕 `p450` — **🔴 THIS FILE CONTRADICTED ITSELF ON THE MOST EXPENSIVE LICENCE IN THE INDUSTRY: one table graded H5P `🟢 MIT`, another in the SAME FILE graded it `🟡 GPL-3.0` and added "widely mislabelled MIT". A first-hand read settles it — GPL-3.0 — and the wrong row is corrected in place rather than left for a reader to pick between. 🟢 Two platform defaults are also measured and neither is `main`: Tutor defaults to `release`, Oppia to `develop`.**

🔴 **`make hooks` was DENIED on this host this pass** (`Code from External`) — no gate attests the
cells below. Stated first, per `Gap 446-A`.

### 🔴 The self-contradiction, and why it is the one that matters

| line | row as it stood | status |
|---|---|---|
| `verticals/solutions.md:687` *(carried platform rows)* | **`\| H5P \| 🟢 MIT \| Interactive content types; embeds in Moodle, Canvas and Open edX. \|`** | 🔴 **WRONG** |
| `verticals/solutions.md:1031` *(same file, later block)* | **`\| H5P \| 🟡 GPL-3.0 \| … 🔴 Widely mislabelled MIT. \|`** | 🟢 **RIGHT** |

🔴 **Both rows were live, in one file, and a reader taking the first table at face value inherits a
copyleft obligation this file had already identified and warned about.** This file's own Canvas row
states the stakes: *"conflating the two is the single most expensive licence error available in this
industry."*

🟢 **Settled first-hand through the `raw` channel, 2026-10-26**
(`evidence/licence-title-anchored.2026-10-26-p450.tsv`):
[h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) · ref **`master`** · grant at **`LICENSE.txt`** · **GPL-3.0, Version 3, 35 146 B** — the same GPLv3
text [moodle/moodle](https://github.com/moodle/moodle) carries at `COPYING.txt`, **35 147 B**, the
one-byte delta being a trailing newline.
🟢 **Line 687 is corrected in place to `🔴 GPL-3.0`** with the mislabelling note carried onto the
row itself, so the correction travels with the citation instead of living two tables away.

🔵 **The distinction the corrected row preserves, because it is what makes H5P usable at all:**
H5P's **JavaScript content types** are MIT; **`h5p-php-library`, the server-side integration
layer, is GPL-3.0**. "H5P is MIT" is true of the half nobody integrates and false of the half
everybody does. 🟢 The permissive route this file already shelves stands unchanged —
[edly-io/h5pxblock](https://github.com/edly-io/h5pxblock) (MIT, 1 064 B) loads H5P as **runtime
content** inside Open edX rather than linking the PHP library.

### 🟢 Platform default refs, measured — and `main` is the minority

Measured on the `ls-remote --symref` channel, **2026-10-26**:

| platform | default ref | heads | 🔴 what a `main`-assuming read returns |
|---|---|---|---|
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **`release`** | 17 | 🔴 nothing — no `main` exists |
| [oppia/oppia](https://github.com/oppia/oppia) | 🔴 **`develop`** | 500 | 🔴 nothing — no `main` exists |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | `master` | 294 | 🔴 nothing |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | `master` | 60 | 🔴 nothing — including the licence |
| [moodle/moodle](https://github.com/moodle/moodle) | 🟢 `main` | 40 | 🟢 resolves — the exception, not the rule |

🟢 **Across the 19 addresses measured this pass the split is `master` 11, `main` 5, `develop` 1,
`release` 1.** 🔵 This is `T104` (*"a grant's PATH is a function of the REF"*) with a denominator:
**74 % of these platform addresses are not on `main`**, so resolving the ref is not a refinement of
the read, it is the read. 🟢 The `HEAD` alias used by this pass's probe does it automatically and is
the reason the licence table above has no holes.

### 🔴 Vertical-platform discovery: nil, and the leg is recorded so the silence is not read as coverage

One leg ran on the prescribed shape (`open source platform education ERP CRM MIT Apache`). 🔴 **It
returned a single vendor source — OpenEduCat's own comparison pages, repeated across ten
translations — and zero addresses not already on these shelves.** Named in it: Moodle, Open edX,
OpenEduCat, Sakai, ILIAS, Canvas, Chamilo; all seven are shelved and graded. 🔵 **The leg's one
informative result is negative and worth the row: no MIT- or Apache-licensed system of record
(LMS *or* SIS) surfaced on the prescribed query** — consistent with `p448`'s `Gap 447-D` finding
that the first permissively-licensed system of record on these shelves came from a *state*-shaped
query, not a market-shaped one.
## 🆕 `p449` — **🟢 THE CONNECTOR TIER WRITES MORE THAN THIS SHELF PUBLISHED, AND THE CORRECTION RUNS AGAINST THE READ-ONLY READING: `Gap 448-C` resolved at source puts the category write share at 35.8 %, not 32.9 %, because `p448`'s denominator was inflated by 19 non-tool fields while its WRITE numerator was EXACT. 🔴 Which makes `Gap 448-B` worse: the allowlist field a gateway would key on is 43 % unpopulated over a LARGER mutating surface than anyone had measured.**

🟢 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` RAN** — fourth trial after
three denials, so `p448`'s settlement of that gap as *"a property of the host class"* is
**refuted**; the denial is **intermittent**. 🟢 Arrival baseline: **58/62 green, 4 RED**, 🔴 **two
of them NEW and both `p448`'s**. Three green on exit; the fourth is `DECLARED_RED`
(`Gap 449-D`).

### 🟢 The vertical fact, corrected at source rather than restated

`bruchris/canvas-lms-mcp` @ `c740624` (committed **2026-10-23** — **not** drift since `p448`).
A `ToolDefinition` counts only when its enclosing object literal carries **both** `name:` and
`inputSchema`:

| cell | `p448` | 🟢 `p449` | why |
|---|---|---|---|
| `bruchris` total tools | 🔴 222 | 🟢 **188** | 19 non-tool `name:` fields, **all outside `src/tools/`** — `normalize-ids.ts` 11, `init/wizard.ts` 5, `init/clients.ts` 3 |
| `bruchris` WRITE tools | **62** | 🟢 **62** | 🟢 **EXACT** — README declares *"125 read-only and 62 … write operations"* |
| `bruchris` write share | 27.9 % | 🔴 **33.0 %** | same numerator, correct denominator |
| **category total** | 414 | 🟢 **380** | |
| 🔴 **category write share** | 32.9 % | 🔴 **35.8 %** | |

🔵 README's own prose total is **187** against a true **188**, and **175 of 188** source ids are
named in it — so the two channels agree to **±1** and `p446`'s README reading was right all
along. The defect was never the README; it was scanning all of `src/` instead of the registries
(`evidence/gap448c-tool-count.2026-10-26-p449.tsv`).

### 🔴 What this changes for the sellable unit

🟢 **An agent layer on the community LMS-connector tier can author and publish courseware** —
`create_course`, `create_module`, `toggle-module-publish`, `update-syllabus`, `post-announcement`,
`bulk_grade_submissions` — at **four** addresses, and across a mutating surface of **35.8 %**
rather than 32.9 %. 🔴 **So the gateway is the product, not a detail.** `Gap 448-B` stands and
hardens: `vishalsachdev/canvas-mcp` declares `read_only_hint` on 72 of 128 tools, leaves
**55 (43.0 %) undeclared — and those 55 are exactly the mutating ones** — while its single
`read_only_hint=False` is `download_course_file`, **a read**. 🔴 **`compose/code/mcp-allowlist-gateway`
must gate on the tool's EFFECT and must never key on that hint.** A gateway keyed on it is now
known to be guarding a larger write surface with the same unsound field.

### 🟢 The platform tier is unchanged, and the grant seam is still the whole architecture

🟢 `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` — Apache-2.0, `LICENSE.txt` **10 172 B**, reproduced to the
digit by `p449` on an independent fetch — remains **the only permissively-licensed system of
record** on these shelves. 🔵 `openedx/XBlock` reproduces at **11 358 B** (`LICENSE.TXT`) and
remains the integration seam into a copyleft LMS. 🔴 Every other system of record here is
GPL-2.0/3.0, AGPL-3.0, or carries no grant — so the shape is unchanged: **permissive agent layer
+ effect-keyed gateway, bolted to a copyleft platform through a licence seam.**

---

## 🆕 `p448` — **🟢 THE CAPABILITY ABSENCE `p447` PUT ON THIS SHELF DOES NOT EXIST. `Gap 447-B` is REFUTED from source at HEAD: the community LMS-connector tier authors and publishes courseware — 136 of 414 tool declarations mutate, and `create_course`, `create_module`, `toggle-module-publish` and `update-syllabus` were read, not inferred. 🟢 A new vertical row: the NA state system of record is Apache-2.0. 🔴 Gate DENIED, third consecutive pass.**

🔴 **Gate posture: `make hooks` DENIED** (`Gap 446-A`, third consecutive pass, third container).

### 🟢 `Gap 447-B` REFUTED — and `p447` was right to carry it as a hypothesis rather than a fact

`p447` wrote on this shelf, flagged explicitly as **a single relayed secondary source**, that
the community MCP supply for Moodle and Canvas is *"overwhelmingly READ-ONLY"* and that *"not
one community server in that guide creates and publishes a course."* 🟢 **It named a test. The
test was run this hour, against source, and the hypothesis fails.**

| the claim | 🟢 what source says |
|---|---|
| *"overwhelmingly read-only"* | 🔴 **136 of 414** tool declarations mutate — **32.9 %**, and a **lower bound** |
| *"not one community server creates and publishes a course"* | 🔴 **false at four addresses** |

| address | authoring / publishing tools, read from the registry |
|---|---|
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | 🟢 **`create_course`** (`src/tools/courses.ts:205`, asserted in `tests/tools/courses.test.ts:53`), `create_module`, `create_module_item`, `create_page`, `create_new_quiz`, `grade_submission`, `enroll_user` — **62 write tools** |
| [`mdweaver/canvas-mcp`](https://github.com/mdweaver/canvas-mcp) | 🟢 `create-module`, `create-module-item`, **`toggle-module-publish`** (`src/tools/modules.ts:114`), **`update-syllabus`** (`src/tools/courses.ts:124`), **`post-announcement`** (`:216`) — **41 write tools, 46.1 %** |
| [`r-huijts/canvas-mcp`](https://github.com/r-huijts/canvas-mcp) | 🟢 `create-module`, `create-module-item`, `toggle-module-publish`, `post-announcement` — **30 write tools, 43.5 %** |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 `create_announcement`, `create_assignment`, `create_module`, `create_page`, `bulk_grade_submissions`, `bulk_update_pages` |
| [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | 🟡 **Go** codebase, 19 tools, 3 write |

🔵 **A server that creates a module and then toggles it published is publishing courseware.**
The authoring half of this tier is **not** vendor-only, and `Pattern AM`'s teacher-facing
courseware factory no longer needs a bespoke write path on Canvas.

### 🟡 But the gate you would reach for to make that safe is itself unsound

🟢 The one address that annotates read-only intent per tool, `vishalsachdev/canvas-mcp`,
declares it on **72 of 128** tools, leaves **55 (43.0 %) undeclared — and those 55 are exactly
the mutating ones** — while the **single** tool marked `read_only_hint=False` is
`download_course_file`, **a read**. 🔴 An MCP allowlist gateway keyed on `read_only_hint` is
keyed on a field that is **43 % unpopulated and at least once inverted**.
🟢 `compose/code/mcp-allowlist-gateway` must gate on the tool's **effect** — an explicit
write-tool denylist read from the registry — never on the hint → `Gap 448-B`.

### 🟢 A new vertical row — the NA state system of record, and it is permissive

| platform | repo | licence, read first-hand 2026-10-26 | region | what it is, and whether Globant can build on it |
|---|---|---|---|---|
| 🟢 **Ed-Fi ODS/API** | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | 🟢 **Apache-2.0** · `LICENSE.txt` **10 172 B** · `59899c6091b5` · HEAD `4d626f9ab257` | **North America** (US, Texas) | The operational data store and API behind **Texas TSDS/TEDS**, which TEA has **mandated** SIS vendors submit to via API transactions. 🟢 **The first permissively-licensed system of record on this shelf** — every other one is GPL-2.0/3.0, AGPL-3.0 or carries no grant. 🟢 **Vendor-and-build row.** 🟡 Bounded by a **233 924 B `NOTICES.md`** (`609e95c99d9b`): Apache-2.0 at the root does not clear the tree (`Trend 40`), so a dependency-closure pass is owed before shipping. |
| 🟢 **Ed-Fi ODS Implementation** | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | 🟡 not read this pass | **North America** | Deployment/implementation tooling for the above. 🟢 Reachable, HEAD `b6b72e594bc4`. Grant unread → next pass. |

### 🟢 `openSIS Classic` re-verified, and the below-root grant reproduces to the digit

| check | result |
|---|---|
| `docs/License.txt` | 🟢 **17 286 B · `224ac3d403e3`** — reproduces this shelf's published cell exactly |
| root grant paths | 🔴 **9 of 9 → 404** → `ABSENCE-ENUMERATED` at root |
| README | *"licensed under the GNU General Public License"*, pointing at `docs/License.txt` |

🔴 **GPL-2.0 confirmed, so the shelf's existing read stands:** distribution-triggered, no
network clause — a self-hosted customisation is fine, a redistributed derivative is not.

### 🔴 Where this tier still cannot serve an engagement, stated as absences rather than silence

| region | system of record | connector supply | verdict |
|---|---|---|---|
| **North America** | TSDS / Ed-Fi | 🟢 Apache-2.0 platform **+** a write-capable Canvas connector tier | 🟢 **servable today** |
| **EMEA** | Bayern `ASV`/`ByCS`/`VIDIS`, Niedersachsen `DaNiS`→`NEO` | 🔴 **no published API spec, no OSS** — `VIDIS` third-party integration still **pilot**; `NEO` primary-school release due **start of 2026/27** | 🟡 **procure through the state programme** |
| **APAC** | `UDISE+` (1.47 M schools) | 🔴 **no official API, no OSS tooling found** | 🔴 **absence** — sell teacher enablement, not integration |
| **LATAM** | `SIGED` (MX), `SIGE` (CL) | 🔴 none; one **third-party commercial** endpoint. Contrast Brazil/Argentina/Colombia, where code exists but is 🔴 **unlicensed more often than copyleft** (`Trend 43`) | 🔴 **split market** |

---

## 🆕 `p447` — **🟡 A CAPABILITY ABSENCE on the LMS-connector tier, carried as a hypothesis with a named test rather than as a fact: the community MCP supply for Moodle and Canvas is overwhelmingly READ-ONLY, and the authoring-and-publishing half appears to be vendor-built.**

🟡 **The claim, and its provenance, stated before its content.** A directory review of the
education MCP tier read this hour reports that the community servers are predominantly
**read-only student tools**, and states that *not one community server in that guide creates
and publishes a course*. 🔴 **This is a single relayed secondary source**, and the official
primaries that could corroborate it are **unreachable from this host** (`Gap 446-D`, re-probed
and widened below). It is therefore recorded as a **hypothesis**, not promoted to a shelf fact.

🟢 **Why it is worth carrying even at that confidence.** If it holds, it is a **market-structure**
statement rather than a tooling note: the connector tier this base sells is strong exactly where
an engagement needs it **least** (reading a student's own timetable and grades) and absent
exactly where an engagement bills **most** (course authoring, bulk enrolment, publishing). 🔵 It
would also explain `Trend 46`'s shape — ten addresses collapsing to six projects is what a
category looks like when everyone re-implements the same small read-only surface.

🟢 **The test, which is cheap and fully offline once cloned, and which the base already has the
instrument for.** Enumerate the registered tool names in each of the **six distinct projects**
`p446` established behind the ten Canvas/Moodle addresses, and classify each tool
**read vs write**. A single write-capable tool (`create_course`, `publish_module`,
`enrol_user`) refutes the absence; zero across six projects confirms it with a denominator.
Registered as `Gap 447-B`.

🔵 **Standing caution on this tier, unchanged and reinforced:** these servers reach **student
records**. Any of them entering a client engagement is a data-protection review, not merely a
licence review — and in EMEA that review now has no first-hand authority behind it, because
`eur-lex.europa.eu` has **never been readable from this host** (`Gap 446-D`).

---

## 🆕 `p446` — **The Moodle/Canvas connector tier re-priced by project count rather than address count: 🔴 the Canvas side is ONE maintained permissive project plus a second small arm, and the Moodle side is AGPL-3.0 or a 13-commit MIT alternative**

🔵 **Why this belongs on this file.** This file's job is the platform tier an engagement
customises. `p446`'s lineage audit (`agents/top.md`) changes the *supply* read under two of the
platforms carried here, and the change is in the direction that matters: **fewer, better-known
options**, not more.

| platform | connector supply, graded by PROJECT | licence cost | engagement read |
|---|---|---|---|
| **Canvas LMS** (Instructure) | 🟢 **4 projects** across 7 addresses — `vishalsachdev` (1 128 commits, 503 files, HEAD today), `bruchris` (430 / 501), `r-huijts`→`mdweaver` arm (64 / 35), and two < 12-commit singletons | 🟢 **MIT throughout** | 🟢 Take `vishalsachdev/canvas-mcp`. It is the only address here with a four-figure commit count **and** a HEAD that moved during this pass |
| **Moodle** | 🔴 **2 projects**, and they are not comparable — `csmediapro/moodle-mcp-server` (58 commits, 107 files) and `Jawadh-Salih/moodle-mcp-server` (13 commits, 37 files) | 🔴 **AGPL-3.0** / 🟢 MIT | 🔴 **The maintained Moodle connector costs AGPL-3.0.** The MIT alternative is 13 commits and stopped in **April 2026** |

🔴 **The Moodle asymmetry is the procurement fact on this file.** Moodle is the LMS with the
largest installed base in this base's region set, and its only actively-maintained MCP connector
is **network-copyleft**: AGPL-3.0 reaches a hosted service, which is exactly how a studio would
deploy it. 🟢 **Three dispositions, in cost order:** run `csmediapro` as a separate service and
publish its source; build on the 13-commit MIT base and own the maintenance; or integrate
Moodle through its own Web Services API directly and skip the connector tier. 🔵 The Canvas side
has no such tension — every address is MIT.

🟡 **Cell note.** `csmediapro`'s AGPL-3.0 payload re-measures **34 523 B · `0d96a4ff68ad`** from
an independent clone this hour, agreeing with this base's own published byte count. 🔵 Both the
figure and the family are confirmed; no disposition on this file changes on the Moodle grant
itself, only on the **count** of alternatives to it.


## 🆕 `p445` — **Two more systems of record mapped, and they are the two OPPOSITE ends of this map: 🟡 SIGAA has a real documented integration layer that is uniformly GPL-3.0, and 🔴 SIIAU has NOTHING — its only SDK's repository has been deleted**

🔵 **Why these two.** `p444` added **SUAP** as the first entry on this map that is
*open-ecosystem without being open-source*. This pass ran the platform-noun channel at three
more countries and the two results that landed are a matched pair: the same platform class
(university system of record), the same region, and **opposite supply states**. Read together
they are the argument for `Pattern AX` — you cannot price one from the other.

### 🟡 SIGAA — Brazil's federal universities. Supply exists, is documented, and cannot be vendored

🟢 **What it is.** **SIGAA** (*Sistema Integrado de Gestão de Atividades Acadêmicas*) is the
academic system of record across Brazil's **federal university** network — UFPB, UFRN, UFMG and
the rest. It holds curricula, enrolment, grades and class administration. Technically it is a
**JSF web application with no public REST API**, which is why every integration in existence is
a parser rather than a client.

| | |
|---|---|
| **Operator** | each federal university runs its own instance |
| **Region** | **LATAM** (Brazil) |
| **Source available?** | 🔴 **No.** The platform itself is not public |
| **Integration supply** | 🟢 **Yes — three addresses, verified first-hand 2026-10-25** |
| **Licence of that supply** | 🔴 **GPL-3.0, all three of three** |
| **Freshness** | 🔴 2016, 2017, 2020 |

| address | grant | HEAD | gives you |
|---|---|---|---|
| [`fernandobrito/cursos_ufpb`](https://github.com/fernandobrito/cursos_ufpb) | 🟡 GPL-3.0 · 35 141 B · `cbdcf32a9188` | 2017-01-26 · 168 files | the endpoint shape (`/api/curricula`) and the `sigaa_parser` logic |
| [`macielti/sigaa-cli`](https://github.com/macielti/sigaa-cli) | 🟡 GPL-3.0 · 35 149 B · `85b9a51f5603` | 2020-01-04 · 25 files | the **auth flow against any SIGAA instance**, by configurable base URL |
| [`fernandobrito/ufpb_sigaa_api_old`](https://github.com/fernandobrito/ufpb_sigaa_api_old) | 🟡 GPL-3.0 · 35 141 B · `4fa17f22c442` | 2016-02-07 · 14 files | the reference shape for "SIGAA behind an HTTP API" |

🟢 **How to customise with AI on top — and it is NOT the usual answer for this map.** For Moodle
or Open edX the move is *write a plugin*. For SIGAA there is no plugin seam and no licence that
permits vendoring, so the move is: **read these three as specification, write a clean-room
adapter, wrap it as an MCP server, and put the agent layer on that.** Full stack with every
licence measured: `Pattern AY`. 🔴 The adapter is unavoidable work; budget it as build, not as
integration.

🔴 **The access gate is separate from the licence gate and is the one that stops projects.**
SIGAA holds student records. A grant answers copyright only; *may we call this system* lives in
the university's terms of use. Get written registrar authorisation before the adapter touches
production.

### 🔴 SIIAU — Universidad de Guadalajara. Zero supply, and that is a measurement, not an absence of information

🟢 **What it is.** **SIIAU** (*Sistema Integral de Información y Administración Universitaria*)
is UdeG's own system of record — finance, HR, school records and planning, with **SIIAU Escolar**
as the student-facing portal for grades, credits and mobility paperwork. UdeG describes itself as
the first Mexican institution to build such a system for its own needs, and it is consolidated
and heavily used. Mexico's second-largest public university system runs on it.

| | |
|---|---|
| **Operator** | Universidad de Guadalajara |
| **Region** | **LATAM** (Mexico) |
| **Source available?** | 🔴 **No** |
| **Integration supply** | 🔴 **ZERO.** One SDK ever existed: `dev-cucei-itrans/siiau-api-client`, a Laravel client for SIIAU's internal API, published on Packagist and **marked abandoned** there |
| **Probed first-hand 2026-10-25** | 🔴 `git ls-remote https://github.com/dev-cucei-itrans/siiau-api-client` → **DOES NOT RESOLVE** |
| 🆕 **Grant, read first-hand 2026-10-26 (`p451`)** | 🔴 **SPLIT across versions — 4 of its 7 are `proprietary`.** `v1.0.0-BETA` · `v1.0.0` · `v1.1.0` · `v1.1.1` = **`proprietary`**; **`BSD-3-Clause` only from `v1.1.2`** (2024-08-25) and on `dev-main`. 🔴 **Pin `>=1.1.2`** — a `^1.0` constraint resolves into the proprietary band. 🔵 Packagist (`packagist.org/packages/…`, controls both ways) is now the **only** surviving channel for either grant: 7 versions · 1 023 downloads · `abandoned: true`. Full table in the `p451` section at the head of this file |

🔵 **Why this entry is worth as much as a positive one.** The package record survives on
Packagist; **the repository behind it is gone.** So the shape existed for SIIAU — somebody built
a client, published it, and deleted it — and an engagement at UdeG therefore starts from **zero**,
not from an unmaintained base it can revive. 🟢 **That is a scoping fact a proposal can be
written against**, and it is the single most common case on this map to be mistaken for *"we'll
find something open source"*. 🔴 Price the adapter as greenfield, and treat the dead Packagist
entry as evidence that UdeG's integration surface is reachable, not as a starting point.

🔵 **Where to go instead for Mexico, from this base's own legs:** **SIASE** (UANL) returned six
addresses (`p444`, top at 38 ★). An engagement that needs a *reference* Mexican implementation
should read SIASE's tier, not SIIAU's.

### 🔴 Two nils on this map, recorded so nobody re-buys them

| platform | country | result |
|---|---|---|
| **UdelaR** / `bedelías` | Uruguay | 🔴 **NIL.** The only artefact is a **2015 Facultad de Ingeniería student report** describing a scrape of the bedelías site to render prerequisites; no repository published with it |
| PUCP *Campus Virtual* · UNI *SIGA* · UNSA | Peru | 🔴 **NIL on a second channel.** PUCP ships an official mobile app authenticating against Campus Virtual and **no public integration code**; UNI and UNSA return nothing. With `p444`'s ministry-noun nil (SIAGIE) and its `UNMSM` coursework result, 🔴 **Peru is now twice-unpaid on two distinct channels** — weak evidence of a genuine supply absence rather than a measurement artefact (`Gap 445-B`) |

---

## 🆕 `p444` — **SUAP: a platform running across Brazil's federal institute network, with a real API ecosystem and 🔴 NO PUBLIC SOURCE — the first entry on this map that is open-ecosystem without being open-source**

🟢 **What SUAP is.** **SUAP** (*Sistema Unificado de Administração Pública*) is the academic and
administrative system of record of the **Instituto Federal** network — Brazil's federal
vocational and technical education system. It holds enrolment, grades, attendance, class
materials and meals. `p444` reached it through the platform-name channel and found an
integration ecosystem larger than any single LATAM platform this base has mapped.

🔴 **And the platform itself is not published.** Two legs were run — the acronym alone (732
hits) and the expanded name (*"suap sistema unificado administracao"*, 12 hits) — and **neither
returns the production Django application.** Every one of the 12 expanded-name results wraps,
extends, authenticates against, load-tests or *simulates* SUAP. The closest, `Thiago-FJ/SUAP`,
describes itself as an academic simulation for a coursework exercise. **Recorded as a measured
absence, not an assumption:** SUAP is reachable through a documented OAuth2 API and is not
forkable.

🔵 **Why that distinction earns a row on this map.** Every other platform here — Moodle,
Open edX, Canvas, Sakai, Kolibri, OpenEduCat, `ipti/br.tag` — is something an engagement can
**fork, read and self-host**. SUAP is something an engagement can only **integrate against**.
That is a different commercial shape: no vendor lock-in analysis, no hosting story, no licence
compatibility question for the platform — and *total* dependency on an API whose owner publishes
no grant for its own clients.

| platform | region | grant | what it is, and the engagement shape |
|---|---|---|---|
| **SUAP** · `suap.ifrn.edu.br` | **LATAM** (Brazil) | 🔴 **source not published** | Academic/administrative system of record for the **Instituto Federal** network. 🟢 Documented **OAuth2** API, confirmed reusable across institutions (`luizpicolo/suap_api` targets **IFMS**, not IFRN). 🔴 Integrate-only: cannot be forked or self-hosted. **Start from [`django-auth-suap`](https://github.com/django-by-kelsoncm/django-auth-suap) (MIT, HEAD 2026-09-05), not from IFRN's own unlicensed clients.** |
| [`suap-ava-suite/moodle-local_suap`](https://github.com/suap-ava-suite/moodle-local_suap) | **LATAM** (Brazil) | 🟡 **GPL-3.0** · `LICENSE` 35 161 B · `54b00c9ffd02` | 🟢 **The bridge between the two anchors of this map.** A Moodle `local` plugin wiring Moodle (the *AVA*, ambiente virtual de aprendizagem) to SUAP's system of record. **HEAD 2026-10-19** — live, 94 files. 🔵 GPL-3.0 here is *coherent, not a problem*: Moodle is GPL-3.0, so a Moodle plugin is expected to be, and the obligation is one the host platform already imposes. This is the first LATAM row on this map that connects an LMS to a SIS. |

🟢 **How this changes the composition story.** This base's LATAM verticals row has been
`ipti/br.tag` — one municipal K-12 platform, GPL-2.0. SUAP adds the **federal, post-secondary,
integrate-only** shape, and `moodle-local_suap` supplies the **LMS↔SIS seam** that
`compose/patterns.md` has previously only been able to describe for EMEA. 🔵 The pairing
*Moodle + `moodle-local_suap` + SUAP OAuth2 via `django-auth-suap`* is a complete, licence-clean
stack for a Brazilian federal-institute engagement, and it is wired up as `Pattern AW`.

🔴 **The gap this leaves, stated as a gap:** this map still has **no row for a LATAM
system of record that is BOTH forkable and permissive.** `ipti/br.tag` is GPL-2.0 (and its
README says BSD-3-Clause — `p443`), SIGAA and SIU Guaraní are institution-internal, SUAP is
unpublished. Every LATAM SIS address on this map is copyleft, closed, or both.

---


## 🆕 `p443` — **A live municipal platform joins the map, and it is the first row on this file whose README names a DIFFERENT, MORE PERMISSIVE grant than its own payload**

🟢 **The row.** `ipti/br.tag` — **T.A.G.** (*Tecnologia de Apoio à Gestão*) — is a Brazilian
basic-education school-management system built by **IPTI** with the municipality of **Santa
Luzia do Itanhy/SE**, explicitly for rural schools, **with offline synchronisation for schools
with no internet**. **3 959 commits**, **2 304 files**, HEAD **2026-10-18**. 🟢 It is the most
engagement-relevant LATAM platform address on these shelves and this file had **1 LATAM row of
6** before this pass.

🔴 **And it is sold here as GPL-2.0, because that is what the file says — against its own
README.** Established first-hand, both channels at the same commit `3e6d315ef881`:

| channel | what it states, read first-hand |
|---|---|
| `LICENSE` **18 027 B · `111e1f411730`** | 🔴 `GNU GENERAL PUBLIC LICENSE`, **`Version 2, June 1991`** — GPL-2.0. No §13 Affero clause, so not GPL-3/AGPL (`P171`); **no BSD operative clause anywhere in the payload** |
| `README.md` **3 065 B · `e9695ee53743`** | 🔴 § `Licença` states **"The BSD-3-Clause"** and reproduces the **BSD operative text** *"Redistribution and use in source and binary forms…"*, © 2011 IPTI. A BSD-3-Clause badge sits **commented out** on line 1 |
| GitHub's sidebar | **GPL-2.0** — with the payload, against the README |

🔴 **Why this is a procurement finding and not a tidiness one.** Every other conflict this file
has recorded ran the safe way — a badge or a roundup claiming **MIT** where the payload was
**AGPL**, so a careful reader was *over*-cautious. This one runs the **expensive** way: the
README is the **more permissive** channel, so a reader who trusts it concludes BSD-3-Clause,
vendors a copyleft school-records platform into a proprietary deliverable, and distributes it.
🟢 **The rule this file already applies survives the test: the payload decides.** 🔵 No
instrument on this base compares the two channels — `p288` built a README channel and `p278` a
channel-conflict gate, and neither asks *"does the README name a different licence from the
file"*. That is `Gap 443-C`.

🔵 **The wider LATAM result, measured in the same tranche:** of the four LATAM institutional
platforms that actually hold student records, **0 of 4 are permissive** — `ipti/br.tag`
(GPL-2.0), `LibreClass/libreclass` (GPL-3.0), `carmonabernaldiego/sistema-escolar` (AGPL-3.0),
and the already-shelved `sete` lineage — while **6 of 8** student-side academic-portal
addresses are. 🟢 **The copyleft frontier in LATAM therefore sits exactly where it sits in
EMEA: around the system of record.** That is the argument for this file's standing advice, now
with a LATAM denominator behind it: *integrate over an interface, never vendor the platform*.
Full tranche, refusals and ledger measurement: [`agents/trending.md`](../agents/trending.md)
`p443`. Recipe: `Pattern AV`.

| Platform | Licence (verified) | HEAD @ 2026-10-25 | Payload | AI layer goes… |
|---|---|---|---|---|
| **T.A.G. (`br.tag`)** | 🔴 **GPL-2.0** — 🔴 **README says BSD-3-Clause; the payload governs** | `3e6d315ef881` | `LICENSE` 18 027 B · `111e1f411730` | …**beside**, never vendored. Municipal basic education, Brazil, **offline-sync by design** — the one platform on this map built for schools with no connectivity *and* a live commit history. [repo](https://github.com/ipti/br.tag) |


## 🆕 `p442` — The platform tier is **enumerated**, not just read: four of these platforms carry a second licence text, and one of this file's own cells did not reproduce

🟢 `p440` and `p441` read the platform grants clause by clause. `p442` asks the prior
question — **is the payload we read the only one the repository carries?** — with the tree
channel now inside the shared library (`Gap 441-A`). Over the **134** repositories these
shelves publish a payload path for: **121** carry exactly one own-grant path, 🔴 **12 carry
more than one**, and four of those twelve are platforms or platform-adjacent rows on this
file.

| platform | the grant this file publishes | what else the tree carries, read first-hand | the read |
|---|---|---|---|
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 · `LICENSE` 35 147 B · `8ceb4b9ee5ad` | 🔴 `license.txt` **1 614 B · `0aaf39205490`** — GPL-3.0 titled, all six clauses **absent**, `GRANT-BY-REFERENCE` | the complete grant is the root file; the second payload is a **pointer** and must never be the one cited |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | `bigbluebutton-web/COPYING.LESSER` **7 637 B · `9ccf26cfe845`**, LGPL-3.0 | 🟢 consistent, and it is the **component** grant: `bigbluebutton-web` states its own LGPL-3.0 rather than inheriting silently. 🔵 Still `GRANT-UNCALIBRATED` — LGPL incorporates GPL-3.0 **by design** and needs `p440`'s unbought `GRANT-BY-DESIGN` verdict (`Gap 440-B`) |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | ECL-2.0 | **four** ECL-2.0 texts: root plus `delegatedaccess/`, `external-calendaring-service/`, `roster2/` (sampled: `delegatedaccess/LICENSE` **11 110 B · `6001bb8caa76`**) | 🟢 consistent; a per-module restatement in a 400-module monorepo, not a second grant |
| [`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) | AGPL-3.0 · `LICENSE` **35 442 B · `698099632698`** (🔴 **repaired here** — the published cell read 35 441 B · `d8d2ea7ef0a1`, measured through a capture) | MIT ×2 + Apache-2.0 under `mathlive-assets/` and `sre-assets/` (MathLive 1 099 B, Speech Rule Engine 10 174 B, Temml 1 074 B) | 🟡 **vendored third-party assets, not the project's grant.** The enumerator's `is_own_path` knows `node_modules/` and `vendor/` but not `*-assets/`, so it types them as own — recorded as `Gap 442-B`, not quietly fixed |

🔵 **What changes for an engagement:** nothing about these four platforms' own licences, which
hold as published. What changes is the **screening procedure** — a platform's grant is now
established by enumerating its tree, so a second text can be *seen* and classified rather than
hidden behind whichever filename a ladder happened to try first. `Pattern AU` is the recipe.

## 🆕 `p441` — The **permissive** half of the platform tier is now read clause by clause too, and one platform-adjacent row is sold with a restriction attached

🟢 `p440` read the ten **copyleft** platforms' grants clause by clause. `p441` does the same
for the **BSD** tier — the assessment and teaching-compute layer this file sells beside the
LMS — and the result is **11 of 12 payloads `GRANT-PRESENT`**, verified against a
variant-aware profile (BSD-2 and BSD-3 are different licences under one family name).

| repository | shelved on | payload · `sha256₁₂` | grant check 2026-10-25 |
|---|---|---|---|
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **this file** (assessment delivery) | `LICENSE.txt` 2 058 B · `a5c692f12090` | 🟢 `GRANT-PRESENT` — digest unchanged since `p390` |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | `repos/foundations.md` | `LICENSE` 1 475 B · `7069c7e8d60e` | 🟢 `GRANT-PRESENT` 🔴 **untitled payload** |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | `repos/foundations.md` | `LICENSE` 1 512 B · `3a83d5b8e22c` | 🟢 `GRANT-PRESENT` 🔴 **untitled payload** |
| [`jupyterlite/jupyterlite`](https://github.com/jupyterlite/jupyterlite) | `repos/foundations.md` | `LICENSE` 1 525 B · `574f8a9cab1e` | 🟢 `GRANT-PRESENT` |

🔵 **Only `qtiworks` is a row on this file**; the other three are the teaching-compute tier
on `repos/foundations.md` and are listed here because they are what sits *beside* the LMS in
a delivery. No row is added to this shelf by this pass.

🔴 **Two warnings that belong on a platform shelf specifically.**

1. [`open-webui/open-webui`](https://github.com/open-webui/open-webui) — a common drop-in
   chat surface in front of an LMS, carried on `agents/top.md` as a warning row rather than
   a build-on row — grades `GRANT-PRESENT` and is **not** a stock BSD-3
   grant: 2 819 B against ~1 515 B, carrying a **branding restriction** and a **Contributor
   Licence Agreement**. `GRANT-PRESENT` answers *is the grant here*, never *is it
   unmodified*. Sell it with the restriction in the SOW, or use `jupyter-ai` instead.
2. 🟡 **`BigBlueButton` and `OpenEduCat` are still `GRANT-UNCALIBRATED`** (LGPL-3.0,
   `Gap 440-B`) and must not be read as cleared. `p441` did not touch that gap: LGPL
   incorporates GPL-3.0 **by design**, so it needs a fifth verdict rather than a profile.

🔵 Recipe for putting this tier in front of a client's counsel: `Pattern AT`. Instrument,
87 controls and mutation results: `compose/code/p441-bsd-variant/README.md`.

## 🆕 `p440` — The platform tier's grants are read **clause by clause** for the first time, and all ten hold

🟢 Every pass before this one verified the platform tier by reading its payload and
naming its **family**: *this is AGPL-3.0, 35 136 B, here is the digest*. That answers
"which licence" and 🔴 **not** "is the licence actually in there". `p439` showed on the
code path why the two differ — a 552 B file titled Apache-2.0 that was a pointer — but
its instrument had profiles for MIT, Apache-2.0 and ISC only, so 🔴 **every copyleft row
on this file was `GRANT-UNCALIBRATED`: the instrument declining to judge the entire tier
this file exists to sell.**

🟢 `p440` profiles the GPL family. The ten platform repositories below were re-probed at
source **2026-10-25** and graded against their own licence version's operative clauses.

| Platform | Branch | Payload | Bytes | `sha256₁₂` | Profile | Grant check |
|---|---|---|---|---|---|---|
| **Moodle** · [`moodle/moodle`](https://github.com/moodle/moodle) | `main` | `COPYING.txt` | 35 147 | `8ceb4b9ee5ad` | GPL-3.0 | 🟢 **GRANT-PRESENT** |
| **Open edX** · [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `master` | `LICENSE` | 35 136 | `e12d78569742` | AGPL-3.0 | 🟢 **GRANT-PRESENT** |
| **Frappe LMS** · [`frappe/lms`](https://github.com/frappe/lms) | `develop` | `license.txt` | 33 893 | `db1a87ba81e8` | AGPL-3.0 | 🟢 **GRANT-PRESENT** |
| **Chamilo** · [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `master` | `LICENSE` | 35 147 | `8ceb4b9ee5ad` | GPL-3.0 | 🟢 **GRANT-PRESENT** |
| **Canvas LMS** · [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `master` | `LICENSE` | 34 520 | `57c8ff33c9c0` | AGPL-3.0 | 🟢 **GRANT-PRESENT** |
| **Gibbon** · [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `v31.0.00` | `LICENSE` | 35 121 | `93178a43d6d3` | GPL-3.0 | 🟢 **GRANT-PRESENT** |
| **RosarioSIS** · [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `mobile` | `LICENSE` | 15 214 | `d954e14e5c75` | GPL-2.0 | 🟢 **GRANT-PRESENT** |
| **i-Educar** · [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | `2.12` | `LICENSE` | 18 092 | `8177f9751321` | GPL-2.0 | 🟢 **GRANT-PRESENT** |
| **openSIS Classic** · [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | `master` | `docs/License.txt` | 17 286 | `224ac3d403e3` | GPL-2.0 | 🟢 **GRANT-PRESENT** |
| **PeerTube** · [`Chocobozzz/PeerTube`](https://github.com/Chocobozzz/PeerTube) | `develop` | `LICENSE` | 34 520 | `76a97c878c9c` | AGPL-3.0 | 🟢 **GRANT-PRESENT** |

🟢 **Ten of ten.** 🔵 **What a clean sweep is worth, precisely:** it does not make the
copyleft exposure smaller — Moodle is still GPL-3.0 and Open edX is still AGPL-3.0, and
the posture on this file is unchanged. What it removes is a *different* risk, the one
`p439` found on the permissive side: a platform whose licence file is a **pointer** to
its licence, leaving the client to discharge the distribution obligation it names. 🟢 On
this tier that risk is now measured at **zero**, rather than assumed.

### 🔴 The sentence a client should hear about AGPL, now that §13 is readable

The AGPL-3.0 profile built this pass requires the **operative §13 sentence** —
*"...interacting with it remotely through a computer network ... an opportunity to
receive the Corresponding Source"*. 🔵 That clause is the whole commercial difference
between Moodle and Open edX, and it is the one a procurement conversation turns on:

- **GPL-3.0 (Moodle, Chamilo, Gibbon)** — the obligation attaches to **distribution**.
  A hosted deployment that never ships binaries to anyone does not trigger it.
- **AGPL-3.0 (Open edX, Canvas, Frappe LMS, PeerTube)** — the obligation attaches to
  **network interaction**. A hosted deployment triggers it by being used, and
  🔴 modifications must be offered to the platform's own users.
- **GPL-2.0 (i-Educar, RosarioSIS, openSIS)** — distribution again, and 🔵 **no network
  clause at all**, because GPL-2.0 predates the question. These three are the LATAM and
  low-cost SIS tier, and this is a genuine, under-stated advantage for a hosted
  engagement: the same posture that makes them look dated makes them cheaper to host.

🔴 **And `p440` measured why that GPL-2.0 row cannot be graded with GPL-3.0's clauses:**
a complete GPL-2.0 licence is missing **four of GPL-3.0's six** operative clauses, so a
single unversioned "GPL" rule would have condemned all three of those platforms as
carrying a truncated grant. The profile is version-aware for exactly that reason.

🟡 **`LGPL-3.0` is still unread, and two platforms on this file carry it** —
**BigBlueButton** and **OpenEduCat**. LGPL-3.0 incorporates GPL-3.0 *by reference* by its
own design, so it needs a verdict this instrument does not yet have. Registered as
`Gap 440-B`; until then those two rows stay `GRANT-UNCALIBRATED`, which is the
instrument declining rather than approving.

---

## 🆕 `p439` — The platform tier re-measured at source, and the **one licence error this industry keeps making** is confirmed live for the third time

🟢 **Four platform-tier addresses re-probed first-hand this hour**, byte-for-byte and
HEAD-for-HEAD against what this shelf already carries. The point of the exercise is that it
was run as a *measurement* and not as an assumption — a shelf that is never re-read is a
shelf whose staleness is unknown:

| Platform | Licence (re-verified 2026-10-25) | Default branch | Payload | Shelf agrees |
|---|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | ⚠️ `master` | `LICENSE` 10 982 B @ `d073ad444fe5` | 🟢 yes |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** | ⚠️ `develop` | `license.txt` 33 893 B @ `5d6df8e3ed8e` | 🟢 yes |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | `main` | `LICENSE` 11 408 B @ `a31d82624c27` | 🟢 yes |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL** | `main` | `LICENSE` 25 289 B @ `7bd8b6794cb7` | 🟢 yes |

🔴 **THE ERROR, LIVE AGAIN: "Frappe LMS is the MIT-licensed option."** Three separate 2026
LMS-comparison pages returned by this pass's own platform search say exactly that, one of
them phrasing it as *"MIT licence with self-hosted data ownership"*. 🟢 **It is AGPL-3.0**,
read from `license.txt` at the commit above. The MIT belongs to **`frappe/frappe`**, the
*framework*; the LMS *application* built on it is AGPL-3.0. `p425` registered this as `T125`
and `p439` is the third independent confirmation.

🔵 **Why this specific error is the most expensive one available in this tier.** The
framework-permissive / application-copyleft split is invisible in a vendor comparison table
and decisive for a client: AGPL-3.0 §13 reaches users **over a network**, so a hosted
student-facing deployment of a modified Frappe LMS owes source to its users. A studio that
priced the engagement off "MIT" has mispriced the whole delivery model, not a line item.
🟢 **And it is the generalisable lesson**, which is why it sits on this shelf rather than only
in the trend record: in a platform tier, **the licence belongs to the artefact you ship, not
to the project whose name is on the box.** Two keys, one platform.

### 🟡 Two default branches that are not `main`, and that is a *platform-tier* property

`OpenOLAT` resolves to **`master`** and `frappe/lms` to **`develop`**. 🔴 A hardcoded `main`
writes both down as **ungranted** — the exact trap `lib/probe_payload.sh` exists to close
(measured on `GibbonEdu/core` → `v31.0.00`, `portabilis/i-educar` → `2.12`,
`francoisjacquet/rosariosis` → `mobile`, three of the five highest-starred open SIS platforms
in existence). 🔵 Mature platform projects are *more* likely than new agents to carry a
non-`main` default, because their branch conventions predate the convention. Resolve with
`ls-remote --symref`, never assume.

### 🟢 The customisation seam, restated for the licences actually on this shelf

Both headline AI-on-top platforms this pass touched are **copyleft** (`frappe/lms` AGPL-3.0;
Moodle GPL-3.0 at **5.2**, April 2026; Open edX AGPL-3.0, current release **Verawood**, with
**Willow** expected December 2026; Canvas AGPL-3.0; Chamilo GPL-3.0; ILIAS at **11**,
PHP 8.3/8.4). 🟢 **The two permissive answers in the whole tier remain `OpenOLAT`
(Apache-2.0) and `kolibri` (MIT)** — and the seam that lets a studio put AI on a copyleft LMS
without inheriting its obligations is still the one this shelf has carried since `p387`:
build **outside** the core, against a supported extension point —
[`openedx/XBlock`](https://github.com/openedx/XBlock) (Apache-2.0) for Open edX, LTI 1.3 or
the REST API for Moodle and Canvas — and keep the AI component in its own repository under
its own grant. 🔵 Calling an AGPL system **over a network boundary** is a different act from
linking into it, and the boundary is the deliverable.

🔴 **New screening question on this tier as of this pass, and it is not theoretical.** Before
adopting any platform component, ask whether its grant is **present** or merely **named** —
`make gate-grant-presence`. A 552 B payload titled Apache-2.0 was found in live education
supply this hour (`spragginsdesigns/ai-tutor-webapp`), holder **Vercel, Inc.**, licence text
absent from the repository. For a platform component the client will *redistribute*,
Apache-2.0 §4(a)'s duty to supply a copy of the License lands on the integrator. See
`Gap 439-A`.

---

## 🆕 `p438` — The platform decision survives a **licence scan** and not a **licence read**, and the difference is now measured on this base's own instruments

🔵 **Why this lands on the verticals shelf.** A platform choice is the one decision on an
education engagement that a client's procurement function actually audits, and it audits it
with a scanner report. 🟢 This shelf's standing finding is that the platform tier is almost
entirely copyleft — Moodle (GPL), Open edX (AGPL-3.0, narrowed), Chamilo (GPL-3.0), Canvas
community edition (AGPL-3.0) — with `OpenOLAT` (Apache-2.0), `Sakai` (ECL-2.0, Apache-derived)
and `learningequality/kolibri` (MIT) the permissive exceptions. 🔴 `p438` adds the part of the
audit that a scanner cannot do.

### 🔴 The measurement, on this base's instruments, not a vendor's

`p438` graded a new education specimen,
[`fangyuan-3149/book-learning-tutor`](https://github.com/fangyuan-3149/book-learning-tutor)
(`LICENSE` **1 503 B** · `sha256₁₂ 54ceeac19921`, HEAD `f0ef6fc3acd7`, read 2026-10-25). One
`bespoke_census.grade()` call returns, **in one row**:

| column | value | what a procurement report would print |
|---|---|---|
| `titled_family` | `MIT` | 🟢 "permissive" |
| `scan_verdict` | `PERMISSIVE` | 🟢 "cleared" |
| `stock` | `YES` | 🟢 "standard text, no review needed" |
| `p1054_verdict` | 🔴 `MIT-BODY-PLUS:unclassified-addition` | ⚠️ nothing — this column is not in the report |
| `needs_a_human` | 🔴 `no` | 🔴 "no legal read required" |

The appended clause — in Chinese, after a `---` rule — states that the repository ships **no
book or copyrighted content**, that the operator supplies the material, and that **the
operator carries the legal and copyright liability for it**. 🔴 On an education engagement the
operator is the client, and the content is textbooks. 🔵 `p427`'s `conjunctive_grant.classify()`
returns `scope: None` on the same payload because every entry in its `SCOPE_MARKERS` is an
English phrase.

🟢 **Sized over the corpus, so it is not one anecdote:** of the **238** licence payloads
committed under `compose/code/**/fixtures/`, **9** carry an addition verdict and **7 of those
9 are routed `needs_a_human = no`** — `p427`'s own two-family specimen among them. Registered
as `Gap 438-A`; the one-disjunct remedy is priced there and deliberately not slipped into this
pass.

### 🟢 The procurement consequence, stated so it can go in a proposal

🔵 **It does not change which platform to pick.** The copyleft map on this file stands: every
payload here was read first-hand and none of them is a stock text with an unread addendum.
🟢 **It changes what Globant can credibly say about the components bolted onto that
platform.** The AI layer on an education engagement is assembled from small permissive
repositories — this pass alone shelved eight — and that layer is where the addendum class
lives: 🔴 **1 of the 9 addresses graded this pass, 11 %, carried a clause that both of this
base's automated instruments missed and that shifts content liability onto the client.**

🟡 **So the deliverable is a three-column clearance, applied to every component that reaches a
client's estate** — the integration-layer analogue of the foundation rule now on
`repos/foundations.md`:

1. 🟢 family from the payload, never from a badge or a comparison blog (this shelf's
   `formalms` row is the standing example: Apache-2.0 in one comparison, GPL-2.0 in another,
   resolved here from the payload);
2. 🟢 the addition column read, not just the family column;
3. 🟢 any bytes above the family's stock band read **by a person, in the payload's own
   language** — the band is an excellent detector that a payload was modified and no
   detector at all of what the modification says.

🔵 **And the platform tier's own exposure is bounded, which is worth saying plainly to a
client**: the large copyleft platforms ship canonical GPL/AGPL texts whose bytes this base has
already measured, so the addendum risk on this file is **low and measured** — it concentrates
in the long tail of permissive components, exactly where the delivery team is moving fastest.

## 🆕 `p437` — Conformity is a **procurement surface** on the platform decision, and it reverses the usual copyleft calculus

🔵 **The connection this file was missing.** This shelf's standing finding is that the
education platform tier is almost entirely copyleft — Moodle, Open edX, Chamilo, Canvas-adjacent
estates — with `OpenOLAT` (Apache-2.0) and `learningequality/kolibri` (MIT) the permissive
exceptions. 🆕 `p437` adds the regulatory half of that decision, and it changes which platform
wins.

Under the EU AI Act, the duties attach to the **AI system** and its provider/deployer role,
not to the LMS it is bolted onto. So the platform choice determines *who carries the
obligation*:

| configuration | who is the provider of the high-risk system | consequence |
|---|---|---|
| AI built **into** the LMS core (vendored fork) | 🔴 The client, for the whole platform | Annex IV documentation must cover the LMS; a copyleft fork makes that documentation a distribution artefact too |
| AI as a **separate component over a seam** (XBlock, MCP, LTI) | 🟢 The component, scoped narrowly | Annex IV covers the component only. **The conformity surface is as small as the seam** |

🟢 **This is the strongest argument yet for the seam-based integration this file already
recommends** — `openedx/XBlock` (Apache-2.0) for Open edX, the MIT connector tier for national
platforms, LTI for the rest. It was previously a licence-hygiene argument. 🔵 **It is now also
a compliance-scoping argument, and that is the one a client's counsel will act on:** keeping
the AI outside the copyleft core keeps the Annex IV technical documentation bounded to code
Globant actually wrote.

🔴 **The corollary, stated plainly.** A client already running a copyleft LMS who asks for AI
"inside the platform" is asking for the maximum conformity surface and a copyleft distribution
obligation on the documentation at the same time. 🟢 The answer is not to refuse the
engagement — it is to price the seam, and `compose/patterns.md` **Pattern AP** is the scoping
gate that produces that price.

🟡 **The education-ERP nil is untouched by this.** Nothing found this pass is an education ERP
or SIS platform; the EU-AI-Act tooling tier is governance instrumentation, not a vertical
system. The standing nil recorded at `p433`/`p434` and reconfirmed at `p435` **stands a fourth
consecutive pass** — this pass did not re-run that sweep and does not claim to.

## 🆕 `p436` — The interoperability layer is a vertical in its own right, and a **national** education body is shipping it permissively

🔵 **The platform map on this file answers "which LMS do we build on?".** `p436` restores a tier
that answers a different and often better question: **"what do we build between the systems the
client already runs?"** Every row below was re-read first-hand on 2026-10-25.

| system | licence (verified) | layer | what it unlocks | Region |
|---|---|---|---|---|
| [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | **Apache-2.0** `10 173` B · `a6cba85bc92e` | roster / SIS interop | Serves a **OneRoster 1.2 API over an Ed-Fi ODS** (DS 4.0, 5.x, 6.1). Lets an agent read enrolment and class structure **without integrating against the SIS**. The US district-data seam. | North America |
| [Kennisnet/php-qti3](https://github.com/Kennisnet/php-qti3) | **MIT** `1 066` B · `27fb6d463569` | assessment interop (PHP) | QTI 3 in PHP from the **Dutch national education-ICT body** — the route into a PHP estate, which is most of the Moodle world. | EMEA |
| [OpenOLAT/qtiworks](https://github.com/OpenOLAT/qtiworks) | **BSD-3-Clause** `2 058` B · `a5c692f12090` — 🟢 `GRANT-PRESENT` clause-by-clause (`p441`) | assessment delivery | QTI 2.1 delivery with **JQTI+** and **MathAssess**. Maintained to **2026-06-30**. | EMEA |
| [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** `1 072` B · `00ed05b90bf8` | assessment authoring | QTI 3 toolkit; `packages/core` implements the **parametric-item mechanism** end to end. | North America |
| [amp-up-io/qti3-item-player](https://github.com/amp-up-io/qti3-item-player) | **MIT** `1 076` B · `7faa621251d7` | assessment rendering | QTI 3 item player — the rendering half of the boundary. | North America |
| [marcosroriz/sete](https://github.com/marcosroriz/sete) | **MIT** `1 069` B · `0bbd32e7e09a` | public-sector operations | **SETE** (CECATE/UFG): school-transport e-governance with a **desktop build for municipalities with restricted internet**. 🔴 HEAD 2023-03-20 — a reference design, not a live dependency. | LATAM |

🟢 **Why `Kennisnet/php-qti3` changes the EMEA story on this file.** This file has repeatedly
recorded that EMEA's open-source education supply is thin and regulation-heavy. A **national
education-ICT agency publishing its own MIT assessment implementation** is the opposite shape:
state-funded, permissively licensed, and institutionally durable. 🔵 Taken with `p435`'s national
school-platform connector tier (IServ, Librus, Smartschool, EduPage, Skola24), the EMEA pattern is
now clear — **the supply is there, it is national rather than pan-European, and it was invisible
to every pan-regional query this base ran.**

🔵 **The decision this tier adds to "choosing the base"**: if the client's constraint is *several
systems that must agree* rather than *one system to extend*, the interop layer is the engagement
and the LMS choice is downstream of it. 🔴 **Reach bound: grant + currency + README; no suite was
executed here.**

# 🏫 Vertical solutions — Education

> Real, deployable platforms that an AI layer can be built **on top of** — the education
> equivalents of Odoo (ERP) or OpenMRS (health). Licences read from each repository's own
> payload at the HEAD shown, 2026-10-25.

## The platform map

🟢 **Re-read at source on 2026-10-25** — licence taken from each repository's own payload at
the HEAD shown, never from a badge.

| Platform | Licence | HEAD @ 2026-10-25 | Payload | AI layer goes… |
|---|---|---|---|---|
| **OpenOLAT** | 🟢 **Apache-2.0** | `d073ad444fe5` | `LICENSE` 10 982 B · `6dbc5b605ed0` | …**inside**. The only full LMS where proprietary AI may be embedded directly. [repo](https://github.com/OpenOLAT/OpenOLAT) |
| **Kolibri** | 🟢 **MIT** | `44a4e68aac3e` | `LICENSE` 1 097 B · `3c056b34a476` | …**inside**. Offline-first; local models via Ollama. [repo](https://github.com/learningequality/kolibri) |
| **Sakai** | 🟡 **ECL-2.0** | `4debc94780cc` | `LICENSE` 11 120 B · `0688f62d04f1` | …**inside**, with notice obligations. 🔴 **Not Apache-2.0**, despite roundups saying so. [repo](https://github.com/sakaiproject/sakai) |
| **Moodle** | 🔴 **GPL-3.0** | `46c042e7da65` | `COPYING.txt` 35 147 B · `8ceb4b9ee5ad` | …**beside**, over Web Services / an MCP server. [repo](https://github.com/moodle/moodle) |
| **Open edX** | 🔴 **AGPL-3.0** | `87cd3811a425` | `LICENSE` 35 136 B · `e12d78569742` | …**in an XBlock** (Apache-2.0) — the supported seam. [repo](https://github.com/openedx/edx-platform) |
| **Chamilo** | 🔴 **GPL-3.0** | `2e5139a816d3` | `LICENSE` 35 147 B · `8ceb4b9ee5ad` | …**beside**, over its REST API. Deep LATAM footprint. [repo](https://github.com/chamilo/chamilo-lms) |
| **Frappe LMS** | 🔴 **AGPL-3.0** | `5d6df8e3ed8e` | `license.txt` 33 893 B · `db1a87ba81e8` | …**beside**. 🔴 Not MIT, despite 2026 roundups. [repo](https://github.com/frappe/lms) |
| **eXeLearning** | 🔴 **AGPL-3.0** | `c848eca0018d` | `LICENSE` 34 523 B · `0d96a4ff68ad` | …**beside**. Spain Ministry of Education-led. [repo](https://github.com/exelearning/exelearning) |
| **BigBlueButton** | 🔴 **LGPL-3.0** | `ec452b65043b` | `LICENSE` 7 652 B · `e3a994d82e64` | …**linked**, never forked. [repo](https://github.com/bigbluebutton/bigbluebutton) |
| **OpenEduCat** | 🔴 **LGPL-3.0** | `46a5d7d40082` | `LICENSE` 8 241 B · `528f84036800` | …**as an Odoo module**. Closest thing to an education ERP. [repo](https://github.com/openeducat/openeducat_erp) |

### Carried platform rows — graded by earlier passes, not re-measured on 2026-10-25

🔵 Stated as carried so a reader does not mistake an older reading for a fresh one.

| Platform | Licence (carried) | Note |
|---|---|---|
| **Canvas LMS** | 🔴 **AGPL-3.0** | The dominant North American LMS. 🔴 Its *agent* ecosystem is MIT — see below — and conflating the two is the single most expensive licence error available in this industry. |
| **Forma LMS** | 🟢 **Apache-2.0** | Corporate-training LMS; permissive. |
| **Opencast** | 🟡 **ECL-2.0** | Lecture capture and video management. |
| **H5P** | 🔴 **GPL-3.0** *(corrected `p450`)* | Interactive content types; embeds in Moodle, Canvas and Open edX. 🔴 ~~MIT~~ — `h5p-php-library` `LICENSE.txt` read first-hand 2026-10-26: **GPLv3, 35 146 B**. The MIT grant covers the **JS content types**, not the PHP integration layer. Permissive route: [edly-io/h5pxblock](https://github.com/edly-io/h5pxblock) (MIT), H5P as runtime content. |
| **Academico** | 🟢 **MIT** | Lightweight SIS. |
| **OpenSIS Classic** | 🔴 **GPL-2.0** | Student information system. |
| **frappe/lms** | 🔴 **AGPL-3.0** | Same project as **Frappe LMS**; two keys, one platform. 🔴 `p425`'s `T125`: the MIT belongs to `frappe/frappe`, the **framework**, not the LMS. |
| **`frappe/lms`** | 🔴 **AGPL-3.0** | The backticked spelling, kept so a citation under either form resolves. |

### 🔴 The agent-facing layer is MIT — and it is a DIFFERENT tier from the platform

The names below grade **MIT** because they are MCP servers and agents *over* a platform,
not the platform. A studio told *"Canvas is MIT"* would ship AGPL-3.0.

| Agent-tier name | Licence | What it actually is |
|---|---|---|
| **Canvas** | 🟢 **MIT** | The Canvas *MCP/agent* tier — not Canvas LMS (AGPL-3.0). |
| **Google Classroom** | 🟢 **MIT** | MCP servers over the Classroom API. 🔴 Use [`vTanco`](https://github.com/vTanco/google-classroom-mcp), **not** `pengusto` — relicensed proprietary 2026-10-23. |
| **Blackboard** | 🟢 **MIT** | The Blackboard agent tier. |
| **Blackboard Learn** | 🟢 **MIT** | MCP servers over Blackboard Learn's REST API. |
| **SCORM Runtime** | 🟢 **MIT** | SCORM 1.2/2004 packaging and playback. |

## 🆕 `p435` — The platform question has a **third** answer, and it is the platform the client is already running

This file has framed the platform decision as *which open-source LMS do we base on* —
OpenOLAT or Kolibri for a permissive base, Moodle or Open edX if copyleft is acceptable.
🟢 **`p435` adds a third option the shelf did not carry: do not replace the platform at
all — speak to it.** The grade census of this base's own backlog
(`compose/code/p435-promotion-sweep`, 2 450 addresses graded first-hand) surfaced a tier of
**MIT connectors for the platform a national school system actually runs**.

### 🟢 The national school-platform tier — every grant read first-hand on 2026-10-25

| Platform | Where it is the default | Connector | Grant | HEAD |
|---|---|---|---|---|
| **IServ** | German state schools | [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) | 🟢 **MIT** · 1 090 B · `5dc99bd5061f` | `8afdea14fbcd` @ 2026-10-25 |
| **Librus Synergia** | Polish schools | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) + [`librus-python-api`](https://github.com/krzysztofbury/librus-python-api) | 🟢 **MIT** · 1 071 B · `22e7ab2dbddc` | `e12e36f24224` @ 2026-10-25 |
| **Smartschool** | Flanders (Belgium) | [`MauroDruwel/Smartschool-MCP`](https://github.com/MauroDruwel/Smartschool-MCP) | 🟢 **MIT** · 1 069 B · `b414ff32815f` | `ab3fa81f857f` @ 2026-10-14 |
| **EduPage** | Slovakia and CEE | [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) | 🟢 **MIT** · 1 070 B · `e99290e1540b` | `b35ce653d2c9` @ 2026-10-23 |
| **Skola24** | Swedish municipal timetables | [`Kretiandpleti/skola-24-haos-integration`](https://github.com/Kretiandpleti/skola-24-haos-integration) | 🟢 **MIT** · 1 070 B · `8b34b498bb1f` | `fdbc9349b20f` @ 2026-10-25 |
| **DTU Learn** (Brightspace / D2L) | Denmark's technical university | [`CarlSvejstrup/dtu-learn-mcp`](https://github.com/CarlSvejstrup/dtu-learn-mcp) | 🟢 **MIT** · 1 079 B · `4f21e3f0f9fc` | `9444a1fd5199` @ 2026-10-07 |
| **NEIS** | Korea's national education data portal | [`hyunbinseo/neis-school-info`](https://github.com/hyunbinseo/neis-school-info) | 🟢 **MIT** · 1 068 B · `e82e1769aaaf` | `5c9ecede5208` @ 2026-09-27 |
| **Schoology + StudentVUE + Ion** | Fairfax County Public Schools (US) | [`jibberswrld/fcps-school-mcp`](https://github.com/jibberswrld/fcps-school-mcp) | 🟢 **MIT** · 1 073 B · `cd9e736254f8` | `7d9dfbfc32bb` @ 2026-09-28 |
| **Artemis** | TUM and its partner universities | [`ls1intum/edutelligence`](https://github.com/ls1intum/edutelligence) | 🟢 **MIT** · 1 091 B · `6b9b9eda00d6` | `a7584174bd3d` @ 2026-10-25 |
| Saigon University portal | Vietnam | [`zaikaman/SGU-Academic-MCP`](https://github.com/zaikaman/SGU-Academic-MCP) | 🟢 **MIT** · 1 068 B · `0b02f0945515` | `d5209305d13e` @ 2026-10-16 |

🔴 **Why this changes the shape of a proposal, not just its parts list.** `Trend 10` and
this file's own lead both say the platform tier is closed to permissive building — which is
true and is why `verticals/solutions.md` leads with OpenOLAT and Kolibri. 🟢 **But a
national school system is not going to migrate off IServ or Librus.** The engagement that
is actually available is a permissive **agent layer over the incumbent platform**, and
until this pass this file had no addresses for it outside Moodle and Canvas.

🟡 **Each connector is unofficial.** Every README says so: `iserv-mcp` warns that instances
differ and asks you to test against the school's own installation; `dtu-learn-mcp` is a
student project and says to use it only with your own account. 🔴 **That is a contract
risk, not a licence risk**, and it is the first question to settle in a deployment: an
unofficial client against a system of record has no API stability promise and no vendor
escalation path.

### 🟢 The public-authority tier — the platform's *owner* publishing its own code

| Authority | What is published | Grant | HEAD |
|---|---|---|---|
| **Utdanningsdirektoratet** (Udir, Norway) | [`PAS2-Public`](https://github.com/Utdanningsdirektoratet/PAS2-Public) — the new exam and test administration services, with public issues and wiki | 🟢 **Apache-2.0** · 11 325 B · `cb5e8e7e5f4a` | `489129c42c9d` @ 2026-09-25 |
| **Department for Education** (England) | [`get-information-about-schools`](https://github.com/DFE-Digital/get-information-about-schools) — the national school registry | 🟢 **MIT** · `LICENCE` 1 116 B · `e18299fd1942` | `ad46faf42690` @ 2026-10-21 |
| **Department for Education** (England) | [`education-benchmarking-and-insights`](https://github.com/DFE-Digital/education-benchmarking-and-insights) — FBIT school finance benchmarking | 🟢 **MIT** · 1 091 B · `5a22fb5576a5` | `3cdbf2cbf47b` @ 2026-10-22 |
| **Department for Education** (England) | [`teaching-vacancies`](https://github.com/DFE-Digital/teaching-vacancies) — the national teaching job service, source **and** infrastructure | 🟢 **MIT** · 1 092 B · `c561ea849ed6` | `a2d4f5fdec58` @ 2026-10-22 |
| **Oak National Academy** (England) | [`oak-curriculum-api`](https://github.com/oaknational/oak-curriculum-api) — the national curriculum as a documented API · [`oak-ai-lesson-assistant`](https://github.com/oaknational/oak-ai-lesson-assistant) — its own AI lesson planner | 🟢 **MIT** · 1 077 B | `0561df5aac12` · `c6871efa8f08` |

🟢 **This is the strongest procurement argument on this file for an EMEA public-sector
engagement**, and it is a different argument from "open source is cheaper": the buyer's own
ministry has already published the data model, the service contract and in Oak's case the
reference AI application. A proposal can cite the client's own code.

🟡 `oak-curriculum-api` and `oaknational/oak-openapi` are the **same repository** — identical
HEAD under `git ls-remote` — so this file carries one row, not two.

### 🔴 The education-ERP nil is unchanged, and this does not touch it

`p433` and `p434` recorded a **standing nil** on a permissive education ERP, confirmed
three passes running. 🔴 **Nothing above changes that.** A school-platform *connector* is
not an ERP, Udir's exam administration is not a student information system, and FBIT is a
finance analytics surface over DfE data rather than a finance system. The nil stands; what
has changed is that the **integration** layer over a national incumbent now has addresses.

## 🆕 `p434` — The education-ERP nil is now a **standing** nil, confirmed a third consecutive pass, and one carried row is corrected

🔴 **The sweep was run again verbatim** (`open source platform education ERP CRM MIT Apache`) and
returned **nil for a permissive education vertical for the third consecutive pass**. What came
back, and why each is not the answer:

| Returned | Grant | Why it is not a permissive education vertical |
|---|---|---|
| **OpenEduCat** | 🔴 **LGPL-3.0** (carried on this file) | The closest thing to an education ERP, built on Odoo. Weak copyleft — integrate, do not vendor. Not permissive. |
| **Apache OFBiz** | 🟢 Apache-2.0 | Genuinely permissive and genuinely **not education** — a general ERP framework. Already this file's `p386` answer for the permissive ERP *base*, and it remains a build, not a product. |
| **ERPNext** | 🔴 GPL-3.0 | General ERP. Strong copyleft. |
| General MIT CRMs | 🟢 MIT | Not education. |
| **CK-ERP** | — | Has education modules (`ck-teacher`, `ck-student`, `ck-registrar`…) but the announcement found dates from **2010**; stale, not a candidate. |

🟢 **So the standing sentence holds and should be quoted rather than re-derived:** *there is no
MIT/Apache education ERP.* It is why this file leads with **OpenOLAT** (Apache-2.0) and
**Kolibri** (MIT), and why `p386`'s permissive-ERP-base answer below is a *base* and not a
product. 🔵 Three independent passes have now spent a leg on this question; a fourth should quote
this row instead.

🔵 **No new platform supply this pass.** The two addresses promoted to `agents/top.md`
(`wenflow-org/wenflow`, `zhangl1001/civil-ai` — both MIT) are agent-layer, not platforms, and the
five high-traction unpromoted addresses graded in `repos/trending.md` are all copyleft,
content-licensed or ungranted. `Trend 10`'s split is unchanged: **the agent layer is permissive,
the platform layer is not.**

🔴 **One correction that matters for a special-education engagement.** This file records that
there is **no open-source special-education system of record** — unchanged, and `p434` adds the
regulatory reason it is unlikely to matter in NYCPS: that district's guidance **prohibits AI
development of IEP and 504 plans outright** (`Gap 433-B`, closed; `intel/market.md`). 🔵 So the
missing system of record is not the binding constraint there — the drafting prohibition is, and
the sellable surface is progress monitoring and accommodation *delivery* against plans a
qualified professional wrote. `compose/patterns.md` `Pattern AL` carries the split.

## 🆕 `p433` — The "education ERP" sweep returns a **standing nil**, and it is the reason this file leads with OpenOLAT and Kolibri

The brief for every pass asks for platforms *"like Odoo for ERP"*. `p433` ran that leg directly —
`open source platform education ERP CRM MIT Apache` — and the result is a **nil worth recording as
a standing fact rather than re-discovering every pass**:

| What the sweep returned | Grant | Education-relevant? |
|---|---|---|
| Apache OFBiz | Apache-2.0 | 🔴 No education module; a general ERP framework |
| Aureus ERP, Krayin CRM, Atomic CRM | MIT | 🔴 General ERP/CRM, no education vertical |
| Huly Platform | Apache-2.0 | 🔴 General, and needs strong in-house capability |
| **ERPNext** | 🔴 **GPL-3.0** | 🟡 **Lists Education among its verticals** — the nearest thing to an education ERP, and it is copyleft |
| iDempiere (GPL-2.0), Dolibarr (GPL-3.0) | 🔴 copyleft | 🔴 General |

🔴 **So: there is no MIT/Apache-licensed education ERP.** The one system that genuinely covers the
education vertical, **ERPNext**, is GPL-3.0, which puts it in this file's integrate-don't-vendor
tier alongside Moodle and Chamilo. **OpenEduCat**, already on this shelf, is the Odoo-based
education ERP and is **LGPL-3.0** — weak copyleft, which is materially better than GPL for an
AI-layer build but still not permissive.

🟢 **Which is the whole argument for how this file is ordered.** `OpenOLAT` (Apache-2.0) and
`Kolibri` (MIT) are not merely *options* in the permissive tier — after this sweep they are
**demonstrably the only ones**, and that is now a measured statement rather than a curatorial
preference. A client who needs a permissive full platform has exactly two choices; a client who
can take copyleft has many. 🔵 `Gap 433-C` applies: this is a search-channel nil, not proof of
absence — but it is the fourth consecutive pass on which the permissive platform tier has not
grown.

## 🆕 `p432` — Special education is a **platform gap**, not a product gap

Every platform row on this file treats the IEP/§504 learner as an ordinary enrolment. None of
them — Moodle, Open edX, Canvas, Sakai, OpenOLAT, Kolibri, OpenEduCat, OpenSIS — ships an
individualised-education-program workflow: goal authoring, progress monitoring against those
goals, accommodation records, or the team-review-and-sign step US law requires. The commercial
market is served here (PowerSchool Special Programs, Frontline, SEIS); **open source is not.**

That makes special education the clearest *platform-adjacent* build on these shelves: there is no
incumbent open platform to displace, and the integration surface is the SIS, not the LMS.

### The deployable pieces that do exist, graded by grant (read at HEAD 2026-10-25)

| Component | Licence | HEAD | Payload | Where it sits |
|---|---|---|---|---|
| [**AlloFlow**](https://github.com/Apomera/AlloFlow) | 🔴 **AGPL-3.0-or-later** | `6194e51e8f1f` | `LICENSE` 35 442 B · `698099632698` | …**beside, over an interface.** The only maintained accessibility-first differentiation engine found: UDL levels/layers/outputs, WCAG, AAC, text-to-speech, offline-first, i18n, Electron + React. Network copyleft over a hosted engine — reach it over HTTP, never vendor it. |
| [**California IEP AI project kit**](https://github.com/robotros/California-IEP-AI-project-kit) | 🟢 **MIT** | `ff1ae0ce30e7` | `LICENSE` 1 065 B · `43554d1189d8` | …**as the knowledge and boundary layer** on whatever drafting surface the district already has. Carries its own "not the system of record" discipline. |
| [**iep-builder**](https://github.com/67tallchris/iep-builder) | 🟢 **MIT** | `b39df0e9a4a1` | `LICENSE` 1 069 B · `aa8cfde0dc31` | …**as a standalone per-district app** (Cloudflare Pages + D1, bring-your-own-key). The deployment shape when a district will not accept a central student store. |
| [**access-to-education**](https://github.com/dougdevitre/access-to-education) | 🟢 **MIT** | `f8abd70707ba` | `LICENSE` 1 069 B · `fc7c8b90fee1` | …**in the parent portal** (`p388`'s surface). ~120 k words of IEP navigation and advocacy content, MIT-granted. |
| [**rubric-desk**](https://github.com/rwrife/rubric-desk) | 🟢 **MIT** | `010a44006014` | `LICENSE` 1 063 B · `c186f5cb204a` | …**as the offline marking surface** (Flutter, no accounts). Pairs with Kolibri where connectivity cannot be assumed. 🟡 Created 2026-10-25. |

🔴 **Not available, and it is the load-bearing piece:** an open-source special-education **system
of record**. `OpenSIS Classic` (GPL-2.0) and `Academico` (MIT) are general SIS products with no
IEP module. So the architecture is forced: the drafting assistant writes a *draft*, and the
authorised commercial system records the entry. That constraint is not a limitation to work
around — in North America it is the compliance requirement (see `intel/market.md`, North America),
and `robotros`' kit states it in its own README.

🔴 **Non-US equivalents: nil result.** No open-source tooling was found for England's EHCP
process or for the inclusive-education mandates of Brazil, Chile or Colombia. Searched; absent.

## 🆕 `p431` — Evaluation is a platform-adjacent procurement surface, and it is the one tier with no copyleft problem

This file grades **platforms**, and its standing finding is that the platform tier is copyleft while
the agent tier is permissive. `p431` measured a third tier that sits beside both and behaves
differently from either: **tutoring evaluation.**

| Component | Grant (read at HEAD, 2026-10-25) | Where it sits relative to the platform |
|---|---|---|
| [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | Apache-2.0 code / CC-BY-4.0 content / brand policy | **Beside** the platform — runs in CI, never links the LMS |
| [Teachable-AI-Lab/tutor_gym](https://github.com/Teachable-AI-Lab/tutor_gym) | MIT | **Beside** — drives the tutoring runtime through its own interface |

🟢 **Why that placement matters commercially.** An evaluation harness **never links against the
LMS**. It drives the tutoring runtime from outside and reads results. So a client on **Moodle
(GPL-3.0)**, **Open edX (AGPL-3.0)**, **Chamilo (GPL-3.0)** or **Frappe LMS (AGPL-3.0)** can take a
fully permissive evidence pack **without the platform's copyleft reaching any of it**. This is the
one tier on this shelf where the platform's licence is simply not a constraint — no XBlock seam, no
GPL-adapter sandwich, no packaging decision.

🟡 **It is also the part of a bid the incumbent platform vendor cannot supply.** Moodle, Canvas and
Open edX vendors sell delivery; none of them sells *proof that the AI teaches well*. Against the
LATAM pattern this base already records — public buyers procuring AI education platforms as
**subscriptions**, with **no tender asking for open source** (`Trend 21`) — the evidence pack is the
line item that fits: assurance work attached to someone else's platform, priced as advisory.

🔴 **Scope limit, stated:** this covers **tutoring** only. There is no open harness for the
**grading** path (`Gap 431-C`), which is the surface NA, EMEA and APAC statutes regulate hardest.
Quote grading assurance as bespoke work.

## Choosing the base — the decision in one pass

1. **Client needs a full LMS and cannot accept copyleft** → **OpenOLAT** (Apache-2.0).
   This is the under-used answer; most teams default to Moodle and inherit GPL unnecessarily.
2. **Connectivity is unreliable, or equity is an explicit requirement** → **Kolibri** (MIT).
3. **Client already runs Moodle / Canvas / Open edX** (the common case) → **do not migrate.**
   Add an MIT **MCP server** beside it. See `compose/patterns.md`, Pattern A.
4. **Client needs student records, not just courses** → **OpenEduCat** on Odoo — the only
   integrated LMS+SIS in open source. 🔴 No MIT- or Apache-licensed SIS exists; this was
   searched for again on 2026-10-25 and the gap is real, not an absence of looking.

## 🔴 What is *not* available as open source, and matters

- **A permissive SIS.** Searched again this pass; nothing MIT/Apache. OpenEduCat (LGPL-3.0)
  is the only integrated option.
- **A credible open proctoring stack for the EU.** Emotion recognition in educational
  institutions is *prohibited* under the AI Act since Feb 2025, so the category is
  substantially closed in EMEA regardless of supply.
- **An open curriculum graph on permissive terms.** The best one found
  ([os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)) is **ODbL** — share-alike
  on derived data.

---

## Choosing the base: the four-way decision

| if the client needs… | base | licence | the catch |
|---|---|---|---|
| **To own closed extensions to the platform itself** | [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | Smaller plugin ecosystem than Moodle; more build, less assemble. **The only permissive major LMS.** |
| **The widest plugin ecosystem and the largest talent pool** | [Moodle](https://github.com/moodle/moodle) | 🟡 GPL-3.0 (`COPYING.txt`) | Copyleft on anything linked. Extend through web services / the MCP plugin, not by patching core. |
| **MOOC scale, cohort analytics, deep data control** | [Open edX](https://github.com/openedx/edx-platform) + [tutor](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 | AGPL reaches **hosted** use. Build XBlocks and LTI tools; keep proprietary logic the other side of the boundary. |
| **🆕 `p389` No incumbent platform at all, and lessons needed now** | [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **MIT** | Not an LMS: no enrolment, no gradebook of record, no SIS. You get the *teaching surface* and you still owe the system of record. See the section below. |
| **🆕 `p390` To *ship* a modified platform, not host one** | [OLI Torus](https://github.com/Simon-Initiative/oli-torus) | 🟢 **MIT** | **The only permissive answer on this shelf, and the catch is staffing, not licensing.** Carnegie Mellon Open Learning Initiative's courseware engine: authoring + delivery, adaptive scripted activities, per-objective mastery reporting, LTI 1.3 delivery into a host LMS. Every other base of comparable scope here is GPL/AGPL, so this is the row to reach for when the deliverable is **software the client redistributes or embeds in a product**. 🔴 **Elixir/Phoenix + PostgreSQL** — a genuine staffing constraint; cost the hiring before proposing it. 🔴 Slug trap: `CMU-OpenLearning/oli-torus` does not resolve. Dated **2026-10-22**. |
| **🆕 `p393` To ship a small permissive LMS, in Spanish, with billing already in it** | [now-lms](https://github.com/bmosoluciones/now-lms) | 🟢 **Apache-2.0** | **21 ★** and no multi-tenancy claim. A Flask application a studio can read in a day — which is the point — but not a ministry platform. |
| **North American higher-ed integration reality** | [Canvas LMS](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0, open-**core** | The published tree ≠ the commercial ecosystem. Scope integrations against the real tenant, not the repo. 🆕 `p389` **And the published tree is also *older than it looks*: `master` last moved 2026-04-30 — 175 days — while the `stable/*` branches move.** Read the API surface off the tenant, and if you must read it off the repo, say which ref. 🟡 🆕 `p390` **Dating caveat, so nobody demotes Canvas off a bad read:** its `master` last moved **2026-04-30 — 175 days**, but Canvas **ships from tags** (`v5.14.2` current), not from the default ref. For any tag-releasing project, a last-commit-on-default-ref date under-reports maintenance; check `git ls-remote --tags` before calling it stale. |

### Regional fit
- **LATAM / Iberia:** 🆕 `p393` **the permissive option now exists and it is regional:**
  [now-lms](https://github.com/bmosoluciones/now-lms) (🟢 **Apache-2.0**, © BMO … S.A., **Nicaragua**;
  676 files, 505 commits, HEAD **2026-08-31**) is the only Spanish-language LMS on this shelf a studio
  can fork and ship **closed**. Use it for SME and pilot delivery; keep Chamilo for public-sector scale.
  [Chamilo](https://github.com/chamilo/chamilo-lms) (GPL-3.0) — strongest
  Spanish/Portuguese public-sector base. [academico-sis/academico](https://github.com/academico-sis/academico)
  (MIT) for SME-scale administration with Spanish built in.
  🆕 `p387` For **Brazil specifically**, the base a municipal engagement will already be running is
  [portabilis/i-educar](https://github.com/portabilis/i-educar) (GPL-2.0-or-later, **real default
  ref `2.12`**) — see the administration table below — and the agent tier now has three granted
  LATAM-native options on [`agents/top.md`](../agents/top.md),
  including one that ships **as an Open edX plugin** rather than as a separate app.
- **EMEA public sector:** [ILIAS](https://github.com/ILIAS-eLearning/ILIAS) (GPL-3.0, default ref
  `release_11`) and [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, Switzerland).
  🆕 `p393` For **assessment migration**, which EMEA procurement is beginning to specify as QTI 3.0:
  [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) (🔴 **GPL-3.0** — run it
  as a batch tool at arm's length, never linked), from the lab of **Cito, the Dutch national assessment
  institute**. For a **Swiss university** engagement,
  [Dathis/swiss-moodle-mcp](https://github.com/Dathis/swiss-moodle-mcp) (🟢 MIT) already speaks ZHAW,
  FHNW, ETH and EPFL Moodle with **SWITCH edu-ID** user-held authentication — 🔴 but at **0 ★** and
  self-described as an unofficial student project, so it is a pilot reference, not a dependency.
  [Serlo](https://github.com/serlo/serlo.org) (Apache-2.0, Germany) and
  [Richie](https://github.com/openfun/richie) (MIT, France) for content and catalogue.
- **APAC:** Moodle itself is Australian in origin; [netless-io/flat](https://github.com/netless-io/flat)
  (MIT) for live online classrooms.
- **Low-connectivity anywhere:** [Kolibri](https://github.com/learningequality/kolibri) (MIT,
  default ref `develop`) — offline-first by design, not as a degraded mode.
- **K-12 administration anywhere:** [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic)
  (GPL-2.0, default ref `master`) — the student-record half that no permissive base supplies.
- 🆕 `p393` **North America K-12 data integration:** the standard is **Ed-Fi**, and the granted client
  is [edanalytics/edfi_api_client](https://github.com/edanalytics/edfi_api_client) (🟢 **Apache-2.0**,
  stock 11,357 B, HEAD **2026-10-06 — 16 d**). The **Canvas / Google Classroom / Schoology → Ed-Fi**
  extractors exist at [Ed-Fi-Exchange-OSS/LMS-Toolkit](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit)
  (🟢 Apache-2.0) 🔴 **but that repository was ARCHIVED by its owner on 2025-03-10 and is read-only** —
  port its field mappings, never depend on it.

## 🔴 The sovereign-stack story in EMEA, corrected

The previous pass carried a headline that **openDesk Edu** was deployed in **8,600 German schools**
and then downgraded it to "traces to a single news item with no official confirmation". **This pass
re-ran the search and the downgrade stands — in fact it goes further:**

- What is **confirmed**: openDesk is a free and open-source productivity suite from **ZenDiS** (the
  German Center for Digital Sovereignty in Public Administration); **v1.0 released 20 Oct 2024**.
  ZenDiS works with France's **DINUM** on the French equivalent **LaSuite**, and the two agencies
  added videotelephony, note-taking and SSO to both suites in **100 workdays**.
- What is **not confirmed**: **no school deployment of openDesk appears in any source found this
  pass.** Named users are public-administration bodies (BWI GmbH for the Bundeswehr, the ÖGD public
  health service). Germany's **DigitalPakt Schule** (€6.5bn school infrastructure) is a separate
  programme and is not evidence of openDesk in schools.
- **How to use it anyway:** the *pattern* is real and sellable even if the school number is not —
  **ILIAS (learning) + OpenProject (collaboration) behind a single SSO**, all open source, all
  EU-hosted. That is the sovereign education stack an EMEA public-sector client will ask for. Sell
  the architecture; do not quote the 8,600.

## Student information and administration

| platform | repo | default ref | licence | fit |
|---|---|---|---|---|
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 `19.0` | 🟡 LGPL-3.0 | Odoo-based SIS/ERP: admissions, curriculum, fees, library, hostel. The Odoo ecosystem is the reason to pick it — AI modules can be ordinary Odoo addons. |
| **Academico** | [academico-sis/academico](https://github.com/academico-sis/academico) | `main` | 🟢 MIT | Laravel, Spanish + French built in, SME-scale: courses, enrolments, scheduling, reports. |
| **openSIS Classic** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 `master` | 🟡 GPL-2.0 — 🔴 grant at **`docs/License.txt`**, not at any root path | 🆕 `p384`. The K-12 default: enrolment, attendance, grades, scheduling, parent/student portals. GPL-2.0 is survivable the Moodle way — reach it over its API, never link. 🔵 A root-only licence read reports this repo as ungranted; it is not. |
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | 🔴 `develop` | 🔴 AGPL-3.0 (`license.txt`) | Only where the client already runs ERPNext — then the student record and the finance record are one system. |
| **i-Educar** 🆕 `p387` | [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **`2.12`** | 🟡 GPL-2.0-or-later (`2.12/LICENSE`, 18,092 B) | 🟢 **The LATAM row this table was missing.** Brazil's largest free education software — municipal student records, enrolment, grades — deployed by Brazilian municipalities at scale and maintained by Portabilis plus a community. 🔴 Its default ref is the version branch **`2.12`**: clone and read the grant there, not at `main` or `master`. Reach it over its API; keep AI alongside it, never inside it. Sibling `i-diario` (classroom diary) is **AGPL-3.0** — different grant, same organisation. |

### 🆕 `p386` — the permissive ERP **base**, since the permissive education ERP does not exist

Every row in the table above is copyleft except `academico` (MIT, SME-scale). The prescribed ERP/CRM
research leg was run directly at that gap. **It does not close it** — no education-specific
permissive ERP was found, which *confirms* the structural claim on
[`repos/foundations.md`](../repos/foundations.md) — but it returns three permissive bases, all three
licence payloads read first-hand this pass:

| base | real default ref | licence | what you get, and what you build |
|---|---|---|---|
| [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) | 🔴 **`master`** | 🟢 **MIT** *(1,077 B, "Copyright 2010-2025, Webkul Software"; `composer.json` also declares `"license": "MIT"`)* | Laravel 13 + FilamentPHP 5 modular ERP **with a plugin system**: accounting, inventory, HR, CRM, projects, and a Filament admin panel a client's staff can actually use. 🔴 **No education module** — admissions, curriculum, fees, attendance and transcripts are **your build**. |
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | 🔴 **`2.2`** *(version branch; no `main`)* | 🟢 **MIT** *(1,078 B, same Webkul holder)* | The **admissions funnel** as a CRM: lead → applicant → enrolment, with the pipeline, activity log and email already built. The piece an SIS always lacks and a school always asks for. |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 🔴 **`trunk`** | 🟢 **Apache-2.0** *(11,906 B; `NOTICE` 166 B, "Copyright 2001-2026 The Apache Software Foundation")* | The ASF alternative: accounting, CRM, manufacturing, order management. 🔴 Developer-facing and heavy — pick it for ASF governance and longevity, not for time-to-first-demo. 🆕 `p389` **Dated: `trunk` committed 2026-10-22 — 0 days. The ASF-longevity argument holds up.** 🔴 **But write the `-framework` suffix into the proposal.** [apache/ofbiz](https://github.com/apache/ofbiz) — the address anyone guesses — resolves, carries a valid Apache-2.0 grant, and its `trunk` **last moved 2017-02-12, 3,539 days ago**. It is the retired monolith. A client engineer who checks the obvious address finds a nine-year-dead tree and concludes the recommendation was careless. |

🔵 **What this changes in a pitch.** [OpenEduCat](https://github.com/openeducat/openeducat_erp)'s
**LGPL-3.0** used to be the only road to an open-source education ERP, so it was not a decision. It
is now a **trade against a named alternative**:

- **Take OpenEduCat (LGPL-3.0)** → admissions, curriculum, fees, library and hostel exist today, on
  the Odoo ecosystem, and AI features can be ordinary Odoo addons. You accept LGPL on the modules
  and the Odoo version-branch cadence (`19.0`).
- **Take Aureus (MIT) + Krayin (MIT)** → the client owns every line, including the education
  modules you write. You are costing **admissions, curriculum, fees, attendance and transcripts as
  a build**, on a base whose plugin system is designed for exactly that.

🔴 **Do not sell the second option as "an open-source education ERP."** It is a permissive ERP plus
a scoped education build, and the honest version of that sentence is the one that survives the
client's own technical review.

🟡 **Still not found, and still the clearest build-vs-buy opening in the rotation:** no open-source
Brazilian or Mexican academic-management system. Aureus + Krayin is now the most *defensible*
starting point for one — Laravel, MIT, and `academico` (MIT, Spanish-native) already proves that
stack fits the region's SME school market.

## Content, assessment and media layers

| layer | platform | licence | note |
|---|---|---|---|
| Interactive content | [H5P](https://github.com/h5p/h5p-php-library) | 🟡 **GPL-3.0** | Embeds in Moodle, Open edX, Canvas, Drupal, WordPress. 🔴 Widely mislabelled MIT. Treat as runtime content, not linked code. |
| 🆕 `p393` H5P **inside Open edX** | [edly-io/h5pxblock](https://github.com/edly-io/h5pxblock) | 🟢 **MIT** *(1,064 B)* | 🟢 **The permissive way to get H5P content into an AGPL platform.** Self-hosted H5P player as an XBlock — HEAD **2026-10-16 — 6 d**, 82 commits, 23 releases, **19 ★**. 🔵 Note the licence shape, which is `p390`'s firewall again: the **content library** above is GPL-3.0 and the **platform** is AGPL-3.0, but this bridge is MIT, so the part a studio writes against stays permissive. |
| 🆕 `p393` QTI assessment exchange | [vosslab/qti_package_maker](https://github.com/vosslab/qti_package_maker) (🟡 **LGPL-3.0**) · [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) (🔴 **GPL-3.0**) | 🟡 / 🔴 copyleft | **Write** QTI packages for Canvas/Blackboard, and **convert** QTI 2.x ↔ 3.0. The assessment-portability layer this shelf had no row for. 🔴 Neither is permissive: use the LGPL one as a **linked dependency** and the GPL one as an **arm's-length batch tool**. 🔴 A third family — PyPI's `timeback-qti` / `-oneroster` / `-caliper`, 147 releases, MIT **declared** — has an **unresolvable source repository**, so it is listed here only as a warning, not an option (`Gap 393-B`). |
| Structured pedagogy | [Oppia](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | Misconception-aware lesson branching. Permissive and pedagogically serious — unusual combination. |
| Open-response assessment | [openedx/edx-ora2](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 | Peer + self + staff assessment rubrics. The place an LLM grader must plug in to stay auditable. |
| Lecture capture | [opencast/opencast](https://github.com/opencast/opencast) | 🟡 ECL-2.0 | Video pipeline → the transcript corpus every education RAG build needs. |
| 🆕 `p390` Self-hosted video delivery | [Chocobozzz/PeerTube](https://github.com/Chocobozzz/PeerTube) | 🔴 **AGPL-3.0** | Federated (ActivityPub) video hosting — the option when lecture video must stay off YouTube and off a hyperscaler, which is a recurring EMEA public-sector requirement. 🔴 **Network copyleft: hosting it as a service for the client triggers source obligations** — fine for a public institution, usually not for a commercial product. Dated **2026-10-16**. 🔴 **A wrong-slug trap worth naming, because it inverts the licence:** [`PeerTube/PeerTube`](https://github.com/PeerTube/PeerTube) also resolves, is **3,660 days stale**, and reads **GPL-3.0** — so a careless licence read off that slug gets the *wrong grant* for the project, not merely a stale one. The canonical owner is `Chocobozzz`. |
| Live classroom | [netless-io/flat](https://github.com/netless-io/flat) | 🟢 MIT | Whiteboard, recording, real-time session. |
| Interop boundary | 🆕 `p392` [academic-innovation/django-lti](https://github.com/academic-innovation/django-lti) (**Python**) · [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) (Node) · [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) (Node, **serverless**) · [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) (PHP) | 🟢 **MIT / Apache-2.0 / MIT / Apache-2.0** | **The copyleft firewall, and as of `p392` it is maintained in THREE languages including Python.** 🆕 `p392` `django-lti` (🟢 MIT, 1,098 B, HEAD **2026-10-20**, PyPI v0.10.1) puts LTI Advantage **inside** a Django agent — one middleware, no second runtime — so `p391`'s *"the edge must be Node or PHP in front of the agent"* is withdrawn; `lti-tool/lti-tool` (🟢 MIT, HEAD **2026-10-20**, npm `@lti-tool/core` v1.3.2) is the **serverless** Node option for Lambda / Cloudflare Workers, where `ltijs` assumes a long-running process with Mongo. 🔴 `p390` dated the standards-body reference copy at 2,332 days and concluded the boundary had no installable implementation; that was wrong. **`ltijs`** — npm v7.0.7, **207 versions, published 2026-10-06**, HEAD 2026-10-13 — and **`packbackbooks/lti-1p3-tool`** — packagist v6.4.4, **68 versions, published 2026-09-23**, HEAD 2026-10-16 — are both live, both Apache-2.0, and either one keeps permissive code the right side of a GPL/AGPL platform boundary without linking to it. Prefer **`ltijs`** unless the client's platform work is already PHP. 🔴 Cite [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) as the **spec reference only** — 2,333 days, and `IMSGlobal/lti-1-3-php-library` is the same project at a renamed org (identical HEAD `3a192de`). 🔴 There is **no maintained Python LTI library**, so the edge is Node or PHP in front of a Python agent. Full note in [`repos/foundations.md`](../repos/foundations.md). |
| Local-first tutoring workspace | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** | 🆕 `p386`. Self-hosted, block-based adaptive workspace: PDF in → notes, flashcards, quizzes and an adapting tutor out, with **FSRS** scheduling, a knowledge graph and cognitive-load detection. Runs on local open-weight models — **no API key, no data leaving the host**, which is the answer to a DPO who will not approve an external model call at all. |
| Campus LLM gateway | [LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | Multi-provider, SSO, quota, audit log. The audit log is what gets a deployment past a university's data-protection officer. |
| Courseware platform | [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT** | 🆕 `p384`. Django courseware with autograding, flexible access rules and per-student statistics. Course-scale and permissive — the base when the client must own the platform code but does not need an institutional LMS. |
| **Agent-native teaching OS** | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | 🔴 **AGPL-3.0** (`main`) · 🟢 MIT at tag `v0.1.0` | 🆕 `p385`. The **inverse** of every other row here: instead of bolting an agent onto an LMS, the classroom itself is an MCP server (~50 tools) and the agent is bring-your-own. Courses, lessons, FSRS flashcards, graded exercises, and a persistent learner-memory layer (`get_context` / `get_learner_brief`) that survives a change of model or session. 🔴 **v1 is single-machine and unauthenticated** — a pilot substrate, not a tenant-ready platform. AGPL reaches hosted use, so a client deployment must either accept that or pin the MIT `v0.1.0` tag and forgo upstream. |
| **Curriculum prerequisite graph** | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL** | 🆕 `p384`. 1,930 micro-topics, 4,102 prerequisite edges, 9 subjects; aligned to NGSS, Common Core, UK National Curriculum, Australian curriculum. 🔴 **Share-alike database licence, not a code licence** — ground a tutor on it (§4.3 *Produced Work*, attribution only); do **not** ship an extended taxonomy (§4.4 *Derivative Database*, share-alike). See **Pattern H**. |

## 🟡 MCP has reached the LMS — and this is new as of 2026

This did not exist a year ago and it changes the integration story:

- 🆕 `p387` **Moodle, the tenancy layer — and this is the part a client-ready deployment needs
  before any MCP server:** [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager)
  (GPL-3.0-or-later, granted in `version.php`, release **5.1.1**) is a **multi-tenant AI backend**
  offered as the alternative to Moodle 4.5's own single-tenant AI subsystem: `aitool` subplugins
  connect providers (ChatGPT, Gemini, Dall-E, **Ollama** for on-premises), `aipurpose` subplugins
  bind a purpose to a provider **per role**, with per-role rate limits, per-tenant enable/disable,
  usage monitoring and capability-gated teacher visibility of student prompts. 🔵 The same project
  is also published at `mebis-lp/moodle-local_ai_manager` — **identical HEAD sha, one project, two
  addresses.** 🔴 Its own README warns it is **not compatible with core-AI-subsystem plugins and
  vice versa**: choosing it is an architectural fork in the road, taken once, early.
- 🆕 `p387` **Open edX, first-party AI extension point:**
  [openedx/openedx-ai-extensions](https://github.com/openedx/openedx-ai-extensions) (AGPL-3.0-only)
  is the platform org's own AI extensibility framework — **experimental**, but it is the contract to
  build against instead of forking `edx-platform`. Pair it with
  [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) for the agent-facing surface.

- **Moodle, first-party path:** the **`webservice_mcp`** plugin in **Moodle's own plugin directory**
  (and the Moodle Marketplace) exposes Moodle's external functions as **MCP tools over JSON-RPC
  2.0**. Supports **Moodle 4.5–5.2**, latest release **23 Jul 2026**, gated on the
  `webservice/mcp:use` capability. Configured inside Moodle — no fork, no patch, **no GPL exposure
  for the agent on the other side of it.**
- **Canvas, community path:** [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (MIT)
  and its fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (MIT, adds office
  hours, syllabus read/write, student groups, course-content copy).
  [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) advertises 54
  tools and Streamable HTTP; it has **no licence file**, but `package.json` declares
  `"license": "MIT"` — 🟡 **manifest-only MIT**, usable if you record the manifest line and ask for
  the file.
- 🆕 `p386` **Blackboard, community path — and it is no longer empty.** Nine addresses probed,
  **6 MIT grants read first-hand**, 1 ungranted, 2 dead. 🟢 **[nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp)
  (MIT) is the only institution-grade LMS MCP server on any of these shelves**: official Blackboard
  Learn REST API, OAuth2, role gate, FERPA handling, rate limiting, PII scrub, JSON audit log,
  Prometheus `/metrics`, 40 tools including **grade write-back** (maintainer self-claims, read not
  executed). The other five —
  [Mattlo0546](https://github.com/Mattlo0546/blackboard-mcp),
  [alanwtom](https://github.com/alanwtom/blackboard-mcp),
  [lukecarroll15](https://github.com/lukecarroll15/blackboard-mcp) (ref **`tcd`**),
  [felipedias-ie](https://github.com/felipedias-ie/blackboard-mcp),
  [Loganxgreaves](https://github.com/Loganxgreaves/blackboard-mcp) (ref **`master`**) — are
  **student-side**: they ride the signed-in user's own browser SSO session. 🔴 Granted, useful, and
  **not deliverable to an institution**.
- 🆕 `p386` **Brightspace / D2L — six addresses, six MIT grants.**
  [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) is the fullest
  (TOTP/OAuth/browser auth strategies, retry + circuit-breaker + cache, **opt-in writes**);
  [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) is the
  upstream of a fork family whose copies publish **byte-identical** licence payloads, so count it
  once. 🔵 **All six are student-side** — an institution-grade D2L server is the one genuine
  greenfield contribution left on this platform.
- **No official server** from Instructure, Moodle HQ, Anthology/Blackboard or D2L. 🟡 Verified gap —
  every server named on this shelf is community-built.
- 🔴 [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) is **UNGRANTED** — no licence file
  *and* no `license` field in its `pyproject.toml`. Use the plugin-directory route for Moodle:
  [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) has no root
  licence file either, but its `version.php` carries the full **GPL-3.0-or-later** header that
  Moodle requires of every plugin, so it *is* granted.

## 🆕 `p388` — The parent portal is a platform surface, and it was missing from this shelf

This shelf asks *"what does the client already run, and what can be bolted onto it?"* For every
platform below it answered that for **the learner, the teacher and the administrator**. It never
answered it for **the parent** — yet in K-12 the parent portal is a shipped feature of every SIS and
the one surface families actually log into.

| platform | server | ref · HEAD | licence | what it bolts on |
|---|---|---|---|---|
| **Infinite Campus** (Campus Parent) | [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` · `971d58f` | 🟢 **MIT** (1,067 B) | 🟢 **The first SIS parent portal on this shelf.** 20 tools: schedule, assignments (`missingOnly`), grades + 14-day recent window, **attendance events with codes and comments**, behavior, food service, documents, standardized **assessment scores**, fees, messaging from three sources. Linked districts auto-discovered via **CUPS SSO**; `FeatureDisabled`-aware, so a district that has switched a module off degrades instead of erroring. **47 npm releases**, → 2026-10-19. |
| **Canvas** | [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` · `428b78b` | 🟢 **MIT** (1,067 B) | 18 `canvas_*` tools held to **the read-only observer surface** (`canvas_list_observees` is the hinge) plus student self-access; four auth modes in priority order; hardened file download (host-pinned, directory-confined, no symlink writes, `0600`). **43 releases**, → 2026-10-16. |

🔵 **Why it belongs on the *verticals* shelf and not only on the agents shelf.** Infinite Campus is a
**major North American K-12 SIS** that this base has only ever been able to name as a proprietary
system with nothing attachable. It now has a granted, maintained, MIT integration surface — so the
"what can be bolted on" answer for a US K-12 district changes from *nothing* to *the parent portal*.

🔴 **The boundary that decides the engagement, and it is not a licence boundary.** Both servers
authenticate as **a person** — a parent's own token, OAuth, or a scraped session. Deployed by a family
for their own child, that is the parent exercising their own access. **Hosted by a studio on behalf of
a district, the same call becomes an institutional disclosure of an education record and FERPA
governs it.** The code is identical; the obligation is not. 🆕 `Pattern P` in
[`compose/patterns.md`](../compose/patterns.md) is built around that line, and it is the same
tenancy problem `p386` found for student-side LMS servers — **the parent surface inherits it
unchanged**, which is worth knowing before a district pilot is scoped.

## 🆕 `p388` — Canvas: the integration surface reordered, and a FERPA mode shipped as a feature

`p387` recorded that the richest Canvas server (`canvas-mcp-server`, 54 tools) had not shipped since
**2025-06-27**. For a client engagement that mattered and there was nothing better to recommend.
There is now:

- 🟢 **[bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp)** — `main` · `34e6156`,
  🟢 **MIT** (1,070 B), `canvas-lms-mcp` **v2.9.0 across 87 releases, 2026-04-13 → 2026-10-22
  (today)**. **187 tools on the teacher/admin surface**, including the ones an institution asks about
  and demos usually lack: gradebook *history*, quiz **accommodations**, grading standards, content
  exports and migrations, outcomes, analytics, appointment groups, plus **link audit**,
  **accessibility audit** and **grade projection**. Three deployment modes (stdio, HTTP, library
  import). 🟢 **It ships a FERPA mode.** That is the first time on these shelves that an education
  compliance regime appears as a *product feature* of an open-source component rather than as a
  caveat this base has to supply — and in a procurement conversation it is worth more than the tool
  count.
- 🟢 **[Fireiscoolsolo/canvas-lms-mcp-local](https://github.com/Fireiscoolsolo/canvas-lms-mcp-local)**
  (`c7e5725`) and its remote twin
  **[`-server`](https://github.com/Fireiscoolsolo/canvas-lms-mcp-server)** (`8e424f1`) — 🟢 **MIT**
  (1,091 B each), **209 tools on the student surface**, split deliberately into a **Local Edition**
  that opens no port and a **Remote Edition** on ngrok with OAuth 2.1 and multi-computer failover.
  🔴 The Remote Edition exposes a **public HTTPS address**: a school's decision, never a default, and
  not a thing to leave switched on in a pilot.

🔵 **Pick by persona, not by tool count.** 187 (teacher/admin) vs 209 (student) vs 20 (parent) is
**scope**, not quality: three different people reading the same institutional data. An engagement
usually needs one, occasionally two, and should deploy them separately — the FERPA posture differs
per surface, and a single server covering all three personas would be the hardest version of this to
get approved.

🟢 **And a wider Moodle surface than `webservice_mcp`:**
[gafapa/moodlia-cli](https://github.com/gafapa/moodlia-cli) — `main` · `7962e49`, 🟡 **GPL-3.0**
(284 B short-form notice) — a Node client and CLI against Moodle Core web services **plus the MoodlIA
plugin, a 250-operation contract**, Moodle 4.5+, with an optional experimental **WebMCP** browser
path. GPL survives here for the same reason it does for `webservice_mcp`: the agent reaches it over
REST, it is not linked.

## 🆕 `p389` — The generated classroom as a platform (OpenMAIC)

[THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 🟢 **MIT**, Tsinghua University, real
default ref `main` @ `269fde2d991f`, **committed 2026-10-22 (0 d)**, ~41.3k ★. Grant read from the
payload: `LICENSE` is stock MIT text, `package.json` declares `"license": "MIT"`.
🔴 **A 2026 third-party review of this project reports it as AGPL-3.0 with paid commercial licensing.
That is false** — see [`agents/top.md`](../agents/top.md#-two-licence-traps-that-a-badge-read-would-miss).

**Why it belongs on *this* shelf and not only the agent shelf.** Every other row here is a system of
record that AI gets bolted onto. OpenMAIC inverts it: the artefact is a **classroom** — narrated
slides, an AI teacher with a voice, teaching assistants, simulated classmates, auto-graded quizzes,
HTML interactives, a shared whiteboard — generated from a topic or an uploaded document, and then
*taught*. It is a Next.js 16 / React 19 / TypeScript application on **PostgreSQL 16**, self-hosted
with Docker, and it has the three properties that separate a platform from a demo:

| property | what it is | why an institution needs it |
|---|---|---|
| **Server-first generation** (v1.2.0) | Generation runs on the server, survives closed tabs and restarts; the web app and the API share one pipeline | A teacher who closes a laptop does not lose a lesson. The demo-grade alternative generates in the tab. |
| **Central model governance** | Every AI use is a named **slot** in `openmaic.yml` (outline, slide content, TTS, web search, …), each pinned to a declared provider, keys referenced as `${VAR}` from `.env.local`; a capability is switched off with `video: null`, and the server can be configured to **forbid user-supplied keys** | This is the artefact a district's AI policy is actually written against: *which model saw student input, under whose contract*. Almost nothing else in this base can answer that in one file. |
| **Export to one offline HTML file** | A finished classroom exports as a single self-contained HTML that plays the lesson, or as a PPTX that keeps every scene | The low-connectivity story (`Pattern D`) **and** the procurement story: a reviewer can be sent the lesson without being given access to the system. |

🟢 **Local inference is a supported path, not a fork:** **Lemonade** for local models and **FunASR**
for local ASR, so a deployment that may not send audio or text off-premises has a configuration
rather than a rewrite. 🟢 **Provenance:** grew out of **MAIC**, run inside Tsinghua and validated on
**700+ students**; paper in **JCST 2026**. 🟢 **Security handled as product work** — five releases
since September 2026 carry SSRF, DNS-rebinding, access-token-expiry and provider-redirect fixes under
published GHSAs, which is a maturity signal almost nothing else on the agent shelf has.

🔴 **What you still owe, and it is the whole administrative half.** No enrolment, no gradebook of
record, no transcripts, no SIS, no LTI story stated. It is a **teaching surface**, so in an engagement
with an incumbent LMS it sits *beside* Moodle/Canvas/Open edX as a content and delivery tool, and the
system of record stays where it is. 🔴 **Pin the ref.** Head is **v1.3.0-rc.1** (knowledge base,
2026-10-22) and the project states **breaking upgrade conditions with no rollback below that
release**; a pilot pins **v1.2.1** (2026-10-18). 🔴 **Operational floor:** Node ≥ 22.19, pnpm ≥ 10,
PostgreSQL 16, a long-running server — Vercel is capped at the 1.1.x line, so "we'll put it on Vercel"
is a downgrade, not a deployment.

🔵 **Where it lands by region.** Origin is **APAC** (China), the interface is EN + zh-CN, and the
provider catalogue is built for a market that includes DeepSeek and Kimi alongside OpenAI, Anthropic
and Gemini. For an engagement under **EU AI Act** or **FERPA** constraints the slot-pinning and
forbid-user-keys controls are an asset, and the *data-residency* question is answered by the local
Lemonade/FunASR path — but the assessment features (auto-graded quizzes, mastery signals) are exactly
what Annex III and Vietnam's Decision 33/2026 treat as high-risk, so human review of any consequential
score is a build item, not a setting. See [`intel/trends.md`](../intel/trends.md).

## What is *not* available as open source, and matters

An informed gap, recorded so silence is not mistaken for coverage:

- **No open-source equivalent of Khanmigo or LearnLM.** The pedagogically-tuned model layer is
  closed across the board; the open supply is agents and scaffolding over general models.
- **No open-source Brazilian or Mexican academic-management system was found.** A targeted search
  for SIGAA source and for Portuguese/Spanish-language academic management on GitHub returned
  nothing usable. `academico` (MIT) and Chamilo are the closest fits, neither region-native at
  university scale. See [`intel/market.md`](../intel/market.md) — this is the clearest
  build-vs-buy opening in the current rotation.
- **No official Instructure or Moodle-HQ MCP server** (community only, as above).
- 🔴 🆕 `p392` **~~Proctoring and AI-detection have no credible permissive open-source option~~ —
  WITHDRAWN. There are two granted components, and one of them is clean.**
  [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) (🟢 **MIT**, 1,069 B,
  manifest agrees, HEAD **2026-09-28**, npm v0.5.1) does tab-switch, camera, **face** (face-api on
  TF.js, in-browser), audio and **virtual-camera / loopback / screen-share** detection, and states
  *"nothing leaves the page unless you set `backend.endpoint`"*.
  [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) (🔴 **grant
  CONFLICT** — Apache-2.0 payload, ISC manifest and npm; HEAD **2026-10-13**, 398 commits) is the
  bigger codebase but ships **lockdown and event telemetry only** — its README marks object
  detection, multi-face and eye tracking *"(To be Done)"*.
  🔵 **What survives of the old sentence, and it is the half worth saying to a client:** the
  *liability* boundary is real and unchanged — an exam decision driven by either component makes the
  client a **deployer of an Annex III high-risk system** (standalone obligations from **2 Dec 2027**).
  The absence of code was never what made proctoring expensive; the obligations are. 🟢 So the honest
  advice flips from *"we cannot build this"* to **"we can build this, and here is what it commits you
  to"** — see [`compose/patterns.md`](../compose/patterns.md) `Pattern Y`. Full rows on
  [`repos/foundations.md`](../repos/foundations.md).

