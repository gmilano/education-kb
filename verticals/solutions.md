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
> and [`verified-repos.2026-10-17-p265.tsv`](../evidence/verified-repos.2026-10-17-p265.tsv) —
> the later pass adds three platforms, kills two that vendor comparisons recommend, and takes
> the permissive-LMS count from one to three.

## The platform shelf

| Platform | Repo | Licence | Stack | Where it fits |
|----------|------|---------|-------|---------------|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 *(`COPYING.txt`)* | PHP + MySQL/PostgreSQL | The default LMS of public education worldwide. Has a **first-party AI subsystem since 4.5** — provider-pluggable, so a client can point it at OpenAI, Azure, or a local Ollama/vLLM endpoint. Start here for K-12 and public universities. |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | Java | **The only Apache-2.0 full LMS found this pass.** Swiss-maintained, used across German-speaking higher education. If procurement rules out copyleft, this is the shelf — and it is the single most under-used finding in this file. |
| **Open edX** | [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | Python/Django + React | MOOC-scale, the platform behind edX. Extend through [XBlock](https://github.com/openedx/XBlock) (Apache-2.0), never by forking core. **The AGPL network clause applies to hosted deployments** — price it before the SOW, not after. |
| **Artemis** | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | Java/Spring + Angular | Interactive learning with **automated feedback** and an integrated exercise runner (TUM Applied Education Technologies; 819★, 12,437 commits, self-hosted by universities in several countries). The permissive choice when the deliverable is assessment rather than content delivery. **Pass 266 — the AI layer is already built and config-gated:** **Iris** (LLM tutor, MIT), **Pyris** (LLM microservice, MIT), **Athena** (feedback suggestion, **licence UNVERIFIED**), **Hyperion** (AI exercise authoring on Spring AI, no separate repo). "Config-gated" is the commercially important word — the same deployment runs with AI off, so a high-risk EU AI Act classification can be met by configuration rather than by re-architecture. |
| **Mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | MIT | TypeScript | **AI-native LMS**, self-hosted, positioned against Docebo/TalentLMS. Ships an AI mentor with voice role-play and auto-scoring, an AI course builder that converts policy documents into courses, open-ended answer grading, **Langfuse tracing of model calls**, an **MCP endpoint**, and bring-your-own-key. The closest thing to a 2026-native corporate L&D starting point under MIT. |
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | Odoo (Python) | Education **ERP**: admissions, SIS, gradebook, library, fees — the Odoo-for-education pattern. Active branches for Odoo 17.0 / 18.0 / 19.0. **The repo path this base previously published (`OpenEduCat-Inc/OpenEduCat`) is a 404; this is the canonical one.** |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | PHP | Lightweight LMS with the deepest LATAM public-sector footprint of any platform here. The pragmatic base for ministry-scale work in Spanish-speaking markets. |
| **ILIAS** | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | PHP | The institutional LMS of German-speaking EMEA (DE/CH/AT), with a strong assessment module and the compliance posture that market expects. |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | Java/Spring | North American higher-ed consortium LMS. **Prior cell said Apache-2.0; the payload is the Educational Community License 2.0** — Apache-derived and OSI-approved, but with patent-grant language scoped to educational use. A real distinction for a commercial deliverable. |
| **Gibbon** | [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | PHP | School management / SIS: timetabling, attendance, behaviour, pastoral records. Complements rather than replaces an LMS. |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | PHP | K-12 SIS, light enough for a single school to self-host. |
| **Richie + Marsha** | [openfun/richie](https://github.com/openfun/richie) · [openfun/marsha](https://github.com/openfun/marsha) | MIT · MIT | Django + React | Course catalogue portal and education video platform from France Université Numérique. MIT, EMEA-origin, nationally proven. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | BSD-3-Clause | Docker-first | Multimodal tutoring platform: voice, video, configurable 3D avatars, local LLMs via Ollama. **Licence re-confirmed this pass** — the payload is the verbatim BSD-3 form; its opening *"All rights reserved"* belongs to that form and is not a reservation. |
| **Oppia** | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** | Python/Angular | *"A free, online learning platform to make quality education accessible for all."* 6.9k stars, **17,004 commits**. Structured lessons with formative feedback built into the lesson model rather than bolted on. **The second Apache-2.0 complete platform in this KB** and the highest-adoption permissive one. Its lesson structure is the cleanest place to attach a tutoring agent without touching an LMS. |
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | Python/Django + Vue | *"the offline app for universal education."* 1.2k stars, **39,803 commits**. Runs fully **offline** and syncs opportunistically — built for schools with intermittent power and bandwidth. **MIT, which makes it the first permissive full platform in this KB that is not Apache-2.0.** The right base for rural LATAM, low-bandwidth APAC and anywhere a prompt cannot assume a network. |
| **Sunbird** | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) · [project-sunbird/knowledge-platform](https://github.com/project-sunbird/knowledge-platform) | **MIT** · **MIT** | Java/Angular + mobile | **India's national education stack, and the APAC-origin platform this KB spent 265 passes declaring absent.** The codebase beneath **DIKSHA** (NCERT / Ministry of Education); README mission: *"improve learning outcomes for **200 million children across India**"*. **38,046 commits, 317 forks — and 41 stars**, which is why star-sorted search never found it. Modular by design: portal, `knowledge-platform` backend, [mobile app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) (MIT). **MIT at national scale is the single most permissive large-platform option in this file** — for an APAC public-sector engagement it is the installed-base answer the way i-Educar is in Brazil. ⚠️ Slug trap: `Sunbird-Ed/sunbird-ed-portal` does not resolve; the live slugs are camel-case. |
| **Numbas** | [numbas/Numbas](https://github.com/numbas/Numbas) | **Apache-2.0** | Python 3 compiler → JS runtime | **E-assessment that executes entirely in the browser** (Newcastle University; 215★, 4,209 commits). Randomised questions, algebraic marking, SCORM-packaged output. Not a full LMS — it is the assessment engine you drop *into* one. Its architecture is the selling point under GDPR or a data-residency rule: **the submission never leaves the device**, so residency is satisfied structurally rather than by a processing agreement. |
| **i-Educar + i-Diário** | [portabilis/i-educar](https://github.com/portabilis/i-educar) · [portabilis/i-diario](https://github.com/portabilis/i-diario) | GPL-2.0 · **AGPL-3.0** | Laravel/PHP | **The Brazilian public-sector stack.** School management (SIS) plus a teacher portal, originally built by the *prefeitura de Itajaí (SC)* and published on the federal **Portal do Software Público in 2008**. 719 stars, 34,948 commits, last commits **2026-10-14** and **2026-10-09**. For a Brazilian municipal or state network this is the installed-base answer, and its provenance matches MEC's sovereignty framing exactly. **Legal note:** i-Diário's licence payload is a *Portuguese translation* of AGPL-3.0, not the FSF English text — cite the English original. |

**17 platform rows, all licence-verified from payload** (13 from pass 264, 4 added in pass 265).

## Not on the shelf — and why

| Candidate | Verdict |
|-----------|---------|
| [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | **Excluded.** Ships a bespoke *PageLM Community License*: non-commercial only, and *"Redistribution of the Software, in whole or in part, in source or binary form, is strictly prohibited"* without written permission. **This base's own `evidence/verified-repos.2026-10-15-p213.tsv` grades it `MIT`.** That cell is wrong and a studio acting on it would have shipped unlicensed code to a client. |
| `OpenEduCat-Inc/OpenEduCat` | **Dead.** Repository page returns 404 and no raw path serves a payload. Replaced above by `openeducat/openeducat_erp`. |
| Canvas / Instructure, Blackboard/Anthology | Commercial SaaS, not a base to build on. Relevant as the incumbent to migrate *off* — see [`intel/market.md`](../intel/market.md). |
| [formalms/formalms](https://github.com/formalms/formalms) (forma.lms) | **Excluded on licence, after being recommended to us.** A 2026 open-source-LMS review lists forma.lms as **Apache-2.0**. Its licence payload — `html/license.txt` — is the **GNU GPL, Version 2**. The project is alive (last commit 2026-07-17) and perfectly usable; it is simply *not* the permissive LMS that comparison implied, and it does not change the permissive count. |
| Fedena ([foradian/fedena](https://github.com/foradian/fedena), [projectfedena/fedena](https://github.com/projectfedena/fedena)) | **Excluded on abandonment.** Vendor comparisons still name Fedena as *the* Apache-2.0 education ERP/SIS. Both repositories are live pages over dead code: `foradian/fedena`'s last commit is **2012-10-12**, the community fork's is **2016-07-20** (message: *"emptying content"*). There is also no licence payload — Apache-2.0 is stated in `README.markdown` and `NOTICE` only. A Rails 2 application last touched in 2016 is not a starting point. |
| [os4ed/openSIS-Classic](https://github.com/os4ed/openSIS-Classic) | **Not shelved — licence unverified.** Repository resolves, but no licence payload was served on any path tried this pass. Commonly cited as GPL-2.0; this KB does not publish a licence it has not read. |

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

### Pattern E — offline-first, where the network is the constraint
`learningequality/kolibri` (MIT) is a complete platform that assumes no connectivity, so the
agent has to follow it: a quantised model served locally (Ollama) against Kolibri's own content
channels, with `fsrs4anki`-style scheduling for retention and sync-on-contact for telemetry.
Nothing in this stack is copylefted and nothing in it requires a data centre — which is the
only honest architecture for rural deployments in LATAM and low-bandwidth APAC.

### Pattern F — the Brazilian municipal network, sovereignty by construction
`i-educar` (GPL-2.0) holds enrolment, attendance and results; `i-diario` (AGPL-3.0) is where
teachers already work. Build the AI layer **outside both**, as a service the portals call over
HTTP/LTI, and the copyleft stays on the platform side of the boundary while the studio's model
code, prompts and evaluation harness stay permissive. The pitch writes itself: federal
software-public provenance, Brazilian maintainers, local inference, no student prompt leaving
the municipality.

### Pattern G — Sunbird for APAC public-sector scale (MIT, national precedent)

```
Sunbird-Ed/SunbirdEd-portal (MIT) + project-sunbird/knowledge-platform (MIT)
  └── already proven at DIKSHA scale under NCERT
  └── agent layer attaches at the knowledge-platform API, not in the portal
       ├── tutoring: ls1intum/Iris + Pyris (MIT) pointed at the course content store
       ├── assessment: numbas/Numbas (Apache-2.0) embedded, browser-side execution
       └── learner model: pykt-toolkit (MIT) over Sunbird telemetry
  └── MIT throughout — no copyleft obligation anywhere in this stack
```

Why this pattern and not "import a Western LMS": a ministry that already runs DIKSHA has the
platform, the content pipeline and the political precedent. The engagement is the **agent
layer over an existing national deployment**, which is a far shorter path than a migration —
and every component above is MIT or Apache-2.0, so nothing in it forces source disclosure.

**The licence point worth putting in a pitch:** Sunbird, Iris, Pyris, Numbas and pykt are all
permissive. This is the only full stack in this file with **no copyleft component at all**.

## Declared gaps

- **Retracted twice: "permissive LMS options are one deep" → three → now five.** With
  **Sunbird** (MIT, national scale) and **Artemis** (MIT, assessment-first) the permissive
  shelf is **five** deep. Each previous count was published as though settled; the pattern is
  the lesson. The original three: **OpenOLAT**
  (Apache-2.0, institutional/higher-ed, Java), **Oppia** (Apache-2.0, structured-lesson
  delivery, highest adoption at 6.9k) and **Kolibri** (MIT, offline-first). They are not
  interchangeable — OpenOLAT is the one that behaves like an institutional LMS, Oppia is
  lesson-delivery, Kolibri is offline-first distribution — so the honest pitch is *"three
  permissive candidates, each strong at a different job"*, not *"exactly one"*. Everything
  else at full-LMS scale remains GPL or AGPL.
- **Two platforms that comparison sites recommend do not survive verification.** forma.lms is
  GPL-2.0 (published as Apache-2.0) and Fedena has been abandoned for a decade. Both were
  recommended to this KB *this pass*, by 2026-dated sources. The shelf is only as good as the
  last payload read.
- **RETRACTED in pass 266: "no APAC-origin platform on the shelf."** **Sunbird is MIT, has
  38,046 commits, and is the stack under DIKSHA** — a national deployment serving Indian school
  education under NCERT. It is now on the shelf above. This was the last surviving piece of
  this base's "APAC is supply-poor" framing, and it is gone: APAC publishes at the agent layer
  (DeepTutor, 41.5k★, University of Hong Kong), the research layer (EduData, EduStudio) **and**
  the platform layer (Sunbird, MIT, national scale).
  **The failure was instrumental, not empirical.** Star-sorted GitHub topic search is
  structurally blind to ministry-funded code: Sunbird has **41 stars against 38,046 commits**,
  so no amount of re-running the same query could have surfaced it. Rank the platform layer by
  **commits and forks**; probe national programmes by name. The earlier note that APAC
  engagements imply "localisation, not a different base" now reads the other way round for
  India specifically — the base **is** national, and the work is the agent layer on top (see
  Pattern G).
- **Star counts are deliberately absent from this file.** Platform choice here turns on
  licence, stack and deployment footprint; carrying unverified star numbers forward is how
  the errors corrected above were introduced.
