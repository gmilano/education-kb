---
industry: education
region: Global
updated: 2026-11-02
---
## 🆕 `p615` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THE INTEROPERABILITY TIER, BYTE-READ AS A POPULATION FOR THE FIRST TIME: `8` LIVE PERMISSIVE ROWS (`7` `Apache-2.0`, `1` `MIT`) AND `8` ARCHIVED ONES — INCLUDING THE CANONICAL SCORM→xAPI BRIDGE, WHICH IS BOTH **ARCHIVED AND UNGRANTED**.**

### 🟢 `615-E` — the xAPI reference tier: what is alive, permissive and safe to build on

🔵 Every row below was already on this base's shelves. 🟢 What is new is that the tier has been read
as a **population**, with its archival state and its grant bytes measured in the same sweep.

| repo | rounded ★ | grant | bytes | branch | what it is, and when a studio reaches for it |
| --- | --: | --- | --: | --- | --- |
| [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | `956` | 🟢 `Apache-2.0` | `11,525 B` | `master` | The xAPI specification itself. 🟢 The normative reference for any learning-analytics brief |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | `334` | 🟢 `Apache-2.0` | `11,357 B` | `master` | Reference **Learning Record Store** (Python). 🟢 A permissive LRS you can host — the piece clients assume must be bought |
| [`adlnet/xAPIWrapper`](https://github.com/adlnet/xAPIWrapper) | `224` | 🟢 `Apache-2.0` | `10,273 B` | `master` | The JS client most xAPI integrations actually start from |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | `78` | 🟢 **`MIT`** | `1,046 B` | `master` | 🟢 Conformance harness — the tier's **only `MIT`** row, and the one that lets a studio *prove* an integration rather than assert it |
| [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) | `60` | 🟢 `Apache-2.0` | `11,357 B` | `master` | Profile specification and tooling — how a sector vocabulary is pinned down |
| [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) | `59` | 🟢 `Apache-2.0` | `11,358 B` | 🔵 `main` | **cmi5** reference suite. 🔵 The tier's only `main` branch |
| [`adlnet/xapi-ontology`](https://github.com/adlnet/xapi-ontology) | `18` | 🟢 `Apache-2.0` | `11,525 B` | `master` | RDF/OWL ontology for xAPI |
| [`adlnet/MasterObjectModel`](https://github.com/adlnet/MasterObjectModel) | `12` | 🟢 `Apache-2.0` | `11,525 B` | `master` | TLA data model |

🟢 `8 of 8` grants byte-read `2026-11-02` at the branch `git ls-remote --symref` reported.
`commercial_use_ok` returns `ALLOWED` on all `8` through `compose/code/lib/license_family.sh`.

### 🔴 `615-E` (b) — the two gaps in the tier, and they are exactly where the work lands

| archived address | rounded ★ | consequence |
| --- | --: | --- |
| [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | `99` | 🔴 **Archived *and* ungranted** — the grant ladder exhausted `7` names at `master`. The canonical legacy-migration bridge is unmaintained and unshippable |
| [`adlnet/Unity-xAPI-Wrapper`](https://github.com/adlnet/Unity-xAPI-Wrapper) | `32` | 🔴 Archived. The **only game-engine binding** in the tier — so simulation and VR-training briefs have no maintained reference path |

🟢 **Read it as a budget line, not a disappointment.** The spec, LRS, client, conformance suite and
profile tooling are live and permissive, so the *backbone* is adoptable. 🔴 The **SCORM migration
path** and the **engine binding** must be budgeted as a build. 🔵 Six further archived rows
(`xapi-authored-profiles` `45`, `xAPI-SCORM-Profile` `42`, `xapi-launch` `41`,
`xapi-statement-viewer` `28`, `xAPI-Workshop` `23`, `xapi-jqm` `21`) are recorded in the evidence
file so a successor does not re-probe them.

### 🔴 `615-D` — stars in this section are **rounded**, by channel failure, not by choice

`api.github.com` and `github.com` HTML are `HTTP 403` to this egress; `raw.githubusercontent.com`
and `git ls-remote` answer. 🟢 Hence: **grants byte-exact, stars rounded.** No `archived` flag came
from the platform either — archival state above is read from the org's rendered repository list, and
is therefore a **display** reading, not an API field.
`evidence/channel-availability.2026-11-02-p615.tsv`.

## 🆕 `p614` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THE CLASSROOM-DELIVERY TIER, WHICH THIS BASE HAD NO ROW FOR: A REAL-TIME COLLABORATIVE IDE (`MIT`, `262★`), A MICROSITE CMS FROM PENN STATE (`Apache-2.0`), AND THE LITERACY-CONTENT STACK THAT PLACES A ROW IN **EMEA** RATHER THAN GLOBAL. 🟢 `4` ROWS, `4 of 4` GRANTS BYTE-READ AGREEING WITH THE PLATFORM FIELD.**

### 🟢 `614-J` — what a learner and a teacher actually touch, which is neither an LMS nor an agent

🔵 **Why this is a gap and not a nice-to-have.** `612-D` shelved how a tool **launches** from a
copyleft LMS (LTI `1.3`), `613-B`/`613-C` shelved how it **reports back** (xAPI, LRS, cmi5
conformance). 🔴 Both seams are plumbing. Neither answers *what is on the screen during the lesson* —
and that is the part a client sees in a demo. 🟢 These four rows are that layer, and all four are
permissive, which the LMS layer itself is not.

| repo | ★ | grant (byte-read) | path | branch | pushed | region | why it is load-bearing |
| --- | --: | --- | --- | --- | --- | --- | --- |
| [`SJRiz/pytogether`](https://github.com/SJRiz/pytogether) | `262` | 🟢 `MIT` `1,073 B` | `LICENSE` | `main` | `2026-10-21` | Global | 🟢 **Browser-based collaborative IDE** — real-time co-editing, live drawing and voice chat, running at `pytogether.org`. 🔵 The highest-starred permissive row this base holds for *synchronous* teaching: a CS classroom where the instructor draws on the same buffer the student types in |
| [`haxtheweb/haxcms-php`](https://github.com/haxtheweb/haxcms-php) | `130` | 🟢 `Apache-2.0` `11,362 B` | `LICENSE.md` | 🔴 `master` | 🟢 `2026-11-02` | 🟢 North America | **HAX + CMS** for a *microsite universe* with a PHP backend — from **Penn State**, an institution rather than a single author, which is the provenance an education procurement prefers. 🟢 Pushed today. 🔴 Default branch is `master`, so a `main`-only reader publishes it as ungranted (`611-C` class) |
| [`langx/langx`](https://github.com/langx/langx) | `109` | 🟢 `BSD-3-Clause` `1,520 B` | `LICENSE` | `main` | `2026-10-31` | Global | Language-learning app connecting learners for live practice. 🟢 **`BSD-3-Clause`** — only the second `BSD` row on this shelf, and the family with the shortest notice obligation of the three permissive ones |
| [`elimu-ai/webapp`](https://github.com/elimu-ai/webapp) | `41` | 🟢 `MIT` `1,065 B` | `LICENSE` | `main` | `2026-10-27` | 🟢 **EMEA** | Hosts Android applications and educational content for **early-grade literacy**, aimed at out-of-school children. 🟢 The pass's one genuinely **region-placed** supply row: a Sub-Saharan deployment target, which is EMEA by this base's closed vocabulary, with the country in this sentence rather than in the field |

🔴 **Stated limits, on the shelf and not in a footnote.** `elimu-ai/webapp` is `41★` and
single-organisation — it is a *content-delivery* reference, not a platform to resell. `langx/langx`
is a consumer social app whose education use is adjacent rather than designed. `pytogether` is one
author; its value is the demonstrated architecture, and a studio should expect to own the fork.

### 🟢 `614-B` — `ECL-2.0` is **not** confined to the Apereo orgs, and outside them the platform field is **right**

🔵 `604-A` swept four Apereo-family orgs (`91` repos, `61` grants byte-read) and closed that *"the API
is wrong about `ECL-2.0` in `10 of 11` repos (`90.9 %`)"* — a figure this base has carried since as a
property of the **licence**. 🔴 Measured here: that is a property of those **owners**.

| address | ★ | platform field | grant on bytes | branch | org in `604-A`'s sweep? | verdict |
| --- | --: | --- | --- | --- | --- | --- |
| [`opencast/annotation-tool`](https://github.com/opencast/annotation-tool) | `42` | 🟢 `ECL-2.0` | 🟢 **`ECL-2.0`** `11,340 B` | 🔴 `master` | 🔴 **No** — a fifth publisher | 🟢 **API CORRECT.** `1 of 1` outside the Apereo orgs |

🔵 **A second, independent data point in the same direction, from this pass's own provenance check on
`haxcms-php`.** HAX is developed at **Penn State** (College of Arts and Architecture) and is listed by
the **Apereo Foundation** under its software programs — so it is an *Apereo-associated* project that
nonetheless publishes under 🟢 `Apache-2.0`, not `ECL-2.0`, and its field reads correctly. 🟢 That cuts
against reading `604-A` as a statement about the Apereo **ecosystem**: the defect tracks the four
specific orgs that sweep covered, not the foundation.

🟢 **Rule revised, with the revision bounded.** `604-A`'s `90.9 %` error rate stands *for the Apereo
orgs* and must be cited that way from now on. 🔵 On the one publisher measured outside them the field
is accurate, so `ECL-2.0` is not intrinsically invisible to the platform — those orgs' grant files
are. 🟢 This is **`613-A`'s owner rule arriving from a second direction**: group by owner before
generalising, whether the subject is a dead address or a licence-metadata defect. 🔴 Limit: `n = 1`
outside Apereo. This narrows `604-A`'s scope; it does not replace its number.

🔵 **And `opencast` is worth the row on its own merits** — a video annotation service for research,
teaching and learning, from the Opencast academic consortium (European universities, which places the
*publisher* in EMEA even though the software is used globally).

### 🔵 Standing: the tiers this pass did **not** move, so a reader is not misled by a short section

🟢 `612-D` LTI `1.3` (`5` stacks), `613-B` xAPI/cmi5 conformance (`9` repos, US DoD ADL),
`613-C` LRS + simulation (`5` repos), `613-D` FSRS scheduling (`8` stacks) are all unchanged and
un-re-read this pass except where a row below cites them. 🔵 Two already-shelved addresses the sweep
re-surfaced and this pass deliberately did **not** re-promote: `tsugiproject/tsugi` (`Apache-2.0`,
`377★`, pushed `2026-11-02`) and `jcputney/scorm-again` (`MIT`, `362★`) — both already carry sell-shelf
cells. 🟢 Recorded here so their appearance in the sweep is not read as a new find.

## 🆕 `p613` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THE TELEMETRY HALF OF THE SEAM: `612-D` SHELVED HOW A TOOL **LAUNCHES** FROM AN LMS; THIS PASS SHELVES HOW IT **REPORTS BACK**, AND IT IS `Apache-2.0` ALL THE WAY DOWN, PUBLISHED BY THE US DoD's ADL INITIATIVE. 🟢 PLUS A COMPLETE **POLYGLOT SCHEDULING TIER** (`8` LANGUAGES, `MIT`/`BSD-3`), THE ALGORITHM `612`'S OWN TOP AGENT ROW ALREADY DEPENDS ON. `24 of 24` GRANTS BYTE-READ AGREE WITH THE PLATFORM FIELD.**

### 🟢 `613-C` — the xAPI telemetry tier: a permissive Learning Record Store, and the simulator to load-test it

🔵 **Why this is the load-bearing row, not a nice-to-have.** `612-D` established that LTI is the
commercial boundary, because both incumbents are copyleft (Moodle `GPL-3.0`, Open edX `AGPL-3.0`) and
LTI is the permissive seam a tool launches through. 🔴 But a launch seam alone cannot answer the only
question an education client actually buys: *did the learner learn anything, and can you prove it?*
🟢 That is xAPI, and the store it writes to is an **LRS** — and there is a permissive, actively
maintained one.

| repo | ★ | grant (byte-read) | path | branch | pushed | region | what it is |
| --- | --: | --- | --- | --- | --- | --- | --- |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | `144` | 🟢 `Apache-2.0` `11,357 B` | `LICENSE` | `main` | `2026-10-27` | 🟢 North America | 🟢 **A SQL-based Learning Record Store** — the permissive system of record for learner evidence. Published by Yet Analytics, a commercial xAPI vendor, which is the rarer vendor-owned-and-permissive combination `612` flagged on `instructure/ims-lti` |
| [`openfun/ralph`](https://github.com/openfun/ralph) | `51` | 🟢 `MIT` `1,094 B` | `LICENSE.md` | `main` | `2026-11-01` | 🟢 EMEA | LRS **and** learning-analytics toolbox from **France Université Numérique**, the French state's higher-education digital operator. 🟢 Pushed yesterday. Second state-published EMEA row in two passes after `612-F`'s UK DfE |
| [`yetanalytics/datasim`](https://github.com/yetanalytics/datasim) | `23` | 🟢 `Apache-2.0` `11,357 B` | `LICENSE` | 🟡 `master` | `2026-10-16` | 🟢 North America | 🟢 **xAPI data simulation** — generates conformant statement volume from a profile. This is how you load-test and demo an LRS before a single real learner exists, which is the week-one blocker on every analytics engagement |
| [`xapijs/xapi`](https://github.com/xapijs/xapi) | `51` | 🟢 `MIT` `1,071 B` | `LICENSE.md` | 🔴 `develop` | `2026-04-29` | Global | The JS/TS client for talking xAPI from a browser or Node tool |
| [`xapijs/cmi5`](https://github.com/xapijs/cmi5) | `25` | 🟢 `MIT` `1,070 B` | `LICENSE.md` | 🔴 `develop` | `2026-04-01` | Global | The same client narrowed to the **cmi5** profile — the packaging contract that replaces SCORM |

🟡 **Stated limit.** `xapijs/*` has not been pushed since `2026-04`; both are small client libraries where
that is survivable, but neither is a maintained dependency in the sense `lrsql` and `ralph` are.

### 🟢 `613-D` — the scheduling tier: `8` languages, one algorithm, and `612` was already selling it

🔵 `p612` promoted `HumphreySun98/Smart-Study-Agent` and called its division of labour *"the cleanest on
this shelf"* — **RL picks the action, FSRS picks the timing, the LLM only writes the quizzes.** 🔴 This
base shelved the agent and never shelved **FSRS**, the scheduler the praise was actually about. It is a
complete permissive implementation tier, one per stack, in the shape `612-D` found for LTI.

| repo | ★ | grant (byte-read) | path | branch | pushed | stack |
| --- | --: | --- | --- | --- | --- | --- |
| [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | `4,122` | 🟢 `MIT` `1,079 B` | `LICENSE` | `main` | `2026-08-14` | 🟢 The reference scheduler, and the highest-starred row this pass touched |
| [`open-spaced-repetition/ts-fsrs`](https://github.com/open-spaced-repetition/ts-fsrs) | `847` | 🟢 `MIT` `1,079 B` | `LICENSE` | `main` | `2026-10-29` | TypeScript / ESM |
| [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | `520` | 🟢 `MIT` `1,079 B` | `LICENSE` | `main` | `2026-08-09` | Python |
| [`open-spaced-repetition/fsrs-rs`](https://github.com/open-spaced-repetition/fsrs-rs) | `455` | 🟢 `BSD-3-Clause` `1,509 B` | `LICENSE` | `main` | `2026-10-28` | Rust — optimizer **and** scheduler |
| [`open-spaced-repetition/go-fsrs`](https://github.com/open-spaced-repetition/go-fsrs) | `157` | 🟢 `MIT` `1,079 B` | `LICENSE` | `main` | `2026-10-31` | Go |
| [`open-spaced-repetition/fsrs-optimizer`](https://github.com/open-spaced-repetition/fsrs-optimizer) | `112` | 🟢 `BSD-3-Clause` `1,509 B` | `LICENSE` | `main` | `2026-08-06` | 🟢 Fits the algorithm's parameters **to one learner's own review history** — the personalisation step |
| [`open-spaced-repetition/swift-fsrs`](https://github.com/open-spaced-repetition/swift-fsrs) | `107` | 🟢 `MIT` `1,066 B` | `LICENSE` | `main` | `2026-05-25` | Swift / iOS |
| [`duolingo/halflife-regression`](https://github.com/duolingo/halflife-regression) | `584` | 🟢 `MIT` `1,070 B` | `LICENSE.md` | 🟡 `master` | 🔴 `2024-04-20` | 🔵 **Duolingo's own** published spaced-repetition model. Permissive and citable; 🔴 unmaintained since `2024`, so it is a baseline to benchmark against, not a dependency |

🟢 **Why a scheduling tier is commercially different from a tutor.** A tutor is a prompt and is copied in
a week. A scheduler is a fitted model over a learner's review history: it improves with retained data,
which is the one asset an incumbent LMS cannot hand to a competitor. 🔵 `fsrs-optimizer` is the row that
makes that concrete.


## 🆕 `p612` — reads `2026-11-02`, commit `2026-11-02` — **🟢 TWO WHOLE **TIERS** WERE SITTING IN THE BACKLOG, NOT TWO ROWS: A FIVE-LANGUAGE PERMISSIVE **LTI 1.3 / LTI ADVANTAGE** INTEGRATION TIER (RUBY, PYTHON, JAVA/SPRING, .NET, TYPESCRIPT) AND A SEVEN-REPOSITORY **RUBRIC / AUTOGRADING** TIER. 🔵 THE FIRST IS HOW ANYTHING GLOBANT BUILDS REACHES A LEARNER AT ALL; THE SECOND IS THE ANNEX III CONFORMITY ARTEFACT. `18` FOUNDATION ROWS PROMOTED.**

### 🟢 `612-D` — the integration tier: `5` permissive LTI implementations, one per stack, none previously shelved

🔵 **Why this is a tier and not a list.** Every education engagement answers the same week-one question
before it writes a feature: *how does our thing appear inside the institution's LMS?* The answer in this
sector is **LTI** — `1.3` / Advantage — and it is non-negotiable, because Moodle (`GPL-3.0`) and
Open edX (`AGPL-3.0`) are the incumbents and neither licence lets a client's proprietary code live
*inside* them. 🟢 LTI is the seam that keeps the client's code out of the copyleft boundary. 🔴 This base
has shelved tutors and quiz generators for `611` passes and never shelved the seam.

🟢 All five grants byte-read `2026-11-02` at the real default branch.

| LTI implementation | ★ | grant (byte-read) | path | branch | pushed | stack | why this one |
| --- | --: | --- | --- | --- | --- | --- | --- |
| [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | `203` | 🟢 `MIT` `1,068 B` | `LICENSE.txt` | `main` | `2026-10-02` | Ruby | 🟢 Published by **Instructure itself** — the Canvas vendor's own tool-consumer/provider library |
| [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | `73` | 🟢 `BSD-3-Clause` `1,528 B` | `LICENSE` | `main` | `2026-10-05` | Python | Launches **JupyterHub** from an LMS — the path for any notebook-based course |
| [`harvard-edtech/caccl`](https://github.com/harvard-edtech/caccl) | `35` | 🟢 `MIT` `1,075 B` | `LICENSE.md` | `main` | `2026-10-28` | TypeScript | Harvard's all-in-one Canvas connector: LTI **＋** authorisation **＋** API in one library |
| [`LtiLibrary/LtiAdvantagePlatform`](https://github.com/LtiLibrary/LtiAdvantagePlatform) | `35` | 🟢 `MIT` `1,068 B` | `LICENSE` | 🟡 `master` | `2026-10-28` | .NET | A reference **platform** (not tool) side — the half you need to test your tool against |
| [`oxctl/spring-security-lti13`](https://github.com/oxctl/spring-security-lti13) | `25` | 🟢 `Apache-2.0` `11,358 B` | `LICENSE.txt` | 🟡 `master` | `2026-10-06` | Java / Spring | 🟢 EMEA — LTI `1.3` on Spring Security's existing OAuth2 support, so it inherits an audited auth stack |

🔵 **Read the star column and then ignore it.** `25`–`203★` across the tier. 🟢 `601` already established
that in education star rank is an **anti**-signal for commercial usability; this is the strongest case
yet — the five repositories that decide whether a deliverable can be *installed* sit two orders of
magnitude below the tutoring demos that trend.

### 🟢 `612-E` — the rubric / autograding tier: `7` permissive repositories, and they are the EMEA compliance artefact

🔵 Annex III of the AI Act makes a system **high-risk** when it *"evaluates learning outcomes"*. 🔴 The
`2027-12-02` deferral (see `intel/market.md`) does not change the obligation, only the date: risk
management, data governance, technical documentation and **human oversight** still have to exist.
🟢 A weighted, versioned, evidence-linked rubric is what turns "the model graded it" into a documented
decision procedure with a human in it — which is to say, 🟢 **this tier is not a nice-to-have feature,
it is the conformity evidence.**

| repository | ★ | grant (byte-read) | path | branch | pushed | region | role in the tier |
| --- | --: | --- | --- | --- | --- | --- | --- |
| [`alphadl/AdaRubrics`](https://github.com/alphadl/AdaRubrics) | `368` | 🟢 `Apache-2.0` `10,761 B` | `LICENSE` | `main` | `2026-08-24` | Global | Adaptive **dynamic** rubric evaluator over agent *trajectories* — grades the process, not only the answer |
| [`gpoore/text2qti`](https://github.com/gpoore/text2qti) | `241` | 🟢 `BSD-3-Clause` `1,522 B` | `LICENSE.txt` | 🟡 `master` | `2026-08-21` | Global | Markdown → **QTI**, the interchange format Canvas and most LMSs import. 🟢 The least glamorous row here and the one that makes output *deliverable* |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | `161` | 🟢 `BSD-3-Clause` `1,560 B` | `LICENSE` | 🟡 `master` | `2026-11-01` | 🟢 North America | UC Berkeley Data Science's Python **and R** autograder — containerised, used at course scale, pushed yesterday |
| [`Sion612/rubrictrail`](https://github.com/Sion612/rubrictrail) | `130` | 🟢 `Apache-2.0` `11,324 B` | `LICENSE` | `main` | `2026-10-30` | Global | Local-first, 🟢 **evidence-linked** assignment planner — the audit trail an Annex III file needs |
| [`paper-instruments/rubric`](https://github.com/paper-instruments/rubric) | `86` | 🟢 `MIT` `1,077 B` | `LICENSE` | `main` | `2026-10-27` | Global | **Weighted**-rubric LLM evaluation as a plain Python library — the component to embed |
| [`webtech-network/autograder`](https://github.com/webtech-network/autograder) | `63` | 🟢 `Apache-2.0` `11,357 B` | `LICENSE` | `main` | `2026-10-20` | Global | Grades submissions **and generates the report** — the report is the human-oversight surface |
| [`OpenEnvision/AutoRubric-as-Reward`](https://github.com/OpenEnvision/AutoRubric-as-Reward) | `59` | 🟢 `Apache-2.0` `10,757 B` | `LICENSE` | `main` | `2026-09-25` | Global | Derives **explicit generative criteria** from implicit preference — how to get a defensible rubric out of expert judgements that were never written down |

### 🟢 `6` further foundation rows — platform, analytics and ingestion

| repository | ★ | grant (byte-read) | path | branch | pushed | region | what it gives an engagement |
| --- | --: | --- | --- | --- | --- | --- | --- |
| [`jdepoix/youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) | `8,546` | 🟢 `MIT` `1,069 B` | `LICENSE` | 🟡 `master` | `2026-10-30` | Global | Transcript ingestion with **no API key and no headless browser** — the cheapest content intake there is |
| [`fairlearn/fairlearn`](https://github.com/fairlearn/fairlearn) | `2,306` | 🟢 `MIT` `1,168 B` | `LICENSE` | `main` | `2026-10-24` | Global | 🟢 Fairness **assessment and mitigation**. Annex III high-risk education systems need a documented bias position; this is the library that produces one |
| [`moodlehq/moodleapp`](https://github.com/moodlehq/moodleapp) | `1,004` | 🟢 `Apache-2.0` `11,358 B` | 🟡 `COPYING.txt` | `main` | `2026-10-29` | Global | 🟢 **The official Moodle app is `Apache-2.0` while Moodle core is `GPL-3.0`.** The permissive surface of a copyleft incumbent is its mobile client — that is where a client's own code can live. 🔵 Its grant is the `COPYING.txt` rung `610-E` had to add |
| [`walt-id/waltid-identity`](https://github.com/walt-id/waltid-identity) | `324` | 🟢 `Apache-2.0` `11,357 B` | `LICENSE` | `main` | `2026-11-02` | Global | Identity **and wallet** toolkit — verifiable credentials for diplomas, micro-credentials and transcript portability |
| [`Azure/Moodle`](https://github.com/Azure/Moodle) | `186` | 🟢 `MIT` `1,090 B` | `LICENSE` | 🟡 `master` | `2026-11-02` | Global | Scalable Moodle **cluster** tooling. 🟡 Stated limit: it is Azure-specific; the topology transfers, the templates do not |
| [`tl-its-umich-edu/my-learning-analytics`](https://github.com/tl-its-umich-edu/my-learning-analytics) | `37` | 🟢 `Apache-2.0` `11,379 B` | `LICENSE` | 🟡 `master` | `2026-10-27` | 🟢 North America | **MyLA**, University of Michigan — a student-facing learning-analytics dashboard a public university actually runs |

🟢 **Controls `2 of 2` `UNREACHABLE`** in the same run (`openai/totally-not-real-edu-repo-p612`,
`anthropics/fabricated-control-p612-<epoch>`). Instrument `ingest/p612-grant-gate.sh`; evidence
`evidence/api-vs-bytes-grants.2026-11-02-p612.tsv`.

---

## 🆕 `p611` — reads `2026-11-02`, commit `2026-11-02` — **🟢 THE FIRST PERMISSIVE **PROVINCIAL** SYSTEM OF RECORD ON THESE SHELVES: A CANADIAN MINISTRY'S STUDENT-FINANCIAL-AID PLATFORM, `Apache-2.0`, BUSINESS-RULES ENGINE INCLUDED, PUSHED `2026-10-31`. 🔴 AND THE DISCOVERY CHANNEL IS MEASURED RATHER THAN DECLARED: `976` ADDRESSES ACROSS `19` AXES, `91.6 %` NEW TO THIS BASE AND ONLY `4.7 %` SHIPPABLE-SHAPED — `14 of 19` AXES YIELD **ZERO**.**

### 🟢 `611-D` — `bcgov/SIMS`: the public-sector tier gains a permissive system of record

🔵 `p448` recorded that *"the NA research unit is the **state**"* and returned this base's first
permissively-licensed system of record. 🟢 This pass returns the **provincial** instance of that same
shape, and it is larger and live:

| axis | reading, byte-read `2026-11-02` |
| --- | --- |
| address | [`bcgov/SIMS`](https://github.com/bcgov/SIMS) |
| grant | 🟢 **`Apache-2.0`**, `11,358 B`, `LICENSE` at `main` |
| owner | 🟢 **Government of British Columbia** (`bcgov`) — a ministry, not a vendor |
| what it is | Student Information Management System: 🟢 **replaces the province's student financial-aid systems** for student, institution and ministry users |
| 🟢 why it matters beyond a loan portal | it ships a **business rules engine** *"that can accommodate regular changes in alignment with policy"* |
| state | `29★`, `15` forks, `53.7 MB`, pushed 🟢 `2026-10-31`, lifecycle badge **Maturing** |

🔵 **Why a `29★` row outranks most four-figure ones here.** The scarce artefact in education is not a
tutor — it is a **permissively-licensed system of record with a policy engine**, owned by a government
that publishes it. 🟢 Star count measures developer attention; this measures *procurement precedent*.
🔵 And `601` already established that in this sector star rank is an **anti**-signal for commercial
usability.

🟡 **Stated limit:** it implements **British Columbia** financial-aid policy. The reusable assets are
the rules-engine architecture, the three-party (student / institution / ministry) domain model and the
Apache-2.0 grant — not the policy content.

### 🔴 `611-E` — the discovery channel, measured: high novelty and low yield are the same number

🔵 The run prompt mandates four global legs. They were run, plus `15` further axes.
Evidence: `evidence/discovery-novelty.2026-11-02-p611.tsv`.

| | `p611` |
| --- | --: |
| distinct axes queried | `19` |
| distinct addresses returned | `976` |
| 🟢 **new** to this `3,758`-address base | 🟢 `894` (**`91.6 %`**) |
| 🟡 new **and** permissive | 🟡 `196` (`20.1 %`) |
| 🔴 new, permissive **and** `≥ 10★` | 🔴 **`46` (`4.7 %`)** |
| 🔴 axes yielding **zero** shippable-shaped rows | 🔴 **`14 of 19`** |

🔴 **So the forty-first global nil is not a dry channel — it is a channel that returns `91.6 %` novelty
with almost none of it usable.** 🟢 This sharpens `601`'s reconciliation of `p600`'s `80.3 %` against
`p599`'s `0 %`: novelty and value are **independent axes**, and this pass separates them in one table.
🔵 What `91.6 %` actually measures on a generic axis is the **long tail of coursework** — the modal new
address is a one-student CRUD project at `0★`.

🟢 **The five axes that did pay** were `topic:education topic:ai` (`25`), `student information system`
(`15`), `rubric grading agent` (`3`), `edutrac` (`2`) and `pendidikan AI indonesia` (`1`) — 🔵 and the
last one is the pattern `p600` named: **a local-language axis phrased as a school subject.**

---

## 🆕 `p610` — reads `2026-11-02`, commit `2026-11-02` — **🟢 `5` FOUNDATION ROWS AND A `5`-ROW **LMS-CONNECTOR** TIER, EVERY GRANT BYTE-READ TODAY AT THE REAL DEFAULT BRANCH. 🟢 THE QTI TIER NOW HAS AN **AUTHORING** END — BSD-3-CLAUSE — SO `p607`'s ENGINE IS REACHABLE FROM MARKDOWN. 🔴 `610-E`: THIS PASS'S OWN GRANT LADDER OMITTED `COPYING.txt` AND GRADED THE **OFFICIAL MOODLE MOBILE APP** UNGRANTED — A RUNG THIS BASE REGISTERED AT `~p460`. 🟢 `4` OF THE CONNECTOR ROWS CLOSE DEBT `609-C` ENUMERATED BY NAME.**

### 🟢 The assessment stack is now permissive from authoring to delivery

🟡 `p604` shelved a QTI 3.0 toolchain. 🟢 `p607` found the **engine** (`OpenOLAT/qtiworks`,
BSD-3-Clause). 🔴 Neither gave an **authoring** path: every recipe here began with a QTI file that had
to already exist.

| stage | before `p610` | 🆕 `p610` |
| --- | --- | --- |
| authoring | 🔴 **none — hand-written XML** | 🟢 [`gpoore/text2qti`](https://github.com/gpoore/text2qti) — **BSD-3-Clause** `1,522 B` |
| engine / delivery | 🟢 `OpenOLAT/qtiworks` (BSD-3-Clause) | unchanged |
| 🟢 copyleft boundary in the path | — | 🟢 **none, end to end** |

### 🟢 New foundation rows — grants byte-read `2026-11-02`, `4 of 4` fabricated controls at `404 14 B`

| Repo | Grant (byte-read) | Branch | Region | ★ | Size | Why it is a foundation |
| --- | --- | --- | --- | --: | --: | --- |
| [`gpoore/text2qti`](https://github.com/gpoore/text2qti) | 🟢 **BSD-3-Clause** `1,522 B` (`LICENSE.txt`) | `master` | 🔵 Global | `241` | `110 KB` | Markdown-based plain text → **QTI 1.2**, importable by Canvas and other LMSs. Multiple-choice, true/false, multiple-answers, numerical, short-answer, essay and file-upload items, with LaTeX math and a `siunitx` subset for units. 🟢 The authoring end the QTI tier lacked |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** `1,560 B` | `master` | 🟢 **North America** (UC Berkeley) | `161` | `52,835 KB` | Autograder from Berkeley's **Data Science Education Program**, built to scale by abstracting the autograding internals away from the distribution pipeline. Grades Python scripts and Jupyter notebooks; runs locally in parallel Docker containers, on a managed grading VM, or through third-party LMS autograders — **Canvas and Gradescope named**. Ships a student-side client for public checks |
| [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **MIT** `1,130 B` | `develop` | 🟢 **North America** (Univ. of Central Florida) | `681` | `4,849 KB` | The Python client for the Canvas LMS REST API, maintained by **UCF Open** — an institution, not a vendor or a lone author. The default substrate for any Canvas-side agent. 🟡 Default branch is `develop`, a non-`main` name of the class `601-B` tracks |
| [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | 🟢 **MIT** `1,068 B` (`LICENSE.txt`) | `main` | 🟢 **North America** (Instructure) | `203` | `479 KB` | LTI implementation published by **Instructure itself** — the Canvas vendor. 🔵 Vendor-owned and permissive is the rarer combination in this sector, and it settles the provider side of LTI that `605-I` had to refuse a stale community library for |
| [`Universidade-Livre/matematica`](https://github.com/Universidade-Livre/matematica) | 🟢 **MIT** `1,086 B` | `main` | 🟢 **LATAM** (Brazil, Portuguese) | `1,426` | `190 KB` | 🟡 **Content, not software, and shelved as such.** An open Brazilian mathematics curriculum in Portuguese, region-evidenced by the artifact's own text (`Brasil`, `Brasileira Livre`). 🟢 Its value here is as a **permissive Portuguese-language corpus** for a LATAM retrieval or item-generation build, where the scarcity is the corpus and not the model |

### 🟢 The LMS-connector tier, extended — `4` of these close debt `609-C` named

🔵 `602-B` opened this tier after `gate-promotion-ledger` had been red about it for ~`165` passes.
`609-C` then enumerated `15` `TRENDING-ONLY` rows by name. Four of them are here, plus the upstream
`610-A` rescued.

| Repo | Grant (byte-read) | Branch | ★ | Size | Note |
| --- | --- | --- | --: | --: | --- |
| [`adriasantacreu/google-classroom-mcp`](https://github.com/adriasantacreu/google-classroom-mcp) | 🟢 **MIT** `1,073 B` | `master` | `2` | `105 KB` | 🟢 **`610-A`'s upstream**, promoted in place of the paid-commercial fork that names it |
| [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) | 🟢 **MIT** `1,068 B` | `main` | `62` | `2,079 KB` | 🟢 Closes `609-C`. **D2L Brightspace** — the LMS least represented on these shelves |
| [`semyonfox/canvas-mcp`](https://github.com/semyonfox/canvas-mcp) | 🟢 **MIT** `1,067 B` | `master` | `1` | `356 KB` | 🟢 Closes `609-C` |
| [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp) | 🟢 **MIT** `1,076 B` | `main` | `1` | `332 KB` | 🟢 Closes `609-C`. Grading-side rather than read-side |
| [`vTanco/google-classroom-mcp`](https://github.com/vTanco/google-classroom-mcp) | 🟢 **MIT** `1,145 B` | `main` | `1` | `101 KB` | 🟢 Closes `609-C` |

🟡 **Said plainly, because the figures are small:** four of these five are `1`–`2★` single-maintainer
connectors of `101`–`356 KB`. 🟢 They are real, live, permissive and byte-read, and a connector is a
thin thing by nature — `609-D`'s size rule refutes a *Kubernetes LMS* at `10 KB`, not an MCP server at
`105 KB`. 🔴 They are **not** a maintained-platform bet, and no recipe here should put one on the
critical path without a fork budget. Shelved as substrate, labelled as substrate.

### 🔴 `610-E` — this pass's own grant ladder graded the official Moodle mobile app ungranted

[`moodlehq/moodleapp`](https://github.com/moodlehq/moodleapp) — Moodle HQ's official mobile client,
`133,226 KB`, `1,004★`, pushed `2026-10-29` — returned 🔴 `NO-GRANT` from this pass's first harness.

| probe | result |
| --- | --- |
| 🔴 `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`, `LICENSE-MIT` | 🔴 **`404 14 B` at every one** |
| 🟢 `COPYING.txt` | 🟢 **`200`, `11,358 B` — stock Apache-2.0 body** |
| 🟢 corroboration 1 — `package.json` | 🟢 `"license": "Apache-2.0"` |
| 🟢 corroboration 2 — `README.md` | 🟢 "Apache 2.0" with the canonical URL |

🔴 **And `COPYING.txt` was not a new rung.** This base registered it at ~`p460` on `moodle/moodle`
— *"the grant lives at `COPYING.txt`, a fifth name outside a four-name probe"* — and
`verticals/solutions.md` has carried it since. 🔴 So this is not a discovery; it is **a pass rebuilding
an instrument worse than the committed one and reproducing a defect already fixed.**
🔵 `605-D`, `605-M`, `606-B`, `606-K`, `609-M` and now `610-C` and `610-E`: **the instrument, not the
corpus, is where this base's errors live.** 🟢 The ladder in `ingest/p610-grant-harness.sh` is
corrected to carry `COPYING.txt`.

---

## 🆕 `p609` — reads `2026-11-02` — **🟢 THE EVALUATION/KNOWLEDGE-TRACING TIER GETS `6` PERMISSIVE HOLDERS IN ONE PASS, EVERY GRANT BYTE-READ TODAY. 🔴 THE GITHUB API CALLED `2` OF THEM `NOASSERTION`; BOTH ARE STOCK `MIT` — `598-D` CONFIRMED A THIRD TIME, FROM A THIRD SET OF REPOSITORIES. 🟡 AND THE CITATION LAYER UNDER THESE ROWS CANNOT BE VERIFIED FROM THIS SESSION AT ALL.**

### 🟢 The central result — the diagnostic layer above `pyKT` now exists, permissively

This base has held [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (**MIT**,
`456★`) as the knowledge-tracing benchmark floor for many passes. What it never had was the layer
**above** it: instruments that say whether a KT benchmark is saturated, whether a pooled score means
what it appears to mean, and whether a tutor evaluated against a simulated student was evaluated
honestly. Six rows, all byte-read `2026-11-02`:

| Repo | Grant (byte-read) | Branch | Region | Size | What it contributes |
| --- | --- | --- | --- | --: | --- |
| [`shivanireddyk/tutoreval`](https://github.com/shivanireddyk/tutoreval) | 🟢 **MIT** `1,074 B` | `main` | 🔵 Global | `69 KB` | 🟢 **PROMOTED off the trending shelf** (`609-B`). *"Measuring whether an AI tutor teaches, rather than whether it answers."* 🔵 **Deterministic, no network calls, no API key, no GPU**, and every score it returns carries **the span of text that caused it** — so it is auditable, re-runnable in CI, and free, which no LLM-judge harness is |
| [`KernelInterrupt/kt-benchmark-diagnosis`](https://github.com/KernelInterrupt/kt-benchmark-diagnosis) | 🟢 **MIT** `1,066 B` | `main` | 🔵 Global — holder not placed | `391 KB` | *An Information-Theoretic Evaluation Framework for Benchmark and Model Diagnosis in Knowledge Tracing.* Aggregate AUC hides **where** errors originate and whether a benchmark is near saturation; this estimates the **Local Irreducible Uncertainty** of each interaction using Context Tree Weighting as a causal anchor and projects predictions onto it. Ships its own `pykt/` fork with the CTW/LIU estimators |
| [`huynhanhkhiem-dms/pooled-auc-knowledge-tracing`](https://github.com/huynhanhkhiem-dms/pooled-auc-knowledge-tracing) | 🟢 **MIT** `1,143 B` — 🔴 API said `NOASSERTION` | `main` | 🟢 **APAC** (Vietnam) | `123 KB` | *Pooled AUC Does Not Identify Within-Learner Predictive Discrimination in Knowledge Tracing.* Decomposes AUC across **14 scoring rules** — GlobalMean, ItemMean, SkillMean, FrozenAbility, FrozenIRT, RunningAbility, PFA-shared, BKT, Best-LR(+I), DKT(+I), SAKT(+I). 🔵 **Ton Duc Thang University**, ORCID in README — holder evidence, not a username. Deliberately does **not** redistribute benchmark files; `fetch_data.sh` pulls the Gervet et al. (2020) release |
| [`baptiste-alonso/knowledge-tracing-benchmark`](https://github.com/baptiste-alonso/knowledge-tracing-benchmark) | 🟢 **MIT** `1,298 B` — 🔴 API said `NOASSERTION` | `main` | 🟢 **EMEA** (France) | `2,681 KB` | Seven **interpretable** KT models on `110,101` real interactions / `267` learners / `102` skills from **Cleverlearn**, a French EdTech firm, under one protocol — **CentraleSupélec** project course, Mar–Jun 2026. Interpretability was a *client requirement*, so DKT was excluded by design. Optimised PFA wins at AUC `0.789 ± 0.006`. 🔵 Client data is private and **not** shipped; a synthetic generator with the same schema runs every model end to end |
| [`devissaputra/knowledge_tracing_benchmark`](https://github.com/devissaputra/knowledge_tracing_benchmark) | 🟢 **MIT** `1,076 B` | `main` | 🔵 Global — holder not placed | `424 KB` | A **learner-disjoint** comparison on ASSISTments 2009 (`4,148` learners, `274,331` interactions): priors vs fixed BKT vs validation-tuned BKT vs PFA vs GRU. Held-out GRU ROC-AUC `0.7470` / Brier `0.1800` against PFA `0.6982` / `0.1976`, three seeds, sample SD `0.0008`. 🔵 **Dataset pinned to a revision hash** (`c72a664…`), leakage safeguards and model-selection boundaries documented, and the README states what it did *not* rerun |
| [`pchi1606/sherpa-simulated-student-audit`](https://github.com/pchi1606/sherpa-simulated-student-audit) | 🟢 **MIT** `1,069 B` | 🔴 **`master`** | 🔵 Global — holder not placed | `1,484 KB` | A **preregistered validity audit** of a student simulator, reproduction package for a manuscript prepared for the *Journal of Educational Data Mining*. `bash reproduce.sh` recomputes every preregistered metric from banked artifacts — 300 simulated episodes against 5,000 real ASSISTments sequences, 24 two-sample KS tests with Holm–Bonferroni, bootstrap CIs — then **verifies each headline number against `expected/headline_numbers.json` and prints PASS/FAIL**. ~2 minutes |

🔴 **`sherpa-simulated-student-audit` resolves only at `master`** — its grant *and* its README `404`
at `main`. A root read at `main` would have returned the `404` that looks exactly like "no grant",
which is `p607`'s branch lesson arriving on a new row rather than being remembered.

### 🔴 `609-F` — the API's licence field is wrong again, and the error is one-directional

| repo | API `spdx_id` | byte-read at the real default branch | API verdict |
| --- | --- | --- | --- |
| `baptiste-alonso/knowledge-tracing-benchmark` | 🔴 `NOASSERTION` | 🟢 **MIT**, `1,298 B` — stock body, five named copyright holders | 🔴 **wrong** |
| `huynhanhkhiem-dms/pooled-auc-knowledge-tracing` | 🔴 `NOASSERTION` | 🟢 **MIT**, `1,143 B` — stock body, © 2026 *"The Authors"* | 🔴 **wrong** |
| `zty552252kevin-code/holdfast` | `NOASSERTION` | 🔴 custom non-commercial (see `intel/measured-unusable.md`) | 🟢 right |

🔵 **`2 of 3`, and the two misses are the expensive direction.** Both rejected repositories were real
permissive grants that a `spdx_id` screen would have discarded as unlicensed — the same direction as
`p607`'s `NOASSERTION` findings, now on a third disjoint set. 🟢 **Why the API is wrong is now
visible:** both bodies are stock MIT whose *copyright line* is non-standard — five names across two
lines in one, the literal string `The Authors` in the other. The classifier keys on the whole file,
so an unusual holder line costs the repository its licence. 🔴 That also kills **byte-size** as a
family check from the other end: `1,143 B` and `1,298 B` sit above the stock-MIT band of
`1,064–1,084 B` purely because the copyright line is longer, and `608-B` had already killed size
from the *over*-reading side. **Size is not family in either direction; only the body is.**

### 🟡 `609-G` — the citations under these rows are repo-declared and unverifiable from this session

Four rows above cite an external venue: NeurIPS 2026 (with a poster URL), ICCE 2026, *JEDM*, and
NAACL for a prior row. This base runs `gate-dead-citation`. It could not run today:

| channel | `neurips.cc` | `icce2026.apsce.net` | `microsoft.github.io` |
| --- | --- | --- | --- |
| `curl` via the session proxy | 🔴 `000` — `connect_rejected` | 🔴 `000` — `connect_rejected` | 🔴 `000` — `connect_rejected` |
| the host's page-fetch tool | 🔴 `ENOTFOUND` | — | — |

🔵 **Both channels are closed for every non-GitHub host**, so no venue claim on this page was verified.
Per this base's own `gate-restatement` rule — *a restatement of an unreachable authority is not a
verified grant* — every venue above is marked **repo-declared**. 🟢 What **was** verified is the part
that governs reuse: the grant bytes, the branch, the existence probe and the repository size. A
NeurIPS claim that turns out to be aspirational would not change the licence under any of these rows.

---


## 🆕 `p608` — reads `2026-11-02` — **🟢 THE CONTENT-INGESTION TIER FINALLY HAS A PERMISSIVE, VENDOR-BACKED REPO. 🟢 A SECOND KT MODEL ON THE HELD BENCHMARK SURFACE. 🔴 THE EVAL TIER STAYS EMPTY — THIS TIME BECAUSE THE BEST CANDIDATE SHIPS NO LICENSE.**

### 🟢 The central result — the gap between "documents" and "course" closes permissively

Every course-generation recipe on this base has assumed a step it could not name: get the
institution's own PDFs, slides and recordings into something an agent can query and cite. `p608`
fills it with a vendor-maintained MIT project.

| | before `p608` | 🆕 `p608` |
| --- | --- | --- |
| permissive doc→RAG→agent→wiki platform | 🔴 **none shelved** | 🟢 [`Tencent/WeKnora`](https://github.com/Tencent/WeKnora) — **MIT**, `15,290 B` byte-read, `v0.9.0` |
| maintainer | — | 🟢 **Tencent** (vendor-backed, not one maintainer) |
| i18n of the docs | — | 🟢 EN · 简体中文 · 日本語 · 한국어 |
| 🔴 the catch | — | ⚠️ **bundled third-party components remain Apache-2.0** under an appendix in the same `LICENSE` — attribution obligations survive the MIT header |

### 🟢 New foundational rows — all byte-read `2026-11-02`

| Repo | License (byte-read) | Region | Why it is foundational |
| --- | --- | --- | --- |
| [`Tencent/WeKnora`](https://github.com/Tencent/WeKnora) | 🟢 **MIT** `15,290 B` ⚠️ Apache-2.0 appendix | APAC | The ingestion + retrieval + self-maintaining-wiki layer under every "tutor that must cite the course material" recipe here |
| [`duaabaig/HiSACKT`](https://github.com/duaabaig/HiSACKT) | 🟢 **MIT** `1,118 B` | EMEA (INSA Lyon · LIRIS) | **Second** independent KT model on this base's existing benchmark surface (`ASSIST2009`/`ASSIST2015`/`Algebra2005`/`Statics2011`). Hierarchical self-attention + dynamic skill clustering, **WI-IAT 2025**. Gives the `pyKT`/`pyBKT` tier a peer-reviewed challenger rather than a single reference implementation |
| [`Bradwave/obfusca`](https://github.com/Bradwave/obfusca) | 🟢 **MIT** `1,071 B` | EMEA (Italy) | The **pre-processor** the grading tier never had: strips identity from exam PDFs *in the browser* before anything reaches a model, and is explicitly tuned so its redaction codes do not corrupt vision/LLM OCR. Zero-backend means it adds no data-residency surface |
| [`harjothkhara/whiteboard-tutor`](https://github.com/harjothkhara/whiteboard-tutor) | 🟢 **MIT** `1,499 B` | Global | Reference wiring for **agent-draws-on-canvas** on the tldraw agent starter kit, with voice both ways. The nearest thing on this shelf to a reusable "explain it visually" substrate |

### 🔴 The eval tier: still empty, and now the reason is on the record

`p607` and several passes before it recorded *"no dominant OSS agent eval/observability"* for this
industry. This pass enumerated the best-fitting candidate yet found —
[`wxxxqcy/ai-learning-assistant`](https://github.com/wxxxqcy/ai-learning-assistant), described as an
**end-to-end evaluation framework for education agents covering tool use, policy and safety tests**
— and byte-read it: `8,045 B` README, 🔴 **no license file at `LICENSE`, `LICENSE.md`,
`LICENSE.txt` or `COPYING` on `main` or `master`.**

🔵 **The distinction matters for a studio:** the tier is not empty because nobody built the thing.
It is empty because the thing that exists carries no grant. That is a *contactable* gap — an
engagement can ask the author for terms — where "unfound" was not.

### 🟢 Prior license flags re-read, independently — all hold

`learning-commons-org/knowledge-graph` re-read today at `5,788 B`: 🟢 **code MIT**, 🔴 **datasets
not uniformly licensed** — each carries an access type (`Open`, `Open + Gated`, `Gated`) and the
file states plainly that *"**Open + Gated** and **Gated** content are not covered by CC BY 4.0, CC0,
or any other open license referenced here."* The base's existing `knowledge-graph MIT-code`
shorthand is 🟢 accurate and the gating boundary is 🟢 as recorded.

---

## 🆕 `p607` — reads `2026-11-02`, commit `2026-11-02` — **🟢 `10` FOUNDATION REPOS PROMOTED, EVERY GRANT BYTE-READ TODAY AT THE REAL DEFAULT BRANCH WITH A PER-REPO FABRICATED CONTROL AT `404 14 B`. 🟢 `607-D`: A **NEW GRANT SHAPE**, AND THIS PASS FOUND IT AT **BOTH ENDS OF THE FILE** — PROSE *BEFORE* THE LICENCE TEXT (BSD-3-CLAUSE, UNIVERSITY OF EDINBURGH) AND A SCOPE NOTE *AFTER* IT (MIT FOR CODE, NOT FOR DATA). BOTH ARE GRADED `NOASSERTION` BY THE API AND **`MIT`/`BSD` BY EVERY GREP READER HERE**. 🟢 `607-E`: THE LATAM NATIONAL LEG `606-H` ASKED FOR SUPPLIED `2` ADDRESSES THIS BASE HAS NEVER HELD. 🔴 `4` NOT PROMOTED, WITH REASONS.**

### 🟢 `607-D` — adjacent prose defeats template identity, at either end of the grant

Two repositories in this pass carry a licence whose **text** is unambiguous and whose **family** the
API declines to name. The cause is the same in both and it is positional:

| | leading prose | trailing prose |
| --- | --- | --- |
| repository | [`davemckain/qtiworks`](https://github.com/davemckain/qtiworks) → maintained fork [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) |
| payload | `LICENSE.txt`, 🟢 **`2,058 B`**, byte-read `2026-11-02` | `LICENSE`, 🟢 **`1,218 B`**, byte-read `2026-11-02` |
| fabricated control | 🟢 `404 14 B` | 🟢 `404 14 B` |
| 🔴 API `spdx_id` | 🔴 **`NOASSERTION`** | 🔴 **`NOASSERTION`** |
| 🟢 what the bytes say | 🟢 **BSD-3-Clause**, © **2014 University of Edinburgh** | 🟢 **MIT**, © 2026 `dfdb76` |
| the adjacent prose | `6` lines **above** the text: *"This license is famously liberal. However, you are strongly urged to contribute back to the QTI community…"* | `4` lines **below** the text: *"A licença MIT acima cobre o CÓDIGO deste repositório. Os DADOS embarcados têm proveniência e licenças próprias — veja `ATTRIBUTION.md`."* |
| 🔴 commercial consequence | none — the grant is permissive and the preface is **exhortation, not a condition** | 🔴 **real — the MIT grant does not reach the data**, and the data is the product |

🟢 **The `bncc-mcp` payload was diffed against a stock MIT byte-read in this same pass**
([`eumakerdev/bncc_api`](https://github.com/eumakerdev/bncc_api), `1,081 B`). The diff is exactly two
hunks: the copyright line, and the appended note. 🟢 **The body is stock MIT, character for
character** — which is precisely why a grep reader passes it and why the `~137 B` that matter are the
ones it ignores.

🟢 **The pointer resolves:** `ATTRIBUTION.md` at `main` returns **`200`, `3,331 B`**, fabricated
control `404 14 B`. 🔵 Stated because `gate-evidence-store` is red about a claim that depends on a
component nobody located — this one was located.

🔵 **The generalisation worth keeping:** this base already documents subtree-split grants (`p382`,
`605-L`), untitled grants (`p314`), source-header grants (`p602`) and HTML-capture grants (`604-B`).
🟢 **`607-D` adds the simplest one and the one most likely to be common:** a *stock* licence body with
prose touching it. Template identity is a **whole-file** operation here, and any prose adjacent to the
text — at either end — breaks it. 🟢 The API's `NOASSERTION` is therefore *correct behaviour reported
uselessly*: it has detected "not a stock file" and declined to say which family, in both directions.

### 🟢 `607-E` — the LATAM national leg, which `606-H` named as the measurement owed

`605-F` proved the national-query channel on APAC; `606-H` proved it on EMEA and closed by naming
LATAM as *"the untested third."* It was tested this pass, in Portuguese, against Brazilian
curriculum vocabulary (`MEC`, `BNCC`, `escola`, `código aberto`):

| | result |
| --- | --- |
| 🟢 addresses returned that this base has **never held** (`0` mentions anywhere) | 🟢 **`2`** |
| 🟡 returned, held in `trending` only, on no sell shelf | 🟡 **`2`** |
| 🔴 returned and already shelved | `2` |
| 🔴 returned, web asserts a licence, **payload refutes it** | 🔴 **`1`** |

🟢 **Third region, third time the national leg out-produced the global legs in the same pass** — which
returned the thirty-seventh nil (`607-A`). 🔵 The channel is now proven on APAC, EMEA and LATAM; North
America is the one region where it has not been run as a *supply* leg, only as a demand leg.

### 🟢 Promoted to this page — `10` rows, grants byte-read `2026-11-02`, every control at `404 14 B`

| repo | grant (byte-read today) | branch | stars | pushed | region |
| --- | --- | --- | --: | --- | --- |
| [`Universidade-Livre/ciencia-da-computacao`](https://github.com/Universidade-Livre/ciencia-da-computacao) | 🟢 **MIT**, `1,087 B`, title block | `main` | 🟢 **`21,000★`** | `2026-05-20` | LATAM |
| [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **MIT**, `1,084 B`, title block | `main` | `356★` | `2026-10-31` | EMEA |
| [`marcosroriz/sete`](https://github.com/marcosroriz/sete) | 🟢 **MIT**, `1,069 B`, title block | `master` | `22★` | `2023-03-20` | LATAM |
| [`eumakerdev/bncc_api`](https://github.com/eumakerdev/bncc_api) | 🟢 **MIT**, `1,081 B`, title block | `main` | `17★` | 🟢 **`2026-11-02`** | LATAM |
| [`php-xapi/client`](https://github.com/php-xapi/client) | 🟡 **MIT, untitled** (`p314`) — `1,068 B`, opens on the copyright line | 🔴 **`0.7`** | `23★` | `2023-11-01` | EMEA |
| [`php-xapi/model`](https://github.com/php-xapi/model) | 🟡 **MIT, untitled** (`p314`) — `1,068 B`, opens on the copyright line | 🔴 **`3.x`** | `3★` | `2025-01-20` | EMEA |
| [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) | 🟢 **MIT**, `1,066 B`, title block | `main` | `7★` | `2024-07-10` | EMEA |
| [`DFE-Digital/education-benchmarking-and-insights`](https://github.com/DFE-Digital/education-benchmarking-and-insights) | 🟢 **MIT**, `1,091 B`, title block | `main` | `4★` | 🟢 **`2026-11-01`** | EMEA |
| [`GuilhermeScarpini/agente-bncc-professores`](https://github.com/GuilhermeScarpini/agente-bncc-professores) | 🟢 **MIT**, `1,074 B`, title block | `main` | `0★` | `2026-10-21` | LATAM |
| [`karsh482/Gaokao`](https://github.com/karsh482/Gaokao) | 🟢 **Apache-2.0**, `11,357 B` | `main` | `1★` | `2026-06-29` | APAC |

🔴 **Three of these ten do not resolve at `main`.** `php-xapi/client` is at `0.7`, `php-xapi/model`
at `3.x`, `marcosroriz/sete` at `master` — and on the agent shelf a fourth,
`datakind/student-success-tool`, resolves only at `develop`. 🔵 `p602` established versioned default
branches as a discovery blocker; a root-only read at `main` would have published *"no grant"* for all
four, which is the same wrong answer as a real absence.

🟡 **The two rows that are institutional rather than popular:**
[`DFE-Digital/education-benchmarking-and-insights`](https://github.com/DFE-Digital/education-benchmarking-and-insights)
is the **United Kingdom Department for Education's** own benchmarking codebase, MIT, pushed
`2026-11-01` — a national ministry publishing permissively, which is rarer on this page than any
star count. [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) is source-code plagiarism
detection out of the Dodona project (Ghent), `356★`, MIT, and is the only maintained permissive tool
of its kind this base holds.

🟡 **`php-xapi/client` and `php-xapi/model` complete the xAPI layer** `p604` opened with the H5P
capture repos: the PHP client and model beneath an LRS, with
[`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) as the store. 🔴 Both are **untitled** grants —
`1,068 B` opening directly on *"Copyright (c) 2014-2019 Christian Flothmann"* — the `p314` class,
and both are **stale**: `2023-11-01` and `2025-01-20`.

### 🔴 Not promoted, with the reason

| address | grant, byte-read `2026-11-02` | 🔴 verdict |
| --- | --- | --- |
| [`financeiroetica01-art/jogos-empreendedorismo-bncc`](https://github.com/financeiroetica01-art/jogos-empreendedorismo-bncc) | 🔴 **NONE** — `404` at `LICENSE`, `.md`, `.txt`, `LICENCA`, `LICENÇA`, `COPYING`, `licenca.md`; control `404 14 B` | 🔴 **BLOCK.** The LATAM leg returned it as *"MIT, free access for public schools"*. 🟢 **The payload refutes the web.** A channel-conflict disconfirmation, recorded |
| [`eledia/moodle-block_elediaai_tutor`](https://github.com/eledia/moodle-block_elediaai_tutor) | 🔴 **NONE** at `7` spellings on branch 🔴 **`51`**; control `404 14 B` | 🔴 **BLOCK — no grant means no permission.** 🔵 A German Moodle AI-tutor block, and the row this page would most like to have |
| [`quizbankorg/quizbank`](https://github.com/quizbankorg/quizbank) | 🔴 **NONE** at `7` spellings; control `404 14 B` | 🔴 **BLOCK — no grant** |
| [`EduardoKrausME/moodle-local_mcp`](https://github.com/EduardoKrausME/moodle-local_mcp) | 🟡 **GPL-3.0**, `35,149 B`, byte-read at `master` | 🟡 **Not blocked, flagged.** Reciprocal. A Moodle MCP plugin, so the licence is Moodle-consistent and the constraint is the studio's, not the repo's |
| [`davemckain/qtiworks`](https://github.com/davemckain/qtiworks) | 🟢 **BSD-3-Clause**, `2,058 B` (`607-D`) | 🔴 **DECLINE STANDS, on support — not on licence.** Closed by its own README, HEAD `2023-01-04`. 🟢 **Credit where it is written:** the ledger's `reverified_evidence` field already recorded this *and* the payload digest `a5c692f12090`. This pass computed `a5c692f120907d58…` independently and it **matches**. The licence family is the only new fact |
| [`google/licenseclassifier`](https://github.com/google/licenseclassifier) | 🟢 **Apache-2.0**, `11,358 B`, `351★` | 🔴 **DISQUALIFIED — relevance.** Not education software. 🟡 **But registered deliberately:** this base grades licences by hand-rolled byte bands and title-line greps, and an Apache-2.0 licence classifier has been sitting in its own `p436` backlog the whole time. See `P607-3` in `compose/patterns.md` |

🔵 **A byte-band coincidence, noted so nobody builds on it:** `karsh482/Gaokao`'s Apache-2.0 payload
is `11,357 B` and `google/licenseclassifier`'s is `11,358 B`. 🔴 One byte apart, two different files.
`p312`'s rule — identify by **template**, never by a byte band — with a one-byte demonstration.

## 🆕 `p606` — reads `2026-11-02`, commit `2026-11-02` — **🟢 A `6,955★` APACHE-2.0 EDUCATION REPOSITORY ON THIS BASE'S OWN SHELVES WAS INVISIBLE TO EVERY CAPABILITY PROBE IT OWNS, AND THE THING HIDING IT WAS A **DIRECTORY**: GITHUB RENDERS `.github/README.md` AS THE REPOSITORY README AND NO LADDER HERE ASKS FOR IT. 🟢 `603-C` CORROBORATED INDEPENDENTLY AT `5.4 %` AND EXTENDED BY TWO RUNGS. 🔴 A TRANSFER `p605` RESOLVED IS STILL SHELVED UNDER ITS STALE NAME AND THE CANONICAL ADDRESS IS HELD NOWHERE.**

### 🟢 `606-G` — `603-C`'s defect, measured on a second population and extended

`603-C` found that `lib/probe_payload.sh` reads the README at **one spelling** and that `5.7 %` of
repositories are invisible to it. This pass harvested README first screens for the entire sell-shelf
population and got the same answer from different data:

| | `603-C` | 🆕 `p606` |
| --- | --- | --- |
| population | the pass's own candidate set | 🟢 **all `3` sell shelves, `536` READMEs** |
| non-`README.md` spellings | `5.7 %` | 🟢 **`29 of 536` = `5.4 %`** |
| rungs in the probe | `1` | `8` |
| 🔴 repositories still unresolved at `8` rungs | — | 🔴 **`5`** |
| 🟢 resolved by **full-tree enumeration** instead | — | 🟢 **`2 of 5`** |

🟢 **The spellings actually in use**, which is the list a probe should carry:

| spelling | repos |
| --- | --: |
| `README.md` | `507` |
| `README.rst` | `15` |
| `readme.md` | `8` |
| `Readme.md` | `3` |
| `README` · `README.txt` · `docs/README.md` | `1` each |
| 🆕 **`.github/README.md`** | 🔴 **not in any probe here** |
| 🆕 **`readme.adoc`** | 🔴 **not in any probe here** |

### 🔴 The `6,955★` repository that reads as README-less

[`oppia/oppia`](https://github.com/oppia/oppia) — **Apache-2.0 byte-read today** (`512 B`, fabricated
control `404`), 🟢 **`6,955★`**, `5,872` forks, default branch `develop`, **pushed `2026-11-02`** —
returns `404` for `README.md` at its real default branch. `git ls-tree -r HEAD` shows why: its README
is at **`.github/README.md`**, one of `26` readme-ish paths in the tree.

🔴 **GitHub renders `.github/README.md` as the repository README.** So the page a human sees exists,
and every probe this base owns reports absence. For a repository of this size on this shelf that is
not a cosmetic miss: `605-I`'s capability probe, `603-C`'s README channel and any description-derived
classification all read it as empty.

🟡 The second recovered rung is `readme.adoc` (AsciiDoc) on
[`hit-moodle/moodle-local_onlinejudge`](https://github.com/hit-moodle/moodle-local_onlinejudge).

🟢 **`3 of the 5` genuinely have no README at any spelling** — established by enumerating the whole
tree rather than by exhausting a ladder, which is the difference between *measured absence* and
*failure to look*:

| repo | root entries | readme-ish paths in tree |
| --- | --- | --: |
| [`corleone000000/fluir`](https://github.com/corleone000000/fluir) | `index.html`, `ai.js`, `speech.js`, `sw.js`, … | 🔴 `0` |
| [`Lawrence-Public-Schools/OneRoster-1.1-PowerQueries`](https://github.com/Lawrence-Public-Schools/OneRoster-1.1-PowerQueries) | `LICENSE`, `plugin.xml`, `queries_root`, … | 🔴 `0` |
| [`Apereo-Learning-Analytics-Initiative/data-loader-library`](https://github.com/Apereo-Learning-Analytics-Initiative/data-loader-library) | `LICENSE`, `pom.xml`, `src` | 🔴 `0` |

🔵 `605-B` recommended tree enumeration for the **grant** ladder and this pass confirms it on the
**README** ladder: one request per repository answers what six rungs could not, in both places.

### 🟢 Promoted to this shelf — `1` row, grant byte-read `2026-11-02`, control at `404`

| repo | grant (byte-read) | branch | stars | region | why it is here |
| --- | --- | --- | --: | --- | --- |
| [`uPortal-Project/CalendarPortlet`](https://github.com/uPortal-Project/CalendarPortlet) | 🟢 **Apache-2.0** (`512 B` read, control `404`) | `master` | `15` | North America | 🟢 The **canonical address** of `Jasig/CalendarPortlet`, which this page has carried under its stale name. Apereo-family JSR-168 calendar portlet, pushed `2026-10-16` |

🔴 **`606-D2`:** `Jasig/CalendarPortlet` has `5` mentions across this page, `agents/top.md` and
`repos/trending.md`; the canonical address had **`0`** before this row. `605-C` resolved the transfer
and no pass rewrote the rows — which is the general defect, not a one-off.

🔵 And it closes a loop on `604-B`: the HTML grant payload that pass found is a **saved page of the
old address** (`saved from url=…Jasig/CalendarPortlet/master/LICENSE`). The transfer is the *cause*
of the defect class.

### 🟡 Not promoted, with the reason

| repo | measured | why not |
| --- | --- | --- |
| [`EduNLP/edu-convokit`](https://github.com/EduNLP/edu-convokit) | 🟢 MIT byte-read (`512 B`, control `404`), `117★`, pushed `2025-04-19` | 🟢 **Already on this page** (line `62`) — `605-C` resolved this transfer *and* rewrote the row. Recorded to show the contrast with `CalendarPortlet` |
| `Tangerine-Community/Tangerine` | 🟢 GPL-3.0 byte-read (`512 B`, control `404`), `116★` | 🔴 **Copyleft** — belongs on `verticals/solutions.md` with the licence flagged, not on a permissive-foundation page. Promoted there this pass |
## 🆕 `p605` — reads `2026-11-02`, commit `2026-11-02` — **🟢 `10` FOUNDATION REPOS PROMOTED OUT OF THE `p436` BACKLOG, EVERY GRANT BYTE-READ TODAY AT THE REAL DEFAULT BRANCH WITH A PER-REPO FABRICATED CONTROL AT `404`. 🟢 TWO ARE **BRAZILIAN NATIONAL-CURRICULUM AND NATIONAL-EXAM ARTEFACTS** — THE LATAM EVIDENCE LAYER THIS BASE HAS BEEN THIN ON. 🔴 `605-K`: THE `p436` BACKLOG'S REAL PROMOTION DEBT, MEASURED AGAINST **SELL SHELVES** RATHER THAN ANY MENTION, IS `107 of 265` (`40.4 %`) — `p603` SIZED THE LEDGER, NOT THE DEBT. 🟢 `605-L`: A NEW GRANT SHAPE — **SPLIT BY SUBTREE, WITH A POINTER AT THE ROOT**, WRITTEN IN PORTUGUESE.**

### 🔴 `605-K` — the backlog's real size is a promotion figure, not a ledger figure

🟡 `p603` corrected `p602` and sized `evidence/promotion-ledger.2026-10-25-p436.tsv` at **`108`
repository addresses**. 🟢 That count is right and it answers a different question from the one
`gate-promotion-ledger` has been red about for ~`166` passes.

| question | predicate | figure |
| --- | --- | --: |
| 🟡 how big is the ledger? | rows whose `slug` is a repository address | `265` |
| 🟡 how many addresses does this base not mention at all? | address absent from `agents`, `repos`, `verticals`, `intel`, `compose` | 🟢 **`0`** |
| 🔴 **how many are claimed but never *sold*?** | address absent from the **three sell shelves** | 🔴 **`107` (`40.4 %`)** |

🔵 **The middle row is the trap.** Measured against *any* mention the backlog looks absorbed,
because a row mentioned in [`./trending.md`](./trending.md) counts as held — and *"claimed in
`trending` and on no live shelf"* is the exact condition the gate objects to. 🟢 **The promotion
debt is the third row, and this pass pays `19` of it** (`10` here, `9` on
[`../agents/top.md`](../agents/top.md)), leaving `88`.

### 🟢 `605-L` — a grant split by subtree, with a pointer at the root, in Portuguese

🟢 [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) carries a root
`LICENSE` of `910 B` that **contains no grant text at all.** It opens `# Licenças` and partitions
the repository:

| subtree | grant | instrument |
| --- | --- | --- |
| `harness/`, `test/`, config files | 🟢 **MIT** | [`LICENSE-CODIGO.md`](https://github.com/bncc-dev/bncc-benchmark/blob/main/LICENSE-CODIGO.md) — `1,286 B`, resolves `200` |
| `itens/`, `resultados/`, `METODOLOGIA.md`, docs | 🟢 **CC BY 4.0** | [`LICENSE-DADOS.md`](https://github.com/bncc-dev/bncc-benchmark/blob/main/LICENSE-DADOS.md) — `577 B`, resolves `200` |

🔵 **Three of this base's registered classes meet in one file.** 🟢 `p307`'s three-valued
classifier grades the root `LICENSE` a **`POINTER`**, not a `GRANT`. 🟢 `p354`'s
`gate-grant-path` is satisfied — both named paths resolve at the asserted branch, and the
fabricated control at the same rung returns `404 14 B`. 🔴 The API reads the whole thing as
`NOASSERTION`.

🔵 **And it is `604-C`'s sibling, not its twin.** `604-C` found **two grants stacked in one file**
from two holders; this is **one file pointing at two grants partitioned by directory**. 🟢 The
mechanical difference matters: a reader that stops at the first declaration (`594-F` stage 2)
returns *nothing* here rather than a half-answer, because there is no declaration to stop at.
🟢 **The general control: a payload that names other paths and grants nothing itself is a
`POINTER`, and the verdict lives one rung down — per subtree, not per repository.**

🔵 The grant is written in **Portuguese**, which is the [`portabilis/i-diario`](https://github.com/portabilis/i-diario)
class carried since `p319`. 🟢 That class now has a second instance and a second shape.

### 🟢 Promoted to this shelf — `10` rows, grants byte-read `2026-11-02`, every control at `404`

🔵 Region is the **HEAD committer tz offset**. 🔵 `★` from the `fork:true` arm of
`search/repositories` (`605-C`).

| Repo | Grant (byte-read) | Branch | HEAD | ★ | tz | Region | Why it is a foundation |
| --- | --- | --- | --- | --: | --- | --- | --- |
| [marimo-team/learn](https://github.com/marimo-team/learn) | 🟢 **MIT** (`1,062 B`) | `main` | `2026-04-30` | `362` | `-07:00` | North America | 🟢 Curated **executable courseware** — reactive marimo notebooks across Python, data science and optimisation. 🔵 The notebook *is* the lesson *and* the runtime, so there is no slide-to-code gap to maintain. Pairs with [`ljchang/marimo-grader`](https://github.com/ljchang/marimo-grader) on [`../agents/top.md`](../agents/top.md) |
| [EduNLP/edu-convokit](https://github.com/EduNLP/edu-convokit) | 🟢 **MIT** (`1,068 B`) | `main` | `2025-04-18` | `117` | `-07:00` | North America | 🟢 The open framework for **education conversation data** — de-identification, annotation and analysis of classroom talk. 🔵 **This is the canonical address of a row this base already shelved as `stanfordnlp/edu-convokit`**; `605-C` proved them one repository by HEAD identity. 🟡 HEAD is `2025-04-18`: a stable research library, flagged |
| [lplnufpi/essay-br](https://github.com/lplnufpi/essay-br) | 🟢 **MIT** (`1,113 B`) | `main` | `2023-05-07` | `17` | `-03:00` | LATAM | 🟢 **Extended Essay-BR** — Brazilian high-school essays **graded by human professionals against the ENEM criteria**. 🔵 A scored corpus in Portuguese is the one thing an automated-essay-scoring engagement cannot synthesise. 🟡 HEAD `2023-05-07`: a **dataset**, which does not rot the way code does — flagged rather than disqualified |
| [bncc-dev/bncc-benchmark](https://github.com/bncc-dev/bncc-benchmark) | 🟢 **MIT** (code) **+ CC BY 4.0** (items/results) — split, see `605-L` | `main` | `2026-09-19` | `12` | `-03:00` | LATAM | 🟢 A **hallucination benchmark over the BNCC**, Brazil's national curriculum: an item bank, per-round model answers, and a written methodology. 🔵 The missing instrument for *"does this model actually know the national curriculum we are paid to teach?"* — and it is the only artefact here that measures an LLM against a **national** curriculum |
| [yetanalytics/pedestal-oidc](https://github.com/yetanalytics/pedestal-oidc) | 🟢 **Apache-2.0** (`11,356 B`) | `main` | `2026-10-16` | `10` | `-04:00` | North America | OIDC authentication interceptors for Clojure/Pedestal services, from **Yet Analytics** — the xAPI/LRS vendor whose capture layer this base already shelves. 🟢 The auth rung under a learning-record service |
| [pie-framework/pie-qti](https://github.com/pie-framework/pie-qti) | 🟢 **MIT** (`1,096 B`) | `master` | `2026-10-26` | `4` | `-07:00` | North America | QTI parsing and transformation inside the **PIE** assessment-element framework. 🟢 A *second maintainer* on the QTI axis, which `p604`'s one-maintainer QTI flag explicitly asked for |
| [sonyccd/qti-playground](https://github.com/sonyccd/qti-playground) | 🟢 **MIT** (`1,069 B`) | `main` | `2025-08-11` | `4` | `-04:00` | North America | Web app to **view, edit and learn** QTI 3.0 items, with the standard documented alongside. 🟢 The onboarding surface for a team that has never touched QTI. 🟡 HEAD `2025-08-11`, flagged |
| [otacke/h5p-theme-picker](https://github.com/otacke/h5p-theme-picker) | 🟢 **MIT** (`1,072 B`) | `master` | `2026-10-28` | `3` | `+01:00` | EMEA | 🟢 A custom element for H5P theme and density selection — 🔵 written because **H5P.com ships one and H5P Group did not release the code**, so every other H5P integration overrides themes by hand. A gap-filler, not a reimplementation |
| [DecoyLex/ltix](https://github.com/DecoyLex/ltix) | 🟢 **MIT** (`1,067 B`) | `main` | `2026-10-30` | `2` | `-07:00` | North America | **LTI** for Elixir, published on Hex with docs and CI. 🟢 The first BEAM-language LTI rung on this base; replaces the `2019` Node library disqualified on [`../agents/top.md`](../agents/top.md) |
| [iamlucasb/lti-core](https://github.com/iamlucasb/lti-core) | 🟢 **MIT** (`1,069 B`) | `main` | `2026-10-29` | `1` | `+08:00` | APAC | A minimal LTI core library, pushed `2026-10-29`. 🟡 `1★` and single-maintainer — shelved for the **standard** and the APAC placement, flagged as such |

🔵 **What the batch is, taken together:** 🟢 the **assessment-interoperability** layer (`3` QTI
repos + `2` LTI libraries + OIDC), the **executable-courseware** layer (`marimo-team/learn` +
its grader), and 🟢 **two LATAM evidence artefacts** — a human-scored Portuguese essay corpus and
a national-curriculum benchmark. 🔵 The second group is the one Globant cannot buy: regional
ground truth with a licence attached.

## 🆕 `p604` — reads `2026-11-02`, commit `2026-11-02` — **🟢 `11` FOUNDATION REPOS PROMOTED, EVERY GRANT BYTE-READ AT THE REAL DEFAULT BRANCH WITH A PER-REPO FABRICATED CONTROL AT `404`. 🟢 `3` OF THEM ARE **ECL-2.0 REPOS THE API CALLS `NOASSERTION`** — RECOVERED BY THE `604-A` SWEEP, NOT BY SEARCH. 🟢 A COMPLETE **QTI 3.0 TOOLCHAIN** (`4` REPOS, ONE MAINTAINER, FLAGGED AS SUCH) AND THE **xAPI CAPTURE LAYER** FOR H5P. 🔴 `1` REPO IN THE SWEEP IS NOT SHELVED BECAUSE ITS GRANT PAYLOAD IS A SAVED WEB PAGE (`604-B`).**

### 🟢 The Apereo Learning Analytics Initiative — the ECL-2.0 pool, and why it is worth shelving

🔵 `604-A` on [`../agents/top.md`](../agents/top.md) establishes that this org holds **`9`
ECL-2.0 repositories and the API calls all nine `NOASSERTION`**. 🟢 That matters here and not
only methodologically: **ECL-2.0 is Apache-2.0 with a narrowed patent grant**, written by and
for the education sector, and it is a licence Globant can build on. 🔴 A dependency screen
reading `spdx_id` rejects this entire stack as unlicensed.

🔵 **What the stack is:** a learning-record warehouse (`OpenLRW`), an xAPI learning-record
store (`OpenLRS`), a processing pipeline (`LearningAnalyticsProcessor`), dashboards, and the
loaders and shared models between them. 🟡 **Dormancy stated plainly** — the newest HEAD in
the org is `2025-09-12` and most rows below are `2017`–`2020`. These are shelved as **reference
implementations of the education-analytics data model**, not as live upstreams.

| Repo | Grant (byte-read) | Bytes | Branch | Pushed | ★ | tz | Region | Why it is a foundation |
| --- | --- | --: | --- | --- | --: | --- | --- | --- |
| [Apereo-LAI/OpenLRW-python-api-client](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW-python-api-client) | 🟢 **ECL-2.0** 🔴 (API: `NOASSERTION`) | `9,877` | `master` | `2019-07-19` | `1` | `+02:00` | EMEA | Python client for the OpenLRW learning-record warehouse — the shortest path from an agent to a standards-shaped learner record |
| [Apereo-LAI/lai-event](https://github.com/Apereo-Learning-Analytics-Initiative/lai-event) | 🟢 **ECL-2.0** 🔴 (API: `NOASSERTION`) | `9,877` | `master` | `2020-02-03` | `1` | `+01:00` | EMEA | 🔵 Grant at `LICENSE.md`, not `LICENSE`. The shared **event model** across the LAI stack — the vocabulary a new analytics producer has to match |
| [Apereo-LAI/lai-model](https://github.com/Apereo-Learning-Analytics-Initiative/lai-model) | 🟢 **ECL-2.0** 🔴 (API: `NOASSERTION`) | `9,877` | `master` | `2019-12-09` | `0` | `+01:00` | EMEA | The shared **data model** beside `lai-event`; read the two together before modelling learner events |
| [Apereo-LAI/data-loader-library](https://github.com/Apereo-Learning-Analytics-Initiative/data-loader-library) | 🟢 **Apache-2.0** | `11,356` | `master` | `2019-11-07` | `0` | `-07:00` | North America | Shared loader library for LAI ingest — the seam where an institution's SIS/LMS extract becomes analytics input |
| [Apereo-LAI/canvas-matthews-data-loader](https://github.com/Apereo-Learning-Analytics-Initiative/canvas-matthews-data-loader) | 🟢 **Apache-2.0** | `11,356` | `master` | `2017-03-08` | `0` | `-05:00` | North America | A worked **Canvas** loader against that library — the concrete example of the seam above |
| [Apereo-LAI/LRSLoadTest](https://github.com/Apereo-Learning-Analytics-Initiative/LRSLoadTest) | 🟢 **Apache-2.0** | `11,323` | `master` | `2015-03-17` | `1` | `-07:00` | North America | 🟡 Oldest row here. A load-test harness for an **LRS** — the capacity question nobody asks until an xAPI pipeline is already in production |
| [sakaiproject/genericdao](https://github.com/sakaiproject/genericdao) | 🟢 **ECL-2.0 AND Apache-2.0** (dual, both texts) 🔴 (API: `NOASSERTION`) | `22,589` | `master` | `2024-12-17` | `4` | `-05:00` | North America | 🟢 `0` prior occurrences in this base. Sakai's DAO library, and the clearest **dual-grant** specimen in the education corpus — `604-A` |

### 🟢 A complete QTI 3.0 toolchain — `4` repos, and the honest caveat

🔵 **Why it is worth a shelf at `0★`.** **QTI 3.0** is the 1EdTech interchange format for
assessment items and results, and open tooling for it is genuinely scarce — it is the format
that makes a question bank portable between an LMS, a proctoring tool and an AI item
generator. 🟡 **The caveat, stated once and applying to all four rows:** these come from a
**single small org** (`metyatech`, `+09:00`), carry `0`–`2★`, and sit beside that org's
unrelated Unreal Engine and VRChat plugins. 🟢 They are shelved for the **standard** they
implement and because every grant was byte-read today — **not** as established infrastructure.

| Repo | Grant (byte-read) | Bytes | Branch | Pushed | ★ | Region | Role in the chain |
| --- | --- | --: | --- | --- | --: | --- | --- |
| [metyatech/markdown-to-qti](https://github.com/metyatech/markdown-to-qti) | 🟢 **MIT** | `1,065` | `main` | `2026-09-19` | `2` | APAC | 🔵 Already held. **Authoring** — Markdown item source becomes a QTI package |
| [metyatech/qti-xml-core](https://github.com/metyatech/qti-xml-core) | 🟢 **MIT** | `1,056` | `main` | `2026-09-20` | `0` | APAC | 🟢 The **XML core** the rest of the chain depends on |
| [metyatech/apply-to-qti-results](https://github.com/metyatech/apply-to-qti-results) | 🟢 **MIT** | `1,070` | `main` | `2026-09-20` | `1` | APAC | 🟢 Applies marks into QTI `assessmentResult` XML — the **write** step an AI grader needs |
| [metyatech/tracklms-to-qti-results](https://github.com/metyatech/tracklms-to-qti-results) | 🟢 **MIT** | `1,065` | `main` | `2026-09-25` | `0` | APAC | 🟢 Converts **TrackLMS** exports into QTI results — the adapter from a real LMS's export shape |

### 🟢 The xAPI capture layer for H5P

| Repo | Grant (byte-read) | Bytes | Branch | Pushed | ★ | tz | Region | Why it is a foundation |
| --- | --- | --: | --- | --- | --: | --- | --- | --- |
| [otacke/h5pxapikatchu](https://github.com/otacke/h5pxapikatchu) | 🟢 **MIT** (🔵 body-anchored — see below) | `1,051` | `master` | `2026-06-16` | `10` | `+02:00` | EMEA | 🟢 Captures the **xAPI statements H5P content already emits** into a WordPress database, with filtering and CSV export. 🔵 H5P is everywhere in European schools and its interaction data is usually thrown away; this is the cheapest place to start measuring |

🔵 **A small grant-reading note worth keeping.** `h5pxapikatchu`'s `LICENSE` has **no title
line** — it opens `Permission is hereby granted, free of charge`. 🔴 A title-anchored reader
(`p525-title-anchored-grant`) returns nothing; the body token settles it as **MIT**. 🟢 Same
shape as `604-C`'s `====` opener: **the first line of a grant file is not reliably its name.**

### 🔴 Not shelved from this sweep, with the reason

| Not shelved | Grant as read | Reason |
| --- | --- | --- |
| [uPortal-Project/FeedbackPortlet](https://github.com/uPortal-Project/FeedbackPortlet) | 🔴 `11,620 B` of **HTML** | 🔴 `604-B`: the payload is a **saved web page of `Jasig/CalendarPortlet`'s licence**, not a grant from this repository's titleholder. A grep reader grades it `Apache-2.0`; the correct verdict is 🟡 **REVIEW** |
| [Apereo-LAI/SakaiXAPI-Provider](https://github.com/Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider) | 🔴 `NO-PAYLOAD` on `6` ladder rungs | 🟡 Already held with its `598-A` verdict (**ECL-2.0** via `pom.xml`). 🔴 A manifest field grades `REVIEW`, never 🟢 — unchanged, and re-confirmed as `NO-PAYLOAD` today |
| `Apereo-LAI/maven-repo` | 🟢 Apache-2.0 `11,356 B` | 🟡 Grant is clean, but the repository is an **artifact store**, not software to build on. Verified and deliberately not padded onto this shelf |
| `Apereo-LAI/OpenDashboard-ux`, `SakaiXAPI`, `community-dataloaders`, `lai-config`, `SNAPPSociogram-jar` | 🔴 `NO-PAYLOAD` | 🔴 No grant file at any ladder rung at the real default branch. `5` repos, named rather than counted |

## 🆕 `p603` — reads `2026-11-02`, commit `2026-11-02` — **🟢 `21` FOUNDATION REPOS PROMOTED OUT OF THE `p436` BACKLOG, EVERY GRANT BYTE-READ TODAY AT THE REAL DEFAULT BRANCH, EVERY FABRICATED-PATH CONTROL AT `404`. 🟢 THE ADDITION IS A WHOLE LAYER THIS PAGE WAS THIN ON: THE **INTEROP-STANDARDS SUBSTRATE** — QTI, xAPI, CASE, OneRoster, Open Badges AND LEARNER CREDENTIALS, `9 of 21` ROWS, MOSTLY FROM THE STANDARDS BODIES THEMSELVES (`1EdTech`, `adlnet`, `instructure`, OpenWallet Foundation). 🔴 `603-C`: THE LIBRARY EVERY PASS SOURCES READS THE README AT **ONE SPELLING**, AND `5.7 %` OF REPOSITORIES ARE INVISIBLE TO IT — THE SAME ERROR CLASS THE LICENCE LADDER ALREADY PAID TO FIX.**

### 🔴 `603-C` — `lib/probe_payload.sh` line `155` is a single-spelling README probe

🔵 The library's header calls its README rung the trap that earns its keep — *"No filename
ladder in this base would have found it — the README's own licence LINK did, in one
request"* (measured on `OS4ED/openSIS-Classic`, GPL-2.0 at `docs/License.txt`). 🔴 **That
rung reads exactly one filename:**

    _readme_license_path() { _raw "$1" "$2" README.md ... }

🟢 **Measured across this base's own backlog, `2026-11-02`**
([`../evidence/readme-spelling-ladder.2026-11-02-p603.tsv`](../evidence/readme-spelling-ladder.2026-11-02-p603.tsv)):

| README path | repos |
| --- | --: |
| `README.md` | `100` |
| 🔴 `readme.md` | `3` |
| 🔴 `README.rst` | `2` |
| 🔴 `Readme.md` | `1` |
| no README at any probed spelling | `1` |
| 🔴 **invisible to a `README.md`-only probe** | 🔴 **`6` of `106` = `5.7 %`** |

🔴 **The repositories it hides are not marginal.** `SafeExamBrowser/seb-server` is one of the
six, and this base maintains **two dedicated instruments** for that project
(`compose/code/seb-proctoring-validator`, `compose/code/sebserver-mcp-gate`). 🔵 Three of
this pass's own promotions — `h5p/h5p-cli` (`readme.md`), `openedx/tutor-contrib-aspects`
(`README.rst`), `kitschpatrol/yanki` (`readme.md`) — returned an **empty description** on the
first read for exactly this reason, and were only described after a ladder was run.

🔵 **Why this is the licence-ladder finding one channel over.** `LICENCE` (British spelling)
was priced at **1 payout in 44** and is in the ladder. 🔴 `readme.md` pays **3 in 106** —
a higher rate — and was not. 🟢 Order priced and the one-line fix written out in
[`../compose/code/p603-readme-ladder/README.md`](../compose/code/p603-readme-ladder/README.md).

🔴 **Why this pass did not patch line `155` itself:** the harness denied executing shell code
from the cloned repository, so the library could neither be sourced nor exercised, and **a
patch this pass cannot run is a patch this pass cannot verify.** `p603probe.sh` is an
independent implementation written against the four defects the library documents by name
(D1 branch resolution, D2 README licence link, D3 British spelling, D4 title-anchored
family). 🟢 **D1 paid four times this pass**: default branches `public-release`
(`chiv-heng/ferpa-guard`), `0.7` (`php-xapi/client`), `3.x` (`php-xapi/model`) and
`eduquest-main` (`EDUQUEST2026-2027/EDUQUEST`) — 🔴 a hardcoded `main`/`master` writes all
four down as ungranted.

### 🟢 The interop-standards substrate — `9` rows, the layer this page was thinnest on

🔵 These are the repositories that make an AI layer *portable between institutions* rather
than bound to one LMS tenancy. 🟢 Mostly published by the standards bodies themselves, which
is what makes them safe to build on.

| Repo | Grant (byte-read) | Branch | Pushed | tz | Region | What it is |
| --- | --- | --- | --- | --- | --- | --- |
| [1EdTech/OpenCASE](https://github.com/1EdTech/OpenCASE) | 🟢 **Apache-2.0** (`11,263 B`) | `main` | `2026-10-29` | `-04:00` | North America | 🟢 **CASE** — curriculum standards, competency frameworks and learning outcomes as structured, addressable documents. From the standards body |
| [1EdTech/digital-credentials-public-validator](https://github.com/1EdTech/digital-credentials-public-validator) | 🟢 **Apache-2.0** (`11,356 B`) | `main` | `2026-10-27` | `+01:00` | EMEA | Public validator for **Open Badges**; a deployment runs at `vc.1ed.tech` |
| [adlnet/xapi-profiles](https://github.com/adlnet/xapi-profiles) | 🟢 **Apache-2.0** (`11,356 B`) | `master` | `2024-12-16` | `-05:00` | North America | The **xAPI Profiles** spec from ADL. 🟡 Its own README flags a review/upgrade in progress following xAPI 2.0 / IEEE p9274.2.1 — read the IEEE base standard alongside it |
| [yetanalytics/xapipe](https://github.com/yetanalytics/xapipe) | 🟢 **Apache-2.0** (`11,356 B`) | `main` | `2026-08-18` | `-04:00` | North America | **LRSPipe** — xAPI middleware that governs data flow between layers *by xAPI Profile*, not just a statement forwarder |
| [yetanalytics/re-oidc](https://github.com/yetanalytics/re-oidc) | 🟢 **Apache-2.0** (`11,356 B`) | `main` | `2026-10-16` | `-04:00` | North America | OIDC for `re-frame`/`reagent` ClojureScript apps — the auth rung for the xAPI tooling above |
| [instructure/qti](https://github.com/instructure/qti) | 🟢 **MIT** (`1,083 B`) | `master` | `2026-09-23` | `+00:00` | North America | 🟢 QTI **1.2 and 2.1** importer gem, published by **Instructure** — the Canvas vendor's own assessment-import path |
| [agencyenterprise/qti-3-player](https://github.com/agencyenterprise/qti-3-player) | 🟢 **MIT** (`1,065 B`) | `main` | `2026-02-12` | `-03:00` | LATAM | Framework-agnostic **QTI 3.x** renderer with multi-frontend support; live sandbox demo |
| [openwallet-foundation-labs/learner-credential-wallet](https://github.com/openwallet-foundation-labs/learner-credential-wallet) | 🟢 **MIT** (`1,091 B`) | `main` | `2026-06-11` | `-04:00` | North America | Cross-platform iOS/Android wallet for **storing and sharing digital learner credentials**. OpenWallet Foundation Labs |
| [h5p/h5p-cli](https://github.com/h5p/h5p-cli) | 🟢 **MIT** (`1,065 B`) | `master` | `2026-10-27` | `+01:00` | EMEA | H5P toolkit for running, editing and **developing H5P content types**. 🔵 README at `readme.md` — one of the `603-C` six |

### 🟢 Analytics, assessment and detection — `12` more rows

| Repo | Grant (byte-read) | Branch | Pushed | tz | Region | What it is |
| --- | --- | --- | --- | --- | --- | --- |
| [openedx/tutor-contrib-aspects](https://github.com/openedx/tutor-contrib-aspects) | 🟢 **Apache-2.0** (`11,356 B`) | `main` | `2026-10-27` | `-04:00` | North America | 🟢 **Open edX Aspects** learner analytics as a Tutor plugin: ClickHouse + Apache Superset + OpenFUN **Ralph** (LRS, validates and stores xAPI) + Vector. 🔵 README at `README.rst` |
| [AI4Bharat/IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) | 🟢 **MIT** (`1,128 B`) | `main` | `2025-10-03` | `+05:30` | **APAC** | 🟢 Indic-language machine translation from **AI4Bharat / IIT Madras** — the realistic path to multilingual courseware across India's scheduled languages |
| [Sunbird-Lern/lms-service](https://github.com/Sunbird-Lern/lms-service) | 🟢 **MIT** (`1,071 B`) | `master` | `2026-01-05` | `+05:30` | **APAC** | LMS micro-service of **Sunbird**, the stack behind India's national education platforms |
| [project-sunbird/sunbird-lms-service](https://github.com/project-sunbird/sunbird-lms-service) | 🟢 **MIT** (`1,071 B`) | `master` | `2025-12-23` | `-08:00` | **APAC** | Sunbird **User/Org** micro-service. 🔵 Same grant bytes as the row above and a `-08:00` committer offset — a US-based committer on an India-origin platform, so `tz` places the *commit*, not the project |
| [stanfordnlp/edu-convokit](https://github.com/stanfordnlp/edu-convokit) | 🟢 **MIT** (`1,068 B`) | `main` | `2025-04-18` | `-07:00` | North America | **Edu-ConvoKit** — framework for education *conversation* data (NAACL 2024, Systems Track). The pre-processing layer for classroom-discourse analysis |
| [baoguangsheng/fast-detect-gpt](https://github.com/baoguangsheng/fast-detect-gpt) | 🟢 **MIT** (`1,070 B`) | `main` | `2026-02-07` | `+08:00` | APAC | **Fast-DetectGPT** (ICLR 2024) — zero-shot machine-generated-text detection via conditional probability curvature |
| [google/prog-edu-assistant](https://github.com/google/prog-edu-assistant) | 🟢 **Apache-2.0** (`11,357 B`) | `main` | `2024-01-16` | `+09:00` | APAC | Google's **autograding** toolset for programming education (notebook-based) |
| [Fuann/open-apa](https://github.com/Fuann/open-apa) | 🟢 **BSD** (`1,527 B`) | `master` | `2026-10-08` | `+08:00` | APAC | **OpenAPA** — open benchmark and evaluation toolkit for **pronunciation assessment** in open-response scenarios |
| [YuanGongND/gopt](https://github.com/YuanGongND/gopt) | 🟢 **BSD** (`1,516 B`) | `master` | `2023-02-13` | `-05:00` | North America | **GOPT** — transformer multi-aspect, multi-granularity pronunciation assessment for non-native English. 🔴 Dormant since `2023-02`: a research artifact to port, not a dependency to adopt |
| [vardanagarwal/Proctoring-AI](https://github.com/vardanagarwal/Proctoring-AI) | 🟢 **MIT** (`1,070 B`) | `master` | `2024-12-10` | `+05:30` | APAC | Automated proctoring over webcam + microphone, split into vision and audio functions. 🟡 Dormant since `2024-12` |
| [kitschpatrol/yanki](https://github.com/kitschpatrol/yanki) | 🟢 **MIT** (`1,070 B`, 🔵 `license.txt`) | `main` | `2026-10-27` | `-04:00` | North America | CLI + TypeScript library turning **Markdown into Anki flashcards**. 🔵 Lowercase `license.txt` *and* `readme.md` — this repo defeats a single-spelling probe on **both** channels |
| [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🟡 **split scope** — **MIT** (`1,091 B`, root, code in `pipeline/`) **+ CC BY 4.0** (`1,583 B`, 🔴 `dados/LICENSE.md`) | `main` | `2026-10-15` | `-03:00` | **LATAM** | 🟢 Brazil's **BNCC** extracted from official MEC/CNE PDFs by a reproducible pipeline. 🔴 **A root-only read publishes "MIT" for a payload that is CC BY 4.0** — see [`../verticals/solutions.md`](../verticals/solutions.md) |

### 🟡 Grant-clean but **not** promoted to this page, with the reason

| Repo | Grant (byte-read) | Why not |
| --- | --- | --- |
| [SafeExamBrowser/seb-server](https://github.com/SafeExamBrowser/seb-server) | 🟡 **MPL-2.0** (`16,724 B`) | Already instrumented on this base (`seb-proctoring-validator`, `sebserver-mcp-gate`); listed here only because it is one of the `603-C` six (`README.rst`) and its grant is now byte-read |
| [kaldi-asr/kaldi](https://github.com/kaldi-asr/kaldi) | 🔴 notice, not a grant | `COPYING` (`17,263 B`) is a **legal notice clarifying the Apache copyright headers**, not licence text. The grant is Apache-2.0 *by header convention*; **the root file is not the grant** and must not be cited as one |
| [ajjalti/EvalStudio](https://github.com/ajjalti/EvalStudio), [Lawrence-Public-Schools/OneRoster-1.1-PowerQueries](https://github.com/Lawrence-Public-Schools/OneRoster-1.1-PowerQueries) | 🟡 AGPL-3.0 (`33,060 B` / `34,522 B`) | Copyleft — usable, but not what Globant can build *on* under the permissive bar |
| [bgwdotdev/go-oneroster](https://github.com/bgwdotdev/go-oneroster) | MIT (`1,063 B`) | 🔴 Last push **`2019-11-04`** — seven years dormant. OneRoster coverage comes from `roster_hub_for_gigaschool` and the 1EdTech rows instead |

## 🆕 `p602` — reads `2026-11-02`, commit `2026-11-02` — **🟢 `26` FOUNDATION REPOS ADDED, EVERY ONE CONFIRMED **NOT HELD** BY A CORRECTED MATCHER, EVERY GRANT BYTE-READ AT THE REAL DEFAULT BRANCH, `65 of 65` FABRICATED-PATH CONTROLS AT `404`. 🟢 THE ADDITION IS A WHOLE LAYER: THE **MOODLE PLUGIN SUBSTRATE** — IN-LMS CODE SUBMISSION, AUTO-GRADING, ATTENDANCE, SSO AND OBJECT STORAGE. `11 of 13` NEW. 🔴 AND THE REASON IT WAS MISSING IS NOT A NEW MECHANISM: THIS BASE ALREADY DOCUMENTED BOTH `version.php` SOURCE-HEADER GRANTS AND VERSIONED DEFAULT BRANCHES — IT HAD SIMPLY NEVER SWEPT `topic:moodle` DEEPLY ENOUGH TO USE THEM.**

### 🔴 Credit where this pass found it already written, because the near-miss is instructive

🔴 **This pass drafted "the grant is in a source header" and "the default branch is a version number"
as new findings. Both are already on these pages** — `version.php` appears `56` times at `HEAD`, and
[`../verticals/solutions.md`](../verticals/solutions.md) already names
`openeducat/openeducat_erp`'s `19.0` branch with the note *"the branch is a version number, which no
`main` probe reads"*. 🟢 **So the honest account of why `11` maintained Moodle plugins were unheld is
narrower and more actionable: the knowledge existed and the *sweep* did not.** `topic:moodle` had been
mentioned `4` times and never walked to depth.
🔵 **The one branch name genuinely new this pass:** `MOODLE_404_STABLE`
([catalyst/moodle-tool_objectfs](https://github.com/catalyst/moodle-tool_objectfs)), joining the
already-held `MOODLE_503_STABLE` and `MOODLE_500_STABLE` — 🟢 confirming the family is **generated per
Moodle release**, so it is not enumerable and only the symref is a probe.

### 🟢 The Moodle plugin substrate — `11` new rows, grants byte-read `2026-11-02`

🟢 `(hdr)` marks a grant read from `version.php` rather than a grant file — this base's existing
source-header channel, applied to a layer it had not reached.

| Repo | ★ | Grant (byte-read) | Branch | Region | What it gives a studio |
| --- | --: | --- | --- | --- | --- |
| [C0D3D3V/Moodle-DL](https://github.com/C0D3D3V/Moodle-DL) | **660** | 🟢 GPL-3.0 (`35,141 B`) | `main` | Global | 🟢 Bulk course-content extraction — the ingest leg for any Moodle RAG corpus |
| [tmuras/moosh](https://github.com/tmuras/moosh) | **262** | 🟢 GPL-3.0 (`35,149 B`) | `master` | Global | 🟢 **Moodle shell**: scriptable admin over `100+` commands — an agent's hands inside Moodle |
| [moodlebox/moodlebox](https://github.com/moodlebox/moodlebox) | `145` | 🟡 AGPL-3.0 (`34,523 B`) | `main` | Global | 🟢 Moodle + Wi-Fi AP on a Raspberry Pi — the offline / low-connectivity deployment shape |
| [jcrodriguez-dis/moodle-mod_vpl](https://github.com/jcrodriguez-dis/moodle-mod_vpl) | `128` | 🟢 GPL-3.0 (`35,147 B`) | `master` | Global | 🟢 **Virtual Programming Lab**: in-LMS code submission + automatic grading. Pushed `2026-11-01` |
| [hit-moodle/moodle-local_onlinejudge](https://github.com/hit-moodle/moodle-local_onlinejudge) | `124` | 🟢 GPL-3.0 (`35,147 B`) | `master` | Global | Online-judge scoring backend for `mod_vpl` submissions |
| [moodle-an-hochschulen/moodle-theme_boost_union](https://github.com/moodle-an-hochschulen/moodle-theme_boost_union) | `106` | 🟢 GPL-3.0 (`35,147 B`) | `main` | **EMEA** | The higher-ed theme layer; German university consortium |
| [catalyst/moodle-tool_objectfs](https://github.com/catalyst/moodle-tool_objectfs) | `102` | 🟢 GPL-3.0 *(hdr)* | 🔴 `MOODLE_404_STABLE` | Global | Offload Moodle files to S3/Azure — prerequisite for large media at scale |
| [FMCorz/mdk](https://github.com/FMCorz/mdk) | `99` | 🟢 GPL-3.0 (`35,147 B`) | `master` | Global | Moodle Development Kit — spin instances up and down for CI |
| [danmarsden/moodle-mod_attendance](https://github.com/danmarsden/moodle-mod_attendance) | `91` | 🟢 GPL-3.0 *(hdr)* | 🔴 `MOODLE_503_STABLE` | Global | Attendance log — the signal most early-warning models actually need |
| [erseco/alpine-moodle](https://github.com/erseco/alpine-moodle) | `88` | 🟢 **MIT** (`1,072 B`) | `main` | Global | 🟢 **The only permissively licensed Moodle packaging found** — Alpine container image |
| [catalyst/moodle-auth_saml2](https://github.com/catalyst/moodle-auth_saml2) | `87` | 🟢 GPL-3.0 *(hdr)* | 🔴 `MOODLE_500_STABLE` | Global | SAML SSO entirely inside Moodle — the institutional-identity gate |

🟡 **Reciprocity limit, which decides how these are used.** `10 of 11` are GPL-3.0-or-later or
AGPL-3.0. 🟢 Correct and safe **as a plugin deployment** inside a GPL host; 🔴 **not a basis for
lifting code into a proprietary product.** 🟢 **The composable seam is `moosh`** (drive Moodle from
outside over its CLI) **and `Moodle-DL`** (extract to your own corpus) — not vendoring plugin source.
`erseco/alpine-moodle` is the one MIT artefact and it is *packaging*.
🔵 Already held and therefore **not** re-added: `FMCorz/moodle-block_xp`, `h5p/moodle-mod_hvp`.

### 🟢 Open edX substrate — `4` new rows, including the one MIT analytics app

| Repo | ★ | Grant (byte-read) | Branch | Region | What it gives |
| --- | --: | --- | --- | --- | --- |
| [openfun/openedx-docker](https://github.com/openfun/openedx-docker) | `142` | 🟡 AGPL-3.0 (`34,520 B`) | `master` | Global | Best-practice Open edX image; 🟡 last push `2025-07-09` — reference, not dependency |
| [cookiecutter-openedx/cookiecutter-openedx-devops](https://github.com/cookiecutter-openedx/cookiecutter-openedx-devops) | `50` | 🟡 AGPL-3.0 (`35,136 B`) | `main` | Global | Tutor on Kubernetes via Terraform |
| [appsembler/figures](https://github.com/appsembler/figures) | `44` | 🟢 **MIT** (`1,078 B`) | `main` | Global | 🟢 Reporting + data retrieval for Open edX — **MIT**, so the analytics layer *is* liftable |
| [eduNEXT/tvm](https://github.com/eduNEXT/tvm) | `24` | 🟡 AGPL-3.0 (`34,523 B`) | `main` | **LATAM** | Tutor version/environment manager — multi-version Open edX operations |

🔵 **The licence split is the plan:** `3 of 4` are AGPL-3.0 — fine to **operate** as a service
provider, 🔴 fatal to redistribute as a product. 🟢 **`figures` is the commercial surface.**

### 🟢 LTI — `5` new rows on the interoperability layer

🔴 **Caution: `topic:lti` is polysemous.** The axis also returns **Linear Time-Invariant** control and
DSP libraries ([kmilo17pet/qlibs](https://github.com/kmilo17pet/qlibs), `104★`;
[jrgenerative/fixed-wing-sim](https://github.com/jrgenerative/fixed-wing-sim), `164★`). 🔵 This base
already carries the *`tooLTIp` / `muLTI-tenancy`* substring defect as `P831`; 🟢 **the `topic:`-level
collision between Learning Tools Interoperability and Linear Time-Invariant is new** and is a
*different* mechanism — a tag two communities both apply correctly.

| Repo | ★ | Grant (byte-read) | Branch | Region | Note |
| --- | --: | --- | --- | --- | --- |
| [csev/wa4e](https://github.com/csev/wa4e) | `216` | 🟢 BSD-2-Clause (`1,301 B`) | `master` | Global | 🟢 Course materials from an **LTI spec co-author**; pushed `2026-11-01` |
| [WebPA/WebPA](https://github.com/WebPA/WebPA) | `37` | 🟢 GPL-3.0 (`35,147 B`, 🔴 `license.txt`) | `master` | Global | Online **peer assessment** — a scoring mode nothing else here covers |
| [doldsimo/lti-1.3-canvas-lms](https://github.com/doldsimo/lti-1.3-canvas-lms) | `29` | 🟢 MIT (`1,067 B`) | `main` | Global | Minimal LTI 1.3 ↔ Canvas reference |
| [js-kyle/nodejs-lti-provider](https://github.com/js-kyle/nodejs-lti-provider) | `26` | 🟢 MIT (`1,067 B`, 🔴 `LICENCE`) | `master` | Global | Node LTI provider; 🔵 grant at the **British** spelling |
| [ucfopen/lti-template-flask](https://github.com/ucfopen/lti-template-flask) | `47` | 🟢 MIT (`1,130 B`) | `master` | Global | 🔴 **Marked `DEPRECATED` in its own description.** Reference only |

### 🟡 Autograding — `4` new rows, real and permissive, and mostly stale

| Repo | ★ | Grant (byte-read) | Branch | Last push | Verdict |
| --- | --: | --- | --- | --- | --- |
| [illinois-cs241/broadway](https://github.com/illinois-cs241/broadway) | `19` | 🟢 **MIT** (`1,681 B`) | `master` | `2024-09-04` | 🟢 API said `NOASSERTION`; the bytes say MIT |
| [tkutcher/jgrade](https://github.com/tkutcher/jgrade) | `26` | 🟢 MIT (`1,070 B`) | 🔴 `dev` | 🔴 `2023-08-16` | 🟡 Java assignment grading; Gradescope JSON |
| [imgVOID/autograding-api](https://github.com/imgVOID/autograding-api) | `15` | 🟢 Apache-2.0 (`11,357 B`) | `master` | 🔴 `2022-01-10` | 🟡 Pattern, not a dependency |
| [RiceComp215-Staff/RiceChecks](https://github.com/RiceComp215-Staff/RiceChecks) | `12` | 🟢 Apache-2.0 (`11,357 B`) | `master` | 🔴 `2023-01-09` | 🟡 Gradle-based Java autograder |

🔵 **Read with the Moodle rows, this is the honest state of open autograding:** the **stale** artefacts
are the standalone services; the **live** one is the LMS plugin (`moodle-mod_vpl`, pushed
`2026-11-01`). 🟢 **The maintained path for grading runs inside the LMS.**

### 🟡 One grant defect worth recording, caught in this pass's own ladder

🔴 This pass's first ladder carried `LICENSE`, `LICENSE.md`, `LICENSE.txt` and bare lowercase
`license` — **but not `license.txt`**, which `p600` had already measured on `frappe/education`.
🔴 The first run therefore reported `WebPA/WebPA` and `navariltd/Junior-School` as grantless.
🟢 Extending the ladder to lowercase-with-extension recovered both (`35,147 B` GPL-3.0 and
`34,523 B` AGPL-3.0). 🔵 **`lib/README.md`'s rule landing again: a rule that has to be remembered is
not a control.** The fix and the `p600` citation are in
[`../compose/code/p602-axis-sweep/verify.sh`](../compose/code/p602-axis-sweep/verify.sh).

Evidence: [`../evidence/grants-byteread.2026-11-02-p602.tsv`](../evidence/grants-byteread.2026-11-02-p602.tsv)
(`65` rows, `65 of 65` controls `404`),
[`../evidence/held-set-matcher-correction.2026-11-02-p602.tsv`](../evidence/held-set-matcher-correction.2026-11-02-p602.tsv).

## 🆕 `p601` — reads `2026-11-01`, commit `2026-11-02` — **🟢 `17` FOUNDATION REPOS ADDED, EVERY GRANT BYTE-READ AT THE REAL DEFAULT BRANCH WITH ITS OWN FABRICATED-PATH CONTROL (`55 of 55` AT `404`). 🟢 THE TWO THAT MATTER MOST ARE AN ASSESSMENT-DELIVERY ENGINE (`4,918★` MIT) AND A SECOND, APAC-BUILT ONE (`3,803★` APACHE-2.0, DIDI) — THIS BASE HAD NEITHER, AND BOTH CLOSE THE "SCORING SEAM" IT HAS CARRIED FOR MANY PASSES. 🔴 `TheOdinProject` (`13,200★`), THE LARGEST OPEN CURRICULUM ESTATE FOUND, IS `CC BY-NC-SA` AND IS **NOT** ADDED.**

### 🟢 Assessment & form delivery — the layer every tutoring recipe on `compose/patterns.md` assumed and none named

| Repo | ★ | Grant (byte-read `2026-11-01`) | Branch | Region | Role |
| --- | --: | --- | --- | --- | --- |
| [surveyjs/survey-library](https://github.com/surveyjs/survey-library) | **4,918** | 🟢 MIT (`1,102 B`) | 🔴 `master` | **EMEA** | JSON-driven form/quiz runtime for React, Angular, Vue, vanilla. Devsoft Baltic OÜ (EE). 🟢 **The item-rendering layer — JSON in, scored response out** |
| [didi/xiaoju-survey](https://github.com/didi/xiaoju-survey) | **3,803** | 🟢 Apache-2.0 (`11,412 B`) | `main` | **APAC** | DiDi's questionnaire/exam/quiz platform *with* analytics — a deployable service, not a library |
| [nymanjens/quizmaster](https://github.com/nymanjens/quizmaster) | `327` | 🟢 Apache-2.0 (`591 B`) | 🔴 `master` | Global | Live synchronous quiz runner — the proctored-session shape |
| [2anki/2anki.net](https://github.com/2anki/2anki.net) | `328` | 🟢 MIT (`LICENSE.md`, `1,310 B`) | `main` | Global | Notion → Anki deck conversion; pairs with the spaced-repetition tier `p600` opened on `verticals/solutions.md` |

🔵 **Why this is a foundation and not an agent.** `p600` shelved `agenticfabriq/beacon` as a free-text
*grading* harness and noted the scoring seam `nbgrader` leaves open. 🟢 **These four are the other half
of that seam — delivery and capture.** An agent that generates items had nowhere to render them; it
does now, under MIT and Apache-2.0.

### 🟢 Teaching-systems courseware — permissive, maintained, university-originated

| Repo | ★ | Grant (byte-read) | Branch | Region | Role |
| --- | --: | --- | --- | --- | --- |
| [git-learning-game/oh-my-git](https://github.com/git-learning-game/oh-my-git) | **2,906** | 🟢 **Blue Oak Model 1.0.0** (`1,552 B`) | `main` | Global | 🟡 Interactive Git game. **A licence class new to this page** — OSI-approved, permissive, patent-explicit |
| [cksystemsteaching/selfie](https://github.com/cksystemsteaching/selfie) | **2,534** | 🟢 BSD-2-Clause (`1,306 B`) | `main` | **EMEA** | Self-compiling C compiler + RISC-V emulator + hypervisor. **University of Salzburg (AT)** — a whole systems curriculum as runnable code |
| [beir-cellar/beir](https://github.com/beir-cellar/beir) | **2,327** | 🟢 Apache-2.0 (`11,348 B`) | `main` | Global | 🟢 `15+`-dataset retrieval benchmark — **the missing evaluation harness for any RAG tutor** on this base |
| [translate-tools/linguist](https://github.com/translate-tools/linguist) | **1,082** | 🟢 BSD-3-Clause (`1,542 B`) | 🔴 `master` | Global | Offline-capable translation engine — the in-language courseware axis |
| [open-scratch/teaching-open](https://github.com/open-scratch/teaching-open) | `633` | 🟢 Apache-2.0 (`11,371 B`) | 🔴 `master` | **APAC** | Scratch/ScratchJr/Python teaching platform **with** courses, classes, assignments, permissions — CN-built |
| [cxli233/Online_R_learning](https://github.com/cxli233/Online_R_learning) | `554` | 🟢 **CC0-1.0** (`LICENSE.md`, `7,048 B`) | 🔴 `master` | Global | Applied-statistics course; 🟢 public-domain dedication — the least encumbered content on this page |
| [skaiui2/SKRTOS_sparrow](https://github.com/skaiui2/SKRTOS_sparrow) | `501` | 🟢 MIT (`1,066 B`) | `main` | Global | Modular RTOS microkernel written to be *taught* — embedded-systems curriculum |
| [tristcoil/hanabira.org](https://github.com/tristcoil/hanabira.org) | `432` | 🟢 MIT (`1,061 B`) | `main` | **APAC** | Self-hostable Japanese **and** Korean learning portal |
| [rampaa/JL](https://github.com/rampaa/JL) | `404` | 🟢 Apache-2.0 (`11,357 B`) | 🔴 `master` | **APAC** | Japanese lookup engine — the in-language reading-support primitive |
| [danzen/zimjs](https://github.com/danzen/zimjs) | — | 🟢 MIT (`LICENSE.txt`, `1,126 B`) | 🔴 `master` | Global | Canvas creative-coding framework used for interactive learning objects |

### 🟢 Institutional & research scaffolding

| Repo | ★ | Grant (byte-read) | Branch | Region | Role |
| --- | --: | --- | --- | --- | --- |
| [Attendize/Attendize](https://github.com/Attendize/Attendize) | **4,283** | 🟢 **Attribution Assurance Licence** (`2,073 B`) | 🔴 **`develop`** | Global | Ticketing/attendee management — the open-day, orientation and CPD-event shape. 🟡 AAL is OSI-approved and rare; read the attribution clause before white-labelling |
| [AhmadHassan-BTed/Attendify](https://github.com/AhmadHassan-BTed/Attendify) | **3,836** | 🟢 MIT (`1,056 B`) | `main` | Global | Attendance **and leave** portal — the one substantial permissive repo in an axis that is otherwise `43–138★` student projects |
| [usnistgov/OSCAL](https://github.com/usnistgov/OSCAL) | — | 🟢 **US worldwide public domain** (`LICENSE.md`, `5,255 B`) | `main` | **North America** | Machine-readable control catalogues — the instrument for evidencing FERPA/COPPA posture to a US district or system office |
| [latextemplates/scientific-thesis-template](https://github.com/latextemplates/scientific-thesis-template) | `397` | 🟡 **`0BSD`** (`665 B`) — 🔴 **copyright line is an unfilled template: `[year] [fullname]`** | `main` | **EMEA** | Thesis template estate. 🟢 `0BSD` requires no attribution so the grant still operates; the defect is recorded (`601-D`), not hidden |

### 🔴 Found, larger than anything above, and deliberately NOT added

| Repo | ★ | Grant (byte-read) | Why excluded |
| --- | --: | --- | --- |
| [TheOdinProject/curriculum](https://github.com/TheOdinProject/curriculum) | **13,200** | 🔴 **CC BY-NC-SA 4.0** (`license.md`, `442 B`) | 🔴 `NonCommercial` **and** `ShareAlike`. The largest open web-dev curriculum in the sector and it cannot enter paid delivery |
| [TheOdinProject/theodinproject](https://github.com/TheOdinProject/theodinproject) | `4,675` | 🔴 **no grant file** at `main` (API claims `MIT`) | `601-C` — API asserts what no byte-read can confirm. **`ABSTAIN`** |
| [Techtonica/curriculum](https://github.com/Techtonica/curriculum) | `670` | 🔴 **no grant file** at `main` (API claims `CC-BY-SA-4.0`) | `601-C`. **`ABSTAIN`** |
| [sobolevn/the-best-python-course](https://github.com/sobolevn/the-best-python-course) | — | 🔴 CC BY-NC-SA (`19,738 B`) | NonCommercial |
| [Allenpandas/BJTU-CS-Notebook](https://github.com/Allenpandas/BJTU-CS-Notebook) | — | 🔴 CC BY-NC-SA (`14,978 B`) | NonCommercial — APAC-placed, and still unusable |
| [cvut/qtrvsim](https://github.com/cvut/qtrvsim) | `647` | 🟡 GPL-3.0 (`35,141 B`) | Reciprocal. Czech Technical University; usable as a *tool*, not as vendored code |

🔵 **The pattern worth carrying forward, because it is the opposite of the usual one.** Across `29`
`NOASSERTION` rows byte-read this pass, **the four highest star counts were all commercially
unusable** and the permissive supply sat in the `300–4,900★` band beneath them. 🟢 **In education,
rank the shortlist by grant first and stars second** — courseware is the sector's biggest artefact
class and `NC` is its default choice.
Evidence: [`../evidence/grants-byteread.2026-11-01-p601.tsv`](../evidence/grants-byteread.2026-11-01-p601.tsv).

## 🆕 `p600` — `2026-11-01` — an `81`-repo BSD-3-Clause university curriculum estate was invisible for `599` passes, and the thing hiding it was a branch name

### 🟢 `600-D` — the find, and both mechanisms that concealed it

[`MathWorks-Teaching-Resources`](https://github.com/MathWorks-Teaching-Resources) — **`81`
repositories**, overwhelmingly **BSD-3-Clause**, institution-targeted undergraduate courseware
(fluid dynamics, thermodynamics, Fourier analysis, control systems, robotics, numerical methods,
programming fundamentals). 🔴 **`0 of 81` held in this base before this pass.**

| default branch | repos | share |
| --- | --: | --: |
| 🔴 **`release`** | **`59`** | 🔴 **`72.8 %`** |
| `main` | `21` | `25.9 %` |
| `master` | `1` | `1.2 %` |

🔴 **Mechanism 1 — the branch.** A probe that tries `main`, then `master`, resolves **nothing** for
`59 of 81` of this org and reports them as having no licence file. This page's own `p599` census found
`master` was the surprise in education (*"education's platforms are old enough that `master` is still
the norm"*). 🔵 **`release` is a third pattern, and it is the majority one inside the largest
permissive curriculum publisher this base has found.**

🔴 **Mechanism 2 — the axis set.** These repos are tagged with MATLAB and subject-matter topics and
🔴 **carry no education topic at all**, so no `topic:lms` / `topic:ai-tutor` / `topic:courseware` query
reaches them. They were found through a subject-keyword axis, which is `600-C`'s point made concrete.

🟡 **The caveat is published with the find, not after it.** These are **MATLAB/Simulink** modules:
🟢 the *content* is BSD-3-Clause and freely redistributable, 🔴 the *runtime* is commercial. 🔵 **So
they are curriculum assets for an engineering-faculty engagement, not an open software stack** — and
they are the strongest answer this base holds to *"we need accredited-quality STEM course content we
are allowed to modify and rebrand"*, which no agent on these pages supplies.

### 🟢 Promoted to the enablement tier — grants byte-read `2026-11-01` at the real default branch

| repo | ★ | grant (byte-read) | branch | fab-path control |
| --- | --: | --- | --- | --: |
| [Computational-Fluid-Dynamics](https://github.com/MathWorks-Teaching-Resources/Computational-Fluid-Dynamics) | **210** | 🟢 **BSD-3-Clause** (`LICENSE`, `1,527 B`) | `main` | 🟢 `404` |
| [Fourier-Analysis](https://github.com/MathWorks-Teaching-Resources/Fourier-Analysis) | **143** | 🟢 **BSD-3-Clause** (`LICENSE.md`, `1,528 B`) | 🔴 **`release`** | 🟢 `404` |
| [Virtual-Controls-Laboratory](https://github.com/MathWorks-Teaching-Resources/Virtual-Controls-Laboratory) | **109** | 🟢 **BSD-3-Clause** (`1,528 B`) | 🔴 **`release`** | 🟢 `404` |
| [Thermodynamics](https://github.com/MathWorks-Teaching-Resources/Thermodynamics) | **43** | 🟢 **BSD-3-Clause** (`1,528 B`) | 🔴 **`release`** | 🟢 `404` |
| [Robotic-Manipulators](https://github.com/MathWorks-Teaching-Resources/Robotic-Manipulators) | **37** | 🟢 **BSD-3-Clause** (`1,528 B`) | 🔴 **`release`** | 🟢 `404` |
| [Fundamentals-of-Programming](https://github.com/MathWorks-Teaching-Resources/Fundamentals-of-Programming) | **37** | 🟢 **BSD-3-Clause** (`1,528 B`) | 🔴 **`release`** | 🟢 `404` |
| [Fluid-Mechanics](https://github.com/MathWorks-Teaching-Resources/Fluid-Mechanics) | **30** | 🟢 **BSD-3-Clause** (`1,528 B`) | 🔴 **`release`** | 🟢 `404` |

🔵 **The `1,527 B` vs `1,528 B` split is the copyright year line**, not a licence difference — all
seven are the three-clause BSD text with *The MathWorks, Inc.* as holder. `74` further repos in the
org carry the same grant shape and are listed in the census rather than individually promoted:
[`../evidence/mathworks-curriculum-census.2026-11-01-p600.tsv`](../evidence/mathworks-curriculum-census.2026-11-01-p600.tsv).

### 🟢 The spaced-repetition component tier — concepts held, implementations missing

🔵 **`FSRS` appears in `318` files of this base and `anki` in `485`**, so this base has argued about
retention scheduling for hundreds of passes while holding almost none of the software that implements
it. Grants byte-read this pass:

| repo | ★ | grant (byte-read) | branch | disposition |
| --- | --: | --- | --- | --- |
| [reuseman/flashcards-obsidian](https://github.com/reuseman/flashcards-obsidian) | **1,113** | 🟢 **MIT** (`1,069 B`) | `main` | 🟢 **Promote** — pushed `2026-10-31`, live |
| [shaankhosla/repeater](https://github.com/shaankhosla/repeater) | **442** | 🟢 **Apache-2.0** (`11,357 B`) | `main` | 🟢 **Promote** — terminal-native, trivially embeddable |
| [lakesare/memcode](https://github.com/lakesare/memcode) | **408** | 🟢 **MIT** (`1,080 B`) | 🔴 **`master`** | 🟢 **Promote** — live; a `600-E` row |
| [olmps/memo](https://github.com/olmps/memo) | **1,871** | 🟢 **BSD-3-Clause** (`1,515 B`) | `main` | 🟡 **Reference only** — last push `2024-07-29` |
| [hwgilbert16/scholarsome](https://github.com/hwgilbert16/scholarsome) | **793** | 🔴 **AGPL-3.0** (`34,523 B`) | 🔴 **`develop`** | 🔴 **Flagged** — reciprocal |
| [mnemosyne-proj/mnemosyne](https://github.com/mnemosyne-proj/mnemosyne) | **605** | 🔴 **pointer, not a grant** (`156 B`) | `master` | 🔴 **BLOCK** — `600-G` |

🔴 **`3 of 6` of this tier are not on `main`** (`master`, `master`, `develop`), which is `600-E` once
more and the reason every branch above was resolved with `git ls-remote --symref` **and**
cross-checked against `search/repositories` before any byte was read.

### 🟢 `600-A` — this page gets a second branch oracle, and `p599`'s branch calls are confirmed

`p599` recorded `Cvmcosta/ltijs` and `openedx/openedx-platform` as `master`. 🟢 **Independently
confirmed this pass by a channel this base believed was unavailable:**
`search/repositories?q=repo:<owner>/<name>` returns `default_branch`, `stargazers_count`,
`license.spdx_id`, `forks_count` and `pushed_at`, and it **agrees with `git ls-remote --symref` on
`16 of 16` repositories measured.** 🔴 The per-repo endpoint `repos/<owner>/<repo>` is unusable here —
it returns `403` for real addresses **and for a fabricated control**, so it carries no information.
🔵 **`git ls-remote --symref` stays the mandated first step** (it is the git-layer truth and needs no
API quota); the search channel is now the cheap cross-check, and it caught nothing wrong this pass.

---

## 🆕 `p599` — `2026-11-01` — the foundational tier is `100 %` held on every star-ranked channel, and `2 of 7` components re-read this pass do not live on `main`

### 🟢 `0` additions, and the `0` is measured rather than asserted

Three topic heads that feed this page were walked star-ranked and every address on each first page
was checked against this whole base before being called new: **`topic:lms` (`2,615` repos) → `13`
addresses, `13` held; `topic:knowledge-tracing` (`102`) → `7`, `7` held; `topic:grading` (`283`) →
`9`, `9` held.** 🔴 **`29 of 29`, `0` new.** Full tables, with per-address hit counts, in
[`trending.md`](trending.md).

🔵 **The result is not that the tier is complete; it is that the star ranking returns this base.**
Re-ordering the same channel by push date (`?o=desc&s=updated`) served `3` addresses never held here —
all `≤ 4★`, none shelvable, `1` carrying a bespoke non-commercial grant (`599-B`, `599-C`).
🟢 **For this page specifically that is a clean result: the foundational tier *is* the high-star band,
so a channel that only reaches the sub-`5★` tail genuinely has nothing to add here.** The nil on
`repos/foundations.md` is real; the nil on `agents/*` was an artefact.

### 🔴 Branch resolution is now a majority problem, not an edge case

`7` components were byte-read at their real default branch this pass to support the new recipes in
[`../compose/patterns.md`](../compose/patterns.md). 🔴 **`2 of 7` are not on `main`:**

| repo | real default branch | grant byte-read `2026-11-01` | what a `main`-only probe reports |
| --- | --- | --- | --- |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🔴 **`master`** | 🟢 Apache-2.0 (`11,361 B`) | 🔴 no licence file |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 **`master`** | 🔴 AGPL-3.0 (`35,136 B`) | 🔴 no licence file |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | `main` | 🟢 MIT (`1,141 B`) | correct |
| [pguso/agents-from-scratch](https://github.com/pguso/agents-from-scratch) | `main` | 🟢 MIT (`1,091 B`) | correct |
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | `main` | 🟢 MIT (`1,071 B`) | correct |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | `main` | 🟢 BSD-3-Clause (`1,512 B`) | correct |
| [inducer/relate](https://github.com/inducer/relate) | `main` | 🟢 MIT/X Consortium (`1,145 B`) | correct |

🔵 **Add `EduPilot` (`master`) and `openeducat_erp` (`19.0`) from this same pass and the rate is
`4 of 9`.** `p593`'s finding that a branch-hardcoding instrument *"fails silently on exactly the rows
it exists to rescue"* is not a rare failure mode in this industry — education's platforms are old
enough that `master` is still the norm among them. 🟢 **Mandatory order of operations, re-affirmed:
`git ls-remote --symref` first, grant second.**

### 🟡 A small correction to this page's own citation rule

This page records that `openedx/edx-platform` *"is the pre-rename name and the API rejects it with
`422`"*. 🟢 **True of `api.github.com` and still worth the warning** — but measured this pass,
`git ls-remote` on the **old** address resolves normally (GitHub follows the rename) and
`raw.githubusercontent.com` served its `35,136 B` AGPL-3.0 grant from it. 🔵 **Which explains why the
dead address keeps being cited: the git-layer oracles never punish it.** The warning should read
*"the API rejects it; git does not"*, so a reader does not conclude the old slug is broken everywhere
and trust a citation that happens to work.

### 🔴 `Gap 372` re-tested from a new direction and it does not move

*No permissive, production-grade library for automated essay grading.* Approached this pass through
`topic:essay-grading` (`17` repos, **all held**, `129` files) and a dedicated search leg. 🔴 The one
address the leg advertised as *"an open-source solution for automated essay evaluation"* —
[`Jatin-Mehra119/Essay-Scoring-Modeling`](https://github.com/Jatin-Mehra119/Essay-Scoring-Modeling) —
has **no grant file on `6` path variants**, byte-read `2026-11-01` at `main`. 🟢 The permissive
option remains [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) (Apache-2.0, `1,865 B`, the
`arXiv:2608.17356` system), already held here. 🔵 **Unchanged conclusion, now triangulated: the
activity the AI Act names as high-risk most explicitly is the one with the thinnest open supply, and
what supply exists is research-grade or unlicensed.**

---


🆕 **`p598` — `4` foundational rows promoted, every grant byte-read at the repository's real default
branch (`3 of 4` are not `main`), and one of them is permissive under a licence the GitHub API
reports as `NOASSERTION`.**

🔵 **Four, not five.** This page's standing bar is five new rows per pass. `6` `gh api` topic axes
were swept this pass — `topic:autograder`, `topic:lms topic:ai`, `topic:learning-analytics`,
`topic:ai-tutor`, `topic:education topic:llm`, `topic:spaced-repetition topic:ai` — returning `47`
candidate addresses, of which `35` were already on a shelf page and `11` sat in the append-only log
only. 🔴 **Of the `12` then byte-read, `1` is copyleft (`infomark-org/infomark`, GPL-3.0) and `7`
belong on the agent and platform pages, not this one.** The remaining four are below. 🟢 The two
nearest misses are recorded rather than promoted:
[`Apereo-LAI/OpenLRS`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS) (`47★`,
ECL-2.0 byte-read `11,087 B`) was last pushed **`2019-01-31`** and
[`OpenDashboard-legacy`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy)
(`47★`, ECL-2.0 `9,919 B`) names itself legacy. 🔵 **Fewer real rows beat padding**, and a reader
can now see exactly which addresses were considered and refused.

🔴 **The instrument note that governs the new rows (`598-A`).** A missing `LICENSE` file is **not**
evidence of a missing grant: a Maven, npm or Python project may declare its licence only in its
build manifest, and this base probed `13` filename variants and `0` manifests until this pass. The
audit of every 🔴 "no licence file" row on these pages is in
[`../evidence/manifest-channel-audit.2026-11-01-p598.tsv`](../evidence/manifest-channel-audit.2026-11-01-p598.tsv)
— 🟢 `15 of 16` of those BLOCK grades survived it.

### 🟢 Promoted this pass — grants byte-read `2026-11-01`

| Repo | ★ | Grant (byte-read) | Branch | Last push | Why it is foundational here |
| --- | --: | --- | --- | --- | --- |
| [kabartay/openunivcourses](https://github.com/kabartay/openunivcourses) | **254** | 🟢 **MIT** (`1,076 B`) | `main` | `2026-10-18` | A searchable index of free MIT, Stanford, Berkeley, CMU, NYU and UChicago courses, **every yearly edition and lecture video linked**. 🔵 The corpus layer: a licensed, structured pointer set to curriculum a studio can build retrieval over without licensing content itself |
| [Apereo-LAI/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | **62** | 🟢 **ECL-2.0** (`9,878 B`) 🔴 API says `NOASSERTION` | 🔴 `master` | 🟡 `2025-09-12` | Standards-based **learning record warehouse** — xAPI/Caliper store for learning analytics, from the Apereo consortium. 🟡 `13` months stale: take it as the **reference schema** for a learning-record store, not a live dependency. 🔵 Its licence is the sector's own (`598-D`) |
| [gradescope/gradescope-utils](https://github.com/gradescope/gradescope-utils) | **38** | 🟢 **MIT** (`1,070 B`) | 🔴 `master` | `2026-08-14` | The Python package for **building Gradescope autograders**, published by Gradescope itself. 🔵 `38★` and institution-grade: a star-ranked screen cannot see it, which is the mechanism `p596` recorded for FOLIO and `p597` for Ed-Fi |
| [quickfeed/quickfeed](https://github.com/quickfeed/quickfeed) | 27 | 🟢 **MIT** (`1,115 B`) | 🔴 `master` | `2026-10-27` | 🆕 **The one address this pass found in neither channel.** Go/TypeScript server + frontend giving **instant automated feedback on programming assignments**, with GitHub-org-per-course enrolment. 🔵 The permissive replacement for `infomark-org/infomark` (GPL-3.0) |

---

🆕 **`p597` — `7` foundational rows promoted off the `596-C` backlog, every grant byte-read at the
repository's *real* default branch (`3 of 7` are not `main`).** 🔵 **Not one required a search leg:**
all seven were on a shelf page in an archived snapshot and were dropped by a wholesale rewrite, and
[`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) — the largest of them — had been
shelved in 🔴 **`13` of `15`** snapshots before vanishing.

🔴 **The instrument note that governs this page.** `curl -sI https://github.com/...` returns `403`
here for any repository not attached to the session, so it is **not** a liveness test (`597-A`).
Every row below was established at `raw.githubusercontent.com`, which served `200` and the full
licence bytes in all cases. Rows marked **(bytes)** had their grant read as text, not taken from the
GitHub API's `spdx_id` field — which `597-B` measured wrong in three different ways in one pass.

### 🟢 Promoted this pass — the platform and component tier, recovered

| Repo | ★ | Grant (byte-read) | Branch | Last push | Size | Role in an education engagement |
| --- | --: | --- | --- | --- | --: | --- |
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | **8,360** | 🟢 **BSD-3-Clause** (`1,475 B`, bytes) | `main` | 🟢 `2026-11-01` | `37.8 MB` | Multi-user notebook server — **the compute substrate for every CS/data course**. Per-student isolated environments, pluggable auth. Shelved `13×`, dropped |
| [autolab/autolab](https://github.com/autolab/autolab) | **808** | 🟢 **Apache-2.0** (`11,324 B`, bytes) | 🔴 `master` | `2026-10-27` | `11.6 MB` | Carnegie Mellon's course-management service with **auto-graded programming assignments** — the grading system of record a studio attaches to, not replaces |
| [anubislms/anubis](https://github.com/anubislms/anubis) | **382** | 🟢 **MIT** (`1,083 B`, bytes) | `main` | `2026-09-15` | `21.7 MB` | NYU's distributed LMS for automating computing-science courses — per-student cloud IDE + autograding pipeline |
| [open-spaced-repetition/fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) | **455** | 🟢 **BSD-3-Clause** (`1,509 B`, bytes) | `main` | `2026-10-28` | `2.3 MB` | FSRS optimiser **and** scheduler in Rust — the retention engine. 🔵 A real algorithm with published parameters, not a prompt |
| [ed-fi-alliance-oss/edfi-oneroster](https://github.com/ed-fi-alliance-oss/edfi-oneroster) | **6** | 🟢 **Apache-2.0** (`10,173 B`, bytes) | `main` | `2026-10-31` | `1.0 MB` | Serves a **OneRoster 1.2 API from an Ed-Fi ODS** — the roster seam for US K-12 districts. 🔵 `6★` and institution-grade; a star screen cannot see it |
| [oaknational/oak-open-curriculum-ecosystem](https://github.com/oaknational/oak-open-curriculum-ecosystem) | **8** | 🟢 **MIT** — file spelled **`LICENCE`** (`1,086 B`, bytes) | `main` | 🟢 `2026-11-01` | `201 MB` | Oak National Academy's open curriculum via **API, SDK and a shipped MCP app**. 🔵 **EMEA/UK, and already agent-addressable** |
| [open-edge-platform/education-ai-suite](https://github.com/open-edge-platform/education-ai-suite) | **2** | 🟢 **Apache-2.0** (`11,351 B`, bytes) | `main` | `2026-10-30` | `102 MB` | Intel's education reference applications and libraries — edge/on-prem inference where data cannot leave the institution |

### 🔴 Rows measured this pass and deliberately NOT promoted

| Repo | ★ | Measured | Why not |
| --- | --: | --- | --- |
| [formalms/formalms](https://github.com/formalms/formalms) | 37 | 🔴 **no licence field**, live `2026-07-17`, `112 MB` | A full LMS with **no grant** — `BLOCK`. The largest unlicensed platform this base has measured |
| [1edtech/caliper-spec](https://github.com/1edtech/caliper-spec) | 22 | 🔴 `NOASSERTION`, pushed `2025-10-07` | The learning-analytics spec itself; **stale `>12` months** and no open grant. Read it, do not vendor it |
| [sunbird-ed/sunbirded-portal](https://github.com/sunbird-ed/sunbirded-portal) | 41 | 🟢 **MIT** (`1,072 B`, bytes), 🟡 pushed `2026-02-21`, 🔴 **`334 MB`** | Promoted to [`../verticals/solutions.md`](../verticals/solutions.md) instead — it is a national platform (India DPG), not a component. 🔴 Its size is `595-A`'s problem again, `2.8×` over |

🔵 **`595-A` restated with this pass's measurements.** Repository size is a delivery constraint this
page must carry, because a shallow clone through this session's proxy is the only way in: the
promoted set includes `334 MB` (Sunbird), `232 MB` (Kolibri Studio), `201 MB` (Oak), `148 MB`
(AutoGen) and `102 MB` (Intel suite). 🔴 **Five of eighteen rows exceed `100 MB`** — so "clone it and
look" is not a free operation on this shelf, and a recipe that assumes it will stall in CI.

---

🆕 **`p595` — this page was not re-measured and no row changed.** The pass spent its
legs on the four mandated regions (`13 of 13` tokens already held), the four global legs
(`0` new addresses) and one topic axis (`grading`/`autograder`/`rubric`), which returned
`6` addresses of which `5` were already held and the sixth is unlicensed. 🟢 **Three
grants on the grading axis were byte-read this pass and are recorded here for the recipe on
[`../compose/patterns.md`](../compose/patterns.md)**: `webtech-network/autograder`
**Apache-2.0** (`11,357 B`), `johnswyou/autograder` **MIT** (`1,065 B`),
`scaleapi/researchrubrics` **MIT** (`1,078 B`). 🔴 **No new foundational platform was
found**, and the honest reason is stated rather than padded: the platform tier of this
industry — Moodle, Open edX, Canvas, OpenOlat, Sakai — is mature and does not turn over
weekly, so a weekly leg against it is expected to return nil and did.

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

## 🆕 `p594` — the blank-licence field is settled on the whole base, and one permissive row is recovered from it

🟢 **`591-B` was measured on a sample and is now measured on the population.** All `46` curated
addresses whose GitHub licence field is blank were byte-read this pass, each on **its own default
branch** (`594-B`) across **`13` path/case variants** (`594-C`):

| API licence state | rows | have a grant file | verdict for an instrument |
| --- | --: | --- | --- |
| `license: null` | `14` | 🔴 **`0 of 14`** | 🟢 **may be trusted to block a row** |
| `NOASSERTION` | `32` | 🟢 **`32 of 32`** | 🔴 **must never block; always byte-read** |

🔵 **Perfect separation, no counter-example.** `591-B` reported `10/10` and `0/12`; the population
reproduces it exactly. 🔴 **`Trend 31`'s "about one in two" conflated the two states and is
superseded** — the two fields are not two grades of the same signal, they are opposite
instructions.

**The `32` `NOASSERTION` rows resolve to:** `13` permissive · `6` strong copyleft · `2` weak
copyleft · `2` not-OSI · `2` content-not-code · `7` bespoke or split-scope → review.

### 🟢 Recovered from a blank field this pass

| Repo | API | Real grant, byte-read | Why it was blank |
| --- | --- | --- | --- |
| [thm-mni-ii/feedbacksystem](https://github.com/thm-mni-ii/feedbacksystem) | `NOASSERTION` | 🟢 **Apache-2.0 (text, `10,784 B`, branch `dev`)** | 🆕 A **copyright line is prepended** — `Copyright 2021 Technische Hochschule Mittelhessen` — so the title is not the licence; the grant is declared on line 2. `24★`, EMEA (Germany), automated programming-exercise feedback and grading |
| [frappe/education](https://github.com/frappe/education) | `NOASSERTION` | 🔴 **GPL-3.0 (`19 B`, `develop/license.txt`)** | 🆕 Grant at **lowercase `license.txt`** on a `develop` default branch, and only `19` bytes long — `License: GNU GPL V3`, a declaration with no licence text |
| [portabilis/i-diario](https://github.com/portabilis/i-diario) | `NOASSERTION` | 🔴 **AGPL-3.0 (text, `35,325 B`, branch `1.6`)** | 🆕 Grant written **in Portuguese** — `LICENÇA PÚBLICA GERAL AFFERO GNU` |
| [portabilis/pre-matricula-digital](https://github.com/portabilis/pre-matricula-digital) | `NOASSERTION` | 🔴 **AGPL-3.0 (text, `35,325 B`, branch `2.12`)** | 🆕 Same Portuguese grant, byte-identical |
| [odoo/odoo](https://github.com/odoo/odoo) | `NOASSERTION` | 🟡 **LGPL-3.0 (text, `43,529 B`, branch `20.0`)** | Prose prepend; declared on line 2. 🟢 Agrees with the value this page already published |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | `NOASSERTION` | 🟡 **LGPL-3.0 (text, `8,240 B`, branch `19.0`)** | Prose prepend; confirms `p593` independently |

🔵 **The four Brazilian/German rows above are the whole of `594-D` in practice:** three of them were
unreadable by this base's previous instrument for a reason that has nothing to do with the project
being unlicensed — branch, filename case, or the language the grant is written in.

### 🔴 The `14` genuine blocks — `license: null`, no grant file at `13` paths on the default branch

[A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) ·
[CryptoJones/OSAPHLA](https://github.com/CryptoJones/OSAPHLA) ·
[DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) ·
[OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) ·
[aaryansamanta/ai-ethos](https://github.com/aaryansamanta/ai-ethos) ·
[adlnet/SCORM-to-xAPI-Wrapper](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) ·
[anandpatikat/guru-latihan-dinamis](https://github.com/anandpatikat/guru-latihan-dinamis) ·
[andresmancilla08/Parlo](https://github.com/andresmancilla08/Parlo) ·
[aneelv75/github-trending](https://github.com/aneelv75/github-trending) ·
[bigdata-ustc/Agent4Edu](https://github.com/bigdata-ustc/Agent4Edu) ·
[corleone000000/fluir](https://github.com/corleone000000/fluir) ·
[jccastel12-ctrl/linguaai-coach](https://github.com/jccastel12-ctrl/linguaai-coach) ·
[rodrigoborgesmachado/questoesConcursos](https://github.com/rodrigoborgesmachado/questoesConcursos) ·
[s64965264-code/nexo-ia](https://github.com/s64965264-code/nexo-ia)

🔴 **`BLOCK` — no grant means no permission**, regardless of stars or how useful the artefact looks.
🔵 Three of these are notable as *informed* gaps rather than oversights:
`adlnet/SCORM-to-xAPI-Wrapper` (`99★`) is from **ADL**, the body that authored SCORM and xAPI, and
is still unlicensed; `bigdata-ustc/Agent4Edu` (`100★`) is the education-agent *simulation*
benchmark this base has wanted a licence on since `p568`; and
`anandpatikat/guru-latihan-dinamis` (`115★`, Indonesian exam practice) is the **one address the
mandated legs surfaced this pass** — and it has no grant, so the nil stands either way (`594-G`).


## The platform tier — LMSs and systems of record

| Repo | Licence | Stars | Last push | Region | Shippable? | Role |
|---|---|--:|---|---|---|---|
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 **AGPL-3.0 (text)** | **8,214** | `2026-11-01` | North America | 🔴 network copyleft | The LMS of record. 🔴 **Cite this address** — `openedx/edx-platform` is the pre-rename name and the API rejects it with `422`. |
| [moodle/moodle](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** | **7,569** | `2026-10-30` | EMEA | 🔴 copyleft | The other LMS of record; 7,690 forks. Australia-origin, EMEA-anchored governance. |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0 (text)** | **9,262** | `2026-10-31` | Global | 🔴 lesser copyleft | 🆕 **The virtual-classroom platform of record** — web conferencing purpose-built for teaching (breakouts, whiteboard, polls, recordings). 🟡 LGPL-3.0 is the mildest copyleft on this tier: a studio may **link** proprietary code against it, but modifications to BBB itself carry back. 🔴 **Default branch is `v4.0.x-develop`** — a licence probe on `main` returns `404` (see `587-D`). Re-found 18× in history and never filed. |
| [apache/openmeetings](https://github.com/apache/openmeetings) | 🟡 **Apache-2.0 + a declared third-party block (text)** | **688** | `2026-10-26` | EMEA | 🟡 **yes, with one read** | 🆕 **The PERMISSIVE virtual-classroom platform — the tier this base recorded as copyleft-only.** Video conferencing, whiteboard, polls, recording and collaborative docs under ASF governance. 🔴 Its `LICENSE` carries an in-payload dependency block (MIT, BSD, EPL, EDL, some `NOASSERTION`, and **Oracle Free Use Terms** — not an open-source grant) exactly as `P1024` predicts; the **ASF's own code is Apache-2.0**, the bundle is the question. 🔵 API said `NOASSERTION`; default branch `master`; carried unfiled since `p525`. |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** | **3,361** | `2026-10-30` | APAC | 🔴 network copyleft | Frappe's LMS. India-origin, 1,566 forks. |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 **AGPL-3.0** | **2,440** | `2026-11-01` | EMEA | 🔴 network copyleft | Next-gen self-hostable learning platform; very active. |
| [classroomio/classroomio](https://github.com/classroomio/classroomio) | 🔴 **AGPL-3.0** | **1,736** | `2026-11-01` | Global | 🔴 network copyleft | Customer-training-oriented platform. |
| [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn) | 🔴 **Split grant — one part is not open source (text)** | **527** | `2026-11-01` | North America | 🔴 **no** | 🆕 **The assessment engine of record for problem-driven courses** (UIUC origin, pushed today). 🔴 Its licence file divides the repository four ways: the **Community Edition is AGPL-3.0**; **all client-side JavaScript is AGPL-3.0** *however it is served or compiled*; `apps/prairielearn/src/ee/` is the **proprietary Enterprise Edition** under its own licence; and only the portions copyright UIUC and outside contributors are **MIT**. 🔵 **Same shape as `orbit`** — permissive at the edges, copyleft-or-closed where the product is. A studio may read it; it may not ship it. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0 (text)** | **1,240** | `2026-10-30` | North America | 🟢 **yes** | 🟢 **The one platform of record a studio may lawfully fork, modify and ship.** ECL-2.0 is Apache-2.0 with the patent grant narrowed for education — its own licence text says so. Higher-ed consortium governance; 1,020 forks. |
| [codelitdev/courselit](https://github.com/codelitdev/courselit) | 🔴 **AGPL-3.0** | **1,292** | `2026-11-01` | Global | 🔴 network copyleft | Course + digital-product platform with a storefront. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** | **1,131** | `2026-10-29` | Global | 🔴 network copyleft | The Docker-based Open edX distribution. **The practical way to stand Open edX up** — the operational entry point, not a fork target. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT (text)** | **1,163** | `2026-11-01` | Global | 🟢 **yes** | 🟢 **The offline-first learning platform for low-connectivity deployments** — 1,016 forks, built for exactly the infrastructure conditions that defeat cloud LMSs. Learning Equality. **The highest-leverage permissive platform on this page for LATAM, Africa and rural APAC.** |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0** | **1,019** | `2026-11-01` | EMEA | 🔴 copyleft | LMS focused on ease of use and accessibility; strong LATAM and francophone deployment base. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0 (text)** | **903** | `2026-10-29` | APAC | 🟡 weak copyleft | 🆕 **The education ERP tier — admissions, fees, attendance, library, hostel, exams on one database.** Built as Odoo modules; India-origin. 🔴 **Cite this address**: `OpenEduCat/OpenEduCat` returns `422` and the live repo is lowercase with an `_erp` suffix, on default branch **`19.0`** (not `main`/`master`). 🟡 **LGPL-3.0 is weak copyleft** — a *separate* AI module that calls its API keeps its own licence; edits to its own files must be published. API reported `NOASSERTION`. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** | **649** | `2026-10-28` | Global | 🔴 copyleft | 🆕 Student Information System (scheduling, grades, attendance, billing). Strong francophone and LATAM deployment base. 🔵 Default branch is **`mobile`**. Relevant to gap `585-F`: the SIS tier is real but copyleft. |
| [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | 🟡 **MIT on the code, split grant (text, `1,683 B`) — refined `p594`** | **981** | 🔴 `2025-12-09` | APAC | 🟡 licence yes, **stale** | 🆕 LMS for asynchronous online schools with reviewed submissions. **Permissive, and the API hid it** (`NOASSERTION`). 🟡 **`p594` (`591-G` audit): the grant is NOT flat MIT.** Its `LICENSE` reads *"Portions of this software are licensed as follows"* — everything under `docs/` is **CC-BY-SA-4.0**, client-side JavaScript is MIT, third-party components keep their own licences, and only *"content outside of the above"* is MIT. 🟢 **The code is still usable permissively**; 🔴 **the documentation is share-alike and must not be lifted into client deliverables.** Caught by `591-G`'s byte-size filter: `1,683 B` against a canonical MIT grant of `~1,050–1,100 B`. 🔴 ~11 months without a push — adopt with eyes open. |
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

## 🆕 The general ERP/CRM systems-of-record tier — added `p591`

🔵 **Why this tier belongs on an education foundations page.** An institution's systems of
record are admissions, fees, attendance, HR and alumni CRM — and
[`openeducat_erp`](https://github.com/openeducat/openeducat_erp) (LGPL-3.0) and
[`frappe/education`](https://github.com/frappe/education) (GPL-3.0) are the only
*education-specific* options, both copyleft. 🟢 **The permissive tier exists, it is large,
and it is general-purpose** — so the real decision is *"customise a general ERP into
education, or attach to a copyleft education ERP from the outside?"* 🟢 Every grant below
byte-read `2026-11-01`, **title-anchored** per `591-A`.

| Repo | Licence | Stars | Last push | Region | Shippable? | Role |
|---|---|--:|---|---|---|---|
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | 🟢 **MIT (text, 1,078 B)** | **24,087** | `2026-11-01` | APAC | 🟢 **yes** | 🆕 **The largest permissive CRM in this base by an order of magnitude.** Laravel/PHP. The admissions-and-enquiry pipeline an institution actually runs on. 🔵 Default branch `master`. |
| [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | 🔴 **GPL-3.0 (text, 35,151 B)** | **7,814** | `2026-11-01` | EMEA | 🔴 copyleft | 🆕 ERP/CRM with very broad module coverage; strong francophone and LATAM base. 🔵 **Grant is at `COPYING`, not `LICENSE`** — a `LICENSE`-only probe files a false absence. |
| [cortezaproject/corteza](https://github.com/cortezaproject/corteza) | 🟢 **Apache-2.0 (text, 11,358 B)** | **2,183** | `2026-10-20` | EMEA | 🟢 **yes** | 🆕 **Low-code** CRM and application platform in Go. 🔵 The build-your-own-module option: closest permissive analogue to what `openeducat` does on top of Odoo. |
| [marmelab/atomic-crm](https://github.com/marmelab/atomic-crm) | 🟢 **MIT (text, 1,105 B, `LICENSE.md`)** | **1,420** | `2026-10-30` | EMEA | 🟢 **yes** | 🆕 React/TypeScript CRM on Supabase. **The fastest permissive starting point** when the deliverable is a custom student-lifecycle CRM rather than a configured product. France (marmelab). |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0 (text, 11,906 B)** | **1,148** | `2026-11-01` | Global | 🟢 **yes** | 🆕 Java ERP/CRM suite under ASF governance — accounting, manufacturing, HR, CRM. 🔵 The most conservative permissive choice: foundation-governed, decade-plus top-level project. Default branch `master`. |
| [idurar/idurar-erp-crm](https://github.com/idurar/idurar-erp-crm) | 🔴 **AGPL-3.0 (text, 34,230 B)** | **8,931** | 🟡 `2026-08-14` | Global | 🔴 **no — network copyleft** | 🔴 **The mandated vertical leg asserted this one is *"fully open-source under the MIT license"*. It is AGPL-3.0** — byte-read, and the API agrees. See `591-E`. 🟡 ~2.7 months since last push. |
| [idempiere/idempiere](https://github.com/idempiere/idempiere) | 🔴 **GPL-2.0 (text, 15,057 B, `LICENSE.md`)** | **675** | `2026-10-30` | Global | 🔴 copyleft | 🆕 Java ERP, community fork lineage. 🔵 **API said `NOASSERTION` and the licence file's first line is `<center>`** — it is HTML-wrapped, which is both why the parser blanked (`591-B`) and why a title-anchored read must strip tags before matching. |

🟢 **The build-vs-buy answer to give an institutional client**, stated plainly: if the
requirement is *configured education ERP* (admissions, fees, attendance, exams on one
database out of the box), the only real options are **copyleft** — `openeducat_erp`
(LGPL-3.0, so a *separate* AI module calling its API keeps its own licence) or
`frappe/education` (GPL-3.0). 🟢 If the requirement is *a custom student-lifecycle system
the studio owns*, start from **`krayin`**, **`corteza`**, **`atomic-crm`** or
**`ofbiz-framework`** and build the education domain on top — all four are permissive and
all four were pushed within the last two weeks. 🔵 **Do not scope `idurar` as permissive.**

---

## 🆕 Component additions — `p591`

| Repo | Licence | Stars | Last push | Region | Role |
|---|---|--:|---|---|---|
| [shand001/geometry-dsl](https://github.com/shand001/geometry-dsl) | 🟢 **MIT (text, 1,082 B)** | **6** | `2026-09-15` | Global | 🆕 **Deterministic** geometry-diagram DSL for agents: text in, exact SVG/PNG figures out. Zero-dependency compiler **plus** a Claude/Codex agent skill. 🔵 **The missing piece in every STEM courseware pipeline on these shelves** — an LLM asked to draw a labelled triangle produces a plausible-looking wrong one; this makes the figure a compile step instead. Small, and it does one thing correctly. |
| [major7apps/pensyve](https://github.com/major7apps/pensyve) | 🟢 **Apache-2.0 (text, 9,488 B)** | **97** | `2026-10-29` | Global | 🆕 Universal **memory runtime** for AI agents, in Rust. 🔵 Not education software — it is the cross-session memory layer that `universal-examprep-skill` and `empty` implement privately, available as a dependency. API said `NOASSERTION`. 🟡 `24` open issues; young. |

🔵 **Why these two and not the other `43` addresses this pass filed:** a *foundation* row has
to be something other rows stand on. These are. The rest are tutors and curricula, and they
are on [`../agents/top.md`](../agents/top.md).

---

## 🆕 `p596` — `5` rows promoted off the trending backlog, not discovered

🔴 **Why these rows arrive now, when the search legs returned nothing — and the honest version
of it.** `596-C` measured that **`2,015` of `2,243` ever-shelved addresses (`89.8 %`) were
dropped** across `15` wholesale rewrites recorded under `archive/`, while the append-only
trending logs lost nothing. 🔴 **Because the "already held?" gate greps the logs, a row dropped
from this page still answers *"held"* forever and is never re-shelved.** 🟢 **All five rows below
were on a shelf page in an archived snapshot and were dropped** — `hyperbook` in three
snapshots (`p351`, `p355`, `p383`), `h5p-offline-player` in two, `PySyft` at
`2026-10-06-pre-reset`, `ltijs-sequelize` and `earthmover_edfi_bundles` at
`2026-10-17-pre-rewrite`. 🔵 **This is recovery, not discovery.** Every one was re-verified first-hand this pass:
stars and `default_branch` from `gh api -X GET search/repositories`, and **every grant
byte-read** on `raw.githubusercontent.com` at the branch the API reported.

🔵 **`3 of 5` default to something other than `main`** — `dev`, `master`, `master`. A probe
hardcoding `main` would have filed all three as unlicensed, which is `594-B` in practice.

| Repo | Licence | Stars | Last push | Region | Role |
|---|---|--:|---|---|---|
| [OpenMined/PySyft](https://github.com/OpenMined/PySyft) | 🟡 **Apache-2.0 (text, `11,941 B`, branch `dev`) + PSF carve-out** | **10,049** | `2026-10-30` | Global | 🆕 **Remote execution over data the analyst never sees** — the privacy layer for cross-institution learning analytics, where the obstacle is never the model but the fact that student records cannot leave the institution. 🔴 **Not flat Apache-2.0:** the grant is `584 B` over canonical and `591-G`'s byte filter flags it. Three-stage read — title `Apache License 2.0`, body canonical, then an **appended carve-out placing `7` named test files under the PSF licence**, copied from CPython. 🟢 Shippable: the carve-out never leaves `packages/syft/tests/`. |
| [openpatch/hyperbook](https://github.com/openpatch/hyperbook) | 🟢 **MIT (text, `1,069 B`)** | **75** | 🟢 `2026-11-01` | EMEA | 🆕 **Interactive workbooks as static sites** — a CLI plus a markdown engine with `30+` custom directives, building courseware that needs no LMS and no server to deliver. 🔵 The authoring half of a courseware factory whose delivery half this base already holds; Germany (OpenPatch). Pushed the day it was measured. |
| [edanalytics/earthmover_edfi_bundles](https://github.com/edanalytics/earthmover_edfi_bundles) | 🟢 **Apache-2.0 (text, `11,357 B`)** | **14** | `2026-10-30` | North America | 🆕 **Pre-built mappings from assessment-vendor formats into the Ed-Fi API** — CSV seeds, JSON templates and YAML transforms, with two packages that auto-detect the right student-ID configuration to maximise matching against an Ed-Fi roster. 🔵 **It exists because most assessment vendors ship no native Ed-Fi integration**, which is precisely the unglamorous work a US K-12 district engagement is actually billed for. |
| [missing-elements/h5p-offline-player](https://github.com/missing-elements/h5p-offline-player) | 🟡 **MIT (text, `1,073 B`) — split artefact** | **6** | 🟢 `2026-11-01` | Global | 🆕 **Plays `.h5p` packages with no H5P server, no Moodle and no backend** — one web component on static hosting, plus a PWA that runs with no network at all. Stable since `1.0` (`2026-10-18`); library pack checked weekly against the H5P hub. 🔴 **Two licences by design, README verbatim:** *"The player is MIT; the H5P runtime it loads is GPL-3.0 and published separately."* 🟢 The player may be forked and shipped closed; 🔴 the runtime may not. 🔵 The offline PWA is the strongest low-connectivity delivery route this page carries. |
| [Cvmcosta/ltijs-sequelize](https://github.com/Cvmcosta/ltijs-sequelize) | 🟢 **Apache-2.0 (text, `11,357 B`, branch `master`)** | **5** | `2026-09-29` | Global | 🆕 **SQL persistence for `ltijs`**, which this page already carries at `373★` and which is **LTI Advantage Complete Certified by 1EdTech**. 🔵 Low stars because it is a database adapter, not a product: it is what lets the certified LTI path run on Postgres or MySQL instead of the default Mongo, which is the difference between a demo and something a university's DBA will accept. |

### 🔴 Not promoted, and the reasons are on the record

- 🔴 [`GoogleCloudPlatform/aira`](https://github.com/GoogleCloudPlatform/aira) — *AI Reading
  Assessor*, Apache-2.0 (`11,357 B`, byte-read), `24★`. 🟢 Passes every screen this page
  normally runs: permissive, real organisation, education-core, live. 🔴 **BLOCKED on its
  own README**: *"demo experiment"*, *"proof-of-concept only"*, *"not an officially supported
  Google product"*, *"do not use any personal or sensitive data"* and *"should not be used by
  children under 13 or to process data from children under 13"* — which excludes K-12, the
  population a reading assessor exists for. 🔵 **`596-D`: a self-declared scope can
  disqualify a row that licence, liveness and provenance all clear.** Read the README's
  status and audience claims before promoting.
- 🟡 [`3iPunt/wordpress-lti-1-3`](https://github.com/3iPunt/wordpress-lti-1-3) — Apache-2.0,
  `6★`, last push `2023-07-11`. Parked, not blocked: **three years and three months stale.**
- 🔵 `adap/flower` and `digitalcredentials/did-io` — both returned `422 Validation Failed`
  on the search channel. 🟢 **Recorded as UNRESOLVED, not as findings.** The channel failing
  loudly is the control working.

---

## The component and spec tier — permissive, and where the real leverage is

| Repo | Licence | Stars | Last push | Region | Role |
|---|---|--:|---|---|---|
| [dream-num/univer](https://github.com/dream-num/univer) | 🟢 **Apache-2.0** | **22,839** | `2026-10-31` | APAC | Sheets/docs/slides/canvas SDK — the document substrate for courseware and worksheets with no Office dependency. 1,916 forks. 🔵 Not education-specific; it is infrastructure this industry needs. |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL-1.0 (text)** — a *database* licence, new to this base | **7,491** | `2026-10-30` | Global | 🆕 **An open skills/occupation taxonomy** — the missing spine for competency mapping, course-to-job alignment and reskilling paths, which is what a corporate-learning client actually buys. 🔴 **ODbL-1.0 is not in this base's software-licence vocabulary and must not be graded as one:** it is share-alike *on derived databases*, with a produced-work clause. A studio may build a product **on** it; publishing an enriched taxonomy means publishing the enrichment. 🔵 **Counsel question, not an engineering one.** |
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
| [Halleck45/OpenPronounce](https://github.com/Halleck45/OpenPronounce) | 🟢 **MIT** | **176** | `2026-08-15` | EMEA | 🆕 Phoneme-level English pronunciation assessment (Wav2Vec2 + DTW), self-hosted. The speaking-assessment component for language engagements. |
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

## 🆕 The enablement tier — the curricula a studio hands a client's own engineers

🔵 **Not a platform tier and not an agent tier.** These are the teaching artefacts for a
reskilling or enablement engagement, and they are listed here because the brief *"train our
people to build this"* arrives in the same conversation as *"and build it for us"*. Full
rows, licence reasoning and the taxonomy argument are on
[`../agents/top.md`](../agents/top.md) under *the enablement tier*; this is the index.

| Repo | Licence | Stars | Last push | Region | Shippable? | Role |
|---|---|--:|---|---|---|---|
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 🟢 **MIT (text)** | **122,716** | `2026-11-01` | Global | 🟢 **yes** | 🆕 **The largest education-adjacent repo on GitHub.** 21 lessons on building with generative AI. The default day-one hand-off. |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 🟡 **Apache-2.0 — code only (text)** | **107,633** | `2026-10-30` | Global | 🟡 **code yes, book no** | 🆕 GPT-class model built one stage at a time. 🔴 **The licence text excludes the books and images from "Source"** — the deepest curriculum here and the one with a carve-out. |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **MIT (text)** | **78,576** | `2026-10-31` | Global | 🟢 **yes** | Agents from first principles, 18 lessons. Shelved `p587`; re-measured `p588`. |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 🟢 **MIT (text)** | **76,170** | `2026-10-29` | Global | 🟢 **yes** | The build-and-ship half. Shelved `p587`; re-measured `p588`. |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🟢 **Apache-2.0 (text)** | **64,724** | `2026-10-27` | APAC | 🟢 **yes** | 🆕 A ~64M-parameter model trained from scratch in ~2 hours. 🔵 Chinese-language project; branch `master`. |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | 🟢 **MIT (text)** | **59,308** | 🟡 `2026-09-07` | Global | 🟢 **yes** | 🆕 The whole ChatGPT-style stack, trainable end-to-end. 🟡 ~2 months — pin it. |

🟢 **All six are permissive and five are unreserved**, so an enablement engagement has **no
licence blocker at all** — which is not true of any platform tier on this page.

---

## 🆕 The SCORM emit-side tier — measured `p589`, and most of it is dead

🔵 **Why this tier is on this page at all.** `Trend 41` splits specifications into two
roles: a **conformance target** you must *speak* (LTI 1.3, xAPI → buy a library) and an
**export target** you must *emit* (SCORM → build the generator). Every engagement that
delivers courseware into a client's existing LMS is an **emit** job, so this is the tier a
studio reaches for — and 🔴 **it is almost entirely abandoned.**

Whole axis measured first-hand `2026-11-01` via `gh api search/repositories -f
q='topic:scorm'`, **`235` repositories, every page walked**. Licence distribution, which is
the first thing to know about it:

| licence (API) | repos | share |
|---|--:|--:|
| 🔴 **none at all** | **`133`** | 🔴 **`56.6 %`** |
| 🟢 MIT | `65` | `27.7 %` |
| 🟢 Apache-2.0 | `12` | `5.1 %` |
| 🔴 GPL-3.0 | `12` | `5.1 %` |
| 🟡 `NOASSERTION` | `8` | `3.4 %` |
| 🟡 CC0-1.0 | `2` | `0.9 %` |
| 🟢 BSD-3-Clause / 🔴 LGPL-2.1 / 🔴 EUPL-1.2 | `1` each | `1.3 %` |

🟢 **`80 of 235` (`34.0 %`) are permissive** — far better than the platform tier above, where
permissive is the exception. 🔴 **But liveness, not licence, is what disqualifies this tier.**

| Repo | Licence | Stars | Last push | Region | Shippable? | Role |
|---|---|--:|---|---|---|---|
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 **MIT (text)** | **362** | `2026-10-28` | Global | 🟢 **yes** | 🟢 **A live, maintained, permissive SCORM runtime (one of six — corrected `p590`) — the single safe dependency on this entire axis.** Modern JS runtime implementing SCORM 1.2 and 2004 API signatures. `1,072`-byte verbatim MIT, no carve-out. 🔵 Already shelved before `p589`; re-confirmed here as the tier's anchor. |
| [sr258/scorm-h5p-wrapper](https://github.com/sr258/scorm-h5p-wrapper) | 🟢 **MIT (text)** | **58** | `2026-10-29` | EMEA | 🟢 **yes** | 🆕 **Another live permissive row.** NodeJS service that packs **H5P** interactive content into SCORM objects — i.e. the bridge from an open authoring format into the LMS container. `1,073`-byte verbatim MIT. 🔵 Small, single-purpose, and exactly the shape a pipeline step should be. Unshelved until now despite 3 history re-finds. |
| [LiaScript/LiaScript-Exporter](https://github.com/LiaScript/LiaScript-Exporter) | 🟢 **BSD-3-Clause** | **29** | `2026-10-30` | EMEA | 🟢 **yes** | 🆕 **Exports one source into SCORM 1.2, SCORM 2004, IMS, xAPI, H5P, PDF, ePub and Web** — README read first-hand `p590`. 🔴 **Absent from `p589`'s table although this base already held it**, and it is the row that refutes the *"exactly two alive"* claim. 🔵 Closest thing on this axis to a finished generator.
| [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 Apache-2.0 | **216** | 🆕 `2026-10-28` (measured `p590`; `p589` left this cell blank) | EMEA | 🟢 yes | Browser-based e-assessment with a real maths engine; SCORM-packageable output. 🔵 Already shelved; listed here for the tier's shape. |
| [dhodges47/SCORM-LearningManagementSystem](https://github.com/dhodges47/SCORM-LearningManagementSystem) | 🟢 MIT | **184** | 🟡 `2026-01-24` | Global | 🟡 reference only | 🆕 Open-source SCORM LMS **demo**. 🟡 ~9 months idle, and its own description calls it a demo — a reading of how SCORM hosting works, not a platform to adopt. |
| [cybercussion/SCOBot](https://github.com/cybercussion/SCOBot) | 🔴 **CC BY-SA 4.0 (text) — reciprocal** | **165** | `2026-10-29` | Global | 🔴 **no** | 🆕 **The trap on this axis.** Live, well-regarded SCORM API for content with QUnit tests — and the `837`-byte `LICENSE` is **Creative Commons Attribution-ShareAlike**, not a software licence. API said `NOASSERTION`. ShareAlike propagates; CC grants no patent. See `589-F` and the block table on [`../agents/top.md`](../agents/top.md). |
| [adaptlearning/adapt_framework](https://github.com/adaptlearning/adapt_framework) | 🔴 **GPL-3.0** | **632** | 🆕 `2026-10-26` (measured `p590`) | EMEA | 🔴 copyleft | 🆕 The most-starred **authoring** toolkit on the axis — responsive, accessible, multilanguage HTML5 courseware with SCORM output. 🔴 Copyleft, so it is a reference architecture rather than a dependency. Unshelved despite 10 history re-finds. |
| [S4-NetQuest/react-scorm-provider](https://github.com/S4-NetQuest/react-scorm-provider) | 🟢 MIT | **67** | 🔴 `2023-01-06` | Global | 🔴 **no — dead** | 🆕 React components wrapping the SCORM API. 🔴 **~3.8 years without a push.** Would be the obvious choice for a React courseware front end; it is not maintained. Default branch `master`. |
| [gamestdio/scorm](https://github.com/gamestdio/scorm) | 🟢 MIT | **38** | 🔴 `2019-02-14` | Global | 🔴 **no — dead** | 🆕 SCORM 1.2 / 2004 wrapper for JavaScript/TypeScript. 🔴 **~7.7 years without a push.** |
| [raccoongang/edx_xblock_scorm](https://github.com/raccoongang/edx_xblock_scorm) | 🟢 Apache-2.0 | **32** | 🔴 **ARCHIVED** | EMEA | 🔴 **no — archived** | 🆕 XBlock to display SCORM content inside Open edX. 🔴 `archived: true`, last push `2023-05-26`. 🔵 The seam between the two LMSs of record on this page, and it is read-only. |
| [adlnet/SCORM-to-xAPI-Wrapper](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | 🔴 **BLOCK — no grant + ARCHIVED** | **99** | 🔴 `2017-10-02` | North America | 🔴 **no** | 🆕 🔴 **Published by ADL — the body that authored SCORM — and it is unlicensed and archived.** 🔵 The strongest single datum behind `Trend 41`: the specification's own authors abandoned their own tooling, which is why generators grew on top of this layer instead of libraries. |

🔴 **WITHDRAWN `p590` — "buy exactly one dependency … and depend on nothing else on this
axis" was wrong, and the row that refutes it is `66` lines above it in THIS FILE.** The
paragraph read that `scorm-again` is *"the one live, maintained, permissive SCORM
runtime"* and that nine of ten rows here are unusable. 🔴 **`numbas/Numbas` is Apache-2.0,
`216★`, pushed `2026-10-28`, ships a `23,811`-byte `runtime/scripts/scorm-storage.js`, and
this page already shelves it at line `78` as *"the permissive assessment anchor to build
on"*** — while `p589`'s own row for it in the table above left `Last push` as `—`. 🔵 **The
unmeasured cell is the whole mechanism: the claim was safe only because the refuting cell
was blank.** This is `584-B`'s failure mode (*shelf refutes claim, nothing checks that
direction*) recurring **one pass after `584-B` was registered**, and `584-B`'s own
prescription — `grep` the pages for the claim's subject terms before writing a universal —
would have caught it for free.

🟢 **The corrected build-vs-buy answer for an emit engagement.** There are **at least six**
live permissive SCORM emitters, not two:

| Repo | Licence | Stars | Last push | Emit role |
|---|---|--:|---|---|
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 MIT | **362** | `2026-10-28` | The runtime — content↔LMS API. **Still the first dependency to add.** |
| [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 Apache-2.0 | **216** | `2026-10-28` | 🆕 Assessment engine with a SCORM runtime of its own. Newcastle University. |
| [sr258/scorm-h5p-wrapper](https://github.com/sr258/scorm-h5p-wrapper) | 🟢 MIT | **58** | `2026-10-29` | Packs H5P into SCORM objects. |
| [LiaScript/LiaScript-Exporter](https://github.com/LiaScript/LiaScript-Exporter) | 🟢 **BSD-3-Clause** | **29** | `2026-10-30` | 🆕 **Exports to SCORM 1.2, SCORM 2004, IMS, xAPI, H5P and Web from one source** — README read first-hand. 🔵 The closest thing on this axis to a finished generator, and `p589` missed it although this base already held it. |
| [kemalyy/edumints-scorm-mcp](https://github.com/kemalyy/edumints-scorm-mcp) | 🟢 MIT | **9** | `2026-10-14` | 🆕 MCP server that assembles SCORM-compliant courses — agent-native emit. |
| [giacomomaria81/scorm-mcp-server](https://github.com/giacomomaria81/scorm-mcp-server) | 🟢 MIT | **6** | `2026-09-03` | 🆕 HTML / design bundles → SCORM 2004 + 1.2 packages, as an MCP tool. |

🔵 **So the answer a client should be given is:** `scorm-again` for the runtime,
**`LiaScript-Exporter` if the source is Markdown-shaped courseware** (it removes most of
the generator), `Numbas` if the deliverable is assessment, `scorm-h5p-wrapper` if the source
is H5P — and the two MCP servers if the pipeline is agent-driven. 🔴 **Build the generator
only after those five are ruled out**, which is a materially different instruction from the
one this page published yesterday.

🟢 **`589-E` is CLOSED BY REFUTATION** — see the `p590` tiers below. 🔴 The licence
distribution table above also does not reproduce: `p589` published `133 / 235` unlicensed
(`56.6 %`); re-walked the **same day** the axis gives `141 / 235` (`60.0 %`) on an identical
denominator of `235`, and permissive `78`, not `80`. 🔵 **Same-day, same channel, different
answer — so a licence *share* on this axis is good to about `± 4 pp` and no finer**, which
is recorded here because `589-F` built a prescription on the `56.6 %` figure.

---

## 🆕 The xAPI and QTI emit-side tiers — measured `p590`, and `589-E` is ANSWERED: the decay is NOT general

🔵 **What `589-E` asked and what the answer costs this page.** `p589` found the SCORM
emit-side dead and asked whether the same holds on `topic:xapi` and `topic:qti` **before**
`Trend 41` generalised. Both axes were walked to exhaustion `2026-11-01` against a
[prediction registered before the measurement](../evidence/prereg-589E-spec-tooling-rot.2026-11-01-p590.md).
🔴 **H1 — "spec tooling rots" — is REFUTED on both axes.** The pre-registered decision rule
said `>= 5` live permissive emitters on an axis refutes it; xAPI has `6` and QTI has `8`.

| axis | repos | permissive | 🔴 no licence at all | live permissive, non-archived | distinct owners among them |
|---|--:|--:|--:|--:|--:|
| `topic:scorm` | `235` | `78` (`33.2 %`) | `141` (🔴 `60.0 %`) | `42` | 🟢 **`39`** |
| `topic:xapi` | `280` | `125` (`44.6 %`) | `115` (🔴 `41.1 %`) | `35` | 🟢 **`27`** |
| `topic:qti` | `52` | `23` (`44.2 %`) | `20` (🔴 `38.5 %`) | `14` | 🔴 **`7`** |

🔴 **The real risk on QTI is not decay, it is CONCENTRATION — and only the owner column
shows it.** `8 of QTI's 14` live permissive repositories belong to **one owner**
(`metyatech`), all pushed inside a six-day window in September `2026`, none above `2★`.
🔵 **A liveness count alone would have called QTI healthy.** It is one publisher: if that
publisher stops, the axis stops. SCORM (`39` owners) and xAPI (`27` owners) are genuinely
diffuse. 🟢 **This is the column that should have been on `p589`'s SCORM table and was not.**

### 🟢 The xAPI emit-side tier — buy, do not build

🔵 Unlike SCORM, xAPI is a **conformance target you speak**, and the client libraries are
alive, permissive and plural. Every grant below was **byte-read** from the repository's own
`LICENSE` this pass; the API's field agreed on `10 of 10`.

| Repo | Licence | Stars | Last push | Region | Shippable? | Role |
|---|---|--:|---|---|---|---|
| [LearningLocker/xapi-service](https://github.com/LearningLocker/xapi-service) | 🟢 **MIT (text, `license`, 1,070 B)** | **42** | `2026-10-26` | EMEA | 🟢 **yes** | 🆕 Standalone xAPI service — the statement endpoint itself. 🔵 Stands in for an LRS when the client will not host Learning Locker whole. |
| [BerryCloud/xapi-java](https://github.com/BerryCloud/xapi-java) | 🟢 **Apache-2.0 (text, 11,350 B)** | **20** | `2026-10-30` | EMEA | 🟢 **yes** | 🆕 **The Java xAPI model, client and tools.** 🟢 The one permissive route for a JVM client estate, which is most university back-offices. |
| [Didask/scol-r](https://github.com/Didask/scol-r) | 🟢 **MIT (text, 1,063 B)** | **15** | `2026-10-27` | EMEA | 🟢 **yes** | 🆕 Shareable Cross-Origin Learning Resources — a SCORM successor format from a French vendor. 🔵 Emit-side, and the only permissive *alternative* to a SCORM package on these shelves. |
| [LearningLocker/xapi-validation](https://github.com/LearningLocker/xapi-validation) | 🟢 **MIT (text, `license`, 1,070 B)** | **12** | `2026-10-26` | EMEA | 🟢 **yes** | 🆕 Validates xAPI statements. 🔵 The cheapest way to stop malformed statements at the studio's own boundary instead of the client's LRS. |
| [ijeffro/laralocker](https://github.com/ijeffro/laralocker) | 🟢 **MIT (text, 1,072 B)** | **9** | `2026-10-03` | Global | 🟢 **yes** | 🆕 Laravel package that emits to Learning Locker. 🔵 Matches the PHP estate that Moodle engagements already run. |
| [yetanalytics/project-pan](https://github.com/yetanalytics/project-pan) | 🟢 **Apache-2.0 (text, 11,356 B)** | **5** | `2026-10-16` | North America | 🟢 **yes** | 🆕 xAPI **Profile** validation library. 🔵 Pairs with `project-persephone` (statement-vs-profile); this one validates the profile itself. |
| [jblough/TinCanDart](https://github.com/jblough/TinCanDart) | 🟢 **Apache-2.0 (text, 11,358 B)** | **5** | `2026-08-06` | Global | 🟢 **yes** | 🆕 xAPI wrapper for **Dart** — i.e. the Flutter path. 🔵 The only permissive mobile-native emitter on these shelves. |

### 🟡 Adjacent permissive rows the same sweep resolved

| Repo | Licence | Stars | Last push | Region | Shippable? | Role |
|---|---|--:|---|---|---|---|
| [erseco/python-moodle](https://github.com/erseco/python-moodle) | 🟢 **MIT (text, 1,071 B)** | **10** | `2026-10-22` | EMEA | 🟢 **yes** | 🆕 Pythonic CLI and library driving a Moodle instance over web sessions. 🔵 The automation handle for the AGPL LMS of record **without forking it** — exactly `573-B`'s attach-over-API rule. |
| [get-bridge/scorm_engine](https://github.com/get-bridge/scorm_engine) | 🟢 **MIT (text, 1,084 B)** | **5** | `2026-09-03` | North America | 🟡 **client only** | 🆕 Ruby client for **Rustici's commercial** SCORM Engine. 🔵 Permissive client, 🔴 proprietary server — shippable as glue, never as the engine. |
| [dr-rompecabezas/wagtail-lms](https://github.com/dr-rompecabezas/wagtail-lms) | 🟢 **MIT (text, 1,072 B)** | **5** | `2026-10-26` | Global | 🟡 **small scale** | 🆕 LMS extension for Wagtail CMS. 🔵 Useful when the client already runs Wagtail; not a platform in its own right. |
| [MathWorks-Teaching-Resources/Computational-Fluid-Dynamics](https://github.com/MathWorks-Teaching-Resources/Computational-Fluid-Dynamics) | 🟢 **BSD-3-Clause (text, 1,527 B)** | **210** | `2025-04-03` | Global | 🟢 **content yes, runtime no** | 🆕 Head of an **`81`-repo** BSD-3-Clause undergraduate STEM curriculum estate (`600-D`). 🟡 MATLAB/Simulink runtime is commercial, so the modules are **course content a studio may modify and rebrand**, not an open stack. 🔴 `59 of 81` siblings default to branch `release` and are invisible to a `main`/`master` probe. |
| [reuseman/flashcards-obsidian](https://github.com/reuseman/flashcards-obsidian) | 🟢 **MIT (text, 1,069 B)** | **1,113** | `2026-10-31` | Global | 🟢 **yes** | 🆕 Markdown notes → Anki cards. The retention layer this base has cited (`FSRS` in `318` files) without ever holding an implementation. |
| [shaankhosla/repeater](https://github.com/shaankhosla/repeater) | 🟢 **Apache-2.0 (text, 11,357 B)** | **442** | `2026-09-28` | Global | 🟢 **yes** | 🆕 Terminal-native spaced repetition — embeds in a CLI tutor with no UI to maintain. |
| [lakesare/memcode](https://github.com/lakesare/memcode)  | 🟢 **MIT (text, 1,080 B)** | **408** | `2026-10-23` | Global | 🟢 **yes** | 🆕 Web SRS, live. 🔴 Default branch `master` — a `600-E` row. |

🔵 **`587-D` extended by this pass: it is not only the BRANCH that is unguessable — it is the
FILENAME CASE.** `LearningLocker/xapi-service` and `xapi-validation` both carry their grant
at lowercase **`license`**; a probe for `LICENSE` alone returns `404` on both, and `4 of 10`
rows here default to `master`, not `main`.

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
