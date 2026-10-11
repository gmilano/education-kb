# `p125-retraction-cue` — ACTION AF, AG, AH, AI

**Pass 125 — 2026-10-11.** Twelfth pass of this date (census window **11:0x → 11:1x UTC**).

`./test_p125.sh` — **52 passed / 0 failed**, fully offline, no network and no clock, over 25
fixtures. Every licence fixture is a real file from a real repository, and every markdown fixture
is a real construction copied off this KB's own live pages.

## What p124 pre-registered, and what happened

| action | clause (verbatim from p124) | verdict |
|---|---|---|
| `ACTION AF` | cover correction forms 4–8. *Refuted if fewer than 20 of the 27 outstanding violations are resolved by it* | 🟢 **DISCHARGED, NOT REFUTED, IMPLEMENTED — 40 of 61 resolved; 81 rows marked** |
| `ACTION AG` | no licence token may be read without reading what SCOPES it. *Refuted if the check does not independently reproduce all four known instances* | 🟢 **DISCHARGED, NOT REFUTED — 4 of 4, plus 4 further instances** |
| `ACTION AH` | complete `ACTION AA`'s token sets; read a bulleted per-file exception list as a sequence of bindings. *Refuted if fewer than 3 further tokens are recovered on `anki`* | 🟢 **DISCHARGED, NOT REFUTED — 4 recovered** |
| `ACTION AI` | the `MAIN-ONLY` false-permissive question over all 86 non-standard-default addresses. *Refuted if `learnosity-qti` is the only such address in the corpus* | 🔴 **DISCHARGED, REFUTED — it is the only one: 1 of 86** |

## 🔴 `P125-H` — an assertion run without its domain

p124's `ACTION AC` enforces one rule: *a repair must be a SEARCH, not an edit.* For every repaired
`(address, superseded token)`, no page may carry that token on a line naming that address outside
a marked span. p124 discharged it at **27 violations over 15 addresses**, read all 27 by hand, and
reported **zero** live false claims.

**Re-derived from p124's own committed code and pages, the same assertion returns 61 violations
over 23 addresses.** The recogniser was reproduced exactly (`BASE_INLINE`, `BASE_PROSE` in
`correction_form.py`) and so was p124's token vocabulary (`BASE_LICENCE`) and its raw address
match — a violation count is not comparable across vocabularies, so the baseline uses p124's.

| domain | violations | addresses |
|---|---|---|
| the five pages p124 had just marked | **23** | **15** — p124 published 27 / 15 |
| 🔴 all ten live pages | 🔴 **61** | 🔴 **23** |

🔴 **The five it did not reach are `agents/trending.md`, `repos/trending.md`, `intel/trends.md`,
`intel/open-gaps.md` and `README.md`.** The two trending pages are append-only, so a repair is
never permitted to rewrite them and stale tokens necessarily accumulate there — they are the last
place an assertion about stale tokens should omit.

🟢 **The lesson is structural, not a lapse.** p122 found a census less precise than the page it
audited; p123 found a repair that was an edit rather than a search; p124 found a token read
without the clause that scopes it; p125 finds **an assertion run without its domain**. Each
instrument was correct about the thing it measured and silent about the boundary of what it
measured. `test_p125.sh` therefore asserts its own baseline cardinality (`AF.15`) before scoring
anything.

## 🟢 `ACTION AF` — one retraction cue, not thirteen regexes

p124's `ACTION AC` enumerated nine surface forms and reached four. p125 began by writing one
pattern per unreached form and stopped at **thirteen**. Forms 4–8 were the clause; 10–13 were not
known to exist:

