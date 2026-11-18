---
industry: education
region: Global
updated: 2026-11-18
---

# Vertical platforms — education

**Pass `p883`, 2026-11-17** (thirteenth pass of the day). **`p883` adds a platform class this file
has never held: a permissively licensed, institutionally deployed AI DISTRIBUTION — not an LMS with
AI bolted on, and not an agent, but a desktop agent runtime packaged as a school product.**

- 🟢 **[`ECNU/EduWork`](https://github.com/ECNU/EduWork) — 376 ★, `MulanPSL-2.0` (bytes verified),
  pushed 2026-11-17.** East China Normal University's education distribution of **DeepSeek
  Harness**. It ships institutional OIDC login and model access (LiteLLM OAuth), a knowledge studio
  over local materials, and a maintained education plugin set, for Windows and macOS. Its sibling
  **[`ECNU/EduWork-ECNU`](https://github.com/ECNU/EduWork-ECNU)** (29 ★) is the university's own
  branded deployment — the configure-and-brand step, already done once, in public.
- 🟡 **Why it belongs on THIS shelf rather than on `agents/top.md` alone.** The copyleft problem
  `p882` measured here — 38.2% copyleft, 50.9% permissive — exists because the platforms
  institutions actually run (Moodle GPL-3.0, Open edX AGPL-3.0, OpenEduCat LGPL-3.0) predate the
  permissive era. **EduWork is the first institution-grade education platform on this shelf whose
  whole stack is permissive**, runtime included. It does not replace an LMS; it sits beside one.
- 🟡 **`MulanPSL-2.0` is a new licence family here.** OSI-approved and permissive with an explicit
  patent grant, so build-safe — but bilingual with the **Chinese text governing** and framed under
  **Chinese law**. 🟢 Usable. 🟡 Name it in the client's legal review rather than passing it
  silently as "Apache-like".

**Previous pass (`p882`), retained:** **Pass `p882`, 2026-11-17** (twelfth pass of the day). **`p882` measured what this file has always
asserted: the copyleft problem in education lives HERE, and almost nowhere else.**

- 🔴 **This shelf is 38.2% copyleft and only 50.9% permissive** — against 6.6% copyleft and 82.9%
  permissive on `repos/foundations.md`. Every address on all three sell shelves was re-measured
  this pass ([`record`](../evidence/sell-shelf-measure.2026-11-17-p882.tsv)); the per-layer table is
  on `repos/foundations.md` and the consequence for an engagement is below.
- 🟢 **The channel:** `api.github.com/search/repositories` is `200` this pass while
  `api.github.com/repos/<slug>` is `403` — `p881` recorded the metadata channel as flatly down, so
  this is the first full re-measure of this shelf since `p879`
  ([`record`](../evidence/channel-state.2026-11-17-p882.tsv)).
- 🔴 **A `p881` repair on this shelf is reversed:** canonical is `sudosylabs/proctor`, lower-case.
  The three addresses are re-cased; the reasoning is kept under the `p881` section below rather than
  edited away.
- 🟢 **This shelf can be counted again:** **55 rows across 12 tables**, measured (`881-G3`; 🆕 `p883` adds `ECNU/EduWork`; 🆕 `p884` adds `tsugiproject/tsugi`).

**Previous pass (`p879`), retained:** **Pass `p879`, 2026-11-17** (ninth pass of the day). **`p879` adds the layer this file has
described 879 passes of systems on top of and never named: identity.**

- 🟢 **`apereo/cas` — Apache-2.0, 11,402 ★, pushed 2026-11-17.** Single sign-on for higher
  education, governed by the Apereo Foundation. 🔵 The EU AI Act's Art. 50 disclosure and Art. 4
  literacy duties, and every US state consent rule in **P15**, are recorded **against an
  identity** — so the SSO layer is where AI governance becomes auditable.
- 🟢 **Permissive mobile clients for copyleft servers:** `moodlehq/moodleapp` (Apache-2.0, 1,006 ★,
  **2,491 forks**), Open edX Android/iOS, `oppia-android`. A white-labelled app is **not** a
  copyleft deliverable.
- 🟢 **Corrected:** Open edX's address here was stale — `openedx/openedx-platform`, 8,240 ★.

**Previous pass (`p878`), retained:** **Pass `p878`, 2026-11-17** (eighth pass of the day). **`p878` adds the first permissively
licensed assessment platform this file has ever carried, a second permissive auto-grader, and
Brazil's incumbent SIS — all three found by a discovery channel no pass had used.**
`api.github.com/search/repositories` takes full discovery queries, not just `repo:` lookups:
44 English legs returned 546 measured repositories, and 12 legs in **Spanish and Portuguese**,
never run before, returned 304 more.

🔵 **The structural point for this file.** Every LMS row above `p878` is copyleft except OpenOLAT,
Kolibri, Oppia and Sakai — and none of those four does assessment at scale. **`ls1intum/Artemis` is
MIT and does programming auto-grading, online exams with plagiarism checks, competencies and
learning analytics.** That is a genuinely new option in the build-versus-buy conversation, not an
incremental row.

🟢 **`OpenOLAT`'s asterisk can come off.** `p877` flagged that GitHub reports `NOASSERTION` while
the bytes read Apache-2.0; `p878` independently byte-read `master/LICENSE` and it is a
byte-identical **Apache License 2.0** preamble. Same for **GegoK12** (**MIT**), whose classifier
abstention is now explained exactly: its `LICENSE` carries `<!-- SPDX-License-Identifier: MIT -->`
as an HTML comment on line 3. 🔵 **Keep briefing clients that the automated check returns
`NOASSERTION` — that part of `p877`'s advice is unchanged and still the practical risk.**

🔴 **And the warning that belongs with this file's flagship row:** **`overhangio/tutor`**
(**AGPL-3.0**, byte-read, 1,132 ★, pushed 2026-11-17) is the Docker-based Open edX distribution and
in practice *the* way Open edX gets deployed. **An Open edX engagement is AGPL at the platform
layer and AGPL at the operations layer.** 🟢 **Corrected by `p879`:** the platform *can* be measured — the address this KB was using was
stale. **https://github.com/openedx/openedx-platform — 8,240 ★, AGPL-3.0, pushed 2026-11-17.**

**Previous pass (`p877`), retained:** Pass `p877`, 2026-11-17** (seventh pass of the day). **`p877` adds the two platforms this file
most needed and did not have: a permissively licensed SIS, and the largest permissively licensed
offline education server in the index.**

> **🟢 The permissive shortlist gains its first STUDENT INFORMATION SYSTEM.**
> [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) is **MIT** at the bytes (1,150 B,
> `sha256₁₂ b8694396d7dc`). Until this pass every SIS in this file was copyleft — Gibbon GPL-3.0,
> RosarioSIS GPL-2.0, openSIS with no licence file at all. **This is the only row in this file a
> studio can fork, rebrand and ship inside a proprietary deliverable.**
> 🟡 It is also **small** (57★, HEAD five months old): the gap closes on licence, not maturity.

> **🔴 [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
> — Apache-2.0, 43,849★, 4,526 forks, 813 commits in 12 months — was in NO curated file in this
> KB before `p877`**, despite being the second-largest education-native repository the KB knows of.
> The *Offline & low-connectivity delivery* section below described that category as "first-class"
> while listing only GPL-3.0 and LGPL options. **The permissive leader of the category was missing
> from the file that calls it first-class.**

**Previous pass note (`p876`)** (sixth pass of the day). `p876` adds the **learning-analytics layer**
to this file, which has until now described platforms that *generate* learner telemetry without
naming anywhere to *put* it. Two permissive, maintained Learning Record Stores are verified below
and in `repos/foundations.md`.

> 🟢 **The permissive shortlist gets a new row and it is a strategically useful one.**
> **`openfun/ralph`** (MIT) comes from **France Université Numérique**, the consortium that
> operates France's national Open edX platform. It is the rare case in this vertical where a
> *public-sector European* project ships under a **permissive** licence — every other EMEA
> platform of comparable provenance in this file is GPL or AGPL. For an EU public-sector bid where
> sovereignty and provenance are scored, that combination is worth more than its 52 stars suggest.

**Previous pass note (`p875`)** (fifth pass of the day). `p875` measured **78 addresses** first-hand
for stars, SPDX licence and last-push date — the channel four passes called impossible (see
`repos/trending.md`). It did not re-verify `p874`'s licence bytes; it independently **corroborated
every one of them through SPDX**, including `p874`'s correction of `SriSatyaLokesh/pariksha` to
AGPL-3.0. Two sections change: **proctoring is re-framed from a licence problem to an adoption
problem**, and the copyleft thesis below is now **quantified**.

> **🔴 The proctoring category has 19 stars across six repositories, and four of them have zero.**
> Three passes argued about the *licence* of open-source proctoring code. The licence was never the
> binding constraint. **There is no open-source proctoring platform to build on in this vertical —
> permissive or copyleft — and the correct advice to a client asking for one is to buy, or to
> treat it as bespoke from zero.** Full table in the proctoring section below.

> **🟡 `OpenOlat` returns `NOASSERTION` from GitHub's SPDX detector** while its licence bytes read
> Apache-2.0. The byte-read is authoritative — a modified header almost certainly defeats
> auto-detection — but **OpenOlat is the load-bearing "only permissive full LMS" claim in this
> file, and a client's counsel will run the automated check and get `NOASSERTION`.** Brief them
> before they ask. `BerriAI/litellm` shows the same pattern. 🔴 **`CaviraOSS/PageLM` DOES NOT, and
> `p877` corrects this sentence:** PageLM's `NOASSERTION` is **not** a detector artefact — its bytes
> are a bespoke non-commercial licence that **prohibits redistribution**. Grouping it with OpenOlat
> and litellm as "same pattern, byte-read will clear it" is the exact inference `intel/trends.md`
> **T14** warns against: the token is identical, the grants are opposite.
> 🔵 **OpenOlat is nonetheless T14's fourth confirmed case** — and the most commercially important,
> since it carries this file's "only permissive full LMS" claim;
> `OS4ED/openSIS-Classic` returns `NONE` — **no detectable licence at all**, treat as all rights
> reserved until proven otherwise.

**Previous pass note (`p874`):** rewrote the proctoring section against seven byte-read licences
and corrected the category heading. Real, deployed systems that can be customised with AI on top —
the education equivalents of Odoo for ERP or OpenMRS for healthcare. Existence and licence bytes
verified via `git ls-remote` + `raw.githubusercontent.com` on the resolved default branch.

> **The single most important strategic fact in this file:** the education platform layer is
> **overwhelmingly copyleft**. Of the 20 verified platforms below, only **5** are permissive
> (Apache-2.0 / MIT / BSD). The brief asks for MIT / Apache / BSD because those are what
> Globant can build on — in this vertical that constraint eliminates Moodle, Canvas, Open edX,
> ILIAS, Chamilo and both SIS options. The workable pattern is therefore **not** forking a
> platform: it is building permissive AI services that attach over **LTI 1.3** and **xAPI**.
> That integration seam is the actual product surface in education.
>
> **🟢 `p875` quantifies this.** Measured by installed attention, the permissive column is real but
> consistently smaller: `oppia` 6,997 (Apache-2.0), `sakai` 1,238 (ECL-2.0), `kolibri` 1,177 (MIT),
> `opencast` 513 (ECL-2.0), `OpenOlat` 452 (Apache-2.0*) — against `moodle` 7,618 (GPL-3.0),
> `canvas-lms` 6,918 (AGPL-3.0), `frappe/lms` 3,428 (AGPL-3.0), `chamilo` 1,025 (GPL-3.0),
> `ILIAS` 512 (GPL-3.0). **No permissive LMS has the installed base of Moodle or Canvas.** The
> conclusion survives the measurement and is strengthened by it: do not fork a platform to chase a
> licence — **attach over LTI 1.3 and xAPI, where the permissive layer is yours to write.**

## 🆕 `p882` · 2026-11-17 — what changed on this shelf

### 🔴 38.2% copyleft, and that is this shelf's defining property rather than a defect

Measured over all 55 resolvable addresses on this shelf:

| Posture | SPDX ids | Rows | Share |
|---|---|---:|---:|
| Permissive | Apache-2.0 14 · MIT 11 · ECL-2.0 2 · BSD-3-Clause 1 | 28 | 50.9% |
| **Copyleft** | GPL-3.0 10 · AGPL-3.0 7 · GPL-2.0 3 · LGPL-3.0 1 | **21** | **38.2%** |
| No resolvable grant | NOASSERTION 5 · none 1 | 6 | 10.9% |

🔵 **The comparison is the finding, not the number.** The substrate shelf is **6.6%** copyleft; this
one is **38.2%** — a sixfold concentration in exactly the layer a client already runs in production
and will not be replacing. 🟢 **That makes the licence question an architecture question with one
answer:** the platform stays where it is and keeps its licence; the work a studio delivers attaches
to it over **LTI 1.3**, **xAPI** and **OneRoster**, and lives in the permissive layer where it is
the client's to license as they choose. Every pattern in `compose/patterns.md` that survived
contact with a real engagement has this shape, and `P19`/`P20` are the explicit recipes.

🔴 **The one thing not to do, stated once:** do not fork an AGPL-3.0 platform to add an agent to it.
The obligation attaches to the modified work served over a network, which is what a hosted LMS is.
Attaching leaves the obligation where it already was.

### 🟢 The permissive escape hatches this shelf already holds, now with first-party numbers

| Address | Licence | ★ | Pushed | Role in an engagement |
|---|---|---:|---|---|
| 🟢 https://github.com/ECNU/EduWork | 🟢 **MulanPSL-2.0** (byte-read, 9,233 B) | 376 | 2026-11-17 | **NEW in `p883`.** A permissive education *distribution* of an MIT agent runtime (DeepSeek Harness) — the first platform on this shelf whose entire stack, runtime included, carries a permissive grant. Institutional OIDC + LiteLLM OAuth out of the box. |
| https://github.com/apereo/cas | **Apache-2.0** | 11,402 | 2026-11-17 | the identity layer under higher education — permissive, and where AI-governance consent becomes auditable |
| https://github.com/moodlehq/moodleapp | **Apache-2.0** | 1,006 | 2026-11-17 | a white-labelled mobile client for a GPL-3.0 server: a permissive deliverable against a copyleft platform |
| https://github.com/ls1intum/Artemis | **MIT** | 832 | 2026-11-17 | assessment at scale without a copyleft core; still the only one on this shelf |
| https://github.com/learningequality/kolibri | **MIT** | 1,178 | 2026-11-17 | the offline platform, MIT end to end with its content supply chain |

🔵 **Four rows, and they are the whole argument.** The permissive half of this shelf is not a thin
version of the copyleft half — it is **identity, assessment, mobile delivery and offline**, which is
precisely the set of places a studio adds value without touching the incumbent's core.

🔴 **Liveness, measured separately from licence:** three addresses on this shelf have not been pushed
in over twelve months — `LearningLocker/learninglocker` (2024-05-30, GPL-3.0, 587 ★),
`kamlendras/OpenProctor` (2025-05-28) and `ganesh-786/Proctor` (2025-06-09). The last two are the
proctoring category `p875` already called *"real demand, and effectively no supply"*; the first is
the xAPI LRS, and it is load-bearing. See `repos/foundations.md`, this pass, for the full list.

## 🆕 `p881` · 2026-11-17 — what changed on this shelf

🟢 **Six slug corrections on this shelf — the two `880-G4` mismatches in the whole base were both here.**
`OpenOlat/OpenOlat` → `OpenOLAT/OpenOLAT` (3) and `sudosylabs/proctor` → `sudosylabs/Proctor` (3). The
base-wide count is now **`0`** ([`record`](../evidence/case-oracle-postfix.2026-11-17-p881.tsv)).
>
> 🔴 **`p882` REVERSED the second of those two.** Canonical is `sudosylabs/proctor`, lower-case —
> first-party `full_name` from `search/repositories`, a channel `p881` recorded as wholly down. The
> `OpenOLAT` half is confirmed correct. The three addresses on this shelf are re-cased back; the
> sentence above is kept rather than quietly edited, because what it got wrong is the lesson.

🟢 **This shelf was RIGHT and the register was WRONG about `h5p/h5p-php-library`, and `p881` byte-read it
to settle the matter.** `gate-shelf-consistency` reported a live disagreement — Apache-2.0 at
`intel/open-gaps.md:11690` against **GPL-3.0** in this shelf's row. The bytes:
`master/LICENSE.txt`, **35,146 B**, `sha256₁₂ c53a65c2fd56`, opening *"GNU GENERAL PUBLIC LICENSE"* and
containing *"Version 3, 29 June 2007"*. 🟢 **GPL-3.0 confirmed; the client-facing cell needed no change.**

🔵 **And the gate that found it has a scope defect worth knowing about:** `intel/open-gaps.md`'s live
region is lines **7–116** (measured: first `##` at 7, second at 117), yet the gate graded line **11690**
as `LIVE`. It reads the whole 40,000-line register as live. Filed in `p881`'s triage as an instrument
defect.

## 🆕 `p880` · 2026-11-17 — what changed on this shelf

🟢 **Two MIT EMEA platforms** from France Université Numérique, byte-read this pass:
**`openfun/richie`** (`318★`, education-portal CMS) and **`openfun/marsha`** (`152★`, LTI video
LCMS) — the portal and media layers clients ask for and that Moodle/Open edX do not provide.
🔴 **Two corrections owed:** the canonical slug is **`OpenOLAT/OpenOLAT`** (five shelves carry
`OpenOLAT/OpenOLAT`; Apache-2.0 re-confirmed on the canonical address), and both high-star education
ERPs remain unusable — `openeducat_erp` is **LGPL**, `frappe/education`'s whole grant is a **19-byte**
`License: GNU GPL V3` declaration.

## The platforms — 55 rows

🟢 **Derived, not asserted.** `53` distinct platforms across the **11** tables below. The raw row
count is `57`: four addresses — `apereo/cas`, `moodlehq/moodleapp`, `ls1intum/Artemis` and
`learningequality/kolibri` — appear both in their layer table and in the `p882` permissive-escape-
hatch table, and are counted **once** (`p813`'s distinct-subject rule). `ingest/derive-counts.py`
grades this heading against the rows on every pass.

🔴 **Read the licence posture before the list:** this shelf is **38.2% copyleft** against 6.6% on
`repos/foundations.md`. That is a property of the layer, not of the curation — see the `p882`
section above.

## Learning management systems

| Platform | Repo | Licence | Branch | Position & AI surface |
|---|---|---|---|---|
| 🟢 **EduWork** (ECNU) | https://github.com/ECNU/EduWork | **MulanPSL-2.0** (`LICENSE`, 9,233 B) | `main` | **NEW in `p883`. An AI-native education distribution rather than an LMS.** Built on [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (MIT, DSH `0.2.1-rc.3`); the AI surface IS the product, not a plugin. Pre-installed: institutional gateway login and model discovery (browser OIDC, LiteLLM OAuth, experimental `oidc-llm`), knowledge studio over local files, agent tools/browser/file capabilities inherited from upstream. Windows x64 · macOS arm64/x64. **Customisation path: write DSH plugins and ship a branded build — `EduWork-ECNU` is that path executed by its own authors.** 🟡 Chinese-language-first; English README present, UI localisation is work. |
| **Moodle** | https://github.com/moodle/moodle | GPL-3.0 (`COPYING.txt`) | `main` | The most widely deployed LMS worldwide and dominant in EMEA and LATAM public education. Has a first-party AI subsystem with pluggable providers, so **AI can be added as a plugin without forking** — the cleanest copyleft-safe integration path in this file. |
| **Open edX** | https://github.com/openedx/openedx-platform 🟢 (`p879`: renamed; `openedx/edx-platform` is the stale slug) | AGPL-3.0 | `master` | Originated at MIT and Harvard, now stewarded by the non-profit Axim Collaborative. The standard choice for large-scale MOOC and national-platform deployments. Note: the *platform* is AGPL-3.0 — the Apache-2.0 figure that circulates in listicles refers to satellite repos such as `openedx-aspects`, not to `edx-platform`. Verified this run. |
| **Canvas LMS** | https://github.com/instructure/canvas-lms | AGPL-3.0 | `master` | Dominant in North American higher education. The open-source edition carries core LMS function; some commercial features are withheld. AGPL. |
| **ILIAS** | https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | `release_11` | Strong in German-speaking EMEA, including public-sector and military training. Note the default branch is `release_11`, not `main`. |
| **Chamilo** | https://github.com/chamilo/chamilo-lms | GPL-3.0 | `master` | Significant installed base in **LATAM** and francophone Africa; lighter to operate than Moodle, which is why ministries with thin IT capacity pick it. |
| **Sakai** | https://github.com/sakaiproject/sakai | **ECL-2.0** | `master` | Apereo Foundation, research-university focus. Educational Community License 2.0 is an Apache-2.0 derivative — **more permissive than the rest of this table**, a genuinely under-used fact. |
| **OpenOLAT** | https://github.com/OpenOLAT/OpenOLAT | **Apache-2.0** | `master` | Swiss-origin, used across EMEA higher education. **The only major full LMS here under a clean permissive licence** — the obvious base if a client needs a customised LMS that Globant can extend without copyleft obligations. |
| **Frappe LMS** | https://github.com/frappe/lms | **AGPL-3.0** | `develop` | Modern, lightweight LMS on the Frappe framework. **Correction recorded this pass:** multiple 2026 listicles state MIT; the licence bytes at `license.txt` are **AGPL-3.0**. |
| **Kolibri** | https://github.com/learningequality/kolibri | **MIT** | `develop` | Learning Equality. Purpose-built for **offline-first, low-connectivity and low-resource deployments** — the platform of record for rural LATAM, Sub-Saharan Africa and South Asia programmes. MIT-licensed. For any equity-of-access or ministry-of-education mandate, this is the starting point, not Moodle. |
| **Artemis** 🟢 **new `p878`** | https://github.com/ls1intum/Artemis | 🟢 **MIT** — byte-read on `main` | **`develop`** | **Technical University of Munich (EMEA-origin). The only permissively licensed assessment platform in this file, and the reason this pass matters.** 832 ★, created 2016-09-29, pushed on the day of measurement. Interactive exercises (programming, modelling, text, quiz, file-upload) as first-class objects with version control, CI and static code analysis; **online exams with per-student exercise variants, test runs, plagiarism checks and structured student reviews**; competencies, learning paths and learning analytics; AI as **optional, configuration-gated** microservices (Iris / Athena / Hyperion) with *"instructors and tutors stay responsible for assessment decisions"* stated in the README. Java/Spring, self-hosted, horizontally scalable, with a maintainer-published **Ansible collection** and native iOS/Android clients. OpenSSF Scorecard + OpenSSF Best Practices (project 14163), Sonar and Codacy gates. 🟡 **Fit caveat: it is built around *university* course structures** — a K-12 or corporate-training engagement will fight it, and Java/Spring is a heavier operational commitment than PHP or Python. |
| **Autolab** 🟢 **new `p878`** | https://github.com/autolab/Autolab | 🟢 **Apache-2.0** — byte-read `master/LICENSE` | `master` | **Carnegie Mellon (North America-origin).** 808 ★, created 2014-10-25, pushed 2026-11-11. Course-management service built around **auto-graded programming assignments** — narrower than Artemis and lighter to run. Apache-2.0 carries an **explicit patent grant** that Artemis's MIT does not, which occasionally decides a public-sector or enterprise procurement. |
| **i-Educar** 🟢 **new `p878`** | https://github.com/portabilis/i-educar | 🔴 **GPL-2.0** — byte-read on `master` | 🔴 **`2.12`** | **LATAM-origin (Brazil) — the incumbent free-software school-management system in Brazilian municipal education**, *"o maior software livre educacional do Brasil"*. 726 ★, created 2013-01-31, pushed 2026-11-13; tagged releases, GitHub Actions CI, modular packages, documented upgrade path. Companion **`portabilis/i-diario`** (🔴 **AGPL-3.0** by byte-read — GitHub reports `NOASSERTION`, per **T14**; 117 ★, default branch 🔴 **`1.6`**) is the electronic class diary. 🔴 **Both projects default to a *version* branch, not `main` or `master`** — a plain `git clone` lands you on `2.12` / `1.6`, and a pass that assumes `main` will report them as broken. 🔵 **Copyleft, so it is an integration target rather than a base** — build the AI layer as a separate service and the boundary holds, exactly as this file prescribes for Moodle. 🔴 **Found only because `p878` searched in Portuguese; eight earlier passes concluded LATAM had no supply.** |

## Courseware, content & assessment

| Platform | Repo | Licence | Branch | Position & AI surface |
|---|---|---|---|---|
| **Oppia** | https://github.com/oppia/oppia | **Apache-2.0** | `develop` | Interactive lesson platform built around structured "explorations" with misconception-specific feedback. Apache-2.0, and its explicit misconception model is unusually well matched to LLM-generated remediation. |
| **Perseus (Khan Academy)** | https://github.com/Khan/perseus | **MIT** | `main` | Khan Academy's exercise and question rendering framework. MIT — directly embeddable, and the fastest route to a credible practice-item UI. |
| **H5P** | https://github.com/h5p/h5p-php-library | GPL-3.0 | `master` | The interactive-content standard embedded inside Moodle, Canvas and Open edX. Content-type authoring for interactive video, branching scenarios, quizzes. |
| **Anki** | https://github.com/ankitects/anki | AGPL-3.0 | `main` | The dominant spaced-repetition application. Relevant as an **export target**: DeepTutor already exports to it, so a Globant build can meet learners in the tool they use. Pair with MIT-licensed `fsrs4anki` for the scheduler. |

## Student information, library & repository systems

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **Gibbon** | https://github.com/GibbonEdu/core | GPL-3.0 | `v31.0.00` | School management / SIS for K-12. Note: default branch is a version tag, not `main`. |
| **GegoK12** 🟢 **new `p877`** | https://github.com/Gego-K12/gegok12 | 🟢 **MIT** — byte-read, 1,150 B, `sha256₁₂ b8694396d7dc` | `main` | 🟢 **The first and only permissive SIS in this KB — closes a gap open since `p872`.** Full-featured school management system in **Laravel/PHP**, **API-first** (`api.md` in-tree), `Dockerfile` + `docker-compose.yml`, `lang/` localisation, plus separate Android **parent** and **teacher** apps. 113 commits in 12 months. 🟡 **57★ and HEAD `2026-06-25`** — propose it as a base you will own and extend, not a community you are joining. 🔴 **GitHub reports `NOASSERTION`** because line 3 of its `LICENSE` is `<!-- SPDX-License-Identifier: MIT -->`; the bytes are stock MIT. Do not let a licence-API readout disqualify it. |
| **openSIS Classic** | https://github.com/OS4ED/openSIS-Classic | **GPL per README; no licence file** | `master` | Student information system. **Licence flag:** there is no `LICENSE`, `COPYING` or `license.txt` on the default branch — the GPL claim exists only in prose in the README. Treat the grant as unconfirmed until clarified with OS4ED. |
| **RosarioSIS** | https://github.com/francoisjacquet/rosariosis | **GPL-2.0** | **`mobile`** | **New in `p873`.** Mature PHP/PostgreSQL student information system, used in production by schools, academies and colleges; latest tags `v9.3`, `v9.3.1`, `v9.3.2`. **The default branch is `mobile`** — a feature name, not `main` or `master`. Nothing about the address hints at it and no heuristic would guess it: a `raw.githubusercontent.com` path built on an assumed `main` 404s, which would have been published as "no licence file" and then as "no grant". Resolve with `git ls-remote --symref` first, always. The **third** verified open-source SIS, and the **third** that is copyleft. |
| **Koha** | https://github.com/Koha-Community/Koha | GPL-3.0 | `main` | The mature open-source integrated library system; very large installed base in school and university libraries worldwide. |
| **DSpace** | https://github.com/DSpace/DSpace | **BSD** | `main` | Institutional repository for theses, datasets and scholarly output. **Permissive** — a strong base for AI-assisted discovery and metadata enrichment over a university's own corpus. |
| **Open Journal Systems** | https://github.com/pkp/ojs | GPL-3.0 | `main` | PKP's scholarly publishing platform; heavily used by LATAM and Global South universities for their own journals. |

## Classroom delivery & lecture capture

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **BigBlueButton** | https://github.com/bigbluebutton/bigbluebutton | LGPL | `v4.0.x-develop` | Virtual classroom built for teaching rather than for meetings (whiteboard, breakout rooms, polling); integrates with Moodle and Canvas. LGPL — linking is permitted, which makes it friendlier than GPL for an attached service. |
| **Opencast** | https://github.com/opencast/opencast | **ECL-2.0** | `develop` | University lecture capture and video management. ECL-2.0 (Apache-derived, permissive). The natural source of the lecture-video corpus a tutoring agent should be grounded in. |
| **Agora Flat** 🟢 **new `p878`** | https://github.com/netless-io/flat | 🟢 **MIT** — byte-read | `main` | Online-classroom client for Web, Windows and macOS. 6,443 ★, pushed 2026-11-10. **Permissive where BigBlueButton is LGPL** — the option when the classroom client must ship inside a proprietary product. |
| **OpenVidu** 🟢 **new `p878`** | https://github.com/OpenVidu/openvidu | 🟢 **Apache-2.0** | `master` | Self-hosted real-time video/audio platform. 2,146 ★, pushed 2026-11-17. The permissive media substrate if you are assembling classroom delivery rather than adopting a platform. |
| **CTFd** 🟢 **new `p878`** | https://github.com/CTFd/CTFd | 🟢 **Apache-2.0** — byte-read | `master` | 6,916 ★, pushed 2026-11-10. The capture-the-flag platform: challenges, scoring, teams, progression. **The permissive substrate for security and technical skills training** where scoring and gamification come for free. |
| **OMRChecker** 🟢 **new `p878`** | https://github.com/Udayraj123/OMRChecker | 🟢 **MIT** — byte-read | `master` | 1,196 ★, pushed 2026-09-04. Grades **paper bubble-sheets from a phone camera or scanner**. 🔵 Not glamorous and strategically important: it is the on-ramp for assessment where exams are still on paper and bandwidth is scarce — see **P18**. |
| **teaching-open** 🟢 **new `p878`** | https://github.com/open-scratch/teaching-open | 🟢 **Apache-2.0** — byte-read | `master` | **APAC-origin (China).** 637 ★. Scratch / ScratchJr / Python teaching platform with courses, classes, assignments, permissions and community. Chinese-language UI — a localisation cost, not an absence. |

## Offline & low-connectivity delivery

Treated as a first-class category rather than a footnote, because it decides whether a
ministry programme reaches rural schools at all.

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **Kiwix** | https://github.com/kiwix/kiwix-tools | GPL-3.0 | `main` | Offline Wikipedia and educational-archive reader (ZIM format). Already an ingest source for DeepTutor, so an offline corpus can feed an offline tutor. |
| **Internet-in-a-Box** | https://github.com/iiab/iiab | LGPL | `master` | Turnkey offline learning server — bundles Kiwix, Moodle and content libraries onto low-cost hardware for schools without reliable connectivity. |
| **Project NOMAD** 🟢 **new `p877`** | https://github.com/Crosstalk-Solutions/project-nomad | **Apache-2.0** (10,778 B, byte-read) | `main` | 🟢 **The permissive leader of this category, and now the default starting point.** An offline-first knowledge and education server: Wikipedia, thousands of books, courses, maps and **optional local AI**, all from one box with no internet. **43,849★ / 4,526 forks / 813 commits in 12 months** — and on an appliance repository, forks read as deployments. Dockerised, with `collections/`, `admin/` and `install/` in-tree and semantic-release. **Apache-2.0 is the decisive fact against Kiwix (GPL-3.0) and Internet-in-a-Box (LGPL):** a ministry deliverable can be rebranded and redistributed without copyleft obligations on the surrounding work. |

**23 verified platforms.**

## Identity & single sign-on — the layer under every other row in this file, new in `p879`

🔴 **This file has described LMSs, SIS, proctoring, content and classroom delivery for 879 passes
and never once named how a user signs in.** Every institutional deployment in this KB assumes an
identity layer, and in higher education that layer has a dominant open-source implementation.

| Platform | Repo | Licence | ★ | Pushed | Notes |
|---|---|---|---:|---|---|
| **Apereo CAS** | https://github.com/apereo/cas | **Apache-2.0** (byte-read, `master/LICENSE`) | **11,402** | 2026-11-17 | Created 2011-09-09, 3,954 forks. Central Authentication Service: CAS protocol plus SAML2, OAuth2, OIDC and WS-Fed, MFA, delegated/social auth, attribute release and consent. Governed by the **Apereo Foundation**, the same non-profit behind Sakai — i.e. an institutional steward, not a vendor. |
| **phpCAS** | https://github.com/apereo/phpCAS | **Apache-2.0** (byte-read) | 802 | 2026-06-30 🔴 | The PHP client library — the usual way a Moodle estate attaches to CAS. **Five months since last push**; treat as mature-but-quiet and check before committing to it. |

🔵 **Why it belongs in a KB about AI.** Two of this file's live compliance clocks attach to a
*person*, not to a system: **EU AI Act Art. 50 disclosure** (who was told that they were talking to
an AI) and **Art. 4 AI-literacy** (who was trained), plus every US state consent and opt-out
requirement tracked in `compose/patterns.md` **P15**. 🟢 **Those obligations are recorded against
an identity, and in a university that identity comes from CAS.** An AI component bolted on beside
the SSO rather than behind it cannot produce the audit trail the regulation asks for.

🟡 **Attribute release is the privacy control, and it is configuration, not code.** CAS decides
which attributes each service receives. A tutoring agent registered as a CAS service can be given a
pseudonymous identifier and a course enrolment and **nothing else** — which is a cheaper and more
defensible data-minimisation story than anything implemented inside the agent.

## Mobile clients — permissive, and separable from their copyleft servers, new in `p879`

🟢 Measured in `p879`'s org census. Each of these is a **permissively licensed client for a
copyleft server**, so a white-labelled app for a client is not a copyleft obligation.

| App | Repo | Licence (byte-read) | ★ | Forks | Server it talks to |
|---|---|---|---:|---:|---|
| **Moodle App** | https://github.com/moodlehq/moodleapp | **Apache-2.0** (`main/package.json`) | 1,006 | **2,491** | Moodle (GPL-3.0) |
| **Open edX Android** | https://github.com/openedx/openedx-app-android | **Apache-2.0** (`LICENSE`) | 38 | — | Open edX (AGPL-3.0) |
| **Open edX iOS** | https://github.com/openedx/openedx-app-ios | **Apache-2.0** (SPDX) | 31 | — | Open edX (AGPL-3.0) |
| **Oppia Android** | https://github.com/oppia/oppia-android | **Apache-2.0** (`LICENSE`) | 422 | — | Oppia (Apache-2.0) — offline-capable |

🔵 **The 2,491 forks on `moodleapp` are the finding.** That is not a developer-interest number; it
is the count of people who have already done the thing a Globant engagement would propose —
**fork the official app, re-brand it, ship it to an institution's students.** The path is
well-trodden and the licence permits it.


## 🟢 EMEA platform layer the recount surfaced, and two slug/grant corrections — new in `p880`

### 🟢 France Université Numérique's two MIT platforms

🔵 **`p880`'s full-estate recount swept `openfun` — France Université Numérique, the operator of
`fun-mooc.fr` — to exhaustion for the first time: `100` source repositories, `52%` permissive.** Two
of them are *platforms* rather than components, both **MIT**, both pushed the day of this pass, and
neither was on this shelf. 🟢 **Licences byte-read this pass**
([`record`](../evidence/licence-byteread.2026-11-17-p880.tsv)).

| Platform | Repo | Licence (byte-read) | ★ | Pushed | What it is |
|---|---|---|---:|---|---|
| **Richie** | https://github.com/openfun/richie | **MIT** (`LICENSE`, `1,079 B`, `e4b2a3148135`) | **318** | 2026-11-17 | **A CMS for building education portals**, Django/DjangoCMS. The *catalogue and marketing* front end that sits in front of an LMS: programmes, courses, teachers, categories, search, multilingual by design. 🔵 **This is the piece clients ask for and Moodle/Open edX do not provide** — and unlike both of them it is **MIT**, so the deliverable can be the client's. |
| **Marsha** | https://github.com/openfun/marsha | **MIT** (`LICENSE`, `1,078 B`, `6dab88f38735`) | 152 | 2026-11-17 | **An LTI Learning Content Management System for video**, i.e. a video/media provider that mounts into any LTI-capable LMS. Upload, transcode, subtitle and serve media *without* putting it in the LMS and without a proprietary video vendor. |

🟢 **Why they matter together, and why EMEA:** Richie + Marsha + an incumbent LMS gives a **public-sector
EU buyer a portal and a media layer under a permissive grant**, attached by LTI rather than by a
fork. 🔵 Both are produced by a French public higher-education consortium, which is `T15` again —
the permissive supply in this vertical comes from public institutions, not startups. 🟡 **Placed
EMEA on the owner's jurisdiction** (France Université Numérique), consistent with the `p870`
commit-domain measurement that put `openfun` at `fun-mooc.fr` `41`/`50`.

### 🔴 Two corrections this pass owes the shelf

🔴 **1. The canonical slug is `OpenOLAT/OpenOLAT`, and this file publishes `OpenOLAT/OpenOLAT`.**
The search index returns `full_name = OpenOLAT/OpenOLAT` for either spelling, because GitHub
resolves owner and repository names case-insensitively and **serves correct licence bytes through
the redirect** — which is exactly why five shelves have carried the wrong case without anything
catching it. 🟢 **`p880` byte-read the canonical slug directly: `master/LICENSE`, `10,982 B`,
`6dbc5b605ed0`, `Apache License` — so `p878`'s Apache-2.0 finding is CONFIRMED on the canonical
address**, and the only defect is the case. 🔵 **This is `870-G5`'s case-sensitivity class in the
curated files**, and it is a presentation defect rather than a grant defect — but a client who
copies the slug into a procurement document should get the owner's own spelling.

🔴 **2. The two education ERP candidates remain unusable, re-measured and now corroborated on the
base's own hash.** 🟡 **`p880` set out to test whether either `NOASSERTION` was a false negative —
this base's standing rule is that `spdx_id` screens and bytes decide — and in both cases the bytes
confirm the existing verdict rather than overturn it:**

| Candidate | ★ | Byte-read this pass | Verdict |
|---|---:|---|---|
| https://github.com/openeducat/openeducat_erp | 913 | `19.0/LICENSE`, `8,241 B`, `528f84036800` | 🔴 **LGPL** — weak copyleft, linkable but not re-licensable. Default branch is **`19.0`**, not `main`/`master`. Matches the base's existing `771-H` row to the byte. |
| https://github.com/frappe/education | 712 | `develop/license.txt`, **`19 B`**, `1fcecf395312` | 🔴 **DECLARATION-ONLY.** The entire file is the string `License: GNU GPL V3`. It names a family, ships none of its text and points at no target. Taken at its word it is **GPL-3.0** and unusable for a proprietary derivative. Matches `771-G`. |

🔵 **So the education-ERP gap on this shelf is real and stays open:** the two highest-star open
education ERPs are weak-copyleft and declaration-only respectively, and **neither can be the base of
a Globant deliverable.** 🟢 **The usable ERP route remains what it was — an Odoo/ERPNext-class
general platform with an education layer built on top as the client's own code**, not an education
ERP distribution adopted wholesale.

## Tsugi — the LTI app framework, and the mechanism behind "attach, don't fork" — new in `p884`

🔵 **This file has prescribed *"attach, don't fork"* for hundreds of passes and never named the
framework that implements it.** `p884` found the gap from the other end: the University of Cape
Town's 50-repository teaching estate (`repos/foundations.md`, this pass) is **largely a set of Tsugi
apps**, and the pattern only makes sense once the framework is on this shelf.

🟢 **What it is.** Tsugi is an Apereo framework for building **LTI (Learning Tools Interoperability)
applications** — tools that mount *inside* whichever LMS an institution already runs. The AI feature
lives in your app, the LMS stays stock, the copyleft of the platform never reaches your code, and the
same app works across Moodle, Canvas, Sakai, Blackboard and Brightspace.

🔴 **This is the single cleanest answer to the problem `T7` and `T16` describe** — a vertical whose
major platforms are GPL/AGPL. An LTI app is a *process boundary that the LMS vendor already
supports*, rather than a boundary you have to argue for.

| Platform | Repo | Licence | ★ | Pushed | Notes |
|---|---|---|---:|---|---|
| **Tsugi** | https://github.com/tsugiproject/tsugi | **Apache-2.0** — byte-read `master/LICENSE`, **10,273 B**, `sha256₁₂ 73ba74dfaa52` | **377** | **2026-11-17** | Apereo's LTI app framework and management console. Created **2013-11-28**, **267 forks**, default branch `master`. 🟢 **Permissive, and it is the seam through which a studio ships function into a copyleft LMS without forking it.** 🔵 Worked, production examples in `repos/foundations.md` → `cilt-uct`: gradebook-to-PeopleSoft upload, student allocation, course-level dashboards, Sakai→Brightspace migration. |

### 🟢 Moodle's AI subsystem — what is actually in core, and the governance control that matters

🟡 **Recorded because a proposal will be asked about it and the vendor blogs disagree.** Moodle does
not ship a model; it ships a **pluggable AI subsystem** in core, present since **4.5**, with
providers as plugins (the documented provider surface is `moodledev.io/docs/5.1/apis/plugintypes/ai`).

- 🟢 **`5.1` adds DeepSeek as a core provider** alongside OpenAI and Azure AI.
- 🟢 **`5.1` adds per-course and per-activity on/off control for AI tools** — teacher-level, not just
  site-level. 🔵 **That is the commercially relevant part**: it is the granularity an institution needs
  to write a defensible AI-use policy, and it is the hook an EU AI Act deployer-side governance
  artefact can point at (`T11`).
- 🟡 **`5.3` is the next LTS** and its AI documentation was still marked in progress at the time of
  this pass; treat any 5.3 feature claim as unconfirmed.
- 🔴 **Moodle remains GPL-3.0.** The subsystem makes Moodle a *better integration target*; it does not
  change the licence calculus. Build the AI layer as a separate service — or, now, as a **Tsugi LTI
  app** per the row above.

🔴 **Declared, and it bounds the row above:** this KB has found **no MCP server published by Moodle
HQ**. The community option (`csmediapro/moodle-mcp-server`) is **AGPL-3.0** and carries no stars —
already in this KB's trending history and still not shelvable. Moodle HQ documents Web Services, not
MCP.

## Permissive-licence shortlist

For a Globant engagement that must avoid copyleft obligations, the verified permissive set is:

| Platform | Licence | Use it for |
|---|---|---|
| **OpenOLAT** | Apache-2.0 | A full LMS you can extend and commercialise |
| **Kolibri** | MIT | Offline-first / low-connectivity delivery |
| **Oppia** | Apache-2.0 | Interactive courseware with misconception handling |
| **Perseus** | MIT | Exercise and assessment item UI |
| **Sakai** | ECL-2.0 | Research-university LMS |
| **Opencast** | ECL-2.0 | Lecture capture and video corpus |
| **DSpace** | BSD | Institutional repository / scholarly corpus |
| **SQL LRS (`yetanalytics/lrsql`)** | Apache-2.0 | 🟢 **New in `p876`** — learner telemetry store (xAPI). The default for measurement |
| **Ralph (`openfun/ralph`)** | MIT | 🟢 **New in `p876`** — LRS + data pipeline, **Open edX-native**, EMEA public sector |
| **Artemis (`ls1intum/Artemis`)** | **MIT** | 🟢 **New in `p878` — assessment at scale, online exams, auto-grading, competencies. The first permissive assessment platform in this KB.** |
| **Autolab (`autolab/Autolab`)** | **Apache-2.0** | 🟢 **New in `p878`** — auto-graded programming coursework, with a patent grant |
| **Ares (`ls1intum/Ares`)** | **MIT** | 🟢 **New in `p878`** — secure sandboxed execution of untrusted student code (JUnit 5) |
| **Apollon (`ls1intum/Apollon`)** | **MIT** | 🟢 **New in `p878`** — UML modelling editor, standalone-capable |
| **Edutelligence (`ls1intum/edutelligence`)** | **MIT** | 🟢 **New in `p878`** — Iris/Athena/Hyperion AI microservices; **Athena produces feedback *suggestions* for a human assessor** |
| **Agora Flat (`netless-io/flat`)** | **MIT** | 🟢 **New in `p878`** — online-classroom client, permissive alternative to BigBlueButton |
| **CTFd** | **Apache-2.0** | 🟢 **New in `p878`** — security/technical skills training with scoring built in |
| **OMRChecker** | **MIT** | 🟢 **New in `p878`** — paper bubble-sheet grading from a phone camera |
| **Gestão Escolar (`Antonio-Neves/Gestao-Escolar`)** | **MIT** | 🟢 **New in `p878`** — the only permissive **LATAM-origin** SIS found; small, propose as a base to own |
| **Project NOMAD** | Apache-2.0 | 🟢 **New in `p877`** — offline-first education server, **43,849★**. The permissive answer for low-connectivity and ministry equity programmes |
| **GegoK12** | MIT | 🟢 **New in `p877`** — **the only permissive SIS.** Laravel, API-first. Small; adopt-and-own, not join |

### Learning analytics — the layer this file was missing

Every platform above emits learner events; none of them is where those events should be kept for
analysis. That is the Learning Record Store, and until `p876` this KB named only
`LearningLocker` — **GPL-3.0, default branch last moved 2021-11-16**.

| Platform | Licence | Stars | HEAD | Use it for |
|---|---|---:|---|---|
| https://github.com/yetanalytics/lrsql | **Apache-2.0** | 144 | 2026-11-14 | The production LRS. SQLite for a pilot; Postgres 14–18, MariaDB or MySQL at scale. OIDC, Docker, documented AWS deployment |
| https://github.com/openfun/ralph | **MIT** | 52 | 2026-10-12 | LRS **and** pipeline. Take it when the platform is **Open edX** (tracking-log→xAPI converters ship in-tree) or when European public-sector provenance is scored. Helm chart included |
| https://github.com/adlnet/ADL_LRS | Apache-2.0 | 335 | 2025-11-14 | The xAPI authors' reference implementation. 🟡 **0 commits in 12 months** — test against it, do not deploy it |
| https://github.com/davidpesce/moodle-logstore_xapi | GPL-3.0 | 83 | 2026-10-29 | The Moodle→LRS bridge. Copyleft, but it is a plugin **inside** GPL Moodle, so it concedes nothing new |
| https://github.com/LearningLocker/learninglocker | GPL-3.0 | 587 | **2021-11-16** | 🔴 **Do not start here.** Five years cold, 0 commits in 12 months. Listed so it is not re-imported from a listicle |

🔴 **The one thing you lose by leaving Learning Locker: dashboards.** It bundled a reporting UI;
`lrsql` and `ralph` do not. Pair them with **Aspects/Superset** (Apache-2.0) or **Grafana**
(AGPL-3.0 — fine self-hosted, a problem in a distributed product) and **price that work
explicitly**. See `compose/patterns.md` **P14**.

## Exam integrity & proctoring — 🔴 `p875`: real demand, and effectively NO supply

> **`p875` measured the whole category. Nineteen stars across six repositories. Four have zero.**
>
> | Repo | Stars | Licence (byte-read, SPDX-confirmed) | Last push |
> |---|---:|---|---|
> | `kamlendras/OpenProctor` | 16 | AGPL-3.0 | 2025-05-28 🔴 |
> | `amaanwarsi/Proctora` | **3** | MIT | 2026-04-07 |
> | `ganesh-786/Proctor` | **0** | MIT | 2025-06-09 🔴 |
> | `code-by-abrar/Online-Proctoring-system` | **0** | MIT | 2026-09-19 |
> | `sudosylabs/proctor` | **0** | AGPL-3.0 | 2026-11-16 |
> | `SriSatyaLokesh/pariksha` | **0** | AGPL-3.0 ✅ (`p874`'s correction, SPDX-confirmed) | 2026-11-07 |
>
> **The framing of the last three passes was wrong in a way that mattered.** `p871` said no
> permissive code existed; `p872` said two existed and both were copyleft; `p874` found three MIT
> repos and said the gap was maturity, not licence. `p874` was closest — and `p875`'s measurement
> shows the maturity gap is not a gap but an absence. **Not one of these projects has a user
> community.** A licence is a permission to build on something; none of these is a something.
>
> 🟡 **What to tell a client who asks for open-source proctoring:** there isn't any. The options
> are a commercial proctoring vendor integrated over LTI, or an accepted redesign of the
> assessment so that proctoring is not required — which, given `intel/trends.md` **T9** on
> scaffolding and `openedx/edx-proctoring` (69 stars, AGPL-3.0) being the only thing here with
> institutional provenance, is usually the better conversation. **Do not propose building one from
> these repositories.**

### Original `p874` category notes (licence bytes, retained)

🔴 **This heading said "no permissive supply" for two passes and that was wrong.** `p871` searched
and found nothing. `p872` found two projects, both AGPL-3.0, and concluded the permissive shelf was
empty. **`p874` searched the category again and byte-read seven licences: three are MIT.** The
strategic conclusion survives, but for a different and more precise reason — **not "nothing
permissive exists", but "the three permissive codebases are reference implementations, not
platforms."** The distinction decides what you can say in a procurement.

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **Proctor** | https://github.com/sudosylabs/proctor | **AGPL-3.0** | `main` | Self-hosted examination **and** proctoring platform aimed at institutions — Go server, React front end. The most complete open-source project in this category. No published supported-release or compatibility window, so treat maturity as unproven. |
| **OpenProctor** | https://github.com/kamlendras/OpenProctor | **AGPL-3.0** | `main` | Next.js/TypeScript. **Licence correction: secondary listings say MIT; the bytes on `main` say AGPL-3.0.** Thin install documentation, Vercel-oriented rather than clearly self-hostable. |
| **Proctor** (ganesh-786) | https://github.com/ganesh-786/Proctor | 🟢 **MIT** | `main` | **NEW `p874`.** Self-described modular, microservices-based AI proctoring. The most architecturally ambitious of the permissive three. **No tags, 1 branch** — a reference implementation. |
| **Proctora** | https://github.com/amaanwarsi/Proctora | 🟢 **MIT** | `main` | **NEW `p874`.** Flask + OpenCV + MediaPipe; webcam, microphone-noise and tab-switch monitoring, session violation logging, CI configured. 🔴 **Its own README says it should not be presented as a secure exam platform in its current state** — the project's words, not this KB's. |
| **SecureExam AI** | https://github.com/code-by-abrar/Online-Proctoring-system | 🟢 **MIT** | `main` | **NEW `p874`.** FastAPI + PostgreSQL with client-side TensorFlow.js face tracking and device detection. **No tags, 1 branch.** |
| **Pariksha** | https://github.com/SriSatyaLokesh/pariksha | 🔴 **AGPL-3.0** | `main` | **NEW `p874` — and a secondary-source correction.** A search summary presented it as *the* Apache-2.0 exam platform in this category. **The licence bytes on `main` say GNU Affero GPL.** Pre-alpha besides: the repo holds requirements and schemas, with the candidate runtime promised for v0.1. |
| **edx-proctoring** | https://github.com/openedx/edx-proctoring | 🔴 **AGPL-3.0** | **`master`** | **NEW `p874`.** Open edX's own proctoring subsystem — the realistic choice if the client is already on Open edX. Note the default branch is **`master`**, not `main`. |

**How to read this table — and it reads differently than it did in `p873`.** Seven candidates,
**three MIT and four AGPL-3.0**, and the licence axis no longer separates the useful from the
useless. The **maturity** axis does:

- 🟢 **The three MIT projects are permissive and genuinely runnable**, and **not one is
  institution-grade**: single-branch, no tagged releases, no supported-version policy, and in
  `Proctora`'s case an explicit author disclaimer against secure use. **Do not put one in front of
  a procurement board as a platform.** Their real value is as *capability references* — the
  face-tracking, tab-switch and audio-monitoring pieces are readable MIT code you can learn the
  shape of a build from, and legally reuse.
- 🔴 **The one complete platform (`sudosylabs/proctor`) is AGPL-3.0.** Workable where the
  institution hosts it itself — the copyleft obligation stays inside one tenancy, which is the
  normal education deployment — and unusable inside a distributed proprietary product. So the
  *mature* path remains open to a Globant **integration** engagement and closed to a Globant
  **product**.
- 🔵 **Net position:** a defensible permissive proctoring product would be a **greenfield build**
  that borrows from the MIT three. `p874` is the first pass able to state that with the licence
  bytes of seven candidates behind it rather than as an inference from two.

**The regulatory context matters more than the licence here.** The EU AI Act puts exam proctoring
in the high-risk tier (obligations from **2 December 2027** after the Digital Omnibus delay), the
Article 5(1)(f) **ban on emotion inference in education has applied since 2 February 2025**, and
Vietnam's **Decision 33/2026/QD-TTg** lists AI that monitors learner behaviour using biometric or
other automated mechanisms as a high-risk education system. Any webcam-and-gaze proctoring product
is now building directly into the most heavily regulated corner of education AI, in at least two
major jurisdictions, with immature copyleft tooling.

**The studio recommendation that follows from that:** lead with **assessment redesign** — oral
defence, process evidence, version-history review, in-class authentic tasks, `edx-ora2`
open-response workflows — and treat proctoring as the fallback the client asks for, priced with
its conformance burden visible. Detection-based integrity is losing on both the evidence and the
regulation; see `intel/trends.md` T8.

## Accessibility conformance — where it exists in this stack, and where it does not

New in `p873`, because it decides public-sector bids. The agent layer has almost no conformance
documentation (see `agents/top.md` gaps: `CAHLR/OATutor` is the only education-native agent in this
KB with a published statement). The **platform** layer is better placed: **Moodle core and its
mobile app are stated to be certified to WCAG 2.2 AA**, alongside Section 508 alignment. That is a
**vendor claim** (Open LMS) and `support.openlms.net` is unreachable from this session, so the
correct action in a bid is to **request the VPAT/ACR**, not to repeat the claim.

The practical consequence is an architecture decision, not a compliance footnote:

> Where **Section 508 / EN 301 549 / WCAG** conformance gates procurement, **do not ship your own
> learner-facing front end.** Launch the agent as an **LTI 1.3 tool inside a platform that already
> holds a conformance statement** (`Cvmcosta/ltijs`, Apache-2.0, is the plumbing) so the
> conformance story rides on the platform, and keep the custom UI for staff-facing surfaces where
> the bar is lower.

Two further facts, both secondary-sourced because EU primary sources are unreachable: the
**European Accessibility Act has applied since 28 June 2025**, and the next **EN 301 549** revision
aligning it with **WCAG 2.2 AA** is reported as due in the Official Journal in late 2026. And the
failure mode that actually loses audits is **embedded content, not the platform** — an accessible
LMS routinely serves an inaccessible SCORM package, PDF workbook or generated slide deck. **Any AI
content generator in the build inherits that obligation for everything it emits.**

## Declared gaps
### 🟢 `p879` — declared

- 🔴 **`ILIAS-eLearning` has no permissive surface at all** — 0 of 16 sampled repositories.
  Combined with `overhangio`/Tutor at 3%, these are the two estates where this KB's copyleft advice
  is **unchanged**, and `compose/patterns.md` **P19** does not apply.
- 🔴 **Still no permissive proctoring platform.** `openedx/edx-proctoring` is **AGPL-3.0**
  (measured this pass, 69 ★), so the census did not change `p875`'s conclusion: the honest advice
  remains **buy, or redesign the assessment** (**P17**).
- 🟡 **`apereo/phpCAS` was last pushed 2026-06-30.** CAS itself is pushed daily; its PHP client is
  not. Check it before committing a Moodle estate to it.


- ~~**No permissive open-source SIS exists**~~ — 🟢 **CLOSED by `p877`.**
  [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) is **MIT** at the bytes (1,150 B,
  `sha256₁₂ b8694396d7dc`): Laravel, API-first, Dockerised, with Android parent and teacher apps
  and 113 commits in 12 months. The three copyleft options stand as recorded — RosarioSIS GPL-2.0,
  Gibbon GPL-3.0, openSIS-Classic with no licence file at all.
  🔵 **Why it took five passes to find a repository that was always there:** the GitHub licence API
  reports `NOASSERTION` for it, because line 3 of its `LICENSE` is an SPDX comment. **The gap was
  never in the ecosystem; it was in trusting a licence-detector readout as a licence.** See
  `intel/trends.md` **T14**.
  🟡 **The restated gap, which is real:** a permissive SIS exists but is **small** (57★, HEAD five
  months cold). *A permissive, AI-native, institution-grade SIS* remains the clearest product gap
  in this file — the difference is that there is now a permissive base to start from rather than a
  copyleft one to work around.
- ~~**No *permissively licensed* open-source proctoring platform exists.**~~ **RESTATED by `p874`,
  which found the earlier framing factually wrong.** Permissive proctoring code **does** exist:
  `ganesh-786/Proctor`, `amaanwarsi/Proctora` and `code-by-abrar/Online-Proctoring-system` are all
  **MIT**, byte-read on `main`. **The accurate gap is maturity, not licence:** of seven verified
  candidates, the three permissive ones are single-branch and untagged (one disclaimed by its own
  author), and the only complete platform is AGPL-3.0. 🔴 **A secondary source also had to be
  corrected here** — `SriSatyaLokesh/pariksha` was presented as Apache-2.0 and is AGPL-3.0. Given
  that the EU moves proctoring into the high-risk tier on **2 Dec 2027** and Vietnam already lists
  biometric learner monitoring as high-risk, an institution-grade permissive proctoring platform
  remains the clearest unbuilt product in education AI — and plausibly one that should not be built.
- **No LATAM-origin education *platform*** surfaced in either pass's searches. LATAM appears in
  this file as a large **deployer** of Moodle, Chamilo, Kolibri and OJS, not as an originator
  of platforms. `p872` refines the picture: the region's own contribution is a **sovereign
  foundation model**, **Latam-GPT** (CENIA-led, launched 10 Feb 2026, open weights, Spanish and
  Portuguese, corpus gated behind an NDA) — infrastructure beneath the platform layer, not a
  platform. That asymmetry is itself the regional finding.
