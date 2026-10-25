---
industry: education
region: Global
updated: 2026-10-25
---

# 🏗️ Foundational repos — Education

> The bases worth starting from, with licences read from each repository's own payload at
> the HEAD SHA shown (2026-10-25). Permissive first — those are the ones Globant can build on.

## ✅ The permissive foundations — verified 2026-10-25

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | `d073ad444fe5` | `LICENSE` 10 982 B · `6dbc5b605ed0` | University-grade LMS and **the only Apache-2.0 platform in the tier**. The default base when the client needs a full LMS and cannot take copyleft. Badly under-used relative to its terms. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | `44a4e68aac3e` | `LICENSE` 1 097 B · `3c056b34a476` | Offline-first learning platform. The only MIT platform; the answer to connectivity and equity constraints (LATAM, rural APAC, Africa). |
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** | `c73c4bb42aa7` | `LICENSE.TXT` 11 358 B · `cfc7749b96f6` | Component SDK for Open edX. **The licence seam**: ship an Apache-2.0 AI component into an AGPL-3.0 platform without the platform's terms reaching your code. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `ccbaf37b07e3` | `LICENSE` 1 066 B · `f5f955194636` | Knowledge tracing (DKT/SAKT/BKT family, standard datasets). The measurement layer that makes an "adaptive" claim defensible rather than rhetorical. |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | **Apache-2.0** | `96f33faaf028` | `LICENSE` 11 357 B · `c71d239df917` | Minimal agent framework, EU-domiciled. The base for a bespoke tutor/grader when a full tutoring platform is too much. |
| [openfun/richie](https://github.com/openfun/richie) | **MIT** | `7cf513c235ee` | `LICENSE` 1 079 B · `e4b2a3148135` | Django/React course-portal CMS (France Université Numérique). The public-sector MOOC front-end. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL** (Apache-derived) | `4debc94780cc` | `LICENSE` 11 120 B · `0688f62d04f1` | Higher-ed consortium LMS. Permissive in practice — but record it as ECL-2.0, **not** Apache-2.0. |
| [Utdanningsdirektoratet/PAS2-Public](https://github.com/Utdanningsdirektoratet/PAS2-Public) | **Apache-2.0** | `489129c42c9d` | `LICENSE` 11 325 B · `cb5e8e7e5f4a` | 🆕 `p435`. **Norway's Directorate for Education (Udir) publishing the public code of its new exam and test administration services (PAS2)**, issue tracker and wiki open to the public. 🟢 A national assessment authority's own administration stack under a permissive grant — the single strongest EMEA public-sector row on this file, and the counterpart to Norway's own age-tiered AI restriction. Default branch is `master`. |
| [DFE-Digital/get-information-about-schools](https://github.com/DFE-Digital/get-information-about-schools) | **MIT** | `ad46faf42690` | `LICENCE` 1 116 B · `e18299fd1942` | 🆕 `p435`. England's **school registry** service (GIAS) — the authoritative establishment dataset behind every DfE service. 🔵 Note the grant is at `LICENCE`, the British spelling: a ladder that only tries `LICENSE` reports this UK government repository as ungranted. |
| [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | **MIT** | `a2d4f5fdec58` | `LICENSE` 1 092 B · `c561ea849ed6` | 🆕 `p435`. The DfE's national teaching job service (Rails + PostgreSQL + Redis), source **and** infrastructure definitions. The reference for a public-sector education service a client can read end to end. |
| [DFE-Digital/education-benchmarking-and-insights](https://github.com/DFE-Digital/education-benchmarking-and-insights) | **MIT** | `3cdbf2cbf47b` | `LICENSE` 1 091 B · `5a22fb5576a5` | 🆕 `p435`. **FBIT** — the DfE's school financial benchmarking and insights tool: compare resource use against similar schools, interrogate the financial data, support governor oversight. 🟢 The one row on this file that is a *finance* analytics surface over school data, which is where a UK trust-level engagement starts. |
| [oaknational/oak-curriculum-api](https://github.com/oaknational/oak-curriculum-api) | **MIT** | `0561df5aac12` | `LICENSE` 1 077 B · `0eeb9d32caed` | 🆕 `p435`. **Oak National Academy's** curriculum API — England's national-curriculum content as a documented, versioned OpenAPI surface. 🟡 `oaknational/oak-openapi` is the **same repository** (identical HEAD under `git ls-remote`, and the repo's own badges use that name); one row, two spellings, shelved once. |
| [instructure/ims-lti](https://github.com/instructure/ims-lti) | **MIT** | `724f1ae45315` | `LICENSE.txt` 1 068 B · `f7e95fbe6fa9` | 🆕 `p435`. **Instructure's own** Ruby IMS-LTI implementation — the Canvas vendor publishing the integration library under MIT. 🟢 The vendor-maintained half of the LTI layer that `Trend 19` says goes stale at the standards body and is carried by the vendor fork. |
| [hyunbinseo/neis-school-info](https://github.com/hyunbinseo/neis-school-info) | **MIT** | `5c9ecede5208` | `LICENSE` 1 068 B · `e82e1769aaaf` | 🆕 `p435`. TypeScript client for **NEIS**, Korea's national education information open-data portal (`open.neis.go.kr`) — school basic information. 🟢 The APAC analogue of GIAS above: a national school registry reachable from code. 🟡 The README warns the upstream dataset is not routinely reconciled, so treat records as reported, not current. |
| [krzysztofbury/librus-python-api](https://github.com/krzysztofbury/librus-python-api) | **MIT** | `fba65fe807eb` | `LICENSE` 1 071 B · `22e7ab2dbddc` | 🆕 `p435`. The independent Python client for **Librus Synergia** that `librus-mcp` (on `agents/top.md`) is built on — the library layer under the Polish gradebook connector. 🔵 Byte-identical MIT payload to the server, same copyright holder: one author, two addresses, no third-party-holder question. |

**15 verified permissive foundations** in the platform/agent tiers above. Each resolved under
`git ls-remote` and each licence was read from the repository's own payload. 🆕 `p435` adds the
**eight** above — the **public-authority** tier: a national assessment authority (Udir), three
UK Department for Education services, England's national-curriculum API, Korea's national school
registry client, the Canvas vendor's own LTI library and the client library under the Polish
gradebook connector. 🆕 `p431` adds a further **4** in **Tier 9 — the evaluation layer** below,
for **19** permissive foundations in all.

## 🔴 Copyleft foundations — usable, but integrate, do not vendor

| Repo | Licence | HEAD | Payload | Note |
|---|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | `46c042e7da65` | `COPYING.txt` 35 147 B · `8ceb4b9ee5ad` | Largest installed base and plugin ecosystem worldwide. Talk to it over its API. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | AGPL-3.0 | `87cd3811a425` | `LICENSE` 35 136 B · `e12d78569742` | Network copyleft. Use XBlock as the seam. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | `2e5139a816d3` | `LICENSE` 35 147 B · `8ceb4b9ee5ad` | Lightest self-host; strong LATAM footprint. |
| [exelearning/exelearning](https://github.com/exelearning/exelearning) | AGPL-3.0 | `c848eca0018d` | `LICENSE` 34 523 B · `0d96a4ff68ad` | Authoring tool led by Spain's Ministry of Education — state-backed EMEA credibility. |
| [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | `5d6df8e3ed8e` | `license.txt` 33 893 B · `db1a87ba81e8` | 🔴 Listed as MIT by several 2026 roundups. **That is wrong** — read at source. |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | `ec452b65043b` | `LICENSE` 7 652 B · `e3a994d82e64` | Virtual classroom. Link against it; don't fork. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | `46a5d7d40082` | `LICENSE` 8 241 B · `528f84036800` | LMS + SIS on Odoo — the closest thing to an education ERP. |

> Moodle and Chamilo ship a **byte-identical** GPL-3.0 payload (`8ceb4b9ee5ad`) — the stock
> FSF text. Recorded so a digest sweep does not misread the collision as a fork.


## 🆕 `p435` — The permissive foundation tier grew for the first time in six passes, and what grew it was a **census**, not a search

`p434`, `p433`, `p432` and the three before them all reported this tier unchanged. 🟢
**This pass added eight rows, and none came from a web search.** They came from grading the
2 450 unpromoted addresses this base already held (`Gap 434-A`, closed:
`compose/code/p435-promotion-sweep`, evidence in
`evidence/promotion-backlog-grants.2026-10-25-p435.tsv`).

### 🔴 The number that explains six passes of "unchanged"

| arm of the unpromoted backlog | n | share |
|---|---|---|
| **PERMISSIVE** (MIT 1 022 · Apache-2.0 330 · BSD/ISC/CC0/ECL/Unlicense 97) | **1 449** | **59.1 %** |
| `NO-GRANT` — 404 on all eight paths × two refs | 500 | 20.4 % |
| GPL / AGPL / LGPL family | 329 | 13.4 % |
| other / unrecognised | 172 | 7.0 % |
| **total probed** | **2 450** | 100 % |

🔴 **The permissive supply was never scarce — it was unexamined.** Six passes reported "no
growth" while 1 449 permissive addresses sat on the trend record ungraded. This also
sharpens `Trend 10` rather than refuting it: the permissive supply really is in the agent
and integration layers, and the **platform** tier is still almost entirely copyleft — what
changes is that the agent/integration layer turns out to be an order of magnitude larger
than this file's seven rows suggested.

### 🟢 What the eight rows have in common: a public authority wrote them

Udir's exam-administration services, three DfE services, Oak National Academy's curriculum
API, Korea's NEIS registry client — **state education bodies publishing their own
production code under MIT or Apache-2.0.** 🔵 That is a different kind of foundation from a
framework: it is the *schema and the service contract a national system already runs*, so a
build on top of it inherits the jurisdiction's own data model instead of inventing one.

### 🔵 And one ladder detail worth more than it looks

`DFE-Digital/get-information-about-schools` carries its grant at **`LICENCE`** — the
British spelling. `p228-shelf-gate`'s ladder tries it; a ladder that stops at `LICENSE`,
`LICENSE.md` and `LICENSE.txt` reports a UK government repository as **ungranted**. 🟢 The
ladder earns its eighth path here, on a real row, for the first time on these shelves.

### 🟡 The reach bound, stated as one

The recency channel (`head_dates.sh`) was run over the **permissive arm only**: 1 449
addresses dated, 0 failures. The 1 001 non-permissive rows carry `head_committed = -` in
the evidence file. 🔵 That is a deliberate bound, not a gap in the data — a stale AGPL row
is not more shelvable for being fresh.

## 🆕 `p434` — The permissive foundation tier is unchanged for a **fifth** pass, and this time the sweep says *why* with a number

`p434` promoted two permissive addresses to `agents/top.md`
([`wenflow-org/wenflow`](https://github.com/wenflow-org/wenflow), MIT, `LICENSE` 1 067 B ·
`b6fac57d4710`; [`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai), MIT,
`LICENSE` 1 067 B · `5731a2d3ccea`). 🔵 **Neither belongs on this file, for `p433`'s reason:**
both are agent-layer — a learning-path agent and an adaptive-tutoring *runtime seam*. They
compose onto a base; they are not one.

🔴 **The permissive foundation tier above is unchanged:** OpenOLAT (Apache-2.0), Kolibri (MIT),
XBlock (Apache-2.0), pykt-toolkit (MIT), smolagents (Apache-2.0). **Five rows, five passes, no
movement** — and `verticals/solutions.md` records the education-ERP sweep returning a **standing
nil for the third consecutive pass**.

🟢 **What is new is that the asymmetry `p433` described in prose now has a measured number.**
This pass graded the seven highest-traction addresses sitting unpromoted in the trending shelves
and **not one is a foundation, nor is one promotable**:

| ★ band | Addresses | Grants found | Foundations among them |
|---|---|---|---|
| ≥ 190 ★ | 5 | 🔴 3 × AGPL-3.0 · 1 × CC-BY-SA-4.0 · 1 × **no licence file** | **0** |
| < 100 ★ | 2 | 🟢 2 × MIT | **0** |

🔴 **So the asymmetry is sharper than "foundations move slowly".** In education's new supply,
**traction and permissiveness are anti-correlated** (`repos/trending.md`, `p434`): the biggest new
addresses are copyleft, content-licensed or ungranted, and the permissive ones are an order of
magnitude smaller — *and none of either kind is platform-shaped*. 🔵 **Pricing consequence,
unchanged in direction but now defensible with a count:** a proposal may assume it can adopt a
fresh permissive **agent**; it may not assume it can adopt a fresh permissive **platform**, and
it may not use stars as a proxy for adoptability at all. The highest-traction education address
this base has ever recorded is **4 771 ★ and CC-BY-SA-4.0**.

🟢 **Instrument added this pass**, and it is the reason this file can state the above as a
standing property rather than a pass observation: `compose/code/p434-promotion-gate`
(`make gate-promotion`, 28 offline controls, wired into `hooks`) fails whenever a **permissive**
address recorded in the trending shelves appears in **no** curated shelf. It was **red on its
first run** and is green after the two promotions, so this tier's completeness is now checked by
a gate instead of by a pass remembering to look.

## 🆕 `p433` — The permissive foundation tier did **not** grow, and that is the finding

`p433` promoted three permissive addresses into `agents/top.md` after first-hand payload reads —
[`learn-from-materials`](https://github.com/dmoshehun-prog/learn-from-materials) (MIT,
`LICENSE.md` 1 122 B · `15ce43afa44a`, **1 118 ★**),
[`PhysicsOS`](https://github.com/122-syf-wcy/PhysicsOS) (Apache-2.0, `LICENSE` 11 356 B ·
`f1a2e5fccede`) and
[`textbook-writer-skills`](https://github.com/cabbage2000-lab/textbook-writer-skills) (MIT,
`LICENSE` 1 064 B · `0d5a33d13ca9`). 🔵 **None of them belongs on this file**, and saying why is
the point: all three are **agents and skill packs**, not foundations. They compose *onto* a base;
they are not a base.

🔴 **The permissive foundation tier above is unchanged for the fourth consecutive pass:**
OpenOLAT (Apache-2.0), Kolibri (MIT), XBlock (Apache-2.0), pykt-toolkit (MIT), smolagents
(Apache-2.0). The `p433` ERP sweep (see `verticals/solutions.md`) independently confirms there is
**no MIT/Apache education ERP** to add, and the trending sweep returned no permissive platform.

🔵 **The asymmetry is worth naming for anyone sizing an engagement.** New permissive supply in this
industry arrives almost entirely as **agent-layer** work — small, fast-moving, APAC-origin, often
skill-pack shaped. The **foundation** layer moves on a scale of years and is majority copyleft.
A proposal that assumes it can pick a fresh permissive platform is mispriced; a proposal that
assumes it can pick a fresh permissive agent is usually right. `Trend 14` is the demand-side
reading of the same fact.

## 🆕 `p432` — Tier 10: the special-education / IEP layer, and why it is a tier of seeds

The surface North American law regulates hardest has the thinnest open-source supply measured
anywhere in this repository. These are the bases that exist, with grants read from each
repository's own payload at the HEAD shown (2026-10-25).

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [robotros/California-IEP-AI-project-kit](https://github.com/robotros/California-IEP-AI-project-kit) | **MIT** | `ff1ae0ce30e7` | `LICENSE` 1 064 B · `2524a8e74f10` | The **knowledge and boundary layer**. Two CA special-education roles as pinned knowledge packs with a declared draft-only / authorised-system-of-record boundary. Start an NA special-education engagement from this, not from a blank prompt. 🔴 Prose discipline, no runtime enforcement — adding that is the work. |
| [67tallchris/iep-builder](https://github.com/67tallchris/iep-builder) | **MIT** | `b39df0e9a4a1` | `LICENSE` 1 068 B · `523f156051cf` | The **deployment reference**: Svelte + Cloudflare Pages Functions + D1 with bring-your-own-key AI. Shows a per-district deployment that holds no vendor key and no central student store. Jurisdiction-pinned to Arizona K-8. |
| [dougdevitre/access-to-education](https://github.com/dougdevitre/access-to-education) | **MIT** | `f8abd70707ba` | `LICENSE` 1 068 B · `68657618a157` | The **parent-facing corpus**: 69 files / ~120 k words on IEP navigation, family–school communication and advocacy, under a code licence. The only MIT answer to the unserved-parent persona of `Trend 10`. |
| [ezixen/PlannedEducation](https://github.com/ezixen/PlannedEducation) | **MIT** | `06fb12159f5e` | `LICENSE` 1 085 B · `4ec3cc564448` | Adjacent, not special-ed specific: grading companion + secure test-taking, privacy-first self-host. Default branch `dev`. |
| [rwrife/rubric-desk](https://github.com/rwrife/rubric-desk) | **MIT** | `010a44006014` | `LICENSE` 1 062 B · `ec0b7dad19a4` | The **offline marking surface** (Flutter; phone/tablet/Windows, no accounts, no cloud LMS). Pairs with `kolibri` wherever connectivity cannot be assumed. 🟡 Created 2026-10-25. |

**5 permissive additions**, taking this file to **16 permissive foundations** in all.

🟡 **Adjacent but copyleft — integrate, do not vendor:**
[`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) is **AGPL-3.0-or-later**
(`LICENSE` 35 441 B · `d8d2ea7ef0a1` @ `6194e51e8f1f`, standard AGPLv3 body, SPDX header, no added
clauses) and is the only maintained accessibility-first differentiation engine found — UDL, WCAG,
AAC, text-to-speech, offline-first, i18n, commit on 2026-10-25. Network copyleft over a hosted
engine is the worst-case shape; reach it over an interface.

🔴 **Two addresses are excluded for cause, both proved by `git ls-tree -r` over the whole tree:**
[`grasped-dev/staircase`](https://github.com/grasped-dev/staircase) (@ `9236fce606c2`, 0 of 33 files)
and [`eakarsu/ai-special-education-iep-compliance`](https://github.com/eakarsu/ai-special-education-iep-compliance)
(@ `ec2516b76699`, 0 of 29 files) carry **no licence at all**. Between them they hold the tier's best
technique (a standards graph for goal reasoning) and its most complete-sounding product. Neither is
a base.

🔴 **The honest health warning on this entire tier.** Star counts are 0, 0, 1, 0 and 0. Two of the
five were created inside the eleven days before this pass. None has a second contributor. These are
**seeds to fork and own**, not dependencies to track — and that is a different commercial
conversation from the one `kolibri` or `OpenOLAT` supports. Said plainly to a client, it is also an
argument *for* the engagement rather than against it: there is no incumbent to displace.

🔴 **Declared gap:** the tier is entirely US. The sweep found **no** open-source tooling for
England's EHCP process or for the inclusive-education mandates of Brazil, Chile or Colombia — a nil
result, not a thin one.

---

## 🔴 Read this before choosing a base: the licence frontier in education runs the wrong way

**The platform tier is copyleft. The agent tier is permissive.** That is the single most
consequential structural fact in this industry for a studio that needs to ship client-owned code:

| tier | licences actually found | what it means |
|---|---|---|
| **LMS / platform** | GPL-3.0 (Moodle, Chamilo, ILIAS, H5P), AGPL-3.0 (Open edX, Canvas, Tutor, Frappe LMS), ECL-2.0 (Sakai, Opencast), LGPL-3.0 (OpenEduCat) | Forking the platform pulls copyleft into the deliverable. AGPL additionally reaches **hosted** use. |
| **the one exception** | 🟢 **Apache-2.0 — [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT)** | The only major open-source LMS a studio can extend with closed code. Underweighted by every roundup we read. |
| **agents / tooling** | MIT, Apache-2.0, BSD-3 almost throughout | Permissive. |

🆕 `p389` — **the "one exception" row is wrong, and the dating is what shows it.** There are **four**
permissive platform-tier bases on this shelf, not one, and the reason the claim survived this long is
that the other three were each filed as something narrower than a platform:

| permissive platform base | licence | last commit | the role it actually fills |
|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 🟢 **2026-10-22 (0 d)** | The permissive base for an **institution**. Swiss, mature, full LMS. |
| [Simon-Initiative/oli-torus](https://github.com/Simon-Initiative/oli-torus) | 🔴 `master` | 🟢 **MIT** *(`LICENSE.md`)* | 🆕 `p390`. 🟢 **The permissive courseware engine, and the gap it fills is a licence gap rather than a feature gap.** **Torus** is the authoring-and-delivery platform behind **Carnegie Mellon's Open Learning Initiative** — the group whose course-effectiveness studies are the most-cited evidence base in the field. Pages, structured activities, adaptive **scripted "advanced authoring"** activities, mastery/proficiency reporting per learning objective, LTI 1.3 delivery into a host LMS, and a research-grade analytics surface. 🟢 **Everything else at this scale is copyleft** (Open edX AGPL-3, Canvas AGPL-3, Moodle GPL-3) — so when a client needs to *ship a modified platform* rather than host one, this is the only row on this shelf that lets them. Elixir/Phoenix + PostgreSQL. Dated **2026-10-22** — committed today. 🔴 **Mind the slug:** `CMU-OpenLearning/oli-torus` does not resolve; the canonical owner is `Simon-Initiative`. 🟡 Elixir is a real staffing constraint for most studio teams — cost it before proposing it. |
| [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | 🟢 **2026-10-22 (0 d)** | The permissive base for **pedagogy**: misconception-aware branching lessons. Filed in *Tier 2* as content, but it is a platform. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 🟢 **2026-10-22 (0 d)** | The permissive base for **low-connectivity delivery**, and the only MIT one. Filed as a runtime; it is the platform in any engagement where bandwidth is the constraint. |
| [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT** | 🟢 **2026-10-21 (1 d)** | The permissive base for a **course**. |

🔵 **What to say instead of "the platform tier is copyleft."** *The platform tier is copyleft wherever
the install base is* — Moodle, Canvas, Open edX, Chamilo, ILIAS are where the clients already are, and
those are GPL/AGPL/ECL. **Permissive platform bases exist, are all actively maintained, and all cost you
the install base.** That is a trade a client can be walked through; "there is one exception" was not.
The design consequence below is unchanged and is still the default — it is the *greenfield* branch of
the decision that just got three more options.

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
| 🆕 `p393` [bmosoluciones/now-lms](https://github.com/bmosoluciones/now-lms) | `main` · `53dcb60` | 🟢 **Apache-2.0** *(10,915 B, `sha256`₁₆ `a9c4042d767d`)* | 🟢 **The permissive LMS this shelf did not have, and it is LATAM-native.** © 2021–2024 **BMO Moreno Berroteran Ortiz Soluciones, S.A. (Nicaragua)**. A complete Flask/Python LMS — courses, delivery, certificates, **monetisation** — at **676 files, 505 commits, 57 releases**, HEAD **2026-08-31 — 52 d**, PyPI `now-lms` v2.0.4, **21 ★**. 🔵 **Why it matters out of proportion to its stars:** every other platform on this tier is GPL (Moodle), AGPL (Open edX, Canvas) or LGPL, so `now-lms` is the **only Tier 1 row a studio can fork, extend and ship closed** — the licence frontier this file opens by describing, crossed at last. 🔴 The trade is scale: 21 ★ against Moodle's install base, and no multi-tenancy claim. Pilot and SME delivery, not a ministry. 🔵 Its non-stock Apache byte count is the **appendix FILLED IN**, not narrowed — `Pattern L` step 4's benign case, distinct from `Ed-Fi`'s absent appendix below. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 `master` | 🔴 **AGPL-3.0** | Dominant in North American higher ed. Open-**core**: the published tree is not the commercial ecosystem, so scope assumptions break on integration. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🔴 `master` | 🟢 **Apache-2.0** | Swiss, mature, permissive. The default recommendation whenever a client needs to own closed extensions to the LMS itself. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 `master` | 🟡 **GPL-3.0** | The LATAM/EMEA public-sector base. Strongest Spanish/Portuguese-language footing of any platform here. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🔴 `master` | 🟡 **ECL-2.0** | Apache-2.0-derived **Educational Community License** — permissive-shaped with an education-specific patent/attribution twist. Read it; do not assume Apache. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`release_11`** | 🟡 **GPL-3.0** | German public-sector LMS and the learning component of the openDesk sovereign stack. Default ref is a release branch. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **`release`** | 🔴 **AGPL-3.0** *(`LICENSE.txt`)* | The Docker distribution for Open edX and the de-facto deployment path. Nobody should be installing `edx-platform` without it. |
| [inducer/relate](https://github.com/inducer/relate) | `main` | 🟢 **MIT** *(`LICENSE`, 1,145 B — "MIT/X Consortium license")* | 🆕 `p384`. Django courseware with autograding, flexible access rules, per-student statistics and multi-course support. 🟢 **Permissive at the platform level**, which almost nothing else in this tier is. 🟡 Courseware-scale: the permissive base for a **course**, where OpenOLAT is the permissive base for an **institution**. Do not pitch it as a Moodle replacement. |
| [openedx/openedx-ai-extensions](https://github.com/openedx/openedx-ai-extensions) | `main` | 🔴 **AGPL-3.0-only** *(`LICENSE`, 34,523 B; `pyproject.toml` → `AGPL-3.0-only`)* | 🆕 `p387`. 🟢 **The platform's own AI extension point — read this before anyone proposes forking Open edX to add AI.** First-party `openedx` org, so the extension surface is maintained with the platform rather than against it; the grant matches the platform's, which is why it can exist inside it. 🟡 Marked **experimental, not for production** in its own docs, so treat it as the contract to build against, not the thing to ship. Compare [aulasneo/tutor-contrib-let](https://github.com/aulasneo/tutor-contrib-let) (`main`, AGPL-3.0, Aulasneo — Argentina) for the LATAM-maintained customisation route. |
| 🆕 `p408` [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | 🔴 `master` | 🟢 **MIT** *(`LICENSE`, 1,072 B, "Copyright (c) 2018 Project Sunbird")* | 🟢 **The counter-example to this file's opening thesis, and the largest one available: a permissive grant at NATIONAL-PLATFORM scale.** Sunbird ED is the building block **DIKSHA**, India's national school platform, is built on — so unlike every other permissive row here it comes with a ministry adopter rather than a pilot. 🔴 **The cost is maintenance, and it is large:** HEAD `9efc8b5` **2025-12-16 — 311 d**. Fork at a pinned SHA, run the client's CVE sweep before week 1 ends, and price a maintenance line; this is a fork-and-maintain base, not an integrate-and-extend one. 🔵 The exact inverse of Moodle's trade (current code, hostile grant) — see `Pattern AG`. 🔴 Sibling `Sunbird-Ed/sunbird-learning-platform` **resolves no ref** and must not be named in a deliverable; a failed resolve cannot distinguish private from deleted. |
| 🆕 `p408` [Sunbird-Ed/SunbirdEd-mobile-app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) | `main` | 🟢 **MIT** *(`LICENSE`, 1,078 B)* | The handset client for the row above, and the surface that matters wherever the learner's only device is a phone. 🔴 HEAD `9de5e08` **2025-09-19 — 399 d**, staler than the portal, so the mobile path carries the heavier maintenance share. 🔵 Pairs with [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT) rather than competing with it: Kolibri owns the offline-first runtime, this owns the DPI-aligned content contract. |

## Tier 2 — Content, courseware and assessment

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | 🔴 `develop` | 🟢 **Apache-2.0** | Structured interactive lessons with a real pedagogy engine (misconception-aware branching). Permissive, which is rare at this level of pedagogical depth. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🔴 `develop` | 🟢 **MIT** | Offline-first learning runtime for low-connectivity deployment. The single most important repo on this shelf for LATAM and African engagements. |
| [serlo/serlo.org](https://github.com/serlo/serlo.org) | `main` | 🟢 **Apache-2.0** | German open learning platform — permissive, EMEA-native, curriculum-aligned content model. 🔴 🆕 `p390` **Dated: last commit `2023-02-09` — 1,351 days.** Serlo the *service* is very much alive (`serlo.org` serves German schools daily); this *repository* is not where it is developed any more. Keep it as the **content-model reference** — the permissive, curriculum-aligned data shape is still the most useful thing here — but do not plan a fork or a dependency on it, and ask Serlo where the current code lives before quoting an EMEA-native platform base. |
| [openfun/richie](https://github.com/openfun/richie) | 🔴 `master` | 🟢 **MIT** | Course catalogue and portal front-end from France Université Numérique. Pairs with Open edX as the public face. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🔴 `master` | 🟡 **GPL-3.0** *(`LICENSE.txt`)* | Interactive content types embedded in nearly every LMS. 🔴 **Routinely described as MIT; it is not.** Keep H5P as *content* loaded at runtime, not as linked code. |
| [openedx/edx-ora2](https://github.com/openedx/edx-ora2) | 🔴 `master` | 🔴 **AGPL-3.0** | Open-response and peer assessment. 🔴 `edx/openassessment` and `openedx/openassessment` are both **DEAD** — this is the live address. |
| [opencast/opencast](https://github.com/opencast/opencast) | 🔴 `develop` | 🟡 **ECL-2.0** | Lecture capture and video pipeline. 🔴 `apereo/opencast` is **DEAD**; use this org. |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) 🆕 `p391` | `master` | 🟢 **Apache-2.0** *(`LICENSE.md`, 11,342 B; `composer.json` declares `"license": "Apache-2.0"`)* | 🟢 **THE LTI 1.3 DEPENDENCY TO INSTALL — and it corrects `p390`'s finding #1, which told three shelves there was none.** LTI 1.3 is *the* standards surface for putting an agent inside Moodle, Canvas, Blackboard or D2L, and this is a **live** implementation of it: HEAD `66d8e4e`, **2026-10-16 — 6 days**, shipping as packagist **`packbackbooks/lti-1p3-tool` v6.4.4, 68 versions, published 2026-09-23**. Same Apache-2.0 grant as the 1EdTech copy (byte-identical 11,342 B licence), under active maintenance. 🟢 It keeps the **copyleft-firewall** role intact: permissive code talks to a GPL/AGPL platform over the LTI boundary without linking to it. 🔵 Note the ref is **`master`**, not `main` — a `main`-assuming licence read fails silently. |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) 🆕 `p391` | `master` | 🟢 **Apache-2.0** *(11,360 B; `package.json` agrees)* | 🟢 **The Node LTI 1.3 route, and the better default for an agent stack.** HEAD `41f150c`, **2026-10-13 — 9 days**; npm **`ltijs` v7.0.7, 207 published versions, 2026-10-06** — the most actively released LTI implementation this base has read. A standalone LTI *tool* provider rather than a platform plugin, which is the shape an agent engagement actually needs: the agent is its own service, and the LMS launches into it. 🟢 Prefer this over the PHP line unless the client's platform work is already PHP (a Moodle plugin, an Open edX fork). |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | 🔴 `master` | 🟢 **Apache-2.0** | 🔴 **DEMOTED to a spec citation — do not install it.** Last commit `2020-06-03` — **2,333 days**, and `composer.json` carries no licence field. An unmaintained PHP library handling OAuth 2 / JWT signing and key rotation is a **security** dependency, not merely a compatibility one. 🟢 The architectural role it was shelved for is not lost: it moves to `packbackbooks/lti-1-3-php-library` (above), which is the maintained line. 🔴 🆕 `p391` **It also has an alias:** [`IMSGlobal/lti-1-3-php-library`](https://github.com/IMSGlobal/lti-1-3-php-library) returns the **identical HEAD sha `3a192de`** — an org rename, one project at two addresses. Counted **once**. |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) 🆕 `p391` | `master` | 🟡 **MIT** | 🔴 **The Python LTI route, and it is genuinely dead — which is an architecture constraint, not a shelf note.** Last commit `2022-11-21` — **1,431 days**; PyPI **`PyLTI1p3` 2.0.0, published 2022-11-20**, 29 releases, none since. 🔴 🆕 `p392` **And `p391`'s conclusion from this row is withdrawn.** It read *"so there is no maintained in-process Python LTI option: the edge must be `ltijs` (Node) or `packbackbooks` (PHP) fronting the Python agent over HTTP"*. `pylti1.3` is dead — that part is right — but **it is not the Python route**; it is one dead address on a road with three live ones (next three rows). `Gap 391-A` is **CLOSED**. |
| [academic-innovation/django-lti](https://github.com/academic-innovation/django-lti) 🆕 `p392` | `main` | 🟢 **MIT** *(1,098 B, "Copyright (c) 2022 The Regents of the University of Michigan"; PyPI classifier agrees)* | 🟢 **THE IN-PROCESS PYTHON LTI 1.3 ROUTE, AND IT IS THE ONE `Gap 391-A` SAID DID NOT EXIST.** A Django reusable app providing **LTI Advantage** — `pip install django-lti`, add `lti_tool` to `INSTALLED_APPS`, add `LtiLaunchMiddleware` after `SessionMiddleware`, migrate. That is the whole integration: **no second runtime, no sidecar, no HTTP hop**, which is the deployment component `p391` told three shelves and two patterns to budget for. HEAD `1ac0b56`, **2026-10-20 — 2 days**; PyPI **`django-lti` v0.10.1, 17 releases, 2026-08-07**; 264 commits, **26 ★**. 🟢 Maintained by the **University of Michigan Center for Academic Innovation** — an institutional maintainer in the region that buys the most LMS integration work. 🔴 Django-shaped: a FastAPI or Flask agent still needs the launch handled elsewhere, and there is **no release tagged on GitHub** (read PyPI for the version, not the Releases tab). |
| [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) 🆕 `p392` | `main` | 🟢 **BSD-3-Clause** *(1,528 B, "Copyright (c) 2016, Project Jupyter Contributors")* | 🟢 **The Python LTI route for the one surface where most CS and data-science teaching already happens.** Implements **both LTI 1.1 and LTI 1.3** authenticators for JupyterHub, so an LMS launch lands the student directly in a running notebook with their identity attached. HEAD `c0c3bf3`, **2026-07-01 — 113 days**; PyPI **`jupyterhub-ltiauthenticator` v1.6.3, 15 releases, 2026-03-26**; 523 commits, **73 ★**. 🟢 **This is what makes `Pattern B` whole** — `jupyterhub`, `nbgrader` and [jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) are already on these shelves, and this is the missing launch edge between them and the client's Moodle or Canvas. 🟡 113 days is slower than `django-lti`; for a Jupyter stack that is a feature, not a risk — but read it as a stable component, not an active one. |
| [openedx/xblock-lti-consumer](https://github.com/openedx/xblock-lti-consumer) 🆕 `p392` | 🔴 `master` | 🔴 **AGPL-3.0** *(34,520 B)* | 🔴 **The best-maintained Python LTI 1.3 implementation in any language — and it is off the permissive shelf.** HEAD `5ba9d16`, **2026-10-22 — committed today**; PyPI `lti-consumer-xblock` **v11.4.2**. Recorded as a **boundary, not a pick**: it is the *platform* side (Open edX consuming an external tool), and AGPL-3.0 reaches hosted use. 🔵 Its existence is why `Gap 391-A` should never have been written as a supply claim — the Python LTI supply was not thin, it was **licence-filtered**, and nobody had split those two readings. |
| [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) 🆕 `p392` | `main` | 🟢 **MIT** *(1,076 B)* | 🟢 **The serverless Node LTI 1.3 route — the shape `ltijs` cannot take.** *"Serverless-native LTI 1.3 toolkit for Node.js (Lambda, Workers, Hono)"*: a seven-package monorepo (`@lti-tool/core`, `hono`, `memory`, `dynamodb`, `postgresql`, `mysql`, `d1`) with **OIDC, Assignment and Grade Services, Names and Role Provisioning, Deep Linking and Dynamic Registration** all implemented, and the session store chosen at deploy time rather than assumed. HEAD `1fa0148`, **2026-10-20 — 2 days**; npm **`@lti-tool/core` v1.3.2, 2026-10-21**; 353 commits, **8 ★**. 🟢 Prefer it over `ltijs` when the deliverable is **Cloudflare Workers or Lambda**: `ltijs` assumes a long-running Node process with Mongo. 🔴 **8 ★ and no stated production claim** — the README's only such wording is a *"Production-ready security features"* heading, which is about the security section, not the project. Pilot it; do not put a ministry on it this quarter. |
| [mdestafadilah/proctoring.js](https://github.com/mdestafadilah/proctoring.js) 🆕 `p392` | `main` | 🟢 **MIT** *(1,069 B; `package.json` agrees)* | 🟢 **THE GRANTED PROCTORING COMPONENT `Gap 391-C` SAID DID NOT EXIST — and its privacy posture is the reason to shelve it rather than merely record it.** *"Zero-dependency browser proctoring toolkit: tab-switch, camera, face and audio monitoring with a single event API."* Detects tab switching, right-click, DevTools/view-source shortcuts, clipboard copy/cut/paste, camera state, **faces**, audio loudness, and **third-party capture software — virtual cameras, loopback audio, screen shares**. Face detection is `@vladmandic/face-api` 1.7.15 on TensorFlow.js/WebGL, **in the browser**. HEAD `c49b41c`, **2026-09-28 — 24 days**; npm **`proctoring.js` v0.5.1, 2026-09-24**; 46 commits, **1 ★**. 🟢 The README's claims are the sellable part, and they are unusually specific: *"No hidden network calls. Nothing leaves the page unless you set `backend.endpoint`"*; audio is analysed in memory and **discarded, never recorded**; the clipboard is **never read** (the event, the element and a character count only); screenshots are **off by default** and held in memory. 🔴 **1 ★, 46 commits, one maintainer** — vendor it, read it, own it; do not sell it as a maintained dependency. 🔴 By default it loads face-api **and its weights from jsDelivr at runtime** — a supply-chain and data-residency defect in any EU or public-sector deployment. **Self-host the weights**; the README says you can. 🔴 And the EU obligation does not transfer with the licence: *you* become the deployer of a high-risk Annex III system the moment this drives an exam decision. |
| [Scaler-Opensource/exam-guard](https://github.com/Scaler-Opensource/exam-guard) 🆕 `p392` | `main` | 🔴 **CONFLICT — Apache-2.0 in the payload, ISC in the manifest** *(`LICENSE` 11,356 B is the stock Apache-2.0 text; `package.json` at the same ref declares `"license": "ISC"`, and npm `@exam_guard/core` v10.1.0 declares ISC too)* | 🟡 **The bigger proctoring codebase, the weaker grant record, and the AI half is explicitly unbuilt.** *"AI Proctoring tool developed by Scaler"* — 398 commits, HEAD `d1193a6`, **2026-10-13 — 9 days**, npm **`@exam_guard/core` v10.1.0, 2026-10-13**, **3 ★**. What it actually ships is **browser lockdown and event telemetry**: blocks copy/paste/cut, right-click, text selection and keyboard shortcuts; detects `tabSwitch`, `browserBlur`, `rightClick`, `exitTab`, `copyPasteCut`, `restrictedKeyEvent`, `textSelection`, `fullScreen`; takes periodic page and webcam snapshots and POSTs events to an `eventsUrl` **you must build**. 🔴 **The README marks object detection, multiple-face detection and eye tracking *"(To be Done)"*** — so the "AI" in the name is a roadmap, not a dependency. 🔵 **Which is good news for a regulated deployment:** lockdown and event telemetry do no biometric inference, so this component is *not* the Annex III surface — the inference you add on top is. 🔴 Both readings of the grant are permissive and OSI-approved, so this is **publishable but ambiguous**; get the maintainer to reconcile the two files before a client depends on it (`gate-conflict`'s class). 🔵 [`aswanth9495/exam-guard`](https://github.com/aswanth9495/exam-guard) returns the **identical HEAD sha `d1193a6`** — one project at two addresses, counted **once**. |
| [Mcp-Brasil/mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil) 🆕 `p392` | `main` | 🟡 **MIT — CODE ONLY** *(1,069→1,072 B, "Copyright (c) 2025-2026 MCP Brasil"; `pyproject.toml` and the PyPI classifier agree — **and the README states the grant covers the code alone: each of the 70 data sources carries its own licence in `SOURCES.md`, under an `ACCEPTABLE_USE.md` policy**)* | 🟢 **THE LATAM ANALOGUE OF THE US DISTRICT-TARGETING INSTRUMENT — `Gap 391-B` closed for Brazil, 24 hours after it was opened.** An MCP server over **70 Brazilian public data sources**, 533 tools, **66 of them needing no API key**, with large datasets cached locally and queried through embedded DuckDB. The education ones are the point: **INEP `censo_escolar`** (the national school census — the per-school enrolment and infrastructure base a Brazilian pilot is scoped against) and **INEP `enem`** (the national exam microdata). HEAD `2efb258`, **2026-08-18 — 65 days**; PyPI **`mcp-brasil` v0.14.0, 18 releases, 2026-04-24**. 🟢 **Its LGPD handling is why this is shelvable and not merely findable.** `SOURCES.md` grades *Educação* **RISCO ALTO**, records that INEP withdrew microdata in 2022 under LGPD and resumed anonymised publication in 2024, states that the bundled snapshot is **2023, post-LGPD**, and documents a **code safeguard**: `COLUNAS_DISTINCT_PERMITIDAS` whitelists aggregate categories only (UF, sex, age band, race, school) and **does not expose** `NU_INSCRICAO`, name or CPF. 🔴 **Three limits to state in a proposal:** the data is a **2023 snapshot**, so currency is the risk and not the licence; the project's own note is to *validate a sample to confirm anonymisation*; and it is **explicitly not an official government service**. 🔴 A dating disagreement, published rather than resolved: this base's harvest row reads *"pushed 2026-10-20"* while `main`'s HEAD commit is **2026-08-18**. Two different signals — `pushed_at` spans every ref, a HEAD date does not. 🔵 This row is also `Gap 549` in the flesh: **a code grant and a data grant in one repository**, and this shelf's licence column was built for the first. |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | `main` | 🟡 **`(ODbL-1.0 AND CC-BY-SA-4.0)`** 🆕 `p390` *(exact SPDX expression, read from `package.json`; the tree carries **two** files — `LICENSE` (ODbL, 25,289 B) and `LICENSE-CONTENT`. There is still no separate permissive code grant.)* | 🆕 `p384`. **The curriculum prerequisite graph**: `v1` ships **1,930 micro-topics** and **4,102 prerequisite edges** as a DAG (`hard`/`soft`, each edge carrying a reason) over **9 subjects**, aligned to NGSS, Common Core, the UK National Curriculum and the Australian curriculum. Data at `data/topics.json`, `data/dependencies.json`, `data/teaching-research.json` (~24 MB). 🔴 **A share-alike *database* licence, not a code licence** — grounding a tutor on it is a §4.3 *Produced Work* (attribution notice only); shipping an extended taxonomy is a §4.4 *Derivative Database* (share-alike). See **Pattern H**. 🟡 Maintainer-stated gap: teaching research covers **1,049** topics, **881 have none**. 🔴 🆕 `p390` **The `CC-BY-SA-4.0` half is the one that reaches the client deliverable**: the *content* (topic prose, teaching research) is share-alike independently of the ODbL database right, so a curriculum document generated from it can inherit SA even where the DAG itself is only a Produced Work. Clear this with the client's legal team **before** it is a deliverable, not after. Dated `2026-10-22` — actively maintained. |
| [intellectif/learning-kit](https://github.com/intellectif/learning-kit) 🆕 `p391` | `main` | 🟢 **MIT** *(1,071 B; `package.json` agrees)* | 🟢 **A permissive, headless alternative to H5P — and the assessment component this shelf was thin on.** TypeScript-first SDK for interactive educational activities, described by its own README as *"a lightweight, composable, bring-your-own-backend alternative to H5P"*, for React 19. `@intellectif/lk-core` is the part that matters to a studio: **schemas, a pure scoring engine, rubric and deferred grading, assessment composition, attempt plans, redaction, and an xAPI statement builder — with zero runtime dependencies beyond Zod**. `@intellectif/lk-react` adds components and a resumable exam/review pager. 🟢 **Three properties that decide an engagement:** scoring is a *pure function* a client can unit-test and an auditor can read; **deferred grading** means a human marker stays in the loop by construction, which is the posture EU high-risk assessment obligations ask for; and **redaction** is in the core rather than bolted on. 🟢 Pairs directly with the xAPI/LRS rows on this shelf — it emits statements, it does not store them. HEAD `1e39e9e`, **2026-10-18 — 4 days**. 🔴 **It is deliberately not a CMS:** authoring UI, content storage, delivery, auth and the learner database are the consuming application's job. 🟡 The two packages' version numbers moved apart at 1.0, so a `lk-react` major is not by itself a breaking React API change — read its changelog. |

## Tier 3 — Grading, notebooks and the CS-teaching stack

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | `main` | 🟢 **BSD-3-Clause** | Multi-user notebook serving — the standard way a cohort gets identical compute. |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | `main` | 🟢 **BSD-3-Clause** | Release / collect / autograde / return. The assignment lifecycle, already solved. |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🔴 `master` | 🟢 **BSD-3-Clause** | Autograding at Berkeley cohort scale; container-isolated execution. |
| 🆕 `p393` [edulinq/autograder-py](https://github.com/edulinq/autograder-py) | `main` · `7984bd2` | 🟢 **MIT** *(1,071 B, `7eb48830c022`)* | The **submission and feedback** client for the edulinq autograding server — the half `nbgrader` and `otter-grader` leave to the institution. **49 releases**, 494 commits, HEAD **2026-10-02 — 20 d**, **16 ★**. 🔵 Pairs with `otter-grader` (grading) rather than competing with it. |
| [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main` | 🟢 **MIT** | Pedagogical assessment of *how* code was written. The missing half of autograding. 🔴 🆕 `p387`: **PyPI `pybryt` has had no release since v0.7.0 on 2022-04-28.** Keep it as the design it states, vendor the code, and do not sell a client a dependency that has not shipped in four and a half years. The maintained halves of this tier (`nbgrader`, `otter-grader`) are where the running infrastructure should sit. |
| 🆕 `p394` [rstudio/gradethis](https://github.com/rstudio/gradethis) | `main` · `48aaf89` | 🟢 **MIT** *(1,078 B, `48c18e68ffed`; `DESCRIPTION`: `MIT + file LICENSE`)* | **Automated feedback for student exercises**, from **Posit Software, PBC**. `grade_this_code()` compares against a model solution; `grade_this()` takes a predicate you write. HEAD **2026-06-18 — 126 d**, **164 ★**, 41 forks. 🟢 **The most-starred *maintained* autograder on this shelf and the most permissively licensed** — it edges `otter-grader` at 161 ★. 🔴 `okpy/ok` leads outright at **370 ★**, 532 d stale (`Gap 397-A`). 🔴 **Not a CRAN package** (`cran/gradethis` ABSENT), so install from GitHub or r-universe, not from CRAN. |
| 🆕 `p394` [rstudio/learnr](https://github.com/rstudio/learnr) | `main` · `e7164a8` | 🟢 **Apache-2.0** *(10,472 B, `60a581bccd57`)* | **Interactive tutorials in R Markdown** — the runtime `gradethis` grades inside; the two are a pair, not alternatives. **738 ★**, 241 forks. 🟡 HEAD **2025-11-13 — 343 d**: a stable substrate rather than an abandoned one, and the movement is in `gradethis`. |
| 🆕 `p394` [ucbds-infra/ottr](https://github.com/ucbds-infra/ottr) | 🔴 `master` · `693b3df` | 🟢 **BSD-3-Clause** *(1,555 B, `1677c5307530`; `DESCRIPTION`: `BSD_3_clause + file LICENSE`)* | **The R autograding extension for `otter-grader`** (row above), UC Berkeley Data Science Education Program — grades R scripts, Rmd documents and Jupyter notebooks with R kernels. HEAD **2026-07-06 — 108 d**. 🟢 So this tier's flagship autograder is permissive in **both** languages. 🔴 **3 ★**: the adoption sits on the Python parent, but this is the component an R course actually deploys. |
| 🆕 `p394` [cran/exams](https://github.com/cran/exams) | `master` · `baa3e28` | 🟡 **GPL-2 \| GPL-3** — 🔴 **disjunctive**, and 🔴 **no licence file at any tree path**: the grant is the `License:` field in `DESCRIPTION` | **R/exams v2.4-5**, Achim Zeileis (R-project). HEAD **2026-10-08 — 14 d**. 🟢 **The broadest assessment exporter on these shelves**: QTI 1.2, QTI 2.1, Moodle XML, Blackboard, Canvas, OpenOlat, ILIAS, TestVision, Particify, ARSnova, Kahoot!, Grasple, TCExam — read from the `R/` source filenames in the clone (`exams2qti21.R`, `exams2moodle.R`, `exams2canvas.R`, …), not from its prose. 🟢 **Plus NOPS**: a standardised PDF printed, scanned and marked automatically — the only offline assessment loop in this base. 🔵 Belongs with **Tier 8** as much as here; it is the generator the standards layer consumes. |
| 🆕 `p394` [philchalmers/mirt](https://github.com/philchalmers/mirt) | `main` · `e37f14c` | 🟡 **GPL (>= 3)** — 🔴 **`DESCRIPTION` only; GitHub's sidebar shows no licence** | **Multidimensional item response theory** — the canonical IRT engine, v1.48.2. HEAD **2026-10-21 — 1 DAY**, **235 ★**, 88 forks. 🔵 This shelf's Tier 4 carries `adaptive-knowledge-graph` (IRT + BKT, ~350 ★) and `OATutor` (BKT) as the adaptive layer; **`mirt` is the thing those approximate**, and it is committed daily. Sibling [`cran/catR`](https://github.com/cran/catR) (🟡 GPL >= 3, v3.17) is the **computerized adaptive testing** engine, [`cran/TAM`](https://github.com/cran/TAM) (🟡 GPL >= 2, v4.3-25) the test-analysis modules, and [`patriciamar/ShinyItemAnalysis`](https://github.com/patriciamar/ShinyItemAnalysis) (🟡 GPL-3, **47 ★**) the non-programmer front end. |

🔴 **The licence line through this tier runs between DELIVERY and MEASUREMENT, and `p394` found it by
accident.** The three components that *run the teaching loop* are permissive — `gradethis` MIT,
`learnr` Apache-2.0, `ottr` BSD-3-Clause — and every component that *measures the learner* is GPL:
`exams`, `mirt`, `catR`, `TAM`, `ShinyItemAnalysis`. 🟢 **That is a workable boundary rather than a
blocker**, because it falls exactly where a studio's product boundary falls anyway: embed the tutoring
and grading loop, reach the psychometrics **over a process boundary**, the same discipline `Pattern A`
and `Pattern O` already apply to copyleft LMSs. 🔴 **But `cran/exams`'s grant is disjunctive — GPL-2
*or* GPL-3 at the licensee's choice — and that choice must be recorded once, deliberately**, because
downstream compatibility differs between the two rungs.

🔴 **A provenance warning this tier needs and the others do not.** `cran/exams`, `mirt`,
`ShinyItemAnalysis`, `cran/catR` and `cran/TAM` have **no licence-shaped file at any path in their
trees** — enumerated, not guessed. GitHub's sidebar therefore shows **no licence** for all five, and a
reviewer who checks the sidebar will report five granted GPL packages as unlicensed. The authoritative
grant is the `License:` field in `DESCRIPTION`, which is what CRAN itself enforces. 🔵 Registered as
**`Gap 394-B`**, because this base already knows the rule — `p1052` carries `DESCRIPTION` in its
manifest list with a test asserting *"CRAN: the grant lives in DESCRIPTION and must be read
verbatim"* — and `licence-grant-gate`, the instrument that produces the verdicts, does not.

## Tier 4 — Measurement, memory and retrieval (what makes the agents honest)

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | `main` | 🟢 **MIT** *(`LICENSE.md`)* | The eval runner. Nothing in this industry should ship without a before/after on the client's own subject mix. |
| [hendrycks/test](https://github.com/hendrycks/test) | 🔴 `master` | 🟢 **MIT** | **MMLU** — 57 academic subjects. The subject-level breakdown is the useful part, not the headline score. |
| [openai/grade-school-math](https://github.com/openai/grade-school-math) | 🔴 `master` | 🟢 **MIT** | **GSM8K** — multi-step arithmetic reasoning; the canonical K-12 maths probe. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | `main` | 🟢 **MIT** | **FSRS** scheduler. A retention model with published parameters — the part of "personalisation" that is actually measurable. Note [ankitects/anki](https://github.com/ankitects/anki) itself is **AGPL-3.0**; the scheduler is the reusable piece. |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | `main` | 🟢 **Apache-2.0** | Document-aware RAG — handles the textbook/worksheet/PDF reality of course material. |
| [livekit/agents](https://github.com/livekit/agents) | `main` | 🟢 **Apache-2.0** | 🆕 `p390`. 🟢 **The realtime voice substrate — the piece a spoken tutor should never write itself.** Full-duplex STT → LLM → TTS pipelines with **turn detection, interruption handling and barge-in**, the three things that separate a tutor a child will talk to from a demo. Provider-agnostic on all three legs, so the ASR can be swapped for a local model where data residency demands it. This is what `Manu` (Tier 4, [`agents/top.md`](../agents/top.md)) is built on, and why that project is ~15 days old and already has a working voice loop. Dated **2026-10-22**. See 🆕 `Pattern V`. |
| [mozilla/common-voice](https://github.com/mozilla/common-voice) | `main` | 🟡 **MPL-2.0** *(code; the **corpora** are **CC0-1.0**)* | 🆕 `p390`. 🟢 **The licence answer to regional-language speech.** Crowd-sourced, CC0 speech corpora across ~130 language variants — including **pt-BR, es-419 variants, Kiswahili, Hindi and Bengali** — which is the fine-tuning and ASR-evaluation data a voice tutor needs outside English. 🟢 **CC0 on the data is the strongest possible position**: no attribution, no share-alike, usable in a commercial deliverable. 🟡 MPL-2.0 is weak file-level copyleft and applies to the **platform code**, not the corpora — do not conflate the two when quoting. Dated **2026-10-21**. |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | `main` | 🟢 **Apache-2.0** *(`LICENSE.md`)* | Ingest for the formats education actually runs on: PDF, DOCX, PPTX, scans. |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | `main` | 🟢 **MIT** | Programmatic prompt optimisation — turns "we tuned the tutor prompt" into something with a metric attached. |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | `main` | 🟢 **MIT** | The campus LLM gateway universities actually deploy: multi-provider, SSO, per-user quota, audit. MIT where the obvious alternative is not (see [`agents/top.md`](../agents/top.md)). |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | 🔴 `master` | 🟢 **MIT** | 🆕 `p389`. **Bayesian Knowledge Tracing, fitted from the client's own interaction logs** — and the maintained answer to a gap this base has carried for two passes. `Pattern B` stands on [microsoft/pybryt](https://github.com/microsoft/pybryt), whose published artefact has had **no release since 2022-04**; this is a *different* job (mastery estimation, not approach assessment) but it is the piece that makes "adaptive" a number instead of an adjective. 🟢 **Last commit 2026-10-21 (1 d)**, from UC Berkeley's CAHLR, who also maintain [`OATutor`](https://github.com/CAHLR/OATutor) (MIT) on [`agents/top.md`](../agents/top.md). 🟢 Per-skill learn/guess/slip/forget parameters are inspectable and defensible — which is what a district's procurement rubric asks for when it asks how the system decides a student is behind. |
| [docling-project/docling](https://github.com/docling-project/docling) | `main` | 🟢 **MIT** | 🆕 `p389`. **Course-material ingest, MIT, and committed today (0 d).** Layout-aware parsing of PDF, DOCX, PPTX, XLSX, HTML and images into a structured document model, with table structure and reading order preserved — which is the difference between a tutor that can cite page 7's table and one that cannot. 🟢 Chosen over [allenai/olmocr](https://github.com/allenai/olmocr) (Apache-2.0) **on the date**: olmocr's last commit is **2026-03-25, 211 days**. 🟢 Complements, not replaces, [`unstructured`](https://github.com/Unstructured-IO/unstructured) — docling is the stronger reader for textbook-shaped PDFs, `unstructured` has the wider connector set. |
| [jupyterlite/jupyterlite](https://github.com/jupyterlite/jupyterlite) | `main` | 🟢 **BSD-3-Clause** | 🆕 `p389`. **Jupyter with no server: the kernel runs in the browser via WebAssembly.** Last commit 2026-10-16 (6 d). 🟢 Two education problems it solves outright: a CS or data-science exercise that needs **no per-student compute, no container and no install** (the cost line that kills notebook teaching at scale), and a **lab that works offline once the page is cached** — the `Pattern D` constraint, met without shipping a server. 🟡 No server means no server-side autograding: pair it with [`nbgrader`](https://github.com/jupyter/nbgrader) on a submitted notebook rather than expecting it to assess in place. |
| [pipeworx-io/mcp-education-data](https://github.com/pipeworx-io/mcp-education-data) 🆕 `p391` | `main` | 🟢 **MIT** *(1,069 B; `package.json` agrees)* | 🟢 **The first row on these shelves that answers *which district*, rather than *what to build* — engagement targeting and funding data, not a classroom capability.** Four MCP tools over **keyless US federal data**: `education_find_schools` (NCES Common Core of Data via the Urban Institute — enrolment, charter/magnet status, grade range, free/reduced-price lunch counts), `education_find_districts` (LEA id, schools, enrolment, teacher counts), **`education_district_finance`** (revenue split **federal / state / local** and expenditure by function, with computed **per-pupil spending**) and **`education_child_poverty`** (Census SAIPE estimates of 5–17-year-olds in poverty — **the figures that drive federal Title I funding**). 🟢 **Why a studio cares:** a North America pitch can be priced against a named district's actual per-pupil budget and Title I eligibility before the first call. 🔴 **Three caveats that belong in the row:** it is an **unofficial** integration, not affiliated with the upstream provider; the default path is a **hosted gateway** (`gateway.pipeworx.io`), so a district deployment means self-hosting or accepting a third party in the data path — the data is public, but the *query pattern* may not be something a client wants off-premises; and a scoped endpoint also lists **~30 shared gateway meta-tools**, so the real context cost is far above four tools. 🟡 The finance survey **lags the directory data by 1–2 years** — never quote per-pupil spend as current-year. HEAD `060371b`, **2026-10-21 — 1 day**. |

## Tier 5 — Student information / administration

| repo | default ref | licence | note |
|---|---|---|---|
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **`19.0`** | 🟡 **LGPL-3.0** | Odoo-based education ERP/SIS. Default ref is a **version branch**, `19.0` — there is no `main`. 🔴 `OpenEduCat/OpenEduCat` is **DEAD**; this is the live address. Its Brazil and Mexico country pages are vendor marketing — treat feature claims as unverified. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | `main` | 🟢 **MIT** | Laravel school-management platform with **Spanish and French built in**. SME-scale, not university-scale. The only permissive, Spanish-native administration platform found in this pass — relevant to the LATAM supply gap recorded in [`intel/market.md`](../intel/market.md). |
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 **`master`** | 🟡 **GPL-2.0** — 🔴 grant is at **`docs/License.txt`** (17,286 B), **not** at any root path; `index.php` and `Modules.php` headers pin *"version 2 of the License"* | 🆕 `p384`. The most widely deployed open-source SIS in the K-12 tier. GPL-2.0 is survivable the same way Moodle is — reach it over its API, do not link to it. 🔵 **This repo is why the licence probe set grew from seven paths to eight**: a root-only read returns "ungranted" for a repository with a perfectly standard grant one directory down. |
| 🆕 `p393` [edanalytics/edfi_api_client](https://github.com/edanalytics/edfi_api_client) | `main` · `6b13cb9` | 🟢 **Apache-2.0** *(11,357 B, `c71d239df917` — 🔵 **STOCK**, this pass's reference byte count)* | 🟢 **The North American K-12 data path, and the first Ed-Fi row on these shelves.** Ed-Fi is the dominant US K-12 **data standard** (state longitudinal systems, district warehouses); this is a maintained Python client for its API — paging, auth, swagger introspection, async pulls. HEAD **2026-10-06 — 16 d**, 79 commits, PyPI v0.4.1, **15 ★**. 🔵 For a North America engagement this is the **roster-and-outcomes join** that `Gap 391-B`'s district instrument needs, and it is Apache-2.0. |
| 🆕 `p393` [Ed-Fi-Exchange-OSS/LMS-Toolkit](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit) | `main` · `b1266b7` | 🟢 **Apache-2.0** *(10,141 B, `cc4d4de0920b` — 🔴 non-stock: the **APPENDIX IS ABSENT**)* | 🔴 **ARCHIVED BY ITS OWNER ON 2025-03-10 — READ-ONLY.** Extractors for **Canvas, Google Classroom and Schoology** into Ed-Fi, plus a harmonizer: 763 files, 451 commits, PyPI `edfi-lms-harmonizer` v1.2.2. 🔵 Published **because** it is archived: it is the best available map of the LMS→Ed-Fi field mappings, and a studio should **read it and port it**, never depend on it. An archived upstream takes no security patch. 🔴 This is the state the licence column cannot show — `Gap 393-E`. |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 `develop` | 🔴 **AGPL-3.0** — grant is in lowercase **`license.txt`** | Frappe/ERPNext-ecosystem LMS; attractive where the client already runs ERPNext. |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **`2.12`** | 🟡 **GPL-2.0-or-later** *(`2.12/LICENSE`, 18,092 B; `composer.json` → `GPL-2.0-or-later`)* | 🆕 `p387`. 🟢 **Brazil's largest free education software, and the SIS a LATAM public-sector engagement will actually meet** — *"o maior software livre educacional do Brasil"*, municipal-scale student records, enrolment, grades. 🔴 **Its real default ref is `2.12`** — a version branch, neither `main` nor `master`: resolved with `git ls-remote --symref` (HEAD `7903a3e`). A `main`-assuming clone or licence read fails or reads the wrong tree, and a `master`-assuming one reads a branch that is not HEAD. 🟡 GPL-2.0 at the platform, so reach it over its API and keep the agent a separate service (`Pattern O`). Sibling `portabilis/i-diario` is AGPL-3.0 — the grant is a per-repository fact, not an organisation-wide one. |

## 🆕 `p387` — Tier 6: the multi-tenant AI layer, which is the thing `p386`'s tenancy gap was asking for

`p386` replaced a licensing gap with a **tenancy** gap: every granted LMS MCP server authenticates
as the signed-in student, so *"a studio cannot deliver one of those to an institution."* On Moodle
the tenancy layer already exists, it is maintained by a state education authority, and this base
has never shelved it.

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager) | `main` | 🟡 **GPL-3.0-or-later — granted in the source headers** (`version.php`), no root licence file | 🟢 **A multi-tenant AI backend for Moodle, explicitly offered as the alternative to Moodle 4.5's own single-tenant AI subsystem.** Two subplugin types — `aitool` (connect ChatGPT, Gemini, Dall-E, **Ollama**…) and `aipurpose` (bind a *purpose* to a tool **per role**) — plus per-role rate limits, per-tenant user enable/disable, usage monitoring, teacher visibility of student prompts (capability-gated), and tenant-handling hooks. Release **5.1.1**, version code **2026102305**. 🟢 This is the component that turns "an agent talks to the LMS" into "an institution can deploy it": the **sovereign EMEA option in `Pattern E`**, from Bavaria's state school platform, with a local-model path via the Ollama tool. 🔵 **Cite this address.** The `mebis-lp` organisation serves the same repository at `mebis-lp/moodle-local_ai_manager`, which this base's alias register already records as **STALE** (canonical: `bycs-lp/moodle-local_ai_manager`, resolved `p350`, confirmed `p370`) — 🆕 `p387` re-confirms it mechanically: `git ls-remote --symref` returns the **identical HEAD sha `4ff5a87`** at both, and `version.php` the identical component, release **5.1.1** and version code **2026102305**, which upgrades `p226`'s sibling-set inference from *weak* to an identity read. One repository, one row. |
| [bycs-lp/moodle-block_ai_chat](https://github.com/bycs-lp/moodle-block_ai_chat) | `main` | 🟡 **GPL-3.0-or-later** in `version.php` | The chat frontend that consumes the manager's API. 🔵 Cited at the canonical org, as above; the manager's own README links the sibling set under `mebis-lp` — `tiny_ai`, `block_ai_control` — and both orgs answer, so resolve the ref before you pin one. The family also includes [marcusgreen/moodle-qtype_aitext](https://github.com/marcusgreen/moodle-qtype_aitext) (AI-marked question type, `main`, resolved this pass). **Deploy the manager first, then pick frontends** — not the other way round. |

🔵 **Second instance of `Pattern L` step 8, and it is now a Moodle-wide rule, not an anecdote.**
`p386` found [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp)
granted **only** in `version.php`. Both plugins above are the same: **no root licence file, a full
GPL-3.0-or-later header in `version.php`.** For a Moodle plugin that is the convention Moodle
requires, so *"no `LICENSE` file"* on a Moodle plugin means **read `version.php`**, never
"ungranted".

## 🆕 `p388` — Tier 7: the integration layer, reordered by maintenance rather than by tool count

`p387` dated this shelf and found its richest LMS integration was also its stalest. **This pass found
the replacements**, via a channel nobody here had asked: `registry.npmjs.org/-/v1/search` is open and
**indexes by relevance while reporting publish history**, so "does this exist?" and "is it
maintained?" are answered in one call. 29 education queries → 383 addresses absent from this base →
**22 granted**. Full method in [`repos/trending.md`](trending.md).

| repo | default ref · HEAD | licence | why it is foundational |
|---|---|---|---|
| [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | `main` · `34e6156` | 🟢 **MIT** (1,070 B) | 🟢 **The maintained teacher/admin Canvas surface, and the new default for an institutional engagement.** 187 tools: grade, comment, rubrics, New Quizzes (LTI), gradebook *history*, enrollments, accounts, analytics, outcomes, grading standards, content exports/migrations, quiz **accommodations**, appointment groups — plus **link audit**, **accessibility audit** and **grade projection**, three deployment modes (stdio, HTTP, library import) and a one-click `.mcpb`. 🟢 **It ships a FERPA mode** — the first time compliance appears as a *product feature* on these shelves rather than a caveat in this base's prose. `canvas-lms-mcp` **v2.9.0 across 87 releases, 2026-04-13 → 2026-10-22 (today)**: the most actively published LMS integration here. |
| [Fireiscoolsolo/canvas-lms-mcp-local](https://github.com/Fireiscoolsolo/canvas-lms-mcp-local) · [`-server`](https://github.com/Fireiscoolsolo/canvas-lms-mcp-server) | `main` · `c7e5725` / `8e424f1` | 🟢 **MIT** (1,091 B, both) | The **student-side** Canvas surface, 209 tools, shipped as a deliberate pair: **Local Edition** (stdio, *no port opened, nothing exposed*) and **Remote Edition** (ngrok, OAuth 2.1, multi-computer failover). Distinctive part is grade *intelligence* rather than grade retrieval: `what_if_grade`, `compute_needed_score`, `grade_impact_ranking`, `study_priority_ranking`, `semester_snapshot`, plus full `.imscc` export. 🔴 Remote Edition opens a **public HTTPS address** — a school's decision, never a default. |
| [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` · `971d58f` | 🟢 **MIT** (1,067 B) | 🟢 **The first SIS-side integration on this shelf, and it opens the parent/guardian persona.** 20 tools over **Campus Parent** — schedule, assignments, grades, attendance *events with codes*, behavior, food service, documents, standardized assessment scores, fees, messaging from three sources — with linked districts auto-discovered via **CUPS SSO** and `FeatureDisabled`-awareness so it degrades per district. **47 releases**, → 2026-10-19. 🔵 Every SIS on this shelf until now was a *platform to deploy* (openSIS, i-educar); this is a *surface to read*. |
| [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` · `428b78b` | 🟢 **MIT** (1,067 B) | The parent-observer scope over Canvas: 18 tools, `canvas_list_observees` as the hinge. 🟢 Download path is hardened in a way worth copying — host-pinned to the Canvas origin, confined to a download directory, never writes through a symlink, new files `0600`. **43 releases**, → 2026-10-16. |
| [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) | `main` · `139bb11` | 🟢 **BSD-3-Clause** (1,532 B) | 🟢 **The live replacement for this shelf's most-depended-on stale artefact.** `Pattern B` rested on `pybryt`, last published **2022-04-28**. This is maintained (**v0.3.2, 7 releases, → 2026-09-25**) and from **QuantStack**, a known Jupyter-ecosystem maintainer. Per-cell **Explain Code** sends source, kernel language, **the traceback**, and preceding cells as the exercise statement; the tutor persona lives in a **`TUTOR.md` found by walking up from the notebook**, so it is per-course and version-controlled; `reference_solution` and `evaluation_criteria` ride in cell metadata, **ROT13-encoded** to keep them from the student. |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | `main` · `687c55b` | 🟢 **MIT** (1,070 B) | 🟢 **The North American curriculum-data layer** — the third region to acquire one. 12 tools over the whole **BC Ministry of Education K–12 curriculum** in its real three-column **KDU** structure with elaborations, Core Competencies, grade progressions, cross-subject connections, full-text search, and the **First Peoples Principles of Learning**. Hosted HTTP *or* local stdio. 🟡 2 releases, both **2026-03-27**, and the data is a crawl of `curriculum.gov.bc.ca` — **currency is the risk here, not the licence**. |
| [danieltyukov/tudelft-mcp](https://github.com/danieltyukov/tudelft-mcp) | `main` · `3c680e0` | 🟢 **MIT** (1,070 B) | 🟢 **The EMEA institution-shaped integration, and the governance reference on this shelf.** One server spanning **Brightspace + OSIRIS (official records) + MyTimetable + the public Study Guide** behind a single browser sign-in **including MFA**, session self-renewing. 🟢 **Every write action shows a preview and requires confirmation** — the human-oversight control EU high-risk obligations ask for, implemented as the default rather than documented as advice. |
| [Ryfter/canvas-toolchain](https://github.com/Ryfter/canvas-toolchain) | `main` · `ac0c75f` | 🟢 **MIT** (1,063 B) | Teacher-facing **semester refresh**: reads a Canvas backup archive plus lecture transcripts, **scores topic currency**, plans the next semester, emits Canvas-safe HTML. 🟢 The **no-token path is first-class** — generate the HTML, paste it in — so it delivers before anyone grants API access, which is how a pilot actually begins. |
| [gafapa/moodlia-cli](https://github.com/gafapa/moodlia-cli) | `main` · `7962e49` | 🟡 **GPL-3.0** (284 B short notice) | Node client and CLI for Moodle Core web services **plus the MoodlIA plugin — a 250-operation contract**, Moodle 4.5+, with an optional experimental **WebMCP** browser path. 🔵 A far wider surface than `webservice_mcp`, and GPL is survivable the same way: reached over REST/JSON-RPC, never linked. |
| [SuperPiTT/moodle-rag](https://github.com/SuperPiTT/moodle-rag) | `main` · `a333415` | 🟢 **MIT** (1,094 B) | 🔵 **Not a teaching tool — a build-cost tool, which is why it is on a foundations shelf.** RAG over a **Moodle codebase** for developers: semantic code search, 7 agents, 9 slash commands, all local. `Pattern A`'s real cost is Moodle plugin work; this is aimed at exactly that. 🟡 v1.0.0, single publish 2025-10-12. |

🔵 **How to read this tier against Tier 1–6.** Those tiers are **systems to deploy**; this one is
**surfaces to read and write**. A studio picks one platform base from Tier 1 and then one integration
row here *per persona* — and the personas are no longer two. Teacher/admin (`bruchris`), student
(`Fireiscoolsolo`), parent/guardian (`chrischall`) are three distinct tool surfaces over the *same*
institutional data, and **the tool counts are scope, not quality**: 187 vs 209 vs 20 reflects who is
being served, not which is better built.

🔴 **The maintenance rule this tier is sorted by, stated so it survives the next pass.** `p387`
established that **recency replaces popularity** here, because no star channel is open. `p388` adds
the corollary: **where two integrations cover the same surface, prefer the one still publishing** —
`canvas-mcp-server` (54 tools, last shipped 2025-06-27) is now dominated on both axes by a 187-tool
server that published today. Tool count and maintenance pointed in opposite directions for one pass;
they no longer do.

🔴 **And a supply category this shelf could not previously name: published-but-unreadable.** Six
addresses from the same sweep **publish to npm from a repository that prompts for credentials** —
the dependency is installable, its provenance is not auditable. The costliest is
[thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit) (**103
published versions**, manifest MIT, SCORM support), and the most instructive is
[ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit), whose manifest reads
**`"SEE LICENSE IN LICENSE"`** — pointing at a file in a repository nobody can read. 🔵 `Pattern L`
clears a repository by reading its subtree; **there is no subtree here to read**, so these cannot be
cleared that way. For an npm-only dependency the rule is: **the manifest is a claim, the tarball is
the evidence** — and `registry.npmjs.org/<pkg>/-/<pkg>-<v>.tgz` serves that tarball even when the
repository is closed. Full table and the Santillana case in
[`agents/top.md`](../agents/top.md#-no-licence-file--and-ungranted-is-three-different-things).

## 🆕 `p393` — Tier 8: the 1EdTech standards layer, which is where Python's education supply actually is

`p388` opened Tier 7 with a channel nobody had asked (npm search). This tier exists because `p393`
opened the **other** channel — `pypi.org/simple/`, PEP 691, **920,784 names in 45 MB in 1.4 s** — and
what came back was not more MCP servers but the **interoperability plumbing**: LTI, QTI, OneRoster,
Caliper, Ed-Fi. 🔵 **Read that as a sourcing rule, not a curiosity:** the integration layer is written
in Python and the agent layer is written in TypeScript, so a sweep of one registry answers only half
the question — and this base answered it with npm alone for eleven passes.

| repo | default ref · HEAD | licence (payload) | why it is foundational |
|---|---|---|---|
| 🆕 `p393` [openfun/django-lti-toolbox](https://github.com/openfun/django-lti-toolbox) | 🔴 `master` · `22c6f2f` | 🟢 **MIT** *(1,078 B, `504c17f9869b`)* | **The fourth Python LTI 1.3 implementation**, from **Open FUN — France Université Numérique**, the French state's higher-education platform operator. A Django app for building LTI **Tool Providers**. PyPI v2.0.0, 7 releases, 53 files, **14 ★**. 🔴 **HEAD 2024-11-14 — 707 days.** Granted and architecturally useful; **cold**. Read it for its shape, pick `django-lti` to ship. |
| 🆕 `p393` [Harvard-University-iCommons/django-lti-dynamic-registration](https://github.com/Harvard-University-iCommons/django-lti-dynamic-registration) | `main` · `2873d2f` | 🟢 **MIT** *(1,100 B, `1ade29a33914`)* | **The fifth**, and the only one covering **LTI Dynamic Registration** — the flow that lets a tool be installed in an LMS without a human exchanging keys. An explicit add-on to `academic-innovation/django-lti`, so it **composes with** `Pattern B`'s pick rather than replacing it. 🔴 HEAD **2025-09-15 — 402 days**, 19 commits, **3 ★**: a small, single-purpose, cold component — vendor it and own it. |
| 🆕 `p393` [vosslab/qti_package_maker](https://github.com/vosslab/qti_package_maker) | `main` · `e22fc04` | 🟡 **LGPL-3.0** *(7,652 B, `e3a994d82e64`, at **`LICENSE.LGPL-3.0`**)* | **Writes QTI** assessment packages for **Canvas and Blackboard** from plain question banks — the export half of an assessment pipeline. 381 commits, HEAD **2026-10-12 — 10 d**, PyPI `qti-package-maker` v26.7.14, **4 ★**. 🔴 **This base first published this row as UNGRANTED and was wrong**: a six-name licence-filename probe missed `LICENSE.LGPL-3.0`. Corrected by enumerating the tree. 🟡 **LGPL, so library-linking is fine and modification is not**: use it as a dependency, do not fork it into a product. |
| 🆕 `p393` [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) | `main` · `7a7ec60` | 🔴 **GPL-3.0** *(35,196 B, `f93eb1d94904`)* | **Converts QTI 2.x → 3.0 and 3.0 → 2.1** — items, tests, stimuli and content packages — from **Citolab**, the lab of **Cito, the Dutch national assessment institute**. The migration nobody else here supplies, and QTI 3.0 is the version procurement is starting to demand in EMEA. 🔴 **GPL-3.0: off the permissive shelf.** Run it as a **batch tool at arm's length** (a container invoked by a pipeline), never linked into delivered code. 🔵 Its TypeScript sibling [`Citolab/qti-convert`](https://github.com/Citolab/qti-convert) serves the **byte-identical** payload — so here the grant is **org-shaped, not language-shaped**, the exact complement of `Gap 391-A`'s lesson. |
| 🆕 `p393` `superbuilders/timeback-dev-python` *(🔴 unlinked deliberately — an absent address may not be linked from a live shelf: `gate-dead-citation` I2)* | 🔴 **does not resolve** — 🔵 and `p371`/`p372` already recorded it `NO-REMOTE`; what is new is that it is the declared source of **147 live releases** | 🔴 **UNAUDITABLE — MIT declared on PyPI, no payload obtainable** | The declared source of **three** live PyPI packages — `timeback-qti`, `timeback-oneroster` (OneRoster **v1.2**), `timeback-caliper` — **147 releases** between them, last **2026-07-18**: on paper the most complete 1EdTech client family in Python. 🔴 **The repository does not resolve for an unauthenticated clone, so the MIT claim cannot be checked even in principle.** `Gap 393-B`. 🔵 **The procurement line to say out loud:** a studio may evaluate these in a sandbox; it may not **warrant** them to a client, because warranting a licence means having read it. If the roster/QTI client is needed and granted, build on `oneroster`-shaped code you can read, or ask the publisher to open the repository. |

🔵 **What this tier changes about how this base searches.** `Gap 392-C` was right that the language
bias of a discovery channel becomes a supply claim — and the correction is not "also sweep PyPI once".
It is that **a supply question needs one channel per ecosystem**, and this base can now name its set:
`registry.npmjs.org/-/v1/search` (npm, relevance + publish history), `pypi.org/simple/` (PyPI, the
whole name space), `packagist.org/search.json` (PHP — open, measured by `p392`, **0 shelvable**), and
`raw.githubusercontent.com` + `git ls-remote` for first-hand verification of whatever any of them
returns. 🔴 **Still missing: Maven, NuGet, RubyGems and CRAN** — and `R` matters here, because
`otter-grader` grades R and the statistics-teaching stack is CRAN-shaped.

## 🆕 `p431` — Tier 9: the evaluation layer, which is what makes every other tier's claim checkable

Every tier above supplies something that **does** tutoring, grading or delivery. None of them
supplies anything that says whether the tutoring was any **good**. `Trend 8` has carried that as an
open measurement gap for many passes. Measured first-hand on 2026-10-25, the layer exists:

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | **Apache-2.0** (code) | `f9d69c7ce3e1` | `LICENSE` 11 358 B · `cfc7749b96f6` | Scenario-based evaluation **and regression** engine. Diagnoses a concrete pedagogical failure and keeps the evidence to re-test it after the fix. The CI gate for a tutoring deliverable. **Maintained** — commit 2026-10-25. |
| [Teachable-AI-Lab/tutor_gym](https://github.com/Teachable-AI-Lab/tutor_gym) | **MIT** | `772f5cdca5dd` | `LICENSE` 1 099 B · `8a0a4ba421a0` | Runs a model as tutor **and** as simulated student across existing ITSs (`ctat`, `apprentice`, `oatutor`). The acceptance-test fixture. 🟡 Stale since 2025-09-10 — fork it. |
| [DannyWeitekamp/tutorenvs](https://github.com/DannyWeitekamp/tutorenvs) | **MIT** | `eacba91d2b6b` | `LICENSE` 1 064 B · `eb1ef5e1a637` | `tutor_gym`'s upstream. Relevant only if the fork diverges; recorded for lineage. |
| [Teachable-AI-Lab/tutorenv](https://github.com/Teachable-AI-Lab/tutorenv) | **MIT** | `b90a4d01f2f1` | `LICENSE` 1 064 B · `eb1ef5e1a637` | Lineage root. Payload **byte-identical** to the row above — same grant, re-attributed at the fork. |

**4 verified permissive rows, bringing this file to 11 permissive foundations.**

🟢 **The composition that comes free.** `tutor_gym`'s `oatutor` backend binds to
[`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT), already on this shelf, and `pykt-toolkit`
(MIT) already supplies knowledge tracing. **Tutor → measurement → evaluation is now MIT end to end**,
which is the first time this base can price an *evidence* deliverable without a licence caveat.

🔴 **What this tier does NOT cover, and it is the regulated half.** Every address above scores
**tutoring** — dialogue, hinting, diagnosis. **Nothing found scores grading.** The only grading-side
candidate measured, [`sdrangan/llmgrader`](https://github.com/sdrangan/llmgrader), is
**non-commercial** (see `agents/top.md`). NA, EMEA and APAC statutes all bite hardest on
**assessment**, so the surface with the most regulatory exposure is the one with no open harness.
Tracked as **`Gap 431-C`**.

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