| # | form | example | status |
|---|---|---|---|
| 1 | `⚠️ **was X**` bold | `🟢 **Apache-2.0** ⚠️ **was 🔴 GPL-3.0**` | 🟢 p123 |
| 2 | audit-table OLD column | `\| row \| published \| 🔴 actually \|` | 🟢 p124 |
| 3 | prose `was X` + publication reference | *"was 🟢 Apache-2.0 in this page's TOP table"* | 🟢 p124 |
| 9 | NEW column named by its SOURCE | `\| address \| this shelf published \| 🔴 the file says \|` | 🟢 p124 |
| 4 | `⚠️ *was X*` **italic** | `🟢 **BSD-3-Clause** ⚠️ *was MIT (`P121`)*` | 🟢 **p125** |
| 5 | `⚠️ **KB said X**` | `🟢 **MIT** ⚠️ **KB said GPL-3.0**` | 🟢 **p125** |
| 6 | reversed `(New, published Old)` | *"`UniTime/unitime` (Apache-2.0, published GPL-3.0)"* | 🟢 **p125** |
| 7 | `as X not Y` | *"build on it, but as GPL-2.0 not LGPL-3.0"* | 🟢 **p125** |
| 8 | OLD column, NEW cell has **no token** | `\| 🟢 MIT \| 🔴 **NO GRANT** \|`, `🔴 **nothing**`, `🔴 badge reads **"License: Open Source"**` | 🟢 **p125** |
| 10 | 🔴 **`⚠️ was X` with NO emphasis** | `🔴 **GPL-3.0** ⚠️ was Apache-2.0, p117 said AGPL-3.0` | 🟢 **p125 — 19 of the 61, the largest single class** |
| 11 | prose naming a PRIOR PASS's reading | *"`p1040` read Elastic-2.0 …"*, *"an older row on this shelf said AGPL-3 and was superseded"* | 🟢 **p125** |
| 12 | a `P###-x` finding SECTION announcing the correction | the heading quotes the old claim, the body corrects it | 🟢 **p125** |
| 13 | a licence in a **CONTRAST clause** | *"Neither restriction exists under AGPL-3"* | 🟢 **p125 — needs no marker at all** |

🟢 **Enumeration is losing, and form 13 is the proof.** Every pass that writes a correction invents
a spelling, and the sweep chasing it ships a pass later. But a licence token inside a comparison
clause was never a claim about that repository, so marking it would record a correction that never
happened. So the model becomes the two-part rule the rest of this lineage converged on — p123
turned one token into a SET, p124 turned a phrase list into a SHAPE, and p125 turns a form list
into a **CUE plus a SCOPE GATE**. Forms 4, 5 and 10 collapse into one pattern with the asterisks
optional; form 13 is handled by `ACTION AG` rather than by a pattern.

**81 rows marked** across 9 pages; rows carrying the marker **105 → 190**; applying it twice marks
nothing. **40 of the 61 baseline violations resolved** against a clause requiring 20.

### 🔴 Four defects in this action's own first application

| defect | what it did | the rule it became |
|---|---|---|
| a correction table's column mapping **outlived its table** | a header row whose columns `classify_header` cannot read left the PREVIOUS table's mapping in force; the foundational shelf's **live** licence column was marked superseded on [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | a header row — the one directly above a `\|---\|` separator — clears the mapping whether or not it can be read. A mapping that outlives its table is worse than no mapping |
| the marker landed **inside** the emphasis | `⚠️ *was GPL<!--corrected-->*` splits the span the marker closes, so the row read back as unmarked and the assertion re-raised it — 3 rows, all already repaired | the marker moves past any closing `*`/`**` the cue opened |
| `\| \`GPL\` \| 🟢 **GPL-3.0** \|` read as a correction | 20 Moodle-plugin rows marked as repairs that never happened | a bare family token made precise is a **RESOLUTION**. p124's `ACTION AD` resolved 41 bare `CC` grants and called none a correction |
| prose **about** the marker read as a row | *"(`⚠️ **was 🟢 MIT**` inside the cell)"*, *"read *\"⚠️ **was LGPL-3.0**\"*"* | the CUE's own position decides: inside backticks or a quotation it is apparatus. The token's position is not the test — *"🔴 **p123 published `MIT` for the whole repository**"* has the token in backticks and IS a correction |

🔵 **The fourth was found twice.** p124 hit it from the other side — its headline of 94 marked rows
differed from a raw `grep`'s 102 by exactly these lines. And p125 hit it again in the **self-audit
p124 made part of the method**: running the marker over the sections the current pass has just
written. This instrument's own forms table, and its own paragraph on discussion of the marker,
produced **8 false positives across 4 pages**. `APPARATUS` gained the vocabulary of the apparatus
(`FORM n`, `surface form`, `retraction cue`, `marker`, an escaped `\"`), the self-audit now
returns **0**, and `AF.10b` asserts it on a fixture.

🔵 **One case is kept as a judgement rather than a rule.** *"The stale cell's value was
**Apache-2.0**"* is apparatus prose **and** a retraction in its own voice, with the cue unquoted.
It is marked, and `AF.9b` records that reading separately from `AF.9`.

## 🟢 `ACTION AG` — the standing check, and four further instances of its own class

