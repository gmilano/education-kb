---
industry: education
region: Global
updated: 2026-11-03
---

## 2026-11-03 — platform layer: what you can customise, and what it costs you in licence terms

28 platforms verified this pass (`search/repositories` + `fork:true`, `422` control; 0 `archived`).
The split below is the single most decision-relevant fact in this file.

### The incumbents are copyleft, 5 for 5

| Platform | Repo | Licence | Stars | Pushed | Region strength |
|---|---|---|---|---|---|
| Moodle | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 `GPL-3.0` | 7578 | 2026-10-30 | Global — the most deployed LMS on earth; dominant in EMEA + LATAM public sector |
| Open edX | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 🔴 `AGPL-3.0` | 8218 | 2026-11-03 | Global — MOOCs, national platforms. ⚠️ Canonical slug is `openedx/openedx-platform`; the pre-rename `openedx/edx-platform` returns `422` |
| Canvas | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 `AGPL-3.0` | 6901 | 2026-04-30 | North America — dominant in US higher ed |
| Chamilo | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 `GPL-3.0` | 1020 | 2026-11-03 | LATAM + EMEA — strong Spanish/French public-sector base |
| ILIAS | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 `GPL-3.0` | 507 | 2026-11-03 | EMEA — German-speaking universities, public administration |

**Consequence:** on any engagement where the client already runs one of these, the viable commercial
shape is an agent or tool attaching over **REST, LTI or xAPI** — a network boundary that does not
trigger copyleft on your own code. In-process plugins (Moodle plugins, XBlocks) do.

### Permissive platform alternatives — available, but smaller

