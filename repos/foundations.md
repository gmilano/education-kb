---
industry: education
region: Global
updated: 2026-10-31
---

# Foundational open source repos for education

The substrate an education engagement builds on or integrates with. Every row
verified first-hand on the repository page, 2026-10-31.

**Read the licence column before the star column.** This is the defining
structural fact of open source education software and it is the opposite of the
AI/agent layer: the platforms of record are overwhelmingly **copyleft**. Only
four of the eleven rows below carry a licence Globant can build a proprietary
derivative on.

## Platforms of record

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 8,200 | North America | ⛔ copyleft | The Open edX LMS & Studio. Python + JavaScript. The reference MOOC-scale platform. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | APAC | ⛔ copyleft | The world's most-deployed LMS. Note the region: Moodle HQ is in Perth, **Australia** — commonly misfiled as EMEA because of its European install base. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 6,900 | North America | ⛔ copyleft | "The open LMS by Instructure, Inc." Dominant in North American higher ed, and the platform the strongest verified agent ecosystem attaches to (see [`../agents/top.md`](../agents/top.md)). |
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | 7,000 | Global | ✅ permissive | Free online learning platform built around structured, explorable lessons. Python, Angular, Google App Engine. The largest permissive learning platform found. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | ECL-2.0 | 1,200 | North America | ✅ permissive | Feature-rich platform for learning, teaching, research and collaboration. ECL-2.0 is an Apache-2.0 derivative written for academic consortia — permissive, with a patent clause tuned for universities. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 1,200 | Global | ✅ permissive | "The offline app for universal education." The reference choice for low- or no-connectivity deployments. Python + JavaScript. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 | 1,100 | EMEA | ⛔ copyleft | The Docker-based Open edX distribution. In practice this, not raw `openedx-platform`, is how Open edX actually gets deployed. France. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | EMEA | ⛔ copyleft | LMS focused on ease of use and accessibility. Strong francophone and LATAM install base. |

## Interoperability and analytics layer

This is where the permissive licences live, and it is the layer an AI
integration actually touches.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | 956 | North America | ✅ permissive | The xAPI specification: how systems communicate learner activity and experience. The vocabulary any learning-analytics or agent-telemetry design should speak. ADL Initiative (US). |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 | 373 | Global | ✅ permissive | Turns an application into a full **LTI 1.3** tool provider: launches, Deep Linking, Assignment & Grade Services, Names and Role Provisioning, Dynamic Registration. **This is the single most important repo on this page for a Globant engagement** — it is the sanctioned, licence-clean way to attach new software to a copyleft LMS without touching its code. Brazilian maintainer. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 153 | EMEA | ⛔ copyleft | The H5P interactive-content runtime. **Licence correction:** earlier passes of this KB recorded H5P as MIT. It is **GPL-3.0**. Norway. |
| [openfun/ralph](https://github.com/openfun/ralph) | MIT | 51 | EMEA | ✅ permissive | Learning Record Store for learning analytics; consumes xAPI statements. The permissive LRS option. France Université Numérique (France). |

## What this means in practice

A client on Moodle, Open edX, Canvas or Chamilo cannot have AI features
delivered as a proprietary fork of their platform — AGPL/GPL forbid it on any
hosted-service reading. The licence-clean route is to build **beside** the
platform and attach across a standard boundary:

- **LTI 1.3** (`ltijs`, Apache-2.0) to launch a tool inside the LMS and write
  grades back.
- **MCP** (the servers in [`../agents/top.md`](../agents/top.md), MIT) to give an
  agent read access to LMS data.
- **xAPI → LRS** (`xAPI-Spec` Apache-2.0, `ralph` MIT) to capture learner
  telemetry without instrumenting the platform's internals.

All three boundary technologies are permissively licensed. That is the whole
basis of the recipes in [`../compose/patterns.md`](../compose/patterns.md).

## Declared gaps

- **No permissive platform of record exists at Moodle/Open edX scale.** Oppia
  (Apache-2.0) and Kolibri (MIT) are the largest permissive options and both
  serve narrower jobs than a university LMS. If a client needs a permissive
  substrate, the honest answer is that they will be assembling one, not adopting
  one.
