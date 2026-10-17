---
industry: education
region: Global
updated: 2026-10-17
---

# Vertical solutions — Education

> Real, running platforms a studio engagement can start from and put an agentic layer on
> top of — the Odoo-for-ERP pattern applied to education. Licences read first-hand from
> payload on 2026-10-17.
> Evidence: [`verified-repos.2026-10-17-p264.tsv`](../evidence/verified-repos.2026-10-17-p264.tsv)

## The platform shelf

| Platform | Repo | Licence | Stack | Where it fits |
|----------|------|---------|-------|---------------|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 *(`COPYING.txt`)* | PHP + MySQL/PostgreSQL | The default LMS of public education worldwide. Has a **first-party AI subsystem since 4.5** — provider-pluggable, so a client can point it at OpenAI, Azure, or a local Ollama/vLLM endpoint. Start here for K-12 and public universities. |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | Java | **The only Apache-2.0 full LMS found this pass.** Swiss-maintained, used across German-speaking higher education. If procurement rules out copyleft, this is the shelf — and it is the single most under-used finding in this file. |
| **Open edX** | [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | Python/Django + React | MOOC-scale, the platform behind edX. Extend through [XBlock](https://github.com/openedx/XBlock) (Apache-2.0), never by forking core. **The AGPL network clause applies to hosted deployments** — price it before the SOW, not after. |
| **Artemis** | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | Java/Spring + Angular | Interactive learning with **automated feedback** and an integrated exercise runner (TUM). The permissive choice when the deliverable is assessment rather than content delivery. |
| **Mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | MIT | TypeScript | **AI-native LMS**, self-hosted, positioned against Docebo/TalentLMS. Ships an AI mentor with voice role-play and auto-scoring, an AI course builder that converts policy documents into courses, open-ended answer grading, **Langfuse tracing of model calls**, an **MCP endpoint**, and bring-your-own-key. The closest thing to a 2026-native corporate L&D starting point under MIT. |
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | Odoo (Python) | Education **ERP**: admissions, SIS, gradebook, library, fees — the Odoo-for-education pattern. Active branches for Odoo 17.0 / 18.0 / 19.0. **The repo path this base previously published (`OpenEduCat-Inc/OpenEduCat`) is a 404; this is the canonical one.** |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | PHP | Lightweight LMS with the deepest LATAM public-sector footprint of any platform here. The pragmatic base for ministry-scale work in Spanish-speaking markets. |
| **ILIAS** | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | PHP | The institutional LMS of German-speaking EMEA (DE/CH/AT), with a strong assessment module and the compliance posture that market expects. |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | Java/Spring | North American higher-ed consortium LMS. **Prior cell said Apache-2.0; the payload is the Educational Community License 2.0** — Apache-derived and OSI-approved, but with patent-grant language scoped to educational use. A real distinction for a commercial deliverable. |
| **Gibbon** | [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | PHP | School management / SIS: timetabling, attendance, behaviour, pastoral records. Complements rather than replaces an LMS. |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | PHP | K-12 SIS, light enough for a single school to self-host. |
| **Richie + Marsha** | [openfun/richie](https://github.com/openfun/richie) · [openfun/marsha](https://github.com/openfun/marsha) | MIT · MIT | Django + React | Course catalogue portal and education video platform from France Université Numérique. MIT, EMEA-origin, nationally proven. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | BSD-3-Clause | Docker-first | Multimodal tutoring platform: voice, video, configurable 3D avatars, local LLMs via Ollama. **Licence re-confirmed this pass** — the payload is the verbatim BSD-3 form; its opening *"All rights reserved"* belongs to that form and is not a reservation. |

**13 platform rows, all licence-verified from payload.**

## Not on the shelf — and why

| Candidate | Verdict |
|-----------|---------|
| [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | **Excluded.** Ships a bespoke *PageLM Community License*: non-commercial only, and *"Redistribution of the Software, in whole or in part, in source or binary form, is strictly prohibited"* without written permission. **This base's own `evidence/verified-repos.2026-10-15-p213.tsv` grades it `MIT`.** That cell is wrong and a studio acting on it would have shipped unlicensed code to a client. |
| `OpenEduCat-Inc/OpenEduCat` | **Dead.** Repository page returns 404 and no raw path serves a payload. Replaced above by `openeducat/openeducat_erp`. |
| Canvas / Instructure, Blackboard/Anthology | Commercial SaaS, not a base to build on. Relevant as the incumbent to migrate *off* — see [`intel/market.md`](../intel/market.md). |

## How to add AI on top

### Pattern A — Moodle AI subsystem (public education, lowest friction)
Moodle has shipped a provider-pluggable AI subsystem since **4.5**; **5.0** added `Explain`
and AI Reports, and **5.1** added DeepSeek support plus **per-course and per-activity
enable/disable** — which is precisely the granularity an EU AI Act compliance story needs.
Point the subsystem at a local Ollama/vLLM endpoint and no student prompt leaves the
institution. Vendor sources describe a 5.2 standardized subsystem and a 5.3 LTS in
October 2026; treat those specific version claims as **vendor-sourced and unconfirmed**
against Moodle's own release notes.

> Core Moodle still has **no** AI question generation, **no** conversational practice and
> **no** AI over SCORM content. Those three absences are the studio's billable surface.

### Pattern B — LTI tool, not a fork (works against any compliant LMS)
Build the agent as an LTI 1.3 tool with [`tsugi`](https://github.com/tsugiproject/tsugi)
(Apache-2.0), [`pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT) or
[`lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) (Apache-2.0).
The tool stays permissively licensed and the client's GPL/AGPL LMS stays untouched — this is
how you keep a copyleft platform from colouring the deliverable.

### Pattern C — XBlock inside Open edX (MOOC and corporate)
`openedx/XBlock` is Apache-2.0 and is the sanctioned extension point. The AGPL obligation
attaches to `edx-platform` itself, so keeping the agent in an XBlock is both the cleanest
architecture and the cleanest licence boundary.

### Pattern D — start AI-native (corporate L&D)
`Selleo/mentingo` (MIT) already has the agent, the tracing and the MCP endpoint. When the
client has no LMS legacy to protect, starting here beats retrofitting Moodle.

## Declared gaps

- **Permissive LMS options are one deep.** OpenOLAT is the only Apache-2.0 complete LMS
  identified. Any "we need a permissive LMS core" requirement is a single-candidate
  conversation, and worth saying out loud in a pitch.
- **No APAC-origin platform on the shelf.** None surfaced this pass. The APAC engagements
  described in [`intel/market.md`](../intel/market.md) (India's Class-3 mandate, Singapore's
  SLS) run on either national systems or the platforms above — localisation, not a different
  base.
- **Star counts are deliberately absent from this file.** Platform choice here turns on
  licence, stack and deployment footprint; carrying unverified star numbers forward is how
  the errors corrected above were introduced.
