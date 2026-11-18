---
industry: education
region: Global
updated: 2026-11-18
---

# Vertical solutions — education

Deployable systems, not libraries: things a client may already be running, or can stand up
in days, and that AI can be layered onto. All URLs and licences verified 2026-11-18 via
`raw.githubusercontent.com`.

Education's equivalent of "Odoo for ERP" is not one product but four categories: the LMS
(Moodle, Open edX, Canvas), the SIS (RosarioSIS, Gibbon, openSIS, i-educar), the repository
(DSpace, Koha, OJS) and the live-classroom stack (BigBlueButton, Opencast, OpenVidu). An
engagement usually touches at least two.

## Learning management systems

| Platform | Repo | Licence | Where it is strong | AI layering seam |
|---|---|---|---|---|
| **Moodle** | https://github.com/moodle/moodle | GPL-3.0 (`COPYING.txt`) | Everywhere; the default in EMEA and LATAM public education | Plugin API + LTI 1.3 tool. Moodle HQ's own https://github.com/moodlehq/wiki-rag (BSD-3-Clause) shows the first-party RAG pattern |
| **Open edX** | https://github.com/openedx/openedx-platform | AGPL-3.0 | Large-scale MOOCs, corporate academies | XBlocks (https://github.com/openedx/XBlock, **Apache-2.0**) and `edx-ora2` open-response grading. **Slug corrected p896** — `openedx/edx-platform` is a rename alias, not the canonical repo. |
| **Canvas LMS** | https://github.com/instructure/canvas-lms | AGPL-3.0 | North American higher ed | Rich REST API; https://github.com/vishalsachdev/canvas-mcp (MIT) exposes it to agents directly |
| **Artemis** | https://github.com/ls1intum/Artemis | MIT | CS/engineering programmes with automated code assessment | First-party AI tier already exists (`edutelligence`, `Pyris`) — **the lowest-friction permissive starting point** |
| **Kolibri** | https://github.com/learningequality/kolibri | MIT | Offline/low-bandwidth deployments | Offline-capable; pair with `ollama` for a fully disconnected tutor |
| **Chamilo** | https://github.com/chamilo/chamilo-lms | GPL-3.0 | LATAM, francophone Africa, Spain | LTI tool provider |
| **ILIAS** | https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | German-speaking EMEA, public sector, regulated training | Plugin slots, SCORM/LTI |
| **Sakai** | https://github.com/sakaiproject/sakai | ECL-2.0 | Research universities | LTI; ECL-2.0 is patent-clause Apache |
| **OpenOLAT** | https://github.com/OpenOLAT/OpenOLAT | Apache-2.0 | Switzerland, Germany, Austria | Permissive — under-used given its maturity |
| **Oppia** | https://github.com/oppia/oppia | Apache-2.0 | Foundational literacy/numeracy, emerging markets | Exploration framework with misconception modelling |
| **Frappe LMS** | https://github.com/frappe/lms | AGPL-3.0 | SMB/corporate training on the Frappe stack | Frappe app hooks; integrates with ERPNext |
| **Mentingo** | https://github.com/Selleo/mentingo | **MIT** (`LICENSE@main`, `Copyright (c) 2024 Selleo`) | Corporate L&D, onboarding and compliance training; white-label, multi-tenant | **No layering needed — the AI mentor is first-party.** Postgres + pgvector is already the retrieval substrate; one-click AWS Marketplace deploy |
| **Tutor** | https://github.com/overhangio/tutor | AGPL-3.0 | The de facto Open edX deployment/ops tool | Plugin system for injecting services into an Open edX cluster |

**Added p893 — the copyleft rule now has a real exception.** Every other LMS in the table above
is GPL, AGPL or ECL. **Mentingo (109 ★, pushed 2026-11-18) is MIT**, licence byte-read, and it
is *AI-native* rather than AI-retrofitted: the mentor and role-play tiers ship with the
platform. That matters for exactly one question, and it is the question clients ask most —
*"can we brand this and keep it closed?"* On Moodle, Open edX or Canvas the answer is no without
an LTI/MCP separation. On Mentingo it is yes.

