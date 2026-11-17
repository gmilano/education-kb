---
industry: education
region: Global
updated: 2026-11-17
---

# Vertical platforms — education

**Pass `p874`, 2026-11-17** (fourth pass of the day; rewrites the **proctoring** section against
seven byte-read licences — the category heading was wrong and is corrected below. `p873`'s
RosarioSIS and accessibility-conformance work stands). Real, deployed systems that can be customised with AI on top —
the education equivalents of Odoo for ERP or OpenMRS for healthcare. Existence and licence
bytes verified this run via `git ls-remote` + `raw.githubusercontent.com` on the resolved
default branch.

> **The single most important strategic fact in this file:** the education platform layer is
> **overwhelmingly copyleft**. Of the 20 verified platforms below, only **5** are permissive
> (Apache-2.0 / MIT / BSD). The brief asks for MIT / Apache / BSD because those are what
> Globant can build on — in this vertical that constraint eliminates Moodle, Canvas, Open edX,
> ILIAS, Chamilo and both SIS options. The workable pattern is therefore **not** forking a
> platform: it is building permissive AI services that attach over **LTI 1.3** and **xAPI**.
> That integration seam is the actual product surface in education.

## Learning management systems

| Platform | Repo | Licence | Branch | Position & AI surface |
|---|---|---|---|---|
| **Moodle** | https://github.com/moodle/moodle | GPL-3.0 (`COPYING.txt`) | `main` | The most widely deployed LMS worldwide and dominant in EMEA and LATAM public education. Has a first-party AI subsystem with pluggable providers, so **AI can be added as a plugin without forking** — the cleanest copyleft-safe integration path in this file. |
| **Open edX** | https://github.com/openedx/edx-platform | AGPL-3.0 | `master` | Originated at MIT and Harvard, now stewarded by the non-profit Axim Collaborative. The standard choice for large-scale MOOC and national-platform deployments. Note: the *platform* is AGPL-3.0 — the Apache-2.0 figure that circulates in listicles refers to satellite repos such as `openedx-aspects`, not to `edx-platform`. Verified this run. |
| **Canvas LMS** | https://github.com/instructure/canvas-lms | AGPL-3.0 | `master` | Dominant in North American higher education. The open-source edition carries core LMS function; some commercial features are withheld. AGPL. |
| **ILIAS** | https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | `release_11` | Strong in German-speaking EMEA, including public-sector and military training. Note the default branch is `release_11`, not `main`. |
| **Chamilo** | https://github.com/chamilo/chamilo-lms | GPL-3.0 | `master` | Significant installed base in **LATAM** and francophone Africa; lighter to operate than Moodle, which is why ministries with thin IT capacity pick it. |
| **Sakai** | https://github.com/sakaiproject/sakai | **ECL-2.0** | `master` | Apereo Foundation, research-university focus. Educational Community License 2.0 is an Apache-2.0 derivative — **more permissive than the rest of this table**, a genuinely under-used fact. |
| **OpenOLAT** | https://github.com/OpenOlat/OpenOlat | **Apache-2.0** | `master` | Swiss-origin, used across EMEA higher education. **The only major full LMS here under a clean permissive licence** — the obvious base if a client needs a customised LMS that Globant can extend without copyleft obligations. |
| **Frappe LMS** | https://github.com/frappe/lms | **AGPL-3.0** | `develop` | Modern, lightweight LMS on the Frappe framework. **Correction recorded this pass:** multiple 2026 listicles state MIT; the licence bytes at `license.txt` are **AGPL-3.0**. |
| **Kolibri** | https://github.com/learningequality/kolibri | **MIT** | `develop` | Learning Equality. Purpose-built for **offline-first, low-connectivity and low-resource deployments** — the platform of record for rural LATAM, Sub-Saharan Africa and South Asia programmes. MIT-licensed. For any equity-of-access or ministry-of-education mandate, this is the starting point, not Moodle. |

## Courseware, content & assessment

