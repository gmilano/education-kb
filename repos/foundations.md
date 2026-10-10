---
industry: education
region: Global
updated: 2026-10-10
---

# Education — foundational repos

**Pass 108, 2026-10-10.** ⏱️ **Eighteenth pass of this date.**

🟢 **`census.sh` read **296 of 296** addresses, zero unread
(`compose/code/p108-release-identity/`, `test_p108.sh` 38 passed / 0 failed).** 🔵 **Every
foundation row below now carries a `class` and a pin, so "mature" is stated in refs
rather than in adjectives.**

### 🟢 🆕 p108 — foundations, with the ref you would actually pin

| repo | licence | `class` | pin | note |
|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | `semver` | 🟢 **`v5.3.0`** | the LMS incumbent; 590 tags, disciplined semver |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🟡 AGPL-3 | `semver` | 🟢 **`v5.14.2`** | AGPL — hosting implications, see `verticals/solutions.md` |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟡 AGPL-3 | `semver` | 🟢 **`v2.1.0`** | 451 tags; 🔴 **its `release-2021-…` tags are NOT releases** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | `semver` | 🟢 **`v0.19.5`** | 🟢 **MIT + offline-first — the permissive foundation of this shelf** |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | `semver` | 🟢 **`v3.5.3`** | 🟢 Apache-2.0, interactive-lesson engine |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🟡 LGPL-3 | `semver` | 🟢 **`v3.0.39`** | synchronous classroom |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🟡 GPL-3 | `semver` | 🟢 **`v3.0.1`** | strong LATAM + francophone install base |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 ECL-2.0 (Apache-derived) | `semver` | 🟢 **`25.2`** | 🟢 permissive; CalVer-style major |
| [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** | `semver` | 🟢 **`1.28.0`** | 🔴 **copyleft core** — interactive content, but see the MIT escape hatch below |
| [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) | 🟢 **MIT** | `semver` | 🟢 **`v3.8.2`** | 🟢 **plays H5P content with no LMS and no GPL server library** |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 | `prefixed` | 🟢 **`OpenOLAT_21.0.3`** | 🟢 **the most permissive full LMS on this shelf** |
| [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | `prefixed` | 🟢 **`dspace-10.1`** | repository/IR layer; 🔴 lexical sort reads this `7.6` |
| [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | 🟡 LGPL-3 | 🔴 `stamp` | 🔴 **SHA only** | LMS+SIS+fees on one DB; **1 tag, a pre-release** |

🟢 **Eleven of the thirteen are version-pinnable.** 🔴 **Licence re-read this pass from each
repo's own `LICENSE` over `raw.githubusercontent.com` rather than carried forward — and one
row moved: `h5p-php-library` is **GPL-3.0**, not MIT.**
🔴 **The AGPL pair (`canvas-lms`, `edx-platform`), the GPL trio (`moodle`, `chamilo`,
`h5p-php-library`) and LGPL `openeducat_erp` are usable but constrain what Globant can ship
on top.** 🟢 **The build-on-freely tier is `kolibri` (MIT), `h5p-standalone` (MIT), `oppia`
(Apache-2.0), `OpenOLAT` (Apache-2.0), `sakai` (ECL-2.0) and `dspace` (BSD-3).**
🔵 **This KB had already established H5P's core as GPL-3.0 further down this page; the
MIT-tier claim above it was a regression introduced earlier in this very pass and is
recorded rather than quietly amended.**

### 🔴 🆕 p108 — a correction to how this page has ranked maintenance

🔵 **`Gap 376` asked for a maintenance signal. p107 supplied tag count. This pass shows
tag count can inverse the answer.**

| repo | tags | tag count says | release identity says |
|---|---|---|---|
| `opetushallitus/valtionavustus` | **4 468** | 🟢 most industrial on the shelf | 🔴 **`stamp` — never cut a release** |
| `opetushallitus/oppijanumerorekisteri` | **4 225** | 🟢 industrial | 🔴 **`stamp` — never cut a release** |
| `opetushallitus/organisaatio` | 1 134 | 🟢 industrial | 🔴 **`stamp`** |
| `opetushallitus/ataru` | 726 | 🟢 industrial | 🔴 **`stamp`** |
| `learningequality/kolibri` | 16 | 🔴 nascent | 🟢 **`semver`, `v0.19.5`** |

🟢 **The Finnish National Agency for Education (`opetushallitus`) stack is real,
production, nationally deployed software and belongs on this shelf.** 🔴 **Its tags are
deploy stamps — `va-green-dev-2026-08-08T22_31_36+00_00`, `green-dev-1791293242` — so
there is no version to pin and `Gap 376` is NOT dischargeable by tag count.** 🔵 **The
maintenance question stays open; what closes this pass is the knowledge that the previous
answer was measuring the wrong thing.**

---


# Education — foundational repos

**Pass 107, 2026-10-10.** ⏱️ **Seventeenth pass of this date.**

🟢 **`Gap 376`'s corrective duty — owed since pass 92 and deferred for fourteen passes because the
instrument needed an API that returns 403 — is DISCHARGED IN PART this pass, by dropping the API
requirement entirely.** 🔵 **Instrument: `compose/code/p107-git-lane-census/`, `test_p107.sh`
**20 passed / 0 failed**, `census.sh` **299 of 299** addresses in 2 m 17 s with **zero unread**.**

### 🟢 🆕 p107 — the first COMPLETE denominator this shelf has had

🔴 **Every census in this KB since pass 92 has carried unread rows, and `P1040` rightly insists an
unread row is unread and never zero.** 🟢 **This one carries none: `rc=0` on all 299 addresses.**
🔵 **The reason is channel choice, not effort** — `git ls-remote` needs no credential, no API and no
clone, and the anonymous git lane serves every public repository.

🟢 **It validated before it was trusted. Three figures this KB had published from unrelated channels
were reproduced exactly:** `academico-sis/academico` **0** tags (p96 derived this from an npm
`"private": true` manifest), `pupilfirst/pupilfirst` **57**, `UniTime/unitime` **101**.
🔵 **A channel that reproduces known values can be believed on unknown ones.**

🟢 **Every row now carries a full 40-character HEAD sha, which closes `Gap 380` structurally** —
that gap exists because this shelf addresses payloads by abbreviated SHA and the abbreviation
sometimes 404s, reading exactly like *no licence payload*. 🔵 **Nothing need be abbreviated again.**

### 🔴 🆕 p107 — `pupilfirst`: pass 96's finding REFINED, and the sharper version is worse

🔵 **Pass 96 read `pupilfirst` as `COMPONENT-VERSIONED`: "57 tags **all scoped npm sub-packages**, so
the platform has never shipped as a unit".** 🟢 **The ref census confirms 57 and corrects the
"all".**

```
57 unique tags:  43 scoped @pupilfirst/* sub-packages
                 14 date-stamped platform releases  —  6 from 2023, 8 from 2024, NONE after
```

🟢 **So the platform *has* shipped as a unit, fourteen times. The ladder did not fail to exist — it
STOPPED, and the newest platform tag is `v2024.2.1efffc4`.** 🔴 **That is the more expensive fact:
"never released" invites you to build the release process; "released and then stopped two years ago"
tells you the maintainers left, and you inherit the whole thing.** 🔵 **`P985`'s three-way split
needs a fourth bucket: `ABANDONED-LADDER`.**

### 🔴 🆕 p107 — `P107-E`: this repository's address corpus holds **72 phantom rows**

🟢 **GitHub owner/repo is case-insensitive; this KB's address strings are not.** Across every `.md`,
`.tsv` and `.txt` here: **1 703 address strings resolving to 1 631 distinct repositories — 69
collisions, 72 phantom rows (~4 %).**

🟢 **Proved same-repo rather than same-name: all three collisions on the shelf return an IDENTICAL
HEAD sha** — `Apereo-…/OpenDashboard-legacy`, `Apereo-…/lap-sakai-extractor` (held under **three**
spellings) and `OpenEduCat/openeducat_erp`, each against its lowercased twin.

🟡 **It overturns no pass-106 finding** — the ECL tier is still ten repositories, because those ten
were named one at a time rather than counted. 🔴 **But pass 106's "1 381 addresses" and every corpus
denominator in this KB is inflated by roughly 4 %, so any *rate* computed against one is slightly
optimistic.** 🟢 **`Gap 401`; the remedy is one `tr A-Z a-z` before the `sort -u` that builds an
address list.**

### 🔴 🆕 p107 — tag counts cannot be taken at face value (`P107-C`)

🟢 **`git ls-remote --tags` emits an annotated tag TWICE — `refs/tags/X` and `refs/tags/X^{}`.**
🔴 **Shelf-wide: raw 112 457 vs unique 71 079, a +58 % overstatement across 120 of 299 rows.**
🔵 **And the ratio is not constant** — `instructure/canvas-lms` 68 051 → **34 029** and
`moodle/moodle` 1 181 → **591** are near-exactly 2×, but `openedx/edx-platform` 6 347 → **5 896** is
only 1.08×, because projects annotate different proportions of their tags. 🔴 **So no divisor
corrects it; the `^{}` lines must be filtered.** 🟢 **`P1046`'s family, found this time in the ref key.**

### 🟢 🆕 p107 — `T33` corroborated from a second direction: EMEA's public stack is **industrially** released

🔵 **Pass 106 found eight EUPL repositories from `opetushallitus` — the Finnish National Agency for
Education — and argued they were "not a side project". The ref census settles it.**

| repo | what it is | unique tags |
|---|---|---|
| [`opetushallitus/valtionavustus`](https://github.com/opetushallitus/valtionavustus) | state-aid administration | 🟢 **4 468** |
| [`opetushallitus/oppijanumerorekisteri`](https://github.com/opetushallitus/oppijanumerorekisteri) | national learner-number registry | 🟢 **4 225** |
| [`opetushallitus/organisaatio`](https://github.com/opetushallitus/organisaatio) | national organisation registry | 🟢 **1 134** |
| [`opetushallitus/ataru`](https://github.com/opetushallitus/ataru) | national admissions | 🟢 **726** |
| [`opetushallitus/koski`](https://github.com/opetushallitus/koski) | national study-rights registry | 🟢 **397** |
| [`opetushallitus/eperusteet`](https://github.com/opetushallitus/eperusteet) | national core curriculum | 🟢 **209** |

🟢 **Four of these outrank every North American asset on this shelf except `canvas-lms` and
`edx-platform`.** 🟡 **The tier remains adopt-and-contribute, because EUPL is copyleft with
reciprocity (`T33`)** — 🔵 **but this is a partner to integrate with, not a prototype to evaluate.**

**Pass 106, 2026-10-10.** ⏱️ **Sixteenth pass of this date** (104: 13:4x–14:xx UTC; 105:
14:4x–15:xx; this one 15:4x–16:xx).

🟢 **Forty rows gain a NAMED GRANT this pass, every one payload-read, and NOT ONE came from a
search** — 🔵 **35 named from their licence payload by the wired-in classifier and 5 from a package
manifest.** 🟡 **Precisely stated, because it is the stronger claim: these addresses were ALREADY
held by this KB. What was missing was a readable grant for them.** They came from auditing this
repository's own 1 381 addresses with the ECL remedy wired into the classifier — pass 105's lead #1.
🔴 **Thirteen further rows were named as NON-GRANTS, and one as a grant/restriction conflict.** 🔵 **Instrument: `compose/code/p1040-ecl-corpus-census/`,
`test_p1040.sh` 82 passed / 0 failed.** 🔴 **`api.github.com` = `http=403`, fourteenth consecutive
pass: a `—` in a ★ column is unread, never zero.**

### 🟢 🆕 p106 — the ECL tier is **10 repositories and SIX texts**, not six and four

🔵 **Pass 105 pinned four texts across six repositories and said the family was settled. It was
settled; the EXTENT was not.** 🟢 **The 99-address sample held 2 uncounted ECL rows; the corpus holds
10** — 🔵 **`P1047`: a blindness measured on a sample gives a FLOOR, never an estimate, because ECL
clusters in one consortium rather than spreading evenly.**

| repo | bytes | `sha256` (16) | text | new this pass |
|---|---|---|---|---|
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 11 120 | `0688f62d04f14e4b` | A | |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 11 340 | `76a975068930323e` | B | |
| [`Apereo-LAI/lap-sakai-extractor`](https://github.com/Apereo-Learning-Analytics-Initiative/lap-sakai-extractor) | 11 087 | `a9ea5cca8da2c8d5` | C | |
| 🆕 [`Apereo-LAI/OpenLRS`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS) | 11 087 | `a9ea5cca8da2c8d5` | **C — identical** | 🟢 **yes** |
| [`Apereo-LAI/LearningAnalyticsProcessor`](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | 9 919 | `fb10d1260ddc8dff` | D | |
| [`Apereo-LAI/OpenDashboard-api`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) | 9 919 | `fb10d1260ddc8dff` | D — identical | |
| [`Apereo-LAI/OpenDashboard-legacy`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy) | 9 919 | `fb10d1260ddc8dff` | D | |
| 🆕 [`Apereo-LAI/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | 9 878 | 🆕 `f339063d2f604ce9` | 🆕 **E** | 🟢 **yes** |
| 🆕 [`kuali/rice`](https://github.com/kuali/rice) | 11 182 | 🆕 `d4db8f22f8d564eb` | 🆕 **F** | 🟢 **yes** |
| 🆕 [`kualico/rice`](https://github.com/kualico/rice) | 11 182 | 🆕 `d4db8f22f8d564eb` | 🆕 **F — identical** | 🟢 **yes** |

🟢 **All ten are PERMISSIVE and buildable-on.** 🔵 **Two structural readings, both by `sha256` rather
than by impression (`P1025`):**

- 🟢 **The Apereo learning-analytics stack shares its grant across five repositories and three
  texts** — an LRS (`OpenLRS`), a learning-record warehouse (`OpenLRW`), a processor and two
  dashboards. 🔵 **A complete, permissively-granted analytics pipeline for higher education, and
  until this pass every row of it was `UNRECOGNISED`.**
- 🟢 **`kuali/rice` and `kualico/rice` carry ONE byte-identical text at two organisation names** —
  🔵 **`P1012` again: an incumbent's code lives under its predecessor organisation's name, and
  probing one name only would have published a dead row or missed a live one.**

### 🟢 🆕 p106 — **Finland's national education stack: eight repositories, all EUPL** (`T33`)

🔴 **The licence family that had NO branch in this KB's classifier at all.** 🔵 **It is named by
REFERENCE in 296–654 B, never as a licence body (`P742`), which is why eight substantial
repositories presented as grant-less:**

| repo | EUPL | what it is | ★ |
|---|---|---|---|
| [`opetushallitus/koski`](https://github.com/opetushallitus/koski) | **1.1** | 🔵 the **national study-rights and completed-studies registry** | — |
| [`opetushallitus/eperusteet`](https://github.com/opetushallitus/eperusteet) | 1.1 | 🔵 the **national core-curriculum service** | — |
| [`opetushallitus/ataru`](https://github.com/opetushallitus/ataru) | **1.2** | national application and admissions | — |
| [`opetushallitus/ehoks`](https://github.com/opetushallitus/ehoks) | 1.1 | personal competence-development plans | — |
| [`opetushallitus/oppijanumerorekisteri`](https://github.com/opetushallitus/oppijanumerorekisteri) | 1.1 | the national learner-number registry | — |
| [`opetushallitus/organisaatio`](https://github.com/opetushallitus/organisaatio) | 1.1 | education-provider organisation registry | — |
| [`opetushallitus/suorituspalvelu`](https://github.com/opetushallitus/suorituspalvelu) | **1.2** | the attainment service | — |
| [`opetushallitus/valtionavustus`](https://github.com/opetushallitus/valtionavustus) | 1.1 | state-aid administration | — |

🟢 **Placed EMEA by `P1035`'s rule, with the placing string published:** ccTLD `eduuni.fi` on
`koski`, and the holder line *"Copyright (c) 2025 Finnish National Agency for Education"* plus the
nationally unique system name `Opetushallitus` on `ataru`. 🔵 **Not by the organisation name, which
`P1035` forbids.**

🟡 **What is NOT yet measured, and is pre-registered as next pass's lead #3: whether these cut
RELEASES.** 🔵 **`T29`/`T30` made the adopt-or-build line turn on release engineering, and that test
has never been applied to a EUPL row.**

### 🟢 🆕 p106 — five rows whose grant is **not in the `LICENSE` file**

🔴 **Their `LICENSE` is 45–108 B holding only `YEAR:` and `COPYRIGHT HOLDER:`.** 🔵 **That is not a
truncated licence — it is the R convention: `DESCRIPTION` declares the grant and `LICENSE` supplies
the two fields the template needs filled in.** 🟢 **A root-`LICENSE`-only census misreads every R
package in the corpus, and misreads them as UNRECOGNISED rather than as missing** (`p283`/`p289`'s
manifest-named licence, measured for R):

| repo | `LICENSE` bytes | `DESCRIPTION` declares |
|---|---|---|
| 🆕 [`rstudio/ggcheck`](https://github.com/rstudio/ggcheck) | 45 | 🟢 **`MIT + file LICENSE`** |
| 🆕 [`rstudio/tblcheck`](https://github.com/rstudio/tblcheck) | 46 | 🟢 **`MIT + file LICENSE`** |
| 🆕 [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna) | 46 | 🟢 **`MIT + file LICENSE`** |
| 🆕 [`sidneybissoli/educabr`](https://github.com/sidneybissoli/educabr) | 61 | 🟢 **`MIT + file LICENSE`** |
| 🆕 [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | 108 | 🟢 **`BSD_3_clause + file LICENSE`** |

🔵 **`ottr` is why the manifest is READ and not assumed: four of five are MIT and a guess would have
made it five.** 🟡 **A declared string is the publisher's CLAIM, not a payload this KB has read; the
two are kept in separate columns and `p963`'s gate is what would reconcile them.**

### 🟢 🆕 p106 — one row RE-VERIFIED across passes, one widely-cited row REFUTED

- 🟢 **[`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) — Apache-2.0, payload read at
  **10 982 B**.** 🔵 **NOT a new row: this KB already records it at that exact byte count
  (`repos/trending.md`). 🟢 **The value is the agreement — an independent instrument, a different
  probe path (`HEAD` ref, no `ls-remote`), the same 10 982 B.** 🟡 **And the open question the
  earlier record left stands: 10 982 B is NOT the pristine 11 358 B, so the text is trimmed or
  augmented, and `P1030` says read that difference before leaning on the row.**
- 🔴 🆕 **[`frappe/education`](https://github.com/frappe/education) and
  [`frappe/lms`](https://github.com/frappe/lms) are `LIVE-NOGRANT`** — no licence payload at eleven
  filenames, with a clean 200 control on each. 🔵 **A secondary source this pass presented the Frappe
  education stack as an open-source option; measured, it ships no grant at its root.** 🟡 **`frappe/lms`
  has been named on this KB's pages as shelved; this is the first pass to read its root for a grant
  and the answer is that there is not one.**

**Pass 104, 2026-10-10.** ⏱️ **Fourteenth pass of this date** (91: 2026-10-09 23:0x–00:00 UTC; 92:
00:4x–01:3x; 93: 01:4x–02:24; 94: 02:5x; 95: 03:4x; 96: 04:4x–05:xx; 97: 05:4x–06:xx; 98:
06:4x–07:xx; 99: 07:4x–08:xx; 100: 08:4x–09:xx; 101: 09:4x–10:xx; 102: 10:4x–11:xx; this one
12:4x–13:xx).

🟢 **Seven rows added this pass, all payload-read, and NONE from a search** — they came from a census
of this repository's own `archive/2026-10-06-pre-reset/` snapshot against every live file
(`Gap 394`). 🔴 **82 of 681 archived addresses are held nowhere outside the archive; 103 are on no
page.** 🔵 **Instrument written AND executed this pass: `compose/code/p1026-archive-regression-census/`
— `test_census.sh` 9 passed / 0 failed, `census.sh . ./archive` → `681 / 1 419 / 88`.**

🟢 **The instrument ran offline for the first time since pass 92: `test_ladder.sh` — 16 passed, 0
failed; `--reach` — `names=24 byte-floor=1B classifier=lib/license_family.sh`.** 🔴 **Its network path
was refused, so the 133-row census was NOT re-derived.** 🔵 **`Gap 376` therefore SPLITS: the
classifier and the reach are verified by execution; only the network path is denied.** 🟢 **No
classifier was written** (`P237`).

🔴 **`api.github.com` = `http=403` for every repository not attached to this session — measured, with
the proxy's message, not assumed.** A `—` is unread, never zero.

### 🟢 🆕 p105 ECL-2.0 pinned by `sha256` — **six repositories, four texts** — and the classifier's limit turns out to be a COST

🔵 **Pass 104 left this page with an explicit open question: "it's ECL" is not yet a measurement of
WHICH ECL text.** 🟢 **Answered. Every payload read, every one pinned:**

| repo | bytes | `sha256` (16) | text |
|---|---|---|---|
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 11 120 | `0688f62d04f14e4b` | **A** — titles itself *"Educational Community License, Version 2.0 (ECL-2.0)"*, cites `opensource.org` |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 11 340 | `76a975068930323e` | **B** |
| [`Apereo-LAI/lap-sakai-extractor`](https://github.com/Apereo-Learning-Analytics-Initiative/lap-sakai-extractor) | 11 087 | `a9ea5cca8da2c8d5` | **C** |
| [`Apereo-LAI/LearningAnalyticsProcessor`](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | 9 919 | `fb10d1260ddc8dff` | 🟢 **D** |
| [`Apereo-LAI/OpenDashboard-api`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) | 9 919 | `fb10d1260ddc8dff` | 🟢 **D — identical** |
| [`Apereo-LAI/OpenDashboard-legacy`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy) | 9 919 | `fb10d1260ddc8dff` | 🟢 **D — identical** |

🟢 **Six repositories, FOUR distinct texts, and all six declare *Version 2.0, April 2007*.**
🔵 **Payload D is one text shared by three repositories — which is precisely the fact a byte count
alone could not establish, and `P1025` exists to force.** 🟡 **Pass 104 read the 9 919 B row as
"1 168 B shorter than its sibling"; it is better described as the lineage's OWN canonical text,
carried unchanged by three repositories, while Sakai and Opencast each carry a longer variant.**

#### 🔴 And the correction this page owes: the classifier's limit is **not** harmless

🔵 **Pass 104 called `UNRECOGNISED` "the instrument's declared limit, not a defect — the honest
output is never a guess."** 🟢 **The honesty holds. The harmlessness does not.**

🔴 **Measured cause, from the text rather than the pattern: the ECL-2.0 payload contains ZERO
occurrences of the string `Apache License`.** It names the *"Apache 2.0 license"* in lower case.
🔵 **So the classifier never mislabels ECL as Apache — it fails to see it, and a row that is
PERMISSIVE then lands in neither the permissive nor the copyleft bucket.**

| | pass 104 | 🟢 **corrected p105** |
|---|---|---|
| permissive | 38 | 🟢 **40** |
| copyleft | 22 | 22 |
| CC family | 5 | 5 |
| 🔴 payload that is not a grant | 1 | 1 |
| total granted | 68 | 🟢 **68 — it reconciles** |

🟢 **`lap-sakai-extractor` and `OpenDashboard-legacy` are permissive supply that two passes of
census did not count.** 🔵 **`P1036`: an invisible family is worse than a mislabelled one, because
the footing stays right while the composition drifts.** 🔵 **`P1037`: the bucket NAME —
*"permissive (MIT / Apache-2.0 / BSD)"* — could not have counted ECL even with a perfect classifier,
so buckets are now named by the PROPERTY, not by an enumeration of members.**

🟢 **Remedy written this pass as `classify_ecl` in
`compose/code/p1035-regrant-holder-ecl/ecl.sh`** — ECL-2.0 is the Apache-2.0 text with section 3's
patent grant narrowed to education: **permissive, and buildable on.** 🔴 **It is NOT yet wired into
the census instrument, and the corpus is 1 400+ addresses of which only 99 have been audited for
this. That is `Gap 398`, and it is the first lead pre-registered for the next pass.**

### 🟢 🆕 p104 Tier 1d — the **runtime and interop spine** this KB owned and never shelved

🔵 **`p1026`'s census found that `ollama/ollama` — the local-inference runtime — was on no page of
this knowledge base, held only inside an instrument's input worklist.** 🟢 **Probed and shelved
here, with eleven others, every grant a payload read at the measured ref (`P1005`).**

| repo | grant · bytes | ref · tags | region | why it is foundational |
|---|---|---|---|---|
| [`ollama/ollama`](https://github.com/ollama/ollama) | 🟢 **MIT** · 1 058 B | `main` · 🟢 **689** | 🟢 **North America** | 🔵 **The local-inference runtime.** The whole EMEA/LATAM sovereign story depends on a permissive one, and this KB had it on no page |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 **MIT** · 1 152 B | `main` · 🟢 **573** | 🟢 **North America** | Durable orchestration — the retry/compensation layer every multi-pass grading workflow needs |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 **Apache-2.0** · 11 418 B 🟡 *(+60 B over pristine)* | `main` · 🟢 **291** | 🟡 **EMEA / North America** | Model loading and fine-tuning substrate |
| [`fwu-de/fwu-kc-extensions`](https://github.com/fwu-de/fwu-kc-extensions) | 🟢 **Apache-2.0** · 11 357 B | `main` · 🟢 **118** | 🟢 **EMEA** (Germany, FWU) | 🔵 **Keycloak extensions for school identity** — see the `Gap 395` correction below |
| [`libretexts/shapeshift`](https://github.com/libretexts/shapeshift) | 🟢 **MIT** · `LICENSE.md` 1 067 B | `main` · 🟢 **45** | 🟢 **North America** (LibreTexts, UC Davis) | OER content transformation at the largest US open-textbook programme |
| [`libretexts/davis`](https://github.com/libretexts/davis) | 🟢 **MIT** · 1 073 B | `main` · 🟢 **32** | 🟢 **North America** (LibreTexts) | Second released LibreTexts component |
| [`nextcloud/llm2`](https://github.com/nextcloud/llm2) | 🟢 **MIT** · 1 069 B | `main` · 🟢 **32** | 🟢 **EMEA** (Germany) | 🔵 **Local LLM backend — and the holder is `cloud-py-api`, not Nextcloud.** See `P1031` |
| [`nextcloud/translate2`](https://github.com/nextcloud/translate2) | 🟢 **MIT** · 1 069 B | `main` · 🟢 **12** | 🟢 **EMEA** (Germany) | On-premises translation — the multilingual-classroom primitive |
| [`nextcloud/text2image_stablediffusion2`](https://github.com/nextcloud/text2image_stablediffusion2) | 🟢 **MIT** · 1 098 B | `main` · 🟢 **12** | 🟢 **EMEA** (Germany) | On-premises image generation for courseware |
| [`csr2017/edfi-oneroster`](https://github.com/csr2017/edfi-oneroster) | 🟢 **Apache-2.0** · 10 173 B | `main` · 🟢 **8** | 🟢 **North America** | 🔵 **An Ed-Fi ↔ OneRoster bridge.** The two US rostering standards, joined, permissively |
| [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 **BSD-3-Clause** · 1 504 B | `main` · 🟢 **136** | 🟢 **North America** (LYRASIS) | Institutional repository — re-confirmed byte-exact this pass |
| [`apereo-learning-analytics-initiative/larissa`](https://github.com/apereo-learning-analytics-initiative/larissa) | 🟢 **Apache-2.0** · 🟢 **11 358 B — byte-exact pristine** | `master` · 0 | 🟢 **North America** (Apereo) | Learning-analytics service. 🔴 **No releases** |

### 🔵 🆕 p104 `P1024` gets the reference it was missing — pristine Apache-2.0 is **11 358 B**, not 11 357

🔴 **This KB has compared Apache-2.0 payloads against 11 357 B as "pristine" for several passes. The
canonical text published by the ASF is 11 358 B.** 🟢 **Fetched from the publisher and pinned:**

```
cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30   11 358 B
apache.org/licenses/LICENSE-2.0.txt, fetched 2026-10-10
```

🟢 **`apereo-learning-analytics-initiative/larissa` is byte-identical AND `sha256`-identical to it.**
🔵 **So `P1024` now compares against a `sha256`, which is what `P1025` demanded and a byte count
cannot give.** 🟡 **Consequence for rows this KB already carries: `moonshot-cicd`,
`fwu-kc-extensions` and `attention-monitor` at 11 357 B are pristine **minus a trailing newline** —
a different fact from "pristine", and the difference is now checkable.** 🔴 **`moonshot-ui` at
11 347 B and `csr2017/edfi-oneroster` at 10 173 B are genuinely short: the Ed-Fi family's 10 173 B
is `P1024`'s omitted appendix, confirmed a third time.**

### 🟢 🆕 p104 `Gap 395` CORRECTED — EMEA's institutional supply is LAYER-SPLIT, not grant-less

🔴 **Pass 103 opened `Gap 395` on the reading that EMEA public-sector publishers ship releases and no
grant**, from two rows: the European Commission's `european-digital-credentials` (no payload,
7 names, `2.0.6`) and `fwu-de/schulfach-ontologie` (no payload, `1.0.0`).

🔴 **This pass probed the same publisher's third repository. `fwu-de/fwu-kc-extensions` is
Apache-2.0 with 118 tags.** 🟢 **The same German public-sector body that ships ungranted ontologies
ships a granted, heavily-released identity component.**

| `fwu-de` (Germany, public-sector) | grant | tags | layer |
|---|---|---|---|
| [`fwu-de/fwu-kc-extensions`](https://github.com/fwu-de/fwu-kc-extensions) | 🟢 **Apache-2.0** · 11 357 B | 🟢 **118** | 🟢 **identity / SSO — CODE** |
| [`fwu-de/schulfach-ontologie`](https://github.com/fwu-de/schulfach-ontologie) | 🔴 **none** (p103) | 1 | 🔴 **vocabulary / DATA** |
| [`fwu-de/schulart-ontologie`](https://github.com/fwu-de/schulart-ontologie) | 🔴 **none** · clean 200-control 1 117 B | 2 | 🔴 **vocabulary / DATA** |
| [`dini-ag-kim/school-curriculum-pg`](https://github.com/dini-ag-kim/school-curriculum-pg) | 🔴 **none** · clean 200-control 136 B | 0 | 🔴 **curriculum vocabulary / DATA** |

🔵 **`Gap 395` is therefore not "EMEA does not grant". It is: 🟢 **EMEA public-sector CODE is
granted and released** · 🔴 **EMEA public-sector VOCABULARY is ungranted, 3 of 3 German rows.**
🔵 **Commercial consequence, and it is sharper than the original gap: an EMEA engagement can BUILD
on the identity layer today, and the written grant request goes to the bodies publishing the
CURRICULUM AND SUBJECT ONTOLOGIES — the data a personalisation engine has to key on.**

### 🔵 🆕 p104 `P1031` — inside one org name, the grant tracks the HOLDER, not the org

🔴 **The `nextcloud` org carries both licences, and the split is not arbitrary.**

| `nextcloud/*` row | grant · bytes | holder line | tags |
|---|---|---|---|
| `llm2` | 🟢 **MIT** · 1 069 B | 🔴 **`cloud-py-api`** | 32 |
| `translate2` | 🟢 **MIT** · 1 069 B | 🔴 **`cloud-py-api`** | 12 |
| `text2image_stablediffusion2` | 🟢 **MIT** · 1 098 B | 🔴 **`cloud-py-api`** | 12 |
| `integration_openai` | 🔴 **AGPL-3.0** · `COPYING` 34 519 B | FSF text only, no project holder | 58 |
| `context_chat_backend` | 🔴 **AGPL-3.0** · 34 520 B | FSF text only, no project holder | 53 |

🟢 **The MIT rows are the MODEL-SERVING backends and are held by an upstream project adopted into
the org. The AGPL rows are the INTEGRATION layer and are the org's own.** 🔵 **`P1012` said an
incumbent's code can live under a predecessor's org name; `P1031` is the same mechanism measured in
the permissive direction.** 🔴 **Commercial consequence for an EMEA sovereign build: the model
runners can be embedded, the integration layer imposes network copyleft, and reading the ORG name
gets this backwards in both directions.**

### 🔵 🆕 p104 ECL-2.0's payload is NOT stable across Apereo's own repositories

🔵 **This page already carries ECL-2.0 — the Educational Community License, Apache-2.0 with the
patent grant narrowed to education communities, and the only OSI-approved licence written FOR this
industry.** 🔴 **Four Apereo-lineage payloads, four distinct byte counts:**

| repo | ECL-2.0 payload | note |
|---|---|---|
| [`opencast/opencast`](https://github.com/opencast/opencast) | 11 340 B | carried |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 11 120 B | carried |
| [`apereo-learning-analytics-initiative/lap-sakai-extractor`](https://github.com/apereo-learning-analytics-initiative/lap-sakai-extractor) | 🆕 **11 087 B** · `master` · 0 tags | 🟢 declares *"[OSI Approved License]"* in line 2 |
| [`apereo-learning-analytics-initiative/opendashboard-legacy`](https://github.com/apereo-learning-analytics-initiative/opendashboard-legacy) | 🆕 🔴 **9 919 B** · `master` · 3 tags | 🔴 **1 168 B shorter than its sibling** — cites `osedu.org/licenses/` |

🔴 **Both classified `UNRECOGNISED` by pattern and were resolved by READING them.** 🔵 **That is the
instrument's declared limit, not a defect: a pattern set tuned to the nine common families will not
recognise an education-specific licence, and the honest output is "unrecognised", never a guess.**
🟡 **For `P1025`: four sizes means ECL payloads must be pinned by `sha256` like every other family,
and "it's ECL" is not yet a measurement of WHICH ECL text.**

### 🟢 🆕 p103 Tier 1c — the **student-data spine**, permissive and release-engineered, and it refutes `T26` for one layer

🔵 **`T26` (pass 102) concluded that the permissive supply in the administrative layer is GENERIC and
the education-specific supply is COPYLEFT, so a permissive SIS is a CONSTRUCTION rather than an
ADOPTION.** 🔴 **That is now refuted for the rostering / student-data layer, by a repository this KB
has held in an instrument worklist since the reset.**

| repo | grant (payload · bytes · `sha256`) | ref · SHA | tags / top | region | what it buys |
|---|---|---|---|---|---|
| 🆕 p103 [`ed-fi-alliance-oss/Ed-Fi-ODS`](https://github.com/ed-fi-alliance-oss/Ed-Fi-ODS) | 🟢 **Apache-2.0** · `LICENSE.txt` **10 172 B** · `59899c60…` | `main` · `e453cd2cad8a0653c65453948d3d235aec7c517c` | 🟢 **42 / `v7.3.2-pre`** | 🟢 **North America** (Ed-Fi Alliance) | 🟢 **The Operational Data Store + API — the student-data spine US K-12 districts actually run**, education-specific, permissive, and released on a maintained line. 🔵 **This is the row `T26` said did not exist.** |
| 🆕 p103 [`ed-fi-alliance-oss/Ed-Fi-Data-Standard`](https://github.com/ed-fi-alliance-oss/Ed-Fi-Data-Standard) | 🟢 **Apache-2.0** · **10 173 B** · `a6cba85b…` | 🔴 **`v6.2.0`** · `3d24df6` | 🟢 **21** | 🟢 **North America** | The domain model on its own, separable from the server — 🔵 **the cheap half when a client already has a warehouse and needs the SCHEMA, not another database.** |
| 🆕 p103 [`project-sunbird/sunbird-lms-service`](https://github.com/project-sunbird/sunbird-lms-service) | 🟢 **MIT** · 1 072 B · `7dde0671…` · © 2018 **Project Sunbird** | `master` · `48c79a8` | 🟢 **450** | 🟢 **APAC** (India) | 🟢 **The learning-management service of the stack behind India's national digital-education infrastructure — 450 releases.** 🔵 **The most release-engineered permissive education backend on this page.** |
| 🆕 p103 [`project-sunbird/knowledge-platform`](https://github.com/project-sunbird/knowledge-platform) | 🟢 **MIT** · 1 072 B · `fd3adcd5…` · © 2019 | `master` · `adca974` | 🟢 **336** | 🟢 **APAC** (India) | Content, taxonomy and framework services — 🔵 **curriculum as queryable platform data, the same purchase as `bncc-pacotes` (p93) two orders of magnitude larger.** |
| 🆕 p103 [`project-sunbird/sunbird-devops`](https://github.com/project-sunbird/sunbird-devops) | 🟢 **MIT** · 1 072 B · `7dde0671…` | `master` · `b5797a4039a45c8f2c813ef343529b8a4212a009` | 🟢 **702** | 🟢 **APAC** (India) | 🟡 Deployment — the limb that makes the other two adoptable rather than readable. |
| 🆕 p103 [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 **BSD-3-Clause** · 1 504 B · © 2002–2021 **LYRASIS** | `main` · `a5b0f0fc17ad5c7f8917eb89b9222f2c2d441aed` | 🟢 **136** | 🟢 **North America** (LYRASIS) | Institutional repository — the layer a university's outputs land in. 🔴 **Tag ordering is unsafe: a naive `sort` ranks `language-pack-1_4_1` last**, the same hazard `P978` recorded for OpenOLAT's two tag spellings. |
| 🆕 p103 [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 **Apache-2.0 + a bundled-grant block INSIDE the `LICENSE`** · **13 185 B** | 🔴 **`develop`** · `0a66b52` | 🟢 **28** | 🟢 **North America** (1EdTech) | Open Badges validation. 🔵 **`P1024` was found in this payload.** 🔴 **And it is now the ONLY surviving limb of the credentialing stack — see `Gap 396`.** |

🔵 **How these rows reached this page matters as much as the rows.** 🔴 **None of them came from a
search.** 🟢 **All seven came from censusing `archive/2026-10-06-pre-reset/` against every live file
(`Gap 394`, `P1026`), which found **82 of 681** archived addresses held nowhere else in the
repository and **103** on no page.** 🔵 **`P1004` for the fourth pass running: when the instrument
channel is restricted, the question whose corpus is this repository is the one that pays.**

### 🔵 🆕 p103 `P1024` — read the payload's SIZE against its family's pristine size, in both directions

🔴 **`P1013` (p101) says a root Apache-2.0 does not describe the shipped artifact, so read the
`NOTICE`.** 🟢 **This pass found a `NOTICE`'s content inside a file called `LICENSE`.**

| payload | bytes | vs pristine Apache-2.0 (11 357 B) | what the difference IS |
|---|---|---|---|
| `1EdTech/openbadges-validator-core` `LICENSE` | **13 185 B** | 🔴 **+1 828 B** | 🔴 **a bundled-subcomponent block**: *"The BasicLTI Utilities (basiclti-util) distribution includes a number of subcomponents with separate copyright notices and license terms"* — **OAuth** (© 1998–2009 AOL LLC; © 2007, 2008 Google, Inc.; © 2007, 2008 Netflix, Inc.) and **Base64** (© 1999–2008 The Apache Software Foundation). 🟢 **Both Apache-2.0, so the closure is clean.** |
| `ed-fi-alliance-oss/Ed-Fi-ODS` `LICENSE.txt` | **10 172 B** | 🟡 **−1 185 B** | 🟢 **the appendix is omitted** — the terms end at *"END OF TERMS AND CONDITIONS"*, with no *"APPENDIX: How to apply the Apache License to your work"*. **A complete grant; a shortened file.** |
| `aiverify-foundation/moonshot` `LICENSE.md` | **11 347 B** | 🟡 **−10 B** | 🟡 Markdown-ised whitespace. 🔵 **Ten bytes is not a finding; 1 828 is.** |

🔵 **The rule: a byte count below pristine means text was REMOVED — usually boilerplate, usually
harmless. A byte count ABOVE pristine means text was ADDED, and what gets added to a licence file is
almost always somebody else's grant.** 🔴 **Six passes of this page treated a non-pristine size as
noise in the `pristine` annotation. It is a POINTER.**

### 🔵 🆕 p103 `P1025` — equal byte count is not identity; pin a grant by `sha256`

🔴 **Three Sunbird payloads are all `1 072 B` MIT and are not all the same file.**

| repo | bytes | `sha256` (first 16) | copyright line |
|---|---|---|---|
| `project-sunbird/sunbird-devops` | 1 072 | `7dde06716f259584` | © **2018** Project Sunbird |
| `project-sunbird/sunbird-lms-service` | 1 072 | `7dde06716f259584` | © **2018** Project Sunbird |
| `project-sunbird/knowledge-platform` | 1 072 | 🔴 **`fd3adcd576767d65`** | © **2019** Project Sunbird |

🟢 **Same holder, same length, different file.** 🔴 **`P386`'s pristine-dedup gate deduplicates by
SIZE, and this is the counter-case from the other side: two files of identical length that are not
the same payload.** 🔵 **The year is harmless here — but a size-based dedup cannot know that, and the
next collision may not be a year.** 🟢 **`curl … | sha256sum` is one command; use it.**

### 🟢 🆕 p102 Tier 4 — the PERMISSIVE administrative core, promoted after living only in this KB's append-only history

🔵 **This page has said for several passes that the education ERP / SIS layer is copyleft: OpenEduCat
is LGPL-3.0, ERPNext is GPL, Dolibarr is GPL-3.0.** 🔴 **That is true of the EDUCATION-SPECIFIC
layer and this page generalised it one step too far.** 🟢 **Two Apache-2.0 general ERP cores have sat
in `repos/trending.md` and `intel/open-gaps.md` for passes and were never shelved, never addressed and
never costed** — exactly `Gap 384`'s shape, discharged here for one tier.

| slug | grant (payload · bytes) | ref · **full SHA** | tags / latest | bundled-grant read (`P1013`) |
|---|---|---|---|---|
| 🆕 p102 [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** · `LICENSE` **11 906 B** | 🔴 **`trunk`** · `45506b377c855e455942b238dbd55e33fce79d4f` | 🟢 **26 / `release24.09.07`** | 🟢 **CLEAN** — `NOTICE` **166 B**; the appended section declares only **Noto Sans (Apache-2.0)** and **timezone files (Public Domain)** |
| 🆕 p102 [`cortezaproject/corteza`](https://github.com/cortezaproject/corteza) | 🟢 **Apache-2.0** · `LICENSE` **11 358 B** *(pristine)* | 🔴 **`2024.9.x`** · `3835dfc4ac8bd89381753f09042ad147a4502576` | 🟢 **298 / `2026.9.0-rc.2`** | 🟡 **nothing to read** — `NOTICE` **404** |

🟢 **`apache/ofbiz-framework` is the first row on this shelf whose `P1013` bundled-grant check comes
back fully CLEAN.** 🔵 **That matters because pass 101 established the opposite case in the same
industry**: `Jasig/SSP`'s root Apache-2.0 sits over **Ext JS (GPL-3.0)**, **JasperReports / JFreeChart
/ c3p0 (LGPL)** and **iText (MPL)**. 🟢 **OFBiz bundles a font and a timezone table. Permissive all
the way down, `Copyright 2001-2026 The Apache Software Foundation`** — so the ASF is still shipping it.

### 🔴 🆕 p102 `P1020` — the default ref is a MEASUREMENT, and this pass found the archived citation was unreachable

🔴 **`refs/heads/master` does NOT EXIST in `apache/ofbiz-framework`.** Measured:
`git ls-remote --heads <repo> master` returns **empty**; HEAD symrefs to **`refs/heads/trunk`**.
🔴 **And this KB's own history row cited the grant as `LICENSE@master`** — an address that 404s on a
repository that is, in fact, cleanly Apache-2.0 with 26 releases.

🔵 **`P1020`: read the default ref before reading the licence. A `main`/`master`-assuming probe does
not return "no licence" — it returns a FALSE NEGATIVE, and this KB has now published one.**

| pass | repository | default ref found | what an assuming probe would have done |
|---|---|---|---|
| 101 | `douglasrizzo/catsim` | 🔴 **`dev`** | 404 every one of 24 names |
| **102** | `apache/ofbiz-framework` | 🔴 **`trunk`** | 🔴 **it DID — the archived row's `@master` citation is unreachable** |
| **102** | `cortezaproject/corteza` | 🔴 **`2024.9.x`** | 404 every one of 24 names |

🟢 **Three non-standard defaults in two passes, across a research tool, an ASF project and a vendor
platform.** 🔵 **This is not a long tail; it is a third of the rows this KB touched in two passes.**

### 🔴 🆕 p102 `P1021` — a default ref is not the newest release line

🔴 **`cortezaproject/corteza` symrefs HEAD to `2024.9.x` while its tags run to `2026.9.0-rc.2`.**
🔵 **So the branch a clone lands on is two release years behind the project's own tip**, and a
currency judgement taken from HEAD alone would have called a live project stale.
🟢 **`P1021`: date a repository from its TAGS, and pin the ref separately.** 🟡 **Its tip is a
release candidate (`-rc.2`, `-dev.2`), so the newest line is not GA either — recorded, not used.**

### 🟢 🆕 p101 Tier 2c re-measured — two carried rows moved, and one of them has a default branch this page never recorded

🔵 **`P1010` says re-measure a tier's existing rows before describing the tier. Applied to Tier 2c:**

| repo | grant (payload · bytes · ref · SHA-40) | tags | what moved |
|---|---|---|---|
| 🆕 p101 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** · 1 066 B · `main` · `4751688e3a10156248d82c4ef80714c5b210dd68` | 🟢 **5** (first count) | 🔴 **DRIFTED** off this page's pinned `77c3e90`. 🟢 **Grant KEPT, byte-identical.** |
| 🆕 p101 [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** · 1 514 B · **`dev`** · `7e6caae84a8e7779422ba9338cfe2e2335185b28` | 🟢 **38** (first count) | 🔴 **Its default ref is `dev`** — not `master`, not `main`. |

🔴 **`P1015`: probe the default ref, never a guessed one.** 🔵 **A `main`-assuming probe of `catsim`
404s all 24 filenames and publishes `NO-LICENCE-PAYLOAD` for a cleanly BSD-3 repository** — the same
false-negative mechanism as `Gap 380`, from a different cause. 🟢 **`ladder.sh` already does this
correctly** (`git ls-remote --symref` first), which is one more reason the census owes its re-derivation.

### 🟢 🆕 p101 Tier 2h — the student-success DOMAIN MODEL, and the `NOTICE` oracle

🟢 **[`Jasig/SSP`](https://github.com/Jasig/SSP) — Apache-2.0, `LICENSE` 11 359 B, `master` ·
`711244dc0d6d5c65fd261c9bec77dd48b4dbaaf6`, 57 tags (`ssp-2.9.0`), `pom.xml`
`org.jasig.ssp:ssp:2.9-SNAPSHOT`.** The Apereo **Student Success Plan**: early alert, caseload, and
intervention tracking. 🔴 **It discharges `Gap 385`, and it was invisible because it lives under
Apereo's PREDECESSOR org name** (`P1012` — `apereo/SSP`, `apereo/OpenLRW`, `apereo/openlrs` and
`apereo/opencast` all return **ABSENT**).

🔴 **`P1013` — and this is a new ORACLE for this page, not only a warning.** The root grant is
Apache-2.0; the shipped artifact is not all permissive, and **the repository says so itself** in
`NOTICE`: **Ext JS GPL-3.0** (Sencha FLOSS exception), **JasperReports / JFreeChart / Hibernate Commons
Annotations / c3p0 LGPL**, **iText MPL**, alongside a long permissive majority (Spring, Lucene, Jackson,
Guava, Liquibase, Quartz — Apache-2.0; jQuery, Knockout, Underscore, Mockito, SLF4J — MIT; ASM, dom4j,
PostgreSQL JDBC — BSD).

🔵 **Where this sits against `Gap 370`.** `Gap 370` is a per-DIRECTORY licence the root cannot see and
for which this page has **no instrument**. 🟢 **This is the per-DEPENDENCY case, and it DOES have one —
`NOTICE`, in the 24-name reach already** (it is the 24th name). 🔴 **The ladder reads `NOTICE` only as a
licence candidate, first-match, so a repo with a real `LICENSE` never gets its `NOTICE` read.**
🔵 **`P1016`: on a JVM or bundled-asset repository, read `NOTICE` IN ADDITION to the grant — it is a
bundled-licence manifest, not a second licence.** 🟢 **`ladder.sh --all` already fetches every name;
what it lacks is the distinction between *a grant* and *a manifest*. That is a one-line reporting change
to the instrument, not a classifier change** — so it does not touch `P237`.

### 🟢 🆕 p101 Tier 3b — the AI-literacy curriculum tier gains a release-engineered row

| repo | grant (payload · bytes · ref · SHA-40) | tags | ★ | note |
|---|---|---|---|---|
| 🆕 p101 [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) | 🟢 **MIT** · 1 070 B · `main` · `a5b10f4ce4ded798e3e1b42d0d74dcd73904ef67` (© 2026) | 🟢 **6** | — | Reached **#1 on GitHub Trending** (first on 2026-05-24, per Trendshift). 🟢 **The only row in this tier with release tags** — `microsoft/ai-agents-for-beginners` has **0**, re-measured this pass at `ff2ba665e088bf51d9959126c5893e089b50da30` (MIT, 1 141 B). 🔵 For a client curriculum, a tagged repo is a citable version. |

### 🔴 `P1010` — the structural finding of this pass is about this page's OWN back catalogue

🔵 **Pass 99 declared the open-response scoring tier *"release-blocked"*.** 🔴 **Tier 2d below has
carried, since pass 94, the most release-engineered repository in educational assessment — and had
recorded its commit count, never its tags.**

| Tier 2d row | recorded at pass 94 | 🟢 measured at pass 100 |
|---|---|---|
| [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) | Apache-2.0 · 11 358 B · `main` · `a844f71` · *2 916 commits* | 🟢 **33 tags · `v12.0.0`** · full SHA **`a844f71614712f81177b5731dbb17b3e018dcc85`** · conda channel `anaconda.org/ets` · **GitLab pipelines AND Azure Pipelines** · codecov · `requires-python >= 3.10` |

🟢 **33 tags, a published conda package and two independent CI systems is not a research artefact.**
🟢 **`P1010`: when a pass declares a tier blocked on a property, re-measure the tier's EXISTING rows
on that property before declaring the gap** — `tags` became a measured column only at pass 98, so
every row tabled before then carries an unpopulated one.

🟢 **`P1011` — in a regulated activity, search the INCUMBENT's open-source output BEFORE the AI
community's.** 🔵 `rsmtool` is **ETS**, the house that scores TOEFL and the GRE; its repository looks
like an organisation that has shipped under audit (versioned releases, a distribution channel,
`fairness` in its own topic list). 🔴 **`P975` still binds and is why this is a rule about
repositories, not publishers** — the same ETS organisation ships `factor_analyzer` under **GPL-2.0**.

### 🟡 `P1008` — `rsmtool`'s `pyproject.toml` is a POINTER, not a second licence oracle

🟢 Payload-read, **1 934 B**: `name = "rsmtool"`, `description = "Rater Scoring Modeling Tool"`,
`requires-python = ">= 3.10"`, `version = { attr = "rsmtool.version.__version__" }`, and
🔴 **`license = { file = "LICENSE" }`.**
🔵 **`P979` made a Maven `pom.xml` a second oracle because it NAMES a licence; a `file = `
declaration names nothing.** 🟡 **Record it as a pointer — treating it as agreement counts one
reading twice.** 🟢 **Tier 2d's Apache-2.0 therefore rests on the `LICENSE` payload alone, 11 358 B,
full canonical length** — the clean contrast with `wwrwbs/AI_AWE`'s **1 865 B** header-notice grant
(`P971`).

### 🟢 `P1009` — a README that says "this *was* the repository" is a redirect

🔴 [`scrosseye/PERSUADE_corpus`](https://github.com/scrosseye/PERSUADE_corpus) — `main` ·
`de78d7a5d22c333d24d489b95dd744a5aa490e5f`, `README.md` **3 557 B** — opens *"This **was** the
repository"* and names its successor in line 5.
🟢 **Resolved:** [`scrosseye/persuade_corpus_2.0`](https://github.com/scrosseye/persuade_corpus_2.0) —
`main` · `67d182ac88ea4a4dda736de859cfdb0bc360ee9b`, `README.md` **2 159 B**.
🔴 **Both state `CC-BY-NC-SA-4.0` in README prose; NEITHER has a licence file at the root** (`LICENSE`,
`.md`, `.txt` → three `404`s). 🔵 **`P969`'s shape again, with `P1009` as the new half: the superseded
repo gives the right licence for the wrong release.** 🟢 **Pin the successor.** `Gap 389` settled,
`Gap 390` opened — both in `agents/top.md`.


### 🟢 The structural finding of this pass is about the INSTRUMENT, so it goes at the top — `P1005`

🔵 **Seven passes recorded "`ladder.sh` denied" as one fact. It is two, and separating them changed
what this page can publish.** Every operation the ladder performs was run inline and permitted:

| operation | permitted? | yield |
|---|---|---|
| `git ls-remote --symref https://github.com/<slug> HEAD` | 🟢 **yes** | default ref + **full 40-char SHA**, 14 of 14 |
| `curl raw.githubusercontent.com/<slug>/<sha>/<name>` | 🟢 **yes** | 200 + payload, 13 of 14 |
| sourcing `lib/license_family.sh` | 🔴 **no** | it is repository code |

🟢 **So the measurement was never what was denied, and the consequence lands on this page's
addresses.** Seven passes published 7-character SHAs because the API that returns long ones is 403;
`git ls-remote` returns **only** the full 40 and was never blocked.
🔵 **`P1005`: when repository code is refused, re-run its OPERATIONS inline and read the title block
yourself — `P237` forbids a second classifier, not a second fetch.**
🔴 **What `P1005` does NOT buy: `Gap 376` still needs `grant-ladder-v4` executed**, because an
inline re-run cannot test the classifier that produced the historical rows.

### 🟢 `Gap 388` — discharged as a CONDITION, re-registered as UNWIRED

🟢 **Measured:** a true 404 from `raw.githubusercontent.com` carries a body of **exactly 14 bytes**,
the literal `404: Not Found`. 🔴 Pass 98's throttle was **429 with a 1 523 B HTML body**.
🔵 **`404` = ABSENT, `429` = THROTTLED, and at the byte level the two cannot be confused.**
🟢 **Zero 429s this pass across 14 slugs × up to 24 names**, and the pass's one negative
([`sankalpjain99/Automatic-Essay-Scoring`](https://github.com/sankalpjain99/Automatic-Essay-Scoring),
`master` · `7dd2c73933aa54ce2542705d7657596e5382f707`) is therefore a **real** absence.
🔴 **Unwired**: the remedy is three lines inside a file this sandbox will not execute.

### 🟢 The row this page LOST, now at a full address — `Gap 387`'s repair holds

🟢 [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) — **MPL-2.0**,
`LICENSE` **16 725 B**, `master` · **`7f45689f79733797e70f8c5318ec9cadb08d03be`**, **194 tags**.
🔵 **Byte term and tag count reproduce pass 98 exactly; only the address got longer.** 🟢 Third
independent agreement on MPL (passes 44, 98, 99) after two of its own `README`s said Apache-2.0
(`P997`). 🟡 **MPL is copyleft per FILE** (`§1.10(a)`), so a proprietary layer around it is lawful —
the branch `sebserver-mcp-gate` already documents.

🔴 **And `P872` false-discards on this very row**, measured at that pinned SHA: `README.md` →
**404 / 14 B**, while `LICENSE` → **200 / 16 725 B**. 🟢 A sweep gated on a `README.md` witness would
have thrown away the platform `Gap 387` exists to recover.

### 🔴 🆕 p99 Tier 2g — the LMS connector layer, and the licence split that decides which LMS is serviceable

🔵 **Every pattern on the compose page assumes an agent can reach the platform the client already
runs.** 🟢 **The three repos that do that were read this pass, and they disagree on licence.**

| slug | grant (payload · bytes · ref · full SHA) | tags / latest | verdict |
|---|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · 1 071 B · `main` · `b054b913603a206c677565bcbec128652cb9d398` | 🟢 **26 / `v1.14.0`** | 🟢 **Foundational.** Permissive **and** released; 40+ tools over the Canvas API. |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** · 34 523 B · `main` · `5a194a53cc399155bdc5e49737709f43f9a16406` | 🟡 **7 / `v0.1.7`** | 🔴 **Declined** — network copyleft on a networked server. Read as a spec, do not link. |
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🟢 **MIT** · 1 064 B · `main` · `666f12222ed6cffc9051455eb4799bb2ac8608ce` | 🔴 **0** | 🟡 **Fork base** — 1 064 B of MIT over Moodle Web Services, auditable in an afternoon. |

🔴 **The asymmetry is the finding: Canvas has a connector that is permissive AND released; Moodle has
one of each and neither is both.** 🔵 **And it is region-bearing — Moodle is what ministries and
public universities run, which is exactly where this KB has aimed LATAM and public-sector work.**
🔴 **`P975` again**: a third-party directory called the AGPL server simply *"open-source"*; the
payload says **AGPL-3.0**, and the slip ran in the expensive direction (`P997`).

### 🟡 🆕 p99 `P998`'s second shape — a clause-complete BSD-3 that a title-block classifier cannot see

[`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) — `main` ·
`196c547291da5df57b68165691e47ca7ffdbb137`, `LICENSE` **1 531 B**. 🟢 All three BSD clauses verbatim
(notice · binary reproduction · **non-endorsement**) → **BSD-3-Clause by its operative text**.
🔴 **Zero occurrences of `"BSD"`. No title block at all** — it opens
`Copyright (c) 2023-2025 Mohamed El hajji On behalf of all R2D-dev` then **`All rights reserved.`**
🔵 **`lib/license_family.sh` classifies on the title block BY DESIGN — that is precisely what `P960`
corrected v3 into — so on this payload it returns UNCLASSIFIED.** 🟢 **Recorded as the measured cost
of a correction that remains right, not as an argument to revert it;** `P237` still forbids the fork.
🟡 And for a client's counsel rather than the classifier: `All rights reserved.` above a permissive
grant is a contradiction on its face. Flagged, not resolved.

#### Pass 97 — carried below, unchanged

**Pass 97, 2026-10-10.** ⏱️ **Seventh pass of this date** (91: 23:0x–00:00 UTC; 92: 00:4x–01:3x; 93:
01:4x–02:24; 94: 02:5x; 95: 03:4x; 96: 04:4x–05:xx; this one 05:4x–06:xx). 🔴 **Repository code was
refused for a FIFTH consecutive pass** — `grant-ladder-v4/ladder.sh` **and** its offline
`test_ladder.sh` denied before starting (`[Code from External]`). 🟢 **No classifier was written**
(`P237`); the oracle map ran by hand (`P970`). **20 slugs resolved.** Evidence:
`compose/code/p989-sha-identity-fork/`.

🔴 **`api.github.com` 403 for a sixth consecutive pass, and `github.com` HTML is 403 too.** The star
channel is closed by both routes — a `—` is unread, never zero.

🔴 **The structural finding of this pass is about THIS PAGE, so it goes at the top of it: `Gap 384`.**
Pass 96 found an Apache-2.0 platform (`UniTime/unitime`) that `compose/code/` had used since pass 42
and no shelf page listed. 🟢 **Pass 97 measured whether that was a one-off. It is not.**

| population | n |
|---|---|
| distinct slugs in the append-only history (`agents/trending.md`, `repos/trending.md`) | **1 259** |
| distinct slugs on the shelf pages (this file, `agents/top.md`, `verticals/solutions.md`, `compose/patterns.md`, `intel/*.md`) | **146** |
| 🔴 in the history, on **no** shelf page | **1 119** |
| 🔴 …carrying a **permissive** grant and **no** rejection marker | **528** |
| on the shelf, never in the history | 6 |

🔵 **1 119 is not the defect and must never be cited as one** — the history records **rejected**
candidates by design (homonyms, ungranted repos, NC licences), and those are correctly absent from a
curated shelf. 🔴 **The defect is that no instrument separates "measured, and judged not worth
shelving" from "measured, and forgotten"** — and both known instances are the forgotten kind, each
found by accident: `UniTime` (pass 42 → shelved at pass 96) and **this page's entirely missing
speech-and-pronunciation tier** (verified at **pass 14**, shelved below at pass 97).
🔵 **528 is a heuristic UPPER BOUND on the forgotten set, not a worklist of 528 omissions.**

🟢 **Remedy pre-registered, and it is a ledger rather than a sweep:** a shelf row should record the
pass that promoted it; a declined candidate should record the decline. Neither fact is on any page
today, which is exactly why this can only be answered by `grep` and only as a bound. **The next pass
that can execute code should write `promotion_ledger.sh` over the committed pages — two columns, and
no new classifier (`P237`).** Lists committed at
`compose/code/p989-sha-identity-fork/promotion-gap-*.txt` so a later pass can contradict this one.

#### Pass 96 — carried below, unchanged

**Pass 96, 2026-10-10.** ⏱️ **Sixth pass of this date** (91: 23:0x–00:00 UTC; 92: 00:4x–01:3x; 93:
01:4x–02:24; 94: 02:5x; 95: 03:4x; this one 04:4x–05:xx). 🔴 **Repository code was refused for a FOURTH
consecutive pass** — `grant-ladder-v4/ladder.sh` **and** its offline `test_ladder.sh` were both denied
before starting (`[Code from External]`). 🟢 **So no classifier was written** (`P237`) and the oracle map
was run by hand (`P970`).

🟢 **What pass 96 adds to this page: Tier 2f (rubric-based evaluation, 4 permissive rows), one new Tier 3
platform row (`UniTime`), `P987`–`P986`, `Gap 377` answered with a correction to its own wording, and
`Gap 375`'s remainder discharged as *unmeasurable* with the mechanism named.** 🟢 **And the corrective
duty `Gap 376` declared was executed in the one axis the open channel allows: 127 published
`(slug, ref, sha7)` triples probed, 122 provably un-drifted, 5 moved and all 5 re-read.** Evidence in
`compose/code/p987-census-sha-currency/`. Everything not marked 🆕 p96 is carried and was not re-read.

#### Pass 94 — carried below, unchanged

**Pass 94, 2026-10-10.** ⏱️ **Fourth pass of this date** (91: 23:0x–00:00 UTC; 92: 00:4x–01:3x; 93:
01:4x–02:24; this one 02:5x). 🔴 **Repository code still will not execute in this sandbox**, so no
classifier was written for the second pass running (`P237`); the oracle map was run by hand and payloads
printed rather than matched (`P970`). 🟢 **Pass 94 adds Tier 2d (scoring validation), `P972`–`P977`, and
resolves `Gap 370`'s failing path by hand.** Everything not marked 🆕 p94 is carried and was not re-read.

#### Pass 93 — carried below, unchanged

**Pass 93, 2026-10-10.** ⏱️ **Third pass of this date** (91 ran 23:0x–00:00 UTC, 92 ran 00:4x–01:3x,
this one later the same day).

🔴 **The instrument changed again, and this time because the pass could not run the shelf's own.**
`compose/code/grant-ladder-v4/ladder.sh` is committed and correct, but **this session's sandbox declines
to execute repository code**, so pass 93 could not call it. 🔴 **The tempting move — write a fresh
classifier — is exactly what `P237` forbids and exactly what cost pass 91 two platform licences.**
🟢 **So pass 93 wrote no classifier at all.** It ran v4's *oracle map* by hand and **printed the
payload's title block instead of matching on it**:

| step | oracle | pass 93 |
|---|---|---|
| existence · default ref · SHA | `git ls-remote --symref` | ✅ ran |
| licence payload | `raw.githubusercontent.com/<slug>/<SHA>/<name>`, HTTP 200 + ≥ 1 B | ✅ ran |
| licence **family** | `lib/license_family.sh` | 🔴 could not execute → 🟢 **title block printed and read, not classified** |

🆕 🔵 **`P970` — when the shared classifier cannot be run, the honest fallback is to decline to classify,
not to fork.** Every new row below carries the bytes, the filename, the ref and the SHA, so v4 can
re-derive it mechanically next pass and disagree with this pass on the record.

**Two-sided control.** 🟡 `moodle/moodle` → `COPYING.txt` **35 147 B** at `main` · `f205347` —
byte-identical to pass 92 **and at the same SHA**, so this is a re-read of the same object rather than an
independent eleventh measurement. **Stated as such instead of counted as a reproduction.** 🟢 Invented
slug `CAHLR/pyBKT-invented-control-p93` → `ABSENT` (git exit 128, auth prompt refused). 🟢 And a
*third-party* control that cost nothing: [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic)
returned **404 on `LICENSE`, `LICENSE.txt` and `LICENSE.md`** at `master` · `5d546f2` — independently
reproducing the no-grant negative `verticals/solutions.md` already carries, with a different instrument.

🔵 **Rows not marked 🆕 are carried at their pass-92 SHAs and were NOT re-read this pass.** `—` in ★ means
not read this pass.

A *foundation* here is a repo a studio can standardise on **across clients**, independent of which LMS any one
client runs. The useful property of this tier is that it sits on spec boundaries (SCORM, xAPI, cmi5, QTI,
Open Badges, LTI), and spec-boundary code is permissive far more often than product code.

## Tier 1 — content and learner-data interoperability

This is the tier to own. Every education engagement eventually has to move content *into* a platform the client
already runs and get learner data *out* of it.

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** · 1 072 B · `master` · `882f3b8` | 354 | 🔵 unplaced | The runtime shim. SCORM 1.2 / 2004 API surface for any content in any LMS. |
| [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) | **Apache-2.0** · 11 324 B · `master` · `ea17c40` | 42 | **North America** (US DoD / ADL) | The authoritative SCORM → xAPI statement mapping. The audit-trail spec. |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | **Apache-2.0** · 11 357 B · `master` · `efa045e` | — | **North America** (US DoD / ADL) | Reference Learning Record Store — the canonical implementation to test against. |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** · 11 357 B · `main` · `cb794e4` | — | **North America** (Yet Analytics, US) | **A production SQL LRS.** Apache-2.0 and backed by a real database — this is the one to deploy, where `ADL_LRS` is the one to conform to. |
| [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) | **MIT** · 1 077 B · `master` · `b5ac7dd` | — | 🟡 **EMEA** (Tunapanda, Kenya lineage) | 🟢 **The MIT escape hatch from H5P's GPL core.** Plays H5P content with no LMS and no GPL server-side library. |
| [`celtic-project/LTI-PHP`](https://github.com/celtic-project/LTI-PHP) | 🟡 **LGPL-3.0** · 7 651 B · `master` · `1f47c93` | — | **EMEA** (UK) | LTI 1.3 tool provider. 🟡 LGPL — link, do not fork into a closed binary. |
| [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | **Apache-2.0** · 13 185 B · `develop` · `0a66b52` | — | **North America** (1EdTech) | Open Badges validation. The credentialing tier's conformance gate. |
| 🆕 [`edly-io/pxc`](https://github.com/edly-io/pxc) | **Apache-2.0** · 11 358 B · `main` · `01114d3` | 9 | 🔵 unplaced (publisher is the Open edX commercial vendor **edly.io**) | 🟢 **Watch this one.** A **proposed standard for learning activities explicitly intended to replace SCORM, H5P *and* LTI** — the three specs this entire tier is built on — published permissively by the vendor that packages Open edX. 🔵 **Nine stars and strategically larger than anything else on this page.** Not a dependency yet; a reason to keep the interop layer behind an interface you own. |

## 🆕 Tier 1b — a national curriculum as verified open data, and the counter-example to `Gap 367`

🔴 **The shelf has said for two passes that the reference frameworks of the curriculum mandates cannot be
shipped:** `touretzkyds/ai4k12` (AAAI/CSTA) carries **no licence payload in 24 filenames**, and
`learning-commons-org/knowledge-graph`'s `LICENSE.md` grants nothing at all (`P965`). 🟢 **For Brazil that
is now false, and the counter-example is better engineered than anything else in this category.**

**`bncc.dev`, run by Profy, publishes Brazil's *Base Nacional Comum Curricular* as verified open data** —
and the licences were read from the payload at pinned SHAs:

| repo | grant (payload · bytes · ref · SHA) | ★ | what it is |
|---|---|---|---|
| 🆕 [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟡 **`LICENSE` = MIT** · 1 073 B · `main` · `daabd7d` — **but the data is CC BY 4.0, and that grant is NOT at the root** (see `P969` below) | 20 | **1 721 learning objectives** (1 580 from the three stages of basic education + 141 from the Computing supplement) in **JSON, SQLite and CSV**, with **per-record provenance** (`fonte` → spreadsheet row + PDF page) and a reproducible extraction pipeline that CI re-runs and rejects on divergence. 🟢 **1 576 of 1 580 BNCC-2018 texts match the official MEC/CNE PDF character for character; the 4 mismatches are documented in `DECISOES.md`. 141 of 141 for Computing.** 🔵 **That is a provenance claim with a denominator — rare anywhere on this shelf.** |
| 🆕 [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 **split grant, declared at the root** · `LICENSE` 1 299 B (index) · `main` · `ac9feb8` → **MIT** for `packages/*/src/`, `python/bncc/*.py`, `mcp-worker/src/`, `scripts/`, tests and config; **CC BY 4.0** for the data | 9 | npm `@bncc/dados` 0.3.1, npm `@bncc/mcp` 0.2.0, PyPI `bncc` 0.2.0, plus a hosted MCP worker. 🟢 **The MCP server exposes 7 tools** (`bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`) **with the dataset embedded, so queries run locally.** 🟡 All three packages are pre-1.0. |
| 🆕 [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟢 **split grant, declared at the root** · `LICENSE` 911 B (index) · `main` · `4713901` → **MIT** for `harness/` and `test/`; **CC BY 4.0** for `itens/`, `resultados/`, `METODOLOGIA.md` | 9 | An **open hallucination benchmark over the BNCC**. See `intel/trends.md` `T11` — it carries the most useful number this pass produced. 🟢 **Its README declares a conflict of interest in its own words**: *"Vale declarar o conflito de interesse: a Profy opera produtos que usam LLMs sobre a BNCC."* |
| 🆕 [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) | **MIT** · `LICENSE` 1 218 B · `main` · `f94ca6a` | — | An **independent** MCP server over the BNCC skills, from a different author. 🔵 **n=2 for MCP × national curriculum**, which is the same "new shape, not n=1" test the shelf applied to MCP × SCORM in pass 92. |

🔵 **Region, and the evidence class.** **LATAM (Brazil)** — and not by inference from the subject matter:
the `bncc-pacotes` and `bncc-benchmark` licence payloads are **written in Portuguese**, and the data's
attribution clause names **MEC/CNE**, Brazil's education ministry and national council. The payload itself
carries the region.

### 🔴 🆕 `P969` — the grant ladder reads repo-root filenames only, so a per-directory data licence is invisible to it

🔴 **`bncc-dados` is the row that proves it, and the cost is an attribution obligation, not a nuance.**

| oracle | what it reports for `bncc-dev/bncc-dados` |
|---|---|
| the 24-filename ladder at the repo root | 🔴 **MIT** (`LICENSE`, 1 073 B) |
| GitHub's own licence sidebar | 🔴 **"MIT license"**, nothing else |
| the repo's README and `dados/LICENSE.md` | 🟢 **data under `dados/` is CC BY 4.0**; MIT covers `pipeline/` |

🔴 **A repository whose entire purpose is the dataset presents MIT at the root, and both automated oracles
agree on the wrong answer for the artefact a studio would actually ship.** `LICENSE-DADOS.md` at the root
is a **404** — the grant is one directory down, where 24 root filenames cannot reach.
🔵 **Two independent oracles, one blind spot, one cause: root-only detection.** That is the strongest form
this finding can take, because it cannot be dismissed as a defect in this KB's instrument.

🟢 **And the same publisher shows the fix in its own other two repos**: `bncc-pacotes` and `bncc-benchmark`
put a **split-grant index at the root** that names each licence and scopes it to explicit paths. The ladder
reads those correctly. **Convention, not tooling, is what makes a split grant legible.**

🟢 **`P965`'s measured threshold survives a payload it was not built on.** Pass 92 set it at *a real grant
names 0–2 families; a framework document names 3, from three lineages*. These index files name **2** (MIT +
CC BY 4.0), from two lineages, and they **are** real grants — each points at the full text
(`LICENSE-CODIGO.md` 1 286 B, `LICENSE-DADOS.md` 577 B, both HTTP 200, both verified present this pass).
🔵 **Same document *shape* as `learning-commons-org/knowledge-graph`, opposite usability — and the
threshold separates them correctly.**

🔴 **The fix this pass does not pretend to have made.** `compose/code/p199-perfile-license/` already does
per-path licence probing — it exists, and it was run on `INGInious`. **It is not wired into the ladder**,
and this pass could not execute either. **Recorded as `Gap 370`**, with the payload that proves it needed,
so the next pass that can run code has a failing case ready.

## Tier 2 — assessment and automated feedback

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| [`numbas/Numbas`](https://github.com/numbas/Numbas) | **Apache-2.0** · 11 357 B · `master` · `39b03e5` | 215 | **EMEA** (Newcastle University, UK) | Browser-native e-assessment with real mathematics; SCORM-packageable. The strongest permissive assessment engine on this shelf. |
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | **BSD** · `LICENSE.md` 1 542 B · `main` · `80d7d66` | — | **North America** (RPI, US) | Full course-management + autograding platform, **BSD**. Permissive and production — rare in this tier. |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | **BSD** · 1 560 B · `master` · `190c1a4` | — | **North America** (UC Berkeley, US) | Notebook autograding; the standard in data-science teaching. |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | **BSD** · 1 512 B · `main` · `f9915da` | — | **North America** (Project Jupyter) | Assignment release/collect/grade for notebooks. |
| [`webtech-network/autograder`](https://github.com/webtech-network/autograder) | **Apache-2.0** · 11 357 B · `main` · `04bee3e` | — | 🔵 unplaced | Rubric-driven autograding with report generation; release 0.4.0 (May 2026). |

## 🆕 p94 Tier 2d — the scoring-**validation** layer, and why it is the half worth having

🟢 **Three rows, all read from the payload this pass, and one of them changes what `Gap 372` says.**

| repo | grant (payload · bytes · file · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| 🆕 p94 · 🟢 **re-measured p100** [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) | 🟢 **Apache-2.0** · **11 358 B** · `LICENSE` · `main` · **`a844f71614712f81177b5731dbb17b3e018dcc85`** | 71 | 🟢 **North America** (ETS) | 🟢 **33 tags · `v12.0.0`** — conda `anaconda.org/ets`, GitLab + Azure CI, codecov, `requires-python >= 3.10`. **2 916 commits.** Builds **and evaluates** automated scoring models from a configuration file; customisable HTML statistical report; scikit-learn + SHAP; `fairness` among its own topics. 🔴 **Not a scoring engine** — it is how you demonstrate one is valid. 🔵 **`P1008`: its `pyproject.toml` points at `LICENSE` and is not a second oracle.** |
| 🆕 p94 [`EducationalTestingService/skll`](https://github.com/EducationalTestingService/skll) | 🟢 **BSD-3-Clause** · 1 555 B · `LICENSE.txt` · `main` · `b350eb0` | — | 🟢 **North America** — `P800`: *"Copyright (c) 2012–2022 Educational Testing Service"* | scikit-learn experiments driven by configuration. Pinned by `rsmtool` at `skll==5.0.1`, so the pair is a single dependency decision. |
| 🆕 p94 [`HASKI-RAK/NodeGrade`](https://github.com/HASKI-RAK/NodeGrade) | 🟢 **MIT** · 1 062 B · `LICENSE` · `main` · `8e144ac` | 3 | 🟡 **EMEA** (Germany, by the ECSEE '25 citation; the payload holder reads only *"HASKI"* — weaker than `P800`) | **421 commits.** Short-answer grading as a node graph with **LTI 1.1/1.3**; NestJS + Prisma + Postgres, React/Vite PWA, Python sentence-embedding worker, **local-model provider included**. |

🔵 **Why this tier is not a duplicate of Tier 2.** Tier 2 grades **structured** work — maths, notebooks,
code — and does it well and permissively. This tier is about **open-response** work and about the artefact
that regulated assessment actually owes: **a validity and fairness argument, in a report, with the model's
behaviour attributable.** 🟢 **That artefact is Apache/BSD.** 🔴 **The scorer is not** — see the flags
below.

🔴 **Flags that belong with this tier, all payload-read this pass:**

| repo | payload | why it is flagged |
|---|---|---|
| 🆕 p94 [`openedx/ease`](https://github.com/openedx/ease) | 🔴 **AGPL-3.0** · 35 136 B · `LICENSE.txt` · `master` · `056da0a` | edX's *Enhanced AI Scoring Engine*. The obvious candidate for an AES build, and network copyleft. |
| 🆕 p94 [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 **AGPL-3.0** · 35 135 B · `LICENSE` · `master` · `1b7ae59` | Open Response Assessment inside Open edX — peer, self and staff assessment. Same grant. |
| 🆕 p94 [`EducationalTestingService/factor_analyzer`](https://github.com/EducationalTestingService/factor_analyzer) | 🔴 **GPL-2.0** · 18 092 B · `LICENSE` · `main` · `de933d2` | 🔴 **From the same publisher as the two permissive rows above.** Dependency-shaped (EFA/CFA) — the kind of library a scoring pipeline imports without reading. `P975`. |

### 🔴 🆕 `P975` — licence is a property of the repository, never of the publisher

**Educational Testing Service ships Apache-2.0, BSD-3-Clause and GPL-2.0 from one GitHub organisation**,
measured in a single sitting above. 🔵 **A licensing-sophisticated publisher is the case where the
inference feels safest, which is what makes it the right counter-example.** 🟢 Negative control recorded
with it: `EducationalTestingService/rsmexplain`, named by a search summary, **does not resolve**
(`git ls-remote` exit 128).

### 🟢 🆕 `P974` — probe for clauses, not for bytes

Pass 93's `P971` (a `LICENSE` that is Apache's **header notice**, not its **licence**) was caught by size.
🔴 **Size alone also condemns honest abridged copies** — `SimonsTang/feifei-companion` is 10 227 B and
real. 🟢 **Four clause headings settle it**: *Grant of Patent License* · *Grant of Copyright License* ·
*Redistribution* · *APPENDIX*. `rsmtool` → **4 of 4**; `AI_AWE` → **0 of 4**. 🔵 **And the discriminating
clause is the one that justifies choosing Apache at all:** §3, the express patent grant.

### 🟢 🆕 `P972` / `P973` — platform versions are payload-readable, and `version.php` is not at the root

Full statement and evidence in **`compose/code/p972-platform-version-ladder/`**; the consequences for the
platform tier are in `verticals/solutions.md`. In one line each:

- 🟢 **`P972`** — `git ls-remote --heads|--tags <slug>` returns the release ladder and
  `raw.githubusercontent.com/<slug>/<SHA>/<version file>` returns the release string. **Moodle: `main` is
  `6.0dev (Build: 20261005)`, `MATURITY_ALPHA`; `MOODLE_503_STABLE` is `5.3`, `MATURITY_STABLE`.** 🔴 Every
  secondary source read this pass said 5.2.
- 🔴 **`P973`** — `moodle/moodle`'s root `version.php` is **404**; the file is `public/version.php`, because
  the web root moved into `public/` at 5.0. **`P969` is a path defect, not a licence defect**, and this KB
  has probed 24 licence filenames at the root for ninety passes.
- 🟡 **`P977`** — the ladder oracle's own limit: `openedx/edx-platform`'s `open-release/*` **heads stop at
  Sumac** while `release/teak.*` and `release/ulmo.*` exist only as **tags** under a **changed prefix**.
  Cross-check the deployment distribution (`overhangio/tutor` → `v22.0.2`).

## 🟢 🆕 p96 Tier 2f — the **rubric** layer, and why it reframes the alignment gap rather than closing it

🔴 **This page has carried a five-pass negative:** *nothing permissive audits whether content meets a
learning outcome with usable evidence.* 🟢 **The technique half of that is now false.** Found on the first
query naming **rubrics** rather than education — `P955` for a fourth consecutive pass:

| repo | grant (payload · bytes · ref · SHA-40 prefix) | ★ | layer it supplies |
|---|---|---|---|
| 🆕 p96 [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🟢 **Apache-2.0** · 10 770 B · `master` · `4c7f22b5707536` | — | 🟢 **the judge** — 50+ query-type rubric sets, criteria **weighted critical / core / important / highlight**, bi-directional A/B debiasing, **interpretable verdicts** |
| 🆕 p96 [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 **MIT** · 1 067 B · `main` · `1a40c14cb7827ae` | — | 🟢 **the generator** — synthetic rubric generation at scale (ACL 2026 long) |
| 🆕 p96 [`planepig/rubricbench`](https://github.com/planepig/rubricbench) | 🟢 **MIT** · 1 067 B · `main` · `07daecc72ac159` | — | 🟢 **the calibrator** — **1 147 pairwise comparisons**, expert-annotated atomic rubrics, scores reasoning **and** verdict |
| 🆕 p96 [`chrisliu298/awesome-rubric-rewards`](https://github.com/chrisliu298/awesome-rubric-rewards) | 🟡 **CC0-1.0** · 7 048 B · `main` · `4897f496d7868e` | — | the index — **a list, not a dependency** |

🟢 **`P974` positive class, second instance, with the missing section identified.** `OpenRS`'s payload is
**10 770 B** against pristine Apache-2.0's **11 357 B**; the clause probe returns **4 of 4** headings and
**`APPENDIX` ABSENT**. 🔵 **An honest abridgement that dropped only the "how to apply" boilerplate** — the
byte gap had a cause and the cause was benign.

### 🔵 Why this is a reframe and not a discharge — `Gap 379`

🔴 **None of these four knows what a learning outcome is.** They bind a rubric to an **instruction**.
🟢 **And this page already carries the other end of the bind, permissively:**
[`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) (**Tier 1b** — MIT code + CC BY 4.0
data, **1 721 verified BNCC objectives** behind **7 MCP tools**, dataset embedded so lookups are local) and
[`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (**MIT** judging
code against research-backed educational rubrics — 🔴 corpora **CC-BY-NC-SA-4.0**).

🔵 **Four permissive layers, three unrelated publishers, zero integrations.** 🟢 **That is `Gap 369`'s exact
shape, and it is tracked as `Gap 379`** with a concrete specification in `P96-A`.

🟢 **One subsidiary finding worth carrying: `rubricbench`'s 1 147 expert-annotated comparisons are MIT** —
**the first permissive annotated comparison set this shelf has found**, even though its domains (Chat, IF,
STEM, Coding, Safety) are not education. 🔵 **It is the thing `evaluators`' NC corpora are not**, and for
*calibrating a judge* rather than *scoring a student* the domain mismatch matters less than the grant.

## 🆕 Tier 2b — the learner model — **`Gap 335` discharged after eight passes untouched**

🔴 **`Gap 335` (knowledge tracing) was the oldest untouched item on this shelf**, named openly in
`agents/top.md` for eight passes: *"only `adaptive-knowledge-graph` (Bayesian) and `Bloom` (2-sigma)
carry an explicit learner model. Everything else relies on the context window, which is not a mastery
estimate."* 🟢 **The canonical library exists, it is MIT, and it was found on the first query that
named the technique instead of the industry** — `P955` holding for a second pass running.

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| 🆕 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` | ~430 | 🔵 unplaced | 🟢 **The reference deep-knowledge-tracing benchmark library** (NeurIPS 2022 datasets-and-benchmarks track, `pykt.org`). Standardised preprocessing plus a model zoo — **DKT, DKVMN, SAKT, SAINT, AKT, GKT, LPKT** — over 7 datasets. 🔵 **This is the missing layer, not another tutor:** it turns "the agent remembers the conversation" into **a per-skill mastery estimate you can threshold on**, which is what adaptive sequencing and mastery-gated progression actually need. MIT, so it can sit inside a paid deliverable. |
| 🆕 [`JonathanSilver/pyKT`](https://github.com/JonathanSilver/pyKT) | **MIT** · 1 065 B · `main` · `2bef7e9` | — | 🔵 unplaced | 🔴 **Name collision, and the weaker of the two.** A separate PyTorch reference implementation whose own README warns *"not all the implemented models have achieved comparable performance to that of the original implementations"*. 🔵 **Read it as a reference, never as the benchmark** — and note it is reachable by the same search string as the row above. |

🔴 **And the third candidate carries no grant:**
[`weiwei1392/knowledge-tracing`](https://github.com/weiwei1392/knowledge-tracing) → **no licence
payload in 24 filenames** · `main` · `136efef`.

🆕 🔵 **`P968` — two repos sharing a project name is a licence-and-quality trap, not a trivia item.**
`pykt-team/pykt-toolkit` and `JonathanSilver/pyKT` are both MIT, so a licence probe cannot separate
them; only reading the README does. This is the same shape as `Gap 368`'s acronym collision on
`topics/lms` (**LMS = Least Mean Squares**, **LMS = Library Management System**) — 🔵 **in this
industry, name collision is a recurring property of the search space, so the canonical slug belongs
in the shelf row and not just the project name.**

## 🆕 Tier 2c — the **psychometric** layer, and why it outranks the deep-learning one for a deliverable

🟢 **Pass 92 discharged `Gap 335` with one library** — `pykt-team/pykt-toolkit`, deep knowledge tracing —
and wrote that the learner model had arrived. 🔴 **That was half the answer.** Naming three more
techniques (`P955` for a third pass running) returns a **complete, composable, permissive stack**, and the
important finding is the ordering inside it:

🔵 **The classical psychometrics layer is more production-ready than the deep-learning layer, and more
defensible.** `catsim` has 877 commits and a BSD grant; `pykt-toolkit` is a research benchmark. More to the
point, **IRT and BKT produce a parameter you can show a regulator** — an item difficulty, a per-skill
mastery probability — whereas a DKT network produces an activation. Under the EU AI Act's Annex III,
assessing learning outcomes is high-risk and owes an explanation (`intel/trends.md` `T9`). **A 2-parameter
logistic item curve is an explanation. A trained LSTM is not.**

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| 🆕 [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | **MIT** · `LICENSE` 1 132 B · `master` · `cc1682e` | 282 | 🟢 **North America** (UC Berkeley — the payload's copyright line reads *"Computational Approaches to Human Learning (CAHL) Research, zp@berkeley.edu"*, `P800`) | **Bayesian Knowledge Tracing** and its variants, scikit-learn-shaped (`Model.fit`/`predict`), EM-fitted. 🟢 **The cheapest real mastery estimate on this shelf**: four interpretable parameters per skill (prior, learn, slip, guess), each of which a teacher can be shown. |
| 🆕 [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | **MIT** · `LICENSE` 1 121 B · `master` · `6514928` | 173 | 🟢 **North America** (Notre Dame — payload copyright line *"John Lalor <john.lalor@nd.edu> and Pedro Rodriguez"*, `P800`) | **Bayesian Item Response Theory** on Pyro/PyTorch, GPU-scalable. Calibrates *item* difficulty and discrimination and *learner* ability on the same scale. 🔵 **This is the calibration step; it does not select items.** |
| 🆕 [`eribean/girth`](https://github.com/eribean/girth) | **MIT** · `LICENSE.txt` 1 064 B · `master` · `daf2277` | 126 | 🔵 unplaced (payload copyright line is a pseudonym — *"eribean"* — no geography to take, so none is asserted) | The second IRT estimator, and the one **`catsim`'s own README points at**. 🟡 Note the filename: `LICENSE` is a **404** here and the grant lives in `LICENSE.txt` — the ladder's 24-name reach is what makes this row readable at all. |
| 🆕 p95 [`eribean/girth_mcmc`](https://github.com/eribean/girth_mcmc) | **MIT** · `LICENSE.txt` 1 061 B · `main` · version **0.6.0** | — | 🔵 unplaced (same pseudonymous holder as `girth`; no geography to take, so none is asserted) | **Bayesian / MCMC item-response-theory estimation** — the sampling companion to `girth`, and the third of the three estimators `catsim`'s README points Python users at. 🟢 **Triple-confirmed grant**: the `LICENSE.txt` payload is canonical MIT, `setup.py` declares `license="MIT"`, and the classifier says `License :: OSI Approved :: MIT License`. 🟡 **Same filename trap as `girth`**: `LICENSE` is a **404**, the grant is in `LICENSE.txt`. |
| 🆕 [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** · `LICENSE` 1 514 B · `dev` · `7e6caae` | 153 | 🟡 **LATAM** (Brazil) — ⚠️ **evidence class is weaker than `P800`**: the payload's copyright line is a personal name only, and the Brazil placement comes from the project's own documentation host, `douglasrizzo.com.br`, linked throughout the README. Labelled, not upgraded. | **Computerized Adaptive Testing engine** — item selection, ability estimation, stopping rules, plus a simulator. 🟢 **The only CAT engine on this shelf, and the only psychometrics row with a LATAM claim.** 🟡 Default branch is `dev`, not `main` — pin it. |
| 🆕 [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | **MIT** · `LICENSE` 1 079 B · `main` · `9446cb0` | 506 | 🔵 unplaced (payload copyright line is the org, *"Open Spaced Repetition"*) | **FSRS scheduling** — when to show an item again, as a library. 🔵 **The complement to mastery, not a duplicate of it:** BKT/IRT say *whether* a learner knows a skill; FSRS says *when they will forget it*. Highest star count in this tier. |
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` | ~430 | 🔵 unplaced | 🟢 Deep knowledge tracing: DKT, DKVMN, SAKT, SAINT, AKT, GKT, LPKT over 7 datasets (NeurIPS 2022). **Carried from pass 92 at its pass-92 SHA; not re-read this pass.** 🔵 Read it as the research ceiling, and `pyBKT` as the deliverable floor. |

### 🟢 The seam is named by the tools themselves, not inferred by this KB

🔵 **This is why the tier composes instead of overlapping, and the evidence is in `catsim`'s README
verbatim:** *"**catsim does not implement item parameter estimation.** I have had great joy outsourcing
that functionality to the [mirt] R package."* It then points Python users at exactly
[`eribean/girth`](https://github.com/eribean/girth), [`eribean/girth_mcmc`](https://github.com/eribean/girth_mcmc)
and [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt).

🟢 **So the wiring is documented by the dependency, not designed by us:** `py-irt` (or `girth`) calibrates
the item bank → `catsim` runs the adaptive session against it → `pyBKT` tracks per-skill mastery across
sessions → `py-fsrs` schedules the review. **Four permissive libraries, one seam each, no overlap.**
Costed as `P93-A` in `compose/patterns.md`.

🟢 **🆕 p95: the subtraction pass 93 and 94 both carried is now paid.** Those passes recorded that
`girth_mcmc` was *named by `catsim` but not resolved* — a lead, not a row. **Pass 95 resolved it: MIT,
`0.6.0`, at `LICENSE.txt`.** It is in the table above, and **all three estimators `catsim` names are now
permissive rows on this shelf** (`girth`, `girth_mcmc`, `py-irt`). 🔵 **The seam is therefore not just
documented by the dependency — it is fully supplied.**

## 🆕 p95 Tier 2e — the **autograding** layer, and the AGPL monopoly that just ended

🔴 **Until this pass, every automated-feedback row on this shelf with real classroom use was copyleft.**
`mumuki/mumuki-laboratory` (AGPL-3.0, Argentina) was the strongest, and `openedx/ease` and
`openedx/edx-ora2` are both AGPL-3.0. 🟢 **There is now a BSD-3 row at that layer.**

| repo | grant (payload · bytes · file · ref · SHA) | version | ★ | region | role in a build |
|---|---|---|---|---|---|
| 🆕 [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** · 1 560 B · `LICENSE` · `master` · `190c1a4` | **7.0.0** | — | 🟢 **North America** (UC Berkeley Data Science Education Program) | 🟢 **Production autograder for Python scripts and Jupyter notebooks at course scale.** Parallel Docker grading, an Otter-managed grading VM, a student-side client for public checks, **native Canvas and Gradescope support**. Zenodo DOI, live CI and coverage. |

🟢 **Three-layer licence agreement** — `LICENSE` payload, `pyproject.toml` (`license = "BSD-3-Clause"`) and
the PyPI classifier all concur. 🟢 **And it is the one row on this shelf where the default branch and the
tag ladder agree** (`7.0.0` = `v7.0.0`), which under `P978` makes its published version also its shippable
one.

🔴 **What this tier is NOT.** Otter grades **code against tests**. It is not an open-response scorer, so
**`Gap 372` is untouched by it** — see `agents/top.md` for that gap's three new measured negatives. 🔵 **The
honest framing: this closes the *programming-assessment* hole, which nobody had named, and leaves the
*constructed-response* hole, which five passes have.**

### 🔴 🆕 `P980` — resolve a tool to its repository, never to its distribution name

Finding this row surfaced a collision worth carrying into every future probe:

| what you cite | PyPI | repository | grant |
|---|---|---|---|
| `otter-grader` | `otter-grader` **7.0.0** | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** · 1 560 B · `190c1a4` |
| `Otter-Autograder` | `Otter-Autograder` **0.15.9** | [`OtterDen-Lab/Autograder`](https://github.com/OtterDen-Lab/Autograder) | 🔴 **GPL-3.0** · 35 149 B · `2d9555f` |

🔴 **Two unrelated projects, both autograders, incompatible grants, seven majors apart.** A search summary
reporting *"Otter-Autograder is GPL-3.0-or-later"* was reading the **other** project. 🟢 **Only the
`project_urls` → repository link disambiguates them.** 🟡 **And do not read `info.license` from PyPI for an
identifier:** `Otter-Autograder` pastes the **entire 35 kB GPL-3.0 text** into that field with
`license_expression` set to `None`. **The `classifiers` array was correct for both.**

## 🟢 🆕 p97 Tier 2g — the **speech and pronunciation** layer, promoted after 83 passes off the shelf

🔴 **This layer was verified in the append-only history at pass 14 and has never appeared on this
page.** It is `Gap 384`'s headline instance. 🟢 **Two rows are genuinely new; the rest are
promotions; three are corrections.** 🔵 **The seam is named by the tools themselves** — alignment,
scoring and benchmarking are three separate repos with three separate interfaces, which is what
makes this layer composable rather than monolithic.

| repo | grant (payload · bytes · ref · SHA-14) | release ladder | layer |
|---|---|---|---|
| 🆕 p97 [`MontrealCorpusTools/Montreal-Forced-Aligner`](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) | 🟢 **MIT** · `LICENSE` **1 066 B** · `main` · `93411fc0df3bc7` | 🟢 **116 tags · `v3.4.3`** | **alignment** — the step under every score. 🟢 **The only member with a real release ladder.** 🔵 Titleless MIT (opens at `Copyright (c) 2016`). |
| 🆕 p97 [`lingjzhu/charsiu`](https://github.com/lingjzhu/charsiu) | 🟢 **MIT** · `LICENSE` **1 061 B** · `main` · `13a69f2a22ca0c` | 🔴 0 tags | **alignment, text-independent** — no reference transcript needed. Complements MFA. |
| 🔵 promoted [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | 🟢 **MIT** · 1 113 B · `main` · `74bc17ea406e6f` | 🟡 2 tags · `v0.3.0` | **scoring** — phoneme/word error rate, DTW distance, prosody. Local, no API key. |
| 🔵 promoted [`YuanGongND/gopt`](https://github.com/YuanGongND/gopt) | 🟢 **BSD-3-Clause** · 1 517 B · `master` · `bed909daf8eca0` | 🔴 0 tags | **scoring, published baseline** (ICASSP 2022). |
| 🆕 p97 [`doheejin/HiPAMA`](https://github.com/doheejin/HiPAMA) | 🟢 **BSD-3-Clause** · 1 526 B · `main` · `89e3f650e224e2` | 🔴 0 tags | **scoring, hierarchical multi-aspect.** 🟢 `P995` — grant carries `Copyright (c) 2022, Yuan Gong` first: **gopt lineage, proved from the payload.** |
| 🔵 promoted [`Fuann/open-apa`](https://github.com/Fuann/open-apa) | 🟢 **BSD-3-Clause** · 1 528 B · `master` · `2c92c0de1eca58` | 🔴 0 tags | **benchmark** — scores the scorer. This is the acceptance-test layer. |
| 🔵 promoted [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | 🟡 **Apache-2.0** · `COPYING` **17 264 B** · `master` · `e02e35f0254bb0` | 🔴 0 tags | **ASR substrate.** 🔴 `P991` — title displaced to byte 2 531; 4/4 clause headings. |
| 🔴 **CORRECTION** [`CyanXLab/Phonos`](https://github.com/CyanXLab/Phonos) | 🔴 **NO LICENCE PAYLOAD** / 24 names @ 1 B · `8a13a3b7611a3d` | 1 tag | 🔴 **This KB counted it in a permissive layer of three. It has no grant.** |
| 🔴 negative [`jimbozhang/speechocean762`](https://github.com/jimbozhang/speechocean762) | 🔴 **NO LICENCE PAYLOAD** · `613968e3b0b789` | 🔴 0 tags | 🔴 **`P994` — the reference CORPUS is ungranted while all seven tools are permissive.** |
| 🔴 negative [`tzyll/goparrot`](https://github.com/tzyll/goparrot) · [`JazminVidal/gop-pykaldi`](https://github.com/JazminVidal/gop-pykaldi) | 🔴 **NO LICENCE PAYLOAD** (both) | 🔴 0 tags | Two more GOP implementations, neither granted (`P981`). |

### 🔴 🆕 `P994` — a permissive toolchain around an ungranted corpus is a scope item, not a blocker

🟢 **Seven of nine members carry a permissive grant**, and the two that do not are the **data**:
the reference corpus (`speechocean762`) and one engine with no licence file at all (`Phonos`).
🔴 **So the honest statement to a client is that the pipeline ships and the calibration data does
not** — the deliverable either licenses a corpus or collects and labels its own.

🔵 **And for two of this KB's four regions that is less bad than it reads.** Pronunciation scoring is
**L1-specific**: a Spanish-L1 or Mandarin-L1 learner needs data from that population, which an
engagement was going to collect locally regardless of what `speechocean762` permits. 🟢 **For LATAM
and APAC the corpus gap is pre-existing scope, not licence-induced risk.** 🔴 **For a North America
or EMEA engagement expecting to drop in an off-the-shelf English benchmark, it is a real cost.**

### 🟡 🆕 `P991` / `P992` — two byte-level facts this tier produced, both about Apache-2.0

🟡 **`P991` — the title block can be DISPLACED rather than absent.** `kaldi-asr/kaldi` serves
`COPYING` at **17 264 B**; `Apache License` first occurs at **byte offset 2 531**, behind a
2 531-byte joint-ownership clarification notice ("*Update to legal notice, made Feb 2012, modified
Sep 2013*"), and `TERMS AND CONDITIONS` at 6 068. 🟢 **All 4 Apache clause headings are present
(`P974`), so the grant is the full unabridged body, and `lib/license_family.sh` resolves it** — its
title window is `head -c 4000` (line 106). 🔵 **What is new is the price of that bound: the worst
displacement this KB has measured consumes 63 % of the window, leaving 1 469 B.** The comment at
line 95 calls the limit *"MEDIDO, NO ELEGIDO"* — **this is the specimen that measures it.**

🟡 **`P992` — the authority and the pristine copy differ by one byte.**
`apache.org/licenses/LICENSE-2.0.txt` is **11 358 B** and opens with a blank line; the repo-side
pristine copy is **11 357 B**, opening at `                                 Apache License`. `diff`
reduces to `0a1 > $`. 🔴 **A byte-equality check against the authoritative text would mark every
pristine repository copy "modified".** 🟢 **11 357 B is the correct repo-side constant**, now on a
third independent instance (`UniTime/unitime` p96, `HendrikStrobelt/detecting-fake-text` p97, and
this canonical compare) — **so never "fix" `p386-pristine-dedup-gate` by diffing upstream.**

## Tier 3 — delivery, runtime and agent substrate

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** · 1 097 B · `develop` · `d4fea9c` | — | **North America** (Learning Equality, US) | **Offline-first learning delivery.** MIT. The correct substrate wherever connectivity is the binding constraint — which, per UNESCO, is most of APAC's and LATAM's deployment reality, not an edge case. |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** · 11 358 B · `develop` · `ad22e91` | — | **North America** (Oppia Foundation) | Structured, explanation-driven interactive lessons; a real pedagogy model in code. |
| [`oppia/oppia-android`](https://github.com/oppia/oppia-android) | **Apache-2.0** · 11 357 B · `develop` · `25e3860` | — | **North America** | The offline Android client for the above. |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | **BSD** · 1 475 B · `main` · `f02ec3c` | — | 🔵 unplaced | Multi-tenant notebook serving — the per-learner compute boundary. |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** · 1 072 B · `main` · `12aeb0f` | — | **North America** | Stateful agent orchestration. The graph, not the agent. |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | **Apache-2.0** · 11 357 B · `main` · `96f33fa` | — | **EMEA** (Hugging Face, FR lineage) | Minimal agent loop; the low-ceremony option when LangGraph is too much machinery. |
| [`huggingface/agents-course`](https://github.com/huggingface/agents-course) | **Apache-2.0** · 11 357 B · `main` · `3c469e7` | — | **EMEA** | 🟢 The permissive **teaching** counterpart to `smolagents` — see the AI-literacy tier in `agents/top.md`. |

## 🔴 🆕 p98 `SafeExamBrowser/seb-server` — the row below `UniTime`'s was DROPPED by this KB's own reset, and `compose/code/` still points at it

🔵 **Read the `UniTime` section that follows first: this is the same defect one pass later, and worse,
because this row was not merely unshelved — it was shelved, verified, and then LOST.**

🟢 **`compose/code/sebserver-mcp-gate/README.md` (pass 44) states that the MPL-2.0 verdict is
*"what `repos/foundations.md` and the pase-41/42 trends say"*.** 🔴 **This page said nothing about it
until now.** 🟢 **`archive/2026-10-06-pre-reset/repos-foundations.md:3774` proves the claim was true
when written:** *"🟢 `SafeExamBrowser/seb-server` (⚠️ MPL-2.0, `HEAD` de `master` = `7f45689`,
2026-04-01)"*. 🔴 **The 2026-10-06 reset dropped it** (`Gap 387`).

| repo | grant (payload · bytes · ref · SHA-14) | release ladder | ★ | region | role in a build |
|---|---|---|---|---|---|
| 🆕 p98 [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | 🟡 **MPL-2.0** · `LICENSE` **16 725 B** · `master` · `7f45689f797337` | 🟢 **194 tags**, `v3.0-latest` | — | 🟡 **EMEA** (ETH Zürich lineage — the Java package tree is `ch/ethz/seb/`) | 🟢 **Institutional exam supervision and lockdown.** The supervision half of the exam layer whose scheduling half is `UniTime`. |

🔵 **Why MPL-2.0 is the useful verdict and not just a licence string:** MPL is **per-file** copyleft
(§1.10(a)). A proprietary integration layer around it is lawful; only **modified MPL files**
reciprocate. 🟢 **In practice a third-party proctoring provider obliges you to publish one enum
value.** 🔴 **That argument is void if the licence is read as Apache-2.0** — and two of the three
`compose/code/` READMEs said exactly that until this commit (`P997`). 🟢 **This is the FIRST MPL-2.0
row on any live page of this KB.**

🟢 **What already exists here, tested, and now has a page to be sold from:**
`sebserver-mcp-gate` (MCP allowlist, `P85`'s second instance) · `seb-proctoring-validator` (closes
upstream gap 90 in `ProctoringSettingsValidator.java`, which checks credentials for `JITSI_MEET` and
`ZOOM` only and then returns `true`) · `proctoring-reach-audit` (which provider methods reach the
network: Jitsi 1, 🔴 **Zoom 5, not 2** — a correction this base already made to its own figure).

🔴 **And the regulatory hook is already on `intel/trends.md`:** emotion recognition in education has
been **prohibited since 2 Feb 2025** under Article 5, and affect inference ships switched on by
default in proctoring products. 🔵 **So the only permissive-adjacent platform in the exposed category
was absent from every shelf page while the exposure was published on one.** 🔵 **That is `Gap 381`
costed as a missing sale, not a missing row.**

| repo | grant (payload · bytes · ref · SHA-14) | release ladder | role in a build |
|---|---|---|---|
| 🆕 p98 [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) | 🟢 **MIT** · `LICENSE` **1 120 B** · `main` · `5695878b4735ed` | 🔴 **0 tags** → `UNRELEASED` (`P985`) | 🟢 **`Gap 372`'s seam in one repository**: writes the grade at `workflowstate=readyforreview` and never releases it. `grading-draft-gate` proves the three properties offline, **37/37**, with negative controls. |
| 🆕 p98 [`juneyaooo/lineage-skill`](https://github.com/juneyaooo/lineage-skill) | 🟢 **Apache-2.0** · `LICENSE` **11 358 B** · `main` · `7e2cbc5dc31713` | 🔴 **0 tags** | Carried by `aiact-50-2-marking`. 🔵 **11 358 B in a repository refines `P992`:** the count is not an `apache.org`-only artefact, so byte-equality against upstream remains the wrong modification test for a second reason. |

## 🟢 🆕 p98 Tier 4 — the skills-taxonomy layer, because `Gap 386` proved this KB could not price an L&D engagement

🔵 **`Gap 386` measured that every market figure on `intel/market.md` was institutional.** 🟢 **A buyer
with no supply tier is a gap in this file, not only in that one** — so the tier exists now.

| repo | grant (payload · bytes · ref · SHA-14) | release ladder | region | role in a build |
|---|---|---|---|---|
| 🆕 p98 [`nestauk/ojd_daps_skills`](https://github.com/nestauk/ojd_daps_skills) | 🟢 **MIT** · `LICENSE` **1 095 B** · `dev` · `e73c2b5045793d` | 🟢 **8 tags**, `v3.0.0` | 🟢 **EMEA** — *"Copyright (c) 2024, Nesta"* (UK), off the grant (`P800`) | 🟢 **The one to standardise on.** Skill phrases out of free text, mapped onto **ESCO**, **Lightcast Open Skills** or a custom taxonomy — 🔵 **the taxonomy is a parameter**, which is what survives a change of client and jurisdiction. |
| 🆕 p98 [`KonstantinosPetrakis/esco-skill-extractor`](https://github.com/KonstantinosPetrakis/esco-skill-extractor) | 🟢 **MIT, read from the BODY** · **1 068 B** · `master` · `cf2877d462f99a` | 🔴 **0 tags** | 🔵 unplaced (holder is a person) | ESCO skills **and** ISCO occupations by embedding similarity. PyPI + Docker. 🟡 **Titleless MIT payload** — second instance here after `Montreal-Forced-Aligner` (p97) — and 🔴 **curly quotes in the grant text** (`P998`). |
| 🆕 p98 [`dkavargy/ESCOPlus2.0`](https://github.com/dkavargy/ESCOPlus2.0) | 🟢 **MIT** · **1 086 B** · `main` · `88338a7cc196c8` | 🔴 **0 tags** | 🟡 **EMEA, weakly** (Aristotle University of Thessaloniki lineage) | Extends and validates **the taxonomy itself** from live job-ad data. 🔵 **The maintenance end — ESCO ages, and nothing else here addresses that.** |

🔴 **The trap, and it is `Gap 385`'s trap again.**
[`workforce-data-initiative/skills-ml`](https://github.com/workforce-data-initiative/skills-ml), the
Open Skills Project's flagship and the first result anyone reaches, is **`NONCOMMERCIAL-NOT-OSI`**:
`LICENSE.md` **1 976 B**, `master` · `feffead90815ccd`, *"Copyright ©2018. The University of
Chicago"*, use granted *"for educational and not-for-profit research purposes"*, which **"excludes
any service or part of selling a service that uses the Program"**. 🔵 **`P999`: the same university
template as `dssg/student-early-warning`. The two highest-ROI institutional use cases in this
industry share one licensing office.** 🔴 **A search key, never a verdict — `P975` governs.**

🟡 **Costing term: two of the three permissive rows have ZERO tags.** This tier is a build
commitment, not a product integration (`P985`).

## 🟢 🆕 p98 Tier 5 — credentialing, and the seam that repeats `Gap 372`'s exactly

🔵 **Tier 1 already carried `1EdTech/openbadges-validator-core` (Apache-2.0) and the ungranted
specification. This is the product end.**

| repo | grant (payload · bytes · ref · SHA-14) | release ladder | role in a build |
|---|---|---|---|
| 🆕 p98 [`CredentialEngine/Open-Badge-Publisher`](https://github.com/CredentialEngine/Open-Badge-Publisher) | 🟢 **Apache-2.0** · **11 357 B pristine**, 🟢 4 of 4 clause headings (`P974`) · `main` · `278b9d7dc084a6` | 🔴 **0 tags** | 🟢 **The only permissive row in the layer.** Publishes badge descriptions to the Credential Registry. 🔴 **No `NOTICE` → no holder → no region from the payload.** |
| 🆕 p98 [`nfh-trust-labs/opencred`](https://github.com/nfh-trust-labs/opencred) | 🟢 **MIT** · **1 071 B**, *"Copyright (c) 2026 NFH Trust Labs"* · `main` · `0fd0a9c65356db` | 🟢 **30 tags**, `v1.9.1` | Local-first **W3C VC** issuer/verifier; issuer keys never leave the host. 🔵 **The permissive issuing option is the generic VC one, not the Open Badges one.** |
| 🔴 p98 `19otherrsh-dot/Opencred` | 🔴 **AGPL-3.0** · 34 523 B · `main` · `d14619e186ed08` | — | OB3 + `did:web` + status-list revocation. 🔴 **Same NAME as the MIT row above, different repository, opposite licence** (`P1000`). |
| 🔴 p98 `Schroedinger-Hat/certo` | 🔴 **AGPL-3.0** · 33 820 B · `main` · `6fd0a11fe2ff61` | — | OB3 on Strapi/Nuxt, bulk CSV issuance. |
| 🔴 p98 `LongsightGroup/credtrail-app` | 🔴 **AGPL-3.0** · 34 523 B · `main` · `948a8ca43f3f33` | — | OB3, Ed25519, `did:web`. |
| 🔴 p98 `CoopCodeCommun/pyopenbadges` | 🔴 **LGPL-3.0** · 26 526 B · `main` · `e38e1894fd9bce` | — | Python OB3 create/validate library. |

🔵 **`P1001`.** Scoring: validation Apache/BSD, scorer AGPL (`Gap 372`, p94). Credentialing: validate
and publish permissive, **mint copyleft, 4 of 5** (p98). 🔵 **Two independent layers, same seam, same
side — stated as a falsifiable rule: the permissive grant sits on the side that MEASURES, copyleft on
the side that becomes the RECORD.** 🔴 **Engagement shape, not trivia: build the measuring side, draw
the boundary at the record, and let the client own the record.**

### 🔴 🆕 `P1002` — a secondary source's licence claim inherits the FRAMEWORK's grant, and it is a 50 % oracle

🔴 **A 2026 listicle names `frappe/lms` as the one MIT-licensed open-source LMS.** The payload says
**AGPL-3.0**: `license.txt` (lowercase), **33 893 B**, `develop` · `933fc6078cfa31`. 🟢 **And the
mechanism is readable:** `frappe/frappe`, the framework underneath, **is** MIT (`LICENSE` 1 118 B,
*"Copyright (c) 2016-2021 Frappe Technologies Pvt. Ltd."*).

🟡 **Measured in both directions, 2 of 2, and it is right once:** `openeducat/openeducat_erp` is
**LGPL-3.0** (`LICENSE` **8 241 B**) on an LGPL Odoo base, so there the inheritance holds.
🔵 **A 50 % oracle is not an oracle** — and 🔴 **the failure direction is the expensive one, because
the framework is the more permissive of the pair.**

🔴 **Two further facts from the same read, both carried as named unknowns rather than verdicts:**
`openeducat`'s `LICENSE` **delegates copyright to a `COPYRIGHT` file** (`P984`'s shape in a second
repository) and 🔴 **that file was not read — `raw.githubusercontent.com` returned HTTP 429 exactly
there** (`Gap 388`). 🔴 **And `openeducat`'s default branch is `19.0`** — a release number, not
`main`.

## 🟢 🆕 p96 `UniTime` — a verified permissive platform that lived in `compose/code/` and on no shelf page

| repo | grant (payload · bytes · ref · SHA-40 prefix) | version | layer |
|---|---|---|---|
| 🆕 p96 [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** · `LICENSE` **11 357 B** *(pristine upstream text)* · `master` · `15668a5e54d155` | 🟢 `pom.xml` **`4.9`** · **101 tags**, newest **`v4.9.152`** | 🟢 **University timetabling, course and student scheduling** — Apereo Foundation. **A layer the permissive tier had nothing for.** |

🔴 **It appears on no shelf page, while `compose/code/unitime-mcp-gate/` has carried a tested MCP gate for
it since pass 42** — re-audited in pass 45 against the four controls written for SEB Server, passing 15/15
on the literal-path control. 🔵 **The KB held the integration and never listed the platform. Nothing
reconciles the `compose/code/` inventory against the shelf**, which is `Gap 381`.

🔴 **The costing term that must travel with the row: `NOTICE` is 22 526 B and HTTP 200.** Apache-2.0 §4(d)
makes propagating NOTICE a condition of redistribution, so **a deliverable built on UniTime ships a 22 KB
attribution file.** 🔵 **Cheap to satisfy, expensive to discover in procurement review** — and this is the
same oracle class as `P917` (Fedena's grant living only in `NOTICE`), used here for an obligation rather
than for a grant.

🟢 **`P986` — `UniTime` is the first JVM row on this shelf to INVERT `P978`.** Its `pom.xml` declares
**`4.9`** and its newest tag is **`v4.9.152`**: the default branch names a **shippable line**, not a
`-SNAPSHOT`. Sakai (`27-SNAPSHOT` vs `25.2`), Opencast (`21-SNAPSHOT` vs `20.4`) and OpenOLAT
(`21.2-SNAPSHOT` vs `OpenOLAT_21.0.3`) all do the opposite. 🔵 **`P978` is a strong tendency, not a law,
and UniTime is the one JVM platform on this shelf you can quote a version for without a caveat.**

## Licence flags in this tier — the traps

| repo | grant | why it matters |
|---|---|---|
| [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** · `LICENSE.txt` 35 146 B · `master` · `cb64a1f` | 🔴 **H5P's core is GPL.** The interactive-content ecosystem everyone reaches for is copyleft at the library level. Use `tunapanda/h5p-standalone` (MIT) for playback instead of linking this. |
| [`lumieducation/H5P-Nodejs-library`](https://github.com/lumieducation/H5P-Nodejs-library) | 🔴 **GPL-3.0** · 35 146 B · `master` · `ac2d6aa` | 🔴 The Node port is GPL too. There is no permissive H5P *authoring* server. |
| [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | 🔴 **GPL-3.0** · 35 141 B · `master` · `5fec948` | 🔴 The best-known LRS is GPL. `yetanalytics/lrsql` (Apache-2.0) is the permissive substitute, and it is the better-maintained one. |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | 🔴 **AGPL-3.0** · 36 983 B · `master` · `d1e44b4` | 🔴 Excellent adaptive-assessment engine (UIUC), AGPL — network copyleft, so hosting it for a client triggers reciprocity. |
| [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** · 34 764 B · `main` · `8f90cc8` | 🔴 UCLouvain autograder, AGPL. |
| [`GatorEducator/gatorgrader`](https://github.com/GatorEducator/gatorgrader) | 🔴 **GPL-3.0** · `LICENSE.md` 35 191 B · `master` · `3be3278` | 🔴 |
| [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) | 🔴 **GPL-3.0** · 35 147 B · `main` · `61b5d8f` | 🔴 The LMS-integrated accessibility checker. GPL, and not AI-driven. 🆕 **But it is no longer the only option** — three permissive AI WCAG checkers are now shelved in `agents/top.md`. |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 **GPL-2.0** · 18 025 B · `develop` · `d9d462a` | 🔴 **CORRECTED this pass — it was published here as "LGPL-3.0 · linkable" and it is not.** TAO (Open Assessment Technologies, Luxembourg) is the serious QTI assessment platform and **the most mature one in this inventory**, so this is the row most likely to be costed. **GPL-2.0 is full copyleft: a fork shipped to a client carries reciprocity, and there is no LGPL linking exception to rely on.** Integrate across a process or network boundary, or budget for the obligation. 🔵 Also **GPL-2.0-only** — one-way incompatible with GPL-3.0 code. |

## 🆕 ADL leaves its own specs ungranted — now measured at three of five

🔴 **The US DoD's Advanced Distributed Learning initiative *authored* SCORM. Three of its repos carry no
licence payload in 24 filenames, while two carry Apache-2.0.** This was one row in pass 89's `Gap 354`; it is
now a pattern inside a single publisher:

| ADL repo | grant | ★ |
|---|---|---|
| [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) | 🟢 **Apache-2.0** · 11 324 B | 42 |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | 🟢 **Apache-2.0** · 11 357 B | — |
| [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | 🔴 **no payload / 24** · `master` · `3e532b8` | 99 |
| 🆕 [`adlnet/SCORM-2004-4ed-Test-Suite`](https://github.com/adlnet/SCORM-2004-4ed-Test-Suite) | 🔴 **no payload / 24** · `master` · `050f1b4` | 18 |
| 🆕 [`adlnet/SCORM-to-TLA-Roadmap`](https://github.com/adlnet/SCORM-to-TLA-Roadmap) | 🔴 **no payload / 24** · `master` · `da1b9a2` | 7 |

🔵 **Why this is worth a table.** Pass 89 read the single `SCORM-to-xAPI-Wrapper` negative as *"one missing
file, not a policy"*, on the reasoning that its Apache-2.0 sibling proved intent. 🔴 **Three of five says the
opposite: inside this publisher, grants are applied to the *profile and the server* and omitted from the
*wrapper, the conformance test suite and the roadmap*.** The omission tracks a category — reference
implementations and documents — not an oversight. 🔴 **Practical effect: the official SCORM 2004 conformance
test suite cannot be redistributed in a client deliverable.** Conformance must be demonstrated against
`ADL_LRS` (Apache-2.0) instead, which is what `P91-B` does.

## Other no-grant rows in this tier

| repo | status |
|---|---|
| [`1EdTech/openbadges-specification`](https://github.com/1EdTech/openbadges-specification) | 🔴 **No payload / 24** · `develop` · `04c4bc2`. The *specification* carries no grant while the *validator* is Apache-2.0. Cite the validator. |
| [`eecs-autograder/autograder.io`](https://github.com/eecs-autograder/autograder.io) | 🔴 **No payload / 24** · `master` · `5af4960`. 🔵 Consistent with its own README — a docs/issue tracker, not the code. Not a defect, but not a dependency either. |

## Slugs that do not exist

🔴 Re-confirmed `ABSENT` this pass. Recorded so they are not re-tried:

- `apereo/opencast` → 🟢 the real slug is [`opencast/opencast`](https://github.com/opencast/opencast)
- `tutor-dev/tutor` → 🟢 the real slug is [`overhangio/tutor`](https://github.com/overhangio/tutor)
- `h5p/h5p-standalone` → 🟢 the real slug is [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone)

## Count, stated plainly

🆕 **p97: 48 foundational rows above the flag line, 7 of them added or promoted this pass** —
`Montreal-Forced-Aligner` and `charsiu` (🟢 **genuinely new**), plus `HiPAMA` (new) and
`OpenPronounce`, `gopt`, `open-apa`, `kaldi` (🔵 **promoted from the history, not discovered**).
🟢 **47 are permissive for the CODE** (MIT / Apache-2.0 / BSD / CC0); **1 is LGPL**
(`celtic-project/LTI-PHP`).

🔴 **The qualifier on this count is sharper than on any previous one, and it has to be read:**
only **3 of the 7** are new measurements of new repositories. **4 are rows this KB measured at pass 14
and never put on a shelf page** — `Gap 384`. 🔵 **So the row count went up by 7 while the amount of
new knowledge went up by 3**, and a reader comparing pass 96's 41 to pass 97's 48 would otherwise
over-read the difference by more than double.

🟢 **All 7 were read from the payload this pass** at the 40-character SHAs named in Tier 2g — the
promotions were **re-measured, not copied forward from the history**, which is what makes them
publishable here. 🔴 **The other 41 rows are carried**, under exactly the bound pass 96 established
below.

🔵 **And three of the 7 are negatives rather than rows**, kept inside the tier so the denominator is
visible: `speechocean762` and `Phonos` carry **no licence payload** (`P994`), and `Phonos` is a
🔴 **correction** — this KB had counted it inside a permissive layer.

🔵 **Pass 96's count, kept because its bound still governs the 41 carried rows:**

🆕 **p96: 41 foundational rows above the flag line, 5 of them added this pass** (`OpenRS`, `OpenRubrics`,
`rubricbench`, `awesome-rubric-rewards`, `UniTime`). 🟢 **40 are permissive for the CODE**
(MIT / Apache-2.0 / BSD / CC0); **1 is LGPL** (`celtic-project/LTI-PHP`). 🔵 **Same qualifier as every
count on this page: a 5-row measurement on top of a 36-row inheritance, not a 41-row measurement.** The
five new rows were read from the payload at the **full 40-character SHAs** named; the other 36 are carried.

🟢 **But for the first time the inheritance is not simply trusted — it is bounded.** `Gap 376` said the
denominator was decaying and could not say by how much. Measured this pass over **127 published
`(slug, ref, sha7)` triples** harvested from all six shelf pages:

| verdict | n | what it licenses you to say |
|---|---|---|
| 🟢 `CURRENT` — pinned SHA still the tip of the pinned ref | **122** | 🟢 **the row cannot have drifted** |
| 🔴 `MOVED` | **5** | re-read this pass; **all 5 kept their grant** |
| `NO-REACH` | **0** | every slug resolves |
| `REF-GONE` | **0** | every published ref still exists |

🔵 **So the honest claim about this page's inheritance is: 96.1 % of it is provably at the SHA it was
measured at, and the 3.9 % that moved was re-read.** 🔴 **It is still NOT a re-verification.** A current
SHA says nothing about whether the 24-name filename reach or the classifier behind that row was sound —
**and that is exactly and only what `grant-ladder-v4` can settle.** 🟢 **`Gap 376` keeps its priority and
loses its vagueness.**

🔵 **Pass 95's own sentence, kept because it still governs the reading:**

🆕 **p95: 36 foundational rows above the flag line, 2 of them added this pass** (`girth_mcmc`,
`otter-grader`). 🟢 **35 are permissive for the CODE** (MIT / Apache-2.0 / BSD); **1 is LGPL**
(`celtic-project/LTI-PHP`). 🔵 **And the same qualifier the p94 count needed: this is a 2-row measurement on
top of a 34-row inheritance, not a 36-row measurement.** Both new rows were read from the payload at the
SHAs named; the other 34 are carried and were **not** re-read. 🔴 **See `Gap 376` — three consecutive
passes of ~12 hand-read rows against a 133-row census is a decaying denominator, and it is now the most
important thing on this page to fix.**

🔵 **Pass 94's own sentence, kept because it still governs the reading:**

**34 foundational rows above the flag line, 3 of them added this pass** (`rsmtool`, `skll`,
`NodeGrade`). 🟢 **33 are permissive for the CODE** (MIT / Apache-2.0 / BSD); **1 is LGPL**
(`celtic-project/LTI-PHP`). 🔵 **Pass 93's own sentence, kept because it still governs the reading:**

**31 foundational rows above the flag line, 9 of them added this pass.** 🟢 **30 are permissive for the
CODE** (MIT / Apache-2.0 / BSD); **1 is LGPL** (`celtic-project/LTI-PHP`).

🟡 **And one qualifier the previous counts did not need.** **3 of the 31 carry a CC BY 4.0 obligation on
their DATA** — the three `bncc-dev` rows. CC BY 4.0 is an **attribution duty, not a copyleft one**, so it
does not move those rows below the flag line; but **counting them as plainly "permissive" without naming
the data grant is precisely the elision `P969` exists to punish.** Named here instead.

🔵 **What the headline number does and does not mean.** 9 rows were resolved from the payload this pass;
**the other 22 are carried at their pass-92 SHAs and were not re-read.** So this is not a 31-row
measurement — it is a 9-row measurement on top of a 22-row inheritance, and the next pass that can run
`grant-ladder-v4/ladder.sh` should re-derive all 31 and disagree with this page on the record if it finds
cause.

🟢 **The standing finding survives a fifth measurement, and widens:** the interoperability, assessment,
learner-model and now **psychometric** tiers are the permissive heart of this industry. 🔵 **Pass 93's
addition to that claim is a ranking, not just a row count:** within the learner-model tier, the
*permissive* and the *explainable* options turn out to be the same ones — BKT, IRT and CAT are all
MIT/BSD **and** all produce a parameter you can defend in an Annex III audit, while the copyleft and the
black-box options sit together at the other end.

🔴 **One honest subtraction from pass 91's count, carried forward.** Pass 91 reported *"19 of 20
permissive, 1 LGPL"*. That line was true of the page as it stood **only because `oat-sa/tao-core` was
misfiled as LGPL-3.0**; it sits below the flag line either way, so that headline was unchanged by the
correction — but the LGPL row it referred to is `celtic-project/LTI-PHP`, and **`tao-core` was never one
of the 20.** Stated rather than silently re-tallied.

## Open gaps on this page

- 🔴 🆕 **`Gap 370` — the ladder cannot see a per-directory licence.** `compose/code/p199-perfile-license/`
  already does per-path probing and is not wired into `grant-ladder-v4`. Failing case ready:
  `bncc-dev/bncc-dados` → root `LICENSE` MIT, data `dados/LICENSE.md` CC BY 4.0, root `LICENSE-DADOS.md`
  404. See `P969`.
- 🟡 🆕 **p94: `Gap 372` narrowed to the scorer.** The validation half exists and is permissive (Tier 2d);
  the production scoring code is AGPL-3.0 (`openedx/ease`, `openedx/edx-ora2`). **What is missing is a
  permissive production-grade scorer for open-response work** — and nothing else.
- 🔴 🆕 **p94: `Gap 375` — this shelf has 3 payload-derived platform versions and the rest are prose.**
  Moodle (`5.3` stable / `6.0dev`), Artemis (`10.3`) and Open edX (`release/ulmo.4`, Tutor `v22.0.2`) were
  read this pass; every other version string in the platform tier still comes from a README or a blog.
  `P972` makes the fix mechanical, so this gap is work, not uncertainty.
- 🟢 🆕 **p95: `eribean/girth_mcmc` RESOLVED, after two passes as a named-and-unrun lead.** **MIT**,
  `0.6.0`, `LICENSE.txt` 1 061 B — triple-confirmed against `setup.py` and its OSI classifier. In **Tier
  2c**. 🟢 **All three estimators `catsim`'s README names are now permissive rows.**
- 🟢 🆕 **p95: `Gap 375` substantially discharged — 12 payload-derived platform versions, up from 3.**
  Nine were read this pass (`ILIAS` **`11.5 2026-10-06`**, Chamilo **`3.0.1`**, `frappe/lms` **`2.45.2`**,
  Gibbon **`31.0.00`**, OpenEduCat **`19.0.1.0`**, Mumuki **`9.23.0`**, `relate` **`2024.1`**,
  `classroomio` **`0.1.13`**, `otter-grader` **`7.0.0`**) plus four release ladders. 🟡 **What remains open
  is the permissive tier's smaller rows** (`pupilfirst`, `academico`, `open-tutor-ai-CE`), which were not
  probed.
- 🟢 🆕 **p95: `P978` — the default branch reports the DEVELOPMENT version.** Measured on four platforms:
  Sakai's root pom says `27-SNAPSHOT` against a newest tag of `25.2`; Opencast `21-SNAPSHOT` against
  `20.4`; OpenOLAT `21.2-SNAPSHOT` against `OpenOLAT_21.0.3`; Moodle `6.0dev` against `5.3` stable.
  🔴 **Publishing a default-branch version means publishing a release nobody can install.** Read both.
- 🔴 🆕 **p95: `Gap 377` — `pom.xml` / `build.gradle` are not in the grant ladder's path list.** Sakai's
  `pom.xml` names *"Educational Community License, Version 2.0"* and so independently confirms an ECL-2.0
  row that generic tooling returns as *unclassified* (`P979`). **A second concurring oracle for the licence
  family this tier most often loses. Cheap to add, and it pays on every JVM platform here.**
- 🔴 🆕 **p95: `Gap 378` — a probe that reads paths cannot follow an indirection.**
  `chamilo/chamilo-lms`'s `public/main/install/version.php` is HTTP 200 and its entire body is
  `return require dirname(__DIR__, 3).'/version.php';` — **a shim pointing back to the repository root**,
  where the real `3.0.1` lives. 🔵 **Moodle made the same `public/` migration and left a 404 instead.** Same
  shape as `Gap 370`: **this KB's probes read paths, and real projects indirect.**
- 🔴 🆕 **p95: `Gap 376` — the instrument has been unrunnable for three consecutive passes.**
  `grant-ladder-v4/ladder.sh` was denied before it started in passes 93, 94 and 95. 🟢 **The method is
  sound; the coverage is decaying.** **The next pass that can execute code must re-derive the full census
  before adding anything, and disagree with these pages on the record if it finds cause.**
- 🔴 **`Gap 369` carried.** Nothing on this shelf wires a knowledge-tracing model into an agent turn, so
  `pyBKT`/`pykt-toolkit` → agent is a build, not an integration. 🟡 **Pass 93 narrows it rather than
  closing it:** `P93-A` in `compose/patterns.md` now specifies that wiring concretely, but **no repository
  found this pass ships it**.

- 🟢 🆕 **p96: `Gap 377` ANSWERED — and the answer corrects the gap's own wording.** 🔴 Pass 95 wrote
  *"`pom.xml`/`build.gradle` are not in the grant ladder's path list … cheap to add, and it pays on every
  JVM platform here."* **Both halves needed amending.**
  🟢 **(a) Nothing needs writing.** `p289-maven-manifest/maven_license.py` (**11/11**, with its negative
  control for the `P171`-in-XML case) was wired into `p283/manifest_license.py::PARSERS` and into
  `sweep_named.sh`'s `MANIFESTS` by **`P294`**, and `build.gradle` already sits in
  `p172-payload-license-sweep`'s manifest list. 🔵 **`grant-ladder-v4` needs a one-line import — the only
  repair `P237` permits — not a new reader.**
  🔴 **(b) `build.gradle` is not a licence oracle.** `ls1intum/Artemis`, the best row on this shelf,
  declares **no licence in 52 855 bytes** of Gradle build script. 🔵 **The asymmetry is distribution
  policy, not language:** a `<licenses>` block is part of what Maven Central requires of a published POM;
  Gradle has no equivalent convention. **Add `pom.xml`; spend nothing on `build.gradle`.**
  🟢 **(c) And the oracle pays, measured at full SHAs on 4 of 4 Maven platforms** — `opencast` and `sakai`
  both declare *"Educational Community License, Version 2.0"* with the OSI URL, `UniTime` declares
  *"Apache Software License (ASL), Version 2.0"*, `OpenOLAT` declares the Apache URL. **ECL is the family
  generic tooling returns as *unclassified*, so a URL-grade identifier is worth more here than anywhere
  else on this page.**
- 🔴 🆕 **p96: `Gap 382` — the pom oracle reads `<name>` and the stronger field is `<url>`** (`P988`).
  **4 of 4 Maven platforms carry a canonical licence URL; 3 of 4 spell the name correctly** —
  `OpenOLAT`'s pom declares **"Apache 2.0 Open Source L6icense"**. 🟡 `p289` survives it anyway, because
  `lib/license_family.sh`'s *declaration* branch keys on bare `apache` where its *title-block* branch
  requires `Apache License` — 🔵 **the coarse branch being the correct one, which is `P637`'s `CONTRATO`
  class observed in the wild rather than constructed.** 🟢 **Reading `<url>` makes it right for the right
  reason.** Cost: one XPath sibling.
- 🔴 🆕 **p96: `Gap 380` / `P987` — this KB addresses payloads by abbreviated SHA and the abbreviation does
  not always resolve.** `raw.githubusercontent.com/Submitty/Submitty/` + the **full 40 characters** →
  **200**; + **`ff82521`** → **404**; *same object*, same pass — while the previous 7-char SHA on the same
  repo resolved fine, so it is **inconsistent per commit**, which fails silently. 🔴 **An unresolved
  abbreviation 404s all 24 filenames and reads exactly like `no licence payload`.** 🟢 **`P872` caught the
  one occurrence** (the `README.md` control 404'd too, so the sweep was discarded) 🟢 **and the blast radius
  was measured rather than assumed: all 10 published no-payload rows return a 200 control at their
  published SHA — 0 of 10 are artefacts.** 🔵 **Publish the abbreviation for a human; address the payload
  with the full 40.** `grant-ladder-v4` carries the defect today.
- 🟢 🆕 **p96: `Gap 375` FULLY DISCHARGED — the remainder is *unmeasurable*, and the mechanism is named.**
  Pass 95 left `pupilfirst`, `academico` and `open-tutor-ai-CE` unprobed. **All three serve their manifest
  at HTTP 200 with no version field**, and the reason is structural: two declare `"private": true`, the npm
  convention for a workspace root that is never published to a registry, and a package never published has
  no registry version. 🟢 **`P985` splits "no version" into three facts that price differently** —
  `UNVERSIONED-BUT-RELEASED` (`open-tutor-ai-CE`, 1 tag, ship `v1.0.0`), `COMPONENT-VERSIONED`
  (`pupilfirst`, 57 tags **all scoped npm sub-packages**, so the platform has never shipped as a unit) and
  `UNRELEASED` (`academico`, **0 tags**). 🔴 **And the third lands on this KB's most-repeated
  recommendation:** `academico-sis/academico` is *"the closest thing to a permissive SIS"* — 404 ★, MIT
  declared in both `composer.json` and the payload, **and no release ladder at all.** 🔵 **A fork inherits
  release engineering, a version scheme and an upgrade path that do not exist.**
- 🟡 🆕 **p96: `Gap 379` — the rubric layer is permissive and nothing binds it to a curriculum standard.**
  Tier 2f above has the judge (`OpenRS`, Apache-2.0), the generator (`OpenRubrics`, MIT) and the calibrator
  (`rubricbench`, MIT); Tier 1b has **1 721 verified BNCC objectives** behind MCP (MIT code + CC BY 4.0
  data). 🔵 **Four permissive layers, three publishers, no integration — `Gap 369`'s exact shape.**
  Specified as `P96-A`.
- 🔴 🆕 **p96: `Gap 381` — nothing reconciles `compose/code/` against the shelf.** `UniTime/unitime` is
  **Apache-2.0** with a pristine 11 357 B payload and 101 release tags, this KB has carried a tested MCP
  gate for it since **pass 42**, and it reached no shelf page until this one. 🔵 **A verified asset can sit
  in the evidence directory indefinitely without ever being offered to a client.**
- 🟡 🆕 **p96: `Gap 378` has a THIRD form, and it is in a licence file** (`P984`).
  `chamilo/chamilo-lms` serves `license.txt` **1 614 B** beside the 35 147 B `LICENSE` this KB read, and the
  small file says *"The full license can be read in `documentation/license.html`"* — **a third location.**
  🟢 **It also yields two facts the big file does not:** the grant is **GPL-3.0-or-later**
  (*"or (at your option) any later version"* — this shelf publishes bare `GPL-3.0`, and `P561` makes a
  dropped qualifier a defect), and **12 copyright holders in 5 countries with `BeezNest Latino SAC, Peru`
  FIRST** (`P800`). 🔵 **`P984`: when a repo serves two licence files of very different sizes, the SMALL one
  has the facts; the large one is the canonical upstream text and says nothing project-specific.**
  🔴 **A first-match ladder ordered `LICENSE` before `license.txt` reads the uninformative file and stops.**
- 🟡 🆕 **p96: `Gap 376` BOUNDED, priority UNCHANGED.** Four consecutive passes without the instrument;
  **122 of 127 rows provably un-drifted and the 5 that moved re-read and unchanged.** 🔴 **Still not a
  re-verification** — filename reach and classifier soundness are untested by a SHA probe, and only
  `grant-ladder-v4` settles them. **The first duty of the next pass that can execute code is still
  corrective.**

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
