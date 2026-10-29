---
industry: education
region: Global
updated: 2026-10-29
---

## 🆕 `p516` — `2026-10-29` — **🔴 THIS SHELF HELD THE ROW THAT REFUTES THE BASE'S LATAM SUPPLY NIL — line 1010, 🇧🇷 `i-educar`, GPL-2.0, flagged live — while `intel/market.md` published "0 LATAM-originated open-source education repositories at any star level" for an eighth pass. 🟢 The row is re-verified from bytes and now carries its star figure (722), its real default branch (`2.12`), and its sibling `i-diario` (AGPL-3.0, default branch `1.6`).**

### 🟢 The Brazilian municipal stack — a real, deployed, customisable LMS/SIS line

🔵 **Why it belongs on this shelf next to Odoo, Moodle and OpenMRS:** it is a *government-adopted*
platform with a long deployment history, which is exactly the profile this shelf exists to hold —
a real system a studio can customise with AI on top rather than a research artifact.

| Platform | Origin & standing | Licence (read from bytes) | ★ | HEAD @ default branch | Customisation surface |
|---|---|---|---|---|---|
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🇧🇷 Built by the **Itajaí-SC municipal government**; published on Brazil's **Portal do Software Público Federal** in **2008**; maintained by Portabilis. Self-described *"o maior software livre de educação do Brasil"* | **GPL-2.0** — root `LICENSE`; sidebar *"GPL-2.0 license"* | **722** (551 forks) | `435649b0474f` @ **`2.12`** | Full municipal **SIS**: enrolment, student/staff records, grades, transfers, municipal census reporting. PHP/Laravel |
| [`portabilis/i-diario`](https://github.com/portabilis/i-diario) | 🇧🇷 Portabilis; the teacher-facing companion to i-educar | 🔴 **AGPL-3.0** — `LICENSE` @ `1.6`; the licence text is **Portuguese** (*"LICENÇA PÚBLICA GERAL AFFERO GNU, Versão 3"*) | — | `ef909f23755a` @ **`1.6`** | *Diário de classe* — attendance, lesson records, continuous assessment, teacher gradebook |

🔴 **Both are copyleft, and the two grants are not the same constraint.** 🟡 **`i-educar` is
GPL-2.0:** a hosted service built on it is workable, since GPL-2.0 has no network-service clause —
but distributed derivatives must carry the grant. 🔴 **`i-diario` is AGPL-3.0:** hosting a modified
version **triggers the source-offer obligation to users over the network**. 🟢 **Operative
consequence for an engagement:** AI features added *around* `i-educar` (a separate service talking
to its database or API) stay clean; AI features added *inside* `i-diario` and hosted for a
municipality put the modified source under an offer obligation. 🔵 That distinction is the kind a
single "copyleft" label loses, which is why both are written with their version.

🟢 **The permissive escape hatch this shelf already documents remains the answer for a closed
derivative:** [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (**Apache-2.0**) and `TutorLoom`
(**Apache-2.0**) — the two permissive full LMS rows, re-confirmed by `p515` against `p514`'s false
*"every LMS on these shelves is copyleft"*. 🔴 That claim was wrong then and is wrong now.

### 🟢 Curriculum-as-data — a customisation surface this shelf has never listed

🟢 **New capability class, 🇧🇷-originated, MIT/CC BY 4.0:** Brazil's **BNCC** national curriculum is
published as machine-readable open data with per-record provenance —
[`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) (**MIT**, **1,721** learning
objectives, JSON/SQLite/CSV) — plus
[`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) (npm + PyPI + **an MCP
server**) and [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark)
(curriculum-grounded LLM hallucination benchmark, **12★**). 🟡 Both package repos are
**split-licensed: code MIT, data CC BY 4.0, in the same npm tarball and PyPI wheel** — buildable,
with an **attribution obligation that ships inside the artifact**. 🔴 `bncc-pacotes` additionally
withholds **name and visual identity** (*"não licenciados"*), so a derivative may use the data and
may **not** present as BNCC-branded. Full stack treatment in
[`repos/foundations.md`](../repos/foundations.md).

🟢 **Why this matters to an i-educar engagement specifically:** a municipality running `i-educar`
holds enrolment and assessment records; `bncc-dados` supplies the competency map those records
should be scored against; `bncc-benchmark` measures whether a model's curriculum claims are
hallucinated. 🟢 **The three compose into the first LATAM pattern on these shelves that is built
from LATAM-originated, licence-verified parts** — see [`compose/patterns.md`](../compose/patterns.md)
(`P521`).

🟢 **A fifth LATAM row, already here:** *br.tag* resolves as
[`ipti/br.tag`](https://github.com/ipti/br.tag) — **GPL-2.0** from bytes, **20★**, HEAD
`5758efb76754` @ `main`, Brazilian municipal school management (Yii/PHP), 🔴 **no AI component**.
🔴 This pass first inferred `portabilis/br.tag` from its siblings' owner, which does not resolve,
and nearly published that as a nil — the same defect it is auditing (`Gap 516-C`, closed in-pass).
🔵 This base already records that its README claims BSD-3 while the payload says GPL-2.0.



## 🆕 `p515` — `2026-10-28` — **🔴 THIS FILE IS THE WITNESS THAT REFUTES `p514`: it has sold `OpenOlat` (**Apache-2.0**) since `p508` as *"the only permissive full LMS — pick this when the client needs a closed derivative"*, and at L983 it added `TutorLoom` (**Apache-2.0**) as *"second permissive full LMS"* — one pass before `compose/patterns.md` declared *"every LMS on these shelves is copyleft"*. 🟢 Both grants re-read from bytes this pass: `OpenOLAT` **10,982 B** `6dbc5b605ed0be6e`, `TutorLoom` **11,362 B** `a890392684288f18`. 🟢 The consequence is a new engagement, `P521`, that this file's rows supported for seven passes and no pattern ever wrote. 🔴 `make hooks` not attempted (declared abstention).**

🔴 **Gate posture, stated first — and it is NOT the prior 18 denials.** The previous eighteen
passes recorded a classifier **DENIAL** (`Code from External`) on `make hooks`. 🟡 **This pass
the battery was never submitted:** every gate in `HOOK_GATES` executes `$(PY) -I` over Python
inside `compose/code/p*/` — interpreter runs over a freshly cloned third-party working tree —
and this session's standing rule is not to run interpreters over cloned repository content.
🟡 **So `p515`'s posture is a declared abstention, not a refusal received.** The distinction
matters because it is *stable*: a future pass should expect abstention, not retry-and-be-denied.
🔴 `p511`'s **45/63** remains the last gate-attested reading — now **four passes stale**.
🔵 Every figure below is named to the channel that produced it, and the one conflict this pass
resolved is resolved on a channel the refusing pass did not use.

### 🔴 The refutation — `p514`'s own `P518` premise, against this base's live shelves

🔴 **What `p514` published**, in [`compose/patterns.md`](../compose/patterns.md), as the stated
reason `P518` could not have been written earlier:

> *"Every LMS on these shelves is copyleft — Moodle **GPL-3.0**, Chamilo **GPL-3.0**, Open edX
> **AGPL-3.0** — so `P515` had to invent a standards boundary to keep a Globant deliverable from
> touching client source. 🟢 **Sunbird removes the need for the boundary**."*

🔴 **The three licences named are correct. The universal claim around them is false, and it is
falsified by this base's own shelves — one of them written one pass earlier.**

| slug | shelf that holds it | grant as shelved | 🟢 `p515` byte-read, third channel | verdict |
|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | [`verticals/solutions.md`](../verticals/solutions.md) L521, L663, L959; [`repos/foundations.md`](../repos/foundations.md) L557 | **Apache-2.0**, 10,982 B `6dbc5b605ed0…` | 🟢 **Apache-2.0**, `master/LICENSE`, **10,982 B**, `sha256₁₆ 6dbc5b605ed0be6e`, HTTP **200** | 🟢 **IDENTICAL** to the shelved cell |
| [`pacewisdomhq/TutorLoom`](https://github.com/pacewisdomhq/TutorLoom) | [`verticals/solutions.md`](../verticals/solutions.md) L983 (**added `p513`**); [`repos/foundations.md`](../repos/foundations.md) L1134 | **Apache-2.0**, 11,362 B | 🟢 **Apache-2.0**, `main/LICENSE`, **11,362 B**, `sha256₁₆ a890392684288f18`, HTTP **200** | 🟢 **byte count IDENTICAL**; digest newly recorded |

🔴 **This base does not merely contain a counterexample — it advertises one.**
[`verticals/solutions.md`](../verticals/solutions.md) L521 sells `OpenOlat` as *"**The only
permissive full LMS found.** Pick this when the client needs a closed derivative."* L663 reduces
the whole decision to *"OpenOlat (Apache-2.0) **or** accept copyleft."* And L983, written at
`p513` — **the pass immediately before the one that claimed every LMS is copyleft** — introduces
`TutorLoom` as *"Second permissive full LMS after OpenOlat."*

### 🔴 The claim was published TWICE, and the probe found the instance a manual read missed

🔵 **This pass wrote a probe before it wrote the finding** (`compose/code/p515-class-claim/`), and
the probe returned an instance that reading `compose/patterns.md` by hand did not:
[`verticals/solutions.md`](../verticals/solutions.md) **L112**, inside `p514`'s own section —

> *"🟢 **Why it matters more than another LMS would.** Every LMS on this shelf is copyleft — Moodle
> and Chamilo **GPL-3.0**, Open edX **AGPL-3.0**, formaLMS **GPL-2.0** — and the only permissive
> rows have been **small**: `gegok12` (SIS) and a handful of components."*

🔴 **This second instance is the worse of the two**, for three reasons:
1. 🔴 It sits in **the very file whose platform table sells `OpenOlat` as the Apache-2.0 full LMS** —
   the counterexample is roughly 400 lines below the claim, in the same document.
2. 🔴 It does not merely omit the permissive rows, it **mischaracterises them**: *"the only
   permissive rows have been small — `gegok12` (SIS) and a handful of components"*. `OpenOlat` is a
   **448★ full Java LMS**, and `TutorLoom` is a full multi-tenant LMS; neither is a component.
3. 🔴 It then draws the operational conclusion — *"impossible with Moodle or Open edX"* — which is
   true of Moodle and Open edX and **false of the shelf it generalises to**.

🟡 **Both instances are left exactly as published**, per this base's standing practice of correcting
above rather than rewriting history. 🔵 The correction is this section; the original stands below it
under its own heading.

### 🟡 What survives, and the qualifier that carries it

🟢 **The `P518` recipe is sound and is not withdrawn.** Sunbird's MIT grant is real — this pass
byte-read it independently and reproduced `p514`'s cell **exactly**: `master/LICENSE`, **1,072 B**,
`sha256₁₆ 7dde06716f259584`, HTTP **200**. DeepTutor's cell reproduces exactly too: **Apache-2.0**,
**11,408 B**, `sha256₁₆ cd2f54e1e5066644`.

🟡 **What must be rewritten is the justification.** The defensible claim is the one with the
qualifier `p514` used in its own headline and then dropped in its rationale:

> 🟢 Sunbird is the first **national-scale, deployed** permissive learning platform on this shelf.

🔴 **Why this is a commercial correction and not a wording nit.** `P518`'s premise tells a reader
that *"must ship closed + wants a full LMS"* was unsolved until `p514`. On this base's own data it
has been solved since `p508`, by a platform with — per [`repos/foundations.md`](../repos/foundations.md)
L557 — a *"strong EMEA higher-ed footprint"*. 🔴 A proposal built off `P518`'s premise would route
an EMEA closed-derivative engagement to a heavy Indian-ministry stack and never mention the Swiss
Apache-2.0 LMS already on the shelf. 🟢 `P521`, written this pass, is that missing recipe.

### 🔴 The first measured cost of the stale gate

🔵 `HOOK_GATES` carries **`gate-shelf-consistency`** (`p308` — *"no slug may carry disagreeing
licence cells across the live shelves"*, 59 controls) and **`gate-prose-claims`**. 🔴 The battery
has not run since `p511`. 🔴 **In that four-pass window a cross-shelf claim shipped that contradicts
two live rows.** 🟡 This is the first instance on this base where the gate's absence can be shown to
have *cost* something rather than merely being noted as stale — and it argues the staleness is
itself the top-priority gap, above any discovery leg (`Gap 515-A`).


## 🆕 `p514` — `2026-10-28` — **🔴 THE "REFUSE" VERDICT ON `ICTSchool` WAS RIGHT FOR THE WRONG REASON, AND THE RIGHT REASON IS WORSE: it is not unlicensed — it ships the **full GPL-3.0 text** on a branch abandoned in **2022**, while the branch it actually ships from (`main`, last commit **2026-10-13**) carries **no grant at all**. 🟢 A new platform row that is not another LMS: [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal), **MIT**, the portal behind **DIKSHA** — the first national-scale permissive learning platform on this shelf. 🔴 `make hooks` DENIED (18th in 19).**

🔴 **Gate posture:** `make hooks` **DENIED** (`Code from External`). 🟡 `p511`'s **45/63** stands.

### 🔴 `ICTSchool` — "none of its own" is wrong, and the correct reading is a sharper refusal

🔴 **This file's row read:** *"🔴 **none of its own** | `main` | 🔴 refuse — only vendored bower
grants."* 🟢 **The refusal survives. The reason does not.**

| branch | last commit | grant at 20 probed paths |
|---|---|---|
| **`main`** *(default — what a client would deploy)* | 🟢 **2026-10-13** `a76fad328c71` — **active** | 🔴 **NONE** |
| `ictschool-laravel-5.5` | 🔴 **2022-09-23** `0e5b4cbe9f50` — abandoned | 🔴 **GPL-3.0**, `LICENSE`, **35,149 B**, `sha256₁₆ 3972dc9744f6499f` |
| `school-new` | — | 🔴 NONE |

🔵 **Why this is worse than "unlicensed", and the distinction is the whole point.** *Unlicensed*
means no rights are granted and the question ends. 🔴 **This is an active 2026 codebase whose only
grant covers a 2022 branch nobody ships** — so a client who believes "ICTSchool is GPL-3.0" (as
every aggregator says) is relying on a grant that **does not reach the code they installed**. 🔴
**That is a procurement hazard, not a licence choice**, and it is the strongest reason to refuse
this platform that this file has had.

🟢 **Byte-level cross-attestation, free:** the payload is **byte-identical** — 35,149 B,
`sha256₁₆ 3972dc9744f6499f` — to [`frappe/erpnext`](https://github.com/frappe/erpnext)'s
`license.txt`, which this base independently recorded as GPL-3.0 at 35,149 B. 🔵 **Two unrelated
addresses, one canonical payload**: the family read is corroborated, not inferred from a title line.

### 🟢 New layer row — a national-scale permissive learning platform, which this shelf did not have

| field | value, byte-read at `p514` |
|---|---|
| layer | **national / state-scale learning portal** *(content, courses, batches, telemetry)* |
| address | [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) |
| licence | 🟢 **MIT** — `LICENSE`, **1,072 B**, `sha256₁₆ 7dde06716f259584` |
| grant coverage | 🟢 **78 of 79 heads**, default `master` **included** |
| HEAD | `9efc8b5819c6`, **2025-12-16** |
| deployed as | **DIKSHA** — India's national school platform *(APAC)* |

🟢 **Why it matters more than another LMS would.** Every LMS on this shelf is copyleft — Moodle and
Chamilo **GPL-3.0**, Open edX **AGPL-3.0**, formaLMS **GPL-2.0** — and the only permissive rows have
been *small*: `gegok12` (SIS) and a handful of components. 🟢 **Sunbird is the first permissive
platform here that is already running at national scale**, which changes what can be proposed: a
Globant deliverable can be **built into** it and still ship closed, which is impossible with
Moodle or Open edX and is the entire problem `P515` was written to work around.

🟡 **Honest limits, stated before anyone proposes it.**

| limit | reading |
|---|---|
| 🟡 it is the **portal**, not the whole stack | Sunbird Ed is a multi-repo distribution; this row attests **one** repository's grant. 🔴 Every other component needs its own byte-read before a delivery decision — `Gap 514-E` |
| 🟡 **native AI** | 🔴 **none claimed here.** Not probed this pass. Treat as an integration target, exactly as this file treats Moodle |
| 🟡 currency | 🟢 **2025-12-16** — ~10 months. Maintained, not fast-moving |
| 🟡 operational weight | A national-scale platform is heavy. 🔵 It suits a ministry or state engagement, **not** a single-institution pilot |

### 🟢 The layer census at `p514`

| | `p513` | 🟢 `p514` |
|---|---|---|
| layer rows | 37 | 🟢 **38** |
| 🔴 verdicts **corrected** | — | 🔴 **1** — `ICTSchool`, *"none of its own"* → **GPL-3.0 on a dead branch, nothing on the shipped one** |
| 🔴 the **LMS + SIS permissive** nil | 🔴 held 3 passes | 🟡 **not tested this pass** — Sunbird is a learning portal, not an SIS; `Gap 514-C` |
| 🔴 permissive **student-success CRM** (`Gap 513-F`) | 🔴 nil | 🔴 **UNMOVED** — Elastic-2.0 remains the only option, and it forbids the hosted engagement |
## 🆕 `p513` — `2026-10-28` — **🟢 NINE LAYERS THIS FILE HAD NO ROW FOR NOW HAVE ONE, AND EVERY ONE IS PERMISSIVE: LTI launch, SCORM runtime, xAPI spec, badge VALIDATION, institutional repository, collaborative coding IDE, microsite authoring, speech assessment and the local-first tutor. 🔴 The student-success CRM layer gets a row and a REFUSAL in the same line: the only real option is **Elastic License 2.0**, which forbids exactly the hosted engagement it would be bought for. 🟢 `OpenOLAT`'s Apache-2.0 payload re-verified from bytes a second pass running — GitHub's own classifier still reports `NOASSERTION` and is still wrong. 🔴 The LMS-plus-SIS permissive nil holds for a THIRD pass.**

### 🟢 Nine new layer rows — and why they matter more than another LMS would

🔴 **This file had 28 layer rows and no row for a single interoperability standard**, which is the
one thing every engagement actually has to implement. `p511` described the spine in prose; the
table never got it. 🟢 **Now it does**, each grant byte-read at the SHA in
[`foundations.md`](../repos/foundations.md):

| layer added | platform | grant |
|---|---|---|
| **LTI / IMS Global launch** | `tsugi` | Apache-2.0 |
| **SCORM 1.2 + 2004 runtime** | `scorm-again` | MIT |
| **xAPI specification** | `adlnet/xAPI-Spec` | Apache-2.0 |
| **Credential validation** | `openbadges-validator-core` (1EdTech) | Apache-2.0 |
| **Institutional repository** | `DSpace` | BSD-3-Clause |
| **Collaborative coding IDE** | `pytogether` | MIT |
| **Course microsite authoring** | `haxcms-php` | Apache-2.0 |
| **Speech / pronunciation assessment** | `OpenPronounce` | MIT |
| **Local-first adaptive tutor** | `OpenTutor` | MIT |

🟢 **The sellable consequence:** a client on **Canvas (AGPL-3.0)** or **Open edX (AGPL-3.0)** can
now be served by a Globant component that speaks LTI in, SCORM both ways, xAPI out and Open Badges
out — **with every one of those pieces permissive**, so the AGPL boundary stays on the client's side
of the wire and Globant's deliverable stays closed. 🔴 **Before this pass that argument existed in
this repository as a sentence. It is now a table with byte-read grants behind it.**

### 🔴 The student-success CRM layer — a row and a refusal in one line

🔴 **This is the layer most likely to be asked for in a North America higher-ed engagement, and the
honest answer is "not from open source".**
[`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) (**340★**, 76 forks) is the only
substantial open student-success / recruitment CRM found — AI advising assistant, retention CRM,
recruitment CRM, purpose-built for colleges.

🔴 **Its grant is `Elastic License 2.0`** (3 860 B at `1ba02ecb6559`, `sha256₁₆ 48255018b41fc0e9`) —
**not OSI-approved**, and its central restriction is that you **may not provide the software to
third parties as a hosted or managed service**. 🔴 **That is the precise shape of a Globant
engagement**, so the licence forbids the exact use it would be bought for. 🔵 GitHub reports it as
`NOASSERTION`, so a sidebar reader learns nothing and a permissive-family detector learns nothing.

🟢 **What to do instead, stated so the gap is actionable:** build the advising layer on
`iblai/lms` (**MIT**, competency + credentials) for the learner-facing surface and a conventional
CRM the client already licenses for the relationship data. 🆕 `Gap 513-F`: **no permissively
licensed student-success CRM exists on this base, and the one candidate is licence-blocked rather
than missing** — an informed gap, not an unmined one.

### 🟢 `OpenOLAT` — Apache-2.0 re-verified from bytes, and the classifier is still wrong

Re-read this pass at `5b42ca47bd10`: `LICENSE`, **10 982 B**, `sha256₁₆ 6dbc5b605ed0be6e`. 🟢 The
payload is a **verbatim Apache-2.0 body**; the non-canonical length (10 982 B vs 11 358 B) and the
blank first line come from an **OLAT / frentix GmbH attribution statement appended after the
terms**, not from altered terms. 🔴 **GitHub's API reports `NOASSERTION` for this repository**, so
any pipeline trusting the sidebar will record the sector's **only permissive full LMS** as
unlicensed. 🟢 **Second independent byte-attestation across two passes — this row is settled.**
`551 tags` and a current push date; it ships.

### 🔴 The LMS-plus-SIS permissive nil — third consecutive pass

🔴 **Still no single permissive platform that is both a full LMS and a student information system.**
The permissive LMS options (`OpenOLAT`, `Kolibri`, `mentingo`, `open-tutor-ai-CE`) ship **no
enrolment, gradebook-of-record or SIS integration** between them; every real SIS on this base is
**GPL-2.0, GPL-3.0 or LGPL-3.0** (`RosarioSIS`, `Gibbon`, `frappe/education`, `OpenEduCat`) with the
single MIT exception `GegoK12` at **54★**. 🟢 **Restated as an estimate rather than an absence, as
`p511` prescribed:** the gap is an integration build between a permissive LMS and the client's
existing SIS, not a platform search — and `tsugi` (LTI) plus `xAPI-Spec`/`ralph` (telemetry), both
promoted this pass, are the two components that build makes use of.

## 🆕 `p512` — `2026-10-28` — **🔴 THIS FILE'S "PICK BY LAYER" TABLE WAS THE WORST-MAINTAINED SHELF ON THE BASE AND NOBODY HAD EVER SWEPT IT: 11 of its 26 star cells were wrong, 9 of them round, 3 OVERSTATED. 🔵 The reason is structural, not careless — every census in this base's history was framed on BOLDED cells, and this table's column is almost entirely plain. 🟢 Two new platform rows: the MIT peer-assessment layer (North America) and the Apache-2.0 robotics-teaching layer (EMEA). 🔴 The LMS-plus-SIS permissive nil holds for a second pass.**

### 🔴 The table nobody swept, and why the frame missed it rather than the reader

`p510` re-read **24 bolded** star cells; `p511` classified **22** cells by suffix and roundness. 🔴 **Of
the 26 rows in this file's `Pick by layer` table, exactly TWO carry a bolded star cell.** The other
24 are plain, so every typography-framed census this base has run was structurally blind to them.
🟢 **Framed on the table's own `★` column instead, 11 of the 26 are wrong:**

| layer | platform | was | is *(🟢 `p512`, API)* | delta |
|---|---|---|---|---|
| LMS — North America HE | [Canvas LMS](https://github.com/instructure/canvas-lms) | `6,900` | **6,890** | 🔴 **−10, OVERSTATED** |
| LMS — offline-first | [Kolibri](https://github.com/learningequality/kolibri) | `1,200` | **1,162** | 🔴 **−38, OVERSTATED** — and `p511` corrected this exact value on another shelf one pass ago |
| LMS — ease of use | [Chamilo](https://github.com/chamilo/chamilo-lms) | `1,000` | **1,019** | +19 |
| LMS + AI mentoring | [mentingo](https://github.com/Selleo/mentingo) | `100` | **101** | +1 — 🔴 `p511` corrected this one too, on [`agents/top.md`](../agents/top.md) only |
| LMS — modern/greenfield | [LearnHouse](https://github.com/learnhouse/learnhouse) | `2,400` | **2,429** | +29 |
| Virtual classroom | [BigBlueButton](https://github.com/bigbluebutton/bigbluebutton) | `9,300` | **9,258** | 🔴 **−42, OVERSTATED** |
| Structured lessons | [Oppia](https://github.com/oppia/oppia) | `6,900` | **6,950** | +50 |
| Spaced repetition | [Anki](https://github.com/ankitects/anki) | `32,300` | **32,365** | +65 |
| Interactive classroom | [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | `41,700` | **41,710** | +10 |
| Teacher workflow (skills) | [k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | `595` | **600** | +5 |
| Eval runtime for tutors | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | — | 🟢 **14,341**, unchanged from `p511` | 🟢 the one cell `p511` did fix here |

🔵 **Nine of the eleven ended in `00`.** 🔴 **Two of the eleven were hidden even from this pass's own
first frame** — `Canvas LMS` and `k12-teacher-skills` — because their notes column cites a *second*
repository (`canvas-mcp`; `learning-commons-org/agent-skills`) and the extractor's single-address
safeguard abstained on them. The safeguard's cost is measured on [`agents/top.md`](../agents/top.md):
**22 % of cells excluded, 2 of them wrong.** 🟢 Reading the star column **by index** needs no
adjacency, and that is how this table was finally swept.

🟡 **Two round cells in this table are NOT corrected, deliberately.**
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) reads **900** and
re-reads **900 exactly** — a round cell that is a measurement. And
[`openedx/edx-platform`](https://github.com/openedx/edx-platform) reads **8,200** and is **unreadable
on this channel** (`Gap 504-A`, re-confirmed this pass against a known-good control in the same
query): the figure stays with its caveat rather than being guessed at.

### 🟢 Two new platform rows — the layers this file had no row for

| layer | platform | grant (read from bytes) | ★ | why it belongs here |
|---|---|---|---|---|
| 🆕 **Peer assessment / peer review** | [expertiza](https://github.com/expertiza/expertiza) | 🟢 **MIT** — `main/LICENSE` **1,068 B** `cc922786cdca1cd7` | **194** *(🟢 `p512`, API)* | 🟢 **North America** (NSF, NC State). Rubric-driven review mapping, instructor moderation, submission of code / articles / sites. **1,329 forks against 194★** — the strongest deployment signal on this base. 🔴 Grant has **no title line**; a title-anchored gate will report no grant |
| 🆕 **STEM / robotics teaching** | [Open Roberta Lab](https://github.com/OpenRoberta/openroberta-lab) | 🟢 **Apache-2.0** — `master/LICENSE` **11,359 B** `8c6db340475136df` | **147** *(🟢 `p512`, API)* | 🟢 **EMEA**, Fraunhofer IAIS. Browser-delivered block programming for real robots, no install — the K-12 STEM layer, permissive, and state-backed, which is the EMEA procurement answer. 🔴 **Grant is NOT on the default branch `develop`** |

🔵 **What to tell a client about `expertiza` specifically:** peer review is the cheapest credible
place to put AI in an assessment pipeline, because **the model never issues the grade** — it drafts
or checks a peer's review, and a human peer plus an instructor stay in the loop. That is the same
structural answer `P497-1` gives for admissions and `P492-1` for arithmetic, and it is now available
on an MIT platform that institutions already run.

### 🔴 The LMS-plus-SIS permissive nil — re-confirmed, second pass

`p511` re-confirmed on a fresh leg that **no permissive platform covers LMS and SIS together**. 🔴 **It
holds.** The fork-ranked leg — a discovery axis this base had never run, and the one most likely to
surface institutionally deployed administrative software — returned **40 rows and not one permissive
LMS+SIS platform**; the SIS-shaped hits were `expertiza` (peer assessment, not SIS),
`uPortal` (a portal) and `oppia-android` (a client). 🟢 **The nil is now confirmed on the axis most
likely to break it**, which is the strongest form an absence on this base has had. It stays a build
estimate, not an absence of need.

## 🆕 `p511` — `2026-10-28` — **🟢 THE PERMISSIVE EDUCATION STACK HAS A COMPLETE INTEROP SPINE AND THIS FILE HAD NEVER SAID SO: LTI, SCORM, xAPI/LRS and QTI are each covered by an MIT or Apache-2.0 component, all four were already on this base unassembled, and the QTI grant is read here for the first time. 🔴 The LMS-plus-SIS permissive nil is RE-CONFIRMED on a fresh leg, and it is now a build estimate rather than an absence.**

### 🟢 The interop spine — four standards, four permissive components, and why it is the sellable part

🔵 **An education engagement never starts with the model; it starts with whether the thing can talk
to the system of record.** This file has carried the platforms for many passes and never assembled
the layer that connects them. All four licences below are read from bytes on this base:

| standard | what it carries | permissive component | licence, read from bytes this pass | default branch |
|---|---|---|---|---|
| **LTI 1.3 / Common Cartridge** | launching a tool inside any LMS, with roles and grade passback | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0** — `LICENSE` **10,273 B**, `sha256₁₆ 73ba74dfaa520b49` | `master` |
| **SCORM 1.2 / 2004** | the legacy package format every corporate and public catalogue still ships | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** — **1,072 B**, `sha256₁₆ 383b85b370e8da44`, holder *"Jonathan Putney"* | `master` |
| **xAPI / LRS** | the statement store that makes learning analytics possible at all | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **MIT** — `LICENSE.md` **1,094 B**, `sha256₁₆ 08ea77291de9c70f`, holder *"France Université Numérique"* | `main` |
| **QTI 3** | interoperable assessment items | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🆕 🟢 **MIT** — **1,076 B**, `sha256₁₆ 7faa621251d7ed2b`, holder *"Amp-up.io, LLC"* | `main` |

🟢 **All four are LIVE on the git channel, and the QTI grant is read here for the first time** — this
base carried `qti3-item-player` with its licence unread, and it is **MIT**.

🟢 **All four are permissive and byte-attested, which means a Globant-built tutor can be
LTI-launched from Moodle, Canvas or Open edX, consume a SCORM catalogue, serve QTI 3 assessment items
and write xAPI statements to an LRS the client owns — with no copyleft reaching the deliverable and
no vendor API in the critical path.** 🔴 **That is a materially different pitch from "we will
integrate with your LMS", and this file had every part of it without ever stating the whole.**

🟡 **The one caveat that must travel with it:** the LMSs themselves are copyleft —
**Moodle GPL-3.0**, **Open edX AGPL-3.0**, **Canvas AGPL-3.0**, **OpenEduCat LGPL-3.0**. 🔵 LTI is
precisely what makes that acceptable: a tool launched over LTI is **not** a derivative work of the
LMS, so the copyleft stops at the boundary. **The interop layer is the licence firewall.**

### 🟢 `OpenOLAT` — the one Apache-2.0 LMS, and its star cell re-read exact

🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) — **448★** *(🟢 `p511`, API; exact
against the carried cell)*, Apache-2.0 with an appended openolat.org attribution statement (which is
why the API classifier says `NOASSERTION` — explained from bytes at `p508`, **10,982 B**,
`sha256₁₆ 6dbc5b605ed0be6e`). 🔵 **University of Zurich lineage, so EMEA**, and it is the only
permissively licensed full LMS on these shelves. For an EMEA engagement that cannot ship an AGPL
platform, this is the row.

### 🔴 The LMS-plus-SIS permissive nil — re-confirmed, and restated as an estimate

🔴 The prescribed vertical leg was re-run this pass and returns the same shape it has returned every
time: **no MIT or Apache-2.0 platform combines a full student information system with an LMS.** What
exists is split across licences:

| platform | scope | licence |
|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | the only one integrating LMS + SIS + fees + parent app on one database | 🟡 **LGPL-3.0** |
| [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | Laravel school management, API-first | 🟢 **MIT** (`p508`, 1,150 B) — 🔴 but **no fees / exams / transport / hostel models** (`p509`) |
| `Gibbon`, `RosarioSIS` | K-12 SIS | 🔴 **GPL** |
| `Frappe LMS` | LMS only | 🟢 **MIT** |
| `Moodle`, `Chamilo` / `Open edX`, `Canvas` | LMS only | 🔴 **GPL-3.0** / **AGPL-3.0** |

🟢 **The honest form of the finding, carried from `p509` and unchanged:** *"there is no MIT education
SIS"* is **false**; *"there is no MIT education SIS that ships fees, exams, transport or hostel"* is
**true**, and that gap is **a build estimate for a Globant engagement, not a dead end** — `gegok12`'s
MIT core (7,623 files, 107 models, 247 controllers, 108 migrations) is the base those four modules
would be built onto.

### 🔴 Correction in this file

🔴 [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) read
**`14,300★`** here — a **round** number carrying **no provenance suffix**. The API reads **14,341**.
🟢 Corrected in place with its suffix. 🔵 It was one of **four** round cells across these shelves and
**all four were wrong**; the method and the 22-cell census are in
[`agents/top.md`](../agents/top.md)'s `p511` block. **A star cell ending in `00` is unread until
re-read.**

# Education platforms you can customise with AI on top

> 🟢 **`p510` (`2026-10-28`) — THE CLONE REF FOR EVERY VERTICAL ON THIS SHELF IS NOW READ RATHER THAN ASSUMED, AND FOR TWELVE OF THEM `git clone` WITHOUT `-b` DOES NOT GIVE YOU WHAT A PASS READING `main` THOUGHT IT WAS READING.**
> 🟢 **Every vertical here is proven LIVE** and its **true default branch** resolved from `HEAD`'s
> symref: [`liveness-branch-census.2026-10-28-p510.tsv`](../evidence/liveness-branch-census.2026-10-28-p510.tsv).
> 🔵 **This is the shelf the default-branch finding actually bites on, because these are the platforms
> an engagement clones, vendors and pins.** The refs, read this pass:

| platform | true default ref | platform | true default ref |
|---|---|---|---|
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | **`release_11`** | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | **`v31.0.00`** |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **`19.0`** | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | **`2.12`** |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | **`v4.0.x-develop`** | [`overhangio/tutor`](https://github.com/overhangio/tutor) | **`release`** |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | **`mobile`** | [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | **`dev`** |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **`develop`** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **`develop`** |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | **`develop`** | [`frappe/erpnext`](https://github.com/frappe/erpnext) · [`frappe/lms`](https://github.com/frappe/lms) · [`frappe/education`](https://github.com/frappe/education) | **`develop`** |

> 🔴 **Five of these are version-pinned defaults** — `release_11`, `v31.0.00`, `19.0`, `2.12`,
> `v4.0.x-develop` — which a `main` → `master` → `develop` fallback list still misses. 🔴 **And
> `rosariosis` defaults to `mobile`**: never infer a default ref from how its name reads.
> 🔴 **The practical hazard is the opposite of a 404, which is why no pass caught it by eye.**
> `GibbonEdu/core` and `bigbluebutton` answer **200 on both `main` and `master`** though neither is
> default, and `kolibri`, `openeducat_erp` and `ILIAS` answer **200 on `master`** — so a hardcoded
> probe silently reads a **stale branch** and reports success.
> 🟢 **Measured, the licence bytes are identical on 7 of 7** that serve a `LICENSE`
> ([`stale-branch-byte-compare.2026-10-28-p510.tsv`](../evidence/stale-branch-byte-compare.2026-10-28-p510.tsv)),
> **so no licence cell on this shelf is wrong.** 🔵 **The exposure is in versioned content — code,
> migrations, release notes — where a stale branch and the default ref genuinely differ, which is
> exactly what a vendoring engagement reads.**
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`) — sixteenth denial in seventeen
> passes.** Nothing in this pass is gate-attested.

> 🟢 **`p509` (`2026-10-28`) — `Gap 508-C` CLOSES WITH CONTENT: `gegok12` IS A REAL SIS CORE, NOT AN OPEN-CORE SHELL — AND THE MODULES IT LACKS ARE EXACTLY THE REVENUE MODULES. 🟢 A VERTICAL THIS BASE HAD AS UNGRANTED IS GPL-2.0, AND ITS GRANT WAS HIDING IN THE INSTALLER.**
> 🟢 **`Gap 508-C` asked whether the MIT [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12)
> repository holds the school-management core or an open-core shell, and said the tree was the half
> that could be done here. Done — and the answer is favourable.** **7,623 files**, **107
> `app/Models`**, **247 `app/Http/Controllers`**, **108 migrations**. The SIS domain is present and
> named: `Admission`, `Attendance`, `AcademicYear`, `Assignment`, `AssignmentApproval`, `Discipline`,
> `Book`/`BookLending`/`BookCategory`, `ClassRoomPage`, `Conversation`, `Bulletin`, `Feedback`,
> `Document`, `Group`, plus a four-model `Payroll*` set. 🟢 **`custompackages/` is not withheld paid
> modules — it is a vendored third-party library** (`brozot/laravel-fcm`, Firebase Cloud Messaging,
> 73 files). 🔴 **But the absence is as informative as the presence: zero models match
> `fee`/`invoice`/`exam`/`result`/`transport`/`hostel`.** 🔵 **Those four are the classic paid add-ons of every
> commercial school-management suite, and they are the ones missing from the MIT repository.**
> 🟡 **Measure definition, per `T31`:** this is a count of filenames under `app/Models/` matching
> that pattern — a module under another name, or implemented without a model, would not be counted.
> Reads: [`gegok12-packaging.2026-10-28-p509.tsv`](../evidence/gegok12-packaging.2026-10-28-p509.tsv).
> 🟢 **So `p501`'s standing finding reaches its final shape.** *"There is no MIT-licensed education
> ERP/SIS"* is **false on the licence axis** (`p508`, from bytes) and now **false on the substance
> axis too** — `gegok12` is a 107-model Laravel SIS under a complete MIT grant. 🔴 **What is true is
> narrower and more useful: there is no MIT education SIS that ships fees, examinations, transport or
> hostel.** That is a **build estimate, not a disqualification**, and it is the sentence to take into
> an engagement.
> 🟢 **A correction in this base's favour: [`formalms/formalms`](https://github.com/formalms/formalms)
> is GPL-2.0, not ungranted.** A 19-path probe returned **no payload** and the API carries **no
> `license` object** — the detector is blind to it. 🟢 Tree enumeration found the grant at
> **`html/lib/System/license/license_english.txt`** — **15,146 B, `sha256 81688a796b2f7a4f`**,
> opening `GNU GENERAL PUBLIC LICENSE Version 2, June 1991`, shipped in **four languages**
> (english, croatian, bosnian + an `index.html`) because it is displayed by the **installer**.
> 🔵 **The grant was never missing; it was in the product rather than at the root.** 🔴 Still
> copyleft, so still not a client base — but *"GPL-2.0, grant served from the installer directory,
> detector blind"* is a true row where *"no grant"* was a false one.
> 🔴 **And one vertical has no own grant at all:
> [`ictinnovations/ICTSchool`](https://github.com/ictinnovations/ICTSchool)** — 2,313 files, and
> **every** licence file sits under `public/bower_components/` (bootstrap, datatables, flot).
> 🔵 **Vendored dependency licences are not the repository's grant.** Refuse it on that basis.
> 🟢 **Verticals re-attested from bytes, not from a detector field:**
> [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) **GPL-3.0** (`master/LICENSE`,
> **35,147 B `8ceb4b9ee5adedde`**) — 🔵 note it *also* serves a 1,614 B `license.txt` that is a
> **copyright roll, not a grant**, and a first-match probe quotes the wrong one;
> [`openedx/edx-platform`](https://github.com/openedx/edx-platform) **AGPL-3.0** — **35,136 B
> `e12d785697426f9d`**, 🟢 *which re-attests `p506`'s `Gap 504-C` reading (35,136 B, `e12d78569742`)
> independently, on a different pass and a different probe*;
> [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) **GPL-2.0** on `develop`;
> [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) **Elastic-2.0** (3,860 B) —
> 🔴 **source-available, not open source**, and the only AI-native student-success CRM on this shelf.
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`).** Nothing here is gate-attested.

### 🟢 `p509` — what a client can actually build on, by grant and not by reputation

| platform | grant (read from bytes) | branch the grant lives on | client posture |
|---|---|---|---|
| [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | 🟢 **MIT**, 1,150 B `b8694396d7dc6439` | `main` | 🟢 **the only permissive full SIS on this shelf.** Build fees/exams/transport/hostel; inherit the other 107 models |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL-3.0**, 35,147 B `8ceb4b9ee5adedde` at `COPYING.txt` | `main` | 🟡 integrate alongside; never vendor into a product |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0**, 35,147 B `8ceb4b9ee5adedde` | `master` | 🟡 same — 🔵 **byte-identical to Moodle's payload**, a useful consistency control |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 | `master` | 🔴 AGPL reaches networked use |
| [`formalms/formalms`](https://github.com/formalms/formalms) | 🔴 **GPL-2.0**, 15,146 B — 🆕 grant found in the installer dir | `master` | 🟡 the payload's only *"any later version"* string is the GPLv2 **appendix boilerplate**, so the project's own `or-later` election is **not readable from it** — `p455`'s second axis stays `UNSTATED` |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 🔴 **Elastic-2.0**, 3,860 B | `main` | 🔴 source-available; licence forbids providing it as a service |
| [`ictinnovations/ICTSchool`](https://github.com/ictinnovations/ICTSchool) | 🔴 **GPL-3.0 on `ictschool-laravel-5.5` ONLY** — 35,149 B `sha256₁₆ 3972dc9744f6499f`; 🔴 **nothing on `main`** *(corrected `p514`; read* **none of its own** *before)* | `main` **2026-10-13** vs grant branch **2022-09-23** | 🔴 **refuse — and for a sharper reason:** the shipped branch carries no grant, so the GPL-3.0 every aggregator prints does not reach the deployed code |
| [`frappe/education`](https://github.com/frappe/education) | 🟡 **GPL-3.0 declared in 19 bytes**, no licence body | `develop` | 🔴 family stated, text absent — treat as GPL-3.0 and ask upstream to serve the text |


> 🔴 **`p508` (`2026-10-28`) — `p507`'s HEADLINE VERTICAL FINDING IS REFUTED ON THE BYTES, AND THIS BASE HAD ALREADY READ THOSE BYTES.**
> 🔴 **`p507` wrote that [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) is *"published as
> MIT by its own site… the repository does not substantiate it"*, on the strength of
> `license.spdx_id: NOASSERTION`. The repository substantiates it completely.**
> `main/LICENSE` → **HTTP 200, 1,150 B, `sha256 b8694396d7dc6439fdfb4d0fa151903268984f2f90db2c18e124adcc1dd72ca9`**,
> opening `MIT License` with an explicit `<!-- SPDX-License-Identifier: MIT -->` and the holder line
> **"Copyright (c) 2025 GegoSoft Technologies and GegoK12 Contributors"** — the full MIT permission and
> warranty paragraphs follow. 🔵 Control: `satvik314/educhain`'s detector-recognised MIT is **1,092 B**;
> `gegok12` is **+58 B** on the same family, which is the SPDX comment line. **The embedded comment is
> the most likely reason the detector abstains.**
> 🔴 **The defect class is this base's own worst one, and it is not the carry — it is a DETECTOR FIELD
> OVERTURNING A BYTE READING THE BASE ALREADY HELD.**
> [`open-gaps.md`](../intel/open-gaps.md) records, under the `no-label` signal, that it *"fires on
> `gegok12`'s plain **1 150-byte MIT payload**"* — the same payload, the same byte count, read passes
> ago. `p507` did not contradict a missing fact; it contradicted a recorded one.
> 🟡 **So `p501`'s standing finding splits, and only the licence half falls.** *"There is no
> MIT-licensed education ERP/SIS"* is **false on the licence axis**: `gegok12` is a full Laravel
> school-management system (SIS) — **54★ / 102 forks, `archived: false`, pushed 2026-09-23** — under an
> MIT payload. 🔴 **What survives are different objections, and they are live:** `Gap 298` records
> **3 distinct `%ae`** with a **shared role account at 67.5% of commits**, `Gap 411-C` records that its
> `composer.json` is the **unedited `laravel/laravel` skeleton** (so the manifest's `"license": "MIT"`
> is *Laravel's*, not evidence about this project), and the product is **open-core**. 🟢 It is shelved
> below as a **build-with-caveats** row, not as a recommendation.
> 🟢 **And the same correction explains this shelf's most consequential row.**
> [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) — sold here as *"the only permissive full
> LMS"* — **also reads `license.spdx_id: NOASSERTION`** on the API channel. Its `master/LICENSE` is
> **10,982 B, `sha256 6dbc5b605ed0be6e945483f08d48f754762c5b6e65a20f141e85fe5f8700aed4`**, title block
> **`Apache License / Version 2.0, January 2004`**, with an appended *"Additional license statement for
> the openolat.org code base"* naming frentix GmbH and the OLAT 7.1 lineage. **A modified Apache, which
> is exactly what a detector refuses to classify** — and `p317`'s byte reading (*"Apache-2.0 +
> attribution"*) is confirmed at **a filename sweep of five paths: only `LICENSE` exists, there is no
> `NOTICE` file.** 🔴 **Consequence for anyone building tooling off these shelves: a licence filter
> keyed on `license.spdx_id` drops BOTH the only permissive full LMS and the only MIT SIS.**
> 🟢 **Platform shelf re-read on the API channel:** `moodle/moodle` **7,556★**,
> `instructure/canvas-lms` **6,889**, `frappe/lms` **3,350**, `learnhouse/learnhouse` **2,428**,
> `learningequality/kolibri` **1,162**, `overhangio/tutor` **1,130**, `chamilo/chamilo-lms` **1,019**,
> `openeducat/openeducat_erp` **900**, `frappe/education` **682**, `francoisjacquet/rosariosis` **647**,
> `GibbonEdu/core` **635**, `ILIAS-eLearning/ILIAS` **505**, `OpenOLAT/OpenOLAT` **448**,
> `oat-sa/tao-core` **64** — **all fourteen `archived: false`, all fourteen unchanged against `p507`.**
> 🔴 `menthorlabs/menthor` (**582**) and `ably-labs/realtime-quiz-framework` (**77**) stay
> `archived: true` and stay flagged. 🔴 `openedx/edx-platform` remains unenumerable on this channel
> (`Gap 504-A`, now characterised in [`repos/foundations.md`](../repos/foundations.md) `p508`).
> 🔴 **No new platform candidate for a seventh consecutive pass.** The prescribed vertical leg returned
> OpenEduCat (**LGPL-3.0**), Apache OFBiz, Huly, Corteza, Krayin, Dolibarr (**GPL-3.0**) and GegoK12 —
> every one already carried. 🟢 Saturation, declared.
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`).** Reads:
> [`licence-bytes.2026-10-28-p508.tsv`](../evidence/licence-bytes.2026-10-28-p508.tsv),
> [`api-shelf-read.2026-10-28-p508.tsv`](../evidence/api-shelf-read.2026-10-28-p508.tsv).

> 🟢 **`p507` (`2026-10-28`) — THE PLATFORM SHELF IS RE-READ AND UNCHANGED; THE NEWS IS A REGULATORY DEADLINE THAT LANDS ON THESE PLATFORMS, NOT A NEW PLATFORM.**
> 🟢 **Re-read on the API channel, `archived` included:** `moodle/moodle` **7,556★**,
> `instructure/canvas-lms` **6,889★**, `frappe/lms` **3,350★**, `learnhouse/learnhouse` **2,428★**,
> `learningequality/kolibri` **1,162★**, `overhangio/tutor` **1,130★**, `chamilo/chamilo-lms`
> **1,019★**, `openeducat/openeducat_erp` **900★**, `frappe/education` **682★**,
> `francoisjacquet/rosariosis` **647★**, `GibbonEdu/core` **635★**, `ILIAS-eLearning/ILIAS`
> **505★**, `OpenOLAT/OpenOLAT` **448★**, `oat-sa/tao-core` **64★**. 🟢 **`archived: false` on all
> fourteen.**
> 🔴 **[`openedx/edx-platform`](https://github.com/openedx/edx-platform) again absent from the
> index** — third consecutive pass, `incomplete_results: false`. The platform is live; the
> **channel** is lying. Never conclude a vertical platform is gone from a search miss.
> 🔴 **`ably-labs/realtime-quiz-framework` stays flagged `archived: true`** (77★) — `p504`'s fix
> re-verified, still correct.
> 🟢 **`p501`'s standing finding — *there is no MIT-licensed education ERP* — SURVIVES, and this
> pass is the first to test it against a named counter-candidate rather than a nil.**
> 🔴 **`GegoK12` is published as MIT by its own site and by at least two comparison pages. The
> repository does not substantiate it.** [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12)
> — **54★ / 102 forks, PHP/Laravel, `archived: false`**, pushed 2026-09-23 — reads
> **`license.spdx_id: NOASSERTION`**: GitHub detects **no OSI licence** at all. 🔵 **A vendor
> claiming MIT, repeated by comparison sites, against a repository with no detectable grant** — the
> claim travelled, the licence did not. **Do not shelve it as permissive.**
> 🟡 Also surfaced and **not shelved**: [`KlassApp-Foundation/KlassApp`](https://github.com/KlassApp-Foundation/KlassApp)
> — *"an open education protocol for humans and agents"*, Laravel + WhatsApp, **4★**, also
> **`NOASSERTION`**. Interesting framing, far too early, no grant.
> Reads: [`api-shelf-read.2026-10-28-p507.tsv`](../evidence/api-shelf-read.2026-10-28-p507.tsv),
> [`channel-probe.2026-10-28-p507.tsv`](../evidence/channel-probe.2026-10-28-p507.tsv).

### 🔴 `p507` — the compliance clock now runs on the platforms in this file

🔵 Independently re-derived this pass and **matching [`intel/market.md`](../intel/market.md)
exactly** — recorded because `p504` established that *the carry*, not the measurement, is this
base's main defect class, so a clean re-attestation is itself evidence:

| what | value |
|---|---|
| Instrument | 🇻🇳 **Decision 33/2026/QD-TTg**, under AI Law **134/2025/QH15** (in force 1 Mar 2026) |
| Issued / in force | **30 Jun 2026** / **15 Aug 2026** |
| Education systems listed high-risk | **3 of 46**, across six sectors |
| What they are | AI generating self-study content from **uncontrolled data sources**; AI that **examines, assesses or ranks** learners; AI that **monitors learner behaviour** via biometrics or automated means |
| Deadline, already live before 15 Aug 2026 | **1 Sep 2027** |
| Deadline, everything else | **1 Mar 2027** |

🔴 **Read this against the shelf above.** An LMS from this file — Moodle, Canvas, Chamilo, ILIAS,
OpenOLAT, TAO — with **automated grading or ranking switched on** is a listed high-risk system in
Vietnam. 🟡 **The platform is not the regulated thing; the configuration is.** A Globant engagement
that turns on auto-assessment in a Vietnamese deployment inherits a conformity assessment, and
🔴 **a new 2026 deployment gets the SHORTER runway (1 Mar 2027), not the incumbent's 1 Sep 2027.**


> 🟢 **`p506` (`2026-10-28`) — EVERY PLATFORM ROW ON THIS SHELF RE-READ ON THE API CHANNEL; ONE ROW GAINS A BYTE-READ LICENCE AND ONE GAINS ITS PLACE IN THE PERMISSIVE TIER.**
> 🟢 **[`openedx/edx-platform`](https://github.com/openedx/edx-platform)** — the one address the API
> search channel cannot enumerate at all (`Gap 504-A`, third consecutive pass) — now has its licence
> **read from bytes** at its current pin `f73b7ae64dd5`: `LICENSE`, **35,136 B**, title block
> **`GNU AFFERO GENERAL PUBLIC LICENSE Version 3`**, blob `1eb391f38837` (`Gap 504-C` closed).
> 🔵 **An address invisible to one channel is not unverifiable** — `raw.githubusercontent.com` reads
> it fine, so the two channels are complementary rather than redundant.
> 🟢 **[`oppia/oppia`](https://github.com/oppia/oppia) re-read at 6,950★ Apache-2.0, `archived: false`.**
> 🔴 It is also the row that **refutes [`agents/top.md`](../agents/top.md)'s "595-to-41,700 cliff"** —
> this shelf has carried the counter-example to that claim the whole time. Retracted there.
> 🟢 **`archived` ran clean on this shelf:** of three archived addresses across the whole base, none
> is a platform row here, and all three were already flagged.
> 🔴 **No new platform row again this pass**, and the `p505` finding below stands unchanged: **no
> education ERP/SIS exists under MIT or Apache-2.0.**
>
> 🟢 **`p505` (`2026-10-28`) — NO NEW PLATFORM ROW THIS PASS, AND THAT IS THE FINDING.**
> The prescribed vertical query (`open source platform education ERP SIS MIT Apache 2026`) returned
> **OpenOLAT, Apache OFBiz, Sakai, OpenEduCat, ERPNext and Open edX** — 🔴 **every one of them
> already on this shelf**, and the licence picture it returned is the one this shelf already
> publishes: **no education ERP/SIS exists under MIT or Apache-2.0**. OpenEduCat is **LGPL-3.0**,
> ERPNext **GPL-3.0**, Sakai **ECL-2.0** (Apache-derived, not Apache), OpenOLAT **Apache-2.0** but an
> **LMS, not an SIS**. 🔵 **This is a saturation reading on the vertical axis, declared as
> saturation rather than left as silence** — the shelf's standing `T2` position (this layer is
> copyleft and that is the binding constraint) survives a fourth dedicated query.
> 🟢 **Standing checks applied:** `Gap 504-A` reconciliation **4 queried / 4 returned**; `T29`
> `archived: false` on all four addresses read this pass.
> 🔵 One candidate was examined and **rejected** rather than shelved:
> [`mcavaliere/ai-spanish-tutor`](https://github.com/mcavaliere/ai-spanish-tutor) — **1★, no
> `license` field, abandoned `2024-05-20`**. Narrative:
> [`agents/trending.md`](../agents/trending.md) `p505`.

> 🔴 **`p504` (`2026-10-28`) — THIS SHELF WAS RECOMMENDING AN ARCHIVED REPOSITORY AS A BUILD BASE.**
> [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework) reads
> **`archived: true`** on the API. It sat here as the permissive base for live classroom response
> with no end-of-life flag — the licence was verified from bytes, the stars were right, and the one
> field that says *"this project is over"* was never read. 🟢 Flagged here and in
> [`repos/foundations.md`](../repos/foundations.md); **`archived` is now part of the standing batch
> read** for every address, since it costs nothing on a call that already returns stars.
> 🔴 **[`openedx/edx-platform`](https://github.com/openedx/edx-platform) — the Open edX row below —
> is unreadable on the API search channel**: 422 alone, silently dropped from a batch that claims
> `"incomplete_results": false` (`Gap 504-A`). Its figures here are HTML-channel reads and were all
> re-confirmed; treat any future "repo not found" on this slug as an instrument artefact until
> `ls-remote` says otherwise.
> 🟢 All **87** addresses across the three shelves were re-read this pass and the carried figures
> held (`Gap 502-A` **closed**). Reads:
> [`api-shelf-reconciliation.2026-10-28-p504.tsv`](../evidence/api-shelf-reconciliation.2026-10-28-p504.tsv),
> [`api-silent-omission.2026-10-28-p504.tsv`](../evidence/api-silent-omission.2026-10-28-p504.tsv).

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it with two platform rows read from bytes and a resolved Fedena entry. Pre-p490
sections remain in
[`archive/2026-10-27-p490-pre-rewrite/solutions.md`](../archive/2026-10-27-p490-pre-rewrite/solutions.md).
New evidence:
[`licence-and-stars.2026-10-27-p491.tsv`](../evidence/licence-and-stars.2026-10-27-p491.tsv).

The "Odoo for education" question, answered by layer. Each row is a real, deployed system with a
license read from bytes at a pinned SHA — see
[`licence-and-stars.2026-10-27-p490.tsv`](../evidence/licence-and-stars.2026-10-27-p490.tsv).

## Pick by layer

| Layer | Platform | License | ★ | Why this one |
|---|---|---|---|---|
| **LMS — mass market** | [Moodle](https://github.com/moodle/moodle) | GPL-3.0 | **7,556** *(`p504`, API)* | Largest installed base; 2,000+ plugins. A Moodle plugin is the lowest-friction way to ship AI into an existing institution. |
| **LMS — higher ed / MOOC** | [Open edX](https://github.com/openedx/edx-platform) | AGPL-3.0 | 8,200 *(🔵 `p504`: HTML only — **the API search channel cannot see this repo**, `Gap 504-A`)* | University and workforce standard. Deploy via [Tutor](https://github.com/overhangio/tutor) (AGPL-3.0), not by hand. |
| **LMS — North America HE** | [Canvas LMS](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 6,890 *(🟢 `p512`, API)* | Dominant in US higher ed. Has a real MCP server already: [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, 309★). |
| **LMS — permissive** | [OpenOlat](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** 🔵 *by payload: `master/LICENSE` 10,982 B, `sha256 6dbc5b605ed0…`, Apache 2.0 title block **plus** an openolat.org attribution statement — so the API `license.spdx_id` reads `NOASSERTION` (`p508`)* | 448 | **The only permissive full LMS found.** Pick this when the client needs a closed derivative. 🔴 Tell any automated licence gate about the payload reading, or it will reject this row. |
| **LMS — offline-first** | [Kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1,162 *(🟢 `p512`, API)* | Runs without connectivity. Decisive for rural LATAM/Africa/APAC and for national programmes. |
| **LMS — ease of use** | [Chamilo](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,019 *(🟢 `p512`, API)* | Francophone + LATAM public sector. |
| **LMS — DACH** | [ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | German universities and public sector; SCORM-strong. |
| **LMS + AI mentoring** | [mentingo](https://github.com/Selleo/mentingo) | **MIT** | 101 *(🟢 `p512`, API)* | Small, modern, AI-native, multi-tenant via Postgres RLS. The best permissive *starting codebase* rather than a migration target. |
| **LMS — modern/greenfield** | [LearnHouse](https://github.com/learnhouse/learnhouse) | AGPL-3.0 | 2,429 *(🟢 `p512`, API)* | **New `p491`.** "Next-gen" course and content platform, modern stack. Larger than Kolibri or Chamilo by stars and previously missing from this KB. 🔴 AGPL — not a closed-SaaS base. Default branch `dev`. |
| **SIS / school mgmt (Frappe)** | [frappe/education](https://github.com/frappe/education) | GPL-3.0 *(declared)* | 682 | **New `p491`.** Admissions, students, programmes, fees on the Frappe stack. 🔴 Grant is a **19-byte stub** naming GPL v3 with no license text — family is GPL-3.0, paperwork is incomplete. **Not the same license as `frappe/lms` (AGPL-3.0).** |
| **Education ERP** | [OpenEduCat](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 900 *(🟢 `p512`, API)* | Admissions, fees, library, hostel, timetable — on Odoo. This is the literal Odoo answer. |
| **SIS (K-12)** | [RosarioSIS](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 647 | Enrolment, scheduling, grades, attendance, billing. |
| **SIS — permissive, with caveats** | [GegoK12](https://github.com/Gego-K12/gegok12) | **MIT** 🟢 *by payload: `main/LICENSE` 1,150 B, `sha256 b8694396d7dc…`, holder GegoSoft Technologies (`p508`)* | 54 | 🟢 **New row `p508`, and it reverses `p507`:** a full Laravel school-management system (SIS) under a complete MIT grant, API-first, mobile-app ready. **The counter-example to this file's "no permissive education SIS" line — on the licence axis only.** 🔴 **Caveats are the reason it is not a recommendation:** 54★ / 102 forks, **open-core** packaging unmeasured (`Gap 508-C`), **3 distinct author emails with a shared role account at 67.5% of commits** (`Gap 298`), and its `composer.json` is the unedited `laravel/laravel` skeleton so the manifest proves nothing (`Gap 411-C`). |
| **School management** | [Gibbon](https://github.com/GibbonEdu/core) | GPL-3.0 | 635 | Teacher/student/parent/leadership workflows. |
| **Assessment / exams** | [TAO](https://github.com/oat-sa/tao-core) | GPL-2.0 | 64 | QTI-standard computer-based testing. The only substantial open assessment engine. |
| **Interactive content** | [H5P](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 152 | 50+ interactive content types; embeds into Moodle, Canvas, Open edX. |
| **Virtual classroom** | [BigBlueButton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | 9,258 *(🟢 `p512`, API)* | Live classes with whiteboard and breakouts. **LGPL — linking allowed**, the friendliest copyleft here. |
| **Structured lessons** | [Oppia](https://github.com/oppia/oppia) | **Apache-2.0** | **6,951** *(🟢 `p513`, API; `p512` 6,950)* | Lesson "explorations" with built-in misconception handling. Permissive. |
| **Spaced repetition** | [Anki](https://github.com/ankitects/anki) | AGPL-3.0 | 32,365 *(🟢 `p512`, API)* | Reference SRS scheduler. Use as the algorithm reference even where the code can't ship. |
| **Interactive classroom / courseware** | [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | **41,712** *(🟢 `p513`, API; the `p512` cell read 41,710 while `p510` and `p509` both read 41,712 — the `p512` figure was the outlier)* | 🟢 **New row `p493`** (restored — see below). Topic or document → multi-agent interactive lesson with slides, quizzes, project work. **The largest permissive asset in this file by 4×.** 🔴 **Not an LMS**: no enrolment, gradebook or SIS integration. Pair it with Kolibri or OpenOlat for the institutional layer. |
| **Tutoring platform — permissive** | [open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** | 114 | 🟢 **New row `p493`** (restored). The permissive answer where ChatTutor (AGPL-3.0) was the only option. 194 forks against 114★ — deployment, not stargazing. |
| **Academic integrity** | [Dolos](https://github.com/dodona-edu/dolos) | **MIT** | 355 | 🟢 **New row `p493`** (restored). Source-code plagiarism detection; **3,865 commits**, Ghent University. The layer this file previously left empty — and the one every client asks about the moment a tutor can write code. |
| **Teacher workflow (skills)** | [k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | **Apache-2.0** | 600 *(🟢 `p512`, API)* | 🟢 **New row `p493`** (restored). Four K-12 teacher skills **plus eval rubrics**, co-developed with Learning Commons; consortium-side twin at [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills) (Apache-2.0, 40★). 🔵 A skill pack has no runtime — nothing to host, no data residency posture. |
| **Tutoring evaluation** | [pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | 13 | 🟢 **New row `p493`** (restored). 1,143 teacher-exam questions (920 CDPK / 223 SEND), 100+ models, `arXiv:2506.18710`. 🔴 13★ — a corpus and baseline, not a dependency. |
| **Low-bandwidth delivery** | [rumi-platform](https://github.com/Orenda-Project/rumi-platform) | **Apache-2.0** | 18 | 🟢 **New row `p493`** (restored). **WhatsApp**-delivered learning, 15 languages, 847 commits (Pakistan / Taleemabad). No app, no browser — the delivery surface below even Kolibri's. |
| **Lesson planning** | [Shiksha-Copilot](https://github.com/microsoft/Shiksha-Copilot) | **MIT** | 9 | 🟢 **New row `p493`** (restored). MSR India, VELLM, with Sikshana Foundation. **Every artefact is routed to a teacher for review before classroom use** — a shipped implementation of the human-oversight gate. |
| **Peer assessment / peer review** | [expertiza](https://github.com/expertiza/expertiza) | **MIT** | **194** *(🟢 `p512`, API)* | 🟢 **New row `p512`**, from the fork-ranked leg. Rubric-driven peer review with review mapping and instructor moderation; **1,329 forks / 194★**, NSF-funded (NC State). **North America.** The cheapest credible place to put AI in assessment: the model drafts or checks a *peer's* review and never issues the grade. 🔴 Grant has no title line — tell your licence gate. |
| **STEM / robotics teaching** | [Open Roberta Lab](https://github.com/OpenRoberta/openroberta-lab) | **Apache-2.0** | **147** *(🟢 `p512`, API)* | 🟢 **New row `p512`.** Fraunhofer IAIS; browser-delivered block programming for real robots, no install. **EMEA, state-backed** — the sovereignty answer in a K-12 STEM procurement. 🔴 **The grant is on `master`, not on the default branch `develop`** (11,359 B `8c6db340475136df`): a default-branch probe reports a phantom absence. |

| **LTI / IMS Global launch** 🆕 | [Tsugi](https://github.com/tsugiproject/tsugi) | **Apache-2.0** | **377** *(🟢 `p513`, API)* | 🟢 **New row `p513`.** The standard by which an external tool is launched *from inside* an LMS — the integration every engagement needs, with no copyleft obligation attached. **267 forks against 377★.** 🔵 **71 tags but not a version ladder** (newest-sorted is `PHP_7_2`): **pin the SHA.** |
| **SCORM runtime** 🆕 | [scorm-again](https://github.com/jcputney/scorm-again) | **MIT** | **360** *(🟢 `p513`, API)* | 🟢 **New row `p513`.** Modern TypeScript **SCORM 1.2 + 2004** runtime, 63 tags. 🟢 Pairs with `Papermorph` (MIT, agents shelf), which **emits** SCORM — so generated lessons land inside the client's existing LMS rather than beside it. |
| **xAPI specification** 🆕 | [xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | **Apache-2.0** | **956** *(🟢 `p513`, API)* | 🟢 **New row `p513`.** The **xAPI statement grammar** from ADL, the spec beside `openfun/ralph`'s MIT LRS — together a fully permissive learning-telemetry path. 🔴 **Last pushed `2025-07-03`, 5 tags — read it, do not vendor it.** |
| **Credential validation** 🆕 | [openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) | **Apache-2.0** | **61** *(🟢 `p513`, API)* | 🟢 **New row `p513`.** **Open Badges validation from 1EdTech itself** — verifies a credential is well-formed and genuinely issued, the half of "digital credentials" that issuing tools skip. 🔴 Last pushed `2025-11-04`, default `develop`: reference implementation at a known-good SHA. |
| **Institutional repository** 🆕 | [DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** | **1,105** *(🟢 `p513`, API)* | 🟢 **New row and new address `p513`.** Theses, datasets, OER and the scholarly record, with OAI-PMH harvesting. **1,505 forks against 1,105★ (1.36×)** — the deployment signal for a system each institution runs its own copy of. 🟢 **The most permissive grant in this file.** |
| **Collaborative coding IDE** 🆕 | [pytogether](https://github.com/SJRiz/pytogether) | **MIT** | **261** *(🟢 `p513`, API)* | 🟢 **New row `p513`.** Real-time collaborative editing, live drawing and voice, with Python executing **client-side via Pyodide/WASM**. 🟢 **No per-student container to pay for** — the cost argument in any coding-education build. |
| **Course microsite authoring** 🆕 | [HAXcms](https://github.com/haxtheweb/haxcms-php) | **Apache-2.0** | **130** *(🟢 `p513`, API)* | 🟢 **New row `p513`.** Web-components authoring/publishing for course microsites, Penn State **ELMS/NGDLE** lineage — the **permissive** counterpart to `elmsln/elmsln` (**GPL-3.0**, 253★), which is why this row and not that one. |
| **Speech / pronunciation assessment** 🆕 | [OpenPronounce](https://github.com/Halleck45/OpenPronounce) | **MIT** | **169** *(🟢 `p513`, API)* | 🟢 **New row `p513`.** Phoneme-level English pronunciation scoring, **Wav2Vec2 + DTW**, self-hosted as a named alternative to Azure Pronunciation Assessment. 🟢 **A named model and a named algorithm, not a prompt** — and **no learner speech leaves the tenant**, which is the whole argument in an EMEA or data-residency build. |
| **Local-first adaptive tutor** 🆕 | [OpenTutor](https://github.com/zijinz456/OpenTutor) | **MIT** | **155** *(🟢 `p513`, API)* | 🟢 **New row `p513`.** Block-based adaptive workspace that **runs locally**; upload material → notes, quizzes, flashcards, adaptive tutor. FastAPI, 10+ providers. 🟢 **The only locally-running adaptive tutor on this base** — the row to reach for whenever data residency is the blocker. 🔴 **0 tags**; HEAD drifted `p513` (`Gap 513-A`). |
| **Student-success / advising CRM** 🆕 | [Advising App](https://github.com/canyongbs/advisingapp) | 🔴 **Elastic License 2.0** *(3 860 B at `1ba02ecb6559`, `sha256₁₆ 48255018b41fc0e9`)* | **340** *(🟢 `p513`, API)* | 🔴 **New row `p513` — listed as a REFUSAL, not an option.** AI advising assistant + retention and recruitment CRM for colleges; the only substantial open option at this layer. 🔴 **Elastic 2.0 is not OSI and forbids providing the software to third parties as a hosted/managed service — the exact shape of this engagement.** 🔵 GitHub reports `NOASSERTION`, so neither a sidebar nor a family detector catches it. 🟢 **Instead:** `iblai/lms` (MIT) for the learner surface + the client's existing CRM (`Gap 513-F`). |

## The decision that actually matters on an engagement

**Does the client need to host a modified platform for third parties?**

- **No** (internal use, or they run it themselves) → any row above works. GPL/AGPL obligations
  are satisfied by their own deployment. Take Moodle or Open edX for installed base.
- **Yes, and it must stay closed** → **only three rows survive**: OpenOlat (Apache-2.0),
  Kolibri (MIT), Oppia (Apache-2.0), plus `mentingo` (MIT) as a greenfield base. Everything
  else forces source release to users over a network (AGPL) or to recipients (GPL).
  🔵 **`p491` added two platforms and this shortlist did not change** — both newcomers are
  copyleft. Three passes of platform discovery have not produced a fourth permissive LMS, which is
  itself the answer to "shouldn't we keep looking?".

**The AGPL trap specifically:** Open edX, Canvas, Frappe LMS, Tutor, Anki **and LearnHouse** are
AGPL-3.0.
A Globant-hosted SaaS built on any of them owes source to its users. This is routinely missed
because listicles print "open source" without the family — and in `frappe/lms`'s case print
"MIT" outright, which this pass refuted from bytes.

## AI-on-top integration surfaces that already exist

Don't build the connector — these are real:

| Surface | Repo | License | Reaches |
|---|---|---|---|
| Canvas tool API for agents | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | Canvas LMS; ~102 tools + 8 agent skills |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | MCQs, lesson plans, flashcards |
| Source → study package | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | MIT | PDF/video/web/audio → quizzes + SRS |
| Mastery modelling | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | Bayesian Knowledge Tracing |
| Moodle plugin API | — | GPL-3.0 (plugin inherits) | 2,000+ plugin ecosystem; note the plugin is a derivative |
| Eval runtime for tutors | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | MIT | **14,341** *(🟢 `p511`, API; prior cell `14,300`, rounded and carrying NO provenance suffix — the one cell on these shelves without one, and the one that was wrong: `Gap 510-A`'s tell confirmed)*. Generic LLM eval; **the only permissive base for a tutoring-quality harness** — the education-specific benchmarks are unlicensed (see [`agents/top.md`](../agents/top.md)) |

## Declared gaps

- **No permissive SIS and no permissive assessment engine exist** (see
  [`repos/foundations.md`](../repos/foundations.md)). For a closed SIS or exam product, there is
  no open base — it is a build.
- **No MCP server for Moodle or Open edX reached a usable star floor.** Canvas is the only
  incumbent LMS with a real, maintained agent tool surface. For Moodle/Open edX, the connector
  is engagement work.
- ~~**`Fedena` (claimed Apache-2.0 SIS) could not be resolved.**~~ 🟢 **Resolved `p491`:** two real
  repos ([`projectfedena/fedena`](https://github.com/projectfedena/fedena) 547★,
  [`foradian/fedena`](https://github.com/foradian/fedena) 4★), **neither carrying a license file**.
  The Apache-2.0 claim comes from a README sentence, not a grant. Still not carried as a row — now
  for an evidenced reason rather than an unresolved one.
- **No maintenance signal is available for any row in this file.** Stars and license are readable;
  the latest-commit date is not, on any channel open to this session. A row's presence here means
  *it exists and its license is known*, **not** *it is actively maintained* — do not let a layer
  table imply currency it cannot support.


## 🆕 `p492` — `2026-10-28` — the virtual-classroom layer gains a permissive option

Evidence: [`licence-and-stars.2026-10-28-p492.tsv`](../evidence/licence-and-stars.2026-10-28-p492.tsv).

| Layer | Platform | License | ★ | Why this one |
|---|---|---|---|---|
| **Virtual classroom — permissive** | [apache/openmeetings](https://github.com/apache/openmeetings) | **Apache-2.0** | 688 | Video conferencing, IM, **whiteboard**, collaborative document editing; media via Kurento. Release `v9.1.0` (a security release), ASF governance. **The only permissively-licensed conferencing platform in this file.** |

🔵 **This does not replace the BigBlueButton row above.** BigBlueButton (LGPL-3.0, 9,300★) is
**13× larger** and stays the default for live classes; LGPL already permits linking. Reach for
OpenMeetings only in the narrow case where the deliverable must **ship modified platform source
inside a proprietary product** — the one case LGPL's linking allowance does not cover. At 688★,
treat it as a **considered fallback**, and verify its Kurento dependency first.

### 🔴 Amendment to the Canvas agent-surface row

The [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) entries above remain correct that
it is MIT and the only maintained agent tool surface on an incumbent LMS. 🔴 **Two things changed
this pass:** its HEAD **drifted** to `830bc2ef8389` (licence byte-identical at both SHAs, so
code-only), and `v1.16.0` publishes **four** security advisories where this KB recorded one —
including **Canvas token handling** (`GHSA-7mj9-4mcg-hvhv`) and a **local code sandbox**
(`GHSA-7pp5-29mw-9jq3`). **Pin `v1.16.0` or later, and treat the institutional Canvas API token —
not the tool scope — as the primary asset to protect.** See
[`compose/patterns.md`](../compose/patterns.md) `P490-1`, amended this pass. 🟡 Its tool count is
self-inconsistent upstream (description 102, README 128) — **do not quote a number to a client.**

### 🟢 The "no maintenance signal" caveat above is now too strong

This file states that "no maintenance signal is available for any row." **Release dates are
readable** via page fetch — `openmeetings v9.1.0`, `canvas-mcp v1.16.0` (Oct 2026). Repos that tag
releases **can** be shown to be live; only untagged ones cannot. Next pass should carry a release
date per row.


## 🆕 `p493` — `2026-10-28` — seven layers gained a permissive option, and none of them is a new discovery

Reads: [`licence-and-stars.2026-10-28-p493.tsv`](../evidence/licence-and-stars.2026-10-28-p493.tsv).
Mechanism: [`agents/trending.md`](../agents/trending.md) `p493`.

🔴 **Every row added to the table above was already in this KB** — read, licence-measured, and
recorded as promoted — and then deleted by a full-file rewrite of the shelf files, with no marker
left behind. **This section is a repair, not a find.** Saying so matters: two consecutive passes
have now moved the permissive count, `p492` by discovery (`apache/openmeetings`) and `p493` by
repair, and reading them as one trend would be wrong.

### 🟢 The decision tree in this file changes shape

The question this file says *actually matters* — **"does the client need to host a modified
platform for third parties?"** — was decisive because an AGPL platform at the bottom of the stack
contaminated the whole engagement. That is still true **for the LMS/SIS/assessment core**. It is no
longer true for everything above it.

| layer | before `p493` | after `p493` |
|---|---|---|
| Full LMS | OpenOlat (Apache-2.0) or accept copyleft | **unchanged** — OpenOlat is still the only permissive full LMS |
| SIS | 🔴 no permissive option | 🔴 **unchanged** — none exists |
| Assessment / QTI | 🔴 no permissive option (TAO, GPL-2.0) | 🔴 **unchanged** — none exists |
| Interactive classroom | *not offered* | 🟢 **OpenMAIC (MIT, 41,700★)** |
| Tutoring platform | ChatTutor (AGPL-3.0) | 🟢 **open-tutor-ai-CE (BSD-3-Clause)** |
| Academic integrity | *not offered* | 🟢 **Dolos (MIT)** |
| Teacher workflow | *not offered* | 🟢 **k12-teacher-skills (Apache-2.0)** |
| Evaluation | 🔴 "nothing licensed exists" | 🟢 **pedagogy-benchmark (MIT)** |
| Virtual classroom | BigBlueButton (LGPL-3.0) | OpenMeetings (Apache-2.0), `p492` |
| Low-bandwidth delivery | Kolibri (MIT, offline) | 🟢 **+ rumi-platform (Apache-2.0, WhatsApp)** |

🟢 **Practical consequence:** a client who cannot accept copyleft is no longer pushed onto
OpenOlat-or-nothing for the whole stack. Build the AI layers permissively — courseware, tutoring,
integrity, teacher workflow, evaluation — and confine the copyleft decision to the LMS/SIS/assessment
core, where it is genuinely unavoidable. 🔴 **And confine it honestly:** if the engagement needs a
student information system or a QTI exam engine, there is still no permissive option and the
AGPL/GPL conversation cannot be avoided. That is a four-pass consistent result.

Wired end-to-end as [`compose/patterns.md`](../compose/patterns.md) `P493-1`.

## 🆕 `p494` — `2026-10-28` — no layer changes; one grant re-pinned, one jurisdiction restored

Reads: [`licence-and-stars.2026-10-28-p494.tsv`](../evidence/licence-and-stars.2026-10-28-p494.tsv).
Narrative: [`../agents/trending.md`](../agents/trending.md) `p494`.

🟢 **The layer table above is unchanged.** `p493`'s seven newly-permissive layers hold, and no
platform read this pass showed drift.

🟢 **The tutoring-platform layer's copyleft option is now grant-pinned by bytes, not by tag.**
[`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) re-read first-hand at
`7d9e9052bc5a`: **AGPL-3.0**, `LICENSE`, **34 522 B**, `sha1 3cd688cb1bd7` — **byte-identical** to
this KB's earlier read. 🔴 **The consequence is unchanged and now defensible from the payload rather
than from a sidebar label: AGPL reaches across the network, so hosting ChatTutor for a client
triggers source obligations on the hosted service.** 🟢 The permissive answer in this layer remains
[`open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) (BSD-3-Clause, 1 531 B,
`196c547291da`) — **with its third condition honoured**: attribution in `NOTICE`, yes; *"built on
Open-TutorAI"* in client-facing marketing, **no**, absent written permission.

### 🔵 A deployment-posture input this file had lost

An APAC regulatory posture relevant to **how** these platforms get deployed was deleted from
[`../intel/market.md`](../intel/market.md) by `p315`'s rewrite and is restored this pass: **Singapore's
Model AI Governance Framework, its generative-AI framework, its Model AI Governance Framework for
Agentic AI (IMDA, 22 Jan 2026) and AI Verify are all voluntary — but vendors selling into government
and banks are expected to point to them**, which makes a voluntary instrument a **procurement gate**.

🟢 **Why it matters when picking a platform rather than a model.** The agentic framework asks how much
**autonomy** an agent is granted, how its actions are **bounded and logged**, where the **human** sits,
and who is **accountable when several agents interact**. 🔵 **Those are platform properties, not model
properties** — a platform that cannot emit a per-action log, or that has no place to put a teacher
review step, cannot be made conformant by swapping the model underneath it.
[`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot)'s shipped design — every
generated artefact routed to a teacher before classroom use — remains the shape to copy at this layer.
Full build guidance: `P494-1` in [`../compose/patterns.md`](../compose/patterns.md).


## 🆕 `p495` — `2026-10-28` — the Odoo answer is byte-verified, and the Canvas surface gets a version floor

### 🟢 `OpenEduCat` — the Education-ERP row, read from the payload

This file's **Education ERP** row has carried `OpenEduCat` as LGPL-3.0 on a shelf tag. 🟢 **Read
first-hand this pass and confirmed**: LGPL-3.0, **`8 241 B`**, `sha1 2979df12244d`, at pin
`46a5d7d40082` (stable). 🔵 It remains *"the literal Odoo answer"* — admissions, fees, library,
hostel, timetable, on Odoo — and it remains the right base for a LATAM administration engagement,
where [`../intel/market.md`](../intel/market.md) `p495` now places the numeric opening (UNESCO
IESALC: administration adoption **34.1%**, against teaching & learning at **73.5%**).

🔴 **One defect found in the grant itself, and it changes the paperwork on an engagement.** Line 1
of its `LICENSE` reads *"For copyright information, please see the COPYRIGHT file"* — and
`COPYRIGHT` returns **`404`**. LGPL-3.0 requires preserving copyright notices; **the repository
points that obligation at a file that does not exist.** 🔵 **Do:** ship the `LICENSE` verbatim, cite
the pin as provenance, and request the `COPYRIGHT` file from the maintainers in writing. **Do not**
reconstruct attribution from commit metadata.

### 🔴 Amendment to the Canvas agent-surface row — a **version floor**, not a preference

The Canvas integration surface in this file is [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp).
🔴 **It now carries a hard minimum**, read first-hand this pass:

| constraint | value | why |
|---|---|---|
| minimum version | 🔴 **`v1.16.0`** (= `b3f06c76e435`) | **all four** published advisories are patched there; **two are High** (`GHSA-7pp5-29mw-9jq3`, CVSS **7.8**, sandbox escape; `GHSA-hmr8-mvr2-mvw5`, prompt injection → data disclosure / **grade change**) |
| pin style | 🔴 **the release tag, never branch HEAD** | HEAD (`47394125364b`) is **unreleased code above the newest tag**, and no `v1.17.0` exists |
| runtime | 🔴 **Node.js ≥ 22.18** | the `1.16.0` sandbox fix works via **Node's permission model**; on an older Node the advisory is **not actually closed** while the version string says it is |
| tool posture | 🔴 **disable `execute_typescript`** | the advisory states as **unfixed**: egress blocking is best-effort and **executed code can still reach the caller's Canvas token** |
| credential | 🔴 **scoped, short-lived Canvas token** | `GHSA-7mj9-4mcg-hvhv` (Moderate): the bearer token is sent to a URL **chosen by the file-storage host** |

🔵 **Read the shape of this, not just the rows.** This is the **only maintained agent surface on an
incumbent LMS** this KB has found, so it stays the recommended integration point — but the honest
posture is *"deploy it pinned, hardened and with the code-execution tool off,"* not *"deploy it."*
The full recipe is [`../compose/patterns.md`](../compose/patterns.md) **`P495-1`**.

### 🔴 Declared gap — the vertical-platform query returns no permissive platform, third pass running

🔴 The brief's `open source platform education ERP CRM MIT Apache` query returned **no MIT- or
Apache-licensed education platform** again: `OpenEduCat` (LGPL-3.0), `Apache OFBiz` (Apache-2.0 but
not education), generic MIT CRMs (not education), `CK-ERP` (2010, dead). 🟢 **Structural conclusion,
now stable across three independent passes: in this layer the mature systems are copyleft, and the
engagement question is which obligation the client can carry** — which is what this file's decision
tree already asks. Registered as `NO-PERMISSIVE-PLATFORM` in the `p495` claim register so a later
rewrite cannot quietly drop it.



## 🆕 `p496` — `2026-10-28` — the special-education layer has **no platform**, and that is the finding

🔴 **No layer in this file changes, and the platform query returned one vendor for the third pass
running** (nine `openeducat.org` pages in eight languages, no second platform). The LGPL-3.0 reading
`p495` byte-verified stands.

🆕 **What is new is a layer this file never had: special education.** Discovery this pass produced
eight addresses in it (see [`../agents/top.md`](../agents/top.md) `p496`), and the shape of what
exists is the useful part for an engagement:

| layer | what exists | permissive answer |
|---|---|---|
| IEP / §504 **knowledge packs** (law, sources, checklists) | three, all MIT | 🟢 [`jscott5811/IEP-and-Section-504-Plans-Skill`](https://github.com/jscott5811/IEP-and-Section-504-Plans-Skill) **(US federal)**, [`robotros/California-IEP-AI-project-kit`](https://github.com/robotros/California-IEP-AI-project-kit) (California), [`67tallchris/iep-builder`](https://github.com/67tallchris/iep-builder) (Arizona K-8) |
| IEP **rendering / plain-language output** | one, MIT, **deterministic** | 🟢 [`rtwergrfh-cmyk/iep`](https://github.com/rtwergrfh-cmyk/iep) |
| IEP **drafting pipeline** (multi-agent, retrieval, compliance gate) | one, **no grant** | 🔴 **none** — `SudhanvaJ-bit/project-samarth` is a read-only reference design |
| special-education **platform / system of record** | 🔴 **nothing**, open or permissive | 🔴 **none** |

🔴 **So the honest brief for a special-education engagement is: there is no platform to customise.**
Every MIT asset in this layer is a *knowledge pack* or a *renderer*. The system of record stays
whatever the district already runs, and Globant's build sits beside it. 🔵 **That is the opposite of
this file's usual answer** — for LMS, ERP and virtual-classroom work the advice is "customise a real
platform". Here there is no platform, and saying so early is worth more than a shortlist.

### 🟢 A deployment posture this file has never been able to offer: **zero-AI, zero-server**

[`rtwergrfh-cmyk/iep`](https://github.com/rtwergrfh-cmyk/iep) — **MIT**, 1 080 B,
`sha1 fb30401f6782` at `264786ddb518` — converts an IEP PDF into one-page plain-language sheets per
adult (classroom teacher, paraprofessional, substitute, family), plus optional accommodation and
goal-data trackers. 🟢 **It runs entirely in the browser: no server, no AI service, rules only.**
Prints in English or Spanish.

🔵 **Why this matters more than its 0★ and 1 commit suggest.** The hardest objection in a
special-education engagement is not accuracy, it is **data egress** — IEPs are among the most
sensitive records a school holds. A tool that never transmits the document answers that objection
*architecturally* rather than contractually. 🟢 **It is also the cleanest instance of `T9`
(offline-first as a differentiator) this KB holds**, because it is offline by construction rather
than by configuration.

🔴 **Three limits to state before anyone proposes it:**
- **Mixed licensing.** Project code MIT; bundled `pdf.js` **Apache-2.0**; Nunito font **SIL OFL
  1.1**. 🔵 The font licence is the one a compliance review will stop on — OFL restricts
  *renaming* the font, which matters if the output is rebranded for a district.
- **Spanish is partial, and upstream says so.** The classifier works in English only; Spanish IEPs
  are read by rules, and translation uses a built-in phrase list of **~150 common accommodations and
  services**, so many items still need a human translator. 🔴 **Do not sell it as bilingual.**
- **1 commit, 0★, no release tags.** No maintenance signal exists. Treat it as a **seed to fork**,
  never as a dependency to track.

### 🔴 Amendment to this file's Canvas row — unchanged, and restated because it is a floor

No new advisory data this pass. The `canvas-mcp` version floor from `p495` stands in full:
**`v1.16.0` = `b3f06c76e435`**, which patches all four advisories including two High (one at CVSS
**7.8**), **requires Node.js ≥ 22.18** for the sandbox fix to be real, and leaves the caller's Canvas
token reachable by executed code as a declared-unfixed residual. 🟢 HEAD stable for a second
consecutive pass (`47394125364b`), so the pin is a security decision, not a drift workaround.

### 🔴 Declared gaps

- 🔴 **No permissive education ERP/SIS platform** — the mandated platform query has now returned
  none for **three** consecutive passes. `openeducat_erp` (**LGPL-3.0**) by elimination.
- 🔴 **No open special-education system of record**, permissive or copyleft. New gap, declared this
  pass, and it is a supply fact rather than a search artefact: the function-shaped queries that
  found eight application-layer addresses found **zero** platforms.
- 🔵 **No AI-on-top integration surface exists for any special-education system.** The Canvas/Moodle
  surfaces this file catalogues have no counterpart here — there is nothing to attach an agent to.

## 🆕 `p497` — `2026-10-28` — the **admissions / grading / proctoring** layer, which is where the regulator looks and where this file had nothing

Evidence: [`licence-and-stars.2026-10-28-p497.tsv`](../evidence/licence-and-stars.2026-10-28-p497.tsv).
Narrative: [`agents/trending.md`](../agents/trending.md) `p497`. Recipe:
[`compose/patterns.md`](../compose/patterns.md) `P497-1`.

### 🔴 The layer this file was missing, and why it is the expensive one

This file picks a platform **by layer** — LMS, SIS, ERP, assessment, conferencing. The layers it
covers are the ones that *hold* data. 🔴 **The four functions the EU AI Act singles out as high-risk
are not layers in this table at all** — they are *decisions* made on top of it:

**EU AI Act Annex III point 3** designates education AI as high-risk for **admissions**, **grading**,
**placement**, and **exam proctoring**. 🔵 Secondary citation — `eur-lex.europa.eu` is `ENOTFOUND`
from this session (`p495`), so the instrument text has not been read here.

🟢 **This is the commercially useful cut of this file**, because those four decisions are exactly
where a client needs a conformance story and exactly where the open-source supply is thinnest.

| Annex III function | best open-source starting point | licence | state of supply |
|---|---|---|---|
| **Admissions** | [`ASUCICREPO/Admissions-AI-Agent`](https://github.com/ASUCICREPO/Admissions-AI-Agent) | **MIT** (1 123 B, `sha1 8a0aae668604`) | 🔴 **One asset, 5★, found `p497`.** Arizona State University's AI Cloud Innovation Centre. Reference architecture only — AWS Bedrock AgentCore, so the MIT grant covers orchestration, not a portable runtime |
| **Grading** | [`TaiRuiQu/oh-my-paper`](https://github.com/TaiRuiQu/oh-my-paper) (MIT, `refs/heads/v2`), [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) (MIT, plagiarism), [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) (GPL, assessment platform) | mixed | 🟡 Thin but real. `oh-my-paper` is 1★; `dolos` at 3,865 commits is the maintained one but detects plagiarism rather than grades |
| **Placement** | — | — | 🔴 **Nothing.** No open-source placement/streaming system found in any pass |
| **Exam proctoring** | [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) (357★), [`vardanagarwal/Proctoring-AI`](https://github.com/vardanagarwal/Proctoring-AI) (633★) | 🔴 **neither permissive** | 🔴 `topic:proctoring` holds **145** repositories and produced **no permissive asset** this pass. For a designated high-risk function |

### 🟢 What to tell a client, by layer

- **Admissions.** There is one MIT reference design and it is a university's, not a vendor's. 🟢 Read
  the adviser-handoff boundary in it — the design decision that keeps a human in the loop on the
  decision itself is the one that carries the Annex III story. Re-implement on your own runtime
  rather than inheriting Bedrock AgentCore.
- **Grading.** 🔴 **Never let the model do the arithmetic** — that is `P492-1` and it stands. Compose
  `oh-my-paper`'s marking flow or build fresh, with scoring in deterministic code.
- **Placement.** 🔴 Greenfield. Price it as a build.
- **Proctoring.** 🔴 The honest answer is that the permissive supply does not exist. Safe Exam
  Browser is the credible institutional system and it is copyleft; plan on deploying it **alongside**
  rather than embedding it, or accept the licence.

### 🔵 The ERP question, settled

Asked explicitly this pass: **no permissively-licensed education ERP exists.** ERPNext GPL-3.0,
Dolibarr GPL-3.0, Odoo Community LGPL-3.0, OpenEduCat LGPL-3.0; Apache OFBiz is Apache-2.0 but ships
no education domain model. 🟢 For a closed derivative at the ERP layer: **build the domain model, or
take LGPL-3.0 and keep the Odoo modules separable.** Full reasoning:
[`repos/foundations.md`](../repos/foundations.md) `p497`.

### 🔴 Branch refs for rows in this file

[`rosariosis`](https://github.com/francoisjacquet/rosariosis)'s default ref is
**`refs/heads/mobile`** and [`openeducat_erp`](https://github.com/openeducat/openeducat_erp)'s is
**`refs/heads/19.0`** — both rows in this KB's platform tables. A deployment script that clones
without resolving the symref gets the wrong tree or no tree. Five variants now recorded:
[`branch-ref-census.2026-10-28-p497.tsv`](../evidence/branch-ref-census.2026-10-28-p497.tsv).

---

## 🆕 `p498` — `2026-10-28` — a platform this file calls unusable is **GPL-2.0**, and the one permissive platform turns out to be a **host**

### 🔴 Correction — `formalms` is licensed, and this file said otherwise

🔵 This file has carried [`formalms/formalms`](https://github.com/formalms/formalms) as a
vertical platform with no usable grant, and `Gap 488-L` asked `p498` to mark it unusable. 🟢 **The
opposite edit is the correct one.**

| | |
|---|---|
| grant | 🟢 **GNU GPL version 2, June 1991** |
| at | `html/license.txt` — 18 346 B · blob `e823963cd437` |
| and at | `html/lib/System/license/license_english.txt` — 15 146 B · blob `b6e1c33e0499`, **plus Italian, Spanish, French, German, Portuguese, Croatian, Bosnian and Tamil**, with an `index.html` to serve them |
| at the repository root | 🔴 **nothing** — which is every previous probe's entire answer |
| ref / HEAD / activity | `master` · `446a77a9b9cb` · last commit **2026-07-17** (🟡 three months stale) |
| 🔴 *or-later* election | **none found** — 0 PHP files in the tree cite the GPL. **GPL-2.0-only.** |

🔴 **Shelf verdict, corrected: `formalms` is a GPL-2.0-only LMS, not an ungranted one.** 🟡 It is
still not a recommendation — three months without a commit, and `Gap 489-L` already warned its 0.70
fork-per-star cannot tell a live deployment from historical forks. **But "unusable, no licence" was
wrong**, and a studio that refused it on this file's say-so refused it for a reason that does not
exist.

🔵 **The transferable lesson for this layer specifically:** an institutional platform that serves its
own licence to end users through its web UI has no reason to keep a copy at the repository root.
**A root-only licence probe is systematically blind to exactly the platforms this file is about.**

### 🔴 The GPL-2.0-only boundary, now measured on two platform rows

| platform | grant | *or-later* elected? | combines with GPL-3.0 code? |
|---|---|---|---|
| 🇧🇷 [`portabilis/i-educar`](https://github.com/portabilis/i-educar) — municipal SIS, ref `2.12`, HEAD `435649b0474f`, last commit **2026-10-22** 🟢 live | GPL-2.0 (root `LICENSE`) | 🔴 **no** — 0 of its PHP files | 🔴 **no** |
| 🇮🇹 [`formalms/formalms`](https://github.com/formalms/formalms) | GPL-2.0 (`html/license.txt`) | 🔴 **no** | 🔴 **no** |

🔴 **Say this in week one of a Brazilian municipal engagement.** `i-educar` is live and maintained,
and it is **GPL-2.0-only**. It cannot take GPL-3.0 code, and the GPL-3.0 platforms on this
file — [`moodle`](https://github.com/moodle/moodle), [`chamilo`](https://github.com/chamilo/chamilo-lms),
[`ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) — cannot take its. The two copyleft families on
this shelf are **not interoperable**, and nothing on this file said so before.

🟡 Read from PHP source notices only; neither tree was read exhaustively for a prose election
(`Gap 498-C`).

### 🟢 `learningequality/kolibri` is an extension host, not a content sink

🔵 This file lists Kolibri as the offline-first delivery platform and the **only permissive**
institutional option. `p498` read its code at HEAD `08e3ecace444` (ref `develop`, last commit
2026-10-27) and the integration surface is larger than this file has claimed.

| surface | what is actually there |
|---|---|
| 🟢 **plugin registry** | `kolibri/plugins/` — **21 in-tree plugins**. A plugin is a Django app with a `kolibri_plugin` module; enabling it adds its apps to `INSTALLED_APPS`. |
| 🟢 **own API** | `KolibriPluginBase` exposes `url_module` and `api_url_module` — a plugin mounts **its own URLs and its own DRF API**. **21 `api_urls.py`** across the tree. |
| 🟢 **runtime kill switch** | plugins enable/disable **from the CLI or a UI**, and via `ENV_VAR_ENABLED_PLUGINS` / `ENV_VAR_DISABLED_PLUGINS` / `ENV_VAR_APPLIED_PLUGINS`. **No rebuild to turn the AI off.** |
| 🔴 **hook singletons** | `KolibriHook` / `KolibriHookMeta(SingletonMeta)` / `HookSingleInstanceError` — **one registration per hook.** Two vendors shipping plugins into one deployment will collide. |
| 🟢 **third-party precedent** | four out-of-tree plugins ship in the repo as `python_packages/`: `kolibri-oidc-provider-plugin`, `kolibri-sentry-plugin`, `kolibri-sync-extras-plugin`, `kolibri-context-translation-plugin`. **OIDC provider as a plugin** — the extension surface reaches authentication. |
| 🔴 **native AI** | **none.** One keyword hit across 3 071 Python/Vue/JS files and it is a false positive (*"transformers"* in a Django `from_db_value` comment, `kolibri/core/content/viewsets/import_metadata.py:152`). |

🟢 **The "no native AI surface" verdict on this row is now a code read at a 2026-10-27 commit**, not
the Apr-2026 secondary comparison `Gap 488-N` objected to. For this row, `Gap 488-N` is closed.

🔵 **The consequence for this file's decision table:** on the permissive path you are not limited to
pre-baking content and importing it. You can ship an **in-platform AI surface** as a plugin, with
the institution holding the off switch, and without forking core. That is a materially better offer
than "generate centrally, import offline", and it is the only permissive route to it on this file.

### 🟡 The institutional layer's permissive count does not move

🔵 Three passes have now ended with the same answer and this one makes four:
[`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0) remains the only permissive full LMS,
`kolibri` (MIT) the only permissive offline platform, and 🔴 **there is still no permissive SIS and
no permissive QTI exam engine.** `formalms`'s re-grading adds a GPL-2.0 LMS to the copyleft column;
it does not add a permissive option. The copyleft conversation on SIS and exams remains unavoidable.

---

## 🆕 `p499` — `2026-10-28` — the "Odoo for education" answer gains a permissive integration layer

**Pass `p499` — reads of 2026-10-28.** This section **extends** the file. Licences read from bytes
at pinned SHAs and graded on the operative-span instrument
([`evidence/canonical/MANIFEST.tsv`](../evidence/canonical/MANIFEST.tsv)); full reads in
[`new-rows-licence-bytes.2026-10-28-p499.tsv`](../evidence/new-rows-licence-bytes.2026-10-28-p499.tsv).

### 🟢 The layer this table was missing

Every row in "Pick by layer" above is a **system of record** — it holds the students, courses and
grades. None of them is the thing you actually write. 🟢 **The integration layer is now on the
shelf, and it is permissive at both standards:**

| Layer | Platform | License | ★ | Why this one |
|---|---|---|---|---|
| 🟢 **LTI tool framework** | [Tsugi](https://github.com/tsugiproject/tsugi) | **Apache-2.0** | 377 | 🟢 **The way into an LMS you do not own.** LTI + IMS Global + Common Cartridge. Works against Moodle, Canvas, Open edX, Blackboard, D2L. **Apache-2.0, so the tool you build stays closed even against an AGPL host.** |
| 🟢 **SCORM / CMI runtime** | [scorm-again](https://github.com/jcputney/scorm-again) | **MIT** | 360 | 🟢 SCORM 1.2 + 2004 + CMI, cross-frame. The courseware-packaging boundary, MIT. Active 2026-10-26. |
| 🟢 **LMS — permissive, new** | [TutorLoom](https://github.com/pacewisdomhq/TutorLoom) | **Apache-2.0** | 52 | 🟢 Second permissive full LMS after OpenOlat — multi-tenant, Django + React. 🔴 **Three weeks old; watch row, not a deployment choice** (`Gap 499-H`). |
| **Skills / credentials** | [iblai/lms](https://github.com/iblai/lms) | **MIT** | 208 | Competency tracking and digital credentials — the layer every workforce-reskilling engagement needs and that had no permissive option here. |
| **Course authoring / microsites** | [HAXcms](https://github.com/haxtheweb/haxcms-php) | **Apache-2.0** | 130 | Course microsite CMS, PHP. Pushed 2026-10-28. |
| **Teaching lab — code** | [pytogether](https://github.com/SJRiz/pytogether) | **MIT** | 261 | Browser-based collaborative Python IDE, real-time. Drop-in for a programming classroom. |
| **Widgets / games over LTI** | [Materia](https://github.com/ucfopen/Materia) | 🔴 AGPL-3.0 | 52 | Embeddable widgets and games. Same UCF stable as UDOIT/Obojobo. 🔴 Hosted derivative must share. |
| **Offline-first services** | [Lokal](https://github.com/Wakoma/Lokal) | **MIT** | 53 | Offline content + local network services. Pairs with Kolibri for low-connectivity deployments. |
| **Spaced repetition — permissive** | [Mnemo](https://github.com/onemnemo/mnemo) | **Apache-2.0** | 122 | 🟢 See the correction below. |

### 🟢 A standing recommendation in this file is now obsolete

The table above carries **Anki (AGPL-3.0)** with the note *"Reference SRS scheduler. Use as the
algorithm reference even where the code can't ship."* 🟢 **That constraint is lifted.** There are
now **two permissive spaced-repetition implementations** read from bytes:
[`onemnemo/mnemo`](https://github.com/onemnemo/mnemo) (**Apache-2.0**, operative IDENTICAL) and
[`kirill-markin/flashcards-open-source-app`](https://github.com/kirill-markin/flashcards-open-source-app)
(**MIT**, operative IDENTICAL, **FSRS** scheduling). 🔵 Anki stays on the shelf as the reference
implementation, but **"the code can't ship" is no longer the end of the sentence** — for SRS
specifically, permissive code now exists.

### 🔵 `formalms` re-graded a second time, and the grade holds

`p498` re-graded [`formalms/formalms`](https://github.com/formalms/formalms) from "no readable
grant" to **GPL-2.0** after finding the payload at `html/license.txt` rather than the repository
root. 🟢 `p499` graded **both** of its GPL-2.0 payloads on the operative instrument (`Gap 498-D`):
**2 489 operative words each, identical diff signatures**, differing from canonical only by the
**1991-vintage FSF transcription** ("Library" for "Lesser", "Franklin St" for "Franklin Street").
🟢 **GPL-2.0 confirmed. Neither payload is truncated or altered** — the 3 200-byte spread between
them is the omitted *How to Apply These Terms* appendix. 🔴 Its staleness is unchanged and still
disqualifying for a new engagement: last commit **2026-07-17** (`Gap 498-E`).

### 🔴 Refused this pass, with reasons

| Platform | ★ | Why refused |
|---|---|---|
| [`ictinnovations/ICTSchool`](https://github.com/ictinnovations/ICTSchool) | 71 | 🔴 **No root grant at any of six probed paths.** School-management software with unified communications — would otherwise fit the SIS layer. |
| [`codeforlife-education/codeforlife-portal`](https://github.com/codeforlife-education/codeforlife-portal) | 54 | 🔴 **121-byte `LICENSE.md` containing only a link.** UK Code for Life schools platform. |
| [`codeforlife-education/rapid-router`](https://github.com/codeforlife-education/rapid-router) | 60 | 🔴 Same 121-byte pointer. Blockly game for ages 5–11. |
| [`studentinsights/studentinsights`](https://github.com/studentinsights/studentinsights) | 135 | 🟡 MIT and clean, but **last push 2024-08-27** — over two years stale. Code for America school-data platform; recorded, not recommended. |

---

## 🆕 `p500` — `2026-10-28` — the permissive LMS row is re-verified, and the student-success layer turns out to be closed

**Pass `p500` — reads of 2026-10-28.** This section **extends** the file; nothing above is
rewritten. Reads:
[`pinned-sha-rows.2026-10-28-p500.tsv`](../evidence/pinned-sha-rows.2026-10-28-p500.tsv).

### 🟢 `OpenOlat` — the "only permissive full LMS" claim survives a byte re-read

This file's single most consequential row is [OpenOlat](https://github.com/OpenOLAT/OpenOLAT)
(Apache-2.0, 448★), because it is the one row that lets an engagement ship a **closed hosted
derivative** of a university-grade LMS. Re-read from bytes at pinned SHA `cd91a957ea2e`
(**10 982 B**): 🟢 **Apache-2.0 confirmed, operative body materially unaltered.** The +99-word
residual against the apache.org canonical form is two appended attribution paragraphs (OLAT
Zentrum, University of Zurich; frentix GmbH) and adds **no condition**.

An independent 2026 vendor round-up also lists OpenOlat as Apache-2.0 — 🟢 **that claim is
correct**, unlike the same genre's **Fedena** claim, which `p491` refuted from bytes. Vendor
licence columns are right about half the time here; the byte read is what decides.

### 🔴 The student-success / advising layer has no permissive option

This is a **new gap in this file's layer map**, and a commercially important one. Student success,
advising and retention is one of the most frequently bought education-AI capabilities. The leading
open-ish implementation:

| Layer | Platform | Licence | ★ | Verdict |
|---|---|---|---|---|
| 🔴 **Student success / advising** | [advisingapp](https://github.com/canyongbs/advisingapp) (Canyon GBS) | 🔴 **Elastic License 2.0**, 3 860 B `4449f765bdd0` | 340 | **Source-available, not open source.** Forbids providing the software to third parties as a hosted service — i.e. it forbids the delivery model an engagement would use. |

🔴 **Consequence for an engagement:** there is **no permissive advising/student-success platform**
to customise. The buildable route is an agent layer over the SIS/LMS you already have — see
[`compose/patterns.md`](../compose/patterns.md) `P500-1` — not a fork of this row. GitHub reports
this repository as `NOASSERTION`, so the restriction is invisible from the API.

### 🟢 Registerable at the content/assessment layer

| Layer | Platform | Licence | ★ | Why this one |
|---|---|---|---|---|
| 🔴 **Live classroom response / quizzing — UPSTREAM ARCHIVED** | [realtime-quiz-framework](https://github.com/ably-labs/realtime-quiz-framework) | **Apache-2.0** | 77 | 🔴 **`p504`: `archived: true` — FROZEN upstream. Fork it or lift the pattern; expect no fixes.** Permissive base for synchronous whole-class response: fan-out, mid-round joins, scoring. Pair with an LMS for roster and gradebook. |
| 🟡 **AI output QA against rubrics** | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | 🟢 code **MIT** / 🔴 corpora **CC BY-NC-SA 4.0** | 87 | Rubric-based QA for generated instructional content (Text Complexity, Feedback, Standards Alignment, Durable Skills). Deploy the **code**; the shipped annotated corpora are **non-commercial** (`Gap 500-E`). |


## 🆕 `p501` — `2026-10-28` — **🔴 THE 6-PATH LICENCE PROBE THIS FILE REASONS WITH PRODUCES FALSE "NO GRANT" VERDICTS, AND THE PROOF IS THE BIGGEST PLATFORM IN THE ERP LAYER: [`frappe/erpnext`](https://github.com/frappe/erpnext) reads `NONE-OF-6-PATHS` and ships **GPL-3.0 at `license.txt`** — lowercase name, lowercase extension, a combination the probe set omits. 🟢 The alumni / advancement CRM layer gains its first row (**CiviCRM, AGPL-3.0, read from bytes**). 🔴 A dedicated query for an **MIT or Apache education ERP** returns none, and the one Apache-2.0 candidate named cannot be resolved to a repository, so it is REFUSED rather than recorded. 🔴 And a published ERPNext version figure is stale by twenty minor releases.**

Reads: [`wide-probe.2026-10-28-p501.tsv`](../evidence/wide-probe.2026-10-28-p501.tsv),
[`licence-bytes-verticals.2026-10-28-p501.tsv`](../evidence/licence-bytes-verticals.2026-10-28-p501.tsv).

### 🔴 The probe, first — because it invalidates verdicts already in this file

| repo | 6-path verdict | 22-path verdict |
|---|---|---|
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 `NONE-OF-6-PATHS` | 🟢 **GPL-3.0**, `license.txt`, **35 149 B**, blob `f288702d2fa1`, at `9afbfa0a67d2` |
| [`0xff-r4bbit/watchmetype`](https://github.com/0xff-r4bbit/watchmetype) | `NONE` | 🔴 **`NONE` confirmed** across 22 forms |
| [`choudaryhussainali/MCQ_Grading_Bot`](https://github.com/choudaryhussainali/MCQ_Grading_Bot) | `NONE` | 🔴 **`NONE` confirmed** across 22 forms |

The missing combination is **`license.txt`** — this base probed `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `COPYING`, `LICENCE` and bare `license`, i.e. it varied *case* and *extension*
**separately but never together**.

🔴 **This file carries at least one verdict reached with the narrow set:**
[`ictinnovations/ICTSchool`](https://github.com/ictinnovations/ICTSchool) is recorded as
*"**No root grant at any of six probed paths**"* and placed in the unusable tier on that basis.
🔵 **That verdict is now unsafe** — not refuted, unsafe. 🔵 Probe width has also varied: an earlier
pass on [`repos/trending.md`](../repos/trending.md) records a row probed at **ten** paths
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license`, `COPYING`, each on `main` **and** `master`) —
🔴 **and `license.txt` is in neither the six-path nor the ten-path set.** A 22-path re-probe of every
`NONE` row is `Gap 501-F`, and until it runs, *"no grant"* on this base means *"no grant at whichever
width that pass happened to use"*, which no file records. 🔵 **The rule:** a negative result from a probe is a statement about the probe's coverage
first.

### 🟢 The alumni / advancement CRM layer — first row

| platform | repo | licence (read at SHA) | layer |
|---|---|---|---|
| **CiviCRM** | [`civicrm/civicrm-core`](https://github.com/civicrm/civicrm-core) | 🔴 **AGPL-3.0**, 34 524 B, blob `1489b7244859`, at `8c7822486842` | constituent / alumni / donor CRM — **the layer above the SIS**, where advancement, alumni events and donor campaigns live |

🔵 **Why it belongs in an education KB:** the layer it occupies is the one a university actually buys
after the LMS and SIS are settled, and this file had **nothing** in it. 🔴 **AGPL-3.0 is the hardest
constraint in this file.** It reaches across the network: hosting a modified CiviCRM for a client
triggers source obligations toward that client's users. `T2`'s re-scoping does **not** rescue this
one — a CRM is not reached over LTI, so there is no arm's-length integration boundary to hide
behind. **Customise it for a client who will host it themselves and accept the grant; do not build a
hosted commercial derivative.**

### 🔴 There is no MIT or Apache education ERP, and the one candidate is refused

A dedicated query (`open source platform education ERP CRM SIS MIT Apache 2026`) returned the layer
this file already holds, and **confirmed the licence posture rather than changing it**:

| platform | licence as returned | already on this file |
|---|---|---|
| OpenEduCat | **LGPL-3.0** | 🟢 yes |
| Frappe Education | **GPL-3.0** | 🟢 yes |
| RosarioSIS | **GPL-2.0** | 🟢 yes |
| Gibbon | **GPL-3.0** | 🟢 yes |
| Dolibarr (not education-specific) | **GPL-3.0** | 🟢 yes |
| ERPNext | **GPL-3.0** 🟢 *now read from bytes this pass* | 🟢 yes |
| CiviCRM | **AGPL-3.0** 🟢 *read from bytes this pass* | 🆕 added above |

🔴 **One Apache-2.0 candidate was named and is REFUSED, not recorded.** The search returned a
*"University Management System (UMS), Apache-2.0, Java desktop and client-server university
administration"* — fees, teacher assignment, exam records. 🔴 **No owner/repo slug was given and
none was resolvable**, and this base does not write a row it cannot pin to a SHA. 🔵 Guessing a slug
is how a 404 becomes a KB entity. Registered as `Gap 501-J`: a named platform with a plausible
licence and no resolvable address is a **lead**, not a finding.

🟢 **So the standing answer on this file is confirmed by a query aimed squarely at overturning it:
the education ERP/SIS layer is copyleft, with no permissive option at the platform tier.** The
permissive work is **above** it — the LTI and integration layer `p499` established (`tsugi`
Apache-2.0, `scorm-again` MIT) and the practice-level agents on
[`agents/top.md`](../agents/top.md). 🔵 That is `T20` holding for a third pass.

### 🔴 A version figure in circulation is stale by twenty minor releases

The query returned ERPNext's *"most recent stable release… August 2026 (v16.32.3)"*. 🔴 **Measured
from the repository's own tags this pass: `v16.52.0`, `v16.52.1` — the `v16.52.x` line.** The cited
figure is **twenty minor versions behind**.

🔵 **Consequence for this file's version floors:** `P498-1` and `P499-2` pin Kolibri to a release
after `Gap 498-G`; the same discipline has to apply to every platform row, and the channel to use is
`git ls-remote --tags`, **not** a search result. A search-sourced version number has no shelf life.


## 🆕 `p502` — `2026-10-28` — **the layer that makes an LMS auditable, and nobody sells it**

This shelf has carried the platforms (Moodle, Canvas, Open edX, Chamilo, ILIAS, OpenOLAT, TAO,
OpenEduCat) for ~35 passes. 🔴 **Every one of them is a system of record for *enrolment and content*
and none of them is a system of record for *what an AI did and who reviewed it*.** That second record
is what the EU AI Act's Art. 26, Oklahoma's grading bar and LATAM's 26%-with-a-strategy finding all
require — and it is a separate, standards-defined layer: **xAPI / cmi5 / Caliper**.

🟢 **It is real, permissive, and customisable in exactly the sense this shelf means** — the same way
Odoo is an ERP you build on top of:

| Platform | Licence (bytes at the pinned SHA) | ★ | Mainline | What you bolt onto it |
|---|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** — 11,356 B `58853eb8199b` | **144** | 🟢 **2 d** `6159416` | 🟢 **The Odoo of this layer.** SQL-backed LRS, runs on SQLite for a pilot and Postgres for an institution; put an agent's review-and-approval events in it and the audit trail is a query |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | **Apache-2.0** — 11,357 B `1128f8f91104` | **334** | 🔴 **502 d** `efa045e` | The US DoD reference LRS. 🔴 **Cite it, do not build on it** |
| [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) | **Apache-2.0** — 11,357 B `1128f8f91104` | 59 | 🔴 281 d `806c0ba` | **cmi5** player + test suite — the launch-and-track profile that replaces SCORM. Pairs with this shelf's SCORM rows |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** — 1,045 B `f1083e4aa47d` | 78 | 🔴 419 d `5bc232d` | 🟢 The **acceptance gate**. Run it against whatever you ship and a procurement office has its answer |
| [`openfun/ralph`](https://github.com/openfun/ralph) | MIT *(carried, `p467`)* | 51 | 🟢 16 d `91fef11` | LRS + ingestion CLI, **EMEA** (France Université Numérique) |
| [`openfun/warren`](https://github.com/openfun/warren) | **MIT** — 1,093 B `14a2c9fcad08` | 17 | 🔴 **708 d** `839fcbb` | The dashboard half. 🟢 **Fork-and-own: MIT, unmaintained, under a dated legal requirement** |

🔵 **Why this belongs on the *verticals* shelf and not only in intel:** the LMS platforms here are
mostly **copyleft** (`T2`'s binding constraint — Moodle GPL-3.0, Canvas and Open edX AGPL-3.0,
Chamilo GPL-3.0). 🟢 **The record layer is the one tier of the education stack that is permissive at
the top of its own star ranking**, so a client deliverable can contain it outright. That inverts the
usual recommendation: don't fork the LMS, integrate with it over LTI and own the record layer.

🔴 **Regional reality, stated as measured:** five of the six rows are North American and the two EMEA
rows are one organisation. **No APAC or LATAM record-layer platform was found** on the channel used
(`Gap 502-E` names the channel and its blind spots — non-English naming and non-GitHub forges).

## 🆕 `p503` — `2026-10-28` — **two platform rows that have been in this base's history for months with no platform row, both read from bytes, and both copyleft — plus the interop claim this file has never checked against its source**

Reads: [`licence-bytes.2026-10-28-p503.tsv`](../evidence/licence-bytes.2026-10-28-p503.tsv),
[`promotion-audit.2026-10-28-p503.tsv`](../evidence/promotion-audit.2026-10-28-p503.tsv).
Narrative: [`agents/trending.md`](../agents/trending.md) `p503`.

### 🟡 Customisable platforms — copyleft, so the grant decides the engagement shape

| Layer | Platform | Licence @ pinned SHA | ★ | What it is | Region basis |
|---|---|---|---|---|---|
| 🟡 **Self-hosted language learning** | [`artcc/freelingo`](https://github.com/artcc/freelingo) | 🔴 **AGPL-3.0**, 34 514 B `269feb00c09a` (blob `128919466b58`, sha256₁₆ `ea94d5765c590b11`), 9 tokens from canonical | 210 | Full platform, not a component: CEFR study plans, an AI tutor, **voice conversations**, flashcards and spaced repetition, with **local or cloud** inference (`ollama` in its own topics), shipped as `docker-compose`. FastAPI + Next.js. | **EMEA** — CEFR is the Council of Europe's framework and the author's site is a Spanish-language personal domain |
| 🟡 **Assessment-item bank** | [`JudgePeach/math-question-bank`](https://github.com/JudgePeach/math-question-bank) | 🔴 **AGPL-3.0**, 34 523 B `135b78b0f22c` (blob `be3f7b28e564`, sha256₁₆ `0d96a4ff68ad6d4b`), 6 tokens from canonical | 358 | The layer every tutor on these shelves assumes and none supplies: a **question bank** with live LaTeX rendering, LLM parsing/solving and **formula OCR** for ingesting paper items. Localised to Chinese senior-secondary maths. | **APAC** — Chinese-language artefact, 高中 (senior secondary) curriculum scope |

🔴 **Both are AGPL-3.0, and for these two that is a deployment question, not a packaging question.**
A hosted deployment for a client triggers §13: the modified source must be offered to the users who
interact with it over the network. 🟢 **Shelf rule, same as `MoodleNet`/`Openki` above: viable where
the client accepts an AGPL estate or runs it internally; not viable as a component inside a
proprietary product.** For the freelingo shape specifically, the **local-inference** posture
(`ollama`) is what survives a ministry data-residency clause — see `T1`/`T13`.

🔵 **Why neither is in the permissive table:** this file's permissive tier is for platforms Globant
can fork into client IP. 🔴 Neither can be. They are here because the alternative — leaving a
210★ voice-capable tutor platform and the only OCR-capable item bank on these shelves **unrecorded**
— is the failure mode `Gap 502-C` named: *graded and unshelved*.

### 🔴 `OpenEduCat`'s interoperability claim — sourced, and marked as the vendor's own

This file's **Education ERP** row (line 34) and `p501`'s byte-read establish the licence
(**LGPL-3.0**). What has never been recorded is what the platform claims to *interoperate* with,
which is the question a client asks second:

| claim | as published by | status here |
|---|---|---|
| **LTI 1.3** tool support | `openeducat.org` solution pages | 🔴 **vendor-sourced, unverified** — no repository artefact read |
| **OneRoster** + **Ed-Fi** roster sync for SIS integration | `openeducat.org` | 🔴 vendor-sourced, unverified |
| **SCORM / xAPI** content support, Shibboleth SSO | `openeducat.org` | 🔴 vendor-sourced, unverified |
| Pricing | `openeducat.org` | 🔴 **internally inconsistent** — one comparison page lists *Free + $69–$1 119/yr*, a solutions page *Enterprise from $19 per staff user* |

🔵 **Recorded as claims, not capabilities**, and with the reason: a single-vendor domain supplied
**every** result for the query *"open source platform education LMS SIS ERP MIT Apache 2026
self-hosted"* — nine of nine results were `openeducat.org` pages in eight languages, the same
single-source pattern `p501` already flagged on this row. 🟢 **If an engagement depends on LTI 1.3
or OneRoster in OpenEduCat, the module must be read in the repository first** — this base has an
LTI corpus (`Cvmcosta/ltijs`, `1EdTech/lti-1-3-php-library`, `Harvard-University-iCommons/django-lti`)
to compare against. Registered as `Gap 503-F`.