Two cautions before it displaces Artemis as the default permissive pick. It is **corporate L&D,
not K-12 or higher ed** — there is no gradebook-of-record, no SIS integration and no
accreditation story. And at 109 ★ with a single vendor (Selleo) behind it, the governance risk
is the mirror image of Moodle's: permissive licence, thin community. **Use it where the client
wants a product; use Artemis or OpenOLAT where the client wants an institution.**

## Student information systems and school ERP

The weakest category for AI today and therefore the strongest opportunity.
`verticals` note: **GegoK12 is the only MIT-licensed SIS verified here** — relevant when a
client wants a closed derivative.

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **GegoK12** | https://github.com/Gego-K12/gegok12 | MIT | K-12 school ERP/SIS, PHP/Laravel. Permissive licence verified in repo, confirming the vendor's claim. |
| **RosarioSIS** | https://github.com/francoisjacquet/rosariosis | GPL-2.0 | Students, grades, scheduling, attendance, billing, discipline, food service. PHP + PostgreSQL/MySQL. Active. |
| **Gibbon** | https://github.com/GibbonEdu/core | GPL-3.0 | Full school platform, strong in international schools across APAC. |
| **openSIS Classic** | https://github.com/OS4ED/openSIS-Classic | 🔴 **GPL-2.0 — resolved p897.** Byte-read at **`master/docs/License.txt`** (17,286 B, `sha256₁₂ 224ac3d403e3`); the `README.md` links it. GitHub's SPDX still reports `NONE` because the file is not at the repository root, and this KB previously recorded it as *"none declared"* for the same reason. **The licence is known; it is strong copyleft.** Fine to deploy and host for a client; a proprietary derivative is not. | Long-standing web SIS from OS4Ed, 351 ★, pushed 2026-10-26. |
| **i-Educar** | https://github.com/portabilis/i-educar | GPL-2.0 | **Brazilian public-education SIS**, built around Brazilian regulatory requirements. The default SIS starting point for a LATAM public-sector engagement. |
| **OpenEduCat** | https://github.com/openeducat/openeducat_erp | LGPL-3.0 (byte-verified p891 from `LICENSE@master`; the GitHub API reports `NOASSERTION` because the file is a preamble plus the GPL text, not an SPDX-matchable template) | Education ERP built **on Odoo** — admissions, fees, LMS, library in one. |
| **Odoo** | https://github.com/odoo/odoo | LGPL-3.0 | The general ERP underneath OpenEduCat; the actual "Odoo for education" answer is Odoo plus OpenEduCat. |
| **Frappe Education** | https://github.com/frappe/education | GPL-3.0 (`license.txt`: "License: GNU GPL V3") | Education module on the ERPNext/Frappe stack. |
| **UniTime** | https://github.com/UniTime/unitime | **Apache-2.0** (`LICENSE@master`) | **Restored p894.** Apereo university **course and exam timetabling plus student scheduling**, 360 ★, **pushed 2026-11-17**. Runs standalone or interfaces with an existing SIS. **The one permissive, actively maintained system in this category** — and the answer to the registrarial gap at the platform layer. Its solver https://github.com/UniTime/cpsolver is **LGPL-3.0** (84 ★): keep it behind a service boundary in a closed derivative. |
| **Timetablely** | https://github.com/GEOSOFT-GLOBAL/timetablely | MIT | **Restored p894.** Automated timetable generator, 27 ★ — the small-scale permissive alternative to UniTime. **Pushed 2026-08-17, three months idle;** a starting point, not a dependency. |
| **i-Diário** | https://github.com/portabilis/i-diario | **AGPL-3.0** — 🔴 **byte-read correction, p896** | **Restored p896.** The teacher-facing *diário de classe* (class register: attendance, marks, lesson records) companion to **i-Educar** above, from the same Brazilian publisher — 117 ★, pushed 2026-10-14. 🔴 **GitHub reports `NOASSERTION` and the licence is AGPL-3.0**: the `LICENSE` file is the **Affero GPL in Portuguese translation** (*"LICENÇA PÚBLICA GERAL AFFERO GNU"*, 35,326 B), which GitHub's SPDX matcher cannot recognise. An engagement that read the API field alone would treat the strongest copyleft in this file as "licence unknown". **Together with i-Educar this is the most complete open Brazilian public-school stack.** |
| **Gestão Escolar** | https://github.com/Antonio-Neves/Gestao-Escolar | MIT | **Restored p896.** Python/Django school-management system, 50 ★, pushed 2026-10-12, Portuguese-language. Self-described as in development. **The only MIT-licensed LATAM-origin school system this KB has verified** — thin, but it is the permissive option in a category where the mature Brazilian systems are GPL and AGPL. |

