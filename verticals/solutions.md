---
industry: education
region: Global
updated: 2026-10-22
---

# Education vertical platforms — real systems to customise with AI on top

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/verticals-solutions.md`](../archive/2026-10-22-p383-pre-rewrite/verticals-solutions.md).
All addresses and licences verified first-hand on this date —
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).

This shelf answers one question: **what existing system does the client already run (or could run),
and what can be bolted onto it?** Same role Odoo plays for ERP or OpenMRS for healthcare.

## Choosing the base: the four-way decision

| if the client needs… | base | licence | the catch |
|---|---|---|---|
| **To own closed extensions to the platform itself** | [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | Smaller plugin ecosystem than Moodle; more build, less assemble. **The only permissive major LMS.** |
| **The widest plugin ecosystem and the largest talent pool** | [Moodle](https://github.com/moodle/moodle) | 🟡 GPL-3.0 (`COPYING.txt`) | Copyleft on anything linked. Extend through web services / the MCP plugin, not by patching core. |
| **MOOC scale, cohort analytics, deep data control** | [Open edX](https://github.com/openedx/edx-platform) + [tutor](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 | AGPL reaches **hosted** use. Build XBlocks and LTI tools; keep proprietary logic the other side of the boundary. |
| **North American higher-ed integration reality** | [Canvas LMS](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0, open-**core** | The published tree ≠ the commercial ecosystem. Scope integrations against the real tenant, not the repo. |

### Regional fit
- **LATAM / Iberia:** [Chamilo](https://github.com/chamilo/chamilo-lms) (GPL-3.0) — strongest
  Spanish/Portuguese public-sector base. [academico-sis/academico](https://github.com/academico-sis/academico)
  (MIT) for SME-scale administration with Spanish built in.
- **EMEA public sector:** [ILIAS](https://github.com/ILIAS-eLearning/ILIAS) (GPL-3.0, default ref
  `release_11`) and [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, Switzerland).
  [Serlo](https://github.com/serlo/serlo.org) (Apache-2.0, Germany) and
  [Richie](https://github.com/openfun/richie) (MIT, France) for content and catalogue.
- **APAC:** Moodle itself is Australian in origin; [netless-io/flat](https://github.com/netless-io/flat)
  (MIT) for live online classrooms.
- **Low-connectivity anywhere:** [Kolibri](https://github.com/learningequality/kolibri) (MIT,
  default ref `develop`) — offline-first by design, not as a degraded mode.

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
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | 🔴 `develop` | 🔴 AGPL-3.0 (`license.txt`) | Only where the client already runs ERPNext — then the student record and the finance record are one system. |

## Content, assessment and media layers

| layer | platform | licence | note |
|---|---|---|---|
| Interactive content | [H5P](https://github.com/h5p/h5p-php-library) | 🟡 **GPL-3.0** | Embeds in Moodle, Open edX, Canvas, Drupal, WordPress. 🔴 Widely mislabelled MIT. Treat as runtime content, not linked code. |
| Structured pedagogy | [Oppia](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | Misconception-aware lesson branching. Permissive and pedagogically serious — unusual combination. |
| Open-response assessment | [openedx/edx-ora2](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 | Peer + self + staff assessment rubrics. The place an LLM grader must plug in to stay auditable. |
| Lecture capture | [opencast/opencast](https://github.com/opencast/opencast) | 🟡 ECL-2.0 | Video pipeline → the transcript corpus every education RAG build needs. |
| Live classroom | [netless-io/flat](https://github.com/netless-io/flat) | 🟢 MIT | Whiteboard, recording, real-time session. |
| Interop boundary | [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | 🟢 Apache-2.0 | **The copyleft firewall.** Standards-body reference implementation. |
| Campus LLM gateway | [LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | Multi-provider, SSO, quota, audit log. The audit log is what gets a deployment past a university's data-protection officer. |

## 🟡 MCP has reached the LMS — and this is new as of 2026

This did not exist a year ago and it changes the integration story:

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
- **No official server** from Instructure or Moodle HQ beyond the community plugin. Verified gap.
- 🔴 [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) is **UNGRANTED** — no licence file
  *and* no `license` field in its `pyproject.toml`. Use the plugin-directory route for Moodle:
  [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) has no root
  licence file either, but its `version.php` carries the full **GPL-3.0-or-later** header that
  Moodle requires of every plugin, so it *is* granted.

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
- **Proctoring and AI-detection** have no credible permissive open-source option — and under the EU
  AI Act both are squarely high-risk, so this gap is also a liability boundary worth naming to a
  client rather than filling.
