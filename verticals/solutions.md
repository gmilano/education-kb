---
industry: education
region: Global
updated: 2026-10-25
---

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
| **H5P** | 🟢 **MIT** | Interactive content types; embeds in Moodle, Canvas and Open edX. |
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
| [**AlloFlow**](https://github.com/Apomera/AlloFlow) | 🔴 **AGPL-3.0-or-later** | `6194e51e8f1f` | `LICENSE` 35 441 B · `d8d2ea7ef0a1` | …**beside, over an interface.** The only maintained accessibility-first differentiation engine found: UDL levels/layers/outputs, WCAG, AAC, text-to-speech, offline-first, i18n, Electron + React. Network copyleft over a hosted engine — reach it over HTTP, never vendor it. |
| [**California IEP AI project kit**](https://github.com/robotros/California-IEP-AI-project-kit) | 🟢 **MIT** | `ff1ae0ce30e7` | `LICENSE` 1 064 B · `2524a8e74f10` | …**as the knowledge and boundary layer** on whatever drafting surface the district already has. Carries its own "not the system of record" discipline. |
| [**iep-builder**](https://github.com/67tallchris/iep-builder) | 🟢 **MIT** | `b39df0e9a4a1` | `LICENSE` 1 068 B · `523f156051cf` | …**as a standalone per-district app** (Cloudflare Pages + D1, bring-your-own-key). The deployment shape when a district will not accept a central student store. |
| [**access-to-education**](https://github.com/dougdevitre/access-to-education) | 🟢 **MIT** | `f8abd70707ba` | `LICENSE` 1 068 B · `68657618a157` | …**in the parent portal** (`p388`'s surface). ~120 k words of IEP navigation and advocacy content, MIT-granted. |
| [**rubric-desk**](https://github.com/rwrife/rubric-desk) | 🟢 **MIT** | `010a44006014` | `LICENSE` 1 062 B · `ec0b7dad19a4` | …**as the offline marking surface** (Flutter, no accounts). Pairs with Kolibri where connectivity cannot be assumed. 🟡 Created 2026-10-25. |

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