**Rejected this pass, recorded so it is not re-proposed (p892).** A fresh search for
open-source school ERP returned **Fedena** in a licence comparison table under **Apache-2.0**,
alongside OpenEduCat and openSIS. It verifies as neither usable nor maintained:
https://github.com/projectfedena/fedena has **547 ★**, SPDX **`NONE`**, **no `LICENSE`,
`LICENSE.md`, `LICENSE.txt` or `COPYING` on `main` or `master` (404 on all eight)**, and a last
push of **2020-05-18** — roughly 2,375 days idle. No licence file means **all rights reserved**.
The comparison table's Apache-2.0 claim has no basis in the repository. See `repos/trending.md`
for the method note: this is the second aggregator-sourced licence error caught in two passes.

**That p892 negative result is retired (p894), and it was wrong in all three of its clauses.**
It read: *"The category is small, static, and copyleft or licence-unclear end to end... the
platform layer beneath the missing registrarial AI agent is not moving either."* **UniTime is
360 ★, Apache-2.0, and was pushed 2026-11-17.** The error was not a bad measurement — an
earlier pass had verified UniTime and hash-checked its Apache payload — it was that the finding
never reached this file, and the 2026-11-18 rewrite dropped it. The p892 leg then re-derived an
absence from a table that had already lost the counter-example. **Method consequence, recorded
in `repos/trending.md`: diff a canonical table against the append-only history before rewriting
it, and before concluding a category is empty.**

**What survives, better specified.** The opportunity note at the top of this section stands and
sharpens: **the registrarial gap is an agent tier, not a platform.** Timetabling, exam
scheduling and student scheduling have a permissive, maintained substrate; enrolment decisioning,
transcripts and financial aid still have nothing, and financial-aid decisioning is EU Annex III
high-risk. See `compose/patterns.md` **P12**.

## Repositories, libraries and scholarly publishing

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **DSpace** | https://github.com/DSpace/DSpace | BSD-3-Clause | Institutional repository standard, 1,115 ★. **The most permissive major system in this file.** |
| **Koha** | https://github.com/Koha-Community/Koha | GPL-3.0 | The incumbent open-source integrated library system. |
| **Open Journal Systems** | https://github.com/pkp/ojs | GPL-3.0 | Scholarly publishing; very heavily used in LATAM academia. |

## Live classroom, video and lecture capture

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **BigBlueButton** | https://github.com/bigbluebutton/bigbluebutton | LGPL | Purpose-built virtual classroom with Moodle/Canvas integrations. The incumbent. |
| **Opencast** | https://github.com/opencast/opencast | ECL-2.0 | Lecture capture and video management at university scale. Pipe output into `faster-whisper`. |
| **OpenVidu** | https://github.com/OpenVidu/openvidu | Apache-2.0 | WebRTC platform; permissive, build-your-own-classroom. |
| **Flat** | https://github.com/netless-io/flat | MIT | Interactive online classroom with whiteboard. **APAC-origin (China), MIT** — strongest permissive option in this category. |
| **Marsha** | https://github.com/openfun/marsha | MIT | LMS-embedded video management from France Université Numérique. |

