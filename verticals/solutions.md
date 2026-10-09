---
industry: education
region: Global
updated: 2026-10-09
---

# Education — vertical platforms you can customise with AI

**Pass 90, 2026-10-09.** Licences read from the payload at a pinned SHA; existence by `git ls-remote --symref`.
`—` in ★ means not read this pass.

## The headline correction of this pass

This file has twice published a census of the platform tier and twice got it wrong in the same direction.

| pass | the claim | status |
|---|---|---|
| 83–88 | *"The established platform tier is **8 of 8 copyleft**. Not one MIT, Apache-2.0 or BSD row."* | 🔴 **False.** Falsified in pass 89 by `OpenOLAT` (Apache-2.0), which this KB had carried since pass 35. |
| 89 | corrected to *"platform / LMS: **2 of 10** permissive"* | 🔴 **Also false, and undercounted by a factor of four.** |
| **90** | **at least 9 permissive platforms, including a production AI-native MIT one** | 🟢 measured below |

🔵 **Why it kept failing.** Both earlier censuses enumerated whatever sample the previous pass happened to
leave behind, then reported the sample's licence mix as the tier's. The fix is not more care — it is a
**membership criterion stated before counting**. The criterion used here: *a self-hostable platform that
manages learners, content and assessment, with a resolvable repo.* Against that criterion, `topics/lms`
sorted by stars (2 432 repos, first 20 read) plus this KB's existing rows yields the table below.

🔵 **A second, mechanical cause, worth more than the census itself.** Two of the permissive platforms carry
**ECL-2.0 — the Educational Community License 2.0**, an OSI-approved, Apache-2.0-derived permissive grant with
a patent clause written for universities. A licence classifier keyed on the familiar families returns
*"unclassified"* for it, and an unclassified row reads as a risk and gets dropped. **Education has its own
permissive licence family, and tooling that does not know the name will systematically undercount the tier.**
That is almost certainly part of how `8 of 8` survived six passes.

## Permissive platform tier — build **on** these, fork them, close the deliverable

