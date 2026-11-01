---
industry: education
region: Global
updated: 2026-11-01
---

# Foundational open source repos for education

**What this page is.** The platform and component tier an education engagement is built
*on* — LMSs of record, interchange specs, assessment engines and the extension points that
let a studio attach proprietary AI to someone else's platform. Every row measured
first-hand **2026-11-01** (`p587`).

🟢 = permissive, shippable in client work. 🔴 = copyleft / no grant / source-available —
not shippable without counsel. **(text)** = licence read from the repository's own licence
file rather than the GitHub API, which is wrong for ~25% of rows here.

---

## The platform tier — LMSs and systems of record

| Repo | Licence | Stars | Last push | Region | Shippable? | Role |
|---|---|--:|---|---|---|---|
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 **AGPL-3.0 (text)** | **8,213** | `2026-11-01` | North America | 🔴 network copyleft | The LMS of record. 🔴 **Cite this address** — `openedx/edx-platform` is the pre-rename name and the API rejects it with `422`. |
| [moodle/moodle](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** | **7,567** | `2026-10-30` | EMEA | 🔴 copyleft | The other LMS of record; 7,690 forks. Australia-origin, EMEA-anchored governance. |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0 (text)** | **9,262** | `2026-10-31` | Global | 🔴 lesser copyleft | 🆕 **The virtual-classroom platform of record** — web conferencing purpose-built for teaching (breakouts, whiteboard, polls, recordings). 🟡 LGPL-3.0 is the mildest copyleft on this tier: a studio may **link** proprietary code against it, but modifications to BBB itself carry back. 🔴 **Default branch is `v4.0.x-develop`** — a licence probe on `main` returns `404` (see `587-D`). Re-found 18× in history and never filed. |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** | **3,360** | `2026-10-30` | APAC | 🔴 network copyleft | Frappe's LMS. India-origin, 1,566 forks. |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 **AGPL-3.0** | **2,438** | `2026-11-01` | EMEA | 🔴 network copyleft | Next-gen self-hostable learning platform; very active. |
| [classroomio/classroomio](https://github.com/classroomio/classroomio) | 🔴 **AGPL-3.0** | **1,736** | `2026-11-01` | Global | 🔴 network copyleft | Customer-training-oriented platform. |
| [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn) | 🔴 **Split grant — one part is not open source (text)** | **527** | `2026-11-01` | North America | 🔴 **no** | 🆕 **The assessment engine of record for problem-driven courses** (UIUC origin, pushed today). 🔴 Its licence file divides the repository four ways: the **Community Edition is AGPL-3.0**; **all client-side JavaScript is AGPL-3.0** *however it is served or compiled*; `apps/prairielearn/src/ee/` is the **proprietary Enterprise Edition** under its own licence; and only the portions copyright UIUC and outside contributors are **MIT**. 🔵 **Same shape as `orbit`** — permissive at the edges, copyleft-or-closed where the product is. A studio may read it; it may not ship it. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0 (text)** | **1,240** | `2026-10-30` | North America | 🟢 **yes** | 🟢 **The one platform of record a studio may lawfully fork, modify and ship.** ECL-2.0 is Apache-2.0 with the patent grant narrowed for education — its own licence text says so. Higher-ed consortium governance; 1,020 forks. |
| [codelitdev/courselit](https://github.com/codelitdev/courselit) | 🔴 **AGPL-3.0** | **1,291** | `2026-11-01` | Global | 🔴 network copyleft | Course + digital-product platform with a storefront. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** | **1,131** | `2026-10-29` | Global | 🔴 network copyleft | The Docker-based Open edX distribution. **The practical way to stand Open edX up** — the operational entry point, not a fork target. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT (text)** | **1,163** | `2026-11-01` | Global | 🟢 **yes** | 🟢 **The offline-first learning platform for low-connectivity deployments** — 1,016 forks, built for exactly the infrastructure conditions that defeat cloud LMSs. Learning Equality. **The highest-leverage permissive platform on this page for LATAM, Africa and rural APAC.** |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0** | **1,019** | `2026-11-01` | EMEA | 🔴 copyleft | LMS focused on ease of use and accessibility; strong LATAM and francophone deployment base. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0 (text)** | **903** | `2026-10-29` | APAC | 🟡 weak copyleft | 🆕 **The education ERP tier — admissions, fees, attendance, library, hostel, exams on one database.** Built as Odoo modules; India-origin. 🔴 **Cite this address**: `OpenEduCat/OpenEduCat` returns `422` and the live repo is lowercase with an `_erp` suffix, on default branch **`19.0`** (not `main`/`master`). 🟡 **LGPL-3.0 is weak copyleft** — a *separate* AI module that calls its API keeps its own licence; edits to its own files must be published. API reported `NOASSERTION`. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** | **649** | `2026-10-28` | Global | 🔴 copyleft | 🆕 Student Information System (scheduling, grades, attendance, billing). Strong francophone and LATAM deployment base. 🔵 Default branch is **`mobile`**. Relevant to gap `585-F`: the SIS tier is real but copyleft. |
| [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | 🟢 **MIT (text)** | **981** | 🔴 `2025-12-09` | APAC | 🟡 licence yes, **stale** | 🆕 LMS for asynchronous online schools with reviewed submissions. **Permissive, and the API hid it** (`NOASSERTION`). 🔴 ~11 months without a push — adopt with eyes open. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL-3.0** | **507** | `2026-10-31` | EMEA | 🔴 copyleft | Long-standing German university LMS; strong assessment module. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0 (text)** | **449** | `2026-10-30` | EMEA | 🟢 **yes** | **A second permissive platform of record.** Swiss-governed LMS used across DACH higher education, forkable and shippable. 🔴 **This base held two contradictory verdicts for this row** — `verticals/solutions.md` and `intel/trends.md` already called it Apache-2.0, while this page carried the API's `NOASSERTION`. The licence text settles it: **Apache-2.0**. |
| [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT (text)** | **437** | `2026-11-01` | North America | 🟢 **yes** | 🆕 Learning environment with versioned (git-backed) course content and auto-graded work. UIUC. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** | **410** | `2026-10-28` | Global | 🟢 **yes** | 🟢 **Permissive school-management / SIS** for small and medium institutions. Laravel + Filament. Rare: the SIS tier is otherwise copyleft. |
| [openfun/richie](https://github.com/openfun/richie) | 🟢 **MIT** | **318** | `2026-11-01` | EMEA | 🟢 **yes** | CMS for building education *portals* in front of an LMS. France Université Numérique. |
| [INGInious/INGInious](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0 (text)** | **243** | `2026-10-30` | EMEA | 🔴 network copyleft | Secure automated exercise assessment with containerised execution. UCLouvain. API said `NOASSERTION`. |
| [iblai/lms](https://github.com/iblai/lms) | 🟢 **MIT** | **208** | `2026-10-30` | Global | 🟢 **yes** | Skills-intelligence platform: competency tracking and credentials. |
| [claroline/Claroline](https://github.com/claroline/Claroline) | 🔴 **AGPL-3.0 (text)** | **349** | `2026-10-13` | EMEA | 🔴 network copyleft | Belgian-origin LMS. API said `NOASSERTION`. |
| [frappe/education](https://github.com/frappe/education) | 🔴 **GPL-3.0 (text)** | **688** | `2026-10-30` | APAC | 🔴 copyleft | School ERP on Frappe; 474 forks. 🔵 Licence at `develop/license.txt` — see the case-sensitivity note under *Method*. |

🔴 **The platform tier is predominantly copyleft — but "without exception" is false, and
this page states the exceptions.** Four platforms of record are permissive and forkable:
**Sakai** (ECL-2.0), **OpenOLAT** (Apache-2.0), **Kolibri** (MIT) and **relate** (MIT).
🟢 **Three of those four were recovered from `NOASSERTION` this pass** — Kolibri, relate
and OpenOLAT. 🔴 **And the fourth exposes a worse failure than a missing grant: this base
was publishing *contradictory* licences for the same repository on different pages.**
OpenOLAT was Apache-2.0 on `verticals/solutions.md` and `intel/trends.md` and
`NOASSERTION` here, simultaneously, for multiple passes. A per-page licence field with no
reconciliation step will do this indefinitely.

---

## The component and spec tier — permissive, and where the real leverage is

| Repo | Licence | Stars | Last push | Region | Role |
|---|---|--:|---|---|---|
| [dream-num/univer](https://github.com/dream-num/univer) | 🟢 **Apache-2.0** | **22,837** | `2026-10-31` | APAC | Sheets/docs/slides/canvas SDK — the document substrate for courseware and worksheets with no Office dependency. 1,916 forks. 🔵 Not education-specific; it is infrastructure this industry needs. |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL-1.0 (text)** — a *database* licence, new to this base | **7,489** | `2026-10-30` | Global | 🆕 **An open skills/occupation taxonomy** — the missing spine for competency mapping, course-to-job alignment and reskilling paths, which is what a corporate-learning client actually buys. 🔴 **ODbL-1.0 is not in this base's software-licence vocabulary and must not be graded as one:** it is share-alike *on derived databases*, with a produced-work clause. A studio may build a product **on** it; publishing an enriched taxonomy means publishing the enrichment. 🔵 **Counsel question, not an engineering one.** |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** | **4,121** | `2026-08-14` | Global | FSRS scheduling — the modern spaced-repetition algorithm. The retention layer for any tutor. |
| [st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 🟢 **MIT** | **2,605** | `2026-10-05` | Global | 🆕 Flashcard + whole-note review inside Obsidian. A working reference for review scheduling over existing notes. |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** | **956** | 🟡 `2025-07-03` | North America | The learning-record interchange **specification**. 🔵 Stale by date and legitimately so — a ratified spec should sit still. |
| [open-spaced-repetition/free-spaced-repetition-scheduler](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | 🟢 **MIT** | **731** | `2026-04-21` | Global | 🆕 The FSRS algorithm itself, as a library. Depend on this rather than vendoring the Anki plug-in. |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | 🟢 **Apache-2.0 (text)** | **124** | 🔴 `2024-08-20` | Global | 🆕 **The LTI 1.3 library under the standards body's own org** — 1EdTech writes the LTI specification, so this is the reference implementation, not a third-party port. 🔴 **Stale by ~26 months.** 🔵 It is the same codebase as `packbackbooks/lti-1-3-php-library`, which this base already carries: **1EdTech is where it moved**, and a pass citing the `packbackbooks` address is citing the upstream fork point. Relevant to `585-E` only by contrast — that gap is about **Python**, and this is PHP. |
| [openedx/codejail](https://github.com/openedx/codejail) | 🟢 **Apache-2.0** | **477** | `2026-10-27` | North America | 🟢 **Sandboxed execution of untrusted learner code** — the component every "run the student's program" feature needs and almost nobody builds correctly. Permissive, inside an AGPL platform. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | **471** | `2026-11-01` | North America | 🟢 **The permissive extension point into an AGPL platform** — the seam an AI component plugs into without inheriting the network-copyleft duty. |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** | **373** | `2026-10-31` | Global | LTI 1.3 tool provider in Node. The maintained way into any LMS without forking it. |
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0** | **377** | `2026-11-01` | North America | LTI tool framework and console (PHP). Authored in the IMS/Sakai lineage. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | **362** | `2026-10-28` | Global | Modern SCORM runtime in JS — the interchange seam for legacy course content. |
| [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0 (text)** | **216** | `2026-10-28` | **EMEA** | Browser-based e-assessment with a maths emphasis. **Newcastle University.** 🟢 The permissive assessment anchor to build on. |
| [Halleck45/OpenPronounce](https://github.com/Halleck45/OpenPronounce) | 🟢 **MIT** | **174** | `2026-08-15` | EMEA | 🆕 Phoneme-level English pronunciation assessment (Wav2Vec2 + DTW), self-hosted. The speaking-assessment component for language engagements. |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** | **138** | 🔴 `2024-08-18` | Global | LTI 1.3 Advantage tool for **Python**. 🔴 **~26 months stale** — and it is still the only maintainable permissive Python LTI 1.3 option. See gap `585-E`. |
| [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) | 🟢 **Apache-2.0** | **61** | 🟡 `2025-11-04` | Global | Open Badges validation — the credentialing conformance check. 1EdTech (the standards body itself). |
| [evoluteur/braille-tools](https://github.com/evoluteur/braille-tools) | 🟢 **MIT** | **43** | `2026-10-22` | Global | English Grade 1 Braille rendering in a web page; zero dependencies. 🔵 Honest scope: it renders Braille for sighted readers — **not** a transcription engine or screen-reader substitute. |
| [SafeExamBrowser/seb-win-refactoring](https://github.com/SafeExamBrowser/seb-win-refactoring) | 🔴 **MPL-2.0** | **361** | `2026-10-30` | EMEA | The sector-standard exam-lockdown client (ETH Zürich). 🔴 File-level copyleft — usable alongside, but modifications to its files stay open. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0 (text)** | **154** | `2026-10-30` | EMEA | H5P interactive content runtime — ubiquitous in Moodle/Drupal estates. 🔴 Copyleft. |

🟢 **This is where a studio's leverage actually is.** The platform tier is mostly copyleft;
the component and extension tier is permissive. **`XBlock` + `codejail` + `ltijs` /
`pylti1.3` + `scorm-again`** let a studio ship proprietary AI against an AGPL platform
without the copyleft duty reaching its own code.

---

## 🔴 Tiers not to start from

| Tier | Verdict | Evidence |
|---|---|---|
| `topic:question-generation` — the fine-tuned T5 generation tier | 🔴 **Absorbed, not neglected. Do not start here.** | All five reference rows last pushed `2023-12`–`2024-08`, one archived: `patil-suraj/question_generation` (1,138★, `2024-04-05`), `ramsrigouthamg/Questgen.ai` (952★, `2023-12-08`), `KristiyanVachev/Question-Generation` (495★, `2024-02-14`), `asahi417/lm-question-generation` (366★, `2024-08-20`), `AMontgomerie/question_generator` (298★, `2024-02-06`, **archived**). Every one is a fine-tuned T5 pipeline for a task instruction-following models now do zero-shot. 🟢 Start instead at **Numbas** (authoring), **scorm-again** (interchange), **nbgrader** (autograding) — all measured current. |
| [kantord/LibreLingo](https://github.com/kantord/LibreLingo) | 🔴 **ARCHIVED + AGPL-3.0** | 2,631★, genuinely good, `archived: true` measured `2026-11-01`. Read-only upstream: no security fixes. |
| [andymatuschak/orbit](https://github.com/andymatuschak/orbit) | 🔴 **Split licence — partly non-OSI** | 1,838★. 🆕 **Resolved this pass, and the API could not see it.** Its licence file says: most sources **Apache-2.0**; but `packages/app` and `packages/backend` are **AGPL-3.0-or-later *or* BUSL-1.1** at the licensee's choice. **BUSL-1.1 is not an open-source licence** (source-available, time-delayed conversion). 🟢 Its libraries are buildable; 🔴 its app and backend are not shippable without AGPL or BUSL compliance. 🆕 **`p586`: re-read first-hand and now reconciled with [`../agents/top.md`](../agents/top.md)**, which was simultaneously publishing this row as *"licence unresolved"* while this page called it resolved — see gap `586-A`. |

---

## Method — and the two traps that cost this base real rows

Existence, stars, forks, `archived`, `pushed_at` and `default_branch` come from
`gh api -X GET search/repositories -f q="repo:owner/name"`. 🔴 **`curl -sI` on a
`github.com` URL returns `403` for every address, real or fabricated** — re-verified this
pass — so it certifies nothing, and `gh api repos/{owner}/{name}` is `403` because this
session's GitHub access is scoped to `gmilano/globant-kb`.

🆕 **Licences come from the repository's own licence file**, which is the only ground
truth: `curl -sL https://raw.githubusercontent.com/{repo}/{default_branch}/{LICENSE}`.
This recovered **six** rows this pass that the API reported as `NONE`/`NOASSERTION`:
OpenOLAT (Apache-2.0), relate (MIT), pupilfirst (MIT), Claroline (AGPL-3.0),
INGInious (AGPL-3.0) and frappe/education (GPL-3.0) — plus `orbit`'s split licence, which
no single-value API field could have represented.

🆕 **`p586` added a third channel: topic facets.** `search/repositories -f q="topic:ai-education"` and
`topic:ai-tutor`, sorted by stars, surfaced rows that name/description search had missed across
twenty passes — including `hugohe3/ppt-master` (MIT, **71,803★**), which is larger than any repo this
base held. 🔴 **A base that only re-measures what it already holds cannot find what it is missing**;
topic facets are how this industry self-labels, and they are cheap.

🔴 **Trap 1 — the path is case-sensitive and the branch is often neither `main` nor
`master`.** `frappe/education` reported "no licence file" against nine filenames on
`main`+`master`; its grant is at **`develop/license.txt`** — lowercase, on a third branch.
🟢 **The fix is to take `default_branch` from the same search call** that confirms
existence, then probe case variants. A `404` from this channel means *"not at this path"*,
never *"no licence"* and never *"no repository"*.

🔴 **Trap 2 — `422` is overloaded.** It is returned both for a repository that does not
exist and for a repository that has been **renamed**, and OR-batching `repo:` qualifiers
makes one bad qualifier zero the whole batch. Use single calls, and resolve an unexpected
`422` by searching the org for the name before recording the row as dead.

---

## 🔴 Open gaps

| Gap | Status | What would close it |
|---|---|---|
| `586-A` 🔴 **REFUTED `p587` — the step exists and blocks commits** | 🔴 **REFUTED** | The step is `gate-shelf-consistency` (`Makefile:660`, 59 controls, in `HOOK_GATES`), and two further sweeps exist (`p121`, `p538`). `586-A` was filed on both this page and [`../agents/top.md`](../agents/top.md) asserting it did not exist. 🔵 Full account, including the 10 false positives a naive rebuild produced, is at `587-A` on [`../agents/top.md`](../agents/top.md). |
| `587-E` 🔴 **The licence vocabulary on these pages has no slot for a DATA licence, and a 7,489★ row now needs one** | 🆕 Opened `p587` | `withmarbleapp/os-taxonomy` is **ODbL-1.0**. Every grading rule in this base maps a token to 🟢 permissive / 🔴 copyleft on the assumption it governs **code**; ODbL governs a **database**, with share-alike on *derived databases* and a separate *produced work* clause. 🔴 Grading it 🔴 would wrongly block a buildable asset; grading it 🟢 would wrongly promise a clean ship. It is filed 🟡 with the mechanism written out. **What would close it:** a third axis — code grant / data grant / content grant — since this base already holds two content-grant anomalies (`nextgen-ai` *"MIT (Code)"*, and `gen-mentor` at CC0-1.0). |
| `587-F` 🔴 **Two addresses this base has re-found 31 times between them do not exist** | 🆕 Opened `p587` | `foradian/fedena` (**17** re-finds in the append-only logs) returns no row at all; the live org is `projectfedena`, whose `fedena` is **547★, licence `NONE`, last pushed `2020-05-18`**. `mitodl/open-learning-ai-tutor` (**14** re-finds) likewise returns nothing; the nearest live address in that org is `mitodl/tutor-mentor`, **0★**, last pushed `2023-10-20`. 🟢 Both were resolved by **org search**, which is `p586`'s own rule for a `422`. 🔵 **Neither was ever promotable** — which is the honest other half of this pass's promotion finding: the backlog is not a queue of missed gems. |
| `586-A` 🆕 **No cross-page reconciliation step — and it produced a contradiction at `p585`** | 🆕 Opened `p586` | This page resolved `orbit`'s split licence at `p585`; `agents/top.md` opened `585-C` calling the same repo *unresolved* **in the same pass**. `p585` correctly named the missing reconciliation step as the cause of contradictory licence fields, then produced another instance of it. 🟢 Reconciled by re-reading the licence text. 🔴 **The step still does not exist**: a pre-commit `grep` of every curated page for each repo address would close it. |
| `586-B` 🆕 **Duplicate gap IDs across pages** | 🆕 Opened `p586` | The proctoring gap is `585-G` here and `585-B` on `agents/top.md` — two IDs, one gap. Allocate gap IDs once per base, not once per page. |
| `586-D` 🆕 **The ERP/SIS tier has no permissive option at any size** | 🆕 Opened `p586` | Measured `2026-11-01`: `openeducat_erp` **LGPL-3.0** (903★), `frappe/education` **GPL-3.0** (688★), `rosariosis` **GPL-2.0** (649★). The only permissive row is `academico-sis/academico` (MIT, 410★) and it is school-management, not an ERP. 🟢 **The usable consequence**: LGPL-3.0 on `openeducat_erp` means a studio's AI module stays proprietary **provided it is a separate module calling the API** — so the play here is an AI side-car, never a fork. |
| `585-E` **Python LTI 1.3 has no maintained permissive option** | Open, re-measured | `pylti1.3` (MIT, 138★) is ~26 months stale and is still the best option. 🟢 This is the cheapest **contribution play** available in this industry: reviving it costs less than a fourth implementation and buys standing with the standards community. |
| `585-F` **The SIS tier is thin on permissive options** | Open | `academico-sis/academico` (MIT, 410★) is the only permissive SIS of any size found. Everything larger is copyleft. |
| `585-G` **No permissive proctoring platform exists** | Open | SafeExamBrowser is MPL-2.0 and is the sector standard; there is no permissive equivalent. A studio composes SEB + an agent rather than adopting a platform. |

---

## History

Pass-by-pass narrative for `p577`–`p584` is preserved at
[`../archive/2026-11-01-p585-pre-consolidation/repos-foundations.md`](../archive/2026-11-01-p585-pre-consolidation/repos-foundations.md);
the append-only discovery log is [`./trending.md`](./trending.md).

🔴 **Why this page was consolidated at `p585`.** It had grown to 1,646 lines of
reverse-chronological pass narrative, and the same stale address
(`openedx/edx-platform`) appeared 40 times against 28 for the live one. A page that
restates its own history eight times cannot be audited for stale citations.