## Study tools, practice and assessment delivery

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **Anki** | https://github.com/ankitects/anki | AGPL-3.0 | Spaced repetition at scale. Pair with https://github.com/open-spaced-repetition/fsrs4anki (MIT) for the FSRS scheduler and https://github.com/warleysr/ankipa (MIT) for pronunciation scoring. |
| **PrairieLearn** | https://github.com/PrairieLearn/PrairieLearn | MIT | Randomised auto-graded assessment delivery. Deployable product and library both. |
| **Autolab** | https://github.com/autolab/Autolab | Apache-2.0 | CMU autograding platform with secure execution. |
| **CTFd** | https://github.com/CTFd/CTFd | Apache-2.0 | Capture-the-flag platform — the practical delivery vehicle for cybersecurity curricula. |
| **OMRChecker** | https://github.com/Udayraj123/OMRChecker | MIT | Scans paper bubble sheets. High value anywhere exams are still on paper. |
| **Teaching-Open** | https://github.com/open-scratch/teaching-open | Apache-2.0 | Scratch-based programming teaching platform (APAC/China origin). |

## Low-connectivity and offline deployment

The category that decides whether a rural LATAM, African or South Asian engagement is
deliverable at all.

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **Internet-in-a-Box** | https://github.com/iiab/iiab | GPL-2.0 | Turnkey offline server bundling Kiwix, Kolibri and more onto low-cost hardware. |
| **Kiwix** | https://github.com/kiwix/kiwix-tools | GPL-3.0 | Offline Wikipedia and ZIM content serving. |
| **Project NOMAD** | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | Offline-first knowledge/education server. Permissive alternative to the above. |
| **Kolibri** | https://github.com/learningequality/kolibri | MIT | See LMS table — designed offline-first from the start. |
| **elimu.ai** | https://github.com/elimu-ai/webapp | MIT (byte-read `main/LICENSE`, 1,065 B) | **Restored p895; region EMEA.** Early-grade literacy for **out-of-school children**, Sub-Saharan (Tanzania/Kenya). 41 ★ / **67 forks**, pushed **2026-11-17**. **Africa-origin and permissive — the only such platform this KB has verified.** The component that matters here is https://github.com/elimu-ai/appstore (MIT, 29 ★): **installs and updates APKs with no app store and no network**, which is a harder problem than offline content and is already solved. `launcher` (MIT, 9 ★) enforces an EGRA/EGMA path. 🔴 **Exclude `ml-authentication` (face-recognition student login — biometric identification of children).** 🟡 Licence and metadata verified; **source not read** (`Gap 486-J`). |

## Supporting platform services

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **Apereo CAS** | https://github.com/apereo/cas | Apache-2.0 | SSO incumbent in higher ed. Where you enforce per-role access to an AI tier. |
| **phpCAS** | https://github.com/apereo/phpCAS | Apache-2.0 | **Restored p896.** The **PHP** CAS client, 802 ★ — the one that matters for Moodle. The row above is the server; this is how your tool actually joins the institution's existing SSO. **Pushed 2026-06-30; pin it.** |
| **java-cas-client** | https://github.com/apereo/java-cas-client | Apache-2.0 (byte-read; API says `NOASSERTION`) | **Restored p896.** JVM CAS client, 949 ★, pushed 2026-11-16. |
| **Aspects** | https://github.com/openedx/openedx-aspects | Apache-2.0 | **Restored p896.** First-party Open edX analytics — permissive, unlike the platform. |
| **Richie** | https://github.com/openfun/richie | MIT | Course catalogue/marketing CMS for Open edX. |
| **JupyterHub** | https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | Multi-user computational classrooms. |
| **Appsmith** | https://github.com/appsmithorg/appsmith | Apache-2.0 | Builds the teacher review queue that makes human-in-the-loop real rather than aspirational. |

