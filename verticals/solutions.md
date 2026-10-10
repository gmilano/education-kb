---
industry: education
region: Global
updated: 2026-10-10
---

# Education — vertical platforms you can customise with AI

**Pass 92, 2026-10-10.** ⏱️ **Second pass of this date.** Licences read from the payload at a pinned
SHA with `compose/code/grant-ladder-v4/ladder.sh` — **24 filenames at a 1-byte floor**, and classified
by the **shared** `compose/code/lib/license_family.sh` rather than by a classifier of the instrument's
own (`P237`). `—` in ★ means not read this pass.

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

🟢 **10 permissive platforms. 5 of them production-grade with named institutional deployments.**

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
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0** · 35 147 B · `master` · `f30df11` | 1.0k | 🟢 **EMEA** origin (Belgium/Spain), 🟢 **heavy LATAM install base** — the practical LATAM LMS incumbent |
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
| 🆕 **mastery-gated progression** / adaptive sequencing | 🟢 **`pykt-toolkit` (MIT)** | the learner-model layer this shelf lacked for eight passes; see `repos/foundations.md` Tier 2b |
| 🆕 **LATAM programming education** with autograding | 🟡 **`mumuki-laboratory` (AGPL-3.0)** | Argentine, in real classroom use; integrate by LTI, don't absorb |
| the client's **existing Moodle / Canvas / Open edX** kept | 🔴 build **beside** it, integrate via LTI 1.3 / SCORM / xAPI | GPL/AGPL reciprocity follows the modified work |

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
