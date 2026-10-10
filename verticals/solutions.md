---
industry: education
region: Global
updated: 2026-10-10
---

# Education — vertical platforms you can customise with AI

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
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · 10 982 B · `master` · `cccdcda` | 447 | **EMEA** (frentix GmbH, Switzerland) | 🟢 Production HE LMS; central LMS of Koblenz University. The EMEA-sovereignty answer. Java. |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | 🟢 **MIT** · 1 684 B · `master` · `001ec46` | 979 | **APAC** (India) | 🟢 LMS for asynchronous online schools, Ruby/Rails. |
| [`inducer/relate`](https://github.com/inducer/relate) | 🟢 **MIT** · 1 145 B · `main` · `7d947c3` | 436 | **North America** (UIUC) | 🟢 Teaching environment with strong assessment primitives; Python/Django. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **MIT** · 1 094 B · `main` · `d0cd78c` | 404 | 🔵 unplaced | 🟢 **School management** (Laravel + Filament) — the closest thing to a **permissive SIS** this KB has found. |
| 🆕 [`openfun/richie`](https://github.com/openfun/richie) | 🟢 **MIT** · 1 079 B · `master` · `8b14aec` | 316 | 🟢 **EMEA** (France Université Numérique / OpenFUN, France) | 🟢 **A CMS for building education portals** — the catalogue, search, course pages and enrolment funnel **in front of** an LMS, MIT, from a French public HE consortium. 🔵 **It fills the one layer this tier had nothing for.** Every other row manages delivery; none of them is the public-facing portal, which is what institutions actually ask to be redesigned. Pairs with Open edX (its native backend) without inheriting AGPL into the portal. |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** · 1 062 B · `main` · `2bca285` | 91 | **EMEA** (Poland) | 🟡 AI-native LMS, TypeScript. Open-core boundary unverified (`Gap 362`). |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD** · 1 531 B · `main` · `196c547` | ~107 | 🔵 unplaced | 🟢 Peer-reviewed AI learning platform (arXiv 2602.07176), local RAG, Ollama-compatible. |
| 🆕 p96 [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** · 11 357 B *(pristine)* · `master` · `15668a5e54d155` · 🟢 `pom.xml` **agrees** | — | **North America** (Apereo Foundation) | 🟢 **University timetabling, course and student scheduling.** Java/Maven, **`v4.9.152`**. 🔵 **The one layer this tier had nothing for.** 🔴 **`NOTICE` 22 526 B — Apache §4(d) makes shipping it a condition.** |

🟢 🆕 **p96: 11 permissive platforms. 6 of them production-grade with named institutional deployments.**
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