## Mobile clients — permissive, and separable from their copyleft servers (restored in `p896`)

The most commercially useful licence asymmetry in this file. **Moodle, Open edX and Oppia are
GPL or AGPL on the server and permissive on the phone.** A studio can therefore ship a branded,
closed mobile experience over a copyleft platform the client already runs — which is exactly the
engagement shape that otherwise dies on the licence review. These rows were carried here and
deleted by the 2026-11-18 cleanup.

| Client | Repo | Licence | Server licence | Note |
|---|---|---|---|---|
| **Moodle App** | https://github.com/moodlehq/moodleapp | **Apache-2.0** | Moodle is GPL-3.0 | 1,007 ★, pushed 2026-11-17, **maintained by Moodle HQ itself**. The largest permissive first-party artefact in the Moodle ecosystem. Licence byte-read at `main/COPYING.txt`. |
| **Open edX Android** | https://github.com/openedx/openedx-app-android | **Apache-2.0** | Open edX is AGPL-3.0 | 38 ★, pushed 2026-11-09. |
| **Open edX iOS** | https://github.com/openedx/openedx-app-ios | **Apache-2.0** | Open edX is AGPL-3.0 | 31 ★, pushed 2026-10-30. |
| **Oppia Android** | https://github.com/oppia/oppia-android | Apache-2.0 | Oppia is Apache-2.0 | 422 ★, pushed 2026-11-18. Offline-capable by design — the mobile half of the low-connectivity brief. |

## Proctoring and exam integrity — restored in `p896`, and read the prohibition first

🔴 **Regulatory position before the rows, because it decides whether any of them can ship.**
Under the EU AI Act, *inferring emotions* in an education institution is not a high-risk
practice to be managed in 2027 — it is a **prohibited practice, in force since 2 February
2025**, outside narrow medical and safety grounds. Exam-access and assessment proctoring is
*separately* Annex III high-risk (obligations from 2 December 2027). So an EMEA proctoring build
has a hard floor: **no affect, stress or "suspicion" inference at all**, today. The open repos
below are near-uniformly built on webcam behaviour analysis, which is the capability the
prohibition targets.

| Tool | Repo | Licence | Stars / last push | Note |
|---|---|---|---|---|
| **OpenProctor** | https://github.com/kamlendras/OpenProctor | **AGPL-3.0** | 16 ★ · 2025-05-28 | The largest of them, and **idle for 18 months**. AGPL on top of the regulatory problem. |
| **pariksha** | https://github.com/SriSatyaLokesh/pariksha | **AGPL-3.0** | 0 ★ · 2026-11-07 | Active but single-author. |
| **sudosylabs/proctor** | https://github.com/sudosylabs/proctor | **AGPL-3.0** | 0 ★ · 2026-11-16 | Active but single-author. |
| **Proctora** | https://github.com/amaanwarsi/Proctora | MIT | 3 ★ · 2026-04-07 | The only permissive one. |
| **Online-Proctoring-system** | https://github.com/code-by-abrar/Online-Proctoring-system | MIT | 0 ★ · 2026-09-19 | Student project. |
| **ganesh-786/Proctor** | https://github.com/ganesh-786/Proctor | MIT | 0 ★ · 2025-06-09 | Idle. |

🔵 **The honest read: there is no adoptable open proctoring platform, and that is the finding.**
The category tops out at 16 ★ with the largest entry dormant, while `openedx/edx-proctoring`
(AGPL-3.0, in `repos/foundations.md`) remains the only institution-maintained option. For an EU
engagement the defensible product is **integrity by assessment design** — randomised item
generation (`PrairieLearn`), authenticated submission over CAS, and auditable human review
(`Appsmith`) — not behavioural surveillance. That is a studio position worth stating to a client
before they ask for a proctoring pilot.

