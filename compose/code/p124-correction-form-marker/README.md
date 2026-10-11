# `p124-correction-form-marker` — ACTION AA, AB, AC, AD, AE

**Pass 124 — 2026-10-11.** Eleventh pass of this date (census window **10:0x → 11:3x UTC**).

`./test_p124.sh` — **50 passed / 0 failed**, fully offline, no network and no clock, over 25
fixtures. Every licence fixture is a real file from a real repository, and every markdown fixture
is a real construction copied off this KB's own live pages.

## What p123 pre-registered, and what happened

| action | clause (verbatim from p123) | verdict |
|---|---|---|
| `ACTION AA` | detect a split grant by its SHAPE (a path-scoping noun phrase followed by two licence tokens), not by adding a phrase to a marker list. *Refuted if fewer than 3 addresses change verdict* | 🟢 **DISCHARGED, NOT REFUTED — 4 addresses, all 4 verified by hand** |
| `ACTION AB` | extend the `ACTION V` marker to the other TWO correction forms: the audit-table OLD column and unmarked prose *"was X"*. *Refuted if fewer than 15 rows need it* | 🟢 **DISCHARGED, NOT REFUTED, IMPLEMENTED — 40 rows across 5 files** |
| `ACTION AC` | a repair must be a SEARCH: after repairing an address, assert no page carries its old token outside a marked span. *Refuted if the assertion passes on all 51 already-repaired rows* | 🟢 **DISCHARGED, NOT REFUTED — the assertion FAILS on 27 lines over 15 addresses** |
| `ACTION AD` | resolve the `CC` bucket (41 rows) to a version. *Refuted if fewer than 10 resolve* | 🟢 **DISCHARGED, NOT REFUTED — 41 of 41** |
| `ACTION AE` | build a gold set that CONTAINS branch disagreements, so `MAIN-ONLY` can be scored honestly. *Refuted if fewer than 5 gold rows sit on a non-`main`/`master` default* | 🟢 **DISCHARGED, NOT REFUTED — 79 gold rows** |

Corpus: **1 370** folded addresses off the ten live pages (p123 counted 1 365 — an independent
re-derivation agreeing to 0.4 %), **1 344 EXISTS / 26 ABSENT**, **1 135** grant files read from
each repository's REAL default branch, **86** of which default to neither `main` nor `master`
across **39 distinct branch names** (p123: 84 — agreeing to 2 %).

## 🔴 `P124-H` — the pass's main finding, and it is about this instrument, not this KB

**Every one of the five actions was refuted on its first build, by its own fixtures, and in the
same way: the instrument was less precise than the text it audited.** That is p122's `P122-H` and
p123's `P123-H` recurring for a third consecutive pass — but this pass can say something the
previous two could not, because it caught all five *before* publishing:

