---
industry: education
region: Global
updated: 2026-11-04
---

# 🏭 Vertical platforms — Education

> Real, running systems that a client may already have, or that can be stood up and then extended with an agentic layer.
> Model: start from something that already works, add agents on top. Verified 2026-11-04 via `git ls-remote --symref` + licence payload read.

## Platforms — 10 verified rows

| Platform | Repo | Licence | Branch | Stack | Use case |
|---|---|---|---|---|---|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | `main` | PHP + MySQL/PostgreSQL | The universal LMS: K-12, higher ed, corporate. Built-in AI subsystem since 4.5. Dominant in LATAM and much of EMEA. |
| **Open edX** | [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | `master` | Python/Django + React | MOOC scale, corporate academies, national platforms. Extend via XBlock. |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | `master` | PHP | Lightweight LMS, strong public-sector adoption in Spanish-speaking LATAM. |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | `master` | Java/Spring | Institutional HE LMS, mostly North American universities. |
| **ILIAS** | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | `release_11` | PHP | Robust LMS with deep adoption in German-speaking EMEA (DE/AT/CH), incl. public sector and military training. |
| **Gibbon** | [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | `v31.0.00` | PHP + MySQL | School management / SIS: enrolment, timetabling, academic records. Complements Moodle rather than competing. |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL (payload 15,214 B) | `mobile` | PHP + PostgreSQL | Student Information System: scheduling, grades, attendance, billing. Fills the SIS gap that LMSs leave open. |
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0** | `develop` | Python (Frappe) | Modern course platform on the Frappe/ERPNext stack — the realistic path when a client already runs ERPNext. |
| **Richie** | [openfun/richie](https://github.com/openfun/richie) | **MIT** | `master` | Django + React | Course-catalogue / MOOC portal CMS. The only permissive platform-level row here. |
| **Veo LMS** | [veolms/veolms](https://github.com/veolms/veolms) | **AGPL-3.0** | `main` | — | Newer actively-developed OSS LMS. Listed for awareness; AGPL-3.0 rules out a proprietary derivative. |

### Licence payloads read this pass

| Repo | Grant file | Bytes | Family |
|---|---|---|---|
| moodle/moodle | `COPYING.txt` | 35,147 | GNU GPL v3 |
| openedx/edx-platform | `LICENSE` | 35,136 | GNU Affero GPL v3 |
| chamilo/chamilo-lms | `LICENSE` | 35,147 | GNU GPL v3 |
| sakaiproject/sakai | `LICENSE` | 11,120 | Educational Community License v2.0 |
| ILIAS-eLearning/ILIAS | `LICENSE` | 35,147 | GNU GPL v3 |
| GibbonEdu/core | `LICENSE` | 35,121 | GNU GPL v3 |
| francoisjacquet/rosariosis | `LICENSE` | 15,214 | GNU GPL (v2 family by payload size) |
| frappe/lms | `license.txt` | 33,893 | GNU Affero GPL v3 |
| openfun/richie | `LICENSE` | 1,079 | MIT |
| veolms/veolms | `LICENSE` | 34,523 | GNU Affero GPL v3 |

## 🔴 Removed — HTTP 404

| Row | Previously published as | Status |
|---|---|---|
| `OpenEduCat-Inc/OpenEduCat` | "Education ERP, LGPL-3.0, 3M+ users / 100+ countries, Odoo-based" | **404.** Does not resolve on `ls-remote`; repository page returns 404; three candidate renames also fail. Removed. The commercial product may still exist — the published GitHub address does not. |

**Consequence:** this KB no longer holds a verified open source *education ERP*. `frappe/lms` on the Frappe/ERPNext stack is the nearest substitute, and it is AGPL-3.0. This is a genuine hole in the "Odoo-for-education" slot, recorded rather than papered over.

## 🔴 The licensing reality of this shelf — read before scoping

**Nine of ten platform rows are copyleft. One is permissive (Richie, MIT).** There is no permissively-licensed production LMS in open source. This changes how an engagement must be structured:

| Licence | What it permits | Engagement model it supports |
|---|---|---|
| **MIT / Apache-2.0 / BSD / ECL-2.0** | Proprietary derivative, closed distribution | Product, resale, closed IP |
| **GPL-3.0** (Moodle, Chamilo, ILIAS, Gibbon) | Derivatives must be GPL **when distributed** | Client-operated deployment and bespoke plugins are fine; a multi-client closed product is not |
| **AGPL-3.0** (Open edX, Frappe LMS, Veo) | Network use counts as distribution — modified source owed to **users** | Managed-service / SaaS delivery is directly affected. Keep modifications in permissively-licensed plug-in points (XBlock) or accept disclosure |

The practical rule: **put the IP in the agent layer, not in the platform fork.** Agents (MIT/Apache, see `agents/top.md`), XBlocks (Apache-2.0) and the portal (Richie, MIT) are where proprietary value can live. The LMS core stays stock.

## How to add AI on top

### Pattern A — Moodle + agent layer (best fit: LATAM public sector, EMEA K-12)
```
Moodle (GPL-3.0)
  └── AI subsystem (4.5+): pluggable provider — Ollama for data-residency, or a hosted model
  └── Moodle Web Services (REST)
       └── MCP server  ──►  tutor agent (DeepTutor / Bloom / OATutor)
```
Keep the agent out-of-tree and talk to Moodle over REST. Nothing you write becomes a GPL derivative, and the client keeps a stock, upgradable Moodle.

### Pattern B — Open edX + XBlock (best fit: corporate academies, national platforms)
```
Open edX (AGPL-3.0)  ← unmodified
  └── XBlock (Apache-2.0)  ← your code lives here
       └── agent backend (MIT/Apache) outside the platform
```
This is the licence-safe shape for Open edX. Modifying the platform itself pulls AGPL network-disclosure onto a managed service; an XBlock plus an external backend does not.

### Pattern C — Canvas (commercial LMS) + MCP
```
Canvas LMS (client's existing SaaS)
  └── canvas-mcp (MIT, 317★) — ~102–128 tools
       └── agent (Claude / Cursor / Codex clients)
```
No platform licence question at all, because the LMS is not ours to modify. The fastest route to a working pilot where the client already runs Canvas.

### Pattern D — SIS + LMS split
Moodle or Open edX handles learning; Gibbon or RosarioSIS handles enrolment, timetabling and records. Administrative agents (scheduling, at-risk alerting, enrolment triage) belong on the SIS side, where the data actually lives. Both SIS options are GPL, so the same out-of-tree rule applies.