The clause needs the gate to **reproduce** four instances, so each is driven through the **naive
pattern that actually produced the defect**. A gate that can only judge its own matches cannot be
shown to catch anything — and instance 4 exists *only* as a naive span, because this module orders
its alternatives longest-first and so never emits `CC BY` inside `CC BY-SA 4.0`. Hence
`label_span(text, start, end)` takes a raw span rather than a match.

| instance | pass | naive read | label |
|---|---|---|---|
| *"(Some other Free Software Foundation software is covered by the GNU **Lesser** General Public License instead.)"* | p122 | `LGPL` | 🟢 `PREAMBLE` |
| *"'Secondary License' means either the GNU General Public License, Version 2.0, or any later versions"* | p123 | `GPL-2.0` | 🟢 `SECONDARY` |
| *"The text of the Creative Commons public licenses is dedicated to the public domain under the CC0 Public Domain Dedication."* | p124 | `CC0-1.0` | 🟢 `DOCUMENT-TEXT` |
| `\bCC[ -]?BY\b` inside `CC BY-SA 4.0` | p124 | a second licence → a split | 🟢 `SUBSTRING` |

🔴 **p124's own description of its third instance is wrong, and a gate built to that description
finds nothing.** p124 called it *"the CC 4.0 legalcode **recommends** CC0 in its own boilerplate"*.
The file says the licence **text** is CC0-dedicated — a real grant, with a real verb, whose
**subject is the licence document rather than the licensed material**. The label is
`DOCUMENT-TEXT`, not `RECOMMENDATION`, and the distinction is the whole content of the check: the
question is never *"is there a verb?"* but *"what does the verb govern?"*

### The eight labels

`GRANT` is the only one that survives. `PREAMBLE`, `RECOMMENDATION`, `SECONDARY` and `SUBSTRING`
are p124's four; `CONTRAST`, `OUT-OF-TREE` and `DOCUMENT-TEXT` are p125's, and none was
hypothesised — each came from a file.

### 🔴 Four further instances, every one found by this module's own controls

| # | instance | consequence |
|---|---|---|
| 5 | 🔴 **`MIT` matches inside `LIMITED`; `ISC` inside `DISCLAIMED`** | **every BSD-3 and Apache-2.0 warranty disclaimer** yields a spurious `MIT` grant. The `SUBSTRING` check cannot see it — it compares a span against other LICENCE tokens, and `LIMITED` is not one. 🔴 **This was p125's first build: the fifth instance of the class, committed inside the module written to prevent it.** The fix is `\b` around the whole alternation |
| 6 | AGPL-3 **section 13** — *"permission to link or combine any covered work with a work licensed under version 3 of the GNU General Public License"* | **five** spurious `GPL` grants from one AGPL-3 file, enough to make every AGPL-3.0 repository in the corpus read as dual-licensed |
| 7 | AGPL-3's preamble on the **historical Affero GPL** — *"This is a different license, not a version of the Affero GPL"* | two more spurious `GPL` grants from the same file |
| 8 | `ankitects/anki` — *"without the need to license your work under an **AGPL3-compatible** license"* | a compatibility **class** read as a grant (found by `ACTION AH`) |

🔵 **And the test suite committed the same error in one line of itself.** The first form of `AG.9`
was `hasnt … "ISC"` over the whole report, and it failed because **`DISCARDED` contains `ISC`**.
The assertion is now scoped to the control's own row. A test that can commit the defect it checks
for is the sharpest available statement of how ordinary this class of error is.

🟢 **The controls assert an EXACT grant set, not non-emptiness.** p124's `ACTION AE` established
that a model scored only where it cannot fail scores perfectly and means nothing; a control that
asks only *"did it find anything?"* is that same mistake inside a test.

🔵 **One more rule came from a control rather than from design.** The **title line** of a bare
grant file is the grant — `BSD 3-Clause License` followed by a copyright line and the terms, with
no operative verb anywhere. A gate that labels it `PREAMBLE` discards every verb-less licence file
in the corpus. p124's `ACTION AD` reached the same conclusion from the other direction: *title line
first, because it is the only channel the CC0 boilerplate cannot poison.*

## 🟢 `ACTION AH` — `ankitects/anki` is six licences, not two

p124 published it as `AGPL-3.0 + CC-BY-SA` and recorded the set as **partial**. The clause required
3 further tokens; **4** are recovered.