| Platform | Repo | Licence | Branch | Position & AI surface |
|---|---|---|---|---|
| **Oppia** | https://github.com/oppia/oppia | **Apache-2.0** | `develop` | Interactive lesson platform built around structured "explorations" with misconception-specific feedback. Apache-2.0, and its explicit misconception model is unusually well matched to LLM-generated remediation. |
| **Perseus (Khan Academy)** | https://github.com/Khan/perseus | **MIT** | `main` | Khan Academy's exercise and question rendering framework. MIT — directly embeddable, and the fastest route to a credible practice-item UI. |
| **H5P** | https://github.com/h5p/h5p-php-library | GPL-3.0 | `master` | The interactive-content standard embedded inside Moodle, Canvas and Open edX. Content-type authoring for interactive video, branching scenarios, quizzes. |
| **Anki** | https://github.com/ankitects/anki | AGPL-3.0 | `main` | The dominant spaced-repetition application. Relevant as an **export target**: DeepTutor already exports to it, so a Globant build can meet learners in the tool they use. Pair with MIT-licensed `fsrs4anki` for the scheduler. |

## Student information, library & repository systems

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **Gibbon** | https://github.com/GibbonEdu/core | GPL-3.0 | `v31.0.00` | School management / SIS for K-12. Note: default branch is a version tag, not `main`. |
| **openSIS Classic** | https://github.com/OS4ED/openSIS-Classic | **GPL per README; no licence file** | `master` | Student information system. **Licence flag:** there is no `LICENSE`, `COPYING` or `license.txt` on the default branch — the GPL claim exists only in prose in the README. Treat the grant as unconfirmed until clarified with OS4ED. |
| **RosarioSIS** | https://github.com/francoisjacquet/rosariosis | **GPL-2.0** | **`mobile`** | **New in `p873`.** Mature PHP/PostgreSQL student information system, used in production by schools, academies and colleges; latest tags `v9.3`, `v9.3.1`, `v9.3.2`. **The default branch is `mobile`** — a feature name, not `main` or `master`. Nothing about the address hints at it and no heuristic would guess it: a `raw.githubusercontent.com` path built on an assumed `main` 404s, which would have been published as "no licence file" and then as "no grant". Resolve with `git ls-remote --symref` first, always. The **third** verified open-source SIS, and the **third** that is copyleft. |
| **Koha** | https://github.com/Koha-Community/Koha | GPL-3.0 | `main` | The mature open-source integrated library system; very large installed base in school and university libraries worldwide. |
| **DSpace** | https://github.com/DSpace/DSpace | **BSD** | `main` | Institutional repository for theses, datasets and scholarly output. **Permissive** — a strong base for AI-assisted discovery and metadata enrichment over a university's own corpus. |
| **Open Journal Systems** | https://github.com/pkp/ojs | GPL-3.0 | `main` | PKP's scholarly publishing platform; heavily used by LATAM and Global South universities for their own journals. |

## Classroom delivery & lecture capture

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **BigBlueButton** | https://github.com/bigbluebutton/bigbluebutton | LGPL | `v4.0.x-develop` | Virtual classroom built for teaching rather than for meetings (whiteboard, breakout rooms, polling); integrates with Moodle and Canvas. LGPL — linking is permitted, which makes it friendlier than GPL for an attached service. |
| **Opencast** | https://github.com/opencast/opencast | **ECL-2.0** | `develop` | University lecture capture and video management. ECL-2.0 (Apache-derived, permissive). The natural source of the lecture-video corpus a tutoring agent should be grounded in. |

## Offline & low-connectivity delivery

Treated as a first-class category rather than a footnote, because it decides whether a
ministry programme reaches rural schools at all.

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **Kiwix** | https://github.com/kiwix/kiwix-tools | GPL-3.0 | `main` | Offline Wikipedia and educational-archive reader (ZIM format). Already an ingest source for DeepTutor, so an offline corpus can feed an offline tutor. |
| **Internet-in-a-Box** | https://github.com/iiab/iiab | LGPL | `master` | Turnkey offline learning server — bundles Kiwix, Moodle and content libraries onto low-cost hardware for schools without reliable connectivity. |

**23 verified platforms.**

## Permissive-licence shortlist

For a Globant engagement that must avoid copyleft obligations, the verified permissive set is:

| Platform | Licence | Use it for |
|---|---|---|
| **OpenOLAT** | Apache-2.0 | A full LMS you can extend and commercialise |
| **Kolibri** | MIT | Offline-first / low-connectivity delivery |
| **Oppia** | Apache-2.0 | Interactive courseware with misconception handling |
| **Perseus** | MIT | Exercise and assessment item UI |
| **Sakai** | ECL-2.0 | Research-university LMS |
| **Opencast** | ECL-2.0 | Lecture capture and video corpus |
| **DSpace** | BSD | Institutional repository / scholarly corpus |

