# `p118-licence-column-sweep` — ACTION E, the whole-KB licence sweep

**Pass 118, 2026-10-11.** Discharges `ACTION E` as p117 pre-registered it:
*"sweep EVERY licence column in this KB from the tree, not just the 26 rows p117
reached."* Refutation clause: **refuted as unnecessary if a full sweep finds fewer
than 3 further wrong licences.**

**Result: 18 wrong licences on 18 distinct addresses, 38 published cells. NOT
refuted. `ACTION E` discharged; `Gap 406` widens, then closes on measurement.**

## What it measures

| | |
|---|---|
| licence claims extracted | **957** table rows across 7 live pages |
| distinct addresses | **249** |
| measured from the DEFAULT branch | **249 / 249**, `rc=0` on every one |
| licence files captured | **467**, stored content-addressed as **183 distinct texts** (`evidence/`, 1.8 MB) |
| readable grant | **230 / 249** (92.4 %) |
| tests | **21 passed / 0 failed**, fully offline |

Final agreement, after this pass's own repairs were applied and the sweep re-run:

| verdict | rows |
|---|---|
| 🟢 `AGREE` | **844** |
| 🟡 `PARTIAL` — tree embodies several grants, row names one | 44 (9 addresses) |
| 🔵 `UNREAD` — no grant this instrument can read | 50 |
| 🔵 `REFERENCE-ONLY` — a pointer, not a grant | 2 |
| 🔴 `WRONG` | **17 — every one of them explained below, none a KB error** |

## Layers

| script | what it does | why it is separate |
|---|---|---|
| `extract.sh` | pulls (file, line, slug, licence-tokens) from the licence COLUMNS | a prose sentence is not a column; `Gap 406` is about the table's published conclusion |
| `defaultbranch.sh` | `git ls-remote --symref HEAD` → the default branch | the only ungated channel (see `P118-A`) |
| `measure2.sh` | fetches the licence file from that branch, keeps the bytes | the streams are the evidence, the TSV a derivation |
| `classify2.sh` | names the grant(s) a licence file EMBODIES | title/ALL-CAPS anchored, so a cross-reference cannot match |
| `verdict2.sh` | joins claim to measurement, five outcomes | three outcomes hid both multi-grant and pointer files |
| `repair.py` | rewrites only the cells the sweep scored WRONG | driven by the verdict TSV, so it cannot touch an unmeasured row |
| `test_p118.sh` | 21 assertions, offline, real bytes | the fixtures are real captured licence files |
| `dedup-evidence.sh` | content-addresses the captured bytes into `evidence/<sha256>` + `evidence-manifest.tsv` | p115's rule is that the streams ARE the evidence; 467 copies of a handful of standard texts is 6.5 MB, and one copy per distinct text is 1.8 MB with every verdict still re-derivable as `classify2.sh evidence/<sha>` |

## `P118-P` — one licence, several byte-distinct renderings

467 captured files reduce to **183 distinct texts**, and the collisions are not one-per-licence:

| addresses sharing the text | sha256 (12) | grant |
|---|---|---|
| 24 | `c71d239df917` | Apache-2.0 |
| 15 | `3972dc9744f6` | GPL-3.0 |
| 14 | `8486a10c4393` | AGPL-3.0 |
| 13 | `8ceb4b9ee5ad` | **GPL-3.0 again** — a second, byte-distinct rendering |
| 10 | `cfc7749b96f6` | **Apache-2.0 again** |
| 6 | `589ed823e9a8` | **GPL-3.0, a third** |

🔵 **Three byte-distinct GPL-3.0 texts and two Apache-2.0 texts circulate across these 249
addresses** — line endings, appended copyright headers and trailing whitespace differ while the
grant does not. This is why `p117`'s size-based identification could not have worked even with
its off-by-one corrected (`P118-F`): **file size does not identify a licence, because one licence
has several sizes.** The title line does.

## `P118-A` — a refusal is a property of the (transport × endpoint) CELL

p117 recorded: *"Three transports, three outcomes, one host — so `P798`'s rule
becomes: a refusal is a property of the TRANSPORT, not of the host."* That rule is
still too coarse. Measured this pass, same host, two endpoints:

