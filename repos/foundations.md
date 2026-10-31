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

## Adjacent systems of record (added second pass, 2026-10-31)

Not learning platforms, but systems a university or school district already
runs, and the systems an AI layer is repeatedly asked to search across. Verified
by reading the repository page *and* the licence file itself.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [DSpace/DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** | 1,100 | North America | ✅ permissive | "(Official) The DSpace digital asset management system that powers your Institutional Repository." Java. **The most permissively licensed platform of record found anywhere in this KB** — BSD-3-Clause, confirmed in the sidebar and in `LICENSE` on `main` ("BSD 3-Clause License, Copyright (c) 2002-2021, LYRASIS"). LYRASIS is a US non-profit. |
| [Koha-Community/Koha](https://github.com/Koha-Community/Koha) | GPL-3.0 | 597 | Global | ⛔ copyleft | "Koha is a free software integrated library system (ILS)." The repo page states GPL v3 *or later* and notes the project uses its own bug tracker rather than GitHub issues — relevant to any contribution plan. Origin country is not stated on the repository page. |

**Why DSpace matters more than its star count suggests.** Every other platform
of record in education is GPL or AGPL. DSpace is BSD-3-Clause, which means the
one category where a client *can* have a proprietary derivative is the
institutional repository — theses, datasets, faculty output, grey literature.
That is also the corpus a RAG-based research or discovery agent most wants. If
an engagement needs a licence-clean substrate rather than an attachment, this is
the only verified place in the education stack where that is available.

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
  one. **Qualified on the second pass of 2026-10-31:** this holds for the *LMS*
  category only. For the **institutional repository** category a permissive
  platform of record does exist and is the category leader —
  [`DSpace/DSpace`](https://github.com/DSpace/DSpace), **BSD-3-Clause**. The
  earlier blanket statement was too strong.
- **Licence hygiene is itself a finding.** Checking licence *files* rather than
  sidebars on the second pass turned up two defects elsewhere in this KB:
  `DMontgomery40/mcp-canvas-lms` claims MIT in its README and ships **no LICENSE
  file at all** (see [`../agents/top.md`](../agents/top.md)), and
  `frappe/education` — recorded here and in
  [`../verticals/solutions.md`](../verticals/solutions.md) as licence-unknown —
  is **GPL-3.0** per its own `license.txt`. Read the file, not the sidebar.
- **Still open: no African-origin repo appears anywhere on this page.** Regional
  demand evidence was found on the second pass (see
  [`../intel/market.md`](../intel/market.md)), but no African education platform
  or agent repository surfaced. The supply side of that region remains unmapped.