| platform | grant (payload · bytes · ref · SHA) | ★ | region | posture |
|---|---|---|---|---|
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **MIT** · 1 091 B · `develop` · `760e2e1` | 816 | **EMEA** (TU München) | 🟢 **The best starting point in this industry right now.** Production university platform, MIT, already AI-native: **Iris** (LLM tutor), **Athena** (feedback suggestion), **Hyperion** (AI exercise authoring, Spring AI). Java/Spring. |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** · 11 120 B · `master` · `10a1d90` | 1.2k | **North America** (Apereo Foundation) | 🟢 Mature HE teaching/learning/collaboration suite. **Permissive** — see the ECL note above. Java. |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **ECL-2.0** · 11 340 B · `develop` · `52805eb` | — | 🟡 **EMEA / North America** (ETH + US university lineage) | 🟢 Lecture capture, transcoding and distribution. The permissive place to attach transcription, captioning and video search. |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · 10 982 B · `master` · `cccdcda` | 447 | **EMEA** (frentix GmbH, Switzerland) | 🟢 Production HE LMS; central LMS of Koblenz University. The EMEA-sovereignty answer. Java. |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | 🟢 **MIT** · 1 684 B · `master` · `001ec46` | 979 | **APAC** (India) | 🟢 LMS for asynchronous online schools, Ruby/Rails. MIT. |
| [`inducer/relate`](https://github.com/inducer/relate) | 🟢 **MIT** · 1 145 B · `main` · `7d947c3` | 436 | **North America** (UIUC) | 🟢 Teaching environment with strong assessment primitives; Python/Django. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **MIT** · 1 094 B · `main` · `d0cd78c` | 404 | 🔵 unplaced | 🟢 **School management** (Laravel + Filament) for small/medium institutions — the closest thing to a **permissive SIS** this KB has found. |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** · 1 062 B · `main` · `2bca285` | 91 | **EMEA** (Poland) | 🟡 AI-native LMS, TypeScript. Open-core boundary unverified. |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD** · 1 531 B · `main` · `196c547` | ~107 (snippet) | 🔵 unplaced | 🟢 Peer-reviewed AI learning platform (arXiv 2602.07176), local RAG, Ollama-compatible. |

🟢 **9 permissive platforms. 4 of them production-grade with named institutional deployments.**

## Linkable tier — LGPL, so link but do not absorb

| platform | grant (payload · bytes · ref · SHA) | region | what it is |
|---|---|---|---|
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🟡 **LGPL-3.0** · 18 092 B · `2.12` · `cd1da68` | 🟢 **LATAM** (Brazil) | 🟢 **A real, large student information system** — self-described as Brazil's biggest free education software, in municipal use. 🔵 **This qualifies pass 87's claim that *"no permissive open-source SIS exists"*: none is permissive, but a substantial **linkable** one exists, and it is LATAM-origin.** The single best anchor for a Brazilian public-sector engagement. |
| [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | 🟡 **LGPL-3.0** · 8 241 B · `19.0` · `1c95cef` | 🔵 unplaced | LMS + SIS on one Odoo database — the ERP-shaped option. |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🟡 **LGPL-3.0** · 18 025 B · `develop` · `d9d462a` | **EMEA** (Luxembourg) | The serious QTI assessment platform. |

## Copyleft tier — build **beside**, integrate by LTI / SCORM / xAPI

Not inferior software. Several are the best in the industry. The constraint is on the *deliverable*, not the quality.

| platform | grant (payload · bytes · ref · SHA) | ★ | region |
|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** · `COPYING.txt` 35 147 B · `main` · `f205347` | — | 🟢 **APAC** (Moodle HQ, Perth, Australia) — the market leader is an Australian project, which matters for an APAC pitch |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** · 35 136 B · `master` · `2e46ebd` | — | **North America** (Axim Collaborative) |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** · 34 523 B · `release` · `2776223` | 1.1k | 🔵 unplaced — the Docker Open edX distribution, i.e. how Open edX actually gets deployed |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** · 34 520 B · `master` · `1c9f0bb` | — | **North America** (Instructure) |
| [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** · `license.txt` 33 893 B · `develop` · `933fc60` | 3.3k | **APAC** (India) — 🔴 **widely mis-listed as MIT; it is not** |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0** · 35 147 B · `master` · `f30df11` | 1.0k | 🟢 **EMEA** origin (Belgium/Spain), 🟢 **heavy LATAM install base** — the practical LATAM LMS incumbent |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL-3.0** · 35 147 B · `release_11` · `c212185` | 505 | **EMEA** (Germany) |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | 🔴 **AGPL-3.0** · 34 523 B · `dev` · `9a13191` | 2.3k | 🔵 unplaced |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 🔴 **AGPL-3.0** · 34 523 B · `main` · `c225cc4` | 1.7k | 🔵 unplaced |
| [`codelitdev/courselit`](https://github.com/codelitdev/courselit) | 🔴 **AGPL-3.0** · `LICENSE.md` 34 143 B · `main` · `62b5abb` | 1.3k | 🔵 unplaced |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **GPL-3.0** · 35 121 B · `v31.0.00` · `1d83c2b` | — | 🟡 **APAC** (Hong Kong lineage) — K-12 school platform |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL** · 15 214 B · `mobile` · `541c509` | — | 🟡 **LATAM** lineage (named for Rosario, Argentina) — SIS |

🔴 **No grant at all:** [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) · `master` · `5d546f2` —
**no licence payload in 17 candidate filenames.** Frequently listed as "GPL" in comparison articles. Unusable
until the publisher states a grant; do not put it in a client proposal.

## The decision rule

| the engagement needs… | use | because |
|---|---|---|
| the deliverable **closed and owned**, AI included | 🟢 **`Artemis` (MIT)** | permissive, production, already has the three AI subsystems |
| **EMEA public-sector sovereignty**, self-hosted, closable | 🟢 **`OpenOLAT` (Apache-2.0)** or `Artemis` | named European university deployments |
| **North American HE**, permissive, committee-friendly | 🟢 **`Sakai` (ECL-2.0)** | Apereo governance is a procurement asset, not just a licence |
| **lecture video** + transcription/captioning AI | 🟢 **`Opencast` (ECL-2.0)** | permissive at exactly the layer AI attaches to |
| **offline / low-connectivity** delivery | 🟢 **`Kolibri` (MIT)** | built for it; see `repos/foundations.md` |
| a **Brazilian public-sector SIS** | 🟡 **`i-educar` (LGPL-3.0)** | real municipal deployments; link, don't absorb |
| the client's **existing Moodle / Canvas / Open edX** kept | 🔴 build **beside** it, integrate via LTI 1.3 / SCORM / xAPI | GPL/AGPL reciprocity follows the modified work |

*Prior pass content is preserved in git history at commit `457eaba` and earlier.*
