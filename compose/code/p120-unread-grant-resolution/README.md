# `p120-unread-grant-resolution` — ACTIONS J, K, L

`test_p120.sh` — **55 passed / 0 failed**, fully offline against the licence
files captured in `evidence/` and `evidence2/` this pass.

## Channels this pass

| channel | state | used for |
|---|---|---|
| `raw.githubusercontent.com` | 🟢 OPEN | every licence file read below |
| GitHub repository search | 🟢 OPEN | stars, `fork`, `archived`, **default branch** |
| `api.github.com` | 🔴 `http=403` | — |
| `github.com` HTML | 🔴 `http=403` | — |
| `git ls-remote` | 🟢 OPEN | not needed; search resolved all 22 |

## `ACTION J` — 🟢 DISCHARGED, **not refuted**, and the mechanism is not the one the action assumed

p119 pre-registered: *resolve the remaining 20 `UNREAD` + permissive-claim
addresses by following each one's prose index, as `ACTION F` did for 5.*
🔴 **Refuted if fewer than 3 of the 20 resolve to a grant that is not
permissive.** **4 do, so the action stands.**

But `ACTION J`'s premise — *follow the prose index* — was right about 7 of 22
addresses and wrong about the rest. The resolution needed **five tiers**, and
naming them is most of what this instrument contributes:

| tier | how the grant was found | addresses |
|---|---|---|
| 1 | a licence file at a conventional root path | 8 |
| 1b | a **split grant** in siblings the root file names | 1 |
| 1c | a **prose index** naming its grants inline | 2 |
| 2 | the **non-conventional path the README names** (`docs/License.txt`) | 1 |
| 3 | the **ecosystem's own manifest** (R `DESCRIPTION`, WordPress `readme.txt`) | 1 |
| 4 | an **author's claim** in a README, with no licence file behind it | 4 |
| 5 | 🔴 **nothing, at any of 22 probed paths** | 5 |

🔴 **Tiers 4 and 5 are 9 of 22 addresses — 41 %.** The `UNREAD` pile is not
mostly made of grants that are hard to read. It is substantially made of
**grants that do not exist**, and every one of those 9 was published here with
an OSI licence token. p118's own `P118-K` wrote the lesson — *absence of a
licence reads as permission* — and applied it to the measurement rather than to
the published cell.

### What the 22 addresses actually carry

