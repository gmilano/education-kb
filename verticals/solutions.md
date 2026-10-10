---
industry: education
region: Global
updated: 2026-10-10
---

# Education — vertical platforms you can customise with AI

**Pass 109, 2026-10-10.** ⏱️ **Nineteenth pass of this date.** 🔴 **This page carries the
most commercially consequential correction of the pass: two of the nine components p108
published as "the permissive tier Globant can build on and ship" have been abandoned for
years.**

### 🔴 🆕 p109 — the permissive tier is SEVEN components, not nine

🔵 **p108 filtered the platform table to OSI-permissive licences and published nine rows,
eight of them version-pinnable, as the build-on-freely tier. Liveness removes two of
them:**

| platform | licence | pin | last commit | age | band |
|---|---|---|---|---|---|
| [`Oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | `v3.5.3` | 2026-10-10 | **0 d** | 🟢 fresh |
| [`DSpace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | `dspace-10.1` | 2026-10-10 | **0 d** | 🟢 fresh |
| [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 | `OpenOLAT_21.0.3` | 2026-10-09 | **1 d** | 🟢 fresh |
| [`Sakai`](https://github.com/sakaiproject/sakai) | 🟢 ECL-2.0 | `25.2` | 2026-10-09 | **1 d** | 🟢 fresh |
| [`Kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | `v0.19.5` | 2026-10-09 | **1 d** | 🟢 fresh |
| [`Apache OFBiz`](https://github.com/apache/ofbiz-framework) | 🟢 Apache-2.0 | 🔴 SHA only | 2026-10-09 | **1 d** | 🟢 fresh |
| [`h5p-standalone`](https://github.com/tunapanda/h5p-standalone) | 🟢 MIT | `v3.8.2` | 2026-03-24 | 🟡 **200 d** | 🟡 slowing |
| 🔴 ~~[`Apereo SSP`](https://github.com/Jasig/SSP)~~ | 🟢 Apache-2.0 | `ssp-2.9.0` | **2021-07-26** | 🔴 **1 902 d** | 🔴 **abandoned** |
| 🔴 ~~[`Kuali Rice`](https://github.com/kuali/rice)~~ | 🟢 ECL-2.0 | `rice-2.6.0` | **2017-05-17** | 🔴 **3 433 d** | 🔴 **abandoned** |

🔴 **`Kuali Rice` — nine years five months. `Apereo SSP` — five years two months.**
🟢 **Both are genuinely permissive and both genuinely have a version to pin, which is
exactly why p107 and p108 could not catch them: every axis this KB had before today scored
them clean.** 🔴 **Recommending ECL-2.0 `rice-2.6.0` as "HiEd admin middleware" to a
client in 2026 means recommending a 2017 codebase with no upstream.**

🔵 **The fork does not rescue it either: `kualico/rice`, the successor organisation's copy,
is itself **2 292 d** abandoned (2020-07-01), and its default branch is `java11` — a
migration branch that was the last thing anyone worked on.**

🟢 **Corrected tier, in the order an engagement should consider it:**

```
OpenOLAT        Apache-2.0   OpenOLAT_21.0.3    1 d   full LMS        <- the headline, and it is alive
Sakai           ECL-2.0      25.2               1 d   full LMS
Oppia           Apache-2.0   v3.5.3             0 d   lesson engine
Kolibri         MIT          v0.19.5            1 d   offline LMS
DSpace          BSD-3        dspace-10.1        0 d   repository
Apache OFBiz    Apache-2.0   — (stamp)          1 d   ERP spine
h5p-standalone  MIT          v3.8.2           200 d   content playback  <- slowing; GPL core is fresher
---------------------------------------------------------------------------------------
Apereo SSP      Apache-2.0   ssp-2.9.0      1 902 d   RETIRE from the tier
Kuali Rice      ECL-2.0      rice-2.6.0     3 433 d   RETIRE from the tier
```

🟢 **Six of the seven survivors are fresh, and the strongest of them is also the most
permissive — `OpenOLAT`, Apache-2.0, 542 tags, a commit yesterday.** 🔵 **That is the
cleanest statement this page has ever been able to make: p108 had to choose between the
licence axis and the incumbency axis; on liveness the permissive tier does not lose.**

### 🟢 🆕 p109 — the copyleft incumbents, measured on the same axis

| platform | licence | pin | last commit | age | band |
|---|---|---|---|---|---|
| [`Chamilo`](https://github.com/chamilo/chamilo-lms) | 🟡 GPL-3 | `v3.0.1` | 2026-10-09 | **0 d** | 🟢 fresh |
| [`Open edX`](https://github.com/openedx/edx-platform) | 🟡 AGPL-3 | `v2.1.0` | 2026-10-09 | **1 d** | 🟢 fresh |
| [`BigBlueButton`](https://github.com/bigbluebutton/bigbluebutton) | 🟡 LGPL-3 | `v3.0.39` | 2026-10-08 | **2 d** | 🟢 fresh |
| [`Moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | `v5.3.0` | 2026-10-03 | **7 d** | 🟢 fresh |
| [`H5P` core](https://github.com/h5p/h5p-php-library) | 🔴 GPL-3.0 | `1.28.0` | 2026-08-11 | **60 d** | 🟢 active |
| [`OpenEduCat`](https://github.com/OpenEduCat/openeducat_erp) | 🟡 LGPL-3 | 🔴 SHA only | 2026-09-07 | **33 d** | 🟢 active |
| [`Canvas LMS`](https://github.com/instructure/canvas-lms) | 🟡 AGPL-3 | `v5.14.2` | 2026-04-30 | 🟡 **163 d** | 🟡 slowing |
| [`ATutor`](https://github.com/atutor/ATutor) | 🟡 GPL-3 | `Atutor_1.4.1` | **2023-02-12** | 🔴 **1 336 d** | 🔴 **abandoned** |

🔴 **`ATutor` — the accessibility-first LMS this page has carried for many passes — is
3 years 8 months dead, and accessibility is exactly the requirement a client cannot
compromise on.** 🟡 **If accessibility drives the selection, the live options are
`OpenOLAT` and `Moodle`, not `ATutor`.**
🟡 **`Canvas LMS` at 163 days is the surprise among the incumbents. Its default branch was
re-confirmed as `master` against a live `ls-remote --symref` this pass, so the figure is
not a branch artefact — but Instructure develops commercially and a quiet public mirror is
a plausible reading. Stated as measured, not interpreted.**

### 🟢 🆕 p109 — the SIS / ERP layer, which is the healthiest segment on this page

| platform | licence | last commit | age | band | note |
|---|---|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🟡 GPL-2 | 2026-10-09 | **1 d** | 🟢 fresh | 🔴 default branch is `mobile`, not `master` |
| [`portabilis/i-diario`](https://github.com/portabilis/i-diario) | — | 2026-10-09 | **1 d** | 🟢 fresh | Brazilian municipal SIS |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | — | 2026-10-07 | **3 d** | 🟢 fresh | |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | — | 2026-10-02 | **8 d** | 🟢 fresh | Brazilian municipal SIS |
| [`frappe/education`](https://github.com/frappe/education) | — | 2026-09-30 | **10 d** | 🟢 fresh | ERPNext school module |
| [`OpenEduCat`](https://github.com/OpenEduCat/openeducat_erp) | 🟡 LGPL-3 | 2026-09-07 | **33 d** | 🟢 active | 🔴 default branch is `19.0` |

🟢 **Every SIS/ERP row on this page is fresh or active — the only segment with no
casualties.** 🔵 **Three of the six are LATAM-published, which is placed and costed in
`intel/market.md`.**

---

# Education — vertical platforms you can customise with AI

**Pass 108, 2026-10-10.** ⏱️ **Eighteenth pass of this date.** 🟢 **Every platform row
gains the ref you would actually pin, and one platform moves from "unreleased" to
"pin 21.0.3" — the correction with the largest commercial consequence on this page.**

### 🟢 🆕 p108 — the customisable-platform tier, by what you can pin

🔵 **Source: `compose/code/p108-release-identity/`, anonymous git lane only, 296 of 296
addresses read, zero unread. Column chosen by `class` (`latest_prefix` is noise on a
`semver` row).**

| platform | licence | `class` | pin | AI-on-top surface |
|---|---|---|---|---|
| [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | `prefixed` | 🟢 **`OpenOLAT_21.0.3`** | 🟢 **most permissive full LMS here**; course elements + REST API |
| [`Moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | `semver` | 🟢 **`v5.3.0`** | plugin API; in-LMS AI subsystem |
| [`Open edX`](https://github.com/openedx/edx-platform) | 🟡 AGPL-3 | `semver` | 🟢 **`v2.1.0`** | XBlocks; 🔴 `release-2021-…` tags are not releases |
| [`Canvas LMS`](https://github.com/instructure/canvas-lms) | 🟡 AGPL-3 | `semver` | 🟢 **`v5.14.2`** | LTI 1.3 + Live Events |
| [`Chamilo`](https://github.com/chamilo/chamilo-lms) | 🟡 GPL-3 | `semver` | 🟢 **`v3.0.1`** | LATAM/francophone base; plugin layer |
| [`Sakai`](https://github.com/sakaiproject/sakai) | 🟢 ECL-2.0 | `semver` | 🟢 **`25.2`** | 🟢 permissive; tool/entity API |
| [`Kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | `semver` | 🟢 **`v0.19.5`** | 🟢 **MIT + offline-first** — low-connectivity deployments |
| [`Oppia`](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | `semver` | 🟢 **`v3.5.3`** | interactive-lesson state graph |
| [`BigBlueButton`](https://github.com/bigbluebutton/bigbluebutton) | 🟡 LGPL-3 | `semver` | 🟢 **`v3.0.39`** | synchronous classroom; recording hooks |
| [`H5P`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** | `semver` | 🟢 **`1.28.0`** | 🔴 **copyleft core**; content types embed in every LMS above |
| [`h5p-standalone`](https://github.com/tunapanda/h5p-standalone) | 🟢 **MIT** | `semver` | 🟢 **`v3.8.2`** | 🟢 **the MIT way to play H5P** — no LMS, no GPL server library |
| [`DSpace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | `prefixed` | 🟢 **`dspace-10.1`** | institutional repository; REST + OAI-PMH |
| [`OpenEduCat`](https://github.com/OpenEduCat/openeducat_erp) | 🟡 LGPL-3 | 🔴 **`stamp`** | 🔴 **SHA only** | **LMS+SIS+fees on one DB** (Odoo-based) |
| [`Kuali Rice`](https://github.com/kuali/rice) | 🟢 ECL-2.0 | `prefixed` | 🟢 **`rice-2.6.0`** | HiEd admin middleware; workflow engine |
| [`ATutor`](https://github.com/atutor/ATutor) | 🟡 GPL-3 | `prefixed` | 🟢 **`Atutor_1.4.1`** | accessibility-first LMS |
| [`Apereo SSP`](https://github.com/Jasig/SSP) | 🟢 **Apache-2.0** | `prefixed` | 🟢 **`ssp-2.9.0`** | student-success/advising case management |
| [`Apache OFBiz`](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** | 🔴 **`stamp`** | 🔴 **SHA only** | the ERP spine when OpenEduCat is too narrow |

### 🟢 The permissive tier — what Globant can build on and ship

🔵 **Filtered to OSI-permissive only (Apache-2.0 / MIT / BSD / ECL-2.0), which is the
licence class the brief prioritises:**

```
OpenOLAT        Apache-2.0   OpenOLAT_21.0.3   full LMS         <- the headline
Sakai           ECL-2.0      25.2              full LMS
Oppia           Apache-2.0   v3.5.3            lesson engine
Kolibri         MIT          v0.19.5           offline LMS
h5p-standalone  MIT          v3.8.2            content PLAYBACK (H5P core itself is GPL-3)
DSpace          BSD-3        dspace-10.1       repository
Kuali Rice      ECL-2.0      rice-2.6.0        admin middleware
Apereo SSP      Apache-2.0   ssp-2.9.0         advising
Apache OFBiz    Apache-2.0   — (stamp)         ERP spine
```

🟢 **Nine permissive components, eight of them version-pinnable** (OFBiz is `stamp`).
🔴 **Licences re-read from each repo's `LICENSE` over `raw.githubusercontent.com` this pass
rather than carried forward, and two rows on this page were wrong:** 🔴 **`h5p-php-library`
is **GPL-3.0**, not MIT; `Jasig/SSP` is **Apache-2.0**, not ECL-2.0.**
🟢 **The GPL finding is why `tunapanda/h5p-standalone` (MIT, `v3.8.2`) takes H5P's place in
this tier — it plays H5P content with no LMS and no GPL server-side library.** 🔴 **Everything strong on
the *incumbency* axis (Moodle, Canvas, Open edX) is GPL or AGPL; everything strong on the
*licence* axis is less widely installed.** 🔵 **That tension is the real platform decision
in an education engagement and it has not moved in 108 passes.**

### 🔴 🆕 p108 — the correction, stated plainly

🔵 **OpenOLAT has been on this page for many passes with no release recorded, because its
tags are spelled `OpenOLAT_21.0.3` and every reading this KB made looked for `v21.0.3`
(`P108-D`).** 🔴 **The effect was to rank the single most permissive full LMS available —
Apache-2.0, 542 tags, actively released — below GPL incumbents on a maintenance axis it
actually wins.** 🟢 **Corrected here.** 🔵 **`dspace` carried the same fault with an extra
twist: ranked lexically its newest release reads `dspace-7.6`, three majors stale
(`P108-C`).**

---


# Education — vertical platforms you can customise with AI

**Pass 107, 2026-10-10.** ⏱️ **Seventeenth pass of this date.** 🟢 **Every platform row below gains a
RELEASE LADDER this pass — the first maintenance figure this page has ever carried that is not `—`.**
🔴 **`api.github.com` repo endpoints remain 403 and that is now known to be permanent (`P107-A`), so
the ladder replaces ★ rather than standing in for it.**

### 🟢 🆕 p107 — the customisable-platform tier, ranked by what you can actually pin

🔵 **Source: `compose/code/p107-git-lane-census/`, `git ls-remote` only, 299 of 299 addresses read.**
🔴 **Tag counts are `^{}`-filtered; unfiltered they overstate by up to 2× (`P107-C`).**

| platform | licence | unique tags | pinnable | tier |
|---|---|---|---|---|
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🟡 AGPL-3 | 🟢 **34 029** | 🟢 yes | 🟢 **industrial** — the largest ladder on this shelf by 6× |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟡 AGPL-3 | 🟢 **5 896** | 🟢 yes | 🟢 **industrial** |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🟡 GPL-2 | 🟢 **1 179** | 🟢 yes | 🟢 **industrial** — assessment (QTI) |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | 🟢 **591** | 🟢 `v5.3.0-rc2` | 🟢 **industrial** |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | 🔴 **composite + EE bar** | 🟢 **551** | 🟡 yes | 🔴 **industrial, but see `P107-F` below — NOT shippable as a whole** |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🔴 **ECL-2.0** | 🟢 **298** | 🟢 `20.4` | 🟡 **mature, ECL tier (p105/p106)** |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🟡 GPL-3-or-later (`P984`) | 🟢 **133** | 🟢 yes | 🟡 **mature** — 🔵 **LATAM-anchored: `BeezNest Latino SAC, Peru` is the FIRST of 12 copyright holders (`P800`)** |
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** | 🟢 **101** | 🟢 `v4.9.152` | 🟢 **the best-engineered PERMISSIVE platform here** |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 **ECL-2.0** | 🟢 **73** | 🟢 `25.2` | 🟡 **mature, ECL tier** |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 MIT | 🔴 **0** | 🔴 **no** | 🔴 **UNRELEASED** |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | 🟢 MIT | 🟡 **57** (43 scoped) | 🔴 **stale** | 🔴 **ABANDONED LADDER — newest platform tag `v2024.2.1efffc4`** |

### 🔴 🆕 p107 — the finding this table forces: **permissive and industrial barely overlap**

🟢 **Of the five industrial-tier platforms (100+ releases), four are AGPL/GPL and one is ECL. The only
permissive platform with a real ladder is `UniTime/unitime` — and it is timetabling, not an LMS or
an SIS.**

🔴 **And the KB's most-repeated recommendation fails on this axis.** `academico-sis/academico` has
been described here across many passes as *"the closest thing to a permissive SIS"*. 🟢 **It is
genuinely MIT, declared in both `composer.json` and the payload. It has **0 tags** — confirmed this
pass from the git lane, independently of pass 96's npm-manifest route.** 🔵 **A fork inherits release
engineering, a version scheme and an upgrade path that do not exist.**

🟡 **So the honest shape of the customisation decision is a two-way trade, not a shelf pick:**
- 🟢 **pin an industrial platform and accept copyleft** (Moodle / Open edX / Canvas / TAO), putting the
  AI outside the licence boundary via API or MCP — which is exactly `P1033`/`T30`'s frontier and
  `P106-A`'s architecture; **or**
- 🟡 **take a permissive base and fund release engineering as a line item** (`academico`, or `UniTime`
  if the domain fits).

🔴 **There is no third option on this shelf, and no amount of further searching has produced one in
eleven passes.** 🟢 **Stated as a standing constraint rather than re-tested each pass.**

### 🔴 🆕 p107 — `P107-F` / `Gap 370` proved a SECOND way, and this one **bars production use**

🔵 **`Gap 370`/`P969` has said since pass 93 that this shelf cannot see a per-directory licence, and
it rested on `bncc-dev/bncc-dados` — MIT at the root, CC BY 4.0 one directory down.** 🟡 **That case
is a attribution obligation. This pass found the same mechanism carrying a COMMERCIAL BAR.**

🟢 **`PrairieLearn/PrairieLearn` — 551 releases, an industrial-tier assessment platform on this very
page — serves a root `LICENSE` of **36 983 B** (`sha256 f3fba75145cfb48a`) that is not one grant but
a composite**, and it names a directory:

> *"All content that resides under the `apps/prairielearn/src/ee/` directory of this repository, if
> that directory exists, is part of the PrairieLearn **Enterprise Edition (EE)** and is licensed as
> described in `apps/prairielearn/src/ee/LICENSE`."*

🔴 **That file resolves — 2 538 B, `sha256 cfd0235081fac7b6` — and it is a subscription licence:**

> *"This software … **may only be used in production, if** you … have agreed to, and are in
> compliance with, the terms of a contract, subscription, or other agreement … and otherwise have a
> valid PrairieLearn Enterprise Edition subscription."*
> *"… it is **forbidden to copy, merge, publish, distribute, sublicense, and/or sell** the Software."*

🟢 **The directory is not hypothetical: `apps/prairielearn/src/ee/lib/billing/plans.ts` resolves at
**8 666 B**.** 🔴 **And the root `LICENSE` is the ONLY licence file at the repository root — `LICENSE.md`,
`COPYING`, `LICENCE` and `NOTICE` are all 404.**

🔴 **So a first-match 24-name ladder reads the root file, classifies the repository from it, and
NEVER REACHES the bar.** 🟡 **The rest of the repository is genuinely open (AGPL-3 for client-side
JavaScript, MIT for the University of Illinois and outside-contributor portions), which is what makes
this expensive: the repository is honestly open-source AND contains a directory a studio has no
production right to.**

🟢 **The operational rule, and it is cheap:** 🔵 **before a clone of any platform enters a client
deliverable, grep the root licence payload for a directory path and follow it.** 🔴 **`P984` already
says the SMALL licence file has the facts; `P107-F` adds that a LARGE one can carry a pointer, and a
ladder that stops at the first match reads neither.**

**Pass 106, 2026-10-10.** ⏱️ **Sixteenth pass of this date** (104: 13:4x–14:xx UTC; 105:
14:4x–15:xx; this one 15:4x–16:xx). 🟢 **`P1005` applied throughout: every row below is a payload
read this pass.** 🔴 **`api.github.com` = `http=403`; no ★ moved.**

### 🔴 🆕 p106 — the Moodle plugin frontier, on a denominator of **143 rows instead of 7**

🔵 **`T30`/`P1033` has said since pass 104 that "the copyleft frontier is the plugin tree": code that
loads INSIDE the LMS inherits its licence, code that talks to it over an API does not. It rested on
seven rows, because `moodle.org` is `http=000` from this environment (`Gap 399`).**

🟢 **A channel that reaches the plugin layer was found this pass: `packagist.org` = 200**, where
Moodle plugins publish as composer packages.

```
types_probed=46  types_nonempty=21  types_zero=25  packages=159
```

🔴 ****all 143** packages that declare a licence at all declare the GPL-3 family. NOT ONE is
permissive.** 🟢 **`P1033` holds without exception on a real denominator** — and the declaration is
free text in **three spellings of one grant** (`GPL-3.0-or-later` 136, `GPL-3.0+` 5, `GPLv3` 2),
🔵 **which is `P1046`: a census keyed on an exact string would split the dominant family into three
buckets and report none of them as dominant.**

| plugin type | packages | | plugin type | packages |
|---|---|---|---|---|
| `moodle-local` | 33 | | `moodle-format` | 4 |
| `moodle-tool` | 27 | | `moodle-auth` | 4 |
| `moodle-block` | 24 | | `moodle-atto` | 4 |
| `moodle-mod` | 22 | | `moodle-report` | 3 |
| `moodle-qtype` | 9 | | `moodle-dataformat` | 3 |
| `moodle-availability` | 8 | | 11 further types | 1–2 each |
| `moodle-filter` | 7 | | 🔴 **`moodle-aiprovider`** | 🔴 **0** |
| | | | 🔴 **`moodle-aiplacement`** | 🔴 **0** |

🔴 **The sharpest row is a zero.** 🔵 **`moodle-aiprovider` and `moodle-aiplacement` are the two
plugin types Moodle's OWN AI subsystem defines, and they have no packagist presence whatever —
against 159 packages across 21 older types.** 🟢 **`T34`: the AI seam of the most-installed LMS on
earth does not publish through the PHP package channel at all.**

#### 🟡 What to do with this in front of a client

🟢 **Two things, and they are the same two the layer split implies:**

1. 🟢 **An AI capability delivered as a `moodle-aiprovider` or `moodle-aiplacement` plugin is
   GREENFIELD** — there is nothing to fork and nothing to be out-competed by. 🔴 **And it will be
   GPL-3, because it loads inside the LMS** (`P1033`, now 143 of 143 that declare one).
2. 🟢 **An AI capability delivered BESIDE Moodle — an MCP server, a service against its web-service
   API — keeps whatever licence Globant chooses.** 🔵 **Measured precedent, both ways:
   `a2br/moodle-mcp` is MIT with no root `version.php`; `jeanlucio/moodle-local_aihub` has one and
   is GPL-3.** 🟡 **The deliverable's licence is decided by WHERE the code is mounted, not by
   negotiation.**

🟡 **`Gap 399` is re-scoped, not closed:** 159 packages is plainly a thin slice of the directory, so
the licence composition is now answered on a real denominator while the POPULATION question is not.

### 🟢 🆕 p106 — a NATIONAL vertical stack, publicly licensed: Finland (`T33`)

🔵 **Eight repositories from `opetushallitus`, the Finnish National Agency for Education, every one
EUPL-licensed and every one `UNRECOGNISED` to this KB until this pass.** 🟢 **This is a vertical
platform family in the sense this page means: something already running in production that an
agentic layer can be built on.**

| platform | EUPL | the vertical it IS |
|---|---|---|
| [`koski`](https://github.com/opetushallitus/koski) | 1.1 | 🔵 **national study-rights + completed-studies registry** — the SIS tier, at national scale |
| [`eperusteet`](https://github.com/opetushallitus/eperusteet) | 1.1 | 🔵 **national core-curriculum service** — the curriculum-vocabulary tier |
| [`ataru`](https://github.com/opetushallitus/ataru) | 1.2 | admissions and application |
| [`ehoks`](https://github.com/opetushallitus/ehoks) | 1.1 | personal competence-development plans |
| [`oppijanumerorekisteri`](https://github.com/opetushallitus/oppijanumerorekisteri) | 1.1 | learner identity |
| [`organisaatio`](https://github.com/opetushallitus/organisaatio) | 1.1 | provider registry |
| [`suorituspalvelu`](https://github.com/opetushallitus/suorituspalvelu) | 1.2 | attainment service |
| [`valtionavustus`](https://github.com/opetushallitus/valtionavustus) | 1.1 | state-aid administration |

🟡 **The EUPL is COPYLEFT, with a reciprocity obligation and an explicit compatibility list, so this
is an **adopt-and-contribute** tier, not an embed-and-keep one.** 🔵 **That is exactly the
`T29`/`T30` reading applied to a new family: the infrastructure end of education grants its code,
and the grant it uses carries obligations.**

🟢 **And it answers `Gap 395` from an angle the gap never considered.** 🔴 **Pass 104 read EMEA as
"ships releases and does not grant". It grants — under the EU's own licence — and a
permissive-first scan cannot see it.**

### 🟢 🆕 p106 — a Brazilian municipal SIS this KB held but could not read

| platform | licence | bytes | `sha256` (16) | region |
|---|---|---|---|---|
| 🆕 [`portabilis/i-diario`](https://github.com/portabilis/i-diario) | **AGPL-3.0** | 35 326 | `fe85f94658bf66de` | 🟢 **LATAM** — ccTLD `com.br` |
| 🆕 [`portabilis/pre-matricula-digital`](https://github.com/portabilis/pre-matricula-digital) | **AGPL-3.0** | 35 326 | `fe85f94658bf66de` | 🟢 **LATAM** |

🔴 **Both were `UNRECOGNISED` for one reason: the licence text is in PORTUGUESE** — *"LICENÇA PÚBLICA
GERAL AFFERO GNU"* — and this KB's classifier was English-only. 🟢 **One text, two repositories,
byte- and `sha256`-identical (`P1025`).**

🔵 **`i-diario` is a school-diary and academic-management system for Brazilian municipal education
networks, and `pre-matricula-digital` is its enrolment front door.** 🟡 **AGPL-3.0 means network
copyleft: a hosted service built on it owes source to its users, which is a structural constraint on
a managed-service engagement and has to be priced, not discovered late.**

🔵 **Placing note (`P1045`): `i-diario`'s first copyright line reads `Copyright © 2007 Free Software
Foundation` — that is the LICENCE's copyright, not the project's. It placed LATAM on its README's
`.com.br`, not on that line.**

**Pass 104, 2026-10-10.** ⏱️ **Fourteenth pass of this date** (101 ran 09:4x–10:xx UTC; 102,
10:4x–11:xx; this one 12:4x–13:xx). 🟢 **`P1005` applied from the outset — every address below
carries a full 40-character SHA.** 🔴 **`api.github.com` = `http=403` for unattached repos, measured
again this pass; no ★ moved.** 🔴 **`T26`, this page's own trend from pass 102, is REFUTED for the
student-data layer by rows this repository already held — see immediately below.**

### 🟢 🆕 p105 — the two ECL platform rows are **pinned by `sha256`**, and the reason generic tooling drops them is now measured

🔵 **This page has said for several passes that "ECL is precisely the family generic tooling returns
as unclassified." It was right, and the CAUSE is now a measurement rather than an observation.**

🔴 **The ECL-2.0 payload contains ZERO occurrences of the string `Apache License`** — it names the
*"Apache 2.0 license"* in lower case. 🟢 **Any classifier keyed on the Apache title therefore
returns `UNRECOGNISED`, and `Sakai` and `Opencast` fall out of the permissive tier of every scan
that uses one.**

| platform | ECL payload | bytes | `sha256` (16) | permissive? |
|---|---|---|---|---|
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `LICENSE` | 11 120 | `0688f62d04f14e4b` | 🟢 **yes — ECL-2.0** |
| [`opencast/opencast`](https://github.com/opencast/opencast) | `LICENSE` | 11 340 | `76a975068930323e` | 🟢 **yes — ECL-2.0** |
| [`Apereo-LAI/lap-sakai-extractor`](https://github.com/Apereo-Learning-Analytics-Initiative/lap-sakai-extractor) | `LICENSE` | 11 087 | `a9ea5cca8da2c8d5` | 🟢 **yes — ECL-2.0** |
| [`Apereo-LAI/LearningAnalyticsProcessor`](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | `LICENSE` | 9 919 | `fb10d1260ddc8dff` | 🟢 **yes — ECL-2.0** |
| [`Apereo-LAI/OpenDashboard-api`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) | `LICENSE` | 9 919 | `fb10d1260ddc8dff` | 🟢 **yes — identical text** |
| [`Apereo-LAI/OpenDashboard-legacy`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy) | `LICENSE` | 9 919 | `fb10d1260ddc8dff` | 🟢 **yes — identical text** |

🟢 **Six platform and analytics rows, four distinct texts, all declaring *Educational Community
License, Version 2.0, April 2007*.** 🔵 **Payload D is ONE text carried unchanged by three
repositories — the Apereo learning-analytics stack shares its grant, which `P1025` lets this page
state as a fact rather than an impression.**

#### 🟡 What to do with this in front of a client

🔴 **The failure mode is not academic.** A due-diligence report produced with a generic scanner will
show `Sakai` and `Opencast` with no recognised licence, and a risk-averse client reads "no
recognised licence" as "do not touch". 🟢 **The two most mature, best-governed, permissively licensed
platforms in higher education then drop out of the shortlist for a string-matching reason.**

🟢 **The one-line answer to give:** *ECL-2.0 is Apache-2.0 with the patent grant narrowed to
education communities; it is OSI-approved, it is permissive, and here is the `sha256` of the exact
text this repository ships.* 🔵 **That is a checkable claim, which is why the hashes are on this
page and not just in the instrument.**

🟡 **And the governance point is worth more than the licence point for North American HE:** the
Apereo Foundation's committee process is a procurement asset. 🟢 **A permissive licence plus a
foundation with named governance is the combination a university counsel approves fastest.**

### 🟢 🆕 p104 — sixteen platform rows recovered from the reset, and the COPYLEFT half is where the release engineering lives

🔵 **`p1029-lost-address-recovery` probed all 99 addresses `Gap 394` carried.** 🔴 **The result
inverts the shape this page has reported for passes: among the recovered rows, the heavily-released
platforms are almost all copyleft, and the permissive rows are almost all unreleased.**

| platform | grant · bytes | ref · tags | region | what it is |
|---|---|---|---|---|
| [`microsoft/o365-moodle`](https://github.com/microsoft/o365-moodle) | 🔴 **GPL-3.0** · 35 147 B | `master` · 🟢 **695** | 🟢 **North America** (Microsoft) | 🔵 **The most released row in the entire corpus.** Microsoft's own Moodle ↔ Microsoft 365 integration, under Moodle's licence, not Microsoft's |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0** · 7 652 B | 🔴 `v3.0.x-develop` · 🟢 **319** | 🔵 unplaced | Virtual classroom. Re-confirmed byte-exact this pass |
| [`elgg/elgg`](https://github.com/elgg/elgg) | 🔴 **GPL-2.0** · `LICENSE.txt` 17 173 B | 🔴 `7.x` · 🟢 **309** | 🔵 unplaced | Social-learning network engine |
| [`pressbooks/pressbooks`](https://github.com/pressbooks/pressbooks) | 🔴 **GPL-3.0** · `LICENSE.md` 35 147 B | 🔴 `dev` · 🟢 **302** | 🟢 **North America** | Open-textbook authoring and publishing |
| [`saylordotorg/moodle-local_ai_course_assistant`](https://github.com/saylordotorg/moodle-local_ai_course_assistant) | 🔴 **GPL-3.0** · 35 149 B | `main` · 🟢 **295** | 🟢 **North America** (Saylor Academy) | 🔵 **An AI course assistant INSIDE Moodle, from a degree-granting nonprofit** — 295 tags |
| [`yukazakiri/koakademy`](https://github.com/yukazakiri/koakademy) | 🔴 **AGPL-3.0** · `LICENSE.md` 34 523 B | `master` · 🟢 **232** | 🔵 unplaced | Full academy platform. 🔴 **Network copyleft** |
| [`openmage/magento-lts`](https://github.com/openmage/magento-lts) | 🔴 **OSL-3.0** · `LICENSE.txt` 10 293 B | `main` · 🟢 **163** | 🔵 unplaced | 🔴 **Commerce, not education** — carried only because the reset dropped it. OSL-3.0 is a reciprocal licence, not permissive |
| [`manifoldscholar/manifold`](https://github.com/manifoldscholar/manifold) | 🔴 **GPL-3.0** · `LICENSE.md` 35 141 B | `main` · 🟢 **121** | 🟢 **North America** | Scholarly-monograph reading platform |
| [`xiaochong0302/course-tencent-cloud`](https://github.com/xiaochong0302/course-tencent-cloud) | 🔴 **GPL-2.0** · 18 092 B | 🔴 `v2` · 🟢 **67** | 🟢 **APAC** (China) | 🔵 **A Chinese-market online-course platform with real release history** |
| [`nextcloud/integration_openai`](https://github.com/nextcloud/integration_openai) | 🔴 **AGPL-3.0** · `COPYING` 34 519 B | `main` · 🟢 **58** | 🟢 **EMEA** (Germany) | LLM integration for the Nextcloud suite |
| [`nextcloud/context_chat_backend`](https://github.com/nextcloud/context_chat_backend) | 🔴 **AGPL-3.0** · 34 520 B | `master` · 🟢 **53** | 🟢 **EMEA** (Germany) | RAG backend over institutional documents |
| [`moodlehq/moodle-tool_dataprivacy`](https://github.com/moodlehq/moodle-tool_dataprivacy) | 🔴 **GPL-3.0** · 35 147 B | 🔴 `MOODLE_34_STABLE` · 🟢 **20** | 🔵 unplaced (Moodle HQ) | 🔴 **GDPR tooling pinned to a 2017 branch** — `P1021`: the default ref is not the newest release line |
| [`limekiller/moodle-block_openai_chat`](https://github.com/limekiller/moodle-block_openai_chat) | 🔴 **GPL-3.0** · 35 149 B | `main` · 🟢 **10** | 🔵 unplaced | The widely-installed Moodle chat block |
| [`jeanlucio/moodle-local_aihub`](https://github.com/jeanlucio/moodle-local_aihub) | 🔴 **GPL-3.0** · `COPYING.txt` 35 149 B | `main` · 🟢 **9** | 🔵 unplaced | Moodle AI provider hub |
| [`tadreeb-lms/tadreeblms`](https://github.com/tadreeb-lms/tadreeblms) | 🔴 **AGPL-3.0** · 34 523 B | `main` · 🟢 **6** | 🟡 **EMEA** (Arabic-language LMS) | 🔵 **The only Arabic-first LMS row this KB has measured** |
| [`openfun/xblock-proctor-exam`](https://github.com/openfun/xblock-proctor-exam) | 🔴 **AGPL-3.0** · 29 077 B | `master` · 🟢 **4** | 🟢 **EMEA** (France, OpenFUN) | Proctoring XBlock for Open edX |

#### 🔴 The asymmetry, stated as a number because it decides engagement shape

🔵 **Of the 99 probed addresses, 38 are permissive and 21 are copyleft.** 🔴 **But sort by release
engineering and the picture reverses:**

| | permissive (MIT/Apache/BSD) | copyleft (GPL/AGPL/LGPL/OSL) |
|---|---|---|
| rows | 🟢 **38** | 22 |
| 🔴 **rows with ≥ 50 tags** | 5 — `ollama` (689), `temporal` (573), `transformers` (291), `dspace` (136), `fwu-kc-extensions` (118) | 🔴 **11** — `o365-moodle` (695), `bigbluebutton` (319), `elgg` (309), `pressbooks` (302), `moodle-local_ai_course_assistant` (295), `koakademy` (232), `magento-lts` (163), `manifold` (121), `course-tencent-cloud` (67), `integration_openai` (58), `context_chat_backend` (53) |
| 🔴 rows with **zero** tags | 🔴 **19 of 38** | 4 of 22 |

🔵 **`T29`: in education, the PLATFORM is copyleft and released; the permissive supply is mostly
runtime and glue.** 🔴 **Half the permissive rows — 19 of 38 — have never cut a release, against 4
of 22 on the copyleft side.** 🟡 **The claim must be stated precisely, because two rows contradict
the lazy version of it: of the five permissive rows above 50 tags, three are general-purpose runtime
(`ollama`, `temporal`, `transformers`) and 🟢 **two ARE education-specific and released** —
[`dspace/dspace`](https://github.com/dspace/dspace) (BSD-3-Clause, 136 tags, institutional
repository) and [`fwu-de/fwu-kc-extensions`](https://github.com/fwu-de/fwu-kc-extensions)
(Apache-2.0, 118 tags, school identity).** 🔵 **So the honest form is: the permissive education
supply that is RELEASED exists and is two rows wide, and both sit at the INFRASTRUCTURE end —
repository and identity — never at the teaching-and-learning end.** 🔴 **The ADOPT/BUILD line
therefore runs between LAYERS, not between regions: adopt the copyleft platform and accept its
licence, or build the teaching layer yourself on permissive runtime.**

🟡 **And the one case that straddles it is the sharpest commercial fact on this page:
`microsoft/o365-moodle` — 695 tags, authored by Microsoft, published under GPL-3.0.** 🔵 **A vendor
with every incentive to keep its integration proprietary shipped it under the platform's licence,
because the platform's licence is what reaches the installed base.**

#### 🔵 Content rows, which are NOT code and must not be shelved as if they were

| row | grant · bytes | tags | note |
|---|---|---|---|
| [`openstax/osbooks-college-physics-bundle`](https://github.com/openstax/osbooks-college-physics-bundle) | 🟡 **CC family** · 21 442 B | 🟢 **16** | 🟢 **North America** (OpenStax / Rice). Released OER courseware |
| [`scollovati/awesome-lti`](https://github.com/scollovati/awesome-lti) | 🟡 **CC family** · 20 131 B | 0 | LTI ecosystem index |
| [`garethmanning/claude-education-skills`](https://github.com/garethmanning/claude-education-skills) | 🔴 **CC-BY-SA-4.0** · 1 230 B | 0 | 🔴 **Agent SKILLS for education under SHARE-ALIKE.** Derivative skill sets inherit the obligation |
| [`genai-gurus/awesome-eu-ai-act`](https://github.com/genai-gurus/awesome-eu-ai-act) | 🟢 **CC0 1.0** · 7 049 B · `7179683e8000e6bd` | 0 | EU AI Act index — public-domain dedication |
| [`mlx-cassio/awesome-eu-ai-act`](https://github.com/mlx-cassio/awesome-eu-ai-act) | 🟢 **CC0 1.0** · 7 049 B · `7179683e8000e6bd` | 0 | 🔵 **Same bytes AND same `sha256` — a confirmed fork pair** (`P1025` satisfied, not merely suggested) |
| [`morganrcu/awesome-eu-ai-act`](https://github.com/morganrcu/awesome-eu-ai-act) | 🔴 **no payload** · clean 200-control 33 251 B | 0 | 🔴 **Third sibling of the same list, and the grant did not travel with the fork** |

🔵 **`P1032`: a fork inherits the CONTENT and does not necessarily inherit the GRANT.** 🔴 **Three
forks of one index: two carry a byte-and-hash-identical CC0 dedication, the third carries none.**
🟢 **The `sha256` match is what makes the first two safe to use and the third unusable — and byte
count alone could not have told them apart from a coincidence.**

### 🟢 🆕 p102 — the mandated platform query returned FOUR permissive-ERP claims, and this KB had already refuted TWO of them

🔵 **This pass ran the mandated `open source platform education ERP CRM MIT Apache` query. It named
Apache OFBiz, Huly, Corteza and Krayin as permissive options.** 🟢 **Two survive a payload read, two
were already refuted on this page's own history — by the same error, in the same direction.**

| claim from the channel | payload read | verdict |
|---|---|---|
| **Apache OFBiz** "Apache 2.0 ERP/CRM" | 🟢 **Apache-2.0**, `LICENSE` **11 906 B**, `trunk` · `45506b377c855e455942b238dbd55e33fce79d4f`, **26 tags** | 🟢 **TRUE — and now shelved** |
| **Corteza** "Apache 2.0 licensed" | 🟢 **Apache-2.0**, `LICENSE` **11 358 B** *(pristine)*, `2024.9.x` · `3835dfc4ac8bd89381753f09042ad147a4502576`, **298 tags** | 🟢 **TRUE — and now shelved** |
| **Huly** "fully open-source, licensed under Apache License 2.0" | 🔴 **EPL-2.0**, **14 196 B** | 🔴 **FALSE — and this is the THIRD pass in which the channel has said Apache-2.0 about this repository** |
| **Krayin** "licensed under MIT" | 🟡 **MIT, 1 078 B — and `cmp`-identical to `aureuserp/aureuserp`'s 1 077 B payload**, both `Copyright 2010-2025, Webkul Software` | 🟡 **TRUE but MISLEADING — "two independent MIT options" are ONE vendor** (`P564`), and neither is an education system of record |

🔴 **Half of a mandated query's permissive claims were wrong or misleading, and this KB only knew
because it had read the payloads in earlier passes.** 🔵 **`P975` again, and the Huly case is now a
measured REPEAT rather than an anecdote: the secondary channel does not drift toward the truth
with time.**

### 🔴 🆕 p103 `T26` is REFUTED for one layer — and the refuting row was in this repository the whole time

🔵 **Pass 102 closed the table below with: *"There is no row that is both education-specific AND
permissive AND release-engineered."*** 🔴 **There is. Two, and they are the same programme.**

| layer | education-specific? | grant | releases |
|---|---|---|---|
| 🆕 p103 **`ed-fi-alliance-oss/Ed-Fi-ODS`** | 🟢 **yes — the US K-12 student-data spine: enrolment, rostering, assessment, discipline** | 🟢 **Apache-2.0** (`LICENSE.txt` 10 172 B) | 🟢 **42 tags**, top `v7.3.2-pre` |
| 🆕 p103 **`ed-fi-alliance-oss/Ed-Fi-Data-Standard`** | 🟢 **yes — the domain model alone** | 🟢 **Apache-2.0** (10 173 B) | 🟢 **21 tags** |
| 🆕 p103 **`project-sunbird/sunbird-lms-service`** | 🟢 **yes — national-scale LMS services** | 🟢 **MIT** (1 072 B) | 🟢 **450 tags** |
| 🆕 p103 **`project-sunbird/knowledge-platform`** | 🟢 **yes — content, taxonomy, curriculum frameworks** | 🟢 **MIT** (1 072 B) | 🟢 **336 tags** |

🔴 **So `T26` was not a property of the industry. It was a property of this page's coverage.**
🟢 **The census that found them is `Gap 394` / `P1026`**: `archive/2026-10-06-pre-reset/` holds
**82 of 681** addresses that exist nowhere else in this repository, and **103** that appear on no
page — among them `project-sunbird/sunbird-devops` (MIT, **702 tags**), which sat in an instrument's
input worklist and on no shelf.

🔵 **`T26`'s SURVIVING half is still load-bearing, and it is now sharper: the refutation is
REGIONAL.** 🔴 **Both permissive, education-specific, release-engineered platforms belong to NATIONAL
programmes — Ed-Fi to a US alliance, Sunbird to India's public digital infrastructure.** 🟢 **Neither
is a vendor product, and no EMEA or LATAM row of this shape has been measured.** 🔵 **So the honest
statement is: the permissive education-specific platform exists where a national programme built one,
and a studio in a region without one is still doing `P102-A`'s construction.** 🟢 **`T27`.**

🔴 **And the counter-evidence from the same sweep keeps it honest.** The EMEA institutional output of
the same period ships **releases with no grant at all**:
[`european-commission-empl/european-digital-credentials`](https://github.com/european-commission-empl/european-digital-credentials)
is at **`2.0.6`** (4 tags, `master` · `ec562a46f54253bf7ad63af78516b17349502c5c`) with
🔴 **no payload at seven licence names** and a clean 200-control, and
[`fwu-de/schulfach-ontologie`](https://github.com/fwu-de/schulfach-ontologie) (Germany, FWU) ships
**`1.0.0`** with 🔴 **no payload** and a clean control (`README.md` 3 216 B). 🔵 **`Gap 395`.**

### 🔴 🆕 p103 Two platform rows re-measured, and both carry a default-ref hazard

| platform | grant (payload · bytes) | ref · SHA | tags / top | note |
|---|---|---|---|---|
| 🆕 p103 [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0** · **7 652 B** | 🔴 **`v3.0.x-develop`** · `1524a63f2bc53f6145ae94e3327b2b479fce0fcc` | 🟢 **319 / `v4.0.x-beta.3`** | 🔵 **The web-conferencing layer every LMS row on this page integrates with, and it was on no live page after the reset.** 🔴 **`P1020`'s fourth non-standard default branch in three passes** (`dev`, `trunk`, `2024.9.x`, now a release-line develop branch) — 🔴 **a `LICENSE@master` citation for this repo is a 404 on a repository that plainly has a grant**, the exact published-false-negative shape pass 102 caught on OFBiz. 🟡 Top tag is a **beta**, so the shippable line is `v3.0.x`. |
| 🆕 p103 [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 **BSD-3-Clause** · **1 504 B** · © 2002–2021 **LYRASIS** | `main` · `a5b0f0fc17ad5c7f8917eb89b9222f2c2d441aed` | 🟢 **136** | The institutional-repository layer — where a university's own outputs become a corpus an agent can be grounded in. 🔴 **Tag ordering is unsafe: a naive `sort` ranks `language-pack-1_4_1` last**, the same two-spelling hazard `P978` recorded for OpenOLAT. |

🔵 **`P1021` extends on a third row.** `ed-fi-alliance-oss/Ed-Fi-Data-Standard`'s default ref is
**`v6.2.0`** — 🔴 **a TAG-SHAPED branch name.** 🔵 **So a `ref` that looks like a version is not
evidence that a tag was pinned, and `--symref` is the only thing that tells you which you got.**

### 🟢 🆕 p102 `T26` — a permissive SIS is a BUILD on a generic core, never an ADOPT

🔵 **Line the two tiers up and the industry's shape is explicit:**

| layer | education-specific? | grant |
|---|---|---|
| OpenEduCat | 🟢 yes — admissions, academics, exams, fees, library | 🔴 **LGPL-3.0** |
| ERPNext / `frappe-education` | 🟢 yes | 🔴 **GPL** |
| Dolibarr | 🔴 no | 🔴 **GPL-3.0** |
| 🆕 **Apache OFBiz** | 🔴 **no** | 🟢 **Apache-2.0** |
| 🆕 **Corteza** | 🔴 **no** | 🟢 **Apache-2.0** |
| `academico-sis/academico` | 🟢 yes — school management | 🟢 **MIT**, 🔴 **0 tags, no version scheme** (`P985`) |

🔴 **There is no row that is both education-specific AND permissive AND release-engineered.**
🟢 **— SUPERSEDED by `🆕 p103` above: Ed-Fi and Sunbird are both, and both were already in this
repository. Kept as the record of a coverage gap that read as an industry property.**
🟢 **So the permissive path is: take a generic Apache-2.0 core with real release engineering (OFBiz:
26 tags; Corteza: 298) and add the education domain model** — and pass 101 found exactly that domain
model, Apache-2.0, with **57 releases** of schema history (`Jasig/SSP`). 🔵 **Costed as `P102-A`.**

### 🟢 🆕 p101 — the nine-pass run of zeroes ENDS, and not because the platform sweep improved

🔴 **The mandated platform sweep returned another zero, for the ninth time.**
`open source platform education LMS SIS MIT Apache 2026` returned **Moodle** and **Chamilo** (GPL),
**Open edX** (AGPL-3.0 platform / Apache-2.0 components — the conflict this page documents), **Sakai**
(ECL-2.0), **ILIAS**, **Opigno**, **Odoo eLearning**, **Forma LMS**, **OpenOLAT** — 🟢 **all already
published here** — and for student-information systems only **openSIS** and **RosarioSIS**, neither
permissive. 🔵 **A sweep that returns nothing new is information; a sweep that invents a row is not.**

🟢 **But TWO platform-grade rows ARE new this pass — and they arrived from the student-early-warning
CAPABILITY query, not from the platform query.** 🔵 **`P1018`: this page's platform sweep is saturated.
New platforms now arrive from queries that name a CAPABILITY the client asked for, not the word
"platform".**

| platform | grant (payload · bytes · ref · SHA-40) | tags | region | what it is, and how you'd use it |
|---|---|---|---|---|
| 🆕 p101 [`Jasig/SSP`](https://github.com/Jasig/SSP) | 🟢 **Apache-2.0** · `LICENSE` 11 359 B · `master` · `711244dc0d6d5c65fd261c9bec77dd48b4dbaaf6` | 🟢 **57** (`ssp-2.9.0`) | 🟢 **North America** (`P800` — `NOTICE` names JA-SIG, Inc. and **Sinclair Community College**) | **Apereo Student Success Plan** — the only **permissive** student early-warning / case-management platform found in 101 passes. 🔴 **Legacy JVM stack** (portlet-api 2.0, Ext JS, `2.9-SNAPSHOT`) and 🔴 **`NOTICE` bundles Ext JS GPL-3.0 + JasperReports/JFreeChart/c3p0/Hibernate-Commons LGPL + iText MPL** (`P1013`). 🟢 **Customise by taking the SCHEMA and the 57-release domain model onto a modern runtime; do not ship the portlet UI.** |
| 🆕 p101 [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | 🔴 **GPL-3.0** · `LICENSE` 35 141 B · `master` · `5fec948a823e372e740df521aa3684c8df1dcba7` | 🟢 **221** | — (publisher country not established from the repo — not `P800`-grade) | The de-facto open **xAPI Learning Record Store** — the event spine a learning-analytics or early-warning product reads from. 🔴 **GPL-3.0: deploy it as a SERVICE BOUNDARY, never link it into client code.** 🔵 **221 tags makes it the most release-engineered data-layer platform on this page.** |

🔵 **Read with `IMSGlobal/caliper-spec`** (`LICENSE.md` 12 402 B, `master` ·
`1849e118b47acb24a6d97f976fe72fc2f5182570`, 4 tags): 🔴 **an IMS Global *Specification Document
License* — a consortium grant, NOT an OSI licence.** 🟢 **So the analytics interop layer is
spec-licensed, the record store is GPL, and the domain model is Apache-2.0** — three different legal
regimes in one stack, which is precisely the due-diligence `P94-B` exists to run.

### 🟢 🆕 p100 — the one thing the sweep DID add is a tag count, and it is the third instance of `P1010`

🔵 **This pass's structural finding is that this KB declares gaps on columns it never populated for
carried rows** (`P1010`, from `agents/top.md`: `Gap 372` was discharged by two rows carried since
passes 93 and 94 whose tags had never been counted). 🔴 **`OpenOLAT` is the third instance, and it is
on this page.**

🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) re-measured at `master` ·
**`cccdcda6861d48817fa2eef1bb4d2f9f189ab774`**:

| property | this page's state before | 🟢 measured this pass |
|---|---|---|
| **release tags** | 🔴 **never recorded** (the row carries ★ 447, not a tag count) | 🟢 **542 tags**, latest **`OpenOLAT_21.0.3`** |
| licence | 🟢 Apache-2.0, 10 982 B — carried since pass 35 | 🟢 **re-confirmed**, and 🟢 **clause-probed for the first time: 3 of 4** — *Grant of Copyright License*, *Grant of Patent License*, *Redistribution* present, **only *APPENDIX* absent**, which carries no terms |
| `NOTICE.TXT` | not read | 🔴 **14 712 B, and it points at `LICENSE.TXT` — which returns `404`.** The file is `LICENSE` |

🟢 **542 tags makes `OpenOLAT` the most release-engineered platform on this page** — more than
`seb-server`'s 194 — 🔵 **and it is an Apache-2.0 LMS, so the fact matters: it is evidence of
sustained maintenance on the one established platform here a client can fork and close.**

🟢 **`P974` is vindicated by the case that nearly failed it.** 🔴 **10 982 B is NOT canonical
Apache-2.0** (11 357/11 358 B measured a dozen times on this shelf), so a **byte-equality** check
rejects this grant. 🟢 **The clause probe accepts it correctly.** 🔵 **Contrast `wwrwbs/AI_AWE`:
1 865 B and **0 of 4** — the header notice with no terms at all (`P971`).** 🟢 **A byte check calls
both "not Apache"; a title-block check calls both "Apache"; only the clause probe separates them.**

🔴 **And a repository's pointer to its own licence file can be stale** — `NOTICE.TXT` naming a
`LICENSE.TXT` that 404s is `P1009`'s shape in a third form. 🟢 **Three oracles agreed on Apache-2.0
here** (`LICENSE` clauses, `pom.xml` `<url>`, `NOTICE.TXT` prose) 🔵 **and two of the three described
it with a defect — a stripped appendix, a dead filename, and `P988`'s long-recorded
`L6icense` typo in the `<name>`. None of the defects touched the grant.** 🔵 **That is the practical
case for reading payloads rather than trusting any single field.**

🟡 **`P978` holds and is already on this page:** `master` declares **`21.2-SNAPSHOT`**, so the
shippable address is the tag. 🔵 With **542** tags the branch/tag gap is permanent, not incidental.
🟢 **What pass 99 adds to THIS page is the layer that sits BETWEEN an agent and these platforms —
and it does not have one licence, it has three.**
🔴 **Carried rows are still at their pass-92/93/96/98 SHAs and were not re-read.**

## 🔴 🆕 p99 `P1006` — the connector layer, and the platform choice it silently makes for you

🔵 **This page lists platforms the studio can customise. Every pattern that uses one assumes an agent
can REACH it.** 🟢 **Pass 99 read the three repos that provide that reach, and the licence split
falls across platforms, not across repos.**

| platform | connector | grant (payload · bytes · ref · full SHA) | tags / latest | what it means for an engagement |
|---|---|---|---|---|
| **Canvas** (Instructure) | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · 1 071 B · `main` · `b054b913603a206c677565bcbec128652cb9d398` | 🟢 **26 / `v1.14.0`** | 🟢 **Permissive end to end.** 40+ tools over the Canvas API; README 44 176 B. The gradebook is reachable through maintained code. |
| **Moodle** | [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** · 34 523 B · `main` · `5a194a53cc399155bdc5e49737709f43f9a16406` | 🟡 **7 / `v0.1.7`** | 🔴 **Declined.** Network copyleft on a server the client reaches over a network; self-describes as the connector *behind* a commercial product. **Read it as a specification, do not link it.** |
| **Moodle** | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🟢 **MIT** · 1 064 B · `main` · `666f12222ed6cffc9051455eb4799bb2ac8608ce` | 🔴 **0** | 🟡 **Fork base.** 1 064 B of MIT over Moodle Web Services — courses, students, assignments, quizzes, **grades and feedback** — auditable in an afternoon. |

🔴 **The asymmetry, stated plainly: Canvas has a connector that is permissive AND released. Moodle has
one of each and neither is both.**

🔵 **And that is a REGIONAL fact about this page, not a licence trivia row.** Moodle is the platform
this KB has pointed at **LATAM** and the public sector across eight passes — it is what ministries
and public universities actually run, and it is the reason `P91-E` and the offline-first patterns name
it. 🔴 **So the region with the strongest Moodle install base is the region whose agent connector
forces a choice between AGPL-3.0 and untagged**, while **North America**'s dominant higher-ed
platform ships a permissive connector at `v1.14.0`.

🟢 **The manoeuvre, and it is already documented in this repository:** fork and pin
`peancor/moodle-mcp-server`, and treat the AGPL server the way `sebserver-mcp-gate` treats MPL —
as a **readable specification** rather than linked code. 🔵 **The licence decides the integration
shape, so it belongs on the platform page and not only in a trends note.**

🔴 **`P975`, third instance in two passes:** the directory that surfaced the AGPL server described it
only as *"open-source"*. 🟢 **Its payload says AGPL-3.0 at 34 523 B.** 🔴 **And the slip ran in the
expensive direction again** (`P997`): a permissive-sounding label over the one family that can reach
a client's own code across a network.

## 🟢 🆕 p99 `seb-server` — the page's own MPL row, re-read at a full address

🟢 [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) — **MPL-2.0**,
`LICENSE` **16 725 B**, `master` · **`7f45689f79733797e70f8c5318ec9cadb08d03be`**, **194 tags**.
🔵 **Pass 98 restored this row at `7f45689f797337`; pass 99 reproduces the byte term and tag count
exactly and extends the address to the full 40 characters** (`P987`).
🔴 **And it is this page's clearest `P872` false-discard:** at that same pinned SHA its `README.md`
returns **404 / 14 B** while its `LICENSE` returns **200 / 16 725 B**.
🟡 **MPL is copyleft per FILE** (`§1.10(a)`), so a proprietary layer around it is lawful — the third
branch of this page's decision rule, unchanged.

🔵 **And the exam layer now has a dated buyer.** The EU AI Act names **remote exam proctoring** as an
**Annex III high-risk** use of AI in education, and the Digital Omnibus — **Regulation (EU) 2026/1744**,
in force **27 July 2026** — moved those obligations to **2 December 2027**. 🟢 **So the platform on
this page has a compliance deadline 14 months out, and three tested artefacts for it already live in
`compose/code/`.** See `intel/trends.md` `T4`.

## 🔴 🆕 p98 The twelfth permissive-adjacent platform, and this page is where it was LOST

🔵 **Pass 96 added `UniTime` with the note that it had been in `compose/code/` since pass 42 and on no
shelf page. Pass 98 found the sequel and it is worse:** `SafeExamBrowser/seb-server` was on this
KB's platform page, verified, and **the 2026-10-06 reset dropped it** (`Gap 387`).

| platform | grant (payload · bytes · ref · SHA-14) | release ladder | layer | region |
|---|---|---|---|---|
| 🆕 p98 [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | 🟡 **MPL-2.0** · `LICENSE` **16 725 B** · `master` · `7f45689f797337` | 🟢 **194 tags**, `v3.0-latest` | **Exam supervision and lockdown** — the layer this page had nothing for | 🟡 **EMEA** (ETH Zürich lineage: upstream's Java package tree is `ch/ethz/seb/`; 🔵 **package-path evidence, not a holder line** — `P800` cannot be applied, because MPL-2.0's text carries no holder) |

🟢 **The archive proves the row existed:** `archive/2026-10-06-pre-reset/repos-foundations.md:3774`
carries *"🟢 `SafeExamBrowser/seb-server` (⚠️ MPL-2.0, `HEAD` de `master` = `7f45689`,
2026-04-01)"* — 🟢 **and today's independent read reproduces it exactly, with the byte term the
archive never had.**

🔵 **Why it belongs in a tier of its own and not in the permissive tier:** **MPL-2.0 is per-file
copyleft** (§1.10(a)). It is weaker than LGPL in practice — you may ship a proprietary layer around
it, and only **modified MPL files** reciprocate. 🟢 **For a studio this is the most favourable
copyleft on this page**, and it is the first MPL row this KB has ever carried.

🔴 **The decision-rule consequence, and it is the reason this row matters more than its licence:**
this page's **Copyleft tier** instruction is *"build beside, integrate by LTI / SCORM / xAPI"*.
🔴 **That instruction is WRONG for MPL-2.0** — building beside is an unnecessary cost when the
boundary can run through the file. 🟢 **`## The decision rule` at the foot of this page now has a
third branch.**

### 🔴 Two platform licence facts from this pass, and a 429 that stopped the third

- 🔴 **`frappe/lms` is AGPL-3.0, not MIT.** `license.txt` (lowercase), **33 893 B**, `develop` ·
  `933fc6078cfa31`. 🔴 **A 2026 listicle names it as the one MIT-licensed open-source LMS**, and the
  mechanism for the error is readable: 🟢 **`frappe/frappe`, the framework underneath, IS MIT**
  (`LICENSE` 1 118 B). 🔵 **`P1002` — a secondary source's licence claim about an app tends to
  inherit the FRAMEWORK's grant**, and 🟡 **it is a 50 % oracle**: `openeducat/openeducat_erp` is
  **LGPL-3.0** on an LGPL Odoo base, where the inheritance holds. 🔴 **The failure direction is the
  expensive one**, because the framework is always the more permissive of the pair.
- 🔴 **`openeducat/openeducat_erp`'s default branch is `19.0`** — a release number, not `main`,
  `master` or `develop`. 🔵 **First instance on this page of a version-numbered default branch**, and
  one more reason `Gap 380`'s assumed-ref defect is not hypothetical.
- 🟡 **`openeducat`'s `LICENSE` (8 241 B) declares LGPL-3.0 and DELEGATES copyright to a `COPYRIGHT`
  file** — `P984`'s shape in a second repository. 🔴 **That file was not read: `raw.githubusercontent.com`
  returned HTTP 429 exactly there** (`Gap 388`). 🟢 **Carried as a named unknown, not as a verdict.**

## 🟢 🆕 p97 `T16` re-ranks this page for one market: **Kolibri is the lead platform in Africa, not a footnote**

🔴 **This page ranks its permissive tier by capability and licence, and for three of this KB's
regions that is the right axis.** 🟢 **Pass 97's Africa sweep found a fourth market where it is the
wrong axis**, and the finding is in `intel/trends.md` as `T16`: **4 of 4 African countries queried
have teacher-capacity programmes and 0 of 4 have a binding national AI-in-education instrument** —
so what is being procured is **teacher capability and device reach**, on dated timelines, with World
Bank and UNESCO money.

🟢 **The binding technical constraint is named by the delivery programmes themselves, not inferred
here:** Nigeria's **`Naija Teacher AI`** (TRCN × GMind AI) is **built to work offline**, and Kenya's
rollout is a **hardware** programme — **>20 700 smartboards and teacher laptops to junior secondary
schools** via the **Kenya Digital Economy Acceleration Project**, which is a statement about
connectivity, not about pedagogy.

| platform | grant | why the ranking changes |
|---|---|---|
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 🟢 **The only permissive platform on this page designed for intermittent or absent connectivity.** For an African capacity engagement it is **the base**, not an also-ran — every other row in the permissive tier assumes a server a browser can reach. 🔵 **Its MIT grant also makes it the cheapest to fork for a ministry deliverable.** |
| `moodle/moodle` · `openedx/edx-platform` | 🔴 GPL-3.0 / AGPL-3.0 | Still the capability leaders, still the wrong fit here: 🔴 **copyleft plus a connectivity assumption.** |

🔴 **What this does NOT claim.** 🔵 **No new platform was found, no licence was re-read, and Kolibri
has been on this page for many passes** — its grant, its tier and its SHA are unchanged and carried.
🟢 **The change is which market it leads in, and that is a `T16` consequence rather than a platform
finding.** 🔴 **It is recorded on this page because a reader picking a base for a Nairobi or Abuja
engagement from the capability ranking above would pick wrong, and nothing on this page told them
so until now.**

🟢 **The deliverable shape that follows is also inverted, and worth stating because it is
counter-intuitive:** the African capacity market wants **teacher-facing** content generation and
lesson preparation on an offline-capable base — **not** a student-facing tutor. 🔵 **Every mandate
and every programme in the four-country sweep funds the teacher**, and `intel/trends.md` `T16`
carries the evidence.

#### Pass 95 — carried below, unchanged

**Pass 95, 2026-10-10.** ⏱️ **Fifth pass of this date.** 🔴 **No licence on this page was re-resolved this
pass either** — they are carried at their pass-92/93 SHAs, and the sandbox refused
`grant-ladder-v4/ladder.sh` for a **third consecutive pass**, so no replacement classifier was written
(`P237`, `P970`). 🟢 **What pass 95 adds is the version field pass 94 opened, taken from 3 platforms to
12 — plus the rule that makes the number meaningful.**

## 🟢 🆕 p96 The permissive tier gains an eleventh platform — and it was in this repository all along

**Pass 96, 2026-10-10.** ⏱️ **Sixth pass of this date** (91: 23:0x–00:00 UTC; 92: 00:4x–01:3x; 93:
01:4x–02:24; 94: 02:5x; 95: 03:4x; this one 04:4x–05:xx). 🔴 **Repository code refused for a FOURTH
consecutive pass**, so no licence on this page was re-resolved by the instrument; rows are carried at their
pass-92/93/95 SHAs. 🟢 **But 122 of the 127 SHAs this shelf publishes were proved still current, and the
5 that moved were re-read** — `compose/code/p987-census-sha-currency/`.

| platform | grant (payload · bytes · ref · SHA-40 prefix) | version | region | posture |
|---|---|---|---|---|
| 🆕 p96 [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** · `LICENSE` **11 357 B** *(pristine upstream text)* · `master` · `15668a5e54d155` · 🟢 **second oracle agrees**: `pom.xml` declares *"Apache Software License (ASL), Version 2.0"* with the canonical Apache URL | 🟢 `pom.xml` **`4.9`** · **101 tags** · newest **`v4.9.152`** | **North America** (Apereo Foundation) | 🟢 **University timetabling, course and student scheduling.** 🔵 **A layer this tier had nothing for** — every other permissive row delivers content or manages learners; none of them solves the timetable, which is the problem a registrar actually owns. 🔴 **Costing term: `NOTICE` is 22 526 B and HTTP 200**, and Apache-2.0 §4(d) makes propagating it a condition — **the deliverable ships a 22 KB attribution file.** |

🔴 **And the finding behind the row is about this KB, not about UniTime.** `compose/code/unitime-mcp-gate/`
has carried a **tested** MCP gate for this platform since **pass 42**, re-audited in pass 45 against the
four controls written for SEB Server and passing **15/15** on the literal-path control. 🔵 **The
integration was on the shelf; the platform was not. Nothing reconciles the two inventories** — `Gap 381`.

🟢 **`P986` — `UniTime` is the first JVM row here to INVERT `P978`.** Its pom says **`4.9`**, its newest tag
is **`v4.9.152`**: the default branch names a **shippable line**. Sakai (`27-SNAPSHOT` vs `25.2`), Opencast
(`21-SNAPSHOT` vs `20.4`) and OpenOLAT (`21.2-SNAPSHOT` vs `OpenOLAT_21.0.3`) all do the opposite.
🔵 **`P978` is a strong tendency, not a law — and UniTime is the one JVM platform on this page you can
quote a version for without a caveat.**

## 🟢 🆕 p96 `P988` / `Gap 377` — the Maven oracle, measured across the whole JVM tier

🟢 Pass 95 found Sakai's `pom.xml` naming its licence and recorded `Gap 377`. **Pass 96 ran the same read
across every JVM platform on this page, at full 40-character SHAs**
(`compose/code/p987-census-sha-currency/maven-oracle.2026-10-10.tsv`):

| platform | manifest | declared `<name>` | declared `<url>` | payload family | agreement |
|---|---|---|---|---|---|
| [`opencast/opencast`](https://github.com/opencast/opencast) | `pom.xml` 63 148 B | Educational Community License, Version 2.0 | 🟢 `opensource.org/licenses/ECL-2.0` | ECL-2.0 (11 340 B) | 🟢 **name + URL** |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `pom.xml` 14 872 B | Educational Community License, Version 2.0 | 🟢 `opensource.org/licenses/ecl2.txt` | ECL-2.0 (11 120 B) | 🟢 **name + URL** |
| 🆕 [`UniTime/unitime`](https://github.com/UniTime/unitime) | `pom.xml` 26 622 B | Apache Software License (ASL), Version 2.0 | 🟢 `apache.org/licenses/LICENSE-2.0` | Apache-2.0 (11 357 B) | 🟢 **name + URL** |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `pom.xml` 84 963 B | 🔴 **"Apache 2.0 Open Source L6icense"** | 🟢 `apache.org/licenses/LICENSE-2.0` | Apache-2.0 (10 982 B) | 🟡 **URL only** |
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | `build.gradle` 52 855 B | 🔴 **no declaration at all** | — | MIT (1 091 B) | 🔴 **no oracle** |

🟢 **`P988` — the `<url>` is an identifier; the `<name>` is prose. Only one of them is typo-proof.**
**4 of 4 carry a canonical URL. 3 of 4 spell the name correctly.** 🔵 **ECL-2.0 is precisely the family
generic tooling calls *unclassified* — the reason Sakai and Opencast were nearly dropped from this tier in
pass 89 — so a machine-resolvable OSI URL is worth more on this page than anywhere else in the KB.**

🔴 **And `Gap 377`'s other half is refuted: `build.gradle` is not a licence oracle.** Artemis — the row this
page calls *"the best starting point in this industry right now"* — declares no licence in **52 855 bytes**
of Gradle build script. 🔵 **The asymmetry is distribution policy, not language:** a `<licenses>` block is
part of what Maven Central requires of a published POM, and Gradle has no equivalent convention.
**Add `pom.xml` to the ladder; spend nothing on `build.gradle`.**

## 🆕 p96 `P984` — Chamilo has a second licence file, and it is the one with the facts in it

🟢 **`chamilo/chamilo-lms` serves `license.txt` at 1 614 B** beside the **35 147 B** `LICENSE` this page has
been citing for five passes. The big file is the canonical upstream GPL text and says nothing
project-specific. **The small one says three things this page had wrong or missing:**

1. 🔴 **The grant is `GPL-3.0`-***or-later***, not bare `GPL-3.0`.** The payload: *"either version 3 of the
   License, or **(at your option) any later version**."* 🔵 **`or-later` is a different compatibility
   position from `only`** — it is what lets downstream code combine it under GPL-4 if one ever exists —
   and **`P561` is the registered rule that a dropped version qualifier is a defect**, not a rounding.
2. 🟢 **The region reading on this page understates it.** This row says *"EMEA origin (Belgium/Spain), heavy
   LATAM install base"*. **The FIRST copyright line in the payload is `BeezNest Latino SAC, Peru`** — ahead
   of BeezNest Belgium SPRL, NoSoloRed (Spain), Université de Grenoble, Université de Genève, CBlue, VUB,
   HoGent, UGent and UCL: **12 holders across 5 countries.** 🔵 **Chamilo's LATAM attachment is in the
   grant itself** (`P800`), not only in the deployment base — which is a materially stronger claim to make
   to a LATAM ministry.
3. 🔴 **It indirects a third time:** *"The full license can be read in `documentation/license.html`."*
   🔵 **`Gap 378` was found in a `version.php` shim last pass and is here in a licence file.** The shape
   generalises: **this KB's probes read paths; real projects point at other paths.**

🔵 **`P984` for adoption:** *when a repository serves two licence files of very different sizes, read the
small one.* It carries the holders, the version qualifier and the scope. 🔴 **A first-match ladder ordered
`LICENSE` before `license.txt` reads the uninformative file and stops** — and `ladder.sh --all` exists for
exactly this case and could not be run.

#### Pass 95 — carried below, unchanged

## 🟢 🆕 p95 `P978` — the version on the default branch is the one you cannot ship

🔴 **Pass 94 read Moodle's `main` as `6.0dev (MATURITY_ALPHA)` and its stable branch as `5.3`, and wrote
that up as a Moodle quirk.** 🟢 **Pass 95 measured three more platforms and it is the normal case.**

| platform | version file on the default branch | newest release tag | delta |
|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | `6.0dev` · `MATURITY_ALPHA` *(p94)* | **`5.3`** stable | **1 major** |
| 🆕 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `pom.xml` → **`27-SNAPSHOT`** | **`25.2`** | **2 majors** |
| 🆕 [`opencast/opencast`](https://github.com/opencast/opencast) | `pom.xml` → **`21-SNAPSHOT`** | **`20.4`** | **1 major** |
| 🆕 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `pom.xml` → **`21.2-SNAPSHOT`** | **`OpenOLAT_21.0.3`** | 1 minor line |

🔴 **In every case measured, the default branch names a release that does not exist yet.** Sakai's is two
majors ahead of anything an institution can install. 🔵 **For a page that exists to answer "what will we be
deploying", `27-SNAPSHOT` is worse than no answer — it is a number that will never appear in a procurement
document.** 🟢 **`P978`: read the version file for the development line and the tag ladder for the
shippable one, and publish both.**

🟡 **One instrument caveat, measured rather than assumed.** A case-sensitive `sort -V` over OpenOLAT's tags
ranks `OpenOlat_20.0.pre2` **above** `OpenOLAT_21.0.3`, because the project has shipped tags under **two
capitalisations of its own name**. 🔵 **Fold case before sorting a tag ladder** — the defect class of
`p288-agpl-casefold` and `p439-case-collision-gate`, found this time in a tag namespace.

## 🟢 🆕 p95 `P979` — the Maven `pom.xml` is a SECOND licence oracle, and it agreed

Reading Sakai's `pom.xml` for a version returned something that was not asked for:

```xml
<name>Educational Community License, Version 2.0</name>
```

🟢 **An independent, payload-grade confirmation of the ECL-2.0 grant** this page carries from `LICENSE`
(11 120 B). 🔵 **Two files in one repository, read for two different reasons, naming the same licence.**
**ECL is precisely the family generic tooling returns as *unclassified*** — the reason Sakai and Opencast
were nearly dropped from the permissive tier in pass 89 — **so a second concurring oracle is worth more
here than anywhere else on this page.** Recorded as `Gap 377` in `repos/foundations.md`: add
`pom.xml`/`build.gradle` to the ladder's path list for JVM projects.

## 🟢 🆕 p95 Nine more versions, read from the payload

| platform | version file | what the payload says |
|---|---|---|
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | **`ilias_version.php`** *(root — **not** `include/inc.ilias_version.php`, which is 404)* | 🟢 **`ILIAS_VERSION = "11.5 2026-10-06"`** — **a version string carrying its own release date, four days before this pass.** The most precise version field found on this page. |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | root **`version.php`** | 🟢 **`3.0.1`**, `new_version_status => 'stable'`, `new_version_major => true` |
| [`frappe/lms`](https://github.com/frappe/lms) | `lms/__init__.py` | 🟢 **`2.45.2`** |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `version.php` | 🟢 **`31.0.00`** — agrees with its ref `v31.0.00` |
| [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | `openeducat_core/__manifest__.py` | 🟢 **`19.0.1.0`** — the Odoo convention (upstream major `19.0` + module version), agreeing with its `19.0` branch |
| [`mumuki/mumuki-laboratory`](https://github.com/mumuki/mumuki-laboratory) | `lib/mumuki/laboratory/version.rb` | 🟢 **`9.23.0`** |
| [`inducer/relate`](https://github.com/inducer/relate) | `pyproject.toml` | 🟢 **`2024.1`** 🟡 — a **calendar** version, and the newest is 2024. **A maintenance signal the 436★ count does not carry.** |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | `package.json` | 🟢 **`0.1.13`** 🟡 — **a sub-1.0 version on a 1.7k★ platform.** Read it before promising production. |
| 🆕 [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | `pyproject.toml` | 🟢 **`7.0.0`**, newest tag `v7.0.0` — **the only row here where the default branch and the tag ladder agree** |

🔴 **And three negative controls, because an HTTP 200 is not a version.**

| platform | file | HTTP | what it actually carries |
|---|---|---|---|
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `package.json` | **200** | 🔴 **`"version": "0.0.0"`** — a placeholder. **The market's largest AGPL LMS does not version its root manifest.** |
| [`openfun/richie`](https://github.com/openfun/richie) | `src/richie/__init__.py` | **200** | 🔴 `from importlib_metadata import version` — **resolved from installed package metadata, so the version is not in the source at all** |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | `apps/web/package.json` | **200** | 🔴 **no `version` field in the payload** |

🔵 **With pass 94's negative (`openedx/edx-platform`'s `openedx/__init__.py`, a docstring), that is four
distinct ways a 200 carries no version.** 🟢 **The instrument rule: a version channel must report
`NO-VERSION-IN-PAYLOAD` as a value and never fall through to the HTTP code.**

### 🔴 🆕 p95 `P973` has a second form — the `public/` migration leaves a 404 **or** a shim

Pass 94 found Moodle's `version.php` had moved to `public/version.php`, leaving the root 404.
🟢 **Chamilo made the same migration and handled it the opposite way:**

- `main/install/version.php` → **404**
- `public/main/install/version.php` → **200**, and its whole body is
  `return require dirname(__DIR__, 3).'/version.php';` — **a shim pointing back to the repository root**
- root `version.php` → **200**, carrying the real `3.0.1`

🔴 **So on one platform the `public/` move breaks a root probe; on another it breaks a `public/` probe and
redirects you home.** 🔵 **A path list alone cannot resolve this — the probe has to be willing to follow a
one-line `require`.** Recorded as `Gap 378`.

#### Pass 94 — carried below, unchanged

**Pass 94, 2026-10-10.** ⏱️ **Fourth pass of this date.** 🔴 **No licence on this page was re-resolved
this pass either** — they remain carried at their pass-92/93 SHAs, and the sandbox still refuses to execute
`grant-ladder-v4/ladder.sh`, so no replacement classifier was written (`P237`, `P970`). 🟢 **What pass 94
adds to this page is a field it never had: the version, read from the payload.** `P972`, evidence in
`compose/code/p972-platform-version-ladder/`.

## 🟢 🆕 p94 Versions, read from the payload — and the market leader is two releases past every blog

🔴 **Until this pass, every version string on this page came from prose.** Two oracles already in this KB's
map fix it for free: `git ls-remote --heads|--tags <slug>` for the release ladder, and the project's own
version file at a pinned SHA for the release string.

| platform | ladder (as the remote reports it) | release string, from the payload | note |
|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | `MOODLE_500/501/502/**503**_STABLE` in **heads**; `main` is development | 🟢 **`5.3 (Build: 20261005)`**, `$branch='503'`, **`MATURITY_STABLE`** · `main` → **`6.0dev (Build: 20261005)`**, `MATURITY_ALPHA` | 🔴 **Every secondary source read this pass said "5.2 is current."** Both payloads are stamped **2026-10-05**, five days before this pass. |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **19 `open-release/*` heads, newest `sumac.master`** — but `refs/tags/release/teak.1–3` and `release/ulmo.1–4` exist | 🔴 **none** — `openedx/__init__.py` is a docstring and declares no version | 🟡 **`P977`:** the ladder moved heads → tags **and** changed prefix (`open-release/` → `release/`) between Sumac and Teak. A heads probe is two named releases stale; a `grep open-release` over tags misses both. |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | newest tag **`v22.0.2`** | — | 🟢 **The cross-check that catches `P977`:** the distribution operators actually install is three named releases past the newest `open-release` head. |
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | `develop` · `760e2e1` | 🟢 **`version = "10.3"`** in `build.gradle` (line 116) | 🟢 Its build file also pins round a named CVE (`CVE-2026-55760`, FileTemplateLoader path traversal) with the reasoning written in comments — **supply-chain hygiene you can read before you commit to a platform.** |

### 🔴 🆕 `P973` — and `version.php` is **not** at the root

**`moodle/moodle`'s root `version.php` → HTTP 404.** The file is **`public/version.php`**: Moodle **moved
its web root into `public/` at 5.0**.

🔵 **This is `P969` one level up — a reach defect, not a licence defect.** A root-only probe reports
*absent* for a file that exists.

🔴 **And on this page it is money rather than taxonomy.** Every Dockerfile, reverse-proxy rule, `config.php`
path, CI job and theme customisation written against pre-5.0 Moodle points one directory too high. **Read
`public/version.php` in week 0 or discover the restructure in week 3.** 🟢 Control held across three passes:
`COPYING.txt` **35 147 B** at `main` · `f205347`, byte-identical.

### 🟢 `Gap 373` — independently re-derived, and it holds

[`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) → `19.0` · `1c95cef`,
`LICENSE` **8 241 B**, HTTP 200, and the payload says it **in words**: *"OpenEduCat is published under the
GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3), as included below."* 🟢 **So the LGPL-3.0 reading on
this page is correct, now confirmed by a second hand-run read at the same SHA** — *"link, don't absorb"*
stands for this row.

🟢 **And the payload yields the counter-measurement `P960` was missing (`P976`).** Raw case-insensitive
counts, two payloads, this pass:

| payload | *"gnu general public"* | *"gnu lesser"* | family |
|---|---|---|---|
| `EducationalTestingService/factor_analyzer` · 18 092 B | **6** | 2 | 🔴 GPL-2.0 |
| `OpenEduCat/openeducat_erp` · 8 241 B | 1 | **10** | 🟢 LGPL-3.0 |

🔵 **A GPL-2.0 preamble mentions the LGPL — which is why pass 91's ordered first-match test inverted two
platform licences — but it does not mention it *more often than its own name*.** 🔴 **Recorded as a
measurement on n=2, explicitly NOT as a classifier branch**: `P237` exists because pass 91 shipped exactly
that kind of edit on exactly this family, and it cost two licences and a client recommendation. The next
pass that can execute code has the fixtures in `compose/code/p972-platform-version-ladder/pass94-grant-ratios.tsv`.

#### Pass 93 — carried below, unchanged

**Pass 93, 2026-10-10.** ⏱️ **Third pass of this date.** 🔴 **No platform row on this page was
re-resolved this pass** — every licence here is carried at its **pass-92** SHA, read from the payload then
by `compose/code/grant-ladder-v4/ladder.sh`. 🔵 **Pass 93 could not execute that instrument** (this
session's sandbox declines to run repository code) and **declined to write a replacement classifier**,
which is what `P237` requires and what pass 91 violated at the cost of two of the rows on this very page
(`P970`, `repos/foundations.md`). `—` in ★ means not read this pass.

🟢 **One third-party control was run, and it reproduced this page's own negative with a different
instrument.** [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) → `master` · `5d546f2`,
and **404 on `LICENSE`, `LICENSE.txt` and `LICENSE.md`** — independently confirming the *"no grant at
all"* verdict recorded below. 🔵 **A negative that two unrelated instruments reach the same way is the
strongest kind on this page**, and it cost three HTTP requests.

🟡 **And one row on this page is now flagged for re-derivation rather than corrected.**
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) is carried here as LGPL-3.0,
and a current vendor-adjacent source this pass restates *"LGPL v3"*. 🔴 **That is a badge-and-blog
agreement, not a payload read, and it is exactly the evidence class that was wrong for `tao-core` and
`i-educar` one pass ago** — both of which were published as LGPL-3.0 and are GPL-2.0.
🔵 **No correction is asserted: the payload was not read this pass.** 🔴 **But `openeducat_erp` is the
highest-traffic LGPL claim left on this page, and the LGPL→GPL-2.0 error has already fired twice in this
exact family — so it is named as `Gap 373`: re-derive it from the payload before any engagement relies on
"link, don't absorb".**

## 🔴 This file carried the most expensive error in this KB, and it is corrected here

🔴 **Pass 91 recommended, by name, for a named engagement:**
*"a **Brazilian public-sector SIS** → `i-educar` (**LGPL-3.0**) — real municipal deployments;
**link, don't absorb**."*

🔴 **[`portabilis/i-educar`](https://github.com/portabilis/i-educar) is GPL-2.0.** Its payload's title
block reads `GNU GENERAL PUBLIC LICENSE, Version 2, June 1991` (18 092 B — the canonical GPL-2.0 byte
count). 🔴 **"Link, don't absorb" is advice that only exists for LGPL. Against GPL-2.0 it is wrong, and
it is wrong in the direction that puts a studio's deliverable under reciprocity.**

🔵 **And this KB already knew.** `agents/trending.md` carries the row
`| portabilis/i-educar | LGPL | 🔴 GPL-2.0 | LATAM — Brazilian municipal school system |` from an
earlier pass. 🔴 **Pass 91 re-derived the licence with a forked classifier, regressed it, and the
regression propagated from the platform table into the engagement-recommendation table at the bottom
of this file.** The mechanism (`P960`: GPL-2.0's preamble cross-references the LGPL at byte 849, and
the fork tested `"gnu lesser"` first) is in `compose/code/grant-ladder-v4/README.md`.
🟢 **The check that catches the class now exists and is committed:**
`compose/code/p963-shelf-licence-agreement/` — `Gap 356`, discharged after four passes.

🔵 **What did NOT change, stated so the correction is not read as bigger than it is.** `i-educar` is
still real, still large, still in Brazilian municipal use, and still the best regional anchor for that
engagement. 🔴 **What changed is the integration boundary and therefore the cost**: not "link against
it", but "run it as a separate service and integrate across a process/network boundary, or budget for
reciprocity on the modified work".

## Where the platform census now stands

This file got the platform tier wrong twice, in the same direction, and pass 90 corrected it. Pass 91 adds a
row and — more usefully — adds the **two traps that make a platform look open when it is not**.

| pass | the claim | status |
|---|---|---|
| 83–88 | *"The established platform tier is **8 of 8 copyleft**."* | 🔴 **False.** Falsified in pass 89 by `OpenOLAT` (Apache-2.0), carried on this shelf since pass 35. |
| 89 | corrected to *"**2 of 10** permissive"* | 🔴 **Also false** — undercounted by a factor of four. |
| 90 | **at least 9 permissive platforms** | 🟢 Stands. |
| **91** | **10 permissive platforms**, and 🆕 **two mechanisms by which an unopen platform reads as open** | 🟢 measured below |

🔵 **Why it kept failing (pass 90's diagnosis, still the right one).** Both earlier censuses enumerated
whatever sample the previous pass left behind, then reported the sample's licence mix as the tier's. The fix is
a **membership criterion stated before counting**: *a self-hostable platform that manages learners, content and
assessment, with a resolvable repo.*

🔵 **And a licence family the tooling did not know.** `Sakai` and `Opencast` are **ECL-2.0** — the Educational
Community License, OSI-approved, Apache-2.0-derived, **permissive**. A classifier keyed on the familiar
families returns *"unclassified"*, and unclassified reads as risk and gets dropped. 🟢 **The instrument now
knows ECL by name** and both rows classify correctly for the first time.

## Permissive platform tier — build **on** these, fork them, close the deliverable

| platform | grant (payload · bytes · ref · SHA) | ★ | region | posture |
|---|---|---|---|---|
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **MIT** · 1 091 B · `develop` · `760e2e1` | 816 | **EMEA** (TU München) | 🟢 **The best starting point in this industry right now.** Production university platform, MIT, already AI-native: **Iris** (LLM tutor), **Athena** (feedback suggestion), **Hyperion** (AI exercise authoring, Spring AI). Java/Spring. |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** · 11 120 B · `master` · `10a1d90` | 1.2k | **North America** (Apereo Foundation) | 🟢 Mature HE teaching/learning/collaboration suite. **Permissive.** Java. |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **ECL-2.0** · 11 340 B · `develop` · `52805eb` | — | 🟡 **EMEA / North America** (ETH + US university lineage) | 🟢 Lecture capture, transcoding and distribution. The permissive place to attach transcription, captioning and video search. |
| 🟢 **re-measured p100** [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · 10 982 B · `master` · **`cccdcda6861d48817fa2eef1bb4d2f9f189ab774`** · 🟢 **542 tags, `OpenOLAT_21.0.3`** · 🟢 **clause probe 3 of 4** (`P974`) | 447 | **EMEA** (frentix GmbH, Switzerland) | 🟢 Production HE LMS; central LMS of Koblenz University. The EMEA-sovereignty answer. Java. |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | 🟢 **MIT** · 1 684 B · `master` · `001ec46` | 979 | **APAC** (India) | 🟢 LMS for asynchronous online schools, Ruby/Rails. |
| [`inducer/relate`](https://github.com/inducer/relate) | 🟢 **MIT** · 1 145 B · `main` · `7d947c3` | 436 | **North America** (UIUC) | 🟢 Teaching environment with strong assessment primitives; Python/Django. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **MIT** · 1 094 B · `main` · `d0cd78c` | 404 | 🔵 unplaced | 🟢 **School management** (Laravel + Filament) — the closest thing to a **permissive SIS** this KB has found. |
| 🆕 [`openfun/richie`](https://github.com/openfun/richie) | 🟢 **MIT** · 1 079 B · `master` · `8b14aec` | 316 | 🟢 **EMEA** (France Université Numérique / OpenFUN, France) | 🟢 **A CMS for building education portals** — the catalogue, search, course pages and enrolment funnel **in front of** an LMS, MIT, from a French public HE consortium. 🔵 **It fills the one layer this tier had nothing for.** Every other row manages delivery; none of them is the public-facing portal, which is what institutions actually ask to be redesigned. Pairs with Open edX (its native backend) without inheriting AGPL into the portal. |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** · 1 062 B · `main` · `2bca285` | 91 | **EMEA** (Poland) | 🟡 AI-native LMS, TypeScript. Open-core boundary unverified (`Gap 362`). |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD** · 1 531 B · `main` · `196c547` | ~107 | 🔵 unplaced | 🟢 Peer-reviewed AI learning platform (arXiv 2602.07176), local RAG, Ollama-compatible. |
| 🆕 p96 [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** · 11 357 B *(pristine)* · `master` · `15668a5e54d155` · 🟢 `pom.xml` **agrees** | — | **North America** (Apereo Foundation) | 🟢 **University timetabling, course and student scheduling.** Java/Maven, **`v4.9.152`**. 🔵 **The one layer this tier had nothing for.** 🔴 **`NOTICE` 22 526 B — Apache §4(d) makes shipping it a condition.** |
| 🆕 p102 [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** · 11 906 B · 🔴 **`trunk`** · `45506b377c855e455942b238dbd55e33fce79d4f` · 🟢 **26 tags, `release24.09.07`** | — | 🔵 unplaced (Apache Software Foundation) | 🟢 **The permissive ADMINISTRATIVE core.** Java ERP/CRM — accounting, HR, inventory, catalogue, CRM, e-commerce. 🔴 **Not education-specific**: no student, enrolment or gradebook model, so this is a core to BUILD the SIS on, not a platform to deploy (`T26`). 🟢 **`P1013` check CLEAN** — `NOTICE` 166 B; bundles only Noto Sans (Apache-2.0) and Public Domain timezones. 🔴 **Default ref is `trunk` and `master` does not exist** (`P1020`). |
| 🆕 p102 [`cortezaproject/corteza`](https://github.com/cortezaproject/corteza) | 🟢 **Apache-2.0** · 11 358 B *(pristine)* · 🔴 **`2024.9.x`** · `3835dfc4ac8bd89381753f09042ad147a4502576` · 🟢 **298 tags, `2026.9.0-rc.2`** | — | 🔵 unplaced | 🟢 **Low-code CRM / workflow platform, Apache-2.0, with the heaviest release history in this tier (298 tags).** 🟢 Useful where the deliverable is case management — advising caseloads, intervention tracking, student services — rather than an LMS. 🔴 **Not education-specific.** 🔴 **HEAD sits on `2024.9.x` while tags run to 2026** (`P1021`); 🟡 tip is `-rc`, not GA. |

🟢 🆕 **p102: 13 permissive platforms** (11 at p96 + **OFBiz** and **Corteza**, promoted from this
KB's own append-only history rather than found by a search — `Gap 384`'s shape again).
**6 of them production-grade with named institutional deployments.**
🔴 **And the two new rows are the only ones in this tier that are NOT education-specific**, which is
the whole content of `T26`: this tier's permissive half and its education-specific half barely overlap.
🔵 **The eleventh was not found by a search — it was found by reading this repository's own
`compose/code/` directory against this page** (`Gap 381`).

🔴 🆕 **p96 — the caveat that belongs beside the permissive-SIS recommendation, not in a footnote.**
This page calls [`academico-sis/academico`](https://github.com/academico-sis/academico) *"the closest thing
to a permissive SIS this KB has found"*. Measured this pass: **MIT declared in both `composer.json` and the
1 094 B payload** 🟢, **404 ★** 🟢 — and 🔴 **ZERO release tags, and no `version` field in either
`composer.json` or `package.json`.** 🔵 **A fork inherits release engineering, a version scheme and an
upgrade path that do not exist.** It remains the best permissive answer to the most common ask on this
page; **it is a starting point with a build attached, not a product to deploy.** `P985`.

## 🆕 The two traps — a platform that reads as open and is not

🔴 **Trap 1 — the source-available licence with a friendly name.**

| platform | grant | ★ | what happened |
|---|---|---|---|
| 🆕 [`leemonade/leemons`](https://github.com/leemonade/leemons) | 🔴 **"Fair Code License" v1.0** · `LICENSE.md` 10 830 B · `main` · `b1ca5d8` | 292 | 🔴 **Not an OSI licence, and not open source.** A learning-experience platform listed on `topics/lms` among genuinely open projects. 🔴 **v2's classifier returned `OTHER/unclassified` for it** — which is conservative but silent. 🟢 v3 names it `FAIRCODE-NOT-OSI`, alongside `BSL-1.1` and the Sustainable Use License, **so it can never be reported as open**. |

🔵 **Why it needs naming rather than dropping.** *Fair Code* is a movement, not a licence family, and its
licences permit self-hosting while restricting commercial redistribution — exactly the clause that breaks a
studio deliverable, and exactly the clause a procurement reviewer will not find if the shelf says
"unclassified". **The same shape caught `n8n` in the technology KB. It is now a named family here.**

🔴 **Trap 2 — the grant that is not in a file at all.**

| platform | grant | ★ | what happened |
|---|---|---|---|
| 🆕 [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) | 🔴 **No licence payload in 24 filenames** · `develop` · `061a3ac` | 275 | 🔵 **Almost certainly GPL** — WordPress plugins declare their grant in a **PHP header comment**, which filename probing cannot see. |
| [`gocodebox/lifterlms`](https://github.com/gocodebox/lifterlms) | 🔴 **GPL-3.0** · 35 141 B · `trunk` · `6ff84cf` | 211 | 🟢 Same ecosystem, **ships a `LICENSE` file**. |
| 🆕 [`atutor/ATutor`](https://github.com/atutor/ATutor) | 🔴 **No licence payload in 24 filenames** · `master` · `333030f` | 180 | 🔴 The accessibility-pioneer LMS (Toronto), historically GPL, with **no grant file at the resolved SHA**. No longer user-level supported. |

🔵 **The transferable rule: within one ecosystem, grant *location* varies by project convention.** Two
WordPress LMS plugins, same licence family, one discoverable and one not. 🔴 **So "no payload" means
*unverifiable from the repo root*, which is weaker than "ungranted" — and this shelf must not collapse the
two.** For `learnpress` the next step is a header read, not a conclusion.

## Linkable tier — LGPL, so link but do not absorb

🔴 **This tier had three rows last pass and has one.** Two were misclassified GPL-2.0 (above), and the
tier they were in is precisely the tier whose name states the integration strategy — 🔵 **which is why
a one-word licence error here costs more than it would anywhere else on the shelf.**

| platform | grant (payload · bytes · ref · SHA) | region | what it is |
|---|---|---|---|
| [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | 🟡 **LGPL-3.0** · 8 241 B · `19.0` · `1c95cef` | 🔵 unplaced | LMS + SIS on one Odoo database — the ERP-shaped option. 🟢 **Verified genuinely LGPL-3.0 this pass**, from a payload that says so in words: *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3)"*. **The only remaining linkable platform on this shelf.** |

### 🔴 Moved OUT of this tier this pass — both are full copyleft

| platform | was published as | is | what changes for a deliverable |
|---|---|---|---|
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 LGPL-3.0 · 18 092 B | 🔴 **GPL-2.0** · 18 092 B · `2.12` · `cd1da68` · 🟢 **LATAM** (Brazil) | 🔴 No linking exception. Brazil's largest free education software and a real municipal SIS — **integrate across a service boundary, do not link or absorb.** 🔵 Pass 87's *"no permissive open-source SIS exists"* is **no longer qualified by this row**: it stands unqualified. |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 LGPL-3.0 · 18 025 B | 🔴 **GPL-2.0** · 18 025 B · `develop` · `d9d462a` · **EMEA** (Luxembourg) | 🔴 The serious QTI assessment platform, and **GPL-2.0-only** — one-way incompatible with GPL-3.0 code, which constrains what can be combined with it as well as what can be shipped. |

## Copyleft tier — build **beside**, integrate by LTI / SCORM / xAPI

Not inferior software. Several are the best in the industry. The constraint is on the *deliverable*, not the quality.

| platform | grant (payload · bytes · ref · SHA) | ★ | region |
|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** · `COPYING.txt` 35 147 B · `main` · `f205347` | — | 🟢 **APAC** (Moodle HQ, Perth, Australia) — the market leader is an Australian project, which matters for an APAC pitch |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** · 35 136 B · `master` · `2e46ebd` | — | **North America** (Axim Collaborative) |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** · 34 523 B · `release` · `2776223` | 1.1k | 🔵 unplaced — the Docker Open edX distribution, i.e. how Open edX actually gets deployed |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** · 34 520 B · `master` · `1c9f0bb` | — | **North America** (Instructure) |
| [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** · `license.txt` 33 893 B · `develop` · `933fc60` | 3.3k | **APAC** (India) — 🔴 **widely mis-listed as MIT.** 🆕 **And the row that exposed the instrument defect v3 fixes:** v2 never probed the lowercase `license.txt` and recorded it as *no grant*. |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 🆕 **p96 GPL-3.0-*or-later*** · `LICENSE` 35 147 B **+ `license.txt` 1 614 B** · `master` · `e5cf557` *(HEAD moved from `f30df11`; grant unchanged)* | 1.0k | 🟢 🆕 **p96 LATAM is in the GRANT**: the payload's **first** copyright line is **`BeezNest Latino SAC, Peru`**, ahead of BeezNest Belgium — 12 holders across Peru, Belgium, Spain, France and Switzerland (`P800`). Still 🟢 EMEA origin with a heavy LATAM install base; **the practical LATAM LMS incumbent.** |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL-3.0** · 35 147 B · `release_11` · `c212185` | 505 | **EMEA** (Germany) |
| 🆕 [`claroline/Claroline`](https://github.com/claroline/Claroline) | 🔴 **AGPL-3.0** · 34 616 B · `15.0` · `396eeba` | 350 | 🟢 **EMEA** (Belgium) — a long-running European LMS; note the default branch is a **version number**, not `main` |
| 🆕 [`elmsln/elmsln`](https://github.com/elmsln/elmsln) | 🔴 **GPL-3.0** · `LICENSE.md` 35 193 B · `master` · `41f22f9` | 253 | **North America** (Penn State) — education innovation platform |
| 🆕 [`mumuki/mumuki-laboratory`](https://github.com/mumuki/mumuki-laboratory) | 🔴 **AGPL-3.0** · 34 523 B · `master` · `fce1ede` | 199 | 🟢 **LATAM** (Argentina) — 🟢 **programming practice with automated feedback**, in real school and university use. The strongest LATAM row in the assessment tier. |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | 🔴 **AGPL-3.0** · 34 523 B · `dev` · `9a13191` | 2.3k | 🔵 unplaced |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 🔴 **AGPL-3.0** · 34 523 B · `main` · `c225cc4` | 1.7k | 🔵 unplaced |
| [`codelitdev/courselit`](https://github.com/codelitdev/courselit) | 🔴 **AGPL-3.0** · `LICENSE.md` 34 143 B · `main` · `62b5abb` | 1.3k | 🔵 unplaced |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **GPL-3.0** · 35 121 B · `v31.0.00` · `1d83c2b` | — | 🟡 **APAC** (Hong Kong lineage) — K-12 school platform |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** · 15 214 B · `mobile` · `541c509` | — | 🟡 **LATAM** lineage (named for Rosario, Argentina) — SIS. 🆕 **Version recovered this pass**: the payload says *"Version 2, June 1991"* and pass 91 published the bare family `GPL`. 🔵 **Its 15 214 B variant text drops the LGPL cross-reference entirely, which is why the same forked classifier that misread `tao-core` and `i-educar` left this row merely imprecise rather than wrong** — the natural control for `P960`. |

🔴 **No grant at all:** [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) · `master` ·
`5d546f2` — **no licence payload in 24 candidate filenames** (was 12; the negative is now twice as strong).
Frequently listed as "GPL" in comparison articles. Unusable until the publisher states a grant.

## 🆕 `topics/lms` is contaminated by an acronym collision — measured

🔵 **The channel this census draws on has a precision problem the other channels do not, and it is worth
knowing before anyone trusts a count from it.** `topics/lms` holds **2 432** repos. On **page 2**, 4 of 20 rows
are not learning platforms at all:

| row | ★ | what it actually is |
|---|---|---|
| `micro-nova/AmpliPi` | 340 | whole-house audio system |
| `tompazourek/Colourful` | 299 | .NET colour-space conversion |
| `LiXirong/AdaptiveFilterandActiveNoiseCancellation` | 180 | 🔵 **LMS = *Least Mean Squares*** adaptive filter |
| `wesdoyle/lightlib-lms` | 152 | 🔵 **LMS = *Library* Management System** |

🔴 **80 % precision on page 2 against ~100 % on page 1.** 🔵 **Cause: "LMS" is an acronym with at least three
unrelated expansions, and the collision rate rises as you go down the star ranking** — the high-star head is
dominated by real learning platforms, the tail is not. 🟢 **`topics/ai-tutor` (664) and `topics/scorm` (220)
do not have this problem**, because both phrases are unambiguous. **Prefer unambiguous topic phrases; discount
any count drawn from an acronym topic.**

## The decision rule

| the engagement needs… | use | because |
|---|---|---|
| the deliverable **closed and owned**, AI included | 🟢 **`Artemis` (MIT)** | permissive, production, already has the three AI subsystems |
| **EMEA public-sector sovereignty**, self-hosted, closable | 🟢 **`OpenOLAT` (Apache-2.0)** or `Artemis` | named European university deployments |
| **North American HE**, permissive, committee-friendly | 🟢 **`Sakai` (ECL-2.0)** | Apereo governance is a procurement asset, not just a licence |
| 🆕 the **public-facing portal / catalogue** redesigned | 🟢 **`richie` (MIT)** | the only permissive row at that layer; French public-HE provenance |
| **lecture video** + transcription/captioning AI | 🟢 **`Opencast` (ECL-2.0)** | permissive at exactly the layer AI attaches to |
| **offline / low-connectivity** delivery | 🟢 **`Kolibri` (MIT)** | built for it; see `repos/foundations.md` |
| a **Brazilian public-sector SIS** | 🔴 **`i-educar` (GPL-2.0)** | 🔴 **CORRECTED — was published here as LGPL-3.0 / "link, don't absorb".** Real municipal deployments, still the right regional anchor; **integrate across a service boundary, or budget for reciprocity.** No permissive SIS exists. |
| a **high-stakes QTI assessment** platform | 🔴 **`tao-core` (GPL-2.0)**, or 🟢 **`Numbas` (Apache-2.0)** for browser-native maths assessment | 🔴 **CORRECTED — `tao-core` was published here as LGPL.** For a closable deliverable prefer `Numbas` + `Submitty` (BSD); reach for TAO when full QTI conformance is the requirement and accept the boundary. |
| 🆕 **mastery-gated progression** / adaptive sequencing | 🟡 **`pykt-toolkit` (MIT)** for predictive accuracy, 🟢 **`pyBKT` (MIT)** for a deliverable | 🔴 🆕 **p93 reverses the default here.** Both are MIT, but under Annex III assessing learning outcomes owes an explanation: `pyBKT`'s prior/learn/slip/guess are explainable, a trained network's activation is not. See `repos/foundations.md` Tier 2c and `P93-A`. |
| 🆕 p93 **adaptive testing** — shorter tests, same confidence, defensible | 🟢 **`catsim` (BSD-3-Clause)** + **`py-irt` (MIT)** | the only CAT engine on this shelf; `catsim` cannot calibrate items and says so, `py-irt` does it. 🔴 **Pin `catsim`'s ref: its default branch is `dev`.** `P93-A` |
| 🆕 p93 **BNCC-aligned content or tutoring (Brazil)** | 🟢 **`bncc-dados` (MIT code / CC BY 4.0 data)** + its MCP server | 🟢 **The national curriculum as audited open data** — 1 721 objectives, per-record provenance, 1 576/1 580 character-exact against the official MEC/CNE PDF. 🟢 **Embed the dataset, don't call it: measured 0.2 % vs 2.3 % hallucination** (`T11`). 🔴 **The CC BY 4.0 data grant is not at the repo root** (`P969`). `P93-B` |
| 🆕 p93 **open-response / essay scoring** | 🔴 **nothing permissive and production-grade exists** | 🔴 `Gap 372`. The whole permissive supply is one 2★ Apache-by-reference research repo. **Scope essays out, or price a human grader into the loop** — this is the activity the EU AI Act names most explicitly and the one with the least open supply. |
| 🆕 **LATAM programming education** with autograding | 🟡 **`mumuki-laboratory` (AGPL-3.0)** | Argentine, in real classroom use; integrate by LTI, don't absorb |
| the client's **existing Moodle / Canvas / Open edX** kept | 🔴 build **beside** it, integrate via LTI 1.3 / SCORM / xAPI | GPL/AGPL reciprocity follows the modified work |
| 🆕 p98 **invigilated / locked-down online exams** | 🟡 **`seb-server` (MPL-2.0)** — integrate directly, do **not** build beside | 🟢 **Per-file copyleft (§1.10(a))**: a proprietary layer around it is lawful and only modified MPL files reciprocate. 🟢 Three tested artefacts already in `compose/code/`. 🔴 Audit affect/engagement inference first — prohibited in education since **2 Feb 2025**. |
| 🆕 p98 **the whole exam lifecycle** — schedule, supervise, grade | 🟢 **`UniTime` (Apache-2.0)** + 🟡 **`seb-server` (MPL-2.0)** + 🟢 **`moodle-grading-mcp` (MIT)** | 🟢 **Every piece has a tested gate committed here**, and the grading end never releases a grade (`workflowstate=readyforreview`). See `compose/patterns.md` `P98-A`. |
| 🆕 p98 **corporate L&D / skills inference** | 🟢 **`ojd_daps_skills` (MIT)** — taxonomy as a parameter | 🔴 **Do NOT reach for `skills-ml`**: University of Chicago **non-commercial** terms, commercial use prohibited (`P999`). |
| 🆕 p98 **a self-hosted LMS a blog called MIT** | 🔴 **`frappe/lms` is AGPL-3.0** | 🔴 The **framework** (`frappe/frappe`) is MIT; the app is not (`P1002`). Read the app's own payload. |

🔵 🆕 **p93 — one addition to how this page should be read, because a new row broke its category.** Every
row above answers *"which platform do we build on or beside?"*. 🟢 **`bncc-dados` is not a platform and
does not belong in that question** — it is a **standards-data layer** that attaches to whichever platform
the client already runs, which is why it appears in the rule table with no platform attached. 🔵 **The
general form is worth stating: the most valuable permissive artefacts in this industry are increasingly
not platforms at all** — they are spec implementations, verified datasets and psychometric libraries, all
of which sit *beside* the client's LMS rather than replacing it. **That is the same conclusion
`P91-RETIRED` reached from the platform side, arrived at from the data side.**

## Open gaps on this page

- 🟢 🆕 **p94: `Gap 373` DISCHARGED.** `OpenEduCat/openeducat_erp` → `19.0` · `1c95cef`, `LICENSE`
  **8 241 B**, and the payload states it in words: *"OpenEduCat is published under the GNU LESSER GENERAL
  PUBLIC LICENSE, Version 3 (LGPLv3)"*. The LGPL-3.0 reading on this page was right; *"link, don't absorb"*
  stands. 🔵 **Pass 93 was right to flag rather than correct it** — the flag cost one pass and the answer
  cost three HTTP requests.
  🔴 **Pass 93's text is left in place above** rather than rewritten, so the record shows a flag raised on
  badge-and-blog evidence and then settled from the payload.
- 🔴 🆕 **p94: `Gap 375` — the version field is payload-derived for 3 platforms and prose for the rest.**
  Moodle, Artemis and Open edX/Tutor were read this pass (section at the top of this page). Every other row
  here still carries a version nobody verified, and `P972` makes verifying it mechanical.
- 🔴 🆕 **p94: `Gap 376` — the `public/` restructure is unmeasured beyond Moodle.** `P973` found one
  platform that moved its web root and broke every root-relative assumption written before 5.0. **No other
  platform on this page has been probed for the same class of change**, and the probe is one HTTP request
  per candidate path.
- 🟢 🆕 **p96: `Gap 375` FULLY DISCHARGED on this page, and the remainder was *unmeasurable* rather than
  unmeasured.** `pupilfirst`, `academico` and `open-tutor-ai-CE` all serve their manifest at **HTTP 200
  with no `version` field**, and the reason is structural: two declare `"private": true`, the npm
  convention for a workspace root never published to a registry. 🟢 **`P985` splits "no version" into three
  facts** — `UNVERSIONED-BUT-RELEASED` (`open-tutor-ai-CE`: 1 tag, quote **`v1.0.0`**),
  `COMPONENT-VERSIONED` (`pupilfirst`: **57 tags, all scoped npm sub-packages** — the platform has never
  shipped as a unit) and `UNRELEASED` (`academico`: **0 tags**). **12 payload-derived versions became 13
  with UniTime; the three that remain do not exist to be read.**
- 🟢 🆕 **p96: `Gap 377` ANSWERED with a correction to its own wording.** The Maven reader already exists
  and is already wired (`p289` → `p283::PARSERS`, by `P294`) — **one import, not new code** (`P237`). And
  **`build.gradle` is not a licence oracle**: Artemis declares none in 52 855 B. 🟢 **The oracle itself pays
  on 4 of 4 Maven platforms** (table above). 🔴 **New `Gap 382`: it should read `<url>`, not `<name>`**
  (`P988`) — **4 of 4 carry a canonical URL, 3 of 4 spell the name right.**
- 🟡 🆕 **p96: `Gap 378` has a third form, now in a licence file rather than a version file** (`P984`).
  Chamilo's 1 614 B `license.txt` points at **`documentation/license.html`**. 🔵 **Probing a path list
  cannot follow an indirection, and real projects indirect in both their version files and their licence
  files.** Worth one HTTP request next pass.
- 🔴 🆕 **p96: `Gap 381` — nothing reconciles `compose/code/` against this page.** `UniTime/unitime` is
  Apache-2.0 with 101 release tags and a tested MCP gate in this repository **since pass 42**, and it
  reached this page only now. 🔵 **A verified platform can sit in the evidence directory for fifty passes
  without ever being offered to a client.** **Cost of the fix: one grep of `compose/code/*/README.md` for
  `github.com/` slugs, diffed against this page.**
- 🔴 **`Gap 376` carried, now BOUNDED.** Four consecutive passes without the instrument. 🟢 **122 of 127
  published SHAs on this shelf are still the tip of their pinned ref; the 5 that moved were re-read and
  kept their grant.** 🔴 **That is not a re-verification** — it says nothing about filename reach or
  classifier soundness, which only `grant-ladder-v4` settles.
- 🔴 **No permissive SIS exists**, for any region — **and `academico`'s zero-tag finding sharpens rather
  than softens that.** The nearest permissive row has never cut a release. Unchanged otherwise, and
  re-stated because it is the most common ask this page cannot answer well.
- 🔴 **No permissive H5P *authoring* server** (the Node port is GPL too). Unchanged.

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
