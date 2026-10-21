---
industry: education
region: Global
updated: 2026-10-21
---

# Education — foundational repos

**Pass 362 · 2026-10-21.** The systems an education engagement starts *from*, rather
than the agents it adds on top. Every row verified first-hand **2026-10-21**: liveness
and default branch via `git ls-remote --symref`, licence **read from the payload**.

🔴 **`p362` corrects two grants in the code-execution tier, and both corrections change
what an engagement may do with the row.** [`QingdaoU/Judger`](https://github.com/QingdaoU/Judger)
is **not MIT** — its payload is the Star And Thank Author License — and
[`mjnaderi/Sharif-Judge`](https://github.com/mjnaderi/Sharif-Judge) is **GPL-3.0, not
AGPL-3.0**. 🔵 The first narrows what was published as permissive; the second *widens*
what was published as network copyleft. Full mechanism in `agents/top.md`; the sweep that
found the first is [`mit-body-sweep`](../evidence/mit-body-sweep.2026-10-21-p362.tsv) and
the corrections are in
[`grant-corrections`](../evidence/grant-corrections.2026-10-21-p362.tsv).

🟢 **Gate state `p362`:** `make hooks` ran — **28/32 green on arrival, 32/32 on exit**.
RED on arrival: `gate-absence`, `gate-shelf-consistency`, `gate-author-key`,
`gate-census-currency`.
🟢 **`gate-shelf-consistency`'s RED is what found the `Sharif-Judge` defect**: it reported
the slug carrying `AGPL-3.0` on `verticals/solutions.md` and `MIT` on this shelf, and both
cells turned out to be wrong in different ways — the `MIT` was an **adjacency** read of a
sentence about `QingdaoU/Judger`, and the `AGPL-3.0` was a real mis-grading of the
payload.

🟢 **`p361` is the first pass since `p355` with a working GitHub index, and it did not
arrive through `curl`.** `api.github.com` still answers **403** on every path; the
session's GitHub MCP search tool answers in full. 🔵 The five passes that recorded "no
index" were recording one transport. See `agents/top.md` for the full channel finding.

🟢 **Gates run before this pass wrote:**

| Gate | Result |
|---|---|
| Whole-corpus liveness (`ls-remote --symref`, 16-way parallel, 277 addresses) | 🟢 **277 of 277 live, 0 dead** |
| Star re-derivation (index, batched `repo:` queries) | 🟢 **273 of 277 measured at their published spelling; 78 blind cells filled; 89 published figures re-derive, 78 within ±2** |
| 🆕 **Archived sweep** (`archived:true fork:true`, all 277) | 🔴 **1 hit — and it was published on this shelf unflagged** |

🔴 **`p361` corrects two rows on this shelf, and both corrections come from the index
rather than from any channel this base already had.**

**1. `zmievsa/autograder` is archived.** Read-only upstream: no commits, issues or PRs
ever again. 🔴 **It answers `ls-remote` exactly like a healthy repository**, which is
precisely why 360 passes of liveness sweeps never caught it. Flagged in the autograding
table below.

**2. The OneRoster row was pointed at a fork, and the fork's death date was published as
the project's.** `p359` shelved [`jeffyding/OpenLRW`](https://github.com/jeffyding/OpenLRW)
as *"the only address that carries OneRoster"* and dated it **January 2018**. 🔴 **That
address is a fork** — `fork: true`, **0 ★**, created and last touched the same day,
2018-01-19. 🟢 **The canonical upstream is
[`Apereo-Learning-Analytics-Initiative/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW)
— 62 ★, 25 forks, different HEAD SHA, ECL-2.0 read from `master/LICENSE`.** 🔵 **This
base already held the same organisation's `Larissa` and still shelved a fork of its other
project**, because the fork was what a non-ranked search surfaced. Corrected below.

🟡 **The conclusion survives the correction, and that is worth saying plainly.** The
canonical's last commit is **2020-02-06**, not 2026 — two years later than the fork, and
still six years ago. 🔴 **So "read the schema, do not take the dependency" stands; the
*address* and the *date* were wrong, the *advice* was right.**

**Read the default-branch column.** Education infrastructure is old software. Of the
grants on this shelf, a large share live on `master`, `develop`, `release` or a
version branch — not `main`. A tool that assumes `main` will report a live,
correctly-licensed repository as grantless. That has happened on this base before, and
`p361` adds a fresh instance from a national curriculum body — Oak National Academy
spells its grant **`LICENCE`**, and `LICENSE` 404s (see `agents/top.md`).
---

## Learning platforms (LMS / VLE)

| Platform | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Open edX LMS + Studio | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | `master/LICENSE` | **8 205** | North America |
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | `main/COPYING.txt` — 🔴 no `LICENSE` file exists | **7 508** | Global |
| Canvas LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | `master/LICENSE` | **6 879** | North America |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | `develop/license.txt` — 🔴 (lower-case) | **3 329** | APAC |
| ClassroomIO | [classroomio/classroomio](https://github.com/classroomio/classroomio) | AGPL-3.0 | `main/LICENSE` | **1 726** | Global |
| Kolibri | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | `develop/LICENSE` | **1 159** | Global |
| Tutor (Open edX distro) | [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 | `release/LICENSE.txt` | **1 128** | Global |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | `master/LICENSE` | **1 016** | EMEA |
| Moodle App (mobile) | [moodlehq/moodleapp](https://github.com/moodlehq/moodleapp) | 🟢 **Apache-2.0** | 🔴 `main/COPYING.txt` | **1 002** | Global |
| Sakai | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | `master/LICENSE` | **1 239** | North America |
| OpenOLAT | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | `master/LICENSE` | **448** | EMEA |
| ELMS Learning Network | [elmsln/elmsln](https://github.com/elmsln/elmsln) | GPL-3.0 | `master/LICENSE.md` | **253** | North America |

🟢 **The two permissive platform rows matter disproportionately.** `OpenOLAT`
(Apache-2.0) and `kolibri` (MIT) are the only full platforms here that can be
embedded in a closed client deliverable without copyleft reach. And
`moodlehq/moodleapp` is **Apache-2.0 while Moodle core is GPL-3.0** — the mobile
client can be forked into proprietary work where the server cannot.

## 🆕 National school portals — the ENT tier, and the first platform family placed in EMEA by its own vendor's commit channel

🟢 **What this shelf was missing.** It carried the *interchange* layer in depth — LTI,
SCORM, xAPI, Caliper, LRS, OneRoster — and every platform row above is an LMS. A **school
portal** is a different system: identity, messaging, timetable, attendance, the statutory
lesson log and the competency record, procured by a region for every school in it. France
has standardised on one since 2003 and it is open source.

**ENT** — *Espace Numérique de Travail* — was launched by the Ministry of Education with
the Caisse des dépôts in 2003 and is procured per *région* and per *département*.
`entcore` is its modular kernel, and it implements both *premier degré* (primary) and
*second degré* (secondary) from the same core.

| System | Repo | Licence (read from payload) | Grant read at | Default ref | Region |
| --- | --- | --- | --- | --- | --- |
| **entcore** — ENT kernel | [edificeio/entcore](https://github.com/edificeio/entcore) | 🟡 **AGPL-3.0** | `master/LICENSE` | `master` | EMEA |
| Cahier de textes | [OPEN-ENT-NG/cahier-de-textes](https://github.com/OPEN-ENT-NG/cahier-de-textes) | 🟡 **AGPL-3.0** | `dev/LICENSE` | 🔴 `dev` | EMEA |
| Présences (attendance) | [OPEN-ENT-NG/presences](https://github.com/OPEN-ENT-NG/presences) | 🟡 **AGPL-3.0** | 🔴 `dev/LICENCE` | 🔴 `dev` | EMEA |
| Compétences (competency record) | [OPEN-ENT-NG/competences](https://github.com/OPEN-ENT-NG/competences) | 🟡 **AGPL-3.0** | 🔴 `dev/LICENCE` | 🔴 `dev` | EMEA |
| Exercizer (interactive exercises) | [open-ent/exercizer](https://github.com/open-ent/exercizer) | 🟡 **AGPL-3.0** | 🔴 `master/LICENCE` | `master` | EMEA |
| Blog module | [edificeio/blog](https://github.com/edificeio/blog) | 🟡 **AGPL-3.0** | `develop/LICENSE` | 🔴 `develop` | EMEA |
| Mindmap module | [OPEN-ENT-NG/mindmap](https://github.com/OPEN-ENT-NG/mindmap) | 🟡 **AGPL-3.0** | `develop/LICENSE` | 🔴 `develop` | EMEA |

🔴 **Not one row in this tier defaults to `main`**, and **three of seven grants are spelled
`LICENCE`.** 🟢 This is the single strongest case on this shelf for the warning three
paragraphs up and for `ACTION ZZ-q`'s orthography axis: a tool keyed on `main/LICENSE`
reports an entire national platform family, currently serving millions of pupils, as
unlicensed.

🟢 **It is alive, and the evidence is the commit log rather than a badge.** `entcore` at
**2026-10-20** — the day before this pass — with **21 distinct authors** in a 200-commit
window and modal commit domains `edifice.io` (128) and `web-education.net` (29). Édifice is
the vendor's current brand; Open Digital Education and `web-education.net` are its former
ones, which is why all three appear in one author set.

🟡 **Three addresses, two repositories, and one is stale.** `edificeio/entcore` and
`opendigitaleducation/entcore` serve an **identical 158-ref list** — one repository under
two names. `OPEN-ENT-NG/entcore` is a **single-branch live mirror**, one commit behind.
🔴 `open-ent/entcore` last moved **2026-06-01** and should not be cloned. 🟢 **Use
`edificeio/entcore`.**

🔴 **The documentation hazard, stated because it changes an estimate.** The `entcore`
README specifies **JSE 7** and a clone URL at `code.web-education.net`. The code is current;
the README is roughly a decade old. 🟢 Price discovery from the source tree. 🔴 An estimate
built by reading the README will be wrong in the expensive direction.

🟡 **Licence reach is the architectural constraint.** The whole tier is **AGPL-3.0**, so
a fork carries network-copyleft into whatever a client deploys. 🟢 `entcore` is a *modular
kernel with its own HTTP API and module boundary*, which is the boundary to build on — see
`compose/patterns.md` for the ENT pattern. 🔴 Forking a module is the expensive mistake here.

## Interoperability — LTI, SCORM, xAPI, Caliper

The layer that lets an agent talk to a client's existing LMS without a bespoke
connector. Almost entirely permissive, which is why this tier is the cheapest place
to start.

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Tsugi (LTI tool host) | [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | Apache-2.0 | `master/LICENSE` | **376** | North America |
| scorm-again (SCORM runtime) | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** | `master/LICENSE` | **356** | Not placed |
| Marsha (LTI LCMS) | [openfun/marsha](https://github.com/openfun/marsha) | **MIT** | `master/LICENSE` | **150** | EMEA |
| ltijs (LTI 1.3, Node) | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 | `master/LICENSE` | **373** | Not placed |
| pylti1.3 (LTI 1.3, Python) | [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** | `master/LICENSE` | **138** | Not placed |
| lti-tool | [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) | **MIT** | `main/LICENSE` | **8** | Not placed |
| ltikit-sdk | [Liberate-Labs/ltikit-sdk](https://github.com/Liberate-Labs/ltikit-sdk) | **MIT** | `main/LICENSE` | **0** | Not placed |
| django-lti-toolbox | [openfun/django-lti-toolbox](https://github.com/openfun/django-lti-toolbox) | **MIT** | `master/LICENSE` | **14** | EMEA |
| CACCL (Canvas app framework) | [harvard-edtech/caccl](https://github.com/harvard-edtech/caccl) | **MIT** | `main/LICENSE.md` | **35** | North America |
| ltiauthenticator | [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | BSD-3-Clause | `main/LICENSE` | **73** | North America |
| Caliper analytics spec | [1EdTech/caliper-spec](https://github.com/1EdTech/caliper-spec) | 🔴 **IMS specification licence — NOT OSI** | `master/LICENSE.md` | **22** | North America |
| 🆕 lti-core (LTI 1.3, TypeScript) | [iamlucasb/lti-core](https://github.com/iamlucasb/lti-core) | **MIT** (holder *Lucas Bossard*, 2026) | `main/LICENSE` | **1** | Not placed |
| 🆕 Ltix (LTI 1.3, **Elixir**) | [DecoyLex/ltix](https://github.com/DecoyLex/ltix) | **MIT** (holder *Alex Wilson*, 2025) | `main/LICENSE` | **2** | Not placed |
| 🆕 lti-node-library | [SanDiegoCodeSchool/lti-node-library](https://github.com/SanDiegoCodeSchool/lti-node-library) | **MIT** (holder *San Diego Code School*, **2019**) | `master/LICENSE` | **30** | North America |
| 🆕 ltijs — **fork** | [edugatorlabs/ltijs](https://github.com/edugatorlabs/ltijs) | Apache-2.0 | `master/LICENSE` | **0** | Not placed |

### 🟢 Choosing an LTI library is a four-way decision, and this pass can finally make it

🔵 **The standard is not one thing.** "LTI 1.3 support" can mean the OIDC launch alone,
or it can include **Deep Linking** (the tool puts content back into the LMS course),
**AGS** (the tool writes grades) and **NRPS** (the tool reads the roster). A library that
does launches only cannot submit a grade, and that is the capability an education
engagement almost always needs.

| Library | Runtime | Grant | Beyond launch | When to reach for it |
|---|---|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | Node | Apache-2.0 | Deep Linking, grades, roles | 🟢 **The default.** The most complete permissive tool provider on this shelf. 🟡 Its README describes v7 as a full rewrite — pin a version |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | Python | MIT | Deep Linking, AGS, NRPS | 🟢 The default when the agent is Python, which on this base it usually is |
| 🆕 [`iamlucasb/lti-core`](https://github.com/iamlucasb/lti-core) | TypeScript, framework-agnostic | MIT | Deep Linking **2.0**, JWKS | 🟢 When the deliverable is typed end-to-end. 🟡 **RS256 keys only**, and its own docs say the library *"never decides who may configure content"* — the tool must enforce that authorisation itself |
| 🆕 [`DecoyLex/ltix`](https://github.com/DecoyLex/ltix) | **Elixir** | MIT | Deep Linking + other Advantage services | 🔵 Narrow but genuinely new ground: the first BEAM-runtime LTI row on this base. Relevant where a client already runs Phoenix |
| 🆕 [`SanDiegoCodeSchool/lti-node-library`](https://github.com/SanDiegoCodeSchool/lti-node-library) | Node | MIT (2019) | 🔴 **none** — its README states NRPS and Deep Linking are **not supported** | 🔴 **Launch-only, and seven years old.** Published as a row so a successor finding it in the same leg does not mistake it for an alternative to `ltijs` |

🔴 **Two LTI addresses in this pass's leg are on the flag table instead, and neither for
a reason the landing page shows.**
[`GSU-CETLOE/lti1p3Library-php`](https://github.com/GSU-CETLOE/lti1p3Library-php) is the
cleanest *small* library found — tool-side Deep Linking 2.0, AGS and NRPS, no framework
dependency, published by a university — and its MIT holder line is the **unfilled
template**, `Copyright (c) 2026 [Your Name / Organization]`. There is nobody to
attribute, and attribution is MIT's only condition.
[`oat-sa/lib-lti1p3-deep-linking`](https://github.com/oat-sa/lib-lti1p3-deep-linking) is
**IMS-certified** and **GPL-2.0**.

🔴 **An instrument defect in this pass, published because the error ran in the safe
direction only by luck.** `p358`'s probe first classified the OAT library as **LGPL**.
The payload's first line is `GNU GENERAL PUBLIC LICENSE / Version 2, June 1991` — it is
GPL-2.0 — and the misread happened because **GPL-2.0's own preamble names the Lesser
GPL** (*"use the GNU Lesser General Public License instead"*), which a grep ordered to
test for "LESSER" before "GENERAL" matches first. 🔵 The consequence is the wrong
direction for an engagement: on a **library**, LGPL permits dynamic linking and GPL-2.0
does not, so a false LGPL **understates** copyleft reach on exactly the component type
where the distinction decides the architecture. Fixed by reading the version line rather
than the preamble, and recorded as **`ACTION ZZ-bg`**: any payload classifier on this
base must key on the licence's **title and version line**, never on a keyword that can
appear in another licence's prose.

🟡 **`edugatorlabs/ltijs` is a fork of `Cvmcosta/ltijs`, same Apache-2.0 grant.** Apache
boilerplate carries no holder field, so the `ZZ-bc` holder test cannot separate fork from
upstream here — 🔵 a measured limit of that test, not a result: **the divergent-holder
check works on MIT and BSD rows and is blind to Apache ones.** Use `Cvmcosta/ltijs`.

## 🆕 Learning records and rostering — where the data lands

🔵 **The gap this fills.** The tier above lets an agent *reach* a client's LMS. It said
nothing about where learning events are **stored**, which is what an analytics,
adaptivity or evidence-of-impact deliverable actually reads from — and §2 of
`intel/trends.md` records evidence becoming a procurement gate. 🟢 **Every row below was
read from the payload this pass**, and 🟡 **all but one are permissive** — `p362`'s
addition, `educa-lrs`, is **AGPL-3.0** and is shelved anyway because it is the first LRS
on this base placed in **EMEA by its own vendor's commit channel** (`+0100` on 26 of 31
commits; `schule-plus.com` ×27 and `digitallearning.gmbh` ×1 on the `%ae` limb). 🔴 Read
it as an **API to reach, never a fork**: the network clause is the whole point of an LRS,
which is a service. 🔴 **And state its dormancy, because the tier's other rows are
active:** last commit **2025-11-13**, roughly eleven months cold.

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| lrsql (SQL xAPI LRS) | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 | `main/LICENSE` | **144** | North America |
| xapi-lrs (xAPI 1.0.3 **and 2.0**) | [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | Apache-2.0 | `main/LICENSE` | **0** | Not placed |
| ADL_LRS (reference LRS) | [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) | Apache-2.0 | `master/LICENSE` | **334** | North America |
| Larissa (Apereo LRS) | [Apereo-Learning-Analytics-Initiative/Larissa](https://github.com/Apereo-Learning-Analytics-Initiative/Larissa) | Apache-2.0 | `master/LICENSE` | **8** | North America |
| learnmcp-xapi (the MCP bridge) | [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | `main/LICENSE` | **15** | Not placed |
| 🆕 OpenLRW (**OneRoster** + Caliper + xAPI) — 🟢 **canonical, corrected `p361`** | [Apereo-Learning-Analytics-Initiative/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | 🟢 **ECL-2.0** (payload; 🔴 index classifier says `NOASSERTION`) | `master/LICENSE` | **62** | North America |
| 🔴 OpenLRW — *the fork `p359` shelved by mistake* | [jeffyding/OpenLRW](https://github.com/jeffyding/OpenLRW) | ECL-2.0 (inherited) | `master/LICENSE` | **0** | — |
| 🆕 educa LRS (xAPI, Laravel) — `p362` | [digital-learning-gmbh/educa-lrs](https://github.com/digital-learning-gmbh/educa-lrs) | 🔴 **AGPL-3.0** (33 889 B) | `main/LICENSE.md` | **4** | **EMEA** (Germany) |

### 🟡 Pick by conformance and maturity, because the licences do not separate these rows

🟢 **`pelotech/xapi-lrs` is the one to start from** — it is the only row whose README
claims conformance to **both xAPI 1.0.3 and xAPI 2.0**, it ships an admin UI and
OpenTelemetry metrics, and it is Apache-2.0 on `main`. 🟢 **`yetanalytics/lrsql` is the
safer choice where the client wants a boring datastore**: SQLite or Postgres, and its
copyright notice runs to 2026.

🔴 **Two rows carry their own disqualifiers in their own READMEs, and a successor should
not re-discover them.** `adlnet/ADL_LRS` — the *reference* implementation, updated to
**xAPI 2.0 / IEEE 9274.1.1** — scopes itself to proof-of-concept use with few users.
`Larissa` states it has **no OAuth and no attachment support**. 🔵 Both are correct
things to read a standard against and wrong things to put under a client's traffic.

### 🔴 OneRoster has one project, two addresses, and `p359` shelved the wrong one — corrected `p361`

🟢 **OpenLRW is the only project found that carries OneRoster, IMS Caliper and xAPI in a
single warehouse**, and its grant is clean: **ECL-2.0**, read from `master/LICENSE` —
Apache-2.0 with §3's patent grant narrowed to education use, which for redistribution
purposes behaves as Apache-2.0.

🔴 **`p359` shelved the wrong address for it, and `p361`'s ranked search is what caught
that.** The canonical upstream is
[`Apereo-Learning-Analytics-Initiative/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW)
(**62 ★**, 25 forks). [`jeffyding/OpenLRW`](https://github.com/jeffyding/OpenLRW) is a
**fork at 0 ★**, created and last touched on the same day — 2018-01-19 — and the two
carry **different HEAD SHAs**. 🔵 **A non-ranked search cannot tell a fork from an
upstream; a ranked one puts 62 ★ above 0 ★ and the question answers itself.**

🔴 **And the index's own "recency" fields would have misled in the other direction.** On
the canonical: `updated_at` **2026-08-04**, `pushed_at` **2025-09-12**, 🟢 **last commit
on `master` 2020-02-06.** Three fields, three answers, a 6½-year spread, and only the
last one is a commit.

🔴 **Both addresses are stale, and every non-commit surface says otherwise.** A GitHub
**topic page** reports *"updated September 2025"*; the index reports `updated_at`
**2026-08-04**. 🟢 **Commit channel, first-hand: the fork ends 2018-01-16 (92 commits, 7
authors, from 2016-10-17); the canonical ends 2020-02-06.** 🔵 **A date that is not a
commit date is not a maintenance signal** — and `p361` widens that rule from topic pages
to the API's own `updated_at` and `pushed_at` fields, which are *metadata* and *any-ref
push* respectively, not commits.

🟢 **So the shelf gains a schema and not a dependency — and the correction does not
change that advice, only the address it points at.** The OneRoster↔Caliper↔xAPI
mapping in the canonical tree is the artefact worth reading. 🔴 **And the connector gap is
real and stated:** **no OneRoster MCP server exists** — `p359` probed the rostering leg
and found none — so an engagement that needs *"who is in this class"* writes that
connector. 🔵 It is the one interoperability standard on these shelves with no agent
connector at all, and it is the one every roster-aware deliverable needs first.

## 🆕 Psychometrics — the measurement layer, permissive and never shelved until now

🔵 **Why it belongs on a foundations shelf.** Every adaptivity and mastery claim on
these shelves — Bayesian Knowledge Tracing in `OATutor`, FSRS in `Smart-Study-Agent`,
"adaptive difficulty" in half the assessment tier — rests on item-response theory.
🔴 **This base had found these libraries at earlier passes and left them on
`agents/trending.md`.** `p359` promotes them, re-verified.

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| 🆕 🟢 **irtorch** (IRT on PyTorch, GPU) | [joakimwallmark/irtorch](https://github.com/joakimwallmark/irtorch) | **MIT** | 🟡 `main/LICENSE.txt` | **18** | **EMEA** — `+0200`/`+0100` |
| 🆕 girth (IRT for Python) | [eribean/girth](https://github.com/eribean/girth) | **MIT** | 🟡 `master/LICENSE.txt` | **127** | **North America** — `-0500`/`-0400` |
| 🆕 girth_mcmc (Bayesian / MCMC IRT) | [eribean/girth_mcmc](https://github.com/eribean/girth_mcmc) | **MIT** | 🟡 `main/LICENSE.txt` | **19** | **North America** — `-0400`/`-0500` |
| 🆕 variational-IRT | [mhw32/variational-item-response-theory-public](https://github.com/mhw32/variational-item-response-theory-public) | **MIT** | `master/LICENSE` | **82** | **North America** — `-0700` |

### 🔴 Three of the four are abandoned, and the live one is not the one this base was pointing at

🟢 **The commit channel separates these rows where the licence does not.** Last commit,
read first-hand:

| Repo | Last commit | State |
|---|---|---|
| [`joakimwallmark/irtorch`](https://github.com/joakimwallmark/irtorch) | 🟢 **2026-10-19 — two days before this pass** | 🟢 **Live. The only maintained permissive IRT engine found** |
| [`eribean/girth`](https://github.com/eribean/girth) | 🔴 2022-01-30 | 🔴 ~5 years stale |
| [`eribean/girth_mcmc`](https://github.com/eribean/girth_mcmc) | 🔴 2021-11-10 | 🔴 ~5 years stale |
| [`mhw32/variational-item-response-theory-public`](https://github.com/mhw32/variational-item-response-theory-public) | 🔴 2020-05-28 | 🔴 ~6 years stale; paper companion code |

🔴 **This corrects a recommendation shape this base was carrying.** `girth` is the row
earlier passes named — it is the oldest, best-known and most-cited — and it has not been
touched in five years. 🟢 **`irtorch` is the row to build on**: MIT, PyTorch-backed with
GPU support, actively committed this week, and **EMEA-origin**, which makes it the only
psychometrics row that places in a region other than North America.

🔵 **Both halves of that matter to an engagement.** A stale MIT library is still legally
safe to vendor and *is* a defensible choice for a stable algorithm — IRT estimation is
not a moving target, and `girth` is a reasonable thing to pin. 🔴 **What it cannot do is
carry a client's security-patching expectations**, and a studio that lists it as a
"maintained dependency" in a proposal has mis-described it.

### 🔴 Three of the four put the grant at `LICENSE.txt`, and `girth`'s `LICENSE` is a 404

🟢 **Read first-hand this pass:** `eribean/girth` serves **404 at `master/LICENSE`** and
**200 at `master/LICENSE.txt`**. 🔵 **The whole permissive psychometrics family shares
that shape** — `girth`, `girth_mcmc` and `irtorch` all carry `LICENSE.txt` — so a probe
that tries `LICENSE` alone reports **the entire tier as grantless**, and every one of
them is stock MIT. 🟢 This is the shelf's existing default-branch warning in its other
form: **the filename is as load-bearing as the branch.**

### 🔴 What is NOT here: a licensed IRT-calibrated LLM grader

🔴 **Three 2026 papers pair IRT calibration with LLM short-answer grading** — including
*"Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer
Grading via Item Response Theory"* — and `p359` could not find a usable implementation
behind any of them. The nearest code, [`mainlp/llm-psychometrics`](https://github.com/mainlp/llm-psychometrics),
is **live with no licence file at seven probed paths**. 🔴 The standard R package,
[`philchalmers/mirt`](https://github.com/philchalmers/mirt), carries **no root
`LICENSE`** at all — its grant is `License: GPL (>= 3)` in `DESCRIPTION`, the CRAN shape,
and it is copyleft when found.

🟢 **So the four rows above are calibration engines with no grading layer, and that is
the opportunity:** the join is **unbuilt**, both halves are MIT, and an engagement that
needs defensible difficulty estimates on AI-marked items builds it rather than buying
it — on **`irtorch`**, per the maturity table above, not on `girth`. 🔵 See §17 of `intel/trends.md` — AI marking has acquired a disclosure duty and a
measured anchoring bias, and an IRT-calibrated item is the evidence that answers both.

## Assessment, integrity and accessibility

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Judge0 (code execution API) | [judge0/judge0](https://github.com/judge0/judge0) | GPL-3.0 | `master/LICENSE` | **4 492** | EMEA |
| Dolos (plagiarism detection) | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | `main/LICENSE` | **353** | EMEA |
| INGInious (exercise assessment) | [INGInious/INGInious](https://github.com/INGInious/INGInious) | AGPL-3.0 (*"most of the files"*) | `main/LICENSE` | **243** | EMEA |
| UDOIT (accessibility inspection) | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | GPL-3.0 | `main/LICENSE` | **117** | North America |
| Ares2 (secure grading runner) | [ls1intum/Ares2](https://github.com/ls1intum/Ares2) | **MIT** | `main/LICENSE` | **5** | EMEA |
| autograder — 🔴 **ARCHIVED** (`p361`) | [zmievsa/autograder](https://github.com/zmievsa/autograder) | GPL-3.0 | `main/LICENSE` | **48** | Not placed |

## Code execution, online judges and autograding — 🆕 a whole tier this base did not have

🟢 **This tier is `p356`'s finding and it is the largest single supply discovery on
this base.** `p354` recovered [`judge0`](https://github.com/judge0/judge0) by aiming a
leg at a **function** instead of at "AI education". `ACTION ZZ-ay` asked for that leg
shape to be run across nine functions. The `"online judge"` leg alone returned **62
repositories, 12 of them verified here, and all 12 absent from this base's entire
corpus** — `archive/` and `evidence/` included — with **7 137 ★** at the head.

🔵 **Why twelve passes of agent-shaped queries could not see it.** This software is
not called an AI tool and does not describe itself as one. It is the **grading
execution substrate** underneath every programming course: a sandbox, a queue, a
verdict. An education engagement that has to run student code needs exactly this and
would otherwise build it.

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Hydro (multi-tenant judge) | [hydro-dev/Hydro](https://github.com/hydro-dev/Hydro) | AGPL-3.0 | `master/LICENSE` | **7 140** | APAC |
| QingdaoU OnlineJudge | [QingdaoU/OnlineJudge](https://github.com/QingdaoU/OnlineJudge) | 🟢 **MIT** | `master/LICENSE` | **6 552** | APAC |
| HUSTOJ | [zhblue/hustoj](https://github.com/zhblue/hustoj) | GPL-2.0 | `master/LICENSE` | **3 813** | APAC |
| DMOJ (judge + contest platform) | [DMOJ/online-judge](https://github.com/DMOJ/online-judge) | AGPL-3.0 | `master/LICENSE` | **1 194** | North America |
| online-judge-tools | [online-judge-tools/oj](https://github.com/online-judge-tools/oj) | 🟢 **MIT** | `master/LICENSE` | **1 172** | APAC |
| DMOJ judge-server | [DMOJ/judge-server](https://github.com/DMOJ/judge-server) | AGPL-3.0 | `master/LICENSE` | **980** | North America |
| NOJ | [ZsgsDesign/NOJ](https://github.com/ZsgsDesign/NOJ) | 🟢 **MIT** | `master/LICENSE` | **942** | APAC |
| HOJ | [HimitZH/HOJ](https://github.com/HimitZH/HOJ) | 🟢 **MIT** | `master/LICENSE` | **942** | APAC |
| SYZOJ | [syzoj/syzoj](https://github.com/syzoj/syzoj) | 🟢 **MIT** | `master/LICENSE` | **922** | APAC |
| SDUOJ (microservices) | [SDUOJ/OnlineJudge](https://github.com/SDUOJ/OnlineJudge) | AGPL-3.0 | `main/LICENSE` | **556** | APAC |
| QingdaoU Judger (seccomp sandbox) | [QingdaoU/Judger](https://github.com/QingdaoU/Judger) | 🔴 **SATA — MIT body + added obligations, NOT permissive** (1 823 B), corrected `p362` | 🔴 `newnew/LICENSE` | **496** | APAC |
| Sharif Judge (course-oriented) | [mjnaderi/Sharif-Judge](https://github.com/mjnaderi/Sharif-Judge) | **GPL-3.0** (35 146 B, no Affero title), corrected `p362` | 🔴 `Version-1/LICENSE` | **395** | EMEA |
| Otter-Grader (notebook autograder) | [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** | `master/LICENSE` | **161** | North America |
| webtech autograder | [webtech-network/autograder](https://github.com/webtech-network/autograder) | 🟢 **Apache-2.0** | `main/LICENSE` | **62** | Not placed |
| OK client (Berkeley autograder) | [okpy/ok-client](https://github.com/okpy/ok-client) | 🟢 **Apache-2.0** | `master/LICENSE` | **57** | North America |
| 🆕 CodeSense (programming-education platform) — `p362` | [XiaoCow666/CodeSense](https://github.com/XiaoCow666/CodeSense) | 🟢 **MIT** (1 067 B) | `main/LICENSE` | **4** | APAC |

🟢 **Read the licence column as the engagement decision.** **Five** of the fifteen are
**MIT, BSD-3-Clause or Apache-2.0** — [`QingdaoU/OnlineJudge`](https://github.com/QingdaoU/OnlineJudge)
at 6 552 ★ is a **complete, MIT-licensed, Docker-deployable judge**, re-read from payload
this pass at **1 085 B**. 🔵 Against this, `judge0` (GPL-3.0) has to be consumed over its
API to keep the boundary. **The permissive option in this tier is still the bigger one**,
which remains the reversal of the assumption the `judge0`-only shelf implied.

### 🔴 `p362`: the MIT judge everybody reaches for cannot execute code under an MIT grant

🔴 **The correction above is a row. This is the stack, and it is the finding.**
`QingdaoU/OnlineJudge` is a **multi-repository system**, and its own README names the
companions: *"Judger Sandbox(Seccomp)"* and *"JudgeServer(A wrapper for Judger)"*. 🔴
**Three of the five components were absent from this entire corpus** — this base had
shelved the two it had found by name and never asked what runs the code.

🟢 **All five read first-hand this pass, at their real default refs:**

| Component | Role | Licence (payload) | Bytes | Grant read at | ★ 2026-10-21 |
| --- | --- | --- | ---: | --- | ---: |
| [QingdaoU/OnlineJudge](https://github.com/QingdaoU/OnlineJudge) | Django backend, contests, problem bank | 🟢 **MIT** | 1 085 | `master/LICENSE` | **6 552** |
| 🆕 [QingdaoU/OnlineJudgeFE](https://github.com/QingdaoU/OnlineJudgeFE) | Vue front end | 🟢 **MIT** | 4 334 | `master/LICENSE` | **330** |
| 🔴 🆕 [QingdaoU/JudgeServer](https://github.com/QingdaoU/JudgeServer) | the wrapper that actually executes submissions | 🔴 **SATA** | 1 823 | `master/LICENSE` | **209** |
| 🔴 [QingdaoU/Judger](https://github.com/QingdaoU/Judger) | the seccomp sandbox | 🔴 **SATA** | 1 823 | `newnew/LICENSE` | **496** |
| 🔴 🆕 [QingdaoU/OnlineJudgeDeploy](https://github.com/QingdaoU/OnlineJudgeDeploy) | the documented `docker compose` deployment | 🔴 **no grant at any probed path** | — | `2.0` — none found | **591** |

🔴 **So the halves split by function, and the split is exactly the wrong way round for a
studio.** The components that **render pages** are MIT. The components that **run
untrusted student code** are SATA. And the manifest a client's ops team will actually
`git clone` — 591 ★, more than the sandbox — carries **no licence at all**, on `2.0`,
which is not `main` or `master` either.

🔵 **Measured, not inferred:** `JudgeServer`'s `Dockerfile` does `COPY Judger/ /app/` and
builds `libjudger.so` into `/usr/lib/judger/`, so the SATA sandbox is **vendored into**
the SATA wrapper; `OnlineJudgeDeploy`'s compose file runs that wrapper as the `oj-judge`
service from a published `judge:1.6.1` image. 🟢 `OnlineJudgeFE`'s 4 334 B is benign and
was read too: **three concatenated MIT notices** — its own, Vue's, and one more — which is
the fourth "excess explained" of this pass.

🟡 **What this changes for an engagement, concretely.** *"Fork `QingdaoU/OnlineJudge` into
a closed client deliverable"* remains true **of the web tier** and says nothing about
grading. A client that needs to run code gets one of three positions, and should pick
deliberately rather than discover it at review:

1. 🟡 **Honour SATA.** Its obligations are cheap — star the project, thank the authors in
   your notices, leave its copyright and project-url block intact — but it is **not OSI
   open source**, an SPDX scanner returns `NOASSERTION`, and a procurement checklist that
   says *"permissive only"* fails it.
2. 🟢 **Replace the executor.** `judge0` (GPL-3.0, over its API),
   [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) (BSD-3-Clause,
   notebooks) and 🆕 [`XiaoCow666/CodeSense`](https://github.com/XiaoCow666/CodeSense)
   (MIT, restricted execution + code evaluation, 554 commits) are all genuinely
   permissive — 🔴 none of them is a drop-in for a seccomp sandbox, so this is a build,
   not a swap.
3. 🟢 **Keep the execution tier outside the deliverable entirely**, reached over HTTP,
   which is the boundary `compose/patterns.md` Pattern 9 already uses for `judge0`.

🔴 **The general form, and it is why this is on the foundations shelf rather than in a
footnote: in this sector a platform's LICENSE file is a statement about one repository,
and the thing that does the dangerous work usually lives in another one.** Published as
`T30` on `intel/trends.md` and registered as `ACTION ZZ-bo`.

🔴 **The count fell from six to five this pass, and the row that left is the one the
permissive path leaned on.** [`QingdaoU/Judger`](https://github.com/QingdaoU/Judger) was
published here as *"its seccomp sandbox on its own MIT grant"*. 🔴 **There is no MIT
grant.** Its payload at `newnew/LICENSE` is the **Star And Thank Author License**: MIT's
permission paragraph, then *"you shall star/+1/like the project(s) ... and then thank the
author(s)"*, plus a clause forbidding modification of the copyright and project-url
sections. 🔴 GitHub's own classifier reads the repository as **`NOASSERTION`**, so **no
channel ever said MIT** — the grant was inherited from the sibling `OnlineJudge`, which
really is MIT. 🟡 **What an engagement may still do:** the obligations are cheap to honour
(star the project, thank the authors in your notices, leave its copyright block intact)
and the sandbox is 292 KB of C. But it is **not OSI open source**, so it cannot go into
the permissive column, and a client whose counsel runs an SPDX scanner will get
`NOASSERTION` back. 🟢 **The permissive substitute measured this pass is
[`XiaoCow666/CodeSense`](https://github.com/XiaoCow666/CodeSense)** — MIT, 554 commits,
restricted execution plus code evaluation — shelved below.

🟡 **Two of the three non-contest rows matter most for a client.**
[`mjnaderi/Sharif-Judge`](https://github.com/mjnaderi/Sharif-Judge) is built for
**programming courses** rather than contests — assignments, deadlines, per-student
feedback — and [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader)
grades **Python *and* R notebooks**, which is where this base's prior autograder
([`nbgrader`](https://github.com/jupyter/nbgrader), Jupyter-only) stopped.

🔴 **Two default branches in this tier are neither `main` nor `master`.**
`QingdaoU/Judger` defaults to **`newnew`** and `Sharif-Judge` to **`Version-1`**. A
licence sweep that probes `main` and `master` reports both as grantless.

🔵 **`p362` found the sharper version of that warning, and it is the opposite shape.**
Both of those odd refs *were* probed, and both cells recorded the right **path** and the
wrong **family** — `Judger` as MIT when the payload is SATA, `Sharif-Judge` as AGPL-3.0
when the payload is the plain GPLv3 text (*"GNU GENERAL PUBLIC LICENSE, Version 3, 29
June 2007"*, 35 146 B, identical at `master`). 🔴 **So finding the grant is not reading
it**, and a path column that says `200` says nothing about the family in the bytes.

## Content authoring, media and delivery

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| JupyterHub | [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | BSD-3-Clause | `main/LICENSE` | **8 361** | North America |
| BigBlueButton | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | `v4.0.x-develop/LICENSE` | **9 249** | North America |
| pytogether (collaborative IDE) | [SJRiz/pytogether](https://github.com/SJRiz/pytogether) | **MIT** | `main/LICENSE` | **261** | Not placed |
| Opencast (lecture capture) | [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** | `develop/LICENSE` | **509** | EMEA |
| H5P core | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | `master/LICENSE.txt` | **151** | EMEA |
| H5P CLI | [h5p/h5p-cli](https://github.com/h5p/h5p-cli) | 🟢 **MIT** | `master/LICENSE` | **78** | EMEA |
| Hyperbook | [openpatch/hyperbook](https://github.com/openpatch/hyperbook) | **MIT** | `main/LICENSE.md` | **74** | EMEA |
| yanki (markdown → Anki) | [kitschpatrol/yanki](https://github.com/kitschpatrol/yanki) | 🟡 **MIT, `package.json` only** | `main/package.json` — 🔴 *no licence file in tree* | **61** | Not placed |

🟢 **H5P is a split grant worth knowing:** the core library is GPL-3.0 but
[`h5p/h5p-cli`](https://github.com/h5p/h5p-cli) is **MIT**. Tooling built against
the CLI carries no copyleft; code linked into the library does.

## Administration — SIS, ERP, credentials

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| OpenEduCat (education ERP) | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | `19.0/LICENSE` | **893** | APAC |
| RosarioSIS (student info system) | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | `mobile/LICENSE` | **647** | EMEA |
| Learner Credential Wallet | [openwallet-foundation-labs/learner-credential-wallet](https://github.com/openwallet-foundation-labs/learner-credential-wallet) | **MIT** | `main/LICENSE` | **89** | Global |
| Terracotta (in-LMS experiments) | [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | Apache-2.0 | `development/LICENSE` | **21** | North America |
| 🆕 openSIS Classic (K-12 SIS) | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | GPL-2.0 | 🔴 `master/docs/License.txt` — **root carries no grant file** | **346** | Not placed |
| 🆕 FenixEdu Academic (HE SIS) | [FenixEdu/fenixedu-academic](https://github.com/FenixEdu/fenixedu-academic) | LGPL-3.0 | `master/LICENSE` | **175** | EMEA |
| 🆕 🟢 **Academico** (school management / SIS) | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** | `main/LICENSE` | **408** | EMEA |
| 🆕 ERPNext (institution-wide ERP) | [frappe/erpnext](https://github.com/frappe/erpnext) | **GPL-3.0** | 🔴 `develop/license.txt` — **lower-case path on a non-`main` default branch** | **40 419** | APAC |

### 🔴 `ERPNext` fails both of this base's grant hazards at once, and it is the row most likely to be reached for

🟢 **`p357` adds it because `frappe/lms` is already on the LMS tier and ERPNext is the
other half of that stack** — an institution running Frappe LMS for teaching and ERPNext
for finance, HR and procurement is a single-vendor deployment a studio will meet.

🔴 **It is also a clean reproduction of the two hazards this base keeps measuring.** Its
default branch is **`develop`**, not `main`, and its grant sits at **`license.txt`**,
lower-case. A probe assuming `main/LICENSE` reports this repository — one of the
largest open-source ERPs in existence — as **grantless**. 🔵 That is the
`frappe/lms` shape exactly, from the same organisation, which is the useful part: the
hazard is an **organisational convention**, not a per-repository accident. Where one
Frappe repository hides its grant this way, assume all of them do.

🔴 **And the licence is the engagement constraint.** GPL-3.0, not the AGPL of
`frappe/lms` and not the LGPL-3.0 of `openeducat_erp`. 🟢 So an institution-wide Frappe
stack spans **three different copyleft strengths**, and a deliverable's obligations
depend on which component it links — which is why
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (LGPL-3.0,
linking permitted) remains this shelf's recommended ERP base for closed work.

### 🔴 The permissive education ERP this leg promised does not exist at the address given

🟢 **The leg was run because a permissive ERP would be the single most valuable row on
this tier** — every ERP and SIS this base carries is copyleft (LGPL-3.0, GPL-2.0,
GPL-3.0, AGPL-3.0), so an engagement that must ship a closed admin deliverable has no
base to fork. A vendor comparison in this pass's leg named two:

| Claimed | Claimed licence | What `p357` found |
|---|---|---|
| **Fedena** ([`foradian/fedena`](https://github.com/foradian/fedena)) | Apache-2.0, Ruby on Rails | 🔴 **Live on `master` and empty.** `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.txt`, `license.txt`, `LICENCE`, `LICENSE-MIT`, `README.md` and `Gemfile` **all 404**. The claim is unverifiable at this address |
| **GegoK12** (`gegok12/gegok12`) | MIT, *"twenty-six modules free forever"* | 🔴 **No such repository** — `ls-remote` returns nothing. The claim traces to a vendor website, not to a public tree |
| **SchoolTool** (`schooltool/schooltool`) | GPL-2.0, per a comparison table | 🔴 **Dead.** No substitute found under that owner |

🔵 **Published as a refutation rather than omitted, for one reason.** All three claims
sit in roundups that rank well and read authoritatively, and a later pass searching
"permissive education ERP" will meet them again. 🟢 **The honest finding is the
absence:** on this base's evidence there is **no verified permissive education ERP**, so
a closed admin deliverable is a **build**, not a fork — and that is a costing input, not
a gap in the research.

🟢 **`openSIS-Classic`'s grant was RECOVERED this pass, and `p354` predicted the exact
shape.** Six root rungs (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`,
`license.txt`, `GNU-AGPL-3.0.txt`) all answer **404**; the README names
`docs/License.txt`, and that path returns **17 286 bytes of GPL-2.0, BOM-prefixed**.
🔴 **Two corrections ride on reading it rather than the README:** the README says only
*"the GNU General Public License"* with no version, and the payload is **Version 2, not
Version 3** — which decides compatibility — while the leading **UTF-8 BOM** means a
classifier anchored on `^GNU` sees no match at all.

## Curriculum corpora and open courseware

| Asset | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| freeCodeCamp | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | BSD-3-Clause | `main/LICENSE.md` | **457 613** | North America |
| Open Source Society CS | [ossu/computer-science](https://github.com/ossu/computer-science) | **MIT** | `master/LICENSE` | **210 188** | Global |
| MCP for Beginners | [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | **MIT** | `main/LICENSE` | **17 486** | North America |
| openunivcourses | [kabartay/openunivcourses](https://github.com/kabartay/openunivcourses) | **MIT** | `main/LICENSE` | **253** | Not placed |
| elimu.ai literacy webapp | [elimu-ai/webapp](https://github.com/elimu-ai/webapp) | **MIT** | `main/LICENSE` | **41** | EMEA |
| UIUC systems coursebook | [cs341-illinois/coursebook](https://github.com/cs341-illinois/coursebook) | 🔴 **NCSA** (code) + **CC-BY-4.0** (built PDFs) | `master/LICENSE/README.md` — 🔴 🔴 **`LICENSE/` is a DIRECTORY** — see `LICENSE/README.md` | **3 849** | North America |

🔴 **`cs341-illinois/coursebook` is this shelf's sharpest grant trap.** `LICENSE` is
not a file, it is a **directory**. Inside, `LICENSE/README.md` states three different
grants: NCSA for code contributions (`LICENSE.code`), CC-BY-4.0 for the generated
PDFs, and the original wikibook's licence for remixed material (`LICENSE.original`).
A previous pass on this base published this row as **MIT**. It is not MIT. NCSA is
permissive and usable, but it must be named correctly.

---

## Carried inventory — re-verified this pass, not promoted to the tiers above

🟢 **72 addresses, every one re-probed first-hand 2026-10-21 and every one ALIVE.** These
were held on this base's shelves from earlier passes. This pass's rewrite of the curated
tiers would have dropped them, and the `fold-identity` gate caught it — so rather than
lose verified work, they are restored here with their grants **re-read from the payload
today**, not carried on trust.

🔴 **20 of the 72 carry no grant file at the repository root on the default branch.**
Absent a licence, the default is all-rights-reserved: these are **not** usable in client
work however public the code is. Most are research artefacts from the OpenEduHub estate.

**OpenEduHub / WirLernenOnline — the largest single open-education engineering estate found on this base (EMEA, Germany)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [openeduhub/duplicate-detection](https://github.com/openeduhub/duplicate-detection) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/edu-sharing-python-client](https://github.com/openeduhub/edu-sharing-python-client) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/its-data](https://github.com/openeduhub/its-data) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/its-jointprobability](https://github.com/openeduhub/its-jointprobability) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/its-prep](https://github.com/openeduhub/its-prep) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/its-qna](https://github.com/openeduhub/its-qna) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/ki-prompt-benchmark](https://github.com/openeduhub/ki-prompt-benchmark) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/lernpfadeditor](https://github.com/openeduhub/lernpfadeditor) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/llm-judge](https://github.com/openeduhub/llm-judge) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/mappings](https://github.com/openeduhub/mappings) | GPL-3.0 | `main/LICENSE` |
| [openeduhub/metadata-agent-api](https://github.com/openeduhub/metadata-agent-api) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/metadata-agent-canvas](https://github.com/openeduhub/metadata-agent-canvas) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/metadata-browser-plugin-fuerapi](https://github.com/openeduhub/metadata-browser-plugin-fuerapi) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/metalookup](https://github.com/openeduhub/metalookup) | GPL-3.0 | `main/LICENSE.txt` |
| [openeduhub/oeh-metadata-vocabs](https://github.com/openeduhub/oeh-metadata-vocabs) | CC | `master/LICENSE` |
| [openeduhub/oeh-search-etl](https://github.com/openeduhub/oeh-search-etl) | 🔴 **no grant at root** | `master/` — none found |
| [openeduhub/oeh-search-frontend](https://github.com/openeduhub/oeh-search-frontend) | 🔴 **no grant at root** | `develop/` — none found |
| [openeduhub/python-kidra](https://github.com/openeduhub/python-kidra) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/skohub-vocabs-oeh-patched](https://github.com/openeduhub/skohub-vocabs-oeh-patched) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/text-extraction](https://github.com/openeduhub/text-extraction) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/text-statistics](https://github.com/openeduhub/text-statistics) | GPL-3.0 | `main/LICENSE` |
| [openeduhub/topic-statistics](https://github.com/openeduhub/topic-statistics) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/tutor-chatbot](https://github.com/openeduhub/tutor-chatbot) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/wlo-quellenliste](https://github.com/openeduhub/wlo-quellenliste) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/z-api-runner](https://github.com/openeduhub/z-api-runner) | 🔴 **no grant at root** | `master/` — none found |

**Open edX ecosystem (North America)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [openedx/frontend-base](https://github.com/openedx/frontend-base) | AGPL-3.0 | `main/LICENSE` |
| [openedx/frontend-platform](https://github.com/openedx/frontend-platform) | AGPL-3.0 | `master/LICENSE` |
| [openedx/openedx-proposals](https://github.com/openedx/openedx-proposals) | CC | `master/LICENSE` |

**France Université Numérique (EMEA, France)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [openfun/ashley](https://github.com/openfun/ashley) | **MIT** | `master/LICENSE` |
| [openfun/potsie](https://github.com/openfun/potsie) | **MIT** | `main/LICENSE.md` |

**D2L Brightspace, first-party (North America)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [Brightspace/test-reporting-node](https://github.com/Brightspace/test-reporting-node) | **Apache-2.0** | `main/LICENSE` |
| [BrightspaceUI/core](https://github.com/BrightspaceUI/core) | **Apache-2.0** | `main/LICENSE` |
| [BrightspaceUI/intl](https://github.com/BrightspaceUI/intl) | **Apache-2.0** | `main/LICENSE` |
| [BrightspaceUI/labs](https://github.com/BrightspaceUI/labs) | **Apache-2.0** | `main/LICENSE` |

**LTI libraries, additional**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [adamzammit/ltiplugin](https://github.com/adamzammit/ltiplugin) | GPL-3.0 | `master/LICENSE` |
| [annoto/ims-lti](https://github.com/annoto/ims-lti) | **MIT** | `master/LICENSE` |
| [godmartinz/node-lti-1.3-library](https://github.com/godmartinz/node-lti-1.3-library) | 🔴 **no grant at root** | `master/` — none found |
| [longsightgroup/lti-tool](https://github.com/longsightgroup/lti-tool) | **MIT** | `main/LICENSE` |
| [scormflow/scorm-engine-client](https://github.com/scormflow/scorm-engine-client) | **MIT** | `main/LICENSE` |

**Curriculum knowledge graphs**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [mizcausevic-dev/curriculum-knowledge-graph](https://github.com/mizcausevic-dev/curriculum-knowledge-graph) | **MIT** | `main/LICENSE` |
| [oseducation/knowledge-graph](https://github.com/oseducation/knowledge-graph) | 🔴 **no grant at root** | `main/` — none found |
| [razi-03/ncert-ckg](https://github.com/razi-03/ncert-ckg) | 🔴 **no grant at root** | `main/` — none found |

**Privacy, de-identification and synthetic data — the compliance toolkit for education data**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [arx-deidentifier/arx](https://github.com/arx-deidentifier/arx) | **Apache-2.0** | `master/LICENSE` |
| [greenmaskio/greenmask](https://github.com/greenmaskio/greenmask) | **Apache-2.0** | `main/LICENSE` |
| [hitsz-ids/synthetic-data-generator](https://github.com/hitsz-ids/synthetic-data-generator) | **Apache-2.0** | `main/LICENSE` |
| [meta-pytorch/opacus](https://github.com/meta-pytorch/opacus) | **Apache-2.0** | `main/LICENSE` |
| [OpenMined/PyDP](https://github.com/OpenMined/PyDP) | **Apache-2.0** | `dev/LICENSE` |
| [rizzo-ai-academy/rizzo-pii](https://github.com/rizzo-ai-academy/rizzo-pii) | **MIT** | `main/LICENSE` |
| [securitybunker/databunker](https://github.com/securitybunker/databunker) | **MIT** | `master/LICENSE` |
| [synthetichealth/synthea](https://github.com/synthetichealth/synthea) | **Apache-2.0** | `master/LICENSE` |
| [thoughtbot/top_secret](https://github.com/thoughtbot/top_secret) | **MIT** | `main/LICENSE.txt` |

**Courseware and curriculum corpora, additional**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [freeCodeCamp/curriculum-helpers](https://github.com/freeCodeCamp/curriculum-helpers) | **BSD** | `main/LICENSE` |
| [h5p/h5p-interactive-video](https://github.com/h5p/h5p-interactive-video) | 🔴 **no grant at root** | `master/` — none found |
| [openki/openki](https://github.com/openki/openki) | AGPL-3.0 | `dev/LICENSE` |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | **MIT** | `main/LICENSE` |
| [weecology/forecasting-course](https://github.com/weecology/forecasting-course) | CC | `main/LICENSE.md` |

**Learning agents, tutors and tooling, additional**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [010ankushsharma/adaptalearn](https://github.com/010ankushsharma/adaptalearn) | 🔴 **no grant at root** | `master/` — none found |
| [chrischall/gogcli-mcp](https://github.com/chrischall/gogcli-mcp) | **MIT** | `main/LICENSE` |
| [christophblessing/quiz-recap](https://github.com/christophblessing/quiz-recap) | **MIT** | `main/LICENSE` |
| [damphuquy/agent-as-a-tutor](https://github.com/damphuquy/agent-as-a-tutor) | **MIT** | `main/LICENSE` |
| [dymchenkko/claude-study-agent](https://github.com/dymchenkko/claude-study-agent) | **MIT** | `main/LICENSE` |
| [groton-school/canvas-cli](https://github.com/groton-school/canvas-cli) | GPL-3.0 | `main/LICENSE` |
| [ibenian/algebench](https://github.com/ibenian/algebench) | **MIT** | `main/LICENSE` |
| [kyyota-wang/cloverailab](https://github.com/kyyota-wang/cloverailab) | 🔴 **no grant at root** | `main/` — none found |
| [lucasspinola/assistentes-educacionais-com-ia](https://github.com/lucasspinola/assistentes-educacionais-com-ia) | **MIT** | `main/LICENSE` |
| [molecule-dev/molecule](https://github.com/molecule-dev/molecule) | **Apache-2.0** | `main/LICENSE` |
| [mthatipamula/educational-assessment-ai-agent-platform](https://github.com/mthatipamula/educational-assessment-ai-agent-platform) | 🔴 **no grant at root** | `main/` — none found |
| [muhammedalakbarli/imparo](https://github.com/muhammedalakbarli/imparo) | **MIT** | `main/LICENSE` |
| [nichochar/ari](https://github.com/nichochar/ari) | **MIT** | `main/LICENSE` |
| [risnake/canvas-mcp-server](https://github.com/risnake/canvas-mcp-server) | 🔴 **no grant at root** | `main/` — none found |
| [smashburger-dev/argmin](https://github.com/smashburger-dev/argmin) | **MIT** | `main/LICENSE` |
| [viendinhcom/supermemo](https://github.com/viendinhcom/supermemo) | **MIT** | `master/LICENSE` |

---

## 🟢 Alias correction applied this pass

[`openedx/edx-platform`](https://github.com/openedx/edx-platform) and
[`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) return the
**identical HEAD** `7f01c42157d30cc273c06d62448b6d5a26624495`. They are one
repository. The authenticated index returns **`openedx/openedx-platform`** as the
canonical name; this base has been publishing the stale one. The table above now
carries the canonical address.

## 🔵 Grant-path distribution, re-derived AFTER this pass wrote — which is what `gate-census-currency` is for

🟢 Derived over the curated tiers of **this** tree, as the last act before the commit,
not carried from `p355`'s sentence:

| Grant filename | Rows on this shelf |
|---|---:|
| `LICENSE` | 51 |
| `LICENSE.md` | 5 |
| 🔴 `COPYING.txt` | 2 — `moodle/moodle`, `moodlehq/moodleapp` |
| `LICENSE.txt` | 2 |
| 🔴 `license.txt` (lower-case) | **2** — `frappe/lms`, 🆕 `frappe/erpnext` |
| 🔴 a **directory** | 1 — `cs341-illinois/coursebook` |
| 🔴 `package.json` field only | 1 — `kitschpatrol/yanki` |
| 🔴 🆕 **`docs/License.txt`** | 1 — `OS4ED/openSIS-Classic` |

**14 of 65 grants (21.5 %) are not at `LICENSE`.** 🔴 **The share went UP again** —
`p355` published 6 of 41 (15 %), `p356` 13 of 64 (20.3 %), and `p357`'s single addition
raises it once more, which is the direction `T13` predicts.

🟢 **And `p357`'s one addition is the most instructive row on this table, because it
makes the hazard organisational rather than accidental.** The lower-case `license.txt`
bucket now holds **two rows and both are Frappe** — [`frappe/lms`](https://github.com/frappe/lms)
and 🆕 [`frappe/erpnext`](https://github.com/frappe/erpnext), each on a non-`main`
default branch (`develop` for both). 🔵 A grant path is not a per-repository quirk to
be rediscovered one repository at a time; **it is a house style**, and the operational
rule follows directly: when one repository in an organisation hides its grant, probe
that organisation's convention rather than the next repository's root.

### 🔴 And the default branch is the larger hazard

| Default branch | Rows |
|---|---:|
| `master` | **31** |
| `main` | 23 |
| `develop` | 3 |
| 🔴 each of `release`, `newnew`, `Version-1`, `v4.0.x-develop`, `19.0`, `mobile`, `development` | 1 |

🔴 **A probe that assumes `main` reports 41 of 64 grants (64.1 %) as absent**, and a
probe that tries `main` then `master` still misses **10**. Two of those ten are
[`QingdaoU/Judger`](https://github.com/QingdaoU/Judger) (`newnew`) and
[`mjnaderi/Sharif-Judge`](https://github.com/mjnaderi/Sharif-Judge) (`Version-1`), both
added at `p356` — and `QingdaoU/Judger` was then the sandbox at the centre of Pattern 9's
permissive path. 🔴 **Corrected `p362`: that sandbox is SATA, not MIT**, so the clause
that used to read *"the MIT sandwich"* has been rewritten to name the repository instead
of leaving a licence token next to the wrong slug. 🔵 One cause explains copyleft
prevalence, grants at `COPYING.txt` and `docs/License.txt`, and non-`main` defaults
alike: **this sector's infrastructure is older than the conventions the tooling
assumes.** Published as `T13`.

🔵 **Why that rewrite is a gate repair and not a style edit.** `gate-shelf-consistency`
read the old sentence as this shelf publishing **`MIT` for `mjnaderi/Sharif-Judge`** —
the nearest slug to the token — and reported a disagreement with the `AGPL-3.0` cell on
`verticals/solutions.md`. 🟢 **The gate was right to fire and wrong about which cell was
broken**, which is `ACTION ZZ-av`'s shape (a figure or a family bound to a slug by
proximity) reproduced on the **licence** axis for the first time. 🟢 Both underlying cells
were wrong anyway, so the gate earned its RED twice over.

## 🔵 Regional placement, counted over this shelf's own cells

🟢 **Derived as the last act before the commit, and it corrects the sentence it
replaces.**

| Region | Placed rows (`p358`) | `p357` published | `p356` published |
|---|---:|---:|---:|
| **North America** | **20** | 19 | 19 |
| **EMEA** | 16 | 16 | 16 |
| **APAC** | 12 | 12 | 🔴 11 |
| Global | 7 | 7 | 7 |
| 🔵 Not placed | **14** | 🔴 11 | 🔴 11 |
| **LATAM** | 🔴 **0** | 0 | 0 |

🟢 **Derived on `p358` with the `ZZ-bd` guard actually implemented**, not merely
registered: the census skips any table whose `Region` header sits in column 0, and
reports `rows excluded by the ZZ-bd self-table guard: 6` — the exact six-row inflation
the paragraph below predicted for this file. 🟢 `p358`'s four additions move
`North America 19 → 20` (`SanDiegoCodeSchool/lti-node-library`) and
`Not placed 11 → 14` (`lti-core`, `ltix`, `edugatorlabs/ltijs`).

🔴 **LATAM is still a hard zero on this shelf, and `p358` is the first pass that can say
why rather than that it is.** This pass ran sixteen LATAM-origin addresses and found the
tooling exists; **three of thirteen live ones carry a licence**, and all three are agents
or applications rather than *foundations* — a tutor inside Open edX, a statutory PIAR
manager, an offline test runner. 🔵 So the zero here is not the same finding as the zero
on `agents/top.md` was: there is **no LATAM-origin LMS, SIS, interop library or judge** on
this shelf because none was found licensed, and the full measurement is on
`agents/top.md` under *"What changed on `p358`"*.

🟢 **`p356`'s figures reproduced exactly on `p357`'s independently-written census
script**, and the only movement is `APAC 11 → 12` from this pass's one addition
(`frappe/erpnext`, India-origin). 🔵 **Two passes' censuses agreeing is worth
recording given the right-hand column**: `p355`'s figures were wrong in four of five
buckets, so agreement here is evidence the derivation is now sound rather than merely
repeated. 🔴 **The same self-counting trap found on `agents/top.md` applies to this
table** — a census that counts every table with a `Region` column counts this one, and
its six rows inflate all six buckets by one. `ACTION ZZ-bd` covers both files.

🔴 **Every figure in the right-hand column was wrong, and only the LATAM zero was
right.** Four of the five gaps predate this pass: before `p356` added a single row this
shelf carried **15** North American and **14** EMEA rows against published figures of
11 and 12. 🔵 **This is `ACTION ZZ-aw` on a third and fourth quantity** — a
*distribution* in prose, unbound by any gate, wrong on both shelves this pass audited
(`agents/top.md` was off by one on North America). The remedy is not care; it is a gate.

- **North America** leads at 19, concentrated in platforms, standards and — new this
  pass — **university autograding**: `otter-grader` (BSD-3-Clause, UC Berkeley, named in
  its own licence payload), `okpy/ok-client` (Apache-2.0, Berkeley) and the two DMOJ
  rows, placed by **`dmoj.ca` appearing ten times in their README**.
- **EMEA** holds 16: European universities built most of the open assessment, media and
  interoperability tooling (Belgium ×2, Croatia, France, Germany, Italy, Norway,
  Switzerland, Spain, Tanzania) and now **Iran** (`Sharif-Judge`, Sharif University of
  Technology) and **Portugal** (`fenixedu-academic`, Instituto Superior Técnico).
- **APAC** rises from 2 to **11** in one pass, and all nine new rows are **online judges
  and sandboxes** from Chinese and Japanese universities. 🔵 This is the repository-side
  half of `T15`: the region the prose legs cannot measure is the region building the
  infrastructure.
- **Global** holds 7 — the genuinely multi-region platforms (Moodle, Kolibri, Tutor).
- **LATAM** places **0 rows on this shelf**, for the *n*th consecutive pass and now with
  a sharper account of why. The function legs run this pass in Spanish and Portuguese
  returned **exam-content archives, not tooling** — FAMAF/UNC (Argentina), Instituto
  Tecnológico de Costa Rica. 🟢 So the regional supply that exists is **content**, and the
  platform layer genuinely has no LATAM-origin project this base can verify. An
  engagement there builds on EMEA or North American platforms with local curriculum data
  on top (`bncc-dados`, `mcp-brasil` — see `agents/top.md`), and that remains a pattern
  rather than a deficiency — see `compose/patterns.md`.
