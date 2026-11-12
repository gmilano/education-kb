---
industry: education
region: Global
updated: 2026-11-12
---

## 🆕 `p797` — **the provenance column re-measured against first-hand bytes: `83` twelve-hex cells on this base's recommendation shelves are TWO object kinds and a third that resolves to neither. `43` commit · `9` blob · `31` unresolved. `ACTION p796-B` discharged, and its premise inverted.**

🟢 **`ACTION p796-B` DISCHARGED — as a measurement, which is not what it asked for.** The action read `T905` as *"the column mixes hash functions and holds values matching neither, so DELETE it"* and argued deletion *"is one pass and cannot fail"*. 🟢 **It did not need to be deleted. It needed to be TYPED.** Machine output: [`provenance-cell-kinds`](../evidence/provenance-cell-kinds.2026-11-12-p797.tsv).

| What the `12`-hex cells actually are | Count | |
|---|---|---|
| 🟢 **A COMMIT sha — `HEAD` at measurement time, still current today** | 🟢 **`43`** | Resolvable, useful, and silently a different object kind from its neighbours |
| 🟢 **A licence-file BLOB sha — still current today** | 🟢 **`9`** | What the column's name implies throughout |
| 🔴 **Resolves to neither today** | 🔴 **`31`** | 🔵 **Mostly not an error: an old `HEAD` on a repository that has since been pushed.** [`odoo/odoo`](https://github.com/odoo/odoo) carries two such cells on one line; [`ankitects/anki`](https://github.com/ankitects/anki)'s went stale **hours** before this pass (`T927`) |

🔵 **So the defect is not wrongness, it is AMBIGUITY: the same `12` hex characters in the same visual position mean a commit on one row and a blob on the next, with nothing in the cell to say which.** 🔴 **A reader cannot verify any of them without guessing the object kind first.** 🟢 **`52` of `83` resolve today, so deleting them would have thrown away working provenance to fix a labelling problem** — and the `31` that do not resolve are the staleness signal this base otherwise pays a maintenance sweep to produce.

🟢 **Rule adopted, and every cell written at `p797` follows it: a provenance cell carries its KIND — `blob <sha>` or `HEAD <sha>` — or it does not go in.** 🔵 Re-typing the `83` historical cells is mechanical, needs no network, and is queued as `p797-B` with the instrument already built and its output published.

### 🆕 `T925` — a brand restriction can live in a different REPOSITORY from the code

🔴 **[`frappe/education`](https://github.com/frappe/education) (`19 B` grant by reference) and [`frappe/lms`](https://github.com/frappe/lms) (AGPL-3.0, `33,893 B`) carry no brand instrument at all.** 🔴 **The policy that governs their brand is `TRADEMARK_POLICY.md` in [`frappe/erpnext`](https://github.com/frappe/erpnext), and it grants permission only to NON-COMMERCIAL projects.** 🟢 **Clear the brand at the project FAMILY** → [`verticals/solutions.md`](../verticals/solutions.md) `p797`, [`intel/trends.md`](../intel/trends.md) `T925`.

### ✏️ Corrected in place below

| Row | Published here | ✏️ `p797` |
|---|---|---|
| ✏️ [`ankitects/anki`](https://github.com/ankitects/anki) | `1,930 B` | ✏️ **`1,937 B`** · blob `1296baf6f4a0` — upstream commit `9c539a036804`, `2026-11-12 16:06:11 -0300`, *"docs: update logo copyright holder in LICENSE"*. 🔴 **Plus two grants this base had not recorded: a bespoke logo licence requiring the logo be used UNMODIFIED, and `CC BY-SA 4.0` on `docs-site/`** |
| ✏️ [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) | `1` grant block | ✏️ 🔴 **three, with a table of contents: GPL-3.0 + CodeIgniter + Twitter Bootstrap, plus a Glyphicons attribution.** 🟢 The GPL-3.0 verdict stands |
| ✏️ [`frappe/erpnext`](https://github.com/frappe/erpnext) | `34,916 B` | ✏️ **`35,149 B`** · blob `f288702d2fa1` — 🔴 **the figure `p796`'s own census published the same day** |

## 🆕 `p796` — **the first licence-FILE census this base has run: `19` rows with no root licence file, `13` with two or more, and `5` serving more than one GRANT. `EUPL-1.2` added as a family. `DSpace`'s `91,354 B` third-party anthology opened and reframed.**

### 🟢 `EUPL-1.2` — the third licence family this base's clause set was missing, and the European one

| Repo | ★ | Licence (byte-verified) | Region | Why it is here |
|---|---|---|---|---|
| 🟢 [`hedyorg/hedy`](https://github.com/hedyorg/hedy) | `1,697` | 🟢 **`EUPL-1.2` · `13,827 B`** · pushed `2026-11-06` | EMEA 🇳🇱 | 🟢 **Gradual-syntax programming environment for schools, multilingual by design.** 🟢 The highest-starred `EUPL-1.2` row in this base, and actively maintained |
| 🟢 [`open-education-api/specification`](https://github.com/open-education-api/specification) | — | 🟢 **`EUPL-1.2` · `13,827 B`** | EMEA 🇳🇱 | 🟢 **OOAPI — the Dutch higher-education interop specification.** 🟢 Its licence text is **byte-identical** to `hedy`'s, which is a positive cross-check on both |
| 🔴 [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) | — | 🟡 `EUPL-1.2` · `13,865 B` | EMEA | 🔴 **ARCHIVED upstream (`T901`) — last push `2024-02-14`.** The EMEA credential vocabulary; usable as a data model, not as maintained code |

🔵 **Why this is a commercial fact and not a taxonomy note: `EUPL-1.2` is the European Commission's own licence, it is COPYLEFT, and it is the one licence here with a statutory compatibility list rather than a compatibility opinion.** 🔴 **It is also the licence an EMEA public-sector education engagement is most likely to actually meet.** 🟢 **GitHub's SPDX independently returns exactly these `3` rows as `EUPL-1.2`.**

### 🔴 Multi-grant rows — the unit is the GRANT, not the file (`T915`)

| Repo | Root licence files | 🔴 Grants served | 🔴 What the engagement inherits |
|---|---|---|---|
| 🔴 [`odoo/odoo`](https://github.com/odoo/odoo) | `1` | 🔴 **`2`** | `LGPL-3.0` at line `15`, then the **full `GPL-3.0` text** at line `183` of one `43,529 B` file. 🔵 The LGPL bound this base spent `p222`–`p225` resolving is the *first* grant in a file that also carries the GPL verbatim |
| 🔴 [`jkbrzt/rrule`](https://github.com/jkbrzt/rrule) | `1` | 🔴 **`2`** | Its own BSD-3 **plus `python-dateutil`'s**. Both notice sets travel with any distribution |
| 🟡 [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | `1` | 🟡 **`2`** | Apache-2.0 **+ a Creative Commons grant** in one `12,227 B` file. 🔴 GitHub reports `Apache-2.0` and drops the CC half (`T916`) |
| 🔴 [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | `3` | 🔴 **`3`** | Ridered BSD (`T900`) + **MIT and BSD inside `LICENSE_HISTORY`** — the relicensing record, which is why that file grades "clean" |
| 🟢 [`kumaken-1/school-office-generative-ai-30`](https://github.com/kumaken-1/school-office-generative-ai-30) | `2` | 🟢 **`2`** | MIT on the code, **CC BY 4.0 on every quest text and printable**. 🔴 GitHub reports `MIT` and drops the content licence (`T916`) |

🔴 **`19` rows serve NO root licence file. `12` more serve one this pass could not grade** — the `3` `EUPL-1.2` rows (now graded), `frappe/education`'s `19 B` name-only file, `anki`'s `1,930 B` pointer (`T919`), `1edtech/caliper-spec`'s `12,402 B` specification licence, `Dirigo`'s `362 B` Spanish `CC BY-NC-SA`, `paes-mcp`'s bilingual MIT, and `4` short notices. 🟢 **Published as two numbers rather than one.**

### 🟢 `DSpace` — the anthology opened, and it is a procurement asset (`T920`, `p795-C`)

| Repo | Root grade | 🟢 What `LICENSES_THIRD_PARTY` (`91,354 B`) actually holds |
|---|---|---|
| 🟢 [`DSpace/DSpace`](https://github.com/DSpace/DSpace) | 🟢 `BSD-3-Clause` · `1,504 B` | 🟢 **`721` dependency entries grouped by licence, plus the project's own policy in the preamble: *"DSpace actually does NOT allow for any dependencies that are solely released under GPL terms."*** 🟢 **Policy verified: the `GPL-3.0` section has exactly ONE entry (`juniversalchardet:2.5.0`) and it is also listed under `LGPL`, i.e. dual-licensed.** 🟡 **Real exposure: ~`13` `LGPL`-named entries** — `openpdf:2.0.5`, `jna:5.18.1` (`LGPL-2.1-or-later`), `JHighlight:1.1.1`, `FindBugs-Annotations:3.0.1u2`, and `8` `java-json-tools` artefacts. 🟢 Low risk server-side; the first question a legal review asks |

🟢 **`DSpace` is the only platform in this base that ships a pre-built third-party licence disclosure.** 🔵 **Hand it to the client's legal review instead of generating one.** 🔴 **Every other `Deps` cell in this base remains a claim about a version nobody identified** — carried as `p796-C`.

### 🟢 Census summary — `ACTION p795-B` discharged

🟢 **`176` addresses · `174` OK · `2` `EMPTY_TREE` · `0` clone failures · `16` seconds at `12` parallel.** 🟢 **The `2` empty trees are the same two rows for a fourth consecutive pass — `0` drift.** 🔴 **`7` first-run `CLONE_FAIL`s were my own address list, not the internet: `6` rows prefixed `NEW/` and one literal `OWNER/REPO` placeholder inside [`evidence/master-row-measurements.2026-11-12-p794.tsv`](../evidence/master-row-measurements.2026-11-12-p794.tsv).**


## 🆕 `p795` — **The rider gate this file needed was specified to key on GitHub's SPDX, and `27.5%` of this file's rows have no SPDX. Rebuilt on the bytes it found a per-FILE proprietary carve-out in the BI row this file recommends, and a `19`-byte "licence" that grants nothing.**

### 🔴 `ACTION p794-B` discharged — and the gate had to be rebuilt before it found anything

🔴 **As specified (*"exceed the canonical size for its family"*, family from `gh api search/repositories`), the gate flagged `0` of `167` rows** — including `open-webui`, whose rider is why the action was queued. 🔵 **A rider is the reason a classifier abstains, so riders and `NOASSERTION` are the same population.**

| Channel | Usable family | Blind |
|---|---|---|
| GitHub SPDX | `121` / `167` | 🔴 **`46` = `27.5%`** (`26` `NOASSERTION` + `20` `NONE`) |
| 🟢 Licence **bytes**, title line | 🟢 `149` / `155` graded files | `6` `UNRECOGNISED` — 🟢 and that is the rider signal itself |

🟢 **Rule for this file: grade from the bytes, use GitHub's SPDX only as a disagreement alarm.** 🟢 **The two channels agreed on `118`/`118` at `p794` and disagreed usefully on `3` this pass (`T910`).**

### 🔴 `T912` — the BI row: the boundary is per-FILE, and the prohibited act is the one this file recommended

🔴 **`metabase/metabase` has FOUR root licence files, not two.** 🔴 **`LICENSE-EMBEDDING.txt` (`8,877 B`) governs the single file `app-embed.js`, carves it out of AGPL (*"free and clear of any Affero GPL License requirements"*), forbids modifying or overlaying the embedded element, and `§3` forbids *"the removal of the Metabase's name or logo in the iframe that is embedded in your application."*** 🔴 **This file recommended metabase as the BI layer under learning-analytics dashboards — embedding it white-labelled is exactly what `§3` prohibits.** 🟢 **Corrected in place; the deployable form is to run metabase as its own AGPL-3.0 application and link to it.** 🔵 **Same shape as `T900`, different row, same gate, same pass.**

### 🔴 `T913` — a `19`-byte declaration is not a grant

🔴 **`frappe/education` `license.txt` is `19` bytes: `License: GNU GPL V3`** (blob `beca17940a71`, no trailing newline). ★`707`, LIVE, pushed `2026-10-30`. 🟢 **GitHub's `NOASSERTION` is right.** 🔵 **The holder named a licence without shipping one — no grant text, no copyright line, no disclaimer.** 🔴 **A client can rely neither on GPL-3.0 terms never published nor on permission never granted.** 🟢 Graded **`DECLARED-GPL-3.0-NO-GRANT-TEXT`**; the remedy is a free upstream issue. 🟢 **This also resolves the identity of `T905`'s `19`-byte file.**

### 🔴 `T910` — `3` licence grades this file would have got wrong, and GitHub got right

🔴 **EUPL-1.2's Appendix names *"GNU Affero General Public License (AGPL) v. 3"* at line `269`, so a body-substring probe mis-families every EUPL row as AGPL-3.0** — `hedyorg/hedy`, `open-education-api/specification` and `european-commission-empl/European-Learning-Model`, all three `EUPL-1.2`, all three called `AGPL-3.0` by my probe. 🔵 **Paired with `p794`'s `ECL-2.0` finding this is a complete statement of the failure mode:** 🔴 **`ECL-2.0` is MISSED because its body omits the title it derives from; `EUPL-1.2` is MIS-CALLED because its body contains the titles of licences it is not.** 🟢 **Match the first non-blank line only; and note byte size would have caught it too — `13,827 B` is nowhere near AGPL-3.0's `34,523 B`.**

### 🟢 `ACTION p794-C` — discharged for `oppia`, CONFIRMED, and honestly scoped

🟢 **`mutagen==1.47.0` verified on the second instrument: PyPI `/pypi/mutagen/1.47.0/json` returns `license: "GPL-2.0-or-later"` and the OSI `GPLv2+` classifier.** 🟢 **Both channels agree, the pin is DIRECT (`requirements.in:25`, `requirements.txt:1079`), and the GPL-2.0-not-AGPL-3.0 distinction this file's `oppia` deliverable rule rests on HOLDS.** 🟢 **No correction needed — and `T884` is why a version-level claim still had to be checked.**

🔴 **Scope limit, named rather than hidden: `p794-C` asked for EVERY remaining `Deps` cell and only `oppia` was done.** 🟢 **Next target identified with the channel already proven:** `DSpace/DSpace` ships `LICENSES_THIRD_PARTY` at **`91,354 B`** in its root tree — a dependency-licence anthology no pass here has opened. 🔵 **Re-queued as `p795-C`, fourth carry.**

### 🔴 `9` rows this file recommends are STALE and carry no archived flag (`ACTION p794-A`)

🟢 **The archived count is CLOSED at `3`** — `164` further rows measured, `0` new, so `T901`'s "the `3` is a floor" is **refuted**. 🔴 **But `pushed_at` exposes `9` rows untouched beyond `24` months**, two of which this file actively recommends:

| Repo | ★ | 🔴 Last push | Consequence, graded by kind |
|---|---|---|---|
| 🔴 [`jkbrzt/rrule`](https://github.com/jkbrzt/rrule) | `3,752` | `2024-06-27` (`28` mo) | 🟢 **Near-harmless** — recurrence rules are frozen mathematics. 🟡 Pin the version; own the fork knowingly |
| 🔴 [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) | `17` | 🔴 **`2018-07-16` (`88` mo)** | 🔴 **An SIS holding student records, unmaintained for over seven years = a fork the engagement owns on day one, under CVE pressure.** 🔵 `p790` rescued its GRANT; no pass asked about its LIFE |

🔵 **Second landing of `p794`'s lesson: a licence rescue is not a viability rescue.** 🟢 Full `9`-row table and the `12`–`24` month watch list in [`repos/trending.md`](trending.md).

## 🆕 `p794` — **`3` repositories this file recommends are ARCHIVED upstream, and the sector's own licence (`ECL-2.0`) is one that no generic probe can see.**

🟢 **All `170` addresses in this base re-measured on three channels** — three-state existence, a multilingual root-grant probe on blobless trees with lazy blob reads, and `gh api search/repositories` for exact stars, SPDX, `pushed_at` and `archived`. 🟢 **`0` clone failures · `118/118` licence agreement with GitHub's own classifier · `1` grade corrected.** Machine output: [`evidence/master-row-measurements.2026-11-12-p794.tsv`](../evidence/master-row-measurements.2026-11-12-p794.tsv).

### 🔴 `T901` — the field this file never had

🔴 **The word *archived* appeared `0` times in this file before `p794`.** Three rows below are archived upstream and are now labelled: **Mahara** (`2023-11-16`), **MyScriptJS** (`2021-01-04`), **European Learning Model** (`2024-02-14`). 🔴 **`git ls-remote` cannot tell an archived repository from a healthy one** — `rc=0`, refs present, valid `HEAD`, licence grades fine. 🟢 `archived: true` is free in the same call that returns the star count.

🔵 **Two lessons this file should carry forward:** 🔴 **resolving canonicity is not resolving maintenance** — this file correctly records `mahara/mahara` as DEAD and `MaharaProject/mahara` as canonical, and the canonical address is the archived one. 🔴 **A licence rescue is not a viability rescue** — `MyScriptJS`'s grant was rescued at `p786` and nothing has been pushed to it in nearly six years. 🟡 Grade the consequence by kind: an archived **data model** may legitimately freeze; archived **application code** is a fork the engagement now owns.

### 🟢 `ECL-2.0` — the one licence family a generic probe structurally cannot find

🟢 **Sakai, Opencast and `SakaiXAPI-Provider` are `ECL-2.0`** — Apache-2.0 with §3's patent grant narrowed for education. 🔴 **The string `"Apache License"` occurs `0` times in the text**, and **Opencast's ECL-2.0 is `11,340 B` against canonical Apache-2.0's `11,358 B` — `18` bytes apart.** 🔴 **So title matching misses it and size matching mis-grades it;** the only reliable discriminator is the phrase *"Educational Community License"*.

🔵 **And the narrowed patent grant is a real diligence item this file has never stated.** §3: *"Any patent license granted hereby with respect to contributions by an individual employed by an institution or organization is limited to patent claims where the individual that is the author of the Work is also the inventor … and where the organization or institution has the right to grant such license under applicable grant and research funding agreements."* 🟡 **Copyright permissions identical to Apache-2.0; patent coverage materially thinner — and these codebases are overwhelmingly university-contributed.** 🟢 **Still permissive, still shippable — just not "basically Apache".**

### 🟢 `23` rows where the bytes beat GitHub's `NOASSERTION`

🔴 `metabase/metabase` **AGPL-3.0** (`★50,301` — §13 reaches a hosted service) · `odoo/odoo` **LGPL-3.0** · `ankitects/anki` **AGPL-3.0** · `INGInious/INGInious` **AGPL-3.0** · `openeducat/openeducat_erp` **LGPL-3.0** · 🟢 `Gego-K12/gegok12` **MIT** · 🟢 `getodk/collect` **Apache-2.0** · 🔴 `TarrySingh/…Tutorials` **CC-BY-NC-SA-4.0** · 🔴 `Tzxser/aipha-learning-os` **PROPRIETARY** · 🔴 `open-webui/open-webui` **BSD-3-Clause + rider** (`T900` — 🟢 **the one row where the classifier was more honest than this file**) · 🔴 `CaviraOSS/PageLM` **NON-COMMERCIAL + NO REDISTRIBUTION** behind an MIT incipit (`T908`, `p795`) · 🔴 `Oriole-FDU/Wisepen` **Business Source License 1.1 — source-available, not OSS** (`p795`) · 🔴 `frappe/education` **DECLARED-GPL-3.0-NO-GRANT-TEXT** (`T913`, `p795`).

### 🔴 Corrected in this file

| Row | Was | 🟢 Now |
|---|---|---|
| `open-webui/open-webui` | 🟢 *"BSD-3-Clause … the quickest compliant front end"* | 🔴 **`BSD-3-Clause + branding rider`, non-OSI — cannot be delivered white-labelled** (`T900`) |
| `Kosudo/nextSIS` | 🔴 **`PROPRIETARY`**, stale since `p790` corrected it | 🟢 **`GPL-3.0`**, `39,890 B`, reproduced on the bytes |
| `Mahara` · `MyScriptJS` · `European Learning Model` | no maintenance field | 🔴 **ARCHIVED, with last-push dates** |
| `1edtech/caliper-spec` | 🔵 `UNGRADED` | 🔵 **Positively identified: IMS Global *Specification Document License* — non-OSI, requires agreement to terms. `UNGRADED` was the right call; this is the name of the thing** |
| `frappe/education` | 🔴 Published as **`GPL-3.0`** in a table cell *and* as a `19`-byte reference in prose, with **three different shas** | 🔴 **The prose is right and the cell is wrong.** `19 B`, `License: GNU GPL V3` and nothing else — **a declaration, not a conveyance.** Blob sha `beca17940a71`, reproduced |

### 🟢 `ACTION p793-C` — NOT done, and named as a scope limit rather than logged as blocked

🔴 **`p793-C` asked for the lockfile audit to be extended to every remaining `Deps` cell.** 🔴 **It was not done this pass.** 🔵 The pass's budget went to `p793-A`, `p793-B` and the three regional gaps (`p793-D`/`E`/`F`), all of which discharged — and the two findings that displaced it (`T900`, `T901`) were both **corrections to rows this file actively recommends**, which outranks extending a clean audit. 🟢 **The method remains proven on three rows and both channels; `oppia`'s `mutagen==1.47.0` GPL-2.0 finding is still unverified against the second instrument.** 🔵 **Re-queued as `p794-C` with the same priority, not silently dropped.**

## 🆕 `p793` — **`ACTION p792-A` discharged on the row that carries this file's whole argument: `kolibri`'s dependency claim is EXACT, and the half nobody had measured is clean.**

🔴 **`p792-A` was blunt about the stakes:** *"`kolibri`'s '2 LGPL of 32' is now the row carrying the embedding argument and it has never been lockfile-resolved… until this is done, every `Deps` cell in this base is a claim about a version nobody identified."*

### 🟢 The Python side — the claim is exact, and the `32` is finally identified

The `32` is the **`base` dependency group in `pyproject.toml`**, not `requirements.txt`. 🔴 **`requirements.txt` is a decoy and says so in its own first line** — *"Bundled runtime dependencies are resolved from the `base` dependency group in `pyproject.toml`… This file exists only as the sink for any EXTRA_REQUIREMENTS injected at build time."* An audit that read it would have found `0` dependencies and reported a confidently clean result.

🟢 **Every entry in `base` is `==`-pinned, so the manifest IS the resolution.** Resolved against PyPI at each pin — `32` packages, `2` LGPL, exactly as published:

| Package | Pin | `license` field | Classifier | Trigger |
|---|---|---|---|---|
| 🔴 `zeroconf-py2compat` | `0.19.17` | `LGPL` | GNU Lesser GPL v2 | 🟡 Distribution |
| 🔴 `json-schema-validator` | `2.4.1` | 🔴 **EMPTY** | GNU Library or Lesser GPL | 🟡 Distribution |

🔵 **The second row is `p791-G` running in the opposite direction**: the `license` field is empty and only the classifier carries the copyleft, so a field-reading audit would have *under*-reported it. A blank field is not a verdict either way.

The other `30` are permissive: `18` BSD-family (`django==3.2.25`, `djangorestframework==3.14.0`, `Click==8.0.4`, `cheroot`, `magicbus`, `configobj`, `idna`, `semver`, `django-{csp,filter,redis-cache,sortedm2m}`, …), `9` MIT (`morango`, `le-utils`, `pytz==2026.3.post1`, `redis`, `whitenoise`, `tzlocal`, `html5lib`, `jsonfield`, `django-mptt`, `ifaddr`, `colorlog`, `django-js-reverse`), `3` Apache-2.0 (`requests==2.27.1`, `diskcache`, `importlib-metadata`/`importlib_resources`), `1` dual Apache/BSD (`python-dateutil`). Machine output: [`evidence/kolibri-pypi-pinned-resolved.2026-11-12-p793.tsv`](../evidence/kolibri-pypi-pinned-resolved.2026-11-12-p793.tsv).

### 🔴 The npm side — `208` runtime packages, never measured before, and the root manifest explains why

🔴 **`kolibri`'s root `package.json` declares `0` runtime `dependencies`.** It is a **pnpm workspace with `40` importers**, so any audit that read the root manifest measured nothing at all and would have seen a clean, empty result.

Collecting `dependencies` + `optionalDependencies` across all `40` importers and resolving **each at its locked version** against the registry gives **`208`** distinct runtime packages:

| Grant, resolved at the pinned version | Count |
|---|---|
| 🟢 MIT | `175` |
| 🟢 Apache-2.0 | `10` |
| 🟢 BSD-2 / BSD-3 | `9` |
| 🟢 ISC | `5` |
| 🟢 MIT-0 · CC0-1.0 · Unlicense · WTFPL · BlueOak-1.0.0 | `5` |
| 🟡 **MPL-2.0** | **`1`** — `mathquill@0.10.1` (bytes confirmed, `16,725 B`) |
| 🟡 **`(MPL-2.0 OR Apache-2.0)`** | **`1`** — `dompurify@3.4.17` → 🟢 **elect Apache-2.0** |
| 🔴 **No grant on any channel** | **`1`** — `@khanacademy/mathjax-renderer@3.0.2` |
| 🟢 **GPL · LGPL · AGPL** | 🟢 **`0`** |

🟢 **Zero GPL-family packages in the JavaScript that reaches a learner's browser.** This file's central claim — that `kolibri` is the permissive platform Globant can link into client code — is **stronger** after measurement than the row claimed.

### 🔴 Where the residual risk actually is: one plugin, named

| Package | Grant | Declared by |
|---|---|---|
| 🟡 `mathquill@0.10.1` | MPL-2.0 — file-level copyleft; 🟢 fine if unmodified, carry the notice | `kolibri/plugins/perseus_viewer` → `dependencies` |
| 🔴 `@khanacademy/mathjax-renderer@3.0.2` | 🔴 **None.** Tarball (`336,573 B`) has no `LICENSE`/`NOTICE`/`COPYING` at any path; registry `license` absent; upstream `Khan/mathjax-renderer` **`rc=128`, address does not resolve** | `kolibri/plugins/perseus_viewer` → `dependencies` |
| 🟢 `dompurify@3.4.17` | Dual → elect Apache-2.0 | `packages/kolibri-common` (core) |

🔵 **The actionable shape for an engagement:** `kolibri` core is clean; the exercise renderer is where the two questions live. A deployment that does not need Perseus exercises avoids both. A deployment that does needs one licence request (`mathjax-renderer`) and one notice obligation (`mathquill`). 🟢 **That is a `2`-item licensing checklist on a platform this base had been describing with a single ambiguous cell.**

🟢 **Standing instruction for every `Deps` cell in this base, now proven on a second row:** resolve the **lockfile or the pin**, never the manifest and never `latest`; and when a registry field is blank, read the **tarball**, because the tarball *is* the version. See `T895`, `T896`.

## 🆕 `p792` — **This base's standing "DO NOT ship `oppia`" verdict is REFUTED on the lockfile. The AGPL-3.0 it warns about is real, and `oppia` does not use it.**

🟢 **Control before any verdict:** `HKUDS/DeepTutor` `LICENSE` reproduced at **`11,408 B`**, `moodle/moodle` `COPYING.txt` at **`35,147 B`**, `oppia/oppia` `LICENSE` at **`11,358 B`** — all three match the bytes this base already records. 🔴 **`5` defects in this pass's own instruments were caught by controls before any verdict shipped** — see `intel/trends.md` `T884`–`T886` and the defect list at the foot of `agents/trending.md`.

### 🔴 `T884` — the row this file has published for four passes, measured on the lockfile

🔴 **What this file said, carried since `p787`:** `oppia/oppia` · `🔴 1 AGPL-3.0 of 171` · *"**DO NOT ship as-is: `angular-shepherd` is AGPL-3.0, and a browser bundle is network delivery.** Remove or replace it first."*

🟢 **The `171` is exactly right** — `83` `dependencies` + `88` `devDependencies` in `package.json`, distinct count `171`. 🟢 **`angular-shepherd` is genuinely declared**, at `package.json` line `179`, in `dependencies` (not `devDependencies`), so it does reach the browser bundle. 🔴 **And the licence verdict is still wrong**, because it was read off the package rather than off the version:

| Measured | Value | Channel |
|---|---|---|
| `angular-shepherd` declared range | `^11.0.0` · in `dependencies` | `package.json` byte channel |
| 🟢 **`yarn.lock` RESOLVES it to** | 🟢 **`11.0.0`** — integrity `sha512-Ig0OU6vE0JAbyWFTH+qgmTgPKUxLmUXMCJde6XFBAg2gc624fvcJ5s6GapM/lUaFaDjtLkGJuAkb9pI0dUo8rQ==` | `yarn.lock` byte channel |
| 🟢 **Licence of `angular-shepherd@11.0.0`** | 🟢 **MIT** | npm registry |
| 🔴 Licence of `angular-shepherd@latest` (`22.0.0`) | 🔴 **AGPL-3.0** | npm registry |
| 🟢 **Where the relicence happened** | 🟢 **MIT from `v0.0.1`; AGPL-3.0 from `v22.0.0`** — one transition, full version history swept | npm registry |
| `shepherd.js` declared / resolved | `^8.0.1` → 🟢 **`8.3.1`**, MIT (`latest` `16.0.0` is AGPL-3.0) | `yarn.lock` + npm |

🟢 **So `oppia` ships MIT versions of both Shepherd packages, and its caret ranges cannot reach the AGPL ones.** `^11.0.0` admits `>=11.0.0 <12.0.0`; the AGPL-3.0 begins at `22.0.0`. `^8.0.1` admits `>=8.0.1 <9.0.0`; `shepherd.js`'s AGPL-3.0 begins at `16.0.0`. **No resolution inside either range is AGPL-3.0.**

🟢 **The verdict therefore flips, and the rule flips with it.**

| Then | Now |
|---|---|
| 🔴 *Do not ship `oppia` as-is; remove or replace `angular-shepherd` first* | 🟢 **Ship `oppia`. Pin Shepherd and gate the major bump.** The exposure is an **upgrade** risk, not a present one |

🔵 **Why this matters beyond one row.** `oppia/oppia` is the interactive-lessons platform this base recommends most often, and the warning was strong enough to steer an engagement away from it. 🔴 **It was wrong in the direction that costs the most** — it removed a usable, Apache-2.0, `7.0k★` option on the strength of a licence field read at `latest`. 🟢 **`T884`'s general form: a licence is a property of a VERSION, not of a package.** A dependency audit that does not resolve the lockfile is reading a licence the project does not use.

### 🟢 And the Python layer has a strong-copyleft direct dependency nobody had recorded

🔵 `oppia` carries two independent dependency layers and this base had audited neither to its lockfile. The Python one is a real `pip-compile` lockfile — `requirements.txt`, `2,504` lines, `--generate-hashes`, **`152` distinct pinned packages** — and all `152` resolved against PyPI with **`0` unresolved**.

| Package | Licence | Direct or transitive |
|---|---|---|
| 🔴 **`mutagen==1.47.0`** | 🔴 **GPL-2.0-or-later** | 🔴 **DIRECT** — `# via -r requirements.in`, named at `requirements.in` line `25` |
| 🟡 `certifi` | MPL-2.0 (file-level weak copyleft) | transitive — via `httpcore`, `httpx`, `requests` |
| 🟡 `orjson` | `MPL-2.0 AND (Apache-2.0 OR MIT)` | transitive |

🔴 **`mutagen` is strong copyleft and it is a declared direct dependency** of a platform this file lists as permissive — and this base had never named it. 🟢 **But it is GPL-2.0, not AGPL-3.0, and the difference is the whole point:** GPL-2.0's copyleft is **distribution-triggered**, and AGPL-3.0's adds a **network-service** trigger. 🟢 **For the normal education deployment — a hosted platform the institution runs — GPL-2.0 does not reach the client's own code.** Had the AGPL claim been true, it would have.

🟡 **Deliverable rule for `oppia`, replacing the old one:** pin `angular-shepherd` and `shepherd.js` and gate their major bumps in CI; and if the Python service is **distributed** rather than hosted, either replace `mutagen` or carry GPL-2.0 at that boundary. `requirements.in` has only **`29`** direct entries, so the substitution is a small, bounded piece of work.

🔵 **`oppia`'s own tree is single-family.** `23` paths match the licence gate; `21` are Angular source files and screenshots for Oppia's in-product *licence page* (`license-page.component.ts` and friends), not grants. The actual grants are `LICENSE` (Apache-2.0, `11,358 B`) and `NOTICE`. 🔴 **A path-name gate over-reports — see `T886`.**

### 🟢 `p791-D` discharged — `Miaotofu01/Study-Mate` cleared beyond the first layer, with one addition

| Path in tree | Bytes | Grant |
|---|---|---|
| `LICENSE` | `1,064 B` | 🟢 MIT |
| `lib/katex/LICENSE` | `1,107 B` | 🟢 MIT (KaTeX — already recorded at `p791`) |
| 🆕 `lib/katex/fonts/LICENSE` | `4,616 B` | 🟡 **SIL Open Font License** — **not read at `p791`** |
| `lib/watch/notice.ts` | `3,871 B` | — a TypeScript source file, not a grant (gate false positive) |

🟢 **`363` files enumerated; `Study-Mate` is `TREE[MIT + MIT + OFL]` and it is usable.** 🔴 **And for the second consecutive pass, the grant the first layer missed was a FONT grant** (`p791`: OpenMAIC's `ZcoolHappy`; `p792`: KaTeX's OFL). 🟢 **Deliverable rule: carry the OFL file and keep the font names intact.** 🔵 KaTeX turned up in **three** separate repositories this pass — it is the sector's most-vendored maths renderer, and its font grant travels with it every time.


## 🆕 `p791` — the permissive layer gains a real SIS/ERP, and a carried foundation row loses its grant text

🟢 **The carried sentence at the top of this file is amended for the first time in four passes, and only slightly.** The famous education platforms are still copyleft — Moodle, Open edX, Canvas, Chamilo, ILIAS, Frappe LMS and ERPNext are GPL or AGPL, and `p790` added `nextSIS` (GPL-3.0) to that list rather than to the permissive one. 🟢 **`p791` adds the first genuinely MIT Student-Information/ERP system this base has verified on the bytes.**

| Repository | Grant, on the bytes | ★ | What it is, and why it matters here |
|---|---|---|---|
| 🆕 [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | 🟢 **MIT** · `1,150 B` · `f86101816893` | `56` | 🟢 **A K-12 school ERP under a real MIT grant — the narrow permissive layer finally has an SIS-shaped member.** Laravel/PHP + Vue, `7,623` files: students, attendance, timetables, fees, and role-scoped portals for admin, teacher, student, parent, accountant and reception. 🟢 **First-layer dependency audit clean:** the one vendored package, `custompackages/brozot/laravel-fcm`, is **MIT** (`1,080 B`); the `15` `*.js.LICENSE.txt` files are webpack-extracted banners, not additional grants. 🔴 **`★56` — this is a small project.** Its value is that it is *embeddable*: AI code can live directly inside it, which is true of almost nothing else in this column |
| ✏️ [`frappe/education`](https://github.com/frappe/education) | 🔴 **`19 B` — `License: GNU GPL V3` and nothing else** · `beca17940a71` | `706` | ✏️ **Carried row, corrected, and it is the sharper half of `T880`.** Its entire licence file is a **family reference with no operative grant text**. Its own siblings in the same org serve the real thing: [`frappe/lms`](https://github.com/frappe/lms) `33,893 B`, [`frappe/erpnext`](https://github.com/frappe/erpnext) `35,149 B`. 🟡 **Treat as intent-to-GPL-3.0:** plan copyleft at the boundary, do not embed, and get the grant confirmed before a derivative ships. 🔵 Almost certainly an upstream oversight — the fix is an issue filed, not an avoidance |

🔵 **Why `Gego-K12/gegok12` is worth a small row.** This file's standing problem is that every platform a client already runs is copyleft, which pushes all AI work to a process or API boundary (`compose/patterns.md`, Rule 1). A permissive SIS changes the available shapes: it is the one place in this sector where an agent can be written **as a module inside the system of record** without a copyleft obligation reaching the client's own code. 🔴 **At `★56` it is not a safe bet for a large deployment** — but for a greenfield K-12 build, or as the reference for how an SIS schema is shaped, it is the only permissive option this base has found.


# Foundational education repositories — `p790`

**The single most useful fact in this file, carried:** in education, *the famous platforms are
copyleft and the permissive layer is narrow and specific.* Moodle, Open edX, Canvas, Chamilo,
ILIAS, Frappe LMS and ERPNext — the names a client will say out loud — are **GPL or AGPL**.

🟢 **`p790` adds one name to that list, and takes it off a different one.** [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS)
— a named **Student Information System** — was published by this base for two passes as
**`PROPRIETARY`**. It is **`GPL-3.0`**. Its `39,890 B` `license.txt` is a licence **anthology**
(§2 nextSIS's own full operative GPL-3.0, §3 **CodeIgniter**/EllisLab, §4 **Twitter Bootstrap**), and
the single `All rights reserved.` this base graded on sits at line `703`, inside EllisLab's section,
two lines above EllisLab's own grant of permission. 🟢 **The carried sentence therefore holds more
strongly, not less: the open SIS is copyleft too.** 🔴 And the correction is a method change —
**a licence file that quotes other licences cannot be graded by substring presence** (`T875`). Read
the tree, never a filename list:

```bash
git clone --filter=blob:none --no-checkout --depth 1 https://github.com/OWNER/REPO /tmp/x
git -C /tmp/x ls-tree -r --name-only HEAD | grep -iE 'licen|copying|legal|terms|notice'
```

🟢 **`221` files enumerated, one match (`license.txt`, lowercase), no blobs downloaded.** `raw` is
case-sensitive, so a candidate-filename probe produces **false absences** — which is what both
`p789` and this pass's first instrument produced on this very row.

🔴 **The single most useful fact ADDED this pass (`T861`):** a permissive repository grant tells you
nothing about its dependencies, and **4 of the 7 highest-star permissive education repos carry
copyleft in their declared direct dependencies.** The `Deps` column below records the first-layer
audit where one was run. **A blank `Deps` cell means not audited, not clean.**

Every grant below was read this pass from the served `LICENSE` bytes by clause presence, with the
title found by scanning for a line that *is* a licence title at any depth (`T863`). `sha` is the
12-char `HEAD` from `git ls-remote`.

## 🟢 Permissive — build on these, link them, ship them in client code

| Repo | Address | Grant, on the bytes | Deps | Region | Role |
|---|---|---|---|---|---|
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** · `1,097 B` · `fe298f54494c` | 🟢 **`2` LGPL of `32` Python pins — CONFIRMED exactly at `p793`; plus `208` npm runtime packages resolved for the first time: `0` GPL-family, `1` MPL-2.0, 🔴 `1` ungranted — all risk inside `perseus_viewer`** | Global | 🟢 **Still the most valuable permissive row in education.** Offline-first learning platform: curated openly-licensed content library, teacher tools, sync, runs on low-cost and legacy hardware, downloads once then works with no connectivity. `1,176★`, reported in use across 195 countries. ⚠️ **`zeroconf-py2compat` (LGPL-2) and `json-schema-validator` (LGPL)** — dynamic linking is permitted, so usable; the components must stay replaceable with source available |
| **Oppia** | [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** · `11,358 B` · `bbda308fd5db` | 🔴 **1 AGPL-3.0 of 171** | Global | Interactive lessons that behave like a one-to-one tutoring conversation. `7.0k★`. 🔴 **DO NOT ship as-is: `angular-shepherd` is AGPL-3.0, and a browser bundle is network delivery.** Remove or replace it first |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** · `11,120 B` · `593c74e1c7a5` | — | North America | Full higher-ed LMS under the **Educational Community Licence 2.0 — an Apache-2.0 derivative**, so permissive. The only mature, permissively-granted university LMS in this base |
| **OpenOLAT** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** · `10,982 B` · `322e90dd5507` | — | EMEA | Swiss-origin university LMS. ⚠️ `375 B` short of the canonical Apache text — clause-verified genuine, the deviation is in the trailing appendix. **The permissive LMS for an EMEA engagement.** 🔴 **`p796` (`T914`): `NOTICE.TXT` (`14,412 B`) puts the OpenOlat logo and icons under `CC BY-ND 2.5` — `NoDerivs`. The CODE is Apache-2.0; the BRAND assets must be REPLACED, not modified, in a white-labelled delivery** |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | **ECL-2.0** · `11,340 B` · `94aecba33ed9` | — | EMEA | Lecture capture, processing and distribution at university scale; permissive |
| **Tsugi** | [`csev/tsugi`](https://github.com/csev/tsugi) | **Apache-2.0** · `10,273 B` · `f54555227df1` | — | Global | 🟢 **The licence-firewall component.** Hosts **LTI** tools that plug into Moodle/Canvas/Sakai *across a process boundary*, so permissive or proprietary code can serve a copyleft LMS without linking to it. Canonical owner is `csev`; `tsugi/tsugi` is DEAD |
| **Perseus** | [`Khan/perseus`](https://github.com/Khan/perseus) | **MIT** · `1,052 B` · `e722e959afd0` | — | North America | Khan Academy's exercise and question rendering engine — the content primitive for interactive assessment |
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** · `1,105 B` · `fae8cc474484` | 🟢 **0 of 43** | North America | UC Berkeley adaptive tutoring with Bayesian Knowledge Tracing. `279★`. 🟢 **The cleanest dependency tree measured this pass** |
| **nbgrader** | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | **BSD-3-Clause** · `1,512 B` · `91d5c12f989b` | 🟢 **0 of 18** | Global | 🟢 Assignment release, collection, **autograding** and feedback for notebooks. **The most defensible autograding core available permissively — and it audits clean to the first layer**, which is why `P788-1` rests on it |
| **JupyterHub** | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | **BSD-3-Clause** · `1,475 B` · `41fffb935326` | — | Global | Multi-user notebook serving — the cohort-scale delivery layer under `nbgrader` |
| **Jupyter Notebook** | [`jupyter/notebook`](https://github.com/jupyter/notebook) | **BSD-3-Clause** · `1,588 B` · `5662506ad194` | — | Global | The notebook surface itself |
| **DSpace** | [`DSpace/DSpace`](https://github.com/DSpace/DSpace) | **BSD-3-Clause** · `1,504 B` · `2d991b4832bb` | — | Global | Institutional repository for theses, OER and research output |
| **Open WebUI** ✏️ | [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | 🔴 **`BSD-3-Clause + BRANDING RIDER` (non-OSI)** · `2,819 B` · 🟢 `99f39e7feff2` | — | Global | 🔴 **CORRECTED at `p794` (`T900`) — was published here as plain BSD-3-Clause.** Clause `4` bars altering, removing or replacing *"Open WebUI" branding*; alteration is a **material breach**. 🔴 **So it cannot be white-labelled for a client**, which is the whole point of a delivery surface. 🔵 Ship it unbranded, or use it only where the Open WebUI name may remain visible. `★158,480` |
| **LangGraph** | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** · `1,072 B` · `b4cb0f19e3d8` | — | Global | Stateful agent graphs — the orchestration layer in most recipes here |
| **smolagents** | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | **Apache-2.0** · `11,357 B` · `96f33faaf028` | — | Global | Minimal agent runtime where LangGraph is more than the engagement needs |
| **xAPI service** `NEW` | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | **MIT** · `1,070 B` · `685c342129c5` | — | Global | 🟢 **Rescued from this base's ungranted class.** An xAPI **Learning Record Store** service under MIT. This base called its Caliper/QTI/xAPI cluster "its most dead cluster"; the live, permissive half was filed as an absence. **This is the component an audit-trail claim actually needs** |
| **xAPI validation** `NEW` | [`LearningLocker/xapi-validation`](https://github.com/LearningLocker/xapi-validation) | **MIT** · `1,070 B` · `13ffff748515` | — | Global | xAPI statement validation — rescued alongside the above |
| **eagle-aig** `NEW` | [`LIST-LUXEMBOURG/eagle-aig`](https://github.com/LIST-LUXEMBOURG/eagle-aig) | **Apache-2.0** · `11,358 B` · `99cecb066ecf` | — | EMEA | 🟢 **Luxembourg Institute of Science and Technology** — a national public research institute, permissively granted. Rescued from the ungranted class |
| **brightspace-d2l-mcp** `NEW` | [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | **MIT** · `1,200 B` · `a873478a6b4e` | — | North America | 🟢 MCP server over **D2L Brightspace** — the third major North American LMS, and the first attachment point this base has for it |
| **ODK Collect** `NEW` | [`getodk/collect`](https://github.com/getodk/collect) | **Apache-2.0** · `10,494 B` · `2344bb9c5da4` | — | Global | Offline mobile data collection — the field instrument for a readiness diagnostic where connectivity fails |
| **elimu-ai** (7 repos) `NEW` | [`elimu-ai/webapp`](https://github.com/elimu-ai/webapp) · [`appstore`](https://github.com/elimu-ai/appstore) · [`launcher`](https://github.com/elimu-ai/launcher) · [`model`](https://github.com/elimu-ai/model) · [`ml-authentication`](https://github.com/elimu-ai/ml-authentication) · [`ml-storybook-reading-level`](https://github.com/elimu-ai/ml-storybook-reading-level) · [`ml-storybook-recommender`](https://github.com/elimu-ai/ml-storybook-recommender) | **MIT** · `1,065 B` each · shas in `agents/top.md` | — | EMEA | 🟢 **A 66-repository MIT African education ecosystem, pushed this week** — Android delivery without an app store, a shared data model, and **ML models for storybook reading level and recommendation**. 🔵 This base was already citing `elimu-ai` and had never placed it |
| **rrule** | [`jkbrzt/rrule`](https://github.com/jkbrzt/rrule) | **BSD-3-Clause** · `3,493 B` · `9f2061febeeb` | 🔴 **STALE — last push `2024-06-27` (`28` mo), ★`3,752`, NOT archived** (`p795`) | Global | Recurrence rules — the scheduling primitive under timetabling and spaced review. 🔵 Grant served at `LICENCE`, the **British spelling**, which a US-spelling-only probe misses. 🔴 **`p796` (`T915`): the file carries TWO BSD-3-Clause grants — its own and bundled `python-dateutil`'s (Niemeyer / Pieviläinen), because `rrule.js` is a port. Shipping it carries both sets of notices, and GitHub abstains (`NOASSERTION`) for exactly that reason** |
| **annotated DL implementations** `NEW` | [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | **MIT** · `1,082 B` · `db59a04a8a2c` | — | Global | Annotated paper implementations — a teaching corpus under a permissive grant. Rescued from the ungranted class |
| **MyScriptJS** 🔴 **ARCHIVED** | [`MyScript/MyScriptJS`](https://github.com/MyScript/MyScriptJS) | **Apache-2.0 (by reference)** · `570 B` · `968021fcc1f4` | — | EMEA | 🔴 **ARCHIVED UPSTREAM — read-only, last push `2021-01-04`, nearly six years stale (`T901`).** `★357`. Handwriting and maths-input recognition (French origin). 🟡 **`p786` rescued the GRANT and no pass checked MAINTENANCE — a licence rescue is not a viability rescue.** It is the standard Apache-2.0 grant-by-reference boilerplate, URL and AS-IS clause included. 🔴 **It was dismissed for being short — the exact error `T845` forbids** |

## 🟢 Permissive rows added this pass (`p789`)

| Repo | Address | Grant, on the bytes | Region | Why it is foundational |
|---|---|---|---|---|
| 🟢 **Timable** `NEW` | [`Nayak-indie/Timable`](https://github.com/Nayak-indie/Timable) | 🟢 Apache-2.0 · `11,357 B` · `c71d239df917` | Global | **OR-Tools** timetabling — a real constraint solver under a permissive grant. The scheduling primitive this base had no row for |
| 🟢 **school-timetable-timefold-case-study** `NEW` | [`paoloantinori/school-timetable-timefold-case-study`](https://github.com/paoloantinori/school-timetable-timefold-case-study) | 🟢 MIT · `1,081 B` · `12e2a597e655` | Global | **Timefold** solver on Quarkus, driven by coding agents — the reference wiring for `P789-1` |
| 🟢 **jp-k12-digital-ai-textbook** `NEW` | [`masa-san-jp/jp-k12-digital-ai-textbook`](https://github.com/masa-san-jp/jp-k12-digital-ai-textbook) | 🟢 MIT · `1,068 B` · `d7c583c9f444` | APAC 🇯🇵 | A `12`-grade curriculum tree aligned to the **next 学習指導要領** and the **UNESCO AI Competency Framework** — content infrastructure, not an app |
| 🟢 **classcharts-agent** `NEW` | [`shan8851/classcharts-agent`](https://github.com/shan8851/classcharts-agent) | 🟢 MIT · `1,066 B` · `65ef4f07f833` | EMEA 🇬🇧 | A **read-only** attachment to a live UK school MIS — this base's second EMEA LMS/MIS attachment point |

## 🟢 BSL-1.0 (Boost) — a licence family new to this base (`p789`)

| Repo | Address | Grant, on the bytes | Region | Note |
|---|---|---|---|---|
| 🟢 **nextgen-learn** `NEW` | [`daddysystem/nextgen-learn`](https://github.com/daddysystem/nextgen-learn) | 🟢 **BSL-1.0 · `1,338 B` · `c9bff7573892`** | EMEA 🇿🇦 | Free **CAPS**-curriculum study site with an AI tutor |

🟢 **Boost-1.0 is permissive, OSI-approved, and in one respect *weaker* than MIT:** it waives the
attribution requirement for distribution in object-code-only form. Nothing in it restricts
commercial use, linking or relicensing of derivatives.
🔴 **It is also the pass's sixth instrument defect, and the reason it is called out here:**
**BSL-1.0 opens with MIT's exact sentence** — *"Permission is hereby granted, free of charge, to
any person or organization obtaining a copy"*. A phrase-matching probe grades it MIT. Only the
title separates them. 🔵 `BSL-1.0` must not be confused with the **Business Source License
(BUSL-1.1)**, which is *not* open source; the SPDX id `BSL-1.0` is Boost.

## 🔴 `T872` — The second dependency layer, and a first-layer audit is a screen not a clearance

🟢 **`ACTION p788-D` discharged, bounded, with the boundary stated first: layer 2 only.**
`jupyter/nbgrader` → **`18`** declared direct runtime dependencies (🟢 the exact count `p788`
recorded — a control on this channel) → **`65`** new transitive packages at layer 2.
Each grant read **PEP 639 `license_expression` first**, then classifiers, then the free-text field,
because `p788` recorded PEP 639 blindness as a defect; **`28` of the `65` are decided by
`license_expression`** and a classifier-only instrument would read them `UNDECLARED`.

| Package | Grant | Enters through | Effect |
|---|---|---|---|
| 🔴 **`certifi`** | **MPL-2.0** | 🔴 `requests` → `certifi` | 🟡 **File-level copyleft.** Triggers on modifying `certifi`'s own files; linking and redistribution are clean. Nobody modifies a CA bundle — **but the graph is no longer "no copyleft"** |
| 🔴 **`paramiko`** | **LGPL-2.1** (PEP 639) | 🔴 `jupyter-client` → `paramiko` | 🟡 **Weak copyleft, dynamic linking permitted.** 🔴 It arrives via `jupyter-client`, a *core* runtime dependency of every Jupyter-based grading stack — not an optional extra |
| 🟡 `pytest-ruff` | **UNDECLARED** | `setuptools` → `pytest-ruff` | 🔵 Build/test-time only. Recorded because an undeclared grant is a fact, not an omission |

🟢 **The other `62` are permissive** — MIT, BSD-2/3-Clause, Apache-2.0, ISC, PSF-2.0 — including
three SPDX **compound** expressions that are mis-read in opposite directions: `packaging` is
`Apache-2.0 OR BSD-2-Clause` (**an election**, both permissive), `prometheus-client` is
`Apache-2.0 AND BSD-2-Clause` (**cumulative — both apply**), and `jupyter-builder` is
`Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT`.

🟢 **Verdict for `P788-1`, which rests on `nbgrader`: it still holds, and its licensing claim is now
weaker and true.** What changes is the sentence a client is told — not *"the grading component's
dependencies are entirely permissive"*, which was true only of layer 1, but *"its graph includes
MPL-2.0 and LGPL-2.1 at layer 2, both weak copyleft, neither triggered by the way we deploy it."*

## 🔴 Copyleft — real, dominant, and a licensing decision before a line is written

| Repo | Address | Grant, on the bytes | Region | What the grant costs you |
|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** · `35,147 B` · `afbcc55fa1bd` | Global | The sector's default LMS. 🔴 Plugins are derivative works — a Moodle plugin must ship GPL-3.0. Keep proprietary logic behind LTI (`Tsugi`) or a web API |
| **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** · `35,136 B` · `d3a86602dcf7` | Global | 🔴 **AGPL: serving it over a network triggers source disclosure.** Community release line *Verawood* (June 2026, 22nd release) |
| **Tutor** | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** · `34,523 B` · `bca91d56136f` | Global | The standard Open edX Docker distribution. Canonical owner is `overhangio`; `openedx/tutor` is DEAD |
| **Open Response Assessment** | [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 **AGPL-3.0** · `35,135 B` · `0d60a779e29d` | Global | Peer/self/staff assessment for Open edX. Correct address is `edx-ora2`; `openedx/openassessment` is DEAD |
| **Canvas LMS** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** · `34,520 B` · `1c9f0bb8013e` | North America | Clause-verified AGPL-3.0, settling a search-channel conflict that also claimed ECL-2.0. The dominant North American higher-ed LMS |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0** · `35,147 B` · `e137bded10b5` | EMEA | Belgian/Spanish-origin LMS with the strongest Spanish-language footprint — heavily deployed across LATAM |
| **ILIAS** | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL-3.0** · `35,147 B` · `87a79b237fcc` | EMEA | German university LMS, strong in DACH public institutions |
| **Frappe LMS** | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** · `33,893 B` · `45edbff87486` | APAC | Indian-origin modern LMS on the Frappe stack |
| **Frappe Education** `NEW` | [`frappe/education`](https://github.com/frappe/education) | 🔴 **GPL-3.0** · **`19 B`** · `61408d3da518` | APAC | Frappe's school-management module. 🔵 **The shortest grant in this base, and it is a real one:** the entire `license.txt` reads `License: GNU GPL V3`. 🔴 A probe matching only expanded licence names scores it `UNGRADED` (`T863`) |
| **ERPNext** | [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **GPL-3.0** · `34,916 B` · `447313109fdd` | APAC | ERP backbone used for school finance/HR |
| **H5P core** | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** · `35,146 B` · `2d7f937a03c9` | EMEA | Norwegian-origin interactive content types, embedded in Moodle and Canvas |
| **Gibbon** | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **GPL-3.0** · `35,121 B` · `59334a28613f` | Global | School management joined to teaching tools in one system |
| **RosarioSIS** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** · `15,214 B` · `e4cd20a48bf1` | Global | Student Information System with strong Spanish and French localisation — the SIS that fits LATAM deployments |
| **Mahara** 🔴 **ARCHIVED** | [`MaharaProject/mahara`](https://github.com/MaharaProject/mahara) | 🔴 **GPL-3.0** · `35,148 B` | Global | 🔴 **ARCHIVED UPSTREAM — read-only, last push `2023-11-16` (`T901`).** ePortfolio, `★120`. 🔵 Canonical owner is `MaharaProject` (`mahara/mahara` is DEAD) — 🔴 **but resolving canonicity is not resolving maintenance.** Do not start an ePortfolio engagement here without owning the fork |
| **Anki** | [`ankitects/anki`](https://github.com/ankitects/anki) | 🔴 **AGPL-3.0** · `1,930 B` · `a5461e33e3db` | Global | Spaced repetition; the reference implementation of the scheduling model tutors copy |
| **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL** · `7,652 B` · `13b55d45c046` | Global | Virtual classroom built for teaching rather than meetings. LGPL is weaker than GPL — dynamic linking is permitted |
| **Odoo** | [`odoo/odoo`](https://github.com/odoo/odoo) | 🔴 **LGPL-3.0** · `43,529 B` · `3ce3a7dc8ecb` | Global | The ERP base under OpenEduCat. ⚠️ `T847`: states LGPL-3.0 on line 3 behind a deferral. 🔵 `HEAD` moved from `75447d905934` since `p787` |
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL** · `8,241 B` · `46a5d7d40082` | Global | Odoo-based education ERP — SIS + LMS + finance in one. Same line-3 deferral pattern as Odoo |
| **INGInious** `NEW` | [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** · `34,764 B` · `98d56ade0351` | EMEA | Automated-grading platform (UCLouvain, BE) — **directly in the regulated assessment surface**. ⚠️ **Also SCOPE-LIMITED:** its licence states *"most of the files … if it is not the case, this is clearly indicated in the files"*, so a per-file audit is required before any reuse |
| **OpenTreeMap otm-core** `NEW` | [`OpenTreeMap/otm-core`](https://github.com/OpenTreeMap/otm-core) | 🔴 **AGPL-3.0** · `35,366 B` · `b26aec8c9e7c` | North America | Newly graded out of the bespoke bucket; prose preamble before the title line |

## 🟡 EUPL — OSI-approved, copyleft, and the reason a prior pass fixed its probe

| Repo | Address | Grant, on the bytes | Region | Note |
|---|---|---|---|---|
| **Hedy** | [`hedyorg/hedy`](https://github.com/hedyorg/hedy) | 🟡 **EUPL-1.2** · `13,827 B` · `38d5db7214ff` | EMEA | Gradual programming language for classrooms; `1,697★`. A long-standing EMEA education anchor |
| **OOAPI specification** | [`open-education-api/specification`](https://github.com/open-education-api/specification) | 🟡 **EUPL-1.2** · `13,827 B` · `d9c5b0a1a68d` | EMEA | Open Education API — a **live** interop standard |
| **European Learning Model** 🟡 **ARCHIVED** | [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) | 🟡 **EUPL-1.2** · `13,865 B` | EMEA | 🟡 **ARCHIVED UPSTREAM — last push `2024-02-14` (`T901`).** `★54`. 🔵 Milder than the other two: a published vocabulary may legitimately freeze — but say so to the client. 🟢 The **European Commission's own** learning/credential data model. Re-verified out of the ungranted class. 🔵 `13,865 B` against Hedy's `13,827 B` — **two EUPL-1.2 texts differing by `38 B`**, which is why length is never a verdict |

🔵 **`T849`, carried:** EUPL-1.2 **names GPL-2.0, GPL-3.0, AGPL, EPL and CeCILL inside its
compatibility appendix**, so a licence that *lists other licences* must be matched **before** any
family check. Verified again this pass: all copyleft controls still reproduce.

## 🔴 Not open source — measured this pass, reason on the bytes

| Address | Grant, on the bytes | Why it is barred |
|---|---|---|
| [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) ✏️ | 🟢 **GPL-3.0** · `39,890 B` · 🟢 `01fa8c8c4c6e` | ✏️ **`p794` removes the stale `PROPRIETARY` text that survived `p790`'s correction in this file.** A named Student Information System, 🔵 Previously filed merely "ungranted". **A `39,890 B` licence is a long licence, not an open one** |
| [`metabase/metabase`](https://github.com/metabase/metabase) | 🔴 **SPLIT BY DIRECTORY *AND* BY FILE** · `4` root licence files | AGPL-3.0 (`LICENSE.txt`, `37,265 B`) outside `enterprise/`; **Metabase Commercial License** (`LICENSE-MCL.txt`, `425 B`) inside it; 🔴 **and `LICENSE-EMBEDDING.txt` (`8,877 B`) carves the single file `app-embed.js` out of AGPL into a proprietary EULA whose `§3` forbids *"the removal of the Metabase's name or logo in the iframe that is embedded in your application"* (`T912`, `p795`).** 🔴 **So the white-labelled embed this file used to recommend is the prohibited act.** 🟢 **Deployable form: run metabase as its own AGPL-3.0 app and link to it; do not embed `app-embed.js` in a client-branded surface** |
| [`Tzxser/aipha-learning-os`](https://github.com/Tzxser/aipha-learning-os) | 🔴 **PROPRIETARY** · `1,296 B` · `aa476a6a6a03` | Source-available multi-agent learning OS; now graded rather than `UNGRADED` |
| [`luscitiosus/Dirigo`](https://github.com/luscitiosus/Dirigo) | 🔴 **CC BY-NC-SA 4.0 (Spanish), SCOPE-LIMITED** · `362 B` · `9ed32d5c2577` | Spanish school-leadership regulation. 🔴 **This base's published reason was wrong** — see `T863`. NonCommercial bars a commercial deliverable, and the BOE/BOC statutory texts are excluded from the grant entirely |
| [`TarrySingh/…-Machine-Learning-Tutorials`](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials) | 🔴 **CC-NonCommercial** · `20,850 B` · `bac3481e8d78` | `4,025★`. NonCommercial cannot be cured by asking. 🔵 `HEAD` moved from `e66c269d4819` since `p786` |
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) · [`1edtech/caliper-spec`](https://github.com/1edtech/caliper-spec) | 🔵 `UNGRADED` **+ CONSEQUENCE** · `8,563 B` · `e1de68833d1c` / `12,402 B` · `1849e118b47a` | Bespoke *PageLM Community License* and 1EdTech consortium terms. 🟢 **`UNGRADED` remains the correct verdict as to FAMILY** — forcing either into an OSI family is the error `T845`–`T849` keep catching. 🔴 **But `UNGRADED` was silent on consequence, and `T909`/`p795` fills it in: `PageLM` is NON-COMMERCIAL and its licence heads a section *"Prohibition on Redistribution"* — it cannot be in a client deliverable in any form, and its licence opens with the canonical MIT grant sentence verbatim before narrowing it (`T908`).** 🟡 `caliper-spec` is implementable but not redistributable; IMS is *"the sole arbitrator of compliance"* |

## Counts

| | Count |
|---|---|
| Foundational repos with a byte-verified grant | **53** (was 48) |
| 🟢 **Permissive** (MIT · Apache-2.0 · BSD-3 · ECL-2.0 · **BSL-1.0**) | **29** (was 24) |
| 🔴 Copyleft (GPL · AGPL · LGPL) | **20** |
| 🟡 EUPL-1.2 | **3** |
| 🟢 **BSL-1.0 (Boost)** — new family this pass | **1** |
| 🔴 Not open source (proprietary · NonCommercial · split · bespoke) | **5** — 🟢 **`1` fewer: `nextSIS` is GPL-3.0, corrected this pass** |
| 🟢 **CC0-1.0** — new family this pass (`awesome-ia-sala-de-aula`), the most permissive grant in this base | **1** |
| 🟢 Permissive repos with a **first-layer** dependency audit | **4 of 53** — `nbgrader` 🟢, `OATutor` 🟢, `Kolibri` 🟡, `Oppia` 🔴 |
| 🟢 Permissive repos with a **second-layer** dependency audit | **1 of 53** — `nbgrader` 🟡 (`65` transitive packages, `2` weak-copyleft) |
| Dead addresses previously corrected to a live canonical owner | **4** — `tsugi/tsugi`→`csev/tsugi`, `openedx/openassessment`→`openedx/edx-ora2`, `mahara/mahara`→`MaharaProject/mahara`, `openedx/tutor`→`overhangio/tutor` |
| 🟢 Controls reproduced exactly before any verdict shipped | **10 of 10** (`p790`) · `3` planted negatives DEAD · 🔴 `7` defects found by those controls, `0` by inspection |

🔴 **Declared gaps added by `p790`:** the `jinlize-tech` set is **sampled, not swept** — `100` of its
`132` repositories were read for an SPDX id on the *claim* channel and only **`2` on the byte
channel**, so licence-byte agreement across the set is inferred from two identical shas
(`cfc7749b96f6`), not proven (`ACTION p790-D`). And `oppia/oppia`'s transitive closure is **still
unmeasured** while it remains the repository this base tells clients to embed and carries a known
layer-1 **AGPL-3.0** package (`ACTION p790-A`).

🔴 **Declared gaps on this file:** transitive depth `3+` is **unmeasured by design**; the npm-side
layer-2 graphs (`OATutor` `43` direct, `Oppia` `171` direct) were **not** re-audited this pass, and
Oppia's layer-1 AGPL-3.0 finding already governs that decision; and these are **declared ranges
from registry metadata, not resolved versions from a lockfile**, so a client's actual tree may differ.

🔴 **Still grant-less after a re-probe with this pass's variant-tolerant, locale-safe,
any-depth-title gate:** [`formalms/formalms`](https://github.com/formalms/formalms) `446a77a9b9cb`,
[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) `8348cd069aa2`,
[`nestauk/skills-taxonomy-v2`](https://github.com/nestauk/skills-taxonomy-v2) `9e30d89157f7`,
[`Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider`](https://github.com/Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider) `59da726edd9b`.
🟢 **The improved gate rescued 8 other rows and did not rescue these four, which strengthens rather
than weakens the verdict:** they are not misread translations or short grants, they serve no licence
at all. 🔵 The deliverable is an upstream licence request, not a permanent exclusion — and
`SakaiXAPI-Provider` is worth asking for, because it is the Apereo bridge between the one
permissively-granted university LMS and the one permissively-granted learning-record store.