A list distributes one introducing sentence over many items, so no single binding window spans it.
A binding is therefore assembled from **three levels**: the grant verb from the introducing
sentence (*"The following included source code items use a license other than AGPL3:"*), the
directory from a sub-heading (*"In the qt folder:"*), and the artifact and licence from the bullet.

| scope | token | read from |
|---|---|---|
| *(whole repository)* | `AGPL-3.0` | *"Anki is licensed under the GNU Affero General Public License, version 3 or later"* |
| contributed portions | 🆕 **`BSD-3-Clause`** | *"portions contributed by Anki users licensed under the BSD-3 license (see CONTRIBUTORS)"* |
| `pylib/statsbg.py` | 🆕 **`CC-BY-4.0`** | ` * statsbg.py: CC BY 4.0.` |
| `qt/mpv.py`, `qt/winpaths.py`, `qt/jQuery and jQuery-UI`, `qt/plot.js` | 🆕 **`MIT`** | four bullets |
| `qt/MathJax` | 🆕 **`Apache-2.0`** | ` * MathJax: Apache 2.` |
| `qt/protobuf.js` | `BSD-3-Clause` | ` * protobuf.js: BSD 3 clause` — **no trailing period** |
| `docs-site/` | `CC-BY-SA-4.0` | the file's last paragraph |

🔵 **Three things the file names that are not grants over its tree**, each discarded by the gate:
*"Binary distributions also include copies of Qt translation files **(LGPL)**"* → `OUT-OF-TREE`;
*"an **AGPL3-compatible** license"* → `SECONDARY`; *"Anki's translations are **a mix of** BSD and
public domain"* → no single grant for the item, so no binding at all.

🔵 Two spellings cost a fixture each. `jQuery-UI` must not be split at its own hyphen, so the item
separator is a colon or a **spaced** dash; and the long FSF/CC names fold to their abbreviations,
without which `anki` reported a seven-token set where six is the truth.

## 🔴 `ACTION AI` — refuted, and it refutes its own premise too

All **86** non-standard-default addresses were probed on their real default branch and on `main`
and `master` as a guessing probe would request them — **258 probes**, of which **79** find a grant
on the real default, independently reproducing p124's 79 to the row.

