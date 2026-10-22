---
industry: education
region: Global
updated: 2026-10-22
---

# Foundational repos for education

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/repos-foundations.md`](../archive/2026-10-22-p383-pre-rewrite/repos-foundations.md).
Every address verified first-hand on this date — method and channel notes in
[`agents/top.md`](../agents/top.md#verification-method), raw results in
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).

## 🔴 Read this before choosing a base: the licence frontier in education runs the wrong way

**The platform tier is copyleft. The agent tier is permissive.** That is the single most
consequential structural fact in this industry for a studio that needs to ship client-owned code:

| tier | licences actually found | what it means |
|---|---|---|
| **LMS / platform** | GPL-3.0 (Moodle, Chamilo, ILIAS, H5P), AGPL-3.0 (Open edX, Canvas, Tutor, Frappe LMS), ECL-2.0 (Sakai, Opencast), LGPL-3.0 (OpenEduCat) | Forking the platform pulls copyleft into the deliverable. AGPL additionally reaches **hosted** use. |
| **the one exception** | 🟢 **Apache-2.0 — [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT)** | The only major open-source LMS a studio can extend with closed code. Underweighted by every roundup we read. |
| **agents / tooling** | MIT, Apache-2.0, BSD-3 almost throughout | Permissive. |

🆕 `p385` **And a third axis the table above cannot show: the grant can differ by *ref* within one
repository.** [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) reads **AGPL-3.0** at
`main` (34,523 B) and **MIT** at tag **`v0.1.0`** (1,081 B) — both read first-hand this pass. It relicensed on
**2026-08-16**. 🔵 So "what is this repository licensed as?" is not a well-formed question; **"what is it
licensed as at the ref I am shipping?"** is. That is now **Pattern L step 10**, and it cuts both ways: a
permissive grant can be *retrievable at a tag* after the project has moved away from it, and a repository
a prior audit cleared as MIT can be AGPL at `main` today.

**The design consequence**, not a preference: compose permissive agents **over** a copyleft platform
across a documented interop boundary — **LTI 1.3**, **MCP**, or the platform's web-services API —
rather than forking the platform. Recipes in [`compose/patterns.md`](../compose/patterns.md).

## Tier 1 — Learning platforms

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | `main` | 🟡 **GPL-3.0** — 🔴 grant is in **`COPYING.txt`**, there is **no root `LICENSE`** | The install base. Moodle Pty Ltd reports 400M+ users and ~150,000 registered sites. Originates in Australia (APAC). Huge plugin catalogue, and now a first-party MCP path. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 `master` | 🔴 **AGPL-3.0** | The MOOC-scale platform: LTI 1.3, XBlocks, deep data control. Deploy via `tutor` below, not by hand. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 `master` | 🔴 **AGPL-3.0** | Dominant in North American higher ed. Open-**core**: the published tree is not the commercial ecosystem, so scope assumptions break on integration. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🔴 `master` | 🟢 **Apache-2.0** | Swiss, mature, permissive. The default recommendation whenever a client needs to own closed extensions to the LMS itself. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 `master` | 🟡 **GPL-3.0** | The LATAM/EMEA public-sector base. Strongest Spanish/Portuguese-language footing of any platform here. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🔴 `master` | 🟡 **ECL-2.0** | Apache-2.0-derived **Educational Community License** — permissive-shaped with an education-specific patent/attribution twist. Read it; do not assume Apache. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`release_11`** | 🟡 **GPL-3.0** | German public-sector LMS and the learning component of the openDesk sovereign stack. Default ref is a release branch. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **`release`** | 🔴 **AGPL-3.0** *(`LICENSE.txt`)* | The Docker distribution for Open edX and the de-facto deployment path. Nobody should be installing `edx-platform` without it. |
| [inducer/relate](https://github.com/inducer/relate) | `main` | 🟢 **MIT** *(`LICENSE`, 1,145 B — "MIT/X Consortium license")* | 🆕 `p384`. Django courseware with autograding, flexible access rules, per-student statistics and multi-course support. 🟢 **Permissive at the platform level**, which almost nothing else in this tier is. 🟡 Courseware-scale: the permissive base for a **course**, where OpenOLAT is the permissive base for an **institution**. Do not pitch it as a Moodle replacement. |

## Tier 2 — Content, courseware and assessment

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | 🔴 `develop` | 🟢 **Apache-2.0** | Structured interactive lessons with a real pedagogy engine (misconception-aware branching). Permissive, which is rare at this level of pedagogical depth. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🔴 `develop` | 🟢 **MIT** | Offline-first learning runtime for low-connectivity deployment. The single most important repo on this shelf for LATAM and African engagements. |
| [serlo/serlo.org](https://github.com/serlo/serlo.org) | `main` | 🟢 **Apache-2.0** | German open learning platform — permissive, EMEA-native, curriculum-aligned content model. |
| [openfun/richie](https://github.com/openfun/richie) | 🔴 `master` | 🟢 **MIT** | Course catalogue and portal front-end from France Université Numérique. Pairs with Open edX as the public face. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🔴 `master` | 🟡 **GPL-3.0** *(`LICENSE.txt`)* | Interactive content types embedded in nearly every LMS. 🔴 **Routinely described as MIT; it is not.** Keep H5P as *content* loaded at runtime, not as linked code. |
| [openedx/edx-ora2](https://github.com/openedx/edx-ora2) | 🔴 `master` | 🔴 **AGPL-3.0** | Open-response and peer assessment. 🔴 `edx/openassessment` and `openedx/openassessment` are both **DEAD** — this is the live address. |
| [opencast/opencast](https://github.com/opencast/opencast) | 🔴 `develop` | 🟡 **ECL-2.0** | Lecture capture and video pipeline. 🔴 `apereo/opencast` is **DEAD**; use this org. |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | 🔴 `master` | 🟢 **Apache-2.0** | Reference LTI 1.3 implementation from the standards body. **This is the copyleft firewall** — the boundary that lets permissive code talk to a GPL/AGPL platform without linking to it. |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | `main` | 🟡 **ODbL** *(`LICENSE`, 25,289 B; **no** separate code grant — `LICENSE-CODE`, `LICENSE.code`, `CODE_LICENSE`, `licenses/LICENSE` all 404)* | 🆕 `p384`. **The curriculum prerequisite graph**: `v1` ships **1,930 micro-topics** and **4,102 prerequisite edges** as a DAG (`hard`/`soft`, each edge carrying a reason) over **9 subjects**, aligned to NGSS, Common Core, the UK National Curriculum and the Australian curriculum. Data at `data/topics.json`, `data/dependencies.json`, `data/teaching-research.json` (~24 MB). 🔴 **A share-alike *database* licence, not a code licence** — grounding a tutor on it is a §4.3 *Produced Work* (attribution notice only); shipping an extended taxonomy is a §4.4 *Derivative Database* (share-alike). See **Pattern H**. 🟡 Maintainer-stated gap: teaching research covers **1,049** topics, **881 have none**. |

## Tier 3 — Grading, notebooks and the CS-teaching stack

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | `main` | 🟢 **BSD-3-Clause** | Multi-user notebook serving — the standard way a cohort gets identical compute. |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | `main` | 🟢 **BSD-3-Clause** | Release / collect / autograde / return. The assignment lifecycle, already solved. |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🔴 `master` | 🟢 **BSD-3-Clause** | Autograding at Berkeley cohort scale; container-isolated execution. |
| [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main` | 🟢 **MIT** | Pedagogical assessment of *how* code was written. The missing half of autograding. |