## Curriculum data and learning-content assets

**Added in pass p890.** Not platforms, but deployable/extensible content assets — and the
category where this KB's MIT/Apache/BSD screen needs a different question asked, because a
*data* licence is not a *software* licence.

| Asset | Repo | Licence | Note |
|---|---|---|---|
| **os-taxonomy** | https://github.com/withmarbleapp/os-taxonomy | **ODbL-1.0** | Open curriculum graph for children's learning, 7,724 ★, pushed 2026-11-17. **Licence warning:** the Open Database Licence carries a **share-alike obligation on derived databases**. Extend the taxonomy and the extension may have to be published under ODbL. Excellent as a reference or an input; **not** a base for a proprietary curriculum data asset without counsel. |
| **jiangshan-map** | https://github.com/DeanChensj/jiangshan-map | GPL-3.0 | 江山时序 — interactive historical atlas of China, 403 BCE to present, 18 dynasties, with quiz modes. 7,708 ★, pushed 2026-11-18. The largest new education *content application* found. APAC-origin. GPL-3.0 blocks a closed derivative; deployable as-is. |

**Pattern worth noting.** Content assets in education are increasingly published under data or
copyleft licences while the *tooling* stays permissive — the inverse of the platform/tooling
split in this KB's headline fact. Licence triage therefore has to be run per artefact class,
not once per engagement.

**63 platforms and content assets, all URL- and licence-verified**, counted programmatically
across this file's tables (`UniTime` and `Timetablely` were restored in p894). **15 were restored
in `p896`** — four mobile clients, six proctoring tools, two Brazilian school systems, two CAS
clients and the Open edX analytics stack — after the shelf-vs-history diff showed they had been
deleted from this file by the 2026-11-18 cleanup rewrite without being listed as removals. All
re-measured today on both channels.

## Honest gaps

- **Unlicensed content corpora are the biggest trap in this category (added p891).** The largest
  education-tagged repo on GitHub, https://github.com/TapXWorld/ChinaTextbook (**84,728 ★**), has
  **no `LICENSE` or `COPYING` file on either `main` or `master`** — all four candidate paths
  return 404, and the GitHub API reports licence `NONE`. No licence means **all rights
  reserved**, and the contents are third-party-copyright PDF textbooks rather than code. It is
  larger than every platform in this file and usable in none of them. **Byte-read the licence of
  any content asset before it reaches a client deck** — curriculum corpora are where star count
  and usability diverge most sharply.

  **A second region, measured p895.** The highest-star African education repo this KB has found is
  https://github.com/Seunope/aloc-endpoints (**223 ★**, pushed 2026-11-17), a Nigerian
  **past-questions API** — self-described *"20,000 past questions API end points for POST-UTME,
  UTME, WASSCE, NECO"* — and it has **no licence on any of 8 candidate paths**
  (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` × `main`/`master`, all 404). Same shape as
  `ChinaTextbook` on a different continent: the most useful-looking asset in the category is the
  least usable, and it carries **third-party exam copyright on top of the licence absence**.
  **The rule generalises: for content, byte-read the licence *and* ask who owns the payload.**

- **No open-source education CRM.** Searches for one returned SIS and school-management
  products only. Student-recruitment and alumni CRM is proprietary (Salesforce Education
  Cloud, Ellucian). A studio can either build on a general open CRM or accept proprietary
  integration — there is no open vertical answer.
- **No open-source proctoring product worth deploying.** `openedx/edx-proctoring` is an
  integration shim, and the standalone candidates in earlier passes of this KB were
  student projects. Given that exam monitoring is EU AI Act Annex III high-risk, the absence
  of a credible, auditable open option is itself a market signal.
- **No open-source financial-aid or admissions-decisioning platform.** Also Annex III
  high-risk in the EU. Same signal, stronger.