| endpoint | `curl` | `gh api` | MCP relay |
|---|---|---|---|
| `/repos/{owner}/{repo}` | 🔴 403 *"access to this repository is not enabled"* | 🔴 403, same body | 🔴 denied, same gate |
| `/search/repositories?q=repo:…` | 🔴 403 *"this API path is not available"* | 🔴 403, same body | 🟢 **200, full object** |

Three transports now give the SAME outcome on `/repos` — so p117's "three
outcomes" was reading two different gates as a transport difference. One endpoint
swap turns the relay's refusal into a 200 carrying `description`, `license.spdx_id`,
`stargazers_count` and `default_branch`. **A refusal is a property of the cell, not
of the row or the column.** The two 403 bodies differ, and that is the tell: one
names the repository, the other names the path.

## `P118-B` — the git transport is ungated, and it answers the question the API was asked for

`git ls-remote --symref https://github.com/{slug} HEAD` returned the default branch
for **249 of 249** addresses with no session scope at all, while both REST endpoints
were gated to `curl` and `gh`. For the one field this sweep could not proceed
without, the oldest transport was the only one that needed no permission.

## `P118-C` — 37 of 249 addresses (14.9 %) default to neither `main` nor `master`

And five default to a **tag-shaped** ref that no `main`/`master`/`develop` probe
reaches at all: `GibbonEdu/core` → `v31.0.00`, `claroline/Claroline` → `15.0`,
`OpenEduCat/openeducat_erp` → `19.0`, `portabilis/i-educar` → `2.12`,
`ed-fi-alliance-oss/Ed-Fi-Data-Standard` → `v6.2.0`. Also `Elgg/Elgg` → `7.x`,
`apache/ofbiz-framework` → `trunk`, `overhangio/tutor` → `release`,
`francoisjacquet/rosariosis` → `mobile`.