## Exam integrity & proctoring — real demand, permissive supply that exists but is not institution-grade

🔴 **This heading said "no permissive supply" for two passes and that was wrong.** `p871` searched
and found nothing. `p872` found two projects, both AGPL-3.0, and concluded the permissive shelf was
empty. **`p874` searched the category again and byte-read seven licences: three are MIT.** The
strategic conclusion survives, but for a different and more precise reason — **not "nothing
permissive exists", but "the three permissive codebases are reference implementations, not
platforms."** The distinction decides what you can say in a procurement.

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **Proctor** | https://github.com/sudosylabs/proctor | **AGPL-3.0** | `main` | Self-hosted examination **and** proctoring platform aimed at institutions — Go server, React front end. The most complete open-source project in this category. No published supported-release or compatibility window, so treat maturity as unproven. |
| **OpenProctor** | https://github.com/kamlendras/OpenProctor | **AGPL-3.0** | `main` | Next.js/TypeScript. **Licence correction: secondary listings say MIT; the bytes on `main` say AGPL-3.0.** Thin install documentation, Vercel-oriented rather than clearly self-hostable. |
| **Proctor** (ganesh-786) | https://github.com/ganesh-786/Proctor | 🟢 **MIT** | `main` | **NEW `p874`.** Self-described modular, microservices-based AI proctoring. The most architecturally ambitious of the permissive three. **No tags, 1 branch** — a reference implementation. |
| **Proctora** | https://github.com/amaanwarsi/Proctora | 🟢 **MIT** | `main` | **NEW `p874`.** Flask + OpenCV + MediaPipe; webcam, microphone-noise and tab-switch monitoring, session violation logging, CI configured. 🔴 **Its own README says it should not be presented as a secure exam platform in its current state** — the project's words, not this KB's. |
| **SecureExam AI** | https://github.com/code-by-abrar/Online-Proctoring-system | 🟢 **MIT** | `main` | **NEW `p874`.** FastAPI + PostgreSQL with client-side TensorFlow.js face tracking and device detection. **No tags, 1 branch.** |
| **Pariksha** | https://github.com/SriSatyaLokesh/pariksha | 🔴 **AGPL-3.0** | `main` | **NEW `p874` — and a secondary-source correction.** A search summary presented it as *the* Apache-2.0 exam platform in this category. **The licence bytes on `main` say GNU Affero GPL.** Pre-alpha besides: the repo holds requirements and schemas, with the candidate runtime promised for v0.1. |
| **edx-proctoring** | https://github.com/openedx/edx-proctoring | 🔴 **AGPL-3.0** | **`master`** | **NEW `p874`.** Open edX's own proctoring subsystem — the realistic choice if the client is already on Open edX. Note the default branch is **`master`**, not `main`. |

**How to read this table — and it reads differently than it did in `p873`.** Seven candidates,
**three MIT and four AGPL-3.0**, and the licence axis no longer separates the useful from the
useless. The **maturity** axis does:

- 🟢 **The three MIT projects are permissive and genuinely runnable**, and **not one is
  institution-grade**: single-branch, no tagged releases, no supported-version policy, and in
  `Proctora`'s case an explicit author disclaimer against secure use. **Do not put one in front of
  a procurement board as a platform.** Their real value is as *capability references* — the
  face-tracking, tab-switch and audio-monitoring pieces are readable MIT code you can learn the
  shape of a build from, and legally reuse.
- 🔴 **The one complete platform (`sudosylabs/proctor`) is AGPL-3.0.** Workable where the
  institution hosts it itself — the copyleft obligation stays inside one tenancy, which is the
  normal education deployment — and unusable inside a distributed proprietary product. So the
  *mature* path remains open to a Globant **integration** engagement and closed to a Globant
  **product**.
- 🔵 **Net position:** a defensible permissive proctoring product would be a **greenfield build**
  that borrows from the MIT three. `p874` is the first pass able to state that with the licence
  bytes of seven candidates behind it rather than as an inference from two.

