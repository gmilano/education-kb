---
industry: education
region: Global
updated: 2026-10-26
---

## 🆕 `p455` — **🟢 A VERTICAL SHAPE THESE SHELVES HAD ONLY ONE INSTANCE OF NOW HAS FOUR: the closed national school system reachable only through third-party clients. France and the DACH countries together, eleven permissive clients, zero customisable cores.**

🔴 **`make hooks` DENIED** (`Code from External`) — tenth denial in eleven passes.

### 🟢 The shape, and why it is a different engagement from Moodle or Open edX

`p453` recorded *"a market shape these shelves had never recorded: a closed national system of
record reached only by third-party clients"*, and `p454` added Indonesia's **Dapodik** as the APAC
instance. This pass establishes that the shape is **the norm across Western Europe**, not an
exception — and that it inverts the economics of every other row on this file.

🔵 **Moodle, Open edX, Kolibri, OpenEduCat and Sakai are platforms you install and extend.**
The systems below are platforms a ministry or a *Land* has already installed, that **cannot be
forked, hosted or extended**, and whose only integration surface is an API — usually undocumented
— wrapped by community clients. The sellable work is therefore an **agent or integration layer
against a system of record you do not control**, never a platform customisation.

| national system | country / scope | status | permissive client tier read first-hand this pass | what it exposes |
|---|---|---|---|---|
| 🔴 **PRONOTE** (Index Éducation) | 🇫🇷 France — the gradebook/timetable of most secondary schools | 🔴 **Proprietary, closed.** No open core at any address | 🟢 [`bain3/pronotepy`](https://github.com/bain3/pronotepy) **MIT** (`1 062` B `4f074ab7dccb`), 🟡 maintenance mode | Grades, timetable, homework, attendance for student/parent/teacher accounts. 🔴 Not the official HYPERPLANNING API |
| 🔴 **EcoleDirecte** | 🇫🇷 France — the second school portal | 🔴 Proprietary, closed | 🟢 [`studoo-app/ecole-directe-api`](https://github.com/studoo-app/ecole-directe-api) **MIT** (`1 071` B `6c086a4639ac`); 🟡 [`a2br/ecoledirecte.js`](https://github.com/a2br/ecoledirecte.js) **MIT** (`1 073` B `e4ba09041791`), unmaintained since 2023-08-08 | Login (incl. 2FA on some clients), grades, timetable, homework |
| 🔴 **Schulportal Hessen** ("Lanis") | 🇩🇪 Germany — the *Land* of Hesse's statewide portal | 🔴 Proprietary, closed, and 🔴 **maintainer-documented as fragmented**: functions *"at specific schools or after a while may no longer work"* | 🟢 [`kurwjan/LanisAPI`](https://github.com/kurwjan/LanisAPI) **MIT** (`1 076` B `0bc449776673`, **@`master`**); 🔴 [`lanis-mobile/lanis-rs`](https://github.com/lanis-mobile/lanis-rs) + [`elderguardian/maria`](https://github.com/elderguardian/maria) both **GPL-3.0 `or-later`** (`35 149` B `3972dc9744f6`) | Homework, substitution plans, calendar, conversations, substitute-teacher plan |
| 🔴 **WebUntis** (Untis GmbH) | 🇦🇹🇩🇪🇨🇭 DACH — the dominant school timetabling system | 🔴 Proprietary, closed. 🔵 **Has a public JSON-RPC API *and* an internal one**, and the client tier splits on which it uses | 🟢 [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) **MIT** (`License`, `1 070` B `d2e54565d9bf`) · [`Tynobi-Company/webuntis_headless`](https://github.com/Tynobi-Company/webuntis_headless) **MIT** · [`thatmarcel/untis-js`](https://github.com/thatmarcel/untis-js) **MIT** · [`Suiram1701/WebUntisAPI.Client`](https://github.com/Suiram1701/WebUntisAPI.Client) **MIT** (.NET) · [`Keule0010/WebUntisAPI`](https://github.com/Keule0010/WebUntisAPI) **MIT** (Java) · 🔴 [`arnim279/untis-api-client`](https://github.com/arnim279/untis-api-client) **GPL-3.0-or-later** (public API) | Timetables over date ranges, lesson detail, sessions |
| 🟡 **Librus Synergia** | 🇵🇱 Poland — *(carried, re-stated here for the shape)* | 🔴 Proprietary, closed | 🟡 [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) **MIT at root** — 🔴 **GPL-3.0 on its `legacy_reference/` subtree**: integrate over MCP, never vendor the tree | Grades, attendance, timetable, homework, messages |

### 🔴 Three constraints this tier carries that a platform engagement does not

🔴 **(1) A stated rate limit, and it is the only one on this file.**
`Suiram1701/WebUntisAPI.Client`'s own documentation sets it: never 10 req/s, no more than
1 800 req/h, **in no case above 3 600 req/h**, and exceeding it *"could permanently block"* the
institution's access. 🔵 That is an architectural constraint on any agent that polls — a per-tenant
scheduler and cache is not an optimisation here, it is a precondition.

🟡 **(2) The client tier is unofficial by construction, so it breaks when the vendor moves.**
`pronotepy` is in maintenance mode *because* of this; `ecoledirecte.js` was abandoned for it;
LanisAPI's maintainers say the portal is fragmented per school. 🔵 A deliverable must treat the
client as a **replaceable adapter**, and the engagement must price a maintenance tail.

🔴 **(3) Copyleft is distributed unevenly across the tier, and it decides the architecture.**
Every WebUntis and French client above is **MIT** except `untis-api-client`, which is
**GPL-3.0-or-later** — and it is the only one on the *public* API. 🟡 So the permissive path and
the documented-API path are **different repositories**: a vendorable deliverable takes the MIT
clients on the internal API and accepts the fragility, or takes the GPL client on the public API
and keeps it behind a service boundary. 🟢 The `or-later` grant, read first-hand, means that
boundary may itself be GPL-3.0.

## 🆕 `p454` — **🟢 A national system of record this base had never named is customisable from MIT code: Indonesia's Dapodik, reached at three strata. 🔴 And the vertical layer gains a licence SHAPE that no single SPDX field can express — the three-strata grant, found independently in Brazil and Indonesia in the same hour.**

🔴 **`make hooks` DENIED** (`Code from External`) — ninth denial in ten passes.

### 🟢 Dapodik — Indonesia's national education register, as a customisable base

🔵 **Dapodik** (*Data Pokok Pendidikan*, `dapo.kemendikdasmen.go.id`) is the Ministry of Primary
and Secondary Education's single register of schools, teachers and students. Like ÉcoleDirecte
(EMEA, `p453`) it is a **closed national system of record with no open core** — but unlike
ÉcoleDirecte, its client layer is **MIT across three languages and three strata**:

| stratum | asset | grant (first-hand, `HEAD`) | what it gives an engagement |
|---|---|---|---|
| register access | [`ardianryan/dapodik-sdk`](https://github.com/ardianryan/dapodik-sdk) | **MIT** · `1 739` B `29e7d361ee3d` | typed TS/JS SDK over the Dapodik web service |
| register access | [`adereksisusanto/dapodik-api-php`](https://github.com/adereksisusanto/dapodik-api-php) | **MIT** · `1 105` B `ce39902853af` | PHP client, CI-tested — the stack most Indonesian school software is written in |
| student identity | [`smantriplw/vervalpd-node`](https://github.com/smantriplw/vervalpd-node) | **MIT** · `1 068` B `0ae5076b1e03` | VerValPD lookups (`findStudent`) over an undocumented API |
| aggregate reporting | [`bantenprov/dapodik-data-guru`](https://github.com/bantenprov/dapodik-data-guru) | **MIT** · `1 072` B `3508ba25c5ad` | provincial teacher-data recapitulation |

🟡 **Read the stratum honestly before selling it.** `vervalpd-node` describes itself as a
**scraper of a non-documented API**. That is a real integration path and a real fragility: it is
not a supported contract, and an engagement that depends on it owes a change-detection test, not
an SLA.

### 🔴 The three-strata grant — a vertical-layer shape, found twice in one hour

🔵 Two unrelated education projects, on two continents, independently split their grant the same
way — and **neither split is expressible in a registry's single `license` field**:

| project | code | content / data | name & brand |
|---|---|---|---|
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) *(LATAM, Brazil)* | 🟢 **MIT** (`LICENSE-CODIGO.md`) | 🟡 **CC BY 4.0** for the BNCC curriculum JSON (`LICENSE-DADOS.md` `1 108` B `965ba269fac6`) | 🔴 *"não licenciados"* — wordmark, logo, colours explicitly withheld |
| [`nakafaai/aksara`](https://github.com/nakafaai/aksara) *(APAC, Indonesia)* | 🔴 **Source Available 2.0** (`11 997` B `97e8bdc2e3cd`) | 🔴 **Content License 2.0** (`10 053` B `2af44ab89691`) | 🔴 **Trademark Policy 2.0** (`4 508` B `3ba64345e201`) |

🟢 **Why education specifically.** A vertical that ships *curriculum* alongside *code* has two
different kinds of asset in one artefact, and content is not licensed like software. `bncc-pacotes`
states the consequence outright: the **npm tarball and the PyPI wheel carry MIT code and CC BY 4.0
data in the same artefact**. 🔴 A studio that vendors it on the registry's `MIT` badge therefore
inherits **attribution obligations it never read**, and the attribution string the project asks for
is specified in `LICENSE-DADOS.md`, not in the package metadata.

🟢 **Operational rule for this layer, and it is new:** for any education vertical, clear **three**
grants — code, content, brand — and record each one's bytes and digest separately. One SPDX value
per package is a category error here, not a shortcut.

### 🔵 Carried vertical rows, re-read at `HEAD`

🟢 [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) — **GPL-2.0, correctly declared**
(`18 025` B `a01259a1b522`). TAO remains the copyleft assessment platform on these shelves;
GPL-2.0 (not LGPL, as a reader defect this pass briefly reported) means **no proprietary
linking**.
🔴 `imsglobal/caliper-php` — **the address is DEAD, which is worse than the `MANIFEST_ONLY` this
pass first recorded.** Packagist declared `LGPL-3.0`; the Packagist record now **404s**; and the
repository itself returns `404` at `HEAD` on **all 13 non-licence paths probed** (`README.md`,
`composer.json`, `.gitignore`, …), as do both plausible successors `1EdTech/caliper-php` and
`IMSGlobal/caliper-php`. 🔴 **The IMS Global reference implementation of the Caliper analytics
standard is not retrievable from this address at all** — so it is not a licence question, and this
row is a dead citation, not a vertical option.
🔴 [`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) —
the fork that **does** serve one: **LGPL-3.0** (`7 438` B `8c401dfc8928`), against a carried cell
of `proprietary`. 🟢 For a Caliper engagement, this is the address to read.
🟢 [`edu-sharing/Edu-Sharing`](https://github.com/edu-sharing/Edu-Sharing) — **GPL-3.0**
(`35 148` B `8b1ba204bb69`), an OER repository/federation platform customisable with AI on top;
🔴 npm's `GNU GPL v2` hint is wrong and the two versions are incompatible.

## 🆕 `p453` — **🟢 The institution-registry layer `p452` opened with one country now spans two regions and three strata — national directory, federal statistical series and school-authored disclosure — and the US stratum is the one an engagement can actually build on. 🔴 And a vertical row is corrected in place: the French national SIS tier exists here for the first time, under a grant its own registry record states wrongly.**

🔴 **`make hooks` DENIED** (`Code from External`) — eighth denial in nine passes. Nothing here is
gate-attested; the load-bearing contracts were re-implemented independently and all are green.

### 🟢 The institution-registry vertical, now readable as a layer rather than a row

🔵 `p452` added `yasserstudio/geoalgeria` and wrote that the layer was *"one country deep"*. 🟢 It
is now three strata deep in two regions, and the strata are **not interchangeable** — an
engagement needs to know which question each answers.

| stratum | question it answers | instance, grant read first-hand | region |
|---|---|---|---|
| 🟢 **national directory** | *which institutions exist, by administrative unit* | [`yasserstudio/geoalgeria`](https://github.com/yasserstudio/geoalgeria) — **MIT** (1 101 B `691e4ec845d7`, carried from `p452`): 1 932 MFEP vocational establishments, 177 MESRS higher-ed, 11 858 schools, 69 wilayas | 🟢 **EMEA** — Algeria |
| 🟢 **federal statistical series** | *what is TRUE of each institution, longitudinally* | [`paulgp/ipeds-database`](https://github.com/paulgp/ipeds-database) — **MIT** (1 056 B `1126322e2cc8`): 27 M rows, 23 tables, 1997-2024; [`scienceforamerica/scipeds`](https://github.com/scienceforamerica/scipeds) — **MIT** (1 088 B `e04b31a1be21`) | 🟢 **North America** — US |
| 🟢 **school-authored disclosure** | *what the institution says about ITSELF, current year* | [`bolewood/collegedata-fyi`](https://github.com/bolewood/collegedata-fyi) — **MIT** (1 115 B `a3a16c648652`): 4 071 archived Common Data Set documents, 1 105-field canonical schema, 6 322-institution federal directory | 🟢 **North America** — US |
| 🟢 **administrative geography** | *the unit a school list JOINS to* | [`nataliasm23/icones-bandeiras-br-uf`](https://github.com/nataliasm23/icones-bandeiras-br-uf) — **CC0-1.0** (7 048 B `a2010f343487`) | 🟢 **LATAM** — Brazil |
| 🔴 **absent stratum** | *national directory, APAC* | 🔴 India's UDISE+-derived directories: **4 of 5 packaged forms grant nothing**, the fifth is **CC-BY-SA-4.0**. See `repos/foundations.md` | 🔴 **APAC** — recorded as an informed absence |

🟢 **Why the US stratification matters commercially.** The federal series and the school-authored
disclosure disagree by construction — IPEDS is the broad-coverage federal baseline, the CDS is the
current-year, school-authored admissions detail — and `collegedata-fyi` is the only row here that
keeps them **separately labelled** rather than blending them. 🔵 An engagement that silently
merges the two produces numbers no institution will confirm.

### 🟢 A new vertical tier: the national SIS that is NOT an LMS

🔵 Every platform row on this shelf until now runs a *course* (Moodle, Canvas, Open edX, Kolibri)
or an *institution* (OpenEduCat, openSIS, Gibbon, Fedena). 🟢 **ÉcoleDirecte is a third thing: a
French national school system of record for grades, homework, timetable and `vie scolaire`**,
reached only through client libraries, with no self-hostable open core at all.

| row | grant, read first-hand at `HEAD` | posture |
|---|---|---|
| [`androz2091/node-ecole-directe`](https://github.com/androz2091/node-ecole-directe) | 🔴 **Apache-2.0** — `LICENSE` **11 357 B `sha256₁₂ c71d239df917`**, title-anchored. 🔴 **npm declares `ISC`** on every version | 🟢 **Build-on.** Apache-2.0 is the *more* obligated of the two readings (NOTICE, change notices) and the one that actually governs; it also carries the patent grant `ISC` lacks |
| [`papillonapp/papillon-ed-core`](https://github.com/papillonapp/papillon-ed-core) | 🔴 **GPL-3.0** — 35 149 B `3972dc9744f6` | 🔴 **Watch only** — strong copyleft propagates into a client deliverable |
| [`louislegrain/api-ecoledirecte`](https://github.com/louislegrain/api-ecoledirecte) | 🔴 **`ISC` on npm, no payload at 9 paths** | 🔴 **Legal review first** — `Gap 451-C` manifest-only class, on a live package |

🔴 **The correction this tier forces on the shelf's own method.** These shelves have graded the
French market through *EU regulation* (Reg. (EU) 2026/1744, Pattern BC) and never through its
*systems of record*. A French engagement integrates ÉcoleDirecte or Pronote long before it reads
an Annex III deadline, and neither appeared on any shelf until this pass.

## 🆕 `p452` — **🟢 A vertical layer these shelves have never carried is now populated: the national INSTITUTION REGISTRY — the master list an engagement keys its rollout to, before any LMS is chosen. 🔴 And it exposes the shape of the gap: this base has eight platforms that run a school and almost no data about which schools exist.**

🔴 **`make hooks` DENIED** (`Code from External`) — seventh denial in eight passes. Nothing here is
gate-attested; the four load-bearing contracts were re-implemented by hand and all four are green.

### 🟢 The new row, read first-hand at `HEAD`

| asset | grant | layer | what it contains | region |
|---|---|---|---|---|
| [`yasserstudio/geoalgeria`](https://github.com/yasserstudio/geoalgeria) | 🟢 **MIT** — `LICENSE` **1 101 B `sha256₁₂ 691e4ec845d7`**. 🔴 the npm manifest declares only `SEE LICENSE IN LICENSE`, so the **payload** is the grant | 🟢 **Institution registry / reference data** — *new layer on this shelf* | **11 858** schools & kindergartens by cycle (primaire, CEM, lycée, préscolaire, from OpenStreetMap) · **1 932** vocational-training establishments (856 CFPA, 182 INSFP, 723 private accredited, 58 DFEPs — **MFEP / takwin.dz**) · **177** higher-education institutions (universities, grandes écoles, ENS, centres — **MESRS**) · all **69 wilayas**, with GPS, contacts, capacity and boarding · trilingual EN/FR/AR | 🟢 **EMEA** — Algeria |

### 🔴 The gap it makes visible, and it is a real asymmetry in this shelf

🔵 This file carries the platforms that **operate** an institution — Moodle (GPL-3.0), Open edX
(AGPL-3.0), Canvas LMS CE (AGPL-3.0), Sakai (Apache-2.0), Kolibri (MIT), OpenEduCat (LGPL-3.0),
BigBlueButton (LGPL-3.0), H5P (MIT). 🔴 **It carries almost nothing that says which institutions
exist.** Those are different buys and they arrive in a different order: a ministry or a group
engagement sizes and segments the estate *before* it selects a platform, and until this pass this
base could serve the second question and not the first.

🟢 **What the registry layer is worth in an engagement.** It is the join key. A rollout plan, a
territorial phasing, a capacity model, a per-wilaya cost estimate and a baseline for measuring
reach all key against the institution list; a permissive, ministry-sourced, GPS-bearing list is
the difference between a proposal with numbers in it and one without.

### 🟡 What this row is NOT, stated so no engagement over-reads it

🔴 It is **data, not software** — there is no API, no auth, no multi-tenancy and no runtime; it is
npm packages of records. 🔴 It is **one country**. 🔴 Its school tier is **OpenStreetMap-derived**,
so that 11 858 is a volunteer-mapped count and not a ministry census, while the vocational and
higher-education tiers **are** ministry-sourced (MFEP, MESRS) — 🟡 **the three tiers do not carry
the same authority and must not be cited as one figure.**

### 🔴 The rest of the layer, named as an informed absence rather than left silent

🟢 **Comparable permissively-licensed national education registries on these shelves, by region:**

| region | institution-registry asset carried | state |
|---|---|---|
| 🟢 **EMEA** | [`yasserstudio/geoalgeria`](https://github.com/yasserstudio/geoalgeria) — MIT, Algeria | 🟢 **new this pass** |
| 🟡 **LATAM** | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) — Brazil's **BNCC curriculum** as data (CC-BY-4.0); [`portabilis/i-educar`](https://github.com/portabilis/i-educar) — **GPL-2.0**, a municipal system, not a registry | 🟡 **curriculum data, not an institution registry** |
| 🔴 **North America** | — | 🔴 **none carried.** The US equivalents are federal/state series (NCES CCD, IPEDS); 🔵 whether a permissively-licensed packaged form exists has **not been searched** on these shelves |
| 🔴 **APAC** | — | 🔴 **none carried** |
| 🔴 **Global** | — | 🔴 **none carried.** UNESCO UIS publishes aggregates, not institution lists |

🔴 **Four of five regions have no institution-registry asset on this shelf, and three of those four
have never been searched for one.** 🟢 That is an informed gap and it is registered as
`Gap 452-D`: the layer is newly visible, one country deep, and the absence elsewhere is
unmeasured rather than established.

## 🆕 `p451` — **🔴 THIS FILE'S SIIAU ROW UNDERSTATED THE PROBLEM: it recorded the one existing SIS SDK as "abandoned", which is a maintenance fact. The licence fact is worse and is corrected here — FOUR of its seven published versions are `proprietary`, and only `v1.1.2` onward is BSD-3-Clause.**

🔴 **`make hooks` was DENIED on this host this pass** (`Code from External`) — no cell below is
gate-attested. Stated first, per `Gap 446-A`.

### 🔴 The correction, in place

🔵 The carried cells (`Integration supply` / `Probed first-hand 2026-10-25`) said: *"One SDK ever
existed: `dev-cucei-itrans/siiau-api-client`, a Laravel client for SIIAU's internal API, published
on Packagist and marked abandoned there"*, and that `git ls-remote` **does not resolve**. 🟢 **Both
cells are reproduced exactly this pass.** 🔴 **What they omit is the grant**, and the grant is the
part an engagement cannot proceed without:

| version | published | licence as published on Packagist |
|---|---|---|
| `v1.0.0-BETA` · `v1.0.0` · `v1.1.0` · `v1.1.1` | 2023-10-20 → 2024-08-14 | 🔴 **`proprietary`** |
| `v1.1.2` · `dev-main` | 2024-08-25 → 2024-10-08 | 🟢 **`BSD-3-Clause`** |

🔵 Read first-hand 2026-10-26 from `packagist.org/packages/dev-cucei-itrans/siiau-api-client.json`
with `laravel/framework` → `200` as the positive control and a fabricated name → `404` as the
negative. Package created 2023-10-13 · **7** versions · **1 023** downloads · 7 stars ·
`abandoned: true` · `repository` back-links the exact carried slug.

🔴 **Rule for any SIIAU engagement:** pin **`>=1.1.2`**. A `^1.0` constraint resolves into the
proprietary band, and because the repository is withdrawn (`404`/`128`, byte-identical to a
fabricated control) **the Packagist record is the only surviving evidence of either grant** — it
is the artefact to retain, not a convenience link.

🟢 **The row's strategic reading is unchanged and now better supported:** SIIAU's integration
supply is not merely thin, it is *ungranted*. A Globant engagement on this system of record is a
**build**, not an integration — and the pinning boundary above is the reason the one existing
client cannot be adopted as a shortcut.

### 🟢 Platform tier, unchanged this pass and re-stated so the shelf is not read as stale

🔵 No platform licence was re-measured this pass; the H5P correction `p450` made in place
(**GPL-3.0**, against the `🟢 MIT` cell this file previously contradicted itself with) stands, as
do Tutor's `release` and Oppia's `develop` defaults. 🔴 **This pass changed exactly one row** — the
SIIAU grant above — and adds no platform claim it did not read.

---

## 🆕 `p450` — **🔴 THIS FILE CONTRADICTED ITSELF ON THE MOST EXPENSIVE LICENCE IN THE INDUSTRY: one table graded H5P `🟢 MIT`, another in the SAME FILE graded it `🟡 GPL-3.0` and added "widely mislabelled MIT". A first-hand read settles it — GPL-3.0 — and the wrong row is corrected in place rather than left for a reader to pick between. 🟢 Two platform defaults are also measured and neither is `main`: Tutor defaults to `release`, Oppia to `develop`.**

🔴 **`make hooks` was DENIED on this host this pass** (`Code from External`) — no gate attests the
cells below. Stated first, per `Gap 446-A`.

### 🔴 The self-contradiction, and why it is the one that matters

| line | row as it stood | status |
|---|---|---|
| `verticals/solutions.md:687` *(carried platform rows)* | **`\| H5P \| 🟢 MIT \| Interactive content types; embeds in Moodle, Canvas and Open edX. \|`** | 🔴 **WRONG** |
| `verticals/solutions.md:1031` *(same file, later block)* | **`\| H5P \| 🟡 GPL-3.0 \| … 🔴 Widely mislabelled MIT. \|`** | 🟢 **RIGHT** |

🔴 **Both rows were live, in one file, and a reader taking the first table at face value inherits a
copyleft obligation this file had already identified and warned about.** This file's own Canvas row
states the stakes: *"conflating the two is the single most expensive licence error available in this
industry."*

🟢 **Settled first-hand through the `raw` channel, 2026-10-26**
(`evidence/licence-title-anchored.2026-10-26-p450.tsv`):
[h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) · ref **`master`** · grant at **`LICENSE.txt`** · **GPL-3.0, Version 3, 35 146 B** — the same GPLv3
text [moodle/moodle](https://github.com/moodle/moodle) carries at `COPYING.txt`, **35 147 B**, the
one-byte delta being a trailing newline.
🟢 **Line 687 is corrected in place to `🔴 GPL-3.0`** with the mislabelling note carried onto the
row itself, so the correction travels with the citation instead of living two tables away.

🔵 **The distinction the corrected row preserves, because it is what makes H5P usable at all:**
H5P's **JavaScript content types** are MIT; **`h5p-php-library`, the server-side integration
layer, is GPL-3.0**. "H5P is MIT" is true of the half nobody integrates and false of the half
everybody does. 🟢 The permissive route this file already shelves stands unchanged —
[edly-io/h5pxblock](https://github.com/edly-io/h5pxblock) (MIT, 1 064 B) loads H5P as **runtime
content** inside Open edX rather than linking the PHP library.

### 🟢 Platform default refs, measured — and `main` is the minority

Measured on the `ls-remote --symref` channel, **2026-10-26**:

| platform | default ref | heads | 🔴 what a `main`-assuming read returns |
|---|---|---|---|
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **`release`** | 17 | 🔴 nothing — no `main` exists |
| [oppia/oppia](https://github.com/oppia/oppia) | 🔴 **`develop`** | 500 | 🔴 nothing — no `main` exists |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | `master` | 294 | 🔴 nothing |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | `master` | 60 | 🔴 nothing — including the licence |
| [moodle/moodle](https://github.com/moodle/moodle) | 🟢 `main` | 40 | 🟢 resolves — the exception, not the rule |

🟢 **Across the 19 addresses measured this pass the split is `master` 11, `main` 5, `develop` 1,
`release` 1.** 🔵 This is `T104` (*"a grant's PATH is a function of the REF"*) with a denominator:
**74 % of these platform addresses are not on `main`**, so resolving the ref is not a refinement of
the read, it is the read. 🟢 The `HEAD` alias used by this pass's probe does it automatically and is
the reason the licence table above has no holes.

### 🔴 Vertical-platform discovery: nil, and the leg is recorded so the silence is not read as coverage

One leg ran on the prescribed shape (`open source platform education ERP CRM MIT Apache`). 🔴 **It
returned a single vendor source — OpenEduCat's own comparison pages, repeated across ten
translations — and zero addresses not already on these shelves.** Named in it: Moodle, Open edX,
OpenEduCat, Sakai, ILIAS, Canvas, Chamilo; all seven are shelved and graded. 🔵 **The leg's one
informative result is negative and worth the row: no MIT- or Apache-licensed system of record
(LMS *or* SIS) surfaced on the prescribed query** — consistent with `p448`'s `Gap 447-D` finding
that the first permissively-licensed system of record on these shelves came from a *state*-shaped
query, not a market-shaped one.
## 🆕 `p449` — **🟢 THE CONNECTOR TIER WRITES MORE THAN THIS SHELF PUBLISHED, AND THE CORRECTION RUNS AGAINST THE READ-ONLY READING: `Gap 448-C` resolved at source puts the category write share at 35.8 %, not 32.9 %, because `p448`'s denominator was inflated by 19 non-tool fields while its WRITE numerator was EXACT. 🔴 Which makes `Gap 448-B` worse: the allowlist field a gateway would key on is 43 % unpopulated over a LARGER mutating surface than anyone had measured.**

🟢 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` RAN** — fourth trial after
three denials, so `p448`'s settlement of that gap as *"a property of the host class"* is
**refuted**; the denial is **intermittent**. 🟢 Arrival baseline: **58/62 green, 4 RED**, 🔴 **two
of them NEW and both `p448`'s**. Three green on exit; the fourth is `DECLARED_RED`
(`Gap 449-D`).

### 🟢 The vertical fact, corrected at source rather than restated

`bruchris/canvas-lms-mcp` @ `c740624` (committed **2026-10-23** — **not** drift since `p448`).
A `ToolDefinition` counts only when its enclosing object literal carries **both** `name:` and
`inputSchema`:

| cell | `p448` | 🟢 `p449` | why |
|---|---|---|---|
| `bruchris` total tools | 🔴 222 | 🟢 **188** | 19 non-tool `name:` fields, **all outside `src/tools/`** — `normalize-ids.ts` 11, `init/wizard.ts` 5, `init/clients.ts` 3 |
| `bruchris` WRITE tools | **62** | 🟢 **62** | 🟢 **EXACT** — README declares *"125 read-only and 62 … write operations"* |
| `bruchris` write share | 27.9 % | 🔴 **33.0 %** | same numerator, correct denominator |
| **category total** | 414 | 🟢 **380** | |
| 🔴 **category write share** | 32.9 % | 🔴 **35.8 %** | |

🔵 README's own prose total is **187** against a true **188**, and **175 of 188** source ids are
named in it — so the two channels agree to **±1** and `p446`'s README reading was right all
along. The defect was never the README; it was scanning all of `src/` instead of the registries
(`evidence/gap448c-tool-count.2026-10-26-p449.tsv`).

### 🔴 What this changes for the sellable unit

🟢 **An agent layer on the community LMS-connector tier can author and publish courseware** —
`create_course`, `create_module`, `toggle-module-publish`, `update-syllabus`, `post-announcement`,
`bulk_grade_submissions` — at **four** addresses, and across a mutating surface of **35.8 %**
rather than 32.9 %. 🔴 **So the gateway is the product, not a detail.** `Gap 448-B` stands and
hardens: `vishalsachdev/canvas-mcp` declares `read_only_hint` on 72 of 128 tools, leaves
**55 (43.0 %) undeclared — and those 55 are exactly the mutating ones** — while its single
`read_only_hint=False` is `download_course_file`, **a read**. 🔴 **`compose/code/mcp-allowlist-gateway`
must gate on the tool's EFFECT and must never key on that hint.** A gateway keyed on it is now
known to be guarding a larger write surface with the same unsound field.

### 🟢 The platform tier is unchanged, and the grant seam is still the whole architecture

🟢 `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` — Apache-2.0, `LICENSE.txt` **10 172 B**, reproduced to the
digit by `p449` on an independent fetch — remains **the only permissively-licensed system of
record** on these shelves. 🔵 `openedx/XBlock` reproduces at **11 358 B** (`LICENSE.TXT`) and
remains the integration seam into a copyleft LMS. 🔴 Every other system of record here is
GPL-2.0/3.0, AGPL-3.0, or carries no grant — so the shape is unchanged: **permissive agent layer
+ effect-keyed gateway, bolted to a copyleft platform through a licence seam.**

---

## 🆕 `p448` — **🟢 THE CAPABILITY ABSENCE `p447` PUT ON THIS SHELF DOES NOT EXIST. `Gap 447-B` is REFUTED from source at HEAD: the community LMS-connector tier authors and publishes courseware — 136 of 414 tool declarations mutate, and `create_course`, `create_module`, `toggle-module-publish` and `update-syllabus` were read, not inferred. 🟢 A new vertical row: the NA state system of record is Apache-2.0. 🔴 Gate DENIED, third consecutive pass.**

🔴 **Gate posture: `make hooks` DENIED** (`Gap 446-A`, third consecutive pass, third container).

### 🟢 `Gap 447-B` REFUTED — and `p447` was right to carry it as a hypothesis rather than a fact

`p447` wrote on this shelf, flagged explicitly as **a single relayed secondary source**, that
the community MCP supply for Moodle and Canvas is *"overwhelmingly READ-ONLY"* and that *"not
one community server in that guide creates and publishes a course."* 🟢 **It named a test. The
test was run this hour, against source, and the hypothesis fails.**

| the claim | 🟢 what source says |
|---|---|
| *"overwhelmingly read-only"* | 🔴 **136 of 414** tool declarations mutate — **32.9 %**, and a **lower bound** |
| *"not one community server creates and publishes a course"* | 🔴 **false at four addresses** |

| address | authoring / publishing tools, read from the registry |
|---|---|
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | 🟢 **`create_course`** (`src/tools/courses.ts:205`, asserted in `tests/tools/courses.test.ts:53`), `create_module`, `create_module_item`, `create_page`, `create_new_quiz`, `grade_submission`, `enroll_user` — **62 write tools** |
| [`mdweaver/canvas-mcp`](https://github.com/mdweaver/canvas-mcp) | 🟢 `create-module`, `create-module-item`, **`toggle-module-publish`** (`src/tools/modules.ts:114`), **`update-syllabus`** (`src/tools/courses.ts:124`), **`post-announcement`** (`:216`) — **41 write tools, 46.1 %** |
| [`r-huijts/canvas-mcp`](https://github.com/r-huijts/canvas-mcp) | 🟢 `create-module`, `create-module-item`, `toggle-module-publish`, `post-announcement` — **30 write tools, 43.5 %** |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 `create_announcement`, `create_assignment`, `create_module`, `create_page`, `bulk_grade_submissions`, `bulk_update_pages` |
| [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | 🟡 **Go** codebase, 19 tools, 3 write |

🔵 **A server that creates a module and then toggles it published is publishing courseware.**
The authoring half of this tier is **not** vendor-only, and `Pattern AM`'s teacher-facing
courseware factory no longer needs a bespoke write path on Canvas.

### 🟡 But the gate you would reach for to make that safe is itself unsound

🟢 The one address that annotates read-only intent per tool, `vishalsachdev/canvas-mcp`,
declares it on **72 of 128** tools, leaves **55 (43.0 %) undeclared — and those 55 are exactly
the mutating ones** — while the **single** tool marked `read_only_hint=False` is
`download_course_file`, **a read**. 🔴 An MCP allowlist gateway keyed on `read_only_hint` is
keyed on a field that is **43 % unpopulated and at least once inverted**.
🟢 `compose/code/mcp-allowlist-gateway` must gate on the tool's **effect** — an explicit
write-tool denylist read from the registry — never on the hint → `Gap 448-B`.

### 🟢 A new vertical row — the NA state system of record, and it is permissive

| platform | repo | licence, read first-hand 2026-10-26 | region | what it is, and whether Globant can build on it |
|---|---|---|---|---|
| 🟢 **Ed-Fi ODS/API** | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | 🟢 **Apache-2.0** · `LICENSE.txt` **10 172 B** · `59899c6091b5` · HEAD `4d626f9ab257` | **North America** (US, Texas) | The operational data store and API behind **Texas TSDS/TEDS**, which TEA has **mandated** SIS vendors submit to via API transactions. 🟢 **The first permissively-licensed system of record on this shelf** — every other one is GPL-2.0/3.0, AGPL-3.0 or carries no grant. 🟢 **Vendor-and-build row.** 🟡 Bounded by a **233 924 B `NOTICES.md`** (`609e95c99d9b`): Apache-2.0 at the root does not clear the tree (`Trend 40`), so a dependency-closure pass is owed before shipping. |
| 🟢 **Ed-Fi ODS Implementation** | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | 🟡 not read this pass | **North America** | Deployment/implementation tooling for the above. 🟢 Reachable, HEAD `b6b72e594bc4`. Grant unread → next pass. |

### 🟢 `openSIS Classic` re-verified, and the below-root grant reproduces to the digit

| check | result |
|---|---|
| `docs/License.txt` | 🟢 **17 286 B · `224ac3d403e3`** — reproduces this shelf's published cell exactly |
| root grant paths | 🔴 **9 of 9 → 404** → `ABSENCE-ENUMERATED` at root |
| README | *"licensed under the GNU General Public License"*, pointing at `docs/License.txt` |

🔴 **GPL-2.0 confirmed, so the shelf's existing read stands:** distribution-triggered, no
network clause — a self-hosted customisation is fine, a redistributed derivative is not.

### 🔴 Where this tier still cannot serve an engagement, stated as absences rather than silence

| region | system of record | connector supply | verdict |
|---|---|---|---|
| **North America** | TSDS / Ed-Fi | 🟢 Apache-2.0 platform **+** a write-capable Canvas connector tier | 🟢 **servable today** |
| **EMEA** | Bayern `ASV`/`ByCS`/`VIDIS`, Niedersachsen `DaNiS`→`NEO` | 🔴 **no published API spec, no OSS** — `VIDIS` third-party integration still **pilot**; `NEO` primary-school release due **start of 2026/27** | 🟡 **procure through the state programme** |
| **APAC** | `UDISE+` (1.47 M schools) | 🔴 **no official API, no OSS tooling found** | 🔴 **absence** — sell teacher enablement, not integration |
| **LATAM** | `SIGED` (MX), `SIGE` (CL) | 🔴 none; one **third-party commercial** endpoint. Contrast Brazil/Argentina/Colombia, where code exists but is 🔴 **unlicensed more often than copyleft** (`Trend 43`) | 🔴 **split market** |

---

## 🆕 `p447` — **🟡 A CAPABILITY ABSENCE on the LMS-connector tier, carried as a hypothesis with a named test rather than as a fact: the community MCP supply for Moodle and Canvas is overwhelmingly READ-ONLY, and the authoring-and-publishing half appears to be vendor-built.**

🟡 **The claim, and its provenance, stated before its content.** A directory review of the
education MCP tier read this hour reports that the community servers are predominantly
**read-only student tools**, and states that *not one community server in that guide creates
and publishes a course*. 🔴 **This is a single relayed secondary source**, and the official
primaries that could corroborate it are **unreachable from this host** (`Gap 446-D`, re-probed
and widened below). It is therefore recorded as a **hypothesis**, not promoted to a shelf fact.

🟢 **Why it is worth carrying even at that confidence.** If it holds, it is a **market-structure**
statement rather than a tooling note: the connector tier this base sells is strong exactly where
an engagement needs it **least** (reading a student's own timetable and grades) and absent
exactly where an engagement bills **most** (course authoring, bulk enrolment, publishing). 🔵 It
would also explain `Trend 46`'s shape — ten addresses collapsing to six projects is what a
category looks like when everyone re-implements the same small read-only surface.

🟢 **The test, which is cheap and fully offline once cloned, and which the base already has the
instrument for.** Enumerate the registered tool names in each of the **six distinct projects**
`p446` established behind the ten Canvas/Moodle addresses, and classify each tool
**read vs write**. A single write-capable tool (`create_course`, `publish_module`,
`enrol_user`) refutes the absence; zero across six projects confirms it with a denominator.
Registered as `Gap 447-B`.

🔵 **Standing caution on this tier, unchanged and reinforced:** these servers reach **student
records**. Any of them entering a client engagement is a data-protection review, not merely a
licence review — and in EMEA that review now has no first-hand authority behind it, because
`eur-lex.europa.eu` has **never been readable from this host** (`Gap 446-D`).

---

## 🆕 `p446` — **The Moodle/Canvas connector tier re-priced by project count rather than address count: 🔴 the Canvas side is ONE maintained permissive project plus a second small arm, and the Moodle side is AGPL-3.0 or a 13-commit MIT alternative**

🔵 **Why this belongs on this file.** This file's job is the platform tier an engagement
customises. `p446`'s lineage audit (`agents/top.md`) changes the *supply* read under two of the
platforms carried here, and the change is in the direction that matters: **fewer, better-known
options**, not more.

| platform | connector supply, graded by PROJECT | licence cost | engagement read |
|---|---|---|---|
| **Canvas LMS** (Instructure) | 🟢 **4 projects** across 7 addresses — `vishalsachdev` (1 128 commits, 503 files, HEAD today), `bruchris` (430 / 501), `r-huijts`→`mdweaver` arm (64 / 35), and two < 12-commit singletons | 🟢 **MIT throughout** | 🟢 Take `vishalsachdev/canvas-mcp`. It is the only address here with a four-figure commit count **and** a HEAD that moved during this pass |
| **Moodle** | 🔴 **2 projects**, and they are not comparable — `csmediapro/moodle-mcp-server` (58 commits, 107 files) and `Jawadh-Salih/moodle-mcp-server` (13 commits, 37 files) | 🔴 **AGPL-3.0** / 🟢 MIT | 🔴 **The maintained Moodle connector costs AGPL-3.0.** The MIT alternative is 13 commits and stopped in **April 2026** |

🔴 **The Moodle asymmetry is the procurement fact on this file.** Moodle is the LMS with the
largest installed base in this base's region set, and its only actively-maintained MCP connector
is **network-copyleft**: AGPL-3.0 reaches a hosted service, which is exactly how a studio would
deploy it. 🟢 **Three dispositions, in cost order:** run `csmediapro` as a separate service and
publish its source; build on the 13-commit MIT base and own the maintenance; or integrate
Moodle through its own Web Services API directly and skip the connector tier. 🔵 The Canvas side
has no such tension — every address is MIT.

🟡 **Cell note.** `csmediapro`'s AGPL-3.0 payload re-measures **34 523 B · `0d96a4ff68ad`** from
an independent clone this hour, agreeing with this base's own published byte count. 🔵 Both the
figure and the family are confirmed; no disposition on this file changes on the Moodle grant
itself, only on the **count** of alternatives to it.


## 🆕 `p445` — **Two more systems of record mapped, and they are the two OPPOSITE ends of this map: 🟡 SIGAA has a real documented integration layer that is uniformly GPL-3.0, and 🔴 SIIAU has NOTHING — its only SDK's repository has been deleted**

🔵 **Why these two.** `p444` added **SUAP** as the first entry on this map that is
*open-ecosystem without being open-source*. This pass ran the platform-noun channel at three
more countries and the two results that landed are a matched pair: the same platform class
(university system of record), the same region, and **opposite supply states**. Read together
they are the argument for `Pattern AX` — you cannot price one from the other.

### 🟡 SIGAA — Brazil's federal universities. Supply exists, is documented, and cannot be vendored

🟢 **What it is.** **SIGAA** (*Sistema Integrado de Gestão de Atividades Acadêmicas*) is the
academic system of record across Brazil's **federal university** network — UFPB, UFRN, UFMG and
the rest. It holds curricula, enrolment, grades and class administration. Technically it is a
**JSF web application with no public REST API**, which is why every integration in existence is
a parser rather than a client.

| | |
|---|---|
| **Operator** | each federal university runs its own instance |
| **Region** | **LATAM** (Brazil) |
| **Source available?** | 🔴 **No.** The platform itself is not public |
| **Integration supply** | 🟢 **Yes — three addresses, verified first-hand 2026-10-25** |
| **Licence of that supply** | 🔴 **GPL-3.0, all three of three** |
| **Freshness** | 🔴 2016, 2017, 2020 |

| address | grant | HEAD | gives you |
|---|---|---|---|
| [`fernandobrito/cursos_ufpb`](https://github.com/fernandobrito/cursos_ufpb) | 🟡 GPL-3.0 · 35 141 B · `cbdcf32a9188` | 2017-01-26 · 168 files | the endpoint shape (`/api/curricula`) and the `sigaa_parser` logic |
| [`macielti/sigaa-cli`](https://github.com/macielti/sigaa-cli) | 🟡 GPL-3.0 · 35 149 B · `85b9a51f5603` | 2020-01-04 · 25 files | the **auth flow against any SIGAA instance**, by configurable base URL |
| [`fernandobrito/ufpb_sigaa_api_old`](https://github.com/fernandobrito/ufpb_sigaa_api_old) | 🟡 GPL-3.0 · 35 141 B · `4fa17f22c442` | 2016-02-07 · 14 files | the reference shape for "SIGAA behind an HTTP API" |

🟢 **How to customise with AI on top — and it is NOT the usual answer for this map.** For Moodle
or Open edX the move is *write a plugin*. For SIGAA there is no plugin seam and no licence that
permits vendoring, so the move is: **read these three as specification, write a clean-room
adapter, wrap it as an MCP server, and put the agent layer on that.** Full stack with every
licence measured: `Pattern AY`. 🔴 The adapter is unavoidable work; budget it as build, not as
integration.

🔴 **The access gate is separate from the licence gate and is the one that stops projects.**
SIGAA holds student records. A grant answers copyright only; *may we call this system* lives in
the university's terms of use. Get written registrar authorisation before the adapter touches
production.

### 🔴 SIIAU — Universidad de Guadalajara. Zero supply, and that is a measurement, not an absence of information

🟢 **What it is.** **SIIAU** (*Sistema Integral de Información y Administración Universitaria*)
is UdeG's own system of record — finance, HR, school records and planning, with **SIIAU Escolar**
as the student-facing portal for grades, credits and mobility paperwork. UdeG describes itself as
the first Mexican institution to build such a system for its own needs, and it is consolidated
and heavily used. Mexico's second-largest public university system runs on it.

| | |
|---|---|
| **Operator** | Universidad de Guadalajara |
| **Region** | **LATAM** (Mexico) |
| **Source available?** | 🔴 **No** |
| **Integration supply** | 🔴 **ZERO.** One SDK ever existed: `dev-cucei-itrans/siiau-api-client`, a Laravel client for SIIAU's internal API, published on Packagist and **marked abandoned** there |
| **Probed first-hand 2026-10-25** | 🔴 `git ls-remote https://github.com/dev-cucei-itrans/siiau-api-client` → **DOES NOT RESOLVE** |
| 🆕 **Grant, read first-hand 2026-10-26 (`p451`)** | 🔴 **SPLIT across versions — 4 of its 7 are `proprietary`.** `v1.0.0-BETA` · `v1.0.0` · `v1.1.0` · `v1.1.1` = **`proprietary`**; **`BSD-3-Clause` only from `v1.1.2`** (2024-08-25) and on `dev-main`. 🔴 **Pin `>=1.1.2`** — a `^1.0` constraint resolves into the proprietary band. 🔵 Packagist (`packagist.org/packages/…`, controls both ways) is now the **only** surviving channel for either grant: 7 versions · 1 023 downloads · `abandoned: true`. Full table in the `p451` section at the head of this file |

🔵 **Why this entry is worth as much as a positive one.** The package record survives on
Packagist; **the repository behind it is gone.** So the shape existed for SIIAU — somebody built
a client, published it, and deleted it — and an engagement at UdeG therefore starts from **zero**,
not from an unmaintained base it can revive. 🟢 **That is a scoping fact a proposal can be
written against**, and it is the single most common case on this map to be mistaken for *"we'll
find something open source"*. 🔴 Price the adapter as greenfield, and treat the dead Packagist
entry as evidence that UdeG's integration surface is reachable, not as a starting point.

🔵 **Where to go instead for Mexico, from this base's own legs:** **SIASE** (UANL) returned six
addresses (`p444`, top at 38 ★). An engagement that needs a *reference* Mexican implementation
should read SIASE's tier, not SIIAU's.

### 🔴 Two nils on this map, recorded so nobody re-buys them

| platform | country | result |
|---|---|---|
| **UdelaR** / `bedelías` | Uruguay | 🔴 **NIL.** The only artefact is a **2015 Facultad de Ingeniería student report** describing a scrape of the bedelías site to render prerequisites; no repository published with it |
| PUCP *Campus Virtual* · UNI *SIGA* · UNSA | Peru | 🔴 **NIL on a second channel.** PUCP ships an official mobile app authenticating against Campus Virtual and **no public integration code**; UNI and UNSA return nothing. With `p444`'s ministry-noun nil (SIAGIE) and its `UNMSM` coursework result, 🔴 **Peru is now twice-unpaid on two distinct channels** — weak evidence of a genuine supply absence rather than a measurement artefact (`Gap 445-B`) |

---

## 🆕 `p444` — **SUAP: a platform running across Brazil's federal institute network, with a real API ecosystem and 🔴 NO PUBLIC SOURCE — the first entry on this map that is open-ecosystem without being open-source**

🟢 **What SUAP is.** **SUAP** (*Sistema Unificado de Administração Pública*) is the academic and
administrative system of record of the **Instituto Federal** network — Brazil's federal
vocational and technical education system. It holds enrolment, grades, attendance, class
materials and meals. `p444` reached it through the platform-name channel and found an
integration ecosystem larger than any single LATAM platform this base has mapped.

🔴 **And the platform itself is not published.** Two legs were run — the acronym alone (732
hits) and the expanded name (*"suap sistema unificado administracao"*, 12 hits) — and **neither
returns the production Django application.** Every one of the 12 expanded-name results wraps,
extends, authenticates against, load-tests or *simulates* SUAP. The closest, `Thiago-FJ/SUAP`,
describes itself as an academic simulation for a coursework exercise. **Recorded as a measured
absence, not an assumption:** SUAP is reachable through a documented OAuth2 API and is not
forkable.

🔵 **Why that distinction earns a row on this map.** Every other platform here — Moodle,
Open edX, Canvas, Sakai, Kolibri, OpenEduCat, `ipti/br.tag` — is something an engagement can
**fork, read and self-host**. SUAP is something an engagement can only **integrate against**.
That is a different commercial shape: no vendor lock-in analysis, no hosting story, no licence
compatibility question for the platform — and *total* dependency on an API whose owner publishes
no grant for its own clients.

| platform | region | grant | what it is, and the engagement shape |
|---|---|---|---|
| **SUAP** · `suap.ifrn.edu.br` | **LATAM** (Brazil) | 🔴 **source not published** | Academic/administrative system of record for the **Instituto Federal** network. 🟢 Documented **OAuth2** API, confirmed reusable across institutions (`luizpicolo/suap_api` targets **IFMS**, not IFRN). 🔴 Integrate-only: cannot be forked or self-hosted. **Start from [`django-auth-suap`](https://github.com/django-by-kelsoncm/django-auth-suap) (MIT, HEAD 2026-09-05), not from IFRN's own unlicensed clients.** |
| [`suap-ava-suite/moodle-local_suap`](https://github.com/suap-ava-suite/moodle-local_suap) | **LATAM** (Brazil) | 🟡 **GPL-3.0** · `LICENSE` 35 161 B · `54b00c9ffd02` | 🟢 **The bridge between the two anchors of this map.** A Moodle `local` plugin wiring Moodle (the *AVA*, ambiente virtual de aprendizagem) to SUAP's system of record. **HEAD 2026-10-19** — live, 94 files. 🔵 GPL-3.0 here is *coherent, not a problem*: Moodle is GPL-3.0, so a Moodle plugin is expected to be, and the obligation is one the host platform already imposes. This is the first LATAM row on this map that connects an LMS to a SIS. |

🟢 **How this changes the composition story.** This base's LATAM verticals row has been
`ipti/br.tag` — one municipal K-12 platform, GPL-2.0. SUAP adds the **federal, post-secondary,
integrate-only** shape, and `moodle-local_suap` supplies the **LMS↔SIS seam** that
`compose/patterns.md` has previously only been able to describe for EMEA. 🔵 The pairing
*Moodle + `moodle-local_suap` + SUAP OAuth2 via `django-auth-suap`* is a complete, licence-clean
stack for a Brazilian federal-institute engagement, and it is wired up as `Pattern AW`.

🔴 **The gap this leaves, stated as a gap:** this map still has **no row for a LATAM
system of record that is BOTH forkable and permissive.** `ipti/br.tag` is GPL-2.0 (and its
README says BSD-3-Clause — `p443`), SIGAA and SIU Guaraní are institution-internal, SUAP is
unpublished. Every LATAM SIS address on this map is copyleft, closed, or both.

---


## 🆕 `p443` — **A live municipal platform joins the map, and it is the first row on this file whose README names a DIFFERENT, MORE PERMISSIVE grant than its own payload**

🟢 **The row.** `ipti/br.tag` — **T.A.G.** (*Tecnologia de Apoio à Gestão*) — is a Brazilian
basic-education school-management system built by **IPTI** with the municipality of **Santa
Luzia do Itanhy/SE**, explicitly for rural schools, **with offline synchronisation for schools
with no internet**. **3 959 commits**, **2 304 files**, HEAD **2026-10-18**. 🟢 It is the most
engagement-relevant LATAM platform address on these shelves and this file had **1 LATAM row of
6** before this pass.

🔴 **And it is sold here as GPL-2.0, because that is what the file says — against its own
README.** Established first-hand, both channels at the same commit `3e6d315ef881`:

| channel | what it states, read first-hand |
|---|---|
| `LICENSE` **18 027 B · `111e1f411730`** | 🔴 `GNU GENERAL PUBLIC LICENSE`, **`Version 2, June 1991`** — GPL-2.0. No §13 Affero clause, so not GPL-3/AGPL (`P171`); **no BSD operative clause anywhere in the payload** |
| `README.md` **3 065 B · `e9695ee53743`** | 🔴 § `Licença` states **"The BSD-3-Clause"** and reproduces the **BSD operative text** *"Redistribution and use in source and binary forms…"*, © 2011 IPTI. A BSD-3-Clause badge sits **commented out** on line 1 |
| GitHub's sidebar | **GPL-2.0** — with the payload, against the README |

🔴 **Why this is a procurement finding and not a tidiness one.** Every other conflict this file
has recorded ran the safe way — a badge or a roundup claiming **MIT** where the payload was
**AGPL**, so a careful reader was *over*-cautious. This one runs the **expensive** way: the
README is the **more permissive** channel, so a reader who trusts it concludes BSD-3-Clause,
vendors a copyleft school-records platform into a proprietary deliverable, and distributes it.
🟢 **The rule this file already applies survives the test: the payload decides.** 🔵 No
instrument on this base compares the two channels — `p288` built a README channel and `p278` a
channel-conflict gate, and neither asks *"does the README name a different licence from the
file"*. That is `Gap 443-C`.

🔵 **The wider LATAM result, measured in the same tranche:** of the four LATAM institutional
platforms that actually hold student records, **0 of 4 are permissive** — `ipti/br.tag`
(GPL-2.0), `LibreClass/libreclass` (GPL-3.0), `carmonabernaldiego/sistema-escolar` (AGPL-3.0),
and the already-shelved `sete` lineage — while **6 of 8** student-side academic-portal
addresses are. 🟢 **The copyleft frontier in LATAM therefore sits exactly where it sits in
EMEA: around the system of record.** That is the argument for this file's standing advice, now
with a LATAM denominator behind it: *integrate over an interface, never vendor the platform*.
Full tranche, refusals and ledger measurement: [`agents/trending.md`](../agents/trending.md)
`p443`. Recipe: `Pattern AV`.

| Platform | Licence (verified) | HEAD @ 2026-10-25 | Payload | AI layer goes… |
|---|---|---|---|---|
| **T.A.G. (`br.tag`)** | 🔴 **GPL-2.0** — 🔴 **README says BSD-3-Clause; the payload governs** | `3e6d315ef881` | `LICENSE` 18 027 B · `111e1f411730` | …**beside**, never vendored. Municipal basic education, Brazil, **offline-sync by design** — the one platform on this map built for schools with no connectivity *and* a live commit history. [repo](https://github.com/ipti/br.tag) |


## 🆕 `p442` — The platform tier is **enumerated**, not just read: four of these platforms carry a second licence text, and one of this file's own cells did not reproduce

🟢 `p440` and `p441` read the platform grants clause by clause. `p442` asks the prior
question — **is the payload we read the only one the repository carries?** — with the tree
channel now inside the shared library (`Gap 441-A`). Over the **134** repositories these
shelves publish a payload path for: **121** carry exactly one own-grant path, 🔴 **12 carry
more than one**, and four of those twelve are platforms or platform-adjacent rows on this
file.

| platform | the grant this file publishes | what else the tree carries, read first-hand | the read |
|---|---|---|---|
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 · `LICENSE` 35 147 B · `8ceb4b9ee5ad` | 🔴 `license.txt` **1 614 B · `0aaf39205490`** — GPL-3.0 titled, all six clauses **absent**, `GRANT-BY-REFERENCE` | the complete grant is the root file; the second payload is a **pointer** and must never be the one cited |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | `bigbluebutton-web/COPYING.LESSER` **7 637 B · `9ccf26cfe845`**, LGPL-3.0 | 🟢 consistent, and it is the **component** grant: `bigbluebutton-web` states its own LGPL-3.0 rather than inheriting silently. 🔵 Still `GRANT-UNCALIBRATED` — LGPL incorporates GPL-3.0 **by design** and needs `p440`'s unbought `GRANT-BY-DESIGN` verdict (`Gap 440-B`) |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | ECL-2.0 | **four** ECL-2.0 texts: root plus `delegatedaccess/`, `external-calendaring-service/`, `roster2/` (sampled: `delegatedaccess/LICENSE` **11 110 B · `6001bb8caa76`**) | 🟢 consistent; a per-module restatement in a 400-module monorepo, not a second grant |
| [`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) | AGPL-3.0 · `LICENSE` **35 442 B · `698099632698`** (🔴 **repaired here** — the published cell read 35 441 B · `d8d2ea7ef0a1`, measured through a capture) | MIT ×2 + Apache-2.0 under `mathlive-assets/` and `sre-assets/` (MathLive 1 099 B, Speech Rule Engine 10 174 B, Temml 1 074 B) | 🟡 **vendored third-party assets, not the project's grant.** The enumerator's `is_own_path` knows `node_modules/` and `vendor/` but not `*-assets/`, so it types them as own — recorded as `Gap 442-B`, not quietly fixed |

🔵 **What changes for an engagement:** nothing about these four platforms' own licences, which
hold as published. What changes is the **screening procedure** — a platform's grant is now
established by enumerating its tree, so a second text can be *seen* and classified rather than
hidden behind whichever filename a ladder happened to try first. `Pattern AU` is the recipe.

## 🆕 `p441` — The **permissive** half of the platform tier is now read clause by clause too, and one platform-adjacent row is sold with a restriction attached

🟢 `p440` read the ten **copyleft** platforms' grants clause by clause. `p441` does the same
for the **BSD** tier — the assessment and teaching-compute layer this file sells beside the
LMS — and the result is **11 of 12 payloads `GRANT-PRESENT`**, verified against a
variant-aware profile (BSD-2 and BSD-3 are different licences under one family name).

| repository | shelved on | payload · `sha256₁₂` | grant check 2026-10-25 |
|---|---|---|---|
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **this file** (assessment delivery) | `LICENSE.txt` 2 058 B · `a5c692f12090` | 🟢 `GRANT-PRESENT` — digest unchanged since `p390` |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | `repos/foundations.md` | `LICENSE` 1 475 B · `7069c7e8d60e` | 🟢 `GRANT-PRESENT` 🔴 **untitled payload** |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | `repos/foundations.md` | `LICENSE` 1 512 B · `3a83d5b8e22c` | 🟢 `GRANT-PRESENT` 🔴 **untitled payload** |
| [`jupyterlite/jupyterlite`](https://github.com/jupyterlite/jupyterlite) | `repos/foundations.md` | `LICENSE` 1 525 B · `574f8a9cab1e` | 🟢 `GRANT-PRESENT` |

🔵 **Only `qtiworks` is a row on this file**; the other three are the teaching-compute tier
on `repos/foundations.md` and are listed here because they are what sits *beside* the LMS in
a delivery. No row is added to this shelf by this pass.

🔴 **Two warnings that belong on a platform shelf specifically.**

1. [`open-webui/open-webui`](https://github.com/open-webui/open-webui) — a common drop-in
   chat surface in front of an LMS, carried on `agents/top.md` as a warning row rather than
   a build-on row — grades `GRANT-PRESENT` and is **not** a stock BSD-3
   grant: 2 819 B against ~1 515 B, carrying a **branding restriction** and a **Contributor
   Licence Agreement**. `GRANT-PRESENT` answers *is the grant here*, never *is it
   unmodified*. Sell it with the restriction in the SOW, or use `jupyter-ai` instead.
2. 🟡 **`BigBlueButton` and `OpenEduCat` are still `GRANT-UNCALIBRATED`** (LGPL-3.0,
   `Gap 440-B`) and must not be read as cleared. `p441` did not touch that gap: LGPL
   incorporates GPL-3.0 **by design**, so it needs a fifth verdict rather than a profile.

🔵 Recipe for putting this tier in front of a client's counsel: `Pattern AT`. Instrument,
87 controls and mutation results: `compose/code/p441-bsd-variant/README.md`.

## 🆕 `p440` — The platform tier's grants are read **clause by clause** for the first time, and all ten hold

🟢 Every pass before this one verified the platform tier by reading its payload and
naming its **family**: *this is AGPL-3.0, 35 136 B, here is the digest*. That answers
"which licence" and 🔴 **not** "is the licence actually in there". `p439` showed on the
code path why the two differ — a 552 B file titled Apache-2.0 that was a pointer — but
its instrument had profiles for MIT, Apache-2.0 and ISC only, so 🔴 **every copyleft row
on this file was `GRANT-UNCALIBRATED`: the instrument declining to judge the entire tier
this file exists to sell.**

🟢 `p440` profiles the GPL family. The ten platform repositories below were re-probed at
source **2026-10-25** and graded against their own licence version's operative clauses.

| Platform | Branch | Payload | Bytes | `sha256₁₂` | Profile | Grant check |
|---|---|---|---|---|---|---|
| **Moodle** · [`moodle/moodle`](https://github.com/moodle/moodle) | `main` | `COPYING.txt` | 35 147 | `8ceb4b9ee5ad` | GPL-3.0 | 🟢 **GRANT-PRESENT** |
| **Open edX** · [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `master` | `LICENSE` | 35 136 | `e12d78569742` | AGPL-3.0 | 🟢 **GRANT-PRESENT** |
| **Frappe LMS** · [`frappe/lms`](https://github.com/frappe/lms) | `develop` | `license.txt` | 33 893 | `db1a87ba81e8` | AGPL-3.0 | 🟢 **GRANT-PRESENT** |
| **Chamilo** · [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `master` | `LICENSE` | 35 147 | `8ceb4b9ee5ad` | GPL-3.0 | 🟢 **GRANT-PRESENT** |
| **Canvas LMS** · [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `master` | `LICENSE` | 34 520 | `57c8ff33c9c0` | AGPL-3.0 | 🟢 **GRANT-PRESENT** |
| **Gibbon** · [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `v31.0.00` | `LICENSE` | 35 121 | `93178a43d6d3` | GPL-3.0 | 🟢 **GRANT-PRESENT** |
| **RosarioSIS** · [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `mobile` | `LICENSE` | 15 214 | `d954e14e5c75` | GPL-2.0 | 🟢 **GRANT-PRESENT** |
| **i-Educar** · [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | `2.12` | `LICENSE` | 18 092 | `8177f9751321` | GPL-2.0 | 🟢 **GRANT-PRESENT** |
| **openSIS Classic** · [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | `master` | `docs/License.txt` | 17 286 | `224ac3d403e3` | GPL-2.0 | 🟢 **GRANT-PRESENT** |
| **PeerTube** · [`Chocobozzz/PeerTube`](https://github.com/Chocobozzz/PeerTube) | `develop` | `LICENSE` | 34 520 | `76a97c878c9c` | AGPL-3.0 | 🟢 **GRANT-PRESENT** |

🟢 **Ten of ten.** 🔵 **What a clean sweep is worth, precisely:** it does not make the
copyleft exposure smaller — Moodle is still GPL-3.0 and Open edX is still AGPL-3.0, and
the posture on this file is unchanged. What it removes is a *different* risk, the one
`p439` found on the permissive side: a platform whose licence file is a **pointer** to
its licence, leaving the client to discharge the distribution obligation it names. 🟢 On
this tier that risk is now measured at **zero**, rather than assumed.

### 🔴 The sentence a client should hear about AGPL, now that §13 is readable

The AGPL-3.0 profile built this pass requires the **operative §13 sentence** —
*"...interacting with it remotely through a computer network ... an opportunity to
receive the Corresponding Source"*. 🔵 That clause is the whole commercial difference
between Moodle and Open edX, and it is the one a procurement conversation turns on:

- **GPL-3.0 (Moodle, Chamilo, Gibbon)** — the obligation attaches to **distribution**.
  A hosted deployment that never ships binaries to anyone does not trigger it.
- **AGPL-3.0 (Open edX, Canvas, Frappe LMS, PeerTube)** — the obligation attaches to
  **network interaction**. A hosted deployment triggers it by being used, and
  🔴 modifications must be offered to the platform's own users.
- **GPL-2.0 (i-Educar, RosarioSIS, openSIS)** — distribution again, and 🔵 **no network
  clause at all**, because GPL-2.0 predates the question. These three are the LATAM and
  low-cost SIS tier, and this is a genuine, under-stated advantage for a hosted
  engagement: the same posture that makes them look dated makes them cheaper to host.

🔴 **And `p440` measured why that GPL-2.0 row cannot be graded with GPL-3.0's clauses:**
a complete GPL-2.0 licence is missing **four of GPL-3.0's six** operative clauses, so a
single unversioned "GPL" rule would have condemned all three of those platforms as
carrying a truncated grant. The profile is version-aware for exactly that reason.

🟡 **`LGPL-3.0` is still unread, and two platforms on this file carry it** —
**BigBlueButton** and **OpenEduCat**. LGPL-3.0 incorporates GPL-3.0 *by reference* by its
own design, so it needs a verdict this instrument does not yet have. Registered as
`Gap 440-B`; until then those two rows stay `GRANT-UNCALIBRATED`, which is the
instrument declining rather than approving.

---

## 🆕 `p439` — The platform tier re-measured at source, and the **one licence error this industry keeps making** is confirmed live for the third time

🟢 **Four platform-tier addresses re-probed first-hand this hour**, byte-for-byte and
HEAD-for-HEAD against what this shelf already carries. The point of the exercise is that it
was run as a *measurement* and not as an assumption — a shelf that is never re-read is a
shelf whose staleness is unknown:

| Platform | Licence (re-verified 2026-10-25) | Default branch | Payload | Shelf agrees |
|---|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | ⚠️ `master` | `LICENSE` 10 982 B @ `d073ad444fe5` | 🟢 yes |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** | ⚠️ `develop` | `license.txt` 33 893 B @ `5d6df8e3ed8e` | 🟢 yes |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | `main` | `LICENSE` 11 408 B @ `a31d82624c27` | 🟢 yes |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL** | `main` | `LICENSE` 25 289 B @ `7bd8b6794cb7` | 🟢 yes |

🔴 **THE ERROR, LIVE AGAIN: "Frappe LMS is the MIT-licensed option."** Three separate 2026
LMS-comparison pages returned by this pass's own platform search say exactly that, one of
them phrasing it as *"MIT licence with self-hosted data ownership"*. 🟢 **It is AGPL-3.0**,
read from `license.txt` at the commit above. The MIT belongs to **`frappe/frappe`**, the
*framework*; the LMS *application* built on it is AGPL-3.0. `p425` registered this as `T125`
and `p439` is the third independent confirmation.

🔵 **Why this specific error is the most expensive one available in this tier.** The
framework-permissive / application-copyleft split is invisible in a vendor comparison table
and decisive for a client: AGPL-3.0 §13 reaches users **over a network**, so a hosted
student-facing deployment of a modified Frappe LMS owes source to its users. A studio that
priced the engagement off "MIT" has mispriced the whole delivery model, not a line item.
🟢 **And it is the generalisable lesson**, which is why it sits on this shelf rather than only
in the trend record: in a platform tier, **the licence belongs to the artefact you ship, not
to the project whose name is on the box.** Two keys, one platform.

### 🟡 Two default branches that are not `main`, and that is a *platform-tier* property

`OpenOLAT` resolves to **`master`** and `frappe/lms` to **`develop`**. 🔴 A hardcoded `main`
writes both down as **ungranted** — the exact trap `lib/probe_payload.sh` exists to close
(measured on `GibbonEdu/core` → `v31.0.00`, `portabilis/i-educar` → `2.12`,
`francoisjacquet/rosariosis` → `mobile`, three of the five highest-starred open SIS platforms
in existence). 🔵 Mature platform projects are *more* likely than new agents to carry a
non-`main` default, because their branch conventions predate the convention. Resolve with
`ls-remote --symref`, never assume.

### 🟢 The customisation seam, restated for the licences actually on this shelf

Both headline AI-on-top platforms this pass touched are **copyleft** (`frappe/lms` AGPL-3.0;
Moodle GPL-3.0 at **5.2**, April 2026; Open edX AGPL-3.0, current release **Verawood**, with
**Willow** expected December 2026; Canvas AGPL-3.0; Chamilo GPL-3.0; ILIAS at **11**,
PHP 8.3/8.4). 🟢 **The two permissive answers in the whole tier remain `OpenOLAT`
(Apache-2.0) and `kolibri` (MIT)** — and the seam that lets a studio put AI on a copyleft LMS
without inheriting its obligations is still the one this shelf has carried since `p387`:
build **outside** the core, against a supported extension point —
[`openedx/XBlock`](https://github.com/openedx/XBlock) (Apache-2.0) for Open edX, LTI 1.3 or
the REST API for Moodle and Canvas — and keep the AI component in its own repository under
its own grant. 🔵 Calling an AGPL system **over a network boundary** is a different act from
linking into it, and the boundary is the deliverable.

🔴 **New screening question on this tier as of this pass, and it is not theoretical.** Before
adopting any platform component, ask whether its grant is **present** or merely **named** —
`make gate-grant-presence`. A 552 B payload titled Apache-2.0 was found in live education
supply this hour (`spragginsdesigns/ai-tutor-webapp`), holder **Vercel, Inc.**, licence text
absent from the repository. For a platform component the client will *redistribute*,
Apache-2.0 §4(a)'s duty to supply a copy of the License lands on the integrator. See
`Gap 439-A`.

---

## 🆕 `p438` — The platform decision survives a **licence scan** and not a **licence read**, and the difference is now measured on this base's own instruments

🔵 **Why this lands on the verticals shelf.** A platform choice is the one decision on an
education engagement that a client's procurement function actually audits, and it audits it
with a scanner report. 🟢 This shelf's standing finding is that the platform tier is almost
entirely copyleft — Moodle (GPL), Open edX (AGPL-3.0, narrowed), Chamilo (GPL-3.0), Canvas
community edition (AGPL-3.0) — with `OpenOLAT` (Apache-2.0), `Sakai` (ECL-2.0, Apache-derived)
and `learningequality/kolibri` (MIT) the permissive exceptions. 🔴 `p438` adds the part of the
audit that a scanner cannot do.

### 🔴 The measurement, on this base's instruments, not a vendor's

`p438` graded a new education specimen,
[`fangyuan-3149/book-learning-tutor`](https://github.com/fangyuan-3149/book-learning-tutor)
(`LICENSE` **1 503 B** · `sha256₁₂ 54ceeac19921`, HEAD `f0ef6fc3acd7`, read 2026-10-25). One
`bespoke_census.grade()` call returns, **in one row**:

| column | value | what a procurement report would print |
|---|---|---|
| `titled_family` | `MIT` | 🟢 "permissive" |
| `scan_verdict` | `PERMISSIVE` | 🟢 "cleared" |
| `stock` | `YES` | 🟢 "standard text, no review needed" |
| `p1054_verdict` | 🔴 `MIT-BODY-PLUS:unclassified-addition` | ⚠️ nothing — this column is not in the report |
| `needs_a_human` | 🔴 `no` | 🔴 "no legal read required" |

The appended clause — in Chinese, after a `---` rule — states that the repository ships **no
book or copyrighted content**, that the operator supplies the material, and that **the
operator carries the legal and copyright liability for it**. 🔴 On an education engagement the
operator is the client, and the content is textbooks. 🔵 `p427`'s `conjunctive_grant.classify()`
returns `scope: None` on the same payload because every entry in its `SCOPE_MARKERS` is an
English phrase.

🟢 **Sized over the corpus, so it is not one anecdote:** of the **238** licence payloads
committed under `compose/code/**/fixtures/`, **9** carry an addition verdict and **7 of those
9 are routed `needs_a_human = no`** — `p427`'s own two-family specimen among them. Registered
as `Gap 438-A`; the one-disjunct remedy is priced there and deliberately not slipped into this
pass.

### 🟢 The procurement consequence, stated so it can go in a proposal

🔵 **It does not change which platform to pick.** The copyleft map on this file stands: every
payload here was read first-hand and none of them is a stock text with an unread addendum.
🟢 **It changes what Globant can credibly say about the components bolted onto that
platform.** The AI layer on an education engagement is assembled from small permissive
repositories — this pass alone shelved eight — and that layer is where the addendum class
lives: 🔴 **1 of the 9 addresses graded this pass, 11 %, carried a clause that both of this
base's automated instruments missed and that shifts content liability onto the client.**

🟡 **So the deliverable is a three-column clearance, applied to every component that reaches a
client's estate** — the integration-layer analogue of the foundation rule now on
`repos/foundations.md`:

1. 🟢 family from the payload, never from a badge or a comparison blog (this shelf's
   `formalms` row is the standing example: Apache-2.0 in one comparison, GPL-2.0 in another,
   resolved here from the payload);
2. 🟢 the addition column read, not just the family column;
3. 🟢 any bytes above the family's stock band read **by a person, in the payload's own
   language** — the band is an excellent detector that a payload was modified and no
   detector at all of what the modification says.

🔵 **And the platform tier's own exposure is bounded, which is worth saying plainly to a
client**: the large copyleft platforms ship canonical GPL/AGPL texts whose bytes this base has
already measured, so the addendum risk on this file is **low and measured** — it concentrates
in the long tail of permissive components, exactly where the delivery team is moving fastest.

## 🆕 `p437` — Conformity is a **procurement surface** on the platform decision, and it reverses the usual copyleft calculus

🔵 **The connection this file was missing.** This shelf's standing finding is that the
education platform tier is almost entirely copyleft — Moodle, Open edX, Chamilo, Canvas-adjacent
estates — with `OpenOLAT` (Apache-2.0) and `learningequality/kolibri` (MIT) the permissive
exceptions. 🆕 `p437` adds the regulatory half of that decision, and it changes which platform
wins.

Under the EU AI Act, the duties attach to the **AI system** and its provider/deployer role,
not to the LMS it is bolted onto. So the platform choice determines *who carries the
obligation*:

| configuration | who is the provider of the high-risk system | consequence |
|---|---|---|
| AI built **into** the LMS core (vendored fork) | 🔴 The client, for the whole platform | Annex IV documentation must cover the LMS; a copyleft fork makes that documentation a distribution artefact too |
| AI as a **separate component over a seam** (XBlock, MCP, LTI) | 🟢 The component, scoped narrowly | Annex IV covers the component only. **The conformity surface is as small as the seam** |

🟢 **This is the strongest argument yet for the seam-based integration this file already
recommends** — `openedx/XBlock` (Apache-2.0) for Open edX, the MIT connector tier for national
platforms, LTI for the rest. It was previously a licence-hygiene argument. 🔵 **It is now also
a compliance-scoping argument, and that is the one a client's counsel will act on:** keeping
the AI outside the copyleft core keeps the Annex IV technical documentation bounded to code
Globant actually wrote.

🔴 **The corollary, stated plainly.** A client already running a copyleft LMS who asks for AI
"inside the platform" is asking for the maximum conformity surface and a copyleft distribution
obligation on the documentation at the same time. 🟢 The answer is not to refuse the
engagement — it is to price the seam, and `compose/patterns.md` **Pattern AP** is the scoping
gate that produces that price.

🟡 **The education-ERP nil is untouched by this.** Nothing found this pass is an education ERP
or SIS platform; the EU-AI-Act tooling tier is governance instrumentation, not a vertical
system. The standing nil recorded at `p433`/`p434` and reconfirmed at `p435` **stands a fourth
consecutive pass** — this pass did not re-run that sweep and does not claim to.

## 🆕 `p436` — The interoperability layer is a vertical in its own right, and a **national** education body is shipping it permissively

🔵 **The platform map on this file answers "which LMS do we build on?".** `p436` restores a tier
that answers a different and often better question: **"what do we build between the systems the
client already runs?"** Every row below was re-read first-hand on 2026-10-25.

| system | licence (verified) | layer | what it unlocks | Region |
|---|---|---|---|---|
| [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | **Apache-2.0** `10 173` B · `a6cba85bc92e` | roster / SIS interop | Serves a **OneRoster 1.2 API over an Ed-Fi ODS** (DS 4.0, 5.x, 6.1). Lets an agent read enrolment and class structure **without integrating against the SIS**. The US district-data seam. | North America |
| [Kennisnet/php-qti3](https://github.com/Kennisnet/php-qti3) | **MIT** `1 066` B · `27fb6d463569` | assessment interop (PHP) | QTI 3 in PHP from the **Dutch national education-ICT body** — the route into a PHP estate, which is most of the Moodle world. | EMEA |
| [OpenOLAT/qtiworks](https://github.com/OpenOLAT/qtiworks) | **BSD-3-Clause** `2 058` B · `a5c692f12090` — 🟢 `GRANT-PRESENT` clause-by-clause (`p441`) | assessment delivery | QTI 2.1 delivery with **JQTI+** and **MathAssess**. Maintained to **2026-06-30**. | EMEA |
| [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** `1 072` B · `00ed05b90bf8` | assessment authoring | QTI 3 toolkit; `packages/core` implements the **parametric-item mechanism** end to end. | North America |
| [amp-up-io/qti3-item-player](https://github.com/amp-up-io/qti3-item-player) | **MIT** `1 076` B · `7faa621251d7` | assessment rendering | QTI 3 item player — the rendering half of the boundary. | North America |
| [marcosroriz/sete](https://github.com/marcosroriz/sete) | **MIT** `1 069` B · `0bbd32e7e09a` | public-sector operations | **SETE** (CECATE/UFG): school-transport e-governance with a **desktop build for municipalities with restricted internet**. 🔴 HEAD 2023-03-20 — a reference design, not a live dependency. | LATAM |

🟢 **Why `Kennisnet/php-qti3` changes the EMEA story on this file.** This file has repeatedly
recorded that EMEA's open-source education supply is thin and regulation-heavy. A **national
education-ICT agency publishing its own MIT assessment implementation** is the opposite shape:
state-funded, permissively licensed, and institutionally durable. 🔵 Taken with `p435`'s national
school-platform connector tier (IServ, Librus, Smartschool, EduPage, Skola24), the EMEA pattern is
now clear — **the supply is there, it is national rather than pan-European, and it was invisible
to every pan-regional query this base ran.**

🔵 **The decision this tier adds to "choosing the base"**: if the client's constraint is *several
systems that must agree* rather than *one system to extend*, the interop layer is the engagement
and the LMS choice is downstream of it. 🔴 **Reach bound: grant + currency + README; no suite was
executed here.**

# 🏫 Vertical solutions — Education

> Real, deployable platforms that an AI layer can be built **on top of** — the education
> equivalents of Odoo (ERP) or OpenMRS (health). Licences read from each repository's own
> payload at the HEAD shown, 2026-10-25.

## The platform map

🟢 **Re-read at source on 2026-10-25** — licence taken from each repository's own payload at
the HEAD shown, never from a badge.

| Platform | Licence | HEAD @ 2026-10-25 | Payload | AI layer goes… |
|---|---|---|---|---|
| **OpenOLAT** | 🟢 **Apache-2.0** | `d073ad444fe5` | `LICENSE` 10 982 B · `6dbc5b605ed0` | …**inside**. The only full LMS where proprietary AI may be embedded directly. [repo](https://github.com/OpenOLAT/OpenOLAT) |
| **Kolibri** | 🟢 **MIT** | `44a4e68aac3e` | `LICENSE` 1 097 B · `3c056b34a476` | …**inside**. Offline-first; local models via Ollama. [repo](https://github.com/learningequality/kolibri) |
| **Sakai** | 🟡 **ECL-2.0** | `4debc94780cc` | `LICENSE` 11 120 B · `0688f62d04f1` | …**inside**, with notice obligations. 🔴 **Not Apache-2.0**, despite roundups saying so. [repo](https://github.com/sakaiproject/sakai) |
| **Moodle** | 🔴 **GPL-3.0** | `46c042e7da65` | `COPYING.txt` 35 147 B · `8ceb4b9ee5ad` | …**beside**, over Web Services / an MCP server. [repo](https://github.com/moodle/moodle) |
| **Open edX** | 🔴 **AGPL-3.0** | `87cd3811a425` | `LICENSE` 35 136 B · `e12d78569742` | …**in an XBlock** (Apache-2.0) — the supported seam. [repo](https://github.com/openedx/edx-platform) |
| **Chamilo** | 🔴 **GPL-3.0** | `2e5139a816d3` | `LICENSE` 35 147 B · `8ceb4b9ee5ad` | …**beside**, over its REST API. Deep LATAM footprint. [repo](https://github.com/chamilo/chamilo-lms) |
| **Frappe LMS** | 🔴 **AGPL-3.0** | `5d6df8e3ed8e` | `license.txt` 33 893 B · `db1a87ba81e8` | …**beside**. 🔴 Not MIT, despite 2026 roundups. [repo](https://github.com/frappe/lms) |
| **eXeLearning** | 🔴 **AGPL-3.0** | `c848eca0018d` | `LICENSE` 34 523 B · `0d96a4ff68ad` | …**beside**. Spain Ministry of Education-led. [repo](https://github.com/exelearning/exelearning) |
| **BigBlueButton** | 🔴 **LGPL-3.0** | `ec452b65043b` | `LICENSE` 7 652 B · `e3a994d82e64` | …**linked**, never forked. [repo](https://github.com/bigbluebutton/bigbluebutton) |
| **OpenEduCat** | 🔴 **LGPL-3.0** | `46a5d7d40082` | `LICENSE` 8 241 B · `528f84036800` | …**as an Odoo module**. Closest thing to an education ERP. [repo](https://github.com/openeducat/openeducat_erp) |

### Carried platform rows — graded by earlier passes, not re-measured on 2026-10-25

🔵 Stated as carried so a reader does not mistake an older reading for a fresh one.

| Platform | Licence (carried) | Note |
|---|---|---|
| **Canvas LMS** | 🔴 **AGPL-3.0** | The dominant North American LMS. 🔴 Its *agent* ecosystem is MIT — see below — and conflating the two is the single most expensive licence error available in this industry. |
| **Forma LMS** | 🟢 **Apache-2.0** | Corporate-training LMS; permissive. |
| **Opencast** | 🟡 **ECL-2.0** | Lecture capture and video management. |
| **H5P** | 🔴 **GPL-3.0** *(corrected `p450`)* | Interactive content types; embeds in Moodle, Canvas and Open edX. 🔴 ~~MIT~~ — `h5p-php-library` `LICENSE.txt` read first-hand 2026-10-26: **GPLv3, 35 146 B**. The MIT grant covers the **JS content types**, not the PHP integration layer. Permissive route: [edly-io/h5pxblock](https://github.com/edly-io/h5pxblock) (MIT), H5P as runtime content. |
| **Academico** | 🟢 **MIT** | Lightweight SIS. |
| **OpenSIS Classic** | 🔴 **GPL-2.0** | Student information system. |
| **frappe/lms** | 🔴 **AGPL-3.0** | Same project as **Frappe LMS**; two keys, one platform. 🔴 `p425`'s `T125`: the MIT belongs to `frappe/frappe`, the **framework**, not the LMS. |
| **`frappe/lms`** | 🔴 **AGPL-3.0** | The backticked spelling, kept so a citation under either form resolves. |

### 🔴 The agent-facing layer is MIT — and it is a DIFFERENT tier from the platform

The names below grade **MIT** because they are MCP servers and agents *over* a platform,
not the platform. A studio told *"Canvas is MIT"* would ship AGPL-3.0.

| Agent-tier name | Licence | What it actually is |
|---|---|---|
| **Canvas** | 🟢 **MIT** | The Canvas *MCP/agent* tier — not Canvas LMS (AGPL-3.0). |
| **Google Classroom** | 🟢 **MIT** | MCP servers over the Classroom API. 🔴 Use [`vTanco`](https://github.com/vTanco/google-classroom-mcp), **not** `pengusto` — relicensed proprietary 2026-10-23. |
| **Blackboard** | 🟢 **MIT** | The Blackboard agent tier. |
| **Blackboard Learn** | 🟢 **MIT** | MCP servers over Blackboard Learn's REST API. |
| **SCORM Runtime** | 🟢 **MIT** | SCORM 1.2/2004 packaging and playback. |

## 🆕 `p435` — The platform question has a **third** answer, and it is the platform the client is already running

This file has framed the platform decision as *which open-source LMS do we base on* —
OpenOLAT or Kolibri for a permissive base, Moodle or Open edX if copyleft is acceptable.
🟢 **`p435` adds a third option the shelf did not carry: do not replace the platform at
all — speak to it.** The grade census of this base's own backlog
(`compose/code/p435-promotion-sweep`, 2 450 addresses graded first-hand) surfaced a tier of
**MIT connectors for the platform a national school system actually runs**.

### 🟢 The national school-platform tier — every grant read first-hand on 2026-10-25

| Platform | Where it is the default | Connector | Grant | HEAD |
|---|---|---|---|---|
| **IServ** | German state schools | [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) | 🟢 **MIT** · 1 090 B · `5dc99bd5061f` | `8afdea14fbcd` @ 2026-10-25 |
| **Librus Synergia** | Polish schools | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) + [`librus-python-api`](https://github.com/krzysztofbury/librus-python-api) | 🟢 **MIT** · 1 071 B · `22e7ab2dbddc` | `e12e36f24224` @ 2026-10-25 |
| **Smartschool** | Flanders (Belgium) | [`MauroDruwel/Smartschool-MCP`](https://github.com/MauroDruwel/Smartschool-MCP) | 🟢 **MIT** · 1 069 B · `b414ff32815f` | `ab3fa81f857f` @ 2026-10-14 |
| **EduPage** | Slovakia and CEE | [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) | 🟢 **MIT** · 1 070 B · `e99290e1540b` | `b35ce653d2c9` @ 2026-10-23 |
| **Skola24** | Swedish municipal timetables | [`Kretiandpleti/skola-24-haos-integration`](https://github.com/Kretiandpleti/skola-24-haos-integration) | 🟢 **MIT** · 1 070 B · `8b34b498bb1f` | `fdbc9349b20f` @ 2026-10-25 |
| **DTU Learn** (Brightspace / D2L) | Denmark's technical university | [`CarlSvejstrup/dtu-learn-mcp`](https://github.com/CarlSvejstrup/dtu-learn-mcp) | 🟢 **MIT** · 1 079 B · `4f21e3f0f9fc` | `9444a1fd5199` @ 2026-10-07 |
| **NEIS** | Korea's national education data portal | [`hyunbinseo/neis-school-info`](https://github.com/hyunbinseo/neis-school-info) | 🟢 **MIT** · 1 068 B · `e82e1769aaaf` | `5c9ecede5208` @ 2026-09-27 |
| **Schoology + StudentVUE + Ion** | Fairfax County Public Schools (US) | [`jibberswrld/fcps-school-mcp`](https://github.com/jibberswrld/fcps-school-mcp) | 🟢 **MIT** · 1 073 B · `cd9e736254f8` | `7d9dfbfc32bb` @ 2026-09-28 |
| **Artemis** | TUM and its partner universities | [`ls1intum/edutelligence`](https://github.com/ls1intum/edutelligence) | 🟢 **MIT** · 1 091 B · `6b9b9eda00d6` | `a7584174bd3d` @ 2026-10-25 |
| Saigon University portal | Vietnam | [`zaikaman/SGU-Academic-MCP`](https://github.com/zaikaman/SGU-Academic-MCP) | 🟢 **MIT** · 1 068 B · `0b02f0945515` | `d5209305d13e` @ 2026-10-16 |

🔴 **Why this changes the shape of a proposal, not just its parts list.** `Trend 10` and
this file's own lead both say the platform tier is closed to permissive building — which is
true and is why `verticals/solutions.md` leads with OpenOLAT and Kolibri. 🟢 **But a
national school system is not going to migrate off IServ or Librus.** The engagement that
is actually available is a permissive **agent layer over the incumbent platform**, and
until this pass this file had no addresses for it outside Moodle and Canvas.

🟡 **Each connector is unofficial.** Every README says so: `iserv-mcp` warns that instances
differ and asks you to test against the school's own installation; `dtu-learn-mcp` is a
student project and says to use it only with your own account. 🔴 **That is a contract
risk, not a licence risk**, and it is the first question to settle in a deployment: an
unofficial client against a system of record has no API stability promise and no vendor
escalation path.

### 🟢 The public-authority tier — the platform's *owner* publishing its own code

| Authority | What is published | Grant | HEAD |
|---|---|---|---|
| **Utdanningsdirektoratet** (Udir, Norway) | [`PAS2-Public`](https://github.com/Utdanningsdirektoratet/PAS2-Public) — the new exam and test administration services, with public issues and wiki | 🟢 **Apache-2.0** · 11 325 B · `cb5e8e7e5f4a` | `489129c42c9d` @ 2026-09-25 |
| **Department for Education** (England) | [`get-information-about-schools`](https://github.com/DFE-Digital/get-information-about-schools) — the national school registry | 🟢 **MIT** · `LICENCE` 1 116 B · `e18299fd1942` | `ad46faf42690` @ 2026-10-21 |
| **Department for Education** (England) | [`education-benchmarking-and-insights`](https://github.com/DFE-Digital/education-benchmarking-and-insights) — FBIT school finance benchmarking | 🟢 **MIT** · 1 091 B · `5a22fb5576a5` | `3cdbf2cbf47b` @ 2026-10-22 |
| **Department for Education** (England) | [`teaching-vacancies`](https://github.com/DFE-Digital/teaching-vacancies) — the national teaching job service, source **and** infrastructure | 🟢 **MIT** · 1 092 B · `c561ea849ed6` | `a2d4f5fdec58` @ 2026-10-22 |
| **Oak National Academy** (England) | [`oak-curriculum-api`](https://github.com/oaknational/oak-curriculum-api) — the national curriculum as a documented API · [`oak-ai-lesson-assistant`](https://github.com/oaknational/oak-ai-lesson-assistant) — its own AI lesson planner | 🟢 **MIT** · 1 077 B | `0561df5aac12` · `c6871efa8f08` |

🟢 **This is the strongest procurement argument on this file for an EMEA public-sector
engagement**, and it is a different argument from "open source is cheaper": the buyer's own
ministry has already published the data model, the service contract and in Oak's case the
reference AI application. A proposal can cite the client's own code.

🟡 `oak-curriculum-api` and `oaknational/oak-openapi` are the **same repository** — identical
HEAD under `git ls-remote` — so this file carries one row, not two.

### 🔴 The education-ERP nil is unchanged, and this does not touch it

`p433` and `p434` recorded a **standing nil** on a permissive education ERP, confirmed
three passes running. 🔴 **Nothing above changes that.** A school-platform *connector* is
not an ERP, Udir's exam administration is not a student information system, and FBIT is a
finance analytics surface over DfE data rather than a finance system. The nil stands; what
has changed is that the **integration** layer over a national incumbent now has addresses.

## 🆕 `p434` — The education-ERP nil is now a **standing** nil, confirmed a third consecutive pass, and one carried row is corrected

🔴 **The sweep was run again verbatim** (`open source platform education ERP CRM MIT Apache`) and
returned **nil for a permissive education vertical for the third consecutive pass**. What came
back, and why each is not the answer:

| Returned | Grant | Why it is not a permissive education vertical |
|---|---|---|
| **OpenEduCat** | 🔴 **LGPL-3.0** (carried on this file) | The closest thing to an education ERP, built on Odoo. Weak copyleft — integrate, do not vendor. Not permissive. |
| **Apache OFBiz** | 🟢 Apache-2.0 | Genuinely permissive and genuinely **not education** — a general ERP framework. Already this file's `p386` answer for the permissive ERP *base*, and it remains a build, not a product. |
| **ERPNext** | 🔴 GPL-3.0 | General ERP. Strong copyleft. |
| General MIT CRMs | 🟢 MIT | Not education. |
| **CK-ERP** | — | Has education modules (`ck-teacher`, `ck-student`, `ck-registrar`…) but the announcement found dates from **2010**; stale, not a candidate. |

🟢 **So the standing sentence holds and should be quoted rather than re-derived:** *there is no
MIT/Apache education ERP.* It is why this file leads with **OpenOLAT** (Apache-2.0) and
**Kolibri** (MIT), and why `p386`'s permissive-ERP-base answer below is a *base* and not a
product. 🔵 Three independent passes have now spent a leg on this question; a fourth should quote
this row instead.

🔵 **No new platform supply this pass.** The two addresses promoted to `agents/top.md`
(`wenflow-org/wenflow`, `zhangl1001/civil-ai` — both MIT) are agent-layer, not platforms, and the
five high-traction unpromoted addresses graded in `repos/trending.md` are all copyleft,
content-licensed or ungranted. `Trend 10`'s split is unchanged: **the agent layer is permissive,
the platform layer is not.**

🔴 **One correction that matters for a special-education engagement.** This file records that
there is **no open-source special-education system of record** — unchanged, and `p434` adds the
regulatory reason it is unlikely to matter in NYCPS: that district's guidance **prohibits AI
development of IEP and 504 plans outright** (`Gap 433-B`, closed; `intel/market.md`). 🔵 So the
missing system of record is not the binding constraint there — the drafting prohibition is, and
the sellable surface is progress monitoring and accommodation *delivery* against plans a
qualified professional wrote. `compose/patterns.md` `Pattern AL` carries the split.

## 🆕 `p433` — The "education ERP" sweep returns a **standing nil**, and it is the reason this file leads with OpenOLAT and Kolibri

The brief for every pass asks for platforms *"like Odoo for ERP"*. `p433` ran that leg directly —
`open source platform education ERP CRM MIT Apache` — and the result is a **nil worth recording as
a standing fact rather than re-discovering every pass**:

| What the sweep returned | Grant | Education-relevant? |
|---|---|---|
| Apache OFBiz | Apache-2.0 | 🔴 No education module; a general ERP framework |
| Aureus ERP, Krayin CRM, Atomic CRM | MIT | 🔴 General ERP/CRM, no education vertical |
| Huly Platform | Apache-2.0 | 🔴 General, and needs strong in-house capability |
| **ERPNext** | 🔴 **GPL-3.0** | 🟡 **Lists Education among its verticals** — the nearest thing to an education ERP, and it is copyleft |
| iDempiere (GPL-2.0), Dolibarr (GPL-3.0) | 🔴 copyleft | 🔴 General |

🔴 **So: there is no MIT/Apache-licensed education ERP.** The one system that genuinely covers the
education vertical, **ERPNext**, is GPL-3.0, which puts it in this file's integrate-don't-vendor
tier alongside Moodle and Chamilo. **OpenEduCat**, already on this shelf, is the Odoo-based
education ERP and is **LGPL-3.0** — weak copyleft, which is materially better than GPL for an
AI-layer build but still not permissive.

🟢 **Which is the whole argument for how this file is ordered.** `OpenOLAT` (Apache-2.0) and
`Kolibri` (MIT) are not merely *options* in the permissive tier — after this sweep they are
**demonstrably the only ones**, and that is now a measured statement rather than a curatorial
preference. A client who needs a permissive full platform has exactly two choices; a client who
can take copyleft has many. 🔵 `Gap 433-C` applies: this is a search-channel nil, not proof of
absence — but it is the fourth consecutive pass on which the permissive platform tier has not
grown.

## 🆕 `p432` — Special education is a **platform gap**, not a product gap

Every platform row on this file treats the IEP/§504 learner as an ordinary enrolment. None of
them — Moodle, Open edX, Canvas, Sakai, OpenOLAT, Kolibri, OpenEduCat, OpenSIS — ships an
individualised-education-program workflow: goal authoring, progress monitoring against those
goals, accommodation records, or the team-review-and-sign step US law requires. The commercial
market is served here (PowerSchool Special Programs, Frontline, SEIS); **open source is not.**

That makes special education the clearest *platform-adjacent* build on these shelves: there is no
incumbent open platform to displace, and the integration surface is the SIS, not the LMS.

### The deployable pieces that do exist, graded by grant (read at HEAD 2026-10-25)

| Component | Licence | HEAD | Payload | Where it sits |
|---|---|---|---|---|
| [**AlloFlow**](https://github.com/Apomera/AlloFlow) | 🔴 **AGPL-3.0-or-later** | `6194e51e8f1f` | `LICENSE` 35 442 B · `698099632698` | …**beside, over an interface.** The only maintained accessibility-first differentiation engine found: UDL levels/layers/outputs, WCAG, AAC, text-to-speech, offline-first, i18n, Electron + React. Network copyleft over a hosted engine — reach it over HTTP, never vendor it. |
| [**California IEP AI project kit**](https://github.com/robotros/California-IEP-AI-project-kit) | 🟢 **MIT** | `ff1ae0ce30e7` | `LICENSE` 1 065 B · `43554d1189d8` | …**as the knowledge and boundary layer** on whatever drafting surface the district already has. Carries its own "not the system of record" discipline. |
| [**iep-builder**](https://github.com/67tallchris/iep-builder) | 🟢 **MIT** | `b39df0e9a4a1` | `LICENSE` 1 069 B · `aa8cfde0dc31` | …**as a standalone per-district app** (Cloudflare Pages + D1, bring-your-own-key). The deployment shape when a district will not accept a central student store. |
| [**access-to-education**](https://github.com/dougdevitre/access-to-education) | 🟢 **MIT** | `f8abd70707ba` | `LICENSE` 1 069 B · `fc7c8b90fee1` | …**in the parent portal** (`p388`'s surface). ~120 k words of IEP navigation and advocacy content, MIT-granted. |
| [**rubric-desk**](https://github.com/rwrife/rubric-desk) | 🟢 **MIT** | `010a44006014` | `LICENSE` 1 063 B · `c186f5cb204a` | …**as the offline marking surface** (Flutter, no accounts). Pairs with Kolibri where connectivity cannot be assumed. 🟡 Created 2026-10-25. |

🔴 **Not available, and it is the load-bearing piece:** an open-source special-education **system
of record**. `OpenSIS Classic` (GPL-2.0) and `Academico` (MIT) are general SIS products with no
IEP module. So the architecture is forced: the drafting assistant writes a *draft*, and the
authorised commercial system records the entry. That constraint is not a limitation to work
around — in North America it is the compliance requirement (see `intel/market.md`, North America),
and `robotros`' kit states it in its own README.

🔴 **Non-US equivalents: nil result.** No open-source tooling was found for England's EHCP
process or for the inclusive-education mandates of Brazil, Chile or Colombia. Searched; absent.

## 🆕 `p431` — Evaluation is a platform-adjacent procurement surface, and it is the one tier with no copyleft problem

This file grades **platforms**, and its standing finding is that the platform tier is copyleft while
the agent tier is permissive. `p431` measured a third tier that sits beside both and behaves
differently from either: **tutoring evaluation.**

| Component | Grant (read at HEAD, 2026-10-25) | Where it sits relative to the platform |
|---|---|---|
| [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | Apache-2.0 code / CC-BY-4.0 content / brand policy | **Beside** the platform — runs in CI, never links the LMS |
| [Teachable-AI-Lab/tutor_gym](https://github.com/Teachable-AI-Lab/tutor_gym) | MIT | **Beside** — drives the tutoring runtime through its own interface |

🟢 **Why that placement matters commercially.** An evaluation harness **never links against the
LMS**. It drives the tutoring runtime from outside and reads results. So a client on **Moodle
(GPL-3.0)**, **Open edX (AGPL-3.0)**, **Chamilo (GPL-3.0)** or **Frappe LMS (AGPL-3.0)** can take a
fully permissive evidence pack **without the platform's copyleft reaching any of it**. This is the
one tier on this shelf where the platform's licence is simply not a constraint — no XBlock seam, no
GPL-adapter sandwich, no packaging decision.

🟡 **It is also the part of a bid the incumbent platform vendor cannot supply.** Moodle, Canvas and
Open edX vendors sell delivery; none of them sells *proof that the AI teaches well*. Against the
LATAM pattern this base already records — public buyers procuring AI education platforms as
**subscriptions**, with **no tender asking for open source** (`Trend 21`) — the evidence pack is the
line item that fits: assurance work attached to someone else's platform, priced as advisory.

🔴 **Scope limit, stated:** this covers **tutoring** only. There is no open harness for the
**grading** path (`Gap 431-C`), which is the surface NA, EMEA and APAC statutes regulate hardest.
Quote grading assurance as bespoke work.

## Choosing the base — the decision in one pass

1. **Client needs a full LMS and cannot accept copyleft** → **OpenOLAT** (Apache-2.0).
   This is the under-used answer; most teams default to Moodle and inherit GPL unnecessarily.
2. **Connectivity is unreliable, or equity is an explicit requirement** → **Kolibri** (MIT).
3. **Client already runs Moodle / Canvas / Open edX** (the common case) → **do not migrate.**
   Add an MIT **MCP server** beside it. See `compose/patterns.md`, Pattern A.
4. **Client needs student records, not just courses** → **OpenEduCat** on Odoo — the only
   integrated LMS+SIS in open source. 🔴 No MIT- or Apache-licensed SIS exists; this was
   searched for again on 2026-10-25 and the gap is real, not an absence of looking.

## 🔴 What is *not* available as open source, and matters

- **A permissive SIS.** Searched again this pass; nothing MIT/Apache. OpenEduCat (LGPL-3.0)
  is the only integrated option.
- **A credible open proctoring stack for the EU.** Emotion recognition in educational
  institutions is *prohibited* under the AI Act since Feb 2025, so the category is
  substantially closed in EMEA regardless of supply.
- **An open curriculum graph on permissive terms.** The best one found
  ([os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)) is **ODbL** — share-alike
  on derived data.

---

## Choosing the base: the four-way decision

| if the client needs… | base | licence | the catch |
|---|---|---|---|
| **To own closed extensions to the platform itself** | [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | Smaller plugin ecosystem than Moodle; more build, less assemble. **The only permissive major LMS.** |
| **The widest plugin ecosystem and the largest talent pool** | [Moodle](https://github.com/moodle/moodle) | 🟡 GPL-3.0 (`COPYING.txt`) | Copyleft on anything linked. Extend through web services / the MCP plugin, not by patching core. |
| **MOOC scale, cohort analytics, deep data control** | [Open edX](https://github.com/openedx/edx-platform) + [tutor](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 | AGPL reaches **hosted** use. Build XBlocks and LTI tools; keep proprietary logic the other side of the boundary. |
| **🆕 `p389` No incumbent platform at all, and lessons needed now** | [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **MIT** | Not an LMS: no enrolment, no gradebook of record, no SIS. You get the *teaching surface* and you still owe the system of record. See the section below. |
| **🆕 `p390` To *ship* a modified platform, not host one** | [OLI Torus](https://github.com/Simon-Initiative/oli-torus) | 🟢 **MIT** | **The only permissive answer on this shelf, and the catch is staffing, not licensing.** Carnegie Mellon Open Learning Initiative's courseware engine: authoring + delivery, adaptive scripted activities, per-objective mastery reporting, LTI 1.3 delivery into a host LMS. Every other base of comparable scope here is GPL/AGPL, so this is the row to reach for when the deliverable is **software the client redistributes or embeds in a product**. 🔴 **Elixir/Phoenix + PostgreSQL** — a genuine staffing constraint; cost the hiring before proposing it. 🔴 Slug trap: `CMU-OpenLearning/oli-torus` does not resolve. Dated **2026-10-22**. |
| **🆕 `p393` To ship a small permissive LMS, in Spanish, with billing already in it** | [now-lms](https://github.com/bmosoluciones/now-lms) | 🟢 **Apache-2.0** | **21 ★** and no multi-tenancy claim. A Flask application a studio can read in a day — which is the point — but not a ministry platform. |
| **North American higher-ed integration reality** | [Canvas LMS](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0, open-**core** | The published tree ≠ the commercial ecosystem. Scope integrations against the real tenant, not the repo. 🆕 `p389` **And the published tree is also *older than it looks*: `master` last moved 2026-04-30 — 175 days — while the `stable/*` branches move.** Read the API surface off the tenant, and if you must read it off the repo, say which ref. 🟡 🆕 `p390` **Dating caveat, so nobody demotes Canvas off a bad read:** its `master` last moved **2026-04-30 — 175 days**, but Canvas **ships from tags** (`v5.14.2` current), not from the default ref. For any tag-releasing project, a last-commit-on-default-ref date under-reports maintenance; check `git ls-remote --tags` before calling it stale. |

### Regional fit
- **LATAM / Iberia:** 🆕 `p393` **the permissive option now exists and it is regional:**
  [now-lms](https://github.com/bmosoluciones/now-lms) (🟢 **Apache-2.0**, © BMO … S.A., **Nicaragua**;
  676 files, 505 commits, HEAD **2026-08-31**) is the only Spanish-language LMS on this shelf a studio
  can fork and ship **closed**. Use it for SME and pilot delivery; keep Chamilo for public-sector scale.
  [Chamilo](https://github.com/chamilo/chamilo-lms) (GPL-3.0) — strongest
  Spanish/Portuguese public-sector base. [academico-sis/academico](https://github.com/academico-sis/academico)
  (MIT) for SME-scale administration with Spanish built in.
  🆕 `p387` For **Brazil specifically**, the base a municipal engagement will already be running is
  [portabilis/i-educar](https://github.com/portabilis/i-educar) (GPL-2.0-or-later, **real default
  ref `2.12`**) — see the administration table below — and the agent tier now has three granted
  LATAM-native options on [`agents/top.md`](../agents/top.md),
  including one that ships **as an Open edX plugin** rather than as a separate app.
- **EMEA public sector:** [ILIAS](https://github.com/ILIAS-eLearning/ILIAS) (GPL-3.0, default ref
  `release_11`) and [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, Switzerland).
  🆕 `p393` For **assessment migration**, which EMEA procurement is beginning to specify as QTI 3.0:
  [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) (🔴 **GPL-3.0** — run it
  as a batch tool at arm's length, never linked), from the lab of **Cito, the Dutch national assessment
  institute**. For a **Swiss university** engagement,
  [Dathis/swiss-moodle-mcp](https://github.com/Dathis/swiss-moodle-mcp) (🟢 MIT) already speaks ZHAW,
  FHNW, ETH and EPFL Moodle with **SWITCH edu-ID** user-held authentication — 🔴 but at **0 ★** and
  self-described as an unofficial student project, so it is a pilot reference, not a dependency.
  [Serlo](https://github.com/serlo/serlo.org) (Apache-2.0, Germany) and
  [Richie](https://github.com/openfun/richie) (MIT, France) for content and catalogue.
- **APAC:** Moodle itself is Australian in origin; [netless-io/flat](https://github.com/netless-io/flat)
  (MIT) for live online classrooms.
- **Low-connectivity anywhere:** [Kolibri](https://github.com/learningequality/kolibri) (MIT,
  default ref `develop`) — offline-first by design, not as a degraded mode.
- **K-12 administration anywhere:** [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic)
  (GPL-2.0, default ref `master`) — the student-record half that no permissive base supplies.
- 🆕 `p393` **North America K-12 data integration:** the standard is **Ed-Fi**, and the granted client
  is [edanalytics/edfi_api_client](https://github.com/edanalytics/edfi_api_client) (🟢 **Apache-2.0**,
  stock 11,357 B, HEAD **2026-10-06 — 16 d**). The **Canvas / Google Classroom / Schoology → Ed-Fi**
  extractors exist at [Ed-Fi-Exchange-OSS/LMS-Toolkit](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit)
  (🟢 Apache-2.0) 🔴 **but that repository was ARCHIVED by its owner on 2025-03-10 and is read-only** —
  port its field mappings, never depend on it.

## 🔴 The sovereign-stack story in EMEA, corrected

The previous pass carried a headline that **openDesk Edu** was deployed in **8,600 German schools**
and then downgraded it to "traces to a single news item with no official confirmation". **This pass
re-ran the search and the downgrade stands — in fact it goes further:**

- What is **confirmed**: openDesk is a free and open-source productivity suite from **ZenDiS** (the
  German Center for Digital Sovereignty in Public Administration); **v1.0 released 20 Oct 2024**.
  ZenDiS works with France's **DINUM** on the French equivalent **LaSuite**, and the two agencies
  added videotelephony, note-taking and SSO to both suites in **100 workdays**.
- What is **not confirmed**: **no school deployment of openDesk appears in any source found this
  pass.** Named users are public-administration bodies (BWI GmbH for the Bundeswehr, the ÖGD public
  health service). Germany's **DigitalPakt Schule** (€6.5bn school infrastructure) is a separate
  programme and is not evidence of openDesk in schools.
- **How to use it anyway:** the *pattern* is real and sellable even if the school number is not —
  **ILIAS (learning) + OpenProject (collaboration) behind a single SSO**, all open source, all
  EU-hosted. That is the sovereign education stack an EMEA public-sector client will ask for. Sell
  the architecture; do not quote the 8,600.

## Student information and administration

| platform | repo | default ref | licence | fit |
|---|---|---|---|---|
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 `19.0` | 🟡 LGPL-3.0 | Odoo-based SIS/ERP: admissions, curriculum, fees, library, hostel. The Odoo ecosystem is the reason to pick it — AI modules can be ordinary Odoo addons. |
| **Academico** | [academico-sis/academico](https://github.com/academico-sis/academico) | `main` | 🟢 MIT | Laravel, Spanish + French built in, SME-scale: courses, enrolments, scheduling, reports. |
| **openSIS Classic** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 `master` | 🟡 GPL-2.0 — 🔴 grant at **`docs/License.txt`**, not at any root path | 🆕 `p384`. The K-12 default: enrolment, attendance, grades, scheduling, parent/student portals. GPL-2.0 is survivable the Moodle way — reach it over its API, never link. 🔵 A root-only licence read reports this repo as ungranted; it is not. |
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | 🔴 `develop` | 🔴 AGPL-3.0 (`license.txt`) | Only where the client already runs ERPNext — then the student record and the finance record are one system. |
| **i-Educar** 🆕 `p387` | [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **`2.12`** | 🟡 GPL-2.0-or-later (`2.12/LICENSE`, 18,092 B) | 🟢 **The LATAM row this table was missing.** Brazil's largest free education software — municipal student records, enrolment, grades — deployed by Brazilian municipalities at scale and maintained by Portabilis plus a community. 🔴 Its default ref is the version branch **`2.12`**: clone and read the grant there, not at `main` or `master`. Reach it over its API; keep AI alongside it, never inside it. Sibling `i-diario` (classroom diary) is **AGPL-3.0** — different grant, same organisation. |

### 🆕 `p386` — the permissive ERP **base**, since the permissive education ERP does not exist

Every row in the table above is copyleft except `academico` (MIT, SME-scale). The prescribed ERP/CRM
research leg was run directly at that gap. **It does not close it** — no education-specific
permissive ERP was found, which *confirms* the structural claim on
[`repos/foundations.md`](../repos/foundations.md) — but it returns three permissive bases, all three
licence payloads read first-hand this pass:

| base | real default ref | licence | what you get, and what you build |
|---|---|---|---|
| [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) | 🔴 **`master`** | 🟢 **MIT** *(1,077 B, "Copyright 2010-2025, Webkul Software"; `composer.json` also declares `"license": "MIT"`)* | Laravel 13 + FilamentPHP 5 modular ERP **with a plugin system**: accounting, inventory, HR, CRM, projects, and a Filament admin panel a client's staff can actually use. 🔴 **No education module** — admissions, curriculum, fees, attendance and transcripts are **your build**. |
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | 🔴 **`2.2`** *(version branch; no `main`)* | 🟢 **MIT** *(1,078 B, same Webkul holder)* | The **admissions funnel** as a CRM: lead → applicant → enrolment, with the pipeline, activity log and email already built. The piece an SIS always lacks and a school always asks for. |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 🔴 **`trunk`** | 🟢 **Apache-2.0** *(11,906 B; `NOTICE` 166 B, "Copyright 2001-2026 The Apache Software Foundation")* | The ASF alternative: accounting, CRM, manufacturing, order management. 🔴 Developer-facing and heavy — pick it for ASF governance and longevity, not for time-to-first-demo. 🆕 `p389` **Dated: `trunk` committed 2026-10-22 — 0 days. The ASF-longevity argument holds up.** 🔴 **But write the `-framework` suffix into the proposal.** [apache/ofbiz](https://github.com/apache/ofbiz) — the address anyone guesses — resolves, carries a valid Apache-2.0 grant, and its `trunk` **last moved 2017-02-12, 3,539 days ago**. It is the retired monolith. A client engineer who checks the obvious address finds a nine-year-dead tree and concludes the recommendation was careless. |

🔵 **What this changes in a pitch.** [OpenEduCat](https://github.com/openeducat/openeducat_erp)'s
**LGPL-3.0** used to be the only road to an open-source education ERP, so it was not a decision. It
is now a **trade against a named alternative**:

- **Take OpenEduCat (LGPL-3.0)** → admissions, curriculum, fees, library and hostel exist today, on
  the Odoo ecosystem, and AI features can be ordinary Odoo addons. You accept LGPL on the modules
  and the Odoo version-branch cadence (`19.0`).
- **Take Aureus (MIT) + Krayin (MIT)** → the client owns every line, including the education
  modules you write. You are costing **admissions, curriculum, fees, attendance and transcripts as
  a build**, on a base whose plugin system is designed for exactly that.

🔴 **Do not sell the second option as "an open-source education ERP."** It is a permissive ERP plus
a scoped education build, and the honest version of that sentence is the one that survives the
client's own technical review.

🟡 **Still not found, and still the clearest build-vs-buy opening in the rotation:** no open-source
Brazilian or Mexican academic-management system. Aureus + Krayin is now the most *defensible*
starting point for one — Laravel, MIT, and `academico` (MIT, Spanish-native) already proves that
stack fits the region's SME school market.

## Content, assessment and media layers

| layer | platform | licence | note |
|---|---|---|---|
| Interactive content | [H5P](https://github.com/h5p/h5p-php-library) | 🟡 **GPL-3.0** | Embeds in Moodle, Open edX, Canvas, Drupal, WordPress. 🔴 Widely mislabelled MIT. Treat as runtime content, not linked code. |
| 🆕 `p393` H5P **inside Open edX** | [edly-io/h5pxblock](https://github.com/edly-io/h5pxblock) | 🟢 **MIT** *(1,064 B)* | 🟢 **The permissive way to get H5P content into an AGPL platform.** Self-hosted H5P player as an XBlock — HEAD **2026-10-16 — 6 d**, 82 commits, 23 releases, **19 ★**. 🔵 Note the licence shape, which is `p390`'s firewall again: the **content library** above is GPL-3.0 and the **platform** is AGPL-3.0, but this bridge is MIT, so the part a studio writes against stays permissive. |
| 🆕 `p393` QTI assessment exchange | [vosslab/qti_package_maker](https://github.com/vosslab/qti_package_maker) (🟡 **LGPL-3.0**) · [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) (🔴 **GPL-3.0**) | 🟡 / 🔴 copyleft | **Write** QTI packages for Canvas/Blackboard, and **convert** QTI 2.x ↔ 3.0. The assessment-portability layer this shelf had no row for. 🔴 Neither is permissive: use the LGPL one as a **linked dependency** and the GPL one as an **arm's-length batch tool**. 🔴 A third family — PyPI's `timeback-qti` / `-oneroster` / `-caliper`, 147 releases, MIT **declared** — has an **unresolvable source repository**, so it is listed here only as a warning, not an option (`Gap 393-B`). |
| Structured pedagogy | [Oppia](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | Misconception-aware lesson branching. Permissive and pedagogically serious — unusual combination. |
| Open-response assessment | [openedx/edx-ora2](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 | Peer + self + staff assessment rubrics. The place an LLM grader must plug in to stay auditable. |
| Lecture capture | [opencast/opencast](https://github.com/opencast/opencast) | 🟡 ECL-2.0 | Video pipeline → the transcript corpus every education RAG build needs. |
| 🆕 `p390` Self-hosted video delivery | [Chocobozzz/PeerTube](https://github.com/Chocobozzz/PeerTube) | 🔴 **AGPL-3.0** | Federated (ActivityPub) video hosting — the option when lecture video must stay off YouTube and off a hyperscaler, which is a recurring EMEA public-sector requirement. 🔴 **Network copyleft: hosting it as a service for the client triggers source obligations** — fine for a public institution, usually not for a commercial product. Dated **2026-10-16**. 🔴 **A wrong-slug trap worth naming, because it inverts the licence:** [`PeerTube/PeerTube`](https://github.com/PeerTube/PeerTube) also resolves, is **3,660 days stale**, and reads **GPL-3.0** — so a careless licence read off that slug gets the *wrong grant* for the project, not merely a stale one. The canonical owner is `Chocobozzz`. |
| Live classroom | [netless-io/flat](https://github.com/netless-io/flat) | 🟢 MIT | Whiteboard, recording, real-time session. |
| Interop boundary | 🆕 `p392` [academic-innovation/django-lti](https://github.com/academic-innovation/django-lti) (**Python**) · [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) (Node) · [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) (Node, **serverless**) · [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) (PHP) | 🟢 **MIT / Apache-2.0 / MIT / Apache-2.0** | **The copyleft firewall, and as of `p392` it is maintained in THREE languages including Python.** 🆕 `p392` `django-lti` (🟢 MIT, 1,098 B, HEAD **2026-10-20**, PyPI v0.10.1) puts LTI Advantage **inside** a Django agent — one middleware, no second runtime — so `p391`'s *"the edge must be Node or PHP in front of the agent"* is withdrawn; `lti-tool/lti-tool` (🟢 MIT, HEAD **2026-10-20**, npm `@lti-tool/core` v1.3.2) is the **serverless** Node option for Lambda / Cloudflare Workers, where `ltijs` assumes a long-running process with Mongo. 🔴 `p390` dated the standards-body reference copy at 2,332 days and concluded the boundary had no installable implementation; that was wrong. **`ltijs`** — npm v7.0.7, **207 versions, published 2026-10-06**, HEAD 2026-10-13 — and **`packbackbooks/lti-1p3-tool`** — packagist v6.4.4, **68 versions, published 2026-09-23**, HEAD 2026-10-16 — are both live, both Apache-2.0, and either one keeps permissive code the right side of a GPL/AGPL platform boundary without linking to it. Prefer **`ltijs`** unless the client's platform work is already PHP. 🔴 Cite [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) as the **spec reference only** — 2,333 days, and `IMSGlobal/lti-1-3-php-library` is the same project at a renamed org (identical HEAD `3a192de`). 🔴 There is **no maintained Python LTI library**, so the edge is Node or PHP in front of a Python agent. Full note in [`repos/foundations.md`](../repos/foundations.md). |
| Local-first tutoring workspace | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** | 🆕 `p386`. Self-hosted, block-based adaptive workspace: PDF in → notes, flashcards, quizzes and an adapting tutor out, with **FSRS** scheduling, a knowledge graph and cognitive-load detection. Runs on local open-weight models — **no API key, no data leaving the host**, which is the answer to a DPO who will not approve an external model call at all. |
| Campus LLM gateway | [LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | Multi-provider, SSO, quota, audit log. The audit log is what gets a deployment past a university's data-protection officer. |
| Courseware platform | [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT** | 🆕 `p384`. Django courseware with autograding, flexible access rules and per-student statistics. Course-scale and permissive — the base when the client must own the platform code but does not need an institutional LMS. |
| **Agent-native teaching OS** | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | 🔴 **AGPL-3.0** (`main`) · 🟢 MIT at tag `v0.1.0` | 🆕 `p385`. The **inverse** of every other row here: instead of bolting an agent onto an LMS, the classroom itself is an MCP server (~50 tools) and the agent is bring-your-own. Courses, lessons, FSRS flashcards, graded exercises, and a persistent learner-memory layer (`get_context` / `get_learner_brief`) that survives a change of model or session. 🔴 **v1 is single-machine and unauthenticated** — a pilot substrate, not a tenant-ready platform. AGPL reaches hosted use, so a client deployment must either accept that or pin the MIT `v0.1.0` tag and forgo upstream. |
| **Curriculum prerequisite graph** | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL** | 🆕 `p384`. 1,930 micro-topics, 4,102 prerequisite edges, 9 subjects; aligned to NGSS, Common Core, UK National Curriculum, Australian curriculum. 🔴 **Share-alike database licence, not a code licence** — ground a tutor on it (§4.3 *Produced Work*, attribution only); do **not** ship an extended taxonomy (§4.4 *Derivative Database*, share-alike). See **Pattern H**. |

## 🟡 MCP has reached the LMS — and this is new as of 2026

This did not exist a year ago and it changes the integration story:

- 🆕 `p387` **Moodle, the tenancy layer — and this is the part a client-ready deployment needs
  before any MCP server:** [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager)
  (GPL-3.0-or-later, granted in `version.php`, release **5.1.1**) is a **multi-tenant AI backend**
  offered as the alternative to Moodle 4.5's own single-tenant AI subsystem: `aitool` subplugins
  connect providers (ChatGPT, Gemini, Dall-E, **Ollama** for on-premises), `aipurpose` subplugins
  bind a purpose to a provider **per role**, with per-role rate limits, per-tenant enable/disable,
  usage monitoring and capability-gated teacher visibility of student prompts. 🔵 The same project
  is also published at `mebis-lp/moodle-local_ai_manager` — **identical HEAD sha, one project, two
  addresses.** 🔴 Its own README warns it is **not compatible with core-AI-subsystem plugins and
  vice versa**: choosing it is an architectural fork in the road, taken once, early.
- 🆕 `p387` **Open edX, first-party AI extension point:**
  [openedx/openedx-ai-extensions](https://github.com/openedx/openedx-ai-extensions) (AGPL-3.0-only)
  is the platform org's own AI extensibility framework — **experimental**, but it is the contract to
  build against instead of forking `edx-platform`. Pair it with
  [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) for the agent-facing surface.

- **Moodle, first-party path:** the **`webservice_mcp`** plugin in **Moodle's own plugin directory**
  (and the Moodle Marketplace) exposes Moodle's external functions as **MCP tools over JSON-RPC
  2.0**. Supports **Moodle 4.5–5.2**, latest release **23 Jul 2026**, gated on the
  `webservice/mcp:use` capability. Configured inside Moodle — no fork, no patch, **no GPL exposure
  for the agent on the other side of it.**
- **Canvas, community path:** [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (MIT)
  and its fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (MIT, adds office
  hours, syllabus read/write, student groups, course-content copy).
  [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) advertises 54
  tools and Streamable HTTP; it has **no licence file**, but `package.json` declares
  `"license": "MIT"` — 🟡 **manifest-only MIT**, usable if you record the manifest line and ask for
  the file.
- 🆕 `p386` **Blackboard, community path — and it is no longer empty.** Nine addresses probed,
  **6 MIT grants read first-hand**, 1 ungranted, 2 dead. 🟢 **[nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp)
  (MIT) is the only institution-grade LMS MCP server on any of these shelves**: official Blackboard
  Learn REST API, OAuth2, role gate, FERPA handling, rate limiting, PII scrub, JSON audit log,
  Prometheus `/metrics`, 40 tools including **grade write-back** (maintainer self-claims, read not
  executed). The other five —
  [Mattlo0546](https://github.com/Mattlo0546/blackboard-mcp),
  [alanwtom](https://github.com/alanwtom/blackboard-mcp),
  [lukecarroll15](https://github.com/lukecarroll15/blackboard-mcp) (ref **`tcd`**),
  [felipedias-ie](https://github.com/felipedias-ie/blackboard-mcp),
  [Loganxgreaves](https://github.com/Loganxgreaves/blackboard-mcp) (ref **`master`**) — are
  **student-side**: they ride the signed-in user's own browser SSO session. 🔴 Granted, useful, and
  **not deliverable to an institution**.
- 🆕 `p386` **Brightspace / D2L — six addresses, six MIT grants.**
  [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) is the fullest
  (TOTP/OAuth/browser auth strategies, retry + circuit-breaker + cache, **opt-in writes**);
  [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) is the
  upstream of a fork family whose copies publish **byte-identical** licence payloads, so count it
  once. 🔵 **All six are student-side** — an institution-grade D2L server is the one genuine
  greenfield contribution left on this platform.
- **No official server** from Instructure, Moodle HQ, Anthology/Blackboard or D2L. 🟡 Verified gap —
  every server named on this shelf is community-built.
- 🔴 [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) is **UNGRANTED** — no licence file
  *and* no `license` field in its `pyproject.toml`. Use the plugin-directory route for Moodle:
  [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) has no root
  licence file either, but its `version.php` carries the full **GPL-3.0-or-later** header that
  Moodle requires of every plugin, so it *is* granted.

## 🆕 `p388` — The parent portal is a platform surface, and it was missing from this shelf

This shelf asks *"what does the client already run, and what can be bolted onto it?"* For every
platform below it answered that for **the learner, the teacher and the administrator**. It never
answered it for **the parent** — yet in K-12 the parent portal is a shipped feature of every SIS and
the one surface families actually log into.

| platform | server | ref · HEAD | licence | what it bolts on |
|---|---|---|---|---|
| **Infinite Campus** (Campus Parent) | [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` · `971d58f` | 🟢 **MIT** (1,067 B) | 🟢 **The first SIS parent portal on this shelf.** 20 tools: schedule, assignments (`missingOnly`), grades + 14-day recent window, **attendance events with codes and comments**, behavior, food service, documents, standardized **assessment scores**, fees, messaging from three sources. Linked districts auto-discovered via **CUPS SSO**; `FeatureDisabled`-aware, so a district that has switched a module off degrades instead of erroring. **47 npm releases**, → 2026-10-19. |
| **Canvas** | [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` · `428b78b` | 🟢 **MIT** (1,067 B) | 18 `canvas_*` tools held to **the read-only observer surface** (`canvas_list_observees` is the hinge) plus student self-access; four auth modes in priority order; hardened file download (host-pinned, directory-confined, no symlink writes, `0600`). **43 releases**, → 2026-10-16. |

🔵 **Why it belongs on the *verticals* shelf and not only on the agents shelf.** Infinite Campus is a
**major North American K-12 SIS** that this base has only ever been able to name as a proprietary
system with nothing attachable. It now has a granted, maintained, MIT integration surface — so the
"what can be bolted on" answer for a US K-12 district changes from *nothing* to *the parent portal*.

🔴 **The boundary that decides the engagement, and it is not a licence boundary.** Both servers
authenticate as **a person** — a parent's own token, OAuth, or a scraped session. Deployed by a family
for their own child, that is the parent exercising their own access. **Hosted by a studio on behalf of
a district, the same call becomes an institutional disclosure of an education record and FERPA
governs it.** The code is identical; the obligation is not. 🆕 `Pattern P` in
[`compose/patterns.md`](../compose/patterns.md) is built around that line, and it is the same
tenancy problem `p386` found for student-side LMS servers — **the parent surface inherits it
unchanged**, which is worth knowing before a district pilot is scoped.

## 🆕 `p388` — Canvas: the integration surface reordered, and a FERPA mode shipped as a feature

`p387` recorded that the richest Canvas server (`canvas-mcp-server`, 54 tools) had not shipped since
**2025-06-27**. For a client engagement that mattered and there was nothing better to recommend.
There is now:

- 🟢 **[bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp)** — `main` · `34e6156`,
  🟢 **MIT** (1,070 B), `canvas-lms-mcp` **v2.9.0 across 87 releases, 2026-04-13 → 2026-10-22
  (today)**. **187 tools on the teacher/admin surface**, including the ones an institution asks about
  and demos usually lack: gradebook *history*, quiz **accommodations**, grading standards, content
  exports and migrations, outcomes, analytics, appointment groups, plus **link audit**,
  **accessibility audit** and **grade projection**. Three deployment modes (stdio, HTTP, library
  import). 🟢 **It ships a FERPA mode.** That is the first time on these shelves that an education
  compliance regime appears as a *product feature* of an open-source component rather than as a
  caveat this base has to supply — and in a procurement conversation it is worth more than the tool
  count.
- 🟢 **[Fireiscoolsolo/canvas-lms-mcp-local](https://github.com/Fireiscoolsolo/canvas-lms-mcp-local)**
  (`c7e5725`) and its remote twin
  **[`-server`](https://github.com/Fireiscoolsolo/canvas-lms-mcp-server)** (`8e424f1`) — 🟢 **MIT**
  (1,091 B each), **209 tools on the student surface**, split deliberately into a **Local Edition**
  that opens no port and a **Remote Edition** on ngrok with OAuth 2.1 and multi-computer failover.
  🔴 The Remote Edition exposes a **public HTTPS address**: a school's decision, never a default, and
  not a thing to leave switched on in a pilot.

🔵 **Pick by persona, not by tool count.** 187 (teacher/admin) vs 209 (student) vs 20 (parent) is
**scope**, not quality: three different people reading the same institutional data. An engagement
usually needs one, occasionally two, and should deploy them separately — the FERPA posture differs
per surface, and a single server covering all three personas would be the hardest version of this to
get approved.

🟢 **And a wider Moodle surface than `webservice_mcp`:**
[gafapa/moodlia-cli](https://github.com/gafapa/moodlia-cli) — `main` · `7962e49`, 🟡 **GPL-3.0**
(284 B short-form notice) — a Node client and CLI against Moodle Core web services **plus the MoodlIA
plugin, a 250-operation contract**, Moodle 4.5+, with an optional experimental **WebMCP** browser
path. GPL survives here for the same reason it does for `webservice_mcp`: the agent reaches it over
REST, it is not linked.

## 🆕 `p389` — The generated classroom as a platform (OpenMAIC)

[THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 🟢 **MIT**, Tsinghua University, real
default ref `main` @ `269fde2d991f`, **committed 2026-10-22 (0 d)**, ~41.3k ★. Grant read from the
payload: `LICENSE` is stock MIT text, `package.json` declares `"license": "MIT"`.
🔴 **A 2026 third-party review of this project reports it as AGPL-3.0 with paid commercial licensing.
That is false** — see [`agents/top.md`](../agents/top.md#-two-licence-traps-that-a-badge-read-would-miss).

**Why it belongs on *this* shelf and not only the agent shelf.** Every other row here is a system of
record that AI gets bolted onto. OpenMAIC inverts it: the artefact is a **classroom** — narrated
slides, an AI teacher with a voice, teaching assistants, simulated classmates, auto-graded quizzes,
HTML interactives, a shared whiteboard — generated from a topic or an uploaded document, and then
*taught*. It is a Next.js 16 / React 19 / TypeScript application on **PostgreSQL 16**, self-hosted
with Docker, and it has the three properties that separate a platform from a demo:

| property | what it is | why an institution needs it |
|---|---|---|
| **Server-first generation** (v1.2.0) | Generation runs on the server, survives closed tabs and restarts; the web app and the API share one pipeline | A teacher who closes a laptop does not lose a lesson. The demo-grade alternative generates in the tab. |
| **Central model governance** | Every AI use is a named **slot** in `openmaic.yml` (outline, slide content, TTS, web search, …), each pinned to a declared provider, keys referenced as `${VAR}` from `.env.local`; a capability is switched off with `video: null`, and the server can be configured to **forbid user-supplied keys** | This is the artefact a district's AI policy is actually written against: *which model saw student input, under whose contract*. Almost nothing else in this base can answer that in one file. |
| **Export to one offline HTML file** | A finished classroom exports as a single self-contained HTML that plays the lesson, or as a PPTX that keeps every scene | The low-connectivity story (`Pattern D`) **and** the procurement story: a reviewer can be sent the lesson without being given access to the system. |

🟢 **Local inference is a supported path, not a fork:** **Lemonade** for local models and **FunASR**
for local ASR, so a deployment that may not send audio or text off-premises has a configuration
rather than a rewrite. 🟢 **Provenance:** grew out of **MAIC**, run inside Tsinghua and validated on
**700+ students**; paper in **JCST 2026**. 🟢 **Security handled as product work** — five releases
since September 2026 carry SSRF, DNS-rebinding, access-token-expiry and provider-redirect fixes under
published GHSAs, which is a maturity signal almost nothing else on the agent shelf has.

🔴 **What you still owe, and it is the whole administrative half.** No enrolment, no gradebook of
record, no transcripts, no SIS, no LTI story stated. It is a **teaching surface**, so in an engagement
with an incumbent LMS it sits *beside* Moodle/Canvas/Open edX as a content and delivery tool, and the
system of record stays where it is. 🔴 **Pin the ref.** Head is **v1.3.0-rc.1** (knowledge base,
2026-10-22) and the project states **breaking upgrade conditions with no rollback below that
release**; a pilot pins **v1.2.1** (2026-10-18). 🔴 **Operational floor:** Node ≥ 22.19, pnpm ≥ 10,
PostgreSQL 16, a long-running server — Vercel is capped at the 1.1.x line, so "we'll put it on Vercel"
is a downgrade, not a deployment.

🔵 **Where it lands by region.** Origin is **APAC** (China), the interface is EN + zh-CN, and the
provider catalogue is built for a market that includes DeepSeek and Kimi alongside OpenAI, Anthropic
and Gemini. For an engagement under **EU AI Act** or **FERPA** constraints the slot-pinning and
forbid-user-keys controls are an asset, and the *data-residency* question is answered by the local
Lemonade/FunASR path — but the assessment features (auto-graded quizzes, mastery signals) are exactly
what Annex III and Vietnam's Decision 33/2026 treat as high-risk, so human review of any consequential
score is a build item, not a setting. See [`intel/trends.md`](../intel/trends.md).

## What is *not* available as open source, and matters

An informed gap, recorded so silence is not mistaken for coverage:

- **No open-source equivalent of Khanmigo or LearnLM.** The pedagogically-tuned model layer is
  closed across the board; the open supply is agents and scaffolding over general models.
- **No open-source Brazilian or Mexican academic-management system was found.** A targeted search
  for SIGAA source and for Portuguese/Spanish-language academic management on GitHub returned
  nothing usable. `academico` (MIT) and Chamilo are the closest fits, neither region-native at
  university scale. See [`intel/market.md`](../intel/market.md) — this is the clearest
  build-vs-buy opening in the current rotation.
- **No official Instructure or Moodle-HQ MCP server** (community only, as above).
- 🔴 🆕 `p392` **~~Proctoring and AI-detection have no credible permissive open-source option~~ —
  WITHDRAWN. There are two granted components, and one of them is clean.**
  [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) (🟢 **MIT**, 1,069 B,
  manifest agrees, HEAD **2026-09-28**, npm v0.5.1) does tab-switch, camera, **face** (face-api on
  TF.js, in-browser), audio and **virtual-camera / loopback / screen-share** detection, and states
  *"nothing leaves the page unless you set `backend.endpoint`"*.
  [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) (🔴 **grant
  CONFLICT** — Apache-2.0 payload, ISC manifest and npm; HEAD **2026-10-13**, 398 commits) is the
  bigger codebase but ships **lockdown and event telemetry only** — its README marks object
  detection, multi-face and eye tracking *"(To be Done)"*.
  🔵 **What survives of the old sentence, and it is the half worth saying to a client:** the
  *liability* boundary is real and unchanged — an exam decision driven by either component makes the
  client a **deployer of an Annex III high-risk system** (standalone obligations from **2 Dec 2027**).
  The absence of code was never what made proctoring expensive; the obligations are. 🟢 So the honest
  advice flips from *"we cannot build this"* to **"we can build this, and here is what it commits you
  to"** — see [`compose/patterns.md`](../compose/patterns.md) `Pattern Y`. Full rows on
  [`repos/foundations.md`](../repos/foundations.md).