## Tier 4 — Measurement, memory and retrieval (what makes the agents honest)

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | `main` | 🟢 **MIT** *(`LICENSE.md`)* | The eval runner. Nothing in this industry should ship without a before/after on the client's own subject mix. |
| [hendrycks/test](https://github.com/hendrycks/test) | 🔴 `master` | 🟢 **MIT** | **MMLU** — 57 academic subjects. The subject-level breakdown is the useful part, not the headline score. |
| [openai/grade-school-math](https://github.com/openai/grade-school-math) | 🔴 `master` | 🟢 **MIT** | **GSM8K** — multi-step arithmetic reasoning; the canonical K-12 maths probe. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | `main` | 🟢 **MIT** | **FSRS** scheduler. A retention model with published parameters — the part of "personalisation" that is actually measurable. Note [ankitects/anki](https://github.com/ankitects/anki) itself is **AGPL-3.0**; the scheduler is the reusable piece. |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | `main` | 🟢 **Apache-2.0** | Document-aware RAG — handles the textbook/worksheet/PDF reality of course material. |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | `main` | 🟢 **Apache-2.0** *(`LICENSE.md`)* | Ingest for the formats education actually runs on: PDF, DOCX, PPTX, scans. |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | `main` | 🟢 **MIT** | Programmatic prompt optimisation — turns "we tuned the tutor prompt" into something with a metric attached. |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | `main` | 🟢 **MIT** | The campus LLM gateway universities actually deploy: multi-provider, SSO, per-user quota, audit. MIT where the obvious alternative is not (see [`agents/top.md`](../agents/top.md)). |

## Tier 5 — Student information / administration

| repo | default ref | licence | note |
|---|---|---|---|
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **`19.0`** | 🟡 **LGPL-3.0** | Odoo-based education ERP/SIS. Default ref is a **version branch**, `19.0` — there is no `main`. 🔴 `OpenEduCat/OpenEduCat` is **DEAD**; this is the live address. Its Brazil and Mexico country pages are vendor marketing — treat feature claims as unverified. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | `main` | 🟢 **MIT** | Laravel school-management platform with **Spanish and French built in**. SME-scale, not university-scale. The only permissive, Spanish-native administration platform found in this pass — relevant to the LATAM supply gap recorded in [`intel/market.md`](../intel/market.md). |
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 **`master`** | 🟡 **GPL-2.0** — 🔴 grant is at **`docs/License.txt`** (17,286 B), **not** at any root path; `index.php` and `Modules.php` headers pin *"version 2 of the License"* | 🆕 `p384`. The most widely deployed open-source SIS in the K-12 tier. GPL-2.0 is survivable the same way Moodle is — reach it over its API, do not link to it. 🔵 **This repo is why the licence probe set grew from seven paths to eight**: a root-only read returns "ungranted" for a repository with a perfectly standard grant one directory down. |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 `develop` | 🔴 **AGPL-3.0** — grant is in lowercase **`license.txt`** | Frappe/ERPNext-ecosystem LMS; attractive where the client already runs ERPNext. |

## 🔴 Dead addresses corrected this pass

Four addresses in common circulation do not resolve. Each has a live replacement:

| dead address | live replacement |
|---|---|
| `apereo/opencast` | [opencast/opencast](https://github.com/opencast/opencast) |
| `edx/openassessment` **and** `openedx/openassessment` | [openedx/edx-ora2](https://github.com/openedx/edx-ora2) |
| `OpenEduCat/OpenEduCat` | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) |

## 🔴 `p384` — an address that resolves but has no tree

[`projectfedena/fedena`](https://github.com/projectfedena/fedena) is listed by a vendor comparison
article as an **Apache-2.0** student information system. It is neither confirmed nor refutable from
a resolution check alone, which is the point:

| check | result |
|---|---|
| `git ls-remote --heads` | 🟢 **resolves** — two refs: `master`, `projectfedena-patch-1` |
| `master/README`, `README.md`, `LICENSE`, `Gemfile`, `app` | 🔴 **404, all five** |

🔵 **`ls-remote` proves a ref, not a tree.** The base's verification method pairs resolution with a
first-hand payload read precisely so this case is caught: there is no readable tree here to carry a
licence, so the Apache-2.0 claim is recorded as **unsubstantiated — nothing read**, not as a
licence of any kind. Any address census built on resolution alone over-counts the supply.

**Still absent from the supply, and it did not change this pass:** no platform is both an **LMS and
a SIS** under a permissive licence. The shape is permissive *courseware*
([`inducer/relate`](https://github.com/inducer/relate),
[`tutors-sdk/tutors`](https://github.com/tutors-sdk/tutors)), one permissive *major LMS*
([OpenOLAT](https://github.com/OpenOLAT/OpenOLAT), Apache-2.0), and copyleft everywhere else —
Moodle GPL-3, Open edX AGPL-3, Canvas CE AGPL-3, openSIS GPL-2.0, OpenEduCat LGPL-3. **Pairing two
bases is the only route**; the single permissive LMS+SIS does not exist to be found, and a pitch
that assumes it will be found is a pitch with a hole in it.

🆕 `p386` **— the claim survives a search aimed straight at it, and gains a third route.** The
prescribed ERP/CRM leg (`open source platform education ERP CRM MIT Apache 2026`) returned **no
permissive education platform**, which is this shelf's claim holding up under test rather than for
want of looking. What it did return is three **permissive general ERP/CRM bases**, licence payloads
read first-hand: [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) (🟢 **MIT**, 1,077 B,
default ref **`master`**, Laravel 13 + FilamentPHP 5 **with a plugin system**),
[krayin/laravel-crm](https://github.com/krayin/laravel-crm) (🟢 **MIT**, 1,078 B, default ref
**`2.2`**) and [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) (🟢 **Apache-2.0**,
11,906 B, default ref **`trunk`**). 🔵 So the pairing routes are now three, not two: copyleft
LMS + copyleft SIS, copyleft LMS + permissive courseware, or **copyleft LMS + a permissive ERP base
whose education modules you build**. The trade is written out on
[`verticals/solutions.md`](../verticals/solutions.md) — and none of the three bases ships an
education module, so the third route is a **build**, costed as one.
