---
industry: education
region: Global
updated: 2026-10-16
---

## Pass 239 — 2026-10-16 — THE US K-12 **DISTRICT DATA LAYER** IS THE VERTICAL PLATFORM THIS SHELF NEVER NAMED: `Ed-Fi` IS AN `Apache-2.0` STANDARD *PLUS* A REFERENCE IMPLEMENTATION *PLUS* A CERTIFICATION PROGRAMME, AND `OneRoster` IS THE SEAM BETWEEN IT AND EVERY LMS ALREADY ON THIS SHELF

🟢 **`14` new permissive rows place a whole platform tier.** 🔴 **The mandated platform query was NOT re-run this pass** — `p238` ran it and got `OpenEduCat` again without a licence; this pass spent its budget on the tier above the LMS instead, and says so rather than implying coverage.

🔵 **Evidence:** [`p239-verified-rows`](../evidence/p239-verified-rows.2026-10-16-p239.tsv) · [`p239-withheld`](../evidence/p239-withheld.2026-10-16-p239.tsv)

### 🟢 The tier this shelf was missing

This shelf carries LMSs *(`Moodle`, `Chamilo`, `Canvas`)* and SISs, and recommends customising them. 🔴 **What it never carried is the layer a US district actually integrates AT: the data standard between the SIS and everything else.**

| platform | grant *(read first-hand)* | region basis | what it is, and the customisation seam |
|---|---|---|---|
| **Ed-Fi ODS/API** — [`Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) *(carried)* + 🆕 [`Ed-Fi-Extensions`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Extensions), 🆕 [`Ed-Fi-Databases`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Databases) | 🟢 **`Apache-2.0`** — `10 172` / `10 173` B | 🟢 **North America** — Ed-Fi Alliance, US non-profit | 🟢 **An operational data store + REST API with a PUBLISHED EXTENSION MECHANISM.** `Ed-Fi-Extensions` is the sanctioned plugin path — 🔵 **the Odoo-module equivalent for a district data store**, and the right place to attach AI rather than forking the ODS |
| **Ed-Fi Data Management Service** — [`Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) *(carried)* + 🆕 [`Ed-Fi-Kafka-Connect`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Kafka-Connect) | 🟢 **`Apache-2.0`** — `11 357` B | 🟢 **North America** | 🟢 **The successor platform, and it has a Kafka seam** — so district events can be consumed as a stream instead of polled. 🟡 `12`★ / `17` forks: new, and the forks outnumber the stars |
| **Ed-Fi model toolchain** — 🆕 [`MetaEd-js`](https://github.com/Ed-Fi-Alliance-OSS/MetaEd-js) + 🆕 [`vscode-metaed-ide`](https://github.com/Ed-Fi-Alliance-OSS/vscode-metaed-ide) | 🟢 **`Apache-2.0`** — `10 173` B | 🟢 **North America** | 🟢 **The data model is GENERATED from a DSL, and the DSL toolchain is permissive** — an extension is authored, not hand-patched |
| **OneRoster 1.2 bridge** — [`edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) *(carried, `6`★)* | 🟢 **`Apache-2.0`** — `10 173` B | 🟢 **North America** | 🔵 **The seam between Ed-Fi and the LMS tier this shelf already carries** — serves a 1EdTech OneRoster API out of an Ed-Fi ODS. 🔴 **`6`★ carrying `13` recipe sites, as [`repos/foundations.md`](../repos/foundations.md) already flags** |
| **Ed-Fi load pipeline** — 🆕 [`edanalytics/lightbeam`](https://github.com/edanalytics/lightbeam) | 🟢 **`Apache-2.0`** — `11 349` B | 🟢 **North America** — Education Analytics, US | Validates and transmits JSONL into an Ed-Fi API. 🟢 **`12`★ and third-party — evidence the API is integrated against, not just published** |
| **SIS clients** — 🆕 [`PowerSchool-API`](https://github.com/aydenp/PowerSchool-API) `34`★, 🆕 [`PyPowerSchool`](https://github.com/dougpenny/PyPowerSchool) `16`★, 🆕 [`ic_parent_api`](https://github.com/schwartzpub/ic_parent_api) `9`★ | 🟢 **`MIT`** — `1 072` / `1 082` / `1 073` B | 🟢 **NA by target system** — PowerSchool and Infinite Campus are US K-12 SISs | 🟡 **Where a district's data actually lives.** 🔴 **Read the grant per client: the highest-starred Infinite Campus client is `GPL` and a third has no licence at all** |
| **Rostering/SSO** — 🆕 [`Clever/clever-go`](https://github.com/Clever/clever-go) | 🟢 **`Apache-2.0`** — `10 757` B | 🟢 **North America** — Clever Inc., US | Go client for the Clever rostering API. 🟡 Sibling `clever-js` *(`24`★)* **archived `2022`** |
| **LMS analytics** — 🆕 [`Ed-Fi-Exchange-OSS/LMS-Toolkit`](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit) | 🟢 **`Apache-2.0`** — `10 141` B | 🟢 **North America** | 🔴 **ARCHIVED `2025-03-10`**, `11`★ / `12` forks. 🟢 **Permissive and frozen — per `p236`, forking is the cheaper and less encumbered path** |

### 🔴 What a studio must NOT pick up from this tier

| repository | ★ | 🔴 grant | why it matters here |
|---|---|---|---|
| [`edanalytics/edu_wh`](https://github.com/edanalytics/edu_wh) | **19** | 🔴 **`PolyForm Noncommercial 1.0.0`** | 🔴 **The obvious companion to the Ed-Fi ODS — *"dbt package for EDU's Ed-Fi data warehouse"* — and the FIRST thing a studio would reach for. A studio engagement is commercial** |
| [`edanalytics/edu_edfi_source`](https://github.com/edanalytics/edu_edfi_source) | 10 | 🔴 **`PolyForm Noncommercial 1.0.0`** | Same; `dbt` package for raw Ed-Fi data |
| [`tonyzimbinski/infinite-campus`](https://github.com/tonyzimbinski/infinite-campus) | **34** | 🔴 **`GPL`** | The most visible Infinite Campus client |
| [`sas-fossdev/saspes`](https://github.com/sas-fossdev/saspes) | 13 | 🔴 **`AGPL-3.0`** | PowerSchool browser extension |

🔵 **`edanalytics` is the trap worth naming on this shelf: the same owner's [`DPS-Ed-Fi-ODS`](https://github.com/edanalytics/DPS-Ed-Fi-ODS) is carried as `Apache-2.0` and cited as evidence the Ed-Fi grant is exercised. One owner, both grants, and the noncommercial ones are the analytics layer a client would most want.**

### 🔴 Stated gaps

- 🔴 **The mandated platform query (`open source platform education ERP CRM MIT Apache`) was NOT run this pass.** `p238`'s result stands unchanged: `OpenEduCat` *(`LGPL-3.0` per its own site)*, `Kuali`, `openSIS`, none `MIT`/`Apache` confirmed by that channel.
- 🔴 **This whole tier is North America.** 🟡 **`ACTION VO`: the EMEA and APAC equivalents are unidentified on this shelf — the UK's `UK Register of Learning Providers`/`LRS` tier, EMEA `xAPI`/`SCORM` stacks and APAC national SIS standards have never been harvested. An informed gap, not coverage.**
- 🟡 **No row in this tier has been RUN.** The grants, heads and extension seams are read; nothing is deployed. `ACTION VB` *(run a compliance scanner over a carried repository)* remains open and now has a natural target in `Ed-Fi-Extensions`.

## Pass 238 — 2026-10-16 — THE MANDATED PLATFORM QUERY RETURNED `OpenEduCat` AGAIN AND STILL COULD NOT STATE A LICENCE; MEANWHILE A REPOSITORY NAMED **`Moodle-Full-Version-Unlocked`** PASSES EVERY AUTOMATED LICENCE CHECK ON THIS SHELF

🟢 **`3` new LATAM public-data platform rows.** 🔴 **`1` impersonation of a platform this shelf recommends on nine files.** 🟡 **The mandated platform query reproduced p237's result exactly.**

🔵 **Evidence:** [`p238-licence-filter-lure-farm`](../evidence/p238-licence-filter-lure-farm.2026-10-16-p238.tsv) · [`p238-queries`](../evidence/p238-queries.2026-10-16-p238.tsv)

### 🔴 `T238-E` — the recommendation shelf is now an attack surface, and that is new here

This shelf recommends `Moodle` across nine files. 🔴 **A repository called [`rockstar49summer/Moodle-Full-Version-Unlocked`](https://github.com/rockstar49summer/Moodle-Full-Version-Unlocked) exists, carries `license: MIT`, serves a `LICENSE` at `HTTP 200`, was pushed `2026-10-16`, and funnels every link to one download host.** Its `README` was read first-hand at `11 604` B: *"Reviewed by the senior review board · Senior Software Analyst · Verified against the official source"*, with **licence badges served as remote images from the funnel host** rather than from the repository.

🔵 **Why that matters on a VERTICALS shelf specifically: this file's output is a shortlist a client procures from.** A shortlist naming `Moodle`, handed to someone who then searches GitHub for it with a licence filter, now has a decoy sitting next to the real thing. 🟡 **The real project is [`moodle/moodle`](https://github.com/moodle/moodle) — `GPL-3.0`, and `P973` on this shelf already records that its `5.0` tree moved the licence out of the root.**

🟢 **The same cohort impersonates `PRONOTE`** *(the French school platform)*, **`CmapTools`, `Stellarium`, `Childsplay`, `Complete Anatomy`, `Packet Tracer`, `Adobe Presenter`, `GeoEnZo`, `WordFox`, `CubeTest`, `DiagramPainter`** — and **`Google Classroom`**, seven weeks after `p236` dated Classroom's shutdown to `2026-08-28`. 🔵 **Eleven of the thirteen were recorded from the listing page, not read; stated as a limit — `ACTION UZ`.**

🟢 **The gate is four predicates and no model, and it is `P238-1` in [`compose/patterns.md`](../compose/patterns.md).**

### 🟡 The mandated platform query, reproduced

`open source platform education ERP CRM MIT Apache student information system` returned, for the second pass running: **`OpenEduCat`** *(whose own site states `LGPL-3.0` — the weak-copyleft third answer p237 added a column for)*, **Kuali**, and **openSIS** *(a SourceForge page with no licence statement)*. 🔴 **The query names `MIT` and `Apache` and the channel returned neither.** 🔵 Consistent with p237's first-hand `LGPL-3.0` read of `OpenEduCat`, so this is a reproduction, not a new finding.

### 🟢 New tier: LATAM national-data platforms, `3` rows

🔵 **Why they belong here rather than on `repos/foundations.md` alone: a customisable platform is only half a vertical solution — the other half is the national data it has to be loaded with, and for LATAM engagements that data has not been on this shelf at all.**

| platform | grant *(read first-hand)* | ★ | head | scope |
|---|---|---|---|---|
| [`cortega26/chile-hub`](https://github.com/cortega26/chile-hub) | 🟢 **`MIT`** — `1 070` B, © 2026 Carlos Ortega | **129** | `main` · `605482f` | Chilean public data **curated, normalised and validated** — geography, demography, economy. 🟢 The validation step is what distinguishes it from a dump |
| [`manusabbath-arch/mcp-uruguay`](https://github.com/manusabbath-arch/mcp-uruguay) | 🟢 **`MIT`** — `1 070` B, © 2026 Manu Martinez | 0 | `main` · `d4c4d0f` | Uruguayan and regional public data over **MCP** — `BCU`, `INDEC`, `IBGE`, `ANCAP`, `INIA`. 🔵 `INDEC` and `IBGE` make it Argentina- and Brazil-reaching too |
| [`Angelthebestone/Normativa-colombiana-MCP`](https://github.com/Angelthebestone/Normativa-colombiana-MCP) | 🟢 **`MIT`** — `1 068` B, © 2026 Angel Peña | 3 | `main` · `cdab134` | Colombian norms and jurisprudence over MCP — the regulatory limb of a LATAM governance engagement |

🔴 **All three are NATIONAL, not education-specific.** Stated so a later pass does not read them as education platforms. 🟡 **`ACTION VD`: no equivalent exists on these shelves for Mexico, Peru or Argentina as a single curated hub.**

### 🔴 What this shelf still cannot answer

- 🔴 **Not one platform row on this shelf has been checked against the lure signature.** 🟡 **`ACTION VE`: run `P238-1`'s four predicates over every slug this shelf recommends, and record the result — including the zero, if it is zero.**
- 🟡 **`OpenEduCat`'s `LGPL-3.0` is still a site claim plus p237's read; the Odoo dependency underneath it carries its own licensing** and that chain is unmeasured here.

## Pass 237 — 2026-10-16 — THE MANDATED PLATFORM QUERY NAMED `OpenEduCat` AND COULD NOT STATE ITS LICENCE; THIS PASS READ IT, AND IT IS **`LGPL-3.0`** — WEAK COPYLEFT, WHICH IS A THIRD ANSWER THIS SHELF HAD NO COLUMN FOR

🟢 **`5` new platform rows, `1` published licence correction, and the largest of the new rows is `6` years dormant and said so before it was shelved.**

🔵 **Evidence:** [`p237-verified-rows`](../evidence/p237-verified-rows.2026-10-16-p237.tsv) · [`p237-rest-licence-channel`](../evidence/p237-rest-licence-channel.2026-10-16-p237.tsv)

### 🟢 `V237-1` — `OpenEduCat`, read at the grant rather than described

The mandated query `"open source platform education ERP CRM MIT Apache"` named **OpenEduCat** *(the education module set on Odoo)* and **Apache OFBiz**, and its own summary said it **could not confirm OpenEduCat's licence**. 🟢 **So this pass read it:**

| platform | grant, read first-hand | head | what it means for a studio |
|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 **`LGPL-3.0`** — `LICENSE` at branch `19.0`; the file's own first line is *"For copyright information, please see the COPYRIGHT file"*, and the text is the **GNU LESSER** General Public License v3 | `19.0` · `46a5d7d` | 🟡 **Weak copyleft, which is neither of the two answers this shelf has been giving.** You may build and ship **separate modules** against it without relicensing your own code; you may **not** fork `openeducat_erp` itself into a closed product. 🔵 **For an Odoo-shaped engagement that is usually the right side of the line — Odoo's own module model is exactly "separate addon" — and it is a materially different answer from `AGPL`, where the network-use clause reaches a hosted deployment** |

🔴 **A correction to this pass's own working note.** An ad-hoc probe written for this run ordered its `GNU GENERAL PUBLIC` test before its `GNU LESSER` test and therefore reported **`GPL`**. 🟢 **The KB's own classifier, `lib/license_family.sh`, returns `LGPL-3.0`, and the published cell is the classifier's.** 🔵 **Recorded because the direction of the error is the dangerous one: it over-reports the restriction, and an over-restrictive cell gets a usable platform struck off a shortlist just as surely as an under-restrictive one gets a studio sued.** 🟡 **`ACTION UW`: no grant cell on these shelves may come from a probe written for one pass. `osi_family_of` is the authority, and it is already in `make gate-offline`.**

### 🟡 `V237-2` — the APAC platform tier, with its dormancy on the row rather than in a footnote

`学校管理 license:apache-2.0` returned **`74`**. Its top rows are the Chinese-language platform estate, and the largest is also the stalest:

| platform | grant | ★ | forks | last push | head | what it is |
|---|---|---|---|---|---|---|
| [`gongfuxiang/schoolcms`](https://github.com/gongfuxiang/schoolcms) | 🟢 **`Apache-2.0`** — `LICENSE` at `master` | **292** | 110 | 🔴 **`2020-04-22`** | `master` · `21d6a41` | 🟢 **The largest permissive school academic-affairs platform on this shelf by stars**, self-described as the first open-source one in China: students, grades, teachers, grade lookup, site layout. PHP. 🔴 **Six years and five months without a push.** 🔵 **Shelved anyway, and this is why: `292`★/`110` forks of `Apache-2.0` PHP is a *fork base*, not a dependency. The honest cell reads "adopt the code, do not expect the project"** |
| [`373675032/academic-report`](https://github.com/373675032/academic-report) | 🟢 **`Apache-2.0`** — `LICENSE` at `main` | **99** | 10 | 🔴 `2023-12-22` | `main` · `4297548` | Spring Boot academic-report/seminar management for Chinese universities. 🔴 Dormant. 🟡 A narrow module, which is what makes it liftable |
| [`3yangyang9/DeepTutor-AILearning`](https://github.com/3yangyang9/DeepTutor-AILearning) | 🟢 **`Apache-2.0`** — `LICENSE` at `main` | **44** | 0 | 🟢 `2026-10-09` | `main` · `ce32cf8` | 🟢 **The one live row of the four, and the only one with a tenancy model worth copying:** platform → institution → **campus** → teacher/student, with the platform operator holding model selection and **billing policy**. Python. 🔴 **Seven days old and `0` forks** — the architecture is the asset, not the code. 🟡 **Name collision warning: it is NOT `HKUDS/DeepTutor`**, the carried `Apache-2.0` row this shelf has held since `p44` |
| [`dromara/skyeye`](https://github.com/dromara/skyeye) | 🟢 **`MIT`** — `LICENSE` at `company_server`, holder *智能制造云办公*, © 2024 | **1230** | 300 | 🟢 `2026-10-15` | 🟡 `company_server` · `dc72fc6` | 🟡 **Not an education platform — an `MIT` OA/ERP/CRM suite from the `dromara` OSS foundation that names schools as a target deployment** alongside hospitals and SMEs, with Activiti 5.22 dynamic forms, attendance, approvals, timetabling. 🟢 **Shelved as the *administrative* half a school ERP needs and the education-specific rows do not have.** 🔴 **Default branch is `company_server`, not `main`** |

### 🟢 `V237-3` — LATAM: a national-examination vertical, which is a platform category this shelf did not have

| platform | grant | head | region | what it is |
|---|---|---|---|---|
| [`Dramoscuello/simic`](https://github.com/Dramoscuello/simic) | 🟢 **`Apache-2.0`** — `LICENSE` at `main` | `main` · `9fc667a` | 🟢 **LATAM** *(evidenced: Spanish payload, binds **ICFES Saber 11**, the Colombian state examination)* | 🟢 **Generation, administration and analysis of Saber 11 mock examinations.** Vue. Created `2026-06-27`. 🔴 `2`★ and dormant since `2026-07-23`. 🔵 **Shelved because of the category, not the traction: a platform bound to a named national high-stakes examination is a procurement object in that country, and this shelf's LATAM entries were general-purpose school systems until now.** 🟡 The same shape exists for Brazil's ENEM and Mexico's EXANI and 🔴 **neither surfaced on this channel this pass** |

### 🔵 The platform map, re-stated at the licence

| posture | what it means for a studio | rows |
|---|---|---|
| 🟢 **permissive, live** | adopt and ship | `3yangyang9/DeepTutor-AILearning` *(7 days old)* · `dromara/skyeye` *(not education-specific)* |
| 🟡 **permissive, dormant — a FORK BASE** | adopt the code, own the maintenance | `gongfuxiang/schoolcms` *(292★)* · `373675032/academic-report` · `Dramoscuello/simic` |
| 🟡 **weak copyleft — module-safe** | build addons freely, do not fork the core closed | 🆕 `openeducat/openeducat_erp` **`LGPL-3.0`** |
| 🔴 **strong copyleft** | the carried Moodle/Sakai/DSpace tier, unchanged this pass | — |

🔴 **Declared gap, stated rather than left silent:** the mandated platform query returned **no** education-specific platform under `MIT` or `Apache-2.0` and said so; this pass's `5` permissive platform rows came from the **REST channel in Chinese and Spanish**, not from it. 🟡 **`ACTION US`'s division of labour holds on this shelf too: web search for market and regulation, REST for supply.**

## Pass 236 — 2026-10-16 — A PLATFORM THIS SHELF NEVER LISTED HAS BEEN **SWITCHED OFF**, AND THE REPLACEMENT MAP IS A COPYLEFT INCUMBENT PLUS TWO PERMISSIVE PROJECTS WITH `1` STAR BETWEEN THEM

🔴 **GitHub Classroom was decommissioned on `2026-08-28`.** It is the platform on which a large share of the world's university CS coursework was distributed and auto-graded, and 🔴 **this shelf never carried it** — because it was hosted, not installable, and this file lists systems you can stand up.

🔵 **Evidence:** [`p236-classroom-decommission`](../evidence/p236-classroom-decommission.2026-10-16-p236.tsv)

### 🟡 The gap this exposes in the shelf's own selection rule

🔵 **This file's rule — *"real systems that can be customized"* — silently excluded every hosted platform, so when one was withdrawn there was no cell to correct.** The platform's absence from the shelf was indistinguishable from the platform not mattering. 🟡 **`ACTION UO`: a hosted platform that an installable row exists *to replace* belongs on this shelf as a `WITHDRAWN` row, precisely so its withdrawal has somewhere to land.** Discharged for this one below.

### 🔴 `WITHDRAWN` — GitHub Classroom

| platform | status | first-hand evidence | what it leaves behind |
|---|---|---|---|
| **GitHub Classroom** *(hosted)* | 🔴 **DECOMMISSIONED `2026-08-28`**; sign-ups closed `2026-05-26` | 🟢 [`github/gh-classroom`](https://github.com/github/gh-classroom), the official CLI extension, returns 🔴 **`archived: true`** on the REST channel, as do `3` of the `12` `classroom-resources` repositories. 🔴 The announcement page itself is **not readable from this session** — `github.blog` does not resolve — so this cell rests on the `archived` flags, not on a quote. | Repositories and accounts survive. 🔴 **Classroom-only data does not**: assignment names, tests defined outside repositories, and LTI-integrated rosters are reported deleted. |

### 🟢 The installable replacement map, read at the grant

| platform | grant | ★ | stands up as | the constraint a studio must price in |
|---|---|---|---|---|
| [`foundation50/classroom50`](https://github.com/foundation50/classroom50) | 🔴 **`GPL-3.0`** *(`LICENSE` + `README` §License, both read)* | **215** | 🟢 **No server and no database of its own** — static site on GitHub Pages, `gh teacher` / `gh student` CLI extensions, assignments and scores live in the teacher's GitHub org, grading runs in GitHub Actions | 🔴 **Copyleft.** A derivative distributed to a client must carry `GPL-3.0`. 🔴 Also requires a **Team or Enterprise** org *(free for verified educators via GitHub Education)* and broad org-wide read/write scope. |
| [`jayenashar/classroom`](https://github.com/jayenashar/classroom) | 🟢 **`MIT`** | 🔴 **1** | Self-hosted: static SPA + Firestore + Cloud Functions + a GitHub App | 🟢 **Verified student identity is first-class** — institutional sign-in, then GitHub OAuth linking. 🔴 One star; treat as a design to read, not a system to adopt. |
| [`jdelfino/handout`](https://github.com/jdelfino/handout) | 🟢 **`Apache-2.0`** | 🔴 **0** | Shell; distribution only | 🔴 **No autograding in v1.** Last push `2026-05-28`. |
| [`classroom-resources/*` autograding Actions](https://github.com/classroom-resources) | 🟢 **`MIT`** throughout | — | The original grading steps, as GitHub Actions | 🔴 **Engine, reporter and command-grader are `archived`; the Python and I/O graders are not.** 🟢 `MIT` means the frozen half is forkable — see [`compose/patterns.md`](../compose/patterns.md) `P236-1`. |

🔴 **The procurement reading, stated plainly:** the only replacement with real adoption is copyleft; the permissive alternatives have `1` star between them; and the permissively licensed code with actual production history is the **archived** first-party chain. 🟢 **That combination is unusual and it favours a studio** — the mature, battle-tested, `MIT` code is sitting unmaintained and free to fork, which is a far better starting position than a greenfield build.

### 🟢 Carried platform rows re-read on the new channel — no change

🟢 **`OpenEduCat`** remains the vendor-confirmed education ERP/SIS answer on this shelf and remains 🔴 **`LGPL-3.0`**, built on Odoo. The mandated vertical query *(`open source platform education ERP CRM MIT Apache`)* returned **no `MIT`- or `Apache`-licensed SIS this pass**, as it has not in any previous pass. 🟡 **Per `ACTION UK` that is this channel's result, not an absence** — and `p234`'s `BSD-3-Clause` state SIS, already on these shelves, is the standing counter-example to reading it as one.

## Pass 235 — 2026-10-16 — THE PLATFORM MAP RE-READ AT THE GRANT, AND `GPL-2.0`'s HOLDER FIELD TURNS OUT NOT TO EXIST

🔴 **`0` new platforms. `3` platform-tier grants re-read at byte precision.** 🔵 **Evidence:** [`p235-latam-verify`](../evidence/p235-latam-verify.2026-10-16-p235.tsv)

### 🟢 Re-verified this window

| platform | SHA this window | grant, read first-hand | what changed |
|---|---|---|---|
| 🔴 [`portabilis/i-educar`](https://github.com/portabilis/i-educar) `719★` | `7903a3efc768` *(was `cd1da68` on this shelf)* | 🔴 **`GPL-2.0`**, `master/LICENSE`, **`18 092` B**, `Version 2, June 1991` | 🟢 **Licence and byte count UNCHANGED — the cell on this shelf is RIGHT.** 🟢 The SHA moved, so the project is active |
| 🟡 [`yunger7/enem-api`](https://github.com/yunger7/enem-api) | `938c56fbd3b3` | 🔴 **`GPL-2.0`**, `18 092` B — **byte-identical to `i-educar`** *(`cmp` clean)* | 🟢 same canonical blob |
| 🟡 [`inepdadosabertos/api`](https://github.com/inepdadosabertos/api) | `7d32b7e23bc6` | 🔴 **`GPL-2.0`**, `18 025` B — same `Version 2, June 1991`, **`67` B shorter** | 🔴 **So byte count does NOT identify a version** |

### 🔴 `GPL-2.0` cannot place its own platform — the extension to p234's lever

p234 established that placement comes from **holder type**, and named `Apache-2.0` as the non-placing class because *"an Apache body has no holder field at all"*. 🟢 **`GPL-2.0` belongs in that class too, and this shelf is where it matters most, because the platform tier is where the copyleft rows are.**

🔴 **A `GPL-2.0` body's only real copyright line is the FSF's own** — `Copyright (C) 1989, 1991 Free Software Foundation, Inc.` at line `4`. The other two are **templates**: `Copyright (C) <year> <name of author>` (line `294`) and the *"Gnomovision version 69"* example (line `315`).

🟢 **The consequence, stated plainly:** `i-educar` is self-described as the largest free-software education platform in Brazil, and **its grant body names Boston, Massachusetts.** 🔴 **Any harvester that places a platform from its licence file will place it to North America or nowhere.** 🟢 **`i-educar` places only from its DESCRIPTION** *("do Brasil")*, which is layer D — and layer D needs a national language or a named country or agency, so it works here and fails on the next row.

### 🟢 The placing platform tier, by contrast

| tier | row | licence | holder in the grant | places from its own grant? |
|---|---|---|---|---|
| 🟢 LMS | [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | **`Apache-2.0`** | 🔴 none *(Apache has no holder field)* | 🔴 **NO** — p234 |
| 🟢 SIS | [`svws-nrw/SVWS-Server`](https://github.com/svws-nrw/SVWS-Server) | **`BSD-3-Clause`** | 🟢 a state ministry at a street address in Düsseldorf | 🟢 **YES** — p234 |
| 🟢 curriculum data | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | **`MIT`** `1 092` B | 🟢 **`Profy Tecnologias Educacionais Ltda`** | 🟢 **YES — and it is the LATAM entry** |
| 🔴 school management | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | **`GPL-2.0`** `18 092` B | 🔴 FSF boilerplate | 🔴 **NO** |

🟢 **So the placeable platform tier is `BSD`/`MIT`, and it is exactly the tier a studio can build on.** 🔴 **The two largest platforms on this shelf — the `Apache-2.0` LMS and the `GPL-2.0` SIS — are both unplaceable from their grants, for opposite reasons: one has no holder field, the other has only the FSF's.**

### 🟡 What to customise, and the licence decision each forces

- 🟢 **`OpenOLAT`** *(`Apache-2.0`)* — a full LMS, `31 854` commits, frentix GmbH Zurich. 🟢 **Permissive: build AI on top, keep your own code.**
- 🟢 **`svws-nrw/SVWS-Server`** *(`BSD-3-Clause`)* — a state school-administration system, `9 832` commits, Java 21 + Gradle 8, MariaDB, Docker, `17` artefacts on Maven Central under `de.svws-nrw`. 🟢 **Permissive, and the reference build for a public-sector SIS.**
- 🟢 **`bncc-dev` estate** *(`MIT` code + `CC BY 4.0` data)* — the curriculum layer, installable from `PyPI`/`npm`, with an MCP server. 🟡 **Note the split scope: code and data carry DIFFERENT licences in the SAME artefact** — the npm tarball and the PyPI wheel each ship `MIT` code and `CC BY 4.0` data, so attribution obligations travel with the data even where the code imposes none. 🔴 **The name and visual identity are explicitly NOT licensed.**
- 🔴 **`i-educar`** *(`GPL-2.0`)* — integrate beside it over its APIs; **a plugin inherits `GPL-2.0`**, and whether that blocks reuse in `GPL-3.0` code still depends on an election nobody has read.

## Pass 234 — 2026-10-16 — THE *"NO PERMISSIVE PLATFORM"* FINDING, CONFIRMED NINE TIMES, IS **BROKEN** — AND THE `Apache-2.0` LMS THAT BREAKS IT WAS GRANT-READ BY `p209`, `25` PASSES BEFORE THIS SHELF LAST DENIED IT

⏱️ **THIRD pass of `2026-10-16`.**

🔴 **`1` NEW permissive platform row *(SVWS)* plus `1` already-carried one promoted to the permissive tier *(OpenOLAT, grant-read at `p209`)*. The nine-pass streak ends here — and on the LMS limb it ends on a counter-example this KB had already VERIFIED and then argued against for `25` passes.**

🔵 **Evidence:** [`p234-new-rows`](../evidence/p234-new-rows.2026-10-16-p234.tsv) · [`p234-census-false-positives`](../evidence/p234-census-false-positives.2026-10-16-p234.tsv) · [`p234-licence-field-defect`](../evidence/p234-licence-field-defect.2026-10-16-p234.tsv)

### 🔴 `V234-1` — the correction, stated against this shelf's own words

`V233-1` published: *"the mandated vertical query returned `0` MIT- or Apache-licensed education platforms, and the search's own summary says so in as many words."* 🟡 **The summary did say so. It also said, in the same result, that OLAT *"is a free e-learning open source software that operates under Apache license 2.0."*** 🔴 **And `p209` had ALREADY opened the `LICENSE` file by hand — `197` lines, verbatim `Apache License, Version 2.0` — and published that the cell was right.** 🔵 **So the nine-pass denial was never short of evidence. It contradicted evidence this KB had already produced.**

| platform | licence — **read first-hand this pass** | what it is | status here |
|---|---|---|---|
| **OpenOLAT** 🔵 *(carried since `p209`, promoted)* | 🟢 **`Apache-2.0`** — canonical body, **`10 982` B**, APPENDIX stripped, `master` @ `40c3af60221b`; `p209` read it as `197` lines / `10.7` KB | 🟢 **A full LMS**: teaching, learning, assessment, communication. `31 854` commits, `447` stars, `167` forks, `21.2-SNAPSHOT`. frentix GmbH, Zurich | 🟢 **THE COUNTER-EXAMPLE. A permissive LMS a client can fork, extend and ship commercially.** 🔴 Not on Maven Central — ships from `nexus.openolat.org`. 🔴 README cites a `NOTICE.TXT` that `404`s. 🔴 `pom.xml` licence string is the typo'd `"Apache 2.0 Open Source L6icense"` |
| 🆕 **SVWS** *(the `svws-nrw` estate)* | 🟢 **`BSD-3-Clause`** — **`1 611` B** core, `dev` @ `c2f1a7f1f902`; `9` further rows `BSD-3-Clause`/`MIT` | 🟢 **A state school-administration system / SIS** in production across North Rhine-Westphalia. `9 832` commits, Java 21, MariaDB, Docker, **`17` Maven artefacts under `de.svws-nrw`**, plus Vue/TS modules for grades, conferences, import and forecasting | 🟢 **The EMEA counterpart to Ed-Fi, and the ONLY row in this industry that is permissive, platform-scale, coordinate-resolvable AND placeable from its own grant** *(a ministry at a street address)*. 🔴 Default branch `dev`. 🔴 GitHub says `"Other"`. 🟡 Domain model encodes NRW school law |
| **OpenEduCat** | 🔴 `LGPL-3.0` *(on Odoo)* | education ERP: enrolment CRM, student information, admissions | already carried — unchanged |
| **TAO** *(`oat-sa`)* | 🔴 `GPL-2.0-only` / `LGPL-2.1` | the most complete open assessment platform | already carried — read to scope, build on the permissive QTI rows |
| **Kuali** | institution-governed consortium | ERP, SIS, research administration | already carried. 🟢 `org.kualigan` confirmed PRESENT this pass: `kc/ kfs/ kuali/ liquibase/ maven/ pom/` |

### 🔴 `V234-2` — the customisable-platform map, corrected where p233's census was read too hard

🔴 **p233's `V233-2` table read platform resolvability off groupId PREFIXES. Two cells opened this pass; both were false positives.** The map below marks what is **established** against what was **assumed**.

| platform | ecosystem | licence | Maven-resolvable? | AI-on-top posture |
|---|---|---|---|---|
| 🆕 **SVWS** | 🟢 **JVM** | 🟢 **`BSD-3-Clause`** | 🟢 **YES — `de.svws-nrw`, `17` artefacts, VERIFIED by opening the listing** | 🟢 **The best AI-on-top target in this industry: permissive, an `svws-openapi` module as the seam, and a published `BSD-3-Clause` anonymised test-database corpus to develop against** |
| **OpenOLAT** 🔵 *(carried since `p44`, grant-read `p209`)* | 🟢 **JVM** | 🟢 **`Apache-2.0`** | 🔴 **NO — and this CORRECTS p233.** `org.olat` is **JAMWiki**; `org.openolat` is a true `404` *(control passed in-window)*. Ships from `nexus.openolat.org` | 🟢 Fork-and-extend is licence-clean. 🔵 Add the project's Nexus to the build, or vendor the war |
| **Moodle** | PHP | copyleft | 🔴 no — expected | the LMS to attach to; plugin + `version.php` conventions already mapped |
| **Open edX** | Python | copyleft | 🔴 no — expected | XBlock remains the integration seam |
| **Sakai** | JVM | `ECL-2.0` | 🟡 **`org.sakaiproject` is a namespace-presence fact, NOT a verified resolvability claim** *(`ACTION UB`)* | a real integration surface, but confirm coordinates before quoting |
| **DSpace** | JVM | copyleft | 🟡 `org.dspace` — presence only, unopened | institutional repository — the research-output seam |
| **Opencast** | JVM | copyleft | 🟡 `org.opencastproject` — presence only, unopened | lecture capture — transcription and search seam |
| **CAS / uPortal** | JVM | `Apache-2.0` *(Apereo)* | 🟡 `org.apereo` + `org.jasig` — presence only, unopened | the identity seam |
| **FenixEdu** | JVM | — | 🔴 **NO — CORRECTED.** `org.fenixedu` holds two artefacts, both `fenixedu-scala-sdk` *(Scala 2.13 and 3)*: **a client SDK, not the platform** | 🔴 **`intel/market.md`'s claim that the census surfaced *"the one natively EMEA platform on this map"* is not supported by the cell.** 🟢 The genuinely EMEA platform rows are now SVWS *(Germany)* and OpenOLAT *(Switzerland)* |
| **TAO** | PHP | 🔴 `GPL-2.0-only` | 🔴 no — expected | assessment; build the conformant pieces on the permissive QTI rows |
| **Gibbon** | PHP | 🔴 `GPL-3.0` | no | 🔴 **default branch is the release branch `v31.0.00`** — the trap row |
| **Frappe Education** | Python | 🔴 `GPL-3.0` by a `19`-byte claim | no | on ERPNext; 🔴 get the grant text before anyone forks it |
| **AlekSIS** | Python | 🔵 unread | n/a | 🔴 **DEAD on github.com — hosted on `edugit.org`.** A channel gap, not an absence. `ACTION UD` |

### 🟢 `V234-3` — what the correction changes about how a vertical engagement is priced

🔵 **For nine passes the sales line was: *the platform tier is copyleft, so the permissive layer is standards and integration, and integration is where the revenue is.* That line is still mostly true, and it is still the right default. What changed is that there is now a second shape available.**

| shape | when it applies | licence posture | what it is worth |
|---|---|---|---|
| **INTEGRATE** *(the nine-pass default)* | Moodle, Open edX, TAO, OpenEduCat, Sakai — the copyleft estate | 🟢 **Safe: a `GPL`/`LGPL` platform you integrate WITH is a client asset. The obligation starts when you DISTRIBUTE a derivative** | the existing recipe book — plugin/XBlock seams, standards adapters |
| 🆕 **FORK** *(new this pass)* | 🟢 **OpenOLAT** *(`Apache-2.0`)* and 🟢 **SVWS** *(`BSD-3-Clause`)* | 🟢 **Clean: fork, extend, re-licence the additions, ship commercially. No copyleft obligation, no consortium governance** | 🟢 **A productisable base.** For an EMEA client that wants *their* LMS or *their* SIS rather than a Moodle instance, this is now quotable — and it was not last pass |

🔴 **Two honest limits on the FORK shape.** **(1)** SVWS's domain model is **NRW school law** — `Laufbahnplanung`, `Blockungen`, `Abschlussberechnungen`, `Zeugnisse` — so outside NRW it is an architecture and a schema to learn from, not a drop-in; the reusable parts are `svws-openapi`, `svws-core`, the reporting module and the test-database corpus. **(2)** OpenOLAT's missing `NOTICE.TXT` and typo'd pom licence string are exactly the kind of diligence snag that stalls a fork at legal review — 🟢 **raise both in week one, when they cost nothing, rather than at contract.**

## Pass 233 — 2026-10-16 — THE VERTICAL PLATFORM TIER IS CONFIRMED COPYLEFT FOR A **NINTH** TIME, NOW FROM MAVEN COORDINATES RATHER THAN FROM GITHUB

⏱️ **SECOND pass of `2026-10-16`.**

🔵 **`0` new platform rows. `1` already-carried platform re-confirmed by the mandated vertical query, `4 798` Maven groupIds enumerated. Published as a measurement rather than padded — the NINTH consecutive pass to do so.**

🔵 **Evidence:** [`p233-maven-org-census`](../evidence/p233-maven-org-census.2026-10-16-p233.tsv) · [`p233-queries`](../evidence/p233-queries.2026-10-16-p233.tsv)

### 🔴 `V233-1` — the mandated vertical query answered the licence question itself

The query was *"open source platform education ERP CRM student information system MIT Apache"*. 🔴 **It returned `0` MIT- or Apache-licensed education platforms, and the search's own summary says so in as many words.**

| platform | licence | status here |
|---|---|---|
| **OpenEduCat** | 🔴 `LGPL-3.0` *(on the Odoo framework)* | already carried — education ERP with enrolment CRM, student information, admissions pipeline |
| **Kuali** | institution-governed consortium | already carried — ERP, SIS and research administration, and 🟢 **present on Maven as `org.kuali` + `org.kualigan`** |

🟢 **This is the ninth independent reproduction of the finding this KB is built on: the platform tier in education is copyleft or consortium-governed, and the permissive layer is STANDARDS AND INTEGRATION.** 🔵 **That is not a disappointment — integration is where the revenue is, and a `GPL`/`LGPL` platform you integrate with is a client asset, not a licence problem. The licence problem starts when you DISTRIBUTE a derivative.**

### 🟢 `V233-2` — the customisable-platform map gains a JVM column, read from coordinates

🟢 **Every vertical platform worth customising with AI on top, now cross-checked against the Maven `org.` namespace** — the channel p232 had to declare unmeasured:

| platform | ecosystem | on Maven `org.`? | AI-on-top posture |
|---|---|---|---|
| **Moodle** | PHP | 🔴 no — **expected** | the LMS to attach to; its plugin and `version.php` conventions are already mapped on these shelves |
| **Open edX** | Python | 🔴 no — **expected** | XBlock remains the integration seam |
| **Sakai** | 🟢 **JVM** | 🟢 `org.sakaiproject` | a real Maven-resolvable integration surface |
| **OpenOLAT** | 🟢 **JVM** | 🟢 `org.olat` — 🔴 **NOT** `org.openolat` | the rename never reached the coordinates; a build file must use the old groupId |
| **DSpace** | 🟢 **JVM** | 🟢 `org.dspace` | institutional repository — the research-output seam |
| **Opencast** | 🟢 **JVM** | 🟢 `org.opencastproject` | lecture capture — the media seam for transcription and search. 🔵 p230: the repository MOVED to `opencast/opencast`, the coordinates did not |
| **CAS / uPortal** | 🟢 **JVM** | 🟢 `org.apereo` + `org.jasig` | the identity seam, and both namespaces publish |
| **FenixEdu** | 🟢 **JVM** | 🟢 `org.fenixedu` | 🟢 **the one natively EMEA platform on this map** — academic management built at Instituto Superior Técnico, Lisbon |
| **TAO** | PHP | 🔴 no — **expected** | assessment; the `oat-sa` estate is `GPL-2.0-only` throughout *(p222)* |
| **OpenEduCat** | Python/Odoo | 🔴 no — **expected** | `LGPL-3.0` ERP |

🔴 **And the standards body, which is the row that matters: `org.imsglobal` holds exactly ONE artefact, `basiclti-util/`.** A client expecting to `pom.xml` their way to LTI 1.3, QTI or OneRoster on the JVM **cannot**. 🔵 **The permissive standards implementations this KB carries are Node, Go, PHP and Python — `lti-tool`, `lrnr-lti`, `peregrine-lti`, `lti-go`, `bnsoftware/lti-1p3-tool`, `go-qti`, `text2qti`, `feyst/qti3-validator`.**

🟢 **The practical consequence for a vertical engagement: the AI layer does NOT go in the JVM platform. It goes beside it, speaking the standard, in the ecosystem that actually has permissive implementations** — which is exactly the shape `P233-R1` and `P233-R2` sell.


## Pass 232 — 2026-10-16 — THE `Ed-Fi` DATA STANDARD ENTERS THIS SHELF AS THE ONLY **`Apache-2.0` PLATFORM-SCALE** ESTATE IN EDUCATION, AND THE `TAO` ASSESSMENT ESTATE ENTERS FLAGGED

🔵 **`2` platform entries added, both verified live this pass. The `no-permissive-platform` finding is CONFIRMED for a ninth consecutive pass — and now has an exception that is not an LMS.**

🔵 **Evidence:** [`p232-edfi`](../evidence/p232-edfi.2026-10-16-p232.tsv) · [`p232-queries`](../evidence/p232-queries.2026-10-16-p232.tsv)

| platform | licence | what it is | the consequence for a deliverable |
|---|---|---|---|
| 🆕 **Ed-Fi ODS / API** *(+ Data Management Service for `v8+`)* | 🟢 **`Apache-2.0`** *(all `9` repositories, grants read first-hand)* | **The K-12 operational data store and REST API standard** used as a district-and-state data backbone, with a published data standard, an API design standard, container deployment, a cross-instance publisher, an admin/credential plane and a third-party production fork | 🟢 **The only platform-scale estate in this industry a client can fork, extend and ship commercially without a copyleft obligation.** 🔵 Scope to the target version first: `v7.x` is the ODS/API line *(admin via `ODS-Admin-API`)*, `v8+` is the Data Management Service line *(admin moves to the Configuration Management Service)*. 🔴 `Ed-Fi-Data-Standard`'s default branch is `v6.2.0`, not `main` — a deployment script that assumes `main` will check out nothing |
| 🆕 **TAO** *(the `oat-sa` estate)* | 🔴 **`GPL-2.0-only` / `LGPL-2.1`** across ~`20` Packagist packages, released through `2026-10-15` | **A full computer-based assessment platform** with its own QTI SDK *(`qtism`)*, item and test runners, QTI printing, LTI delivery providers and a OneRoster importer — the most complete open assessment estate in existence | 🔴 **Flagged, not recommended for a customised client delivery: `GPL-2.0-only` on the libraries and `LGPL-2.1` on the Symfony bundle.** 🟡 **Tabled because it is the reference for what a complete assessment platform contains** — read it to scope, then build the conformant pieces on the `MIT`/`BSD` rows this KB carries *(`qti3-validator`, `qti-scoring-system`, `go-qti`, `text2qti`)* |

## Pass 231 — 2026-10-15 — THE ASSESSMENT VERTICAL GETS A **GATE** AND A **HUMAN SURFACE**, AND THE *"NO MIT LMS"* FINDING REPRODUCES A FOURTH TIME

🔵 **`2` platform-adjacent rows added, `1` standing licence finding re-confirmed on a fresh query, `0` padded.**

🔵 **Evidence:** [`p231-new-rows`](../evidence/p231-new-rows.2026-10-15-p231.tsv) · [`p231-regional-queries`](../evidence/p231-regional-queries.2026-10-15-p231.tsv)

### 🔴 `V231-1` — there is still no `MIT` LMS, and the vertical query returns the same six platforms every time

🟡 **Probed again this pass *(`open source platform education LMS SIS ERP MIT Apache 2026`)* and the answer is unchanged — which is worth publishing precisely because it keeps being asked:**

| platform | licence | what it is | the consequence for a deliverable |
|---|---|---|---|
| **Moodle** | 🟡 `GPL-3.0` | the most-deployed open-source LMS in the world | 🔴 customisation stays plugin-shaped; a proprietary fork is not available |
| **Open edX** | 🟡 `AGPL-3.0` *(some components Apache-2.0 — contested across sources, verify per component)* | MOOC-scale platform | 🔴 AGPL `§13`: network use triggers the source obligation |
| **Canvas LMS** *(community edition)* | 🟡 `AGPL-3.0` | the dominant HE LMS in North America | 🔴 same `§13` reach |
| **Sakai** | 🟡 `Apache-2.0` / `ECL-2.0` — 🔴 **sources DISAGREE and this KB has not read the grant first-hand** | HE collaboration + learning environment | 🟡 ECL-2.0 is Apache-2.0 with a narrowed patent clause; the difference matters and must be read before it is quoted |
| **OpenOLAT** | 🟢 **`Apache-2.0`** | web LMS shipping QTI, SCORM, curriculum management and assessment | 🟢 **the permissive option, and the reason this KB retired *"no permissively licensed full-featured LMS"* as stated** |
| **OpenEduCat** | 🟡 `LGPL-3.0` | the closest thing to an integrated LMS + SIS + ERP *(`70`+ modules, attendance, fees)* | 🟡 library-copyleft: linking is fine, modifying the modules is not free |

🔵 **The honest summary for a buyer: the permissive LMS is `OpenOLAT`, the ubiquitous LMS is `GPL` Moodle, and the ERP-shaped one is `LGPL` OpenEduCat. There is no `MIT` row in this tier and four passes of querying have not produced one.**

### 🟢 `V231-2` — what IS newly permissive is the layer ABOVE the platform, and that is where the vertical is actually built

🟢 **Both rows added this pass are platform-INDEPENDENT and `MIT`, which is what makes them usable against a `GPL`/`AGPL` estate without contaminating anything:**

| row | licence | the vertical slot it fills | wiring |
|---|---|---|---|
| 🆕 [`feyst/qti3-validator`](https://github.com/feyst/qti3-validator) | 🟢 **MIT** | **assessment conformance gate** — the slot that was empty on these shelves | an HTTP service beside the LMS: `POST` the QTI 3 package, fail the pipeline on `fatals`. Docker/`ghcr`, `~21` MB, schemas built in, **no egress by its own claim** |
| 🆕 [`metyatech/qti-scoring-system`](https://github.com/metyatech/qti-scoring-system) | 🟢 **MIT** | **human scoring + oversight record** | a Next.js app over exported assessment-test + Results Reporting XML; comments persist as `COMMENT` outcomes, so the record returns to the platform in the standard's own vocabulary |

🔵 **The vertical pattern this establishes, and it generalises past assessment:** the platform stays copyleft and untouched; the AI and governance layer is permissive and studio-owned; the interface between them is the **standard's own file format**, not an API wrapper. 🟢 **`OpenOLAT` is the one platform in the table that already speaks QTI natively, which makes it the cheapest demo environment for this stack — and its `Apache-2.0` grant means the demo can become the product.**

🔴 **The slot still empty in this tier: an ingestion path. Both new rows read a FOLDER or a POSTed package, not an LMS. The export/import job between Canvas or Moodle and this stack is bespoke code in every engagement, and nothing on these shelves provides it.**

## Pass 230 — 2026-10-15 — THE PLATFORM TIER IS RE-PROBED FOR EXISTENCE FOR THE FIRST TIME, AND IT HOLDS — BUT THE STANDARDS LAYER UNDERNEATH IT DOES NOT

🔵 **`0` new platform rows *(`1` of `1` named platform already carried, for a FOURTH pass)*. All `9` platform-tier addresses confirmed LIVE. `1` adjacent platform confirmed GONE, `1` confirmed MOVED.** 🔵 **Evidence:** [`tc-existence-sweep`](../evidence/tc-existence-sweep.2026-10-15-p230.tsv) · [`td-dotted-slug-regate`](../evidence/td-dotted-slug-regate.2026-10-15-p230.tsv)

### 🟢 `P230-V1` — every platform this KB recommends still resolves

🟢 **`ACTION TC` swept `1 904` addresses. The platform tier lost NOTHING: [`moodle/moodle`](https://github.com/moodle/moodle), [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform), [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms), [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms), [`frappe/lms`](https://github.com/frappe/lms), [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT), [`UniTime/unitime`](https://github.com/UniTime/unitime), [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst), [`Elgg/Elgg`](https://github.com/Elgg/Elgg), [`GibbonEdu/core`](https://github.com/GibbonEdu/core), [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis), [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp), [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic), [`formalms/formalms`](https://github.com/formalms/formalms), [`acanas/swad-core`](https://github.com/acanas/swad-core) and [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) all resolve with a default branch and a `HEAD`.**

🔵 **The `4` permissively buildable platforms are unchanged and all four are LIVE: `OpenOlat` *(`Apache-2.0`)*, `UniTime` *(`Apache-2.0`)*, `pupilfirst` *(`MIT`, code)* and `Elgg` *(`MIT` OR `GPL-2.0`, dual)*.**

### 🔴 `P230-V2` — what DID disappear is the layer a platform integrates through

🔴 **The adjacent tier lost `11` addresses, and the losses are structural rather than random:**

| what a client asks for | the address this KB recorded | state |
|---|---|---|
| **Caliper Analytics** *(learning analytics standard)* | `1EdTech/caliper-{java,js}`, `1edtech/caliper-php`, `imsglobal/caliper-python` | 🔴 **all four GONE, both org spellings** |
| **Open Badges** *(credentialing)* | `concentricsky/badgr-server`, `1EdTech/badgr-server` | 🔴 **GONE** |
| **xAPI pipeline** | `yetanalytics/lrspipe` | 🔴 **GONE** |
| **QTI 3** *(assessment interchange)* | `LongsightGroup/qti3-core` | 🔴 **GONE** |
| **OneRoster** *(rostering)* | `Eduware-Inc/eduware-oneroster` | 🔴 **GONE** — 🟢 but [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) and [`theopenem/OneRoster.NET`](https://github.com/theopenem/OneRoster.NET) are LIVE and `MIT` |
| **LTI 1.3** | `UOC/java-lti-1.3-provider` | 🔴 **GONE** — 🟢 [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) *(`MIT`)*, [`ucfopen/pylti1.3`](https://github.com/ucfopen/pylti1.3) *(`MIT`)*, [`UOC/java-lti-1.3`](https://github.com/UOC/java-lti-1.3) *(`MIT`)* and [`paurushrai/lti-1.3-node-nextjs-starter`](https://github.com/paurushrai/lti-1.3-node-nextjs-starter) *(`MIT`)* are LIVE |
| **lecture capture** | `apereo/opencast` | 🟡 **MOVED** → 🟢 [`opencast/opencast`](https://github.com/opencast/opencast) |
| **PHP business framework** | `Epesi-Team/epesi` | 🔴 **GONE**, both spellings |

🟢 **What a studio does with this: the LMS layer is solid and the ROSTERING and LTI layers are solid under different addresses than this KB used to reach for — all `MIT`, all read first-hand this pass. The ANALYTICS and CREDENTIALING layers have no retrievable reference implementation, and a proposal must say so rather than name a repository that `404`s in the client's first sprint.**

### 🔴 `P230-V3` — the non-OSI platform row gets the NAME of its instrument

🟡 **p229 placed [`nakafaai/nakafa.com`](https://github.com/nakafaai/nakafa.com) — an Indonesian learning platform cited `6` times here — in the non-OSI tier as `NONCOMMERCIAL-NOT-OSI`, with its channel reporting `NOASSERTION`. p230 reads the `7 705` B body:**

> 🔴 *"# **Nakafa Source Available License 1.0** — Effective date: **April 24, 2026** — Copyright (c) 2026 PT NAKAFA TEKNO KREATIF. All rights reserved. **This is not an open-source license.**"*

🟢 **A token tells a studio not to build. A NAMED instrument with an effective date is what counsel reviews, and the two are one read apart.** 🟡 **It stays beside `BUSL-1.1` on [`sdv-dev/SDV`](https://github.com/sdv-dev/SDV): readable source, no permission to build on it.**

## Pass 229 — 2026-10-15 — FIVE PLATFORM ROWS GAINED A FIRST-HAND GRANT, AND THE TWO THAT DID NOT ARE THE INTERESTING ONES

🔵 **`0` new platform rows.** 🔵 **Evidence:** [`sw-grant-ladder-reach`](../evidence/sw-grant-ladder-reach.2026-10-15-p229.tsv) · [`sy-bound-channel`](../evidence/sy-bound-channel.2026-10-15-p229.tsv)

### 🟢 `P229-V1` — the platform grants, each read at a path p228's ladder did not reach

| platform | grant | channel | what a studio may do |
|---|---|---|---|
| **Moodle** · [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 **`GPL-3.0`** *(canonical, `35 147` B)* | `main/COPYING.txt` | 🟢 build plugins; 🔴 anything linked in must be GPL-3.0-compatible — which is why the `oat-sa` `GPL-2.0-only` assessment tier stays a separate LTI tool |
| **openSIS Classic** · [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🟢 **`GPL-2.0`** | `master/docs/License.txt` | 🟡 SIS for a school district; GPL-2.0 is one-way incompatible with GPL-3.0 hosts |
| **openSIS Responsive** · [`OS4ED/openSIS-Responsive-Design`](https://github.com/OS4ED/openSIS-Responsive-Design) | 🟢 **`GPL-2.0`** | `master/docs/License.txt` | 🔵 serves the SAME `HEAD` SHA as openSIS-Classic — treat as one codebase under two names |
| **Forma LMS** · [`formalms/formalms`](https://github.com/formalms/formalms) | 🟢 **`GPL-2.0`** | `master/html/license.txt` | 🟡 corporate LMS, Italian-origin, EMEA |
| **Fedena** · [`foradian/fedena`](https://github.com/foradian/fedena) | 🟡 **`Apache-2.0` BY REFERENCE** | `NOTICE` | 🟡 permissive if the reference holds — ask for a `LICENSE` body before building on it |
| **Lumi (H5P desktop)** · [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) | 🟢 **`AGPL-3.0`** | `main/package.json` | 🔴 network copyleft: a hosted deployment triggers source disclosure |

### 🔴 `P229-V2` — `LMS-Laravel` is not MIT, and nothing here can say what it is

🔴 **Both [`LMS-Laravel/LMS-Laravel`](https://github.com/LMS-Laravel/LMS-Laravel) and [`LMS-Laravel/OLD-LMS-Laravel`](https://github.com/LMS-Laravel/OLD-LMS-Laravel) serve a `composer.json` declaring `"name": "laravel/laravel"` — the unrenamed framework skeleton. The `MIT` in it is LARAVEL's grant.** 🟡 **Published as `FOREIGN-MANIFEST`: the platform's own licence is UNKNOWN from every channel this session can reach, and a proposal that calls it MIT is quoting the scaffold.**

### 🟢 `P229-V3` — six Moodle plugin platforms settle their BOUND, and one famous row does not

🟢 **`ACTION SY` settled `9` of the `26` `BOUND` cells at `version.php`: [`Limekiller/moodle-block_openai_chat`](https://github.com/Limekiller/moodle-block_openai_chat), [`adamjenkins/moodle-local_nomoreai`](https://github.com/adamjenkins/moodle-local_nomoreai), [`caiocarvalhofre/moodle-mod_maici`](https://github.com/caiocarvalhofre/moodle-mod_maici), [`saylordotorg/moodle-local_ai_course_assistant`](https://github.com/saylordotorg/moodle-local_ai_course_assistant), [`solin-repo/moodle-block_atrisk`](https://github.com/solin-repo/moodle-block_atrisk) and [`yedidiaklein/moodle-local_aiquestions`](https://github.com/yedidiaklein/moodle-local_aiquestions) are all `GPL-3.0-or-later`.**

🔴 **[`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) is NOT settled, and the reason is the trap p225 and p227 both named:** its `main/LICENSE` is `7 652` B of CANONICAL LGPL-3.0 body, whose own text contains *"any later version"* twice. 🟢 **The canonical body is not a channel for the project's bound. Rejected rather than counted — this pass's easiest false positive.**

🟡 **`chamilo/chamilo-lms`, `frappe/lms`, `instructure/canvas-lms`, `overhangio/tutor`, `penecho/penecho` and `unslothai/notebooks` stay at the CONSERVATIVE `-only` reading, resting on ABSENCE, and this page says so rather than implying a read.**

## Pass 228 — 2026-10-15 — THE PLATFORM TIER GAINS A SECOND PERMISSIVELY BUILDABLE MEMBER FROM A RE-READ AND LOSES A `GPL` READING THAT UNDERSTATED A **NETWORK-USE OBLIGATION** — THE SECOND CONSECUTIVE PASS IN WHICH THE TIER CHANGED WITHOUT A SINGLE NEW ROW

🔵 **`0` new platform rows *(`9` of `9` named platforms already carried, for a THIRD pass)*. `2` carried platform grants corrected on first-hand reads. `1` of the two corrections runs AGAINST Globant and `1` runs against a client — the first pass on these shelves to find one of each.**

🔵 **Evidence:** [`st-shelf-gate`](../evidence/st-shelf-gate.2026-10-15-p228.tsv) · [`st-family-defects`](../evidence/st-family-defects.2026-10-15-p228.tsv) · [`st-grant-reads`](../evidence/st-grant-reads.2026-10-15-p228.tsv) · **Instrument:** [`p228-shelf-gate`](../compose/code/p228-shelf-gate/README.md) *(`30` controls)*

### 🔴 `P228-V1` — the tier, corrected

| platform | tier | p227 published | 🟢 first-hand truth, read `2026-10-15` | buildable under the standing MIT/Apache/BSD preference |
|---|---|---|---|---|
| [`OpenOlat`](https://github.com/OpenOLAT/OpenOLAT) | LMS | 🟢 `Apache-2.0` | 🟢 **unchanged** | 🟢 **YES** |
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | timetabling | 🟢 `Apache-2.0` | 🟢 **unchanged** *(`11 357` B, `58d1e17ffe51`)* | 🟢 **YES** |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | LMS / school ops | 🟢 `MIT` *(code)* | 🟢 **unchanged** — `1 684` B, `bda0aa6d49f2`; `docs/**` `CC-BY-SA-4.0` | 🟢 **YES, for the code** |
| 🆕 [`Elgg/Elgg`](https://github.com/Elgg/Elgg) | social learning | 🔴 **`GPL-2.0-only`** *(from `composer.json`)* | 🟢 **`MIT` OR `GPL-2.0` — DUAL**, `17 173` B, `7188c83d8764` | 🟢 **YES, under `MIT`** — 🔴 **it was excluded for nothing** |
| 🆕 [`acanas/swad-core`](https://github.com/acanas/swad-core) | LMS / campus | 🔴 **`GPL-3.0`** | 🔴 **`AGPL-3.0`**, `34 501` B, `884b434957ba` | 🔴 **no — and now with a NETWORK obligation it did not carry before** |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | SIS | 🟢 `GPL-3.0` *(p227)* | 🟢 **unchanged** — `35 121` B, `93178a43d6d3` reproduced to the byte | 🔴 no — **but no network-use obligation** |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | SIS | 🔴 `GPL-2.0` | 🟢 **unchanged** | 🔴 no |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | LMS | 🔴 `AGPL-3.0-only` | 🔴 **unchanged** — `35 136` B, `e12d78569742` | 🔴 no |
| [`frappe/lms`](https://github.com/frappe/lms) | LMS | 🔴 `AGPL-3.0` | 🔴 **unchanged** *(`license.txt` `33 893` B, `db1a87ba81e8`)* | 🔴 no |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | ERP / LMS+SIS | 🟡 `LGPL-3.0-only` *(p225, `2`–`1`)* | 🟢 **`LGPL-3.0` corroborated** — `8 241` B, `528f84036800` | 🟡 **weak copyleft — linkable** |
| `Moodle` · `Chamilo` · `Canvas LMS` | LMS | 🔴 copyleft | 🔴 **unchanged** | 🔴 no |
| `AlekSIS` | SIS | 🔴 no resolvable repository | 🔴 **unchanged** | 🔴 n/a |

🟢 **So the honest statement of the tier is `4` permissively buildable platforms — `OpenOlat`, `UniTime`, `pupilfirst` and now `Elgg` — up from `3`, and again the new one was already here.**

### 🔴 `P228-V2` — the two corrections point in OPPOSITE directions, and that is the pass's commercial finding

🔵 **p227 made the refuted-claims table bidirectional and predicted who pays in each direction. p228 is the first pass to produce one of each at platform tier, on the same day:**

| platform | direction | the error | who pays |
|---|---|---|---|
| 🆕 `Elgg/Elgg` | 🟢 **RESTRICTIVE** | a dual `MIT`/`GPLv2` grant published as `GPL-2.0-only` | 🟡 **Globant** — a buildable social-learning platform excluded from every engagement filter |
| 🆕 `acanas/swad-core` | 🔴 **PERMISSIVE** | `AGPL-3.0` published as `GPL-3.0` | 🔴 **a client** — a hosted build told it had no source-disclosure trigger, when it has one |

🔴 **The asymmetry that matters to a SOW: the restrictive error costs a sales opportunity and is recoverable at any time. The permissive error is discovered by a client's counsel AFTER a hosted deployment ships, and is not.** 🟢 **Both are now corrected in place behind `<!--corrected-->` markers.**

### 🟢 `P228-V3` — what each grant lets a studio ship, with the two changed rows in place

| grant | what it reaches | what a studio can ship |
|---|---|---|
| 🟢 `Apache-2.0` *(`OpenOlat`, `UniTime`)* | notice and patent terms only | 🟢 **a proprietary deliverable on top, no source disclosure** |
| 🟢 `MIT` *(`pupilfirst` code, 🆕 `Elgg` under its MIT option)* | notice only | 🟢 **same** — 🟡 `pupilfirst`'s `docs/` is `CC-BY-SA-4.0`; `Elgg`'s `/mod` plugins are `GPL-2.0-only` |
| 🟡 `LGPL-3.0-only` *(`OpenEduCat`)* | modifications to the library itself | 🟡 **link and ship proprietary around it; publish changes to the module** |
| 🟡 `GPL-2.0` / `GPL-3.0` *(`RosarioSIS`, `Gibbon`)* | derivative works **distributed** | 🟡 **a hosted service is fine; shipping a modified binary is not** |
| 🔴 `AGPL-3.0` *(`Open edX`, `frappe/lms`, `Canvas`, 🆕 `swad-core`)* | derivative works **made available over a network** | 🔴 **a hosted service triggers source disclosure — and `swad-core` joined this row this pass** |

### 🔵 `P228-V4` — the structural gap, restated for a third pass and still unclosed

🔴 **There is still NO permissively licensed, full-featured SIS.** 🟢 **`Elgg` is social learning, `UniTime` is timetabling, `pupilfirst` is school operations and course delivery. The `2` real SIS platforms here are `GPL-3.0` and `GPL-2.0`, `openSIS` is `GPL-2.0`, and `AlekSIS` still has no resolvable repository.** 🟡 **Third consecutive pass with `9` of `9` named platforms already carried: this is a genuine gap in the open-source education landscape, not a sourcing failure.**

🟢 **What DID change is that the buildable set is `4` rather than `3`, and both of this pass's movements came from re-reading grants rather than from finding software.** 🔵 **For a tier that has added no row in three passes, a shelf-wide grant re-read is the only remaining source of new commercial fact — which is the argument for `ACTION ST` becoming a standing step.**


## Pass 227 — 2026-10-15 — THE SIS TIER GAINS A PERMISSIVELY LICENSED MEMBER WITHOUT A SINGLE NEW ROW, BECAUSE **TWO OF ITS CARRIED ROWS WERE PUBLISHED UNDER THE WRONG LICENCE** — AND BOTH ERRORS RAN AGAINST GLOBANT

🔵 **`0` new platform rows *(`9` of `9` named platforms already carried, for a second pass)*. `2` carried platform grants CORRECTED on first-hand reads. `1` live table row and `1` live assertion WITHDRAWN in place. The tier's permissive count goes from `1` to `2` on a re-read, not a discovery.**

🔵 **Evidence:** [`so-untabled-refutations`](../evidence/so-untabled-refutations.2026-10-15-p227.tsv) · [`p227-verified-repos`](../evidence/p227-verified-repos.2026-10-15-p227.tsv) · **Instrument:** [`p227-direction-gate`](../compose/code/p227-direction-gate/README.md)

### 🔴 `P227-V1` — p226's platform table, corrected

🟢 **p226 published the tier as *"exactly ONE permissively-licensed LMS and ZERO permissively-licensed SIS"*.** 🔴 **The LMS half stands. The SIS half was wrong twice over, and both errors were in the RESTRICTIVE direction** — the direction the refuted-claims table could not express until this pass.

| platform | tier | p226 published | 🟢 first-hand truth, read `2026-10-15` | buildable under the standing MIT/Apache/BSD preference |
|---|---|---|---|---|
| [`OpenOlat`](https://github.com/OpenOLAT/OpenOLAT) | LMS | 🟢 `Apache-2.0` | 🟢 **unchanged** | 🟢 **YES** |
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | timetabling | 🔴 **`GPL-3.0`** | 🟢 **`Apache-2.0`** — `master/LICENSE` `11 357` B, `sha256`₁₂ `58d1e17ffe51` | 🟢 **YES — and it was excluded for nothing** |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | SIS | 🔴 **`AGPL-3.0`** | 🟢 **`GPL-3.0`** — `35 121` B, `sha256`₁₂ `93178a43d6d3` | 🔴 no — **but no network-use obligation either** |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | SIS | 🔴 `GPL-2.0` | 🟢 **unchanged** | 🔴 no |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | LMS / school ops | 🔴 **`AGPL-3.0`** | 🟢 **`MIT`**, with `docs/` at `CC-BY-SA-4.0` — `1 684` B, `sha256`₁₂ `bda0aa6d49f2` | 🟢 **YES, for the code** |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | LMS | 🔴 `AGPL-3.0` | 🔴 **`AGPL-3.0-only`** — bound settled this pass | 🔴 no |
| [`frappe/lms`](https://github.com/frappe/lms) | LMS | 🔴 `AGPL-3.0` | 🔴 **unchanged** *(`license.txt` `33 893` B)* | 🔴 no |
| `Moodle` · `Chamilo` · `Canvas LMS` | LMS | 🔴 copyleft | 🔴 **unchanged** | 🔴 no |
| `AlekSIS` | SIS | 🔴 no resolvable repository | 🔴 **unchanged** | 🔴 n/a |

🟢 **So the honest statement of the tier is: `2` permissively licensed platforms a studio can build on, not `1` — and the second one was already here.**

### 🔴 `P227-V2` — what this cost, stated plainly

🔵 **`GibbonEdu/core` and `UniTime/unitime` are the two platforms in this tier closest to the problems a studio is actually hired to solve: school administration and timetabling.** 🔴 **Both were published under a licence stricter than their real one. Any engagement filter applied to this shelf — *"show me what we can build on"* — returned `OpenOlat` and nothing else.**

🟡 **The `Gibbon` case is worse than a stale cell, because p226 did the right thing and still got it wrong:** 🔴 **its draft wrote `GPL` — correctly — then its self-audit checked that draft against these shelves, found `4` stale `AGPL` cells, and "corrected" a right answer into a wrong one, filing it under *"the error was in the PERMISSIVE direction"*.** 🟢 **Both cells are now withdrawn in place behind `<!--corrected-->` markers, and `P227-SO1` in [`agents/top.md`](../agents/top.md) carries the full sequence.**

### 🟢 `P227-V3` — and the obligation that actually changes for an engagement

🔵 **These are not interchangeable bounds, which is why the correction matters commercially and not just bibliographically:**

| grant | what it reaches | what a studio can ship |
|---|---|---|
| 🟢 `Apache-2.0` *(`OpenOlat`, `UniTime`)* | nothing beyond notice and patent terms | 🟢 **a proprietary deliverable on top, no source disclosure** |
| 🟢 `MIT` *(`pupilfirst` code)* | nothing beyond notice | 🟢 **same** — 🟡 **but `docs/` is `CC-BY-SA-4.0`: ship the docs and the share-alike obligation comes with them** |
| 🟡 `GPL-3.0` *(`Gibbon`)* | derivative works **distributed** | 🟡 **a hosted service is fine; shipping a modified binary is not** |
| 🔴 `AGPL-3.0-only` *(`Open edX`, `Canvas`)* | derivative works **made available over a network** | 🔴 **a hosted service triggers source disclosure — the single most consequential cell on this shelf** |

🔴 **The `Gibbon` error was exactly the jump from row `3` to row `4`: it asserted a network-use obligation on a platform that has none.** 🟢 **For a hosted school-management build, that is the difference between a routine engagement and one that must publish its source.**

### 🔵 `P227-V4` — the structural gap, restated and still unclosed

🔴 **There is still NO permissively licensed, full-featured SIS.** 🟢 **`UniTime` is timetabling, not a student information system; `pupilfirst` is school operations and course delivery, not a record of enrolment and transcript.** 🔵 **The `2` real SIS platforms on this shelf are `GPL-3.0` and `GPL-2.0`, and `AlekSIS` still has no resolvable repository at all.** 🟡 **This remains a genuine gap in the open-source education landscape and not a sourcing failure — `9` of `9` named platforms were already carried, for the second pass running.**


## Pass 226 — 2026-10-15 — THE SELF-HOSTED EDUCATION STACK HAS EXACTLY **ONE** PERMISSIVELY-LICENSED LMS AND **ZERO** PERMISSIVELY-LICENSED SIS, AND THE MANDATED VERTICAL QUERY RETURNED A LICENCE CONFLICT IN THE WILD

🔵 **`0` new platform rows *(`9` of `9` named platforms already carried)*. `1` canonical slug corrected on the tier's largest platform. `1` structural gap measured rather than asserted.**

🔵 **Evidence:** [`p226-regional-queries`](../evidence/p226-regional-queries.2026-10-15-p226.tsv) · [`si-alias-direction`](../evidence/si-alias-direction.2026-10-15-p226.tsv)

### 🔴 The licence shape of the tier, and what it costs a Globant engagement

🟢 **Verbatim query: `open source platform education LMS SIS MIT Apache self-hosted 2026`.** Returned `9` platforms, all already carried. 🔴 **Sorted by the grant a studio can actually build on, the tier is lopsided:**

| platform | tier | grant | buildable-on under the standing MIT/Apache/BSD preference |
|---|---|---|---|
| [`OpenOlat`](https://github.com/OpenOLAT/OpenOLAT) | LMS | 🟢 **`Apache-2.0`** | 🟢 **YES — the only one** |
| [`frappe/lms`](https://github.com/frappe/lms) | LMS | 🔴 **`AGPL-3.0`** *(`license.txt`, `33 893` B — a comparison claimed `MIT` AGAIN this pass; see below)* | 🔴 no |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | LMS | 🔴 **`AGPL-3.0`** *(`LICENSE`, `35 136` B, `sha256`₁₂ `e12d78569742`, read first-hand this pass)* | 🔴 no |
| `Moodle` | LMS | 🔴 `GPL-3.0-or-later` | 🔴 no |
| `Chamilo` | LMS | 🔴 `GPL` *(bare token on these shelves — NOT a read bound)* | 🔴 no |
| `Canvas LMS` | LMS | 🔴 `AGPL-3.0` *(community edition)* | 🔴 no |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | SIS | 🔴 **`GPL-2.0`** *(complete body minus the non-operative appendix, `15 214` B)* | 🔴 no |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | SIS | 🟢 **`GPL-3.0`** <!--corrected--> *(was `AGPL-3.0`; `P227-SO1`, read first-hand: `master/LICENSE` `35 121` B, `sha256`₁₂ `93178a43d6d3`, title line `GNU GENERAL PUBLIC LICENSE`)* | 🔴 no |
| `AlekSIS` | SIS | 🔴 **NO GRANT ESTABLISHED — the slug does not resolve** | 🔴 n/a |

🔴 **`1` of `6` LMS platforms carries a permissive grant. Of the `3` SIS platforms, `2` have an established grant and NEITHER is permissive; the third has no resolvable repository at all.** 🟡 **This is not a sourcing failure to be fixed by more searching — it is the shape of the market, and it has been stable across passes.**

### 🔴 `T226-V0` — three defects in this pass's OWN table, found before publishing

🔴 **The first draft of the table above carried three wrong cells, caught by checking each against what these shelves already hold first-hand rather than against the query results:**

| cell as first written | 🟢 what the shelves actually carry |
|---|---|
| 🟢 `Gibbon` — `GPL` — **THIS DRAFT CELL WAS RIGHT** | 🔴 **`AGPL-3.0` was the WRONG “correction”** <!--corrected--> — `GibbonEdu/core` is `GPL-3.0`. p226 judged a correct cell a defect against this KB's own `4` stale `AGPL` cells, and the error ran in the RESTRICTIVE direction, not the permissive one. See `P227-SO1` |
| 🔴 `RosarioSIS` — `GPL` | 🟢 **`francoisjacquet/rosariosis`, `GPL-2.0`**, complete body read, `15 214` B |
| 🔴 `AlekSIS` — `EUPL`/copyleft | 🔴 **NOT FOUND** — `AlekSIS/AlekSIS` and `aleksis/AlekSIS-Core` BOTH fail `git ls-remote`. There was no grant to state |

🟡 **All three came from writing a plausible licence beside a platform name instead of reading the cell.** 🔴 **`GPL` for `Gibbon` is the same class of error as the listicle's `MIT` for `frappe/lms`, committed inside this KB in the same pass that caught it outside** — which is the strongest argument available for `ACTION QO`'s licence gate. 🔵 **Thirteenth and fourteenth unit-mismatch findings: a BARE family token *(`GPL`)* is not a bound, and a platform NAME is not a resolvable repository.**

🟢 **What it means for an engagement, concretely:** the copyleft tier is perfectly usable, and most Globant education work will sit on Moodle or Open edX. 🔴 **What changes is the DELIVERABLE BOUNDARY. On AGPL-3.0 — `Open edX` and `Canvas` — network use is distribution, so a hosted customisation triggers the source obligation for the modified work.** 🟡 **The architecture that keeps a client's proprietary logic proprietary is the one that keeps it OUT of the platform process: an `aiprovider_*`/`aitool_*` plugin seam, or a separate service the platform calls. 🔵 `OpenOlat` is the one platform where that constraint does not apply, which is the whole reason to know it is there.**

### 🔴 `T226-V1` — a licence CONFLICT in the wild, returned by the mandated query itself

🔴 **A comparison page in this pass's results lists `Frappe LMS` as `MIT`. These shelves refuted that exact claim at p209 with the payload — `AGPL-3.0`, `license.txt`, `33 893` B — and it came back anyway, seventeen passes later, from a different source.** 🟢 **It was caught INBOUND by `ACTION SH`'s gate before anything was written, and is the one hit that gate produced this pass** → [`sh-inbound-gate-run`](../evidence/sh-inbound-gate-run.2026-10-15-p226.tsv).

🟡 **A second page lists `Open edX` as `MIT` — but flags its own conflict with the `AGPL` listings around it.** 🟢 **That is a source reporting the error, not circulating it, and the gate correctly stayed silent.** 🔵 **The distinction is worth keeping: one of these needs correcting, the other is doing the correcting.**

🔴 **Neither was written to any shelf.** 🟢 **And the prompt for reading `Open edX`'s `LICENSE` first-hand came out of this: `65` + `9` `AGPL` cells on these shelves and not one byte read, until now** → [`repos/foundations.md`](../repos/foundations.md) `P226-A`.

🔵 **The finding is that the vertical-platform tier is where third-party licence claims are least reliable, and the error direction is consistently PERMISSIVE: a listicle that gets it wrong gets it wrong in the direction that would make a studio relax.** 🔴 **An `AGPL-3.0` platform mistaken for `MIT` is the single most expensive licence error available in this tier.** 🟡 **Standing guidance: never take an LMS grant from a comparison page; read the repository.**

### 🔴 `P226-V2` — cite `Open edX` as `openedx/openedx-platform`

🟢 **The tier's largest platform now has a canonical slug on evidence: its own `README.rst`, byte-identical from both paths, names `openedx/openedx-platform` `5` times and `openedx/edx-platform` `0` times** → [`repos/foundations.md`](../repos/foundations.md) `P226-A`. 🔵 **This REVERSES p225's recommendation in the section below, which is left standing as the dated record.** 🟡 **Practical effect: an SBOM, dependency pin or client inventory should carry the canonical slug, with `edx-platform` noted as the alias it resolves through.**

### 🔴 The standing gap, re-measured and unchanged: no open-source SIS connector tier

🔴 **A constrained query for MCP servers against student information systems returned `9` named projects and NOT ONE institutional connector** — no Banner, no PeopleSoft, no Ellucian, no Workday Student. 🟢 **What exists is personal-scale:** one university's HEMIS instance, a Purdue public-data server that explicitly avoids student accounts, a portal SCRAPER, a read-only course catalogue, and a no-grant study assistant.

🟡 **For a studio this is the clearest unoccupied build slot on these shelves, and it has survived several passes of searching.** 🔵 **The platforms are permissively reachable even where they are copyleft, because a connector talks to an API and does not link the platform — so the licence shape above does NOT block it** → [`compose/patterns.md`](../compose/patterns.md) `P226-R3`.

## Pass 225 — 2026-10-15 — THE SHELF'S SHARPEST LICENCE QUESTION IS SETTLED: `OpenEduCat` IS `LGPL-3.0-only` BY A `2`–`1` VOTE THAT AGREES WITH THE CONSERVATIVE READING

🟢 **`ACTION RV`, carried three passes and registered p225's highest priority, is discharged on limb `1`.** 🔵 **The platform every Odoo education recipe on these shelves stands on now has a resolved bound instead of a conflict** → [`repos/foundations.md`](../repos/foundations.md) `P225-A`, [`rv-openeducat-third-channel`](../evidence/rv-openeducat-third-channel.2026-10-15-p225.tsv).

### 🟢 What changed for a customisation engagement

- 🟢 **`openeducat/openeducat_erp` — `LGPL-3.0-only` (RESOLVED, p225).** 🔵 **Third channel: the repository's root `LICENSE`, whose own preamble names *"Version 3 (LGPLv3)"* with no grant of later versions, siding with the manifest field against the module header. 🟡 The SOW language is no longer *"assume `only` and say so"* — it is `only`, with three channels cited. 🔵 p222's and p224's `RANGE-CONFLICT` cells below are superseded by this section, not rewritten.**
- 🔴 **The or-later header is still in all `8` modules read.** 🟡 **So a client who takes the header at face value will read `or-later`, and the engagement should say which channel governs before anyone relicenses a derivative. 🔵 This is the one place the resolution still needs a sentence in writing.**
- 🔴 **The root `LICENSE` points to a `COPYRIGHT` file that is `404`.** 🟡 **Copyright is named only in the module headers *(`OpenEduCat Inc`, `2009-TODAY`)* — a one-file fix on `ACTION PH`'s queue.**

### 🟢 A platform row these shelves were carrying twice

🟢 **[`INGInious/INGInious`](https://github.com/INGInious/INGInious) and [`UCL-INGI/INGInious`](https://github.com/UCL-INGI/INGInious) are ONE repository under two paths** — byte-identical ref sets, `HEAD` `76ddb145da81`, `675` refs each. 🔵 **The shelves carry `INGInious`=`19` mentions and `UCL-INGI`=`4`; those are the same autograder, and `JuezUN`=`2` is a genuine separate fork.** 🟡 **Cite it once, under either path, and note the alias — the canonical direction is NOT established, because the git service serves both with a bare `200` and no redirect.**

🔵 **Same correction, same method, for the Open edX tier:** `openedx/edx-platform` and `openedx/openedx-platform` are one repository *(`49 749` identical refs)*, so the KB's `65` + `9` AGPL cells were counting one platform twice → `ACTION SD`, limb `2`.

## Pass 224 — 2026-10-15 — MOODLE'S AI LAYER IS A **FORK, NOT A STACK**: TWO SUBSYSTEMS THAT CANNOT COMPOSE, WITH DIFFERENT MAJOR-VERSION FLOORS AND DISJOINT PLUGIN ECOSYSTEMS

🔵 **`0` new platform rows. `1` platform-level architectural constraint established first-hand, on the most-deployed LMS on these shelves.**

🔵 **Evidence:** [`p224-new-rows`](../evidence/p224-new-rows.2026-10-15-p224.tsv) · [`t224-namespace-mirror`](../evidence/t224-namespace-mirror.2026-10-15-p224.tsv)

### 🆕 🔴 `T224-V1` — the sentence that forks the Moodle AI market

> **`CARE: Currently, plugins requiring the moodle AI subsystem are not compatible with the AI manager and vice versa.`**
> — [`bycs-lp/moodle-local_ai_manager`](https://github.com/bycs-lp/moodle-local_ai_manager) `README.md`, `5 354` B, read first-hand `2026-10-15`

🔴 **Two AI subsystems, one LMS, no interoperability:**

| | **A — core `core_ai`** | **B — `local_ai_manager`** |
|---|---|---|
| origin | 🟢 ships **with Moodle `4.5`** | a plugin by **`ISB Bayern`** *(Bavarian state institute)* |
| Moodle floor | 🟢 **`4.5`** | 🔴 **`5.0`** *(`supported [500, 502]`)* |
| seam | `aiprovider_*` | `aitool_*` + `aipurpose_*` |
| multi-tenant | 🔴 no | 🟢 **yes, and that is its stated reason to exist** |
| per-role quotas, purpose-level routing, teacher visibility of student prompts | 🔴 no | 🟢 **yes** |
| self-hosted inference | 🆕 [`rabser/moodle-aiprovider_openwebui`](https://github.com/rabser/moodle-aiprovider_openwebui) · [`lmscloud-io/moodle-aiprovider_openaicompatible`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible) | **Ollama**, plus 🟢 **`Telli`, a service for German schools** |

🟡 **This is the first question to ask in a Moodle AI engagement and it is architectural, not cosmetic.** 🔴 **A client on `4.5` can have **A** today and cannot have **B** without a major-version upgrade.** 🔴 **A ministry or university system that needs per-tenant quotas needs **B**, and inherits the `5.0` floor plus a `MATURITY_BETA` frontend *(`local_ai_injection` `0.3`)*.** 🟢 **Recipe and decision gate: [`compose/patterns.md`](../compose/patterns.md) `P224-R1`.**

### 🆕 🟢 `T224-V2` — a state-procured inference endpoint is already a first-class provider

🟢 **Column B lists `Telli` — *"Service for German schools"* — beside OpenAI, Gemini, Vertex Imagen and Ollama.** 🔵 **An EMEA data-residency requirement does not need a custom integration here; it needs a provider selection in a shipping, `GPL-3.0-or-later` plugin.** 🟡 **That is a materially shorter EMEA sovereignty path than this KB has previously carried, and it is the kind of claim a procurement officer can verify in the plugin's own settings page.**

### 🟢 Platform licensing, re-read under this pass's census

- 🔴 **`openeducat/openeducat_erp` — the shelf's most-mentioned GNU platform row — is `LGPL-3.0-only` under Odoo's grammar**, and in a `RANGE-CONFLICT` with its own file header. 🟡 **For a customisation engagement, assume `only` and say so in the SOW.** 🔵 **[`repos/foundations.md`](../repos/foundations.md), `ACTION RU` / `ACTION RV`.**
- 🟢 **`ERPNext` — `GPL-3`.** 🔴 **`Twenty` — `BSL-1.1`, which is NOT an OSI grant**, recorded here so that no later pass promotes it into a permissive recipe.
- 🔴 **Unchanged and still load-bearing: the `oat-sa` exclusion.** `GPL-2.0-only` across all `6` TAO/QTI rows keeps the assessment supply out of every GPLv3 LMS on these shelves *(Moodle, Chamilo, ILIAS, Gibbon)*; the route that works is LTI 1.3 — `P222-R1`.

## Pass 223 — 2026-10-15 — `0` NEW PLATFORM ROWS, AND THE PLATFORM TIER'S COMPLIANCE DATE WAS WRONG ON THE PAGE THAT SELLS IT

🔵 **`0` new platform rows. `0` platform grants changed.** 🔴 **What changed is the sentence a studio says to a Moodle, Open edX or Chamilo client about *when* the EU obligation bites.**

### 🔴 `T223-V1` — the two clocks a platform engagement runs on

🟢 **Any AI layer bolted onto an LMS for an EU client now has two dated obligations, and this KB had them collapsed into one:**

| obligation | date | what it touches in a platform build |
|---|---|---|
| **Article `50`** transparency | 🟢 **in force `2026-08-02`** | the learner-facing surface: a disclosure that the tutor/grader is a machine, on every AI activity in the course |
| **Annex III** stand-alone high-risk | 🟡 **`2027-12-02`** | admissions, assessing learning outcomes, monitoring during tests — i.e. the **grading and proctoring** plug-ins, not the chat ones |
| embedded-in-product high-risk | 🟡 **`2028-08-02`** | AI shipped as part of a regulated product |
| prohibitions *(emotion inference in education)* | 🔴 **since `2025-02-02`** | rules out an entire proctoring feature class, today |

🔵 **Practical effect on the platform tier:** an **AI chat activity** *(course-scoped, disclosed)* is a `2026` sale; an **AI grader or proctor** is a `2027` conformity programme with a `2026` design phase. 🟢 **Same platform, same client, two SOWs — and the second one is where the margin is.**

🔵 **Nothing on the platform shelf changes technically: [`lmscloud-io/moodle-aiprovider_openaicompatible`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible) remains the row that makes a self-hosted model usable inside Moodle, and p222's finding stands — the TAO/`oat-sa` assessment tier is `GPL-2.0-only` and must stay outside a GPLv3 LMS, over LTI `1.3`.**

### 🟡 `T223-V2` — the sovereignty argument now has a Council-level source

🟢 **Council of the EU conclusions `ST-9003/2026` *(`11` May `2026`)* reportedly press for teacher AI literacy and for reduced dependence on AI tools built outside Europe.** 🔴 **`SNIPPET-ONLY` — `data.consilium.europa.eu` is unreachable from this session.**

🔵 **If it holds, it converts the self-hosted stack from a cost argument into a policy argument in EMEA, exactly as sovereignty requirements already do in APAC. 🟢 The platform tier is ready for it: a GPLv3 LMS + a self-hosted OpenAI-compatible provider + local inference is an assembly, not a build.**

## Pass 222 — 2026-10-15 — THE ASSESSMENT TIER CANNOT GO INSIDE THE LMS TIER: `6` OF `6` `oat-sa` PLATFORMS ARE `GPL-2.0-only` AND EVERY MAJOR OPEN-SOURCE LMS HERE IS GPLv3

🔵 **`1` new platform row.** 🔴 **And a structural finding about the shelf: the two layers a studio most often wants to combine — an LMS and an assessment engine — are on opposite sides of a licence incompatibility that no cell on this page recorded until p221.**

🔵 **Evidence:** [`rq-gpl2-only-exclusion`](../evidence/rq-gpl2-only-exclusion.2026-10-15-p222.tsv) · [`rp-bound-sweep`](../evidence/rp-bound-sweep.2026-10-15-p222.tsv) · **Instrument:** [`p222-ecosystem-bound-grammar`](../compose/code/p222-ecosystem-bound-grammar/README.md) — `blocks_gpl3_host()`

### 🆕 🔴 `P222-V1` — the platform compatibility map, read first-hand

| platform | tier | licence as read | bound | may its code enter a **GPLv3** host? |
|---|---|---|---|---|
| **Moodle** | LMS | `GPL-3.0-or-later` *(mandated plugin header)* | 🟢 `or-later` | 🟢 **it IS the host** |
| **Chamilo** [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | LMS | 🆕 `composer.json`: **`"GPL-3.0-or-later"`** *(`8 294` B)* | 🟢 `or-later` | 🟢 host |
| **ILIAS** [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | LMS | 🟡 `composer.json`: **`"GPL v3"`** — 🔴 **not a valid SPDX expression** | 🔴 `unreadable` | 🟡 host, but the declared field is unusable by a scanner |
| **Gibbon** [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | SIS/LMS | 🆕 `composer.json`: `"GPL-3.0"` *(`3 097` B)* | 🟡 `unspecified` | 🟡 host |
| **Open edX** via **Tutor** [`overhangio/tutor`](https://github.com/overhangio/tutor) | distribution | 🆕 `pyproject.toml`: **`license = {text = "AGPL-3.0-only"}`** | 🔴 **`only`** | 🔴 **see `P222-V2`** |
| **Frappe LMS** [`frappe/lms`](https://github.com/frappe/lms) | LMS | 🆕 `package.json`: **`"AGPL-3.0-or-later"`** *(`875` B)* | 🟢 `or-later` | 🟢 |
| **OpenEduCat** [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | education ERP | 🆕 module manifest `'LGPL-3'` **vs** module header *"or (at your option) any later"* | 🔴 **`RANGE-CONFLICT`** | 🟡 LGPL links either way; the conflict bites on *modifying* it |
| **TAO** [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | assessment | 🆕 `composer.json`: **`["GPL-2.0-only"]`** | 🔴 **`only`** | 🔴 **NO** |
| **TAO QTI test** [`oat-sa/extension-tao-testqti`](https://github.com/oat-sa/extension-tao-testqti) | assessment | 🆕 **`["GPL-2.0-only"]`** | 🔴 **`only`** | 🔴 **NO** |
| **QTI-SDK** [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) | assessment lib | 🆕 **`["GPL-2.0-only"]`**, package name `qtism/qtism` | 🔴 **`only`** | 🔴 **NO** |
| **LTI 1.3 core** [`oat-sa/lib-lti1p3-core`](https://github.com/oat-sa/lib-lti1p3-core) | integration lib | `"GPL-2.0-only"` *(p221)* | 🔴 **`only`** | 🔴 **NO** |
| **Elgg** 🆕 [`Elgg/Elgg`](https://github.com/Elgg/Elgg) | social learning | 🆕 **`MIT` OR `GPL-2.0`** — DUAL, read first-hand: `master/LICENSE.txt` `17 173` B, `sha256`₁₂ `7188c83d8764` <!--corrected--> | 🟡 **dual** *(`/mod` plugins `GPL-2.0-only`)* | 🟢 **YES, under `MIT`** |

🔴 **So the shelf has a hard seam.** The LMS tier is GPLv3-family; the whole `oat-sa` assessment tier plus Elgg is `GPL-2.0-only`. 🔵 **`LGPL` rows are the exception and that is deliberate in the instrument: `blocks_gpl3_host()` returns `False` for `LGPL` at any version, because LGPL is written to be *linked* into a differently licensed host.**

### 🆕 🟢 `P222-V2` — the seam is not a dead end, and the detour is already standard practice

🟢 **`GPL-2.0-only` constrains *combining code into one work*. It does not constrain *talking to a separate program over a protocol*.** The sector's own answer is already on these shelves:

- 🟢 **Run TAO as its own deployment** and launch it from the LMS over **LTI 1.3**. Nothing links; two programs, one protocol. 🔵 **The LTI tool side can use a permissive library instead of `oat-sa`'s: [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) is `Apache-2.0`, and [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) is `BSD-3-Clause` *(both confirmed to ship their grant, see [`repos/foundations.md`](../repos/foundations.md) `P222-B`)*.**
- 🔴 **What is NOT available: a Moodle plugin that bundles QTI-SDK.** 🟡 **Any SOW proposing one is unbuildable as written, and this is the first pass on which this page can say so with a first-hand citation per row.**
- 🟡 **Tutor's `AGPL-3.0-only` matters in a different way.** AGPL-3 is the strongest reciprocal grant here and `only` removes the forward escape. 🔵 **For a hosted Open edX engagement, the practical consequence is that *network interaction* triggers source provision and there is no option to move to a later AGPL — so plan the source-offer process into the engagement rather than treating it as a licence footnote.**

### 🆕 🟢 `P222-V3` — the new platform row, and it is the one that removes a vendor dependency

| platform | licence | channel | why it is on this page |
|---|---|---|---|
| 🆕 🟢 [`lmscloud-io/moodle-aiprovider_openaicompatible`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible) | 🟢 **`GPL-3.0-or-later`** — grant + `@license` tag agree | `main/version.php` | 🟢 **Moodle `4.5`+ ships a core **AI subsystem** with pluggable providers, and every provider on these shelves until now pointed at a proprietary vendor API. This one targets any **OpenAI-compatible** endpoint, so the same Moodle build can run against a self-hosted model.** 🔵 **This is the concrete escape from `ACTION RB`'s `UNKNOWN-PLUS-TOS` finding: the licence cell stops being the wrong question when there is no vendor API in the path** |

🟢 **Paired with 🆕 [`mebis-lp/moodle-local_ai_manager`](https://github.com/mebis-lp/moodle-local_ai_manager)** *(`GPL-3.0-or-later`, read at `main/version.php`)*, which adds **per-tenant** provider selection, quotas and purpose scoping on top. 🔵 **Both are GPLv3-family, so both may live inside the Moodle tree — unlike the assessment tier above.**


## Pass 221 — 2026-10-15 — THE PLATFORM ROWS ARE THE ONES WHERE AN UNBOUNDED `GPL` CELL COSTS MONEY, BECAUSE A PLATFORM IS WHAT YOU EXTEND

🔵 **`0` new platform rows.** 🔴 **But three carried platform rows changed state on a file-level read, and one of them changes what can be built on top of it.**

🔵 **Evidence:** [`rh-file-level-range`](../evidence/rh-file-level-range.2026-10-15-p221.tsv) · **Instrument:** [`p221-licence-version-range`](../compose/code/p221-licence-version-range/README.md)

### 🆕 🔴 `P221-D` — `themeum/tutor`: three channels, three answers, on a platform with `129` stars-tier adoption

🔴 **Tutor LMS is a WordPress LMS plugin — the shape a studio extends by writing more PHP inside the same tree. Read `2026-10-15`:**

| channel | reading, verbatim | grant |
|---|---|---|
| `master/LICENSE` *(`35 149` B)* | the GPLv3 text | 🟡 `GPL-3.0`, unbounded |
| 🆕 🔴 `master/tutor.php` l.`12` *(`1 484` B)* | **`* License: GPLv2 or later`** | 🔴 **`GPL-2.0-or-later`** |
| 🆕 🔴 `master/readme.txt` l.`9`–`10` *(`42 450` B)* | **`License: GPLv3`** / `License URI: https://www.gnu.org/licenses/gpl-3.0.html` | 🔴 **`GPL-3.0`, unbounded** |

🔴 **`tutor.php` is the plugin header WordPress itself parses, and `readme.txt` is the file wordpress.org publishes from. Both are `PRESCRIBED-CHANNEL` files, both are mandatory, and they disagree with each other.** 🔵 **`GPLv2 or later` and `GPLv3` are not the same grant: the first permits distribution under v2, the second does not. A derivative work built on this platform inherits whichever one actually governs, and the repository does not say which.**

🟢 **Corrected on the shelf to `GRANT-CONFLICT` with all three channels recorded. 🔴 This is not a question a script can close — it goes to counsel with the three readings attached.**

### 🆕 🟡 `P221-E` — `gocodebox/lifterlms`: the control that exonerates this KB

🟡 **The sibling WordPress LMS platform, read the same way, comes back consistent and **unbounded at source**:**

| channel | reading | grant |
|---|---|---|
| `LICENSE` *(`35 141` B, `trunk`, `6ff84cf`)* | GPLv3 text | `GPL-3.0` |
| 🆕 `master/lifterlms.php` l.`18`–`19` *(`1 844` B)* | `* License: GPLv3` / `* License URI: https://www.gnu.org/licenses/gpl-3.0.html` | `GPL-3.0`, unbounded |

🟢 **`BOTH-UNSPECIFIED`, and that verdict matters: the shelf cell is a faithful copy of an ambiguous source. 🔵 The right record is `UNSPECIFIED-AT-SOURCE` plus a question for the maintainer — NOT a KB defect, and not something to "fix" by inventing a bound.**

### 🆕 🟡 `P221-F` — `h5p/h5p-php-library`: the platform whose own code validates *content* licences and declares none for itself

🔴 **`master/h5p.classes.php`, `196 920` B — the largest file read in this pass or the last — carries no licence notice.** 🟢 **What it does carry is a licence *validator* for learning objects:**

```php
'license' => '/^(CC BY|CC BY-SA|CC BY-ND|CC BY-NC|CC BY-NC-SA|CC BY-NC-ND|CC0 1\.0|GNU GPL|PD|ODC PDDL|CC PDM|U|C)$/',
'licenseVersion' => '/^(1\.0|2\.0|2\.5|3\.0|4\.0)$/',
'licenseExtras' => '/^.{1,5000}$/s',
```

🔵 **Recorded because it is the sector's own confirmation of this pass's headline: H5P models a content licence as a **family plus a separate `licenseVersion` field**, because it knows a family alone is not a grant. 🔴 Its own code file carries neither.** 🟢 **The platform's cell stays `GPL-3.0` from `LICENSE.txt` *(`35 146` B)*, now marked `FILE-SILENT`.**

### 🆕 🟡 `P221-G` — the platform-extension rows re-read, and the `-or-later` that was always there

🟢 **Four Moodle extension rows and `bigbluebutton` all resolve to an `-or-later` grant their shelf cell did not carry:**

| platform row | cell was | file says | now |
|---|---|---|---|
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) *(web conferencing, the sector's default)* | `LGPL-3.0` | `MeetingService.java` *(`71 514` B)*: *"either version 3.0 of the License, or (at your option) any later version"* | 🟢 **`LGPL-3.0-or-later`** |
| [`willianmano/moodle-theme_moove`](https://github.com/willianmano/moodle-theme_moove) | `GPL-3.0` | `version.php` *(`1 572` B)* | 🟢 **`GPL-3.0-or-later`** |
| [`valentineus/moodle-webhooks`](https://github.com/valentineus/moodle-webhooks) | `GPL-3.0` | `version.php` *(`1 135` B)* | 🟢 **`GPL-3.0-or-later`** |
| [`eLearning-BS23/moodle-quizaccess_proctoring`](https://github.com/eLearning-BS23/moodle-quizaccess_proctoring) | `GPL-3.0` | `version.php` *(`1 122` B)* | 🟢 **`GPL-3.0-or-later`** |
| [`moodlehq/moodle-enrol_oneroster`](https://github.com/moodlehq/moodle-enrol_oneroster) | `GPL-3.0` | `version.php` *(`1 249` B)* | 🟢 **`GPL-3.0-or-later`** |

🔵 **`-or-later` is the permissive direction, so none of these is a new risk. The point is the opposite: these cells were *understating* the grant, and a studio reading `GPL-3.0` would have assumed it could not carry the component forward.**

### 🆕 🔴 `P221-H` — and the one platform-adjacent row where the bound is a hard stop

🔴 **[`oat-sa/lib-lti1p3-core`](https://github.com/oat-sa/lib-lti1p3-core) is `GPL-2.0-only` — *"under version 2 of the License (non-upgradable)"* in `src/Message/LtiMessage.php` *(`3 800` B)*, and `"license": "GPL-2.0-only"` in `composer.json`.**

🔴 **Consequence, stated for an SOW: this LTI 1.3 library may NOT be combined with a GPLv3 platform. Moodle is `GPL-3.0-or-later`. So the one LTI library on these shelves with the strongest institutional pedigree *(Open Assessment Technologies, the TAO people)* is the one that cannot go into a Moodle build** — and the shelf published it as a bare `GPL-2.0`, which reads as permissive-enough to anyone who does not know the `-only` / `-or-later` distinction.

🟢 **For a Moodle engagement the substitutes already on these shelves:** [`celtic-project/LTI-PHP`](https://github.com/celtic-project/LTI-PHP) *(`LGPL-3.0`, `BOTH-UNSPECIFIED` — ask first)* and [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) *(`Apache-2.0` in `composer.json`, `FILE-SILENT`)*. 🔵 **For an Open edX engagement the question does not arise the same way — `edx-platform` is `AGPL-3.0`, which is also v3.**

## Pass 220 — 2026-10-15 — THE OFFLINE STACK AND THE MOODLE AI LAYER: `1` NEW PLATFORM ROW AND `4` CUSTOMISABLE PLUGINS ON TOP OF ONE ALREADY HERE

🔵 **`1` new platform row.** 🟢 **And the Moodle layer on this shelf stops being *"Moodle, plus write your own AI"*: there is now a verified plugin category to customise instead of a greenfield build.**

### 🆕 🟢 New platform row — the offline-first education server

| platform | licence | what it is | what a studio customises |
|---|---|---|---|
| 🆕 🟢 **Project NOMAD** — [`Crosstalk-Solutions/Project-NOMAD`](https://github.com/Crosstalk-Solutions/Project-NOMAD) | 🟢 **`Apache-2.0`** *(`LICENSE` `10 779` B + `package.json`; `v1.35.1`)* | A Docker-orchestrating **Command Center** UI + API that installs and manages a bundle: **Kolibri** *(Khan Academy courses with progress tracking)*, **Kiwix** *(offline Wikipedia, medical references, ebooks)*, **Ollama** or any OpenAI-compatible endpoint *(LM Studio, `llama.cpp`)* for AI chat over an uploaded document base, ProtoMaps, CyberChef, FlatNotes | 🟢 The *"Supply Depot"* catalogue takes **arbitrary custom containers**, so a studio's own service drops in beside the bundled ones without forking NOMAD. 🟢 Content curation *(ZIM selection, Kolibri channels)* is configuration, not code |

🔵 **Where it belongs on this shelf:** every other platform row here — Moodle, Canvas, Open edX, Sakai, OpenOLAT — assumes a reachable server and a reachable model. 🟢 **NOMAD is the first that assumes neither, and it is `Apache-2.0`, so it can be rebranded and resold.** 🔴 **Constraints for a proposal: Debian-based hosts only *(Ubuntu `26.04` LTS recommended, `24.04` LTS and Debian `12` supported; Windows via WSL2)*, ~`5` GB disk and <`1` GB RAM for the core before any content, and its headline install is a `curl | sudo bash`. 🟢 Use the documented Docker-Compose route in an SOW instead.**

🟢 **Two of the bundled upstreams were read first-hand this pass and are both `MIT`: [`learningequality/kolibri`](https://github.com/learningequality/kolibri) and [`ollama/ollama`](https://github.com/ollama/ollama).** 🟡 **[`kiwix/kiwix-tools`](https://github.com/kiwix/kiwix-tools), [`kiwix/libkiwix`](https://github.com/kiwix/libkiwix) and [`protomaps/basemaps`](https://github.com/protomaps/basemaps) have NO root `LICENSE` — three more `PERMISSIVE-MANIFEST` rows, unresolved.** 🔵 **NOMAD orchestrates rather than vendors them, so for a resale engagement the licence question is per-container, not per-NOMAD. Registered as part of `ACTION RH`.**

### 🆕 🟢 The Moodle AI plugin layer — customise, do not rebuild

🟢 **Moodle has been the best-governed platform row on this shelf for `200`+ passes, and the gap was always *"and then you build the AI part yourself."* Four verified plugins close it:**

| plugin | licence | maturity | the build it replaces |
|---|---|---|---|
| 🆕 🟢 [`saylordotorg/moodle-local_ai_course_assistant`](https://github.com/saylordotorg/moodle-local_ai_course_assistant) *(SOLA)* | 🟢 `GPL-3.0-or-later` | 🟢 **`MATURITY_STABLE`, `release 7.8.9`, in production at Saylor** | an AI learning coach — **start here**, it is the only row of the four with a production deployment behind it |
| 🆕 🟢 [`bycs-lp/moodle-local_ai_manager`](https://github.com/bycs-lp/moodle-local_ai_manager) + [`bycs-lp/moodle-block_ai_chat`](https://github.com/bycs-lp/moodle-block_ai_chat) | 🟢 `GPL-3.0-or-later` *(read from `version.php` this pass — these rows were `CLAIMED-IN-PROSE` until now)* | 🟢 `MATURITY_STABLE`, `release 5.1.1` / `3.3` | the **provider/quota layer**: API connections to AI services, per-role request limits, usage accounting. 🔵 This is the piece studios keep rewriting |
| 🆕 🟢 [`Limekiller/moodle-block_openai_chat`](https://github.com/Limekiller/moodle-block_openai_chat) | 🟢 `GPL-3.0-or-later` | 🟢 `MATURITY_STABLE`, `release 4.0.2` | a course-level chat block |
| 🆕 🟢 [`yedidiaklein/moodle-local_aiquestions`](https://github.com/yedidiaklein/moodle-local_aiquestions) | 🟢 `GPL-3.0-or-later` | 🟢 `MATURITY_STABLE` | question generation from course text |
| 🆕 🔴 [`microsoft/moodle-ai-assistant`](https://github.com/microsoft/moodle-ai-assistant) | 🔴 **`MIT` at root, `GPL-3.0-or-later` in `local/aichat/version.php`** | 🔴 `MATURITY_ALPHA`, `release 0.1.0` | an Azure-OpenAI-backed widget + RAG over course content. 🔴 **Do not put it in an SOW until the grant question is answered by its holder** |

🔴 **And the counter-measure sits in the same tree.** [`adamjenkins/moodle-local_nomoreai`](https://github.com/adamjenkins/moodle-local_nomoreai) *(p219, `GPL-3.0-or-later`)* exists to **block** exactly these integrations when they act for a student. 🟢 **A Moodle AI proposal that does not mention it is incomplete: the institution may install both, and `Detect only` mode means they can measure your traffic for a term before deciding.**

### 🆕 🔴 A platform-adjacent correction a studio must not inherit

🔴 **[`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) is the standard route on this shelf for getting xAPI statements out of legacy SCORM courses, and this KB has carried it as `Apache-2.0`.** 🔴 **The files it tells you to drop into **every SCO** carry a custom ADL grant with a **non-disparagement clause** and **CC BY-SA 3.0** — share-alike, on every course package delivered.** 🔵 **The `Apache-2.0` text is real and sits in the `README`; it is not what travels with the bytes. Full reading in [`agents/top.md`](../agents/top.md) `T220-1`.**

### 🆕 🟡 The vendor-terms column this shelf has never had

🟢 **`ACTION RB`: `19` rows across the `8` shelves have a line naming a proprietary platform — Blackboard Learn, PowerSchool, Google Classroom, Brightspace, Instructure, Clever, Anthology, Workday.** 🔴 **For a closed-API integration the licence cell answers the wrong question: what governs is the vendor's API terms of service, plus whatever tenancy agreement the institution signed. This shelf records that for no row.** 🔵 **`UNKNOWN-PLUS-TOS` enters the vocabulary; the field itself is `ACTION RK`.**

## Pass 219 — 2026-10-15 — `0` NEW PLATFORM ROWS, AND A DISTRIBUTION CHANNEL FOR THE MOODLE TIER THAT THIS KB HAS NEVER READ

🔵 **`0` new platform rows.** 🟢 **`ACTION QV` — registered here at `T218-6` — is DISCHARGED, and the answer reorders `ACTION PH` for a different reason than the one predicted.**

🔵 **Evidence:** [`qv-upstream-reciprocity`](../evidence/qv-upstream-reciprocity.2026-10-15-p219.tsv) · [`qw-constrained-trending`](../evidence/qw-constrained-trending.2026-10-15-p219.tsv)

### 🆕 🟢 `ACTION QV` closes — the platform tier is where the answer came from

🔴 **`T218-6`, written on this shelf, asked whether the `47` genuine unknowns had ever been checked for a reciprocal upstream. They had not. They have now.**

🟢 **`6` of `47` name a reciprocal upstream; `4` of `47` are installed INTO one.** 🟢 **Limb `1` fires on both readings.** 🔴 **And every one of the `4` is a derivative of a platform already in this file's tier table — Moodle, WordPress, Magento 1.**

🔵 **So the platform tier turns out to carry the answer for the agent shelf:** 🟢 **if a row is a plugin for a platform listed here, the platform's own packaging convention says where its licence lives, and that is cheaper than asking its maintainer anything.**

| platform *(already in this file's tier table)* | its reciprocity | where its ecosystem puts the licence |
|---|---|---|
| **Moodle** | `GPL-3.0-or-later` | 🟢 `version.php` + per-file docblocks *(`@license`)* — and the plugin directory REQUIRES `GPL-3.0-or-later` |
| **WordPress** *(Tutor LMS, LearnPress)* | `GPL-2.0-or-later` | 🟢 `readme.txt` header + the main plugin file's `License:` line |
| **Magento 1 / OpenMage** | 🔴 `OSL-3.0` + `AFL-3.0`, **network-reciprocal** | 🟡 `composer.json` — 🔴 **but check `"name"`: a vendored fork's manifest describes the UPSTREAM** |
| **Open edX** | `AGPL-3.0` | `setup.py` / `pyproject.toml` |
| **Sakai · Opencast** *(Apereo)* | 🟢 `ECL-2.0` — **NOT reciprocal** | `pom.xml`; p216 read it at clause level |

🔴 **The `ECL-2.0` row is in that table as a control. Apereo is an LMS family and it is Apache-derived — treating "education platform" as a proxy for "copyleft" would be wrong on `8` of `13` Apereo rows *(p216)*.**

### 🆕 🔴 A third risk class this file does not record, and `3` rows sit in it

🟡 **`3` of the `47` call a PROPRIETARY SaaS platform over its vendor API:** [`P1ckle3/blackboard-mcp`](https://github.com/P1ckle3/blackboard-mcp), [`karkarkins/BlackboardAssistantMCP`](https://github.com/karkarkins/BlackboardAssistantMCP), [`ruud0/aula-virtual-mcp`](https://github.com/ruud0/aula-virtual-mcp) — all three against **Blackboard Learn**.

🔴 **For these rows the licence question is nearly beside the point.** 🟢 **No reciprocity reaches them — Blackboard is not open source and they derive nothing from it.** 🔴 **What governs them is the vendor's API terms of service: rate limits, permitted use, whether an institution's contract allows a third-party client at all, and whether the vendor may withdraw the endpoint.** 🔴 **This KB records none of that for any row, on any shelf.**

🔵 **So a studio reading a `UNKNOWN` cell on one of those `3` is being pointed at the wrong risk.** 🆕 **`UNKNOWN-PLUS-TOS`, and `ACTION RB` registered: the API-terms axis, for every row on these shelves that calls a proprietary platform — which is more than these `3`.**

### 🆕 🟡 The Moodle plugin directory — a distribution channel with its own licence rule, never read here

🟢 **Every plugin in the Moodle plugin directory is `GPL-3.0-or-later`: Moodle requires it as a condition of listing.** 🔵 **That makes the directory the one platform channel on this shelf where the licence is answered by the channel itself, before any repository is opened.**

🔴 **`7` AI plugins were named in it this pass. `grep` over the `8` client-facing shelves returns `0` for all `7` slugs.** 🔴 **And `moodle.org` → `ENOTFOUND` from this session, so `6` of the `7` cannot be verified here at all — see [`agents/trending.md`](../agents/trending.md) for the table and [`ACTION RA`](../intel/open-gaps.md).**

🔴 **One of the `7` is the reason a channel rule is not a licence read:** 🟡 **`local_assign_ai` is itself `GPL` by the directory's rule, and *"fully dependent on the DataCurso AI Provider plugin … will not function until the provider is installed, configured and properly licensed."*** 🔴 **A `GPL` plugin that cannot run without a proprietary paid dependency is not a thing a studio can build on, and no licence field on either one says so.**

## Pass 218 — 2026-10-15 — THE PLATFORM TIER IS UNCHANGED FOR A THIRD PASS; THE OWNER-LEVEL SHORTCUT THAT WOULD HAVE CHANGED TWO CELLS WAS TESTED AND IS WRONG

🔵 **`0` new platform rows.** 🟢 **`ACTION QR` applied to the platform-adjacent rows; the `alfredang` owner census completed.** 🔵 **Evidence:
[`evidence/owner-level-refusal-probe.2026-10-15-p218.tsv`](../evidence/owner-level-refusal-probe.2026-10-15-p218.tsv),
[`evidence/grant-state-schema.2026-10-15-p218.tsv`](../evidence/grant-state-schema.2026-10-15-p218.tsv).**

### 🆕 🟢 `P218-V1` — the `ECL-2.0` platform tier, re-confirmed, no drift

| platform | repo | grant | what it is | install base |
|---|---|---|---|---|
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`** | Full LMS/VLE in Java — the reference `ECL-2.0` codebase | 🟢 **Global** |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **`ECL-2.0`** | Automated lecture capture and video distribution at scale | 🟢 **EMEA**-led |

🟢 **Control re-run this pass: `sakai`'s `LICENSE` serves `200` over `raw.githubusercontent.com`, fourteenth consecutive confirmation.** 🔵 **`ECL-2.0` remains `Apache-2.0` copyright terms with a narrowed `§3` patent grant — the clause a studio puts in a contract, quoted in full at `P216-V2`.**

### 🆕 🟢 `P218-V2` — the correction p217 wrote at l.`25` and did not carry to l.`2182`

🔴 **p217's own headline was the propagation defect. It published the `alfredang/AI-LMS-TMS` correction at l.`25` of THIS FILE and left the contradicting cell standing at l.`2182`, `2 157` lines below it, still reading *"NO GRANT"*.**

🟢 **The correct cell, for the record:**

| repo | state | why it is not *"no grant"* |
|---|---|---|
| [`alfredang/AI-LMS-TMS`](https://github.com/alfredang/AI-LMS-TMS) | 🔴 **`GRANT-REFUSED`** | `README` l.`703`: *«This project is **proprietary software** developed by Tertiary Infotech Pte Ltd. **All rights reserved**.»* 🔴 An absence can be fixed by asking. 🔴 **A refusal cannot** |

🔵 **The cell sits inside `## Pass 187 — 2026-10-14` and is therefore corrected here, not rewritten — but see [`repos/foundations.md`](foundations.md) `P218-F3`: the instrument p216 used to certify that *"`0` live stale cells"* exist returns the WRONG enclosing heading on `intel/market.md`, and this file carries `9` shadowing level-2 headings of its own.**

### 🆕 🟢 `P218-V3` — the owner-level shortcut, tested before a cell was written, and REFUTED

🔴 **The tempting inference: `AI-LMS-TMS` is refused, so its siblings under the same owner — and the same operator credit, *Tertiary Infotech Academy Pte. Ltd.* — are refused too. Two cells, free, no new reading.** 🟢 **It was tested instead.**

| repo | `README` | licence prose | state | what it is |
|---|---|---|---|---|
| [`alfredang/AI-LMS-TMS`](https://github.com/alfredang/AI-LMS-TMS) | `57 174` B | 🔴 refusal at l.`703` | 🔴 **`GRANT-REFUSED`** | `WSQ`/`SkillsFuture`/`SSG` LMS+TMS. 🟡 Still the best `SkillsFuture` documentation on these shelves |
| [`alfredang/ai-mms`](https://github.com/alfredang/ai-mms) | `30 558` B | 🟢 **`0` hits** on `licen`\|`proprietary`\|`all rights reserved` | 🟡 **`UNKNOWN`** | Course-registration + LMS on **`OpenMage LTS v20.12.0`** |
| [`alfredang/ai4kids`](https://github.com/alfredang/ai4kids) | `13 228` B | 🟢 **`0` hits** | 🟡 **`UNKNOWN`** | Kids AI portal; live site + App Store `id6780267161` + Play `sg.com.tertiarycourses.ai4kids` |

🔴 **One owner, `3` repositories, `2` states. The refusal does not propagate, and the shortcut would have put `2` wrong cells on this shelf.** 🟢 **An operator credit is neither a grant nor a refusal — that is precisely the distinction the inference erases.** 🔵 **`ACTION QK`'s rule, run *before* the cell rather than swept up after it.**

### 🆕 🔴 `P218-V4` — the thing on `ai-mms` worth more than its missing licence

🟢 **l.`5` carries an `OpenMage LTS v20.12.0` badge; l.`35` describes a *"production-grade course-registration and learning-management platform built on OpenMage 1.x (Magento 1 LTS)"*, with every product modelled as a **course** — instructor-led trainings, workshops, certifications, no physical inventory.**

🔴 **OpenMage inherits Magento 1's **`OSL-3.0`** — network-reciprocal, not permissive.** 🔵 **So:**

- 🔴 **An ungranted repository sitting on a RECIPROCAL upstream.** 🔴 **If the author granted MIT tomorrow, the derivative question would survive it.**
- 🟢 **A studio evaluating `ai-mms` needs the upstream answer first, and the upstream answer is already known.**
- 🟡 **`T218-6`: the `47` genuine unknowns have not been checked for this shape at all. A repo with no grant of its own but a known-reciprocal upstream is a DIFFERENT procurement risk from a repo with no grant and a permissive upstream — and this KB records neither.** 🔵 **Registered as `ACTION QV`.**

### 🆕 🟡 `P218-V5` — the platform tier that returned, and why it stays off this shelf

🟢 **`open source platform education ERP CRM MIT Apache` ran verbatim.** 🔴 **It returned `0` platforms this shelf does not carry.** 🔵 **What came back:**

| returned | status |
|---|---|
| **OpenEduCat** *(on Odoo)*, **ERPNext** *(`GPL-3.0`)*, **Krayin**, **Huly**, **Apache OFBiz**, **Odoo** | 🟢 all already carried |
| 🆕 **`twentyhq/twenty`** *(CRM)* | 🔴 **`BSL-1.1`** — source-available with SaaS restrictions. 🔴 Not OSI, not education-sector. 🟡 **Recorded as a licence flag, not a row** |

🔴 **The query's own result is worth recording: it found *"no clear match for an education ERP/CRM platform under MIT or Apache licensing"*. 🟢 That is consistent with what this shelf has established over `218` passes — the education platform tier is `GPL`/`AGPL`/`ECL`, not permissive, and a studio's build-on-top decision has to start from reciprocity, not from a hunt for an MIT alternative that does not exist.**

## Pass 217 — 2026-10-15 — THE PLATFORM TIER IS UNCHANGED; THE WARNING TIER IS NOT: THE BEST `SkillsFuture` DOCUMENTATION ON THESE SHELVES IS PROPRIETARY AND HAS BEEN SINCE `pase 126`

🔵 **`0` new platform rows.** 🟢 **`ACTION QN` discharged against the platform-adjacent rows.**
🔵 **Evidence:
[`evidence/readme-prose-grant-probe.2026-10-15-p217.tsv`](../evidence/readme-prose-grant-probe.2026-10-15-p217.tsv).**

### 🆕 🟢 `P217-V1` — the two `ECL-2.0` platform rows, re-confirmed, no drift

| platform | repo | grant | what it is | region of install base |
|---|---|---|---|---|
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`** · `11 120` B | Full LMS/VLE in Java — the reference `ECL-2.0` codebase | 🟢 **Global** |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **`ECL-2.0`** · `11 340` B | Automated lecture capture and video distribution at scale | 🟢 **EMEA**-led |

🟢 **Control re-run this pass: `sakai`'s `LICENSE` serves `200` over `raw`, default branch
`master` at `38dc517…`.** 🔵 **`Opencast` remains the one layer no LLM framework provides, and
`ECL-2.0` remains permissive-with-a-narrower-patent-grant — the clause a studio puts in a
contract, quoted in full at `P216-V2`.**

### 🆕 🔴 `P217-V2` — the correction this shelf owes: `alfredang/AI-LMS-TMS` is not *"no grant"*, it is **refused**

🔴 **This shelf carries, at l.`2107`:**

> | 🔴 **[`alfredang/AI-LMS-TMS`]** | 🔴 **NO GRANT.** 🟡 But its `57 120` B README is the best
> description this KB holds of Singapore's `WSQ`/`SkillsFuture`/`SSG` assessment-and-funding
> regime …

🟢 **The `README`, read in full this pass *(`57 174` B at `HEAD`)*, says at l.`703`:**

> *«This project is **proprietary software** developed by Tertiary Infotech Pte Ltd.
> **All rights reserved**.»*

🔴 **So the correct cell is `GRANT-REFUSED`, not `NO GRANT`, and the difference is the whole
procurement answer:**

| if the cell says | an analyst does | cost |
|---|---|---|
| 🔴 *"NO GRANT"* | queues a licence probe, asks the author, waits | 🔴 wasted — it was answered on day one |
| 🟢 **`GRANT-REFUSED`** | reads it as a **specification**, writes nothing from it | 🟢 correct and immediate |

🟢 **The row keeps its value and changes its instruction: it is the best available description of
the Singapore `WSQ`/`SkillsFuture` regime, and it is a document to LEARN from, never a codebase to
fork, vendor or copy from.** 🔴 **Its sibling [`alfredang/ai-mms`](https://github.com/alfredang/ai-mms)
is grant-absent on the same author's account; neither is buildable.**

🟡 **And the finding is not new to this KB — `agents/trending.md` l.`19972` recorded
*"PROPIETARIO EXPLÍCITO"* at `pase 126` on `2026-10-05`. It did not reach this shelf because the
propagation gate greps English *(`T217-2`)*.**

### 🆕 🔴 `P217-V3` — the identity/rostering exemplar carries a restriction its licence name does not contain

🔴 [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) — cited on these shelves five
times as the Okta OIDC/SAML + OAuth 2.0 + **SCIM** rostering pattern worth copying — says, at
l.`456`–`458`:

> `## License` / **MIT — demo use only.**

🔴 **"Demo use only" is a field-of-use restriction. MIT contains no such term, and a permissive
name with a usage limit bolted on is not the permissive licence.** 🔴 **The complete tree
*(`89` files)* contains no licence file at all, so the `README` line is the entire grant.**
🟢 **Instruction: keep reading it as the reference ARCHITECTURE for SIS identity and rostering —
that is why it is cited — and 🔴 do not lift its code into a deliverable.**

### 🆕 🟡 `P217-V4` — the Moodle plugin tier is GPL, stated in prose only

🟡 **Two `ISB Bayern` Moodle plugins —
[`bycs-lp/moodle-block_ai_chat`](https://github.com/bycs-lp/moodle-block_ai_chat) and
[`bycs-lp/moodle-local_ai_manager`](https://github.com/bycs-lp/moodle-local_ai_manager) — carry
GNU GPL boilerplate inside the `README` *(`2024, ISB Bayern`, lead developer named)* and no
licence file.** 🟢 **This is the expected shape: a Moodle plugin inherits GPL by the host's
architecture, and the Moodle plugin directory requires it.** 🔵 **Recorded as
`PROSE-CLAIM-BARE` with the version unpinned in the title window — 🟡 *"GNU General Public
License as published by"* does not, in the matched window, say `v2` or `v3`, and for a Moodle
plugin that distinction decides compatibility with the host.** 🔴 **Registered as part of
`ACTION QT`; not resolved this pass.**


## Pass 216 — 2026-10-15 — THE PLATFORM TIER'S LICENCE FAMILY, RE-READ AT CLAUSE LEVEL: `ECL-2.0` IS PERMISSIVE ON COPYRIGHT AND NARROWER THAN `Apache-2.0` ON PATENTS, AND THAT IS THE SENTENCE A STUDIO HAS TO PUT IN A CONTRACT

🔵 **`0` new platform rows.** 🟢 **`ACTION QI` discharged.** 🔵 **Method:
[`compose/code/p216-ecl-sweep/`](../compose/code/p216-ecl-sweep/README.md); evidence:
[`evidence/ecl-classifier-blindspot.2026-10-15-p216.tsv`](../evidence/ecl-classifier-blindspot.2026-10-15-p216.tsv).**

### 🆕 🟢 `P216-V1` — the two platform rows that matter, with the grant read from the blob

🟢 **Both are `ECL-2.0`, both byte-identical to p200's readings, both confirmed today:**

| platform | repo | grant *(blob, bytes)* | what it is | region of install base |
|---|---|---|---|---|
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`** · `11 120` B | Full LMS/VLE in Java — the reference `ECL-2.0` codebase | 🟢 **Global** |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **`ECL-2.0`** · `11 340` B | Automated lecture capture and video distribution at scale | 🟢 **EMEA**-led *(German/European universities)* |

🔵 **Opencast remains the piece this KB has repeatedly noted that no LLM framework provides: if a
client wants AI over lecture VIDEO, the capture and distribution layer is this, and it is
permissive.**

### 🆕 🟢 `P216-V2` — the clause, quoted, because *"Apache-derived"* is not a procurement answer

🟢 **From `sakaiproject/sakai`'s `LICENSE` l.`9`–`13`, read today:**

```
The Educational Community License version 2.0 ("ECL") consists of the Apache
2.0 license, modified to change the scope of the patent grant in section 3 to
be specific to the needs of the education communities using this license.
```

🟢 **On the COPYRIGHT axis there is nothing to negotiate: `ECL-2.0` is `Apache-2.0`.** Permissive,
commercial use, sublicensable, no copyleft, OSI-approved *(`opensource.org/licenses/ECL-2.0`;
`OpenLRS`' blob prints `[OSI Approved License]` in its own header)*. 🔴 **The amendment is in the
patent grant, and it is written for universities** *(l.`95`–`100`)*:

> *"Any patent license granted hereby with respect to contributions by an individual employed by an
> institution or organization is limited to patent claims where the individual that is the author
> of the Work is also the inventor of the patent claims licensed, and where the organization or
> institution has the right to grant such license under applicable grant and research funding
> agreements."*

🔴 **Read plainly, and this is the operative difference for a deliverable:** where an `Apache-2.0`
contribution carries a patent peace from the contributor's employer, an `ECL-2.0` contribution
may not — **because a university's grant or research-funding agreement can withhold the right to
grant it.** 🔵 **Nothing about distribution changes. What changes is the patent warranty a studio
can offer on a Sakai or Opencast derivative**, and the honest position to take into a contract
review is: permissive to ship, with a patent indemnity that cannot be inherited from upstream and
must be priced or carved out.

🟢 **Credit where it belongs: p199 called this *"Apache-derived with an education-specific patent
clause"* and p200 quoted the scope and named the consequence.** 🔴 **p215 then registered
`ACTION QI` on the claim that the family had never been recorded, and this pass paid to rediscover
it.** 🔵 **The licence reading is `16` passes old and correct; the register was wrong.**

### 🆕 🟡 `P216-V3` — the learning-analytics tier is permissive and dead, and both halves must be said together

🟢 **`5` further `ECL-2.0` grant cells established first-hand this pass**, all in
`Apereo-Learning-Analytics-Initiative`: `OpenLRS` *(`11 087` B)*, `LearningAnalyticsProcessor`
*(`9 919`)*, `OpenDashboard-api` *(`9 919`)*, `OpenDashboard-legacy` *(`9 919`)*,
`lap-sakai-extractor` *(`11 087`)*, alongside `OpenLRW` *(`9 878`, un-drifted from p212)*.

🔴 **`6` of `6` repositories in that organisation are abandoned — youngest `6.6` years, oldest
`11.9`** *(measured at p109 from commit dates and at p111 independently from Travis dependence)*.
🔵 **So the platform-tier verdict is unchanged and now fully specified:**

| question a client asks | answer this KB can now give |
|---|---|
| *"Can we build on the open learning-analytics stack?"* | 🔴 **No maintained option on these shelves.** The `ECL-2.0` stack of the mid-`2010s` is permissive and unmaintained |
| *"Can we READ it?"* | 🟢 **Yes, and now lawfully and knowingly** — `ECL-2.0` on all six, grants read from the blob |
| *"What do we deploy instead?"* | 🔵 **Sakai or Opencast for the platform**, with the record layer built rather than adopted — and the segment gap stated to the client rather than papered over |

🟢 **`T216-3`: in education the licence axis and the maintenance axis are INDEPENDENT, and a
permissive grant on an abandoned repository is a citation right, not a build decision.** 🔴 **This
KB has twice promoted rows on grant alone; the pairing is now a standing rule on this shelf.**

### 🔵 Platforms re-confirmed, `0` cells changed

🟢 **`uPortal-Project/uPortal`, `Unicon/tool13demo` and
`Apereo-Learning-Analytics-Initiative/Larissa` are genuinely `Apache-2.0`** — classified
identically by p215's instrument and p216's, 🔵 **so the new ECL token does not over-fire on the
neighbouring Apache population: `3` of `3` controls hold.** 🟡 **`apereo/opencast` serves no blob
on `14` paths and is not the canonical slug; `opencast/opencast` is.**

---
*Pass 216 — `0` new platform rows, `1` licence family re-read at clause level, `5` grant cells added.*
## Pass 215 — 2026-10-15 — THREE PLATFORMS MOVE FROM *"UNUSABLE"* TO BUILDABLE, AND ONE `P971` INSTANCE IS WITHDRAWN

🔵 **`0` new platform rows.** 🟢 **`ACTION QD` re-read the `94` `ABSENT` rows through the
`git ls-tree` channel; `ACTION QG` then propagated every result into every current-state cell in
the same pass.** 🔵 **Method:
[`compose/code/p215-lstree-grant-recovery/`](../compose/code/p215-lstree-grant-recovery/README.md).**

### 🆕 🟢 `P215-V1` — the platform tier's corrections, and all four change a BUILD decision

| platform | 🔴 this shelf said | 🟢 established `2026-10-15` | what it unblocks |
|---|---|---|---|
| **Forma LMS** — [`formalms/formalms`](https://github.com/formalms/formalms) | 🔴 *"has no licence body"*, *"the default is exclusive copyright"* | 🟢 **`GPL-2.0`**, `html/license.txt` *(`18 346` B)*, plus the grant as a translated UI asset in **`10` languages** | 🟢 A corporate-training LMS that **ships its own licence in the procurement language** — Spanish and Portuguese included |
| **openSIS** — [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🔴 *"`GPL` by reference in the README ONLY"*, so *"a fork inherits an obligation whose text is not in the tree"* | 🟢 **`GPL-2.0` with the FULL BODY in-tree** at `docs/License.txt` *(`17 286` B)* | 🟢 **`P971` instance SEVEN is WITHDRAWN** — the terms do travel with the work |
| **Lumi** — [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) | 🔴 *"`NONE` / none / none found"* | 🟢 **`AGPL-3.0`** *(`package.json`, `3 600` B)* | 🔴 **Granted, and the WORST direction for a hosted build**: the H5P desktop authoring tool is network-copyleft |
| **School Management System** — [`ProjectsAndPrograms/…`](https://github.com/ProjectsAndPrograms/school-management-system) | 🔴 *"no grant on any path or manifest. Unusable at any quality"* | 🟡 **`MIT`** at `student_panel/LICENSE` *(`1 070` B)* | 🟡 Usable **with the provenance written down** — see the caveat below |

🔴 **The `Lumi` correction is the one to read carefully.** 🔵 **An `AGPL-3.0` grant is worse for a
client engagement than no grant found, because *"no grant"* stops a build at the proposal while
*"`AGPL-3.0`"* can pass an unaware reviewer and surface after deployment.** 🟢 **Recorded as a
licence that changes an architecture, not as good news.**

🟡 **And the caveat on `school-management-system`, stated rather than smoothed:** 🔴 **the `MIT`
text sits in ONE module directory and is copyright an **individual contributor**, not the
organisation that owns the repository; the root carries nothing, the other modules carry nothing,
and `phpmailer/LICENSE` in the same tree is vendored `LGPL-2.1`.** 🔵 **That is a grant, and it is
the weakest shape of one on this shelf. Use it only with the provenance recorded.**

### 🆕 🟢 `P215-V2` — the SIS/LMS connector tier is now permissive across all four platforms

🟢 **A week ago this shelf described its own connector tier as unusable. The tier did not change;
the reading did.**

| platform | connector | was | is |
|---|---|---|---|
| **Canvas** | `DMontgomery40/mcp-canvas-lms`, `MisterCommand/mcp-canvas-lms` | 🔴 absent | 🟢 **`MIT`** both |
| **Moodle** | `ink-waffle/moodle-mcp` | 🔴 none | 🟢 **`MIT`** |
| **Brightspace** | `Exhabition/brightspace-mcp-rs` | 🔴 absent | 🟢 **`MIT`** *(`Cargo.toml` and `package.json` agreeing)* |
| **Sisu (Funidata)** — EMEA | `ink-waffle/sisu-mcp` | 🔴 *"no licence, unusable as published"* | 🟢 **`MIT`** |
| **LTI 1.3** | `Simon-Initiative/lti-example-tool` *(CMU)*, `kstateome/lti-launch` | 🔴 `NOASSERTION` / absent | 🟢 **`MIT`** / **`LGPL-3.0`** |

🔵 **EMEA specifically gains a usable institutional-SIS path: `sisu-mcp` is written for *any* Sisu
deployment rather than one university, and Sisu is the Finnish higher-education SIS.**
🟡 **`kstateome/lti-launch` is `LGPL-3.0`, not `MIT` — linkable, but modifications to the library
itself carry obligations.**

### 🆕 🟢 `P215-V3` — `ECL-2.0` belongs on this shelf, and it was never here

🟢 **The **Educational Community License `2.0`** is the Apereo/Sakai house licence — read
first-hand this pass from `Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider`'s
`LICENSE_HEADER` (`558` B), pointing at `osedu.org/licenses/ECL-2.0`.**
🔵 **It is an `Apache-2.0` derivative with a patent grant, so for build purposes it sits beside
`Apache-2.0`, and it is the licence family a studio meets first when it touches **Sakai**,
**Apereo**, `OpenEQUELLA` or the Learning Analytics Initiative.** 🔴 **`214` passes of this KB
never recorded it, because a title-window matcher looking for `apache license` does not match
*"Educational Community License"*.** 🔵 **`ACTION QI` re-reads the Apereo rows rather than
assuming; this pass claims only the row it read.**

## Pass 214 — 2026-10-15 — THE PLATFORM SHELF'S BIGGEST CORRECTION THIS MONTH: `GibbonEdu` IS NOT NETWORK-COPYLEFT, AND FORMA LMS HAS A GRANT AFTER ALL

🔵 **`ACTION PZ` *(p211, offline)* reconciled every repository printing more than one grant
across the four client-facing shelves.** 🟢 **`3` cells on THIS page change, and both changes
move a platform from *"integrate-only"* to *"buildable"*.** 🔵 **Method:
[`compose/code/p214-multi-grant-reconciliation/`](../compose/code/p214-multi-grant-reconciliation/README.md).**

### 🆕 🟢 `P214-1` — `GibbonEdu/core` is `GPL-3.0`, not `AGPL-3.0`, and the architecture advice inverts

🔴 **For `4` cells across this KB — `2` of them on this page — `GibbonEdu/core` was published as
`AGPL-3.0`, marked `integrate-only`, and flagged with *"the hosted-deployment question arrives on
day one."*** 🟢 **It is `GPL-3.0`. That question does not arise.**

| | 🔴 what this page said | 🟢 what is true |
|---|---|---|
| grant | `AGPL-3.0` | 🟢 **`GPL-3.0`** *(`35 121` B · `LICENSE`)* |
| channels | one body match | 🟢 **`3` agreeing:** `LICENSE` title line, `composer.json` `"license": "GPL-3.0"`, `README` l.`81` |
| copyleft reach | 🔴 network — serving it triggers disclosure | 🟢 **file** — fork, modify, host; **no source disclosure owed to users** |
| studio posture | 🔴 integrate-only, keep at a service boundary | 🟢 **fork-and-host is open.** Distributing a modified binary still carries `GPL-3.0` |

🔴 **One of the two cells had hardened the error into an assertion — *"`AGPL-3.0` (not `GPL`, as
secondary sources say)"*.** 🟢 **The secondary sources were right.** 🔵 **The cause is
mechanical: `GPL-3.0` §13 is titled *"Use with the GNU Affero General Public License"*, so the
word `Affero` appears `3` times inside a `GPL-3.0` body and a whole-body matcher flips the
family.** 🔴 **This KB documented that mechanism in `P171` and stated *"Gibbon es `GPL-3.0`"* at
the time — and these cells still said `AGPL-3.0`.** 🔵 **Full reading in
[`agents/top.md`](../agents/top.md) `P214-1` and `P214-3`.**

🟢 **Why this is the month's most consequential cell on this page:** 🔵 **a self-hosted school
SIS, forked and customised, is the single most requested build in this industry.** 🔴 **This KB
had ruled the most mature open SIS out of it on a licence reading that was wrong.**

### 🆕 🟢 `P214-2` — Forma LMS: the grant was in-tree the whole time

🔴 **This page carried Forma LMS as *"NO GRANT at `9` path forms … carries no licence body at
all"*.** 🟢 **That was a ROOT-ONLY reading.** 🟢 **`formalms/formalms` is `GPL-2.0`:**

| path | bytes | reads |
|---|---|---|
| `html/license.txt` | **`18 346`** | 🟢 **`GNU GENERAL PUBLIC LICENSE`, Version 2, June 1991** |
| `html/lib/System/license/license_english.txt` | **`15 146`** | 🟢 same, **+ `9` translations** *(Bosnian, Croatian, French, German, Italian, Portuguese, Spanish, Tamil)* |

🔵 **The `Apache-2.0` that three comparison articles reported is a vendored file** —
`html/templates/standard/jsdoc/scripts/prettify/Apache-License-2.0.txt`. 🟢 **The articles were
reading a dependency; this KB was reading the root; the project's own answer is `GPL-2.0`, and a
localised installer licence in `10` languages is where a 2000s-era PHP LMS puts it.**

🟡 **Posture, now that it has a grant:** 🔴 **`GPL-2.0` is file copyleft with no network clause,
so hosting is clean — but `GPL-2.0` *(not "or later")* is incompatible with `GPL-3.0` code**, so
a build mixing Forma LMS with a `GPL-3.0` component has a real problem. 🟢 **Mixing with `MIT`
or `Apache-2.0` components is fine.**

### 🆕 🔴 Understated the other way: `2` hosted-service platforms DO owe source

🔵 **The GNU axis is not biased in one direction — these two moved the opposite way:**

| repo | 🔴 was | 🟢 is | what it means hosted |
|---|---|---|---|
| [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) | 🟡 `GPL-3.0` | 🔴 **`AGPL-3.0`** *(`33 820` B)* | 🔴 **An Open Badges `3.0` issuer run as a service owes source to its users** |
| [`memphis-iis/MoFaCTS`](https://github.com/memphis-iis/MoFaCTS) | 🟡 `GPL-3.0` | 🔴 **`AGPL-3.0`** *(`34 523` B)* | 🔴 **A hosted adaptive-practice tutor owes source** |

### 🟢 Unchanged and re-confirmed: `odoo/odoo` is `LGPL-3.0`

🔵 **`PZ` flagged `odoo/odoo` and `bigbluebutton` as self-contradicting; both are FALSE
POSITIVES of the script** — the stray `GPL-3.0` tokens are in this page's own table *about
licence-text structure* *("`GPL-3.0` included by **value**")*, not grant claims. 🟢 **Both cells
are correct and untouched.** 🟢 **`odoo/odoo` remains `LGPL-3.0` *(`43 529` B, `LGPLv3` named in
line `2` of the blob)*, so the education-ERP-on-Odoo pattern this page recommends stands.**

---
## Pass 213 — 2026-10-15 — THE SYSTEM OF RECORD HAS NO AI IN IT: `183` SIS REPOSITORIES, `0` AI ROWS. AND A PLATFORM THAT CALLS ITSELF "TRULY OPEN SOURCE, FREE FOR COMMERCIAL USE" IS `GPL-2.0`

🔵 **Grants read from the licence blob at `HEAD` on `2026-10-15`; bytes AS SERVED, per `T208-8`.**

### 🆕 🔴 `P213-6` — `topics/student-information-system`: `183` repositories, `0` of the top `20` mention AI

🟢 **The SIS is the system of record — enrolment, attendance, grades, the data every tutor needs
and every compliance regime audits.** 🔴 **Not one of the top `20` repositories in its topic
mentions AI, an LLM, an agent or a tutor.** 🔵 **Two mention grades at all** *(`MeetPlan`,
`school-management-system`)*, **as CRUD, not as inference.**

🟢 **The shelf, with grants read today:**

| platform | 🟢 Grant *(blob bytes · form)* | ★ | Region | What it is |
|---|---|---|---|---|
| [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** *(`1 094`)* | **404** | Global | 🟢 **The permissive SIS**, Laravel + Filament. Still the only `MIT` row in this slot |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** *(`15 214`)* | **646** | Global | The most-starred open SIS. 🔴 **`GPL-2.0`** |
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 **GPL-2.0** *(`17 286` · `docs/License.txt`)* | **345** | North America | 🟡 **Grant is NOT at the repository root** — `19` root path forms return `404`, reproduced blind this pass *(`T213-7`)* |

🔵 **The engagement reading:** 🟢 **an AI layer in education attaches to a system of record that
was not built to host one, under `GPL-2.0` two times in three.** 🔴 **`academico` *(`MIT`)* is the
only row a studio can extend into a proprietary deliverable without a service boundary.**

### 🆕 🟡 `P213-7` — "truly open source, free for commercial use" is `GPL-2.0`, and both halves are true

🟢 **[`xiaochong0302/course-tencent-cloud`](https://github.com/xiaochong0302/course-tencent-cloud)
— `1.2`k★, PHP, Chinese-language, **APAC** — describes itself as
*"名符其实的开源，可免费商用"* *("genuinely open source, free for commercial use")*.** 🟢 **The blob
is **`GPL-2.0`, `18 092` B**, read today.**

🔴 **Nothing in that description is false, and a studio that reads it as *permissive* is wrong
anyway.** 🟢 **`GPL-2.0` IS free for commercial use; what it is not is embeddable in a closed
deliverable.** 🔵 **This is a distinct trap from the ones p205–p212 catalogued: not a mislabelled
grant, not a scope partition, but a TRUE self-description that answers a different question than
the one diligence is asking.** 🟢 **The gate must read the blob even when the description sounds
settled — especially then.**

### 🟢 Platform rows — grants read from the blob on 2026-10-15

🔵 **`2` rows are new to this KB *(marked 🆕)*; `2` are CARRIED rows re-read today, agreeing with
their published cells.**

| platform | 🟢 Grant *(blob bytes)* | ★ | Origin → region | What it is, and what it replaces |
|---|---|---|---|---|
| 🆕 [kalvilabs/kalvi](https://github.com/kalvilabs/kalvi) | 🔴 **AGPL-3.0** *(`34 523`)* | **117** | 🟡 unplaced *(no country stated; `kalvi.co`)* | 🟢 **"Open Source Infrastructure for Online Education"** — launch a platform, author courses, sell practice exams, run live classes, gamify. 🔴 **`AGPL-3.0`: run it, do not embed it** |
| 🆕 [PapillonApp/papillon-v6](https://github.com/PapillonApp/papillon-v6) | 🔴 **GPL-3.0** *(`35 149`)* | **117** | France → **EMEA** | 🟢 **A community-built alternative CLIENT for school-life systems** *("vie scolaire")*. 🔵 **The only row on these shelves that is a third-party client for national school software** — a shape worth knowing in EMEA public-sector work |
| [edrys-org/edrys](https://github.com/edrys-org/edrys) | 🟡 **MPL-2.0** *(`16 725`)* | **334** | Global | 🟢 **Modular remote-teaching platform, "the first live LMS".** 🟡 **`MPL-2.0` is the middle ground this industry almost never offers: file-level copyleft, so a new module you add stays yours** |
| [classroomio/classroomio](https://github.com/classroomio/classroomio) | 🔴 **AGPL-3.0** *(`34 523`)* | **1.7**k | Global | Self-hostable education platform pitched as a Moodle alternative for companies. 🔴 **`AGPL`** |

🟢 **Why `edrys` earns a line of its own:** 🔵 **the permissive-platform question `P212-3` answered
with `OpenOLAT` *(`Apache-2.0`)*, `Artemis` *(`MIT`)*, `mentingo` *(`MIT`)* and `academico`
*(`MIT`)* now has a fifth shape — `MPL-2.0`.** 🟢 **For a studio writing NEW modules rather than
modifying existing files, `MPL` is functionally permissive on the work it adds.** 🔴 **It is not
permissive on the files it edits, which is the distinction a licence column cannot carry and a
pattern must.**

### 🆕 🔴 `P213-8` — `LTI` is the adapter slot, and there is nothing AI-shaped in it

🟢 **`topics/lti`, `185` repositories, `0` of the top `20` AI-adjacent** *(full table in
[`repos/foundations.md`](../repos/foundations.md) `P213-5`)*. 🔵 **This is the concrete form of the
pitch:** 🟢 **every LMS on this shelf — `Moodle`, `Open edX`, `Canvas`, `OpenOLAT`, `Artemis` —
speaks `LTI 1.3`, and the `LTI` ecosystem contains no AI tool.** 🔴 **So "add AI to your LMS" is
not a platform migration. It is one `LTI 1.3` tool, and `pylti1.3` *(**MIT**, `1 070` B)* or
`tsugi` *(**Apache-2.0**, `10 273` B)* is the whole integration surface.**

### 🟢 Carried forward unchanged

## Pass 212 — 2026-10-15 — THE PERMISSIVE PLATFORM EXISTS, SAKAI IS NOT APACHE, AND `pupilfirst` DEFEATED THIS KB'S OWN CLASSIFIER

### 🆕 🟢 `P212-3` — nine passes answered the permissive-platform query with `0`. The answer was `3` rows.

🟢 **The task's vertical query — `open source platform education ERP CRM MIT Apache` — has
returned `0` new permissive education platforms for nine consecutive passes, and p211 recorded that
`apache/ofbiz-framework` is "the only permissive ERP in reach and has no education layer at all".**
🔴 **That is true of the *search-engine* channel.** 🟢 **Reading `topics/lms` *(`2 468`
repositories)* and `topics/ai-tutor` *(`707`)* directly produced three permissive platforms in one
pass:**

| platform | 🟢 Grant *(blob bytes · form)* | ★ | Origin → region | What it is, and what it replaces |
|---|---|---|---|---|
| 🆕 🟢 **[Selleo/mentingo](https://github.com/Selleo/mentingo)** | 🟢 **MIT** *(`1 062` · `LICENSE`)* | **95** | Selleo, Poland → **EMEA** | 🟢 **Self-hosted, AI-native LMS — course delivery *with an AI mentor built in*.** 🔵 **The only row on this shelf where the AI layer is native to the platform rather than bolted beside it, and it is `MIT`.** 🟡 Young and small: fork it, own it, do not treat it as a vendor |
| 🆕 🟢 **[OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT)** | 🟢 **Apache-2.0** *(`10 982`)* | **447** | Switzerland → **EMEA** | 🟢 **A mature, university-grade LMS under `Apache-2.0`.** 🔵 **Deployed across Swiss and German higher education for over a decade.** 🟢 **This is the build-proprietary-modules-on-top answer that `Moodle` *(`GPL-3.0`)* and `Open edX` *(`AGPL-3.0`)* cannot give** |
| 🆕 🟢 **[academico-sis/academico](https://github.com/academico-sis/academico)** | 🟢 **MIT** *(`1 094`)* | **404** | → Global | School management / **SIS** on Laravel + Filament for small and mid-sized institutions. 🔵 **The permissive student-information-system slot, which `OpenEduCat` *(`LGPL-3.0`, on Odoo)* has held alone on this shelf** |
| 🆕 🟢 **[ls1intum/Artemis](https://github.com/ls1intum/Artemis)** | 🟢 **MIT** *(`1 091` · `develop`)* | **818** | TUM, Germany → **EMEA** | 🟢 **Interactive learning platform with automated feedback, `12 396` commits.** Detail on the grading tier in [`repos/foundations.md`](../repos/foundations.md) p212 |

🔵 **Stated for the next pass so the finding is not re-discovered:** **the permissive-platform query
is answered. `OpenOLAT` for a mature LMS, `Artemis` for assessment-led teaching, `mentingo` for an
AI-native greenfield, `academico` for an SIS.** 🔴 **The nine `0` readings measured the channel.**

### 🔴 `P212-2` — Sakai is `ECL-2.0`. This shelf has said `Apache-2.0` since cycle 3.

🟢 **[`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) — read first-hand, `11 120`
bytes, first line `Educational Community License, Version 2.0 (ECL-2.0)`.**

🔵 **`ECL-2.0` is `Apache-2.0` with one change, in the licence's own words: the patent grant in
section `3` is narrowed "to be specific to the needs of the education communities using this
license".** 🟢 **Copyright permissions, attribution and `NOTICE` obligations are identical, and it
is OSI-approved.**

🟢 **Engagement impact: none for building on top.** 🔴 **Procurement impact: real.** 🔵 **A ministry
or publisher whose diligence reads patent clauses is not being told the truth by "Sakai is Apache",
and this KB has been supplying that answer for three cycles.** 🟢 **Also `ECL-2.0`:
[`Apereo-Learning-Analytics-Initiative/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW).**
🟢 **Confirmed NOT `ECL` by first-hand read the same pass — these four cells on this shelf are
correct as they stand:** `openedx/edx-platform` *(`AGPL-3.0`)*, `learningequality/kolibri`
*(`MIT`)*, `oppia/oppia` *(`Apache-2.0`)*, `uPortal-project/uPortal` *(`Apache-2.0`)*.

### 🆕 🔴 `P212-7` — `pupilfirst` is a SPLIT-SCOPE grant, and it broke this pass's own classifier

🔴 **[`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) *(`978`★, Pupilfirst Pvt.
Ltd., India → APAC)* was first classified by this pass's probe as `CC-family`. That is wrong, and
it is wrong in the direction that loses a client a usable platform.**

🟢 **What the blob actually says, read in full *(`1 684` bytes)*:**

| scope | grant |
|---|---|
| everything under `docs/` | `CC-BY-SA-4.0` |
| all client-side JavaScript *(served, compiled, arranged, augmented or combined)* | 🟢 **`MIT`** |
| third-party components | their own original licences |
| 🟢 **everything else** | 🟢 **`MIT`** *(full text follows in the same file)* |

🟢 **So `pupilfirst` is an `MIT` platform with `CC-BY-SA` documentation.** 🔴 **A head-anchored
classifier reads the first licence named — `CC-BY-SA-4.0` — and blocks it.**

🔵 **This is the `Gap 466` class p205 fixed, running the other way.** 🟢 **p211's trap was `odoo`:
a title saying `LGPLv3` above the full `GPL` text, where a whole-body matcher is wrong and a
title-anchored one is right.** 🔴 **`pupilfirst` is the mirror: the title-anchored read is wrong
and only a **scope-aware** read is right.** 🟢 **Neither ordering is sufficient. A licence file can
carry several grants partitioned by *path*, and the only correct instrument reads the partition.**
🔵 **The gate in [`compose/patterns.md`](../compose/patterns.md) `P211-A` gains a step for this —
see `P212-A`.**

### 🟢 The platform shelf, re-read first-hand this pass

| platform | 🟢 Grant *(blob bytes · form)* | ★ | Region | Build-or-integrate |
|---|---|---|---|---|
| [frappe/lms](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** *(`33 893` · `license.txt` · `develop`)* | **3.3k** | APAC *(India)* | 🟢 **Re-confirms p209 and p211 independently.** Integrate; hosted modifications trigger disclosure |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 **AGPL-3.0** *(`34 523` · `dev`)* | **2.4k** | Global | "Next-generation learning platform", AI in its tags. 🔴 `AGPL` — integrate only |
| [classroomio/classroomio](https://github.com/classroomio/classroomio) | 🔴 **AGPL-3.0** *(`34 523`)* | **1.7k** | Global | Positions itself as the Moodle alternative for companies |
| [codelitdev/courselit](https://github.com/codelitdev/courselit) | 🔴 **AGPL-3.0** *(`34 143` · `LICENSE.md`)* | **1.3k** | Global | Course selling + digital downloads |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🆕 🟢 **ECL-2.0** *(`11 120`)* | **1.2k** | **North America** *(Apereo)* | 🟢 **Permissive. Build on it** — with the patent-scope note above |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** *(`34 523` · `LICENSE.txt` · `release`)* | **1.1k** | Global | The Docker Open edX distribution — the standard way to actually run Open edX |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0** *(`35 147`)* | **1k** | EMEA + 🟢 **LATAM install base** | 🔵 **The LMS with genuine Spanish-speaking institutional adoption.** 🟢 **For a LATAM engagement this is the platform in the room, and `GPL-3.0` means plugins, not forks** |
| [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | 🟢 **MIT** *(code)* / `CC-BY-SA-4.0` *(`docs/`)* *(`1 684`)* | **978** | APAC *(India)* | 🟢 **Permissive. Asynchronous online school: tasks, feedback, community** |
| [gazpachu/hypatia](https://github.com/gazpachu/hypatia) | 🟡 **LGPL** *(`19 350` · `license.txt`)* | **651** | Global | JS LMS for MOOCs. 🟡 Library-scoped copyleft — link, do not modify |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL-3.0** *(`35 147` · `release_11`)* | **505** | **EMEA** *(Germany)* | Long-established German HE platform |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** *(`10 982`)* | **447** | **EMEA** *(Switzerland)* | 🟢 **Build. The permissive mature LMS** |
| [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** *(`1 094`)* | **404** | Global | 🟢 **Build. Permissive SIS** |
| [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT/X** *(`1 145`)* | **437** | **North America** | Teaching environment with auto-graded code homework |

### 🔴 The finding that should change how this shelf is sold

🔴 **`18` of the top `20` repositories in `topics/lms` make no mention of AI or an LLM.** 🔵 **Not
"weak AI" — no mention.** 🟢 **The exceptions are `learnhouse` *(AI in topic tags only)* and
`Selleo/mentingo` *(genuinely AI-native, and `95`★)*.**

🟢 **Read against the Council of Europe's `2026`–`27` work programme and the EU AI Act's August
`2026` high-risk classification** *(see [`intel/market.md`](../intel/market.md) p212)*, **the
conclusion is commercial, not technical:** 🔴 **the installed platform base will not have an
agent layer by the time the obligations bite.** 🟢 **The seam — `LTI 1.3`, an `MCP` server, a
Moodle plugin, an `xAPI` emitter — is where the work is, and it is work a studio can deliver in
weeks against a platform the client already runs.** 🔵 **Selling a platform replacement into this
market is selling against the client's own sunk cost; selling the seam is selling into a
deadline.**

### 🟢 Carried forward unchanged

🟢 **`SWAD` is `AGPL-3.0`** *(p211's reclassification stands — integrate-only until the deployment
model is known)*. 🟢 **`odoo`'s `LICENSE` is the `Gap 466` trap: title-anchored reads `LGPL-3.0`,
whole-body reads `GPL-3.0`, and `LGPL-3.0` is the correct answer that makes the `OpenEduCat` stack
buildable.** 🟢 **`Moodle`, `Open edX`, `Canvas`, `BigBlueButton` *(`LGPL-3.0`)*, `H5P`, `Kolibri`
*(`MIT`)*, `OpenEduCat` *(`LGPL-3.0`)* and `Koha` remain as previously recorded.**

## Pass 211 — 2026-10-15 — TWO PLATFORM GRANTS WERE WRONGER THAN THE SHELF KNEW, AND BOTH RUN IN THE DIRECTION THAT CHANGES THE RECOMMENDATION

### 🔴 The platform grants, re-read from the blob

🟢 **Every platform on this shelf had its licence blob read first-hand this pass** *(channel
correction in [`repos/foundations.md`](../repos/foundations.md) p211)*. 🔵 **This shelf
contributed `665` table rows to the audit; `2` platforms carry a cell that would change a
build/integrate decision, and `1` of those is a platform this KB recommends constantly.**

| platform | a cell on this shelf says | 🟢 read from the blob | why it matters |
|---|---|---|---|
| 🔴 **[`acanas/swad-core`](https://github.com/acanas/swad-core)** | 🔴 `GPL-3.0` | 🔴 **`AGPL-3.0`** | 🔴 **network copyleft, on a student-facing platform. Wrong in BOTH places it appears and never corrected** |
| [`odoo/odoo`](https://github.com/odoo/odoo) `:936` | 🟡 `GPL-3.0` *(describing the embedded text)* | 🟢 **`LGPL-3.0`** | 🟢 **more permissive than the cell reads** — `LGPL` is what makes the `OpenEduCat` stack buildable |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) `:934` | 🟡 `GPL-3.0` *(by reference)* | 🟢 **`LGPL-3.0`** | 🟢 **the virtual-classroom layer is library-scoped copyleft, not full `GPL`** |

🔵 **The `odoo` and `bigbluebutton` cells sit in a byte-structure table and describe what is
*inside* the `LICENSE` file rather than asserting a grant — [`foundations.md`](../repos/foundations.md)
`:4686` and `:4825` already carry `LGPL-3.0` correctly.** 🔴 **But a reader scanning this shelf
sees a platform name next to the token `GPL-3.0`, and that is the whole risk `P211-1`
describes.**

### 🆕 🔴 `P211-4` — `odoo`'s `LICENSE` is the `Gap 466` trap, still armed

🔴 **`odoo/odoo`'s `LICENSE` names `LGPLv3` in its third line and then includes the **full text
of the GPL** below it**, because the LGPL is drafted as a set of additional permissions on top
of the GPL. 🟢 **A whole-body matcher returns `GPL-3.0`. A title-anchored one returns
`LGPL-3.0`.** 🔵 **This is precisely the defect p205 fixed as `Gap 466`, and `odoo` is the
highest-traffic repository on these shelves where it still bites.**

🟢 **Consequence for the vertical, stated plainly because it decides engagements:** **`LGPL-3.0`
lets a studio ship proprietary modules on top of Odoo and `OpenEduCat`; `GPL-3.0` would not.**
🔴 **A shelf that reads `GPL-3.0` would have ruled out the single most common education-ERP
build pattern this KB recommends.**

### 🟢 `SWAD` — reclassified, and the recommendation changes with it

🟢 **SWAD *(Universidad de Granada, `76`★, EMEA, two decades in production)* is `AGPL-3.0`.**
🔴 **Previously carried here as `GPL-3.0` with no copyleft caveat.**

🔵 **Revised guidance: integrate-only until the client's deployment model is known.** 🟢 **If
SWAD is hosted and students reach it over a network, `AGPL-3.0` obliges source disclosure of
modifications to those users.** 🔵 **That is survivable — it is the same obligation Open edX
carries — but it must be priced into the engagement, and until this pass it was not visible on
this shelf at all.**

### 🟢 Permissive-ERP check — ninth negative reading

🟢 **Query run as specified: `open source platform education ERP CRM MIT Apache`.** 🔴 **`0` new
permissive education ERPs.** 🔵 **The returns restated what this shelf holds: `OpenEduCat`
*(`LGPL-3.0`, on Odoo)*, `ERPNext` *(`GPL-3.0`)*, and `Twenty` *(`BSL-1.1`, non-OSI, not
education)*.** 🟢 **p210's `ACTION PY` finding stands as the answer to this query:
[`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) is the only permissive ERP
in reach and **has no education layer at all**.**

🟢 **Two SIS candidates came back and neither changes the shelf:**
[`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) is already here in
`33` places *(`GPL-2.0`, confirmed from the blob this pass)*; **OpenCampus** — the Drupal + ECA
SIS reported at `1`M+ European higher-ed users, presented at Apereo in January `2026` — 🔴 **has
no public repository reachable under the obvious names, so its grant is unknown and it is
recorded as an informed gap rather than as a component.**

## Pass 210 — 2026-10-15 — EIGHTH NEGATIVE READING ON A PERMISSIVE SIS, AND THE CHANNEL HAS STARTED ANSWERING A DIFFERENT QUESTION

### 🔴 No permissive education SIS, eighth consecutive reading

🟢 **`open source platform education ERP CRM SIS MIT Apache 2026` returned nine sources.** 🔴 **The
channel's own verdict, quoted: it *"didn't turn up an open source education platform that is MIT or
Apache licensed and covers ERP, CRM, and SIS together."*** 🟢 **What it returned, with grants read
first-hand where the row is on these shelves:**

| platform | grant | read how | what it is | permissive? |
|---|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **`LGPL-3.0`** | 🟢 **blob, `2026-10-15`** — *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3"*, `8.05` KB | Education ERP: SIS + LMS + CRM modules, `889`★ | 🔴 **no** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | `GPL-3.0` | 🟢 sidebar, `2026-10-15` | the largest ecosystem, `7.5k`★ | 🔴 no |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `AGPL-3.0` | 🟢 sidebar, `2026-10-15` | Open edX LMS & Studio, `8.2k`★ | 🔴 no |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `ECL-2.0` | 🟢 sidebar, `2026-10-15` | HE LMS, `1.2k`★ | 🟡 effectively yes, via `ECL` |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `GPL-3.0` *(multi-licence)* | 🟢 sidebar, `2026-10-15` | LMS focused on ease of use and accessibility, `1.0k`★ | 🔴 no |
| [`frappe/education`](https://github.com/frappe/education) | 🟡 **`GPL-3.0` by `19`-byte statement** | 🟢 blob, `2026-10-15` | *"Open source education / school management system"*, `666`★ | 🔴 no |
| `ERPNext` · `Dolibarr` | `GPL-3.0` | search snippet | generic ERP with an education module | 🔴 no |
| [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | 🟢 **`Apache-2.0`** | 🟢 **sidebar, `2026-10-15`** | generic ERP: accounting, CRM, orders, warehousing, MRP; `1.1k`★, `30 511` commits | 🟢 **yes — and no education layer at all** |
| `Atomic CRM` · `Krayin` | `MIT` | search snippet | 🔴 **CRMs, not education systems** | 🟢 yes / 🔴 irrelevant |
| `RosarioSIS` · `Gibbon` | `GPL` | prior passes | the only SIS answers that exist | 🔴 **no** |

🟢 **State it to clients as the market fact eight readings make it: the student-record layer of
open-source education is COPYLEFT, end to end, and no amount of searching changes that.**

### 🆕 🔴 The channel drifted, and that is itself the finding

🔴 **Three of this pass's nine hits were generic business software with no education dimension —
`Apache OFBiz`, `Atomic CRM`, `Krayin`.** 🔵 **The query named `ERP` and `CRM` alongside `SIS`, and
the channel resolved the permissive constraint by dropping the INDUSTRY instead of returning
nothing.**

🟢 **Guidance for later passes, because this will recur with any multi-term vertical query:** 🔴 **a
search that cannot satisfy every term silently relaxes one, and the term it relaxes is the one
hardest to match — here, `education`.** 🔵 **So a hit list that is `30`% off-vertical is not a bad
sample; it is the channel telling you the constrained set is EMPTY.** 🟢 **Read the drift as a
negative result with a confidence attached, and do not re-run the query hoping for better luck.**

### 🆕 🟢 What `Apache OFBiz` is actually worth here — one honest option, not a recommendation

🔵 **`OFBiz` is the only permissive ERP the channel has ever returned for this vertical, and it has
no education layer whatsoever.** 🟢 **That makes it a genuine architectural option in exactly one
situation, worth writing down because the shelf has been answering "no permissive SIS" for eight
passes without naming what the alternative would cost:**

- 🟢 **Use it when** the client's hard constraint is that the record layer must not be copyleft — a vendor embedding the system in a proprietary product, or a ministry whose procurement forbids reciprocal licences on state systems.
- 🔴 **The cost is the whole domain model.** `OFBiz` gives accounting, parties, orders and warehousing; enrolment, courses, sections, terms, transcripts, attendance and grading are all BUILD. 🔵 **That is `OpenEduCat`'s entire value proposition rebuilt from parties and orders.**
- 🟡 **The honest comparison:** 🔴 **`OFBiz`-plus-build is almost always the wrong answer on cost, and almost always the only answer on licence.** 🟢 **The cheaper escape remains the one these shelves already prefer: a copyleft record system with the proprietary work in the AI layer ABOVE it, or `Ed-Fi ODS/API` (`Apache-2.0`) as the permissive data-standard escape hatch.**
- 🟢 **Verified first-hand this pass, so `ACTION PY` opened and closed inside p210:** [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) is 🟢 **`Apache-2.0`** by sidebar, `1.1k`★, `30 511` commits, described as *"an open source product for the automation of enterprise processes"* covering ERP, CRM and e-commerce. 🔵 **The grant is real and the education layer genuinely does not exist — the `30 511` commits are accounting, parties, orders and warehousing.**

### 🆕 🔴 `opensalt/OB3DefinitionWidget` — this shelf's most fragile row, named

🔴 **Read first-hand `2026-10-15`: `MIT`, and `1`★.** 🔴 **It appears at `11` sites on this shelf
and `19` sites in [`compose/patterns.md`](../compose/patterns.md) — the Open Badges 3.0 credential
path in every micro-credential recipe this KB publishes runs through a one-star repository.**

🟢 **The mitigation is unusually cheap here, which is why this row is a flag and not an
emergency:** 🔵 **Open Badges 3.0 is a published `1EdTech` specification, and the widget is a
convenience for authoring an achievement definition — not an implementation of anything secret.**
🟢 **Any engagement can emit a conformant achievement definition directly from the spec, and
should treat the widget as a reference rather than a dependency.** 🔴 **Recipes naming it must say
so; `ACTION PX` in `repos/foundations.md` p210 carries this.**

### 🟢 Two platform grants that no licence scanner can see — now a `15`% rate, not a curiosity

🔴 **p209 reported that `OpenOLAT`'s sound `Apache-2.0` grant is invisible to GitHub's classifier.**
🔴 **p210 adds `openeducat/openeducat_erp` (`LGPL-3.0`, `8.05` KB body) and `frappe/education`
(`GPL-3.0` statement, `19` bytes) — both showing an unnamed `License` link and no SPDX token.**

🔵 **Three of twenty rows read first-hand, `15`%** *(full count in [`agents/top.md`](../agents/top.md) p210)*.
🔴 **Procurement consequence, now with a number on it: a client's SBOM or licence-scan tool keyed on
GitHub's detection will report NO LICENCE for roughly one in seven of the platforms on this shelf
— including two it will then block.** 🟢 **The remedy is the same and it is now routine: ship the
blob URL, the byte count and the read date beside every grant in a deliverable, so the scanner's
silence is answered before it is raised.** 🔵 **That is precisely what the tables in this pass do.**

## Pass 209 — 2026-10-14 — SEVENTH NEGATIVE READING ON A PERMISSIVE SIS, AND A PLATFORM WHOSE GRANT NO SCANNER CAN SEE

### 🔴 The permissive education SIS does not exist — and seven readings make that a market fact

🟢 **`open source platform education LMS SIS MIT Apache 2026 self-hosted` returned nine sources
and not one permissive student information system.** 🔴 **What it returned, and what each actually
is:**

| platform | grant *(verified or shelf-confirmed)* | what it is | permissive? |
|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** *(read from the blob this pass)* | Java LMS, strong in DACH higher education | 🟢 **yes** |
| [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **`AGPL-3.0`** *(sidebar, verified this pass)* | Frappe-stack LMS, `3.3k`★ | 🔴 **no — and a blog this pass called it `MIT`** |
| Moodle | `GPL-3.0` | the largest ecosystem | 🔴 no |
| Open edX · Canvas | `AGPL` | heavy to self-host | 🔴 no |
| Sakai | `ECL-2.0` *(Apache-compatible)* | HE LMS | 🟡 effectively yes, via `ECL` |
| RosarioSIS · Gibbon | `GPL` | the only SIS/school-management answers returned | 🔴 **no** |
| Forma LMS | 🔴 **sources CONFLICT: `Apache-2.0` vs `GPL`/`LGPL`** | Docebo PHP fork | 🔴 **unresolved — do not quote** |

🔵 **Seventh consecutive negative reading on a permissive SIS.** 🟢 **Stop treating this as a search
failure and state it to clients as a market fact: the student-record layer of open-source education
is COPYLEFT, end to end.** 🔴 **Which means the SIS is the wrong place to put proprietary client
IP, and the architecture must put it in the AI layer ABOVE a copyleft record system** — exactly
what the `Ed-Fi`-first pattern on this shelf already does *(`Ed-Fi ODS/API`, `Apache-2.0`, is a
data standard, not an SIS, and that is why it is the permissive escape hatch)*.

### 🆕 🔴 `OpenOLAT`'s grant is sound and INVISIBLE to every automated scanner

🟢 **Read first-hand this pass:
[`OpenOLAT/OpenOLAT/LICENSE`](https://github.com/OpenOLAT/OpenOLAT/blob/master/LICENSE) is a
verbatim `Apache License, Version 2.0, January 2004` — `197` lines, `10.7` KB.** 🔴 **GitHub's
sidebar names no licence for the repository at all, and the API's `license` field uses the same
detection.**

🔵 **Procurement consequence, and it is concrete:** 🔴 **a client's own licence-scan, SBOM tool or
vendor-risk questionnaire will come back `NOASSERTION` / "no licence found" for `OpenOLAT`, and in
most enterprise gates that blocks adoption.** 🟢 **The engagement answer is to ship the blob
evidence with the recommendation — path, `197` lines, `10.7` KB, first three lines quoted — rather
than argue with the scanner.** 🔵 **This is the second platform-level instance on these shelves of
a CORRECT grant that cheap tooling cannot see, and it is worth a standing line in any
open-source-recommendation deliverable.**

## Pass 208 — 2026-10-14 — SIXTH PASS WITHOUT A PERMISSIVE EDUCATION ERP, AND THE PLATFORM CHOICE IS NOW DECIDED BY A CONNECTIVITY NUMBER

### 🔴 The permissive ERP still does not exist, and the sweep is now boring enough to state as a fact

🟢 **`open source platform education ERP CRM MIT Apache LMS student information system` returned
exactly two platforms, and both are copyleft and both are already on this shelf:**

| platform | grant | what it is |
|---|---|---|
| **OpenEduCat** *(community edition)* | 🔴 **`LGPL-3.0`** | Education ERP on the **Odoo** framework — SIS, LMS, CRM with leads/interactions/admissions, modular adoption. 🟡 Vendor claims *"`30 000`+ institutions in `130`+ countries"* are self-published and not verified |
| **Chamilo** | 🔴 **`GPL`** | LMS plus content management. **LMS-only** — not an ERP and not a CRM |

🔵 **Sixth consecutive measurement.** 🔴 **There is no `MIT`/`Apache-2.0` education ERP, so every
records-of-authority engagement in this industry is a copyleft engagement, and the only
architecture that keeps a client's own code closed is the one this KB has published since
`P207-B`: the ERP keeps the records, the agent layer runs OUT OF PROCESS across an API.**

### 🆕 🔴 The platform decision India's mandate forces, and it is not a licence decision

🔴 **`UDISE+` `2024-25`: `64.7`% of Indian schools have computers, `58`% functional for teaching,
`63.5`% have internet** — against an `AI & Computational Thinking` curriculum that is
**mandatory for Classes `3`–`8` from the `2026-27` session**. 🟢 **That pair of numbers selects
the platform tier before any licence argument starts:**

| tier | asset | grant | fits a `63.5`%-connected national mandate? |
|---|---|---|---|
| 🟢 **offline-first** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** | 🟢 **YES — packaged content, local sync, designed for intermittent connectivity** |
| 🟡 server LMS | Moodle | 🔴 `GPL-3.0` | 🟡 only where a school has a server AND a link |
| 🔴 cloud-first tutor | any hosted agent | — | 🔴 **NO — a third of the schools cannot reach it** |

🔵 **This is the first time in this KB that a CONNECTIVITY statistic, not a licence, picks the
platform** — and it is the reason `P208-B` is built on Kolibri rather than on the larger
platforms.

### 🟡 The MCP integration tier: one connector this KB cannot assess

🟡 **The Moodle/Open edX agent-integration sweep *(see [`repos/trending.md`](../repos/trending.md))*
returned the **eLeDia MCP Connector**, described as open source and able to create courses,
manage users and search content **inside Moodle's existing roles and permissions** — 🔴 **and it
is distributed from `eledia.de`, not GitHub, so this KB's locator and per-cell comparator cannot
read its grant at all.** 🟢 **Shortlisted as *legal review required*, never as a base.**
🟢 [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) re-read this
pass: 🔴 **`AGPL-3.0`, `34 523` B** — reference only.

### 🟢 The platform shelf, unchanged — and one conflict found incidentally

🟢 **Moodle `GPL-3.0` · Open edX `AGPL-3.0` *(with [`openedx/XBlock`](https://github.com/openedx/XBlock)
`Apache-2.0`, `LICENSE.TXT`, `11 358` B as the permissive way IN)* · Sakai `ECL-2.0` ·
ILIAS `GPL-3.0` · BigBlueButton `LGPL-3.0` · [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
`MIT` · [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) `Apache-2.0` ·
OpenEduCat `LGPL-3.0` · Chamilo `GPL` · [`frappe/lms`](https://github.com/frappe/lms) `AGPL-3.0`
(`33 893` B) · [`Selleo/mentingo`](https://github.com/Selleo/mentingo) `MIT` ·
[`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) 🔴 `Elastic-2.0`,
source-available, NOT open source.** 🔵 **No row changed family this pass.**

🆕 🟡 **One conflict this pass found without looking for it, and it is NOT adjudicated:** these
shelves carry **H5P** as `GPL-3.0` in three places *(`h5p/h5p-php-library`, `h5p/moodle-mod_hvp`,
and a GPL grouping with Moodle, Chamilo and ILIAS)* **and as `MIT` in one**. 🔴 **H5P is a
MULTI-REPOSITORY project, so both cells may be right about different repositories — which is
precisely why a conflict between two repository-level cells cannot be settled at the project
level.** 🟢 **Registered as `ACTION PW`: name the repository in the cell, then read its blob.**

## Pass 207 — 2026-10-14 — ONE PLATFORM ROW RECOVERED FROM A CAPITAL LETTER; THE PERMISSIVE ERP STILL DOES NOT EXIST

### 🟢 `openedx/XBlock` was never ungranted. Its file is called `LICENSE.TXT`

🔴 **The integration tier's most-used extension point was recorded as ungranted by p207's first
probe.** 🟢 [`openedx/XBlock`](https://github.com/openedx/XBlock) — the XBlock SDK, the entry
point for putting an agent inside Open edX — is **`Apache-2.0`, `11 358` B, `470`★, branch
`master`, not archived**, read from its own blob this pass.

🔴 **It returns `404` on `LICENSE`, `LICENSE.md` and `LICENSE.txt`, because the file is
`LICENSE.TXT` and `raw.githubusercontent.com` is case-sensitive.** 🔵 **For this page the
consequence is direct: the one permissively-licensed way into the second-most-deployed LMS in
the world was one capital letter from being struck off a shortlist.**

### 🟢 The permissive platform tier, unchanged and re-confirmed

🟢 **`185` licence bodies read at `HEAD` this pass across the whole shelf. `0` platform rows
change family.** The tier stands exactly as p206 published it:

| platform | repo | 🟢 grant, first-hand | what it is |
|---|---|---|---|
| 🟢 **OpenOLAT** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** `10 982` B | **the only full LMS on this shelf under a permissive grant.** Switzerland → **EMEA** |
| 🟢 **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`** `11 120` B | Apache-2.0 modified for university IP; OSI-approved, permissive → **North America** |
| 🟢 **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **`ECL-2.0`** `11 340` B | lecture capture and video, the classroom-media tier |
| 🟢 **XBlock SDK** | [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **`Apache-2.0`** `11 358` B 🆕 *(`LICENSE.TXT`)* | the permissive way INTO Open edX, whose platform is `AGPL-3.0` |

### 🔴 The education ERP gap is now searched three ways and still real

🟢 **An explicit sweep for an MIT- or Apache-licensed education ERP / SIS returned nothing.** 🔴
**[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) remains
`LGPL-3.0`** *(`8 241` B)* — weak copyleft, inherited from the Odoo framework it is built on, and
the only serious open education ERP in the field. Kuali, Compiere and Openbravo surface as
candidates in undated secondary material and were **not** blob-verified this pass.

🔵 **Stated as an informed gap rather than left silent, for the third pass running:** 🔴 **there
is no permissively-licensed education ERP.** 🟢 **The practical consequence is a split: take
`LGPL-3.0` OpenEduCat for the records tier and keep the agent layer in a separate process over
its API, so the weak copyleft never reaches the client's own code.** 🔵 **That split is `P207-B`
in [`compose/patterns.md`](../compose/patterns.md).**

### 🔴 The licence rider a customisation shortlist cannot see

🟢 **A `Commons Clause` rider does not replace a licence, it amends one — removing the right to
SELL.** 🔴 **p206's classifier returns a clean `MIT` on such a body**, which for this page is the
dangerous case: a platform shortlisted as `MIT` that may not be sold as part of a deliverable.

🟢 **Census result: `0` of `185` bodies on this shelf carry a rider or any source-available
family.** 🔵 **The platform tier is clean, and
[`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp)'s `Elastic-2.0` —
source-available, NOT open source, a higher-education student-success CRM — remains the only one
in this industry's published supply.** 🔴 **It stays on the DO-NOT-USE list.** 🟢 **The reader
was extended to catch riders anyway**, because the cost of finding the first one by accident is
a client deliverable built on a licence that forbids selling it.

## Pass 206 — 2026-10-14 — THE PLATFORM TIER, RE-READ FROM `15` BLOBS: THERE ARE EXACTLY `4` PERMISSIVE LMSs

### 🟢 Every row below was read from its own `LICENSE` blob at `HEAD` this pass. No secondary sources

| platform | repo | 🟢 grant, first-hand | bytes | what it is |
|---|---|---|---|---|
| 🟢 **OpenOLAT** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** | `10 982` | 🆕 **the ONLY full LMS on this shelf under a permissive grant.** Java, modular course editor, universities and corporates. Switzerland → **EMEA** |
| 🟢 **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`** | `11 120` | Apache-2.0 **modified for university IP**; OSI-approved and permissive. → **North America** |
| 🟢 **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** | `1 097` | **offline-first** learning platform — the low-connectivity answer. Global, heavy LATAM/Africa deployment |
| 🟢 **Richie** | [`openfun/richie`](https://github.com/openfun/richie) | 🟢 **`MIT`** | `1 079` | course-catalogue / marketing front end for Open edX. France → **EMEA** |
| 🟡 **OpenEduCat** | [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | 🟡 **`LGPL-3.0`** | `8 241` | the **Odoo analogue for education**: admissions, LMS, SIS, parent app. India → **APAC**. 🟢 LGPL permits linking from closed code |
| 🟡 **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🟡 **`LGPL-3.0`** | `7 652` | virtual classroom / conferencing. → **North America** |
| 🔴 **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** | `35 147` | the installed base. 🔴 **Plugins are derivative works: a Moodle plugin is GPL** |
| 🔴 **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **`GPL-3.0`** | `35 147` | strong Spanish-speaking and LATAM install base |
| 🔴 **H5P** | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **`GPL-3.0`** | `35 146` | interactive content, embedded in most of the LMSs above |
| 🔴 **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | `35 136` | 🔴 **network copyleft: a hosted modification must be published** |
| 🔴 **Tutor** | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **`AGPL-3.0`** | `34 523` | the Docker distribution of Open edX; **same reciprocity** |
| 🔴 **Canvas** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **`AGPL-3.0`** | `34 520` | Community Edition. 🔴 Cloud features remain proprietary |
| 🔴 **Frappe Learning** | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **`AGPL-3.0`** | `33 893` | 🔴 **A widely-repeated comparison this pass called it *"MIT, self-hosted data ownership"*. The blob says `AGPL-3.0`.** India → **APAC** |
| 🟡 **Frappe Education** | [`frappe/education`](https://github.com/frappe/education) | 🟡 **`GPL-3.0-STATEMENT`** | **`19`** | SIS on Frappe. 🔴 **Nineteen bytes: `License: GNU GPL V3`. The family is named, the instrument is not shipped** |
| 🟡 **Forma LMS** | [`formalms/formalms`](https://github.com/formalms/formalms) | 🟢 **`GPL-2.0`** *(🆕 `P214-2`)* | `18 346` B · `html/license.txt` | 🟢 **RESOLVED: the grant is in-tree, not at the root.** `html/license.txt` *(`18 346` B)* and `html/lib/System/license/license_english.txt` *(`15 146` B, + `9` translations)* both carry **GNU GPL Version 2, June 1991**. 🔴 **The earlier *"no licence body at all"* was a ROOT-ONLY reading**; the `Apache-2.0` an article reported is a vendored `jsdoc/prettify` file |

### 🔴 The two corrections that cost money, and both were secondary sources, not this KB

🔴 **`frappe/lms` is `AGPL-3.0`, not `MIT`.** 🔵 A studio that picked it on the strength of the
comparison article would have built a hosted product on a **network-copyleft** base and owed its
modifications back. 🟢 **`33 893` B of body, read this pass.**

🟢 **`formalms/formalms` IS granted: `GPL-2.0`**, body in-tree at `html/license.txt` *(`18 346` B,
re-read binary-safe p215)*. <!--corrected--> 🔴 **This KB carried *"no licence body"* here for `35`
passes; p214 resolved it and this cell was not updated.** 🔵 Three articles still name three
different families, and the repository DOES settle it — one directory down. 🟡 **The
`22`%-ungranted figure for the PLATFORM tier is therefore an OVERCOUNT**, and `P215-1` prices
that: `25` of `94` rows this KB called ungranted carry a grant off-root.

### 🆕 🟢 The sourcing rule this tier now has

🟢 **`4` of `15` platforms are permissive: `OpenOLAT` (`Apache-2.0`), `Sakai` (`ECL-2.0`),
`Kolibri` (`MIT`), `Richie` (`MIT`).** 🔴 **`8` are `GPL`/`AGPL` copyleft, `2` are `LGPL`, and
`1` has no grant.**

🔵 **So the decision is made at the base, not at the AI layer:** 🟢 **if the deliverable is a
hosted, closed product, the base is `OpenOLAT` or `Sakai`** — 🔴 **anything built by modifying
Open edX, Tutor, Canvas or Frappe Learning and then hosted triggers `AGPL` publication.** 🟢 **If
the deliverable is a plugin or an LTI tool, the base does not matter**: `instructure/ims-lti`
(`MIT`) launches an external tool from inside any compliant LMS **without touching platform
source**, which is the one route that avoids reciprocity entirely.

### 🔴 The LATAM school-system tier, re-read in its own language

🟢 **[`portabilis/i-diario`](https://github.com/portabilis/i-diario)** *(diário de classe)* and
🟢 **[`portabilis/pre-matricula-digital`](https://github.com/portabilis/pre-matricula-digital)**
*(pre-enrolment)* — Brazilian **municipal** school-management systems, deployed by secretarias de
educação. 🔴 **Both `AGPL-3.0`, `35 326` B each.** 🆕 **Their grant is written in Portuguese
(`LICENÇA PÚBLICA GERAL AFFERO GNU`), which is why every prior pass of this KB read them as
`UNRECOGNISED`.** 🔵 **They are the closest thing LATAM has to an `OpenSIS`, they are real
municipal infrastructure, and a SaaS layer over either of them must be published.**

## Pass 205 — 2026-10-14 — `moodle` IS `GPL-3.0` AND THIS PASS NEARLY PUBLISHED OTHERWISE

### 🔴 The vertical shelf's biggest row was a false negative, and the cause was a path list

🔴 **p205's first grant sweep reported [`moodle/moodle`](https://github.com/moodle/moodle) — the
single most-deployed platform in this industry — as having NO licence file.** 🟢 **It has one:
`COPYING.txt`, `GNU GENERAL PUBLIC LICENSE Version 3`, read from its own blob this pass.** 🔴 **The
`12` path forms inherited from p203 do not include `COPYING.txt`.**

🟢 **Same cause, second vertical row:** [`frappe/lms`](https://github.com/frappe/lms) ships
`license.txt` (**`AGPL-3.0`**) and was also reported ungranted. 🔵 **Lowercase `license.txt` and
`COPYING.txt` are both common in PHP and Python platform projects — exactly the stack this shelf
is made of.**

🟢 **The list is `16` forms now**, and 🟢 **p204's `58` ungranted rows were re-probed against the
`6` additions: `0` recovered**, so the `22`% figure is unaffected. 🔵 **But the lesson is
load-bearing: an ungranted RATE is a statement about a path list as much as about the repositories**,
and this shelf is where a false negative costs most — 🔴 **"Moodle is unlicensed" would have been
the single most damaging sentence this KB could emit.**

### 🟢 Vertical platform grants re-read at the `HEAD` ref, this pass

🔵 **Every row below was read from its own blob this pass** — no row is carried over.

| platform | repo | grant | path | note |
|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 **`GPL-3.0`** | `COPYING.txt` | 🔴 copyleft — plugins distributed with it inherit |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`** | `LICENSE` | 🔴 Apache-class, **narrower patent grant** *(p204 `T204-4`)* |
| **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🟡 **`LGPL-3.0`** | `LICENSE` | 🟢 linking permitted; modifications to BBB itself are not |
| **Canvas** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **`AGPL-3.0`** | `LICENSE` | 🔴 network use triggers source obligations |
| **Frappe LMS** | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **`AGPL-3.0`** | `license.txt` | 🆕 path corrected this pass |
| **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | `LICENSE` | 🔴 the MOOC substrate is itself AGPL |

🔵 **Nothing on this shelf is permissive.** 🟢 **That is not a defect in the shelf — it is the
shape of the LMS market**, and it means the permissive layer a studio builds on is always the
layer ABOVE the platform *(connectors, agents, analytics)*, never the platform itself. 🔴 **An
engagement that modifies Moodle or Canvas core ships source. Price that, or stay out of core.**

### 🔵 `ECL-2.0` is the one to read twice

🟢 **Sakai's grant re-read from its blob this pass: `Educational Community License, Version 2.0`.**
🔴 **p203's classifier returns `UNRECOGNISED` for it** — it has no ECL branch at all, although
p204 measured `ECL-2.0` on two rows. 🟢 **p205's classifier recognises it**, and the standing
reading is unchanged: **Apache-class for copying and redistribution, with a patent grant narrowed
to education use.** 🔵 **For an education deployment the narrowing is aligned with the use; for a
platform a studio intends to resell outside education, it is a counsel question.**

---

## Pass 204 — 2026-10-14 — A PLATFORM ROW THAT READS PERMISSIVE AND SHIPS COPYLEFT

### 🔴 `LearnPress` is the vertical row this pass corrects, and it was never blob-read

🔴 **[LearnPress/learnpress](https://github.com/LearnPress/learnpress)** is a WordPress LMS
plugin and a real vertical platform row — WordPress is the substrate a large share of small
institutions actually run on. 🔴 **Its grant was in this KB's ungranted population because no
`LICENSE` file exists on any branch.** 🟢 **Read this pass from two channels on its true
default branch `develop` @ `f9f2d6e2`:**

| channel | declares | authority |
|---|---|---|
| `package.json` | 🟢 `"license": "ISC"` | 🔴 **build tooling** — not the distributed plugin |
| 🔴 **`readme.txt`** | 🔴 **`License: GPLv3`** *(+ `License URI`)* | 🟢 **the WordPress plugin manifest — this governs what ships** |

🔴 **So the platform row is `GPL-3.0` and must be routed around exactly like Moodle.** 🟢 **A
pass that had read only `package.json` would have published the one permissive general-purpose
LMS this industry does not have.**

🔵 **The rule for this shelf, stated so it is reusable:** 🟢 **on a WordPress-ecosystem row,
`readme.txt` outranks `package.json`.** 🔴 **Never publish a vertical platform's licence from a
`package.json` alone.**

### 🟢 The platform shelf is unchanged, and now it is unchanged for a measured reason

🔴 **p203 concluded that every general-purpose LMS/SIS this industry runs on is copyleft.**
🟢 **p204 adds a row to the copyleft side and none to the permissive side:**

| Platform | role | grant | channel |
|---|---|---|---|
| **LearnPress** | LMS plugin on WordPress | 🔴 **GPL-3.0** | 🆕 🟢 **`readme.txt` blob-read this pass** |
| [opencast/opencast](https://github.com/opencast/opencast) | **lecture capture / video** | 🟡 **`ECL-2.0`** | 🆕 🟢 **blob-read, `develop` @ `ae86c6aa`** |
| Moodle | LMS, the reference | 🔴 GPL-3.0 | carried |
| Open edX | LMS at scale | 🔴 AGPL-3.0 *(platform)* | carried; verify per component |
| Canvas LMS | LMS, community edition | 🔴 AGPL-3.0 | carried |
| OpenOlat | LMS | 🟢 **Apache-2.0** | carried — still the only permissive general-purpose LMS |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 **AI-native LMS, self-hostable** | 🟢 **MIT** | 🟢 **re-verified `main` @ `242a9324`** |
| OpenEduCat | SIS + LMS on Odoo | 🔴 LGPL-3.0 *(bundled carve-outs)* | carried |
| rosariosis | SIS | 🔴 GPL-2.0 | carried |

🟢 **`opencast` is a genuinely useful addition to the vertical shelf** rather than a licence
curiosity: lecture capture is a line item in almost every higher-education engagement, and
🟢 **`ECL-2.0` is permissive for redistribution.** 🔴 **Its patent grant is narrowed to
education use — see `T204-4` in [`intel/trends.md`](../intel/trends.md).**

### 🟢 The permissive layer is still one level down, and it gained a second LRS

🔴 **The customisation shape this industry supports has not changed: take the copyleft platform
as the system of record, keep the client's work at the integration boundary.** 🟢 **The
permissive interop spine, every row blob-read at p203 or p204:**

**`ADL_LRS` (Apache-2.0)** · 🆕 **`yetanalytics/lrsql` (Apache-2.0, `main` @ `cb794e4b`)** ·
**`lrs-conformance-test-suite` (MIT)** · **`ralph` (MIT)** · **`pylti1.3` (MIT)** ·
**`1EdTech/lti-1-3-php-library` (Apache-2.0)** · **`ltiauthenticator` (BSD-3)** ·
**`CATAPULT` (Apache-2.0)** · **`scorm-h5p-wrapper` (MIT)** · **`LiaScript-Exporter` (BSD-3)** ·
**`marsha` (MIT)** · 🆕 **`jcputney/scorm-again` (MIT, `master` @ `25ca01f9`)** ·
🆕 **`numbas/Numbas` (Apache-2.0, `master` @ `8c7f23a6`)** ·
🆕 **`adlnet/xAPIWrapper` (Apache-2.0)** · 🆕 **`RusticiSoftware/TinCanJS` (Apache-2.0)** ·
🆕 **`RusticiSoftware/TinCanPython` (Apache-2.0, `3.x`)** ·
🆕 **`S4-NetQuest/react-scorm-provider` (MIT)**

🟢 **Two of these close real holes on this shelf:**

- 🟢 **`scorm-again` (MIT) is the permissive replacement for `cybercussion/SCOBot`**, which
  p203 flagged as 🔴 **a SCORM JavaScript API under `CC-BY-SA-4.0`** — a content copyleft over
  software. 🟢 **The remedy for p203's own finding is a row this KB already held.**
- 🟢 **`lrsql` (Apache-2.0) is a second permissive LRS beside `ADL_LRS`**, so the evidence
  layer is no longer single-sourced. 🔴 **`g3i/lxHive` (GPL-2.0) and `LearningLocker`
  (GPL-3.0) remain the rows to route around.**

🔴 **Excluded after reading, carried and extended:** `lxHive` *(GPL-2.0)*,
`oat-sa/lib-lti1p3-core` *(GPL-2.0)*, `Edlib` *(GPL-3.0)*, `SCOBot` *(`CC-BY-SA-4.0`)*,
🆕 `adaptlearning/adapt_framework` *(GPL-3.0)*, 🆕 `davidpesce/moodle-logstore_xapi`
*(GPL-3.0)*, 🆕 `Lumieducation/Lumi` *(AGPL-3.0, manifest-declared)*.

---

## Pass 203 — 2026-10-14 — THE PLATFORM SHELF IS COPYLEFT, AND THE INTEROP LAYER BESIDE IT IS NOT

🔴 **Every general-purpose LMS/SIS this industry actually runs on is copyleft, and p203
blob-read another one to confirm the pattern rather than assert it.**

| Platform | role | grant | channel |
|---|---|---|---|
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | **SIS** — grades, scheduling, attendance | 🔴 **GPL-2.0** | 🟢 **blob-read this pass**, `master/LICENSE` |
| Moodle | LMS, the reference everything is measured against | 🔴 GPL-3.0 | carried |
| Open edX | LMS at scale | 🔴 AGPL-3.0 *(platform)*, Apache-2.0 *(some components)* | carried; ⚠️ roundups disagree — **verify per component** |
| Canvas LMS | LMS, community edition | 🔴 AGPL-3.0 | carried; 🔴 **community edition excludes features the commercial one has** |
| OpenOlat | LMS | 🟢 **Apache-2.0** | carried — 🟢 **the one permissive general-purpose LMS on this shelf** |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | **SIS + LMS on Odoo** | carried *(p202: bundled-grant carve-outs)* | carried |

🟢 **So the vertical answer has not changed and p203 can now say WHY it does not change:**
a client who needs the system of record takes a copyleft platform and keeps their work at
the integration boundary. 🔴 **Searching for a permissive general-purpose LMS is a dead end —
`OpenOlat` is the single permissive option and it is not the market.**

### 🟢 What DID change: the permissive layer is one level down, and it is now blob-read

🔴 **p202 found the interop layer (`~1 088` repositories) and published its spine
unread. p203 read it.** 🟢 **`10` rows, every grant read from its own blob, nothing
copyleft:**

**`ADL_LRS` (Apache-2.0)** · **`lrs-conformance-test-suite` (MIT)** · **`ralph` (MIT)** ·
**`pylti1.3` (MIT)** · **`1EdTech/lti-1-3-php-library` (Apache-2.0)** ·
**`ltiauthenticator` (BSD-3)** · **`CATAPULT` (Apache-2.0)** · **`scorm-h5p-wrapper` (MIT)**
· **`LiaScript-Exporter` (BSD-3)** · **`marsha` (MIT)**

🔴 **Excluded after reading: `lxHive` (GPL-2.0), `oat-sa/lib-lti1p3-core` (GPL-2.0),
`Edlib` (GPL-3.0), `SCOBot` (`CC-BY-SA-4.0`).**

🟢 **The customisation shape this industry actually supports, stated plainly:** 🔴 **you do
not fork the LMS.** 🟢 **You speak `LTI 1.3` into it, emit `xAPI` out of it to an LRS you own,
and keep every line you write on the permissive side of that boundary** — which is exactly
where the `10` rows above sit. **The copyleft platform stays unmodified and its licence
never reaches your work.**

### 🆕 🟢 The content layer the platform shelf never had

🟢 **New this pass:** the Carpentries family — `12` rows, **`CC-BY-4.0` for instructional
material and MIT for example code, in one instrument**, propagated by the lesson template
[`carpentries/lesson-example`](https://github.com/carpentries/lesson-example). 🟢 **This is
the first row on this shelf that is curriculum rather than software, with a grant explicit
enough to ship:** `CC-BY` permits commercial adaptation with attribution, and the code
examples inside the same repository are separately MIT.

🔴 **The trap, and it is one line away:** `CC-BY` *(Carpentries)* permits a closed
adaptation; **`CC-BY-SA`** *(`education-agent-skills` `858★`, `SCOBot` `164★`)* does **not** —
the adaptation must carry the same licence. 🟢 **Same four letters at the front, opposite
answer to "can we ship this to a client", and only a blob read tells you which you have.**

## Pass 202 — 2026-10-14 — THE STANDARDS LAYER IS THE VERTICAL NOBODY SELLS, AND IT IS PERMISSIVE

🔵 This page exists for the Odoo/OpenMRS/Moodle move: **start from something that already
works and add the agentic layer on top.** 🟢 **This pass adds a vertical the KB had missed
for `201` passes — and unlike the LMS layer, it is NOT copyleft.**

### 🟢 The platforms, with the licence that decides whether you can ship on them

| Platform | What it is | Licence *(source)* | ★ | Region | The agentic layer to add |
|---|---|---|---|---|---|
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | Interactive learning + automated feedback; exam mode | 🟢 **MIT** · `1 091` B *(p201 blob)* | **818** | TU Munich → **EMEA** | 🟢 **Still the best insertion point in this KB.** Already carries `gen-ai` and `text-exercises`. 🔴 **And `exam grading` is Annex III high-risk from `2027-12-02`** |
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | Submission + automated **and TA** grading | 🟢 **BSD-3-Clause** *(p201 blob)* | **803** | RPI → North America | The human-in-the-loop half; add LLM free-text grading **behind** its existing TA workflow |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🆕 Learning Record Store on SQL | 🟢 **Apache-2.0** *(blob)* | **144** | North America | 🟢 **The permissive memory substrate.** Agent emits xAPI statements; your BI stack reads the same tables |
| [adaptlearning/adapt_framework](https://github.com/adaptlearning/adapt_framework) | 🆕 HTML5 course authoring, accessible + multilanguage | 🔴 **GPL-3.0, v3-only** *(blob + README)* | **631** | → EMEA | Agent authors the course JSON; Adapt renders it. 🔴 **GPL-3.0 v3-only: a SaaS wrapper is fine, a redistributed closed fork is not** |
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | 🆕 Framework for building LTI tools | 🟢 **Apache-2.0** *(blob)* | **376** | North America | 🟢 **The install path.** Wrap any agent as an LTI 1.3 tool and every Moodle/Canvas/Blackboard becomes a deployment target |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | AI-native LMS, SCORM + xAPI, white-label | 🟢 **MIT** *(p201 blob)* | **95** | Selleo → **EMEA** | 🟢 **MIT LMS with the AI mentor already in it** — the fastest white-label demo in this KB |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Full university LMS | 🟢 **Apache-2.0** *(p199)* | **447** | Switzerland → **EMEA** | The permissive LMS exit. Carries `topic:scorm` natively |
| [Berserk-hub150/moodle-ai-skill-navigator](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) | 🆕 AI tutoring/assessment **inside** Moodle | 🔴 **GPL-3.0-or-later** *(README)* | **223** | → UNDETERMINED | 🟢 **Teachers choose which materials the AI may use** — consent-by-design, and the default provider makes no network calls |
| [INGInious/INGInious](https://github.com/INGInious/INGInious) | Sandboxed assessment with LTI | 🔴 **AGPL-3.0** *(p201 blob)* | **243** | UCLouvain → **EMEA** | 🔴 **AGPL + SaaS compels disclosure to the client's end users.** Use as an internal sandbox, not a hosted product |
| [numbas/Numbas](https://github.com/numbas/Numbas) | Browser-based maths e-assessment | *(p117 evidence on disk)* | **215** | Newcastle Univ → **EMEA** | Agent generates question variants; Numbas marks them deterministically |
| [moodle/moodle](https://github.com/moodle/moodle) · Chamilo · ILIAS | The installed base | 🔴 **GPL-3.0** — 🆕 **Chamilo is `-or-later`** | — | Global | Plugin layer, never a fork. **`916` `topic:moodle-plugin` repositories is the real market signal** |

### 🔴 The licence map of this vertical, and it is the opposite of the LMS layer

🔴 p201's finding stands and sharpens: **the modern LMS layer is AGPL** (`frappe/lms`,
`learnhouse`, `classroomio`, `courselit`, `tutor`, `Claroline`), and **with `71`% cloud
deployment AGPL + SaaS is the one combination that can compel disclosure to a client's end
users.** 🟢 **But the standards layer added this pass is permissive almost throughout** —
`Apache-2.0` for `lrsql` and `tsugi`, `MIT` for `scorm-again` and `ralph`, `BSD-3` for
`Submitty`, `MIT` for `Artemis` and `mentingo`.

🟢 **So the architecture that survives a commercial deliverable is: permissive standards
layer (xAPI/LTI/SCORM) + permissive assessment core (`Artemis`/`Submitty`) + the copyleft
LMS left strictly as an integration target you never fork.** That sentence decides more than
any market figure on [`intel/market.md`](../intel/market.md).

### 🔴 🆕 And a verdict a licence badge cannot give you: `CURRENTLY`

[`PlaypowerLabs/EdOptimize`](https://github.com/PlaypowerLabs/EdOptimize) (`31★`, K-12
learning analytics, three dashboards) states in its README: **`"CURRENTLY, THIS PLATFORM IS
LICENSED GPLv3."`** 🔴 **An express reservation of the right to change the grant.** The code
you take today stays GPL-3.0 forever, but the project's future is not a dependency you can
plan on. 🔵 **A new column this KB should carry: is the grant declared as permanent or as
provisional?** `ACTION OU`.


## Pass 201 — 2026-10-14 — THREE PLATFORMS WHOSE LICENCE IS NOT WHAT A SCANNER SAYS

🔵 **p200's SIS/ERP table stands.** What this pass adds is the class of platform where the
licence **column itself is the wrong shape** — and all three rows have real adoption.

### 🔴 `leemonade/leemons` (`291★`) is NOT open source, and no scanner will tell you

🟢 Read from its own blob this pass — `LICENSE.md`, `10 830` B:

> *"Content outside of the above mentioned files or restrictions is available under the **"Fair
> code License"** as defined below… **Terms and Conditions of Use for the Fair Code License of
> Leemons, Version 1.0**"*

🔴 **A bespoke, non-OSI licence on a `291★` LMS/LXP that markets itself as open source.** 🔵 This
is the `n8n` shape *(Sustainable Use License)* arriving in education. 🟢 **GitHub's API says
`NOASSERTION` — correctly conservative — and this KB's own `family_of` answers `FAIRCODE`**, so
the control exists; what was missing was anyone looking. 🔴 **Verdict for AI Studios: not
usable in a client deliverable without a commercial agreement. Do not shortlist it.**

### 🟡 Two platforms whose grant depends on WHICH DIRECTORY you take

🟢 `ACTION OJ`'s population is `3` repositories, `1 841★` combined — not the one p200 found:

| repo | ★ | path pattern | grant | shippable in a closed deliverable? |
|---|---|---|---|---|
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | **572** | `skills/**` | **AGPL-3.0 OR MIT**, licensee's option | 🟢 **YES, via the MIT option** |
| | | `app/**` | **AGPL-3.0** only | 🔴 **NO** |
| [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | **978** | `docs/**` | **CC-BY-SA-4.0** | 🟡 content ShareAlike attaches |
| | | client-side JavaScript *(incl. compiled output)* | **MIT** | 🟢 **YES** |
| | | everything else | **MIT** | 🟢 **YES** |
| [leemonade/leemons](https://github.com/leemonade/leemons) | **291** | third-party components | each owner's own licence | per component |
| | | everything else | **Fair Code License v1.0** | 🔴 **NO** |

🔴 **And here is the trap that makes a scope reader mandatory rather than nice to have:
`pupilfirst` and `leemons` open with the SAME boilerplate sentence, verbatim** —
*"Portions of this software are licensed as follows:"* — **and they end in opposite places.**
One resolves to **MIT**; the other to a **non-OSI** licence. 🟢 **So the preamble is a SHAPE, not
a verdict: an instrument must read every bullet to the end and emit `(path pattern → grant)`
pairs.** 🔵 A repo-level licence column cannot represent any of these three rows, which is why
this table carries paths.

🟢 **The commercially useful read, stated plainly:** `human-skill-tree`'s **`skills/` payloads
are MIT-takeable** — a studio may embed those `SKILL.md` files in a client deliverable and must
not fork the `app/`. That is the single most shippable asset on the agent-skill shelf.
[`evidence/split-scope-notices.2026-10-14-p201.tsv`](../evidence/split-scope-notices.2026-10-14-p201.tsv)

### 🟢 The platform shelf an engagement actually chooses from — licence from bytes, this hour

| Layer | Platform | Licence | ★ | Customisable with AI on top? |
|---|---|---|---|---|
| **LMS / VLE** | [Moodle](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** `35 147` B | — | Yes — **over Web Services + the `8` MCP servers in [`agents/top.md`](../agents/top.md)**; do not fork into a closed deliverable |
| | [Open edX](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** `35 136` B | — | Yes — **via `XBlock` (Apache-2.0)**; `tutor` (AGPL) is the distribution |
| | [Chamilo](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0-**or-later** `35 147` B | **1 013** | Strong LATAM + francophone Africa footprint. 🆕 **or-later**, per its own notice |
| | [ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL-3.0** `35 147` B | **505** | German-speaking EMEA. Branch `release_11` |
| | [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** `10 982` B | **447** | 🟢 **The permissive full-LMS exit.** QTI, SCORM, curriculum management |
| | [Sakai](https://github.com/sakaiproject/sakai) | 🟡 **ECL-2.0** `11 120` B | **1 238** | Apache-2.0 with the § 3 patent grant **narrowed to education** — contract review, not a label |
| | 🆕 [mentingo](https://github.com/Selleo/mentingo) | 🟢 **MIT** `1 062` B | **95** | 🟢 **AI-native by design: AI mentor + role-play, SCORM + xAPI, white-label** |
| | 🆕 [ulearn](https://github.com/safytech/ulearn) | 🟢 **MIT** `1 066` B | **700** | Laravel + React |
| **SIS / school ERP** | 🆕 [academico](https://github.com/academico-sis/academico) | 🟢 **MIT** `1 094` B | **404** | 🟢 **The permissive SIS+LMS.** Laravel + Filament — **the row this layer was missing** |
| | [RosarioSIS](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** `15 214` B | **646** | Gradebook, attendance, billing. Branch `mobile` |
| | [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 **GPL-2.0** `17 286` B | **345** | Grant at `docs/License.txt` **with a UTF-8 BOM** |
| | [OpenEduCat](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0** `8 241` B | — | 🟢 **Education ERP on Odoo** — weak copyleft, so **linkable**: the practical middle for an ERP engagement |
| **Content runtime** | [H5P](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** `35 146` B | — | Copyleft reaches the interactive-content runtime |
| | 🆕 [scorm-again](https://github.com/jcputney/scorm-again) | 🟢 **MIT** `1 072` B | **355** | 🟢 **SCORM 1.2/2004 runtime, offline-first** — the standards piece, permissive |
| **Catalogue** | 🆕 [richie](https://github.com/openfun/richie) | 🟢 **MIT** `1 079` B | **316** | Course catalogue/marketing CMS in front of Open edX or Moodle **without inheriting AGPL** |
| **Synchronous class** | 🆕 [flat](https://github.com/netless-io/flat) | 🟢 **MIT** `1 062` B | **6 439** | Whiteboard + recording, desktop and web clients |
| | 🆕 [OpenVidu](https://github.com/OpenVidu/openvidu) | 🟢 **Apache-2.0** `11 357` B | **2 136** | Self-hosted WebRTC on LiveKit; `ai-agents` in its own topics |
| | [BigBlueButton](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0** | — | 🔵 Carried from cycle 3; not re-read this pass |
| **Offline / low-bandwidth** | [Kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** `1 097` B | — | 🟢 The LATAM/Africa deployment shape |
| **Assessment / grading** | 🆕 [Artemis](https://github.com/ls1intum/Artemis) | 🟢 **MIT** `1 091` B | **818** | 🟢 **The one platform already doing gen-AI feedback under a permissive licence** |
| | 🆕 [Submitty](https://github.com/Submitty/Submitty) | 🟢 **BSD-3-Clause** `1 542` B | **803** | Automated **and TA** grading — human-in-the-loop built in |
| | 🆕 [INGInious](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** `34 764` B | **243** | Sandboxed assessment **with LTI into any LMS** |
| **Lecture capture** | [Opencast](https://github.com/opencast/opencast) | 🟡 **ECL-2.0** `11 340` B | **508** | 🟢 Front-ended by [`paella`](https://github.com/polimediaupv/paella) — **ECL-2.0, `9 915` B, grant now FOUND** |

🔴 **Three rows a shortlist must exclude on licence grounds alone**, all with real stars:
`leemons` (`291★`, Fair Code), `LMS-Laravel` (`505★`, **no grant on any channel**) and
`LearnPress` (`275★`, **no grant, not even in its WordPress plugin header**). 🟢 **Checking this
costs one `curl`; discovering it after a SOW costs a renegotiation.**


## Pass 200 — 2026-10-14 — THE SIS/ERP LAYER, DECIDED BY LICENCE

🔵 **p199's platform table stands; this section fills the half of it that was thinnest.** p199
listed four student-information systems without star counts, because star counts were
unreadable to it. 🟢 **With the API channel open *(see [`agents/top.md`](../agents/top.md))*
the whole `topic:school-management` shelf above `200★` is enumerable — `7` repositories — and
once the licences are read from their own blobs, the decision collapses to two options.**

### 🟢 Education SIS / school ERP — ranked, then filtered by what Globant can actually ship

| Platform | Repo | Licence *(blob, bytes)* | Stars · forks | Verdict |
|---|---|---|---|---|
| **LAVSMS** | [4jean/lav_sms](https://github.com/4jean/lav_sms) | 🟢 **MIT** · `1 072` B | **1 042** · `650` | 🟢 **The permissive pick.** Laravel/PHP: exams, marksheets, teachers, results. Embeddable in a closed deliverable |
| **Skuul** | [yungifez/skuul](https://github.com/yungifez/skuul) | 🟢 **MIT** · `1 069` B | **409** · `147` | 🟢 **Permissive AND multi-school** — built multi-tenant, which is what a group, network or ministry deployment actually needs |
| School Management System | [hrshadhin/school-management-system](https://github.com/hrshadhin/school-management-system) | 🔴 **AGPL-3.0** · `34 522` B | **1 145** · `994` | 🔴 **The most-starred, and the one to avoid.** AGPL is *network* copyleft: hosting it for a client can trigger source disclosure |
| **Frappe Education** | [frappe/education](https://github.com/frappe/education) | 🔴 **GPL-3** — by a **`19`-byte reference** | **665** · `455` | Odoo-alternative education ERP on ERPNext. 🔴 Its `license.txt` reads `License: GNU GPL V3` *and nothing else* — the grant is not in this repo |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** · `15 214` B | **646** · `391` | K-12, multilingual incl. ES/PT → **LATAM**. 🔵 **Default branch is `mobile`** |
| **openSIS Classic** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 **GPL-2.0** · `17 286` B at **`docs/License.txt`** | **345** · `288` | 🔴 **No licence at root** — a root-only scan calls this unlicensed and is wrong |
| School Management System *(PHP)* | [ProjectsAndPrograms/school-management-system](https://github.com/ProjectsAndPrograms/school-management-system) | 🟡 **`MIT` at `student_panel/LICENSE`** *(`1 070` B, p215)* <!--corrected--> | **206** · `111` | 🟡 **Granted, but weakly:** the `MIT` text sits in ONE subdirectory and is copyright an individual contributor, not the org; the root and the other modules carry nothing, and `phpmailer/LICENSE` is vendored `LGPL-2.1`. 🔵 Usable with the provenance written down |
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0** · `8 241` B | — | Odoo-based: admissions, LMS, SIS, parent app. 🟡 Weak copyleft — **linkable**, the practical middle. 🔵 **Default branch is `19.0`** |

🟢 **The one-line answer an engagement needs: of the seven most-adopted school-management
systems in open source, exactly two are permissive — `lav_sms` (MIT, `1 042★`) and `skuul`
(MIT, `409★`), both Laravel — and the single most-starred option is AGPL.** 🔵 Popularity and
licence point in opposite directions here, which is the whole reason this table is worth
reading before a proposal rather than after.

🔴 **And the Odoo analogue is weaker than cycle 2 implied.** Cycle 2 named OpenEduCat as the
"Odoo for education." It is LGPL-3.0 and real — but `frappe/education`, the other candidate, is
**GPL-3 asserted in a nineteen-byte file whose grant text lives in another repository.** For a
client deliverable, *"the licence of this component cannot be established from this component"*
is a finding, not a technicality.

### 🔴 ECL-2.0 platforms need a contract step, not just a licence column

[`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) (**1 238★**) and
[`opencast/opencast`](https://github.com/opencast/opencast) (**508★**) are **ECL-2.0**:
Apache-2.0 with **the § 3 patent grant narrowed to "the needs of the education communities."**
🟢 p199 flagged the clause; **this pass read the text and counted the family — `18` repos
GitHub-wide** *(see [`repos/foundations.md`](../repos/foundations.md))*. 🔵 **Practical
consequence for a platform choice:** permission-wise ECL-2.0 behaves like Apache-2.0, so builds
and redistribution are fine; **patent-wise the peace is scoped**, so if the deliverable serves a
non-education licensee or a non-education purpose, that scoping is a question for counsel
**before** the SOW, not a line in a compliance appendix.

### 🟢 Where this leaves the platform decision, by region

- **LATAM** — Moodle and **Chamilo** remain the installed base (both **GPL-3.0**, so integrate
  over Web Services, don't embed); **Kolibri (MIT)** where connectivity is the binding
  constraint; **`skuul` (MIT)** if a new multi-school SIS is in scope. 🔵 `RosarioSIS` is the
  Spanish/Portuguese-friendly incumbent but GPL-2.0.
- **EMEA** — **OpenOLAT (Apache-2.0)** is the only permissive full LMS; **ILIAS** for
  German-speaking assessment-heavy institutions (GPL-3.0, branch `release_11`); **Opencast
  (ECL-2.0)** for lecture capture, with the patent-scope step above.
- **North America** — Canvas and Open edX dominate; **`edx-platform` is the one genuine AGPL
  platform in this set**, so extend it with `XBlock` (`Apache-2.0`) and never fork it into a
  hosted product.
- **APAC** — Moodle plus the **Frappe/ERPNext** stack where finance is already on ERPNext
  (`GPL-3.0`, `license.txt` **lowercase**); **OpenEduCat (LGPL-3.0)** out of India.

## Pass 199 — 2026-10-14 — CANONICAL PLATFORM TABLE (read this section first)

The customisable systems an engagement actually lands on. **Licence read from the repo's own
blob this pass**; default branch resolved first, because several of these do not use `main`.

### Learning platforms (LMS)

| Platform | Repo | Licence *(blob read)* | Origin → region | Why it shows up in an engagement |
|---|---|---|---|---|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | **GPL-3.0** *(`COPYING.txt`)* | Australia → **APAC** | The global installed-base default, dominant in EMEA public education and LATAM universities. Plugin architecture + Web Services REST API = the AI attach point **without forking** |
| **Open edX** | [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | Axim Collaborative *(Harvard/MIT)* → **North America** | MOOC-scale cohorts, strong authoring. Run it with `overhangio/tutor`; extend it with `XBlock`, never by forking the platform |
| **Canvas LMS** | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | US → **North America** | Dominant in US HiEd. 🔵 Instructure's parent announced an **OpenAI partnership to build AI into the platform**, so a 2026 Canvas engagement is competing with first-party features — integrate at the MCP layer rather than rebuilding the gradebook |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | **GPL-3.0** | Spain/Belgium → **EMEA** | Strong Spanish/French-language footprint; genuinely used across **LATAM** public institutions. 🟢 Underrated for a Spanish-first deployment |
| **ILIAS** | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | **GPL-3.0** | Germany → **EMEA** | German-speaking universities and public sector; built around formal assessment, which maps directly onto EU AI Act high-risk duties |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | Switzerland → **EMEA** | 🟢 **The only major LMS on this list with a permissive licence.** If a client needs to embed LMS code in a proprietary product, this is the short list |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | US consortium → **North America** | Apereo-stewarded HiEd suite; ECL-2.0 is Apache-derived with an education-specific patent clause |
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** · `1.1k`★ | → **Global** | 🟢 **Offline-first and MIT.** The right answer where bandwidth, not pedagogy, is the binding constraint |
| **Oppia** | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** · `6.9k`★ | → **Global** | Interactive lessons with built-in misconception handling; permissive and forkable |

### Student information systems & education ERP

| Platform | Repo | Licence | Note |
|---|---|---|---|
| **OpenEduCat** | [OpenEduCat/openeducat_erp](https://github.com/OpenEduCat/openeducat_erp) | **LGPL** | **Odoo-based** education ERP: admissions, LMS, SIS, parent app in one. 🟢 The Odoo analogue for education — and LGPL is friendlier than the AGPL LMSs above. India → **APAC** |
| **Frappe Education** | [frappe/education](https://github.com/frappe/education) | **GPL-3.0** *(`license.txt`, branch `develop`)* | SIS on the Frappe/ERPNext stack; strong **APAC** (India) adoption, pairs with existing ERPNext finance |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | **GPL-2.0** | K-12 SIS, PHP; multilingual incl. Spanish/Portuguese → useful in **LATAM** |
| **Gibbon** | [GibbonEdu/core](https://github.com/GibbonEdu/core) | **GPL-3.0** | K-12, blends SIS with teaching/learning rather than bolting them together |

### Classroom infrastructure & assessment

| Platform | Repo | Licence | Note |
|---|---|---|---|
| **BigBlueButton** | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | **LGPL** | Purpose-built virtual classroom (not a meeting tool): breakouts, polls, shared whiteboard; native Moodle/Canvas integrations |
| **Jitsi Meet** | [jitsi/jitsi-meet](https://github.com/jitsi/jitsi-meet) | **Apache-2.0** | Permissive self-hosted video when BBB's LGPL or weight is wrong |
| **Opencast** | [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** | Automated lecture capture → the corpus a tutoring agent should be grounded in |
| **H5P** | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | **GPL-3.0** | ~50 interactive content types usable inside Moodle/Canvas/Drupal |
| **INGInious** | [UCL-INGI/INGInious](https://github.com/UCL-INGI/INGInious) | **AGPL-3.0** | Sandboxed secure code assessment; UCLouvain → **EMEA** |
| **Pawtograder** | [pawtograder/platform](https://github.com/pawtograder/platform) | **GPL-3.0** | CS-course platform: Actions autograding, rubrics, office hours, gradebook |
| **Richie** | [openfun/richie](https://github.com/openfun/richie) | **MIT** | Course catalogue/CMS front end for Open edX; France Université Numérique → **EMEA** |

### 🟢 The 2026 shift worth acting on

In cycles 2–3 this section was a list of platforms to *customise*. **The change this pass
records is that the integration layer now exists off the shelf**: `6` MIT-licensed Canvas MCP
servers and `2` Moodle MCP servers were verified alive today (`agents/top.md`). The work has
moved from *"build an LMS integration"* to *"choose, fork and harden one, then spend the budget
on pedagogy and evidence."* 🔴 **No official MCP server exists from Instructure or Moodle HQ** —
so that fork is the engagement's own asset, and its maintenance is a line item.
## Pass 198 — 2026-10-14

🆕 🔴 **The open web was wrong about `2` of the `8` biggest platforms at p196. This pass swept
wider and found `3` MORE errors — and all `3` run in the same permissive direction.** 🟢 Every
platform row below carries a licence read from **bytes**, on a branch **resolved** rather than
guessed.

### 🔴 Five web licence claims, measured against bytes

| platform | 🔴 the open web says | 🟢 the bytes say | verdict |
|---|---|---|---|
| 🆕 🔴 [`formalms/formalms`](https://github.com/formalms/formalms) | 🔴 *"Apache 2.0"* | 🟢 **`GPL-2.0`** · `15 146` B — 🔴 **and nothing at the root** | 🔴 **WRONG.** Copyleft reported as permissive |
| 🆕 🟡 [`foradian/fedena`](https://github.com/foradian/fedena) | 🔴 *"Apache 2.0"* | 🟡 Apache-2.0 **declared in `NOTICE`** `679` B — 🔴 **no licence text shipped anywhere** | 🟡 **family right, grant thinner than stated** |
| 🆕 🔴 [`frappe/education`](https://github.com/frappe/education) | 🔴 `GPL-3.0` *(sidebar)* | 🔴 **`license.txt` = `19` bytes:** `License: GNU GPL V3` | 🔴 **a POINTER, not a grant** |
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 split: `AGPLv3` **or** `Apache-2.0` | 🟢 **`AGPL-3.0`** · `35 136` B | 🔴 the Apache claim is **WRONG** *(re-confirmed)* |
| 🔴 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 *"Apache 2.0"* | 🟢 **`ECL-2.0`** · `11 120` B | 🔴 **WRONG** *(re-confirmed)*. ECL is Apache-*derived*, not the same grant |
| 🔴 [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 one source: *"Apache License 2.0"* | 🟢 **`AGPL-3.0`** · `34 520` B | 🔴 **WRONG** — 🆕 a **new** source made this error this pass |

🔴 **Six claims, six errors or understatements, every one of them optimistic.** This is now
measured across two consecutive passes and `10`+ sources. 🟢 **The structural conclusion:
licence claims about education platforms on the open web are not merely noisy — they are
BIASED, and the bias costs the client.** A studio that takes *"Open edX is Apache-2.0"* or
*"Forma LMS is Apache-2.0"* from a comparison blog and ships a hosted deliverable has adopted
a copyleft obligation it does not know it has.

### 🆕 🔴 `formalms` ships its licence as a TRANSLATED UI ASSET, and `3` of the `9` are one file

🔵 Tree enumeration *(`5 321` paths)* returns **nothing licence-named at the root.** The grant
lives at `html/lib/System/license/license_english.txt` alongside `8` translations:

| language | bytes | 🟢 family *(title line)* | note |
|---|---|---|---|
| 🟢 **english** | `15 146` | 🟢 **`GPL-2.0`** | 🟢 **THE ONLY LEGALLY OPERATIVE TEXT** — the FSF holds translations unofficial |
| croatian | `18 011` | `GPL-2.0` | 🔴 **byte-identical** to bosnian + tamil |
| bosnian | `18 011` | `GPL-2.0` | 🔴 **byte-identical** to croatian + tamil |
| tamil | `18 011` | `GPL-2.0` | 🔴 **byte-identical** — `3` "translations", **one file** *(md5 `eb723b61…`)* |
| italian | `22 483` | 🟡 `GPL?` | version not resolvable from a translated title |
| french | `22 154` | 🔴 `LGPL?` *(window rule)* | 🔴 a translated title misread as **LESSER** |
| german | `23 652` | `GPL-2.0` | — |
| spanish | `19 978` | 🔴 `NO-FAMILY` | no title line this instrument recognises |
| portuguese | `20 506` | 🟡 `GPL?` | — |

🔵 **Declared limit of the instrument, not of the documents:** the grant detector is
**English-only**, so every translated body scores `GRANT?-NON-EN`. That is a property of the
reader. 🔵 [`evidence/formalms-translated-licence.2026-10-14-p198.tsv`](../evidence/formalms-translated-licence.2026-10-14-p198.tsv).

### 🟢 The platform shelf — `13` rows, licence from BYTES, branch RESOLVED

| platform | repo | 🟢 licence *(bytes)* | branch | what it is |
|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** · `35 147` B at `COPYING.txt` | `main` | the largest installed LMS base worldwide |
| **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** · `35 136` B | `master` | higher-ed/MOOC platform |
| **Tutor** | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **`AGPL-3.0`** · `34 523` B | 🔵 **`release`** | the Docker distribution that makes Open edX operable |
| **Canvas** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **`AGPL-3.0`** · `34 520` B | `master` | North American university incumbent |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** · `11 120` B | `master` | research-university collaboration/learning environment |
| 🟢 **OpenOLAT** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** · `10 982` B | `master` | 🟢 **the one permissive university LMS** |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **`GPL-3.0`** · `35 147` B | `master` | LMS with deep LATAM + francophone-Africa deployment |
| **Forma LMS** | [`formalms/formalms`](https://github.com/formalms/formalms) | 🔴 **`GPL-2.0`** · `15 146` B *(off-root)* | `master` | corporate-training LMS, Docebo fork lineage |
| 🟢 **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** · `1 097` B | `develop` | 🟢 **offline-first** — the low-connectivity primitive |
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 **`LGPL-3.0`** · `8 241` B | 🔵 **`19.0`** | education **ERP/SIS** on Odoo: admissions, attendance, fees, gradebook |
| **Gibbon** | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **`GPL-3.0`** · `35 121` B | 🔵 **`v31.0.00`** | K-12 school management |
| **RosarioSIS** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** · `15 214` B | 🔵 **`mobile`** | student information system — 🟡 **v2, a different compatibility story** |
| **openSIS** | [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🔴 **`GPL-2.0`** · `17 286` B at `docs/License.txt` | `master` | SIS — 🔴 **this KB stored it as `LGPL?` for ten passes** |
| **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🟡 **`LGPL-3.0`** · `7 652` B | 🔵 **`v3.0.x-develop`** | virtual classroom / web conferencing |
| **H5P** | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **`GPL-3.0`** · `35 146` B | `master` | interactive content runtime embedded by Moodle + Canvas |
| **Richie** | [`openfun/richie`](https://github.com/openfun/richie) | 🟢 **`MIT`** · `1 079` B | `master` | course catalogue/portal front end for Open edX |

### 🟢 The permissive shortlist, which is the only part of this page a studio needs in a hurry

🟢 **`OpenOLAT` *(Apache-2.0)*, `Kolibri` *(MIT)*, `Richie` *(MIT)*, `oppia` *(Apache-2.0)*.**
🟡 `OpenEduCat` *(LGPL-3.0)* and `BigBlueButton` *(LGPL-3.0)* are weak copyleft — linkable
without infecting the caller, which is usually workable. 🔴 **Everything else on the shelf is
`GPL`/`AGPL`/`ECL`, and `4` of the `16` rows are Affero**, where merely *operating* the service
over a network triggers source disclosure to users.

### 🔵 Branch resolution is not a detail

🔴 **`6` of the `16` platforms above have a default branch that is neither `main` nor
`master`** — `release`, `19.0`, `v31.0.00`, `mobile`, `v3.0.x-develop`, `develop`. 🔴 **A sweep
that guesses gets `404` and records "no licence"**, which is a **false absence** on six of the
most important platforms in this industry. 🟢 `git ls-remote --symref HEAD`, `30`/`30`.
🔵 [`evidence/default-branch-resolution.2026-10-14-p198.tsv`](../evidence/default-branch-resolution.2026-10-14-p198.tsv).

## Pass 197 — 2026-10-14

🆕 🟢 **The platform layer of this market has a CUSTOMISATION ECONOMY, it is `198` repositories
deep on one platform alone, and this KB had not sampled it.** 🔵 p196 measured the platforms
themselves and asked the right next question; it asked it with the wrong word *(see
[`repos/trending.md`](../repos/trending.md))*.

### 🟢 Moodle is not one repository — it is a plugin market, and the governance plugin already exists

| plugin | licence *(from bytes or headers)* | what it customises |
|---|---|---|
| 🟢 [`bycs-lp/moodle-local_ai_manager`](https://github.com/bycs-lp/moodle-local_ai_manager) | 🟢 **`GPL` in `255` of `278` source headers** | **providers, quotas and per-tenant AI policy** — the layer a ministry or district buys before it buys a tutor |
| 🟢 [`bycs-lp/moodle-block_ai_chat`](https://github.com/bycs-lp/moodle-block_ai_chat) | 🟢 **`GPL` in `64` of `91`** | the chat surface **on top of** that manager, not beside it |
| 🟢 [`marcusgreen/moodle-qtype_aitext`](https://github.com/marcusgreen/moodle-qtype_aitext) | 🟢 **`GPL` in `40` of `50`** | an **LLM-graded free-text question type** — assessment inside the LMS's own grading pipeline |
| 🟡 [`human2human-ai/moodle-tool_human2human`](https://github.com/human2human-ai/moodle-tool_human2human) | 🟡 `GPL-3.0` *(`35 149` B)* | AI-facilitated **oral exams**, role plays, debates. Created `2026-10-05` |
| 🟡 [`cgrevisse/moodle-qbank_genai`](https://github.com/cgrevisse/moodle-qbank_genai) | 🟡 `GPL-3.0` *(`35 178` B)* | generative question bank |
| 🟢 [`microsoft/moodle-ai-assistant`](https://github.com/microsoft/moodle-ai-assistant) | 🟢 **`MIT`** *(`1 084` B)* | Microsoft's assistant accelerator — 🟢 **the one permissive row in the layer** |
| [`onbirdev/moodle-webservice_mcp`](https://github.com/onbirdev/moodle-webservice_mcp) | *(on shelf)* | **MCP over Moodle's web-service layer** — the agent-facing seam |
| [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) | *(on shelf)* | `223`★ — tutoring, quizzes, mind maps, RAG over course material |
| [`saylordotorg/moodle-local_ai_course_assistant`](https://github.com/saylordotorg/moodle-local_ai_course_assistant) | *(on shelf)* | Saylor's SOLA learning coach |

🔵 **Why this changes the shape of an engagement.** The platform decision in this market is
usually framed as *«which LMS»*. 🟢 **It is at least as much *«which extension points, under
which grant»***: the plugin layer is where an AI deliverable actually lands, it is `GPL-3.0`
almost throughout, and the one `MIT` row in it comes from Microsoft.

### 🆕 🔴 «No licence file» means something different in this layer, and the difference is commercial

🟢 **`3` of the plugins above ship NO licence file anywhere in the complete tree** — and carry an
**operative `GPL` grant in nearly every source file**, because Moodle requires it by project
rule.

| | |
|---|---|
| 🔴 what a root-file probe reports | *«no licence»* |
| 🔴 what a complete-tree probe reports | *«absence enumerated»* — stronger, and still wrong |
| 🟢 what the source headers say | 🟢 **`GRANT_GPL`, in `40`/`50`, `255`/`278`, `64`/`91` files** |

🔴 **So the shelf-wide figure *«`16.2`% of rows have no licence»* OVERSTATES absence in this
layer**, in the direction that makes a usable base look unusable. 🟢 **The obligation is real
either way**: a `GPL` grant in a header is a `GPL` grant, so a derivative plugin is `GPL` and a
client who wanted a proprietary module cannot have one here. 🔵 p139 measured *«`0` of `9`»* for
the same question over **npm** connector packages. **Two layers, two conventions, one figure
that cannot describe both.**

### 🟢 The extension point itself, read at last

🟢 [`openedx/XBlock`](https://github.com/openedx/XBlock) — **`Apache-2.0`**, `11 358` B, at
`LICENSE.TXT`. 🔵 The row that defeated five filename lists in this KB now has its grant read
from bytes by **two independent channels** *(`git cat-file` and `raw.githubusercontent.com`,
same `11 358`)*. 🟢 **And it matters commercially:** `edx-platform` is `AGPL-3.0`, but
**`XBlock` — the component API you build against — is permissive with a patent grant.** An
`XBlock` is therefore the cheapest compliant place to put proprietary logic in the Open edX
world.

### 🆕 🔴 The bundling trap, measured: `Lumi` ships `14` other people's grants and one EULA

p196 counted `15` *«own licence texts»* in
[`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) and registered the row-by-row read.
Run:

| what the `15` are | count |
|---|---|
| 🔴 H5P content-type libraries under `assets/h5p/libraries/…`, copyright **Joubel**, **H5P**, **Oliver Tacke**, **CKSource** | 🔴 **`14`** *(13 `MIT`, 1 `Apache-2.0` font licence)* |
| 🔴 `client/assets/legal/eula.html` — **`259 095` B** | 🔴 **`1`, and an EULA is the opposite of a grant** |
| 🟢 `Lumi`'s own grant | 🟢 **`0`** |

🟢 **p195's claim *«the interoperability layer grants nothing»* SURVIVES, on better evidence**
— `1EdTech`, `adlnet` and `Lumi` all grant nothing of their own.
🔴 **And the deployment consequence is specific:** an H5P-based deliverable redistributes `14`
third-party grants whose holders are not the platform, so the notice file a client needs is
**not** the platform's licence — it is a bill of materials.

🆕 🔴 **Two instrument defects fall out of this row, both recorded and neither patched here.**
`is_bundled` is a **path list** *(`node_modules`, `vendor`, `third_party`…)* and these vendored
texts live under `assets/h5p/libraries/` — 🔵 **what identifies them is the copyright HOLDER,
not the path**, which is `P441`'s lesson biting p196's own instrument. And `is_licence_path`
counts `eula` as a grant. Both pre-registered with falsifiers; `P237` forbids editing the
predicate in the same pass that promoted it to `lib/`.

## Pass 196 — 2026-10-14

🆕 🟢 **A web sweep this pass returned, in its own words, *"sources disagree on several
licenses"* and *"most say AGPLv3, one says Apache 2.0"* about Open edX. This page does not have
to choose: every platform row below carries a licence read from BYTES, and the disagreements
resolve one way.** 🟢 Two of the open web's claims about the biggest platforms in this market
are **wrong**, and both errors run in the permissive direction — the direction that costs a
client.

### 🔴 The open web is wrong about `2` of the `8` biggest platforms, both times optimistically

| platform | the open web says | 🟢 the bytes say | verdict |
|---|---|---|---|
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 split: `AGPLv3` **or** `Apache-2.0` | 🟢 **`AGPL-3.0`** · `35 136` B | 🔴 **the Apache claim is WRONG** |
| 🔴 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 one source: *"Apache 2.0"* | 🟢 **`ECL-2.0`** · `11 120` B | 🔴 **WRONG.** ECL is Apache-*derived*; not the same grant |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `AGPLv3` core | 🟢 **`AGPL-3.0`** · `34 520` B | 🟢 confirmed |
| [`moodle/moodle`](https://github.com/moodle/moodle) | *"GPL"* | 🟢 **`GPL-3.0`** · `35 147` B at **`COPYING.txt`** | 🟢 confirmed — 🔵 **and the file is not named `LICENSE`** |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `Apache-2.0` | 🟢 **`Apache-2.0`** · `10 982` B | 🟢 confirmed — 🟢 **the one permissive university LMS** |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `LGPLv3` | 🟢 **`LGPL-3.0`** · `8 241` B | 🟢 confirmed |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | *"GPL"* | 🟢 **`GPL-3.0`** · `35 121` B | 🟢 confirmed |
| 🟡 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | *"GPL"* | 🟢 **`GPL-2.0`** · `15 214` B | 🟡 **v2, not v3** — a different compatibility story |

🔴 **Both web errors point the same way: they report a copyleft platform as permissive.** A
studio that takes *"Open edX is Apache-2.0"* from a comparison blog and builds a hosted
deliverable has adopted an **Affero network-use disclosure obligation** it does not know it
has. 🟢 This is the concrete value of the byte lane over the consensus lane.

### 🟢 The sweep's own negative result, confirmed by measurement

🔵 The web sweep reported *"none of the results confirmed MIT licensing for any LMS or SIS."*
🟢 **p195's `468`-slug census agrees, and can say it more strongly: of the hosted-LMS layer,
`0` rows are `MIT`.** The `218` `MIT` rows on this shelf are tools, agents and content — not
platforms.

🔴 **`41` of `380` licensed rows are `AGPL-3.0`**, more than every restricted and
source-available category combined, and they include the `openedx` family *(4 slugs)*,
`canvas-lms`, `frappe/lms`, `classroomio`, `learnhouse` and `tutor`. 🔵 **The hosted-LMS layer
is Affero as a market, not as an exception** — and that now rests on two independent channels.

### 🟢 `rosariosis`'s `GPL-2.0` is COMPLETE — the `389`-byte shortfall is an appendix

🔵 This pass's band control flagged it as `UNDER` — the one flag that could have been a real
narrowing of a platform grant. **Read:**

| | SPDX `GPL-2.0` | `rosariosis` |
|---|---|---|
| lines | `117` *(reflowed)* | `276` *(hard-wrapped ~`72` cols)* |
| words | `2 910` | `2 496` |
| ends at | the Ty Coon signature block | 🔵 **`END OF TERMS AND CONDITIONS`** |

🟢 **Operative sections `0`–`12` all present. The `414` missing words are entirely the
non-operative *"How to Apply These Terms to Your New Programs"* appendix. The grant is whole;
`GPL-2.0` stands.** 🆕 🔵 And it reads *"GNU **Library** General Public License"* where SPDX
reads *"**Lesser**"* — the FSF's pre-`1999` wording. **`rosariosis` ships the authentic 1991
text; SPDX ships a modernised one**, so part of the delta is SPDX's edit.

### 🆕 🟢 `odoo/odoo` is IN-BAND, and a one-interval band would have called it narrowed

🔵 `LGPL-3.0` is published in **two legitimate forms**, and this page carries platforms on both:

| platform | bytes | form |
|---|---|---|
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | `7 652` | 🟢 **short** — LGPL preamble, `GPL-3.0` by **reference** |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `8 241` | 🟢 short |
| 🆕 [`odoo/odoo`](https://github.com/odoo/odoo) | **`43 529`** | 🟢 **full** — `GPL-3.0` included by **value** *(SPDX's own text is `42 098` B)* |

🟢 **`odoo/odoo` carries the full LGPL-3.0, not a `35`kB anomaly** — a reading a single
`lo`/`hi` band gets backwards. 🔵 This is why the band became a **SET** of intervals this pass;
see [`compose/code/p196-copyleft-band/`](../compose/code/p196-copyleft-band/).

### 🆕 🟢 Platform-grade additions this pass, byte-verified

🔵 Found through the reopened MCP ranked channel, then read from bytes.

| platform | ★ | 🟢 licence | bytes | what it is, and why a studio would start here |
|---|---|---|---|---|
| 🟢 [`oppia/oppia`](https://github.com/oppia/oppia) | `6 855` | 🟢 **`Apache-2.0`** | `11 358` | **branching lesson engine** with learner-state and *explorations*. 🟢 Patent grant. The permissive answer to *"we need adaptive sequences, not a course shell"* |
| 🟢 [`CTFd/CTFd`](https://github.com/CTFd/CTFd) | `6 876` | 🟢 **`Apache-2.0`** | `11 314` | **assessment platform**: challenges, scoring, teams, hints, submission gating. Built for CTFs, but it is a general graded-challenge engine |
| 🟢 [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | `381` | 🟢 **`MIT`** | `1 083` | **autograding + per-student cloud IDE.** The row that covers CS-course delivery end to end |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `1 145` | 🟢 **`MIT`** | `1 097` | re-confirmed from **both** channels. 🟢 **Still the only permissive, platform-grade, offline-first LMS on this shelf** |

🔴 **And one row that must NOT be taken as a platform:**
[`frappe/education`](https://github.com/frappe/education) `665`★ — a Frappe-based school
management app whose **entire licence file is `19` bytes**: `License: GNU GPL V3`, at lowercase
`license.txt`. 🔴 **A declaration, not a grant.** The ranked channel reports it `NOASSERTION`.
🔵 Compare `frappe/lms`, whose `AGPL-3.0` is a real `33 893`-byte text — **same publisher,
different rigour, and the difference decides a hosted deliverable.**

### 🟢 The platform shelf, by delivery posture

| posture | platforms | what it means for a client engagement |
|---|---|---|
| 🟢 **permissive — closed deliverable OK** | `OpenOLAT` *(Apache-2.0)*, `Kolibri` *(MIT)*, `oppia` *(Apache-2.0)*, `CTFd` *(Apache-2.0)*, `Anubis` *(MIT)*, `Sakai` + `Opencast` *(ECL-2.0)* | 🟢 the short list. **`ECL-2.0`'s patent grant is scoped to education** — read it if the deliverable is cross-sector |
| 🟡 **weak copyleft — linkable** | `BigBlueButton`, `OpenEduCat`, `odoo` *(LGPL-3.0)*, `edrys` *(MPL-2.0)* | 🟡 dynamic linking is fine; **modifications to the library itself flow back** |
| 🔴 **strong copyleft — source on distribution** | `Moodle`, `ILIAS`, `Chamilo`, `Gibbon` *(GPL-3.0)*, `RosarioSIS`, `i-educar` *(GPL-2.0)* | 🔴 distribute the plugin, publish the plugin |
| 🔴 **Affero — network use triggers disclosure** | `Open edX` family, `Canvas`, `frappe/lms`, `classroomio`, `learnhouse`, `tutor` | 🔴 **a hosted SaaS deliverable discloses.** `41` rows — the largest non-permissive class on this shelf |
| 🔴 **source-available, NOT open source** | `canyongbs/advisingapp` *(Elastic)*, `TrenTorch` *(PolyForm Noncommercial)* | 🔴 **cannot base a client deliverable.** `advisingapp` remains the only AI-native higher-ed CRM here, and **no permissive row replaces it** |

### Open limbs

🔴 **`advisingapp`'s gap is still open:** `Elastic`-licensed, so the only AI-native higher-ed
student-success CRM on this shelf is unusable, and p195's search for a permissive replacement
found none. 🔴 **p195's claim that *"the interoperability layer grants nothing"* is now in
doubt** — `Lumieducation/Lumi` carries `15` own licence texts below its root *(see
[`agents/top.md`](../agents/top.md))*, so the layer claim needs re-reading row by row.
🔴 **`26` of the shelf's `494` distinct rows have never been licence-probed at all.**

## Pass 195 — 2026-10-14

🆕 🔴 **A platform row this page has carried as *"UNKNOWN until the body is read"* is now read,
and the answer is that it is not open source at all.** 🟢 Every platform row below also had its
licence re-read from bytes through the raw lane this pass, at census volume rather than row by
row.

### 🆕 🔴 `advisingapp` — the named gap CLOSES, and it closes against the platform

🔵 This page carried: 🔴 *"`advisingapp` is `NOASSERTION` and unread — a `340`★ AI-native
higher-ed platform whose…"*, with `P47` attached. 🟢 **Read this pass:**

| platform | ★ | path | bytes | 🔴 licence | can it base a client deliverable? |
|---|---|---|---|---|---|
| 🔴 [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | `340` | `LICENSE` | **`3 860`** | 🔴 **`Elastic`** | 🔴 **NO — source-available, not OSS** |

🔴 **The Elastic License permits reading and self-hosting, and bars providing the software to
third parties as a managed service.** 🟡 That is precisely what an AI Studios engagement
building a student-success platform **for** a university would do. 🟢 `commercial_use_ok`
denies it on the family name alone — `Elastic` is a named branch of the gate — so no body
parse was needed and no judgement call is involved.

🔵 **Why it matters more than one row: `advisingapp` was the only AI-NATIVE higher-ed CRM on
this page.** 🔴 **The permissive student-success-CRM row does not exist**, and this page should
stop implying one does.

### 🟢 The platform shelf, licence from bytes, `15` of `15`

| platform | layer | 🟢 licence | bytes | delivery gate |
|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | LMS | 🟡 `GPL-3.0` | `35 147` | 🟡 copyleft, **no network clause** |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | LMS | 🟡 `GPL-3.0` | `35 147` | 🟡 copyleft |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | school mgmt | 🟡 `GPL-3.0` | `35 121` | 🟡 copyleft |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | SIS | 🟡 `GPL-2.0` | `15 214` | 🟡 copyleft |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | LMS | 🔴 `AGPL-3.0` | `35 136` | 🔴 network-use disclosure |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | LMS | 🔴 `AGPL-3.0` | `34 520` | 🔴 network-use disclosure |
| [`frappe/lms`](https://github.com/frappe/lms) | LMS | 🔴 `AGPL-3.0` | `33 893` | 🔴 **not `MIT`, per p193** |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | Open edX deploy | 🔴 `AGPL-3.0` | `34 523` | 🔴 the deployer too |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | LMS | 🟢 **`ECL-2.0`** | `11 120` | 🟢 **permissive**, patent grant scoped to education |
| [`opencast/opencast`](https://github.com/opencast/opencast) | lecture capture | 🟢 **`ECL-2.0`** | `11 340` | 🟢 **permissive** |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | LMS | 🟢 **`Apache-2.0`** | `10 982` | 🟢 **permissive** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | offline learning | 🟢 **`MIT`** | `1 097` | 🟢 **permissive** |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | education ERP | 🟡 `LGPL-3.0` | `8 241` | 🟡 linkable |
| 🔴 [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | student-success CRM | 🔴 **`Elastic`** | `3 860` | 🔴 **BARRED as a hosted deliverable** |
| 🔴 [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | SIS | 🟡 **`GPL-2.0`** | `17 286` | 🟡 copyleft — 🔴 **but see below** |

### 🆕 🟡 The ERP/SIS question, and this pass finally has a measured answer shape

🔵 Searched again this pass: `open source platform education ERP SIS student information system
MIT Apache license 2026`. 🔴 **The search returned no permissive education ERP or SIS. It
returned two copyleft ones and a dead end** — which is the same answer p194 recorded, now with
the licences read from bytes rather than taken from the vendors' own pages:

| candidate | vendor page claims | 🟢 bytes say |
|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | *"LGPL v3"* | 🟢 **`LGPL-3.0`, `8 241` B — AGREES** |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | *"GNU General Public License"* | 🟡 **`GPL-2.0`, `17 286` B — AGREES, but NOT at root** |
| Kuali | licence not stated in results | 🔴 **not resolved — recorded as unsearched, not as absent** |

🔴 **`openSIS` is the instructive one: the root ladder returns NOTHING across `19` filenames**,
and the grant is at `docs/License.txt`, one directory down, exactly where its README says.
🟢 **So the honest verdict is `GPL-2.0`, and the honest method note is that a root-only ladder
would have filed this platform as unlicensed.** 🔵 Registered upstream as
[`p969-root-only-licence-reach`](../compose/code/p969-root-only-licence-reach/).

🟢 **Standing conclusion, unchanged and now priced: there is no MIT/Apache education ERP or SIS
on this shelf.** 🟡 **The permissive route into administration is to put an agent layer ON a
copyleft SIS over its API rather than to fork it** — the copyleft reaches the derivative work,
not the client of a network service, for `GPL-2.0` and `GPL-3.0` *(no network clause)*. 🔴 **For
the `AGPL-3.0` rows that reasoning does not hold**, and that is the distinction this page exists
to make.

### 🔴 `Odoo`-shaped question, answered for education: the vertical ERP layer is LGPL, not MIT

🟢 `openeducat_erp` is the education analogue of the Odoo pattern this KB cites elsewhere —
**and it is literally an Odoo module set** *(default branch `19.0`, version-named, tracking
Odoo releases)*. 🟡 **`LGPL-3.0` means a client's own modules can link it without becoming
copyleft, and modifications TO it must be shared.** 🟢 **That is a workable commercial posture
and should be stated as the recommendation rather than as a compromise.**

### 🔴 Platform rows that are source-available, and must never be filed as OSS

| row | licence | bars |
|---|---|---|
| 🔴 [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | **`Elastic`** | 🔴 offering it to third parties as a managed service |
| 🔴 [`willwearing/graspful`](https://github.com/willwearing/graspful) | **`P1054`** — MIT's body + an anti-SaaS non-compete | 🔴 hosted competition *(already on this page)* |
| 🔴 `freesoft/MathCrew` · `minouza/MathCrew` · `lilialla/bandwise` · `shine11224/EchoLingo` | **`PolyForm`** | 🔴 commercial use |
| 🔴 [`GautamVhavle/learner-verse`](https://github.com/GautamVhavle/learner-verse) | **BUSL 1.1** | 🔴 *"any purpose involving direct or indirect commercial activity"* |

🟢 **`7` platform-shaped rows across four source-available families.** 🔴 **None of them is open
source, and all of them look like it in a search result** — `MathCrew` appears twice because
it is a fork pair with byte-identical `PolyForm` licences *(`sha256` `2392d719…`)*.

### 🟢 Unchanged and re-confirmed this pass

🟢 `menthorlabs/menthor` is still **`archived: true`** — a LATAM vertical row frozen upstream,
re-measured through the ranked channel, unchanged from p192 and p193. 🟢 The `ECL-2.0` reading
of `sakai` and `opencast` holds across a third channel. 🔴 **`Aeries SIS + Edgenuity` stays
closed per p192**; no call was spent re-opening it.
## Pass 194 — 2026-10-14

🆕 🟢 **The platform licence matrix p193 built from one channel has been re-read from bytes
through a second, independent channel. `15` of `15` rows agree. Nothing moved.**

🔵 p193 took licences from the recovered search channel's `license.spdx_id`, falling back to a
blobless clone where it returned `NOASSERTION`. 🆕 **p194 re-read every row from
`raw.githubusercontent.com` — a transport with no relationship to either — and then re-classified
every payload with [`compose/code/lib/license_family.sh`](../compose/code/lib/license_family.sh),
this KB's hardened classifier (`207`/`207` assertions today).** 🟢 **A platform shelf that
survives re-measurement through an unrelated transport AND an independent classifier is one an
engagement can quote.**

🆕 🟡 **Provenance note, because this page needed it most.** Until this pass **this file named no
channel at all** — `0` mentions of the lane its every verdict depends on, while
[`agents/trending.md`](../agents/trending.md) carries `150`. 🟢 Every row below now carries its
byte count, and the channel is named here: **`raw.githubusercontent.com/<slug>/HEAD/<file>`,
classified by `lib/license_family.sh`.**

### 🟢 `15` platform rows, licence re-verified from bytes — `5` / `5` / `5` CONFIRMED

| 🟢 PERMISSIVE — build on, deliver, keep your changes | 🔴 AFFERO — network use triggers disclosure | 🟡 OTHER COPYLEFT |
|---|---|---|
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) `ECL-2.0` · `11 120` B | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) `AGPL-3.0` · `35 136` B | [`moodle/moodle`](https://github.com/moodle/moodle) `GPL-3.0` · `35 147` B *(`COPYING.txt`)* |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) `MIT` · `1 097` B | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) `AGPL-3.0` · `34 520` B | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) `GPL-3.0` · `35 147` B |
| [`opencast/opencast`](https://github.com/opencast/opencast) `ECL-2.0` · `11 340` B | 🔴 [`frappe/lms`](https://github.com/frappe/lms) **`AGPL-3.0`** · `33 893` B | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) `LGPL-3.0` · `8 241` B |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) `Apache-2.0` · `10 982` B | [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) `AGPL-3.0` · `34 523` B | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) `GPL-2.0` · `15 214` B |
| 🔴 [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor) `Apache-2.0` · `11 337` B — **ARCHIVED** | [`classroomio/classroomio`](https://github.com/classroomio/classroomio) `AGPL-3.0` · `34 523` B | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) `GPL-3.0` · `35 121` B |

🟢 **Every cell carries its byte count this pass**, so any later pass can tell a re-read from a
restatement. 🔵 `frappe/lms` at `33 893` B is the row p193 corrected from a roundup's `MIT`;
🟢 **the second channel returns the same `33 893` B of Affero.** The correction holds.

### 🔴 A near-miss worth recording: the three GPL rows were almost published as Affero

🔴 This pass's first, ad-hoc classifier returned **`AGPL-3.0` for `moodle`, `chamilo` and
`GibbonEdu`**, because GPLv3's §`13` names the Affero licence. 🔴 **This KB registered that defect
as `P171` and tooled against it in `lib/license_family.sh`; p194 re-derived it because it wrote a
new classifier instead of sourcing the hardened one.** 🟢 **The library gets all three right**
— `GPL-3.0`, `GPL-3.0`, `GPL-3.0` — and the full account is in
[`repos/foundations.md`](../repos/foundations.md) this pass.

🔵 **Why this mattered more here than anywhere else in the KB.** Moodle is the single most
likely LMS under a client's existing deployment.

| if this KB had published | the advice that follows | 🔴 cost |
|---|---|---|
| 🔴 Moodle is `AGPL-3.0` | *"your hosted Moodle obliges you to disclose your modifications to every user over the network"* | 🔴 **a client is told to open-source plugin work it has no obligation to disclose** |
| 🟢 Moodle is `GPL-3.0` | 🟢 distribute the modified code **if you distribute the software**; hosting it as a service does **not** trigger §`13` by itself | 🟢 correct |

🟡 **p193's error direction was understating obligation; this one would have overstated it.**
🟢 Both are delivery-routing errors, and the matrix above is now the only form this KB
publishes: **licence, byte count, and the channel it was read from.**

### 🆕 🔴 The platform shelf did not trend, and that is a finding about the shelf

🔵 Six trending lanes were measured this pass *(see [`agents/trending.md`](../agents/trending.md))*.
🔴 **Not one of these `15` platforms appeared in any of them.** `openedx/openedx-platform`
moved `+3` stars in `4` days at p192.

🟢 **Read correctly, that is reassurance, not decay.** 🔵 An LMS with a national installed base
is not supposed to gain `4 000` stars a week; **a platform that suddenly trends is usually a
platform being rewritten.** 🟡 **The actionable form: pick platforms from this matrix and pick
curriculum from the trending lane — they are different markets moving at different speeds, and
this KB should stop expecting one shelf to serve both.**

### 🆕 🟡 The ERP/SIS question, searched again and still answered the same way

🔵 Searched this pass: `open source platform education ERP SIS MIT Apache 2026`.
🔴 **No education ERP or SIS under `MIT`, `Apache-2.0` or `BSD` was found.**

| candidate | licence | verdict |
|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 `LGPL-3.0` *(`8 241` B, bytes)* | 🟡 the real ERP/SIS answer — **weak copyleft, usable, conditions attach** |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🟡 `GPL-2.0` *(`15 214` B, bytes)* | 🟡 SIS, copyleft |
| ERPNext / Frappe *(education module)* | 🔴 publisher page states no licence | 🔴 **and its sibling [`frappe/lms`](https://github.com/frappe/lms) is `AGPL-3.0` — treat the family as Affero until read from bytes** |
| Forma LMS | 🔴 a secondary comparison calls it *"the most permissive licence in this comparison"* | 🔴 **NOT VERIFIED — no bytes read, no slug resolved. Recorded as a lead, not a row** |

🟢 **Stated as an informed gap with the search named:** the permissive end of this market is
LMS and lecture-capture *(`sakai`, `kolibri`, `opencast`, `OpenOLAT`)*, **not administration.**
🔴 **An engagement that needs permissive student-records software will be building it, not
adopting it** — and that is a scoping fact worth more than a filler row.

## Pass 193 — 2026-10-14

🆕 🔴 **The platform shelf has a licence matrix for the first time, every cell measured today,
and it says the opposite of what this KB told an APAC engagement one pass ago.**

### 🟢 `15` platform rows, licence read this pass — `5` / `5` / `5`

🔵 Licence taken from the recovered channel's `license.spdx_id` where it resolves, and from
the **bytes** where it returns `NOASSERTION`. 🔴 Not from a README, not from a badge.

| 🟢 PERMISSIVE — build on, deliver, keep your changes | 🔴 AFFERO — network use triggers disclosure | 🟡 OTHER COPYLEFT |
|---|---|---|
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) `ECL-2.0` · `1 238`★ | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) `AGPL-3.0` · `8 198`★ | [`moodle/moodle`](https://github.com/moodle/moodle) `GPL-3.0` · `7 476`★ |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) `MIT` · `1 145`★ | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) `AGPL-3.0` · `6 869`★ | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) `GPL-3.0` · `1 012`★ |
| [`opencast/opencast`](https://github.com/opencast/opencast) `ECL-2.0` · `508`★ | 🔴 [`frappe/lms`](https://github.com/frappe/lms) **`AGPL-3.0`** · `3 311`★ | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) `LGPL-3.0` · `888`★ |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) `Apache-2.0` · `447`★ | [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) `AGPL-3.0` · `2 372`★ | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) `GPL-2.0` · `646`★ |
| 🔴 [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor) `Apache-2.0` · `582`★ — **ARCHIVED** | [`classroomio/classroomio`](https://github.com/classroomio/classroomio) `AGPL-3.0` · `1 717`★ | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) `GPL-3.0` · `637`★ |

🔵 **Five, five and five** — and the only permissive row with LATAM reach is archived.

### 🆕 🔴 CORRECTION — the APAC sentence this KB published yesterday is false

🔵 [`intel/market.md`](../intel/market.md), p192, APAC:
*"Two of this shelf's platform rows are APAC-origin — `frappe/lms` (`3 311`★, **`MIT`**…) and
`openeducat/openeducat_erp` (`888`★…) — **so an APAC engagement can start on APAC-built,
permissively-licensed code**, which is the one region where that is true."*

| the claim | 🔴 measured |
|---|---|
| `frappe/lms` is `MIT` | 🔴 **`AGPL-3.0`** — `license.txt`, `33 893` B, read from bytes this pass |
| `openeducat_erp` is permissive by implication | 🔴 **`LGPL-3.0`** — this KB's own earlier byte read |
| APAC is *"the one region"* where you can start on permissive code | 🔴 **INVERTED. Both APAC-origin platform rows are copyleft; one is Affero.** The permissive rows are Apereo *(NA)*, Learning Equality *(NA)*, Opencast *(EMEA consortium)* and OpenOLAT *(Switzerland, EMEA)* |

🔴 **This is the costliest kind of error this KB can make**, because it is not a wrong star
count — **it routes a delivery.** A hosted LMS built on `frappe/lms` and modified for a client
is an **Affero** deployment: serving it over a network obliges source disclosure of the
modifications. 🟢 Under `MIT` the same engagement has no such obligation. 🔵 **The word
changed; the contract changed with it.**

🟢 **Corrected in three places this pass** — here, in [`agents/top.md`](../agents/top.md)'s
ranked table, and in `intel/market.md`'s APAC opportunity paragraph.

### 🟡 What an APAC engagement should actually start from

🔵 **The honest replacement for the retracted sentence:**
🟢 **`OpenOLAT` *(`Apache-2.0`)* and `Sakai` *(`ECL-2.0`)* are the fork-safe platforms, and
neither is APAC-origin.** 🟡 `frappe/lms` and `openeducat_erp` remain the best APAC-built
platforms and remain **usable** — copyleft is not a prohibition — 🔴 **but they are a
disclosure decision made at architecture time, not a licence footnote discovered at
delivery.** 🔵 The clean pattern is agent-side: keep the client's proprietary work in a
separate service that talks to the platform, rather than inside the Affero tree.

### 🆕 🔴 An APAC vertical row exists, and it is unusable

🔵 [`jude-miller-dev/Milky-institute-online`](https://github.com/jude-miller-dev/Milky-institute-online)
— `367`★, created `2026-01-30`, **`786` paths**, Java/Spring Cloud, bilingual
Chinese/English description. 🟢 **A production-shaped adult-education platform split into
`tj-course`, `tj-exam`, `tj-auth`, `tj-data`, `tj-gateway` services — with a
course-recommendation AI agent as a first-class service, not a bolt-on.** 🔵 Structurally it
is the closest thing on GitHub to *"what an APAC institutional LMS with agents inside it
looks like"*.

🔴 **Root tree read: no `LICENSE`, no `COPYING`, nothing.** All rights reserved.
🟡 **Listed here as evidence of the architecture, explicitly NOT as a starting point.** 🟢 It
is the reference design an APAC proposal can point at while building on `OpenOLAT` or on the
client's existing Moodle estate.

### 🟢 Unchanged and re-confirmed this pass

🔵 `menthorlabs/menthor` **`archived: true`**, `582`★ — re-read today, still frozen, still the
only LATAM-reaching permissive platform row, still not recommendable.
🔵 `openeducat_erp` default branch `19.0`, `rosariosis` default branch `mobile`,
`GibbonEdu/core` default branch `v31.0.00`, `frappe/lms` default branch `develop`,
`learnhouse` default branch `dev`, `kolibri` default branch `develop`, `opencast` default
branch `develop` — 🔴 **`7` of `15` platform rows do not default to `main` or `master`.**
🟡 p192 counted `5` of `12`; the ratio holds as the population grows. 🟢 Any clone script in a
delivery pipeline that assumes `main` fails on nearly half this shelf.
## Pass 192 — 2026-10-14

🆕 🟢 **Three cells on this page change status this pass, and two of them change because a
question this page asked ITSELF has been answered.**

### 🟢 `Aeries SIS + Edgenuity` — the open question CLOSES, and the cell loses its product

🔵 **This page published:** *"the raw lane returned `404` for `15` candidate paths across
`HEAD`/`main`/`master`, so **this pass verified that the repository exists and did not verify
that it contains anything.**"*

🟢 **Measured now, one call:**
[`openfresno/edgenuity-aeries-grade-passback`](https://github.com/openfresno/edgenuity-aeries-grade-passback)
resolves anonymously, exits `0`, writes nothing to stderr, and returns **`0` refs.**
🔴 **The repository is EMPTY — there are no commits.** Not blocked, not a raw-lane artefact.
🔵 `15` × `404` was a correct measurement read against the wrong hypothesis: a path probe
cannot tell *"this path is missing"* from *"every path is missing"*.

🟢 **The cell stays, with its claim corrected rather than deleted.** What it documents is now
unambiguous: **a US school district published the NAME of an Aeries↔Edgenuity passback job and
no code.** 🔵 That is still the most honest K-12 integration signal on this page for
**North America** — the need, in public, from the buyer's side — but it is a need, not a
starting point, and nobody should plan a sprint around cloning it.

### 🔴 `menthor` — a LATAM vertical row that is FROZEN upstream

🔴 [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor), `582`★, `Vue`,
*"Plataforma gratuita e open-source de ensino de programação"* — **`archived: true`.**
🔵 **`updated_at` still reads `2026-10-12`, which is precisely why `updated_at` is not a
liveness signal**: metadata moves on a read-only repository, and `git ls-remote` answers an
archived repo exactly as it answers a live one.

🟢 **Consequence for a LATAM engagement, stated concretely:** a Portuguese-language
programming-education platform at `582`★ is a legitimate fork base and **not** a partner —
no upstream will merge anything, so the fork is the product and its maintenance is the
client's from day one. 🔵 Price it as a one-time asset acquisition, never as a community.

### 🔴 `enkidevs/curriculum` — `833`★ of curriculum nobody can sell

🆕 **New to this KB, and it belongs on THIS page rather than the agents shelf**, because
curriculum is a vertical asset: `5 345` paths of structured lessons across `20`+ tracks.
🔴 **`LICENSE.md` is `189` B and the entire file is one sentence: `CC-BY-NC-SA-4.0`.**

🔵 **This KB has carried *"avoid the `CC-BY-NC-SA` curriculum trap"* as a LATAM warning since
p191.** 🆕 **The trap is not regional.** `NonCommercial` bars client delivery in every region,
`ShareAlike` reaches derivative curriculum, and at `833`★ in English this is the instance most
likely to be proposed by someone who checked that the repo was popular and active and never
opened `LICENSE.md`. 🟢 **Tabled as a priced negative.**

### 🟢 The vertical shelf, now with reach attached

🔵 **First time this page can rank its platforms** — the search channel returns
`stargazers_count` and `default_branch` again. 🟡 **Two of the four columns below are measured
today and one is not**: the region column is carried from this KB's existing placements and
was not re-verified this pass, so it is labelled rather than re-asserted *(see [`agents/top.md`](../agents/top.md) for the full `30`-row
table)*. The vertical-relevant rows:

| platform | ★ *(measured today)* | 🟡 region of origin *(carried from this KB's prior placements — NOT measured this pass)* | default branch *(measured today)* — 🔵 *a deployment detail that bites* |
|---|---|---|---|
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | `8 198` | North America | `master` 🔴 **and the slug is the RENAMED one** — `openedx/edx-platform` still clones, so CI never breaks and docs silently drift |
| [`moodle/moodle`](https://github.com/moodle/moodle) | `7 476` | EMEA *(Australia-founded, EMEA-dominant install base)* | `main`, and the tree is `public/`-prefixed since `5.3` |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `6 869` | North America | `master` |
| [`frappe/lms`](https://github.com/frappe/lms) | `3 311` | APAC *(India)* | 🔴 **`develop`** — not `main`; a `git clone` lands on unreleased code |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | `1 717` | EMEA *(Nigeria/UK)* | `main` |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `1 237` | North America | `master`, `ECL-2.0` |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `1 145` | Global *(offline-first, LATAM + Africa deployments)* | 🔴 **`develop`**, and `544` open issues |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `1 012` | EMEA *(Belgium/Spain)* + LATAM install base | `master` — ships the native MCP server |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `888` | APAC *(India)* | 🔴 **`19.0`** — version-named default branch, the Odoo convention |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `646` | EMEA *(France)* | 🔴 **`mobile`** — the default branch is not `main`, `master` or `develop` |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `637` | APAC *(Hong Kong)* | 🔴 **`v31.0.00`** |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `447` | EMEA *(Switzerland)* | `master` |

🆕 🔴 **Five of twelve vertical platforms do NOT default to `main` or `master`** —
`develop`, `develop`, `19.0`, `mobile`, `v31.0.00`. 🟢 **That is a concrete, repeatable
engagement defect**: every runbook, Dockerfile and CI config that hardcodes
`git clone -b main` fails on `42`% of this shelf, and it fails *after* the estimate is
signed. 🔵 **`default_branch` is a field the recovered channel returns.** Read it before
writing the runbook — it costs one call and this KB could not make it until today.
## Pass 191 — 2026-10-14

🆕 🔴 **The Chamilo cell changes category, not just content: it is no longer an LMS that an
agent can be bolted onto — it ships the agent layer.** `config/packages/mcp.yaml` declares
`app: 'Chamilo'`, `version: '2.1.0'`, `/mcp` over HTTP and stdio, and the tree carries
**`68` `#[McpTool]` definitions, `47` of them writes**, at HEAD `6f9bb2c61985` *(`2026-10-13`)*.

| platform | grant, at full tree depth | 🆕 agent layer, measured from definitions | what an engagement must supply |
|---|---|---|---|
| 🟢 **[`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms)** | 🟢 **`GPL-3.0+`** — `LICENSE` + `license.txt` at root; `13 271` paths; two vendored subtrees name other families and are **not** the project's grant | 🆕 **native MCP `2.1.0`**: `68` tools *(`21` read / `47` write)*, `48` enforcement sites in `18` of `67` sources, roles `ROLE_ADMIN` / `ROLE_GLOBAL_ADMIN` / `ROLE_QUESTION_MANAGER` / `ROLE_TEACHER`, OAuth 2.1 + JWT + hashed personal keys, **fails closed** on malformed role config | 🔴 **a scoped-key gateway, an audit row and a confirm step for the `47` writes.** The platform supplies the capability and `0` of the accountability |
| 🟢 **[`moodle/moodle`](https://github.com/moodle/moodle)** | 🟢 **`GPL-3.0`** — `COPYING.txt`, `35 147` B, canonical *(the standing path list reaches `COPYING`, not `COPYING.txt`: enumerated, not guessed)* | `5.3` shipped `2026-10-05`; HEAD `2026-10-13`. 🔴 **No native MCP server in-tree** — the layer is third-party *(`csmediapro/moodle-mcp-server`, `AGPL-3.0?`, read-only)* | 🔴 **`67 592` paths and the tree is now `public/`-prefixed** — every rooted path this KB publishes for Moodle is suspect until re-read *(`ACTION NU`)* |
| 🟢 **[`sakaiproject/sakai`](https://github.com/sakaiproject/sakai)** | 🟢 **`ECL-2.0`** — `LICENSE`, `11 120` B, plus three module subtrees; **confirmed at full depth** | HEAD `31590f191769`, **`2026-10-14`** | 🟡 `ECL-2.0` is an Apache-2.0 derivative with a modified patent grant: permissive, and **not** spellable as `Apache-2.0` in a client licence register |
| 🟢 **[`opencast/opencast`](https://github.com/opencast/opencast)** | 🟢 **`ECL-2.0`** — `LICENSE`, `11 340` B | HEAD `637882d48eb8`, `2026-10-13` | 🟢 lecture capture with in-tree local transcription; the `ECL-2.0` verdict holds |

🔵 **Both `ECL-2.0` rows are worth re-stating because p191's own instrument accused them of
contradicting themselves** — the id this shelf meets most often in US higher education is the
one the extractor could not spell. 🟢 **The platforms were right; the tool was wrong.** See
[`repos/foundations.md`](../repos/foundations.md).

### 🔴 The question a buyer asks about an LMS has changed, and the shelf should answer it in this order

1. 🟢 **Does the platform ship an agent layer?** Chamilo yes *(`68` tools)*; Moodle no;
   Open edX only via a third-party facade *(`openedx-mcp`, `33` tools)*.
2. 🔴 **Can a key be narrowed below the human?** Open edX's facade yes *(`9` scopes)*;
   Chamilo **no** — one role boolean for all `68` tools, so the key IS the user.
3. 🔴 **Is there a record of what the agent did?** 🔴 **Neither platform.** Chamilo has `0`
   audit and `0` logger references across its MCP sources; Open edX writes an audit row and
   **never guards its delete path**.
4. 🟡 **Is the grant usable for the deliverable?** Chamilo and Moodle `GPL`-family *(copyleft:
   deploy and extend, do not embed)*; Sakai and Opencast `ECL-2.0` *(permissive)*.

🟢 **Measurement:** [`P1060`](../compose/code/p191-chamilo-agent-surface/README.md) ·
[`evidence/agent-layer-two-platforms.2026-10-14-p191.tsv`](../evidence/agent-layer-two-platforms.2026-10-14-p191.tsv)
· [`evidence/git-recency-recovered.2026-10-14-p191.tsv`](../evidence/git-recency-recovered.2026-10-14-p191.tsv)

## Pass 190 — 2026-10-14

🆕 🔴 **The Open edX cell changes a THIRD time in three passes — from a policy, to a
repository, to a MEASURED AUTHORISATION MODEL — and the direction reverses. p189 recorded
the agent layer as ungoverned. It is not: it carries nine enforced scopes, a payload-bound
confirm handshake and an append-only audit intent. 🔴 What it does NOT protect is WHO acted.**

### 🔴 The platform table gains the column that actually decides an engagement

p189 added *"who can delete a learner record, and whether anything stops them"*. p190 splits
that column, because the two halves have **opposite** answers on the same artefact:

| platform | agent surface | can an agent delete a learner record? | 🆕 is the ACTOR protected? |
|---|---|---|---|
| 🔴 [**Open edX**](https://github.com/openedx/edx-platform) *(`AGPL-3.0`)* via [`blend-ed/tutor-contrib-openedxmcp`](https://github.com/blend-ed/tutor-contrib-openedxmcp) + [`openedx-mcp`](https://pypi.org/project/openedx-mcp/) `0.1.5` | 🟢 **yes — `33` tools, `19` writes** | 🟡 **yes, but rail'd**: `request_retirement` needs `write:users` **+** `destructive` **+** a single-use confirm token, is rate-limited `5`/`600`s, and audits before it writes. 🔴 **BUT `reset_student_attempts` deletes a learner's submitted block state with `write:users` ALONE — no `destructive`, no exception** | 🔴 **NO.** `MCPAuditLogAdmin` blocks **add** and **change** and makes every field readonly — and **never overrides `has_delete_permission`**, which Django defaults to `user.has_perm("delete_mcpauditlog")`. It declares no `actions`, so it keeps the default **"Delete selected objects"** bulk action |
| 🟡 [**Moodle**](https://github.com/moodle/moodle) *(`GPL-3.0` — 🆕 grant read from `COPYING.txt`, `35 147` B this pass)* | yes, three community MCP servers | *(carried)* | not measured |
| 🟢 [**openfun/ralph**](https://github.com/openfun/ralph) *(`MIT` — 🆕 grant read from `LICENSE.md`, `1 094` B this pass)* | LRS / xAPI | 🟢 **no — `409 CONFLICT` on both write paths**, returning before the backend write *(p189)* | 🔴 **NO.** `statements_are_equivalent` compares a **subset**, and `authority` — the field naming who asserted the statement — is **excluded by name** in the code's own comment |

### 🔴 The cross-platform finding, and it is the reason to read this page

🔵 **Two unrelated codebases. Two languages. Two layers of the stack. The same omission.**

- `ralph` protects the **record** in code *(`409`, both write paths, documented in a source
  comment)* and leaves **attribution** outside the comparison.
- `openedx-mcp` protects the **record** in its admin *(add blocked, change blocked, all
  fields readonly)* and leaves **attribution** deletable — 🔴 **by two independent paths**:
  the audit log's own delete permission, **and** `MCPAuditLog.key` / `.user` being
  `on_delete=models.SET_NULL`, so **deleting a key or a user NULLs the attribution on every
  audit row it produced.** The rows survive. The actor does not. 🔵 **The second path needs no
  delete permission on the log at all.**

🟢 **p189 named the trend as *"nobody protects the durable record of a human decision about a
learner"*. p190 corrects it, and the correction is more useful: the RECORD is protected in
both. The ACTOR is not.** That is the sentence to open a governance conversation with, and
it is now measured in code on two platforms rather than asserted.

### 🔴 A third finding on the same artefact, and a DPO will ask it first

🔴 **The PII that `request_retirement` exists to remove is retained by `request_retirement`'s
own audit row.** `_rails.redact()` redacts `{confirm_token, password, key, secret, token}`
and does **not** redact `username` or `email`. The tool's payload is
`{"username": …, "full": …}`, so the audit log permanently stores the username of a learner
whose account was retired **precisely to remove their PII**. 🔴 A search of
`native/retirement.py` and `settings/` for `retention|purge|anonymi|MCPAuditLog` returns
**nothing**: no hook ties the two together.

🔵 **This is not a reason to avoid the platform — it is a scoped, cheap deliverable.** The fix
is a retention rule on one table plus a redaction entry, and it is the kind of finding that
justifies an audit before a client discovers it in a DSAR.

### 🟢 The permissive route to an Open edX agent surface still does not exist

🔴 `tutor-contrib-openedxmcp` is **`AGPL-3.0`** *(`LICENSE` `34 524` B)* and **`1`★**, and its
facade `openedx-mcp` declares **no repository address at all** — no `project_urls`, no
`home_page` on PyPI. 🔵 **The artefact in which every authorisation decision is made is
auditable only as a package payload.** Bus factor `1`.

🟢 **The licence is inherited from the host, not caused by it** — Moodle is `GPL-3` and
carries three servers. 🟢 And the permissive entry point into Open edX is unchanged and now
sound: [`openedx/XBlock`](https://github.com/openedx/XBlock), **`Apache-2.0`**, whose
`NO_LICENCE_FILE` verdict p189 refuted *(`LICENSE.TXT`, `11 358` B)* — a correction that
`ACTION NG` confirms was isolated across all `160` published licence rows this pass.

### 🟢 Exam-integrity platforms, re-scoped by `ACTION NH`

| platform | biometric processing | Art. `5(1)(f)` *(prohibited, LIVE since `2025-02-02`)* | Annex III point `3` *(duty, `2027-12-02`)* |
|---|---|---|---|
| 🟢 [`VIJAYAPANDIANT/online-examination-system`](https://github.com/VIJAYAPANDIANT/online-examination-system) *(`MIT`)* | 🟢 **NONE** — no camera API outside vendored trees | 🟢 **not in scope** | 🟡 behaviour monitoring, non-biometric |
| 🟡 [`singhrajvardhan/SecureExam-Platform`](https://github.com/singhrajvardhan/SecureExam-Platform) *(`MIT`)* | camera; `face_detected` as a **boolean** | 🟢 clear — no affect inference | 🔴 yes |
| 🟡 [`shaheeranser/exam-proctor`](https://github.com/shaheeranser/exam-proctor) | MediaPipe landmarker + `face-api` **identity** check | 🟢 clear — 🔴 **only because `outputFaceBlendshapes` defaults to `false`** | 🔴 yes, **plus GDPR Art. `9`** |
| 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) *(`MIT`)* | 🟢 none — session-level anomaly detection | 🟢 clear *(carried token census)* | 🟡 non-biometric |

🔵 **For an EU engagement the ranking inverts the usual one:** the platform with **no AI and
no camera** is the lowest-risk and was published on this KB's own pages as *"full exam
platform with AI proctoring"* — a description
[`agents/top.md`](../agents/top.md) corrects this pass. 🔴 And the cleanest biometric row is
clear by **one unset flag**: `outputFaceBlendshapes: true` is a single line that moves it
from a `2027` duty into a **live prohibition at EUR `35`M or `7`% of worldwide turnover**.

**Full measurement:**
[`evidence/openedx-mcp-tool-surface.2026-10-14-p190.tsv`](../evidence/openedx-mcp-tool-surface.2026-10-14-p190.tsv)
· [`evidence/ralph-equivalence-subset.2026-10-14-p190.tsv`](../evidence/ralph-equivalence-subset.2026-10-14-p190.tsv)
· [`evidence/proctoring-affect-inference.2026-10-14-p190.tsv`](../evidence/proctoring-affect-inference.2026-10-14-p190.tsv)

## Pass 189 — 2026-10-14

🆕 🟢 **The Open edX cell changes AGAIN — from a policy into a repository — and the
platform table gains a column it has been missing: who can delete a learner record, and
whether anything stops them.**

### 🆕 🔴 AMENDED — the Open edX agent cell. p188 published a POLICY; there is a SERVER

p188 recorded Open edX's agent surface as an absence with an official cause: the official
MCP client's documentation states it *"will never expose MCP server functionality"*. 🟢 That
statement is still true **of the official client**. 🔴 **A community server exists anyway.**

| platform | agent surface | licence | verdict for an engagement |
|---|---|---|---|
| 🔴 **Open edX** *(`AGPL-3`)* | 🆕 [`blend-ed/tutor-contrib-openedxmcp`](https://github.com/blend-ed/tutor-contrib-openedxmcp) `v0.2.0` — Tutor plugin + `openedx-mcp` Django facade *(`/api/mcp/`, `/api/mcp/cms/`)* + MCP streamable-http container behind Caddy at `mcp.<LMS_HOST>` | 🔴 **`AGPL-3.0`** *(`34 524` B, `200`)* | 🟡 **Deployable in `4`–`6` weeks instead of `8`–`10`. 🔴 But `1`★ and `AGPL`, so a studio that EXTENDS it is extending copyleft.** 🔵 The PERMISSIVE route to an Open edX agent surface still does not exist |
| 🟢 **Moodle** *(`GPL-3`, `v5.x`)* | 🟢 **three independent servers** *(unchanged: `G36maid/moodle-mcp`, `CloudDown/polymtl-moodle-connect`, `onbirdev/moodle-webservice_mcp`)* | mixed, `MIT` available | 🟢 still the best-served host, and p188's point stands: 🔴 **`AGPL` is not what prevents a server** — Moodle is `GPL-3` and carries three |

### 🆕 🔴 A new column for this table: who can destroy the record, and what refuses them

🔵 Three jurisdictions now require a durable record of a human decision about a learner
*(Trend `1`)*. This pass measured, in code, what two platform-layer artefacts actually do
when asked to overwrite one — and the answers are opposite.

| layer | artefact | asked to overwrite an existing record | measured |
|---|---|---|---|
| 🟢 **LRS / xAPI** | [`openfun/ralph`](https://github.com/openfun/ralph) HTTP API | 🟢 **REFUSES** | `409 CONFLICT` on both write paths. `PUT` *(lines `624`–`700`)* and `POST` *(via `_filter_existing_statements`)* compare deeply and **return before `BACKEND_CLIENT.write` is reached**. Source comment, verbatim: *"In the case that the current statement is not equivalent to one found in the database we return a 409, otherwise the usual 204."* 🟢 Append-only **by construction** |
| 🔴 **LRS storage** | same, backends | 🔴 **ALLOWS** | `BaseOperationType` declares `DELETE` and `UPDATE`; default is `INDEX`, which overwrites at a specific id; `--es-op-type` exposes all four on the CLI *(p188)* |
| 🔴 **LMS / agent** | `tutor-contrib-openedxmcp` | 🔴 **NOTHING REFUSES** | the LMS tool list includes **`retire`**, authorised only by `is_staff`/`is_superuser` and reachable by any agent holding one MCP key. 🔴 `/health` is unauthenticated |

🔵 **So the guarantee is real and it is in the wrong place.** An xAPI **client** cannot
tamper with a stored statement; an **operator** with Elasticsearch or Mongo credentials
can; and an **agent** on the LMS side can retire the learner outright. 🟢 **That is the
distinction to put in front of a client's DPO, and it is cheap to demonstrate: one `409`,
live.** Pattern `32`'s WORM store is not there to stop the application — it is there to stop
the operator.

### 🟢 Corrections to this table's own rows

| row | correction |
|---|---|
| 🟢 [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Clean `Apache-2.0`.** `LICENSE.TXT`, `11 358` B, HTTP `200`. The `NO_LICENCE_FILE` verdict this KB published was a path-**case** artefact. 🔵 The permissive customisation layer onto `AGPL` Open edX carries no licence caveat |
| 🟢 [`valentineus/moodle-webhooks`](https://github.com/valentineus/moodle-webhooks) | 🟢 **`GPL-3.0`**, not bare `GPL` *(`35 200` B, version line read)*. 🔵 Matters because Moodle core is `GPL-3`-or-later, so the plugin is version-compatible with its host |
| 🔴 [`shuyunyuan/talentcoach`](https://github.com/shuyunyuan/talentcoach) | 🔴 **VIEW-ONLY, remove from any customisation shortlist.** *"Viewing the source on GitHub is permitted; no other rights are granted"* — it negates `MIT`'s verb list item by item while carrying `MIT`'s warranty paragraph verbatim |

🟢 **Unchanged and still the recommendation set for a customisable host:** Moodle *(`GPL-3`,
three agent servers)*, [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) *(`Apache-2.0`,
`10 982` B — a whole university LMS, permissively licensed)*,
[`tsugi`](https://github.com/tsugiproject/tsugi) *(`Apache-2.0`, the LTI framework by the
LTI spec's own author)*, [`Numbas`](https://github.com/numbas/Numbas) *(`Apache-2.0`,
assessment)*, [`academico`](https://github.com/academico-sis/academico) *(`MIT`, `404`★,
LATAM-built SIS)*, [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms),
[`OpenEduCat`](https://github.com/openeducat/openeducat_erp), Open edX *(`AGPL-3`)*.

Evidence: [`openedx-mcp-server`](evidence/openedx-mcp-server.2026-10-14-p189.tsv) ·
[`ralph-append-only`](evidence/ralph-append-only.2026-10-14-p189.tsv) ·
[`licence-path-case`](evidence/licence-path-case.2026-10-14-p189.tsv)

## Pass 188 — 2026-10-14

🆕 🟢 **Two corrections to this table's own rows, one new LAYER, and the Open edX cell
changes from an absence into a POLICY — which is a different thing to price.**

### 🔴 AMENDED — the Open edX cell. "None found" was true and incomplete

🔵 p187 wrote 🔴 *"Open edX (`AGPL-3`) — NO `MCP` server found on any page read this pass"*
and priced the client as an adapter build. 🟢 **`ACTION MV` read `topics/open-edx` at both
sort orders and the Open edX org itself. The absence holds. The CELL was wrong.**

| platform | the agent surface, as measured this pass | licence | what it means for a build |
|---|---|---|---|
| 🔴 🟢 **Open edX** *(`AGPL-3`)* | 🟢 **an OFFICIAL `MCP` CLIENT exists**: [`openedx/openedx-ai-extensions`](https://github.com/openedx/openedx-ai-extensions). 🔴 **And its docs refuse the server role as policy:** *"acts as an MCP CLIENT only"*, *"does not run or host MCP servers"*, **_"will never expose MCP server functionality"_**. The only server in its tree is a `roll_dice` demo behind `ngrok`, marked not for production | 🔴 **`AGPL-3.0`** *(`34 523` B)*, and 🔴 **"experimental" / "proof-of-concept" by its own README** | 🟢 **do NOT build the orchestration half — it exists and it is official.** 🔴 **Do build the server half, and assume you own it permanently** |
| 🔴 **Chamilo, OpenOLAT, Sakai** | 🔴 still **none found** | — | adapter build |

🔴 **And `Gap 427`'s stated cause is REFUTED by this table's own Moodle row: Moodle is
`GPL-3.0`, strong copyleft, and carries THREE independent `MCP` servers.** 🔵 **Copyleft
does not explain the gap.** 🟢 What distinguishes Open edX is that extension is routed
through its own plugin framework and that framework has put the server side out of scope
in writing. 🔵 **A licence can be dual-licensed; a documented design decision cannot be
waited out.** Price accordingly and say why.

### 🔴 AMENDED — `ralph`'s LRS cell carries a caveat it did not have

🔵 p187 added the LRS layer and called `ralph` *"the agent's MEMORY of what the learner
actually did"*. 🟢 **`ACTION MX` read its retention surface as code. The memory is not
protected.**

| what was checked | measured at `HEAD 91fef112` |
|---|---|
| 🟢 LRS HTTP API | 🟢 **route decorators are `get`, `put`, `post` and NOTHING ELSE — there is no `@router.delete`.** Over the LRS API a statement cannot be deleted |
| 🔴 `xAPI` voiding | 🔴 `voidedStatementId` is accepted and its own description reads **"*Not implemented* Id of voided Statement to fetch"**. The spec's OWN substitute for deletion is absent |
| 🔴 storage backend | 🔴 `BaseOperationType` declares **`DELETE`** *("deletes an existing record")* and **`UPDATE`** *("updates or overwrites an existing record")*; `--es-op-type` exposes them as a **first-class CLI option** |
| 🔴 default write mode | 🔴 `default_operation_type = INDEX`, and `INDEX` *"creates a new record with a specific ID"* — so a re-write carrying an existing statement id **OVERWRITES** |
| 🔴 immutability / append-only / WORM | 🔴 **ZERO occurrences in `6` files read.** The one "Immutability" string is the `xAPI` `format=canonical` docstring, about Activity/Verb representation — 🔴 **not a storage guarantee, and it must not be quoted as one** |

🔴 **So `ralph` is append-only AT THE API LAYER AND NOWHERE ELSE. The audit record's
protection is the absence of an HTTP route.** 🟢 Anyone holding Elasticsearch or MongoDB
credentials deletes or overwrites statements using ralph's own CLI, in one documented
option. 🔵 **Still the right LRS to adopt — it is `MIT` and it runs at national scale —
but the WORM store is a SEPARATE line item, not a property you inherit.** Pattern `32`
step `3` is amended.

🔴 **This is the SECOND independent instance of p187's `dotty-tutor` finding**, and two
unrelated projects make it a class rather than a bug: in `dotty-tutor` the teacher's
`corrected_assessment` is `CASCADE`-deleted by its class; in `ralph` the record has no
immutability at all. 🔵 **The human-oversight record is protected by convention, never by
the store.**

### 🆕 🟢 NEW LAYER — the credential, and it is the only cryptographically durable row here

🔵 p187 added the record store. 🟢 **`topics/open-badges` supplies the layer above it, and
the permissive rows are all on the `OB 3.0` / W3C Verifiable Credentials side of a
migration.**

| component | licence | layer | what it does |
|---|---|---|---|
| 🆕 🟢 **[`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget)** | 🟢 **`MIT`** *(`1 080` B)* | 🟢 **Open Badges `3.0`** | badge/credential definition authoring on the current standard |
| 🆕 🟢 **[`oneorigin-2-0/dcc-credential-co-writer-monorep`](https://github.com/oneorigin-2-0/dcc-credential-co-writer-monorep)** | 🟢 **`MIT`** *(`1 087` B)* | VC issuance | 🟢 built on the **Digital Credentials Consortium** stack — the MIT-led effort, i.e. the side a university registrar recognises |
| 🆕 🟢 **[`iblai/wallet`](https://github.com/iblai/wallet)** | 🟢 **`MIT`** *(`1 063` B)* | holder wallet | 🟢 pairs with [`iblai/lms`](https://github.com/iblai/lms) *(`MIT`)*, already on this table — **one publisher covering LMS → credential → wallet** |
| 🆕 🟢 **[`MrPrinceAli/proven`](https://github.com/MrPrinceAli/proven)** · **[`brody-0125/signet-campus`](https://github.com/brody-0125/signet-campus)** | 🟢 **`MIT`** *(`1 095` / `1 070` B)* | verification · campus issuance | the verifier and issuer ends |
| 🔴 [`hoijui/obadgen`](https://github.com/hoijui/obadgen) | 🔴 `AGPL-3.0` *(`34 020` B)* | generation | copyleft — not a vendoring candidate |
| 🔴 [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) | 🔴 `LGPL` *(`7 650` B)* | legacy | 🔵 Open Badges **`2.0`** — the generation this layer is leaving |

🟢 **The licence/generation split is unusually clean and it favours a studio: permissive on
`OB 3.0`/VC, copyleft on `2.0`.** 🔵 And it is the layer that answers this week's
regulation *(see [`intel/market.md`](../intel/market.md))*: where Oklahoma, Maryland, the
EU's Annex III and Vietnam's Decision `33/2026/QD-TTg` all demand a durable record of a
human decision about a learner, **a verifiable credential is the one artefact in this
stack that is durable by cryptography rather than by convention.**

### 🟢 Platforms added to the routing table

| platform | licence | region | layer / note |
|---|---|---|---|
| 🆕 🟢 **[`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT)** | 🟢 **`Apache-2.0`** *(`10 982` B)* | EMEA | `447`★ — 🟢 **a complete university LMS under a permissive grant.** p187's "permissive ROUTE" call, now read and confirmed. 🔴 No `MCP` surface |
| 🆕 🟢 **[`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi)** | 🟢 **`Apache-2.0`** *(`10 273` B)* | North America | `376`★ — the **LTI framework by the LTI spec's own author**. The integration layer, permissively licensed |
| 🆕 🟢 **[`academico-sis/academico`](https://github.com/academico-sis/academico)** | 🟢 **`MIT`** *(`1 094` B)* | 🟢 **LATAM** | `404`★ — 🟢 **a permissive SIS built in-region.** The first time this table answers a LATAM SIS question with a LATAM row |
| 🆕 🟢 **[`numbas/Numbas`](https://github.com/numbas/Numbas)** | 🟢 **`Apache-2.0`** *(`11 357` B)* | EMEA | `215`★ — assessment authoring + marking, Newcastle University. LTI side is [`numbas-lti-provider`](https://github.com/numbas/numbas-lti-provider) 🟡 *(`Apache-2.0` **by reference**, `560` B)* |
| 🆕 🟢 **[`openfun/marsha`](https://github.com/openfun/marsha)** | 🟢 **`MIT`** *(`1 078` B)* | EMEA | `151`★ — video for an LMS, **France Université Numérique**. 🔵 Same publisher as `ralph`: one EMEA public body now supplies two layers of this stack |
| 🆕 🔴 **[`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis)** | 🔴 `GPL` *(`15 214` B)* | EMEA | `646`★ SIS — copyleft |
| 🆕 🔴 **[`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms)** | 🔴 `GPL-3.0` *(`35 147` B)* | EMEA | `1`k★ — grant now read; still no `MCP` surface |

### 🔴 DO-NOT-FORK, added this pass

| row | verdict |
|---|---|
| 🟡 **[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic)** | 🟢 `345`★, and the grant is **`GPL-2.0` with its FULL TEXT IN THE TREE** at `docs/License.txt` *(`17 286` B, re-read p215)*; the README points there. 🔴 **Nothing at the `10` probed ROOT paths.** 🔵 **p215 WITHDRAWS this row from `P971`:** the terms DO travel with the work, so a fork inherits no textless obligation — the instance was a root-only artefact <!--corrected--> |
| 🆕 🔴 **[`No-Suggest/NoSuggest`](https://github.com/No-Suggest/NoSuggest)** | 🔴 `36`★, **NOT OPEN SOURCE.** The whole `417` B licence: *"Source code is made available for transparency and personal non-commercial use only … You may NOT: Redistribute … Rebrand or redeploy this application commercially or publicly … Use this code as the basis for a competing product or service. All rights reserved."* |
| 🆕 🔴 **[`Rick-254/moodle-quizsmith`](https://github.com/Rick-254/moodle-quizsmith)** · **[`VICKY07092005/moodle-5-1-authentic-relay`](https://github.com/VICKY07092005/moodle-5-1-authentic-relay)** | 🔴 Both claim **`MIT` in the README and nowhere else** — no licence file at `15` paths, no grant in `22` header paths. 🔴 **And both are Moodle-plugin-shaped, where Moodle's own rules require `GPL`** — an `MIT` claim over a plugin linking `GPL` core is a claim its dependency may not permit |

Evidence: [`evidence/openedx-agent-surface.2026-10-14-p188.tsv`](../evidence/openedx-agent-surface.2026-10-14-p188.tsv),
[`evidence/ralph-retention-surface.2026-10-14-p188.tsv`](../evidence/ralph-retention-surface.2026-10-14-p188.tsv),
[`evidence/new-supply-grants.2026-10-14-p188.tsv`](../evidence/new-supply-grants.2026-10-14-p188.tsv).

## Pass 187 — 2026-10-14

🆕 🟢 **The routing table gains a LAYER it has never had — the learning record store — and the
`MCP` row p186 added as a curiosity is promoted to a column, because every major LMS on this table
now has one.**

### 🟢 NEW LAYER — the Learning Record Store, named at last

🔵 **This page has told implementers to "stand up an LRS" for many passes without naming a
permissive one.** 🟢 **Two now exist on the shelf, and one of them is a national platform's.**

| platform | licence | layer | tenancy | AI seam |
|---|---|---|---|---|
| 🆕 🟢 **[`openfun/ralph`](https://github.com/openfun/ralph)** | 🟢 **`MIT`** *(`LICENSE.md`, `1 094` B)* | 🟢 **LRS** — `xAPI` statements in, queryable analytics out | self-hosted; **France Université Numérique** runs it at national scale | 🟢 **the agent's MEMORY of what the learner actually did**, in a standard format, separable from the LMS |
| 🆕 🟢 **[`scormflow/scorm-engine`](https://github.com/scormflow/scorm-engine)** | 🟢 **`MIT`** *(`LICENSE`, `1 079` B)* | 🟢 `SCORM` **+ `xAPI` + `cmi5` + LRS** in one tree | self-hosted | 🟢 content standards AND the record store without stitching two projects together |

🔵 **Why a separate LRS layer changes an engagement.** 🔴 Every tutoring pattern on this shelf has
had to answer *"where does the interaction history live?"* with either the LMS's own tables *(a fork)*
or a bespoke store *(a migration later)*. 🟢 **An `xAPI` LRS is the answer that outlives the tutor:
swap the model, keep the record.** 🔵 And `xAPI`/`cmi5` is what a procurement officer already knows
how to ask for.

### 🟢 PROMOTED TO A COLUMN — `MCP` availability per platform

🟢 **p186 added `sisu-mcp` as a new layer. `ACTION MR` shows it was the first row of a populated
one**: the agent-tool surface is now a property worth recording for every platform on this table.

| platform | the `MCP`/agent surface, as found | licence of the surface |
|---|---|---|
| 🟢 **Moodle** *(`GPL-3`, `v5.x`)* | 🟢 **three independent servers**: [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) *(courses, assignments, grades)*, [`CloudDown/polymtl-moodle-connect`](https://github.com/CloudDown/polymtl-moodle-connect) *(with installers)*, [`onbirdev/moodle-webservice_mcp`](https://github.com/onbirdev/moodle-webservice_mcp) *(in-tree, as a web service plugin)*. 🟢 Plus [`valentineus/moodle-webhooks`](https://github.com/valentineus/moodle-webhooks) for **push** | 🟢 `MIT` / `MIT` / `GPL-3.0-or-later` *(file headers)* |
| 🟢 **Canvas** | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) *(`9`★)*; 🟢 **[`chaz-clark/canvas-toolbox`](https://github.com/chaz-clark/canvas-toolbox) adds a `FERPA`-safe wrapper** | 🟢 `MIT` |
| 🟢 **Brightspace / D2L** | [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) *(`57`★ — the category's most-starred row)* | *(on shelf; grant recorded earlier)* |
| 🟢 **Sisu / Funidata** *(SIS)* | [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) — 🟢 **read-only by design** | 🟢 `MIT` *(`package.json` only)* |
| 🟢 **`SCORM`** *(as a format)* | [`kemalyy/edumints-scorm-mcp`](https://github.com/kemalyy/edumints-scorm-mcp) + [`-skill`](https://github.com/kemalyy/edumints-scorm-skill) | 🟢 `MIT` |
| 🔴 **Open edX** *(`AGPL-3`)* | 🔴 **NO `MCP` server found** on any page read this pass | — |
| 🔴 **Chamilo, OpenOLAT, Sakai** | 🔴 **none found** | — |

🔴 **`Gap 427`, and it is the one to quote in a planning conversation: the agent-tool layer exists
for the platforms with the most permissive or most commercial gravity, and NOT for `AGPL` Open edX
nor for the European academic platforms.** 🔵 An Open edX client is therefore an adapter build, and
should be priced as one.

### 🟢 NEW LAYER — compliance as code, in front of the model

🔵 **Every pattern on this shelf has described student-data protection as a design obligation.
`topics/ferpa` returned it as SOFTWARE.**

| component | licence | layer | what it does |
|---|---|---|---|
| 🆕 🟢 **[`Principled-Evolution/gopal`](https://github.com/Principled-Evolution/gopal)** | 🟢 **`Apache-2.0`** *(`11 357` B)* | 🟢 **`Rego` policy** | `8`★ — AI-compliance policies including `FERPA`, as policy-as-code. 🟢 Drops into an `OPA` gate a client may already run for other reasons |
| 🆕 🟢 **[`Polycentric-Labs/regrails`](https://github.com/Polycentric-Labs/regrails)** | 🟢 **`Apache-2.0`** *(`11 282` B)* | guardrail | 🟢 **`FERPA` AND Title IV together** — the first row here treating student *funding* rules as an AI surface |
| 🆕 🟢 **[`ashutoshrana/haystack-ferpa-filter`](https://github.com/ashutoshrana/haystack-ferpa-filter)** | 🟢 **`Apache-2.0`** *(`12 101` B)* | RAG pre-filter | a `FERPA` document filter for **Haystack** pipelines. 🟡 One author publishes five adjacent repos — one body of work, not five corroborations |
| 🆕 🟢 **[`siskinskai/spedlex`](https://github.com/siskinskai/spedlex)** | 🟢 **`MIT`** *(`1 076` B)* | vocabulary | 🟢 **special-education terms for de-identifying student PII/PHI** — the asset nobody budgets for and every SPED engagement needs |
| 🆕 🟢 **[`ZachRouan/district-brain`](https://github.com/ZachRouan/district-brain)** | 🟢 **`MIT`** *(`1 066` B)* | role-scoped RAG | locally hosted district assistant, **scoped by role** rather than filtered after retrieval |
| 🆕 🟢 **[`zhamanov-seabus/nau-ai-advisor`](https://github.com/zhamanov-seabus/nau-ai-advisor)** | 🟢 **`Apache-2.0`** *(`11 375` B)* | application | a self-hostable **`FERPA`-aware academic advisor** |

### 🟢 Platforms added to the routing table

| platform | licence | region | layer / note |
|---|---|---|---|
| 🆕 🟢 **[`rage/secret-project-331`](https://github.com/rage/secret-project-331)** | 🟢 **`Apache-2.0`** *(`11 357` B)* | EMEA | `320`★ — **University of Helsinki**'s MOOC platform. 🟢 The most permissive course-delivery platform on this table |
| 🆕 🟡 **[`acanas/swad-core`](https://github.com/acanas/swad-core)** | 🔴 **`AGPL-3.0`** *(`34 501` B, `sha256`₁₂ `884b434957ba`)* <!--corrected--> | EMEA | `76`★ — Universidad de Granada, two decades in production. 🔴 **network-use obligation** |
| 🆕 🟡 **[`xiaochong0302/course-tencent-cloud`](https://github.com/xiaochong0302/course-tencent-cloud)** | 🟡 `GPL-2.0` *(`18 092` B)* | APAC | `1.2`k★ — PHP, Docker, knowledge-sales oriented. 🔵 **`GPL-2`, so `P960` applies: NOT `LGPL`** |
| 🆕 🟢 **[`iblai/lms`](https://github.com/iblai/lms)** | 🟢 `MIT` *(`1 062` B)* | North America | skills / competencies / credentials, with a `wallet` companion |
| 🆕 🟡 **[`LaurentSta/Oneduc`](https://github.com/LaurentSta/Oneduc)** | *(grant unread this pass)* | EMEA | Laravel LMS with `SCORM` + native quizzes — recorded for a later probe |

### 🔴 DO-NOT-FORK, recorded with the reason

| row | verdict |
|---|---|
| 🔴 **[`alfredang/AI-LMS-TMS`](https://github.com/alfredang/AI-LMS-TMS)** | 🔴 **NO GRANT.** 🟡 But its `57 120` B README is the best description this KB holds of Singapore's `WSQ`/`SkillsFuture`/`SSG` assessment-and-funding regime — assessor signature blocks stamped into submitted documents, `TRAQOM` survey completion gating trainer payout, per-method submission states. 🟢 **Read as APAC domain intelligence; build your own** |
| 🔴 **[`willwearing/graspful`](https://github.com/willwearing/graspful)** | 🔴 **NOT OPEN SOURCE** — `P1054`, MIT's body with an anti-SaaS non-compete appended |
| 🔴 **[`Nasus20202/MoodleMCP`](https://github.com/Nasus20202/MoodleMCP)** | 🔴 **NO GRANT** at `10` paths plus README |

## Pass 186 — 2026-10-14

🆕 🟢 **The routing table gains a row in a layer it had only ever described as *"build an adapter"*,
and the `opencast` row gains the named class an implementer needs. One row moves to DO-NOT-USE on
its licence text.**

### 🟢 NEW LAYER — the student record as an agent TOOL SURFACE: `ink-waffle/sisu-mcp`

| platform | licence | layer | tenancy | AI seam |
|---|---|---|---|---|
| 🆕 🟢 **[`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp)** | 🟢 **`MIT`** *(`"license": "MIT"` in `package.json`, `999` B — 🔴 **no licence file in the tree**)* | 🟢 **SIS access as `MCP` tools** — `sisu_studies`, `sisu_attainments`, `sisu_connect` / `sisu_status` / `sisu_disconnect` | 🔵 per-user browser session, renewed automatically; stored locally | 🟢 **the server IS the seam.** An agent calls the SIS directly; there is no adapter to write |

🟢 **Why this changes a conversation.** Every SIS row above this one — `openSIS`, `Fedena`,
`Kosudo/nextSIS`, the Ed-Fi SDKs — is a system you integrate WITH. 🟢 **This is a system already
shaped as tools an agent can call, and `read-only` is the server's stated design, not a promise in a
statement of work.** 🔵 For a university engagement, *"the agent can see the student's attainments
and cannot change them"* is a sentence that survives a data-protection review; *"we will restrict
the integration to reads"* is a sentence that invites one.

🔴 **Three limits, stated before anyone quotes it.** It targets **one** SIS product — Sisu, by
Funidata, run by the Finnish universities *(`sisu.tuni.fi` is the README's own example)*, so outside
the Nordics it is a DESIGN to copy rather than a dependency to adopt. It is `0`★ and
`"version": "0.1.0"`. 🔴 **And the grant exists only as an npm manifest field** — there is no licence
file, which is exactly why this KB recorded it as unlicensed until this pass.

### 🟢 `opencast/opencast` — the ROUTE grade is confirmed, and the implementer now has a class name

🔵 **p185 graded `opencast` a ROUTE on a SCHEMA-level provider abstraction and pre-registered
`ACTION MM` to find the code seam. It is found.**

| what an implementer gets | detail |
|---|---|
| 🟢 **the interface** | `org.opencastproject.transcription.api.TranscriptionService` in **`modules/transcription-service-api`** — a public `api` module, `ECL-2.0`, `7` methods |
| 🟢 **the shape** | asynchronous with callbacks: `startTranscription` → `Job`, then `transcriptionDone` / `transcriptionError`. 🔵 **Exactly how an agent wants to be invoked** |
| 🟢 **the extra channel** | `getReturnValues(mpId, jobId)` exists so a provider can hand the attach handler more than the transcript — confidence, diarisation, an agent's own metadata |
| 🔴 **the deployment limit** | **`getLanguage()` returns ONE `String`.** One provider instance, one language |

🔴 **That last row is a pricing fact, not a detail.** 🟢 **A bilingual institution registers one
provider instance per language and routes on the series' language in the workflow.** 🔵 **For LATAM
*(`pt-BR` + `es`)* and for much of EMEA, multiply the configuration and the testing by the number of
languages — and remember `opencast` ships **`0`** `pt-BR` / `pt-PT` locale catalogues *(`17`
catalogues, `es-ES` and `gl-ES` present)*, so a Brazilian deployment carries a translation project
on top.

### 🟢 Confirmed, not new: `ai-shifu/ai-shifu` is `Apache-2.0` — and the confirmation is a correction

🟡 **`P1052` returned `ai-shifu` as a licence recovery. It is not one.** 🟢 **`LICENSE.txt`,
`11 342` B, `Apache License 2.0`, *«Copyright 2024 ai-shifu.com»* — and this KB has recorded exactly
that since p184.** 🔴 **The row entered a *"no grant"* population through a defect in p185's own
single-slug-per-line extractor.** 🔵 **So the `61`-row population was not `61` absences, and the
`43`/`61` *"absence holds"* denominator published yesterday is soft at the edges.** 🟢 **The
platform's ROUTE grade and its `29`-table commerce coupling *(p185, `ACTION MG`)* are unchanged.**

### 🔴 Moving to DO-NOT-USE: `ShuyunYuan/talentcoach`

🔵 Surfaced this pass on `topics/intelligent-tutoring-system?s=updated` as an *"adaptive guided
tutoring and performance support system for workplace training"* — a description that reads like a
corporate-L&D ROUTE candidate.

🔴 **Its `LICENSE` is `842` B and says: *"All rights reserved … published for portfolio and
code-review purposes only. Viewing the source on GitHub is permitted; no other rights are
granted."*** 🔴 **Then it copies `MIT`'s warranty disclaimer verbatim**, which is why an automated
grant-text matcher flags it as permissive.

🟢 **The rule this forces onto the routing table, and it is cheap:** a licence FILE is not a
licence. 🔵 **`842` B is too short for `Apache-2.0` and too long for `MIT` — and on this shelf an
anomalous byte count now means *read the file*, because three distinct sub-`1`kB shapes have been
measured and only one of them grants anything** *(`Gap 421`)*.

## Pass 185 — 2026-10-14

🆕 🟢 **One platform enters the routing table and fills a layer that had `0` rows; one platform's
ROUTE grade gains a qualifier that changes what a studio may promise; and one row is added to the
DO-NOT-BUILD column for a reason that is not a licence.**

### 🟢 NEW LAYER — lecture capture and video management: `opencast/opencast`

| platform | licence | layer | tenancy | AI seam |
|---|---|---|---|---|
| 🟢 **[`opencast/opencast`](https://github.com/opencast/opencast)** | 🟢 **`ECL-2.0`** *(`11 340` B, full text; OSI-approved `Apache-2.0` derivative for universities)* | 🟢 **lecture capture + video management** — `oc_series`, `oc_scheduled_extended_event`, `oc_assets_snapshot`, `oc_acl_managed_acl`, `oc_search`, `oc_oaipmh` | 🔵 per-institution install *(`modules/adopter-registration-*` exists; multi-tenancy NOT measured this pass)* | 🟢 **`oc_transcription_service_provider` is a SCHEMA-level provider abstraction, and `modules/speech-to-text-workflowoperation` is the named attachment point** |

🟢 **This is the row a university engagement has been missing.** Everything else on this table is an
LMS, an SIS or an ERP; **none of them owns the lecture recording.** 🔵 `opencast` owns the capture,
the versioned asset, the access-control list and the publication channel — and it already speaks
`OAI-PMH`, so the library's harvester needs no adapter.

🟢 **Three LOCAL transcription engines in-tree** *(Whisper, whisper.cpp, Vosk, each with
`etc/*.cfg` and an admin-guide page)*, against four cloud providers.
🔵 **For a public university under a data-residency constraint, that is the difference between a
procurement conversation and a deployment.**

🔴 **Two honest limits before anyone quotes it:** `230` modules is a large operational surface — this
is a platform to run, not a library to import — and **`0` of its `17` locale catalogues is `pt-BR`
or `pt-PT`**, so a Brazilian engagement starts with a translation project *(`es-ES` and `gl-ES`
are present)*.

### 🟡 QUALIFIER — `ai-shifu/ai-shifu` is a ROUTE *for a paid-course engagement*

🔵 **p184 placed `ai-shifu` as a ROUTE and pre-registered `ACTION MG` to test whether the `29`
commerce tables are droppable. They are not droppable from the LEARNING half.**

| half | coupling | verdict |
|---|---|---|
| 🟢 **authoring** *(`shifu_draft_*`, `shifu_published_*`, outline items)* | **`1` of `55`** core `shifu/` files touches billing *(`shifu/route.py`, creator usage admission)*; `17` of the other `18` importers are `admin*` | 🟢 **LIFTABLE** |
| 🔴 **learning runtime** *(`learn_progress_records`, generated blocks/elements)* | **`14` of `55`** `learn/` files import `order`/`billing`/`promo`/`credit`/`referral`; the status vocabulary is DEFINED in `order/consts.py:12-20`; `learn/models.py:6` imports `LEARN_STATUS_LOCKED` from the order module; **lesson access is gated on `Order.status == ORDER_STATUS_SUCCESS`** *(`learn/agent/lesson_entry.py:188-200`)* | 🔴 **NOT SEPARABLE without replacing the access gate** |

🔴 **And the measurement that makes this generalisable: `ForeignKey` appears `0` times in the entire
`ai-shifu` service tree.** 🔵 **A schema-level FK census would have declared the platform fully
separable and been wrong. On a project with no declared referential integrity, coupling can only be
read in the IMPORT graph.** 🟢 **`P1051`.**

🟢 **So the promise a studio can make:** *"we can lift the authoring model"* — yes.
*"we can deploy it for a ministry's free courses"* — only after replacing `_require_access()`, the
`601`–`608` status vocabulary's home, and the metering admission calls in the learn path.
🔵 Evidence: [`evidence/ai-shifu-commerce-coupling.2026-10-14-p185.tsv`](../evidence/ai-shifu-commerce-coupling.2026-10-14-p185.tsv).

### 🟢 Rows this table can now route to, after `ACTION MD`

- 🟢 **[`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) is
  `Apache-2.0`** *(`## License` → *"Copyright ©2016 Advanced Distributed Learning / Licensed under
  the Apache License, Version 2.0"*)*. 🔵 **The SCORM→xAPI bridge published by the steward of both
  standards is usable after all** — this table recorded it as unlicensed for five passes.
- 🟢 **[`CreveXTech/canvas-lms-mcp`](https://github.com/CreveXTech/canvas-lms-mcp) is `MIT`**, so the
  Canvas connector column has a shippable row that is not a dangling reference. 🔴 **Unlike
  [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms), whose README
  points at a `LICENSE` file that does not exist.**
- 🟢 **[`educredentials/ec-issuer`](https://github.com/educredentials/ec-issuer) is `MIT`**, which
  changes `Gap 325`: the Open Badges 3.0 + ELM + OID4VCI issuer is permissive, and the credentialing
  column has a real candidate.

### 🔴 DO NOT BUILD — and this one is a prohibition, not a licence

🔴 **[`mskljns/ComprehensionProblems_DAiSEE`](https://github.com/mskljns/ComprehensionProblems_DAiSEE)
infers learner comprehension from facial video** *(DAiSEE labels: boredom, confusion, engagement,
frustration)*. **`AI Act` Article `5`(1)(f) prohibits emotion inference in education institutions**,
in force since **`2025-02-02`**, and a prohibition has **no conformity-assessment route out**.
🔵 **It also has `0` licence files, but the licence is the lesser blocker.** 🟢 **`Gap 416`: every
webcam-affect row this table meets stops at the same line, and the client conversation is about
replacing affect inference with interaction signals the learner knowingly produces.**

## Pass 184 — 2026-10-13

🆕 🟢 **Three changes to the routing table, and all three change what a studio can PROMISE: one
platform's licence family is corrected, one platform's integration boundary is now MEASURED rather
than argued, and one row leaves the table because it does not exist.**

### 🟢 `openeducat_erp` — the SIS boundary is real, and the project proves it on itself

🔵 **Pattern `26` told a studio to deploy `openeducat_erp` unmodified, add nothing inside
`openeducat_*`, and build the missing `OneRoster` / `LTI 1.3` / `Ed-Fi` layer as NEW addons. The
open question was whether that is architecturally possible or merely a licence slogan.**
🟢 **It is possible, and the evidence is openeducat's own `14` modules:**

| measurement at `HEAD 46a5d7d` | value | what it means |
|---|---|---|
| 🟢 `odoo.addons.openeducat*` Python imports, tree-wide | **`0`** | 🟢 **no module imports another's Python** |
| 🟢 `env['op.*']` accesses by model-name string | **`218`** | 🟢 **this is how the tree crosses its own boundaries** |
| 🟢 inter-module coupling | `__manifest__.py` `depends` *(`7` modules depend on `openeducat_core`)* | 🟢 **declared as DATA, not as an import** |
| 🟡 `_inherit` declarations | `55` | 🟡 **the grey zone — see below** |

🟢 **So a new addon reads and writes `op.course`, `op.student`, `op.exam` and the other `59`
business models through the registry, by name, with no `openeducat_*` import anywhere.**
🔵 **`env['op.session']` appears `22` times, `env['op.student']` `21`, `env['op.course']` `19` —
inside openeducat itself.**

🟡 **The caveat, and it is the line Pattern `26` is actually drawing:** `_inherit = 'op.course'`
from a new addon **extends openeducat's model in place**, which is a different act from reading it.
🔵 **Read `op.*` and add your own models: clean. Extend `op.*` in place: that is the *"patch"* in
*"add, do not patch"*.** 🔴 **Whether `LGPL-3.0` §`5` treats registry-mediated inheritance as *"a
work that uses the Library"* is counsel's question — this KB measured the technical boundary and
says so, rather than implying a legal answer.**

🔴 **And the entity count is corrected: `59` business models, not the `141` p183 published**
*(`88` `_name` declarations + `55` `_inherit` extensions = `143`, which is how that number was
reached)*. 🟢 **`59` is what belongs in a proposal.**

### 🟡 `formalms` — `GPL-2.0`, entity-rich, and it stays on the copyleft side of the table

🟢 **Settled: `GPL-2.0`**, payload at `html/license.txt` *(`18 346` B, `md5 65dd37cc…`, `0`
occurrences of *"Lesser"*)*, installer copies in `8` languages, every PHP header naming
`gpl-2.0.txt` and the Docebo `4.0.5` CE lineage. 🔴 **Not `Apache-2.0`.**

🟡 **It is a genuine LMS, which is why this matters:** `405` `CREATE TABLE`, with
`learning_course`, `learning_coursepath`, `learning_course_editions`, `learning_certificate_course`,
`learning_competence_course`, `learning_assessment_rule`, `learning_catalogue`, and a
`conference_*` family that already integrates BigBlueButton. 🟢 **Routing verdict: a copyleft
DEPLOYMENT — deploy it, keep the AI in a separate permissive service, and never absorb its code
into a client's product.** 🔵 **Same engagement shape as Moodle and Open edX, now with a verified
grant instead of a quoted one.**

### 🔴 `apereo/opencast` leaves the table; `opencast/opencast` enters as UNREAD

🔴 **`apereo/opencast` does not exist** *(`git ls-remote` `exit 128`, identical to an invented
control slug)*. 🟢 **The real project is
[`opencast/opencast`](https://github.com/opencast/opencast)**, `HEAD e7655449`, default branch
`develop`. 🔵 **The lecture-capture layer therefore has `0` read rows in this KB, not one unprobed
one — a different and more honest statement.** 🟢 `ACTION ME` reads it at p185.

### 🟢 The routing table, unchanged where it was already measured

🔵 **For reference, the rows this pass did not touch keep their verdicts:** `Moodle` *(`GPL-3.0`,
deployment)*, `Open edX` *(`AGPL-3.0`, deployment — the strongest copyleft on the table)*,
`Canvas LMS` *(`AGPL-3.0`)*, `BigBlueButton` *(`LGPL-3.0`)*, `H5P` *(`MIT`, absorbable)*,
`Kolibri` *(`MIT`, offline-first)*, `Sakai` *(`Apache-2.0`)*, `OpenOLAT` *(`Apache-2.0`, the
permissive ROUTE)*, `Artemis` *(`MIT`)*. 🔴 **`0` permissive student-information systems still
exist** — `RosarioSIS` and `Gibbon` are `GPL`, `openeducat_erp` is `LGPL-3.0`, and `formalms` is
now a measured `GPL-2.0`. 🟢 **Which is exactly why Pattern `26` is a module boundary and not a
licence hope.**

## Pass 183 — 2026-10-13

🆕 🟢 **Two amendments to the routing table, both to rows this KB has carried for passes, and both
change what a studio can PROMISE rather than what it can pick.**

🟢 **`Gap 362` — *"open-core unverified"* — closes for
[`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE), in both
directions at once: `0` capability gates in `4 702` files, and an Enterprise Edition the README
declares in its own words.** 🟢 **And
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) — the SIS route this
KB has carried for `16` passes on its licence alone — finally has its domain model MEASURED:
`141` Odoo models, and they are real.**

### 🆕 🟢 `openeducat_erp`, amendment — `T162` was about standards, not about entities

🔵 **This KB's record on this row has been a licence, a byte count and an absence: `LGPL-3.0`,
`8 241` B, APAC *(India)*, and `T162` — its vendor-stated OneRoster / Ed-Fi / `LTI 1.3` support is
absent from the open tree. 🔴 What was never measured is whether the SIS underneath those missing
standards exists at all.** 🟢 **It does.**

| measured this pass *(`HEAD 46a5d7d`, `1 345` tracked files)* | value |
|---|---|
| 🟢 **Odoo models** | **`141`** `_name = ` declarations |
| 🟢 **modules** | **`13`**: `core`, `admission`, `exam`, `assignment`, `attendance`, `classroom`, `timetable`, `fees`, `library`, `parent`, `facility`, `activity`, `erp` |
| 🟢 **admissions** | `op.admission`, `op.admission.register`, `op.admission.fees.line` |
| 🟢 **academic structure** | `op.course`, `op.batch`, `op.classroom`, `op.department`, `op.academic.year`, `op.academic.term`, `op.faculty` |
| 🟢 **assessment** | `op.exam`, `op.exam.type`, `op.exam.session`, `op.exam.room`, `op.exam.attendees`, `op.held.exam`, `op.marksheet.register`, `op.marksheet.line`, `op.grade.configuration` |
| 🟢 **attendance** | `op.attendance.register`, `op.attendance.sheet`, `op.attendance.line`, `op.attendance.type` |
| 🟢 **operations** | `op.fees.terms`, `op.fees.terms.line`, `op.fees.element`, `op.library.card`, `op.media`, `op.media.movement`, `op.facility`, `op.activity` |

🟢 **The grade is unchanged — `LGPL-3.0` keeps it integrate-only — but the SENTENCE a studio says
about it changes.** 🔴 **Before: *"the one integrated LMS+SIS route, copyleft, and its standards
claims do not survive a read."*** 🟢 **Now: *"a `141`-entity SIS with admissions, examinations,
marksheets, attendance and fees already modelled, under weak copyleft, with the interoperability
layer missing and therefore in scope."*** 🔵 **`T162`'s absence stops being a disqualification and
becomes the deliverable: the missing standards are exactly where a studio's work goes.**

🟢 **The `LGPL` engagement rule, stated once:** 🔵 **weak copyleft reaches the MODULE you modify,
not the application that calls it.** 🟢 **Add `openeducat_`-adjacent modules of your own and keep
them closed — a OneRoster or `LTI 1.3` bridge is a NEW module, which is the easy side of that
line.** 🔴 **Patch `openeducat_core` in place and you publish that module.** 🔵 **So: add, do not
patch.**

🔴 **Three caveats, none of them a measurement.** 🔴 The tree is **Odoo-coupled**, so adopting it
adopts Odoo's licence posture and upgrade cadence. 🔴 **`LGPL` linking semantics for Python/Odoo
addons are a legal reading** — say *"weak copyleft, scoped to the modules you edit"* and route a
commercial-resale question to counsel, the same discipline this KB applies to `sakai`'s
educational-use patent grant. 🔴 **The holder's own licence header warns that bundled external
libraries *"may be published under other GPL-compatible licenses"*** — the tree is not
single-grant, and a dependency closure is a separate job.

### 🆕 🟢 `open-tutor-ai-CE`, amendment — ungated, open core DECLARED, and never a course platform

| axis | verdict this pass |
|---|---|
| 🟢 **capability gating** | 🟢 **NONE.** `0` hits for `license_key`, `is_enterprise`, `feature_flag`, `entitlement`, `paywall`, `upgrade_required` across every `.py` in `4 702` files. A full account lifecycle is present |
| 🔴 **open core** | 🔴 **DECLARED**, resolving `Gap 362` for this row: *"the foundation for a proprietary **Enterprise Edition (EE)**"*, which *"includes custom theming & branding, SLA support, LTS versions, **and more"*** |
| 🔴 **domain model** | 🔴 **`10` tables tree-wide, all chat/file/user.** `learning/courses/` is a `30`-byte docstring; `learning/sessions/service.py` is `"""Chats service."""` *(`ACTION LS`)* |
| 🔴 **tenancy** | 🔴 `0` references anywhere |
| 🟢 **what it is still good for** | 🟢 **An ungated `BSD-3-Clause` chat-and-RAG appliance with real identity and `ar-MA` + `fr-FR` locales** — the Maghreb-facing option, and the cheapest permissive place to put a tutoring conversation |

🔵 **Reading the open-core verdict correctly: `declared` is not a disqualification.** 🟢 **The CE
runs, complete, today.** 🔴 **It is a dependency on a vendor's roadmap, and it belongs in a
proposal's risk section rather than a footnote.** 🆕 🔵 **And it is the axis this KB's strongest
channel cannot see: an open-core edition is invisible to `git clone`. `Gap 362` stays OPEN for
every other row, because silence in a README is not evidence of absence.**

### 🔴 What the routing table still cannot do

🔴 **`0` permissive, North-American-origin, ROUTE-grade rows — fourth pass.** 🔵 The permissive
routes remain European *(`OpenOLAT` `Apache-2.0`, `Artemis` `MIT`, `feedbacksystem` `Apache-2.0`,
`mentingo` `MIT`)*.

🔴 **`0` permissive student-information systems — and that absence is now better described.**
🔵 **`RosarioSIS` and `Gibbon` are `GPL`; `openeducat_erp` and `odoo/odoo` are `LGPL-3.0`;
`frappe/erpnext` is `GPL-3.0`.** 🟢 **So the honest line for an estimate is not *"budget a
build"* but *"budget modules against a weak-copyleft SIS whose `141` entities are already
there"*** — a materially cheaper proposal, and the first pass at which this KB can say which.

## Pass 182 — 2026-10-13

🆕 🟢 **Two changes to the routing table, and they point in opposite directions.**
🟢 **[`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) loses the
precondition this KB was about to attach to it** — `ACTION LQ` establishes that its `Keycloak` is
an OPTION, not a dependency, so the institutional route does not require the client to operate an
identity provider. 🔴 **[`frappe/lms`](https://github.com/frappe/lms) is DISQUALIFIED from the
permissive column on its licence payload.**

🆕 🟢 **And the multi-tenant route is now verified at the layer that matters.**
[`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp)'s tenancy was credited
from its schema at p181; `ACTION LN` read it at the query layer and it holds *(see
[`agents/top.md`](../agents/top.md))*.

### 🟢 `ACTION LQ` — `feedbacksystem` needs no IdP, and that is a procurement saving

| measured | value | what it means for an engagement |
|---|---|---|
| 🟢 **SAML default** | `app.saml.enabled: ${APP_SAML_ENABLED:false}` | 🟢 **Federation is OFF out of the box.** The system boots and authenticates without any external IdP |
| 🟡 **the `keycloak` string** | `registration-id: ${APP_SAML_REGISTRATION_ID:keycloak}` | 🟡 **This is why it looked required.** It is the default NAME of a SAML registration, not a dependency |
| 🟢 **local fallback** | `SecurityConfig.kt:184` — `formLogin { loginPage("/login").permitAll() }`, unconditional; `saml2Login` is the conditional branch at `:195` | 🟢 A local login path always exists |
| 🟢 **it is itself an IdP** | own OIDC provider: client `fbs-web-shell`, signing key alias `identity-signing`, access-token and authorization-code TTLs, `post-logout-redirect-uri` set | 🟢 **It ISSUES tokens. A studio can put other services behind it** |
| 🔵 **where `Keycloak` actually appears** | `docs/saml-local-keycloak.md`, `application-saml-local.yaml` *(a local profile)*, `docker-compose.demo.yml` | 🔵 Dev and demo scaffolding — the normal way to test SAML locally |

🟢 **Pattern `20` and Pattern `22` do NOT need *"the client operates a Keycloak"* as a
precondition.** 🔵 **Federation is a configuration the client can turn on when their IT asks for
it, which is a much easier conversation than a procurement.**

### 🟢 The platform table, re-graded

🔵 **Grades: ROUTE** *(owns its data + its own auth + speaks a standard, or is multi-tenant — build
the engagement on it)*, **APPLIANCE** *(owns its data, deploys cleanly, no usable identity — one
learner or one cohort per deployment)*, **COMPONENT** *(neither — compose it into something else)*,
**integrate-only** *(copyleft reach makes a fork or hosted derivative a legal conversation)*.

| platform | layer | licence *(payload-verified)* | grade | standards, MEASURED | what it means for an engagement |
|---|---|---|---|---|---|
| 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | full LMS | 🟢 **`Apache-2.0`**, `10 982` B | 🟢 **ROUTE** | 🟢 `LTI 1.3` `252` files, `QTI` `1 201`, `SCORM` `355`, `OpenBadges` `263` | 🟢 **START HERE for a permissive full-LMS engagement.** `440` `@Entity`, own `Shibboleth`/`LDAP` auth. 🔴 Budget `385` tables and `186` Maven dependencies of discovery |
| 🟢 [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | multi-tenant tutoring + assessment | 🟢 `MIT`, `1 073` B | 🟢 **ROUTE — the MULTI-TENANT one, now ENFORCEMENT-verified** | 🟡 `MCP` server; 🔴 no `LTI`, `SCORM` or `QTI` | 🟢 **START HERE when the client sells to MANY institutions.** 🆕 Tenancy is fail-closed at a typed boundary, not a column: `36` scope-taking store methods, `350` `tenant_id` predicates, anti-replay session binding, `6` tests asserting refusal. 🟡 Read the in-flight `LearnerID` backfill before quoting |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | LMS *(TypeScript)* | 🟢 `MIT`, `1 062` B | 🟢 **ROUTE** | 🟢 **`SCORM 1.2` BOTH WAYS**; 🔴 `xAPI` `0`, `LTI` `0` | 🟢 **START HERE for a JS/TS studio.** `123` `pgTable`, `tenant` in `305` files. 🔴 **It cannot receive an `LTI` launch — it replaces a university's LMS rather than plugging into one** |
| 🟢 [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | automated grading | 🟢 `Apache-2.0`, `10 785` B | 🟢 **ROUTE** *(institutional)* | 🟡 own checker protocol; 🔴 no `LTI`/`SCORM` | 🆕 🟢 **No IdP precondition** *(`ACTION LQ`)*: `SAML` defaults off, local `formLogin` always present, and the `fbs-identity-service` module is **itself an OIDC provider**. Kotlin/Spring + Angular, from a German university |
| 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | interactive learning **+ assessment** | 🟢 `MIT`, `1 091` B | 🟢 **ROUTE** | 🟢 `LTI 1.3` with grade passback, nightly Moodle interop test | 🟢 The assessment specialist: `257` entities, `528` write endpoints. 🔵 **Pair with `OpenOLAT` rather than choosing** |
| 🟢 [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | AI tutor platform | 🟢 `MIT`, `1 068` B | 🟢 ROUTE | 🔴 none | 🟢 The smallest route a studio can hold in its head: `34` tables, `141` endpoints, `10+` LLM providers |
| 🆕 🟡 [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | AI tutoring layer | 🟢 **`BSD-3-Clause`**, `1 531` B | 🟡 **APPLIANCE+** | 🔴 none | 🟡 **`4 702` files with OWN identity** *(`user.py`, `users/repository.py`, `routers/auth.py`, `tests/test_auth.py`)*. 🔴 **But `data/models/` has `0` course, lesson, enrollment or assessment entities** — it models chats and knowledge. 🟢 **Its `ar-MA` + `fr-FR` locales make it the Maghreb-facing option** |
| 🟡 [`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai) | assessment + content pipeline | 🟢 `MIT`, `1 067` B | 🟡 **APPLIANCE+** | 🔴 none | 🆕 🟢 **The audit shape is REAL, not named**: `agent_tool_receipts` and `assessment_policy_versions` both have write sites, a status state machine, version-checked concurrency and an `ON DELETE RESTRICT` policy FK. 🟢 **Borrow the schema even if you do not deploy the app** |
| 🔴 [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | AI tutor | 🟢 `Apache-2.0`, `11 408` B | 🟡 **APPLIANCE** | 🔴 none | 🟡 `69` tables of real learning state. 🔴 **No `users` table: identity is a JSON file plus an optional PocketBase proxy** |
| 🆕 🔴 [`frappe/lms`](https://github.com/frappe/lms) | full LMS *(Frappe/Python)* | 🔴 **`AGPL-3.0`**, **`33 893` B** | 🔴 **integrate-only** | 🟡 not measured | 🔴 **A `2026` roundup lists this as the `MIT` LMS. Its own `license.txt` is the GNU Affero GPL v3.** 🔵 A hosted AI layer that links into it inherits the network-copyleft obligation — the same conversation as Open edX, not the easy one the roundup implies |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | full LMS | `GPL-3.0`, `35 147` B | 🟡 integrate-only | 🟢 full `LTI`/`SCORM`/`QTI` | 🟡 The default institutional incumbent. Plugin-shaped AI work is normal; a closed fork is not |
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | LMS / collaboration | 🟡 `ECL-2.0`, `11 120` B | 🟡 integrate-only | 🟢 `LTI`, `QTI` | 🟡 Permissive in practice, 🔴 **but the patent grant is scoped to educational use — read it before a commercial resale** |
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | MOOC / LMS | `AGPL-3.0`, `35 136` B | 🔴 integrate-only | 🟢 full | 🔴 Network copyleft: a hosted AI layer that links into it inherits the obligation |

### 🔴 The SIS layer — a gap a studio should price, not shop for

🆕 🔴 **This pass looked for a permissive student-information system and found none.** The only
SIS platforms surfaced are **`RosarioSIS`** and **`Gibbon`**, both `GPL`, both PHP, both K-12.
🔵 **There appears to be no MIT/Apache/BSD SIS. For an engagement that means the student record
system is either an integration against the client's incumbent, a copyleft deployment, or
bespoke — and that should be a line item from the first estimate, not a discovery.**

### 🔵 A standing note on licence columns

🆕 🔴 **`frappe/lms` is the second time in three passes that a published capability or licence
claim has not survived a read** *(`mentingo`'s `xAPI` was the first)*. 🟢 **Every licence in the
table above is a file read from a clone and sized in bytes. 🔵 When this KB cannot verify one, it
says so rather than copying a column.**


## Pass 181 — 2026-10-13

🆕 🟢 **The routing table gains TWO permissive routes and loses a feature it had been crediting to a
row for three passes.** 🟢 **[`Selleo/mentingo`](https://github.com/Selleo/mentingo) was finally
read past its `MIT` licence (`ACTION LH`) and is ROUTE-grade — 🔴 **but its `xAPI` and `LTI` support
do not exist**, and this KB had been publishing them since p178.

🆕 🟢 **The second new route is the one a studio should hear about first:**
[`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) *(`MIT`, `44`★)* is the
only row on this shelf that is **multi-tenant out of the box** — `tenant_id` resolved in three Go
auth handlers, an `Institution` selector in its own login template, and `cohorts`,
`cohort_trainers`, `cohort_statistics`, `account_tokens`, `audit_events` and
`billing_provider_events` among `240` `CREATE TABLE` statements.

### 🟢 The platform table, re-graded

🔵 **Grades: ROUTE** *(owns its data + its own auth + speaks a standard, or is multi-tenant — build
the engagement on it)*, **APPLIANCE** *(owns its data, deploys cleanly, no usable identity — one
learner or one cohort per deployment)*, **COMPONENT** *(neither — compose it into something else)*,
**integrate-only** *(copyleft reach makes a fork or hosted derivative a legal conversation)*.

| platform | layer | licence *(payload-verified)* | grade | standards, MEASURED | what it means for an engagement |
|---|---|---|---|---|---|
| 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | full LMS | 🟢 **`Apache-2.0`**, `10 982` B | 🟢 **ROUTE** | 🟢 `LTI 1.3` `252` files, `QTI` `1 201`, `SCORM` `355`, `OpenBadges` `263` | 🟢 **START HERE for a permissive full-LMS engagement.** `440` `@Entity`, own `Shibboleth`/`LDAP` auth, `openai` already in `33` files. 🆕 🔴 **Budget the discovery honestly: `385` tables in the shipped PostgreSQL schema and `186` Maven dependencies** |
| 🆕 🟢 [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | multi-tenant tutoring + assessment | 🟢 `MIT`, `1 073` B | 🟢 **ROUTE — the MULTI-TENANT one** | 🟡 `MCP` server; 🔴 **no `LTI`, no `SCORM`, no `QTI`** | 🟢 **START HERE when the client sells to MANY institutions.** Tenancy, cohorts, billing events and an audit trail are already modelled. 🔴 You bring the standards layer |
| 🆕 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | LMS *(TypeScript)* | 🟢 `MIT`, `1 062` B, `md5 88f104b7644947b4a8b6e71f4972c02f` | 🟢 **ROUTE** *(promoted from PLATFORM-unread)* | 🟢 **`SCORM 1.2` BOTH WAYS** *(own generator + runtime player packages; `imsmanifest.xml` fixtures; import e2e spec)*; 🔴 **`xAPI` `0`, `LTI` `0`** | 🟢 **START HERE for a JS/TS studio.** `123` `pgTable`, `tenant` in `305` files, `pnpm` workspaces, `docker-compose`. 🔴 **It cannot receive an `LTI` launch — so it does not plug into a university; it replaces one** |
| 🆕 🟢 [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | automated grading | 🟢 `Apache-2.0`, `10 785` B | 🟢 **ROUTE** *(institutional)* | 🟡 own checker protocol; 🔴 no `LTI`/`SCORM` measured | 🟢 **A working university grading system with a SEPARATE `fbs-identity-service` and `Keycloak`/`auth0` federation** — the deployment shape an institution's IT will recognise. Kotlin/Spring + Angular |
| 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | interactive learning **+ assessment** | 🟢 `MIT`, `1 091` B | 🟢 **ROUTE** | 🟢 `LTI 1.3` with grade passback, nightly Moodle interop test | 🟢 The assessment specialist: `257` entities, `528` write endpoints, `passkey` `136` files. 🔵 **Pair with `OpenOLAT` rather than choosing** |
| 🟢 [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | AI tutor platform | 🟢 `MIT`, `1 068` B | 🟢 ROUTE | 🔴 none | 🟢 The smallest route a studio can hold in its head: `34` tables, `141` endpoints, `10+` LLM providers, local-first |
| 🆕 🟡 [`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai) | assessment + content pipeline | 🟢 `MIT`, `1 067` B | 🟡 **APPLIANCE+** | 🔴 none | 🟡 **`84` tables with `assessment_policy_versions`, `content_schema_versions` and `agent_tool_receipts`.** 🟢 **The audit shape is the asset here** — borrow the schema even if you do not deploy the app |
| 🔴 [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | AI tutor | 🟢 `Apache-2.0`, `11 408` B | 🟡 **APPLIANCE** | 🔴 none | 🟡 `69` tables of real learning state. 🔴 **No `users` table: identity is a JSON file plus an optional PocketBase proxy. One deployment per cohort, or you add the identity layer** |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | full LMS | `GPL-3.0`, `35 147` B | 🟡 integrate-only | 🟢 full `LTI`/`SCORM`/`QTI` | 🟡 The default institutional incumbent. Plugin-shaped AI work is normal; a closed fork is not |
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | LMS / collaboration | 🟡 `ECL-2.0`, `11 120` B | 🟡 integrate-only | 🟢 `LTI`, `QTI` | 🟡 Permissive in practice, 🔴 **but the patent grant is scoped to educational use — read it before a commercial resale** |
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | MOOC / LMS | `AGPL-3.0`, `35 136` B | 🔴 integrate-only | 🟢 full | 🔴 Network copyleft: a hosted AI layer that links into it inherits the obligation |
| 🔴 [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | full LMS | `AGPL-3.0`, `34 520` B | 🔴 integrate-only | 🟢 full | 🔴 Same reach. Integrate over `LTI`, never fork |

🟢 **`6` of the `17` routing rows are now CODE-verified, up from `4` at p180.**

### 🆕 🔴 The standards gap, now the sharpest thing in this table

🔴 **Every permissive route this KB has found is missing the interoperability layer, and the two are
almost mutually exclusive:**

| | speaks `LTI 1.3` | does NOT |
|---|---|---|
| 🟢 **permissive** | 🟢 `OpenOLAT` *(Apache-2.0, Java, `385` tables)*, `Artemis` *(MIT, Java)* | 🟢 `tutor-mcp` *(Go, multi-tenant)*, `mentingo` *(TS, `SCORM` only)*, `OpenTutor`, `feedbacksystem`, `civil-ai`, `DeepTutor` |
| 🔴 **copyleft** | 🔴 `Moodle`, `Open edX`, `Canvas`, `Chamilo`, `ILIAS` | — |

🔵 **`T305`: a studio choosing a permissive education route in a language that is NOT Java is
choosing a system that cannot receive an `LTI` launch. The `LTI` layer is then the engagement's
first build, not an integration task — and it is the single most reusable asset a studio could
carry between education clients.**

🆕 🟢 **The one bridge that exists is `SCORM`, and `mentingo` holds both ends of it.** It generates
`SCORM 1.2` packages *(`manifest-builder.ts`, `package-builder.ts`, a standalone browser runtime
player)* and imports them *(`scorm.service.ts`, tenant-scoped storage prefixes, real
`imsmanifest.xml` fixtures)*. 🔵 **So content can move permissively between a `mentingo` deployment
and any `SCORM`-speaking incumbent, including `Moodle`, without touching the incumbent's copyleft
code.**

### 🔴 The wider LMS market, from prose search — and what it did not yield

🟡 **A dedicated search for a permissively licensed `Moodle` alternative returned no MIT-licensed
full LMS at all.** 🟢 **It confirms `OpenOLAT` as the Apache-2.0 option** *(upstream stable `20.3.4`,
June `2026`; this KB reads `21.2-SNAPSHOT` at `HEAD 8494a140b2ca`)*, 🟡 **names `Sakai` as
`ECL-2.0`**, and 🔴 **reports `formalms/formalms` as `Apache-2.0` in one listing and `GPL` in
another — unresolved, and still unprobed here for a third pass.** 🔵 **Searching for licences
produces disagreement; reading payloads produces answers. This KB keeps doing the second.**

## Pass 180 — 2026-10-13

🆕 🟢 **The routing recommendation CHANGES this pass, and for the first time it changes in the
client's favour: there is now a permissive platform to start FROM, rather than a copyleft platform
to integrate AROUND.** 🟢 **[`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) was read
past its `Apache-2.0` licence (`ACTION LE`, limb `1` fired) and it owns its data, carries its own
federated auth and speaks four education standards.**

### 🟢 The platform table, with the routing grade each row actually earns

🔵 **Grades: ROUTE** *(owns its data + its own auth + speaks a standard — build the engagement on
it)*, **APPLIANCE** *(owns its data, deploys cleanly, no user — one learner per deployment)*,
**COMPONENT** *(neither — compose it into something else)*.

| platform | layer | licence *(payload-verified)* | bytes | grade | what it means for an engagement |
|---|---|---|---|---|---|
| 🆕 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | full LMS | 🟢 **`Apache-2.0`** | `10 982` | 🟢 **ROUTE** | 🟢 **START HERE for a permissive full-LMS engagement.** `440` `@Entity`, `419` `@Table`, `497` DAO/Manager classes, `199` schema files, Oracle+PostgreSQL+MySQL. Own auth incl. `Shibboleth` (`147` files) and `LDAP` (`158`). `LTI 1.3` (`252` files), `QTI` (`1 201`), `SCORM` (`355`), `OpenBadges` (`263`). 🟢 **`openai` already in `33` files and `ollama` in `13` — the AI extension point exists upstream.** A closed derivative, a white-label deployment and a proprietary AI layer are all available without a copyleft conversation |
| 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | interactive learning **+ assessment** | 🟢 `MIT` | `1 091` | 🟢 **ROUTE** | 🟢 The assessment specialist: `257` entities, `528` write endpoints, own auth (`passkey` `136` files, `saml2` `54`), `LTI 1.3` with grade passback and a nightly Moodle interop test. 🔵 **Pair it with `OpenOLAT` rather than choosing between them** |
| 🆕 🟢 [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | AI tutor platform | 🟢 `MIT` | `1 068` | 🟢 **ROUTE** *(promoted)* | 🟢 **The APAC-origin route, and the smallest one a studio can actually hold in its head**: `34` tables, `141` endpoints, `jose` access+refresh tokens, `bcrypt`, `alembic` migrations, `Dockerfile`, `user_id` in `202` files. `10+` LLM providers, local-first |
| 🟡 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | LMS *(commercial OSS)* | 🟢 `MIT` | `1 062` | 🟡 PLATFORM *(not read past its licence)* | 🟡 **Still the only shelf row that DECLARES both `scorm` and `xapi`**, and it ships a licence gate (`T208`). 🔴 Carried unread for a fourth pass — a candidate for p181 |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | full LMS | `GPL-3.0` *(`COPYING.txt`, `md5 d32239bcb673463ab874e80d47fae504`)* | `35 147` | 🟡 integrate-only | 🟡 The default institutional incumbent. Plugin-shaped AI work is normal; a closed fork is not |
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | MOOC / LMS | `AGPL-3.0` | `35 136` | 🔴 integrate-only | 🔴 Network copyleft: a hosted AI layer that links into it inherits the obligation |
| 🔴 [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | full LMS | `AGPL-3.0` | `34 520` | 🔴 integrate-only | 🔴 Same reach. Integrate over `LTI`, never fork |
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | LMS / collaboration | 🟡 `ECL-2.0` | `11 120` | 🟡 integrate-only | 🟡 Permissive in practice, but the patent grant is scoped to educational use — read it before a commercial resale |
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **ERP + LMS + SIS** *(Odoo)* | `LGPL-3.0` | `8 241` | 🟡 ERP route | 🟡 The one integrated LMS+SIS+fees route. `LGPL` permits a separately licensed AI module beside it, which is the natural shape |
| 🟡 [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | school management / SIS | 🟢 **`GPL-3.0`** *(🆕 `P214-1`: was `AGPL-3.0`)* | `35 121` | 🟡 **fork-and-host is open** | 🟢 **File copyleft, not network** — the hosted-deployment question this row raised for 4 cells does not arise |
| 🟡 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | SIS *(K-12)* | `GPL` | `15 214` | 🟡 on-prem | 🟡 Classic copyleft; on-premise deployments are the comfortable case |
| 🔴 [`frappe/education`](https://github.com/frappe/education) | school ERP *(Frappe)* | 🔴 **`19`-byte assertion, `md5 2884e131cfab2111873ff0eb5ba55997`** | **`19`** | 🔴 **DO NOT RELY** | 🔴 **There is no grant text in the file — only the string `License: GNU GPL V3`.** Intended `GPL-3.0`; treat as unverified until upstream ships the body |
| 🟡 [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | single-learner study app | 🟢 `MIT` | `1 069` | 🟡 **APPLIANCE** | 🟡 `7` tables, `16` write endpoints, `docker-compose` with a healthcheck. 🔴 **No user, no auth, no tenant — one learner per deployment** |
| 🟡 [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | spaced-repetition bridge *(`MCP`)* | 🟢 `MIT` | `1 074` | 🟡 **COMPONENT** | 🟡 The shelf's only `MCP` server. Identity is **BORROWED** — its `auth` files are `MCP` client credentials, not learners |
| 🔴 [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | multi-host skill adapter | 🟢 `MIT` | `1 064` | 🔴 **COMPONENT** | 🔴 `0` databases, `0` servers. `199` files whose job is to run one skill set inside four vendor runtimes |
| 🔴 [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) | exam-prep skill pack | 🟢 `MIT` | `1 065` | 🔴 **COMPONENT** | 🔴 `auth` `0`, no ORM, no server. Declares `anti-hallucination` and page citations — relevant to Article `50(2)` provenance work |
| 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | academic integrity | 🟢 `MIT` | `1 084` | 🟢 **COMPONENT, CALIBRATED** | 🟢 Executed at p179: threshold belongs near `0.85`; `0.7` sits `0.028` above the honest-work band |

### 🟢 The routing consequence, stated plainly

🟢 **`4` of this table's `17` rows are now code-verified** — `OpenOLAT`, `Artemis`, `OpenTutor` and
`dolos` — 🟢 **up from `3` at p179, and the new one is the largest and the only `Apache-2.0`
platform.**

🆕 🟢 **The recommendation a Globant engagement should hear, in one line:** 🟢 **build on
`OpenOLAT` (`Apache-2.0`, owns the data, owns the auth, speaks `LTI 1.3`), attach `Artemis` over
`LTI 1.3` where assessment matters, gate submissions with `dolos` at `0.85`, and treat
`Bloom`/`Study-Mate`/`examprep` as parts to harvest rather than products to deploy.**

🔴 **The honest caveat on that line:** 🔴 **`OpenOLAT` is `2.6` million lines of Java with a
`pom.xml`. It was READ this pass, not BUILT or RUN.** 🔵 **`T294`: *"owns its data"* is a static
property and this KB proved it statically; *"deploys in a week"* is an operational claim and
nothing here supports it yet.** 🟢 **Pre-registered as `ACTION LG`.**

🆕 🟡 **One vocabulary note that matters for the compiler:** 🟡 **`Selleo/mentingo` has been carried
as grade *"PLATFORM (off-vocabulary)"* for four passes.** 🔵 **It is off-vocabulary because it has
never been read past its licence, not because it resists the vocabulary. Reading it is the cheapest
way to resolve a stale grade on this page.**

## Pass 179 — 2026-10-13

🆕 🟢 **The platform table gets the column it has always needed and never had: the licence as READ
from the payload, with bytes and an `md5`, on a channel this pass repaired.** Eight platforms
re-read. 🔵 **Three verdicts in this table changed, and one of them changes which platform a
Globant engagement should start from.**

| platform | layer | licence *(payload-verified)* | bytes | what it means for an engagement |
|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | LMS | 🟢 **`Apache-2.0`** | `10 982` | 🟢 **THE permissive LMS of this set, and the only one.** A closed derivative, a white-labelled deployment and a proprietary AI layer are all available without a copyleft conversation |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | LMS / collaboration | 🟡 **`ECL-2.0`** *(settles the `Apache-2.0` vs `ECL-2.0` conflict)* | `11 120` | 🟡 Permissive in practice, but the patent grant is scoped to educational use — read it before a commercial resale |
| [`moodle/moodle`](https://github.com/moodle/moodle) | LMS | `GPL-3.0` *(at `COPYING.txt`)* | `35 147` | 🟡 The default institutional incumbent. Plugin-shaped AI work is normal here; a closed fork is not |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | MOOC / LMS | `AGPL-3.0` | `35 136` | 🔴 Network copyleft. A hosted AI layer that links into it inherits the obligation |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | LMS | `AGPL-3.0` | `34 520` | 🔴 Same reach. Integrate over `LTI`, do not fork |
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | interactive learning **+ assessment** | 🟢 `MIT`, `1 091` B | `1 091` | 🟢 **Still the strongest route in this table** *(p178)*: `257` entities, `528` write endpoints, its own auth, `LTI 1.3` with grade passback |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | school management / SIS | 🟢 **`GPL-3.0`** *(🆕 `P214-1`: **the secondary sources were right and this cell was wrong** — `LICENSE` title, `composer.json` and `README` all say `GPL-3.0`)* | `35 121` | 🟢 **File copyleft** — fork and host without source disclosure |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | SIS *(K-12)* | `GPL` | `15 214` | 🟡 Classic copyleft; on-premise deployments are the comfortable case |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | ERP + LMS + SIS *(Odoo)* | `LGPL-3.0` | `8 241` | 🟡 The one integrated LMS+SIS route. `LGPL` permits a separately licensed module alongside it, which is the natural AI shape |
| [`frappe/education`](https://github.com/frappe/education) | school ERP *(Frappe)* | 🔴 **`19`-byte ASSERTION: `License: GNU GPL V3`** | **`19`** | 🔴 **The grant was NOT read because there is no grant in the file.** Intended as `GPL-3.0`; treat as unverified until upstream ships the text |

### 🟢 The routing consequence, stated plainly

🟢 **`3` of this table's rows are code-verified** — `Artemis`, `dolos` and now the appliance row
below — and that denominator is unchanged from p178 because this pass verified LICENCES broadly
rather than one platform deeply.

🆕 🟢 **For a client who needs a permissive LMS base, the answer changed this pass: it is
`OpenOLAT`, on `Apache-2.0`, confirmed at `10 982` B.** 🔵 **Every other full LMS in this set is
copyleft, and two of the three biggest are AFFERO copyleft — which for a hosted AI layer is the
difference between an integration and a disclosure obligation.** 🟡 **`OpenOLAT` has NOT been read
past its licence, so it is a LICENCE verdict and not yet a route (`ACTION LE`).**

### 🆕 🟡 A new shelf row, and a new grade below "route": the APPLIANCE

🟡 **[`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom)** — `MIT`, `1 069` B,
`md5 d3ac8ed0a50bd8de7d9c2ad5be4248ab`, `HEAD b3918981bb34` — owns its data (`7` tables), writes
to it (`16` write endpoints), and deploys in one command (`docker-compose`, `2` `Dockerfile`s,
healthcheck, named volume). 🔴 **And it has no user: `auth` `0`, `login` `0`, `jwt` `0`,
`oauth` `0`, `password` `0`, `users` `0`, `tenant` `0`, and no `User` entity.**

🔵 **So this table now needs three grades, not two:**

| grade | test | example |
|---|---|---|
| **ROUTE** | owns its data, has its own auth, speaks a standard | 🟢 `Artemis` *(`LTI 1.3` + AGS, `passkey`, `saml2`)* |
| 🆕 **APPLIANCE** | owns its data, deploys cleanly, **but has no user and no tenant** | 🟡 `Bloom` — one learner per deployment |
| **COMPONENT** | neither; it is a library or a plugin inside someone else's runtime | 🔴 `Study-Mate` *(adapters for `4` vendor runtimes, `0` databases)* |

🔴 **An appliance cannot hold a cohort, and that is the whole cost line: taking `Bloom` to a
class of `30` means building the user, the tenant and the enrolment model that `Artemis` already
has.** 🔴 **Its `pyproject.toml` declares `python-jose`, `bcrypt`, `email-validator` and
`python-multipart` with `0` import sites each — so a reader who scopes the auth work from the
manifest will scope it at zero and be wrong (`T285`).**

### 🔴 Declared, so the table is not read as more verified than it is

- 🟢 **`formalms/formalms` is RESOLVED — `GPL-2.0` at `html/license.txt`** *(`18 346` B, p215)*. <!--corrected-->
  🔴 **`apereo/opencast` is still UNRESOLVED, not absent:** `404` on
  `LICENSE` at `HEAD`, and a `404` on one filename is an unprobed name, not a measured absence.
- 🔴 **`moodle/moodle` was published `NO-LICENCE-FILE` by this KB's own probe** until
  `COPYING.txt` was tried by hand. The probe lists disagree about that filename (`gap 135`).
- 🔴 **No platform in this table was deployed this pass.** `Bloom` could not even have its test
  suite run, because PyPI is unreachable from this environment (`gap 139`).


## Pass 178 — 2026-10-13

🆕 🟢 **The platform row stops being a candidate, and it is the strongest route in this table.**
`ACTION KT` read [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) past its grant:
`13 810` files, `257` `@Entity` classes, `137` Liquibase changelogs, `528` write endpoints across
exercise, exam and assessment, its own auth *(`passkey` in `136` files, `saml2` in `54`)*, and
**`LTI 1.3` with Deep Linking AND Assignment-and-Grade-Services, tested nightly against Moodle in
CI.** 🔵 **Fifteen passes of *"no permissive institutional platform"* end here.**
🆕 🟢 **Three code-verified routes out of `22`, and this one is the first PLATFORM among them.**
`canvasapi` (p176) is a client, `dolos` (p177) is a tool, `Artemis` is a system of record.
🆕 🔵 **The pairing this table has been circling for three passes is now explicit, and it is an
ARCHITECTURAL pairing rather than a feature list:** `dolos` ranks pairs and returns NO verdict;
`Artemis` grades, scores and adjudicates by design. 🔴 **Routing them together means routing one
Annex III high-risk system and one deliberately non-adjudicating tool, and the compliance work
attaches to exactly one of them — see [`intel/trends.md`](../intel/trends.md).**
🆕 🔴 **The condition that will decide an `Artemis` engagement's budget is not the licence, it is
the standard count: ONE.** `LTI` in `248` files; `SCORM` `0`, `xAPI` `0`, `QTI` `0`, `OneRoster`
`0`, `Ed-Fi` `0`, `Caliper` `0`. 🟢 **So `Artemis` + `mentingo` is not a redundant pair: `mentingo`
is still the only row here DECLARING `scorm` and `xapi`, and `Artemis` is the only row speaking
`LTI 1.3` with grade passback.**
🆕 🔴 **And a new dependency row, admitted because the AI path cannot be quoted without it:**
[`ls1intum/Pyris`](https://github.com/ls1intum/Pyris), `MIT`, **`12`★**. 🟢 **Measured mitigation
from `Artemis`'s own admin doc: the authoring half (`Hyperion`) needs Spring AI and an LLM endpoint,
NOT `Pyris`; `Pyris` is required only for semantic lecture search and quiz generation falls back
without it.**
🟢 **The routing table RE-STATES EVERY ROW, per `P170-C`/`T216`: under *"only the newest block is
canonical"* a row not re-stated is lost however true it remains below.**

### 🟢 THE ROUTING TABLE — re-stated in full at p178

| need | route | licence *(body read)* | status at p178 |
|---|---|---|---|
| 🟢 **LMS, permissive — institutional** | [**OpenOLAT**](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** *(§`1`–`9` verbatim, `10 982` B)* | 🟢 **CARRIED unchanged. `QTI`, `SCORM`, curriculum and assessment built in. Carry the `2` attribution statements** |
| 🟢 **LMS, permissive — offline / low-connectivity** | [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The LATAM, APAC low-bandwidth and Africa row. 🟡 Its PLACEMENT evidence stays downgraded (`ACTION KK`): the artefact names *"Learning Equality"* and no country** |
| 🟡 **LMS, permissive — Java institutional, patent limb** | [**Sakai**](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** *(root)* | 🟡 **CARRIED WITH THE SAME THREE FLAGS. Narrowed patent grant (`T200`); fails `mentingo`'s own licence gate (`T208`); `8` of `86` `licenses/` paths are NOT open-source grants; `25` of `86` are `Apache-1.1`, so clause `3` attribution is owed (`ACTION JU`)** |
| 🟢 **LMS, permissive — AI-native / corporate L&D** | [**Selleo/mentingo**](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** *(`1 062` B — EXACT; its licence carries no trailing `LF`)* | 🟢 **CARRIED, EMEA. `SCORM` import AND export, ships `licenses.config.yaml`, the gate to LIFT. 🆕 Still the only row in this KB DECLARING both `scorm` and `xapi` — which is now a COMPLEMENT to `Artemis` rather than an alternative to it** |
| 🆕 🟢 **LMS / exercise + exam platform, permissive — university-OWNED, AI-native, `LTI 1.3`** | 🟢 [**ls1intum/Artemis**](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** *(`1 091` B, `md5 021aaec73f7b974dc5edf4ef703f941b`, identical on `main` and `develop`; *"© 2026 TUM Applied Education Technologies"*)* | 🆕 🟢 **PROMOTED from CANDIDATE to verified ROUTE, EMEA, HOLDER-GRADE. `develop@8c158741c38e`, `v10.3`, `818`★. `ACTION KT`: `257` JPA entities, `137` migrations, `528` write endpoints, own auth, `LTI 1.3` + Deep Linking + AGS, nightly Moodle interop test, `Iris`/`Hyperion`/`Athena` AI modules, compose-deployable, `proctor`/`webcam`/`emotion` all `0`. 🔴 **CONDITIONS:** it ADJUDICATES (Annex III); ONE standard only; `FERPA` `0`; AI default provider is OpenAI/Azure** |
| 🆕 🟡 **LLM microservice for `Artemis` — semantic lecture search** | 🟡 [**ls1intum/Pyris**](https://github.com/ls1intum/Pyris) | 🟢 **`MIT`** *(`1 089` B, `md5 5cc3b9844f092545a99800eb9edce880`)* | 🆕 🟡 **ADMITTED as a DEPENDENCY, not a product, EMEA. `HEAD` `d7b2c095204e`, 🔴 **`12`★, `16` open issues, last push `2026-09-17`**. `ollama` + `weaviate` + `langchain`. 🟢 NOT required for `Hyperion` authoring — only for lecture search** |
| 🟢 **Assessment integrity — plagiarism detection, permissive** | 🟢 [**dodona-edu/dolos**](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** *(`1 084` B; `md5 00ffc342d555c4129ee54e3286818d50`; *"© 2019 Team Dolos <dolos@ugent.be>"*)* | 🟢 **CARRIED as verified ROUTE, EMEA. `HEAD` `44925b867ce7`, unmoved for a third pass. `20` languages / `19` vendored grammars (docs claim `11`); false positives handled by `-i` plus `-m`/`-M`; `defaultMinSimilarity = 0`; the only threshold is GUESSED in the report UI. 🔴 CONDITIONS: `0` LMS integration, `0` interop standards, NO verdict — decision support only. 🆕 🔵 Its `0` LMS integration is now priced: `Artemis` is the row that HAS one** |
| 🟢 **Rostering, permissive — standards-native, READ-ONLY** | [**Ed-Fi-Alliance-OSS/edfi-oneroster**](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`** *(`10 173` B)* | 🟢 **CARRIED unchanged. `OneRoster 1.2`, `24` GETs over `12` entities, `0` write routes. Still the only STANDARDS-native permissive rostering route here — and `Artemis` does NOT change that: `OneRoster` `0`, `Ed-Fi` `0`** |
| 🟢 **Rostering, permissive — Canvas-native, READ AND WRITE** | 🟢 [**ucfopen/canvasapi**](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** *(`1 130` B — EXACT, `md5 37cd0f92…`)* | 🟢 **CARRIED as verified ROUTE, North America. `HEAD` `513588f3077f` on `master`, `682`★. `enrollments`, `sections`, `enrollment_terms` READ AND WRITE; `Bearer` auth; `per_page=100`; `10` typed exceptions; `1 112` test methods. 🔴 CONDITIONS: `0` standards interop, and a client for an `AGPL-3.0` core. 🟡 Last commit `2026-04-16` — `180` d, AT the liveness bar** |
| 🟢 **Portable credentials — Open Badges `3.0` authoring** | [**opensalt/OB3DefinitionWidget**](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **`MIT`** *(`1 080` B — 🆕 CONFIRMED EXACT by `ACTION KU`)* | 🟢 **CARRIED unchanged. Pair with `OpenOLAT`'s `OB2` module — which is `2.0` ONLY, no W3C VC** |
| 🟢 **SCORM / AICC / xAPI interop** | [**jcputney/scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The only row where grant-named paths and grant bodies agree exactly. 🆕 🔵 The row that fills `Artemis`'s `SCORM` `0` and `xAPI` `0`** |
| 🟡 **Assessment / exam generation, permissive** | 🟡 [**niansia/taiwan-exam**](https://github.com/niansia/taiwan-exam) *(`MIT`, APAC)* or 🟡 [**jeliael/fakao-ai-exam-engine**](https://github.com/jeliael/fakao-ai-exam-engine) *(`MIT`, APAC)* | 🟡 **`MIT` root, with a dependency caveat** | 🟡 **CARRIED as CANDIDATE, not production. `taiwan-exam` depends on **`PyMuPDF`, `AGPL-3.0`-or-Artifex-commercial**, so the `MIT` root does not reach the closure (`ACTION JR`). Swap for `pypdf` — already in the same `requirements.txt` — or buy the commercial limb BEFORE routing. 🆕 Both re-confirmed at `18`★ and `10`★ in p178's census. 🆕 🔵 `Artemis`'s `Hyperion` generates VERIFIED quiz variants in-platform, which is the institutional alternative to both** |
| 🔴 **Education ERP / SIS** | [**openeducat_erp**](https://github.com/openeducat/openeducat_erp) *(`LGPL-3.0`)* on [**odoo/odoo**](https://github.com/odoo/odoo) *(`LGPL-3.0`)*, or [**frappe/erpnext**](https://github.com/frappe/erpnext) *(`GPL-3.0`)* | 🔴 **copyleft — no permissive option exists** | 🔴 **CARRIED, SIXTEENTH pass with no `MIT`/`Apache` education ERP. Its vendor-stated OneRoster / Ed-Fi / LTI 1.3 support is ABSENT from the open tree (`T162`)** |
| 🔴 **Full-stack MOOC platform** | [**openedx/edx-platform**](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | 🟢 **CARRIED unchanged. The RPC carve-out is a LICENSOR statement, not counsel (`gap 107`) — flag it as such in any deck** |
| 🔴 **LMS, mass-market copyleft** | [**moodle/moodle**](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** *(at `COPYING.txt`, not `LICENSE`)* | 🟢 **CARRIED unchanged. `88` grant documents, corrected down from `193` — `105` were PHP source files (`T223`). 🆕 🟢 And as of p178 it is also the LMS `Artemis` is nightly-tested against, which makes a Moodle-plus-Artemis topology the best-evidenced hybrid in this table** |
| 🔴 **LMS, plain copyleft — second option** | [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`GPL-3.0`** | 🟢 **CARRIED unchanged. The cleanest inner grant surface of any copyleft LMS here — `2` bodies against `Moodle`'s `88`. Strong built-in exam/assessment tooling** |
| 🟡 **SIS, active** | [**RosarioSIS**](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** | 🟢 **CARRIED unchanged. Still the most active SIS this KB holds** |
| 🟡 **SIS, active** | [**openSIS-Classic**](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** *(NOT at the root)* | 🟢 **CARRIED. `ACTION KJ` probed `16` paths including every British spelling and `COPYING.md` — `0` of `16`; its `GPL-2.0` is at `docs/License.txt`** |
| 🔴 **SIS, PERMISSIVE and institutional-scale** | 🔴 **none** | — | 🔴 **CARRIED, SIXTEENTH pass. `ACTION KE` refuted the one candidate at p175 (`eagles-edu/sis` is a portal: `0` interop tokens at word-boundary precision). 🆕 🔵 `Artemis` does NOT fill this row and must not be sold as filling it: it owns exercises, exams and assessments, not enrolment, fees or guardians** |
| 🟡 **SIS, permissive — remaining candidates** | 🟡 [**opensacorg/learning-blocks**](https://github.com/opensacorg/learning-blocks) *(`849` files, **Code for Sacramento**)* · [**Arux-Software/Bright**](https://github.com/Arux-Software/Bright) *(toolkit, not a system of record)* | 🟢 **both `MIT`** — bodies read at p174 | 🟡 **CARRIED as CANDIDATES. NEITHER has been probed the way `ACTION KE` probed the third one. 🔴 Do not quote either as rostering-capable. 🆕 🟢 Their byte counts are no longer suspect — `ACTION KU` measured both: `1 076` B each, **CORRECTED** from `1 075`** |
| 🔴 **LMS, corporate training** | [**Forma LMS**](https://github.com/formalms/formalms) | 🔴 **`GPL-2.0`** *(at `html/license.txt`; NO root grant)* | 🔴 **CARRIED as REFUTED, probe-complete. A secondary source calls it *"Apache 2.0"*; its body is the GNU `GPL` v`2` verbatim, shipped in `9` languages with nothing naming which governs (`gap 116`)** |
| 🔵 **Learning-record plumbing** | 🔴 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | 🟢 `Apache-2.0` *(`11 357` B)* | 🔵 **DELIBERATELY NOT ROUTED, eighth pass. Last commit `2026-02-26`, `Django<4.0` (EOL April `2024`), `0` matches for `xapi`/`caliper`/`statement`. Vendor the idea, do not ship the package** |
| 🔴 **THREAT MODEL — not a dependency** | 🔴 [**sgaofen/vibe-schooling**](https://github.com/sgaofen/vibe-schooling) | 🟢 **`MIT`** *(`1 064` B, *"© 2026 sgaofen"*)* | 🔴 **CARRIED as an ATTACK SURFACE, per `P171-D`. `HEAD` `7c2f87a4641b`, `56` files, `80`★ — UNMOVED in stars for a second pass. Canvas named `19`×, topics `canvas-lms` + `exam-automation`. 🔵 Any Canvas engagement that routes `canvasapi` should assume this exists on the student side** |

🟢 **The tally, counted by ROW rather than by summing buckets.**
**`24` rows: `13` permissive and routable** *(OpenOLAT, Kolibri, mentingo, **Artemis**, **Pyris**,
dolos, edfi-oneroster, canvasapi, OB3DefinitionWidget, scorm-again, plus the exam-generation pair as
ONE row and the SIS-candidate pair as ONE row)*, **`1` permissive-with-a-patent-limb** *(Sakai)*,
**`7` copyleft or non-permissive** *(education ERP, Open edX, Moodle, ILIAS, RosarioSIS,
openSIS-Classic, Forma LMS)*, **`1` declared EMPTY** *(permissive institutional SIS)*, **`1`
deliberately not routed** *(openlxp-xia)*, **`1` threat model** *(vibe-schooling)*.
🔵 **`13 + 1 + 7 + 1 + 1 + 1 = 24`, and the `24` is the row count, not a reconciliation of it.**
🆕 🟢 **Verified ROUTES promoted by reading code rather than a licence: `3` of `24`** — `canvasapi`
(p176), `dolos` (p177), `Artemis` (p178). 🔴 **That is the honest denominator for this table's
maturity, and it moved for the third pass running.**

### 🆕 🟢 The topology this table now supports, named once so a deck can reuse it

🔵 **An institution that wants permissive AI-assisted assessment can now be given a real answer
rather than a list:**
**`Moodle` or `OpenOLAT` as the LMS of record** → **`Artemis` as the exercise and exam platform**,
wired in as an `LTI 1.3` tool with Deep Linking and grades flowing back through AGS *(the limb that
is nightly-tested against Moodle)* → **`dolos` for integrity**, ranking pairs and refusing to
adjudicate → **`Hyperion` inside `Artemis` for authoring**, needing only an LLM endpoint →
**`scorm-again` where SCORM or xAPI is contractually required**, because `Artemis` declares neither.
🔴 **And the four conditions carried verbatim into the deck: `Artemis` adjudicates and is therefore
Annex III; it speaks one standard; it names `FERPA` nowhere; and its self-hosted AI limb rests on a
`12`★ microservice.** 🟢 **Concrete wiring, with the version pins, in
[`compose/patterns.md`](../compose/patterns.md).**

## Pass 177 — 2026-10-13

🆕 🟢 **The assessment-integrity row stops being a candidate.** `ACTION KQ` read
[`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) past its grant at the `HEAD` this KB
recorded at p175: `20` programming languages in the registry against `11` in its own docs, `19`
vendored `tree-sitter` grammars, `513` files, `57` test files, `103` test declarations, and three
shipped controls for the false-positive problem its docs name in their own words.
🟢 **It is the second row in two passes promoted by reading code rather than a licence, and the
only defence this file holds against the threat-model row it admitted one pass ago.**
🔴 **Two conditions travel with it and neither is optional in a deck: it has NO LMS integration of
any kind — `Moodle` `0`, `webhook` `0`, and Canvas LMS `0` once the `29` `canvas` hits are read as
the HTML5 element they are — and it returns NO verdict.** 🔵 **The second is the feature. An
integrity tool that adjudicates a student is an Annex III decision system; one that ranks pairs for
a human is not, which is why this row survives contact with both the EU and the US statutes
([`intel/trends.md`](../intel/trends.md)).**
🆕 🔴 **And the arms race this file opened at p176 is now asymmetric in a MEASURED way, not a
rhetorical one.** The attack row automates a specific LMS from the student's browser; the defence
row has no LMS integration at all and no concept of a verdict. 🔵 **They do not meet, and the gap
between them is where the engagement's design work actually is.**
🆕 🔴 **`ACTION KS` corrects a licence byte count in `4` of this table's rows.** 🔵 **The figures
were never load-bearing for routing, but they were published as identity keys, and `8` of `12`
across this KB were short by exactly one byte.** 🟢 **Corrected inline and marked `CORRECTED`.**
🟢 **The routing table RE-STATES EVERY ROW, per `P170-C`/`T216`: under *"only the newest block is
canonical"* a row not re-stated is lost however true it remains below.**

### 🟢 THE ROUTING TABLE — re-stated in full at p177

| need | route | licence *(body read)* | status at p177 |
|---|---|---|---|
| 🟢 **LMS, permissive — institutional** | [**OpenOLAT**](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** *(§`1`–`9` verbatim, `10 982` B)* | 🟢 **CARRIED unchanged. `QTI`, `SCORM`, curriculum and assessment built in. Carry the `2` attribution statements** |
| 🟢 **LMS, permissive — offline / low-connectivity** | [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The LATAM, APAC low-bandwidth and Africa row. 🟡 Its PLACEMENT evidence stays downgraded (`ACTION KK`): the artefact names *"Learning Equality"* and no country** |
| 🟡 **LMS, permissive — Java institutional, patent limb** | [**Sakai**](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** *(root)* | 🟡 **CARRIED WITH THE SAME THREE FLAGS. Narrowed patent grant (`T200`); fails `mentingo`'s own licence gate (`T208`); `8` of `86` `licenses/` paths are NOT open-source grants; `25` of `86` are `Apache-1.1`, so clause `3` attribution is owed (`ACTION JU`)** |
| 🟢 **LMS, permissive — AI-native / corporate L&D** | [**Selleo/mentingo**](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** *(`1 062` B — 🆕 CONFIRMED EXACT by `ACTION KS`; its licence carries no trailing `LF`)* | 🟢 **CARRIED, EMEA. `SCORM` import AND export, ships `licenses.config.yaml`, the gate to LIFT. Still the only row in this KB DECLARING both `scorm` and `xapi`** |
| 🟡 **LMS, permissive — university-OWNED exercise + exam platform** | 🟡 [**ls1intum/Artemis**](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** *(🆕 **`1 091` B — CORRECTED** from `1 090`, *"© 2026 TUM Applied Education Technologies"*)* | 🟡 **CARRIED as CANDIDATE, EMEA, HOLDER-GRADE. `HEAD` `09266581a02c`, `818`★. 🔴 Now the LAST fully unverified holder-grade row in this KB — `gap 134`'s remainder, and the obvious subject for p178** |
| 🟢 **Assessment integrity — plagiarism detection, permissive** | 🟢 [**dodona-edu/dolos**](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** *(🆕 **`1 084` B — CORRECTED** from `1 083`; `md5 00ffc342d555c4129ee54e3286818d50`; *"© 2019 Team Dolos <dolos@ugent.be>"*)* | 🆕 🟢 **PROMOTED from CANDIDATE to verified ROUTE, EMEA. `HEAD` `44925b867ce7`, unmoved. `ACTION KQ`: `20` languages / `19` vendored grammars (docs claim `11`); `char` tokenizer also reaches `.txt`/`.md`; false positives handled by template exclusion (`-i`) plus auto-detection (`-m`, `-M`); `defaultMinSimilarity = 0`; the only threshold is GUESSED in the report UI. 🔴 **CONDITIONS:** `0` LMS integration, `0` interop standards, `0` of `FERPA`/`GDPR` named, and NO verdict — decision support only** |
| 🟢 **Rostering, permissive — standards-native, READ-ONLY** | [**Ed-Fi-Alliance-OSS/edfi-oneroster**](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`** *(`10 173` B)* | 🟢 **CARRIED unchanged. `OneRoster 1.2`, `24` GETs over `12` entities, `0` write routes. Still the only STANDARDS-native permissive rostering route here** |
| 🟢 **Rostering, permissive — Canvas-native, READ AND WRITE** | 🟢 [**ucfopen/canvasapi**](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** *(`1 130` B — 🆕 CONFIRMED EXACT, `md5 37cd0f92…` reproduced independently)* | 🟢 **CARRIED as ROUTE, North America. `HEAD` `513588f3077f`, `682`★. `enrollments`, `sections`, `enrollment_terms` with READ AND WRITE; `Bearer` auth; `per_page=100` pagination; `10` typed exceptions; `1 112` test methods. 🔴 CONDITIONS unchanged: `0` standards interop, and a client for an `AGPL-3.0` core. 🟡 Last commit `2026-04-16` — now `180` d, AT the liveness bar** |
| 🟢 **Portable credentials — Open Badges `3.0` authoring** | [**opensalt/OB3DefinitionWidget**](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **`MIT`** *(`1 080` B)* | 🟢 **CARRIED unchanged. Pair with `OpenOLAT`'s `OB2` module — which is `2.0` ONLY, no W3C VC** |
| 🟢 **SCORM / AICC / xAPI interop** | [**jcputney/scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The only row where grant-named paths and grant bodies agree exactly** |
| 🟡 **Assessment / exam generation, permissive** | 🟡 [**niansia/taiwan-exam**](https://github.com/niansia/taiwan-exam) *(`MIT`, APAC)* or 🟡 [**jeliael/fakao-ai-exam-engine**](https://github.com/jeliael/fakao-ai-exam-engine) *(`MIT`, APAC)* | 🟡 **`MIT` root, with a dependency caveat** | 🟡 **CARRIED as CANDIDATE, not production. `taiwan-exam` depends on **`PyMuPDF`, `AGPL-3.0`-or-Artifex-commercial**, so the `MIT` root does not reach the closure (`ACTION JR`). Swap for `pypdf` — already in the same `requirements.txt` — or buy the commercial limb BEFORE routing. 🆕 Both re-confirmed present and `MIT`-filtered in p177's census, at `18`★ and `10`★** |
| 🔴 **Education ERP / SIS** | [**openeducat_erp**](https://github.com/openeducat/openeducat_erp) *(`LGPL-3.0`)* on [**odoo/odoo**](https://github.com/odoo/odoo) *(`LGPL-3.0`)*, or [**frappe/erpnext**](https://github.com/frappe/erpnext) *(`GPL-3.0`)* | 🔴 **copyleft — no permissive option exists** | 🔴 **CARRIED, FIFTEENTH pass with no `MIT`/`Apache` education ERP. Its vendor-stated OneRoster / Ed-Fi / LTI 1.3 support is ABSENT from the open tree (`T162`)** |
| 🔴 **Full-stack MOOC platform** | [**openedx/edx-platform**](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | 🟢 **CARRIED unchanged. The RPC carve-out is a LICENSOR statement, not counsel (`gap 107`) — flag it as such in any deck** |
| 🔴 **LMS, mass-market copyleft** | [**moodle/moodle**](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** *(at `COPYING.txt`, not `LICENSE`)* | 🟢 **CARRIED unchanged. `88` grant documents, corrected down from `193` — `105` were PHP source files (`T223`)** |
| 🔴 **LMS, plain copyleft — second option** | [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`GPL-3.0`** | 🟢 **CARRIED unchanged. The cleanest inner grant surface of any copyleft LMS here — `2` bodies against `Moodle`'s `88`. Strong built-in exam/assessment tooling** |
| 🟡 **SIS, active** | [**RosarioSIS**](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** | 🟢 **CARRIED unchanged. Still the most active SIS this KB holds** |
| 🟡 **SIS, active** | [**openSIS-Classic**](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** *(NOT at the root)* | 🟢 **CARRIED. `ACTION KJ` probed `16` paths including every British spelling and `COPYING.md` — `0` of `16`; its `GPL-2.0` is at `docs/License.txt`** |
| 🔴 **SIS, PERMISSIVE and institutional-scale** | 🔴 **none** | — | 🔴 **CARRIED, FIFTEENTH pass. `ACTION KE` refuted the one candidate at p175 (`eagles-edu/sis` is a portal: `0` interop tokens at word-boundary precision). 🔵 `canvasapi` remains a permissive rostering CLIENT with write reach, which is a different thing from a permissive system of record** |
| 🟡 **SIS, permissive — remaining candidates** | 🟡 [**opensacorg/learning-blocks**](https://github.com/opensacorg/learning-blocks) *(`849` files, **Code for Sacramento**)* · [**Arux-Software/Bright**](https://github.com/Arux-Software/Bright) *(toolkit, not a system of record)* | 🟢 **both `MIT`** — bodies read at p174 | 🟡 **CARRIED as CANDIDATES. NEITHER has been probed the way `ACTION KE` probed the third one. 🔴 Do not quote either as rostering-capable. 🆕 🔴 Their published byte counts (`1 075` B each) are now suspect under `ACTION KS` and were NOT re-measured this pass** |
| 🔴 **LMS, corporate training** | [**Forma LMS**](https://github.com/formalms/formalms) | 🔴 **`GPL-2.0`** *(at `html/license.txt`; NO root grant)* | 🔴 **CARRIED as REFUTED, probe-complete. A secondary source calls it *"Apache 2.0"*; its body is the GNU `GPL` v`2` verbatim, shipped in `9` languages with nothing naming which governs (`gap 116`)** |
| 🔵 **Learning-record plumbing** | 🔴 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | 🟢 `Apache-2.0` *(`11 357` B)* | 🔵 **DELIBERATELY NOT ROUTED, seventh pass. Last commit `2026-02-26`, `Django<4.0` (EOL April `2024`), `0` matches for `xapi`/`caliper`/`statement`. Vendor the idea, do not ship the package** |
| 🔴 **THREAT MODEL — not a dependency** | 🔴 [**sgaofen/vibe-schooling**](https://github.com/sgaofen/vibe-schooling) | 🟢 **`MIT`** *(🆕 **`1 064` B — CORRECTED** from `1 063`, *"© 2026 sgaofen"*)* | 🔴 **CARRIED as an ATTACK SURFACE, per `P171-D`. `HEAD` `7c2f87a4641b`, `56` files, `80`★ — still the third-most-starred row on `topic:ai-education` and UNMOVED in stars this pass. Canvas named `19`×, topics `canvas-lms` + `exam-automation`. 🔵 Any Canvas engagement that routes `canvasapi` should assume this exists on the student side** |

🟢 **The tally, counted by ROW rather than by summing buckets — the discipline p176 adopted after
two compensating arithmetic errors cancelled into a right-looking total.**
**`22` rows: `11` permissive and routable** *(OpenOLAT, Kolibri, mentingo, dolos, edfi-oneroster,
canvasapi, OB3DefinitionWidget, scorm-again, plus the `3` candidate entries — Artemis, the
exam-generation pair counted as ONE row, and the SIS-candidate pair counted as ONE row)*, **`1`
permissive-with-a-patent-limb** *(Sakai)*, **`7` copyleft or non-permissive** *(education ERP, Open
edX, Moodle, ILIAS, RosarioSIS, openSIS-Classic, Forma LMS)*, **`1` declared EMPTY** *(permissive
institutional SIS)*, **`1` deliberately not routed** *(openlxp-xia)*, **`1` threat model**
*(vibe-schooling)*. 🔵 **`11 + 1 + 7 + 1 + 1 + 1 = 22`, and the `22` is the row count, not a
reconciliation of it.**
🆕 🟢 **Verified ROUTES promoted by reading code rather than a licence: `2` of `22`** — `canvasapi`
(p176) and `dolos` (p177). 🔴 **That is the honest denominator for this table's maturity.**


## Pass 176 — 2026-10-13

🆕 🟢 **One CANDIDATE becomes a ROUTE, and it is the first time this file has promoted a row by
reading its code rather than its licence.** `ACTION KM` read
[`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) past its grant: `612` named REST calls,
`127` `POST` / `89` `PUT` / `74` `DELETE` among them, a `Bearer`-token auth model of its own,
`per_page`-driven pagination that follows the next link, `10` typed exceptions including
`RateLimitExceeded`, and rostering routes named outright — `courses/{}/enrollments`,
`sections/{}/enrollments`, `enrollment_terms`.
🔴 **It routes under one condition that must be said in the same breath: it is a CLIENT for Canvas,
and Canvas's own core is `AGPL-3.0` with the operated product sold.** 🔵 **The permissive layer is
the client. The system of record is not permissive, and this file should never let that elide.**
🆕 🔴 **And a threat-model row enters, from the same tag this KB samples its agents from.** The
third-most-starred repository on `topic:ai-education` is
[`sgaofen/vibe-schooling`](https://github.com/sgaofen/vibe-schooling) (`MIT`, `1 063` B,
`HEAD` `7c2f87a4641b`, `80`★) — *"Get 4.0 GPA without learning"*, naming **Canvas `19` times**,
`quiz` `7`, `exam` `6`, `answer` `10`, with topics `canvas-lms` and `exam-automation`.
🔵 **The platform this file now routes a rostering client FOR is the platform the tag's third row
automates cheating against.** 🟢 **Both are `MIT`, both are real, and the defence row
(`dodona-edu/dolos`) entered one pass ago. Name all three together or the engagement finds out in
week two.**
🟢 **The routing table RE-STATES EVERY ROW, per `P170-C`/`T216`: under *"only the newest block is
canonical"* a row not re-stated is lost however true it remains below.**

### 🟢 THE ROUTING TABLE — re-stated in full at p176

| need | route | licence *(body read)* | status at p176 |
|---|---|---|---|
| 🟢 **LMS, permissive — institutional** | [**OpenOLAT**](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** *(§`1`–`9` verbatim, `10 982` B)* | 🟢 **CARRIED unchanged. `QTI`, `SCORM`, curriculum and assessment built in. Carry the `2` attribution statements** |
| 🟢 **LMS, permissive — offline / low-connectivity** | [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The LATAM, APAC low-bandwidth and Africa row. 🆕 🟡 `ACTION KK` downgrades its PLACEMENT evidence, not the row: its artefact names *"Learning Equality"* and no country** |
| 🟡 **LMS, permissive — Java institutional, patent limb** | [**Sakai**](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** *(root)* | 🟡 **CARRIED WITH THE SAME THREE FLAGS. Narrowed patent grant (`T200`); fails `mentingo`'s own licence gate (`T208`); `8` of `86` `licenses/` paths are NOT open-source grants; `25` of `86` are `Apache-1.1`, so clause `3` attribution is owed (`ACTION JU`)** |
| 🟢 **LMS, permissive — AI-native / corporate L&D** | [**Selleo/mentingo**](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** *(`1 062` B)* | 🟢 **CARRIED, EMEA. `SCORM` import AND export, ships `licenses.config.yaml`, the gate to LIFT. Still the only row in this KB DECLARING both `scorm` and `xapi`** |
| 🟡 **LMS, permissive — university-OWNED exercise + exam platform** | 🟡 [**ls1intum/Artemis**](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** *(`1 090` B, *"© 2026 TUM Applied Education Technologies"*)* | 🟡 **CARRIED as CANDIDATE, EMEA, HOLDER-GRADE. `HEAD` `09266581a02c`, `818`★. 🔴 Still licence-, holder- and `HEAD`-verified ONLY — p176 spent its code-reading budget on `canvasapi` instead, and says so (`gap 134`)** |
| 🟢 **Assessment integrity — plagiarism detection, permissive** | 🟢 [**dodona-edu/dolos**](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** *(`1 083` B, *"© 2019 Team Dolos <dolos@ugent.be>"*)* | 🟢 **CARRIED, EMEA, HOLDER-GRADE. `HEAD` `44925b867ce7`, `350`★. 🆕 🔴 And its urgency rises: the tag's third row is Canvas-targeted exam automation under `MIT`. 🟡 CANDIDATE still — language coverage and false-positive behaviour UNVERIFIED** |
| 🟢 **Rostering, permissive — standards-native, READ-ONLY** | [**Ed-Fi-Alliance-OSS/edfi-oneroster**](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`** *(`10 173` B)* | 🟢 **CARRIED unchanged. `OneRoster 1.2`, `24` GETs over `12` entities, `0` write routes. Still the only STANDARDS-native permissive rostering route here** |
| 🆕 🟢 **Rostering, permissive — Canvas-native, READ AND WRITE** | 🆕 🟢 [**ucfopen/canvasapi**](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** *(🆕 `1 130` B, *"© 2017 University of Central Florida — Center for Distributed Learning"*)* | 🆕 🟢 **PROMOTED from candidate to ROUTE, North America. `HEAD` `513588f3077f`, `682`★. `ACTION KM`: `enrollments`, `sections`, `enrollment_terms` reached with READ AND WRITE; `Bearer` auth; `per_page=100` pagination following the next link; `10` typed exceptions; `sis_*_id` addressing; `1 112` test methods. 🔴 **CONDITIONS:** `0` word-boundary matches for OneRoster, Ed-Fi, SCORM, xAPI or Caliper — it speaks Canvas, not a standard; and it is a client for an `AGPL-3.0` core. 🟡 Last commit `2026-04-16` — `180` d, exactly at the liveness bar** |
| 🟢 **Portable credentials — Open Badges `3.0` authoring** | [**opensalt/OB3DefinitionWidget**](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **`MIT`** *(`1 080` B)* | 🟢 **CARRIED unchanged. Pair with `OpenOLAT`'s `OB2` module — which is `2.0` ONLY, no W3C VC** |
| 🟢 **SCORM / AICC / xAPI interop** | [**jcputney/scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The only row where grant-named paths and grant bodies agree exactly** |
| 🟡 **Assessment / exam generation, permissive** | 🟡 [**niansia/taiwan-exam**](https://github.com/niansia/taiwan-exam) *(`MIT`, APAC)* or 🟡 [**jeliael/fakao-ai-exam-engine**](https://github.com/jeliael/fakao-ai-exam-engine) *(`MIT`, APAC)* | 🟡 **`MIT` root, with a dependency caveat** | 🟡 **CARRIED as CANDIDATE, not production. `taiwan-exam` depends on **`PyMuPDF`, `AGPL-3.0`-or-Artifex-commercial**, so the `MIT` root does not reach the closure (`ACTION JR`). Swap for `pypdf` — already in the same `requirements.txt` — or buy the commercial limb BEFORE routing. 🆕 Both re-confirmed present and `MIT`-filtered in p176's `topic:ai-education` census, at `18`★ and `10`★** |
| 🔴 **Education ERP / SIS** | [**openeducat_erp**](https://github.com/openeducat/openeducat_erp) *(`LGPL-3.0`)* on [**odoo/odoo**](https://github.com/odoo/odoo) *(`LGPL-3.0`)*, or [**frappe/erpnext**](https://github.com/frappe/erpnext) *(`GPL-3.0`)* | 🔴 **copyleft — no permissive option exists** | 🔴 **CARRIED, FOURTEENTH pass with no `MIT`/`Apache` education ERP. Its vendor-stated OneRoster / Ed-Fi / LTI 1.3 support is ABSENT from the open tree (`T162`)** |
| 🔴 **Full-stack MOOC platform** | [**openedx/edx-platform**](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | 🟢 **CARRIED unchanged. The RPC carve-out is a LICENSOR statement, not counsel (`gap 107`) — flag it as such in any deck** |
| 🔴 **LMS, mass-market copyleft** | [**moodle/moodle**](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** *(at `COPYING.txt`, not `LICENSE`)* | 🟢 **CARRIED unchanged. `88` grant documents, corrected down from `193` — `105` were PHP source files (`T223`)** |
| 🔴 **LMS, plain copyleft — second option** | [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`GPL-3.0`** | 🟢 **CARRIED unchanged. The cleanest inner grant surface of any copyleft LMS here — `2` bodies against `Moodle`'s `88`. Strong built-in exam/assessment tooling** |
| 🟡 **SIS, active** | [**RosarioSIS**](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** | 🟢 **CARRIED unchanged. Still the most active SIS this KB holds** |
| 🟡 **SIS, active** | [**openSIS-Classic**](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** *(NOT at the root)* | 🆕 🟢 **CARRIED, and the doubt `gap 133` cast on it is LIFTED: `ACTION KJ` probed `16` paths including every British spelling and `COPYING.md` — `0` of `16`. The *"no root grant"* verdict was right, and its `GPL-2.0` is still at `docs/License.txt`** |
| 🔴 **SIS, PERMISSIVE and institutional-scale** | 🔴 **none** | — | 🔴 **CARRIED, FOURTEENTH pass. `ACTION KE` refuted the one candidate at p175 (`eagles-edu/sis` is a portal: `0` interop tokens at word-boundary precision, a `SisConfigMirror` model). 🆕 🔵 And `ACTION KM` sharpens what *"none"* means rather than softening it: a permissive rostering CLIENT with write reach now exists for Canvas-run institutions, which is a different thing from a permissive system of record** |
| 🟡 **SIS, permissive — remaining candidates** | 🟡 [**opensacorg/learning-blocks**](https://github.com/opensacorg/learning-blocks) *(`849` files, **Code for Sacramento**)* · [**Arux-Software/Bright**](https://github.com/Arux-Software/Bright) *(toolkit, not a system of record)* | 🟢 **both `MIT`** — bodies read at p174: `1 075` B, and `1 075` B at `LICENSE.txt` | 🟡 **CARRIED as CANDIDATES. NEITHER has been probed the way `ACTION KE` probed the third one. 🔴 Do not quote either as rostering-capable — that is exactly the claim that failed at p175. 🆕 `learning-blocks` is placed to the United States at SUBNATIONAL grade by `ACTION KK` (*"Sacramento"* in the artefact)** |
| 🔴 **LMS, corporate training** | [**Forma LMS**](https://github.com/formalms/formalms) | 🔴 **`GPL-2.0`** *(at `html/license.txt`; NO root grant)* | 🆕 🔴 **CARRIED as REFUTED, and the refutation is now probe-complete: `ACTION KJ` found `0` of `16` grant paths at the root, British spellings included. A secondary source calls it *"Apache 2.0"*; its body is the GNU `GPL` v`2` verbatim, shipped in `9` languages with nothing naming which governs (`gap 116`)** |
| 🔵 **Learning-record plumbing** | 🔴 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | 🟢 `Apache-2.0` *(`11 357` B)* | 🔵 **DELIBERATELY NOT ROUTED, sixth pass. Last commit `2026-02-26`, `Django<4.0` (EOL April `2024`), `0` matches for `xapi`/`caliper`/`statement`. Vendor the idea, do not ship the package** |
| 🆕 🔴 **THREAT MODEL — not a dependency** | 🆕 🔴 [**sgaofen/vibe-schooling**](https://github.com/sgaofen/vibe-schooling) | 🟢 **`MIT`** *(`1 063` B, *"© 2026 sgaofen"*)* | 🆕 🔴 **NEW ROW, recorded as an ATTACK SURFACE exactly as `P171-D` records the proctoring-attack tool. `HEAD` `7c2f87a4641b`, `56` files, `80`★, third-most-starred on `topic:ai-education`. Canvas named `19`×, `quiz` `7`, `exam` `6`, topics `canvas-lms` + `exam-automation`. 🔵 Any Canvas engagement that routes `canvasapi` should assume this exists on the student side** |

🆕 🟢 **The tally, RE-COUNTED against the `22` rows above — and the first count was WRONG, by two
errors that cancelled.** 🔴 **The draft tally read `7` + `5` + `6` + `4` = `22`, which matched the
row count and was still wrong twice: it counted the exam-generation row as TWO rows because it names
two repositories, and it gave `Sakai` no bucket at all.** 🔵 **Two compensating errors summing to the
right total is the exact failure this file keeps warning about, and it was caught by counting the
rows rather than trusting the sum.**

| verdict | rows | which |
|---|---|---|
| 🟢 **permissive and ROUTABLE** | 🟢 **`7`** | institutional LMS, offline LMS, AI-native LMS, standards rostering *(read-only)*, 🆕 **Canvas rostering *(read+write)***, credentials, SCORM interop |
| 🟡 **permissive CANDIDATE — licence verified, code not** | 🟡 **`4`** | `Artemis`, `dolos`, exam generation *(ONE row, two named repositories)*, remaining SIS candidates |
| 🟡 **permissive WITH FLAGS — a narrowed grant, not a clean one** | 🟡 **`1`** | `Sakai` (`ECL-2.0`) — the bucket the draft tally forgot |
| 🔴 **copyleft only, no permissive option** | 🔴 **`6`** | education ERP/SIS, MOOC platform, mass-market LMS, second copyleft LMS, `2` active SIS |
| 🔴 **refuted, not routed, or a threat model** | 🔴 **`4`** | `Forma LMS`, `openlxp-xia`, permissive institutional SIS *(none exists)*, 🆕 `vibe-schooling` |

🔵 **`7` + `4` + `1` + `6` + `4` = `22`, against `22` rows counted one by one.** 🟢 **The sum and the
row count are both shown, because this pass has just demonstrated that agreeing with the total is
not the same as being right.**

## Pass 175 — 2026-10-13

🆕 🔴 **The row p174 was most pleased with is REFUTED, and the twelve-pass sentence it overturned is
RESTORED with p174's denominator correction intact.** `ACTION KE` read
[`eagles-edu/sis`](https://github.com/eagles-edu/sis) past its licence and found `0` word-boundary
matches for OneRoster, Ed-Fi, LTI, SCORM, xAPI, `tenant`, `tenancy` and every federated auth
protocol. 🔴 **Every signal it appeared to carry was a substring:** `ed-fi` was matching `red-fill`,
`edfi` was matching `normalizedField`, `lti` was matching `LevelTile` (`T265`). 🔵 **And its own
schema settles it — a model named `SisConfigMirror` holding an opaque `payloadJson`. A system of
record does not mirror its configuration from somewhere else.**
🆕 🟢 **Three rows ENTER, and one of them fills a need this file has never had a row for at all:
assessment integrity.** `dodona-edu/dolos` is Ghent University's source-code plagiarism detector
under `MIT` — the first permissive route this KB can name for the problem every AI-in-education
engagement hits in week one.
🟡 **The three new rows are licence-, holder-, byte- and `HEAD`-verified and NOTHING else.** 🔵 **That
restraint IS the lesson of the row that left: p174 published a capability claim on top of a licence
check, and p175 will not.**
🟢 **No platform root grant was re-read this pass and this file says so.** Every other row carries
its p168–p174 verdict forward unchanged.
🟢 **The routing table RE-STATES EVERY ROW, per `P170-C`/`T216`: under *"only the newest block is
canonical"* a row not re-stated is lost however true it remains below.**

### 🟢 THE ROUTING TABLE — re-stated in full at p175

| need | route | licence *(body read)* | status at p175 |
|---|---|---|---|
| 🟢 **LMS, permissive — institutional** | [**OpenOLAT**](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** *(§`1`–`9` verbatim, `10 982` B)* | 🟢 **CARRIED unchanged. `QTI`, `SCORM`, curriculum and assessment built in. Carry the `2` attribution statements** |
| 🟢 **LMS, permissive — offline / low-connectivity** | [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged, and independently re-confirmed in p175's `topic:education` sweep at `1 143`★ with holder-grade North American placement. The LATAM, APAC low-bandwidth and Africa row — the last on a MEASUREMENT (`ACTION JY`: `16` formulations, `0` MEA-originated permissive active repositories)** |
| 🟡 **LMS, permissive — Java institutional, patent limb** | [**Sakai**](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** *(root)* | 🟡 **CARRIED WITH THE SAME THREE FLAGS. Narrowed patent grant (`T200`); fails `mentingo`'s own licence gate (`T208`); `8` of `86` `licenses/` paths are NOT open-source grants; `25` of `86` are `Apache-1.1`, so clause `3` attribution is owed (`ACTION JU`)** |
| 🟢 **LMS, permissive — AI-native / corporate L&D** | [**Selleo/mentingo**](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** *(`1 062` B)* | 🟢 **CARRIED, EMEA. `SCORM` import AND export, ships `licenses.config.yaml`, the gate to LIFT. 🆕 And `ACTION KE` makes one of its properties worth stating plainly: it is the only row in this KB that DECLARES both `scorm` and `xapi`, where the candidate SIS declared neither at any precision** |
| 🆕 🟡 **LMS, permissive — university-OWNED exercise + exam platform** | 🆕 🟡 [**ls1intum/Artemis**](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** *(`1 090` B, *"© 2026 TUM Applied Education Technologies"*)* | 🆕 🟡 **NEW, EMEA, HOLDER-GRADE. `HEAD` `09266581a02c`, `818`★. Programming, modelling and text exercises, autograding, automated feedback, an exam mode — a Technical University of Munich teaching system released permissively. 🟡 **CANDIDATE, NOT ROUTE:** licence body, holder and `HEAD` verified; interop, tenancy, auth and dependency closure are NOT (`gap 134`)** |
| 🆕 🟢 **Assessment integrity — plagiarism detection, permissive** | 🆕 🟢 [**dodona-edu/dolos**](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** *(`1 083` B, *"© 2019 Team Dolos <dolos@ugent.be>"*)* | 🆕 🟢 **NEW, EMEA, HOLDER-GRADE. `HEAD` `44925b867ce7`, `350`★. Source-code similarity and collusion detection from Ghent University. 🔵 **This need has had NO row in this file until now** — every assessment-integrity recommendation here was a design pattern (oral defence, process evidence) because no permissive tool existed to name. 🟡 **CANDIDATE:** licence verified, language coverage and false-positive behaviour are not** |
| 🟢 **Rostering, permissive** | [**Ed-Fi-Alliance-OSS/edfi-oneroster**](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`** *(`10 173` B)* | 🟢 **CARRIED unchanged. `OneRoster 1.2`, `24` GETs over `12` entities, `0` write routes. Still the only permissive rostering route verified here** |
| 🆕 🟡 **Canvas LMS integration — client library, permissive** | 🆕 🟡 [**ucfopen/canvasapi**](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** *(`1 129` B, *"© 2017 University of Central Florida — Center for Distributed Learning"*)* | 🆕 🟡 **NEW, North America, HOLDER-GRADE. `HEAD` `513588f3077f`, `682`★. A Python client for Canvas LMS — courses, users, gradebooks. 🔵 **Rostering-ADJACENT rather than rostering-primary**, so `gap 123` improves without closing: the administrative layer finally has a permissive client under it. 🟡 **CANDIDATE:** whether it reaches `enrollments`/`sections`/`terms`, and its auth and pagination semantics, are UNVERIFIED — `ACTION KM`** |
| 🟢 **Portable credentials — Open Badges `3.0` authoring** | [**opensalt/OB3DefinitionWidget**](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **`MIT`** *(`1 080` B)* | 🟢 **CARRIED unchanged. Pair with `OpenOLAT`'s `OB2` module — which is `2.0` ONLY, no W3C VC** |
| 🟢 **SCORM / AICC / xAPI interop** | [**jcputney/scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The only row where grant-named paths and grant bodies agree exactly** |
| 🟡 **Assessment / exam generation, permissive** | 🟡 [**niansia/taiwan-exam**](https://github.com/niansia/taiwan-exam) *(`MIT`, APAC)* or 🟡 [**jeliael/fakao-ai-exam-engine**](https://github.com/jeliael/fakao-ai-exam-engine) *(`MIT`, APAC)* | 🟡 **`MIT` root, with a dependency caveat** | 🟡 **CARRIED as CANDIDATE, not production. `taiwan-exam` depends on **`PyMuPDF`, `AGPL-3.0`-or-Artifex-commercial**, so the `MIT` root does not reach the closure (`ACTION JR`). Swap for `pypdf` — already in the same `requirements.txt` — or buy the commercial limb BEFORE routing. 🆕 Both rows are `P800`-placeable in APAC by the national examination each names, confirmed in p175's sweep** |
| 🔴 **Education ERP / SIS** | [**openeducat_erp**](https://github.com/openeducat/openeducat_erp) *(`LGPL-3.0`)* on [**odoo/odoo**](https://github.com/odoo/odoo) *(`LGPL-3.0`)*, or [**frappe/erpnext**](https://github.com/frappe/erpnext) *(`GPL-3.0`)* | 🔴 **copyleft — no permissive option exists** | 🔴 **CARRIED, THIRTEENTH pass with no `MIT`/`Apache` education ERP. Its vendor-stated OneRoster / Ed-Fi / LTI 1.3 support is ABSENT from the open tree (`T162`)** |
| 🔴 **Full-stack MOOC platform** | [**openedx/edx-platform**](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | 🟢 **CARRIED unchanged. The RPC carve-out is a LICENSOR statement, not counsel (`gap 107`) — flag it as such in any deck** |
| 🔴 **LMS, mass-market copyleft** | [**moodle/moodle**](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** *(at `COPYING.txt`, not `LICENSE`)* | 🟢 **CARRIED unchanged. `88` grant documents, corrected down from `193` — `105` were PHP source files (`T223`)** |
| 🔴 **LMS, plain copyleft — second option** | [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`GPL-3.0`** | 🟢 **CARRIED unchanged. The cleanest inner grant surface of any copyleft LMS here — `2` bodies against `Moodle`'s `88`. Strong built-in exam/assessment tooling** |
| 🟡 **SIS, active** | [**RosarioSIS**](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** | 🟢 **CARRIED unchanged. Still the most active SIS this KB holds** |
| 🟡 **SIS, active** | [**openSIS-Classic**](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** *(NOT at the root)* | 🟡 **CARRIED unchanged — and `gap 133` puts its *"no root grant file"* verdict back in doubt along with every other licence-absence claim here: the British spelling `LICENCE` was never probed. `ACTION KJ`** |
| 🔴 **SIS, PERMISSIVE and institutional-scale** | 🔴 **none** | — | 🔴 **RESTORED after one pass as a route, THIRTEENTH pass as a verdict. `ACTION KE` refuted the candidate: `eagles-edu/sis` is a parent-and-student PORTAL in front of an SIS — `0` interop tokens at word-boundary precision, `0` tenancy, hand-rolled cookie sessions, and a `SisConfigMirror` model. 🟢 **p174's denominator correction STANDS** — `54` permissive SIS repositories are active and `topic:education` is `8 197` — **but the head of that population is `31`★ and the largest tree in it does not roster.** 🔵 **The honest sentence is a procurement statement, not an absence: permissive SIS repositories exist, none is institutional-scale, and the biggest is a portal** |
| 🟡 **SIS, permissive — remaining candidates** | 🟡 [**opensacorg/learning-blocks**](https://github.com/opensacorg/learning-blocks) *(`849` files, **Code for Sacramento**)* · [**Arux-Software/Bright**](https://github.com/Arux-Software/Bright) *(toolkit, not a system of record)* | 🟢 **both `MIT`** — bodies read at p174: `1 075` B, and `1 075` B at `LICENSE.txt` | 🟡 **CARRIED as CANDIDATES, and now carried with an explicit warning: NEITHER has been probed the way `ACTION KE` probed the third one.** `learning-blocks` is holder-placed in North America by a Code for America brigade. 🔴 **Do not quote either as rostering-capable — that is exactly the claim that failed this pass** |
| 🔴 **LMS, corporate training** | [**Forma LMS**](https://github.com/formalms/formalms) | 🔴 **`GPL-2.0`** *(at `html/license.txt`; NO root grant)* | 🔴 **CARRIED as REFUTED. A secondary source calls it *"Apache 2.0"*; its body is the GNU `GPL` v`2` verbatim, shipped in `9` languages with nothing naming which governs (`gap 116`)** |
| 🔵 **Learning-record plumbing** | 🔴 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | 🟢 `Apache-2.0` *(`11 357` B)* | 🔵 **DELIBERATELY NOT ROUTED, fifth pass. Last commit `2026-02-26`, `Django<4.0` (EOL April `2024`), `0` matches for `xapi`/`caliper`/`statement`. Vendor the idea, do not ship the package** |

🆕 🟢 **The tally, RE-COUNTED against the `21` rows above rather than carried — this file keeps
being defeated by its own arithmetic, so the sum is shown:**

| verdict | rows | which |
|---|---|---|
| 🟢 **permissive and routable** | 🟢 **`6`** | institutional LMS, offline LMS, AI-native LMS, rostering, credentials, SCORM interop |
| 🟡 **permissive, CANDIDATE — licence verified, capability NOT** | 🟡 **`7`** | `Sakai` *(three flags)*, assessment generation *(dependency closure)*, 🆕 `Artemis`, 🆕 `Dolos`, 🆕 `canvasapi`, SIS remaining candidates, `openSIS-Classic`'s grant-path doubt |
| 🔴 **copyleft only** | 🔴 **`6`** | education ERP, MOOC platform, `Moodle`, `ILIAS`, `RosarioSIS`, `Forma LMS` |
| 🔵 **permissive but DELIBERATELY not routed** | 🔵 **`1`** | learning-record plumbing *(`openlxp-xia`, dead tree)* |
| 🔴 **needs with NO option at all** | 🔴 **`1`** | 🔴 **institutional-scale permissive SIS — the column is OCCUPIED again** |

🟢 **`6 + 7 + 6 + 1 + 1 = 21`, which is the number of rows.**
🔴 **And the last line is this pass's finding: the *"no option at all"* column was empty for exactly
one pass.** 🔵 **It emptied because a query was fixed and it refilled because the thing the query
found was read properly. Both are progress; only one of them is good news.**

### 🆕 🔴 How this file states a negative, corrected twice in two passes

| | |
|---|---|
| 🔴 **p173 and before** | 🔴 ***"SIS, permissive: none exists. Twelfth pass."*** — a negative re-tested every pass on the SAME query, which is repetition, not re-testing |
| 🟡 **p174** | 🟡 ***"`54` permissive SIS repositories are active; the two with substantial trees are `eagles-edu/sis` and `learning-blocks`; neither verified for OneRoster, SCORM or tenancy."*** — the denominator fixed, the candidate routed too fast |
| 🟢 **p175** | 🟢 ***"`54` exist. The largest is a parent-and-student portal in front of an SIS, measured at word-boundary precision: `0` rostering, `0` standards interop, `0` tenancy, and a `SisConfigMirror` model. The head of the population is `31`★. There is no institutional-scale permissive SIS, and that is a procurement statement — not an absence of software, and not a gap in this KB's searching."*** |

🆕 🔵 **`T265`, stated where a routing decision gets made: a capability claim needs an ARTEFACT, not
a token.** For rostering that means an `/ims/oneroster/v1p1` route or an `EdFi` client class; for
tracking, an xAPI or `cmi5` statement emitter; for tenancy, a tenant column or schema per customer.
🔵 **Grepping the standard's NAME finds the CSS variable that happens to contain it.**
[`evidence/sis-interop-probe.2026-10-13-p175.tsv`](../evidence/sis-interop-probe.2026-10-13-p175.tsv)

## Pass 174 — 2026-10-13

🆕 🔴 **One row changes and it is the one this file has carried as *"none exists"* for twelve
passes. A PERMISSIVE student information system does exist — three of them, `MIT`, bodies read, and
two with real trees (`2 598` and `849` files) committed inside the last month. 🟢 **Nothing new was
written by anyone: the DENOMINATOR was wrong.** p173 found that every population figure here was
measured on `topic:ai-education`, which `1` of this KB's `12` shelf rows carries (`T255`). p174 made
`topic:education` countable (`ACTION JZ`, `8 191` exactly), ran the sweep p173 said had never been
run, and `"student information system" license:mit pushed:>=2026-04-16` returned **`54`**.**
🆕 🟡 **They are routed as CANDIDATES and not as routes, deliberately.** Licence body, `HEAD`, tree
size and commit date are verified; `OneRoster`, `SCORM`, tenancy and dependency closure are not.
🔴 **The honest residue: the head of that `54` is `31`★.** *"No institutional-scale permissive SIS"*
survives this pass. *"None exists"* does not, and it should never have been stated on a denominator
`~61×` too small.
🆕 🟢 **The Africa line on the Kolibri row is now a measurement, not an inference** — `16` query
formulations, `0` MEA-originated permissive active education repositories (`ACTION JY`).
🟢 **No platform root grant was re-read this pass and this file says so.** Every other row carries
its p168–p173 verdict forward unchanged.
🟢 **The routing table RE-STATES EVERY ROW, per `P170-C`/`T216`: under *"only the newest block is
canonical"* a row not re-stated is lost however true it remains below. Verified with
[`compose/code/p171-cross-block-gate/check_lost_rows.py`](../compose/code/p171-cross-block-gate/check_lost_rows.py)
before commit.**

### 🟢 THE ROUTING TABLE — re-stated in full at p174

| need | route | licence *(body read)* | status at p174 |
|---|---|---|---|
| 🟢 **LMS, permissive — institutional** | [**OpenOLAT**](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** *(§`1`–`9` verbatim, `10 982` B)* | 🟢 **CARRIED unchanged. `QTI`, `SCORM`, curriculum and assessment built in. Carry the `2` attribution statements** |
| 🟢 **LMS, permissive — offline / low-connectivity** | [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The LATAM and APAC low-bandwidth row — and now the Africa row too, on a MEASUREMENT rather than an inference: `16` formulations across two channels returned `0` MEA-originated permissive active education repositories (`ACTION JY`), so for this region Kolibri is not the low-bandwidth preference — it is the only thing to build on** |
| 🟡 **LMS, permissive — Java institutional, patent limb** | [**Sakai**](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** *(root)* | 🆕 🟡 **CARRIED WITH THE SAME THREE FLAGS, one of them now MEASURED CORRECTLY. Narrowed patent grant (`T200`); fails `mentingo`'s own licence gate (`T208`); `8` of `86` `licenses/` paths are NOT open-source grants (`ACTION JO`). 🆕 **And `25` of the `86` are `Apache-1.1`, not `BSD` — clause `3` attribution is owed (`ACTION JU`)** |
| 🟢 **LMS, permissive — AI-native / corporate L&D** | [**Selleo/mentingo**](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** *(`1 062` B)* | 🟢 **CARRIED, EMEA. HEAD `242a9324fe48`, last commit `2026-10-10` — `3` days before this pass. `SCORM` import AND export, ships `licenses.config.yaml`, the gate to LIFT. `20` declared topics, the most of any row this KB holds** |
| 🟢 **Rostering, permissive** | [**Ed-Fi-Alliance-OSS/edfi-oneroster**](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`** *(`10 173` B)* | 🟢 **CARRIED unchanged. `OneRoster 1.2`, `24` GETs over `12` entities, `0` write routes. The only permissive rostering route verified here** |
| 🟢 **Portable credentials — Open Badges `3.0` authoring** | [**opensalt/OB3DefinitionWidget**](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **`MIT`** *(`1 080` B)* | 🟢 **CARRIED unchanged. Pair with `OpenOLAT`'s `OB2` module — which is `2.0` ONLY, no W3C VC** |
| 🟢 **SCORM / AICC / xAPI interop** | [**jcputney/scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The only row where grant-named paths and grant bodies agree exactly** |
| 🟡 **Assessment / exam generation, permissive** | 🟡 [**niansia/taiwan-exam**](https://github.com/niansia/taiwan-exam) *(`MIT`, APAC)* or 🟡 [**jeliael/fakao-ai-exam-engine**](https://github.com/jeliael/fakao-ai-exam-engine) *(`MIT`, APAC)* | 🟡 **`MIT` root, with a dependency caveat** | 🟡 **CARRIED as CANDIDATE, not production. `taiwan-exam` is the stronger tree (`593` files, `129` commits in `30` d, `89` tests) but depends on **`PyMuPDF`, `AGPL-3.0`-or-Artifex-commercial**, so the `MIT` root does not reach the closure (`ACTION JR`). Swap for `pypdf` — already in the same `requirements.txt` — or buy the commercial limb BEFORE routing** |
| 🔴 **Education ERP / SIS** | [**openeducat_erp**](https://github.com/openeducat/openeducat_erp) *(`LGPL-3.0`)* on [**odoo/odoo**](https://github.com/odoo/odoo) *(`LGPL-3.0`)*, or [**frappe/erpnext**](https://github.com/frappe/erpnext) *(`GPL-3.0`)* | 🔴 **copyleft — no permissive option exists** | 🔴 **CARRIED, TWELFTH pass with no `MIT`/`Apache` education ERP. Its vendor-stated OneRoster / Ed-Fi / LTI 1.3 support is ABSENT from the open tree (`T162`)** |
| 🔴 **Full-stack MOOC platform** | [**openedx/edx-platform**](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | 🟢 **CARRIED unchanged. The RPC carve-out is a LICENSOR statement, not counsel (`gap 107`) — flag it as such in any deck** |
| 🔴 **LMS, mass-market copyleft** | [**moodle/moodle**](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** *(at `COPYING.txt`, not `LICENSE`)* | 🟢 **CARRIED unchanged. `88` grant documents, corrected down from `193` — `105` were PHP source files (`T223`)** |
| 🔴 **LMS, plain copyleft — second option** | [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`GPL-3.0`** | 🟢 **CARRIED unchanged. The cleanest inner grant surface of any copyleft LMS here — `2` bodies against `Moodle`'s `88`. Strong built-in exam/assessment tooling** |
| 🟡 **SIS, active** | [**RosarioSIS**](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** | 🟢 **CARRIED unchanged. Still the most active SIS this KB holds** |
| 🟡 **SIS, active** | [**openSIS-Classic**](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** *(NOT at the root)* | 🟢 **CARRIED unchanged. No root grant file, confirmed twice. The bundled CKEditor grants remain unread** |
| 🆕 🟡 **SIS, PERMISSIVE** | 🆕 🟡 [**eagles-edu/sis**](https://github.com/eagles-edu/sis) *(`2 598` files)* · [**opensacorg/learning-blocks**](https://github.com/opensacorg/learning-blocks) *(`849` files, **Code for Sacramento**)* · [**Arux-Software/Bright**](https://github.com/Arux-Software/Bright) *(toolkit, not a system of record)* | 🟢 **all three `MIT` — bodies read: `1 066` B, `1 075` B, `1 075` B at `LICENSE.txt`** | 🆕 🔴 **TWELVE PASSES OF *"none exists"* REFUTED, and by a DENOMINATOR fix rather than by new software. `ACTION JZ` made `topic:education` countable, so the sweep p173 said had never been run was run: `"student information system" license:mit pushed:>=2026-04-16` returns `54` — EXACTLY, not `~`. `eagles-edu/sis` last committed `2026-09-26` (`17` d) and `learning-blocks` `2026-09-15` (`28` d). 🟡 **CANDIDATE, NOT ROUTE:** licence, `HEAD`, tree size and commit date are verified and NOTHING else — no OneRoster, no SCORM, no tenancy, no dependency closure (`ACTION JR` discipline). The head of this population is `31`★, so *"no institutional-scale permissive SIS"* survives; *"none exists"* does not** |
| 🔴 **LMS, corporate training** | [**Forma LMS**](https://github.com/formalms/formalms) | 🔴 **`GPL-2.0`** *(at `html/license.txt`; NO root grant)* | 🔴 **CARRIED as REFUTED. A secondary source calls it *"Apache 2.0"*; its body is the GNU `GPL` v`2` verbatim, shipped in `9` languages with nothing naming which governs (`gap 116`)** |
| 🔴 **Learning-record plumbing** | 🔴 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | 🟢 `Apache-2.0` *(`11 357` B)* | 🔴 **DELIBERATELY NOT ROUTED, fourth pass. Last commit `2026-02-26`, `Django<4.0` (EOL April `2024`), `0` matches for `xapi`/`caliper`/`statement`. Vendor the idea, do not ship the package. `ACTION JV` put a number on why this call was right: `25.2%` of the *"active"* population is unpushed for `90` days (`T242`). 🆕 **And `ACTION KB` removes that reading's last caveat: `pushed:` and the last COMMIT are the same measurement to within a day on `19` of `20` sampled repositories** |

🆕 🟢 **The tally, RE-COUNTED against the `17` rows above rather than carried — p171's lesson was
that this file keeps being defeated by arithmetic, and p173's *"`6` of `16`"* did not add up:**

| verdict | rows | which |
|---|---|---|
| 🟢 **permissive and routable** | 🟢 **`6`** | institutional LMS, offline LMS, AI-native LMS, rostering, credentials, SCORM |
| 🟡 **permissive with a caveat** | 🟡 **`3`** | `Sakai` (`ECL-2.0`, three flags), assessment generation (dependency closure), 🆕 the SIS row (candidate, not route) |
| 🔴 **copyleft only** | 🔴 **`7`** | education ERP, MOOC platform, `Moodle`, `ILIAS`, `RosarioSIS`, `openSIS-Classic`, `Forma LMS` |
| 🔵 **permissive but DELIBERATELY not routed** | 🔵 **`1`** | learning-record plumbing (`openlxp-xia`, dead tree) |
| 🟢 **needs with NO option at all** | 🟢 **`0`** | — |

🟢 **`6 + 3 + 7 + 1 + 0 = 17`, which is the number of rows.** 🔴 **And the last line is the finding:
the *"no option at all"* column is EMPTY for the first time in twelve passes — because a query was
fixed, not because software appeared.**

### 🆕 🔴 What the SIS correction changes about how this file states a negative

| | |
|---|---|
| 🔴 **what p173 and the passes before it said** | 🔴 ***"SIS, permissive: none exists. Twelfth pass."*** |
| 🟢 **what p174 says** | 🟢 ***"`54` permissive student-information-system repositories are active right now. The two with substantial trees are `eagles-edu/sis` (`2 598` files, committed `17` days ago) and `opensacorg/learning-blocks` (`849` files, Code for Sacramento, `28` days). Neither is verified for OneRoster, SCORM or tenancy. The head of the population is `31`★, so there is still no institutional-scale option — which is a procurement statement, not an absence."*** |
| 🔴 **why the old sentence survived twelve passes** | 🔴 **It was re-tested every pass on the SAME query. `T255` found the query was the `1`-in-`12` tag; `ACTION JZ` made the wider one countable. 🔵 **A negative re-tested on an unchanged denominator is not re-tested — it is repeated.** |

🟡 **The liveness bar used on every row above, with its last caveat removed.** `ACTION JV` measured
the `180`-day *"active"* bar admitting `25.2%` of repositories unpushed for `90` days, and declared
a limit: it had measured PUSH recency where a routing decision wants COMMIT recency. 🟢 **`ACTION KB`
retires that limit:** across `20` repositories the push/commit gap is `0` days for `19` and `10`
days for the twentieth. **For a routing decision, read the commit date anyway** — `git clone
--depth 1 --filter=blob:none --no-checkout` then `git log -1 --format=%cI`, no API, `20` of `20`
reachable — but p173's bands need no asterisk.
## Pass 173 — 2026-10-13

🆕 🟢 **One row changes and it is a MEASUREMENT, not a status: the `Sakai` row's scanner-output
line. p170–p172 all reported *"`34` `BSD`"* over `Sakai`'s `licenses/`; the shared classifier was
blind to `Apache-1.1` and is not any more. The manifest is `25` `Apache-1.1` + `9` `BSD`
(`ACTION JU`). Nothing about whether to route `Sakai` changes — `Apache-1.1` is permissive and OSI
— but the ATTRIBUTION the client owes does.**
🆕 🟢 **No platform root grant was re-read this pass and this file says so. Every row below carries
its p168–p172 verdict forward except the `Sakai` scanner line.**
🟢 **The routing table RE-STATES EVERY ROW, per `P170-C`/`T216`: under *"only the newest block is
canonical"* a row not re-stated is lost however true it remains below. Verified with
[`compose/code/p171-cross-block-gate/check_lost_rows.py`](../compose/code/p171-cross-block-gate/check_lost_rows.py)
before commit.**

### 🟢 THE ROUTING TABLE — re-stated in full at p173

| need | route | licence *(body read)* | status at p173 |
|---|---|---|---|
| 🟢 **LMS, permissive — institutional** | [**OpenOLAT**](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** *(§`1`–`9` verbatim, `10 982` B)* | 🟢 **CARRIED unchanged. `QTI`, `SCORM`, curriculum and assessment built in. Carry the `2` attribution statements** |
| 🟢 **LMS, permissive — offline / low-connectivity** | [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The LATAM and APAC low-bandwidth row — and now the Africa row too: `gap 124` places two compulsory curricula and `6`-in-`10` HEIs without AI policy against an empty repository column** |
| 🟡 **LMS, permissive — Java institutional, patent limb** | [**Sakai**](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** *(root)* | 🆕 🟡 **CARRIED WITH THE SAME THREE FLAGS, one of them now MEASURED CORRECTLY. Narrowed patent grant (`T200`); fails `mentingo`'s own licence gate (`T208`); `8` of `86` `licenses/` paths are NOT open-source grants (`ACTION JO`). 🆕 **And `25` of the `86` are `Apache-1.1`, not `BSD` — clause `3` attribution is owed (`ACTION JU`)** |
| 🟢 **LMS, permissive — AI-native / corporate L&D** | [**Selleo/mentingo**](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** *(`1 062` B)* | 🟢 **CARRIED, EMEA. HEAD `242a9324fe48`, last commit `2026-10-10` — `3` days before this pass. `SCORM` import AND export, ships `licenses.config.yaml`, the gate to LIFT. `20` declared topics, the most of any row this KB holds** |
| 🟢 **Rostering, permissive** | [**Ed-Fi-Alliance-OSS/edfi-oneroster**](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`** *(`10 173` B)* | 🟢 **CARRIED unchanged. `OneRoster 1.2`, `24` GETs over `12` entities, `0` write routes. The only permissive rostering route verified here** |
| 🟢 **Portable credentials — Open Badges `3.0` authoring** | [**opensalt/OB3DefinitionWidget**](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **`MIT`** *(`1 080` B)* | 🟢 **CARRIED unchanged. Pair with `OpenOLAT`'s `OB2` module — which is `2.0` ONLY, no W3C VC** |
| 🟢 **SCORM / AICC / xAPI interop** | [**jcputney/scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 **CARRIED unchanged. The only row where grant-named paths and grant bodies agree exactly** |
| 🟡 **Assessment / exam generation, permissive** | 🟡 [**niansia/taiwan-exam**](https://github.com/niansia/taiwan-exam) *(`MIT`, APAC)* or 🟡 [**jeliael/fakao-ai-exam-engine**](https://github.com/jeliael/fakao-ai-exam-engine) *(`MIT`, APAC)* | 🟡 **`MIT` root, with a dependency caveat** | 🟡 **CARRIED as CANDIDATE, not production. `taiwan-exam` is the stronger tree (`593` files, `129` commits in `30` d, `89` tests) but depends on **`PyMuPDF`, `AGPL-3.0`-or-Artifex-commercial**, so the `MIT` root does not reach the closure (`ACTION JR`). Swap for `pypdf` — already in the same `requirements.txt` — or buy the commercial limb BEFORE routing** |
| 🔴 **Education ERP / SIS** | [**openeducat_erp**](https://github.com/openeducat/openeducat_erp) *(`LGPL-3.0`)* on [**odoo/odoo**](https://github.com/odoo/odoo) *(`LGPL-3.0`)*, or [**frappe/erpnext**](https://github.com/frappe/erpnext) *(`GPL-3.0`)* | 🔴 **copyleft — no permissive option exists** | 🔴 **CARRIED, TWELFTH pass with no `MIT`/`Apache` education ERP. Its vendor-stated OneRoster / Ed-Fi / LTI 1.3 support is ABSENT from the open tree (`T162`)** |
| 🔴 **Full-stack MOOC platform** | [**openedx/edx-platform**](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | 🟢 **CARRIED unchanged. The RPC carve-out is a LICENSOR statement, not counsel (`gap 107`) — flag it as such in any deck** |
| 🔴 **LMS, mass-market copyleft** | [**moodle/moodle**](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** *(at `COPYING.txt`, not `LICENSE`)* | 🟢 **CARRIED unchanged. `88` grant documents, corrected down from `193` — `105` were PHP source files (`T223`)** |
| 🔴 **LMS, plain copyleft — second option** | [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`GPL-3.0`** | 🟢 **CARRIED unchanged. The cleanest inner grant surface of any copyleft LMS here — `2` bodies against `Moodle`'s `88`. Strong built-in exam/assessment tooling** |
| 🟡 **SIS, active** | [**RosarioSIS**](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** | 🟢 **CARRIED unchanged. Still the most active SIS this KB holds** |
| 🟡 **SIS, active** | [**openSIS-Classic**](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** *(NOT at the root)* | 🟢 **CARRIED unchanged. No root grant file, confirmed twice. The bundled CKEditor grants remain unread** |
| 🔴 **SIS, PERMISSIVE** | 🔴 **none exists** | — | 🔴 **TWELFTH pass. 🆕 And the re-test is now honest about its own denominator: the sweep that keeps returning nothing was `topic:ai-education`, which `1` of this KB's `12` shelf rows carries. `topic:education` is `~8.2k` repositories and has NOT been swept for an SIS (`T255`, `gap 125`). `Fedena` stays settled-and-abandoned (`T212`)** |
| 🔴 **LMS, corporate training** | [**Forma LMS**](https://github.com/formalms/formalms) | 🔴 **`GPL-2.0`** *(at `html/license.txt`; NO root grant)* | 🔴 **CARRIED as REFUTED. A secondary source calls it *"Apache 2.0"*; its body is the GNU `GPL` v`2` verbatim, shipped in `9` languages with nothing naming which governs (`gap 116`)** |
| 🔴 **Learning-record plumbing** | 🔴 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | 🟢 `Apache-2.0` *(`11 357` B)* | 🔴 **DELIBERATELY NOT ROUTED, fourth pass. Last commit `2026-02-26`, `Django<4.0` (EOL April `2024`), `0` matches for `xapi`/`caliper`/`statement`. Vendor the idea, do not ship the package. 🆕 **And `ACTION JV` puts a number on why this call was right: `25.2%` of the *"active"* population is unpushed for `90` days (`T242`)** |

🟢 **Permissive routes available: `6` of `16` needs** — institutional LMS, offline LMS, AI-native
LMS, rostering, credentials, SCORM. 🟡 **`1` permissive-with-a-caveat:** assessment generation.
🔴 **`5` copyleft-only.** 🔴 **`1` need with NO option at all: a permissive SIS** — and p173 is the
first pass to say that verdict rests on a denominator it has now measured as `~61×` too small.

### 🆕 🟢 The one line in the `Sakai` engagement that changes

| | |
|---|---|
| 🔴 **what p170–p172 would have said** | 🔴 ***"A scanner reports `34` BSD files in `licenses/`."*** |
| 🟢 **what p173 says** | 🟢 ***"`25` of those `34` are the Apache Software License 1.1, not BSD. `Apache-1.1` carries the same redistribution grant as BSD plus clause `3`: the end-user documentation must say 'This product includes software developed by the Apache Software Foundation'. That is an attribution line in the deliverable, not a permission problem."*** |
| 🟢 **why the correction is safe to state** | 🟢 **Both families are permissive and OSI, so no commercial verdict moves. `0` of the manifest's bodies withhold commercial use — the problems remain the `8` proprietary Sun click-through paths and the `3` stale component files, both unchanged from `ACTION JO`** |

🟡 **And the liveness bar used on every row above is now known to be loose.** `ACTION JV` measured
the `180`-day *"active"* bar admitting `25.2%` of repositories unpushed for `90` days. **For a
routing decision, read the COMMIT date** — `git clone --depth 1 --filter=blob:none --no-checkout`
then `git log -1 --format=%cI`, no API needed. The `5` rows sampled that way this pass committed
`0`, `1`, `3`, `4` and `22` days before p173.
## Pass 172 — 2026-10-13

🆕 🔴 **The `Sakai` row changes, and it is the only row whose STATUS this pass moves. p171 routed it
with *"inner audit now classified, `0` hostile"*. p172 read the manifest end to end: `8` of its
`86` paths are proprietary click-through agreements — Sun Binary Code Licenses, Sun Specification
licences and one single-seat licence. The `0` was a phrase test looking for the wrong word
(`T231`).**
🆕 🟢 **Two rows get their REGION placed for the first time: `mentingo` is **EMEA** (Selleo, Poland)
and this file's `Kolibri` low-bandwidth claim now has an APAC-placed sibling on the agent shelf.**
🆕 🟢 **One row is ADDED — the assessment/exam-generation route, which `T229` showed this KB had
never catalogued despite permissive candidates existing.**
🟢 **The routing table below RE-STATES EVERY ROW, per `P170-C`/`T216`: under *"only the newest block
is canonical"* a row not re-stated is lost however true it remains below.**

### 🟢 THE ROUTING TABLE — re-stated in full at p172

| need | route | licence *(body read)* | status at p172 |
|---|---|---|---|
| 🟢 **LMS, permissive — institutional** | [**OpenOLAT**](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** *(§`1`–`9` verbatim, `10 982` B)* | 🟢 **CARRIED. `QTI`, `SCORM`, curriculum and assessment built in. Carry the `2` attribution statements** |
| 🟢 **LMS, permissive — offline / low-connectivity** | [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** | 🟢 **CARRIED, HEAD `5d47c94a8ecc` unchanged. The LATAM and APAC low-bandwidth row** |
| 🟡 **LMS, permissive — Java institutional, patent limb** | [**Sakai**](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** *(root)* | 🆕 🔴 **CARRIED WITH A THIRD FLAG. Narrowed patent grant (`T200`); fails `mentingo`'s own licence gate (`T208`); and 🔴 **`8` of the `86` paths in `licenses/` are NOT open-source grants** (`ACTION JO`). HEAD moved TWICE today → `ad60834ff1f8`** |
| 🟢 **LMS, permissive — AI-native / corporate L&D** | [**Selleo/mentingo**](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** *(`1 062` B)* | 🆕 🟢 **CARRIED, REGION PLACED → **EMEA** (Selleo, Poland; Polish prose still in the `README`). `SCORM` import AND export, `119` `SCORM` paths. Ships `licenses.config.yaml`, the gate to LIFT** |
| 🟢 **Rostering, permissive** | [**Ed-Fi-Alliance-OSS/edfi-oneroster**](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`** *(`10 173` B)* | 🟢 **CARRIED. `OneRoster 1.2`, `24` GETs over `12` entities, `0` write routes. The only permissive rostering route this KB has verified** |
| 🟢 **Portable credentials — Open Badges `3.0` authoring** | [**opensalt/OB3DefinitionWidget**](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **`MIT`** *(`1 080` B)* | 🟢 **CARRIED. Pair with `OpenOLAT`'s `OB2` module — which is `2.0` ONLY, no W3C VC** |
| 🟢 **SCORM / AICC / xAPI interop** | [**jcputney/scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 **CARRIED, HEAD `882f3b8c7498` unchanged. The only row where grant-named paths and grant bodies agree exactly** |
| 🆕 🟡 **Assessment / exam generation, permissive** | 🆕 🟡 [**niansia/taiwan-exam**](https://github.com/niansia/taiwan-exam) *(`MIT`, APAC)* or 🆕 🟡 [**jeliael/fakao-ai-exam-engine**](https://github.com/jeliael/fakao-ai-exam-engine) *(`MIT`, APAC)* | 🟡 **`MIT` root, with a dependency caveat** | 🆕 🔴 **NEW ROW, routed as CANDIDATE not PRODUCTION. `taiwan-exam` is the stronger tree (`593` files, `129` commits in `30` d, `89` tests) but depends on **`PyMuPDF`, which is `AGPL-3.0`-or-Artifex-commercial** — so the `MIT` root does not reach the whole closure (`ACTION JR`). Swap `PyMuPDF` for `pypdf` (already a dependency) or buy the commercial limb BEFORE routing** |
| 🔴 **Education ERP / SIS** | [**openeducat_erp**](https://github.com/openeducat/openeducat_erp) *(`LGPL-3.0`)* on [**odoo/odoo**](https://github.com/odoo/odoo) *(`LGPL-3.0`)*, or [**frappe/erpnext**](https://github.com/frappe/erpnext) *(`GPL-3.0`)* | 🔴 **copyleft — no permissive option exists** | 🔴 **CARRIED, ELEVENTH pass with no `MIT`/`Apache` education ERP. `openeducat` HEAD moved → `46a5d7d40082`, its first movement this KB has recorded. Its vendor-stated OneRoster / Ed-Fi / LTI 1.3 support is ABSENT from the open tree (`T162`)** |
| 🔴 **Full-stack MOOC platform** | [**openedx/edx-platform**](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | 🟢 **CARRIED. The RPC carve-out is a LICENSOR statement, not counsel (`gap 107`) — flag it as such in any deck** |
| 🔴 **LMS, mass-market copyleft** | [**moodle/moodle**](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** *(at `COPYING.txt`, not `LICENSE`)* | 🟢 **CARRIED, HEAD `f20534726a59` unchanged. `88` grant documents, corrected down from `193` — `105` were PHP source files (`T223`)** |
| 🔴 **LMS, plain copyleft — second option** | [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`GPL-3.0`** | 🟢 **CARRIED. The cleanest inner grant surface of any copyleft LMS here — `2` bodies against `Moodle`'s `88`. Strong built-in exam/assessment tooling, which matters now that the assessment row exists** |
| 🟡 **SIS, active** | [**RosarioSIS**](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** | 🟢 **CARRIED. Still the most active SIS this KB holds** |
| 🟡 **SIS, active** | [**openSIS-Classic**](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** *(NOT at the root)* | 🟢 **CARRIED. No root grant file, confirmed twice. The bundled CKEditor grants remain unread** |
| 🔴 **SIS, PERMISSIVE** | 🔴 **none exists** | — | 🔴 **ELEVENTH pass. Re-tested this pass against the same `485`-repository topic sweep, now with its query strings recorded and reproduced (`ACTION JS`). `Fedena` stays settled-and-abandoned (`T212`) despite secondary sources still listing it as `Apache-2.0`** |
| 🔴 **LMS, corporate training** | [**Forma LMS**](https://github.com/formalms/formalms) | 🔴 **`GPL-2.0`** *(at `html/license.txt`; NO root grant)* | 🔴 **CARRIED as REFUTED. A secondary source calls it *"Apache 2.0"*; its body is the GNU `GPL` v`2` verbatim, shipped in `9` languages with nothing naming which governs (`gap 116`)** |
| 🔴 **Learning-record plumbing** | 🔴 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | 🟢 `Apache-2.0` *(`11 357` B)* | 🔴 **DELIBERATELY NOT ROUTED, third pass. Last commit `2026-02-26`, `Django<4.0` (EOL April `2024`), `0` matches for `xapi`/`caliper`/`statement`. Vendor the idea, do not ship the package** |

🟢 **Permissive routes available: `6` of `16` needs — institutional LMS, offline LMS, AI-native LMS,
rostering, credentials, SCORM.** 🟡 **`1` permissive-with-a-caveat: assessment generation.**
🔴 **`5` copyleft-only.** 🔴 **`1` need with NO option at all: a permissive SIS.**

### 🆕 🔴 What `ACTION JO` changes for a `Sakai` engagement

🟡 **Say this in the engagement, and say it in this order:**

| | |
|---|---|
| 🟢 **`Sakai`'s OWN grant** | 🟢 **`ECL-2.0`, clean — an `Apache-2.0` variant whose patent grant is narrowed to the licensor's own contributions. Buildable** |
| 🔴 **what a reviewer will find in `licenses/`** | 🔴 **`8` paths that are proprietary agreements: `activation`, `jta`, `jdbc2_0-stdext` (Sun Binary Code License — one archival copy, no modification, and `jta` says *"internal use only … for which the corresponding fee has been paid"*), `servlet` (Sun Entitlement), `jsf-api`, `jsf-impl`, `standard` (Sun Specification click-through), `java2html` (single seat)** |
| 🟡 **what that does NOT prove** | 🟡 **These are 2005-era manifest files for components `Sakai` may no longer ship. The finding is about the MANIFEST a reviewer reads, not a demonstrated proprietary jar in today's build. p172 did not check the build, and says so** |
| 🔴 **the self-contradiction to expect a question about** | 🔴 **`servlet.license.txt` carries Sun's proprietary Entitlement while `jsp-api.license.txt` — sibling API, same upstream, same directory — carries `Apache-2.0`. The servlet API as Tomcat ships it IS `Apache-2.0`** |
| 🔴 **the scanner-output correction** | 🔴 **A tool reporting *"34 BSD"* over this tree is reporting `25` **`Apache-1.1`** files as BSD (`T232`). `Apache-1.1` carries an attribution clause BSD does not** |
| 🟢 **the reassuring part, which is still true** | 🟢 **`0` of the manifest's bodies withhold COMMERCIAL use. The problem is redistribution and modification on eight paths, not commercial use anywhere** |

### 🆕 🟡 The assessment row, and why it is a candidate rather than a route

🔴 **This KB routed tutoring, authoring, rostering, credentials and packaging, and never routed
ASSESSMENT — while `4` of p171's `5` new finds were assessment tools. The hole was in the catalogue.**
🟡 **But the strongest candidate does not route cleanly, and the reason is one line in a
`requirements.txt`:**

| | |
|---|---|
| 🟢 **root grant** | 🟢 **`MIT`, `1 063` B, body read** |
| 🔴 **the closure** | 🔴 **`PyMuPDF` — PyPI metadata reads *"Dual Licensed - GNU AFFERO GPL 3.0 or Artifex Commercial License"*. An `AGPL` dependency under an `MIT` root** |
| 🟢 **the fix, and it is cheap** | 🟢 **`pypdf` (`BSD-3-Clause`) is ALREADY in the same `requirements.txt`. The `AGPL` limb is `PyMuPDF`'s rendering path, not its parsing path** |
| 🟢 **what the project itself discloses** | 🟢 **Its `references/attribution-and-forks.md` states that *"third-party examination papers, literary passages, photographs and fonts remain separately governed and are not licensed by this project's MIT declaration."* It carves out its DATA layer honestly and in writing** |
| 🔴 **what it does NOT disclose** | 🔴 **the `AGPL` dependency. A project can be scrupulous about one layer and silent about another, and `ACTION JR` found exactly that** |

🔵 **Contrast with `penecho` (`T207`), where the root grant itself was the trap. Here the root grant
is clean and honest, the DATA carve-out is volunteered, and the risk is one transitive dependency.
Those need different conversations and this KB should stop calling both *"licence risk"*.**
## Pass 171 — 2026-10-13

🆕 🔴 **`ACTION JM`'s falsifier FIRED, and `T216` is not one omission — it is SIX. Besides
`OpenOLAT`, which p170 restored, six repositories were routed by an earlier pass and are absent from
the newest routing table. `T216` is SYSTEMIC in this file, and `P170-C` is necessary.**
🆕 🟢 **The remedy is this block: the routing table below RE-STATES every row, because under
*"only the newest block is canonical"* a row not re-stated is lost however true it remains below.**
🆕 🟢 **One of the six is a DELIBERATE removal and is NOT restored — which is precisely why
`P170-C` reports and never auto-fixes.**
[`evidence/routing-table-lost-rows.2026-10-13-p171.tsv`](../evidence/routing-table-lost-rows.2026-10-13-p171.tsv)

### 🆕 🟢 THE ROUTING TABLE — re-stated in full, every licence a BODY READ

| need | route | licence *(body read)* | grant bodies | status at p171 |
|---|---|---|---|---|
| 🟢 **LMS, permissive — institutional** | [**OpenOLAT**](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** *(§`1`–`9` verbatim, `10 982` B)* | `154` name matches | 🟢 **CARRIED from p170. `QTI`, `SCORM`, curriculum and assessment built in. Carry the `2` attribution statements** |
| 🟢 **LMS, permissive — offline / low-connectivity** | [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** | 🟢 **`6`** of `11` | 🟢 **CARRIED. The LATAM and APAC low-bandwidth row** |
| 🟡 **LMS, permissive — Java institutional, patent limb** | [**Sakai**](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** | 🟡 **`129`** *(`72` blobs, `0` hostile)* | 🟡 **CARRIED with both flags: narrowed patent grant (`T200`) and it FAILS `mentingo`'s own licence gate (`T208`). Inner audit now classified, `0` hostile** |
| 🆕 🟢 **LMS, permissive — AI-native / corporate L&D** | 🆕 🟢 [**Selleo/mentingo**](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** *(`1 062` B)* | `3` + `6` | 🆕 🟢 **RESTORED (`ACTION JM`). `SCORM` is import AND export — `4` import endpoints, a resumable-upload service, an import worker, `119` `SCORM` paths. Ships `licenses.config.yaml`, the gate to LIFT** |
| 🆕 🟢 **Rostering, permissive** | 🆕 🟢 [**Ed-Fi-Alliance-OSS/edfi-oneroster**](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`** *(`10 173` B)* | n/a | 🆕 🟢 **RESTORED. `OneRoster 1.2`, `24` GETs over `12` entities, per-scope auth, `0` write routes in the tree. The only permissive rostering route this KB has verified** |
| 🆕 🟢 **Portable credentials — Open Badges `3.0` authoring** | 🆕 🟢 [**opensalt/OB3DefinitionWidget**](https://github.com/opensalt/OB3DefinitionWidget) | 🟢 **`MIT`** *(`1 080` B)* | `1` | 🆕 🟢 **RESTORED. The only clean permissive active row in the Open Badges topic, and the `v3` half of `P159-A`. Pair with `OpenOLAT`'s `OB2` module — which is `2.0` ONLY, no W3C VC** |
| 🟢 **SCORM / AICC interop** | [**jcputney/scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 **`1`** of `1` | 🟢 **CARRIED. `SCORM 1.2` / `2004` + `AICC`. The only row where grant-named paths and grant bodies agree exactly** |
| 🔴 **Education ERP / SIS** | 🆕 🔴 [**openeducat_erp**](https://github.com/openeducat/openeducat_erp) *(`LGPL-3.0`)* on 🆕 🔴 [**odoo/odoo**](https://github.com/odoo/odoo) *(`LGPL-3.0`)*, or 🆕 🔴 [**frappe/erpnext**](https://github.com/frappe/erpnext) *(`GPL-3.0`)* | 🔴 **copyleft — no permissive option exists** | `1` of `15` *(`openeducat`)* | 🆕 🔴 **RESTORED, all three, as the COPYLEFT-ONLY row. TENTH pass with no `MIT`/`Apache` education ERP, now tested against a `485`-repository topic sweep. Dropping this row HID the finding rather than stating it** |
| 🔴 **Full-stack MOOC platform** | [**openedx/edx-platform**](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | 🟡 **`15`** of `27` | 🟢 **CARRIED. The RPC carve-out is a LICENSOR statement, not counsel (`gap 107`) — flag it as such in any deck** |
| 🔴 **LMS, mass-market copyleft** | [**moodle/moodle**](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** *(at `COPYING.txt`, not `LICENSE`)* | 🆕 🔴 **`88` documents** *(was published as `193`)* | 🆕 🟡 **CARRIED, COUNT CORRECTED. `105` of the `193` were PHP source files, not grants (`T223`)** |
| 🔴 **LMS, plain copyleft — second option** | [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`GPL-3.0`** | 🟢 **`2`** of `7` | 🆕 🟢 **RE-STATED (`ACTION JM`, caught by `P170-C` against p171's OWN first draft). The cleanest inner grant surface of any copyleft LMS here — `2` bodies against `Moodle`'s `88`** |
| 🟡 **SIS, active** | [**RosarioSIS**](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** | 🟡 **`11`** | 🆕 🟢 **RE-STATED. Still the most active SIS this KB holds — HEAD was `1` d old at p170** |
| 🟡 **SIS, active** | [**openSIS-Classic**](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** *(NOT at the root)* | 🟡 **`22`** | 🆕 🟢 **RE-STATED. No root grant file, confirmed twice. The bundled CKEditor grants remain unread** |
| 🔴 **SIS, PERMISSIVE** | 🔴 **none exists** | — | — | 🔴 **TENTH pass. Tested this pass against a `485`-repository topic sweep (`ACTION JN`) as well as the usual queries. `Fedena` stays settled-and-abandoned (`T212`); `Forma LMS` was p170's candidate and is `GPL-2.0`** |
| 🔴 **LMS, corporate training** | [**Forma LMS**](https://github.com/formalms/formalms) | 🔴 **`GPL-2.0`** *(at `html/license.txt`; NO root grant)* | — | 🔴 **CARRIED as REFUTED. A secondary source calls it *"Apache 2.0"*; its body is the GNU `GPL` v`2` verbatim, shipped in `9` languages with nothing naming which governs (`gap 116`)** |

### 🆕 🔴 The one row p171 did NOT restore, and why that matters more than the five it did

| | |
|---|---|
| 🔴 **the row** | 🔴 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) — `Apache-2.0`, `11 357` B, routed by an earlier pass as *"learning-record plumbing"*, then as *"metadata cataloguing"* |
| 🔴 **why it was dropped** | 🔴 **p169 MEASURED it stale: last commit `2026-02-26` (a README edit), `Django<4.0` (EOL April `2024`), `0` matches for `xapi`, `caliper` or `statement`, and its `openlxp-xsr-aws` sibling does not resolve** |
| 🟢 **p171's call** | 🟢 **DO NOT RESTORE. p169's verdict — *"vendor the V-T-V-L idea, do not ship the package"* — stands** |

🔵 **A gate that had *"corrected"* this row back onto the routing table would have re-recommended a
package this KB's own measurement calls abandoned. `P170-C` reports; a human decides. Five RESTORE,
one DELIBERATE, and the call is recorded either way.**

### 🆕 🟡 What the classified inner audit changes for a platform engagement

🟢 **`ACTION JK` closes `gap 115` on the procedural side: `217` third-party grant documents across
the two leading institutional LMSes, `12` families, and `0` that withhold commercial use or
redistribution.**

| | `Sakai` | `Moodle` |
|---|---|---|
| 🟢 **grant DOCUMENTS** | 🟢 **`129`** *(`72` distinct blobs)* | 🆕 🟡 **`88`** *(`80` distinct blobs)* |
| 🔴 **source files miscounted as grants** | 🟢 **`0`** | 🔴 **`105`** |
| 🟢 **families** | 🟢 **`BSD` `29`, `Apache-2.0` `21`, `ECL-2.0` `10`, `MIT` `7`, `LGPL` `2`, `IPL-1.0` `1`, `2` multi-family** | 🟢 **`MIT` `47`, `BSD` `12`, `Apache-2.0` `8`, `LGPL` `3`, `GPL` `2`, `6` multi-family** |
| 🟢 **withholding commercial use** | 🟢 **`0`** | 🟢 **`0`** |

🔴 **The number to quote a client is `Moodle` `88`, not `193` — and then warn them their scanner will
report something closer to `193`, because `105` Moodle PHP files carry a GPL header and live under
filenames containing *"license"* (`gap 118`). That is a review-cost hazard, not a legal one, and it
is now sized before anyone bills for it.**
🆕 🟡 **New caution on `Sakai`, and it is small but real: its `licenses/` directory is a MANIFEST and
it MISLABELS at least `3` components. `aopalliance.license.txt` and `dnsjava-1.2.3.license.txt` both
carry the `LGPL-2.1` text, but AOP Alliance is public domain upstream and dnsjava is `BSD`;
`junit-3.8.1.license.txt` carries `IPL-1.0` where JUnit `3.8.1` shipped under `CPL-1.0`. Do not use
that directory as a per-component attribution map (`gap 117`, `ACTION JO`).**
## Pass 170 — 2026-10-13

🆕 🔴 **The permissive LMS route is THREE, not two — and the third was already verified by this KB,
in this file, `32` passes ago. `verticals/solutions.md:784` carries `OpenOLAT` as `Apache-2.0` at
`10 982` B and calls it *"the cleanest fork target of any LMS on this shelf"*. p169's routing table,
`745` lines above it, says the permissive route is *"exactly two"*. Same file, two blocks,
contradicting each other (`T216`).**
🆕 🟢 **p170 re-measured `OpenOLAT` from scratch without consulting that block: `10 982` B, sections
`1`–`9` of `Apache-2.0` VERBATIM, appendix replaced by two attribution statements that add no term.
The byte count matches to the byte, `32` passes apart.**
🆕 🔴 **And a candidate was REFUTED before it could enter: a secondary source calls `Forma LMS`
*"Apache 2.0"*. Its grant is the GNU `GPL` version `2`, verbatim, at `html/license.txt`. There is no
root grant file at all.**
🆕 🟢 **`ACTION JH` DISCHARGED: `7` of `7` platform root verdicts reproduce under the folded,
tree-wide gate. The licence COLUMN survives; what it DESCRIBES does not — `Sakai` carries `129` grant
bodies and `Moodle` `193` where this page prints one cell.**
[`evidence/permissive-lms-candidates.2026-10-13-p170.tsv`](../evidence/permissive-lms-candidates.2026-10-13-p170.tsv)
[`evidence/platform-tree-grants.2026-10-13-p170.tsv`](../evidence/platform-tree-grants.2026-10-13-p170.tsv)
[`evidence/name-vs-body-divergence.2026-10-13-p170.tsv`](../evidence/name-vs-body-divergence.2026-10-13-p170.tsv)

### 🆕 🔴 `T216` — a verified row fell off the routing table and stayed verified elsewhere

🟢 **Both statements below are in `verticals/solutions.md` right now, and both are this KB's own:**

| line | block | what it says |
|---|---|---|
| 🔴 **`39`, `49`** | 🔴 **p169's routing table — the CURRENT one** | 🔴 ***"LMS, permissive → Sakai · Kolibri"*** and ***"still exactly two"*** |
| 🟢 **`784`** | 🟢 **an earlier pass's block** | 🟢 ***"`OpenOLAT` · `Apache-2.0` (`10 982` B) · Full institutional LMS, permissive, with a patent grant · the cleanest fork target of any LMS on this shelf"*** |

🔵 **Nobody deleted anything and nobody lied. The append-only convention means each pass writes a
fresh block, and a row a pass does not RE-STATE silently leaves the current view while remaining true
in the history below.** 🔴 **That is not a cosmetic defect: a client engagement reading the top of
this page is told its permissive options are `Sakai` (which has a known patent limb, `T200`, and a
known gate problem, `T208`) and `Kolibri` (which is not an institutional LMS) — when a clean
`Apache-2.0` Java LMS with `QTI`, `SCORM` and assessment built in was verified and is one day old.**
🟢 **`T216` and `gap 112` are ONE defect from two sides. The region gate's amendment (`ACTION JF`)
establishes that only the newest block is canonical; the moment that is true, every row not re-stated
is LOST. The gate made the convention's cost measurable.**
🟢 **Pre-registered as `ACTION JM`: is the LMS route the only shelf this has happened to?**

### 🆕 🟢 `OpenOLAT` verified from scratch — and why the appendix swap is not a defect

| probe | measurement |
|---|---|
| 🟢 **HEAD** | 🟢 **`e4be14f0d1bb`, `2026-10-12` — `1` day old** |
| 🟢 **root grant** | 🟢 **`LICENSE`, `10 982` B, blob `e8870c0f5f52`** |
| 🟢 **folded word-diff vs canonical `Apache-2.0`** | 🟡 **`90` added / `159` removed — and EVERY hunk at or after word `1410`** |
| 🟢 **operative sections `1`–`9`** | 🟢 **IDENTICAL to canonical, `0` deviations** |
| 🟡 **what replaces `END OF TERMS` + `APPENDIX`** | 🟡 **two ATTRIBUTION statements: the original OLAT base at the University of Zurich, and openolat.org initiated by frentix GmbH** |
| 🟢 **second grant surface** | 🟢 **`NOTICE.TXT` — independently states *"Licensed under the Apache License, Version 2.0"* and names the holders** |

🔵 **Read correctly: this is the GOOD case, and it is worth stating plainly because `8` of the `26`
bodies this KB has read deviate from what they are published as and most of those deviations are
hazards. Here the deviation is `0` in the operative text and the replacement adds no obligation
beyond preserving notices — which `Apache-2.0` §`4` already requires.**
🟢 **The only real duty it creates: carry both attribution statements into any redistribution.**
🔴 **The one caution: because the body is not byte-identical to canonical `Apache-2.0`, a
hash-matching scanner will flag it — the same operational, non-legal risk as `T206`.**

### 🆕 🔴 `Forma LMS` — REFUTED, and the shape of the refutation is the lesson

| | |
|---|---|
| 🔴 **what a secondary source said** | 🔴 ***"Forma LMS, a fork of Docebo, is Apache 2.0 and aimed at corporate training"*** |
| 🟡 **root grant file** | 🔴 **NONE at ROOT** — `formalms/formalms` has no `LICENSE`, `LICENCE`, `COPYING` or `NOTICE` there. 🟢 **The `GPL-2.0` body is at `html/license.txt`** *(`18 346` B, p215)* <!--corrected--> |
| 🟢 **where the grant actually is** | 🟢 **`html/license.txt`, `18 346` B** |
| 🔴 **what it actually is** | 🔴 **`GNU GENERAL PUBLIC LICENSE Version 2, June 1991` — verbatim. `5` occurrences of the GPL title, `0` of *"Apache"*** |
| 🟡 **HEAD** | 🟡 **`446a77a9b9cb`, `2026-07-17` — `88` days** |

🟡 **A second finding in the same tree, recorded because it is a hazard this KB has not seen before:
`Forma LMS` ships its licence in NINE languages under `html/lib/System/license/` — english, spanish,
portuguese, italian, german, french, croatian, bosnian, tamil.** 🔴 **Nothing in the tree states which
language GOVERNS.** 🔵 **For a LATAM or EMEA engagement that looks like a convenience and is a
question: a translated copyleft licence is not a second licence, and a client's counsel will want the
English text named as controlling.**
🟢 **Caught BEFORE the shelf, which is the point. The permissive-SIS hole has been re-searched for
eight passes; this pass the query finally returned new names, and testing them cost two treeless
clones.**

### 🆕 🟢 Platform routing — corrected, with `OpenOLAT` restored and grant surfaces counted

| need | route | licence | grant bodies *(tree-wide)* | status |
|---|---|---|---|---|
| 🆕 🟢 **LMS, permissive — institutional** | 🆕 🟢 [**OpenOLAT**](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0`** *(§`1`–`9` verbatim)* | 🔴 **`154` name matches** | 🆕 🟢 **RESTORED (`T216`). HEAD `1` d. `QTI`, `SCORM`, curriculum and assessment built in. Carry the `2` attribution statements** |
| 🟢 **LMS, permissive** | 🟡 [**Sakai**](https://github.com/sakaiproject/sakai) · [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 `ECL-2.0` · 🟢 `MIT` | 🔴 **`129`** · 🟡 **`6`** | 🟡 **`Sakai` keeps its gate problem (`T208`) and patent limb (`T200`) — now with `129` inner grants measured** |
| 🟢 **LMS, behind an API boundary** | 🟢 [**Open edX**](https://github.com/openedx/edx-platform) | 🔴 `AGPL-3.0` | 🟡 **`15`** | 🟢 **unchanged — the RPC carve-out, `gap 107` stands** |
| 🟢 **LMS, plain copyleft** | 🟢 [**Moodle**](https://github.com/moodle/moodle) · [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 `GPL-3.0` | 🔴 **`193`** · 🟢 **`2`** | 🟢 **root verdicts reproduce. `Moodle` has the largest inner grant surface on this shelf** |
| 🆕 🔴 **LMS, corporate training** | 🆕 🔴 [**Forma LMS**](https://github.com/formalms/formalms) | 🔴 **`GPL-2.0`** *(at `html/license.txt`, no root grant)* | — | 🆕 🔴 **NEW ROW, REFUTED as permissive. A source called it `Apache-2.0`; the artifact is `GPL-2.0` verbatim. Licence shipped in `9` languages, none named as governing** |
| 🟡 **SIS, active** | 🟡 [**RosarioSIS**](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** | 🟡 **`11`** | 🟢 **re-verified — HEAD `2026-10-12`, `1` d. Still the most active SIS this KB holds** |
| 🟡 **SIS, active** | 🟡 [**openSIS-Classic**](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** *(not at the root)* | 🟡 **`22`** | 🟢 **re-verified — HEAD `2026-10-05`. NO root grant file, confirming p169. `gap 112`'s CKEditor grants still unread** |
| 🟡 **SIS / education ERP, weak copyleft** | 🟡 [**OpenEduCat**](https://github.com/openeducat/openeducat_erp) | 🟡 `LGPL-3.0` | 🟢 **`1`** | 🟢 **p169's `gap 109` finding VINDICATED by a second instrument: `15` name matches, `1` body, the other `14` an icon** |
| 🔴 **SIS, PERMISSIVE** | 🔴 **none** | — | — | 🔴 **NINTH pass. `Fedena` stays settled-and-abandoned (`T212`); `Forma LMS` was this pass's candidate and is `GPL-2.0`** |
| 🟢 **SCORM `2004` export** | 🟢 [**scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | 🟢 **`1`** | 🟢 **unchanged — and the ONLY row where name matches and grant bodies agree exactly** |

🟢 **The permissive LMS route is now THREE: `OpenOLAT` (`Apache-2.0`, institutional), `Sakai`
(`ECL-2.0`, with two known caveats) and `Kolibri` (`MIT`, not institutional).**
🔴 **The permissive SIS route is still EMPTY, for a ninth pass — and now with one more name tested and
refuted rather than merely re-searched.**

### 🆕 🔴 What the tree-wide count changes for a client engagement

🔵 **The honest sentence to lead with: the licence cell on this page is the OUTER grant. For `Sakai`
it describes `1` of `129` grant bodies in the tree; for `Moodle`, `1` of `193`.**
🟢 **That is not a reason to distrust the column — `7` of `7` root verdicts reproduced this pass under
a stricter instrument.** 🔴 **It is a reason to budget the inner audit as work: a client's scanner
reads all `129`, and `T213` shows that counting them by filename alone is wrong by `36` on that repo
in the over-reading direction.**
🟢 **`P170-A` is the procedure, and its step `2` is the content test that makes the count mean
something.**

## Pass 169 — 2026-10-13

🆕 🟢 **The SIS row on the platform table changes for the first time in seven passes — not because a
permissive option appeared, but because the absence is now DATED and two active copyleft routes are
verified.**
🆕 🔴 **And the licence gate a client would actually run is no longer hypothetical. `Selleo/mentingo`,
a platform this page recommends, ships one — and it would REFUSE `Sakai`, which is the permissive LMS
route this same page recommends.**
[`evidence/sis-permissive-settled.2026-10-13-p169.tsv`](../evidence/sis-permissive-settled.2026-10-13-p169.tsv)
[`evidence/agent-grant-surface.2026-10-13-p169.tsv`](../evidence/agent-grant-surface.2026-10-13-p169.tsv)

### 🆕 🔴 The gate conflict a client hits on day one, with both sides on this page

🟢 **p168 established that `Sakai` is `ECL-2.0` and that `ECL-2.0` narrows the patent grant for
institutionally employed contributors (`T200`). It then PREDICTED that no permissive allow-list would
contain `ECL-2.0`.** 🟢 **p169 found a real allow-list on this shelf and the prediction holds (`T208`).**

| | |
|---|---|
| 🟢 **the gate** | 🟢 **`Selleo/mentingo` → `licenses.config.yaml`: `19` allowed licence identifiers, `13` named package exceptions** |
| 🔴 **what it refuses** | 🔴 **`ECL-2.0` (`Sakai`) and `EPL-2.0` (`penecho`'s vendored `elkjs` layout worker) — neither is in the list** |
| 🟡 **how loose it is** | 🟡 **`3` of `19` entries are not SPDX identifiers (`Apache`, `BSD`, `Apache License 2.0`), so it matches declared STRINGS** |
| 🔴 **its own gap** | 🔴 **`licenses.comment.md`, where the reasoning belongs, is `0` bytes** |

🔵 **What to tell a client, in one sentence: your scanner will stop on `Sakai`, and the right response
is a recorded decision about `ECL-2.0`'s patent limb — not a swap to a copyleft LMS, and not a waiver
nobody read.** 🟢 **`P169-C` is that decision, pre-written.**

### 🆕 🟢 Platform routing — the SIS row, finally with dates

| need | route | licence | status |
|---|---|---|---|
| 🟢 **LMS, permissive** | 🟡 [**Sakai**](https://github.com/sakaiproject/sakai) · [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 `ECL-2.0` · 🟢 `MIT` | 🟡 **unchanged — and `Sakai` now has a known gate problem (`T208`) and a known patent limb (`T200`)** |
| 🟢 **LMS, behind an API boundary** | 🟢 [**Open edX**](https://github.com/openedx/edx-platform) | 🔴 `AGPL-3.0` | 🟢 **unchanged — the RPC carve-out, `gap 107` stands** |
| 🟢 **LMS, plain copyleft** | 🟢 [**Moodle**](https://github.com/moodle/moodle) · [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 `GPL-3.0` | 🟢 **unchanged — verbatim FSF text** |
| 🆕 🟡 **SIS, active** | 🆕 🟡 [**RosarioSIS**](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** | 🆕 🟢 **NEW ROW — HEAD `2026-10-12`, `1` day old at this pass. The most active SIS this KB has verified** |
| 🆕 🟡 **SIS, active** | 🆕 🟡 [**openSIS-Classic**](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** *(at `docs/License.txt`, not the root)* | 🆕 🟡 **NEW ROW — HEAD `2026-10-05`. Vendors `CKEditor` with its own grants, unread (`gap 112`)** |
| 🟡 **SIS / education ERP, weak copyleft** | 🟡 [**OpenEduCat**](https://github.com/openeducat/openeducat_erp) | 🟡 `LGPL-3.0` | 🆕 🟢 **IMPROVED: uniform across `14` of `14` modules, nothing vendored (`gap 109` CLOSED). `T201`'s incomplete body stands** |
| 🔴 **SIS, PERMISSIVE** | 🔴 **none** | — | 🆕 🔴 **SETTLED, not merely absent (`T212`): the web's one `Apache-2.0` answer, `Fedena`, is a real grant on abandoned code — newest commit `2016-07-20`, and no licence body in either tree** |
| 🟢 **SCORM `2004` export** | 🟢 [**scorm-again**](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | 🟢 **unchanged — `mentingo` emits `1.2` only (`gap 103`, p168)** |
| 🆕 🟡 **courseware / AI literacy** | 🟢 `P168-C` tier | 🟢 `MIT` | 🟢 **unchanged — `53` verified locales including `es` and `pt-BR`** |

🟢 **The permissive LMS route is still short and still exactly two: `Sakai` (`ECL-2.0`) and `Kolibri`
(`MIT`).** 🔴 **The permissive SIS route is still empty, for an EIGHTH pass — but for the first time
the search behind it is closed rather than pending.**

### 🆕 🔴 What `penecho` changes for a client engagement

🟢 **`penecho` is the only copyleft row on any of this KB's shelves with a NAMED commercial path
(`T207`).** 🔵 **That makes it the one `AGPL-3.0` component this page can route to for a client who
cannot accept `AGPL-3.0` — with the costs stated.**

| what the client wants to do | 🟢 safe under `AGPL-3.0-only` | 🔴 needs the commercial path |
|---|---|---|
| **run an unmodified copy internally or commercially** | 🟢 **yes — the project says so in `COMMERCIAL-LICENSE.md`** | |
| **ship it, or a derivative, inside a proprietary product** | | 🔴 **yes** |
| **run a MODIFIED copy as a network service without releasing source** | | 🔴 **yes — this is the AGPL limb** |
| **combine it with AGPL-incompatible code** | | 🔴 **yes** |
| **get support, warranty or indemnity** | | 🔴 **yes** |

🔴 **The procurement facts: terms are *"negotiated separately with the applicable PenEcho copyright
holder"*, on no published timeline; a CLA assigns contributions so the owner can keep offering the dual
licence; and the name, wordmark and logo are reserved separately from the code.**
🟡 **One sub-component is NOT under the repository default and must be handled on its own terms:
`elkjs 0.12.0` under **`EPL-2.0`**, which is also the licence `mentingo`'s gate does not allow.**


## Pass 168 — 2026-10-13

🆕 🔴 **Two cells in the platform routing table change what a client may build, and one changes what
they may CONTRIBUTE — which this page had never distinguished.**
🔴 **`mentingo`'s SCORM export is `1.2`-ONLY, hardcoded, and a `2004` package imported into it is
re-exported DECLARED as `1.2` with its sequencing silently dropped.**
🔴 **`Sakai`'s `ECL-2.0` narrows the patent grant specifically for contributors employed by an
institution or organisation — the exact shape of a university engagement.**
[`evidence/scorm-export-manifest.2026-10-13-p168.tsv`](../evidence/scorm-export-manifest.2026-10-13-p168.tsv)
[`evidence/licence-canonical-diff.2026-10-13-p168.tsv`](../evidence/licence-canonical-diff.2026-10-13-p168.tsv)

### 🆕 🔴 `gap 103` CLOSED — `mentingo` exports SCORM `1.2` only, and the import path makes it lossy

🟢 **`ACTION IY` read all `7` files of `packages/scorm-export-generator` on the raw channel
(`HTTP 200` on every one), pinned at `Selleo/mentingo` `242a9324fe48`.**
🟢 **The manifest emitter is `src/manifest-builder.ts`, `202` lines: ONE template literal, ONE
`return`, and no version parameter anywhere in the package.**

| line | emitted, verbatim | binds to |
|---|---|---|
| `:27` | `xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"` | 🔴 **IMS CP `1.1.2`** |
| `:27` | `xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"` | 🔴 **SCORM `1.2`** |
| `:29` | `<schema>ADL SCORM</schema>` | — |
| `:30` | `<schemaversion>1.2</schemaversion>` | 🔴 **HARDCODED `1.2`** |

🔴 **ABSENT from the whole package, each probed: `2004`, `adlcp_rootv1p3`, `adlseq`, `adlnav`,
`imsss`, `CAM 1.3`.** 🟢 **Without `imsss`/`adlseq`/`adlnav` no `2004` manifest can be valid, so
this is not *"`2004` untested"* — it is `2004` not emitted.**
🔴 **`ACTION IY`'s falsifier was *"refuted if the generator emits a valid `2004` manifest"*. SILENT.**

🆕 🔴 **The hazard, sharper than `gap 103` stated it.** 🟢 **p167 established that the SCORM IMPORT
pipeline is real (`4` endpoints, a tus resumable upload, a worker).** 🔴 **`renderLessonResources()`
filters `lesson.type === "scorm"` and re-emits each imported `SCO` as
`<resource type="webcontent" adlcp:scormtype="sco">` INSIDE the `1.2` manifest.**
🔴 **So: import a SCORM `2004` package, export the course, and you get a package DECLARING `1.2`
whose `2004` sequencing rules were never carried over. The round trip is lossy and nothing warns.**
🟢 **The `103` `scorm_2004` markers p166 counted are therefore the IMPORT/player side, not the
export capability — `gap 103` was asking the right question of the wrong half of the pipeline.**

| what to tell a client | 🟢 safe | 🔴 not safe |
|---|---|---|
| **export courses to an LMS that accepts SCORM `1.2`** | 🟢 **yes — this is what the generator is** | |
| **export to an LMS that requires SCORM `2004` sequencing** | | 🔴 **no. Build the `2004` manifest yourself or route via `jcputney/scorm-again`** |
| **re-export a `2004` package you imported** | | 🔴 **no — it will be declared `1.2` and lose its sequencing** |

### 🆕 🔴 Platform routing — the patent column this page never had

🟡 **Every row below was already correct on LICENCE. What is added is the CONTRIBUTION column,
because three of this page's recommended platforms carry a grant that is not what its family name
implies.**

| platform | published licence | 🆕 what the body adds | engagement consequence |
|---|---|---|---|
| 🟡 [**Sakai**](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`** *(`11 120 B`)* | 🔴 **patent grant narrowed for contributors employed by an institution or organisation (`T200`)** | 🟡 **Build on it freely. Diligence the patent limb before contributing code back from a university engagement** |
| 🔴 [**OpenEduCat**](https://github.com/openeducat/openeducat_erp) | 🟡 `LGPL-3.0` | 🔴 **the body PROMISES the `GPL-3.0` text and contains `0` of it; bundled libraries declared to be *"other GPL-compatible licenses"*, unnamed (`T201`)** | 🔴 **The outer grant is `LGPL-3.0`. Bundled components are unaudited and the grant on disk is incomplete by its own construction** |
| 🔴 [**Chamilo**](https://github.com/chamilo/chamilo-lms) | 🔴 `GPL-3.0` | 🆕 🟡 **a SECOND root grant file elects `-or-later`; both of its pointers are `404` (`T202`)** | 🟡 **More permissive than published — `-or-later`, in the file every source header cites. The contributor list it promises is unrecoverable** |
| 🟢 [**Open edX**](https://github.com/openedx/edx-platform) | 🔴 `AGPL-3.0` | 🟢 **RPC carve-out, re-confirmed by a second instrument this pass** | 🟢 **Still the one copyleft LMS usable behind an API boundary. `gap 107` stands: licensor statement, not counsel** |
| 🟢 [**OpenOLAT**](https://github.com/openolat/OpenOLAT) | 🟢 `Apache-2.0` | 🟡 **an *"Additional license statement"* replaces the `APPENDIX`** | 🟢 **Permissive. Read the statement before redistribution** |
| 🟢 [**Moodle**](https://github.com/moodle/moodle) · [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 `GPL-3.0` | 🟢 **CLEAN — verbatim FSF text, older URL revision only** | 🟢 **Plain `GPL-3.0`. No surprises in the grant** |

🟢 **The permissive LMS route is unchanged and still short: `Sakai` (`ECL-2.0`) and `Kolibri`
(`MIT`).** 🔴 **And the oldest hole on this page is unchanged for a SEVENTH pass: no SIS and no
education ERP under `MIT` or `Apache-2.0`. p168 re-ran the query on an independent sweep and the
only candidate the web named was `OpenEduCat` itself — `LGPL-3.0`, and now with `T201` against it.**

## Pass 167 — 2026-10-13

🆕 🟢 **Two cells in last pass's routing table were wrong in a way that changes what you can sell,
and both are corrected here by reading code instead of prose.**
🔴 **`mentingo`'s SCORM is not export-only — it has a full import pipeline the upstream README
itself is unsure about.** 🟢 **And `edx-platform` is AGPL-3.0 with an RPC carve-out that makes it
usable in an architecture this page would otherwise have refused.**
[`evidence/comment-guard-census.2026-10-13-p167.tsv`](../evidence/comment-guard-census.2026-10-13-p167.tsv)
[`evidence/licence-bands.2026-10-13-p167.tsv`](../evidence/licence-bands.2026-10-13-p167.tsv)
[`evidence/oneroster-endpoints.2026-10-13-p167.tsv`](../evidence/oneroster-endpoints.2026-10-13-p167.tsv)

### 🆕 🟢 Platform routing — p167 corrections

| need | platform | licence *(title-line probe, body read)* | correction this pass |
|---|---|---|---|
| 🟢 **Permissive AI-native LMS / corporate L&D** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** (`1 062 B`) | 🆕 🟢 **SCORM is import AND export: `4` import endpoints, a tus resumable-upload service, a dedicated import worker, `2` e2e specs, `119` SCORM paths. The README says export-only; the code says both** |
| 🆕 🟡 **Already-deployed MOOC platform at scale** | 🆕 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** (`35 136 B`) 🟢 **+ RPC CARVE-OUT** | 🆕 🟢 **The licence body carries an EdX Inc. addendum: a public, independently available service talking to it over RPC is NOT a derivative work, and its source is outside Corresponding Source. `P167-C`** |
| 🟢 **OneRoster rostering, permissive** | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`** (`10 173 B`) | 🆕 🟢 **`12` entities over `24` GETs, per-scope authorisation; `0` write routes in the tree** |
| 🟢 **Permissive LMS, standards-native** | [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **`Apache-2.0`** (`10 982 B`) | 🆕 🟡 **The body carries two *"Additional license statement"* attribution sections (OLAT / University of Zurich, frentix GmbH) — attribution only, no grant change** |

🔵 **Read the `edx-platform` row against this page's own history: for several passes AGPL-3.0 has
been a stop-ship (`P37`), and on the bare licence text that is right.** 🟢 **Here the licensor has
narrowed §13 in writing for exactly the service-to-service shape an AI studio builds.**
🔴 **The carve-out does NOT reach in-process code — an XBlock, a Django app, a patch or a fork is
still AGPL-3.0, and modifications to the platform itself must still be offered to users.**

### 🆕 🟢 The `mentingo` SCORM cell, in full

| capability | evidence | verdict |
|---|---|---|
| 🟢 **SCORM export** | `course-scorm-export.service.ts`, `scorm-export.types.ts`, SCORM 1.2 named in the README | 🟢 **IN-TREE** |
| 🆕 🟢 **SCORM import** | `@Post("import/init")`, `@Post("import/tus")`, `@Patch("import/tus/:packageId")`, `@Post("import/:packageId/complete")`, `scorm-import.worker.ts`, `scorm-tus-upload.service.ts` | 🆕 🟢 **IN-TREE — upstream's own docs understate it** |
| 🟢 **runtime / player** | `@Get("runtime/launch")`, `@Post("runtime/commit")`, `@Post("runtime/finish")`; player is `jcputney/scorm-again` (MIT, pinned `3.0.4`) | 🟢 **IN-TREE + MIT sibling** |
| 🔴 **SCORM 2004 parity** | `scorm_2004` markers ×`103` against a generator naming only `1.2` | 🔴 **UNESTABLISHED — `gap 103` stands, do not sell it** |
| 🔴 **xAPI / LTI 1.3** | `1` hit each, both inside one Polish HTML comment marked *"DO NOT PUBLISH WITHOUT VERIFICATION"*; `0` in code | 🔴 **ABSENT — unchanged from p166** |

🔵 **The asymmetry is the lesson: the same repository understates one standard in its docs and
over-states two others in an unpublished comment. Neither direction is discoverable from prose.**


## Pass 166 — 2026-10-13

🟢 **The routing table gains the row it has lacked since p156: OneRoster rostering on a PERMISSIVE
licence.** 🔴 **It is not a platform — it is a server you put in front of one, because `3` of the
`3` platforms this page recommends measure `0`.**
[`evidence/capability-census.2026-10-13-p166.tsv`](../evidence/capability-census.2026-10-13-p166.tsv)
[`evidence/sibling-licences.2026-10-13-p166.tsv`](../evidence/sibling-licences.2026-10-13-p166.tsv)

### 🆕 🟢 Platform routing, with OneRoster and Ed-Fi now MEASURED on all three

🔵 **Every cell below was measured with `P166-A`'s guarded grep against a pinned tree. No cell is a
vendor claim, and every sibling named carries its own licence.**

| need | platform | licence | LTI 1.3 | SCORM | xAPI | OneRoster | Ed-Fi |
|---|---|---|---|---|---|---|---|
| 🟢 **Permissive LMS, standards-native** | [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **`Apache-2.0`** | 🟢 **in-tree, `145` files / `18 067` LOC** | 🟢 **in-tree, `65` Java files** | 🔴 **ABSENT** | 🔴 **ABSENT** | 🔴 **ABSENT** |
| 🟡 **Already-deployed LMS at scale** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 **`GPL-3.0`** | 🟢 **in-tree, `423` paths** | 🟢 **in-tree, `166` paths** | 🟢 **in-tree, `99` paths** | 🟡 **SIBLING only — 🔴 `GPL-3.0`, `2 091` d stale** | 🔴 **ABSENT** |
| 🟢 **Permissive AI-native LMS / corporate L&D** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **`MIT`** | 🔴 **ABSENT** | 🟢 **in-tree + MIT player** | 🔴 **ABSENT** | 🔴 **ABSENT** | 🔴 **ABSENT** |
| 🆕 🟢 **OneRoster rostering, permissive** | 🆕 🟢 [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`** (`10 173 B`) | n/a | n/a | n/a | 🟢 **OneRoster 1.2, 🔴 ~~`14`~~ → **`24`** GET endpoints over `12` entities (`T189`, p167)** | 🟡 **Ed-Fi ODS is a separate, unmeasured decision** |

🟢 **Read the OneRoster column across the first three rows and the engagement writes itself:**
🔴 **no permissive platform on this shelf rosters, and the one copyleft platform that does, does it
through a plugin last touched in January 2021.** 🟢 **`P166-B` is the composition that fixes it.**

### 🆕 🟢 mentingo's SCORM row, CORRECTED upward — it is first-party, not just a bundled player

🔴 **This page has been carrying mentingo's SCORM as *"it DOES ship SCORM — `119` files … with a
bundled player"*, and `repos/foundations.md` recorded the player as *"an EXTERNAL npm
dependency"*.** 🟢 **Both are true and both understate it. Measured at HEAD `242a9324fe48`:**

| component | what it is | size |
|---|---|---|
| 🟢 **`@repo/scorm-export-generator`** | 🟢 **first-party, in-tree — *"Node-side SCORM 1.2 export package generator"*** | `9` files, **`585` LOC** |
| 🟢 **`@repo/scorm-export-runtime`** | 🟢 **first-party, in-tree — *"Standalone browser runtime for exported SCORM packages"*** | `9` files, **`1 381` LOC** |
| 🟢 **[`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) `3.0.4`** | 🟢 **the PLAYER, an external dependency pinned in `apps/web/package.json`** | 🟢 **`MIT`, `1 072 B`, HEAD `2026-10-09` — `3` d** |

🟢 **Standard markers in-tree: `scorm_2004` ×`103`, `SCORM 1.2` ×`58`, `cmi.core` ×`50`,
`adlcp` ×`20`, `imsmanifest` ×`8`.** 🟡 **The generator names `1.2` explicitly; the `2004` markers
are present but p166 did not establish 2004 export parity.** 🔵 **So the honest sentence for a
client is *"SCORM 1.2 export is first-party and the player is MIT"*, which is both narrower and
stronger than *"SCORM support"*.**

### 🆕 🔴 mentingo's xAPI is ABSENT — and upstream says so itself

🔴 **mentingo's whole tree returns `1` hit for `xapi` and `1` for `lti`: the SAME line,
`README.md:246`, inside an HTML comment, in Polish, reading *"STAGE 3 — to be confirmed by the
team, DO NOT PUBLISH WITHOUT VERIFICATION: … pentest, xAPI/LTI, mapping to NIS-2 / art. 8e KSC,
retention and data deletion."*** 🟢 **mentingo's actual published interoperability claim, in
English, in the body of the README, is exactly one sentence and it is accurate: *"SCORM 1.2 export,
so content authored in Mentingo can be handed to another LMS."***
🟢 **So `T127` is CONFIRMED a third time, and now EXPLAINED rather than merely measured: the
capability is absent and upstream has not claimed it.** 🔵 **This is the strongest form an absence
can take on this shelf — do not price xAPI into a mentingo engagement, and do not open an
upstream issue asking where it is.**

### 🔴 The administrative / SIS hole, confirmed again on the search channel

🔴 **p166's vertical-platform sweep returned NO student-information or ERP system under `MIT` or
`Apache-2.0`.** 🟡 **`OpenEduCat` is `LGPL-3.0`** 🔴 **· `RosarioSIS` is `GPL-2.0`** 🟡 **·
`OpenOLAT` is `Apache-2.0` but is an LMS, not an SIS** 🔴 **· `Fedena` and `openSIS` gate finance
and multi-campus behind paid tiers, and `SchoolTool` is discontinued.**
🟢 **`P9` has described this as *"the real hole"* since p132 and it is unchanged at p166.**
🔵 **Recorded as a declared gap, not as silence: the sweep ran and returned nothing, which is
different from not having looked.**

## Pass 165 — 2026-10-13

🟢 **`ACTION IM` is DISCHARGED and the routing table gains the one thing it lacked: a row that is
measured GREEN on licence and on standards simultaneously.**
[`evidence/interop-guarded-grep.2026-10-13-p165.tsv`](../evidence/interop-guarded-grep.2026-10-13-p165.tsv)

### 🆕 🟢 Platform routing, with interop MEASURED and every sibling licensed

🔵 **Every interop cell was measured with `P164-A`'s guarded grep against a pinned tree. No cell is
a vendor claim.**

| platform | licence *(body-read)* | LTI 1.3 | SCORM | xAPI | OneRoster / Ed-Fi | route here when |
|---|---|---|---|---|---|---|
| 🆕 🟢 **[`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT)** | 🟢 **`Apache-2.0`** | 🟢 **IN-TREE — `145` files, `18 067` LOC** | 🟢 **IN-TREE — `65` files** | 🔴 ABSENT | 🔴 ABSENT | 🟢 **standards interop AND a permissive licence are both required. The only row that satisfies both** |
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** | 🟡 **sibling** — `xblock-lti-consumer`, 🔴 **AGPL** | 🟡 **sibling** — `overhangio/openedx-scorm-xblock`, 🔴 **AGPL** | 🟡 **sibling** — `event-routing-backends`, 🔴 **AGPL** | 🔴 ABSENT | 🟡 **capability and scale outweigh licence, and counsel has cleared AGPL for the deployment model** |
| 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 `LGPL-3.0` | 🔴 **ABSENT** *(`T161`)* | 🔴 ABSENT | 🔴 ABSENT | 🔴 **ABSENT — vendor claim REFUTED** | 🔴 **only for its `14` ERP modules. Every integration is bespoke** |
| 🟡 Moodle | 🟡 `GPL-3.0` *(`P56`)* | 🟡 core *(spells it `ltiadvantage` — `T142`)* | 🟡 core | 🟡 core | 🟡 plugin ecosystem | 🟡 **the institution already runs it — retrofit, do not replace** |

🆕 **`T172` makes the second row a decision rather than a preference:** 🔴 **the Open edX interop
surface is `AGPL-3.0` at EVERY layer — core, each plugin, and each published PyPI package. There is
no permissive path through it.**
🔵 **Stated fairly: AGPL is a GATE, not a defect, and Open edX remains the most capable OSS LMS
here. Whether the gate binds turns on whether the client distributes or offers the platform as a
network service — their counsel's call, not this shelf's.**

🔵 **And the honest limit on the new top row:** 🔴 **OpenOLAT's `OneRoster`, `Ed-Fi` and `xAPI` are
measured ABSENT (`620` naive Ed-Fi hits, `0` real — `T170`).** 🟢 **Rostering and analytics are a
BUILD on this platform, and must be priced as one. What you get for free is the tool-integration
and content-packaging surface, which is where most integrations actually live.**

## Pass 164 — 2026-10-13

🔴 **`ACTION IJ` is REFUTED and its falsifier fired on ALL THREE limbs.** 🟢 **The routing
table's newest row — `openeducat/openeducat_erp`, added p163 on a vendor-stated interoperability
claim — is AMENDED here, exactly as the registration required.**
[`evidence/openeducat-interop-probe.2026-10-13-p164.tsv`](../evidence/openeducat-interop-probe.2026-10-13-p164.tsv)

### 🆕 🔴 `T161` — OpenEduCat's OneRoster, Ed-Fi and LTI 1.3 are NOT in the repository

🟢 **Measured at the registered tree: HEAD `1c95cef`, branch `19.0`, last commit `2026-09-07`,
`1 345` tracked paths, full content read.**

| claim | path names | file CONTENT | verdict |
|---|---|---|---|
| 🔴 **OneRoster** | `0` | 🔴 **`0`** | 🔴 **ABSENT** |
| 🔴 **Ed-Fi** | `0` | 🔴 **`0` once verified** | 🔴 **ABSENT** |
| 🔴 **LTI 1.3** | `0` once verified | 🔴 **`0` once verified** | 🔴 **ABSENT** |
| 🔴 IMS / 1EdTech, Caliper, SCORM, xAPI, Turnitin, Proctorio | `0` | `0` | 🔴 **ABSENT** |

🆕 **`T161`:** 🔴 **`0` of the three vendor-stated standards has implementing code.** 🟢 **The
p163 row said the claims were vendor-stated and registered them rather than repeating them as
fact. That was the right call, and this is the payoff.**

### 🆕 🔴 `T162` — and EVERY apparent hit was a false positive, in three distinct classes

🔵 **This is the part worth carrying to other industries, because a naive capability grep would
have CONFIRMED the vendor claim.**

| raw hit | what it actually was | class |
|---|---|---|
| 🔴 `14` path hits for `lti` | 🔴 **`facu`*`lti`*`es-icon.svg`**, the same asset in 14 modules | 🔴 **substring inside a longer word** |
| 🔴 `1` content hit for `ed-fi` | 🔴 **`requir`*`ed-fi`*`eld`** in a code comment, `openeducat_timetable/tests/test_compute_timing.py:47` | 🔴 **substring inside a longer word** |
| 🔴 `4` content hits for `lti` | 🔴 **raw bytes inside `2` PNG and `2` JPEG assets** | 🔴 **binary file matched as text** |
| 🔴 `4` content hits for `saml` | 🔴 **Danish `Samlet` (= *"total"*) ×6, `samlet` ×3, `saml` ×1 in `da_DK.po`** | 🔴 **a word in another natural language** |

🆕 **`T162`:** 🔴 **an unguarded capability grep over this repository reports `23` hits across
four standards and the true count is `0`.** 🟢 **The guard is three flags and one exclusion:
`grep -I` (skip binaries), `\b` word boundaries, and exclude `*.po` i18n catalogues.**
🔵 **Recorded as a reusable instrument because *"the repo mentions OneRoster"* is exactly the
kind of claim a client engagement inherits without checking.**

### 🟢 The one thing that would have made the claim true, tested and ABSENT

🔵 **A fair reading has to allow that the capability might live in a SIBLING repository and that
the vendor page is describing a product rather than this tree.** 🟢 **Tested with `P54`:**

| candidate | `git ls-remote --symref` |
|---|---|
| 🟢 `openeducat/openeducat_erp` | 🟢 **EXISTS** *(the row's repo)* |
| 🔴 `openeducat/openeducat_lti` · `openeducat_oneroster` · `openeducat_enterprise` · `openeducat_core` · `openeducat_lms` | 🔴 **ABSENT, all five** |

🟢 **So the capability is not in an adjacent open repository under any obvious name.**
🟡 **Stated fairly: it may still exist in OpenEduCat's commercial edition, which this shelf
cannot read and does not claim to have tested. What is settled is narrower and is what the
routing table needed — it is not in the open-source tree the row points at.**

### 🟢 The routing table, with the amended row

| the engagement… | platform | licence | grading | can grading be switched OFF? | 🆕 **rostering standards, VERIFIED** |
|---|---|---|---|---|---|
| 🟢 must NOT grade with AI | 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3.0 | 🟢 **none** — `4` actions, `0` evaluative | 🟢 **n/a** | 🟡 **LTI + Open Badges confirmed p162** |
| 🟢 may grade, must be able to STOP | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | 🔴 `essay-grading` | 🟢 **YES — flag ships `false`** | 🟡 not probed |
| 🟡 grades, wants MIT + multi-tenancy | 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 🔴 **`ai_judge`, `7` tables** | 🔴 **NO** | 🟢 **SCORM confirmed** (`scorm-again@3.0.4`) |
| 🟡 needs an education **ERP** | 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0** *(body `8 241 B`, INCOMPLETE)* | 🟢 **none AI-evaluative** | 🟢 **n/a** | 🆕 🔴 **NONE. OneRoster, Ed-Fi and LTI 1.3 all ABSENT from the tree (`T161`)** |
| 🔴 must avoid network copyleft | 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 | 🔴 `0` AI files | 🟢 **n/a** | 🟡 not probed |

🔵 **How the OpenEduCat row should now be used:** 🟡 **it remains a real, maintained,
self-hostable education ERP, and that is why it keeps its row** — 🔴 **but it is an
INTEGRATION-TARGET with no standards-based integration surface of its own, which is a materially
worse starting point than p163's row implied.** 🔴 **Combined with its copyleft licence and its
incomplete grant, it drops from 🟡 amber to 🔴 red for anything but a scoped, bespoke
integration.**

### 🟡 What this page still carries unverified

- 🟡 **OpenOLAT's and edx-platform's rostering surfaces have never been probed.** 🟢 **Registered
  as `ACTION IM` rather than left implicit** — 🔵 **the OpenEduCat result is a reason to doubt
  every unverified interoperability claim on this page, including the two this shelf has simply
  never asked about.**

## Pass 163 — 2026-10-13

🔴 **This page's routing table splits on *"does the engagement GRADE?"* and sends grading
engagements to OpenOLAT.** 🆕 🔴 **p163 adds the question that decides a regulated deployment and
that the table has never asked: *can the grading be TURNED OFF?*** 🟢 **The answer separates the
two platforms more sharply than licence does.**
[`evidence/mentingo-judge-controls.2026-10-13-p163.tsv`](../evidence/mentingo-judge-controls.2026-10-13-p163.tsv)
[`evidence/openeducat-grant.2026-10-13-p163.tsv`](../evidence/openeducat-grant.2026-10-13-p163.tsv)

### 🆕 🔴 `T157` — `mentingo` has NO off switch for its AI judge, and `enabled: false` is a provider selector

🟢 **Measured in `apps/api/src/ai/services/ai-runtime.service.ts:360-369` at HEAD `242a9324`:**

```js
async resolveSource(capability) {
  const capabilityStatus = configuration?.capabilities?.[capability];
  if (capabilityStatus?.enabled && capabilityStatus.provider === AiCapabilityProvider.Luma)
    return AI_RUNTIME_SOURCES.LUMA;
  return AI_RUNTIME_SOURCES.CORE;        // <-- enabled:false lands HERE
}
```

🔴 **Setting `AiMentorJudge.enabled = false` does not disable the judge. It routes it to the
CORE provider.** 🟢 **And `AI_RUNTIME_SOURCES` has exactly two members — `{CORE, LUMA}` — with
**no `OFF`**, so the router cannot decline to run.** 🟢 **The request path
`ai.controller.ts:152 → ai.service.ts:437 → judge.service.ts:41` carries no feature flag at all;
its only guards are `thread.status === ACTIVE` and *a rubric must exist*.**

🟡 **The one honest caveat: configuring no rubric DOES stop it** —
`BadRequestException("common.error.aiJudgeConfigurationMissing")`. 🔵 **But that is an off switch
by OMISSION, not a control an administrator can find, document or audit.**

🟢 **Contrast, and this is what the routing table needs:** 🟢 **OpenOLAT's `essay-grading` flag
SHIPS `false`** *(`T145`, p162)*. 🔴 **mentingo's judge surface is present by default and has no
deliberate way to stop it.**

### 🟢 The routing table, with the new column

| the engagement… | platform | licence | grading | 🆕 **can grading be switched OFF?** |
|---|---|---|---|---|
| 🟢 must NOT grade with AI | 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3.0 | 🟢 **none** — `4` actions, `0` evaluative | 🟢 **n/a — nothing to switch** |
| 🟢 may grade, must be able to STOP | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | 🔴 `essay-grading` | 🟢 **YES — and the flag ships `false`** |
| 🟡 grades, wants MIT + multi-tenancy | 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 🔴 **`ai_judge`, `7` tables** | 🔴 **NO — `enabled:false` re-routes, it does not disable** |
| 🟡 needs an education **ERP** (admissions, fees, library, timetable) | 🆕 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0** *(body `8 241 B`, INCOMPLETE)* | 🟢 **none AI-evaluative** | 🟢 **n/a** |
| 🔴 must avoid network copyleft | 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 | 🔴 `0` AI files | 🟢 **n/a** |

🔵 **How to read the new column in an Annex III engagement:** 🟢 **the AI Act's Article 14
oversight expectations are much easier to evidence on a platform whose evaluative feature has a
documented default-off than on one where the only way to stop it is to leave a rubric
unconfigured.** 🟢 **That makes OpenOLAT the lower-risk grading platform despite mentingo's more
permissive licence and better-designed verdict controls** — 🔵 **which is the first time on this
page that licence has NOT been the deciding field.**

### 🆕 🟡 `openeducat/openeducat_erp` — a real ERP row, and the reason it is amber not green

🟢 **Verified at source this pass, not from the vendor's pages: LGPL-3.0 read from the `LICENSE`
body (`8 241 B`, blob `ef163fea`, sha256 `528f8403…47a9`), the only licence-bearing path in
`1 345` tracked files, head `1c95cef`, last commit `2026-09-07`, default branch `19.0`.**

🟢 **What it is:** 🟢 **an Odoo-based education ERP with `14` installable modules in-tree —
`admission`, `fees`, `library`, `timetable`, `exam`, `attendance`, `classroom`, `facility`,
`parent`, `activity`, `assignment`, `core`, `erp`, plus a web theme.** 🔵 **This is the
administrative surface Moodle does not have and that UNESCO IESALC's LATAM decomposition shows is
the LEAST-adopted and most governance-relevant area** *(admin `34.1%` against teaching `73.5%`)*.

🔴 **Why amber:** 🔴 **LGPL-3.0 is copyleft, so it is an INTEGRATION target, never a fork.**
🔴 **And its grant is defective on its own terms** — the body promises the GPL text *"at the
bottom as well"* and at `8 241 B` cannot contain it, while the `COPYRIGHT` file it directs the
reader to is absent from all `1 345` paths. 🟢 **Both defects are in
[`repos/foundations.md`](../repos/foundations.md) with the measurements.**

🟡 **Its OneRoster / Ed-Fi / LTI 1.3 claims are VENDOR-STATED and unverified in the tree.**
🟢 **Registered as `ACTION IJ`, not repeated as fact.**

### 🔴 What this page still cannot do, after p163

- 🔴 **Recommend a PERMISSIVE education ERP.** 🟢 **Searched this pass; OpenEduCat (LGPL-3.0) is
  the closest real system and it is copyleft.** 🔵 **The gap is declared, not padded.**
- 🟡 **`ACTION IJ` is open on OpenEduCat's rostering standards.**
- 🟡 **The grading column now rests on two platforms read at one HEAD each.** 🔵 **Concentration
  noted.**

## Pass 162 — 2026-10-13

🔴 **One pass ago this page split its routing table on *"does the engagement GRADE?"* and sent
every grading engagement to OpenOLAT as the only open-source platform that does it.**
🔴 **That is now wrong in two ways: a MIT-licensed platform on this shelf also grades, and the
platform this page recommends for grading defends its authored content in code while defending
the graded answer with a sentence in a prompt.**
[`evidence/evaluative-tier-tri-platform.2026-10-13-p162.tsv`](../evidence/evaluative-tier-tri-platform.2026-10-13-p162.tsv)

### 🆕 🟢 The routing table, re-cut on licence × evaluative, which is the cut a client actually faces

| engagement | platform | licence *(body-read)* | why — and what changed this pass |
|---|---|---|---|
| 🟢 **Governed AI inside an existing LMS, NO grading** | 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) core AI | 🟡 **GPL-3.0** | 🟢 **UNCHANGED, and now measured twice: `4` actions, `0` evaluative, so CORE cannot be configured into Annex III.** 🆕 🔴 **But a PLUGIN can — `ACTION IE` proved an `aiplacement_*` plugin reaches `grade_update()`. The boundary is what core SHIPS, not a gate core ENFORCES.** 🔴 **Ledger keeps prompt and response forever — pair with `P161-B`** |
| 🆕 🟢 **AI that GRADES, and the client needs a PERMISSIVE licence with a patent grant** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | 🟢 **Still the strongest oversight design on the shelf: model returns signals, server computes the mark, consent modal, `3` pre-filters, `a_prompt_template_version` for re-running a contested mark, `33`-column ledger.** 🆕 🔴 **Ships with NO code-level injection guard on the student answer — close that before go-live (`P162-B`), it is a four-hour change** |
| 🆕 🟢 **AI that GRADES, and the client needs MIT and MULTI-TENANCY from day one** | 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** (`LICENSE`, 1 062 B) | 🆕 🟢 **NEW ROW. A `7`-table AI judge: author-set `passing_threshold_percent`, rubric score ANCHORS with worked examples, `passed` computed server-side, blocking errors re-verified by a second model call before they can fail a learner, `max_score_at_judgement` so editing a rubric never rewrites a past mark.** 🟢 **All `7` tables tenant-scoped with RLS — the only platform here that is multi-tenant by construction.** 🔴 **`4 753` files against Moodle's `67 589`: far less platform, so far more to build** |
| 🟢 **Content, courseware, no AI governance requirement** | 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | 🔴 **UNCHANGED and still not in the permissive tier.** 🔴 **`0` AI files — nothing to govern, and nothing to build on either** |
| 🟢 **SCORM authoring / export** | 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 🆕 🟢 **Confirmed by a second instrument this pass: `@repo/scorm-export-generator` + `@repo/scorm-export-runtime` in-tree, player `scorm-again@3.0.4` (MIT, registry-read).** 🟢 **Licence closure MIT over MIT** |

### 🆕 🔴 The question that now decides a grading engagement, and it is not the licence

🔴 **Both grading platforms keep the final verdict in server code. Neither hardens the student
answer in code.** 🟢 **So the delivery question is no longer *"which platform grades"* — two do —
but *"who owns the injection surface on the graded path"*, and on both platforms the answer today
is nobody.**

| platform | guard on AUTHOR content | guard on STUDENT answer | verdict authority |
|---|---|---|---|
| 🟢 OpenOLAT | 🟢 **`AiContentHardener`: `14` regexes, `5` HTML tags, `javascript:`, tested** | 🔴 **prompt instruction + `-----` fence only** | 🟢 server-side weighting |
| 🟢 mentingo | 🟡 **not assessed this pass** | 🟡 **not assessed this pass** | 🟢 **server sum vs author threshold, + double-verified veto** |

🔵 **This is a selling point, not a disqualification: the oversight apparatus a regulator asks
about is already built on both platforms, and the gap that remains is small, specific and
cheap — which is exactly the shape of work a studio should want to be holding.**
🔜 **mentingo's two unassessed cells are registered as `ACTION IH`.**

### 🟡 The platform inventory, carried unchanged

🟢 **Moodle, Open edX, Canvas, BigBlueButton, H5P, Kolibri, OpenEduCat, Sakai, Richie and
Tutor-CLI stand as previously recorded.** 🔴 **`OpenEduCat` is re-confirmed LGPLv3 from the
vendor's own glossary this pass — NOT MIT and NOT Apache, which the global ERP query has now
asserted six passes running** *(`T122`)*. 🔵 **It is built on Odoo, so the ERP primitives are
Odoo's and the licence question is Odoo's too.**
## Pass 161 — 2026-10-12

🔴 **This page routed *"governed AI inside an existing LMS"* to Moodle one pass ago on the
strength of a ledger only Moodle was thought to have.** 🔴 **OpenOLAT has one too, with `33`
columns to Moodle's `15` — so the row is REWRITTEN, and it now splits on the question that
actually decides it: does the engagement GRADE?**

### 🆕 🟢 The routing table, re-cut on the dimension that changed

| engagement | platform | licence *(body-read)* | why — and what changed this pass |
|---|---|---|---|
| 🆕 🟢 **Client wants governed AI inside an LMS and does NOT grade with it** | 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) core AI | 🟡 **GPL-3.0** | 🟢 **UNCHANGED recommendation, now for a stated reason: `4` actions, `0` evaluative, so core cannot be configured into the AI Act's Annex III tier.** 🟢 **Ledger keeps prompt AND response, which is what a regulator asks for.** 🔴 **And keeps them FOREVER — pair with `P161-B` or do not turn it on** |
| 🆕 🔴 **Client wants AI to GRADE free-text** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | 🆕 🔴 **The ONLY open-source platform on this shelf that ships it: `ai.feature.essay-grading.enabled`, default `false`.** 🟢 **And it is built for oversight — model returns signals only, server computes the score, student consent modal, three pre-filters, `a_prompt_template_version` for re-running a contested mark.** 🔴 **Turning the flag on is an Annex III decision, not a feature decision.** 🟢 **`P161-A`** |
| 🆕 🟢 **Cost / reliability engineering on an AI estate** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | 🆕 🟢 **`o_ai_usage_log` carries `a_req_temperature`, `a_req_top_p`, `a_cached_input_tokens`, `a_reasoning_tokens`, `a_duration_millis`, `a_resp_finish_reason` and a call-correlation id.** 🔴 **Moodle's ledger has none of these.** 🔵 **FinOps for AI is a reporting job here, not a build** |
| 🆕 🟢 **Data-residency / air-gapped engagement** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) **or** 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | mixed | 🆕 🟢 **Two different answers, both CONFIGURATION: Moodle's `ollama` provider plugin, and OpenOLAT's `GenericAiSPI` (any OpenAI-compatible `base.url`) PLUS `LocalOnnxSPI`, which runs an admin-uploaded ONNX embedding model IN-PROCESS.** 🔵 **For embeddings OpenOLAT needs no server at all — the strongest residency answer on this shelf** |
| 🆕 🟡 **Large consortium / MOOC estate wanting many branded sites** | 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** `35 136 B` | 🆕 🟢 **Tenancy CONFIRMED (`ACTION IB`): `SiteConfiguration` one-to-one on `django.contrib.sites.Site`, `66` files on the sites framework.** 🟡 **It is CONFIGURATION-scoped tenancy, not row-level isolation like `mentingo`'s RLS — brand and settings per site, one database.** 🔴 **AGPL, so the licence conversation happens before the architecture one** |
| 🆕 🔴 **Credentialing on Open edX** | 🔴 **none — do not plan on core** | — | 🆕 🔴 **`lms/djangoapps/badges` still EXISTS as `23` paths and its models were DELETED by `migrations/0005_delete_all_models.py` in 2023.** 🔴 **`0` matches for OB 3.0 / W3C VC.** 🟢 **`0 of 6` platforms issue a modern verifiable credential; `P159-A` / `P157-C` remain BUILDS** |
| 🆕 🔴 **LTI 1.3 or xAPI on Open edX** | 🟡 **separate packages, not core** | mixed | 🆕 🔴 **`T142`: `lti13`/`lti1p3`/`ltiadvantage` return `0` in the platform repo — the capability is `lti-consumer-xblock`, and learning records are `event-routing-backends`.** 🟡 **Both are pinned in `requirements/edx/base.txt`. Scope them as dependencies with their own licences, not as platform features** |
| 🔴 **Education ERP / SIS** | 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) *(LGPL-3.0)*, [`frappe/erpnext`](https://github.com/frappe/erpnext) *(GPL-3.0)* | 🔴 copyleft | 🔴 **FOURTEENTH pass with no MIT/Apache education ERP.** 🆕 🔴 **`T122` a FIFTH time: this pass's query returned the same vendor's glossary page in FIVE locales, plus ERPNext (GPL-3.0) and Twenty (BSL-1.1). The query has stopped measuring the market** |

### 🔴 The one thing a studio must put in writing before either AI row is sold

🔴 **Neither platform deletes AI data.** 🔴 **Moodle stores `prompt` and `generatedcontent`
verbatim in three tables and `prompt` + `revisedprompt` + `sourceurl` in a fourth, with NO
scheduled cleanup and NO retention setting.** 🔴 **OpenOLAT's `AiUsageLogDAO` has no delete
method, and `o_ai_essay_correction.a_student_answer` is `text NOT NULL` — the student's essay
itself, retained.**
🟢 **What each DOES have:** 🟢 **Moodle — a complete GDPR provider (`806` LOC) so erasure works
on REQUEST, plus `tool_dataprivacy` retention periods that are off by default
(`automaticdatadeletionapproval = 0`).** 🟡 **OpenOLAT — `UserDataDeletable` on
`EssayAiCorrectionService`, so corrections die with the user account; the usage log is NOT
covered by it.**
🔵 **Say this before the pilot, not after the first subject-access request.** 🟢 **`P161-B`.**

## Pass 160 — 2026-10-12

🟢 **Moodle — the platform this page routes copyleft engagements to, and the one it had never
read — is now measured from its tree.** 🟢 **Two of its rows change, one correction is owed to
`mentingo`, and one description on this page was simply wrong.**

### 🆕 🟢 The routing table, corrected where this pass's measurements changed it

| engagement | platform | licence *(body-read)* | why — and what changed this pass |
|---|---|---|---|
| 🟢 **Institution that wants to OWN an academic platform** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** `10 982 B` | 🟢 **UNCHANGED and now CURRENT: committed `2026-10-12`, the day of this pass.** 🟢 **QTI 2.1 at `919` paths on a uniform re-count** |
| 🆕 🟢 **ASSESSMENT-heavy engagement** *(exams, item banks, QTI interchange)* | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | 🆕 🟢 **Settled by one dimension: OpenOLAT `919` QTI paths against Moodle's `8`, and Moodle's eight are QTI `v1.2` LEGACY — Common Cartridge `.xsd` schemas and a Blackboard import filter.** 🔴 **Moodle cannot interchange a modern QTI item bank** |
| 🆕 🟢 **xAPI / learning-record engagement** | 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 **GPL-3.0** `35 147 B` | 🆕 🟢 **REVERSED from this page's standing assumption: Moodle SHIPS xAPI — `public/lib/xapi`, `78` paths, `api.php`/`iri.php`/`state_store.php`.** 🔴 **OpenOLAT has `0` on four spellings.** 🔵 **First dimension where the copyleft platform is the right answer on capability, not just on incumbency** |
| 🆕 🟢 **Client wants GOVERNED AI inside an existing LMS** | 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) core AI | 🟡 **GPL-3.0** | 🆕 🟢 **`public/ai`, `372` files: seven providers (`ollama` included — sovereign deployment is CONFIGURATION), a per-call ledger in `ai_action_register`, policy acceptance in `ai_policy_register` with a report, and `rate_limiter.php`.** 🔴 **Four actions, NONE evaluative.** 🔵 **`P160-B`** |
| 🟢 **Corporate L&D / HRTech, greenfield, white-labelled or resold** | 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** `1 062 B` | 🟢 **Still the only row with a real tenancy boundary (PostgreSQL RLS).** 🆕 🟢 **CORRECTION: it DOES ship SCORM — `119` files, `packages/scorm-export-generator` + `packages/scorm-export-runtime` with a bundled player.** 🔴 **xAPI still absent (README only)** |
| 🟢 **Client needs ISSUED, portable CREDENTIALS** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) *(Apache-2.0)* **or** 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) *(GPL-3.0)* | mixed | 🆕 🟢 **TWO incumbents, not one: OpenOLAT `182` paths, Moodle `306` — `assertion.php`, `badgeclass.php`, `criteria/`, backpack export, `backpack_api2p1_mapping.php`.** 🔴 **BOTH are Open Badges `v2` only; `OPEN_BADGES_V2` appears `132` times in Moodle and `V3` never.** 🟢 **`P159-A`'s signing build stands — `ACTION HY` confirmed `0 of 5` platforms issue an OB 3.0 / W3C VC** |
| 🔴 **MULTI-TENANT public-sector or district estate** | 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) **or** separate instances | 🟢 MIT | 🆕 🔴 **Measured and negative: Moodle core has NO tenancy — its `62` *"tenant"* paths are `62 of 62` inside the vendored `public/lib/google2-service`** *(`T136`)*. 🔴 **Moodle Workplace, which has it, is proprietary.** 🔴 **OpenOLAT has none either** |
| 🆕 🔴 **Metadata CATALOGUING plumbing** *(was: "learning-record plumbing")* | 🟡 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | 🟢 **Apache-2.0** `11 357 B` | 🆕 🔴 **CORRECTION — this page described it wrongly.** 🔴 **`0` matches for `xapi`, `caliper` or `statement`: it carries METADATA, not learning records.** 🔴 **`53` files, last commit `2026-02-26` (`228` days, a README edit), `Django<4.0` (EOL April 2024), and its `openlxp-xsr-aws` sibling does not resolve.** 🟡 **Vendor the V-T-V-L idea; do not ship the package** |
| 🔴 **Education ERP / SIS** | 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) *(LGPL-3.0)*, [`frappe/erpnext`](https://github.com/frappe/erpnext) *(GPL-3.0)* | 🔴 copyleft | 🔴 **THIRTEENTH pass with no MIT/Apache education ERP.** 🆕 🔴 **This pass's ERP/CRM query returned one vendor's own pages in SEVEN locales — `T122` a fourth time** |

### 🆕 🔴 `T135` — a capability that ships as an EXPORT PIPELINE is invisible to a schema census

[`evidence/mentingo-scorm-correction.2026-10-12-p160.tsv`](../evidence/mentingo-scorm-correction.2026-10-12-p160.tsv)

🔴 **p158's `T127` read `mentingo`'s DATABASE SCHEMA and concluded its topics over-claim `scorm`
and `xapi`.** 🟢 **The tree says otherwise on half of it:** 🟢 **`119` SCORM files —
`packages/scorm-export-generator`, `packages/scorm-export-runtime` including `src/player` and its
assets, `packages/shared/src/constants/scorm.ts`, and SCORM references inside the API's
`certificates`, `adminChapter` and `native-archive` import/snapshot services.**
🟢 **`xapi` appears ONLY in `README.md` — `0` code or schema matches, so `T127` stands there.**
🆕 **`T135`:** 🔵 **SCORM in `mentingo` is an EXPORT PIPELINE — a build artefact with a bundled
player — not a schema concept. A schema census structurally cannot see it**, 🔵 **exactly as
`T133`'s topic census could not see a capability shipped as a module.** 🟢 **Three instruments,
three blind spots, one lesson: match the instrument to how the capability is IMPLEMENTED.**
🟡 **`T127` is amended, not withdrawn: the `xapi` half was right.**
## Pass 159 — 2026-10-12

🟢 **`OpenOLAT` was this page's default recommendation for the fork-and-own academic case on an
UNVERIFIED assumption one pass ago. It is now verified, and the recommendation STANDS** —
🟢 **with more behind it than p158 claimed.**
🆕 🟢 **And this page gains a column it never had: CREDENTIALING, because `OpenOLAT` ships Open
Badges.**

### 🟢 CONFIRMED — `OpenOLAT` is the fork-safe academic platform, and it federates both ways

| claim this page carried | p159 verdict |
|---|---|
| 🟢 *"Apache-2.0, 447 ★"* | 🟢 **CONFIRMED from the body — `10 982 B` on `master`. `447 ★`, `167` forks, `5` open issues, pushed `2026-10-12`** |
| 🟢 *"Fork-safe AND speaks LTI and QTI"* | 🟢 **CONFIRMED and DEEPER than claimed: LTI 1.3 in BOTH directions, with AGS, NRPS and Deep Linking; QTI 2.1 at `660` paths** |
| 🟡 *(not claimed)* | 🆕 🟢 **SCORM at `154` paths; Open Badges 2.0 at `156` paths with automatic rule-driven award** |
| 🔴 *(not claimed)* | 🔴 **xAPI ABSENT — `0` matches on four spellings.** 🔵 **Same hole as `mentingo`. Neither permissive platform on this shelf emits xAPI** |

### 🆕 🟢 The routing table, now with a credentialing row

| engagement | platform | licence | why |
|---|---|---|---|
| 🟢 **Institution that wants to OWN an academic platform** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0 + patent grant** | 🟢 **VERIFIED: LTI 1.3 platform **and** tool, AGS, NRPS, Deep Linking, QTI 2.1, SCORM, Open Badges 2.0, hierarchical organisations with per-node roles.** 🔵 **The default, and now on evidence** |
| 🟢 **Corporate L&D / HRTech, greenfield, white-labelled or resold** | 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 🟢 **DB-level RLS tenancy, LLM-judge rubric engine as DATA.** 🔴 **No LTI — never where tools must federate into a campus LMS** |
| 🟢 **University / K-12 with an existing LMS estate; AI as a federated tool** | 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) *(GPL-3.0, `COPYING.txt`)* or [`openedx/edx-platform`](https://github.com/openedx/edx-platform) *(AGPL-3.0)*, **left unmodified** | 🔴 copyleft | 🟢 **They speak LTI 1.3 + AGS. `P156-A` crosses at the protocol, so the deliverable stays permissive** |
| 🆕 🟢 **Client needs ISSUED, portable CREDENTIALS** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) **Open Badges module** | 🟢 **Apache-2.0** | 🟢 **`156` paths, `v2` spec: `Badge`, `Assertion`, `Criteria`, `Profile`, `Identity`, `BadgeClass`, plus LinkedIn push.** 🔴 **Open Badges 2.0 ONLY — no 3.0, no W3C VC.** 🟢 **Pair with the MIT [`OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget) for `v3` authoring.** 🔵 **`P159-A` is the upgrade, and only the SIGNING half is a build** |
| 🆕 🟡 **Client needs learning-record PLUMBING** | 🟡 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | 🟢 **Apache-2.0** *(11 357 B)* | 🟢 **A permissive learning-experience data pipeline. NEW to this shelf** — 🟡 **unassessed beyond its licence; see `ACTION HY`** |
| 🔴 **Education ERP / SIS** | 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) *(LGPL-3.0)* on [`odoo/odoo`](https://github.com/odoo/odoo) *(LGPL-3.0)*, or [`frappe/erpnext`](https://github.com/frappe/erpnext) *(GPL-3.0)* | 🔴 **copyleft, no permissive option exists** | 🔴 **TWELFTH pass with no MIT- or Apache-licensed education ERP.** 🟢 **This is a SUPPLY fact, now licence-verified from four bodies rather than inferred** |

### 🔴 A correction this page owes `frappe/lms` adopters

🔴 **[`frappe/lms`](https://github.com/frappe/lms) is AGPL-3.0, not GPL** — read from `license.txt`
on its `develop` default branch, `33 893 B`.
🔴 **It is STRICTER than ERPNext (GPL-3.0) in the same organisation**, 🔴 **so hosting Frappe LMS
for a client is distribution and triggers source obligations on the hosted work.**
🟢 **Anyone comparing the Frappe stack by organisation rather than by repository gets this wrong.**

### 🔴 And one `P157-C` caveat, stated plainly

🔴 **[`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) — the standards-complete
Open Badges 3.0 / W3C VC library p157 proposed as a BUILD BASE — is LGPL-3.0**, read from
`LICENSE.txt` on `master`, `7 650 B`.
🟡 **LGPL on a library is workable** *(linking, not statically absorbing)*, 🔴 **but it is copyleft
and p157 presented it without saying so.** 🟢 **A client who expected a permissive foundation
needs to hear this before the architecture, not after.**
## Pass 158 — 2026-10-12

🔴 **A CORRECTION to this page's own recommendation, and it is the client-facing half of
`ACTION HR`.** 🟢 **`Selleo/mentingo` is fully assessed for the first time in four passes — and it
belongs in a different column than this page has been putting it in.**

### 🔴 CORRECTED — `mentingo` is not an academic LMS, and it does not speak LTI 1.3

🔴 **This page has offered `mentingo` as the MIT answer to *"to OWN the platform, fork-safe"*
without qualification. That is right for one engagement shape and wrong for the other.**

| claim this page carried | p158 verdict |
|---|---|
| 🔴 *"AI-native LMS, SCORM + xAPI, white-label"* | 🔴 **xAPI is ABSENT from the data model.** The claim traces to the repository's GitHub **topic list**; the maintainers' own README keeps `xAPI/LTI` inside a commented-out block marked *"DO NOT PUBLISH WITHOUT VERIFICATION"* |
| 🔴 *"the only MIT LMS"* | 🟡 **True on licence, misleading on category.** 🟢 **Its README: *"designed for corporate L&D… If you need a large academic plugin ecosystem, choose Moodle"*** |
| 🟢 *"MIT, 1 062 B, fork freely"* | 🟢 **CONFIRMED again from the body** |

### 🟢 The corrected routing table — which platform for which engagement

| engagement | platform | licence | why |
|---|---|---|---|
| 🟢 **University / K-12 with an existing LMS estate; AI delivered as a federated tool** | 🟢 [`moodle/moodle`](https://github.com/moodle/moodle) *(GPL)* or [`openedx/edx-platform`](https://github.com/openedx/edx-platform) *(AGPL-3.0)*, **left unmodified** | 🔴 copyleft | 🟢 **They speak LTI 1.3 + AGS. `P156-A` crosses the licence boundary at the protocol, so the deliverable stays MIT** |
| 🟢 **Institution that wants to OWN an academic platform** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) *(Apache-2.0, 447 ★)* | 🟢 permissive + patent grant | 🟢 **Fork-safe AND speaks LTI and QTI.** 🔵 **This is now the default recommendation for the fork-and-own academic case** |
| 🆕 🟢 **Corporate L&D / HRTech, greenfield, white-labelled or resold** | 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) *(MIT, 93 ★)* | 🟢 **MIT — imposes nothing** | 🟢 **DB-level multi-tenancy (PostgreSQL RLS), AI mentor and an LLM-judge rubric engine in the core, AWS Marketplace one-click deploy.** 🔴 **No LTI — do not propose it where tools must federate into a campus LMS** |
| 🔴 **Hosted-for-the-client AI-native platform** | 🔴 `learnhouse`, `lextures` *(AGPL-3.0)* | 🔴 network copyleft | 🔴 **Hosting IS distribution under AGPL. `mentingo` is the MIT row in the same architectural slot** |

### 🆕 🟢 Why `mentingo` is a stronger corporate row than this page realised

🟢 **The assessment turned up a subsystem no other platform on this shelf has:** 🟢 **an
LLM-as-judge assessment engine modelled in the database** — `aiJudgeConfigurations`,
`aiJudgeCriteria`, `aiJudgeScoreGuidance`, `aiJudgeBlockingErrors`, plus per-judgement tables.
🔵 **Rubric criteria, score guidance and *hard-fail blocking errors* are first-class rows, not
prompt text.**

🟢 **For a compliance-training engagement that is the whole product**: 🟢 **mandatory training
where a specific error must fail the attempt regardless of overall score is precisely what
`aiJudgeBlockingErrors` models**, and 🟢 **the EU AI Act reading on this shelf (`trends` T6) puts
EVALUATIVE use in the high-risk tier, where an auditable, data-modelled rubric is worth more
than a better prompt.**

🟢 **Also shipped, and relevant to a studio:** 🟢 **a `permission*` RBAC rule-set engine (5
tables), learning paths with their own certificates, live training with attendance (LiveKit),
calendar sync both directions, a transactional `outboxEvents` table for integration, and a
`courseAuthoring*` surface (4 tables) that is an authoring-agent landing zone.**
🔴 **Against that: `93 ★`, `107` open issues, single vendor (Selleo, Poland), and no third-party
deployment this shelf can point to.** 🔵 **Read it as a reference architecture and fork base,
which is what this page has always said about it.**

### 🟡 Regional note, from the same read

🟢 **`mentingo` ships UI in English, Polish, German, Spanish, French and Czech.**
🟢 **Spanish is present — so a LATAM or Iberian corporate deployment starts with the interface
already translated.**
🔴 **Portuguese is NOT present**, which is a concrete localisation cost for Brazil — 🔵 **the
largest LATAM market, and the one whose AI bill (`PL 2338/2023`) is furthest advanced.**

### 🔴 Still open on this page

- 🔴 **`OpenOLAT`'s data model is unread**, and it is now the recommended fork-and-own academic platform. 🔵 **It should be assessed the way `mentingo` just was.**
- 🔴 **No platform row on this shelf has a third-party production deployment this KB can name**, 🟡 **other than Moodle and Open edX, which are the two it tells clients not to fork.**
- 🟡 **`scormStandardEnum`'s members unread** — `mentingo`'s SCORM 2004 support is unknown.

## Pass 157 — 2026-10-12

🟢 **A 156-pass gap on this page is CLOSED, and the answer is a build decision rather than a
shortlist.**
🔴 **The credentialing layer that 2026 buyer-demand sources keep naming has `29` repositories
behind it, a `85 ★` ceiling, and a reference implementation with ONE star.**

### 🆕 🟢 The credentialing layer — the gap is CLOSED, and the finding is that the supply is not there

🔵 **This shelf has carried *"no credentialing / skills-pathway repository"* as an open gap for
156 passes, with the honest caveat that it might be a search failure rather than a supply gap.**
🟢 **It is a supply gap. Measured:**
[`evidence/credentialing-census.2026-10-12-p157.tsv`](../evidence/credentialing-census.2026-10-12-p157.tsv)

| measurement | value |
|---|---|
| 🔴 **Population of `topic:open-badges`** | 🔴 **`29` repositories, entire topic** |
| 🔴 **Highest star count in the topic** | 🔴 **`85`** — `fedora-infra/tahrir` |
| 🔴 **Stars on the only production-oriented Open Badges 3.0 library** | 🔴 **`1`** |
| 🔴 **Rows that are MIT or Apache AND pushed in 2026** | 🔴 **`2` of 29** |
| 🔴 **Rows last pushed before 2022** | 🔴 **`6` of the 15 read** |

🟢 **The rows worth naming, licence read from the body where it mattered:**

| repo | ★ | licence | what it is, and the verdict |
|---|---|---|---|
| 🆕 🟡 [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) | 🔴 **1** | 🟡 **LGPL-3.0** (🆕 `master/LICENSE.txt`, 7 650 B) | 🟢 **Issue, verify and revoke Open Badges 3.0 / W3C Verifiable Credentials as JWT-VC, with Bitstring Status List revocation. Active `2026-10-04`.** 🔵 **This is THE standards-complete implementation, and it has one star.** 🟡 **LGPL: link freely; modifying the library is not free** |
| 🆕 🟡 [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) | **63** | 🔴 **AGPL-3.0** (`LICENSE`, 33 820 B) | 🟢 **Open Badges 3.0 issuance for course, workshop and conference organisers — the closest thing to a usable issuer product.** 🔴 **AGPL: a hosted derivative discloses** |
| 🆕 🟡 [`fedora-infra/tahrir`](https://github.com/fedora-infra/tahrir) | **85** | 🔴 **AGPL-3.0** (🆕 `develop/LICENSE`, 34 917 B) | 🟢 **A badge-issuing web app with a decade of real operation behind Fedora's badges programme.** 🟡 **GitHub reports `NOASSERTION` because the body is `394 B` longer than standard AGPL — the body read resolves it** |
| 🆕 🟢 [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget) | 🔴 **1** | 🟢 **MIT** (`LICENSE`, 1 080 B) | 🟢 **A Vue widget to author an Open Badge 3.0 achievement definition. Active `2026-09-28`.** 🔵 **The ONLY clean permissive active row in the topic** — 🔴 **and it is a form widget, not a system** |

🔵 **The studio call, and it is the clearest build-vs-adopt decision on this shelf:**
- 🟢 **Demand is named by 2026 trend sources** — digital credentials and micro-credentials
  against employer skills-based hiring.
- 🔴 **Supply is 29 repositories whose best permissive row is a form widget.** 🔴 **There is no
  credentialing PLATFORM to adopt.**
- 🟢 **So this is a BUILD lane, not an integrate lane** — 🟢 **and the standards work is already
  done for free: Open Badges 3.0 is W3C Verifiable Credentials, `openbadgeslib` shows the
  JWT-VC issue/verify/revoke path, and LGPL lets a product link it without disclosing.**
- 🔵 **It is also the only lane on this shelf where a studio could credibly own the reference
  implementation**, 🟢 **because the incumbent has one star.**

### 🆕 🔴 `learnhouse` joins the platform shelf, and it is AGPL — re-verified from the body

🆕 🔴 [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) — **2 351 ★**, active
`2026-10-11`, 🔴 **AGPL-3.0, body-read `34 523 B` this pass on `main`** *(the shelf's prior read
was on `dev`; it resolves identically on both, as p145 recorded)*.
🟢 **A next-generation learning platform with AI features first-class rather than bolted on** —
🔵 **so it is the closest open competitor to what a studio would otherwise propose building**,
and 🔴 **its AGPL makes hosting it for a client a disclosure event.**
🟢 **Independent re-confirmation, not a new row: this shelf already corrected its licence from
Apache-2.0 to AGPL-3.0, and the body read this pass agrees.**

### 🔴 `T122` — the ERP/CRM query has stopped measuring the market

🟢 **Run this pass as registered:** `open source platform education ERP CRM MIT Apache`.
🔴 **`10` of `10` results were ONE vendor's own glossary pages — `openeducat.org`, the same two
articles in ten locales** (`ar`, `fr`, `pt-BR`, `zh`, `de`, `es`, and more).

🆕 **`T122`** — 🔴 **a research query whose result page is a single vendor's glossary repeated in
ten languages is not returning a market picture; it is returning that vendor's SEO.**
🟢 **The query is retired as a market instrument** and 🔵 **kept only as a reminder that a
channel can saturate without going quiet, which is the harder failure to notice** —
🟢 **`T110`'s lesson on a different axis: there, the words resolved to the wrong domain; here,
they resolve to one seller.**

🟢 **One real thing did come back, and it is a confirmation:** 🔴 **the source itself states that
*"MIT and Apache 2.0 are permissive... so if you specifically want MIT or Apache, OpenEduCat is
not the match"*** — 🟢 **i.e. the question *"is there a permissive education ERP?"* is answered
NO by the leading vendor in the category.** 🔴 **ELEVENTH pass with no open-source vendor named
in any market source.**

### 🟢 The vertical platform shelf, with attention now attached

🔵 **The full ★ / activity / licence table for all 14 platform and foundational rows is on
[`repos/foundations.md`](../repos/foundations.md) this pass** *(`ACTION HM`)*. 🟢 **The
platform-selection summary for an engagement:**

| if the client needs | take | licence posture |
|---|---|---|
| 🟢 **To keep their LMS and add AI** | 🟢 **leave Moodle / Open edX ALONE, integrate over LTI 1.3 + AGS** | 🟢 **A protocol boundary is not a derivative work. `P156-A`** |
| 🟢 **To OWN the platform, fork-safe** | 🟢 **`OpenOLAT` (Apache-2.0, 447 ★)** or 🟢 **`Selleo/mentingo` (MIT, 93 ★)** | 🟢 **Permissive, patent grant on OpenOLAT** |
| 🟢 **Low/no-connectivity deployment** | 🟢 **`kolibri` (MIT, 1 143 ★)** | 🟢 **MIT** |
| 🟢 **Student records, not courses** | 🔴 **`rosariosis` (GPL-2.0, 646 ★)** | 🔴 **GPL-2.0 — distribution discloses** |
| 🟢 **Education ERP** | 🔴 **`openeducat_erp` (LGPL-3.0, 887 ★, default branch `19.0`)** | 🟡 **LGPL — link, do not modify** |
| 🟢 **Verifiable credentials** | 🔴 **nothing to adopt — see above. BUILD, linking `openbadgeslib`** | 🟡 **LGPL-3.0 linking** |
| 🟢 **Virtual classroom** | 🔴 **`bigbluebutton` (LGPL-3.0, 9 241 ★)** | 🟡 **LGPL** |
| 🟢 **Interactive content** | 🔴 **`h5p-php-library` (GPL, 150 ★)** | 🔴 **GPL** |

## Pass 156 — 2026-10-12

🟢 **`ACTION HB` DISCHARGED, and it REFUTED this shelf's own published claim about the row a
studio is most likely to bill against.**
🟢 **Every platform licence below is body-read this pass with the answering PATH recorded** —
🔴 **and one of them is not where anyone would look.**

### 🔴 CORRECTION — `openeducat_erp` does NOT admit to bundled non-conforming licences

🔵 **p155 recorded OpenEduCat's `LICENSE` preamble as the SECOND instance of `T92`** *(a project
admitting by its own words that it bundles externals under other licences)*, and warned a studio
to read it before billing.
🔴 **That reading is now REFUTED, exactly on `HB`'s registered falsifier.**
[`evidence/openeducat-carveout.2026-10-12-p156.tsv`](../evidence/openeducat-carveout.2026-10-12-p156.tsv)

| probe | result |
|---|---|
| 🟢 `openeducat_erp/master/LICENSE` | **200**, 8 241 B, LGPLv3. Carve-out sentence present: *"Some external libraries and contributions bundled with OpenEduCat may be publishedunder other GPL-compatible licenses."* |
| 🆕 🔴 `odoo/odoo/master/LICENSE` | **200.** 🔴 **Carries the SAME SENTENCE VERBATIM, with only the project name changed**, and the same preceding line *"For copyright information, please see the COPYRIGHT file."* 🟢 **Odoo's copy has no typo; OpenEduCat's reads `publishedunder`** |
| 🔴 `openeducat_erp/{master,18.0,17.0}/COPYRIGHT` | 🔴 **404, 404, 404.** 🔴 **The pointer in line 1 of its own licence is DANGLING on all three branches** |
| 🔴 `NOTICE`, `AUTHORS`, `openeducat_core/static/src/lib/LICENSE` | 🔴 **404 on every path.** 🔴 **No bundled non-LGPL notice found anywhere probed** |

🟢 **Verdict: the carve-out is INHERITED ODOO BOILERPLATE, copied with a transcription defect,
pointing at a file OpenEduCat never added.** 🟢 **It is not a statement about OpenEduCat's own
tree.** 🟢 **`T92`'s second instance is CLOSED, and `T92` returns to resting on one real
observation — `scibly`'s proprietary `ee/` directory.**
🟢 **Two further things worth a studio's attention:** 🟢 **the carve-out is bounded to
*"GPL-COMPATIBLE"* licences, so even if it were live it could not introduce a proprietary
term** — 🔴 **and OpenEduCat is a module set that RUNS ON Odoo, so the inherited sentence is
about Odoo's bundle, which the deployment does include.**
🆕 **`T116`** — 🔴 **a licence preamble inherited from an upstream framework describes the
UPSTREAM's bundle, not the fork's**, 🟢 **and the way to tell is to diff it against upstream,
which costs one fetch.**

### 🟢 The platform shelf — licence, path, and the integration consequence

| platform | licence *(body-read, p156)* | path | what it is | how to put AI on it |
|---|---|---|---|---|
| 🔴 [**Moodle**](https://github.com/moodle/moodle) | 🔴 **GPL** *(35 147 B)* | 🆕 **`COPYING.txt`** | 🟢 **The most-deployed open-source LMS.** Vendor self-reports 400M+ users, 150k+ sites | 🟢 **Plugin boundary + LTI 1.3.** 🔴 **Do not fork and resell** |
| 🔴 [**Open edX**](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** *(35 136 B)* | `LICENSE` | 🟢 **The MOOC platform; course-centric at scale** | 🔴 **AGPL reaches hosted derivatives.** 🟢 **Integrate as a separate service over REST/LTI, never in-process** |
| 🟡 [**Sakai**](https://github.com/sakaiproject/sakai) | 🟡 **ECL-2.0** *(11 120 B)* | `LICENSE` | 🟢 **Institutional, built for university consortia** | 🟢 **Permissive (Apache-derived). Fork freely** |
| 🟢 [**OpenOLAT**](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** *(10 982 B)* | `LICENSE` | 🟢 **Full institutional LMS, permissive, with a patent grant** | 🟢 **The cleanest fork target of any LMS on this shelf** |
| 🟢 [**Kolibri**](https://github.com/learningequality/kolibri) | 🟢 **MIT** *(1 097 B)* | `LICENSE` | 🟢 **Offline-first, built for low/no connectivity** | 🟢 **MIT. 🔵 The LATAM / Africa infrastructure play, and UNESCO's own caution names exactly its market** |
| 🟢 [**Mentingo**](https://github.com/Selleo/mentingo) | 🟢 **MIT** *(1 062 B)* | `LICENSE` | 🟢 **The only MIT-licensed LMS on this shelf.** 🟡 **EMEA — Poland** *(`P36`, verified profile)* | 🟢 **Fork freely.** 🔴 **Still unassessed on data model and multi-tenancy** |
| 🔴 [**BigBlueButton**](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0** *(7 652 B)* | `LICENSE` | 🟢 **Virtual classroom: WebRTC, whiteboard, breakouts, recording** | 🟡 **LGPL: link, don't modify.** 🟢 **The live-session capture surface** |
| 🔴 [**H5P**](https://github.com/h5p/h5p-php-library) | 🔴 **GPL** *(35 146 B)* | `LICENSE.txt` | 🟢 **Interactive content types that drop into Moodle, Open edX and Canvas** | 🟢 **Generate H5P content with AI; the generator stays outside the GPL boundary** |
| 🔴 [**Chamilo**](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL** *(35 147 B)* | `LICENSE` | 🟢 **Lightweight LMS with real francophone and LATAM public-sector deployment** | 🟢 **LTI + plugin** |
| 🔴 [**ILIAS**](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL** *(35 147 B)* | `LICENSE` | 🟢 **Institutional LMS, strong in German-speaking EMEA** | 🟢 **LTI + plugin** |
| 🔴 [**OpenEduCat**](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0** *(8 241 B)* | `LICENSE` | 🟢 **Education ERP on Odoo: admissions, fees, library, hostel, exams** | 🟢 **LGPL + Odoo module boundary. 🔵 The ERP/SIS row, closest analogue to Odoo-for-education** |
| 🔴 [**Frappe Education**](https://github.com/frappe/education) | 🔴 **GPL-3.0**, 🔴 **from a 19 B stub** | `license.txt` | 🟢 **Education module on the Frappe/ERPNext stack** | 🔴 **The whole grant is `License: GNU GPL V3`; `-only` vs `-or-later` is UNANSWERABLE** |
| 🟡 **Canvas LMS** | 🟡 **open core, commercial** *(not body-read this pass)* | — | 🟢 **Dominant in US higher ed** | 🟢 **LTI 1.3 + its REST API. 🔵 Two `canvas-mcp` connectors already on this shelf, both MIT** |

🟢 **Permissive and forkable: `OpenOLAT` (Apache-2.0), `Kolibri` (MIT), `Mentingo` (MIT),
`Sakai` (ECL-2.0) — four of twelve body-read rows.**
🔴 **Eight are copyleft, and the two with the largest installed bases are the GPL and AGPL
rows.**

### 🔵 The one structural recommendation this page supports

🟢 **Do not fork the LMS. Compose beside it.**
🔴 **Moodle's GPL and Open edX's AGPL turn a resold derivative into a source-disclosure event**,
and 🟢 **every client already runs one of them.** 🟢 **An MIT or Apache-2.0 agent that reaches the
LMS over **LTI 1.3**, **MCP** or **REST** carries none of those obligations** — 🔵 **and that is
the same architecture in all five regions, which is why it is worth saying once here rather than
four times in `intel/market.md`.** 🟢 **See `compose/patterns.md` `P156-A`.**


## Pass 155 — 2026-10-12

🔴 **A load-bearing claim on this page is WRONG and is corrected here.** This shelf has said
for several passes that **`sakai` (ECL-2.0) is *the* answer whenever copyleft is a blocker.**
🟢 **There are now THREE permissive institutional routes, not one** — and one of them is **MIT**.

### 🆕 🟢 The permissive-platform table, rebuilt from bodies read this pass

| platform | licence *(body-read)* | bytes | what it is | the permissive story |
|---|---|---|---|---|
| 🆕 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | **10 982** | Full Java institutional LMS: courses, assessment, communication | 🟢 **A STANDARD permissive grant on a complete LMS.** 🔵 **Nothing to negotiate, nothing to carve out — the cleanest substrate on this page** |
| 🟢 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | **11 120** | University-governed LMS, Apache-derived | 🟡 **Permissive, but NOT Apache-2.0.** 🔴 **ECL-2.0 narrows the patent grant** — read it before assuming Apache terms. 🔴 Its one GNU notice is VENDORED TrimPath (`T86`) |
| 🆕 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | **1 062** | 🟢 **AI-native LMS with a built-in AI mentor and role-play** | 🟢 **MIT — the only LMS on this shelf that imposes nothing.** 🔴 **92 ★ and young**: this is a fork-and-own candidate, not an institutional procurement |
| 🆕 🔴 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** | **15 214** | 🟢 **K-12 Student Information System** — attendance, grades, scheduling, billing | 🔴 **GPL-2.0, and version 2 is NOT version 3**: different compatibility, no Apache-2.0 patent-clause interop. 🟢 **Go out to an API, do not build inside** |

🔵 **How to choose between the three permissive routes, and it is not a tie:**

- 🟢 **Institutional procurement, EMEA especially → `OpenOLAT`.** A complete LMS with a grant
  every legal department already recognises. 🟡 **Region placement needs `P36` work** (`ACTION HA`).
- 🟢 **University consortium, existing Java estate → `sakai`.** 🔴 **But brief counsel that
  ECL-2.0 ≠ Apache-2.0.**
- 🟢 **Greenfield, AI-first, small cohort → `mentingo`.** 🔵 **It is the only row where the
  platform's own licence is a non-event** — and it ships the AI mentor already.
- 🔴 **Never: build inside `rosariosis`, Canvas, Moodle or Open edX.** 🟢 **The boundary rows
  (`tsugi` Apache-2.0, `XBlock` Apache-2.0, `scorm-again` MIT, an external MCP server) remain
  the way in** — unchanged and re-affirmed.

### 🆕 🔴 `openeducat_erp`'s warning is WITHDRAWN, and replaced by a sharper one

🟢 **The licence IS file-read now: 8 241 B, LGPL-3.0, identical on `master`, `18.0`, `17.0`**
(`repos/foundations.md`, `ACTION GQ`). 🔴 **The *"do not quote the licence from here"* line on
this page is therefore wrong and is withdrawn.**

🔴 **The replacement warning is narrower and real:** the root body itself says bundled external
libraries *"may be published under other GPL-compatible licenses"* and points into the tree.
🔵 **So for an OpenEduCat engagement: the ERP is LGPL-3.0 — 🟢 which permits linking your own
modules without inheriting — 🔴 but the bundled paths are not enumerated and must be before
you ship.** 🔵 **`ACTION HB`.**

🔴 **`frappe/education` keeps its warning, with an exact figure:** a **19-byte** `license.txt`
on `develop`, nothing in `pyproject.toml`, and 🔴 **no `-or-later`/`-only` wording anywhere**,
so `P43` has no surface to run on. 🔵 **Get it in writing from Frappe Technologies.**

### 🟢 Which route sells, by region

🔵 **Four regions, and the gaps are named where they exist.** 🔵 **The canonical opportunity block for this industry lives in [`intel/market.md`](../intel/market.md) under `## Opportunities by region`** — this section is the PLATFORM-CHOICE reading of those same regions, not a second register.

#### North America

🟢 **Canvas (AGPL-3.0-only) dominates HiEd → the external-MCP architecture stands**, and
[`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, 290 ★) is the
demonstrable artefact. 🆕 🟢 **The new, concrete asks this pass found are statutory and
dated:** Oklahoma **`SB 1734`** requires **every district** to adopt a written AI policy before
the **2027–28** school year, bars AI as the primary basis for high-stakes student decisions,
and mandates a parental opt-out — 🔵 **that is three deliverables (policy instrument, approval
gate, opt-out plumbing) with a statutory deadline.** Maryland **`SB 720`** funds statewide
teacher AI professional development; Alabama **`HB 329`** ties graduation to a CS course
including AI instruction; California **`AB 1159`** bars training on student data; Idaho
**`SB 1227`** sets tool-privacy requirements. 🔴 **Canada and Mexico returned nothing, FIFTH
consecutive pass** — the continental query is US-only in practice.

#### EMEA

🟢 **Moodle + Open edX institutional base, and the sellable structure is now THREE-TIERED, not
two:** 🔴 **Article 5 PROHIBITIONS are live and absolute** — emotion inference in schools is
banned outright, not regulated — 🟢 **Article 4 AI-literacy duties are live**, and 🟢 **the
Annex III high-risk programme for admissions, grading and proctoring is a `2027-12-02`
engagement.** 🆕 🟢 **Commission guidelines of `2026-05-19` distinguish pedagogical support
from evaluative use**, 🔵 **which is the line a studio should architect to: keep the agent on
the pedagogical side of it and the high-risk obligations do not attach.** 🟢 **Deployer duties
are concrete work**: a Fundamental Rights Impact Assessment before go-live, and a student's
right to a meaningful explanation of the system's role in a decision. 🆕 🟢 **`OpenOLAT`
(Apache-2.0) is a European-origin permissive LMS** — 🟡 **placement unverified** (`ACTION HA`).

#### APAC

🆕 🟢 **Korea's enforcement posture is the news, and it changes the pitch:** the Ministry of
Science and ICT has signalled that **2026 is effectively a pilot period with limited
enforcement.** 🔵 **So Korea is a design-and-pilot year, not a compliance scramble** — sell
readiness, not remediation. 🟢 **Vietnam's 2026 decree names education among SIX high-risk
sectors**, specifically **automated assessment and behavioural monitoring**; 🔴 **sources
conflict on the deadline — p153 recorded in force `2026-03-01`, one source this pass puts the
high-risk education obligation at September 2027.** 🟢 **Both carried, neither quoted as
settled.** 🟢 **Vietnam's regime is extraterritorial (p153), so a LATAM or EMEA vendor selling
into Vietnam is in scope.** 🆕 🟢 **`ACTION GY` CLOSES**: the **2026 APEC Digital and AI
Ministerial Statement** is a ministerial education source — it commits member economies to
broadening education access and sharing digital-education practice. Japan: an **AI Basic Plan**
plus a transition to official digital textbooks. India: 🔴 a proposed licensing regime for AI
training that industry warns will slow adoption.

#### LATAM

🆕 🟢 **The adoption figure this shelf has been unable to quote for six passes now has an
independent corroboration WITH a readable sample.** 🟢 **A UNAM study of `22 941` students and
`7 319` faculty finds `91.5%` of students and `75%` of faculty using AI tools.** 🔵 **Set
against the Digital Education Council × Tecnológico de Monterrey pair (`92%` / `79%`) whose
host is unresolvable (`ACTION GJ`), the UNAM figures land within 0.5 and 4 points — 🟢 two
instruments, one named university, one readable denominator.** 🟢 **UNESCO IESALC (September
2026): 200 institutions across 19 countries, 87% using AI in at least one area, 74% in
teaching and learning, 🔴 26% with a formal strategy.** 🔵 **So the sale is governance depth,
with no external deadline to force it — an accreditation and quality-assurance argument.**
🔴 **A Colombian MinEducación roadmap (64 public universities, $412M, 2028) appeared on ONE
low-confidence host and is NOT adopted** — recorded in `intel/market.md` as unverified.

##### 🔴 What this page still cannot do, after p155

- 🔴 **`OpenOLAT` and `mentingo` are UNPLACED by region** (`ACTION HA`), and `OpenOLAT`'s
  European origin is an expectation this pass did not verify.
- 🔴 **`openeducat_erp`'s bundled non-LGPL paths are unenumerated** (`ACTION HB`).
- 🔴 **No star count for any platform row** (`ACTION GN`, second pass unreached).
- 🔴 **`mentingo` is unassessed beyond its licence and star count** — no read of its AI mentor,
  its data model, or whether it is multi-tenant. 🔵 **`ACTION HC`.**


## Pass 154 — 2026-10-12

🟢 **The platform map gains the layer it was missing: the INTEGRATION BOUNDARY.** p153 asked
the right question per platform — *what licence does my plugin inherit* — and answered it for
LMS and ERP rows. 🟢 **This pass adds the permissive standards layer that lets you avoid
inheriting anything at all**, plus 🔵 **the largest LATAM school platform on this shelf,
re-measured.**

### 🟢 The integration boundary — permissive rows that attach to copyleft platforms

🔵 **The structural fact `P43` keeps running into:** the big LMS rows are GPL (Moodle), AGPL
(Canvas, Open edX) or LGPL (BigBlueButton). 🟢 **You do not have to fork them.** Every one of
them speaks **LTI** and **SCORM/xAPI**, and the libraries that speak those are permissive.

| repo | licence (API detector) | ★ | `HEAD` | what it is, and why it is the boundary |
|---|---|---|---|---|
| 🟢 [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0** | **376** | `0b806bf` | 🟢 **An LTI tool framework.** Write your agent as an LTI tool, host it yourself, and 🟢 **nothing of Moodle's or Canvas's licence reaches your code** |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | **354** | — | 🟢 **A modern SCORM runtime in JavaScript.** The permissive way to make AI-generated content report completion and scores back to ANY conformant LMS |
| 🟢 [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | — | `948a378` | 🟢 **Carried from p153** — the permissive component boundary INSIDE an AGPL platform |
| 🟢 [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🟢 **MIT** | **515** | `e0e347f` | 🟢 **The MCP boundary onto a learner's real review queue** |

🔵 **The sentence a studio can take to a client.** 🟢 *"Your Moodle stays GPL and ours stays
ours: we attach over LTI with an Apache-2.0 framework and report results over SCORM with an
MIT runtime."* 🔴 **The alternative — a plugin inside the platform tree — inherits the
platform's licence, and on Canvas that licence is AGPL-3.0-ONLY with no `-or-later` route.**

### 🔵 The LATAM platform row, measured rather than remembered

| platform | licence | ★ | `HEAD` | what it is | where AI attaches |
|---|---|---|---|---|---|
| 🔵 [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** | **719** | 🔴 **`cd1da68` — see `T94`** | 🟢 **Self-described as the largest free-software education platform in Brazil** — municipal school management: enrolment, attendance, grades | Dropout early-warning on enrolment + attendance; 🔴 **a plugin inherits GPL-2.0 — and whether that blocks reuse in GPL-3.0 code depends on an election nobody has read** |
| 🔵 [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor) | 🟢 **Apache-2.0** | **583** | `94cedd7` | 🟢 **Brazilian open-source programming-education platform** (*"Plataforma gratuita e open-source de ensino de programação"*) | 🟢 **Permissive. Content generation, exercise grading, tutor agent** |
| 🔵 [`Universidade-Livre/ciencia-da-computacao`](https://github.com/Universidade-Livre/ciencia-da-computacao) | 🟢 **MIT** | **20 914** | `b995c11` | 🟢 **The largest Portuguese-language education repository this shelf has measured** — a self-taught CS curriculum | Curriculum-aware tutoring; it is CONTENT, not software |

🔴 **`i-educar` is this shelf's first GPL-**2.0** row, and the version matters more here than
anywhere else on the page.** 🔴 **If the election is `-only`, GPL-2.0 and GPL-3.0 code cannot
be combined**, so an agent written for `i-educar` could not be reused inside a GPL-3.0
platform — a problem no amount of care in the studio's OWN code fixes. 🟢 **If it is
`-or-later`, the route stays open**, exactly as p152 found for Moodle's 13 859 `-or-later`
notices.
🔴 **And the API CANNOT tell you which**: GitHub's detector reports the key `gpl-2.0` for both
elections, the same way `T85` found Canvas's `-only` elected BY OMISSION. 🟢 **So the one
question that decides reuse on Brazil's largest school platform is still unanswered** —
🔵 **`ACTION GX`**: read `i-educar`'s notice headers and settle the election.

### 🟢 Platform rows added to the map this pass

| platform | licence | ★ | what it runs | 🔴 **what YOUR plugin inherits** | where AI attaches |
|---|---|---|---|---|---|
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 🔴 **AGPL-3.0** | **1 718** | Course platform for companies, Teachable alternative | 🔴 **AGPL — network use counts** | Course authoring, cohort analytics |
| [`elmsln/elmsln`](https://github.com/elmsln/elmsln) | 🔴 **GPL-3.0** | **253** | Distributed course network (higher ed) | 🔴 GPL | Course-content pipeline |
| 🟢 [`haxtheweb/haxcms-php`](https://github.com/haxtheweb/haxcms-php) | 🟢 **Apache-2.0** | **130** | 🟡 **North America** — microsite/courseware CMS | 🟢 **Yours, with a patent grant** | 🟢 **Permissive courseware authoring front end** |
| [`edrys-org/edrys`](https://github.com/edrys-org/edrys) | 🟡 **MPL-2.0** | **336** | Remote-teaching platform, modular | 🟡 **MPL — file-level copyleft; your NEW files stay yours** | Live classroom agent, lab modules |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 🟡 **NOASSERTION** | **340** | 🟡 **North America** — AI advising for student success | 🔴 **UNKNOWN until the body is read** (`P47`) | Already AI-native: advising assistant |
| 🟢 [`studentinsights/studentinsights`](https://github.com/studentinsights/studentinsights) | 🟢 **MIT** | **134** | 🟡 **North America** — student-centred data systems for school districts | 🟢 **Yours** | 🟢 **Early-warning and intervention signals on real district data** |
| [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) | 🔴 **GPL-3.0** | **223** | 🟢 **An AI plugin that already lives INSIDE Moodle** — tutoring, quizzes, mind maps, RAG over course material | 🔴 **GPL-3.0 — the inheritance `P43` warned about, in a shipped artefact** | 🔵 **Read it as the reference implementation of the inside-the-tree route** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | **1 143** | 🟢 **Offline-first learning platform** — carried, now star-measured | 🟢 **Yours** | On-device models; LATAM rural, Africa, APAC islands |

🔵 **`moodle-ai-skill-navigator` is the row to show a sceptical client.** 🟢 **It proves the
inside-the-tree route works** — tutoring, quiz generation and RAG over course material, in
production Moodle. 🔴 **And it proves the price: it is GPL-3.0, because it had to be.**

### 🟢 The two routes, side by side, now that both have real rows

| | 🔴 **inside the tree** | 🟢 **over the boundary** |
|---|---|---|
| the row that proves it | `moodle-ai-skill-navigator` (GPL-3.0, 223 ★) | `tsugi` (Apache-2.0, 376 ★) + `scorm-again` (MIT, 354 ★) |
| your licence | 🔴 **the platform's** | 🟢 **yours** |
| deploy | inside the client's Moodle | 🟢 **your own service, any client LMS** |
| reach | 🟢 **everything the platform's internals expose** | 🔴 **only what LTI/SCORM/xAPI expose** |
| when it is right | deep gradebook//course-format work | 🟢 **tutoring, content generation, analytics — i.e. most engagements** |

##### 🔴 What this page still cannot do, after p154

- 🔴 **`advisingapp` is `NOASSERTION` and unread** — a 340 ★ AI-native higher-ed platform whose
  licence this shelf cannot state. 🔵 **`ACTION GU`** covers it.
- 🔴 **Licences on this page are the API detector's except where p153 body-read them.** The
  ERP problem p153 named (`openeducat` README-declared, `frappe/education` ~20 B grant by
  reference) is UNCHANGED — the API cannot fix a grant by reference either.
- 🔴 **No LTI-conformance claim was tested.** `tsugi` says LTI; nobody on this shelf has run
  it against a Canvas or Moodle instance. 🔵 **`ACTION GW`**.

## Pass 153 — 2026-10-12

🟢 **The vertical platforms now carry a licence read from the FILE BODY plus a live `HEAD`**
— and 🔴 **the two ERP-class rows, which are the ones a studio bills against, are the two
whose licence cannot be read that way.**

### 🟢 The platform map — what it is, what it costs you in licence terms, where AI attaches

🔵 **The column that decides the engagement is not "what does it do". It is "what licence
does my code inherit when I plug in".** 🟢 **`P43`'s question, answered per row.**

| platform | what it runs | licence (file body) | 🔴 **what YOUR plugin inherits** | where AI attaches |
|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | The world's most-deployed LMS | 🟡 **GPL-3.0-or-later** (35 147 B) | 🔴 **GPL** — 🟢 **but `-or-later` leaves a relicensing route open** | AI subsystem + plugin API; LTI |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | HiEd LMS, strong in NA | 🔴 **AGPL-3.0-ONLY** — elected **by omission** in 16 896 files (`T85`) | 🔴 **AGPL, and NO `-or-later` route** — 🔴 **network use counts as distribution** | 🟢 **LTI, or an external MCP server** — `vishalsachdev/canvas-mcp` (MIT, 290 ★) |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | MOOC-grade, corporate + government | 🔴 **AGPL-3.0** | 🔴 AGPL inside the platform | 🟢 **`XBlock` (Apache-2.0) — the permissive component boundary** |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | University-governed LMS | 🟢 **ECL-2.0** | 🟢 **Permissive. Apache-derived** | 🟢 **The copyleft-free LMS route.** 🔴 Its one GNU notice is VENDORED TrimPath, not Sakai's (`T86`) |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | Virtual classroom, LMS-native | 🟡 **LGPL-3.0-or-later** | 🟡 **LGPL — linking is permitted**; modification is not | Recording/transcript pipeline for AI summarisation |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **Offline-first learning platform** | 🟢 **MIT** | 🟢 **Yours** | 🟢 **On-device models.** 🔵 **The row for low-connectivity: LATAM rural, Africa, APAC islands** |
| [`netless-io/flat`](https://github.com/netless-io/flat) | Synchronous classroom, complete | 🟢 **MIT** (1 062 B) | 🟢 **Yours** | Live tutoring agent, co-browsing, whiteboard capture |
| [`OpenVidu/openvidu`](https://github.com/OpenVidu/openvidu) | Self-hosted real-time video | 🟢 **Apache-2.0** (11 357 B) | 🟢 **Yours, with a patent grant** | Real-time transcription, attention/engagement signals |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **Permissive SIS** | 🟢 **MIT** (1 094 B) | 🟢 **Yours** | 🟢 **Dropout prediction on enrolment + attendance** |
| [`Ilyas-Codes/eCourse`](https://github.com/Ilyas-Codes/eCourse) | Lightweight LMS | 🟢 **MIT** (1 062 B) | 🟢 **Yours** | Course generation, assessment drafting |
| [`geli-lms/geli`](https://github.com/geli-lms/geli) | E-learning platform | 🟢 **Apache-2.0** (11 358 B) | 🟢 **Yours** | Content pipeline |
| [`openfun/richie`](https://github.com/openfun/richie) | Education portal CMS (Django+React) | 🟢 **MIT** (1 079 B) | 🟢 **Yours** | 🟢 **Permissive front end for an AGPL LMS** |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | School management / SIS | 🔴 **GPL-3.0** (35 121 B) | 🔴 GPL | Attendance + grade signals for an early-warning agent |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **Education ERP on Odoo, 73+ modules** | 🟡 **LGPL-3.0 — README-declared, NOT file-read** | 🟡 LGPL if the README is right | Admissions, finance, prospect CRM |
| [`frappe/education`](https://github.com/frappe/education) | School management on Frappe/ERPNext | 🟡 **GPL-3.0 by a ~20-byte `license.txt`** | 🟡 GPL if the one-liner binds | Admissions, scheduling, attendance |

🟢 **All 15 verified live this pass: `git ls-remote` 15 of 15, with a firing negative
control.** 🟢 **13 of 15 licences read from the file body.**

### 🔴 The ERP problem, stated for the people who sell the work

🔵 **Odoo and ERPNext are where an education engagement becomes an ERP engagement, which is
where the budget is.** 🔴 **And they are the two rows on this page whose licence a studio
cannot read the way it reads the other thirteen:**

- 🔴 **`frappe/education`'s entire licence file is the sentence `License: GNU GPL V3`** —
  ~20 bytes where a real GPL-3.0 body is 35 147. 🔴 **GitHub's detector declines it; so
  does every body-marker matcher.** 🆕 **A GRANT BY REFERENCE** — `T85`'s omission shape in
  a new location.
- 🔴 **`openeducat_erp`'s LGPL-3.0 comes from its README**, and 🔴 **`lumen` proved this
  pass that a README can contradict the file it links to** (`T89`).

🟢 **Both are usable. Neither licence should be quoted to a client's legal team from this
page** — clone and read, or ask the maintainer (`ACTION GQ`). 🔵 **That sentence is worth
more than a confident table row, because the confident row is what gets repeated in a
proposal.**

### 🟢 The Moodle-vs-Canvas decision, now with the asymmetry that settles it

🔵 **`P43` asked which platform to attach to. p152 measured the election; this page states
the consequence:**

| | Moodle | Canvas |
|---|---|---|
| licence | 🟡 GPL-3.0-**or-later** | 🔴 AGPL-3.0-**only** |
| 🟢 **relicensing route** | 🟢 **OPEN** — `-or-later` admits a future GPL version | 🔴 **CLOSED** — `-only`, and 🔴 **elected by OMISSION in 16 896 files**, so nothing in the tree ever says so out loud |
| network use | GPL: distribution only | 🔴 **AGPL: serving it over a network IS distribution** |
| 🟢 **the permissive route** | plugin inherits GPL → 🟢 **go out to LTI** | 🟢 **go out to an external MCP server** — `canvas-mcp` (MIT) talks to Canvas without linking into it |

🟢 **So the recommendation inverts by deployment model, not by feature set.** For a
client who will **self-host and extend privately**, Moodle's `-or-later` is the safer
substrate. For a client on **Canvas**, 🔴 **do not build inside the platform** — 🟢 **build
an external MCP server**, which is exactly what the shelf's most-starred agent row
(`vishalsachdev/canvas-mcp`, MIT, 290 ★, 102+ tools) already is. 🔵 **That is the strongest
architecture recommendation on this shelf, and it is a licence consequence rather than an
engineering preference.**

### 🟢 Regional fit, because the same platform is not the same sale everywhere

| region | the platform argument that lands |
|---|---|
| **North America** | 🔴 **Canvas dominates HiEd** → 🟢 **external-MCP architecture, plus a data-flow audit for California `AB 1159` / Idaho `SB 1227`.** `zavora-ai/mcp-student-records`' FERPA logging is the demonstrable artefact |
| **EMEA** | 🟢 **Moodle + Open edX institutional base** → 🟢 **sell the live Article 50 transparency duty now and the `2027-12-02` high-risk programme as a roadmap.** 🟢 OECD's purpose-built-over-general-purpose line favours a composed stack |
| **APAC** | 🔴 **Vietnam's extraterritorial law names education high-risk and is in force** → 🟢 **approval gates and audit logs are a compliance deliverable, not a nice-to-have.** `BetterSEQTA-Plus` (MIT) is the region's own measured artefact |
| **LATAM** | 🟢 **No external deadline** → 🟢 **sell on accreditation and quality.** 🟢 **`kolibri` (MIT, offline-first) and `academico` (MIT, SIS) fit rural connectivity and thin budgets** — permissive, so the institution keeps what it pays for |
| **Global** | 🟢 **`sakai` (ECL-2.0) is the answer whenever copyleft is a blocker at all** |

##### 🔴 What this page still cannot do, after p153

- 🔴 **Two of fifteen licences are not file-read** (`frappe/education`, `openeducat_erp`).
- 🔴 **No election was re-measured this pass.** The `-only`/`-or-later` verdicts are
  p152's, and 🔴 **p152's clones no longer exist** — the container is ephemeral.
- 🔴 **No star counts and no activity measures for any platform row** (`ACTION GN`).
- 🔴 **`H5P`, `Open Tutor AI CE`, `Moodle Workplace` and the national K-12 platforms
  catalogued in earlier passes were NOT re-verified this pass** — the 15 rows above are the
  ones that were, and the rest stand on their original measurement with its date.
- 🔴 **The regional-fit table is an ARGUMENT, not a measurement.** No deployment counts per
  region exist on this shelf for any platform here.

## Pass 152 — 2026-10-12

🟢 **`ACTION GA` is DISCHARGED and the verticals stop being a negative control: they are
now the most consequential licence measurement on this shelf.** 🔴 **Two of the six
platform verdicts this page has implied are WRONG**, in two different ways, and 🟢 **one of
them changes what a studio may do with Canvas LMS.**

🟢 **And these six rows carry STAR COUNTS for the first time in 152 passes** — `T78` is
refuted on a channel this shelf had declared closed (see `intel/trends.md`, `T87`).

| platform | licence | ★ | forks | 🆕 **election** | what a fork may relicense to |
|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | **GPL-3.0** | **7.5k** | — | 🟢 **`-or-later`** — 13 859 of 14 024 notices | 🟢 **GPL-3.0 or any later GPL** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | **6.9k** | 3.0k | 🔴 **`-only`, by OMISSION** — 16 896 files | 🔴 **AGPL-3.0 ONLY. Not "or later".** |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | **AGPL-3.0** | **8.2k** | 4.4k | 🟡 **UNSTATED per-file** (root-only surface) | 🟡 **ask — but the README says *"version 3 … unless otherwise noted"*** |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | **LGPL-3.0** | **9.2k** | 6.0k | 🟢 **`-or-later`** — 255 of 263 notices | 🟢 **LGPL-3.0 or any later LGPL** |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | **1.2k** | 1.0k | 🔴 **NONE — the one hit is VENDORED** | 🟢 **ECL-2.0 (permissive); the GPL hit is not Sakai's** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | **1.1k** | 1.0k | 🟢 **not applicable — 0 notices** | 🟢 **anything MIT allows** |

🟢 **Six of six sidebar licences independently CONFIRM what this page already said**, read
from a second channel this pass. 🔵 **That is the negative control still doing its job**:
the licence *identities* on this page have now been corroborated twice (p150's hand read of
the licence files, p152's sidebar read), 🔴 **while the licence *terms* turn out to have
been unmeasured all along.**

### 🔴 The Canvas LMS finding, which is the one to take into an engagement

🔴 **`instructure/canvas-lms` carries a complete AGPL notice in 16 905 of 19 286 source
files — 87.7%, the highest notice rate on this shelf — and NOT ONE of them says "or later".**

    # Canvas is free software: you can redistribute it and/or modify it under
    # the terms of the GNU Affero General Public License as published by the Free
    # Software Foundation, version 3 of the License.

🔴 **That sentence is an election.** It is the FSF's own `-only` form, expressed by
**omitting** the or-later clause rather than by writing the word "only" — 🔴 **so every
matcher on this shelf reads it as `SILENT`, the same verdict it gives a file with no notice
at all.** 🆕 **`T85`.**

🔵 **What it changes in a room.** `P38` step 4 has been saying the election is UNSTATED, so
ask the author. 🔴 **For Canvas that advice is wrong and would waste a client's time**: the
answer is in the tree 16 896 times. 🟢 **Say instead: a Canvas fork is AGPL-3.0-only, so a
future AGPL-4 is not a relicensing route, and the §13 network-use obligation is fixed at
version 3's wording.** 🟢 **A Moodle fork does have the or-later route.** 🔵 **That
difference is a real decision input between the two platforms and this shelf could not state
it before this pass.**

### 🔴 The Sakai finding — this page would have published a licence that is not Sakai's

🔴 **Sakai's single `-or-later` hit is `library/src/webapp/js/trimpath-template-latest.js`**
— *"TrimPath Template. Release 1.0.38. Copyright (C) 2004, 2005 Metaha"*, dual
GPL-2.0-or-later / Apache-2.0. 🔴 **A bundled third-party library, not Sakai's code.**

🟢 **Sakai elects nothing and remains ECL-2.0**, which is the permissive reading this page
has always carried. 🔴 **But the instrument attributed a vendored GPL to an ECL-2.0
project**, and `SKIP_DIRS` cannot catch it: it excludes `vendor/`, and this copy lives under
`library/src/webapp/js/`. 🆕 **`T86`**, measured and **not** fixed — 🔵 **`ACTION GF`.**

🔴 **The same defect reaches Open edX**, whose only notice-bearing file is
`common/test/data/uploads/jschannel.js`, also vendored. 🟢 **So Open edX's FIRST-PARTY
per-file notice surface is zero**, and its silence is a root-only licence surface rather
than a declination.

### 🟢 What `ACTION GA` actually settled, stated against its own falsifier

> 🔴 *Refuted if the verticals are also silent, 6 of 6.*

🔴 **It did not fire: 3 of 6 state an election.** 🟢 **So `T81` is CONFINED to the small
rows** and `P38`'s "ask the author" stays row-specific rather than becoming universal. 🔵
**And the four large copyleft codebases p151 flagged as "exactly the kind that DO carry
per-file headers" split two ways**: Moodle and BigBlueButton carry them and elect;
Canvas carries them and declines; Open edX does not carry them at all.

🟢 **Instrument, with the reproduction control and 25 offline tests:**
[`p152-vertical-election`](../compose/code/p152-vertical-election/README.md) ·
[the verticals result](../compose/code/p152-vertical-election/result.verticals.2026-10-12-p152.tsv) ·
[the omission result](../compose/code/p152-vertical-election/result.omission.2026-10-12-p152.tsv).
🔵 **105 727 source files over six `--depth 1` clones, 6 of 6 OK.**

### 🔴 What this page still cannot do

- 🔴 **The `-only` / `-or-later` election is still unmeasured for every vertical this page
  does NOT list.** Six platforms were cloned; the page names no others, so there is no
  hidden population — 🟢 **said so it is not read as six-of-many.**
- 🔴 **No notice-to-subject attribution.** `sakai`'s row is published with a verdict this
  page knows is wrong, because dropping it would hide `T86`. 🔵 **`ACTION GF`.**
- 🔴 **The positive control degrades on big trees and the figure is given rather than
  hidden**: it fires on **10 of 161** licence bodies here, against 7 of 7 on p151's small
  rows, because these six trees bundle 161 licence files that are mostly vendored
  MIT/Apache. 🔵 **`ACTION GG`.**
- 🔴 **Star counts are rendered values** (`7.5k`, `6.9k`), not exact integers, and carry the
  shelf's `K-3CIFRAS` band — 🟢 **a band, named, not a false precision.**

## Pass 151 — 2026-10-12

🟢 **The six vertical platforms are the negative control that bounds `T77`, and p151 keeps
them in that role** — their licences were known independently of this shelf's matcher, and
p150 re-measured **6 of 6 correct**. 🔵 **p151 changes nothing about them and says so**
rather than re-stating six values as if they had moved.

| platform | licence | why it is the control |
|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | **GPL-3.0** | 🟢 a plain GPL file — the exact shape the retired matcher called `AGPL-3.0` |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | **AGPL-3.0** | 🟢 the true positive |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | 🟢 second true positive |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | 🟢 permissive, offline-first — still the one row a studio can build on without a copyleft conversation |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | **LGPL-3.0** | 🟢 the third GNU family, which the title surface must separate from the other two |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 🟢 non-GNU, and the reason `ECL-2.0` is now a title rung in `lib/` |

### 🔴 What p151 did NOT measure on the verticals, stated so it is not assumed

🔴 **The `-only` / `-or-later` election was NOT measured on these six.** `ACTION FO` ran over
the **7 connector/agent GNU rows** and found **0 elections in 1 513 files**; 🔴 **the
verticals were not in that population.** 🔵 **So `T81` is NOT claimed for `moodle`,
`edx-platform`, `canvas-lms` or `bigbluebutton`** — four large, long-lived copyleft
codebases, which are exactly the kind that *do* often carry per-file headers. 🟢 **An
engagement that forks one of them must read its election directly, and the instrument to do
it is committed**:

    python3 compose/code/p151-election-surface/election.py <clones-dir> moodle_moodle …

🔵 **This is the highest-value unmeasured thing on this page**, and it is registered rather
than guessed: 🔵 **`ACTION GA`**.

### 🟢 Where the licence question now lives, for every page including this one

🟢 **[`compose/code/lib/licence_identity.py`](../compose/code/lib/licence_identity.py)**,
with the three GNU title rungs, the `ECL-2.0` rung these verticals required, and the AGPL
§13 clause as an independent second surface. **47 tests.** 🔵 **`P40`** is the pattern that
says why it lives there and not in the next instrument.

## Pass 150 — 2026-10-12 — the verticals are RE-MEASURED, and they are the negative control that bounds `T77`

🟢 **Six platform licences read from the tree this pass**, by sparse clone of the licence file
at `HEAD`. 🔵 **Done because `T77` established that this shelf's licence identifier is wrong on
five census rows, and the obvious next question is whether this page is wrong too.**

| platform | repo | licence read this pass | title line | matches this page |
|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 **GPL-3.0** | `GNU GENERAL PUBLIC LICENSE` / `Version 3` | 🟢 **yes** |
| **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | `GNU AFFERO GENERAL PUBLIC LICENSE` / `Version 3` | 🟢 **yes** |
| **Canvas LMS** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** | `GNU AFFERO GENERAL PUBLIC LICENSE` / `Version 3` | 🟢 **yes** |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | `Educational Community License, Version 2.0` | 🟢 **yes** |
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | `MIT License` | 🟢 **yes** |
| **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🟡 **LGPL-3.0** | `GNU LESSER GENERAL PUBLIC LICENSE` / `Version 3` | 🟢 **yes** |

🟢 **Six of six agree with what this page already said.** 🔵 **This is the result worth
having, and it is a negative control in two directions at once:**

1. 🟢 **`T77`'s damage is CONFINED to rows measured by `p145-licence-census`.** This page's
   values were read by hand from the licence files and are correct. 🔵 **Which bounds
   `ACTION FU`: the question is the census's population, not the shelf's.**
2. 🟢 **And it validates the FIX against six known-correct answers**, including every
   discrimination `T77` is about — **two AGPL-3.0, one GPL-3.0, one LGPL-3.0** — all three
   families distinguished correctly on the title surface. 🔵 **A fix that agreed with the
   broken matcher on these would be worthless; this one agrees with the hand reading.**

🔴 **The build bar on this page does not move.** Open edX and Canvas remain **network
copyleft** — the obligation that bites a studio offering a hosted product — and Moodle remains
**GPL-3.0**, distribution copyleft. 🟢 **Sakai (ECL-2.0) and Kolibri (MIT) remain the two
permissive routes**, and `P7`'s premise is unchanged.

### 🟡 What this page still carries from earlier passes, unchanged

🔵 **Stated plainly rather than implied fresh.** Only the six licence identifiers above were
re-measured this pass. Every other claim on the rows below — tool surfaces, version ladders,
plugin APIs, deployment shapes, the AI-feature readings — **carries its earlier pass's
measurement and its earlier pass's date.** 🟢 **The six re-measurements do not refresh them.**

### 🔴 What this pass did NOT do to the verticals

- 🔴 **No vertical was functionally exercised.** No Moodle plugin built, no Open edX course
  generated, no BigBlueButton session started. 🟢 **The measurement is a licence read, and
  that is all it claims.**
- 🔴 **OpenEduCat, H5P, ERPNext, Odoo and Tutor-CLI were NOT re-measured** — the six above
  were chosen as the ones whose licence family bears on a build decision. 🔵 **The unmeasured
  rows are a named gap, not a silent one.**
- 🔴 **`qxbao/qldt-hanu-mcp`'s correction reaches a vertical connector, not a vertical.** It
  is GPL-2.0, not `LGPL` — see [`repos/foundations.md`](../repos/foundations.md). 🔴 **A row
  this shelf filed as the most permissive copyleft is the least.**

**Pass 149, 2026-10-12.** 🔴 **No vertical was re-measured this pass, and that is a choice
worth stating rather than hiding.** 🔵 **All eight pre-registered actions (`EW`–`FD`) were
instrument, licence or policy work**, and 🟢 **none of them touched a vertical platform** — so
every row below carries p148's measurement and p148's date, unchanged.

🟢 **What did change for this page is a caveat on one of its claims**, and it is upstream of
the verticals rather than in them:

- 🟢 **`T72` is CLOSED as out-of-population.** The `Fedena` refusal that opens this page was
  the evidence for `T72` — *a licence named in words rather than in an SPDX token*. 🔴 **An
  extended matcher carrying eighteen common-title forms changed 0 of 58 rows on the connector
  and agent tiers**, so 🟢 **`T72` is confirmed specific to Fedena and must not be cited as a
  shelf-wide licence-reading gap.** 🔵 **The `Fedena` refusal itself stands untouched** — it
  rests on a clone with no licence body and a last commit in **2012**, not on a matcher.
- 🔴 **The licence figures on this page were read by `p147-licence-language`, which `T74` now
  shows carries an inverted grant ladder.** 🟢 **No vertical row is affected**: the inversion
  only moves a row that has **both** a package-manifest licence field and a README licence
  heading, and 🟢 **the three verticals read from a clone in p148 all have a `FILE` grant**,
  which is the top rung either way. 🔵 **Stated because the same module produced both sets of
  figures**, and a reader checking one should know the defect's reach.

🔵 **And one regional note for this page's engagement map.** 🟢 **The Africa null closed this
pass** (`P149-C`: AU Continental AI Strategy, Kenya, Nigeria, South Africa — see
`intel/market.md`). 🔴 **No African deployment of any platform on this page was measured**, and
🔴 **no adoption figure exists for any of the four jurisdictions** — so 🔵 **the right reading is
that the policy case for an African education engagement is now documentable while the
platform evidence is not.** 🟢 **`ACTION FI` registers the figure.**

**Pass 148, 2026-10-12.** 🔴 **The one permissively-licensed SIS that 2026 comparison tables
name does not ship a licence, and has not been touched in a decade.** 🟢 **Three vertical
licences are now read from a clone instead of off a rendered page.**

### 🔴 REFUSED — `Fedena` is not the Apache-2.0 SIS the market tables call it

A 2026 free-SIS comparison surfaced this pass lists **Fedena as Apache 2.0** and notes it as
*"the only Apache-licensed SIS in that table."* 🔴 **Both repositories were cloned and the
claim does not hold in the form a studio could rely on.**

| | `foradian/fedena` | `projectfedena/fedena` |
|---|---|---|
| grant | 🟡 **README prose** — *"Fedena is released under the Apache License 2.0."* | 🟡 **same prose** |
| 🔴 **own licence file** | 🔴 **NONE** | 🔴 **NONE** |
| licence-named files present | **14** — 🔴 **all vendored third-party** (FCKeditor, TinyMCE, `delayed_job` MIT, `index_length` MIT) | **14**, 🔴 **same** |
| tracked files | 4 568 | 4 608 |
| 🔴 **HEAD** | 🔴 **2012-10-12** | 🔴 **2016-07-20** |

🔵 **The grant is real prose and it is not nothing** — it is an unambiguous statement of
intent by the copyright holder. 🔴 **What is missing is the licence body**, which is `T21`'s
exact shape and the same defect this page already records against
`moodle-mcp-server-aql` — except that there the text existed in the monorepo and merely
failed to ship, while here 🔴 **no Apache-2.0 text exists in either repository at all.**

🔴 **And the maintenance finding is the decisive one for a studio.** A Rails 2-era codebase
last committed in **2012** is not a platform to put AI on top of, licence or no licence.
🟢 **Recorded here so the next pass does not re-surface the comparison table and re-adopt
the claim.** 🆕 **`T72`** also comes out of this row — see `agents/trending.md` for why the
census reads the grant as `UNIDENTIFIED` rather than `Apache-2.0`.

### 🟢 Vertical licences, read from the payload this pass

| platform | repo | 🟢 licence, from the clone | HEAD | buildable by Globant? |
|---|---|---|---|---|
| 🟢 **RosarioSIS** — K-12 SIS, PHP | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** — full body at `LICENSE` | 🟢 **2026-10-09** | 🔴 **no — strong copyleft.** 🟢 **Alive and the most actively maintained SIS on this page** |
| **OpenEduCat** — SIS+LMS+fees on Odoo | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0** — `LICENSE` names it, `COPYRIGHT` referenced | 🟢 **2026-09-07** | 🔴 **no.** 🔵 **p146 read this off a rendered page; it is now confirmed from source** |
| 🔴 **Fedena** — SIS, Rails | [`foradian/fedena`](https://github.com/foradian/fedena) | 🔴 **README-only "Apache License 2.0", no body** | 🔴 **2012-10-12** | 🔴 **no — and abandoned** |
| 🟢 **`mcp-student-records`** — SIS tool layer, Rust | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | 🟢 **Apache-2.0 — full body at `LICENSE`** | 🟢 2026 | 🟢 **YES** |

🔵 **The shape of this page has not changed, and now it is measured rather than asserted.**
🔴 **Every full-platform SIS a studio could deploy is copyleft or dead.** 🟢 **The one
permissive, live, Apache-2.0 row is a tool layer, not a platform** — 46 tools over a records
store, with a typed manifest proved set-identical to its router this pass (`ACTION EP`).

🟢 **So the composition `P31` describes is still the only permissive route to a records
layer, and it is now the only one this page can recommend without a copyleft caveat**:
Sakai (**ECL-2.0**) for the LMS + `mcp-student-records` (**Apache-2.0**) for the records
tools, with no GPL, LGPL or AGPL anywhere in the stack.

🔵 **Stated as a limit, not hidden:** that route buys a *tool surface* over student records,
not a registrar. A studio that needs enrolment workflows, fee management, timetabling and
report cards out of the box is choosing between **LGPL-3.0 (OpenEduCat)**, **GPL-2.0
(RosarioSIS)** and a build. 🟢 **That is a procurement conversation to have in week one, and
this page's job is to make sure it happens then rather than at integration.**
**Pass 147, 2026-10-12.** 🔴 **The AGPL warning this page carried on `moodle-mcp-server-aql`
was the wrong KIND of warning, and the correction matters commercially.** 🆕 🟢 **A
permissively-licensed SIS layer joins the page for the first time.**

### 🔴 CORRECTION — `moodle-mcp-server-aql` has a grant; what it lacks is a shipped licence file

🔴 **p145 recorded this row as declaring AGPL-3.0 with nothing behind it**, and this page
warned accordingly. 🟢 **`ACTION EF` tested that and refuted it.**

| question | answer |
|---|---|
| does a licence file exist? | 🟢 **yes** — `csmediapro/moodle-mcp-server`, monorepo root, **661 lines, complete AGPL-3.0 body** |
| is it in the published tarball? | 🔴 **no** |
| why? | 🔴 `packages/server/package.json` ships a **`files` allowlist of 16 globs**, none `LICENSE`; no `LICENSE` inside `packages/server/` |
| what kind of defect is it? | 🟢 **packaging** (`T21`'s shape), not a missing grant |

🔵 **The practical difference for a studio.** A missing grant means *you may not use this
without asking the author.* A packaging defect means *the grant is AGPL-3.0, the obligation
is live, and the file you need for your own compliance file is one directory up in the
repository.* 🔴 **The AGPL-3.0 network clause still fires on a hosted multi-tenant Moodle
connector** — which is how this row would actually be deployed. 🔵 **The warning stands;
its reason changes.**

### 🆕 🟢 The permissive SIS row this page did not have

🟢 **Every system-of-record row on this page has been copyleft or unlicensed.**

| platform | layer | licence | note |
|---|---|---|---|
| Moodle | LMS | 🔴 GPL-3.0 | copyleft |
| Open edX | LMS | 🔴 **AGPL-3.0** | 🔴 network clause fires on hosted multi-tenant |
| Canvas | LMS | 🔴 **AGPL-3.0** | 🔴 same |
| Chamilo, ILIAS | LMS | 🔴 GPL-3.0 | copyleft |
| OpenEduCat | education ERP | 🔴 LGPL-3.0 | weak copyleft |
| Sakai | LMS | 🟢 **ECL-2.0** | 🟢 **the one permissive major LMS** (p146) |
| 🆕 **`zavora-ai/mcp-student-records`** | 🆕 **SIS / MCP** | 🟢 **Apache-2.0** | 🆕 🟢 **46 tools, FERPA access log, approval-gated writes** |

🟢 **So a studio can now assemble LMS + SIS with no copyleft anywhere**: **Sakai**
(ECL-2.0) for the learning layer, **`mcp-student-records`** (Apache-2.0) for the records
layer and the agent surface over it. 🔵 **That is the first time this page can say that.**

🟢 **And it is the only row here that ships a machine-checked governance surface:**
`mcp-server.toml` declares a `risk_class` and a `requires_approval` flag per tool
(**23 of 46 require approval**), and `tests/manifest_test.rs` asserts approval on **11
named FERPA-sensitive writes** — `record_grade`, `record_attendance`, `send_communication`,
`set_student_status`, `add_accommodation`, `enroll`, `add_guardian`,
`record_mastery_evidence`, `place_hold`, `release_hold`, `assign_intervention` — plus
`risk_class = ExternalWrite` on `send_communication`. 🔵 **A procurement review asks for
exactly that list, and here it is enforced by CI rather than asserted in a datasheet.**

🔴 **Two limits, stated.** It is **Rust**, which is not most studios' default stack for this
layer. And 🔴 **nothing asserts the manifest's 46 names against the router's 46 `#[tool]`
names** — the counts meet at the literal `46` and set identity is never checked, so it is a
very strong property pin and **not** a bidirectional identity pin.

### 🟡 Two connector rows now have a deployment region

🟢 **`eth-moodle-mcp` → EMEA (Switzerland)** — its shipped `MOODLE_URL` default is **ETH
Zürich's** production Moodle and its auth flow names **nethz** and **SWITCHaai**. 🔵 **A
ready reference for a European university Moodle engagement, and a reminder that the EU AI
Act's Annex III obligations land on 2027-12-02 for exactly this deployment shape.**

🟡 **`mcp-canvas-lms` → APAC (Hong Kong)**, on `canvas.ust.hk` (HKUST) given as an example
rather than a default — a lead, not a placement.

**Pass 146, 2026-10-12.** 🆕 🟢 **The whole major-LMS layer was read on the licence axis for
the first time, and it has exactly ONE permissive member.** 🔴 **Six of the seven platforms
a studio would reach for are copyleft** — and the exception is not the one this page or the
wider market would have guessed.

### 🆕 🟢 The major open-source LMS/SIS layer, every licence read off its own page

🔵 **Read on the `WebFetch` channel, which `P146-I` found open while `clone` is refused and
`curl -sI` answers 403.** Each row's licence and star count is what the repository page
displayed on **2026-10-12**.

| platform | repo | licence | ★ | build bar |
|---|---|---|---|---|
| 🟢 **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | 1.2k | 🟢 **PASSES — the only one** |
| Moodle | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | 6.2k | 🔴 copyleft |
| Open edX | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | 8.2k | 🔴 **network copyleft** |
| Canvas LMS | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** | 6.9k | 🔴 **network copyleft** |
| OpenEduCat | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL-3.0 | 886 | 🔴 weak copyleft |
| Chamilo | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 | 1.0k | 🔴 copyleft |
| ILIAS | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 GPL-3.0 | 505 | 🔴 copyleft |

### 🆕 🟢 Why Sakai is the finding, and it is not a star-count finding

🟢 **ECL-2.0 is Apache-2.0 with one change**: its §3 patent grant is narrowed to the needs
of educational institutions. The rest of the text is Apache's. 🟢 **OSI-approved,
copyleft: no.** It is GPLv3-compatible and 🔴 **not GPLv2-compatible**.

🔵 **So the permissive/copyleft split in this vertical does not track maturity, adoption or
stars.** Sakai is the fourth-largest row here and the only one a studio can build a
proprietary derivative on without a reciprocal obligation. 🔴 **The two largest rows —
Open edX and Canvas — are both AGPL-3.0, the strongest copyleft in the set**, and AGPL's
network clause is triggered by exactly the deployment shape these platforms are used in:
hosted, multi-tenant, served over a network.

🔴 **What this does NOT say.** Copyleft is not a disqualification; it is a constraint on
where the boundary goes. The practical pattern on every GPL/AGPL row is unchanged and is
the one this page has recommended for twenty passes:

| approach | obligation | verdict |
|---|---|---|
| fork the platform, modify core, host it | 🔴 **source disclosure (AGPL: to every user)** | 🔴 avoid |
| 🟢 **build a separate agent service, talk to it over the REST/LTI API** | 🟢 **none on your code** | 🟢 **the pattern** |
| write a plugin inside the platform's tree | 🔴 likely derivative | 🔴 counsel first |

🟢 **Sakai is the row where the first option is also available**, which is worth knowing
before a client's procurement forces the question.

### 🔴 OpenEduCat — the Odoo-shaped candidate, read and licence-flagged

The vertical search for *"open source platform education ERP/CRM"* surfaced
**OpenEduCat** as the closest education analogue to Odoo's position in ERP: 🟢 **LMS, SIS,
fees and a parent app on one database**, built on the Odoo framework. 🔴 **It is
LGPL-3.0**, 886★ — 🔴 **outside this KB's MIT/Apache/BSD bar.**

🔵 **Recorded rather than dropped**, because the single-database LMS+SIS consolidation is a
real architectural position and this page had no row for it. 🔴 **An integrated system of
record is also the highest-copyleft-risk place to put agent logic**, since the agent and
the records live in one tree.

🔴 **Not verified this pass**: whether OpenEduCat's Odoo dependency pulls additional
licence obligations. Its upstream framework is itself LGPL-3.0 with a proprietary
Enterprise edition, and the interaction was not read.

# Education — vertical platforms you can customise

**Pass 145, 2026-10-12.** 🔴 **The Moodle copyleft warning this page carried is corrected:
the AGPL-3.0 row is `moodle-mcp-server-aql`, it declares the licence in `package.json` and
ships no licence text at all.** 🔴 **And three rows on the LATAM system-of-record tier —
the tier this page recommends as an entry point — carry no licence whatsoever.**

### 🔴 CORRECTION — Moodle's npm connectors, all three measured, and the copyleft row named

p144 wrote that *"the one Moodle connector published to npm whose source is reachable is
AGPL-3.0"*. 🔴 **The reachability qualifier is now gone** — `P145-A` shows all three were
always readable, the instrument was excluding the tree they ship — and the licence picture
is more specific than p144 could state.

| Moodle npm connector | tools | grant | licence |
|---|---|---|---|
| `eth-moodle-mcp@1.3.3` | 🟢 **18 literal** | 🔴 `package.json` only | MIT |
| `@ink-waffle/moodle-mcp@0.2.0` | 🟢 **16 literal** | 🔴 `package.json` only | MIT |
| `moodle-mcp-server-aql@0.1.7` | 🔴 **plugin-extensible** | 🔴 `package.json` only | 🔴 **AGPL-3.0** |

🔴 **None of the three ships a licence file.** 🔵 **Two declare MIT and one declares
AGPL-3.0, and all three declarations are equally unbacked** — so the build decision rests
on a string in a manifest rather than on a grant, for the permissive rows as much as for
the copyleft one.

🔴 **`moodle-mcp-server-aql` is the row to keep away from a client deliverable**, and for
two reasons that compound. It declares **AGPL-3.0**, and it is the one connector on these
shelves whose **tool surface grows with the plugins installed at run time**
(`dist/server/factory.js:131` pushes a descriptor per discovered plugin). 🔵 **A copyleft
licence attaches to modification, and a plugin architecture is an invitation to modify.**

🟢 **The two MIT-declared rows are the Moodle attachment points to use** — `eth-moodle-mcp`
at 18 tools, `@ink-waffle/moodle-mcp` at 16 — with `ACTION EF`'s outcome as the condition on
the third.

### 🔴 The LATAM system-of-record tier has a licence hole, and it is in the rows this page recommends

🔴 **Three of the eight wholly unlicensed connector rows are on the tier this page sends
engagements to:**

| row | platform | region | grant |
|---|---|---|---|
| `frjunioalves/suap-mcp` | **SUAP** (Brazil) | LATAM | 🔴 **NONE** |
| `SIU-Toba/docker-guarani` | **SIU-Guaraní** (Argentina) | LATAM | 🔴 **NONE** |
| `eugeborzone/Auto_Grade_Guarani` | **SIU-Guaraní**, auto-grading | LATAM | 🔴 **NONE** |

🔵 **`SIU-Toba/docker-guarani` is the vendor-adjacent one** — the SIU-Guaraní
containerisation, under the consortium's own GitHub organisation, and still with no licence
file at HEAD. 🔴 **An unlicensed artefact published by the platform consortium is a
different problem from an unlicensed hobby connector**: it cannot be routed around by
asking a single author.

🔴 **`eugeborzone/Auto_Grade_Guarani` is the row where two gaps meet.** Auto-grading is the
named high-risk use case under the EU AI Act (`T3`), and in LATAM it is the use case with
the highest teacher-adoption base (`T41`). 🔵 **The row that sits on the most demand and the
most regulation is the row with no grant at all.**

🟡 **And the copyleft rows on this tier are named rather than discovered later**:
`despedite/siu-guarani`, `Agso-o/sigaa-calendar` and `fabrica-de-inovacao/expeditto` are
GPL-family. 🟢 **Readable, auditable, demonstrable — not foldable into a client
deliverable** without accepting the obligation.

### 🟢 Blackboard Learn — the placed row is unlicensed, and that changes the recommendation

🔴 **`karkarkins/BlackboardAssistantMCP`, the row `ACTION DK` placed in p143 on a login URL
it configures itself, carries no licence file at HEAD.** 🔵 **Placement and measurement do
not make a row usable** — this page has spent four passes establishing where that connector
is deployed, and it cannot be built on as it stands.

🟡 **`P1ckle3/blackboard-mcp` is likewise unlicensed**; `felipedias-ie/blackboard-mcp` and
`NiccoloSalvini/mcp-blackboard-ucsc` do carry grants. 🟢 **So the Blackboard attachment
point stands, on the two licensed rows**, and `ACTION EE` tests whether the unlicensed pair
are forks of a licensed parent.

### 🟡 No ERP/LMS platform row was added or removed this pass, and that is stated rather than padded

🟢 **The platform tier below — Moodle, Open edX, Sakai, Canvas, ILIAS, OpenOLAT, Chamilo,
OpenEduCat, ERPNext, SIGAA/SUAP, SIU-Guaraní, WordPress + Tutor LMS — is unchanged.** 🔵
**The search channel returned one vendor's own comparison site and nothing else this pass**
(`openeducat.org`, nine localisations of one page), which is a null on the platform channel
and is recorded as one. 🔴 **No row was invented to fill it.**

🟢 **One citation from that channel is worth keeping**, because it agrees with this page's
own licence column: the permissive/copyleft split it describes for LMS platforms — Moodle
**GPL**, Canvas open-core, Open edX **AGPL** at the application layer — matches what
`ACTION DA` and `ACTION CS` measured from the artefacts. 🔵 **A vendor page that agrees with
the measurement is a corroboration; it is not promoted to a source.**


**Pass 144, 2026-10-12.** 🆕 **A second European institutional tenancy, named in shipped
source: Universidad de Navarra.** 🔴 **And the Moodle entry gains a copyleft warning the npm tier
had been hiding** — the one Moodle connector published to npm whose source is reachable is
**AGPL-3.0**.

### 🆕 🟢 Moodle — the reachable npm connector is AGPL-3.0, and that changes the build decision

[`p144-npm-source-parity`](../compose/code/p144-npm-source-parity/README.md). Moodle itself is
**GPL-3.0** and always has been; the question for a studio is the *connector* layer on top.

| connector | repo | licence | tools | verdict for a studio build |
|---|---|---|---|---|
| `moodle-mcp-server-aql@0.1.7` | [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** | **14** | 🔴 **STOP-SHIP as a dependency.** AGPL reaches across a network boundary |
| `@ink-waffle/moodle-mcp@0.2.0` | 🔴 none reachable | 🟢 MIT (declared in npm) | **16** | 🟡 **Permissive but unverifiable** — no `repository`, no `homepage`, no `sourcesContent` |
| `eth-moodle-mcp@1.3.3` | 🔴 none reachable | 🟢 MIT (declared in npm) | **18** | 🟡 ETH Zurich lecture-PDF scope; permissive but unverifiable |

🔵 **The permissive Moodle connectors are the ones nobody can read, and the readable one is
copyleft.** 🔴 **That is the opposite of a usable supply position**, and it is a direct
consequence of `P144-B`: a declared SPDX identifier in npm metadata is not a licence file in a
repository, and p138 already recorded that *"a licence identifier is not a licence"*.

### 🆕 🟢 Universidad de Navarra — the second institutional tenancy this page can name

[`p144-author-window-strict`](../compose/code/p144-author-window-strict/README.md).

| row | evidence | institution | region |
|---|---|---|---|
| 🟢 [`ruud0/aula-virtual-mcp`](https://github.com/ruud0/aula-virtual-mcp) | `server.py:19` — `BASE_URL = "https://aula-virtual.unav.edu"` | **Universidad de Navarra**, Pamplona | 🟢 **EMEA** (Spain) |

🟢 **The LMS behind it is *Aula Virtual ADI*, the university's own learning platform.** 🔴 **And
the disambiguation matters**: `MiAulario`/Sakai belongs to the **Universidad Pública de
Navarra** — a different institution in the same city. 🔵 **Two universities, one city, two
unrelated LMS stacks** is exactly the sort of pair a ccTLD-level census collapses.

🔴 **The row itself is UNLICENSED and four commits long.** 🔵 **It is a tenancy signal, not a
software asset**: it tells a studio that a named Spanish university's Aula Virtual has been
scouted in the open, and nothing more.

### 🔵 Blackboard Learn — `P143-G` confirmed on the row that motivated it

`nitsuah/bb-mcp` was the last `UNMAPPED` row and it stays unmapped, with the reason now
measured rather than suspected. Of its URLs: `developer.blackboard.com` **×9** is the vendor's
own developer estate, and `blackboard.example.edu`, `mcp.example.edu` and `push.example.edu` are
**placeholders**. 🔴 **241 commits and not one institutional host.**

🔵 **This is the case `P143-G` predicted**: a Blackboard connector can be large, active and
MIT-licensed and still place nothing, because the only real hostname in it belongs to Blackboard.

### 🟡 No ERP/LMS platform row was added or removed this pass, and that is stated rather than padded

The mandated vertical query — `open source platform education ERP CRM MIT Apache` — returned
**one vendor's glossary across ten locales** and no new platform. 🔵 **It did confirm the standing
entries**: **OpenEduCat** is **LGPLv3** on **Odoo**, with **Moodle** (LMS) and **Koha** (library)
named as the reference open-source education systems. 🔴 **No MIT- or Apache-licensed education
ERP surfaced**, which is the fourth pass in a row this page has recorded that absence.

**Pass 143, 2026-10-12.** 🆕 **A vendor tier this page has never had: the company that
maintains an Open edX extension point, placed in Colombia.** 🆕 **And the Blackboard entry
gains a named institutional tenancy plus a warning about the four hosts that look like
tenancies and are not.**

### 🆕 🟢 Open edX — the extension point has a commercial maintainer, and it is LATAM

[`p143-edunext-jurisdiction`](../compose/code/p143-edunext-jurisdiction/README.md).

| platform | the vendor fact | licence posture |
|---|---|---|
| **Open edX** *(already on this page)* | 🆕 🟢 **`eduNEXT` — a Colombian company — is author of record on `openedx/openedx-filters`**, the hook interface third-party Open edX customisation runs through, set 2026-10-02 during the `modernize` campaign. Placed **LATAM** on 13 authors committing `-0500` in both DST windows across 1 485 commits, with `edunext.co` on **998 of them (67%)** | `openedx-filters`: 🔴 **AGPL-3.0-or-later.** 🔵 The eduNEXT `eox-*` extension family is a separate licence question this pass did not read |

🔵 **Why this belongs on a platforms page rather than only on a market map.** A studio
customising Open edX does not touch the core — 🟢 **it writes against the filters and hooks
interface**, and the maintainer of that interface decides what is extensible. 🟢 **For a LATAM
engagement that maintainer is in the same region and the same timezone**, which is a delivery
fact, not a trivium. 🔴 **For any engagement it is an AGPL-3.0-or-later interface**, so the
obligation travels with anything built through it that is distributed or served.

🔴 **What is NOT claimed:** no licence has been read for the `eox-*` repositories themselves,
and nothing here is a grant for them. 🔵 **The jurisdiction finding and the licence question
are separate**, and only the first was asked.

### 🆕 Blackboard Learn — a named institutional tenancy, and the four hosts that place nothing

[`p143-vendor-tenancy`](../compose/code/p143-vendor-tenancy/README.md).

| platform | tenancy evidence | what it tells a studio |
|---|---|---|
| **Blackboard Learn** *(already on this page)* | 🆕 🟢 **`ncat.blackboard.com` — North Carolina A&T State University**, from `karkarkins/BlackboardAssistantMCP`'s own `README.md`: `BB_LOGIN_URL=https://ncat.blackboard.com/`. 🆕 `ntnu.blackboard.com` ×8 — **NTNU, Norway** (🟡 in a test fixture, not shipped source) | 🟢 **Two named public institutions on Blackboard, one US and one Norwegian**, each with an open connector already written against it |

🔴 **And the negative finding, which is the more useful half.** Of 6 rows in this KB's
44-row connector population carrying any Blackboard/Canvas host, 🔴 **4 carry only the vendor's
own estate**:

| host | occurrences | what it is |
|---|---|---|
| 🔴 `developer.blackboard.com` | **19** | the vendor's developer portal — 🔴 **the single most common vendor-domain string in the whole population, and it places nothing** |
| 🔴 `basic-doc-viewer.eu.api.blackboard.com`, `notif-websockets-eu-central-1.prod.notifications.api.blackboard.com`, `prod01-euc1-prod01-xythos.prod.files.blackboard.com`, `files.blackboard.com` | 1 each | vendor infrastructure |
| 🔴 `community.canvaslms.com` | 1 | vendor community site |
| 🔴 `example.blackboard.com`, `your-instance.blackboard.com`, `school.instructure.com`, `myuni.blackboard.com` | 1 each | documentation placeholders |
| 🔴 `alt-5f0d0e6d23ee0.blackboard.com`, `alt-0123456789abc.blackboard.com` | 1 each | real tenancies whose label names nobody |

🔵 **This is the `your-institution.instructure.com` lesson one layer up.** The frequent
host-shaped string under a vendor domain is the vendor's own, and a census that counts
`*.blackboard.com` as "institutions using Blackboard" would return 19 hits for Blackboard
itself. 🟢 **Only a single-label subdomain that is an institution's own abbreviation places
anything**, and in 44 repositories there are exactly **two**.

🔴 **`myuni.blackboard.com` was checked rather than assumed** to be a placeholder: it occurs in
`felipedias-ie/blackboard-mcp/test/auth.test.ts:145` in a list beside `blackboard.example.edu`
and `learn.university.edu`. 🔵 **Its neighbours settle it.**

### 🔵 SIGAA, SUAP and SIU-Guaraní — unchanged, and the licence question still unasked

The three national platforms added at p142 stand as written. 🔴 **No licence has been read for
SIGAA, SUAP or SIU-Guaraní and this page still does not assert one.** 🟢 **One addition from
this pass:** `SIU-Toba/docker-guarani` remains the only row on this page whose *platform vendor*
publishes on GitHub, and the probe re-confirmed its Argentine hosts (`siu.edu.ar`,
`colab.siu.edu.ar`, `repositorio.siu.edu.ar`) on a fresh clone.

**Pass 142, 2026-10-12.** 🆕 **Two national student-information platforms arrive on this page,
and they arrive with thirteen connectors already written against them.** 🔴 **And veraPDF — the
accessibility validator a studio reaches for when course material has a compliance obligation —
turns out to grant different licences per module.**

### 🆕 🟢 The platform tier this page was missing: Brazil's SIGAA/SUAP and Argentina's SIU-Guaraní

[`p142-americas-disambiguation`](../compose/code/p142-americas-disambiguation/README.md) placed
13 connector rows in LATAM by the hosts they hardcode. 🔵 **Read the other way round, those hosts
are a platform census** — and the platforms behind them are the ones a Brazilian or Argentine
engagement actually meets.

| platform | what it is | installations named in connector source | licence posture |
|---|---|---|---|
| 🆕 **SIGAA** — *Sistema Integrado de Gestão de Atividades Acadêmicas* | The academic-management system of Brazil's **federal** universities: enrolment, timetable, grades, course history | `sigaa.ufrn.br` (UFRN — the originating university), `sigaa.ufpe.br`, `sigaa.ufc.br`, `sigaa.ufpb.br`, `sigaa.ufpi.br`, `sigaa.sistemas.ufg.br`, `sigaa.sistemas.ufj.edu.br`, `sig.unb.br`, `sis.sig.uema.br` — **9 institutions across 7 connectors** | 🔵 **Not probed this pass.** SIGAA originates at UFRN and is adopted by federal institutions; no licence claim is made here, and 🔴 **this page does not assert one it has not read** |
| 🆕 **SUAP** — *Sistema Unificado de Administração Pública* | The administrative/academic system of Brazil's **federal institutes** (the IF network) | `suap.ifrn.edu.br` (IFRN — the originating institute), `suap.ifpi.edu.br`, `suap.ifsp.edu.br`, `acad.ifma.edu.br`, `campusparaiso.ifto.edu.br` | 🔵 Same caveat |
| 🆕 **SIU-Guaraní** | The student system of Argentina's **national** universities, under the SIU consortium | `siu.edu.ar`, `colab.siu.edu.ar`, `repositorio.siu.edu.ar`, `guarani.unq.edu.ar` (Quilmes), `servicios.unl.edu.ar` (Litoral) | 🟢 **`SIU-Toba/docker-guarani` is the consortium's own GitHub organisation** — a platform tier whose *vendor* publishes on GitHub, which is rare on this page |
| **Blackboard Learn** *(tenancy evidence added)* | Already on this page | 🆕 `ncat.blackboard.com` — a **tenancy subdomain**, the first on this page. 🔵 It names an institution exactly and carries no country | — |
| **Canvas / Instructure** *(negative evidence)* | Already on this page | 🔴 **`your-institution.instructure.com` is the single most common "hostname" across these shelves and it places nothing.** Worth stating: a Canvas connector's source usually names no real tenancy at all | — |

🔵 **Why this matters more than a row count.** This page's job is platforms a studio can customise.
🟢 **For Brazil and Argentina the attachment point is now specific**: not "an LMS", but SIGAA, SUAP
and SIU-Guaraní, with 13 open connectors naming 15 real installations between them. 🔴 **The
connectors remain one-person projects at 0–10 stars** — their value is that the integration
surface against three national platforms has been scouted in the open.

🔴 **And the honest gap on the same evidence:** no licence has been read for SIGAA, SUAP or
SIU-Guaraní, and nothing on this page should be taken as a grant for any of them. 🔵 **The
connectors are MIT/ISC; the platforms they target are a separate question this pass did not ask.**

### 🔴 veraPDF, the accessibility validator — the election is per-module

[`p142-verapdf-module-grant`](../compose/code/p142-verapdf-module-grant/README.md). A studio
validating PDF/UA on course material resolves modules, not the umbrella:

| coordinate | effective licence | ships licence text? |
|---|---|---|
| `org.verapdf:core:1.30.3` | **GPL-3.0 *or* MPL-2.0**, inherited at depth 4 | 🔴 **no** |
| `org.verapdf:validation-model:1.30.3` | **GPL-3.0 *or* MPL-2.0**, inherited at depth 4 | 🔴 **no** |
| 🟢 `org.verapdf:verapdf-xmp-core:1.30.3` | 🟢 **BSD-3-Clause — its own declaration** | 🔴 **no** |
| 🔴 `org.verapdf:verapdf-library:1.30.3` | the dual offer, in a parent | 🔴 **no jar exists** |

🔵 **Elect MPL-2.0 for the two that need an election, record BSD-3-Clause for the third, and do
not write "veraPDF is GPL-or-MPL" in a bill of materials** — it is true of two of the three
artefacts a build pulls. 🔴 **No jar carries licence text, so nothing a consumer unzips will tell
them any of this.**

**Pass 141, 2026-10-12.** 🔴 **Two of this page's platform rows change character.** Sakai's
`org.sakaiproject:kernel` aggregator is added to the inheritance ledger — it declares nothing
and inherits ECL-2.0 at depth 3, like its `impl` sibling. 🆕 **And a platform category this page
has never carried arrives through a connector: WordPress + Tutor LMS**, measured at 31 tools and
17 writes, with no licence.

### 🆕 🔴 The platform layer this page was missing: WordPress + Tutor LMS

[`hesham0-0nasser/tutor-lms-mcp`](https://github.com/hesham0-0nasser/tutor-lms-mcp) is not a
standalone MCP server. It is a **WordPress plugin** that exposes **Tutor LMS** — the WordPress
LMS plugin — to an agent over a hand-rolled JSON-RPC router mounted on `register_rest_route`,
with its own OAuth class. 🔵 **That makes WordPress an education platform tier on this page, and
it is the only one whose attachment point is a CMS plugin rather than an LTI launch or a REST
API.**

| measure | value |
|---|---|
| tools | **31**, from one static `TLMS_MCP_Tools::list_tools()` array — **0 conditionals**, so the surface is fixed by the build |
| 🔴 writes | 🔴 **17 of 33 distinct names** — `tutor_create_course`, `tutor_update_course`, 🔴 **`tutor_delete_course`**, plus topic and lesson writes |
| 🔴 licence | 🔴 **no file at `HEAD`** — 7 commits, HEAD **2026-05-26** |
| region | 🟢 **EMEA** — `+0300` on 7 of 7 commits |
| files | 6 PHP: `class-mcp-router.php`, `class-mcp-tools.php`, `class-mcp-auth.php`, `class-mcp-oauth.php`, `class-mcp-admin.php` |

🔴 **The missing licence is a harder stop here than elsewhere on this page.** WordPress's own
distribution terms assume GPL-compatibility for plugins, so the *"permissive by omission"*
reading that a reader might attempt on a bare npm package is not available — and p140's `T26`
cuts the other way too: there is no parent manifest to inherit from in a WordPress plugin.
🔴 **Unusable as shipped**, and worth watching precisely because the shape is right: a
course-authoring write surface on a platform with an enormous installed base.

🔵 **The architectural point for a studio is the attachment pattern, which is reusable
regardless of this row's licence**: WordPress already solves authentication, roles and REST
routing, so an MCP surface over a WP LMS is a router class plus a tool table. The licence is a
one-file fix the maintainer has not made.

### 🔴 Sakai: the aggregator declares nothing either, and now the whole family is measured

p140 corrected this page's claim that `sakai-kernel-api` and `sakai-kernel-impl` have *"opposite
licence posture"* — both are **ECL-2.0**, one by inheritance at depth 4. 🆕 **`ACTION DC` adds
the third member.**

| coordinate | own POM | inherits from | licence | depth |
|---|---|---|---|---|
| 🟢 `org.sakaiproject.kernel:sakai-kernel-api:25.2` | ECL-2.0 | — | ECL-2.0 | 2 |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl:23.3` | **NONE** | `org.sakaiproject:oss-parent:1` | ECL-2.0 | 4 |
| 🆕 🔴 `org.sakaiproject:kernel:23.3` | 🔴 **NONE** | `org.sakaiproject:master:23.3` → `org.sakaiproject:oss-parent:1` | ECL-2.0 | **3** |

🟢 **So Sakai's grant is consistent — ECL-2.0 throughout — and 2 of 3 artefacts state it
nowhere in their own files.** 🔵 **The whole family's licence rests on a single POM,
`org.sakaiproject:oss-parent:1`**, and `org.sakaiproject:master:23.3` between them declares
nothing, so a walk that stops at the first silent ancestor finds no grant at all. 🟡 A European
university's review burden on Sakai is therefore procedural rather than legal: the licence is
fine, the paperwork proving it is three fetches away, and **none of the jars ships the text**.

🟡 **p140's `org.sakaiproject:kernel:25.2` is 404 on Central, confirmed again** — Central holds
60 versions of that coordinate, latest **23.3**. 🔵 **So `sakai-kernel-api:25.2`'s parent chain
is genuinely broken upstream: its POM names a parent version that was never published**, and no
amount of walking fixes it. The row survives only because it declares its own licence. 🟢 A
clean example of why the walker reports a fetch failure as a failure rather than as an absence.

### 🔴 Open edX: the licence is impeccable at the wheel and absent in everything inside it

`ACTION DA` measured the six top-level packages inside `openedx-core` **1.9.1**: 🔴 **zero
licence files, zero SPDX headers and zero copyright lines across 237 Python files**, against a
distribution that declares `AGPL-3.0-only` and ships **35 139 bytes** of licence text in
`dist-info/licenses/`.
[`p141-package-grant-layer`](../compose/code/p141-package-grant-layer/README.md).

🔵 **For this page the consequence is concrete and routine.** The normal way a studio uses Open
edX's learning core is not `pip install` — it is lifting `openedx_tagging/` or
`openedx_content/` into a service. 🔴 **A subtree lifted out of that wheel carries no grant, no
holder and no notice, and the obligation it silently carries is the most reciprocal on this
page.** 🟢 **The fix is one file per package and it costs nothing**: `P17`'s notice-injection
step already exists for exactly this, and this is the clearest case on the shelf for running it.

🟢 **And `openedx_learning` is confirmed alive as a package name** even though the *distribution*
`openedx-learning` is a retired shim: 29 files of live code at 1.9.1. 🔵 **Demoted from
distribution to subpackage, not killed** — the distinction `T27` exists to catch.

### 🟡 No platform row was added or removed from the ERP/LMS tier this pass, and that is stated rather than padded

Moodle, Open edX, Canvas, Sakai, OpenOLAT, Kolibri, OpenEduCat, BigBlueButton, H5P, Tutor and
the national K-12 systems below are unchanged. 🔴 **Four global searches and four regional ones
returned no new platform**, and the single addition above arrived through the connector shelf
rather than the market channel — 🔵 **the third consecutive pass in which the artefact channel
produced what the demand channel did not.**


**Pass 140, 2026-10-12.** 🔴 **Two claims this page made about Sakai last pass are wrong, and the
correction is published here rather than quietly dropped.** 🆕 **A third platform row changes
identity entirely**: the package Open edX's learning core ships under has been renamed, and this
page has been pointing at the retired name.

### 🔴 CORRECTION — Sakai's two kernel artefacts have the SAME licence posture, not opposite ones

p139 wrote, on this page:

> *"Two artefacts of one kernel, same release line, **opposite licence posture**. The `api` jar
> declares **ECL-2.0** … and ships no text for it. The `impl` jar declares nothing at all."*

🔴 **`impl` does declare ECL-2.0** — inherited from `org.sakaiproject:oss-parent:1`, three levels
up its parent-POM chain, resolved by `ACTION CR`:

| coordinate | own POM | inherits | from | licence in jar |
|---|---|---|---|---|
| `org.sakaiproject.kernel:sakai-kernel-api` 25.2 | ECL-2.0 | — | — | 🔴 **NONE** |
| `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | 🔴 nothing | 🆕 **ECL-2.0** | 🆕 `org.sakaiproject:oss-parent:1` | 🔴 **NONE** |

🔵 **Both are ECL-2.0. Only the declaration DEPTH differs** — and depth is exactly what an
off-the-shelf scanner reading one POM does not traverse. 🟢 **The sentence to put in front of
Sakai's maintainers is unchanged and now better supported**: `org.imsglobal:basiclti-util` 1.2.0
ships `META-INF/LICENSE` *and* `META-INF/NOTICE` for its Apache-2.0 grant, so 🔵 **this is
fixable build configuration, not a Maven law.**

🔴 **And the review burden on a Sakai integration is HIGHER than p139 said, not lower.** With
inheritance resolved, **5 of 5** Java artefacts on this shelf declare a licence and **4 of 5
(80%)** ship no text for it. A client doing classpath licence review gets `ECL-2.0` — *education's
own licence*, an Apache-2.0 derivative with a university patent clause that off-the-shelf scanners
do not recognise — from a **sibling POM three levels up**, and nothing whatsoever from the jar.
[`p140-pom-parent-chain`](../compose/code/p140-pom-parent-chain/README.md).

### 🆕 🔴 Open edX: the learning-core package has been RENAMED, and this page tracked the retired name

`openedx-learning` **0.33.1** is not a broken release — it is a deliberate rename shim.
Its `setup.py`: *"Builds a final shell release of openedx-learning which simply 'redirects' to
openedx-core"*, with `packages=[]`, `install_requires=["openedx-core==0.34.1"]` and
`Development Status :: 7 - Inactive`.

| | retired | 🆕 current |
|---|---|---|
| package | `openedx-learning` 0.33.1 | 🆕 [`openedx-core`](https://pypi.org/project/openedx-core/) **1.9.1** |
| uploaded | 2026-02-18 | 🟢 **2026-10-09** |
| wheel | 🔴 1 479 B, 4 metadata paths | 358 188 B, **261 paths** |
| licence | AGPL 3.0 (legacy field) | 🔴 **AGPL-3.0-only** as a PEP 639 `License-Expression` |
| 🟢 licence payload | 🔴 none — it ships nothing | 🟢 `dist-info/licenses/LICENSE.txt`, **35 139 B** |

🔵 **For an institution customising Open edX, the practical consequence is a dependency rename,
not a licence change** — AGPL-3.0 either way, and the platform's copyleft posture on this page is
unaffected. 🟢 **What improves is auditability**: `openedx-core` ships its grant in the artefact
automatically under PEP 639, which is the cleanest licence payload this KB has measured, and
consolidates six top-level packages into one distribution.

🔴 **What a procurement conversation needs to know is the contact, and there are three of them.**
`openedx/XBlock` routes notices to `oscm@edx.org`; its sibling `openedx/codejail` routes to
`oscm@openedx.org`; the live PyPI artefact names `dave@axim.org`. 🟢 **The holder itself is
continuous** — edX Inc. was *renamed* Axim Collaborative, same trustees and tax ID, after Harvard
and MIT sold the edX brand to 2U. 🔴 **But `edx.org` is now operated by 2U**, a different company
from the steward, so one of those two repositories is routing its notice obligation to the wrong
organisation.

### 🔴 The attachment layer: a connector's tool surface moves with the DEPLOYMENT, not the version

p139 told this page that attachment review must *"enumerate `tools/list` against the live server,
not read the README"*. 🟢 **That instruction survives `ACTION CP` and the reason has changed.**

🟢 **On the npm connector shelf the README is not the problem the enumeration solves** — all eight
downloadable rows register literal tool names on a single server instance with no gate, so the
static count provably equals the live list. 🔴 **The enumeration is needed because of two shapes
that defeat any payload read:**

- 🔴 **Deployment-flag gating.** `ArnaudGuiovanna/tutor-mcp` registers **55** tool names and its
  own CI test asserts a live `tools/list` of **46**, gated on `deps.Institution`,
  `REGULATION_GOAL` and `deps.OAuthGranularScopes`. 🔵 **An institution that buys the
  institutional tier enables precisely the nine tools the vendor's documentation does not
  cover — three of them writes that author the curriculum a cohort is assessed against.**
- 🔴 **Two server instances in one package.** `@owen-x-tech/canvas-mcp` 1.1.0 exposes a different
  code path under `--http` than on stdio. Both happen to serve 62 tools, but the HTTP path names
  only **1** of them as a literal and registers 61 through a loop.

🔵 **So the line for an attachment review is: enumerate every transport the institution will
connect on AND every flag its contract enables, and record the flag set beside the count.** A
tool count with no configuration attached is not a measurement. `P18` step 5 is amended
accordingly.

### 🆕 🟢 Two connector rows place themselves on a hostname — and one of them is a misconfiguration

| row | evidence | region |
|---|---|---|
| 🟢 `eth-moodle-mcp` 1.3.3 | `moodle-app2.let.ethz.ch` (4×), `safari.ethz.ch` | 🟢 **EMEA** — ETH Zürich |
| 🟢 `mcp-canvas-lms` 1.0.5 | `canvas.ust.hk` (2×) | 🟢 **APAC** — HKUST, Hong Kong |

🔴 **For a platform owner, `mcp-canvas-lms` is the row with an operational defect, not just an
origin.** It reads `CANVAS_BASE_URL` in `dist/common/utils.js:4` and then hardcodes
`https://canvas.ust.hk/api/v1/courses` in `dist/operations/canvas.js:58`. 🔵 **One of its three
tools queries a different university's Canvas tenant regardless of configuration** — which is a
data-egress question for any institution that installs it, and it is invisible from the README.

🔴 **Host reachability could not be confirmed**: all three institutional hosts answer `403` at
`CONNECT` through this environment's proxy, which this pass established refuses **university**
hosts as well as the government hosts p139 diagnosed. The evidence is the compiled-in hostname,
not the host's liveness.

### 🟡 No platform row was added or removed this pass, and that is stated rather than padded

🔵 **The platform shelf below is unchanged.** Moodle, Open edX, Canvas, Sakai, BigBlueButton,
H5P, Kolibri and OpenEduCat are where p139 left them; the mandated vertical-platform search
returned only rows this page already carries (OpenEduCat LGPL-3, `frappe/education`, ERPNext,
RosarioSIS). 🔴 **Everything above is a correction to how an existing row should be READ**, which
is the kind of movement this page should expect once its shelf is saturated.

**Pass 139, 2026-10-12.** 🟡 **No platform row changed this pass either, and it is again stated
rather than padded.** But two measurements this pass land *on* the platform layer rather than beside
it, and one of them is about Sakai itself.

### 🔴 Sakai's own published artefacts do not carry the licence Sakai declares

`ACTION CM` probed Maven Central, where the Java platforms on this page actually ship. Two Sakai
kernel artefacts, **sha1-verified against the repository's own `.sha1`**:

| coordinate | version | POM declares | jar paths | licence file in jar |
|---|---|---|---|---|
| 🔴 `org.sakaiproject.kernel:sakai-kernel-api` | **25.2** | 🔴 **Educational Community License 2.0** | **578** | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` | 23.3 | 🔴 **nothing declared** | **524** | 🔴 **NONE** |

🔵 **Two artefacts of one kernel, same release line, opposite licence posture.** The `api` jar
declares **ECL-2.0** — *education's own licence*, an Apache-2.0 derivative with a patent clause
written for universities — and ships no text for it. The `impl` jar declares nothing at all.
🔴 **A client doing classpath licence review on a Sakai integration gets `ECL-2.0` from a sibling
POM file and nothing from the jar**, and ECL-2.0 is exactly the identifier an off-the-shelf scanner
does not recognise. Detail and method:
[`p139-pypi-maven-payload`](../compose/code/p139-pypi-maven-payload/README.md).

🟢 **The contrast row matters as much**: `org.imsglobal:basiclti-util` 1.2.0 ships
`META-INF/LICENSE` **and** `META-INF/NOTICE` for its Apache-2.0 grant. 🔵 **So this is fixable
configuration, not a Maven law** — which is the sentence to put in front of a platform's maintainers.

### 🔴 The attachment layer: what `install` actually gives an institution

This page's standing claim is that AI attaches to these platforms through connectors rather than by
forking platform source. Pass 139 measured what those connectors contain, and two results change how
an attachment should be reviewed:

- 🔴 **A connector's tool list is not its documentation.** Across the nine npm connector rows,
  **411** tools are registered and **249** documented; **62** of the 162 undocumented ones **write**
  to the LMS. For Canvas specifically, `@imazhar101/mcp-canvas-server` registers **227** tools with
  **61 undocumented writes**, including `bulk_update_grades`, `grade_submission`, `create_user`,
  `update_user_login` and 🔴 **`update_sso_settings`** — a tool that changes how the tenant
  authenticates. 🔵 **Attachment review must enumerate `tools/list` against the live server, not
  read the README.**
- 🔴 **An npm connector may not contain the connector.** `@exhabition/brightspace-mcp` is an
  **82-line loader** that downloads a Rust binary from GitHub Releases on first run, `chmod 0o700`s
  it and executes it, with **no checksum or signature verification**. 🔵 **For a Brightspace
  institution that is a procurement question, not a packaging detail.**

Both measured in [`p139-tool-count-drift`](../compose/code/p139-tool-count-drift/README.md).

### 🟢 The brokered-identity seam was executed against a live server, and it works

p138 read `canvas-lms-mcp`'s `OAuthStore` interface and called it sufficient for pattern `P13`.
`ACTION CL` ran it. 🟢 **With a grant pre-seeded into the store, `POST /oauth/token` returned
HTTP 200 with a Bearer access token, the seeded scopes (`canvas:read canvas:write`), a rotated
single-use refresh token — and ZERO contacts with Canvas**, measured by a sentinel listener rather
than inferred.

🔴 **But the documented embedder entry point cannot be imported.** `dist/http.js` calls `main()` at
module top level with no `import.meta.main` guard, so importing `canvas-lms-mcp/http` parses the
*importer's* `process.argv` and calls `process.exit(1)`. 🔵 **So the attachment shape for an
institution that already holds Canvas tokens is: seed the encrypted grant store, run `serve` as a
managed process.** Not an in-process embed — which is cheaper on protocol work and dearer on
plumbing. Full transcript:
[`p139-oauthstore-adapter`](../compose/code/p139-oauthstore-adapter/README.md).

### 🔴 One platform-adjacent library of this page is currently an empty package

🔴 **`openedx-learning` ("Open edX Learning Core (and Tagging)") ships no code in its two most
recent releases** — 0.33.0 and 0.33.1 are **1 479-byte** wheels containing only `dist-info`
metadata, down from **257 553 B** at 0.32.0, across 79 releases. `pip install openedx-learning`
resolves to the empty one. 🔵 **Anyone pinning Open edX's learning core from PyPI right now should
pin `0.32.0`**, and this is the kind of state a studio should verify at the payload layer before an
engagement rather than after.


**Pass 139 — second probe lane (`ACTION CH`), 2026-10-12.** 🟡 **No platform row changed this pass either, and it is stated rather
than padded for the second consecutive time.** `ACTION CH` was spent on the **attachment** layer —
the connector packages that bolt onto the platforms below — and it produced a finding that changes
how the platforms are *integrated* rather than which ones are listed: 🔴 **per-file licence notice
is practised by 1 of the 21 published connectors, so a developer who lifts one file out of an
attachment into a client codebase carries no holder and no grant with it.** 🟢 **The platform table
below is p137's, unchanged.** 🔵 **The four regional searches returned no new platform**, and the
one new regulatory item they surfaced (Texas HB 149, in force 2026-01-01) could not be read in this
channel and is registered rather than published.

**Pass 138, 2026-10-12.** 🟡 **No platform row changed this pass, and that is stated rather than
padded.** `ACTION CD`, `CE`, `CF`, `CG` and part of `CI` were spent on the **connector** layer that
attaches to these platforms, not on the platforms themselves — so the platform table below is
p137's, unchanged, and this page's own measurement this pass is about what happens when a client
*installs* one of the attachments.

🔴 **The attachment layer has a distribution defect this page must flag, because it lands on the
copyleft platform.** Of **21** education-LMS connector packages probed at the payload layer,
**9 ship no licence file**, and the worst is the one attached to Moodle:
`moodle-mcp-server-aql` **0.1.7** declares **AGPL-3.0** across **141 shipped paths** with no licence
text, while its repository
([`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server)) carries the
canonical **34 523-byte** grant. 🔵 **For this page the consequence is specific**: a studio that
attaches an AGPL-3.0 connector to a GPL-3.0 platform inherits the strongest obligation on the shelf
and is handed none of the text that states it.
[`p138-npm-payload-licence`](../compose/code/p138-npm-payload-licence/README.md).

🟢 **One attachment-point fact worth adding to this page.** Moodle now has **three independent
connectors in three different languages**, sharing no implementation —
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) (**AGPL-3.0**,
Node workspace monorepo), [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server)
(**MIT**, **Go**, with a committed `go vet` / `staticcheck` / `-race` / coverage harness) and
`GhaithAlHallak8/moodler-mcp` (**MIT**, **Python**, `playwright`-driven session) — plus at least six
more Moodle packages on npm that this KB's slug-first method never surfaced. 🔵 **For the
permissive-side route this page recommends (`P7`), the Go row is the only one that ships its own
test-and-lint discipline, and the only permissive one whose canonical address is not in question.**

**Pass 137, 2026-10-11.** 🔴 **The licence column on this page is a ROOT licence column, and for the
platforms a client actually runs that is now a measured understatement.** `ACTION BY` enumerated the
trees of the twenty largest rows across this KB's platform and foundation layers: **10 of 20 carry a
licence file whose holder is not the project** (`compose/code/p137-foreign-holder-tree`). The
platforms on this page are the worst of it, because they are the biggest:

| platform | root licence | what the tree adds |
|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | 🔴 **96 non-root licence files, 87 real grants, 66 of them somebody else's** — Fonticons, CKSource, OTPHP (Florent Morselli) under `admin/tool/mfa/factor/totp/extlib`, the QUAIL accessibility library, and more |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | ECL-2.0 | 🔴 **76 / 58 / 13**, including **The Trustees of Columbia University** (`delegatedaccess/NOTICE`), the Apache Software Foundation and AOL LLC |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 🔴 **28 / 22 / 17** — d3, highlight.js, the Harmattan font, Symfony contributors |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 *(payload-read, p135)* | 🔴 **17 / 13 / 10** — Bootstrap, Font Awesome, Tiny Technologies' editor, Adobe cmaps, Dailymotion |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 🟢 **`gems/lti-advantage/LICENSE.txt` is MIT, held by a named individual.** The LTI Advantage implementation inside the dominant North-American LMS is the **permissive** part of it |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 🔴 **18 / 11 / 9** — pdf.js with Adobe's cmaps, the PDFium Authors, Google's Liberation data, Mozilla |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 LGPL-3.0 *(payload-read, p131)* | 🟡 **14 licence-shaped non-root paths and not one readable grant** — no family anchor, no dated notice. A measured *unreadable* class, not a measured absence |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | 🟡 one foreign holder, and it is a **Debian packaging** copyright under `platforms/debian-server/debian/copyright` |
| [`overhangio/tutor`](https://github.com/overhangio/tutor), [`frappe/lms`](https://github.com/frappe/lms), [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | AGPL-3.0 / AGPL-3.0 / GPL-3.0 | 🟢 **`ROOT_ONLY` — the root file is the whole story.** The cleanest licence position of any platform here |
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 🟢 Apache-2.0 | 🔴 **`ROOT_ONLY` and that is misleading**: it composes Kiwix, Kolibri and Ollama **as container images**, so its third-party obligations exist and are not in its tree at all |

🔵 **What to do with this on an engagement.** The licence cell still decides whether a *derivative*
can ship. 🟢 **The tree decides what goes in the NOTICE file**, and for a Moodle or Sakai derivative
that is now a countable task with a number next to it rather than a vague caution.

## 🆕 The procurement route into these platforms, EMEA — `ACTION CC`

🔴 **p136 recorded European procurement data as "does not exist on this KB's pages", measured as an
empty probe.** 🟢 **It was a vocabulary problem**: the words that work are *framework agreement*,
*tender* and *catalogue*, not *procurement*.

| route | what it is | the date that matters |
|---|---|---|
| **Jisc digital assessment tools framework** | market engagement for digital assessment solutions across UK further and higher education | 🟢 **Responses closed 2026-03-13; contract runs 2026-11-01 → 2029-10-31** — a four-week window at the time of this pass |
| **Jisc Google for Education reseller framework** | single-lot, multi-supplier framework; 🟢 **the published scope names Gemini for Education**, with Google pricing under a separate Jisc–Google agreement | published **April 2026** |
| **Jisc Chest** | catalogue/purchasing service: members buy **without running their own tender** (LearnWise AI is listed on it) | standing route |
| **Jisc VR/AR framework** | immersive-technology procurement vehicle | standing route |

🟢 **Why this belongs on a platforms page**: an AI layer sold into a UK institution does not need a
new tender if it arrives through a framework the institution already calls off. 🔴 **SURF — the Dutch
equivalent — returned nothing**, so the Netherlands remains a hole, and it is now a *measured* one.

---

**Pass 135, 2026-10-11.** 🟢 **This page's longest-standing unresolved licence cell is resolved by
payload read, and the answer promotes a platform the page had written off.** `OpenOLAT` has sat in
*Declared gaps* as *"survives as unresolved — its own documentation describes an Apache-2.0 basis
that GitHub's matcher does not recognise, and no payload read is on record here."* 🔴 **A payload
read is now on record, and the matcher was defeated by something neither side guessed.**

🟢 **Two platforms are added**, both permissive, both pushed the day before this pass:
**OpenOlat** (a full LMS with QTI and SCORM built in) and **Mentingo** (an AI-native LMS under MIT).
🟢 **One authoring platform is added** — **Adapt Framework**, the largest repository in the entire
standards stack at 630★.

🔵 **Licence cells added or corrected this pass were established by sha256 identity against
canonical SPDX texts**, not by GitHub's badge — `compose/code/p135-licence-sha-identity`, which
discharges `ACTION BP`.

**Pass 132, 2026-10-11.** p131's structure and rows retained; 🔴 **a whole category of platform is
ADDED below — the national K-12 school platforms, which carry more AI connectors than Moodle and
which no previous pass of this KB had listed at all** (see `README.md` → Pass 132, `P132-A`). The
Kolibri row is also corrected. This page answers one question: *the client runs X — where does AI
attach, and what does the licence let us ship?* Repo-level verification lives in
`repos/foundations.md`; this page is about the attachment, the integration standard and the
constraint.

## The attachment points, before the platforms

Four ways to put AI into an existing education platform, in increasing order of coupling:

1. **LTI 1.3 / LTI Advantage** — the external tool is launched from inside the LMS with signed
   identity and grade passback. Touches no platform source, so **no copyleft reciprocity at all**,
   and works across Moodle, Canvas, Open edX, Sakai, Blackboard, D2L and ILIAS. Library:
   [`instructure/ims-lti`](https://github.com/instructure/ims-lti) (MIT). **This is the default
   recommendation** and the one most engagements under-use.
   🟢 **Corrected by p134 — the library to reach for is not the one this page has been naming.**
   `ims-lti` (MIT, 203★) is Instructure's library. The platform-independent reference implementation
   is [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) — **Apache-2.0, 373★, pushed 2026-10-06**,
   with OIDC launch, Deep Linking, **AGS grade passback** and NRPS rosters, plus first-party database
   plugins. In Python, [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT,
   138★) — 🔴 **but dormant since 2024-08-18, which is the weak link for an agent build.** For a PoC,
   [`paurushrai/lti-1.3-node-nextjs-starter`](https://github.com/paurushrai/lti-1.3-node-nextjs-starter)
   (MIT) is a template over `ltijs`. 🟢 **And for the first time this page can name a conformance
   test:** [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests)
   (Apache-2.0) for the rostering side.
2. **MCP against the platform's REST API** — the agent gets tools, the platform stays untouched.
   Connectors on the shelf in `agents/top.md`.
3. **Plugin / XBlock inside the platform** — deepest UX integration, inherits the platform's
   licence obligations for the plugin.
4. **Fork the platform** — only defensible when the licence is permissive and the client wants to
   own the product.

## Platforms and where AI goes

| platform | licence | the attachment point | real AI-on-top that exists today |
|---|---|---|---|
| **Moodle** — [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | Moodle plugin types, or the AI subsystem introduced in the 4.5+ line; LTI for anything you want to keep out of GPL | [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) (GPL-3.0, 222★ — tutoring, quiz generation, RAG over course materials); [`saylordotorg/moodle-local_ai_course_assistant`](https://github.com/saylordotorg/moodle-local_ai_course_assistant) (GPL-3.0, 16★ — Saylor Academy's "SOLA" learning coach, a real institutional deployment); [`onbirdev/moodle-webservice_mcp`](https://github.com/onbirdev/moodle-webservice_mcp) (17★, **unlicensed** — MCP as a web-service plugin, listed on marketplace.moodle.com). 🟢 **CORRECTED BY p131 — the permissive route exists and p130 denied it:** a *standalone* MCP server against Moodle's web-service API needs **no in-tree plugin and inherits no GPL obligation**. [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) is **MIT** (43★, verified at pass 30 of this KB as the licence-boundary exemplar), with [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) (**MIT**, assessment + gradebooks, writes gated), [`1alexandrer/moodle-mcp`](https://github.com/1alexandrer/moodle-mcp) (**MIT**, template) and [`Deeptanshuu/mydy-lms-helper`](https://github.com/Deeptanshuu/mydy-lms-helper) (**MIT**, single-institution worked example). Avoid [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) (40★, **no licence**). Build help: [`SaadRahman01/claude-moodle-dev`](https://github.com/SaadRahman01/claude-moodle-dev) (MIT). **Delivery note:** GitHub is a mirror; contribution goes to git.moodle.org. |
| **Open edX** — [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | **XBlock** ([`openedx/XBlock`](https://github.com/openedx/XBlock), Apache-2.0) is the clean route — the component framework is permissive even though the platform is not. Operations go through **Tutor** | [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) (AGPL-3.0, 2★, experimental) is the only MCP path. Sandboxing for generated/learner code: [`openedx/codejail`](https://github.com/openedx/codejail) (Apache-2.0). Analytics: `tutor-cairn`. |
| **Tutor** (Open edX distribution) — [`overhangio/tutor`](https://github.com/overhangio/tutor) | AGPL-3.0 | Write a Tutor plugin (cookiecutter provided) to ship AI services as containers alongside the platform | Plugin family is first-party and broad: `tutor-mfe`, `tutor-cairn`, `tutor-discovery`, `tutor-credentials`, `tutor-jupyter`, `openedx-scorm-xblock`. A Tutor plugin is how an AI service gets deployed and upgraded with the platform rather than beside it. |
| **Canvas** — [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | Canvas's REST API is the richest of any LMS — hence MCP first, LTI second. Avoid forking | The deepest connector ecosystem in education AI: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, 288★, canonical) and [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (MIT, 9★). Avoid [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) (103★ but **no licence**). |
| **Kolibri** — [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | Fork freely, or extend the Python app directly; content pipeline via [`learningequality/studio`](https://github.com/learningequality/studio) (MIT). 🟢 **Or do not integrate at all — orchestrate it** | 🔴 **CORRECTED BY p132. The claim that this was "the most valuable unfilled slot in the whole KB" is false.** [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) (**Apache-2.0, 39 444★**) already runs **Kolibri as its education container** beside **Kiwix** (library) and **Ollama** (AI assistant), as a Docker orchestration layer. It is the second-largest repo in this KB. Also [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) (20★, macOS port) and [`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI) (2★, Indian Class-10 curriculum, claims Kolibri integration). 🟢 **The surviving slots are narrower: nothing builds AI *inside* Kolibri** (NOMAD attaches from outside), **and nothing offline targets LATAM.** See pattern P2 in `compose/patterns.md`. |
| **Sakai** — [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** (permissive) | Java tool/provider model, or LTI | No notable AI-on-top found. Attractive because the licence is permissive and the installed base is institutional Java estate. |
| **Chamilo** — [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | Plugin API, or LTI | No notable AI-on-top found. Matters for engagement reach: real adoption in Francophone Europe and Spanish-speaking LATAM, where Moodle/Canvas assumptions do not hold. |
| **ILIAS** — [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | Plugin slots, or LTI | No notable AI-on-top found. Chosen in EMEA public-sector procurement for standards and accessibility compliance — the same reasons that make AI features there a documentation exercise as much as an engineering one. |
| **OpenOLAT** — [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **NOASSERTION** — verify | Java extension model, or LTI | No notable AI-on-top found. Swiss/German university base. |
| **OpenEduCat** — [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read; the API's `NOASSERTION` is a matcher artefact) | Odoo module (it is an Odoo app), so the whole Odoo module ecosystem applies. **LGPL permits linking without reciprocity** — so an AI service calling it from outside is clean | No notable AI-on-top found. **The ERP slot** — admissions, records, timetabling, fees. This is where "80% of routine administration automated" claims would have to land. 🟢 **And the tier is wider than p130 said:** `frappe/education` (662★), `academico` (MIT, 404★), RosarioSIS, Gibbon, openSIS, Fedena — see `repos/foundations.md`. |
| **BigBlueButton** — [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | Use the API/webhooks and the recording pipeline; LGPL permits linking without reciprocity | No notable AI-on-top found. The live-classroom surface: transcription, session summarisation, participation analytics, post-session question generation. Install and front-end: `bbb-install`, `greenlight`. |
| **Oppia** — [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** | Fork or extend directly — no reciprocity | No notable AI-on-top found. Its lesson model already encodes misconceptions explicitly, which is exactly the structure an LLM tutor needs and usually lacks. Permissive + pedagogically structured is a rare combination. |
| **Frappe LMS** — [`frappe/lms`](https://github.com/frappe/lms) | AGPL-3.0 | Frappe app; inherits the Frappe/ERPNext data model | No notable AI-on-top found. Pick when the client already runs ERPNext and wants learning next to HR and finance data. |
| **H5P** — [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | **MIT** | Content type authored once, embedded into any host LMS (`moodle-mod_hvp` for Moodle) | The standard delivery vehicle for generated interactive content: have an agent produce H5P content types and they render in every platform above. |
| **Richie** — [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | Django/React CMS in front of Open edX | The catalogue/portal layer. MIT, so the public-facing surface can be customised freely even when the LMS behind it is AGPL. |
| **SCORM/xAPI** — [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | Runtime shim | How legacy courseware a client already paid for keeps working, and how learner interaction data gets out of it for analytics. |
| **Blackboard** (proprietary) | n/a | API only | [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) (ISC, 11★, Peru) is the only open connector found. Blackboard retains significant higher-ed share, especially in LATAM, and is almost entirely unserved by open source. |

## The category this page was missing: national K-12 school platforms

🔴 **Every platform above is an LMS or an ERP, and in most of EMEA and APAC that is not what a
school actually runs.** A Polish school runs **Librus**. A Slovak or Czech school runs **EduPage**.
A French school runs **Pronote**. A German one runs **IServ**. These are the systems of record for
grades, attendance, homework and parent communication for millions of pupils — and this KB had
never listed one.

🟢 **Extended by p133 to LATAM and ANZ, and the same rule holds with different nouns.** A Brazilian
federal university runs **SIGAA**; a Brazilian federal institute runs **SUAP**; an Argentine
university runs **SIU-Guaraní**; an Australian school runs **SEQTA**; a New Zealand school runs
**KAMAR**. 🔴 **None of these five was on this page before p133, and together they carry 12 of the
category's connectors — including every teacher-facing one this KB has found.**

🟢 **They are also, by connector count, better served by open-source AI than Moodle is.** The
connectors are tiny and unofficial, but they exist and they map the API surface.

| platform | country | proprietary? | the attachment point | open connectors that exist |
|---|---|---|---|---|
| **Librus Synergia** | Poland | yes | portal login; no public partner API found | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) — 🟡 **MIT (2.x)**, `legacy_reference/` **GPL-3.0-only**, 10★. The largest connector of the tier. 🔴 Unofficial, *"not affiliated with Librus"*, and **no 2FA support** |
| **EduPage** | Slovakia / Czechia | yes | portal login | [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) (**MIT**, 3★ — timetables, grades, homework, **meal ordering**, multi-school discovery, 2FA) and an independent second implementation [`mhlavac/edupage-mcp`](https://github.com/mhlavac/edupage-mcp) (**MIT**, 1★). 🟢 **Two independent implementations is the strongest demand signal in the tier** |
| **Pronote** | France | yes | portal login | [`HAL-XP/mcp-pronotes`](https://github.com/HAL-XP/mcp-pronotes) (**MIT**, 1★) — grades, timetables, homework, absences |
| **IServ** | Germany | yes | portal login | [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) (**MIT**, 0★) — parent letters, timetables, **sick notes**. 🔵 The only connector in this KB whose user is a **parent** |
| **Sisu (Funidata)** | Finland (higher ed) | yes | institutional SIS API | [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) (🟢 **`MIT`** in `package.json`, `999` B, p215 <!--corrected-->, 1★) — written for **any** Sisu deployment, so the broadest reach of the tier, and **usable**: the only EMEA-bound SIS connector on these shelves with a permissive grant |
| **uSaint** | South Korea (higher ed) | yes | via `rusaint` | [`yourssu/soongpt-plugin`](https://github.com/yourssu/soongpt-plugin) (**MIT**, 3★) — course search, timetable planning, **graduation requirements**. Org-owned |
| **VTOP** | India (VIT) | yes | portal login | [`divyarthjain/vtop-bhopal-mcp`](https://github.com/divyarthjain/vtop-bhopal-mcp) (**Apache-2.0**, 4★) — attendance, marks, timetable, exams |
| **QLDT** | Vietnam (Hanoi Univ.) | yes | portal login | [`qxbao/qldt-hanu-mcp`](https://github.com/qxbao/qldt-hanu-mcp) (**GPL-2.0**, 1★). 🔴 **Jurisdiction warning:** Vietnam's Decision 33/2026/QD-TTg names education, including automated assessment and behavioural monitoring, as high-risk |
| **SIGAA** | Brazil (federal universities) | yes (SIG/UFRN-derived) | portal login | 🟢 **The deepest connector shelf of any platform on this page — 5 rows.** [`Agso-o/sigaa-calendar`](https://github.com/Agso-o/sigaa-calendar) (🟡 GPL-3.0, 20★ — deadlines → Google Tasks), [`trindadetiago/sigaa-caiu`](https://github.com/trindadetiago/sigaa-caiu) (**MIT**, 19★), [`RubsNeto/SigaaUI`](https://github.com/RubsNeto/SigaaUI) (**MIT**, 16★ — UI modernisation), [`MatheusMach/QuantoFalta`](https://github.com/MatheusMach/QuantoFalta) (🔴 no licence, 9★ — absence counter), and 🔴 **the teacher-facing one:** [`filipecalegario/auto-sigaa`](https://github.com/filipecalegario/auto-sigaa) (**MIT**, 9★ — grade entry from a spreadsheet) |
| **SUAP** | Brazil (federal institutes / IFs) | yes | portal login + institutional API | [`joojdev/academic-tracker-mcp`](https://github.com/joojdev/academic-tracker-mcp) (**MIT**, 0★) and [`frjunioalves/suap-mcp`](https://github.com/frjunioalves/suap-mcp) (🔴 no licence, 0★) — 🟢 two independent MCP implementations. Plus [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) (🟡 **AGPL-3.0**, 1★), **org-owned**, which drafts a lecturer's **RIT** workload report |
| **SIU-Guaraní** | Argentina (university consortium) | yes | portal login | [`juliancasaburi/siu-guarani-promedio-extension`](https://github.com/juliancasaburi/siu-guarani-promedio-extension) (**MIT**, 17★), [`despedite/siu-guarani`](https://github.com/despedite/siu-guarani) (🟡 GPL-3.0, 8★ — seat watcher), [`eugeborzone/Auto_Grade_Guarani`](https://github.com/eugeborzone/Auto_Grade_Guarani) (🔴 no licence — **teacher** grade upload). 🟢 **Uniquely, the vendor consortium is itself on GitHub:** [`SIU-Toba/docker-guarani`](https://github.com/SIU-Toba/docker-guarani) (🔴 no licence, 4★, dormant since 2017) |
| **SEQTA** | Australia | yes (TheSchoolBox) | portal login | 🟢 **The best-licensed and only product-shaped corner of this category.** [`BetterSEQTA/BetterSEQTA-Plus`](https://github.com/BetterSEQTA/BetterSEQTA-Plus) (**MIT**, **40★**, org-owned, 25 forks, Chrome Web Store, pushed 2026-10-06) and [`BetterSEQTA/DesQTA`](https://github.com/BetterSEQTA/DesQTA) (**MIT**, 16★ — native desktop port) |
| **KAMAR** | New Zealand | yes | portal login | 🔴 **One row, archived.** [`st22209/Parent-Portal`](https://github.com/st22209/Parent-Portal) (**MIT**, 2★) — README: *"[DEPRECATED AFTER KAMAR API CHANGE]"*. 🔵 **Keep this row on the page precisely because it is dead: it is this category's only measured example of what a vendor API change does to an unsanctioned connector.** |
| **Visual Schedule Builder (VSB)** | Canada | yes | institutional API | [`luca-dupont2/mcgill-vsb-mcp`](https://github.com/luca-dupont2/mcgill-vsb-mcp) (**MIT**, 2★ — conflict checks and schedule generation **without browser automation**) and [`SleepyPandas/UofT-MCP`](https://github.com/SleepyPandas/UofT-MCP) (**MIT**, 1★) |

🔴 **The attachment point for this whole category is the problem, not the opportunity.** There is no
LTI here, no MCP-friendly partner API, and no vendor programme — the connectors log in **as the
pupil or the parent, with their password**, against a platform that has not sanctioned it. For the
four K-12 platforms that is children's attendance and grade data under GDPR with no processing
agreement, and `librus-mcp` only works where **two-factor authentication is switched off**.

🟢 **How to use this category in an engagement anyway, which is the genuinely valuable part:**

1. **As integration intelligence.** The expensive, slow work — mapping each platform's undocumented
   API surface — is done and published under MIT. Read it, keep the surface map, rebuild the auth.
2. **As the opening for a sanctioned integration.** None of these vendors has an agent story. A
   studio that brings one a properly authenticated, logged, DPA-backed connector is not competing
   with open source; it is replacing a password-scraper the vendor would rather did not exist.
3. **Never deploy one as-is.** See the credential-model blocker in `agents/top.md`.

### 🆕 Four more national academic systems, and one national dataset *(p134)*

p133 added SIGAA, SUAP, SIU-Guaraní, SEQTA and KAMAR. 🟢 **p134's `ACTION BJ` sweep adds four more
and records two hard zeros with their probes named** — because an unprobed platform and an empty one
are different findings, and only one of them is information.

| platform | country | what it is | open-source AI/connector supply found | probe |
|---|---|---|---|---|
| **Q-Acadêmico** | 🟢 **Brazil** | The academic system of Brazil's **federal institutes** (IFs) — a fourth Brazilian national system alongside SIGAA, SUAP and the SAE family | 🟡 **~7 real rows out of 85 hits, topping out at 6★.** Best-licensed: [`adiel-calixto/IFAcademico`](https://github.com/adiel-calixto/IFAcademico) (**Apache-2.0**, 6★, 2026-04-26, Android). Also [`WKolodziejski/QMobile`](https://github.com/WKolodziejski/QMobile) (no licence, 6★, IFSul), [`MuriloCalegari/Ifes-Academico`](https://github.com/MuriloCalegari/Ifes-Academico) (GPL-3.0, 4★ — syncs grades, so **staff-adjacent**), [`kkauaon/qaluno`](https://github.com/kkauaon/qaluno) (no licence, 4★, IFCE), [`AlexandreL0pes/q-scraper`](https://github.com/AlexandreL0pes/q-scraper) (no licence — self-declared scraping) | `q-academico` |
| **SAES** (*Sistema de Administración Escolar*) | 🟢 **Mexico** | The academic portal of the **Instituto Politécnico Nacional** and other Mexican institutions | 🔴 **19 hits and effectively nothing usable.** Only 3 carry a permissive licence; the rest are unlicensed student scrapers. 🟢 **Two are conversational agents** — [`DanieelRC/SAES-R`](https://github.com/DanieelRC/SAES-R) (*"incluye un agente conversacional"*) and [`DanieelRC/AgenteConversacional-SAES-R`](https://github.com/DanieelRC/AgenteConversacional-SAES-R) (answers questions on the IPN academic regulations, *"para profesores"*) — 🔴 **both unlicensed, both 0★.** The one MIT row is a utility library, [`roncuevas/ipn_saes_utils`](https://github.com/roncuevas/ipn_saes_utils). [`pekochu/SAES2GO`](https://github.com/pekochu/SAES2GO) (GPL-3.0, 4★) **declares itself obsolete** | `saes escolar` |
| **SIMAT** (*Sistema Integrado de Matrícula*) | 🟢 **Colombia** | The national school-enrolment system run by the Ministry of National Education | 🟢 **One row, and it is a different species from everything else on this page:** [`juanfelipemalaver00-arch/Predictive-model-for-primary-school-dropout-in-Colombia`](https://github.com/juanfelipemalaver00-arch/Predictive-model-for-primary-school-dropout-in-Colombia) (🔴 **no licence field**, 1★, pushed **2026-10-10**) — a CRISP-DM pipeline joining **C-600, SIMAT and IPM** with territorial variables to raise **explainable dropout-risk alerts for a Secretaría de Educación**. 🔵 **Not a portal connector and not a chatbot: a government-facing early-warning model.** The only row in this KB aimed at a ministry rather than a student | `simat colombia` |
| **SIAGIE** | **Peru** | The national school information system (MINEDU) | 🔴 **NO EVIDENCE FOUND FOR THIS PLATFORM.** `siagie peru in:name,description` → **`total_count: 0`**. Reported per `agents/top.md` clause 4 as a platform-level absence with its probe named — **not** as a Peruvian zero, since Peru's one row ([`campus-cli`](https://github.com/alejooroncoy/campus-cli), ISC, 11★) targets Blackboard | `siagie peru` |

🔵 **What the four of them together say, and it is the most useful sentence on this page for a LATAM
engagement:** **Brazil has four national academic systems and a real builder community around each;
Mexico has one with a scraper community and no licences; Colombia's activity is aimed at the
ministry rather than the portal; and Peru's national system has no open-source footprint at all.**
Four countries, four different market shapes — which is why "LATAM" is not a strategy.

## 🟢 The category this page has been missing in the other direction: vendors that publish their own integration *(new, p134)*

🔴 **Every platform section above this one describes something a client runs and we attach to from
outside, usually unsanctioned.** These are the opposite: **the vendor ships the integration path
itself, under a permissive licence.** That makes them the shortest route to a defensible engagement,
and this KB had never listed one.

| platform | vendor / region | what the vendor publishes | licence |
|---|---|---|---|
| **WISEflow** | 🟢 **UNIwise ApS — EMEA (Denmark)** | [`AlexMeiling/wiseflow-api-integration-packages`](https://github.com/AlexMeiling/wiseflow-api-integration-packages) — user creation, flow setup, **assessor allocation** and **grade passback** against the WISEflow API. 🟢 **Licence payload-read and the holder is the vendor company itself.** WISEflow is a digital-assessment platform used across Nordic and UK higher education — so this is an **assessment** counterparty, the segment `intel/trends.md` records as the fastest-growing | **MIT** |
| **Blackboard Learn** | **Anthology — North America** | Two LTI 1.3 Advantage reference tools in Blackboard's own org: [`BBDN-lti-1p3-tool-example`](https://github.com/blackboard/BBDN-lti-1p3-tool-example) (Python/Flask, **Apache-2.0**) and [`BBDN-LTI-Adv-Node`](https://github.com/blackboard/BBDN-LTI-Adv-Node) (Node/React, 🔴 **no licence field**). 🟢 **Plus a public REST API that four of the seven Blackboard connectors in `agents/top.md` actually use** | **Apache-2.0** (one of two) |
| **TAO** | **Open Assessment Technologies — EMEA (Luxembourg)** | [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import) — OneRoster import into the TAO assessment platform | 🟡 **GPL-2.0** |
| **Ed-Fi ODS** | 🟢 **Ed-Fi Alliance (standards body) — North America** | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) — serves a **OneRoster 1.2 API from an Ed-Fi ODS**, pushed 2026-10-09 | 🟢 **Apache-2.0** |
| **Google Classroom estate** | 🟢 **Google — North America** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) — conformance tests proving a OneRoster integration correct | 🟢 **Apache-2.0** |
| **Aeries SIS + Edgenuity** | **North America (Fresno, California)** | [`openfresno/edgenuity-aeries-grade-passback`](https://github.com/openfresno/edgenuity-aeries-grade-passback) — keeps an **Aeries** gradebook current from **Edgenuity**. 🔴 **No licence field**, 0★. 🔴 **And its content could not be reached:** repo search returns it with metadata, but the raw lane returned 404 for 15 candidate paths across `HEAD`/`main`/`master`, so **this pass verified that the repository exists and did not verify that it contains anything.** 🟢 **Listed because of who owns it: a US school-district-adjacent org publishing its own passback job** — the K-12 integration need, in public, from the buyer's side | 🔴 **none** |
| 🆕 **TKAWEN OS** *(p136)* | 🟢 **TKAWEN — EMEA (Algeria)** | [`tkawen/developer-platform`](https://github.com/tkawen/developer-platform) — an **OpenAPI v1 spec, a TypeScript SDK and an MCP server** for an academy's live catalogue, instructors, certificate verification and, with a learner token, that learner's own dashboard, courses and transcript. 🟢 **Read-only by construction: the repo states it ships no write tool of any kind** — no cart, checkout, review, discussion or progress write. 🟢 **Auth is a learner bearer token, never a password**, and its `whoami` returns the token's abilities and expiry *"never the token itself"*. 🔴 Carries topics `lti`, `scorm`, `xapi` and implements none of them — in the SDK those are **lesson-type enum values**. 🔵 **The first North-African supply row on this page**, and 0★ | 🟢 **MIT** *(payload-read, 1 063 B)* |
| **Agilix Buzz** | **North America (Idaho Digital Learning Alliance)** | [`RyanGravetteIDLA/qualtrics-lti-connector`](https://github.com/RyanGravetteIDLA/qualtrics-lti-connector) — LTI 1.3 bridge from Buzz LMS to Qualtrics with automated grade passback. 🔴 **ARCHIVED** | **MIT** |
| **Virtual Arkansas** | **North America (state virtual school)** | [`virtualarkansas/jupyterlite-zestables`](https://github.com/virtualarkansas/jupyterlite-zestables) — JupyterLite notebooks packaged as Canvas content with assessment and state persistence. 🟢 **`MIT`** — declared in BOTH `package.json` *(`567` B)* and `extension/pyproject.toml` *(`license = {text = "MIT"}`)*, p215 <!--corrected--> | 🟢 **`MIT`** |

🔵 **The pattern across this table is the sales argument.** 🟢 **Where a vendor or a public body
publishes its own integration, the licence is usually permissive and the auth is sanctioned.**
🔴 **Where a school district or state agency publishes one, it is usually unlicensed** — not out of
hostility but because nobody asked them to add a `LICENSE` file. **That is a conversation, not a
blocker: an unlicensed repo from an institutional owner is the one case where asking for a grant is
likely to succeed**, unlike the 20-odd unlicensed student scrapers elsewhere in this KB.

### 🆕 The open-source education ERP field, named properly *(p134)*

`repos/foundations.md` carries `openeducat_erp` (LGPL-3.0, 886★) and `frappe/lms` (AGPL-3.0). The
surrounding product field, for when a client asks what else exists:

| product | licence | what it covers | note for an engagement |
|---|---|---|---|
| **OpenEduCat** | LGPL-3.0 (payload-read, per `repos/foundations.md`) | Admissions, attendance, exams, fees; **73+ modules**; built on **Odoo**/Flectra, so it sits beside Odoo finance and HR | 🟢 **The Odoo base is the point** — an AI module attaches as an Odoo addon, and the client's non-education ERP data is already in the same schema. 🟡 Vendor lists a paid tier from ~US$575/yr alongside the free community edition; treat vendor TCO claims as marketing |
| **Frappe Education** | AGPL-3.0 | Student enrolment, class assignments, assessments, fee collection, on the Frappe framework | Same reasoning as `frappe/lms` — adjacency to Frappe/ERPNext finance and HR. 🔴 AGPL: fine inside a client estate, a problem if offered as a hosted service |
| **RosarioSIS** | 🟡 **GPL-2.0** | K-12 student information system; PHP + PostgreSQL/MySQL | 🔴 **Still zero agent coverage** — one of the open-source systems of record this KB has flagged as unserved for several passes. `compose/patterns.md` → **P9** |
| **openSIS** | varies by edition — **verify** | K-12 and higher-ed school information system | 🔴 **Community/commercial split: do not assume the public edition's licence covers the feature a client saw in a demo.** Unverified by this pass |
| **Gibbon** | not verified this pass | School platform | 🔴 **Named in listicles with no detail.** This pass found no primary evidence; it remains an unexamined row, recorded so a later pass does not mistake absence of evidence for evidence of absence |

🔴 **Instrument note on this subsection, because it is weaker than the rest of the page.** These
five rows come from **vendor pages and listicles via web search**, not from repo search or a payload
read. One review source was ~656 days old. 🟢 **Everything else on this page is repo-verified;
this table is not, and a client-facing claim should be re-verified against each project's own
repository first.**

## 🟢 Platforms added by p135 — and one licence cell finally resolved

| platform | licence *(hash-verified this pass)* | the attachment point | real AI-on-top that exists today |
|---|---|---|---|
| **OpenOlat** — [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT), **447★**, pushed 2026-10-09 | 🟢 **Apache-2.0 + 2 attribution statements** (payload read, 10 982 B, Apache-2.0 core verbatim) | 🟢 **The richest attachment surface of any permissive LMS here**: QTI assessment, SCORM content, curriculum management, lecture management and course templates are all first-party, so AI attaches to a *standard* inside the platform rather than to a bespoke API. LTI for anything kept at arm's length | 🔴 **Nothing.** This KB has found no AI project targeting OpenOlat — and now that the licence is permissive and the surface is standards-native, 🟢 **this is the cleanest unclaimed platform slot on the page**, especially for a German-speaking-Europe engagement |
| **Mentingo** — [`Selleo/mentingo`](https://github.com/Selleo/mentingo), 92★, pushed **2026-10-10** | 🟢 **MIT** | Not an attachment at all — **the AI is the platform.** Fork it, white-label it, self-host it | 🟢 **It ships its own:** AI mentor, role-play scenarios, compliance/corporate training flows, SCORM and xAPI. Positioned explicitly as a self-hosted alternative to Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX. 🔵 Small and vendor-led (Selleo, Poland), so read it as a **reference architecture and a fork base**, not as a mature platform |
| **Adapt Framework** — [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework), **630★**, pushed **2026-10-10** | 🔴 **GPL-3.0** | A **content authoring** platform rather than an LMS: it produces responsive, accessible, multi-language course packages that emit **SCORM and xAPI**, which any LMS above can then consume | Generation of course structure and items into Adapt's JSON authoring format, then export as a tracked SCORM package. 🔴 **Copyleft matters here in a specific way:** the client *runs* Adapt as a tool and owns the course output, so GPL-3.0 constrains redistribution of Adapt itself and not the courses it authors |

### 🟢 The OpenOLAT `NOASSERTION`, explained — and it is a general lesson

p132 recorded that GitHub's matcher does not recognise OpenOlat's licence and that its own
documentation claims Apache-2.0. **Both were right, and the reason is now measured.** The file is
Apache-2.0 **to the character** through all nine sections of the terms — and then, where
`END OF TERMS AND CONDITIONS` and the boilerplate appendix belong, it carries instead:

> `* * *` *Additional license statement for the original olat.org code base:* … *originally created
> by the OLAT Zentrum at the University of Zurich* … `* * *` *Additional license statement for the
> openolat.org code base:* … *OpenOLAT is initiated by frentix GmbH and is initially based on the
> OLAT 7.1 release.*

🟢 **Consequence for a client engagement: this is a permissive licence.** The grant, the patent
clause and the disclaimer are unmodified Apache-2.0. 🔴 **The obligation is the attribution:** both
statements must be carried into any redistribution, which is an ordinary Apache-2.0 `NOTICE`-style
duty stated in an unusual place.

🔵 **The general lesson, and it applies to every `NOASSERTION` on this page.** A licence matcher
answers *"are these bytes a template I know?"* A client needs the answer to *"what may we ship?"*
Those differ whenever a project appends institutional attribution — which **well-governed,
institution-derived projects are the most likely to do.** 🔴 **So `NOASSERTION` is biased towards
exactly the platforms an education engagement most wants to use**, and that is the second time this
KB has recorded that bias (`P134-F`).

## 🆕 Platforms and platform-adjacent rows added by p136

| platform | licence *(payload-read)* | the attachment point | what exists today |
|---|---|---|---|
| **Brightspace / D2L** — proprietary, **not** open source | n/a (the platform) · 🟢 **MIT** (the connector) | 🟢 **A platform tier this page did not have.** [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) (**56★**, 27 forks, pushed **2026-10-11**, published to npm) reads grades, due dates, assignments, announcements, rosters, syllabus and course content over the **Brightspace API** and states it *"works with any school"* | 🟡 **A read connector, individually owned.** Brightspace is the third major commercial LMS after Canvas and Blackboard, and this is the first row this KB has for it. 🔴 **Not source-read this pass** — its write surface is unknown, and D2L publishes no vendor agent programme this pass could find |
| **Lextures** — [`StudyDrift/lextures`](https://github.com/StudyDrift/lextures), **62★**, pushed 2026-10-10 | 🔴 **AGPL-3.0** *(payload, 34 520 B)* | Not an attachment — another **AI-native** platform, self-described as *"the learning environment that adapts"* | 🔴 **The licence is the finding.** AGPL-3.0 means a **hosted** deliverable for a client's students triggers network-copyleft source provision. Compare `Selleo/mentingo` (MIT) for the same architectural slot: 🟢 **when two AI-native platforms sit side by side, the licence decides which one a studio can host** |

### 🔵 A vendor-page caution, measured rather than asserted

This pass re-ran the open-source-platform probe that produced the ERP table above, and **every one
of the ten results came from a single vendor's own domain** (`openeducat.org`, in nine languages).
🔴 **That vendor's pages contradict each other**: its Moodle comparison table marks Moodle as *not*
open source, while another of its own pages describes Moodle as *"GPL PHP"*. 🟢 **Useful facts do
come out of it**, and they are recorded as **vendor self-reported**: the Community Edition is
**LGPLv3**, needs **Python 3.10+** and **PostgreSQL 14+**, and the vendor claims **3M+ users across
90+ countries since 2014**. 🔵 **The lesson for this page is the channel, not the product:** a
query naming a product returns that product's marketing, so the ERP table's weakness is structural
and will not improve by re-running the same query.

## The licence decision, stated plainly

| client intent | platforms that permit it |
|---|---|
| Ship a **closed derivative** the client owns | Oppia (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT), Academico (MIT), Richie (MIT), H5P (MIT) |
| Run a **hosted service** for third parties | Anything, **via LTI or MCP only**. Forking an AGPL platform (Open edX, Canvas, Frappe LMS, Tutor, LearnHouse, ClassroomIO) triggers network-copyleft source release |
| Deepest **in-platform UX**, client keeps the estate | Moodle plugin (GPL-3.0) or Open edX XBlock (Apache-2.0 component in an AGPL host) |
| Touch **no platform source** | LTI 1.3 everywhere — the safe default |

## Declared gaps

- **Eight of the fifteen platforms above have no AI-on-top project at all.** 🟢 **SURVIVES.** The AI
  work has concentrated almost entirely on Canvas (five-plus MCP servers) and Moodle (three plugins
  **plus eight standalone MCP servers, five of them MIT** — p131). Sakai, Chamilo, ILIAS, OpenOLAT,
  Oppia, Kolibri, Frappe LMS and OpenEduCat are open ground. 🆕 **p136 adds a platform to the
  numerator and the denominator at once**: Brightspace/D2L now has a connector (MIT, 56★) and had
  none here before — and it is **proprietary**, so it joins Canvas and Blackboard in the column a
  studio cannot fork.
- ~~**Two platform licences (`openeducat_erp`, `OpenOLAT`) do not resolve to an OSI identifier.**~~
  🟢 **FULLY RESOLVED BY p135 — both halves.** `openeducat_erp` resolves to **LGPL-3.0**, read from
  an 8 241-byte `master/LICENSE` by an earlier pass. 🟢 **`OpenOLAT` resolves to Apache-2.0 with two
  attribution statements replacing the appendix** — payload read this pass, core terms verbatim,
  permissive in effect (see *The OpenOLAT `NOASSERTION`, explained* above). **Rule, now with two
  instances behind it:** `NOASSERTION` means "GitHub's matcher did not recognise the file", never
  "no grant" — and it is **biased towards institution-derived projects**, because they are the ones
  that append attribution.
- ~~**No open-source proctoring or academic-integrity system** was found.~~ 🔴 **REFUTED.** Four
  **MIT** proctoring projects are now on the shelf (`agents/top.md` → academic-integrity tier), one
  of which this KB already held. 🟢 **The surviving gap is grade, not existence:** the largest is
  18★, all four are individually owned, and three do affect-adjacent inference — which is
  **prohibited** in EU education settings under AI Act Art. 5, not merely high-risk. Assessment
  integrity remains the top institutional concern and the shelf still cannot answer it at
  production grade.
- **No AI-on-top for any *open-source* system of record.** 🟢 **NARROWED, and the distinction is
  now the whole point.** p132 found **21 SIS/student-portal agents** (`agents/top.md`), so the
  blanket claim *"no AI-on-top for any system of record"* is **refuted** — but every one of the 21
  connects to a **proprietary or institution-hosted** portal (Librus, EduPage, Pronote, IServ,
  Sisu, uSaint, VTOP, QLDT, VSB, Quercus). 🔴 **The open-source systems of record —
  `openeducat_erp`, `frappe/education`, `academico`, RosarioSIS, Gibbon, openSIS, Fedena — still
  have exactly zero agent coverage between them.** That is the sharper and more useful gap: the
  connector effort has gone to the platforms a studio *cannot* fork, and avoided the ones it can.
- 🆕 **The national K-12 platforms have no sanctioned integration path at all.** Nine proprietary
  platforms (above) with real open connectors and **no LTI, no partner API and no vendor agent
  programme** between them. Every existing connector is an unofficial password-scraper. This is
  simultaneously the clearest unmet need and the clearest compliance hazard on this page.
- 🆕 **p136: the national-platform gap now has a counter-example, and it is 8 000 km from Europe.**
  [`tkawen/developer-platform`](https://github.com/tkawen/developer-platform) is a vendor publishing
  a read-only MCP server with **token** auth for its own academy platform — exactly the shape the
  nine national K-12 platforms do not publish. 🔵 It is 0★ and serves one small vendor, so it is a
  **proof that the shape is cheap**, not evidence that the gap is closing.
- 🆕 **This page's licence cells are root-level, and p136 found a root licence hiding a vendored
  third-party grant** (`numbas/Numbas`, Apache-2.0 at the root, an MIT-style `pipwerks` header four
  levels down — `repos/foundations.md`). **None of the platforms on this page has had its vendored
  subtrees read.** For a platform of Moodle's or OpenOlat's size that is a material unknown, not a
  footnote.


