---
industry: education
region: Global
updated: 2026-10-21
---

# Education — vertical platforms to customise with AI

**Pass 367 · 2026-10-21.** 🔴 **`p364` read all 60 platform READMEs on this shelf and graded
their companions against a corpus that could not see 496 live repositories. `p367` built the
missing channel, and seven of the repositories it surfaced are components of platforms this
shelf publishes — four of them AGPL-3.0.**

🔵 **Why this shelf is where the defect bites hardest.** A platform row's commercial value
is *"what does adopting this make you install?"* — `p362`'s `QingdaoU/OnlineJudge` finding,
`p364`'s sweep, `p366`'s manifest channel. 🔴 All three tested absence against a
**URL-only** corpus, so a component discussed here as a bare backticked slug counted as
*absent from this base* when it was sitting on these shelves, and counted as *present* to
nothing.

| Component surfaced by channel B | Licence, read from payload | The platform it belongs to |
|---|---|---|
| 🔴 [`openedx/openedx-filters`](https://github.com/openedx/openedx-filters) | **AGPL-3.0** (`main/LICENSE.txt`, 35 136 B) | Open edX extension framework |
| 🔴 [`overhangio/openedx-scorm-xblock`](https://github.com/overhangio/openedx-scorm-xblock) | **AGPL-3.0** (`master/LICENSE.txt`, 34 522 B) | the SCORM player for Open edX / Tutor |
| 🔴 [`instructure/analytics`](https://github.com/instructure/analytics) | **AGPL** (`master/LICENSE.txt`, 34 519 B) | Canvas analytics |
| 🔴 [`bgwdotdev/libre-oneroster`](https://github.com/bgwdotdev/libre-oneroster) | **AGPL** (`master/LICENSE`, 34 522 B) | OneRoster rostering |
| 🟡 [`lumieducation/h5p-nodejs-library`](https://github.com/lumieducation/h5p-nodejs-library) | **GPL** (`master/LICENSE`, 35 146 B) | the Node implementation behind H5P |
| 🟡 [`bigbluebutton/bbb-install`](https://github.com/bigbluebutton/bbb-install) | **LGPL** (`v4.0.x-release/LICENSE`) | BigBlueButton deployment |
| 🟢 [`instructure/qtimigrationtool`](https://github.com/instructure/qtimigrationtool) | **BSD-3-Clause** (`master/LICENSE.txt`, 1 391 B) | QTI import for Canvas |

🟢 **The `qtimigrationtool` cell is a correction to `p367`'s own grader, published beside the
first verdict.** It was first graded `UNCLASSIFIED`, because the body reads *"Redistribution
and use **of this software** in source and binary forms (where applicable)"* — a University
of Cambridge BSD variant — and the classifier tested only the canonical *"Redistribution and
use in source and binary forms"*. 🔴 That is the `p366` precedence/ladder defect in a third
costume: **an instrument reporting UNCLASSIFIED when it means "my phrase list is too
narrow."** 🔵 Read by hand, the body is plainly BSD-3-Clause, holder **University of
Cambridge (2004–2008)**, GUI code **Pierre Gorissen**.

### 🔴 What this means for the Open edX recipes on this base

🔵 **Four AGPL components, and two of them sit in the middle of patterns this base already
publishes.** 🔴 `openedx-scorm-xblock` is the only maintained SCORM player for the Tutor
stack, and `openedx-filters` is the documented extension point — *the* hook an AI layer is
supposed to attach to. 🟢 **Neither is a surprise about Open edX** (the platform is AGPL and
this shelf says so), 🔴 **but neither was in the corpus**, so no absence or exposure figure
this base published about the Open edX tier counted them.

🟡 **The commercial reading, stated plainly for an engagement:** on Open edX, an AI layer
that attaches through `openedx-filters` is attaching to AGPL-3.0, and **§13** is the live
clause because a learning platform is a network service. 🟢 The pattern that avoids it is the
one this base already prefers — a **separate service** the platform calls, with the AGPL
component unmodified — and `compose/patterns.md` carries it. 🔴 What changes is that the
exposure is now *measured on this shelf* rather than inferred from the platform's own grant.

🔵 **`p367` adds no platform row.** The seven above are **components**, not platforms, and
`p364`'s rule stands: a companion is never promoted to a component on the strength of a link,
and a component is never shelved as a platform. They are recorded here because this is the
shelf whose figures they change.

**Pass 366 · 2026-10-21.** 🟢 **`p366` adds no platform and brings this shelf the
discriminator that `p364`'s sweep of it lacked.** `p364` read the README of all 60 rows here,
found **91** companion edges and graded **72 of 91 (79%)** as absent and ungraded. 🔵 **`p366`
ran the same sweep over the two shelves `p364` skipped (329 addresses, 484 edges) and added
the channel `ACTION ZZ-bs` named but never built — the host's own manifest — and it changes
how `p364`'s 91 should be read.**

| The direction of a README-named companion | Share of 484 edges |
|---|---:|
| 🔴 **declared in the host's manifest — a real dependency** | **17.8%** |
| 🟡 an **adopter** of the host, pointing the other way | 6.6% |
| 🟡 a bare **mention**, neither declared nor flagged | **55.0%** |
| 🔴 **host ships no manifest — direction UNANSWERABLE** | **20.7%** |

🔴 **So `p364`'s "79% absent" is a count of mentions, not of exposure.** Roughly four in five
edges of this shape are not dependencies at all. 🟢 **What that buys this shelf is cheaper
diligence, not weaker diligence:** on `p366`'s own population the backlog fell from **330**
absent companions to **58** worth grading — **5.7×** — for one manifest read per host. 🔵 The
`Marsha` row below remains the reference case and is unaffected: its exposure was established
from the **manifest** (`@types/iframe-resizer`, types only) plus a documented build step, which
is exactly the channel `p366` has now generalised.

🟡 **And the limit is on the record: 20.7% of edges cannot be graded on this channel at all**
because 34 of 165 hosts publish no manifest at any of 16 rungs. That is the same shape as
`p365`'s **31.9%** unpinnable rows — an instrument that works on most of a population and is
silent, not negative, on the rest.

🔵 **ERP/SIS absence restated rather than quietly dropped**, as `p363` requires. The
`open source platform education ERP CRM MIT Apache` leg returned **OpenEduCat's own glossary
pages in five languages** plus a generic CRM tag page, Apache OFBiz and a **2010** release
note for CK-ERP — the **thirteenth** consecutive listicle. 🔴 **No permissive education ERP has
been found in thirteen attempts.** OpenEduCat remains **LGPLv3** on an **LGPLv3** Odoo base.
🟡 Apache OFBiz is genuinely Apache-2.0 but is **not an education system**, and CK-ERP's last
visible release is **2010**; neither is shelved. Evidence:
[`regional-legs`](../evidence/regional-legs.2026-10-21-p366.tsv).

🟢 **`p366` evidence:** [`edge-direction`](../evidence/edge-direction.2026-10-21-p366.tsv) ·
[`companion-closure-unswept`](../evidence/companion-closure-unswept.2026-10-21-p366.tsv) ·
[`exposure-grants`](../evidence/exposure-grants.2026-10-21-p366.tsv) ·
[`regional-legs`](../evidence/regional-legs.2026-10-21-p366.tsv)

🔴 **Gate state `p366`: NOT RUN** — `make hooks` could not execute in this pass's environment.
No claim in this section was gate-checked; all of it is first-hand `ls-remote` and
`raw.githubusercontent.com`.

---

**Pass 365 · 2026-10-21.** 🟢 **`p365` adds no platform and qualifies every grant on this
shelf with the axis `p364` opened.** `p364` showed that a platform's permissive headline
can hide a **copyleft component** (the `iframe-resizer` instance: GPL-3.0-or-commercial at
`master`, MIT at `v3.5.13`). 🔵 **`p365` measured the *version* half of that across the whole
permissive population — 191 addresses, each read at the default branch and at the latest
stable tag — and the two findings pull in opposite directions:**

- 🟢 **The hazard is rare.** 128 of the 130 pinnable addresses carry the **same** licence
  family at both pins. For a platform with a real release history — and 94 of the 130 have
  **six or more** tags — reading the grant at the branch is sound.
- 🔴 **The hazard is concentrated where release discipline is unproven.** Both mismatches sit
  in the 11-row class that has tagged **exactly once**: 🔴 **18.2%** there against 🟢 **0%**
  among the 119 rows with two or more tags.
- 🔴 **And for 61 of the 191 — 31.9% — there is no stable tag to read at all.** The
  "pin it and check" instruction cannot be executed. Those rows are consumed at a moving
  branch by construction.

🔵 **What this means for a platform selection on this shelf, stated plainly:** the grant
column here is trustworthy for the mature platforms it mostly describes. The pin question
is a **triage** step, not a re-audit — count `refs/tags/*` in one request, and read the
grant at the tag only where the count is one.

🟢 **`p365` evidence:** [`version-axis-frequency`](../evidence/version-axis-frequency.2026-10-21-p365.tsv) ·
[`single-tag-risk`](../evidence/single-tag-risk.2026-10-21-p365.tsv) ·
[`transport-enumeration`](../evidence/transport-enumeration.2026-10-21-p365.tsv)

🔵 **ERP/SIS absence restated rather than quietly dropped**, as `p363` required: the
`open source platform education ERP CRM MIT Apache` leg returned **OpenEduCat's own
glossary pages in seven languages** and nothing else — one vendor's SEO surface occupying
10 of 10 result slots, the **twelfth** consecutive listicle. OpenEduCat remains **LGPLv3**
on an **LGPLv3** Odoo base; no permissive education ERP has been found in twelve attempts.

**Pass 364 · 2026-10-21.** Real, deployed systems that an engagement can extend, in the
sense that Odoo is extensible for ERP or OpenMRS for healthcare.

🔴 **`p364` generalises `p362`'s OnlineJudge finding across this whole shelf, and it is no
longer one platform's problem.** `p362` found that a platform's headline grant does not
govern the components that execute. `p364` read the README of **all 60 addresses on this
shelf**, extracted every GitHub address they name, and graded the grant of each one that
this base did not already hold.

| the question `ACTION ZZ-bo` asked | the answer, measured `2026-10-21` |
|---|---:|
| how many of this shelf's rows name a companion repository? | **25 of 60 (41.7 %)** — 60 live, 60 with a README, 0 unresolved |
| how many companion edges is that? | **91** — 46 `SAME-OWNER`, 45 `THIRD-PARTY` |
| how many were absent from a **2 550-address** corpus? | 🔴 **72 of 91 (79 %)**, i.e. **69 distinct repositories** |
| how many of those 69 are permissive? | **33** (16 MIT, 11 BSD, 6 Apache-2.0) |
| how many carry copyleft or worse? | **19** (12 AGPL-3.0, 3 GPL-3.0, 1 GPL-2.0, 2 LGPL-3.0, 1 Elastic) |
| how many carry **no grant at all**? | 🔴 **12** |

🔵 **The headline correction is `Marsha`, below** — published on this shelf as **MIT**
with copyleft reach **None**, and that cell is right about `openfun/marsha`'s own bytes and
incomplete about what a deployment of it reaches. **Evidence:**
[`companion-population`](../evidence/companion-population.2026-10-21-p364.tsv) ·
[`companion-grants`](../evidence/companion-grants.2026-10-21-p364.tsv) ·
[`version-axis-grant`](../evidence/version-axis-grant.2026-10-21-p364.tsv).

🔴 **`p362` changes this shelf's code-execution recommendation.** The judge tier's
permissive pick, `QingdaoU OnlineJudge`, **is still MIT** — but the components that
execute student code (`JudgeServer`, `Judger`) are **SATA**, not MIT, and the documented
deployment repository carries **no grant at all**. Measured component by component in
`repos/foundations.md`; the row-level corrections are in
[`grant-corrections`](../evidence/grant-corrections.2026-10-21-p362.tsv). All verified first-hand
**2026-10-21** (liveness + default branch via `git ls-remote --symref`, licence read
from payload). 🟢 Every address on this shelf was part of a **277-address corpus liveness
sweep: 277 live, 0 dead** — and, for the first time since `p355`, a **star
re-derivation**: the GitHub index is open through the session's MCP search tool, though
`api.github.com` still answers 403 by `curl`. See `agents/top.md`.

## 🔴 `p364`: the permissive headline with the copyleft deployment — and the version axis nobody here was reading

### The correction: `openfun/marsha`

🔴 **This shelf published `Marsha` as MIT with copyleft reach `None`.** The grant is real —
`openfun/marsha` is MIT in its own bytes. 🔴 **But its own organisation ships the piece that
makes it work inside Open edX, and that piece is AGPL-3.0:**

| component | relation | grant, read from payload `2026-10-21` | what it does |
|---|---|---|---|
| [`openfun/xblock-configurable-lti-consumer`](https://github.com/openfun/xblock-configurable-lti-consumer) | 🔴 `SAME-OWNER` | **AGPL-3.0** — `master/LICENSE`, **34 520 B** | the XBlock that injects Marsha's host-side JS into Open edX. Marsha's own README names it as the thing that "already does this" |
| [`davidjbradshaw/iframe-resizer`](https://github.com/davidjbradshaw/iframe-resizer) | `THIRD-PARTY` | 🔴 **GPL-3.0-or-commercial** at the default branch · 🟢 **MIT** at `v3.5.13` | resizes the LTI `<iframe>`; its host-side JS is copied into **the client's LMS pages** |

🔵 **This is `p362`'s class on a permissive headline, which is the direction that costs
more.** A GPL platform with a GPL component surprises nobody; **an MIT platform whose
documented deployment reaches AGPL-3.0 is exactly the row a studio forks into a closed
client deliverable.** The reach cell is corrected above; `openfun/marsha` itself is
unchanged and still MIT.

### 🆕 The new defect class: a grant is a function of the PIN, and every instrument here reads the BRANCH

🔴 **`p364`'s first draft of the row above was wrong, and the way it was wrong is the
finding.** Reading `iframe-resizer`'s default branch returns **GPL-3.0-or-commercial**
(*"Iframe Resizer Version 5 … dual-licensed, either under GPL V3, or a commercial
license"*). Published as-is, that asserts a GPL exposure in a client's LMS pages. 🟢 **It
is not true of the version Marsha uses.** Measured at the tag:

- `v3.5.13` → **MIT** (*"Copyright (c) 2013-2015"*) · `v3.6.6` → **MIT** (*"2013-2019"*)
- Marsha declares only **`@types/iframe-resizer` `3.5.13`** — DefinitelyTyped, **types
  only** — in `lib_video` and `lib_components`; **no `iframe-resizer` runtime dependency is
  declared in any of its five manifests.**

🔴 **So the real exposure is an UPGRADE, not a current breach**, and it is sharper than a
licence cell: the library relicensed **MIT → GPL-3.0-or-commercial at v5**, and the thing
that crosses into the client's estate is JS *injected into their LMS pages*. A studio that
runs `yarn copy-iframe-resizer` against a modern lockfile ships GPL-3.0 to a customer and
the platform's MIT cell will still read `None`.

🔴 **The general statement, and it applies to this entire base:** `gate-grant-path` parses
**299 grant claims** across these shelves and **every one of them asserts a BRANCH and a
file** — `main`, `master`, `develop`, `19.0`. 🔴 **Not one asserts a TAG.** A grant read at
a moving ref is a grant that can change under a client without any instrument here
noticing. 🟢 This fires **`ACTION VU`**'s payload shape — a `LICENSE` naming *two licences
and a date* — on a **second** row (the first was `snflwr-ai/snflwr.ai`, AGPL-3.0 →
proprietary on 2026-09-18), and VU's own note that *"no instrument here looks for that
shape"* still holds. Registered as `ACTION ZZ-br`.

### 🟢 The coverage this bought: JupyterHub's deployment tier, 11 components, all BSD

🟢 **The cheapest good news on this shelf.** JupyterHub is the platform a CS or
data-science engagement actually stands up, and **a class cluster is never just
`jupyterhub`** — it is a spawner plus an authenticator. All **11** named same-owner
components read **BSD** from payload, **none** was in this base's 2 550 addresses, and they
are now shelved in `repos/foundations.md`. 🔵 A BSD core with a BSD deployment tier is the
only row on this shelf where *"fork freely into a closed client deliverable"* survives
contact with the deployment.

### 🔴 The ungranted tier: 12 of 69 companions carry no grant at any probed path

🔴 **`p362`'s `OnlineJudgeDeploy` was not a one-off.** The same shape — the repository that
*deploys* or *localises* a platform, ungranted — recurs:

| companion | named by | what it is | grant |
|---|---|---|---|
| [`sakaicontrib/legacy-language-packs`](https://github.com/sakaicontrib/legacy-language-packs) | `sakaiproject/sakai` | Sakai's own language packs — **content a deployment ships** | 🔴 **no payload** |
| [`batlez/hiddenvm`](https://github.com/batlez/hiddenvm) | `Batlez/CloakBox` | same-owner companion of a shelf row | 🔴 **no payload** |
| [`muzea/hustoj-benchmark`](https://github.com/muzea/hustoj-benchmark) | `zhblue/hustoj` | benchmark harness for the judge | 🔴 **no payload** |

🔵 **`bigbluebutton/bbb-install` is the counter-example that makes the point fair:** it is
the deploy repository of an LGPL-3.0 platform and it **is** granted, **LGPL-3.0**, read
from payload. The ungranted-deploy shape is common, not universal, and it has to be
measured per row rather than assumed either way.

### 🟡 What the relation column cannot tell you yet

🔴 **`judge0/judge0`'s README names 20 third-party repositories and almost none of them is
a component** — they are an **adopter showcase**, projects that *use* Judge0. The
`THIRD-PARTY` relation correctly refused to promote any of them to a component, which is
what it is for. 🔴 **But the edge has no DIRECTION**, so a dependency and a dependent look
identical to this instrument, and the one genuine dependency hiding in that list is
[`ioi/isolate`](https://github.com/ioi/isolate) — **GPL-2.0**, Judge0's actual sandbox.
🟡 Registered as `ACTION ZZ-bs`; the cheap first cut is the manifest, which is how the
`iframe-resizer` reading above was settled.

---

## 🟢 `p361`: this shelf's most expensive finding is now properly qualified, not cracked

🔴 **`p357` published *there is no permissive education ERP*. `p358` cracked it with
`Moha-abshir/SMS` — and `p359` then had to warn that the crack was worthless**, because
that address is stock MIT on an organisation account with **four commits** behind it. The
shelf's answer was a new column: *a permissive grant with no software behind it is not a
platform.*

🟢 **`p361` found the row that actually settles it, and it was invisible to every prose
search this base has run.** [`academico-sis/academico`](https://github.com/academico-sis/academico)
— **MIT**, read from `main/LICENSE` — is a Laravel + Filament school-management and
student-information platform at **408 ★ and 151 forks**, with 🟢 **139 commits in 2026
and its last commit the day before this pass**. Measured first-hand on the commit
channel, not from a badge.

🔵 **So the finding becomes precise rather than refuted.** The shelf's platform rows
split three ways now, and the distinction is what decides an engagement:

| Shape | Example | What it means for a deliverable |
|---|---|---|
| 🔴 Copyleft platform, real software | Moodle, Open edX, Canvas | Reach it over LTI/MCP; never fork |
| 🟡 Permissive grant, **no software** | `Moha-abshir/SMS` (4 commits) | 🔴 Not a platform. The grant is free and buys nothing |
| 🟢 **Permissive grant, real software** | 🆕 **`academico-sis/academico`** (139 commits in 2026), Kolibri, OpenOLAT, Moodle App | 🟢 Fork freely into a closed client deliverable |

🔴 **What it does not do is make the LMS tier permissive.** Academico is
*administration* — enrolments, courses, attendance, invoicing — not a VLE. For teaching
and learning, OpenOLAT remains the only full-featured permissive platform on this shelf,
and everything else of scale is GPL or AGPL.

## 🔴 `p361` corrects the learning-record line on this shelf

🔴 This file's interoperability note read **`jeffyding/OpenLRW` (ECL-2.0 — schema only,
dead since 2018)**. 🟢 **That address is a 0 ★ fork.** The canonical is
[`Apereo-Learning-Analytics-Initiative/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW)
at **62 ★**, same ECL-2.0 grant, last commit **2020-02-06**. 🟡 **Still schema and not a
dependency — but the right address, and six years stale rather than eight.**

The column that decides engagement shape is **Licence reach**: whether AI added on
top can stay in a closed client deliverable, or whether the copyleft of the host
platform reaches it.
---

## 🔵 `p363`: no new platform, and the ERP/SIS absence restated rather than quietly dropped

🟢 **`p363` ran a platform leg and it returned nothing shelvable — recorded here because
an unstated null reads exactly like coverage.** The query
`open source platform education ERP CRM SIS MIT Apache` surfaced
**OpenEduCat (LGPL-3.0)**, **openSIS (GPL)**, **RosarioSIS**, **Frappe Education** and
**ERPNext Education** — 🔵 **every one of them already on this shelf, and not one of them
permissive.** The strongest-worded vendor pages in this sector advertise "open source"
for **LGPL and GPL** products.

🔴 **So `p357`'s absence stands, with `p361`'s qualifier intact: there is still no
verified *permissive* education ERP.** The distinction that keeps it defensible is
**ERP vs SIS** — [`academico-sis/academico`](https://github.com/academico-sis/academico)
is school-management/SIS, which is why it does not refute the sentence.

🟡 **The consequence for an engagement is unchanged and worth repeating in a deck:** the
administrative tier of education is **copyleft by default**. Reach it the way `p359`
recommended for Moodle plugins — **as a plugin inside the client's existing GPL estate**,
never vendored into a studio deliverable. The AI layer Globant builds stays on the
permissive side of the boundary and talks to the ERP over its API.

## Core platforms

| Platform | Repo | Licence | Licence reach for AI built on top | Where it fits |
|---|---|---|---|---|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 (`COPYING.txt`) | 🟡 A **plugin** is a derivative work → GPL-3.0. An **external agent** talking over web services / LTI stays separate | The default K-12 and HE LMS worldwide. Largest installed base; plugin API is the integration surface |
| **Open edX** | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 🔴 AGPL — network use triggers source obligations. Extend via **XBlock** or stay out-of-process | Large-scale HE, MOOCs, corporate academies. Deploy with [tutor](https://github.com/overhangio/tutor) |
| **Canvas LMS** | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 🔴 AGPL. Build as an **LTI 1.3 tool**, not a fork | Dominant HE LMS in North America. 🟡 The public mirror last pushed **2026-04-30** — ~6 months stale; treat GitHub as reference, not upstream |
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 🟢 **None.** Fork freely into closed deliverables | Offline-first. The right base for low-connectivity deployments — rural LATAM, Sub-Saharan Africa, remote APAC |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 🟢 **None** | Swiss-built HE LMS. The only full-featured *permissive* HE platform on this shelf |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 🟡 Plugin = derivative | Accessibility- and ease-of-use-focused. Strong Spanish/French-language support; real LATAM and EMEA public-sector deployments |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 🟢 **Permissive** (Apache-2.0 derivative with an education patent clause) | Research-university collaboration + learning environment |
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 (`license.txt`) | 🔴 AGPL | Modern LMS on the Frappe framework — pairs with ERPNext for an institution-wide stack (India-origin) |
| **ClassroomIO** | [classroomio/classroomio](https://github.com/classroomio/classroomio) | AGPL-3.0 | 🔴 AGPL | Customer/partner training academies for SaaS companies — the corporate-learning vertical |
| **ELMS Learning Network** | [elmsln/elmsln](https://github.com/elmsln/elmsln) | GPL-3.0 (`LICENSE.md`) | 🟡 Plugin = derivative | Distributed course-delivery ecosystem (Penn State origin) |
| **Moodle App** | [moodlehq/moodleapp](https://github.com/moodlehq/moodleapp) | 🟢 **Apache-2.0** (`COPYING.txt`) | 🟢 **None** | The official mobile client — **permissive while core is GPL-3.0**. White-labelled branded learner apps are a clean, licence-safe deliverable |

## 🆕 National school portals — the ENT tier, `p360`

🟢 **This shelf's premise is Odoo-for-ERP or OpenMRS-for-healthcare: a real, deployed
system an engagement extends rather than builds.** France's **ENT** (*Espace Numérique de
Travail*) is that, for school administration and the parent/pupil/teacher portal, and it
had no row here for 359 passes.

| Platform | Repo | Licence | Licence reach | Where it fits |
| --- | --- | --- | --- | --- |
| **entcore** — ENT kernel | [edificeio/entcore](https://github.com/edificeio/entcore) | 🟡 **AGPL-3.0** (`master/LICENSE`, © Édifice) | 🔴 **Network copyleft reaches a fork.** 🟢 Does **not** reach a separate service that talks to its HTTP API | A **régional** school portal: identity, messaging, timetable, the statutory *cahier de textes*, attendance, the competency record. Both *premier* and *second degré* from one core |
| Cahier de textes module | [OPEN-ENT-NG/cahier-de-textes](https://github.com/OPEN-ENT-NG/cahier-de-textes) | 🟡 AGPL-3.0 (`dev/LICENSE`) | 🔴 as above | The statutory lesson log — per-session lessons, homework, attachments, annual archival |
| Présences module | [OPEN-ENT-NG/presences](https://github.com/OPEN-ENT-NG/presences) | 🟡 AGPL-3.0 (🔴 `dev/LICENCE`) | 🔴 as above | Attendance and absence workflow |
| Compétences module | [OPEN-ENT-NG/competences](https://github.com/OPEN-ENT-NG/competences) | 🟡 AGPL-3.0 (🔴 `dev/LICENCE`) | 🔴 as above | Competency-based assessment — the *livret scolaire* data model |
| Exercizer module | [open-ent/exercizer](https://github.com/open-ent/exercizer) | 🟡 AGPL-3.0 (🔴 `master/LICENCE`) | 🔴 as above | Interactive exercises — MCQ, cloze, ordering; auto- and/or hand-marked |

🟢 **Deployment evidence, which is what this shelf exists to require.** Unlike the single-
author rows this shelf has had to warn about, the ENT stack has procurement behind it:

| Claim | Figure | Source quality |
|---|---|---|
| **ONE & NEO**, Hauts-de-France (Édifice) | **2.7 M users**, **5 790 institutions**, **>1 M daily connections**; contract renewed 2023 for four years | 🟡 Vendor self-reported (Édifice reference page) |
| **OpenENT** (CGI's ENT build) | **2 M pupils and students**, **1 700+ schools** | 🟡 Vendor self-reported, undated page (c. 2020) |
| ENT coverage, French public **primary** schools | 🔴 **62 %** | 🟢 IGÉSR inspectorate report, 15 Jul 2025, via Banque des Territoires |
| Fragmentation | 🔴 a family with children in école, collège and lycée can face **three different ENT solutions**; the report recommends territorial harmonisation and ÉduConnect | 🟢 Same IGÉSR report |

🟢 **That last pair is the engagement thesis, and it is an EMEA one.** A platform with
millions of users per région, a statutory data model, **62 % primary coverage** and a
government inspectorate asking for harmonisation is an integration and migration market,
not a greenfield one. 🔴 **It is also AGPL-3.0**, so the shape is a service beside the
portal, not a fork of it — see `compose/patterns.md`.

🟡 **Two cautions this shelf is the right place for.** The `entcore` README specifies
**JSE 7** and a clone URL on a decommissioned host while the code took a commit on
**2026-10-20** — price discovery from the tree, not the docs. And of four `entcore`
addresses, 🟢 `edificeio/entcore` is canonical, `opendigitaleducation/entcore` is **the
same repository** (identical 158-ref list), `OPEN-ENT-NG/entcore` is a single-branch
mirror one commit behind, and 🔴 `open-ent/entcore` is **five months stale**.

## Administration — SIS and ERP

| Platform | Repo | Licence | Licence reach | Where it fits |
|---|---|---|---|---|
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 (branch `19.0`) | 🟡 LGPL — dynamic linking stays separate; a fork does not | Education ERP on **Odoo**: admissions, fees, timetabling, library, hostel. The Odoo module ecosystem comes with it. This is the education analogue of "Odoo for ERP" |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 (branch `mobile`) | 🟡 Module = derivative | K-12 student information system: enrolment, grades, attendance, scheduling, billing. Multilingual with strong Spanish/Portuguese support — practical for LATAM public-sector K-12 |
| **Learner Credential Wallet** | [openwallet-foundation-labs/learner-credential-wallet](https://github.com/openwallet-foundation-labs/learner-credential-wallet) | 🟢 **MIT** | 🟢 **None** | Verifiable credentials / digital diplomas under OpenWallet Foundation. The build target for skills-based hiring work |
| 🆕 **openSIS Classic** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | GPL-2.0 (🔴 `docs/License.txt`) | 🟡 Module = derivative. **GPL-2.0, not 3.0** — do not assume GPL-3.0 compatibility | K-12 SIS with parent and teacher portals, gradebook, report cards and transcripts. The second mature K-12 SIS on this shelf alongside RosarioSIS, and a genuine alternative when a client needs portals rather than Spanish localisation |
| 🆕 **FenixEdu Academic** | [FenixEdu/fenixedu-academic](https://github.com/FenixEdu/fenixedu-academic) | LGPL-3.0 | 🟡 LGPL — dynamic linking stays separate | **Higher-education** SIS from Instituto Superior Técnico, Lisbon: curricular plans, enrolment, degrees, theses. The HE counterpart to the two K-12 systems above, and the only European university SIS on this shelf |
| 🆕 🟢 **Academico** | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** (`main/LICENSE`) | 🟢 **None.** Fork into a closed deliverable | Laravel + Filament school management for small and medium institutions. 🟢 **408 ★, 151 forks, 139 commits in 2026, last commit 2026-10-20** — the first permissive education-administration platform on this shelf with real software behind it |
| 🆕 **ERPNext** | [frappe/erpnext](https://github.com/frappe/erpnext) | **GPL-3.0** (🔴 `develop/license.txt`) | 🔴 **GPL-3.0 — strongest copyleft on this tier.** A custom app is a derivative; reach it over its **REST API**, not as a Frappe app | Full institution-wide ERP — finance, HR, procurement, assets — with an education module. Pairs with [`frappe/lms`](https://github.com/frappe/lms) for a single-vendor teaching-plus-administration stack. India-origin |
| 🆕 **School Management System (SMS)** | [Moha-abshir/SMS](https://github.com/Moha-abshir/SMS) | 🟢 **MIT** (`main/LICENSE`, holder *Mohamed Abshir*, 2026) | 🟢 **None.** Fork into a closed deliverable | 🟢 **The first permissive administration row on this shelf.** Multi-role school management built for **Kenya's Competency-Based Curriculum (CBC)**: TypeScript 5.3, React 18, Node 20, Drizzle ORM, PostgreSQL 16, Tailwind. 🟡 Single-author and young — read the qualification below before it displaces `openeducat_erp` in a proposal |

### 🟡 `p358`: there is now **one** permissive administration row, and it does not change the recommendation

🟢 **`Moha-abshir/SMS` is real, live, and genuinely MIT** — holder *Mohamed Abshir*,
2026, read from `main/LICENSE`. It is a multi-role school management system built
against **Kenya's CBC**, on a current stack (TypeScript/React/Node/Drizzle/PostgreSQL).
🟢 On the closed region vocabulary it is **EMEA**, and with `elimu-mcp` it gives that
region its first African rows anywhere on this base.

🔴 **A correction to this pass's own source before the row is used.** The search leg that
surfaced it described a *"Flask + SQLite web app, Tkinter desktop app, Android app,
M-Pesa payments, bilingual SMS, report card PDFs"* with 240 tests. 🟢 **Read first-hand,
the README describes none of that** — no Flask, no Tkinter, no M-Pesa. The snippet had
conflated this repository with a different Kenyan school-ERP project in the same leg.
🔵 The lesson is the one this base keeps relearning: **a snippet describes a repository
it has not opened**, and the payload is the only channel that settles it. Nothing was
published from the snippet; the row above states only what the README states.

🟡 **And it does not displace `openeducat_erp`.** The honest comparison:

| | `openeducat_erp` | `Moha-abshir/SMS` |
|---|---|---|
| Licence | LGPL-3.0 | 🟢 **MIT** |
| Scope | admissions, fees, timetabling, library, hostel, **plus the whole Odoo module ecosystem** | school management for one national curriculum |
| Maturity | a vendor-backed product on Odoo | 🔴 **single author, 2026, no deployment evidence found** |
| Fork into a closed deliverable | 🟡 LGPL reaches a fork | 🟢 **yes** |

🟢 **So the guidance splits rather than flips.** For an institution-wide ERP,
`openeducat_erp` remains the recommendation and `p357`'s "price it as a build" still
holds — one young single-author system is not an ERP. 🟢 For a **narrow, K-12,
school-administration deliverable that must stay closed**, `Moha-abshir/SMS` is now the
first base on this shelf that permits it, and a Kenyan or East African engagement gets
the curriculum alignment for free. 🔵 Registered as **`ACTION ZZ-bh`**: re-probe this row
next pass for commit activity and contributor count before any proposal rests on it.

### 🔴 `p357`: there is no permissive education ERP — the finding this pass qualifies

🟢 **Every row on this tier is copyleft** — LGPL-3.0, GPL-2.0, GPL-3.0 — and the one
permissive row (Learner Credential Wallet) is a credential wallet, not an
administration system. `p357` ran a leg specifically to break that, because a
permissive education ERP would be the most valuable address on this shelf: it would let
a studio **fork** an admin system into a closed deliverable instead of building one.

🔴 **All three candidates the leg returned are unusable, and none for a licence
reason:** `foradian/fedena` (claimed Apache-2.0) is live and serves **nothing** at any
standard path; `gegok12/gegok12` (claimed MIT) **does not exist**; and
`schooltool/schooltool` is dead. See `repos/foundations.md` for the probe detail.

🟢 **So the engagement guidance is settled rather than pending**, and it is the opposite
of a gap:

1. **Closed admin deliverable → it is a build.** Price it as one. There is no
   permissive base to fork, and a successor meeting the Fedena or GegoK12 claim in a
   roundup should read this paragraph before costing a fork.
2. **Can accept copyleft on the admin tier → `openeducat_erp` (LGPL-3.0)** remains the
   recommendation, because LGPL permits dynamic linking: AI modules can stay separate
   works. It is also the closest true analogue to "Odoo for ERP" — it *is* Odoo.
3. **Already on Frappe → reach ERPNext over its REST API.** GPL-3.0 reaches a Frappe
   app; it does not reach a separate service calling the API.

## Content, media and delivery

| Platform | Repo | Licence | Licence reach | Where it fits |
|---|---|---|---|---|
| **H5P** | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) · [h5p/h5p-cli](https://github.com/h5p/h5p-cli) | GPL-3.0 core / 🟢 **MIT** CLI | 🟢 Tooling on the **CLI** is unencumbered; code linked into the library is GPL | ~50 interactive content types that embed in Moodle, Canvas and Open edX. The fastest route to AI-generated interactive exercises inside an existing LMS |
| **Opencast** | [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** (branch `develop`) | 🟢 **Permissive** | Lecture capture, video pipeline, scheduled recording. The ingestion point for transcript- and video-based AI |
| **BigBlueButton** | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 (branch `v4.0.x-develop`) | 🟡 LGPL | Virtual classroom with whiteboard, breakouts, recording. Integrates with Moodle and Canvas |
| 🔴 **Marsha** | [openfun/marsha](https://github.com/openfun/marsha) | 🟢 **MIT** (own bytes) | 🔴 **NOT "None" — see `p364` below.** Its own `openfun/xblock-configurable-lti-consumer` is **AGPL-3.0** (`master/LICENSE`, 34 520 B), and the documented build injects `iframe-resizer` JS **into the host LMS pages** | LTI learning-content management system from France Université Numérique — drop-in video/content provider for any LTI host |
| **Hyperbook** | [openpatch/hyperbook](https://github.com/openpatch/hyperbook) | 🟢 **MIT** | 🟢 **None** | Interactive teaching books from markdown. Good fit for AI-generated courseware that must stay editable by teachers |
| 🆕 **JupyterHub** | [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | 🟢 **BSD-3-Clause** | 🟢 **None — and `p364` is the first pass that can say so about the DEPLOYMENT and not just the core.** All **11** of its named same-owner components read **BSD** from payload | Multi-user notebooks for CS/data-science teaching. Pair with [ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) for LMS single sign-on. 🟢 The spawner/authenticator tier is now shelved in `repos/foundations.md` |

## Assessment and integrity

| Platform | Repo | Licence | Licence reach | Where it fits |
|---|---|---|---|---|
| **Judge0** | [judge0/judge0](https://github.com/judge0/judge0) | GPL-3.0 | 🟡 Use **as a service over its API** and the boundary holds | Sandboxed code execution in 60+ languages. The execution backend for any programming-assessment or coding-tutor build |
| **INGInious** | [INGInious/INGInious](https://github.com/INGInious/INGInious) | AGPL-3.0, *"most of the files"* | 🔴 AGPL, and 🟡 **mixed** — the grant text itself scopes to most, not all | Secure automated exercise assessment (UCLouvain). Mature grading platform |
| **Dolos** | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | 🟢 **MIT** | 🟢 **None** | Source-code plagiarism detection (Ghent). The integrity layer for AI-era programming courses — and newly relevant now that students submit agent-assisted code |
| **UDOIT** | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | GPL-3.0 | 🟡 Derivative if forked | Accessibility inspection of LMS course content. Directly serviceable against EU accessibility and US Section 508 obligations |
| **scorm-again** | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | 🟢 **None** | Modern SCORM 1.2 / 2004 JS runtime. The bridge for the enormous installed base of legacy SCORM corporate content |
| 🆕 **exam-proctor** | [shaheeranser/exam-proctor](https://github.com/shaheeranser/exam-proctor) | 🟢 **Apache-2.0** (`main/LICENSE`, read `p359`) | 🟢 **None** — 🔴 **but see the Art. 5 note: the binding constraint on this row is not its licence** | **An LTI 1.3 tool that launches from inside Moodle**, authors quizzes, guards the browser, passes grades back over AGS. Dockerised with MinIO + Caddy. 🟢 **The only proctoring row on this base that reaches the LMS over a protocol boundary.** 🔴 25 commits, **2 authors (`%ae`)** — `%an` reads 1, corrected `p362` — 2026-07-05 → 2026-10-11. 🔴 **`p190` read its source: head pose, iris deviation and `face-api` identity checks — GDPR Art. 9, and clear of the Art. 5 prohibition by one unset default** |
| 🆕 **openproct** | [OpenProct/openproct](https://github.com/OpenProct/openproct) | 🟢 MIT | 🟢 None | 🔴 **Not a platform — 4 commits, 2 authors (`%ae`), all on 2025-10-26, nothing since.** Listed only so a successor who finds "MIT, organisation account, privacy-first proctoring" does not stop here |

### 🟡 `p359`: the permissive proctoring row that is *architecturally* different — and `Gap 344`'s survivor is still the right worry

🔵 **State the record first, because the cheap version of this finding is already
refuted.** `Gap 344` once claimed the proctoring tier had **zero permissive rows**;
`P131-D` refuted that with four MIT addresses and recorded that **the gap survives as a
maturity gap, not a licence gap** — largest 18 ★, all individually owned, none
institution-backed. 🟢 **That framing still holds, and `p359` does not disturb it.**

🟢 **What [`shaheeranser/exam-proctor`](https://github.com/shaheeranser/exam-proctor)
adds is architecture, and `p359` adds its grant.** It is the only proctoring address on
this base that is an **LTI 1.3 tool**: it launches from inside Moodle — a GPL-3.0 host —
across the protocol boundary, authors quizzes in the tool, and passes grades back over
AGS. 🔵 Compare the two first-party alternatives: `openedx/edx-proctoring` and
`eLearning-BS23/moodle-quizaccess_proctoring` are **both AGPL plugins inside AGPL/GPL
hosts** — correct for the host, wrong for a studio deliverable. The four MIT rows
`P131-D` found are standalone web apps that do not reach a client's LMS at all.

🟢 **`p359`'s contribution to this row is the licence and the placement, and nothing
else about it is new to this base.** Its grant was never published here: **Apache-2.0,
read from `main/LICENSE` this pass.** Commit channel: 25 commits, **2 authors (`%ae`)** — corrected `p362`; `%an` reads 1 — `+0800`
and `+0500`, 2026-07-05 → 2026-10-11 → **APAC**.

### 🔴 And the reason this row was read before and never shelved — which is the thing to quote, not the licence

🔴 **`p190` read this repository's source at a pinned `HEAD` and found head pose
(yaw/pitch), iris deviation and a `face-api` **identity consistency** check.** Its
verdict, carried in `compose/code/p190-affect-inference-scan/`:

- 🔴 **GDPR Art. 9.** Biometric identity checking is special-category processing. A
  lawful basis under Art. 9(2) is required before a single frame is captured, and
  "legitimate interests" is not one of them.
- 🔴 **Clear of the EU AI Act Art. 5(1)(f) prohibition by one unset default.** MediaPipe's
  `outputFaceBlendshapes` is not set, and it defaults to `false`. 🔴 **Setting that one
  line moves the deliverable from a `2027-12-02` Annex III duty into a LIVE prohibition
  at EUR 35 M or 7 % of worldwide turnover.**
- 🔴 **Both face models are fetched at runtime** from `cdn.jsdelivr.net` and
  `storage.googleapis.com` — so the model can change without the repository changing, and
  no source review of the repo can see that.

🟢 **So the recommendation is precise rather than enthusiastic.** `exam-proctor` is the
**reference architecture** for LMS-integrated invigilation — read its LTI wiring, its AGS
grade passback and its Docker topology. 🔴 **It is not a row to deploy into an EU
engagement as it stands**, and the reason is a config default and a CDN fetch, not its
Apache-2.0 grant. 🔵 Pattern 12 on `compose/patterns.md` already holds the
process-evidence alternative for exactly this situation.

🔴 **Read the integrity recommendation with all of it, because it has not changed.**
Proctoring surveils the student; `dodona-edu/dolos` (MIT, Ghent University — 🟢 the one
institution-backed integrity row) inspects what the submission *is*. 🟢 **`dolos` remains
the first recommendation.** 🔵 And per §16 of `intel/trends.md`, invigilation is a
requirement the detection market's own customers are increasingly withdrawing.

## 🆕 Code-execution and online-judge platforms

🟢 **New section, `p356`.** Last pass this shelf had exactly one way to run student
code — `judge0`, GPL-3.0, over its API. There are at least fifteen, and **the largest
permissive one is bigger than the copyleft one everybody reaches for first.**

| Platform | Repo | Licence | Licence reach | Where it fits |
|---|---|---|---|---|
| **QingdaoU OnlineJudge** | [QingdaoU/OnlineJudge](https://github.com/QingdaoU/OnlineJudge) | 🟢 **MIT** (1 085 B, re-read `p362`) | 🟢 **None on the web tier.** Fork it into a closed deliverable | **Still the recommendation for the platform**, at 6 552 ★ — Django backend plus the MIT `OnlineJudgeFE`. 🔴 **But its execution path is not MIT:** `JudgeServer` and `Judger` are SATA and `OnlineJudgeDeploy` is ungranted, so a closed deliverable that must *run code* has to decide about those three separately |
| **QingdaoU Judger** | [QingdaoU/Judger](https://github.com/QingdaoU/Judger) | 🔴 **SATA — not MIT, not OSI** (branch `newnew`, 1 823 B), corrected `p362` | 🟡 **Obligations, not copyleft:** star the project, thank the authors, keep its copyright block intact | The seccomp execution sandbox alone. 🔴 **Its grant was never MIT** — the cell inherited it from the sibling `OnlineJudge`. Usable if the client accepts a non-OSI notice; fails a *"permissive only"* procurement rule |
| **Judge0** | [judge0/judge0](https://github.com/judge0/judge0) | GPL-3.0 | 🟡 Service over HTTP keeps the boundary | 60+ languages behind a REST API. Still the fastest thing to stand up; the licence is the cost |
| **Hydro** | [hydro-dev/Hydro](https://github.com/hydro-dev/Hydro) | AGPL-3.0 | 🔴 AGPL — network use triggers source obligations | Multi-tenant, high-performance, plugin architecture. The right base for an institution running many courses and contests — if the client can accept AGPL |
| **DMOJ** | [DMOJ/online-judge](https://github.com/DMOJ/online-judge) · [DMOJ/judge-server](https://github.com/DMOJ/judge-server) | AGPL-3.0 | 🔴 AGPL | Django contest platform plus a separate judging backend. Clean split between web tier and executor |
| **Sharif Judge** | [mjnaderi/Sharif-Judge](https://github.com/mjnaderi/Sharif-Judge) | **GPL-3.0** (branch `Version-1`, 35 146 B), corrected `p362` from AGPL-3.0 | 🟡 **GPL, not AGPL** — derivative obligations on distribution, 🟢 **no network clause** | 🟢 **Built for COURSES, not contests** — assignments, deadlines, per-student feedback. Closest in shape to what a university client actually asks for, and 🟢 **the correction widens what may be done with it**: a studio MAY host it as a service without triggering source obligations |
| **Otter-Grader** | [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** | 🟢 **None** | Autogrades **Python and R notebooks**, with containerised execution and LMS export. Pairs with JupyterHub for data-science teaching |
| **HUSTOJ** | [zhblue/hustoj](https://github.com/zhblue/hustoj) | GPL-2.0 | 🟡 Derivative if forked | The long-running PHP/C++ judge; very low deployment footprint |

🔵 **Pick on the licence, then on the shape — and `p362` changes two of the three
sentences this paragraph used to carry.** For a closed client deliverable the platform is
still **QingdaoU OnlineJudge (MIT)**; 🔴 **"Judger (MIT) inside your own platform" is
withdrawn** — the sandbox is SATA, so dropping it into a closed deliverable ships a
non-OSI notice obligation rather than a permissive component. For an institution that
will run it themselves and publish nothing, Hydro's plugin architecture is the better
engineering. For a *course* rather than a contest, Sharif Judge is the only row built for
it — 🟢 **and it is GPL-3.0, not AGPL-3.0**, so unlike the AGPL rows a studio may also
**host it as a service**; distributing a modified build is still what triggers the
obligation. Wired end-to-end in `compose/patterns.md` Pattern 9.

🟢 **The genuinely permissive execution options, after this pass:** `judge0` over its API
(GPL-3.0, boundary-kept), [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader)
(BSD-3-Clause, notebooks), and 🆕 [`XiaoCow666/CodeSense`](https://github.com/XiaoCow666/CodeSense)
(**MIT**, 554 commits, 7 authors (`%ae`), code evaluation + restricted execution +
learning analytics, APAC/China) — 🔴 the last at **4 ★**, so it is a credible base to
build on and not a thing to cite as proven in production.

---

## 🔴 Platforms to exclude, and why

| Platform | Repo | Why excluded |
|---|---|---|
| Advising App | [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) | 🔴 **Elastic License 2.0** — source-available, not OSI. Globant **cannot offer it as a managed or hosted service**. Capable AI student-advising product; wrong licence for studio delivery |
| Caliper spec | [1EdTech/caliper-spec](https://github.com/1EdTech/caliper-spec) | 🔴 **IMS specification document licence** — not software. Implement the standard; do not vendor the document |
| cn-math-taxonomy | [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) | 🔴 **CC-BY-NC-4.0** — NonCommercial. Excellent China K-12 curriculum graph, unusable in paid engagements |
| 🆕 CBIT-AiExam-plus | [reneverland/CBIT-AiExam-plus](https://github.com/reneverland/CBIT-AiExam-plus) | 🔴 **No grant at all.** The README carries an MIT badge; the `LICENSE` it links to **404s**, as do four other rungs. The most complete AI examination platform found this pass and it is all-rights-reserved until its author adds a file |
| 🆕 MathCyclus (Lingxi) | [JinLingxi/MathCyclus---Lingxi-Question-Bank-Assistant](https://github.com/JinLingxi/MathCyclus---Lingxi-Question-Bank-Assistant) | 🔴 **Grant exists only as a prose sentence in the README.** A claim, not a licence file — cheap for the author to fix and not safe to assume |
| 🆕 Anti-proctoring tooling | [`Batlez/CloakBox`](https://github.com/Batlez/CloakBox) · `SunnyCOdet/ofradr` | 🔴 **Not education software.** Both are high-starred results in the `proctoring` leg and both exist to **defeat** exam monitoring. Named here so a successor running that leg does not mistake them for supply |
| 🆕 ElewaSTEM | [ondinookello96/elewastem](https://github.com/ondinookello96/elewastem) | 🔴 **No grant at any probed path.** Offline-first multilingual AI STEM tutor targeting **16+ African languages** — the most interesting *shape* in the Africa leg and legally untouchable. Hackathon-origin, so its capability claims are also unverified |
| 🆕 AI-CONNECT-AFRICA | [EccentricIvan/AI-CONNECT-AFRICA](https://github.com/EccentricIvan/AI-CONNECT-AFRICA) | 🔴 **No grant at any probed path.** Fully on-device learning platform (bundled Gemma 3 1B) for schools with no connectivity; updates ship by **USB drive or school LAN**. 🔵 Named because its *architecture* answers a real constraint this shelf cares about — see `Kolibri` (MIT) for the same constraint with a licence |
| 🆕 nemia-escolar | [helmerpersonal-escuela/nemia-escolar](https://github.com/helmerpersonal-escuela/nemia-escolar) | 🔴 **No grant at any probed path.** Mexican school platform aligned to the **Nueva Escuela Mexicana** — planning, assessment, family communication. One of ten unlicensed LATAM addresses this pass measured; see `agents/top.md` |
| 🆕 educational-assessment-ai-agent-platform | [mthatipamula/educational-assessment-ai-agent-platform](https://github.com/mthatipamula/educational-assessment-ai-agent-platform) | 🔴 **No grant at any probed path.** The most complete K-12 assessment architecture found this pass — RAG item authoring with self-review, rubric scoring with human review, sandboxed code grading, evals and observability. 🔵 Read it as a reference design; none of it can be used |

## 🟢 The permissive shortlist

When a client needs AI inside a closed deliverable, these are the platforms whose
licences do not reach it:

**Platforms:** OpenOLAT (Apache-2.0) · Kolibri (MIT) · Sakai (ECL-2.0) ·
Moodle App (Apache-2.0)
**Interop:** scorm-again · ltijs · pylti1.3 · CACCL · Marsha · ltiauthenticator (all MIT/Apache/BSD)
**Content:** H5P CLI · Hyperbook · JupyterHub
**Assessment:** Dolos · Ares2 · 🆕 **QingdaoU OnlineJudge** (🟡 **web tier only** —
🔴 `QingdaoU/Judger` and `QingdaoU/JudgeServer` **removed from this shortlist `p362`:
SATA, not MIT**; `QingdaoU/OnlineJudgeDeploy` has no grant) · 🆕 **Otter-Grader** ·
🆕 **XiaoCow666/CodeSense** (MIT, `p362` — the permissive execution row) ·
🆕 **shaheeranser/exam-proctor** (Apache-2.0 — 🟢 LTI 1.3, the only proctoring row that
stays outside the host's copyleft; 🔴 **reference architecture only** — GDPR Art. 9, and
clear of the Art. 5 prohibition by one unset MediaPipe default)
**Learning records:** 🆕 **pelotech/xapi-lrs** · 🆕 **yetanalytics/lrsql** ·
🆕 **adlnet/ADL_LRS** · 🆕 **Larissa** (all Apache-2.0) · 🆕 **DavidLMS/learnmcp-xapi**
(MIT) · 🆕 **Apereo-Learning-Analytics-Initiative/OpenLRW** (ECL-2.0, 62 ★ — 🔴 **schema only, last commit 2020-02-06**; `p359`'s `jeffyding/OpenLRW` was a 0 ★ fork, corrected `p361`)
**Psychometrics:** 🆕 **joakimwallmark/irtorch** (MIT, 🟢 live) · 🆕 **eribean/girth**,
🆕 **girth_mcmc**, 🆕 **variational-IRT** (MIT, 🔴 all stale ≥4 years)
**Special education:** 🆕 **dg13788/iep-system** (MIT) — 🔴 **one permissive row out of
seven addresses measured; see `agents/top.md` §Special education before quoting this
tier to a client**
**Scheduling and tutor memory:** 🆕 py-fsrs · 🆕 fsrs4anki · 🆕 FSRS (algorithm) ·
🆕 **tura-learn/Dhee** (MIT, `p362` — memory built for tutor agents, 198 commits, APAC/India)
**Pedagogy skill packs:** 🆕 **nuwa-skills/montessori-skill** (MIT, `p362`, 72 ★ — 🟢 the
first *permissive* one on this base, 🔴 and only 5 files; `education-agent-skills` has 165
and is `CC-BY-SA-4.0`)
**Credentials:** Learner Credential Wallet
**Curriculum data:** 🆕 **oak-curriculum-ontology** (OGL-3.0 data + MIT code — 🟢 the
only curriculum asset on this base with commercial use and **no** share-alike)
**LMS connectors:** **bruchris/canvas-lms-mcp** · **G36maid/moodle-mcp** ·
**AnonymousOnyx22/canvas-lms-student-mcp** · falkenslab/moodle-mcp ·
🆕 **Yuanpeng-Li/gradescope-mcp** · 🆕 **hughsibbele/Canvas-Agent** ·
🆕 **gabrielmahia/elimu-mcp** (Kenya — 🟡 read its DEMO-data caveat) (all MIT)
**LTI 1.3 libraries:** 🆕 **iamlucasb/lti-core** (TypeScript) · 🆕 **DecoyLex/ltix**
(Elixir) · ltijs · pylti1.3 · CACCL — 🔴 **never** `oat-sa/lib-lti1p3-deep-linking`
(GPL-2.0) or `GSU-CETLOE/lti1p3Library-php` (MIT with no licensor named)
**School administration:** 🆕 **Moha-abshir/SMS** (MIT — 🟡 single-author, Kenya CBC)
**LATAM:** 🆕 **LabSirius/TutorIA** (MIT, Colombia, inside Open edX) ·
🆕 **Riskbreaker2077/open-test** (MIT, offline LAN assessment)
**Lecture capture:** 🆕 **LectureLab** (MIT) · 🟡 the MIT *engines* inside Cap and
CaptureFlow — never their AGPL applications

🟡 **One row on this shortlist is now a school-administration system** —
`Moha-abshir/SMS`, added `p358`. 🔴 **Nothing on it is an institution-wide ERP**, and that
absence is measured, not unexamined — see the ERP note above for why the distinction
decides how a proposal is priced.

Everything else on this shelf is GPL/AGPL/LGPL and should be reached **over a
protocol boundary** — LTI 1.3, web services, or MCP — rather than forked. That
boundary choice is the single most consequential architectural decision in an
education engagement, and it is a licence decision before it is a technical one.
