---
industry: education
region: Global
updated: 2026-11-17
---

# Vertical platforms — education

**Pass `p877`, 2026-11-17** (seventh pass of the day). **`p877` adds the two platforms this file
most needed and did not have: a permissively licensed SIS, and the largest permissively licensed
offline education server in the index.**

> **🟢 The permissive shortlist gains its first STUDENT INFORMATION SYSTEM.**
> [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) is **MIT** at the bytes (1,150 B,
> `sha256₁₂ b8694396d7dc`). Until this pass every SIS in this file was copyleft — Gibbon GPL-3.0,
> RosarioSIS GPL-2.0, openSIS with no licence file at all. **This is the only row in this file a
> studio can fork, rebrand and ship inside a proprietary deliverable.**
> 🟡 It is also **small** (57★, HEAD five months old): the gap closes on licence, not maturity.

> **🔴 [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
> — Apache-2.0, 43,849★, 4,526 forks, 813 commits in 12 months — was in NO curated file in this
> KB before `p877`**, despite being the second-largest education-native repository the KB knows of.
> The *Offline & low-connectivity delivery* section below described that category as "first-class"
> while listing only GPL-3.0 and LGPL options. **The permissive leader of the category was missing
> from the file that calls it first-class.**

**Previous pass note (`p876`)** (sixth pass of the day). `p876` adds the **learning-analytics layer**
to this file, which has until now described platforms that *generate* learner telemetry without
naming anywhere to *put* it. Two permissive, maintained Learning Record Stores are verified below
and in `repos/foundations.md`.

> 🟢 **The permissive shortlist gets a new row and it is a strategically useful one.**
> **`openfun/ralph`** (MIT) comes from **France Université Numérique**, the consortium that
> operates France's national Open edX platform. It is the rare case in this vertical where a
> *public-sector European* project ships under a **permissive** licence — every other EMEA
> platform of comparable provenance in this file is GPL or AGPL. For an EU public-sector bid where
> sovereignty and provenance are scored, that combination is worth more than its 52 stars suggest.

**Previous pass note (`p875`)** (fifth pass of the day). `p875` measured **78 addresses** first-hand
for stars, SPDX licence and last-push date — the channel four passes called impossible (see
`repos/trending.md`). It did not re-verify `p874`'s licence bytes; it independently **corroborated
every one of them through SPDX**, including `p874`'s correction of `SriSatyaLokesh/pariksha` to
AGPL-3.0. Two sections change: **proctoring is re-framed from a licence problem to an adoption
problem**, and the copyleft thesis below is now **quantified**.

> **🔴 The proctoring category has 19 stars across six repositories, and four of them have zero.**
> Three passes argued about the *licence* of open-source proctoring code. The licence was never the
> binding constraint. **There is no open-source proctoring platform to build on in this vertical —
> permissive or copyleft — and the correct advice to a client asking for one is to buy, or to
> treat it as bespoke from zero.** Full table in the proctoring section below.

> **🟡 `OpenOlat` returns `NOASSERTION` from GitHub's SPDX detector** while its licence bytes read
> Apache-2.0. The byte-read is authoritative — a modified header almost certainly defeats
> auto-detection — but **OpenOlat is the load-bearing "only permissive full LMS" claim in this
> file, and a client's counsel will run the automated check and get `NOASSERTION`.** Brief them
> before they ask. `BerriAI/litellm` shows the same pattern. 🔴 **`CaviraOSS/PageLM` DOES NOT, and
> `p877` corrects this sentence:** PageLM's `NOASSERTION` is **not** a detector artefact — its bytes
> are a bespoke non-commercial licence that **prohibits redistribution**. Grouping it with OpenOlat
> and litellm as "same pattern, byte-read will clear it" is the exact inference `intel/trends.md`
> **T14** warns against: the token is identical, the grants are opposite.
> 🔵 **OpenOlat is nonetheless T14's fourth confirmed case** — and the most commercially important,
> since it carries this file's "only permissive full LMS" claim;
> `OS4ED/openSIS-Classic` returns `NONE` — **no detectable licence at all**, treat as all rights
> reserved until proven otherwise.

**Previous pass note (`p874`):** rewrote the proctoring section against seven byte-read licences
and corrected the category heading. Real, deployed systems that can be customised with AI on top —
the education equivalents of Odoo for ERP or OpenMRS for healthcare. Existence and licence bytes
verified via `git ls-remote` + `raw.githubusercontent.com` on the resolved default branch.

> **The single most important strategic fact in this file:** the education platform layer is
> **overwhelmingly copyleft**. Of the 20 verified platforms below, only **5** are permissive
> (Apache-2.0 / MIT / BSD). The brief asks for MIT / Apache / BSD because those are what
> Globant can build on — in this vertical that constraint eliminates Moodle, Canvas, Open edX,
> ILIAS, Chamilo and both SIS options. The workable pattern is therefore **not** forking a
> platform: it is building permissive AI services that attach over **LTI 1.3** and **xAPI**.
> That integration seam is the actual product surface in education.
>
> **🟢 `p875` quantifies this.** Measured by installed attention, the permissive column is real but
> consistently smaller: `oppia` 6,997 (Apache-2.0), `sakai` 1,238 (ECL-2.0), `kolibri` 1,177 (MIT),
> `opencast` 513 (ECL-2.0), `OpenOlat` 452 (Apache-2.0*) — against `moodle` 7,618 (GPL-3.0),
> `canvas-lms` 6,918 (AGPL-3.0), `frappe/lms` 3,428 (AGPL-3.0), `chamilo` 1,025 (GPL-3.0),
> `ILIAS` 512 (GPL-3.0). **No permissive LMS has the installed base of Moodle or Canvas.** The
> conclusion survives the measurement and is strengthened by it: do not fork a platform to chase a
> licence — **attach over LTI 1.3 and xAPI, where the permissive layer is yours to write.**

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
| **GegoK12** 🟢 **new `p877`** | https://github.com/Gego-K12/gegok12 | 🟢 **MIT** — byte-read, 1,150 B, `sha256₁₂ b8694396d7dc` | `main` | 🟢 **The first and only permissive SIS in this KB — closes a gap open since `p872`.** Full-featured school management system in **Laravel/PHP**, **API-first** (`api.md` in-tree), `Dockerfile` + `docker-compose.yml`, `lang/` localisation, plus separate Android **parent** and **teacher** apps. 113 commits in 12 months. 🟡 **57★ and HEAD `2026-06-25`** — propose it as a base you will own and extend, not a community you are joining. 🔴 **GitHub reports `NOASSERTION`** because line 3 of its `LICENSE` is `<!-- SPDX-License-Identifier: MIT -->`; the bytes are stock MIT. Do not let a licence-API readout disqualify it. |
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
| **Project NOMAD** 🟢 **new `p877`** | https://github.com/Crosstalk-Solutions/project-nomad | **Apache-2.0** (10,778 B, byte-read) | `main` | 🟢 **The permissive leader of this category, and now the default starting point.** An offline-first knowledge and education server: Wikipedia, thousands of books, courses, maps and **optional local AI**, all from one box with no internet. **43,849★ / 4,526 forks / 813 commits in 12 months** — and on an appliance repository, forks read as deployments. Dockerised, with `collections/`, `admin/` and `install/` in-tree and semantic-release. **Apache-2.0 is the decisive fact against Kiwix (GPL-3.0) and Internet-in-a-Box (LGPL):** a ministry deliverable can be rebranded and redistributed without copyleft obligations on the surrounding work. |

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
| **SQL LRS (`yetanalytics/lrsql`)** | Apache-2.0 | 🟢 **New in `p876`** — learner telemetry store (xAPI). The default for measurement |
| **Ralph (`openfun/ralph`)** | MIT | 🟢 **New in `p876`** — LRS + data pipeline, **Open edX-native**, EMEA public sector |
| **Project NOMAD** | Apache-2.0 | 🟢 **New in `p877`** — offline-first education server, **43,849★**. The permissive answer for low-connectivity and ministry equity programmes |
| **GegoK12** | MIT | 🟢 **New in `p877`** — **the only permissive SIS.** Laravel, API-first. Small; adopt-and-own, not join |

### Learning analytics — the layer this file was missing

Every platform above emits learner events; none of them is where those events should be kept for
analysis. That is the Learning Record Store, and until `p876` this KB named only
`LearningLocker` — **GPL-3.0, default branch last moved 2021-11-16**.

| Platform | Licence | Stars | HEAD | Use it for |
|---|---|---:|---|---|
| https://github.com/yetanalytics/lrsql | **Apache-2.0** | 144 | 2026-11-14 | The production LRS. SQLite for a pilot; Postgres 14–18, MariaDB or MySQL at scale. OIDC, Docker, documented AWS deployment |
| https://github.com/openfun/ralph | **MIT** | 52 | 2026-10-12 | LRS **and** pipeline. Take it when the platform is **Open edX** (tracking-log→xAPI converters ship in-tree) or when European public-sector provenance is scored. Helm chart included |
| https://github.com/adlnet/ADL_LRS | Apache-2.0 | 335 | 2025-11-14 | The xAPI authors' reference implementation. 🟡 **0 commits in 12 months** — test against it, do not deploy it |
| https://github.com/davidpesce/moodle-logstore_xapi | GPL-3.0 | 83 | 2026-10-29 | The Moodle→LRS bridge. Copyleft, but it is a plugin **inside** GPL Moodle, so it concedes nothing new |
| https://github.com/LearningLocker/learninglocker | GPL-3.0 | 587 | **2021-11-16** | 🔴 **Do not start here.** Five years cold, 0 commits in 12 months. Listed so it is not re-imported from a listicle |

🔴 **The one thing you lose by leaving Learning Locker: dashboards.** It bundled a reporting UI;
`lrsql` and `ralph` do not. Pair them with **Aspects/Superset** (Apache-2.0) or **Grafana**
(AGPL-3.0 — fine self-hosted, a problem in a distributed product) and **price that work
explicitly**. See `compose/patterns.md` **P14**.

## Exam integrity & proctoring — 🔴 `p875`: real demand, and effectively NO supply

> **`p875` measured the whole category. Nineteen stars across six repositories. Four have zero.**
>
> | Repo | Stars | Licence (byte-read, SPDX-confirmed) | Last push |
> |---|---:|---|---|
> | `kamlendras/OpenProctor` | 16 | AGPL-3.0 | 2025-05-28 🔴 |
> | `amaanwarsi/Proctora` | **3** | MIT | 2026-04-07 |
> | `ganesh-786/Proctor` | **0** | MIT | 2025-06-09 🔴 |
> | `code-by-abrar/Online-Proctoring-system` | **0** | MIT | 2026-09-19 |
> | `sudosylabs/proctor` | **0** | AGPL-3.0 | 2026-11-16 |
> | `SriSatyaLokesh/pariksha` | **0** | AGPL-3.0 ✅ (`p874`'s correction, SPDX-confirmed) | 2026-11-07 |
>
> **The framing of the last three passes was wrong in a way that mattered.** `p871` said no
> permissive code existed; `p872` said two existed and both were copyleft; `p874` found three MIT
> repos and said the gap was maturity, not licence. `p874` was closest — and `p875`'s measurement
> shows the maturity gap is not a gap but an absence. **Not one of these projects has a user
> community.** A licence is a permission to build on something; none of these is a something.
>
> 🟡 **What to tell a client who asks for open-source proctoring:** there isn't any. The options
> are a commercial proctoring vendor integrated over LTI, or an accepted redesign of the
> assessment so that proctoring is not required — which, given `intel/trends.md` **T9** on
> scaffolding and `openedx/edx-proctoring` (69 stars, AGPL-3.0) being the only thing here with
> institutional provenance, is usually the better conversation. **Do not propose building one from
> these repositories.**

### Original `p874` category notes (licence bytes, retained)

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

- ~~**No permissive open-source SIS exists**~~ — 🟢 **CLOSED by `p877`.**
  [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) is **MIT** at the bytes (1,150 B,
  `sha256₁₂ b8694396d7dc`): Laravel, API-first, Dockerised, with Android parent and teacher apps
  and 113 commits in 12 months. The three copyleft options stand as recorded — RosarioSIS GPL-2.0,
  Gibbon GPL-3.0, openSIS-Classic with no licence file at all.
  🔵 **Why it took five passes to find a repository that was always there:** the GitHub licence API
  reports `NOASSERTION` for it, because line 3 of its `LICENSE` is an SPDX comment. **The gap was
  never in the ecosystem; it was in trusting a licence-detector readout as a licence.** See
  `intel/trends.md` **T14**.
  🟡 **The restated gap, which is real:** a permissive SIS exists but is **small** (57★, HEAD five
  months cold). *A permissive, AI-native, institution-grade SIS* remains the clearest product gap
  in this file — the difference is that there is now a permissive base to start from rather than a
  copyleft one to work around.
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