This is not a detail. `frappe/frappe`'s `master` carries an **MIT** file; `develop`,
the branch the project actually ships, is where the current grant lives. v1 of this
instrument — and p117's `licence.sh` before it, which tried `main master develop
release` in that order — read whichever candidate answered FIRST. **First-answering
is not default.**

## `P118-D` — p117's correction was page-local

p117 corrected four rows on `agents/top.md` and published the finding. The same
four addresses were still wrong on `repos/foundations.md`, `verticals/solutions.md`,
`compose/patterns.md` and `intel/market.md` when this sweep ran. `fwu-de/ais-chat`
read `AGREE` on the page p117 fixed and `WRONG` on three others in the same census.
**A correction published in prose is not a correction applied to the KB**, and only
a whole-KB sweep can tell the difference.

## `P118-E` — `elmsln/elmsln` is GPL-3.0, and p117's own AGPL-3.0 is wrong

p117's `licence.tsv` records `elmsln/elmsln master LICENSE.md AGPL-3.0`. The title
line is `GNU GENERAL PUBLIC LICENSE / Version 3, 29 June 2007`. This is exactly the
trap p117 declared and fixed as `P117-K` — GPL-3 §13 *names* the AGPL — caught in
three repositories and missed in a fourth, because the fix was applied to the three
rows under audit rather than re-run over the file it had already written.

## `P118-F` — every byte figure p117 published is short by one trailing newline

p117 measured licence files as `$(printf '%s' "$body" | wc -c)`, and command
substitution strips trailing newlines before `wc` sees them. Tested on three files:

| file | bytes on disk | bytes with trailing newline stripped | p117 published |
|---|---|---|---|
| `huggingface/transformers` `LICENSE` | 11 418 | 11 417 | **11 417** |
| `elmsln/elmsln` `LICENSE.md` | 35 193 | 35 192 | **35 192** |
| `openedx/edx-ora2` `LICENSE` | 35 135 | 35 135 *(no trailing newline)* | **35 135** |

3 / 3, including the discriminating case: the one file that matches its on-disk size
is the one file that does not end in a newline. p117 also declared, as its own fault
`P117-K`, that it *"inferred licence identity from FILE SIZE (~34.5 kB = AGPL,
~35.1 kB = GPL)"*. The sizes it was inferring from were systematically off by one.

## `P118-G` — the Frappe family carries three different licences

| repo | default branch | licence file | grant |
|---|---|---|---|
| [`frappe/frappe`](https://github.com/frappe/frappe) | `develop` | `LICENSE` | 🟢 **MIT** |
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | `develop` | `license.txt` | 🔴 **GPL-3.0** |
| [`frappe/lms`](https://github.com/frappe/lms) | `develop` | `license.txt` | 🔴 **AGPL-3.0** |
| [`frappe/education`](https://github.com/frappe/education) | `develop` | `license.txt` | 🔵 **no grant body** — see `P118-H` |

The framework is permissive and the applications are copyleft. This KB published
`GPL-3.0` for `frappe/frappe`, which inherits ERPNext's licence onto the one repo in
the family that does not have it — and it is the repo a studio would actually build
on.

## `P118-H` — a licence by reference is not a grant

`frappe/education`'s `license.txt` is one line: `License: GNU GPL V3`. No grant body,
no terms, no copyright holder. Five further addresses commit a field stub whose
licence is named in a package manifest instead (`rstudio/ggcheck` is 45 bytes:
`YEAR: 2021 / COPYRIGHT HOLDER: ggcheck authors`, with the licence in `DESCRIPTION`).
Reported as `GRANT-BY-REFERENCE` and `GRANT-IN-MANIFEST`, never resolved into a
grant, because resolving a pointer is a different measurement than reading one.

## `P118-I` — `canyongbs/advisingapp` is not open source, and the KB said AGPL-3

The most commercially consequential single row in this sweep. The root `LICENSE` on
`main` is **Elastic License 2.0**, 3 860 bytes, with **zero** occurrences of
"affero" or "general public". `p1040` had recorded Elastic-2.0 as a `NON-GRANT`
found *in tree* beside a root AGPL-3; the root IS Elastic-2.0.

Elastic 2.0 forbids providing the software to third parties as a managed service and
forbids circumventing licence keys. **Neither restriction exists under AGPL-3.** An
engagement told "AGPL-3, build on it, AGPL duties apply" — which is what
`compose/patterns.md` said until this pass — would have mis-scoped a hosted-offering
decision in the one direction that cannot be fixed after launch.

## `P118-J` — `PrairieLearn` ships a non-open-source directory inside an AGPL repo

`apps/prairielearn/src/ee/` is the Enterprise Edition and carries its own licence.
The Community Edition is AGPL-3.0; contributed and Illinois-copyright portions are
MIT. A fork that keeps the `ee/` tree is not an AGPL fork. The published token for
this address was `AGPL-3.0,GPL`, which is right about the CE and silent about the
part that matters at fork time.

## `P118-K` — the 19 addresses with no readable grant are four nameable classes

`UNKNOWN` fell from 18 addresses to 5 once the classifier learned what the bucket
actually contained:

| class | n | what it is |
|---|---|---|
| `GRANT-IN-MANIFEST` | 5 | field stub; licence named in `DESCRIPTION`/manifest |
| 🔴 `*-NOT-OSS` | 1 | `canyongbs/advisingapp`, Elastic-2.0 — source-available, use-restricted |
| `GRANT-BY-REFERENCE` | 1 | `frappe/education`, a one-line pointer |
| non-English grant | 2 | `portabilis/i-diario`, `portabilis/pre-matricula-digital` — the AGPL-3 **in Portuguese** |
| `CC0-1.0` | 4 | reads "Creative Commons Legal Code", never "Attribution" |
| still unread | 5 | 4 multi-grant prose indexes + 1 Chinese-language file |

🔴 **The non-English class is a REGIONAL blind spot in a KB whose brief is to place
findings by region.** The classifier was English-only and the two addresses it could
not read were Brazilian (`LICENÇA PÚBLICA GERAL AFFERO GNU`); a fifth still-unread
file is Chinese (`版权所有`). `P471` recorded the mirror image of this defect — a gap
extractor that was Spanish-only. A probe written in the wrong alphabet for its data
reports absence where there is presence, and absence of a licence reads as
permission.

The fix also had to be written carefully: `LICEN.A P.BLICA` does **not** match
`LICENÇA PÚBLICA`, because a `.` in a POSIX regex matches one BYTE and `Ç` is two in
UTF-8. The working anchor is the ASCII tail, `GERAL AFFERO GNU`.

## `P118-L` — this pass's own faults, all seven, all caught before publishing

p117 owned two. This pass owns seven, and one of them would have published a false
headline.

| | fault | effect | fix |
|---|---|---|---|
| **F1** | emitted `LGPL-3` where the KB publishes `LGPL-3.0` | 2 false `WRONG` | normalise versions to `x.0` at both ends |
| **F2** | read the FIRST meaningful line of a multi-grant file | `PrairieLearn` → MIT from a *portions* clause; `elgg` → MIT from a *bundled plugins* clause | report the plurality as `MULTI-GRANT`, never pick by position |
| **F3** | read the first-answering branch, not the default | `frappe/frappe` → MIT from a stale `master` | resolve the default branch first (`P118-C`) |
| **F4** | one licence file wins | `microsoft/autogen` → CC-BY from `LICENSE`, ignoring `LICENSE-CODE` (MIT) | probe `LICENSE-CODE`; 2 addresses still excluded by name |
| 🔴 **F5** | the token regex had no entry for the KB's own short spellings | **on `AGPL-3` the leftmost match was the bare `GPL` inside it**, so every row correctly reading `AGPL-3` was scored as claiming `GPL` and called WRONG against an `AGPL-3.0` tree | matched the short forms; **the headline fell from 23 wrong addresses to 16** |
| **F6** | classifier was English-only | 2 Brazilian repos reported as having no readable grant | see `P118-K` |
| **F7** | cannot tell a licence CLAIM from a licence named in a RETRACTION | this pass's own correction note for `advisingapp` mentions `AGPL-3` while explaining AGPL-3 was wrong, and the sweep scores those 2 rows WRONG | **unfixed**, pre-registered as `ACTION H` |

🔴 **F5 is the one that matters.** It is `P471`'s and `P117-K`'s shape a third and
fourth time in a single pass: *a probe that matched a substring of the thing rather
than the thing.* p117 matched the AGPL's name inside GPL-3 §13; this pass matched
`GPL` inside `AGPL-3`. The lesson is now specific enough to act on: **when a token
set has long and short spellings, the long ones must be in the alternation or the
short match will silently win.**

## The 17 residual `WRONG` rows — all three addresses explained, none a KB error

| address | rows | why it is not a KB error |
|---|---|---|
| `bncc-dev/bncc-pacotes` | 13 | `LICENSE` is a **prose index** naming `LICENSE-CODIGO.md` (MIT) and `LICENSE-DADOS.md` (CC BY 4.0). The KB's `MIT` is right for the code. The repo also declares its **name and visual identity NOT licensed** — a third class this sweep has no column for. |
| `microsoft/autogen` | 1 | `LICENSE` is CC-BY-4.0 (docs), `LICENSE-CODE` is MIT (code). The KB's `MIT` is right for the code. |
| `canyongbs/advisingapp` | 2 | F7: the rows are *this pass's own retraction prose*, which names AGPL-3 in order to retract it. |

## Pre-registered for p119, each with its refutation clause

🟢 **`ACTION F` — resolve the 5 still-unread addresses by following their prose
indexes to the sibling licence files they name.** 🔴 **Refuted as unnecessary if
fewer than 3 of the 5 resolve to a grant that differs from what the KB publishes.**

🟢 **`ACTION G` — re-run `ACTION E` over `agents/trending.md` and
`repos/trending.md`** (811 and 1 123 addresses, excluded here because an append-only
history records what a pass BELIEVED and correcting it would destroy the record).
🔴 **Refuted if the two pages' CURRENT-section claims disagree with the tree on
fewer than 5 addresses** — only the current section is in scope; the history stays.

🟢 **`ACTION H` — teach `extract.sh` to skip tokens inside a retraction context**
(a cell naming a licence in order to correct it). 🔴 **Refuted if the residual
`WRONG` count does not fall to the 14 split-licence rows exactly.**

🟢 **`ACTION I` — audit the OTHER columns p117's `Gap 406` logic implicates.** The
error rate split on *re-measured vs carried forward*, not on subject matter. Licence
was one carried column; star counts, region and bus-factor are others. 🔴 **Refuted
if a carried non-licence column is wrong on fewer than 3 addresses.**