| verdict | n | what it means for a studio |
|---|---|---|
| `AGREE` | **77** | `raw.githubusercontent.com` keeps serving a `main`/`master` that still exists even when the repository's *default* has moved, so guessing usually returns the same bytes |
| `BOTH-ABSENT` | 7 | no grant on any of the three branches at any of 14 paths |
| 🔴 **`FALSE-PERMISSIVE`** | 🔴 **1** | [`Learnosity/learnosity-qti`](https://github.com/Learnosity/learnosity-qti): `develop` is **`GPL-2.0`** (18 264 B), `master` is 🟢 **`MIT`** (1 067 B) |
| `GUESS-MISSES-GRANT` | 1 | [`pressbooks/pressbooks`](https://github.com/pressbooks/pressbooks): `dev` is `GPL-3.0`, `main` and `master` both 404 |
| `GUESS-INVENTS-GRANT` | 🟢 **0** | no address where a guess asserts a licence the real default does not grant |

🟢 **The useful part is the direction.** p124 reported `MAIN-ONLY` at 2.5 % on the population where
it can err, counting both failures as one mode. They are not one mode: `pressbooks` returns nothing
where there is something, which costs a shortlist, and `learnosity-qti` returns **permissive** for
a **copyleft** repository, which costs a licence breach. The tiers in `permissiveness.py` order
grants by the duty a studio must accept — public domain, permissive, weak copyleft, strong
copyleft, network copyleft, not open source — so a false-permissive answer is a **lower duty than
the real one**. The rate is **1 of 79 = 1.3 %** where it can err, **1.2 %** across the 86.

🔵 **The clause's premise was that p124's gold set hid the worst case by requiring a grant on the
real default. That is refuted too**: the 7 excluded addresses were probed on 14 paths × 3 branches
and not one has a `main`/`master` grant over a grant-less default.

🟢 **But two of the 7 are not grant-less, and that is a finding about the instrument, not the
shelf.**

| address | the 21-path list requests | the grant actually is |
|---|---|---|
| [`veraPDF/veraPDF-library`](https://github.com/veraPDF/veraPDF-library) | no `LICENSE.GPL`, no `LICENSE.MPL` | 🟡 **dual `GPL-3.0` (35 142 B) + `MPL-2.0` (15 921 B)** on default branch `integration` |
| [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) | no `readme.txt` | 🔴 **`GPL-3.0`** — WordPress plugin header, *"License: GPLv3"* |

🔴 **So "no grant file at 22 probed paths" is a statement about the path list**, and p123's
`ACTION Y` built a *genuinely absent* census on it. 🟢 **Both repositories' real licences were
already correctly recorded on this KB's live pages** — the page is more precise than the census
auditing it, which is `P122-H` for a fourth consecutive pass. The genuinely grant-less set is
**5**, not 7.

## Files

| file | what it does |
|---|---|
| `scope_gate.py` | `ACTION AG`. Eight labels; `label_span` judges a RAW span so naive matches can be scored. Longest-first alternation, `\b`-anchored. |
| `mark_forms.py` | `ACTION AF`. One retraction cue over forms 1–13, the apparatus/quotation test, the resolution rule, header-row mapping reset, emphasis-safe placement. `--apply` is idempotent. |
| `correction_form.py` | Header classification and `norm_token`, plus `BASE_*` — p124's recogniser and vocabulary kept exactly, so the 61→23 baseline is reproduced rather than trusted. |
| `repair_search.py` | The `ACTION AC` assertion, with `--baseline` to run it as p124 ran it. |
| `bullet_bindings.py` | `ACTION AH`. Three-level bindings off a bulleted per-file exception list, every token gated. |
| `permissiveness.py` | `ACTION AI`. Six duty tiers and a title-line-first classifier. |
| `false_permissive.sh` | `ACTION AI`. 258 probes over 86 addresses × 3 branches × 14 paths. |
| `run_ai.py` | Joins the probe rows into `out/ai-verdict.tsv`. |
| `test_p125.sh` | 52 assertions, fully offline. |

🔵 **Channel note.** `raw.githubusercontent.com` is **200** and `git ls-remote --symref` works and
is the only branch source used, so every figure above is read from file bytes rather than from API
metadata. 🔴 **`www.digitaleducationcouncil.com` is unreachable from this environment**
(`ENOTFOUND` via the fetch tool, `CONNECT tunnel failed, response 403` at the agent proxy), which
is why the Digital Education Council faculty-denominator reconciliation stays open — a refusal
with a status, not a gap in the literature.

🔵 **One of p124's figures did not reproduce.** p124 reports the 86 non-standard defaults spread
over **39** distinct branch names; re-derived from p124's own `out/heads-all.tsv` the count is
**37** (`develop` 34, `dev` 11, `v6.2.0` 3, then `trunk`, `java11`, `3.x` and `2.12` with 2 each,
and 30 names with 1). The address count 86 reproduces exactly.

## Pre-registered for p126

🟢 **`ACTION AJ`** — bind a licence token to an ADDRESS, not to a line. All **15** violations
`ACTION AF` newly surfaced share one cause: a cell naming two repositories
(*"`moodle` GPL-3.0 · `canvas-lms` AGPL-3.0"*, *"the spec carries no grant while the validator is
Apache-2.0"*) lets a token co-occur with an address it does not describe. This is p123's row-scope
rule one level finer. 🔴 *Refuted if fewer than 12 of the 15 are explained by mis-binding.*

🟢 **`ACTION AK`** — give the correction apparatus p123's grant-as-a-SET. A correction table that
collapses a split grant into one token ([`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst),
*"published CC-BY-SA-4.0 → corrected MIT"*, where the truth is `MIT` **+** `CC-BY-SA-4.0` on
`docs/`) makes the surviving split member read as superseded on **6** live rows. 🔴 *Refuted if
treating both the old and the new value as SETS does not clear all 6.*

🟢 **`ACTION AL`** — extend the grant path list by the two ecosystem conventions `ACTION AI` found
it blind to (`LICENSE.GPL`/`LICENSE.MPL` dual-licence filenames, and the WordPress `readme.txt`
plugin header) and re-run p123's `ACTION Y` absence census over the full corpus. 🔴 *Refuted if
fewer than 3 of the corpus's "genuinely absent" addresses turn out to carry a grant.*

🟢 **`ACTION AM`** — mark at WRITE time instead of sweeping afterwards. Thirteen surface forms over
four passes is a losing race, and the honest conclusion of `ACTION AF` is that a pass writing a
retraction should emit the marker with it. 🔴 *Refuted if a write-time check cannot reproduce ≥ 90 %
of the 81 rows `ACTION AF` marked this pass.*