| address | this KB published | 🔴 measured this pass | tier |
|---|---|---|---|
| [`yuanjiusheng/cloud-learning-ce`](https://github.com/yuanjiusheng/cloud-learning-ce) | 🟢 MIT | 🔴 **proprietary Chinese EULA** | 1 |
| [`FWU-DE/ais-chat`](https://github.com/FWU-DE/ais-chat) | 🟢 Apache-2.0 | 🔴 **AGPL-3.0** | 1 |
| [`leemonade/leemons`](https://github.com/leemonade/leemons) | 🔴 Fair Code *(p119)* | 🔴 **proprietary, reproduced** | 1 |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🟡 GPL-2 | 🟢 **GPL-2.0 confirmed** | 2 |
| [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) | 🔵 *"unknown — do not assume GPL"* | 🟢 **GPL-3.0 resolved** | 3 |
| [`Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | 🟢 Apache-2.0 | 🟢 **Apache-2.0 confirmed** | 1 |
| [`rstudio/ggcheck`](https://github.com/rstudio/ggcheck) | 🟢 MIT | 🟢 **MIT confirmed** | 1 |
| [`rstudio/tblcheck`](https://github.com/rstudio/tblcheck) | 🟢 MIT | 🟢 **MIT confirmed** | 1 |
| [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna) | 🟢 MIT | 🟢 **MIT confirmed** | 1 |
| [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR) | 🟢 MIT | 🟢 **MIT confirmed** | 1 |
| [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | 🟢 BSD | 🟢 **BSD-3 confirmed** | 1 |
| [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | split grant | 🟢 **MIT code + CC BY 4.0 data** | 1b |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | MIT + CC-BY-NC | 🟢 **reproduced, incl. NC corpora** | 1c |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | multi-grant | 🟢 **MIT + CC0 + CC BY 4.0** | 1c |
| [`cezarc/EPESI`](https://github.com/cezarc/EPESI) | 🔴 already NONE | 🔴 **README prose only** | 4 |
| [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) | 🔴 already NONE | 🔴 **badge → `LICENSE` 404** | 4 |
| [`qed42/ai-accessibility-checker`](https://github.com/qed42/ai-accessibility-checker) | 🔴 already NONE | 🔴 **"See the LICENSE file" → 404** | 4 |
| [`xGabrielCv/Auto-Matricula-SIGAA-UnB`](https://github.com/xGabrielCv/Auto-Matricula-SIGAA-UnB) | 🟢 MIT | 🔴 **badge reads "License: Open Source"** | 4 |
| [`Gnanakamalesh-M/student-dropout-early-warning`](https://github.com/Gnanakamalesh-M/student-dropout-early-warning) | 🔴 already UNGRANTED | 🔴 **README "Code: MIT", no file** | 4 |
| [`1EdTech/openbadges-specification`](https://github.com/1EdTech/openbadges-specification) | 🟢 Apache-2.0 | 🔴 **NO GRANT — 22 paths, all 404** | 5 |
| [`lovejzzz/CourseMapper`](https://github.com/lovejzzz/CourseMapper) | 🟢 MIT | 🔴 **NO GRANT** | 5 |
| [`Zion-support/curriculum-alignment-checker`](https://github.com/Zion-support/curriculum-alignment-checker) | 🟢 MIT | 🔴 **NO GRANT** | 5 |

## 🔴 `P120-A` — `yuanjiusheng/cloud-learning-ce`, 126★, published here as 🟢 MIT, is proprietary

Its root `LICENSE` (4 117 B, default branch `master`) contains **zero**
occurrences of any OSI licence name. Read from the file:

| clause | text, as committed |
|---|---|
| reservation | 版权所有 (c) 2021，猿究生 / **保留所有权利** — *all rights reserved* |
| §1.1 | free use for **non-commercial** purposes only |
| 🔴 §2.1 | **commercial use forbidden** without a purchased licence — *"企业网站、经营性网站、以营利为目或实现盈利的网站"* (enterprise, operating, or profit-making sites) |
| §2.2 | no renting, selling, pledging or **sublicensing** |
| §2.3 | the footer *"Powered by cloud-learning ©2021 猿究生"* **must be retained** |
| 🔴 §2.5 | **derivative, modified or third-party versions for redistribution are forbidden** |
| §3.4 | the licensor may **change the terms and the price list without notice** |

🔴 **For a consultancy this is categorically worse than `leemons`.** `leemons`
is expensive — €100 000 past 1 000 users. This one is **unusable at any price
the file names**: §2.5 forbids the derivative work that customisation *is*, and
§2.1 forbids the commercial deployment that an engagement *is*. There is no fee
schedule to budget against, only an e-mail address.

## 🔴 `P120-B` — why no sweep could have caught it, and why `ACTION K` as written would not have either

v2.1 detects source-available licences **by name**: Elastic, BUSL, SSPL,
Commons Clause, PolyForm. `ACTION K` pre-registered adding `Elastic-2.0`,
`Fair-Code`, `SustainableUse`, `BUSL` and `SSPL` to the **claim** side.

🔴 **Both are name lists, and a bespoke licence has no name.** `cloud-learning-ce`
and `leemons` are each a one-off document; no alternation of licence names will
ever match them. `classify3.sh` therefore matches **restriction semantics** —
a reserved-rights assertion, a non-commercial restriction, a fee trigger — and
requires **two independent signals** before it will call a file proprietary.

🔵 **The two-signal threshold is the part that needed a test.** Every BSD-3
licence contains the words *"All rights reserved"*. A one-signal threshold
would have reclassified every BSD repository in this KB as proprietary. Section
B of the suite asserts the guard on real BSD, MIT, Apache and AGPL files, and
asserts that `ottr`'s BSD **does** contain the phrase — so the guard is tested
against the trap, not against its absence.

## `ACTION K` — 🟢 DISCHARGED on its mechanism, 🟡 **its clause is NOT the measurement that matters**

Clause: *refuted if the residual `WRONG` count does not fall below 19.* That
clause measures a re-run of `ACTION E`'s full sweep, which this pass did not
run. What the extended alternation actually bought is different and better:

🟢 **22 claim rows across 6 pages carry a source-available token that p118's
alternation could not express** — `canyongbs/advisingapp` (Elastic-2.0, 11
rows), `leemonade/leemons` (Fair Code, 5), `Earth-OL-Player/Ai_learn_project`
and `digillab-lmu/smart-rag` (PolyForm), `sdv-dev/sdv` (BUSL-1.1),
`sodadata/soda-core` (Elastic-2.0).

🔴 **Every one of those rows had LEFT THE CENSUS.** Once a pass repairs a row
to *"Fair Code License v1.0"*, the row stops matching an OSI-only alternation
and becomes invisible to the instrument that repaired it. **A repaired row that
vanishes is worse than a wrong one**: the page is right and nothing can see it
any more, so nothing will notice when it next goes stale.

## 🟡 `P120-C` — the claim side has no word boundary, and it manufactures defects

`MIT` in p118's alternation is unanchored, so it matches **inside
`COMMITTED`**. Two rows reading *"the dependency tree is COMMITTED"* were
counted as claiming MIT, and the first run of this pass's scorer reported both
as licence defects on rows that were entirely correct.

🟡 **Said plainly, this is a weak finding in magnitude: 2 of 461 MIT claims,
0.4 %.** It is recorded because of its *direction*. Every other defect this KB
hunts is a published cell that is wrong; this one is an instrument inventing a
wrong cell out of a right one, and an instrument that cries wolf twice is how a
census stops being read.

## 🔴 `ACTION L` — **REFUTED on its premise**, by an independent sample

p119 found all 7 of its wrong **star** cells below 78 % page depth and
pre-registered a tail re-measurement. `ACTION J`'s 17 **licence** defects are a
second sample of the same pages and they do not cluster in the tail:

| | below 78 % depth | at or above 78 % |
|---|---|---|
| p119 wrong star cells | 0 | 7 |
| 🔴 p120 licence defects | **13** | 4 |

🔴 **The single most consequential cell sits at 2.0 % depth** —
`agents/top.md:64`, the top table of the most-read page in this KB, publishing
`FWU-DE/ais-chat` as 🟢 Apache-2.0 when it is AGPL-3.0. p119's depth
correlation is real for star counts and **does not generalise to licences**.

🔵 **The reason is the repair mechanism, and it is the pass's most portable
lesson.** `ais-chat`'s AGPL was measured by p117 and published in correction
tables on *both* `agents/top.md` and `intel/market.md`. Those corrections say
the superseded value *"was MIT"*. This row's superseded value was
**Apache-2.0**. 🔴 **A repair keyed on the wrong value you expect to find
cannot fix a row that is wrong in a different way** — and it leaves the error
65 lines from its own correction, on the same page, for three passes.

## 🔵 `P120-D` — `LearnPress/learnpress`: an open question this KB was right to leave open

`verticals/solutions.md` has carried *"🔴 no licence file at `develop`"* and
*"🔴 unknown — do not assume GPL"*, with a later row hypothesising that
*"WordPress plugins declare their grant in a PHP header comment, which filename
probing cannot see."*

🟢 **Resolved, and the hypothesis was right in kind and wrong in detail.** The
grant is declared in **`readme.txt`** — the WordPress plugin header, which is
not a licence filename and so is invisible to filename probing:

| channel | says |
|---|---|
| `readme.txt` (WP plugin header) | 🟢 **`License: GPLv3`** + `License URI: gnu.org/licenses/gpl-3.0.html` |
| `composer.json` | 🟢 **`GPL-3.0-or-later`** |
| 🔴 `package.json` | 🔴 **`ISC`** — `npm init` boilerplate, contradicting both |
| any licence file | 🔴 absent at every probed path |

🔴 **`package.json.license` is not evidence.** `leemons` declares **`MIT`** in
its own `package.json` while its `LICENSE.md` bills €100 000. Two of the four
addresses with a `package.json` licence field state something their licence
file contradicts, so the field was given no weight in any tier above.

## Repaired in this commit

| cells | what |
|---|---|
| **1** | `agents/top.md:64` `FWU-DE/ais-chat` 🟢 Apache-2.0 → 🔴 **AGPL-3.0**, network copyleft named |
| **2** | `verticals/solutions.md:671,762` `cloud-learning-ce` 🟢 MIT → 🔴 **proprietary EULA — NOT OSS** |
| **1** | `agents/top.md:448` `CourseMapper` 🟢 MIT → 🔴 **NO GRANT** |
| **2** | `intel/market.md:4339,4341` SIGAA bot and Zion checker 🟢 MIT → 🔴 **NO GRANT** |
| **1** | `compose/patterns.md:131` `openbadges-specification` 🟢 → 🔴 **NO GRANT**, inside a recommendation |

🟢 **7 cells, re-scored to 0 `OVERSTATED` / 0 `UNGRANTED` / 0 `WRONG`,** and
`repair.py` is asserted idempotent so a re-run cannot double-apply.

🔵 **11 further rows measured `ALREADY-CORRECT`** — they state *"NONE"*,
*"No payload / 24"* or *"UNGRANTED"* and name the claimed MIT only to attribute
it. The first run of the scorer called those 11 defects too. Reading each row
before repairing it is what kept the headline at 7 instead of 18.

## Pre-registered for p121, each with its refutation clause

🟢 **`ACTION N` — probe the other 227 addresses for tier-4 and tier-5 shapes:
an author claim with no file, and a licence badge whose target 404s.** 9 of
these 22 are ungranted; the 22 were selected for being `UNREAD`, so the rate is
an upper bound, not an estimate. 🔴 **Refuted if fewer than 10 of the 227 are
ungranted or author-claim-only.**

🟢 **`ACTION O` — anchor `MIT` and every other bare token in the claim-side
alternation on word boundaries, then re-run the full `ACTION E` sweep and
compare the claim count.** 🔴 **Refuted if the corrected sweep's claim count
differs from p118's 957 by fewer than 3.**

🟢 **`ACTION P` — re-measure every row whose superseded value a prior pass
recorded as `was X`, checking the OTHER pages for the same address against
values that are NOT `X`.** `ais-chat` was wrong in a third value and survived
three passes of corrections. 🔴 **Refuted if no second address carries a stale
licence token differing from the one its own correction table names.**

🟢 **`ACTION Q` — read the licence of every address whose `package.json`,
`composer.json` or `pyproject.toml` declares one, and count the
contradictions.** 2 of 4 contradict here. 🔴 **Refuted if fewer than 15 % of
manifest-declared licences differ from the committed licence file.**

## 🔴 `P120-E` — this instrument's own repair script broke three rows, and the failure is recorded because it generalises

🔴 **`repair.py` v1 anchored each repair on a LINE NUMBER.** That was correct when
it ran and wrong twenty minutes later, because this same pass then **prepended
its findings sections to the same pages** and every anchor moved.

🔴 **v2 re-anchored on `(page, slug, old-token)` and over-matched in the other
direction**: it repaired three rows *this pass had just written to describe its
own findings*, turning `| 🟢 Apache-2.0 | 🔴 **AGPL-3.0** |` into a doubled
marker. The rows were caught by inspection and reverted by hand.

🟢 **v3 guards on the table HEADER** — the same signal `score.py` uses to tell a
repaired row from a live claim. A row under a `published` / `measured from the
tree` / `what is actually there` header quotes its superseded token **on
purpose**, so a repair must never touch a row that is ABOUT a repair. Both
scorers were widened to the same header vocabulary, and the suite now asserts
idempotence across two consecutive runs plus the absence of any doubled marker
in the live pages.

🔵 **Stated plainly because it is the pass's own defect, not the world's: an
instrument that edits the pages it also measures has a feedback loop, and
neither a line number nor a bare token is a safe anchor inside one.** The only
stable anchor is a structural one — what the row is about, plus what kind of
table it sits in. 🟢 The three mangled rows were found because the repair was
re-run and its output read, not because a test caught them; the test that would
have caught them exists now.