**The regulatory context matters more than the licence here.** The EU AI Act puts exam proctoring
in the high-risk tier (obligations from **2 December 2027** after the Digital Omnibus delay), the
Article 5(1)(f) **ban on emotion inference in education has applied since 2 February 2025**, and
Vietnam's **Decision 33/2026/QD-TTg** lists AI that monitors learner behaviour using biometric or
other automated mechanisms as a high-risk education system. Any webcam-and-gaze proctoring product
is now building directly into the most heavily regulated corner of education AI, in at least two
major jurisdictions, with immature copyleft tooling.

**The studio recommendation that follows from that:** lead with **assessment redesign** — oral
defence, process evidence, version-history review, in-class authentic tasks, `edx-ora2`
open-response workflows — and treat proctoring as the fallback the client asks for, priced with
its conformance burden visible. Detection-based integrity is losing on both the evidence and the
regulation; see `intel/trends.md` T8.

## Accessibility conformance — where it exists in this stack, and where it does not

New in `p873`, because it decides public-sector bids. The agent layer has almost no conformance
documentation (see `agents/top.md` gaps: `CAHLR/OATutor` is the only education-native agent in this
KB with a published statement). The **platform** layer is better placed: **Moodle core and its
mobile app are stated to be certified to WCAG 2.2 AA**, alongside Section 508 alignment. That is a
**vendor claim** (Open LMS) and `support.openlms.net` is unreachable from this session, so the
correct action in a bid is to **request the VPAT/ACR**, not to repeat the claim.

The practical consequence is an architecture decision, not a compliance footnote:

> Where **Section 508 / EN 301 549 / WCAG** conformance gates procurement, **do not ship your own
> learner-facing front end.** Launch the agent as an **LTI 1.3 tool inside a platform that already
> holds a conformance statement** (`Cvmcosta/ltijs`, Apache-2.0, is the plumbing) so the
> conformance story rides on the platform, and keep the custom UI for staff-facing surfaces where
> the bar is lower.

Two further facts, both secondary-sourced because EU primary sources are unreachable: the
**European Accessibility Act has applied since 28 June 2025**, and the next **EN 301 549** revision
aligning it with **WCAG 2.2 AA** is reported as due in the Official Journal in late 2026. And the
failure mode that actually loses audits is **embedded content, not the platform** — an accessible
LMS routinely serves an inaccessible SCORM package, PDF workbook or generated slide deck. **Any AI
content generator in the build inherits that obligation for everything it emits.**

## Declared gaps

- **No permissive open-source SIS exists — now three independent data points, not two.** `p873`
  verified **RosarioSIS** (GPL-2.0) alongside Gibbon (GPL-3.0) and openSIS-Classic (no licence
  file at all). Three verified options, **zero permissive**. A permissive, AI-native SIS is an
  unmet need — and the most clearly evidenced product gap in this file.
- ~~**No *permissively licensed* open-source proctoring platform exists.**~~ **RESTATED by `p874`,
  which found the earlier framing factually wrong.** Permissive proctoring code **does** exist:
  `ganesh-786/Proctor`, `amaanwarsi/Proctora` and `code-by-abrar/Online-Proctoring-system` are all
  **MIT**, byte-read on `main`. **The accurate gap is maturity, not licence:** of seven verified
  candidates, the three permissive ones are single-branch and untagged (one disclaimed by its own
  author), and the only complete platform is AGPL-3.0. 🔴 **A secondary source also had to be
  corrected here** — `SriSatyaLokesh/pariksha` was presented as Apache-2.0 and is AGPL-3.0. Given
  that the EU moves proctoring into the high-risk tier on **2 Dec 2027** and Vietnam already lists
  biometric learner monitoring as high-risk, an institution-grade permissive proctoring platform
  remains the clearest unbuilt product in education AI — and plausibly one that should not be built.
- **No LATAM-origin education *platform*** surfaced in either pass's searches. LATAM appears in
  this file as a large **deployer** of Moodle, Chamilo, Kolibri and OJS, not as an originator
  of platforms. `p872` refines the picture: the region's own contribution is a **sovereign
  foundation model**, **Latam-GPT** (CENIA-led, launched 10 Feb 2026, open weights, Spanish and
  Portuguese, corpus gated behind an NDA) — infrastructure beneath the platform layer, not a
  platform. That asymmetry is itself the regional finding.