| action | what the first build published, and why it was wrong |
|---|---|
| `AD` | **9 of 13** bare-`CC` rows resolved to `CC0-1.0`, including [`openstax/osbooks-college-physics-bundle`](https://github.com/openstax/osbooks-college-physics-bundle), which is `CC-BY-NC-SA-4.0`. The **CC 4.0 legalcode recommends the CC0 Public Domain Dedication in its own boilerplate**, so every CC-BY file on earth contains the string `CC0 Public Domain Dedication`. |
| `AA` | **2 of 6** findings were `CC-BY-SA` files reported as split grants, because `\bCC[ -]?BY\b` matches **inside** `CC BY-SA 4.0` — the hyphen is a word boundary. |
| `AB` | **88 hits, of which 56 were false.** `\bwas\b` in a table header is a **relative pronoun** (*"token that was invisible"*, *"licence, and where it was read"*), and those columns hold LIVE claims. A two-pass table (*"p119 found, by hand \| p120 measured, by instrument \| agrees"*) is a **cross-check**, not a correction. `GPL-3` and `GPL-3.0` are **the same grant**. |
| `AC` | **63 "repaired pairs" and 100+ "violations", every one of which was the KB being RIGHT.** A FORM-1 cell holds the old AND the new value together, so treating the whole cell as marked harvested the *repaired, correct* token as an old one. |
| `AE` | the gold set is the point of the action, and p123 had already named its defect. |

🟢 **The lesson is sharper than "verify first", because three of the five defects are the same
defect.** `AD`'s CC0 boilerplate, `AA`'s hyphen boundary and `AB`'s relative pronoun are all one
error: **a token was read without reading what SCOPES it** — which licence the boilerplate is
recommending rather than granting, which element set the `BY` belongs to, which grammatical role
the `was` is playing. 🔵 **This KB's classifier lineage has been fixing instances of that error
since p122 (GPL-2.0's preamble naming the Lesser GPL, EPL-2.0's secondary-licence clause) and has
never named the class.** `ACTION AG` below makes it a standing requirement rather than a lesson.

## 🟢 `ACTION AA` — the four split grants a marker list could not reach

The detector takes no phrasings. It requires a **binding** — a scope expression, a grant verb and
a licence token in that order inside a window — and declares a split only on **≥ 2 bindings with
≥ 2 distinct scopes AND ≥ 2 distinct licences**. Two scopes under one licence is a scoped single
grant; one scope under two licences is a dual grant where the licensee chooses. Neither is a
split, and both occur in the fixtures.

| address | p123 published | p124 reads, from the file | why it matters |
|---|---|---|---|
| [`Elgg/Elgg`](https://github.com/Elgg/Elgg) (1 677★, `7.x`) | 🟢 `MIT` | 🔴 **`GPL-2.0` + `MIT`** | *"Bundled plugins (the contents of the `/mod` directory) are available only under the GPLv2 license. The remainder of the project is available under either MIT or GPLv2."* The plugin directory of a social-learning platform is GPL-2.0 **only**. |
| [`vieanderes/understory`](https://github.com/vieanderes/understory) | 🟢 `MIT` | 🔴 **`MIT` + `CC-BY-NC-SA-4.0`** | *"This repository has two parts under two licences. 1. Lesson content … CC BY-NC-SA 4.0. 2. Everything else, including source code … MIT."* 🔴 **In an education engagement the lesson content IS the deliverable, and it is NonCommercial.** |
| [`masakhane-io/masakhane-ner`](https://github.com/masakhane-io/masakhane-ner) | 🟢 `Apache-2.0` | 🔴 **`Apache-2.0` + `CC-BY-NC-4.0`** | Apache-2.0 for the code (*"based on the original transformer code by the Hugging Face team"*), and the **African-language NER data** under `Attribution-NonCommercial 4.0 International`. 🔴 The dataset is the asset and it is NonCommercial. |
| [`ankitects/anki`](https://github.com/ankitects/anki) | 🟢 `AGPL-3.0` | 🟡 **`AGPL-3.0` core + named per-file exceptions** | *"with portions contributed by Anki users licensed under the BSD-3 license … The following included source code items use a license other than AGPL3: statsbg.py: CC BY 4.0 … mpv.py: MIT … MathJax: Apache 2 … protobuf.js: BSD 3 clause."* |

🔵 **The detector's SPLIT verdict is right on all four; its token SET is partial on `anki`** — it
reports `AGPL-3.0+CC-BY-SA` and the file also names MIT, Apache-2 and BSD-3 in a bulleted
per-file list the binding window does not span. Recorded as partial rather than published as
complete.

🟢 **Three independent cross-validations.** On [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators),
[`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
and [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) the shape detector finds a
split where p123's marker list also found one — reached by a completely different route, agreeing
on the verdict.

## 🟢 `ACTION AB` — 42 rows marked, and the three header rules that earned it

**42 rows** across 5 files now carry `<!--corrected-->`: **30** audit-table OLD cells and **12**
prose retractions. Marked rows corpus-wide: **52 → 94**.

🔵 **94 ROWS, where a raw `grep` for the marker returns 102.** The 8-line difference is prose
*about* the marker, inside backticks, on these same pages. 🔴 **p122's "57 rows" included 6 such
lines and p124 nearly repeated the error in its own headline**; the figure above counts a table
row carrying the marker, or a prose line whose `was …` span carries it.

Two header rules do most of the work, and both were found by a fixture rather than by design:

- 🟢 **A correction table may carry MORE THAN ONE old column.** This KB writes
  `| row | published p114 / p115 / p116 | 🔴 tree, p117 | published p93–p112 |` — three columns of
  which two are superseded publications. The first build required exactly one and rejected the
  table outright.
- 🟢 **`actually`, not `actual`.** `| row | published | 🔴 actually | what changes for a client |`
  is the header over four rows that invert a commercial answer, and an `\bactual\b` regex misses
  every one of them.

🔴 **And one defect that made FORM-3 structurally blind.** The prose window was
`\bwas\b[^.\n]{0,40}` — `[^.\n]` was meant to stop at a sentence end and also stopped at the dot
in `Apache-2.0`. **So FORM-3 could only ever see version-less tokens, and all 9 of its first
findings were a bare `MIT` or `GPL` for exactly that reason.** A period followed by a digit is a
version, not a full stop; the fix found three more retractions, all three on `Apache-2.0`.

## 🟢 `ACTION AC` — the assertion fails, and WHY it fails is the useful part

**27 violations over 15 addresses.** The clause is discharged and not refuted: a repair in this KB
is still an edit, not a search.

🟢 **But every one of the 27 was read by hand, and ZERO are live false claims.** All 27 are
correction *records* sitting in a surface form the marker does not yet reach. p123's `P123-A`
found two genuine stale claims at this point; p124 finds none, and that is a real improvement in
the KB rather than in the instrument.

🔴 **What the 27 enumerate is that the correction apparatus has at least NINE surface forms, not
the three p123 named:**

| # | form | status | example |
|---|---|---|---|
| 1 | `⚠️ **was X**` (bold) | 🟢 covered by `ACTION V` (p123) | `🟢 **Apache-2.0** ⚠️ **was 🔴 GPL-3.0**` |
| 2 | audit-table OLD column | 🟢 covered by `ACTION AB` (p124) | `\| row \| published \| 🔴 actually \|` |
| 3 | prose `was X` + publication reference | 🟢 covered by `ACTION AB` (p124) | *"was 🟢 Apache-2.0 in this page's TOP table"* |
| 4 | `⚠️ *was X*` — **italic**, not bold | 🔴 **unreached** | `🔴 **proprietary EULA** ⚠️ *was 🟢 MIT*` |
| 5 | `⚠️ **KB said X**` — a different verb | 🔴 **unreached** | `🟢 **MIT** ⚠️ **KB said GPL-3.0**` |
| 6 | prose `(NewLicence, published X)` — reversed order | 🔴 **unreached** | *"`UniTime/unitime` (Apache-2.0, published GPL-3.0)"* |
| 7 | prose `as X not Y` | 🔴 **unreached** | *"build on it, but as GPL-2.0 not LGPL-3.0"* |
| 8 | OLD column whose NEW cell has **no licence token at all** | 🔴 **unreached** | `\| 🟢 MIT \| 🔴 **NO GRANT** \|` |
| 9 | NEW column named by its **source** rather than by a measurement noun | 🟢 **covered — found by self-audit, see below** | `\| address \| this shelf published \| 🔴 the file says \|` |

🟢 **Form 9 was found by running `correction_form.py` against the sections THIS PASS had just
written, and that step is now part of the method.** p124's own new audit tables on
`agents/top.md` and `verticals/solutions.md` head their corrected column *"🔴 the file says"* — a
source, not a measurement noun — so `ACTION AB` did not recognise its own author's table and left
two rows unmarked. 🔴 **Had it shipped, the next census would have raised them as live defects and
spent a pass discovering they were corrections.** `HDR_NEW` now accepts a source-named column, and
the two rows are marked.

🔵 **Form 8 is the interesting one, because it is not a vocabulary problem.** `ACTION AB` requires
a correction to be a PAIR — an old token and a differing new token — and a correction *to nothing*
("no licence file at any of 22 probed paths") has no new token to pair with. The pair rule is what
removed 56 false positives; it is also what makes this class invisible. `ACTION AF` follows.

## 🟢 `ACTION AD` — 41 of 41, and 15 of them forbid a commercial derivative

p123 left **41** readable grants in a bare `CC` bucket. **All 41 resolve**, and the independent
re-derivation landing on exactly 41 is itself a check on both censuses.

| token | rows | commercial use |
|---|---|---|
| `CC-BY-NC-SA-4.0` | **13** | 🔴 **no** |
| `CC0-1.0` | 11 | 🟢 yes — public domain dedication |
| `CC-BY-4.0` | 7 | 🟢 yes, with attribution |
| `CC-BY-SA-4.0` | 6 | 🟡 yes, but the derivative is ShareAlike |
| `CC-BY-SA-3.0` | 2 | 🟡 as above, older text |
| `CC-BY-NC-ND-4.0` | 1 | 🔴 **no, and no derivatives either** |
| `CC-BY-NC-4.0` | 1 | 🔴 **no** |

🔴 **15 of 41 — 37 % of this KB's CC bucket — cannot be used in a commercial deliverable**, and
until this pass all 41 read as the same token. 🟢 **16 further candidates were correctly rejected
as `NOT-CC`** (`GPL-UNTITLED` rows that merely mention Creative Commons).

The channel order is **title line → canonical URL → short token → elements + version read
separately**, and the title line is first because it is the only channel the CC0 boilerplate
cannot poison. Two refinements came from real files: the CC0 legalcode puts `CC0 1.0 Universal` on
its **second** line under a `Creative Commons Legal Code` document header, and
[`azure/moodle`](https://github.com/azure/moodle)'s `LICENSE-DOCS` is served with a **UTF-8 BOM**
that hides the title from a naive first-line read.

## 🟢 `ACTION AE` — `MAIN-ONLY` scored where it CAN fail: 2 of 79

p123 measured `MAIN-ONLY` at **0 % error** and said in the same breath that its gold set could not
see the defect — every gold row's default branch *was* `main` or `master`, so guessing and
resolving agreed by construction. **A model scored only where it cannot fail scores perfectly and
means nothing.**

The complement: **79 gold rows**, each an address whose real default branch is neither `main` nor
`master` and which carries a readable grant there. `MAIN-ONLY` gets **77 right and 2 wrong**.

🟢 **The 77 are a genuine and useful result, not a let-off.** `raw.githubusercontent.com` keeps
serving a `master`/`main` branch that still exists even when the repository's *default* has moved
on, so guessing usually returns the same bytes. 🔴 **Usually is not always, and the 2 failures are
the expensive kind:**

| address | real default | grant there | what guessing returns |
|---|---|---|---|
| [`Learnosity/learnosity-qti`](https://github.com/Learnosity/learnosity-qti) | `develop` | 🔴 **`GPL-2.0`** (18 264 B) | 🟢 **`MIT`** from `master` (1 067 B) |
| [`pressbooks/pressbooks`](https://github.com/pressbooks/pressbooks) | `dev` | 🔴 `GPL-3.0` (`LICENSE.md`) | 🔴 **nothing** — `main` and `master` both 404 |

🔴 **`learnosity-qti` is the finding.** Both files were fetched and read: `master/LICENSE` is the
MIT text, `develop/LICENSE` is GPL-2.0 verbatim. A branch-guessing probe hands a studio the
**permissive** answer for a repository whose current default branch is **copyleft** — the one
direction of error that costs money rather than opportunity. 🟢 **This KB publishes `GPL-2.0` on
`develop` at `repos/trending.md:3720` and is correct**; the defect is in the model, not the shelf.

🔵 **So the honest statement of `MAIN-ONLY`'s error rate is 2.5 % on the population where it can
err, 0.15 % across the whole 1 344-address corpus, and 0 % on the set p123 scored it against** —
three true numbers, of which only the first is useful.

## Files

| file | what it does |
|---|---|
| `split_shape.py` | `ACTION AA`. Scope/grant-verb/licence bindings; a split needs 2 distinct scopes AND 2 distinct licences. |
| `cc_version.py` | `ACTION AD`. Four-channel CC resolution, title line first. |
| `correction_form.py` | `ACTION AB`. Header classification, pair requirement, quotation exclusion; `--apply` emits the marker. Idempotent. |
| `repair_search.py` | `ACTION AC`. Harvests (address, superseded token) from marked spans and asserts no page carries it unmarked. |
| `gold_branch.sh` | `ACTION AE`. Builds the non-`main`/`master` gold set and probes `main`/`master` for comparison. |
| `resolve_head.sh` | Carried from p123 unchanged. `git ls-remote --symref` for existence + default branch. |
| `grant_set.sh` | Carried from p123 unchanged. `ACTION Z`'s grant-as-a-SET reader. |
| `classify_licence.py` | Carried from p123. Token vocabulary unchanged this pass. |
| `run_actions.py` | Runs `AA` and `AD` over the harvested corpus. |
| `test_p124.sh` | 50 assertions, fully offline. |

🔵 **Channel note.** `api.github.com` is **403** to `curl` and `raw.githubusercontent.com` is
**200**, so every figure above is read from file bytes rather than from API metadata.
`git ls-remote --symref` works and is the only branch source used.

## Pre-registered for p125

🟢 **`ACTION AF`** — cover correction forms 4–8 from the `ACTION AC` table: the italic `⚠️ *was X*`
variant, the `KB said X` verb, the reversed `(New, published Old)` prose order, `as X not Y`, and
the pair rule's blind spot where the NEW value is `NO GRANT` rather than a licence token.
🔴 *Refuted if fewer than 20 of the 27 outstanding violations are resolved by it.*

🟢 **`ACTION AG`** — make the shared cause of p122/p123/p124's first-build defects a standing
check: **no licence token may be read without reading what SCOPES it.** Concretely, every token
match must record whether it sits in a granting clause, a recommendation, a preamble, a secondary
-licence clause, or a longer token's substring — and a match in any of the last four is discarded.
🔴 *Refuted if the check does not independently reproduce all four known instances (GPL-2.0
preamble → LGPL, EPL-2.0 secondary → GPL-2.0, CC 4.0 boilerplate → CC0, `CC BY` inside
`CC BY-SA`).*

🟢 **`ACTION AH`** — complete `ACTION AA`'s token sets. The verdict is right on all four addresses
and the set is partial on `ankitects/anki`, whose per-file exceptions sit in a bulleted list no
single binding window spans. Read a bulleted per-file exception list as a sequence of bindings.
🔴 *Refuted if fewer than 3 further tokens are recovered on `anki` alone.*

🟢 **`ACTION AI`** — extend `ACTION AE`'s gold set to the `MAIN-ONLY` **false-permissive** question
specifically: for all 86 non-standard-default addresses, probe whether a surviving `main`/`master`
branch grants a MORE permissive licence than the real default does.
🔴 *Refuted if `learnosity-qti` is the only such address in the corpus.*