| Platform | Repo | Licence | Stars | Pushed | Fit |
|---|---|---|---|---|---|
| Kolibri | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `MIT` | 1168 | 2026-11-02 | **Offline-first** learning platform for low-connectivity deployment. Real LATAM/Africa field history. The strongest permissive platform in this base. |
| Sakai | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `ECL-2.0` | 1240 | 2026-11-03 | Higher-ed LMS under the Educational Community Licence — an Apache-2.0 derivative, i.e. **permissive**. The only incumbent-scale non-copyleft LMS. |
| Oppia | [`oppia/oppia`](https://github.com/oppia/oppia) | `Apache-2.0` | 6963 | 2026-11-03 | Interactive lesson platform with built-in pedagogy; strong for basic-education and underserved-learner programmes. |
| Project NOMAD | [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | `Apache-2.0` | 42059 | 2026-11-01 | Offline-first knowledge/education server (Wikipedia + book corpora). Largest permissive address in the sector by stars. |
| Flat | [`netless-io/flat`](https://github.com/netless-io/flat) | `MIT` | 6442 | 2026-10-30 | APAC — interactive virtual classroom client (web/Windows/macOS), Agora-based. |
| OpenVidu | [`OpenVidu/openvidu`](https://github.com/OpenVidu/openvidu) | `Apache-2.0` | 2141 | 2026-11-03 | Self-hosted real-time video/audio — the permissive live-classroom primitive. Spanish-origin, strong EMEA/LATAM fit. |
| Marsha | [`openfun/marsha`](https://github.com/openfun/marsha) | `MIT` | 151 | 2026-11-01 | EMEA — LTI learning-content management system (France Université Numérique). Permissive and LTI-native. |
| Richie | [`openfun/richie`](https://github.com/openfun/richie) | `MIT` | 318 | 2026-11-03 | EMEA — CMS for building course catalogue/portal front ends over Open edX. |
| Academico | [`academico-sis/academico`](https://github.com/academico-sis/academico) | `MIT` | 411 | 2026-10-28 | School management (Laravel/Filament) for small and mid institutions — permissive SIS. |
| IBL LMS | [`iblai/lms`](https://github.com/iblai/lms) | `MIT` | 208 | 2026-11-03 | Skills-intelligence platform: course discovery, competency tracking, credentials. Aligns with the 2026 skills-based-credential trend. |
| Sugarizer | [`llaske/sugarizer`](https://github.com/llaske/sugarizer) | `Apache-2.0` | 232 | 2026-11-01 | Web Sugar platform (OLPC lineage) for primary education on any device. **New to this base.** |
| Tutor | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 `AGPL-3.0` | 1131 | 2026-11-03 | The standard Docker distribution for operating Open edX. Operationally near-essential; licence is `AGPL-3.0`. |

### Education ERP / SIS — the Odoo-style customisable systems

| System | Repo | Licence | Stars | Pushed | Note |
|---|---|---|---|---|---|
| OpenEduCat | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 `NOASSERTION` | 905 | 2026-11-02 | Education ERP built natively on **Odoo** — the closest analogue to "Odoo for ERP" in this sector. 🔴 Licence undeclared in API metadata; byte-read `LICENSE` before any engagement. |
| RosarioSIS | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 `GPL-2.0` | 650 | 2026-11-03 | Student Information System for school management; mature, multi-language. |
| i-Educar | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 `GPL-2.0` | 723 | 2026-10-29 | **LATAM / Brazil** — the largest Brazilian free-software school-management system, used by municipal education networks. Highest-value LATAM public-sector reference in this file. |
| openSIS Classic | [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🔴 none declared | 349 | 2026-10-26 | SIS with commercial editions. No licence grant in metadata — treat as unavailable until verified. |

### Other live platforms worth knowing

| Platform | Repo | Licence | Stars | Pushed | Note |
|---|---|---|---|---|---|
| Frappe LMS | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 `AGPL-3.0` | 3369 | 2026-11-03 | Integrates with the Frappe/ERPNext stack — relevant when the client already runs ERPNext. |
| LearnHouse | [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | 🔴 `AGPL-3.0` | 2446 | 2026-11-03 | Modern next-gen learning platform, very actively developed. |
| ClassroomIO | [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 🔴 `AGPL-3.0` | 1737 | 2026-11-03 | Customer-training platform — the B2B/academy use case rather than schools. |
| OpenOLAT | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🔴 `NOASSERTION` | 449 | 2026-11-03 | EMEA — Swiss/German university LMS. Licence undeclared in metadata (project states Apache-2.0; verify by byte-read). |
| INGInious | [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 `NOASSERTION` | 243 | 2026-11-03 | EMEA — secure containerised automated exercise assessment (UCLouvain). The pick when submitted code must run safely. |
| Adapt Framework | [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | 🔴 `GPL-3.0` | 632 | 2026-11-02 | Authoring toolkit for responsive, accessible, multi-language HTML5 courses. |
| MOOCCubeX | [`THU-KEG/MOOCCubeX`](https://github.com/THU-KEG/MOOCCubeX) | 🔴 `GPL-3.0` | 202 | 2023-12-27 | **APAC** — Tsinghua large-scale knowledge repository for adaptive learning and knowledge tracing. A *dataset/graph*, not a platform. 🔴 Stale since 2023-12. **New to this base.** |
| cn-math-taxonomy | [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | 🔴 `NOASSERTION` | 6376 | 2026-11-03 | **APAC** — curriculum-aligned knowledge graph for Chinese maths/English/physics: 1,644 concepts, 2,403 prerequisite edges, 6,723 items. Rare curriculum-structure asset; licence undeclared. |

## 🆕 `p637` — the largest address in this file is read-only, and the platform question gains a third column

🔴 **`637-A` lands hardest here.** This file publishes
[`ketanchoyal/Our-E-School`](https://github.com/ketanchoyal/Our-E-School) as *"the largest address in
the axis"* — `504★`, `MIT` (`1,069 B`), correctly marked *"Abandoned — last push `2021-08-19`"*.
🔴 Measured today it is also **`archived: true`**, which this file does not say in any of its `4`
mentions. 🟡 The existing verdict (*"Flutter app, not a platform"*) already steers a studio away from
it, so no quote is at risk — but the `504★` figure is the one a client sees, and *"abandoned"* invites
the obvious question *"so can we pick it up?"*, whose answer is **no, not upstream**.

| This file's row | Stars | Grant | Published verdict | Measured `archived` | Change |
|---|---|---|---|---|---|
| [`ketanchoyal/Our-E-School`](https://github.com/ketanchoyal/Our-E-School) | **`504`** | `MIT` | 🔴 Abandoned, last push `2021-08-19` | 🔴 **`true`** | 🔴 add **read-only** |
| [`mindsdb/edux`](https://github.com/mindsdb/edux) | `6` | `MIT` | 🔴 Last push `2020-07-01`; Open edX *theme* | 🔴 **`true`** | 🔴 add **read-only** |
| [`otsimo-archive/aac`](https://github.com/otsimo-archive/aac) | `25` | `AGPL-3.0` | 🔴 abandoned by declaration | 🔴 `true` | 🟢 already flagged |
| [`microsoftarchive/Learn-LTI`](https://github.com/microsoftarchive/Learn-LTI) | `132` | `MIT` | 🔴 abandoned by declaration | 🔴 `true` | 🟢 already flagged |

🔵 **The pattern in the FLAGGED column is worth naming.** The two rows this base caught are the two
whose **owner namespace announces it** — `microsoftarchive`, `otsimo-archive`. The two it missed are
owned by `ketanchoyal` and `mindsdb`, names that say nothing. 🟡 So the base's archive coverage is not
the product of an instrument; it is the product of a naming coincidence, and it will keep missing every
archived repository whose owner did not rename itself.

🟢 **The platform table from `p636` gains the column that decides a fork.** `p636` established that what
a studio can own is set by the **extension substrate**, not the core licence. `637-A` adds the second
axis: whether the thing you would fork is still **writable**.

| Platform / row | Core licence | Boundary | Writable upstream? | What a studio can do |
|---|---|---|---|---|
| **Canvas** | `AGPL-3.0` | 🟢 network (`REST`/`LTI`) | 🟢 yes — `MCP` head `317★`, pushed on the read date | Build client-side and upstream freely |
| **Brightspace (`D2L`)** | proprietary | 🟢 network | 🟢 yes — `62★`, pushed `2026-11-03T17:31Z` | `MIT` tooling against the API |
| **Open edX** | `AGPL-3.0` | 🔴 in-process `XBlock` | 🟡 mixed — `raccoongang/edx_xblock_scorm` (`32★`) is **archived** | Themes `MIT`; `XBlock`s `AGPL` and the SCORM one is read-only |
| **Moodle** | `GPL-3.0` | 🔴 in-process `PHP` | 🟢 yes, but `GPL` headers bind (`635-A`) | Own only what sits outside the plugin boundary |
| [`openfun/marsha`](https://github.com/openfun/marsha) | 🟢 `MIT` | 🟢 `LTI` `LCMS` | 🟢 **yes** — `151★`, pushed `2026-11-01` | 🟢 The one permissive `LTI` platform here, and it is live |

🔵 **Quote accordingly:** ask for the integration boundary, then ask whether the repository still accepts
a pull request. `openfun/marsha` is the only row in this file that answers 🟢 to both.


## 🆕 `p636` — the platform question, answered with a number, and the one `LTI` `LMS` that is `MIT`

🟢 **`p635` left this base a question to ask of any `LMS` before quoting — *what substrate does it
extend in?* — and said the answer was checkable in an afternoon. It was. Here it is as a table.**

| Platform | Core licence | Extension substrate | Boundary | Permissive share of its extension estate | What a studio can own |
|---|---|---|---|---|---|
| **Moodle** | `GPL-3.0` | `PHP` plugin, in-process | 🔴 in-process | `10.0%` (`138` `MIT` / `1,239` `GPL-3.0`) | Only what sits outside the plugin boundary — `MCP` servers, provisioning, containerisation |
| **Open edX** | `AGPL-3.0` | `Python` `XBlock`, in-process | 🔴 in-process | `25.0%` (`76` `MIT` / `228` `AGPL-3.0`) | Themes (assets and configuration, `12 of 12` `MIT` at `p634`); **not** `XBlock`s |
| **WordPress `LMS`** | `GPL-2.0+` | `PHP` plugin, in-process | 🔴 in-process | `40.0%` (`12` `MIT` / `18` `GPL-3.0`) — small denominator | Nominally more, but the contract is unenforced and the grants are unreliable (`636-C`) |
| **Canvas** | `AGPL-3.0` | `REST`/`GraphQL` API + `LTI`, over the network | 🟢 **network** | Not measurable (`636-E`), but the `MCP` channel head is `317★` `MIT` | Everything on the client side of the API |
| **Brightspace (`D2L`)** | proprietary | `REST` API + `LTI`, over the network | 🟢 **network** | n/a — core is not open | `MIT` tooling against the API (`62★` head) |

🔵 **The rule, now with a mechanism and a number.** The core's licence does not predict what a studio can
own; the **substrate the extension runs in** does. Moodle and WordPress are both `GPL` cores with `PHP`
plugin substrates and sit a factor of four apart on permissive share, because enforcement differs — and
Canvas, whose core is the *most* restrictive licence in the table (`AGPL-3.0`), is the one platform whose
extension ecosystem is permissive almost throughout, because its extensions are **network clients**.
🟡 Quote accordingly: ask for the integration boundary before asking for the licence.

🟢 **The vertical solution this pass actually adds, and it is a real platform.**
[`openfun/marsha`](https://github.com/openfun/marsha) — an open-source **`LTI` Learning Content
Management System** from France Université Numérique, `MIT` (`1,078 B` payload read at
`raw.githubusercontent.com`, `151★`, pushed `2026-11-01`). 🔵 This is the rarest shape in this base's
holdings: an `LMS`-class system that is **permissive**, where Moodle is `GPL-3.0`, Open edX `AGPL-3.0`,
Chamilo `GPL`, Sakai `Apache-2.0`-but-dormant and Canvas `AGPL-3.0`. 🟡 It is an `LCMS` — it manages
content and plugs into an existing `LMS` over `LTI` rather than replacing it — so it fits beside Moodle
or Canvas, not instead of them. 🔴 `EMEA`-institutional and single-publisher: price the bus-factor.

🟢 **The boundary layer, also real and also permissive.**
[`instructure/ims-lti`](https://github.com/instructure/ims-lti) (`MIT`, `1,068 B`, `203★`, pushed
`2026-10-02`) is maintained by Canvas's own vendor and implements both sides of `LTI`;
[`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (`MIT`, `1,070 B`, `138★`) is the
`Python` `LTI` `1.3` Advantage entry point but has been untouched since `2024`. 🔴
[`microsoftarchive/Learn-LTI`](https://github.com/microsoftarchive/Learn-LTI) (`MIT`, `132★`) is
**archived** — a design reference, not a dependency.

🔴 **The grant-reading rule, revised again and now in its portable form.** `p635` said: for a Moodle
plugin, grade the source header because it says `GPL` under an `MIT` `LICENSE`. Tested on `WordPress`
this pass, the `GPL` half does not hold — `0 of 4` graded `WordPress` `LMS` plugins carry a `GPL` header
— but the **disagreement** does: [`devMiguelCarrero/lms-matic-extender`](https://github.com/devMiguelCarrero/lms-matic-extender)
reports `MIT` on GitHub, reads `MIT` in a `1,073 B` byte-read `LICENSE`, and declares `License: OSLv3` in
its own plugin header. 🟡 `Open Software License 3.0` is copyleft **and `GPL`-incompatible** — a licence
that is neither of the two a reviewer would be looking for. 🔵 So the rule to carry into an engagement is
**"grade all three channels and expect them to disagree"**, not "expect `GPL`". `636-B`/`636-C`.

🟡 **Unchanged and still the honest ceiling:** no permissive **platform of record** exists for the
accessibility / special-education tier (`619-Q`, closed at `p635`), and nothing this pass changes it.

## 🆕 `p635` — `Moodle` as a vertical starting point: the licence line runs around the plugin boundary, not through the middle of the estate

🟢 **What is new.** This base has held `Moodle` as its first vertical since `p1` and has priced it as
"`GPL-3.0` core, therefore careful". `p634` graded the Open edX estate and produced a more optimistic
rule — permissive presentation, copyleft function — and named `Moodle` plugin estates as the test. The
test was run this pass against three estates (`770` repositories, `EMEA` and `APAC`) and **`Moodle` does
not behave like Open edX.**

🔴 **The measured comparison, and it changes the advice rather than extending it:**

| What a client asks for | Open edX estate (`p634`) | `Moodle` estates (`p635`) | Consequence for a `Moodle` engagement |
|---|---|---|---|
| A themed, branded institutional portal | 🟢 `12 of 12` themes `MIT` — fork and ship | 🔴 `0` permissive of `9` graded themes; `GPL-3.0` at an identical `35,146 B` payload, or ungranted | 🔴 A rebranded Moodle theme is a `GPL-3.0` derivative. **`p634`'s advice must not be reused here** |
| A reproducible deployment of the platform | 🟢 `MIT` | 🟢 `MIT` — [`moodledocker-nginx-proxy`](https://github.com/learnweb/moodledocker-nginx-proxy), [`moodle-provisioner-frontend`](https://github.com/Moodle-An-Hochschulen/moodle-provisioner-frontend) | 🟢 The one permissive layer, and it is real: proven university-scale practice |
| A new graded activity, quiz type, tutoring block | 🔴 `AGPL-3.0` | 🔴 `GPL-3.0` | 🔴 Derivative either way. Quote as a client-owned contribution |
| Learner analytics | 🔴 `AGPL-3.0` in-platform | 🟡 `GPL-3.0` as a `local_` plugin, or `MIT` outside via `MCP` | 🟢 **The choice exists in Moodle** — see [`compose/patterns.md`](../compose/patterns.md) `p635` |

🟡 **`635-B`, the rule that now covers both platforms:** *the permissive subset of a platform-derived
estate is whatever sits outside the platform's own **extension mechanism**.* Presentation is not
inherently safe — it was safe in Open edX because a theme there is assets and configuration, and it is
unsafe in Moodle because a theme there is a `PHP` plugin. 🔵 The question to ask of any `LMS` before
quoting is *what substrate does this platform extend in?*, and the answer is checkable in an afternoon.

🔴 **The grant-reading rule that has to go in front of all of it (`635-A`).** For a `Moodle` plugin,
neither the `LICENSE` payload nor GitHub's licence badge is the grant. `3 of 3` candidate `MIT` themes
carry `GPL-3.0-or-later` headers in their own source files while reporting `MIT` on both channels — a
fork can replace a repository `LICENSE` and `license.spdx_id` follows the file. 🟡 Grade `version.php` /
`config.php` headers. 🔵 This is the first case on this base where payload and metadata **agree with each
other and are both wrong**, which is why two-channel agreement is no longer sufficient corroboration.

🟢 **The vertical that genuinely opened this pass is not a platform — it is the agent boundary.** `138`
repositories match `moodle plugin license:mit`, maximum `42★`, median `0★`, and the freshest cohort is
`MCP` servers and agent skills updated within hours of this read.
[`IsaacAnwar/moodle-mcp`](https://github.com/IsaacAnwar/moodle-mcp) (`MIT`, `9★`) is the cleanest
permissive entry point to an `LMS` this base holds, because Moodle's web-services API makes an `MCP`
server a **consumer** of `GPL` software rather than a derivative of it. 🟡 Unclaimed and maintained by
individuals: a vertical opportunity rather than a vertical solution.

🟢 **`619-Q` can close.** Its third and last instrument was probed this pass: the Deaf-education channel
holds `27` repositories, maximum `5★`, top two **ungranted**, and three `Apache-2.0` instruments at `≤2★`
of which **none is an `LMS`** — they are sign-language translation and practice components. 🔵 Final
three-part answer: `AAC` has permissive institutional supply (`p634`), `IEP` is a measured sector-wide
absence (`p634`), Deaf-education has permissive components with no platform and no traction (`p635`).
🔴 In all three arms a permissive **platform of record** for the accessibility / special-education tier
remains absent — which is the answer, not a failure to find one.

## 🆕 `p634` — the Open edX **institutional estate** is a vertical starting point, and its licence line runs through the middle of it

🟢 **What is new.** This base has held `openedx/edx-platform` (`AGPL-3.0`) as a vertical since `p2` and has
priced it as copyleft-and-therefore-hard. The LATAM estate found this pass changes the shape of that
advice: [`eol-uchile`](https://github.com/eol-uchile) — `113` repositories, Universidad de Chile — shows
what a decade of **running** Open edX at national scale publishes, and `23` of it is permissive.

🔴 **But the licence line is functional, not arbitrary**, and it is measured rather than assumed:

| What a client asks for | Where it sits in the estate | Grant | Consequence for an engagement |
|---|---|---|---|
| A themed, branded institutional portal | `12` graded themes | `MIT` | 🟢 Fork, rebrand, ship. No notice obligation beyond attribution |
| A reproducible deployment of the platform | `edx-openuchile`, `eol-edx`, containers | `MIT` | 🟢 The highest-value permissive artefact here: proven national-scale deployment practice |
| A new graded activity, quiz type, tutoring block | `15` graded `XBlock`s | `AGPL-3.0` | 🔴 Derivative of the `AGPL` core. Network-served, so the source obligation **triggers**. Quote as a build or as a client-owned contribution |
| Learner profiling / recommendation | `eol_learner_profiles` | `AGPL-3.0` | 🔴 Precisely the component a client wants and the one that cannot be taken proprietary |

🟡 **The sentence to put in an estimate:** *in an Open edX estate the presentation and deployment layers
are reusable and the pedagogy layer is not.* That is `634-A`, and it generalises beyond this estate as an
open question — Moodle plugin estates (`GPL-3.0` core) are the obvious next test and have not been run.

🟢 **`619-Q` narrows again, and this time on the supply side rather than by counter-example.** The
accessibility half of the gap has a **permissive institutional publisher**:
[`inclusive-design`](https://github.com/inclusive-design) (OCAD University) publishes `28`
`BSD-3-Clause` repositories, `23` of them pushed in `2026`, covering `AAC` palettes
([`adaptive-palette`](https://github.com/inclusive-design/adaptive-palette), pushed `2026-11-02`),
generative-AI `AAC` ([`baby-bliss-bot`](https://github.com/inclusive-design/baby-bliss-bot)), `WCAG`
reporting and `ATAG` material. 🔵 This is the first time this base can name a permissive **system of
practice** for accessibility rather than a single repository.

🔴 **The `IEP` half does not narrow — it is now a measured sector-wide absence.** See `634-C`: `7` `MIT`
and `0` `Apache-2.0` repositories worldwide in the education-context channel, maximum `5★`, and that
maximum is ungranted and dead since `2016`
([`ChelseaSchool/MyIEP`](https://github.com/ChelseaSchool/MyIEP)). US special-education compliance
remains a **build**, and that is a finding about the sector, not about this shelf.

## 🆕 `p632` — reads `2026-11-03` — **🟢 THE "NO PERMISSIVE PLATFORM OF RECORD" FINDING NARROWS TWICE IN ONE PASS: AN `Apache-2.0` HIGHER-ED **ACCOMMODATIONS** SYSTEM OF RECORD EXISTS (`619-Q`), AND A `521★` `MIT` **SCHOOL** SYSTEM OF RECORD EXISTS. 🟢 `630-H` IS CENSUSED FOR THE FIRST TIME AND THE CLASS SPLITS INTO FOUR WITH OPPOSITE COMMERCIAL CONSEQUENCES. 🔴 THE CENSUS INSTRUMENT IS REJECTED WITH A PRECISION FIGURE RATHER THAN ADOPTED.**

### 🟡 `619-Q` NARROWED, not closed — the accessibility tier has a permissive platform of record, in the wrong segment

🔵 **`619-Q` as written:** *"no permissive platform of record exists in the accessibility / special-education
tier … searched and not found: an `IEP` management system, an `AAC` platform, a Deaf-education LMS … the
components are permissive and already built; the platform is not."*

🟢 **Counter-example found today.** [`EsupPortail/esup-oasis`](https://github.com/EsupPortail/esup-oasis) —
`Apache-2.0`, `11,357 B` byte-read, pushed `2026-10-21` — is a platform of record for students who need
individual accommodation: student-submitted requests against manager-defined campaigns, commission review,
a beneficiary file, accommodation plans, interview minutes. That is the case-management spine of a
disability-services office, permissively licensed and live.

🔴 **Why `619-Q` stays open rather than closing.** `619-Q`'s three named misses are all **K-12 US**
instruments — `IEP` is a statutory artefact of US special education, and `AAC` is a device category.
`esup-oasis` is **higher education**, **EMEA**, and organised around *accommodation campaigns*, not around a
legally-mandated individualised education programme. 🟡 So the honest revision is: the tier gap is **segment
specific**. A permissive HE accommodations platform exists; a permissive K-12 `IEP` system is still not found.
🔵 Commercially this is the better news of the two, because HE is where Globant's education engagements sit.

### 🟢 Platforms filed this pass

| Platform | Repo | Licence | Bytes | Region | Segment | What a studio does with it | Stars | Pushed |
|---|---|---|---|---|---|---|---|---|
| **Oasis** | [`EsupPortail/esup-oasis`](https://github.com/EsupPortail/esup-oasis) | 🟢 `Apache-2.0` | `11,357 B` | 🟢 EMEA | Higher ed | Accommodations system of record. Customise the campaign model; put an agent on the request triage, not on the file | `6★` | `2026-10-21` |
| **SIAKAD Laravel** | [`adhiariyadi/Sistem-Informasi-Akademik-Sekolah-Laravel`](https://github.com/adhiariyadi/Sistem-Informasi-Akademik-Sekolah-Laravel) | 🟢 `MIT` | `1,069 B` | 🟢 APAC (Indonesia) | K-12 | A whole permissive school academic system. 🔴 Last pushed `2023-07-30`: adopt as a **base to fork**, not a dependency to track | `521★` | `2023-07-30` |
| **Hyper Web School** | [`ugunNet21/hypervel-web-school`](https://github.com/ugunNet21/hypervel-web-school) | 🟢 `MIT` | `1,097 B` | 🟢 APAC (Indonesia) | K-12 | The maintained alternative to the row above — administration, teaching, reporting; Laravel-family stack | `75★` | `2026-09-02` |
| **esup-signature** | [`EsupPortail/esup-signature`](https://github.com/EsupPortail/esup-signature) | 🟢 `Apache-2.0` | `11,361 B` | 🟢 EMEA | Higher ed | Signature/visa circuits. The highest-leverage permissive HE back-office component found to date | `36★` | `2026-10-14` |
| **esup-emargement** | [`EsupPortail/esup-emargement`](https://github.com/EsupPortail/esup-emargement) | 🟢 `Apache-2.0` | `11,358 B` | 🟢 EMEA | Higher ed | Attendance and presence control against the institution's SI | `12★` | `2026-10-21` |
| **esup-dematec** | [`EsupPortail/esup-dematec`](https://github.com/EsupPortail/esup-dematec) | 🟢 `Apache-2.0` | `11,358 B` | 🟢 EMEA | Higher ed | Academic recruitment dematerialisation, wired to the national recruitment application | `6★` | `2026-09-11` |
| **esup-pay** | [`EsupPortail/esup-pay`](https://github.com/EsupPortail/esup-pay) | 🟢 `Apache-2.0` | `11,358 B` | 🟢 EMEA | Higher ed | Online payment forms for enrolments, conference fees, donations. 🔴 **`CLIENT-ONLY`, vendor counterparty**: it executes payment through **Paybox**, a commercial service. Permissive code, contract required | `6★` | `2026-10-19` |

### 🔴 Copyleft platforms of record found the same day — placed, and not sellable as a base

| Platform | Repo | Licence | Bytes | Region | Why it matters anyway |
|---|---|---|---|---|---|
| **SME-SGP** | [`prefeiturasp/SME-SGP`](https://github.com/prefeiturasp/SME-SGP) | 🔴 `AGPL-3.0` | `34,442 B` | 🟢 **LATAM** (Brazil) | The **São Paulo municipal education secretariat's** pedagogical management system. Proof that LATAM public bodies publish their systems of record — and that they publish them reciprocally |
| **Kimkëlen** | [`Desarrollo-CeSPI/kimkelen`](https://github.com/Desarrollo-CeSPI/kimkelen) | 🔴 `GPL-2.0-only` | `697 B` notice | 🟢 **LATAM** (Argentina) | *Sistema Integral de Gestión de Colegios*, held by **CeSPI – UNLP**. `GPL-2.0` **without** "or later" is the most restrictive combination in this base: not even upgradeable to `GPL-3.0` |
| **Esup-Pod** | [`EsupPortail/Esup-Pod`](https://github.com/EsupPortail/Esup-Pod) | 🔴 `LGPL-3.0` | `7,652 B` | 🟢 **EMEA** | The estate's video platform. 🟡 `LGPL` is the mildest of the three: link against it, keep your own code — the `MPL-2.0` argument from `p631`, one notch stricter |
| **absensi-sekolah-qr-code** | [`ikhsan3adi/absensi-sekolah-qr-code`](https://github.com/ikhsan3adi/absensi-sekolah-qr-code) | 🔴 `GPL-3.0` | `35,149 B` | 🟢 **APAC** (Indonesia) | `495★`, pushed `2026-10-25` — QR attendance with WhatsApp notification. The best-starred Indonesian attendance system, and reciprocal |

### 🟢 `632-C` — `630-H` censused at last, and the class is really **four** classes

🔵 `630-H` named *"permissively-licensed thin clients for proprietary services"* and the register has carried
*"no census of the existing shelves against it yet"* ever since. 🟢 Censused today over `1,577` sell-shelf
rows — `649` on `agents/top.md`, `466` on `repos/foundations.md`, `462` here —
`evidence/client-only-census.2026-11-03-p632.tsv`.

| Subclass | What the client talks to | Rows found | Commercial consequence |
|---|---|---|---|
| 🔴 **VENDOR** | a commercial service | `3` shelved + `1` new (`esup-pay`) | Permissive code, **useless without a contract**. This is the only subclass `630-H` actually warned about |
| 🟢 **STATE** | a public-sector platform | `1` shelved (`neispy`, Korea NEIS) + `1` new (`esup-siscol`, APOGEE) | **The opposite of a risk.** Free to interoperate, and the counterparty outlives the engagement |
| 🟡 **OPEN** | software that is itself open source | `2` (`canvasapi`, `OpenLRW` client) | No lock-in; worst case you fork the server too |
| 🔵 **PROTOCOL** | a *specification* (xAPI, SCORM) | `4` | **Not a client-only risk at all** — there is no service to be locked out of |

🔴 **And the census instrument is rejected, with a number.** A keyword sweep for client-shaped prose returned
`11` hits of which `6` are true clients: **precision `54.5 %`, recall unknown**. The `5` false positives are
`4` standard-protocol wrappers and one autograder whose row happens to read *"ships a student-side client for
public checks"*. 🟡 Following `606`'s rule — measure a proposed control before adopting it — the keyword
sweep is **not adopted**: it measures this base's vocabulary, not the class. 🔵 The census that would settle
`630-H` is the `606` method, `1,577` upstream README first screens, and that is its price.

🟢 **The finding that makes the split worth the work.** `p631`'s APAC operative was *"don't fork the local
platform — interoperate with the state platform"*. That play **produces** `CLIENT-ONLY` artefacts by
construction. Under `630-H` as written, the recommended pattern looked like the flagged risk. Split by
counterparty, the two separate cleanly: interoperating with a **state** platform is the play, and depending
on a **vendor** platform is the risk. `esup-siscol` (APOGEE, France) and `neispy` (NEIS, Korea) are the same
artefact in two regions, and `esup-pay` sits in the other column in the same estate.

## 🆕 `p631` — reads `2026-11-03` — **🔴 THE PLATFORM LEG'S *ABSENCE* CLAIM IS REFUTED ON THIS BASE'S OWN ROWS, AND `MPL-2.0` ENTERS THIS SHELF AS A THIRD LICENCE POSTURE BETWEEN PERMISSIVE AND COPYLEFT.**

🔵 Every licence below was read from payload bytes on the metadata-declared default branch. Evidence:
`evidence/grant-byteread.2026-11-03-p631.tsv`.

### 🔴 The platform leg claimed no permissive education ERP exists. Three do.

| Platform | Repo | Byte-read licence | Stars | Status |
|---|---|---|---|---|
| **skuul** | [`yungifez/skuul`](https://github.com/yungifez/skuul) | 🟢 `MIT` | `471★` | held, re-confirmed |
| **College-ERP** | [`Ansarimajid/College-ERP`](https://github.com/Ansarimajid/College-ERP) | 🟢 `MIT` | `201★` | held, re-confirmed |
| **Django-School-Management-System** | [`adigunsherif/Django-School-Management-System`](https://github.com/adigunsherif/Django-School-Management-System) | 🟢 `MIT` | `395★` | 🟢 **new this pass** |
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 `LGPL-3.0` | — | held — the leg got this one **right** |
| **ERPNext (education)** | [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 `GPL-3.0` | — | held — right again |

🟢 **What the leg got right and wrong is itself the lesson.** It graded the two *named, well-known* education
ERPs correctly and concluded from their copyleft that **no permissive one exists**. 🔴 The three `MIT` systems
above are smaller, unbranded and absent from listicles — so the leg's absence claim is really a statement about
**what gets written about**, not about what is published. See `631-F`.

### 🟡 `MPL-2.0` — a third posture this shelf has not carried, and it is not a footnote

🔵 [`rolling-scopes/rsschool-app`](https://github.com/rolling-scopes/rsschool-app) (`16,724 B`, `10,392★`,
pushed `2026-11-02`) runs a complete education process: cohorts, mentor assignment, task distribution,
cross-check review rounds, certificates.

| | `Apache-2.0` / `MIT` | 🟡 `MPL-2.0` | `GPL-3.0` / `AGPL-3.0` |
|---|---|---|---|
| Link from proprietary code | 🟢 yes | 🟢 **yes** | 🔴 no (derivative work) |
| Modify a source file | 🟢 keep it closed | 🟡 **that file stays `MPL`** | 🔴 whole work becomes copyleft |
| Hosted service trigger | 🟢 none | 🟢 **none** | 🔴 `AGPL` only |

🟢 **Operative for a studio:** `MPL-2.0` is the one posture where *"fork the platform"* and *"keep our IP"* are
**both** true, with a bounded obligation — publish your diffs to **the files you touched**, nothing more. That
is a materially different conversation from Moodle or Open edX, and it is cheaper to price than either
extreme. 🔴 The trap is treating it as permissive in a procurement sheet: it is not, and the obligation is
real even though it is narrow.

### 🔴 The platform tier by region, measured on the supply channel today (`631-F`)

🔵 `p631` ran the **supply** census in-region for the first time (`evidence/region-supply-census.2026-11-03-p631.tsv`).
The platform-tier result is the sharpest regional statement this shelf can make:

| Region | Platform-tier supply found | Licence posture |
|---|---|---|
| 🔴 **APAC (China)** | [`edusoho/edusoho`](https://github.com/edusoho/edusoho) `1,866★`; [`roncoo/roncoo-education`](https://github.com/roncoo/roncoo-education) `1,567★`; [`zijian-optics/SolaireEPDA`](https://github.com/zijian-optics/SolaireEPDA) `90★` | 🔴 `0 of 10` permissive: one **ungranted**, two `AGPL-3.0`, one `GPL-3.0` |
| 🟢 **APAC (China), permissive exception** | [`zhistaredu/StarTraining`](https://github.com/zhistaredu/StarTraining) `1,239★` | 🟢 `Apache-2.0` — the only buildable platform the leg returned in-region |
| 🟡 **LATAM** | `Universidade-Livre` lines (`MIT`, `21,006★` + `1,427★`) — **held** | 🟢 permissive, but **curriculum corpora, not platforms** |
| 🔴 **EMEA** | nil permissive across `de`, `ar` and Africa legs, each **calibrated** against a bare-query count | an informed gap, not silence |

🟢 **Operative:** a China engagement that assumes it can fork the local platform is wrong by default —
the local platform tier is copyleft or ungranted, and `StarTraining` is the single permissive exception.

## 🆕 `p630` — reads `2026-11-03` — **🔴 THIS PASS'S OWN WEB LEG GOT `2 of 2` PLATFORM LICENCE CLAIMS WRONG, BOTH REFUTED ON BYTES: CHAMILO IS `GPL-3.0` NOT `Apache-2.0`, AND SAKAI IS `ECL-2.0` NOT `Apache 2.0`. 🟢 AND `openedx/edx-platform`'s RENAME IS RESOLVED BY NAME ON IDENTICAL `HEAD`.**

🔵 Every licence in the table below was read from the payload bytes on the repository's metadata-declared
default branch. Evidence: `evidence/grant-byteread.2026-11-03-p630.tsv`.

### 🔴 The web leg's platform licence claims, adjudicated on bytes

🔵 The `open source platform education LMS SIS MIT Apache 2026` leg returned two **Apache** claims, each
sourced to a third-party tracker or a vendor comparison page. Both are wrong:

| Platform | 🔴 The leg claimed | 🟢 Byte-read today | Payload | Why the difference is not cosmetic |
|---|---|---|---|---|
| **Chamilo** [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 `Apache-2.0` *("actively maintained, under Apache-2.0 on a third-party tracker page")* | 🔴 **`GPL-3.0`** | `LICENSE`, `35,147 B`, title `GNU GENERAL PUBLIC LICENSE` | 🔴 **Strong copyleft.** A client fork delivered as a hosted service is a distribution question Globant must answer; `Apache-2.0` would have said there was nothing to answer. |
| **Sakai** [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 `Apache 2.0` *("stewarded by the Apereo Foundation and licensed under Apache 2.0")* | 🟢 **`ECL-2.0`** | `LICENSE`, `11,120 B`, title `Educational Community License Version 2.0` | 🟢 **Buildable, but it is not Apache.** `ECL-2.0` is `Apache-2.0` with the **patent grant narrowed** to the contributor's own work — this base diffed the two on bytes at `624-E` and found `78` words added, `9` removed and **no obligation added**. |

🟢 **Sakai is still a build-on platform** — `1,240★`, pushed `2026-11-02`, `ECL-2.0` is OSI-approved and
`624-E` settled that it adds no obligation over `Apache-2.0`. 🔴 What is refuted is the **name**, and the name
is what a procurement reviewer greps for.

🔵 **The generalisation, which `p623` already measured once:** web digests got `2 of 2` permissive claims wrong
at `p623` and `2 of 2` wrong again here, in a different tier. 🟢 A licence claim from a tracker page, a vendor
comparison or a "best open source LMS 2026" listicle is a **lead**, never a finding.

### 🟢 `openedx/edx-platform` — the rename resolved by **name**, on identical `HEAD`

🔵 `p626` established that this address was *renamed, not mis-served*, and the `repo:` channel reports it
🔴 `HTTP 422`. 🟢 `629-D`'s procedure — `422` **and** `ls-remote` exit `0` ⇒ rename, then read the name
GitHub's redirect serves — names the target:

| Was | 🟢 Now | `HEAD` on both | Metadata today |
|---|---|---|---|
| `openedx/edx-platform` | 🟢 [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 🟢 **`732fc11ebef1fea7a85f074bbbdf4c92ec3faae4`** | `8,216★` `AGPL-3.0` pushed `2026-11-03` |

🟢 The new repository's own README confirms it: *"Formerly known as 'edx-platform'."* Grant byte-read on
`master`: `LICENSE`, `35,136 B`, title `GNU AFFERO GENERAL PUBLIC LICENSE`. 🔵 The target was already on this
base, so this is a **name-level** closure, not a new row — and it is the second consecutive pass where
`629-D`'s `422`-plus-exit-`0` discriminator paid.

### 🟢 The platform shelf, re-measured on bytes today

| Platform | Repo | 🟢 Licence (byte-read) | Payload | Stars | Pushed | Build-on reading |
|---|---|---|---|---|---|---|
| Moodle | [`moodle/moodle`](https://github.com/moodle/moodle) | `GPL-3.0` | `COPYING.txt`, `35,147 B` | `7,576★` | `2026-10-30` | 🔴 Copyleft. Customise via **plugins**, which is Moodle's own extension contract. |
| Open edX | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | `AGPL-3.0` | `LICENSE`, `35,136 B` | `8,216★` | `2026-11-03` | 🔴 Network copyleft. The strictest obligation on this shelf. |
| Canvas LMS | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `AGPL-3.0` | `LICENSE`, `34,520 B` | `6,900★` | 🔴 `2026-04-30` | 🔴 Network copyleft, and `6.1` months since last push. |
| Sakai | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`** | `LICENSE`, `11,120 B` | `1,240★` | `2026-11-02` | 🟢 **Buildable** — `Apache-2.0` with a narrowed patent grant, no added obligation (`624-E`). |
| Chamilo | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **`GPL-3.0`** | `LICENSE`, `35,147 B` | `1,020★` | `2026-11-03` | 🔴 Copyleft, actively maintained. |
| Kolibri | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | `LICENSE`, `1,097 B` | `1,167★` | `2026-11-02` | 🟢 **Buildable.** 🔴 Default branch is `develop` (`630-J`). |
| LiaScript | [`LiaScript/LiaScript`](https://github.com/LiaScript/LiaScript) | 🟢 `BSD-3-Clause` | `LICENSE`, `1,523 B` | `287★` | `2026-11-03` | 🟢 **Buildable.** 🔴 Default branch is `development` (`630-J`). |
| Great Reading Adventure | [`MCLD/greatreadingadventure`](https://github.com/MCLD/greatreadingadventure) | 🟢 `MIT` | `LICENSE`, `1,088 B` | `17★` | `2026-09-28` | 🟢 **Buildable** — a public-library reading-program system of record. |

🟢 **Three of the eight carry a permissive grant** — Kolibri, LiaScript and Great Reading Adventure — plus
Sakai under `ECL-2.0`. 🔴 The four largest by stars are all copyleft, and that has been stable across this
base's history: **the installed base of education platforms is GPL/AGPL, and the permissive layer is the
newer and smaller one.**

🔴 **Still a declared gap: no open-source SIS under a permissive grant.** The leg searched for one explicitly
(`LMS SIS MIT Apache`) and returned no permissive student-information system; what it returned instead was a
vendor comparison asserting its own product is *"the only platform … that integrates LMS with SIS, fees and
parent app on one database"*, with **no licence stated**. 🟢 Recorded as unmeasured rather than filled.

## 🆕 `p629` — reads `2026-11-03` — **🟢 THE VERTICAL SHELF GAINS A CATEGORY THE SECTOR'S PLATFORMS DO NOT COVER: THE **VIRTUAL SCIENCE LAB**, WHICH NO LMS SHIPS AND EVERY SCIENCE CURRICULUM NEEDS. 🔴 AND THE ERP/CRM LEG — RETIRED AT `619-B` AFTER FOUR NILS — WAS RE-RUN ONCE AS A CONTROL AND RETURNED `0 of 6` UNHELD FOR A FIFTH TIME, WHICH CLOSES THE QUESTION.**

### 🟢 The platform tier — unchanged, and re-stated because engagements quote it

🔵 No row below changed its grant this pass. `p628` measured the maintenance split and it stands: **Open edX and
Moodle were pushed this week; Canvas has not accepted a push in `187` days.**

| Platform | Repo | Licence | Role |
|---|---|---|---|
| Moodle | [`moodle/moodle`](https://github.com/moodle/moodle) | `GPL-3.0` | The sector's default LMS. 🔵 Copyleft — integrate across the LTI boundary (`626-N`). |
| Open edX | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | `AGPL-3.0` | MOOC-scale LMS. 🔵 Canonical address since `625-F`/`626-A`'s rename. |
| Sakai | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 `ECL-2.0` | Higher-ed LMS. 🟢 `ECL-2.0` is education's Apache-derivative and `624-D` proved it adds **no obligation** over `Apache-2.0` — **buildable**. 🔴 Not `Apache-2.0`, which a web leg asserted at `628-I`. |
| OpenEduCat | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `LGPL-3.0` | Education **ERP** on Odoo — SIS, attendance, fees, timetabling. |
| Frappe Education | [`frappe/education`](https://github.com/frappe/education) | `AGPL-3.0` | Education module on the ERPNext stack; inherits ERP + CRM. |
| RosarioSIS | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `GPL-2.0` | K-12 student information system, PHP + PostgreSQL. |
| openSIS | [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | `GPL-2.0` | SIS for K-12, trade schools and higher ed. |
| Gibbon | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `GPL-3.0` | School management for schools and education departments. |
| QTIWorks | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 `BSD-3-Clause` | QTI assessment delivery engine. 🟢 Confirmed on bytes at `628-F` (metadata says `NOASSERTION`); the **only fully permissive assessment tier** this base holds. |
| Kolibri | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | Offline-first learning platform for low/no-connectivity deployments; UNESCO-documented in Uganda refugee settlements. |

### 🟢 New vertical category — the virtual science lab

🔵 **Why it is a category and not a feature:** every platform above manages *enrolment, content and assessment*.
**None of them simulates an experiment.** A science curriculum without lab access therefore has no open-source
answer inside its own LMS, and the gap is permissive and live.

| Solution | Repo | Licence | Customisation surface |
|---|---|---|---|
| ScienceLab 3D | [`rudra496/sciencelab3d`](https://github.com/rudra496/sciencelab3d) | 🟢 `MIT` | `40+` experiments, Next.js + TypeScript + Three.js. Browser-delivered, so it embeds in Moodle/Open edX via LTI without touching their copyleft. `25★`, pushed `2026-11-01`. |
| VirtualChemLab | [`qilaidev/virtual-chem-lab`](https://github.com/qilaidev/virtual-chem-lab) | 🟢 `MIT` | Python + PySide6/Qt6 **desktop** — runs where there is no browser and no network. Bilingual (EN/中文). `2★`. |
| Ta3alam | [`ahmadarrabee/Ta3alam`](https://github.com/ahmadarrabee/Ta3alam) | 🟢 `MIT` | Offline-first education **server** — the delivery substrate the two labs above need in a disconnected school. `0★`. |
| open-aac | [`svankamamidi/open-aac`](https://github.com/svankamamidi/open-aac) | 🟢 `Apache-2.0` | AAC board with picture search + drag-and-drop editing; the accessibility surface no LMS above ships. 🔴 Default branch `search_for_picture`. |

🔴 **Maturity flag, stated plainly:** three of these four are `0`–`2★`. As **vertical solutions** they are patterns
and starting code, not products — unlike Moodle or Odoo, a client cannot be handed one and told it is supported.

### 🔴 The ERP/CRM leg: retired at `619-B`, re-run once, nil a fifth time

🟢 The mandated vertical-platform leg was run once more as a **control on the retirement decision**, not in hope:
`open source platform education ERP CRM MIT Apache student information system`. It returned `6` names —
OpenEduCat, RosarioSIS, Frappe Education, openSIS, Gibbon, Fedena — and 🔴 **`0` were unheld.**

🔴 **And the leg repeated `619-J`'s fourth channel-failure shape on the way.** It described **Fedena** as *"a
free, open-source school management package"*. Measured:
[`projectfedena/fedena`](https://github.com/projectfedena/fedena) is `547★` with 🔴 **no licence at all** and last
pushed `2020-05-18` — **`6.5` years quiet**; [`foradian/fedena`](https://github.com/foradian/fedena) is `4★`, no
grant, last pushed `2012-10-12`. 🟢 Only the smaller forks
[`projectfedena/project_fedena`](https://github.com/projectfedena/project_fedena) (`66★`, `Apache-2.0`, `2019`) and
[`mazhar266/fedena`](https://github.com/mazhar266/fedena) (`5★`, `Apache-2.0`, `2019`) carry a grant, and all of
them are abandoned. 🔵 **"Open source" in a digest is a description of intent, not a grant** — this is the fifth
instance of a channel asserting a licence for a tree that has none, and it is the shape that would have shipped.

🔴 **The licence picture the leg returns is the standing finding of this tier, not news:** every education ERP/SIS it
surfaced is `GPL`/`LGPL`/`AGPL`. 🔵 There is **no permissive education ERP**, five legs deep. The operative is
unchanged and now five-times evidenced: **build the AI layer permissively and meet the ERP across a process or LTI
boundary** — never inside its source tree.

## 🆕 `p628` — reads `2026-11-03` — **🔴 THE SECTOR'S TWO CANONICAL LMS PLATFORMS HAVE DIVERGED ON MAINTENANCE: OPEN edX AND MOODLE WERE PUSHED THIS WEEK, CANVAS HAS NOT ACCEPTED A PUSH IN `187` DAYS. 🟢 AND THE QTI ASSESSMENT TIER IS CONFIRMED PERMISSIVE ON BYTES.**

### 🔴 Platform maintenance, measured today — the fact that decides a platform recommendation

| Platform | Repo | 🟢 Stars | Licence | Pushed | Verdict |
|---|---|---|---|---|---|
| **Open edX** | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | `8,216` | `AGPL-3.0` | 🟢 `2026-11-03` | 🟢 **active** — stewarded by Axim Collaborative |
| **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | `9,263` | `LGPL-3.0` | 🟢 `2026-11-03` | 🟢 **active** — virtual classroom |
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | `7,575` | `GPL-3.0` | 🟢 `2026-10-30` | 🟢 **active** |
| **Canvas LMS** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `6,900` | `AGPL-3.0` | 🔴 `2026-04-30` | 🔴 **`187` days / `6.1` months quiet** |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `1,240` | 🟢 `ECL-2.0` | 🟢 `2026-11-02` | 🟢 **active** — permissive |
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `1,166` | 🟢 `MIT` | 🟢 `2026-11-02` | 🟢 **active** — offline-first |
| **Tsugi** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | `377` | 🟢 `Apache-2.0` | 🟢 `2026-11-03` | 🟢 **active** — LTI 1.3 broker |
| **H5P** | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | `154` | `GPL-3.0` | 🟢 `2026-11-02` | 🟢 **active** — interactive content |
| **Sunbird (User/Org)** | [`Sunbird-Lern/userorg-service`](https://github.com/Sunbird-Lern/userorg-service) | `31` | 🟢 `MIT` | `2026-03-02` | 🟢 India DPI tier (`628-C`) |
| **QTIWorks** | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | `3` | 🟢 `BSD-3-Clause` (bytes) | `2026-06-30` | 🟢 QTI engine, **buildable** (`628-F`) |

🔴 **Canvas is the finding.** It is one of the two platforms every higher-education engagement asks about, and its
open-source repository has been static for half a year while Moodle and Open edX both took pushes this week.
🟢 **Recommendation:** lead with Moodle (institutional familiarity) or Open edX (course-scale, Axim-stewarded);
if a client is already on Canvas, scope against the commercial SaaS and **not** against the AGPL repository.

### 🟢 The permissive customisation surface, after this pass

🟢 Five platform-tier rows carry grants Globant can build on and ship: **Sakai** (`ECL-2.0`), **Kolibri**
(`MIT`), **Tsugi** (`Apache-2.0`), **Sunbird userorg-service** (`MIT`) and **QTIWorks** (`BSD-3-Clause`).
🔵 `624-D` byte-proved `ECL-2.0` adds **no obligation** over `Apache-2.0`, so Sakai is a genuine permissive LMS —
the only one at platform scale on this shelf, and worth saying out loud because the web digests get it wrong
(one called it `Apache-2.0` this pass; `628-I`).

🔴 **The copyleft tier is for integration, not embedding:** Moodle (`GPL-3.0`), Open edX and Canvas (`AGPL-3.0`),
BigBlueButton (`LGPL-3.0`), H5P (`GPL-3.0`). Cross the boundary with LTI 1.3, xAPI or REST — never by linking
client-proprietary code into the tree. 🟢 Tsugi exists precisely to be that boundary and is `Apache-2.0`.

### 🔴 An unmaintained tier a client should be warned off

🔴 **Unity + xAPI:** [`adlnet/Unity-xAPI-Wrapper`](https://github.com/adlnet/Unity-xAPI-Wrapper) is archived
read-only (`2026-03-26`) and its parent is four years quiet. 🟢 Emit xAPI statements from a thin in-house client
against the spec instead; do not adopt either address.

## 🆕 `p627` — reads `2026-11-03` — **🟢 `7` ADDRESS CORRECTIONS ON THIS SHELF, INCLUDING THE FRENCH ENT PLATFORM ROW AND `6` OCCURRENCES OF THE OPEN edX PLATFORM ADDRESS.**

### 🟢 Corrections applied to this shelf's table rows

| Was cited | 🟢 Canonical today | Proof (`HEAD`) | Metadata |
|---|---|---|---|
| `opendigitaleducation/entcore` | [`edificeio/entcore`](https://github.com/edificeio/entcore) | `933435ba7acc` | `24★` `NOASSERTION` pushed `2026-11-02` |
| `openedx/edx-platform` | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | `f2fc446def69` | `8,216★` `AGPL-3.0` pushed `2026-11-02` |

🟢 **The `entcore` correction matters regionally.** It is the platform behind French regional *ENT* deployments and
the row is the EMEA sovereignty pick on this shelf; `opendigitaleducation` → `edificeio` is an organisation rename
(same `HEAD`), so the old address still resolves and quietly misattributes the publisher in any client document
that cites it.

🔴 **`edificeio/entcore` reads `NOASSERTION`.** `24★` is also thin for a platform row. 🟢 Sell it as *the* French
ENT integration target — which it is — but do not sell it as a permissive base until the grant is byte-read.

### 🔵 Vertical platform currency, checked today

| Platform | Licence | Stars | Pushed | Verdict |
|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | `GPL-3.0` | `7,574` | `2026-10-30` | 🟢 current |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | `AGPL-3.0` | `8,216` | `2026-11-02` | 🟢 current |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `GPL-3.0` | `1,020` | `2026-11-03` | 🟢 pushed today |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `ECL-2.0` | `1,240` | `2026-11-02` | 🟢 current |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `MIT` | `1,166` | `2026-11-02` | 🟢 current, permissive |
| [`oppia/oppia`](https://github.com/oppia/oppia) | `Apache-2.0` | `6,957` | `2026-11-02` | 🟢 current, permissive |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `AGPL-3.0` | `6,900` | 🔴 `2026-04-30` | 🔴 six months quiet |

🔴 **Canvas is the only incumbent going quiet**, now reproduced on a third separate day with the metadata channel.
🟢 `archived=false`, so this is a *cadence* signal rather than an end-of-life announcement — but it is the
migration argument, and `627-H` prices it for North America.

🟢 **Only `kolibri` (`MIT`) and `oppia` (`Apache-2.0`) are permissive.** Everything else on this shelf is copyleft,
which is why the LTI boundary in `compose/patterns.md` `627-K` is the load-bearing pattern for this industry.


## 🆕 `p626` — reads `2026-11-03` — **🔴 THE FRENCH ENT ROW ON THIS PAGE CITES A STALE ADDRESS AND IS NOW FLAGGED: THE CANONICAL HOME IS `edificeio/entcore`, PUSHED `2026-11-02`. 🟢 THE VERTICAL PLATFORM TIER IS OTHERWISE UNCHANGED AND FRESH — EVERY PLATFORM BELOW EXCEPT CANVAS PUSHED WITHIN FOUR DAYS.**

🔵 Method and controls: `agents/top.md` `626-A`…`626-E`.

### 🔴 The address correction that affects a recommendation on this page

| Cited here | Status `2026-11-03` | Action |
|---|---|---|
| [`edificeio/entcore`](https://github.com/edificeio/entcore) | 🔴 **STALE** — canonical [`edificeio/entcore`](https://github.com/edificeio/entcore), `24★`, pushed `2026-11-02`, identical `HEAD` | 🟢 Flagged in place at `622-D2` |

🔴 **This base already held the pair** in `compose/code/p406-carried-existence/README.md:144` and never propagated
it to the page that sells the row. 🔴 And `agents/top.md:788` filed the very same address as a *"channel B miss
(`422`)"* — the `422` was the channel **reporting the rename**, not failing (`626-B`).
🔵 The branding obligation `622-D2` found in its grant is unaffected; the field still reads `NOASSERTION`.

### 🟢 The vertical platform tier — real systems that can be customised with AI on top, measured `2026-11-03`

| Platform | Repo | Licencia | ★ | `pushed_at` | What it actually is |
|---|---|---|---|---|---|
| **Open edX** | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 🔴 `AGPL-3.0` | `8,216` | `2026-11-02` | MOOC-grade LMS. 🟢 **Canonical address corrected this pass** |
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 `GPL-3.0` | `7,574` | `2026-10-30` | The world's largest LMS install base; plugin API is the integration surface |
| **Oppia** | [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 `Apache-2.0` | `6,957` | `2026-11-02` | 🟢 The **permissive** large platform — structured interactive lessons |
| **Canvas** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 `AGPL-3.0` | `6,900` | 🔴 `2026-04-30` | 🔴 **Six months quiet.** Migrate off, don't build on |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 `ECL-2.0` | `1,240` | `2026-11-02` | Apereo higher-ed LMS; `ECL-2.0` proven buildable (`624-E`) |
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | `1,166` | `2026-11-02` | 🟢 **Offline-first** — the low-connectivity answer |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🟡 `GPL-3.0` | `1,020` | 🟢 `2026-11-03` | **Pushed today.** Strong LATAM install base |
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 field `NOASSERTION` / 🟡 bytes `LGPL-3.0` | `903` | `2026-11-02` | 🟢 **The education ERP** — built on Odoo; admissions, fees, HR, CRM |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 `ECL-2.0` | `509` | `2026-11-02` | Lecture capture and video pipeline |
| **ENT Core** | [`edificeio/entcore`](https://github.com/edificeio/entcore) | 🔴 `NOASSERTION` | `24` | `2026-11-02` | French school ENT estate; 🔴 branding obligation in grant |
| **Tsugi** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 `Apache-2.0` | `377` | `2026-11-02` | 🟢 **LTI framework** — reaches *any* conformant LMS |
| **scorm-again** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | `362` | `2026-11-02` | SCORM / AICC / xAPI runtime |
| **ibl LMS** | [`iblai/lms`](https://github.com/iblai/lms) | 🟢 `MIT` | `208` | `2026-11-02` | Open edX-derived under a **permissive** grant |

### 🟢 The licence shape of this tier, restated because it decides the engagement

🔴 **Every large platform of record is reciprocal** — `AGPL-3.0` (Open edX, Canvas) or `GPL-3.0` (Moodle, Chamilo).
🟢 **The permissive options are real but smaller**: `oppia` (`Apache-2.0`, `6,957★`) is the only large one;
`kolibri`, `iblai/lms` and `scorm-again` are `MIT`; `sakai` and `opencast` are `ECL-2.0`.

> 🟢 **The pattern that keeps Globant's work permissive on a reciprocal platform:** build at the **LTI boundary**
> with `tsugi` (`Apache-2.0`) rather than inside the platform tree. The AI service stays a separate, independently
> licensed tool that any conformant LMS can launch — Moodle, Open edX, Sakai or Canvas — and no reciprocal grant
> reaches it. 🔵 This is the recipe `compose/patterns.md` `626-M` specifies end to end.

---

## 🆕 `p625` — reads `2026-11-02` — **THE VERTICAL SHELF RE-MEASURED, AND THE CUSTOMIZATION ENTRY POINT MOVES FROM *PLUGINS* TO *STANDARDS*: `tsugi` (`Apache-2.0`) + `scorm-again` (`MIT`) REACH EVERY PLATFORM BELOW WITHOUT FORKING ANY OF THEM**

### 🟢 Plataformas verticales — medidas `2026-11-02`

| Plataforma | Repo | Licencia | ★ | `pushed_at` | Stack | Caso de uso |
|---|---|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 `GPL-3.0` (bytes) | `7,574` | `2026-10-30` | PHP + MySQL/PgSQL | LMS universal: K-12, HE, corporativo. `tool_ai` 4.5+ |
| **Open edX** | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 🔴 `AGPL-3.0` (bytes) | *n/d — canal `NO-ROW`* | — | Python/Django + React | MOOC, corporativo, gobierno. XBlock |
| **Oppia** | [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 `Apache-2.0` (bytes) | `6,957` | `2026-11-02` | Python/Angular | 🟢 **La plataforma grande más permisiva.** Lecciones estructuradas, K-12 |
| **Canvas LMS** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 `AGPL-3.0` (bytes) | `6,900` | 🔴 **`2026-04-30`** | Ruby on Rails | ⚠️ Incumbente NA. **Árbol OSS frío 6 meses** |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 `ECL-2.0` (bytes) | `1,240` | `2026-11-02` | Java/Spring | LMS institucional universitario. `ECL-2.0` = `Apache-2.0` en obligaciones (`624-E`) |
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` (bytes) | `1,166` | `2026-11-02` | Python/Vue | 🟢 **Offline-first.** Conectividad baja, rural, refugiados |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🟡 `GPL-3.0` (bytes) | `1,020` | `2026-11-02` | PHP | LMS ligero. Base instalada fuerte en LATAM público |
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 `LGPL-3.0` (bytes) | `903` | `2026-11-02` | Odoo (Python) | 🟢 **El "Odoo de educación":** ERP completo — admisiones, SIS, gradebook, biblioteca |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 `ECL-2.0` (bytes) | `509` | `2026-11-02` | Java | Captura de clase, transcripción, publicación |
| **ELMS:LN** | [`elmsln/elmsln`](https://github.com/elmsln/elmsln) | 🟡 `GPL-3.0` | `253` | `2026-08-14` | PHP/Drupal | Penn State. Infraestructura de cursos distribuida |

🔵 **Capa de integración — y aquí está lo permisivo:**

| Componente | Repo | Licencia | ★ | Qué resuelve |
|---|---|---|---|---|
| **Tsugi** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 `Apache-2.0` | `377` | 🟢 **LTI 1.3 / Advantage.** Una integración → Moodle, Canvas, Blackboard, Sakai, D2L, Open edX |
| **scorm-again** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | `362` | 🟢 **SCORM 1.2 / 2004 + AICC** en browser. Puente al courseware heredado |
| **H5P** | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🟡 `GPL-3.0` (bytes) | — | Tipos de contenido interactivo embebibles |
| **ibl.ai LMS** | [`iblai/lms`](https://github.com/iblai/lms) | 🟢 `MIT` | `208` | Inteligencia de skills y competencias bajo `MIT` |

### 🟢 Cómo customizar con AI — el patrón que las licencias **sí** permiten

🔴 **El error estructural a evitar:** forkear la plataforma. Moodle es `GPL-3.0`, Open edX y Canvas son `AGPL-3.0`
— y `AGPL` alcanza el **uso en red**, no sólo la distribución. Un fork convierte la capa de agentes de Globant en
obra derivada con obligación recíproca.

🟢 **El patrón correcto — hablar estándares, cruzar un límite de red:**

```
┌─ Plataforma del cliente (GPL / AGPL / LGPL / ECL) ── NO SE TOCA, NO SE FORKEA ─┐
│   Moodle · Open edX · Canvas · Sakai · Chamilo · OpenEduCat                    │
└───────────────┬────────────────────────────────────────────────────────────────┘
                │  LTI 1.3 / Advantage  (tsugi, Apache-2.0)
                │  SCORM 1.2 / 2004     (scorm-again, MIT)
                │  xAPI / Caliper        (analítica de aprendizaje)
                ▼  ── límite de red + estándar publicado ──
┌─ Capa Globant: MIT / Apache-2.0, IP separable ────────────────────────────────┐
│   Tutoría: DeepTutor (Apache-2.0) · OpenMAIC (MIT) · OpenTutor (MIT)          │
│   Docencia: ai-shifu (Apache-2.0) · Papermorph (MIT) · claudemy (MIT)         │
│   Competencias: iblai/lms (MIT)                                               │
│   Gobernanza: registro de decisiones, trazas, FRIA (ver intel/market.md)      │
└───────────────┬───────────────────────────────────────────────────────────────┘
                ▼
[Kolibri (MIT) para entrega offline donde el ancho de banda es la restricción]
```

🟢 **Por qué esto es lo vendible:** la pregunta "¿qué LMS usa el cliente?" deja de ser bloqueante y pasa a ser
configuración. Una sola integración LTI cubre el parque instalado completo, y la IP de la capa de agentes queda
limpia y permisiva. 🔵 Es también la ruta más rápida: no hay que esperar el ciclo de release de la plataforma.

### 🔴 Señal de mercado nueva en esta vertical: el árbol OSS de Canvas se está enfriando

🔴 `instructure/canvas-lms` — último push **`2026-04-30`**, seis meses. 🟢 Medido contra `moodle`, `oppia`, `sakai`,
`kolibri`, `chamilo`, `openeducat_erp` y `opencast`, **todos con push hoy o esta semana**.

🟢 **Lectura comercial:** el producto comercial de Canvas envía AI; su repositorio abierto no. Para un cliente sobre
Canvas, la salida open-source se está cerrando — lo que **refuerza** la jugada de migración a Open edX o Moodle con
capa agéntica, y la vuelve más urgente. 🔴 **Caveat honesto:** un `pushed_at` frío no es abandono (puede haber
desarrollo interno sin publicar). Re-medir antes de usarlo en una propuesta.

### 🟡 Fuera del mandato permisivo, listadas porque existen y el cliente preguntará

🔴 `AGPL-3.0`: [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) (`2,441★`),
[`classroomio/classroomio`](https://github.com/classroomio/classroomio) (`1,736★`),
[`artcc/freelingo`](https://github.com/artcc/freelingo) (`225★`),
[`JudgePeach/math-question-bank`](https://github.com/JudgePeach/math-question-bank) (`368★`).
🔴 `NOASSERTION` — **no construir hasta leer bytes**: [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM)
(`2,060★`), [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) (`340★`).
🔴 **NonCommercial, confirmado en bytes por `p615`**: [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy)
(`6,211★`, `CC-BY-NC-4.0`) — el grafo de conocimiento más rico del sector y **no se puede usar comercialmente**.

## 🆕 `p624` — reads `2026-11-02` — **🟢 THE WHOLE PLATFORM TIER'S GRANTS ARE RE-ESTABLISHED BY **ENUMERATION**, AND THE TIER GAINS ITS FIRST `AGPL-3.0` CHINESE PLATFORM. 🟢 `ECL-2.0` IS NOW CLAUSE-DIFFED AGAINST `Apache-2.0` AND ADDS **NO OBLIGATION** — SO SAKAI AND OPENCAST ARE THE TIER'S ONLY TRULY SHIPPABLE BASES. 🔴 AND THE `621 B` FILE THAT WOULD HAVE HIDDEN CANVAS'S NETWORK COPYLEFT IS NAMED.**

### 🟢 The vertical platform tier — every grant **enumerated**, not guessed, and byte-read today

🔵 Real, customisable systems — the Odoo / OpenMRS / Moodle class the brief asks for. 🟢 Method: `624-A`.
Branch is the repository's actual default, because five of these are not `main`.

| Platform | What it runs | Grant (enumerated + byte-read) | Bytes | Branch | ★ | Pushed | AI-on-top verdict |
|---|---|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | LMS — largest installed base in education | 🟡 `GPL-3.0` in **`COPYING.txt`** | `35,147` | `main` | `7,574` | `2026-10-30` | 🟢 **Best AI target in the tier.** The plugin API keeps client code outside the copyleft boundary; the `moodle-*-mcp` wave sits here |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | LMS / MOOC at scale | 🔴 `AGPL-3.0` | `35,136` | `master` | 🔴 channel-blind (`623-O`) | — | 🔴 Self-host and extend; the **network clause** must be cleared before any hosted client offering |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | Higher-ed LMS / collaboration | 🟢 **`ECL-2.0`** + a `licenses/` tree | `11,120` | `master` | `1,240` | `2026-11-02` | 🟢 **The tier's cleanest base for a shipped derivative** — and `624-E` now proves why |
| [`opencast/opencast`](https://github.com/opencast/opencast) | Lecture capture, media pipeline | 🟢 **`ECL-2.0`** + `NOTICES` | `11,340` / `126,439` | `develop` | `509` | `2026-11-02` | 🟢 Permissive. Natural host for transcription / captioning / indexing agents. 🟡 That `126 KB` `NOTICES` roll is a real attribution duty |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | Offline-first learning platform | 🟢 `MIT` | `1,097` | `develop` | `1,166` | `2026-11-02` | 🟢 **Permissive.** The low-connectivity anchor — LATAM, EMEA-Africa, rural APAC |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | Education ERP / SIS on Odoo | 🟡 `LGPL-3.0` | `8,241` | **`19.0`** | `903` | `2026-11-02` | 🟡 The Odoo-for-education answer. 🟢 `623-F`'s dangle is **settled and downgraded** — see below |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | LMS, strong LATAM + francophone footprint | 🟡 `GPL-3.0` + `license.txt` | `35,147` / `1,614` | `master` | `1,020` | `2026-11-02` | 🟡 Copyleft, very actively pushed. 🔵 Holder is **BeezNest Latino**, in the second file |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | LMS — large NA higher-ed share | 🔴 `AGPL-3.0` + `COPYRIGHT` (`621 B`) | `34,520` / `621` | `master` | `6,900` | 🔴 **`2026-04-30`** | 🔴 Network copyleft **and** `6` months without a push |
| [`oppia/oppia`](https://github.com/oppia/oppia) | Interactive lesson platform | 🟢 **`Apache-2.0`** + `NOTICE` | `11,358` / `146` | `develop` | `6,957` | `2026-11-02` | 🟢 **Permissive and the most actively pushed platform here.** Carry the `NOTICE` under §4 |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | Next-gen OSS learning platform | 🔴 `AGPL-3.0` | — | `main` | `2,441` | `2026-11-02` | 🔴 Modern stack, network copyleft |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | Customer-training / course platform | 🔴 `AGPL-3.0` | — | `main` | `1,736` | `2026-11-02` | 🔴 Closest OSS fit for SaaS customer-education; licence blocks resale-as-a-service |
| 🆕 [`roncoo/roncoo-education`](https://github.com/roncoo/roncoo-education) | Online-education system (CN): VOD, live, exams, question bank, tasks | 🔴 **`AGPL-3.0`**, byte-read | `35,184` | `master` | `1,567` | `2026-10-13` | 🔴 **New to this tier.** A complete China-market platform; the open edition is a trimmed commercial product — 🟡 dual-licence posture, so a commercial grant may be purchasable |
| [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | Interactive content engine | 🟡 `GPL-3.0` (`LICENSE.txt`) | `35,146` | `master` | `154` | `2026-11-02` | 🟡 Embeds in Moodle / Canvas / Drupal; copyleft |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | Assignment release + autograding | 🟢 **`BSD-3-Clause`** | — | `main` | `1,370` | `2026-10-28` | 🟢 Permissive. The grading substrate for any CS / data curriculum |
| [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | Secure automated exercise assessment | 🟡 `NOASSERTION` (channel B) | — | `master` | `243` | `2026-11-02` | 🟡 Sandboxed code grading. 🔴 Grant **not** byte-read this pass — do not rely on the column |

### 🟢 `624-E` applied here — the tier's licence question is finally answered, not deferred

🔵 `p623` named `ECL-2.0` and flagged that its relation to `Apache-2.0` was *assumed*, not diffed. 🟢 **The
diff was run on bytes this pass** ([`../agents/top.md`](../agents/top.md) `624-E`): `78` words added, `9`
removed; the addition is **one contiguous `60`-word run** appended to §3, and §4's four redistribution
conditions were read in full in both texts and are **all present** in `ECL-2.0`.

> 🟢 **Verdict for this page.** `ECL-2.0` **adds no obligation** over `Apache-2.0`; it *narrows a patent grant
> you receive* from institutionally-employed contributors. 🟢 So **Sakai and Opencast are the only platforms
> in this tier a studio can fork, modify and ship as a closed derivative with Apache-grade freedom** —
> which is a materially different offer from everything else here. 🟡 The residual: do not price patent
> indemnity against academic contributors whose institution never had the right to grant it.

### 🟢 `623-F` settled — the openeducat dangle is **cosmetic**, and enumeration is what settled it

| Probe | Result |
|---|---|
| `openeducat_erp` `LICENSE` opens with | *"For copyright information, please see the COPYRIGHT file."* |
| `COPYRIGHT` anywhere in the tree (`1,345` tracked paths) | 🟢 **`0` — absence proven by enumeration** |
| Grant stated in the **same** `8,241 B` file? | 🟢 **Yes** — `GNU LESSER GENERAL PUBLIC LICENSE, Version 3`, full text included below the pointer |

🟡 **Downgraded 🔴 → 🟡.** Nothing is missing but a pointer to a file that was never shipped. The row is
`LGPL-3.0` and is safe to rely on. 🔵 `p623` was right to flag it and right to refuse to settle it on a `404`.

### 🔴 `624-N1` — the `621 B` file that would have hidden Canvas's network copyleft

🔵 A filename ladder ordered as `p622` ordered it reaches `COPYRIGHT` **before** `LICENSE`. 🔴 On
`instructure/canvas-lms` that returns a `621 B` Instructure notice as the grant. 🟢 Enumeration returns
**both** files, and the real one is `LICENSE`, `34,520 B`, `GNU AFFERO GENERAL PUBLIC LICENSE`.

> 🔴 **Concretely: a studio that trusted the ladder could have built a hosted Canvas offering believing the
> licence was a short permissive notice.** That is the same error class as `623-H`'s `idurar` (`MIT` claimed,
> `AGPL-3.0` in fact) — reached this time not from a bad digest but from a **good instrument in the wrong
> order**. 🟢 Enumeration has no order to get wrong.

### 🔴 Carried from `623-H` — the digests' permissive claims, still wrong

| Platform | Digest claimed | Bytes say |
|---|---|---|
| [`idurar/idurar-erp-crm`](https://github.com/idurar/idurar-erp-crm) | 🔴 `MIT` | 🟢 `AGPL-3.0`, `34,230 B` |
| [`hcengineering/platform`](https://github.com/hcengineering/platform) (Huly) | 🔴 `Apache-2.0` | 🟢 `EPL-2.0`, `14,197 B` |
| [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | 🟡 both `Apache-2.0` **and** `GPLv2` | 🟢 `Apache License`, `11,906 B` |

🔵 Running total across `p623`–`p624`: **`5 of 5`** checkable licence claims in the mandated digests were
wrong or unresolvable. 🟢 The digest surfaces the *name*; only the bytes may fill the *licence* column.

### 🟡 Declared gaps

- 🔴 **No permissively-licensed education ERP / SIS exists**, as far as six legs can see. The Odoo-for-education
  answer is `LGPL-3.0` (`openeducat`); every other integrated platform found is `AGPL-3.0` or `GPL-3.0`.
  🟢 The permissive column in this industry is **tooling and agents**, not platforms.
- 🔴 `INGInious` and `inducer/relate` carry `NOASSERTION` and were **not** byte-read this pass. Their licence
  cells are explicitly unreliable; `624-H` is why that matters.

## 🆕 `p623` — reads `2026-11-02` — **🔴 THE VERTICAL FINDING IS THAT THE SEARCH DIGEST A PASS IS *INSTRUCTED* TO RESEARCH WITH GOT `2 of 2` PERMISSIVE-LICENCE CLAIMS WRONG, BOTH IN THE DIRECTION THAT INVITES A STUDIO TO BUILD ON COPYLEFT. 🟢 AND THE EDUCATION-SPECIFIC PLATFORM TIER HAS ITS OWN PERMISSIVE LICENCE FAMILY, `ECL-2.0`, WHICH THIS BASE HAD NEVER NAMED.**

### 🔴 `623-H` (carried) — the digest said `MIT`; the bytes said `AGPL-3.0`

🔵 The mandated leg `open source platform {industry} ERP CRM MIT Apache` returned two platforms under
**explicit** permissive claims, which is exactly what the leg is for. 🔴 **Both claims are false.**

| Platform | What the digest asserted | Byte-read grant, `2026-11-02` | Consequence if the digest had been trusted |
|---|---|---|---|
| [`idurar/idurar-erp-crm`](https://github.com/idurar/idurar-erp-crm) | 🔴 *"fully open-source under the **MIT** license"* | 🟢 `GNU AFFERO GENERAL PUBLIC LICENSE`, `34,230 B`, `master` | 🔴 A hosted client ERP built on `AGPL-3.0` under the belief it was `MIT` — **the worst licence error available** |
| [`hcengineering/platform`](https://github.com/hcengineering/platform) (Huly) | 🔴 *"**Apache 2.0** licensed"* | 🟢 `Eclipse Public License - v 2.0`, `14,197 B`, `develop` | 🟡 `EPL-2.0` is weak copyleft with a source-availability duty — survivable, but not what was promised |

🔵 The same leg also raised a **conflict it could not settle itself** — one source calling Apache
OFBiz `Apache-2.0` and another calling its GitHub code `GPLv2`. 🟢 **Settled by bytes:**
`apache/ofbiz-framework`, branch `trunk`, `LICENSE` `11,906 B`, title `Apache License`. The `GPLv2`
claim is wrong.

> 🟢 **This is the quality bar working as designed.** The digest surfaces the *name*; only the bytes
> may fill the *licence column*. `3 of 3` licence claims from this pass's digests were wrong or
> unresolvable, and `3 of 3` were settled by one `raw.githubusercontent.com` read each.

### 🟢 The vertical platform tier, every grant byte-read today

🔵 Real, customisable systems — the Odoo/OpenMRS/Moodle class the brief asks for — with the branch
each one actually defaults to, because three of them are not `main`.

| Platform | What it runs | Grant (byte-read) | Branch | ★ | AI-on-top verdict |
|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | LMS — the industry's largest installed base | 🟡 `GPL-3.0`, `35,147 B` in `COPYING.txt` | `main` | `7,574` | 🟢 **Best AI target in the tier.** Plugin API keeps client code out of the copyleft boundary; the whole `moodle-*-mcp` wave this base tracks sits here |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | LMS / MOOC at scale | 🟡 `AGPL-3.0`, `35,136 B` | `master` | 🔴 channel-blind (`623-O`) | 🟡 Self-host and extend; **AGPL network clause** must be cleared before any hosted client offering |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | Higher-ed LMS / collaboration | 🟢 **`ECL-2.0`**, `11,120 B` | `master` | `1,240` | 🟢 **Permissive.** The tier's cleanest base for a shipped derivative product |
| [`opencast/opencast`](https://github.com/opencast/opencast) | Lecture capture, media pipeline | 🟢 **`ECL-2.0`**, `11,340 B` | `develop` | `509` | 🟢 Permissive. Natural host for transcription/captioning/indexing agents |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | Offline-first learning platform | 🟢 `MIT`, `1,097 B` | `develop` | `1,165` | 🟢 **Permissive.** The low-connectivity anchor — LATAM, EMEA-Africa, rural APAC |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | Education ERP / SIS on Odoo | 🟡 `LGPL-3.0`, `8,241 B` | **`19.0`** | `903` | 🟡 The Odoo-for-education answer. 🔴 Its `LICENSE` points at a `COPYRIGHT` file that **`404`s** (`623-F`) |
| [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | K-12 school ERP | 🟢 `MIT`, `1,150 B` | `main` | `55` | 🟢 Permissive and small enough to fork outright. 🔴 Channel B calls it `NOASSERTION` and is wrong (`623-G`) |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | Virtual classroom / conferencing | 🟡 `LGPL-3.0`, `7,652 B` | **`v4.0.x-develop`** | `9,263` | 🟡 Integrate, don't embed. Moodle/Sakai-native |
| [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | ERP/CRM spine | 🟢 `Apache-2.0`, `11,906 B` | **`trunk`** | `1,148` | 🟡 Permissive but **no education module** — a build-from-spine option, not a vertical product |
| [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | CRM (admissions / enrolment funnel) | 🟢 `MIT`, `1,078 B` | **`2.2`** | `24,095` | 🟢 Permissive. The admissions-CRM layer an education ERP usually lacks |
| [`idurar/idurar-erp-crm`](https://github.com/idurar/idurar-erp-crm) | ERP/CRM | 🔴 `AGPL-3.0`, `34,230 B` | `master` | `8,934` | 🔴 **Do not use for a hosted client build.** Shelved here only to correct the digest (`623-H`) |
| [`hcengineering/platform`](https://github.com/hcengineering/platform) (Huly) | All-in-one PM / collaboration | 🟡 `EPL-2.0`, `14,197 B` | `develop` | `28,042` | 🟡 Not education-specific; weak copyleft with source-availability duty |

### 🟢 `623-R` — the content/code split, fourth instance, and the first where the content licence is a **government** licence

🔵 `622-I` established that the code/content split is carried on three instances and that *"the
content is NonCommercial"* is the wrong way to state it. 🟢 **Instance four proves the point from the
permissive side.** [`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology),
`LICENSE.md`, `1,867 B`, byte-read — title line is `# License`, so rule `v5`'s body scan is what
grades it:

| Layer | Grant | Applies to | Commercial use |
|---|---|---|---|
| Data / ontology | 🟢 **Open Government Licence v3.0** (UK National Archives) | `ontology/`, `data/`, `docs/` | 🟢 **Permitted** — *"Exploit the information commercially and non-commercially"* |
| Code / scripts | 🟢 `MIT` | `scripts/`, `.github/workflows/`, `pyproject.toml` | 🟢 Permitted |

🔵 Required attribution is prescribed verbatim: *"Contains public sector information licensed under
the Open Government Licence v3.0."*, plus a credit to **Oak National Academy**. 🟢 **Consequence for
EMEA engagements:** a nationally curated UK curriculum ontology is commercially reusable with a fixed
attribution string — the cleanest curriculum-alignment substrate this base has found in any region,
and the `OGL-3.0` family should be probed on other national curriculum bodies next pass.

🔴 **The standing caution still holds in the other direction**, from `622-I`: ARASAAC's pictograms are
`MIT` in code and `CC BY-NC-SA` in content, which blocks paid work where the pictograms *are* the
vocabulary. 🟢 The rule is unchanged and now has instances on both sides: **grade the layer the client
actually ships, not the repository.**

## 🆕 `p622` — reads `2026-11-02` — **the vertical finding is a licence file that no automated channel can read: a bespoke bilingual document that names `AGPL-3.0` and then requires a third party's name on the client's home page**

### 🔴 `622-D2` — ENT Core: the platform of record for French school ENTs, and the branding obligation buried in its grant

[`opendigitaleducation/entcore`](https://github.com/opendigitaleducation/entcore) 🔴 **STALE ADDRESS (`626-E`)** — canonical is [`edificeio/entcore`](https://github.com/edificeio/entcore) (`24★`, pushed `2026-11-02`, same `HEAD`) — this base already held the pair in `compose/code/p406-carried-existence/README.md:144` and never propagated it here (`626-E`). It is the core of the
*espace numérique de travail* estate deployed across French regional school systems — the closest
thing EMEA has to a public-sector LMS/portal system of record outside the Apereo orgs. It is on these
shelves already. 🔴 **Its licence had never been read, and reading it changes the row.**

| Property | Measured today |
|---|---|
| `ls-remote --symref` | `PRESENT`, default branch `master`, `HEAD` `933435ba7acc` |
| `LICENSE` | `200`, **`8,537 B`** |
| First line of the payload | 🔴 `///////////////////////////////////////////////////////////` |
| Named licence | `GNU Affero General Public License`, **version 3** |
| **Additional term 1** | 🔴 *"indicate on the home page … `powered by Edifice` with a reference to the website `https://edifice.io/`"* |
| **Additional term 2** | 🟡 A written carve-out: modules communicating with ENT Core *"over native Web protocols, such as HTTP"* are *"outside the scope of this license"* |
| Channel B `spdx_id` | 🔴 `422` — the address is not in the search index (`622-F`) |

🔵 **What it means for a vertical engagement.** The `AGPL` is the ordinary half: it bounds hosting,
and a studio that knows the licence plans for it. **The branding clause is the one that surprises a
client at launch** — the deliverable's home page must carry a third-party vendor's name and a
backlink. It is not in the `AGPL`, it is not in any `spdx_id`, and no licence scanner in existence
emits it. 🟢 The HTTP carve-out cuts the other way and is genuinely useful: it is the vendor's own
written statement that an integration speaking HTTP to ENT Core is **not** a covered work, which is
exactly the architecture a studio would propose.

🔴 **Vertical verdict: `CONDITIONAL`.** Usable as a system of record to integrate *beside* — through
HTTP, on the vendor's own construction — and a poor base to fork, because the fork inherits both the
network copyleft and the homepage obligation.

### 🟢 `622-J3` — the OER/textbook-publishing vertical has a platform of record, and it is copyleft; the permissive option is `8★`

| Layer | Platform of record | Grant | Permissive alternative | Grant |
|---|---|---|---|---|
| Scholarly press / monograph | [`pkp/omp`](https://github.com/pkp/omp) (`145★`, pushed today) | 🔴 `GPL-3.0` | — | — |
| Institutional open textbook | `pressbooks/pressbooks` (held, WordPress-based) | 🔴 `GPL` | [`coko-foundation/ketty`](https://github.com/coko-foundation/ketty) (`8★`) | 🟢 `MIT` |
| Media-rich scholarly | [`anvc/scalar`](https://github.com/anvc/scalar) (`244★`, active) | 🔴 **none at `5` probes** | — | — |
| Render / build | — | — | [`quarto-dev/quarto-cli`](https://github.com/quarto-dev/quarto-cli) (`6,148★`), [`jupyter-book/jupyter-book`](https://github.com/jupyter-book/jupyter-book) (`4,289★`) | 🟢 `MIT` (exceptions noted), `BSD-3-Clause` |

🔵 **The shape a client will hear as a recommendation:** take the permissive render layer, and decide
deliberately between an `8★` permissive platform you will co-maintain and a mature `GPL` platform you
will host rather than ship. `622-J` is the evidence; this is the choice it forces.

### 🟡 `622-N3` — the medical-education vertical has runtimes and no platform of record

`medical education` and `simulation nursing` were **`0`** on these shelves before this pass. After it
there are two usable permissive runtimes (`622-N`: `ashemag/human-atlas` `MIT` `4,455★`,
`biocat-ugent/Open-Anatomy-Explorer` `Apache-2.0` Ghent University) and **no** platform: nothing that
manages cohorts, stations, examiners, simulated patients and scoring.

🔴 **The OSCE tier is the named gap.** Two legs ran (`...OSCE station management ... Apache license`,
`...nursing simulation OSCE ... MIT`). What came back: a **vendor** page describing an "open source"
OSCE manager built for a Swiss university with **no licence named and no repository linked**; a
nursing OSCE scorer described as *"Windows-based, limited to an intranet"*; and
`ScreenBasedSimulator` (`Apache-2.0`, real, **`2015`**). 🔵 **An informed gap:** the examination
logistics layer of medical education has no open, licensed implementation this base can find — and
`exam logistics` returned `0` in the census, so the hole is consistent across two instruments.

### 🟢 `622-C3` — the one-laptop estate, re-typed as a vertical with the licence line through it

Sugar is a *vertical platform*, not a library: a complete learner desktop with an activity model,
journal and collaboration layer, deployed at national scale by LATAM ministries. 🟢 Typed correctly,
the engagement shape is unusual and good: **extend through `LGPL-2.1`
[`sugarlabs/sugar-toolkit-gtk3`](https://github.com/sugarlabs/sugar-toolkit-gtk3) (`32★`, pushed
`2026-10-31`), do not fork `GPL-3.0` [`sugarlabs/sugar`](https://github.com/sugarlabs/sugar)
(`314★`)** — new activities can be proprietary, the shell cannot (`622-C`).

### 🟢 `622-Q2` — the administrative substrate is unchanged, a seventh consecutive confirmation

No new permissive administrative platform surfaced. `openeducat/openeducat_erp` remains `LGPLv3` by
its publisher's own statement (`622-N2`), `frappe/education` and the Odoo-based estate are unchanged,
and the leg that asks for one has now paid nothing **seven** times. 🔵 `618-N`'s standing conclusion
holds and is the sellable version of it: **education's pedagogy is permissive and its administration
is copyleft**, so an administrative engagement is a hosting-and-integration engagement, not a
ship-the-binary one.

## 🆕 `p621` — reads `2026-11-02` — **the AAC vertical has a platform of record and it is `AGPL`; the curriculum-alignment vertical has no platform at all, and both answers are delivery-model constraints rather than licensing footnotes**

### 🔴 `621-L` — the AAC vertical's platform of record is `CoughDrop`/`SweetSuite`, and it is network-copyleft

`619-M2` found the accessibility tier had **no platform of record**. 🟢 The AAC sub-tier named this
pass **does** have one, and it is unambiguous on every axis this base measures except the one that
decides a delivery model.

[`open-aac/sweet-suite-aac`](https://github.com/open-aac/sweet-suite-aac) — `1,892` files, a full
web AAC application plus support suite (speech synthesis, communication boards, supervisor/therapist
tooling), forked from `CoughDrop`, the long-standing open AAC product. Byte-read grant:
🔴 **`AGPL-3.0`, `34,519 B`**. Channel B agrees (`AGPL-3.0`, `9★`, pushed `2025-04-24`) — but only
when queried with `fork:true`, which is `621-M` below.

| Axis | Verdict |
|---|---|
| Completeness | 🟢 `1,892` files — the only AAC tree on this shelf that is a product rather than an app |
| Lineage | 🟢 `CoughDrop` fork; a decade of real clinical deployment behind the codebase |
| Maintenance | 🟡 Pushed `2025-04-24` — ~`18` months stale; the tier's active trees are smaller |
| Grant | 🔴 `AGPL-3.0`: network copyleft. Hosting a modified version **for users over a network** triggers source disclosure to those users |

🔵 **What that means for an engagement, stated plainly.** AAC is delivered as a hosted service to
schools and families far more often than as a shipped binary, and `AGPL`'s §13 is written for exactly
that case. A studio that forks `SweetSuite`, modifies it, and hosts it for a district **owes the
modified source to the district's users**. That is a workable model — it is the one `CoughDrop`
itself runs on — but it must be priced and contracted deliberately, not discovered at delivery.
🟢 The permissive escape hatch exists and it is `621-E`'s `freevoice-aac` (`MIT`) or `OpenAAC`
(`Apache-2.0`), at the cost of a far smaller tree and, in both cases, stale maintenance.

🔴 **The vertical's structural problem, measured:** of `6` real AAC trees, the `3` actively developed
are **all** copyleft (`AGPL`×2, `GPL`×1) and the `2` permissive are the `2` most stale. There is no
actively-maintained permissive AAC platform. This is the same shape `618-N`/`621-N` found in
administration — **permissive where the sector is pedagogical, copyleft where the sector is
operational** — and AAC is operational software.

### 🔴 `621-M` — `p620`'s new discovery channel omits forks, and that nearly cost this pass its platform of record

🟢 `620-A` adopted `gh api search/repositories` as a discovery and per-repository metadata channel
after `600+` passes of recording it blocked. It works. 🔴 **It is also lossy in a way that is silent,
and this pass calibrated it on the tier that exposed it.**

| Query | `total_count` |
|---|---|
| `repo:open-aac/sweet-suite-aac` | **`0`** |
| `repo:open-aac/sweet-suite-aac fork:true` | **`1`** — `fork=true`, `AGPL-3.0`, `9★`, `2025-04-24` |

🔵 **Proven mechanism:** GitHub's search index **excludes forks by default**. `SweetSuite` is a
`CoughDrop` fork, so the default query returns `total_count: 0` — a result shaped exactly like
"this repository does not exist." Channel A (`git ls-remote`) resolved it to `refs/heads/master`
throughout, and the byte read returned `34,519 B` of `AGPL-3.0`, so all three channels agree the
tree is real and granted.

🔴 **Standing rule, registered:** **channel-B absence is not nonexistence.** A `total_count: 0` from
`search/repositories` means *"not in the default index"*, and for this sector that bites hardest
exactly where it matters — a mature platform in an under-supplied vertical is disproportionately
likely to be a fork of the incumbent. Existence verdicts belong to channel A; channel B is for
metadata and cross-checking only.

### 🟡 `621-O` — the curriculum-alignment vertical has four tools and no platform of record

Unlike AAC, this vertical's answer is a **negative** one, and `619-M2`'s distinction applies: this is
a *platform* gap, not a repo gap. Four real trees exist (`621-J`) and not one of them is a platform:

| Tree | Why it is not the platform of record |
|---|---|
| `cloudpedagogy/…-came` | 🟢 Permissive (`MIT`) and the best pick, but **local-first by design** — no multi-user server, no persistence layer, no integration surface. A reviewing instrument, not a system of record. |
| `UBCForestryTLS/curriculum-development-tool` | 🔴 Single-institution (UBC Forestry) and `GPL-3.0`; active but not built to be adopted elsewhere. |
| `usaskulc/cat` | 🔴 `LGPL-3.0`, last pushed `2014`. A survey instrument. |
| `nsip/curriculum-align` | 🔴 A callable classifier, not an application — **and retired by its own maintainers** (`621-J2`). |
| `icarnaghan/Mapper21` (ex-`CurriculumStart`) | 🔴 Active (`2026-10-19`) and ships **no grant** (channel B `NULL`). |

🔵 **The consequence for a studio, which is the point of this page.** Curriculum alignment is
procured constantly — accreditation cycles, programme review, standards migration — and there is
**no open platform to customise**. The honest engagement shape is: `CAME` (`MIT`) as the alignment
*model* and gap-detection logic to read and reimplement, `CASS` (`Apache-2.0`, `621-J3`) as the
competency/standards spine that actually persists and exchanges data, and bespoke application code
between them. Anyone proposing "deploy and extend the open curriculum-mapping platform" is proposing
something that does not exist.

### 🟢 `621-Q` — the administrative substrate is unchanged, sixth consecutive confirmation

`621-N` re-measured the education ERP/CRM leg to a sixth nil. The substrate stands as `616-M`/`618-N`
left it: `OpenOLAT` (`Apache-2.0`) for a full LMS, `Kolibri` (`MIT`) for offline-first delivery,
and — for administration specifically — a choice between copyleft-with-domain (`OpenEduCat`
`LGPL-3.0`, `ERPNext`/`Frappe Education` `GPL-3.0`) and permissive-without-domain (`OFBiz` and
`Corteza`, both `Apache-2.0`). No change this pass, and the leg is retired as a supply instrument.

## 🆕 `p620` — reads `2026-11-02` — **the science-simulation vertical has a platform of record, and its licence boundary runs *through* the product: MIT engine, ungranted content, `CC-BY` distribution**

### 🟢 `620-I` — `PhET Interactive Simulations` as the vertical's platform of record, and the split that decides how a studio uses it

`619` found the accessibility tier had **no platform of record**. 🟢 The science-simulation tier
named this pass has one, it is unambiguous, and it is the most-used science-simulation platform in
the world: **PhET**, University of Colorado Boulder. 🔴 **What matters commercially is not that it is
open — it is *where* it is open.** Measured as two populations, every grant byte-read today under
ladder `v2`:

| Layer | Repos probed | Grant | Bytes | Holder | What a studio may do |
|---|---|---|---|---|---|
| 🟢 **Engine, libraries, build tooling** — `chipper`, `joist`, `scenery`, `alpenglow`, `axon`, `dot`, `kite`, `sun`, `tandem` | **`9`** | 🟢 **`MIT`, `9 of 9`** | `1,096`–`1,097 B` | **University of Colorado** (`2014`–`2023`); `PhET Interactive Simulations` for `tandem` | 🟢 **Build on it, fork it, ship it closed-source.** No reciprocity |
| 🔴 **The simulations themselves** — `circuit-construction-kit-dc`, `-common`, `wave-interference`, `projectile-motion`, `forces-and-motion-basics`, `build-an-atom`, `states-of-matter`, `bending-light`, `example-sim` | **`9`** | 🔴 **no grant payload, `9 of 9`** at `24` paths | — | — | 🔴 **Do not lift a simulation repository.** There is nothing in the tree granting you anything |
| 🟢 **The published simulations** (via the PhET website, not the repos) | — | 🟢 **`CC-BY`** OER | — | PhET | 🟢 Use and adapt **with attribution** — and [`openzim/phet`](https://github.com/openzim/phet) (`Apache-2.0`, pushed today) is the maintained pipeline that acquires them into offline `ZIM` archives |

🟢 **The vertical finding, stated as a delivery rule:** *the repository is the right acquisition
channel for PhET's **engine** and the wrong one for PhET's **content**; the website is the right
channel for the content.* 🔵 A team that clones a sim repo because "PhET is open source" has
acquired `0` rights; a team that builds on `scenery` + `sun` + `tandem` and pulls published sims
through `openzim/phet` has a clean chain for both. 🔴 **This is the kind of error that surfaces in
due diligence, not in development**, which is why it belongs on a vertical page rather than in a
footnote.

🟢 **`tandem` is the row that makes PhET a platform rather than a toy.** `PhET-iO` instrumentation
makes simulation state addressable and serialisable — so a simulation can **emit what a learner
did**, which is precisely the input `p613`'s `Apache-2.0` `xAPI`/`cmi5` conformance tier (US DoD ADL
Initiative) consumes. 🔵 **Engine → instrumentation → `xAPI` → LMS is a complete, permissive,
assessment-grade chain**, and every link was already on these shelves except the first two.

### 🟡 `620-O` — the virtual-lab tier below PhET: four shapes, no second platform

🔴 **No second platform of record exists in this tier**, and that is the measurement. What exists is
four distinct *shapes*, each a single-holder artefact:

| Repo | Grant | ★ | Shape | Region |
|---|---|---|---|---|
| [`ghwmelite-dotcom/AfriLab`](https://github.com/ghwmelite-dotcom/AfriLab) | 🟢 `MIT`, `1,064 B` | `2` | **Breadth** — `29` sims across chemistry, biology, physics, pharmacy, medicine, plus an AI lab assistant | 🟢 **EMEA** — *"African universities — no physical lab required"* |
| [`Ghost-ops721/alyra-labs`](https://github.com/Ghost-ops721/alyra-labs) | 🟢 `MIT`, `1,068 B` | `1` | **Reaction simulation** — real chemistry, scientific visualisation | 🔵 Global |
| [`hlavacs/PhyLab`](https://github.com/hlavacs/PhyLab) | 🟢 `MIT`, `1,071 B` | `5` | **Immersive** — VR laboratory for secondary-school physics | 🔵 Global (holder not placed — `620-E`) |
| [`AMAN6921/SikhshaBox…Education-Labs`](https://github.com/AMAN6921/SikhshaBox-Lightweight-OS-Virtualization-For-Affordable-Education-Labs) | 🟢 `MIT`, `1,069 B` | `13` | **Infrastructure** — virtualises the lab environment instead of simulating the experiment | 🔵 Global |
| [`Xooter/Open-Microcosm`](https://github.com/Xooter/Open-Microcosm) | 🔴 **`GPL-3.0`**, `35,147 B` | `22` | **Emergent physics** — virtual microscope over soft-body, low-Reynolds simulation | 🔵 Global |

🔴 **`Open-Microcosm` is the tier's most technically ambitious artefact and the one a studio cannot
put in a permissive deliverable.** Promoted here from `repos/trending.md` with the boundary stated
rather than left on a trending shelf where the licence would not be read. 🟢 `AfriLab` is the row to
take into an EMEA engagement: it is permissive, byte-read, region-placed on its own text, and it
**states the constraint it was built for** (scarce equipment, expensive consumables) rather than
assuming a lab exists.

### 🟡 `620-P` — the music-education vertical has a server but no platform of record either

🔵 Same shape as `619`'s accessibility finding and worth recording as a pattern across three
consecutive passes: **the named tier has primitives and applications and no system of record.**

- 🟢 **Closest thing to a platform:** [`sirged/fermata`](https://github.com/sirged/fermata)
  (`MIT`, `1,077 B`, `38★`) — a self-hosted sheet-music server with library, search, PDF reading and
  interactive notation/tab rendering. It is the only row in the tier that stores and serves an
  institution's **own** content.
- 🟢 **Rendering substrate:** [`CoderLine/alphaTab`](https://github.com/CoderLine/alphaTab)
  (🟡 `MPL-2.0`, `1,899★`) — and the `MPL-2.0` boundary is **file-level**: it links into closed
  deliverables; modifications to its own files must be published. 🔵 That belongs in the engagement's
  licence matrix on day one, not at delivery.
- 🔴 **No LMS integration anywhere in the tier.** No `LTI 1.3`, no `xAPI`, no gradebook in any of
  `14` names surveyed. 🔵 So music education is, on these shelves, **entirely outside** the
  integration tier `p612`/`p613` built — which is the gap to sell against rather than a gap to fill
  with filler.
- 🔴 **The incumbent is copyleft and was not displaced.** `MuseScore` remains the sector's
  notation incumbent under `GPL-3.0`; nothing surfaced this pass changes that, and it is recorded
  here so the next pass does not re-derive it.

### 🟢 `620-Q` — the administrative substrate is unchanged, and this is the fifth consecutive confirmation

The mandated ERP/CRM vertical leg ran and paid **nothing** for the fifth pass running (`3` head
names, `3` held — `620-N`). 🟢 **The standing position, re-stated rather than re-derived:**

| Need | Permissive option | Copyleft incumbent |
|---|---|---|
| Full LMS | 🟢 **`OpenOLAT`** — `Apache-2.0`, `QTI 2.1` + `SCORM 1.2` + `LTI 1.3` in the box (`p615`, byte-read `10,982 B`) | `Moodle` (`GPL-3.0`), `Open edX` (`AGPL-3.0`) |
| Offline-first delivery | 🟢 **`Kolibri`** — `MIT`, `1,097 B`, branch `develop` (`p616`) — 🟢 and now a natural consumer of `openzim/phet`'s `ZIM` archives | — |
| Assessment engine | 🟢 **`QTIWorks`** — `BSD-3-Clause`, University of Edinburgh (`p607`) | — |
| Telemetry / conformance | 🟢 **`xAPI` / `cmi5` tier** — `Apache-2.0`, US DoD ADL Initiative (`p613`) | — |
| Education ERP / SIS | 🔴 **none** | `OpenEduCat` (`LGPL-3.0`), `ERPNext` (`GPL-3.0`), `Odoo` (split) |
| Student-success CRM | 🔴 **none** — `Elastic License 2.0` **forbids** hosted/managed service (`p614`) | — |

🔴 **The two red rows are the durable commercial finding of this whole shelf**, and five nils on the
mandated leg is now evidence for it rather than an absence of evidence: **there is no permissive
education ERP or student-success CRM**, so any studio engagement touching the administrative tier is
either a copyleft deployment, a licence negotiation, or a build.

## 🆕 `p619` — reads `2026-11-02` — **the accessibility tier has no platform of record, and that is the vertical finding: the incumbents expose the hook but ship nothing behind it**

### 🔴 `619-B` (companion) — the ERP/CRM leg's fourth nil, and the leg is now retired

`619-B` in `repos/foundations.md` carries the measurement. What belongs **here** is the consequence:
after four passes the administrative tier of education has produced **no permissive platform of
record**, and the table below is unchanged from `p618` except for three additions, all of which fail
on *being education software at all* rather than on licence.

| Platform | Grant | Shape | Studio consequence |
|---|---|---|---|
| [`OpenEduCat`](https://openeducat.org/open-source-education-erp/) | 🔴 `LGPL-3.0` | Education ERP on **Odoo** | Carried: usable, but the AI layer belongs **beside** it, not inside it |
| `RosarioSIS` · `Open Admin` | 🔴 GPL-family | School `SIS` / family information | Carried: attach-only for a client that must not relicense |
| `Kuali` (KFS) | 🟡 not stated in channel | Java enterprise ERP | Carried: 🔴 still **ungraded** — needs a byte read before any citation |
| `.LRN` | 🟡 not permissive-confirmed | LMS, **MIT-originated** | Carried, and still this base's best trap: *"developed at MIT"* is an **institutional provenance**, not a grant |
| [`hcengineering/platform`](https://github.com/hcengineering/platform) (Huly) | 🔴 **`EPL-2.0`** — the channel said `Apache-2.0`; the sidebar says **Eclipse Public License**, which is **weak copyleft** (`619-U`) | General data/relationship framework | 🔴 **Not education software, and not permissive.** `EPL-2.0`'s reciprocity bites on **modified source files**, so a closed derivative is not available — a studio told *"Apache"* would have planned the wrong delivery model |
| [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | 🟢 `MIT` — sidebar-confirmed, `24.1k★` | General `CRM` (Laravel) | 🔴 Not education software. Relevant only to the **admissions/enrolment** funnel, where a generic `CRM` is in fact the honest answer |
| `NextCRM` | 🟡 `MIT` — **channel-only, not byte-read** | General `CRM` (`Next.js`) | 🔴 Not education software, and not verified. Not cited as supply anywhere (`619-U`) |
| `CK-ERP` | 🟡 not stated | Edu/`ERP`/`CRM`/`MRP` | 🔴 Latest release in channel is **`2010`**. Stale, not supply |

🟢 **The one honest re-aim the leg produced:** for **admissions and enrolment**, a permissive general
`CRM` (`Krayin`, `MIT`) genuinely beats waiting for an education-specific permissive `SIS` that four
passes say does not exist. 🔴 For **student records**, there is no permissive answer; the studio
attaches to a `GPL`-family `SIS` and keeps its own work on the other side of the boundary.

### 🔴 `619-M2` — the vertical gap this pass actually found, and it is a *platform* gap, not a repo gap

`619-C` landed `12` permissive accessibility and early-literacy artefacts. 🔴 **Not one of them is a
platform, and no platform of record exists for this tier.** Every row is a model, a corpus, an asset
or a single-purpose app. The incumbents expose the integration point and ship nothing behind it:

| Incumbent | Grant | The hook it exposes | 🔴 What it does **not** ship |
|---|---|---|---|
| **Moodle** | 🔴 `GPL-3.0` | Plugin API; `H5P` content types; `SCORM`; accessibility toolkit | No read-aloud **assessment**, no miscue analysis, no sign-language channel |
| **Open edX** | 🔴 `AGPL-3.0` | `XBlock` component API; `Tutor` (CLI) deployment | Same — and `AGPL` makes a hosted derivative a licensing decision, not a technical one |
| **Canvas LMS** | 🔴 `AGPL-3.0` | `LTI 1.3` / **LTI Advantage**; Canvas `API` | Same. 🟢 `LTI 1.3` is the **cleanest boundary of the three**: an external tool, no code in the LMS, no copyleft reach |
| **Kolibri** | 🟢 `MIT` | Offline-first content distribution, device-local | 🟢 The **only permissive** incumbent, and the natural host for offline artefacts — but it distributes content, it does not assess reading |
| **H5P** | 🔴 `MIT` core / mixed | Interactive content types inside any LMS | Authoring, not measurement |
| **BigBlueButton** | 🔴 `LGPL-3.0` | Live classroom, `WebRTC` media | 🔵 The media pipe a **sign-language** channel would ride on; no recognition of its own |

🟢 **The pattern that follows, and it is this base's standing LMS advice applied to a new tier:** build
the accessibility layer as an **`LTI 1.3` external tool**, not as a Moodle plugin or an `XBlock`. The
tool holds the permissive stack (`619-D`'s runtimes + `619-D2`'s models and corpora); the LMS holds
roster, grade passback and nothing else. 🔵 **This is what keeps the studio's work permissive beside a
`GPL`/`AGPL` incumbent** — and it is the same boundary `618-N` drew for the ERP tier, which is why it
is worth stating as one rule rather than two.

🟡 **For offline and low-connectivity delivery — and `619-N` in `intel/market.md` says LATAM public
universities fund AI at `4%`** — the host is **Kolibri** (`MIT`), not an `LTI` tool, because there is
no LMS to attach to. 🟢 `Anmol-Singh-Jaggi`'s classical-`ML` recognizer and `developerali123`'s
`IndexedDB` `PWA` are the two rows that actually run in that setting; the hosted-model rows
(`sunnydev07/Open-Speech`'s `CEFR` rating) do not.

🔴 **Stated gap, so the silence is not mistaken for coverage:** this pass searched for a permissive
**platform** in the accessibility / special-education tier and found none. No `IEP` management system,
no `AAC` platform, no Deaf-education LMS returned a permissive grant. The `12` rows are **components
for a platform that does not exist** — which is an opportunity in `intel/market.md` and a risk in any
estimate that assumes one can be adopted rather than built.


## 🆕 `p618` — reads `2026-11-02` — **the administrative tier is copyleft by default, and that is a delivery-model constraint rather than a licensing footnote**

### 🔴 `618-N` (companion) — what the ERP/CRM leg actually measured, third pass running
| Platform | Grant | Shape | Studio consequence |
|---|---|---|---|
| [`OpenEduCat`](https://openeducat.org/open-source-education-erp/) | 🔴 `LGPL-3.0` | Education ERP on **Odoo** (admissions, courses, fees, library) | Usable, but the **Odoo** base plus `LGPL` shapes how a derivative ships; the AI layer belongs **beside** it, not inside it |
| `RosarioSIS` | 🔴 GPL-family | Web SIS for school administration | Attach-only for a studio that must not relicense |
| `Open Admin` | 🔴 GPL-family | Student + family information | Same |
| `Kuali` (KFS) | 🟡 not stated in channel | Java enterprise ERP on Apache/Tomcat | 🔴 Ungraded — needs a byte read before any citation |
| `.LRN` | 🟡 not permissive-confirmed | LMS, MIT-originated | 🔴 "Originated at MIT" is **not** the MIT licence; a trap this base should name explicitly |

🔵 **`.LRN` deserves its own note.** The channel describes it as *"originally developed at MIT"*, which
is an **institutional provenance**, not a grant. 🔴 This is the licence-family confusion of `618-E` in
its most seductive form, and any shelf that reads "MIT" out of that sentence publishes unusable supply.

🟢 **The pattern that follows, and it is this base's standing LMS advice sharpened.** The incumbent
administrative estate (`Moodle`, `Open edX`, `OpenEduCat`, a GPL SIS) is **not** the thing to replace or
fork. Put the permissive, AI-bearing surface **next to** it, speaking its APIs and `xAPI`, so the
copyleft boundary is never crossed and the deliverable stays relicensable. `P617-3` and `P618-1` both
build on exactly this boundary.


## 🆕 `p617` — reads `2026-11-02` — **the grading/assessment vertical acquires a permissive platform row, and the LATAM platform row is confirmed as an Open edX *attachment* rather than a replacement**

🟢 **New vertical row, byte-read this pass:**

| Platform | Repo | Grant | What it replaces or attaches to | Fit |
| --- | --- | --- | --- | --- |
| **FAIR** | [`azapg/FAIR`](https://github.com/azapg/FAIR) | 🟢 **`MIT`** (`main/LICENSE`, title `MIT License`, © `2026 Allan Zapata`, no additional clause) | A **grading platform *and* LMS in one tree** — so it competes with the LMS tier (`Moodle`, `Open edX`, `ILIAS`, `OpenOLAT`) rather than attaching to it | 🟡 `6★`, `572` commits. 🔴 **Not** an LMS migration target at this maturity. 🟢 Worth running as the **assessment service beside** an incumbent LMS, which is the deployment its rubric/grader model actually supports |

🔵 **Why it is shelved at all, at `6★`.** The permissive LMS tier is `GPL`/`AGPL`-dominated — `Moodle`
`GPL-3.0`, `Open edX` `AGPL-3.0`, `ILIAS` `GPL-3.0` — and the copyleft question is the single most
frequent procurement objection in this sector. 🟢 A permissively licensed assessment platform, however
early, is a different answer to that objection than *"fork Moodle"*. 🟡 Stated plainly: that is an
argument for **watching** it, not for proposing it.

### 🟢 `617-A` — the LATAM platform row, confirmed and correctly typed

[`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (🟢 `MIT`, © `2026 Grupo Sirius`,
Universidad Tecnológica de Pereira, Colombia) **runs inside Open edX** — an **XBlock-shaped
attachment**, not a platform replacement. 🔵 That is the property that makes it the most reusable
LATAM row this base holds: an engagement keeps the client's `AGPL-3.0` Open edX estate and adds a
permissive tutoring surface to it, so the copyleft question never reaches the new code. 🟢 It is also
the row that refutes `616-H`'s index-form gap (`617-A`).

## 🆕 `p616` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THE PERMISSIVE VERTICAL SUBSTRATE IS SETTLED AND RE-MEASURED: `OpenOLAT` (`Apache-2.0`, `p615`) FOR A FULL LMS, `Kolibri` (`MIT`, `1,097 B`, BRANCH `develop`) FOR OFFLINE-FIRST DELIVERY. 🔴 AND THE SKILL-PACKAGE LAYER THAT SITS ON TOP OF THEM IS WHERE THE LICENCE RISK NOW LIVES.**

### 🟢 `616-M` — the vertical stack, as this base can actually defend it today

🔵 `p615` refuted this base's long-standing position that the education vertical's incumbents are all
copyleft, by byte-reading `OpenOLAT` as `Apache-2.0` (`10,982 B`) with `QTI 2.1` + `SCORM 1.2` +
`LTI 1.3` in the box. 🟢 That row is carried unchanged. This pass adds the **delivery-constraint** half
of the stack and re-measures it:

| layer | row | grant read | when a studio reaches for it |
| --- | --- | --- | --- |
| full LMS, permissive | [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 `Apache-2.0` `10,982 B` (`p615`) | Default when the client needs a complete LMS and a permissive licence in the same artefact |
| offline-first delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` `1,097 B`, branch **`develop`** (re-read today) | 🔵 Low-connectivity, low-device contexts — the binding constraint reported for LATAM and Sub-Saharan deployments |
| incumbent, copyleft | `Moodle` / `Open edX` | 🔴 `GPL-3.0` / `AGPL-3.0` (carried) | Where the client already runs it; the grant forces the integration boundary, not the choice |
| education ERP/SIS | `OpenEduCat` | 🔴 `LGPL-3.0` (carried, `p615` leg) | 🟡 Still no `MIT`/`Apache` education-specific ERP found — leg `3` returned the same answer for a fourth pass |

🟡 **Leg `3` repeated verbatim this pass** (`open source platform education LMS ERP CRM MIT Apache`)
and returned the same shape `p615` recorded: a single vendor's content dominating the index, no
independent `MIT`/`Apache` education ERP, and nothing at all on CRM. 🔴 Recorded as a **standing
absence with a known cause** (the index is vendor-captured), not as a new finding.

### 🔴 `616-N` — a refusal pattern for the layer clients will actually ask about

🟢 The skill-package layer is now where new supply arrives (`T616-1`), which means it is where a
studio gets asked *"can we just drop this in?"*. 🔴 On this layer the answer is governed by the tree,
not the root, and this pass has two worked examples:

| candidate | root licence | shippable? | the reason |
| --- | --- | --- | --- |
| [`EtherealMingo/university-teacher-skills`](https://github.com/EtherealMingo/university-teacher-skills) | 🟢 title `MIT License` | 🔴 **not as shipped** | MIT covers first-party parts only; `26` vendored directories excluded, incl. `CC BY-NC-SA 4.0` content and `7` admittedly-unlicensed copies. 🟢 **Remediable** — see `P616-2` |
| [`dmccreary/ibook-skills`](https://github.com/dmccreary/ibook-skills) | 🔴 none — badge only | 🔴 **no** | No grant payload. Badge asserts `CC BY-NC-SA 4.0`; honoured ⇒ `NonCommercial`, not honoured ⇒ all rights reserved. **Both readings refuse** |
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 🔴 `PageLM Community License` | 🔴 **no** (`594-A`, re-read today at `8,563 B`) | Non-commercial only; redistribution *"strictly prohibited"*; commercial use requires a signed revenue-share. 🟢 Verdict unchanged on an independent re-read |

🔵 **The one genuinely permissive member of that upstream set** —
[`ChatGPT3a01/claude-educational-ai-skills`](https://github.com/ChatGPT3a01/claude-educational-ai-skills)
(`MIT`, `1,086 B`, branch `master`) — is the component a studio can actually take from this
neighbourhood, and it is education-specific by design: skills for education researchers, teachers and
e-learning platform developers.

### 🟡 `616-O` — a delivery-model bar that metadata will never show you, carried from `p614`

🔴 `p614`'s [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) (`340★`) — a
student-success platform and recruitment CRM, the exact vertical a client asks for — is **Elastic
License `2.0`**, which forbids *"provid[ing] the software to third parties as a hosted or managed
service"*. 🟢 Re-confirmed today: platform field still reads only `NOASSERTION`, so nothing warns a
reader who triages from metadata.

🔵 **That is a bar on the studio's delivery model, not merely on redistribution** — it survives into
this pass unchanged and generalises: on this shelf, `NOASSERTION` on a *vertical platform* is the
highest-cost unread cell in the whole base, because the row looks like exactly what the engagement
needs. 🟢 `616-E`'s revised rule is the reason to always read it.

## 🆕 `p615` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THIS BASE'S STANDING POSITION THAT THE EDUCATION VERTICAL'S INCUMBENTS ARE COPYLEFT IS **REFUTED ON BYTES**: `OpenOLAT` IS `Apache-2.0` (`10,982 B`, byte-read today) AND SHIPS `QTI 2.1` + `SCORM 1.2` + `LTI 1.3` IN THE BOX. 🔴 AND `614-G`'s GREEN DATA ROW IS `CC-BY-NC-4.0` — THE VERTICAL'S SCARCEST ASSET IS COMMERCIALLY BARRED.**

### 🟢 `615-F` — a permissive full LMS exists, and three passes' legs have been restating the opposite

🔴 This pass's leg `3` (`open source platform education ERP CRM MIT Apache`) returned, in its own
words, that no education-specific ERP under `MIT`/`Apache` was found, offering `OpenEduCat`
(`LGPL-3.0`), `ERPNext` (`GPL-3.0`), Apache OFBiz and Krayin (both generic). 🟢 That matches what
this base has recorded for several passes.

🔴 **It is wrong, and the counterexample was already on this shelf under `5,005` mentions.**

| platform | grant (byte-read `2026-11-02`) | bytes | branch | standards in the box | why it matters |
| --- | --- | --: | --- | --- | --- |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** | `10,982 B` | `master` | 🟢 `QTI 2.1`, `SCORM 1.2`, `LTI 1.3` | 🟢 A **complete LMS under a permissive grant**. Forkable, white-labellable, deliverable as a managed service — none of which `Moodle` (`GPL-3.0`), `Open edX` (`AGPL-3.0`), `ERPNext` (`GPL-3.0`) or `OpenEduCat` (`LGPL-3.0`) permit on the same terms |
| [`RusticiSoftware/TinCanPHP`](https://github.com/RusticiSoftware/TinCanPHP) | 🟢 `Apache-2.0` | `11,358 B` | `master` | xAPI client (PHP) | 🔵 Vendor-published rather than ADL — a second, independent permissive implementation of the same standard |

🟢 **`commercial_use_ok` → `ALLOWED` on both**, via `compose/code/lib/license_family.sh`.
🔴 **Correction to the standing position, stated precisely:** the vertical's *most-adopted*
incumbents are copyleft — that part holds. The claim that *no* permissive full-LMS option exists
does not. `OpenOLAT` is the permissive option, and a brief that hinges on hosted delivery or
white-labelling should start there rather than at a `Moodle` fork.

### 🔴 `615-A` — the vertical's scarcest input is `NonCommercial`, and this base published it green

🔵 `614-G` shelved a K-12 curriculum **knowledge graph** — `1,644` knowledge points, `2,403`
prerequisite edges, `6,723` problems, aligned to China's national curriculum — and called it
🟢 *"fit for purpose"*, correctly noting it is *"the scarcest input an adaptive-learning engagement
has"*.

| address | bytes | instrument (library-resolved) | commercial | status |
| --- | --: | --- | --- | --- |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | `19,347 B` | 🔴 **`CC-BY-NC-4.0`** | 🔴 `DENIED` (exit `1`) | 🔴 **verdict inverted** |

🔴 **`NonCommercial` appears `9` times in the payload; `ShareAlike` `0`.** A paid client engagement is
commercial use. 🟢 The asset's **value** assessment stands untouched — a prerequisite graph is
genuinely the scarce input. 🔴 Its **shippability** does not: it cannot go into a delivered system.
🟢 The honest consequence for the vertical: an adaptive-learning engagement in APAC must either
license this graph separately from its author, or **build the prerequisite layer**, and that is a
scoped work item rather than a free dependency. Full working in `agents/top.md` `615-A`/`615-B`.

### 🟡 Standing vertical table — grant axis, unchanged this pass and restated because it is the axis that decides delivery

| platform | grant | hosted-delivery by a studio |
| --- | --- | --- |
| 🟢 `OpenOLAT` | `Apache-2.0` | 🟢 permitted outright |
| 🟡 `Moodle` | `GPL-3.0` | 🟡 permitted; modifications must be published |
| 🟡 `Open edX` | `AGPL-3.0` | 🔴 network-use clause reaches the hosted service itself |
| 🟡 `OpenEduCat` | `LGPL-3.0` | 🟡 permitted; linking boundary matters |
| 🟡 `ERPNext` / Frappe Education | `GPL-3.0` | 🟡 as `Moodle` |
| 🔴 `canyongbs/advisingapp` (`614`) | **Elastic License `2.0`** | 🔴 **forbidden** — bars providing the software as a hosted or managed service |

🔵 `Kolibri`, `Canvas`, `BigBlueButton`, `H5P`, `Sakai`, `Richie` and `Tutor-CLI` rows stand from
earlier passes and were not re-read this pass; their grants are **not** re-asserted here.

## 🆕 `p614` — reads `2026-11-02`, commit `2026-11-02` — **🔴 THE PASS'S MOST COMMERCIALLY IMPORTANT ROW IS A LICENCE, NOT A PLATFORM: THE SECTOR'S BEST-STARRED OPEN **STUDENT-SUCCESS / RECRUITMENT CRM** (`340★`) IS **ELASTIC LICENSE `2.0`**, WHICH FORBIDS PROVIDING IT AS A HOSTED OR MANAGED SERVICE — A DIRECT BAR ON THE STUDIO DELIVERY MODEL, AND THE PLATFORM FIELD SAYS ONLY `NOASSERTION`. 🟢 PLUS `ECL-2.0` RECOVERED FROM A FIFTH PUBLISHER OUTSIDE APEREO.**

### 🔴 `614-E` (verticals arm) — the ERP/CRM question the run prompt asks, answered with the licence rather than the feature list

🔵 The mandated vertical leg asks for *"real platforms (like Odoo for ERP)"* under `MIT`/`Apache`.
🟢 **The leg's own summary says no education ERP under `MIT` or `Apache` was found**, and this pass
confirms that from the supply side rather than restating it: the education vertical's incumbents are
copyleft or non-OSI, and the interesting rows are the ones that *look* permissive and are not.

| platform | ★ | platform field | grant on bytes | what it is | what a studio may do with it |
| --- | --: | --- | --- | --- | --- |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | `340` | 🔴 `NOASSERTION` | 🔴 **Elastic License `2.0`** `3,860 B` | AI conversational assistant for staff, **student success platform and recruitment CRM** for colleges and universities — the closest thing in open supply to an education CRM | 🔴 **Self-host for the client, yes. Operate it for them, no.** `ELv2`: *"You may not provide the software to third parties as a hosted or managed service."* 🔴 Also forbids disabling the licence-key functionality. A managed-service engagement on this codebase is a licence breach, not a negotiation |
| [`opencast/annotation-tool`](https://github.com/opencast/annotation-tool) | `42` | 🟢 `ECL-2.0` | 🟢 **`ECL-2.0`** `11,340 B` | Video annotation for research, teaching and learning, from the **Opencast** academic consortium | 🟢 **Build on it.** `ECL-2.0` is `Apache-2.0`-derived and permissive; the sector's own licence. 🔴 Default branch `master` |
| [`codeforlife-education/rapid-router`](https://github.com/codeforlife-education/rapid-router) + [`codeforlife-portal`](https://github.com/codeforlife-education/codeforlife-portal) | `60` + `54` | 🔴 `NOASSERTION` ×2 | 🔴 `121 B` **pointer** → **`AGPL-3.0`** | UK primary/secondary coding curriculum: a Blockly game for ages `5`–`11` and a Python game for `11`+ | 🔴 **Reference only.** Network copyleft, discovered only by following a Markdown link out of the repository — `614-F` |

🟡 **`OpenEduCat` remains the honest answer to the ERP question and it is still not permissive.** The
leg surfaced it again at `LGPL-3.0`; `ERPNext` has an education module and is `GPL-3.0`. 🔵 Neither
moved this pass and neither is re-read here. 🟢 The standing position is unchanged: **the education
ERP/SIS tier is copyleft, and the permissive opportunity is the seam around it** — `612-D`'s LTI
launch, `613-B`/`613-C`'s xAPI telemetry, and `614-J`'s classroom-delivery layer.

### 🟢 `614-B` (verticals arm) — `ECL-2.0` outside the Apereo orgs, and why it matters for a procurement

🔵 `604-A` carried *"the API is wrong about `ECL-2.0` in `10 of 11` repos"* as a licence property.
🟢 `opencast/annotation-tool` is a **fifth publisher**, outside the four orgs that sweep covered, and
there the platform field is **correct**. 🔵 For a vertical shelf the practical consequence is narrow
and useful: an `ECL-2.0` component from Apereo needs a byte read before it can be relied on in a bid;
one from Opencast can be triaged from the field like any `Apache` row. 🔴 `n = 1` outside Apereo —
this bounds `604-A`'s claim, it does not replace its number.

### 🔵 The customisable-base table, restated with this pass's additions marked

🟢 Unchanged rows are carried, not re-measured; only the marked rows were read today.

| system | layer | licence | region of publisher | AI-on-top fit |
| --- | --- | --- | --- | --- |
| Moodle | LMS | 🔴 `GPL-3.0` | EMEA | Launch via LTI (`612-D`), report via xAPI (`613-C`) — never fork |
| Open edX | LMS | 🔴 `AGPL-3.0` | North America | Same seam strategy; release branches changed convention after Sumac (`612-G`) |
| Kolibri | offline-first LMS | 🟡 carried | APAC/Global | Offline deployment reference |
| 🆕 [`opencast/annotation-tool`](https://github.com/opencast/annotation-tool) | classroom video | 🟢 **`ECL-2.0`** (byte-read today) | EMEA | 🟢 Permissive annotation layer over lecture capture — a place to put an AI summariser without touching the LMS |
| 🆕 [`haxtheweb/haxcms-php`](https://github.com/haxtheweb/haxcms-php) | course content CMS | 🟢 **`Apache-2.0`** (byte-read today) | North America | 🟢 Microsite-per-course authoring, institutional provenance (Penn State) |
| 🆕 [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | student success / CRM | 🔴 **Elastic `2.0`** (byte-read today) | North America | 🔴 **Warning row.** Shelved so no one proposes it as the managed-service base |

## 🆕 `p613` — reads `2026-11-02`, commit `2026-11-02` — **🔴 THE SECTOR'S STANDARDS INDEX POINTS `12 of 28` ADDRESSES (`42.9 %`) AT AN ORG THAT HAS **ZERO** REPOSITORIES — AND ALL `12` RECOVER, BY SLUG, UNDER THE REAL PUBLISHER. 🟢 THAT RECOVERY IS THE WHOLE `Apache-2.0` xAPI / cmi5 CONFORMANCE TIER, PUBLISHED BY THE US DoD's ADL INITIATIVE, AND THIS BASE HAD NONE OF IT.**

### 🟢 `613-B` — the conformance tier, recovered from a dead org

🔵 **What this tier is for.** `612-E` shelved rubric/autograding repos and argued they are *"not a
feature but the Annex III conformity evidence."* 🟢 This is the same argument one layer down and with a
government behind it: xAPI and cmi5 are the **interoperability standards** an education procurement
writes into a contract, and the publisher ships a **conformance test suite** that answers "is your
implementation compliant?" with a test run rather than an assertion.

| repo | ★ | grant (byte-read) | path | branch | pushed | what it is |
| --- | --: | --- | --- | --- | --- | --- |
| [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | `956` | 🟢 `Apache-2.0` `11,525 B` | `LICENSE` | 🟡 `master` | `2025-07-03` | 🟢 The **specification itself**, permissively licensed — so the contract language can be quoted, forked and annotated for a client without permission |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | `334` | 🟢 `Apache-2.0` `11,357 B` | `LICENSE` | 🟡 `master` | `2025-11-14` | The publisher's own reference Learning Record Store — the thing `yetanalytics/lrsql` is a production alternative to |
| [`adlnet/xAPIWrapper`](https://github.com/adlnet/xAPIWrapper) | `224` | 🟢 `Apache-2.0` `10,273 B` | `LICENSE` | 🟡 `master` | 🔴 `2022-12-04` | Browser wrapper for talking to an LRS. 🔴 **Unmaintained since `2022`** — prefer `xapijs/xapi` (`613-C`) and keep this only as a reference |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | `78` | 🟢 `MIT` `1,046 B` | `LICENSE` | 🟡 `master` | `2025-09-04` | 🟢 **The procurement answer.** A Node suite that tests the `MUST` requirements of the spec against a live LRS. `MIT`, so it ships inside a client's own CI |
| [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) | `60` | 🟢 `Apache-2.0` `11,357 B` | `LICENSE` | 🟡 `master` | `2024-12-16` | The profile **specification** — how a sector agrees on what a statement means |
| [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) | `59` | 🟢 `Apache-2.0` `11,358 B` | `LICENSE` | `main` | `2026-01-20` | 🟢 **cmi5** test application and player — the SCORM replacement's conformance kit |
| [`adlnet/xapi-authored-profiles`](https://github.com/adlnet/xapi-authored-profiles) | `45` | 🟢 `Apache-2.0` `11,357 B` | `LICENSE` | 🟡 `master` | `2025-11-17` | The official profile library — reusable vocabularies rather than inventing statement semantics per client |
| [`adlnet/MasterObjectModel`](https://github.com/adlnet/MasterObjectModel) | `12` | 🟢 `Apache-2.0` `11,525 B` | `LICENSE` | 🟡 `master` | `2025-07-03` | A profile denoting how a statement is structured — small, but it is the schema a validator keys on |
| [`AICC/CMI-5_Spec_Current`](https://github.com/AICC/CMI-5_Spec_Current) | `189` | 🟢 `Apache-2.0` `10,824 B` | `LICENSE` | 🔴 `quartz` | `2024-09-06` | The **cmi5 specification** at the standards body. 🔴 Default branch is `quartz` — neither `main` nor `master`, and a third distinct shape after `611-C`'s `produção` |

🟡 **Stated limit, because it bounds how this tier is sold.** Five of the nine were last pushed in `2024`
or `2025`, and one in `2022`. 🔵 For a *specification* that is close to a non-finding — specs are stable
by design, and `xAPI-Spec` being quiet is what a ratified standard looks like. 🔴 For `xAPIWrapper`,
which is **code**, it is a real defect, and the row says so. The live code in this stack is
`613-C`'s `lrsql`, `ralph` and `datasim`, all pushed within the last `17` days.

### 🔴 `613-A` — the mechanism: `42.9 %` of a curated standards index is one dead org, not scattered rot

🟢 `org:i2idl` returns **`0`** repositories. `org:adlnet` returns **`92`**. Every one of the `12`
unresolved `i2idl/*` addresses in [`tla-ecosystem/awesome-tla`](https://github.com/tla-ecosystem/awesome-tla)
recovers **by unchanged slug** under `adlnet`. Evidence:
`evidence/dead-org-recovery.2026-11-02-p613.tsv`.

🔵 **Why the shape matters more than the count.** `612-A` measured `101 of 848` (`11.9 %`) of a carried
backlog no longer resolving and concluded *"a carried backlog is a wasting asset."* 🔴 That framing
implies **attrition** — many small repos dying independently, which nothing can recover. 🟢 This failure
is the opposite: **one owner-level redirect, `12` addresses, `100 %` recoverable in a single step.**
🟢 **Operative rule:** before writing off unresolved addresses, group them by owner — an owner with
several dead addresses is a *move*, and a move is free to follow; only a singleton is attrition.
🔵 On this population the rule recovers `12 of 16` (`75 %`) of what a per-address sweep discards.


## 🆕 `p612` — reads `2026-11-02`, commit `2026-11-02` — **🟢 A NATIONAL EDUCATION MINISTRY SHIPS **THREE** LIVE SERVICES UNDER `MIT` AND THIS BASE HAD SHELVED NONE OF THEM. 🔴 `612-G`: THE TWO INCUMBENT PLATFORMS BOTH MOVED SOMETHING THAT BREAKS TOOLING — MOODLE DELETED ROOT `version.php` AT `5.x`, OPEN EDX CHANGED ITS RELEASE-BRANCH CONVENTION AFTER SUMAC. BOTH RESOLVED FROM REFS AND BYTES, NOT FROM PROSE. `6` PLATFORM ROWS PROMOTED.**

### 🟢 `612-F` — the public-sector tier: a ministry's own code, `MIT`, pushed today

🔵 `611-D` found the first permissive **provincial** system of record (`bcgov/SIMS`, Government of
British Columbia) and called the public sector the most transferable asset class in education. 🟢 This
pass finds the **national** case, and it is three services from one ministry.

| platform | ★ | grant (byte-read) | path | branch | pushed | region | what it actually is |
| --- | --: | --- | --- | --- | --- | --- | --- |
| [`DFE-Digital/apply-for-teacher-training`](https://github.com/DFE-Digital/apply-for-teacher-training) | `38` | 🟢 `MIT` `1,094 B` | 🟡 `LICENCE` | `main` | `2026-11-02` | 🟢 EMEA | 🟢 The **live national service** by which candidates apply for teacher training in England. UK Department for Education. A working admissions pipeline at national scale, permissively licensed |
| [`vincenzo-afk/Proctored-MCQ-Exam-Platform`](https://github.com/vincenzo-afk/Proctored-MCQ-Exam-Platform) | `37` | 🟢 `MIT` `1,072 B` | `LICENSE` | `main` | `2026-08-24` | Global | Browser exam platform with camera proctoring, module progression and certificate export. 🔴 Read the Annex III note below before proposing it |
| [`DFE-Digital/teaching-vacancies`](https://github.com/DFE-Digital/teaching-vacancies) | `27` | 🟢 `MIT` `1,092 B` | `LICENSE` | `main` | `2026-11-02` | 🟢 EMEA | The DfE's free national teaching **job-listing** service — a two-sided marketplace a government runs in the open |
| [`DFE-Digital/get-into-teaching-app`](https://github.com/DFE-Digital/get-into-teaching-app) | `25` | 🟢 `MIT` `1,091 B` | 🟡 `LICENCE` | 🟡 `master` | `2026-10-29` | 🟢 EMEA | The DfE's recruitment front door — content, events and lead capture |
| [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | `97` | 🟡 `MPL-2.0` `16,725 B` | `LICENSE` | 🟡 `master` | `2026-10-31` | 🟢 EMEA | **SEB Server** — centralised configuration and conduct of exams across Safe Exam Browser clients, integrating with an LMS or exam system. 🟡 `MPL-2.0` is file-level copyleft: link freely, publish changes to *its* files |
| [`zuhairhalawa/studyai`](https://github.com/zuhairhalawa/studyai) | `251` | 🟢 `MIT` `1,069 B` | `LICENSE` | `main` | `2026-10-24` | Global | Local-first study platform for university lectures: slide ingestion, spaced repetition, exams, optional tutor on a free model tier |

🟡 **Two of the five `MIT` grants are spelled `LICENCE`.** British spelling, and `612-C` is why that is
worth a line: a case- and spelling-incomplete ladder reports a government service as ungranted.

🔴 **Annex III warning attached to two rows, stated here so it travels with them.** `seb-server` and
`Proctored-MCQ-Exam-Platform` both *"monitor students for prohibited behaviour during tests"* — that is
the Annex III high-risk category verbatim. 🟢 They are permissive and real and they are the right
starting points; 🔴 deploying either into the EU puts the deployer inside the high-risk regime from
`2027-12-02`. 🟢 Pair them with `612-E`'s rubric tier from day one rather than retrofitting the
documentation.

### 🔴 `612-G` — both incumbents moved something that breaks tooling, and the prose sources contradicted each other

🔵 The global verticals leg returned three mutually inconsistent claims: *"Moodle 5.3 LTS, released
2026-10-05"*; *"Verawood (2026-07-30) is the only supported Open edX release"*; *"Ulmo (2026-01-15)
remains the only supported branch."* 🟢 None of it was resolvable from prose. Resolved from git refs and
grant/version bytes. Evidence: `evidence/moodle-version-path.2026-11-02-p612.tsv`,
`evidence/openedx-release-refs.2026-11-02-p612.tsv`.

🔴 **Moodle: root `version.php` is gone at `5.x`.**

| ref | `version.php` | `public/version.php` | what the bytes say |
| --- | --- | --- | --- |
| `MOODLE_405_STABLE` | 🟢 `200` `1,641 B` | 🔴 `404` | `$release = '4.5.15+ (Build: 20261030)'`, `$branch = '405'`, `MATURITY_STABLE` |
| `MOODLE_503_STABLE` | 🔴 **`404`** | 🟢 `200` `1,638 B` | `$release = '5.3+ (Build: 20261030)'`, `$branch = '503'`, `MATURITY_STABLE` |
| `v5.3.0` (tag) | 🔴 `404` | — | the tag agrees with the stable branch |
| `main` (real default) | 🔴 `404` | — | absent on the default branch too |

🟢 **The web root moved under `public/` at Moodle `5.x`** — `public/index.php` is `200` at `5.3` and
`404` at `4.5`. 🔴 **Consequence, and it is the finding:** every version probe, upgrade checker, uptime
check, CI pin and deployment script that reads root `version.php` returns *nothing* against Moodle `5.x`
and, depending on how it is written, reports the instance as not-Moodle rather than as 5.x. 🟢 Read
`public/version.php`, and fall back to root `version.php` for `4.x`.

🔴 **Two prose claims corrected.** `2026-10-05` is `$version`'s **branching date**
(`2026100500.08`), not a release date. 🔴 And nothing in the refs or bytes marks `5.3` **LTS** — the LTS
signature in this repository is `4.5`, still built the same day (`4.5.15+ (Build: 20261030)`) three
minor releases later. 🟡 Recorded as unverified rather than repeated.

🟢 **Open edX: both releases exist, and the branch convention changed.** The two sources were describing
different moments, and neither was right that only one release exists.

| branch | head | convention |
| --- | --- | --- |
| `open-release/sumac.master` | `02f0f03b2f96` | 🟡 the **last** release under `open-release/<name>.master` |
| `release/teak` | `c4c9043c2593` | 🔴 the convention **changes here** to `release/<name>` |
| `release/ulmo` | `e8e829e31c68` | `release/<name>` |
| `release/verawood` | `484f080fa0cf` | `release/<name>` — 🟢 latest, by the project's own alphabetical naming (T → U → V) |

🔴 **Consequence:** any pin, mirror, Tutor config or CI matrix that globs `open-release/*` silently stops
finding releases after **Sumac** — it does not error, it just never sees Teak, Ulmo or Verawood. 🟢 Pin
`release/<name>`.

🔵 **`612-G` stated generally:** the incumbents in this sector are `GPL-3.0` and `AGPL-3.0`, so an
engagement integrates with them rather than forking them — and **an integration breaks on a moved path
or a renamed ref, not on a licence.** 🟢 Read the refs and the bytes; a release note is prose.

---

## 🆕 `p611` — reads `2026-11-02`, commit `2026-11-02` — **🟢 TWO PLATFORM ROWS WHOSE LICENCES THIS BASE WOULD HAVE GOT WRONG IF IT HAD TRUSTED THE SECTOR'S STANDARD INDEX: A SCHOOL/UNIVERSITY PLATFORM PUBLISHED AS `GPL-3.0` IS **`MIT`**, AND THE UNESCO-ENDORSED NATIONAL EMIS PUBLISHED AS `GPL-3.0` IS **`GPL-2.0`**. 🔴 BOTH CORRECTED FROM GRANT BYTES AT THE REAL DEFAULT BRANCH.**

### 🟢 `collejo` — a permissive school-and-university platform, mislabelled copyleft

| axis | reading, byte-read `2026-11-02` |
| --- | --- |
| address | [`CodeBreez/collejo`](https://github.com/CodeBreez/collejo) |
| 🔴 what the sector index publishes | 🔴 `GPL-3.0` |
| 🟢 what the grant bytes say | 🟢 **`MIT`**, `1,076 B`, `LICENSE` at `master`, *"Copyright (c) 2016 Anuradha Jayathilaka"* |
| what it is | Laravel school & university management: student grades, class management, attendance logs, role permissions |
| state | `51★`, `30` forks, 🔴 **pushed `2019-07-16`** |
| 🔴 stack age | 🔴 `Laravel 5.6` (2018); the README's build badges point at `astroanu/collejo-workbench` branch `L55` |

🔵 **How to use this row, stated honestly.** 🔴 It is **not** a build recommendation — a seven-year-old
Laravel 5.6 tree is a migration project, not a foundation. 🟢 It is on this shelf for two reasons that
survive the staleness: the **`MIT` grant is real**, so its data model and permission scheme can be
lifted without a copyleft obligation; and it is 🟢 **the counter-example that makes `611-A`'s rule
symmetric** — an index's licence column errs toward copyleft as well as away from it.

### 🟢 `OpenEMIS Core` — the national EMIS tier, with its grant version corrected

| axis | reading, byte-read `2026-11-02` |
| --- | --- |
| address | [`OpenEMIS/core`](https://github.com/OpenEMIS/core) |
| 🔴 what the sector index publishes | 🔴 `GPL-3.0` |
| 🟢 what the grant bytes say | 🟢 **`GPL-2.0`** — *"GNU GENERAL PUBLIC LICENSE / Version 2, June 1991"*, `15,518 B`, `master` |
| what it is | Education Management Information System for 🟢 **national, district and school-level** data — schools, students, staff |
| backing | UNESCO-endorsed; *"widely used in many countries"*; vendor-hosted or self-hosted |
| state | `24★`, `18` forks, `288 MB`, pushed 🟢 `2026-10-26` |

🔵 **Why the version matters commercially, not pedantically.** `GPL-2.0` and `GPL-3.0` differ on
patent grant and on anti-tivoisation, and 🔴 `GPL-2.0` has **no explicit patent licence** — which is
exactly the clause a ministry's counsel asks about when a vendor builds on top. 🟢 The engagement shape
is unchanged (`LINK-ONLY`, client-hosted, AI layer in a separate process communicating over the API),
but the **advice** changes, and a row carrying the wrong version gives the wrong advice.

🟡 **And this is the row `611-B` nearly broke.** This pass's own classifier graded it `LGPL-2.1`,
because the `GPL-2.0` text names the Lesser GPL at line `18`. 🟢 Caught on a title-line re-grade before
it shipped; the mechanism is written up on `agents/top.md`.

### 🔵 The platform tier's licence reality, after this pass

🔵 Restating what these two rows change, because the tier's shape is what an engagement plans against:

| tier | grant family | engagement shape |
| --- | --- | --- |
| 🔴 national EMIS of record (`OpenEMIS/core`) | `GPL-2.0` | `LINK-ONLY` — client-hosted, AI in a separate process over the API |
| 🔴 education ERP (`openeducat_erp`, `odoo`) | `LGPL-3.0` | `LINK-ONLY` — confirmed `p557`; 🟡 default branch `19.0`, **not** `main` |
| 🔴 LMS of record (`moodle/moodle`) | `GPL-3.0` | `LINK-ONLY`; 🟢 mobile + deployment layers permissive since `p610` |
| 🟢 provincial financial-aid system of record (`bcgov/SIMS`) | 🟢 **`Apache-2.0`** | 🟢 **fork-and-extend** — this pass, `repos/foundations.md` |
| 🟢 school/university management (`collejo`) | 🟢 **`MIT`** | 🟢 fork-and-extend, 🔴 but stale since `2019` |

🔴 **The standing conclusion is unchanged and now better evidenced: every education platform of record
is copyleft, and the permissive rows are the periphery and the public sector** — never the core LMS.

---

## 🆕 `p610` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THE MOODLE TIER FINALLY HAS ITS **MOBILE** AND **DEPLOYMENT** LAYERS, BOTH PERMISSIVE, WHILE THE CORE STAYS `GPL-3.0`. 🔴 AND THE OFFICIAL MOBILE CLIENT WAS NEARLY REFUSED AS UNGRANTED BY THIS PASS'S OWN LADDER — `610-E`.**

### 🟢 Why these two rows matter more than their star counts

🔵 This base has carried [`moodle/moodle`](https://github.com/moodle/moodle) as the sector's largest
plugin ecosystem for hundreds of passes, with the **`GPL-3.0`** boundary stated every time: anything
linked into the Moodle core inherits it. 🟢 Both rows below sit **outside** that boundary — one is a
separate mobile client, one is infrastructure-as-code — so a client deliverable built on either does
not take GPL terms from them.

| Platform | Repo | Grant (byte-read) | Region | ★ | Size | Last push | What it gives a build |
| --- | --- | --- | --- | --: | --: | --- | --- |
| **Moodle App** (official) | [`moodlehq/moodleapp`](https://github.com/moodlehq/moodleapp) | 🟢 **Apache-2.0** `11,358 B` — at **`COPYING.txt`**, see `610-E` | 🔵 Global (Moodle HQ) | `1,004` | `133,226 KB` | `2026-10-29` | 🟢 **Moodle HQ's own mobile client**, Ionic/Angular, with offline course content and submission sync. The one place a Moodle engagement can add an agentic surface **without touching GPL core** — and the mobile seam is where the offline-first requirement in low-connectivity LATAM and African deployments actually lives |
| **Moodle on Azure** | [`Azure/Moodle`](https://github.com/Azure/Moodle) | 🟢 **MIT** `1,090 B` | 🔵 Global (Microsoft) | `186` | `2,280 KB` | `2026-11-02` | 🟢 ARM/Bicep templates for a scaled Moodle: autoscaled web tier, managed MySQL/PostgreSQL, Redis, shared storage and an optional Elastic stack. 🟢 **MIT on the deployment layer** means the reference architecture is reusable in a client's own tenancy. Pushed **today** |

🟡 **The honest boundary, restated.** Neither row makes Moodle itself permissive. A plugin inside
`moodle/moodle` is `GPL-3.0` and this base has never said otherwise; what changed is that the
**mobile** and **deployment** layers are now shelved with permissive grants of their own, so a
three-layer Moodle engagement has exactly one copyleft layer instead of three unstated ones.

---

## 🆕 `p609` — reads `2026-11-02` — **🔴 NO NEW PLATFORM ROW THIS PASS, AND THE REASON IS NAMED: THE MANDATED VERTICAL LEG RETURNED ONE VENDOR'S OWN WEBSITE `10 of 10` TIMES. 🟢 THE TIER WAS PROBED THROUGH A SECOND, WORKING CHANNEL ANYWAY, AND THE ONE REAL CANDIDATE IT FOUND IS ALREADY HELD HERE. 🔴 `609-D`: A `10 KB` REPOSITORY CLAIMING A PRODUCTION-READY KUBERNETES LMS, WITH A VALID APACHE GRANT.**

### 🔴 The mandated vertical leg is captured by a single vendor

The run prompt's vertical query — `open source platform education ERP CRM MIT Apache` — returned ten
results. All ten were pages on **`openeducat.org`**: the same vendor glossary served at `/ar/`,
`/fr/`, `/pt-BR/`, `/zh/`, `/de/`, `/es/` and the bare path. 🔵 A leg that cannot return a second
vendor is measuring one SEO estate, not a market.

🟡 **And the product it points to does not satisfy the query it answered.** **OpenEduCat** is an
education ERP on the Odoo framework, held on this shelf for many passes, and its own site states
**LGPL-3.0** — a copyleft grant, not the MIT/Apache surface the query asked for. The vendor's pages
also cite Gartner, European Commission and CISA studies for its cost and security claims; none of
those is reachable from this session (`609-G`), so they are **restatements, not verifications**.

### 🟢 The tier probed through the channel that works — and it genuinely did not move

Narrow permissive queries (`609`'s productive channel) against the platform tier:

| query | `total_count` | what it actually contained |
| --- | --: | --- |
| `student information system school management license:mit pushed:>2026-01-01` | `19` | 🔴 coursework — console C programs, Django CRUD exercises, one Home Assistant integration, one single-school monorepo |
| `LMS learning management system license:apache-2.0 pushed:>2026-01-01` | `29` | 🔴 coursework — `Mini-LMS` ×2 for a database course, an early-alpha Rust LMS, a university assignment |

| the one real candidate | verdict |
| --- | --- |
| [`pacewisdomhq/TutorLoom`](https://github.com/pacewisdomhq/TutorLoom) — 🟢 **Apache-2.0**, `11,362 B` byte-read today, `63★`, multi-tenant self-hosted LMS for institutes and training teams (Django 6 / DRF / PostgreSQL / React 19 / Flutter), *"one installation serves many organisations, every query scoped to the organisation"* | 🔴 **already held on this shelf** — re-byte-read today and the grant **confirmed** |

🟢 **So the nil is informed.** The vertical tier did not gain a holder this week; it also did not lose
one, and the single platform worth having was re-measured rather than assumed. 🔵 `p608` made the
same shape of statement about this tier from the other direction — `10 of 10` platform rows
re-byte-read and matching — so two consecutive passes now agree the LMS/SIS tier here is **stable and
correctly recorded**, which is the condition under which a nil is a result.

### 🔴 `609-D` — the vapour row, and why a grant-first screen cannot catch it

[`mkhomytsya/MuckeligAgentLMS`](https://github.com/mkhomytsya/MuckeligAgentLMS) is the row this tier
would have been wrong to take, and it would have been taken on terms:

| axis | reading |
| --- | --- |
| claims | *"The first cloud-native Learning Management System powered by autonomous AI agents"* — autonomous course generation, AI personalisation, self-managing administration, **built-in xAPI LRS**, real-time dashboards, *"Kubernetes-Native, scalable, production-ready"* |
| grant | 🟢 **Apache-2.0**, `11,366 B`, byte-read `2026-11-02` — a real, stock, permissive grant |
| existence | 🟢 `606-E` probe `200` — the address is real |
| 🔴 **repository size** | 🔴 **`10 KB`, total** |
| 🔴 history | 🔴 created `2026-02-12`, pushed `2026-02-12`, `0` open issues, `0` topics — one day, never touched since |

🔵 **Every gate this base runs on the vertical tier would have passed it.** The grant is genuine, the
address resolves, the README is specific and confident, and an xAPI LRS is exactly the capability this
tier wants. Only **size** refutes it: `10 KB` cannot contain a multi-tenant Kubernetes LMS, so the
README describes an intention in the present tense. 🟢 Size is free on a channel this base already
calls, and from `p609` it is run on every platform candidate **before** the grant, because it is the
only one of these axes that measures whether the software exists.

---


## 🆕 `p608` — reads `2026-11-02` — **🟢 THE WHOLE LMS/SIS TIER RE-BYTE-READ FROM SCRATCH BY AN INDEPENDENT INSTRUMENT: `10 of 10` MATCH WHAT THIS BASE ALREADY HELD. 🔴 AND THE INSTRUMENT FELL INTO `3` OF THIS BASE'S OWN PRE-REGISTERED TRAPS, WHICH IS THE RESULT.**

### 🟢 The platform tier, re-measured today against the real default branch

A fresh four-name probe (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` × `main`, `master`) was
run blind against the customisable-platform tier. **Every grant it resolved matched this base's
existing column.**

| Platform | Repo | License (byte-read `2026-11-02`) | Customisable with AI on top? |
| --- | --- | --- | --- |
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 **GPL-3.0** — `COPYING.txt`, both branches `200` | 🟢 Largest plugin ecosystem in the industry; the AI subsystem is the supported insertion point |
| **Open edX** | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 🔴 **AGPL-3.0**, `35,135 B` | ⚠️ MOOC-grade, but the grant is **network copyleft** — the single most consequential license fact in this tier |
| **XBlock** | [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0**, `11,358 B` | 🟢 **The permissive component boundary inside an AGPL platform** — build the AI component here |
| **Canvas** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0**, `34,519 B` | ⚠️ Integrate via API/LTI rather than fork |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **AGPL-3.0**, `35,146 B` | ⚠️ Lighter to operate than Open edX; same copyleft shape |
| **ILIAS** | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **AGPL-3.0**, `35,146 B` | ⚠️ Strong EMEA/DACH institutional base |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** (*Educational Community License* v2.0, April 2007), `11,119 B` | 🟢 Permissive, Apache-*derived* — the grant most specific to this industry |
| **Richie** | [`openfun/richie`](https://github.com/openfun/richie) | 🟢 **MIT**, `1,077 B` | 🟢 Django+React course-portal front end — France Université Numérique |
| **Pupilfirst** | [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | 🟡 **split**: `docs/` CC BY-SA 4.0, client-side JS MIT, remainder MIT, third-party components under their own terms, `1,683 B` | 🟢 APAC (India) · ⚠️ read the split before shipping docs |
| **QTIWorks** | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause**, `2,058 B` at `LICENSE.txt` | 🟢 The QTI 3.0 **engine** `p607` shelved — assessment stack permissive end to end |
| 🆕 **WeKnora** | [`Tencent/WeKnora`](https://github.com/Tencent/WeKnora) | 🟢 **MIT**, `15,290 B` ⚠️ Apache-2.0 third-party appendix | 🟢 **New this pass.** Not an LMS — the doc→RAG→agent→wiki layer you bolt *beside* one |

### 🔴 The real result — an independent instrument hit `3` pre-registered traps

The probe above was deliberately naive. It produced **three false negatives**, and this base had
already named all three in advance:

| what the probe reported | truth | the trap, as this base had already registered it |
| --- | --- | --- |
| 🔴 `openedx/XBlock` → **`404-NOT-A-REPO`** | 🟢 **Apache-2.0**, `11,358 B` | 🔴 **UPPERCASE extension `LICENSE.TXT`.** `raw.githubusercontent.com` is case-sensitive; `LICENSE.txt` returns `404: Not Found` (`14 B`) three times running, while `LICENSE.TXT` returns `200`. This base's own note reads: *"XBlock was one absent file from being filed ungranted."* 🔵 It very nearly was, again, today |
| 🔴 `moodle/moodle` → **`NO-LICENSE-FILE`** | 🟢 **GPL-3.0** | 🔴 The grant lives at **`COPYING.txt`** — a fifth name outside a four-name probe |
| 🔴 `sakaiproject/sakai` → **`OTHER/unclassified`** | 🟢 **ECL-2.0** | 🔴 ECL-2.0's text names *"Apache 2.0 license"* in **lower case** and contains **zero** occurrences of the string `Apache License`, so an `Apache License` matcher cannot see it. This base keeps `compose/code/p1040-ecl-corpus-census` for exactly this |

🔵 **What this is worth.** Three passes' worth of recorded traps were tested blind by an instrument
that had not read them, and the instrument fell into all three — then the base's column turned out
right in all three. 🔴 **A naive license probe under-reports permissive grants**, and it
under-reports them in the direction that costs a studio real options: XBlock would have been filed
ungranted, Sakai unclassified, Moodle grantless. The correct conclusion from a `404` on a license
path is **"try another name and another case,"** never *"no license."*

### 🟢 What the tier looks like for an engagement, after re-measurement

- 🔴 **`5 of 11` platforms are AGPL-3.0** (Open edX, Canvas, Chamilo, ILIAS — plus `edgameclaw`,
  `godspeed`, `open-jarvis`, `terramentor` rejected this pass on the agent shelf). **Network
  copyleft is the default condition of this industry's platform tier**, not the exception.
- 🟢 **The permissive path exists and is now continuous:** component layer `XBlock` (Apache-2.0) ·
  platform `Sakai` (ECL-2.0) · portal `Richie` (MIT) · assessment engine `qtiworks` (BSD-3-Clause) ·
  ingestion `WeKnora` (MIT) · anonymisation `obfusca` (MIT). An engagement can be assembled
  end to end without crossing a copyleft boundary.
- ⚠️ **Moodle (GPL-3.0) is not AGPL.** Plugins distributed to a customer carry GPL obligations;
  a hosted service does not trigger the network clause Open edX would. The distinction is worth
  money and is frequently collapsed in vendor comparisons.

---

## 🆕 `p607` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THE PLATFORM FINDING IS AN **ENGINE**, NOT A CONNECTOR: QTIWORKS — A COMPLETE QTI 2.1 ASSESSMENT ENGINE OUT OF THE **UNIVERSITY OF EDINBURGH**, BSD-3-CLAUSE BYTE-READ, MAINTAINED TO `2026-06-30` IN ITS **OPENOLAT FORK** — HAS BEEN IN THIS BASE'S `trending` SHELVES FOR `21` MENTIONS AND ON NO PLATFORM PAGE. 🟢 IT ALSO RETIRES `p604`'s OWN SINGLE-MAINTAINER FLAG ON THE QTI TIER. 🔴 THE API CALLS IT `NOASSERTION` AND A DEPENDENCY SCREEN WOULD REJECT IT. 🟡 `605-K`'s DEBT: `26` PAID THIS PASS, `73` REMAIN.**

### 🟢 `607-I` — QTIWorks: the assessment **engine** this page has been assuming

`p601` added an assessment-*delivery* tier (the layer that renders and scores an item). `p604` and
`p605` added a QTI 3.0 *toolchain* (players, item banks, libraries). 🔴 **Neither added an engine** —
the component that actually runs an assessment session, sequences items, and holds candidate state.

| | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) |
| --- | --- |
| upstream | [`davemckain/qtiworks`](https://github.com/davemckain/qtiworks), University of Edinburgh |
| grant | 🟢 **BSD-3-Clause**, `LICENSE.txt`, **`2,058 B`**, byte-read `2026-11-02` at `master` |
| fabricated control | 🟢 `404 14 B` |
| 🔴 API `spdx_id` | 🔴 **`NOASSERTION`** — the grant is prefaced by `6` lines of prose (`607-D`) |
| copyright | © **2014, University of Edinburgh** |
| maintained | 🟢 **`2026-06-30`** on the fork · 🔴 `2023-01-04` upstream, closed by its own README |
| channel flag | 🟡 `fork: true` |
| payload digest | 🟢 `a5c692f120907d58…` — **byte-identical** to upstream |

🟢 **Why the fork and not the upstream.** The upstream is closed by its author's own statement and
carries the ledger verdict `DECLINED-p436`. 🟢 **That decline was correct and it was about support,
not licence** — and the ledger already said so, naming the fork as the live carrier and recording the
same digest this pass recomputed. The platform row belongs to the maintained carrier.

### 🟢 Why this retires a flag `p604` raised against itself

🟡 `p604` shelved the QTI 3.0 toolchain with an explicit caveat: *"`4` repos, **one maintainer**,
flagged as such."* `p605` reported the tier *"no longer single-maintainer"* on the strength of two
MIT libraries. 🟢 **With QTIWorks the tier now spans four independent holders**, each byte-read today:

| layer | component | holder | grant |
| --- | --- | --- | --- |
| 🟢 **engine** | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | OpenOlat (Switzerland) | 🟢 **BSD-3-Clause**, `2,058 B` |
| player | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | amp-up.io | 🟢 **MIT**, `1,076 B` |
| library | [`kennisnet/php-qti3`](https://github.com/kennisnet/php-qti3) | 🟢 **Kennisnet** (Dutch national education-ICT body) | 🟢 **MIT**, `1,066 B` |
| library | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | Longsight Group | 🟢 **MIT**, `1,072 B`, pushed 🟢 **`2026-11-02`** |

🟢 **`kennisnet/php-qti3` is the row with institutional weight.** Kennisnet is the Netherlands'
public foundation for ICT in education — a national body publishing an MIT QTI 3.0 library. 🔴 It
carries `0★`, which is exactly `p601`'s star-anti-signal: the least-starred row in the tier is the
one with a ministry-adjacent holder behind it.

🔵 **What a studio gets from the four together:** a permissive path from authoring to scoring that
crosses no copyleft boundary and depends on no vendor — engine (BSD-3-Clause) + player (MIT) + two
MIT libraries, three of the four maintained within the last `12` months.

### 🟡 Platform-adjacent rows promoted this pass

| row | grant, byte-read `2026-11-02` | why a platform page |
| --- | --- | --- |
| [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) | 🟢 **MIT**, `1,066 B`, `main` | An **xAPI Learning Record Store** — the system of record a platform writes to, not a tool bolted beside it. EMEA (Poland) |
| [`DFE-Digital/education-benchmarking-and-insights`](https://github.com/DFE-Digital/education-benchmarking-and-insights) | 🟢 **MIT**, `1,091 B`, `main`, pushed `2026-11-01` | A **national ministry's** benchmarking platform, published permissively and actively developed. EMEA (UK) |
| [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | 🟢 **MIT**, `1,072 B`, `main`, `1,849★` | The Brazilian MCP server collection — the integration surface a LATAM engagement attaches agents through. LATAM |

### 🔴 This page's standing gaps, re-stated honestly

🔴 **The ERP/SIS gap is unchanged and this pass did not move it.** `p601` measured
`topic:school-management` at `88.9 %` in-domain yielding `0` shippable platforms; `p602` confirmed
the permissive education ERP the web names (`GegoK12`) has no shippable repository. 🟢 This pass
probed two more ERP-shaped backlog addresses and both are 🔴 **BLOCK — no grant**
(`quizbankorg/quizbank`, `eledia/moodle-block_elediaai_tutor`). The permissive education ERP of
record still does not exist; `openeducat/openeducat_erp` (LGPL-3.0) and `frappe/education` remain the
answer and both are reciprocal.

🟡 **`605-K` promotion debt after this pass, counted rather than asserted:** the measured debt was
`99` real repositories (`607-C`). This pass promoted **`26` distinct addresses**, of which 🟢 **`23`
pay debt** and `3` came from the LATAM national leg and were never in the ledger
(`eumakerdev/bncc_api`, `dfdb76/bncc-mcp`, `Universidade-Livre/ciencia-da-computacao`). 🟡 **`76`
remain.**

🔵 A first draft of this line said `73`, by subtracting promotions from debt without checking that
every promotion *was* debt. `3` were not. The figure is published from a set difference, not a
subtraction.

## 🆕 `p606` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THE PLATFORM THIS PAGE GAINS IS ONE THIS BASE HAS HAD IN `trending` SINCE `70★` AND SHELVED NOWHERE — AND IT IS THE OPEN-SOURCE ASSESSMENT PLATFORM **NIGERIA'S OWN EDTECH GAP ANALYSIS NAMES BY NAME**. 🟢 THE ROW AND THE REGIONAL EVIDENCE FOR IT ARRIVED IN THE SAME PASS, FROM THE NATIONAL QUERY LEGS `605-F` ASKED TO BE TESTED ON EMEA. 🔴 `605-K`'S PROMOTION DEBT: `3` PAID, `85` REMAIN.**

### 🟢 `606-I` — Tangerine: an EMEA/Africa field-assessment platform, promoted with its licence flagged

| platform | repo | grant (byte-read `2026-11-02`) | branch | stars | region | what it is |
| --- | --- | --- | --- | --: | --- | --- |
| **Tangerine** | [`Tangerine-Community/Tangerine`](https://github.com/Tangerine-Community/Tangerine) | 🟡 **GPL-3.0** (`512 B` read, control `404`) | `main` | 🟢 **`116`** | **EMEA** | Offline-first **field data collection for early-grade reading and maths assessment** (EGRA/EGMA), tablet-based, built for low-connectivity classrooms. Pushed `2026-09-04` |
| **tangy-form** | [`Tangerine-Community/tangy-form`](https://github.com/Tangerine-Community/tangy-form) | 🟡 **GPL-3.0** (`512 B` read, control `404`) | `master` | `16` | **EMEA** | The web-component form engine underneath Tangerine — the reusable half |
| **tangy-form-editor** | [`Tangerine-Community/tangy-form-editor`](https://github.com/Tangerine-Community/tangy-form-editor) | 🟡 **GPL-3.0** (`512 B` read, control `404`) | `master` | `5` | **EMEA** | Authoring UI for those forms. Pushed `2026-10-22` |

🔴 **Licence posture, stated plainly:** GPL-3.0 is **copyleft**, so this is a *deploy-and-extend*
platform in the same class as Moodle and Chamilo on this page — **not** a codebase to vendor into a
proprietary deliverable. A studio runs it, authors instruments for it and builds alongside it.
🟢 `tangy-form` matters precisely because it is the component layer: an AI scoring or
item-generation service talks to the form schema over its own boundary.

### 🟢 Why this row is worth a page entry and not a trending line

🔴 It was already in `repos/trending.md` — at `70★`, then `76★`, and on **no sell shelf**. That is
exactly `605-K`'s shape, and `gate-promotion-ledger` has been red about this class for ~`170`
passes. It is 🟢 **`116★` today**, so the carried figure was stale by `40★` as well as unshelved.

🟢 **What makes it shelvable now is `606-H`'s evidence, not its star count.** The national query leg
for Nigeria returned a gap analysis of **Nigeria's National EdTech Strategy (2025–2030)** that names
open-source tooling to build on — **RTI's Tangerine** among them — and recommends tuning open-weight
models on Nigerian educational content. So this page gains a platform *and* a sourced reason a
regional engagement would start from it.

🔵 The constraint that platform choice has to answer, from the same leg: 🔴 **`5.67 %` of Nigerian
public primary schools have computer facilities, against `54.55 %` of private schools.** An
offline-first, tablet-based assessment platform is a response to that number. A cloud-first LMS is
not.

### 🔴 This page's standing gaps, unchanged

| gap | state |
| --- | --- |
| 🔴 **ERP / SIS** | Unchanged since `p601`/`p602` re-measured it. `topic:school-management` is `88.9 %` in-domain and yields `0` shippable permissive platforms; `openeducat/openeducat_erp` (LGPL-3.0) and `frappe/education` are the honest ceiling |
| 🔴 `605-L` residual | The sweep for other root grant payloads that **grant nothing and name paths** is still not run. Population unmeasured |
| 🟡 `oppia/oppia` on this page | 🟢 Apache-2.0 **re-confirmed byte-read today**, `6,955★`, pushed `2026-11-02` — but see `606-G`: its README is at `.github/README.md` and every capability probe here reads it as absent |
## 🆕 `p605` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THE PLATFORM LAYER GAINS AN **ASSESSMENT-INTEROPERABILITY** TIER THAT IS NOW COMPLETE ENOUGH TO BUILD ON: `3` QTI 3.0 REPOS AND `2` LTI LIBRARIES, ALL MIT, ALL BYTE-READ TODAY. 🟢 AND THE FIRST ENTRY HERE FOR A **NATIONAL UNIVERSITY'S OWN LMS DEPLOYMENT** RATHER THAN A VENDOR PRODUCT. 🔴 THIS PAGE'S `74` PERMISSIVE-MARKED ROWS WERE PART OF `605-A`'S `400`-ADDRESS PAYLOAD SWEEP: `0` MARKUP DEFECTS FOUND HERE.**

### 🟢 Where this pass's rows attach to the platforms already on this page

🔵 This page's job is the **customisable system of record**. This pass did not find a new
platform; it found the **integration tier** that lets an agent reach the platforms already listed.

| Platform already here | 🆕 what `p605` adds beneath it | Grant | Region |
| --- | --- | --- | --- |
| **Canvas** (Instructure) | 🟢 [`psychquant/che-ntucool-mcp`](https://github.com/psychquant/che-ntucool-mcp) — CLI **and MCP server** for **NTU COOL**, National Taiwan University's Canvas deployment, verified live as a customised Canvas | 🟢 MIT (`1,065 B`) | APAC |
| **Google Classroom** | [`OmarNiazi/classroom-mcp`](https://github.com/OmarNiazi/classroom-mcp) — courses, rosters, coursework, submissions as agent tools. 🟡 `0★`, flagged | 🟢 MIT (`1,066 B`) | APAC |
| **Moodle / Open edX / Canvas** (LTI consumers) | [`DecoyLex/ltix`](https://github.com/DecoyLex/ltix) (Elixir, on Hex) and [`iamlucasb/lti-core`](https://github.com/iamlucasb/lti-core) | 🟢 MIT | NA / APAC |
| **H5P** | 🟢 [`otacke/h5p-theme-picker`](https://github.com/otacke/h5p-theme-picker) — 🔵 exists because **H5P.com ships a theme picker and H5P Group did not release the code** | 🟢 MIT (`1,072 B`) | EMEA |
| **QTI 3.0** (the assessment interchange standard) | [`pie-framework/pie-qti`](https://github.com/pie-framework/pie-qti), [`sonyccd/qti-playground`](https://github.com/sonyccd/qti-playground), [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer) | 🟢 MIT | NA / APAC |
| **xAPI / LRS** (Learning Locker, Yet Analytics) | [`yetanalytics/pedestal-oidc`](https://github.com/yetanalytics/pedestal-oidc) — the auth rung under a learning-record service | 🟢 Apache-2.0 (`11,356 B`) | NA |

### 🟢 The QTI 3.0 toolchain is no longer single-maintainer — which was `p604`'s own flag

🟡 `p604` shelved [`metyatech/qti-reporter`](https://github.com/metyatech/qti-reporter) at `0★` and
flagged the whole QTI axis as **one maintainer**. 🟢 That flag is now partly discharged:

| QTI repo | maintainer | role | ★ |
| --- | --- | --- | --: |
| [metyatech/qti-reporter](https://github.com/metyatech/qti-reporter) | `metyatech` | 🟢 results → HTML + aggregate CSV (`p604`) | `0` |
| 🆕 [metyatech/qti-html-renderer](https://github.com/metyatech/qti-html-renderer) | `metyatech` | 🟢 items → HTML — the declared companion | `0` |
| 🆕 [pie-framework/pie-qti](https://github.com/pie-framework/pie-qti) | 🟢 **`pie-framework`** | 🟢 parsing / transformation inside an assessment-element framework | `4` |
| 🆕 [sonyccd/qti-playground](https://github.com/sonyccd/qti-playground) | 🟢 **`sonyccd`** | 🟢 view / edit / learn the standard | `4` |

🟢 **Three independent maintainers now, not one** — 🔵 and `p364`'s companion-closure question is
answered for this platform: the companion `qti-reporter` declared does exist and is now shelved
beside it. 🟡 All four remain small; the axis is shelved for **the standard**, which is
institution-mandated, not for the star counts.

### 🟢 Why an MCP server against *one university's* LMS belongs on a platform page

🔵 [`psychquant/che-ntucool-mcp`](https://github.com/psychquant/che-ntucool-mcp) targets a single
institution — NTU COOL — which looks like the opposite of a platform row. 🟢 **It is on this page
because of what it proves:** a national university's LMS is a **customised** Canvas, and the
customisation is discoverable and scriptable. 🔵 That is the generalisable fact. A client's "we run
Canvas" almost never means vanilla Canvas, and this repo is a worked example of finding the
delta and wrapping it as tools rather than assuming the vendor API.

### 🔴 This page in `605-A`'s sweep

🔵 `74` of the `400` addresses swept for `604-B`'s HTML-capture defect came from this page.
🟢 **`0` defects found here.** 🔵 The single base-wide hit,
[`uPortal-Project/FeedbackPortlet`](https://github.com/uPortal-Project/FeedbackPortlet), is on
[`../repos/trending.md`](../repos/trending.md), not on a platform shelf. Ledger:
[`../evidence/shelf-payload-markup-sweep.2026-11-02-p605.tsv`](../evidence/shelf-payload-markup-sweep.2026-11-02-p605.tsv).

## 🆕 `p604` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THE PLATFORM FINDING OF THIS PASS IS A LICENCE ONE: THE APEREO STACK — SAKAI, uPORTAL, CAS, AND THE WHOLE LEARNING-ANALYTICS TIER — IS THE DEEPEST POOL OF **INSTITUTION-GRADE PERMISSIVE** EDUCATION SOFTWARE, AND A DEPENDENCY SCREEN READING `spdx_id` REJECTS `10 of 11` OF ITS ECL-2.0 REPOSITORIES AS UNLICENSED. 🟢 MEASURED ACROSS `91` REPOSITORIES, `61` GRANTS BYTE-READ.**

### 🟢 Why this is a platform row and not only a methodology note

🔵 The platforms on this shelf are the systems a client **already runs**. 🟢 The Apereo
family is the part of that estate that is *permissively licensed*, which makes it the part
Globant can extend and redistribute rather than merely integrate with:

| Platform | Grant (byte-read `2026-11-02`) | What an institution runs it for |
| --- | --- | --- |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** (`11,120 B`, `master`) | A full LMS — the open alternative to Canvas/Blackboard in higher ed |
| [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | 🟢 **Apache-2.0** (`11,359 B`, `master`, `287★`) | The campus portal layer — where a student actually lands |
| [apereo/cas](https://github.com/apereo/cas) | 🟢 **Apache-2.0** (`11,358 B`, `11,392★`, pushed `2026-11-02`) | 🟢 **Single sign-on.** The most actively maintained row in the family and the one every AI feature must authenticate through |
| [Apereo-LAI/OpenLRS](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS) | 🟢 **ECL-2.0** (`11,085 B`) 🔴 API: `NOASSERTION` | An **xAPI learning-record store** — the system of record for learner interaction data |
| [Apereo-LAI/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | 🟢 **ECL-2.0** (`9,877 B`) 🔴 API: `NOASSERTION` | The learning-record **warehouse** above the LRS |
| [Apereo-LAI/LearningAnalyticsProcessor](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | 🟢 **ECL-2.0** (`9,919 B`) 🔴 API: `NOASSERTION` | The batch **processing tier** that turns records into risk/engagement signals |

🔴 **The commercial consequence, stated plainly.** 🟢 **ECL-2.0 is Apache-2.0 with the patent
grant narrowed to education use** — permissive, commercially usable, and written by this
sector for itself. 🔴 But it is rare enough that licence scanners do not model it: the GitHub
API returns `NOASSERTION` for `10 of the 11` ECL-2.0 repositories in the Apereo orgs, and a
procurement or OSS-review gate wired to `spdx_id` will therefore mark **Sakai's entire
analytics stack as unlicensed and block it.** 🟡 The fix is a one-line allowlist entry, and
the cost of not having it is an engagement losing access to the only open learning-analytics
tier that exists at institutional grade.

### 🟡 The dormancy caveat, because the shelf should not oversell it

| | |
| --- | --- |
| 🟢 live and actively maintained | `apereo/cas` (`2026-11-02`), `sakaiproject/sakai` (`2026-10-30`), the `uPortal-Project` portlets (most pushed `2026-10`) |
| 🟡 reference-grade, not live | the **Learning Analytics Initiative** tier — newest HEAD in the org is `2025-09-12`, most rows `2017`–`2020` |

🔵 So the honest recipe is: **run the live tier, read the dormant one.** The LAI repositories
are the best available specification of the education-analytics data model (`lai-event`,
`lai-model`) and should be treated as a schema source rather than an upstream dependency.

### 🟢 New platform-adjacent rows this pass

| Platform / tool | Grant (byte-read) | Branch | Region | Role |
| --- | --- | --- | --- | --- |
| [cloudpedagogy/cloudpedagogy-moodle-course-auditor](https://github.com/cloudpedagogy/cloudpedagogy-moodle-course-auditor) | 🟢 **MIT** (`1,069 B`) | `main` | EMEA | 🟢 Audits **Moodle `.mbz` backups** offline. 🔵 The migration/quality tool for the single most-deployed LMS on this shelf, and it needs **no credentials on the live instance** |
| [ucfopen/quiz-extensions](https://github.com/ucfopen/quiz-extensions) | 🟢 **MIT** (`1,129 B`) | `master` | North America | A **Canvas** LTI tool for bulk quiz-time accommodations — published by a university, in production at one |
| [tl-its-umich-edu/instructor-tools](https://github.com/tl-its-umich-edu/instructor-tools) | 🟢 **Apache-2.0** (`11,356 B`) | `main` | North America | LTI-launched instructor tooling from **University of Michigan** — the pattern for adding a tool to an LMS an institution already runs |
| [otacke/h5pxapikatchu](https://github.com/otacke/h5pxapikatchu) | 🟢 **MIT** (`1,051 B`) | `master` | EMEA | Turns a **WordPress + H5P** estate into an xAPI data source — the cheapest on-ramp from content to measurement |

🔵 **A note on `ucfopen` as a publisher.** The org holds `65` repositories, and its licence
posture splits sharply: 🟢 the **LTI tooling and API clients are MIT**
([`canvasapi`](https://github.com/ucfopen/canvasapi), `681★`), while 🔴 the **learning-content
platforms are copyleft** — [`Obojobo`](https://github.com/ucfopen/Obojobo) and
[`Materia`](https://github.com/ucfopen/Materia) are **AGPL-3.0**, and
[`UDOIT`](https://github.com/ucfopen/UDOIT) (the accessibility checker, `117★`) is
**GPL-3.0**. 🟢 **The same split this base has recorded globally holds inside a single
university's org: the integration layer is permissive, the platform is copyleft.**

## 🆕 `p603` — reads `2026-11-02`, commit `2026-11-02` — **🟢 `11` PLATFORMS PROMOTED OUT OF THE `p436` BACKLOG, EVERY GRANT BYTE-READ AT THE REAL DEFAULT BRANCH, EVERY CONTROL AT `404`. 🟢 THE BEST OF THEM IS A **LATAM** ROW THIS BASE HAD CLAIMED IN `trending` AND NEVER SHELVED: BRAZIL'S **BNCC NATIONAL CURRICULUM** AS AN `npm` PACKAGE, A `PyPI` PACKAGE AND AN **MCP SERVER** — `1,721` VERIFIED LEARNING OBJECTIVES. 🔴 AND IT CARRIES A **SPLIT-SCOPE GRANT WHOSE SECOND HALF IS IN A SUBDIRECTORY**: A ROOT-ONLY READ PUBLISHES "MIT" FOR A PAYLOAD THAT IS CC BY 4.0. 🔴 `603-E`: THE `14` BACKLOG REPOS WITH **NO GRANT AT ALL** ARE NOT RANDOM — `9` OF THEM ARE FRANCOPHONE OR INDONESIAN SCHOOL APPS.**

### 🔴 The BNCC split-scope grant, read to the bottom because the top is misleading

🟢 [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) is the **Base Nacional
Comum Curricular** — the Brazilian national curriculum — *"consumível em uma linha de
código"*: `1,721` learning objectives for basic education, verified against the official
**MEC/CNE** documents, shipped as an npm package, a PyPI package **and an MCP server**.

🔴 **Its root `LICENSE` is not a licence.** It is a `1,298 B` router that says the repository
uses two, and points elsewhere:

| path | bytes | grant | covers |
| --- | --: | --- | --- |
| `LICENSE` (root) | `1,298` | 🔴 **router only — not a grant** | — |
| `LICENSE-CODIGO.md` | `1,107` | 🟢 **MIT** | `packages/*/src/`, `python/bncc/*.py`, `mcp-worker/src/`, `scripts/`, tests, config |
| `LICENSE-DADOS.md` | `1,108` | 🟡 **CC BY 4.0** | the curriculum JSON in `packages/bncc/dados/`, `python/bncc/dados/` |

🔵 **The data is not native to that repo**: it is synced from a *pinned commit* of
[`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) and keeps the grant from
there. 🔴 **And that upstream repo is where the trap closes** — its root `LICENSE` is a clean
`1,091 B` **MIT**, while the data grant sits at **`dados/LICENSE.md` (`1,583 B`, CC BY 4.0)**:

| | what a probe reads | what is true |
| --- | --- | --- |
| 🔴 root-only read of `bncc-dados` | **MIT** | 🔴 wrong for the payload anyone actually wants |
| 🟢 root **+ README-linked subdirectory** | MIT *(code in `pipeline/`)* **+ CC BY 4.0** *(`dados/`)* | 🟢 correct |

🟢 **This is `p969-root-only-licence-reach` reproduced live on a platform this base wants**,
and it is the exact case the library's D2 rung exists for — the README *does* link
`dados/LICENSE.md`, so the rung would fire here. 🔵 **Both repositories' controls are `404`**
(`LICENSE-FABRICATED-p603-control`, `dados/LICENSE-FABRICATED-p603.md`), so the reads are
real absences, not proxy noise.

🟢 **The legal note is worth more to a LATAM engagement than the licence string**, and it is
in the upstream README: the BNCC's normative texts are **official acts, not protected by
copyright** under *art. 8º, IV da Lei 9.610/98*; the CC BY 4.0 therefore covers **the
compilation, structuring and curation**, whose rights belong to **Profy Tecnologias
Educacionais Ltda** (the holder byte-read in both grant files). 🔵 So attribution is owed to
the compiler, not to the curriculum.

### 🟢 Platforms promoted to this page — `11` rows

| Platform | Grant (byte-read) | Branch | Pushed | tz | Region | What it is |
| --- | --- | --- | --- | --- | --- | --- |
| [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes) | 🟡 **MIT** (`1,107 B`, `LICENSE-CODIGO.md`) **+ CC BY 4.0** (`1,108 B`, `LICENSE-DADOS.md`) | `main` | `2026-10-15` | `-03:00` | **LATAM** | 🟢 BNCC as npm + PyPI + **MCP server**; `1,721` objectives verified against MEC/CNE |
| [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) | 🟢 **MIT** (`1,118 B`) | `master` | `2026-11-01` | `+08:00` | **APAC** | 🟢 Open-source **gamified** learning platform, Rails; pushed the day of this pass. The most actively maintained platform in the whole backlog |
| [wort-schule/wort.schule](https://github.com/wort-schule/wort.schule) | 🟢 **MIT** (`1,074 B`) | `main` | `2026-10-26` | `+01:00` | **EMEA** | German vocabulary/word-study school platform on Rails + PostgreSQL |
| [nvaes/CEB](https://github.com/nvaes/CEB) | 🟢 **MIT** (`1,239 B`) | `main` | `2026-10-25` | `+01:00` | **EMEA** | 🟢 **CEB** revision site (Certificat d'Études de Base, Fédération Wallonie-Bruxelles) built **automatically from the official past-year PDFs** — the same pattern as BNCC, one country over |
| [diego-costanzo/tournesol-scolaire](https://github.com/diego-costanzo/tournesol-scolaire) | 🟢 **MIT** (`1,070 B`) | `main` | `2026-09-25` | `+02:00` | **EMEA** | *Tournesol* — French smart homework book, timetable and active revision, CM1→Terminale |
| [RF1705/beste-schule](https://github.com/RF1705/beste-schule) | 🟢 **MIT** (`1,062 B`) | `main` | `2026-10-06` | `+02:00` | **EMEA** | 🔵 **Home Assistant** integration for `beste.schule` — timetables, absences, homework, tests, grade averages. An unusual surface: the school record in home automation |
| [Antonio-Neves/Gestao-Escolar](https://github.com/Antonio-Neves/Gestao-Escolar) | 🟢 **MIT** (`1,077 B`) | `master` | `2026-10-12` | `-03:00` | **LATAM** | Brazilian *Sistema de Gestão Escolar*. 🟡 **Its own README says "under development"** — carried as such, not as a shippable platform |
| [telekom/ki-in-schulen](https://github.com/telekom/ki-in-schulen) | 🟢 **MIT** (`1,227 B`) | `master` | `2025-06-04` | `+02:00` | **EMEA** | 🟢 *AI@School* from **Deutsche Telekom** — teaching material bringing AI into schools playfully. A named corporate holder, which matters for reuse |
| [SaidBySolo/neispy](https://github.com/SaidBySolo/neispy) | 🟢 **MIT** (`1,066 B`) | `master` | `2025-11-19` | `+09:00` | **APAC** | Sync **and** async wrapper for Korea's **NEIS** open education API; a 2020 Korean OSS competition prize-winner |
| [hisahonakata/roster_hub_for_gigaschool](https://github.com/hisahonakata/roster_hub_for_gigaschool) | 🟢 **Apache-2.0** (`11,356 B`) | `main` | `2023-08-05` | `+09:00` | **APAC** | Takes **OneRoster CSV** in and serves a **OneRoster API** out — the rostering adapter for Japan's GIGA School estate. 🟡 Dormant since `2023-08` |
| [schild-report/schild.report](https://github.com/schild-report/schild.report) | 🟢 **MIT** (`1,054 B`) | `master` | `2022-05-22` | `+02:00` | **EMEA** | Replaces the report designer shipped with **SchILD** (the North-Rhine-Westphalia school database). 🔴 **Dormant since `2022-05`** — reference implementation, not a dependency. 🔵 README at `Readme.md`, one of the `603-C` six |

### 🔴 `603-E` — the repos with no grant at all are a *region*, not noise

🟢 `14` of the `108` backlog repositories have **no licence file at any ladder rung** —
probed today across the full case- and extension-varied ladder plus the README link, with
the branch resolved by symref. 🔴 **They are not randomly distributed:**

| cluster | repos | addresses |
| --- | --: | --- |
| 🔴 **francophone school apps** | `7` | `Bendjou-art/Correct-QCM`, `Emmanuel26-code/cahier-texte-numerique`, `NZOKOS06/gestion_school`, `kbma/gestion-scolaire`, `mael12854/preau`, `olibertrand/questionnapp`, `Solemntumult/EcoGes` |
| 🔴 **Indonesian school apps** | `2` | `nwmustofa/e-rts`, `twakew/e-rapor` *(e-rapor = report card)* |
| other / unplaced | `5` | `EDUQUEST2026-2027/EDUQUEST` (branch 🔴 `eduquest-main`), `ProfFranco/check-app`, `quizbankorg/quizbank`, `techpivot25/Educate-AI`, `Naresh1401/education-tutor-agent` |

🔵 **Why this is a finding and not a tidying note.** `9 of 14` ungranted repositories are
EMEA-francophone or APAC-Indonesian school apps — 🟢 **so in exactly the two sub-regions
where this page's platform coverage is thinnest, local supply does exist and is
unusable.** 🔴 The constraint is not that nobody is building school software in francophone
Africa/Europe or Indonesia; it is that **it ships without a grant**, so Globant cannot
build on it and neither can anyone else.

🟢 **That makes it an actionable ask rather than a gap**: a maintainer who published public
code and no licence has usually not refused — the base already distinguishes
`DECLARED-NOT-GRANTED` from `NO-PAYLOAD` for this reason. 🔵 **An upstream licence request to
these `9` is the cheapest regional supply this page could gain**, and it is cheaper than
finding nine new platforms. Full rows, branches and ladder verdicts in
[`../evidence/backlog-regrade.2026-11-02-p603.tsv`](../evidence/backlog-regrade.2026-11-02-p603.tsv).

## 🆕 `p602` — reads `2026-11-02`, commit `2026-11-02` — **🔴 THIS PASS DRAFTED "THE ERP/SIS GAP MOVES — TWO PLATFORMS WERE INVISIBLE BECAUSE OF THEIR BRANCH NAMES" AND IT IS **FALSE**: THIS PAGE ALREADY NAMES `openeducat/openeducat_erp` (BRANCH `19.0`, LGPL-3.0, `8,241 B`) AND `frappe/education` (BRANCH `develop`, `19`-BYTE `license.txt`), BRANCHES AND GRANT BYTES INCLUDED. 🟢 SO THE GAP IS RE-STATED, NOT MOVED — AND WHAT IS GENUINELY NEW IS SMALLER AND HONEST: `2` NEW ADDRESSES, AND A **DISCONFIRMATION** — THE MIT EDUCATION ERP THE WEB NAMES (`GegoK12`) HAS NO SHIPPABLE REPOSITORY AT ALL.**

### 🔴 The restatement, named before anything new, because this page's gap depends on it

🔴 **Struck from this pass's draft:** that `openeducat` and `frappe/education` were newly shipped and
previously invisible. 🟢 **They are already on this page**, with their version-numbered and `develop`
default branches explicitly called out, and with `openeducat`'s `8,241 B` LGPL-3.0 grant byte-read at
branch `19.0`. 🔵 **This pass re-measured both independently and agrees with the existing rows** —
`openeducat` LGPL-3.0 `8,241 B` at `19.0`, `frappe/education` a `19`-byte `license.txt` reading in full
`License: GNU GPL V3` — 🟢 which is worth something as a **reproduction check** and nothing as a
discovery. The ERP/SIS gap statement on this page stands as written.

### 🟢 Genuinely new this pass — `2` addresses, both confirmed unheld by the corrected matcher

| Platform | ★ | Grant (byte-read) | Branch | Region | What it is |
| --- | --: | --- | --- | --- | --- |
| [Ansarimajid/College-ERP](https://github.com/Ansarimajid/College-ERP) | `201` | 🟢 **MIT** (`1,075 B`) | `main` | Global | 🟡 Django college ERP — **permissive**, but a single-maintainer app, not a platform with a module ecosystem. Pushed `2026-04-28` |
| [navariltd/Junior-School](https://github.com/navariltd/Junior-School) | `21` | 🟡 AGPL-3.0 (`34,523 B`, 🔴 `license.txt`) | 🔴 `develop` | Global | 🟢 Proof the Frappe path is **extensible in practice**: a third-party app extending `frappe/education`. Pushed `2026-09-14` |

🔵 **Why `Junior-School` earns a row despite `21★`.** This page's standing question about
`frappe/education` is whether anyone builds on it. 🟢 **Someone does, in public, with a byte-read
grant** — that is a maintainability signal about the *platform*, which is what a studio is buying.

### 🟢 A disconfirmation: the MIT education ERP the web names does not exist

The mandated leg `open source platform education ERP CRM MIT Apache` returned **GegoK12** as "an open
source school ERP released under the MIT licence". 🔴 **It does not resolve to a usable repository:**

| address found | ★ | ladder result | control | verdict |
| --- | --: | --- | --- | --- |
| [RukkmaniT/gegok12-documentation](https://github.com/RukkmaniT/gegok12-documentation) | `0` | 🔴 no grant file (`25` names, real default branch) | `404` | 🔴 documentation stub |
| `Gego-K12/.github` | `0` | — | — | 🔴 org profile placeholder only |

🟢 **So this page's oldest gap is confirmed from a new direction:** a *permissive* education ERP at
platform scale does not exist, and the one the web advertises as MIT is a vendor marketing claim with
no code behind it. 🔵 **A vendor page claiming a licence is not a licence finding** — resolve the claim
to an address, then byte-read the address. 🟡 **The only MIT row on this page remains a
single-maintainer Django app.**

### 🔴 Platform-shaped addresses found and rejected this pass

| address | ★ | grant (byte-read) | why rejected |
| --- | --: | --- | --- |
| [ketanchoyal/Our-E-School](https://github.com/ketanchoyal/Our-E-School) | `504` | 🟢 MIT (`1,069 B`) | 🔴 **Abandoned — last push `2021-08-19`.** Flutter app, not a platform 🔴 **ARCHIVED (read-only) — measured `p637`** |
| [jobic10/student-management-using-django](https://github.com/jobic10/student-management-using-django) | `393` | 🟢 MIT (`1,075 B`) | 🔴 Last push `2023-11-04`; coursework-scale |
| [mindsdb/edux](https://github.com/mindsdb/edux) | `6` | 🟢 MIT (`1,068 B`) | 🔴 Last push `2020-07-01`; an Open edX *theme*, not a platform 🔴 **ARCHIVED (read-only) — measured `p637`** |
| [codern-org/codern](https://github.com/codern-org/codern) | `29` | 🔴 **grantless** | 🔴 `25`-name ladder misses at `main`; `README.md` has a `## License` heading and **no grant**. Control `404` |
| [krayin/agent-skills](https://github.com/krayin/agent-skills) | `2` | 🔴 **grantless** | 🔴 Same vendor as this page's MIT `krayin/laravel-crm` — 🔴 **the child does not inherit the parent's grant** |

Evidence: [`../evidence/grants-byteread.2026-11-02-p602.tsv`](../evidence/grants-byteread.2026-11-02-p602.tsv),
[`../evidence/held-set-matcher-correction.2026-11-02-p602.tsv`](../evidence/held-set-matcher-correction.2026-11-02-p602.tsv).

## 🆕 `p601` — reads `2026-11-01`, commit `2026-11-02` — **🟢 AN ASSESSMENT-DELIVERY PLATFORM TIER, NEW ON THIS PAGE: THE LAYER THAT RENDERS AND SCORES AN ITEM, WHICH `600` PASSES OF TUTOR AND LMS ROWS ASSUMED AND NEVER NAMED. `4` PLATFORMS, `4,918★` DOWN TO `327★`, ALL MIT OR APACHE-2.0, ALL BYTE-READ. 🔴 AND THE ERP/SIS GAP — THIS PAGE'S OLDEST — IS RE-MEASURED AGAINST ITS WHOLE POPULATION FOR THE FIRST TIME: `topic:school-management` IS `88.9 %` IN-DOMAIN AND YIELDS `0` SHIPPABLE PLATFORMS. THE GAP IS CONFIRMED, WITH `18` ADDRESSES OF EVIDENCE.**

### 🟢 The assessment-delivery tier — platforms a studio attaches AI to, rather than rebuilds

| Platform | ★ | Grant (byte-read `2026-11-01`) | Branch | Region | What it is, and the AI seam |
| --- | --: | --- | --- | --- | --- |
| [surveyjs/survey-library](https://github.com/surveyjs/survey-library) | **4,918** | 🟢 MIT (`1,102 B`) | 🔴 `master` | **EMEA** | JSON-schema form/quiz runtime (React, Angular, Vue, vanilla). 🟢 **An item generator emits JSON; this renders, validates and scores it.** Devsoft Baltic OÜ (EE) |
| [didi/xiaoju-survey](https://github.com/didi/xiaoju-survey) | **3,803** | 🟢 Apache-2.0 (`11,412 B`) | `main` | **APAC** | Deployable questionnaire/exam/quiz **service** with analytics — not a library. DiDi (CN). 🟢 The APAC-sovereign option when data must stay in-region |
| [nymanjens/quizmaster](https://github.com/nymanjens/quizmaster) | `327` | 🟢 Apache-2.0 (`591 B`) | 🔴 `master` | Global | Synchronous multi-participant quiz runner — the live/proctored session shape |
| [2anki/2anki.net](https://github.com/2anki/2anki.net) | `328` | 🟢 MIT (`LICENSE.md`, `1,310 B`) | `main` | Global | Notion → Anki pipeline; 🟢 feeds the **spaced-repetition tier `p600` opened on this page** from institutional notes |

🔵 **Why this tier was missing, stated plainly.** This page has carried LMS platforms (Moodle,
Open edX, Sakai, Chamilo, ILIAS, OpenOLAT, Canvas) and `p600` added retention. 🔴 **An LMS stores and
tracks; it does not author or score free-form items well, which is exactly why every AI-tutor recipe
on `compose/patterns.md` had to hand-wave the delivery step.** 🟢 These four are that step, under
permissive grants, and two of them are full services rather than libraries.
🟡 **Limit:** none implements **QTI**, so interchange with an existing assessment estate is bespoke work.

### 🟢 Teaching platforms — classroom-shaped, permissive, and one is APAC-sovereign

| Platform | ★ | Grant (byte-read) | Branch | Region | Note |
| --- | --: | --- | --- | --- | --- |
| [open-scratch/teaching-open](https://github.com/open-scratch/teaching-open) | `633` | 🟢 Apache-2.0 (`11,371 B`) | 🔴 `master` | **APAC** | 🟢 **Scratch + ScratchJr + Python teaching platform with courses, classes, assignments, permissions and community** — a complete K-12 coding school in one deployable, CN-built and CN-localised |
| [tristcoil/hanabira.org](https://github.com/tristcoil/hanabira.org) | `432` | 🟢 MIT (`1,061 B`) | `main` | **APAC** | Self-hostable Japanese **and** Korean learning portal — language-school shape |
| [Attendize/Attendize](https://github.com/Attendize/Attendize) | **4,283** | 🟢 Attribution Assurance Licence (`2,073 B`) | 🔴 **`develop`** | Global | Ticketing/attendee management for open days, orientation, CPD. 🟡 AAL is OSI-approved but rare — read its attribution clause before white-labelling |
| [AhmadHassan-BTed/Attendify](https://github.com/AhmadHassan-BTed/Attendify) | **3,836** | 🟢 MIT (`1,056 B`) | `main` | Global | Attendance **and leave** portal — the only substantial permissive repo in its axis |

### 🔴 The ERP / SIS gap — re-measured against its full population, and confirmed

`p599` and `p600` carried this as this page's oldest open gap. This pass measured the axis exhaustively
rather than sampling it: **`topic:school-management` + `topic:student-information-system` +
`topic:student-management`, `30` addresses each.**

| | result |
| --- | --: |
| in-domain relevance of `topic:school-management` | 🟢 **`88.9 %`** — the cleanest axis measured this pass |
| addresses unheld | `18` |
| 🔴 **shippable platforms** (permissive **and** `≥ 300★` **and** pushed since `2025-06`) | 🔴 **`0`** |
| largest address in the axis | `ketanchoyal/Our-E-School` — `504★`, MIT, 🔴 **last pushed `2021-08-19`** |
| remainder | `43–138★`, PHP/Laravel/Flask/MERN coursework projects, majority last pushed before `2025` |

🟢 **So the gap is not an artefact of a narrow search — it is a property of the sector.** The axis is
unambiguous (no homonym contamination: `88.9 %` in-domain), it is well populated (`18` unheld
addresses), and it contains **no permissive, maintained, substantial student-information system.**
🔵 **What that means for an engagement:** SIS/ERP remains **buy-or-build**, and the credible open
anchors stay the ones this page already names — `frappe/education` (🔴 `19`-byte `license.txt` naming
GPL-3 without granting it, `600-H`), `OpenEduCat` (LGPLv3, Odoo-dependent) and `ERPNext` (GPL-3) —
**all three reciprocal or defective, none permissive.** 🟡 Unchanged from `p600`; now evidenced rather
than asserted.

### 🔴 Platform-shaped addresses found and rejected this pass

| Address | ★ | Grant (byte-read) | Why rejected |
| --- | --: | --- | --- |
| [TheOdinProject/curriculum](https://github.com/TheOdinProject/curriculum) | **13,200** | 🔴 CC BY-NC-SA (`license.md`, `442 B`) | NonCommercial **and** ShareAlike — cannot enter paid delivery |
| [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | **4,041** | 🔴 **grantless** — no file at `main`, control `404` | All rights reserved by default |
| [AhmadHassan-BTed/Turnitout-Humanizer](https://github.com/AhmadHassan-BTed/Turnitout-Humanizer) | **11,200** | 🔴 *"Proprietary License … All rights reserved"* (`800 B`) | 🟡 Same author as `Attendify` above, opposite grant — **per-repo probes, never per-author** |
| [Yogndrr/MERN-School-Management-System](https://github.com/Yogndrr/MERN-School-Management-System) | `648` | 🔴 licence field `NONE` | The axis's second-largest address, and grantless |

🔵 **One author, two grants.** `AhmadHassan-BTed` ships `Attendify` under MIT and
`Turnitout-Humanizer` as proprietary. 🟢 **Rung for this page: a grant verified on one repository
tells you nothing about its neighbour, even under the same owner** — every row above was probed
individually, each with its own fabricated-path control at `404`.
Evidence: [`../evidence/grants-byteread.2026-11-01-p601.tsv`](../evidence/grants-byteread.2026-11-01-p601.tsv),
[`../evidence/axis-relevance-funnel.2026-11-01-p601.tsv`](../evidence/axis-relevance-funnel.2026-11-01-p601.tsv).

## 🆕 `p600` — `2026-11-01` — a permissive, self-hostable retention platform tier finally exists on this page, and the ERP/SIS gap moves for the first time in many passes

### 🟢 The spaced-repetition / retention tier — new on this page

🔵 **Why it belongs here rather than on [`../agents/top.md`](../agents/top.md):** these are *systems*
a client runs, with their own storage, scheduling and UI — the same category as Moodle or Kolibri,
one layer down. Every grant byte-read `2026-11-01` at the real default branch; every repo's
fabricated-path control returned `404`.

| Platform | Repo | ★ | Grant (byte-read) | Branch | Customisable with AI on top? |
| --- | --- | --: | --- | --- | --- |
| **flashcards-obsidian** | [reuseman/flashcards-obsidian](https://github.com/reuseman/flashcards-obsidian) | **1,113** | 🟢 **MIT** (`1,069 B`) | `main` | 🟢 **Yes** — notes→cards pipeline; an agent writes the markdown, the plugin schedules it. Pushed `2026-10-31` |
| **memcode** | [lakesare/memcode](https://github.com/lakesare/memcode) | **408** | 🟢 **MIT** (`1,080 B`) | 🔴 **`master`** | 🟢 **Yes** — hostable web SRS with public decks; the multi-tenant option |
| **repeater** | [shaankhosla/repeater](https://github.com/shaankhosla/repeater) | **442** | 🟢 **Apache-2.0** (`11,357 B`) | `main` | 🟢 **Yes** — terminal-native, so it embeds in a CLI tutor with **no hosting, no auth, no UI** |
| **memo** | [olmps/memo](https://github.com/olmps/memo) | **1,871** | 🟢 **BSD-3-Clause** (`1,515 B`) | `main` | 🟡 **Reference only** — Flutter mobile SRS, last push `2024-07-29` |
| **scholarsome** | [hwgilbert16/scholarsome](https://github.com/hwgilbert16/scholarsome) | **793** | 🔴 **AGPL-3.0** (`34,523 B`) | 🔴 **`develop`** | 🔴 **Reciprocal — do not vendor into a client product.** The most feature-complete of the set, which is exactly why the grant matters |
| **mnemosyne** | [mnemosyne-proj/mnemosyne](https://github.com/mnemosyne-proj/mnemosyne) | **605** | 🔴 **pointer, not a grant** (`156 B`) | `master` | 🔴 **BLOCK** — the file says only *"Different parts of the software use different licenses:"*. `600-G` |

🔵 **The commercially useful shape of this tier:** `4 of 6` are permissive and `2 of 6` are not, and
🔴 **the two that are not are the two a feature comparison would pick first** (`scholarsome` is the
most complete web app; `mnemosyne` the most mature desktop one). That is `599-C`'s pattern inverted —
here the licence risk sits at the *top* of the quality ranking, not in the unaudited tail.

### 🟢 The ERP / SIS gap moves — the oldest open gap on this page, narrowed and NOT closed

This page has carried *"no permissive education ERP/SIS of record"* as its oldest unclosed gap. The
field measured again this pass:

| Platform | Grant | Branch | Verdict |
| --- | --- | --- | --- |
| [frappe/education](https://github.com/frappe/education) | 🔴 **`19 B` pointer** — `license.txt`, in full: `License: GNU GPL V3` | 🔴 **`develop`** | 🔴 **Reciprocal, and the grant names a licence without granting one** (`600-H`). 🔴 Only the **lowercase** path resolves |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL-3.0 | 🔴 **`19.0`** | 🔴 Reciprocal; and the branch is a *version number*, which no `main`/`master` probe resolves |
| [RosarioSIS](https://www.rosariosis.org/) | 🔴 GPL-2.0 | — | 🔴 Reciprocal |
| GegoK12 | 🟡 MIT claimed by vendor site | — | 🟡 **Unverified — no canonical repo address resolved this pass**; recorded as a lead, not a row |
| 🆕 [weidonglang/EduNexus-AI](https://github.com/weidonglang/EduNexus-AI) | 🟢 **MIT** (byte-read, `1,071 B`) | `main` | 🟢 **First permissive address this page has ever held in this category** — and it is `5★`, a graduation-project-scale Spring Boot + Vue 3 teaching-administration system |

🔵 **So the gap narrows in a specific and limited way:** 🟢 a permissively-licensed education
administration system now *exists* on this page, 🔴 **and it is nowhere near institution-grade.** The
honest statement for a proposal is that **the permissive SIS must still be built, not adopted** —
but `EduNexus-AI` is now a readable reference for the data model rather than a blank sheet. 🔴 **Gap
re-registered as narrowed, not closed.**

### 🟢 `600-D` — an `81`-repo permissive curriculum estate, relevant here as *content* for the platforms above

[`MathWorks-Teaching-Resources`](https://github.com/MathWorks-Teaching-Resources) — `81` repos, mostly
**BSD-3-Clause**, undergraduate STEM courseware. 🔵 **It is not a platform, so it is not a row in the
tables above** — it is the thing a studio *loads into* Moodle, Open edX or Kolibri when the client is
an engineering faculty. 🟡 **MATLAB/Simulink runtime is commercial**; the course content is
permissive. 🔴 `59 of 81` default to branch `release`, which is why `599` passes never saw it. Census:
[`../evidence/mathworks-curriculum-census.2026-11-01-p600.tsv`](../evidence/mathworks-curriculum-census.2026-11-01-p600.tsv).

### 🔴 `600-E` — a warning that applies to every row on this page

A `200` from `raw.githubusercontent.com/<repo>/<branch>/LICENSE` proves **the branch exists**, not
that it is the default. Measured on `8` platform-tier repos: 🔴 **`master` returned `200` on `6`, and
on `4 of those 6` the real default branch is `main`, `develop` or `19.0`.** 🟢 Fabricated-branch
controls returned `404` on `8 of 8`, so the channel discriminates — these are real files on real
non-default branches. 🔵 **Every grant on this page must be resolved by
`git ls-remote --symref` first** (now cross-checkable against `search/repositories`, which agreed
`16 of 16` — `600-A`). Census:
[`../evidence/branch-probe-asymmetry.2026-11-01-p600.tsv`](../evidence/branch-probe-asymmetry.2026-11-01-p600.tsv).

---

## 🆕 `p599` — `2026-11-01` — the vertical tier is fully held, and the one new platform-shaped address this pass is not open source

### 🟢 `topic:lms` walked star-ranked — `13 of 13` already held

Every address on the first page of [`github.com/topics/lms`](https://github.com/topics/lms)
(`2,615` repos) was checked against this whole base: `frappe/lms` (`3.4k★`), `learnhouse`,
`classroomio`, `courselit`, `overhangio/tutor`, `pupilfirst`, `hypatia`, `Automattic/sensei`,
`OpenOLAT`, `academico-sis/academico`, plus `sakai`, `chamilo-lms` and `ILIAS` already on this page.
🔴 **`0` new.** 🟢 **For a platform-of-record tier this is the expected and correct result** — a
system a ministry runs does not appear in a topic head for the first time in `2026`.

### 🔴 The one new platform-shaped address, and it is a block

[`2092372408-pixel/EduPilot`](https://github.com/2092372408-pixel/EduPilot) — a local-first desktop
platform that builds courses, exercises and review schedules from Chinese and English textbooks.
Served by the recency-ordered channel (`599-B`), never held here.

| field | measured `2026-11-01` |
| --- | --- |
| stars | `2` |
| default branch | 🔴 **`master`** |
| grant | 🔴 **"EduPilot Noncommercial Source License 1.0"**, `LICENSE`, **`1,951 B`**, opens *"All rights reserved"* |
| build manifest | 🔴 `"license": "SEE LICENSE IN LICENSE"` |
| verdict | **BLOCK — not open source.** Source-available, non-commercial |

🔵 **Why it belongs on this page rather than only in the log.** This tier is where a studio looks for
*something it can stand up for a client*, and "source-available, non-commercial" is the licence class
that most resembles open source to a non-specialist reader. 🔴 **At `2★` nobody has had a commercial
reason to read its grant** — which is the shape `Trend 63` generalises, and the same shape that let
[`PageLM`](https://github.com/CaviraOSS/PageLM) sit on this base's shelves as *MIT* for five passes at
`2,057★`.

### 🟢 Re-reads on two platforms this page already recommends, both confirmed, both off `main`

| platform | real default branch | grant byte-read `2026-11-01` | consequence |
| --- | --- | --- | --- |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **`19.0`** | 🔴 **LGPL-3.0** (`8,241 B`, *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3"*) | 🟡 Weak copyleft confirmed a third time. **AI as a separate Odoo module calling the API keeps its own licence; edits to its own files must be published.** Never fork |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 **`master`** | 🔴 **AGPL-3.0** (`35,136 B`) | Unchanged: integrate through `XBlock` / `codejail` (both Apache-2.0). Never fork |

🔵 **Both are off `main`, and so is [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0,
`master`) — the LTI 1.3 seam this page's integration advice depends on.** `4 of 9` repositories
branch-resolved this pass are not on `main`; see [`../repos/foundations.md`](../repos/foundations.md).
🟢 **This page's integration advice is only as good as the branch its licence was read at.**

### 🔴 The ERP/SIS gap is unchanged, and it is now the oldest open gap on this page

`586-D` — *no permissive option exists in the education ERP/SIS tier at any size* — survived a fresh
`topic:lms` walk and a dedicated `open source platform education ERP SIS MIT Apache {year}` leg. The
leg returned **`OpenEduCat` (LGPL-3.0), Kuali (licence unstated in the source), Open Admin (GPL) and
Centre (GPL)**. 🔴 **Not one permissive ERP.** 🟢 The only permissive row remains
[`academico-sis/academico`](https://github.com/academico-sis/academico) (MIT, `410★`) and it is
school management, not an ERP. 🔵 **Stable, usable conclusion: in this tier the play is an AI
side-car against an LGPL or GPL system of record — never a fork, and never a greenfield ERP.**

---


## 🆕 `p598` — `2026-11-01` — two customisable platforms promoted, and the licence screen that would have rejected the Apereo consortium

🔵 **Why the Apereo finding belongs on this page and not only in a methods note.** This page's job is
*platforms of record a studio can customise*. The Apereo consortium — **Sakai** (LMS), **uPortal**
(institutional portal), **CAS** (the single-sign-on almost every university estate runs), **OpenLRW**
(learning-record warehouse) — is the deepest pool of institution-grade, permissively licensed
education software in existence. 🔴 **A licence screen reading the GitHub API's `spdx_id` rejects
most of it**: `6 of 8` Apereo-family repositories measured this pass report `NOASSERTION`, and `3`
of those are plain **ECL-2.0** (`598-D`, census on
[`../repos/trending.md`](../repos/trending.md)). 🟢 ECL-2.0 is Apache-2.0 with a narrowed,
education-specific patent grant — permissive and shippable. 🔵 **The one Apereo row this base
already carries, Sakai, passed the screen only because its title line happens to carry the
parenthetical tag `(ECL-2.0)`.** That is the whole discriminator.

### 🟢 Promoted this pass — grants byte-read `2026-11-01` at the real default branch

| Platform | Repo | ★ | Grant (byte-read) | Branch | Last push | What you customise |
| --- | --- | --: | --- | --- | --- | --- |
| **lms-front** | [guillermoscript/lms-front](https://github.com/guillermoscript/lms-front) | **44** | 🟢 **MIT** (`1,072 B`) | 🔴 `master` | 🟢 `2026-11-01` | 🆕 **A multi-tenant, self-hostable LMS with the AI tutor already on MCP.** Next.js 16 + React 19 + Supabase with row-level security + Stripe Connect; subdomain-per-school, gamification, certificates, **i18n `en`/`es`**. 🔵 The only row on this page that ships *both* the tenancy model and an MCP tutor seam — and the `es` locale makes it the LATAM-ready starting point this page has been short of |
| **FreeITSM** | [edmozley/freeitsm](https://github.com/edmozley/freeitsm) | **119** | 🟢 **MIT** (`1,066 B`) | `main` | 🟢 `2026-10-31` | Service-desk / ITSM — ticketing, assets, change. 🔵 Adjacent, not an LMS: every university and district runs an **IT help desk**, and it is the least-contested place to put a first agent (triage, routing, knowledge-base answers) because no student data and no pedagogy are in scope. 🟡 Judge it as an ITSM tool, not an education product |

### 🟢 Standing Apereo tier — permissive, institution-grade, and invisible to an `spdx_id` screen

| Platform | Repo | ★ | Grant (byte-read `2026-11-01`) | Last push | Role in an education estate |
| --- | --- | --: | --- | --- | --- |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **1,240** | 🟢 **ECL-2.0** (`11,120 B`) | 🟢 `2026-10-30` | Full LMS of record; the API grades it correctly |
| **CAS** | [apereo/cas](https://github.com/apereo/cas) | **11,392** | 🟢 **Apache-2.0** | 🟢 `2026-11-01` | Single sign-on. 🔵 The largest repo in the consortium and the one an agent integration meets first |
| **uPortal** | [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | **287** | 🟢 **Apache-2.0** | 🟢 `2026-10-30` | Institutional portal / student dashboard shell |
| **OpenLRW** | [Apereo-LAI/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | **62** | 🟢 **ECL-2.0** (`9,878 B`) 🔴 API `NOASSERTION` | 🟡 `2025-09-12` | Learning-record warehouse (xAPI/Caliper). 🟡 Stale — reference schema, not a live dependency |

🔴 **One row measured and held back.** [`uPortal-Project/CoursesPortlet`](https://github.com/uPortal-Project/CoursesPortlet)
(`12★`) ships a **BSD-3-Clause** grant (`1,529 B`) whose copyright holder is *"News Reader Portlet
Development Team"* — a different project — and the file is byte-identical to
[`NewsReaderPortlet`](https://github.com/uPortal-Project/NewsReaderPortlet)'s. 🟡 **REVIEW, not
shippable on sight**: the terms are permissive but the named holder does not match the work.

---

## 🆕 p597 — 2026-11-01 — four customisable platforms of record recovered off the `596-C` backlog, and one of them is a `12,149★` MIT ERP this base had dropped

### 🔵 Why these arrive as promotions rather than discoveries

`596-C` established that this base's shelves are rewritten wholesale while its trending logs are
append-only, so a dropped row answers *"already held"* forever. 🟢 **Re-measured this pass under a
corrected gate:** `3,366` addresses have reached a shelf page across `15` snapshots plus today,
`767` carry a disposition now, so 🔴 **`2,640` (`78.4 %`) were dropped** — and 🔴 **`2,049` of those
are reported "held" by a log-grepping gate**. 🟢 Both figures reproduced on two instruments (`comm`
and `awk`) under forced `LC_ALL=C`, per `p596`'s locale warning. 🔵 `p596` measured `2,015` of
`2,243` (`89.8 %`); **the gate-blind count replicates almost exactly** (`2,049` vs `2,015`) and the
denominator was the only real difference.

🔴 **A withdrawn figure of this pass's own, published per `589-C`.** The first run of this census
returned `614` dropped of `1,130` (`54.3 %`) and that is **wrong**: the filter restricted archive
files to the basenames `top.md`, `foundations.md`, `solutions.md`, … which exist in 🔴 **`1` of
`15`** snapshots, because the other `14` store the same pages as `agents-top.md`,
`repos-foundations.md`, `verticals-solutions.md`. A basename filter silently became a
single-snapshot filter. 🔵 Corrected before publication; recorded because the same mistake is
available to the next pass.

### 🟢 Promoted — platforms a studio can fork, customise and attach AI to

| Platform | Repo | ★ | Grant (byte-read `2026-11-01`) | Branch | Last push | Tier it serves |
| --- | --: | --: | --- | --- | --- | --- |
| **Aureus ERP** | [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) | **12,149** | 🟢 **MIT** (`1,077 B`) | 🔴 `master` | `2026-10-30` | The institution **back office** — Laravel/Filament ERP. 🟢 The permissive answer to OpenEduCat's LGPL-3.0 and ERPNext's GPL-3.0; a studio may ship it closed |
| **Agora Flat** | [netless-io/flat](https://github.com/netless-io/flat) | **6,443** | 🟢 **MIT** (`1,062 B`) | `main` | `2026-10-30` | The **synchronous classroom** — Web, Windows and macOS clients, interactive whiteboard. 🔵 Replaces a BigBlueButton deployment where the client, not the server, is the product |
| **Kolibri Studio** | [learningequality/studio](https://github.com/learningequality/studio) | **211** | 🟢 **MIT** (`1,115 B`) | 🔴 **`unstable`** | 🟢 `2026-11-01` | **Content curation and packaging** for Kolibri's offline-first delivery. 🔴 Its default branch is `unstable` — pin a SHA, never track the branch |
| **Sunbird** | [sunbird-ed/sunbirded-portal](https://github.com/sunbird-ed/sunbirded-portal) | **41** | 🟢 **MIT** (`1,072 B`) | 🔴 `master` | 🟡 `2026-02-21` | **National-scale platform of record** (India's DPG stack, the portal tier). 🔵 APAC; 🔴 `334 MB` and `8` months since a push — a reference architecture, not a live dependency |

🟢 **Also promoted and platform-adjacent:** [`autolab/autolab`](https://github.com/autolab/autolab)
(Apache-2.0, `808★`) and [`anubislms/anubis`](https://github.com/anubislms/anubis) (MIT, `382★`) are
both **complete course-delivery systems**, shelved on
[`../repos/foundations.md`](../repos/foundations.md) this pass because an engagement builds *on* them
rather than replacing them. 🔵 Together with Aureus and Flat, this page now carries a **fully
permissive stack** — back office, synchronous classroom, course delivery, autograding, content
packaging — which it has never previously been able to state.

### 🔴 The platform rows that are not usable, measured and named

| Platform | Repo | Measured | Disposition |
| --- | --- | --- | --- |
| **Forma LMS** | [formalms/formalms](https://github.com/formalms/formalms) | 🔴 **no licence file**, `37★`, live `2026-07-17`, `112 MB` | **BLOCK** — a complete LMS with no grant at all |
| **Menthor** | [menthorlabs/menthor](https://github.com/menthorlabs/menthor) | 🟢 Apache-2.0, `582★` — 🔴 **ARCHIVED**, last push `2024-04-21` | **DEAD.** 🔵 A Brazilian (LATAM) open programming-education platform, and the largest LATAM-origin permissive row this base has found — it has been read-only for `2.5` years. Recorded so it is never proposed |

🔵 **The LATAM reading this forces.** `594-D` found LATAM's largest school platforms
(`portabilis/i-educar`, `i-diario`, `pre-matricula-digital`) to be copyleft; Menthor was the
permissive counter-example and it is **archived**. 🔴 **So the region's permissive platform tier is
genuinely empty, not merely unmeasured** — an informed gap, carried to
[`../intel/market.md`](../intel/market.md) rather than left silent.

---

## 🆕 p596 — 2026-11-01 — a SECOND permissive platform of record for this page, carried unfiled in this base's logs, and it serves a tier this page has never covered: the academic library

### 🔴 Why it arrives as a promotion rather than a discovery

`596-C`, measured this pass: **`2,015` of `2,243` ever-shelved addresses (`89.8 %`) were
dropped** across the `15` wholesale rewrites recorded under `archive/`, while the append-only
trending logs lost nothing — and because the "already held?" gate greps those logs, a dropped
row answers *"held"* forever and is never re-shelved. 🔴 **FOLIO is in that population**, and
`folio-org/platform-complete` was specifically on `repos-foundations.md` at
`archive/2026-10-06-pre-reset` before being dropped. 🟢 `folio-org/okapi` — the gateway, and
the actual AI seam — is the one component here that was **genuinely never shelved**. `folio-org` appears in `3` sections of
[`../agents/trending.md`](../agents/trending.md) and `4` of
[`../repos/trending.md`](../repos/trending.md), and in 🔴 **`0`** of this page, `agents/top.md`,
`repos/foundations.md`, `intel/market.md` or `intel/trends.md`. 🔴 So it was shelved, dropped, and then permanently invisible to search.

### 🟢 FOLIO — the Library Services Platform, and it is Apache-2.0 end to end

| Repo | ★ | Licence (byte-read on the real branch) | Branch | Last push | Role |
|---|--:|---|---|---|---|
| [folio-org/okapi](https://github.com/folio-org/okapi) | **134** | 🟢 **Apache-2.0** (`11,357 B`) | 🔴 `master` | `2026-10-29` | The API gateway and module registry — the seam every FOLIO module is mounted on, and the natural attachment point for an AI side-car |
| [folio-org/stripes](https://github.com/folio-org/stripes) | **21** | 🟢 **Apache-2.0** (`11,357 B`) | `main` | `2026-10-13` | The UI framework for front-end modules |
| [folio-org/platform-complete](https://github.com/folio-org/platform-complete) | **15** | 🟢 **Apache-2.0** (`11,357 B`) | 🔴 `master` | `2026-10-05` | The "complete" platform build — a `package.json` pinning `@folio/stripes-core` and the module set, plus module-descriptor generation. This is the **build entry point**, not the product |
| [folio-org/mod-inventory](https://github.com/folio-org/mod-inventory) | **4** | 🟢 **Apache-2.0** (`11,357 B`) | 🔴 `master` | 🟢 `2026-11-01` | Instance/holdings/item inventory — the system-of-record domain module |
| [folio-org/mod-users](https://github.com/folio-org/mod-users) | **1** | 🟢 Apache-2.0 (API) | 🔴 `master` | `2026-10-26` | Patron identity and user domain model |

### 🟢 The licence shape, measured across the whole organisation rather than sampled

| `org:folio-org` | repos |
| --- | --: |
| total | **456** |
| 🟢 `license:apache-2.0` | **398** (`87.3 %`) |
| 🔴 **any copyleft** (`gpl-3.0`, `agpl-3.0`, `lgpl-3.0`) | 🟢 **`0`** |
| `mit` | `1` |
| 🟡 no licence field (`NULL` / `NOASSERTION`) | `57` |

🟢 **This page's standing rule has a second exception, and this is it.** `p584` established
that the education platform-of-record tier is *"copyleft with exactly ONE permissive
exception"*, and `p588` added a permissive virtual classroom. 🟢 **FOLIO is a full
system-of-record platform — patrons, inventory, circulation, acquisitions, ERM — with
`0` copyleft repositories in `456`.** A studio may fork it, modify it and ship it closed.

🔴 **And the caveat that matters operationally, because it sits on the deployment path:** the
`57` unlicensed repositories are not platform code — they are auxiliary tooling: the website
(`folio-org.github.io`), CI (`folio-tools`, `pipelines-shared-library`), test suites
(`folio-api-tests`, `container-perf-tests`, archived), governance (`tech-council`) — and
🔴 **`folio-org/folio-helm`, the Helm chart set, is among them (`NULL` licence, `5★`).** 🔵 **So
the platform is permissively licensed and the most common way to deploy it is not.** A client
deployment that vendors the Helm charts is vendoring an unlicensed artefact; the fix is cheap
(write your own charts against the Apache-2.0 modules, or get a grant in writing) but it has
to be known before procurement, not after.

### 🔴 Why a star-based screen was always going to miss this

🔴 **FOLIO is a `456`-repository microservice platform, so no single repo carries the
platform's weight.** Its largest component is `okapi` at `134★`; its system-of-record
inventory module is `4★` and was pushed **today**. 🔵 **Any screen that ranks platforms of
record by stars on a single address will rate FOLIO below a `2,000★` single-repo demo**, which
is how a live, Apache-2.0, institution-grade platform stayed in this base's logs for passes
without reaching a shelf. 🟢 **Standing instruction: for the platform tier, screen on
organisation-level liveness and licence uniformity, not on one repository's stars.**

### 🔵 What it is for — the tier this page has never carried

Every platform on this page so far serves teaching (LMS), administration (SIS/ERP) or
delivery (virtual classroom). 🟢 **FOLIO serves the academic library**, which in a university
engagement is a separate budget, a separate buyer and a separate system of record — and one
with an unusually clean AI attachment surface, because discovery, metadata enrichment and
collection analytics are exactly the problems an agent is good at and are already exposed as
Okapi modules. 🔵 Strongest in **North America** and **EMEA**, where FOLIO's institutional
adoption sits; LATAM and APAC deployments exist but this pass did not measure them and does
not claim them.

---
## 🆕 p595 — 2026-11-01 — the platform tier was not re-measured this pass; the grading axis was, and it yielded one unlicensed address rather than a platform

### The one new address, and why it is not promotable

🆕 [`dajarbot/AutoGrader`](https://github.com/dajarbot/AutoGrader) — the only address the
nine legs served that this base has **never** held (`0` files). Local-first grading
workspace: student writing scored against versioned rubrics by a local Ollama model, no API
key, human approval before export.

🔴 **It is 🔴 BLOCK, not 🟢.** Measured first-hand this pass: `0`★, `0` forks, `0`
watchers, `8` commits, no description — and
**`10` grant probes (`LICENSE` / `.md` / `.txt` / `COPYING` / `LICENCE` × `main`+`master`) all
answer `404`**, against a `200` control on `main/README.md` that proves the branch exists and
the absences are real rather than a wrong-branch artefact. **No grant of any kind.** It cannot
be forked into client work, and it is filed here so a twenty-seventh pass does not spend a leg
rediscovering it.

🔵 The five other autograder addresses the topic axis served were all already held:
`webtech-network/autograder` (`14` files), `johnswyou/autograder` (`11`),
`scaleapi/researchrubrics` (`8`), `alphadl/AdaRubrics` (`6`), `alphadl` (`5`).

---
## 🆕 p594 — 2026-11-01 — the licence-probe defect `p593` inferred from one row is a property of THIS page's tier: `30 of 253` curated addresses default to neither `main` nor `master`, and they are the platforms of record almost without exception

🔵 **Why this census belongs on the verticals page and not on an agent page.** `p593` found one
address — `openeducat/openeducat_erp`, default branch `19.0` — whose licence a hardcoded
`main`/`master` probe cannot read, and registered `593-B1` on the reasoning that others probably
existed. This pass measured the whole curated base (`253` addresses resolved through the
`search/repositories` channel, which returns `default_branch`). 🔴 **`30` of `253` (`11.9 %`) default
to one of `18` names that are neither `main` nor `master` — and the list reads like a roll-call of
this page's own shelf.**

🔵 **The reason is not mysterious, and it is the point.** Mature platforms branch by release:
Odoo ships from `20.0`, OpenEduCat from `19.0`, Claroline from `15.0`, ILIAS from `release_11`,
Gibbon from `v31.0.00`, BigBlueButton from `v4.0.x-develop`, Corteza from `2026.9.x`, i-educar from
`2.12`, Tutor from `release`, OFBiz from `trunk`. Young single-maintainer agent repos ship from
`main`. 🔴 **So a probe that assumes `main` is systematically blind to exactly the tier a client
engagement is built on, and silently reports "no licence file" for it.** That is a selection
effect, not bad luck.

### 🔴 The census — all `30`, re-read on the correct branch this pass

Licence from the `p594` three-stage classifier (TITLE → declaration → body, abbreviations matched
only as whole tokens). 🟢 permissive · 🟡 weak/file copyleft · 🔴 strong copyleft or not-OSI ·
🔵 escalated to review. The last column is what a `main`-only probe would have received.

| Repo | default branch | ★ | Licence (read on the real branch) | Grant file | `main/LICENSE` says |
| --- | --- | --: | --- | --- | --- |
| [odoo/odoo](https://github.com/odoo/odoo) | **`20.0`** | 55463 | 🟡 `LGPL-3.0` | `LICENSE` | 🔴 `404` |
| [frappe/erpnext](https://github.com/frappe/erpnext) | **`develop`** | 40822 | 🔴 `GPL` | `license.txt` | 🔴 `404` |
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | **`2.2`** | 24088 | 🟢 `MIT` | `LICENSE` | 🔴 `404` |
| [dream-num/univer](https://github.com/dream-num/univer) | **`dev`** | 22840 | 🟢 `Apache-2.0` | `LICENSE` | 🟡 `200` (exists but not default) |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | **`v4.0.x-develop`** | 9262 | 🟡 `LGPL-3.0` | `LICENSE` | 🟡 `200` (exists but not default) |
| [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | **`develop`** | 7814 | 🔴 `GPL` | `COPYING` | 🔴 `404` |
| [oppia/oppia](https://github.com/oppia/oppia) | **`develop`** | 6954 | 🟢 `Apache-2.0` | `LICENSE` | 🔴 `404` |
| [frappe/lms](https://github.com/frappe/lms) | **`develop`** | 3361 | 🔴 `AGPL-3.0` | `license.txt` | 🔴 `404` |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | **`dev`** | 2440 | 🔴 `AGPL-3.0` | `LICENSE` | 🟡 `200` (exists but not default) |
| [cortezaproject/corteza](https://github.com/cortezaproject/corteza) | **`2026.9.x`** | 2184 | 🟢 `Apache-2.0` | `LICENSE` | 🟡 `200` (exists but not default) |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **`develop`** | 1163 | 🟢 `MIT` | `LICENSE` | 🔴 `404` |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | **`trunk`** | 1148 | 🟢 `Apache-2.0` | `LICENSE` | 🔴 `404` |
| [overhangio/tutor](https://github.com/overhangio/tutor) | **`release`** | 1131 | 🔴 `AGPL-3.0` | `LICENSE.txt` | 🔴 `404` |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | **`19.0`** | 903 | 🟡 `LGPL-3.0` | `LICENSE` | 🔴 `404` |
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **`develop`** | 824 | 🟢 `MIT` | `LICENSE` | 🟡 `200` (exists but not default) |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | **`2.12`** | 723 | 🔴 `GPL` | `LICENSE` | 🔴 `404` |
| [frappe/education](https://github.com/frappe/education) | **`develop`** | 688 | 🔴 `GPL` | `license.txt` | 🔴 `404` |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | **`mobile`** | 649 | 🔴 `GPL` | `LICENSE` | 🔴 `404` |
| [GibbonEdu/core](https://github.com/GibbonEdu/core) | **`v31.0.00`** | 637 | 🔴 `GPL` | `LICENSE` | 🟡 `200` (exists but not default) |
| [opencast/opencast](https://github.com/opencast/opencast) | **`develop`** | 509 | 🟢 `ECL-2.0` | `LICENSE` | 🔴 `404` |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | **`release_11`** | 507 | 🔴 `GPL` | `LICENSE` | 🔴 `404` |
| [claroline/Claroline](https://github.com/claroline/Claroline) | **`15.0`** | 349 | 🔵 `-` | `LICENSE` | 🔴 `404` |
| [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | **`dev`** | 153 | 🟢 `BSD-3-Clause` | `LICENSE` | 🟡 `200` (exists but not default) |
| [portabilis/i-diario](https://github.com/portabilis/i-diario) | **`1.6`** | 117 | 🔴 `AGPL-3.0` | `LICENSE` | 🟡 `200` (exists but not default) |
| [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | **`develop`** | 64 | 🔴 `GPL` | `LICENSE` | 🔴 `404` |
| [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) | **`develop`** | 61 | 🟢 `Apache-2.0` | `LICENSE` | 🔴 `404` |
| [thm-mni-ii/feedbacksystem](https://github.com/thm-mni-ii/feedbacksystem) | **`dev`** | 24 | 🟢 `Apache-2.0` | `LICENSE` | 🟡 `200` (exists but not default) |
| [portabilis/pre-matricula-digital](https://github.com/portabilis/pre-matricula-digital) | **`2.12`** | 21 | 🔴 `AGPL-3.0` | `LICENSE` | 🟡 `200` (exists but not default) |
| [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | **`development`** | 21 | 🟢 `Apache-2.0` | `LICENSE` | 🟡 `200` (exists but not default) |
| [oat-sa/extension-tao-itemqti](https://github.com/oat-sa/extension-tao-itemqti) | **`develop`** | 7 | 🔴 `GPL` | `LICENSE` | 🔴 `404` |

🔴 **`19 of 30` return a hard `404` on `main/LICENSE`** — a probe reports no grant and the row is
blocked. 🟡 **The other `11` are worse, not better: `main` exists but is not the default branch**,
so the probe gets a `200` and reads a grant from a branch the project does not ship — a *stale*
answer that looks like a successful read. 🔵 **The second failure mode is undetectable without
`default_branch`, which is precisely why `593-B1` called this failure silent.**

### 🟢 What the corrected read changes for delivery

| Finding | Consequence for an engagement |
| --- | --- |
| 🟡 **`odoo/odoo` is `LGPL-3.0`**, declared on line 2 of `LICENSE` under a prose prepend | 🟢 **The single most important licence fact on this page is readable only off `20.0`.** Weak copyleft: a new Odoo module may link without being forced open — the basis of every Odoo-family recipe here |
| 🟡 **`openeducat/openeducat_erp` is `LGPL-3.0`** (`19.0`), same prose prepend | 🟢 Confirms `p593` by an independent route — an AI side-car on the education ERP is lawful without a fork |
| 🟢 **`thm-mni-ii/feedbacksystem` is `Apache-2.0`** (`dev`), declared under a prepended copyright line | 🟢 **A permissive row recovered from a blank API field** — German automated-feedback/grading system, EMEA |
| 🔴 **`frappe/erpnext`, `frappe/lms`, `frappe/education`** keep grants at lowercase `license.txt` on `develop` | 🔴 Invisible to a `6`- or `7`-path probe. `GPL-3.0` / `AGPL-3.0` / `GPL-3.0` — attach, do not fork |
| 🔴 **`portabilis/i-educar`, `i-diario`, `pre-matricula-digital`** (Brazil) on `2.12` / `1.6` | 🔴 `GPL-2.0` and **`AGPL-3.0` written in Portuguese** — see `594-D`; an English-only matcher false-blocks all three |
| 🔵 **`claroline/Claroline`** (`15.0`) — title *"Claroline Connect License"*, body verbatim `AGPL-3.0` | 🔵 Escalate, do not auto-pass: a bespoke title over a standard body may add terms the body does not contain |

🔵 **`frappe/education`'s grant is `19` bytes** — `License: GNU GPL V3`, a declaration with no
licence text. 🔴 **A successful fetch is not a read, and byte count is not evidence**: three of this
page's rows would pass a "grant file exists" gate while supplying no terms to inspect.

### 🟢 The probe this page should be read with, stored as a runnable block

🔴 Per `p590`, a committed script is inert here (`make`, `bash ingest/*.sh` and `python3
ingest/*.py` are all **DENIED**). 🟢 This form runs inline and is what produced the table above:

```bash
# 1. ALWAYS take the branch from the API first — never assume main/master (593-B1)
gh api -X GET search/repositories -f q="repo:$REPO" \
  --jq '.items[]|[.full_name,.default_branch,(.license.spdx_id//"null")]|@tsv'
# 2. probe 13 path/case variants on THAT branch (594-C: lowercase license.txt is real)
for p in LICENSE LICENSE.md LICENSE.txt license.txt license license.md LICENCE LICENCE.txt \
         COPYING COPYING.txt LICENSE.rst LICENSE-APACHE LICENSE-MIT; do
  curl -sf "https://raw.githubusercontent.com/$REPO/$BRANCH/$p" && break
done
# 3. classify on the TITLE (591-A); if the title is prose or a copyright line, use the
#    "published/licensed under X" declaration (593-B); only then fall back to the body.
# 4. match FULL licence names; abbreviations ONLY as whole tokens \bMIT\b, \bMPL\b (594-E).
```

🔴 **Step 4 is not pedantry.** Measured this pass: an unanchored `MPL` substring matches **`65` of
`65`** real grants read, because every licence disclaims warranties "EXPRESS OR I**MPL**IED" and
most say "co**mpl**iance" and "exa**mpl**e"; an unanchored `MIT` matches "li**mit**ation",
"per**mit**ted" and "sub**mit**ted". 🟢 With the anchors in place the classifier returns `0` false
permissives across `10` known-hard rows, **including refusing to pass `CaviraOSS/PageLM`**, which
this base published as 🟢 MIT until this pass (`594-A`).

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
| **LMS of record** | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 **AGPL-3.0** | **8,213** | `2026-11-01` | 🔴 **No** | 🟢 **But the extension points are permissive**: [`XBlock`](https://github.com/openedx/XBlock) (Apache-2.0) and [`codejail`](https://github.com/openedx/codejail) (Apache-2.0) let proprietary AI plug in **without inheriting network copyleft**. Stand it up with [`overhangio/tutor`](https://github.com/overhangio/tutor). 🔴 Cite *this* address — `openedx/openedx-platform` is the pre-rename name and returns `422`. |
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
| `openedx/openedx-platform` | **`422`** — moved | `openedx/openedx-platform` (**AGPL-3.0**, `8,213★`) |


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
